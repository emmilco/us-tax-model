# usage: python3 -I causes.py <repo> trace1.jsonl ... > causes.json : per (template, class) the frontier lines with their expressions
import json, glob, sys, os, re
repo = sys.argv[1]
lines = {}
for f in glob.glob(f"{repo}/canonical/2025/*.json"):
    try: d = json.load(open(f))
    except Exception: continue
    doc = d.get("form") or d.get("def") or d
    if isinstance(doc, dict):
        for l in doc.get("lines") or []:
            if isinstance(l, dict) and "id" in l: lines[l["id"]] = l
def show(e):
    if isinstance(e, str): return e
    if isinstance(e, (int, float, bool)) or e is None: return json.dumps(e)
    if isinstance(e, list): return "[" + ", ".join(show(x) for x in e) + "]"
    if "const" in e: return json.dumps(e["const"])
    if "param" in e and "op" not in e: return "param " + e["param"]
    op = e.get("op")
    if op == "test" or op is None:
        for k in ("all", "any"):
            if k in e: return f"{k}(" + ", ".join(show(x) for x in e[k]) + ")"
        if "not" in e: return "not(" + show(e["not"]) + ")"
        for k, s in (("eq","="),("ne","!="),("lt","<"),("le","<="),("gt",">"),("ge",">=")):
            if k in e: return f"{show(e[k][0])} {s} {show(e[k][1])}"
    if op == "choose": return "choose{" + "; ".join(f"{show(a['guard'])} -> {show(a['then'])}" for a in e["alternatives"]) + "}"
    if op == "sum_over": return f"sum_over({e['collection']}, {show(e['field'])}" + (f", where {show(e['where'])}" if e.get("where") else "") + ")"
    return f"{op}(" + ", ".join(f"{k}={show(v)}" for k, v in e.items() if k != "op") + ")"
def tl(i):
    s = re.sub(r"\[[^\]]*\]", "", i)
    parts = s.split(".")
    for n in range(len(parts) - 1):
        c = ".".join(parts[n:])
        if c in lines: return c
    return s
out = {}
for f in sys.argv[2:]:
    for l in open(f):
        r = json.loads(l)
        if not r.get("found"): continue
        fr = []
        for x in r.get("frontier", []):
            t = tl(x["line"])
            if t in lines and not any(y["line"] == t for y in fr):
                fr.append({"line": t, "expr": show(lines[t]["expr"])[:900], "refuses": [show(g["when"]) for g in lines[t].get("refuses") or []], "decided": not x["value"].startswith("unknown"), "value": re.sub(r"\[[^\]]*\]", "", x["value"])[:80]})
        out[f"{r['template']}|{r['cls']}"] = {"seed": r["seed"], "i": r["i"], "hiddenBy": tl(r["hiddenBy"]) if r.get("hiddenBy") else None, "frontier": fr,
            "probe": [{"v": p["v"], "status": p["status"], "gate": tl(p["gate"]) if p.get("gate") else None, "same": p["sameValues"]} for p in r.get("probe") or []] or None}
print(json.dumps(out, indent=1))
