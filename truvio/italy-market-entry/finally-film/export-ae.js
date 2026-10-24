// Exports the animatic's geometry and motion for the After Effects build.
// Usage: node export-ae.js   (writes ae/ae-data.json, ae/road.svg and ae/car.svg)
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const out = path.join(__dirname, 'ae');
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  await page.goto('file://' + path.join(__dirname, 'film.html') + '?t=0');
  await page.waitForFunction(() => window.filmReady === true);
  const data = await page.evaluate(() => window.exportAE(25));
  const car = await page.evaluate(() => document.getElementById('car').innerHTML.trim());
  await browser.close();

  fs.writeFileSync(path.join(out, 'ae-data.json'), JSON.stringify(data));
  // The road centre line (the E's baseline) as one open path, for Illustrator or a copy-paste into an AE mask.
  const d = 'M' + data.roadPolyline.map(p => p.join(' ')).join(' L');
  fs.writeFileSync(path.join(out, 'road.svg'),
    `<svg xmlns="http://www.w3.org/2000/svg" width="4320" height="1350" viewBox="0 0 4320 1350">\n` +
    `  <path d="${d}" fill="none" stroke="#400685" stroke-width="3"/>\n</svg>\n`);
  // The car at 1x (74 x 34), origin on the ground line between the wheels. Scale it 260% in AE.
  fs.writeFileSync(path.join(out, 'car.svg'),
    `<svg xmlns="http://www.w3.org/2000/svg" width="80" height="40" viewBox="-38 -36 80 40">\n  ${car}\n</svg>\n`);
  console.log(`letters ${data.letterCount}, road ${data.roadLength}px, ${data.roadPolyline.length} path points, ${data.frames.length} frames`);
})();
