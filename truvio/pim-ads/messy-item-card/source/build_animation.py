"""Row 52 Clean-up animation, built from Grady's Illustrator file.

usage: python3 source/build_animation.py            (run from the ad folder)

1. Converts source/Truvio-PIM-for-BC-Row-52.ai to SVG and cuts it into layers by paint order.
2. Renders each layer as a full-frame transparent PNG at 2x (2160x2160) into animation/assets/.
3. Renders the preview from those same PNGs and one timeline: a looping MP4 and a GIF.
4. Writes animation/build_row52_cleanup.jsx, which builds the same comp in After Effects.

The timeline below is the single source of truth for the preview and the AE script.
"""
import glob, json, math, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path
import numpy as np
from PIL import Image

AD = Path(__file__).resolve().parent.parent
AI = AD / "source" / "Truvio-PIM-for-BC-Row-52.ai"
OUT = AD / "animation"
ASSETS = OUT / "assets"
W = H = 1080
FPS, DUR, LOOP_TAIL = 30, 6.0, 0.5

CHROME = os.environ.get("CHROME") or next(
    (c for c in ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                 *sorted(glob.glob("/opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell"))]
     if os.access(c, os.X_OK)), None)

# ---------- 1. Layers, by the paint-order index of each top-level SVG element ----------
R = lambda a, b: list(range(a, b + 1))
RED_L = {1: R(110, 117), 2: R(130, 136), 3: R(149, 153)}
RED_ALL = sum(RED_L.values(), [])
# The Today card copied onto the right tile: the start state of the Truvio PIM side.
S = 448 / 446.2
TO_RIGHT = (S, 561.9 - 72.1 * S, 440.5 - 441.7 * S)

LAYERS = [  # bottom to top. name, element indexes, optional transform (s, tx, ty)
    ("BG", [1], None),
    ("Logo", R(386, 393), None),
    ("Headline", R(365, 376), None),
    ("Label_BC", [395], None),
    ("Label_PIM", [394], None),
    ("CTA", R(377, 385), None),
    ("Tile_Today", [i for i in R(2, 155) if i not in RED_ALL], None),
    ("Red_L1", RED_L[1], None),
    ("Red_L2", RED_L[2], None),
    ("Red_L3", RED_L[3], None),
    ("Tile_PIM_clean", R(156, 258), None),
    ("Tile_PIM_clutter", [i for i in R(3, 155) if i not in RED_ALL], TO_RIGHT),
    ("Red_R3", RED_L[3], TO_RIGHT),
    ("PIM_popup", R(259, 309), None),
    ("Row1", R(310, 320), None),
    ("Row2", R(321, 331), None),
    ("Row3", R(332, 342), None),
    ("Row4", R(343, 353), None),
    ("Row5", R(354, 364), None),
    ("Red_R1", RED_L[1], TO_RIGHT),
    ("Red_R2", RED_L[2], TO_RIGHT),
]

def moved(rect, t):  # x, y, w, h through a TO_RIGHT style transform
    s, tx, ty = t
    return (rect[0] * s + tx, rect[1] * s + ty, rect[2] * s, rect[3] * s)

FIELD = {1: (83.7, 647.3, 413.2, 58.2), 2: (83.7, 765.7, 413.2, 47.5), 3: (83.7, 873.3, 413.2, 58.2)}
ROW = {k: (735.7, 615.3 + 56.47 * (k - 1), 256.1, 47.7) for k in range(1, 6)}
POPUP = (717.2, 430.3, 293.1, 480.1)
center = lambda r: (r[0] + r[2] / 2, r[1] + r[3] / 2)
ANCHOR = {"PIM_popup": center(POPUP),
          **{f"Red_L{k}": center(FIELD[k]) for k in (1, 2, 3)},
          **{f"Red_R{k}": center(moved(FIELD[k], TO_RIGHT)) for k in (1, 2, 3)},
          **{f"Row{k}": center(ROW[k]) for k in range(1, 6)}}

# ---------- 2. Timeline. Keys: (time, value). o = opacity %, p = offset [dx, dy] px, s = scale [sx, sy] % ----------
def pulse(t0):
    return [(t0, [100, 100]), (t0 + 0.25, [104, 104]), (t0 + 0.55, [100, 100])]

