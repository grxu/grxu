# After Effects build: Variants thread animation

Build brief for a Claude session that writes an ExtendScript (`.jsx`). Grady runs the script in After Effects on his Mac, and it builds the whole animation: comp, layers, keyframes, render queue item. Claude can't open AE, so the script has to be right from the specs below, and Grady checks the result against the animatic.

Ad: Truvio PIM LinkedIn video ad, 1:1, 1080x1080, 14 seconds, 30 fps, no sound. The animation plays out the forum thread from the static ad, and the final 4 seconds hold on a frame that matches the static flat layout pixel for pixel.

## Start here
1. Watch `animation/variants-thread-animatic.mp4`. It is the target. Every move in it comes from the same data file the AE script will read.
2. Look at `animation/storyboard.png` for the 16 beats at a glance.
3. Read this file to the end, then write `animation/variants-thread-build.jsx`.
4. Keyframe data: `animation/vt-data.js`. It holds `var VT = {...};`, so the script loads it with `$.evalFile()`. Never retype its numbers.
5. Static reference for the hold frame: `variants-thread-flat.png` (1080x1080) and `variants-thread-flat-1x1.svg` (exact geometry, live text).

## Files
All paths are relative to `truvio/pim-ads/variants-thread/`.

| File | What it is |
|---|---|
| `animation/variants-thread-animatic.mp4` | The motion target, rendered from the HTML animatic |
| `animation/storyboard.png` | 16 frames with times and beat names |
| `animation/vt-data.js` | All keyframes: UI tracks, 288 tiles, AE path data for every icon |
| `animation/build_data.py` | Generates `vt-data.js` and `callout-gradient.png`. Fixed seed, so reruns give the same data |
| `animation/callout-gradient.png` | 1080x1080 plate of the callout's secondary gradient at 25.4 degrees. Used through a track matte |
| `animation/animatic.html` | The HTML animatic. `renderAt(seconds)` draws any frame |
| `animation/render_animatic.mjs` | Renders the animatic to MP4 with Playwright and ffmpeg |
| `source/assets/truvio-lockup-reversed.png` | Reversed lockup, 1170x387, rendered from the official white SVG |
| `variants-thread-flat.png` | The static ad. The final frame must match it |
| `variants-thread-flat-1x1.svg` | The static ad as SVG, exact positions |

## Why the motion improves the ad
Every beat turns a line of copy into something the viewer sees happen.
- "How are you handling complex variants in Business Central?": the hook is on screen from frame 0. Nothing covers it, ever.
- "One product, 12 sizes, 8 colors, 3 materials": a red underline marks the numbers, then the variants multiply out of that line. 12 size chips, times 8 colours, times 3 materials, 288 tiles. The viewer watches the count explode.
- "Our item setup is falling apart": the matrix breaks apart, falls and piles up in a heap. The post card shudders as it lands.
- "We moved variants and enrichment into Truvio PIM": the answer types on. Right after Truvio PIM is on screen, the heap lifts and sorts itself into an ordered grid.
- Upvoted top answer: a cursor clicks the upvote, the arrow fills red with a small burst, and the Top answer tag pops on.
- "syncs back only what BC needs": the grid collapses left to right into the callout outline, which draws on as the tiles reach it.
- "Test your hardest variants in a demo →": the lockup and CTA slide in. The arrow nudges twice during the hold.

## Decisions (14 Oct 2026)
- Built in After Effects by script. No Higgsfield. AI video warps letters, and this ad is 45 words of exact copy.
- Flat layout throughout. The answer never lifts out.
- Full scope: thread plus the variant explosion. 14 seconds.
- A plain pointer cursor clicks the upvote. Approved.

