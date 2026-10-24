// Renders the storyboard key frames and the animatic from film.html.
// Usage: node render.js frames <outDir> 0.6 1.8 ...   (one PNG per time, 1080x1350)
//        node render.js video <outDir> [fps]          (PNG sequence for ffmpeg)
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const [mode, out, ...rest] = process.argv.slice(2);
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  await page.goto('file://' + path.join(__dirname, 'film.html') + '?t=0');
  await page.waitForFunction(() => window.filmReady === true);
  const shoot = async (t, file) => {
    await page.evaluate(t => window.render(t), t);
    await page.screenshot({ path: path.join(out, file) });
  };
  if (mode === 'frames') {
    for (const t of rest.map(Number)) await shoot(t, `frame-${t.toFixed(1).padStart(4, '0')}s.png`);
  } else {
    const fps = Number(rest[0] || 25), dur = await page.evaluate(() => window.DUR);
    const n = Math.round(dur * fps);
    for (let i = 0; i <= n; i++) await shoot(i / fps, `f${String(i).padStart(4, '0')}.png`);
  }
  await browser.close();
})();
