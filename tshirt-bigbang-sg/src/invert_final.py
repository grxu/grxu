#!/usr/bin/env python3
"""White-tee and black-tee versions of the final artwork, edited directly in the
vector files.

Reads the raw Illustrator files in ../final-raw/ and writes ../final/white-tee/
and ../final/black-tee/. Both get the background rectangles removed and the
full-res flowers; the white tee additionally recolours as follows:
  - FRONT: black background removed, B filled black, its outline stroke made
    white (a thin gap against the flowers), and the two flower images replaced
    by the full-resolution originals at exactly the same placement.
  - BACK: grey background removed, BIGBANG wordmark and piano keys black;
    the characters are left untouched.
  - .ai (PDF-compatible) + .pdf, transparent PNG renders, a white-shirt
    mockup and the vendor spec sheet.

    python3 invert_final.py
"""
import base64
import io
import json
import os
import subprocess
import tempfile

import cairosvg
import numpy as np
import pikepdf
from PIL import Image

import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RAW = os.path.join(ROOT, "final-raw")
OUT = os.path.join(ROOT, "final")
FRONT_IN = os.path.join(RAW, "FRONT_left-chest_100x100mm.ai")
BACK_IN = os.path.join(RAW, "BACK_277.5x317.4mm.ai")
SHIRT_WHITE = "#f7f7f5"


# ------------------------------------------------------------------ helpers
def walk_fills(ops):
    """Yield (op_index, fill_rgb, bbox_pt) for every painted path, tracking q/Q and cm."""
    fill, stack, ctm, pts = None, [], [1, 0, 0, 1, 0, 0], []

    def tf(x, y):
        a, b, c, d, e, f = ctm
        return a * x + c * y + e, b * x + d * y + f

    for i, (operands, op) in enumerate(ops):
        o = str(op)
        if o == "q":
            stack.append((ctm[:], fill))
        elif o == "Q":
            ctm, fill = stack.pop()
        elif o == "cm":
            a2, b2, c2, d2, e2, f2 = [float(v) for v in operands]
            a, b, c, d, e, f = ctm
            ctm = [a2 * a + b2 * c, a2 * b + b2 * d, c2 * a + d2 * c, c2 * b + d2 * d,
                   e2 * a + f2 * c + e, e2 * b + f2 * d + f]
        elif o == "rg":
            fill = tuple(round(float(v), 3) for v in operands)
        elif o in ("m", "l"):
            pts.append(tf(float(operands[0]), float(operands[1])))
        elif o == "c":
            pts.append(tf(float(operands[4]), float(operands[5])))
        elif o == "re":
            x, y, w, h = [float(v) for v in operands]
            pts += [tf(x, y), tf(x + w, y + h)]
        elif o in ("f", "f*", "F", "B", "B*", "S", "n"):
            if pts and o in ("f", "f*", "F", "B", "B*"):
                xs, ys = [p[0] for p in pts], [p[1] for p in pts]
                yield i, fill, (min(xs), min(ys), max(xs), max(ys))
            pts = []


def set_fill_before(ops, i, rgb):
    """Make the path painted at ops[i] use `rgb`, without touching other paths:
    a new rg goes right before the path starts, and q/Q keep it local."""
    start = i
    while start > 0 and str(ops[start - 1][1]) in ("m", "l", "c", "v", "y", "h", "re"):
        start -= 1
    ops.insert(i + 1, pikepdf.ContentStreamInstruction([], pikepdf.Operator("Q")))
    ops.insert(start, pikepdf.ContentStreamInstruction([*rgb], pikepdf.Operator("rg")))
    ops.insert(start, pikepdf.ContentStreamInstruction([], pikepdf.Operator("q")))


def mm(pt):
    return pt / 72 * 25.4


def full_res_pieces():
    """The two flower pieces exactly as make_ai.py cut them (before Illustrator downsampled them)."""
    cfg = json.load(open(os.path.join(HERE, "assets", "under-b-nudged-left-hug.json")))
    canvas = Image.open(os.path.join(HERE, "assets", cfg["png"])).convert("RGBA")
    r, g, b, a = canvas.split()
    canvas = Image.merge("RGBA", (r, g, b, a.point(lambda v: 255 if v >= 240 else v)))
    gx, gy = cfg["group_xy"]
    gw, gh = cfg["group_size"]
    out = []
    for x0, y0, x1, y1 in ((0, 0, canvas.width, cfg["split_y"]), (gx, gy, gx + gw, gy + gh)):
        part = canvas.crop((x0, y0, x1, y1))
        part = part.crop(part.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox())
        out.append(part)
    return out  # [iris spray, peony + rose]


