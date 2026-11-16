import sys,json
# usage: rep.py file pairs.json  (list of [old,new])
p=sys.argv[1]; pairs=json.load(open(sys.argv[2]))
s=open(p).read()
for o,n in pairs:
    c=s.count(o)
    if c!=1: sys.exit(f"count {c} for: {o[:80]}")
    s=s.replace(o,n)
open(p,'w').write(s); print("ok",p,len(pairs))
