# Handoff: Truvio Connect 2026, Higgsfield generation run

You are generating image plates in Higgsfield for a Truvio LinkedIn campaign. Use your Higgsfield MCP tools. Grady, a designer at Truvio, will finish every image by hand in Photoshop. Your job is clean plates, not finished ads.

## The job in one paragraph
Truvio Connect 2026 is a free one-day event for Microsoft Dynamics 365 Finance & Operations customers, in London (10 Nov), Copenhagen (12 Nov), Eindhoven (24 Nov) and Stockholm (26 Nov). Two visual directions go to the event lead as options. **Option A, Postcards:** a "Greetings from London" postcard. Higgsfield makes a dusk photo of each landmark, which Grady clips inside big city letters, plus one blank real-paper postcard on a violet desk. **Option B, Miniature Cities:** each landmark as a clay miniature diorama on its own pastel colour, with tiny attendees walking past. Higgsfield makes the full plate with empty space for type. You run 16 prompts, listed at the end with IDs A1 to A7 and B1 to B9.

## Hard rules
1. Paste each prompt exactly as written. Change a prompt only through the fix list below, one fix at a time, and log it.
2. Never add text, logos, names or words to any prompt. All type is added later by hand.
3. Never generate a real person. No likeness of anyone, including the event host.
4. Plates only. Upscaling, editing, animating and compositing wait for Grady to ask.
5. If a setting below doesn't exist in your tools, use the stated fallback and say so in the report. Never guess a tool name. List your tools first.

## Step 0: check your tools
- List your Higgsfield tools and the models they offer. Confirm Nano Banana Pro is available. If it isn't, stop and ask Grady which model to use.
- Check which aspect ratios Nano Banana Pro accepts (need 1:1, 4:5, 21:9; fallbacks 3:4 and 16:9).
- Check how reference images are passed (upload, URL or file id). Grady attaches 10 PNGs to this chat, named as listed below.
- Check the resolution and batch settings. Target: 2K, batch 4.
- Tell Grady in one short message what you found, then start. Don't wait for an answer. The one exception is a missing Nano Banana Pro.

## Reference images (attached by Grady)
These are flat layout mocks. They lock composition only. Their colours and shapes are rough stand-ins, so the prompt text wins on colour and detail.
- `ref-d3-lon-1080x1080.png`, `ref-d3-lon-1080x1350.png`: blank card on violet, for A5 and A6
- `ref-d1-lon-1080x1080.png`, `ref-d1-lon-1080x1350.png`: London miniature, for B1 and B2
- `ref-d1-cph-1080x1080.png`, `ref-d1-cph-1080x1350.png`: Copenhagen, for B3 and B4
- `ref-d1-ein-1080x1080.png`, `ref-d1-ein-1080x1350.png`: Eindhoven, for B5 and B6
- `ref-d1-sth-1080x1080.png`, `ref-d1-sth-1080x1350.png`: Stockholm, for B7 and B8

## Settings for every prompt
- Model: Nano Banana Pro
- Resolution: 2K
- Batch: 4
- Aspect and references: as listed on each prompt. If 4:5 is missing, use 3:4 (Grady trims 90 px). If 21:9 is missing, use 16:9.
- No negative prompt field is needed. The exclusions are inside the prompts.

## Run order
1. **A1 to A4**, the four landmark plates. No references.
2. **A5, A6, A7**, the card flat lays.
3. **B1 first, on its own.** London miniature 1:1 with only its layout ref. Pick the best frame. This is the "B1 winner".
4. **B2 to B8**, each with its own layout ref plus the B1 winner as a second reference. Watch for one failure: the model copies the London layout or the London landmark instead of following the new ref and text. If that happens, rerun that prompt with only its layout ref. It doesn't count as the reroll.
5. **B9**, the cover, with the B1 winner as a style reference.

About 64 images for the first pass, plus up to 16 reroll batches.

## Self-check after every batch
Look at all 4 images. Score each against the checks for its direction. An image passes if it clears every "must" check.

**Postcards landmark plates (A1 to A4)**
- Must: the right landmark, recognisable, built correctly. Tower Bridge has exactly two towers with two high walkways. Nyhavn has gabled canal houses. Evoluon is the flying saucer on V columns. Stockholm City Hall has a square brick tower with three gold crowns.
- Must: no text, signs, logos, people or named boats.
- Must: the whole landmark sits inside the frame, with the horizon near 72 percent height.
- Should: a smooth cloudless sky, deep violet at the top to warm gold at the horizon.

**Postcards card plates (A5 to A7)**
- Must: every card face is blank. No marks, lines, text or stamp.
- Must: the desk is a flat, even deep violet, with no vignette or gradient.
- Must: no props, hands or pens.
- Should: the card is about 86 percent of the frame width, with empty desk above and below.

**Miniature Cities (B1 to B9)**, in this order
- Must: brand colours only. Every saturated colour matches a hex named in the prompt.
- Must: the landmark wins the frame within two seconds. The figures stay small and never compete.
- Must: dead-on front camera. No isometric view and no tilt.
- Must: one flat background colour edge to edge. No horizon, seam or gradient.
- Must: no text or marks on the badges, models or anywhere else.
- Should: the top 38 to 42 percent is empty for the headline.
- Should: one dark mass, one hot accent, at most four saturated hues.

**Reroll rule:** if all 4 images in a batch fail a must check, pick the single fix from the list below that targets the failure. Add it to the prompt and rerun once. After that one reroll, stop on that prompt and report, even if it still fails.