def fly(k, t0, dur=0.75):
    f, r = moved(FIELD[k], TO_RIGHT), ROW[k]
    (fx, fy), (rx, ry) = center(f), center(r)
    end = [round(r[2] / f[2] * 100, 2), round(r[3] / f[3] * 100, 2)]
    return {
        "s": pulse(0.6 + 0.08 * (k - 1)) + [(1.32, [100, 100]), (1.55, [103, 103]), (t0, [103, 103]), (t0 + dur, end)],
        "p": [(t0, [0, 0]), (t0 + dur, [round(rx - fx, 2), round(ry - fy, 2)])],
        "o": [(t0 + dur - 0.2, 100), (t0 + dur, 0)],
    }

def appear(t0, dur=0.3, dy=0):
    k = {"o": [(t0, 0), (t0 + dur, 100)]}
    if dy:
        k["p"] = [(t0, [0, dy]), (t0 + dur, [0, 0])]
    else:
        k["s"] = [(t0, [96, 96]), (t0 + dur, [100, 100])]
    return k

TIMELINE = {
    "Red_L1": {"s": pulse(0.6)}, "Red_L2": {"s": pulse(0.68)}, "Red_L3": {"s": pulse(0.76)},
    "Red_R3": {"s": pulse(0.76), "o": [(2.4, 100), (3.0, 0)]},
    "Tile_PIM_clutter": {"o": [(2.4, 100), (3.0, 0)]},
    "PIM_popup": {"o": [(1.15, 0), (1.45, 100)],
                  "s": [(1.15, [88, 88]), (1.5, [102, 102]), (1.7, [100, 100])],
                  "p": [(1.15, [0, 20]), (1.5, [0, 0])]},
    "Red_R1": fly(1, 1.75), "Red_R2": fly(2, 1.95),
    "Row1": appear(2.3, 0.25), "Row2": appear(2.5, 0.25),
    "Row3": appear(2.75, dy=14), "Row4": appear(2.9, dy=14), "Row5": appear(3.05, dy=14),
}

# Round key times to the millisecond and check every property runs forward in time.
for _n, _k in TIMELINE.items():
    for _p, _keys in _k.items():
        _k[_p] = [(round(t, 3), v) for t, v in _keys]
        assert all(a[0] < b[0] for a, b in zip(_k[_p], _k[_p][1:])), f"{_n}.{_p} keys out of order"

def ease(u):  # cubic-bezier(0.6, 0, 0.4, 1): matches AE keyframe ease, 60 percent influence both sides
    lo, hi = 0.0, 1.0
    for _ in range(40):
        m = (lo + hi) / 2
        x = 3 * (1 - m) ** 2 * m * 0.6 + 3 * (1 - m) * m * m * 0.4 + m ** 3
        lo, hi = (m, hi) if x < u else (lo, m)
    m = (lo + hi) / 2
    return 3 * (1 - m) * m * m + m ** 3

def value(keys, t, default):
    if not keys:
        return default
    if t <= keys[0][0]:
        return keys[0][1]
    for (t0, v0), (t1, v1) in zip(keys, keys[1:]):
        if t <= t1:
            e = ease((t - t0) / (t1 - t0)) if t1 > t0 else 1
            return [a + (b - a) * e for a, b in zip(v0, v1)] if isinstance(v0, list) else v0 + (v1 - v0) * e
    return keys[-1][1]

def state(name, t):
    k = TIMELINE.get(name, {})
    first_o = k.get("o", [(0, 100)])[0][1]
    return (value(k.get("o"), t, first_o), value(k.get("p"), t, [0, 0]), value(k.get("s"), t, [100, 100]))

