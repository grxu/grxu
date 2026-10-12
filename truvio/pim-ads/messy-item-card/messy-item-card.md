# Messy item card: layout mock

Truvio PIM LinkedIn single-image ad, 1:1 (1080x1080) and 4:5 (1080x1350). Split screen: the cluttered Business Central item card today on the left, the same card clean with the Truvio PIM Product View panel on the right. No Higgsfield plate. Grady chose to have the UI rebuilt as simplified flat UI from the existing BC and PIM screenshot (`source/reference-bc-pim.webp`).

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
- "wasn't built for this": the left card runs past its own bottom edge. Two columns of fields, a tiny scrollbar thumb on a long track.
- "Move enrichment into Truvio PIM": the four red fields on the left are custom enrichment fields (long text, specs, image links). On the right they are gone from BC and live in the PIM panel as assets.
- "sync back only what BC needs": the clean card keeps No., Description and Item Category Code in one roomy column.
- "messiest item": the hook and the left card carry it. The CTA invites the viewer to bring their own.

## Decisions (12 Oct 2026)
- UI source: rebuilt by hand from the screenshot, not generated. Higgsfield can't draw real BC or the PIM panel.
- CTA kept as briefed ("messiest item"), not "item card".
- Right side: the PIM panel floats in front of the clean card's right edge, with a Twilight (hex #9C9DEC) glow taken from the screenshot.
- Readable words: FastTab names (Item, Inventory, Prices & Sales, Replenishment), the fields No., Description and Item Category Code, the BC header, the item title, and the PIM panel's Add-in, Truvio PIM Product View, product name, Master, Assets, Product Details and EN. Everything else is a grey bar.
- Red fields: custom enrichment fields. Prometheus Red (hex #F76336) 2px outline with a 10 percent tint.
- Right label underline: secondary gradient at 25.4 degrees. Left label underline: Prometheus Red.

## Layout
- Ground Deep Violet (hex #400685), flat.
- Hook top left, Arvo Bold 66px in #E6E8FC, two lines.
- Labels at y 250, Be Vietnam Pro ExtraBold 22px.
- Left card x 65 to 525. Clean card x 555 to 885. PIM panel x 728 to 1015.
- Cards from y 300 to 153px above the bottom edge. 4:5 gets 270px more card height and more rows.
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
- `messy-item-card-1x1.pdf`, `messy-item-card-4x5.pdf`: vector, open in Illustrator. Text stays live. Shadows and the panel glow may come in as raster.
- `source/messy-item-card.html`: the mock. Render with `.claude/skills/truvio-higgsfield-ad/scripts/render_mock.sh source/messy-item-card.html <out> 1080x1350`.

## QA (both sizes)
- Viewport matches the canvas: 1080x1080 and 1080x1350.
- Light ink inside the 65px safe margin: 0.
- Ground #400685 at both clear sample points. The third sample lands on the left card.
- Red ink mode #F7683D against #F76336 (anti-aliasing on the 2px outline).
- Hook clears the labels by 42px. Cards clear the lockup by 30px.
- Fonts loaded: Slab 700, BVP 400, BVP 800.
