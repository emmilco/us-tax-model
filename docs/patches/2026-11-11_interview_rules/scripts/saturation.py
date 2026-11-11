import json, glob, sys, os, re
def T(k):
    if k.startswith("$"): return k.split("@")[0]
    if "[" not in k: return k
    head, field = k.rsplit("]", 1)
    return head[:head.rindex("[")].split(".")[-1] + field
d = sys.argv[1]
files = sorted(glob.glob(f"{d}/s*.jsonl"), key=lambda f: int(re.findall(r"s(\d+)\.jsonl", f)[0]))
seen = {}; n = 0; comp = 0; last_new = 0
for f in files:
    rows = [json.loads(l) for l in open(f)]
    if len(rows) < 50: continue
    for r in rows:
        n += 1; comp += r.get("status") == "complete"
        for c, ks in (("out", list(r.get("outOfOrder") or {}) + (r.get("reached") or [])), ("unread", r.get("askedUnread") or []), ("early", (r.get("early") or []) + (r.get("randomEarly") or []) + (r.get("subsetEarly") or []))):
            for k in ks:
                key = (c, T(k))
                if key not in seen: seen[key] = (n, r["seed"], r["i"]); last_new = n
print(f"complete seeds' returns: {n} ({comp} complete); distinct (class, template) pairs {len(seen)}; distinct templates {len({t for _, t in seen})}; last new pair at return {last_new}")
for (c, t), (at, s, i) in sorted(seen.items(), key=lambda x: x[1][0]): print(f"  return {at:5d} (seed {s}, i {i}): {c} {t}")
print("order errors:", sum(len((r.get('orderErrors') or []) + (r.get('randomErrors') or [])) for f in files for r in map(json.loads, open(f))))
