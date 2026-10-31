# SPDX-License-Identifier: Apache-2.0
"""Shared acceptance logic for the source-coverage checks (T-084 to T-089).

A check produces findings {"kind", "line", "form", "detail"}. A finding is accepted by a ruling
(`rulings`: key -> reason) or by the baseline of findings that existed when the check was introduced
(`baseline`: key -> hash of the finding's subject). The subject is the form's canonical data unless the finding
names a narrower one (`subject`: the line itself for line findings, one sentence, or one input-and-section pair). A baseline entry holds only while
its subject is unchanged, so the baseline is worked off as each subject is next changed; it may only shrink, and an
entry or ruling that no longer fails is an error.
"""
import hashlib
import json
from pathlib import Path


def load_forms(canonical):
    forms = []
    for path in sorted(Path(canonical).glob("*.json")):
        doc = next(iter(json.loads(path.read_text()).values()))
        if isinstance(doc, dict) and "lines" in doc:
            forms.append(doc)
    return forms


def form_hashes(forms):
    return {f["id"]: hashlib.sha256(json.dumps(f, sort_keys=True).encode()).hexdigest()[:16] for f in forms}


def key(f):
    return f"{f['kind']}:{f['line']}"


def line_subject(line):
    """A line's own canonical data: a finding about one line comes due when that line changes (owner's decision 2026-10-30)."""
    return json.dumps(line, sort_keys=True)


def subject_hash(f, hashes):
    if "subject" in f:
        return hashlib.sha256(str(f["subject"]).encode()).hexdigest()[:16]
    return hashes[f["form"]]


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
    baseline = {k for k, h in recorded.items() if k in current and subject_hash(current[k], hashes) == h}
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
