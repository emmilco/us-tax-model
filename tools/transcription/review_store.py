#!/usr/bin/env python3
"""Review records and per-form indexes: the committed form of the transcription, render and class M
reviews (the review store design, section 2.2).

    reviews/store/<kind>/<record-sha>.md          one pass, stored once and never rewritten
    reviews/<year>/<kind>/<stem>.index.json       per form and family (New York: reviews/ny/<year>/...)

A record is one pass: a whole-form review (its header, source pages, catalog and checks, the sections of
the lines it judged, the gate rows it listed for them, and its raw reply) or a line-scoped pass (its block
and the sections and gate rows of the lines it judged). A class M pass is whole-form. A section is stored
with its ruling line as "Ruling: open": rulings are written later and live in the index. `record-sha`
hashes the pass's identity: kind, form, family, scope, each scoped line's subject key, prompt sha,
response sha and policy versions (identity()). The file holds that identity and the pass's parts.

The index maps each compared line, in section order, to {key, record, status, ruling, subject_key}, with
the line subjects (`subjects`, the per-line hashes of subjects.py), the rest of the document (`__rest__`),
the foreign interfaces of transcription lines (`foreign`), the whole-form record the view's header comes
from (`base`) and the header rows a later pass rewrote (`head_rows`). A line's `subject_key` folds its line
subject and its foreign interfaces together.

The per-form log is a view, generated, not committed: view() assembles it from the index and the records it
names, byte for byte as the review tools wrote it; ingest() takes a log a tool wrote (or rule.py ruled) and
stores what is new in it, verifying that the view reproduces it. `render` writes the views to the
git-ignored .transcription/logs/<year>/<kind>/<stem>.md.

    review_store.py render [--kind K] [--form F]   write views (every form of every kind by default)
    review_store.py migrate                         store every committed log (*.md) and remove it
    review_store.py check                           every index's records exist and its view parses back
"""
import argparse, hashlib, json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import families  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from taxyear import Y  # noqa: E402
import jurisdiction  # noqa: E402

KINDS = ("transcription", "render", "classm")
RAW_HEADINGS = {"transcription": "## Raw second transcription", "render": "## Raw response", "classm": "## Raw responses"}
PASS_HEADING = "## Line-scoped reviews"
GATES_HEADING = "## Refusal gates listed by the second transcription"
LINE_SUBJECTS = "## Line subjects"
FOREIGN = "## Foreign interfaces"
TAG_RE = re.compile(r"^Reviewed in: pass ([0-9a-f]{12})$", re.M)
RULING_RE = re.compile(r"^Ruling: .*$", re.M)
PART = re.compile(r"^<!-- part (.+?) -->$", re.M)
OPEN = "Ruling: open"
REVIEWS_TOP = os.path.join(ROOT, "reviews")


def _reviews():
    import rulings
    return rulings.REVIEWS


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _inside(path, top):
    path, top = os.path.realpath(path), os.path.realpath(top)
    return path == top or path.startswith(top + os.sep)


def store_dir(kind):
    """reviews/store/<kind>; beside the reviews directory when that is elsewhere (a test's)."""
    reviews = _reviews()
    base = os.path.join(REVIEWS_TOP, "store") if _inside(reviews, REVIEWS_TOP) else os.path.join(reviews, "store")
    return os.path.join(base, kind)


def record_path(kind, sha):
    return os.path.join(store_dir(kind), sha + ".md")


def index_path(kind, form, family=families.DEFAULT):
    return os.path.join(_reviews(), kind, families.stem(form, family) + ".index.json")


def view_path(kind, form, family=families.DEFAULT):
    """Where `render` writes a form's view: under .transcription/logs/ (git-ignored), or beside the
    index when the reviews directory is elsewhere (a test's)."""
    reviews = _reviews()
    if _inside(reviews, REVIEWS_TOP):
        top = os.path.join(VIEWS_TOP, os.path.relpath(os.path.realpath(reviews), os.path.realpath(REVIEWS_TOP)))
    else:
        top = reviews
    return os.path.join(top, kind, families.stem(form, family) + ".md")


