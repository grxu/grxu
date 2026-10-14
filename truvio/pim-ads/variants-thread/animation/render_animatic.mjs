// Render the animatic to MP4 and a storyboard of key moments.
// usage: node render_animatic.mjs [--frames-only t1,t2,...]
// Needs Playwright (Chromium) and ffmpeg. Writes variants-thread-animatic.mp4 and frames/ next to this file.
import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import { mkdirSync } from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const here = path.dirname(fileURLToPath(import.meta.url));
const exe = process.env.CHROME || undefined;
const browser = await chromium.launch({ executablePath: exe, args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1080, height: 1080 }, deviceScaleFactor: 1 });
await page.goto(pathToFileURL(path.join(here, 'animatic.html')).href);
await page.waitForSelector('body[data-ready]');
const { comp } = await page.evaluate(() => VT);

const only = process.argv.indexOf('--frames-only');
if (only > 0) {
  mkdirSync(path.join(here, 'frames'), { recursive: true });
  for (const t of process.argv[only + 1].split(',').map(Number)) {
    await page.evaluate(t => renderAt(t), t);
    await page.screenshot({ path: path.join(here, 'frames', `t${t.toFixed(2).padStart(5, '0')}.png`) });
  }
  await browser.close(); process.exit(0);
}

const out = path.join(here, 'variants-thread-animatic.mp4');
const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(comp.fps), '-i', '-',
  '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
const n = Math.round(comp.duration * comp.fps);
for (let f = 0; f < n; f++) {
  await page.evaluate(t => renderAt(t), f / comp.fps);
  const buf = await page.screenshot({ type: 'png' });
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
}
ff.stdin.end();
await new Promise(r => ff.on('close', r));
await page.evaluate(t => renderAt(t), comp.duration);
await page.screenshot({ path: path.join(here, 'last-frame.png') });
await browser.close();
console.log('wrote', out, n, 'frames');
