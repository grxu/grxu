"""Row 52 Clean-up animation, built from Grady's Illustrator file.

usage: python3 source/build_animation.py [layers] [preview] [jsx]     (run from the ad folder)

1. Converts source/Truvio-PIM-for-BC-Row-52.ai to SVG and cuts it into layers by paint order.
2. Renders each layer as a full-frame transparent PNG at 2x (2160x2160) into animation/assets/.
3. Renders the preview from those same PNGs and one timeline: a looping MP4 and a GIF.
4. Writes animation/build_row52_cleanup.jsx, which builds the same comp in After Effects.

The timeline below is the single source of truth for the preview and the AE script.
Layers in a mask group sit in an AE precomp with a rectangle mask, so they only show inside it.
"""
import glob, json, os, re, subprocess, sys, tempfile
from pathlib import Path
import numpy as np
from PIL import Image

AD = Path(__file__).resolve().parent.parent
AI = AD / "source" / "Truvio-PIM-for-BC-Row-52.ai"
OUT = AD / "animation"
ASSETS = OUT / "assets"
W = H = 1080
FPS, DUR, LOOP_TAIL = 30, 10.0, 0.6

CHROME = os.environ.get("CHROME") or next(
    (c for c in ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                 *sorted(glob.glob("/opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell"))]
     if os.access(c, os.X_OK)), None)

# ---------- 1. Layers, by the paint-order index of each top-level SVG element ----------
R = lambda a, b: list(range(a, b + 1))
RED_L = {1: R(110, 117), 2: R(130, 136), 3: R(149, 153)}
RED_ALL = sum(RED_L.values(), [])
S = 448 / 446.2  # the BC Card tile copied onto the right tile: the start state of the Truvio PIM side
TO_RIGHT = (S, 561.9 - 72.1 * S, 440.5 - 441.7 * S)

# Mask groups (x, y, w, h): the clean card body inside its tile, and the asset list inside the pop-up.
MASKS = {"CleanBody": (561.9, 481.4, 448, 407.1), "Assets": (717.2, 608.0, 293.1, 296.0)}

LAYERS = [  # bottom to top: name, element indexes, transform (s, tx, ty) or None, mask group or None
    ("BG", [1], None, None),
    ("Logo", R(386, 393), None, None),
    ("Headline", R(365, 376), None, None),
    ("Label_BC", [395], None, None),
    ("Label_PIM", [394], None, None),
    ("CTA", R(377, 385), None, None),
    ("Tile_Today", [i for i in R(2, 155) if i not in RED_ALL], None, None),
    ("Red_L1", RED_L[1], None, None),
    ("Red_L2", RED_L[2], None, None),
    ("Red_L3", RED_L[3], None, None),
    ("Tile_PIM_base", R(156, 197), None, None),
    ("Tile_PIM_clutter", [i for i in R(3, 155) if i not in RED_ALL], TO_RIGHT, None),
    ("Red_R3", RED_L[3], TO_RIGHT, None),
    ("Clean_body", [198], None, "CleanBody"),
    ("Clean_title", R(199, 208), None, "CleanBody"),
    ("Clean_tab", R(209, 213), None, "CleanBody"),
    ("Clean_no", R(214, 223), None, "CleanBody"),
    ("Clean_desc", R(224, 237), None, "CleanBody"),
    ("Clean_cat", R(238, 258), None, "CleanBody"),
    ("Red_R1", RED_L[1], TO_RIGHT, None),
    ("Red_R2", RED_L[2], TO_RIGHT, None),
    ("PIM_popup", R(259, 309), None, None),
    ("Row1", R(310, 320), None, "Assets"),
    ("Row2", R(321, 331), None, "Assets"),
    ("Row3", R(332, 342), None, "Assets"),
    ("Row4", R(343, 353), None, "Assets"),
    ("Row5", R(354, 364), None, "Assets"),
]

def moved(rect, t):
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

# ---------- 2. Timeline ----------
# Keys: (time, value) or (time, value, ease). ease = (in influence %, out influence %) at that key, AE style.
# Each segment eases with cubic-bezier(out of the first key, 0, 1 - in of the second key, 1).
IO = (60, 60)          # gentle ease in and out
SETTLE = (85, 15)      # used on an end key with START on the first key: quick start, long soft landing
START = (15, 15)

def pulse(t0):
    return [(t0, [100, 100], IO), (t0 + 0.4, [103, 103], IO), (t0 + 0.9, [100, 100], IO)]

