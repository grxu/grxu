"""QA for a rendered mock: downsample 2x to 1x, check the 65px safe margin, sample ground and accent ink.
usage: qa_mock.py <basename> [--accent F76336]
       qa_mock.py --sheet <out.png> <img1.png> <img2.png> ...   (squint test, 520px tiles)
"""
import sys
from PIL import Image
import numpy as np

if sys.argv[1] == "--sheet":
    out, files = sys.argv[2], sys.argv[3:]
    tiles = [Image.open(f).convert("RGB") for f in files]
    tiles = [t.resize((520, round(520 * t.height / t.width)), Image.LANCZOS) for t in tiles]
    h = max(t.height for t in tiles)
    sheet = Image.new("RGB", (10 + 530 * len(tiles), h + 20), "#222")
    for i, t in enumerate(tiles):
        sheet.paste(t, (10 + i * 530, 10))
    sheet.save(out); print("sheet:", out); sys.exit()

base = sys.argv[1]
accent = sys.argv[sys.argv.index("--accent") + 1] if "--accent" in sys.argv else "F76336"
im = Image.open(f"{base}@2x.png").convert("RGB")
im.resize((im.width // 2, im.height // 2), Image.LANCZOS).save(f"{base}.png")
a = np.asarray(Image.open(f"{base}.png").convert("RGB")).astype(int)
H, W, _ = a.shape
band = np.concatenate([a[:, :65].reshape(-1, 3), a[:, W-65:].reshape(-1, 3),
                       a[:65, :].reshape(-1, 3), a[H-65:, :].reshape(-1, 3)])
ink = ((band[:, 0] > 200) & (band[:, 1] > 200) & (band[:, 2] > 200)).sum()
hexs = lambda p: "#%02X%02X%02X" % tuple(p)
print("1x:", W, "x", H)
print("light ink inside the 65px safe margin:", ink, "(must be 0)")
print("ground samples:", hexs(a[int(H*.42), 150]), hexs(a[H-120, W-120]), hexs(a[100, W-100]), "(target #400685)")
t = np.array([int(accent[i:i+2], 16) for i in (0, 2, 4)])
px = a.reshape(-1, 3)
near = px[np.abs(px - t).sum(1) < 60]
if len(near):
    vals, counts = np.unique(near, axis=0, return_counts=True)
    print(f"accent ink mode: {hexs(vals[counts.argmax()])} (target #{accent.upper()}), {len(near)} px")
else:
    print(f"accent #{accent.upper()}: not found")
