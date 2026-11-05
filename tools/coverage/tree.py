#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""The coverage table and the reference of every refusal gate.

A refusal gate is the `when` line of a `refuses` entry in the forms. tools/coverage/tree.json holds two
things. Its `table` is the README's coverage table: one row per theme of a return, what the tool handles
there, and the situations it refuses, each standing for coverage-estimate categories (reports/<year>/
filer_coverage.json, with their share of returns) or for gates the estimate does not measure. A reader
makes one decision: does anything in the refused column apply to me. The table is meant to be nearly
right for nearly everyone, not exhaustive: every refused category the estimate measures at the
`threshold` share of returns or more must appear in it, and the rest is left to the interview, which asks
every gate and refuses with a citation. Its `gates` place every gate in a topic for docs/COVERAGE.md, the
reference that lists each one with its wording, refusals and sources.

    tree.py            write the README table and docs/COVERAGE.md
    tree.py --check    fail if the placement or table does not match the forms and the estimate, or either output is stale
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
    # The federal tree: the New York documents (ny_*.json, built beside the federal ones) have no place in it.
    for path in sorted(p for p in canonical.glob("*.json") if not p.name.startswith("ny_")):
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


def load_report(path=FILER_COVERAGE):
    """The coverage estimate's refused categories by id (label, share, gates), and the report itself."""
    if not path.exists():
        return {}, None
    report = json.loads(path.read_text())
    return {c["id"]: c for c in report.get("categories", [])}, report


def validate(gates, placement, categories):
    """Problems: unplaced, vanished or repeated gates; unknown topics, parts or kinds; situations without a
    question; gates refusing under several form names without a stop; table items naming unknown gates or
    categories, or naming nothing; measured categories at or over the threshold missing from the table."""
    errors = []
    topics = placement["topics"]
    seen = set()
    for entry in placement["gates"]:
        g = entry.get("gate")
        if g in seen:
            errors.append(f"{g}: placed more than once")
        seen.add(g)
        if g not in gates:
            errors.append(f"{g}: placed in tree.json but no refusal in the forms uses it")
        t = topics.get(entry.get("topic"))
        if t is None:
            errors.append(f"{g}: unknown topic {entry.get('topic')!r}")
        else:
            parts = {p["id"] for p in t.get("parts", [])}
            if parts and entry.get("part") not in parts:
                errors.append(f"{g}: topic {entry['topic']!r} has parts; part {entry.get('part')!r} is not one")
            if not parts and entry.get("part") is not None:
                errors.append(f"{g}: topic {entry['topic']!r} has no parts")
        if entry.get("kind") not in KINDS:
            errors.append(f"{g}: kind must be one of {', '.join(KINDS)}")
        if entry.get("kind") == "situation":
            if not entry.get("question", "").strip():
                errors.append(f"{g}: a situation needs a question")
            if g in gates and not entry.get("stop", "").strip():
                forms = {r.get("form") for r in gates[g]["refusals"]}
                if len(forms) > 1:
                    errors.append(f"{g}: refuses under {len(forms)} form names, so it needs a 'stop'")
    for g in sorted(set(gates) - seen):
        errors.append(f"{g}: a refusal gate in the forms that tree.json does not place")
    in_table = set()
    for row in placement["table"]:
        for item in row.get("refused", []):
            if not item.get("categories") and not item.get("gates"):
                errors.append(f"table, {row['theme']}: '{item['label']}' names no category or gate")
            for c in item.get("categories", []):
                in_table.add(c)
                if c not in categories:
                    errors.append(f"table, {row['theme']}: unknown coverage category {c!r}")
            for g in item.get("gates", []):
                if g not in gates:
                    errors.append(f"table, {row['theme']}: unknown gate {g!r}")
    threshold = placement["threshold"]
    for c, cat in categories.items():
        if cat["share"] >= threshold and c not in in_table:
            errors.append(f"coverage category {c!r} ({pct(cat['share'])} of returns) is at or over the threshold "
                          f"({pct(threshold)}) but not in the table")
    return errors


def pct(share):
    return f"{share * 100:.1f}%"


