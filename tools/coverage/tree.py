#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""The coverage decision tree: every refusal gate as a yes/no question, with early exits.

A refusal gate is the `when` line of a `refuses` entry in the forms. Each gate is placed by hand in
tools/coverage/tree.json: an area, optionally a group within it, an order, a kind, and for a tax
situation a plain-language question. The first area is the trunk, which everyone answers; every other
area and every group has an entry question, and a no to it skips everything placed under it. The
placement must make that sound: a no to an entry question has to rule out a yes to each gate under it,
which is checked by hand against each gate's definition (the description in tree.json says so).
Everything else comes from the built data: the gate's own wording, the forms it refuses, the remedies
and the citations. Shares of returns come from reports/<year>/filer_coverage.json where the coverage
estimate measures a gate.

Writes docs/COVERAGE.md (the trunk chart, then each area's and group's chart with every gate, its
refusals and sources) and the trunk chart between the coverage-tree markers in README.md. Reads
canonical/<year>/, so the build must run first.

    tree.py            write both
    tree.py --check    fail if the placement does not match the forms, or either output is stale
    tree.py --self-test
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402

PLACEMENT = Path(__file__).with_name("tree.json")
CANONICAL = ROOT / "canonical" / Y
FILER_COVERAGE = ROOT / "reports" / Y / "filer_coverage.json"
PAGE = ROOT / "docs" / "COVERAGE.md"
README = ROOT / "README.md"
START = "<!-- coverage-tree:start -->"
END = "<!-- coverage-tree:end -->"
KINDS = ("situation", "entry")


def load_gates(canonical=CANONICAL):
    """Every gate in the built forms and definitions: its line and the refusals that use it, in file order."""
    lines, gates = {}, {}
    for path in sorted(canonical.glob("*.json")):
        data = json.loads(path.read_text())
        for kind in ("form", "def"):
            doc = data.get(kind)
            if not doc:
                continue
            for line in doc.get("lines", []):
                lines[line["id"]] = line
                for ref in line.get("refuses") or []:
                    gates.setdefault(ref["when"], []).append({"at": line["id"], **ref})
    return {g: {"line": lines.get(g), "refusals": refs} for g, refs in gates.items()}


def load_shares(path=FILER_COVERAGE):
    """Gate id -> [(category label, share)] from the coverage estimate, largest first; and the report itself."""
    if not path.exists():
        return {}, None
    report = json.loads(path.read_text())
    shares = {}
    for cat in report.get("categories", []):
        for gate in cat.get("gates", []):
            shares.setdefault(gate, []).append((cat["label"], cat["share"]))
    for v in shares.values():
        v.sort(key=lambda x: -x[1])
    return shares, report


def validate(gates, placement):
    """Problems with the placement: unplaced or vanished gates, duplicates, unknown areas, groups or kinds,
    missing questions, entry questions or stops."""
    errors = []
    areas = placement["areas"]
    ids = [a["id"] for a in areas]
    if len(set(ids)) != len(ids):
        errors.append("an area id is repeated in tree.json")
    if areas and areas[0].get("entry"):
        errors.append(f"{areas[0]['id']}: the first area is the trunk everyone answers; it has no entry question")
    groups = {}
    for a in areas[1:]:
        if not a.get("entry", "").strip():
            errors.append(f"{a['id']}: an area after the first needs an entry question")
    for a in areas:
        gids = [g["id"] for g in a.get("groups", [])]
        if len(set(gids)) != len(gids):
            errors.append(f"{a['id']}: a group id is repeated")
        for g in a.get("groups", []):
            if not g.get("entry", "").strip():
                errors.append(f"{a['id']}.{g['id']}: a group needs an entry question")
        groups[a["id"]] = set(gids)
    seen = set()
    for entry in placement["gates"]:
        g = entry.get("gate")
        if g in seen:
            errors.append(f"{g}: placed more than once")
        seen.add(g)
        if g not in gates:
            errors.append(f"{g}: placed in tree.json but no refusal in the forms uses it")
        if entry.get("area") not in groups:
            errors.append(f"{g}: unknown area {entry.get('area')!r}")
        elif entry.get("group") is not None and entry["group"] not in groups[entry["area"]]:
            errors.append(f"{g}: unknown group {entry['group']!r} in area {entry['area']!r}")
        if entry.get("kind") not in KINDS:
            errors.append(f"{g}: kind must be one of {', '.join(KINDS)}")
        if entry.get("kind") == "situation" and not entry.get("question", "").strip():
            errors.append(f"{g}: a situation needs a question")
        if entry.get("kind") == "situation" and g in gates and not entry.get("stop", "").strip():
            forms = {r.get("form") for r in gates[g]["refusals"]}
            if len(forms) > 1:
                errors.append(f"{g}: refuses under {len(forms)} form names, so it needs a 'stop' naming what the tree shows")
    for g in sorted(set(gates) - seen):
        errors.append(f"{g}: a refusal gate in the forms that tree.json does not place")
    return errors


