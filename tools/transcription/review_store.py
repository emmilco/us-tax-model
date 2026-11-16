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

A record over SHARED_MIN_BYTES stores each JSON subtree its sections repeat once, in a `shared` part, and a
reference ({"$shared": "<id>"}) in its place; parse_record expands the references, so every reader sees each
section exactly as the review tool wrote it, and rulings and carry keys, computed on that text, are unchanged.
A record without a `shared` part is read as it is.

The index maps each compared line, in section order, to {key, record, status, ruling, subject_key}, with
the line subjects (`subjects`, the per-line hashes of subjects.py), the rest of the document (`__rest__`),
the foreign interfaces of transcription lines (`foreign`), the whole-form record the view's header comes
from (`base`) and the header rows a later pass rewrote (`head_rows`). A line's `subject_key` folds its line
subject and its foreign interfaces together.

A verdict carried across a proven rename of line ids (rename_carry.py) is marked on its line with `carried`
({"by": "rename", "map", "from", ...}). When the rename changed the line's log key, the line also names the
record section it was judged under (`section`, the old key); the view shows that section under the new key.
A whole-form subject carried the same way is `subject_carried` ({"subject", "was", "carried"}): state() reads
`subject` in place of the base record's header subject only while `was` is that header's; year_carry.py writes one
(`carried` {"by": "year"}) for a render index with no line subjects whose rendering moved only the year. ingest() keeps a
line's `carried` and `section` while the line's verdict still comes from the same record.

The per-form log is a view, generated, not committed: view() assembles it from the index and the records it
names, byte for byte as the review tools wrote it; ingest() takes a log a tool wrote (or rule.py ruled) and
stores what is new in it, verifying that the view reproduces it. `render` writes the views to the
git-ignored .transcription/logs/<year>/<kind>/<stem>.md.

    review_store.py render [--kind K] [--form F]   write views (every form of every kind by default)
    review_store.py migrate                         store every committed log (*.md) and remove it
    review_store.py check                           every index's records exist and its view parses back
    review_store.py share [--write]                 store the repeated subtrees of large unshared records once
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


# ---------------------------------------------------------------- shared subtrees

# A transcription section shows each side of a disagreement as one line of canonical JSON (transcribe.canonical:
# sorted keys, the default separators). Helpers are expanded in place, so a form that reuses guard helpers repeats
# the same subtrees many times over. A record whose parts exceed SHARED_MIN_BYTES characters stores each subtree of
# at least SHARED_MIN_CHARS characters that its sections hold more than once a single time: in the part SHARED_PART,
# one line "<id> <text>" per subtree, children before parents, with {"$shared": "<id>"} in its place in the sections
# and in the shared texts. The id is the start of the sha256 of the subtree's shared text, which names its own shared
# children by their ids. Expanding the references gives back each section byte for byte; _share verifies that, and
# stores the parts as they are when it does not hold.
SHARED_PART = "shared"
SHARED_MIN_BYTES = 1 << 20
SHARED_MIN_CHARS = 80
SHARED_MARK = '"$shared"'
SHARED_REF = re.compile(r'\{"\$shared": "([0-9a-f]{16})"\}')
JSON_LINE = re.compile(r"^```json\n(.*)\n```$", re.M)


def _dump(value):
    return json.dumps(value, ensure_ascii=False)


class _Forest:
    """JSON trees with equal subtrees under one id (hash-consing). nodes[i] is ("=", scalar text), ("[", child ids)
    or ("{", sorted keys, child ids); size[i] is the length of its canonical text and count[i] the number of times
    it occurs in the trees added. A node's id is assigned after its children's, so children precede parents."""

    def __init__(self):
        self.ids, self.nodes, self.size, self.count = {}, [], [], []

    def add(self, tree):
        """The id of `tree`, counting one occurrence of it and of each of its subtrees (iteratively: the trees are
        deep)."""
        work, done = [(tree, False)], []
        while work:
            node, ready = work.pop()
            if isinstance(node, (dict, list)) and not ready:
                work.append((node, True))
                kids = [node[k] for k in sorted(node)] if isinstance(node, dict) else node
                work.extend((k, False) for k in reversed(kids))
                continue
            if isinstance(node, (dict, list)):
                keys = tuple(sorted(node)) if isinstance(node, dict) else None
                kids = tuple(done[len(done) - len(node):])
                del done[len(done) - len(node):]
                sep = 2 * max(len(kids) - 1, 0)
                if keys is None:
                    sig, n = ("[", kids), 2 + sep + sum(self.size[c] for c in kids)
                else:
                    sig = ("{", keys, kids)
                    n = 2 + sep + sum(len(_dump(k)) + 2 + self.size[c] for k, c in zip(keys, kids))
            else:
                sig = ("=", _dump(node))
                n = len(sig[1])
            i = self.ids.get(sig)
            if i is None:
                i = self.ids[sig] = len(self.nodes)
                self.nodes.append(sig)
                self.size.append(n)
                self.count.append(0)
            self.count[i] += 1
            done.append(i)
        return done[0]