def item_share(item, categories):
    shares = [categories[c]["share"] for c in item.get("categories", []) if c in categories]
    if not shares:
        return "not measured"
    total = pct(sum(shares))
    if item.get("upper_bound"):
        return f"up to {total} of returns"
    return f"{'about ' if len(shares) > 1 else ''}{total} of returns"


def table(placement, categories):
    out = ["| | The tool handles | The tool can't handle |", "|---|---|---|"]
    for row in placement["table"]:
        refused = "<br>".join(f"✗ {i['label']}: {item_share(i, categories)}" for i in row.get("refused", [])) or "—"
        out.append(f"| **{row['theme']}** | ✓ {row['covered']} | {refused} |")
    return "\n".join(out)


def residual(placement, categories, gates):
    """What the table leaves to the interview: measured categories it does not name, and the count of
    situation gates no table item names."""
    named_cats = {c for r in placement["table"] for i in r.get("refused", []) for c in i.get("categories", [])}
    named_gates = {g for r in placement["table"] for i in r.get("refused", []) for g in i.get("gates", [])}
    named_gates |= {g for c in named_cats for g in categories.get(c, {}).get("gates", [])}
    cats = sorted((c for c in categories if c not in named_cats), key=lambda c: -categories[c]["share"])
    rest = [e for e in placement["gates"] if e["kind"] == "situation" and e["gate"] not in named_gates]
    return cats, rest


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


def gate_entry(e, gates, categories):
    g = e["gate"]
    line = gates[g]["line"] or {}
    head = f"**`{g}`**" + (f": {e['question']}" if e.get("question") else "")
    out = [f"- {head}", f"  - *The data asks or tests:* {line.get('label', '')} (`{line.get('expr', {}).get('op')}`)"]
    if e.get("stop"):
        out.append(f"  - *Stops the return as:* {e['stop']}")
    for r in distinct(gates[g]["refusals"]):
        cite = r.get("cite") or {}
        out.append(f"  - *Not covered:* {r.get('form')}. {r.get('remedy', '')}")
        out.append(f"    *Source:* [{cite.get('doc')}] {cite.get('locator')}")
    at = list(dict.fromkeys(r["at"] for r in gates[g]["refusals"]))
    out.append("  - *Refused at:* " + ", ".join(f"`{a}`" for a in at))
    measured = [c for c in categories.values() if g in c.get("gates", [])]
    if measured:
        out.append("  - *Share of returns (coverage estimate):* "
                   + "; ".join(f"{c['label']}, {pct(c['share'])}" for c in sorted(measured, key=lambda c: -c["share"])))
    return "\n".join(out)


def anchor(title):
    keep = "".join(c for c in title.lower() if c.isalnum() or c in " -")
    return keep.replace(" ", "-")