VIEWS_TOP = os.path.join(ROOT, ".transcription", "logs")


def is_view(path):
    """Whether a path is a generated view (under .transcription/logs/), which is never read as a record."""
    return _inside(path, VIEWS_TOP)


def _sha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def subject_key(line_subject, foreign):
    """A compared line's subject key: its line subject with its foreign interfaces folded in."""
    if line_subject is None:
        return None
    return _sha([line_subject, foreign])


# ---------------------------------------------------------------- parsing a log

def section_key(kind, part):
    """The key of a section (its text after "### "): the printed handle, or for class M the case and
    handle ("<case> — <printed>") or the case heading ("case <id>")."""
    title = part.partition("\n")[0]
    bits = title.split(" — ")
    if kind == "classm":
        return bits[0] if title.startswith("case ") else " — ".join(bits[:2])
    return bits[0]


def _rows(text):
    """[(name, value)] of the field table rows of a header or block."""
    return re.findall(r"^\| ([^|\n]+?) \| (.*?) \|$", text.split("\n\n## ")[0].split("\n\n##### ")[0], re.M)


def row(text, name):
    m = re.search(rf"^\| {re.escape(name)} \| (.*?) \|$", text, re.M)
    return m.group(1) if m else None


def parse(kind, text):
    """The parts of a log: {head, lead, sections: [(key, part)], gates: {key: row}, subjects, rest, foreign,
    blocks: {pid: block}, extras, raw}. `extras` is the text between the sections and the raw reply."""
    head, sep, rest = text.partition("\n## Lines\n")
    if not sep:
        raise ValueError("the log has no Lines section")
    at = rest.find("\n" + RAW_HEADINGS[kind] + "\n")
    if at < 0:
        raise ValueError(f"the log has no {RAW_HEADINGS[kind]!r} section")
    pre, raw = rest[:at], rest[at:]
    ends = [i for i in (pre.find("\n" + h) for h in (GATES_HEADING, LINE_SUBJECTS + "\n", PASS_HEADING + "\n")) if i >= 0]
    end = min(ends) if ends else len(pre)
    body, extras = pre[:end], pre[end:]
    pieces = body.split("\n### ")
    sections = [(section_key(kind, p), p) for p in pieces[1:]]
    out = {"head": head, "lead": pieces[0], "sections": sections, "extras": extras, "raw": raw,
           "gates": {}, "subjects": None, "rest": None, "foreign": None, "blocks": {}}
    g = extras.find("\n" + GATES_HEADING)
    if g >= 0:
        for r in re.split(r"\n## ", extras[g + 1:], maxsplit=1)[0].splitlines():
            if r.startswith("| ") and not r.startswith("| line |") and not r.startswith("| --- |"):
                out["gates"][r[2:].split(" | ")[0]] = r
    for heading, field in ((LINE_SUBJECTS, "subjects"), (FOREIGN, "foreign")):
        _, s, tail = extras.partition("\n" + heading + "\n")
        if s:
            rows = re.findall(r"^\| (.+?) \| ([0-9a-f]{64}) \|$", re.split(r"\n## ", tail, maxsplit=1)[0], re.M)
            out[field] = dict(rows)
    if out["subjects"] is not None:
        out["rest"] = out["subjects"].pop("(rest of the document)", None)
    p = extras.find("\n" + PASS_HEADING + "\n")
    if p >= 0:
        for part in extras[p:].split("\n#### Pass ")[1:]:
            out["blocks"][part.partition("\n")[0].strip()] = "#### Pass " + part.rstrip("\n")
    return out


def _normal(part):
    """(section part with its ruling as "Ruling: open", the ruling line or None)."""
    m = RULING_RE.search(part)
    if not m:
        return part, None
    return part[:m.start()] + OPEN + part[m.end():], m.group(0)


