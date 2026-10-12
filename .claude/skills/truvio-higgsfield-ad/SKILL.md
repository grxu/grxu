---
name: truvio-higgsfield-ad
description: Turn a final-copy Truvio ad brief into Higgsfield prompts Grady can paste - image prompts (Nano Banana Pro, Soul) for a full layout or a hero-only plate, alternative hero concepts with flat HTML layout mocks, animation prompts for Seedance or Kling (first and last frame), and a v2 prompt after reviewing a first-pass Higgsfield clip frame by frame. Use it whenever Grady briefs an ad formula, ad concept or LinkedIn ad visual and wants a Higgsfield, Nano Banana, Seedance or Kling prompt, asks for other ideas or mocks for an ad, wants an ad animated, or drops a Higgsfield mp4 and asks how to fix it - even if he doesn't say "Higgsfield". Not for rendering the finished square ad PNG (truvio-square-ad) or building the After Effects scene (ae-script-copycat).
---

# Truvio Higgsfield ad

Grady designs Truvio's LinkedIn ads. The copy arrives final. He composes the headline, the lockup and the CTA line himself, and uses Higgsfield to make the picture underneath. This skill writes the prompts he pastes into Higgsfield, the mocks that show what they should produce, and the fixes when a generation misses.

AI output is his first draft, never the final. The job is to give him a plate he can comp, not a finished ad.

## Before anything

Read these, every run. They hold the brand, the voice and the rules this skill leans on:
- `~/Documents/Truvio CoWork/ABOUT ME/brand-spec-cache.md` (palette, fonts, 65px safe margin)
- `~/Documents/Truvio CoWork/ABOUT ME/anti-ai-writing.md` (the voice for every file and reply)
- `~/Documents/Truvio CoWork/ABOUT ME/about-me.md` (what Grady rates and hates)
- The project memory index, if one is loaded. It holds campaign decisions (stamp colours, approved exceptions, blockers) you shouldn't re-ask.

In a cloud session (Claude Code on the web, working in the `grxu` repo) the `ABOUT ME` folder isn't there. Load the `truvio-work` skill instead. It carries the same brand spec, voice rules and what Grady rates. Earlier campaign files live in the repo under `truvio/`.

Then look in the ad's project folder for earlier prompt files from the same campaign. Match their format and carry over decisions already made. Don't reread unrelated `OUTPUTS/` folders.

## The five jobs

Work out which job Grady is asking for. Often it's one, sometimes a chain (prompt, then mocks, then animation, then review).

1. Intake check, always first
2. Concepts and mocks, when he asks for ideas, options or "a mock"
3. Image prompt file
4. Animation prompts
5. First-pass review, when he sends a clip or image from Higgsfield

### 1. Intake check

Pressure-test the brief before writing. The copy is final, so never rewrite it. Your job is to catch problems the copy owner can't see. Raise them in one AskUserQuestion call, with the most likely answer first:

- **Copy that belongs to another ad.** Briefs get pasted from older ones. If an on-design line doesn't fit the formula or the product, ask whether it's a paste error. (Example: a Production Planning headline turned up in an invoice compliance brief.)
- **Off-palette colours.** Check every hex against the brand palette and the house off-whites #E6E8FC and #F8F9FE. If one isn't there, name it and offer the nearest brand colour that fits the message. In the Document Stamp series: Prometheus Red #F76336 for problem stamps, Electric Green #2DB34A for good-news stamps.
- **New words on the canvas.** Anything you'd add to the image that isn't in the copy (a stamp word, a tag, a button) is new copy. Ask before adding it.
- **What Higgsfield makes.** Full plate with empty space for the copy, or hero only? The headline, lockup and CTA are never generated. AI distorts logos and can't set Museo Slab or Arvo.
- **Sizes.** Usually 1:1 (1080x1080) and 4:5 (1080x1350).

If the brief is complete and nothing conflicts, say so in one line and move on.

### 2. Concepts and mocks

When Grady asks for other ideas, give 3 to 5 heroes. Each one gets a name, a one-line description, the copy line it makes visible, and its risk. Recommend one and say why. Tie every idea to a specific word in the copy, so it drives consideration and isn't just a nice picture.

Mocks are flat HTML layouts rendered with headless Chrome. They show hierarchy and placement, not the final photographic look. Say so in the delivery note. Read `references/layout-mocks.md` for the build and QA steps, and use `scripts/render_mock.sh`.