def _share(parts):
    """`parts` ([(name, text)]) with the subtrees their sections' JSON lines repeat stored once (the note above), or
    `parts` itself when the record is small, repeats nothing, or the shared form would not expand back to it."""
    if sum(len(t) for _, t in parts) <= SHARED_MIN_BYTES:
        return parts
    if any(n.startswith("section ") and SHARED_MARK in t for n, t in parts):
        return parts  # a reference could not be told from the text
    forest, roots = _Forest(), {}
    for at, (name, text) in enumerate(parts):
        if not name.startswith("section "):
            continue
        for m in JSON_LINE.finditer(text):
            try:
                tree = json.loads(m.group(1))
            except ValueError:
                continue  # not JSON (a missing or unparseable side): kept as written
            if json.dumps(tree, sort_keys=True, ensure_ascii=False) != m.group(1):
                continue  # not in the canonical form the shared texts are written in: kept as written
            roots[(at, m.start(1), m.end(1))] = forest.add(tree)
            del tree
    shared = {i for i, (n, c) in enumerate(zip(forest.size, forest.count)) if c > 1 and n >= SHARED_MIN_CHARS}
    if not shared:
        return parts
    text, lines, ids = [None] * len(forest.nodes), [], set()
    for i, sig in enumerate(forest.nodes):
        if sig[0] == "=":
            body = sig[1]
        elif sig[0] == "[":
            body = "[" + ", ".join(text[c] for c in sig[1]) + "]"
        else:
            body = "{" + ", ".join(_dump(k) + ": " + text[c] for k, c in zip(sig[1], sig[2])) + "}"
        if sig[0] != "=":
            for c in sig[-1]:
                if forest.count[c] == 1:
                    text[c] = None  # its only occurrence is in this node's text now
        if i in shared:
            sid = hashlib.sha256(body.encode()).hexdigest()[:16]
            if sid in ids:
                return parts
            ids.add(sid)
            lines.append(sid + " " + body)
            body = '{"$shared": "' + sid + '"}'
        text[i] = body
    out = []
    for at, (name, t) in enumerate(parts):
        spans = sorted((s, e, r) for (a, s, e), r in roots.items() if a == at)
        if spans:
            pieces, last = [], 0
            for s, e, r in spans:
                pieces += [t[last:s], text[r]]
                last = e
            t = "".join(pieces) + t[last:]
        out.append((name, t))
    out.append((SHARED_PART, "\n".join(lines)))
    if list(_unshare(dict(out)).items()) != list(parts):
        print("review_store: the shared form of a record does not expand back to it; stored unshared", file=sys.stderr)
        return parts
    return out


def _unshare(parts):
    """`parts` ({name: text}) with the shared part removed and its references in the sections expanded. A shared
    text may name only the subtrees listed before it, so expansion ends."""
    table = {}
    for line in parts.pop(SHARED_PART).split("\n"):
        sid, _, body = line.partition(" ")
        pieces = SHARED_REF.split(body)
        if not re.fullmatch(r"[0-9a-f]{16}", sid) or sid in table or any(p not in table for p in pieces[1::2]):
            raise ValueError(f"shared subtree {sid!r} is malformed, repeated or names one not listed before it")
        table[sid] = pieces

    def expand(t):
        pieces = SHARED_REF.split(t)
        if any(p not in table for p in pieces[1::2]):
            raise ValueError("a section names a shared subtree the record does not hold")
        out, work, at = [], [], 0
        while True:
            if at < len(pieces):
                if at % 2:
                    work.append((pieces, at + 1))
                    pieces, at = table[pieces[at]], 0
                else:
                    out.append(pieces[at])
                    at += 1
            elif work:
                pieces, at = work.pop()
            else:
                return "".join(out)

    return {n: expand(t) if n.startswith("section ") else t for n, t in parts.items()}