def distinct(refusals):
    """Refusals with the same form, remedy and citation, once each, in order."""
    out, seen = [], set()
    for r in refusals:
        cite = r.get("cite") or {}
        key = (r.get("form"), r.get("remedy"), cite.get("doc"), cite.get("locator"))
        if key not in seen:
            seen.add(key)
            out.append(r)
    return out


def pct(share):
    return f"{share * 100:.1f}%"


def mm(text):
    """Text safe inside a quoted Mermaid label."""
    return text.replace('"', "#quot;").replace("<", "#lt;").replace(">", "#gt;")


def share_note(shares):
    """'2.6% of returns', or for a gate the estimate splits into several situations, the largest and a count."""
    if not shares:
        return ""
    label, top = shares[0]
    if len(shares) == 1:
        return f"{pct(top)} of returns"
    return f"{pct(top)} of returns ({label.lower()}), plus {len(shares) - 1} more measured situations"


def share_list(shares):
    return "; ".join(f"{label}, {pct(s)}" for label, s in shares)


def stop_text(entry, gates):
    """What the tree names when a gate fires: the placement's 'stop', else the one form its refusals name."""
    if entry.get("stop"):
        return entry["stop"]
    return gates[entry["gate"]]["refusals"][0]["form"]


def gate_row(e, gates, shares):
    """A gate as a chart row: its question, with a yes leading to the refusal."""
    stop = "Not covered: " + mm(stop_text(e, gates))
    note = share_note(shares.get(e["gate"], []))
    if note:
        stop += "<br/>" + mm(note)
    return {"question": e["question"], "side": "Yes", "down": "No", "box": stop, "cls": "stop"}


def chart(start, rows, end):
    """A Mermaid flowchart of rows top to bottom. Each row is a question with one answer leading out to the
    side (a refusal, a skip or a pointer to another chart) and the other answer leading down to the next
    row. Rows are borderless left-to-right subgraphs, so the chart grows downward however long it is."""
    out = ["```mermaid", "flowchart TD", f'  start(["{mm(start)}"])']
    classes, prev, prev_down = {"stop": [], "go": ["done"], "jump": []}, "start", None
    for i, r in enumerate(rows):
        out += [f'  subgraph s{i}[" "]', "    direction LR",
                f'    q{i}["{mm(r["question"])}"] -->|{r["side"]}| r{i}["{r["box"]}"]', "  end",
                f"  style s{i} fill:none,stroke:none"]
        out.append(f"  {prev} -->{f'|{prev_down}|' if prev_down else ''} s{i}")
        classes[r["cls"]].append(f"r{i}")
        prev, prev_down = f"s{i}", r["down"]
    out.append(f'  {prev} -->{f"|{prev_down}|" if prev_down else ""} done(["{mm(end)}"])')
    out.append("  classDef stop fill:#fde2e2,stroke:#c0392b,color:#000")
    out.append("  classDef go fill:#e2f5e9,stroke:#27ae60,color:#000")
    out.append("  classDef jump fill:#e3ecfa,stroke:#2e64b5,color:#000")
    for cls, nodes in classes.items():
        if nodes:
            out.append(f"  class {','.join(nodes)} {cls}")
    out.append("```")
    return "\n".join(out)


def situations(placement, area, group=None):
    return [e for e in placement["gates"] if e["area"] == area and e.get("group") == group and e["kind"] == "situation"]


