"""Watermarked copies of the mockups for posting.

Tiles "@dorotheaphils" across each image at a 28° angle, faint. Each letter
is light where the image under it is dark and dark where it is light, so the
mark reads the same on the grey backdrop, the black or white shirt and the
print. The label block at the top left is left clear.

Usage: python3 watermark.py <mockups_dir> <out_dir>
"""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

SRC, OUT = sys.argv[1:3]
os.makedirs(OUT, exist_ok=True)

TEXT = "@dorotheaphils"
FONT = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-SemiBold.otf", 30)
ANGLE = 28
GAP_X, GAP_Y = 120, 150      # space between repeats (px at 1080 wide)
ALPHA_ON_DARK = 0.17         # light text over dark areas
ALPHA_ON_LIGHT = 0.13        # dark text over light areas
LABEL_BOX = (40, 40, 430, 200)  # top-left label block, kept clear


def tile_mask(size):
    W, H = size
    big = Image.new("L", (W * 2, H * 2), 0)
    d = ImageDraw.Draw(big)
    step_x = d.textlength(TEXT, font=FONT) + GAP_X
    for row, y in enumerate(range(0, H * 2, GAP_Y)):
        x = -step_x + (row % 2) * step_x / 2
        while x < W * 2:
            d.text((x, y), TEXT, font=FONT, fill=255)
            x += step_x
    big = big.rotate(ANGLE, resample=Image.BICUBIC, center=(W, H))
    mask = big.crop((W // 2, H // 2, W // 2 + W, H // 2 + H))
    # Fade the mask out over the label block.
    clear = Image.new("L", size, 255)
    ImageDraw.Draw(clear).rectangle(LABEL_BOX, fill=0)
    clear = clear.filter(ImageFilter.GaussianBlur(12))
    return np.asarray(mask, np.float32) / 255 * np.asarray(clear, np.float32) / 255


for name in sorted(os.listdir(SRC)):
    if not (name.endswith(".jpg") and name[:2].isdigit()):
        continue
    im = Image.open(os.path.join(SRC, name)).convert("RGB")
    rgb = np.asarray(im, np.float32)
    m = tile_mask(im.size)
    # Local brightness decides the ink: light text on dark, dark on light.
    lum = np.asarray(im.convert("L").filter(ImageFilter.GaussianBlur(3)), np.float32)
    dark = lum < 128
    ink = np.where(dark[..., None], 255.0, 0.0)
    a = (m * np.where(dark, ALPHA_ON_DARK, ALPHA_ON_LIGHT))[..., None]
    out = rgb * (1 - a) + ink * a
    base = os.path.splitext(name)[0]
    Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(
        os.path.join(OUT, f"{base}_watermarked.jpg"), quality=92)
    print(base)