Mocks pull double duty. Attached in Higgsfield as a layout reference, a flat mock locks the composition. An earlier render attached as the reference makes Nano Banana treat the job as an edit and ignore layout changes in the text.

Build the mock before you finalise any spatial claim in a prompt. In the first Document Stamp prompt, "the stamp rises from lower left to upper right, its right end over the totals block" turned out to be impossible. The totals sat bottom right. The mock caught it.

### 3. Image prompt file

Write one markdown file per ad in the ad's folder, named `higgsfield-prompt-<ad-name>.md`. Follow the structure in `references/image-prompt-file.md`. In short: copy for reference, how the image matches the copy, direction and decisions, settings, prompts per size, brand check, avoid list, fixes.

How Higgsfield prompts work best:
- One dense paragraph per prompt, written as a photograph: what the object is made of, how it's lit, the camera and lens, the surface, where it sits. Premium editorial still life beats "3D render" for this brand.
- Colours as a plain name plus the hex in brackets, for example "deep violet (hex #400685)". If hex codes show up as text in the image, the fix is to drop them and correct the colour in Photoshop.
- Control text hard. Name the only readable words ("The only readable words in the image are INVOICE and REJECTED"). Make every other line a grey placeholder bar, with no readable words or numbers. Small text turns into gibberish.
- Give the layout in percentages per size, and name the empty zones ("The top 30 percent of the frame is empty violet, reserved for a headline"). Keep the hero clear of the lockup corner.
- End with exclusions: no logos, no hands, no props, nothing else in the frame.
- Model: Nano Banana Pro for objects, graphics, paper and short words. Soul 2.0 for candid documentary photos of people (it garbles type). Run each size separately, at 2K with a batch of 4. If 4:5 is missing, use 3:4 and trim 90px.
- Hero-only plates: centre the object on a flat ground at about 65 percent of the frame width, with wide margins, so it scales into both sizes.

### 4. Animation prompts

Read `references/video-prompts.md` before writing any video prompt. It holds the lessons from every clip that went wrong. The core of it:
- Seedance 2.0 in first-and-last-frame mode, with Kling as the backup. Lock the camera.
- **Anything the first frame lacks gets faded in, not animated.** So stamps, stickers, badges and any letters go in After Effects on an exact frame. Generate clean motion, then slam the stamp in AE.
- Keep the headline, logo and CTA out of the start and end frames. Add them back in the edit.
- Name every move in order, with a time, a position and an angle. Say which object lands last and that it appears only once.
- Fewer moves than you think. About four distinct actions in three seconds is the ceiling.
- Hold the end still for about two seconds, so the clip lands on the hero.

Every animation idea starts with why it improves the ad: the copy line it turns into motion.

### 5. First-pass review

When Grady sends a Higgsfield clip, look at it. Never guess from the description. Run `scripts/clip_frames.sh <video>` to get a full contact sheet and a zoomed sheet of the first seconds, then Read both images. Compare what you see against the failure list in `references/video-prompts.md`. For a still image, Read it and check it against the brand check in the prompt file.

Then append a `### v2 after the first pass (<date>)` section to the existing prompt file, under the prompt it fixes. It covers:
- What went wrong, with timestamps, and why the model did it.
- What v2 changes.
- The v2 prompt and any changed start or end frames.
- Fixes for v2, including a structural fallback (for example, start with some objects already in place).

If your own earlier prompt or fix note caused the problem, say so plainly and correct it in the file.

## Delivering

- Save everything in the ad's folder inside `OUTPUTS/<campaign>/`. Prompt files go there, mocks go there as PNGs with `source/` for the HTML.
- In a cloud session, the ad's folder is `truvio/<campaign>/<ad-name>/` in the repo. Commit and push when you deliver. The container is wiped when the session ends.
- Send mocks with SendUserFile, rendered. When Grady asks for an Illustrator file, use `scripts/export_svg.py` (see `references/layout-mocks.md`).
- Keep the reply short, written to `anti-ai-writing.md`. Cover what you made, any departure from the brief and why, what Grady must fix before publishing (font stand-ins, reconstructed lockup, new copy needing sign-off), and what you verified, with numbers.
- Save decisions Grady made (colour swaps, approved exceptions, chosen direction) to project memory, so the next run doesn't ask again.

## Formula-specific notes

- Document Stamp (a document with a rubber-stamp verdict): `references/document-stamp.md`.
- Other formulas: follow the earlier prompt files in the campaign folder. If you learn something that would help next time, offer to add a reference file for that formula.
