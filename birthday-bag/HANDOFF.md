# Handoff – Hanna's 3rd-birthday souvenir bag

**Written:** 2026-10-20. **Branch:** `claude/wonderful-ramanujan-a68g5y`. Read this file first, then `README.md`, `asset-list.md` and `prompts/style-4-storybook-forest.md`.

## The job

Grady and his wife are making a souvenir bag for their daughter **Hanna's** 3rd birthday party. The bag says **"Hanna is turning 3"**. The art is a Rapunzel-like princess based on Hanna, in a forest with animals. The **giraffe, elephant, capybara and horse** are must-haves; woodland friends (bunny, fox, deer, hedgehog, squirrel), birds and butterflies are extras.

The finished file is a **layered PSD on the vendor's template** (`template/TAMPLET_BOXY.psd`, 2050 × 1656 px at 200 ppi, 26 × 21 cm). The art runs full-bleed past the red cut line; the name, the "3", faces and the four key animals stay inside the blue safe line (about 22 × 17 cm). The vendor's guide layer must stay in the file. The same design goes on front and back; the side panels are plain fabric colour.

## Deadline

The **party is around Nov 1–3**. The vendor hasn't yet said how many days production takes, so treat **Oct 25–26** as the latest date for sending the final file, and chase the vendor answers (see below).

## Decisions locked (don't re-ask)

| Topic | Decision |
|---|---|
| Style | **Style 4, storybook** (`prompts/style-4-storybook-forest.md`): lineless, flat layered shapes with soft gradients, fine grain and halftone texture, soft light rim, chibi proportions. The knit, preschool and drawing styles are dropped. |
| Character sheet | **v7-a, Higgsfield job `65d6b0ff-e9e5-4815-9208-386a1cf73b99`.** Locked: don't edit it further. |
| Princess look | Based on Hanna's face. Straight black hair just below the shoulder blades; one thin braid with flowers hanging forward over her right shoulder to just above the sash; periwinkle and white flower crown; lilac puffed-sleeve dress with a white scalloped collar, a flower vine along the hem and tiny gold stars; rosy-pink sash with a bow at the back; barefoot. |
| Name | **Hanna**, exactly this spelling. Typeset as real type at the end; never put it in an image prompt. |
| Layout | A, dynamic. **A1 (Ring dance) vs A2 (Peekaboo forest) is still open**; see next step 1. |
| Bag | Same design front and back, full-bleed, plain side panels. |

### Known flaws in the locked sheet (accepted, don't fix)

- The back view shows loose hair with no braid (her braid hangs forward, so it's hidden from behind).
- The side view faces left.
- The front and three-quarter views were edited five times, so there's slight re-encoding wear.

Her bag poses are rendered fresh from this sheet, so none of this reaches the bag.

## Rules for Higgsfield (from Grady)

1. **Always confirm before rendering:** show the exact prompt, the attachments, the variant count and the credit cost, and wait for a yes. No exceptions.
2. **At most 2 variants per prompt.**
3. For a fix in one area, **use a mask** (`is_inpaint: true`, plus a `mask` media made with ImageMagick; white = repaint) instead of re-editing the whole image.
4. Submit batches of at most 3–4 at a time; Higgsfield rate-limits bigger batches.
5. **Never attach the watermarked style references** (Zhentengteng images, all marked "All rights reserved"): the model copies the watermark, and attaching them copies one artist's work. Describe the style in words; once a render is approved, use **our own renders** as style references.
6. Don't name artists in prompts.

**Model:** `nano_banana_2_1`, `resolution: "2k"` for work (about 2 credits per image; 4K is 3). Its media role for references is `image_references`, and `mask` for inpainting. **Balance at handoff:** 1,382.75 credits.

## Lessons from this session (avoid repeating)

- **Ask which views or areas feedback refers to.** "The braid is not fixed" meant *it's missing in the side and back views*. Three passes were wasted shortening it instead.
- **An attached reference passes on its line style.** To remove outlines or change the look, edit the image itself with an edit prompt ("remove every outline, keep everything else") rather than re-describing it next to a reference.
- **Each edit pass degrades the image a little.** Stop after 2–3 passes on one image and render fresh from the locked sheet.
- When checking a render, compare **every view** and zoom in before saying something is fixed.

## Privacy

- Hanna's photos and every render with her face live only in her parents' Higgsfield account and in `private/`, which is **git-ignored**, so it is **not in a new session's checkout**. Re-fetch renders by job ID; don't commit them or paste result URLs into the repo.
- Face photos in Higgsfield media: `d096a896-db46-4270-bc85-250f2562a510`, `74687f4c-0a6c-47ca-bfad-d4d006201161`.

## Next steps, in order

1. **Pick the layout.** Render the **E1 forest plate** in style 4 at 5:4 (prompt in `prompts/style-4-storybook-forest.md`), attaching the locked sheet `65d6b0ff…` as the style and texture reference. Mock A1 and A2 on the bag template, with rough cutouts of the princess sheet plus the forest, so Grady can choose. *Confirm before rendering.*
2. **Princess pose for the chosen layout:** A1, standing, leaning in and waving; or A2, sitting on a log and swinging her legs. Attach `65d6b0ff…` plus the face photos. Plain pale-mint backdrop, then Higgsfield `remove_background`.
3. **Animals:** S1–S11 from `asset-list.md` in style 4, poses per the chosen layout. Attach the approved forest plate or the sheet as style reference. Start with the four key animals.
4. **Props and foreground leaves** (E2, E3) as needed.
5. **Assemble in the PSD template:** layers for background, characters and text; keep the vendor guide layer; check the safe area. Typeset "Hanna is turning 3" in a rounded storybook face that matches the style (open-licence candidates: Fredoka, Baloo 2). Export the PSD plus a flattened PNG proof.
6. **Vendor:** Grady is still waiting on answers to `vendor-questions.md` (print method, finest printable line, production days, RGB/CMYK, 200 vs 300 ppi). The answers may change the export settings.

## Where things are

| Path | What |
|---|---|
| `README.md` | Specs, decisions, layout notes |
| `asset-list.md` | Every asset to render, per layout |
| `prompts/style-4-storybook-forest.md` | Style 4 prompts and the full log of princess passes v1–v8 with job IDs |
| `prompts/README.md` | Model, cost, workflow rules |
| `layouts/` | Layout wireframes (A, B, C, A1, A2) |
| `template/` | Vendor PSD, guide layer PNG, vendor sample |
| `vendor-questions.md` | WhatsApp-ready questions in Bahasa Indonesia |
| `private/` (git-ignored) | Face photos and renders; not in a fresh checkout |