## Fix list (add the exact words)
- Tower Bridge has extra towers or turns into London Bridge: "exactly two towers, the Victorian bascule bridge with two high walkways next to the Tower of London"
- Landmark is cropped: "the whole landmark sits inside the frame with a wide margin on both sides"
- Busy sky or clouds: "a clean, cloudless, smooth gradient sky with no texture"
- Text or marks on the blank card: move "The card face is completely blank: no printing, no lines, no stamp, no text, no marks." to the very start of the prompt
- Card looks like a cheap stock mockup: "high-end editorial still life, real heavy paper, soft directional daylight"
- Vignette or gradient on the ground or desk: "perfectly flat, even colour from edge to edge"
- Camera drifts to isometric or three-quarter: move "dead-on front elevation, near-orthographic, no tilt" to the very start of the prompt
- Figures too big or crowding: "the figures are tiny, each no taller than one sixth of the landmark, with wide gaps between them"
- Text or logos on the badges: "badges are plain white rectangles with no marks"
- A second hot accent appears, such as gold badges or red clothes: add "figures wear only White and Silver" right after the colour paragraph
- Hex codes appear as text in the image: delete the hex codes from that prompt and keep the colour names

## What to send back
One message, with a table per direction:

| ID | Output links (all 4) | Pick | Why (one line) | Fix applied | Open issue |
|---|---|---|---|---|---|

Then:
- Settings you changed or fell back to (model, aspect, resolution), and why.
- Any prompt that still fails after its reroll, with what is wrong.
- The B1 winner's link, called out at the top.
- Pick rules: landmark accuracy first, then brand colours, then layout zones. Say "none" when no image is usable. Don't pick the least bad one.

Keep the report plain and short. Use no em dashes.

---

# The 16 prompts
## A1. Postcards: landmark plate, London, Tower Bridge
- Aspect: 21:9 (fallback 16:9)
- References: none

```text
Premium editorial travel photograph of Tower Bridge in London at dusk, taken from the south bank of the Thames, looking straight at the full length of the bridge at eye level with a 50mm lens. Exactly two stone towers with steep pointed roofs and small corner turrets, the two high walkways between them, the road deck and the suspension chains sweeping down to both banks are all fully visible and sharp. The sky is a clear, smooth dusk gradient from deep violet (hex #400685) at the top through soft lavender to a warm yellow gold (hex #FFB310) glow just above the horizon, with no clouds. The towers catch the last warm light and a few tower windows glow warm gold. The river is calm and dark violet, with soft vertical reflections of the bridge. High detail, sharp from edge to edge, true-to-life colour, premium travel photography, not a stock postcard. No text, no signs, no logos, no boats, no people, no birds, no lens flare, nothing else in the frame. The bridge sits centred and spans 70 percent of the frame width. The horizon sits at 72 percent of the frame height. The tops of the towers reach 22 percent from the top. This image will be clipped inside large letters, so keep a strong silhouette across the whole width.
```

## A2. Postcards: landmark plate, Copenhagen, Nyhavn
- Aspect: 21:9 (fallback 16:9)
- References: none

```text
Premium editorial travel photograph of the row of narrow 17th-century gabled townhouses along the Nyhavn canal in Copenhagen at dusk, seen straight on from across the water at eye level with a 50mm lens. Facades in warm yellow gold, soft red, celestial blue and off-white, each house with tall white-framed windows. Two old wooden sailing boats with bare masts are moored along the quay. The sky is a clear, smooth dusk gradient from deep violet (hex #400685) at the top through soft lavender to a warm yellow gold (hex #FFB310) glow just above the horizon, with no clouds. The facades catch the last warm light and a few windows glow warm gold. The canal is calm and dark violet, with soft vertical reflections of the houses. High detail, sharp from edge to edge, true-to-life colour, premium travel photography, not a stock postcard. No text, no signs, no logos, no other boats, no people, no birds, no lens flare, nothing else in the frame. The row of houses sits centred and spans 70 percent of the frame width. The waterline sits at 72 percent of the frame height. The tops of the gables reach 22 percent from the top. This image will be clipped inside large letters, so keep a strong silhouette across the whole width.
```

## A3. Postcards: landmark plate, Eindhoven, Evoluon
- Aspect: 21:9 (fallback 16:9)
- References: none

```text
Premium editorial travel photograph of the Evoluon in Eindhoven at dusk, the 1966 flying-saucer-shaped concrete building, seen from the lawn at eye level with a 50mm lens. A smooth white concrete dome on top of a wide rim and a shallow bowl underneath, standing on slender V-shaped concrete columns. A thin ring of windows along the dome glows warm gold. The sky is a clear, smooth dusk gradient from deep violet (hex #400685) at the top through soft lavender to a warm yellow gold (hex #FFB310) glow just above the horizon, with no clouds. The concrete catches the last warm light. The ground is a flat dark lawn with a shallow reflecting pool in front, with soft reflections of the building. High detail, sharp from edge to edge, true-to-life colour, premium travel photography, not a stock postcard. No text, no signs, no logos, no people, no birds, no lens flare, nothing else in the frame. The building sits centred and spans 70 percent of the frame width. The ground line sits at 72 percent of the frame height. The top of the dome reaches 30 percent from the top. This image will be clipped inside large letters, so keep a strong silhouette across the whole width.
```

## A4. Postcards: landmark plate, Stockholm, City Hall
- Aspect: 21:9 (fallback 16:9)
- References: none

```text
Premium editorial travel photograph of Stockholm City Hall at dusk, seen across the water of Riddarfjärden at eye level with a 50mm lens. The long dark red-brick building and its tall square brick tower, topped by a slim spire with three small gold crowns at the very top. The sky is a clear, smooth dusk gradient from deep violet (hex #400685) at the top through soft lavender to a warm yellow gold (hex #FFB310) glow just above the horizon, with no clouds. The brick catches the last warm light and a few windows glow warm gold. The water is calm and dark violet, with soft vertical reflections of the building. High detail, sharp from edge to edge, true-to-life colour, premium travel photography, not a stock postcard. No text, no signs, no logos, no boats, no people, no birds, no lens flare, nothing else in the frame. The building sits centred and spans 70 percent of the frame width. The waterline sits at 72 percent of the frame height. The crowns at the top of the tower reach 18 percent from the top. This image will be clipped inside large letters, so keep a strong silhouette across the whole width.
```

