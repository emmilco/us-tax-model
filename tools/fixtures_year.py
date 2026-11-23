#!/usr/bin/env python3
"""Carry the fixtures into a new year (spec 6.7), once the new year's definitions build.

    fixtures_year.py --from 2025 --to 2026 [--no-hand-work]

Copies fixtures/<from>/ to fixtures/<to>/ (refusing to overwrite) and re-derives it:

  - inputs: a parameter-relative input (engine/src/fixture-inputs.ts) follows its
    parameter by itself; an input that is a year (the keys in YEAR_KEYS: "placed"
    as "y2025", "placed_date" as 2025) moves with the year;
  - an official IRS example (evidence class A) is dropped: it proves nothing about
    another year; the report lists them, to find the new year's;
  - every other case is evaluated on the new year's data and its expected values
    re-recorded. A case keeps its evidence when no expected value changed and nothing
    a value rests on (the lines and parameters of its derivation) is on the year-diff
    worklist (tools/year_diff.py, the new year's citations against both years' text);
    otherwise it becomes "re-recorded for <to>", its earlier evidence and the reason
    kept in the note. Refusals are compared by gate and form (their citation names
    the new year's archive). The Lean evaluator and the engine differential in
    check-all then cover every re-recorded value;
  - a case whose inputs the new year's data rejects (a year value its definitions do
    not list yet) is marked "not evaluated" and listed;
  - class M hand-work (tools/transcription/classm.py, paid model calls) runs for the
    documents with a line on the worklist, unless --no-hand-work;
  - the test-data defaults (defaults.json) follow the year's operations (changes/<to>/,
    tools/year_changes.py): each new input takes the default and reason its add_question
    states, placed after the default of the question it is placed after; the default of an
    input the operations remove (remove_line, remove_question) is dropped. A case's answer to
    a removed input that equals the input's unconditional from-year default says what the
    default said and is dropped with it; a case that still states a removed input otherwise
    is marked "not evaluated" and listed (the engine's fixture loader leaves such a case out,
    and test-fixtures fails while any remain). An expectation on a removed line is dropped and
    listed. The cases resolve against the carried defaults.

Writes reports/<to>/fixtures_from_<from>.md.

    fixtures_year.py --self-test     (in check-all) parameter-relative inputs resolve, and
                                      one naming no dollar parameter is refused, as the engine does

    fixtures_year.py --from 2025 --to 2026 --plan

writes the same report without carrying anything, for a year whose definitions do
not build yet (a rehearsal on draft documents, where some cited documents have no
edition): each case is evaluated on the from-year's data and listed as re-recorded
when its derivation rests on the to-year's worklist; whether a value changes is not
known until the to-year builds, so a case listed as kept may still be re-recorded.
fixtures/<to>/ is not written.
"""

import argparse
import collections
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import year_diff  # noqa: E402
import jurisdiction  # noqa: E402  (--jurisdiction ny, docs/ny/DECISIONS.md C1, C8)
from jurisdiction import ypath  # noqa: E402
from fixture_inputs import resolve_cases  # noqa: E402

YEAR_KEYS = ("placed", "placed_date")
NODE = ["node", str(ROOT / "engine" / "dist" / "main.js")]


def defaults_files(year):
    """The year's defaults files, federal first (fixture-inputs.ts): the New York fixtures take both."""
    fed = ROOT / "fixtures" / str(year) / "defaults.json"
    ny = ROOT / "fixtures" / "ny" / str(year) / "defaults.json"
    return [p for p in ([fed, ny] if jurisdiction.J == "ny" else [fed]) if p.exists()]


def canonical_params(year):
    """The canonical parameter values of a year: params.json, with the New York ones (params-ny.json,
    decision C1) merged in when the build wrote them."""
    d = ROOT / "canonical" / str(year)
    values = json.loads((d / "params.json").read_text())["params"]["values"]
    if (d / "params-ny.json").exists():
        values = {**values, **json.loads((d / "params-ny.json").read_text())["params"]["values"]}
    return values