def trunk_chart(placement, gates, shares, where):
    """The main chart: the trunk's gates, then one entry question per area pointing to that area's chart."""
    areas = placement["areas"]
    rows = [gate_row(e, gates, shares) for e in situations(placement, areas[0]["id"])]
    for a in areas[1:]:
        rows.append({"question": a["entry"], "side": "Yes", "down": "No",
                     "box": mm(f"See {a['title']}{where}"), "cls": "jump"})
    return chart(areas[0]["title"], rows, "No to all: none of the tree's refusals applies")


def gate_entry(e, gates, shares):
    g = e["gate"]
    line = gates[g]["line"] or {}
    refs = distinct(gates[g]["refusals"])
    head = f"**`{g}`**" + (f": {e['question']}" if e.get("question") else "")
    out = [f"- {head}", f"  - *The data asks or tests:* {line.get('label', '')} (`{line.get('expr', {}).get('op')}`)"]
    if e.get("stop"):
        out.append(f"  - *The tree names:* {e['stop']}")
    for r in refs:
        out.append(f"  - *Not covered:* {r.get('form')}. {r.get('remedy', '')}")
        out.append(f"    *Source:* [{(r.get('cite') or {}).get('doc')}] {(r.get('cite') or {}).get('locator')}")
    at = list(dict.fromkeys(r["at"] for r in gates[g]["refusals"]))
    out.append("  - *Refused at:* " + ", ".join(f"`{a}`" for a in at))
    if shares.get(g):
        out.append("  - *Share of returns (coverage estimate):* " + share_list(shares[g]))
    return "\n".join(out)


def anchor(title):
    keep = "".join(c for c in title.lower() if c.isalnum() or c in " -")
    return keep.replace(" ", "-")


def render(gates, placement, shares, report):
    areas = placement["areas"]
    trunk = areas[0]
    n_sit = sum(1 for e in placement["gates"] if e["kind"] == "situation")
    n_ent = sum(1 for e in placement["gates"] if e["kind"] == "entry")
    n_groups = sum(len(a.get("groups", [])) for a in areas)
    est = ""
    if report:
        est = (f" Shares of returns come from the coverage estimate (`reports/{Y}/filer_coverage.json`, an estimate "
               f"of {pct(report['coverage']['central'])} of returns), which measures {len(shares)} of the gates; the "
               "rest have no IRS count to measure them by.")
    page = [
        "# Coverage decision tree",
        "",
        f"Generated by `tools/coverage/tree.py` from the tax year {Y} form data and the placement in "
        "`tools/coverage/tree.json`; do not edit by hand. `check-all` fails when a refusal gate is missing "
        "from the tree, when the tree names a gate the forms no longer have, or when this page is out of date.",
        "",
        "Every situation the tool refuses is here, as a yes/no question. Start with the main chart. Its first "
        "questions apply to everyone: a **yes** to any of them means the tool cannot prepare your return. "
        "Then come one question per area of the return; a **no** skips the whole area, and a **yes** sends you "
        "to that area's chart below, where larger areas split again into groups with questions of their own. "
        "If you answer **no** throughout, none of the tool's refusals should apply to you. The questions here "
        "are summaries, though, and some gates test figures you enter later: the interview asks the full "
        "questions and, if a refusal does apply, stops and cites the instruction behind it.",
        "",
        "The entry questions that let you skip an area or group are placed by hand. Each is worded so that a "
        "**no** rules out a yes to every gate beneath it, checked against each gate's definition; gates no "
        "entry question can rule out, some of which refuse a return whenever their answer is yes, are asked "
        "of everyone in the main chart.",
        "",
        f"The data holds **{len(gates)} refusal gates**: {n_sit} tax situations the tool does not prepare, in "
        f"{len(areas)} areas and {n_groups} groups, and {n_ent} entry checks, refusals that fire when the figures "
        "entered contradict each other or an entry cannot stand under the instructions as given. Entry checks "
        "are not limits on coverage; they are listed at the end." + est,
        "",
        "Under each chart, every gate is listed with the wording the data itself uses, each form it refuses, "
        "the remedy the tool prints, and the archived IRS source.",
        "",
        "## Contents",
        "",
        f"- [Main chart: {trunk['title']}](#main-chart) ({len(situations(placement, trunk['id']))})",
    ]
    for a in areas[1:]:
        n = sum(1 for e in placement["gates"] if e["area"] == a["id"] and e["kind"] == "situation")
        page.append(f"- [{a['title']}](#{anchor(a['title'])}) ({n})")
    page += [f"- [Entry checks](#entry-checks) ({n_ent})", "",
             "## Main chart", "", trunk["intro"], "",
             trunk_chart(placement, gates, shares, " below"), ""]
    page += [gate_entry(e, gates, shares) for e in situations(placement, trunk["id"])]
    page.append("")
    for a in areas[1:]:
        page += [f"## {a['title']}", "", a["intro"], "",
                 f"You are here because you answered yes to: *{a['entry']}*", ""]
        groups = a.get("groups", [])
        loose = situations(placement, a["id"])
        if loose:
            end = "No to all: this area is clear" if not groups else "No to all: continue with the groups below"
            rows = [gate_row(e, gates, shares) for e in loose]
            page += [chart(a["title"], rows, end), ""] + [gate_entry(e, gates, shares) for e in loose] + [""]
        for i, g in enumerate(groups):
            members = situations(placement, a["id"], g["id"])
            nxt = groups[i + 1]["title"] if i + 1 < len(groups) else None
            skip = f"No: skip to {nxt}" if nxt else "No: this area is clear"
            rows = [{"question": g["entry"], "side": "No", "down": "Yes", "box": mm(skip), "cls": "go"}]
            rows += [gate_row(e, gates, shares) for e in members]
            page += [f"### {g['title']}", "", chart(g["title"], rows, "No to all: this group is clear"), ""]
            page += [gate_entry(e, gates, shares) for e in members] + [""]
    page += ["## Entry checks", "",
             "These refuse a return when entered figures contradict each other, or when an entry cannot stand "
             "under the instructions as given. Correcting the entry, as each remedy says, clears the refusal.", ""]
    for a in areas:
        ents = [e for e in placement["gates"] if e["area"] == a["id"] and e["kind"] == "entry"]
        if ents:
            page += [f"### {a['title']}", ""] + [gate_entry(e, gates, shares) for e in ents] + [""]
    return "\n".join(page).rstrip() + "\n"


