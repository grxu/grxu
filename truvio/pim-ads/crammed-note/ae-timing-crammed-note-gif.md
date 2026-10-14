# After Effects timing: crammed note GIF (Row 53)

Animated GIF of the Row 53 static, for a LinkedIn single image ad. 1080x1080, 25 fps, 145 frames (5.8 s), loops forever. Everything is built in After Effects from the Row 53 .ai. Higgsfield isn't used, because everything that moves is UI and type, and a video model redraws letters.

Measured against the original Row 53 file (`source/row53-original.png`). The arrows, the 23:51 status bar and the stray "7:02" were fixed in Grady's copy afterwards. Recheck the card position on the fixed file.

## How the motion matches the copy
- "Things we crammed into our BC item cards": frame 1 shows the whole note, title included. The static hides the title under the card.
- 23:47 to 23:51: the clock moves on four minutes, then the reply arrives.
- "47 custom fields → attributes", "6 languages → translations", "Image links, spec sheets → assets": each arrow draws, then its PIM word lands. The problem stays on the left and the fix arrives on the right.
- "Sorted in Truvio PIM": the check draws last inside the card.
- "There's a better place for it.": the brand gradient wipes across "better" as the final beat.

## Decisions (14 Oct 2026)
- Idea 1, "The 23:51 reply".
- Frame 1: the note only, no card. "better" in white.
- "better" wipe: added.
- Clock cut: kept. 23:47 at the start, 23:51 from frame 20.
- 25 fps. GIF stores frame delays in hundredths of a second, so 25 fps gives an exact 4/100 s per frame. 30 fps can't be timed exactly.

## Layer prep in Illustrator
Top-level layers, one element each. These names are used in the table.
- Background
- Lockup
- Headline_rest: the headline without "better"
- Better_white: "better" in #FFFFFF, same position
- Better_gradient: "better" with the brand gradient, exactly over Better_white
- Subline
- Phone: frame, screen and note, without the status bar time
- Clock_2347, Clock_2351: the status bar time, one layer each
- Card_bg: the white card with its shadow
- Card_header: app icon, TRUVIO PIM, 23:51
- Card_left: 47 custom fields, 6 languages, Image links, spec sheets
- Arrow_1, Arrow_2, Arrow_3
- Word_1 (attributes), Word_2 (translations), Word_3 (assets)
- Check_circle, Check_tick
- Sorted_text

## Setup in After Effects
1. Import the .ai as Composition, Retain Layer Sizes. Comp settings: 1080x1080, 25 fps, 145 frames.
2. Select every Card_, Arrow_, Word_, Check_ and Sorted_ layer. Pre-compose with "Move all attributes" and the full 1080x1080 size, so nothing shifts. Name it CARD. It starts at frame 0, so frame numbers inside it match the main comp.
3. Use the precomp, not a parent null. Opacity doesn't pass from a parent to its children, and the card has to fade as one piece.
4. CARD anchor point: the card's top centre, x 540, y 580. Position (540, 580).
5. Arrows and check: Create Shapes from Vector Layer, then add Trim Paths. If an arrow is two paths (shaft and head), set Trim Multiple Shapes to Individually, so the head draws after the shaft.
6. Better_gradient: add Linear Wipe, Feather 20.

## Timing table
Frame numbers are main comp frames. Time = frame / 25. "Ease out" means Easy Ease Out on the first key.