def _tag(part):
    m = TAG_RE.search(part.split("\n## ", 1)[0])
    return m.group(1) if m else None


# ---------------------------------------------------------------- records

def _reply_sha(text):
    return hashlib.sha256(text.strip().encode()).hexdigest()


def _fenced_reply(text, start):
    at = text.find(start)
    if at < 0:
        return None
    body = text[at + len(start):]
    end = body.rfind("\n```")
    return body[:end] if end >= 0 else None


def identity(kind, form, family, scope, subjects, head_text, raw_text):
    """What a record's sha hashes: kind, form, family, scope, each scoped line's subject key (for a pass
    with no per-line subjects, as class M, the document subject it records), the prompt and response
    hashes and the policy versions of the pass."""
    policies = {n: v for n, v in _rows(head_text) if "policy" in n}
    if not subjects and row(head_text, "subject sha256"):
        subjects = {"(document)": row(head_text, "subject sha256")}
    if kind == "classm":
        prompts = sorted(re.findall(r"^### case (\S+) — prompt sha256 ([0-9a-f]{64});", head_text + raw_text, re.M))
        prompt = _sha(prompts) if prompts else None
        response = _reply_sha(raw_text)
    else:
        prompt = row(head_text, "prompt sha256")
        reply = _fenced_reply(raw_text, "```yaml\n")
        response = _reply_sha(reply) if reply is not None else _reply_sha(raw_text)
    return {"kind": kind, "form": form, "family": family, "scope": scope, "subjects": subjects,
            "prompt_sha256": prompt, "response_sha256": response, "policies": policies}


def write_record(ident, parts):
    """Store a record (identity, [(part name, text)]); returns its sha. A record already stored is never
    rewritten: storing the same sha with other parts is an error."""
    sha = _sha(ident)
    text = [f"# Review record {sha[:12]} — {ident['kind']} {families.stem(ident['form'], ident['family'])}", "",
            "One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines "
            "it still judges.", "", "```json", json.dumps(ident, sort_keys=True, ensure_ascii=False, indent=1), "```", ""]
    for name, body in parts:
        if PART.search(body):
            raise ValueError(f"record part {name} contains a part delimiter")
        text += [f"<!-- part {name} -->", body]
    text += ["<!-- end -->", ""]
    content = "\n".join(text)
    path = record_path(ident["kind"], sha)
    if os.path.exists(path):
        if _read(path) != content:
            raise ValueError(f"record {sha} is stored with other content; records are never rewritten")
        return sha
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return sha


def parse_record(content):
    """(identity, {part name: text}) of a stored record."""
    ident = json.loads(content.partition("```json\n")[2].partition("\n```\n")[0])
    body = content[content.index("<!-- part "):] if "<!-- part " in content else ""
    names = PART.findall(body)
    chunks = PART.split(body)
    parts = {}
    # PART.split gives ["", name1, text1, name2, text2, ...]; each text is "\n<part>\n", the last one
    # followed by the end marker.
    for i in range(1, len(chunks), 2):
        t = chunks[i + 1]
        if i + 2 >= len(chunks):
            t = t[:t.rindex("<!-- end -->")]
        parts[chunks[i]] = t[1:-1]
    assert list(parts) == names
    return ident, parts


def _reader(rev=None):
    """A function reading a repository-relative path: the working tree, or a commit."""
    if rev is None:
        return lambda rel: _read(os.path.join(ROOT, rel)) if os.path.exists(os.path.join(ROOT, rel)) else None
    def read(rel):
        r = subprocess.run(["git", "-C", ROOT, "show", f"{rev}:{rel}"], capture_output=True, text=True)
        return r.stdout if r.returncode == 0 else None
    return read


def load_record(kind, sha, read=None):
    path = record_path(kind, sha)
    if read is None:
        content = _read(path)
    else:
        content = read(os.path.relpath(os.path.realpath(path), os.path.realpath(ROOT)))
        if content is None:
            raise FileNotFoundError(path)
    return parse_record(content)


