"""Rebuild the BIIIG print art with clean geometry.

The original front-biiig.svg and back-iii.svg are hand traces of a poster, so
their edges wobble and parts that should match don't (left and right III
serifs and slots, the B's top and bottom serifs). This rebuilds them:

- III + circles (back, and the front's red III as an exact scaled copy):
  built from exact geometry, mirrored left to right and top to bottom.
  Square outer corners, equal circles, slots with pointed-arch ends.
- Flames: each keeps its own traced shape, smoothed, with the top and bottom
  tips pinned to the points where the circles cross.
- B and G: traced outlines smoothed between their corners; straight edges
  made straight (and exactly horizontal or vertical). The B's stem piece is
  mirrored top to bottom from its cleaner bottom half.

Everything is built as dense polygons (shapely), then each outline is fitted
back to lines and cubic Béziers, split at its corners.

Usage: python3 rebuild.py traced ../ghost-mannequin/print
"""
import math
import os
import re
import sys

import numpy as np
from shapely import affinity
from shapely.geometry import Point, Polygon
from shapely.ops import unary_union
from svgpathtools import parse_path

SRC, OUT = sys.argv[1:3]
os.makedirs(OUT, exist_ok=True)

BLUE, RED, YELLOW, WHITE = "#0756C6", "#E73A07", "#FDBB05", "#FFFFFF"

# ---- back geometry (units of back-iii.svg) --------------------------------
CX = 960.0                      # centre line
III_L, III_R = 236.0, 1684.0    # outer edges
III_T, III_B = 704.2, 1842.2    # top and bottom
BAR = 156.6                     # bar thickness at the outer edge
STEM_IN = 174.2                 # outer edge -> stem
BRACKET_DROP = 84.5             # bracket height below the bar
SLOT_DX, SLOT_W = 201.0, 106.5  # slot centre offset from CX, slot width
SLOT_TIP, SLOT_SIDE = 880.6, 941.0  # top tip y, where the straight sides start
CIRCLE_R, CIRCLE_DX, CIRCLE_Y = 255.15, 395.0, 335.55
MID_Y = (III_T + III_B) / 2
CORNER_DEG = 40  # a traced joint sharper than this is a real corner


# ---- small helpers ----------------------------------------------------------
def cubic(p0, p1, p2, p3, n):
    t = np.linspace(0, 1, n)[:, None]
    p0, p1, p2, p3 = map(np.asarray, (p0, p1, p2, p3))
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3


def arc(c, r, a0, a1, step=0.3):
    n = max(8, int(abs(a1 - a0) * r / step))
    a = np.linspace(a0, a1, n)
    return np.c_[c[0] + r * np.cos(a), c[1] + r * np.sin(a)]


def circle(cx, cy, r):
    return Polygon(arc((cx, cy), r, 0, 2 * math.pi)[:-1])


def mirror_x(poly, x):
    return affinity.scale(poly, -1, 1, origin=(x, 0))


def mirror_y(poly, y):
    return affinity.scale(poly, 1, -1, origin=(0, y))


def sample_subpath(sp, step=0.5):
    """Dense points along an svgpathtools subpath + indices of corner joints."""
    pts, corners = [], []
    for k, seg in enumerate(sp):
        n = max(2, int(seg.length() / step))
        ts = np.linspace(0, 1, n, endpoint=False)
        if k:
            # Corner if the tangent jumps at this joint.
            a = sp[k - 1].unit_tangent(1)
            b = seg.unit_tangent(0)
            ang = abs(math.degrees(math.atan2((a.conjugate() * b).imag, (a.conjugate() * b).real)))
            if ang > CORNER_DEG:
                corners.append(len(pts))
        else:
            corners.append(0)
        pts.extend((seg.point(t).real, seg.point(t).imag) for t in ts)
    return np.array(pts), corners


