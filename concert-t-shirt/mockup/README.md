# Mockup

| File | What it is |
|---|---|
| `mockup.png` | The Floral B mockup, kept as the base |
| `bigbang-mockup.png` | **Current design.** The floral B on the front, BIGBANG with the three characters on the back |
| `bigbang-mockup.svg` | Editable version of `bigbang-mockup.png`, in three layers: `Tee` (the blank tee, embedded), `Front floral B` and `Back BIGBANG` (both inlined from the `.ai` files) |
| `bigbang-front.svg`, `bigbang-back.svg` | The two `.ai` print files from `print/`, as SVG with their preview backgrounds removed |
| `bigbang-mockup.html` | The layout that builds `bigbang-mockup.png` |
| `biiig-mockup.png` | The concert tee: a BIIIG emblem on the front, III on the back |
| `biiig-mockup.svg` | **Editable version** of `biiig-mockup.png`. Three layers: `Tee` (the blank tee, embedded), `Front BIIIG emblem` and `Back III` (vector paths, one per ink). Opens in Illustrator, Figma and Inkscape |
| `blank-tee.png` | The Floral B mockup with its artwork painted out, ready for the next tee |
| `biiig-mockup.html` | The layout that builds `biiig-mockup.png` from `mockup.png` and the `print/` SVGs |

![BIGBANG mockup](bigbang-mockup.png)

## How the BIGBANG mockup is built

- It's built on `blank-tee.png`, at 2.11 px per mm. That's the scale of the Floral B artwork on this mockup: its 270 mm back fills 570 px.
- **Front.** `print/FRONT_left-chest_100x100mm.ai`, 100 × 100 mm, so 211 × 211 px. It's centred where the Floral B emblem sat (1130, 546).
- **Back.** `print/BACK_270x317.4mm.ai`. The artboard is 277.5 × 317.4 mm (586 × 670 px): the BIGBANG lettering is 270 mm wide, and the lion pokes out a little past it. It's centred on the back body (x 2519), with its top where the Floral B back artwork started (y 375).
- Both `.ai` files have a solid background behind the art: dark grey `#212121` on the back, black on the front. On a black tee those would print as visible boxes, so the mockup leaves them out. If they're meant to print, put them back in `bigbang-front.svg` and `bigbang-back.svg`.

To change a size or position, edit the `left`, `top`, `width` and `height` values in `bigbang-mockup.html`, open it in Chrome at 3400 × 1840 and take a screenshot.

## How the BIIIG mockup is built

![BIIIG mockup](biiig-mockup.png)

- The Floral B artwork is painted over with the shirt colour, `#121212`.
- **Front.** `print/front-biiig.svg` as a left-chest emblem, 220 px wide on the 3400 × 1840 canvas. It's centred where the Floral B emblem sat.
- **Back.** `print/back-iii.svg`, 540 × 657 px. That's the same width and top edge as the Floral B back artwork, centred on the body.

To change a size or position, edit the `left`, `top`, `width` and `height` values in `biiig-mockup.html`, open it in Chrome at 3400 × 1840 and take a screenshot.
