#!/usr/bin/env python3
"""Class M hand-work (spec 6.1, 6.5): an isolated model works one document by hand from its
archived pages and the values that flow into it, for a few generated returns that together
take every reachable branch of the document. Its answers are compared with the project's
and become class M fixtures (fixtures/<year>/classm.json); every disagreement is logged with
a ruling.

    node engine/dist/main.js classm-jobs                  # write .classm/jobs.json (offline)
    python3 tools/transcription/classm.py --doc qdcg [--model M] [--dry-run] [--from-response]
    python3 tools/transcription/rule.py --kind classm --doc qdcg --rulings r.json

Logs go to reviews/<year>/classm/<doc>.md. Rulings persist in <doc>.rulings.json beside the log
(rulings.py) and are reapplied on rerun. A ruling may drop a line from the fixture (a model
arithmetic error is not evidence) by giving {"ruling": "...", "drop": true}.
"""
import argparse, datetime, hashlib, json, os, re, sys
from fractions import Fraction
import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from transcribe import ROOT, manifest, excerpt_for, call_model, load_form  # noqa: E402
from taxyear import YEAR, Y  # noqa: E402
import rulings  # noqa: E402

JOBS = os.path.join(ROOT, ".classm", "jobs.json")
RAW = os.path.join(ROOT, ".classm")
LOGS = os.path.join(ROOT, "reviews", Y, "classm")
FIXTURE = os.path.join(ROOT, "fixtures", Y, "classm.json")
SYSTEM = ("You work IRS forms and worksheets by hand from the text given to you and the amounts you are "
          "given. You have no tools and no other sources. Output only the YAML requested.")
STATUS_WORDS = {"single": "Single", "mfj": "Married filing jointly", "mfs": "Married filing separately",
                "hoh": "Head of household", "qss": "Qualifying surviving spouse"}


RATE_ENUM_NOTE = """ A Rate line takes a percentage exactly as the table prints it (for example 17.49%); an
Enum(name) line takes one of that enumeration's values, written as the value itself (for example y5 or hy)."""


def dollars(v):
    k = v.get("kind")
    if k == "money":
        return f"${v['cents'] / 100:,.2f}"
    if k == "bool":
        return "yes" if v["value"] else "no"
    if k == "count":
        return str(v["value"])
    if k == "enum":
        return STATUS_WORDS.get(v["value"], v["value"])
    if k == "rate":
        return _pct(v)
    return str(v)


def _pct(v):
    """A rate as an exact percentage: 0.1749 is 17.49%."""
    from decimal import Decimal, getcontext
    getcontext().prec = 40
    d = Decimal(v["num"]) * 100 / Decimal(v["den"])
    t = format(d.normalize(), "f")
    return t + "%"


_titles = {}


def title_of(doc_id):
    if doc_id not in _titles:
        try:
            _titles[doc_id] = load_form(doc_id)["title"]
        except Exception:
            _titles[doc_id] = doc_id
    return _titles[doc_id]


def given_name(g, fid):
    """How a given amount is named: a printed line of another document by its document title and
    line number with its wording; a helper of another document by its label; a line of this document
    by its number."""
    if g["doc"] == fid:
        return f"this document, line {g['printed']}"
    if re.match(r"^[0-9]", g["printed"]):
        return f"{title_of(g['doc'])}, line {g['printed']} ({g['label']})"
    return f"{title_of(g['doc'])}: {g['label']}"