def template(key):
    """A line id from an instance key: "person[taxpayer].w2[a].box1" -> "w2.box1"."""
    parts = key.split(".")
    if len(parts) > 2 and "[" in key:
        return parts[-2].split("[")[0] + "." + parts[-1]
    return re.sub(r"\[[^\]]*\]", "", key)


def shift_year(key, value, shift):
    if key.split(".")[-1] not in YEAR_KEYS:
        return value
    if isinstance(value, int) and not isinstance(value, bool):
        return value + shift
    m = re.fullmatch(r"y(\d{4})", value) if isinstance(value, str) else None
    return f"y{int(m.group(1)) + shift}" if m else value


def self_test():
    """Parameter-relative inputs resolve through the engine (fixture_inputs.resolve_cases, the resolver this tool
    uses), and one naming no dollar amount is refused. A class M file name keeps the defaults out."""
    import taxyear
    year = taxyear.YEAR
    base = canonical_params(year)["medicare.threshold"]["value"]["mfj"]
    case = lambda inputs: [{"id": "t", "file": "classm.json", "inputs": inputs}]
    good = resolve_cases(case({"x": {"param": "medicare.threshold", "status": "mfj", "offset": -1}, "z": 7}), year)
    ok = good == {"t": {"x": base - 1, "z": 7}}
    refused = []
    for bad in ({"param": "a.missing", "offset": 0}, {"param": "medicare.threshold", "offset": 0},
                {"param": "medicare.threshold", "status": "xyz", "offset": 0},
                {"param": "medicare.threshold", "status": "mfj", "offset": 0.5}):
        try:
            resolve_cases(case({"k": bad}), year)
            refused.append(False)
        except ValueError as e:
            refused.append("input k refers to " in str(e) and "not a dollar amount" in str(e))
    print("fixtures-year self-test: parameter-relative inputs " + ("resolve, and those naming no dollar amount are refused"
          if ok and all(refused) else f"WRONG (resolved {good}; refused {refused})"))
    # The defaults follow the operations: a new input's default after its anchor's, a removed input's dropped.
    import year_changes
    Op = year_changes.Op
    ops = [Op("x", "C", 1, "add_question", {"input": "f.new", "like": "f.a", "default": 0, "reason": "r"}, {}),
           Op("x", "C", 2, "add_question", {"input": "f.newer", "after": "f.new", "default": False, "reason": "s"}, {}),
           Op("x", "C", 3, "add_question", {"input": "f.nodefault", "after": "f.a"}, {}),
           Op("x", "C", 4, "remove_question", {"input": "f.b"}, {}),
           Op("x", "C", 5, "remove_line", {"line": "f.c"}, {})]
    d = {"defaults": [{"input": i, "value": 0, "reason": "x"} for i in ("f.a", "f.b", "f.c", "f.d")]}
    added, dropped, _ = carry_defaults(d, ops)
    got = [(x["input"], x["value"], x["reason"]) for x in d["defaults"]]
    ok2 = (got == [("f.a", 0, "x"), ("f.new", 0, "r"), ("f.newer", False, "s"), ("f.d", 0, "x")]
           and added == ["f.new", "f.newer"] and dropped == ["f.b", "f.c"])
    print("fixtures-year self-test: defaults follow the operations (new inputs added after their anchors, removed ones "
          "dropped): " + ("as expected" if ok2 else f"WRONG ({got}; added {added}; dropped {dropped})"))
    # An answer to a removed input that equals its unconditional from-year default is dropped; one that differs, or
    # answers an input whose default is conditional, marks the case; an expectation on a removed line is dropped.
    removed = {"f.any", "w2.miles", "f.cond", "f.placed"}
    defaults = plain_defaults({"defaults": [{"input": "f.any", "value": False, "reason": "r"},
                                            {"input": "w2.miles", "value": 0, "reason": "r"},
                                            {"input": "f.cond", "value": False, "reason": "r", "withheld": {"when": []}},
                                            {"input": "f.placed", "value": "y2025", "reason": "r"}]})
    inputs = {"f.any": False, "person[taxpayer].w2[a].miles": 12, "person[taxpayer].w2[b].miles": 0, "f.cond": False,
              "f.placed": "y2026", "f.kept": 3}
    got3 = removed_answers(inputs, removed, defaults, 1)
    want3 = (["f.cond", "person[taxpayer].w2[a].miles"], ["f.any", "f.placed", "person[taxpayer].w2[b].miles"])
    got4 = removed_expectations({"f.line13": 1, "f.line14": 2, "person[taxpayer].w2[a].miles": 0}, removed | {"f.line13"})
    ok3 = got3 == want3 and got4 == ({"f.line14": 2}, ["f.line13", "person[taxpayer].w2[a].miles"])
    print("fixtures-year self-test: answers to removed inputs equal to their default dropped, others marked; "
          "expectations on removed lines dropped: " + ("as expected" if ok3 else f"WRONG ({got3}; {got4})"))
    return 0 if ok and all(refused) and ok2 and ok3 else 1


