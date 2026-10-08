# Run order: Every bank GIF (Higgsfield)

Work top to bottom. Every prompt is final and complete, so copy each code block as it is. Don't move to the next step until the "Check" for the current step passes.

Background files (only if you need the why):
- Video plan: `higgsfield-video-bank-formats-gif.md`
- Stills and the AE fallback: `higgsfield-prompt-bank-formats-gif.md`

Save every pick into `Bank Formats/higgsfield-refs/` with the step name, for example `T0.png` or `V1.mp4`.

---

# Part 1: Stills

Nano Banana Pro · 1:1 · 2K

## Step 1. T0, tower master (the most important still)
Attach: `bank-formats-one-bank-layout-ref_1080x1080.png` · Batch: 4

```text
Match the layout of the reference image exactly: the same building in the same position and size, the same sheet of paper in the same spot, the same empty areas. Render it as a premium studio 3D scene. High-end product visualisation, physically based materials, soft global illumination, crisp detail. A single miniature bank building stands alone in the centre of a smooth, matte, deep violet tabletop that sweeps up seamlessly into a deep violet backdrop (hex #400685). It is one continuous colour, with no horizon line, no gradient, no vignette and no texture. The building is a slim modern tower, a crisp matte white architectural model, like white resin and laser-cut card, with sharp clean edges and very soft rounded corners. Its front has a neat grid of small square windows in the upper two thirds. At street level sits one deposit slot: a tall, narrow vertical slit framed by a thin metal plate in sky blue (hex #008FC4). Above the slot sits a tiny white plaque with a simple bank pictogram, a triangular pediment over columns, in the same sky blue. On the tabletop, centred in front of the tower, lies one small sheet of white paper, flat, with a thin dark grey band along its far edge (hex #6D757A) and a few thin light grey lines. A faint, soft pool of cool lavender light lies on the floor around the base of the tower. Soft studio light from the upper left, gentle fill, a soft clean contact shadow falling to the lower right, true-to-life colour, sharp focus, clean and noise-free, no film grain. There are no letters, no words and no numbers anywhere in the image. No bank names, no logos, no flags, no people, no hands, no figurines, no other buildings, no trees, no cars, nothing else in the frame. The tower stands between 15 and 60 percent of the frame height. The top 15 percent and the bottom 40 percent of the frame are empty, flat violet.
```

Check:
- The slit and plaque read at 400px wide.
- The sheet sits centred in front of the base, fully flat.
- The top-left and the bottom 40 percent are empty violet.

Everything else is built from T0, so send it to me before you go on.

## Step 2. T2, tower with the file in the slit
Attach: T0 · Batch: 2

```text
Same scene, same camera, same lighting, same colours, same sheet of paper. Change only what is described below. Everything else stays exactly the same. The sheet is gone from the tabletop. It has been folded into a tight, narrow accordion pleat and pushed into the tower's vertical slit. The end of the pleat still shows in the lower half of the slit, white zigzag folds with a small soft shadow. It fits the slit.
```

Check: the tower and the light didn't change. Overlay it on T0 at 50 percent to compare.

## Step 3. C0, classical bank
Attach: T0 · Batch: 2

```text
Same scene, same camera, same lighting, same colours, same sheet of paper. Change only what is described below. Everything else stays exactly the same. Replace the tower with a different miniature bank building, in the same matte white material, standing on the same spot. The new building is a classical bank: a triangular pediment over four columns, standing on three wide, shallow steps, with a wall set back behind the columns. It is wider than the tower, and the middle gap between the columns is wider than the others. In that middle gap, at about chest height on a person, sits one deposit slot: a wide, flat letterbox slot framed by a thin metal plate in golden yellow (hex #FFB310). Above it, a tiny white plaque with the same bank pictogram in golden yellow. The sheet of paper on the tabletop stays exactly where it is, flat. The soft lavender floor pool sits around the base of the steps.
```

Check: the base sits on the same line as the tower. The sheet hasn't moved.

## Step 4. C2, classical jammed (the payoff)
Attach: C0 · Batch: 2

