# Higgsfield prompt: Truvio Connect 2026, Postcard Motion

The Postcards direction, restyled after Grady's motion reference (an illustrated travel-poster card per city, the card and city name swap from one city to the next). The full sequence runs London, Copenhagen, Eindhoven, Stockholm. This file covers London only, image plates only. Grady rebuilds the final art in Illustrator from these plates and the layout file in `source/`.

## Decisions (26 Oct 2026)
- Format 4:5 (1080x1350). The top 33% (446 px) is a brand gradient for the event name and details. The card sits below it.
- City name: live Museo Slab with an outline stroke, set in Illustrator. Never generated.
- Palette: the Truvio palette only (primary, secondary, accent, neutral). One lead colour per city: London green, Copenhagen blue, Eindhoven gold, Stockholm violet.
- Higgsfield makes one full scene, then four layer plates cut from it (sky and sun, skyline, Tower Bridge, foreground) so each maps to an Illustrator and animation layer.
- No people. The reference has none, and they wouldn't read at this scale.

## Reference read (`ref.mp4`, 720x1280, 10.9 s)
- Flat editorial vector illustration with grain: soft gradient fills, stipple and noise shading, rough card edges.
- One dominant hue family per city (indigo for Zurich), one warm accent (orange), a sun disc.
- Scene in layers: sky and sun, distant skyline, hero building, water and foreground plants.
- City name in a thin outlined condensed sans over the sky, a small italic "from" or "to" above it.
- The transition wipes the old card out and builds the new one in layers, with the background gradient changing hue.

## London palette (green lead)
| Role | Colour |
|---|---|
| Dominant dark | Teal Meridian #006D5B |
| Dominant mid | Electric Green #2DB34A |
| Highlights, water glints | Luminous Aqua #66FFCC |
| River depth | Atlas Blue #00476D |
| Sun, lit windows | Yellow Gold #FFB310 |
| Warm accent (bus, boat stripe) | Prometheus Red #F76336 |
| Paper whites | White #FFFFFF |

## Settings
- Nano Banana Pro, 2K, batch of 1.
- Full plate at 1:1. The card is 950x839, so Grady crops about 6% off the top and bottom.
- Layer plates: the full plate as the only reference, each on flat magenta #FF00FF for clean masking. Magenta is in no city palette.

## Prompt 1: London full plate (1:1)

```text
Flat editorial travel-poster illustration of London, a modern hand-made vector illustration with risograph-style grain: flat shapes with soft gradient fills, fine stippled grain and noise texture for shading, slightly rough hand-drawn edges, simplified architecture with small lit windows. Seen straight on and layered in depth like a stage set. Back layer: a smooth sky, deep Teal Meridian (hex #006D5B) at the top fading to pale mint near the horizon, with a large soft Yellow Gold (hex #FFB310) sun disc in the upper right. Middle layer: the London skyline in cool teal and green tones: The Shard, a slim tapered glass pyramid and the tallest shape; the Gherkin, a rounded bullet-shaped tower with a diagonal grid; the Walkie-Talkie, a tower that widens toward its top; and the Tower of London's square White Tower with four corner turrets. Hero layer: Tower Bridge across the centre, built correctly: exactly two Gothic towers with pointed roofs and small corner turrets, the high walkway between them, the bascule road deck and suspension chains sweeping down to both banks, in Electric Green (hex #2DB34A) and pale mint stone, with Yellow Gold lit windows. Front layer: the Thames in Atlas Blue (hex #00476D) with Luminous Aqua (hex #66FFCC) ripple lines and soft reflections of the bridge, a long river boat with a Prometheus Red (hex #F76336) stripe, a red double-decker bus on the embankment at the left, two tall rounded plane trees in dark teal at the right edge and low shrubs at the left edge. Use only these colours: Teal Meridian, Electric Green, Luminous Aqua, Atlas Blue, Yellow Gold, Prometheus Red and white. Green and teal are the dominant hue family, gold and red are small warm accents. No text, no letters, no numbers, no signs, no logos, no flags, no people, no border, no frame. Full-bleed scene filling the whole frame edge to edge. The river line sits at 72 percent of the frame height. The tops of the Tower Bridge towers reach 36 percent from the top. The tip of The Shard reaches no higher than 26 percent from the top. The top 24 percent of the frame is plain sky with the sun, kept clear for a large outlined city name.
```

