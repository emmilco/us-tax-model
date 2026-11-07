#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Formal gates as the review tools see them.

A gated input is an input line marked `gated_by: <gate line>`; the gate line is a `choose` of the same document that
takes the input when its guard holds and otherwise a parameter of the input's type: zero, false or a designated enum
value (engine/src/gates.ts checks the convention). The review unit is the gate's condition: the one line every guard of a gate line reads (an applicability or existence
`Bool` the filer answers, or a computed condition), with every gate line that guards on it. A gate line whose guards
read more than one line is a unit of its own. Units are keyed `gate:<condition>`.

The screen review (screen_review.py) and the false-no review (false_no_review.py) give a unit's condition, its wording
as the filer reads it, and each gate line with its gated input and their English, against the pages they cite. A
unit's subject (`subject`) is what those reviews judge: the condition's line and wording and each gate line's and gated
input's line, English and wording, citations included. The review prompt's own text and the archived page text are
not in it, so a prompt change applies at a unit's next real change.
"""
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from transcribe import ROOT  # noqa: E402
from taxyear import Y  # noqa: E402
import jurisdiction  # noqa: E402
from structured_text import indent_rest  # noqa: E402

NOT_REFS = {"cite", "source", "label", "op", "ref", "def", "line", "const", "param"}


def refs(node, out=None):
    """Every string in an expression that can name a line (gates.ts refsOf)."""
    out = set() if out is None else out
    if isinstance(node, str):
        out.add(node)
    elif isinstance(node, list):
        for n in node:
            refs(n, out)
    elif isinstance(node, dict):
        for k, v in node.items():
            if k not in NOT_REFS:
                refs(v, out)
    return out


def units(lines):
    """{"gate:<condition>": {"key", "condition" (a line id or None), "gates": [(doc, gate line, gated input line)]}}
    over `lines` ({id: (doc, line)}, screen_review.load_lines), for the gate lines of the jurisdiction under review."""
    out = {}
    for lid, (doc, l) in sorted(lines.items()):
        gate_id = l.get("gated_by")
        if not gate_id or not jurisdiction.mine(doc) or gate_id not in lines:
            continue
        gdoc, gate = lines[gate_id]
        if (gate.get("expr") or {}).get("op") != "choose":
            continue
        guard_refs = sorted(refs([a.get("guard") for a in gate["expr"].get("alternatives", [])]) & set(lines))
        condition = guard_refs[0] if len(guard_refs) == 1 else None
        key = "gate:" + (condition or gate_id)
        unit = out.setdefault(key, {"key": key, "condition": condition, "gates": []})
        unit["gates"].append((gdoc, gate, l))
    for u in out.values():
        u["gates"].sort(key=lambda g: g[1]["id"])
    return dict(sorted(out.items()))


def unit_form(unit, lines):
    """The document a unit's review is logged under: its condition's, or its first gate line's."""
    return lines[unit["condition"]][0] if unit["condition"] else unit["gates"][0][0]


_QUESTIONS = None


def questions():
    """{input template: {"prompt", "help"}}: the wording the interview shows, from the built profiles (the New York
    profile asks every federal question too)."""
    global _QUESTIONS
    if _QUESTIONS is None:
        _QUESTIONS = {}
        for name in ("interview-full.json", "interview-ny.json"):
            path = os.path.join(ROOT, "canonical", str(Y), name)
            if os.path.exists(path):
                with open(path, encoding="utf-8") as f:
                    profile = json.load(f)
                for q in profile["questions"]:
                    _QUESTIONS[q["input"]] = {"prompt": q["prompt"], "help": q.get("help", "")}
    return _QUESTIONS


def wording(line):
    """The question a filer reads for an input line: the interview's prompt and help, or the line's own question text."""
    q = questions().get(line["id"])
    if q:
        return q
    return {"prompt": (line.get("expr") or {}).get("source", ""), "help": ""}


def subject(unit, lines, english):
    """The unit's subject hash: what its reviews judge (see the module docstring). `english(doc, line id)` gives a
    line's rendered English."""
    cond = unit["condition"]
    body = {"condition": None, "gates": []}
    if cond:
        cdoc, cline = lines[cond]
        body["condition"] = {"line": cline, "english": english(cdoc, cond),
                             "wording": wording(cline) if (cline.get("expr") or {}).get("op") == "input" else None}
    for gdoc, gate, inp in unit["gates"]:
        body["gates"].append({"gate": gate, "english": english(gdoc, gate["id"]), "input": inp, "wording": wording(inp)})
    return hashlib.sha256(json.dumps(body, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def describe(unit, lines, english):
    """The condition and gated lines as a prompt gives them: (condition text, [gated line items])."""
    cond = unit["condition"]
    if cond:
        cdoc, cline = lines[cond]
        if (cline.get("expr") or {}).get("op") == "input":
            w = wording(cline)
            condition = (f"The filer is asked (input `{cond}`, document {cdoc}): {indent_rest(w['prompt'], '    ')}"
                         + (f"\n  Help shown with it: {indent_rest(w['help'], '    ')}" if w["help"] else "")
                         + f"\n  Cited: {cline['cite']['doc']} {cline['cite']['locator']}")
        else:
            condition = (f"A condition the tool computes (line `{cond}`, document {cdoc}): {indent_rest(cline['label'], '    ')}"
                         f"\n  Computed as: {indent_rest(english(cdoc, cond), '    ')}\n  Cited: {cline['cite']['doc']} {cline['cite']['locator']}")
    else:
        condition = "The guards of the gate line below (more than one line decides it)."
    items = []
    for gdoc, gate, inp in unit["gates"]:
        w = wording(inp)
        items.append(f"""- Line `{gate['id']}` (document {gdoc}, printed {gate['printed']}): {indent_rest(gate['label'], '    ')}
  When the condition holds: {indent_rest(english(gdoc, gate['id']), '    ')}
  Otherwise: zero, and the question below is not asked.
  Gated question (input `{inp['id']}`): {indent_rest(w['prompt'], '    ')}""" + (f"\n  Help shown with it: {indent_rest(w['help'], '    ')}" if w["help"] else "") + f"""
  Cited: {gate['cite']['doc']} {gate['cite']['locator']}; the input cites {inp['cite']['doc']} {inp['cite']['locator']}""")
    return condition, items


def pseudo_form(unit, lines):
    """A form-shaped object whose lines are the unit's, for transcribe.excerpt_for (the pages they cite)."""
    own = ([lines[unit["condition"]][1]] if unit["condition"] else []) + [x for _, g, i in unit["gates"] for x in (g, i)]
    return {"id": unit["key"], "lines": own}


def safe_name(key):
    """A unit key as a file name."""
    return re.sub(r"[^A-Za-z0-9_.-]", "_", key)
