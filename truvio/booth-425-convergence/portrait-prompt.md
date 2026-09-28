# Booth 425 convergence, portrait prompt (v5 draft)

Adapted from Higgsfield generation `44848270-2ebb-4b41-9434-a1ea2acc4ad7` (Seedance 2.5, 21:9, 18 s, 20 Aug 2026). Matches storyboard v5. Do not render until the storyboard is locked.

## Settings

| Setting | Value |
|---|---|
| Model | Seedance 2.5 |
| Mode | `omni_reference` |
| Aspect ratio | 9:16, cropped to 780 × 1520 in After Effects |
| Duration | 20 s render, trimmed to 19.5 s in the edit |
| Frame rate | 30 fps final. Conform in After Effects (the sample rendered at 24 fps) |
| Resolution | 480p draft first, then finalise the same draft at 1080p |
| Audio | Off |
| Bitrate | High |
| Video reference | `<<<video_1>>>` the white sample (motion, pacing, lighting) |
| Image references | `<<<image_1>>>` SignUp, `<<<image_2>>>` Axtension, `<<<image_3>>>` SKsoft, `<<<image_4>>>` DynamicWeb, all white PNG |

## Timeline

| Time | Frames at 30 fps | Panel | Beat | Type set in After Effects |
|---|---|---|---|---|
| 0.0–1.0 s | 0–30 | 1 | Plates drift in | Your Trusted Brands |
| 1.0–5.0 s | 30–150 | 1 | Plates orbit a tall tilted oval | Your Trusted Brands |
| 5.0–5.4 s | 150–162 | 1 | Orbit collapses into a vortex | none |
| 5.4–6.0 s | 162–180 | Flare | White-hot flare | none |
| 6.0–7.5 s | 180–225 | 2 | Spectrum rings expand | Are now |
| 7.5–10.5 s | 225–315 | 3 | Rings settle into a halo | Truvio logo |
| 10.5–15.5 s | 315–465 | 3 | Spectrum rule draws in | Finance, Operations, Commerce, Intelligence |
| 15.5–19.5 s | 465–585 | 4 | Gradient pill, light sweep, halo fades out by 17.5 s, hold, dissolve from 19.0 s | See if Truvio is right for you. Booth 425 |

## Prompt

```
"Premium enterprise motion-graphics sequence, portrait 9:16, 20 seconds, no camera shake, elegant and restrained. Follow the motion, pacing and lighting of <<<video_1>>>, restaged for a tall portrait frame.

Background: a soft matte gradient field. Pure white at the centre, easing through off-white to pale lavender #E6E8FC at the edges.

0-5s: Four small dark glass plates orbit slowly around the centre on a tall tilted elliptical path in gentle 3D perspective. They grow larger and sharper as they swing toward the viewer, and smaller, paler and softly blurred as they pass behind. Each plate carries one white logo, reproduced exactly and never redrawn: <<<image_1>>>, <<<image_2>>>, <<<image_3>>>, <<<image_4>>>. Each plate casts a soft coloured glow beneath it, in the same order as the logos: orange #EB8A23, magenta #E03170, red #F12425 and blue #003CFF. The centre of the frame stays empty. Everything drifts slowly.

5-6s: The orbit collapses inward. The four plates accelerate toward the centre with long directional motion-blur smears in their glow colours and braid into a single point of white-hot light. The light blooms outward with a thin horizontal streak.

6-7.5s: Concentric rings in a deep violet, blue, green and gold spectrum expand from the bloom and soften. The centre stays clear and calm.

7.5-10.5s: The rings settle into one faint, soft spectrum halo behind the centre. Total stillness.

10.5-15.5s: The halo slowly widens until it frames the upper two thirds of the frame with a clear margin, then drifts gently. A thin spectrum rule in deep violet, blue, green and gold draws from left to right in the lower middle of the frame.

15.5-20s: The rule fades. A rounded white pill outlined in a deep violet, blue, green and gold gradient settles into the lower middle, and a single bright sweep of light runs through its outline. At 16.5 seconds the halo begins to fade and is fully gone by 17.5 seconds, leaving only the clean gradient field and the pill. The frame holds perfectly still to the end.

Style: high-end broadcast motion design, soft volumetric light, generous negative space, matte background, no people, no photography, no clutter, smooth cross-dissolves, nothing snaps or cuts. No text, letters or numbers anywhere in the frame. The four logos on the plates are the only graphics with lettering.
```

