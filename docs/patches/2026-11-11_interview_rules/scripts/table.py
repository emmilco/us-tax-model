# usage: python3 -I table.py <sweep dir> : per template, classes with return and seed counts
import json, glob, sys, re, collections
def T(k):
    if k.startswith("$"): return k.split("@")[0]
    if "[" not in k: return k
    head, field = k.rsplit("]", 1)
    return head[:head.rindex("[")].split(".")[-1] + field
d = sys.argv[1]
rows = [json.loads(l) for f in glob.glob(f"{d}/s*.jsonl") for l in open(f)]
comp = [r for r in rows if r.get("status") == "complete"]
by = collections.defaultdict(lambda: collections.defaultdict(set))
for r in comp:
    out = {T(k) for k in (r.get("outOfOrder") or {})}
    for c, ks in (("out-bank", out), ("out-random", {T(k) for k in r.get("reached") or []} - out), ("unread", {T(k) for k in r.get("askedUnread") or []}), ("early", {T(k) for k in (r.get("early") or []) + (r.get("randomEarly") or []) + (r.get("subsetEarly") or [])})):
        for t in ks: by[t][c].add((r["seed"], r["i"]))
print(json.dumps({"returns": len(rows), "complete": len(comp), "seeds": len({r["seed"] for r in rows}), "templates": {t: {c: len(v) for c, v in cs.items()} for t, cs in sorted(by.items())},
  "affected": len({x for cs in by.values() for v in cs.values() for x in v})}))