## Prompts 2 to 5: layer plates (1:1, full plate as reference)
Each opens with: "Edit the reference image. Keep exactly the same drawing style, grain, colours, position and scale." Then:

- **L1 Sky:** "Keep only the sky gradient and the sun disc. Remove every building, the bridge, the river, the boat, the bus and all trees, and continue the sky smoothly where they were, down to the bottom of the frame. No text, nothing else."
- **L2 Skyline:** "Keep only the background skyline: The Shard, the Gherkin, the Walkie-Talkie, the Tower of London and the distant buildings behind Tower Bridge. Complete any part that Tower Bridge hid. Replace the sky, the sun, Tower Bridge, the river and everything in front with plain flat magenta (hex #FF00FF). No text, nothing else."
- **L3 Tower Bridge:** "Keep only Tower Bridge: both towers, the walkway, the road deck and the chains. Replace everything else, including the sky, skyline, river and trees, with plain flat magenta (hex #FF00FF). No text, nothing else."
- **L4 Foreground:** "Keep only the front layer: the river with its ripples and reflections, the boat, the bus, the embankments, the trees and the shrubs. Complete the river where Tower Bridge's piers stood. Replace the sky, the sun, the skyline and Tower Bridge with plain flat magenta (hex #FF00FF). No text, nothing else."

## Fixes if a render misses
- Text or a city name appears: move "No text, no letters, no numbers" to the very start.
- Colours drift off palette: delete the hex codes, keep the names, and correct in Illustrator.
- Too photographic or 3D: "flat vector shapes only, no realistic lighting, no 3D rendering".
- Tower Bridge gets extra towers: "exactly two towers, the Victorian bascule bridge with one high walkway between them".
- A layer plate redraws the scene instead of isolating it: add "Do not redraw, cut out" and rerun once.

## Style v2: editorial golden hour (26 Oct 2026)

