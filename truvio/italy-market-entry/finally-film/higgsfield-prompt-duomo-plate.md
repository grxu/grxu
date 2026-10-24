# Higgsfield prompt: Duomo plate

The destination plate for the "Siamo finalmente in Italia" film, one LinkedIn organic video at 1080x1350. It replaces the Flipkart storefront from the reference. The plate sits at the top of panel 4 (x 65 to 1015, y 120 to 715, 950 x 595) on the white page. The E-road runs under it, and the flat Yellow Gold car parks at the road end below its left half. Higgsfield makes the hero only: a soft 3D miniature of the Duomo di Milano facade on white. Grady sets everything else by hand in After Effects: the headline, the E-road, "in Italia", the car and the logo.

## Copy (final, for reference only)
- On design: Siamo / FINALMENTEEEE ... in Italia
- The plate carries no words.

## How the image matches the copy
- "in Italia": the Duomo says Italy at a glance, and Milan is the country's business and finance capital. That suits a B2B finance audience better than a tourist landmark.
- "FINALMENTE": the car arrives at a real place. The plate is the payoff the whole road drives toward.
- The gilded statue on the top spire (the Madonnina) is the plate's one warm accent. It echoes the Yellow Gold car and the gold end of the road.
- The plate stays brand-free. The logo and "in Italia" carry Truvio.

## Decisions (24 Oct 2026)
- Landmark: Duomo di Milano.
- Style: soft 3D miniature, a tabletop model in pale marble under soft studio light. It sits between the flat car and a photo, and it reads well small.
- View: straight-on facade, square to camera, like the reference storefront.
- Ground: pure white (#FFFFFF), the same as the page, so the cutout drops in with its own soft shadow.
- No text, no logos and no brand colours in the generated image. The road brings the colour.

## Settings
- Model: Nano Banana Pro. It handles architecture, materials and clean grounds better than Soul, which is built for people.
- Aspect ratio: 3:2, then crop to the plate's 16:10 (950 x 595) by trimming top and bottom. Use 16:9 as the fallback and trim the sides.
- Resolution 2K, batch 4.
- Reference image: none. Nano Banana knows the Duomo. Don't attach the animatic frame, since its placeholder text would turn up in the render. Attach a facade photo only if Grady holds the rights to it.

## Prompt A: white marble miniature (recommended)
Premium studio product photo of a detailed tabletop miniature model of the Duomo di Milano cathedral facade, shot straight-on at eye level with a long lens, so the front of the cathedral is square to the camera and perfectly symmetrical. The model is carved from pale, slightly warm white marble with a soft satin finish, with crisp Gothic detail: the five bronze-toned doors at the base, the tall pointed windows, the rows of slender spires along the roofline and the main spire rising behind the centre. A small gilded statue in warm, polished gold stands on the tip of the tallest spire, the only warm colour in the image. The model stands on a pure white seamless studio ground that is flat and evenly lit from edge to edge, with no gradient, no vignette and no texture. Soft, diffused key light comes from the upper left, with gentle fill from the right, and the model casts one short, soft contact shadow straight down onto the white ground. True-to-life colour, sharp focus across the whole facade, high-end editorial still life. The image contains no readable words, no letters, no numbers and no signage. No logos, no people, no birds, no sky, no piazza, no street, no other buildings, no props, nothing else in the frame. The whole cathedral sits inside the frame, centred, filling about 80 percent of the frame width, with even white margins on every side, and the base of the model sits at about 85 percent of the frame height.

## Prompt B: miniature on a violet plinth
How it matches the copy: a slim Deep Violet base ties the plate to the road and the headline colour, at the cost of a more "product on display" look.

Use Prompt A, and replace the contact-shadow sentence with: "The model stands on a slim, low rectangular plinth in matte deep violet (hex #400685), slightly wider than the facade, and the plinth casts one short, soft contact shadow onto the white ground." If the hex shows up as text in the render, drop it and correct the plinth colour in Photoshop.

## After the render
1. Cut out the model in Photoshop, or use Higgsfield's remove background. Keep the contact shadow on its own layer at Multiply, so it sits on the white page.
2. Scale the cutout to fit 950 x 595, bottom-aligned at y 715 in panel 4. The base should sit about 150px above the road.
3. Check that the left half of the facade sits over the road end at x 400 and the parked car, as the storefront does in the reference.

## Brand check before you comp
- Ground: sample it. It should read #FFFFFF. If it reads grey or warm, lift it with Levels on a mask, or cut the model out and drop the ground.
- Gold statue: warm gold, not orange or brassy green. Nudge it toward Yellow Gold (#FFB310) with a masked Hue/Saturation adjustment if needed.
- Architecture: symmetrical, with no melted or duplicated spires and no doors out of line.
- No readable words, no gibberish carved on the facade, no logos.
- The cutout sits inside the 65px safe margin in panel 4.

## Avoid list
Nano Banana has no negative prompt field. The exclusions are inside the prompt. For a model with a field, use: text, letters, signage, logo, watermark, people, tourists, pigeons, sky, clouds, piazza, street, cars, other buildings, gradient background, vignette, coloured background, tilted perspective, fisheye, melted spires, asymmetry.

## Fixes if a batch misses
- Perspective tilts or the facade turns: add "camera exactly level with the centre of the facade, no perspective tilt, front face parallel to the image plane".
- Spires melt or multiply: add "clean, evenly spaced spires, architecturally accurate, crisp edges" near the start.
- It looks like the real cathedral in a city: move "a tabletop miniature model on a white studio ground" to the very start, and repeat "no sky, no piazza".
- Ground goes grey or shows a gradient: add "pure white seamless ground, perfectly flat and even from edge to edge".
- The statue comes out brassy, or missing: add "a small gilded statue in bright, warm polished gold on the very tip of the tallest central spire".
- Cropped at the edges: add "the whole cathedral sits inside the frame with wide white margins".
- Looks plasticky: add "real carved marble with soft satin sheen and subtle stone grain".
