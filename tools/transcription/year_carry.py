#!/usr/bin/env python3
"""Carry review verdicts across a tax-year change (the review store design, section 2.3).

Given the tree of tax year TY (its reviews committed as records and indexes, review_store.py) and the tree
of TY+1, list which compared lines of each review carry to TY+1 and which need a review, and with --write
write the carried entries into TY+1's indexes and the rulings they show into TY+1's rulings sidecars. Run it
from the TY+1 tree; --from names the TY tree.

A line carries only when its year-carry key is equal in both years and the review tools' policy versions
are the same for both (always so within one checkout; rename_carry.py compares another commit's). The key
hashes three things, and is recorded on each carried index line (`year_key`), so check_logs.py can recompute
it and find a carried line whose source text, values or subject changed after the carry; a policy version
change applies to carried lines as to any other, at their next review, and is not part of the key:

1. the line's subject as its review kind sees it: for transcription the line and its in-document reach
   (subjects.reach; citations and wording left out, an input's question kept) and the interface (id,
   document, marker, type, input question) of every foreign line that reach names; for render the line's
   rendered section and its glossary sections; for class M the document's computation (subjects.
   of_computation);
2. the values of every parameter, enum and table the reach reads (a changed value blocks the carry: the
   prompt and the compared expression show the year's value); a table's value is its data, every field but
   its title, citation and tax year (table_value), so a table carries when only its year moved;
3. the cited source text, at anchor-section granularity, of every line of the reach and every foreign line
   it names: for each cited page segment, the text (read through archive_text, normalized as citations.norm
   normalizes a page) from the cited anchor's heading to the next heading of an anchor any citation of the
   same document names, else the cited pages whole (anchor_section); a citation naming no page stands for
   its whole document. Never only the quoted words, so a paragraph added under the same heading changes the
   key; a cross-reference in the section's prose to another anchor is not a heading and does not end it.

With --jurisdiction ny the reviews carried are New York's (reviews/ny/<year>/), and each tree is read across both
jurisdictions as the New York review tools read it: the federal and New York forms (a New York line names federal
lines), both years' parameters and tables, and each document's sources and rendering in its own jurisdiction's
directory (ny_ ids under sources/ny/<year>/ and rendered/ny/<year>/). Federally only the federal tree is read.

Year normalization is lockstep, never blind. The two years' texts are aligned token by token (difflib);
a year literal is replaced by {Y}, {Y-1}, ... only where it moved by exactly +1 between the two years and
lies within YEAR_WINDOW of the tax year. In the project's own subject a moved year is normalized only
where the line's cited source moved the same year and printed it nowhere unchanged in the same context
(the two words before it), so a fixed statutory date the project wrongly incremented ("after January 19,
2025" printed in both years' text, "2026" in the project) stays a difference. Birth-year cutoffs (1961 -> 1962) lie outside the window:
they change, so their lines are reviewed.

    year_carry.py --year 2026 --from ../tax-2025 [--from-year 2025] [--jurisdiction ny] [--kind K] [--write] [--report PATH] [--verbose]
    year_carry.py --self-test
"""
import argparse, difflib, hashlib, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))

import yaml  # noqa: E402
from taxyear import Y  # noqa: E402  (--year: the tax year TY+1 of this tree)
import jurisdiction  # noqa: E402  (--jurisdiction ny: New York's reviews)
import archive_text  # noqa: E402

_Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
YEAR_WINDOW = (-10, 1)  # years from TY-10 to TY+1 may be normalized
TOKEN = re.compile(r"\w+|[^\w\s]")
YEAR = re.compile(r"^(19|20)\d\d$")
NOT_ARCHIVED = "\x00"  # the text of a cited document the tree has not archived
WAITING = ("cited document not archived for the new year", "no value yet for the new year")


def _sha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


# ---------------------------------------------------------------- one year's tree

class Tree:
    """The forms, parameters, tables, sources and rendered text of one tax year in one checkout."""

    def __init__(self, root, year):
        self.root, self.year, self._c = root, str(year), {}

    def path(self, *parts):
        return os.path.join(self.root, *parts)

    def dir(self, top, doc=None):
        """The path parts of a per-year directory: a document's own jurisdiction's, or (no document) the
        jurisdiction under review's."""
        ny = jurisdiction.is_ny(doc) if doc is not None else jurisdiction.NY
        return (top, "ny", self.year) if ny else (top, self.year)

    def dirs(self, top):
        """The per-year directories this tree is read from: the federal one, then (New York) the New York one."""
        return [(top, self.year)] + ([(top, "ny", self.year)] if jurisdiction.NY else [])

    def read(self, *parts):
        p = self.path(*parts)
        if p not in self._c:
            self._c[p] = open(p, encoding="utf-8").read() if os.path.exists(p) else None
        return self._c[p]

    def docs(self):
        if "__docs" not in self._c:
            out = {}
            for parts in self.dirs("forms"):
                d = self.path(*parts)
                for name in sorted(os.listdir(d)) if os.path.isdir(d) else []:
                    if name.endswith(".yaml"):
                        raw = yaml.load(self.read(*parts, name), Loader=_Loader) or {}
                        doc = raw.get("form") or raw.get("def")
                        if doc:
                            out[doc["id"]] = doc
            self._c["__docs"] = out
        return self._c["__docs"]

    def lines(self):
        """{line id: (document id, line)} over every document."""
        if "__lines" not in self._c:
            out = {}
            for fid, doc in self.docs().items():
                for l in doc.get("lines", []):
                    out.setdefault(l["id"], (fid, l))
            self._c["__lines"] = out
        return self._c["__lines"]

    def params(self):
        if "__params" not in self._c:
            values, enums = {}, {}
            for parts in [("params", self.year + ".yaml")] + ([("params", "ny", self.year + ".yaml")] if jurisdiction.NY else []):
                text = self.read(*parts)
                raw = (yaml.load(text, Loader=_Loader) or {}) if text else {}
                p = raw.get("params") or raw
                values.update(p.get("values") or {})
                enums.update(p.get("enums") or {})
            self._c["__params"] = (values, enums)
        return self._c["__params"]

    def tables(self):
        """{table id: the path parts of its file}."""
        if "__tables" not in self._c:
            out = {}
            for parts in self.dirs("tables"):
                d = self.path(*parts)
                out.update({n.split(".")[0]: (*parts, n) for n in sorted(os.listdir(d))} if os.path.isdir(d) else {})
            self._c["__tables"] = out
        return self._c["__tables"]

    def pages(self, doc):
        """The pages of an archived document's reading-order text (its cols_file, else its text_file), read
        through archive_text.read so that a draft's cover and watermarks are removed; None when the document or
        its text layer is not archived."""
        key = f"__pages {doc}"
        if key not in self._c:
            m = json.loads(self.read(*self.dir("sources", doc), "manifest.json") or "{}")
            entries = m["documents"] if isinstance(m, dict) else m
            d = next((e for e in entries if e.get("id") == doc), None)
            layer = d and next((k for k in ("cols_file", "text_file") if d.get(k)), None)
            archive = self.path(*self.dir("sources", doc))
            text = archive_text.read(archive, d, layer) if layer and os.path.exists(os.path.join(archive, d[layer])) else None
            self._c[key] = text.split("\f") if text is not None else None
        return self._c[key]

    def anchors(self, doc):
        """Every anchor any citation of this year names in a document: the section boundaries."""
        if "__anchors" not in self._c:
            import citations
            out = {}
            for _, l in self.lines().values():
                c = l.get("cite") or {}
                for cite in c if isinstance(c, list) else [c]:
                    for seg_doc, _, anchor, _, _ in citations.segments(cite.get("doc"), cite.get("locator") or ""):
                        if anchor:
                            out.setdefault(seg_doc, set()).add(anchor)
            self._c["__anchors"] = out
        return self._c["__anchors"].get(doc, set())


