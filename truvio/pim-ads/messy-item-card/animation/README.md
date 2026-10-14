# Row 52 Clean-up animation

Built from Grady's final Illustrator file, `source/Truvio-PIM-for-BC-Row-52.ai`. 1080x1080, 30 fps, 10 seconds, silent. Signed off as idea A, the Clean-up (14 Oct 2026). v2 (14 Oct 2026): smoother, per Grady. No opacity swap behind the pop-up, a gentler pop-up, and rows rising one by one. v3 (14 Oct 2026): the finished pop-up holds 2 s longer, 4.8 s in all.

The copy line it turns into motion: "Move enrichment into Truvio PIM and sync back only what BC needs." The Truvio PIM side opens as the same cluttered card as the BC Card side. The pop-up eases in, two red enrichment fields glide into it, the clean card rises up over the clutter piece by piece, and the assets rise into the pop-up one by one. The clip lands on the static ad.

## Files
- `row52-cleanup-loop-1080.mp4`: preview, H.264, 10.6 s. The 10 s ad, then a 0.6 s dissolve back to the first frame, so it loops.
- `row52-cleanup-loop-1080.gif`: full-size GIF, 1080x1080, 30 fps, 10.6 s, loops. 2.4 MB. Rendered from the source frames with one 256-colour palette, so expect faint grain in the gradient headline at 100 percent zoom.
- `row52-cleanup-preview-540.gif`: small preview for Teams or Slack, 15 fps, loops.
- `assets/*.png`: 27 layers cut from the .ai, each a full-frame 2160x2160 transparent PNG. Every layer sits exactly where it sits in the .ai.
- `build_row52_cleanup.jsx`: builds the comp in After Effects from those PNGs, with every keyframe below.
- `../source/build_animation.py`: rebuilds the layers, the preview and the script from one timeline. Change the timing there and run it again.

## Build it in After Effects
1. Keep the `assets` folder next to the .jsx.
2. In After Effects: File > Scripts > Run Script File, then pick `build_row52_cleanup.jsx`.
3. It creates a `Row52_CleanUp` comp, two masked precomps (`Row52_CleanBody` and `Row52_Assets`) and a `Row52 assets` folder, and opens the comp. Motion blur is on for the moving layers.

Every layer comes in at 50 percent scale, since the PNGs are 2x. Anchor points sit on the parts that move, so scale happens around each part. Entrances use a 15 percent ease out of the first key and an 85 percent ease into the last, for a quick start and a long soft landing. Pulses and the red field glides use 60 percent both ways. The script has not been run in After Effects yet, because none is available here. Test it before you build on it.

The AE comp is the 10 s ad without the loop tail. For a loop, add a 0.6 s cross dissolve from the end frame back to the start.

## Layers, bottom to top
BG, Logo, Headline, Label_BC, Label_PIM, CTA, Tile_Today, Red_L1 to Red_L3, Tile_PIM_base, Tile_PIM_clutter, Red_R3, [CleanBody precomp: Clean_body, Clean_title, Clean_tab, Clean_no, Clean_desc, Clean_cat], Red_R1, Red_R2, PIM_popup, [Assets precomp: Row1 to Row5].

- `Tile_Today` is the BC Card tile without its red fields. `Red_L1` to `Red_L3` are those fields.
- `Tile_PIM_base` is the right tile's shadow, card and header. `Tile_PIM_clutter` and `Red_R1` to `Red_R3` are the BC Card tile copied on top of it: the start state.
- The CleanBody precomp is masked to the card body (x 561.9, y 481.4, 448 by 407.1). The clean body and its items slide up into it from below.
- `Red_R1` and `Red_R2` sit under the pop-up, so they disappear behind it as they glide in. No fade.
- The Assets precomp is masked to the pop-up's asset list (x 717.2, y 608, 293.1 by 296). Rows rise into it from its bottom edge.

## Timing (30 fps)
| Time | Frame | What happens |
|---|---|---|
| 0.00 | 0 | Both tiles show the cluttered card. Pop-up hidden, rows parked below the asset list. |
| 0.80 to 1.94 | 24 to 58 | Red fields pulse once, 100 to 103 to 100 percent, 0.12 s apart down each card. |
| 1.90 to 2.85 | 57 to 86 | Pop-up eases in: opacity 0 to 100 by 2.25, scale 96 to 100, rises 16 px. No overshoot. |
| 2.60 to 3.80 | 78 to 114 | Red_R1 glides right and down, shrinks to 58 percent and slips behind the pop-up. |
| 2.80 to 4.00 | 84 to 120 | Red_R2 does the same, 0.2 s later. |
| 3.35 to 4.45 | 101 to 134 | The clean card body slides up from the bottom of the tile and covers the clutter. |
| 3.50 to 5.05 | 105 to 152 | Its items follow one by one, 0.1 s apart: title, Item tab, No., Description, Item Category Code. |
| 3.55 to 5.23 | 107 to 157 | Asset rows 1 to 5 rise from the bottom of the asset list, 0.17 s apart, and settle into place. |
| 5.23 to 10.00 | 157 to 300 | Hold, 4.8 s. Every layer sits exactly as in the static ad. |

## Why the third red field does not fly
It is cut off at the bottom edge of the tile in the .ai. Flying a half field reads as a mistake, so the clean card covers it instead.

## QA
- The final-state layers stacked together match the .ai rendered at 2x. 0.85 percent of pixels differ by more than 60 levels, all on antialiased edges.
- The held end frame equals the static ad. The start frame shows the cluttered card on both sides.
- The build checks every frame that no two visible rows overlap on the way up.
- The script passes a syntax check and avoids modern JavaScript, so ExtendScript can read it.
