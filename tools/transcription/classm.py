#!/usr/bin/env python3
"""Class M hand-work (spec 6.1, 6.5): an isolated model works one document by hand from its
archived pages and the values that flow into it, for a few generated returns that together
take every reachable branch of the document. Its answers are compared with the project's
and become class M fixtures (fixtures/<year>/classm.json); every disagreement is logged with
a ruling.

    python3 tools/transcription/classm.py --doc qdcg [--model M] [--dry-run] [--from-response]

It builds the data and rebuilds the document's jobs (classm-jobs, .classm/jobs.json)
before every run, including --from-response, so a run never works from jobs of older data.
    python3 tools/transcription/rule.py --kind classm --doc qdcg --rulings r.json

Logs go to reviews/<year>/classm/<doc>.md. Rulings persist in <doc>.rulings.json beside the log
(rulings.py) and are reapplied on rerun. A ruling may drop a line from the fixture (a model
arithmetic error is not evidence) by giving {"ruling": "...", "drop": true}.

A model of another family (families.py) writes <doc>.<family>.md with <doc>.<family>.rulings.json,
its fixtures to fixtures/<year>/classm.<family>.json with the family suffixed to each case id, and
its raw prompts and responses under .classm/ with the same suffix; the Claude log and fixtures are
untouched.
"""
import argparse, datetime, hashlib, json, os, re, subprocess, sys
from fractions import Fraction
import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from transcribe import ROOT, manifest, excerpt_for, load_form, review_response  # noqa: E402
from taxyear import YEAR, Y, YEAR_ARGS  # noqa: E402
import families  # noqa: E402
import rulings  # noqa: E402
import subjects  # noqa: E402

JOBS = os.path.join(ROOT, ".classm", "jobs.json")
RAW = os.path.join(ROOT, ".classm")
LOGS = os.path.join(ROOT, "reviews", Y, "classm")
PROMPT_POLICY = "worked-values-request-bound-v2"


def fixture_path(family=families.DEFAULT):
    return os.path.join(ROOT, "fixtures", Y, families.fixture_name(family))
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
    # The value type follows the label in brackets: in parentheses after the number it reads as
    # part of the handle (the form shared line numbers take) and is echoed back.
    fill = "\n".join(f'- line {handle(job, l)}: {l["label"]} [value type: {l["type"]}]' for l in job["fill"])
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
IRS text (where two lines share a number, followed by a name in parentheses: answer with the whole
handle, exactly as given), with its value type: a money line takes a dollar amount; a Bool line takes yes or no; a
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
    fill = "\n".join(f'- "{handle(job, l)}" ({l["type"]}): {l["label"]}' for l in job["fill"])
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

{('Only printed IRS output lines are requested. Work any intermediate steps you need from the source, but do not report unrequested implementation helpers.' if job.get('worked_scope') == 'printed-irs-lines' else '')}

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
    if s in ("", "blank", "skip", "skipped", "none", "n/a"):
        return {"kind": "blank"}
    if vtype.startswith("Enum("):
        return {"kind": "enum", "value": s}
    if vtype == "Rate":
        if s == "-0-":
            return {"kind": "rate", "num": 0, "den": 1}
        f = Fraction(s.rstrip("%")) / (100 if s.endswith("%") else 1)
        return {"kind": "rate", "num": f.numerator, "den": f.denominator}
    if s == "-0-":
        return {"kind": "money", "cents": 0} if vtype not in ("Bool", "Count") else ({"kind": "bool", "value": False} if vtype == "Bool" else {"kind": "count", "value": 0})
    if vtype == "Bool":
        if s not in ("yes", "true", "y", "1", "no", "false", "n", "0"):
            raise ValueError(f"invalid Bool answer: {raw!r}")
        return {"kind": "bool", "value": s in ("yes", "true", "y", "1")}
    if vtype == "Count":
        n = float(s)
        if not n.is_integer():
            raise ValueError(f"noninteger Count answer: {raw!r}")
        return {"kind": "count", "value": int(n)}
    neg = s.startswith("(") and s.endswith(")")
    s = s.strip("()").strip("$")
    cents = int(round(float(s) * 100))
    return {"kind": "money", "cents": -cents if neg else cents}


