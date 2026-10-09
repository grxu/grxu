# Prompt for the Claude app

Attach `every-bank-gif-handoff.zip` and paste everything inside the block below.

```text
I'm handing off the "Every bank" GIF for the Truvio F&O Compliance LinkedIn ads. The attached zip has everything made so far: the Higgsfield kit docs, all seven stills, the three plates, two paper cut-outs, all seven video clips (V1 to V7), a job log and the helper scripts. Every generation is done. What's left is assembling the 10-second GIF.

Start by unzipping it and reading, in this order:
1. HANDOFF.md: status, what changed from the kit, known issues per clip, and a suggested frame map.
2. higgsfield-refs/JOBS.md: every pick, its job ID and its frame notes.
3. higgsfield-video-bank-formats-gif.md: the "AE assembly", "GIF export" and "Brand check before export" sections.
4. higgsfield-prompt-bank-formats-gif.md: the "Layout (artboard 14 grid)", "Cast and colours" and "Timeline (12 fps)" sections.

Then do this:

1. Build a preview GIF in code, without copy or logo. Use Python and ffmpeg, or whatever you have. Follow the frame map in HANDOFF.md: 1080×1080, 12 fps, 120 frames, a loop. Handle every item under "Known issues to handle in assembly": the R-family 12px shift, the C0 slot patch on V7's early frames, V1 from f38 only, the V2 sliver, the V5 light streak and the V7 cut from f38 to f46. Use stills for every rest frame and composite the two banks during each slide. Export with the kit's ffmpeg palette settings and get it to 5 MB or under.

2. Check it against the kit's brand check. Ground #400685, same base line and centre line for all three banks, the same file in every flat frame, paper that moves like paper, no hands, no green, no red, no readable text. Show me the GIF, a contact sheet of all 120 frames and the file size. List anything that still looks off, with frame numbers.

3. Write an After Effects ExtendScript (.jsx) that builds the same comp: 1080×1080, 12 fps, 120 frames. It should import the files from the unzipped folder and lay out the plates, the file layers, the stills and the retimed clips, using the same frame map. Leave clearly named empty layers for the lockup and copy, which go at the artboard 14 positions. I'll finish in AE.

4. Ask me for the Truvio lockup PNG and the final copy layout. If I give you them, add them as static layers on top of every frame in the preview GIF too.

Rules:
- Use the question tool whenever you're unsure, and give me options with your recommendation first.
- Don't spend Higgsfield credits without asking me first. If a beat really needs a new generation, use the same settings as before: Kling 3.0, mode pro, 1:1, 3 s, sound off, batch 2. The prompt wording is in JOBS.md.
- Keep copy and logos out of anything AI-generated.
- Send me each deliverable as a file as soon as it's ready.
```
