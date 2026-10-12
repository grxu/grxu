# Higgsfield prompt: crammed note

Truvio PIM LinkedIn single-image ad, 1:1 (1080x1080) only. A phone lies on Deep Violet with an Apple Notes style note on screen. The note is a tired product data specialist's list of everything stuffed into the BC item card. Below the phone sit a Truvio line, the lockup and the CTA. The LinkedIn headline and body sit outside the image. Higgsfield makes the ground and the phone with a blank white screen. Grady comps the note screen from `crammed-note-screen.ai` (or the SVG or 4x PNG), then the line, the lockup and the CTA.

## Launch blocker
- The PIM landing page is still in progress. Until it ships, this ad links to https://truvio.com/products/business-central/pim.
- The messy item card ad in this campaign links to a different fallback, https://truvio.com/products/commerce/product-information-management. Pick one page for both ads before they go live. Neither URL could be checked from the cloud session.

## Copy (final, for reference only)
- On design, note title: Things we crammed into our BC item cards
- On design, note list: 47 custom fields / Marketing texts in 6 languages / Image links nobody updates / Spec sheets as attachments
- On design, below the phone: There's a better place for it. Truvio PIM, inside Business Central.
- On design, bottom: See it in a demo →
- On design, new: 23:47 in the status bar. Added on 12 Oct 2026, needs copy sign-off.
- Ads headline: See Truvio PIM running inside your BC
- Ads body: Truvio PIM takes attributes, assets and translations off your BC item card. AppSource install, guided setup, no code. See it in a demo.
- Link: PIM landing page (WIP), see the blocker above.

## How the image matches the copy
- "Things we crammed into our BC item cards": the note is the hook. A personal phone note, not a vendor slide, so it reads as something the viewer could have written.
- "a tired product data specialist": 23:47 in the status bar. Still listing item card problems near midnight.
- "47 custom fields": the attributes in the ads body.
- "Marketing texts in 6 languages": the translations.
- "Image links nobody updates" and "Spec sheets as attachments": the assets.
- "There's a better place for it.": the line sits directly under the phone, so the eye goes from the list to the answer.
- "Truvio PIM, inside Business Central.": set in Yellow Gold, it picks up the Notes yellow on the screen and ties the fix to the problem.
- The image shows the problem. The line, the lockup and the ads copy bring the fix.

## Decisions (12 Oct 2026)
- Higgsfield makes the phone on violet with a blank white screen. The note is comped from the mock, so every word is exact and the type size is under Grady's control.
- Notes yellow: Apple's kept. Off palette, approved for the screen only. The mock uses #E3A600 as a stand-in. Sample a real Notes screenshot and replace it before publishing.
- New words: 23:47 in the status bar only. The back chevron, share, more and toolbar items are icons with no labels. No date line under the nav bar.
- Size: 1:1 only, same as the messy item card ad.
- Note type: Be Vietnam Pro, not SF Pro. Apple licenses SF Pro for mock-ups of apps on its own platforms, and an ad falls outside that.
- Note size: body text runs at about 1.8 times real iOS size, like the Larger Text setting. At true size the list would not read in the feed.
- List style: bullets. Non-breaking spaces steer the wraps so "nobody updates", "6 languages" and "as attachments" stay together. The words are unchanged.
- Line colours: "There's a better place for it." in off-white #E6E8FC, "Truvio PIM, inside Business Central." in Yellow Gold #FFB310. Swap the second line to off-white if two yellows feel like too much.
- Recommended: Prompt A. B's tilt adds a casual feel but shrinks the note by 5 percent.