# ---------------------------------------------------------------- the parts of a key

def _strings(o):
    import subjects
    return subjects._strings(o)


def reach(doc, line_id):
    import subjects
    return subjects.reach(doc, line_id)


def subject_text(tree, doc, line_id):
    """The transcription subject of a line, as text: the reach as the comparison sees it and the foreign
    interfaces it names (subjects.transcription_line_subjects, foreign_interfaces)."""
    import subjects
    view = lambda o: subjects._without_cites(subjects._unworded(o))
    members, boundary = reach(doc, line_id)
    by_id = {l["id"]: l for l in doc["lines"]}
    rows = [view(by_id[i]) for i in sorted(members)]
    rows += [{"boundary": i, "printed": str(by_id[i]["printed"]), "type": by_id[i]["type"]} for i in sorted(boundary)]
    index = tree.lines()
    names = {s for i in members for s in _strings({k: v for k, v in by_id[i].items() if k != "id"}) if s in index and s not in by_id}
    for n in sorted(names):
        fid, l = index[n]
        row = {"foreign": n, "doc": fid, "printed": str(l.get("printed")), "type": l.get("type")}
        if (l.get("expr") or {}).get("op") == "input":
            row["source"] = " ".join(str(l["expr"].get("source", "")).split())
        rows.append(row)
    return json.dumps(rows, sort_keys=True, ensure_ascii=False, indent=0), sorted(names)


def values(tree, doc, ids):
    """{name: value} of every parameter, enum and table the given lines name."""
    params, enums = tree.params()
    tables = tree.tables()
    by_id = {l["id"]: l for l in doc["lines"]}
    out = {}
    for i in sorted(ids):
        for s in _strings({k: v for k, v in by_id[i].items() if k != "id"}):
            m = re.match(r"^Enum\(([^()]+)\)$", s)
            if m and m.group(1) in enums:
                out["enum " + m.group(1)] = enums[m.group(1)]
            elif s in params:
                out["param " + s] = (params[s] or {}).get("value") if isinstance(params[s], dict) else params[s]
            elif s in tables:
                out["table " + s] = table_value(tree.read(*tables[s]))
    return out


TABLE_NOT_VALUES = ("title", "cite", "tax_year")


def table_value(text):
    """The hash of a table file's data: the parsed table without its title, citation and tax year (comments are
    not parsed), so the same bands or rows under the next year's heading hash alike."""
    raw = (yaml.load(text, Loader=_Loader) or {}) if text else {}
    table = raw.get("table") if isinstance(raw, dict) else None
    data = {k: v for k, v in table.items() if k not in TABLE_NOT_VALUES} if isinstance(table, dict) else raw
    return _sha(data)


def cites(line):
    c = line.get("cite") or {}
    return [x for x in (c if isinstance(c, list) else [c]) if isinstance(x, dict)]


def _norm_space(text):
    return " ".join(text.split())


def section_texts(tree, line):
    """[(label, text)] of the cited source of a line, at anchor-section granularity."""
    import citations
    out = []
    for cite in cites(line):
        doc = cite.get("doc")
        segs = citations.segments(doc, cite.get("locator") or "")
        if not segs:
            pages = tree.pages(doc)
            out.append((f"{doc} whole", _norm_space("\n".join(pages)) if pages else NOT_ARCHIVED + f" {doc} not archived"))
            continue
        for seg_doc, pages, anchor, _, _ in segs:
            all_pages = tree.pages(seg_doc)
            if all_pages is None:
                out.append((f"{seg_doc} {anchor or 'pages'}", NOT_ARCHIVED + f" {seg_doc} not archived"))
                continue
            text = "\n".join(all_pages[p - 1] for p in pages if 0 < p <= len(all_pages))
            out.append((f"{seg_doc} {anchor or 'pages'}", anchor_section(text, anchor, tree.anchors(seg_doc))))
    return out


# The last word of a line whose sentence runs on into the next line, with any lowercase word ending in "ing"
# ("subtracting"): a known anchor at the start of the next line is a cross-reference in that sentence
# ("Subtract" / "Line 4 from Line 3"), not a heading.
RUNS_ON = {"a", "add", "an", "and", "as", "at", "by", "combine", "enter", "from", "in", "include", "includes",
           "including", "into", "is", "less", "minus", "of", "on", "or", "plus", "see", "subtract", "than", "the",
           "to", "under", "with"}


def _lines(text):
    """The extracted lines of a text, each normalized as citations.norm normalizes a page (a word broken across
    a line end joined first), as (raw line, normalized line); empty lines dropped."""
    import citations
    text = re.sub(r"(\w)-[ \t]*\n\s*(\w)", r"\1\2", re.sub("\u00ad\\s*", "", text))
    return [(raw.strip(), n) for raw in text.split("\n") if (n := citations.norm(raw))]


