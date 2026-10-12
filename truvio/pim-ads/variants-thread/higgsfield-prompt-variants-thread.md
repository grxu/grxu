# Higgsfield prompt: Variants thread

Truvio PIM LinkedIn single-image ad, 1:1 (1080x1080) only. Forum-thread formula: a Reddit-style post in a fictional Dynamics and ERP community, an upvoted top answer that names Truvio PIM, and a Truvio callout box under the thread. The LinkedIn headline and body sit outside the image. Nano Banana Pro draws the thread with its copy and the callout box empty. Grady sets the lockup and the CTA line inside the callout in the comp. No separate headline sits above the thread. The post title is the hook.

## Launch blocker
- The PIM landing page is still in progress. Until it ships, the ad links to https://truvio.com/products/business-central/pim, as briefed.
- The item card ad used a different interim link: https://truvio.com/products/commerce/product-information-management. Check the new one loads before launch. The sandbox can't reach truvio.com, so neither link was tested.

## Copy (final, for reference only)
- On design, post title: How are you handling complex variants in Business Central?
- On design, post body: One product, 12 sizes, 8 colors, 3 materials. Our item setup is falling apart.
- On design, top answer: We moved variants and enrichment into Truvio PIM. It runs inside BC and syncs back only what BC needs.
- On design, callout: Test your hardest variants in a demo →
- Ads headline: Test your hardest variants in Truvio PIM
- Ads body: Dozens of sizes, colors and specs per product? Truvio PIM structures variants properly and syncs the right data back to BC. Test yours in a demo.
- Link: PIM landing page (WIP), see the blocker above.

## New words on the canvas (need sign-off)
The brief asked for fictional names, so these are proposals. None of them is in the copy.
- Community: c/ERPadmins. The c/ prefix keeps the forum look without Reddit's r/. It stays clear of the real r/Dynamics365, r/businesscentral and r/ERP.
- Poster: variant_wrangler
- Top answer author: erp_ops_lead
- Tag: Top answer
- Search all three names on Reddit before launch, so none of them points to a real account or community.
- No Reddit logo, alien mascot, wordmark or orange header bar anywhere.

## How the image matches the copy
- "How are you handling complex variants in Business Central?": the post title is the largest type on the canvas, set as a forum title. A BC buyer reads their own question in a peer's words.
- "One product, 12 sizes, 8 colors, 3 materials": the body sits right under the title. The three numbers carry the variant explosion, so the image draws no product grid.
- "upvoted top answer": a filled orange-red upvote arrow and a teal Top answer tag. Peers picked the answer, not the vendor.
- "We moved variants and enrichment into Truvio PIM": Truvio PIM is the only bold run in the answer. In Prompt A the answer card lifts out of the thread with a Twilight glow, the same move as the PIM pop-up in the item card ad.
- "Test your hardest variants in a demo →": the callout box with the gradient outline. It is the only branded element in the image.
- The image shows a peer's answer. The ads headline and body name the fix and the demo.

