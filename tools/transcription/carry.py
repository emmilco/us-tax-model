#!/usr/bin/env python3
"""Carry an earlier ruling over to a repeat review disagreement.

A rerun (a prompt change, a new model reply) reopens every disagreement whose
recorded review context changed, even where the same objection recurs on the
same unchanged line. This step rules such a repeat automatically, so an
adjudicator sees only new disagreements. A ruling carries only when all hold:

- the same kind, form and model family (the same log stem), and the same
  printed line or id, with the same status;
- the same disagreement content: for transcription both expression trees
  (canonical JSON); for render the restated English; for class M the case id
  (part of the handle) and both values (a case's branch list is not compared:
  it changes with instrumentation, and what the line computes is checked below);
- the same project line: the line's own definition (citations left out) and
  everything it reads, followed through other lines, documents, tables and the
  year parameters, is unchanged between the source log's commit and the
  working tree; for render also the line's rendered section;
- the earlier ruling is of a settled class: not a finding or defect (those are
  re-judged), not an interface gap or unclassified prose (still pending in
  compare_families.py), and not open.

A class M ruling that dropped the line from the fixture is carried with its
drop, which rule.py repeats on the fixture.

A render objection is free text, so render matches on the restated English and
the status (MISMATCH, UNCLEAR, MISSING), not on the objection's wording.

The source is the log the ruling was written in: by default the committed
version of the same log (`git show HEAD:...`), else a log, its rulings sidecar,
an archive directory (`<stem>.md`, `render.<stem>.md`, `classm.<stem>.md`) or
`git:<rev>`. The reviewed forms are read from the commit that introduced the
source log (a pre-commit check holds every committed log's subject current);
a source log found in no commit is matched by its recorded subject hash, and
a source whose forms cannot be found carries nothing.

The carried ruling keeps its text, so its class prefix is read as before, and
names its source:
    Ruling: <earlier text> (carried over from <source>, review of <date>)
It is written through rule.py, into the log and the sidecar with the current
review context; check_logs.py counts it as ruled like any other.

    carry.py --kind transcription --form s3 [--family deepseek] [--from DIR|FILE|git:REV] [--dry-run]
    carry.py --kind render --form all --from .transcription/archive/<dir> --dry-run
"""
import argparse, collections, hashlib, json, os, re, subprocess, sys

import yaml

_Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import families  # noqa: E402
import rulings as sidecar  # noqa: E402
import rule  # noqa: E402
import subjects  # noqa: E402
import compare_families  # noqa: E402

ROOT = sidecar.ROOT
Y = sidecar.Y
CARRIED = re.compile(r" \(carried over from [^()]*\)$")
ARCHIVE_PREFIX = {"transcription": "", "render": "render.", "classm": "classm."}
STATUS = re.compile(r"^Status: \*\*(\w+)\*\*", re.M)


# ---------------------------------------------------------------- snapshots

def _git(*args):
    r = subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


class Snapshot:
    """The repository's forms, rendered English, tables and parameters at a commit, or in the
    working tree when `rev` is None."""

    def __init__(self, rev=None):
        self.rev, self._cache = rev, {}

    def read(self, rel):
        if rel not in self._cache:
            if self.rev is None:
                p = os.path.join(ROOT, rel)
                self._cache[rel] = open(p, encoding="utf-8").read() if os.path.exists(p) else None
            else:
                self._cache[rel] = _git("show", f"{self.rev}:{rel}")
        return self._cache[rel]

    def forms(self):
        if "__forms" not in self._cache:
            if self.rev is None:
                names = os.listdir(os.path.join(ROOT, "forms", Y))
            else:
                names = [os.path.basename(n) for n in (_git("ls-tree", "--name-only", self.rev, f"forms/{Y}/") or "").split()]
            self._cache["__forms"] = sorted(n[:-5] for n in names if n.endswith(".yaml"))
        return self._cache["__forms"]

    def tables(self):
        if "__tables" not in self._cache:
            if self.rev is None:
                d = os.path.join(ROOT, "tables", Y)
                names = os.listdir(d) if os.path.isdir(d) else []
            else:
                names = [os.path.basename(n) for n in (_git("ls-tree", "--name-only", self.rev, f"tables/{Y}/") or "").split()]
            self._cache["__tables"] = {n.split(".")[0]: n for n in sorted(names)}
        return self._cache["__tables"]

    def doc(self, fid):
        key = "__doc " + fid
        if key not in self._cache:
            text = self.read(f"forms/{Y}/{fid}.yaml")
            raw = yaml.load(text, Loader=_Loader) if text else None
            self._cache[key] = (raw.get("form") or raw.get("def")) if raw else None
            self._cache["__subject " + fid] = subjects._sha(subjects._without_cites(raw)) if raw else None
        return self._cache[key]

    def subject(self, fid):
        """subjects.of_form of a document, from the parse already made."""
        self.doc(fid)
        return self._cache["__subject " + fid]

    def line_index(self):
        """{line id: (form id, line dict)} over every document."""
        if "__lines" not in self._cache:
            idx = {}
            for fid in self.forms():
                for l in (self.doc(fid) or {}).get("lines", []):
                    idx.setdefault(l["id"], (fid, l))
            self._cache["__lines"] = idx
        return self._cache["__lines"]