def render(gates, placement, categories, report):
    n_sit = sum(1 for e in placement["gates"] if e["kind"] == "situation")
    n_ent = sum(1 for e in placement["gates"] if e["kind"] == "entry")
    cats, rest = residual(placement, categories, gates)
    threshold = pct(placement["threshold"])
    page = [
        "# Coverage reference",
        "",
        f"Generated by `tools/coverage/tree.py` from the tax year {Y} form data, the coverage estimate and "
        "`tools/coverage/tree.json`; do not edit by hand. `check-all` fails when a refusal gate is missing here, "
        "when a gate listed here is gone from the forms, or when this page or the README table is out of date.",
        "",
        "Start with the coverage table in the [README](../README.md#where-the-scope-runs-out): if nothing in its "
        "right-hand column applies to you, the tool should be able to prepare your return. This page is the "
        "reference behind that table: every situation the tool refuses, with the wording the data uses, the "
        "forms it names, the remedy the tool prints and the archived IRS source.",
        "",
        "## What the table leaves to the interview",
        "",
        f"The table is built to be nearly right for nearly everyone in one look, not to list everything. Every "
        f"refused situation the coverage estimate measures at {threshold} of returns or more is in it (the "
        "check enforces that), along with a few situations the estimate cannot measure but that are common enough "
        "to name. Everything else is left to the interview, which asks about every situation below and, if one "
        "applies, stops and cites the instruction behind it.",
        "",
    ]
    if cats:
        page += [f"Measured, below {threshold} of returns, and not in the table:", ""]
        page += [f"- {categories[c]['label']}: {pct(categories[c]['share'])}" for c in cats] + [""]
    page += [f"Not named in the table: {len(rest)} of the {n_sit} situations the tool refuses. Most are rare, "
             "and most are not measured; the coverage estimate has an IRS count for only a handful of situations, "
             "so the table's choice of unmeasured ones is a judgment.", ""]
    if report:
        page += [f"The estimate puts coverage at {pct(report['coverage']['central'])} of returns "
                 f"(`reports/{Y}/filer_coverage.json`). It does not count the unmeasured situations, so the true "
                 "figure is lower.", ""]
    page += [
        f"## Every refusal",
        "",
        f"The data holds **{len(gates)} refusal gates**: {n_sit} tax situations the tool does not prepare, "
        f"grouped by topic below, and {n_ent} entry checks, refusals that fire when the figures entered "
        "contradict each other or an entry cannot stand under the instructions as given. Entry checks are not "
        "limits on coverage; they are listed at the end.",
        "",
    ]
    for tid, t in placement["topics"].items():
        sits = [e for e in placement["gates"] if e["topic"] == tid and e["kind"] == "situation"]
        if sits:
            page.append(f"- [{t['title']}](#{anchor(t['title'])}) ({len(sits)})")
    page += [f"- [Entry checks](#entry-checks) ({n_ent})", ""]
    for tid, t in placement["topics"].items():
        sits = [e for e in placement["gates"] if e["topic"] == tid and e["kind"] == "situation"]
        if not sits:
            continue
        page += [f"### {t['title']}", ""]
        for p in t.get("parts") or [None]:
            items = [e for e in sits if e.get("part") == (p["id"] if p else None)]
            if p:
                page += [f"*{p['title']}*", ""]
            page += [gate_entry(e, gates, categories) for e in items] + [""]
    page += ["## Entry checks", "",
             "These refuse a return when entered figures contradict each other, or when an entry cannot stand "
             "under the instructions as given. Correcting the entry, as each remedy says, clears the refusal.", ""]
    for tid, t in placement["topics"].items():
        ents = [e for e in placement["gates"] if e["topic"] == tid and e["kind"] == "entry"]
        if ents:
            page += [f"#### {t['title']}", ""] + [gate_entry(e, gates, categories) for e in ents] + [""]
    return "\n".join(page).rstrip() + "\n"


def readme_block(gates, placement, categories):
    n_sit = sum(1 for e in placement["gates"] if e["kind"] == "situation")
    return "\n".join([
        START,
        "<!-- Generated by tools/coverage/tree.py; do not edit between these markers. -->",
        "",
        "**If anything in the right-hand column applies to you, the tool cannot prepare your return.** "
        "Otherwise it should be able to. Shares are of all individual returns, from the coverage estimate.",
        "",
        table(placement, categories),
        "",
        "Rare exceptions within the left-hand column are left to the interview, which stops with a citation if "
        f"one applies. [`docs/COVERAGE.md`](docs/COVERAGE.md) lists all {n_sit} situations the tool refuses, "
        "and says exactly what this table leaves out.",
        END,
    ])


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
    categories, report = load_report()
    errors = validate(gates, placement, categories)
    if errors:
        print("coverage tree: tools/coverage/tree.json does not match the forms or the estimate:", file=sys.stderr)
        for e in errors:
            print("  " + e, file=sys.stderr)
        return 1
    page = render(gates, placement, categories, report)
    readme = splice(README.read_text(), readme_block(gates, placement, categories))
    if "--check" in argv:
        stale = [p.relative_to(ROOT).as_posix() for p, text in ((PAGE, page), (README, readme))
                 if not p.exists() or p.read_text() != text]
        if stale:
            print(f"coverage tree: out of date: {', '.join(stale)}; run python3 tools/coverage/tree.py", file=sys.stderr)
            return 1
        print(f"coverage tree: {len(gates)} gates placed, docs/COVERAGE.md and the README table current")
        return 0
    PAGE.write_text(page)
    README.write_text(readme)
    print(f"coverage tree: wrote docs/COVERAGE.md and the README table ({len(gates)} gates)")
    return 0