def glide(k, t0, dur=1.2):
    """A red field slides right and shrinks, passing behind the pop-up, which hides it. No fade."""
    f = moved(FIELD[k], TO_RIGHT)
    fx, fy = center(f)
    tx, ty = POPUP[0] + POPUP[2] * 0.56, ROW[k + 2][1] + 24   # ends well inside the pop-up footprint
    return {"s": pulse(0.8 + 0.12 * (k - 1)) + [(t0, [100, 100], IO), (t0 + dur, [58, 58], IO)],
            "p": [(t0, [0, 0], IO), (t0 + dur, [round(tx - fx, 2), round(ty - fy, 2)], IO)]}

def rise(t0, dy, dur):
    """Slides up into place from dy below, inside its mask group. Quick start, long soft landing."""
    return {"p": [(t0, [0, round(dy, 2)], START), (t0 + dur, [0, 0], SETTLE)]}

ASSET_BOTTOM = MASKS["Assets"][1] + MASKS["Assets"][3]
BODY = MASKS["CleanBody"]

TIMELINE = {
    "Red_L1": {"s": pulse(0.8)}, "Red_L2": {"s": pulse(0.92)}, "Red_L3": {"s": pulse(1.04)},
    "Red_R3": {"s": pulse(1.04)},
    # The pop-up eases in gently: a short fade so it never ghosts, a longer rise and scale, no overshoot.
    "PIM_popup": {"o": [(1.9, 0, START), (2.25, 100, SETTLE)],
                  "s": [(1.9, [96, 96], START), (2.85, [100, 100], SETTLE)],
                  "p": [(1.9, [0, 16], START), (2.85, [0, 0], SETTLE)]},
    "Red_R1": glide(1, 2.6), "Red_R2": glide(2, 2.8),
    # The clean card body slides up over the clutter, then its items follow one by one.
    "Clean_body": rise(3.35, BODY[3], 1.1),
    "Clean_title": rise(3.5, BODY[3], 1.15),
    "Clean_tab": rise(3.6, BODY[3], 1.15),
    "Clean_no": rise(3.7, BODY[3], 1.15),
    "Clean_desc": rise(3.8, BODY[3], 1.15),
    "Clean_cat": rise(3.9, BODY[3], 1.15),
    # Asset rows rise one by one from the bottom of the pop-up's asset list.
    **{f"Row{k}": rise(3.55 + 0.17 * (k - 1), ASSET_BOTTOM - ROW[k][1], 1.0) for k in range(1, 6)},
}

for _n, _k in TIMELINE.items():  # millisecond times, keys in order
    for _p, _keys in _k.items():
        _k[_p] = [(round(k[0], 3), k[1], k[2] if len(k) > 2 else IO) for k in _keys]
        assert all(a[0] < b[0] for a, b in zip(_k[_p], _k[_p][1:])), f"{_n}.{_p} keys out of order"

def bezier(u, x1, x2):  # cubic-bezier(x1, 0, x2, 1), solved for x = u
    lo, hi = 0.0, 1.0
    for _ in range(40):
        m = (lo + hi) / 2
        x = 3 * (1 - m) ** 2 * m * x1 + 3 * (1 - m) * m * m * x2 + m ** 3
        lo, hi = (m, hi) if x < u else (lo, m)
    m = (lo + hi) / 2
    return 3 * (1 - m) * m * m + m ** 3

def value(keys, t, default):
    if not keys:
        return default
    if t <= keys[0][0]:
        return keys[0][1]
    for (t0, v0, e0), (t1, v1, e1) in zip(keys, keys[1:]):
        if t <= t1:
            e = bezier((t - t0) / (t1 - t0), e0[1] / 100, 1 - e1[0] / 100)
            return [a + (b - a) * e for a, b in zip(v0, v1)] if isinstance(v0, list) else v0 + (v1 - v0) * e
    return keys[-1][1]

def state(name, t):
    k = TIMELINE.get(name, {})
    first_o = k["o"][0][1] if "o" in k else 100
    return (value(k.get("o"), t, first_o), value(k.get("p"), t, [0, 0]), value(k.get("s"), t, [100, 100]))

def check_rows():
    """Rows rise in order and never overlap on the way up."""
    for f in range(int(DUR * FPS)):
        t = f / FPS
        ys = [ROW[k][1] + state(f"Row{k}", t)[1][1] for k in range(1, 6)]
        for a, b in zip(ys, ys[1:]):
            if b < ASSET_BOTTOM - 1:  # rows parked at or below the mask edge are hidden
                assert b - a >= 47.7 - 0.5, f"rows overlap at {t:.2f}s: {a:.1f} {b:.1f}"