# ---------------------------------------------------------------- the view

# Header rows a line-scoped pass rewrites (transcribe.merge_log): the counts, and the pass summary.
MUTABLE_ROWS = ("printed lines compared", "agree / disagree / missing", "lines judged",
                "match / mismatch / unclear / missing", "line-scoped reviews")


def _head_rows(base_head, head):
    """{row: value} of `head` that differ from `base_head` or that it adds, all of them rows a later pass
    rewrites (MUTABLE_ROWS); None when the two differ in anything else (another review's header)."""
    strip = lambda t: re.sub(r"^\| line-scoped reviews \| .*? \|\n", "", t, flags=re.M)
    b, h = strip(base_head), strip(head)
    pat = r"^(\| (?:" + "|".join(re.escape(n) for n in MUTABLE_ROWS) + r") \| ).*?( \|)$"
    if re.sub(pat, r"\1\2", b, flags=re.M) != re.sub(pat, r"\1\2", h, flags=re.M):
        return None
    out = {n: v for (n, v), (_, w) in zip(_rows(h), _rows(b)) if v != w}
    m = re.search(r"^\| line-scoped reviews \| (.*?) \|$", head, re.M)
    if m:
        out["line-scoped reviews"] = m.group(1)
    return out


def _apply_head(base_head, rows):
    head = base_head
    for name, value in rows.items():
        if name == "line-scoped reviews":
            continue
        head = re.sub(rf"^\| {re.escape(name)} \| .*? \|$", lambda _: f"| {name} | {value} |", head, count=1, flags=re.M)
    if "line-scoped reviews" in rows:
        head = re.sub(r"^(\| date \| .*? \|)$", lambda m: m.group(1) + f"\n| line-scoped reviews | {rows['line-scoped reviews']} |",
                      head, count=1, flags=re.M)
    return head


def _extras(kind, index, records):
    """The text between the sections and the raw reply, as merge_log writes it."""
    import subjects as S
    if "extras" in index:
        return index["extras"]
    tail = []
    if kind == "transcription":
        rows = [records[l["record"]][1].get("gate " + l["key"]) for l in index["lines"]]
        rows = [r for r in rows if r is not None]
        if rows:
            tail += [GATES_HEADING, "",
                     "Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.", "",
                     "| line | gates listed | not read by the project's line |", "| --- | --- | --- |", *rows, ""]
    if index.get("subjects") is not None:
        tail += S.table(index["subjects"], index.get("__rest__"))
        if kind == "transcription":
            tail += S.foreign_table(index.get("foreign") or {})
    blocks = {}
    for l in index["lines"]:
        ident, parts = records[l["record"]]
        if ident["scope"] != "whole":
            blocks[parts["block"].partition("\n")[0][len("#### Pass "):].strip()] = parts["block"]
    if blocks:
        import transcribe as T
        tail += [PASS_HEADING, "", T.PASS_INTRO, ""]
        for pid in sorted(blocks, key=lambda p: re.search(r"^\| date \| (.*?) \|$", blocks[p], re.M).group(1) + p):
            tail += [blocks[pid], ""]
    return "\n" + "\n".join(tail).rstrip("\n") + "\n" if tail else ""


def view_of(index, read=None):
    """The log text an index and its records describe."""
    kind = index["kind"]
    records = {}
    for sha in [index["base"]] + [l["record"] for l in index["lines"]]:
        if sha not in records:
            records[sha] = load_record(kind, sha, read)
    base = records[index["base"]][1]
    head = _apply_head(base["head"], index.get("head_rows") or {})
    body = index.get("lead", "")
    for l in index["lines"]:
        part = records[l["record"]][1]["section " + l["key"]]
        if l.get("ruling") is not None:
            m = RULING_RE.search(part)
            part = part[:m.start()] + l["ruling"] + part[m.end():]
        body += "\n### " + part
    return head + "\n## Lines\n" + body + _extras(kind, index, records) + base["raw"]


