# Runs natively in BC (Row 57): animated 1:1

Truvio PIM LinkedIn ad, 1:1 (1080x1080). The static Illustrator layout (`source/Truvio_-_PIM_for_BC_-_Row_57.ai`) with its pastel chat bubbles removed. The Jitter chat animation (`source/PIM_for_BC_-_Row_57.json`) now plays inside the phone screen.

## Deliverables
- `runs-natively-bc-row57-1x1-30fps.mp4`: H.264, 1080x1080, 30fps, 13.0s.
- `runs-natively-bc-row57-1x1-12fps.gif`: 1080x1080, 12fps, full 256-colour palette, 156 frames, 13.0s, loops. GIF delays are in 1/100s, so frames repeat 8/8/9cs to average exactly 12fps.
- `runs-natively-bc-row57-final-frame.png`: the last frame, as a still.

## Chat (from the JSON)
- Them: IT wants us to get a PIM 😩 another system to learn
- Me: Ours runs inside Business Central
- Them: Inside BC? Same screens, same roles?
- Me: Same look, same permissions. It's Truvio PIM
- Them: Ok, booking a demo 🚀

## Decisions (13 Oct 2026)
- Bubbles: the JSON's iMessage style (bright blue and grey), not the AI file's pastels.
- Header kept as in the AI file: Sarah (PM), 13 OCT 17:18, status bar 17:21.
- Ending as in the JSON, about 1s hold on the last message. No extra hold or loop fade.
- The Jitter watermark sits outside the phone screen, so the clip mask crops it out.

## How it was built
- The AI file is rendered at 2x. Its old bubbles are painted out with screen white (2x box x 600 to 1600, y 1030 to 2160) and saved as `source/background-no-bubbles@2x.png`.
- The Lottie (1080x1920, 60fps) is scaled to the screen width: 510px, scale 0.4722, left edge x 294.5. Its top sits at y 355, so the first bubble starts at y 525, where the old one did. It is clipped to the screen from y 500 down.
- `source/composite.js` (lottie-web 5.12.2 + Playwright) screenshots each frame: every 2nd for 30fps, every 5th for 12fps. ffmpeg encodes them.
