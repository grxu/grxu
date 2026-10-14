// Renders inside-bc-chat.html frame by frame to PNGs.
// Usage: node render.js <outdir> <fps> [frame,frame,...]
// Needs playwright-core and a Chromium headless shell (set CHROME_PATH).
const { chromium } = require("playwright-core");
const fs = require("fs");
const path = require("path");

const [, , outdir, fpsArg, only] = process.argv;
const fps = Number(fpsArg || 30);
(async () => {
  const browser = await chromium.launch({ executablePath: process.env.CHROME_PATH, args: ["--allow-file-access-from-files"] });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1080 } });
  await page.goto("file://" + path.join(__dirname, "inside-bc-chat.html") + "?render");
  await page.evaluate(() => window.ready);
  const duration = await page.evaluate(() => window.DURATION);
  const frames = only ? only.split(",").map(Number) : [...Array(Math.round(duration * fps)).keys()];
  fs.mkdirSync(outdir, { recursive: true });
  for (const f of frames) {
    await page.evaluate(t => window.renderAt(t), f / fps);
    await page.screenshot({ path: path.join(outdir, `f${String(f).padStart(4, "0")}.png`) });
  }
  await browser.close();
})();
