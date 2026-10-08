# Higgsfield jobs: Every bank GIF

Batch size from Step 2 on: 2 per generation, stills and clips alike.

Layout ref upload: media `0e3bc410-2710-4369-8dcd-52e587894867`

| Step | Pick | Job | Model · settings | Cost |
|---|---|---|---|---|
| T0 | `T0.png` | `fc2feafc-d818-4673-90cc-1d379751b74f` | Nano Banana Pro · 1:1 · 2K · batch 4 | 8 credits |
| T2 | `T2.png` | `1914cd6d-db62-40d2-9bca-d1064072528c` | Nano Banana Pro · 1:1 · 2K · batch 2, T0 attached · two runs | 8 credits |
| C0 | `C0.png` | `37824a55-0c70-4b7f-a7b7-4f24f5fa1846` | Nano Banana Pro · 1:1 · 2K · batch 2, T0 attached | 4 credits |
| C2 | `C2.png` | `8ce9f136-e81a-4034-9c70-dd82b493604c` | Nano Banana Pro · 1:1 · 2K · batch 2, C0 attached · two runs | 8 credits |
| R0 | `R0.png` | `57058009-573b-4070-8628-dcc7e9ff2497` | Nano Banana Pro · 1:1 · 2K · batch 2, T0 attached | 4 credits |

Nano Banana Pro is 2 credits per image.

## Photoshop to-dos for Step 11
- C0: darken the inside of the letterbox slot so it reads as an open gap. As generated it's a solid yellow panel.
- R0: the front of the rotunda's base sits 12px lower than the tower's at 2048 (1134 against 1122). Nudge plate-R up to match when lining the plates up.

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

## C0 batch notes
- `37824a55-0c70-4b7f-a7b7-4f24f5fa1846`: **pick.** The sheet is in the same spot as in T0 (mean diff 7.6 out of 255 over the sheet). The front step is within about 20px of the tower's base line at 2048px. Four columns with a wider middle gap, three steps, golden plaque. The slot is a solid yellow panel with no dark opening; it gets fixed in Photoshop (see the to-dos above).
- `a3d47ec6-6930-4196-a46d-4ee57e51eee9`: the sheet moved about 40px down and the base sits lower. The slot does read as open. Out.

## C2 batch notes
Both runs used the kit prompt plus: "The letterbox slot is an open gap with a thin dark opening, and the sheet goes into that opening." The slot reads as open in all four images, and the bank is unchanged from C0 in all four (same outline, drift of 1 to 7 levels out of 255).

For scale, the sheet on the tabletop in T0 and C0 is 213px wide at 2048px, and the slot plate is 180px. The original sheet is only about 18% wider than the slot.

Run 1, kit prompt plus the open-gap line:
- `c1434458-8acf-4989-905e-79e57978188f`: a slot-width strip draped out of the slot, with the grey band running down its whole length. Doesn't read as stuck. Out.
- `93d23081-042f-475b-a890-ffa70fcb1914`: the clearest jam, with a wide sheet crumpled against both sides of the plate. But the sheet is about 500px wide, roughly 2.3× the original, so V7 would have to grow it. Out.

Run 2, run 1 prompt plus: "The sheet is the same size as the sheet that lay on the tabletop, only a little wider than the slot, so its two side edges catch on the plate and crumple."
- `8ce9f136-e81a-4034-9c70-dd82b493604c`: **pick.** About 1.5× the original width, with the grey band just inside the slot. It reads as soft cloth draped over the steps rather than crisp paper, and its edges don't catch on the plate.
- `e5773157-64d9-4ed4-8e47-afe51730a471`: a draped strip again. Out.

## R0 batch notes
Both keep the sheet where it was in T0 (mean diff about 5 out of 255 over the sheet). Both are about twice the tower's width, centred on the frame, and both read clearly at 400px.
- `42d65f36-c588-4674-8378-148055b7b048`: base on the tower's line (3px off). But the lantern spire reaches y 269, which is 13% from the top: higher than the tower's top and inside the top 15% that has to stay clear. The drum is deeply fluted. Out.
- `57058009-573b-4070-8628-dcc7e9ff2497`: **pick.** The top sits at y 369, a little lower than the tower (301), with the top 15% clear. A few shallow grooves, a plain teal ring and a teal plaque. The base front is 12px lower than the tower's; see the to-dos.
