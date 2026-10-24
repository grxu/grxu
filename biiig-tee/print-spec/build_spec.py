"""BIIIG tee: vendor print files and A3 print spec sheets, one set per shirt colour.

Uses the same sheet layout as the BIGBANG SG tee spec (tshirt-bigbang-sg/src/
build.py on branch claude/brave-edison-i18pzh): flat front and back tees drawn
in garment millimetres, pink dimension lines, and a notes table. Text is
converted to outlines (Montserrat, SIL OFL), so no fonts are needed to open
the files.

    pip install cairosvg fonttools
    python3 build_spec.py ../ghost-mannequin/print ../final

Writes <out>/print-files/<colour>-tee/ (.svg, .pdf, .ai, 300 dpi .png for the
front and back) and <out>/spec-sheets/ (spec-sheet_<colour>-tee .pdf + .png).
"""
import os
import re
import shutil
import sys
from functools import lru_cache

import cairosvg
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

SRC, OUT = sys.argv[1:3]
HERE = os.path.dirname(os.path.abspath(__file__))
SANS = os.path.join(HERE, "fonts", "Montserrat[wght].ttf")

# ---- settings (garment millimetres) ----------------------------------------
FRONT_W_MM = 100             # front emblem width; height follows the art
BACK_W_MM = 320              # back art width; height follows the art
FRONT_FROM_CENTRE_MM = 100   # centre line -> left edge of the chest emblem
FRONT_BELOW_COLLAR_MM = 180  # centre-front collar seam -> top of the emblem
BACK_BELOW_COLLAR_MM = 150   # centre-back collar seam -> top of the back art
DPI = 300

COLOURWAYS = {
    "black": {
        "shirt": "#121212", "back_svg": "back-iii.svg",
        "garment": "Black cotton tee, oversized / drop-shoulder fit",
        "back_ink": "white ink only",
        "colour": "Blue #0756C6, red #E73A07, yellow #FDBB05, white 100%",
        "background": "Transparent - do NOT print the black",
    },
    "white": {
        "shirt": "#f7f7f5", "back_svg": "back-iii_white-tee.svg",
        "garment": "White cotton tee, oversized / drop-shoulder fit",
        "back_ink": "blue / red / yellow",
        "colour": "Blue #0756C6, red #E73A07, yellow #FDBB05 (sRGB)",
        "background": "Transparent - do NOT print the white",
    },
}


# ---- text -> outlines --------------------------------------------------------
@lru_cache(None)
def _font(wght):
    f = TTFont(SANS)
    return instantiateVariableFont(f, {"wght": wght}) if "fvar" in f else f


def text_path(text, size, x, y, wght=600, anchor="start", tracking=0.0):
    f = _font(wght)
    gs, cmap = f.getGlyphSet(), f.getBestCmap()
    s = size / f["head"].unitsPerEm
    adv = [f["hmtx"][cmap[ord(c)]][0] * s for c in text]
    width = sum(adv) + tracking * (len(text) - 1)
    x -= {"start": 0, "middle": width / 2, "end": width}[anchor]
    pen, bp = SVGPathPen(gs), BoundsPen(gs)
    for c, a in zip(text, adv):
        t = (s, 0, 0, -s, x, y)
        gs[cmap[ord(c)]].draw(TransformPen(pen, t))
        gs[cmap[ord(c)]].draw(TransformPen(bp, t))
        x += a + tracking
    return pen.getCommands()


def label(text, x, y, size, wght=600, anchor="middle", fill="#1a1a1a", tracking_em=0.0):
    d = text_path(text, size, x, y, wght, anchor, tracking_em * size)
    return f'<path d="{d}" fill="{fill}"/>'


# ---- artwork -----------------------------------------------------------------
def read_art(fn):
    """(viewBox, inner SVG markup) of a print file."""
    s = open(fn).read()
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', s).group(1).split()]
    inner = s[s.index(">", s.index("<svg")) + 1: s.rindex("</svg>")]
    inner = re.sub(r"<title>.*?</title>", "", inner, flags=re.S)
    return vb, inner


def place(art, mm_w, x, y):
    (vx, vy, vw, vh), inner = art
    k = mm_w / vw
    return (f'<g transform="translate({x:.2f} {y:.2f}) scale({k:.6f}) '
            f'translate({-vx:.2f} {-vy:.2f})">{inner}</g>')


def print_file(art, mm_w, title):
    (vx, vy, vw, vh), inner = art
    mm_h = mm_w * vh / vw
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{mm_w:g}mm" height="{mm_h:.2f}mm" '
            f'viewBox="{vx:.2f} {vy:.2f} {vw:.2f} {vh:.2f}">\n<title>{title}</title>{inner}</svg>\n'), mm_h