def build_prompt(form_doc, excerpt, job):
    fid = form_doc["id"]
    given = []
    for g in job["given"]:
        if g["ref"] == "f1040.status":
            continue  # the filing status heads the prompt
        note = f" [{g['note']}]" if g.get("note") else ""
        given.append(f"- {given_name(g, fid)}: {dollars(g['value'])}{note}")
    for o in job["own_inputs"]:
        tag = f"line {o['printed']}" if not o["printed"].startswith("(") else "a record the filer supplies"
        given.append(f"- {tag}: {o['source']}: {dollars(o['value'])}")
    coll = []
    for cname, entries in job["collections"].items():
        for entry, fields in entries.items():
            coll.append(f"- {entry}: " + "; ".join(f"{f['label']} = {dollars(f['value'])}" for f in fields))
    fill = "\n".join(f'- line {l["printed"]} ({l["type"]}): {l["label"]}' for l in job["fill"])
    return f"""You are filling in one IRS form or worksheet by hand for one taxpayer, working ONLY from the IRS
text provided below and the amounts given here. Do not rely on memory of the tax law or of any
software. Follow the printed line instructions exactly, including every "if zero or less, enter -0-",
every "smaller of" and "larger of", every skip instruction, and every filing-status choice.

# The document

Form id: {fid}
Title: {form_doc['title']}
Tax year: {form_doc['tax_year']}
Filing status: {STATUS_WORDS.get(job['status'], job['status'])}

# Amounts given

These are the amounts that flow into this document from the rest of the return, and the amounts the
filer supplies. Use them as they are; they are already correct. Amounts are dollars and cents.

{chr(10).join(given) if given else '(none)'}
{(chr(10) + 'Entries of the keyed collections the document totals (each entry with the fields it reads):' + chr(10) + chr(10).join(coll)) if coll else ''}

# Lines to fill

Work these lines of the document in order. Each is named by its printed number as it appears in the
IRS text, with its value type: a money line takes a dollar amount; a Bool line takes yes or no; a
Count line takes a whole number. A line the instructions tell you to skip, or that is blank, is
written as blank.

{fill}

# Output

Return ONLY a YAML document of the form

lines:
  - printed: "<printed>"
    value: "<dollars.cents, or yes/no, or a whole number, or blank>"
    work: "<one short line showing the arithmetic or the rule applied>"

No prose before or after the YAML.

# IRS text (archived snapshots; page markers show document, revision and page)

{excerpt}
"""


def build_entry_prompt(form_doc, excerpt, job):
    """A keyed collection worked once per entry, or one instance of a shared definition."""
    fid = form_doc["id"]
    given = []
    for g in job["given"]:
        if g["ref"] == "f1040.status":
            continue
        if job.get("kind") == "def":
            given.append(f"- {g['label']}: {dollars(g['value'])}")
            continue
        note = f" [{g['note']}]" if g.get("note") else ""
        given.append(f"- {given_name(g, fid)}: {dollars(g['value'])}{note}")
    entries = []
    for entry, fields in (job.get("entries") or {}).items():
        entries.append(f"- {entry}: " + ("; ".join(f"{f['label']} = {dollars(f['value'])}" for f in fields) or "(no amounts given)"))
    coll = []
    for cname, ents in job["collections"].items():
        for entry, fields in ents.items():
            coll.append(f"- {entry}: " + "; ".join(f"{f['label']} = {dollars(f['value'])}" for f in fields))
    fill = "\n".join(f'- "{l["printed"]}" ({l["type"]}): {l["label"]}' for l in job["fill"])
    if job.get("kind") == "def":
        what = ("This is a shared computation the forms invoke on an amount: work it for the one amount and "
                "filing status given.") if len(job["given"]) <= 1 else (
                "This is a shared computation a form invokes for one person: work it for the amounts and filing "
                "status given.")
    else:
        what = ("This document is filled in once per entry (one row or one record per person, employer, sale "
                "or gift). Each entry below is named by its key; work every listed line for every entry.")
    return f"""You are working one IRS computation by hand for one taxpayer, working ONLY from the IRS text
provided below and the amounts given here. Do not rely on memory of the tax law or of any software.
Follow the printed instructions exactly, including every test, every "if zero or less, enter -0-",
every "smaller of" and "larger of", and every filing-status choice.

# The computation

Id: {fid}
Title: {form_doc['title']}
Tax year: {form_doc['tax_year']}
Filing status: {STATUS_WORDS.get(job['status'], job['status'])}

{what}

# Amounts given

Use them as they are; they are already correct. Amounts are dollars and cents.

{chr(10).join(given) if given else '(none)'}
{(chr(10) + 'Entries (each with the amounts and answers the filer supplied for it):' + chr(10) + chr(10).join(entries)) if entries else ''}
{(chr(10) + 'Entries of other keyed collections this one totals:' + chr(10) + chr(10).join(coll)) if coll else ''}

# Lines to fill

Each line is named by a quoted handle, with its value type and what it asks: a money line takes a
dollar amount; a Bool line takes yes or no (the answer to the question or test as stated); a Count
line takes a whole number.{RATE_ENUM_NOTE if any(l["type"] == "Rate" or l["type"].startswith("Enum(") for l in job["fill"]) else ""}

{fill}

# Output

Return ONLY a YAML document of the form

lines:
  - printed: "<the quoted handle, exactly as given>"
    value: "<dollars.cents, or yes/no, or a whole number>"
    work: "<one short line citing the rule or the arithmetic>"

No prose before or after the YAML.

# IRS text (archived snapshots; page markers show document, revision and page)

{excerpt}
"""


