# python3 prep.py <read-design.json> <first_page> <pages...>: roles, safety scan, ops chunks
import json,sys,subprocess
sys.path.insert(0,".")
F,first=sys.argv[1],sys.argv[2]; pages=sys.argv[3:]
subprocess.run(["python3","roles.py",F,first],check=True,stdout=subprocess.DEVNULL)
from engine import build_page; from specs import SPECS
d=json.loads(open(F).read()); d=json.loads(d[0]["text"]) if isinstance(d,list) else d
print("txn",d.get("transaction"))
R=json.load(open("roles.json")); P={p["id"]:p for p in d["design_content"]["pages"]}
for n in pages:
    r=R[n]; els={}
    def walk(L):
        for e in L: els[e["id"]]=e; walk(e.get("children",[]))
    walk(P[r["pid"]]["elements"])
    print("PAGE",n,"boxes",[(b["numtxt"],b["top"]) for b in r["boxes"]],"bigGroups",[e["id"] for e in P[r["pid"]]["elements"] if e["type"]=="group" and e["height"]>500])
    print("  locked refl",[(e["type"],e["w"]) for e in r["refl"].get("els",[]) if e.get("locked")])
    for loc,t,lk in r["dele"]:
        e=els[loc.split("-")[-1]]
        if e["width"]>500 or e["top"]<180 or t=="rect" or lk: print("  CHECKDEL",loc,t,lk,round(e["top"]),round(e["width"]))
    dels=[x[0] for x in r["dele"]]+[b["box"] for b in r["boxes"] if not b["numtxt"]]
    ops,info=build_page(r,SPECS[int(n)],dels,fs=11); print(" ",info)
    ch=[[]]
    for o in ops:
        if len(json.dumps(ch[-1]+[o]))>28000: ch.append([])
        ch[-1].append(o)
    for i,c in enumerate(ch): json.dump(c,open(f"ops{n}_{i}.json","w"))
    print("  chunks",len(ch))
