"""Build the keyframe data for the variants thread animation.

usage: python3 build_data.py            writes vt-data.js and callout-gradient.png next to this file

vt-data.js holds `var VT = {...};`. The HTML animatic loads it with a script tag, and the
After Effects build script loads it with $.evalFile, so both play exactly the same keys.
The seed is fixed, so every run gives the same tile positions.

Key format, UI tracks:  [time_s, value, ease]
Key format, tiles:      [time_s, x, y, rotation_deg, scale_pct, opacity_pct, ease]
Ease names the segment that arrives at the key:
  L  linear   O  ease out (decelerate into the key)   I  ease in (accelerate into the key)
  IO ease in and out   H  hold (jump to the value at the key time)
The first key of a track ignores its ease.
"""
import json, math, random
from pathlib import Path

HERE = Path(__file__).resolve().parent
rng = random.Random(4062026)
r3 = lambda v: round(v, 3)

# ---------- palette and tile system ----------
COLOURS = [  # 8 colour variants, all on-palette and visible on Deep Violet
    ("White", "#FFFFFF"), ("Silver", "#CFD2D4"), ("Celestial Blue", "#008FC4"), ("Electric Green", "#2DB34A"),
    ("Yellow Gold", "#FFB310"), ("Prometheus Red", "#F76336"), ("Twilight", "#9C9DEC"), ("Celestial Bloom", "#E19CEC"),
]
MATERIALS = ["solid", "outline", "split"]  # 3 material variants, drawn as surface treatments, no texture files
SIZES = [16 + 2 * i for i in range(12)]    # 12 size variants, 16 to 38px squares

ORIGIN = (532.25, 368.7)                   # centre of "12 sizes, 8 colors, 3 materials" in the post body
COL_X = [110 + i * 860 / 11 for i in range(12)]
ROW_Y = [590 + k * 56 for k in range(8)]
GRID_TILE = 11.0                           # ordered grid inside the callout box: 8 colour rows x 36 columns


def grid_xy(i, k, m):
    col = i * 3 + m
    return 122 + col * 22 + i * 6, 846.78 + k * 15, col


def bound(s):  # half the diagonal of a rotated square, so a tile never crosses the 65px safe margin
    return 0.71 * s


tiles = []
for i, s in enumerate(SIZES):
    for k in range(8):
        for m in range(3):
            tiles.append({"name": f"Tile_s{i + 1:02d}_c{k + 1}_m{m + 1}", "i": i, "k": k, "m": m, "s": s,
                          "colour": COLOURS[k][1], "material": MATERIALS[m], "keys": []})

# ---------- stages 1 to 3: multiply 12 -> 96 -> 288, then scatter ----------
for t in tiles:
    i, k, m, s = t["i"], t["k"], t["m"], t["s"]
    K = t["keys"]
    if k == 0 and m == 0:                                  # stage 1: 12 size chips out of the numbers line
        t0 = 1.50 + 0.025 * i
        K += [[t0, *ORIGIN, 0, 0, 100, "L"], [t0 + 0.30, COL_X[i], ROW_Y[0], 0, 100, 100, "O"]]
        pos = (COL_X[i], ROW_Y[0])
    if m == 0 and k > 0:                                   # stage 2: each size spawns 8 colours down its column
        t0 = 2.00 + 0.05 * k + 0.01 * i
        K += [[t0, COL_X[i], ROW_Y[0], 0, 0, 100, "L"], [t0 + 0.25, COL_X[i], ROW_Y[k], 0, 100, 100, "O"]]
    if m > 0:                                              # stage 3: each colour spawns 3 materials
        t0 = 2.60 + rng.random() * 0.12
        dx, dy = (-22, 10) if m == 1 else (22, -10)
        K += [[t0, COL_X[i], ROW_Y[k], 0, 0, 100, "L"], [t0 + 0.18, COL_X[i] + dx, ROW_Y[k] + dy, 0, 100, 100, "O"]]
    last = K[-1]
    ts = max(last[0] + 0.02, 2.85 + rng.random() * 0.10)  # scatter: the matrix breaks apart
    b = bound(s)
    sx, sy = rng.uniform(65 + b, 1015 - b), rng.uniform(545, 1015 - b)
    rs = rng.uniform(-150, 150)
    K += [[ts, last[1], last[2], 0, 100, 100, "L"], [ts + 0.30, sx, sy, rs, 100, 100, "O"]]
    t["fall_at"] = max(ts + 0.32, 3.20 + rng.random() * 0.22)

