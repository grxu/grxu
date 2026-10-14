# Row 52 Clean-up animation

Built from Grady's final Illustrator file, `source/Truvio-PIM-for-BC-Row-52.ai`. 1080x1080, 30 fps, 6 seconds, silent. Signed off as idea A, the Clean-up (14 Oct 2026).

The copy line it turns into motion: "Move enrichment into Truvio PIM and sync back only what BC needs." The Truvio PIM side opens as the same cluttered card as the BC Card side. Two red enrichment fields leave the card and become assets in the PIM pop-up. The card cleans up underneath, and the clip lands on the static ad.

## Files
- `row52-cleanup-loop-1080.mp4`: preview, H.264, 6.5 s. The last 0.5 s dissolves back to the first frame, so it loops.
- `row52-cleanup-preview-540.gif`: small preview for Teams or Slack, 15 fps, loops.
- `assets/*.png`: 21 layers cut from the .ai, each a full-frame 2160x2160 transparent PNG. Every layer sits exactly where it sits in the .ai.
- `build_row52_cleanup.jsx`: builds the comp in After Effects from those PNGs, with every keyframe below.
- `../source/build_animation.py`: rebuilds the layers, the preview and the script from one timeline. Change the timing there and run it again.

## Build it in After Effects
1. Keep the `assets` folder next to the .jsx.
2. In After Effects: File > Scripts > Run Script File, then pick `build_row52_cleanup.jsx`.
3. It creates a `Row52_CleanUp` comp and a `Row52 assets` folder, and opens the comp.

Every layer comes in at 50 percent scale, since the PNGs are 2x. Anchor points sit on the parts that move, so scale happens around each part. Keyframes use a 60 percent ease in and out. The script has not been run in After Effects yet, because none is available here. Test it before you build on it.

The AE comp is the 6 s ad without the loop tail. For a loop, add a 0.5 s cross dissolve from the end frame back to the start.

## Layers, bottom to top
BG, Logo, Headline, Label_BC, Label_PIM, CTA, Tile_Today, Red_L1 to Red_L3, Tile_PIM_clean, Tile_PIM_clutter, Red_R3, PIM_popup, Row1 to Row5, Red_R1, Red_R2.

- `Tile_Today` is the BC Card tile without its red fields. `Red_L1` to `Red_L3` are those fields.
- `Tile_PIM_clutter` and `Red_R1` to `Red_R3` are the BC Card tile copied onto the right tile. They are the start state of the Truvio PIM side.
- `Red_R1` and `Red_R2` sit above the pop-up, so they fly over it.

## Timing (30 fps)
| Time | Frame | What happens |
|---|---|---|
| 0.00 | 0 | Both tiles show the cluttered card. Pop-up and asset rows hidden. |
| 0.60 to 1.31 | 18 to 39 | Red fields pulse once, 100 to 104 to 100 percent, staggered 0.08 s down each card. |
| 1.15 to 1.70 | 35 to 51 | Pop-up springs in: opacity 0 to 100 by 1.45, scale 88 to 102 to 100, rises 20 px. |
| 1.32 to 1.55 | 40 to 47 | Red_R1 and Red_R2 lift to 103 percent. |
| 1.75 to 2.50 | 53 to 75 | Red_R1 flies to asset row 1 and shrinks to the row (61.7 by 81.6 percent). Fades out over its last 0.2 s. |
| 1.95 to 2.70 | 59 to 81 | Red_R2 flies to asset row 2 (61.7 by 100 percent). Fades out over its last 0.2 s. |
| 2.30 to 2.55 | 69 to 77 | Row 1 appears, scale 96 to 100 percent. |
| 2.50 to 2.75 | 75 to 83 | Row 2 appears, scale 96 to 100 percent. |
| 2.40 to 3.00 | 72 to 90 | Clutter and Red_R3 fade out. The clean card shows underneath. |
| 2.75 to 3.35 | 83 to 101 | Rows 3, 4 and 5 rise 14 px and fade in, 0.15 s apart. |
| 3.35 to 6.00 | 101 to 180 | Hold. Every layer sits exactly as in the static ad. |

## Why the third red field does not fly
It is cut off at the bottom edge of the tile in the .ai. Flying a half field reads as a mistake, so it fades with the clutter.

## QA
- The final-state layers stacked together match the .ai rendered at 2x. 0.85 percent of pixels differ by more than 60 levels, all on antialiased edges.
- The held end frame equals the static ad. The start frame shows the cluttered card on both sides.
- The script passes a syntax check and avoids modern JavaScript, so ExtendScript can read it.
