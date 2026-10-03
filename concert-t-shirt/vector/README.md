# BIIIG vector

Clean vector trace of the BIIIG poster artwork. The print "scatter" texture is removed, so every edge is sharp.

![preview](biiig-preview.png)

*The preview is shown on cream. The SVGs themselves have a transparent background.*

| File | What it is |
| --- | --- |
| `biiig.svg` | All four inks in one file, one path per ink: `black`, `blue`, `yellow`, `red` (stacked bottom to top) |
| `separations/biiig-<ink>.svg` | One ink per file, for screen-print separations |

## Inks

| Ink | Hex (sampled from the artwork) |
| --- | --- |
| Black | `#0D0D09` |
| Blue | `#0756C6` |
| Yellow | `#FDBB05` |
| Red | `#E73A07` |

## Notes

- **Transparent background.** Every cream area is a true cut-out, so the shirt colour shows through. That includes the flame shapes, the gaps between the legs and the small BIIIG.
- **Trap.** Black runs about 5 px (at the 1920 px artboard) under the blue, yellow and red edges, so no gaps show between colours.
- **Cleaned-up geometry:**
  - The three big circles are exact circles of equal size, evenly spaced and centred on the artboard. The three red circles are the same.
  - Straight edges are straight.
  - The flame tips run into the points where the circles cross.
- **Rebuilt from the large shapes.** The small red flames and the small cream BIIIG inside the red block are scaled copies of the large flames and letters. In the source they were too small to trace cleanly (the BIIIG also had an embossed look). The small BIIIG is now a flat cut-out.
