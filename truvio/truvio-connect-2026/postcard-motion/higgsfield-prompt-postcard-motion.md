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
