# Higgsfield jobs: Every bank GIF

Batch size from Step 2 on: 2 per generation, stills and clips alike.

Layout ref upload: media `0e3bc410-2710-4369-8dcd-52e587894867`

| Step | Pick | Job | Model · settings | Cost |
|---|---|---|---|---|
| T0 | `T0.png` | `fc2feafc-d818-4673-90cc-1d379751b74f` | Nano Banana Pro · 1:1 · 2K · batch 4 | 8 credits |
| T2 | `T2.png` | `1914cd6d-db62-40d2-9bca-d1064072528c` | Nano Banana Pro · 1:1 · 2K · batch 2, T0 attached · two runs | 8 credits |

Nano Banana Pro is 2 credits per image.

## T0 batch notes
- `9f416128-a7d1-4f14-b38e-dde43541a38a`: hard floor edge across the full width at about 65% height. Reads as a horizon. Out.
- `fc2feafc-d818-4673-90cc-1d379751b74f`: **pick.** Soft light pool with no edge, crisp tower, sheet flat and centred, grey band on the far edge.
- `96498a14-afcb-4d3f-89cd-fae74ed5cad8`: same hard floor edge as the first. Out.
- `f5c96422-9a08-4a47-93a0-740161029f3e`: passes, but the light pool has a visible oval rim that spills further into the bottom 40%, and the grey band sits back from the sheet's edge.

## T2 batch notes
Both runs pass the overlay check. The tower bbox is pixel-identical to T0, and the light and background drift by 1 to 2 levels out of 255.

Run 1, kit prompt as written. In both images the pleat hangs out of the slit down to the tabletop, so it reads as coming out rather than fitting.
- `e0ca3e1d-8344-4343-bf9e-6fe696641b84`: pleat wider than the slit, offset to the left. Out.
- `b843e642-9572-4410-8d2f-c5d405021439`: slit-width, but hangs past the base onto the floor. Out.

Run 2, kit prompt plus: "Most of the pleat is already inside the slit. Only its last few folds stick out of the lower half of the slit, no wider than the slit, and they do not reach the tabletop."
- `30c7e94b-0a9e-4c31-af15-3434c344cde4`: still hangs onto the floor. Out.
- `1914cd6d-db62-40d2-9bca-d1064072528c`: **pick.** Slit-width pleat sitting in the slit. Its tip finishes level with the tower base, clear of the tabletop. It runs the full height of the slit and covers the plate's left edge.
