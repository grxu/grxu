// 2. After Effects: builds the crammed note GIF animation (Row 53) and queues a PNG sequence.
// Run step 1 in Illustrator first. Then here: File > Scripts > Run Script File, pick this file,
// then pick the <name>-AE-layers.ai it saved.
// Needs Preferences > Scripting & Expressions > "Allow Scripts to Write Files and Access Network" (it makes the output folder).
// Timing follows timing-table.md. Written without After Effects at hand and dry-run against a mock.
// Any step that fails is listed in the closing alert. Edit > Undo "Crammed note GIF" takes back the keys and setup.

(function () {
  var FPS = 25, FRAMES = 145;
  var CARD_ANCHOR = [540, 580];   // top centre of the card, measured on the original Row 53 file
  var WIPE_ANGLE = 244.6;         // reveals "better" left to right along a 25.4 degree gradient. Add 180 if it runs backwards.
  var CARD = ['Card_bg', 'Card_header', 'Card_left', 'Arrow_1', 'Arrow_2', 'Arrow_3',
              'Word_1', 'Word_2', 'Word_3', 'Check_circle', 'Check_tick', 'Sorted_text'];
  var OPTIONAL = ['Clock_2347', 'Clock_2351', 'Better_gradient'].concat(CARD.slice(1));
  var DRAW = ['Arrow_1', 'Arrow_2', 'Arrow_3', 'Check_circle', 'Check_tick'];
  var notes = [];

  function t(f) { return f / FPS; }

  function find(comp, name) {
    for (var i = 1; i <= comp.numLayers; i++) if (comp.layer(i).name === name) return comp.layer(i);
    return null;
  }

  // Temporal ease. Spatial and one-value properties take one ease, others one per dimension.
  function ease(prop, k, inInf, outInf) {
    var n = 1, vt = prop.propertyValueType;
    if (vt === PropertyValueType.TwoD || vt === PropertyValueType.ThreeD) n = prop.keyValue(k).length;
    var a = [], b = [];
    for (var i = 0; i < n; i++) { a.push(new KeyframeEase(0, inInf)); b.push(new KeyframeEase(0, outInf)); }
    prop.setTemporalEaseAtKey(k, a, b);
  }

  // Straight spatial path, so the card and the words never curve or overshoot sideways.
  function straight(prop, k) {
    if (!prop.isSpatial) return;
    var v = prop.keyValue(k), z = [];
    for (var i = 0; i < v.length; i++) z.push(0);
    prop.setSpatialTangentsAtKey(k, z, z);
  }

  function key(prop, f, v) {
    prop.setValueAtTime(t(f), v);
    var k = prop.nearestKeyIndex(t(f));
    straight(prop, k);
    return k;
  }

  // Decelerate: leaves fast, lands softly. AE's Easy Ease In on the last key.
  function decel(prop, f0, v0, f1, v1, inInf) {
    key(prop, f0, v0); key(prop, f1, v1);
    ease(prop, prop.nearestKeyIndex(t(f0)), 33.3, 10);
    ease(prop, prop.nearestKeyIndex(t(f1)), inInf, 33.3);
  }

  function holds(prop, list) {
    for (var i = 0; i < list.length; i++) {
      var k = key(prop, list[i][0], list[i][1]);
      prop.setInterpolationTypeAtKey(k, KeyframeInterpolationType.HOLD, KeyframeInterpolationType.HOLD);
    }
  }

  function hasStroke(group) {
    for (var i = 1; i <= group.numProperties; i++) {
      var p = group.property(i);
      if (p.matchName === 'ADBE Vector Graphic - Stroke' && p.enabled) return true;
      if (p.propertyType !== PropertyType.PROPERTY && hasStroke(p)) return true;
    }
    return false;
  }

  // ---------- Import ----------
  var file = File.openDialog('Pick the -AE-layers.ai that step 1 saved');
  if (!file) return;
  var io = new ImportOptions(file);
  if (!io.canImportAs(ImportAsType.COMP_CROPPED_LAYERS)) { alert('This file can\'t be imported as a composition with layers. Save it from Illustrator with "Create PDF Compatible File" on.'); return; }
  io.importAs = ImportAsType.COMP_CROPPED_LAYERS;

  app.beginUndoGroup('Crammed note GIF');
  try {
    var comp = app.project.importFile(io);
    if (!(comp instanceof CompItem)) { alert('The import didn\'t return a composition. Import the .ai as Composition - Retain Layer Sizes and check its layers.'); return; }

    if (!find(comp, 'Card_bg')) {
      var found = [];
      for (var i = 1; i <= comp.numLayers; i++) found.push(comp.layer(i).name);
      alert('No Card_bg layer, so there is no card to animate.\n\nLayers in the file: ' + found.join(', ') +
            '\n\nRun 1-illustrator-layers.jsx on the fixed .ai first, or rename the card background layer to Card_bg.');
      return;
    }
    var skipped = [];
    for (i = 0; i < OPTIONAL.length; i++) if (!find(comp, OPTIONAL[i])) skipped.push(OPTIONAL[i]);
    if (comp.width !== 1080 || comp.height !== 1080) notes.push('Comp is ' + comp.width + 'x' + comp.height + ', not 1080x1080. Check the artboard.');

    // ---------- Comp settings ----------
    comp.name = 'Crammed note GIF';
    comp.frameRate = FPS;
    comp.duration = FRAMES / FPS;
    for (i = 1; i <= comp.numLayers; i++) { comp.layer(i).inPoint = 0; comp.layer(i).outPoint = comp.duration; }

    // ---------- Arrows and check as shape layers with Trim Paths ----------
    var viewer = comp.openInViewer();   // the menu command acts on the active comp
    if (viewer) viewer.setActive();
    var cmd = app.findMenuCommandId('Create Shapes from Vector Layer') || 3973;
    var drawable = {};
    for (i = 0; i < DRAW.length; i++) {
      var name = DRAW[i], src = find(comp, name);
      if (!src) continue;
      for (var j = 1; j <= comp.numLayers; j++) comp.layer(j).selected = false;
      src.selected = true;
      app.executeCommand(cmd);
      var shp = find(comp, name + ' Outlines');
      if (!shp) { drawable[name] = false; notes.push(name + ': Create Shapes from Vector Layer failed. It fades in.'); continue; }
      src.remove();
      shp.name = name;
      shp.inPoint = 0; shp.outPoint = comp.duration;
      drawable[name] = hasStroke(shp.property('ADBE Root Vectors Group'));
      if (!drawable[name]) notes.push(name + ': no live stroke (outlined?). It fades in.');
    }

    // ---------- CARD precomp ----------
    var idx = [];
    for (i = 0; i < CARD.length; i++) { var cl0 = find(comp, CARD[i]); if (cl0) idx.push(cl0.index); }
    var cardComp = comp.layers.precompose(idx, 'CARD', true);
    cardComp.frameRate = FPS;
    cardComp.duration = comp.duration;
    var card = find(comp, 'CARD');
    card.transform.anchorPoint.setValue(CARD_ANCHOR);
    card.transform.position.setValue(CARD_ANCHOR);
    card.collapseTransformation = true;   // keeps the vectors sharp during the 96 to 100 percent scale
    for (i = 1; i <= cardComp.numLayers; i++) {
      var cl = cardComp.layer(i);
      cl.inPoint = 0; cl.outPoint = cardComp.duration;
      try { cl.collapseTransformation = true; } catch (e) { /* shape layers don't need it */ }
    }

    // ---------- Main comp keys ----------
    var c47 = find(comp, 'Clock_2347'), c51 = find(comp, 'Clock_2351');
    if (c47 && c51) {
      holds(c47.transform.opacity, [[0, 100], [20, 0], [141, 100]]);
      holds(c51.transform.opacity, [[0, 0], [20, 100], [141, 0]]);
    } else notes.push('Clock cut skipped: it needs both Clock_2347 and Clock_2351.');

    // Card drop: 60 px drop, 5 px overshoot, settle. Then the exit: rises 40 px and fades.
    var pos = card.transform.position, x = CARD_ANCHOR[0], y = CARD_ANCHOR[1];
    key(pos, 25, [x, y - 60]); key(pos, 32, [x, y + 5]); key(pos, 35, [x, y]);
    key(pos, 133, [x, y]); key(pos, 140, [x, y - 40]);
    ease(pos, pos.nearestKeyIndex(t(25)), 33.3, 10);
    ease(pos, pos.nearestKeyIndex(t(32)), 70, 33.3);
    ease(pos, pos.nearestKeyIndex(t(35)), 33.3, 33.3);
    ease(pos, pos.nearestKeyIndex(t(133)), 33.3, 75);   // accelerate away: AE's Easy Ease Out on the first key
    ease(pos, pos.nearestKeyIndex(t(140)), 10, 33.3);

    decel(card.transform.scale, 25, [96, 96], 33, [100, 100], 75);
    var op = card.transform.opacity;
    key(op, 25, 0); key(op, 29, 100); key(op, 133, 100); key(op, 140, 0);

    // "better": white at the start, gradient wipes on after the check, fades back to white for the loop.
    var better = find(comp, 'Better_gradient');
    if (better) {
      if (!find(comp, 'Better_white')) {
        var bw = better.duplicate();
        bw.name = 'Better_white';
        bw.moveAfter(better);
        var fill = bw.property('ADBE Effect Parade').addProperty('ADBE Fill');
        for (i = 1; i <= fill.numProperties; i++) {
          if (fill.property(i).propertyValueType === PropertyValueType.COLOR) { fill.property(i).setValue([1, 1, 1, 1]); break; }
        }
      }
      var wipe = better.property('ADBE Effect Parade').addProperty('ADBE Linear Wipe');
      var done = wipe.property(1);   // Transition Completion
      wipe.property(2).setValue(WIPE_ANGLE);
      wipe.property(3).setValue(20); // Feather
      key(done, 70, 100); key(done, 82, 0);
      ease(done, done.nearestKeyIndex(t(70)), 33.3, 33.3);
      ease(done, done.nearestKeyIndex(t(82)), 33.3, 33.3);
      key(better.transform.opacity, 133, 100); key(better.transform.opacity, 140, 0);
    } else notes.push('"better" wipe skipped: no Better_gradient layer.');

    // ---------- CARD keys (same frame numbers: the precomp starts at frame 0) ----------
    function draw(name, f0, f1) {
      var L = find(cardComp, name);
      if (!L) return;
      if (drawable[name]) {
        var trim = L.property('ADBE Root Vectors Group').addProperty('ADBE Vector Filter - Trim');
        trim.property('ADBE Vector Trim Type').setValue(2);   // Individually: shaft, then head
        decel(trim.property('ADBE Vector Trim End'), f0, 0, f1, 100, 70);
      } else {
        decel(L.transform.opacity, f0, 0, f1, 100, 70);
      }
    }
    function slideIn(name, f0, f1, dx) {
      var L = find(cardComp, name);
      if (!L) return;
      var p = L.transform.position, v = p.value, from = [];
      for (var i = 0; i < v.length; i++) from.push(v[i]);
      from[0] -= dx;
      decel(L.transform.opacity, f0, 0, f1, 100, 75);
      decel(p, f0, from, f1, v, 75);
    }
    draw('Arrow_1', 37, 43);  slideIn('Word_1', 41, 46, 12);
    draw('Arrow_2', 43, 49);  slideIn('Word_2', 47, 52, 12);
    draw('Arrow_3', 49, 55);  slideIn('Word_3', 53, 58, 12);
    draw('Check_circle', 58, 65);
    draw('Check_tick', 62, 66);
    slideIn('Sorted_text', 62, 68, 10);

    // ---------- Render queue: PNG sequence, frames 0 to 144 ----------
    var rq = app.project.renderQueue.items.add(comp);
    try { rq.applyTemplate('Best Settings'); } catch (e) { notes.push('Render Settings: pick Best Settings by hand.'); }
    rq.timeSpanStart = 0;
    rq.timeSpanDuration = comp.duration;
    var om = rq.outputModule(1), tpl = null;
    for (i = 0; i < om.templates.length; i++) {
      if (/PNG/i.test(om.templates[i]) && !/alpha/i.test(om.templates[i])) { tpl = om.templates[i]; break; }
    }
    try {
      if (tpl) om.applyTemplate(tpl); else om.setSettings({ 'Format': 'PNG Sequence' });
    } catch (e) { notes.push('Output Module: set the format to PNG Sequence by hand.'); }
    var out = new Folder(file.parent.fsName + '/crammed-note-gif-png');
    if (!out.exists && !out.create()) notes.push('Could not make ' + out.fsName + '. Turn on "Allow Scripts to Write Files" and set the output folder by hand.');
    om.file = new File(out.fsName + '/crammed-note-gif_[#####].png');

    comp.openInViewer();
    alert('Built "Crammed note GIF" and queued a PNG sequence to:\n' + out.fsName +
          '\n\nCheck frames 0, 35, 82, 132 and 141 against timing-table.md, then press Render in the Render Queue.' +
          (skipped.length ? '\n\nNot in the file, skipped: ' + skipped.join(', ') : '') +
          (notes.length ? '\n\nFix by hand:\n- ' + notes.join('\n- ') : ''));
  } catch (err) {
    alert('Stopped at line ' + err.line + ': ' + err.toString() + (notes.length ? '\n\nFix by hand:\n- ' + notes.join('\n- ') : ''));
  } finally {
    app.endUndoGroup();
  }
})();