def carry_defaults(d, ops):
    """The defaults document `d` with the operations' new inputs added (add_question `default`, `reason`) and the
    inputs they remove dropped. Returns (added, dropped, removed), `removed` every input id the operations remove."""
    removed = {op.body["line"] for op in ops if op.kind == "remove_line"} | \
        {op.body["input"] for op in ops if op.kind == "remove_question"}
    defaults = [x for x in d.get("defaults", []) if x.get("input") not in removed]
    dropped = sorted({x["input"] for x in d.get("defaults", [])} - {x["input"] for x in defaults})
    added = []
    for op in ops:
        b = op.body
        if op.kind != "add_question" or "default" not in b or any(x["input"] == b["input"] for x in defaults):
            continue
        entry = {"input": b["input"], "value": b["default"], "reason": b.get("reason", "")}
        anchor = b.get("like") or b.get("after")
        at = next((i for i, x in enumerate(defaults) if x["input"] == anchor), None)
        defaults.insert(len(defaults) if at is None else at + 1, entry)
        added.append(b["input"])
    d["defaults"] = defaults
    return added, dropped, removed


def plain_defaults(d):
    """The unconditional test-data defaults of a defaults document, input -> value (an entry with a `withheld`
    condition is left out: whether it applies depends on the case)."""
    return {x["input"]: x["value"] for x in (d or {}).get("defaults", []) if "withheld" not in x}


def removed_answers(inputs, removed, defaults, shift):
    """A case's answers to the inputs the year removes, split: (those that differ from the input's from-year
    default, those that equal it). An answer equal to the default says what the default said, so it can be dropped
    and the case evaluated; one that differs makes the case not evaluated until it is moved."""
    gone, said = [], []
    for k in sorted(inputs):
        if template(k) not in removed:
            continue
        default = defaults.get(template(k), ())
        (said if default != () and json.dumps(inputs[k]) == json.dumps(shift_year(k, default, shift)) else gone).append(k)
    return gone, said


def removed_expectations(expect, removed):
    """A case's expectations split: (those on lines the year keeps, the keys of those on lines it removes)."""
    return ({k: v for k, v in expect.items() if template(k) not in removed},
            sorted(k for k in expect if template(k) in removed))


def comparable(value):
    """A value as compared across years: a refusal by its gate and form."""
    if isinstance(value, dict) and value.get("kind") == "refusal":
        return json.dumps({k: value.get(k) for k in ("kind", "gate", "form")}, sort_keys=True)
    return json.dumps(value, sort_keys=True)


def rests_on(derivations, key):
    """The line ids and parameter names a value's derivation reads, transitively."""
    lines, params, seen, todo = set(), set(), set(), [key]
    while todo:
        k = todo.pop()
        if k in seen:
            continue
        seen.add(k)
        lines.add(template(k))
        for op in (derivations.get(k) or {}).get("operands", []):
            ref = op.get("ref") or ""
            if ref.startswith("#"):
                params.add(ref[1:])
            elif ref in derivations:
                todo.append(ref)
    return lines, params


