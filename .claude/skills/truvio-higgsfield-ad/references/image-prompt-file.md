# Image prompt file: structure

This is the house format Grady has used across the Production Planning and F&O Compliance campaigns. Keep the section order, and drop a section only if it really doesn't apply.

```markdown
# Higgsfield prompt: <ad name>

<One paragraph: ad formula, campaign, placement (LinkedIn single image), sizes,
what sits outside the image (LinkedIn headline and body), what Grady comps
(on-design copy, lockup), and what Higgsfield makes (ground + hero, or hero only).>

## Launch blocker            <- only if one exists (landing page, unconfirmed date)

## Copy (final, for reference only)
- On design: ...
- Ads headline: ...
- Ads body: ...
- CTA: <url>

## How the image matches the copy
- "<copy line>": <what in the image shows it>
- ... one bullet per line that matters. End with what the image leaves to the copy
  (usually the fix: "the image shows the problem, the copy and lockup bring the fix").

## Direction                  <- or "Decisions (<date>)" when Grady chose between options
- Background, hero, stamp/accent colours with names + hex, headline font and colour,
  lockup position. Note any swap from the brief and why (e.g. peach -> Prometheus Red).

## Settings
- Model, and one line on why
- Aspect ratio per size, run separately, plus the 3:4 fallback
- Resolution 2K, batch 4
- Reference image: none / the flat layout mock (never an earlier render, never the logo)

## Prompt A: <name> (recommended)
### 1:1
<one paragraph>
### 4:5
Same prompt. Replace the last N sentences with: <layout sentences for 4:5>

## Prompt B: <name>
How it matches the copy: <one or two lines on what B adds>
<one paragraph>

## Clean plate option         <- when a stamp, badge or word needs an exact hex or spelling
How to generate without it, and how to add it in Illustrator or Photoshop.

## Brand check before you comp
- Ground hex, sampled. How to correct it (masked Hue/Saturation or Curves keeps the shadows).
- Accent hex.
- Every readable word spelled right.
- No gibberish, no logos.
- Copy zones clear. 65px safe margin in both sizes.

## Avoid list
<comma list for models with a negative prompt field. Say Nano Banana and Soul have none.>

## Fixes if a batch misses
- <symptom>: <exact words to add or change>
```

## Writing the prompt paragraph

Order that works:
1. Shot type and camera: "Premium editorial still-life photo, shot from directly above."
2. Ground: material, colour with hex, "flat and evenly lit from edge to edge, with no gradient, no vignette and no texture".
3. Hero: what it is, its size relative to the frame, angle, shadow.
4. Detail inside the hero: layout, placeholder bars, the few readable words.
5. Accent (stamp, sticker, tag): word, typeface style, border, ink colour with hex, angle and direction, position, texture.
6. Material and light: paper grain, focus, light direction, "true-to-life colour".
7. Text control: "The only readable words in the image are ..."
8. Exclusions: "No logos, no other text, no hands, no props, nothing else in the frame."
9. Layout: hero position and size in percentages, plus the empty zones for copy and lockup.

Keep the layout sentences last, so the 4:5 version only swaps the tail.

## Fixes list: the ones that keep coming back
- Hex codes appear as text: delete the hex, keep the colour name, correct it in Photoshop.
- A word is misspelled: spell it letter by letter in the prompt ("spelled R-E-J-E-C-T-E-D"), then regenerate rather than fix by hand.
- Gibberish on documents: move "no readable words or numbers, grey placeholder bars only" to the start.
- Looks like a cheap stock mockup: add "high-end editorial still life, real paper, soft directional daylight".
- Vignette or gradient on the ground: add "perfectly flat, even violet ground from edge to edge".
- Hero cropped or too big: add "the whole <hero> sits inside the frame with wide violet margins".
- Props appear: repeat "nothing else in the frame" at the start.
