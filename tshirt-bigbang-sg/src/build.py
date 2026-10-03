#!/usr/bin/env python3
"""Build the print files, mockup and vendor spec sheet for the SG concert tee.

    pip install cairosvg fonttools
    python3 build.py

Outputs go to ../print-files and ../mockup. Tweak the SETTINGS block below
(sizes, the Singapore line, flower seeds) and re-run to regenerate everything.
"""
import base64
import io
import math
import os
from functools import lru_cache

import cairosvg
from fontTools.pens.basePen import BasePen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from PIL import Image
from shapely.geometry import Polygon

from brush import brushed_keys
from flowers import Art, bud, cupped_bloom, iris, leaf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FONTS = os.path.join(ROOT, "fonts")
OUT_PRINT = os.path.join(ROOT, "print-files")
OUT_MOCK = os.path.join(ROOT, "mockup")

# ------------------------------------------------------------------ SETTINGS
SHIRT = "#121212"            # garment colour used in the mockup only
WHITE = "#ffffff"            # white ink (B, wordmark, piano keys)
FRONT_MM = 100               # front emblem artboard, square (mm)
B_WIDTH = 0.519              # B width as a fraction of the emblem (0.519 x 100 mm = 5.2 cm)
B_XSCALE = 1.6               # horizontal stretch of the B (1.6 = same shape as the back wordmark)
BACK_W_MM = 270              # back artboard width (mm); height follows the art
KEYS_STYLE = "brushed"       # piano keys: "brushed" (rough painted edges) or "clean"
KEYS_SEED = 7                # change to get a different brush pattern
SG_LINE = ""                 # optional line under the piano keys, e.g. "SINGAPORE · 2026"
KNOCKOUT_MM = 1.0            # black gap between the white B and the flowers (0 = none)
B_NUDGE = (25, 45)           # shift the B from centre (x, y) in 1/1000ths of the artboard
FLOWERS = "watercolour"      # "watercolour" (painted PNG layer) or "vector" (generated paths)
UPLOAD_DIR = os.path.join(ROOT, "upload-here")  # drop the painted flowers PNG here (any name)
EDITED_PNG = os.path.join(HERE, "assets", "flowers-tight.png")  # written by edit_flowers.py
DPI = 300
FRONT_FROM_CENTRE_MM = 80    # centre line -> left edge of the chest emblem
FRONT_BELOW_COLLAR_MM = 75   # centre-front collar seam -> top of the emblem
BACK_BELOW_COLLAR_MM = 100   # centre-back collar seam -> top of the back art

SLAB = "Ultra-Regular.ttf"   # Ultra by Astigmatic, Apache 2.0 licence
SANS = "Montserrat[wght].ttf"  # Montserrat, SIL OFL 1.1


# ------------------------------------------------------------------ type -> outlines
@lru_cache(None)
def _font(name, wght=None):
    f = TTFont(os.path.join(FONTS, name))
    if wght is not None and "fvar" in f:
        f = instantiateVariableFont(f, {"wght": wght})
    return f


def text_path(fontname, text, size, x=0.0, y=0.0, xscale=1.0, tracking=0.0, wght=None, anchor="start"):
    """Text converted to outlines. Returns (path_d, (xmin, ymin, xmax, ymax)). y is the baseline."""
    f = _font(fontname, wght)
    gs, cmap = f.getGlyphSet(), f.getBestCmap()
    s = size / f["head"].unitsPerEm
    adv = [f["hmtx"][cmap[ord(c)]][0] * s * xscale for c in text]
    width = sum(adv) + tracking * (len(text) - 1)
    x -= {"start": 0, "middle": width / 2, "end": width}[anchor]
    pen, bp = SVGPathPen(gs), BoundsPen(gs)
    cx = x
    for c, a in zip(text, adv):
        t = (s * xscale, 0, 0, -s, cx, y)
        gs[cmap[ord(c)]].draw(TransformPen(pen, t))
        gs[cmap[ord(c)]].draw(TransformPen(bp, t))
        cx += a + tracking
    return pen.getCommands(), bp.bounds


