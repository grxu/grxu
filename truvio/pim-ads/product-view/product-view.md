# Product View: 1:1 comp

Truvio PIM LinkedIn single-image ad, 1:1 (1080x1080) only. A real screenshot of the Truvio PIM Product View open on the BC item card, with four arrows to images, PDFs, related products and variant thumbnails. No Higgsfield plate. Higgsfield can't draw real UI, and the brief asks for a real screenshot. This folder holds the layout comp with a drawn stand-in for the screenshot, the Illustrator files, and the screenshot spec for the product team.

## Launch blockers
- The screenshot. The product team hasn't supplied it yet. The spec and a message to send are below.
- The PIM landing page is still in progress. Until it ships, the ad links to https://truvio.com/products/business-central/pim. The messy item card file points to https://truvio.com/products/commerce/product-information-management. Settle on one URL before both ads run. Neither link was checked: truvio.com is blocked from the cloud session.

## Copy (final, for reference only)
- On design, hook: Everything about the product. Right on the item card.
- On design, arrow labels: Images / PDFs and spec sheets / Related products / Variant thumbnails
- On design, CTA: Click through it in a demo →
- Ads headline: Click through the Product View in BC
- Ads body: Images, PDFs, related products and variant thumbnails, right on the BC item card. Click through the Product View yourself in a demo.
- Link: https://truvio.com/products/business-central/pim for now. See the blockers above.

## How the image matches the copy
- "Everything about the product": one panel carries four kinds of product content, and each gets an arrow.
- "Right on the item card": the BC header bar and a strip of item card fields stay visible behind the panel. The viewer sees Business Central before reading a word.
- The four labels: each sits level with its row and names it. They carry the reading at feed size. UI text inside a screenshot won't read on a phone.
- "Click through it in a demo": the image shows the four stops, the CTA offers the clicks.

## Decisions (12 Oct 2026)
- No Higgsfield plate. The real screenshot is the hero. Arrows, labels, hook, CTA and lockup are comped by hand.
- One capture from the product team shows all four elements in one view. Spec below. If the product can't show them together, choose between a stitched composite (product team signs it off) and arrows on the Variants and Relations tabs.
- Size: 1:1 only, like the messy item card.
- Link: this brief's URL.

