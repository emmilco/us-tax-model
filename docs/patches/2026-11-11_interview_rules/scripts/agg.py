import json, glob, re, sys, collections
pat = sys.argv[1]
rows = [json.loads(l) for f in sorted(glob.glob(pat)) for l in open(f)]
def T(k):
    if k.startswith("$"): return k.split("@")[0]
    if "[" not in k: return k
    head, field = k.rsplit("]", 1)
    return head[:head.rindex("[")].split(".")[-1] + field
print("returns", len(rows), "seeds", len({r["seed"] for r in rows}))
print("kind/status", collections.Counter((r["kind"], r.get("status")) for r in rows))
print("with a Form 1095-A", sum(1 for r in rows if r["f1095a"]), "complete with one", sum(1 for r in rows if r["f1095a"] and r.get("status") == "complete"),
      "complete with a monthly one", sum(1 for r in rows if r.get("status") == "complete" and False in r["uniform"]))
def tally(name, get):
    by = collections.defaultdict(set); seeds = collections.defaultdict(set)
    for r in rows:
        for k in get(r) or []:
            by[T(k)].add((r["seed"], r["i"])); seeds[T(k)].add(r["seed"])
    print(f"== {name}: {len(by)} templates; returns affected {len(set().union(*by.values())) if by else 0}; seeds affected {len(set().union(*seeds.values())) if seeds else 0}")
    forms = collections.defaultdict(set)
    for t, s in by.items(): forms[t.split('.')[0]] |= s
    for f, s in sorted(forms.items()): print(f"   form {f}: {len(s)} returns: {sorted(s)[:6]}")
    for t, s in sorted(by.items()): print(f"     {t}: {len(s)} returns, {len(seeds[t])} seeds, first {sorted(s)[0]}")
tally("outOfOrder (bank walk exposure)", lambda r: list((r.get("outOfOrder") or {}).keys()))
tally("reached in random order", lambda r: r.get("reached"))
tally("askedUnread", lambda r: r.get("askedUnread"))
tally("readUnasked", lambda r: r.get("readUnasked"))
tally("early completion (walk)", lambda r: r.get("early"))
tally("early completion (random)", lambda r: r.get("randomEarly"))
tally("early completion (subsets)", lambda r: r.get("subsetEarly"))
print("order errors", [(r["seed"], r["i"], e) for r in rows for e in (r.get("orderErrors") or []) + (r.get("randomErrors") or [])][:10])
print("bad", [(r["seed"], r["i"], r["bad"]) for r in rows if r.get("bad")][:5])
print("not walked", [(r["seed"], r["i"], r["kind"], r.get("detail")) for r in rows if r["kind"] != "walked"][:10])
print("mean ms per return", sum(r["ms"] for r in rows) / max(1, len(rows)))