def load_index(kind, form, family=families.DEFAULT, read=None):
    path = index_path(kind, form, family)
    if read is None:
        if not os.path.exists(path):
            return None
        return json.loads(_read(path))
    text = read(os.path.relpath(os.path.realpath(path), os.path.realpath(ROOT)))
    return json.loads(text) if text is not None else None


def view(kind, form, family=families.DEFAULT, read=None):
    index = load_index(kind, form, family, read)
    return view_of(index, read) if index is not None else None


def line_passes(kind, form, family=families.DEFAULT):
    """{line key: {record, pass, status}} of a form's index, `pass` being the id of the line-scoped pass
    whose record the line's verdict comes from (None for the whole-form review); None without an index."""
    index = load_index(kind, form, family)
    if index is None:
        return None
    pids = {}
    for sha in {l["record"] for l in index["lines"]}:
        ident, parts = load_record(kind, sha)
        pids[sha] = None if ident["scope"] == "whole" else parts["block"].partition("\n")[0][len("#### Pass "):].strip()
    return {l["key"]: {"record": l["record"], "pass": pids[l["record"]], "status": l["status"]} for l in index["lines"]}


NO_INDEX = object()


def state(kind, form, family, year):
    """subjects.index_state of a form's index (None when every compared line and the rest are current,
    else what is stale), or NO_INDEX when the form has none."""
    import subjects
    index = load_index(kind, form, family)
    if index is None:
        return NO_INDEX
    _, base = load_record(kind, index["base"])
    m = re.search(r"^\| subject sha256 \| ([0-9a-f]{64}) \|$", base["head"], re.M)
    passes = line_passes(kind, form, family)
    return subjects.index_state(kind, form, year, index, m.group(1) if m else None,
                                any(v["pass"] for v in passes.values()))


# ---------------------------------------------------------------- ingest