## A5. Postcards: blank card flat lay, 1:1
- Aspect: 1:1
- References: ref-d3-lon-1080x1080.png

```text
Premium editorial still-life photo, shot from directly above. Nothing else in the frame apart from one postcard. A single blank postcard lies on a flat matte deep violet (hex #400685) desk surface, evenly lit from edge to edge, with no gradient, no vignette and no texture. The postcard is heavy uncoated off-white card stock (hex #F8F9FE) in landscape format, rotated 3 degrees counter-clockwise, with crisp, very slightly rounded corners and a soft natural contact shadow on the lower right. The card face is completely blank: no printing, no lines, no stamp, no text, no marks. Fine paper fibre is visible up close. Soft directional daylight from the upper left, true-to-life colour. No pens, no hands, no plants, no envelopes, no props, no logos, no text. The card is centred, spans 86 percent of the frame width and 57 percent of the frame height. The top 12 percent and the bottom 18 percent of the frame are empty violet desk, kept clear for the logo and the CTA.
```

## A6. Postcards: blank card flat lay, 4:5
- Aspect: 4:5 (fallback 3:4)
- References: ref-d3-lon-1080x1350.png

```text
Premium editorial still-life photo, shot from directly above. Nothing else in the frame apart from one postcard. A single blank postcard lies on a flat matte deep violet (hex #400685) desk surface, evenly lit from edge to edge, with no gradient, no vignette and no texture. The postcard is heavy uncoated off-white card stock (hex #F8F9FE) in landscape format, rotated 3 degrees counter-clockwise, with crisp, very slightly rounded corners and a soft natural contact shadow on the lower right. The card face is completely blank: no printing, no lines, no stamp, no text, no marks. Fine paper fibre is visible up close. Soft directional daylight from the upper left, true-to-life colour. No pens, no hands, no plants, no envelopes, no props, no logos, no text. The card is centred, spans 86 percent of the frame width and 56 percent of the frame height. The top 14 percent and the bottom 18 percent of the frame are empty violet desk, kept clear for the logo and the CTA.
```

## A7. Postcards: carousel cover, four blank cards
- Aspect: 1:1
- References: none

```text
Premium editorial still-life photo, shot from directly above. Nothing else in the frame apart from four postcards. Four identical blank postcards lie in a loose two-by-two grid on a flat matte deep violet (hex #400685) desk surface, evenly lit from edge to edge, with no gradient, no vignette and no texture. Each postcard is heavy uncoated off-white card stock (hex #F8F9FE) in landscape format, each rotated a few degrees in a different direction and slightly overlapping at the centre, with crisp, very slightly rounded corners and a soft natural contact shadow on the lower right. Every card face is completely blank: no printing, no lines, no stamp, no text, no marks. Fine paper fibre is visible up close. Soft directional daylight from the upper left, true-to-life colour. No pens, no hands, no plants, no envelopes, no props, no logos, no text. The cards fill the lower 60 percent of the frame. The top 38 percent is empty violet desk, kept clear for the headline.
```

## B1. Miniature Cities: London, Tower Bridge, 1:1
- Aspect: 1:1
- References: ref-d1-lon-1080x1080.png

```text
Square stylized 3D miniature diorama of Tower Bridge in London, built as a simplified scale model and seen as a flat front elevation. Exactly two square towers, each with a steep pointed roof and four small corner turrets, two high walkways joining the towers near the top, a flat road deck running the full width of the model, two solid stone piers under the towers, and two curved suspension chains sweeping down from the towers to the ground at the left and right ends. Seven tiny attendees walk in a loose, widely spaced line along the ground in front of the bridge, left to right, mid-step. Each figure stands no taller than one sixth of the tower height and wears a simple Deep Violet lanyard with a small plain white badge. The model sits directly on the ground with a short soft contact shadow.

3D rendered still, stylized miniature diorama. Matte soft-vinyl and modelling-clay materials with a faint waxy sheen. No glossy plastic and no mirror reflections, apart from named metal and glass props. Faint subsurface scatter on skin. Surfaces are clean and unmarked, with no grain, no scratches and no fabric weave. Forms are simplified and rounded, all edges softly beveled, no sharp corners.

Camera: dead-on front elevation at the main subject's chest height, near-orthographic, long lens around 100mm, no lens distortion, no tilt. Frame as set in the layout lines, subject centered.

Staging: every object rests on one continuous flat ground plane. Background and floor are the same single flat color, with no horizon line, no wall seam, no gradient, no texture and no vignette. Props sit left and right of center like a flat elevation, spaced with generous air between them. Nothing overlaps the main subject's silhouette.

Light: one broad soft frontal key with gentle fill. Low contrast, no hard shadows, no rim light, no colored gels. Each object drops a short soft contact shadow directly beneath it and nothing else.

Render: clean edges, no depth of field, no bloom, no lens flare, no film grain, no motion blur, no floating dust. Physically based, offline render quality, crisp at full resolution.

Characters: adult proportions, head a little larger than life, roughly 6.5 heads tall. Faces are small and simplified, eyes as clean rounded shapes, mouths minimal. Hair is one sculpted mass with carved planes and no individual strands. Hands are simplified with defined fingers and no knuckle detail. Glasses are chunky flat-fronted shapes. Clothing is soft cloth with large rounded folds, no weave texture and no print. Expressions are calm and mid-action, caught halfway through a real task, never posing at camera. No wide cartoon grins, no oversized eyes, no caricature.

Background and floor are flat Violet Mist #D6C7DB. The towers and walkways are the largest mass, in Deep Violet #400685. The two suspension chains are the one hot accent, in Yellow Gold #FFB310, touching the violet towers. The tower roofs are the mid-tone, in Regal Plum #890062. The road deck and piers are White #FFFFFF. The figures wear White #FFFFFF and Silver #CFD2D4. Nothing else is saturated.

No text, no logos, no signage, no readable labels, no screens, no user interface, no watermark. No isometric or three-quarter camera. No visible wall or horizon line. No gradient background. No depth of field. No hard directional shadow. No glossy or metallic finish on skin or cloth. No stock-photo lighting. No Pixar or Disney face styling, no Ghibli styling, no anime eyes. No extra saturated colors beyond the ones named.

Layout: the model spans 78 percent of the frame width, centred. Its base sits at 84 percent of the frame height. The top 38 percent of the frame is empty Violet Mist, kept clear for a headline. The bottom 12 percent is empty ground, kept clear for the date and a button.
```

