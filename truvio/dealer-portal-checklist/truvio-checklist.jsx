/*
    TRUVIO CHECKLIST  -  After Effects build script (written for AE 2026)
    =====================================================================

    Rebuilds the reference "checklist" clip in Truvio branding:
      - off-white brand gradient background (25.4 deg brand angle)
      - heading: "One dealer portal. Four fewer headaches."
      - four checklist rows that tick one by one (no strikethrough)
      - Truvio colour lockup at the bottom
      - seamless loop: after a hold, every box unchecks and the clip resets

    RUN IT
      File > Scripts > Run Script File...  and pick this file.
      It builds a new comp inside a "Truvio Checklist" project folder.
      Nothing is rendered or added to the render queue.

    SAVE THE .AEP
      Run it in a new, unsaved project and it saves "Truvio Checklist.aep"
      next to this script. It never overwrites a file and never re-saves a
      project that already has one. Turn it off with CONFIG.saveAep.

    SCALE THE CHECKLIST
      The card and everything on it (checkboxes, text, emoji, dividers, shadow)
      is parented to the CHECKLIST null and scales around the card's centre.
      Change "Checklist Scale" on the CONTROLS layer (starts at 75%).
      The heading and logo stay on the safe margins. Text and shapes stay sharp,
      but the Character panel shows the unscaled 36px size.

    CHANGE COLOURS LATER
      Select the CONTROLS layer (top of the comp) and open Effect Controls.
      Every colour in the comp is linked to one of those swatches. The same
      swatches are also listed in the Essential Graphics panel.
      Don't rename the CONTROLS layer or its effects: expressions find them by name.

    CHANGE TEXT LATER
      Double-click any text layer in the comp and type. The card resizes to fit
      the longest line, and each emoji follows the end of its line.

    RETIME
      Every tick is plain keyframes on the "Item N Checkbox" layers
      (Scale, Box > Fill > Opacity, Tick > Trim > End). Comp markers show each beat.
      Or change CONFIG.timing below and re-run.

    This file is pure ASCII on purpose (emoji are \u escapes), so it survives
    any text-encoding setting in After Effects.
*/

