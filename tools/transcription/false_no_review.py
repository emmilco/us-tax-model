#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""False-no review: an isolated model looks for filers who would honestly answer a gate "no" while a gated line is
non-zero (the adversarial gate review).

A gate (gates.py: inputs marked `gated_by`, grouped by the condition their gate lines guard on) hides its gated
questions and zeroes its gated lines when its condition is false. A wrong no is silent: nothing downstream shows the
dropped amount. The review gives the model the condition as the filer reads it (question and help, or the computed
condition), each gated line with its English and gated question, the archived pages they cite, and the known false-no
patterns (PATTERNS below), and asks for every kind of filer
who would answer no truthfully, or by a plausible misreading, while the cited text gives a gated line an amount.

    false_no_review.py [--gates gate:a,gate:b] [--samples K] [--force-rerun REASON] [--approve-cost DOLLARS]
                       [--dry-run] [--jobs 6] [--model M]

Sampled standing review (samples.py): logged per form in reviews/<year>/false_no/<form>.json (the form of the gate's
condition), one record per gate holding its subject (gates.subject) and the samples run against it, each with its
verdict, findings, prompt hash, model and cost; rulings per sample in reviews/<year>/false_no/rulings.json under
"unruled:<gate>#<k>" with the record's subject_sha. A run gives each selected gate the samples its current subject
still needs this milestone; samples beyond it need --force-rerun REASON, and a run estimated above the owner's gate
needs --approve-cost (spend.py). Between releases a gate whose subject changed is due, not failed (check_false_no.py);
its --release mode refuses a release while any gate is due. Each call is one
fixed-prompt call to the selected model with no tools, logged in the cost ledger as kind `false_no`
(transcribe.call_model; costs.py reports it). Raw prompts and replies go to .transcription/false_no/.
"""
import argparse
import datetime
import glob
import hashlib
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from transcribe import ROOT, manifest, excerpt_for, call_model  # noqa: E402
from taxyear import Y  # noqa: E402
import jurisdiction  # noqa: E402
import gates  # noqa: E402
from screen_review import load_lines, encoded_english  # noqa: E402
import samples  # noqa: E402
import spend  # noqa: E402

OUT = str(jurisdiction.ypath("reviews", Y, "false_no"))
RAW = os.path.join(ROOT, ".transcription", *(["ny"] if jurisdiction.NY else []), "false_no")
KIND = "false_no"
SYSTEM = jurisdiction.system("You are an adversarial reviewer of the questions a tax tool asks a filer. You have no tools "
                             "and no other sources. Output only the YAML requested.")

# The failure patterns of the T-251 review's 43 findings (L-1 to L-43), each with the findings that show it.
PATTERNS = f"""1. A narrow time frame. "In {Y}" or the present tense, where the line also takes amounts from an
   earlier year's event or a disposition earlier this year: an installment payment on a 2021 sale (L-1); a
   partnership audit adjustment for a year the filer has since left (L-5); recapture of a fractional gift ten
   years on (L-6); a foreign fund sold in March, asked as "do you own" (L-13); a carryover or NOL from an earlier
   year's loss (L-10, L-20); a theft discovered this year, or insurance paid this year for last year's loss
   (L-18); recapture of an earlier year's credit (L-30); a section 965 installment after a disposition (L-29);
   tense generally (L-40).
2. A narrow verb or event. "Sell", "paid", "receive" or "payments", where the line also covers exchanges,
   worthless stock and bad debts (L-3), amounts included in income but not paid, such as a failed 409A plan (L-12),
   contributions an employer made that a Form 1099-R reports (L-4), small business stock losses (L-16), forks and
   airdrops besides "pay or rewards" (L-25).
3. A missing spouse. "You" on a joint return, where the spouse's facts make the line non-zero (L-17). Every
   per-return gate says "you or your spouse".
4. A document for a fact, or one issuer for all. Asking whether a form arrived, or naming one kind of issuer, when
   the line depends on the fact with or without a form: Form 2439 from a REIT, not only a mutual fund or ETF (L-2);
   a Form 1099-K for personal items sold at a loss (L-27); a CT-2 employee representative with no Form W-2 (L-11).