def _compose(sha, ident, parts):
    """The text of a record file: its title, identity and parts ([(name, text)])."""
    text = [f"# Review record {sha[:12]} — {ident['kind']} {families.stem(ident['form'], ident['family'])}", "",
            "One pass of a review, stored once (tools/transcription/review_store.py); the form's index says which lines "
            "it still judges.", "", "```json", json.dumps(ident, sort_keys=True, ensure_ascii=False, indent=1), "```", ""]
    for name, body in parts:
        text += [f"<!-- part {name} -->", body]
    text += ["<!-- end -->", ""]
    return "\n".join(text)


def write_record(ident, parts):
    """Store a record (identity, [(part name, text)]); returns its sha. A large record stores its repeated
    subtrees once (_share). A record already stored is never rewritten: storing the same sha with other parts is
    an error, and a record stored unshared is kept as it is."""
    names = [name for name, _ in parts]
    if len(set(names)) != len(names):
        raise ValueError(f"record parts share a name: {sorted({n for n in names if names.count(n) > 1})}")
    if SHARED_PART in names:
        raise ValueError(f"record part name {SHARED_PART!r} is reserved for shared subtrees")
    for name, body in parts:
        if PART.search(body):
            raise ValueError(f"record part {name} contains a part delimiter")
    sha = _sha(ident)
    content = _compose(sha, ident, _share(parts))
    path = record_path(ident["kind"], sha)
    if os.path.exists(path):
        stored = _read(path)
        if stored != content:
            was, got = parse_record(stored)
            if _compose(sha, was, got.items()) != _compose(sha, ident, parts):
                raise ValueError(f"record {sha} is stored with other content; records are never rewritten")
        return sha
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return sha


def parse_record(content):
    """(identity, {part name: text}) of a stored record, its shared subtrees expanded."""
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
    if SHARED_PART in parts:
        parts = _unshare(parts)
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


def aliased(text, old, new):
    """A record's section (or gate row) judged under log key `old`, shown under key `new`: the key that opens
    the section's title (or the row's first cell) is replaced; nothing else changes."""
    if text is None or old is None or old == new:
        return text
    if text.startswith("| " + old + " | "):
        return "| " + new + " | " + text[len("| " + old + " | "):]
    if text.startswith(old):
        return new + text[len(old):]
    raise ValueError(f"record section {old!r} does not open with its key")


def section_of(parts, line):
    """The text of an index line's section from its record's parts, under the line's key."""
    return aliased(parts["section " + line.get("section", line["key"])], line.get("section"), line["key"])


def _gate_of(parts, line):
    return aliased(parts.get("gate " + line.get("section", line["key"])), line.get("section"), line["key"])


def _extras(kind, index, records):
    """The text between the sections and the raw reply, as merge_log writes it."""
    import subjects as S
    if "extras" in index:
        return index["extras"]
    tail = []
    if kind == "transcription":
        rows = [_gate_of(records[l["record"]][1], l) for l in index["lines"]]
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
        part = section_of(records[l["record"]][1], l)
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
    passes = line_passes(kind, form, family)
    return subjects.index_state(kind, form, year, index, recorded_subject(kind, index),
                                any(v["pass"] for v in passes.values()))


def recorded_subject(kind, index):
    """The whole-form subject an index answers: its base record's header subject, or the subject carried
    across a proven rename or a tax-year change (`subject_carried`, by "rename" or "year": year_carry.py)
    while that carry names the header's subject as the one it was proven from."""
    _, base = load_record(kind, index["base"])
    m = re.search(r"^\| subject sha256 \| ([0-9a-f]{64}) \|$", base["head"], re.M)
    header = m.group(1) if m else None
    carried = index.get("subject_carried")
    if header and carried and carried.get("was") == header and carried.get("subject"):
        return carried["subject"]
    return header


# ---------------------------------------------------------------- ingest

