# Higgsfield prompts

Everything is rendered separately (see `../asset-list.md`) and assembled on the template.

**Model:** Nano Banana 2.1 (Nano Banana Pro isn't in this Higgsfield account). It follows several reference images at once (style references plus the face photo), renders 5:4 natively and goes up to 4K. Attach the reference images listed in each prompt file.

- Round 1 at 2K: 2 credits per image, so 9 tests ≈ 18 credits.
- Finals at 4K: 3 credits per image.
- Fallback for cutouts: GPT Image 2.5 (quality *high*, background *transparent*, about 2.75 credits at 2K). Use it if wool fuzz or fine hatching doesn't cut out cleanly from a plain backdrop.

**Order:**
0. **Face reference:** 1–3 clear, front-facing photos of our daughter, attached to every princess render. Uploaded to Higgsfield only; never committed to this repo.
1. **Round 1, style test** (3 renders per style): princess character sheet, giraffe, forest plate. Compare the styles and pick one.
2. **Round 2, full set** for the winning style: the princess's poses for the chosen layout (A1 or A2), every animal, props. Attach the approved character sheet to every render.

**Settings:** 2K or 4K. Single assets at 1:1 or 3:4. The forest plate at 5:4 (or 4:3, then extend it to 5:4). Single assets go on a plain backdrop so the background can be removed cleanly in Higgsfield.

**Never in a prompt:** the name, the "3", or any text. Those are typeset at the end.