5. A hierarchy leak. The question is reached only through a parent whose truthful no excludes situations the
   child covers: a casualty NOL reached only through a business (L-10); railroad compensation only through wages
   (L-11); a fee-basis official only through wages (L-38); a child's investment income only through dependent
   care (L-32); a foreign corporation officer only through share ownership (L-34); refunds of deducted amounts
   only under "other income" (L-19); a tax credit bond, which may pay no interest, only under interest (L-31).
6. A list read as complete. Examples a filer takes as the whole rule: signature authority missing from foreign
   accounts (L-7); the grantor of an existing foreign trust (L-8); current-employer and inherited plans for
   required distributions (L-9); strike benefits (L-14); agency bonds beside Treasuries and savings bonds (L-22);
   Treasury money market funds read as not "bonds" (L-21); work around the home, not only in it (L-26);
   beneficiaries, who do not "own a share" of a trust (L-24); a list a filer reads as exhaustive (L-37).
7. A legal classification asked before a fact the filer can check. A filer cannot tell whether they have a
   "QBI loss carryforward" (L-20) or "section 1244 stock" (L-16), or whether all foreign income is "passive"
   (L-15); ask what they can check (a form received, a thing done) and classify after a broad yes.
8. An amount not perceived as the thing asked. A refund of a deducted tax as income (L-19); co-op maintenance as
   taxes and mortgage interest (L-23); strike benefits as pay (L-14); help text that invites a misreading (L-33,
   L-39); a complement or rule the filer must apply themselves (L-35, L-36)."""


def build_prompt(unit, lines, excerpt):
    condition, items = gates.describe(unit, lines, encoded_english)
    return jurisdiction.preface(f"""A tax preparation tool asks some questions only when a gate condition holds. When the condition does
not hold (the filer answers no, or the computed condition is false), the tool never asks the gated
questions below and treats each gated line as zero. A wrong no is silent: nothing later in the
return shows the amount it dropped. A joint return is in scope, and the filer may be anyone who
files a United States individual return.

Your task is adversarial: find every kind of filer who would answer the gate no, truthfully or by a
plausible reading of its words and help, while the IRS text below gives one of the gated lines an
amount (or makes it matter, such as a refusal the line leads to).

# The gate condition

{condition}

# Gated lines

{chr(10).join(items)}

# Patterns that produced wrong noes before

An earlier review of 43 such questions found these patterns. Test the gate against each, and look
for others.

{PATTERNS}

# Output

Return ONLY a YAML document of the form

verdict: "SOUND | FALSE_NO | UNCLEAR"
findings:
  - kind: "FALSE_NO | UNCLEAR"
    pattern: "<the number of the pattern above, or 'other'>"
    who: "<the filer, concretely: their situation in one or two sentences>"
    why_no: "<why they would answer no: the words they read that way>"
    line: "<the gated line that is then wrong>"
    irs_text: "<short quote with document and page that gives the line its amount>"
    severity: "high | medium | low"
    fix: "<wording, a broader gate, or a condition stated by the instructions>"

Severity: high, a truthful no to the question as worded yields a wrong value or a missed refusal;
medium, a plausible misreading does; low, wording or clarity. FALSE_NO is a truthful no; UNCLEAR a
plausible misreading. The verdict is SOUND only with no finding of medium or high severity. Use an
empty list when no filer answers no wrongly. No prose before or after the YAML.

# IRS text (archived snapshots; page markers show document, revision and page)

