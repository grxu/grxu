# Higgsfield video: Every bank, one bank at a time GIF (10 s)

The lead build. Higgsfield video makes the motion: the paper really folds, rolls and crumples, and the banks glide in and out with real weight. Everything moves in a handmade stop-motion style, so the work looks like someone did it by hand, not like automation. The camera stays locked. Same story, layout and timeline as the AE build.

## Fallbacks
1. **Per beat.** If one clip fails, swap that beat for its AE stop-motion stills. Every clip lines up with the same frames as the AE timeline, so you can mix the two freely.
2. **Whole GIF.** The AE stop-motion build in `higgsfield-prompt-bank-formats-gif.md`.
3. **Different concept.** The spotlight version, three banks on stage: `higgsfield-prompt-bank-formats-gif-spotlight-FALLBACK.md`.

## Decisions (2026-10-09)
- Grady generates in Higgsfield. Claude writes the prompts and checks the clips.
- Real paper motion, locked camera. No camera moves.
- Stop-motion look on every clip, slides included. The paper folds itself with no hands, so smooth motion would read as magic, which is what Truvio promises. Stop-motion steps read as handmade, a person nudging the paper frame by frame. That matches the copy: by hand.
- Everything else is unchanged:
  - Order: tower, rotunda, classical (the jam).
  - The banks slide through.
  - One file stays centre front.
  - Premium studio 3D, 1:1, 1080x1080, 12 fps GIF, 120 frames.

## Copy (final, for reference only. Nothing changed)
- On design (big): Every bank. A different format.
- On design: Stop reformatting payment files by hand.
- On design (CTA line): Automate it in Dynamics 365 →
- Ads headline: Stop fixing payment files by hand daily
- Ads body: Reformatting addresses for every bank and country requires hours every week. Truvio automates it inside Dynamics 365.
- CTA: https://truvio.com/three-compliance-deadlines-one-dynamics-365-answer

---

## Two rules from earlier video passes

**1. First-and-last-frame mode fades in anything the first frame doesn't have.** It did that to the REJECTED stamps. Two things follow from it:
- **Paper beats are safe.** The sheet is in both the first and the last frame, so the model has to move it, not fade it.
- **Slides are not safe.** Tower in the first frame and rotunda in the last, on the same spot, gives you a tower that morphs into a rotunda. So each slide clip shows one bank only, made from its start frame alone, gliding out of frame. Entrances are exits played in reverse. A rotunda gliding out to the right, reversed, glides in from the right.

**2. The AI ground drifts into a gradient.** Every clip gets keyed onto a flat #400685 solid in AE. That's the same fix as the other motion ads.

## Video settings (all clips)
- Model: Seedance 2.0. Kling is the backup.
- Aspect ratio: 1:1. Resolution: the highest available, 1080p or above.
- Length: the shortest available, usually 5 s. AE retimes every clip to its slot in the timeline.
- Camera: locked. Every prompt starts with "Locked camera."
- Sound: none.
- Batch: 2 per clip. Pick by paper motion first, then by how still the bank stays.

## Stills you need first
Make these from `higgsfield-prompt-bank-formats-gif.md` (T0 master, edits, then the Photoshop prep). T1 isn't needed for video.

| Still | Used as |
|-------|---------|
| T0, R0, C0 | first frames of the paper clips |
| T2, R2, C2 | last frames of the paper clips |
| plate-T, plate-R, plate-C (sheet cloned off the floor) | start frames of the slide clips |
| file-flat.png (cut from T0) | the static file layer during slides |

One change for video: make R2 without the tape. Delete "held with a narrow band of clear tape" from the R2 edit. A tape band that isn't in R0 would fade in mid-roll.

---

## The clips

| Clip | Mode | First frame | Last frame | Used in the GIF at |
|------|------|-------------|------------|--------------------|
| V1 Tower, fold and in | first and last frame | T0 | T2 | frames 6 to 23 |
| V2 Tower, out to the left | start frame only | plate-T | | frames 26 to 33 |
| V3 Rotunda, in from the right | start frame only, then reversed | plate-R | | frames 26 to 33 |
| V4 Rotunda, roll and in | first and last frame | R0 | R2 (no tape) | frames 38 to 55 |
| V5 Rotunda, out to the left | start frame only | plate-R | | frames 58 to 65 |
| V6 Classical, in from the right | start frame only, then reversed | plate-C | | frames 58 to 65 |
| V7 Classical, the jam | first and last frame | C0 | C2 | frames 70 to 119 |
| V1 and V4 reversed, 4x speed | from V1 and V4 | | | frames 24 to 25, 56 to 57 (the pop-back) |

The pop-back is the insert clip played backwards, fast. The file comes out of the slot and unfolds flat, like hitting undo. Same file, redone for the next bank. No extra clip needed.

---

## V1: Tower, fold and in
First frame: T0. Last frame: T2.