## B2. Miniature Cities: London, Tower Bridge, 4:5
- Aspect: 4:5 (fallback 3:4)
- References: ref-d1-lon-1080x1350.png + B1 winner

```text
Portrait stylized 3D miniature diorama of Tower Bridge in London, built as a simplified scale model and seen as a flat front elevation. Exactly two square towers, each with a steep pointed roof and four small corner turrets, two high walkways joining the towers near the top, a flat road deck running the full width of the model, two solid stone piers under the towers, and two curved suspension chains sweeping down from the towers to the ground at the left and right ends. Seven tiny attendees walk in a loose, widely spaced line along the ground in front of the bridge, left to right, mid-step. Each figure stands no taller than one sixth of the tower height and wears a simple Deep Violet lanyard with a small plain white badge. The model sits directly on the ground with a short soft contact shadow.

3D rendered still, stylized miniature diorama. Matte soft-vinyl and modelling-clay materials with a faint waxy sheen. No glossy plastic and no mirror reflections, apart from named metal and glass props. Faint subsurface scatter on skin. Surfaces are clean and unmarked, with no grain, no scratches and no fabric weave. Forms are simplified and rounded, all edges softly beveled, no sharp corners.

Camera: dead-on front elevation at the main subject's chest height, near-orthographic, long lens around 100mm, no lens distortion, no tilt. Frame as set in the layout lines, subject centered.

Staging: every object rests on one continuous flat ground plane. Background and floor are the same single flat color, with no horizon line, no wall seam, no gradient, no texture and no vignette. Props sit left and right of center like a flat elevation, spaced with generous air between them. Nothing overlaps the main subject's silhouette.

Light: one broad soft frontal key with gentle fill. Low contrast, no hard shadows, no rim light, no colored gels. Each object drops a short soft contact shadow directly beneath it and nothing else.

Render: clean edges, no depth of field, no bloom, no lens flare, no film grain, no motion blur, no floating dust. Physically based, offline render quality, crisp at full resolution.

Characters: adult proportions, head a little larger than life, roughly 6.5 heads tall. Faces are small and simplified, eyes as clean rounded shapes, mouths minimal. Hair is one sculpted mass with carved planes and no individual strands. Hands are simplified with defined fingers and no knuckle detail. Glasses are chunky flat-fronted shapes. Clothing is soft cloth with large rounded folds, no weave texture and no print. Expressions are calm and mid-action, caught halfway through a real task, never posing at camera. No wide cartoon grins, no oversized eyes, no caricature.

Background and floor are flat Violet Mist #D6C7DB. The towers and walkways are the largest mass, in Deep Violet #400685. The two suspension chains are the one hot accent, in Yellow Gold #FFB310, touching the violet towers. The tower roofs are the mid-tone, in Regal Plum #890062. The road deck and piers are White #FFFFFF. The figures wear White #FFFFFF and Silver #CFD2D4. Nothing else is saturated.

No text, no logos, no signage, no readable labels, no screens, no user interface, no watermark. No isometric or three-quarter camera. No visible wall or horizon line. No gradient background. No depth of field. No hard directional shadow. No glossy or metallic finish on skin or cloth. No stock-photo lighting. No Pixar or Disney face styling, no Ghibli styling, no anime eyes. No extra saturated colors beyond the ones named.

Layout: the model spans 88 percent of the frame width, centred. Its base sits at 87 percent of the frame height. The top 42 percent of the frame is empty Violet Mist, kept clear for a headline. The bottom 10 percent is empty ground, kept clear for the date and a button.
```

## B3. Miniature Cities: Copenhagen, Nyhavn, 1:1
- Aspect: 1:1
- References: ref-d1-cph-1080x1080.png + B1 winner