def fit_text(fontname, text, box_cx, box_top, target_w, xscale=1.0, tracking_em=0.0, wght=None):
    """Outline text so its ink is exactly target_w wide, centred on box_cx, top at box_top."""
    _, (x0, y0, x1, y1) = text_path(fontname, text, 1000, 0, 0, xscale, tracking_em * 1000, wght)
    k = target_w / (x1 - x0)
    size = 1000 * k
    x = box_cx - (x0 + (x1 - x0) / 2) * k
    y = box_top - y0 * k
    d, bounds = text_path(fontname, text, size, x, y, xscale, tracking_em * size, wght)
    fit_text.last = (size, x, y)
    return d, bounds


class _FlattenPen(BasePen):
    """Glyph outline -> list of polylines (for offsetting the knockout)."""

    def __init__(self, glyphset, steps=16):
        super().__init__(glyphset)
        self.contours, self.cur, self.steps = [], [], steps

    def _moveTo(self, p):
        self.cur = [p]

    def _lineTo(self, p):
        self.cur.append(p)

    def _curveToOne(self, p1, p2, p3):
        p0 = self.cur[-1]
        for i in range(1, self.steps + 1):
            t = i / self.steps
            mt = 1 - t
            self.cur.append(tuple(mt ** 3 * a + 3 * mt * mt * t * b + 3 * mt * t * t * c + t ** 3 * d
                                  for a, b, c, d in zip(p0, p1, p2, p3)))

    def _qCurveToOne(self, p1, p2):
        p0 = self.cur[-1]
        for i in range(1, self.steps + 1):
            t = i / self.steps
            mt = 1 - t
            self.cur.append(tuple(mt * mt * a + 2 * mt * t * b + t * t * c for a, b, c in zip(p0, p1, p2)))

    def _closePath(self):
        if len(self.cur) > 2:
            self.contours.append(self.cur)
        self.cur = []

    _endPath = _closePath


def text_shape(fontname, text, size, x=0.0, y=0.0, xscale=1.0, tracking=0.0, wght=None):
    """Same placement as text_path, but as a shapely geometry (holes resolved even-odd)."""
    f = _font(fontname, wght)
    gs, cmap = f.getGlyphSet(), f.getBestCmap()
    s = size / f["head"].unitsPerEm
    pen = _FlattenPen(gs)
    cx = x
    for c in text:
        gs[cmap[ord(c)]].draw(TransformPen(pen, (s * xscale, 0, 0, -s, cx, y)))
        cx += f["hmtx"][cmap[ord(c)]][0] * s * xscale + tracking
    geom = None
    for ring in pen.contours:
        poly = Polygon(ring).buffer(0)
        geom = poly if geom is None else geom.symmetric_difference(poly)
    return geom


def knockout_clip(clip_id, geom, gap, W, H, fill_counters=True):
    """clipPath = whole artboard minus `geom` grown by `gap`.

    With fill_counters the letter's counters are knocked out too, so they read
    as solid shirt colour (like the reference B) instead of showing flowers.
    """
    if fill_counters:
        geom = Polygon(geom.exterior) if geom.geom_type == "Polygon" else geom
    grown = geom.buffer(gap, join_style="round", quad_segs=8)
    polys = getattr(grown, "geoms", [grown])
    rings = []
    for poly in polys:
        for ring in [poly.exterior, *poly.interiors]:
            rings.append("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in ring.coords[:-1]) + "Z")
    return (f'<clipPath id="{clip_id}" clipPathUnits="userSpaceOnUse">'
            f'<path clip-rule="evenodd" d="M0,0 L{W},0 L{W},{H} L0,{H}Z {"".join(rings)}"/></clipPath>')


def layer(gid, label, body, extra=""):
    return (f'<g id="{gid}" inkscape:groupmode="layer" inkscape:label="{label}"{extra}>'
            + "".join(body) + "</g>")


def svg_doc(w_mm, h_mm, vb_w, vb_h, defs, body, bg=None):
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<svg xmlns="http://www.w3.org/2000/svg" '
            'xmlns:xlink="http://www.w3.org/1999/xlink" '
            'xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" '
            f'width="{w_mm}mm" height="{h_mm}mm" viewBox="0 0 {vb_w:.1f} {vb_h:.1f}">\n'
            f'<defs>{"".join(defs)}</defs>\n'
            + (f'<rect width="100%" height="100%" fill="{bg}"/>' if bg else "")
            + "\n".join(body) + "\n</svg>\n")


