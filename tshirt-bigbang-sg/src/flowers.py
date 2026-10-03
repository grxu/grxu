"""Procedural, fully-vector flower illustrations (peony, rose, iris, leaves).

Everything is plain SVG paths + gradients (no filters, no embedded bitmaps),
so the output stays editable in Illustrator / Inkscape / Figma and safe for
print RIP software. Every flower is seeded, so a build is reproducible.
"""
import math
import random


# ---------------------------------------------------------------- colour utils
def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb2hex(c):
    return "#%02x%02x%02x" % tuple(max(0, min(255, round(v))) for v in c)


def mix(a, b, t):
    A, B = hex2rgb(a), hex2rgb(b)
    return rgb2hex([A[i] + (B[i] - A[i]) * t for i in range(3)])


def jitter(col, rnd, amt=10):
    return rgb2hex([v + rnd.uniform(-amt, amt) for v in hex2rgb(col)])


# ---------------------------------------------------------------- geometry
def smoothstep(e0, e1, x):
    t = max(0.0, min(1.0, (x - e0) / (e1 - e0)))
    return t * t * (3 - 2 * t)


def _n(v):
    return f"{v:.1f}"


def cr_closed(pts, k=1 / 6):
    """Closed Catmull-Rom spline through pts -> SVG path data."""
    n = len(pts)
    d = [f"M{_n(pts[0][0])},{_n(pts[0][1])}"]
    for i in range(n):
        p0, p1, p2, p3 = pts[(i - 1) % n], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) * k, p1[1] + (p2[1] - p0[1]) * k)
        c2 = (p2[0] - (p3[0] - p1[0]) * k, p2[1] - (p3[1] - p1[1]) * k)
        d.append(f"C{_n(c1[0])},{_n(c1[1])} {_n(c2[0])},{_n(c2[1])} {_n(p2[0])},{_n(p2[1])}")
    return "".join(d) + "Z"


def cr_open(pts, k=1 / 6):
    pts = [pts[0]] + list(pts) + [pts[-1]]
    d = [f"M{_n(pts[1][0])},{_n(pts[1][1])}"]
    for i in range(1, len(pts) - 2):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[i + 1], pts[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) * k, p1[1] + (p2[1] - p0[1]) * k)
        c2 = (p2[0] - (p3[0] - p1[0]) * k, p2[1] - (p3[1] - p1[1]) * k)
        d.append(f"C{_n(c1[0])},{_n(c1[1])} {_n(c2[0])},{_n(c2[1])} {_n(p2[0])},{_n(p2[1])}")
    return "".join(d)


def ruffle_outline(pts, ts, amp, bumps, rnd, start=0.45):
    """Push outline points along their outward normal to make scalloped edges."""
    n = len(pts)
    phase = rnd.uniform(0, math.pi)
    out = []
    for i, (x, y) in enumerate(pts):
        ax, ay = pts[(i - 1) % n]
        bx, by = pts[(i + 1) % n]
        tx, ty = bx - ax, by - ay
        ln = math.hypot(tx, ty) or 1
        nx, ny = ty / ln, -tx / ln
        u = i / n
        a = amp * smoothstep(start, start + 0.35, ts[i])
        d = a * (0.55 - abs(math.sin(math.pi * bumps * u + phase))) + a * rnd.uniform(-0.15, 0.15)
        out.append((x + nx * d, y + ny * d))
    return out


def petal_pts(L, W, rnd, ruffle=0.0, bumps=3, widest=0.6, fullness=0.6,
              base=0.08, asym=0.0, n=30):
    """Petal in local coords: base at (0,0), tip pointing to (0,-L)."""
    p = math.log(0.5) / math.log(widest)

    def w(t):
        return W / 2 * (base * (1 - t) + (1 - base * (1 - t)) * math.sin(math.pi * t ** p) ** fullness)

    ts = [i / n for i in range(n + 1)]
    left = [(-w(t) + asym * W * t * t, -L * t) for t in ts]
    right = [(w(t) + asym * W * t * t, -L * t) for t in reversed(ts[1:-1])]
    pts = [(0, L * 0.02)] + left + right
    tvals = [0.0] + ts + list(reversed(ts[1:-1]))
    if ruffle:
        pts = ruffle_outline(pts, tvals, ruffle * W, bumps, rnd)
    return pts


