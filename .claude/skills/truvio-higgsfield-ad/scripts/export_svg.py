"""Export a rendered mock as Illustrator files: a layered SVG and a PDF-based .ai.

usage: export_svg.py <mock.html> <out-basename> [WxH]

Writes <out>.svg (named groups, live text by PostScript font name, vector lockup) and
<out>.ai (the same artwork as a PDF-compatible Illustrator file), then renders the SVG
back and compares it with a fresh render of the mock.

Groups come from data-layer="Name" on elements in the mock. Fonts map Slab 700 to
MuseoSlab-700 and BVP to BeVietnamPro-Regular / -ExtraBold, so Illustrator asks for the
licensed fonts. Run it from anywhere. It needs the same Chrome as render_mock.sh.
"""
import glob, html, os, re, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
src, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
W, H = (int(v) for v in (sys.argv[3] if len(sys.argv) > 3 else "1080x1080").split("x"))

def chrome():
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    for c in ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
              *sorted(glob.glob("/opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell")),
              "/opt/pw-browsers/chromium"]:
        if os.access(c, os.X_OK):
            return c
    sys.exit("no Chrome found, set CHROME")

CHROME = chrome()
FLAGS = ["--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
         "--virtual-time-budget=8000"] + (["--no-sandbox"] if sys.platform.startswith("linux") else [])

def run(*args):
    return subprocess.run([CHROME, *FLAGS, *args], capture_output=True, text=True).stdout

# 1. Walk the mock in the browser and collect the SVG.
walker = (HERE / "svg_walker.js").read_text()
page = src.read_text()
hook = ("<pre id=\"svgout\"></pre><script>document.fonts.ready.then(() => setTimeout(() => {\n"
        + walker + "\n}, 300));</script>")
tmp = src.with_name("_export_" + src.name)
tmp.write_text(page.replace("</body>", hook + "\n</body>"))
try:
    dom = run(f"--window-size={W},{H}", "--dump-dom", tmp.as_uri())
finally:
    tmp.unlink()
m = re.search(r'<pre id="svgout">(.*?)</pre>', dom, re.S)
if not m or not m.group(1).strip():
    sys.exit("walker produced no SVG")
svg = html.unescape(m.group(1))

# 2. Swap image placeholders for the vector logo when an SVG sits next to the PNG, else embed the PNG.
def place(mt):
    name, img, box = mt.group(1), mt.group(2), [float(v) for v in mt.group(3).split()]
    vec = (src.parent / img).with_suffix(".svg")
    if vec.exists():
        t = vec.read_text()
        vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', t).group(1).split()]
        inner = re.search(r"<svg[^>]*>(.*)</svg>", t, re.S).group(1)
        inner = re.sub(r"<!--.*?-->|<style>.*?</style>", "", inner, flags=re.S)
        inner = inner.replace('id="linear-gradient"', 'id="lockup-gradient"')
        inner = inner.replace('class="st0"', 'fill="url(#lockup-gradient)"').replace('class="st1"', 'fill="#FFFFFF"')
        s = box[2] / vb[2]
        return (f'<g id="{name}" transform="translate({box[0]} {box[1]}) scale({s:.5f})">'
                + re.sub(r"\s+\n", "\n", inner).strip() + "</g>")
    import base64
    data = base64.b64encode((src.parent / img).read_bytes()).decode()
    return (f'<image id="{name}" x="{box[0]}" y="{box[1]}" width="{box[2]}" height="{box[3]}" '
            f'xlink:href="data:image/png;base64,{data}"/>')

svg = re.sub(r'<g id="([^"]+)" data-img="([^"]+)" data-box="([^"]+)"></g>', place, svg)
svg = '<?xml version="1.0" encoding="UTF-8"?>\n' + svg
out.with_suffix(".svg").write_text(svg)

# 3. Render the SVG back, with the PostScript font names aliased to the kit fonts, for QA and the .ai.
fonts = src.parent / "fonts"
alias = "".join(
    f"@font-face{{font-family:'{ps}';src:url('{(fonts / f).as_uri()}') format('woff2')}}"
    for ps, f in [("MuseoSlab-700", "arvo-latin-700-normal.woff2"),
                  ("BeVietnamPro-Regular", "be-vietnam-pro-latin-400-normal.woff2"),
                  ("BeVietnamPro-ExtraBold", "be-vietnam-pro-latin-800-normal.woff2")])
inline = svg.split("?>", 1)[1]
wrap = (f"<!doctype html><html><head><meta charset='utf-8'><style>{alias}"
        f"@page{{size:{W}px {H}px;margin:0}}*{{margin:0;padding:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}}"
        f"html,body{{width:{W}px;height:{H}px;overflow:hidden;background:#fff}}svg{{display:block}}</style></head>"
        f"<body>{inline}</body></html>")
with tempfile.TemporaryDirectory() as d:
    w = Path(d) / "wrap.html"
    w.write_text(wrap)
    back = Path(d) / "back.png"
    run(f"--window-size={W},{H}", f"--screenshot={back}", w.as_uri())
    mock = Path(d) / "mock.png"
    run(f"--window-size={W},{H}", f"--screenshot={mock}", src.as_uri())
    raw = Path(d) / "raw.pdf"
    run("--no-pdf-header-footer", f"--print-to-pdf={raw}", w.as_uri())

    from PIL import Image, ImageChops
    import numpy as np
    a = np.asarray(Image.open(back).convert("RGB")).astype(int)
    b = np.asarray(Image.open(mock).convert("RGB")).astype(int)
    diff = np.abs(a - b).sum(2)
    print(f"svg vs mock: mean diff {diff.mean():.2f} per px, {(diff > 60).mean() * 100:.2f}% of px differ by more than 60")
    qa = Path(tempfile.gettempdir()) / f"{out.name}-svgqa"
    qa.mkdir(exist_ok=True)
    Image.fromarray(np.uint8(np.clip(diff, 0, 255))).save(qa / "diff.png")
    Image.open(back).save(qa / "svg-render.png")
    print("QA images (read them):", qa / "svg-render.png", qa / "diff.png")

    # PDF page boxes come out a fraction too big. Trim them to the exact canvas.
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import RectangleObject
    r, wr = PdfReader(raw), PdfWriter()
    for pg in r.pages:
        x0, y0, x1, y1 = (float(v) for v in pg.mediabox)
        box = RectangleObject([x0, y1 - H * 0.75, x0 + W * 0.75, y1])
        pg.mediabox = box; pg.cropbox = box; pg.trimbox = box; pg.artbox = box
        wr.add_page(pg)
    wr.add_metadata({"/Title": out.name, "/Creator": "truvio-higgsfield-ad export_svg.py"})
    wr.write(out.with_suffix(".ai"))
    print("pages:", len(r.pages))

print("wrote", out.with_suffix(".svg"), out.with_suffix(".ai"))
groups = re.findall(r'<g id="([^"]+)"', svg)
print("named groups:", len(groups), "|", ", ".join(g for g in groups if not re.search(r"_\d+$", g)))
print("fonts:", sorted(set(re.findall(r"font-family=\"'([^']+)'\"", svg))))
