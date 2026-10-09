"""Slide-clip check: contact sheet of the whole frame plus how much white building is left in the last frames."""
import os, subprocess, sys
import numpy as np, cv2
clip, out = sys.argv[1], sys.argv[2]
fd = os.path.join(out, 'frames'); os.makedirs(fd, exist_ok=True)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', clip, '-vsync', '0', os.path.join(fd, '%03d.png')], check=True)
names = sorted(os.listdir(fd))
white = []
for n in names:
    L = cv2.imread(os.path.join(fd, n)).mean(2)
    white.append(int((L > 185).sum()))
gone = next((i for i, w in enumerate(white) if w < 200 and all(x < 200 for x in white[i:])), None)
print('frames', len(names), '| white px f0', white[0], '| building fully gone from frame', gone, '| last frame white px', white[-1])
picks = names[::3]
tw, cols = 160, 9
rows = (len(picks) + cols - 1) // cols
sheet = np.full((rows * tw, cols * tw, 3), 17, np.uint8)
for i, n in enumerate(picks):
    im = cv2.resize(cv2.imread(os.path.join(fd, n)), (tw - 4, tw - 4), interpolation=cv2.INTER_AREA)
    cv2.putText(im, str(i * 3), (4, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
    r, c = divmod(i, cols); sheet[r * tw + 2:r * tw + tw - 2, c * tw + 2:c * tw + tw - 2] = im
cv2.imwrite(os.path.join(out, 'sheet.png'), sheet)
