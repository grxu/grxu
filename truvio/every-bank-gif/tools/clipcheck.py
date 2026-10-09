"""Contact sheet + drift check for a generated clip.

usage: python3 -I clipcheck.py <clip.mp4> <out_dir> <crop x0,y0,x1,y1> <still-region x0,y0,x1,y1>
Writes <out_dir>/frames/*.png, <out_dir>/sheet.png (every 2nd frame, i.e. 12 fps)
and prints the mean abs drift of the still region against frame 0.
"""
import os
import subprocess
import sys

from PIL import Image, ImageChops, ImageDraw

clip, out = sys.argv[1], sys.argv[2]
crop = tuple(int(v) for v in sys.argv[3].split(','))
still = tuple(int(v) for v in sys.argv[4].split(','))

frames_dir = os.path.join(out, 'frames')
os.makedirs(frames_dir, exist_ok=True)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', clip, '-vsync', '0',
                os.path.join(frames_dir, '%03d.png')], check=True)
names = sorted(os.listdir(frames_dir))

first = Image.open(os.path.join(frames_dir, names[0])).convert('L')
drift = []
for i, n in enumerate(names):
    im = Image.open(os.path.join(frames_dir, n)).convert('L')
    h = ImageChops.difference(first, im).crop(still).histogram()
    drift.append(sum(k * v for k, v in enumerate(h)) / sum(h))
print('frames:', len(names), '| still-region drift max %.1f, at frame %d' % (max(drift), drift.index(max(drift))))
print('drift every 6th:', [round(d, 1) for d in drift[::6]])

picks = names[::2]
tw, th, cols = 210, int(210 * (crop[3] - crop[1]) / (crop[2] - crop[0])) + 4, 7
rows = (len(picks) + cols - 1) // cols
sheet = Image.new('RGB', (cols * tw, rows * th), '#111')
dr = ImageDraw.Draw(sheet)
for i, n in enumerate(picks):
    im = Image.open(os.path.join(frames_dir, n)).convert('RGB').crop(crop).resize((tw - 4, th - 4))
    sheet.paste(im, ((i % cols) * tw + 2, (i // cols) * th + 2))
    dr.text(((i % cols) * tw + 6, (i // cols) * th + 4), str(i * 2), fill='white')
sheet.save(os.path.join(out, 'sheet.png'))
