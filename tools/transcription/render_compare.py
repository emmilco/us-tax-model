#!/usr/bin/env python3
"""Render comparison (spec 6.5): an isolated model reads the rendered English of every
printed line of one form against the archived IRS pages the form cites, and reports each
line whose restatement does not say what the text says. The model sees the rendering
(`rendered/<year>/<form>.md`, encoded English and refusal rules) and the IRS pages; never
the YAML or its expression trees.

    python3 tools/transcription/render_compare.py --form qdcg [--model M] [--dry-run] [--from-response]

Logs go to reviews/<year>/render/<form>.md (<form>.<family>.md for a model family other than
Claude: families.py); a MISMATCH or UNCLEAR line carries "Ruling: open" until ruled with
rule.py --kind render. Raw prompts and responses are kept under the git-ignored .transcription/
as <stem>.render.*.
"""
import argparse, datetime, hashlib, json, os, re, sys
from functools import cache
import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from transcribe import ROOT, RAW, manifest, excerpt_for, call_model, load_form, review_response, project_yaml  # noqa: E402
from taxyear import Y  # noqa: E402
import families  # noqa: E402
import rulings  # noqa: E402
import subjects  # noqa: E402

RENDERED = os.path.join(ROOT, "rendered", Y)
LOGS = os.path.join(ROOT, "reviews", Y, "render")
HELPER_MARKERS = {"(helper)", "(gate)", "(computed helper)", "(question)", "(status)"}
SYSTEM = ("You check whether plain-English restatements of IRS form and worksheet lines say what the IRS text "
          "says. You have no tools and no other sources. Output only the YAML requested.")
STATUSES = ("MATCH", "MISMATCH", "UNCLEAR")
PROMPT_POLICY = "render-source-comparison-v2"


def parse_rendered(form_id):
    """Every line of a rendered document: printed marker, id, type, label, encoded English, refusals."""
    text = open(os.path.join(RENDERED, form_id + ".md"), encoding="utf-8").read()
    entries = {}
    for sec in re.split(r"(?m)^## ", text)[1:]:
        head, _, body = sec.partition("\n")
        m = re.match(r"(.+?) — `([^`]+)`\s*$", head)
        if not m:
            continue
        enc = re.search(r"(?m)^- \*\*Encoded \((.+?)\):\*\* (.*)$", body)
        label = re.search(r"(?m)^- \*\*(?:IRS|Authored helper label):\*\* (.*)$", body)
        refusals = re.findall(r"(?m)^- \*\*Refusal:\*\* (.*?) Cite: ", body)
        shown_when = re.search(r"(?m)^- \*\*Shown on the values sheet only when:\*\* (.*?) \(`[^`]+`\)$", body)
        entries[m.group(2)] = {"printed": m.group(1), "id": m.group(2), "type": enc.group(1), "encoded": enc.group(2),
                               "label": label.group(1) if label else "", "refusals": refusals,
                               "shown_when": shown_when.group(1) if shown_when else None}
    return entries


_rendered_cache = {}


def rendered(form_id):
    if form_id not in _rendered_cache:
        _rendered_cache[form_id] = parse_rendered(form_id)
    return _rendered_cache[form_id]


@cache
def form_ids():
    return {f[:-3] for f in os.listdir(RENDERED) if f.endswith(".md")}


def helper_refs(text, form_id):
    """(form, label) pairs the restatement names as helpers; a word before `helper` is a
    form id only when a rendered document of that name exists."""
    out = []
    known = form_ids()
    for m in re.finditer(r'(?:\b([a-z0-9_]+) )?helper "([^"]+)"', text):
        fid = m.group(1) if m.group(1) in known else form_id
        out.append((fid, m.group(2)))
    return out


@cache
def def_titles():
    """Shared definitions by title ({title: def id}); a restatement invokes one as
    '"<output>" of <title>'."""
    out = {}
    forms_dir = os.path.join(ROOT, "forms", Y)
    for f in sorted(os.listdir(forms_dir)):
        if f.endswith(".yaml"):
            d = project_yaml(os.path.join(forms_dir, f))
            if isinstance(d, dict) and "def" in d:
                out[d["def"]["title"]] = d["def"]["id"]
    return out