def runs_between(pts, corners):
    """Split a closed point loop into open runs between corner indices."""
    corners = sorted(set(corners))
    runs = []
    for i, c in enumerate(corners):
        nxt = corners[(i + 1) % len(corners)]
        if nxt > c:
            runs.append(pts[c:nxt + 1])
        else:
            runs.append(np.vstack([pts[c:], pts[: nxt + 1]]))
    return runs


def resample(run, step):
    d = np.r_[0, np.cumsum(np.hypot(*np.diff(run, axis=0).T))]
    if d[-1] < 1e-9:
        return run
    s = np.linspace(0, d[-1], max(3, int(d[-1] / step) + 1))
    return np.c_[np.interp(s, d, run[:, 0]), np.interp(s, d, run[:, 1])]


def smooth_run(run, sigma, step=0.5):
    """Gaussian-smooth an open run, keeping both end points fixed."""
    run = resample(run, step)
    n = len(run)
    if n < 5 or sigma <= 0:
        return run
    base = run[0] + (run[-1] - run[0]) * np.linspace(0, 1, n)[:, None]
    dev = run - base
    s = sigma / step
    pad = int(3 * s) + 1
    # Odd reflection about the pinned ends keeps them at zero deviation.
    ext = np.vstack([-dev[pad:0:-1], dev, -dev[-2:-pad - 2:-1]]) if n > pad + 2 else None
    if ext is None:
        return run
    k = np.exp(-0.5 * (np.arange(-pad, pad + 1) / s) ** 2)
    k /= k.sum()
    sm = np.c_[np.convolve(ext[:, 0], k, "same"), np.convolve(ext[:, 1], k, "same")][pad:pad + n]
    return base + sm


def is_straight(run, tol):
    a, b = run[0], run[-1]
    L = np.hypot(*(b - a))
    if L < 1e-6:
        return True
    v, w = b - a, run - a
    dev = np.abs(v[0] * w[:, 1] - v[1] * w[:, 0]) / L
    return dev.max() < tol


def faired_ring(sp, sigma, line_tol, extra_corners=(), pins=()):
    """Smoothed dense polygon ring for a traced subpath."""
    pts, corners = sample_subpath(sp)
    for q in extra_corners:  # extra corners given as points near the outline
        corners.append(int(np.argmin(np.hypot(*(pts - q).T))))
    for q, target in pins:   # move the nearest point exactly onto a target
        i = int(np.argmin(np.hypot(*(pts - q).T)))
        pts[i] = target
        corners.append(i)
    out = []
    for run in runs_between(pts, corners):
        if is_straight(run, line_tol):
            a, b = run[0].copy(), run[-1].copy()
            out.append(np.array([a, b]))
        else:
            out.append(smooth_run(run, sigma))
    ring = np.vstack([r[:-1] for r in out])
    return snap_hv(ring)


def snap_hv(ring, deg=3.0):
    """Make near-horizontal / near-vertical straight edges exact."""
    ring = ring.copy()
    n = len(ring)
    for i in range(n):
        a, b = ring[i], ring[(i + 1) % n]
        d = b - a
        L = np.hypot(*d)
        if L < 8:  # only real straight edges (dense curve steps are ~0.5)
            continue
        ang = math.degrees(math.atan2(abs(d[1]), abs(d[0])))
        if ang < deg:
            y = (a[1] + b[1]) / 2
            ring[i][1] = ring[(i + 1) % n][1] = y
        elif ang > 90 - deg:
            x = (a[0] + b[0]) / 2
            ring[i][0] = ring[(i + 1) % n][0] = x
    return ring


# ---- Bézier fitting (Schneider, Graphics Gems 1990) -------------------------
def _bez(ctrl, t):
    t = np.asarray(t)[:, None]
    return ((1 - t) ** 3 * ctrl[0] + 3 * (1 - t) ** 2 * t * ctrl[1]
            + 3 * (1 - t) * t ** 2 * ctrl[2] + t ** 3 * ctrl[3])