def parse_value(raw, vtype):
    s = str(raw).strip().strip("$").replace(",", "").lower()
    if vtype.startswith("Enum("):
        return {"kind": "enum", "value": s}
    if vtype == "Rate":
        if s in ("", "blank", "-0-", "none", "n/a"):
            return {"kind": "rate", "num": 0, "den": 1}
        f = Fraction(s.rstrip("%")) / (100 if s.endswith("%") else 1)
        return {"kind": "rate", "num": f.numerator, "den": f.denominator}
    if s in ("", "blank", "-0-", "skip", "skipped", "none", "n/a"):
        return {"kind": "money", "cents": 0} if vtype not in ("Bool", "Count") else ({"kind": "bool", "value": False} if vtype == "Bool" else {"kind": "count", "value": 0})
    if vtype == "Bool":
        return {"kind": "bool", "value": s in ("yes", "true", "y")}
    if vtype == "Count":
        return {"kind": "count", "value": int(round(float(s)))}
    neg = s.startswith("(") and s.endswith(")")
    s = s.strip("()").strip("$")
    cents = int(round(float(s) * 100))
    return {"kind": "money", "cents": -cents if neg else cents}


def extract(text):
    # A response may hold an abandoned draft block before the finished one; the answer is the last block.
    blocks = re.findall(r"```(?:yaml)?\s*\n(.*?)```", text, re.S)
    m = blocks[-1] if blocks else None
    doc = yaml.safe_load(m if m is not None else text)
    out = {}
    for l in doc["lines"]:
        out[str(l.get("printed", ""))] = {"value": l.get("value", ""), "work": str(l.get("work", "")).strip()}
    return out


def same(a, b):
    if a.get("kind") == "rate" and b.get("kind") == "rate":
        return a["num"] * b["den"] == b["num"] * a["den"]
    return a.get("kind") == b.get("kind") and (a.get("cents") == b.get("cents") if a.get("kind") == "money" else a.get("value") == b.get("value"))


