# SPDX-License-Identifier: Apache-2.0
"""Shared acceptance logic for the source-coverage checks (T-084 to T-089).

A check produces findings {"kind", "line", "form", "detail"}. A finding is accepted by a ruling
(`rulings`: key -> reason) or by the baseline of findings that existed when the check was introduced
(`baseline`: key -> hash of the finding's subject). The subject is the form's canonical data unless the finding
names a narrower one (`subject`: the line itself for line findings, one sentence, or one input-and-section pair). A baseline entry holds only while
its subject is unchanged, so the baseline is worked off as each subject is next changed; it may only shrink, and an
entry or ruling that no longer fails is an error.

A year's rulings and baseline are carried to the next year at adoption (year_diff.py --adopt), byte for byte. Adoption
moves two marks of the year in every subject without changing what it says: each citation's `tax_year` and a
"(<year>)" edition in a locator. An entry therefore also holds when its subject, with those two marks moved back one
year, hashes as recorded (year_back); any other change makes it due. The match reaches back one year only: an entry
still recorded with the hash of two years before comes due.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import jurisdiction  # noqa: E402


def load_forms(canonical):
    """The jurisdiction's documents of the canonical build: the federal ones by default, the New York
    ones (ids `ny_`) with --jurisdiction ny. The build writes both into canonical/<year>/ (decision C1);
    each check looks at its own jurisdiction's documents, so federal findings are unchanged."""
    forms = []
    for path in sorted(Path(canonical).glob("*.json")):
        doc = next(iter(json.loads(path.read_text()).values()))
        if isinstance(doc, dict) and "lines" in doc and str(doc.get("id", "")).startswith("ny_") == jurisdiction.NY:
            forms.append(doc)
    return forms


def form_hashes(forms):
    return {f["id"]: hashlib.sha256(json.dumps(f, sort_keys=True).encode()).hexdigest()[:16] for f in forms}


def key(f):
    return f"{f['kind']}:{f['line']}"


def line_subject(line):
    """A line's own canonical data: a finding about one line comes due when that line changes (owner's decision 2026-10-30)."""
    return json.dumps(line, sort_keys=True)


def subject_hash(f, hashes, year=None):
    """The hash of a finding's subject; with `year`, of the subject with that year's adoption marks moved back
    (year_back; `hashes` then holds the forms' hashes moved back the same way)."""
    if "subject" in f:
        text = str(f["subject"])
        return hashlib.sha256((year_back(text, year) if year else text).encode()).hexdigest()[:16]
    return hashes[f["form"]]


def year_back(text, year):
    """A subject's text with the marks adoption moves to `year` moved back one year: a `tax_year` field and a
    "(<year>)" edition."""
    year = int(year)
    text = re.sub(rf'("tax_year": ){year}(?!\d)', rf"\g<1>{year - 1}", text)
    return re.sub(rf"\({year}\)", f"({year - 1})", text)


def forms_year(forms):
    """The tax year of the canonical documents, else None."""
    years = {f.get("tax_year") for f in forms if isinstance(f.get("tax_year"), int)}
    return years.pop() if len(years) == 1 else None


def year_of(path):
    """The year directory a rulings file lies in (reviews/<year>/ or reviews/ny/<year>/), else None."""
    name = Path(path).parent.name
    return int(name) if name.isdigit() else None


def run(name, forms, found, rulings_path, report_path, title, legend, rebaseline=False):
    """Accept, report and print; returns the exit status (1 on new findings or stale entries)."""
    rulings_path, report_path = Path(rulings_path), Path(report_path)
    hashes = form_hashes(forms)
    data = json.loads(rulings_path.read_text()) if rulings_path.exists() else {"rulings": {}, "baseline": {}}
    rulings = data.get("rulings", {})
    if rebaseline:
        data["baseline"] = {key(f): subject_hash(f, hashes) for f in sorted(found, key=key) if key(f) not in rulings}
        rulings_path.parent.mkdir(parents=True, exist_ok=True)
        rulings_path.write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")
    recorded = data.get("baseline", {})
    current = {key(f): f for f in found}
    year = forms_year(forms) or year_of(rulings_path)
    moved = {fid: hashlib.sha256(year_back(json.dumps(f, sort_keys=True), year).encode()).hexdigest()[:16]
             for fid, f in ((f["id"], f) for f in forms)} if year else {}
    baseline = {k for k, h in recorded.items() if k in current and h in
                (subject_hash(current[k], hashes), year and subject_hash(current[k], moved, year))}
    changed = {k for k in recorded if k in current and k not in baseline}
    new = [f for f in found if key(f) not in rulings and key(f) not in baseline]
    stale = sorted(set(recorded) - set(current)) + sorted(set(rulings) - set(current))

    report_path.parent.mkdir(parents=True, exist_ok=True)
    rows = [f"# {title}", "", legend, "",
            f"Findings: {len(found)}; ruled {sum(1 for k in current if k in rulings)}; "
            f"in the baseline to be worked off {len(baseline - set(rulings))}.", "",
            "| Kind | Line | Detail | Status |", "| --- | --- | --- | --- |"]
    for k in sorted(current):
        f = current[k]
        r = rulings.get(k)
        if isinstance(r, dict):  # a structured ruling: its class or verdict, then its reason
            r = "; ".join(str(r[x]) for x in ("class", "verdict", "reason", "evidence", "refusal", "bug", "line", "gate") if r.get(x))
        status = f"ruled: {r}" if k in rulings else ("baseline" if k in baseline else "**new**")
        rows.append(f"| {f['kind']} | `{f['line']}` | {f['detail']} | {status} |")
    report_path.write_text("\n".join(rows) + "\n", encoding="utf-8")

    print(f"{name}: {len(found)} finding(s); {len(new)} new; {len(baseline & set(current))} in the baseline; "
          f"{len(set(rulings) & set(current))} ruled; {len(stale)} stale")
    for f in new:
        why = "its form changed since the baseline; fix or rule it" if key(f) in changed else "new"
        print(f"  {why}: {f['kind']}: {f['line']}: {f['detail']}")
    for k in stale:
        print(f"  stale: {k} no longer fails; remove it from {rulings_path.name}")
    return 1 if new or stale else 0
