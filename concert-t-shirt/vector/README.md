# BIIIG vector

Clean vector trace of the BIIIG poster artwork. The print "scatter" texture is removed, so every edge is sharp.

There are two versions. The only difference is the centre of the red block.

| v1: with the small cream BIIIG | v2: small BIIIG merged into the red and black |
| --- | --- |
| ![v1 preview](biiig-preview.png) | ![v2 preview](biiig-v2-preview.png) |

*The previews are shown on cream. The SVGs themselves have a transparent background.*

| File | What it is |
| --- | --- |
| `biiig.svg` | v1: all four inks in one file, one path per ink: `black`, `blue`, `yellow`, `red` (stacked bottom to top) |
| `separations/biiig-<ink>.svg` | v1: one ink per file, for screen-print separations |
| `biiig-v2.svg` | v2: same layout as v1, without the small BIIIG |
| `separations-v2/biiig-v2-<ink>.svg` | v2: one ink per file |

## Inks

| Ink | Hex (sampled from the artwork) |
| --- | --- |
| Black | `#0D0D09` |
| Blue | `#0756C6` |
| Yellow | `#FDBB05` |
| Red | `#E73A07` |

## Notes

- **Transparent background.** Every cream area is a true cut-out, so the shirt colour shows through. That includes the flame shapes, the gaps between the legs and (in v1) the small BIIIG.
- **Trap.** Black runs about 5 px (at the 1920 px artboard) under the blue, yellow and red edges, so no gaps show between colours.
- **Cleaned-up geometry:**
  - The three big circles are exact circles of equal size, evenly spaced and centred on the artboard. The three red circles are the same.
  - Straight edges are straight.
  - The flame tips run into the points where the circles cross.
- **Rebuilt from the large shapes.** The small red flames and the small cream BIIIG inside the red block are scaled copies of the large flames and letters. In the source they were too small to trace cleanly (the BIIIG also had an embossed look). The small BIIIG is now a flat cut-out.
- **v2 centre.** The small BIIIG is filled in with the red and black that surround it. The two black slots in the red block were hidden behind those letters in the source. In v2 their tops are drawn as mirror images of their pointed bottoms, so the red III matches top and bottom. Everything outside the centre is identical to v1.
