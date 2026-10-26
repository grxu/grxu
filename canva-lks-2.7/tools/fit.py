import sys; sys.path.insert(0,".")
from engine import build_page,H,Page
from specs import SPECS
fake=dict(pid="P",pool=[],spares=[],boxes=[],refl={},dele=[])
for n in map(int,sys.argv[1:]):
    fs=11; ops,info=build_page(fake,SPECS[n],fs=fs); pg=Page("P",fake,fs)
    bh={}
    for s in SPECS[n]["secs"]:
        W=(638.11 if s.get("full") else 307.32)-17.75; ih=pg.nlines(s["instr"],W)*fs*1.2
        bh[s["n"]]=round(28.5+ih+7+H(pg,s["items"],W)+6)
    print(n,"over",info["over"],info["rowh"],bh,"refl",round(H(pg,SPECS[n]["refl"]["items"],449)+14))