def ingest(kind, form, family, text):
    """Store a log a review tool wrote: new records for the passes the index does not yet hold, and the
    index; the view must reproduce `text` exactly. Records the index no longer names are removed."""
    old = load_index(kind, form, family)
    p = parse(kind, text)
    by_pid, base = {}, None
    old_records = set()
    if old is not None:
        old_records = {old["base"]} | {l["record"] for l in old["lines"]}
        for sha in old_records:
            ident, parts = load_record(kind, sha)
            if ident["scope"] == "whole":
                if sha == old["base"] and _head_rows(parts["head"], p["head"]) is not None and parts["raw"] == p["raw"]:
                    base = (sha, parts)
            else:
                by_pid[parts["block"].partition("\n")[0][len("#### Pass "):].strip()] = (sha, parts)
    subjects_now = p["subjects"] or {}
    owner = {}
    for key, part in p["sections"]:
        owner[key] = _tag(part) if kind != "classm" else None
    if base is not None and any(base[1].get("section " + k) != _normal(s)[0] for k, s in p["sections"] if owner[k] is None):
        base = None  # a whole-form review with the same header and reply, but other verdicts: a new record
    if base is None:
        untagged = [(k, s) for k, s in p["sections"] if owner[k] is None]
        scope = "whole"
        # A class M review records its prompts on its case headings, so they are read with the header.
        head_text = p["head"] + ("".join("\n### " + s for _, s in untagged) if kind == "classm" else "")
        ident = identity(kind, form, family, scope, {k: subjects_now.get(k) for k, _ in untagged if k in subjects_now},
                         head_text, p["raw"])
        parts = [("head", re.sub(r"^\| line-scoped reviews \| .*? \|\n", "", p["head"], flags=re.M))]
        parts += [("section " + k, _normal(s)[0]) for k, s in untagged]
        parts += [("gate " + k, p["gates"][k]) for k, _ in untagged if k in p["gates"]]
        parts += [("raw", p["raw"])]
        sha = write_record(ident, parts)
        base = (sha, dict(parts))
    shas = {None: base[0]}
    for pid, block in p["blocks"].items():
        mine = [(k, s) for k, s in p["sections"] if owner[k] == pid]
        if pid in by_pid and all(by_pid[pid][1].get("section " + k) == _normal(s)[0] for k, s in mine):
            shas[pid] = by_pid[pid][0]
            continue
        scope = row(block, "review scope")
        import subjects
        scope = subjects.scope_keys(scope) or [k for k, _ in mine]
        reply = _fenced_reply(block, "```yaml\n") or ""
        ident = identity(kind, form, family, scope, {k: subjects_now.get(k) for k, _ in mine if k in subjects_now}, block, reply)
        parts = [("block", block)] + [("section " + k, _normal(s)[0]) for k, s in mine]
        parts += [("gate " + k, p["gates"][k]) for k, _ in mine if k in p["gates"]]
        shas[pid] = write_record(ident, parts)
    for k, s in p["sections"]:
        if owner[k] is not None and owner[k] not in shas:
            raise ValueError(f"{families.stem(form, family)}: section {k} names pass {owner[k]}, which the log does not hold")
    lines = []
    for k, s in p["sections"]:
        status = re.search(r"^Status: \*\*(\w+)\*\*", s, re.M)
        ruling = _normal(s)[1]
        ls = (p["subjects"] or {}).get(k)
        fo = (p["foreign"] or {}).get(k)
        lines.append({"key": k, "record": shas[owner[k]], "status": status.group(1) if status else None,
                      **({"ruling": ruling} if ruling is not None else {}),
                      **({"subject_key": subject_key(ls, fo)} if ls is not None else {})})
    index = {"kind": kind, "form": form, "family": family, "base": base[0]}
    rows = _head_rows(base[1]["head"], p["head"])
    if rows:
        index["head_rows"] = rows
    if p["lead"]:
        index["lead"] = p["lead"]
    index["lines"] = lines
    if p["subjects"] is not None:
        index["subjects"] = p["subjects"]
        index["__rest__"] = p["rest"]
    if p["foreign"] is not None:
        index["foreign"] = p["foreign"]
    if view_of(index) != text:
        index["extras"] = p["extras"]  # a log whose frame the current tools would not write so
        if view_of(index) != text:
            raise ValueError(f"{kind}/{families.stem(form, family)}: the stored review does not reproduce the log")
    path = index_path(kind, form, family)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=1, ensure_ascii=False)
        f.write("\n")
    keep = {index["base"]} | {l["record"] for l in index["lines"]}
    for sha in old_records - keep:
        if os.path.exists(record_path(kind, sha)):
            os.remove(record_path(kind, sha))
    return index


# ---------------------------------------------------------------- commands

def forms(kind):
    import rulings
    return [(f, fam) for f, fam in rulings.forms_with_logs(kind) if os.path.exists(index_path(kind, f, fam))]


def render(kinds=KINDS, only=None):
    """Write the readable view of every stored review (or of form `only`); returns the paths written."""
    out = []
    for kind in kinds:
        for form, family in forms(kind):
            if only and form != only:
                continue
            path = view_path(kind, form, family)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(view(kind, form, family))
            out.append(path)
    return out


def migrate():
    """Store every committed log file (reviews/<year>/<kind>/<stem>.md) as records and an index, verify its
    view reproduces it byte for byte, write the view and remove the file."""
    import rulings
    n = 0
    for kind in KINDS:
        d = os.path.join(_reviews(), kind)
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            if not name.endswith(".md"):
                continue
            form, family = families.split_stem(name[:-3])
            path = os.path.join(d, name)
            text = _read(path)
            ingest(kind, form, family, text)
            if view(kind, form, family) != text:
                raise SystemExit(f"{kind}/{name}: the stored review does not reproduce the log")
            os.remove(path)
            target = view_path(kind, form, family)
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with open(target, "w", encoding="utf-8") as f:
                f.write(text)
            n += 1
    print(f"review store: {n} logs stored as records and indexes under {os.path.relpath(_reviews(), ROOT)}")