Locked camera, no camera movement, no zoom. Handmade stop-motion animation, shot on twos at 12 frames per second. The paper moves in small, visible steps, with slight frame-to-frame jitter and tiny imperfections, like a real miniature set animated by a person between frames. No motion blur. The light and the building stay exactly the same in every frame. A premium studio 3D scene: a matte white miniature tower bank stands on a flat, matte, deep violet tabletop, with one sheet of white paper lying flat in front of it. The tower never moves. At 0.5 seconds the sheet lifts off the tabletop by itself and hovers just above it. It folds itself into a tight accordion pleat, one sharp crease at a time, crisp printer paper with real weight. At 2.5 seconds the pleat steps into the tall narrow blue slit on the front of the tower and stops with a small tap, its folded end still showing in the slit. Then everything is still until the end. A soft contact shadow follows the paper. Soft even studio light. No hands, no people, no new objects, no light changes, no flicker, no camera shake.

## V2: Tower, out to the left
Start frame only: plate-T.

Locked camera, no camera movement, no zoom. Handmade stop-motion animation, shot on twos at 12 frames per second. The building moves in small, even steps, like a real miniature set animated by a person between frames. No motion blur. The light stays exactly the same in every frame. A matte white miniature tower bank stands alone on a flat, matte, deep violet tabletop. At 0.5 seconds the tower starts moving to the left along the tabletop in small even steps, as if on a hidden track. The steps get a little longer and it leaves the frame completely by 2 seconds. Its contact shadow and the soft lavender glow under it travel with it. The tower stays upright and rigid and never changes shape. Then the frame is empty, flat violet, until the end. Soft even studio light. No people, no hands, no new objects, no camera shake.

## V3: Rotunda, in from the right (reverse this one)
Start frame only: plate-R.

Locked camera, no camera movement, no zoom. Handmade stop-motion animation, shot on twos at 12 frames per second. The building moves in small, even steps, like a real miniature set animated by a person between frames. No motion blur. The light stays exactly the same in every frame. A matte white miniature rotunda bank with a shallow dome stands alone on a flat, matte, deep violet tabletop. At 0.5 seconds it rocks back very slightly, as if nudged, settles, and then moves to the right along the tabletop in small even steps, as if on a hidden track. The steps get a little longer and it leaves the frame completely by 2 seconds. Its contact shadow and the soft lavender glow under it travel with it. The rotunda stays rigid and never changes shape. Then the frame is empty, flat violet, until the end. Soft even studio light. No people, no hands, no new objects, no camera shake.

Reverse it in AE. It then steps in from the right, slows, and settles with a small rock. That small rock is the weight AE alone can't fake.

## V4: Rotunda, roll and in
First frame: R0. Last frame: R2, no tape.

Locked camera, no camera movement, no zoom. Handmade stop-motion animation, shot on twos at 12 frames per second. The paper moves in small, visible steps, with slight frame-to-frame jitter and tiny imperfections, like a real miniature set animated by a person between frames. No motion blur. The light and the building stay exactly the same in every frame. A premium studio 3D scene: a matte white miniature rotunda bank with a shallow dome stands on a flat, matte, deep violet tabletop, with one sheet of white paper lying flat in front of it. The rotunda never moves. At 0.5 seconds the far edge of the sheet curls up by itself and the sheet rolls toward the camera into a tight paper tube, real paper, crisp and springy. At 2 seconds the tube lifts, turns to face the rotunda and steps into the round teal porthole, open end facing the camera, and stops with a small tap. Then everything is still until the end. A soft contact shadow follows the paper. Soft even studio light. No hands, no people, no tape, no new objects, no light changes, no flicker, no camera shake.

## V5: Rotunda, out to the left
Start frame only: plate-R.

Same prompt as V2. Replace "tower" with "rotunda bank with a shallow dome".

## V6: Classical, in from the right (reverse this one)
Start frame only: plate-C.

Same prompt as V3. Replace "rotunda bank with a shallow dome" with "classical bank with a triangular pediment, four columns and three front steps". Reverse it in AE.

## V7: Classical, the jam (the payoff)
First frame: C0. Last frame: C2.

Locked camera, no camera movement, no zoom. Handmade stop-motion animation, shot on twos at 12 frames per second. The paper moves in small, visible steps, with slight frame-to-frame jitter and tiny imperfections, like a real miniature set animated by a person between frames. No motion blur. The light and the building stay exactly the same in every frame. A premium studio 3D scene: a matte white miniature classical bank with a triangular pediment, four columns and three front steps stands on a flat, matte, deep violet tabletop, with one sheet of white paper lying flat in front of it. The bank never moves. At 0.5 seconds the sheet lifts off the tabletop by itself and folds once into a flat panel. At 1.5 seconds it steps toward the wide golden yellow letterbox slot between the middle columns, and its leading edge goes in. The sheet is too wide for the slot. Its corners catch on the slot edges, and it stops dead. It gets pushed again. It buckles outward, creasing and crumpling at both sides against the plate. One more push at 3 seconds, and it buckles further, stuck halfway, hanging down over the front steps. Then everything is still until the end. Crisp printer paper, sharp creases, real weight. A soft contact shadow follows the paper. Soft even studio light. No hands, no people, no new objects, no light changes, no flicker, no camera shake.

