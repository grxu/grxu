#!/usr/bin/env bash
# Render a Truvio layout mock with headless Chrome at 2x, write the 1x file and run QA.
# usage:
#   render_mock.sh --init <source-dir>                 copy kit fonts, lockups and the base template
#   render_mock.sh <input.html> <out-basename> [WxH] [--accent HEX]
#                                                      WxH defaults to 1080x1080 (also 1080x1350)
# Set TRUVIO_KIT or CHROME to override the paths found below.
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
# The Mac kit wins when it exists. Cloud sessions fall back to the kit bundled with the skill.
KIT="${TRUVIO_KIT:-$HOME/Documents/Truvio CoWork/ABOUT ME/truvio-brand/ad-render-kit}"
[[ -d "$KIT" ]] || KIT="$HERE/../assets/render-kit"
if [[ -z "$CHROME" ]]; then
  # The Linux headless shell comes first: full Chromium's new headless mode shrinks the viewport by about 87px.
  for c in "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
           /opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell /opt/pw-browsers/chromium \
           "$(command -v google-chrome || true)" "$(command -v chromium || true)"; do
    if [[ -n "$c" && -x "$c" ]]; then CHROME="$c"; break; fi
  done
fi

if [[ "$1" == "--init" ]]; then
  mkdir -p "$2"
  cp -R "$KIT/fonts" "$KIT/assets" "$2/"
  cp "$HERE/../assets/mock-base.html" "$2/"
  echo "ready: $2 (fonts/, assets/, mock-base.html) from $KIT"
  exit 0
fi

in="$1"; base="$2"; size="${3:-1080x1080}"
W="${size%x*}"; H="${size#*x}"
url=$(python3 -c 'import pathlib,sys;print(pathlib.Path(sys.argv[1]).resolve().as_uri())' "$in")
abs_base=$(python3 -c 'import os,sys;print(os.path.abspath(sys.argv[1]))' "$base")
flags=(--headless=new --disable-gpu --hide-scrollbars --allow-file-access-from-files
       --force-device-scale-factor=2 --window-size=$W,$H --virtual-time-budget=6000)
# Headless Chrome running as root on Linux needs the sandbox off.
[[ "$(uname)" == Linux ]] && flags+=(--no-sandbox)
"$CHROME" "${flags[@]}" --screenshot="${abs_base}@2x.png" "$url" 2>/dev/null
"$CHROME" "${flags[@]}" --dump-dom "$url" 2>/dev/null \
  | python3 -c '
import sys,re,html,json
m=re.search(r"<pre id=\"qa\">(.*?)</pre>",sys.stdin.read(),re.S)
if not m: print("no QA block in page"); sys.exit()
q=html.unescape(m.group(1)); print(q)
vp=json.loads(q).get("viewport")
if vp and vp!=[int(sys.argv[1]),int(sys.argv[2])]:
    print(f"WARNING: viewport {vp[0]}x{vp[1]}, expected {sys.argv[1]}x{sys.argv[2]}. Layout is wrong. Use another Chrome build.")
' "$W" "$H"
python3 "$HERE/qa_mock.py" "$base" "${@:4}"
echo "contact sheet: python3 $HERE/qa_mock.py --sheet out.png a.png b.png ..."
