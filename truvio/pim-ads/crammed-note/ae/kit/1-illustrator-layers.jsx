// 1. Illustrator: sorts the Row 53 artwork into the layers the After Effects script needs.
// Open the fixed Row 53 .ai, then File > Scripts > Other Script... and pick this file.
// It first saves a copy next to your file (<name>-AE-layers.ai, PDF compatible). Your original stays as it is.
// Anything it can't place goes to a layer called _Unsorted. The closing message says what to move by hand.
// Written without Illustrator at hand and dry-run against a mock. If a step fails, the message gives the line.

(function () {
  if (!app.documents.length) { alert('Open the fixed Row 53 .ai first.'); return; }
  var doc = app.activeDocument;
  var folder = '';
  try { folder = doc.path.fsName; } catch (e) {}
  if (!folder) { alert('Save the file once first, then run this again.'); return; }

  // Front to back. The After Effects script reads these names.
  var LAYERS = ['Sorted_text', 'Check_tick', 'Check_circle', 'Word_3', 'Word_2', 'Word_1', 'Arrow_3', 'Arrow_2', 'Arrow_1',
                'Card_left', 'Card_header', 'Card_bg', 'Clock_2351', 'Clock_2347', 'Phone', 'Subline', 'Better_gradient',
                'Better_white', 'Headline_rest', 'Lockup', 'Background'];
  var WORDS = ['attributes', 'translations', 'assets'];
  var TAG = '\u0001crammed:';
  var notes = [];

  // ---------- Save a copy and work on that ----------
  var base = doc.name.replace(/\.ai$/i, '').replace(/-AE-layers$/, '');
  var outFile = new File(folder + '/' + base + '-AE-layers.ai');
  var opts = new IllustratorSaveOptions();
  opts.pdfCompatible = true;   // After Effects reads the PDF part of the .ai
  doc.saveAs(outFile, opts);

  // ---------- Prep: unlock, embed placed files ----------
  function unlockLayers(layers) {
    for (var i = 0; i < layers.length; i++) { layers[i].locked = false; unlockLayers(layers[i].layers); }
  }
  unlockLayers(doc.layers);
  for (var i = 0; i < doc.pageItems.length; i++) { try { doc.pageItems[i].locked = false; } catch (e) {} }
  var embedded = 0;
  for (i = doc.placedItems.length - 1; i >= 0; i--) {
    try { doc.placedItems[i].embed(); embedded++; } catch (e) { notes.push('A placed file could not be embedded. Embed it in the Links panel and run again.'); }
  }

  // ---------- Geometry. "up" values grow toward the top of the artboard ----------
  var ab = doc.artboards[doc.artboards.getActiveArtboardIndex()].artboardRect;
  var SIGN = ab[1] > ab[3] ? 1 : -1;
  var AB = { l: ab[0], r: ab[2], top: SIGN * ab[1], bot: SIGN * ab[3] };
  AB.w = AB.r - AB.l; AB.h = AB.top - AB.bot;
  function box(item) {
    var g = item.geometricBounds, a = SIGN * g[1], b = SIGN * g[3];
    var o = { l: Math.min(g[0], g[2]), r: Math.max(g[0], g[2]), top: Math.max(a, b), bot: Math.min(a, b) };
    o.w = o.r - o.l; o.h = o.top - o.bot; o.cx = (o.l + o.r) / 2; o.cy = (o.top + o.bot) / 2; o.area = o.w * o.h;
    return o;
  }
  function inside(b, c, pad) { pad = pad || 0; return b.cx >= c.l - pad && b.cx <= c.r + pad && b.cy >= c.bot - pad && b.cy <= c.top + pad; }
  function contains(c, b) { return c.l <= b.l && c.r >= b.r && c.top >= b.top && c.bot <= b.bot; }

  // ---------- Collect leaves, front to back ----------
  function hiddenUp(item) {
    if (item.hidden) return true;
    var L = item.layer;
    while (L && L.typename === 'Layer') { if (!L.visible) return true; L = L.parent; }
    return false;
  }
  var tops = [];
  for (i = 0; i < doc.pageItems.length; i++) {
    var it = doc.pageItems[i];
    if (it.parent.typename === 'Layer' && !hiddenUp(it)) tops.push(it);
  }
  var leaves = [], z = 0;
  function isClip(item) {
    if (item.typename === 'PathItem') return item.clipping;
    if (item.typename === 'CompoundPathItem') return item.pathItems.length > 0 && item.pathItems[0].clipping;
    return false;
  }
  function walk(item) {
    if (item.hidden) return;
    if (item.typename === 'GroupItem') { for (var k = 0; k < item.pageItems.length; k++) walk(item.pageItems[k]); return; }
    leaves.push({ item: item, z: z++, clip: isClip(item), text: item.typename === 'TextFrame', b: box(item), cat: null });
  }
  for (i = 0; i < tops.length; i++) walk(tops[i]);

  function norm(s) { return String(s).replace(/[\u2018\u2019]/g, "'").replace(/\s+/g, ' ').replace(/^\s+|\s+$/g, '').toLowerCase(); }
  function fillOf(item) {
    try {
      if (item.typename === 'TextFrame') return item.textRange.characterAttributes.fillColor;
      if (item.typename === 'CompoundPathItem') return item.pathItems[0].filled ? item.pathItems[0].fillColor : null;
      if (item.typename === 'PathItem') return item.filled ? item.fillColor : null;
    } catch (e) {}
    return null;
  }
  function isWhite(c) {
    if (!c) return false;
    if (c.typename === 'RGBColor') return c.red > 244 && c.green > 244 && c.blue > 244;
    if (c.typename === 'GrayColor') return c.gray < 5;
    if (c.typename === 'CMYKColor') return c.cyan < 3 && c.magenta < 3 && c.yellow < 3 && c.black < 3;
    return false;
  }
  function isGradient(c) { return !!c && c.typename === 'GradientColor'; }
  function texts() { var o = []; for (var k = 0; k < leaves.length; k++) if (leaves[k].text) o.push(leaves[k]); return o; }

  // ---------- Anchors ----------
  var T = texts(), hdr = null, sorted = null, subline = null, better = null, betterWhite = null, headline = [], times = [];
  for (i = 0; i < T.length; i++) {
    var n = norm(T[i].item.contents);
    if (n === 'truvio pim' && !hdr) hdr = T[i];
    else if (n.indexOf('sorted') === 0 && !sorted) sorted = T[i];
    else if (n.indexOf('inside business central') >= 0 && !subline) subline = T[i];
    else if (n === 'better') {
      // The gradient one animates. A plain copy, if you made one, stays as Better_white.
      if (isGradient(fillOf(T[i].item)) || !better) { if (better) betterWhite = better; better = T[i]; } else betterWhite = T[i];
    }
    else if (n.indexOf("there's") >= 0 || n.indexOf('place for it') >= 0) {
      headline.push(T[i]);
      if (n.indexOf('better') >= 0) notes.push('"better" shares a text box with the headline. Split it into its own text box, put it on Better_gradient, and move the rest to Headline_rest.');
    }
    else if (/^\d{1,2}:\d{2}$/.test(n)) times.push(T[i]);
  }

  // Card background: the smallest shape behind TRUVIO PIM that contains it. White first.
  var card = null;
  if (hdr) {
    var best = null;
    for (i = 0; i < leaves.length; i++) {
      var L = leaves[i];
      if (L.text || L.clip || L.z < hdr.z || !contains(L.b, hdr.b)) continue;
      var score = L.b.area * (isWhite(fillOf(L.item)) ? 1 : 4);
      if (!best || score < best.score) best = { leaf: L, score: score };
    }
    if (best) card = best.leaf;
  }
  if (!card) notes.push('No card found behind "TRUVIO PIM". Card layers need placing by hand.');
  function onCard(L) { return card && L.z < card.z && inside(L.b, card.b, 4); }

  // Words: a box that ends with the PIM word. Split it when the left part shares the box.
  var words = [null, null, null];
  function splitWord(L, w) {
    var tf = L.item, s = tf.contents, at = s.toLowerCase().lastIndexOf(w);
    var right = L.b.r, left = L.b.l;
    var r = tf.duplicate(tf, ElementPlacement.PLACEBEFORE);
    r.contents = s.substring(at);
    r.translate(right - box(r).r, 0);
    tf.contents = s.substring(0, at).replace(/[\s\-\u2013\u2014\u2192>]+$/, '');
    tf.translate(left - box(tf).l, 0);
    L.b = box(tf);
    var R = { item: r, z: L.z - 0.5, clip: false, text: true, b: box(r), cat: null };
    leaves.push(R);
    return R;
  }
  for (var w = 0; w < WORDS.length; w++) {
    for (i = 0; i < T.length; i++) {
      if (!onCard(T[i])) continue;
      var nn = norm(T[i].item.contents);
      if (nn === WORDS[w]) { words[w] = T[i]; break; }
      if (nn.length > WORDS[w].length && nn.slice(-WORDS[w].length) === WORDS[w]) {
        words[w] = splitWord(T[i], WORDS[w]);
        notes.push('Split "' + T[i].item.contents + '" from "' + words[w].item.contents + '". Check the gap before the arrow.');
        break;
      }
    }
    if (!words[w]) notes.push('No "' + WORDS[w] + '" text on the card. Word_' + (w + 1) + ' stays empty.');
  }

  // Status bar clock: a time outside the card. 23:47 or 23:51 wins over strays like 7:02.
  var clock = null;
  for (i = 0; i < times.length; i++) {
    if (onCard(times[i])) continue;
    var tn = norm(times[i].item.contents);
    if (!clock || tn === '23:47' || tn === '23:51') clock = times[i];
  }

  var firstLineTop = -Infinity;
  for (w = 0; w < 3; w++) if (words[w]) firstLineTop = Math.max(firstLineTop, words[w].b.top);
  if (firstLineTop === -Infinity && hdr) firstLineTop = hdr.b.bot;
  var headTop = -Infinity, headBot = Infinity;
  for (i = 0; i < headline.length; i++) { headTop = Math.max(headTop, headline[i].b.top); headBot = Math.min(headBot, headline[i].b.bot); }
  if (better) { headTop = Math.max(headTop, better.b.top); headBot = Math.min(headBot, better.b.bot); }
  if (headTop === -Infinity) { headTop = AB.top - AB.h * 0.12; headBot = AB.top - AB.h * 0.32; }
  var phoneZoneTop = subline ? subline.b.bot : AB.top - AB.h * 0.4;

  // ---------- Classify ----------
  function classify(L) {
    var b = L.b, it = L.item;
    if (L.clip) return '__clip';
    if (b.area >= AB.w * AB.h * 0.85) return 'Background';
    if (L === hdr) return 'Card_header';
    if (L === sorted) return 'Sorted_text';
    if (L === subline) return 'Subline';
    if (L === better) return 'Better_gradient';
    if (L === betterWhite) return 'Better_white';
    for (var k = 0; k < headline.length; k++) if (L === headline[k]) return 'Headline_rest';
    for (k = 0; k < 3; k++) if (L === words[k]) return 'Word_' + (k + 1);
    if (L === clock) { var cn = norm(it.contents); return cn === '23:47' ? 'Clock_2347' : 'Clock_2351'; }
    if (L === card) return 'Card_bg';

    if (onCard(L)) {
      if (b.cy > firstLineTop) return 'Card_header';
      if (L.text) return 'Card_left';
      if (sorted && b.cx < sorted.b.l && Math.abs(b.cy - sorted.b.cy) < sorted.b.h) return '__check';
      for (k = 0; k < 3; k++) {
        var W = words[k];
        if (W && b.cx < W.b.l && Math.abs(b.cy - W.b.cy) < W.b.h * 0.7 && b.w < 200) return 'Arrow_' + (k + 1);
      }
      return '_Unsorted';
    }
    // A separate card shadow sits behind the card at about its size.
    if (card && !L.text && L.z > card.z && Math.abs(b.l - card.b.l) < 40 && Math.abs(b.r - card.b.r) < 40 &&
        Math.abs(b.top - card.b.top) < 40 && Math.abs(b.bot - card.b.bot) < 40) return 'Card_bg';
    if (L.text && /^\d{1,2}:\d{2}$/.test(norm(it.contents))) {
      notes.push('Stray time "' + it.contents + '" moved to _Unsorted. Delete it if it\'s left over.');
      return '_Unsorted';
    }
    if (b.cy > headTop) return 'Lockup';
    if (!L.text && b.cy <= headTop && b.cy >= headBot) return isGradient(fillOf(it)) ? 'Better_gradient' : 'Headline_rest';
    if (b.cy < phoneZoneTop) return 'Phone';
    return '_Unsorted';
  }
  for (i = 0; i < leaves.length; i++) leaves[i].cat = classify(leaves[i]);

  // Check icon: the biggest piece is the circle, the rest is the tick.
  var checks = [];
  for (i = 0; i < leaves.length; i++) if (leaves[i].cat === '__check') checks.push(leaves[i]);
  checks.sort(function (a, b) { return b.b.area - a.b.area; });
  for (i = 0; i < checks.length; i++) checks[i].cat = i === 0 ? 'Check_circle' : 'Check_tick';
  if (checks.length === 1) notes.push('The check is one shape. It goes on Check_circle and fades in. Split circle and tick if you want them drawn.');

  // ---------- Tag, then move ----------
  var origNotes = [];
  for (i = 0; i < leaves.length; i++) { origNotes.push(leaves[i].item.note); leaves[i].item.note = TAG + leaves[i].cat; }
  function tag(item) { var s = item.note; return s && s.indexOf(TAG) === 0 ? s.substring(TAG.length) : null; }

  var layerCache = {};
  function getLayer(name) {
    if (layerCache[name]) return layerCache[name];
    var L = null;
    for (var k = 0; k < doc.layers.length; k++) if (doc.layers[k].name === name) { L = doc.layers[k]; break; }
    if (!L) { L = doc.layers.add(); L.name = name; }
    L.locked = false; L.visible = true;
    return (layerCache[name] = L);
  }
  function cats(item, acc) {
    if (item.typename === 'GroupItem') { for (var k = 0; k < item.pageItems.length; k++) cats(item.pageItems[k], acc); return acc; }
    var c = tag(item);
    if (c && c !== '__clip') acc[c] = (acc[c] || 0) + 1;
    return acc;
  }
  function keys(o) { var a = []; for (var k in o) if (o.hasOwnProperty(k)) a.push(k); return a; }
  function kids(g) { var a = []; for (var k = 0; k < g.pageItems.length; k++) a.push(g.pageItems[k]); return a; }
  function place(item) {
    if (item.hidden) return;
    if (item.typename !== 'GroupItem') {
      var c = tag(item);
      if (c && c !== '__clip') item.move(getLayer(c), ElementPlacement.PLACEATEND);
      return;
    }
    var acc = cats(item, {}), ks = keys(acc);
    if (!ks.length) return;
    if (ks.length === 1) { item.move(getLayer(ks[0]), ElementPlacement.PLACEATEND); return; }
    var ch = kids(item), k;
    if (item.clipped) {
      // Keep the clipping group whole for its main layer. Pull out only what belongs elsewhere.
      var M = ks[0];
      for (k = 1; k < ks.length; k++) if (acc[ks[k]] > acc[M]) M = ks[k];
      for (k = 0; k < ch.length; k++) {
        var a = keys(cats(ch[k], {}));
        if (a.length && !(a.length === 1 && a[0] === M)) place(ch[k]);
      }
      item.move(getLayer(M), ElementPlacement.PLACEATEND);
      return;
    }
    for (k = 0; k < ch.length; k++) place(ch[k]);
  }
  for (i = 0; i < tops.length; i++) place(tops[i]);

  for (i = 0; i < leaves.length; i++) { try { leaves[i].item.note = origNotes[i] || ''; } catch (e) {} }

  // ---------- Clock copy: one layer with 23:47, one with 23:51 ----------
  if (clock) {
    var cv = norm(clock.item.contents);
    var twin = clock.item.duplicate(getLayer(cv === '23:47' ? 'Clock_2351' : 'Clock_2347'), ElementPlacement.PLACEATBEGINNING);
    twin.contents = cv === '23:47' ? '23:51' : '23:47';
    if (cv !== '23:47' && cv !== '23:51') notes.push('The status bar reads ' + clock.item.contents + '. Clock_2347 got a 23:47 copy. Set Clock_2351 to 23:51.');
  } else {
    notes.push('No live status bar time found. Put the time on Clock_2351, copy it to Clock_2347 and retype it as 23:47.');
  }

  // ---------- Tidy: empty groups, empty layers, layer order ----------
  for (i = doc.groupItems.length - 1; i >= 0; i--) { try { if (!doc.groupItems[i].pageItems.length) doc.groupItems[i].remove(); } catch (e) {} }
  function prune(layers) {
    for (var k = layers.length - 1; k >= 0; k--) {
      prune(layers[k].layers);
      if (!layers[k].pageItems.length && !layers[k].layers.length) layers[k].remove();
    }
  }
  prune(doc.layers);
  for (i = LAYERS.length - 1; i >= 0; i--) if (layerCache[LAYERS[i]]) { try { layerCache[LAYERS[i]].zOrder(ZOrderMethod.BRINGTOFRONT); } catch (e) {} }
  if (layerCache['_Unsorted']) { try { layerCache['_Unsorted'].zOrder(ZOrderMethod.BRINGTOFRONT); } catch (e) {} }

  doc.saveAs(outFile, opts);

  // ---------- Report ----------
  var lines = [], empty = [];
  for (i = 0; i < LAYERS.length; i++) {
    var lay = null;
    for (var j = 0; j < doc.layers.length; j++) if (doc.layers[j].name === LAYERS[i]) lay = doc.layers[j];
    if (lay) lines.push(LAYERS[i] + ': ' + lay.pageItems.length); else if (LAYERS[i] !== 'Better_white') empty.push(LAYERS[i]);   // AE makes Better_white itself
  }
  var other = [];
  for (i = 0; i < doc.layers.length; i++) {
    var nm = doc.layers[i].name, known = nm === '_Unsorted';
    for (j = 0; j < LAYERS.length; j++) if (LAYERS[j] === nm) known = true;
    if (!known) other.push(nm);
  }
  if (layerCache['_Unsorted']) lines.unshift('_Unsorted: ' + layerCache['_Unsorted'].pageItems.length + '  <- cut each one and Edit > Paste in Place into its layer');
  if (other.length) notes.push('Layers left as they were (hidden or not recognised): ' + other.join(', ') + '. Delete them if they aren\'t part of the ad.');
  if (embedded) notes.push(embedded + ' placed file(s) embedded.');
  alert('Saved: ' + outFile.fsName + '\n\n' + lines.join('\n') +
        (empty.length ? '\n\nEmpty, skipped in After Effects: ' + empty.join(', ') : '') +
        (notes.length ? '\n\nCheck:\n- ' + notes.join('\n- ') : '') +
        '\n\nLook at each layer once with the others hidden, then run 2-after-effects-build.jsx in After Effects.');
})();
