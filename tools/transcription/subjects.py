"""What each kind of review judges, as a hash: the "subject sha256" every review log
records, so that check_logs.py can tell when a log no longer describes the data.

  transcription  the form's definition, citations left out (tools/citations.py checks them)
  render         the rendered English (rendered/<year>/<form>.md), citations left out
  classm         what the hand-work computes: each line's id, type and expression,
                 without an input's question wording, plus explicit when_known consistency modes

A change to the review tool's prompt or to the pages a citation names does not
change a subject: those are deliberate and rerun deliberately.
"""
import hashlib
import json
import os
import re

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# A rendered citation runs from its [doc] tag to "; sha256 <hex>)"; the document details may
# themselves contain parentheses ("January 2024 (continuous-use form)").
CITE_TEXT = re.compile(r"\[[a-z0-9-]+\] [^\n]*?; sha256 [0-9a-f]+\)")


def _sha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def _without_cites(o):
    if isinstance(o, dict):
        return {k: _without_cites(v) for k, v in o.items() if k != "cite"}
    if isinstance(o, list):
        return [_without_cites(x) for x in o]
    return o


def of_form(yaml_text):
    return _sha(_without_cites(yaml.safe_load(yaml_text)))


def of_rendered(md_text):
    return hashlib.sha256(CITE_TEXT.sub("[cite]", md_text).encode()).hexdigest()


def of_computation(yaml_text):
    raw = yaml.safe_load(yaml_text)
    doc = raw.get("form") or raw.get("def")
    rows = [{"id": l.get("id"), "type": l.get("type"),
             "expr": {k: v for k, v in (l.get("expr") or {}).items() if k != "source"},
             **({"when_known": [r["when"] for r in l.get("refuses", []) if r.get("when_known")]}
                if any(r.get("when_known") for r in l.get("refuses", [])) else {})}
            for l in doc.get("lines", [])]
    return _sha(rows)


def path(kind, fid, year):
    if kind == "render":
        return os.path.join(ROOT, "rendered", str(year), fid + ".md")
    return os.path.join(ROOT, "forms", str(year), fid + ".yaml")


def of_text(kind, text):
    return {"transcription": of_form, "render": of_rendered, "classm": of_computation}[kind](text)


def current(kind, fid, year):
    """The subject hash of a form as it is now."""
    return of_text(kind, open(path(kind, fid, year), encoding="utf-8").read())


# ---------- per-line subjects ----------
#
# A transcription or render log may review some lines again after a change (a line-scoped
# review) and keep the verdicts of the rest. It then records, per compared line, the hash of
# what that line's verdict depends on within the document, and one hash for the rest of the
# document, in a "## Line subjects" table:
#
#   transcription  the line and what it reads within the document as the comparison expands it:
#                  its helper and input lines, followed through helpers (any in-document line id
#                  named anywhere in an expression, refusals or shown_when), and, of each other
#                  printed computed line reached, only its id, printed marker and type (the
#                  comparison references a printed line by its marker); in a shared definition
#                  every line is followed. Citations left out;
#   render         the line's rendered section and the sections of the in-document glossary
#                  entries it names (render_compare.glossary, which stops at the document's other
#                  judged lines), citations left out;
#   rest           the document's own fields without its lines (transcription), or the rendered
#                  head before the first line (render). A line no compared line reaches enters no
#                  verdict of this review (the reviews of the documents that read it judge it).
#
# Like the whole-document subject, lines of other documents are not included.

LINE_SUBJECTS = "## Line subjects"
REST_KEY = "(rest of the document)"
SUBJECT_ROW = re.compile(r"^\| (.+?) \| ([0-9a-f]{64}) \|$", re.M)


def _strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for k, v in o.items():
            if k not in ("cite", "source", "label", "help", "note"):
                yield from _strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from _strings(v)


HELPER_PRINTED = ("(helper)", "(gate)", "(computed helper)")   # transcribe.HELPER_PRINTED


def reach(doc, line_id):
    """(members, boundary) of a line: the ids of the line and of the helper and input lines of the
    same document it reads, followed through helpers; and the other printed computed lines it reads,
    which are not followed. In a shared definition every line is followed (no boundary)."""
    by_id = {l["id"]: l for l in doc["lines"]}
    whole = doc.get("kind") == "def"
    members, boundary, todo = set(), set(), [line_id]
    while todo:
        cur = todo.pop()
        if cur in members or cur in boundary or cur not in by_id:
            continue
        line = by_id[cur]
        if (cur != line_id and not whole and str(line.get("printed")) not in HELPER_PRINTED
                and (line.get("expr") or {}).get("op") != "input"):
            boundary.add(cur)
            continue
        members.add(cur)
        todo.extend(x for x in _strings({k: v for k, v in line.items() if k != "id"}) if x in by_id)
    return members, boundary


def closure(doc, line_id):
    """Every in-document line id a line reads as the comparison expands it (reach), boundary included."""
    members, boundary = reach(doc, line_id)
    return members | boundary


def _doc(yaml_text):
    raw = yaml.safe_load(yaml_text)
    return raw.get("form") or raw.get("def"), ("form" if "form" in raw else "def")


def transcription_line_subjects(yaml_text, targets):
    """({line id: subject} for each target id present, rest subject) of a form's YAML."""
    doc, wrapper = _doc(yaml_text)
    by_id = {l["id"]: l for l in doc["lines"]}
    out = {}
    for t in targets:
        if t not in by_id:
            continue
        members, boundary = reach(doc, t)
        out[t] = _sha([_without_cites(by_id[i]) for i in sorted(members)] +
                      [{"boundary": i, "printed": str(by_id[i]["printed"]), "type": by_id[i]["type"]} for i in sorted(boundary)])
    return out, _sha({wrapper: _without_cites({k: v for k, v in doc.items() if k != "lines"})})


