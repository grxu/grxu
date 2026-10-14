# Inside BC chat: animated 1:1

Truvio PIM LinkedIn ad, 1:1 (1080x1080). An iMessage-style chat on black, after Grady's Conveyor reference. Sarah asks about a PIM, Tom answers with Truvio PIM. The Truvio lockup closes it.

## Deliverables
- `inside-bc-chat-1x1-30fps.mp4`: H.264, 1080x1080, 30fps, 18.3s.
- `inside-bc-chat-1x1-12fps.gif`: 1080x1080, 12fps, 256-colour palette, 220 frames, 18.3s, loops. GIF delays are in 1/100s, so frames repeat 8/8/9cs to average exactly 12fps.
- `inside-bc-chat-last-chat-frame.png`: the full chat just before the end card.

## Chat
- Sarah (Product Manager): IT wants us to get a PIM 😩 another system to learn
- Tom: Ours runs inside Business Central
- Sarah: Inside BC? Same screens, same roles?
- Tom: Same look, same permissions. It’s Truvio PIM
- Sarah: Ok, booking a demo 🚀

## Decisions (14 Oct 2026)
- Black background, like the reference. Sarah's bubbles dark grey (#2C2C2E), left. Tom's bubbles Celestial Blue (#008FC4), right. White text on both.
- No sender names. "Truvio PIM" stays plain text, no inline logo.
- Be Vietnam Pro Regular, 46px on a 60px line. Line breaks set by hand.
- Emoji from Noto Color Emoji (OFL). Apple's set isn't licensed for this use.
- Message 5 uses the Row 57 wording, "Ok, booking a demo 🚀".
- Five messages don't fit at this size, so the chat scrolls. Message 1 fades off under the top edge. The last frame shows messages 2 to 5.
- Motion: typing dots in the sender's colour, then the bubble pops from its tail corner with a small bounce.
- End: the chat holds 2.5s after the last message (1s longer than the first preview), fades, then the reversed Truvio lockup shows centred for about 2s.

## Timing (seconds)
| Message | Dots | Bubble |
|---|---|---|
| 1 | 0.4 | 1.4 |
| 2 | 3.4 | 4.3 |
| 3 | 6.1 | 7.0 |
| 4 | 8.8 | 9.9 |
| 5 | 12.0 | 12.8 |

Chat fades out 15.3 to 15.8. Logo fades in 15.9 to 16.5. End at 18.3.

## Layout
- 65px safe margin. Bubble tails sit inside it (bubbles start 89px in).
- Bubbles: 42px radius, 38px top and 56px side padding, 46px gap between messages.
- The view runs from y 110 to y 970, with a 70px fade at the top edge.
- Lockup 440px wide, centred.

## Editing and re-rendering
- `source/inside-bc-chat.html` holds the whole animation. Copy, line breaks and timing sit in `MESSAGES` at the top of the script. Colours sit in `:root`.
- Open the HTML in Chrome to watch it loop.
- `source/render.js` writes PNG frames: `CHROME_PATH=<chromium> node render.js <outdir> 30`. It needs playwright-core. Then encode with ffmpeg.