## Decisions (12 Oct 2026)
- Nano Banana Pro writes the thread copy. The callout box comes back empty. Grady sets the lockup and the CTA.
- Upvote signal: a filled Prometheus Red (hex #F76336) arrow plus a Top answer tag. No numbers on the canvas: no vote counts, no timestamps, no comment counts. A count would be an invented figure that reads as real social proof.
- Size: 1:1 only, same as the item card ad.
- Link: /products/business-central/pim, as briefed.

## Direction
- Ground: Deep Violet (hex #400685), flat from edge to edge.
- Thread card: white, 18px corners, the same drop shadow as the item card ad tiles.
- Top answer, Prompt A: a white card that overlaps the post card's bottom edge, indented 48px from the post text. 1px Twilight (hex #9C9DEC) outline, Twilight glow and a deep shadow.
- Top answer, Prompt B: a house off-white (hex #E6E8FC) panel inside the post card. No glow.
- Top answer tag: Teal Meridian (hex #006D5B) with white bold text, the same colour as the Master tag in the item card ad.
- Community icon: Celestial Blue (hex #008FC4) circle with a white 2x2 grid, one cell Yellow Gold (hex #FFB310), a nod to variants. Answer avatar: Yellow Gold circle with a plain white person glyph.
- Action buttons: Dark Gray (hex #6D757A) outline icons in Silver (hex #CFD2D4) pills. Icons only, no words.
- Thread type: a clean UI sans. Be Vietnam Pro in the mock, title 52px ExtraBold, body and answer 31px Regular, names 22px.
- No Museo Slab on this canvas. The post title is forum UI, and a slab title would break the native look. Departure from the default headline treatment.
- Callout: Deep Violet fill, 2px outline in the secondary gradient (Celestial Blue Light, Electric Green, Yellow Gold) at 25.4 degrees, 18px corners. Reversed lockup on the left at 176px wide. CTA on the right in Be Vietnam Pro ExtraBold 26px, #E6E8FC, with the vector arrow from the item card ad.

## Settings
- Model: Nano Banana Pro. It handles flat UI and full sentences far better than Soul, which garbles type.
- Aspect ratio 1:1. Resolution 2K, batch 4.
- Reference image: the flat mock with the lockup and CTA hidden. `variants-thread-lift-ref@2x.png` for Prompt A, `variants-thread-flat-ref@2x.png` for Prompt B. It holds the exact copy, so it helps spelling as much as layout. Never attach an earlier render or the logo.
- The mock is already close to the target look. Two failed batches on spelling mean the mock is the faster base. Export it with `.claude/skills/truvio-higgsfield-ad/scripts/export_svg.py` and finish in Illustrator.

## Prompt A: Answer lifts out (recommended)
### 1:1
Crisp, flat digital interface graphic for a premium B2B social ad, viewed straight on with no tilt, no device and no browser window. An original, unbranded discussion forum thread sits on a perfectly flat, even deep violet ground (hex #400685) from edge to edge, with no gradient, no vignette and no texture. A white post card with softly rounded corners and a soft, deep violet-tinted drop shadow holds the post. At the top left of the card sits a small round sky blue (hex #008FC4) community icon with a white two-by-two grid of rounded squares, one square yellow gold. Next to it, the community name c/ERPadmins in bold near-black, a small grey middle dot, and the username variant_wrangler in medium grey. Below them, the post title in a very large, heavy, clean geometric sans-serif in near-black, on exactly two lines: "How are you handling complex" then "variants in Business Central?". Below the title, the post body in a regular-weight dark grey sans-serif on two lines: "One product, 12 sizes, 8 colors, 3 materials. Our item" then "setup is falling apart.". Below the body, a row of three small white pill buttons with thin light grey borders and dark grey outline icons: an up arrow and a down arrow side by side, a speech bubble, a share arrow, with no numbers and no words. A white reply card, indented from the left, overlaps the lower part of the post card and hangs past its bottom edge, floating in front of it with a thin soft lavender outline (hex #9C9DEC), a faint lavender glow and a deep soft shadow. Inside the reply card, a small round yellow gold avatar (hex #FFB310) with a plain white person silhouette, the username erp_ops_lead in bold near-black, and a small rounded teal tag (hex #006D5B) with white bold text: Top answer. Below them, the reply text in a regular-weight near-black sans-serif on exactly two lines, with only the words Truvio PIM in bold: "We moved variants and enrichment into Truvio PIM." then "It runs inside BC and syncs back only what BC needs.". Below the reply text, a pill with a solid filled orange-red up arrow (hex #F76336) next to an outlined grey down arrow, with nothing between them, and a pill with a speech bubble icon. Below the thread, separated by a band of violet, a wide rounded rectangle with a thin gradient outline running from sky blue at the left through green to yellow gold at the right, flat violet inside and completely empty. The only readable words in the image are c/ERPadmins, variant_wrangler, the post title, the post body, erp_ops_lead, Top answer and the reply text, all spelled exactly as given. Truvio is spelled T-R-U-V-I-O. No vote counts, no timestamps, no other numbers, no other words. No logos, no mascot, no Reddit branding, no browser bar, no device frame, no cursor, no hands, no people, no props, nothing else in the frame. The post card spans from 6 to 94 percent of the frame width and from 12 to 69 percent of the frame height. The reply card spans from 14 to 94 percent of the width and from 50 to 73 percent of the height. The empty gradient-outlined box spans from 6 to 94 percent of the width and from 76 to 88 percent of the height. The outer 6 percent of the frame stays flat violet on all four sides.

## Prompt B: Flat thread
How it matches the copy: the most native read, a thread as it looks on screen. The answer stands out through the tint and the tag alone, so Truvio PIM gets less pull than in A.

Crisp, flat digital interface graphic for a premium B2B social ad, viewed straight on with no tilt, no device and no browser window. An original, unbranded discussion forum thread sits on a perfectly flat, even deep violet ground (hex #400685) from edge to edge, with no gradient, no vignette and no texture. A white post card with softly rounded corners and a soft, deep violet-tinted drop shadow holds the whole thread. At the top left of the card sits a small round sky blue (hex #008FC4) community icon with a white two-by-two grid of rounded squares, one square yellow gold. Next to it, the community name c/ERPadmins in bold near-black, a small grey middle dot, and the username variant_wrangler in medium grey. Below them, the post title in a very large, heavy, clean geometric sans-serif in near-black, on exactly two lines: "How are you handling complex" then "variants in Business Central?". Below the title, the post body in a regular-weight dark grey sans-serif on two lines: "One product, 12 sizes, 8 colors, 3 materials. Our item" then "setup is falling apart.". Below the body, a row of three small white pill buttons with thin light grey borders and dark grey outline icons: an up arrow and a down arrow side by side, a speech bubble, a share arrow, with no numbers and no words. Below the buttons, inside the same card, a pale lavender panel (hex #E6E8FC) with rounded corners holds the top reply. Inside the panel, a small round yellow gold avatar (hex #FFB310) with a plain white person silhouette, the username erp_ops_lead in bold near-black, and a small rounded teal tag (hex #006D5B) with white bold text: Top answer. Below them, the reply text in a regular-weight near-black sans-serif on exactly two lines, with only the words Truvio PIM in bold: "We moved variants and enrichment into Truvio PIM." then "It runs inside BC and syncs back only what BC needs.". Below the reply text, a white pill with a solid filled orange-red up arrow (hex #F76336) next to an outlined grey down arrow, with nothing between them, and a white pill with a speech bubble icon. Below the thread card, separated by a band of violet, a wide rounded rectangle with a thin gradient outline running from sky blue at the left through green to yellow gold at the right, flat violet inside and completely empty. The only readable words in the image are c/ERPadmins, variant_wrangler, the post title, the post body, erp_ops_lead, Top answer and the reply text, all spelled exactly as given. Truvio is spelled T-R-U-V-I-O. No vote counts, no timestamps, no other numbers, no other words. No logos, no mascot, no Reddit branding, no browser bar, no device frame, no cursor, no hands, no people, no props, nothing else in the frame. The post card spans from 6 to 94 percent of the frame width and from 11 to 74 percent of the frame height. The lavender reply panel spans from 10 to 90 percent of the width and from 49 to 71 percent of the height. The empty gradient-outlined box spans from 6 to 94 percent of the width and from 77 to 89 percent of the height. The outer 6 percent of the frame stays flat violet on all four sides.

## Clean plate option
- Callout box: the gradient outline needs exact hexes, and the model tends to shift them or add a glow. To skip it, replace the gradient-box sentence with "The bottom 25 percent of the frame is empty flat violet." and drop its layout sentence. Draw the box in Illustrator: 950x132px, 18px corners, 2px stroke, secondary gradient at 25.4 degrees, at x 65 and y 819 (A) or y 833 (B).
- A misspelled line that survives two batches: cover it with a white box and set it in Be Vietnam Pro at the mock sizes (title 52px ExtraBold, body 31px Regular, answer 31px Regular with Truvio PIM in ExtraBold).

## Brand check before you comp
- Ground samples #400685. Correct drift with a masked Hue/Saturation or Curves layer, which keeps the shadows.
- Upvote arrow #F76336, Top answer tag #006D5B, community icon #008FC4, avatar #FFB310, glow and outline #9C9DEC.
- Every word spelled right. Watch Truvio, enrichment, materials, Business Central, the _ characters in variant_wrangler and erp_ops_lead, and the capitals in c/ERPadmins.
- Truvio PIM is bold. Nothing else in the answer is bold.
- No numbers beyond 12, 8 and 3 in the post body. No vote counts, timestamps, Reply, Share or Sponsored labels.
- No logos, no mascot. The callout box is empty.
- Thread type is a clean sans. A serif or condensed face means retype in Be Vietnam Pro.
- 65px safe margin: nothing light crosses it.
- Comp: the official reversed lockup at 176px wide, left in the callout and vertically centred, 36px in from the outer edge of the box. CTA in Be Vietnam Pro ExtraBold 26px, #E6E8FC, right-aligned 36px in, with the vector arrow.

## Avoid list
Nano Banana Pro has no negative prompt field, so the exclusions sit inside the prompts. For a model with one: reddit logo, alien mascot, orange header bar, vote count, numbers next to arrows, timestamps, hours ago, award icons, karma, sponsored, promoted, reply button text, browser window, address bar, phone frame, laptop, mouse cursor, hands, people, photo background, gradient background, vignette, lorem ipsum, gibberish text, watermark, logo, serif font, tilted card, 3D render.

## Fixes if a batch misses
- Reddit branding appears (alien, orange bar, the word reddit): open the prompt with "An original, unbranded discussion forum interface, not any real app."
- Numbers appear next to the arrows: add "The vote pill holds two arrow icons side by side with nothing between them."
- A word is misspelled: spell it letter by letter in the prompt ("enrichment, spelled E-N-R-I-C-H-M-E-N-T") and regenerate. After two failed batches, retype it (see the clean plate option).
- Lines break in the wrong places: keep the quoted line pairs, and add "each quoted line is one line of text".
- Card tilted or shown on a screen: add "perfectly front-on, flat on the violet ground, no device, no window, no tilt" at the start.
- Callout box gets text or a logo: add "the outlined box at the bottom is completely empty inside, with no text and no icons".
- Hex codes show up as text: delete the hex, keep the colour name, correct the colour in Photoshop.
- Extra replies or a second thread appear: add "exactly one post and one reply, nothing below the reply".
- Prompt A reply card doesn't overlap: add "the reply card covers the bottom fifth of the post card and hangs past its bottom edge".
- Glow turns neon: change it to "a barely visible lavender glow".
- Title too small: add "the post title is the largest text, each line about 5 percent of the frame height".

## Files
- `variants-thread-lift.png` and `variants-thread-flat.png`: the two layouts with the lockup and CTA in place, 1x. `@2x` versions at 2160x2160.
- `variants-thread-lift-ref@2x.png` and `variants-thread-flat-ref@2x.png`: the Higgsfield references, with no lockup and no CTA.
- `source/`: the HTML mocks and `thread.css`. Render with `.claude/skills/truvio-higgsfield-ad/scripts/render_mock.sh source/variants-thread-lift.html variants-thread-lift 1080x1080`.

## QA (mocks)
- Viewport 1080x1080 for all four renders.
- Light ink inside the 65px safe margin: 0 in all four.
- Ground #400685 at the clear sample point. The other two samples land on the card (#FFFFFF) and in the card's shadow falloff (#3F0583 in A, #3E0581 in B).
- Upvote ink #F76336 exactly, 188px.
- Title two lines, body two lines, answer two lines in both options. No widows.
- Prompt A: the reply card overlaps the post card by 201px and hangs 40px past its bottom edge. Reply to callout gap 36px.
- Fonts loaded: Be Vietnam Pro 400 and 800. No Arvo on this canvas, by design.