def handle(job, line):
    """How a line to fill is named to the model and in the log: its printed number, or, where
    two lines of the job share it (EIC Worksheets A and B both have a line 6), the number
    followed by the line's id, so that one answer cannot stand for the other."""
    shared = sum(1 for l in job["fill"] if l["printed"] == line["printed"]) > 1
    return f'{line["printed"]} ({line["id"]})' if shared else line["printed"]


def extract(text):
    # A response may hold an abandoned draft block before the finished one; the answer is the last block.
    blocks = re.findall(r"```(?:yaml)?\s*\n(.*?)```", text, re.S)
    m = blocks[-1] if blocks else None
    doc = yaml.safe_load(m if m is not None else text)
    if not isinstance(doc, dict) or not isinstance(doc.get("lines"), list):
        raise ValueError("response has no `lines`")
    out = {}
    for l in doc["lines"]:
        if not isinstance(l, dict):
            raise ValueError("worked line must be a mapping")
        # The prompt lists "line 6"; an answer may repeat the word.
        key = re.sub(r"^line\s+", "", str(l.get("printed", "")).strip(), flags=re.I)
        if not key or key in out:
            raise ValueError(f"missing or duplicate worked-line key: {key!r}")
        out[key] = {"value": l.get("value", ""), "work": str(l.get("work", "")).strip()}
    return out


def answers_for(job, verdicts):
    """The worked answers keyed by the handles of the job's lines. A reply key that is not a handle
    is matched when it is one with its parentheses dropped ("Step 5, 1" or "CLW 1" for "(Step 5, 1)")
    or with the line's value type echoed after it ("1 (NonNegDollars)"); an exact key wins."""
    handles = {handle(job, l): l for l in job["fill"]}
    out = {k: v for k, v in verdicts.items() if k in handles}
    for key, v in verdicts.items():
        if key in handles:
            continue
        aliases = [(f"({key})", None)]
        typed = re.match(r"^(.*?)\s*\(([^()]*(?:\([^()]*\))?)\)$", key)
        if typed:
            aliases += [(typed.group(1), typed.group(2)), (f"({typed.group(1)})", typed.group(2))]
        for alias, echoed in aliases:
            line = handles.get(alias)
            if line is not None and echoed in (None, line["type"]):
                out.setdefault(alias, v)
                break
    return out


def same(a, b):
    if a.get("kind") == "rate" and b.get("kind") == "rate":
        return a["num"] * b["den"] == b["num"] * a["den"]
    return a.get("kind") == b.get("kind") and (a.get("cents") == b.get("cents") if a.get("kind") == "money" else a.get("value") == b.get("value"))


