"""Hand-brushed look for flat vector shapes (used for the piano keys on the back).

Edges get a brush-stroke wobble along the stroke direction and frayed,
dry-brush ends across it; a few thin streaks are cut into the paint. The
result is still pure vector (paths with holes), seeded so it's reproducible.
"""
import math
import random

from shapely.geometry import Polygon
from shapely.ops import unary_union


def _noise(rnd, length, smooth_amp, jag_amp, smooth_wl, jag_step):
    """1-D noise over [0, length]: a few soft waves plus jagged value-noise."""
    waves = [(rnd.uniform(0, 2 * math.pi), smooth_wl / (1.7 ** i), smooth_amp / (1.6 ** i)) for i in range(4)]
    n = int(length / jag_step) + 3
    vals = [rnd.uniform(-1, 1) for _ in range(n)]
    # occasional deep bites, like the brush skipping
    for _ in range(max(1, int(length / (jag_step * 25)))):
        i = rnd.randrange(n)
        vals[i] = rnd.choice([-1, 1]) * rnd.uniform(2.0, 3.5)

    def f(t):
        s = sum(a * math.sin(2 * math.pi * t / wl + p) for p, wl, a in waves)
        x = t / jag_step
        i = int(x)
        fr = x - i
        j = vals[i] * (1 - fr) + vals[min(i + 1, n - 1)] * fr
        return s + jag_amp * j

    return f


def rough_polygon(pts, rnd, step=6.0, side_amp=7.0, end_amp=26.0):
    """Roughen a polygon (clockwise in SVG coords). Vertical edges are treated as
    the brush direction (gentle wobble); horizontal edges as stroke ends (fraying)."""
    out = []
    n = len(pts)
    for k in range(n):
        (x0, y0), (x1, y1) = pts[k], pts[(k + 1) % n]
        dx, dy = x1 - x0, y1 - y0
        L = math.hypot(dx, dy)
        if L == 0:
            continue
        nx, ny = dy / L, -dx / L  # outward for clockwise screen-space polygons
        vertical = abs(dy) > abs(dx)
        if vertical:
            f = _noise(rnd, L, side_amp * 0.25, side_amp * 0.45, L / 2.5, step * 4)
        else:
            f = _noise(rnd, L, end_amp * 0.3, end_amp * 0.6, L / 1.5, step * 3.5)
        # now and then a bigger chunk missing from a long edge, like the brush
        # running dry
        bites = []
        if vertical and L > step * 60 and rnd.random() < 0.45:
            bites.append((rnd.uniform(0.25, 0.85) * L, rnd.uniform(6, 14) * step, rnd.uniform(2.5, 5) * side_amp))
        m = max(2, int(L / step))
        for i in range(m):
            t = L * i / m
            # taper displacement into the corners so edges still meet cleanly
            taper = min(1.0, t / (step * 6), (L - t) / (step * 6))
            d = f(t) * (0.35 + 0.65 * taper)
            d -= sum(a * math.exp(-((t - t0) / w) ** 2) for t0, w, a in bites)
            out.append((x0 + dx * t / L + nx * d, y0 + dy * t / L + ny * d))
    return Polygon(out).buffer(0)


def streaks(rnd, x0, x1, y0, y1, count, max_len, max_w):
    """Thin tapered slivers (dry-brush gaps) running vertically inside a box."""
    shapes = []
    for _ in range(count):
        L = rnd.uniform(0.35, 1.0) * max_len
        w = rnd.uniform(0.35, 1.0) * max_w
        cx = rnd.uniform(x0 + w, x1 - w)
        # streaks hug the stroke ends, where a dry brush breaks up
        top = rnd.random() < 0.5
        sy = y0 + rnd.uniform(-0.05, 0.25) * L if top else y1 - L - rnd.uniform(-0.05, 0.25) * L
        pts = []
        for i in range(13):
            t = i / 12
            half = w / 2 * math.sin(math.pi * t) ** 0.7
            pts.append((cx - half + rnd.uniform(-w * 0.15, w * 0.15), sy + L * t))
        for i in range(12, -1, -1):
            t = i / 12
            half = w / 2 * math.sin(math.pi * t) ** 0.7
            pts.append((cx + half + rnd.uniform(-w * 0.15, w * 0.15), sy + L * t))
        shapes.append(Polygon(pts).buffer(0))
    return unary_union(shapes) if shapes else None


def geom_to_path(geom):
    polys = getattr(geom, "geoms", [geom])
    d = []
    for p in polys:
        if p.is_empty:
            continue
        for ring in [p.exterior, *p.interiors]:
            d.append("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in ring.coords[:-1]) + "Z")
    return "".join(d)


def brushed_keys(polys, seed=7, unit=1.0):
    """Turn clean key polygons into brushed ones. `unit` scales all amplitudes
    (1.0 suits keys ~2000 units tall). Returns (SVG path data per key, bounds)."""
    rnd = random.Random(seed)
    out, geoms = [], []
    for pts in polys:
        g = rough_polygon(pts, rnd, step=6 * unit, side_amp=7 * unit, end_amp=14 * unit)
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        cut = streaks(rnd, min(xs), max(xs), min(ys), max(ys), count=rnd.randint(0, 2),
                      max_len=(max(ys) - min(ys)) * 0.12, max_w=7 * unit)
        if cut is not None:
            g = g.difference(cut)
        out.append(geom_to_path(g))
        geoms.append(g)
    return out, unary_union(geoms).bounds