def crescent_pts(r, th, a0, a1, rnd, ruffle=0.0, bumps=4, n=26):
    """A cupped inner petal seen from above: a tapered band around the centre."""
    outer, inner = [], []
    phase = rnd.uniform(0, math.pi)
    for i in range(n + 1):
        u = i / n
        a = a0 + (a1 - a0) * u
        tap = math.sin(math.pi * u) ** 0.55
        wob = 1 + ruffle * (0.5 - abs(math.sin(math.pi * bumps * u + phase)))
        ro = r + th * tap * wob
        ri = r - th * 0.22 * tap
        outer.append((ro * math.cos(a), ro * math.sin(a)))
        inner.append((ri * math.cos(a), ri * math.sin(a)))
    return outer + inner[::-1][1:-1]


# ---------------------------------------------------------------- canvas
class Art:
    """Collects <defs> and drawable elements; ids are prefixed per artwork."""

    def __init__(self, prefix):
        self.prefix = prefix
        self.defs = []
        self._n = 0

    def uid(self, kind):
        self._n += 1
        return f"{self.prefix}-{kind}{self._n}"

    def lin(self, stops, x1=0.5, y1=1, x2=0.5, y2=0):
        gid = self.uid("lg")
        s = "".join(f'<stop offset="{o:.3f}" stop-color="{c}" stop-opacity="{a:.2f}"/>' for o, c, a in stops)
        self.defs.append(f'<linearGradient id="{gid}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">{s}</linearGradient>')
        return gid

    def rad(self, stops, cx, cy, r):
        gid = self.uid("rg")
        s = "".join(f'<stop offset="{o:.3f}" stop-color="{c}" stop-opacity="{a:.2f}"/>' for o, c, a in stops)
        self.defs.append(f'<radialGradient id="{gid}" gradientUnits="userSpaceOnUse" '
                         f'cx="{_n(cx)}" cy="{_n(cy)}" r="{_n(r)}">{s}</radialGradient>')
        return gid


def _petal_el(art, pts, x, y, ang, grad, edge, sw, veins=None, vein_col=None, op=1.0):
    tr = f'translate({_n(x)} {_n(y)}) rotate({ang:.1f})'
    out = [f'<path d="{cr_closed(pts)}" transform="{tr}" fill="url(#{grad})" '
           f'stroke="{edge}" stroke-opacity="0.38" stroke-width="{sw:.2f}" stroke-linejoin="round"'
           + (f' opacity="{op:.2f}"' if op < 1 else "") + "/>"]
    if veins:
        out.append(f'<g transform="{tr}" fill="none" stroke="{vein_col}" stroke-opacity="0.16" '
                   f'stroke-width="{sw * 0.7:.2f}" stroke-linecap="round">'
                   + "".join(f'<path d="{v}"/>' for v in veins) + "</g>")
    return out


def _veins(L, W, rnd, count=4, reach=0.75):
    vs = []
    for i in range(count):
        s = (i + 0.5) / count * 2 - 1
        end = (s * W * 0.32 + rnd.uniform(-W * 0.04, W * 0.04), -L * rnd.uniform(reach - 0.15, reach))
        mid = (end[0] * 0.45, -L * 0.35)
        vs.append(cr_open([(s * W * 0.03, -L * 0.06), mid, end]))
    return vs


def _shadow(art, x, y, r, col, strength=0.45):
    g = art.rad([(0.55, col, strength), (1, col, 0)], x, y, r)
    return f'<circle cx="{_n(x)}" cy="{_n(y)}" r="{_n(r)}" fill="url(#{g})"/>'


# ---------------------------------------------------------------- palettes
PALETTES = {
    "crimson": dict(deep="#650a27", mid="#a3173f", light="#d4506f", pale="#eda3b5", shadow="#3a0716"),
    "magenta": dict(deep="#8a0f45", mid="#c81f62", light="#e9709d", pale="#f7b6cd", shadow="#4f0828"),
    "blush":   dict(deep="#b2557f", mid="#de8db0", light="#f4c2d6", pale="#fde6ef", shadow="#6e2a4a"),
    "cream":   dict(deep="#b89b6a", mid="#e3d2ad", light="#f6eedb", pale="#fffaf0", shadow="#6d5a3a"),
    "iris":    dict(deep="#2f4a8f", mid="#6f8fd0", light="#b5c9ee", pale="#e2ebfa", shadow="#1b2c5a"),
    "leaf":    dict(deep="#33502a", mid="#5f8040", light="#9bb66a", pale="#c8d99a", shadow="#1d2e16"),
}


