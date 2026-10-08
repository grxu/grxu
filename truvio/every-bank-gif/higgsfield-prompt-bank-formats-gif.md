# Higgsfield stills + AE build (fallback 1): Every bank, one bank at a time GIF (10 s)

Option B as a 10-second looping GIF for a LinkedIn single-image ad. One bank stands on stage at a time. One payment file lies in the same spot, centre front, for the whole loop. A bank slides in, the file gets folded by hand to fit its slot, the bank slides out, and the file springs back flat for the next one. Same file, redone for every bank. The third bank jams it.

Status (2026-10-09): fallback 1. The lead build is Higgsfield video, in `higgsfield-video-bank-formats-gif.md`. That build still needs the stills and the Photoshop prep in this file. The spotlight version, with all three banks on stage, is fallback 2: `higgsfield-prompt-bank-formats-gif-spotlight-FALLBACK.md`.

## Decisions (2026-10-09)
- One bank on stage at a time. Order: tower, rotunda, classical. The classical bank jams, last.
- Transition: slide through. The bank glides out to the left as the next glides in from the right, like a queue that never ends.
- The file stays put, centre front, for all 10 seconds.
- Style: premium studio 3D. Matte white models, soft studio light. No glassmorphism.
- Output: GIF, 1:1, 1080x1080, 12 fps, 120 frames.

## Copy (final, for reference only. Nothing changed)
- On design (big): Every bank. A different format.
- On design: Stop reformatting payment files by hand.
- On design (CTA line): Automate it in Dynamics 365 →
- Ads headline: Stop fixing payment files by hand daily
- Ads body: Reformatting addresses for every bank and country requires hours every week. Truvio automates it inside Dynamics 365.
- CTA: https://truvio.com/three-compliance-deadlines-one-dynamics-365-answer

## Files in this folder
- `bank-formats-one-bank-layout-ref_1080x1080.png`: the flat layout mock, with the tower and the flat file only. No copy, no lockup. Attach it to the first still.
- `bank-formats-one-bank-animatic_1080x1080.gif`: the 10 s timing animatic. It came out at 484 KB. Use it as the timing guide in AE.
- `source/gif-one-bank.html`: the mock source. Each layer renders from a URL, for example `?bank=R&file=in&copy=0`.
- `source/compose-one-bank.py`: builds the animatic frames from those layers. The timeline in it matches the table below.

## LinkedIn GIF limits
- Single-image ads accept animated GIFs. 250 frames at most. One LinkedIn page says 300, so stay under 250. 5 MB at most.
- This GIF is 120 frames. The 5 MB cap is the real limit. See the export section.

## Layout (artboard 14 grid)
- Lockup top-left, inside the 65px margin. The top 15 percent (162px) stays clear.
- The bank stands centred, between 15 and 60 percent of the frame height (162px to 648px).
- All three banks stand on the same line, and each one fills the hero height. The tower is tall and slim. The rotunda and the classical bank are wider.
- The file lies centre front on the floor, in the same spot in every frame.
- The bottom 40 percent (432px) stays empty violet for the copy.
- The copy and lockup are static AE layers on top of every frame. Never in the AI images.
- During a slide, the banks cross the side margins. That's motion, not a margin break. Every resting frame keeps 65px.

## Cast and colours
| Order | Bank | Slot | Slot colour | What the file becomes |
|-------|------|------|-------------|-----------------------|
| 1 | Slim modern tower | tall narrow vertical slit | Celestial Blue #008FC4 | an accordion pleat, pushed into the slit. It fits |
| 2 | Rotunda with a shallow dome | round porthole | Teal Meridian #006D5B | a rolled tube, pushed into the porthole. It fits |
| 3 | Classical bank, pediment and four columns | wide flat letterbox | Yellow Gold #FFB310 | half pushed in, buckled and jammed. It doesn't fit |

- Ground: Deep Violet #400685, flat. Soft floor pool under each bank in Twilight #9C9DEC at low opacity.
- Models: matte white. Payment file: white paper, Dark Gray #6D757A band, Silver #CFD2D4 lines.
- No green. Nothing is solved yet. No red. Gold makes the jam the brightest point of the loop.

---

## How it's built

