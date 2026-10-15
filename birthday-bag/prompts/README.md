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

## Round 1 log (2026-10-15)

Nano Banana 2.1 at 2K, 9 renders plus 1 background removal: 19 credits in total. Higgsfield rate-limited a batch of 9, so send at most 3–4 at a time.

| Style | P0 princess sheet | S1 giraffe | E1 forest plate |
|---|---|---|---|
| 1 knit | `80914c87-2e77-447f-b00c-7739ea8c3611` | `a1080f6d-3749-4b93-a7b5-e41e6cdfb722` (cutout `df49ba9e-6bda-42d3-8263-40046a21b7c4`) | `860b4afd-a92c-43cd-8dc5-45a1c03c0bc7` |
| 2 preschool | `54097501-16e2-402f-8634-9cb48ec984b6` | `dca02427-d75a-4f15-ab54-030b8c44a47b` | `dfb04a3d-9ab5-4754-80ed-e4da4d3c9de3` |
| 3 drawing | `f182bbdf-7580-47f9-a793-3fc527c8c00e` | `abd4c21a-c18e-46e9-96a5-dd86ca2835ad` | `5621f828-7ed4-40e5-a4c7-5a016cc0a486` |

These are Higgsfield job IDs. Pass the winning style's P0 job ID as a reference in round 2 so the princess stays consistent. The renders themselves are in `../private/round-1/`, which is git-ignored because the princess is based on our daughter's face.

Findings:
- **Knit:** the materials match the references closely and the giraffe is excellent. Her likeness is only moderate (closed, polite smile instead of the big cheeky grin). Higgsfield's background remover cuts the wool fuzz out cleanly.
- **Preschool:** the most readable and print-proof; the face is generic.
- **Drawing:** the closest likeness. The hatching is very fine (vendor line-width question matters), the forest plate is pale for a full-bleed bag, and the white dress has no colour.