def rendered_sections(md_text):
    """(head, {line id: section text}) of a rendered document; a section runs from its "## " heading."""
    parts = re.split(r"(?m)^(?=## )", md_text)
    head, sections = parts[0], {}
    for sec in parts[1:]:
        m = re.match(r"## .+? — `([^`]+)`\s*$", sec.partition("\n")[0])
        if m:
            sections[m.group(1)] = sec
        else:
            head += sec
    return head, sections


def render_line_subjects(fid, md_text, targets):
    """({line id: subject} for each target id present, rest subject) of a rendered document."""
    import render_compare as R
    head, sections = rendered_sections(md_text)
    saved = R._rendered_cache.get(fid)
    R._rendered_cache[fid] = R.parse_rendered_text(md_text)
    try:
        entries = R._rendered_cache[fid]
        judged = {e["id"] for e in R.judged_entries(entries)}
        out = {}
        for t in targets:
            if t not in sections or t not in entries:
                continue
            ids = {t} | {e["id"] for gfid, e in R.glossary(fid, [entries[t]], stop=judged) if gfid == fid}
            out[t] = hashlib.sha256("".join(CITE_TEXT.sub("[cite]", sections[i]) for i in sorted(ids)).encode()).hexdigest()
    finally:
        if saved is None:
            R._rendered_cache.pop(fid, None)
        else:
            R._rendered_cache[fid] = saved
    return out, hashlib.sha256(CITE_TEXT.sub("[cite]", head).encode()).hexdigest()


def target_keys(kind, fid):
    """[(log key, line id)] of the lines a review of the current document compares, in log order."""
    if kind == "transcription":
        import transcribe as T
        return T.line_keys(T.load_form(fid))
    import render_compare as R
    import transcribe as T
    return [(e["key"], e["id"]) for e in R.judged_lines(T.load_form(fid))]


def line_subjects_of(kind, fid, text, keys):
    """({log key: subject}, rest subject) of a document's text (YAML or rendered English)."""
    ids = [i for _, i in keys]
    per_id, rest = (transcription_line_subjects(text, ids) if kind == "transcription"
                    else render_line_subjects(fid, text, ids))
    return {k: per_id[i] for k, i in keys if i in per_id}, rest


def current_line_subjects(kind, fid, year):
    keys = target_keys(kind, fid)
    return line_subjects_of(kind, fid, open(path(kind, fid, year), encoding="utf-8").read(), keys)


def table(per_key, rest):
    """The "## Line subjects" section of a log."""
    out = [LINE_SUBJECTS, "",
           "What each compared line's verdict depends on within the document (tools/transcription/subjects.py); "
           "a line-scoped review reruns the lines whose hash changed.", "",
           "| line | subject sha256 |", "| --- | --- |"]
    out += [f"| {k} | {v} |" for k, v in per_key.items()]
    out += [f"| {REST_KEY} | {rest} |", ""]
    return out


def table_for(kind, fid, year):
    """The current "## Line subjects" section of a document's log; none for a document with no
    file (a synthetic test document)."""
    if not os.path.exists(path(kind, fid, year)):
        return []
    return table(*current_line_subjects(kind, fid, year))


def recorded(text):
    """({log key: subject}, rest subject) from a log's "## Line subjects" table, or None."""
    _, sep, tail = text.partition("\n" + LINE_SUBJECTS + "\n")
    if not sep:
        return None
    body = re.split(r"\n## ", tail, maxsplit=1)[0]
    rows = dict((k, v) for k, v in SUBJECT_ROW.findall(body))
    rest = rows.pop(REST_KEY, None)
    return rows, rest


def has_line_scoped_passes(text):
    return "\n## Line-scoped reviews\n" in text


def stale_lines(kind, fid, year, text):
    """(stale keys, rest changed, keys no longer compared) of a log against the current document,
    from its line-subject table; None when the log has no table."""
    rec = recorded(text)
    if rec is None:
        return None
    rows, rest = rec
    cur, cur_rest = current_line_subjects(kind, fid, year)
    stale = [k for k in cur if rows.get(k) != cur[k]]
    return stale, rest != cur_rest, sorted(set(rows) - set(cur))


def log_state(kind, fid, year, text):
    """None when a log describes the current document, else what is stale. A log reviewed whole
    is current when its subject is; a log with line-scoped reviews, or a reviewed-whole log whose
    subject changed, is current when every compared line's subject and the rest are."""
    subject = re.search(r"^\| subject sha256 \| ([0-9a-f]{64}) \|$", text, flags=re.M)
    if not subject:
        return f"the {kind} log records no subject hash (tools/transcription/subjects.py)"
    what = {"transcription": "form", "render": "rendered English", "classm": "computation"}[kind]
    whole = subject.group(1) == current(kind, fid, year)
    if kind == "classm" or (whole and not has_line_scoped_passes(text)):
        return None if whole else f"the {kind} log reviewed an earlier {what} of {fid}; rerun the review"
    found = stale_lines(kind, fid, year, text)
    if found is None:
        return None if whole else f"the {kind} log reviewed an earlier {what} of {fid}; rerun the review"
    stale, rest_changed, gone = found
    if rest_changed:
        return f"the {kind} log reviewed an earlier {what} of {fid} outside every compared line; rerun the whole review"
    if stale or gone:
        parts = ([f"lines changed or not yet reviewed: {', '.join(stale)}"] if stale else []) + \
                ([f"lines no longer compared: {', '.join(gone)}"] if gone else [])
        tool = "transcribe.py" if kind == "transcription" else "render_compare.py"
        return f"the {kind} log is stale for {'; '.join(parts)}; rerun them: {tool} --form {fid} --lines auto"
    return None