# ------------------------------------------------------------------ FRONT
def find_uploaded_watercolour():
    """The painted flowers as uploaded: the PNG in upload-here/ (newest if several)."""
    if not os.path.isdir(UPLOAD_DIR):
        return None
    pngs = [os.path.join(UPLOAD_DIR, f) for f in os.listdir(UPLOAD_DIR) if f.lower().endswith(".png")]
    return max(pngs, key=os.path.getmtime) if pngs else None


def find_watercolour():
    """The flowers to print: the reworked version from edit_flowers.py if present."""
    return EDITED_PNG if os.path.exists(EDITED_PNG) else find_uploaded_watercolour()


def native_px():
    """Pixel width at which the painted flowers print 1:1 (no upscaling), or None."""
    painted = find_watercolour()
    if FLOWERS != "watercolour" or not painted:
        return None
    im = Image.open(painted).convert("RGBA")
    return max(im.crop(im.getchannel("A").point(lambda a: 255 if a > 8 else 0).getbbox()).size)


def watercolour_layer(png_path, S):
    """Embed the painted flowers, cropped to their ink and centred on the artboard."""
    im = Image.open(png_path).convert("RGBA")
    bbox = im.getchannel("A").point(lambda a: 255 if a > 8 else 0).getbbox()
    im = im.crop(bbox)
    # AI watercolour comes out at alpha ~250 rather than 255; snap near-opaque
    # paint to solid so the printer lays a full white underbase under it
    r, g, b, a = im.split()
    im = Image.merge("RGBA", (r, g, b, a.point(lambda v: 255 if v >= 240 else v)))
    k = S / max(im.size)
    w, h = im.width * k, im.height * k
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True)
    data = base64.b64encode(buf.getvalue()).decode()
    return (f'<image id="watercolour-flowers" x="{(S - w) / 2:.1f}" y="{(S - h) / 2:.1f}" '
            f'width="{w:.1f}" height="{h:.1f}" preserveAspectRatio="xMidYMid meet" '
            f'xlink:href="data:image/png;base64,{data}"/>')


def vector_flowers(art, grp):
    """The original procedural flower ring (kept as an alternative to the watercolour)."""
    # leaves first (they sit behind everything)
    leaves = []
    for i, (x, y, L, a) in enumerate([
        (215, 520, 250, 188), (240, 600, 210, 150),          # left
        (785, 470, 250, -8), (770, 390, 200, -42),           # right
        (470, 300, 230, -112), (560, 290, 190, -70),         # top
        (520, 700, 230, 75), (430, 720, 190, 112),           # bottom
        (330, 330, 170, -150), (690, 690, 170, 30),          # diagonals
    ]):
        leaves += leaf(art, x, y, L, a, seed=100 + i)
    grp("leaves", leaves)
    grp("peony-cream-centre", cupped_bloom(art, 505, 470, 185, "cream", 11, "peony", rot=10))
    grp("buds", bud(art, 640, 120, 32, -60, 21, "magenta") + bud(art, 120, 760, 28, 150, 22, "crimson")
        + bud(art, 905, 640, 26, 10, 23, "blush"))
    grp("rose-magenta-bottom-left", cupped_bloom(art, 290, 705, 180, "magenta", 12, "rose", rot=-20))
    grp("peony-blush-bottom-right", cupped_bloom(art, 712, 712, 175, "blush", 13, "peony", rot=25))
    grp("iris-blue-top-left", iris(art, 285, 300, 205, 14, rot=-12))
    grp("peony-crimson-top-right", cupped_bloom(art, 715, 290, 195, "crimson", 15, "peony", rot=15))


def front_art():
    """Square emblem: white slab B over a ring of flowers. 1 unit = 0.1 mm at 100 mm."""
    S = 1000
    art = Art("f")
    groups = []

    def grp(gid, els):
        groups.append(f'<g id="{gid}">' + "".join(els) + "</g>")

    painted = find_watercolour()
    if FLOWERS == "watercolour" and painted:
        groups.append(watercolour_layer(painted, S))
    else:
        vector_flowers(art, grp)

    # the B, centred, with a knockout gap so it reads cleanly on top of the flowers
    B_W = S * B_WIDTH
    _, (bx0, by0, bx1, by1) = text_path(SLAB, "B", 1000, 0, 0, B_XSCALE)
    b_h = (by1 - by0) * B_W / (bx1 - bx0)
    nx, ny = B_NUDGE
    b_d, _ = fit_text(SLAB, "B", S / 2 + nx, S / 2 - b_h / 2 + 10 + ny, B_W, xscale=B_XSCALE)
    size, bx, by = fit_text.last
    clip = ""
    if KNOCKOUT_MM:
        art.defs.append(knockout_clip("f-knockout", text_shape(SLAB, "B", size, bx, by, B_XSCALE),
                                      KNOCKOUT_MM * S / FRONT_MM, S, S))
        clip = ' clip-path="url(#f-knockout)"'
    body = [
        layer("layer-flowers", "Flowers (full colour)", groups, clip),
        layer("layer-B", "B (white ink)", [f'<path id="letter-B" d="{b_d}" fill="{WHITE}"/>']),
    ]
    return art.defs, body, S, S