def _keys(anchor):
    """The normalized phrases that may print an anchor, most specific first (citations.anchor_keys)."""
    import citations
    return [k[0] for k in citations.anchor_keys(anchor) if len(k) == 1]


def _word_at(line, at, key):
    """Whether `key` is printed in `line` at `at` as whole words."""
    end = at + len(key)
    return (at == 0 or not line[at - 1].isalnum()) and (end == len(line) or not line[end].isalnum())


def _heading(lines, i, keys):
    """Whether line i is a heading printing one of `keys`: it starts with the key as whole words, does not start
    with a lowercase letter, and does not continue the sentence of the line before (RUNS_ON)."""
    raw, n = lines[i]
    if raw[:1].islower():
        return False
    last = lines[i - 1][0].split()[-1] if i else ""
    if last in RUNS_ON or re.fullmatch(r"[a-z]+ing", last):
        return False
    return any(n.startswith(k) and _word_at(n, 0, k) for k in keys)


def anchor_section(text, anchor, known):
    """The cited section of the cited pages, normalized line by line as citations.norm normalizes a page: from
    the anchor's heading to the next heading of another known anchor, else to the end of the pages. A heading is
    a line that starts with the anchor as whole words (_heading). A compound anchor ("Lines 4a-5b") whose own
    words are not a heading starts at the heading of its first member (citations.anchor_keys) and runs to the
    end of the pages, since the sections it spans are headed by other known anchors. An anchor printed on the
    pages only inside a line, or not at all, gives the pages whole: the section it names may have begun on an
    earlier page. A known anchor printed inside a line, as a cross-reference in the section's prose ("Subtract
    Line 4 from Line 3"), never ends the section."""
    lines = _lines(text)
    flat = lambda rows: " ".join(n for _, n in rows)
    keys = _keys(anchor) if anchor else []
    for k in keys:
        start = next((i for i in range(len(lines)) if _heading(lines, i, [k])), None)
        if start is None:
            continue
        if k != keys[0]:
            return flat(lines[start:])
        others = {o for a in known if a for o in _keys(a)} - set(keys)
        end = next((i for i in range(start + 1, len(lines)) if _heading(lines, i, others)), len(lines))
        return flat(lines[start:end])
    return flat(lines)


# ---------------------------------------------------------------- lockstep normalization

def _tokens(text):
    return TOKEN.findall(text)


def _ctx(tokens, i):
    return tuple(t.lower() for t in tokens[max(0, i - 2):i])


_SHIFTS = {}


def shifts(old, new, ty):
    """(normalized old tokens, normalized new tokens, evidence) of a source text in both years. Evidence is
    {("moved", context, year)} for each aligned year that moved by +1 within the window and {("kept", context,
    year)} for each year printed unchanged in both years. Memoized: a cited section recurs across lines."""
    key = (hashlib.sha256(old.encode()).digest(), hashlib.sha256(new.encode()).digest(), ty)
    if key not in _SHIFTS:
        _SHIFTS[key] = _shifts(old, new, ty)
    return _SHIFTS[key]


def _shifts(old, new, ty):
    a, b = _tokens(old), _tokens(new)
    if a == b:
        return a, b, {("kept", _ctx(a, i), a[i]) for i in range(len(a)) if YEAR.match(a[i])}
    na, nb, moved = list(a), list(b), set()
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == "equal":
            moved |= {("kept", _ctx(a, i), a[i]) for i in range(i1, i2) if YEAR.match(a[i])}
        if op == "replace" and i2 - i1 == j2 - j1:
            for i, j in zip(range(i1, i2), range(j1, j2)):
                if YEAR.match(a[i]) and YEAR.match(b[j]) and int(b[j]) == int(a[i]) + 1:
                    k = int(a[i]) - int(ty)
                    if YEAR_WINDOW[0] <= k <= YEAR_WINDOW[1]:
                        moved.add(("moved", _ctx(a, i), a[i]))
                        na[i] = nb[j] = "{Y%+d}" % k if k else "{Y}"
    return na, nb, moved


def project_pair(old, new, ty, evidence):
    """The project's own text of both years. A year that moved by +1 is normalized only where the cited
    source moved the same year too, and printed it nowhere unchanged in the same context (the two words
    before it): a fixed date the source keeps ("after January 19, 2025") stays literal in the project.
    The other way round, a year the project kept where the source moved it in the same context and kept
    it in none ("paid in 2025" still in the project, "paid in 2026" in the new source) is a difference:
    the project was not rolled forward."""
    a, b = _tokens(old), _tokens(new)
    na, nb = list(a), list(b)
    moved_years = {y for tag, _, y in evidence if tag == "moved"}
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == "equal":
            for i, j in zip(range(i1, i2), range(j1, j2)):
                if YEAR.match(a[i]) and ("moved", _ctx(a, i), a[i]) in evidence and ("kept", _ctx(a, i), a[i]) not in evidence:
                    nb[j] = b[j] + " (not moved with the source)"
        if op == "replace" and i2 - i1 == j2 - j1:
            for i, j in zip(range(i1, i2), range(j1, j2)):
                if (YEAR.match(a[i]) and YEAR.match(b[j]) and int(b[j]) == int(a[i]) + 1 and a[i] in moved_years
                        and ("kept", _ctx(a, i), a[i]) not in evidence):
                    k = int(a[i]) - int(ty)
                    na[i] = nb[j] = "{Y%+d}" % k if k else "{Y}"
    return na, nb


def policies():
    """The policy versions of the review tools (compared beside the key)."""
    import transcribe as T
    import triage
    return {"prompt": T.PROMPT_POLICY, "comparison": T.COMPARISON_POLICY, "types": T.TYPE_VALIDATION_POLICY,
            "inputs": T.INPUT_CONTEXT_POLICY, "triage": triage.POLICY}


