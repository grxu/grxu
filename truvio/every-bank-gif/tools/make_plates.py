"""Build the Step 11 plates and paper cut-outs from the Higgsfield stills.

usage: python3 -I make_plates.py <refs_dir> <out_dir>
Writes plate-T.png, plate-R.png, plate-C.png, file-flat.png, file-fold.png (2048x2048, aligned to T0).
"""
import sys

import cv2
import numpy as np
from scipy import ndimage

refs, out = sys.argv[1], sys.argv[2]

# Sheet + contact shadow footprint on T0, R0 and C0 (all three keep the sheet in the same spot).
SHEET_BOX = (895, 1166, 1162, 1252)  # x0, y0, x1, y1
R0_NUDGE = 12                        # rotunda base sits 12px low against the tower
FLOOR_TOP = 1110                     # just above T0's tower base; shadows are only cut out below it


def load(name):
    return cv2.imread(f'{refs}/{name}.png', cv2.IMREAD_COLOR).astype(np.float32)


def harmonic_fill(img, box, iters=6000):
    """Replace the box with a smooth surface solved from its border (Laplace equation)."""
    x0, y0, x1, y1 = box
    out_img = img.copy()
    patch = img[y0 - 1:y1 + 1, x0 - 1:x1 + 1].copy()
    # Start from a bilinear blend of the border so the solve converges fast.
    top, bot = patch[0], patch[-1]
    t = np.linspace(0, 1, patch.shape[0])[:, None, None]
    patch[1:-1, 1:-1] = ((1 - t) * top + t * bot)[1:-1, 1:-1]
    for _ in range(iters):
        patch[1:-1, 1:-1] = 0.25 * (patch[:-2, 1:-1] + patch[2:, 1:-1] + patch[1:-1, :-2] + patch[1:-1, 2:])
    out_img[y0 - 1:y1 + 1, x0 - 1:x1 + 1] = patch
    return out_img


def remove_sheet(img):
    return harmonic_fill(img, SHEET_BOX)


SLOT_OPENING = (958, 815, 1116, 856)  # inside of C0's yellow recess, inset from its gold bevel


def open_slot(img):
    """Turn C0's solid yellow letterbox panel into a dark opening, keeping the gold bevel, frame and screws."""
    x0, y0, x1, y1 = SLOT_OPENING
    h, w = y1 - y0, x1 - x0
    # Near-black violet just under the top lip, easing a touch lighter toward the bottom.
    t = np.linspace(0, 1, h)[:, None, None]
    top, bottom = np.array([20, 6, 14], np.float32), np.array([46, 22, 36], np.float32)  # BGR
    dark = np.broadcast_to(top * (1 - t) + bottom * t, (h, w, 3))
    mask = np.zeros(img.shape[:2], np.float32)
    mask[y0:y1, x0:x1] = 1
    mask = cv2.GaussianBlur(mask, (5, 5), 0)[..., None]
    fill = img.copy()
    fill[y0:y1, x0:x1] = dark
    return img * (1 - mask) + fill * mask, SLOT_OPENING


def nudge_up(img, px):
    shifted = np.empty_like(img)
    shifted[:-px] = img[px:]
    shifted[-px:] = img[-1:]  # bottom rows are flat violet floor; repeat the last row
    return shifted