Use V7 at real speed if it fits. The struggle is the payoff, and it can take 1.5 to 2 seconds before the hold.

## V8 (optional): life in the hold
Start frame only: C2.

Locked camera, no camera movement. Handmade stop-motion, shot on twos at 12 frames per second, no motion blur. The jammed sheet in the golden yellow letterbox trembles slightly twice, as if someone gave it a small push, and stays stuck. Nothing else moves. No hands, no new objects, no camera shake.

Only use V8 if the GIF has room under 5 MB. A still hold costs almost nothing. A moving one costs every frame.

---

## Checking each clip
All clips:
- The motion steps like stop-motion. It doesn't slide smoothly or smear.
- Between steps, only the paper or the bank moves. The light and the ground don't flicker.

Paper clips (V1, V4, V7):
- The paper visibly folds, rolls or buckles. It doesn't fade or melt into its end shape.
- The building stays dead still. Check it with Difference blend against the first frame.
- The last frame matches T2, R2 or C2 closely enough that the AE swap to the still doesn't jump.

Slide clips (V2, V3, V5, V6):
- The bank stays rigid all the way out. No stretching, no morphing.
- It leaves the frame cleanly.
- The ground under it stays violet, not grey or gradient.

Any clip:
- No hands, no new objects, no text.
- Hands or wobble in a few frames: trim around them.
- Hands or wobble throughout: rerun once with "no hands" moved to the start of the prompt.
- Still bad after the rerun: use the AE fallback for that beat.
- The motion comes out smooth, not stepped: move the stop-motion sentence to the very start of the prompt. If it's still smooth, keep it and step it in AE with Posterize Time.
- The light flickers between steps: add "constant studio light, no flicker" at the start. Then patch the building from the still in AE.

## AE assembly
Comp: 1080x1080, 12 fps, 120 frames. Same timeline as the AE build. The frame numbers in the clip table above match it exactly.

Layers, bottom to top:
1. Flat #400685 solid. The ground stays locked for the whole loop.
2. Slide clips, keyed on violet with soft shadows kept, retimed to 8 frames each:
   - V2 and V3 reversed overlap on frames 26 to 33.
   - V5 and V6 reversed overlap on frames 58 to 65.
   - Line up each clip so its bank's first or last frame sits exactly on the resting position.
3. Paper clips V1, V4 and V7, retimed to their slots. Frame Blending off. Add Posterize Time at 12 on every clip, so each step holds for exactly one GIF frame. If a clip came out smooth, Posterize Time at 8 to 10 gives it the stop-motion step in AE.
4. Patch layer: the matching still (T2, R2, C2, or the plates) over everything except the moving paper. It's a feathered mask around the paper's path. The building pixels then come from the still, so they never shimmer.
5. File layer: file-flat.png, static, on during the slides and the flat holds. The AI clips never carry the resting file.
6. Static on top: the lockup and the copy, at the artboard 14 positions.

Holds: end each paper clip by cutting to its still (T2, R2, C2). Still frames compress to almost nothing in the GIF.

## GIF export

AI video carries fine noise that changes every frame. That's the biggest risk to the 5 MB cap. Before export:
- Add Remove Grain, or a light Median at 1px, on the clip layers only.
- Rely on the patch layer. Everything that shouldn't move comes from a still.
- Cut to stills for every hold.

Stop-motion helps here. Each step repeats on twos, and repeated frames cost almost nothing.

Then export with the same settings as the AE build:

```bash
ffmpeg -framerate 12 -i frame_%04d.png -vf "split[a][b];[a]palettegen=stats_mode=diff:max_colors=192[p];[b][p]paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle" -loop 0 bank-formats-one-bank_1080x1080.gif
```

```bash
gifsicle -O3 --lossy=40 bank-formats-one-bank_1080x1080.gif -o bank-formats-one-bank_1080x1080.gif
```

Over 5 MB? Try these in order:
1. Raise `--lossy` to 60, then 80.
2. Drop V8.
3. Drop `max_colors` to 128.
4. Shorten the paper clips by 2 to 3 frames each.
5. Drop to 10 fps.

## Brand check before export
- Ground matches #400685 in every frame. Check frames 0, 30, 60 and 119.
- All three banks rest on the same base line and centre line.
- The file is the same file in every flat frame.
- The paper moves like paper: crisp creases, no melting, no fading.
- No hands, no green, no red, no off-palette colours, no readable text.
- Lockup top-left and copy band match artboard 14. 65px margin on every resting frame.
- 10.0 s, 120 frames, loops forever, 5 MB or under.

## Avoid list (for the negative prompt field)

hands, fingers, people, motion blur, smooth interpolation, camera movement, zoom, pan, camera shake, morphing, melting, fading, dissolve, flicker, light change, new objects, tape, text, letters, numbers, logos, other buildings, building moving, building stretching, gradient background, horizon line, film grain, noise, glass, cartoon, low-poly