def compare_parts(ty, old, new):
    """(carries, reason, old key, new key) of one line from its parts in both years: {subject, values,
    cited: [(label, text)]}. The cited texts give the shift evidence for the subject."""
    why = []
    if len(old["cited"]) != len(new["cited"]) or [l for l, _ in old["cited"]] != [l for l, _ in new["cited"]]:
        why.append("its citations changed")
    evidence, cited_a, cited_b = set(), [], []
    for (la, ta), (lb, tb) in zip(old["cited"], new["cited"]):
        na, nb, moved = shifts(ta, tb, ty)
        evidence |= moved
        cited_a.append((la, na)); cited_b.append((lb, nb))
    if cited_a != cited_b:
        changed = [(la, b) for (la, a), (_, b) in zip(cited_a, cited_b) if a != b]
        missing = sorted({la.split(" ")[0] for la, b in changed if b and b[0] == NOT_ARCHIVED})
        printed = [la for la, b in changed if not (b and b[0] == NOT_ARCHIVED)]
        if missing:
            why.append("cited document not archived for the new year: " + ", ".join(missing))
        if printed:
            why.append("cited text changed: " + ", ".join(printed))
    sa, sb = project_pair(old["subject"], new["subject"], ty, evidence)
    if sa != sb:
        why.append("the line or what it reads changed")
    if old["values"] != new["values"]:
        diff = sorted(k for k in set(old["values"]) | set(new["values"]) if old["values"].get(k) != new["values"].get(k))
        unset = [k for k in diff if new["values"].get(k) is None and k in new["values"]]
        if unset:
            why.append("no value yet for the new year: " + ", ".join(unset))
        if [k for k in diff if k not in unset]:
            why.append("values changed: " + ", ".join(k for k in diff if k not in unset))
    if old.get("policies") != new.get("policies"):
        why.append("policy versions changed")
    key_a = _sha([sa, old["values"], cited_a])
    key_b = _sha([sb, new["values"], cited_b])
    return (not why, "; ".join(why) or None, key_a, key_b)


def parts(kind, tree, fid, line_id):
    """{subject, values, cited, policies} of a compared line (or, for class M, of the document)."""
    import subjects
    doc = tree.docs().get(fid)
    if doc is None:
        return None
    by_id = {l["id"]: l for l in doc["lines"]}
    if kind == "classm":
        text = tree.read(*tree.dir("forms", fid), fid + ".yaml")
        raw = yaml.load(text, Loader=_Loader)
        d = raw.get("form") or raw.get("def")
        rows = [{"id": l.get("id"), "type": l.get("type"), "expr": {k: v for k, v in (l.get("expr") or {}).items() if k != "source"}}
                for l in d.get("lines", [])]
        cited = [c for l in doc["lines"] for c in section_texts(tree, l)]
        return {"subject": json.dumps(rows, sort_keys=True, indent=0), "values": values(tree, doc, list(by_id)),
                "cited": cited, "policies": policies()}
    if line_id not in by_id:
        return None
    subject, foreign = subject_text(tree, doc, line_id)
    members, boundary = reach(doc, line_id)
    if kind == "render":
        rendered = tree.read(*tree.dir("rendered", fid), fid + ".md")
        if rendered is None:
            return None
        head, sections = subjects.rendered_sections(rendered)
        if line_id not in sections:
            return None
        ids = {line_id} | set(_rendered(tree, fid, lambda R, entries: {
            e["id"] for gfid, e in R.glossary(fid, [entries[line_id]], stop={x["id"] for x in R.judged_entries(entries)})
            if gfid == fid}) or ())
        subject = "".join(subjects.CITE_TEXT.sub("[cite]", sections[i]) for i in sorted(ids) if i in sections)
    cited = []
    for i in sorted(members | boundary):
        cited += section_texts(tree, by_id[i])
    index = tree.lines()
    for n in foreign:
        cited += section_texts(tree, index[n][1])
    return {"subject": subject, "values": values(tree, doc, members), "cited": cited, "policies": policies()}


# ---------------------------------------------------------------- the carry

def _rendered(tree, fid, use):
    """use(render_compare, parsed entries) with the tree's rendering of a document in render_compare's
    cache (it reads the rendering of the checkout it runs in), else None without a rendering."""
    import render_compare as R
    text = tree.read(*tree.dir("rendered", fid), fid + ".md")
    if text is None:
        return None
    saved = R._rendered_cache.get(fid)
    R._rendered_cache[fid] = R.parse_rendered_text(text)
    try:
        return use(R, R._rendered_cache[fid])
    finally:
        if saved is None:
            R._rendered_cache.pop(fid, None)
        else:
            R._rendered_cache[fid] = saved


def compared_keys(kind, tree, doc):
    """{log key: line id} of the lines a review of the kind compares in a tree's document."""
    import transcribe as T
    if kind == "render":
        return _rendered(tree, doc["id"], lambda R, _: {e["key"]: e["id"] for e in R.judged_lines(doc)}) or {}
    return dict(T.line_keys(doc))


def carry_keys(kind, old, new, fid, keys):
    """{log key: (carries, reason, year key)} of the given log keys of a document's review of the kind, from
    tree `old` to tree `new`; the year key is the new year's (compare_parts), None where the line does not
    carry. Class M judges the document whole, so every key gets the document's result."""
    doc_old, doc_new = old.docs().get(fid), new.docs().get(fid)
    if doc_new is None or doc_old is None:
        why = f"{fid} is not a document of {new.year if doc_new is None else old.year}"
        return {k: (False, why, None) for k in keys}
    if kind == "classm":
        ok, why, _, kb = compare_parts(old.year, parts(kind, old, fid, None), parts(kind, new, fid, None))
        return {k: (ok, why, kb if ok else None) for k in keys}
    if kind == "render" and new.read(*new.dir("rendered", fid), fid + ".md") is None:
        return {k: (False, f"no rendering of the form in {new.year}", None) for k in keys}
    keys_old, keys_new = compared_keys(kind, old, doc_old), compared_keys(kind, new, doc_new)
    out = {}
    for k in keys:
        lid = keys_old.get(k)
        if lid is None or keys_new.get(k) != lid:
            out[k] = (False, "the line is not compared under the same key in both years", None)
            continue
        a, b = parts(kind, old, fid, lid), parts(kind, new, fid, lid)
        if a is None or b is None:
            out[k] = (False, f"no {kind} subject in {old.year if a is None else new.year}", None)
            continue
        ok, why, _, kb = compare_parts(old.year, a, b)
        out[k] = (ok, why, kb if ok else None)
    return out


