"""BIIIG tee ghost-mannequin mockups.

Composites the real print SVGs onto the four blank Higgsfield ghost-mannequin
tees (black / white, front / back), the same way the BIGBANG SG set was made:
fabric shading from the blank is applied to the ink, then the 1792x2240 plate
is cut down to 1080x1350 with a small label and, on fronts, a zoom circle.

Usage: python3 build_mockups.py <blanks_dir> <svg_dir> <out_dir>
"""
import io
import os
import re
import sys

import cairosvg
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

BLANKS, SVGS, OUT = sys.argv[1:4]
os.makedirs(OUT, exist_ok=True)

# ---- settings -------------------------------------------------------------
FRONT_W_CM = float(os.environ.get("FRONT_W_CM", "10"))      # emblem width
FRONT_TOP_CM = float(os.environ.get("FRONT_TOP_CM", "18"))  # top below collar
FRONT_IN_CM = float(os.environ.get("FRONT_IN_CM", "10"))   # centre line -> left edge
BACK_W_CM = float(os.environ.get("BACK_W_CM", "32"))        # back width
BACK_TOP_CM = float(os.environ.get("BACK_TOP_CM", "15"))    # top below collar
BLACK_INK = "#0D0D09"
BLUE, RED, YELLOW = "#0756C6", "#E73A07", "#FDBB05"  # the front's three inks
# White-tee back: "tricolour" (blue / red / yellow, left to right) or "mono" (black).
WHITE_BACK = os.environ.get("WHITE_BACK", "tricolour")
FABRIC = os.environ.get("FABRIC", "Combed 24s / Bamboo")
KICKER = "BIIIG TEE"

# Calibration on the 1792x2240 blanks (same values the BIGBANG set used):
# px per cm, centre-line x, collar-seam y.
CAL = {
    "black_front": (14.77, 898.8, 420.4),
    "black_back": (15.12, 903.0, 280.2),
    "white_front": (15.19, 894.5, 405.1),
    "white_back": (15.02, 903.5, 284.7),
}

FONT_DIR = "/usr/share/fonts/opentype/inter"


def font(weight, size):
    return ImageFont.truetype(f"{FONT_DIR}/Inter-{weight}.otf", size)


def tricolour_back(path):
    """back-iii.svg in the front's three inks: blue, red, yellow, left to right.

    The art is one path: three equal circles (r 255.15, centres x 565 / 960 /
    1355, y 335.55) over the III (slot centres x 759 / 1161), as built by
    ../vector-rebuild/rebuild.py. It is drawn
    blue, then red clipped to the middle circle plus the III right of the first
    slot, then yellow clipped to the right circle plus the III right of the
    second slot. Each circle stays whole, layered left to right (so the flames
    sit in red and yellow), and the colours butt together with no gap.
    """
    svg = open(path).read()
    d = re.search(r' d="([^"]*)"', svg).group(1)
    split_y = 657  # between the circles (bottom ~590) and the III (top 704.3)
    r = 256  # a hair over the art's radius so the clip edge never shows

    def clip(i, cx, slot_x):
        return (f'<clipPath id="c{i}"><circle cx="{cx}" cy="335.55" r="{r}"/>'
                f'<rect x="{slot_x}" y="{split_y}" width="1e4" height="1e4"/></clipPath>')

    head = svg[: svg.index("<path")]
    return (head + f'<defs>{clip(0, 960, 759)}{clip(1, 1355, 1161)}</defs>'
            f'<path fill="{BLUE}" d="{d}"/>'
            f'<path fill="{RED}" clip-path="url(#c0)" d="{d}"/>'
            f'<path fill="{YELLOW}" clip-path="url(#c1)" d="{d}"/>'
            "</svg>")


def render_svg(path, width_px, recolour=None, svg=None):
    svg = svg or open(path).read()
    if recolour:
        for old, new in recolour.items():
            svg = re.sub(old, new, svg, flags=re.I)
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=int(round(width_px)))
    return Image.open(io.BytesIO(png)).convert("RGBA")


def svg_aspect(path):
    vb = re.search(r'viewBox="([\d.\s-]+)"', open(path).read()).group(1).split()
    return float(vb[2]) / float(vb[3])


def shade_print(blank, art, x, y, dark_shirt):
    """Lay art (RGBA) on blank at (x, y) with the fabric's folds and grain."""
    w, h = art.size
    region = blank.crop((x, y, x + w, y + h))
    lum = np.asarray(region.convert("L")).astype(np.float32)
    # Big folds: luminance relative to the shirt's typical value.
    big = np.asarray(region.convert("L").filter(ImageFilter.GaussianBlur(10))).astype(np.float32)
    ref = np.median(np.asarray(blank.convert("L")).astype(np.float32)[700:1500, 600:1200])
    if dark_shirt:
        fold = np.clip(1 + 0.30 * (big / ref - 1), 0.80, 1.06)
    else:
        fold = np.clip(big / ref, 0.78, 1.03)
    # Fine grain: high-pass of the knit.
    fine = np.asarray(region.convert("L").filter(ImageFilter.GaussianBlur(1.5))).astype(np.float32)
    grain = np.clip(1 + (0.9 if dark_shirt else 0.6) * (lum - fine) / max(ref, 40), 0.9, 1.1)
    a = np.asarray(art).astype(np.float32)
    rgb = a[..., :3] * (fold * grain)[..., None]
    alpha = a[..., 3:4] / 255.0 * 0.97
    base = np.asarray(region.convert("RGB")).astype(np.float32)
    out = base * (1 - alpha) + np.clip(rgb, 0, 255) * alpha
    blank.paste(Image.fromarray(out.astype(np.uint8)), (x, y))
    return (x, y, w, h)


