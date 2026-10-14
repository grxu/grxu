#!/bin/bash
# 3. Turns the After Effects PNG sequence into the LinkedIn GIF.
# Double-click it and pick the crammed-note-gif-png folder. Or in Terminal:
#   bash 3-make-gif.command /path/to/crammed-note-gif-png
# Needs ffmpeg. gifsicle is optional and makes the file smaller. Install both with Homebrew:
#   brew install ffmpeg gifsicle
# LinkedIn single image ads take GIFs up to 5 MB and 250 frames. This one is 145 frames at 25 fps.

LIMIT=5000000
DIR="$1"
if [ -z "$DIR" ]; then
  DIR=$(osascript -e 'POSIX path of (choose folder with prompt "Pick the crammed-note-gif-png folder")' 2>/dev/null)
  [ -n "$DIR" ] || { echo "No folder picked."; exit 1; }
fi
DIR="${DIR%/}"

if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "ffmpeg isn't installed."
  echo "Install Homebrew from https://brew.sh, then run: brew install ffmpeg gifsicle"
  exit 1
fi
COUNT=$(ls "$DIR"/crammed-note-gif_*.png 2>/dev/null | wc -l | tr -d ' ')
if [ "$COUNT" -eq 0 ]; then echo "No crammed-note-gif_#####.png frames in $DIR"; exit 1; fi
[ "$COUNT" -eq 145 ] || echo "Note: $COUNT frames found, the timing table has 145."

OUT="$(dirname "$DIR")/crammed-note-linkedin.gif"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
size() { wc -c < "$1" | tr -d ' '; }
mb() { awk -v b="$1" 'BEGIN { printf "%.2f MB", b / 1000000 }'; }

# One palette from every frame. Bayer dither is the same on every frame, so the violet ground
# doesn't band and doesn't shimmer. Only the changed rectangle is stored per frame.
build() {   # $1 = colours, $2 = dither
  ffmpeg -v error -y -framerate 25 -start_number 0 -i "$DIR/crammed-note-gif_%05d.png" \
    -vf "palettegen=stats_mode=full:max_colors=$1" "$TMP/palette.png" &&
  ffmpeg -v error -y -framerate 25 -start_number 0 -i "$DIR/crammed-note-gif_%05d.png" -i "$TMP/palette.png" \
    -lavfi "paletteuse=dither=$2:diff_mode=rectangle" -loop 0 "$OUT"
}
squeeze() { command -v gifsicle >/dev/null 2>&1 && gifsicle -O3 $1 -b "$OUT"; }

echo "Making the GIF from $COUNT frames..."
build 256 "bayer:bayer_scale=5" || { echo "ffmpeg failed."; exit 1; }
squeeze
STEP="256 colours"
if [ "$(size "$OUT")" -gt $LIMIT ] && command -v gifsicle >/dev/null 2>&1; then
  build 256 "bayer:bayer_scale=5" && squeeze "--lossy=30"; STEP="256 colours, light lossy"
fi
if [ "$(size "$OUT")" -gt $LIMIT ]; then
  build 128 "bayer:bayer_scale=5" && squeeze "--lossy=30"; STEP="128 colours"
fi

FRAMES=$(ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 "$OUT" 2>/dev/null)
BYTES=$(size "$OUT")
echo ""
echo "Saved: $OUT"
echo "Size:   $(mb "$BYTES") ($STEP). LinkedIn limit: 5 MB."
echo "Frames: ${FRAMES:-?}. LinkedIn limit: 250."
command -v gifsicle >/dev/null 2>&1 || echo "Tip: brew install gifsicle makes it smaller."
if [ "$BYTES" -gt $LIMIT ]; then
  echo "Still over 5 MB. Upload the PNG folder to Claude and it will look at what's taking the space."
  exit 2
fi
[ "$(uname)" = "Darwin" ] && open -R "$OUT"
exit 0