def evaluate(cases, year):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump([{"id": c["id"], "inputs": c["resolved"]} for c in cases], f)
        path = f.name
    # The results go to a file: written to a pipe, output this large fails (ENOBUFS).
    with tempfile.NamedTemporaryFile("w+", suffix=".json") as out:
        subprocess.run(NODE + ["eval", "--batch", path, "--year", str(year)], stdout=out, check=True)
        out.seek(0)
        results = json.load(out)["cases"]
    Path(path).unlink()
    return {cid: r.get("values", r) for cid, r in results.items()}


def build(year, plan_hint):
    """Build the year's data; on failure, exit with the build's error count and first errors."""
    r = subprocess.run(NODE + ["build", "--year", str(year)], capture_output=True, text=True)
    if r.returncode:
        errors = [line for line in (r.stdout + r.stderr).splitlines() if line.startswith("  - ")]
        sys.exit(f"the {year} definitions do not build ({len(errors)} errors; node engine/dist/main.js build --year {year}):\n"
                 + "\n".join(e[:200] for e in errors[:8]) + (f"\n{plan_hint}" if plan_hint else ""))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--from", dest="from_year", type=int, required=True)
    ap.add_argument("--to", dest="to_year", type=int, required=True)
    ap.add_argument("--no-hand-work", action="store_true")
    ap.add_argument("--plan", action="store_true", help="report on the from-year's data only; write no fixtures (see above)")
    a = ap.parse_args()
    f, t = a.from_year, a.to_year
    src, dst = ypath("fixtures", str(f)), ypath("fixtures", str(t))
    if a.plan:
        return plan(f, t, src)
    if dst.exists():
        sys.exit(f"refusing to overwrite fixtures/{t}/")
    build(t, f"--plan reports what would be re-recorded without the {t} build.")

    work_lines, work_params = worklist(f, t)

    files = {}
    for path in sorted(src.glob("*.json")):
        text = path.read_text(encoding="utf-8")
        data = json.loads(text)
        if "cases" not in data:
            continue
        indent = 1 if path.name == "classm.json" else 2
        files[path.name] = (data, indent)

    # The defaults follow the year's operations: new inputs' defaults added, removed inputs' dropped. The carried
    # file is the one the cases resolve against.
    import year_changes
    _, ops, problems = year_changes.load_changes(ypath("changes", str(t)))
    if problems:
        sys.exit("fixtures: the year changes do not load: " + "; ".join(problems))
    d = json.loads((src / "defaults.json").read_text(encoding="utf-8")) if (src / "defaults.json").exists() else None
    from_defaults = plain_defaults(d)
    new_defaults, dropped_defaults, removed_inputs = carry_defaults(d, ops) if d else ([], [], set())
    carried = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
    if d:
        d["tax_year"] = t
        json.dump(d, carried)
    carried.close()
    defaults = ([p for p in [ROOT / "fixtures" / str(y) / "defaults.json" for y in (t, f)] if p.exists()][:1]
                if jurisdiction.J == "ny" else []) + ([Path(carried.name)] if d else [])

    dropped, kept, rerecorded, reasons = [], 0, 0, collections.Counter()
    all_cases, stating, marked, answers_dropped = [], [], [], []
    for name, (data, _) in files.items():
        data["tax_year"] = t
        cases = []
        for c in data["cases"]:
            if str(c.get("evidence", "")).startswith("A"):
                dropped.append((name, c["id"]))
                continue
            c["inputs"] = {k: shift_year(k, v, t - f) for k, v in c["inputs"].items()}
            cases.append(c)
            # An answer to a removed input that is its from-year default says what the default said: dropped.
            gone, said = removed_answers(c["inputs"], removed_inputs, from_defaults, t - f)
            for k in said:
                del c["inputs"][k]
            if said:
                answers_dropped.append((name, c["id"], said))
                c["evidence_note"] = (f"Carried from {f}: dropped {', '.join(said)} (the {f} default; the {t} operations "
                                      f"remove the input). " + c.get("evidence_note", "")).strip()
            if gone:  # an answer to an input the year removes: not evaluated until it is moved to its successor
                stating += [(name, c["id"], k) for k in gone]
                marked.append((name, c["id"]))
                c["evidence_note"] = (f"Carried from {f}: was \u201c{c.get('evidence')}\u201d; states "
                                      f"{', '.join(gone)}, which the {t} operations remove. Earlier note: "
                                      f"{c.get('evidence_note', '')}").strip()
                c["evidence"] = f"not evaluated in {t}"
                continue
            c["file"] = name
            all_cases.append(c)
        data["cases"] = cases
    try:
        resolved = resolve_cases(all_cases, t, jurisdiction.J == "ny", defaults)
    except ValueError as e:
        sys.exit(f"fixtures {f} -> {t}: {e}")
    finally:
        Path(carried.name).unlink()
    for c in all_cases:
        c["resolved"] = resolved[c["id"]]
    results = evaluate(all_cases, t)

    failed, expect_dropped = [], []
    for c in all_cases:
        del c["file"]
        derivations = results[c["id"]]
        if "error" in derivations:
            failed.append((c["id"], derivations["error"]))
            del c["resolved"]
            c["evidence_note"] = (f"Carried from {f}: was \u201c{c.get('evidence')}\u201d; could not be evaluated in {t}: "
                                  f"{derivations['error']}. Earlier note: {c.get('evidence_note', '')}").strip()
            c["evidence"] = f"not evaluated in {t}"
            continue
        changed, resting = [], set()
        new_expect = {}
        expect, gone_lines = removed_expectations(c.get("expect") or {}, removed_inputs)
        if gone_lines:  # a line the year removes: nothing to expect of it
            expect_dropped += [(c["id"], k) for k in gone_lines]
            c["evidence_note"] = (f"Carried from {f}: dropped the expectation of {', '.join(gone_lines)}, removed by the "
                                  f"{t} operations. " + c.get("evidence_note", "")).strip()
        for key, old in expect.items():
            new = (derivations.get(key) or {}).get("value", {"kind": "unknown"})
            new_expect[key] = new
            if comparable(new) != comparable(old):
                changed.append(key)
            lines, ps = rests_on(derivations, key)
            resting |= (lines & work_lines) | {"#" + p for p in ps & work_params}
        c["expect"] = new_expect
        del c["resolved"]
        if changed or resting:
            rerecorded += 1
            why = []
            if changed:
                why.append(f"{len(changed)} value(s) changed ({', '.join(changed[:4])}{'...' if len(changed) > 4 else ''})")
                reasons["value changed"] += 1
            if resting:
                why.append("rests on " + ", ".join(sorted(resting)[:4]) + " (year-diff worklist)")
                reasons["rests on the worklist"] += 1
            c["evidence_note"] = (f"Carried from {f}: was “{c.get('evidence')}”; " + "; ".join(why)
                                  + (f". Earlier note: {c['evidence_note']}" if c.get("evidence_note") else ""))
            c["evidence"] = f"re-recorded for {t} (engine)"
        else:
            kept += 1
            c["evidence_note"] = (c.get("evidence_note", "") + f" Carried from {f} unchanged.").strip()

    dst.mkdir(parents=True)
    for name, (data, indent) in files.items():
        (dst / name).write_text(json.dumps(data, indent=indent, ensure_ascii=False) + "\n", encoding="utf-8")
    if d:
        # A consistency rule's open list names cases; one that names a dropped case would be refused by the build.
        gone = {cid for _, cid in dropped}
        for rule in d.get("consistency", []):
            if "open" in rule:
                rule["open"] = {cid: why for cid, why in rule["open"].items() if cid not in gone}
        (dst / "defaults.json").write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    docs = sorted({line.split(".")[0] for line in work_lines})
    hand = []
    if docs and not a.no_hand_work:
        subprocess.run(NODE + ["classm-jobs", "--year", str(t), "--docs", ",".join(docs)], check=True)
        for d in docs:
            r = subprocess.run([sys.executable, str(ROOT / "tools" / "transcription" / "classm.py"), "--doc", d, "--year", str(t)],
                               capture_output=True, text=True)
            hand.append((d, r.returncode, (r.stdout.strip().splitlines() or [""])[-1]))

    out = [f"# Fixtures carried from {f} to {t}", "",
           f"Generated by `tools/fixtures_year.py`. {kept + rerecorded} cases carried: {kept} kept their evidence, "
           f"{rerecorded} re-recorded ({', '.join(f'{k} {v}' for k, v in reasons.items()) or 'none'}); "
           f"{len(dropped)} official examples dropped; {len(failed) + len(marked)} marked not evaluated in {t} "
           f"({len(marked)} stating a removed input, {len(failed)} the {t} data rejects); "
           f"{len(answers_dropped)} cases had answers to a removed input equal to its {f} default dropped; "
           f"{len(expect_dropped)} expectations on removed lines dropped.", ""]
    if failed:
        out += [f"## Cases the {t} data rejects ({len(failed)})", "",
                "Their inputs are not valid for the new year (often a year value the new year's definitions do not "
                "yet list); their expected values are the old year's until they evaluate.", ""]
        out += [f"- `{cid}`: {err}" for cid, err in failed] + [""]
    if expect_dropped:
        out += [f"## Expectations dropped on lines the {t} operations remove ({len(expect_dropped)})", ""]
        out += [f"- `{cid}`: `{k}`" for cid, k in expect_dropped] + [""]
    if dropped:
        out += ["## Official examples to find for the new year", ""] + [f"- `{n}`: `{cid}`" for n, cid in dropped] + [""]
    out += ["## Test-data defaults", "",
            f"Added from the year's operations (add_question default): {', '.join(f'`{i}`' for i in new_defaults) or 'none'}. "
            f"Dropped with their inputs: {', '.join(f'`{i}`' for i in dropped_defaults) or 'none'}.", ""]
    if answers_dropped:
        by_input = collections.Counter(k for _, _, said in answers_dropped for k in said)
        out += [f"Answers to a removed input equal to its {f} default, dropped ({sum(by_input.values())} in "
                f"{len(answers_dropped)} cases): " + ", ".join(f"`{k}` {n}" for k, n in by_input.most_common()) + ".", ""]
    if stating:
        out += [f"Answers to an input the operations remove that differ from its {f} default ({len(stating)}, in "
                f"{len(marked)} cases): their cases are marked not evaluated, until the answer is moved to the input "
                "that replaces it or the case is re-derived:", ""]
        out += [f"- `{n}` `{cid}`: `{k}`" for n, cid, k in stating[:200]] + ([f"- and {len(stating) - 200} more"]
                                                                              if len(stating) > 200 else []) + [""]
    out += ["## Class M hand-work", ""]
    if not docs:
        out.append("No line of the definitions is on the year-diff worklist.")
    elif a.no_hand_work:
        out.append("Not run (--no-hand-work). Documents with a line on the worklist: " + ", ".join(docs) + ".")
    else:
        out += [f"- `{d}`: exit {code}; {last}" for d, code, last in hand]
    report = ypath("reports", str(t)) / f"fixtures_from_{f}.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"fixtures {f} -> {t}: defaults {len(new_defaults)} added, {len(dropped_defaults)} dropped "
          f"({sum(len(x[2]) for x in answers_dropped)} case answers to a removed input were its default and dropped; "
          f"{len(stating)} differ from it; {len(expect_dropped)} expectations on removed lines dropped)")
    print(f"fixtures {f} -> {t}: {kept} kept, {rerecorded} re-recorded, {len(failed) + len(marked)} not evaluated "
          f"({len(marked)} stating a removed input, {len(failed)} rejected), {len(dropped)} official examples dropped; "
          f"hand-work: {'skipped' if a.no_hand_work else len(hand)} document(s); report: {report.relative_to(ROOT)}")