```text
Square stylized 3D miniature diorama of Nyhavn in Copenhagen, built as a simplified scale model and seen as a flat front elevation. A row of six narrow canal houses with steep gabled roofs stands shoulder to shoulder, each a different height, each with two rows of simple rectangular windows. A small wooden boat with one bare mast lies along the quay in front of the houses. Six tiny attendees walk in a loose, widely spaced line along the quay, left to right, mid-step. Each figure stands no taller than one sixth of the tallest house and wears a simple Deep Violet lanyard with a small plain white badge. The model sits directly on the ground with a short soft contact shadow.

3D rendered still, stylized miniature diorama. Matte soft-vinyl and modelling-clay materials with a faint waxy sheen. No glossy plastic and no mirror reflections, apart from named metal and glass props. Faint subsurface scatter on skin. Surfaces are clean and unmarked, with no grain, no scratches and no fabric weave. Forms are simplified and rounded, all edges softly beveled, no sharp corners.

Camera: dead-on front elevation at the main subject's chest height, near-orthographic, long lens around 100mm, no lens distortion, no tilt. Frame as set in the layout lines, subject centered.

Staging: every object rests on one continuous flat ground plane. Background and floor are the same single flat color, with no horizon line, no wall seam, no gradient, no texture and no vignette. Props sit left and right of center like a flat elevation, spaced with generous air between them. Nothing overlaps the main subject's silhouette.

Light: one broad soft frontal key with gentle fill. Low contrast, no hard shadows, no rim light, no colored gels. Each object drops a short soft contact shadow directly beneath it and nothing else.

Render: clean edges, no depth of field, no bloom, no lens flare, no film grain, no motion blur, no floating dust. Physically based, offline render quality, crisp at full resolution.

Characters: adult proportions, head a little larger than life, roughly 6.5 heads tall. Faces are small and simplified, eyes as clean rounded shapes, mouths minimal. Hair is one sculpted mass with carved planes and no individual strands. Hands are simplified with defined fingers and no knuckle detail. Glasses are chunky flat-fronted shapes. Clothing is soft cloth with large rounded folds, no weave texture and no print. Expressions are calm and mid-action, caught halfway through a real task, never posing at camera. No wide cartoon grins, no oversized eyes, no caricature.

Background and floor are flat Aqua Wash #B5DAE4. Two houses are the largest mass, in Deep Violet #400685. Two houses are the mid-tone, in Teal Meridian #006D5B. Two houses are White #FFFFFF. The boat hull is the one hot accent, in Prometheus Red #F76336, sitting in front of a violet house. Window frames are White #FFFFFF. The figures wear White #FFFFFF and Silver #CFD2D4. Nothing else is saturated.

No text, no logos, no signage, no readable labels, no screens, no user interface, no watermark. No isometric or three-quarter camera. No visible wall or horizon line. No gradient background. No depth of field. No hard directional shadow. No glossy or metallic finish on skin or cloth. No stock-photo lighting. No Pixar or Disney face styling, no Ghibli styling, no anime eyes. No extra saturated colors beyond the ones named.

Layout: the model spans 78 percent of the frame width, centred. Its base sits at 84 percent of the frame height. The top 38 percent of the frame is empty Aqua Wash, kept clear for a headline. The bottom 12 percent is empty ground, kept clear for the date and a button.
```

## B4. Miniature Cities: Copenhagen, Nyhavn, 4:5
- Aspect: 4:5 (fallback 3:4)
- References: ref-d1-cph-1080x1350.png + B1 winner

```text
Portrait stylized 3D miniature diorama of Nyhavn in Copenhagen, built as a simplified scale model and seen as a flat front elevation. A row of six narrow canal houses with steep gabled roofs stands shoulder to shoulder, each a different height, each with two rows of simple rectangular windows. A small wooden boat with one bare mast lies along the quay in front of the houses. Six tiny attendees walk in a loose, widely spaced line along the quay, left to right, mid-step. Each figure stands no taller than one sixth of the tallest house and wears a simple Deep Violet lanyard with a small plain white badge. The model sits directly on the ground with a short soft contact shadow.

3D rendered still, stylized miniature diorama. Matte soft-vinyl and modelling-clay materials with a faint waxy sheen. No glossy plastic and no mirror reflections, apart from named metal and glass props. Faint subsurface scatter on skin. Surfaces are clean and unmarked, with no grain, no scratches and no fabric weave. Forms are simplified and rounded, all edges softly beveled, no sharp corners.

Camera: dead-on front elevation at the main subject's chest height, near-orthographic, long lens around 100mm, no lens distortion, no tilt. Frame as set in the layout lines, subject centered.

Staging: every object rests on one continuous flat ground plane. Background and floor are the same single flat color, with no horizon line, no wall seam, no gradient, no texture and no vignette. Props sit left and right of center like a flat elevation, spaced with generous air between them. Nothing overlaps the main subject's silhouette.

Light: one broad soft frontal key with gentle fill. Low contrast, no hard shadows, no rim light, no colored gels. Each object drops a short soft contact shadow directly beneath it and nothing else.

Render: clean edges, no depth of field, no bloom, no lens flare, no film grain, no motion blur, no floating dust. Physically based, offline render quality, crisp at full resolution.

Characters: adult proportions, head a little larger than life, roughly 6.5 heads tall. Faces are small and simplified, eyes as clean rounded shapes, mouths minimal. Hair is one sculpted mass with carved planes and no individual strands. Hands are simplified with defined fingers and no knuckle detail. Glasses are chunky flat-fronted shapes. Clothing is soft cloth with large rounded folds, no weave texture and no print. Expressions are calm and mid-action, caught halfway through a real task, never posing at camera. No wide cartoon grins, no oversized eyes, no caricature.

Background and floor are flat Aqua Wash #B5DAE4. Two houses are the largest mass, in Deep Violet #400685. Two houses are the mid-tone, in Teal Meridian #006D5B. Two houses are White #FFFFFF. The boat hull is the one hot accent, in Prometheus Red #F76336, sitting in front of a violet house. Window frames are White #FFFFFF. The figures wear White #FFFFFF and Silver #CFD2D4. Nothing else is saturated.

No text, no logos, no signage, no readable labels, no screens, no user interface, no watermark. No isometric or three-quarter camera. No visible wall or horizon line. No gradient background. No depth of field. No hard directional shadow. No glossy or metallic finish on skin or cloth. No stock-photo lighting. No Pixar or Disney face styling, no Ghibli styling, no anime eyes. No extra saturated colors beyond the ones named.

Layout: the model spans 88 percent of the frame width, centred. Its base sits at 87 percent of the frame height. The top 42 percent of the frame is empty Aqua Wash, kept clear for a headline. The bottom 10 percent is empty ground, kept clear for the date and a button.
```