# ---------- 3. Render the layers ----------
def render_layers():
    ASSETS.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        subprocess.run(["pdftocairo", "-svg", str(AI), str(d / "src.svg")], check=True)
        svg = (d / "src.svg").read_text()
        svg = svg.split("?>", 1)[1] if svg.lstrip().startswith("<?xml") else svg
        head = re.match(r"\s*(<svg[^>]*>)", svg).group(1)
        body = svg[svg.index(head) + len(head): svg.rindex("</svg>")]
        # Split the top level into elements, keeping defs. Depth-aware scan over tags.
        elems, depth, start = [], 0, None
        for m in re.finditer(r"<(/?)([a-zA-Z]+)[^>]*?(/?)>", body):
            closing, selfclose = m.group(1) == "/", m.group(3) == "/"
            if depth == 0 and not closing:
                start = m.start()
            if not closing and not selfclose:
                depth += 1
            elif closing:
                depth -= 1
            if depth == 0 and start is not None:
                elems.append(body[start:m.end()]); start = None
        defs, items = elems[0], elems[1:]
        assert defs.startswith("<defs"), "first element should be defs"
        print("top-level elements:", len(items))
        for name, idx, tf in LAYERS:
            content = "".join(items[i - 1] for i in idx)
            if tf:
                content = f'<g transform="matrix({tf[0]} 0 0 {tf[0]} {tf[1]:.3f} {tf[2]:.3f})">{content}</g>'
            page = (f"<!doctype html><html><head><style>html,body{{margin:0;background:transparent}}svg{{display:block}}</style></head>"
                    f"<body>{head}{defs}{content}</svg></body></html>")
            (d / "p.html").write_text(page)
            subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                            "--force-device-scale-factor=2", f"--window-size={W},{H}", "--virtual-time-budget=8000",
                            "--default-background-color=00000000", f"--screenshot={ASSETS / (name + '.png')}",
                            (d / "p.html").as_uri()], capture_output=True)
            print("layer", name, Image.open(ASSETS / f"{name}.png").size)

# ---------- 4. Preview ----------
def frames(loop=True):
    lay = {}
    for name, _, _ in LAYERS:
        im = Image.open(ASSETS / f"{name}.png").convert("RGBA").resize((W, H), Image.LANCZOS)
        lay[name] = im
    animated = set(TIMELINE)
    # Pre-composite the static stack up to the first animated layer that sits above it.
    order = [n for n, _, _ in LAYERS]
    base = Image.new("RGBA", (W, H))
    for n in order:
        if n in animated:
            continue
        base.alpha_composite(lay[n])
    n_main = int(round(DUR * FPS))
    out = []
    for f in range(n_main):
        t = f / FPS
        im = base.copy()
        for n in order:
            if n not in animated:
                continue
            o, (dx, dy), (sx, sy) = state(n, t)
            if o <= 0.5:
                continue
            src = lay[n]
            if (sx, sy) != (100, 100) or dx or dy:
                ax, ay = ANCHOR.get(n, (W / 2, H / 2))
                a, e = 100 / sx, 100 / sy
                src = src.transform((W, H), Image.AFFINE, (a, 0, ax - (ax + dx) * a, 0, e, ay - (ay + dy) * e), Image.BICUBIC)
            if o < 99.5:
                src = src.copy(); alpha = np.asarray(src.getchannel("A"), dtype=np.float32) * (o / 100)
                src.putalpha(Image.fromarray(alpha.astype(np.uint8)))
            im.alpha_composite(src)
        out.append(im.convert("RGB"))
    if loop:  # dissolve from the held end frame back to the first frame
        n_tail = int(round(LOOP_TAIL * FPS))
        for i in range(n_tail):
            u = ease(min(1, (i + 1) / (n_tail - 3)))
            out.append(Image.blend(out[n_main - 1], out[0], u))
    return out

def render_preview():
    with tempfile.TemporaryDirectory() as d:
        fr = frames(loop=True)
        for i, im in enumerate(fr):
            im.save(f"{d}/{i:04d}.png")
        mp4 = OUT / "row52-cleanup-loop-1080.mp4"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", f"{d}/%04d.png",
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", "-preset", "slow",
                        "-movflags", "+faststart", str(mp4)], check=True)
        gif = OUT / "row52-cleanup-preview-540.gif"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", f"{d}/%04d.png",
                        "-vf", "fps=15,scale=540:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=192[p];[b][p]paletteuse=dither=sierra2_4a",
                        "-loop", "0", str(gif)], check=True)
        # Contact sheet for review: every 0.25 s
        review = Path(tempfile.gettempdir()) / "row52-review"; review.mkdir(exist_ok=True)
        sheet = review / "sheet.png"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(mp4), "-vf", "fps=4,scale=270:-1,tile=7x4",
                        "-frames:v", "1", str(sheet)], check=True)
        fr[int(DUR * FPS) - 1].save(review / "end-frame.png")
        print("frames:", len(fr), "->", mp4.name, gif.name, "| review images (read them):", review)

