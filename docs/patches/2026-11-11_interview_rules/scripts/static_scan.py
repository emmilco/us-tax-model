# usage: python3 -I static_scan.py <repo> : every federal line whose expression (or sum_over where) is an all/any test of two
# or more operands, with the inputs each operand can reach (transitively), so the candidates for "an operand read past an
# unknown one" are listed whether or not a sampled return shows them.
import json, glob, sys, os
repo = sys.argv[1]
lines = {}
for f in glob.glob(f"{repo}/canonical/2025/*.json"):
    try: d = json.load(open(f))
    except Exception: continue
    doc = d.get("form") or d.get("def") or d
    if not isinstance(doc, dict): continue
    for l in doc.get("lines") or []:
        if isinstance(l, dict) and "id" in l: lines[l["id"]] = (doc.get("id"), l)
def refs(e, out):
    if isinstance(e, str):
        if e in lines: out.add(e)
    elif isinstance(e, list): [refs(x, out) for x in e]
    elif isinstance(e, dict): [refs(v, out) for k, v in e.items() if k not in ("cite", "label", "source", "printed")]
    return out
memo = {}
def inputs_of(i, stack=()):
    if i in memo: return memo[i]
    if i in stack: return set()
    l = lines[i][1]
    if l["expr"].get("op") == "input": memo[i] = {i}; return memo[i]
    out = set()
    for r in refs(l["expr"], set()): out |= inputs_of(r, stack + (i,))
    memo[i] = out; return out
def conj(e):
    if isinstance(e, dict):
        if e.get("op") == "test" and ("all" in e or "any" in e): yield e
        for k, v in e.items():
            if k not in ("cite",): yield from conj(v)
    elif isinstance(e, list):
        for x in e: yield from conj(x)
out = []
for i, (doc, l) in sorted(lines.items()):
    if str(doc).startswith("ny_"): continue
    top = l["expr"]
    cs = list(conj(top))
    if not cs: continue
    c = cs[0]; kind = "all" if "all" in c else "any"; ops = c[kind]
    if len(ops) < 2: continue
    per = []
    for o in ops:
        s = set()
        for r in refs(o, set()): s |= inputs_of(r)
        per.append(s)
    later_new = any(per[k] - set().union(*per[:k]) for k in range(1, len(per)))
    out.append({"line": i, "doc": doc, "kind": kind, "n": len(ops), "where": top.get("op") == "sum_over", "inputs": [len(p) for p in per], "later_reads_new_input": later_new})
cand = [o for o in out if o["later_reads_new_input"]]
print(f"federal lines with a top-level all/any of 2+ operands (incl. sum_over where): {len(out)}; of them a later operand reads an input no earlier operand reads: {len(cand)}")
import collections
print("by document:", dict(collections.Counter(o["doc"] for o in cand).most_common()))
json.dump(cand, open("/tmp/f1095a/out/static_candidates.json", "w"))
