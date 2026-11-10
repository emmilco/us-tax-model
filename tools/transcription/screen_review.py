#!/usr/bin/env python3
"""Screen review (T-008): an isolated model judges each scope screen against the instruction
text of every line it stands in for.

A screen is a yes/no input that one or more lines name as a refusal gate: answered yes, those
lines refuse with a citation; answered no, they are computed (usually with the source the screen
covers pinned to zero). A screen worded narrower than those lines lets an unsupported case through
as a zero; one worded wider refuses cases the tool computes. The review gives the model the
screen's question, each gated line with its encoded English (from rendered/) and its refusal text,
and the archived pages those lines cite, and asks for every case the wording misses or sweeps in.

A choose-guard gate (gates.py: an input marked `gated_by` and its gate line) is reviewed the same way, keyed
`gate:<condition>`: the condition's wording (the question the filer answers, or the computed condition) and every gate
line on it with its gated question, against the pages they cite. Answered no (or false), the gate's lines are zero and
their questions are not asked, so the review looks for a situation the cited text gives a gated line an amount in which
the condition is false (NARROW), and checks that the condition is the one the cited text states. A gate's review is
current while its subject (gates.subject: wording and gated lines, not the prompt's own text) is unchanged.

    screen_review.py [--screens a,b] [--gates-only] [--samples K] [--force-rerun REASON] [--approve-cost DOLLARS]
                     [--dry-run] [--jobs 6] [--model M]

Sampled standing review (samples.py): a unit's subject is its question, the gated lines' English and refusals and
the pages they cite (screen_subject; gates.subject for a gate), without the system prompt. A run gives each selected
unit the samples its current subject still needs this milestone, merged into reviews/<year>/screens/screen_review.json;
samples beyond it need --force-rerun REASON, and a run estimated above the owner's gate needs --approve-cost
(spend.py). Between releases a unit whose subject changed is due, not failed (tools/transcription/check_screens.py);
its --release mode refuses a release while any unit is due. Findings are adjudicated in
reviews/<year>/screens/screen_review.md and ruled per sample in reviews/<year>/screens/rulings.json. Each call is one fixed-prompt call to the selected model with no tools (fixed-prompt, curated input, no action surface): `claude` through `claude -p`, or an equal-authority peer through its transport (families.py; docs/2026-10-24_validation_policy.md).
"""
import argparse, datetime, glob, hashlib, json, os, re, sys
from concurrent.futures import ThreadPoolExecutor
import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from transcribe import ROOT, manifest, excerpt_for, call_model  # noqa: E402
from taxyear import Y  # noqa: E402
import jurisdiction  # noqa: E402  (--jurisdiction ny: the screens of New York lines; reviews/ny/<year>/screens/)
import gates  # noqa: E402
from structured_text import indent_rest, continued  # noqa: E402
import samples  # noqa: E402
import spend  # noqa: E402

OUT = str(jurisdiction.ypath("reviews", Y, "screens"))
# A New York screen review may share its screen (a federal scope question gating New York lines) with a federal
# one, so its raw prompts and responses are kept apart.
RAW = os.path.join(ROOT, ".transcription", *(["ny"] if jurisdiction.NY else []), "screens")
SYSTEM = jurisdiction.system("You review the questions a tax tool asks a filer against the IRS text the questions stand in "
                             "for. You have no tools and no other sources. Output only the YAML requested.")


def load_lines():
    lines = {}
    for path in [p for d in jurisdiction.read_dirs("forms", Y) for p in sorted(glob.glob(os.path.join(str(d), "*.yaml")))]:
        d = yaml.safe_load(open(path, encoding="utf-8"))
        doc = d.get("form") or d.get("def")
        for l in doc["lines"]:
            lines[l["id"]] = (doc["id"], l)
    return lines


def encoded_english(doc_id, line_id):
    path = os.path.join(str(jurisdiction.doc_dir("rendered", Y, doc_id)), doc_id + ".md")
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^## [^\n]*`" + re.escape(line_id) + r"`\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        return "(no rendering)"
    enc = re.search(r"\*\*Encoded[^*]*\*\*:? ?(.*)", m.group(1))
    return (enc.group(1) + continued(m.group(1), enc.start())).strip() if enc else "(no rendering)"