def def_refs(text):
    """Ids of the shared definitions a restatement invokes."""
    return [did for title, did in def_titles().items() if f'" of {title}' in text]


def gate_refs(refusals):
    """Ids of the gate lines refusal rules name ("when sd.screen is true, ...")."""
    return [m.group(1) for r in refusals for m in re.finditer(r"when ([a-z0-9_]+\.[a-z0-9_.]+) is true", r)]


def field_refs(text):
    """Ids of the per-entry fields a collection sum adds ("Add person.ira_line6 over every
    confirmed person entry ...")."""
    return re.findall(r"\bAdd ([a-z0-9_]+\.[a-z0-9_]+) over every confirmed ", text)


@cache
def local_ref_pattern(marker):
    word = "column" if marker.startswith("(") else "line"
    return re.compile(rf'(?:(\b[a-z0-9_]+) )?\b{word} {re.escape(marker)}(?![a-zA-Z0-9_]|\.[0-9])')


def local_printed_refs(text, form_id):
    """Printed references within a glossary entry keep that entry's form scope.

    Collection fields such as person.credit refer to 'line eligible' and
    'line excess'; these are printed markers, not quoted helper labels.
    Explicit references to another form remain incoming amounts.
    """
    out = []
    known = form_ids()
    for entry in rendered(form_id).values():
        marker = entry["printed"]
        if marker in HELPER_MARKERS:
            continue
        for match in local_ref_pattern(marker).finditer(text):
            prefix = match.group(1)
            if prefix in known and prefix != form_id:
                continue
            out.append(entry["id"])
            break
    return out


def glossary(form_id, lines):
    """Helper values the judged lines refer to (by label within their form), the per-entry
    fields their collection sums add and the gate lines their refusals name (by id), followed
    transitively, each with its restatement."""
    seen, emitted, order, queue = set(), set(), [], []
    def refs_of(text, refusals, fid):
        # References in a record question describe supplied facts (often last
        # year's form), not dependencies of this year's computation.
        if text.startswith("Input —"):
            return ([("label", owner, lab) for owner, lab in helper_refs(" ".join(refusals), fid)]
                    + [("id", gid.split(".")[0], gid) for gid in gate_refs(refusals)])
        return ([("label", fid, lab) for fid, lab in helper_refs(text + " " + " ".join(refusals), fid)]
                + [("id", gid.split(".")[0], gid) for gid in gate_refs(refusals)]
                + [("id", f.split(".")[0], f) for f in field_refs(text)]
                + [("id", fid, ref) for ref in local_printed_refs(text, fid)]
                + [("def", did, did) for did in def_refs(text)])
    for l in lines:
        queue += refs_of(l["encoded"], l["refusals"], form_id)
    judged = {(form_id, l["id"]) for l in lines}
    while queue:
        kind, fid, key = queue.pop(0)
        if (kind, fid, key) in seen:
            continue
        seen.add((kind, fid, key))
        try:
            entries = rendered(fid)
        except FileNotFoundError:
            continue
        if kind == "label":
            matches = [e for e in entries.values() if e["label"] == key and e["printed"] in HELPER_MARKERS]
        elif kind == "def":
            matches = list(entries.values())  # every line of the invoked definition
        else:
            matches = [entries[key]] if key in entries else []
        for e in matches:
            if (fid, e["id"]) in judged or (fid, e["id"]) in emitted:
                continue
            emitted.add((fid, e["id"]))
            order.append((fid, e))
            queue += refs_of(e["encoded"], e["refusals"], fid)
    return order