Seven stills from Nano Banana Pro. After Effects does the slides and the stop-motion timing.

- **The banks slide in AE, not in AI video.** Each bank is a cut-out with its contact shadow, moved with position keyframes. The motion is exact, the models never warp, and every bank lands on the same spot.
- **The paper moves in stop-motion.** Each paper state is a still, swapped on the beat at 12 fps. AI video morphs folding paper into blobs and fades new shapes in. It did that to the REJECTED stamps.
- **There is one file, cut out once.** The flat sheet and the folding sheet come from the tower stills. They sit on their own layer and get reused in front of every bank, so the file never changes between banks.
- **Rotunda and classical inherit the tower's layout.** You generate them with the approved tower still as the reference. A reference image makes Nano Banana treat the job as an edit, so the set, the camera, the light and the sheet stay locked. Only the building changes.

## Settings
- Model: Nano Banana Pro.
- Aspect ratio: 1:1. Resolution: 2K. Downscale to 1080.
- Batch size: 4 for T0. 2 for everything else.

## The seven stills
| Still | Reference to attach | What it is |
|-------|---------------------|------------|
| T0 | the layout ref | tower plus the flat file. The master for the whole GIF |
| T1 | T0 | tower plus the file, folding |
| T2 | T0 | tower with the file pushed into the slit |
| R0 | T0 | rotunda plus the flat file |
| R2 | R0 | rotunda with the file pushed into the porthole |
| C0 | T0 | classical bank plus the flat file |
| C2 | C0 | classical bank with the file jammed in the letterbox |

---

## T0: Tower master (attach the layout ref)