def gate_inputs(lines):
    """{gate line: its gated Bool input} (gates.py convention: the input is marked `gated_by` and the gate line is a
    `choose` of the same document). A refusal that names such a gate line is the refusal of the input's screen."""
    out = {}
    for lid, (doc, l) in lines.items():
        g = l.get("gated_by")
        if g and g in lines and l.get("type") == "Bool" and (l.get("expr") or {}).get("op") == "input" \
                and (lines[g][1].get("expr") or {}).get("op") == "choose":
            out.setdefault(g, []).append(lid)
    return {g: ids[0] for g, ids in out.items() if len(ids) == 1}


def screens(lines):
    """{screen: [(doc, gated line, refusal)]}: every input that gates a line, with the lines of the jurisdiction
    under review it gates (in New York mode a federal screen gating New York lines is reviewed for those). A refusal
    whose `when` is the gate line of a gated Bool input counts for that input."""
    gated = gate_inputs(lines)
    found = {}
    for lid, (doc, l) in lines.items():
        if not jurisdiction.mine(doc):
            continue
        for r in l.get("refuses", []) or []:
            found.setdefault(gated.get(r["when"], r["when"]), []).append((doc, l, r))
    return {g: v for g, v in sorted(found.items()) if g in lines and lines[g][1]["expr"].get("op") == "input"}


def screen_gate(screen, lines):
    """The gate condition text of a gated screen input (shown in its prompt, not part of its subject), or ""."""
    sdoc, sline = lines[screen]
    gid = sline.get("gated_by")
    if not gid or gid not in lines or gate_inputs(lines).get(gid) != screen:
        return ""
    gdoc, gate = lines[gid]
    guard_refs = sorted(gates.refs([a.get("guard") for a in gate["expr"].get("alternatives", [])]) & set(lines))
    cond = guard_refs[0] if len(guard_refs) == 1 else None
    text, _ = gates.describe({"condition": cond, "gates": [(gdoc, gate, sline)]}, lines, encoded_english)
    return text


def gate_note(gate):
    if not gate:
        return ""
    return ("\nThe filer is asked this question only when its gate condition holds; otherwise it is not asked and the "
            "answer is no (the lines then compute as shown). The gate condition is reviewed separately.\n"
            f"Gate condition: {gate}\n")


def build_prompt(screen, sline, gated, excerpt, gate=""):
    items = []
    for doc, l, r in gated:
        items.append(f"""- Line `{l['id']}` (document {doc}, printed {l['printed']}): {indent_rest(l['label'], "    ")}
  Computed as (when the screen is answered no): {indent_rest(encoded_english(doc, l['id']), "    ")}
  Refusal when the screen is answered yes: {r['form']} — {r['remedy']}
  Cited: {l['cite']['doc']} {l['cite']['locator']}; refusal cites {r['cite']['doc']} {r['cite']['locator']}""")
    return jurisdiction.preface(f"""A tax preparation tool asks the filer a yes/no screening question. If the filer answers YES, the
tool refuses the lines listed below (it stops and names the form the filer needs). If the filer
answers NO, the tool computes those lines as shown, which usually means the amounts the screen
covers are treated as zero.

The question is right only if a filer who reads it and answers truthfully answers YES in every
situation the IRS text of those lines needs that the tool does not compute, and NO in every
situation the tool does compute correctly.

# The screening question

Input `{screen}`: {sline['expr']['source']}
{gate_note(gate)}
# Lines that refuse when the answer is yes

{chr(10).join(items)}

# Your task

Read the IRS text below. Report:
- NARROW: a situation the IRS text of these lines covers, which the tool does not compute (the
  computed line would treat it as zero or ignore it), but which a filer could truthfully answer NO
  to under the question's wording. Quote the IRS text and say why the wording misses it.
- WIDE: a situation the question's wording makes a filer answer YES to, although the tool computes
  it correctly. Quote the question and the IRS text.
- UNCLEAR: wording a filer could reasonably read either way.
Do not report differences that arise only on a joint return (married filing statuses are refused
elsewhere) or situations another listed refusal already covers.

# Output

Return ONLY a YAML document of the form

verdict: "COVERS | NARROW | WIDE | UNCLEAR"
findings:
  - kind: "NARROW | WIDE | UNCLEAR"
    situation: "<one sentence>"
    irs_text: "<short quote with document and page>"
    why: "<one or two sentences>"

Use an empty list when the question covers the lines exactly. No prose before or after the YAML.

# IRS text (archived snapshots; page markers show document, revision and page)

{excerpt}
""")