| Frame | Time (s) | Layer | Property and keys | Easing |
|---|---|---|---|---|
| 0 to 19 | 0.00 to 0.76 | all | Hold. Full note readable. Clock_2347 on, Clock_2351 off. CARD opacity 0. Better_gradient wipe at 100 percent (hidden). This is frame 1 of the GIF. | |
| 20 | 0.80 | Clock_2347, Clock_2351 | Hard cut: Clock_2347 off, Clock_2351 on | Hold keys |
| 25, 32, 35 | 1.00 to 1.40 | CARD | Position (540, 520), (540, 585), (540, 580). Drops 60 px, overshoots 5 px, settles | Key 25 ease out at 85 percent influence, keys 32 and 35 Easy Ease |
| 25 to 33 | 1.00 to 1.32 | CARD | Scale 96 to 100 percent | Ease out |
| 25 to 29 | 1.00 to 1.16 | CARD | Opacity 0 to 100 percent | Linear |
| 37 to 43 | 1.48 to 1.72 | Arrow_1 | Trim Paths End 0 to 100 percent | Ease out, 70 percent influence |
| 41 to 46 | 1.64 to 1.84 | Word_1 | Opacity 0 to 100 percent. Position X from 12 px left to its final spot | Ease out |
| 43 to 49 | 1.72 to 1.96 | Arrow_2 | Trim Paths End 0 to 100 percent | Ease out, 70 percent influence |
| 47 to 52 | 1.88 to 2.08 | Word_2 | Opacity 0 to 100 percent. Position X from 12 px left | Ease out |
| 49 to 55 | 1.96 to 2.20 | Arrow_3 | Trim Paths End 0 to 100 percent | Ease out, 70 percent influence |
| 53 to 58 | 2.12 to 2.32 | Word_3 | Opacity 0 to 100 percent. Position X from 12 px left | Ease out |
| 58 to 65 | 2.32 to 2.60 | Check_circle | Trim Paths End 0 to 100 percent. Set Offset so it starts at the top and runs clockwise | Ease out |
| 62 to 66 | 2.48 to 2.64 | Check_tick | Trim Paths End 0 to 100 percent | Ease out |
| 62 to 68 | 2.48 to 2.72 | Sorted_text | Opacity 0 to 100 percent. Position X from 10 px left | Ease out |
| 70 to 82 | 2.80 to 3.28 | Better_gradient | Linear Wipe Transition Completion 100 to 0 percent. The reveal runs left to right along the gradient's own angle | Easy Ease |
| 82 to 132 | 3.28 to 5.28 | all | Hold, 2 s. Matches the static ad | |
| 133 to 140 | 5.32 to 5.60 | CARD | Position (540, 580) to (540, 540). Opacity 100 to 0 percent | Ease in, 75 percent influence |
| 133 to 140 | 5.32 to 5.60 | Better_gradient | Opacity 100 to 0 percent, so "better" is white again for the loop | Linear |
| 141 | 5.64 | Clock_2347, Clock_2351 | Hard cut back: Clock_2351 off, Clock_2347 on | Hold keys |
| 141 to 144 | 5.64 to 5.76 | all | Matches frame 0, so the loop doesn't pop | |

## Export to GIF
1. Render a PNG sequence from AE: 1080x1080, 25 fps, frames 0 to 144. A ProRes 4444 MOV works too.
2. Upload the sequence (zipped) or the MOV, and the conversion runs here: one palette built from all frames, no dither on the ground, only changed areas stored per frame, gifsicle at -O3, loop forever. The report covers file size and frame count.
3. LinkedIn limits: 5 MB and 250 frames. This GIF is 145 frames.
4. Over 5 MB: try light lossy GIF compression first, then 128 colours, then 20 fps. 20 fps changes every frame number in this table, so it goes last.

## QA after export
- Frame 0: no card, full note, 23:47, "better" white.
- Frame 35: the card has settled. No overshoot left.
- Frame 82: "better" fully in gradient.
- Frame 132: matches the fixed static ad.
- Frames 141 to 144 match frame 0.
- The ground gradient shows no banding or shimmer between frames.
- Under 5 MB, 145 frames, loops forever.

## Fixes if it misses
- The card drop feels slow: tighten to frames 25 to 33 and cut the overshoot to 3 px.
- The arrows feel busy: offset them 4 frames apart instead of 6.
- An arrow draws backwards from its head: reverse the path direction, or animate Trim Paths Start 100 to 0 percent instead.
- The wipe pulls focus from the card: start it at frame 74 and shorten it to 10 frames.
- The loop pops: check Clock_2347, Clock_2351 and Better_gradient at frame 141.
- The ground shimmers in the GIF: rebuild the palette with dither off, or flatten the ground in the comp.