## B5. Miniature Cities: Eindhoven, Evoluon, 1:1
- Aspect: 1:1
- References: ref-d1-ein-1080x1080.png + B1 winner

```text
Square stylized 3D miniature diorama of the Evoluon in Eindhoven, built as a simplified scale model and seen as a flat front elevation. A wide flying-saucer-shaped building: a smooth shallow dome on top, a thin flat rim around its widest point, and a shallow bowl underneath, raised off the ground on slender V-shaped columns. A thin ring of windows runs around the dome. Two small rounded shrubs stand on the ground, one either side of the building. Six tiny attendees walk in a loose, widely spaced line along the ground under and in front of the building, left to right, mid-step. Each figure stands no taller than one quarter of the column height and wears a simple Deep Violet lanyard with a small plain white badge. The model sits directly on the ground with a short soft contact shadow.

3D rendered still, stylized miniature diorama. Matte soft-vinyl and modelling-clay materials with a faint waxy sheen. No glossy plastic and no mirror reflections, apart from named metal and glass props. Faint subsurface scatter on skin. Surfaces are clean and unmarked, with no grain, no scratches and no fabric weave. Forms are simplified and rounded, all edges softly beveled, no sharp corners.

Camera: dead-on front elevation at the main subject's chest height, near-orthographic, long lens around 100mm, no lens distortion, no tilt. Frame as set in the layout lines, subject centered.

Staging: every object rests on one continuous flat ground plane. Background and floor are the same single flat color, with no horizon line, no wall seam, no gradient, no texture and no vignette. Props sit left and right of center like a flat elevation, spaced with generous air between them. Nothing overlaps the main subject's silhouette.

Light: one broad soft frontal key with gentle fill. Low contrast, no hard shadows, no rim light, no colored gels. Each object drops a short soft contact shadow directly beneath it and nothing else.

Render: clean edges, no depth of field, no bloom, no lens flare, no film grain, no motion blur, no floating dust. Physically based, offline render quality, crisp at full resolution.

Characters: adult proportions, head a little larger than life, roughly 6.5 heads tall. Faces are small and simplified, eyes as clean rounded shapes, mouths minimal. Hair is one sculpted mass with carved planes and no individual strands. Hands are simplified with defined fingers and no knuckle detail. Glasses are chunky flat-fronted shapes. Clothing is soft cloth with large rounded folds, no weave texture and no print. Expressions are calm and mid-action, caught halfway through a real task, never posing at camera. No wide cartoon grins, no oversized eyes, no caricature.

Background and floor are flat Gold Sand #FCE5B6. The rim and the columns are the largest mass, in Deep Violet #400685. The dome and the bowl are White #FFFFFF. The ring of windows is the one hot accent, in Regal Plum #890062, touching the violet rim. The two shrubs are the mid-tone, in Electric Green #2DB34A, each placed against a violet column. The figures wear White #FFFFFF and Silver #CFD2D4. Nothing else is saturated.

No text, no logos, no signage, no readable labels, no screens, no user interface, no watermark. No isometric or three-quarter camera. No visible wall or horizon line. No gradient background. No depth of field. No hard directional shadow. No glossy or metallic finish on skin or cloth. No stock-photo lighting. No Pixar or Disney face styling, no Ghibli styling, no anime eyes. No extra saturated colors beyond the ones named.

Layout: the model spans 78 percent of the frame width, centred. Its base sits at 84 percent of the frame height. The top 38 percent of the frame is empty Gold Sand, kept clear for a headline. The bottom 12 percent is empty ground, kept clear for the date and a button.
```

## B6. Miniature Cities: Eindhoven, Evoluon, 4:5
- Aspect: 4:5 (fallback 3:4)
- References: ref-d1-ein-1080x1350.png + B1 winner

```text
Portrait stylized 3D miniature diorama of the Evoluon in Eindhoven, built as a simplified scale model and seen as a flat front elevation. A wide flying-saucer-shaped building: a smooth shallow dome on top, a thin flat rim around its widest point, and a shallow bowl underneath, raised off the ground on slender V-shaped columns. A thin ring of windows runs around the dome. Two small rounded shrubs stand on the ground, one either side of the building. Six tiny attendees walk in a loose, widely spaced line along the ground under and in front of the building, left to right, mid-step. Each figure stands no taller than one quarter of the column height and wears a simple Deep Violet lanyard with a small plain white badge. The model sits directly on the ground with a short soft contact shadow.

3D rendered still, stylized miniature diorama. Matte soft-vinyl and modelling-clay materials with a faint waxy sheen. No glossy plastic and no mirror reflections, apart from named metal and glass props. Faint subsurface scatter on skin. Surfaces are clean and unmarked, with no grain, no scratches and no fabric weave. Forms are simplified and rounded, all edges softly beveled, no sharp corners.

Camera: dead-on front elevation at the main subject's chest height, near-orthographic, long lens around 100mm, no lens distortion, no tilt. Frame as set in the layout lines, subject centered.

Staging: every object rests on one continuous flat ground plane. Background and floor are the same single flat color, with no horizon line, no wall seam, no gradient, no texture and no vignette. Props sit left and right of center like a flat elevation, spaced with generous air between them. Nothing overlaps the main subject's silhouette.

Light: one broad soft frontal key with gentle fill. Low contrast, no hard shadows, no rim light, no colored gels. Each object drops a short soft contact shadow directly beneath it and nothing else.

Render: clean edges, no depth of field, no bloom, no lens flare, no film grain, no motion blur, no floating dust. Physically based, offline render quality, crisp at full resolution.

Characters: adult proportions, head a little larger than life, roughly 6.5 heads tall. Faces are small and simplified, eyes as clean rounded shapes, mouths minimal. Hair is one sculpted mass with carved planes and no individual strands. Hands are simplified with defined fingers and no knuckle detail. Glasses are chunky flat-fronted shapes. Clothing is soft cloth with large rounded folds, no weave texture and no print. Expressions are calm and mid-action, caught halfway through a real task, never posing at camera. No wide cartoon grins, no oversized eyes, no caricature.

Background and floor are flat Gold Sand #FCE5B6. The rim and the columns are the largest mass, in Deep Violet #400685. The dome and the bowl are White #FFFFFF. The ring of windows is the one hot accent, in Regal Plum #890062, touching the violet rim. The two shrubs are the mid-tone, in Electric Green #2DB34A, each placed against a violet column. The figures wear White #FFFFFF and Silver #CFD2D4. Nothing else is saturated.

No text, no logos, no signage, no readable labels, no screens, no user interface, no watermark. No isometric or three-quarter camera. No visible wall or horizon line. No gradient background. No depth of field. No hard directional shadow. No glossy or metallic finish on skin or cloth. No stock-photo lighting. No Pixar or Disney face styling, no Ghibli styling, no anime eyes. No extra saturated colors beyond the ones named.

Layout: the model spans 88 percent of the frame width, centred. Its base sits at 87 percent of the frame height. The top 42 percent of the frame is empty Gold Sand, kept clear for a headline. The bottom 10 percent is empty ground, kept clear for the date and a button.
```

