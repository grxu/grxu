import json,sys
sys.path.insert(0,".")
from engine import build_page
from specs import SPECS
roles=json.load(open("roles.json"))
n=int(sys.argv[1]); fs=int(sys.argv[2]) if len(sys.argv)>2 else 12
R=roles[str(n)]
ops,info=build_page(R,SPECS[n],[d[0] for d in R["dele"]],fs=fs)
print(info)
json.dump(ops,open(f"ops{n}.json","w"))