def plan(kind, old, new):
    """{form: {"carry": [(key, line id, year key)], "review": [(key, line id, reason)]}} for every form of
    the TY tree with an index of the kind."""
    import families
    out = {}
    d = old.path(*old.dir("reviews"), kind)
    stems = sorted(n[:-len(".index.json")] for n in os.listdir(d) if n.endswith(".index.json")) if os.path.isdir(d) else []
    for stem in stems:
        fid, family = families.split_stem(stem)
        if family != families.DEFAULT:
            continue  # the second family is dropped: its historical reviews do not carry
        index = json.loads(old.read(*old.dir("reviews"), kind, stem + ".index.json"))
        rec = out.setdefault(fid, {"carry": [], "review": []})
        doc_old, doc_new = old.docs().get(fid), new.docs().get(fid)
        result = carry_keys(kind, old, new, fid, [l["key"] for l in index["lines"]])
        ids = compared_keys(kind, old, doc_old) if doc_old is not None and kind != "classm" else {}
        for l in index["lines"]:
            ok, why, key = result[l["key"]]
            if ok:
                rec["carry"].append((l["key"], ids.get(l["key"]), key))
            else:
                rec["review"].append((l["key"], ids.get(l["key"]), why))
        if doc_new is None or kind == "classm" or (doc_old is None):
            continue
        if kind == "render" and new.read(*new.dir("rendered", fid), fid + ".md") is None:
            continue
        keys_new = compared_keys(kind, new, doc_new)
        for k in sorted(set(keys_new) - {l["key"] for l in index["lines"]}):
            rec["review"].append((k, keys_new[k], "a compared line with no review in " + old.year))
        rec["rest"] = rest_carries(old, new, doc_old, doc_new)
    return out


def rest_carries(old, new, doc_old, doc_new):
    """Whether the document's own fields (outside every compared line: subjects.REST_KEY) are equal in
    both years, its own tax_year normalized (own_year) and any other moved year where the document's cited
    source moved it."""
    import subjects
    view = lambda d: json.dumps(subjects._without_cites(subjects._unworded({k: v for k, v in d.items() if k != "lines"})),
                                sort_keys=True, ensure_ascii=False, indent=0)
    evidence = set()
    for la, lb in zip(doc_old["lines"], doc_new["lines"]):
        for (_, ta), (_, tb) in zip(section_texts(old, la), section_texts(new, lb)):
            evidence |= shifts(ta, tb, old.year)[2]
    a, b = project_pair(*own_year("rest", view(doc_old), view(doc_new), old.year), old.year, evidence)
    return a == b


def write(kind, old, new_year, result):
    """Write each form's carried lines into its TY+1 index: the TY entries of the lines that carry (same
    record, status and ruling), each marked (year_marked), and the TY+1 line subjects, rest and
    foreign interfaces of the lines written, then its rulings sidecar (write_sidecar); a form with no carried
    line gets neither."""
    import subjects
    import review_store
    import rulings
    written = []
    for fid, rec in sorted(result.items()):
        if not rec["carry"]:
            continue
        index = json.loads(old.read(*old.dir("reviews"), kind, fid + ".index.json"))
        carried = {k: key for k, _, key in rec["carry"]}
        lines = [year_marked(l, old.year, carried[l["key"]]) for l in index["lines"] if l["key"] in carried]
        out = {**index, "lines": lines, "carried_from": old.year, "base_sources": index.get("base_sources") or old.year}
        if kind != "classm" and index.get("subjects") is not None:
            cur, rest = subjects.current_line_subjects(kind, fid, new_year)
            out["subjects"] = {k: v for k, v in cur.items() if k in carried}
            if rec.get("rest"):
                out["__rest__"] = rest  # else the earlier year's: check_logs asks for the whole review
            if kind == "transcription":
                fo = subjects.current_foreign(fid, new_year)
                out["foreign"] = {k: v for k, v in fo.items() if k in carried}
            for l in lines:
                l["subject_key"] = review_store.subject_key(out["subjects"].get(l["key"]), (out.get("foreign") or {}).get(l["key"]))
        moved = whole_carried(kind, old, new_year, fid, index, rec)
        if moved:
            out["subject_carried"] = moved
        path = os.path.join(rulings.REVIEWS, kind, fid + ".index.json")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(out, f, indent=1, ensure_ascii=False)
            f.write("\n")
        written.append(path)
        side = write_sidecar(kind, old, fid)
        if side:
            written.append(side)
    return written


def whole_carried(kind, old, new_year, fid, index, rec):
    """The whole-form subject a render index with no line subjects carries to TY+1 (`subject_carried`, which
    review_store.recorded_subject reads), else None. Such an index answers the whole rendering, which names the
    tax year. It carries only when every compared line carries, the TY index answered the TY rendering, and
    the two renderings (citations left out, as subjects.of_rendered) are equal once a year is normalized in
    lockstep where the document's cited sources moved it (project_pair, as rest_carries)."""
    import review_store
    import subjects
    if kind != "render" or index.get("subjects") is not None or rec["review"] or not rec["carry"]:
        return None
    was = review_store.recorded_subject(kind, index)
    text_old = old.read(*old.dir("rendered", fid), fid + ".md")
    new = Tree(ROOT, new_year)
    text_new = new.read(*new.dir("rendered", fid), fid + ".md")
    if not was or text_old is None or text_new is None or subjects.of_rendered(text_old) != was:
        return None
    doc_old, doc_new = old.docs().get(fid), new.docs().get(fid)
    evidence = set()
    for la, lb in zip(doc_old["lines"], doc_new["lines"]):
        for (_, ta), (_, tb) in zip(section_texts(old, la), section_texts(new, lb)):
            evidence |= shifts(ta, tb, old.year)[2]
    if not renderings_carry(text_old, text_new, old.year, evidence):
        return None
    header = review_store.recorded_subject(kind, {k: v for k, v in index.items() if k != "subject_carried"})
    return {"subject": subjects.of_rendered(text_new), "was": header,
            "carried": {"by": "year", "from": old.year, **({"after": index["subject_carried"]["carried"]}
                                                           if index.get("subject_carried") else {})}}


# The document's own tax year, which adoption writes (year_diff.py --adopt): the rendered header line and the
# `tax_year` field of a document's own fields. It is normalized without source evidence, from TY to TY+1 only.
OWN_YEAR = {"render": re.compile(r"(?m)^(- Document: `[^`]+` \([^,()]+, tax year )(\d{4})(\))$"),
            "rest": re.compile(r'("tax_year": )(\d{4})(?!\d)()')}