def _bez_d(ctrl, t):
    t = np.asarray(t)[:, None]
    return (3 * (1 - t) ** 2 * (ctrl[1] - ctrl[0]) + 6 * (1 - t) * t * (ctrl[2] - ctrl[1])
            + 3 * t ** 2 * (ctrl[3] - ctrl[2]))


def _bez_dd(ctrl, t):
    t = np.asarray(t)[:, None]
    return 6 * (1 - t) * (ctrl[2] - 2 * ctrl[1] + ctrl[0]) + 6 * t * (ctrl[3] - 2 * ctrl[2] + ctrl[1])


def _unit(v):
    n = np.hypot(*v)
    return v / n if n > 1e-12 else v


def _chord_params(p):
    d = np.r_[0, np.cumsum(np.hypot(*np.diff(p, axis=0).T))]
    return d / d[-1]


def _gen_bezier(p, u, t1, t2):
    a1, a2 = u[:, None] * 0 + t1, t2 + u[:, None] * 0
    b = lambda t: np.c_[(1 - t) ** 3, 3 * (1 - t) ** 2 * t, 3 * (1 - t) * t ** 2, t ** 3]
    B = b(u)
    A1 = t1[None, :] * B[:, 1:2]
    A2 = t2[None, :] * B[:, 2:3]
    C = np.array([[np.sum(A1 * A1), np.sum(A1 * A2)], [np.sum(A1 * A2), np.sum(A2 * A2)]])
    tmp = p - (B[:, :1] * p[0] + B[:, 1:2] * p[0] + B[:, 2:3] * p[-1] + B[:, 3:] * p[-1])
    X = np.array([np.sum(A1 * tmp), np.sum(A2 * tmp)])
    det = C[0, 0] * C[1, 1] - C[0, 1] * C[1, 0]
    seg = np.hypot(*(p[-1] - p[0]))
    if abs(det) > 1e-12:
        al = (X[0] * C[1, 1] - X[1] * C[0, 1]) / det
        ar = (C[0, 0] * X[1] - C[1, 0] * X[0]) / det
    else:
        al = ar = seg / 3
    if al < 1e-6 * seg or ar < 1e-6 * seg:
        al = ar = seg / 3
    return np.array([p[0], p[0] + t1 * al, p[-1] + t2 * ar, p[-1]])