def write_outputs(form_doc, model, jobs, runs, meta_all):
    """One log for the document and the fixture cases for it."""
    os.makedirs(LOGS, exist_ok=True)
    fid = form_doc["id"]
    path = os.path.join(LOGS, fid + ".md")
    kept = rulings.kept("classm", fid)
    counts = {"AGREE": 0, "DISAGREE": 0, "MISSING": 0}
    out = [f"# Class M hand-work — {fid}", "",
           f"`{form_doc['title']}` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/{Y}/classm.json`; each disagreement carries a ruling.", "",
           "| field | value |", "| --- | --- |",
           f"| date | {datetime.date.today().isoformat()} |",
           f"| model requested | {model} |",
           f"| model reported | {', '.join(sorted({m for meta in meta_all.values() for m in meta.get('model_reported', [])})) or '-'} |",
           f"| cases | {len(jobs)} |"]
    used = runs[jobs[0]["id"]]["used"]
    out += ["", "## Source pages given to the model", "", "| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for u in used:
        out.append(f"| {u['doc']} | {u['revision']} | {', '.join(map(str, u['pages'])) or '-'} | {u['how']} | {u['text_sha256']} | {', '.join(map(str, u.get('cols_pages', []))) or '-'} | {u.get('cols_sha256', '-')} |")
    out += ["", "## Lines", ""]
    fixture_cases = []
    for job in jobs:
        run = runs[job["id"]]
        out.append(f"### case {job['id']} — prompt sha256 {run['prompt_sha']}; branches: {', '.join(job['branches'])}")
        out.append("")
        expect = {}
        for l in job["fill"]:
            v = run["verdicts"].get(l["printed"])
            proj = job["project"][l["id"]]
            if v is None:
                status = "MISSING"; model_v = None
            else:
                try:
                    model_v = parse_value(v["value"], l["type"])
                except (ValueError, TypeError):
                    model_v = None
                status = "AGREE" if model_v is not None and same(model_v, proj) else "DISAGREE"
            counts[status] += 1
            out.append(f"### {job['id']} — {l['printed']} — {l['label'][:80]}")
            out.append(f"Status: **{status}**")
            if status == "AGREE":
                out += ["", f"Value: {dollars(proj)}", ""]
                expect[l["id"]] = proj
            else:
                pv, mv = dollars(proj), (dollars(model_v) if model_v else str(v["value"] if v else "no answer"))
                out += ["", f"Project: {pv}", f"Model: {mv}"]
                if v and v.get("work"):
                    out.append(f"Work: {v['work']}")
                ruling = kept.get((job["id"], l["printed"], pv, mv), "Ruling: open")
                out += ["", ruling, ""]
                if model_v is not None and not ruling.endswith("[dropped]"):
                    expect[l["id"]] = model_v
        fixture_cases.append({"id": job["id"], "covers": [fid], "evidence": "M",
                              "evidence_note": f"Class M: {model}; prompt sha256 {run['prompt_sha']}; pages " + "; ".join(f"{u['doc']} {','.join(map(str, u['pages']))} ({u['text_sha256'][:12]})" for u in used) + f"; branches {', '.join(job['branches'])}",
                              "inputs": job["inputs"], "expect": expect})
    out += ["## Raw responses", ""]
    for job in jobs:
        out += [f"### {job['id']}", "", "```yaml", runs[job["id"]]["raw"].strip(), "```", ""]
    open(path, "w", encoding="utf-8").write("\n".join(out))
    # Merge this document's cases into the fixture file.
    fx = json.load(open(FIXTURE)) if os.path.exists(FIXTURE) else {"tax_year": YEAR, "cases": []}
    fx["cases"] = [c for c in fx["cases"] if not c["id"].startswith(f"classm.{fid}.")] + fixture_cases
    fx["cases"].sort(key=lambda c: c["id"])
    json.dump(fx, open(FIXTURE, "w"), indent=1)
    open(FIXTURE, "a").write("\n")
    return path, counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--doc", required=True)
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--from-response", action="store_true")
    a = ap.parse_args()
    jobs = [j for j in json.load(open(JOBS))["jobs"] if j["doc"] == a.doc]
    if not jobs:
        sys.exit(f"{a.doc}: no jobs in {JOBS}; run classm-jobs")
    form_doc = load_form(a.doc)
    excerpt, used = excerpt_for(form_doc, manifest())
    runs, meta_all = {}, {}
    for job in jobs:
        prompt = build_entry_prompt(form_doc, excerpt, job) if job.get("kind") else build_prompt(form_doc, excerpt, job)
        base = os.path.join(RAW, job["id"])
        open(base + ".prompt.txt", "w", encoding="utf-8").write(prompt)
        sha = hashlib.sha256(prompt.encode()).hexdigest()
        print(f"{job['id']}: prompt {len(prompt):,} chars, {len(job['fill'])} lines to fill, {len(job['given']) + len(job['own_inputs'])} amounts given")
        if a.dry_run:
            continue
        if a.from_response:
            text = open(base + ".response.txt", encoding="utf-8").read()
            meta = json.load(open(base + ".meta.json")) if os.path.exists(base + ".meta.json") else {}
        else:
            text, meta = call_model(prompt, a.model, system=SYSTEM)
            open(base + ".response.txt", "w", encoding="utf-8").write(text)
            json.dump(meta, open(base + ".meta.json", "w"))
        runs[job["id"]] = {"verdicts": extract(text), "raw": text, "prompt_sha": sha, "used": used}
        meta_all[job["id"]] = meta
    if a.dry_run:
        return
    path, counts = write_outputs(form_doc, a.model, jobs, runs, meta_all)
    cost = sum((m.get("cost_usd") or 0) for m in meta_all.values())
    print(f"{a.doc}: agree {counts['AGREE']}, disagree {counts['DISAGREE']}, missing {counts['MISSING']}; cost {cost:.2f} -> {os.path.relpath(path, ROOT)}")
    sys.exit(0 if counts["DISAGREE"] + counts["MISSING"] == 0 else 3)


if __name__ == "__main__":
    main()
