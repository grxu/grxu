# BIGBANG SG concert tee: print files

Black tee. Front: a crisp white slab "B" over a watercolour cluster of a blue
iris, pink and cream peonies, a yellow rose and a crimson peony, worn on the
left chest. Back: the BIGBANG wordmark over three piano keys.

![mockup](mockup/mockup.png)

## Send these to the printer

| File | What it is |
|---|---|
| `print-files/FRONT_left-chest_120x120mm.pdf` / `.svg` | Front, 12 × 12 cm: watercolour flowers (embedded image) + vector B |
| `print-files/FRONT_left-chest_120x120mm_300dpi.png` | Same, 300 dpi at print size, transparent background |
| `print-files/FRONT_left-chest_120x120mm_2048px.png` | Same at the flowers' full resolution (~430 dpi at 12 cm) |
| `print-files/BACK_270x303.9mm.pdf` / `.svg` | Back, vector, 27 × 30.4 cm, white ink only |
| `print-files/BACK_270x303.9mm_300dpi.png` | Same, raster at 300 dpi, transparent background |
| `mockup/spec-sheet.pdf` | Placement and size sheet (A3) for the vendor |

Notes for the vendor:

- **Print method:** DTF or DTG. The front is a full-colour watercolour, so it
  is not a spot-colour screen-print job. The back is a single colour (white).
- **Background is transparent.** The black in the previews is the shirt. Do not
  print it.
- **Placement:** front emblem 7 cm from the centre line on the wearer's left
  chest, top edge 6.5 cm below the centre-front collar seam. Back art centred,
  10 cm below the centre-back collar seam.
- All text is converted to outlines, so no fonts are needed to open the files.
- Colours are sRGB. White = 100% white ink.

## Editing

- **Illustrator / Inkscape / Figma:** open the `.svg` (or `.pdf`). Layers are
  named: *Flowers (full colour)*, which holds the watercolour as one embedded
  image; *B (white ink)*, a vector path you can resize or move; and on the
  back, *BIGBANG wordmark* and *Piano keys*.
- **Swap the flowers:** the watercolour source is the PNG in `upload-here/`.
  Replace it, then re-run the build.
- **Regenerate:** `pip install cairosvg fonttools shapely pillow` then
  `python3 src/build.py`. The `SETTINGS` block at the top of `src/build.py`
  controls the front size, back width, an optional line under the keys, an
  optional black gap around the B, and placement. Set `FLOWERS = "vector"` to
  switch back to the procedural vector flowers in `src/flowers.py`.

## Fonts

- "B" and wordmark: **Ultra** (Astigmatic), Apache 2.0, stretched
  horizontally.
- Spec sheet labels and the optional line under the keys: **Montserrat** SemiBold,
  SIL OFL 1.1.

Licence files are in `fonts/`. The watercolour flowers were generated for
this shirt with an AI image model (GPT Image 2.5 via Higgsfield). Nothing is
traced from other artwork.

"BIGBANG" is a trademark of its owners. This design is meant for personal
fan use. Selling shirts with the name on them needs permission.