# ---------- stage 4: everything falls into a heap on the floor (y 1015) ----------
BIN_W, X0, X1 = 15, 65, 1015
bins = [0.0] * int((X1 - X0) / BIN_W)
for t in sorted(tiles, key=lambda t: t["fall_at"]):
    s, b = t["s"], bound(t["s"])
    best = None
    for attempt in range(60):
        x = rng.triangular(65 + b, 1015 - b, 540) if rng.random() < 0.5 else rng.uniform(65 + b, 1015 - b)
        lo, hi = int((x - s / 2 - X0) / BIN_W), int((x + s / 2 - X0) / BIN_W)
        lo, hi = max(lo, 0), min(hi, len(bins) - 1)
        h = max(bins[lo:hi + 1])
        cy = 1015 - h - 0.6 * s
        cy = min(cy, 1015 - b)
        if cy - b >= 815:                                  # the heap stays clear of the answer panel and card
            best = (x, cy, lo, hi)
            break
    if best is None or best[1] - b < 815:                 # no random spot fits: take the lowest spot on the floor
        best = None
        for xi in range(int(65 + b) + 1, int(1015 - b), 3):
            lo, hi = max(int((xi - s / 2 - X0) / BIN_W), 0), min(int((xi + s / 2 - X0) / BIN_W), len(bins) - 1)
            cy = min(1015 - max(bins[lo:hi + 1]) - 0.6 * s, 1015 - b)
            if best is None or cy > best[1]:
                best = (xi, cy, lo, hi)
    x, cy, lo, hi = best
    for j in range(lo, hi + 1):
        bins[j] = max(bins[j], 1015 - cy - 0.6 * s) + 0.2 * s  # tiles in a pile overlap heavily
    t["heap"] = (x, cy, rng.uniform(-40, 40))
    t1 = t["fall_at"]
    K = t["keys"]
    sx, sy, rs = K[-1][1], K[-1][2], K[-1][3]
    K += [[t1, sx, sy, rs, 100, 100, "L"],
          [t1 + 0.42, x, cy, t["heap"][2], 100, 100, "I"],
          [t1 + 0.50, x, cy - 7, t["heap"][2], 100, 100, "O"],
          [t1 + 0.58, x, cy, t["heap"][2], 100, 100, "I"]]

# ---------- stage 5: Truvio PIM sorts the heap into an ordered grid in the callout zone ----------
for t in tiles:
    gx, gy, col = grid_xy(t["i"], t["k"], t["m"])
    hx, hy, hr = t["heap"]
    t2 = 6.62 + col / 35 * 0.35 + t["k"] * 0.02
    sc = GRID_TILE / t["s"] * 100
    t["keys"] += [[t2, hx, hy, hr, 100, 100, "L"], [t2 + 0.55, gx, gy, 0, sc, 100, "IO"]]
    # stage 6: the grid syncs into the callout outline, left to right
    t3 = 8.70 + col / 35 * 0.45
    ey = 834.28 if t["k"] < 4 else 964.28
    t["keys"] += [[t3, gx, gy, 0, sc, 100, "L"], [t3 + 0.30, gx, ey, 0, sc * 0.25, 0, "I"]]
    t["keys"] = [[r3(k[0]), r3(k[1]), r3(k[2]), r3(k[3]), r3(k[4]), r3(k[5]), k[6]] for k in t["keys"]]
    for a, b in zip(t["keys"], t["keys"][1:]):
        assert b[0] > a[0], (t["name"], a, b)
    for key in t["keys"]:
        e = (bound(t["s"]) if abs(key[3]) > 1 else t["s"] / 2) * key[4] / 100
        assert key[4] == 0 or (65 <= key[1] - e and key[1] + e <= 1015 and key[2] + e <= 1015.5), (t["name"], key)

