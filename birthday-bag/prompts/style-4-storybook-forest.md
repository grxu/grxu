# Style 4 – Storybook forest (layered, grainy, glowing)

**Attach:**
- **P0 only:** the two photos of Hanna (face reference). They're already in Higgsfield media as `face-1.jpg` and `face-2.jpg`.
- **No style image.** The shared reference has a copyright watermark that the model would copy, and its boy with a crown is an existing anime character the model would likely redraw. The text below carries the style. After round 1, attach the approved E1 forest plate as the style reference for all other assets.

**Style block** (already included in every prompt below):
> modern storybook illustration, flat layered digital shapes with soft gradients, grainy risograph texture and fine halftone dots over everything, glowing backlight through the canopy, atmospheric depth where far layers are pale and hazy and near layers are rich and dark, palette of luminous lime and yellow-green light, emerald, teal and mint, deep blue and indigo foreground foliage, warm accents of golden yellow and rosy pink

**Why it suits the bag:** it's rich and full-bleed by nature, the dark leaves in the foreground frame the corners, and the glowing centre leaves room for the text.

---

## Round 1 – style test (Nano Banana 2.1, 2K)

### P0 · Princess character sheet (16:9)
```
Use the two reference photos of a 3-year-old girl only for the princess's likeness: round face with full cheeks, dark brown eyes, light warm skin tone, straight black hair with a side part and face-framing strands, big cheeky smile.
Character turnaround sheet of this toddler princess in a modern storybook illustration style: front view, three-quarter view, side view and back view, standing in a row, evenly spaced, full body, same size, on a plain pale mint background. Chibi proportions: big round head, simple dark eyes with a white highlight, tiny nose, the same cheeky smile, round rosy cheeks. Her hair is flat black shapes with a soft blue-grey highlight, extremely long, in one thick braid that trails past her feet and curls on the ground, with small periwinkle and white flowers along it. Small flower crown. Short lilac dress with puffed sleeves and a rosy-pink sash, barefoot. Flat layered shapes with soft gradients, a thin darker outline and a light rim along the edges, grainy risograph texture and fine halftone dots. Consistent character in every view. No text, no labels, no watermark.
```

### S1 · Giraffe test (3:4)
```
One cute giraffe in a modern storybook illustration style, full body, standing, long neck curving gently upward and leaning forward, head tilted with a friendly smile, simple dark eyes with a white highlight, round rosy cheeks, small rounded horns. Golden-yellow body with soft rounded caramel spots, built from flat layered shapes with soft gradients, a thin darker outline and a light rim along the edges, grainy risograph texture and fine halftone dots. Plain pale mint background. No text, no watermark.
```

### E1 · Forest plate (5:4)
```
A lush storybook forest in a modern illustration style, wide, seen straight on, filling the entire frame edge to edge. Tall pale-green tree trunks and rounded canopies in the background glow with soft lime and yellow light coming from behind; layered rounded bushes and big tropical leaves in emerald, teal and mint fill the middle distance; deep blue and indigo leaves, periwinkle five-petal flowers and small glowing white bulb flowers frame the bottom corners and both sides in the foreground. A pale mossy stone path winds from the bottom centre into a soft, open, sunlit clearing in the centre. The centre stays light and uncluttered: space for characters and a title. Little doodle sprouts and dots scattered in the foliage. Flat layered shapes with soft gradients, grainy risograph texture and fine halftone dots, atmospheric depth. No characters, no animals, no people, no text, no watermark.
```

---

## P0 v2 – after Grady's first pass (16:9)

Feedback on v1: too soft and too detailed, close to a children's-book painting; it needs to be more cartoon, with visible texture like the reference. The braid was far too long: hair should match Hanna's real length, just below her shoulder blades.

Changes: cartoon proportions (head about half her height, stubby limbs, mitten hands), a simpler face, hair at her real length (loose, with one thin flowered side braid as the Rapunzel nod), and the texture spelled out strongly. Attach the two photos of Hanna. If the E1 forest plate has already come out with the right grain, attach it too as a texture reference. Don't attach v1; it would pull the style back.

