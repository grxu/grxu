# BIGBANG SG concert tee: print files

Black tee. Front: a white slab "B" (the same letter shape as the back wordmark)
with a thin black outline, with watercolour flowers set asymmetrically around it:
a blue iris and fern sprigs at the top right, a red peony and a yellow rose
along the bottom left. Worn on the left chest. Back: the BIGBANG wordmark over
three hand-brushed piano keys.

![mockup](mockup/mockup.png)

## Send these to the printer

| File | What it is |
|---|---|
| `print-files/FRONT_left-chest_100x100mm.pdf` / `.svg` | Front, 10 × 10 cm: watercolour flowers (embedded image) + vector B |
| `print-files/FRONT_left-chest_100x100mm_300dpi.png` | Same, 300 dpi at print size, transparent background |
| `print-files/FRONT_left-chest_100x100mm_3875px.png` | Same at the flowers' full resolution (~980 dpi at 10 cm) |
| `print-files/BACK_270x317.4mm.pdf` / `.svg` | Back, vector, 27 × 31.7 cm, white ink only |
| `print-files/BACK_270x317.4mm_300dpi.png` | Same, raster at 300 dpi, transparent background |
| `mockup/spec-sheet.pdf` | Placement and size sheet (A3) for the vendor |

Notes for the vendor:

- **Print method:** DTF or DTG. The front is a full-colour watercolour, so it
  is not a spot-colour screen-print job. The back is a single colour (white).
- **Background is transparent.** The black in the previews is the shirt. Do not
  print it.
- **Placement:** front emblem 8 cm from the centre line on the wearer's left
  chest, top edge 7.5 cm below the centre-front collar seam. Back art centred,
  10 cm below the centre-back collar seam.
- All text is converted to outlines, so no fonts are needed to open the files.
- Colours are sRGB. White = 100% white ink.

The other front option the team compared is kept in `print-files/options/` and
`mockup/options/` (option 2 is the one chosen).

## Editing

- **Illustrator / Inkscape / Figma:** open the `.svg` (or `.pdf`). Layers are
  named: *Flowers (full colour)*, which holds the watercolour as one embedded
  image; *B (white ink)*, a vector path you can resize or move; and on the
  back, *BIGBANG wordmark* and *Piano keys*.
- **Swap the flowers:** the layouts live in `upload-here/layout-*/`.
  `src/options.py` cuts out the white background, softens the generator's
  straight edge and places the B. `build.py` then uses
  `src/assets/option-2.png` (set by `EDITED_PNG`).
- **Regenerate:** `pip install cairosvg fonttools shapely pillow` then
  `python3 src/build.py`. The `SETTINGS` block at the top of `src/build.py`
  controls the front size, the B's size, shape and position, the black gap
  around it, the brushed or clean keys, an optional line under the keys, and
  placement. Set `FLOWERS = "vector"` to
  switch back to the procedural vector flowers in `src/flowers.py`.

## Fonts

- "B" and wordmark: **Ultra** (Astigmatic), Apache 2.0, stretched
  horizontally.
- Spec sheet labels and the optional line under the keys: **Montserrat** SemiBold,
  SIL OFL 1.1.

Licence files are in `fonts/`. The watercolour flowers were generated for
this shirt with AI image models (GPT Image 2.5 and Nano Banana Pro via
Higgsfield). The brushed piano keys are drawn procedurally by `src/brush.py`,
modelled on a reference but not traced from it.

"BIGBANG" is a trademark of its owners. This design is meant for personal
fan use. Selling shirts with the name on them needs permission.