def ingest(kind, form, family, text):
    """Store a log a review tool wrote: new records for the passes the index does not yet hold, and the
    index; the view must reproduce `text` exactly. Records the index no longer names are removed."""
    old = load_index(kind, form, family)
    p = parse(kind, text)
    by_pid, base = {}, None
    old_records = set()
    old_lines = {l["key"]: l for l in (old or {}).get("lines", [])}

    def recorded_section(parts, k):
        """A record's section for log key k, shown under k as the old index showed it."""
        line = old_lines.get(k)
        name = line.get("section", k) if line else k
        got = parts.get("section " + name)
        return aliased(got, line.get("section"), k) if line and got is not None else got

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
    if base is not None and any(recorded_section(base[1], k) != _normal(s)[0] for k, s in p["sections"] if owner[k] is None):
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
        if pid in by_pid and all(recorded_section(by_pid[pid][1], k) == _normal(s)[0] for k, s in mine):
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
        line = {"key": k, "record": shas[owner[k]], "status": status.group(1) if status else None,
                **({"ruling": ruling} if ruling is not None else {}),
                **({"subject_key": subject_key(ls, fo)} if ls is not None else {})}
        was = old_lines.get(k)
        if was is not None and was["record"] == line["record"]:
            # the same verdict from the same record: a carry across a rename still describes it
            if was.get("section"):
                line["section"] = was["section"]
            if was.get("carried") and was.get("subject_key") == line.get("subject_key"):
                line["carried"] = was["carried"]
        lines.append(line)
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
            for l in index["lines"]:
                if l.get("section") and ((l.get("carried") or {}).get("by") != "rename"
                                         or (l["carried"].get("keys") or {}).get(l["section"]) != l["key"]):
                    problems.append(f"{tag}: line {l['key']} is shown from record section {l['section']} without a "
                                    "rename carry that maps that key to it")
            sc = index.get("subject_carried")
            if sc is not None and (sc.get("carried") or {}).get("by") not in ("rename", "year"):
                problems.append(f"{tag}: subject_carried without a rename or year carry")
            for sha in {index["base"]} | {l["record"] for l in index["lines"]}:
                used.add((kind, sha))
                try:
                    ident, _ = load_record(kind, sha)
                except (OSError, ValueError) as ex:
                    problems.append(f"{kind}/{families.stem(form, family)}: record {sha[:12]}: {ex}"); continue
                if _sha(ident) != sha or (ident["kind"], ident["form"], ident["family"]) not in \
                        {(kind, name, family) for name in (form, former_document(form))}:
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


def share(write=False):
    """Every stored record over SHARED_MIN_BYTES that is stored unshared, in its shared form (_share): the same
    identity and parts, verified to read back the same before it is written. Reports the sizes; writes only with
    `write`. Returns the number of records that would shrink or did."""
    n = 0
    for kind in KINDS:
        d = store_dir(kind)
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            path = os.path.join(d, name)
            if not name.endswith(".md") or os.path.getsize(path) <= SHARED_MIN_BYTES:
                continue
            old = _read(path)
            ident, parts = parse_record(old)
            sha = _sha(ident)
            if sha != name[:-3]:
                print(f"{kind}/{name[:12]}: not the pass its name hashes; left as it is", file=sys.stderr)
                continue
            new = _compose(sha, ident, _share(list(parts.items())))
            if len(new) >= len(old):
                continue
            if parse_record(new) != (ident, parts):
                raise SystemExit(f"{kind}/{name[:12]}: the shared form does not read back as the record")
            n += 1
            print(f"{kind}/{name[:12]}: {len(old.encode()):,} -> {len(new.encode()):,} bytes")
            if write:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new)
    print(f"review store: {n} record(s) {'stored shared' if write else 'would shrink (--write stores them)'}")
    return n


def former_document(form):
    """The name a document had before the rename recorded in tools/year_free_names.json (None if it was not renamed):
    a record is immutable, so it keeps the name of the document it reviewed, and its index, moved to the new name by
    rename_carry.py, still holds it."""
    path = os.path.join(ROOT, "tools", "year_free_names.json")
    renames = json.load(open(path, encoding="utf-8")).get("renames", {}) if os.path.exists(path) else {}
    return next((old for old, r in renames.items() if r.get("kind") == "document" and r["to"] == form), None)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("render", help="write the readable views")
    r.add_argument("--kind", choices=KINDS)
    r.add_argument("--form")
    sub.add_parser("migrate", help="store every committed log file and remove it")
    sub.add_parser("check", help="every index's records are present and its view assembles")
    s = sub.add_parser("share", help="store the repeated subtrees of large unshared records once")
    s.add_argument("--write", action="store_true", help="rewrite them (default: report only)")
    a = ap.parse_args(argv)
    if a.cmd == "share":
        share(a.write)
        return 0
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