# ---------- 5. After Effects script ----------
def write_jsx():
    layers = []
    for name, _, _ in LAYERS:
        ax, ay = ANCHOR.get(name, (W / 2, H / 2))
        layers.append({"name": name, "file": f"assets/{name}.png", "anchor": [round(ax, 2), round(ay, 2)],
                       "keys": {k: [[round(t, 3), v] for t, v in ks] for k, ks in TIMELINE.get(name, {}).items()}})
    data = json.dumps({"comp": "Row52_CleanUp", "w": W, "h": H, "fps": FPS, "dur": DUR, "layers": layers}, indent=1)
    jsx = """// Row 52 Clean-up: builds the After Effects comp from the layer PNGs in ./assets.
// Run in After Effects: File > Scripts > Run Script File, then pick this file.
// Every layer is a full-frame 2160x2160 PNG at 50 percent scale, so it sits exactly where it sits in the .ai.
// Anchor points sit on each moving part, so scale happens around the part. Keyframes use 60 percent ease.
(function () {
  var DATA = %DATA%;
  var root = new File($.fileName).parent;
  app.beginUndoGroup("Build Row52 Clean-up");
  var folder = app.project.items.addFolder("Row52 assets");
  var comp = app.project.items.addComp(DATA.comp, DATA.w, DATA.h, 1, DATA.dur, DATA.fps);
  comp.bgColor = [1, 1, 1];
  function ease(prop) {
    for (var k = 1; k <= prop.numKeys; k++) {
      var dims = 1;
      if (prop.propertyValueType == PropertyValueType.TwoD) dims = 2;
      if (prop.propertyValueType == PropertyValueType.ThreeD) dims = 3;
      if (prop.propertyValueType == PropertyValueType.TwoD_SPATIAL || prop.propertyValueType == PropertyValueType.ThreeD_SPATIAL) dims = 1;
      var e = [];
      for (var d = 0; d < dims; d++) e.push(new KeyframeEase(0, 60));
      prop.setTemporalEaseAtKey(k, e, e);
    }
  }
  for (var i = 0; i < DATA.layers.length; i++) {
    var L = DATA.layers[i];
    var item = app.project.importFile(new ImportOptions(new File(root.fsName + "/" + L.file)));
    item.parentFolder = folder;
    var layer = comp.layers.add(item);
    layer.name = L.name;
    var tr = layer.property("ADBE Transform Group");
    var ap = tr.property("ADBE Anchor Point"), pos = tr.property("ADBE Position");
    var sc = tr.property("ADBE Scale"), op = tr.property("ADBE Opacity");
    ap.setValue([L.anchor[0] * 2, L.anchor[1] * 2]);
    pos.setValue([L.anchor[0], L.anchor[1]]);
    sc.setValue([50, 50]);
    var keys = L.keys, j;
    if (keys.o) { for (j = 0; j < keys.o.length; j++) op.setValueAtTime(keys.o[j][0], keys.o[j][1]); ease(op); }
    if (keys.p) {
      for (j = 0; j < keys.p.length; j++) pos.setValueAtTime(keys.p[j][0], [L.anchor[0] + keys.p[j][1][0], L.anchor[1] + keys.p[j][1][1]]);
      ease(pos);
    }
    if (keys.s) {
      for (j = 0; j < keys.s.length; j++) sc.setValueAtTime(keys.s[j][0], [keys.s[j][1][0] / 2, keys.s[j][1][1] / 2]);
      ease(sc);
    }
  }
  comp.openInViewer();
  app.endUndoGroup();
})();
""".replace("%DATA%", data)
    (OUT / "build_row52_cleanup.jsx").write_text(jsx)
    print("wrote", OUT / "build_row52_cleanup.jsx")

if __name__ == "__main__":
    steps = sys.argv[1:] or ["layers", "preview", "jsx"]
    if "layers" in steps: render_layers()
    if "preview" in steps: render_preview()
    if "jsx" in steps: write_jsx()