# ------------------------------------------------------------------ BACK
def _jag(a, b, teeth, depth):
    """Zig-zag points strictly between a and b (a sawtooth to one side)."""
    (ax, ay), (bx, by) = a, b
    L = ((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5
    nx, ny = (by - ay) / L, -(bx - ax) / L
    pts = []
    for i in range(1, 2 * teeth):
        t = i / (2 * teeth)
        d = depth * (1.0 if i % 2 else 0.0) * (0.7 + 0.6 * ((i * 37) % 10) / 10)
        pts.append((ax + (bx - ax) * t + nx * d, ay + (by - ay) * t + ny * d))
    return pts


def _dagger(x, y_top, y_bot, w):
    """A thin pointed sliver (a black streak cut into a white key), widest low down."""
    left, right, n = [], [], 12
    for i in range(n + 1):
        t = i / n
        half = w / 2 * math.sin(math.pi * t) ** 0.9 * (0.6 + 0.4 * t)
        yy = y_top + (y_bot - y_top) * t
        left.append((x - half, yy))
        right.append((x + half, yy))
    return left + right[::-1][1:-1]


def piano_keys(x, y, W, H, gap, black_w=0.55, black_l=(0.71, 0.70), flare=(0.05, 0.06), flare_from=0.47):
    """Three white keys as polygons; the two black keys are the notches between
    them. black_l = how far each black key reaches down (share of H); flare =
    how much each black key widens on its right over its lower part (share of
    W, from flare_from of H) with a jagged edge, like a brush pressing harder.
    Returns (key polygons, dagger slivers to cut out above each flare)."""
    kw = (W - 2 * gap) / 3
    bw = kw * black_w
    xs = [x + i * (kw + gap) for i in range(3)]
    b1, b2 = xs[0] + kw + gap / 2, xs[1] + kw + gap / 2
    Y0, Y1 = y, y + H
    YB1, YB2 = y + H * black_l[0], y + H * black_l[1]
    YF = y + H * flare_from
    f1, f2 = W * flare[0], W * flare[1]
    r1, r2 = b1 + bw / 2, b2 + bw / 2  # right edges of the black keys
    jag1 = _jag((r1 + f1, YF + H * 0.11), (r1, YF), 3, W * 0.014)
    jag2 = _jag((r2 + f2, YF + H * 0.12), (r2, YF + H * 0.02), 4, W * 0.012)
    keys = [
        [(xs[0], Y0), (b1 - bw / 2, Y0), (b1 - bw / 2, YB1), (xs[0] + kw, YB1), (xs[0] + kw, Y1), (xs[0], Y1)],
        [(r1, Y0), (b2 - bw / 2, Y0), (b2 - bw / 2, YB2), (xs[1] + kw, YB2), (xs[1] + kw, Y1),
         (xs[1], Y1), (xs[1], YB1), (r1 + f1, YB1), (r1 + f1, YF + H * 0.11), *jag1, (r1, YF)],
        [(r2, Y0), (xs[2] + kw, Y0), (xs[2] + kw, Y1), (xs[2], Y1), (xs[2], YB2), (r2 + f2, YB2),
         (r2 + f2, YF + H * 0.12), *jag2, (r2, YF + H * 0.02)],
    ]
    daggers = [
        _dagger(r1 + W * 0.03, YF - H * 0.07, YF + H * 0.09, W * 0.022),
        _dagger(r2 + W * 0.028, YF - H * 0.12, YF + H * 0.02, W * 0.016),
    ]
    return keys, daggers


def back_art():
    """BIGBANG wordmark + piano keys (+ optional Singapore line). 1 unit = 0.1 mm."""
    W = BACK_W_MM * 10
    cx = W / 2
    word_d, (_, _, _, wy1) = fit_text(SLAB, "BIGBANG", cx, 0, W, xscale=1.6, tracking_em=0.02)
    keys_top = wy1 + 300
    keys_w = W * 0.76
    keys_h = keys_w / 0.78  # same block proportions as the reference
    polys, daggers = piano_keys(cx - keys_w / 2, keys_top, keys_w, keys_h, gap=keys_w * 0.027)
    bottom = keys_top + keys_h
    if KEYS_STYLE == "brushed":
        keys, (_, _, _, kb) = brushed_keys(polys, seed=KEYS_SEED, unit=keys_h / 2000, holes=daggers)
        bottom = max(bottom, kb)  # frayed ends reach past the clean outline
    else:
        keys = ["M" + " L".join(f"{px:.1f},{py:.1f}" for px, py in p) + "Z" for p in polys]
    body = [layer("layer-wordmark", "BIGBANG wordmark (white ink)",
                  [f'<path id="wordmark" d="{word_d}" fill="{WHITE}"/>']),
            layer("layer-keys", "Piano keys (white ink)",
                  [f'<path id="key-{i + 1}" d="{k}" fill="{WHITE}" fill-rule="evenodd"/>'
                   for i, k in enumerate(keys)])]
    if SG_LINE:
        sg_d, (_, _, _, sy1) = fit_text(SANS, SG_LINE, cx, bottom + 160, W * 0.46, tracking_em=0.32, wght=600)
        body.append(layer("layer-sg", "Singapore line (white ink)", [f'<path id="sg-line" d="{sg_d}" fill="{WHITE}"/>']))
        bottom = sy1
    return [], body, W, bottom + 2


# ------------------------------------------------------------------ MOCKUP
def tee(cx, top, back=False, fill=SHIRT):
    """Simple oversized tee silhouette in mm (body 580 wide, 740 long)."""
    def P(x, y):
        return f"{cx + x:.1f},{top + y:.1f}"
    drop = 22 if back else 88
    out = (f"M{P(-95, 0)} C{P(-88, drop * .7)} {P(-50, drop)} {P(0, drop)} C{P(50, drop)} {P(88, drop * .7)} {P(95, 0)} "
           f"Q{P(180, 18)} {P(268, 52)} Q{P(330, 160)} {P(392, 290)} L{P(302, 350)} Q{P(292, 300)} {P(290, 262)} "
           f"Q{P(287, 500)} {P(292, 742)} Q{P(0, 752)} {P(-292, 742)} Q{P(-287, 500)} {P(-290, 262)} "
           f"Q{P(-292, 300)} {P(-302, 350)} L{P(-392, 290)} Q{P(-330, 160)} {P(-268, 52)} Q{P(-180, 18)} {P(-95, 0)}Z")
    inner = (f"M{P(-95, 0)} C{P(-88, 16)} {P(-50, 24)} {P(0, 24)} C{P(50, 24)} {P(88, 16)} {P(95, 0)} "
             f"C{P(88, drop * .7)} {P(50, drop)} {P(0, drop)} C{P(-50, drop)} {P(-88, drop * .7)} {P(-95, 0)}Z")
    rib = (f"M{P(-95, 0)} C{P(-88, drop * .7)} {P(-50, drop)} {P(0, drop)} C{P(50, drop)} {P(88, drop * .7)} {P(95, 0)}")
    seams = (f"M{P(-268, 52)} Q{P(-282, 160)} {P(-290, 262)} M{P(268, 52)} Q{P(282, 160)} {P(290, 262)} "
             f"M{P(-392, 290)} L{P(-302, 350)} M{P(392, 290)} L{P(302, 350)} M{P(-290, 715)} Q{P(0, 724)} {P(290, 715)}")
    return [f'<path d="{out}" fill="{fill}" stroke="#2a2a2a" stroke-width="1.5"/>',
            "" if back else f'<path d="{inner}" fill="#050505"/>',
            f'<path d="{rib}" fill="none" stroke="#1e1e1e" stroke-width="16" stroke-linecap="round"/>',
            f'<path d="{rib}" fill="none" stroke="#2c2c2c" stroke-width="1.2"/>',
            f'<path d="{seams}" fill="none" stroke="#262626" stroke-width="1.4" stroke-dasharray="3 2"/>']


def place(body, vb_w, mm_w, x, y):
    k = mm_w / vb_w
    return f'<g transform="translate({x:.1f} {y:.1f}) scale({k:.5f})">' + "".join(body) + "</g>"


def label(text, x, y, size, wght=600, anchor="middle", fill="#1a1a1a", tracking_em=0.0):
    d, _ = text_path(SANS, text, size, x, y, tracking=tracking_em * size, wght=wght, anchor=anchor)
    return f'<path d="{d}" fill="{fill}"/>'


def hdim(x0, x1, y, text, col="#d0245e"):
    t = 6
    return (f'<g stroke="{col}" stroke-width="1.6" fill="none"><path d="M{x0},{y} L{x1},{y} M{x0},{y - t} L{x0},{y + t} '
            f'M{x1},{y - t} L{x1},{y + t}"/></g>' + label(text, (x0 + x1) / 2, y - 9, 15, 600, fill=col))


def vdim(x, y0, y1, text, col="#d0245e", side=1):
    t = 6
    lx = x + side * 10
    return (f'<g stroke="{col}" stroke-width="1.6" fill="none"><path d="M{x},{y0} L{x},{y1} M{x - t},{y0} L{x + t},{y0} '
            f'M{x - t},{y1} L{x + t},{y1}"/></g>'
            + label(text, lx, (y0 + y1) / 2 + 5, 15, 600, anchor="start" if side > 0 else "end", fill=col))


def mockup_svg(front, back, annotate):
    fdefs, fbody, fW, fH = front
    bdefs, bbody, bW, bH = back
    sheet_w = 1700
    sheet_h = 1202 if annotate else 920
    top = 70
    fcx, bcx = 440, 1260
    back_mm_h = bH / 10
    collar_f, collar_b = top + 88, top + 22  # centre-front / centre-back collar seam
    # placements (mm on the garment)
    f_x = fcx + FRONT_FROM_CENTRE_MM        # emblem left edge (wearer's left chest)
    f_y = collar_f + FRONT_BELOW_COLLAR_MM  # emblem top
    b_x = bcx - BACK_W_MM / 2
    b_y = collar_b + BACK_BELOW_COLLAR_MM   # back art top
    guide = 'stroke="#8a8a8a" stroke-width="1" stroke-dasharray="6 5"'
    f_mid = f_x + FRONT_MM / 2
    f_guides = [f'<path d="M{fcx},{collar_f} L{fcx},{top + 760}" {guide}/>',
                f'<path d="M{fcx},{collar_f} L{f_mid + 8},{collar_f}" {guide}/>'] if annotate else []
    b_guides = [f'<path d="M{bcx},{collar_b} L{bcx},{top + 760}" {guide}/>'] if annotate else []
    body = [f'<rect width="{sheet_w}" height="{sheet_h}" fill="#f4f2ee"/>']
    body += tee(fcx, top) + f_guides + [place(fbody, fW, FRONT_MM, f_x, f_y)]
    body += tee(bcx, top, back=True) + b_guides + [place(bbody, bW, BACK_W_MM, b_x, b_y)]
    body.append(label("FRONT", fcx, top + 810, 22, 700, tracking_em=0.3))
    body.append(label("BACK", bcx, top + 810, 22, 700, tracking_em=0.3))
    if annotate:
        body.append(vdim(f_mid, collar_f, f_y, f"{FRONT_BELOW_COLLAR_MM / 10:g} cm below collar"))
        body.append(vdim(f_x + FRONT_MM + 16, f_y, f_y + FRONT_MM, f"{FRONT_MM / 10:g} cm"))
        body.append(hdim(f_x, f_x + FRONT_MM, f_y + FRONT_MM + 30, f"{FRONT_MM / 10:g} cm"))
        body.append(hdim(fcx, f_x, f_y + FRONT_MM + 70, f"{FRONT_FROM_CENTRE_MM / 10:g} cm from centre"))
        body.append(vdim(bcx, collar_b, b_y, f"{BACK_BELOW_COLLAR_MM / 10:g} cm below collar"))
        body.append(vdim(b_x + BACK_W_MM + 16, b_y, b_y + back_mm_h, f"{back_mm_h / 10:.1f} cm"))
        body.append(hdim(b_x, b_x + BACK_W_MM, b_y + back_mm_h + 30, f"{BACK_W_MM / 10:g} cm"))
        notes_left = [
            ("GARMENT", "Black cotton tee, oversized / drop-shoulder fit"),
            ("PRINT METHOD", "DTF or DTG, full colour + white underbase"),
            ("FRONT", f"Wearer's left chest, {FRONT_MM / 10:g} x {FRONT_MM / 10:g} cm, full colour"),
            ("BACK", f"Centred, {BACK_W_MM / 10:g} x {back_mm_h / 10:.1f} cm, white ink only"),
        ]
        notes_right = [
            ("FILES", "FRONT / BACK as .pdf + .svg, .png 300 dpi + 2048 px"),
            ("COLOUR", "sRGB artwork; white = 100% white ink"),
            ("BACKGROUND", "Transparent - do NOT print the black"),
            ("SIZING", "Same print size on all shirt sizes unless noted"),
        ]
        y0 = 990
        body.append(f'<path d="M80,{y0 - 50} L{sheet_w - 80},{y0 - 50}" stroke="#cfcac2" stroke-width="1.5"/>')
        for col_x, notes in ((80, notes_left), (880, notes_right)):
            for i, (k, v) in enumerate(notes):
                yy = y0 + i * 48
                body.append(label(k, col_x, yy, 15, 700, anchor="start", fill="#8a1c45", tracking_em=0.18))
                body.append(label(v, col_x + 200, yy, 17, 500, anchor="start"))
        body.append(label("BIGBANG SG CONCERT TEE  ·  PRINT SPEC", 80, 46, 20, 700, anchor="start",
                          tracking_em=0.18))
    return svg_doc(420 if annotate else 340, 297 if annotate else 184, sheet_w, sheet_h, fdefs + bdefs, body)


# ------------------------------------------------------------------ export
def export(svg, base, w_mm, png_dpi=DPI, extra_png=None):
    with open(base + ".svg", "w") as fh:
        fh.write(svg)
    cairosvg.svg2pdf(bytestring=svg.encode(), write_to=base + ".pdf")
    px = round(w_mm / 25.4 * png_dpi)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=base + f"_{png_dpi}dpi.png", output_width=px)
    if extra_png:
        cairosvg.svg2png(bytestring=svg.encode(), write_to=base + f"_{extra_png}px.png", output_width=extra_png)


def main():
    os.makedirs(OUT_PRINT, exist_ok=True)
    for f in os.listdir(OUT_PRINT):  # drop outputs from earlier settings
        os.remove(os.path.join(OUT_PRINT, f))
    os.makedirs(OUT_MOCK, exist_ok=True)
    front = front_art()
    back = back_art()
    fdefs, fbody, fW, fH = front
    bdefs, bbody, bW, bH = back
    back_h_mm = round(bH / 10, 1)

    export(svg_doc(FRONT_MM, FRONT_MM, fW, fH, fdefs, fbody),
           os.path.join(OUT_PRINT, f"FRONT_left-chest_{FRONT_MM}x{FRONT_MM}mm"), FRONT_MM,
           extra_png=native_px() or 4000)
    export(svg_doc(BACK_W_MM, back_h_mm, bW, bH, bdefs, bbody),
           os.path.join(OUT_PRINT, f"BACK_{BACK_W_MM}x{back_h_mm:g}mm"), BACK_W_MM)

    # previews on black so the white/transparent art is visible
    cairosvg.svg2png(bytestring=svg_doc(FRONT_MM, FRONT_MM, fW, fH, fdefs, fbody, bg=SHIRT).encode(),
                     write_to=os.path.join(OUT_MOCK, "preview_front-emblem.png"), output_width=1600)

    mock = mockup_svg(front, back, annotate=False)
    cairosvg.svg2png(bytestring=mock.encode(), write_to=os.path.join(OUT_MOCK, "mockup.png"), output_width=3400)
    spec = mockup_svg(front, back, annotate=True)
    cairosvg.svg2pdf(bytestring=spec.encode(), write_to=os.path.join(OUT_MOCK, "spec-sheet.pdf"))
    cairosvg.svg2png(bytestring=spec.encode(), write_to=os.path.join(OUT_MOCK, "spec-sheet.png"), output_width=3400)
    print("front", FRONT_MM, "mm  back", BACK_W_MM, "x", back_h_mm, "mm")


if __name__ == "__main__":
    main()
