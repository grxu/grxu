#!/usr/bin/env python3
"""Thank-you card fronts for the BIGBANG Flower Road tee (Floral B).

A6 landscape: 148 x 105 mm trim, 3 mm bleed on every side (154 x 111 mm page).

Writes ../illustrator/:
  option-1_encore_A6.ai / .svg        - black card: Ultra headline, watercolour
                                         flowers resting on piano keys
  option-2_flower-road_A6.ai / .svg   - cream card: hand-lettered headline, a
                                         line-drawn flower road that leads to a
                                         crown lightstick
and ../preview/ PNGs (trimmed, plus a bleed view with the trim line).

The .ai files are PDF-compatible, so Illustrator opens and edits them directly.
The .svg files keep live text and named groups.

    pip install cairosvg pillow
    python3 build.py
"""
import base64
import math
import os
import random

import cairosvg
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ASSETS = os.path.join(HERE, "assets")
OUT_AI = os.path.join(ROOT, "illustrator")
OUT_PREVIEW = os.path.join(ROOT, "preview")

# ---------------------------------------------------------------- SETTINGS
TRIM_W, TRIM_H = 148.0, 105.0   # A6 landscape, mm
BLEED = 3.0                     # mm, every side
HANDLE = "@yourhandle"          # Instagram handle (also editable as live text)

# copy, as approved ("light fix")
HEAD_1 = "Thank you"
HEAD_2 = "for your purchase,"
HEAD_3 = "VIPs!"
BODY = ["We hope this Flower Road-inspired tee",
        "is everything you wished for.",
        "See you at the BIGBANG concert!"]

# palette
SHIRT_BLACK = "#111111"   # the tee
CREAM = "#F5F0E6"
VIP_YELLOW = "#F5C832"    # crown lightstick yellow
YELLOW_LIGHT = "#F8DD7A"
YELLOW_DEEP = "#E0A51C"
INK_BLUE = "#1E3FA0"      # cobalt ink, from the references and the tee's iris
PEONY_PINK = "#F3A9BA"
IRIS_LILAC = "#B9C3F2"
KEY_WHITE = "#F4F1EA"
# ---------------------------------------------------------------- helpers

PAGE_W, PAGE_H = TRIM_W + 2 * BLEED, TRIM_H + 2 * BLEED


def f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def layer(name, body):
    lid = name.lower().replace(" ", "-").replace("(", "").replace(")", "").replace(",", "")
    return (f'<g id="{lid}" inkscape:groupmode="layer" inkscape:label="{name}">\n'
            + "\n".join(body) + "\n</g>")


def svg_doc(title, layers):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
     width="{f(PAGE_W)}mm" height="{f(PAGE_H)}mm" viewBox="0 0 {f(PAGE_W)} {f(PAGE_H)}">
