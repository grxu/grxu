# Print vendor pack

Everything the print vendor needs for the BIGBANG tee. Send the files in this folder; start with `BIGBANG_tee_print_spec.pdf`.

| File | What it is |
|---|---|
| `BIGBANG_tee_print_spec.pdf` | Two-page spec: mockup, print sizes, placement measurements, method, file list and notes |
| `FRONT_left-chest_100x100mm.pdf` | Front print file at actual size. Vector, with the flowers embedded at 300 ppi |
| `FRONT_left-chest_100x100mm_300dpi.png` | The same, as a transparent PNG (1182 × 1182 px) |
| `BACK_277.5x317.4mm.pdf` | Back print file at actual size. All vector |
| `BACK_277.5x317.4mm_300dpi.png` | The same, as a transparent PNG (3278 × 3749 px) |
| `BIGBANG_tee_mockup.png` | Mockup of both prints on the tee |

## How these differ from the `.ai` files in `print/`

- **No background box.** Both `.ai` files have a solid box behind the art: `#212121` on the back, black on the front. On a black tee it would print as a visible rectangle. Here it's removed, and nothing else changes: the print output is identical pixel for pixel.
- **No Illustrator editing data.** The back `.ai` keeps Illustrator's own copy of the artwork, box included. Illustrator opens that copy instead of the PDF, so it's stripped from these files. That way the box can't come back when the vendor opens them.
- **Real back size in the name.** The back artboard is 277.5 × 317.4 mm. The BIGBANG lettering is 270 mm wide, and the lion pokes out past it.

## Placement

Measured on the mockup, at 2.11 px per mm.

| Location | Size | Placement |
|---|---|---|
| Front, left chest | 100 × 100 mm | Top 15 cm below the high point of the shoulder (HPS). Centre 12 cm from the centre front |
| Back | 277.5 × 317.4 mm | Centred. Top 11 cm below the back neck seam |