def readme_block(gates, placement, shares):
    areas = placement["areas"]
    n_sit = sum(1 for e in placement["gates"] if e["kind"] == "situation")
    body = [
        START,
        "<!-- Generated by tools/coverage/tree.py; do not edit between these markers. -->",
        "",
        "Start here to see whether the tool covers your return. The first questions apply to everyone: a "
        "**yes** to any of them means the tool cannot prepare your return. The rest ask about one area of "
        "the return each; a **no** skips that area, and a **yes** sends you to its chart.",
        "",
        trunk_chart(placement, gates, shares, " in docs/COVERAGE.md"),
        "",
        f"[`docs/COVERAGE.md`](docs/COVERAGE.md) has every area's chart, covering all {n_sit} situations the "
        f"tool refuses out of {len(gates)} refusal gates in the data, each with the form it names and the "
        "archived IRS source.",
        END,
    ]
    return "\n".join(body)


def splice(readme_text, block):
    s, e = readme_text.find(START), readme_text.find(END)
    if s < 0 or e < s:
        raise SystemExit(f"README.md: the {START} and {END} markers are missing")
    return readme_text[:s] + block + readme_text[e + len(END):]


def main(argv):
    if "--self-test" in argv:
        return self_test()
    gates = load_gates()
    if not gates:
        raise SystemExit(f"no refusal gates under {CANONICAL.relative_to(ROOT)}; run the build first")
    placement = json.loads(PLACEMENT.read_text())
    shares, report = load_shares()
    errors = validate(gates, placement)
    if errors:
        print("coverage tree: tools/coverage/tree.json does not match the forms:", file=sys.stderr)
        for e in errors:
            print("  " + e, file=sys.stderr)
        return 1
    page = render(gates, placement, shares, report)
    readme = splice(README.read_text(), readme_block(gates, placement, shares))
    if "--check" in argv:
        stale = [p.relative_to(ROOT).as_posix() for p, text in ((PAGE, page), (README, readme))
                 if not p.exists() or p.read_text() != text]
        if stale:
            print(f"coverage tree: out of date: {', '.join(stale)}; run python3 tools/coverage/tree.py", file=sys.stderr)
            return 1
        print(f"coverage tree: {len(gates)} gates placed, docs/COVERAGE.md and README.md current")
        return 0
    PAGE.write_text(page)
    README.write_text(readme)
    print(f"coverage tree: wrote docs/COVERAGE.md and the README block ({len(gates)} gates)")
    return 0