```
Use the two reference photos of a 3-year-old girl only for the princess's likeness: round face with full cheeks, dark brown eyes, light warm skin tone, big cheeky smile, and her hair: straight black hair with a side part and face-framing strands, falling loose to just below her shoulder blades.
Character turnaround sheet of this toddler princess as a simplified 2D cartoon character, like a frame from a modern hand-made animated series: front view, three-quarter view, side view and back view, standing in a row, evenly spaced, full body, same size, on a plain pale mint background.
Cartoon proportions: a very big round head about half her total height, a small rounded body, short stubby arms and legs, chunky mitten-like hands with simple fingers, simple rounded bare feet without toe detail. Small simple face: dark oval eyes with one white highlight, a tiny curved nose, a small cheeky smile, big round rosy-pink cheeks.
Hair: one solid black shape with a single soft blue-grey highlight band, side part, face-framing strands, loose and straight, ending just below her shoulder blades and no longer, with one thin side braid woven with tiny periwinkle and white flowers. Small flower crown.
Outfit: short lilac dress with puffed sleeves and a rosy-pink sash tied in a bow at the back.
Rendering: flat colour shapes with one soft shadow tone and a light rim along the edges, slightly uneven dark-brown outlines like a brush pen, and strong visible texture on every surface: coarse grain and noise, risograph print texture, halftone dots in the shadows. Not smooth, not clean vector, no detailed linework.
Consistent character in every view. No text, no labels, no watermark.
```

### P0 v2 results (2026-10-20)

Nano Banana 2.1, 2K, 2 variants, about 4 credits. Renders are in `../private/style-4/`.