def label(img, view, colour_name, dark_bg_text=(20, 20, 20)):
    d = ImageDraw.Draw(img)
    kicker = f"{KICKER} · {view.upper()}"
    x, y = 55, 48
    f1 = font("SemiBold", 21)
    cx = x
    for ch in kicker:  # letter-spaced kicker
        d.text((cx, y), ch, font=f1, fill=(95, 95, 95))
        cx += d.textlength(ch, font=f1) + 2.2
    d.text((x - 3, y + 30), colour_name, font=font("Bold", 62), fill=dark_bg_text)
    d.text((x, y + 108), FABRIC, font=font("Medium", 22), fill=(95, 95, 95))


def zoom_circle(img, src, box, size_text):
    """Magnified view of the emblem in a white-rimmed circle, bottom right."""
    bx, by, bw, bh = box
    R = 172
    cxy = (img.width - 55 - R, img.height - 70 - R)
    # Square crop centred on the print, a little wider than it.
    side = int(max(bw, bh) * 1.45)
    mx, my = bx + bw / 2, by + bh / 2
    crop = src.crop((int(mx - side / 2), int(my - side / 2), int(mx + side / 2), int(my + side / 2)))
    crop = crop.resize((2 * R, 2 * R), Image.LANCZOS)
    mask = Image.new("L", (2 * R, 2 * R), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, 2 * R - 1, 2 * R - 1), fill=255)
    # Soft shadow.
    sh = Image.new("L", img.size, 0)
    ImageDraw.Draw(sh).ellipse((cxy[0] - R - 2, cxy[1] - R + 8, cxy[0] + R + 2, cxy[1] + R + 14), fill=90)
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    img.paste(Image.new("RGB", img.size, (0, 0, 0)), (0, 0), sh)
    ring = 7
    d = ImageDraw.Draw(img)
    d.ellipse((cxy[0] - R - ring, cxy[1] - R - ring, cxy[0] + R + ring, cxy[1] + R + ring), fill=(255, 255, 255))
    img.paste(crop, (cxy[0] - R, cxy[1] - R), mask)
    # Size pill.
    f = font("SemiBold", 19)
    tw = d.textlength(size_text, font=f)
    pw, ph = tw + 34, 36
    px, py = cxy[0] - pw / 2, cxy[1] + R - ph / 2 + 4
    d.rounded_rectangle((px, py, px + pw, py + ph), radius=ph / 2, fill=(255, 255, 255), outline=(225, 225, 225))
    d.text((cxy[0] - tw / 2, py + 7), size_text, font=f, fill=(30, 30, 30))


def to_post(plate):
    # 1792x2240 -> 1080x1350 (same 4:5 frame).
    return plate.resize((1080, 1350), Image.LANCZOS)


front_svg = f"{SVGS}/front-biiig.svg"
back_svg = f"{SVGS}/back-iii.svg"
front_h_cm = FRONT_W_CM / svg_aspect(front_svg)
back_h_cm = BACK_W_CM / svg_aspect(back_svg)

jobs = [
    ("01_black_front", "black_front", "Front", "Black", True),
    ("02_black_back", "black_back", "Back", "Black", True),
    ("03_white_front", "white_front", "Front", "White", False),
    ("04_white_back", "white_back", "Back", "White", False),
]
for out_name, blank_name, view, colour, dark in jobs:
    ppcm, cx, collar = CAL[blank_name]
    blank = Image.open(f"{BLANKS}/{blank_name}.jpg").convert("RGB")
    if view == "Front":
        art = render_svg(front_svg, FRONT_W_CM * ppcm)
        x = int(round(cx + FRONT_IN_CM * ppcm))
        y = int(round(collar + FRONT_TOP_CM * ppcm))
    else:
        recolour, svg = None, None
        if not dark and WHITE_BACK == "mono":
            recolour = {"#FFFFFF": BLACK_INK}
        elif not dark:
            svg = tricolour_back(back_svg)
            with open(f"{OUT}/back-iii_white-tee.svg", "w") as f:  # print file
                f.write(svg)
        art = render_svg(back_svg, BACK_W_CM * ppcm, recolour, svg)
        x = int(round(cx - art.width / 2))
        y = int(round(collar + BACK_TOP_CM * ppcm))
    box = shade_print(blank, art, x, y, dark)
    post = to_post(blank)
    label(post, view, colour)
    if view == "Front":
        # Zoom from the full-res plate for sharpness.
        zoom_circle(post, blank, box, f"{FRONT_W_CM:g} × {front_h_cm:.1f} cm")
    post.save(f"{OUT}/{out_name}.jpg", quality=92)
    print(f"{out_name}: {ppcm} px/cm, art {art.width}x{art.height} at ({x},{y})")
print(f"front {FRONT_W_CM:g} x {front_h_cm:.2f} cm; back {BACK_W_CM:g} x {back_h_cm:.2f} cm")