def worklist(f, t, doc_only=None):
    """The to-year's worklist lines and parameters (the to-year's citations against both years);
    `doc_only`, if given, collects the ids ("#" before a parameter) whose only worklist
    finding is a cited document with no edition in one of the years."""
    diff = year_diff.run(f, t, t)
    work = [e for e in diff["items"] if year_diff.on_worklist(e)] if diff["flagged"] else []
    if doc_only is not None:
        for e in work:
            if {x["strength"] for x in e["findings"]} & year_diff.REVIEW == {"document"}:
                doc_only.add(("#" if e["kind"] == "parameter" else "") + e["id"])
    return ({e["id"] for e in work if e["kind"] in ("line", "refusal")},
            {e["id"] for e in work if e["kind"] == "parameter"})


def plan(f, t, src):
    """The --plan report: which carried cases rest on the to-year's worklist, by their
    derivations on the from-year's data."""
    if not (ypath("forms", str(t))).is_dir():
        sys.exit(f"--plan reads the {t} definitions' citations: adopt first (tools/year_diff.py --from {f} --to {t} --adopt)")
    build(f, "")
    doc_only = set()
    work_lines, work_params = worklist(f, t, doc_only)
    dropped, cases = [], []
    for path in sorted(src.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for c in ([] if path.name == "defaults.json" else data.get("cases", [])):
            if str(c.get("evidence", "")).startswith("A"):
                dropped.append((path.name, c["id"]))
                continue
            c["file"] = path.name
            cases.append(c)
    try:
        resolved = resolve_cases(cases, f, jurisdiction.J == "ny")
    except ValueError as e:
        sys.exit(f"fixtures {f} -> {t} (plan): {e}")
    for c in cases:
        c["resolved"] = resolved[c["id"]]
    results = evaluate(cases, f)
    rest, kept, failed = [], [], []
    for c in cases:
        derivations = results[c["id"]]
        if "error" in derivations:
            failed.append((c["id"], derivations["error"]))
            continue
        resting = set()
        for key in (c.get("expect") or {}):
            lines, ps = rests_on(derivations, key)
            resting |= (lines & work_lines) | {"#" + p for p in ps & work_params}
        (rest if resting else kept).append((c, resting))
    by_item = collections.Counter(r for _, resting in rest for r in resting)
    only_missing = sum(1 for _, resting in rest if resting <= doc_only)
    out = [f"# Fixtures carried from {f} to {t} (plan)", "",
           f"Generated by `tools/fixtures_year.py --plan`: the {t} definitions do not build yet, so no case was evaluated on "
           f"{t} data and fixtures/{t}/ was not written. Each case's derivation on the {f} data was read against the {t} "
           f"year-diff worklist. Of {len(cases)} cases that would be carried, {len(rest)} would be re-recorded (they rest on a "
           f"worklist line or parameter) and {len(kept)} would keep their evidence unless a value changes, which is known "
           f"only once {t} builds; {len(dropped)} official examples would be dropped; {len(failed)} could not be evaluated. "
           f"{only_missing} of the {len(rest)} rest only on items whose sole worklist finding is a cited document with no "
           f"{t} edition archived (marked * below).", "",
           "## Worklist items the most cases rest on", "", "| Item | Cases |", "| --- | --- |"]
    out += [f"| `{k}`{' *' if k in doc_only else ''} | {v} |" for k, v in by_item.most_common(25)]
    out += ["", f"## Cases that would be re-recorded ({len(rest)})", ""]
    out += [f"- `{c['file']}` `{c['id']}`: rests on " + ", ".join(f"`{r}`" for r in sorted(resting)[:5])
            + (f" and {len(resting) - 5} more" if len(resting) > 5 else "") for c, resting in rest]
    out += ["", f"## Cases that would keep their evidence unless a value changes ({len(kept)})", ""]
    out += [f"- `{c['file']}` `{c['id']}`" for c, _ in kept]
    if dropped:
        out += ["", "## Official examples to find for the new year", ""] + [f"- `{n}`: `{cid}`" for n, cid in dropped]
    if failed:
        out += ["", f"## Cases the {f} data rejects ({len(failed)})", ""] + [f"- `{cid}`: {err}" for cid, err in failed]
    out += ["", "## Class M hand-work", "", "Not run in a plan."]
    report = ypath("reports", str(t)) / f"fixtures_from_{f}.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"fixtures {f} -> {t} (plan): {len(rest)} would be re-recorded, {len(kept)} kept unless a value changes, "
          f"{len(dropped)} official examples dropped, {len(failed)} not evaluated; report: {report.relative_to(ROOT)}")


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    main()
