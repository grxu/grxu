# Handoff: LKS Literasi 2.7 (Bab 7) layout in Canva

## Goal
Fill the Canva design with the text from `source/LKS_Literasi_2.7_-_Teks.md` and lay out each page like `source/LKS_Literasi_2.7_compressed.pdf`.

- Canva design: https://www.canva.com/design/DAHZFqS73zI/GfA6ChrtArk6JLNq5m8leA/edit (17 pages).
- Canva page N is Pertemuan N.
- Page 16 is Pertemuan 16, part 1 of 2: sections 1–4 only, with no REFLEKSI.
- Page 17 is Pertemuan 16, part 2 of 2: sections 4 (continued), 5, 6, 7, and 8 "Refleksi dan Check Out" (a table plus a feelings checklist).

## The owner's rules (verbatim, keep them)
- "Template header, PDF layout, .md wording, 8-9 pt bold (but keep it consistent for the whole page), blue answer lines, empty picture frames, REFLEKSI SISWA strip as section 8. I'll only stop for real problems."
- Body text is Proxima Nova Bold, which is the template font `YAFcfjveRFU,0`.
  - Reuse existing template text boxes and the 15 "Text placeholder" spares on each page. `add_text` creates a different font.
  - The owner switches any added text boxes to Proxima Nova Bold by hand. List them at the end.
- Pictures: the owner deletes them. Picture spots become empty frames.
- "______" blanks become thin blue lines: 1 px rectangles, colour `#23a6df`.
- Save every 4 pages:
  1. Build the pages.
  2. Show the 4 thumbnails.
  3. Ask with AskUserQuestion.
  4. Commit only after an OK.
- Use AskUserQuestion for flags and questions.

## Status
- **Saved:** pages 1–9 (6–9 at fs 11). Known small blemishes: page 8 section 1 title touches its pill edge; page 9 section 7 answer lines are slightly uneven.
- **Next:** pages 10–13, then 14–17.
  - Text for 6–9 is in the .md. Pertemuan 6 is at line ~353, 7 at ~437, 8 at ~515, 9 at ~595.
  - **SPECS[6]–[9] are written** (`tools/specs.py`) and fit at fs 11 (`python3 fit.py 6 7 8 9` checks the fit offline without Canva). They have not been built in Canva yet, because the Canva connector exposed no tools in the session that wrote them.
  - Page 8's REFLEKSI content needs about 100 px, but its locked strip is 79 px. Ask the owner to unlock it, or try fix (b).
  - Specs for 10–17 are not written yet.
  - The PDF layouts for pages 6–9 were reviewed. They use 7 boxed sections plus section 8 = REFLEKSI strip.
- No Canva draft is open with pending work. An empty draft from the last session will just expire.

## Toolkit (`tools/`)
Run from `tools/` with Python 3.

### tw.py
Width estimator for Proxima Nova Bold: `width(s, fs)` and `lines(s, w, fs)`. It slightly overestimates.

### roles.py
`python3 roles.py <read-design.json> [first_page_no]` writes `roles.json`.

How to get the input file:
- Call `read-design` with `fields:["design_content"]` and the page indices you need.
- The result is too big to show, so it gets saved to a file.
- Pass that file to roles.py, with `first_page_no` set to the page number of the first page in it.

For each page it detects:
- template boxes: stroke `#aae0fa`, no fill, more than 250 × 80;
- for each box, its pill (`#feefbc`), circle (`#f8c357`), number, title and instruction texts;
- the REFLEKSI strip: a `#d9f0fb` shape more than 600 wide, with the star image, the label and the white box;
- a pool of reusable template-font texts;
- the spare text boxes;
- leftovers to delete.

### engine.py
`build_page(roles, spec, deletes, fs)` returns `(ops, info)`.

`info` gives `total`, `avail` and `over`. Keep `over` at 0 or below, and choose `fs` 11 or 12 per page.

Item types in specs:

| Item | What it draws |
|---|---|
| `T` | plain text |
| `FILL` | lines of label text followed by a blue blank; a tuple `(label, tail)` puts text after the blank |
| `OPTS` | checkbox options |
| `FRAMES(n, cols, h, {cb, num, line, labels, sq})` | empty picture frames |
| `COLS([[items]...], {frac, gap})` | columns |
| `BOX` | word box |
| `TABLE(heads, rows, {...})` | table; a `"☐"` cell is a checkbox, `"___"` is a blank |
| `MATCH(L, R, {wl, pitch})` | draw-a-line matching, with dots |
| `CARD`, `LINES`, `FOUR` | card, ruled lines, 4-line writing guide |
| `GAP` | vertical space |

Page specs:
- `spec["rows"]` changes the row grouping. Example: `[(1,(2,3)),(4,5),(6,7)]`.
- `full=True` on a section makes it span the full width.
- `spec["abs"]` places extra items at absolute positions.
- `spec["refl"]` holds the REFLEKSI content (section 8).

### specs.py
`SPECS[2]`…`SPECS[5]` are done. Use them as examples.

### run.py
`python3 run.py <page> <fs>` writes `ops<page>.json`.
- Apply the ops with `edit-design` in chunks of about 28 KB.
- Use `keep_open`, then check thumbnails, then `commit` after approval.

## Gotchas learned the hard way
1. **Drafts expire.** An idle Canva transaction is lost along with all its edits, and that happened twice. Build, apply, preview and commit promptly. Don't leave a draft open while waiting.
2. **Locked elements.**
   - Locked elements can't be moved, resized or ungrouped, but `replace_text` and `delete_element` work on them.
   - The fix used on page 4: delete the locked box outline, then set that box's `box` to `None` in roles.json. The engine then draws a new box and brings the pill, circle, number and title to the front.
3. **Locked REFLEKSI strips.**
   - The strip, star and label are locked on pages 5, 7, 8, 9, 10, 11, 12 and 14. The engine currently tries to move and resize them, which silently fails.
   - On page 5 the content was refitted by hand into the fixed strip at top 989, height 79.
   - Fix (a) is now in `engine.py`. A locked strip keeps its geometry, and `info["notes"]` flags content that is too tall for it.
   - Two possible fixes:
     - (a) Treat a locked strip as fixed geometry. Skip its move and resize ops and fit the content inside.
     - (b) Delete the locked strip, star and label and recreate them. Whether `insert_fill` with asset `MAHWpPlzdzA` recreates the star was never tested.
   - Page 8's section 8 has two sentences plus three checkbox statements, which does not fit a 79 px strip. Either use (b) or ask the owner to unlock it.
4. **Big template groups.**
   - A big group holds the whole section template (42 children) on page 2 (done) and page 8 (`LByRxLvc6fKMgx9z`, unlocked).
   - Ungroup it with `ungroup_elements`, then re-read the page, because child IDs change after ungrouping. Then rerun roles.py.
5. **Boxes without a number text** (roles shows `numtxt: None`) are not deleted by the engine. Add them to the deletes, or fix `build_page`.
6. **Don't delete backgrounds.** roles.py skips page-size shapes (top < 30, width > 700). Always scan the delete list for anything wider than 500 px, near the top, or of type `rect` before applying.
7. Long table headers can wrap. On page 3, the "Hemat Air" column header needed width 56.
8. Edit responses are cut off at 100k characters, so check results with `read-design` thumbnails.

## When finished
List any text boxes created with `add_text` (wrong font) and anything to fix by hand, such as pictures and fonts.