def source_context(form_doc):
    """Cite the calculations actually exposed in the rendered glossary as well.

    Only their archived source text is supplied to the reviewer; source YAML
    expressions are used here to select parameter citations, never as output.
    Explicit incoming printed lines are not recursively expanded.
    """
    lines = list(form_doc["lines"])
    for fid, entry in glossary(form_doc["id"], judged_lines(form_doc)):
        if fid != form_doc["id"]:
            source = next(l for l in load_form(fid)["lines"] if l["id"] == entry["id"])
            lines.append(source)
    return {**form_doc, "lines": lines}


def referenced_lines(form_id, texts):
    """Printed lines of other forms that the texts name ("sb line 4", "sales column (e)"),
    with their IRS labels, so a cross-form reference can be read."""
    out = []
    joined = " ".join(texts)
    for fid in sorted(form_ids()):
        if fid == form_id:
            continue
        for e in rendered(fid).values():
            if e["printed"] in HELPER_MARKERS:
                continue
            word = "column" if e["printed"].startswith("(") else "line"
            if f"{fid} {word} {e['printed']}" in joined:
                out.append((fid, word, e))
    return out


def judged_lines(form_doc):
    """The lines the model judges: the printed lines, each keyed by its printed number; or,
    for a form whose lines are all helpers, every line keyed by its id within the form, label shown."""
    entries = rendered(form_doc["id"])
    printed = [entries[l["id"]] for l in form_doc["lines"] if l["id"] in entries and str(l["printed"]) not in HELPER_MARKERS]
    if printed:
        # A printed marker several lines share (a worksheet's repeated row columns)
        # is keyed by the line id so each row gets its own verdict.
        counts = {}
        for e in printed:
            counts[e["printed"]] = counts.get(e["printed"], 0) + 1
        out = []
        for e in printed:
            key = e["printed"] if counts[e["printed"]] == 1 else f'{e["printed"]} ({e["id"]})'
            out.append(dict(e, key=key, shown=f'printed "{key}"'))
        return out
    all_lines = [entries[l["id"]] for l in form_doc["lines"] if l["id"] in entries]
    local = lambda e: e["id"].split(".", 1)[1]
    return [dict(e, key=local(e), shown=f'{local(e)} helper "{e["label"]}"') for e in all_lines]


