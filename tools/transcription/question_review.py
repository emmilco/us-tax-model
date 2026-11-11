#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Question review: an isolated model judges each interview question against the tax text of the lines that use its
answer (docs/2026-11-10_question_review_design.md).

A unit is one input line of the jurisdiction (the question). Its prompt gives the question as the filer reads it (the
interview's prompt and help, from the built profiles), its type and accepted values, its label, note and linked
ambiguity entries, the gate it is asked behind, every line that reads it with its rendered English (and every refusal
it gates), the printed lines the answer reaches through helpers, and the archived pages the question and those lines
cite. The reviewer is asked whether an ordinary filer's truthful answer is the value the reading lines need: MATCH,
or the most serious of NARROW, WIDE, WRONG_FIGURE, TYPE (a sign, bound, date, rate or choice the type does not fit)
and UNCLEAR. A question read by more than BRIEF_READERS lines lists its readers by label only, with the pages of the
question's own citation.

    question_review.py [--inputs a,b] [--samples K] [--force-rerun REASON] [--approve-cost DOLLARS] [--dry-run]
                       [--jobs 6] [--model M]
    question_review.py --measure [--inputs a,b] [--by-form] [--write-prompts DIR] [--json PATH]
    question_review.py --coverage [--json PATH]
    question_review.py --self-test

Sampled standing review (samples.py): logged per form in reviews/<year>/questions/<form>.json, one record per question
holding its subject (`subject`: the question's line, interview wording and help, and each direct reader's line and
English; not the prompt's text, the archived pages, the gate condition or the reached lines) and the samples run
against it, each with its verdict, findings, prompt hash, model and cost; rulings per sample in
reviews/<year>/questions/rulings.json under "unruled:<input>#<k>" with the record's subject_sha. A run gives each
selected question the samples its current subject still needs this milestone; samples beyond it need --force-rerun
REASON, and a run estimated above the owner's gate needs --approve-cost (spend.py). Between releases a question whose
subject changed is due, not failed (check_questions.py). Each call is one fixed-prompt call to the selected model with
no tools, logged in the cost ledger as kind `question` (transcribe.call_model). Raw prompts and replies go to
.transcription/questions/ (.transcription/ny/questions/ with --jurisdiction ny).

--measure builds and prices every selected unit's prompt whatever its records hold; --by-form also prices one prompt
per form. --coverage lists, per input, which existing reviews see its wording and whether they judge it. Neither
calls a model. Every mode reads canonical/ (the interview profiles) and rendered/, and refuses to run unless both are what the
sources build and render to (tools/build_fresh.py).
"""
import argparse
import datetime
import functools
import glob
import hashlib
import json
import os
import re
import statistics
import sys
from concurrent.futures import ThreadPoolExecutor

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from taxyear import Y  # noqa: E402
import jurisdiction  # noqa: E402
from structured_text import indent_rest, continued  # noqa: E402
from transcribe import ROOT, manifest, excerpt_for, call_model  # noqa: E402
import samples  # noqa: E402
import spend  # noqa: E402

OUT = str(jurisdiction.ypath("reviews", Y, "questions"))
RAW = os.path.join(ROOT, ".transcription", *(["ny"] if jurisdiction.NY else []), "questions")
KIND = "question"
TOOL = "question_review.py"
SYSTEM = jurisdiction.system("You review the questions a tax tool asks a filer against the tax text each question "
                             "stands in for. You have no tools and no other sources. Output only the YAML requested.")
SYSTEM_SHA = hashlib.sha256(SYSTEM.encode()).hexdigest()
VERDICTS = ("MATCH", "NARROW", "WIDE", "WRONG_FIGURE", "TYPE", "UNCLEAR")
# The fields of one sample; the others describe the question and are kept once on its record.
SAMPLE_FIELDS = ("verdict", "findings", "prompt_sha", "system_sha", "model", "cost", "date", "response", "rerun_reason")
PRICE_PROXY = "screen_review.py"   # the ledger tool whose fitted price stands in while this tool has no calls of its own
BRIEF_READERS = 20                 # above this many readers, readers by label only and the question's own pages
RENDER_HELPERS = {"(helper)", "(gate)", "(computed helper)", "(question)", "(status)"}   # render_compare.HELPER_MARKERS


# ---------- the model of the forms ----------

def is_input(line):
    return (line.get("expr") or {}).get("op") == "input"


def refs(node, out=None):
    """Every string in an expression that can name a line (gates.refs, without its imports)."""
    out = set() if out is None else out
    if isinstance(node, str):
        out.add(node)
    elif isinstance(node, list):
        for n in node:
            refs(n, out)
    elif isinstance(node, dict):
        for k, v in node.items():
            if k not in ("cite", "source", "label", "op", "ref", "def", "line", "const", "param"):
                refs(v, out)
    return out


def readers(lines):
    """{input id: [(doc, reading line, how)]}: each line whose expression reads the input ("operand"), whose refusal
    names it as its gate ("refusal gate"), or whose values-sheet condition reads it ("shown_when")."""
    inputs = {i for i, (_, l) in lines.items() if is_input(l)}
    out = {i: [] for i in inputs}
    for lid, (doc, l) in sorted(lines.items()):
        for i in sorted(refs(l.get("expr") or {}) & inputs - {lid}):
            out[i].append((doc, l, "operand"))
        for r in l.get("refuses") or []:
            for i in sorted(refs(r.get("when")) & inputs):
                out[i].append((doc, l, "refusal gate"))
        if l.get("shown_when"):
            for i in sorted(refs(l["shown_when"]) & inputs):
                out[i].append((doc, l, "shown_when"))
    return out


def printed_reached(inp, lines, max_lines=8):
    """[(doc, line)]: the printed lines the input's value reaches through helper lines (operand reads only), nearest
    first, at most `max_lines`. A printed direct reader is listed with the readers already, so only lines beyond a
    helper are returned: they say which form line a helper-only question finally feeds."""
    users = {}
    for lid, (doc, l) in lines.items():
        for r in refs(l.get("expr") or {}) - {lid}:
            users.setdefault(r, []).append(lid)
    out, seen, frontier = [], {inp}, [u for u in sorted(users.get(inp, []))]
    while frontier and len(out) < max_lines:
        nxt = []
        for lid in frontier:
            if lid in seen or lid not in lines:
                continue
            seen.add(lid)
            doc, l = lines[lid]
            if not str(l.get("printed", "(")).startswith("("):
                if lid not in users.get(inp, []):
                    out.append((doc, l))
                continue
            nxt.extend(sorted(users.get(lid, [])))
        frontier = nxt
    return out[:max_lines]


def type_text(line, enum_values):
    """The accepted values of an input as the reviewer reads them."""
    t = line["type"]
    if t == "Bool":
        return "Bool: yes or no"
    if t == "NonNegDollars":
        return "NonNegDollars: an amount in dollars and cents, zero or more"
    if t == "Dollars":
        return "Dollars: an amount in dollars and cents, which may be negative"
    if t == "Count":
        return "Count: a whole number, zero or more, with no upper bound"
    m = re.match(r"Enum\((.+)\)", t)
    if m:
        vals = enum_values.get(m.group(1))
        return f"Enum {m.group(1)}: one of " + (", ".join(vals) if vals else "(values not found)")
    return t


# ---------- the prompt ----------

def reader_items(inp, reading, english, brief):
    """The prompt's list of the lines that use the answer. `brief`: each by its label only."""
    items = []
    for rdoc, l, how in reading:
        if how == "refusal gate":
            for r in l.get("refuses") or []:
                if inp in refs(r.get("when")):
                    head = (f"- Line `{l['id']}` (document {rdoc}, printed {l['printed']}) refuses when the answer "
                            f"makes its gate hold: {r['form']}")
                    items.append(head if brief else
                                 f"{head} — {indent_rest(r.get('remedy', ''), '    ')}\n"
                                 f"  Refusal cites: {r['cite']['doc']} {indent_rest(r['cite']['locator'], '    ')}")
            continue
        role = "is shown on the values sheet only when" if how == "shown_when" else "reads the answer"
        head = f"- Line `{l['id']}` (document {rdoc}, printed {l['printed']}) {role}: {indent_rest(l['label'], '    ')}"
        items.append(head if brief else
                     f"{head}\n  Computed as: {indent_rest(english(rdoc, l['id']), '    ')}\n"
                     f"  Cited: {l['cite']['doc']} {indent_rest(l['cite']['locator'], '    ')}")
    return items


def build_prompt(inp, doc, line, wording, ambiguities, reading, gate_text, enum_values, english, excerpt, reached=(),
                 brief=False):
    """The review prompt of one question. `wording` is {"prompt", "help", "cite"} as the interview shows it, or None
    when no profile asks the input; `reading` the readers of the input; `english(doc, id)` a line's rendered English;
    `brief` lists the readers by label only (the excerpt then holds the question's own pages)."""
    asked = (f"Question (input `{inp}`, document {doc}): {indent_rest(wording['prompt'], '  ')}"
             + (f"\nHelp shown with it: {indent_rest(wording['help'], '  ')}" if wording.get("help") else "")
             if wording else
             f"Question text (input `{inp}`, document {doc}; no interview profile asks it): "
             f"{indent_rest(line['expr'].get('source', ''), '  ')}")
    facts = [f"Accepted answer: {type_text(line, enum_values)}", f"Label: {line['label']}",
             f"Question cites: {line['cite']['doc']} {indent_rest(line['cite']['locator'], '  ')}"]
    if wording and wording.get("cite") and wording["cite"].get("locator") != line["cite"]["locator"]:
        facts.append(f"Interview cites: {wording['cite']['doc']} {indent_rest(wording['cite']['locator'], '  ')}")
    if line.get("note"):
        facts.append(f"Note: {indent_rest(line['note'], '  ')}")
    for a in ambiguities:
        facts.append(f"Recorded reading {a['id']}: {indent_rest(str(a.get('text_at_issue', '')).strip(), '  ')} "
                     f"Chosen: {indent_rest(str(a.get('chosen', '')).strip(), '  ')}")
    gate = (f"\nThe question is asked only when this holds; otherwise it is not asked and its value is zero, "
            f"no or the else value of its gate (the gate is reviewed separately):\n  {indent_rest(gate_text, '  ')}\n"
            if gate_text else "")
    items = reader_items(inp, reading, english, brief)
    if brief:
        items.insert(0, f"({len(reading)} lines use the answer. They are listed by label only, and the tax text below "
                        "is the question's own citation; judge the question against that text and these labels.)")
    if reached:
        items.append("Through the lines above, the answer reaches these form lines:")
        items.extend(f"- `{l['id']}` (document {rdoc}, printed {l['printed']}): {indent_rest(l['label'], '    ')}; "
                     f"cited {l['cite']['doc']} {indent_rest(l['cite']['locator'], '    ')}" for rdoc, l in reached)
    return jurisdiction.preface(f"""A tax preparation tool asks a filer the question below and uses the answer, exactly as given,
in the lines listed after it. The question is right only if an ordinary filer, reading it with
its help and answering truthfully, gives the value those lines need under the tax text below:
the same set of situations (for a yes/no question), the same amount, of the same people, time
frame and kind (for an amount), the same choice (for a list of answers).

# The question

{asked}
{chr(10).join(facts)}
{gate}
# The lines that use the answer

{chr(10).join(items) if items else "(no line reads it)"}

# Your task

Read the tax text below. Report:
- NARROW: a situation in which the lines need a yes, an amount or a choice that a filer
  answering the question truthfully would not give (a condition, alternative, person, time
  frame or source the wording leaves out). Quote the tax text and say what the wording misses.
- WIDE: a situation in which a truthful answer brings in a yes, an amount or a choice the lines
  must not have (an amount counted twice or counted elsewhere, a broader category, another
  year). Quote the question and the tax text.
- WRONG_FIGURE: the question asks for another figure than the one the lines need (another box,
  line or worksheet result, before or after an adjustment, gross for net, per person for
  combined). Quote both.
- TYPE: the accepted answer does not fit what the text allows: a sign, a bound (months 0 to 12,
  a percentage, a count with a maximum), a date or a rate taken as a count, a choice missing
  from the list. Give the bound or value set the text states.
- UNCLEAR: wording an ordinary filer could reasonably read two ways that give different values.
Do not report style, or a situation that a listed refusal or the gate already handles.

# Output

Return ONLY a YAML document of the form

verdict: "MATCH | NARROW | WIDE | WRONG_FIGURE | TYPE | UNCLEAR"
findings:
  - kind: "NARROW | WIDE | WRONG_FIGURE | TYPE | UNCLEAR"
    situation: "<one sentence>"
    source_text: "<short quote with document and page>"
    why: "<one or two sentences>"
    bound: "<for TYPE: the range or value set the text states, else empty>"

The verdict is the most serious finding's kind, in the order listed, or MATCH with an empty list.
No prose before or after the YAML.

# Tax text (archived snapshots; page markers show document, revision and page)

{excerpt}
""")


def subject(inp, lines, reading, wording, english):
    """The question's subject hash: what its review judges. The question's line (wording, type, label, note, ambiguity
    ids, citation), the interview's prompt, help and citation, and each direct reader's line, how it reads the answer,
    and its English. The prompt's own text, the archived pages, the gate condition (reviewed as its gate) and the lines
    reached through helpers are not in it, so a prompt change applies at a question's next real change."""
    doc, line = lines[inp]
    body = {"doc": doc, "question": line, "wording": wording,
            "readers": [{"doc": rdoc, "line": l, "how": how,
                         "english": None if how == "refusal gate" else english(rdoc, l["id"])} for rdoc, l, how in reading]}
    return hashlib.sha256(json.dumps(body, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


# ---------- coverage by the existing reviews ----------

def coverage(lines, screen_keys, gate_units, render_judged):
    """{input: {review: "judged" | "context"}}. judged: the review asks a model whether this question's wording is
    right; context: a prompt shows the wording while judging something else. Reviews: render (a judged line of its
    form's render review: a printed input, or any input of a form with no printed lines), screen (a refusal-gate screen
    of screen_review.py), gate (the condition of a choose-guard gate, judged by screen_review.py and
    false_no_review.py), gated (the gated question of a gate, shown in the gate's prompts), completeness (every input,
    listed as QUESTION in its form's prompt), transcription (every input, given as the form's input interface)."""
    out = {}
    cond = {u["condition"] for u in gate_units.values() if u["condition"]}
    gated = {i["id"] for u in gate_units.values() for _, _, i in u["gates"]}
    for lid, (doc, l) in lines.items():
        if not is_input(l) or not jurisdiction.mine(doc):
            continue
        c = {"completeness": "context", "transcription": "context"}
        if lid in render_judged:
            c["render"] = "judged"
        if lid in screen_keys:
            c["screen"] = "judged"
        if lid in cond:
            c["gate"] = "judged"
        if lid in gated:
            c["gated"] = "context"
        out[lid] = c
    return out


def render_judged_inputs(lines, form_docs):
    """The inputs a whole render review judges (render_compare._judged_lines): printed inputs, or every input of a
    form whose lines are all helpers."""
    out = set()
    for doc_id, doc_lines in form_docs.items():
        printed = [l for l in doc_lines if str(l.get("printed")) not in RENDER_HELPERS]
        for l in (printed or doc_lines):
            if is_input(l):
                out.add(l["id"])
    return out


def summarize_coverage(cov):
    judged_by = {}
    for i, c in cov.items():
        key = "+".join(sorted(k for k, v in c.items() if v == "judged")) or "none"
        judged_by[key] = judged_by.get(key, 0) + 1
    ctx_gated = sum(1 for c in cov.values() if "gated" in c and not any(v == "judged" for v in c.values()))
    return {"inputs": len(cov), "judged_by": dict(sorted(judged_by.items(), key=lambda kv: -kv[1])),
            "not_judged": sum(1 for c in cov.values() if not any(v == "judged" for v in c.values())),
            "not_judged_but_shown_in_a_gate_prompt": ctx_gated}


# ---------- type suspects (T-253), mechanical ----------

SUSPECT = [("Count", r"\b(date|percent|percentage|rate|ratio)\b", "a Count whose question asks for a date, percent or rate"),
           ("Count", r"\bmonths?\b", "a month count: bounded 0 to 12 (or to the months of the year)"),
           ("Dollars", r".", "a signed amount: check that the text allows a negative entry")]


def type_suspects(lines):
    """[(input, reason)]: mechanical flags for the TYPE half (T-253), each a lead for the reviewer, not a finding."""
    out = []
    for lid, (doc, l) in sorted(lines.items()):
        if not is_input(l) or not jurisdiction.mine(doc):
            continue
        text = (l["expr"].get("source", "") + " " + l["label"]).lower()
        for t, pat, why in SUSPECT:
            if l["type"] == t and re.search(pat, text):
                out.append((lid, why))
                break
    return out


# ---------- glue to the repository ----------

def load():
    """(lines, form_docs, ambiguities) of the jurisdiction's forms and, in New York mode, the federal ones its lines
    read. A definition document (`def`: tax_on_amount, se, aqee, ...) is left out: its inputs are parameters its
    callers bind, not questions, and a caller's `bind` names the lines it passes."""
    lines, form_docs = {}, {}
    for d in jurisdiction.read_dirs("forms", Y):
        for path in sorted(glob.glob(os.path.join(str(d), "*.yaml"))):
            data = yaml.safe_load(open(path, encoding="utf-8"))
            doc = data.get("form")
            if not doc:
                continue
            form_docs[doc["id"]] = doc["lines"]
            for l in doc["lines"]:
                lines[l["id"]] = (doc["id"], l)
    amb = {}
    for reg in {str(jurisdiction.ROOT / "ambiguities" / f"{Y}.yaml"), str(jurisdiction.register_file(Y))}:
        if os.path.exists(reg):
            for e in (yaml.safe_load(open(reg, encoding="utf-8")) or {}).get("register", {}).get("entries", []):
                amb[e["id"]] = e
    return lines, form_docs, amb


def enum_catalog():
    """{enum name: [values]} from the year parameters (federal, and New York's in New York mode)."""
    out = {}
    for path in {str(jurisdiction.ROOT / "params" / f"{Y}.yaml"), str(jurisdiction.params_file(Y))}:
        if os.path.exists(path):
            data = yaml.safe_load(open(path, encoding="utf-8")) or {}
            for k, v in ((next(iter(data.values())) or {}).get("enums") or {}).items():
                out[k] = [str(x) for x in (v.get("values") if isinstance(v, dict) else v) or []]
    return out


def questions_of(root):
    """{input: {"prompt", "help", "cite"}} from the built interview profiles (the New York profile asks the federal
    questions too)."""
    out = {}
    for name in ("interview-full.json", "interview-ny.json"):
        path = os.path.join(root, "canonical", str(Y), name)
        if os.path.exists(path):
            for q in json.load(open(path, encoding="utf-8"))["questions"]:
                out.setdefault(q["input"], {"prompt": q["prompt"], "help": q.get("help", ""), "cite": q.get("cite")})
    return out


@functools.lru_cache(maxsize=None)
def _rendered(doc_id):
    path = os.path.join(str(jurisdiction.doc_dir("rendered", Y, doc_id)), doc_id + ".md")
    return open(path, encoding="utf-8").read() if os.path.exists(path) else ""


def english(doc_id, line_id):
    """A line's rendered English (screen_review.encoded_english, reading each rendering once)."""
    m = re.search(r"^## [^\n]*`" + re.escape(line_id) + r"`\n(.*?)(?=^## |\Z)", _rendered(doc_id), re.S | re.M)
    if not m:
        return "(no rendering)"
    enc = re.search(r"\*\*Encoded[^*]*\*\*:? ?(.*)", m.group(1))
    return (enc.group(1) + continued(m.group(1), enc.start())).strip() if enc else "(no rendering)"


def gate_texts_of(lines, english):
    """{gated input: the gate condition as its prompt states it}."""
    import gates
    out = {}
    for u in gates.units(lines).values():
        cond, _ = gates.describe(u, lines, english)
        for _, _, i in u["gates"]:
            out[i["id"]] = cond
    return out


class Ctx:
    """What every unit's prompt and subject are built from."""

    def __init__(self, lines, amb=None, enum_values=None, questions=None, gate_texts=None, english=english,
                 mani=None, form_docs=None):
        self.lines, self.amb, self.enum_values = lines, amb or {}, enum_values or {}
        self.questions, self.gate_texts, self.english = questions or {}, gate_texts or {}, english
        self.mani, self.form_docs = mani, form_docs or {}
        self.reading = readers(lines)

    @classmethod
    def load(cls):
        lines, form_docs, amb = load()
        return cls(lines, amb, enum_catalog(), questions_of(ROOT), gate_texts_of(lines, english), english, manifest(),
                   form_docs)

    def units(self):
        """The questions of the jurisdiction under review, in id order."""
        return [i for i, (d, l) in sorted(self.lines.items()) if is_input(l) and jurisdiction.mine(d)]

    def subject(self, inp):
        return subject(inp, self.lines, self.reading[inp], self.questions.get(inp), self.english)

    def brief(self, inp):
        return len(self.reading[inp]) > BRIEF_READERS

    def prompt(self, inp):
        """(prompt, pages used) of one question. A brief unit gets the pages of the question's own citation (and the
        interview's); otherwise those of its readers and the refusals it gates too."""
        doc, line = self.lines[inp]
        reading, brief = self.reading[inp], self.brief(inp)
        own = [line]
        if not brief:
            own += [l for _, l, how in reading if how != "refusal gate"]
            own += [{"cite": r["cite"], "expr": {}} for _, l, how in reading if how == "refusal gate"
                    for r in l.get("refuses") or [] if inp in refs(r.get("when"))]
        q = self.questions.get(inp)
        if q and q.get("cite") and q["cite"].get("doc"):
            own.append({"cite": {"doc": q["cite"]["doc"], "locator": q["cite"]["locator"]}, "expr": {}})
        excerpt, used = excerpt_for({"id": "question:" + inp, "lines": own}, self.mani)
        ids = [line["ambiguity"]] if isinstance(line.get("ambiguity"), str) else line.get("ambiguity") or []
        prompt = build_prompt(inp, doc, line, q, [self.amb[a] for a in ids if a in self.amb], reading,
                              self.gate_texts.get(inp, ""), self.enum_values, self.english, excerpt,
                              printed_reached(inp, self.lines), brief)
        return prompt, used


def dist(xs):
    xs = sorted(xs)
    if not xs:
        return {}
    q = lambda p: xs[min(len(xs) - 1, int(p * len(xs)))]
    return {"n": len(xs), "total": round(sum(xs), 2), "mean": round(statistics.mean(xs), 4), "median": round(q(0.5), 4),
            "p90": round(q(0.9), 4), "max": round(xs[-1], 4)}


# ---------- the review: records, plan, run ----------

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


def records():
    """{input: (form, record)} over every form's log."""
    out = {}
    for path in sorted(glob.glob(os.path.join(OUT, "*.json"))):
        if os.path.basename(path) == "rulings.json":
            continue
        log = json.load(open(path, encoding="utf-8"))
        for key, r in log.get("reviews", {}).items():
            out[key] = (log.get("form"), r)
    return out


def parse_reply(text):
    blocks = re.findall(r"```(?:yaml)?\s*\n(.*?)```", text, re.S)
    try:
        doc = yaml.safe_load(blocks[-1] if blocks else text) or {}
    except yaml.YAMLError:
        doc = {}
    return doc if isinstance(doc, dict) else {}


def run_one(inp, ctx, model, dry, from_response, k=None, subject_sha=None):
    """One review of a question (a flat record: the question's fields and the sample's, split by as_sample). Sample
    k's reply is kept as <input>.<subject>.<k>.response.txt; without k, as <input>.response.txt."""
    prompt, used = ctx.prompt(inp)
    os.makedirs(RAW, exist_ok=True)
    base = os.path.join(RAW, re.sub(r"[^A-Za-z0-9_.-]", "_", inp))
    write_text(base + ".prompt.txt", prompt)
    doc, line = ctx.lines[inp]
    if dry:
        return {"input": inp, "chars": len(prompt), "readers": len(ctx.reading[inp])}
    response = f"{base}.{subject_sha[:12]}.{k}.response.txt" if k and subject_sha else base + ".response.txt"
    if from_response:
        with open(response, encoding="utf-8") as f:
            text, meta = f.read(), {}
    else:
        text, meta = call_model(prompt, model, system=SYSTEM, kind=KIND, subject=inp)
        write_text(response, text)
    reply = parse_reply(text)
    out = {"input": inp, "form": doc, "type": line["type"], "readers": len(ctx.reading[inp]), "brief": ctx.brief(inp),
           "verdict": str(reply.get("verdict", "UNPARSED")), "findings": reply.get("findings") or [],
           "prompt_sha": hashlib.sha256(prompt.encode()).hexdigest(), "subject_sha": subject_sha or ctx.subject(inp),
           "used": used, "model": ", ".join(meta.get("model_reported", [])) or model, "cost": meta.get("cost_usd") or 0,
           "date": datetime.date.today().isoformat(), "system_sha": SYSTEM_SHA, "response": os.path.relpath(response, ROOT)}
    if os.environ.get(spend.REASON_ENV):
        out["rerun_reason"] = os.environ[spend.REASON_ENV]
    return out


def as_sample(flat):
    """(question fields, sample) of run_one's flat record. A verdict outside VERDICTS is an unparsed sample."""
    unit = {k: v for k, v in flat.items() if k not in SAMPLE_FIELDS and k not in ("input", "form")}
    smp = {k: flat[k] for k in SAMPLE_FIELDS if k in flat}
    if smp.get("verdict") not in VERDICTS:
        smp["parse_error"] = True
    return unit, smp


def write_results(results, subjects):
    """Merges each sample into its question's record in its form's log: a question whose subject changed starts a new
    record; other questions' records are kept."""
    by_form = {}
    for j, r in sorted(results, key=lambda x: x[0]["k"]):
        by_form.setdefault(r["form"], []).append(r)
    os.makedirs(OUT, exist_ok=True)
    for form, rs in sorted(by_form.items()):
        log = read_log(form)
        for r in rs:
            unit, smp = as_sample(r)
            rec = log["reviews"].get(r["input"])
            if not rec or rec.get("subject_sha") != subjects[r["input"]]:
                rec = log["reviews"][r["input"]] = {"subject_sha": subjects[r["input"]], "samples": []}
            rec.update({k: v for k, v in unit.items() if k != "subject_sha"})
            rec["samples"].append(smp)
        log["reviews"] = dict(sorted(log["reviews"].items()))
        with open(log_path(form), "w", encoding="utf-8") as f:
            json.dump(log, f, indent=1, ensure_ascii=False)
            f.write("\n")


def price_of(chars, model, price):
    """The estimate of one call: this tool's own ledger fit, else the screen review's (PRICE_PROXY)."""
    usd = spend.estimate(chars, TOOL, model, price)
    return usd if usd is not None else spend.estimate(chars, PRICE_PROXY, model, price)


def plan(inputs, ctx, recs, asked, force, price, model):
    """One entry per selected question: {input, subject, note, jobs}, as false_no_review.plan."""
    out = []
    for inp in inputs:
        sha = ctx.subject(inp)
        held = recs.get(inp)
        rec = held[1] if held and held[0] == ctx.lines[inp][0] else None
        n, beyond = samples.wanted(rec, sha, asked)
        entry = {"input": inp, "subject": sha, "jobs": []}
        if n == 0:
            entry["note"] = "satisfied: its current subject has the milestone's samples"
        elif beyond and not force:
            entry["note"] = (f"refused: {n} sample(s) would go beyond the milestone's {samples.SAMPLES_PER_MILESTONE}; "
                             "--force-rerun REASON runs them")
        else:
            first = len(rec["samples"]) + 1 if rec and rec.get("subject_sha") == sha else 1
            usd = price_of(len(ctx.prompt(inp)[0]), model, price)
            entry["jobs"] = [{"kind": KIND, "form": inp, "k": k, "run": True, "usd": usd} for k in range(first, first + n)]
            entry["note"] = f"{n} sample(s) from #{first}"
        out.append(entry)
    return out


def review(a, ctx):
    inputs = ctx.units()
    if a.inputs:
        wanted = a.inputs.split(",")
        unknown = [i for i in wanted if i not in inputs]
        if unknown:
            sys.exit("not a question of this jurisdiction: " + ", ".join(unknown))
        inputs = [i for i in inputs if i in wanted]
    planned = plan(inputs, ctx, records(), a.samples, a.force_rerun, spend.prices(), a.model)
    jobs = [j for e in planned for j in e["jobs"]]
    for e in planned:
        print(f"{e['input']:40s} {e['note']}" + (f"  ~${sum(j['usd'] or 0 for j in e['jobs']):.3f}" if e["jobs"] else ""))
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
    by_key = {e["input"]: e for e in planned if e["jobs"]}
    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        results = list(ex.map(lambda j: (j, run_one(j["form"], ctx, a.model, False, False, j["k"],
                                                     by_key[j["form"]]["subject"])), jobs))
    write_results(results, {k: e["subject"] for k, e in by_key.items()})
    done = [as_sample(r)[1] for _, r in results]
    print(f"{len(done)} sample(s); verdicts: " + ", ".join(f"{v} {sum(1 for d in done if d['verdict'] == v)}"
                                                          for v in sorted({d["verdict"] for d in done}))
          + f"; cost {sum(d['cost'] for d in done):.2f}")


def measure(a, ctx):
    """--measure: every selected unit's prompt built and priced, whatever its records hold (no model call)."""
    import families
    from transcribe import doc_pages
    want = ctx.units()
    if a.inputs:
        want = [i for i in want if i in set(a.inputs.split(","))]
    price = spend.prices()
    p = price.get((TOOL, families.family_of(a.model))) or price.get((PRICE_PROXY, families.family_of(a.model)))
    print(f"price: ${p[0]:.4f} per call + ${p[1] * 1e6:.2f} per million prompt chars" if p else "no ledger price")
    units, by_form = [], {}
    for inp in want:
        prompt, used = ctx.prompt(inp)
        usd = price_of(len(prompt), a.model, price)
        doc, line = ctx.lines[inp]
        units.append({"input": inp, "form": doc, "type": line["type"], "chars": len(prompt),
                      "pages": sum(len(u["pages"]) for u in used), "readers": len(ctx.reading[inp]),
                      "brief": ctx.brief(inp), "usd": usd, "subject": ctx.subject(inp)})
        by_form.setdefault(doc, set()).update((u["doc"], pg) for u in used for pg in u["pages"])
        if a.write_prompts:
            os.makedirs(a.write_prompts, exist_ok=True)
            write_text(os.path.join(a.write_prompts, inp.replace("$", "_") + ".prompt.txt"), prompt)
    result = {"units": units, "per_question": {"usd": dist([u["usd"] or 0 for u in units]),
                                               "chars": dist([u["chars"] for u in units]),
                                               "pages": dist([u["pages"] for u in units])}}
    print(f"{len(units)} question unit(s); estimated ${sum(u['usd'] or 0 for u in units):.2f}")
    print("per question: " + json.dumps(result["per_question"]))
    if a.by_form:
        # One prompt per form: its questions' blocks (at most 4,000 characters each) and the union of their pages.
        # Estimated from the page union, not built.
        alt = []
        for form, pages in sorted(by_form.items()):
            text = sum(len(doc_pages(ctx.mani[d])[pg - 1]) for d, pg in pages)
            qs = [u for u in units if u["form"] == form]
            chars = text + sum(min(u["chars"], 4000) for u in qs)
            alt.append({"form": form, "questions": len(qs), "chars": chars, "usd": price_of(chars, a.model, price)})
        result["per_form_units"] = alt
        print(f"per-form alternative: {len(alt)} unit(s); estimated ${sum(f['usd'] or 0 for f in alt):.2f}; "
              "per form: " + json.dumps(dist([f["usd"] or 0 for f in alt])))
    return result


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--inputs", help="comma-separated input ids (default: every question of the jurisdiction)")
    ap.add_argument("--dry-run", action="store_true", help="plan and estimate; call no model")
    ap.add_argument("--samples", type=int, metavar="K", help="run K samples per question (default: those the milestone still needs)")
    ap.add_argument("--force-rerun", metavar="REASON", help="run samples beyond the milestone; the reason is recorded")
    ap.add_argument("--approve-cost", metavar="DOLLARS", type=float,
                    help=f"run although the estimate exceeds the ${spend.COST_GATE_USD:.2f} gate; at least the estimate")
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--measure", action="store_true", help="build and price every selected prompt; call no model")
    ap.add_argument("--coverage", action="store_true", help="which existing reviews see each input's wording")
    ap.add_argument("--by-form", action="store_true", help="with --measure: also price one prompt per form")
    ap.add_argument("--write-prompts", metavar="DIR", help="with --measure: write each prompt to DIR/<input>.prompt.txt")
    ap.add_argument("--json", metavar="PATH", help="with --measure or --coverage: write the measurements as JSON")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    if a.force_rerun is not None and not a.force_rerun.strip():
        ap.error("--force-rerun needs a reason")
    import build_fresh
    build_fresh.require(rendered=True)  # every mode reads canonical/ and each reader's rendered English
    ctx = Ctx.load()
    if not (a.measure or a.coverage):
        return review(a, ctx)
    result = {}
    if a.coverage:
        import screen_review
        import gates
        render_judged = render_judged_inputs(ctx.lines, {d: ls for d, ls in ctx.form_docs.items() if jurisdiction.mine(d)})
        cov = coverage(ctx.lines, set(screen_review.screens(ctx.lines)), gates.units(ctx.lines), render_judged)
        summ = summarize_coverage(cov)
        summ["not_in_any_profile"] = sorted(i for i in cov if i not in ctx.questions)
        summ["type_suspects"] = type_suspects(ctx.lines)
        result["coverage"] = {"summary": summ, "inputs": cov}
        print(json.dumps({k: v for k, v in summ.items() if k != "type_suspects"}, indent=1))
        print(f"type suspects (mechanical leads for T-253): {len(summ['type_suspects'])}")
        for i, why in summ["type_suspects"]:
            print(f"  {i}: {why}")
    if a.measure:
        result.update(measure(a, ctx))
    if a.json:
        json.dump(result, open(a.json, "w"), indent=1, ensure_ascii=False, default=list)


# ---------- self-test ----------

def _test_lines():
    cite = {"doc": "i1", "locator": "p. 1"}
    return {
        "f.any": ("f", {"id": "f.any", "printed": "(gate)", "label": "Any", "type": "Bool",
                        "expr": {"op": "input", "source": "Any?"}, "cite": cite}),
        "f.amt": ("f", {"id": "f.amt", "printed": "(question)", "label": "Amount", "type": "NonNegDollars",
                        "gated_by": "f.g", "expr": {"op": "input", "source": "How much?"}, "cite": cite}),
        "f.g": ("f", {"id": "f.g", "printed": "(helper)", "label": "Gate", "type": "NonNegDollars", "cite": cite,
                      "expr": {"op": "choose", "alternatives": [{"guard": {"op": "test", "eq": ["f.any", {"const": True}]},
                                                                  "then": "f.amt"}, {"guard": True, "then": "f.zero"}]}}),
        "f.l1": ("f", {"id": "f.l1", "printed": "1", "label": "Line 1", "type": "NonNegDollars", "cite": cite,
                       "expr": {"op": "sum", "of": ["f.g"]},
                       "refuses": [{"when": "f.screen", "form": "Form X", "remedy": "Use Form X.", "cite": cite}]}),
        "f.screen": ("f", {"id": "f.screen", "printed": "(question)", "label": "Screen", "type": "Bool",
                           "expr": {"op": "input", "source": "Anything unusual?"}, "cite": cite}),
        "f.months": ("f", {"id": "f.months", "printed": "2", "label": "Months", "type": "Count",
                           "expr": {"op": "input", "source": "Number of months covered"}, "cite": cite}),
    }


def self_test():
    import tempfile
    lines = _test_lines()
    rd = readers(lines)
    assert [(l["id"], h) for _, l, h in rd["f.amt"]] == [("f.g", "operand")], rd["f.amt"]
    assert ("f.l1", "refusal gate") in [(l["id"], h) for _, l, h in rd["f.screen"]]
    assert rd["f.months"] == []
    assert [l["id"] for _, l in printed_reached("f.amt", lines)] == ["f.l1"]
    assert printed_reached("f.months", lines) == []
    units = {"gate:f.any": {"key": "gate:f.any", "condition": "f.any", "gates": [("f", lines["f.g"][1], lines["f.amt"][1])]}}
    judged = render_judged_inputs(lines, {"f": [l for _, l in lines.values()]})
    assert judged == {"f.months"}, judged
    cov = coverage(lines, {"f.screen"}, units, judged)
    assert cov["f.any"].get("gate") == "judged" and cov["f.amt"].get("gated") == "context"
    assert cov["f.screen"]["screen"] == "judged" and cov["f.months"]["render"] == "judged"
    s = summarize_coverage(cov)
    assert s["not_judged"] == 1 and s["not_judged_but_shown_in_a_gate_prompt"] == 1, s
    assert type_suspects(lines) == [("f.months", "a month count: bounded 0 to 12 (or to the months of the year)")]
    eng = lambda d, i: f"English of {i}"
    p = build_prompt("f.amt", "f", lines["f.amt"][1], {"prompt": "How much did you get?", "help": "All of it."},
                     [{"id": "amb.x", "text_at_issue": "T", "chosen": "C"}], rd["f.amt"], "The filer is asked: Any?",
                     {}, eng, "PAGE TEXT")
    for want in ("How much did you get?", "Help shown with it: All of it.", "English of f.g", "amb.x",
                 "The filer is asked: Any?", "PAGE TEXT", "NonNegDollars", "TYPE"):
        assert want in p, want
    p2 = build_prompt("f.screen", "f", lines["f.screen"][1], None, [], rd["f.screen"], "", {}, eng, "")
    assert "no interview profile asks it" in p2 and "Form X — Use Form X." in p2
    # A brief prompt lists its readers by label only.
    p3 = build_prompt("f.screen", "f", lines["f.screen"][1], None, [], rd["f.screen"], "", {}, eng, "", brief=True)
    assert "listed by label only" in p3 and "Use Form X." not in p3 and "Form X" in p3

    # The subject follows the question, its wording and help, and its readers; not the gate or the prompt's text.
    w = {"prompt": "How much?", "help": "", "cite": None}
    base = subject("f.amt", lines, rd["f.amt"], w, eng)
    assert base == subject("f.amt", _test_lines(), readers(_test_lines())["f.amt"], dict(w), eng)
    assert base != subject("f.amt", lines, rd["f.amt"], dict(w, help="Include tips."), eng)
    assert base != subject("f.amt", lines, rd["f.amt"], w, lambda d, i: "other English")
    changed = _test_lines()
    changed["f.g"][1]["label"] = "Gate line"
    assert base != subject("f.amt", changed, readers(changed)["f.amt"], w, eng)
    regated = _test_lines()
    regated["f.any"][1]["expr"]["source"] = "Anything at all?"
    assert base == subject("f.amt", regated, readers(regated)["f.amt"], w, eng), "the gate condition is not in it"

    # A run, offline: the call is a stub; the records merge per form; currency follows the subject.
    g = globals()
    saved = {k: g[k] for k in ("RAW", "OUT", "excerpt_for", "call_model")}
    calls = []
    reply = ("verdict: NARROW\nfindings:\n  - kind: NARROW\n    situation: tips\n    source_text: x\n    why: y\n"
             "    bound: ''\n")
    with tempfile.TemporaryDirectory() as tmp:
        try:
            g.update(RAW=os.path.join(tmp, "raw"), OUT=os.path.join(tmp, "questions"),
                     excerpt_for=lambda form, mani: ("ARCHIVED", [{"doc": "i1", "pages": [1]}]),
                     call_model=lambda prompt, model, **kw: (calls.append(kw) or reply, {"model_reported": [model], "cost_usd": 0.07}))
            ctx = Ctx(lines, questions={"f.amt": w}, english=eng)
            assert ctx.units() == ["f.amt", "f.any", "f.months", "f.screen"]
            assert run_one("f.amt", ctx, "claude-opus-5-5", True, False)["chars"] > 0 and not calls
            sha = ctx.subject("f.amt")
            r = run_one("f.amt", ctx, "claude-opus-5-5", False, False, 1, sha)
            assert calls[-1] == {"system": SYSTEM, "kind": "question", "subject": "f.amt"}, calls
            assert (r["verdict"], r["form"], r["subject_sha"], r["cost"]) == ("NARROW", "f", sha, 0.07), r
            write_results([({"k": 1}, r)], {"f.amt": sha})
            recs = records()
            assert list(recs) == ["f.amt"] and recs["f.amt"][0] == "f"
            assert [x["verdict"] for x in recs["f.amt"][1]["samples"]] == ["NARROW"]
            # A satisfied subject plans no sample; another sample needs --force-rerun; a new subject plans one.
            price = {}
            e = plan(["f.amt"], ctx, recs, None, None, price, "claude-opus-5-5")[0]
            assert not e["jobs"] and e["note"].startswith("satisfied"), e
            assert plan(["f.amt"], ctx, recs, 1, None, price, "claude-opus-5-5")[0]["note"].startswith("refused")
            assert [j["k"] for j in plan(["f.amt"], ctx, recs, 1, "why", price, "claude-opus-5-5")[0]["jobs"]] == [2]
            ctx2 = Ctx(lines, questions={"f.amt": dict(w, help="Include tips.")}, english=eng)
            e = plan(["f.amt"], ctx2, recs, None, None, price, "claude-opus-5-5")[0]
            assert [j["k"] for j in e["jobs"]] == [1] and e["jobs"][0]["usd"] is None, e
            # An unparsed reply is a sample that does not count.
            reply = "not yaml: ["
            bad = run_one("f.months", ctx, "claude-opus-5-5", False, False, 1, ctx.subject("f.months"))
            assert as_sample(bad)[1].get("parse_error") is True
        finally:
            g.update(saved)
    print("question_review self-test: ok")


if __name__ == "__main__":
    sys.exit(main())