(function buildTruvioChecklist() {

    // =====================================================================
    //  CONFIG  -  everything you'd normally tweak lives here
    // =====================================================================
    var CONFIG = {
        compName: "Truvio Checklist",
        width: 1080,
        height: 1080,
        fps: 60,          // the reference clip is 60fps; 30 also works
        margin: 65,       // safe margin: 6% of the short edge
        checklistScale: 75,   // percent; the card and its rows. Live on CONTROLS > Checklist Scale
        saveAep: true,        // save "<compName>.aep" next to this script when run in an unsaved project

        heading: ["One dealer portal.", "Four fewer headaches."],   // one entry per line

        items: [
            { text: "No more phone-in parts orders",                    emoji: "\uD83D\uDCF1" },  // mobile phone
            { text: "HIN and warranty lookups in seconds",              emoji: "\uD83D\uDD0D" },  // magnifying glass
            { text: "Claims without the paperwork chase",               emoji: "\uD83D\uDCC3" },  // page with curl
            { text: "No more \u201Cwhat\u2019s my bonus?\u201D emails", emoji: "\u2709" }         // envelope
        ],

        fonts: {
            heading: "MuseoSlab-700",         // Truvio headline font
            item:    "BeVietnamPro-Medium",   // Truvio body font
            emoji:   "AppleColorEmoji"
        },
        headingSize: 62,
        headingLeading: 72,
        itemSize: 36,     // shrinks automatically if the longest line won't fit

        logo: {
            path: "~/Documents/Truvio CoWork/ABOUT ME/truvio-brand/ad-render-kit/assets/truvio-lockup-colour.png",
            width: 200    // px, same as the ad-render-kit lockup
        },

        // Starting colours. After the build, change them on the CONTROLS layer instead.
        colors: {
            bgStart:           "#E6E8FC",   // gradient, lower-left end
            bgEnd:             "#F8F9FE",   // gradient, upper-right end
            bgAngle:           25.4,        // Truvio brand gradient angle (degrees)
            heading:           "#400685",   // Deep Violet
            itemText:          "#400685",   // Deep Violet
            cardFill:          "#F3EFFB",
            cardBorder:        "#FFFFFF",
            cardShadow:        "#400685",
            cardShadowOpacity: 10,          // percent
            divider:           "#E1D8EF",
            checkboxOutline:   "#400685",   // Deep Violet
            checkboxChecked:   "#2DB34A",   // Electric Green
            checkmark:         "#FFFFFF"
        },

        // Pixel sizes at 1080x1080, scaled from the 720px reference.
        // The card and rows are drawn at these sizes, then scaled by checklistScale.
        layout: {
            cardRadius:    46,
            cardBorder:    4,
            cardPadLeft:   56,
            cardPadRight:  58,
            cardPadV:      12,
            rowPitch:      150,
            boxSize:       62,
            boxRadius:     17,
            boxStroke:     4.5,
            tickStroke:    6.5,
            textGap:       26,   // checkbox to text
            emojiGap:      12,   // text to emoji
            dividerHeight: 2,
            shadowOffset:  18,
            shadowBlur:    60
        },

        // Seconds
        timing: {
            firstCheck:     0.60,   // first tick (reference: 0.58s)
            stagger:        0.75,   // gap between ticks (reference: 0.75s)
            hold:           1.40,   // all-checked hold before the reset
            uncheckStagger: 0.05,
            endHold:        0.45    // unchecked hold at the end (plus firstCheck = the loop pause)
        }
    };

    // =====================================================================
    //  Names the expressions depend on. Don't rename these in AE.
    // =====================================================================
    var CTRL = "CONTROLS";
    var LAYOUT = "LAYOUT";
    var CHECKLIST = "CHECKLIST";
    var SCALE_CTRL = "Checklist Scale";

    // [effect name on CONTROLS, type, CONFIG.colors key, Essential Graphics label]
    var CONTROL_SPEC = [
        ["BG Start Color",      "color",  "bgStart",           "Background: start"],
        ["BG End Color",        "color",  "bgEnd",             "Background: end"],
        ["BG Angle",            "angle",  "bgAngle",           "Background: angle"],
        ["Heading",             "color",  "heading",           "Heading text"],
        ["Item Text",           "color",  "itemText",          "Checklist text"],
        ["Card Fill",           "color",  "cardFill",          "Card fill"],
        ["Card Border",         "color",  "cardBorder",        "Card border"],
        ["Card Shadow",         "color",  "cardShadow",        "Card shadow"],
        ["Card Shadow Opacity", "slider", "cardShadowOpacity", "Card shadow opacity"],
        ["Divider",             "color",  "divider",           "Divider lines"],
        ["Checkbox Outline",    "color",  "checkboxOutline",   "Checkbox: outline"],
        ["Checkbox Checked",    "color",  "checkboxChecked",   "Checkbox: checked fill"],
        ["Checkmark",           "color",  "checkmark",         "Checkmark"]
    ];

    var L = CONFIG.layout, T = CONFIG.timing, C = CONFIG.colors;
    var W = CONFIG.width, H = CONFIG.height, M = CONFIG.margin;
    var N = CONFIG.items.length;
    var SCALE = CONFIG.checklistScale / 100;
    var TEXT_LEFT = L.cardPadLeft + L.boxSize + L.textGap;   // card's left edge to the start of each line
    var CHECK_DUR = 0.32;     // press, fill, tick: measured from the reference
    var UNCHECK_DUR = 0.24;
    var warnings = [];

    // =====================================================================
    //  Helpers
    // =====================================================================
    function hexToRgb(h) {
        h = h.replace("#", "");
        return [parseInt(h.substr(0, 2), 16) / 255, parseInt(h.substr(2, 2), 16) / 255, parseInt(h.substr(4, 2), 16) / 255];
    }
    function warn(msg) {
        for (var i = 0; i < warnings.length; i++) if (warnings[i] === msg) return;
        warnings.push(msg);
    }
    function ctrl(name) { return 'thisComp.layer("' + CTRL + '").effect("' + name + '")(1)'; }
    function cardWidth() { return 'thisComp.layer("' + LAYOUT + '").effect("Card Width")(1)'; }
    // x relative to the card's (auto-sized, centred) left edge; keeps the property's own y
    function xFromCardLeft(offset) {
        return 'var w = ' + cardWidth() + ';\n[thisComp.width / 2 - w / 2 + ' + offset + ', value[1]];';
    }
    function transform(layer, matchName) { return layer.property("ADBE Transform Group").property(matchName); }
    // Parent without AE adjusting the child's transform values
    function setParent(child, parent) {
        if (typeof child.setParentWithJump === "function") child.setParentWithJump(parent);
        else child.parent = parent;
    }

    // Adding an effect invalidates older effect references on that layer,
    // so always re-fetch with fx(layer, name) after adding.
    function fxGroup(layer) { return layer.property("ADBE Effect Parade"); }
    function addEffect(layer, matchName, name) { fxGroup(layer).addProperty(matchName).name = name; }
    function fx(layer, name) { return fxGroup(layer).property(name); }
    function param(effect, matchName, fallbackName) {
        var p = effect.property(matchName);
        if (!p && fallbackName) p = effect.property(fallbackName);
        if (!p) throw new Error('Missing parameter "' + matchName + '" on effect "' + effect.name + '"');
        return p;
    }

    // Shape layers. Same rule: fetch by name after every add.
    function rootVectors(layer) { return layer.property("ADBE Root Vectors Group"); }
    function groupContents(layer, groupName) { return rootVectors(layer).property(groupName).property("ADBE Vectors Group"); }
    function item(layer, groupName, itemName) { return groupContents(layer, groupName).property(itemName); }

    function addShapeLayer(comp, name, pos) {
        var s = comp.layers.addShape();
        s.name = name;
        transform(s, "ADBE Position").setValue(pos || [0, 0]);   // [0,0] means contents use comp coordinates
        return s;
    }
    function addGroup(layer, name) { rootVectors(layer).addProperty("ADBE Vector Group").name = name; }
    function addRect(layer, groupName, size, pos, roundness) {
        var r = groupContents(layer, groupName).addProperty("ADBE Vector Shape - Rect");
        r.name = "Rect";
        r.property("ADBE Vector Rect Size").setValue(size);
        r.property("ADBE Vector Rect Position").setValue(pos);
        r.property("ADBE Vector Rect Roundness").setValue(roundness);
    }
    function addPath(layer, groupName, vertices) {
        var p = groupContents(layer, groupName).addProperty("ADBE Vector Shape - Group");
        p.name = "Path";
        var s = new Shape();
        s.vertices = vertices;
        s.closed = false;
        p.property("ADBE Vector Shape").setValue(s);
    }
    function addFill(layer, groupName) {
        groupContents(layer, groupName).addProperty("ADBE Vector Graphic - Fill").name = "Fill";
    }
    function addStroke(layer, groupName, name, width, round) {
        var s = groupContents(layer, groupName).addProperty("ADBE Vector Graphic - Stroke");
        s.name = name;
        s.property("ADBE Vector Stroke Width").setValue(width);
        if (round) {
            s.property("ADBE Vector Stroke Line Cap").setValue(2);    // round cap
            s.property("ADBE Vector Stroke Line Join").setValue(2);   // round join
        }
    }
    function addTrim(layer, groupName) {
        groupContents(layer, groupName).addProperty("ADBE Vector Filter - Trim").name = "Trim";
    }

    // keys: [[time, value, easeIn%, easeOut%], ...]; ease defaults to 66 (Easy Ease)
    function animate(prop, keys) {
        var i;
        for (i = 0; i < keys.length; i++) prop.setValueAtTime(keys[i][0], keys[i][1]);
        for (i = 0; i < keys.length; i++) {
            var k = prop.nearestKeyIndex(keys[i][0]);
            var inInf = keys[i].length > 2 ? keys[i][2] : 66;
            var outInf = keys[i].length > 3 ? keys[i][3] : inInf;
            prop.setInterpolationTypeAtKey(k, KeyframeInterpolationType.BEZIER, KeyframeInterpolationType.BEZIER);
            setEase(prop, k, inInf, outInf);
        }
    }
    function setEase(prop, k, inInf, outInf) {
        var dims = (!prop.isSpatial && prop.value instanceof Array) ? prop.value.length : 1;
        var tries = [dims, 1, 2, 3];
        for (var t = 0; t < tries.length; t++) {
            try {
                prop.setTemporalEaseAtKey(k, easeList(tries[t], inInf), easeList(tries[t], outInf));
                return;
            } catch (e) {}
        }
    }
    function easeList(n, influence) {
        var a = [];
        for (var d = 0; d < n; d++) a.push(new KeyframeEase(0, influence));
        return a;
    }

    // Text
    function textSource(layer) { return layer.property("ADBE Text Properties").property("ADBE Text Document"); }
    function addText(comp, name, str, font, size, justification, leading, hex) {
        var layer = comp.layers.addText(str);
        layer.name = name;
        var src = textSource(layer);
        var doc = src.value;
        doc.font = font;
        doc.fontSize = size;
        doc.applyFill = true;
        doc.fillColor = hexToRgb(hex);
        doc.applyStroke = false;
        doc.tracking = 0;
        doc.justification = justification;
        if (leading) {
            try { doc.autoLeading = false; } catch (e1) {}
            try { doc.leading = leading; } catch (e2) {}
        }
        src.setValue(doc);
        var used = textSource(layer).value.font;
        if (used !== font) warn('Font "' + font + '" is missing (AE used "' + used + '"). Install it and re-run.');
        return layer;
    }
    function setFontSize(layer, size) {
        var src = textSource(layer);
        var doc = src.value;
        doc.fontSize = size;
        src.setValue(doc);
    }
    function bounds(layer) { return layer.sourceRectAtTime(0, false); }
    function linkTextColor(layer, controlName) {
        addEffect(layer, "ADBE Fill", "Color Link");
        param(fx(layer, "Color Link"), "ADBE Fill-0002", "Color").expression = ctrl(controlName);
    }

    // Project
    function findItem(name, type) {
        for (var i = 1; i <= app.project.numItems; i++) {
            var it = app.project.item(i);
            if (it.name === name && it instanceof type) return it;
        }
        return null;
    }
    function uniqueCompName(base) {
        var name = base, n = 2;
        while (findItem(name, CompItem)) name = base + " " + (n++);
        return name;
    }
    function findFootage(file) {
        for (var i = 1; i <= app.project.numItems; i++) {
            var it = app.project.item(i);
            if (it instanceof FootageItem && it.file && it.file.fsName === file.fsName) return it;
        }
        return null;
    }
    function marker(comp, t, label) {
        try { comp.markerProperty.setValueAtTime(t, new MarkerValue(label)); } catch (e) {}
    }

    // Re-enables every expression and reports any that error, so problems surface at build time
    function checkExpressions(group, layerName, out) {
        for (var i = 1; i <= group.numProperties; i++) {
            var p;
            try { p = group.property(i); } catch (e0) { continue; }
            if (!p) continue;
            if (p.propertyType === PropertyType.PROPERTY) {
                try {
                    if (p.canSetExpression && p.expression !== "") {
                        if (!p.expressionEnabled) p.expressionEnabled = true;
                        p.valueAtTime(0, false);
                        if (p.expressionError) out.push(layerName + " > " + p.name + ": " + p.expressionError);
                    }
                } catch (e1) {}
            } else {
                try { checkExpressions(p, layerName, out); } catch (e2) {}
            }
        }
    }

    // =====================================================================
    //  Build
    // =====================================================================
    function build() {
        var i;
        if (!app.project) app.newProject();

        // ---- timing ------------------------------------------------------
        var checkT = [], uncheckT = [];
        for (i = 0; i < N; i++) checkT.push(T.firstCheck + i * T.stagger);
        var uncheckStart = checkT[N - 1] + CHECK_DUR + T.hold;
        for (i = 0; i < N; i++) uncheckT.push(uncheckStart + i * T.uncheckStagger);
        var duration = uncheckT[N - 1] + UNCHECK_DUR + T.endHold;
        duration = Math.ceil(duration * CONFIG.fps) / CONFIG.fps;

        // ---- project + comp ---------------------------------------------
        var folder = findItem(CONFIG.compName, FolderItem) || app.project.items.addFolder(CONFIG.compName);
        var comp = app.project.items.addComp(uniqueCompName(CONFIG.compName), W, H, 1, duration, CONFIG.fps);
        comp.parentFolder = folder;
        comp.bgColor = hexToRgb(C.bgEnd);

        // ---- CONTROLS: every colour in the comp reads from here -----------
        var controls = comp.layers.addNull(duration);
        controls.name = CTRL;
        controls.guideLayer = true;
        transform(controls, "ADBE Position").setValue([60, 60]);
        for (i = 0; i < CONTROL_SPEC.length; i++) {
            var spec = CONTROL_SPEC[i];
            if (spec[1] === "color") {
                addEffect(controls, "ADBE Color Control", spec[0]);
                param(fx(controls, spec[0]), "ADBE Color Control-0001", "Color").setValue(hexToRgb(C[spec[2]]));
            } else if (spec[1] === "angle") {
                addEffect(controls, "ADBE Angle Control", spec[0]);
                param(fx(controls, spec[0]), "ADBE Angle Control-0001", "Angle").setValue(C[spec[2]]);
            } else {
                addEffect(controls, "ADBE Slider Control", spec[0]);
                param(fx(controls, spec[0]), "ADBE Slider Control-0001", "Slider").setValue(C[spec[2]]);
            }
        }
        addEffect(controls, "ADBE Slider Control", SCALE_CTRL);
        param(fx(controls, SCALE_CTRL), "ADBE Slider Control-0001", "Slider").setValue(CONFIG.checklistScale);

        // ---- LAYOUT: auto card width (expression added once rows exist) ----
        var layout = comp.layers.addNull(duration);
        layout.name = LAYOUT;
        layout.guideLayer = true;
        transform(layout, "ADBE Position").setValue([60, 140]);
        addEffect(layout, "ADBE Slider Control", "Card Width");

        // ---- measure the item font's cap height, for vertical centring ----
        var probe = addText(comp, "probe", "H", CONFIG.fonts.item, CONFIG.itemSize, ParagraphJustification.LEFT_JUSTIFY, 0, C.itemText);
        var capRatio = -bounds(probe).top / CONFIG.itemSize;
        probe.remove();

        // ---- checklist text + emoji --------------------------------------
        var size = CONFIG.itemSize;
        var rows = [];
        for (i = 0; i < N; i++) {
            var n = i + 1;
            var row = { text: null, emoji: null };
            row.text = addText(comp, "Item " + n + " Text", CONFIG.items[i].text, CONFIG.fonts.item, size,
                               ParagraphJustification.LEFT_JUSTIFY, 0, C.itemText);
            if (CONFIG.items[i].emoji) {
                row.emoji = addText(comp, "Item " + n + " Emoji", CONFIG.items[i].emoji, CONFIG.fonts.emoji, size,
                                    ParagraphJustification.LEFT_JUSTIFY, 0, "#000000");
            }
            rows.push(row);
        }

        function widestRow() {
            var m = 0;
            for (var r = 0; r < rows.length; r++) {
                var b = bounds(rows[r].text);
                var w = b.left + b.width;
                if (rows[r].emoji) w += L.emojiGap + bounds(rows[r].emoji).width;
                if (w > m) m = w;
            }
            return m;
        }

        // Shrink the item size until the widest row fits inside the safe margins (after scaling)
        var safeW = W - 2 * M;
        var maxCardW = safeW / SCALE;
        var widest = widestRow();
        for (var pass = 0; pass < 4 && TEXT_LEFT + widest + L.cardPadRight > maxCardW; pass++) {
            size = Math.floor(size * (maxCardW - TEXT_LEFT - L.cardPadRight) / widest);
            for (i = 0; i < N; i++) {
                setFontSize(rows[i].text, size);
                if (rows[i].emoji) setFontSize(rows[i].emoji, size);
            }
            widest = widestRow();
        }
        if (size !== CONFIG.itemSize) warn("Checklist text was reduced from " + CONFIG.itemSize + "px to " + size + "px so the longest line fits.");
        var cardW = TEXT_LEFT + widest + L.cardPadRight;
        if (cardW > maxCardW + 0.5) warn("The card is wider than the safe margins. Shorten the longest line.");
        param(fx(layout, "Card Width"), "ADBE Slider Control-0001", "Slider").setValue(cardW);

        // ---- heading -----------------------------------------------------
        var heading = addText(comp, "Heading", CONFIG.heading.join("\r"), CONFIG.fonts.heading, CONFIG.headingSize,
                              ParagraphJustification.CENTER_JUSTIFY, CONFIG.headingLeading, C.heading);
        var hb = bounds(heading);
        transform(heading, "ADBE Position").setValue([W / 2, M - hb.top]);
        linkTextColor(heading, "Heading");
        var headingBottom = M + hb.height;
        if (hb.width > safeW) warn("The heading is wider than the safe margins. Shorten a line or lower CONFIG.headingSize.");

        // ---- logo --------------------------------------------------------
        var logo = null, logoTop = H - M;
        var logoFile = new File(CONFIG.logo.path);
        if (CONFIG.logo.path && logoFile.exists) {
            var foot = findFootage(logoFile);
            if (!foot) {
                foot = app.project.importFile(new ImportOptions(logoFile));
                foot.parentFolder = folder;
            }
            logo = comp.layers.add(foot);
            logo.name = "Truvio Logo";
            var s = CONFIG.logo.width / foot.width * 100;
            var logoH = foot.height * s / 100;
            transform(logo, "ADBE Scale").setValue([s, s, 100]);
            transform(logo, "ADBE Position").setValue([W / 2, H - M - logoH / 2]);
            logoTop = H - M - logoH;
        } else if (CONFIG.logo.path) {
            warn("Logo not found at " + CONFIG.logo.path + ". Skipped it; fix CONFIG.logo.path and re-run.");
        }

        // ---- vertical layout: centre the card between heading and logo ----
        var cardH = N * L.rowPitch + 2 * L.cardPadV;
        var cardTop = headingBottom + (logoTop - headingBottom - cardH) / 2;
        var cardCY = cardTop + cardH / 2;
        if ((logoTop - headingBottom - cardH * SCALE) / 2 < 32) warn("Vertical fit is tight. Lower CONFIG.checklistScale, CONFIG.layout.rowPitch or CONFIG.headingSize.");

        // ---- CHECKLIST: scales the card and rows around the card's centre --
        // Anchor = position, so children keep comp coordinates at 100% and every
        // layout expression below works unchanged.
        var checklist = comp.layers.addNull(duration);
        checklist.name = CHECKLIST;
        checklist.guideLayer = true;
        transform(checklist, "ADBE Anchor Point").setValue([W / 2, cardCY]);
        transform(checklist, "ADBE Position").setValue([W / 2, cardCY]);
        var cardLeft = W / 2 - cardW / 2;
        var capH = capRatio * size;

        // ---- card shadow + card -----------------------------------------
        var shadow = addShapeLayer(comp, "Card Shadow");
        addGroup(shadow, "Card");
        addRect(shadow, "Card", [cardW, cardH], [W / 2, cardCY + L.shadowOffset], L.cardRadius);
        addFill(shadow, "Card");
        item(shadow, "Card", "Rect").property("ADBE Vector Rect Size").expression = "[" + cardWidth() + ", " + cardH + "];";
        item(shadow, "Card", "Fill").property("ADBE Vector Fill Color").expression = ctrl("Card Shadow");
        addEffect(shadow, "ADBE Gaussian Blur 2", "Blur");
        param(fx(shadow, "Blur"), "ADBE Gaussian Blur 2-0001", "Blurriness").setValue(L.shadowBlur);
        transform(shadow, "ADBE Opacity").expression = ctrl("Card Shadow Opacity");

        var card = addShapeLayer(comp, "Card");
        addGroup(card, "Card");
        addRect(card, "Card", [cardW, cardH], [W / 2, cardCY], L.cardRadius);
        addStroke(card, "Card", "Border", L.cardBorder, false);
        addFill(card, "Card");
        item(card, "Card", "Rect").property("ADBE Vector Rect Size").expression = "[" + cardWidth() + ", " + cardH + "];";
        item(card, "Card", "Border").property("ADBE Vector Stroke Color").expression = ctrl("Card Border");
        item(card, "Card", "Fill").property("ADBE Vector Fill Color").expression = ctrl("Card Fill");

        // ---- dividers: from the text column to the card's right edge ------
        var dividers = addShapeLayer(comp, "Dividers");
        var divInset = TEXT_LEFT + L.cardBorder / 2;
        for (i = 0; i < N - 1; i++) {
            var g = "Divider " + (i + 1);
            var y = cardTop + L.cardPadV + L.rowPitch * (i + 1);
            var len = cardW - divInset;
            addGroup(dividers, g);
            addRect(dividers, g, [len, L.dividerHeight], [cardLeft + TEXT_LEFT + len / 2, y], 0);
            addFill(dividers, g);
            item(dividers, g, "Fill").property("ADBE Vector Fill Color").expression = ctrl("Divider");
            item(dividers, g, "Rect").property("ADBE Vector Rect Size").expression =
                "var w = " + cardWidth() + ";\n[w - " + divInset + ", " + L.dividerHeight + "];";
            item(dividers, g, "Rect").property("ADBE Vector Rect Position").expression =
                "var w = " + cardWidth() + ";\nvar len = w - " + divInset + ";\n" +
                "[thisComp.width / 2 - w / 2 + " + TEXT_LEFT + " + len / 2, value[1]];";
        }

        // ---- rows: position text + emoji, build animated checkboxes -------
        var boxes = [];
        for (i = 0; i < N; i++) {
            var rowCY = cardTop + L.cardPadV + L.rowPitch * (i + 0.5);
            var baseline = rowCY + capH / 2;

            var tPos = transform(rows[i].text, "ADBE Position");
            tPos.setValue([cardLeft + TEXT_LEFT, baseline]);
            tPos.expression = xFromCardLeft(TEXT_LEFT);
            linkTextColor(rows[i].text, "Item Text");

            if (rows[i].emoji) {
                var tb = bounds(rows[i].text), eb = bounds(rows[i].emoji);
                var ePos = transform(rows[i].emoji, "ADBE Position");
                ePos.setValue([cardLeft + TEXT_LEFT + tb.left + tb.width + L.emojiGap - eb.left, baseline]);
                ePos.expression =
                    'var t = thisComp.layer("' + rows[i].text.name + '");\n' +
                    "var r = t.sourceRectAtTime(time, false);\n" +
                    "var me = thisLayer.sourceRectAtTime(time, false);\n" +
                    "[t.transform.position[0] + r.left + r.width + " + L.emojiGap + " - me.left, t.transform.position[1]];";
            }

            boxes.push(buildCheckbox(comp, i, cardLeft + L.cardPadLeft + L.boxSize / 2, rowCY, checkT[i], uncheckT[i]));
        }

        // ---- parent the card and rows to CHECKLIST (still at 100%, so nothing moves)
        var cardLayers = [shadow, card, dividers];
        for (i = 0; i < N; i++) {
            cardLayers.push(rows[i].text, boxes[i]);
            if (rows[i].emoji) cardLayers.push(rows[i].emoji);
        }
        for (i = 0; i < cardLayers.length; i++) setParent(cardLayers[i], checklist);
        transform(checklist, "ADBE Scale").expression = "var s = " + ctrl(SCALE_CTRL) + ";\n[s, s];";
        // Shape layers apply effects after transforms, so scale the shadow blur by hand
        param(fx(shadow, "Blur"), "ADBE Gaussian Blur 2-0001", "Blurriness").expression =
            'value * thisComp.layer("' + CHECKLIST + '").transform.scale[0] / 100;';

        // ---- card width follows the longest line from now on --------------
        var rowList = [];
        for (i = 0; i < N; i++) {
            rowList.push('["' + rows[i].text.name + '", "' + (rows[i].emoji ? rows[i].emoji.name : "") + '"]');
        }
        param(fx(layout, "Card Width"), "ADBE Slider Control-0001", "Slider").expression = [
            "// Auto: widest row + padding. Don't edit; change the text layers instead.",
            "var rows = [" + rowList.join(", ") + "];",
            "var m = 0;",
            "for (var i = 0; i < rows.length; i++) {",
            "    var t = thisComp.layer(rows[i][0]).sourceRectAtTime(time, false);",
            "    var w = t.left + t.width;",
            "    if (rows[i][1] !== \"\") {",
            "        var e = thisComp.layer(rows[i][1]).sourceRectAtTime(time, false);",
            "        if (e.width > 0) w += " + L.emojiGap + " + e.width;",
            "    }",
            "    if (w > m) m = w;",
            "}",
            TEXT_LEFT + " + m + " + L.cardPadRight + ";"
        ].join("\n");

        // ---- background: brand-angle gradient -----------------------------
        var bg = comp.layers.addSolid([1, 1, 1], "Background", W, H, 1, duration);
        addEffect(bg, "ADBE Ramp", "Gradient");
        var ramp = fx(bg, "Gradient");
        var rampEnd = function (sign) {
            return [
                "var a = degreesToRadians(" + ctrl("BG Angle") + ");",
                "var dx = Math.cos(a), dy = -Math.sin(a);",
                "var r = (Math.abs(dx) * thisComp.width + Math.abs(dy) * thisComp.height) / 2;",
                "[thisComp.width / 2 " + sign + " dx * r, thisComp.height / 2 " + sign + " dy * r];"
            ].join("\n");
        };
        param(ramp, "ADBE Ramp-0005", "Ramp Shape").setValue(1);        // linear
        param(ramp, "ADBE Ramp-0006", "Ramp Scatter").setValue(10);     // light dither, stops banding
        param(ramp, "ADBE Ramp-0001", "Start of Ramp").expression = rampEnd("-");
        param(ramp, "ADBE Ramp-0002", "Start Color").expression = ctrl("BG Start Color");
        param(ramp, "ADBE Ramp-0003", "End of Ramp").expression = rampEnd("+");
        param(ramp, "ADBE Ramp-0004", "End Color").expression = ctrl("BG End Color");

        // ---- stacking order, top to bottom --------------------------------
        var order = [controls, layout, checklist];
        if (logo) order.push(logo);
        order.push(heading);
        for (i = 0; i < N; i++) {
            if (rows[i].emoji) order.push(rows[i].emoji);
            order.push(rows[i].text);
            order.push(boxes[i]);
        }
        order.push(dividers, card, shadow, bg);
        for (i = order.length - 1; i >= 0; i--) order[i].moveToBeginning();

        // ---- comp markers for retiming ------------------------------------
        for (i = 0; i < N; i++) marker(comp, checkT[i], "Check " + (i + 1));
        marker(comp, uncheckStart, "Reset");
        marker(comp, duration - 1 / CONFIG.fps, "Loop point");

        // ---- Essential Graphics: expose every control ---------------------
        var egpOk = true;
        try { comp.motionGraphicsTemplateName = CONFIG.compName; } catch (e3) {}
        for (i = 0; i < CONTROL_SPEC.length; i++) {
            try {
                var p = fx(controls, CONTROL_SPEC[i][0]).property(1);
                if (p.canAddToMotionGraphicsTemplate(comp)) p.addToMotionGraphicsTemplateAs(comp, CONTROL_SPEC[i][3]);
            } catch (e4) { egpOk = false; }
        }
        try {
            var sp = fx(controls, SCALE_CTRL).property(1);
            if (sp.canAddToMotionGraphicsTemplate(comp)) sp.addToMotionGraphicsTemplateAs(comp, "Checklist scale (%)");
        } catch (e5) { egpOk = false; }
        if (!egpOk) warn("Couldn't add every control to Essential Graphics. The CONTROLS layer still works.");

        // ---- verify expressions, tidy up ----------------------------------
        var exprErrors = [];
        for (i = 1; i <= comp.numLayers; i++) checkExpressions(comp.layer(i), comp.layer(i).name, exprErrors);
        for (i = 0; i < exprErrors.length; i++) warn("Expression error: " + exprErrors[i]);

        comp.openInViewer();
        comp.time = checkT[N - 1] + CHECK_DUR + 0.5;   // park on the all-checked frame
        for (i = 1; i <= comp.numLayers; i++) comp.layer(i).selected = false;
        controls.selected = true;
        layout.locked = true;   // last: a locked layer can't be changed
        checklist.locked = true;

        return { comp: comp, duration: duration, size: size };
    }

    // Checkbox layer: "Tick" group above a "Box" group, all colours from CONTROLS
    function buildCheckbox(comp, i, x, y, tCheck, tUncheck) {
        var b = L.boxSize;
        var layer = addShapeLayer(comp, "Item " + (i + 1) + " Checkbox", [x, y]);
        transform(layer, "ADBE Position").expression = xFromCardLeft(L.cardPadLeft + L.boxSize / 2);

        addGroup(layer, "Tick");   // added first so it renders on top
        addPath(layer, "Tick", [[-0.21 * b, 0.01 * b], [-0.07 * b, 0.15 * b], [0.22 * b, -0.15 * b]]);
        addTrim(layer, "Tick");
        addStroke(layer, "Tick", "Stroke", L.tickStroke, true);

        addGroup(layer, "Box");
        addRect(layer, "Box", [b, b], [0, 0], L.boxRadius);
        addStroke(layer, "Box", "Outline", L.boxStroke, false);
        addFill(layer, "Box");

        item(layer, "Tick", "Stroke").property("ADBE Vector Stroke Color").expression = ctrl("Checkmark");
        item(layer, "Tick", "Stroke").property("ADBE Vector Stroke Opacity").expression =
            'content("Tick").content("Trim").end > 0 ? 100 : 0;';
        item(layer, "Box", "Fill").property("ADBE Vector Fill Color").expression = ctrl("Checkbox Checked");
        // Outline shifts to the checked colour as the box fills
        item(layer, "Box", "Outline").property("ADBE Vector Stroke Color").expression =
            'linear(content("Box").content("Fill").opacity, 0, 50, ' + ctrl("Checkbox Outline") + ", " + ctrl("Checkbox Checked") + ");";

        // Click: light "press" fill, then solid, then the tick draws (short leg, long leg)
        var fill = item(layer, "Box", "Fill").property("ADBE Vector Fill Opacity");
        animate(fill, [
            [tCheck, 0], [tCheck + 0.10, 40], [tCheck + 0.20, 100],
            [tUncheck + 0.04, 100], [tUncheck + UNCHECK_DUR, 0]
        ]);
        var trimEnd = item(layer, "Tick", "Trim").property("ADBE Vector Trim End");
        animate(trimEnd, [
            [tCheck + 0.16, 0, 66, 30], [tCheck + CHECK_DUR, 100, 85, 66],
            [tUncheck, 100], [tUncheck + 0.14, 0]
        ]);
        animate(transform(layer, "ADBE Scale"), [
            [tCheck, [100, 100, 100]], [tCheck + 0.08, [94, 94, 100]], [tCheck + 0.22, [100, 100, 100]]
        ]);
        return layer;
    }

    // =====================================================================
    //  Run
    // =====================================================================
    // Saves an unsaved project next to this script. Never overwrites a file,
    // never re-saves a project that already has one.
    function saveProject() {
        if (app.project.file) {
            warn("This project already has a file, so the script didn't save it. Use File > Save.");
            return null;
        }
        var script = new File($.fileName);
        var folder = ($.fileName && script.parent && script.parent.exists) ? script.parent : Folder.desktop;
        var f = new File(folder.fsName + "/" + CONFIG.compName + ".aep"), n = 2;
        while (f.exists) f = new File(folder.fsName + "/" + CONFIG.compName + " " + (n++) + ".aep");
        try {
            app.project.save(f);
            return f;
        } catch (e) {
            warn("Couldn't save the .aep (" + e.toString() + "). Use File > Save As.");
            return null;
        }
    }

    var result = null;
    app.beginUndoGroup("Build Truvio Checklist");
    try {
        result = build();
    } catch (err) {
        alert("Truvio Checklist build stopped:\n" + err.toString() + (err.line ? "\n(script line " + err.line + ")" : ""));
    }
    app.endUndoGroup();
    if (!result) return;

    var saved = CONFIG.saveAep ? saveProject() : null;
    var msg = "Truvio Checklist is built.\n\n" +
              "Comp: " + result.comp.name + " (" + W + "x" + H + ", " + CONFIG.fps + "fps, " +
              (Math.round(result.duration * 100) / 100) + "s, loops seamlessly)\n" +
              "Checklist at " + CONFIG.checklistScale + "%: change it with CONTROLS > " + SCALE_CTRL + ".\n\n" +
              "Colours: select the CONTROLS layer and open Effect Controls.\n" +
              "They're also in the Essential Graphics panel.";
    if (saved) msg += "\n\nSaved: " + saved.fsName;
    if (warnings.length) msg += "\n\nCheck these:\n- " + warnings.join("\n- ");
    alert(msg);

})();