def own_year(kind, text_old, text_new, ty):
    """Both texts with the document's own tax year (OWN_YEAR) replaced by {Y} where it is TY in the old text and
    TY+1 in the new; any other year there is left as it is."""
    pat, ty = OWN_YEAR[kind], int(ty)
    mark = lambda year: lambda m: m.group(1) + ("{Y}" if int(m.group(2)) == year else m.group(2)) + m.group(3)
    return pat.sub(mark(ty), text_old), pat.sub(mark(ty + 1), text_new)


def renderings_carry(text_old, text_new, ty, evidence):
    """Whether two years' renderings of a document are equal, citations left out (subjects.of_rendered), once the
    header's own tax year is normalized (own_year) and any other year in lockstep where the cited sources moved it
    (`evidence`, as shifts returns it)."""
    import subjects
    a, b = own_year("render", subjects.CITE_TEXT.sub("[cite]", text_old), subjects.CITE_TEXT.sub("[cite]", text_new), ty)
    a, b = project_pair(a, b, ty, evidence)
    return a == b


def year_marked(line, from_year, year_key):
    """An index line as carried to TY+1: marked `carried` {from, year_key}; a line shown from a renamed record
    section (`section`) keeps the rename carry that maps that section to its key (review_store.check) and is
    marked `year_carried` instead. A line already carried from an earlier year keeps, as `sources`, the year
    whose archive its record was made against, which check_logs.py checks the record's source pages against."""
    prev = line.get("year_carried") or line.get("carried")
    prev = prev if prev and "year_key" in prev else None
    mark = {"from": from_year, "year_key": year_key}
    if prev:
        mark["sources"] = prev.get("sources") or prev["from"]
    return {**line, "year_carried": mark} if line.get("section") else {**line, "carried": mark}


def write_sidecar(kind, old, fid):
    """Write a form's TY+1 rulings sidecar from its TY one, after its TY+1 index is written: the TY entries
    (same key, ruling, context and stamps) of the rulings the carried log shows, so that each ruling in the
    log is in the sidecar (rulings.check). Returns its path, or None when the TY form has no sidecar."""
    import rulings
    src = old.path(*old.dir("reviews"), kind, fid + ".rulings.json")
    if not os.path.exists(src):
        return None
    data = json.load(open(src, encoding="utf-8"))
    text = rulings.read_log(kind, fid)
    shown = {rulings.stored_key(kind, k) for k, line in rulings.log_sections(kind, text or "") if line != rulings.OPEN}
    fields = rulings.stored_fields(kind)
    rows = [r for r in (rulings.compact_row(kind, r) for r in data["rulings"]) if tuple(r[f] for f in fields) in shown]
    path = rulings.sidecar_path(kind, fid)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"kind": kind, "form": fid, "carried_from": old.year, "rulings": rows}, f, indent=1, ensure_ascii=False)
        f.write("\n")
    return path


def report(kind, result, from_year, to_year, verbose=False):
    carry = sum(len(r["carry"]) for r in result.values())
    review = sum(len(r["review"]) for r in result.values())
    whole = sorted(f for f, r in result.items() if r["carry"] and not r["review"])
    none = sorted(f for f, r in result.items() if r["review"] and not r["carry"])
    reasons, waiting = {}, 0
    for r in result.values():
        for _, _, why in r["review"]:
            heads = {part.split(":")[0] for part in (why or "").split("; ")}
            for head in heads:
                reasons[head] = reasons.get(head, 0) + 1
            waiting += heads <= set(WAITING)
    lines = [f"# Year carry {from_year} -> {to_year}: {kind}", "",
             f"{carry} compared lines carry, {review} need a review; {len(whole)} forms carry whole, "
             f"{len(none)} need a review of every line, {len(result) - len(whole) - len(none)} in part. Of the lines "
             f"to review, {waiting} wait only on a {to_year} source not yet archived or a {to_year} value not yet set; "
             f"{review - waiting} have a difference in what is archived and set.", "",
             "Reasons a line needs a review (a line may have several):", ""]
    lines += [f"- {k}: {v}" for k, v in sorted(reasons.items(), key=lambda kv: -kv[1])]
    lines += ["", "| form | carry | review | lines carried (for spot review) | reasons to review (lines) |", "| --- | --- | --- | --- | --- |"]
    for fid, r in sorted(result.items()):
        heads = {}
        for _, _, why in r["review"]:
            for h in {part.split(":")[0] for part in (why or "").split("; ")}:
                heads[h] = heads.get(h, 0) + 1
        lines.append(f"| {fid} | {len(r['carry'])} | {len(r['review'])} | {', '.join(k for k, _, _ in r['carry']) or '-'} | "
                     + ("; ".join(f"{h} ({n})" for h, n in sorted(heads.items(), key=lambda kv: -kv[1])) or "-") + " |")
    if verbose:
        lines += ["", "## Every line to review, with its reasons", ""]
        lines += [f"- {fid} {k}: {w}" for fid, r in sorted(result.items()) for k, _, w in r["review"]]
    return "\n".join(lines) + "\n", carry, review


# ---------------------------------------------------------------- self-test