def image_xobject(pdf, im):
    """RGB image XObject with its alpha as a soft mask (lossless)."""
    rgb = im.convert("RGB")
    alpha = im.getchannel("A")
    import zlib
    smask = pikepdf.Stream(pdf, zlib.compress(alpha.tobytes(), 9))
    smask.update({"/Type": pikepdf.Name.XObject, "/Subtype": pikepdf.Name.Image, "/Width": im.width,
                  "/Height": im.height, "/ColorSpace": pikepdf.Name.DeviceGray, "/BitsPerComponent": 8,
                  "/Filter": pikepdf.Name.FlateDecode})
    img = pikepdf.Stream(pdf, zlib.compress(rgb.tobytes(), 9))
    img.update({"/Type": pikepdf.Name.XObject, "/Subtype": pikepdf.Name.Image, "/Width": im.width,
                "/Height": im.height, "/ColorSpace": pikepdf.Name.DeviceRGB, "/BitsPerComponent": 8,
                "/Filter": pikepdf.Name.FlateDecode, "/SMask": smask})
    return img


def check_match(old_xobj, new_im):
    """Sanity check: the full-res piece really is the image in the user's file."""
    old = pikepdf.PdfImage(old_xobj).as_pil_image().convert("RGB")
    new = new_im.convert("RGB").resize(old.size, Image.LANCZOS)
    a = np.asarray(old, float)
    b = np.asarray(new, float)
    mask = np.asarray(new_im.getchannel("A").resize(old.size), float) > 200
    return float(np.abs(a - b)[mask].mean())


# ------------------------------------------------------------------ front
def invert_front(dst, white_tee=True):
    pdf = pikepdf.open(FRONT_IN)
    fm = pdf.pages[0].Resources.XObject["/Fm0"]
    ops = list(pikepdf.parse_content_stream(fm))
    painted = list(walk_fills(ops))
    # 1. the full-artboard black rectangle: stop painting it
    i_bg = next(i for i, fill, bb in painted if fill == (0.0, 0.0, 0.0) and mm(bb[2] - bb[0]) > 99)
    ops[i_bg] = pikepdf.ContentStreamInstruction([], pikepdf.Operator("n"))
    # 2. white tee only - the B: white fill -> black, black outline stroke -> white
    for k, (operands, op) in enumerate(ops if white_tee else []):
        if str(op) == "rg" and [float(v) for v in operands] == [1, 1, 1]:
            ops[k] = pikepdf.ContentStreamInstruction([0, 0, 0], pikepdf.Operator("rg"))
        elif str(op) == "RG" and [float(v) for v in operands] == [0, 0, 0]:
            ops[k] = pikepdf.ContentStreamInstruction([1, 1, 1], pikepdf.Operator("RG"))
    # 3. flowers: swap the downsampled images (with their luminosity masks) for
    #    the full-res originals with real alpha; placement matrices stay as saved
    spray, peony = full_res_pieces()
    xo = fm.Resources.XObject
    report = {}
    for name, im in (("/Im0", spray), ("/Im1", peony)):
        report[name] = (int(xo[name].Width), int(xo[name].Height), im.size, check_match(xo[name], im))
        xo[name] = image_xobject(pdf, im)
    for k, (operands, op) in enumerate(ops):  # drop the old luminosity soft masks
        if str(op) == "gs" and str(operands[0]) in ("/GS1", "/GS2"):
            ops[k] = pikepdf.ContentStreamInstruction([pikepdf.Name("/GS0")], pikepdf.Operator("gs"))
    fm.write(pikepdf.unparse_content_stream(ops))
    pdf.save(dst)
    return report


# ------------------------------------------------------------------ back
def invert_back(dst, white_tee=True):
    pdf = pikepdf.open(BACK_IN)
    pg = pdf.pages[0]
    # Illustrator's private copy of the artwork would override our PDF edits
    # when reopened in Illustrator, so it goes (as does the stale thumbnail)
    for key in ("/PieceInfo", "/Thumb"):
        if key in pg.obj:
            del pg.obj[key]
    ops = list(pikepdf.parse_content_stream(pg))
    painted = list(walk_fills(ops))
    w_pt = float(pg.MediaBox[2]) - float(pg.MediaBox[0])
    targets, bg = [], None
    for i, fill, (x0, y0, x1, y1) in painted:
        if mm(x1 - x0) > mm(w_pt) - 1 and fill and max(fill) < 0.2:
            bg = i                                    # the dark artboard background
        elif fill == (1.0, 1.0, 1.0) and (mm(y1 - y0) > 100 or mm(x1 - x0) > 200):
            targets.append(i)                         # wordmark + piano keys
    assert bg is not None and len(targets) == 4, (bg, targets)
    for i in sorted(targets, reverse=True) if white_tee else []:
        set_fill_before(ops, i, (0, 0, 0))
    assert all(i > bg for i in targets)  # inserts land after the background, so its index holds
    ops[bg] = pikepdf.ContentStreamInstruction([], pikepdf.Operator("n"))
    pg.Contents = pdf.make_stream(pikepdf.unparse_content_stream(ops))
    pdf.save(dst)
    return len(targets)


