# Messy item card: final 1:1

Truvio PIM LinkedIn single-image ad, 1:1 (1080x1080) only. Split screen of two square UI tiles: the cluttered Business Central item card today on the left, the same card clean on the right with the Truvio PIM Product View pop-up in front of it. No Higgsfield plate. Grady chose to have the UI rebuilt as simplified flat UI from the existing BC and PIM screenshot (`source/reference-bc-pim.webp`).

## Launch blocker
- The PIM landing page is still in progress. Until it ships, the ad links to https://truvio.com/products/commerce/product-information-management.

## Copy (final, for reference only)
- On design, hook: Your item card wasn't built for this.
- On design, left label: BC item card today
- On design, right label: With Truvio PIM
- On design, CTA: Bring your messiest item to a demo →
- Ads headline: Bring your messiest item card to a demo
- Ads body: Move enrichment into Truvio PIM and sync back only what BC needs. Bring your most overloaded item card to a demo and see it cleaned up.
- Link: PIM landing page (WIP), see the blocker above.

## How the image matches the copy
- "wasn't built for this": the left tile runs past its own bottom edge. Two columns of fields, a tiny scrollbar thumb on a long track.
- "Move enrichment into Truvio PIM": the red fields on the left are custom enrichment fields (long text, specs, image links). On the right they are gone from BC and live in the PIM pop-up as assets.
- "sync back only what BC needs": the clean card keeps No., Description and Item Category Code, nothing else.
- "messiest item": the hook and the left tile carry it. The CTA invites the viewer to bring their own.

## Decisions (12 Oct 2026)
- UI source: rebuilt by hand from the screenshot, not generated. Higgsfield can't draw real BC or the PIM panel.
- CTA kept as briefed ("messiest item"), not "item card".
- Format: two 460x460 square tiles, simple UI. One FastTab per side, no action bar.
- Final size: 1:1 only. The 4:5 version was dropped.
- PIM pop-up: floats in front of the right tile, 10px above its top edge and 22px below its bottom edge. It covers the right half of the clean card's fields. Twilight (hex #9C9DEC) glow from the screenshot. Five asset rows.
- Clean card under the pop-up uses the house tint (#B9CDD8) from the screenshot, so the pop-up is the focal point.
- Readable words: the BC header, Item Card, the Item FastTab, the fields No., Description and Item Category Code, and the pop-up's Add-in, Truvio PIM Product View, product name, Master, Assets and EN. The item title is a dark bar. Everything else is a grey bar.
- Red fields: custom enrichment fields. Prometheus Red (hex #F76336) 2px outline with a 10 percent tint.
- Label underlines: Prometheus Red on the left, the secondary gradient at 25.4 degrees on the right.
- CTA arrow drawn as a vector shape in #E6E8FC, sized to the Be Vietnam Pro ExtraBold text.

## Layout
- Ground Deep Violet (hex #400685), flat.
- Hook top left, Arvo Bold 66px in #E6E8FC, two lines.
- Labels and tiles sit as one block, centred between the hook and the lockup row. Labels Be Vietnam Pro ExtraBold 22px.
- Left tile x 65 to 525, right tile x 555 to 1015, both y 380 to 840. Pop-up x 715 to 1015, y 370 to 862.
- Lockup bottom left at 176px wide. CTA bottom right, Be Vietnam Pro ExtraBold 24px.

## Brand check before you publish
- Swap Arvo Bold for Museo Slab in the hook.
- The lockup is rendered from the official Truvio_logo_white.svg. Place the official asset anyway.
- BC chrome keeps its own dark bar (#002B36) and teal (#0F7C8C). They are off palette on purpose, so the card reads as Business Central. The pop-up uses Teal Meridian and Celestial Blue.
- The pop-up title, product name and Master tag come from the product screenshot. Check them with the product team before launch.
- Fonts inside the UI are Be Vietnam Pro standing in for Segoe UI.

## Files
- `messy-item-card-1x1.png`: final at 1x. `messy-item-card-1x1@2x.png` at 2160x2160.
- `messy-item-card-1x1.pdf`: vector, open in Illustrator. Text stays live, fonts embedded. Shadows and the glow may come in as raster.
- `source/messy-item-card.html`: the mock. Render with `.claude/skills/truvio-higgsfield-ad/scripts/render_mock.sh source/messy-item-card.html messy-item-card-1x1 1080x1080`.

## QA
- Viewport matches the canvas: 1080x1080.
- Light ink inside the 65px safe margin: 0.
- Ground #400685 at both clear sample points. The third sample lands on the left tile.
- Red outline samples #F76336 exactly at 2x. The 1x mode reads #F64B17, an artefact of the Lanczos downscale on a thin line.
- Hook clears the labels by 118px. The pop-up clears the lockup row by 95px.
- Pop-up rows clear its bottom edge by 22px. No clipped row.
- PDF fonts: Arvo Bold, Be Vietnam Pro Regular and ExtraBold, all embedded. No fallback font.