def self_test():
    """Near-miss pairs: each must carry or not as stated."""
    pol = {"p": 1}
    page = lambda *paras: list(paras)

    def line_parts(subject, cited, vals=None):
        return {"subject": subject, "values": vals or {}, "cited": cited, "policies": pol}

    known = {"Line 3", "Line 4", "Line 5", "Line 6", "Line 19"}
    sec = lambda text, anchor="Line 5": [("i1 " + anchor, anchor_section(text, anchor, known))]
    base = "Line 5 Enter the amount from your 2025 Form W-2.\nLine 6 Add lines 4 and 5."
    xref = "Line 4 Enter your wages.\nLine 5 Subtract Line 4 from Line 3.\nDo not enter less than zero.\nLine 6 Add lines 4 and 5."
    wrapped = "Line 5 Enter the amount figured by subtracting\nLine 4 from Line 3.\nDo not enter less than zero.\nLine 6 Add."
    cases = [
        ("unchanged but the year: rolling 2025 -> 2026 in source and project", True,
         line_parts('{"source": "Amount paid in 2025"}', sec(base)),
         line_parts('{"source": "Amount paid in 2026"}', sec(base.replace("2025", "2026")))),
        ("a paragraph added under the same heading", False,
         line_parts("s", sec(base)),
         line_parts("s", sec(base.replace("Form W-2.", "Form W-2. Include tips reported to your employer.")))),
        ("a paragraph added under the next heading only", True,
         line_parts("s", sec(base)),
         line_parts("s", sec(base + " Include line 4 only once."))),
        ("a sentence changed after a cross-reference to another known anchor in the section", False,
         line_parts("s", sec(xref)),
         line_parts("s", sec(xref.replace("less than zero.", "less than zero. If zero, skip line 6.")))),
        ("a sentence changed after a cross-reference wrapped to the start of a line", False,
         line_parts("s", sec(wrapped)),
         line_parts("s", sec(wrapped.replace("less than zero.", "more than $500.")))),
        ("a sentence changed under the next heading, the section holding a cross-reference", True,
         line_parts("s", sec(xref)),
         line_parts("s", sec(xref.replace("Add lines 4 and 5.", "Add lines 4 and 5 and enter the total.")))),
        ("the anchor printed with other spacing and case; text under the next heading changed", True,
         line_parts("s", sec("CHART \u2014 LINE 18a Use the chart.\nLine 19 Enter.", "Chart—Line 18a")),
         line_parts("s", sec("CHART \u2014 LINE 18a Use the chart.\nLine 19 Enter, unless you file Form 2555.", "Chart—Line 18a"))),
        ("the anchor printed with other spacing and case; text under it changed", False,
         line_parts("s", sec("CHART \u2014 LINE 18a Use the chart.\nLine 19 Enter.", "Chart—Line 18a")),
         line_parts("s", sec("CHART \u2014 LINE 18a Use the chart, unless you file Form 2555.\nLine 19 Enter.", "Chart—Line 18a"))),
        ("a changed parameter value", False,
         line_parts("s", sec(base), {"param s1a.tip_limit": 25000}),
         line_parts("s", sec(base), {"param s1a.tip_limit": 25750})),
        ("a fixed statutory date the project incremented", False,
         line_parts('{"source": "Placed in service after January 19, 2025"}',
                    [("i4562 p", "property placed in service after January 19, 2025, in 2025")]),
         line_parts('{"source": "Placed in service after January 19, 2026"}',
                    [("i4562 p", "property placed in service after January 19, 2025, in 2026")])),
        ("a fixed statutory date kept literal", True,
         line_parts('{"source": "Placed in service after January 19, 2025"}',
                    [("i4562 p", "property placed in service after January 19, 2025, in 2025")]),
         line_parts('{"source": "Placed in service after January 19, 2025"}',
                    [("i4562 p", "property placed in service after January 19, 2025, in 2026")])),
        ("a birth-year cutoff that moved (outside the window)", False,
         line_parts('{"source": "Were you born before January 2, 1961?"}', [("i1040 p", "born before January 2, 1961")]),
         line_parts('{"source": "Were you born before January 2, 1962?"}', [("i1040 p", "born before January 2, 1962")])),
        ("a rolling year the project did not move", False,
         line_parts('{"source": "Amount paid in 2025"}', [("p", "Amounts paid in 2025 qualify")]),
         line_parts('{"source": "Amount paid in 2025"}', [("p", "Amounts paid in 2026 qualify")])),
        ("a year that moved by 2", False,
         line_parts("s", [("p", "in 2025")]), line_parts("s", [("p", "in 2027")])),
    ]
    bad = []
    for name, want, a, b in cases:
        got = compare_parts("2025", a, b)
        if got[0] != want:
            bad.append(f"{name}: carried={got[0]} ({got[1]})")
        if want and got[2] != got[3]:
            bad.append(f"{name}: carried with unequal keys")
    table = ("# 2025 Table\ntable:\n  id: t\n  title: \"2025 Table\"\n  tax_year: 2025\n"
             "  cite: { doc: d, locator: '2025 Table' }\n  bands:\n    - { at_least: 0, less_than: 100, tax: [5] }\n")
    tables = [("a table whose title, citation, comment and tax year moved", True,
               table.replace("2025", "2026")),
              ("a table with a band amount changed", False, table.replace("tax: [5]", "tax: [6]"))]
    for name, want, other in tables:
        if (table_value(table) == table_value(other)) != want:
            bad.append(f"{name}: equal={not want}")
    n = len(cases) + len(tables)
    head = "# Form X\n\n- Document: `x` (form, tax year {y})\n\n## Line 1\n\nEnter the amount{extra}.\n"
    moved = shifts("Enter your 2025 amounts.", "Enter your 2026 amounts.", "2025")[2]
    kept = shifts("Enter your 2025 amounts. For tax year 2025, see Pub. 1.", "Enter your 2026 amounts. For tax year 2025, see Pub. 1.", "2025")[2]
    none = shifts("Enter it.", "Enter it.", "2025")[2]
    renders = [("a rendering whose header year moved where the sources moved the year", True, moved, 2026, ""),
               ("only the header year moved, the sources printing no year", True, none, 2026, ""),
               ("only the header year moved, the sources keeping it in the same words", True, kept, 2026, ""),
               ("the header year moved by two", False, moved, 2027, ""),
               ("the header year moved and a sentence changed", False, none, 2026, " shown on Form W-2"),
               ("the header year moved and a year in the text moved, the sources moving no year", False, none, 2026,
                " paid in 2026")]
    for name, want, evidence, y, extra in renders:
        new_text = head.format(y=y, extra=extra)
        old_text = head.format(y=2025, extra=" paid in 2025" if "paid in" in extra else "")
        if renderings_carry(old_text, new_text, "2025", evidence) != want:
            bad.append(f"{name}: carried={not want}")
    rest = lambda y, title: json.dumps({"id": "x", "tax_year": y, "title": title}, sort_keys=True, indent=0)
    rests = [("a document's own fields with only tax_year moved, the sources printing no year", True, rest(2026, "X")),
             ("tax_year moved and the title changed", False, rest(2026, "Y")),
             ("tax_year moved by two", False, rest(2027, "X"))]
    for name, want, new_text in rests:
        a, b = project_pair(*own_year("rest", rest(2025, "X"), new_text, "2025"), "2025", none)
        if (a == b) != want:
            bad.append(f"{name}: carried={not want}")
    n += len(renders) + len(rests)
    for b in bad:
        print("year-carry self-test: WRONG", b, file=sys.stderr)
    print(f"year-carry self-test: {n - len(bad)}/{n} near-miss pairs as expected")
    drafts = pages_self_test()
    print("year-carry self-test: a draft's pages read without its cover and watermarks: "
          + ("as expected" if not drafts else "WRONG: " + "; ".join(drafts)))
    side = sidecar_self_test()
    print("year-carry self-test: rulings sidecar and line marks written with the carried index: "
          + ("as expected" if not side else "WRONG: " + "; ".join(side)))
    return 1 if bad or side or drafts else 0