def build_gate_prompt(unit, lines, excerpt):
    condition, items = gates.describe(unit, lines, encoded_english)
    return jurisdiction.preface(f"""A tax preparation tool asks some questions only when a gate condition holds. When the condition does
not hold, the tool never asks the gated questions below and treats each gated line as zero. The
condition is either a question the filer answers (answered no, the gated lines are zero) or a
condition the tool computes from earlier answers.

The gate is right only if, in every situation the IRS text below gives one of the gated lines an
amount (or makes it matter), the condition holds: a filer who reads the question and answers it
truthfully answers yes, or the computed condition is true. Where the cited text states the
condition itself ("Use this form if...", "Who must file"), the gate must be that condition.
Gate questions deliberately lean to yes: a wrong yes costs a few questions, a wrong no silently
drops an amount. A joint return is in scope: the question must cover the spouse.

# The gate condition

{condition}

# Gated lines

{chr(10).join(items)}

# Your task

Read the IRS text below. Report:
- NARROW: a situation the IRS text gives a gated line an amount (or a refusal) in which the
  condition is false: a filer could truthfully answer no, or the computed condition is false.
  Quote the IRS text and say why the condition misses it.
- SOURCE: the cited text states a condition, and the gate's condition differs from it (another
  threshold, time frame, person or event). Quote both.
- UNCLEAR: wording a filer could reasonably read either way.
- WIDE: the condition holds in a situation the IRS text gives every gated line no amount. Report
  it, but it does not change the verdict: gates lean to yes by design.

# Output

Return ONLY a YAML document of the form

verdict: "COVERS | NARROW | SOURCE | UNCLEAR"
findings:
  - kind: "NARROW | SOURCE | UNCLEAR | WIDE"
    situation: "<one sentence>"
    irs_text: "<short quote with document and page>"
    why: "<one or two sentences>"

The verdict is COVERS when there is no NARROW, SOURCE or UNCLEAR finding. Use an empty list when the
gate covers the lines exactly. No prose before or after the YAML.

# IRS text (archived snapshots; page markers show document, revision and page)

{excerpt}
""")


def units(lines):
    """Every review subject of the jurisdiction: {screen: ("screen", gated lines)} and {"gate:<condition>": ("gate",
    unit)}. --screens selects among both keys."""
    out = {k: ("screen", v) for k, v in screens(lines).items()}
    out.update({k: ("gate", u) for k, u in gates.units(lines).items()})
    return out


def gate_prompt_for(unit, lines, mani):
    """The review prompt of one gate and the pages it gives."""
    excerpt, used = excerpt_for(gates.pseudo_form(unit, lines), mani)
    return build_gate_prompt(unit, lines, excerpt), used


def prompt_for(screen, gated, lines, mani, with_gate=True):
    """The review prompt of one screen and the pages it gives. A gated screen's prompt shows its gate condition;
    `with_gate=False` is the prompt without it, which is the screen's review subject (screen_subject)."""
    if screen.startswith("gate:"):
        return gate_prompt_for(gated, lines, mani)
    sdoc, sline = lines[screen]
    pseudo = {"id": screen, "lines": [sline] + [l for _, l, _ in gated] + [{"cite": r["cite"], "expr": {}} for _, _, r in gated]}
    excerpt, used = excerpt_for(pseudo, mani)
    return build_prompt(screen, sline, gated, excerpt, screen_gate(screen, lines) if with_gate else ""), used


def screen_subject(screen, gated, lines, mani):
    """The hash a screen's review is current against: the prompt without the gate condition, so gating a screen's
    input changes it only through the wording or gated lines it already depended on. The gate condition is the subject of
    the gate's own review (gate:<condition>)."""
    prompt, _ = prompt_for(screen, gated, lines, mani, with_gate=False)
    return hashlib.sha256(prompt.encode()).hexdigest()


def subject_of(key, unit, lines, mani):
    """The subject hash a unit's samples are current against: screen_subject for a screen, gates.subject for a gate."""
    kind, gated = unit
    return gates.subject(gated, lines, encoded_english) if kind == "gate" else screen_subject(key, gated, lines, mani)