| Variant | Job ID | Notes |
|---|---|---|
| a | `76f4406e-f527-425b-a856-b749721ead3a` | Open, cheeky grin (closest to Hanna's smile). Colourful mixed flower crown, toe lines on the feet. |
| b | `81e0a9bf-d1e1-4ce2-89e4-a6f4a0d218df` | Calm closed smile. Lilac and white crown that matches the palette, flowered braid more visible, no toes. |

Both have the right hair length and cartoon proportions. The texture is there (grain, halftone in the shadows) but softer than the reference, and the outlines are heavier than the reference's.

### P0 v3 – mix, no outlines (2026-10-20)

Pass 1: v2-b attached as the character reference, plus the two photos of Hanna, asking for a's open grin, no outlines and stronger grain. The grin and the texture came through, but the outlines did not go away: the attached v2-b sheet carried its line art along. Jobs `3d57c301-7c5b-4c60-9826-eb9df67d1b8c`, `4e620506-21d9-4301-aa2e-4d271144dc0f`.

Pass 2 (edit): `4e620506…` attached alone, with a "remove every outline, keep everything else" edit prompt. This worked: lineless, with the open grin, coarse grain and halftone dots. Jobs `ce32acab-fceb-4094-b882-b736b9fd5093` (a), `639a2891-2f77-447b-85ad-522af903e2c2` (b).

Lesson: an attached reference passes on its line style. To change how something is drawn, edit the image itself instead of re-describing it next to a reference.

```
Edit this character turnaround sheet. Remove every outline: all dark brown contour lines and line art around the face, hair, ears, arms, hands, legs, feet, dress, sleeves, sash, bow, braid and flowers must disappear completely. Where a line was, the shapes now meet directly colour against colour, separated only by a soft light rim or a slightly darker shadow tone. The facial features stay as small solid filled shapes (dark eyes with a white highlight, tiny nose, the open cheeky grin) with no outlines. Keep everything else exactly the same: the four views, proportions, the open cheeky grin, black hair ending just below the shoulder blades, the thin flowered side braid, the flower crown, the lilac dress with puffed sleeves, the rosy-pink sash and bow, all colours, the pale mint background, and the coarse grain, risograph texture and halftone dots. Lineless storybook illustration. No text, no labels, no watermark.
```

### P0 v1 lineless (2026-10-20)

Grady preferred the softer v1 look and asked for it without outlines and with more texture. I uploaded his v1 sheet (`3c6ff680-fe3a-44b8-b3fb-e5c61a754fb4`) and ran two edit passes:

| Variant | Job ID | Change |
|---|---|---|
| 1 | `5140ec88-d333-4cab-b018-43bd26551a56` | No outlines, stronger texture; long floor-length braid kept |
| 2 | `957398c0-997b-4af0-8cfe-4673e98d2f81` | The same, plus hair at Hanna's real length with a thin flowered side braid; adds soft ground shadows |

Both came out without outlines and with clear grain and halftone dots. In variant 2 the side braid is longer in the three-quarter view (down to the dress hem) than in the other views.

### P0 v4 – stylised further (2026-10-20)

Grady picked the softer v1 look, at Hanna's real hair length and without outlines, then shared two more images in the same style (an indoor window scene and a greenhouse, both watermarked "All rights reserved"). They aren't attached or stored; the prompt describes the character style instead: big round head, stubby tube limbs, wide-set dark oval eyes, tiny nose and smile, chunky hair and dress shapes with one highlight swoosh, soft light rim, fine grain.

Edit of `957398c0…` (v1 lineless, real hair length), 2 variants:

| Variant | Job ID | Notes |
|---|---|---|
| a | `5d4b23b2-0a41-4ab3-a94e-ad2ac4cdf7c8` | Flattest and simplest: solid dark oval eyes with no highlight; closest to the reference |
| b | `43dbfbd2-44e7-4135-811d-75c45343bac6` | Same, with a white highlight in each eye, so a bit more expressive |

Still open: in the three-quarter view the side braid hangs to the dress hem, longer than in the front view.

```
Edit this character turnaround sheet into a more stylised, chunkier storybook look, keeping her clearly the same girl.
Keep: no outlines anywhere (lineless); the four views (front, three-quarter, side, back); her black hair ending just below her shoulder blades with the side part and face-framing strands; the thin side braid with tiny flowers; the flower crown; the lilac puffed-sleeve dress with the rosy-pink sash and bow; the colours; the soft ground shadows; the pale mint background.
Change:
1. Proportions: an even bigger, rounder head, about half her total height; a smaller body; short rounded tube-like arms and legs; small mitten-like hands; simple rounded feet without toes.
2. Face: simplify it. Two large dark oval eyes set wide apart and fairly low on the face, each with one small white highlight, no eyelashes; a tiny dot nose; a small simple smile; soft round blush on the cheeks. Fewer details, more charm.
3. Hair and dress as big, chunky, simple shapes with one soft highlight swoosh each, fewer strands and fewer folds, with a slightly faceted, softly angular feel.
4. The side braid is the same length in every view, ending at her chest.
5. Rendering: flat shapes with gentle gradients, a soft light rim on the edges facing the light, and a fine grainy noise texture over everything, like a digital gouache print. Flowers as simple five-petal shapes.
No text, no labels, no watermark.
```

### P0 v5 – braid fix and dress decorations (2026-10-20)

Edit of v4-b (`43dbfbd2…`): make the three-quarter braid end at the chest like the front view, plus dress decorations. **The braid was not fixed:** in the front and three-quarter views it still hangs past the sash to the hip. Grady picked the collar + stars dress.

| Variant | Job ID | Decorations |
|---|---|---|
| Flowers | `c35e1824-1630-4486-9707-11e5c5833617` | Periwinkle and cream flowers scattered on the skirt, plus a tiny-flower border along the hem |
| Collar + stars | `9f8a08aa-ed4a-443e-8045-b06999f7e272` | White scalloped collar, flower vine along the hem, tiny gold star dots |

Other decoration ideas offered and not yet rendered: a tiny parade of the four key animals embroidered on the hem; lace trim with ribbon bows and bodice lacing.

### P0 v6 – braid length fix (2026-10-20, confirmed by Grady first)

Edit of the collar + stars sheet (`9f8a08aa…`), 1 variant, about 2 credits: job `33917ea5-10cb-4f32-bd7e-9e712303cd4b`. The braid is shorter than before (it used to reach the hip). The tie now sits on the sash and the tip ends just below it, at the top of the skirt, so it's not fully above the sash as asked. Everything else is unchanged.

### P0 v7 – side and back views, masked inpaint (2026-10-20, confirmed)

What Grady actually meant by "braid not fixed": the braid shows in the front and three-quarter views but is missing in the side and back views. The three earlier passes wrongly shortened it.

Inpaint on v6 (`33917ea5…`) with a mask over the right half only (side and back views; mask media `5a18b755-6df4-42b0-acbc-1453c741402b`), 2 variants, about 4 credits:

| Variant | Job ID | Side view | Back view |
|---|---|---|---|
| a | `65d6b0ff-e9e5-4815-9208-386a1cf73b99` | Braid now visible over her shoulder, a clean single braid | Still no braid |
| b | `222da559-f4f5-4724-ab2b-e558ba09f14b` | Braid visible, but it looks doubled and messy | Still no braid |

She still faces left in the side view; the model ignored "turn her to face the right". The left half (front and three-quarter views) is not pixel-identical: about 3% RMSE difference, slightly crisper and more saturated, with the same design.

### P0 v8 – back view braid, masked inpaint (2026-10-20, confirmed)

Inpaint on v7-a (`65d6b0ff…`) with a back-view-only mask (`f860cda6-18f5-497b-81af-7a60a83e6122`), 1 variant, about 2 credits: job `ee463c5a-fbde-4dc7-9805-37aaa37b0012`. The braid now shows in all four views. But in the back view it's on the viewer's **left**, which is her left side: mirrored compared with the front view, where it's on her right. Each edit pass also adds a bit of re-encoding wear: a faint light halo around the figures and slightly crunchier texture than v6.
