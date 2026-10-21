#!/usr/bin/env python3
"""Screen review (T-008): an isolated model judges each scope screen against the instruction
text of every line it stands in for.

A screen is a yes/no input that one or more lines name as a refusal gate: answered yes, those
lines refuse with a citation; answered no, they are computed (usually with the source the screen
covers pinned to zero). A screen worded narrower than those lines lets an unsupported case through
as a zero; one worded wider refuses cases the tool computes. The review gives the model the
screen's question, each gated line with its encoded English (from rendered/) and its refusal text,
and the archived pages those lines cite, and asks for every case the wording misses or sweeps in.

    screen_review.py [--screens a,b] [--dry-run] [--from-response] [--jobs 6] [--model M]

One-time review, adjudicated in reviews/<year>/screens/screen_review.md (rerun it when the
sources are refetched). Each call is one fixed-prompt `claude -p` with no tools (fixed-prompt, curated input, no action surface).
"""
import argparse, datetime, glob, hashlib, json, os, re, sys
from concurrent.futures import ThreadPoolExecutor
import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from transcribe import ROOT, manifest, excerpt_for, call_model  # noqa: E402
from taxyear import Y  # noqa: E402

OUT = os.path.join(ROOT, "reviews", Y, "screens")
RAW = os.path.join(ROOT, ".transcription", "screens")
SYSTEM = ("You review the questions a tax tool asks a filer against the IRS text the questions stand in "
          "for. You have no tools and no other sources. Output only the YAML requested.")


def load_lines():
    lines = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "forms", Y, "*.yaml"))):
        d = yaml.safe_load(open(path, encoding="utf-8"))
        doc = d.get("form") or d.get("def")
        for l in doc["lines"]:
            lines[l["id"]] = (doc["id"], l)
    return lines


def encoded_english(doc_id, line_id):
    path = os.path.join(ROOT, "rendered", Y, doc_id + ".md")
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^## [^\n]*`" + re.escape(line_id) + r"`\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        return "(no rendering)"
    enc = re.search(r"\*\*Encoded[^*]*\*\*:? ?(.*)", m.group(1))
    return enc.group(1).strip() if enc else "(no rendering)"


def screens(lines):
    gates = {}
    for lid, (doc, l) in lines.items():
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
    return f"""A tax preparation tool asks the filer a yes/no screening question. If the filer answers YES, the
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
"""


def run_one(screen, gated, lines, mani, model, dry, from_response):
    sdoc, sline = lines[screen]
    pseudo = {"id": screen, "lines": [sline] + [l for _, l, _ in gated] + [{"cite": r["cite"], "expr": {}} for _, _, r in gated]}
    excerpt, used = excerpt_for(pseudo, mani)
    prompt = build_prompt(screen, sline, gated, excerpt)
    os.makedirs(RAW, exist_ok=True)
    base = os.path.join(RAW, screen)
    open(base + ".prompt.txt", "w", encoding="utf-8").write(prompt)
    if dry:
        return {"screen": screen, "chars": len(prompt), "lines": len(gated)}
    if from_response:
        text = open(base + ".response.txt", encoding="utf-8").read(); meta = {}
    else:
        text, meta = call_model(prompt, model, system=SYSTEM)
        open(base + ".response.txt", "w", encoding="utf-8").write(text)
    blocks = re.findall(r"```(?:yaml)?\s*\n(.*?)```", text, re.S)
    doc = yaml.safe_load(blocks[-1] if blocks else text) or {}
    return {"screen": screen, "question": sline["expr"]["source"], "lines": [l["id"] for _, l, _ in gated],
            "verdict": str(doc.get("verdict", "UNPARSED")), "findings": doc.get("findings") or [],
            "prompt_sha": hashlib.sha256(prompt.encode()).hexdigest(), "used": used, "cost": meta.get("cost_usd") or 0,
            "model": ", ".join(meta.get("model_reported", []))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--screens"); ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--from-response", action="store_true")
    ap.add_argument("--jobs", type=int, default=6); ap.add_argument("--model", default="claude-opus-5-5")
    a = ap.parse_args()
    lines = load_lines(); mani = manifest(); sc = screens(lines)
    if a.screens:
        sc = {k: v for k, v in sc.items() if k in a.screens.split(",")}
    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        results = list(ex.map(lambda kv: run_one(kv[0], kv[1], lines, mani, a.model, a.dry_run, a.from_response), sc.items()))
    if a.dry_run:
        for r in results:
            print(f"{r['screen']:32s} {r['lines']:3d} lines {r['chars']:8,d} chars")
        print(f"{len(results)} screens, {sum(r['chars'] for r in results):,} chars in all")
        return
    os.makedirs(OUT, exist_ok=True)
    json.dump(results, open(os.path.join(OUT, "screen_review.json"), "w"), indent=1, ensure_ascii=False)
    cost = sum(r["cost"] for r in results)
    print(f"{len(results)} screens; verdicts: " + ", ".join(f"{v} {sum(1 for r in results if r['verdict'] == v)}" for v in sorted({r['verdict'] for r in results})) + f"; cost {cost:.2f}")


if __name__ == "__main__":
    main()
