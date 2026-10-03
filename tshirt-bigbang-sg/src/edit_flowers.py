#!/usr/bin/env python3
"""Rework the uploaded watercolour: drop the centre peony and pull the four
corner flowers together so their petals meet behind the B.

    pip install numpy scipy scikit-image pillow
    python3 edit_flowers.py        # -> src/assets/flowers-tight.png (used by build.py)

The source is the PNG in ../upload-here/ (untouched). Tune OFFSETS / ORDER
and re-run; then run build.py.
"""
import os

import numpy as np
from PIL import Image
from scipy import ndimage
from skimage.segmentation import watershed

from build import find_uploaded_watercolour

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets", "flowers-tight.png")

# flower centres in the 2048 px source, used as seeds to split the clusters
SEEDS = {"iris": (474, 512), "pink": (1613, 550), "yellow": (525, 1536), "cream": (1510, 1562)}
# how far each cluster slides towards the centre (px, in source pixels)
OFFSETS = {"iris": (215, 175), "pink": (-185, 175), "yellow": (215, -150), "cream": (-175, -150)}
ORDER = ["cream", "yellow", "pink", "iris"]  # bottom -> top


def centre_peony_mask(rgba):
    """The crimson peony in the middle (its petals only; corner buds are excluded)."""
    r, g, b, a = [rgba[..., i].astype(float) for i in range(4)]
    mx = np.maximum(np.maximum(r, g), b)
    mn = np.minimum(np.minimum(r, g), b)
    sat = (mx - mn) / (mx + 1e-6)
    h, w = a.shape
    yy, xx = np.mgrid[0:h, 0:w]
    central = (xx > w * 0.28) & (xx < w * 0.72) & (yy > h * 0.28) & (yy < h * 0.72)
    m = (a > 8) & central & (r > g * 1.8) & (r > b * 1.25) & (sat > 0.45) & (r < 235)
    m = ndimage.binary_fill_holes(ndimage.binary_closing(m, iterations=6))
    lab, n = ndimage.label(m)
    biggest = 1 + int(np.argmax(ndimage.sum(m, lab, range(1, n + 1))))
    return ndimage.binary_dilation(lab == biggest, iterations=4)


def main():
    src = find_uploaded_watercolour()
    rgba = np.array(Image.open(src).convert("RGBA"))
    rgba[centre_peony_mask(rgba), 3] = 0

    ink = rgba[..., 3] > 8
    markers = np.zeros(ink.shape, int)
    yy, xx = np.mgrid[0:ink.shape[0], 0:ink.shape[1]]
    for i, (cx, cy) in enumerate(SEEDS.values(), start=1):
        markers[((xx - cx) ** 2 + (yy - cy) ** 2 < 40 ** 2) & ink] = i
    # split along the narrowest necks; pieces not connected to a seed (the
    # centre peony's own leaves) get label 0 and are dropped
    labels = watershed(-ndimage.distance_transform_edt(ink), markers, mask=ink)

    pad = 200
    h, w = ink.shape
    canvas = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    names = list(SEEDS)
    for name in ORDER:
        layer = rgba.copy()
        layer[labels != names.index(name) + 1, 3] = 0
        dx, dy = OFFSETS[name]
        canvas.alpha_composite(Image.fromarray(layer), (pad + dx, pad + dy))

    bbox = canvas.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    canvas = canvas.crop(bbox)
    side = max(canvas.size)
    square = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    square.alpha_composite(canvas, ((side - canvas.width) // 2, (side - canvas.height) // 2))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    square.save(OUT, optimize=True)
    print("wrote", OUT, square.size, "from", os.path.basename(src))


if __name__ == "__main__":
    main()
