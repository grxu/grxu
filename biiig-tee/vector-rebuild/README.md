# BIIIG art: clean rebuild

`front-biiig.svg` and `back-iii.svg` in `traced/` are hand traces of the
BIIIG poster. Up close, their edges have small bumps, and parts that should
match don't: the III's left and right serifs and slots differ, and only its
right corners are rounded. `rebuild.py` redraws both and writes them to
`../ghost-mannequin/print/`.

## What changed

- **III and circles (back):** built from exact geometry and mirrored left to
  right and top to bottom. Square outer corners, curved serifs fitted to the
  traced ones, three equal circles (r 255.15, 395 apart) and slots with
  pointed-arch ends.
- **Red III on the front:** an exact scaled copy of the back III, so the two
  match.
- **Flames:** each flame keeps its own traced shape, smoothed. Each is
  stretched about 1.6% so its tips meet the points where the circles cross.
- **B:** the stem piece is mirrored top to bottom from its cleaner bottom
  half. The bowls are smoothed, and their corners stay sharp.
- **G:** all three pieces are smoothed, with straight edges kept straight.
  The big curve is smoothed more because its trace had flat spots.
- The colours, layout and overall size stay the same. The front is
  1766.7 × 593.9 units (10 × 3.36 cm) and the back is 1448 × 1761.8 units
  (32 × 38.9 cm).

## Run it

Install with `pip install shapely svgpathtools numpy`, then run:

    python3 rebuild.py traced ../ghost-mannequin/print

Each outline is built as a dense polygon, then fitted back to lines and cubic
Béziers. Holes use the even-odd fill rule.
