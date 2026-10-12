// Walks a rendered mock and writes an Illustrator-friendly SVG into <pre id="svgout">.
// export_svg.py injects this into a copy of the mock. Runs after the page's own fonts.ready work.
// Groups: an element with data-layer="Name" becomes <g id="Name">. A few UI classes get numbered groups.
// Text stays live and names fonts by PostScript name, the way Illustrator writes its own SVG.
(function () {
  const PS = {'Slab|700': 'MuseoSlab-700', 'BVP|400': 'BeVietnamPro-Regular', 'BVP|800': 'BeVietnamPro-ExtraBold'};
  const AUTO = ['bar', 'red', 'f', 'st', 'row', 'hero', 'thumb', 'scroll', 'waffle', 'clean', 'tab'];
  const f = n => +(+n).toFixed(2);
  const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const defs = [], used = {};
  const uniq = name => { used[name] = (used[name] || 0) + 1; return used[name] === 1 ? name : `${name}_${used[name]}`; };
  let defId = 0; const nextId = p => `${p}${++defId}`;
  const ctx = document.createElement('canvas').getContext('2d');

  function color(c) {
    const m = c && c.match(/rgba?\(([^)]+)\)/); if (!m) return null;
    const p = m[1].split(',').map(parseFloat), a = p.length > 3 ? p[3] : 1;
    if (a === 0) return null;
    return {hex: '#' + p.slice(0, 3).map(v => Math.round(v).toString(16).padStart(2, '0')).join('').toUpperCase(), a};
  }
  const paint = (c, attr = 'fill') => `${attr}="${c.hex}"` + (c.a < 1 ? ` ${attr}-opacity="${f(c.a)}"` : '');

  function gradient(bi, x, y, w, h) {
    const m = bi.match(/linear-gradient\((.*)\)$/); if (!m) return null;
    const parts = m[1].split(/,(?![^(]*\))/).map(s => s.trim());
    let ang = 180; if (/deg$/.test(parts[0])) ang = parseFloat(parts.shift());
    const stops = parts.map((p, i) => { const c = color(p); const pos = p.match(/([\d.]+)%\s*$/);
      return {c, pos: pos ? +pos[1] / 100 : (i === 0 ? 0 : i === parts.length - 1 ? 1 : null)}; });
    stops.forEach((s, i) => { if (s.pos === null) s.pos = (stops[i - 1].pos + 1) / 2; });
    const a = ang * Math.PI / 180, L = Math.abs(w * Math.sin(a)) + Math.abs(h * Math.cos(a));
    const cx = x + w / 2, cy = y + h / 2, dx = Math.sin(a) * L / 2, dy = -Math.cos(a) * L / 2;
    const id = nextId('grad');
    defs.push(`<linearGradient id="${id}" gradientUnits="userSpaceOnUse" x1="${f(cx - dx)}" y1="${f(cy - dy)}" x2="${f(cx + dx)}" y2="${f(cy + dy)}">` +
      stops.map(s => `<stop offset="${f(s.pos)}" stop-color="${s.c.hex}"${s.c.a < 1 ? ` stop-opacity="${f(s.c.a)}"` : ''}/>`).join('') + `</linearGradient>`);
    return id;
  }

  // CSS shadows to an SVG filter that draws the shadows only. Blur radius b becomes stdDeviation b/2.
  // A spread ring is drawn as a stroke instead. The filter sits on its own shape under the content,
  // so print and Illustrator keep the content vector.
  function shadowFilter(list) {
    if (!list.length) return null;
    const id = nextId('shadow');
    const prims = list.map((s, i) => `<feGaussianBlur in="SourceAlpha" stdDeviation="${f(s.b / 2)}"/><feOffset dx="${s.dx}" dy="${s.dy}" result="o${i}"/>` +
      `<feFlood flood-color="${s.c.hex}" flood-opacity="${f(s.c.a)}"/><feComposite in2="o${i}" operator="in" result="s${i}"/>`).join('');
    defs.push(`<filter id="${id}" x="-30%" y="-30%" width="160%" height="160%" color-interpolation-filters="sRGB">${prims}` +
      `<feMerge>${list.map((_, i) => `<feMergeNode in="s${i}"/>`).join('')}</feMerge></filter>`);
    return id;
  }
  function parseShadows(str) {
    if (!str || str === 'none') return [];
    return (str.match(/(rgba?\([^)]+\)[^,]*(?:,(?![^(]*\))|$))/g) || []).map(p => {
      const c = color(p), n = p.replace(/rgba?\([^)]+\)/, '').match(/-?[\d.]+px/g).map(parseFloat);
      return {c, dx: n[0], dy: n[1], b: n[2] || 0, spread: n[3] || 0};
    });
  }

  function box(el, cs, x, y, w, h) {
    let s = '';
    const r = parseFloat(cs.borderTopLeftRadius) || 0, rx = r ? ` rx="${f(Math.min(r, w / 2, h / 2))}"` : '';
    const bg = color(cs.backgroundColor), gi = cs.backgroundImage !== 'none' ? gradient(cs.backgroundImage, x, y, w, h) : null;
    if (bg) s += `<rect x="${f(x)}" y="${f(y)}" width="${f(w)}" height="${f(h)}"${rx} ${paint(bg)}/>`;
    if (gi) s += `<rect x="${f(x)}" y="${f(y)}" width="${f(w)}" height="${f(h)}"${rx} fill="url(#${gi})"/>`;
    const bw = ['Top', 'Right', 'Bottom', 'Left'].map(k => cs[`border${k}Style`] !== 'none' ? parseFloat(cs[`border${k}Width`]) : 0);
    const bc = color(cs.borderTopColor) || color(cs.borderBottomColor);
    if (bw.every(v => v > 0 && v === bw[0]) && bc) {
      const b = bw[0];
      s += `<rect x="${f(x + b / 2)}" y="${f(y + b / 2)}" width="${f(w - b)}" height="${f(h - b)}"${r ? ` rx="${f(Math.max(r - b / 2, 0))}"` : ''} fill="none" ${paint(bc, 'stroke')} stroke-width="${b}"/>`;
    } else if (bw[2] > 0) {
      const c = color(cs.borderBottomColor);
      if (c) s += `<rect x="${f(x)}" y="${f(y + h - bw[2])}" width="${f(w)}" height="${bw[2]}" ${paint(c)}/>`;
    }
    for (const sh of parseShadows(cs.boxShadow).filter(sh => sh.spread && !sh.b))
      s = `<rect x="${f(x - sh.spread / 2)}" y="${f(y - sh.spread / 2)}" width="${f(w + sh.spread)}" height="${f(h + sh.spread)}"${r ? ` rx="${f(r + sh.spread / 2)}"` : ''} fill="none" ${paint(sh.c, 'stroke')} stroke-width="${sh.spread}"/>` + s;
    return s;
  }

  function pseudo(el, which, r, cs) {
    const p = getComputedStyle(el, which);
    if (p.content === 'none' || p.display === 'none') return '';
    const bl = parseFloat(cs.borderLeftWidth), bt = parseFloat(cs.borderTopWidth);
    const w = parseFloat(p.width), h = parseFloat(p.height);
    const x = p.left !== 'auto' ? r.left + bl + parseFloat(p.left) : r.right - parseFloat(cs.borderRightWidth) - parseFloat(p.right) - w;
    const y = p.top !== 'auto' ? r.top + bt + parseFloat(p.top) : r.bottom - parseFloat(cs.borderBottomWidth) - parseFloat(p.bottom) - h;
    return box(el, p, x - B.left, y - B.top, w, h);
  }

  function texts(el, cs) {
    let s = '';
    const fam = cs.fontFamily.split(',')[0].replace(/['"]/g, '').trim(), wt = cs.fontWeight;
    const ps = PS[`${fam}|${wt}`] || fam, c = color(cs.color);
    ctx.font = `${wt} ${cs.fontSize} ${cs.fontFamily}`;
    const asc = ctx.measureText('Hg').fontBoundingBoxAscent;
    const ls = cs.letterSpacing === 'normal' ? 0 : parseFloat(cs.letterSpacing);
    const range = document.createRange();
    for (const n of el.childNodes) {
      if (n.nodeType !== 3 || !n.textContent.trim()) continue;
      const t = n.textContent, lines = []; let cur = null;
      for (let i = 0; i < t.length; i++) {
        if (!t[i].trim()) { if (cur && !cur.s.endsWith(' ')) cur.s += ' '; continue; }
        range.setStart(n, i); range.setEnd(n, i + 1);
        const rc = range.getClientRects()[0]; if (!rc) continue;
        if (!cur || Math.abs(rc.top - cur.top) > 2) { cur = {top: rc.top, left: rc.left, s: ''}; lines.push(cur); }
        cur.s += t[i];
      }
      for (const L of lines) s += `<text x="${f(L.left - B.left)}" y="${f(L.top - B.top + asc)}" font-family="'${ps}'" font-size="${parseFloat(cs.fontSize)}"` +
        `${ls ? ` letter-spacing="${f(ls)}"` : ''} ${paint(c)}>${esc(L.s.trim())}</text>`;
    }
    return s;
  }

  function inlineSvg(el, r) {
    const vb = (el.getAttribute('viewBox') || `0 0 ${r.width} ${r.height}`).split(/[\s,]+/).map(parseFloat);
    const sx = r.width / vb[2], sy = r.height / vb[3];
    return `<g transform="translate(${f(r.left - B.left - vb[0] * sx)} ${f(r.top - B.top - vb[1] * sy)}) scale(${f(sx)} ${f(sy)})">${el.innerHTML}</g>`;
  }

  function walk(el) {
    if (['SCRIPT', 'STYLE', 'PRE'].includes(el.tagName)) return '';
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') return '';
    const r = el.getBoundingClientRect(), x = r.left - B.left, y = r.top - B.top;
    if (el.tagName.toLowerCase() === 'svg') return inlineSvg(el, r);
    if (el.tagName === 'IMG')
      return `<g id="${uniq(el.dataset.layer || 'Image')}" data-img="${el.getAttribute('src')}" data-box="${f(x)} ${f(y)} ${f(r.width)} ${f(r.height)}"></g>`;
    let s = box(el, cs, x, y, r.width, r.height) + pseudo(el, '::before', r, cs) + texts(el, cs);
    for (const ch of el.children) s += walk(ch);
    s += pseudo(el, '::after', r, cs);
    if (cs.overflow === 'hidden' && el !== board) {
      const id = nextId('clip'), rad = parseFloat(cs.borderTopLeftRadius) || 0;
      defs.push(`<clipPath id="${id}"><rect x="${f(x)}" y="${f(y)}" width="${f(r.width)}" height="${f(r.height)}"${rad ? ` rx="${rad}"` : ''}/></clipPath>`);
      s = `<g clip-path="url(#${id})">${s}</g>`;
    }
    const shadows = [...parseShadows(cs.boxShadow).filter(sh => sh.b),
                     ...(cs.filter.match(/drop-shadow\([^)]*\)[^)]*\)/g) || []).map(d => parseShadows(d.slice(12, -1))[0])];
    const fid = shadowFilter(shadows.filter(Boolean));
    const auto = AUTO.find(c => el.classList.contains(c));
    const name = el.dataset.layer || (auto && auto[0].toUpperCase() + auto.slice(1));
    if (fid) {
      const rad = parseFloat(cs.borderTopLeftRadius) || 0;
      s = `<g id="${uniq((name || 'Shape') + '_shadow')}" filter="url(#${fid})"><rect x="${f(x)}" y="${f(y)}" width="${f(r.width)}" height="${f(r.height)}"` +
        `${rad ? ` rx="${rad}"` : ''} fill="#000000"/></g>` + s;
    }
    if (name) s = `<g id="${uniq(name)}">${s}</g>`;
    return s;
  }

  const board = document.getElementById('board'), B = board.getBoundingClientRect();
  const body = walk(board);
  const W = Math.round(B.width), H = Math.round(B.height);
  document.getElementById('svgout').textContent =
    `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">` +
    `<defs>${defs.join('')}</defs>${body}</svg>`;
})();
