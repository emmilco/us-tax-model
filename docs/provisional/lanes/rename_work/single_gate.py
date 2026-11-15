#!/usr/bin/env python3
"""Inputs read by exactly one line, a `choose` of the same document taking the input as an alternative's `then` with an
else of zero or false (a parameter line), whose guards do not read it, and not marked `gated_by` (T-281). Reads the
canonical build (canonical/<year>); run after a build."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
can = ROOT / "canonical" / "2025"
forms, params = [], {}
for p in sorted(can.glob("*.json")):
    d = json.loads(p.read_text())
    if set(d) in ({"form"}, {"def"}):
        forms.append((next(iter(d)), next(iter(d.values()))))
    elif set(d) == {"params"}:
        params.update(d["params"]["values"])
NOT = {"cite", "source", "label", "op", "ref", "def", "line"}
def refs(n, out):
    if isinstance(n, str): out.add(n)
    elif isinstance(n, list):
        for x in n: refs(x, out)
    elif isinstance(n, dict):
        for k, v in n.items():
            if k not in NOT: refs(v, out)
    return out
lines, docof, readers = {}, {}, {}
for kind, doc in forms:
    for l in doc["lines"]:
        lines[l["id"]] = l; docof[l["id"]] = doc["id"]
        r = refs(l["expr"], set())
        for x in l.get("refuses") or []: r.add(x["when"])
        if l.get("shown_when"): r.add(l["shown_when"])
        for x in r: readers.setdefault(x, []).append(l["id"])
def is_else(ref, ty):
    l = lines.get(ref)
    if not l or l["expr"].get("op") != "param": return False
    p = params.get(l["expr"]["ref"])
    if p is None: return False
    if ty == "Bool": return p["value"] is False
    if ty.startswith("Enum("): return l.get("type") == ty
    return ty in ("Dollars", "NonNegDollars") and p["value"] == 0
for kind, doc in forms:
    if kind != "form": continue
    for l in doc["lines"]:
        if l["expr"].get("op") != "input" or l.get("gated_by"): continue
        rs = sorted(set(readers.get(l["id"], [])))
        if len(rs) != 1: continue
        g = lines[rs[0]]
        e = g["expr"]
        if e.get("op") != "choose" or docof[g["id"]] != doc["id"]: continue
        alts = e["alternatives"]
        if not any(a["then"] == l["id"] for a in alts): continue
        if any(l["id"] in refs(a["guard"], set()) for a in alts): continue
        ok = all(a["then"] == l["id"] or (isinstance(a["then"], str) and is_else(a["then"], l["type"])) for a in alts)
        print(f"{l['id']:45} {l['type']:14} gate {g['id']}{'' if ok else '  (else not a parameter of the type)'}")