<title>{title}</title>
<g id="trim-origin" transform="translate({f(BLEED)} {f(BLEED)})">
{chr(10).join(layers)}
</g>
</svg>
'''


def text(x, y, s, family, size, fill, weight=400, anchor="start", spacing=0, extra=""):
    ls = f' letter-spacing="{f(spacing)}"' if spacing else ""
    return (f'<text x="{f(x)}" y="{f(y)}" font-family="{family}" font-size="{f(size)}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{ls}{extra}>{s}</text>')


def image(iid, path, x, y, w):
    im = Image.open(path)
    h = w * im.height / im.width
    data = base64.b64encode(open(path, "rb").read()).decode()
    return (f'<image id="{iid}" x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
            f'preserveAspectRatio="none" xlink:href="data:image/png;base64,{data}"/>'), h


def smooth_closed(pts):
    """Catmull-Rom through pts -> closed cubic path."""
    n = len(pts)
    d = f"M{f(pts[0][0])} {f(pts[0][1])}"
    for i in range(n):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{f(c1[0])} {f(c1[1])} {f(c2[0])} {f(c2[1])} {f(p2[0])} {f(p2[1])}"
    return d + " Z"


def smooth_open(pts):
    d = f"M{f(pts[0][0])} {f(pts[0][1])}"
    n = len(pts)
    for i in range(n - 1):
        p0 = pts[i - 1] if i > 0 else pts[i]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < n else pts[i + 1]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{f(c1[0])} {f(c1[1])} {f(c2[0])} {f(c2[1])} {f(p2[0])} {f(p2[1])}"
    return d


def sparkle(cx, cy, s, fill):
    return (f'<path d="M{f(cx)} {f(cy - s)} Q{f(cx)} {f(cy)} {f(cx + s)} {f(cy)} '
            f'Q{f(cx)} {f(cy)} {f(cx)} {f(cy + s)} Q{f(cx)} {f(cy)} {f(cx - s)} {f(cy)} '
            f'Q{f(cx)} {f(cy)} {f(cx)} {f(cy - s)} Z" fill="{fill}"/>')


# ---------------------------------------------------------------- crown lightstick
def lightstick(gid, x, y, height, line="#2B2B2B", handle="#2E2E2E", glow=None, rotate=0):
    """Crown lightstick drawn in a 100-unit-tall box; (x, y) = bottom centre."""
    k = height / 84.0
    sw = 1.6
    st = f'stroke="{line}" stroke-width="{sw}" stroke-linejoin="round"'
    parts = []
    if glow:
        parts.append(f'<circle cx="0" cy="-58" r="34" fill="{glow}" opacity="0.28"/>')
        parts.append(f'<circle cx="0" cy="-58" r="24" fill="{glow}" opacity="0.35"/>')
    # back points
    parts.append(f'<path d="M-15 -36 L-29 -72 L-6 -48 Z" fill="{YELLOW_LIGHT}" {st}/>')
    parts.append(f'<path d="M15 -36 L29 -72 L6 -48 Z" fill="{YELLOW_LIGHT}" {st}/>')
    parts.append(f'<path d="M-9 -52 L0 -66 L9 -52 Z" fill="{YELLOW_DEEP}" {st}/>')
    # front crown
    parts.append(f'<path d="M-17 -36 Q-25 -56 -22 -76 L0 -50 L22 -76 Q25 -56 17 -36 Z" '
                 f'fill="{VIP_YELLOW}" {st}/>')
    # balls
    for bx, by, r in ((-30, -74, 3.4), (30, -74, 3.4), (-22, -79, 3.8), (22, -79, 3.8), (0, -69, 3.2)):
        parts.append(f'<circle cx="{bx}" cy="{by}" r="{r}" fill="#FFFFFF" {st}/>')
    # handle + collar
    parts.append(f'<path d="M-9 -33 L9 -33 L6.5 -5 Q6.5 0 0 0 Q-6.5 0 -6.5 -5 Z" fill="{handle}" {st}/>')
    parts.append(f'<rect x="-19" y="-38" width="38" height="5.5" rx="2.6" fill="#6E6E6E" {st}/>')
    parts.append(f'<rect x="-2.6" y="-27" width="5.2" height="5.6" rx="0.6" fill="{VIP_YELLOW}"/>')
    parts.append('<circle cx="0" cy="-6" r="1.8" fill="#000000" opacity="0.55"/>')
    rot = f" rotate({f(rotate)})" if rotate else ""
    return (f'<g id="{gid}" transform="translate({f(x)} {f(y)}){rot} scale({k:.4f})">'
            + "".join(parts) + "</g>")


# ---------------------------------------------------------------- line-drawn flowers
def leaf(x, y, length, angle, width_ratio=0.38, ink=INK_BLUE, sw=0.45, fill="none"):
    w = length * width_ratio
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(angle)})">'
            f'<path d="M0 0 Q{f(w)} {f(-length * 0.45)} 0 {f(-length)} Q{f(-w)} {f(-length * 0.45)} 0 0 Z" '
            f'fill="{fill}" stroke="{ink}" stroke-width="{sw}" stroke-linejoin="round"/>'
            f'<path d="M0 {f(-length * 0.08)} L0 {f(-length * 0.78)}" stroke="{ink}" '
            f'stroke-width="{f(sw * 0.8)}" stroke-linecap="round" fill="none"/></g>')


def stem(x0, y0, x1, y1, bend, ink=INK_BLUE, sw=0.5):
    mx, my = (x0 + x1) / 2 + bend, (y0 + y1) / 2
    return (f'<path d="M{f(x0)} {f(y0)} Q{f(mx)} {f(my)} {f(x1)} {f(y1)}" fill="none" '
            f'stroke="{ink}" stroke-width="{f(sw)}" stroke-linecap="round"/>')


def rose(cx, cy, r, fill, ink=INK_BLUE, sw=0.5):
    pts = []
    for i in range(40):
        t = i / 40 * 2 * math.pi
        rr = r * (0.9 + 0.1 * abs(math.cos(2.5 * t)))
        pts.append((cx + rr * math.cos(t), cy + rr * math.sin(t) * 0.92))
    spiral = []
    turns = 2.3
    for i in range(70):
        t = i / 69
        a = t * turns * 2 * math.pi + 0.6
        rr = r * (0.08 + 0.68 * t)
        spiral.append((cx + rr * math.cos(a), cy + rr * math.sin(a) * 0.92))
    return (f'<path d="{smooth_closed(pts)}" fill="{fill}" stroke="{ink}" stroke-width="{f(sw)}"/>'
            f'<path d="{smooth_open(spiral)}" fill="none" stroke="{ink}" stroke-width="{f(sw)}" '
            f'stroke-linecap="round"/>')


def peony(cx, cy, r, fill, ink=INK_BLUE, sw=0.5):
    outer, inner = [], []
    for i in range(72):
        t = i / 72 * 2 * math.pi
        outer.append((cx + r * (0.84 + 0.16 * abs(math.sin(4.5 * t))) * math.cos(t),
                      cy + r * (0.84 + 0.16 * abs(math.sin(4.5 * t))) * math.sin(t) * 0.88))
        ri = r * 0.55 * (0.82 + 0.18 * abs(math.sin(3 * t + 0.4)))
        inner.append((cx + ri * math.cos(t), cy - r * 0.06 + ri * math.sin(t) * 0.85))
    dots = "".join(f'<circle cx="{f(cx + r * 0.18 * math.cos(a))}" cy="{f(cy - r * 0.06 + r * 0.15 * math.sin(a))}" '
                   f'r="{f(r * 0.06)}" fill="{ink}"/>' for a in (0.3, 2.2, 4.1))
    return (f'<path d="{smooth_closed(outer)}" fill="{fill}" stroke="{ink}" stroke-width="{f(sw)}"/>'
            f'<path d="{smooth_closed(inner)}" fill="none" stroke="{ink}" stroke-width="{f(sw)}"/>' + dots)


def petal(length, width, angle):
    w = width
    return (f'<path transform="rotate({f(angle)})" d="M0 0 C{f(w)} {f(-length * 0.3)} {f(w * 0.85)} '
            f'{f(-length)} 0 {f(-length)} C{f(-w * 0.85)} {f(-length)} {f(-w)} {f(-length * 0.3)} 0 0 Z"/>')


def iris(cx, cy, size, fill, ink=INK_BLUE, sw=0.5):
    g = (f'<g transform="translate({f(cx)} {f(cy)})" fill="{fill}" stroke="{ink}" '
         f'stroke-width="{f(sw)}" stroke-linejoin="round">')
    g += petal(size * 0.95, size * 0.42, -128) + petal(size * 0.95, size * 0.42, 128)
    g += petal(size * 1.0, size * 0.36, -22) + petal(size * 1.0, size * 0.36, 22)
    g += petal(size * 1.12, size * 0.34, 0)
    g += (f'<path d="M{f(-size * 0.42)} {f(size * 0.32)} Q{f(-size * 0.2)} {f(size * 0.05)} 0 0" '
          f'fill="none" stroke="{YELLOW_DEEP}" stroke-width="{f(sw * 1.6)}" stroke-linecap="round"/>')
    g += (f'<path d="M{f(size * 0.42)} {f(size * 0.32)} Q{f(size * 0.2)} {f(size * 0.05)} 0 0" '
          f'fill="none" stroke="{YELLOW_DEEP}" stroke-width="{f(sw * 1.6)}" stroke-linecap="round"/>')
    return g + "</g>"


def bud(cx, cy, size, fill, ink=INK_BLUE, sw=0.5):
    s = size
    return (f'<path d="M{f(cx - s * 0.5)} {f(cy - s * 0.2)} Q{f(cx - s * 0.55)} {f(cy + s * 0.55)} {f(cx)} '
            f'{f(cy + s * 0.55)} Q{f(cx + s * 0.55)} {f(cy + s * 0.55)} {f(cx + s * 0.5)} {f(cy - s * 0.2)} '
            f'L{f(cx + s * 0.22)} {f(cy + s * 0.05)} L{f(cx)} {f(cy - s * 0.45)} L{f(cx - s * 0.22)} '
            f'{f(cy + s * 0.05)} Z" fill="{fill}" stroke="{ink}" stroke-width="{f(sw)}" stroke-linejoin="round"/>')


# ---------------------------------------------------------------- option 1: Encore (black)
def option_1():
    W, H, B = TRIM_W, TRIM_H, BLEED
    bg = [f'<rect id="bg" x="{f(-B)}" y="{f(-B)}" width="{f(PAGE_W)}" height="{f(PAGE_H)}" fill="{SHIRT_BLACK}"/>']

    # piano keys along the bottom, running into the bleed
    keys_top = 82.0
    kw, gap = 9.0, 0.9
    keys = []
    x, i = -B, 0
    while x < W + B:
        keys.append(f'<rect x="{f(x)}" y="{f(keys_top)}" width="{f(kw)}" height="{f(H + B - keys_top + 1)}" '
                    f'rx="0.5" fill="{KEY_WHITE}"/>')
        if i % 7 in (0, 1, 3, 4, 5):
            bx = x + kw + gap / 2 - 2.7
            keys.append(f'<rect x="{f(bx)}" y="{f(keys_top - 1)}" width="5.4" height="14" rx="0.6" '
                        f'fill="{SHIRT_BLACK}"/>')
        x += kw + gap
        i += 1

    # watercolour flowers from the tee: iris spray grows up out of the keys,
    # the peony + rose rest on the keys in front of it
    iris_img, iris_h = image("iris-spray", os.path.join(ASSETS, "iris-spray.png"), 70.0, 0, 80.0)
    iris_img = iris_img.replace(' y="0"', f' y="{f(keys_top + 1.2 - iris_h)}"')
    pr_img, pr_h = image("peony-rose", os.path.join(ASSETS, "peony-rose.png"), 90.0, 0, 58.0)
    pr_img = pr_img.replace(' y="0"', f' y="{f(keys_top + 15.5 - pr_h)}"')

    x0 = 10.0
    head = [
        text(x0, 21.5, HEAD_1, "Ultra", 11.2, "#FFFFFF"),
        text(x0 + 0.3, 29.6, HEAD_2.upper(), "Montserrat", 4.3, VIP_YELLOW, weight=700, spacing=0.45),
        text(x0, 43.2, HEAD_3, "Ultra", 11.2, VIP_YELLOW),
    ]
    body = [
        text(x0 + 0.2, 51.5, BODY[0], "Montserrat", 3.0, "#E9E6DF"),
        text(x0 + 0.2, 55.9, BODY[1], "Montserrat", 3.0, "#E9E6DF"),
        text(x0 + 0.2, 62.4, BODY[2], "Montserrat", 3.0, "#FFFFFF", weight=700),
    ]
    handle = [
        lightstick("crown-lightstick", x0 + 4.4, 77.0, 12.5, line=SHIRT_BLACK, handle="#4A4A4A"),
        text(x0 + 11.5, 73.6, HANDLE, "Montserrat", 3.3, VIP_YELLOW, weight=700, spacing=0.15),
    ]
    sparks = [sparkle(92.0, 9.5, 1.8, VIP_YELLOW), sparkle(97.0, 14.5, 0.9, VIP_YELLOW),
              sparkle(132.0, 18.0, 1.2, "#FFFFFF"), sparkle(54.0, 38.0, 1.1, "#FFFFFF")]
    layers = [
        layer("Background", bg),
        layer("Flowers - iris spray (watercolour)", [iris_img]),
        layer("Piano keys", keys),
        layer("Flowers - peony and rose (watercolour)", [pr_img]),
        layer("Sparkles", sparks),
        layer("Headline", head),
        layer("Body copy", body),
        layer("Instagram handle", handle),
    ]
    return svg_doc("Thank-you card - Option 1 - Encore", layers)


# ---------------------------------------------------------------- option 2: Flower Road (cream)
def option_2():
    W, H, B = TRIM_W, TRIM_H, BLEED
    rnd = random.Random(7)
    bg = [f'<rect id="bg" x="{f(-B)}" y="{f(-B)}" width="{f(PAGE_W)}" height="{f(PAGE_H)}" fill="{CREAM}"/>']

    # corner doodles, bleeding off the edges like the references
    loop = [(-6, 16), (4, 10), (12, 4), (10, -2), (4, 2), (8, 10), (18, 9), (26, 0), (30, -6)]
    doodles = [
        f'<path d="{smooth_open(loop)}" fill="none" stroke="{YELLOW_LIGHT}" stroke-width="2.6" stroke-linecap="round"/>',
        f'<path d="{smooth_open([(122, -6), (128, 4), (138, 2), (142, 10), (152, 9)])}" fill="none" '
        f'stroke="{IRIS_LILAC}" stroke-width="2.6" stroke-linecap="round"/>',
        sparkle(18, 30, 2.0, VIP_YELLOW), sparkle(23, 25, 1.0, VIP_YELLOW),
        sparkle(131, 27, 2.0, VIP_YELLOW), sparkle(125.5, 33, 1.0, PEONY_PINK),
    ]

    cx = W / 2
    # a yellow marker swash behind "VIPs!"
    swash = (f'<path d="M{f(cx - 17)} {f(36.4)} Q{f(cx)} {f(34.6)} {f(cx + 17.5)} {f(35.6)} L{f(cx + 16.5)} {f(41.6)} '
             f'Q{f(cx)} {f(42.8)} {f(cx - 16)} {f(42.2)} Z" fill="{YELLOW_LIGHT}"/>')
    head = [
        text(cx, 22.5, f"{HEAD_1} {HEAD_2}", "Caveat Brush", 10.4, INK_BLUE, anchor="middle"),
        swash,
        text(cx, 40.6, HEAD_3, "Caveat Brush", 13.0, INK_BLUE, anchor="middle"),
    ]
    body = [
        text(cx, 49.0, BODY[0], "Gaegu", 4.6, INK_BLUE, weight=700, anchor="middle", spacing=-0.12),
        text(cx, 53.8, BODY[1], "Gaegu", 4.6, INK_BLUE, weight=700, anchor="middle", spacing=-0.12),
        text(cx, 58.6, BODY[2], "Gaegu", 4.6, INK_BLUE, weight=700, anchor="middle", spacing=-0.12),
    ]
    pill_w = 33.0
    handle = [
        f'<rect x="{f(cx - pill_w / 2)}" y="62.4" width="{f(pill_w)}" height="6.6" rx="3.3" fill="{PEONY_PINK}"/>',
        text(cx, 67.0, HANDLE, "Gaegu", 4.2, INK_BLUE, weight=700, anchor="middle"),
    ]

    # the flower road: a dashed path winding from the left edge to the lightstick
    road_pts = [(-6, 96), (14, 92.5), (34, 95.5), (56, 91.5), (78, 94.5), (100, 90.5), (118, 92)]
    road = [
        f'<path d="{smooth_open(road_pts)}" fill="none" stroke="{YELLOW_LIGHT}" stroke-width="4.2" stroke-linecap="round"/>',
        f'<path d="{smooth_open(road_pts)}" fill="none" stroke="{INK_BLUE}" stroke-width="0.55" '
        f'stroke-dasharray="2.2 1.8" stroke-linecap="round"/>',
    ]

    def road_y(x):
        # nearest point on the polyline, good enough for planting stems
        best = min(road_pts, key=lambda p: abs(p[0] - x))
        i = road_pts.index(best)
        a, b = (road_pts[i], road_pts[i + 1]) if x >= best[0] and i + 1 < len(road_pts) else (road_pts[i - 1], road_pts[i])
        t = (x - a[0]) / (b[0] - a[0]) if b[0] != a[0] else 0
        return a[1] + t * (b[1] - a[1])

    flowers = []
    plan = [  # x, kind, height, side (-1 above road / +1 below), bend
        (6, "leaf", 7, -1, 0), (12, "rose", 13, -1, -1.5), (20, "bud", 9, -1, 1.2),
        (28, "iris", 15, -1, -1.0), (37, "leaf", 6, -1, 0), (44, "peony", 12, -1, 1.5),
        (53, "rose", 9, -1, -1), (62, "iris", 12, -1, 1.0), (71, "bud", 8, -1, -0.8),
        (79, "peony", 14, -1, -1.2), (90, "rose", 11, -1, 1.0), (98, "leaf", 7, -1, 0),
        (104, "iris", 10, -1, -0.6),
            ]
    for x, kind, h, side, bend in plan:
        y = road_y(x) - 2.6
        if kind == "small":
            yb = road_y(x) + 3.0
            flowers.append(leaf(x - 1, yb + 4.2, 4.2, -55))
            flowers.append(leaf(x + 1, yb + 4.2, 4.2, 55))
            continue
        if kind == "leaf":
            flowers.append(leaf(x - 0.6, y, h, -28 + rnd.uniform(-6, 6)))
            flowers.append(leaf(x + 0.6, y, h * 0.8, 30 + rnd.uniform(-6, 6)))
            continue
        top = (x + bend, y - h)
        flowers.append(stem(x, y, top[0], top[1], bend * 0.6))
        flowers.append(leaf(x + 0.2, y - h * 0.32, h * 0.38, 38 if bend < 0 else -38))
        if kind == "rose":
            flowers.append(rose(top[0], top[1] - 2.2, 3.4, YELLOW_LIGHT))
        elif kind == "peony":
            flowers.append(peony(top[0], top[1] - 2.6, 4.2, PEONY_PINK))
        elif kind == "iris":
            flowers.append(iris(top[0], top[1], 4.0, IRIS_LILAC))
        elif kind == "bud":
            flowers.append(bud(top[0], top[1] - 1.4, 3.6, PEONY_PINK))

    # the lightstick at the end of the road, lit up
    ls = [
        lightstick("crown-lightstick", 128.0, 98.5, 27.0, line=INK_BLUE, handle="#2F3A66", glow=YELLOW_LIGHT, rotate=8),
        sparkle(112.5, 66.5, 1.8, VIP_YELLOW), sparkle(143.0, 74.0, 1.4, VIP_YELLOW),
        sparkle(139.5, 63.0, 0.9, INK_BLUE), sparkle(116.5, 75.5, 0.9, INK_BLUE),
    ]
    layers = [
        layer("Background", bg),
        layer("Corner doodles", doodles),
        layer("Flower road", road),
        layer("Line flowers", flowers),
        layer("Crown lightstick", ls),
        layer("Headline", head),
        layer("Body copy", body),
        layer("Instagram handle", handle),
    ]
    return svg_doc("Thank-you card - Option 2 - Flower Road", layers)


# ---------------------------------------------------------------- output
def render(svg, base):
    open(base + ".svg", "w").write(svg)
    cairosvg.svg2pdf(bytestring=svg.encode(), write_to=base + ".ai")
    px_per_mm = 300 / 25.4
    full = base.replace(OUT_AI, OUT_PREVIEW) + "_bleed.png"
    cairosvg.svg2png(bytestring=svg.encode(), write_to=full, output_width=round(PAGE_W * px_per_mm))
    im = Image.open(full).convert("RGB")
    b = round(BLEED * px_per_mm)
    trimmed = im.crop((b, b, im.width - b, im.height - b))
    trimmed.save(base.replace(OUT_AI, OUT_PREVIEW) + ".png", optimize=True)
    d = ImageDraw.Draw(im)
    d.rectangle((b, b, im.width - b - 1, im.height - b - 1), outline=(255, 0, 170), width=3)
    s = round(5 * px_per_mm)  # 5 mm safe area
    for i in range(b + s, im.width - b - s, 24):
        d.line((i, b + s, i + 12, b + s), fill=(0, 170, 255), width=2)
        d.line((i, im.height - b - s, i + 12, im.height - b - s), fill=(0, 170, 255), width=2)
    for j in range(b + s, im.height - b - s, 24):
        d.line((b + s, j, b + s, j + 12), fill=(0, 170, 255), width=2)
        d.line((im.width - b - s, j, im.width - b - s, j + 12), fill=(0, 170, 255), width=2)
    im.save(full, optimize=True)
    print("wrote", os.path.relpath(base, ROOT) + ".ai/.svg + previews")


def main():
    os.makedirs(OUT_AI, exist_ok=True)
    os.makedirs(OUT_PREVIEW, exist_ok=True)
    render(option_1(), os.path.join(OUT_AI, "option-1_encore_A6"))
    render(option_2(), os.path.join(OUT_AI, "option-2_flower-road_A6"))


if __name__ == "__main__":
    main()
