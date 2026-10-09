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
| R2 | `R2.png` | `4088cd46-251a-4d00-86cb-28daaf009c73` | Nano Banana Pro · 1:1 · 2K · batch 2, R0 attached · two runs | 8 credits |
| T1 | `T1.png` | `61d6578b-3808-4c7c-a4ac-4c4a169ef611` | Nano Banana Pro · 1:1 · 2K · batch 2, T0 attached · two runs | 8 credits |

Nano Banana Pro is 2 credits per image. Kling 3.0 pro (1080p tier), sound off, is 1.75 credits per second.

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

## R2 batch notes
All four keep the rotunda identical to R0 (same outline, drift of 1 to 3 levels out of 255), and in all four the sheet is gone from the tabletop.

Run 1, kit prompt as written. In both images the tube sticks a long way out toward the camera and down to the tabletop, so the spiral end sits on the floor rather than in the ring.
- `bd0c2c33-9ac7-4e27-9eeb-728fac9b3bbe`: also has a band around the tube just outside the porthole that could read as tape. Out.
- `0fb6a102-98c4-426c-ba0e-0d8c6c3d2a84`: no tape, but long, down to the floor. Out.

Run 2, kit prompt plus: "Most of the tube is already inside the porthole. Only a short stub sticks out, no longer than it is wide, so the spiral end sits right inside the teal ring. It does not reach the tabletop."
- `4088cd46-251a-4d00-86cb-28daaf009c73`: **pick.** A short stub with the spiral end right at the teal ring, ending above the plinth. No tape.
- `92aa0a08-ba7a-4f8a-a3eb-a89f622bb453`: no tape, but the stub runs down to the front edge of the base. Out.

## T1 batch notes
Fallback only: Step 11 cuts this sheet out as `file-fold.png`. The tower is unchanged from T0 in all four images (window drift about 2 out of 255).

Run 1, kit prompt as written. In both images the sheet grew to about 1.5 to 2× its T0 size and slid left, and the crease ran front to back, with the lifted half rising up and to the left instead of toward the tower.
- `e085a619-26e2-4f18-9793-945f4ea6b689`: Out.
- `70998f13-bd77-49c5-9020-bde29261bc9b`: Out.

Run 2, kit prompt plus: "The sheet keeps its exact size and spot from the reference, centred in front of the tower. The crease runs left to right, parallel to the tower's front. The half nearest the camera lies flat where it was; the half nearest the tower lifts toward the slit."
- `61d6578b-3808-4c7c-a4ac-4c4a169ef611`: **pick.** Crease runs left to right. The front half lies flat over T0's sheet, a little wider on the left (857 to 1105, against 917 to 1130). The back half lifts toward the tower with the grey band along its top edge. It stands steeper than 60° and covers the lower part of the slit.
- `3671c01a-04de-4d1d-bd9d-b53388731ce0`: the crease is diagonal and the lifted half runs up to the tower's right side. The sheet is far longer. Out.

## V1 attempts
Kling 3.0 · pro · 1:1 · 3 s (Kling's shortest) · sound off · batch 2. First frame T0, last frame T2, kit prompt word for word. There's no negative-prompt field, so it was left out. Each clip comes back at 1440×1440, 24 fps, 73 frames. 10.5 credits per run.

Run 1:
- `1c563c97-c3f3-4931-b0c7-865759932369`: the sheet hovers flat for about 1.4 s and grows as it rises. Over f49 to f55 zigzags sprout from its edge and it shrinks into the pleat: a morph. Tower drift up to 6 out of 255.
- `77c12a4a-9625-4651-9995-c0253015509d`: hovers for about 1.2 s, then smears and ghosts into a finished pleat over f42 to f46, with motion blur: a dissolve. Tower drift up to 3.5.

Run 2 (the kit's one rerun, same settings):
- `92a9c85e-43e2-48b8-9077-f5021a786fe0`: the sheet crumples into a shredded mass (f32 to f44) before becoming a pleat. Tower drift up to 9.7. Out.
- `d35c3873-0de9-46a8-888e-c8deeaf920ac`: closest. Flat until f36, one ghosted in-between frame at f37, a finished pleat at f38: an instant snap rather than crease by crease, and the grey band disappears. Then it turns and steps into the slit cleanly. Tower drift up to 4.2, no hands.

### V1 decision: hybrid, AE stills plus D
`V1.mp4` is `d35c3873-0de9-46a8-888e-c8deeaf920ac`. In AE, build the fold as stop-motion:
1. T0's flat sheet (`file-flat.png` over `plate-T`).
2. T1's half-fold (`file-fold.png` over `plate-T`).
3. `V1.mp4` from source frame 38 at 24 fps: the finished pleat turning and stepping into the slit, then the hold.

From f38 to the end is 35 source frames, about 18 frames at 12 fps, which fits V1's slot (frames 6 to 23). Nothing before f38 is used, so the flat-to-pleat snap never shows.
