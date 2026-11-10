#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Section completeness review: an isolated model names the operative rules in a form's IRS instruction
sections that the encoding neither implements, asks about, nor refuses.

One unit per form (canonical/<year>/*.json). The sections are the instruction or publication pages (documents not
starting with "f") that the form's lines and refusals cite, grouped into contiguous page runs (gaps of at most 2
pages filled), given whole from the reading-order text; a form that cites no such document is reviewed on its cited
form pages (instructions printed on the form). The encoding list is every line of the form: id, printed
marker, label, input question, refusals and citation. A HANDLED ELSEWHERE list adds the refusals on other forms tied to lines the form reads, the return-wide refusals (scope inputs, Form 1040), and the refusals on forms that read this form. The model returns YAML
claims grouped by encoded item (item, sentences[quote, page], why_uncovered, effect). Each call is one fixed-prompt `claude -p` with no tools.

    completeness_review.py [--forms a,b] [--samples K] [--force-rerun REASON] [--approve-cost DOLLARS]
                           [--dry-run] [--from-response] [--jobs 4] [--model M]

Sampled (samples.py): a form's subject is the hash of its prompt without the system prompt. A run gives each
selected form the samples its current subject still needs this milestone (samples.SAMPLES_PER_MILESTONE; a form
whose subject changed starts over), merged into reviews/<year>/completeness/completeness.json. Samples beyond the
milestone need --force-rerun REASON. The run is priced from the cost ledger and refused above the owner's gate
without --approve-cost (spend.py). Between releases a form whose subject changed is due, not failed
(tools/transcription/check_completeness.py); its --release mode refuses a release while any form is due. Raw
prompts and responses go to .transcription/completeness/. Limitation: a collection form (dependent, person) is reviewed with its own lines
only; the parent forms that hold its questions (household, person) are not added. A form whose prompt exceeds
MAX_CHARS is skipped.
"""
import argparse, datetime, hashlib, json, os, re, sys
from concurrent.futures import ThreadPoolExecutor
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from transcribe import ROOT, SOURCES, manifest, call_model, source_dir  # noqa: E402
from taxyear import Y  # noqa: E402
import jurisdiction  # noqa: E402  (--jurisdiction ny: the New York forms; reviews/ny/<year>/completeness/)
import archive_text  # noqa: E402
import baseline_check  # noqa: E402
import citations  # noqa: E402
from structured_text import indent_rest  # noqa: E402
import samples  # noqa: E402
import spend  # noqa: E402

OUT = str(jurisdiction.ypath("reviews", Y, "completeness"))
RAW = os.path.join(ROOT, ".transcription", "completeness")
MAX_CHARS = 700_000
GAP = 2
EFFECTS = ("amount", "eligibility", "presentation")
SYSTEM = jurisdiction.system("You review a software encoding of US federal tax instructions for completeness. You are given the "
          "pages of the 2025 IRS instructions or publications that a form's lines cite, and the list of what the "
          "software encodes for the form: its computed lines, the questions it asks the filer, and the situations "
          "it refuses to handle. A HANDLED ELSEWHERE list gives refusals on other forms tied to lines this form "
          "reads; a rule that leads to one of those situations is already handled and is not a gap.\n"
          "List every OPERATIVE rule in the pages that nothing in the encoding implements, asks about, or refuses. "
          "An operative rule is a sentence that changes who qualifies, what amount is allowed, what must be entered "
          "or provided, or when something is denied or limited (look for: must, can't, cannot, unless, except, "
          "exception, only if, limited to, treated as, disallowed, required). Ignore explanations, examples, "
          "record-keeping advice, and rules about other forms unless they change this form's result.\n"
          "Group the gaps by the encoded item they bear on: ONE claim per item, listing every uncovered sentence "
          "that bears on it (each with its exact quote and page), not one claim per sentence. For each claim give: "
          "the item id; why no listed line, question or refusal covers those sentences; and whether they could "
          "change a tax amount, eligibility, or only presentation. Be precise and conservative: do not report a rule that an encoded question or "
          "refusal already covers in substance.\n"
          "Return ONLY a YAML document of the form\n"
          "claims:\n"
          "  - item: \"<id of the encoded item these sentences bear on>\"\n"
          "    sentences:\n"
          "      - quote: \"<exact sentence>\"\n"
          "        page: \"<document and page, e.g. i1040gi p. 21>\"\n"
          "    why_uncovered: \"<why nothing covers them>\"\n"
          "    effect: \"amount | eligibility | presentation\"\n"
          "Use `claims: []` when there are no gaps. No prose before or after the YAML.")


def load_forms():
    return baseline_check.load_forms(os.path.join(ROOT, "canonical", Y))


def context_forms():
    """The documents whose refusals a review lists as HANDLED ELSEWHERE: the reviewed jurisdiction's; in
    New York mode the federal ones too, since a New York return reads the federal return's lines."""
    if not jurisdiction.NY:
        return load_forms()
    import json as _json
    from pathlib import Path
    docs = []
    for path in sorted(Path(ROOT, "canonical", Y).glob("*.json")):
        doc = next(iter(_json.loads(path.read_text()).values()))
        if isinstance(doc, dict) and "lines" in doc:
            docs.append(doc)
    return docs


def is_form_doc(doc):
    """An archived form (its instructions printed on it) rather than instructions or a publication: a federal
    id starting "f"; a New York form id (ny_it201, ny_it2, ny_it201att), not its instructions (ny_it201i,
    ny_it201i-html, ny_it270i) or tax tables."""
    if jurisdiction.is_ny(doc):
        return not re.search(r"i(-html)?$|tax_tables", doc)
    return doc.startswith("f")


def cited_pages(form):
    """{doc: set of pages} cited by the form's lines and refusals, instruction and publication documents only;
    for a form whose instructions are printed on the form itself (it cites no other document, as Forms 4952 and
    8880), the cited form pages."""
    out, forms_cited = {}, {}
    for line in form["lines"]:
        for c in [line["cite"]] + [r["cite"] for r in line.get("refuses") or []]:
            for doc, pages, *_ in citations.segments(c["doc"], c["locator"]):
                (forms_cited if is_form_doc(doc) else out).setdefault(doc, set()).update(pages)
    return out or forms_cited


def runs(pages, gap=GAP):
    """Contiguous (start, end) page runs, filling gaps of at most `gap` pages."""
    out = []
    for p in sorted(pages):
        if out and p - out[-1][1] <= gap + 1:
            out[-1][1] = p
        else:
            out.append([p, p])
    return [tuple(r) for r in out]


def layer(doc, mani):
    """The pages of a document's reading-order text (its text layer when it has no reading-order one)."""
    entry = mani[doc]
    key = "cols_file" if "cols_file" in entry else "text_file"
    pages = archive_text.read(source_dir(doc), entry, key=key).split("\f")
    return pages[:-1] if pages and not pages[-1].strip() else pages


def sections(form, mani):
    """([(doc, start, end, text)], used) for the form's cited pages; page numbers outside the document drop."""
    secs, used = [], []
    for doc, pages in sorted(cited_pages(form).items()):
        if doc not in mani:
            continue
        text = layer(doc, mani)
        pages = {p for p in pages if 1 <= p <= len(text)}
        for a, b in runs(pages):
            body = "\n\n".join(f"[{doc} page {p}]\n{text[p - 1].strip()}" for p in range(a, b + 1))
            secs.append((doc, a, b, body))
            used.append({"doc": doc, "pages": list(range(a, b + 1))})
    return secs, used


def encoding(form):
    out = [f"== {form['id']} =="]
    for l in form["lines"]:
        out.append(f"- {l['id']} [{l.get('printed', '')}] {indent_rest(l['label'], '    ')}")
        if l["expr"].get("op") == "input":
            out.append(f"    QUESTION: {indent_rest(l['expr'].get('source', ''), '      ')}")
        for r in l.get("refuses") or []:
            out.append(f"    REFUSES when {r['when']}: {r['form']}")
        out.append(f"    cites: {l['cite']['doc']} {l['cite']['locator']}")
    return "\n".join(out)


def _line_refs(x, ids, out):
    """The line ids an expression reads. A param name or a constant is not a line read, even when it
    spells a line id (the param sales.zero and the line sales.zero)."""
    if isinstance(x, str):
        if x in ids:
            out.add(x)
    elif isinstance(x, dict):
        for k, v in x.items():
            if k not in ("param", "const"):
                _line_refs(v, ids, out)
    elif isinstance(x, list):
        for v in x:
            _line_refs(v, ids, out)
    return out


def elsewhere(form, forms):
    """Compact lines naming the refusals on OTHER forms that already handle a situation this form might be
    claimed to miss: refusals tied to lines this form reads (on a read line, gated by a read line, or gated by a
    line that itself reads one), return-wide refusals (gated by a scope.* input, or on a Form 1040 line), and
    refusals on lines of other forms that read a line of this form directly. Deduplicated by (gate, refused form)."""
    where = {l["id"]: (f["id"], l) for f in forms for l in f["lines"]}
    ids = set(where)
    own = {l["id"] for l in form["lines"]}
    read = set()
    for l in form["lines"]:
        read |= _line_refs(l["expr"], ids, set())
        for r in l.get("refuses") or []:
            read |= _line_refs(r["when"], ids, set()) | ({r["when"]} & ids)
    read = {i for i in read if where[i][0] != form["id"]}
    seen, out = set(), []
    for f in forms:
        if f["id"] == form["id"]:
            continue
        for l in f["lines"]:
            readers = f["id"] == "f1040" or bool(_line_refs(l["expr"], ids, set()) & own)
            for r in l.get("refuses") or []:
                g = r["when"]
                gs = g if isinstance(g, str) else json.dumps(g, sort_keys=True)
                scoped = isinstance(g, str) and g.startswith("scope.")
                if not (readers or scoped or l["id"] in read or g in read
                        or (g in where and _line_refs(where[g][1]["expr"], ids, set()) & read)):
                    continue
                if (gs, r["form"]) in seen:
                    continue
                seen.add((gs, r["form"]))
                remedy = " ".join(str(r.get("remedy", "")).split())
                out.append(f"- {f['id']}: {r['form']}" + (f" -- {remedy[:140]}" if remedy else ""))
    return out


def build_prompt(form, secs, forms=()):
    head = f'FORM: "{form["title"]}" ({form["id"]})\n'
    names = "; ".join(f"{d} pp. {a}–{b}" if a != b else f"{d} p. {a}" for d, a, b, _ in secs)
    out = f"{head}SECTIONS: {names}\n\n" + "\n\n".join(s[3] for s in secs) + "\n\nENCODING:\n" + encoding(form)
    other = elsewhere(form, forms)
    if other:
        out += "\n\nHANDLED ELSEWHERE (refusals on other forms tied to lines this form reads):\n" + "\n".join(other)
    return out


def prompt_for(form, mani, forms=None):
    """(prompt, used, subject_sha) of a form's review, or None when it has no cited instruction pages. The subject
    hash covers the prompt only, not the system prompt: a change to the reviewer's instructions applies at each
    form's next sample and does not make every review due (samples.py)."""
    secs, used = sections(form, mani)
    if not secs:
        return None
    prompt = jurisdiction.preface(build_prompt(form, secs, forms if forms is not None else context_forms()))
    return prompt, used, hashlib.sha256(prompt.encode()).hexdigest()


SYSTEM_SHA = hashlib.sha256(SYSTEM.encode()).hexdigest()


def parse(text):
    """The claims of a response, leniently (last fenced block, else the whole text); None if it is not YAML claims."""
    blocks = re.findall(r"```(?:yaml)?\s*\n(.*?)```", text, re.S)
    try:
        doc = yaml.safe_load(blocks[-1] if blocks else text)
    except yaml.YAMLError:
        return None
    claims = doc.get("claims") if isinstance(doc, dict) else doc
    if claims is None and doc in (None, {}):
        return []
    if not isinstance(claims, list):
        return None
    return [claim(c) for c in claims if isinstance(c, dict)]


def claim(c):
    """One claim, leniently: sentences from `sentences` (dicts or strings), `quotes`, or a flat quote/page; the
    item from `item` or `closest_item`. `quote`, `page` and `closest_item` summarise the sentences."""
    sents = []
    for s in c.get("sentences") or c.get("quotes") or []:
        if isinstance(s, dict):
            sents.append({"quote": str(s.get("quote", "")), "page": str(s.get("page", c.get("page", "")))})
        else:
            sents.append({"quote": str(s), "page": str(c.get("page", ""))})
    if not sents and c.get("quote"):
        sents = [{"quote": str(c["quote"]), "page": str(c.get("page", ""))}]
    item = str(c.get("item") or c.get("closest_item") or "")
    pages = list(dict.fromkeys(s["page"] for s in sents if s["page"]))
    return {"item": item, "sentences": sents, "quote": " / ".join(s["quote"] for s in sents),
            "page": "; ".join(pages), "why_uncovered": str(c.get("why_uncovered", "")), "closest_item": item,
            "effect": str(c.get("effect", ""))}


def response_path(form_id, subject, k):
    return os.path.join(RAW, f"{form_id}.{subject[:12]}.{k}.response.txt")


def sample(form_id, prompt, subject, k, model):
    """Run sample k of a form's review: the sample record."""
    path = response_path(form_id, subject, k)
    text, meta = call_model(prompt, model, system=SYSTEM, kind="completeness", subject=form_id)
    open(path, "w", encoding="utf-8").write(text)
    claims = parse(text)
    rec = {"system_sha": SYSTEM_SHA, "claims": claims or [], "cost": meta.get("cost_usd") or 0,
           "model": ", ".join(meta.get("model_reported", [])) or model, "date": datetime.date.today().isoformat(),
           "response": os.path.relpath(path, ROOT)}
    if os.environ.get(spend.REASON_ENV):
        rec["rerun_reason"] = os.environ[spend.REASON_ENV]
    if claims is None:
        rec["parse_error"] = True
    return rec


def read_records(path):
    """{form: record} of a completeness.json in the sampled format (samples.py)."""
    if not os.path.exists(path):
        return {}
    rows = json.load(open(path, encoding="utf-8"))
    legacy = [r["form"] for r in rows if "samples" not in r]
    if legacy:
        sys.exit(f"{path}: {len(legacy)} record(s) in the single-review format ({', '.join(legacy[:5])}); "
                 "the file predates sampled reviews")
    return {r["form"]: r for r in rows}


def plan(forms, mani, records, asked, force, price, model):
    """One entry per selected form: {form, subject, prompt, used, n, beyond, note, jobs}. `jobs` are the planned
    samples ({kind, form, k, run, usd}) for spend.gate; a form beyond its milestone without --force-rerun plans none."""
    everything = context_forms()
    out = []
    for f in forms:
        p = prompt_for(f, mani, everything)
        if p is None:
            out.append({"form": f["id"], "note": "no cited instruction pages", "jobs": []})
            continue
        prompt, used, subject = p
        if len(prompt) > MAX_CHARS:
            out.append({"form": f["id"], "note": f"prompt {len(prompt):,} chars exceeds {MAX_CHARS:,}", "jobs": []})
            continue
        rec = records.get(f["id"])
        n, beyond = samples.wanted(rec, subject, asked)
        entry = {"form": f["id"], "subject": subject, "prompt": prompt, "used": used, "n": n, "beyond": beyond, "jobs": []}
        if n == 0:
            entry["note"] = "satisfied: its current subject has the milestone's samples"
        elif beyond and not force:
            entry["note"] = (f"refused: {n} sample(s) would go beyond the milestone's {samples.SAMPLES_PER_MILESTONE}; "
                             "--force-rerun REASON runs them")
        else:
            first = len(rec["samples"]) + 1 if rec and rec.get("subject_sha") == subject else 1
            usd = spend.estimate(len(prompt), "completeness_review.py", model, price)
            entry["jobs"] = [{"kind": "completeness", "form": f["id"], "k": k, "run": True, "usd": usd}
                             for k in range(first, first + n)]
            entry["note"] = f"{n} sample(s) from #{first}"
        out.append(entry)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--forms")
    ap.add_argument("--dry-run", action="store_true", help="plan and estimate; call no model")
    ap.add_argument("--from-response", action="store_true",
                    help="re-parse the saved responses of the current subject's samples; call no model")
    ap.add_argument("--samples", type=int, metavar="K", help="run K samples per form (default: those the milestone still needs)")
    ap.add_argument("--force-rerun", metavar="REASON", help="run samples beyond the milestone; the reason is recorded")
    ap.add_argument("--approve-cost", metavar="DOLLARS", type=float,
                    help=f"run although the estimate exceeds the ${spend.COST_GATE_USD:.2f} gate; at least the estimate")
    ap.add_argument("--jobs", type=int, default=4); ap.add_argument("--model", default="claude-opus-5-5")
    a = ap.parse_args()
    if a.force_rerun is not None and not a.force_rerun.strip():
        ap.error("--force-rerun needs a reason")
    forms = load_forms(); mani = manifest()
    if a.forms:
        want = a.forms.split(",")
        missing = [w for w in want if w not in {f["id"] for f in forms}]
        if missing:
            sys.exit(f"unknown form(s): {', '.join(missing)}")
        forms = [f for f in forms if f["id"] in want]
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "completeness.json")
    records = read_records(path)
    if a.from_response:
        n = 0
        for f in forms:
            for smp in (records.get(f["id"]) or {}).get("samples", []):
                where = os.path.join(ROOT, smp.get("response", ""))
                if not smp.get("response") or not os.path.exists(where):
                    continue
                claims = parse(open(where, encoding="utf-8").read())
                smp["claims"] = claims or []
                smp.pop("parse_error", None)
                if claims is None:
                    smp["parse_error"] = True
                n += 1
        json.dump(sorted(records.values(), key=lambda r: r["form"]), open(path, "w"), indent=1, ensure_ascii=False)
        print(f"re-parsed {n} saved sample(s)")
        return
    planned = plan(forms, mani, records, a.samples, a.force_rerun, spend.prices(), a.model)
    jobs = [j for e in planned for j in e["jobs"]]
    for e in planned:
        cost = sum(j["usd"] or 0 for j in e["jobs"])
        print(f"{e['form']:20s} {e['note']}" + (f"  ~${cost:.2f}" if e["jobs"] else ""))
    total = sum(j["usd"] or 0 for j in jobs)
    print(f"{len(jobs)} sample(s), estimated ${total:.2f}; gate ${spend.COST_GATE_USD:.2f}")
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
    os.makedirs(RAW, exist_ok=True)
    by_form = {e["form"]: e for e in planned if e["jobs"]}
    for e in by_form.values():
        open(os.path.join(RAW, e["form"] + ".prompt.txt"), "w", encoding="utf-8").write(e["prompt"])
    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        results = list(ex.map(lambda j: (j, sample(j["form"], by_form[j["form"]]["prompt"], by_form[j["form"]]["subject"],
                                                    j["k"], a.model)), jobs))
    for form_id, e in by_form.items():
        rec = records.get(form_id)
        if not rec or rec.get("subject_sha") != e["subject"]:
            rec = records[form_id] = {"form": form_id, "subject_sha": e["subject"], "used": e["used"], "samples": []}
        rec["used"] = e["used"]
        rec["samples"] += [s for j, s in sorted(results, key=lambda r: r[0]["k"]) if j["form"] == form_id]
    json.dump(sorted(records.values(), key=lambda r: r["form"]), open(path, "w"), indent=1, ensure_ascii=False)
    done = [s for _, s in results]
    print(f"{len(done)} sample(s) of {len(by_form)} form(s); {sum(len(s['claims']) for s in done)} claims; "
          f"{sum(1 for s in done if s.get('parse_error'))} unparsed; cost {sum(s['cost'] for s in done):.2f}")


if __name__ == "__main__":
    main()
