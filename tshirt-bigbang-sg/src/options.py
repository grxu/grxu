#!/usr/bin/env python3
"""Build the front-design options from the layouts in ../upload-here/layout-*/.

For each layout PNG (painted on white):
  1. cut the white background out (only white connected to the border, so
     highlights inside petals survive), with clean anti-aliased edges;
  2. soften the generator's straight cut under the top flower group into
     ragged leaf tips;
  3. place the B so its top edge covers the middle of that cut;
  4. export print files to ../print-files/options/ and a mockup to
     ../mockup/options/.

    python3 options.py
"""
import glob
import math
import os
import random

import cairosvg
import numpy as np
from PIL import Image
from scipy import ndimage

import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT_PRINT = os.path.join(ROOT, "print-files", "options")
OUT_MOCK = os.path.join(ROOT, "mockup", "options")
ASSETS = os.path.join(HERE, "assets")


def find_cut(ink):
    """Row of the straight cut (lots of ink just above, none just below) and its columns."""
    rows = ink.sum(1)
    h = ink.shape[0]
    y = max(range(h // 6, h // 2), key=lambda r: rows[r - 3] - rows[r + 3])
    cols = np.where(ink[y - 3] & ~ink[y + 4])[0]
    return y, cols.min(), cols.max()


def cut_out_white(rgb):
    """RGBA with the border-connected white background made transparent."""
    a = rgb.astype(float)
    whiteness = 255 - a.min(2)  # 0 = pure white
    bgish = whiteness < 22
    lab, n = ndimage.label(bgish)
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    # enclosed pockets of paper between leaves count as background too, unless
    # tiny (genuine highlights inside petals)
    sizes = ndimage.sum(bgish, lab, range(1, n + 1))
    min_px = 300 * (rgb.shape[1] / 4096) ** 2
    pockets = {i + 1 for i, sz in enumerate(sizes) if sz >= min_px}
    bg = np.isin(lab, list(border | pockets))
    # soft edge: in a thin band around the background, alpha follows how far
    # the pixel is from white; colour is un-mixed from the white backdrop
    band = ndimage.binary_dilation(bg, iterations=3) & ~bg
    alpha = np.where(bg, 0.0, 1.0)
    alpha[band] = np.clip(whiteness[band] / 60.0, 0, 1)
    rgbf = a.copy()
    m = band & (alpha > 0.02)
    for c in range(3):
        ch = rgbf[..., c]
        ch[m] = np.clip((ch[m] - (1 - alpha[m]) * 255) / alpha[m], 0, 255)
    return np.dstack([rgbf, alpha * 255]).astype(np.uint8)


def soften_cut(rgba, y, x0, x1, seed):
    """Eat back the straight cut with a ragged, feathered edge (leaf-tip-ish)."""
    rnd = random.Random(seed)
    h, w = rgba.shape[:2]
    scale = w / 4096
    phases = [rnd.uniform(0, 2 * math.pi) for _ in range(3)]
    feather = 14 * scale
    xs = np.arange(max(0, x0 - 4), min(w, x1 + 5))
    t = xs * 2 * math.pi / w
    depth = (55 + 28 * np.sin(t * 9 + phases[0]) + 18 * np.sin(t * 23 + phases[1])
             + 10 * np.sin(t * 61 + phases[2]) + np.array([rnd.uniform(-8, 8) for _ in xs])) * scale
    top = y - depth  # ragged edge per column
    y_lo = int(top.min() - feather) - 1
    ys = np.arange(max(0, y_lo), min(h, y + 6))[:, None]
    k = np.clip((top[None, :] - ys) / feather, 0, 1)  # 1 above the ragged edge, 0 below
    a = rgba[..., 3].astype(float)
    a[ys[:, 0][:, None], xs[None, :]] *= k
    rgba[..., 3] = a.astype(np.uint8)
    return rgba


def prepare(src, idx):
    rgb = np.array(Image.open(src).convert("RGB"))
    ink = rgb.min(2) < 225
    y, x0, x1 = find_cut(ink)
    rgba = soften_cut(cut_out_white(rgb), y, x0, x1, seed=idx)
    im = Image.fromarray(rgba)
    out = os.path.join(ASSETS, f"option-{idx}.png")
    im.save(out, optimize=True)
    # where the cut lands on the artboard (same crop/fit as build.watercolour_layer)
    bbox = im.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    bw, bh = bbox[2] - bbox[0], bbox[3] - bbox[1]
    S = 1000
    k = S / max(bw, bh)
    ox, oy = (S - bw * k) / 2, (S - bh * k) / 2
    to_art = lambda px, py: (ox + (px - bbox[0]) * k, oy + (py - bbox[1]) * k)
    (cx0, cy), (cx1, _) = to_art(x0, y), to_art(x1, y)
    return out, cy, (cx0 + cx1) / 2


def main():
    os.makedirs(OUT_PRINT, exist_ok=True)
    os.makedirs(OUT_MOCK, exist_ok=True)
    layouts = sorted(glob.glob(os.path.join(ROOT, "upload-here", "layout-*", "*.png")))
    back = build.back_art()
    for idx, src in enumerate(layouts, start=1):
        png, cut_y, cut_cx = prepare(src, idx)
        S = 1000
        # B height for the current B settings, then put its top just above the cut
        _, (bx0, by0, bx1, by1) = build.text_path(build.SLAB, "B", 1000, 0, 0, build.B_XSCALE)
        b_h = (by1 - by0) * S * build.B_WIDTH / (bx1 - bx0)
        top = cut_y - 0.18 * b_h
        build.EDITED_PNG = png
        build.B_NUDGE = (cut_cx - S / 2, top - (S / 2 - b_h / 2 + 10))
        front = build.front_art()
        fdefs, fbody, fW, fH = front
        base = os.path.join(OUT_PRINT, f"FRONT_option-{idx}_{build.FRONT_MM}x{build.FRONT_MM}mm")
        build.export(build.svg_doc(build.FRONT_MM, build.FRONT_MM, fW, fH, fdefs, fbody), base,
                     build.FRONT_MM, extra_png=build.native_px())
        cairosvg.svg2png(bytestring=build.svg_doc(build.FRONT_MM, build.FRONT_MM, fW, fH, fdefs, fbody,
                                                  bg=build.SHIRT).encode(),
                         write_to=os.path.join(OUT_MOCK, f"option-{idx}_emblem.png"), output_width=1600)
        mock = build.mockup_svg(front, back, annotate=False)
        cairosvg.svg2png(bytestring=mock.encode(), write_to=os.path.join(OUT_MOCK, f"option-{idx}_mockup.png"),
                         output_width=3400)
        print(f"option {idx}: {os.path.relpath(src, ROOT)} cut y={cut_y:.0f} centre x={cut_cx:.0f}")


if __name__ == "__main__":
    main()