# ---------- UI tracks (layer.property) ----------
CARD_TOP, CARD_H0, CARD_H1 = 114.72, 419.08, 682.56
tracks = {
    "Body_line1.opacity": [[0.25, 0, "L"], [0.60, 100, "O"]],
    "Body_line1.dy": [[0.25, 10, "L"], [0.60, 0, "O"]],
    "Body_line2.opacity": [[0.40, 0, "L"], [0.75, 100, "O"]],
    "Body_line2.dy": [[0.40, 10, "L"], [0.75, 0, "O"]],
    "Underline.trim": [[1.10, 0, "L"], [1.45, 100, "O"]],
    "Underline.opacity": [[3.80, 100, "L"], [4.10, 0, "L"]],
    "Card_null.dx": [[3.42, 0, "L"], [3.45, 4, "L"], [3.48, -4, "L"], [3.52, 2, "L"], [3.56, 0, "L"]],
    "Card_bg.height": [[3.80, CARD_H0, "L"], [4.25, CARD_H1, "O"]],
    "Answer_bg.height": [[3.85, 0, "L"], [4.25, 237.53, "O"]],
    "Answer_bg.opacity": [[3.85, 0, "L"], [3.95, 100, "L"]],
    "Answer_avatar.scale": [[4.10, 0, "L"], [4.24, 110, "O"], [4.32, 100, "IO"]],
    "Answer_user.opacity": [[4.15, 0, "L"], [4.35, 100, "O"]],
    "Answer_user.dx": [[4.15, -12, "L"], [4.35, 0, "O"]],
    "Answer_pills.opacity": [[4.15, 0, "L"], [4.35, 100, "O"]],
    "Answer_l1.type": [[5.10, 0, "L"], [5.62, 100, "L"]],
    "Answer_bold.type": [[5.62, 0, "L"], [5.80, 100, "L"]],
    "Answer_period.type": [[5.80, 0, "L"], [5.83, 100, "H"]],
    "Answer_l2.type": [[5.90, 0, "L"], [6.58, 100, "L"]],
    "Cursor.position": [[7.62, [390, 800], "L"], [8.10, [161, 722], "O"], [8.45, [161, 722], "L"], [8.85, [330, 805], "I"]],
    "Cursor.opacity": [[7.62, 0, "L"], [7.75, 100, "L"], [8.62, 100, "L"], [8.85, 0, "L"]],
    "Cursor.scale": [[8.10, 100, "L"], [8.15, 85, "L"], [8.22, 100, "O"]],
    "Upvote_outline.opacity": [[4.15, 0, "L"], [4.35, 100, "O"], [8.13, 0, "H"]],
    "Upvote_fill.opacity": [[0, 0, "L"], [8.13, 100, "H"]],
    "Upvote_null.scale": [[8.13, 100, "L"], [8.22, 135, "O"], [8.35, 95, "IO"], [8.42, 100, "IO"]],
    "Burst.scale": [[8.15, 60, "L"], [8.45, 130, "O"]],
    "Burst.opacity": [[8.14, 0, "L"], [8.15, 100, "H"], [8.30, 100, "L"], [8.45, 0, "L"]],
    "Tag.scale": [[8.28, 0, "L"], [8.42, 108, "O"], [8.50, 100, "IO"]],
    "Tag.opacity": [[8.28, 0, "L"], [8.33, 100, "L"]],
    "Callout_outline.trim": [[8.95, 0, "L"], [9.50, 100, "L"]],
    "Lockup.opacity": [[9.30, 0, "L"], [9.70, 100, "O"]],
    "Lockup.dx": [[9.30, -12, "L"], [9.70, 0, "O"]],
    "CTA.opacity": [[9.45, 0, "L"], [9.90, 100, "O"]],
    "CTA.dx": [[9.45, 16, "L"], [9.90, 0, "O"]],
    "CTA_arrow.dx": [[10.40, 0, "L"], [10.55, 7, "O"], [10.80, 0, "IO"], [12.40, 0, "L"], [12.55, 7, "O"], [12.80, 0, "IO"]],
}
for d in range(3):  # typing dots: two pulses each, staggered 0.10s
    p1, p2 = 4.42 + 0.10 * d, 4.72 + 0.10 * d
    tracks[f"Dot{d + 1}.opacity"] = [[4.35, 0, "L"], [4.40, 30, "L"], [p1, 100, "IO"], [p1 + 0.14, 30, "IO"],
                                    [p2, 100, "IO"], [p2 + 0.14, 30, "IO"], [5.10, 0, "L"]]

# ---------- icon and outline geometry as AE shapes ----------
import re