## Shot A render setup (keyframe method)

Replaces the single 20 s shot above, which drifted with the sample as a video reference.

| Input | Role | Higgsfield media ID |
|---|---|---|
| `keyframes/key-start.png` (plates level) | start_image | `a2eeb4a0-591f-49ba-a622-7d51b475b6bf` |
| `keyframes/key-flare.png` | end_image | `c2d679a5-b720-41a2-812d-94633426a183` |
| `keyframes/plate-signup.png` | image reference | `382abe91-2eee-4e92-b573-4c2cc39cec87` |
| `keyframes/plate-axtension.png` | image reference | `04a6697e-1986-45b7-8464-9b8cccda7081` |
| `keyframes/plate-sksoft.png` | image reference | `87a3eb52-7e13-4549-905a-e60cc0f8ebb6` |
| `keyframes/plate-dynamicweb.png` | image reference | `9b5d9bf1-776e-4f95-9154-5bada9da003b` |

Settings: Seedance 2.5, omni_reference, 9:16, 6 s, audio off, high bitrate. 480p draft cost 18 credits. First draft: job `7b2cd519-c064-4745-8518-308a097611f7`.

### Shot A draft 3 prompt (fixes SignUp popping toward camera and mirrored logos)

Start keyframe updated: front plates at 80%, back plates at 70% (was 100% and 60%).

```
Premium enterprise motion-graphics shot, portrait 9:16, 6 seconds, locked-off camera, no camera shake, elegant and restrained. The first frame is the start image and the last frame is the end image.

Background stays the same soft matte gradient field for the whole shot: pure white at the centre easing to pale lavender #E6E8FC at the edges. The scene stays bright and light the entire time. Never dark.

0-4.8s: The four dark glass plates from the start image travel together, at an even, slow speed, clockwise around the empty centre on one tall tilted elliptical ring, completing about half a turn. Every plate stays on that ring at a constant distance from the centre. No plate ever leaves the ring, moves toward the camera or passes in front of the others. Depth stays subtle: a plate at the front of the ring is at most slightly larger than one at the back, and no plate ever grows wider than about a third of the frame. The plates stay level, upright and facing the viewer the whole time. They never tilt, turn or flip, so every logo always reads the right way round. Each plate keeps its exact logo from the reference images, crisp and unchanged: <<<image_1>>> SignUp, <<<image_2>>> Axtension, <<<image_3>>> SKsoft, <<<image_4>>> DynamicWeb. Each plate keeps its soft coloured glow beneath it: orange, magenta, red and blue. The centre of the frame stays empty.

4.8-5.4s: The ring speeds up and tightens inward. The plates stay facing the viewer as they spiral toward the centre with directional motion-blur smears in their glow colours. Logos never mirror or flip. The vortex stays compact, no wider than about half the frame width, centred.

5.4-6s: The smears meet in a single white-hot point of light that blooms outward with a soft lavender glow and a thin horizontal streak, matching the end image.

Style: high-end broadcast motion design, soft volumetric light, generous negative space, no people, no clutter, smooth motion, nothing snaps or cuts. No text, letters or numbers anywhere except the four logos on the plates.
```

Shot A draft 3 approved: job `ad08da37-9a40-46b7-801b-f94e2b3f1edf` (start keyframe `33ff076b-c114-4133-8ddb-b0e0ae51c66e`).

## Shot B plate (6 to 20 s, textless)

| Input | Role | Higgsfield media ID |
|---|---|---|
| `keyframes/key-flare.png` | start_image (matches Shot A's last frame) | `c2d679a5-b720-41a2-812d-94633426a183` |
| `keyframes/key-end.png` | end_image | `16db74b7-a430-4a9c-a4e4-8cffef5cad18` |

Settings: Seedance 2.5, omni_reference, 9:16, 14 s, 480p draft, audio off, high bitrate, 42 credits. First draft: job `68357b25-fe21-4de3-82f5-23e1d2cd0ae5`.

Local timing (add 6 s for the edit): rings 0 to 1.5 s, halo 1.5 to 4.5 s, halo widens and rule draws 4.5 to 9.5 s, rule fades and pill settles with light sweep from 9.5 s, halo fades 10.5 to 11.5 s, hold to 14 s. No text or logos. Spectrum only: deep violet, blue, green, gold.
