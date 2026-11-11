# usage: python3 -I compare_sweeps.py <base sweep dir> <patched sweep dir> <max seed> <out.json>
import json, glob, re, collections, sys
def T(k):
    if k.startswith("$"): return k.split("@")[0]
    if "[" not in k: return k
    head, field = k.rsplit("]", 1)
    return head[:head.rindex("[")].split(".")[-1] + field
def load(d, maxseed):
    out = {}
    for f in glob.glob(f"{d}/s*.jsonl"):
        s = int(re.findall(r"s(\d+)\.jsonl", f)[0])
        if s > maxseed: continue
        for l in open(f):
            r = json.loads(l); out[(r["seed"], r["i"])] = r
    return out
a, b = load(sys.argv[1], int(sys.argv[3])), load(sys.argv[2], int(sys.argv[3]))
def cls(r):
    o = set()
    for c, ks in (("out", list(r.get("outOfOrder") or {}) + (r.get("reached") or [])), ("unread", r.get("askedUnread") or []), ("early", (r.get("early") or []) + (r.get("randomEarly") or []) + (r.get("subsetEarly") or []))):
        o |= {(c, T(k)) for k in ks}
    return o
A = collections.Counter(); B = collections.Counter()
st = qa = qb = more = less = moreR = lessR = qra = qrb = err = ca = affA = affB = unA = unB = 0
for k, ra in a.items():
    rb = b[k]
    st += ra.get("status") != rb.get("status")
    na, nb = ra.get("states", 0), rb.get("states", 0)
    if ra.get("status") == "complete":
        ca += 1; qa += na; qb += nb; more += nb > na; less += nb < na
        for x in cls(ra): A[x] += 1
        for x in cls(rb): B[x] += 1
        affA += bool(cls(ra)); affB += bool(cls(rb)); unA += len(ra.get("askedUnread") or []); unB += len(rb.get("askedUnread") or [])
    else:
        qra += na; qrb += nb; moreR += nb > na; lessR += nb < na
    err += len((rb.get("orderErrors") or []) + (rb.get("randomErrors") or []))
res = {"returns": len(a), "status_differs": st, "complete": ca, "qa": qa, "qb": qb, "less": less, "more": more, "refused": len(a) - ca, "qra": qra, "qrb": qrb, "lessR": lessR, "moreR": moreR, "order_errors": err, "affA": affA, "affB": affB, "unA": unA, "unB": unB,
       "pairsA": len(A), "pairsB": len(B), "templatesA": len({t for _, t in A}), "templatesB": len({t for _, t in B}), "left": [[c, t, B[(c, t)], A.get((c, t), 0)] for (c, t) in sorted(B)]}
json.dump(res, open(sys.argv[4], "w"))
print({k: v for k, v in res.items() if k != "left"}); print("left:", res["left"])