# ---------- 3. Render the layers ----------
def render_layers():
    ASSETS.mkdir(parents=True, exist_ok=True)
    for old in ASSETS.glob("*.png"):
        old.unlink()
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        subprocess.run(["pdftocairo", "-svg", str(AI), str(d / "src.svg")], check=True)
        svg = (d / "src.svg").read_text()
        svg = svg.split("?>", 1)[1] if svg.lstrip().startswith("<?xml") else svg
        head = re.match(r"\s*(<svg[^>]*>)", svg).group(1)
        body = svg[svg.index(head) + len(head): svg.rindex("</svg>")]
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
        assert defs.startswith("<defs") and len(items) == 395, "unexpected structure in the .ai"
        for name, idx, tf, _ in LAYERS:
            content = "".join(items[i - 1] for i in idx)
            if tf:
                content = f'<g transform="matrix({tf[0]} 0 0 {tf[0]} {tf[1]:.3f} {tf[2]:.3f})">{content}</g>'
            (d / "p.html").write_text(
                "<!doctype html><html><head><style>html,body{margin:0;background:transparent}svg{display:block}</style></head>"
                f"<body>{head}{defs}{content}</svg></body></html>")
            subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                            "--force-device-scale-factor=2", f"--window-size={W},{H}", "--virtual-time-budget=8000",
                            "--default-background-color=00000000", f"--screenshot={ASSETS / (name + '.png')}",
                            (d / "p.html").as_uri()], capture_output=True)
        print("layers:", len(LAYERS), "->", ASSETS)

# ---------- 4. Preview ----------
def mask_alpha(group):
    m = np.zeros((H, W), np.float32)
    x, y, w, h = MASKS[group]
    m[int(round(y)):int(round(y + h)), int(round(x)):int(round(x + w))] = 1
    return m

def frames(loop=True):
    lay = {n: Image.open(ASSETS / f"{n}.png").convert("RGBA").resize((W, H), Image.LANCZOS) for n, *_ in LAYERS}
    group = {n: g for n, _, _, g in LAYERS}
    masks = {g: mask_alpha(g) for g in MASKS}
    order = [n for n, *_ in LAYERS]
    animated = set(TIMELINE) | {n for n in order if group[n]}
    first_anim = next(i for i, n in enumerate(order) if n in animated)
    base = Image.new("RGBA", (W, H))
    for n in order[:first_anim]:
        base.alpha_composite(lay[n])
    rest = order[first_anim:]
    n_main = int(round(DUR * FPS))
    out = []
    for f in range(n_main):
        t = f / FPS
        im = base.copy()
        for n in rest:
            o, (dx, dy), (sx, sy) = state(n, t)
            if o <= 0.5:
                continue
            src = lay[n]
            if (sx, sy) != (100, 100) or dx or dy:
                ax, ay = ANCHOR.get(n, (W / 2, H / 2))
                a, e = 100 / sx, 100 / sy
                src = src.transform((W, H), Image.AFFINE, (a, 0, ax - (ax + dx) * a, 0, e, ay - (ay + dy) * e), Image.BICUBIC)
            if o < 99.5 or group[n]:
                alpha = np.asarray(src.getchannel("A"), np.float32) * (o / 100)
                if group[n]:
                    alpha *= masks[group[n]]
                src = src.copy(); src.putalpha(Image.fromarray(alpha.astype(np.uint8)))
            im.alpha_composite(src)
        out.append(im.convert("RGB"))
    if loop:  # dissolve from the held end frame back to the first frame
        n_tail = int(round(LOOP_TAIL * FPS))
        for i in range(n_tail):
            u = bezier(min(1, (i + 1) / (n_tail - 3)), 0.6, 0.4)
            out.append(Image.blend(out[n_main - 1], out[0], u))
    return out

def render_preview():
    check_rows()
    review = Path(tempfile.gettempdir()) / "row52-review"; review.mkdir(exist_ok=True)
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
        # Full-size GIF: 30 fps, one palette built from whole frames (so the static gradient headline keeps its colours), only changed regions written per frame.
        gif_full = OUT / "row52-cleanup-loop-1080.gif"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", f"{d}/%04d.png",
                        "-vf", "split[a][b];[a]palettegen=max_colors=256:stats_mode=full[p];[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle",
                        "-loop", "0", str(gif_full)], check=True)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(mp4), "-vf", "fps=4,scale=270:-1,tile=8x4",
                        "-frames:v", "1", str(review / "sheet.png")], check=True)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "1.2", "-t", "2.4", "-i", str(mp4), "-vf",
                        "fps=10,crop=520:560:530:380,scale=260:-1,tile=8x3", "-frames:v", "1", str(review / "zoom.png")], check=True)
        fr[int(DUR * FPS) - 1].save(review / "end-frame.png")
        print("frames:", len(fr), "->", mp4.name, gif.name, "| review images (read them):", review)