def self_test():
    """Plant each kind of mismatch and check that validate() reports it; check charts, shares and splice()."""
    gates = {"a.one": {"line": {"label": "One", "expr": {"op": "input"}}, "refusals": [
                {"at": "a.x", "form": "Form A", "remedy": "Do A.", "cite": {"doc": "d", "locator": "p. 1"}}]},
             "a.two": {"line": {"label": "Two", "expr": {"op": "test"}}, "refusals": [
                {"at": "a.y", "form": "Form B", "remedy": "Do B.", "cite": {"doc": "d", "locator": "p. 2"}}]},
             "b.one": {"line": {"label": "Three", "expr": {"op": "input"}}, "refusals": [
                {"at": "b.x", "form": "Form D", "remedy": "Do D.", "cite": {"doc": "d", "locator": "p. 4"}}]}}
    base = {"areas": [{"id": "t", "title": "T", "intro": "i"},
                      {"id": "x", "title": "X", "intro": "i", "entry": "X?",
                       "groups": [{"id": "g", "title": "G", "entry": "G?"}]}],
            "gates": [{"gate": "a.one", "area": "t", "kind": "situation", "question": "One?"},
                      {"gate": "a.two", "area": "x", "kind": "entry"},
                      {"gate": "b.one", "area": "x", "group": "g", "kind": "situation", "question": "Three?"}]}
    assert validate(gates, base) == [], validate(gates, base)
    sit, ent, grp = base["gates"]
    cases = {
        "does not place": {**base, "gates": [sit, ent]},
        "no refusal in the forms uses it": {**base, "gates": base["gates"] + [{"gate": "a.gone", "area": "t", "kind": "entry"}]},
        "placed more than once": {**base, "gates": base["gates"] + [ent]},
        "unknown area": {**base, "gates": [{**sit, "area": "y"}, ent, grp]},
        "unknown group": {**base, "gates": [sit, ent, {**grp, "group": "h"}]},
        "kind must be": {**base, "gates": [{**sit, "kind": "other"}, ent, grp]},
        "needs a question": {**base, "gates": [{**sit, "question": " "}, ent, grp]},
        "first area is the trunk": {**base, "areas": [{**base["areas"][0], "entry": "T?"}, base["areas"][1]]},
        "needs an entry question": {**base, "areas": [base["areas"][0], {**base["areas"][1], "entry": ""}]},
        "a group needs an entry": {**base, "areas": [base["areas"][0], {**base["areas"][1], "groups": [{"id": "g", "title": "G"}]}]},
    }
    for want, placement in cases.items():
        errors = validate(gates, placement)
        assert any(want in e for e in errors), (want, errors)
    two_forms = {**gates, "a.one": {**gates["a.one"], "refusals": gates["a.one"]["refusals"] + [
        {"at": "a.z", "form": "Form C", "remedy": "Do C.", "cite": {"doc": "d", "locator": "p. 3"}}]}}
    assert any("needs a 'stop'" in e for e in validate(two_forms, base)), validate(two_forms, base)
    assert validate(two_forms, {**base, "gates": [{**sit, "stop": "Form A or C"}, ent, grp]}) == []
    text = trunk_chart(base, gates, {"a.one": [("Cat", 0.05)]}, " below")
    assert 'q0["One?"] -->|Yes| r0["Not covered: Form A<br/>5.0% of returns"]' in text, text
    assert 'q1["X?"] -->|Yes| r1["See X below"]' in text and "s0 -->|No| s1" in text and "class r1 jump" in text, text
    page = render(gates, base, {}, None)
    assert 'q0["G?"] -->|No| r0["No: this area is clear"]' in page and "s0 -->|Yes| s1" in page, page
    assert share_note([("Big", 0.05), ("Small", 0.01)]) == "5.0% of returns (big), plus 1 more measured situations"
    assert mm('say "hi" <b>') == "say #quot;hi#quot; #lt;b#gt;"
    assert splice(f"a {START} old {END} b", "NEW") == "a NEW b"
    try:
        splice("no markers", "NEW")
        raise AssertionError("splice accepted a README without markers")
    except SystemExit:
        pass
    print("coverage tree self-test: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
