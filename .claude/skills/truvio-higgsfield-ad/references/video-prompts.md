# Video prompts: rules and failure list

Learned from Seedance and Kling runs on the F&O Compliance campaign (Oct 2026). Every rule below comes from a clip that went wrong.

## Settings
- Model: Seedance 2.0, image to video, first frame + last frame. Kling is the backup.
- Duration: 5 seconds. The payoff lands by about 2.5 seconds, then it holds still. LinkedIn feed viewers leave fast, and a still tail stops the model rushing.
- Resolution: 1080p. Aspect ratio matches the frames. Seedance has no 4:5, so pad a 4:5 frame to 3:4 with ground colour and crop back in AE.
- Camera: locked off. Any camera move warps paper and letters.
- Sound: none needed. LinkedIn plays muted.

## The split: what Higgsfield makes, what After Effects adds
- Higgsfield makes the physical motion only: things falling, sliding, crumpling, settling.
- After Effects adds anything that has to be exact: stamps, stickers, badges, words, the headline, the lockup and the CTA line. Stamp hit recipe: scale 115 to 100 percent over 3 frames, a 2-frame position shake on the paper, and a grunge mask for ink.
- Plan a flat #400685 ground replacement in AE. AI grounds drift into a gradient.
- Write an AE timing table (time, frame, what happens) at the end of the file, so Grady can build it straight away.

## Frames
- Start and end frames contain no headline, logo, CTA or stamp. Text in a frame gets covered, redrawn and wobbles.
- Anything the first frame lacks gets faded in, not animated. If something must fly, fall or slide in, it has to sit in the first frame, outside its final position. Or start from an empty ground and accept that the model will invent the entrance.
- Build frames from the final comp layout with the copy band empty, so the video matches the static ad.
- If a frame needs regenerating (for example the object in flight), use Nano Banana Pro with the end frame attached and "Edit this image. Keep ... Change only its position and shape."

## Writing the prompt
- Open with "Locked-off camera, no camera movement" and the view (overhead, low three-quarter).
- Number every move in order, with a time, a position and an angle: "Drop one, at 0.3 seconds: the sheet tilted furthest to the left lands on the left side of the pile."
- Say which object comes last, and that it appears only once: "The centred top invoice appears only once, as the final drop. Nothing lands in the centre before it." Without this, the model gives the first move the most visible object in the end frame, then repeats it.
- Ceiling: about four distinct actions in three seconds. More than that, and the extras fade in.
- Overhead physics: a sheet falling toward a surface under an overhead camera starts large and soft near the lens and shrinks as it lands. It never slides across the frame (or across the copy band).
- Force solidity: "Every sheet is solid, opaque paper the whole time. No sheet fades in, turns see-through or appears without falling."
- End with "From X seconds, everything is completely still" and the exclusions: no hands, no people, no other objects, no camera shake, no cuts.
- Add a negative prompt where the model has one: text, letters, words, stamp, morphing, fading in, appearing, duplicate, extra objects, camera movement, zoom, shake, background colour shift, gradient, vignette, flicker, motion trails, slow motion, cartoon, plastic, logos.

## Failure list for reviewing a first pass
Check the contact sheets for each of these, and note the time it happens:

| Symptom | Usual cause | Fix |
|---|---|---|
| The hero object appears twice (lands early, then again at the end) | Only the last move was described | Name every move in order. The hero appears once, last |
| Objects fade in or turn see-through mid-move | Too many moves for the time, or the object isn't in the first frame | Fewer moves. Add the solidity line. Put the object in the first frame |
| Stamp or badge fades in, letters wobble | It was in the end frame but not the start | Clean frames. Stamp in AE |
| Objects slide over the headline or logo | Copy baked into the frames, entry from the frame edge | Remove copy from frames. Drop toward the surface, not across it |
| Final frame drifts from the hero | No still tail | "Everything is completely still for the final two seconds". Trim to the held frame |
| Ground turns into a gradient or shifts colour | Normal model drift | Key and replace with flat #400685 in AE |
| Camera creeps or zooms | Missing lock line | "Locked-off camera" at the start, camera moves in the negative prompt |
| Paper bends like cloth, unfolds or tears | Physics not stated | "Rigid real paper, real paper weight" |

Structural fallback when prompt fixes don't hold: start with some objects already in place (for example the bottom two sheets of a pile) and animate only the last moves. The model then has far less to invent.

## Animation idea format
For each idea: a name, how it improves the ad (the copy line it turns into motion), the start frame, the end frame, the prompt, fixes, and a loop option if it fits (for example a quick swipe from the held end back to the empty start).
