// Builds the Notes screen inside every .screen element. Icon colours are written as literal hex,
// so the SVG export keeps them. The note copy is final. Change it only from the brief.
(function () {
  const Y = getComputedStyle(document.documentElement).getPropertyValue('--notes').trim() || '#E3A600';
  const K = '#000000';
  const icon = (x, y, w, h, vb, body) =>
    `<svg style="left:${x}px;top:${y}px" width="${w}" height="${h}" viewBox="${vb}">${body}</svg>`;
  const st = (c, w) => `fill="none" stroke="${c}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"`;

  // Status bar: signal, wifi, battery at about half charge.
  const sys =
    icon(0, 1, 19, 12, '0 0 19 12',
      `<g fill="${K}"><rect x="0" y="8" width="3.4" height="4" rx="1"/><rect x="5" y="5.5" width="3.4" height="6.5" rx="1"/>` +
      `<rect x="10" y="3" width="3.4" height="9" rx="1"/><rect x="15" y="0" width="3.4" height="12" rx="1"/></g>`) +
    icon(25, 0, 18, 13, '0 0 18 13',
      `<path d="M1.6 4.6a10.6 10.6 0 0 1 14.8 0M4.5 7.6a6.4 6.4 0 0 1 9 0" ${st(K, 2.1)}/><circle cx="9" cy="11" r="1.7" fill="${K}"/>`) +
    icon(49, 0, 27, 13, '0 0 27 13',
      `<rect x=".6" y=".6" width="23" height="11.8" rx="3.4" fill="none" stroke="${K}" stroke-opacity=".4" stroke-width="1.2"/>` +
      `<rect x="2.6" y="2.6" width="11" height="7.8" rx="1.6" fill="${K}"/><rect x="25" y="4.3" width="1.8" height="4.4" rx=".9" fill="${K}" fill-opacity=".45"/>`);

  // Nav bar: back chevron on the left, share and more on the right. Icons only, no labels.
  const nav =
    icon(18, 10, 15, 26, '0 0 15 26', `<path d="M12.5 2 2.5 13l10 11" ${st(Y, 3.2)}/>`) +
    icon(236, 6, 24, 31, '0 0 24 31', `<path d="M7 12H3.5v16.5h17V12H17M12 2.5v16M7.3 7 12 2.5 16.7 7" ${st(Y, 2.4)}/>`) +
    icon(278, 8, 28, 28, '0 0 28 28',
      `<circle cx="14" cy="14" r="12.3" ${st(Y, 2.2)}/><g fill="${Y}"><circle cx="8.3" cy="14" r="1.9"/><circle cx="14" cy="14" r="1.9"/><circle cx="19.7" cy="14" r="1.9"/></g>`);

  // Bottom toolbar: checklist, camera, markup, compose.
  const tb =
    icon(30, 3, 28, 26, '0 0 28 26', `<path d="M2.5 6.5 5.5 9.5 11 3.5M2.5 18.5l3 3 5.5-6M15.5 7h10M15.5 19h10" ${st(Y, 2.4)}/>`) +
    icon(110, 3, 32, 26, '0 0 32 26', `<path d="M4.5 7h5l2.3-3.5h8.4L22.5 7h5a2.5 2.5 0 0 1 2.5 2.5V21a2.5 2.5 0 0 1-2.5 2.5h-23A2.5 2.5 0 0 1 2 21V9.5A2.5 2.5 0 0 1 4.5 7Z" ${st(Y, 2.2)}/><circle cx="16" cy="15" r="5" ${st(Y, 2.2)}/>`) +
    icon(190, 1, 30, 30, '0 0 30 30', `<circle cx="15" cy="15" r="13" ${st(Y, 2.2)}/><path d="M10.5 22 15 8.5 19.5 22M12.2 17h5.6" ${st(Y, 2.2)}/>`) +
    icon(270, 1, 30, 30, '0 0 30 30', `<path d="M14 4.5H6.5A3 3 0 0 0 3.5 7.5v16a3 3 0 0 0 3 3h16a3 3 0 0 0 3-3V16M23.5 3.2l3.3 3.3-11 11-4.4 1.1 1.1-4.4Z" ${st(Y, 2.2)}/>`);

  // The note. Copy from the brief, unchanged.
  const title = 'Things we crammed into our BC item cards';
  // Non-breaking spaces only steer the wraps ("nobody updates" stays together). The words are the brief's.
  const items = ['47 custom fields', 'Marketing texts in 6\u00a0languages', 'Image links nobody\u00a0updates', 'Spec sheets as\u00a0attachments'];
  const note = `<div class="title" data-layer="Note_title">${title}</div>` +
    items.map((t, i) => `<div class="li" data-layer="Note_item_${i + 1}"><span class="dot">•</span><span class="tx">${t}</span></div>`).join('');

  for (const s of document.querySelectorAll('.screen')) {
    s.innerHTML =
      `<div class="sb" data-layer="Status_bar"><span class="time">23:47</span><i class="island" data-layer="Camera_island"></i><span class="sys">${sys}</span></div>` +
      `<div class="nav" data-layer="Nav_bar">${nav}</div>` +
      `<div class="note" data-layer="Note">${note}</div>` +
      `<div class="tb" data-layer="Toolbar">${tb}</div>` +
      `<i class="home" data-layer="Home_indicator"></i>`;
  }
})();
