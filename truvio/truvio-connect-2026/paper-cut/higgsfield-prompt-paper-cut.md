# Higgsfield prompt: Truvio Connect 2026, Paper Cut

A direction under test for the Truvio Connect 2026 LinkedIn campaign (decided 26 Oct 2026). Each city is a layered paper-cut scene on a cream paper card, like a handmade travel poster. Higgsfield makes the scene with an empty top for type. Grady sets the city name, date and CTA by hand. Sizes 4:5 (1080x1350) first, then 1:1 (1080x1080).

## Decisions (26 Oct 2026)
- Style from Grady's Istanbul and Seoul paper-cut references. Mood only, not attached, since both carry readable titles.
- Natural pastel paper (cream, sage, dusty blue, blush, sand, terracotta) with Deep Violet #400685 as a sparing accent.
- Same heroes as City Tiles: Tower Bridge, Nyhavn, Evoluon, City Hall.
- A few small paper clouds at the sides. No birds.
- Tiny paper attendees with Deep Violet lanyards, matching City Tiles.
- No text in the image. The references' title and tagline are left out.

## Risks flagged
- This paper-cut travel poster circulates widely as an AI trend. The Deep Violet accents are the ownable part.
- It sits close to City Tiles. Both show miniature landmark clusters.
- Colours baked into paper texture are hard to shift in Photoshop. Get the palette right in the render.
- Nano Banana ignored layout percentages on City Tiles. Expect to scale the scene in Photoshop.

## Settings
- Nano Banana Pro, 2K, batch of 1. No reference image.

## London, 4:5

```text
Handmade layered paper-cut art poster of London, photographed straight on under soft even daylight. The whole scene is cut from thick matte watercolour paper and card in about eight stacked layers, with soft deckled and torn edges, visible paper fibre, slight raised relief and small gaps between layers that cast soft, short shadows. The hero is Tower Bridge at the front centre, spanning the Thames: exactly two Gothic stone towers with pointed roofs and small corner turrets, the high walkway between them, and suspension chains sweeping down to both banks. Behind it sit the Tower of London with its square White Tower, the Gherkin, the Walkie-Talkie, and The Shard, a slim pointed glass pyramid, the tallest shape in the scene. In front, the river curls through the lower scene in layered dusty blue paper with small cut-paper ripples, with two small boats, riverside trees, a cobbled embankment and rows of little houses with terracotta roofs. A red double-decker bus on the embankment. Eight tiny paper attendees walk along the embankment toward the bridge, each with a small lanyard. Natural pastel paper palette: cream, warm sand, soft sage green, dusty blue, blush pink, pale stone grey and muted terracotta. Deep Violet (hex #400685) paper appears only here and there as a sparing accent: the bridge's suspension chains and high walkway, the hulls of the two boats, a few roofs, and the attendees' lanyards. Nothing else is violet. Three small layered paper clouds sit at the far left and far right of the sky, none in the centre. The cut scene forms a soft irregular island with a torn lower edge, mounted on a plain cream paper background card that is flat and evenly lit from edge to edge. No text anywhere: no title, no city name, no letters, no numbers, no signs, no labels, no logos, no flags, no birds, no frame, no hands, nothing else in the frame. The scene fills the lower 68 percent of the frame and spans 88 percent of the width, centred. The tip of The Shard reaches no higher than 34 percent from the top. The top 30 percent of the frame is plain cream paper, kept clear for a headline.
```

## Fixes if a render misses
- Text or a title appears: move the "No text anywhere" sentence to the very start.
- Too much violet: "Deep Violet appears on no more than four small details."
- Looks like flat vector art: "real photographed paper, deckled edges, visible fibre, soft layer shadows".
- Clouds or birds crowd the top: "plain cream paper sky above the skyline, no clouds in the top third".
- Tower Bridge gets extra towers: "exactly two towers, the Victorian bascule bridge with one high walkway between them".

## Test 1: London 4:5 (26 Oct 2026)

Output: https://d8j0ntlcm91z4.cloudfront.net/user_3F9g5MvyxWEcBzuFjPmI97hrMM7/hf_20261026_135020_039be28e-6733-4937-a2dd-460615b711e3.png
Preview: `test1-london-4x5-preview.jpg`. 1856x2304. Cost 2 credits.

What worked
- Convincing photographed paper: layered card, deckled edges, fibre and soft layer shadows. It doesn't read as vector art.
- All five landmarks right: Tower Bridge with two towers, walkway and chains, the White Tower, the Gherkin, the Walkie-Talkie and The Shard.
- Deep Violet reads as an accent on the chains, walkway, tower roofs and boat hulls. The pastel base stays calm.
- No text, no birds. Two sage and cream clouds at the sides only.
- The attendees read on the embankment, walking toward the bridge.

What missed
- The Shard tip reaches 21% from the top (target 34%). Shrink in Photoshop, as with City Tiles.
- The attendees wear violet trousers as well as lanyards, so violet runs a little past "sparing".
- The torn edge frames the scene like a window torn in the card, not a floating island. The rooftops at the lower right run off the frame edge.
- The camera sits higher than straight on, closer to an elevated three-quarter view. It suits the scene.