## B7. Miniature Cities: Stockholm, City Hall, 1:1
- Aspect: 1:1
- References: ref-d1-sth-1080x1080.png + B1 winner

```text
Square stylized 3D miniature diorama of Stockholm City Hall, built as a simplified scale model and seen as a flat front elevation. A long low brick hall with a row of tall simple windows, a tall square brick tower rising on the right third of the hall, and a lower wing beyond the tower. The tower ends in a slim spire topped by exactly three small crowns. A small corner turret with a pointed roof stands at the left end of the hall. One small arched door sits at the foot of the tower. Six tiny attendees walk in a loose, widely spaced line along the ground in front of the hall, left to right, mid-step. Each figure stands no taller than one sixth of the hall height and wears a simple Deep Violet lanyard with a small plain white badge. The model sits directly on the ground with a short soft contact shadow.

3D rendered still, stylized miniature diorama. Matte soft-vinyl and modelling-clay materials with a faint waxy sheen. No glossy plastic and no mirror reflections, apart from named metal and glass props. Faint subsurface scatter on skin. Surfaces are clean and unmarked, with no grain, no scratches and no fabric weave. Forms are simplified and rounded, all edges softly beveled, no sharp corners.

Camera: dead-on front elevation at the main subject's chest height, near-orthographic, long lens around 100mm, no lens distortion, no tilt. Frame as set in the layout lines, subject centered.

Staging: every object rests on one continuous flat ground plane. Background and floor are the same single flat color, with no horizon line, no wall seam, no gradient, no texture and no vignette. Props sit left and right of center like a flat elevation, spaced with generous air between them. Nothing overlaps the main subject's silhouette.

Light: one broad soft frontal key with gentle fill. Low contrast, no hard shadows, no rim light, no colored gels. Each object drops a short soft contact shadow directly beneath it and nothing else.

Render: clean edges, no depth of field, no bloom, no lens flare, no film grain, no motion blur, no floating dust. Physically based, offline render quality, crisp at full resolution.

Characters: adult proportions, head a little larger than life, roughly 6.5 heads tall. Faces are small and simplified, eyes as clean rounded shapes, mouths minimal. Hair is one sculpted mass with carved planes and no individual strands. Hands are simplified with defined fingers and no knuckle detail. Glasses are chunky flat-fronted shapes. Clothing is soft cloth with large rounded folds, no weave texture and no print. Expressions are calm and mid-action, caught halfway through a real task, never posing at camera. No wide cartoon grins, no oversized eyes, no caricature.

Background and floor are flat Sage Gold #DCE0AD. The hall, tower and wing are the largest mass, in Deep Violet #400685. The corner turret and the spire roof are the mid-tone, in Teal Meridian #006D5B. The three crowns are small brushed metal details in Yellow Gold #FFB310. The arched door is the one hot accent, in Prometheus Red #F76336, set into the violet tower. Window frames are White #FFFFFF. The figures wear White #FFFFFF and Silver #CFD2D4. Nothing else is saturated.

No text, no logos, no signage, no readable labels, no screens, no user interface, no watermark. No isometric or three-quarter camera. No visible wall or horizon line. No gradient background. No depth of field. No hard directional shadow. No glossy or metallic finish on skin or cloth. No stock-photo lighting. No Pixar or Disney face styling, no Ghibli styling, no anime eyes. No extra saturated colors beyond the ones named.

Layout: the model spans 78 percent of the frame width, centred. Its base sits at 84 percent of the frame height. The top 38 percent of the frame is empty Sage Gold, kept clear for a headline. The bottom 12 percent is empty ground, kept clear for the date and a button.
```

## B8. Miniature Cities: Stockholm, City Hall, 4:5
- Aspect: 4:5 (fallback 3:4)
- References: ref-d1-sth-1080x1350.png + B1 winner