def export(svg, base, mm_w):
    with open(base + ".svg", "w") as f:
        f.write(svg)
    cairosvg.svg2pdf(bytestring=svg.encode(), write_to=base + ".pdf")
    shutil.copyfile(base + ".pdf", base + ".ai")  # PDF-compatible .ai, as in the BIGBANG pack
    px = round(mm_w / 25.4 * DPI)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=base + f"_{DPI}dpi.png", output_width=px)


# ---- sheet drawing (same tee and dimension style as the BIGBANG spec) ----------
def tee(cx, top, back, fill):
    """Simple oversized tee silhouette in mm (body 580 wide, 740 long)."""
    dark = fill.lower() in ("#121212", "#000000")
    edge, rib, rib_l, seam, neck = (("#2a2a2a", "#1e1e1e", "#2c2c2c", "#262626", "#050505") if dark
                                    else ("#b9b8b2", "#e6e5e0", "#c9c8c2", "#cfcec8", "#e2e1dc"))

    def P(x, y):
        return f"{cx + x:.1f},{top + y:.1f}"
    drop = 22 if back else 88
    out = (f"M{P(-95, 0)} C{P(-88, drop * .7)} {P(-50, drop)} {P(0, drop)} C{P(50, drop)} {P(88, drop * .7)} {P(95, 0)} "
           f"Q{P(180, 18)} {P(268, 52)} Q{P(330, 160)} {P(392, 290)} L{P(302, 350)} Q{P(292, 300)} {P(290, 262)} "
           f"Q{P(287, 500)} {P(292, 742)} Q{P(0, 752)} {P(-292, 742)} Q{P(-287, 500)} {P(-290, 262)} "
           f"Q{P(-292, 300)} {P(-302, 350)} L{P(-392, 290)} Q{P(-330, 160)} {P(-268, 52)} Q{P(-180, 18)} {P(-95, 0)}Z")
    inner = (f"M{P(-95, 0)} C{P(-88, 16)} {P(-50, 24)} {P(0, 24)} C{P(50, 24)} {P(88, 16)} {P(95, 0)} "
             f"C{P(88, drop * .7)} {P(50, drop)} {P(0, drop)} C{P(-50, drop)} {P(-88, drop * .7)} {P(-95, 0)}Z")
    ribp = f"M{P(-95, 0)} C{P(-88, drop * .7)} {P(-50, drop)} {P(0, drop)} C{P(50, drop)} {P(88, drop * .7)} {P(95, 0)}"
    seams = (f"M{P(-268, 52)} Q{P(-282, 160)} {P(-290, 262)} M{P(268, 52)} Q{P(282, 160)} {P(290, 262)} "
             f"M{P(-392, 290)} L{P(-302, 350)} M{P(392, 290)} L{P(302, 350)} M{P(-290, 715)} Q{P(0, 724)} {P(290, 715)}")
    return [f'<path d="{out}" fill="{fill}" stroke="{edge}" stroke-width="1.5"/>',
            "" if back else f'<path d="{inner}" fill="{neck}"/>',
            f'<path d="{ribp}" fill="none" stroke="{rib}" stroke-width="16" stroke-linecap="round"/>',
            f'<path d="{ribp}" fill="none" stroke="{rib_l}" stroke-width="1.2"/>',
            f'<path d="{seams}" fill="none" stroke="{seam}" stroke-width="1.4" stroke-dasharray="3 2"/>']


def hdim(x0, x1, y, text, col="#d0245e"):
    t = 6
    return (f'<g stroke="{col}" stroke-width="1.6" fill="none"><path d="M{x0},{y} L{x1},{y} M{x0},{y - t} L{x0},{y + t} '
            f'M{x1},{y - t} L{x1},{y + t}"/></g>' + label(text, (x0 + x1) / 2, y - 9, 15, 600, fill=col))


def vdim(x, y0, y1, text, col="#d0245e", side=1):
    t = 6
    return (f'<g stroke="{col}" stroke-width="1.6" fill="none"><path d="M{x},{y0} L{x},{y1} M{x - t},{y0} L{x + t},{y0} '
            f'M{x - t},{y1} L{x + t},{y1}"/></g>'
            + label(text, x + side * 10, (y0 + y1) / 2 + 5, 15, 600, anchor="start" if side > 0 else "end", fill=col))