# ------------------------------------------------------------------ renders + mockup
def render_png(pdf_path, png_path, dpi):
    with tempfile.TemporaryDirectory() as tmp:
        base = os.path.join(tmp, "r")
        subprocess.run(["pdftocairo", "-png", "-r", str(dpi), "-transp", "-singlefile", pdf_path, base], check=True)
        os.replace(base + ".png", png_path)


def art_tuple(png_path, w_units, h_units):
    buf = io.BytesIO()
    Image.open(png_path).save(buf, "PNG")
    data = base64.b64encode(buf.getvalue()).decode()
    body = [build.layer("layer-art", "Art", [f'<image x="0" y="0" width="{w_units}" height="{h_units}" '
                                             f'xlink:href="data:image/png;base64,{data}"/>'])]
    return [], body, w_units, h_units


LIGHT = {"#121212": SHIRT_WHITE, "#050505": "#e6e6e3", "#1e1e1e": "#ebebe8", "#2c2c2c": "#cdcdca",
         "#262626": "#d3d3d0", "#2a2a2a": "#c4c4c1"}
NOTES = {
    "Black cotton tee, oversized / drop-shoulder fit": "White cotton tee, oversized / drop-shoulder fit",
    "DTF or DTG, full colour + white underbase": "DTF or DTG, full colour on a white tee",
    "FRONT / BACK as .pdf + .svg, .png 300 dpi + 2048 px": "FRONT / BACK as .ai + .pdf, .png 300 dpi (+ hi-res front)",
    "sRGB artwork; white = 100% white ink": "sRGB artwork; black = 100% black",
    "Transparent - do NOT print the black": "Transparent - do NOT print a background",
}


def tee_mockup(front, back, back_w_mm, annotate, white_tee=True):
    orig_label, orig_w = build.label, build.BACK_W_MM
    build.BACK_W_MM = back_w_mm

    def label(text, *a, **k):
        if white_tee:
            text = NOTES.get(text, text)
        elif text == "FRONT / BACK as .pdf + .svg, .png 300 dpi + 2048 px":
            text = NOTES[text]
        if text.startswith("Centred,") and "white ink only" in text:
            text = text.replace("white ink only", ("black" if white_tee else "white") + " + full-colour characters")
        return orig_label(text, *a, **k)

    build.label = label
    try:
        svg = build.mockup_svg(front, back, annotate=annotate)
    finally:
        build.label, build.BACK_W_MM = orig_label, orig_w
    for dark, light in LIGHT.items() if white_tee else ():
        svg = svg.replace(f'"{dark}"', f'"{light}"')
    return svg


def build_colourway(white_tee):
    tag = "white-tee" if white_tee else "black-tee"
    out = os.path.join(OUT, tag)
    os.makedirs(out, exist_ok=True)
    front_pdf = os.path.join(out, f"FRONT_left-chest_100x100mm_{tag}.pdf")
    back_pdf = os.path.join(out, f"BACK_277.5x317.4mm_{tag}.pdf")
    report = invert_front(front_pdf, white_tee)
    n = invert_back(back_pdf, white_tee)
    for p in (front_pdf, back_pdf):  # PDF-compatible .ai twins for Illustrator
        with open(p, "rb") as src, open(p[:-4] + ".ai", "wb") as dst:
            dst.write(src.read())
    render_png(front_pdf, front_pdf[:-4] + "_300dpi.png", 300)
    render_png(front_pdf, front_pdf[:-4] + "_hires.png", 900)
    render_png(back_pdf, back_pdf[:-4] + "_300dpi.png", 300)

    front = art_tuple(front_pdf[:-4] + "_hires.png", 1000, 1000)
    back_png = os.path.join(tempfile.gettempdir(), f"back_mock_{tag}.png")
    render_png(back_pdf, back_png, 200)
    back = art_tuple(back_png, 2775, 3174)
    mock = tee_mockup(front, back, 277.5, False, white_tee)
    cairosvg.svg2png(bytestring=mock.encode(), write_to=os.path.join(out, f"mockup_{tag}.png"), output_width=3400)
    # the spec sheet is a reference document, so it embeds the 300 dpi art to stay light
    spec = tee_mockup(art_tuple(front_pdf[:-4] + "_300dpi.png", 1000, 1000), back, 277.5, True, white_tee)
    cairosvg.svg2pdf(bytestring=spec.encode(), write_to=os.path.join(out, f"spec-sheet_{tag}.pdf"))
    cairosvg.svg2png(bytestring=spec.encode(), write_to=os.path.join(out, f"spec-sheet_{tag}.png"), output_width=3400)
    print(tag, "front images swapped:", report, "| back shapes recoloured:", n if white_tee else 0)


def main():
    for white_tee in (True, False):
        build_colourway(white_tee)


if __name__ == "__main__":
    main()