```text
Portrait stylized 3D miniature diorama of Stockholm City Hall, built as a simplified scale model and seen as a flat front elevation. A long low brick hall with a row of tall simple windows, a tall square brick tower rising on the right third of the hall, and a lower wing beyond the tower. The tower ends in a slim spire topped by exactly three small crowns. A small corner turret with a pointed roof stands at the left end of the hall. One small arched door sits at the foot of the tower. Six tiny attendees walk in a loose, widely spaced line along the ground in front of the hall, left to right, mid-step. Each figure stands no taller than one sixth of the hall height and wears a simple Deep Violet lanyard with a small plain white badge. The model sits directly on the ground with a short soft contact shadow.

3D rendered still, stylized miniature diorama. Matte soft-vinyl and modelling-clay materials with a faint waxy sheen. No glossy plastic and no mirror reflections, apart from named metal and glass props. Faint subsurface scatter on skin. Surfaces are clean and unmarked, with no grain, no scratches and no fabric weave. Forms are simplified and rounded, all edges softly beveled, no sharp corners.

Camera: dead-on front elevation at the main subject's chest height, near-orthographic, long lens around 100mm, no lens distortion, no tilt. Frame as set in the layout lines, subject centered.

Staging: every object rests on one continuous flat ground plane. Background and floor are the same single flat color, with no horizon line, no wall seam, no gradient, no texture and no vignette. Props sit left and right of center like a flat elevation, spaced with generous air between them. Nothing overlaps the main subject's silhouette.

Light: one broad soft frontal key with gentle fill. Low contrast, no hard shadows, no rim light, no colored gels. Each object drops a short soft contact shadow directly beneath it and nothing else.

Render: clean edges, no depth of field, no bloom, no lens flare, no film grain, no motion blur, no floating dust. Physically based, offline render quality, crisp at full resolution.

Characters: adult proportions, head a little larger than life, roughly 6.5 heads tall. Faces are small and simplified, eyes as clean rounded shapes, mouths minimal. Hair is one sculpted mass with carved planes and no individual strands. Hands are simplified with defined fingers and no knuckle detail. Glasses are chunky flat-fronted shapes. Clothing is soft cloth with large rounded folds, no weave texture and no print. Expressions are calm and mid-action, caught halfway through a real task, never posing at camera. No wide cartoon grins, no oversized eyes, no caricature.

Background and floor are flat Sage Gold #DCE0AD. The hall, tower and wing are the largest mass, in Deep Violet #400685. The corner turret and the spire roof are the mid-tone, in Teal Meridian #006D5B. The three crowns are small brushed metal details in Yellow Gold #FFB310. The arched door is the one hot accent, in Prometheus Red #F76336, set into the violet tower. Window frames are White #FFFFFF. The figures wear White #FFFFFF and Silver #CFD2D4. Nothing else is saturated.

No text, no logos, no signage, no readable labels, no screens, no user interface, no watermark. No isometric or three-quarter camera. No visible wall or horizon line. No gradient background. No depth of field. No hard directional shadow. No glossy or metallic finish on skin or cloth. No stock-photo lighting. No Pixar or Disney face styling, no Ghibli styling, no anime eyes. No extra saturated colors beyond the ones named.

Layout: the model spans 88 percent of the frame width, centred. Its base sits at 87 percent of the frame height. The top 42 percent of the frame is empty Sage Gold, kept clear for a headline. The bottom 10 percent is empty ground, kept clear for the date and a button.
```

## B9. Miniature Cities: carousel cover, all four
- Aspect: 1:1
- References: B1 winner (style only)

```text
Square stylized 3D diorama. Four small simplified scale models stand in one evenly spaced row on the ground, seen as a flat front elevation, left to right: Tower Bridge with two pointed towers and curved chains, a row of narrow gabled Nyhavn canal houses, the flying-saucer Evoluon on V-shaped columns, and Stockholm City Hall with its tall square tower. All four are the same height. Wide air between them. No figures.

3D rendered still, stylized miniature diorama. Matte soft-vinyl and modelling-clay materials with a faint waxy sheen. No glossy plastic and no mirror reflections, apart from named metal and glass props. Faint subsurface scatter on skin. Surfaces are clean and unmarked, with no grain, no scratches and no fabric weave. Forms are simplified and rounded, all edges softly beveled, no sharp corners.

Camera: dead-on front elevation at the main subject's chest height, near-orthographic, long lens around 100mm, no lens distortion, no tilt. Frame as set in the layout lines, subject centered.

Staging: every object rests on one continuous flat ground plane. Background and floor are the same single flat color, with no horizon line, no wall seam, no gradient, no texture and no vignette. Props sit left and right of center like a flat elevation, spaced with generous air between them. Nothing overlaps the main subject's silhouette.

Light: one broad soft frontal key with gentle fill. Low contrast, no hard shadows, no rim light, no colored gels. Each object drops a short soft contact shadow directly beneath it and nothing else.

Render: clean edges, no depth of field, no bloom, no lens flare, no film grain, no motion blur, no floating dust. Physically based, offline render quality, crisp at full resolution.

Background and floor are flat Deep Violet #400685. The four models are the largest mass, in Silver #CFD2D4 and White #FFFFFF. The Tower Bridge chains are the one hot accent, in Yellow Gold #FFB310. The Evoluon window ring is the cool accent, in Luminous Aqua #66FFCC. The Nyhavn boat and the shrubs are the mid-tone, in Electric Green #2DB34A. Nothing else is saturated.

No text, no logos, no signage, no readable labels, no screens, no user interface, no watermark. No isometric or three-quarter camera. No visible wall or horizon line. No gradient background. No depth of field. No hard directional shadow. No glossy or metallic finish on skin or cloth. No stock-photo lighting. No Pixar or Disney face styling, no Ghibli styling, no anime eyes. No extra saturated colors beyond the ones named.

Layout: the row spans 88 percent of the frame width, centred. The bases sit at 66 percent of the frame height. The top 48 percent of the frame is empty, kept clear for a headline. The bottom 26 percent is empty, kept clear for city names and dates.
```