def run_one(screen, gated, lines, mani, model, dry, from_response, k=None, subject=None):
    """One review of a unit (a flat record: the unit's fields and the sample's, split by SAMPLE_FIELDS). Sample k's
    response is kept as <unit>.<subject>.<k>.response.txt; without k, as <unit>.response.txt."""
    gate = screen.startswith("gate:")
    prompt, used = prompt_for(screen, gated, lines, mani)
    os.makedirs(RAW, exist_ok=True)
    base = os.path.join(RAW, gates.safe_name(screen))
    open(base + ".prompt.txt", "w", encoding="utf-8").write(prompt)
    if dry:
        return {"screen": screen, "chars": len(prompt), "lines": len(gated["gates"] if gate else gated)}
    response = f"{base}.{subject[:12]}.{k}.response.txt" if k and subject else base + ".response.txt"
    if from_response:
        text = open(response, encoding="utf-8").read(); meta = {}
    else:
        text, meta = call_model(prompt, model, system=SYSTEM, kind="screen", subject=screen)
        open(response, "w", encoding="utf-8").write(text)
    blocks = re.findall(r"```(?:yaml)?\s*\n(.*?)```", text, re.S)
    doc = yaml.safe_load(blocks[-1] if blocks else text) or {}
    if gate:
        return {"screen": screen, "kind": "gate", "condition": gated["condition"],
                "lines": [g["id"] for _, g, _ in gated["gates"]], "inputs": [i["id"] for _, _, i in gated["gates"]],
                "verdict": str(doc.get("verdict", "UNPARSED")), "findings": doc.get("findings") or [],
                "prompt_sha": hashlib.sha256(prompt.encode()).hexdigest(),
                "subject_sha": gates.subject(gated, lines, encoded_english), "used": used,
                "cost": meta.get("cost_usd") or 0, "model": ", ".join(meta.get("model_reported", [])),
                "date": datetime.date.today().isoformat(), "system_sha": SYSTEM_SHA,
                "response": os.path.relpath(response, ROOT), **_reason()}
    sline = lines[screen][1]
    return {"screen": screen, "question": sline["expr"]["source"], "lines": [l["id"] for _, l, _ in gated],
            "verdict": str(doc.get("verdict", "UNPARSED")), "findings": doc.get("findings") or [],
            "prompt_sha": hashlib.sha256(prompt.encode()).hexdigest(), "subject_sha": screen_subject(screen, gated, lines, mani),
            "used": used, "cost": meta.get("cost_usd") or 0, "model": ", ".join(meta.get("model_reported", [])),
            "date": datetime.date.today().isoformat(), "system_sha": SYSTEM_SHA, "response": os.path.relpath(response, ROOT),
            **_reason()}


SYSTEM_SHA = hashlib.sha256(SYSTEM.encode()).hexdigest()
# The fields of one sample; the others describe the unit and are kept once on its record.
SAMPLE_FIELDS = ("verdict", "findings", "prompt_sha", "system_sha", "cost", "model", "date", "response", "rerun_reason")
VERDICTS = ("COVERS", "NARROW", "WIDE", "SOURCE", "UNCLEAR")


def _reason():
    return {"rerun_reason": os.environ[spend.REASON_ENV]} if os.environ.get(spend.REASON_ENV) else {}


def read_records(path):
    """{unit: record} of a screen_review.json in the sampled format (samples.py)."""
    if not os.path.exists(path):
        return {}
    rows = json.load(open(path, encoding="utf-8"))
    legacy = [r["screen"] for r in rows if "samples" not in r]
    if legacy:
        sys.exit(f"{path}: {len(legacy)} record(s) in the single-review format ({', '.join(legacy[:5])}); "
                 "the file predates sampled reviews")
    return {r["screen"]: r for r in rows}


def as_sample(flat):
    """(unit fields, sample) of run_one's flat record. A verdict outside VERDICTS is an unparsed sample."""
    unit = {k: v for k, v in flat.items() if k not in SAMPLE_FIELDS}
    smp = {k: flat[k] for k in SAMPLE_FIELDS if k in flat}
    if smp.get("verdict") not in VERDICTS:
        smp["parse_error"] = True
    return unit, smp