def svg_to_ae(d):
    """Convert an SVG path (M L H V C S A Z, any case) into AE shapes: vertices, in and out tangents (relative), closed."""
    toks = re.findall(r"[MLHVCSAZmlhvcsaz]|-?\d*\.?\d+(?:e-?\d+)?", d)
    shapes, cur, pos, start, cmd, last_c2 = [], None, [0.0, 0.0], [0.0, 0.0], None, None
    num = lambda: float(toks.pop(0))

    def new(pt):
        nonlocal cur
        cur = {"v": [list(pt)], "i": [[0, 0]], "o": [[0, 0]], "closed": False}
        shapes.append(cur)

    def line(pt):
        cur["v"].append(list(pt)); cur["i"].append([0, 0]); cur["o"].append([0, 0])

    def curve(c1, c2, pt):
        v0 = cur["v"][-1]
        cur["o"][-1] = [c1[0] - v0[0], c1[1] - v0[1]]
        cur["v"].append(list(pt)); cur["i"].append([c2[0] - pt[0], c2[1] - pt[1]]); cur["o"].append([0, 0])

    def arc(rx, ry, phi, fa, fs, x2, y2):  # endpoint arc to cubic segments (rx == ry, phi == 0 in these paths)
        x1, y1 = pos
        dx, dy = (x1 - x2) / 2, (y1 - y2) / 2
        r = rx
        lam = (dx * dx + dy * dy) / (r * r)
        if lam > 1: r *= math.sqrt(lam)
        sq = max(0.0, (r * r * r * r - r * r * dy * dy - r * r * dx * dx) / (r * r * dy * dy + r * r * dx * dx))
        coef = (-1 if fa == fs else 1) * math.sqrt(sq)
        cxp, cyp = coef * dy, -coef * dx
        cx, cy = cxp + (x1 + x2) / 2, cyp + (y1 + y2) / 2
        a1 = math.atan2((y1 - cy) / r, (x1 - cx) / r)
        a2 = math.atan2((y2 - cy) / r, (x2 - cx) / r)
        da = a2 - a1
        if fs and da < 0: da += 2 * math.pi
        if not fs and da > 0: da -= 2 * math.pi
        n = max(1, int(math.ceil(abs(da) / (math.pi / 2) - 1e-9)))
        for k in range(n):
            t1, t2 = a1 + da * k / n, a1 + da * (k + 1) / n
            h = 4 / 3 * math.tan((t2 - t1) / 4) * r
            p1 = (cx + r * math.cos(t1), cy + r * math.sin(t1)); p2 = (cx + r * math.cos(t2), cy + r * math.sin(t2))
            c1 = (p1[0] - h * math.sin(t1), p1[1] + h * math.cos(t1)); c2 = (p2[0] + h * math.sin(t2), p2[1] - h * math.cos(t2))
            curve(c1, c2, p2)

    while toks:
        if re.match(r"[A-Za-z]", toks[0]): cmd = toks.pop(0)
        rel = cmd.islower(); C = cmd.upper()
        ox, oy = (pos if rel else (0, 0))
        if C == "M":
            pos = [ox + num(), oy + num()]; start = list(pos); new(pos); cmd = "l" if rel else "L"; last_c2 = None
        elif C == "L": pos = [ox + num(), oy + num()]; line(pos); last_c2 = None
        elif C == "H": pos = [(pos[0] if rel else 0) + num(), pos[1]]; line(pos); last_c2 = None
        elif C == "V": pos = [pos[0], (pos[1] if rel else 0) + num()]; line(pos); last_c2 = None
        elif C == "C":
            c1 = (ox + num(), oy + num()); c2 = (ox + num(), oy + num()); pt = (ox + num(), oy + num())
            curve(c1, c2, pt); pos = list(pt); last_c2 = c2
        elif C == "S":
            c1 = (2 * pos[0] - last_c2[0], 2 * pos[1] - last_c2[1]) if last_c2 else tuple(pos)
            c2 = (ox + num(), oy + num()); pt = (ox + num(), oy + num())
            curve(c1, c2, pt); pos = list(pt); last_c2 = c2
        elif C == "A":
            rx, ry, phi, fa, fs = num(), num(), num(), int(num()), int(num()); x2, y2 = ox + num(), oy + num()
            arc(rx, ry, phi, fa, fs, x2, y2); pos = [x2, y2]; last_c2 = None
        elif C == "Z":
            if cur["v"][-1] == cur["v"][0] or (abs(cur["v"][-1][0] - start[0]) < 1e-6 and abs(cur["v"][-1][1] - start[1]) < 1e-6):
                if len(cur["v"]) > 1:  # fold the closing vertex into the first
                    cur["i"][0] = cur["i"][-1]; cur["v"].pop(); cur["i"].pop(); cur["o"].pop()
            cur["closed"] = True; pos = list(start); last_c2 = None
    for sh in shapes:
        for key in ("v", "i", "o"): sh[key] = [[round(x, 3), round(y, 3)] for x, y in sh[key]]
    return shapes


