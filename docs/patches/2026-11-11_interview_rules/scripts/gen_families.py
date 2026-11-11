# usage: python3 -I gen_families.py > out/catalog_families.md   (per-family sections and the ranked table)
import json, sys, re, glob, collections, os
sys.path.insert(0, "/tmp/f1095a/scripts")
from fam_meta import FAMS
O = "/tmp/f1095a/out"
fs = json.load(open(f"{O}/famsummary.json"))
unread = json.load(open(f"{O}/unread_stats.json"))
lines = {}
for f in glob.glob("/tmp/f1095a/base/canonical/2025/*.json"):
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
def pretty(xs):
    by = collections.defaultdict(list)
    for x in xs:
        c, t = x.split(":", 1); by[{"randomEarly": "left reachable at completion", "early": "left reachable at completion", "out": "out of bank order", "reached": "out of bank order", "unread": "asked and unread"}[c]].append(t)
    def fold(ts):
        out = []
        for col in ("a", "b"):
            ms = [t for t in ts if t.startswith(f"f1095a.in_{col}_")]
            if ms: out.append(f"`f1095a.in_{col}_<month>` ({len(set(ms))} months)")
        return out + [f"`{t}`" for t in sorted(set(ts)) if not t.startswith("f1095a.in_")]
    return "; ".join(f"{c}: " + ", ".join(fold(ts)) for c, ts in sorted(by.items())) or "none"
rank = []
for m in FAMS:
    r = fs.get(m["key"])
    print(f"### {m['id']}. {m['title']}\n")
    print(f"- **Cause lines** (`forms/2025/`, as on main):")
    for l in m["lines"]:
        e = show(lines[l]["expr"]) if l in lines else "?"
        ref = "; refusal gates: " + ", ".join(show(g["when"]) for g in lines[l].get("refuses") or []) if l in lines and lines[l].get("refuses") else ""
        print(f"  - `{l}` := `{e[:520]}{'…' if len(e) > 520 else ''}`{ref}")
    print(f"- **Pattern:** {m['pattern']}")
    print(f"- **What a filer meets:** {m['effect']}")
    print(f"- **Rewrite:** {m['rewrite']} Patch: `/tmp/f1095a/patches/{m['key']}.patch`.")
    if not r or r["status"] != "ok":
        print(f"- **Test:** {'not run' if not r else r['status']}.\n"); rank.append((m, None)); continue
    w = r["witness"] or {}
    fx = f"federal {r['fixtures_fed']}, New York {r['fixtures_ny']}"
    note = " The one federal fixture that changes is `stage8.mut.hoh_child_months_unanswered_absence`: `dependent[child].hoh_test2` was false and is unknown, with `dependent[child].months` unanswered (an incomplete state; no value or refusal of a complete return changes)." if r["fixtures_fed"].split("/")[0] != r["fixtures_fed"].split("/")[1] else ""
    d = r["differential"] or {}
    print(f"- **Test (this family alone, on main's tip):** build OK; fixtures pass {fx}.{note} Target values and status of {d.get('generated', '?')} generated returns ({d.get('complete', '?')} complete) and of every fixture's inputs: {d.get('differ', '?')} differ from main."
          f" On the {w.get('returns', 0)} sweep returns that showed the family: questions asked in bank order {w.get('asked_before', 0)} to {w.get('asked_after', 0)} ({w.get('asked_before', 0) - w.get('asked_after', 0)} saved on {w.get('returns_shorter', 0)} returns); status differs on {w.get('status_differs', '?')}, values on {w.get('values_differ', '?')}; order errors {w.get('order_errors', '?')}."
          f" Gone there: {pretty(w.get('gone') or [])}. New there: {pretty(w.get('new') or [])}."
          + (f" Standard length set (full profile, {r['standard']['walks']} walks, complete and refused): {r['standard']['before']} to {r['standard']['after']} questions." if r.get("standard") else ""))
    print(f"- **Touched:** {len(r['rewritten'])} line(s) rewritten, {r['helpers_added']} helper line(s) added, in {', '.join('`' + f.split('/')[-1] + '`' for f in r['files'])} (+{r['patch_lines'][0]}/-{r['patch_lines'][1]} lines); "
          f"{r['pins']['moved']} of {r['pins']['live']} pinned mutation arguments un-pinned; rendered files changed: {', '.join('`' + x.split('/')[-1] + '`' for x in r['rendered']) or 'none'}; "
          f"review subjects (transcription, render, class M) of {', '.join(sorted({'`' + f.split('/')[-1][:-5] + '`' for f in r['files']}))}.")
    if not m.get("note"): print()
    if m.get("note"): print(f"- **Note:** {m['note']}\n")
    rank.append((m, r))
json.dump([{"id": m["id"], "key": m["key"]} for m, _ in rank], open(f"{O}/rank_ids.json", "w"))
