#!/usr/bin/env python3
"""Editable Illustrator files for the final design.

Writes ../illustrator/:
  FRONT_left-chest_100x100mm.ai / .svg  - flowers split into two placed images
                                          (iris spray, peony + rose) + vector B
  BACK_<w>x<h>mm.ai / .svg              - vector wordmark + brushed keys

The .ai files are PDF-compatible (the same container Illustrator uses for
"Create PDF Compatible File"), so Illustrator opens and edits them directly;
File > Save As > Illustrator (.ai) once makes them fully native. The .svg
files keep the named layers/groups.

    python3 make_ai.py
"""
import base64
import io
import json
import os
import re

import cairosvg
from PIL import Image

import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "illustrator")
SETTINGS = os.path.join(HERE, "assets", "under-b-nudged-left-hug.json")
S = 1000


def _ink_bbox(im):
    return im.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()


def _image_el(gid, im, x, y, w, h):
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True)
    data = base64.b64encode(buf.getvalue()).decode()
    return (f'<image id="{gid}" x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" '
            f'preserveAspectRatio="none" xlink:href="data:image/png;base64,{data}"/>')


def front_svg():
    cfg = json.load(open(SETTINGS))
    canvas_path = os.path.join(HERE, "assets", cfg["png"])
    build.EDITED_PNG = canvas_path
    build.B_WIDTH = cfg["B_WIDTH"]
    build.B_NUDGE = tuple(cfg["B_NUDGE"])
    defs, body, W, H = build.front_art()

    # same crop/fit as build.watercolour_layer, so pieces land exactly where the
    # single image was
    canvas = Image.open(canvas_path).convert("RGBA")
    r, g, b, a = canvas.split()
    canvas = Image.merge("RGBA", (r, g, b, a.point(lambda v: 255 if v >= 240 else v)))
    bx0, by0, bx1, by1 = _ink_bbox(canvas)
    k = S / max(bx1 - bx0, by1 - by0)
    ox, oy = (S - (bx1 - bx0) * k) / 2, (S - (by1 - by0) * k) / 2

    gx, gy = cfg["group_xy"]
    gw, gh = cfg["group_size"]
    regions = {
        "flowers-iris-spray": (0, 0, canvas.width, cfg["split_y"]),
        "flowers-peony-rose": (gx, gy, gx + gw, gy + gh),
    }
    pieces = []
    for gid, (x0, y0, x1, y1) in regions.items():
        part = canvas.crop((x0, y0, x1, y1))
        px0, py0, px1, py1 = _ink_bbox(part)
        part = part.crop((px0, py0, px1, py1))
        X, Y = x0 + px0, y0 + py0
        pieces.append(_image_el(gid, part, ox + (X - bx0) * k, oy + (Y - by0) * k, part.width * k, part.height * k))

    flowers = body[0]
    flowers = re.sub(r'<image id="watercolour-flowers"[^>]*/>', lambda m: "".join(pieces), flowers, count=1)
    assert "flowers-peony-rose" in flowers
    body = [flowers.replace('inkscape:label="Flowers (full colour)"',
                            'inkscape:label="Flowers (full colour) - 2 pieces"')] + body[1:]
    return defs, body, W, H


def main():
    os.makedirs(OUT, exist_ok=True)
    fdefs, fbody, fW, fH = front_svg()
    front = build.svg_doc(build.FRONT_MM, build.FRONT_MM, fW, fH, fdefs, fbody)
    bdefs, bbody, bW, bH = build.back_art()
    back_h = round(bH / 10, 1)
    back = build.svg_doc(build.BACK_W_MM, back_h, bW, bH, bdefs, bbody)
    for name, svg in ((f"FRONT_left-chest_{build.FRONT_MM}x{build.FRONT_MM}mm", front),
                      (f"BACK_{build.BACK_W_MM}x{back_h:g}mm", back)):
        base = os.path.join(OUT, name)
        open(base + ".svg", "w").write(svg)
        cairosvg.svg2pdf(bytestring=svg.encode(), write_to=base + ".ai")
        cairosvg.svg2png(bytestring=svg.encode(), write_to=base + "_check.png", output_width=1200,
                         background_color=build.SHIRT)
        print("wrote", os.path.relpath(base, ROOT) + ".ai/.svg")


if __name__ == "__main__":
    main()