def cutout(src, plate, box, fill_sheet_holes=True, crease_y=None):
    """RGBA layer that recreates src when laid over plate: paper at full alpha, shadow as black at partial alpha."""
    x0, y0, x1, y1 = box
    rgba = np.zeros((src.shape[0], src.shape[1], 4), np.float32)
    s, p = src[y0:y1, x0:x1], plate[y0:y1, x0:x1]
    ls, lp = s.mean(2), p.mean(2)
    diff = np.abs(s - p).max(2)
    # Paper is neutral white/grey; the violet floor, its shadows and the blue slit are saturated.
    sat = cv2.cvtColor(np.clip(s, 0, 255).astype(np.uint8), cv2.COLOR_BGR2HSV)[..., 1]
    paper = (diff > 14) & (sat < 70)
    paper = ndimage.binary_opening(paper, iterations=3)
    # The sheet is one piece: keep the largest component, drop tower drift specks.
    lab, n = ndimage.label(paper)
    if n:
        paper = lab == 1 + np.argmax(ndimage.sum(paper, lab, range(1, n + 1)))
    paper = ndimage.binary_closing(paper, iterations=4)
    if fill_sheet_holes:
        paper = ndimage.binary_fill_holes(paper)
    if crease_y is not None:
        # A folded sheet is two flat panels: fill each with its convex hull, so paper standing in
        # front of the white tower (too close in colour to mask) is kept whole.
        cy = crease_y - y0
        filled = np.zeros(paper.shape, np.uint8)
        for part in (slice(0, cy + 3), slice(cy - 3, paper.shape[0])):
            sub = np.zeros_like(paper)
            sub[part] = paper[part]
            pts = cv2.findNonZero(sub.astype(np.uint8))
            if pts is not None:
                cv2.fillConvexPoly(filled, cv2.convexHull(pts), 1)
        paper = filled.astype(bool)
        # Nothing of the sheet sits above its grey band: trim the hull there (drops tower drift).
        grey = (np.abs(ls - 118) < 25) & (sat < 40) & paper
        band_rows = np.where(grey.sum(1) > 120)[0]
        if len(band_rows):
            paper[:band_rows.min()] = False
    soft = cv2.GaussianBlur(paper.astype(np.float32), (3, 3), 0)
    shadow_a = np.clip(1 - ls / np.maximum(lp, 1), 0, 1)
    shadow_a[shadow_a < 0.02] = 0
    shadow_a = np.where(soft > 0, 0, shadow_a)
    # Shadows only land on the violet floor; on the white tower any difference is just drift.
    plate_sat = cv2.cvtColor(np.clip(p, 0, 255).astype(np.uint8), cv2.COLOR_BGR2HSV)[..., 1]
    floor = (plate_sat > 60) & (np.arange(y0, y1)[:, None] >= FLOOR_TOP)
    shadow_a = np.where(floor, shadow_a, 0)
    a = np.maximum(soft, shadow_a)
    colour = np.where(soft[..., None] > 0, s, 0)
    rgba[y0:y1, x0:x1, :3] = colour
    rgba[y0:y1, x0:x1, 3] = a * 255
    return rgba, paper.sum()


def save(name, img):
    cv2.imwrite(f'{out}/{name}', np.clip(img, 0, 255).astype(np.uint8))


t0, r0, c0, t1 = load('T0'), load('R0'), load('C0'), load('T1')

plate_t = remove_sheet(t0)
plate_r = nudge_up(remove_sheet(r0), R0_NUDGE)
plate_c, slot_box = open_slot(remove_sheet(c0))
print('slot panel darkened at', slot_box)

flat, n_flat = cutout(t0, plate_t, SHEET_BOX)
fold, n_fold = cutout(t1, plate_t, (830, 960, 1400, 1300), crease_y=1175)
print('paper pixels: flat', n_flat, 'fold', n_fold)

save('plate-T.png', plate_t)
save('plate-R.png', plate_r)
save('plate-C.png', plate_c)
cv2.imwrite(f'{out}/file-flat.png', np.clip(flat, 0, 255).astype(np.uint8))
cv2.imwrite(f'{out}/file-fold.png', np.clip(fold, 0, 255).astype(np.uint8))

# Round-trip check: cut-out over plate should give back the source.
for name, src, layer in (('flat', t0, flat), ('fold', t1, fold)):
    a = layer[..., 3:] / 255
    comp = layer[..., :3] * a + plate_t * (1 - a)
    err = np.abs(comp - src).mean(2)
    print(f'{name} round-trip mean abs error in its box: {err[960:1300, 830:1400].mean():.2f}')
