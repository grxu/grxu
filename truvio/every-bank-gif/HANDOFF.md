# Handoff: Every bank GIF, after generation (2026-10-09)

Every Higgsfield generation is done. What's left is the assembly and the GIF export (Part 6 of the run order). Read this first, then `higgsfield-refs/JOBS.md` for the detail on every pick.

## Status
| Part | Steps | State |
|------|-------|-------|
| 1. Stills | 1 to 7 | Done. T0, T1, T2, C0, C2, R0, R2 |
| 2. Paper clips | 8 to 10 | Done. V1 (hybrid, see below), V4, V7 |
| 3. Photoshop prep | 11 | Done in code. Plates and cut-outs, see below |
| 4. Slide clips | 12 to 15 | Done. V2, V3, V5, V6 |
| 5. Optional V8 | 16 | Skipped. Only if the GIF has room under 5 MB |
| 6. Into AE, GIF export | | **Next** |

Credits spent: 146.5. Higgsfield balance at handoff: 352.25.

## What changed from the kit
- **Video model: Kling 3.0, not Seedance 2.0.** Grady chose it. Settings on every clip: `kling3_0`, mode `pro` (the 1080p tier), 1:1, 3 s (Kling's shortest), sound off, batch 2. No negative-prompt field, so the kit's negative prompt was left out. Clips come back at 1440×1440, 24 fps, 73 frames.
- **Batch 2 on every generation** after T0. Grady's rule.
- **Prompt additions.** Several stills needed an extra line or two. The exact wording is in `JOBS.md` under each step: T2 (pleat mostly inside the slit), C2 (open slot, size lock, crisp paper), R2 (short stub), T1 (position lock).
- **C2 was redone** with crisp paper after the first V7 run turned the sheet into cloth. The C2 sheet is about 2× the size of the original sheet.
- **V1 is a hybrid.** Kling never folded the paper crease by crease; it snaps from flat to pleat. Grady chose: T0's flat sheet, then T1's half-fold, then V1 from its source frame 38 on (the pleat turning and stepping into the slit). Nothing before f38 is used.
- **Plates and cut-outs were made in code**, not Photoshop: `tools/make_plates.py`. plate-R is nudged up 12px (at 2048) so its base sits on the tower's line. plate-C has the solid yellow slot opened into a dark recess.

## Files
All stills are 2048×2048 and line up with T0. All clips are 1440×1440 at 24 fps, 73 frames.

In this handoff zip the stills are high-quality JPEGs (`.jpg`) so the zip fits the upload limit. The cut-outs stay PNG (they carry alpha), and the clips are the originals. The lossless PNG stills are in the repo, `truvio/every-bank-gif/higgsfield-refs/`, on branch `claude/sleepy-knuth-bhx46w` of `grxu/grxu`.

| File | What it is |
|------|------------|
| `T0` `T1` `T2` | Tower: file flat, file half-folded (fallback), file pleated in the slit |
| `R0` `R2` | Rotunda: file flat, file rolled in the porthole |
| `C0` `C2` | Classical: file flat, file jammed in the letterbox (crisp redo) |
| `plate-T` `plate-R` `plate-C` | The three banks with the sheet removed. Start frames of the slides and the base for the file layer |
| `file-flat.png` | T0's flat sheet plus contact shadow, transparent, full frame. Over plate-T it gives back T0 |
| `file-fold.png` | T1's half-folded sheet plus floor shadow, transparent, full frame. Cut against plate-T |
| `V1.mp4` | Tower fold and in. Use from source f38 only |
| `V2.mp4` | Tower out to the left |
| `V3.mp4` | Rotunda out to the right. Reverse it, so it enters |
| `V4.mp4` | Rotunda roll and in |
| `V5.mp4` | Rotunda out to the left |
| `V6.mp4` | Classical out to the right. Reverse it, so it enters |
| `V7.mp4` | Classical jam, the payoff |
| `JOBS.md` | Every pick and reject, job IDs, prompt changes, frame notes |
| `tools/make_plates.py` | Rebuilds the plates and cut-outs from the stills |
| `tools/clipcheck.py`, `tools/slidecheck.py` | Contact sheets and drift checks for clips |

## Known issues to handle in assembly
- **R-family is 12px low.** plate-R is nudged up 12px at 2048 (about 8px at 1440, 6px at 1080). R0, R2 and V4 are not. Shift every R0, R2 and V4 frame up by the same amount so the rotunda doesn't jump between slides and the roll. V3 and V5 were made from plate-R, so they already match.
- **C0's slot is solid yellow; plate-C's is open.** V7 starts from C0, so its first frames show the yellow panel, and the slot goes dark once the paper arrives (C2 has an open slot). Patch the slot from plate-C over V7's early frames with a soft mask, or accept the change at the moment the paper goes in.
- **V1:** use f38 to f72 only. f38 starts with the finished pleat hovering left of the slit, so the cut from T1's half-fold is one stop-motion step.
- **V2:** a thin sliver of the tower is still on the left edge at the last frame. Cut from it to the empty floor.
- **V5:** the rotunda is gone by f68, but a faint lavender light streak stays on the floor. Fade it, or cut to the empty floor.
- **V7:** the sheet jumps to the bigger C2 size between f38 and f40, and there's a small glitch in the slot at f44. Cut from f38 straight to f46.
- **Copy and lockup are not in this package.** They come from artboard 14 of the F&O Compliance Illustrator file. Ask Grady for a lockup PNG and the copy layout, or leave them as static layers to add in AE.

## Suggested frame map (12 fps, 120 frames)
A starting point that follows the kit's timeline (`higgsfield-prompt-bank-formats-gif.md`, "Timeline"). Source frames are at 24 fps. Adjust by eye. Each GIF frame is one stop-motion step.

| GIF frames | Bank | Source |
|------------|------|--------|
| 0 to 5 | tower | plate-T + file-flat (identical to T0) |
| 6 to 9 | tower | plate-T + file-fold (the half-fold) |
| 10 to 21 | tower | V1 f38 → f71, every 3rd source frame |
| 22 to 23 | tower | T2 (hold) |
| 24 to 25 | tower | pop-back: V1 f60, then f44 (pleat backing out) |
| 26 to 33 | tower out, rotunda in | V2 f24 → f72 (tower leaving, about every 7th frame) with V3 reversed f66 → f12 (rotunda entering, ends on its little rock), both keyed onto the floor |
| 34 to 37 | rotunda | plate-R + file-flat |
| 38 to 55 | rotunda | V4 f28 → f62, every 2nd source frame, shifted up (see above) |
| 56 to 57 | rotunda | pop-back: V4 f50, then f40, shifted up |
| 58 to 65 | rotunda out, classical in | V5 f24 → f68 with V6 reversed f72 → f9, both keyed |
| 66 to 69 | classical | plate-C + file-flat |
| 70 to 95 | classical | V7 f12 → f38, then f46 → f72, every 2nd source frame, slot patched until the paper arrives |
| 96 to 119 | classical | C2 (the jam hold). Optional: the kit's 1-frame jolt and nudge in the hold |

The loop is a hard cut from 119 back to 0.

Two clips run at once during each slide (26 to 33, 58 to 65). Key each one against the floor so both banks show: the kit keys every clip onto a flat #400685 solid with the soft shadows kept. If that loses the lavender floor pool, composite over the outgoing plate's floor instead.

## Export and checks
Follow `higgsfield-video-bank-formats-gif.md`: "GIF export" (ffmpeg palette + gifsicle, 5 MB cap and the fallback order) and "Brand check before export". The targets are 1080×1080, 12 fps, 120 frames, a loop, 5 MB or under. Keep noise down: hold stills for every rest frame, and run a light median on the clip frames.