## Direction
- Ground: Deep Violet (hex #400685), flat, matte paper.
- Hero: a modern smartphone, face up, dark graphite metal rim, thin black bezel, blank white screen. Generic. No Apple logo or name anywhere.
- Shadow: soft and short, down and to the right, from daylight at the upper left.
- Layout (mock A): phone centred, x 364 to 716, y 65 to 785. Line centred, Museo Slab 700 at 36px with 42px leading, top at y 832. Lockup bottom left at 176px wide. CTA bottom right, Be Vietnam Pro ExtraBold 24px in #E6E8FC with the drawn arrow.

## Settings
- Model: Nano Banana Pro. It holds clean product geometry and a flat ground. Soul is for candid people shots.
- Aspect ratio: 1:1, run on its own.
- Resolution 2K, batch 4.
- Reference image: `mocks/crammed-note-a-plate-ref.png` for A, `mocks/crammed-note-b-plate-ref.png` for B. These flat mocks show the phone with a blank screen and no copy, so they lock the composition. Never attach the full mock with the note on it (the model will try to draw the text). Never attach an earlier render or the logo.

## Prompt A: straight flat lay (recommended)
### 1:1
Premium editorial still-life photo, shot from exactly overhead with the camera parallel to the surface. A smooth matte deep violet (hex #400685) paper surface fills the whole frame, flat and evenly lit from edge to edge, with no gradient, no vignette and no texture. A modern smartphone lies face up on it, perfectly straight, its long side vertical and its four edges parallel to the frame edges. It has a thin dark graphite metal rim with softly rounded corners and a thin, even black bezel around the display. The phone is switched on and its screen shows a solid, flat, pure white display from edge to edge, with no status bar, no icons, no notch, no camera cutout, no reflections and no glare. Soft directional daylight from the upper left puts a fine highlight along the top and left edges of the rim and casts a soft, short shadow down and to the right on the violet surface. Crisp focus across the whole phone, real brushed metal, true-to-life colour. There are no readable words, letters or numbers anywhere in the image. No logos, no brand marks, no hands, no props, no cables, nothing else in the frame. The phone is centred horizontally and measures about 33 percent of the frame width and two thirds of the frame height. Its top edge sits about 6 percent below the top of the frame. The bottom 27 percent of the frame is empty violet, reserved for text, and wide empty violet margins run down the left and right sides.

## Prompt B: tilted flat lay
How it matches the copy: the phone looks dropped on the desk at the end of a long day, which backs up 23:47. The note comes out 5 percent smaller than in A, and the screen comp needs a 5 degree turn.

Premium editorial still-life photo, shot from exactly overhead with the camera parallel to the surface. A smooth matte deep violet (hex #400685) paper surface fills the whole frame, flat and evenly lit from edge to edge, with no gradient, no vignette and no texture. A modern smartphone lies face up on it, turned about 5 degrees counterclockwise so its top leans slightly to the left. It has a thin dark graphite metal rim with softly rounded corners and a thin, even black bezel around the display. The phone is switched on and its screen shows a solid, flat, pure white display from edge to edge, with no status bar, no icons, no notch, no camera cutout, no reflections and no glare. Soft directional daylight from the upper left puts a fine highlight along the top and left edges of the rim and casts a soft, short shadow down and to the right on the violet surface. Crisp focus across the whole phone, real brushed metal, true-to-life colour. There are no readable words, letters or numbers anywhere in the image. No logos, no brand marks, no hands, no props, no cables, nothing else in the frame. The phone sits in the horizontal centre of the frame and measures about 31 percent of the frame width and 63 percent of the frame height. Its highest corner sits about 6 percent below the top of the frame. The bottom 28 percent of the frame is empty violet, reserved for text, and wide empty violet margins run down the left and right sides.

## Comp the note screen
1. Pick the frame with the cleanest white screen and the straightest rim.
2. Magic Wand the white screen (contiguous, tolerance about 10) and save the selection.
3. Place `crammed-note-screen.ai` as a vector smart object. The 4x PNG works too. Scale it to the screen width. For B, rotate it -5 degrees to match.
4. Load the saved selection as a layer mask on the screen, so its corners follow the phone in the plate.
5. The screen file is 328x696. If the generated screen is taller or shorter, open the smart object and move the Toolbar and Home_indicator groups to the new bottom. Don't stretch the type.
6. Optional: a white-to-clear gradient at 3 to 5 percent on Screen across the top left, so the flat UI sits behind glass.
7. Set the line, lockup and CTA at the positions in Direction.

Screen type, for reference: title Be Vietnam Pro ExtraBold 31/36, list Regular 26/34, time ExtraBold 20, all black. Icons in the Notes yellow stand-in #E3A600. Named layers: Status_bar, Camera_island, Nav_bar, Note_title, Note_item_1 to 4, Toolbar, Home_indicator.

## Brand check before you comp
- Ground reads #400685 at three points clear of the phone and its shadow. Correct with masked Curves or Hue/Saturation, which keeps the shadow.
- Rim reads dark graphite. No gold, silver or coloured phone.
- No Apple logo or Apple name anywhere. No generated text or gibberish on the screen or the ground.
- Notes yellow: replace the #E3A600 stand-in with a value sampled from a real Notes screenshot. Screen only.
- Line: #E6E8FC and Yellow Gold #FFB310. CTA #E6E8FC.
- Museo Slab in the line, swapped in for the mock's Arvo Bold.
- 23:47 has copy sign-off.
- 65px safe margin: nothing light inside it. The phone's top edge sits exactly on it in A.

## Avoid list
For a model with a negative prompt field: text, letters, numbers, words, watermark, logo, Apple logo, brand mark, notch, camera cutout, status bar, app icons, user interface, screen reflection, glare, screen glow, hands, fingers, props, coffee cup, desk, keyboard, cable, gradient background, vignette, textured surface, wood, 3D render, illustration, cartoon, perspective tilt, cropped phone. Nano Banana Pro and Soul have no negative prompt field, so the exclusions sit inside the prompt.

## Fixes if a batch misses
- UI, icons or text appear on the screen: move "its screen shows a solid, flat, pure white display" to the start, after the shot type, and add "the screen is completely blank".
- A notch or camera cutout appears: keep the frame. Hide the Camera_island layer in the screen file and line the comp up with the plate's own cutout, or paint the cutout white first.
- Glare, reflections or a glow on the screen: add "matte screen, evenly lit pure white, no reflections, no glare, no glow".
- The phone comes out in perspective or at an angle (A): add "the phone's four edges run straight and parallel to the frame edges, seen from exactly above".
- The phone comes out too big or cropped: add "the whole phone sits inside the frame with wide violet margins, about a third of the frame width".
- The phone comes out silver, gold or coloured: add "dark graphite metal rim, almost black".
- It looks like a cheap stock mockup: add "high-end editorial still life, real brushed metal, soft directional daylight".
- Vignette or gradient on the ground: add "perfectly flat, even violet ground from edge to edge".
- Hex codes appear as text: delete the hex, keep "deep violet", and correct the colour in Photoshop.
- Hard or long shadow: change to "a soft, short contact shadow".

## Files
- `mocks/crammed-note-a-1x1.png`: mock of the finished ad, Prompt A. `@2x` at 2160x2160.
- `mocks/crammed-note-b-1x1.png`: the same with the tilted phone, Prompt B.
- `mocks/crammed-note-a-plate-ref.png`, `mocks/crammed-note-b-plate-ref.png`: Higgsfield layout references. Blank screen, no copy.
- `crammed-note-screen.ai`: the note screen as a PDF-based Illustrator file, live text, vector icons. Text uses the kit's Be Vietnam Pro.
- `crammed-note-screen.svg`: the same, editable master with named layers.
- `crammed-note-screen@4x.png`: the same at 1312x2784 with transparent corners.
- `source/`: the HTML mocks. `note.css` and `note.js` build the screen for all of them. Render with `.claude/skills/truvio-higgsfield-ad/scripts/render_mock.sh source/crammed-note-a.html mocks/crammed-note-a-1x1 1080x1080`. Export the screen with `.claude/skills/truvio-higgsfield-ad/scripts/export_svg.py source/note-screen.html crammed-note-screen 328x696`.
- Neither the .svg nor the .ai carries Illustrator's private editing data. Open one, then Save As .ai once to get a native file.

## QA
- Viewport matches the canvas: 1080x1080 for both mocks.
- Light ink inside the 65px safe margin: 0 in all four renders.
- Ground #400685 at all three sample points in all four renders.
- Yellow Gold in the line samples #FFB310 exactly.
- Fonts loaded: Arvo Bold, Be Vietnam Pro Regular and ExtraBold.
- Mock A gaps: phone to line 47px, line to lockup row 41px.
- Note fits the screen: the last list line ends at y 500 of 696, the toolbar starts at y 630.
- Screen SVG rendered back against the HTML: 0.07 percent of pixels off by more than 60, all on antialiased edges.
- Feed size: on a 520px contact sheet the list text renders at about 12.5px and reads.