def _strings(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k != "cite":
                yield from _strings(v)
    elif isinstance(o, list):
        for x in o:
            yield from _strings(x)
    elif isinstance(o, str):
        yield o


def _sha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


DEPTH = None  # how many references deep closure() follows; None follows every one


def closure(snap, fid, line, depth=None):
    """What a line reads, as {node: hash}: the line itself and, transitively, every line it
    names, every document it names without naming a line of it (whole, citations left out),
    every table it names, and the year parameters. Any string in a line that is a line id,
    a document id or a document-prefixed name counts as a reference; over-collecting only
    makes a carry less likely."""
    idx, forms, tables = snap.line_index(), set(snap.forms()), snap.tables()
    if "__params" not in snap._cache:
        snap._cache["__params"] = hashlib.sha256((snap.read(f"params/{Y}.yaml") or "").encode()).hexdigest()
    out = {"params": snap._cache["__params"]}
    todo, seen = [(fid, line, 0)], set()
    while todo:
        f, l, n = todo.pop(0)
        if l["id"] in seen:
            continue
        seen.add(l["id"])
        out["line " + l["id"]] = _sha(subjects._without_cites(l))
        if depth is not None and n >= depth:
            continue
        for s in _strings({k: v for k, v in l.items() if k != "id"}):
            base = re.split(r"[\[\]]", s)[0]
            if base in idx:
                todo.append((*idx[base], n + 1))
                continue
            head = re.split(r"[.\[]", s)[0]
            if s in tables:
                out["table " + s] = hashlib.sha256((snap.read(f"tables/{Y}/{tables[s]}") or "").encode()).hexdigest()
            elif head in forms and head != f or s in forms:
                d = head if head in forms else s
                if "doc " + d not in out:
                    out["doc " + d] = snap.subject(d)
                    if depth is None:
                        todo += [(d, dl, n + 1) for dl in (snap.doc(d) or {}).get("lines", [])]
    return out


def find_line(snap, fid, handle):
    """The line of a document a log section names (printed number, id, or 'printed (id)'), or None
    when it cannot be named uniquely."""
    doc = snap.doc(fid)
    if not doc:
        return None
    lines = doc.get("lines", [])
    if "]." in handle:  # a class M line of a collection entry: person[taxpayer].sc[biz_b].scveh[car_1].line9w
        handle = handle.rsplit("].", 1)[1]
    for test in (lambda l: l["id"] == handle, lambda l: l["id"] == f"{fid}.{handle}",
                 lambda l: str(l.get("printed")) == handle):
        hit = [l for l in lines if test(l)]
        if len(hit) == 1:
            return hit[0]
        if len(hit) > 1:
            break
    m = re.match(r"^(.*) \(([^()]+)\)$", handle)
    if m:
        hit = [l for l in lines if str(l.get("printed")) == m.group(1) and l["id"] in (m.group(2), f"{fid}.{m.group(2)}")]
        if len(hit) == 1:
            return hit[0]
    return None


def rendered_section(snap, fid, line_id):
    text = snap.read(f"rendered/{Y}/{fid}.md")
    if not text:
        return None
    for sec in re.split(r"(?m)^## ", text)[1:]:
        head, _, _ = sec.partition("\n")
        if head.rstrip().endswith(f"`{line_id}`"):
            return hashlib.sha256(subjects.CITE_TEXT.sub("[cite]", sec).encode()).hexdigest()
    return None


def line_subject(kind, snap, fid, handle):
    """Everything the line's ruling may rest on, as a hash, or None when the line cannot be found."""
    key = ("__subject", kind, fid, handle, DEPTH)
    if key not in snap._cache:
        snap._cache[key] = _line_subject(kind, snap, fid, handle)
    return snap._cache[key]


def _line_subject(kind, snap, fid, handle):
    line = find_line(snap, fid, handle)
    if line is None:
        return None
    nodes = closure(snap, fid, line, DEPTH)
    if kind == "render":
        nodes["rendered"] = rendered_section(snap, fid, line["id"])
        if nodes["rendered"] is None:
            return None
    return _sha(nodes)


# ---------------------------------------------------------------- log sections

def sections(kind, text):
    """[{handle, key, status, ruling, case}] for every disagreement section of a log, with the
    class M case heading's branch list as `case`."""
    _, _, rest = text.partition("\n## Lines\n")
    body, _, _ = rest.partition("\n## Raw ")
    out, branches = [], {}
    for part in body.split("\n### ")[1:]:
        title, _, content = part.partition("\n")
        m = re.match(r"^case (\S+) — prompt sha256 [0-9a-f]{64}; branches: (.*)$", title)
        if m:
            branches[m.group(1)] = m.group(2)
            continue
        found = sidecar.section_key(kind, title, content)
        if not found:
            continue
        key, ruling = found
        status = STATUS.match(content)
        if kind == "classm":
            handle, case = f"{key[0]} — {key[1]}", branches.get(key[0])
        else:
            handle, case = key[0], None
        out.append({"handle": handle, "key": key, "status": status.group(1) if status else None,
                    "ruling": ruling, "case": case})
    return out


def _canon(s):
    try:
        return json.dumps(json.loads(s), sort_keys=True, ensure_ascii=False)
    except (ValueError, TypeError):
        return s


def content(kind, sec):
    """The disagreement content a repeat must share."""
    k = sec["key"]
    if kind == "transcription":
        return (sec["status"], _canon(k[1]), _canon(k[2]))
    if kind == "render":
        return (sec["status"], k[1])
    return (sec["status"], k[2], k[3])  # the case id is part of the handle


def excluded(ruling):
    """Why an earlier ruling may not be carried, else None."""
    text, drop = sidecar.split_ruling(ruling)
    if text == sidecar.OPEN:
        return "open"
    body = text[len("Ruling: "):] if text.startswith("Ruling: ") else text
    category = compare_families.ruling_category(body)
    if category == "finding" or re.match(r"defect\b", body, re.I):
        return "finding or defect"
    if category in ("interface_gap", "unclassified"):
        # An interface gap is an unresolved contract and unclassified prose no class at all;
        # both stay pending in compare_families.py and are re-judged when they recur.
        return "unsettled class (" + category.replace("_", " ") + ")"
    return None


def carried_text(ruling, source, date):
    text = sidecar.split_ruling(ruling)[0]
    if CARRIED.search(text):
        return text  # already carried: it names the review it was first written in
    return f"{text} (carried over from {source}, review of {date})"


# ---------------------------------------------------------------- sources

def _blob(text):
    data = text.encode()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def introducing_commit(rel, text):
    """The first commit in which `rel` had exactly `text`, else None."""
    want = _blob(text)
    out = _git("log", "--reverse", "--format=commit %H", "--raw", "--no-abbrev", "--", rel) or ""
    commit = None
    for line in out.splitlines():
        if line.startswith("commit "):
            commit = line[7:]
        elif line.startswith(":") and line.split()[3] == want:
            return commit
    return None


def subject_commit(kind, fid, recorded):
    """The newest commit whose subject of `fid` equals the recorded one, else None."""
    rel = subjects.path(kind, fid, Y)
    rel = os.path.relpath(rel, ROOT)
    for rev in (_git("log", "--format=%H", "--", rel) or "").split():
        text = _git("show", f"{rev}:{rel}")
        if text is not None and subjects.of_text(kind, text) == recorded:
            return rev
    return None


def recorded(text, field):
    m = re.search(rf"^\| {field} \| (.*?) \|$", text, re.M)
    return m.group(1) if m else None


def source_log(kind, form, family, origin):
    """(source text, label, snapshot) for the earlier log, or (None, reason, None)."""
    stem = families.stem(form, family)
    rel = f"reviews/{Y}/{kind}/{stem}.md"  # where the log is committed
    if origin is None or origin.startswith("git:"):
        rev = "HEAD" if origin is None else origin[4:]
        text = _git("show", f"{rev}:{rel}")
        label = f"{rel} at {(_git('rev-parse', '--short', rev) or rev).strip()}"
    else:
        if os.path.isdir(origin):
            path = os.path.join(origin, ARCHIVE_PREFIX[kind] + stem + ".md")
            if not os.path.exists(path):
                path = os.path.join(origin, stem + ".md") if kind == "transcription" else path
        elif origin.endswith(".rulings.json"):
            path = origin[: -len(".rulings.json")] + ".md"
        else:
            path = origin
        text = open(path, encoding="utf-8").read() if os.path.exists(path) else None
        label = os.path.relpath(os.path.abspath(path), ROOT)
    if text is None:
        return None, "no source log", None
    rev = introducing_commit(rel, text)
    if rev is None:
        subject = recorded(text, "subject sha256")
        rev = subject and subject_commit(kind, form, subject)
    if rev is None:
        return None, "the source log's forms are in no commit", None
    return text, label, snapshot(rev)


_snapshots = {}


def snapshot(rev):
    """One Snapshot per commit, shared by every log carried from it."""
    if rev not in _snapshots:
        _snapshots[rev] = Snapshot(rev)
    return _snapshots[rev]


# ---------------------------------------------------------------- carry

def plan(kind, form, family=families.DEFAULT, origin=None, current=None):
    """(rulings for rule.apply, report counter, [(handle, why)] for every section left open)."""
    stats = collections.Counter()
    path = sidecar.log_path(kind, form, family)
    text = open(path, encoding="utf-8").read()
    targets = [s for s in sections(kind, text) if s["ruling"] == sidecar.OPEN]
    stats["open"] = len(targets)
    if not targets:
        return {}, stats, []
    current = current or Snapshot(None)
    reviewed = current.read(os.path.relpath(subjects.path(kind, form, Y), ROOT))
    if reviewed is None or recorded(text, "subject sha256") != subjects.of_text(kind, reviewed):
        return {}, stats, [(s["handle"], "the log is stale; rerun first") for s in targets]
    src, label, snap = source_log(kind, form, family, origin)
    if src is None:
        return {}, stats, [(s["handle"], label) for s in targets]
    date = recorded(src, "date") or "unknown date"
    earlier = {}
    for s in sections(kind, src):
        earlier.setdefault(s["handle"], []).append(s)
    out, left = {}, []
    for s in targets:
        cands = [e for e in earlier.get(s["handle"], []) if content(kind, e) == content(kind, s)]
        if not cands:
            left.append((s["handle"], "no earlier ruling on the same disagreement")); continue
        e = cands[0]
        why = excluded(e["ruling"])
        if why:
            left.append((s["handle"], f"earlier ruling not carried: {why}")); continue
        printed = s["key"][1] if kind == "classm" else s["handle"]
        old, new = line_subject(kind, snap, form, printed), line_subject(kind, current, form, printed)
        if old is None or new is None:
            left.append((s["handle"], "line not found in the reviewed forms")); continue
        if old != new:
            left.append((s["handle"], "the project line or what it reads changed")); continue
        text = carried_text(e["ruling"], label, date)
        # A class M model error dropped from the fixture is dropped again (rule.py does it).
        out[s["handle"]] = {"ruling": text, "drop": True} if sidecar.split_ruling(e["ruling"])[1] else text
    stats["carried"] = len(out)
    return out, stats, left


def carry(kind, form, family=families.DEFAULT, origin=None, dry_run=False, current=None):
    ruled, stats, left = plan(kind, form, family, origin, current)
    if ruled and not dry_run:
        applied = rule.apply(form, ruled, kind, family)
        assert sorted(applied) == sorted(ruled), (applied, ruled)
    return ruled, stats, left


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--kind", required=True, choices=sorted(sidecar.KINDS))
    ap.add_argument("--form", required=True, help="a form id, or 'all' for every log of the kind and family")
    ap.add_argument("--family", default=families.DEFAULT)
    ap.add_argument("--from", dest="origin", help="earlier log, its .rulings.json, an archive directory or git:<rev> (default git:HEAD)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--depth", type=int, help="follow references only this many lines deep (default: all; "
                    "0 compares the line alone); a looser check carries more and is less precise")
    ap.add_argument("--verbose", action="store_true", help="print every section left open and why")
    a = ap.parse_args(argv)
    global DEPTH
    DEPTH = a.depth
    forms = [f for f, fam in sidecar.forms_with_logs(a.kind) if fam == a.family] if a.form == "all" else [a.form]
    total, current = collections.Counter(), Snapshot(None)
    for form in forms:
        ruled, stats, left = carry(a.kind, form, a.family, a.origin, a.dry_run, current)
        total.update(stats)
        reasons = collections.Counter(w for _, w in left)
        total.update({"left: " + w: n for w, n in reasons.items()})
        if stats["open"]:
            print(f"{families.stem(form, a.family)}: {stats['open']} open, {len(ruled)} carried"
                  + (" (dry run)" if a.dry_run else "") + "".join(f"; {n} {w}" for w, n in sorted(reasons.items())))
        if a.verbose:
            for h, w in left:
                print(f"  open {h}: {w}")
    print(f"{a.kind} [{a.family}]: {total['carried']} carried, {total['open'] - total['carried']} left open of {total['open']}"
          + (" (dry run; nothing written)" if a.dry_run else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
