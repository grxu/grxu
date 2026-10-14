CRAMMED NOTE GIF KIT (Row 53)
=============================

What's inside
- 1-illustrator-layers.jsx   Sorts your artwork into the layers After Effects needs.
- 2-after-effects-build.jsx  Builds the animation and queues the render.
- 3-make-gif.command         Turns the rendered frames into the LinkedIn GIF.
- timing-table.md            Every move, frame by frame.


ONCE, BEFORE YOU START
- After Effects: After Effects > Settings (or Preferences) > Scripting & Expressions.
  Tick "Allow Scripts to Write Files and Access Network".
- For step 3: install Homebrew from https://brew.sh, then run this in Terminal:
  brew install ffmpeg gifsicle


STEP 1. ILLUSTRATOR
1. Open your fixed Row 53 .ai.
2. File > Scripts > Other Script... (Cmd+F12) and pick 1-illustrator-layers.jsx.
3. It saves a copy next to your file called <name>-AE-layers.ai and works on that.
   Your original isn't touched.
4. Read the message at the end. It lists every layer with its item count,
   and anything to fix by hand.
5. If there's a layer called _Unsorted: select each item in it, Edit > Cut,
   click the right layer, then Edit > Paste in Place (Shift+Cmd+V).
   Delete _Unsorted when it's empty.
6. Look at each layer once with the others hidden. Then save.


LAYER GUIDE
Use this to check the script's work, or to do it by hand. Each one is a
top-level layer (not a sublayer). Front to back:

  Sorted_text      "Sorted in Truvio PIM"
  Check_tick       the tick inside the check circle
  Check_circle     the check circle
  Word_3           "assets"
  Word_2           "translations"
  Word_1           "attributes"
  Arrow_3          the arrow on line 3. Live stroke, not outlined.
  Arrow_2          the arrow on line 2. Live stroke, not outlined.
  Arrow_1          the arrow on line 1. Live stroke, not outlined.
  Card_left        "47 custom fields", "6 languages", "Image links, spec sheets"
  Card_header      app icon, TRUVIO PIM, 23:51
  Card_bg          the white card and its shadow
  Clock_2351       the status bar time, reading 23:51
  Clock_2347       a copy of it, reading 23:47
  Phone            the phone, its screen and the note
  Subline          "Truvio PIM, inside Business Central."
  Better_gradient  "better" with the gradient
  Headline_rest    the rest of the headline
  Lockup           the truvio logo
  Background       the violet background

You don't need a white "better". After Effects makes that copy itself.
If the check is one shape, leave Check_tick out. The check fades in instead of drawing.


STEP 2. AFTER EFFECTS
1. File > Scripts > Run Script File... and pick 2-after-effects-build.jsx.
2. Pick the <name>-AE-layers.ai from step 1.
3. Read the message at the end. It names anything it skipped or that needs a fix by hand.
4. Check these frames in the "Crammed note GIF" comp:
     0    no card, the whole note readable, clock 23:47, "better" white
     35   the card has landed
     68   "Sorted in Truvio PIM" fully in
     82   "better" fully in gradient
     132  matches your static
     141  same as frame 0
5. Press Render in the Render Queue. The frames go to a folder called
   crammed-note-gif-png, next to the .ai.


STEP 3. GIF
1. Double-click 3-make-gif.command and pick the crammed-note-gif-png folder.
   If macOS blocks it, right-click it > Open > Open.
   Or in Terminal, type "bash " (with the space), drag the .command file in,
   drag the folder in after it, then press Return.
2. It saves crammed-note-linkedin.gif next to that folder, then prints the size
   and frame count. LinkedIn takes up to 5 MB and 250 frames. A test run from
   your static came out at 0.40 MB and 145 frames.


IF SOMETHING LOOKS WRONG
- The script stops: its message says what's missing and lists the layers it found.
- An arrow draws from its head: reverse its path direction in Illustrator and run
  steps 1 and 2 again. Or in After Effects, animate Trim Paths Start from 100 to 0
  instead of End.
- The check circle starts drawing in the wrong place: change Offset in its Trim Paths.
- "better" reveals right to left: on Better_gradient, add 180 to Linear Wipe's Wipe Angle.
- The card lands in the wrong place: the CARD layer's anchor point should sit at the
  card's top centre. The script uses 540, 580.
- Start over in After Effects: Edit > Undo "Crammed note GIF".
- Anything else: send Claude the message text or a screenshot.

These scripts were written and tested against mocks of Illustrator and After Effects,
not the apps themselves. Your first run is the real test.