Match the layout of the reference image exactly: the same building in the same position and size, the same sheet of paper in the same spot, the same empty areas. Render it as a premium studio 3D scene. High-end product visualisation, physically based materials, soft global illumination, crisp detail. A single miniature bank building stands alone in the centre of a smooth, matte, deep violet tabletop that sweeps up seamlessly into a deep violet backdrop (hex #400685). It is one continuous colour, with no horizon line, no gradient, no vignette and no texture. The building is a slim modern tower, a crisp matte white architectural model, like white resin and laser-cut card, with sharp clean edges and very soft rounded corners. Its front has a neat grid of small square windows in the upper two thirds. At street level sits one deposit slot: a tall, narrow vertical slit framed by a thin metal plate in sky blue (hex #008FC4). Above the slot sits a tiny white plaque with a simple bank pictogram, a triangular pediment over columns, in the same sky blue. On the tabletop, centred in front of the tower, lies one small sheet of white paper, flat, with a thin dark grey band along its far edge (hex #6D757A) and a few thin light grey lines. A faint, soft pool of cool lavender light lies on the floor around the base of the tower. Soft studio light from the upper left, gentle fill, a soft clean contact shadow falling to the lower right, true-to-life colour, sharp focus, clean and noise-free, no film grain. There are no letters, no words and no numbers anywhere in the image. No bank names, no logos, no flags, no people, no hands, no figurines, no other buildings, no trees, no cars, nothing else in the frame. The tower stands between 15 and 60 percent of the frame height. The top 15 percent and the bottom 40 percent of the frame are empty, flat violet.

Approve T0 before anything else. Check:
- The slit and plaque read at 400px wide.
- The sheet sits centred, in front of the base, fully flat.
- Empty violet top-left (for the lockup) and in the bottom 40 percent.

---

## Edits (start each one with this line)

Same scene, same camera, same lighting, same colours, same sheet of paper. Change only what is described below. Everything else stays exactly the same.

### T1: Tower, folding (attach T0)
The sheet of paper in front of the tower is halfway through being folded. Its front half lies flat on the tabletop, in the same spot. Its back half lifts up toward the tower at about 60 degrees, with a crisp crease across the middle and the dark grey band along its top edge.

### T2: Tower, pushed in (attach T0)
The sheet is gone from the tabletop. It has been folded into a tight, narrow accordion pleat and pushed into the tower's vertical slit. The end of the pleat still shows in the lower half of the slit, white zigzag folds with a small soft shadow. It fits the slit.

### R0: Rotunda (attach T0)
Replace the tower with a different miniature bank building, in the same matte white material, standing on the same spot, the same width from the centre line. The new building is a round rotunda with a shallow dome and a small lantern on top, a thin cornice ring under the dome, and a few shallow vertical grooves around the drum. It is shorter and wider than the tower. Its top sits a little lower and its sides reach a little wider. At street level sits one deposit slot: a round porthole framed by a thin metal ring in deep teal (hex #006D5B). Above it, a tiny white plaque with the same bank pictogram in deep teal. The sheet of paper on the tabletop stays exactly where it is, flat. The soft lavender floor pool sits around the base of the rotunda.

### R2: Rotunda, pushed in (attach R0)
The sheet is gone from the tabletop. It has been rolled into a tight paper tube, held with a narrow band of clear tape, and pushed into the round porthole. The open end of the tube faces the camera and fills the porthole. You can see the spiral of the rolled paper. It fits.

### C0: Classical bank (attach T0)
Replace the tower with a different miniature bank building, in the same matte white material, standing on the same spot. The new building is a classical bank: a triangular pediment over four columns, standing on three wide, shallow steps, with a wall set back behind the columns. It is wider than the tower, and the middle gap between the columns is wider than the others. In that middle gap, at about chest height on a person, sits one deposit slot: a wide, flat letterbox slot framed by a thin metal plate in golden yellow (hex #FFB310). Above it, a tiny white plaque with the same bank pictogram in golden yellow. The sheet of paper on the tabletop stays exactly where it is, flat. The soft lavender floor pool sits around the base of the steps.

### C2: Classical, jammed. The payoff (attach C0)
The sheet is gone from the tabletop. It has been pushed halfway into the wide golden yellow letterbox slot, and it is stuck. The sheet is clearly too wide for the slot. It buckles outward below the slot, creased and crumpled at both sides where it presses against the plate. The dark grey band shows just inside the slot. It hangs down over the front steps and casts a soft shadow. This is the only crumpled paper in the image.

---

## Photoshop prep (before AE)
1. T0: cut the sheet and its shadow out onto its own layer. Save it as `file-flat.png`. That's the one file for the whole GIF.
2. T1: cut the folding sheet the same way. Save it as `file-fold.png`.
3. T0, R0, C0: clone the sheet off the floor, so the floor is clean violet. Save them as `plate-T.png`, `plate-R.png` and `plate-C.png`.
4. T2, R2, C2: keep them whole. Save them as `in-T.png`, `in-R.png` and `in-C.png`.
5. Line them up. Overlay each plate on T0 at 50 percent, and nudge it until the base line and centre line match. Every bank has to land on the same spot.
6. Key out the violet on every layer, and keep the contact shadows and floor pool as soft alpha.

## AE assembly
Comp: 1080x1080, 12 fps, 120 frames (10 s). It loops.

Layers, bottom to top:
1. A flat #400685 solid. The ground stays locked for the whole loop.
2. The bank plates, each with its own position keyframes. Bank spacing is 760px.
3. The "in" stills: in-T, in-R and in-C, each on at its own frames, at the resting position.
4. The file layer: file-flat and file-fold, swapped on the beat. It is hidden when the file is in a slot.
5. Static on top: the lockup, the headline, the body and the CTA line, at the artboard 14 positions.

Slides: both banks move together, 8 frames each, with Easy Ease in and out. The outgoing bank goes from 0 to -760px. The incoming bank goes from +760px to 0. Motion blur on, shutter angle 90. More blur adds soft gradients that bloat the GIF.

### Timeline (12 fps)
| Frames | Time | Bank on stage | File |
|--------|------|---------------|------|
| 0 to 5 | 0.0 to 0.5 s | tower | flat |
| 6 to 11 | 0.5 to 1.0 s | tower | folding |
| 12 to 23 | 1.0 to 2.0 s | tower, in-T | in the slit. It fits. First payoff |
| 24 to 25 | 2.0 to 2.2 s | tower | pops back out, folding |
| 26 to 33 | 2.2 to 2.8 s | tower slides out, rotunda slides in | flat |
| 34 to 37 | 2.8 to 3.1 s | rotunda | flat |
| 38 to 43 | 3.2 to 3.6 s | rotunda | folding |
| 44 to 55 | 3.7 to 4.6 s | rotunda, in-R | in the porthole. It fits |
| 56 to 57 | 4.7 to 4.8 s | rotunda | pops back out, folding |
| 58 to 65 | 4.8 to 5.5 s | rotunda slides out, classical slides in | flat |
| 66 to 69 | 5.5 to 5.8 s | classical | flat |
| 70 to 75 | 5.8 to 6.3 s | classical | folding |
| 76 to 119 | 6.3 to 10.0 s | classical, in-C | jammed. Hold 3.7 s |

- Loop: hard cut from frame 119 back to frame 0. The tower is back with a fresh flat file, so the work starts over. Every bank, every week.
- Life in the hold: a 1-frame jolt on the jam at frame 76 (scale 103 percent, then back), and a 1-frame nudge at frame 96, as if someone pushed again.
- Feed timing: the first payoff lands at 1 s, so the idea reads inside the 3-second window. Two banks in 5 seconds sets up the jam.
- Thumbnail: frame 0 shows the tower and the file, a complete picture with no empty stage.

---

## GIF export

Render a PNG sequence from AE, then run these in the export folder.

Build the GIF with a shared palette. Only the changed areas are redrawn each frame:

```bash
ffmpeg -framerate 12 -i frame_%04d.png -vf "split[a][b];[a]palettegen=stats_mode=diff:max_colors=192[p];[b][p]paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle" -loop 0 bank-formats-one-bank_1080x1080.gif
```

Squeeze it, keeping the timing:

```bash
gifsicle -O3 --lossy=40 bank-formats-one-bank_1080x1080.gif -o bank-formats-one-bank_1080x1080.gif
```

The flat animatic came out at 484 KB with these settings. The slides cost the most. The whole bank moves across the frame. The 3D render will be bigger. If it goes over 5 MB, try these in order:
1. Raise `--lossy` to 60, then 80.
2. Turn motion blur off.
3. Drop `max_colors` to 128.
4. Drop to 10 fps (100 frames) and scale the timeline by 10/12.

Keep grain, noise and bloom out of the renders. Noise changes every pixel on every frame and kills GIF compression.

---

## Fixes
- T0: the tower comes out grey or plastic. Add "pure matte white model, like a high-end architecture studio presentation".
- T0: a horizon line splits the set. Add "seamless infinity curve, no horizon, no edge".
- T0: the layout ignores the reference. Start with "Match the layout of the reference image exactly", and attach nothing else.
- R0 or C0: the new building lands somewhere else or at another size. Add "standing exactly where the tower stood, its base on the same line, centred on the same point". Fix the last few pixels in step 5 of the Photoshop prep.
- R0 or C0: the sheet moves or changes. Ignore it. AE uses the sheet from T0. Only the building matters in these stills.
- T2, R2 or C2: the whole scene changes. Shorten the edit to the one sentence about the sheet, and keep "Change only what is described below" at the start.
- C2: the paper fits too cleanly. Add "it is clearly too wide, buckled and creased, stuck halfway".
- Any still: the paper looks like fabric or plastic. Add "crisp white printer paper, sharp creases, thin".
- Any still: a hand appears. Add "no hands, the paper is already in this state".
- Any still: hex codes show up as text. Delete them and keep the colour names. Correct the colours in AE.

## Brand check before export
- Ground matches #400685 in every frame. Check frames 0, 30, 60 and 119.
- All three banks rest on the same base line and centre line. Step through frames 25, 34 and 66.
- The file is pixel-identical in every flat frame.
- One bank on stage at rest. Two only during a slide.
- No green, no red, no off-palette colours.
- No readable text, logos or bank names in the image layers.
- Every slot shape reads at 400px.
- Lockup top-left and copy band match artboard 14. 65px margin on every resting frame.
- 10.0 s, 120 frames, loops forever, 5 MB or under.

## Avoid list (for models with a negative prompt field)

letters, words, numbers, signage, bank names, real bank logos, flags, people, hands, figurines, other buildings, trees, cars, streets, city, skyline, horizon line, grey models, plastic toy look, glass, glassmorphism, transparency, neon, green, red, vignette, gradient backdrop, film grain, noise, bloom, cartoon, low-poly, HDR, oversaturated, lens flare, tilt-shift blur