Grady shared four new style references (Segesta, Melbourne, YHA "Experience the City", St Paul's). Decisions:
- Blend of what they share. No single piece copied.
- No people.
- Reference palette snapped to brand: Stellar Midnight #070089, Deep Violet #400685, Twilight #9C9DEC, Celestial Bloom #E19CEC, Yellow Gold #FFB310, Prometheus Red #F76336, Teal Meridian #006D5B, Silver #CFD2D4, White. The same palette for every city, replacing the per-city lead colour.
- References described in text only, never uploaded. They look like real illustrators' commissioned work.

What the four share
- Flat editorial illustration with soft gradients and fine grain or dry-brush texture.
- A warm and cool light split: lit faces in peach and gold, shadows in blue and violet.
- An eye-level view, one landmark centred, framed by buildings or trees at the sides, with open sky for a headline.
- Indigo and violet dominate, with warm light as the accent.

### London v2 (1:1)

```text
Editorial travel illustration of Tower Bridge in London at golden hour, a modern hand-made digital painting: flat shapes with soft gradients, fine grain and subtle dry-brush texture, crisp simplified architecture, no outlines, nothing photographic. Seen at eye level from the riverside walk on the south bank, looking straight at Tower Bridge, which stands centred as the hero: exactly two Gothic stone towers with pointed roofs and small corner turrets, the high walkway between them, the bascule road deck and suspension chains sweeping down to both banks. Low warm sun from the left lights the stone faces in peach and Yellow Gold (hex #FFB310) with Prometheus Red (hex #F76336) on the brightest edges, and every shadow side falls in cool Deep Violet (hex #400685) and Twilight (hex #9C9DEC). Behind the bridge, The Shard rises on the right and the City towers sit soft and hazy on the left in pale Twilight. The sky runs from Stellar Midnight (hex #070089) at the very top through Deep Violet and Twilight to a soft Celestial Bloom (hex #E19CEC) and peach glow at the horizon, with two or three long soft brushed clouds catching warm light. The Thames is calm, deep violet, with long gold and peach reflections of the lit towers. Framing: a large plane tree in dark Teal Meridian (hex #006D5B) and Deep Violet leans in from the left edge, and the corner of a warm-lit brick building with glowing windows stands at the right edge. A stone riverside railing runs along the bottom. Use only these colours plus Silver (hex #CFD2D4) and white: Stellar Midnight, Deep Violet, Twilight, Celestial Bloom, Yellow Gold, Prometheus Red, Teal Meridian. No people, no text, no letters, no numbers, no signs, no logos, no flags, no border. Full-bleed scene. The tops of the bridge towers reach 38 percent from the top. The tip of The Shard reaches no higher than 28 percent from the top. The top 26 percent of the frame is open sky, kept clear for a headline.
```

### London v2 result (26 Oct 2026)

Output: https://d8j0ntlcm91z4.cloudfront.net/user_3F9g5MvyxWEcBzuFjPmI97hrMM7/hf_20261026_141735_62ae0671-dfd7-4e93-9db9-be264bfe1c59.png
Full size: `plates/london-v2-golden-hour-2048.png`. Preview: `london-v2-golden-hour-preview.jpg`. Cost 2 credits.

What worked
- Hits the shared traits: golden-hour warm and cool light, an indigo-to-pink sky, fine grain, soft brushed clouds, flat simplified shapes.
- Framing as in the references: a plane tree from the left, a warm-lit brick building at the right edge, a stone railing along the bottom.
- Tower Bridge is right: two towers, turrets, the walkway, the bascule deck, red-lit chains, the shore tower at the left. The Shard and the old City Hall "egg" sit where they really are.
- Palette holds: violet, Twilight and Celestial Bloom in shade, gold and Prometheus Red on lit edges, Teal Meridian only in the tree.
- No text anywhere, checked at full size. No people.

What to watch
- The view is three-quarter, not straight-on. Closer to YHA and Melbourne, and it reads better.
- One high walkway band. The real bridge has two side by side, which look like one from here.
- Tower tops at 30% from the top, the Shard at 29%. The top quarter is clear sky with two clouds, so the city name fits.
- The 2K plate is raster. For Illustrator and animation, split it into sky, skyline, bridge, foreground frame (tree, building, railing) and water by hand or with Image Trace. AI layer extraction failed on the earlier plate.

### London v2, extended to 4:5 for a headline (26 Oct 2026)

Grady liked v2 and asked for room at the top for type, laid out like the YHA "Experience the City" poster.
- FLUX.2 Pro Outpaint, top only, +400 px on a 1600 px copy (its canvas cap is 4 MP, so the 2048 plate couldn't go in). Result 1600x2000, 4:5. Cost 4.4 credits.
- Output: https://d8j0ntlcm91z4.cloudfront.net/user_3F9g5MvyxWEcBzuFjPmI97hrMM7/hf_20261026_142409_e1db8770-511a-427e-8f62-da8b460b68b4.png
- File: `plates/london-v2-4x5-outpaint-1600x2000.png`. Preview: `london-v2-4x5-preview.jpg`.

What worked
- The original image is untouched, with no visible seam at the join (row 400 matches: #161179).
- The plane tree grows naturally up into the top left corner, framing the sky the way the YHA trees do.

What missed
- The new sky runs the wrong way: pink at the very top (#D56D98), then violet, then indigo at the join. It should deepen to indigo at the top.
- It added a cloud in the new area despite "no clouds".
- Both sit in the headline zone, so white type there has weaker contrast.

Fix options
- Photoshop, about 10 minutes: Select Color Range on the sky in the top 400 px, then fill with a gradient from about #0A0672 at the top to #161179 at the join, then add noise to match the grain.
- Or rerun the outpaint with a stronger sky instruction (4.4 credits, random result).

## London v3: true landmark colours, 4:5 (26 Oct 2026)

Grady's calls: a fresh 4:5 render; landmarks in their true real-world colours, even off-palette; soft golden-hour light; the indigo-to-pink sky from the square v2; headline space at the top, laid out like YHA.

```text
Portrait editorial travel-poster illustration of Tower Bridge in London at golden hour, a modern hand-made digital painting: flat shapes with soft gradients, fine grain and subtle dry-brush texture, crisp simplified architecture, no outlines, nothing photographic. Seen at eye level from the riverside walk on the south bank, looking at Tower Bridge, which stands centred as the hero: exactly two Gothic towers with pointed roofs and small corner turrets, the high walkway between them, the bascule road deck and suspension chains sweeping down to both banks. The landmarks keep their true real-world colours: the towers in pale warm grey Portland stone and granite with dark slate roofs and small gold-tipped finials, all the bridge steelwork (the walkway lattice, the suspension chains, the deck girders) painted its real light blue and white. Behind the bridge, The Shard rises on the right in pale grey-blue glass, the silver glass dome of the old City Hall sits low on the right bank, and the City towers stand soft and hazy on the left in grey-blue glass. Soft golden-hour light: a low warm sun from the left adds a gentle peach glow on the sunlit faces, the shadow sides fall in cool soft violet, and the true colours stay clearly readable. The sky is deep indigo (Stellar Midnight, hex #070089) at the very top, through Deep Violet (hex #400685) and soft lavender, to a gentle pink and peach glow at the horizon, with two or three long soft brushed clouds catching warm light, all of them low in the sky just above the skyline. The Thames is calm and deep violet, with long reflections of the bridge in its true stone, blue and white. Framing: a large plane tree with dark green leaves leans in from the left edge and its leafy branches reach up into the top left corner, and the corner of a warm-lit brick building with glowing windows stands at the right edge. A pale stone riverside railing runs along the bottom. No people, no text, no letters, no numbers, no signs, no logos, no flags, no border. Full-bleed scene. The top 34 percent of the frame is open, even indigo sky with no clouds, kept clear for a headline, framed only by the tree branches at the top left. The tops of the bridge towers reach 44 percent from the top. The tip of The Shard reaches no higher than 38 percent from the top.
```

Result: https://d8j0ntlcm91z4.cloudfront.net/user_3F9g5MvyxWEcBzuFjPmI97hrMM7/hf_20261026_152419_8141711a-9fa6-4334-930d-d694f7f580b5.png
File: `plates/london-v3-4x5-true-colour-1856x2304.png`. Preview: `london-v3-4x5-preview.jpg`. Cost 2 credits.

What worked
- True colours read at a glance: stone towers, slate roofs, gold finials, light blue and white steelwork. Both walkways show.
- The Shard, the Gherkin, the City towers and the old City Hall are all in place, in grey-blue and silver glass.
- The sky is indigo at the top (#1A1F6C at the top right), through lavender to a pink and peach glow. Clouds stay low, from 38% down.
- Soft golden hour: a peach glow on the lit faces, violet shade, colours still true.
- Same framing as v2: the tree from the left, the lit brick building at right, the stone railing at the bottom.
- No text and no people, checked at full size.

What to watch
- The tree canopy is heavier than in YHA. It covers about three quarters of the width in the top 15%. The clear sky for type sits from about 15% to 34% down, centred or right of centre. Trim branches in Photoshop if the headline needs the full top band.
- The tower tops sit at 43% and the Shard at 44%. Both are below the headline zone.
- The steel blue (about #6FA8DC) and the brick are off-palette by Grady's choice. The sky stays brand indigo.
