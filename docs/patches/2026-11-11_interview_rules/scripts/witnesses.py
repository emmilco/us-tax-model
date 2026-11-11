# usage: python3 -I witnesses.py '<glob of sweep jsonl>' <per pair> > witnesses.json
import json, glob, sys, collections
def T(k):
    if k.startswith("$"): return k.split("@")[0]
    if "[" not in k: return k
    head, field = k.rsplit("]", 1)
    return head[:head.rindex("[")].split(".")[-1] + field
held = set()
got = collections.defaultdict(list)
rows = sorted((json.loads(l) for f in glob.glob(sys.argv[1]) for l in open(f)), key=lambda r: (r.get("states") or 0))
n = int(sys.argv[2])
for r in rows:
    out = set(T(k) for k in (r.get("outOfOrder") or {}))
    for cls, ks in (("out", out), ("random", set(T(k) for k in r.get("reached") or []) - out), ("unread", set(T(k) for k in r.get("askedUnread") or [])), ("early", set(T(k) for k in (r.get("randomEarly") or []) + (r.get("early") or []) + (r.get("subsetEarly") or [])))):
        for t in ks:
            if len(got[(t, cls)]) < n: got[(t, cls)].append({"template": t, "cls": cls, "seed": r["seed"], "i": r["i"]})
print(json.dumps([w for k in sorted(got) for w in got[k]]))
