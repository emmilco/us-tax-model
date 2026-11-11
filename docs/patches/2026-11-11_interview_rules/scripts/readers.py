# usage: python3 -I readers.py <repo> <id> [<id> ...] : the line itself (if a computed line) and every line that reads it, compactly
import json, glob, sys, os
repo = sys.argv[1]
lines = {}
for f in glob.glob(f"{repo}/canonical/2025/*.json"):
    try: d = json.load(open(f))
    except Exception: continue
    doc = d.get("form") or d.get("def") or d
    for l in (doc.get("lines") or []) if isinstance(doc, dict) else []:
        if isinstance(l, dict) and "id" in l: lines[l["id"]] = (os.path.basename(f), l)
def show(e):
    if isinstance(e, str): return e
    if isinstance(e, (int, float, bool)) or e is None: return json.dumps(e)
    if isinstance(e, list): return "[" + ", ".join(show(x) for x in e) + "]"
    if "const" in e and len(e) <= 2: return json.dumps(e["const"])
    op = e.get("op")
    if op == "test" or (op is None and any(k in e for k in ("all","any","not","eq","ne","lt","le","gt","ge"))):
        for k in ("all", "any"):
            if k in e: return f"{k}(" + ", ".join(show(x) for x in e[k]) + ")"
        if "not" in e: return "not(" + show(e["not"]) + ")"
        for k, s in (("eq","="),("ne","!="),("lt","<"),("le","<="),("gt",">"),("ge",">=")):
            if k in e: return f"{show(e[k][0])} {s} {show(e[k][1])}"
    if op == "choose": return "choose{" + "; ".join(f"{show(a['guard'])} -> {show(a['then'])}" for a in e["alternatives"]) + "}"
    rest = {k: v for k, v in e.items() if k != "op"}
    return f"{op}(" + ", ".join(f"{k}={show(v)}" for k, v in rest.items()) + ")"
def refs(e, out):
    if isinstance(e, str): out.add(e)
    elif isinstance(e, list): [refs(x, out) for x in e]
    elif isinstance(e, dict): [refs(v, out) for k, v in e.items() if k not in ("cite", "label", "source", "printed")]
    return out
def extras(l):
    x = []
    if l.get("shown_when"): x.append(f"shown_when {l['shown_when']}")
    for r in l.get("refuses") or []: x.append(f"refuses when {show(r['when'])}")
    for k in ("bindings", "where"):
        if l.get(k): x.append(f"{k} {show(l[k])}")
    return ("  [" + "; ".join(x) + "]") if x else ""
for t in sys.argv[2:]:
    print(f"### {t}")
    if t in lines:
        f, l = lines[t]; print(f"  DEF {f}: {t} := {show(l['expr'])[:(120 if l['expr'].get('op')=='input' else 1500)]}{extras(l)[:600]}")
    for i, (f, l) in sorted(lines.items()):
        r = refs(l["expr"], set()) | refs(l.get("refuses") or [], set()) | ({l["shown_when"]} if isinstance(l.get("shown_when"), str) else set())
        if t in r and i != t: print(f"  READ BY {i} := {show(l['expr'])[:1200]}{extras(l)[:500]}")