def _reparam(ctrl, p, u):
    q = _bez(ctrl, u) - p
    d1, d2 = _bez_d(ctrl, u), _bez_dd(ctrl, u)
    num = np.sum(q * d1, axis=1)
    den = np.sum(d1 * d1, axis=1) + np.sum(q * d2, axis=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        un = np.where(np.abs(den) > 1e-12, u - num / den, u)
    return np.clip(un, 0, 1)


def fit_cubics(p, tol, t1=None, t2=None):
    """Fit points p (open run) with G1 cubic segments within tol."""
    if len(p) == 2:
        d = (p[1] - p[0]) / 3
        return [np.array([p[0], p[0] + d, p[1] - d, p[1]])]
    t1 = _unit(p[min(2, len(p) - 1)] - p[0]) if t1 is None else t1
    t2 = _unit(p[max(-3, -len(p))] - p[-1]) if t2 is None else t2
    u = _chord_params(p)
    ctrl = _gen_bezier(p, u, t1, t2)
    for _ in range(6):
        err = np.hypot(*(_bez(ctrl, u) - p).T)
        if err.max() <= tol:
            return [ctrl]
        u = _reparam(ctrl, p, u)
        ctrl = _gen_bezier(p, u, t1, t2)
    err = np.hypot(*(_bez(ctrl, u) - p).T)
    if err.max() <= tol:
        return [ctrl]
    split = int(np.argmax(err[1:-1])) + 1
    split = min(max(split, 2), len(p) - 3) if len(p) > 5 else len(p) // 2
    tc = _unit(p[split - 1] - p[split + 1])
    return fit_cubics(p[: split + 1], tol, t1, tc) + fit_cubics(p[split:], tol, -tc, t2)


# ---- polygon ring -> SVG path ----------------------------------------------
def ring_corners(ring, win=3.0, thresh=24.0):
    """Indices where the outline turns sharply (measured over +-win units)."""
    n = len(ring)
    ext = np.vstack([ring, ring, ring])
    d = np.r_[0, np.cumsum(np.hypot(*np.diff(ext, axis=0).T))]
    total = d[n]
    idx = np.arange(n, 2 * n)
    j = np.clip(np.searchsorted(d, d[idx] + win), 0, 3 * n - 1)
    k = np.clip(np.searchsorted(d, d[idx] - win, side="right") - 1, 0, 3 * n - 1)
    a = ext[idx] - ext[k]
    b = ext[j] - ext[idx]
    na, nb = np.hypot(*a.T), np.hypot(*b.T)
    ok = (na > 1e-9) & (nb > 1e-9)
    cr = (a[:, 0] * b[:, 1] - a[:, 1] * b[:, 0])
    dt = (a * b).sum(1)
    ang = np.where(ok, np.abs(np.degrees(np.arctan2(cr, dt))), 0)
    corners = []
    for i in np.where(ang >= thresh)[0]:
        lo = np.searchsorted(d, d[i + n] - 2 * win)
        hi = np.searchsorted(d, d[i + n] + 2 * win, side="right")
        neigh = ang[(np.arange(lo, hi) - n) % n]
        if ang[i] >= neigh.max():
            corners.append(int(i))
    # Both ends of a long straight step (an exact line) are corners.
    step = np.hypot(*np.diff(np.vstack([ring, ring[:1]]), axis=0).T)
    for i in np.where(step > 4 * win)[0]:
        corners += [int(i), int((i + 1) % n)]
    # Drop near-duplicates.
    out = []
    for c in sorted(set(corners)):
        if not out or d[c + n] - d[out[-1] + n] > 0.75:
            out.append(c)
    return out


def ring_to_path(ring, tol, line_tol):
    ring = np.asarray(ring)
    if np.allclose(ring[0], ring[-1]):
        ring = ring[:-1]
    corners = ring_corners(ring)
    if not corners:  # a smooth closed loop (circle): split in four
        corners = [0, len(ring) // 4, len(ring) // 2, 3 * len(ring) // 4]
    cmds = [f"M{ring[corners[0]][0]:.2f} {ring[corners[0]][1]:.2f}"]
    for run in runs_between(ring, corners):
        if is_straight(run, line_tol):
            cmds.append(f"L{run[-1][0]:.2f} {run[-1][1]:.2f}")
            continue
        for c in fit_cubics(resample(run, 0.5), tol):
            cmds.append("C" + " ".join(f"{x:.2f} {y:.2f}" for x, y in c[1:]))
    return "".join(cmds) + "Z"


def geom_to_path(g, tol=0.2, line_tol=0.35):
    polys = [g] if g.geom_type == "Polygon" else list(g.geoms)
    out = []
    for p in polys:
        out.append(ring_to_path(np.asarray(p.exterior.coords), tol, line_tol))
        out += [ring_to_path(np.asarray(h.coords), tol, line_tol) for h in p.interiors]
    return "".join(out)


# ---- the III unit -----------------------------------------------------------
def fit_bracket(src):
    """Cubic for the top-left bracket, fitted to the traced one with the end
    tangents forced horizontal (at the bar) and vertical (into the stem)."""
    p0 = np.array([III_L, III_T + BAR])
    p3 = np.array([III_L + STEM_IN, III_T + BAR + BRACKET_DROP])
    best, best_err = None, 1e9
    for a in np.linspace(0.3, 1.0, 36):
        for b in np.linspace(0.3, 1.0, 36):
            c = cubic(p0, p0 + [a * STEM_IN, 0], p3 - [0, b * BRACKET_DROP], p3, 120)
            err = np.mean([np.min(np.hypot(*(c - q).T)) for q in src])
            if err < best_err:
                best, best_err = (a, b), err
    a, b = best
    return cubic(p0, p0 + [a * STEM_IN, 0], p3 - [0, b * BRACKET_DROP], p3, 400)


def iii_unit(bracket):
    """The III: outer outline (mirrored both ways) minus the two slots."""
    def mx(p):
        return np.c_[2 * CX - p[:, 0], p[:, 1]]

    def my(p):
        return np.c_[p[:, 0], 2 * MID_Y - p[:, 1]]

    b = bracket  # (III_L, bar underside) -> (stem, bracket bottom)
    outline = np.vstack([
        [[III_L, III_T], [III_R, III_T]],
        mx(b),                 # top right, outer edge -> stem
        my(mx(b))[::-1],       # bottom right, stem -> outer edge
        [[III_R, III_B], [III_L, III_B]],
        my(b),                 # bottom left, outer edge -> stem
        b[::-1],               # top left, stem -> outer edge
    ])
    body = Polygon(outline).buffer(0)
    # Slots: straight sides with pointed-arch ends (two arcs meeting on the
    # centre line, each tangent to its side).
    a, h = SLOT_W / 2, SLOT_SIDE - SLOT_TIP
    R = (a * a + h * h) / (2 * a)
    def slot(cx):
        ang = math.asin(h / R)
        top = np.vstack([arc((cx - a + R, SLOT_SIDE), R, math.pi, math.pi + ang, step=0.2),
                         arc((cx + a - R, SLOT_SIDE), R, -ang, 0, step=0.2)])
        bottom = np.c_[top[::-1, 0], 2 * MID_Y - top[::-1, 1]]
        return Polygon(np.vstack([top, bottom]))
    slots = [slot(CX - SLOT_DX), slot(CX + SLOT_DX)]
    return body.difference(unary_union(slots))


def circles():
    return unary_union([circle(CX + k * CIRCLE_DX, CIRCLE_Y, CIRCLE_R) for k in (-1, 0, 1)])


def crossings():
    """Top and bottom points where neighbouring circles cross."""
    dy = math.sqrt(CIRCLE_R ** 2 - (CIRCLE_DX / 2) ** 2)
    xs = (CX - CIRCLE_DX / 2, CX + CIRCLE_DX / 2)
    return [((x, CIRCLE_Y - dy), (x, CIRCLE_Y + dy)) for x in xs]


def read_paths(fn):
    s = open(fn).read()
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', s).group(1).split()]
    paths = {m.group(1): parse_path(m.group(2)).continuous_subpaths()
             for m in re.finditer(r'<path id="(\w+)"[^>]* d="([^"]*)"', s)}
    return vb, paths


def write_svg(fn, title, layers, pad=0.0):
    geoms = [g for _, _, g in layers]
    x0, y0, x1, y1 = unary_union(geoms).bounds
    x0, y0, x1, y1 = x0 - pad, y0 - pad, x1 + pad, y1 + pad
    w, h = x1 - x0, y1 - y0
    body = "\n".join(f'  <path id="{i}" fill="{c}" fill-rule="evenodd" d="{geom_to_path(g)}"/>' for i, c, g in layers)
    with open(fn, "w") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.2f} {y0:.2f} {w:.2f} {h:.2f}" '
                f'width="{w:.2f}" height="{h:.2f}">\n<title>{title}</title>\n{body}\n</svg>\n')
    return (x0, y0, w, h)


