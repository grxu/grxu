import json
import sys
F=sys.argv[1]  # saved read-design JSON (design_content for pages 2..17, in order)
d=json.loads(open(F).read())
if isinstance(d,list): d=json.loads(d[0]["text"])
pages=d["design_content"]["pages"]
def txt(e): return "".join(r["characters"] for r in e.get("textRegions",[]))
def fmt(e): return e["textRegions"][0]["formatting"] if e.get("textRegions") else {}
def fill(e):
    p=e.get("paths") or []
    return (p[0].get("fill") or {}).get("color",{}).get("color") if p else None
def strk(e):
    p=e.get("paths") or []
    return (p[0].get("stroke") or {}).get("color",{}).get("color") if p else None
def analyze(pg):
    els=[]
    tg=None
    for e in pg["elements"]:
        if e["type"]=="group" and e.get("isLocked") and e["height"]>500:
            tg=e; els+= [dict(c,_loc=pg["id"]+"-"+e["id"]+"-"+c["id"]) for c in e["children"]]
        else: els.append(dict(e,_loc=pg["id"]+"-"+e["id"]))
    R={"pid":pg["id"],"boxes":[],"header":{},"refl":{},"pool":[],"dele":[],"spares":[]}
    used=set()
    st=[e for e in els if e["type"]=="shape" and fill(e)=="#d9f0fb" and e["width"]>600 and 900<e["top"]<1060]
    RT=min([e["top"] for e in st]+[984])-3
    content=[e for e in els if 170<e["top"]<RT]
    boxes=[e for e in content if e["type"]=="shape" and strk(e)=="#aae0fa" and e["height"]>80 and e["width"]>250 and fill(e) is None]
    pills=[e for e in content if e["type"]=="shape" and fill(e)=="#feefbc" and e["height"]<45]
    circs=[e for e in content if e["type"]=="shape" and fill(e)=="#f8c357" and e["height"]<55]
    texts=[e for e in content if e["type"]=="text"]
    for b in sorted(boxes,key=lambda e:(e["left"]>390,e["top"])):
        t,l=b["top"],b["left"]
        def near(lst,dt,dl,tol=8):
            c=[e for e in lst if abs(e["top"]-(t+dt))<tol and abs(e["left"]-(l+dl))<tol and e["id"] not in used]
            return c[0] if c else None
        pill=near(pills,-19.5,7.2); circ=near(circs,-24.9,-12.2)
        num=near([e for e in texts if txt(e).strip().isdigit()],-11.5,5.1)
        title=near([e for e in texts if fmt(e).get("fontSize",0)>15 and not txt(e).strip().isdigit()],-9.4,48)
        ins=near([e for e in texts if fmt(e).get("fontSize",99)<15],28.5,9,tol=10)
        bx=dict(box=b["_loc"],pill=pill and pill["_loc"],circ=circ and circ["_loc"],num=num and num["_loc"],title=title and title["_loc"],instr=ins and ins["_loc"],
                numtxt=num and txt(num),titletxt=title and txt(title),top=round(t),left=round(l),w=round(b["width"]),h=round(b["height"]))
        for x in (b,pill,circ,num,title,ins):
            if x: used.add(x["id"])
        R["boxes"].append(bx)
    for e in els:
        if e["id"] in used: continue
        if e["top"]<175 and e["top"]+e["height"]<180 or (e["type"]=="group" and e["top"]<175): continue
        if e is tg: continue
        if e["top"]>=RT:
            R["refl"].setdefault("els",[]).append(dict(loc=e["_loc"],type=e["type"],locked=e.get("isLocked"),top=round(e["top"],1),left=round(e["left"],1),w=round(e["width"],1),h=round(e["height"],1),txt=txt(e)[:70] if e["type"]=="text" else fill(e)))
            continue
        if e["top"]<30 and e["width"]>700: continue
        if e["type"]=="text" and txt(e).startswith("Text placeholder"): R["spares"].append(e["_loc"]); continue
        if e["type"]=="text" and fmt(e).get("fontRef")=="YAFcfjveRFU,0" and not e.get("isLocked"): R["pool"].append(e["_loc"]); continue
        R["dele"].append((e["_loc"],e["type"],e.get("isLocked")))
    return R
out={}
FIRST=int(sys.argv[2]) if len(sys.argv)>2 else 2  # page number of the first page in the file
for i,pg in enumerate(pages):
    R=analyze(pg); out[i+FIRST]=R
    nb=len(R["boxes"]); miss=[k for b in R["boxes"] for k in ("pill","circ","num","title","instr") if not b[k]]
    print(i+2,R["pid"],"boxes",nb,[ (b["numtxt"],b["top"],b["left"],b["h"]) for b in R["boxes"]],"miss",miss,"pool",len(R["pool"]),"spares",len(R["spares"]),"del",len(R["dele"]),"lockdel",sum(1 for x in R["dele"] if x[2]))
json.dump(out,open("roles.json","w"),indent=1)
