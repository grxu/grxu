//@target illustrator
// Italy market entry: builds the six team-pick artboards in one Illustrator document.
// V1 Dotted Italy, V2 Autostrada, V3 Map + motorway, each as P1 (Or is it?) and P2 (Less invoice chasing).
// Run in Illustrator: File > Scripts > Other Script, then pick this file. Keep assets/ next to it.
// All sizes are px at 1080x1350 (1px = 1pt). Coordinates below are measured from each artboard's top left,
// the same numbers as the HTML mocks, and converted to Illustrator's y-up space by X() and Y().
(function () {
  var W = 1080, H = 1350, M = 65;
  var here = File($.fileName).parent;

  // Map grid: dot centre = (MAP_X + 9 + 18i, MAP_Y + 9 + 18j). Generated from Natural Earth 1:50m, see source/make_dots.py.
  var MAP_X = 269, MAP_Y = 405, S = 18;
  var P = [16,0,17,0,18,0,13,1,14,1,15,1,16,1,17,1,18,1,19,1,12,2,13,2,14,2,15,2,16,2,17,2,18,2,19,2,20,2,21,2,22,2,23,2,9,3,11,3,12,3,13,3,14,3,15,3,16,3,17,3,18,3,19,3,20,3,21,3,22,3,23,3,5,4,6,4,9,4,10,4,11,4,12,4,13,4,14,4,15,4,16,4,17,4,18,4,19,4,20,4,21,4,22,4,23,4,2,5,3,5,4,5,5,5,6,5,7,5,8,5,9,5,10,5,11,5,12,5,13,5,14,5,15,5,16,5,17,5,18,5,19,5,20,5,21,5,22,5,23,5,1,6,2,6,3,6,4,6,5,6,6,6,7,6,8,6,9,6,10,6,11,6,12,6,13,6,14,6,15,6,16,6,17,6,18,6,19,6,20,6,21,6,22,6,1,7,2,7,3,7,4,7,5,7,6,7,7,7,8,7,9,7,10,7,11,7,12,7,13,7,14,7,15,7,16,7,17,7,18,7,19,7,20,7,2,8,3,8,4,8,5,8,6,8,7,8,8,8,9,8,10,8,11,8,12,8,13,8,14,8,15,8,16,8,17,8,18,8,19,8,0,9,1,9,2,9,3,9,4,9,5,9,6,9,7,9,8,9,9,9,10,9,11,9,12,9,13,9,14,9,15,9,16,9,17,9,18,9,19,9,1,10,2,10,3,10,4,10,5,10,6,10,7,10,8,10,9,10,10,10,11,10,12,10,13,10,14,10,15,10,16,10,17,10,18,10,19,10,1,11,2,11,3,11,4,11,5,11,6,11,7,11,8,11,9,11,10,11,11,11,12,11,13,11,14,11,15,11,16,11,17,11,18,11,19,11,1,12,2,12,3,12,4,12,5,12,6,12,7,12,8,12,9,12,10,12,11,12,12,12,13,12,14,12,15,12,16,12,17,12,18,12,19,12,2,13,3,13,4,13,5,13,10,13,11,13,12,13,13,13,14,13,15,13,16,13,17,13,18,13,19,13,3,14,4,14,12,14,13,14,14,14,15,14,16,14,17,14,18,14,19,14,20,14,13,15,14,15,15,15,16,15,17,15,18,15,19,15,20,15,21,15,22,15,13,16,14,16,15,16,16,16,17,16,18,16,19,16,20,16,21,16,22,16,23,16,13,17,14,17,15,17,16,17,17,17,18,17,19,17,20,17,21,17,22,17,23,17,24,17,14,18,15,18,16,18,17,18,18,18,19,18,20,18,21,18,22,18,23,18,24,18,14,19,15,19,16,19,17,19,18,19,19,19,20,19,21,19,22,19,23,19,24,19,15,20,16,20,17,20,18,20,19,20,20,20,21,20,22,20,23,20,24,20,25,20,16,21,17,21,18,21,19,21,20,21,21,21,22,21,23,21,24,21,25,21,17,22,18,22,19,22,20,22,21,22,22,22,23,22,24,22,25,22,26,22,18,23,19,23,20,23,21,23,22,23,23,23,24,23,25,23,26,23,27,23,28,23,19,24,20,24,21,24,22,24,23,24,24,24,25,24,26,24,27,24,28,24,29,24,30,24,31,24,32,24,20,25,21,25,22,25,23,25,24,25,25,25,26,25,27,25,28,25,29,25,30,25,31,25,32,25,21,26,22,26,23,26,24,26,25,26,26,26,27,26,28,26,29,26,30,26,31,26,32,26,25,27,26,27,27,27,28,27,29,27,30,27,31,27,32,27,33,27,34,27,8,28,9,28,26,28,27,28,28,28,29,28,30,28,31,28,32,28,33,28,34,28,35,28,36,28,5,29,6,29,7,29,8,29,9,29,10,29,27,29,28,29,29,29,30,29,31,29,32,29,33,29,34,29,35,29,36,29,37,29,6,30,7,30,8,30,9,30,10,30,29,30,30,30,31,30,32,30,33,30,34,30,35,30,36,30,37,30,38,30,39,30,6,31,7,31,8,31,9,31,10,31,29,31,30,31,31,31,32,31,33,31,34,31,35,31,37,31,38,31,39,31,40,31,6,32,7,32,8,32,9,32,10,32,30,32,31,32,32,32,33,32,34,32,40,32,6,33,7,33,8,33,9,33,10,33,32,33,33,33,34,33,40,33,7,34,8,34,9,34,10,34,32,34,33,34,34,34,6,35,7,35,8,35,9,35,10,35,32,35,33,35,34,35,35,35,6,36,7,36,8,36,9,36,33,36,34,36,35,36,36,36,6,37,7,37,33,37,34,37,35,37,36,37,33,38,34,38,33,39,34,39,32,40,33,40,34,40,32,41,33,41,21,42,22,42,23,42,28,42,29,42,30,42,32,42,20,43,21,43,22,43,23,43,24,43,25,43,26,43,27,43,28,43,29,43,21,44,22,44,23,44,24,44,25,44,26,44,27,44,28,44,29,44,23,45,24,45,25,45,26,45,27,45,28,45,29,45,25,46,26,46,27,46,28,46,29,46,27,47,28,47,29,47,28,48,29,48];
  // Route for the dot and merge variants: Milano, Bologna, Roma, Napoli (grid indices).
  var ROUTE = [[8, 7], [16, 12], [20, 24], [27, 29]];

  var FONTS = {
    head: ['MuseoSlab-700', 'Arvo-Bold'],
    headItalic: ['MuseoSlab-700Italic', 'MuseoSlab-700', 'Arvo-BoldItalic', 'Arvo-Bold'],
    reg: ['BeVietnamPro-Regular', 'ArialMT'],
    semi: ['BeVietnamPro-SemiBold', 'BeVietnamPro-Bold', 'Arial-BoldMT'],
    bold: ['BeVietnamPro-Bold', 'Arial-BoldMT'],
    xbold: ['BeVietnamPro-ExtraBold', 'BeVietnamPro-Bold', 'Arial-BoldMT']
  };
  var missing = [];
  var fontCache = {};
  function font(key) {
    if (fontCache[key]) return fontCache[key];
    var list = FONTS[key];
    for (var i = 0; i < list.length; i++) {
      try {
        var f = app.textFonts.getByName(list[i]);
        if (i > 0) missing.push(list[0] + ' (used ' + list[i] + ')');
        fontCache[key] = f;
        return f;
      } catch (e) {}
    }
    missing.push(list[0] + ' (used default)');
    fontCache[key] = app.textFonts[0];
    return fontCache[key];
  }

  var doc = app.documents.add(DocumentColorSpace.RGB, W, H, 6, DocumentArtboardLayout.GridByRow, 120, 2);
  var NAMES = ['V1-P1 Dotted Italy', 'V1-P2 Dotted Italy', 'V2-P1 Autostrada', 'V2-P2 Autostrada', 'V3-P1 Map + motorway', 'V3-P2 Map + motorway'];

  // Brand swatches as global process colours, so a swatch edit updates every artboard.
  function hexRGB(hex) {
    var c = new RGBColor();
    c.red = parseInt(hex.substr(1, 2), 16);
    c.green = parseInt(hex.substr(3, 2), 16);
    c.blue = parseInt(hex.substr(5, 2), 16);
    return c;
  }
  function globalSwatch(name, hex) {
    var sp = doc.spots.add();
    sp.name = name;
    sp.colorType = ColorModel.PROCESS;
    sp.color = hexRGB(hex);
    return sp;
  }
  function tint(spot, t) {
    var c = new SpotColor();
    c.spot = spot;
    c.tint = t === undefined ? 100 : t;
    return c;
  }
  var SW = {
    violet: globalSwatch('Deep Violet', '#400685'),
    blue: globalSwatch('Celestial Blue', '#008FC4'),
    green: globalSwatch('Electric Green', '#2DB34A'),
    gold: globalSwatch('Yellow Gold', '#FFB310'),
    teal: globalSwatch('Teal Meridian', '#006D5B'),
    red: globalSwatch('Prometheus Red', '#F76336'),
    gray: globalSwatch('Dark Gray', '#6D757A'),
    silver: globalSwatch('Silver', '#CFD2D4'),
    black: globalSwatch('Truvio Black', '#000000'),
    white: globalSwatch('Truvio White', '#FFFFFF')
  };
  var STOP_SW = [SW.violet, SW.blue, SW.green, SW.gold];
  var STOP_HEX = ['#400685', '#008FC4', '#2DB34A', '#FFB310'];

  // Primary gradient. 25.4 degrees in Illustrator's own convention, as the brand guidelines set it.
  var grad = doc.gradients.add();
  grad.name = 'Truvio Primary 25.4';
  grad.type = GradientType.LINEAR;
  while (grad.gradientStops.length < 4) grad.gradientStops.add();
  for (var gs = 0; gs < 4; gs++) {
    grad.gradientStops[gs].rampPoint = [0, 34, 68, 100][gs];
    grad.gradientStops[gs].midPoint = 50;
    grad.gradientStops[gs].color = tint(STOP_SW[gs]);
  }
  function gradientFill() {
    var g = new GradientColor();
    g.gradient = grad;
    g.angle = 25.4;
    return g;
  }

  // Layers, top to bottom.
  function layer(name) {
    var l = doc.layers.add();
    l.name = name;
    return l;
  }
  var LAYER_ORDER = ['Guides', 'Logo', 'Copy', 'UI chips', 'Signs', 'Map dots'];
  var LAYERS = {};
  for (var li = LAYER_ORDER.length - 1; li >= 0; li--) LAYERS[LAYER_ORDER[li]] = layer(LAYER_ORDER[li]);
  try { doc.layers.getByName('Layer 1').remove(); } catch (e) {}

  var R; // active artboard rect [left, top, right, bottom]
  var AB_NAME;
  function X(x) { return R[0] + x; }
  function Y(y) { return R[1] - y; }
  function group(layerName, label) {
    var g = LAYERS[layerName].groupItems.add();
    g.name = AB_NAME.split(' ')[0] + ' ' + label;
    return g;
  }

  function style(p, fill, stroke, sw) {
    if (fill) { p.filled = true; p.fillColor = fill; } else { p.filled = false; }
    if (stroke) { p.stroked = true; p.strokeColor = stroke; p.strokeWidth = sw || 1; } else { p.stroked = false; }
    return p;
  }
  function rect(g, x, y, w, h, fill, stroke, sw, r) {
    var p = r ? g.pathItems.roundedRectangle(Y(y), X(x), w, h, r, r) : g.pathItems.rectangle(Y(y), X(x), w, h);
    return style(p, fill, stroke, sw);
  }
  // A stroked box drawn so the stroke sits fully inside x, y, w, h, like CSS box-sizing border-box.
  function innerBox(g, x, y, w, h, stroke, sw, r) {
    return rect(g, x + sw / 2, y + sw / 2, w - sw, h - sw, null, stroke, sw, r);
  }
  function circle(g, cx, cy, d, fill, stroke, sw) {
    var p = g.pathItems.ellipse(Y(cy - d / 2), X(cx - d / 2), d, d);
    return style(p, fill, stroke, sw);
  }
  // pts are [x, y] pairs in a local box scaled by s and placed at ox, oy.
  function poly(g, pts, ox, oy, s, closed, fill, stroke, sw) {
    var a = [];
    for (var i = 0; i < pts.length; i++) a.push([X(ox + pts[i][0] * s), Y(oy + pts[i][1] * s)]);
    var p = g.pathItems.add();
    p.setEntirePath(a);
    p.closed = closed;
    style(p, fill, stroke, sw);
    if (stroke) { p.strokeCap = StrokeCap.ROUNDENDCAP; p.strokeJoin = StrokeJoin.ROUNDENDJOIN; }
    return p;
  }

  function text(g, str, x, y, fontKey, size, color, tracking) {
    var tf = g.textFrames.add();
    tf.contents = str;
    var ca = tf.textRange.characterAttributes;
    ca.textFont = font(fontKey);
    ca.size = size;
    ca.fillColor = color;
    if (tracking) ca.tracking = tracking;
    tf.position = [X(x), Y(y)];
    return tf;
  }
  function textRight(g, str, right, y, fontKey, size, color) {
    var tf = text(g, str, 0, y, fontKey, size, color);
    tf.position = [X(right) - tf.width, Y(y)];
    return tf;
  }
  function textCentered(g, str, cx, cy, fontKey, size, color) {
    var tf = text(g, str, 0, 0, fontKey, size, color);
    tf.position = [X(cx) - tf.width / 2, Y(cy) + tf.height / 2];
    return tf;
  }
  function areaText(g, str, x, y, w, h, fontKey, size, color, leading) {
    var box = g.pathItems.rectangle(Y(y), X(x), w, h);
    var tf = g.textFrames.areaText(box);
    tf.contents = str;
    var ca = tf.textRange.characterAttributes;
    ca.textFont = font(fontKey);
    ca.size = size;
    ca.fillColor = color;
    ca.autoLeading = false;
    ca.leading = leading || size * 1.3;
    return tf;
  }

  // Icons, drawn on a 24px grid like the mock's inline SVGs.
  var ICON = {
    pause: function (g, x, y, s, c) { poly(g, [[9, 5], [9, 19]], x, y, s, false, null, c, 3 * s); poly(g, [[15, 5], [15, 19]], x, y, s, false, null, c, 3 * s); },
    clock: function (g, x, y, s, c) { circle(g, x + 12 * s, y + 12 * s, 18 * s, null, c, 2.5 * s); poly(g, [[12, 7], [12, 12], [15, 14]], x, y, s, false, null, c, 2.5 * s); },
    warn: function (g, x, y, s, c) { poly(g, [[12, 4], [21, 20], [3, 20]], x, y, s, true, null, c, 2.5 * s); poly(g, [[12, 10], [12, 14]], x, y, s, false, null, c, 2.5 * s); circle(g, x + 12 * s, y + 17.3 * s, 2.6 * s, c, null); },
    check: function (g, x, y, s, c) { poly(g, [[5, 12], [10, 17], [20, 7]], x, y, s, false, null, c, 3.5 * s); }
  };
  var ARROW_UP = [[28, 0], [56, 30], [38, 30], [38, 72], [18, 72], [18, 30], [0, 30]];
  function arrowUp(g, x, y, h, c) { poly(g, ARROW_UP, x, y, h / 72, true, c, null); }
  function arrowTurn(g, x, y, size, c) {
    var s = size / 84;
    poly(g, [[18, 84], [18, 34], [62, 34]], x, y, s, false, null, c, 12 * s).strokeCap = StrokeCap.BUTTENDCAP;
    poly(g, [[54, 16], [76, 34], [54, 52]], x, y, s, true, c, null);
  }

  // White status chip: icon + label. If right is true, x is the chip's right edge.
  function chip(g, x, y, label, icon, iconColor, right) {
    var cg = g.groupItems.add();
    cg.name = 'Chip ' + label;
    var tf = text(cg, label, 0, 0, 'semi', 22, tint(SW.black));
    var w = 16 + 22 + 10 + tf.width + 16, h = 48;
    var left = right ? x - w : x;
    var bg = rect(cg, left, y, w, h, tint(SW.white), tint(SW.silver), 1, 12);
    bg.zOrder(ZOrderMethod.SENDTOBACK);
    ICON[icon](cg, left + 16, y + 13, 22 / 24, iconColor);
    tf.position = [X(left + 48), Y(y + (h - tf.height) / 2)];
    return cg;
  }

  function header(eyebrow) {
    var lg = group('Logo', 'Truvio logo');
    var f = File(here + '/assets/truvio-logo-violet.svg');
    if (f.exists) {
      var logo = lg.groupItems.createFromFile(f);
      var s = 160 / logo.width * 100;
      logo.resize(s, s);
      logo.position = [X(M), Y(M)];
    } else {
      rect(lg, M, M, 160, 53, null, tint(SW.silver), 2, 8);
      text(lg, 'Truvio logo', M + 32, M + 16, 'semi', 16, tint(SW.gray));
    }
    var cg = group('Copy', 'Eyebrow');
    var tf = text(cg, eyebrow, 0, 0, 'semi', 20, tint(SW.violet));
    tf.position = [X(W - M) - tf.width, Y(M + (53 - tf.height) / 2)];
  }
  function headline(line1, line2, size) {
    var g = group('Copy', 'Headline');
    text(g, line1, M, 160, 'head', size, tint(SW.violet), -10);
    text(g, line2, M, 160 + size * 1.12, 'headItalic', size, tint(SW.blue), -10);
  }
  function sub(str) {
    var g = group('Copy', 'Sub');
    areaText(g, str, M, 1190, 540, 95, 'reg', 32, tint(SW.black), 41.6);
  }
  function ground(y) {
    rect(group('Signs', 'Ground line'), M, y, W - 2 * M, 2, tint(SW.silver), null);
  }

  // Map dots.
  function dotXY(i, j) { return [MAP_X + 9 + S * i, MAP_Y + 9 + S * j]; }
  function near(i, j) {
    var best = null;
    for (var k = 0; k < ROUTE.length - 1; k++) {
      var a = ROUTE[k], b = ROUTE[k + 1], dx = b[0] - a[0], dy = b[1] - a[1];
      var t = ((i - a[0]) * dx + (j - a[1]) * dy) / (dx * dx + dy * dy);
      t = Math.max(0, Math.min(1, t));
      var qx = a[0] + t * dx - i, qy = a[1] + t * dy - j, dist = Math.sqrt(qx * qx + qy * qy);
      if (!best || dist < best.dist) best = { dist: dist, k: k, t: t };
    }
    return best;
  }
  function mixHex(a, b, t) {
    var A = hexRGB(a), B = hexRGB(b), c = new RGBColor();
    c.red = Math.round(A.red + (B.red - A.red) * t);
    c.green = Math.round(A.green + (B.green - A.green) * t);
    c.blue = Math.round(A.blue + (B.blue - A.blue) * t);
    return c;
  }
  // One compound path per dot set, so a set takes a single fill (a global swatch or the live gradient).
  function dotSet(g, name, list, d, fill) {
    if (!list.length) return null;
    var cp = g.compoundPathItems.add();
    cp.name = name;
    for (var n = 0; n < list.length; n++) {
      var c = dotXY(list[n][0], list[n][1]);
      cp.pathItems.ellipse(Y(c[1] - d / 2), X(c[0] - d / 2), d, d);
    }
    for (var m = 0; m < cp.pathItems.length; m++) style(cp.pathItems[m], fill, null);
    return cp;
  }
  // Route dots carry their own colour along the route (blended between the stops), so they stay separate paths.
  function routeDots(g, litSegments, base, stalledFill) {
    var plain = [], stalled = [], lit = [];
    for (var n = 0; n < P.length; n += 2) {
      var i = P[n], j = P[n + 1], r = near(i, j);
      if (r.dist >= 0.8) plain.push([i, j]);
      else if (r.k < litSegments) lit.push([i, j, r]);
      else stalled.push([i, j]);
    }
    dotSet(g, 'Dots base', plain, 10, base);
    dotSet(g, 'Route stalled', stalled, 12, stalledFill);
    var rg = g.groupItems.add();
    rg.name = 'Route lit';
    for (var q = 0; q < lit.length; q++) {
      var c = dotXY(lit[q][0], lit[q][1]), rr = lit[q][2];
      circle(rg, c[0], c[1], 12, mixHex(STOP_HEX[rr.k], STOP_HEX[rr.k + 1], rr.t), null);
    }
  }

  // Autostrada sign pieces.
  function signPanel(g, x, y, w, h, bg, line, pad, lineW, r, rInner) {
    rect(g, x, y, w, h, bg, null, 0, r);
    innerBox(g, x + pad, y + pad, w - 2 * pad, h - 2 * pad, line, lineW, rInner);
  }
  function shield(g, x, y, w, h, size, lineW, r) {
    innerBox(g, x, y, w, h, tint(SW.white), lineW, r);
    textCentered(g, 'AP', x + w / 2, y + h / 2, 'xbold', size, tint(SW.white));
  }
  function checkDisc(g, x, y) {
    circle(g, x + 24, y + 24, 48, tint(SW.white), null);
    ICON.check(g, x + 10, y + 10, 28 / 24, tint(SW.teal));
  }

  // ---- The six artboards ----
  var BUILD = [
    function v1p1() {
      header('2026 AP Automation Report');
      headline('Your AP is automated.', 'Or is it?', 72);
      var g = group('Map dots', 'Map');
      var stuckKeys = { '19,7': 1, '20,24': 1, '35,28': 1 };
      var live = [], grey = [];
      for (var n = 0; n < P.length; n += 2) {
        var i = P[n], j = P[n + 1];
        if (stuckKeys[i + ',' + j] || (i * 7 + j * 13) % 31 === 0) grey.push([i, j]); else live.push([i, j]);
      }
      dotSet(g, 'Dots gradient', live, 10, gradientFill());
      dotSet(g, 'Dots stuck', grey, 10, tint(SW.silver));
      var u = group('UI chips', 'Stuck invoices');
      circle(u, 620, 540, 34, null, tint(SW.gray), 2);
      circle(u, 638, 846, 34, null, tint(SW.gray), 2);
      circle(u, 908, 918, 34, null, tint(SW.gray), 2);
      rect(u, 907, 798, 2, 102, tint(SW.gray), null);
      chip(u, 652, 516, 'Verifica manuale', 'pause', tint(SW.gray), false);
      chip(u, 606, 822, 'In attesa di approvazione', 'clock', tint(SW.gray), true);
      chip(u, 1015, 750, 'Importo non corrispondente', 'warn', tint(SW.red), true);
      sub('See what 1,000 finance professionals revealed.');
    },
    function v1p2() {
      header('Dynamics 365 Finance & Operations');
      headline('Less invoice chasing.', 'More finance thinking.', 72);
      routeDots(group('Map dots', 'Map'), 3, tint(SW.silver), tint(SW.silver));
      var u = group('UI chips', 'Route stops');
      var stops = [[422, 540], [566, 630], [638, 846], [764, 936]];
      var numInk = [SW.white, SW.white, SW.black, SW.black];
      for (var s = 0; s < 4; s++) {
        circle(u, stops[s][0], stops[s][1], 34, tint(STOP_SW[s]), tint(SW.white), 3);
        textCentered(u, String(s + 1), stops[s][0], stops[s][1], 'xbold', 16, tint(numInk[s]));
      }
      var c = group('UI chips', 'Step card');
      rect(c, 720, 430, 295, 270, tint(SW.white), tint(SW.silver), 1, 16);
      text(c, 'Fattura 0418', 740, 452, 'reg', 16, tint(SW.gray));
      rect(c, 893, 448, 102, 26, tint(SW.green, 12), null, 0, 13);
      textCentered(c, 'Automatico', 944, 461, 'bold', 14, tint(SW.black));
      var steps = ['Acquisizione', 'Abbinamento', 'Approvazione', 'Registrazione'];
      for (var k = 0; k < 4; k++) {
        var top = 486 + k * 50;
        rect(c, 740, top, 255, 1, tint(SW.silver), null);
        circle(c, 753, top + 23, 26, tint(STOP_SW[k]), null);
        textCentered(c, String(k + 1), 753, top + 23, 'xbold', 13, tint(numInk[k]));
        text(c, steps[k], 778, top + 11, 'semi', 20, tint(SW.black));
        ICON.check(c, 973, top + 13, 20 / 24, tint(SW.green));
      }
      sub('Put routine AP work on autopilot.');
    },
    function v2p1() {
      header('2026 AP Automation Report');
      headline('Your AP is automated.', 'Or is it?', 72);
      var g = group('Signs', 'Autostrada detour');
      rect(g, 300, 900, 24, 250, tint(SW.gray), null);
      rect(g, 756, 900, 24, 250, tint(SW.gray), null);
      signPanel(g, 115, 420, 850, 380, tint(SW.teal), tint(SW.white), 14, 4, 24, 14);
      shield(g, 169, 508, 112, 72, 40, 4, 12);
      text(g, 'Fattura registrata', 309, 513, 'bold', 50, tint(SW.white));
      arrowUp(g, 855, 508, 72, tint(SW.white));
      rect(g, 169, 608, 742, 4, tint(SW.white), null, 0, 2);
      text(g, 'Pagamento', 309, 645, 'bold', 50, tint(SW.white));
      arrowUp(g, 855, 640, 72, tint(SW.white));
      signPanel(g, 115, 816, 850, 180, tint(SW.gold), tint(SW.black), 12, 4, 18, 10);
      text(g, 'Deviazione', 167, 860, 'bold', 24, tint(SW.black));
      text(g, 'Verifica manuale', 167, 892, 'xbold', 50, tint(SW.black));
      arrowTurn(g, 825, 864, 84, tint(SW.black));
      ground(1150);
      sub('See what 1,000 finance professionals revealed.');
    },
    function v2p2() {
      header('Dynamics 365 Finance & Operations');
      headline('Less invoice chasing.', 'More finance thinking.', 72);
      var g = group('Signs', 'Autostrada autopilot');
      rect(g, 300, 1000, 24, 150, tint(SW.gray), null);
      rect(g, 756, 1000, 24, 150, tint(SW.gray), null);
      signPanel(g, 115, 420, 850, 600, tint(SW.teal), tint(SW.white), 14, 4, 24, 14);
      shield(g, 169, 466, 112, 72, 40, 4, 12);
      text(g, 'Pilota automatico', 309, 474, 'bold', 46, tint(SW.white));
      arrowUp(g, 855, 466, 72, tint(SW.white));
      rect(g, 169, 584, 742, 4, tint(SW.white), null, 0, 2);
      var rows = ['Acquisizione', 'Abbinamento', 'Approvazione', 'Registrazione'];
      for (var k = 0; k < 4; k++) {
        var top = 635 + k * 96.4;
        text(g, rows[k], 169, top + 2, 'bold', 42, tint(SW.white));
        checkDisc(g, 863, top);
      }
      ground(1150);
      sub('Put routine AP work on autopilot.');
    },
    function v3p1() {
      header('2026 AP Automation Report');
      headline('Your AP is automated.', 'Or is it?', 72);
      routeDots(group('Map dots', 'Map'), 2, tint(SW.silver, 60), tint(SW.gray, 65));
      var g = group('Signs', 'Route signs');
      rect(g, 322, 514, 84, 52, tint(SW.teal), null, 0, 10);
      shield(g, 326, 518, 76, 44, 24, 3, 7);
      circle(g, 638, 846, 40, tint(SW.white), tint(SW.gold), 4);
      signPanel(g, 250, 790, 350, 112, tint(SW.gold), tint(SW.black), 7, 3, 12, 7);
      text(g, 'Deviazione', 278, 821, 'bold', 16, tint(SW.black));
      text(g, 'Verifica manuale', 278, 842, 'xbold', 24, tint(SW.black));
      arrowTurn(g, 532, 826, 40, tint(SW.black));
      sub('See what 1,000 finance professionals revealed.');
    },
    function v3p2() {
      header('Dynamics 365 Finance & Operations');
      headline('Less invoice chasing.', 'More finance thinking.', 72);
      routeDots(group('Map dots', 'Map'), 3, tint(SW.silver, 60), tint(SW.gray, 65));
      var g = group('Signs', 'Route signs');
      rect(g, 322, 514, 84, 52, tint(SW.teal), null, 0, 10);
      shield(g, 326, 518, 76, 44, 24, 3, 7);
      circle(g, 764, 936, 40, tint(SW.white), tint(SW.gold), 4);
      signPanel(g, 390, 880, 340, 112, tint(SW.teal), tint(SW.white), 7, 3, 12, 7);
      text(g, 'Pilota automatico', 418, 911, 'bold', 16, tint(SW.white));
      text(g, 'Registrazione', 418, 932, 'xbold', 24, tint(SW.white));
      arrowUp(g, 672, 916, 40, tint(SW.white));
      sub('Put routine AP work on autopilot.');
    }
  ];

  for (var a = 0; a < BUILD.length; a++) {
    var ab = doc.artboards[a];
    ab.name = NAMES[a];
    doc.artboards.setActiveArtboardIndex(a);
    R = ab.artboardRect;
    AB_NAME = NAMES[a];
    var guide = LAYERS['Guides'].pathItems.rectangle(Y(M), X(M), W - 2 * M, H - 2 * M);
    guide.guides = true;
    BUILD[a]();
  }
  LAYERS['Guides'].locked = true;
  doc.artboards.setActiveArtboardIndex(0);

  var msg = 'Built ' + BUILD.length + ' artboards.';
  if (missing.length) msg += '\n\nFonts not found, substituted:\n' + missing.join('\n');
  alert(msg);
})();