def pages_self_test():
    """Tree.pages in a scratch tree: a draft's reading-order text is read through archive_text (cover page
    emptied, watermarks removed), a final edition's as extracted. Returns what went wrong."""
    import tempfile
    page = "Line 5 Enter TREASURY/IRS AND OMB USE ONLY DRAFT the amount."
    with tempfile.TemporaryDirectory() as tmp:
        tree = Tree(tmp, "2025")
        archive = tree.path("sources", "2025")
        os.makedirs(archive)
        for name in ("d.cols.txt", "f.cols.txt"):
            with open(os.path.join(archive, name), "w", encoding="utf-8") as f:
                f.write(archive_text.DRAFT_COVER + "\f" + page)
        with open(os.path.join(archive, "manifest.json"), "w", encoding="utf-8") as f:
            json.dump({"documents": [{"id": "d", "file": "d.pdf", "text_file": "d.txt", "cols_file": "d.cols.txt", "draft": True},
                                     {"id": "f", "file": "f.pdf", "cols_file": "f.cols.txt"}]}, f)
        draft, final, absent = tree.pages("d"), tree.pages("f"), tree.pages("x")
    bad = []
    if draft is None or draft[0] != "" or "DRAFT" in "".join(draft):
        bad.append(f"draft read as {draft}")
    if final != [archive_text.DRAFT_COVER, page]:
        bad.append(f"final edition read as {final}")
    if absent is not None:
        bad.append(f"a document not archived read as {absent}")
    return bad


def sidecar_self_test():
    """write_sidecar in a scratch tree: of a TY sidecar's entries, those whose ruling the carried log shows
    are written to TY+1, as stored (key, ruling, context, stamps); an entry for a line the log does not show,
    and an open section, are not. Returns what went wrong."""
    import tempfile
    import rulings
    section = lambda printed, project, ruling: (f"\n### {printed} — x\nStatus: **DISAGREE**\n\nProject:\n\n```json\n"
                                                f"{project}\n```\n\nSecond:\n\n```json\n2\n```\n\n{ruling}\n")
    log = "# Log\n\n## Lines\n" + section("1", "1", "Ruling: representation") + section("3", "3", rulings.OPEN)
    row = lambda printed, project, ruling: {"printed": printed, "project_expr_sha256": rulings._sha_text(project),
                                            "second_expr_sha256": rulings._sha_text("2"), "ruling": ruling,
                                            "context": "c", "date": "2025-12-01"}
    old_rows = [row("1", "1", "Ruling: representation"), row("2", "2", "Ruling: equivalent"),
                row("3", "3", "Ruling: equivalent")]
    saved = rulings.read_log, rulings.sidecar_path
    with tempfile.TemporaryDirectory() as tmp:
        old = Tree(os.path.join(tmp, "old"), "2025")
        os.makedirs(old.path(*old.dir("reviews"), "transcription"))
        with open(old.path(*old.dir("reviews"), "transcription", "fx.rulings.json"), "w") as f:
            json.dump({"kind": "transcription", "form": "fx", "rulings": old_rows}, f)
        rulings.read_log = lambda kind, form, family=None: log
        rulings.sidecar_path = lambda kind, form, family=None: os.path.join(tmp, "fx.rulings.json")
        try:
            path = write_sidecar("transcription", old, "fx")
            got = json.load(open(path))
        finally:
            rulings.read_log, rulings.sidecar_path = saved
    bad = [] if got["rulings"] == old_rows[:1] and got.get("carried_from") == "2025" else [f"rulings sidecar carried as {got}"]
    renamed = year_marked({"key": "k", "section": "s", "carried": {"by": "rename", "keys": {"s": "k"}}}, "2025", "h")
    plain = year_marked({"key": "k", "carried": {"by": "rename"}}, "2025", "h")
    if renamed["carried"].get("by") != "rename" or renamed.get("year_carried") != {"from": "2025", "year_key": "h"} \
            or plain["carried"] != {"from": "2025", "year_key": "h"}:
        bad.append(f"index lines marked as {renamed} and {plain}")
    again, renamed_again = year_marked(plain, "2026", "i"), year_marked(renamed, "2026", "i")
    if again["carried"] != {"from": "2026", "year_key": "i", "sources": "2025"} \
            or renamed_again["year_carried"] != {"from": "2026", "year_key": "i", "sources": "2025"}:
        bad.append(f"lines carried a second year marked as {again} and {renamed_again}")
    return bad


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--from", dest="origin", help="the tree of tax year TY (default: none; required unless --self-test)")
    ap.add_argument("--from-year", help="TY (default: the year before this tree's)")
    ap.add_argument("--kind", choices=("transcription", "render", "classm"), action="append")
    ap.add_argument("--write", action="store_true", help="write the carried entries into this tree's indexes and rulings sidecars")
    ap.add_argument("--report", help="write the report here (default: print it)")
    ap.add_argument("--verbose", action="store_true", help="list every line to review with its reasons in the report")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    if not a.origin:
        ap.error("--from is required")
    new_year = str(Y)
    jurisdiction.require_year(new_year, "year_carry")
    old = Tree(os.path.abspath(a.origin), a.from_year or str(int(new_year) - 1))
    new = Tree(ROOT, new_year)
    texts = []
    for kind in a.kind or ["transcription", "render", "classm"]:
        result = plan(kind, old, new)
        text, carry, review = report(kind, result, old.year, new.year, a.verbose)
        texts.append(text)
        print(text.split("\n")[2])
        if a.write:
            paths = write(kind, old, new.year, result)
            sides = sum(p.endswith(".rulings.json") for p in paths)
            print(f"{kind}: wrote {len(paths) - sides} indexes and {sides} rulings sidecars")
    if a.report:
        with open(a.report, "w", encoding="utf-8") as f:
            f.write("\n".join(texts))
    return 0


if __name__ == "__main__":
    sys.exit(main())