# ---- back -------------------------------------------------------------------
vb_back, back = read_paths(f"{SRC}/back-iii.svg")
subs = back["white"]
# Traced top-left bracket (two cubics after the left edge) for the fit.
trace_bracket = np.array([(subs[0][k].point(t).real, subs[0][k].point(t).imag)
                          for k in (4, 5) for t in np.linspace(0, 1, 40)])
bracket = fit_bracket(trace_bracket)
iii = iii_unit(bracket)
(cl_top, cl_bot), (cr_top, cr_bot) = crossings()
flames = []
TIP_GAP = 0.3  # flame tips stop this far short of the crossings
for sp, (tip, bot) in ((subs[5], (cl_top, cl_bot)), (subs[4], (cr_top, cr_bot))):
    # Stretch the traced flame evenly so its tips land on the crossings
    # (the rebuilt circles cross ~2.5 units further out than the trace).
    pts, _ = sample_subpath(sp)
    t0, t1 = pts[:, 1].min(), pts[:, 1].max()
    tx = pts[np.argmin(pts[:, 1]), 0]
    k = ((bot[1] - TIP_GAP) - (tip[1] + TIP_GAP)) / (t1 - t0)
    sp = sp.scaled(1, k, complex(tx, t0)).translated(complex(tip[0] - tx, tip[1] + TIP_GAP - t0))
    pts, _ = sample_subpath(sp)
    top_i = pts[np.argmin(pts[:, 1])]
    bot_i = pts[np.argmax(pts[:, 1])]
    ring = faired_ring(sp, sigma=5.0, line_tol=0.0,
                       pins=[(top_i, np.array([tip[0], tip[1] + TIP_GAP])),
                             (bot_i, np.array([bot[0], bot[1] - TIP_GAP]))])
    flames.append(Polygon(ring).buffer(0))