## New elements on the canvas (need sign-off before launch)
- The pointer cursor (approved), the three typing dots, the red underline under the numbers, the 288 variant tiles and the six-ray burst. None of them carries words or numbers.
- The tile colours include two accent colours, Twilight (#9C9DEC) and Celestial Bloom (#E19CEC). The brand spec allows accents on screen in limited use. They appear for under 8 seconds and are gone from the hold frame.

## Comp
- Name `Variants_thread_1x1`, 1080x1080, square pixels, 30 fps, 14:00 (420 frames).
- Background: a solid layer `BG` in Deep Violet #400685, full frame. Don't rely on the comp background colour, which doesn't render into every format.
- Motion blur: on for the comp, shutter angle 180. Switch it on for the 288 tiles and the cursor only.
- Coordinates in this file and in `vt-data.js` are comp pixels, origin top-left, y down. Text positions are the left end of the baseline.

## Fonts
- Be Vietnam Pro Regular and ExtraBold, PostScript names `BeVietnamPro-Regular` and `BeVietnamPro-ExtraBold`. Free on Google Fonts. The script checks both are installed and stops with a clear alert if not.
- No Museo Slab in this ad. The post title is set as forum UI.

## Layer stack, top to bottom

| # | Layer | Type | Parent | Notes |
|---|---|---|---|---|
| 1 | Cursor | Shape | none | Motion blur on |
| 2 | Burst | Shape | none | Origin at (160, 721.28) |
| 3 | Tile_s01_c1_m1 ... Tile_s12_c8_m3 | Shape, 288 layers | none | Motion blur on. Order as in `VT.tiles` |
| 4 | Callout_gradient | Footage `callout-gradient.png` | none | Alpha track matte: Callout_outline |
| 5 | Callout_outline | Shape | none | Matte layer for 4, two open paths |
| 6 | CTA_arrow | Shape | CTA | |
| 7 | CTA | Text | none | |
| 8 | Lockup | Footage PNG | none | |
| 9 | Underline | Shape | Card_null | |
| 10 | Dot1, Dot2, Dot3 | Shape | Card_null | |
| 11 | Upvote_fill | Shape | Upvote_null | |
| 12 | Upvote_outline | Shape | Upvote_null | |
| 13 | Upvote_null | Null | Card_null | Anchor and position (160, 721.28) |
| 14 | Answer_pills | Shape | Card_null | Both pills, the down arrow and the bubble |
| 15 | Answer_l2, Answer_period, Answer_bold, Answer_l1 | Text | Card_null | |
| 16 | Tag_text, Tag_pill | Text, Shape | Tag_null | |
| 17 | Tag_null | Null | Card_null | Anchor and position (354.92, 565.75) |
| 18 | Answer_user | Text | Card_null | |
| 19 | Answer_avatar | Shape | Card_null | Anchor and position (151, 565.75) |
| 20 | Answer_bg | Shape | Card_null | |
| 21 | Post_pills | Shape | Card_null | Pills and icons of the post |
| 22 | Body_line2, Body_line1 | Text | Card_null | |
| 23 | Title_line2, Title_line1 | Text | Card_null | |
| 24 | Meta_user, Meta_dot, Meta_comm, Meta_icon | Text, Shape | Card_null | |
| 25 | Card_bg | Shape | Card_null | Two Drop Shadow effects |
| 26 | Card_null | Null | none | Anchor (0, 0), position (0, 0). Carries the shudder |
| 27 | BG | Solid #400685 | none | |

Parenting rules:
- Every null gets anchor and position set so children keep comp coordinates. Card_null sits at (0, 0) with anchor (0, 0). A pivot null (Upvote_null, Tag_null) has anchor and position on the same point.
- Parenting passes position, scale and rotation, never opacity. Where a track fades a group, key the opacity on every member layer. Tag.opacity goes on Tag_pill and Tag_text. CTA.opacity goes on CTA and CTA_arrow.

## Static geometry
Shape layers for the UI keep layer position (0, 0) and anchor (0, 0), and draw their contents in comp coordinates. The exceptions are layers that scale or rotate, which say "drawn around the origin".

### Card
- Card_bg: rectangle, size [950, h], position [540, 114.72 + h/2], roundness 18, fill #FFFFFF. h comes from the track `Card_bg.height` (419.08 before the answer, 682.56 after).
- Drop Shadow 1: colour #0E0028, opacity 45 percent, direction 150.9 degrees, distance 20.6, softness 26.
- Drop Shadow 2: colour #0E0028, opacity 35 percent, direction 153.4 degrees, distance 2.2, softness 2.
- These match CSS `drop-shadow(10px 18px 26px)` and `drop-shadow(1px 2px 2px)`. Check them against `variants-thread-flat.png` and adjust softness by eye.

### Post meta, title, body
| Layer | Font | Size | Colour | Tracking | Baseline x, y | Text |
|---|---|---|---|---|---|---|
| Meta_comm | ExtraBold | 22 | #141414 | 0 | 159, 178.72 | c/ERPadmins |
| Meta_dot | Regular | 22 | #6D757A | 0 | 323.36, 178.72 | · |
| Meta_user | Regular | 22 | #6D757A | 0 | 340.98, 178.72 | variant_wrangler |
| Title_line1 | ExtraBold | 52 | #141414 | -14 | 107, 262.72 | How are you handling complex |
| Title_line2 | ExtraBold | 52 | #141414 | -14 | 107, 321.47 | variants in Business Central? |
| Body_line1 | Regular | 31 | #2A2A2A | 0 | 107, 380.22 | One product, 12 sizes, 8 colors, 3 materials. Our item |
| Body_line2 | Regular | 31 | #2A2A2A | 0 | 107, 422.98 | setup is falling apart. |

- Meta_icon: ellipse 40x40 at centre (127, 170.72), fill #008FC4. Four rounded squares 8x8, roundness 2, centres (122, 165.72), (132, 165.72), (122, 175.72) in #FFFFFF and (132, 175.72) in #FFB310.
- Point text, left justified. Tracking -14 equals the mock's -0.014em.

### Post pills (Post_pills)
- Three pills: rectangles with a 1.5px #CFD2D4 stroke, no fill, roundness 22. Outer boxes (x, y, w, h): (107, 455.75, 90, 44), (209, 455.75, 54, 44), (275, 455.75, 54, 44). Inset the stroke centre by 0.75px, so the rectangle size is w-1.5 by h-1.5.
- Four icons, each a 24x24 box, stroke #6D757A 2px, round joins, no fill. Top-left corners: arrow_up (122, 465.75), arrow_down (158, 465.75), bubble (224, 465.75), share (290, 465.75).

### Answer
- Answer_bg: rectangle size [866, h], position [540, 525.75 + h/2], roundness 14, fill #E6E8FC. h from `Answer_bg.height`.
- Answer_avatar: ellipse 36x36 fill #FFB310, plus person icon in #FFFFFF: circle r 4.2 at icon (12, 9) and the `person_body` path, icon box top-left (139, 553.75). Drawn around the origin: layer anchor and position (151, 565.75), contents offset by (-151, -565.75).
- Answer_user: ExtraBold 22 #141414, baseline (181, 573.75), "erp_ops_lead".
- Tag_pill: rectangle 118.02x29, centre (413.93, 565.75), roundness 14, fill #006D5B. Tag_text: ExtraBold 16 #FFFFFF, baseline (366.92, 571.25), "Top answer".
- Answer text, all #141414 at size 31:

| Layer | Font | Baseline x, y | Text |
|---|---|---|---|
| Answer_l1 | Regular | 133, 629.75 | We moved variants and enrichment into |
| Answer_bold | ExtraBold | 737.88, 629.75 | Truvio PIM |
| Answer_period | Regular | 905.31, 629.75 | . |
| Answer_l2 | Regular | 133, 672.52 | It runs inside BC and syncs back only what BC needs. |

- AE sets text a pixel or two differently from Chrome. After the build, check the gaps around Truvio PIM read as normal word spaces. Nudge Answer_bold and Answer_period on x if needed.
- Answer_pills: two pills with fill #FFFFFF and a 1.5px #CFD2D4 stroke, roundness 22, boxes (133, 699.28, 90, 44) and (235, 699.28, 54, 44). Icons: arrow_down at (184, 709.28) and bubble at (250, 709.28), same stroke as the post icons.
- Upvote_outline: arrow_up at (148, 709.28), stroke #6D757A 2px, no fill. Upvote_fill: the same path, fill and 2px stroke both #F76336. Both drawn around (160, 721.28) under Upvote_null.
- Dot1, Dot2, Dot3: ellipses 8x8 fill #6D757A, centres (141, 619), (157, 619), (173, 619).

### Effects layers
- Underline: open path from (313.5, 388.5) to (751, 388.5), stroke #F76336 4px, round caps, Trim Paths End from the track.
- Burst: six lines from radius 16 to radius 24 at 0, 60, 120, 180, 240 and 300 degrees, stroke #F76336 2.5px, round caps. Drawn around the origin, layer position (160, 721.28).
- Cursor: `cursor` path at 120 percent, fill #FFFFFF, stroke #141414 1.4px, round joins. The tip is the layer origin, so the position track places the tip.

### Callout
- Callout_outline: the paths `outline_top` and `outline_bottom` (comp coordinates), stroke 2px in any opaque colour, no fill. One Trim Paths on the group, End from the track. Both paths start at the left middle (66, 899.28) and end at the right middle, so the outline draws from left to right along both edges at once.
- Callout_gradient: `callout-gradient.png` at full frame, position (540, 540), with Callout_outline as its alpha matte. AE scripting can't set gradient colour stops, so the plate carries them: #33B4E8, #2DB34A at 55 percent, #FFB310.
- Lockup: `truvio-lockup-reversed.png` scaled to 15.043 percent (176px wide), centre (189, 899.33). If Grady has the official lockup `.ai`, use it with continuous rasterisation at the same width.
- CTA: ExtraBold 26 #E6E8FC, baseline (460.88, 908.78), "Test your hardest variants in a demo".
- CTA_arrow: `cta_arrow` path (two open subpaths, 24x16 box) scaled to 26x18 (108.33 by 112.5 percent), top-left (953, 891.28), stroke #E6E8FC 3px, round caps and joins. Parent to CTA so it rides CTA.dx.

## Path data
`VT.icons.ae` holds every icon as AE shapes, already converted from SVG (arcs and curves included). Each entry is a list of subpaths: `v` vertices, `i` in tangents, `o` out tangents (both relative to their vertex, as AE expects), `closed`. Icon coordinates sit in a 24x24 box with the origin at the top-left. Place an icon by adding the box's top-left to every vertex, or with the group transform. `VT.icons.svg` keeps the original SVG strings for reference.

```js
function aeShape(sub, dx, dy, sx, sy) {           // sx, sy default 1
  var s = new Shape(), v = [], i = [], o = [];
  for (var n = 0; n < sub.v.length; n++) {
    v.push([sub.v[n][0] * sx + dx, sub.v[n][1] * sy + dy]);
    i.push([sub.i[n][0] * sx, sub.i[n][1] * sy]);
    o.push([sub.o[n][0] * sx, sub.o[n][1] * sy]);
  }
  s.vertices = v; s.inTangents = i; s.outTangents = o; s.closed = sub.closed;
  return s;
}
```

The converter was checked: the AE path data redrawn as SVG matches the originals with zero differing pixels.

## Timeline
Frame = seconds x 30.

| Time (s) | Frames | Beat | What happens |
|---|---|---|---|
| 0.00 | 0 | Hook | Card with meta, title and post pills. Body hidden |
| 0.25 to 0.75 | 8 to 23 | Body | Body lines fade up 10px, line 2 starts 0.15s after line 1 |
| 1.10 to 1.45 | 33 to 44 | Numbers | Red underline draws under "12 sizes, 8 colors, 3 materials" |
| 1.50 to 2.08 | 45 to 62 | 12 sizes | 12 white chips fly out of the numbers into a row at y 590, small to large |
| 2.00 to 2.71 | 60 to 81 | x 8 colours | Each chip spawns 7 more colours down its column. 96 tiles |
| 2.60 to 2.90 | 78 to 87 | x 3 materials | Each tile spawns an outline and a split version. 288 tiles |
| 2.85 to 3.25 | 86 to 98 | Breaks apart | Every tile flies to a random spot and spins |
| 3.20 to 4.00 | 96 to 120 | Falls apart | Tiles fall and bounce into a heap on the floor (y 815 to 1015) |
| 3.42 to 3.56 | 103 to 107 | Shudder | Card_null x: 0, +4, -4, +2, 0 |
| 3.80 to 4.25 | 114 to 128 | Reply opens | Card grows to its final height. Answer panel grows in. Underline fades out |
| 4.10 to 4.35 | 123 to 131 | Author | Avatar pops, name slides in 12px, answer pills fade in |
| 4.35 to 5.10 | 131 to 153 | Typing | Three dots pulse twice |
| 5.10 to 6.58 | 153 to 197 | Answer | Line 1, Truvio PIM, the period, then line 2 type on |
| 6.62 to 7.66 | 199 to 230 | Sorted | The heap lifts and flies into an 8 by 36 grid in the callout zone |
| 7.62 to 8.85 | 229 to 266 | Upvote | Cursor glides in, clicks at 8.10, leaves |
| 8.13 | 244 | Click | Arrow switches to red fill, scales 135 percent and back. Burst rays |
| 8.28 to 8.50 | 248 to 255 | Top answer | Tag pops in from its left edge |
| 8.70 to 9.45 | 261 to 284 | Sync | Grid collapses left to right into the callout edges and fades |
| 8.95 to 9.50 | 269 to 285 | Outline | Callout outline draws on from the left |
| 9.30 to 9.90 | 279 to 297 | Brand | Lockup slides in 12px, CTA slides in 16px |
| 10.40 and 12.40 | 312, 372 | Nudge | CTA arrow nudges 7px right and back |
| 9.90 to 14.00 | 297 to 420 | Hold | Static flat ad. Nothing else moves |

## Applying the data

### UI tracks
`VT.tracks` maps `"Layer.property"` to keys `[time, value, ease]`. Map them like this:

| Track | AE property |
|---|---|
| `X.opacity` | Opacity, 0 to 100 |
| `X.scale` | Scale [v, v] (3 values for a 3D-capable property, pass [v, v, 100]) |
| `X.dx` | Position x = base x + dx. Base x is the layer's static position |
| `X.dy` | Position y = base y + dy |
| `X.position` | Position [x, y] |
| `Card_bg.height`, `Answer_bg.height` | Rectangle Size [w, h] and Rectangle Position [cx, top + h/2], keyed together with the same ease |
| `Underline.trim`, `Callout_outline.trim` | Trim Paths End, 0 to 100 |
| `Answer_*.type` | Type-on animator, Range Selector Start, 0 to 100 (see below) |
| `Card_null.dx` | Card_null position x |
| `Tag.*`, `CTA.*`, `Lockup.*`, `Upvote_null.scale`, `Burst.*`, `Cursor.*` | As above, on the layers named in the stack |

### Tiles
`VT.tiles` has 288 entries: `name`, `size` (16 to 38px), `colour`, `material` (solid, outline, split) and `keys` as `[time, x, y, rotation, scale, opacity, ease]`. Scale is a percent of the tile's own size.

Build each tile as one shape layer, drawn around its origin:
- Rectangle size [size, size], roundness 18 percent of size.
- solid: fill in its colour.
- outline: no fill, stroke in its colour, width 12 percent of size, rectangle size reduced by the stroke width so the outer edge stays at `size`.
- split: fill in its colour, plus a triangle above it with vertices (-size/2, -size/2), (size/2, -size/2), (-size/2, size/2), fill #400685 at 35 percent opacity, with Round Corners at 18 percent of size.
- Key Position [x, y], Rotation, Scale [s, s] and Opacity at every key time.
- Set the layer in-point to its first key time and its out-point to its last key time plus one frame. AE then skips the layer outside its life, which keeps 288 layers fast.
- Use `prop.setValuesAtTimes(times, values)` per property, then set eases in a second pass. It is far faster than one `setValueAtTime` per key.
- Set spatial interpolation on position keys to linear: `setSpatialTangentsAtKey(k, [0,0], [0,0])` and `setSpatialAutoBezierAtKey(k, false)`. Auto bezier makes the tiles loop and overshoot.

### Ease codes
The ease on a key describes the segment that arrives at it. The first key's ease is ignored.

| Code | Meaning | Previous key, out side | This key, in side |
|---|---|---|---|
| L | linear | LINEAR | LINEAR |
| O | ease out, decelerate into the key | LINEAR | BEZIER, KeyframeEase(0, 75) |
| I | ease in, accelerate into the key | BEZIER, KeyframeEase(0, 75) | LINEAR |
| IO | ease in and out | BEZIER, KeyframeEase(0, 60) | BEZIER, KeyframeEase(0, 60) |
| H | hold, jump at this key | HOLD | LINEAR |

- Set interpolation types first (`setInterpolationTypeAtKey(k, inType, outType)`), then eases (`setTemporalEaseAtKey`).
- KeyframeEase arrays need one entry per temporal dimension: one for Opacity, Rotation, Position (spatial) and Trim, two or three for Scale and Rectangle Size (non-spatial multi-value properties). Read `prop.value.length` and match it.

### Type-on
For Answer_l1, Answer_bold, Answer_period and Answer_l2:
- Add a Text Animator with an Opacity property at 0.
- Range Selector: Units Percentage, Based On Characters, Shape Square, Smoothness 0, End 100.
- Key Start from the `*.type` track. Characters before Start show, characters after it stay hidden.
- Matchnames: `ADBE Text Animators`, `ADBE Text Animator`, `ADBE Text Animator Properties`, `ADBE Text Opacity`, `ADBE Text Selectors`, `ADBE Text Selector`, `ADBE Text Percent Start`, `ADBE Text Percent End`, `ADBE Text Range Advanced`, `ADBE Text Range Type2` (Based On), `ADBE Text Range Shape`, `ADBE Text Selector Smoothness`. Confirm each matchname at runtime and fall back to display names if one is missing.

## ExtendScript notes
- ES3 only: `var`, no arrow functions, no `let` or `const`, no template strings, no `Array.forEach`. `vt-data.js` is plain object literals, so `$.evalFile()` reads it.
- Resolve file paths from the script's own location: `File($.fileName).parent`. Grady runs it from the `animation/` folder.
- Wrap the build in `app.beginUndoGroup()` and `app.endUndoGroup()`.
- Shape matchnames: `ADBE Root Vectors Group`, `ADBE Vector Group`, `ADBE Vectors Group`, `ADBE Vector Shape - Rect` (`ADBE Vector Rect Size`, `ADBE Vector Rect Position`, `ADBE Vector Rect Roundness`), `ADBE Vector Shape - Ellipse` (`ADBE Vector Ellipse Size`, `ADBE Vector Ellipse Position`), `ADBE Vector Shape - Group` (`ADBE Vector Shape`), `ADBE Vector Graphic - Fill` (`ADBE Vector Fill Color`, `ADBE Vector Fill Opacity`), `ADBE Vector Graphic - Stroke` (`ADBE Vector Stroke Color`, `ADBE Vector Stroke Width`, `ADBE Vector Stroke Line Cap`, `ADBE Vector Stroke Line Join`), `ADBE Vector Filter - Trim` (`ADBE Vector Trim End`), `ADBE Vector Filter - RC` (Round Corners).
- Colours are [r, g, b] from 0 to 1. Write one `hex()` helper.
- Text: `comp.layers.addText()`, then a TextDocument with `font`, `fontSize`, `fillColor`, `applyFill = true`, `applyStroke = false`, `tracking`, `justification = ParagraphJustification.LEFT_JUSTIFY`. Set the position to the baseline point after the text is set.
- Track matte: AE 2023 and later use `gradLayer.setTrackMatte(outlineLayer, TrackMatteType.ALPHA)`. Older versions need the matte directly above and `gradLayer.trackMatteType = TrackMatteType.ALPHA`. Try the new call first.
- Drop Shadow (`ADBE Drop Shadow`): read Opacity back after setting it. Some versions store 0 to 255 in scripting, not 0 to 100.
- Nulls: `comp.layers.addNull()` makes a 100x100 null with its anchor at (50, 50). Set anchor and position before parenting anything to it.
- Self-check at the end: count layers (expect 325: 288 tiles plus 37 others), confirm both fonts resolved (`textDocument.font` reads back the PostScript name), and show one alert with the counts and any warnings.

## Render
- Add the comp to the render queue. AE 2023 and later: output module template "H.264 - Match Render Settings - 15 Mbps", file `variants-thread-1x1.mp4`. Older AE: ProRes 422, then encode to H.264 in Media Encoder or CapCut.
- MP4, H.264, 1080x1080, 30 fps, no audio. 14 seconds sits well inside LinkedIn's video ad limits.
- Upload `variants-thread-flat.png` as the LinkedIn video thumbnail. Viewers who don't autoplay then see the full ad.

## QA for Grady after running the script
- Scrub against the animatic at 0, 1.9, 2.8, 3.1, 4.0, 5.5, 7.6, 8.15, 8.5, 9.1 and 14 seconds. Those match the storyboard frames.
- Frame 0: hook fully readable. No stray dot from the underline (a zero-length round cap draws one in the browser, so check AE too).
- Frames 300 to 420: put `variants-thread-flat.png` on top in Difference mode. Everything reads black except antialiasing. The animatic's own last frame matches a 1x render of the static mock to a mean of 0.96 per pixel.
- Gaps around Truvio PIM read as normal spaces.
- No tile crosses the 65px safe margin at any time. The data was checked for this.
- The heap never touches the card. Its top sits at y 815.6, the card ends at 797.
- Card shadow softness matches the static PNG.
- Ground stays #400685 in the exported MP4. H.264 can shift it a few levels.

## Fixes if something looks wrong
- Tiles loop or overshoot between keys: the position keys still have auto bezier. Set spatial tangents to zero.
- AE crawls with 288 layers: check the in and out points are trimmed. Work with motion blur off. Turn it on for the render.
- Type-on reveals the whole word at once: Based On is set to Words. Set Characters.
- Text sits a few pixels high or low: point text was positioned before the text was set, or anchor point changed. Re-set position after the TextDocument.
- Gradient outline renders solid white: the track matte didn't attach. Check the matte layer order and type.
- A font falls back to Arial or Myriad: Be Vietnam Pro isn't installed, or the PostScript name has a typo.
- Burst and Upvote scale from a corner: the layer anchor isn't on (160, 721.28).

## Changing the motion
- Edit `build_data.py`, run `python3 build_data.py`, then re-run the `.jsx` in a fresh comp. Never hand-edit `vt-data.js`.
- Preview a change before AE: `node render_animatic.mjs` renders the MP4 again in about 30 seconds. It needs Playwright and ffmpeg. Link a Playwright install as `node_modules` next to the script, or run `npm i playwright` there.
- `node render_animatic.mjs --frames-only 2.8,7.6` writes single frames to `frames/`.
- The animatic eases approximate AE's: cubic curves for O, I and IO. Expect small timing feel differences, not position differences.

## Options not built
- 6-second cutdown: start at 4.0 with the heap in place, run to 10.0. Loses the multiplication beat.
- 4:5 version: the thread fits 1080x1350 with the variant zone 270px taller. Needs a new layout pass first.
- Loop: LinkedIn may loop short videos. The cut from the held end back to frame 0 reads as a refresh, so no transition is planned.
