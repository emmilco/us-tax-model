#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Section completeness review: an isolated model names the operative rules in a form's IRS instruction
sections that the encoding neither implements, asks about, nor refuses.

One unit per form (canonical/<year>/*.json). The sections are the instruction or publication pages (documents not
starting with "f") that the form's lines and refusals cite, grouped into contiguous page runs (gaps of at most 2
pages filled), given whole from the reading-order text. The encoding list is every line of the form: id, printed
marker, label, input question, refusals and citation. A HANDLED ELSEWHERE list adds the refusals on other forms tied to lines the form reads, the return-wide refusals (scope inputs, Form 1040), and the refusals on forms that read this form. The model returns YAML
claims grouped by encoded item (item, sentences[quote, page], why_uncovered, effect). Each call is one fixed-prompt `claude -p` with no tools.

    completeness_review.py [--forms a,b] [--dry-run] [--from-response] [--jobs 4] [--model M]

A form whose prompt hash differs from its recorded review is stale in check-all
(tools/transcription/check_completeness.py); rerun it with --forms, which merges into
reviews/<year>/completeness/completeness.json and keeps the other forms' entries. Raw prompts and responses go
to .transcription/completeness/. Limitation: a collection form (dependent, person) is reviewed with its own lines
only; the parent forms that hold its questions (household, person) are not added. A form whose prompt exceeds
MAX_CHARS is skipped.
"""
import argparse, hashlib, json, os, re, sys
from concurrent.futures import ThreadPoolExecutor
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from transcribe import ROOT, SOURCES, manifest, call_model  # noqa: E402
from taxyear import Y  # noqa: E402
import archive_text  # noqa: E402
import baseline_check  # noqa: E402
import citations  # noqa: E402

OUT = os.path.join(ROOT, "reviews", Y, "completeness")
RAW = os.path.join(ROOT, ".transcription", "completeness")
MAX_CHARS = 400_000
GAP = 2
EFFECTS = ("amount", "eligibility", "presentation")
SYSTEM = ("You review a software encoding of US federal tax instructions for completeness. You are given the "
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


def cited_pages(form):
    """{doc: set of pages} cited by the form's lines and refusals, instruction and publication documents only."""
    out = {}
    for line in form["lines"]:
        for c in [line["cite"]] + [r["cite"] for r in line.get("refuses") or []]:
            for doc, pages, *_ in citations.segments(c["doc"], c["locator"]):
                if not doc.startswith("f"):
                    out.setdefault(doc, set()).update(pages)
    return out


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
    pages = archive_text.read(SOURCES, entry, key=key).split("\f")
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
        out.append(f"- {l['id']} [{l.get('printed', '')}] {l['label']}")
        if l["expr"].get("op") == "input":
            out.append(f"    QUESTION: {l['expr'].get('source', '')}")
        for r in l.get("refuses") or []:
            out.append(f"    REFUSES when {r['when']}: {r['form']}")
        out.append(f"    cites: {l['cite']['doc']} {l['cite']['locator']}")
    return "\n".join(out)


def _line_refs(x, ids, out):
    if isinstance(x, str):
        if x in ids:
            out.add(x)
    elif isinstance(x, dict):
        for v in x.values():
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
    """(prompt, used, sha) of a form's review, or None when it has no cited instruction pages. The hash covers
    the system prompt, so a change to the instructions makes every review stale."""
    secs, used = sections(form, mani)
    if not secs:
        return None
    prompt = build_prompt(form, secs, forms if forms is not None else load_forms())
    return prompt, used, hashlib.sha256((SYSTEM + "\n" + prompt).encode()).hexdigest()


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


def run_one(form, mani, model, dry, from_response, forms=None):
    p = prompt_for(form, mani, forms)
    if p is None:
        return {"form": form["id"], "skip": "no cited instruction pages"}
    prompt, used, sha = p
    if len(prompt) > MAX_CHARS:
        return {"form": form["id"], "skip": f"prompt {len(prompt):,} chars exceeds {MAX_CHARS:,}", "chars": len(prompt),
                "pages": sum(len(u["pages"]) for u in used)}
    pages = sum(len(u["pages"]) for u in used)
    if dry:
        return {"form": form["id"], "chars": len(prompt), "pages": pages}
    os.makedirs(RAW, exist_ok=True)
    base = os.path.join(RAW, form["id"])
    open(base + ".prompt.txt", "w", encoding="utf-8").write(prompt)
    if from_response:
        text = open(base + ".response.txt", encoding="utf-8").read(); meta = {}
    else:
        text, meta = call_model(prompt, model, system=SYSTEM)
        open(base + ".response.txt", "w", encoding="utf-8").write(text)
    claims = parse(text)
    rec = {"form": form["id"], "prompt_sha": sha, "claims": claims or [], "used": used,
           "cost": meta.get("cost_usd") or 0, "model": ", ".join(meta.get("model_reported", [])) or model}
    if claims is None:
        rec["parse_error"] = True
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--forms"); ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--from-response", action="store_true")
    ap.add_argument("--jobs", type=int, default=4); ap.add_argument("--model", default="claude-opus-5-5")
    a = ap.parse_args()
    forms = everything = load_forms(); mani = manifest()
    if a.forms:
        want = a.forms.split(",")
        missing = [w for w in want if w not in {f["id"] for f in forms}]
        if missing:
            sys.exit(f"unknown form(s): {', '.join(missing)}")
        forms = [f for f in forms if f["id"] in want]
    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        results = list(ex.map(lambda f: run_one(f, mani, a.model, a.dry_run, a.from_response, everything), forms))
    done = [r for r in results if "skip" not in r]
    skipped = [r for r in results if "skip" in r]
    if a.dry_run:
        for r in done:
            print(f"{r['form']:20s} {r['pages']:4d} pages {r['chars']:9,d} chars")
        print(f"{len(done)} forms, {sum(r['chars'] for r in done):,} chars in all")
        for r in skipped:
            print(f"skipped {r['form']}: {r['skip']}")
        return
    for r in skipped:
        print(f"skipped {r['form']}: {r['skip']}")
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "completeness.json")
    previous = json.load(open(path)) if os.path.exists(path) else []
    rerun = {r["form"] for r in done}
    merged = [r for r in previous if r["form"] not in rerun] + done
    json.dump(sorted(merged, key=lambda r: r["form"]), open(path, "w"), indent=1, ensure_ascii=False)
    print(f"{len(done)} forms; {sum(len(r['claims']) for r in done)} claims; "
          f"{sum(1 for r in done if r.get('parse_error'))} unparsed; cost {sum(r['cost'] for r in done):.2f}")


if __name__ == "__main__":
    main()
