#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Operand check (T-085), offline, in check-all.

A computed line printed with a line number whose printed instruction is arithmetic over named lines ("Add lines 1
through 3", "Combine lines 7 and 15", "Subtract line 5 from line 4", "Enter the smaller of line 3 or line 6") must
have exactly those lines as operands, after same-form helpers are followed. The printed instruction is taken from the
line's citation quotes, which tools/citations.py verifies against the archived form, and else from its label.

`missing`: a named line is not an operand. Under the refused-operand convention a line that is out of scope stays in
the expression as a reference to the refused line rather than being dropped, so a missing operand is accepted only by
a ruling that names the refusal guarding the line ({"reason": ..., "refusal": "<gate line id>"}); the check verifies
that the gate is declared on the line. `extra`: for an addition, an operand the instruction does not name.

Rulings and baseline: reviews/<year>/operands.json (tools/baseline_check.py); report: reports/<year>/operands.md.

    check_operands.py [--baseline] | --self-test
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402
from citations import split_top  # noqa: E402
import baseline_check  # noqa: E402
from baseline_check import line_subject  # noqa: E402

CANONICAL = ROOT / "canonical" / Y
RULINGS = ROOT / "reviews" / Y / "operands.json"
REPORT = ROOT / "reports" / Y / "operands.md"

PRINTED = re.compile(r"^\d{1,2}[a-z]?$")
NUM = r"\d{1,2}[a-z]?"
VERB = re.compile(r"^(Add|Combine|Enter the total of|Total of|Subtract|Enter the smaller of|Enter the larger of)\b(.*)", re.I | re.S)
ADDITIVE = {"add", "combine", "enter the total of", "total of"}
# Another document named in the instruction: only Form 1040 and its schedules are resolved.
OTHER_DOC = re.compile(r"(Schedule 1|Schedule 2|Schedule 3|Form 1040|Form 8959|Schedule SE)( \(Form 1040\))?,? lines?")
DOC_IDS = {"Schedule 1": "s1", "Schedule 2": "s2", "Schedule 3": "s3", "Form 1040": "f1040", "Form 8959": "f8959",
           "Schedule SE": "se"}


def norm(printed):
    """A printed marker as a line number: "(SMW 4)" -> "4", "6(a)" -> "6"; other text unchanged."""
    p = str(printed).strip()
    m = re.match(r"^\(?(?:[A-Z]{2,4}(?: [AB])?|Step \d+,)\s*(\d{1,2}[a-z]?)\)?$", p)
    if m:
        return m.group(1)
    m = re.match(r"^(\d{1,2}[a-z]?)\s*\((?:[a-z]|i+v?|iv|v)\)$", p)
    return m.group(1) if m else p


def refs(expr, lines):
    if isinstance(expr, str):
        return [expr] if expr in lines else []
    if isinstance(expr, dict):
        # A choose guard selects an alternative; it is not an operand.
        return [r for k, v in expr.items() if k not in ("op", "source", "guard") for r in refs(v, lines)]
    if isinstance(expr, list):
        return [r for v in expr for r in refs(v, lines)]
    return []


def operands(line_id, lines, depth=0, seen=None):
    """Printed numbers reached from a line through same-form helpers ("form:n" for another form's line)."""
    seen = set() if seen is None else seen
    form = lines[line_id]["form"]
    out = set()
    for r in refs(lines[line_id].get("expr"), lines):
        if r in seen:
            continue
        seen.add(r)
        target = lines[r]
        p = norm(target.get("printed", ""))
        if target["form"] != form:
            out.add(f"{target['form']}:{p}")
        elif PRINTED.match(p):
            out.add(p)
        elif depth < 4:
            out |= operands(r, lines, depth + 1, seen)
    return out


# Where the result goes ("... here and on Schedule 1, line 1") is not an operand.
DESTINATION = re.compile(r"\s*(?:,?\s*here and on|,?\s*and enter (?:this amount|the total|the result|here)|,?\s*and on (?:Schedule|Form)|"
                         r";?\s*also enter|,?\s*here and in)\b.*", re.I | re.S)


def clause_of(rest):
    return DESTINATION.sub("", re.split(r"\.(?:\s|$)", rest)[0])


def named(text):
    """Line numbers an instruction names: explicit numbers and (start, end) ranges."""
    text = clause_of(text)
    ranges = set(re.findall(rf"({NUM})\s+through\s+({NUM})", text))
    rest = re.sub(rf"({NUM})\s+through\s+({NUM})", "", text)
    single = set(re.findall(rf"\b(?:line|lines|and|or|from)\s+({NUM})\b", rest)) | set(re.findall(rf",\s*({NUM})\b", rest))
    return single, ranges


def order(p):
    m = re.match(r"(\d+)([a-z]?)", p)
    return (int(m.group(1)), m.group(2)) if m else None


def instruction(line):
    """The printed arithmetic instruction: the first citation quote that is one, else the label."""
    cite = line.get("cite", {})
    quotes = [q for _, qs in split_top(cite.get("locator", "")) for q in qs]
    for text in quotes + [str(line.get("label", ""))]:
        # A worksheet quote starts with its own line number ("5. Enter the total of ...").
        m = VERB.match(re.sub(r"^\d{1,2}[a-z]?\.\s*", "", text.strip()))
        if m:
            return m.group(1).lower(), m.group(2)
    return None


def findings(forms):
    lines = {l["id"]: dict(l, form=f["id"]) for f in forms for l in f["lines"]}
    out = []
    for lid, line in lines.items():
        # Printed lines and worksheet lines ("(CLW 2)"), not helpers.
        if not PRINTED.match(norm(line.get("printed", ""))):
            continue
        if line.get("expr", {}).get("op") in ("input", "param"):
            continue
        found = instruction(line)
        if not found:
            continue
        verb, rest = found
        clause = clause_of(rest)
        # Instructions over a worksheet's own lines, table columns or both copies of a form name lines that are not
        # this form's printed lines.
        if re.search(r"worksheet|column|both Forms|each Form", clause, re.I):
            continue
        other = OTHER_DOC.search(clause)
        target = line["form"]
        if other:
            target = DOC_IDS[other.group(1)]
        elif re.search(r"Schedule|Form \d", clause):
            continue
        single, ranges = named(rest)
        if not single and not ranges:
            continue
        have = operands(lid, lines)
        same = {h.split(":", 1)[1] for h in have if h.startswith(target + ":")} if target != line["form"] else \
               {h for h in have if ":" not in h}
        missing, extra = set(), set(same)
        for a, b in ranges:
            # Every line number in the range must be an operand (any lettered line of that number counts).
            inside = {h for h in same if order(h) and order(a) <= order(h) <= order(b)}
            extra -= inside
            numbers = {order(h)[0] for h in inside}
            gaps = [str(k) for k in range(order(a)[0], order(b)[0] + 1) if k not in numbers]
            if gaps:
                missing.add(f"{', '.join(gaps)} (of {a} through {b})")
        for n in single:
            if n in same:
                extra.discard(n)
            elif not any(n == h.rstrip("abcdefghijklmnopqrstuvwxyz") for h in same):
                missing.add(n)
            else:
                extra -= {h for h in same if h.rstrip("abcdefghijklmnopqrstuvwxyz") == n}
        if verb not in ADDITIVE:
            extra = set()
        if missing or extra:
            detail = f'"{verb.capitalize()}{clause[:120]}"'
            if missing:
                detail += f"; not an operand: {', '.join(sorted(missing))}"
            if extra:
                detail += f"; operand not named: {', '.join(sorted(extra))}"
            out.append({"kind": "operands", "line": lid, "subject": line_subject(line), "form": line["form"], "detail": detail,
                        "refuses": [r.get("when") for r in line.get("refuses", []) or []]})
    return out


def check_rulings(found):
    """A ruling that names a refusal must name one declared on the line."""
    data = json.loads(RULINGS.read_text()) if RULINGS.exists() else {}
    errors = []
    by_key = {baseline_check.key(f): f for f in found}
    for k, ruling in data.get("rulings", {}).items():
        gate = ruling.get("refusal") if isinstance(ruling, dict) else None
        if gate and k in by_key and gate not in by_key[k]["refuses"]:
            errors.append(f"  ruling {k} names refusal {gate}, which is not declared on the line")
    return errors


def check(rebaseline=False):
    forms = baseline_check.load_forms(CANONICAL)
    found = findings(forms)
    status = baseline_check.run(
        "operands", forms, found, RULINGS, REPORT, "Operand check",
        "Generated by `tools/check_operands.py` (T-085): computed lines whose printed arithmetic instruction names "
        "lines that are not its operands (or, for an addition, operands it does not name).", rebaseline)
    errors = check_rulings(found)
    for e in errors:
        print(e)
    return 1 if status or errors else 0


def self_test():
    assert named("Add lines 1 through 3") == (set(), {("1", "3")})
    assert named("Add lines 1z, 2b, 3b, 4b, 5b, 6b, 7a, and 8")[0] == {"1z", "2b", "3b", "4b", "5b", "6b", "7a", "8"}
    assert named("Subtract line 5 from line 4. If zero or less, enter -0-")[0] == {"5", "4"}
    assert named("Enter the smaller of line 3 or line 8 here and on Schedule 1, line 1")[0] == {"3", "8"}
    assert norm("(SMW 4)") == "4" and norm("6(a)") == "6" and norm("(CLW B 7)") == "7"
    assert VERB.match("Enter the smaller of line 3 or line 6").group(1) == "Enter the smaller of"
    print("operands self-test: ok")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    sys.exit(check(rebaseline="--baseline" in sys.argv))
