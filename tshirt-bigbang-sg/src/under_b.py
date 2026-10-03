#!/usr/bin/env python3
"""Option-2 variants with the red peony + yellow rose group shrunk to sit
below the B (a bit wider than it), in three alignments.

Reads src/assets/option-2.png (from options.py) and the B placement in
build.py; writes src/assets/under-b-<align>.png plus print files and
mockups under ../print-files/options/ and ../mockup/options/.

    python3 under_b.py
"""
import json
import os

import cairosvg
import numpy as np
from PIL import Image

import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(HERE, "assets", "option-2.png")
OUT_PRINT = os.path.join(ROOT, "print-files", "options")
OUT_MOCK = os.path.join(ROOT, "mockup", "options")

GROUP_W = 1.15       # bottom group width as a multiple of the B's width
GAP = -0.14          # space between B and the group (share of B height); negative = tucked behind the B
ALIGNS = {           # group centre relative to the B centre, as a share of B width
    "nudged-left-hug": -0.12,
}
S = 1000


def b_rect_units():
    """The B's box on the current artboard (units), as build.front_art places it."""
    _, (bx0, by0, bx1, by1) = build.text_path(build.SLAB, "B", 1000, 0, 0, build.B_XSCALE)
    b_w = S * build.B_WIDTH
    b_h = (by1 - by0) * b_w / (bx1 - bx0)
    nx, ny = build.B_NUDGE
    cx = S / 2 + nx
    top = S / 2 - b_h / 2 + 10 + ny
    return cx - b_w / 2, top, cx + b_w / 2, top + b_h


def art_transform(alpha_img):
    """(bbox, k, ox, oy) used by build.watercolour_layer to fit art on the artboard."""
    bbox = alpha_img.point(lambda v: 255 if v > 8 else 0).getbbox()
    bw, bh = bbox[2] - bbox[0], bbox[3] - bbox[1]
    k = S / max(bw, bh)
    return bbox, k, (S - bw * k) / 2, (S - bh * k) / 2


def main():
    os.makedirs(OUT_PRINT, exist_ok=True)
    os.makedirs(OUT_MOCK, exist_ok=True)
    im = Image.open(SRC).convert("RGBA")
    rgba = np.array(im)
    a = rgba[..., 3]
    bbox, k, ox, oy = art_transform(im.getchannel("A"))
    to_px = lambda u, v: (bbox[0] + (u - ox) / k, bbox[1] + (v - oy) / k)

    ux0, uy0, ux1, uy1 = b_rect_units()
    (bx0, by0), (bx1, by1) = to_px(ux0, uy0), to_px(ux1, uy1)
    b_w_px, b_h_px = bx1 - bx0, by1 - by0

    # split top spray / bottom group at the emptiest row between them
    rows = (a > 8).sum(1)
    lo, hi = int(by0), int(by1 + b_h_px)
    split = lo + int(np.argmin(rows[lo:hi]))
    top_part = rgba.copy()
    top_part[split:, :, 3] = 0
    bottom = Image.fromarray(rgba[split:])
    bottom = bottom.crop(bottom.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox())

    s = GROUP_W * b_w_px / bottom.width
    bottom = bottom.resize((round(bottom.width * s), round(bottom.height * s)), Image.LANCZOS)
    gy = int(by1 + GAP * b_h_px)
    b_cx = (bx0 + bx1) / 2

    back = build.back_art()
    for name, off in ALIGNS.items():
        gx = int(bx0) if off is None else int(b_cx + off * b_w_px - bottom.width / 2)
        pad = max(0, -gx) + 50
        h = max(rgba.shape[0], gy + bottom.height) + 50
        w = max(rgba.shape[1], gx + bottom.width) + pad + 50
        canvas = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        canvas.alpha_composite(Image.fromarray(top_part), (pad, 0))
        canvas.alpha_composite(bottom, (gx + pad, gy))
        out_png = os.path.join(HERE, "assets", f"under-b-{name}.png")
        canvas.save(out_png, optimize=True)

        # re-derive the B's size/position on the new artboard
        nbbox, nk, nox, noy = art_transform(canvas.getchannel("A"))
        to_u = lambda px, py: (nox + (px - nbbox[0]) * nk, noy + (py - nbbox[1]) * nk)
        (nux0, nuy0), (nux1, nuy1) = to_u(bx0 + pad, by0), to_u(bx1 + pad, by1)
        build.EDITED_PNG = out_png
        build.B_WIDTH = (nux1 - nux0) / S
        b_h_u = nuy1 - nuy0
        build.B_NUDGE = ((nux0 + nux1) / 2 - S / 2, nuy0 - (S / 2 - b_h_u / 2 + 10))
        with open(os.path.join(HERE, "assets", f"under-b-{name}.json"), "w") as fh:
            json.dump({"png": os.path.basename(out_png), "B_WIDTH": build.B_WIDTH, "B_NUDGE": build.B_NUDGE,
                       "split_y": split - 0 + 0, "pad": pad, "group_xy": [gx + pad, gy],
                       "group_size": list(bottom.size)}, fh, indent=1)
        front = build.front_art()
        fdefs, fbody, fW, fH = front
        base = os.path.join(OUT_PRINT, f"FRONT_under-b-{name}_{build.FRONT_MM}x{build.FRONT_MM}mm")
        build.export(build.svg_doc(build.FRONT_MM, build.FRONT_MM, fW, fH, fdefs, fbody), base, build.FRONT_MM)
        cairosvg.svg2png(bytestring=build.svg_doc(build.FRONT_MM, build.FRONT_MM, fW, fH, fdefs, fbody,
                                                  bg=build.SHIRT).encode(),
                         write_to=os.path.join(OUT_MOCK, f"under-b-{name}_emblem.png"), output_width=1600)
        mock = build.mockup_svg(front, back, annotate=False)
        cairosvg.svg2png(bytestring=mock.encode(), write_to=os.path.join(OUT_MOCK, f"under-b-{name}_mockup.png"),
                         output_width=3400)
        print(f"{name}: B {build.B_WIDTH * build.FRONT_MM / 10:.1f} cm wide, nudge "
              f"({build.B_NUDGE[0]:.0f}, {build.B_NUDGE[1]:.0f})", flush=True)


if __name__ == "__main__":
    main()