```text
Same scene, same camera, same lighting, same colours, same sheet of paper. Change only what is described below. Everything else stays exactly the same. The sheet is gone from the tabletop. It has been pushed halfway into the wide golden yellow letterbox slot, and it is stuck. The sheet is clearly too wide for the slot. It buckles outward below the slot, creased and crumpled at both sides where it presses against the plate. The dark grey band shows just inside the slot. It hangs down over the front steps and casts a soft shadow. This is the only crumpled paper in the image.
```

Check: it's clearly stuck, not fitting. The bank is unchanged from C0.

## Step 5. R0, rotunda
Attach: T0 · Batch: 2

```text
Same scene, same camera, same lighting, same colours, same sheet of paper. Change only what is described below. Everything else stays exactly the same. Replace the tower with a different miniature bank building, in the same matte white material, standing on the same spot, the same width from the centre line. The new building is a round rotunda with a shallow dome and a small lantern on top, a thin cornice ring under the dome, and a few shallow vertical grooves around the drum. It is shorter and wider than the tower. Its top sits a little lower and its sides reach a little wider. At street level sits one deposit slot: a round porthole framed by a thin metal ring in deep teal (hex #006D5B). Above it, a tiny white plaque with the same bank pictogram in deep teal. The sheet of paper on the tabletop stays exactly where it is, flat. The soft lavender floor pool sits around the base of the rotunda.
```

Check: the base sits on the same line as the tower. The sheet hasn't moved.

## Step 6. R2, rotunda with the file in the porthole (no tape)
Attach: R0 · Batch: 2

```text
Same scene, same camera, same lighting, same colours, same sheet of paper. Change only what is described below. Everything else stays exactly the same. The sheet is gone from the tabletop. It has been rolled into a tight paper tube and pushed into the round porthole. The open end of the tube faces the camera and fills the porthole. You can see the spiral of the rolled paper. It fits. No tape.
```

Check: no tape. Tape that isn't in R0 would fade in during the video.

## Step 7. T1, tower with the file folding (fallback only)
Attach: T0 · Batch: 2

```text
Same scene, same camera, same lighting, same colours, same sheet of paper. Change only what is described below. Everything else stays exactly the same. The sheet of paper in front of the tower is halfway through being folded. Its front half lies flat on the tabletop, in the same spot. Its back half lifts up toward the tower at about 60 degrees, with a crisp crease across the middle and the dark grey band along its top edge.
```

The video doesn't use T1. It's cheap insurance: if a paper clip fails, the AE stop-motion fallback for that beat needs it.

---

# Part 2: Paper clips

Seedance 2.0 · first-and-last-frame · 1:1 · highest resolution · shortest length · Batch: 2

These come first. They are the riskiest. Run V1 as a pilot before spending credits on the others.

## Step 8. V1, tower fold and in (the pilot)
First frame: T0 · Last frame: T2

```text
Locked camera, no camera movement, no zoom. Handmade stop-motion animation, shot on twos at 12 frames per second. The paper moves in small, visible steps, with slight frame-to-frame jitter and tiny imperfections, like a real miniature set animated by a person between frames. No motion blur. The light and the building stay exactly the same in every frame. A premium studio 3D scene: a matte white miniature tower bank stands on a flat, matte, deep violet tabletop, with one sheet of white paper lying flat in front of it. The tower never moves. At 0.5 seconds the sheet lifts off the tabletop by itself and hovers just above it. It folds itself into a tight accordion pleat, one sharp crease at a time, crisp printer paper with real weight. At 2.5 seconds the pleat steps into the tall narrow blue slit on the front of the tower and stops with a small tap, its folded end still showing in the slit. Then everything is still until the end. A soft contact shadow follows the paper. Soft even studio light. No hands, no people, no new objects, no light changes, no flicker, no camera shake.
```

Negative prompt, if there's a field. Use it for every clip:

