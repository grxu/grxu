# Italy market entry: team pick for P1 and P2

The warm-up campaign for Truvio AP Automation in Dynamics 365 F&O in Italy. Four organic LinkedIn posts at 4:5 (1080x1350) drive traffic to the campaign page and build interest before the webinar. This round covers P1 and P2 in three variants, so the team can pick one. P3 and P4 follow in the chosen variant.

## Status
- Waiting on the team pick. The mocks sit on the "Team pick" page of the Design canvas: https://claude.ai/artifact/NbXDWBueeNsdmiZSUUXtiw. It is private. Share it from the page's Share menu before you send the link.
- The canvas's "Exploration" page keeps the earlier rounds: A dots, B arches and C (dictionary, inbox, autostrada, stamp, annotated invoice).
- Campaign page: https://truvio.com/truvio-ap-automation-for-finance-and-operations-in-italy

## Copy (from the brief, on design)
- P1 headline: Your AP is automated. / Or is it?
- P1 sub: See what 1,000 finance professionals revealed.
- P1 eyebrow: 2026 AP Automation Report
- P2 headline: Less invoice chasing. / More finance thinking.
- P2 sub: Put routine AP work on autopilot.
- P2 eyebrow: Dynamics 365 Finance & Operations

## The three variants
- V1 Dotted Italy. Every dot is an invoice. P1: the map is lit in the primary gradient, with three stuck invoices flagged by chips. P2: one route from Milano to Napoli with four numbered stops and a step card.
- V2 Autostrada. An Italian motorway sign with "AP" as the route number. P1: the route reads "Fattura registrata" and "Pagamento", and a yellow detour panel sends you to "Verifica manuale". P2: one clean sign, "Pilota automatico", lists the four steps with checks.
- V3 Map + motorway. The V1 map carries the V2 signs. P1: the AP route is lit from Milano to Roma, then turns grey after a detour sign at Roma. P2: the route is lit all the way to Napoli, ending at a "Registrazione" sign.

## Italian microcopy (needs a native check before launch)
- Verifica manuale: manual check
- In attesa di approvazione: awaiting approval
- Importo non corrispondente: amount does not match
- Acquisizione, Abbinamento, Approvazione, Registrazione: capture, matching, approval, posting
- Fattura registrata: invoice posted
- Pagamento: payment
- Deviazione: detour
- Pilota automatico: autopilot
- Automatico: automatic
- Fattura 0418: a dummy invoice number, not real data

## Build it in Illustrator
1. Keep `assets/` next to `build_italy_variants.jsx`.
2. In Illustrator: File > Scripts > Other Script, then pick `build_italy_variants.jsx`.
3. The closing alert lists any font it could not find and the stand-in it used.

What the script builds:
- One RGB document with six 1080x1350 artboards in a 2-column grid: V1-P1, V1-P2, V2-P1, V2-P2, V3-P1, V3-P2, each named.
- Layers: Guides (locked), Logo, Copy, UI chips, Signs, Map dots. Inside each layer, one named group per artboard, for example "V2-P1 Autostrada detour".
- Global process swatches: Deep Violet, Celestial Blue, Electric Green, Yellow Gold, Teal Meridian, Prometheus Red, Dark Gray, Silver, Truvio Black, Truvio White. Tints use them too, so a swatch edit carries through.
- A "Truvio Primary 25.4" gradient swatch (Deep Violet, Celestial Blue, Electric Green, Yellow Gold at 0, 34, 68 and 100).
- Map dots as compound paths. In V1-P1 the lit dots are one compound path with the live gradient across the whole map.
- Live text in MuseoSlab-700 and MuseoSlab-700Italic for headlines, and Be Vietnam Pro Regular, SemiBold, Bold and ExtraBold for the rest.
- 65px safe-margin guides on every artboard.
- The logo, placed from `assets/truvio-logo-violet.svg` at 160px wide.

## Brand check before you publish
- Gradient angle: the script sets 25.4 degrees in Illustrator's convention, as the guidelines state it. The HTML mocks used CSS 25.4deg, which runs much steeper. In Illustrator the V1-P1 map runs closer to left to right, from violet in the west to gold in the east. Check this against the guidelines before you lock it.
- Teal Meridian is a secondary colour. It leads the V2 and V3 signs, so they read as Italian motorway signs. Grady approved it for this campaign. Flag it to Jess at sign-off.
- Route dots in V1-P2, V3-P1 and V3-P2 carry fixed RGB blends between the stop colours, so they do not follow swatch edits. Everything else uses global swatches.
- The logo comes from the official `Truvio_logo_white.svg`, with the wordmark recoloured to Deep Violet for white grounds. The mark's gradient is untouched. Swap in the official colour lockup if one exists.
- Shadows are not built. Add native Drop Shadow by hand: chips 0px x, 6px y, 18px blur, Deep Violet at 12 percent. Step card 0, 12, 32 at 14 percent. Signs 0, 16, 36, black at 16 percent.
- The eyebrows are from the brief's post copy, not its graphic text. Confirm them with the copywriter.

## Files
- `build_italy_variants.jsx`: the Illustrator build. Plain ExtendScript, no plugins.
- `assets/truvio-logo-violet.svg`: the Deep Violet logo the script places.
- `source/make_dots.py` and `source/italy-ne50m.json`: rebuild the dot grid (Natural Earth 1:50m, public domain). The grid indices are pasted into the script and the mocks.
- `source/mock-render-contact-sheet.png`: the script's output, drawn by the test mock. Read it for layout only. The mock paints the gradient on each dot separately and uses Arvo for Museo Slab.

## QA
- The script parses, and it ran end to end against a Node mock of the Illustrator DOM: 6 artboards, 10 swatches, 6 layers, 2,338 objects, no errors.
- It has not run in real Illustrator yet. Check the first run for text baselines, since the script places point text by its bounding box.
- The mock render matched the HTML mocks. One fix came out of it: the V3 signs were too narrow for their labels, so both grew to 350px and 340px with 24px labels, in the script and on the canvas.