unit = unary_union([iii, circles()]).difference(unary_union(flames))
back_bounds = write_svg(f"{OUT}/back-iii.svg", "BIIIG back - III", [("white", WHITE, unit)])

# ---- front ------------------------------------------------------------------
vb_front, front = read_paths(f"{SRC}/front-biiig.svg")

# Red: the back unit scaled to the traced red III's width, centred on it,
# bottom on the traced baseline.
red_trace = [Polygon(sample_subpath(sp)[0]) for sp in front["red"][:2]]
rx0, _, rx1, ry1 = unary_union(red_trace).bounds
s = (rx1 - rx0) / (III_R - III_L)
red = affinity.scale(unit, s, s, origin=(CX, III_B))
red = affinity.translate(red, (rx0 + rx1) / 2 - CX, ry1 - III_B)

# Blue B: stem piece mirrored from its cleaner bottom half; bowl piece smoothed.
stem_sp, bowl_sp = front["blue"]
stem = Polygon(faired_ring(stem_sp, sigma=6.0, line_tol=1.5)).buffer(0)
sx0, sy0, sx1, sy1 = stem.bounds
smid = (sy0 + sy1) / 2
lower = stem.intersection(Polygon([(sx0 - 5, smid), (sx1 + 5, smid), (sx1 + 5, sy1 + 5), (sx0 - 5, sy1 + 5)]))
stem = unary_union([lower, mirror_y(lower, smid)]).buffer(0.01).buffer(-0.01)
bowl = Polygon(faired_ring(bowl_sp, sigma=14.0, line_tol=1.5)).buffer(0)
blue = unary_union([stem, bowl])

# Yellow G: three pieces, smoothed.
# The big C gets more smoothing: its trace has short flats on the left side.
yellow = unary_union([Polygon(faired_ring(sp, sigma=s_, line_tol=1.5)).buffer(0)
                      for sp, s_ in zip(front["yellow"], (28.0, 14.0, 14.0))])

front_bounds = write_svg(f"{OUT}/front-biiig.svg", "BIIIG front",
                         [("blue", BLUE, blue), ("yellow", YELLOW, yellow), ("red", RED, red)])

print("back viewBox", ["%.2f" % v for v in back_bounds], "was", vb_back)
print("front viewBox", ["%.2f" % v for v in front_bounds], "was", vb_front)