```text
hands, fingers, people, motion blur, smooth interpolation, camera movement, zoom, pan, camera shake, morphing, melting, fading, dissolve, flicker, light change, new objects, tape, text, letters, numbers, logos, other buildings, building moving, building stretching, gradient background, horizon line, film grain, noise, glass, cartoon, low-poly
```

Check before going on. Send it to me.
- The paper folds in steps. It doesn't melt or fade into the pleat.
- The tower is dead still.
- No hands.

If the paper melts, rerun once. If it still melts, tell me before you run V7 and V4. We'll adjust the wording or switch that beat to the AE stills.

## Step 9. V7, classical jam (the payoff)
First frame: C0 · Last frame: C2

```text
Locked camera, no camera movement, no zoom. Handmade stop-motion animation, shot on twos at 12 frames per second. The paper moves in small, visible steps, with slight frame-to-frame jitter and tiny imperfections, like a real miniature set animated by a person between frames. No motion blur. The light and the building stay exactly the same in every frame. A premium studio 3D scene: a matte white miniature classical bank with a triangular pediment, four columns and three front steps stands on a flat, matte, deep violet tabletop, with one sheet of white paper lying flat in front of it. The bank never moves. At 0.5 seconds the sheet lifts off the tabletop by itself and folds once into a flat panel. At 1.5 seconds it steps toward the wide golden yellow letterbox slot between the middle columns, and its leading edge goes in. The sheet is too wide for the slot. Its corners catch on the slot edges, and it stops dead. It gets pushed again. It buckles outward, creasing and crumpling at both sides against the plate. One more push at 3 seconds, and it buckles further, stuck halfway, hanging down over the front steps. Then everything is still until the end. Crisp printer paper, sharp creases, real weight. A soft contact shadow follows the paper. Soft even studio light. No hands, no people, no new objects, no light changes, no flicker, no camera shake.
```

Check: two visible pushes, the buckle gets worse, and it ends stuck.

## Step 10. V4, rotunda roll and in
First frame: R0 · Last frame: R2

```text
Locked camera, no camera movement, no zoom. Handmade stop-motion animation, shot on twos at 12 frames per second. The paper moves in small, visible steps, with slight frame-to-frame jitter and tiny imperfections, like a real miniature set animated by a person between frames. No motion blur. The light and the building stay exactly the same in every frame. A premium studio 3D scene: a matte white miniature rotunda bank with a shallow dome stands on a flat, matte, deep violet tabletop, with one sheet of white paper lying flat in front of it. The rotunda never moves. At 0.5 seconds the far edge of the sheet curls up by itself and the sheet rolls toward the camera into a tight paper tube, real paper, crisp and springy. At 2 seconds the tube lifts, turns to face the rotunda and steps into the round teal porthole, open end facing the camera, and stops with a small tap. Then everything is still until the end. A soft contact shadow follows the paper. Soft even studio light. No hands, no people, no tape, no new objects, no light changes, no flicker, no camera shake.
```

Check: it rolls in steps, no tape appears, and it ends in the porthole.

---

# Part 3: Photoshop prep

Only the slide clips need this. Do it now.

## Step 11. Make the plates and the file layer
1. T0, R0, C0: clone the sheet off the floor, so the floor is clean violet. Save them as `plate-T.png`, `plate-R.png` and `plate-C.png`.
2. T0: cut the flat sheet and its shadow onto its own layer. Save it as `file-flat.png`.
3. T1: cut the folding sheet the same way. Save it as `file-fold.png`. It's only needed for the fallback.
4. Line them up. Overlay each plate on T0 at 50 percent, and nudge it until the base line and centre line match.

---

# Part 4: Slide clips

Seedance 2.0 · start frame only (image-to-video) · 1:1 · shortest length · Batch: 2

Low risk. Run all four. Use the same negative prompt as in Part 2.

## Step 12. V2, tower out to the left
Start frame: plate-T

