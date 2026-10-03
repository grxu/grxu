# Mockup

| File | What it is |
|---|---|
| `mockup.png` | The Floral B mockup, kept as the base |
| `biiig-mockup.png` | The concert tee: BIIIG on the front, III on the back |
| `biiig-mockup.html` | The layout that builds `biiig-mockup.png` from `mockup.png` and the `print/` SVGs |

![BIIIG mockup](biiig-mockup.png)

## How it's built

- The Floral B artwork is painted over with the shirt colour, `#121212`.
- **Front.** `print/front-biiig.svg`, 660 px wide on the 3400 × 1840 canvas. That's about 57% of the body width. It's centred on the body, about 165 px below the collar.
- **Back.** `print/back-iii.svg`, 540 × 657 px. That's the same width and top edge as the Floral B back artwork, centred on the body.

To change a size or position, edit the `left`, `top`, `width` and `height` values in `biiig-mockup.html`, open it in Chrome at 3400 × 1840 and take a screenshot.