# ---------- 5. After Effects script ----------
def write_jsx():
    layers = []
    for name, _, _, grp in LAYERS:
        ax, ay = ANCHOR.get(name, (W / 2, H / 2))
        layers.append({"name": name, "file": f"assets/{name}.png", "group": grp, "anchor": [round(ax, 2), round(ay, 2)],
                       "keys": {k: [[t, v, list(e)] for t, v, e in ks] for k, ks in TIMELINE.get(name, {}).items()}})
    data = json.dumps({"comp": "Row52_CleanUp", "w": W, "h": H, "fps": FPS, "dur": DUR,
                       "masks": {g: [round(v, 2) for v in r] for g, r in MASKS.items()}, "layers": layers}, indent=1)
    jsx = """// Row 52 Clean-up: builds the After Effects comp from the layer PNGs in ./assets.
// Run in After Effects: File > Scripts > Run Script File, then pick this file.
// Every layer is a full-frame 2160x2160 PNG at 50 percent scale, so it sits exactly where it sits in the .ai.
// Layers in a mask group go into a precomp (Row52_CleanBody, Row52_Assets) with a rectangle mask on it.
// Keyframe eases carry the in and out influence from the timeline, so the motion matches the preview.
(function () {
  var DATA = %DATA%;
  var root = new File($.fileName).parent;
  app.beginUndoGroup("Build Row52 Clean-up");
  var folder = app.project.items.addFolder("Row52 assets");
  var main = app.project.items.addComp(DATA.comp, DATA.w, DATA.h, 1, DATA.dur, DATA.fps);
  main.bgColor = [1, 1, 1];
  var pre = {};

  function dimsOf(prop) {
    var t = prop.propertyValueType;
    if (t == PropertyValueType.TwoD_SPATIAL || t == PropertyValueType.ThreeD_SPATIAL || t == PropertyValueType.OneD) return 1;
    if (t == PropertyValueType.TwoD) return 2;
    if (t == PropertyValueType.ThreeD) return 3;
    return 1;
  }
  function keyAll(prop, keys, toValue) {
    var j, d, n = dimsOf(prop);
    for (j = 0; j < keys.length; j++) prop.setValueAtTime(keys[j][0], toValue(keys[j][1]));
    for (j = 0; j < keys.length; j++) {
      var k = prop.nearestKeyIndex(keys[j][0]), ein = [], eout = [];
      for (d = 0; d < n; d++) { ein.push(new KeyframeEase(0, keys[j][2][0])); eout.push(new KeyframeEase(0, keys[j][2][1])); }
      prop.setTemporalEaseAtKey(k, ein, eout);
    }
  }
  function maskLayer(layer, r) {
    var m = layer.property("ADBE Mask Parade").addProperty("ADBE Mask Atom");
    var s = new Shape();
    s.vertices = [[r[0], r[1]], [r[0] + r[2], r[1]], [r[0] + r[2], r[1] + r[3]], [r[0], r[1] + r[3]]];
    s.closed = true;
    m.property("ADBE Mask Shape").setValue(s);
  }
  function target(L) {
    if (!L.group) return main;
    if (!pre[L.group]) {
      var c = app.project.items.addComp("Row52_" + L.group, DATA.w, DATA.h, 1, DATA.dur, DATA.fps);
      c.parentFolder = folder;
      var holder = main.layers.add(c);
      holder.name = L.group + " (masked)";
      maskLayer(holder, DATA.masks[L.group]);
      pre[L.group] = c;
    }
    return pre[L.group];
  }

  for (var i = 0; i < DATA.layers.length; i++) {
    var L = DATA.layers[i];
    var item = app.project.importFile(new ImportOptions(new File(root.fsName + "/" + L.file)));
    item.parentFolder = folder;
    var layer = target(L).layers.add(item);
    layer.name = L.name;
    var tr = layer.property("ADBE Transform Group");
    var ap = tr.property("ADBE Anchor Point"), pos = tr.property("ADBE Position");
    var sc = tr.property("ADBE Scale"), op = tr.property("ADBE Opacity");
    var ax = L.anchor[0], ay = L.anchor[1];
    ap.setValue([ax * 2, ay * 2]);
    pos.setValue([ax, ay]);
    sc.setValue([50, 50]);
    if (L.keys.o) keyAll(op, L.keys.o, function (v) { return v; });
    if (L.keys.p) keyAll(pos, L.keys.p, function (v) { return [ax + v[0], ay + v[1]]; });
    if (L.keys.s) keyAll(sc, L.keys.s, function (v) { return [v[0] / 2, v[1] / 2]; });
    layer.motionBlur = !!(L.keys.p || L.keys.s);
  }
  main.motionBlur = true;
  for (var g in pre) pre[g].motionBlur = true;
  main.openInViewer();
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
