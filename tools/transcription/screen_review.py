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

    screen_review.py [--screens a,b] [--gates-only] [--dry-run] [--from-response] [--jobs 6] [--model M]

Standing review (T-088): a screen whose prompt hash (its question, the gated lines' English and refusals, and
the pages they cite) differs from its recorded review is stale in check-all (tools/transcription/check_screens.py)
and is rerun with --screens, which merges into reviews/<year>/screens/screen_review.json; findings are adjudicated
in reviews/<year>/screens/screen_review.md and ruled in reviews/<year>/screens/rulings.json. Each call is one fixed-prompt call to the selected model with no tools (fixed-prompt, curated input, no action surface): `claude` through `claude -p`, or an equal-authority peer through its transport (families.py; docs/2026-10-24_validation_policy.md).
"""
import argparse, datetime, glob, hashlib, json, os, re, sys
from concurrent.futures import ThreadPoolExecutor
import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from transcribe import ROOT, manifest, excerpt_for, call_model  # noqa: E402
from taxyear import Y  # noqa: E402
import jurisdiction  # noqa: E402  (--jurisdiction ny: the screens of New York lines; reviews/ny/<year>/screens/)
import gates  # noqa: E402

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
    return enc.group(1).strip() if enc else "(no rendering)"


def screens(lines):
    """{screen: [(doc, gated line, refusal)]}: every input that gates a line, with the lines of the jurisdiction
    under review it gates (in New York mode a federal screen gating New York lines is reviewed for those)."""
    gates = {}
    for lid, (doc, l) in lines.items():
        if not jurisdiction.mine(doc):
            continue
        for r in l.get("refuses", []) or []:
            gates.setdefault(r["when"], []).append((doc, l, r))
    return {g: v for g, v in sorted(gates.items()) if g in lines and lines[g][1]["expr"].get("op") == "input"}


def build_prompt(screen, sline, gated, excerpt):
    items = []
    for doc, l, r in gated:
        items.append(f"""- Line `{l['id']}` (document {doc}, printed {l['printed']}): {l['label']}
  Computed as (when the screen is answered no): {encoded_english(doc, l['id'])}
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


def prompt_for(screen, gated, lines, mani):
    """The review prompt of one screen and the pages it gives; its hash is the screen's review subject."""
    if screen.startswith("gate:"):
        return gate_prompt_for(gated, lines, mani)
    sdoc, sline = lines[screen]
    pseudo = {"id": screen, "lines": [sline] + [l for _, l, _ in gated] + [{"cite": r["cite"], "expr": {}} for _, _, r in gated]}
    excerpt, used = excerpt_for(pseudo, mani)
    return build_prompt(screen, sline, gated, excerpt), used


def run_one(screen, gated, lines, mani, model, dry, from_response):
    gate = screen.startswith("gate:")
    prompt, used = prompt_for(screen, gated, lines, mani)
    os.makedirs(RAW, exist_ok=True)
    base = os.path.join(RAW, gates.safe_name(screen))
    open(base + ".prompt.txt", "w", encoding="utf-8").write(prompt)
    if dry:
        return {"screen": screen, "chars": len(prompt), "lines": len(gated["gates"] if gate else gated)}
    if from_response:
        text = open(base + ".response.txt", encoding="utf-8").read(); meta = {}
    else:
        text, meta = call_model(prompt, model, system=SYSTEM, kind="screen", subject=screen)
        open(base + ".response.txt", "w", encoding="utf-8").write(text)
    blocks = re.findall(r"```(?:yaml)?\s*\n(.*?)```", text, re.S)
    doc = yaml.safe_load(blocks[-1] if blocks else text) or {}
    if gate:
        return {"screen": screen, "kind": "gate", "condition": gated["condition"],
                "lines": [g["id"] for _, g, _ in gated["gates"]], "inputs": [i["id"] for _, _, i in gated["gates"]],
                "verdict": str(doc.get("verdict", "UNPARSED")), "findings": doc.get("findings") or [],
                "prompt_sha": hashlib.sha256(prompt.encode()).hexdigest(),
                "subject_sha": gates.subject(gated, lines, encoded_english), "used": used,
                "cost": meta.get("cost_usd") or 0, "model": ", ".join(meta.get("model_reported", [])),
                "date": datetime.date.today().isoformat()}
    sline = lines[screen][1]
    return {"screen": screen, "question": sline["expr"]["source"], "lines": [l["id"] for _, l, _ in gated],
            "verdict": str(doc.get("verdict", "UNPARSED")), "findings": doc.get("findings") or [],
            "prompt_sha": hashlib.sha256(prompt.encode()).hexdigest(), "used": used, "cost": meta.get("cost_usd") or 0,
            "model": ", ".join(meta.get("model_reported", []))}


# The cost of a Claude screen review by prompt size: a least-squares fit to the cost ledger's 17 successful screen calls
# (claude-opus-5-5, reported cost, 16,808 to 115,466 prompt characters, $0.09 to $0.38): $0.048 a call plus $0.00295
# per thousand characters, within $0.03 of each call. Claude's price basis is the reported cost (prices.json), so this
# is a planning estimate; the ledger records what each call cost.
USD_PER_KCHAR = 0.00295
USD_PER_CALL = 0.048


def estimate_usd(chars):
    return USD_PER_CALL + USD_PER_KCHAR * chars / 1000


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--screens"); ap.add_argument("--gates-only", action="store_true", help="review only the choose-guard gates")
    ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--from-response", action="store_true")
    ap.add_argument("--jobs", type=int, default=6); ap.add_argument("--model", default="claude-opus-5-5")
    a = ap.parse_args()
    lines = load_lines(); mani = manifest(); sc = {k: v for k, (_, v) in units(lines).items()}
    if a.gates_only:
        sc = {k: v for k, v in sc.items() if k.startswith("gate:")}
    if a.screens:
        sc = {k: v for k, v in sc.items() if k in a.screens.split(",")}
    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        results = list(ex.map(lambda kv: run_one(kv[0], kv[1], lines, mani, a.model, a.dry_run, a.from_response), sc.items()))
    if a.dry_run:
        for r in results:
            print(f"{r['screen']:32s} {r['lines']:3d} lines {r['chars']:8,d} chars  ~${estimate_usd(r['chars']):.2f}")
        print(f"{len(results)} screens, {sum(r['chars'] for r in results):,} chars in all, ~${sum(estimate_usd(r['chars']) for r in results):.2f} at the "
              "Claude rate of the ledger's screen reviews (estimate_usd)")
        return
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "screen_review.json")
    # A run over some screens replaces their entries and keeps the others (the standing review, T-088).
    previous = json.load(open(path)) if os.path.exists(path) else []
    rerun = {r["screen"] for r in results}
    merged = [r for r in previous if r["screen"] not in rerun] + results
    json.dump(sorted(merged, key=lambda r: r["screen"]), open(path, "w"), indent=1, ensure_ascii=False)
    cost = sum(r["cost"] for r in results)
    print(f"{len(results)} screens; verdicts: " + ", ".join(f"{v} {sum(1 for r in results if r['verdict'] == v)}" for v in sorted({r['verdict'] for r in results})) + f"; cost {cost:.2f}")


if __name__ == "__main__":
    main()