{excerpt}
""")


def prompt_for(unit, lines, mani):
    excerpt, used = excerpt_for(gates.pseudo_form(unit, lines), mani)
    return build_prompt(unit, lines, excerpt), used


def write_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def log_path(form):
    return os.path.join(OUT, f"{form}.json")


def read_log(form):
    path = log_path(form)
    if not os.path.exists(path):
        return {"form": form, "reviews": {}}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


SYSTEM_SHA = hashlib.sha256(SYSTEM.encode()).hexdigest()
# The fields of one sample; the others describe the gate and are kept once on its record.
SAMPLE_FIELDS = ("verdict", "findings", "prompt_sha", "system_sha", "model", "cost", "date", "response", "rerun_reason")
VERDICTS = ("SOUND", "FALSE_NO", "UNCLEAR")


def run_one(key, unit, lines, mani, model, dry, from_response, k=None, subject=None):
    """One review of a gate (a flat record: the gate's fields and the sample's, split by as_sample). Sample k's reply
    is kept as <gate>.<subject>.<k>.response.txt; without k, as <gate>.response.txt."""
    prompt, used = prompt_for(unit, lines, mani)
    os.makedirs(RAW, exist_ok=True)
    base = os.path.join(RAW, gates.safe_name(key))
    write_text(base + ".prompt.txt", prompt)
    if dry:
        return {"gate": key, "chars": len(prompt), "lines": len(unit["gates"])}
    response = f"{base}.{subject[:12]}.{k}.response.txt" if k and subject else base + ".response.txt"
    if from_response:
        with open(response, encoding="utf-8") as f:
            text, meta = f.read(), {}
    else:
        text, meta = call_model(prompt, model, system=SYSTEM, kind=KIND, subject=key)
        write_text(response, text)
    blocks = re.findall(r"```(?:yaml)?\s*\n(.*?)```", text, re.S)
    try:
        doc = yaml.safe_load(blocks[-1] if blocks else text) or {}
    except yaml.YAMLError:
        doc = {}
    if not isinstance(doc, dict):
        doc = {}
    out = {"gate": key, "form": gates.unit_form(unit, lines), "condition": unit["condition"],
           "lines": [g["id"] for _, g, _ in unit["gates"]], "inputs": [i["id"] for _, _, i in unit["gates"]],
           "verdict": str(doc.get("verdict", "UNPARSED")), "findings": doc.get("findings") or [],
           "prompt_sha": hashlib.sha256(prompt.encode()).hexdigest(),
           "subject_sha": gates.subject(unit, lines, encoded_english), "used": used,
           "model": ", ".join(meta.get("model_reported", [])) or model, "cost": meta.get("cost_usd") or 0,
           "date": datetime.date.today().isoformat(), "system_sha": SYSTEM_SHA, "response": os.path.relpath(response, ROOT)}
    if os.environ.get(spend.REASON_ENV):
        out["rerun_reason"] = os.environ[spend.REASON_ENV]
    return out


def as_sample(flat):
    """(gate fields, sample) of run_one's flat record. A verdict outside VERDICTS is an unparsed sample."""
    unit = {k: v for k, v in flat.items() if k not in SAMPLE_FIELDS and k not in ("gate", "form")}
    smp = {k: flat[k] for k in SAMPLE_FIELDS if k in flat}
    if smp.get("verdict") not in VERDICTS:
        smp["parse_error"] = True
    return unit, smp


def records():
    """{gate: (form, record)} over every form's log, in the sampled format (samples.py)."""
    out = {}
    for path in sorted(glob.glob(os.path.join(OUT, "*.json"))):
        if os.path.basename(path) == "rulings.json":
            continue
        log = json.load(open(path, encoding="utf-8"))
        legacy = [k for k, r in log.get("reviews", {}).items() if "samples" not in r]
        if legacy:
            sys.exit(f"{path}: {len(legacy)} review(s) in the single-review format ({', '.join(legacy[:5])}); "
                     "the file predates sampled reviews")
        for key, r in log.get("reviews", {}).items():
            out[key] = (log.get("form"), r)
    return out


def write_results(results, subjects):
    """Merges each sample into its gate's record in its form's log: a gate whose subject changed starts a new record;
    other gates' records are kept."""
    by_form = {}
    for j, r in sorted(results, key=lambda x: x[0]["k"]):
        by_form.setdefault(r["form"], []).append(r)
    os.makedirs(OUT, exist_ok=True)
    for form, rs in sorted(by_form.items()):
        log = read_log(form)
        for r in rs:
            unit, smp = as_sample(r)
            rec = log["reviews"].get(r["gate"])
            if not rec or rec.get("subject_sha") != subjects[r["gate"]]:
                rec = log["reviews"][r["gate"]] = {"subject_sha": subjects[r["gate"]], "samples": []}
            rec.update({k: v for k, v in unit.items() if k != "subject_sha"})
            rec["samples"].append(smp)
        log["reviews"] = dict(sorted(log["reviews"].items()))
        with open(log_path(form), "w", encoding="utf-8") as f:
            json.dump(log, f, indent=1, ensure_ascii=False)
            f.write("\n")