ICONS = {  # all in a 24x24 box with the origin at the top-left, except where noted
    "arrow_up": "M12 3.2 20.6 12.6H15.4V20.8H8.6V12.6H3.4Z",
    "arrow_down": "M12 20.8 3.4 11.4H8.6V3.2H15.4V11.4H20.6Z",
    "bubble": "M4.5 5.5h15a1.8 1.8 0 0 1 1.8 1.8v8.4a1.8 1.8 0 0 1-1.8 1.8H11l-4.6 3.6v-3.6H4.5a1.8 1.8 0 0 1-1.8-1.8V7.3a1.8 1.8 0 0 1 1.8-1.8Z",
    "share": "M13.5 4.5 20.5 11l-7 6.5v-3.9C8.6 13.6 5.6 15.3 3.5 19c.6-5.6 3.9-9.4 10-10.4Z",
    "person_body": "M4.6 20.4c.9-4 3.8-6.2 7.4-6.2s6.5 2.2 7.4 6.2Z",   # plus a circle r 4.2 at (12, 9)
    "cta_arrow": "M1.5 8h19M14 2l6.5 6-6.5 6",                        # 24x16 box, drawn at 26x18
    "cursor": "M0 0V23L5.6 17.6 9.6 26.4 13.4 24.8 9.5 16.2H16.8Z",   # tip at the origin, drawn at 120 percent
    "outline_top": "M66 899.28V851.28A17 17 0 0 1 83 834.28H997A17 17 0 0 1 1014 851.28V899.28",      # comp coords
    "outline_bottom": "M66 899.28V947.28A17 17 0 0 0 83 964.28H997A17 17 0 0 0 1014 947.28V899.28",  # comp coords
}
ICON_SHAPES = {k: svg_to_ae(v) for k, v in ICONS.items()}

VT = {
    "comp": {"name": "Variants_thread_1x1", "width": 1080, "height": 1080, "fps": 30, "duration": 14.0,
             "background": "#400685"},
    "colours": [{"name": n, "hex": h} for n, h in COLOURS],
    "materials": MATERIALS, "sizes": SIZES,
    "tile_style": {"corner_radius_pct": 18, "outline_width_pct": 12, "split_overlay": "#400685", "split_opacity": 35},
    "tracks": tracks,
    "icons": {"svg": ICONS, "ae": ICON_SHAPES},
    "tiles": [{"name": t["name"], "size": t["s"], "colour": t["colour"], "material": t["material"], "keys": t["keys"]}
              for t in tiles],
}
out = HERE / "vt-data.js"
out.write_text("// Generated by build_data.py. Do not edit by hand.\nvar VT = " + json.dumps(VT, separators=(",", ":")) + ";\n")
print("wrote", out, f"{out.stat().st_size / 1024:.0f} KB,", len(tiles), "tiles,", sum(len(t["keys"]) for t in tiles), "tile keys")
print("heap top y:", round(min(t["heap"][1] - bound(t["s"]) for t in tiles), 1), "(must be >= 815)")

# ---------- callout gradient plate: CSS 64.6deg (brand 25.4deg) over the callout box ----------
from PIL import Image
import numpy as np
x1, y1, x2, y2 = 126.82, 1095.47, 953.18, 703.09
stops = [(0, (0x33, 0xB4, 0xE8)), (0.55, (0x2D, 0xB3, 0x4A)), (1, (0xFF, 0xB3, 0x10))]
yy, xx = np.mgrid[0:1080, 0:1080].astype(float) + 0.5
dx, dy = x2 - x1, y2 - y1
p = np.clip(((xx - x1) * dx + (yy - y1) * dy) / (dx * dx + dy * dy), 0, 1)
img = np.zeros((1080, 1080, 3))
for (a, ca), (b, cb) in zip(stops, stops[1:]):
    m = (p >= a) & (p <= b)
    f = ((p - a) / (b - a))[m][:, None]
    img[m] = np.array(ca) * (1 - f) + np.array(cb) * f
Image.fromarray(np.uint8(np.round(img))).save(HERE / "callout-gradient.png")
print("wrote", HERE / "callout-gradient.png")