def plan(sc, lines, mani, records, asked, force, price, model):
    """One entry per selected unit: {screen, subject, n, note, jobs}, as completeness_review.plan."""
    out = []
    for key, unit in sc.items():
        subject = subject_of(key, unit, lines, mani)
        rec = records.get(key)
        n, beyond = samples.wanted(rec, subject, asked)
        entry = {"screen": key, "unit": unit, "subject": subject, "jobs": []}
        if n == 0:
            entry["note"] = "satisfied: its current subject has the milestone's samples"
        elif beyond and not force:
            entry["note"] = (f"refused: {n} sample(s) would go beyond the milestone's {samples.SAMPLES_PER_MILESTONE}; "
                             "--force-rerun REASON runs them")
        else:
            first = len(rec["samples"]) + 1 if rec and rec.get("subject_sha") == subject else 1
            chars = len(prompt_for(key, unit[1], lines, mani)[0])
            usd = spend.estimate(chars, "screen_review.py", model, price)
            entry["jobs"] = [{"kind": "screen", "form": key, "k": k, "run": True, "usd": usd} for k in range(first, first + n)]
            entry["note"] = f"{n} sample(s) from #{first}"
        out.append(entry)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--screens"); ap.add_argument("--gates-only", action="store_true", help="review only the choose-guard gates")
    ap.add_argument("--dry-run", action="store_true", help="plan and estimate; call no model")
    ap.add_argument("--samples", type=int, metavar="K", help="run K samples per unit (default: those the milestone still needs)")
    ap.add_argument("--force-rerun", metavar="REASON", help="run samples beyond the milestone; the reason is recorded")
    ap.add_argument("--approve-cost", metavar="DOLLARS", type=float,
                    help=f"run although the estimate exceeds the ${spend.COST_GATE_USD:.2f} gate; at least the estimate")
    ap.add_argument("--jobs", type=int, default=6); ap.add_argument("--model", default="claude-opus-5-5")
    a = ap.parse_args()
    if a.force_rerun is not None and not a.force_rerun.strip():
        ap.error("--force-rerun needs a reason")
    lines = load_lines(); mani = manifest(); sc = units(lines)
    if a.gates_only:
        sc = {k: v for k, v in sc.items() if k.startswith("gate:")}
    if a.screens:
        want = a.screens.split(",")
        missing = [w for w in want if w not in sc]
        if missing:
            sys.exit(f"unknown screen(s): {', '.join(missing)}")
        sc = {k: v for k, v in sc.items() if k in want}
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "screen_review.json")
    records = read_records(path)
    planned = plan(sc, lines, mani, records, a.samples, a.force_rerun, spend.prices(), a.model)
    jobs = [j for e in planned for j in e["jobs"]]
    for e in planned:
        print(f"{e['screen']:40s} {e['note']}" + (f"  ~${sum(j['usd'] or 0 for j in e['jobs']):.2f}" if e["jobs"] else ""))
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
    by_key = {e["screen"]: e for e in planned if e["jobs"]}
    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        results = list(ex.map(lambda j: (j, run_one(j["form"], by_key[j["form"]]["unit"][1], lines, mani, a.model, False, False,
                                                     j["k"], by_key[j["form"]]["subject"])), jobs))
    for key, e in by_key.items():
        rec = records.get(key)
        if not rec or rec.get("subject_sha") != e["subject"]:
            rec = records[key] = {"screen": key, "subject_sha": e["subject"], "samples": []}
        for j, flat in sorted([r for r in results if r[0]["form"] == key], key=lambda r: r[0]["k"]):
            unit, smp = as_sample(flat)
            rec.update({k: v for k, v in unit.items() if k != "subject_sha"})
            rec["samples"].append(smp)
    json.dump(sorted(records.values(), key=lambda r: r["screen"]), open(path, "w"), indent=1, ensure_ascii=False)
    done = [as_sample(f)[1] for _, f in results]
    print(f"{len(done)} sample(s); verdicts: " + ", ".join(f"{v} {sum(1 for d in done if d['verdict'] == v)}"
                                                          for v in sorted({d["verdict"] for d in done}))
          + f"; cost {sum(d['cost'] for d in done):.2f}")


if __name__ == "__main__":
    main()