def build_prompt(form_doc, excerpt):
    fid = form_doc["id"]
    printed = judged_lines(form_doc)
    rows = []
    for e in printed:
        rows.append(f'- {e["shown"]} ({e["type"]}): {e["encoded"]}')
        if e.get("shown_when"):
            rows.append(f"    reported on this line only for an entry where: {e['shown_when']} (otherwise the line is left out for that entry)")
        for r in e["refusals"]:
            rows.append(f"    refusal: {r}")
    gl = []
    gloss = glossary(fid, printed)
    for gfid, e in gloss:
        where = "" if gfid == fid else f" (on {gfid})"
        if e["printed"] in HELPER_MARKERS:
            name = f'{e["id"]} "{e["label"]}"'
        elif gfid == fid:
            continue
        else:
            name = f'{gfid} line {e["printed"]} "{e["label"]}"'
        gl.append(f'- {name}{where} ({e["type"]}): {e["encoded"]}')
        for r in e["refusals"]:
            gl.append(f"    refusal: {r}")
    texts = [e["encoded"] + " " + " ".join(e["refusals"]) for e in printed] + [e["encoded"] + " " + " ".join(e["refusals"]) for _, e in gloss]
    refd = referenced_lines(fid, texts)
    if refd:
        gl += ["", "Lines of other forms named above, with the IRS wording of each:"]
        for rfid, word, e in refd:
            gl.append(f'- {rfid} {word} {e["printed"]}: "{e["label"]}"')
    return f"""You are checking whether a program's plain-English restatement of each printed line of an IRS form
or worksheet says what the IRS text says. Work ONLY from the IRS text provided below. Do not rely on
memory of the tax law or of any software; if the text does not say it, it is not evidence.

# The form

Form id: {fid}
Title: {form_doc['title']}
Tax year: {form_doc['tax_year']}

# Restated lines

Each line as the program restates it, with its value type and any refusal rule (a case the program
declines to compute, naming the form the filer must use instead). Amounts are dollars; a "line N" is
a line of this form unless another form's id precedes it. A value in quotes after the word helper is
one of the program's intermediate values; helpers are not printed on the IRS form. Where a line to
judge is itself a helper (keyed h1, h2, ...), its label states what the program means it to be and
the restatement is how it is computed; judge both against the text. Other helpers are defined in
the glossary. "Input" means the filer supplies the amount from the named record.

{chr(10).join(rows)}

# Glossary of helper values and gates

A gate named in a refusal ("when X is true") is listed by its id with its label and restatement.
Within a glossary entry, an unqualified line name belongs to the form named on that entry.

{chr(10).join(gl) if gl else '(none)'}

# What to decide

For each printed line, compare the restatement with what the IRS text says for that line: the line's
own words on the form or worksheet, and any instruction text for it in the pages given. Decide:

- MATCH: the restatement computes what the IRS line says, allowing for wording. A refusal or a
  helper may narrow a line to the cases the program supports; that is still a MATCH when the
  restatement is right within those cases and the refusal names what is excluded.
- MISMATCH: the restatement computes something different from the IRS line: a different operand,
  direction, rate, threshold, condition, rounding or omission that would change the value. Quote
  the IRS words that differ.
- UNCLEAR: the restatement cannot be judged from the IRS text given. Say what is missing.

Judge every line listed above, in order, exactly once, keyed exactly as shown in quotes after
"printed" (a printed number, or a marker qualified by a line id when rows share it) or by its helper name.

# Output

Return ONLY a YAML document of the form

lines:
  - key: "<printed number or helper name>"
    status: MATCH | MISMATCH | UNCLEAR
    reason: "<one or two sentences; for MISMATCH quote the IRS text that differs>"

No prose before or after the YAML.

# IRS text (archived snapshots; page markers show document, revision and page)

{excerpt}
"""


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
            raise ValueError("verdict must be a mapping")
        status = str(l.get("status", "")).strip().upper()
        key = str(l.get("key", l.get("printed", "")))
        if not key or key in out:
            raise ValueError(f"missing or duplicate verdict key: {key!r}")
        if status not in STATUSES:
            raise ValueError(f"invalid verdict for {key}: {status!r}")
        reason = l.get("reason")
        if not isinstance(reason, str) or not reason.strip():
            raise ValueError(f"verdict {key} has no reason")
        out[key] = {"status": status, "reason": reason.strip()}
    return out