# ---------------------------------------------------------------- flowers
def cupped_bloom(art, cx, cy, R, pal, seed, kind="rose", rot=0.0):
    """Top-down rose / peony: outer radiating petals + cupped crescents inside."""
    rnd = random.Random(seed)
    P = PALETTES[pal] if isinstance(pal, str) else pal
    els = []
    sw = R * 0.010
    peony = kind == "peony"

    def grad_variant(base_t=0.0):
        return art.lin([
            (0.0, jitter(mix(P["deep"], P["mid"], base_t), rnd, 6), 1.0),
            (0.55, jitter(P["mid"], rnd, 8), 1.0),
            (0.9, jitter(P["light"], rnd, 8), 1.0),
            (1.0, P["pale"], 1.0),
        ])

    grads = [grad_variant(t) for t in (0.0, 0.3, 0.6)]
    edge = mix(P["deep"], P["shadow"], 0.3)

    # outer radiating petals (2-3 rings)
    rings = ([(7, 1.0, 0.82), (7, 0.88, 0.78), (6, 0.74, 0.70)] if peony
             else [(5, 1.0, 0.95), (5, 0.86, 0.86)])
    for ri, (cnt, lf, wf) in enumerate(rings):
        off = rot + ri * (180 / cnt) + rnd.uniform(-8, 8)
        for i in range(cnt):
            ang = off + i * 360 / cnt + rnd.uniform(-9, 9)
            L = R * lf * rnd.uniform(0.9, 1.05)
            W = R * wf * rnd.uniform(0.9, 1.1)
            pts = petal_pts(L, W, rnd, ruffle=(0.07 if peony else 0.035), bumps=rnd.choice([2, 3, 4]),
                            widest=rnd.uniform(0.62, 0.72), fullness=0.55, base=0.1,
                            asym=rnd.uniform(-0.08, 0.08))
            els += _petal_el(art, pts, cx, cy, ang + 90, rnd.choice(grads), edge, sw,
                             veins=_veins(L, W, rnd, 5), vein_col=P["deep"])
        els.append(_shadow(art, cx, cy, R * (0.8 - ri * 0.1), P["shadow"], 0.35))

    # cupped crescents spiralling into the centre; the centre drifts a little
    # towards `tilt` so the bloom reads as a 3/4 view rather than a target
    layers = 6 if peony else 7
    r_out = R * (0.52 if peony else 0.6)
    ta = math.radians(rot - 90 + rnd.uniform(-30, 30))
    tilt = R * 0.16
    for k in range(layers):
        f = 1 - k / layers
        r = r_out * f ** 0.95
        ox = cx + math.cos(ta) * tilt * (1 - f)
        oy = cy + math.sin(ta) * tilt * (1 - f)
        th = R * (0.15 if peony else 0.13) * (0.5 + 0.5 * f)
        cg = art.rad([(0.0, P["shadow"], 1), (max(0.01, (r - th * 0.3) / (r + th)), P["deep"], 1),
                      (0.82, P["mid"], 1), (1.0, P["light"], 1)], ox, oy, r + th)
        cnt = 4 if peony else 3
        a_start = rnd.uniform(0, 2 * math.pi)
        for j in range(cnt):
            a0 = a_start + j * 2 * math.pi / cnt + rnd.uniform(-0.35, 0.35)
            span = rnd.uniform(1.5, 2.4) if peony else rnd.uniform(1.9, 2.8)
            rr = r * rnd.uniform(0.9, 1.08)
            pts = crescent_pts(rr, th * rnd.uniform(0.85, 1.15), a0, a0 + span, rnd,
                               ruffle=(0.4 if peony else 0.12), bumps=rnd.choice([3, 4, 5]))
            n_out = len(pts) // 2 + 1
            pts = [(ox + x, oy + y) for x, y in pts]
            els.append(f'<path d="{cr_closed(pts)}" fill="url(#{cg})" stroke="{edge}" '
                       f'stroke-opacity="0.35" stroke-width="{sw:.2f}" stroke-linejoin="round"/>')
            rim = pts[2:n_out - 2]
            els.append(f'<path d="{cr_open(rim)}" fill="none" stroke="{P["pale"]}" stroke-opacity="0.4" '
                       f'stroke-width="{sw * 1.3:.2f}" stroke-linecap="round"/>')
        if k % 2 == 1:
            els.append(_shadow(art, ox, oy, r * 1.05, P["shadow"], 0.3))
    cx, cy = ox, oy

    # heart of the bloom
    hg = art.rad([(0, P["shadow"], 1), (1, P["deep"], 1)], cx, cy, R * 0.07)
    els.append(f'<circle cx="{_n(cx)}" cy="{_n(cy)}" r="{_n(R * 0.06)}" fill="url(#{hg})"/>')
    if peony and pal == "cream":
        # a few golden stamens peeking out
        for i in range(14):
            a = rnd.uniform(0, 2 * math.pi)
            rr = R * rnd.uniform(0.03, 0.11)
            els.append(f'<circle cx="{_n(cx + rr * math.cos(a))}" cy="{_n(cy + rr * math.sin(a))}" '
                       f'r="{_n(R * rnd.uniform(0.012, 0.022))}" fill="{jitter("#e8b84a", rnd, 15)}"/>')
    return els