def spec_sheet(cw, front, back, front_h, back_h):
    sheet_w, sheet_h, top = 1700, 1202, 70
    fcx, bcx = 440, 1260
    collar_f, collar_b = top + 88, top + 22  # centre-front / centre-back collar seam
    f_x, f_y = fcx + FRONT_FROM_CENTRE_MM, collar_f + FRONT_BELOW_COLLAR_MM
    b_x, b_y = bcx - BACK_W_MM / 2, collar_b + BACK_BELOW_COLLAR_MM
    guide = 'stroke="#8a8a8a" stroke-width="1" stroke-dasharray="6 5"'
    f_mid = f_x + FRONT_W_MM / 2
    body = [f'<rect width="{sheet_w}" height="{sheet_h}" fill="#f4f2ee"/>']
    body += tee(fcx, top, False, cw["shirt"])
    body += [f'<path d="M{fcx},{collar_f} L{fcx},{top + 760}" {guide}/>',
             f'<path d="M{fcx},{collar_f} L{f_mid + 8},{collar_f}" {guide}/>',
             place(front, FRONT_W_MM, f_x, f_y)]
    body += tee(bcx, top, True, cw["shirt"])
    body += [f'<path d="M{bcx},{collar_b} L{bcx},{top + 760}" {guide}/>', place(back, BACK_W_MM, b_x, b_y)]
    body.append(label("FRONT", fcx, top + 810, 22, 700, tracking_em=0.3))
    body.append(label("BACK", bcx, top + 810, 22, 700, tracking_em=0.3))
    # Front dimensions.
    body.append(vdim(f_mid, collar_f, f_y, f"{FRONT_BELOW_COLLAR_MM / 10:g} cm below collar"))
    body.append(vdim(f_x + FRONT_W_MM + 16, f_y, f_y + front_h, f"{front_h / 10:.1f} cm"))
    body.append(hdim(f_x, f_x + FRONT_W_MM, f_y + front_h + 30, f"{FRONT_W_MM / 10:g} cm"))
    body.append(hdim(fcx, f_x, f_y + front_h + 70, f"{FRONT_FROM_CENTRE_MM / 10:g} cm from centre"))
    # Back dimensions.
    body.append(vdim(bcx, collar_b, b_y, f"{BACK_BELOW_COLLAR_MM / 10:g} cm below collar"))
    body.append(vdim(b_x + BACK_W_MM + 16, b_y, b_y + back_h, f"{back_h / 10:.1f} cm"))
    body.append(hdim(b_x, b_x + BACK_W_MM, b_y + back_h + 30, f"{BACK_W_MM / 10:g} cm"))
    notes_left = [
        ("GARMENT", cw["garment"]),
        ("PRINT METHOD", "Screen print (spot colours), or DTF / DTG"),
        ("FRONT", f"Wearer's left chest, {FRONT_W_MM / 10:g} x {front_h / 10:.1f} cm, blue / red / yellow"),
        ("BACK", f"Centred, {BACK_W_MM / 10:g} x {back_h / 10:.1f} cm, {cw['back_ink']}"),
    ]
    notes_right = [
        ("FILES", "FRONT / BACK as .ai + .pdf + .svg, .png 300 dpi"),
        ("COLOUR", cw["colour"]),
        ("BACKGROUND", cw["background"]),
        ("SIZING", "Same print size on all shirt sizes unless noted"),
    ]
    y0 = 990
    body.append(f'<path d="M80,{y0 - 50} L{sheet_w - 80},{y0 - 50}" stroke="#cfcac2" stroke-width="1.5"/>')
    for col_x, notes in ((80, notes_left), (880, notes_right)):
        for i, (k, v) in enumerate(notes):
            yy = y0 + i * 48
            body.append(label(k, col_x, yy, 15, 700, anchor="start", fill="#8a1c45", tracking_em=0.18))
            body.append(label(v, col_x + 200, yy, 17, 500, anchor="start"))
    title = f"BIIIG CONCERT TEE  ·  {cw['name'].upper()} TEE  ·  PRINT SPEC"
    body.append(label(title, 80, 46, 20, 700, anchor="start", tracking_em=0.18))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="420mm" height="297mm" '
            f'viewBox="0 0 {sheet_w} {sheet_h}">' + "".join(body) + "</svg>")


front = read_art(f"{SRC}/front-biiig.svg")
os.makedirs(f"{OUT}/spec-sheets", exist_ok=True)
for name, cw in COLOURWAYS.items():
    cw["name"] = name
    back = read_art(f"{SRC}/{cw['back_svg']}")
    d = f"{OUT}/print-files/{name}-tee"
    os.makedirs(d, exist_ok=True)
    fsvg, front_h = print_file(front, FRONT_W_MM, "BIIIG front, left chest")
    bsvg, back_h = print_file(back, BACK_W_MM, f"BIIIG back, {name} tee")
    export(fsvg, f"{d}/FRONT_left-chest_{FRONT_W_MM}x{front_h:.1f}mm_{name}-tee", FRONT_W_MM)
    export(bsvg, f"{d}/BACK_{BACK_W_MM}x{back_h:.1f}mm_{name}-tee", BACK_W_MM)
    sheet = spec_sheet(cw, front, back, front_h, back_h)
    base = f"{OUT}/spec-sheets/spec-sheet_{name}-tee"
    cairosvg.svg2pdf(bytestring=sheet.encode(), write_to=base + ".pdf")
    cairosvg.svg2png(bytestring=sheet.encode(), write_to=base + ".png", output_width=3400)
    print(f"{name}: front {FRONT_W_MM} x {front_h:.1f} mm, back {BACK_W_MM} x {back_h:.1f} mm")