def write_outputs(form_doc, model, jobs, runs, meta_all):
    """One log for the document and the fixture cases for it."""
    os.makedirs(LOGS, exist_ok=True)
    fid = form_doc["id"]
    family = families.family_of(model)
    path = rulings.log_path("classm", fid, family)
    fixture = fixture_path(family)
    counts = {"AGREE": 0, "DISAGREE": 0, "SKIPPED": 0, "MISSING": 0}
    out = [f"# Class M hand-work — {fid}", "",
           f"`{form_doc['title']}` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/{Y}/{families.fixture_name(family)}`; each disagreement carries a ruling.", "",
           "| field | value |", "| --- | --- |",
           f"| date | {datetime.date.today().isoformat()} |",
           f"| model requested | {model} |",
           f"| model reported | {', '.join(sorted({m for meta in meta_all.values() for m in meta.get('model_reported', [])})) or '-'} |",
           f"| prompt policy | {PROMPT_POLICY} |",
           f"| system sha256 | {hashlib.sha256(SYSTEM.encode()).hexdigest()} |",
           f"| reasoning effort | {next(iter(meta_all.values())).get('reasoning_effort') or 'provider default'} |",
           f"| output token budget | {next(iter(meta_all.values())).get('request_max_tokens') or 'transport default (65536 for DeepSeek)'} |",
           f"| subject sha256 | {subjects.current('classm', fid, Y)} |",
           f"| cases | {len(jobs)} |"]
    if all(job.get('worked_scope') == 'printed-irs-lines' for job in jobs):
        out.append('| worked target scope | printed IRS lines |')
    used = runs[jobs[0]["id"]]["used"]
    out += ["", "## Source pages given to the model", "", "| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for u in used:
        out.append(f"| {u['doc']} | {u['revision']} | {', '.join(map(str, u['pages'])) or '-'} | {u['how']} | {u['text_sha256']} | {', '.join(map(str, u.get('cols_pages', []))) or '-'} | {u.get('cols_sha256', '-')} |")
    out += ["", "## Lines", ""]
    context_text = "\n".join(out + [f"### case {job['id']} — prompt sha256 {runs[job['id']]['prompt_sha']};" for job in jobs])
    kept = rulings.kept("classm", fid, family, context=rulings.review_context("classm", context_text))
    fixture_cases = []
    for job in jobs:
        run = runs[job["id"]]
        out.append(f"### case {job['id']} — prompt sha256 {run['prompt_sha']}; branches: {', '.join(job['branches'])}")
        out.append("")
        expect = {}
        answers = answers_for(job, run["verdicts"])
        for l in job["fill"]:
            v = answers.get(handle(job, l))
            proj = job["project"][l["id"]]
            if v is None:
                status = "MISSING"; model_v = None
            else:
                try:
                    model_v = parse_value(v["value"], l["type"])
                except (ValueError, TypeError):
                    model_v = None
                status = ("SKIPPED" if model_v is not None and model_v["kind"] == "blank" else
                          "AGREE" if model_v is not None and same(model_v, proj) else "DISAGREE")
            counts[status] += 1
            out.append(f"### {job['id']} — {handle(job, l)} — {l['label'][:80].rstrip()}")
            out.append(f"Status: **{status}**")
            if status == "AGREE":
                out += ["", f"Value: {dollars(proj)}", ""]
                expect[l["id"]] = proj
            elif status == "SKIPPED":
                out += ["", "Model: blank", f"Work: {v.get('work', '')}", "",
                        "No numeric assertion or class M credit: the model left this line blank.", ""]
            else:
                pv, mv = dollars(proj), (dollars(model_v) if model_v else str(v["value"] if v else "no answer"))
                out += ["", f"Project: {pv}", f"Model: {mv}"]
                if v and v.get("work"):
                    out.append(f"Work: {v['work']}")
                ruling = kept.get((job["id"], handle(job, l), pv, mv), "Ruling: open")
                out += ["", ruling, ""]
                if model_v is not None and not ruling.endswith("[dropped]"):
                    expect[l["id"]] = model_v
        fixture_cases.append({"id": families.case_id(job["id"], family), "covers": [fid], "evidence": "M",
                              "evidence_note": f"Class M: {model}; prompt sha256 {run['prompt_sha']}; pages " + "; ".join(f"{u['doc']} {','.join(map(str, u['pages']))} ({u['text_sha256'][:12]})" for u in used) + f"; branches {', '.join(job['branches'])}",
                              "inputs": job["inputs"], "expect": expect})
    out += ["## Raw responses", ""]
    for job in jobs:
        out += [f"### {job['id']}", "", "```yaml", runs[job["id"]]["raw"].strip(), "```", ""]
    open(path, "w", encoding="utf-8").write("\n".join(out))
    # Merge this document's cases into the family's fixture file.
    fx = json.load(open(fixture)) if os.path.exists(fixture) else {"tax_year": YEAR, "cases": []}
    # A rerun regenerates the cases, so a mutant only a replaced case killed can survive: name the
    # replaced cases so any the mutation step needs can be kept in a stage fixture.
    kept_inputs = {json.dumps(c["inputs"], sort_keys=True) for c in fixture_cases}
    replaced = [c["id"] for c in fx["cases"] if c["id"].startswith(f"classm.{fid}.")
                and json.dumps(c["inputs"], sort_keys=True) not in kept_inputs]
    if replaced:
        print(f"{fid}: {len(replaced)} earlier class M case(s) replaced ({', '.join(replaced)}); rerun the mutation step and keep "
              "any case a mutant needs in a stage fixture", file=sys.stderr)
    merged, inserted = [], False
    for case in fx["cases"]:
        if case["id"].startswith(f"classm.{fid}."):
            if not inserted:
                merged.extend(fixture_cases)
                inserted = True
        else:
            merged.append(case)
    if not inserted:
        merged.extend(fixture_cases)
    fx["cases"] = merged
    json.dump(fx, open(fixture, "w"), indent=2)
    open(fixture, "a").write("\n")
    return path, counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--doc", required=True)
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--reasoning-effort", choices=("low", "high", "max"))
    ap.add_argument("--max-output-tokens", type=int)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--from-response", action="store_true")
    ap.add_argument("--case-jobs", type=int, default=1, help="concurrent isolated case requests (default 1)")
    a = ap.parse_args()
    if not 1 <= a.case_jobs <= 8:
        ap.error('--case-jobs must be between 1 and 8')
    # The jobs are built from the canonical data, so build it and rebuild this document's jobs
    # first: a run on jobs from older data would compare the model with old values. A lock keeps
    # runs side by side (rerun_all.py) from building at once.
    import fcntl
    os.makedirs(os.path.dirname(JOBS), exist_ok=True)
    with open(os.path.join(os.path.dirname(JOBS), "lock"), "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        main_js = os.path.join(ROOT, "engine", "dist", "main.js")
        subprocess.run(["node", main_js, "build", *YEAR_ARGS], check=True, stdout=subprocess.DEVNULL)
        subprocess.run(["node", "--max-old-space-size=8192", main_js, "classm-jobs", "--docs", a.doc, "--include-fixtures", *YEAR_ARGS], check=True, stdout=subprocess.DEVNULL)
        jobs = [j for j in json.load(open(JOBS))["jobs"] if j["doc"] == a.doc]
    if not jobs:
        sys.exit(f"{a.doc}: no jobs in {JOBS}; run classm-jobs")
    form_doc = load_form(a.doc)
    excerpt, used = excerpt_for(form_doc, manifest())
    runs, meta_all = {}, {}
    family = families.family_of(a.model)
    def work(job):
        prompt = build_entry_prompt(form_doc, excerpt, job) if job.get("kind") else build_prompt(form_doc, excerpt, job)
        base = os.path.join(RAW, families.case_id(job["id"], family))
        sha = hashlib.sha256(prompt.encode()).hexdigest()
        print(f"{job['id']}: prompt {len(prompt):,} chars, {len(job['fill'])} lines to fill, {len(job['given']) + len(job['own_inputs'])} amounts given")
        if a.dry_run:
            with open(base + ".preview.prompt.txt", "w", encoding="utf-8") as f:
                f.write(prompt)
            return job['id'], None, None
        text, meta = review_response(prompt, a.model, base, PROMPT_POLICY, a.from_response, SYSTEM, a.reasoning_effort, a.max_output_tokens)
        return job['id'], {"verdicts": extract(text), "raw": text, "prompt_sha": sha, "used": used}, meta
    if a.case_jobs == 1:
        worked = map(work, jobs)
        for ident, run, meta in worked:
            if run is not None:
                runs[ident] = run
                meta_all[ident] = meta
    else:
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=a.case_jobs) as pool:
            for ident, run, meta in pool.map(work, jobs):
                if run is not None:
                    runs[ident] = run
                    meta_all[ident] = meta
    if a.dry_run:
        return
    path, counts = write_outputs(form_doc, a.model, jobs, runs, meta_all)
    cost = sum((m.get("cost_usd") or 0) for m in meta_all.values())
    print(f"{a.doc}: agree {counts['AGREE']}, disagree {counts['DISAGREE']}, skipped {counts['SKIPPED']}, missing {counts['MISSING']}; cost {cost:.2f} -> {os.path.relpath(path, ROOT)}")
    sys.exit(0 if counts["DISAGREE"] + counts["MISSING"] == 0 else 3)


if __name__ == "__main__":
    main()