def iris(art, cx, cy, R, seed, rot=0.0, pal="iris"):
    """Ruffled bearded iris, front view: 3 standards up, 3 falls down."""
    rnd = random.Random(seed)
    P = PALETTES[pal]
    els = []
    sw = R * 0.009
    edge = mix(P["deep"], P["shadow"], 0.2)

    def g():
        return art.lin([(0.0, P["deep"], 1), (0.35, jitter(P["mid"], rnd, 10), 1),
                        (0.8, jitter(P["light"], rnd, 8), 1), (1.0, P["pale"], 1)])

    # standards (behind)
    for ang, lf in ((-90, 0.9), (-132, 0.8), (-48, 0.8)):
        L, W = R * lf, R * 0.52
        pts = petal_pts(L, W, rnd, ruffle=0.16, bumps=7, widest=0.62, fullness=0.5, base=0.15,
                        asym=rnd.uniform(-0.1, 0.1))
        els += _petal_el(art, pts, cx, cy, rot + ang + 90, g(), edge, sw,
                         veins=_veins(L, W, rnd, 5, 0.7), vein_col=P["deep"])
    els.append(_shadow(art, cx, cy, R * 0.55, P["shadow"], 0.4))
    # falls (front, drooping outward), each with a frilly lighter under-layer
    for ang, lf in ((150, 0.95), (30, 0.95), (90, 1.0)):
        L, W = R * lf, R * 0.86
        under = petal_pts(L * 1.03, W * 1.08, rnd, ruffle=0.2, bumps=9, widest=0.66, fullness=0.45,
                          base=0.15, asym=rnd.uniform(-0.1, 0.1))
        ug = art.lin([(0.0, P["mid"], 1), (0.7, P["light"], 1), (1.0, P["pale"], 1)])
        els += _petal_el(art, under, cx, cy, rot + ang + 90 + rnd.uniform(-8, 8), ug, edge, sw)
        pts = petal_pts(L, W * 0.9, rnd, ruffle=0.17, bumps=8, widest=0.6, fullness=0.5, base=0.15,
                        asym=rnd.uniform(-0.12, 0.12))
        els += _petal_el(art, pts, cx, cy, rot + ang + 90, g(), edge, sw,
                         veins=_veins(L, W * 0.9, rnd, 7, 0.62), vein_col=P["shadow"])
        # the "beard": a short soft stripe down the middle of each fall
        a = math.radians(rot + ang)
        beard = [(cx + math.cos(a) * R * t, cy + math.sin(a) * R * t) for t in (0.08, 0.2, 0.34)]
        els.append(f'<path d="{cr_open(beard)}" fill="none" stroke="#f3e2a6" stroke-opacity="0.9" '
                   f'stroke-width="{R * 0.05:.2f}" stroke-linecap="round"/>')
    # style arms in the centre
    for ang in (150, 30, 90):
        L, W = R * 0.32, R * 0.2
        pts = petal_pts(L, W, rnd, ruffle=0.06, bumps=2, widest=0.7, base=0.2)
        gg = art.lin([(0, P["mid"], 1), (1, P["pale"], 1)])
        els += _petal_el(art, pts, cx, cy, rot + ang + 90, gg, edge, sw)
    return els


