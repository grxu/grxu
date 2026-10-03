# Mockup

| File | What it is |
|---|---|
| `mockup.png` | The Floral B mockup, kept as the base |
| `biiig-mockup.png` | The concert tee: a BIIIG emblem on the front, III on the back |
| `biiig-mockup.svg` | **Editable version** of `biiig-mockup.png`. Three layers: `Tee` (the blank tee, embedded), `Front BIIIG emblem` and `Back III` (vector paths, one per ink). Opens in Illustrator, Figma and Inkscape |
| `blank-tee.png` | The Floral B mockup with its artwork painted out, ready for the next tee |
| `biiig-mockup.html` | The layout that builds `biiig-mockup.png` from `mockup.png` and the `print/` SVGs |

![BIIIG mockup](biiig-mockup.png)

## How it's built

- The Floral B artwork is painted over with the shirt colour, `#121212`.
- **Front.** `print/front-biiig.svg` as a left-chest emblem, 220 px wide on the 3400 × 1840 canvas. It's centred where the Floral B emblem sat.
- **Back.** `print/back-iii.svg`, 540 × 657 px. That's the same width and top edge as the Floral B back artwork, centred on the body.

To change a size or position, edit the `left`, `top`, `width` and `height` values in `biiig-mockup.html`, open it in Chrome at 3400 × 1840 and take a screenshot.
