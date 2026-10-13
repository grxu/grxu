const { chromium } = require('playwright-core');
const fs=require('fs');
const [,,json,bg,outdir,framesArg,cfgJson]=process.argv;
const c=Object.assign({left:294.5,width:510,top:355,clipTop:500,clipBottom:1080},JSON.parse(cfgJson||'{}'));
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell'});
 const d=JSON.parse(fs.readFileSync(json));
 const s=c.width/d.w;
 const p=await b.newPage({viewport:{width:1080,height:1080}});
 const bgData='data:image/png;base64,'+fs.readFileSync(bg).toString('base64');
 await p.setContent(`<html><body style="margin:0;width:1080px;height:1080px;overflow:hidden;background:url(${bgData}) 0 0/1080px 1080px no-repeat">
 <div style="position:absolute;left:${c.left}px;top:${c.clipTop}px;width:${c.width}px;height:${c.clipBottom-c.clipTop}px;overflow:hidden">
 <div id=a style="position:absolute;left:0;top:${c.top-c.clipTop}px;width:${d.w}px;height:${d.h}px;transform:scale(${s});transform-origin:0 0"></div></div></body></html>`);
 await p.addScriptTag({path:require.resolve('lottie-web/build/player/lottie.min.js')});
 await p.evaluate(d=>{window.anim=lottie.loadAnimation({container:document.getElementById('a'),renderer:'svg',loop:false,autoplay:false,animationData:d});},d);
 await p.waitForTimeout(500);
 const frames=framesArg==='all'?[...Array(Math.floor(d.op)).keys()]:framesArg.split(',').map(Number);
 fs.mkdirSync(outdir,{recursive:true});
 for(const f of frames){await p.evaluate(f=>anim.goToAndStop(f,true),f);
  await p.screenshot({path:`${outdir}/f${String(f).padStart(4,'0')}.png`});}
 await b.close();
})();