def write_log(form_doc, model, prompt, used, printed, verdicts, raw_text, meta):
    os.makedirs(LOGS, exist_ok=True)
    fid = form_doc["id"]
    family = families.family_of(model)
    path = rulings.log_path("render", fid, family)
    results = []
    for e in printed:
        v = verdicts.get(e["key"])
        results.append({"printed": e["key"], "label": e["label"], "encoded": e["encoded"],
                        "status": v["status"] if v else "MISSING", "reason": v["reason"] if v else "the model returned no verdict for this line"})
    extra = sorted(set(verdicts) - {e["key"] for e in printed})
    counts = {k: sum(1 for r in results if r["status"] == k) for k in STATUSES + ("MISSING",)}
    out = [f"# Render comparison — {fid}", "",
           f"The rendered English of every printed line of `{form_doc['title']}` (`rendered/{Y}/{fid}.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).", "",
           "| field | value |", "| --- | --- |",
           f"| date | {datetime.date.today().isoformat()} |",
           f"| model requested | {model} |",
           f"| model reported | {', '.join(meta.get('model_reported', [])) or '-'} |",
           f"| prompt sha256 | {hashlib.sha256(prompt.encode()).hexdigest()} |",
           f"| prompt policy | {meta.get('prompt_policy', 'legacy-unrecorded')} |",
           f"| system sha256 | {meta.get('system_sha256', '-')} |",
           f"| reasoning effort | {meta.get('reasoning_effort') or 'provider default'} |",
           f"| output token budget | {meta.get('request_max_tokens') or 'transport default (65536 for DeepSeek)'} |",
           f"| subject sha256 | {subjects.current('render', fid, Y)} |",
           f"| lines judged | {len(results)} |",
           f"| match / mismatch / unclear / missing | {counts['MATCH']} / {counts['MISMATCH']} / {counts['UNCLEAR']} / {counts['MISSING']} |",
           f"| verdicts for lines not in the form | {', '.join(extra) if extra else 'none'} |", "",
           "## Source pages given to the model", "", "| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for u in used:
        out.append(f"| {u['doc']} | {u['revision']} | {', '.join(map(str, u['pages'])) or '-'} | {u['how']} | {u['text_sha256']} | {', '.join(map(str, u.get('cols_pages', []))) or '-'} | {u.get('cols_sha256', '-')} |")
    out += ["", "## Lines", ""]
    kept = rulings.kept("render", fid, family, context=rulings.review_context("render", "\n".join(out)))
    for r in results:
        out.append(f"### {r['printed']} — {r['label'][:90].rstrip()}")
        out.append(f"Status: **{r['status']}**")
        if r["status"] != "MATCH":
            out += ["", f"Restated: {r['encoded']}", "", f"Model: {r['reason']}", "",
                    kept.get((r["printed"], r["encoded"], r["reason"]), "Ruling: open"), ""]
        else:
            out += ["", f"Model: {r['reason']}", ""]
    out += ["## Raw response", "", "```yaml", raw_text.strip(), "```", ""]
    open(path, "w", encoding="utf-8").write("\n".join(out))
    return path, counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--form", required=True)
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--reasoning-effort", choices=("low", "high", "max"))
    ap.add_argument("--max-output-tokens", type=int)
    ap.add_argument("--dry-run", action="store_true", help="build the prompt and excerpt; call no model")
    ap.add_argument("--from-response", action="store_true", help="re-read the saved response; call no model")
    a = ap.parse_args()
    form_doc = load_form(a.form)
    excerpt, used = excerpt_for(source_context(form_doc), manifest())
    prompt = build_prompt(form_doc, excerpt)
    os.makedirs(RAW, exist_ok=True)
    base = os.path.join(RAW, families.stem(a.form, families.family_of(a.model)) + ".render")
    print(f"{a.form}: excerpt {len(excerpt):,} chars from " + "; ".join(f"{u['doc']} pages {u['pages']} ({u['how']})" for u in used))
    print(f"prompt {len(prompt):,} chars -> {os.path.relpath(base, ROOT)}{'.preview' if a.dry_run else ''}.prompt.txt")
    if a.dry_run:
        with open(base + ".preview.prompt.txt", "w", encoding="utf-8") as f:
            f.write(prompt)
        return
    text, meta = review_response(prompt, a.model, base, PROMPT_POLICY, a.from_response, SYSTEM, a.reasoning_effort, a.max_output_tokens)
    verdicts = extract(text)
    judged = judged_lines(form_doc)
    # A verdict keyed by a line's label or full id instead of its key is still that line's.
    aliases = {}
    for e in judged:
        aliases[e["label"]] = e["key"]; aliases[e["id"]] = e["key"]
    for k in list(verdicts):
        if k not in {e["key"] for e in judged} and k in aliases and aliases[k] not in verdicts:
            verdicts[aliases[k]] = verdicts.pop(k)
    path, counts = write_log(form_doc, a.model, prompt, used, judged, verdicts, text, meta)
    print(f"{a.form}: match {counts['MATCH']}, mismatch {counts['MISMATCH']}, unclear {counts['UNCLEAR']}, missing {counts['MISSING']}; cost {meta.get('cost_usd')} -> {os.path.relpath(path, ROOT)}")
    sys.exit(0 if counts["MISMATCH"] + counts["UNCLEAR"] + counts["MISSING"] == 0 else 3)


if __name__ == "__main__":
    main()
