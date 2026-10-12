# Messy item card: layout mock

Truvio PIM LinkedIn single-image ad, 1:1 (1080x1080) and 4:5 (1080x1350). Split screen of two square UI tiles: the cluttered Business Central item card today on the left, the same card clean with the Truvio PIM Product View panel docked on the right. No Higgsfield plate. Grady chose to have the UI rebuilt as simplified flat UI from the existing BC and PIM screenshot (`source/reference-bc-pim.webp`).

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
- "Move enrichment into Truvio PIM": the red fields on the left are custom enrichment fields (long text, specs, image links). On the right they are gone from BC and live in the PIM panel as assets.
- "sync back only what BC needs": the clean card keeps No., Description and Item Category Code, nothing else.
- "messiest item": the hook and the left card carry it. The CTA invites the viewer to bring their own.

## Decisions (12 Oct 2026)
- UI source: rebuilt by hand from the screenshot, not generated. Higgsfield can't draw real BC or the PIM panel.
- CTA kept as briefed ("messiest item"), not "item card".
- v2 (12 Oct 2026): simpler UI in two square tiles, per Grady. Each tile is 460x460. The PIM panel docks inside the right tile, the way the real add-in docks, with a Twilight (hex #9C9DEC) edge. One FastTab per side, three asset rows, no action bar.
- Readable words: the BC header, Item Card, the Item FastTab, the fields No., Description and Item Category Code, and the PIM panel's Add-in, Truvio PIM Product View, product name, Master, Assets and EN. The item title is a dark bar. Everything else is a grey bar.
- Red fields: custom enrichment fields. Prometheus Red (hex #F76336) 2px outline with a 10 percent tint.
- Right label underline: secondary gradient at 25.4 degrees. Left label underline: Prometheus Red.

## Layout
- Ground Deep Violet (hex #400685), flat.
- Hook top left, Arvo Bold 66px in #E6E8FC, two lines.
- Labels and tiles sit as one block, centred between the hook and the lockup row. Labels Be Vietnam Pro ExtraBold 22px.
- Left tile x 65 to 525, right tile x 555 to 1015. 1:1 tiles at y 380 to 840. 4:5 tiles at y 515 to 975.
- The tiles keep their size in 4:5, so 4:5 carries about 135px more violet above and below the block.
- Lockup bottom left at 176px wide. CTA bottom right, Be Vietnam Pro ExtraBold 24px.

## Brand check before you publish
- Swap Arvo Bold for Museo Slab in the hook.
- The lockup is rendered from the official Truvio_logo_white.svg. Place the official asset anyway.
- The CTA arrow (→) falls back to a system font. Be Vietnam Pro's web subset lacks it. Set it in the full font.
- BC chrome keeps its own dark bar (#002B36) and teal (#0F7C8C). They are off palette on purpose, so the card reads as Business Central. The PIM panel uses Teal Meridian and Celestial Blue.
- The PIM panel title, product name and Master tag come from the product screenshot. Check them with the product team before launch.
- Fonts inside the UI are Be Vietnam Pro standing in for Segoe UI.

## Files
- `messy-item-card-1x1.png`, `messy-item-card-4x5.png`: 1x renders. `@2x` versions for zoom.
- `messy-item-card-1x1.pdf`, `messy-item-card-4x5.pdf`: vector, open in Illustrator. Text stays live. Shadows may come in as raster.
- `source/messy-item-card.html`: the mock. Render with `.claude/skills/truvio-higgsfield-ad/scripts/render_mock.sh source/messy-item-card.html <out> 1080x1350`.

## QA (both sizes)
- Viewport matches the canvas: 1080x1080 and 1080x1350.
- Light ink inside the 65px safe margin: 0.
- Ground #400685 at both clear sample points. The third sample lands on the left card.
- Red outline samples #F76336 exactly at 2x. The 1x mode reads #F64B17, an artefact of the Lanczos downscale on a thin line.
- 1:1: hook clears the labels by 118px. Tiles clear the lockup by 117px.
- PIM rows clear the tile bottom by 68px.
- Fonts loaded: Slab 700, BVP 400, BVP 800.
