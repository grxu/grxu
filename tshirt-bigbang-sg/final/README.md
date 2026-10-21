# Final artwork: white tee

Made from your raw Illustrator files in `../final-raw/` by `src/invert_final.py`.
All edits are on the vector files themselves.

| File | What it is |
|---|---|
| `FRONT_left-chest_100x100mm_white-tee.ai` / `.pdf` | Front, 10 × 10 cm. Black B with a thin white gap against the flowers. Flowers are the full-resolution originals (~980 dpi) in exactly your positions. Transparent background. |
| `FRONT_..._300dpi.png` / `_hires.png` | Transparent renders (300 dpi and 900 dpi). |
| `BACK_277.5x317.4mm_white-tee.ai` / `.pdf` | Back, 27.75 × 31.7 cm. Black BIGBANG wordmark and piano keys; the characters are unchanged (full colour). Transparent background. |
| `BACK_..._300dpi.png` | Transparent render, 300 dpi. |
| `mockup_white-tee.png`, `spec-sheet_white-tee.pdf` | Mockup on a white tee and the A3 vendor spec sheet. |

What changed from the raw files:
- **Front:** the black background rectangle is removed. The B fill is now
  black and its 3 pt outline stroke is white. The two flower images are
  swapped for lossless full-res versions with real transparency, replacing
  the downsampled image and JPEG with their luminosity masks.
- **Back:** the dark grey background rectangle is removed, and the wordmark
  and three keys are filled black. Illustrator's private data block is
  removed so Illustrator shows these edits; it opens the file from its PDF
  content.

The .ai files are PDF-compatible. In Illustrator, use File → Save As → Adobe
Illustrator (.ai) once to make them fully native.