def plan(units, lines, mani, recs, asked, force, price, model):
    """One entry per selected gate: {gate, subject, note, jobs}, as completeness_review.plan."""
    out = []
    for key, unit in units.items():
        subject = gates.subject(unit, lines, encoded_english)
        form = gates.unit_form(unit, lines)
        held = recs.get(key)
        rec = held[1] if held and held[0] == form else None
        n, beyond = samples.wanted(rec, subject, asked)
        entry = {"gate": key, "unit": unit, "subject": subject, "jobs": []}
        if n == 0:
            entry["note"] = "satisfied: its current subject has the milestone's samples"
        elif beyond and not force:
            entry["note"] = (f"refused: {n} sample(s) would go beyond the milestone's {samples.SAMPLES_PER_MILESTONE}; "
                             "--force-rerun REASON runs them")
        else:
            first = len(rec["samples"]) + 1 if rec and rec.get("subject_sha") == subject else 1
            usd = spend.estimate(len(prompt_for(unit, lines, mani)[0]), "false_no_review.py", model, price)
            entry["jobs"] = [{"kind": "false_no", "form": key, "k": k, "run": True, "usd": usd} for k in range(first, first + n)]
            entry["note"] = f"{n} sample(s) from #{first}"
        out.append(entry)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--gates", help="comma-separated gate keys (gate:<condition>); default every gate")
    ap.add_argument("--dry-run", action="store_true", help="plan and estimate; call no model")
    ap.add_argument("--samples", type=int, metavar="K", help="run K samples per gate (default: those the milestone still needs)")
    ap.add_argument("--force-rerun", metavar="REASON", help="run samples beyond the milestone; the reason is recorded")
    ap.add_argument("--approve-cost", metavar="DOLLARS", type=float,
                    help=f"run although the estimate exceeds the ${spend.COST_GATE_USD:.2f} gate; at least the estimate")
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--model", default="claude-opus-5-5")
    a = ap.parse_args(argv)
    if a.force_rerun is not None and not a.force_rerun.strip():
        ap.error("--force-rerun needs a reason")
    import build_fresh
    build_fresh.require(rendered=True)  # the prompt quotes each gated line's rendered English
    lines = load_lines()
    mani = manifest()
    units = gates.units(lines)
    if a.gates:
        wanted = a.gates.split(",")
        unknown = [g for g in wanted if g not in units]
        if unknown:
            ap.error("no such gate: " + ", ".join(unknown))
        units = {k: v for k, v in units.items() if k in wanted}
    planned = plan(units, lines, mani, records(), a.samples, a.force_rerun, spend.prices(), a.model)
    jobs = [j for e in planned for j in e["jobs"]]
    for e in planned:
        print(f"{e['gate']:40s} {e['note']}" + (f"  ~${sum(j['usd'] or 0 for j in e['jobs']):.2f}" if e["jobs"] else ""))
    print(f"{len(jobs)} sample(s), estimated ${sum(j['usd'] or 0 for j in jobs):.2f}; gate ${spend.COST_GATE_USD:.2f}")
    refusal = spend.gate(jobs, a.approve_cost)
    if a.dry_run:
        if refusal:
            print(f"would be refused: {refusal}")
        return
    if refusal:
        sys.exit(f"refused: {refusal}")
    if not jobs:
        return
    if a.force_rerun:
        os.environ[spend.REASON_ENV] = a.force_rerun
    by_key = {e["gate"]: e for e in planned if e["jobs"]}
    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        results = list(ex.map(lambda j: (j, run_one(j["form"], by_key[j["form"]]["unit"], lines, mani, a.model, False, False,
                                                     j["k"], by_key[j["form"]]["subject"])), jobs))
    write_results(results, {k: e["subject"] for k, e in by_key.items()})
    done = [as_sample(r)[1] for _, r in results]
    print(f"{len(done)} sample(s); verdicts: " + ", ".join(f"{v} {sum(1 for d in done if d['verdict'] == v)}"
                                                          for v in sorted({d["verdict"] for d in done}))
          + f"; cost {sum(d['cost'] for d in done):.2f}")


if __name__ == "__main__":
    main()
