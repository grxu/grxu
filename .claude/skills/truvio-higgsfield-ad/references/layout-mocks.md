# Layout mocks

Flat HTML mocks of the ad, rendered with headless Chrome at 2x. They show hierarchy, placement and how the hero reads at feed size. They also work as a layout reference in Higgsfield.

## Start
1. Make a `source/` folder in the ad's folder. Run `scripts/render_mock.sh --init <source-dir>`. It copies the kit fonts (Arvo, Be Vietnam Pro) and lockups from `ABOUT ME/truvio-brand/ad-render-kit/` and the base template `assets/mock-base.html`. When that folder isn't there (cloud sessions), it uses the copy bundled in `assets/render-kit/`. Its lockup is rendered from the official `Truvio_logo_white.svg`.
2. Copy `mock-base.html` once per option (`option-a.html`, `idea-1-pile.html`) and build the hero in the `.stage`. Shared styles go in one CSS file, so options stay consistent.
3. Render: `scripts/render_mock.sh <file.html> <out-basename> [1080x1080|1080x1350]`. It writes `<out>@2x.png` and `<out>.png`, prints the element boxes, and runs QA.

## Illustrator files
When Grady wants to finish a mock in Illustrator, run `scripts/export_svg.py <file.html> <out-basename> [WxH]`.
- It writes `<out>.svg`, the editable master, and `<out>.ai`, a PDF-based Illustrator file of the same artwork.
- Put `data-layer="Name"` on the parts that should become named groups (headline, labels, each hero, CTA, lockup).
- Text stays live and names fonts by PostScript name (MuseoSlab-700, BeVietnamPro-Regular, BeVietnamPro-ExtraBold), so Illustrator asks for the licensed fonts. The .ai embeds Arvo in place of Museo Slab.
- The lockup goes in as vectors when `assets/truvio-lockup-reversed.svg` sits next to the PNG.
- Shadows sit on their own `_shadow` shapes under each group, so the UI stays vector in the .ai.
- Check the printed diff against the mock and read the QA render it points to. Under 3 percent of pixels off is antialiasing.
- Neither file carries Illustrator's private editing data. Say so, and tell Grady to Save As .ai once to get a native file.

## Build rules
- Board: flat #400685, unless the brief says otherwise. Copy and lockup follow the campaign layout (look at earlier mocks in the folder). The default is the headline top left, two lines at most, Arvo Bold 66px #E6E8FC, with the lockup small at the bottom left, 176px wide.
- 65px safe margin on all sides. Nothing light crosses it.
- Build the hero from CSS and inline SVG: paper as white boxes with silver placeholder bars, a drop-shadow filter for flat-lay shadows, clip-path for folded corners. For ink texture, use an SVG filter (feTurbulence + feDisplacementMap for rough edges, a speck mask, a pressure mask) with mix-blend-mode multiply.
- Mock what you'll promise in the prompt (angles, positions, which end sits where). If the mock can't do it physically, fix the prompt.
- Keep the stamp bold. Specks should take out under 10 percent of the ink.

## QA, every render
- Read the PNG. Look at it, then squint at a 300 to 520px contact sheet of all options (`scripts/render_mock.sh` prints how to build one).
- `light ink inside the 65px safe margin: 0`.
- The ground sample reads #400685. If the sample point lands on the hero, say so instead of calling it a failure.
- Accent ink mode is within a few levels of its hex.
- Fonts loaded: check the printed list includes Slab 700.
- The hero clears the headline (at least 40px) and the lockup corner.

## Delivery note must say
- Mocks are drawn stand-ins for the Higgsfield output.
- Arvo Bold stands in for Museo Slab (licensed). Swap it in the comp.
- The reversed lockup is the kit's reconstruction. Use the official suitcase asset. (Skip this line when the mock used the bundled cloud kit, whose lockup is the official white logo.)
- Any new on-canvas word needs sign-off.