def leaf(art, x, y, L, ang, seed, pal="leaf", W=None, bend=0.12):
    """Two-tone watercolour leaf. (x,y) is the stem end; ang in degrees, 0 = pointing right."""
    rnd = random.Random(seed)
    P = PALETTES[pal]
    W = W or L * rnd.uniform(0.38, 0.46)
    n = 24
    ts = [i / n for i in range(n + 1)]

    def spine(t):
        return (bend * L * math.sin(math.pi * t) * t, -L * t)

    def w(t):
        return W / 2 * math.sin(math.pi * t ** 0.85) ** 0.8

    left = [(spine(t)[0] - w(t), spine(t)[1]) for t in ts]
    right = [(spine(t)[0] + w(t), spine(t)[1]) for t in ts]
    mid = [spine(t) for t in ts]
    tr = f'translate({_n(x)} {_n(y)}) rotate({ang + 90:.1f})'
    g1 = art.lin([(0, P["deep"], 1), (0.6, jitter(P["mid"], rnd, 8), 1), (1, P["light"], 1)])
    g2 = art.lin([(0, P["mid"], 1), (0.6, jitter(P["light"], rnd, 8), 1), (1, P["pale"], 1)])
    edge = P["shadow"]
    sw = L * 0.008
    els = [f'<g transform="{tr}">',
           f'<path d="{cr_closed(left + mid[::-1][1:-1])}" fill="url(#{g1})" stroke="{edge}" '
           f'stroke-opacity="0.45" stroke-width="{sw:.2f}"/>',
           f'<path d="{cr_closed(right + mid[::-1][1:-1])}" fill="url(#{g2})" stroke="{edge}" '
           f'stroke-opacity="0.45" stroke-width="{sw:.2f}"/>',
           f'<path d="{cr_open(mid[:-2])}" fill="none" stroke="{P["pale"]}" stroke-opacity="0.75" '
           f'stroke-width="{sw * 1.3:.2f}" stroke-linecap="round"/>']
    veins = []
    for i in range(1, 7):
        t = i / 7.5
        sx, sy = spine(t)
        for side in (-1, 1):
            ex = sx + side * w(t + 0.06) * 0.85
            ey = sy - L * 0.07
            veins.append(cr_open([(sx, sy), (sx + side * w(t) * 0.45, sy - L * 0.04), (ex, ey)]))
    els.append(f'<g fill="none" stroke="{P["shadow"]}" stroke-opacity="0.28" stroke-width="{sw * 0.8:.2f}" '
               f'stroke-linecap="round">' + "".join(f'<path d="{v}"/>' for v in veins) + "</g>")
    els.append("</g>")
    return els


def bud(art, x, y, r, ang, seed, pal="magenta"):
    """Small closed bud with two sepals - used as filler."""
    rnd = random.Random(seed)
    P = PALETTES[pal]
    G = PALETTES["leaf"]
    tr = f'translate({_n(x)} {_n(y)}) rotate({ang + 90:.1f})'
    g = art.lin([(0, P["deep"], 1), (0.6, P["mid"], 1), (1, P["light"], 1)])
    gs = art.lin([(0, G["deep"], 1), (1, G["mid"], 1)])
    body = petal_pts(r * 1.6, r * 1.15, rnd, widest=0.45, fullness=0.7, base=0.25)
    s1 = petal_pts(r * 1.2, r * 0.45, rnd, widest=0.35, fullness=0.8, base=0.2)
    return [f'<g transform="{tr}">',
            f'<path d="{cr_closed(body)}" fill="url(#{g})" stroke="{P["shadow"]}" stroke-opacity="0.45" '
            f'stroke-width="{r * 0.04:.2f}"/>',
            f'<path d="{cr_closed(s1)}" transform="rotate(-28)" fill="url(#{gs})"/>',
            f'<path d="{cr_closed(s1)}" transform="rotate(28)" fill="url(#{gs})"/>',
            f'<path d="M0,0 L0,{_n(r * 0.9)}" stroke="{G["deep"]}" stroke-width="{r * 0.12:.2f}" '
            f'stroke-linecap="round"/>',
            "</g>"]
