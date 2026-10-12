#!/usr/bin/env bash
# Contact sheets for reviewing a Higgsfield clip.
# usage: clip_frames.sh <video> [out-dir] [zoom-seconds]
# Writes sheet.png (whole clip at 4 fps) and zoom.png (first N seconds at 8 fps, centre crop), then prints clip info.
set -e
V="$1"; O="${2:-$(dirname "$V")/clip-review}"; Z="${3:-3}"
mkdir -p "$O"
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate -of compact "$V"
ffmpeg -v error -y -i "$V" -vf "fps=4,scale=270:-1,tile=6x5" -frames:v 1 "$O/sheet.png"
ffmpeg -v error -y -i "$V" -t "$Z" -vf "fps=8,crop=iw*0.62:ih*0.65:iw*0.19:ih*0.3,scale=200:-1,tile=8x3" -frames:v 1 "$O/zoom.png"
echo "sheet (4 fps, read left to right, 0.25s per tile): $O/sheet.png"
echo "zoom (first ${Z}s, 8 fps, 0.125s per tile): $O/zoom.png"
echo "single frame: ffmpeg -v error -ss <sec> -i \"$V\" -frames:v 1 $O/f.png"
