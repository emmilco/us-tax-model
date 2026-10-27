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
    documents with a line on the worklist, unless --no-hand-work.

Writes reports/<to>/fixtures_from_<from>.md.

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

YEAR_KEYS = ("placed", "placed_date")
NODE = ["node", str(ROOT / "engine" / "dist" / "main.js")]


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


def resolve(inputs, params):
    out = {}
    for k, v in inputs.items():
        if isinstance(v, dict) and "param" in v:
            base = params[v["param"]]["value"]
            out[k] = (base[v["status"]] if "status" in v else base) + v["offset"]
        else:
            out[k] = v
    return out


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
    src, dst = ROOT / "fixtures" / str(f), ROOT / "fixtures" / str(t)
    if a.plan:
        return plan(f, t, src)
    if dst.exists():
        sys.exit(f"refusing to overwrite fixtures/{t}/")
    build(t, f"--plan reports what would be re-recorded without the {t} build.")
    params = json.loads((ROOT / "canonical" / str(t) / "params.json").read_text())["params"]["values"]

    work_lines, work_params = worklist(f, t)

    files = {}
    for path in sorted(src.glob("*.json")):
        text = path.read_text(encoding="utf-8")
        data = json.loads(text)
        if "cases" not in data:
            continue
        indent = 1 if path.name == "classm.json" else 2
        files[path.name] = (data, indent)

    dropped, kept, rerecorded, reasons = [], 0, 0, collections.Counter()
    all_cases = []
    for name, (data, _) in files.items():
        data["tax_year"] = t
        cases = []
        for c in data["cases"]:
            if str(c.get("evidence", "")).startswith("A"):
                dropped.append((name, c["id"]))
                continue
            c["inputs"] = {k: shift_year(k, v, t - f) for k, v in c["inputs"].items()}
            c["resolved"] = resolve(c["inputs"], params)
            cases.append(c)
            all_cases.append(c)
        data["cases"] = cases
    results = evaluate(all_cases, t)

    failed = []
    for c in all_cases:
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
        for key, old in (c.get("expect") or {}).items():
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
           f"{len(dropped)} official examples dropped; {len(failed)} could not be evaluated.", ""]
    if failed:
        out += [f"## Cases the {t} data rejects ({len(failed)})", "",
                "Their inputs are not valid for the new year (often a year value the new year's definitions do not "
                "yet list); their expected values are the old year's until they evaluate.", ""]
        out += [f"- `{cid}`: {err}" for cid, err in failed] + [""]
    if dropped:
        out += ["## Official examples to find for the new year", ""] + [f"- `{n}`: `{cid}`" for n, cid in dropped] + [""]
    out += ["## Class M hand-work", ""]
    if not docs:
        out.append("No line of the definitions is on the year-diff worklist.")
    elif a.no_hand_work:
        out.append("Not run (--no-hand-work). Documents with a line on the worklist: " + ", ".join(docs) + ".")
    else:
        out += [f"- `{d}`: exit {code}; {last}" for d, code, last in hand]
    report = ROOT / "reports" / str(t) / f"fixtures_from_{f}.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"fixtures {f} -> {t}: {kept} kept, {rerecorded} re-recorded, {len(failed)} not evaluated, {len(dropped)} official examples dropped; "
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
    if not (ROOT / "forms" / str(t)).is_dir():
        sys.exit(f"--plan reads the {t} definitions' citations: adopt first (tools/year_diff.py --from {f} --to {t} --adopt)")
    build(f, "")
    params = json.loads((ROOT / "canonical" / str(f) / "params.json").read_text())["params"]["values"]
    doc_only = set()
    work_lines, work_params = worklist(f, t, doc_only)
    dropped, cases = [], []
    for path in sorted(src.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for c in data.get("cases", []):
            if str(c.get("evidence", "")).startswith("A"):
                dropped.append((path.name, c["id"]))
                continue
            c["resolved"] = resolve(c["inputs"], params)
            c["file"] = path.name
            cases.append(c)
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
    report = ROOT / "reports" / str(t) / f"fixtures_from_{f}.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"fixtures {f} -> {t} (plan): {len(rest)} would be re-recorded, {len(kept)} kept unless a value changes, "
          f"{len(dropped)} official examples dropped, {len(failed)} not evaluated; report: {report.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
