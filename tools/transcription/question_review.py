#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Question review, prototype: builds, for every interview question, the
prompt a reviewer would get to judge the question against the source text it stands in for, and prices a first full
pass. It calls no model: the review itself waits for the owner's decision on the design.

A unit is one input line (the question). Its prompt gives the question as the filer reads it (the interview's prompt
and help, from the built profiles), its type and accepted values, its label, note and linked ambiguity entries, the
gate it is asked behind, every line that reads it with its rendered English (and every refusal it gates), and the
archived pages the question and those lines cite. The reviewer is asked whether an ordinary filer's truthful answer is
the value the reading lines need (NARROW, WIDE, WRONG_FIGURE, TYPE, UNCLEAR, or MATCH).

    question_review.py --dry-run [--inputs a,b] [--by-form] [--model M] [--write-prompts DIR] [--json PATH]
    question_review.py --coverage [--json PATH]
    question_review.py --self-test

--dry-run builds every selected unit's prompt and prices it with spend.py. No ledger price exists for this tool, so
the estimate uses the screen review's fitted price (the closest kind: the same shape of prompt and reply), stated in
the output. --by-form also prices the alternative unit, one prompt per form holding all of its questions.
--coverage lists, per input, which existing reviews see its wording and whether they judge it (no model call).
Both read canonical/ (the interview profiles) and rendered/, so build and render first.
"""
import argparse
import glob
import hashlib
import json
import os
import re
import statistics
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from taxyear import Y  # noqa: E402
import jurisdiction  # noqa: E402
from structured_text import indent_rest  # noqa: E402

SYSTEM = jurisdiction.system("You review the questions a tax tool asks a filer against the tax text each question "
                             "stands in for. You have no tools and no other sources. Output only the YAML requested.")
VERDICTS = ("MATCH", "NARROW", "WIDE", "WRONG_FIGURE", "TYPE", "UNCLEAR")
PRICE_PROXY = "screen_review.py"   # the ledger tool whose fitted price stands in until this tool has calls of its own
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

def build_prompt(inp, doc, line, wording, ambiguities, reading, gate_text, enum_values, english, excerpt, reached=()):
    """The review prompt of one question. `wording` is {"prompt", "help", "cite"} as the interview shows it, or None
    when no profile asks the input; `reading` the readers of the input; `english(doc, id)` a line's rendered English."""
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
    items = []
    for rdoc, l, how in reading:
        if how == "refusal gate":
            for r in l.get("refuses") or []:
                if inp in refs(r.get("when")):
                    items.append(f"- Line `{l['id']}` (document {rdoc}, printed {l['printed']}) refuses when the answer "
                                 f"makes its gate hold: {r['form']} — {indent_rest(r.get('remedy', ''), '    ')}\n"
                                 f"  Refusal cites: {r['cite']['doc']} {indent_rest(r['cite']['locator'], '    ')}")
            continue
        role = "is shown on the values sheet only when" if how == "shown_when" else "reads the answer"
        items.append(f"- Line `{l['id']}` (document {rdoc}, printed {l['printed']}) {role}: "
                     f"{indent_rest(l['label'], '    ')}\n"
                     f"  Computed as: {indent_rest(english(rdoc, l['id']), '    ')}\n"
                     f"  Cited: {l['cite']['doc']} {indent_rest(l['cite']['locator'], '    ')}")
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


# ---------- glue to the repository (not used by the self-test) ----------

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


def unit_prompt(inp, lines, reading, mani, english, enum_values, amb, questions, gate_texts):
    from transcribe import excerpt_for
    doc, line = lines[inp]
    pseudo = {"id": "question:" + inp,
              "lines": [line] + [l for _, l, how in reading if how != "refusal gate"]
              + [{"cite": r["cite"], "expr": {}} for _, l, how in reading if how == "refusal gate"
                 for r in l.get("refuses") or [] if inp in refs(r.get("when"))]}
    q = questions.get(inp)
    if q and q.get("cite") and q["cite"].get("doc"):
        pseudo["lines"].append({"cite": {"doc": q["cite"]["doc"], "locator": q["cite"]["locator"]}, "expr": {}})
    excerpt, used = excerpt_for(pseudo, mani)
    ambs = [amb[a] for a in ([line["ambiguity"]] if isinstance(line.get("ambiguity"), str) else line.get("ambiguity") or [])
            if a in amb]
    prompt = build_prompt(inp, doc, line, q, ambs, reading, gate_texts.get(inp, ""), enum_values, english, excerpt,
                          printed_reached(inp, lines))
    return prompt, used


def gate_texts_of(lines, english):
    """{gated input: the gate condition as its prompt states it}."""
    import gates
    out = {}
    for u in gates.units(lines).values():
        cond, _ = gates.describe(u, lines, english)
        for _, _, i in u["gates"]:
            out[i["id"]] = cond
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