```text
Locked camera, no camera movement, no zoom. Handmade stop-motion animation, shot on twos at 12 frames per second. The building moves in small, even steps, like a real miniature set animated by a person between frames. No motion blur. The light stays exactly the same in every frame. A matte white miniature tower bank stands alone on a flat, matte, deep violet tabletop. At 0.5 seconds the tower starts moving to the left along the tabletop in small even steps, as if on a hidden track. The steps get a little longer and it leaves the frame completely by 2 seconds. Its contact shadow and the soft lavender glow under it travel with it. The tower stays upright and rigid and never changes shape. Then the frame is empty, flat violet, until the end. Soft even studio light. No people, no hands, no new objects, no camera shake.
```

## Step 13. V3, rotunda out to the right (reverse it in AE, so it enters)
Start frame: plate-R

```text
Locked camera, no camera movement, no zoom. Handmade stop-motion animation, shot on twos at 12 frames per second. The building moves in small, even steps, like a real miniature set animated by a person between frames. No motion blur. The light stays exactly the same in every frame. A matte white miniature rotunda bank with a shallow dome stands alone on a flat, matte, deep violet tabletop. At 0.5 seconds it rocks back very slightly, as if nudged, settles, and then moves to the right along the tabletop in small even steps, as if on a hidden track. The steps get a little longer and it leaves the frame completely by 2 seconds. Its contact shadow and the soft lavender glow under it travel with it. The rotunda stays rigid and never changes shape. Then the frame is empty, flat violet, until the end. Soft even studio light. No people, no hands, no new objects, no camera shake.
```

## Step 14. V5, rotunda out to the left
Start frame: plate-R

```text
Locked camera, no camera movement, no zoom. Handmade stop-motion animation, shot on twos at 12 frames per second. The building moves in small, even steps, like a real miniature set animated by a person between frames. No motion blur. The light stays exactly the same in every frame. A matte white miniature rotunda bank with a shallow dome stands alone on a flat, matte, deep violet tabletop. At 0.5 seconds the rotunda starts moving to the left along the tabletop in small even steps, as if on a hidden track. The steps get a little longer and it leaves the frame completely by 2 seconds. Its contact shadow and the soft lavender glow under it travel with it. The rotunda stays upright and rigid and never changes shape. Then the frame is empty, flat violet, until the end. Soft even studio light. No people, no hands, no new objects, no camera shake.
```

## Step 15. V6, classical out to the right (reverse it in AE, so it enters)
Start frame: plate-C

```text
Locked camera, no camera movement, no zoom. Handmade stop-motion animation, shot on twos at 12 frames per second. The building moves in small, even steps, like a real miniature set animated by a person between frames. No motion blur. The light stays exactly the same in every frame. A matte white miniature classical bank with a triangular pediment, four columns and three front steps stands alone on a flat, matte, deep violet tabletop. At 0.5 seconds it rocks back very slightly, as if nudged, settles, and then moves to the right along the tabletop in small even steps, as if on a hidden track. The steps get a little longer and it leaves the frame completely by 2 seconds. Its contact shadow and the soft lavender glow under it travel with it. The bank stays rigid and never changes shape. Then the frame is empty, flat violet, until the end. Soft even studio light. No people, no hands, no new objects, no camera shake.
```

Check for all four:
- The bank stays rigid all the way out and leaves the frame cleanly.
- The ground stays violet.

---

# Part 5: Optional

## Step 16. V8, life in the hold
Start frame: C2 · Image-to-video

```text
Locked camera, no camera movement. Handmade stop-motion, shot on twos at 12 frames per second, no motion blur. The jammed sheet in the golden yellow letterbox trembles slightly twice, as if someone gave it a small push, and stays stuck. Nothing else moves. No hands, no new objects, no camera shake.
```

Only use V8 if the finished GIF has room under 5 MB.

---

# Part 6: Into AE
Send me the picks from Steps 8 to 15. I'll check each one against the timeline, then the AE assembly and GIF export follow `higgsfield-video-bank-formats-gif.md`.

## Tally
| Part | Generations |
|------|-------------|
| Stills | 7 runs: T0 at a batch of 4, six edits at a batch of 2 = 16 images |
| Videos | 7 clips at a batch of 2 = 14, plus V8 if you use it |
| Reruns | budget about 4 extra, mostly V1 and V7 |