## Layout
- Ground Deep Violet (hex #400685), flat.
- Hook top left, Arvo Bold 62px in #E6E8FC, two lines. Down from the series' 66px: at 66px "Everything about the product." runs 995px wide and crosses the right margin. At 62px it ends 80px from the edge.
- BC item card x 65 to 690, y 262 to 872, in the house tint (#B9CDD8) from the messy item card ad. BC chrome on top: dark bar (#002B36) with "Dynamics 365 Business Central", teal (#0F7C8C) waffle.
- Product View panel in front at x 195 to 740, y 318 to 905 (545x587). It covers the card from 130px in, so the header and a strip of fields stay readable. It overhangs the card by 50px on the right and 33px at the bottom, like the product screenshot. Twilight (hex #9C9DEC) glow, as in the messy item card pop-up.
- Panel rows, top to bottom, in the brief's label order: images, PDFs and spec sheets, related products, variant thumbnails.
- Labels in a column from x 812, Be Vietnam Pro ExtraBold 30px in #E6E8FC. Each label is centred on its row.
- Arrows: Yellow Gold (hex #FFB310) 4.5px stroke over a 10px Deep Violet keyline. The keyline disappears on violet and outlines the tip where it lands on the white panel. Each tip touches the right edge of its row. All four run horizontal.
- Lockup bottom left at 176px wide. CTA bottom right, Be Vietnam Pro ExtraBold 24px, the series size. Try 28px if it reads small on a phone.

## When the real screenshot lands
- Replace the Screenshot_standin group. Keep the panel about 545px wide. Wider squeezes the label column, narrower loses the thumbnails on a phone.
- Crop to the panel plus a strip of item card on its left, with the "Dynamics 365 Business Central" bar readable. The full item card at 1080px shrinks the UI past reading.
- Move each label to its row's centre and each arrow tip to the row's right edge.
- If the capture's rows run in another order, reorder the labels to match the screenshot and keep the copy as written.
- Mask the capture's own shadow edge, then reuse the panel glow.

## Screenshot spec for the product team
One PNG of the Truvio PIM Product View open on a BC item card:
1. The item card visible behind or beside the panel, with the Business Central header bar.
2. In one view: 4 to 6 product images, at least one PDF spec sheet with a clear file name, 2 or 3 related products with photos, and 3 or more variant thumbnails that look different at a glance (colour variants work best).
3. Sample data only. A demo item with clean product photos on plain backgrounds, cleared for public use. No customer data and no third-party brand names. The current demo item is a Mongoose bike, a real brand.
4. No avatar in the BC header. The current screenshot shows a person's photo top right. No cursor, hover states, notifications or browser chrome.
5. 200% display scaling or browser zoom, so the panel is at least 1,100px wide in the file.
6. Light theme, English.

### Message to send
> Hi [name], I'm designing a LinkedIn ad for the Truvio PIM Product View. It needs a clean screenshot of the Product View open on a BC item card. Could you set one up with sample data?
>
> 1. One view showing product images, a PDF spec sheet, related products and variant thumbnails.
> 2. A demo item with clean product photos, cleared for public use. No customer data and no third-party brand names.
> 3. No avatar, cursor or notifications on screen.
> 4. 200% zoom or display scaling, light theme, English. A PNG is perfect.
>
> If those four can't show in one view, let me know and we'll find another way. When could you share it? Thank you!

## Brand check before you publish
- Swap Arvo Bold for Museo Slab in the hook. Check the first line still ends inside the 65px margin.
- The lockup is rendered from the official Truvio_logo_white.svg. Place the official asset anyway.
- BC chrome keeps its own dark bar and teal. They are off palette on purpose, so the card reads as Business Central.
- Readable words in the stand-in: Dynamics 365 Business Central, Item Card, Item, No., 10001, Description, Type, Blocked, Last Date Modified, Add-in, Truvio PIM Product View, Master, PDF and EN. Everything else is a grey bar. The real screenshot brings its own words. Proof them, and confirm the product name and file names with the product team.
- Stand-in thumbnails are drawn bikes, PDF icons and accessories. The screenshot replaces all of them.
- Fonts inside the UI are Be Vietnam Pro standing in for Segoe UI.

## Files
- `product-view-1x1.png`: the comp at 1x. `product-view-1x1@2x.png` at 2160x2160.
- `product-view-1x1-phone-390.png`: the comp at 390px, phone feed width, for the mobile check.
- `product-view-1x1.svg`: the editable Illustrator master. Named groups: Headline, Screenshot_standin (BC_item_card, Product_View, Sec_Images, Sec_PDFs, Sec_Related, Sec_Variants), Label_Images, Label_PDFs, Label_Related, Label_Variants, Arrows, CTA, Truvio_lockup. Live text set in MuseoSlab-700, BeVietnamPro-Regular and BeVietnamPro-ExtraBold. Vector lockup from the official SVG.
- `product-view-1x1.ai`: the same artwork as a PDF-based Illustrator file. Text is live with Arvo Bold standing in for Museo Slab. The two panel shadows are raster, everything else is vector.
- Neither the .svg nor the .ai carries Illustrator's private editing data. Open one, then Save As .ai once to get a native file.
- `source/product-view.html`: the mock. Render with `.claude/skills/truvio-higgsfield-ad/scripts/render_mock.sh source/product-view.html product-view-1x1 1080x1080 --accent FFB310`. Export with `.claude/skills/truvio-higgsfield-ad/scripts/export_svg.py source/product-view.html product-view-1x1 1080x1080`. Labels and arrows follow their rows automatically.

## QA
- Viewport matches the canvas: 1080x1080. Fonts loaded: Slab 700, BVP 400, BVP 800.
- Light ink inside the 65px safe margin: 0.
- Ground #400685 at both clear sample points. The third sample lands on the item card.
- Arrow ink mode #FEB210 against #FFB310, one level off on red.
- Hook ends 80px from the right edge and clears the BC bar by 63px. The widest label ends 86px from the right edge.
- The panel clears the lockup row by 52px. Its last row clears the panel's bottom edge by 29px.
- Phone check at 390px wide: hook 22px, labels 11px, CTA 9px, image thumbnails 27px. All four labels, the hook, the CTA and the BC header bar read. UI text inside the panel doesn't, as expected.
- SVG rendered back against the mock: mean difference 2.4 per pixel, 0.75 percent of pixels off by more than 60, all on antialiased edges.
- .ai fonts: Arvo Bold, Be Vietnam Pro ExtraBold and Regular, all embedded.