def dist(xs):
    xs = sorted(xs)
    if not xs:
        return {}
    q = lambda p: xs[min(len(xs) - 1, int(p * len(xs)))]
    return {"n": len(xs), "total": round(sum(xs), 2), "mean": round(statistics.mean(xs), 4), "median": round(q(0.5), 4),
            "p90": round(q(0.9), 4), "max": round(xs[-1], 4)}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="build and price every unit's prompt; call no model")
    ap.add_argument("--coverage", action="store_true", help="which existing reviews see each input's wording")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--inputs", help="comma-separated input ids (default: every input of the jurisdiction)")
    ap.add_argument("--by-form", action="store_true", help="also price one prompt per form")
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--write-prompts", metavar="DIR", help="with --dry-run: write each prompt to DIR/<input>.prompt.txt")
    ap.add_argument("--json", metavar="PATH", help="write the measurements as JSON")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not (a.dry_run or a.coverage):
        ap.error("this prototype only plans: pass --dry-run or --coverage (the review is not approved to run)")
    import screen_review
    import gates
    import spend
    from transcribe import manifest
    root = os.path.dirname(os.path.dirname(HERE))
    lines, form_docs, amb = load()
    enum_values = enum_catalog()
    english = screen_review.encoded_english
    result = {}
    if a.coverage:
        render_judged = render_judged_inputs(lines, {d: ls for d, ls in form_docs.items() if jurisdiction.mine(d)})
        cov = coverage(lines, set(screen_review.screens(lines)), gates.units(lines), render_judged)
        asked = questions_of(root)
        summ = summarize_coverage(cov)
        summ["not_in_any_profile"] = sorted(i for i in cov if i not in asked)
        summ["type_suspects"] = type_suspects(lines)
        result["coverage"] = {"summary": summ, "inputs": cov}
        print(json.dumps({k: v for k, v in summ.items() if k != "type_suspects"}, indent=1))
        print(f"type suspects (mechanical leads for T-253): {len(summ['type_suspects'])}")
        for i, why in summ["type_suspects"]:
            print(f"  {i}: {why}")
    if a.dry_run:
        mani = manifest()
        rd = readers(lines)
        questions = questions_of(root)
        gtexts = gate_texts_of(lines, english)
        want = [i for i, (d, l) in sorted(lines.items()) if is_input(l) and jurisdiction.mine(d)]
        if a.inputs:
            want = [i for i in want if i in set(a.inputs.split(","))]
        price = spend.prices()
        p = price.get((PRICE_PROXY, __import__("families").family_of(a.model)))
        print(f"price proxy: {PRICE_PROXY} fit = ${p[0]:.4f} per call + ${p[1] * 1e6:.2f} per million prompt chars"
              if p else f"no ledger price for {PRICE_PROXY}")
        units, by_form = [], {}
        for inp in want:
            prompt, used = unit_prompt(inp, lines, rd[inp], mani, english, enum_values, amb, questions, gtexts)
            usd = spend.estimate(len(prompt), PRICE_PROXY, a.model, price)
            pages = sum(len(u["pages"]) for u in used)
            units.append({"input": inp, "form": lines[inp][0], "type": lines[inp][1]["type"], "chars": len(prompt),
                          "pages": pages, "readers": len(rd[inp]), "usd": usd,
                          "subject": hashlib.sha256(prompt.encode()).hexdigest()})
            by_form.setdefault(lines[inp][0], set()).update((u["doc"], p) for u in used for p in u["pages"])
            if a.write_prompts:
                os.makedirs(a.write_prompts, exist_ok=True)
                open(os.path.join(a.write_prompts, inp.replace("$", "_") + ".prompt.txt"), "w", encoding="utf-8").write(prompt)
        result["units"] = units
        result["per_question"] = {"usd": dist([u["usd"] or 0 for u in units]), "chars": dist([u["chars"] for u in units]),
                                  "pages": dist([u["pages"] for u in units])}
        by = {}
        for u in units:
            f = by.setdefault(u["form"], {"form": u["form"], "questions": 0, "usd": 0.0, "chars": 0})
            f["questions"] += 1; f["usd"] += u["usd"] or 0; f["chars"] += u["chars"]
        result["per_form_of_question_units"] = sorted(by.values(), key=lambda f: -f["usd"])
        print(f"{len(units)} question unit(s); estimated ${sum(u['usd'] or 0 for u in units):.2f}")
        print("per question: " + json.dumps(result["per_question"]))
        if a.by_form:
            # One prompt per form: its questions' blocks (about 2,500 characters each, the prompt less its pages) and
            # the union of their pages. Estimated from the page union, not built.
            from transcribe import doc_pages
            alt = []
            for form, pages in sorted(by_form.items()):
                text = sum(len(doc_pages(mani[d])[p - 1]) for d, p in pages)
                qs = [u for u in units if u["form"] == form]
                chars = text + sum(min(u["chars"], 4000) for u in qs)
                alt.append({"form": form, "questions": len(qs), "chars": chars,
                            "usd": spend.estimate(chars, PRICE_PROXY, a.model, price)})
            result["per_form_units"] = alt
            print(f"per-form alternative: {len(alt)} unit(s); estimated ${sum(f['usd'] or 0 for f in alt):.2f}; "
                  "per form: " + json.dumps(dist([f["usd"] or 0 for f in alt])))
    if a.json:
        json.dump(result, open(a.json, "w"), indent=1, ensure_ascii=False, default=list)


# ---------- self-test ----------

def self_test():
    cite = {"doc": "i1", "locator": "p. 1"}
    lines = {
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
    p = build_prompt("f.amt", "f", lines["f.amt"][1], {"prompt": "How much did you get?", "help": "All of it."},
                     [{"id": "amb.x", "text_at_issue": "T", "chosen": "C"}], rd["f.amt"], "The filer is asked: Any?",
                     {}, lambda d, i: f"English of {i}", "PAGE TEXT")
    for want in ("How much did you get?", "Help shown with it: All of it.", "English of f.g", "amb.x",
                 "The filer is asked: Any?", "PAGE TEXT", "NonNegDollars"):
        assert want in p, want
    p2 = build_prompt("f.screen", "f", lines["f.screen"][1], None, [], rd["f.screen"], "", {},
                      lambda d, i: "", "")
    assert "no interview profile asks it" in p2 and "Form X — Use Form X." in p2
    print("question_review self-test: ok")


if __name__ == "__main__":
    main()