def self_test():
    """Plant each kind of mismatch and check that validate() reports it; check the table, residual and splice()."""
    def gate(label, form):
        return {"line": {"label": label, "expr": {"op": "input"}}, "refusals": [
            {"at": "x." + label, "form": form, "remedy": "Do it.", "cite": {"doc": "d", "locator": "p. 1"}}]}
    gates = {"a.one": gate("one", "Form A"), "a.two": gate("two", "Form B"), "b.one": gate("three", "Form D")}
    categories = {"big": {"label": "Big", "share": 0.05, "gates": ["a.one"]},
                  "small": {"label": "Small", "share": 0.001, "gates": ["a.one"]}}
    base = {"threshold": 0.005,
            "table": [{"theme": "T", "covered": "Wages", "refused": [
                {"label": "Big thing", "categories": ["big"]}, {"label": "Unmeasured", "gates": ["b.one"]}]}],
            "topics": {"t": {"title": "Topic", "parts": [{"id": "p", "title": "P"}]}, "u": {"title": "U"}},
            "gates": [{"gate": "a.one", "topic": "t", "part": "p", "kind": "situation", "question": "One?"},
                      {"gate": "a.two", "topic": "u", "kind": "entry"},
                      {"gate": "b.one", "topic": "u", "kind": "situation", "question": "Three?"}]}
    assert validate(gates, base, categories) == [], validate(gates, base, categories)
    one, two, three = base["gates"]
    row = base["table"][0]
    cases = {
        "does not place": {**base, "gates": [one, three]},
        "no refusal in the forms uses it": {**base, "gates": base["gates"] + [{"gate": "a.gone", "topic": "u", "kind": "entry"}]},
        "placed more than once": {**base, "gates": base["gates"] + [two]},
        "unknown topic": {**base, "gates": [{**one, "topic": "zz"}, two, three]},
        "is not one": {**base, "gates": [{**one, "part": "q"}, two, three]},
        "has no parts": {**base, "gates": [one, two, {**three, "part": "p"}]},
        "kind must be": {**base, "gates": [{**one, "kind": "other"}, two, three]},
        "needs a question": {**base, "gates": [{**one, "question": " "}, two, three]},
        "names no category or gate": {**base, "table": [{**row, "refused": row["refused"] + [{"label": "Empty"}]}]},
        "unknown coverage category": {**base, "table": [{**row, "refused": row["refused"] + [{"label": "X", "categories": ["nope"]}]}]},
        "unknown gate": {**base, "table": [{**row, "refused": row["refused"] + [{"label": "X", "gates": ["no.gate"]}]}]},
        "at or over the threshold": {**base, "table": [{**row, "refused": row["refused"][1:]}]},
    }
    for want, placement in cases.items():
        errors = validate(gates, placement, categories)
        assert any(want in e for e in errors), (want, errors)
    two_forms = {**gates, "a.one": {**gates["a.one"], "refusals": gates["a.one"]["refusals"] + [
        {"at": "a.z", "form": "Form C", "remedy": "Do C.", "cite": {"doc": "d", "locator": "p. 3"}}]}}
    assert any("needs a 'stop'" in e for e in validate(two_forms, base, categories))
    text = table(base, categories)
    assert "| **T** | ✓ Wages | ✗ Big thing: 5.0% of returns<br>✗ Unmeasured: not measured |" in text, text
    assert item_share({"categories": ["big", "small"]}, categories) == "about 5.1% of returns"
    assert item_share({"categories": ["big"], "upper_bound": "why"}, categories) == "up to 5.0% of returns"
    cats, rest = residual(base, categories, gates)
    assert cats == ["small"] and rest == [], (cats, rest)
    page = render(gates, base, categories, None)
    assert "- Small: 0.1%" in page and "**`b.one`**: Three?" in page and "#### U" in page, page
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