# Indexes held out of the line/subject agreement below: {"<kind>/<stem>": reason}. Shrink-only: an entry is
# removed when its form is reviewed, and an entry that no longer has a gap fails until it is removed.
SUBJECT_VERDICT_EXCEPTIONS = {
    "transcription/div.deepseek": "optional-family log whose verdict section div.screen has no line subject; "
                                  "stale for the lines now compared, rerun only where it can earn credit (BUG-0468)",
}


def subject_verdict_gap(index):
    """What differs between an index's compared lines (those with a verdict section) and its line subjects:
    ([keys with a subject and no verdict], [keys with a verdict and no subject]); both empty when the index
    records no per-line subjects (a whole-form review of an older form)."""
    subj = index.get("subjects")
    if subj is None:
        return [], []
    lines = [l["key"] for l in index["lines"]]
    return sorted(set(subj) - set(lines)), sorted(set(lines) - set(subj))


def check():
    """Every index's records exist, parse, name their kind, form and family, and hash to their names, the
    index's view parses back to the same index, and every key with a line subject has a verdict section
    and the reverse (SUBJECT_VERDICT_EXCEPTIONS aside)."""
    problems, n, used = [], 0, set()
    for kind in KINDS:
        for form, family in forms(kind):
            n += 1
            index = load_index(kind, form, family)
            tag = f"{kind}/{families.stem(form, family)}"
            no_verdict, no_subject = subject_verdict_gap(index)
            if (no_verdict or no_subject) and tag not in SUBJECT_VERDICT_EXCEPTIONS:
                problems.append(f"{tag}: " + "; ".join(
                    ([f"line subject without a verdict section: {', '.join(no_verdict)}"] if no_verdict else []) +
                    ([f"verdict section without a line subject: {', '.join(no_subject)}"] if no_subject else [])))
            elif tag in SUBJECT_VERDICT_EXCEPTIONS and not (no_verdict or no_subject):
                problems.append(f"{tag}: listed in SUBJECT_VERDICT_EXCEPTIONS but has no gap; remove it")
            for sha in {index["base"]} | {l["record"] for l in index["lines"]}:
                used.add((kind, sha))
                try:
                    ident, _ = load_record(kind, sha)
                except (OSError, ValueError) as ex:
                    problems.append(f"{kind}/{families.stem(form, family)}: record {sha[:12]}: {ex}"); continue
                if _sha(ident) != sha or (ident["kind"], ident["form"], ident["family"]) != (kind, form, family):
                    problems.append(f"{kind}/{families.stem(form, family)}: record {sha[:12]} is not the pass its name hashes")
            try:
                text = view_of(index)
                again = parse(kind, text)
                keys = [k for k, _ in again["sections"]]
                if keys != [l["key"] for l in index["lines"]]:
                    problems.append(f"{kind}/{families.stem(form, family)}: the view's sections are not the index's lines")
            except (OSError, ValueError, KeyError) as ex:
                problems.append(f"{kind}/{families.stem(form, family)}: the view cannot be assembled: {ex}")
    for p in problems:
        print(p, file=sys.stderr)
    print(f"review store: {n} indexes, {len(used)} records" + (f"; {len(problems)} problem(s)" if problems else "; every record present and named by its hash"))
    return 1 if problems else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("render", help="write the readable views")
    r.add_argument("--kind", choices=KINDS)
    r.add_argument("--form")
    sub.add_parser("migrate", help="store every committed log file and remove it")
    sub.add_parser("check", help="every index's records are present and its view assembles")
    a = ap.parse_args(argv)
    if a.cmd == "render":
        paths = render((a.kind,) if a.kind else KINDS, a.form)
        print(f"review store: {len(paths)} views written under {os.path.relpath(os.path.dirname(os.path.dirname(paths[0])), ROOT) if paths else '-'}")
        return 0
    if a.cmd == "migrate":
        migrate()
        return 0
    return check()


if __name__ == "__main__":
    sys.exit(main())
