#!/usr/bin/env python3
"""The year-label lint: a line's label, or a question's prompt or help, that prints this year's amount of a dollar
parameter the line reads, when next year's staged value differs and no operation of changes/<year+1>/ rewrites that
text.

A form line reads its parameters in its expression (`op: param` and `param:` operands). A question reads the
parameters of its input's line and of every line that reads the input directly (a threshold the answer is tested
against). The text "prints" the amount when it holds the parameter's value as written in dollars (`$10,918.20`,
`$176,100`; a per-status value, each status's amount), not followed by another digit. Next year's values are the
staged ones of research/ty<year+1>/params-<year+1>.proposed.yaml; a parameter staged with no value (`value: null`)
is listed as a note and not checked until a value is staged, so the relabel joins the staging. A line's label is
rewritten by a `set` of `label` (or the line is removed); a question's text by a `set_question` of `prompt` or
`help`, a `set` of the line's `label` or `expr.source` (the prompt of a question with no prompt of its own), or
`remove_question`.

A hit fails unless tools/label_year_baseline.json holds it (`held`, by line or input id, with the reason the printed
amount stays right next year); a held id that is no longer a hit fails too, so the list only shrinks.

    check_label_year.py [--year N]     the check; exit 1 on a hit not held or a stale hold
    check_label_year.py --self-test    a planted tree
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import taxyear  # noqa: E402  (--year)
import year_changes as C  # noqa: E402

BASELINE = ROOT / "tools" / "label_year_baseline.json"
DOLLAR_TYPES = ("Dollars", "NonNegDollars")


def amount_texts(value):
    """The dollar amounts a parameter value prints as: one per status for a per-status value."""
    values = value.values() if isinstance(value, dict) else [value]
    out = set()
    for v in values:
        if isinstance(v, bool) or not isinstance(v, int):
            continue
        v = abs(v)
        out.add(f"${v // 100:,}" if v % 100 == 0 else f"${v / 100:,.2f}")
    return out


def prints(text, amounts):
    """The amounts of `amounts` that `text` holds, not followed by a digit (`$5,300` is not in `$5,3000` or `$5,300.50`)."""
    return sorted(a for a in amounts if re.search(re.escape(a) + r"(?![0-9]|[.,][0-9])", text or ""))


def text_of(node):
    """A label or prompt as one string (a structured label's strings joined)."""
    if isinstance(node, str):
        return node
    if isinstance(node, list):
        return "\n".join(text_of(x) for x in node)
    if isinstance(node, dict):
        return "\n".join(text_of(v) for v in node.values())
    return ""


def hits(forms, bank, params, staged, ops):
    """(hits, notes): hits maps a line or input id to what it prints; notes name the parameters staged without a value.
    `forms` maps form id to its document, `bank` is the question list, `params` this year's values by id (with
    `type` and `value`), `staged` next year's, `ops` the operations of next year."""
    relabeled_lines, retexted_inputs = set(), set()
    for op in ops:
        b = op.body
        if op.kind == "set" and b.get("field") == "label" or op.kind == "remove_line":
            relabeled_lines.add(b.get("line"))
        if op.kind == "set" and b.get("field") == "expr.source":
            retexted_inputs.add(b.get("line"))
        if op.kind == "set_question" and b.get("field") in ("prompt", "help") or op.kind == "remove_question":
            retexted_inputs.add(b.get("input"))

    def changed(pid):
        p, s = params.get(pid), staged.get(pid)
        if not p or p.get("type") not in DOLLAR_TYPES or not isinstance(s, dict) or "value" not in s:
            return None
        return "unstaged" if s["value"] is None else (s["value"] != p.get("value"))

    lines = {l["id"]: l for f in forms.values() for l in f.get("lines") or [] if isinstance(l, dict) and "id" in l}
    readers = {}
    for lid, l in lines.items():
        for r in C.reads_of(l):
            readers.setdefault(r, set()).add(lid)
    out, notes = {}, set()

    def check(where, text, pids):
        found = []
        for pid in sorted(pids):
            state = changed(pid)
            if not state:
                continue
            printed = prints(text, amount_texts(params[pid].get("value")))
            if not printed:
                continue
            if state == "unstaged":
                notes.add(f"{where} prints {', '.join(printed)} ({pid}), whose next-year value is not staged; checked once it is")
            else:
                found.append(f"{', '.join(printed)} ({pid})")
        return found

    for lid, l in sorted(lines.items()):
        if lid in relabeled_lines:
            continue
        found = check(lid, text_of(l.get("label")), C.params_of(l.get("expr")))
        if found:
            out[lid] = f"its label prints {'; '.join(found)}"
    for q in bank:
        inp = q.get("input", "")
        line = lines.get(inp)
        if inp in retexted_inputs or line is None:
            continue
        pids = set(C.params_of(line.get("expr")))
        for r in readers.get(inp, ()):
            pids |= C.params_of(lines[r].get("expr"))
        prompt = q.get("prompt") or (line.get("expr") or {}).get("source") or ""
        found = check(inp, f"{text_of(prompt)}\n{text_of(q.get('help'))}", pids)
        if found:
            out[inp] = f"its question prints {'; '.join(found)}"
    return out, sorted(notes)


def problems(found, held):
    out = []
    for k, what in sorted(found.items()):
        if k not in held:
            out.append(f"{k}: {what}, which changes next year, and no operation of changes/<next year>/ rewrites it: "
                       "add a `set` of its label (or `set_question` of its prompt) printing the staged amount, or hold it in "
                       "tools/label_year_baseline.json with the reason the amount stays right")
    for k in sorted(held):
        if k not in found:
            out.append(f"{k}: held in tools/label_year_baseline.json but no longer a hit; remove it")
    return out


def load_staged(year):
    path = ROOT / "research" / f"ty{year}" / f"params-{year}.proposed.yaml"
    if not path.exists():
        return None, path
    return ((C.load_yaml(path.read_text(encoding="utf-8")) or {}).get("params") or {}).get("values") or {}, path


def run(year):
    staged, path = load_staged(year + 1)
    if staged is None:
        print(f"label-year: no staged values for {year + 1} ({path.relative_to(ROOT)}); nothing to check")
        return 0
    tree = C.year_tree(year)
    params = ((C.load_yaml(Path(C.jurisdiction.params_file(year)).read_text(encoding="utf-8")) or {}).get("params") or {}).get("values") or {}
    _, ops, bad = C.load_changes(ROOT / "changes" / str(year + 1))
    if bad:
        print("label-year: changes files do not load (year_changes.py --check names them):\n  " + "\n  ".join(bad), file=sys.stderr)
        return 1
    found, notes = hits({k: v["doc"] for k, v in tree.forms.items()}, tree.bank.get("questions") or [], params, staged, ops)
    held = json.loads(BASELINE.read_text(encoding="utf-8")).get("held") or {}
    for n in notes:
        print(f"  note: {n}")
    probs = problems(found, held)
    for p in probs:
        print(f"  {p}", file=sys.stderr)
    print(f"label-year: {len(found)} text(s) printing a {year} amount that changes in {year + 1} with no operation, "
          f"{sum(1 for k in found if k in held)} held, {len(notes)} waiting on a staged value, {len(probs)} problem(s)")
    return 1 if probs else 0


def self_test():
    params = {"p.lim": {"type": "NonNegDollars", "value": 1091820}, "p.base": {"type": "NonNegDollars", "value": 17610000},
              "p.same": {"type": "NonNegDollars", "value": 50000}, "p.none": {"type": "NonNegDollars", "value": 160000},
              "p.status": {"type": "NonNegDollars", "value": {"single": 8900000, "mfj": 24600000}},
              "p.rate": {"type": "Rate", "value": {"num": 15, "den": 100}}}
    staged = {"p.lim": {"value": 1143900}, "p.base": {"value": 18450000}, "p.same": {"value": 50000},
              "p.none": {"value": None}, "p.status": {"value": {"single": 9100000, "mfj": 25200000}}, "p.rate": {"value": {"num": 2, "den": 10}}}
    ln = lambda i, label, expr: {"id": i, "label": label, "expr": expr}  # noqa: E731
    forms = {"a": {"lines": [
        ln("a.over", "Did this employer withhold more than $10,918.20?", {"op": "test", "gt": ["a.box4", {"param": "p.lim"}]}),
        ln("a.base", "Wages over $176,100", {"op": "param", "ref": "p.base"}),
        ln("a.done", "Wages over $176,100", {"op": "param", "ref": "p.base"}),
        ln("a.same", "Over $500", {"op": "param", "ref": "p.same"}),
        ln("a.none", "Over $1,600", {"op": "param", "ref": "p.none"}),
        ln("a.longer", "Over $176,1000", {"op": "param", "ref": "p.base"}),
        ln("a.status", "$246,000", {"op": "param", "ref": "p.status"}),
        ln("a.rate", "15%", {"op": "param", "ref": "p.rate"}),
        ln("a.box4", "Box 4", {"op": "input", "source": "Box 4"}),
        ln("a.q", "Q", {"op": "input", "source": "Q"}),
        ln("a.test_q", "test", {"op": "test", "gt": ["a.q", {"param": "p.lim"}]}),
    ]}}
    bank = [{"input": "a.q", "prompt": "Was more than $10,918.20 withheld?"}, {"input": "a.box4", "prompt": "Box 4 of the W-2"}]
    Op = lambda kind, body: C.Op("x.yaml", "C-1", 1, kind, body, {})  # noqa: E731
    ops = [Op("set", {"line": "a.done", "field": "label", "from": "Wages over $176,100", "to": "Wages over $184,500"})]
    found, notes = hits(forms, bank, params, staged, ops)
    assert sorted(found) == ["a.base", "a.over", "a.q", "a.status"], found
    assert "$246,000 (p.status)" in found["a.status"], found["a.status"]
    assert len(notes) == 1 and notes[0].startswith("a.none prints $1,600"), notes
    found2, _ = hits(forms, bank, params, staged, ops + [Op("set_question", {"input": "a.q", "field": "prompt", "from": "x", "to": "y"})])
    assert "a.q" not in found2, "a set_question rewrites the prompt"
    assert problems(found, {k: "r" for k in found}) == []
    assert problems(found, {}) and all("no operation" in p for p in problems(found, {}))
    assert any("no longer a hit" in p for p in problems(found, {**{k: "r" for k in found}, "a.same": "r"}))
    assert prints("$5,3000 and $5,300.50", {"$5,300"}) == [] and prints("($5,300)", {"$5,300"}) == ["$5,300"]
    held = json.loads(BASELINE.read_text(encoding="utf-8")).get("held") or {}
    assert all(isinstance(v, str) and v.strip() for v in held.values()), "every hold states its reason"
    print("check_label_year self-test: passed (a planted tree: 4 hits of 11 lines and 2 questions; a relabeled line, an unchanged, "
          "an unstaged and a non-dollar parameter, a longer number and a set_question not hits; per-status amounts; the baseline)")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--year", type=int)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    return run(int(taxyear.Y))


if __name__ == "__main__":
    sys.exit(main())
