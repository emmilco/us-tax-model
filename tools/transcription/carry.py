#!/usr/bin/env python3
"""Rule review disagreements without adjudication: model errors on the declaration, and earlier
rulings carried over to repeat disagreements.

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
- the same project line: the line and everything it reads, followed as the
  evaluator resolves references (closure: lines, definition instances, the
  collections it sums over, tables, and only the year parameters it names), is
  unchanged between the source log's commit and the working tree, each part as
  the review kind sees it (view: citations left out, and for transcription and
  class M wording left out too); for render also the line's rendered section;
- the earlier ruling is of a settled class: not a finding or defect (those are
  re-judged), not an interface gap or unclassified prose (still pending in
  compare_families.py), and not open.

A class M ruling that dropped the line from the fixture is carried with its
drop, which rule.py repeats on the fixture.

Before carrying, a transcription disagreement whose reply fails the host's
schema, type or reference validation on the line or a line it reads (the
comparison records those failures beside the reply's tree as
`invalid_model_types`) is ruled a model error on the declaration mechanically,
with the validation messages: the project's own rules class it so whatever the
source says (reviews/<year>/transcription/adjudication/README.md, "model
error"), and the line was not executed. No earlier ruling is needed. A reply
that merely omits a `shown_when` is not ruled this way: whether the source
conditions the line's display is a source reading, and earlier rulings on such
lines split between model error, scope, representation and interface gap.

A render objection is free text, so render matches on the restated English and
the status (MISMATCH, UNCLEAR, MISSING), not on the objection's wording.

The source is the log the ruling was written in: by default every committed
version of the same log, newest first, each read with the forms of the commit
that wrote it (a pre-commit check holds every committed log's subject current);
else a log, its rulings sidecar, an archive directory (`<stem>.md`,
`render.<stem>.md`, `classm.<stem>.md`) or `git:<rev>`, whose forms are read from
the commit that introduced it, or matched by its recorded subject hash when it
is in no commit; a source whose forms cannot be found carries nothing. Across
versions, the newest settled ruling on the same disagreement whose line was
then as it is now carries; a newer finding, defect or unsettled ruling on the
same disagreement stops the search.

A transcription disagreement whose reply differs from the earlier one (so no
earlier section has the same content) is still a repeat when the reply differs
from the project's line exactly as an earlier ruled reply did: the form's
triage record evaluated the section's reply on the current form and found it
differing, and an earlier ruling in the form's sidecar on the same handle
carries the same triage stamp (verdict, kinds of difference, witness inputs and
triage policy) and the same line subject (the line and what it reads, as
above). The newest such ruling carries, naming that it matched by triage kinds
and witnesses; a ruling of a re-judged class stops it.

Last, a transcription disagreement still open is ruled from the form's
executable triage record (triage.py, .transcription/triage/) when that record
evaluated the very reply the section records, on the current form, and found
the project's line and the reply's agreeing on every input it ran: no value
different, missing or invalid, compared on fixture cases and on at least
MIN_GENERATED generated returns, with no evaluation failure. The ruling is
"representation; equivalent on executable triage, ruled mechanically" with the
counts it rests on. One in AUDIT_EVERY such disagreements, chosen by a hash of
the disagreement's identity (not by time, so a rerun chooses the same ones), is
left open and listed as held for adjudication, so that a broken rule shows in an
agent's ruling. A disagreement an earlier ruling of a re-judged class answered
(a finding, a defect, an unsettled class) is not ruled by triage.

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
jurisdiction = sidecar.jurisdiction  # --jurisdiction ny: the New York documents, which read federal ones


def _dirs(top):
    """Repository-relative per-year directories the jurisdiction reads: <top>/<year>, then (New York) <top>/ny/<year>."""
    return [f"{top}/{Y}"] + ([f"{top}/ny/{Y}"] if jurisdiction.NY else [])


def _rel(top, doc_id, ext):
    return f"{top}/ny/{Y}/{doc_id}{ext}" if jurisdiction.is_ny(doc_id) else f"{top}/{Y}/{doc_id}{ext}"
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
            names = []
            for rel in _dirs("forms"):
                if self.rev is None:
                    names += os.listdir(os.path.join(ROOT, rel)) if os.path.isdir(os.path.join(ROOT, rel)) else []
                else:
                    names += [os.path.basename(n) for n in (_git("ls-tree", "--name-only", self.rev, f"{rel}/") or "").split()]
            self._cache["__forms"] = sorted(n[:-5] for n in names if n.endswith(".yaml"))
        return self._cache["__forms"]

    def tables(self):
        """{table id: repository-relative path}."""
        if "__tables" not in self._cache:
            out = {}
            for rel in _dirs("tables"):
                if self.rev is None:
                    d = os.path.join(ROOT, rel)
                    names = os.listdir(d) if os.path.isdir(d) else []
                else:
                    names = [os.path.basename(n) for n in (_git("ls-tree", "--name-only", self.rev, f"{rel}/") or "").split()]
                out.update({n.split(".")[0]: f"{rel}/{n}" for n in sorted(names)})
            self._cache["__tables"] = out
        return self._cache["__tables"]

    def doc(self, fid):
        key = "__doc " + fid
        if key not in self._cache:
            text = self.read(_rel("forms", fid, ".yaml"))
            raw = yaml.load(text, Loader=_Loader) if text else None
            self._cache[key] = (raw.get("form") or raw.get("def")) if raw else None
            self._cache["__subject " + fid] = subjects._sha(subjects._without_cites(raw)) if raw else None
        return self._cache[key]

    def subject(self, fid):
        """subjects.of_form of a document, from the parse already made."""
        self.doc(fid)
        return self._cache["__subject " + fid]

    def params(self):
        """({parameter name: entry}, {enum name: entry}) of the year parameters (in New York mode
        merged with the New York ones, as the canonical build merges them)."""
        if "__params" not in self._cache:
            values, enums = {}, {}
            for rel in [f"params/{Y}.yaml"] + ([f"params/ny/{Y}.yaml"] if jurisdiction.NY else []):
                text = self.read(rel)
                raw = (yaml.load(text, Loader=_Loader) or {}) if text else {}
                p = raw.get("params") or raw
                values.update(p.get("values") or {})
                enums.update(p.get("enums") or {})
            self._cache["__params"] = (values, enums)
        return self._cache["__params"]

    def line(self, fid, line_id):
        """A document's line by id, else None."""
        key = "__line " + fid
        if key not in self._cache:
            self._cache[key] = {l["id"]: l for l in (self.doc(fid) or {}).get("lines", [])}
        return self._cache[key].get(line_id)


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


def _dicts(o):
    if isinstance(o, dict):
        yield o
        for k, v in o.items():
            if k != "cite":
                yield from _dicts(v)
    elif isinstance(o, list):
        for x in o:
            yield from _dicts(x)


def _sha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


DEPTH = None  # how many references deep closure() follows; None follows every one


def view(kind):
    """What a review kind sees of a line, a document's own fields or a parameter: render judges
    wording, so only citations are left out; transcription and class M judge computation, so
    wording (subjects.WORDING) is left out as well."""
    if kind == "render":
        return subjects._without_cites
    return lambda o: subjects._without_cites(subjects._unworded(o) if isinstance(o, dict) else o)


ENUM = re.compile(r"^Enum\(([^()]+)\)$")


def closure(snap, fid, line, depth=None, kind="transcription"):
    """What a line reads, as {node: hash}, each node hashed as the review `kind` sees it (view).
    References are resolved as the evaluator resolves them (engine/src/eval.ts):

    - a string naming a line of the document being read (a definition's lines are named by their
      local ids), else a line `<doc>.<name>` of another document: that line, followed;
    - a definition instance ({def, bind, line}): the definition's `line`, followed within the
      definition; the bound operands are strings of the calling line, followed there;
    - a sum over a collection ({collection, field, where}): the field and the `where` lines are
      strings, followed; of the collection document, its own fields (the roster's parent and
      implicit entry) are read;
    - a year parameter ({param: name}, {op: param, ref: name}) or an Enum(name) type: that entry;
    - a table id: the table file.

    The own fields (everything but the lines) of every document a followed line belongs to are
    included. A string that names a document, or starts with a document id, and is none of the above
    stands for the whole document (its own fields and every line, followed), which over-collects:
    over-collecting only makes a carry less likely."""
    tables, (params, enums), see = snap.tables(), snap.params(), view(kind)
    forms = set(snap.forms())
    out = {}

    def head(d):
        if "head " + d not in out:
            doc = snap.doc(d) or {}
            out["head " + d] = _sha(see({k: v for k, v in doc.items() if k != "lines"}))

    todo, seen = [(fid, line, 0)], set()
    while todo:
        f, l, n = todo.pop(0)
        if (f, l["id"]) in seen:
            continue
        seen.add((f, l["id"]))
        out[f"line {f}:{l['id']}"] = _sha(see(l))
        head(f)
        if depth is not None and n >= depth:
            continue
        body = {k: v for k, v in l.items() if k != "id"}
        named = set()
        for o in _dicts(body):
            d = o.get("def")
            if isinstance(d, str) and d in forms and (snap.doc(d) or {}).get("kind") == "def":
                head(d)
                named.add(d)
                target = snap.line(d, o.get("line"))
                if target is None:
                    todo += [(d, dl, n + 1) for dl in snap.doc(d).get("lines", [])]
                else:
                    todo.append((d, target, n + 1))
            c = o.get("collection")
            if isinstance(c, str) and c in forms:
                head(c)
                named.add(c)
        for s in _strings(body):
            m = ENUM.match(s)
            if m and m.group(1) in enums:
                out["enum " + m.group(1)] = _sha(see(enums[m.group(1)]))
                continue
            if s in params:
                out["param " + s] = _sha(see(params[s]))
                continue
            if s in tables:
                out["table " + s] = hashlib.sha256((snap.read(tables[s]) or "").encode()).hexdigest()
                continue
            if s in named:
                continue
            target = snap.line(f, s)
            base = re.split(r"[\[\]]", s)[0]
            owner = re.split(r"[.\[]", s)[0]
            if target is None and owner in forms:
                target = snap.line(owner, base)
            if target is not None:
                todo.append((f if snap.line(f, s) is not None else owner, target, n + 1))
                continue
            d = owner if owner in forms else s if s in forms else None
            if d is not None and (d != f or s == d) and "doc " + d not in out:
                out["doc " + d] = _sha([see(x) for x in (snap.doc(d) or {}).get("lines", [])])
                head(d)
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
    text = snap.read(_rel("rendered", fid, ".md"))
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
    nodes = closure(snap, fid, line, DEPTH, kind)
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


MECHANICAL = "Ruling: model error on the declaration, ruled mechanically"


def mechanical(kind, sec):
    """The ruling the project's own rules give a section without a source reading, else None: a
    transcription disagreement whose second side is the reply's tree beside the validation
    failures that reach the line (transcribe.checked_second)."""
    if kind != "transcription" or sec["status"] != "DISAGREE":
        return None
    try:
        second = json.loads(sec["key"][2])
    except (ValueError, TypeError):
        return None
    if not isinstance(second, dict) or set(second) != {"invalid_model_types", "expression"} or not second["invalid_model_types"]:
        return None
    messages = sorted({f'{e.get("line") or "the reply"}: "{" ".join(str(e.get("message", "")).split())}"'
                       for e in second["invalid_model_types"] if isinstance(e, dict)})
    if not messages:
        return None
    return (f"{MECHANICAL}: the reply fails the host's schema, type or reference validation on this line or a line "
            f"it reads ({'; '.join(messages)}), so the line was not executed. This adjudicates the declaration, "
            "not the tax reading.")


TRIAGE_RULING = "Ruling: representation; equivalent on executable triage, ruled mechanically"
AUDIT_EVERY = 10      # one in AUDIT_EVERY triage-equivalent disagreements is held for an agent instead
MIN_GENERATED = 500   # the generated returns a triage run needs before its agreement rules anything


def held_for_audit(kind, form, family, sec):
    """Whether a triage-equivalent disagreement is held for adjudication: one in AUDIT_EVERY, chosen by the
    disagreement's identity (log stem, handle, status and both sides), so the same disagreement is always
    held or always ruled, whenever and however often the step runs."""
    ident = json.dumps([kind, families.stem(form, family), sec["handle"], *content(kind, sec)], ensure_ascii=False)
    return int(hashlib.sha256(ident.encode()).hexdigest(), 16) % AUDIT_EVERY == 0


def triage_equivalence(record, line, subject):
    """(ruling text, None) when the triage line shows the project's line and the reply's agreeing on every
    fixture case and every generated return run, else (None, why). `record` is the form's triage record,
    `line` its line for the section and the reply the section records (rulings.triage_line), `subject` the
    form's current transcription subject."""
    import triage
    if record.get("policy") != triage.POLICY:
        return None, f"triage record of another policy ({record.get('policy')})"
    if record.get("subject_sha256") != subject:
        return None, "triage record of an earlier version of the form; rerun triage"
    state = (record.get("passes") or {}).get(line.get("pass")) if line.get("pass") else record
    bank = (state or {}).get("bank") or {}
    if (state or {}).get("state") != "evaluated" or (state or {}).get("errors"):
        return None, "triage did not evaluate the reply"
    if line.get("triage") != "agrees on sample":
        return None, f"triage: {line.get('triage')}"
    sources = line.get("sources") or {}
    if bank.get("evaluation_failures") or line.get("absent") or line.get("differ") or line.get("invalid"):
        return None, "triage: not every input evaluated alike"
    if (bank.get("generated") or 0) < MIN_GENERATED or not sources.get("fixture") or not sources.get("generated"):
        return None, "triage: the line was not compared on the fixtures and enough generated returns"
    return (f"{TRIAGE_RULING}: the project's line and the reply's agree on every input triage ran "
            f"({line['compared']} values compared, none different or missing: {sources.get('fixture', 0)} on "
            f"{bank.get('fixtures')} fixture cases, {sources.get('generated', 0)} on {bank['generated']} generated returns "
            f"seed {bank.get('seed')}, {sources.get('partial', 0)} on {bank.get('partial_records', 0)} partial records; "
            f"policy {record['policy']}). No agent read the source; one in {AUDIT_EVERY} such disagreements is "
            "held for adjudication instead."), None


def _triage_record(form, family):
    path = sidecar.triage_path(form, family)
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def triage_repeats(kind, form, family, text, targets, current):
    """({handle: ruling} for open transcription sections whose reply differs from the project's line exactly as
    the reply of an earlier settled ruling did, [(handle, why)] for those an earlier ruling of a re-judged class
    matches). A repeat: the form's triage record evaluated the section's reply on the current form and found it
    differing; an earlier ruling in the form's sidecar on the same handle carries the same triage stamp (verdict,
    kinds of difference, witness inputs, triage policy: rulings.triage_stamp) and was made when the line and what
    it reads (line_subject) were as they are now. The newest such ruling carries, naming that it matched by triage."""
    if kind != "transcription":
        return {}, []
    record = _triage_record(form, family)
    if record is None or record.get("subject_sha256") != subjects.current("transcription", form, Y):
        return {}, []
    side = sidecar.load(kind, form, family)
    blocks = sidecar.pass_blocks(text)
    contents = {key[0]: c for key, _, c in sidecar.log_sections(kind, text, with_content=True)}
    out, stopped = {}, []
    for s in targets:
        if s["status"] != "DISAGREE" or s["handle"] not in contents:
            continue
        run = sidecar.section_run(kind, text, s["handle"], contents[s["handle"]], blocks)
        line = sidecar.triage_line(record, s["handle"], run)
        if line is None or line.get("triage") != "differs" or not line.get("witnesses"):
            continue
        stamp = sidecar.triage_stamp(record, line)
        subject = line_subject(kind, current, form, s["handle"])
        same = [v for k, v in side.items() if k[0] == s["handle"] and v.get("triage") == stamp and subject
                and v.get("subject_key") == subject and v.get("ruling")]
        if not same:
            continue
        same.sort(key=lambda v: v.get("date") or "", reverse=True)
        stop = excluded(same[0]["ruling"])
        if stop:
            stopped.append((s["handle"], f"earlier ruling not carried: {stop} (matched by triage kinds and witnesses)"))
            continue
        out[s["handle"]] = carried_text(same[0]["ruling"], f"{families.stem(form, family)}.rulings.json, matched by "
                                        "triage kinds and witnesses", same[0].get("date") or "unknown date")
    return out, stopped


def triage_rulings(kind, form, family, text, targets):
    """({handle: ruling} for open transcription sections triage shows equivalent, [(handle, why)] for those held
    for adjudication by the one-in-AUDIT_EVERY sample). Without a triage record of the form, nothing."""
    if kind != "transcription":
        return {}, []
    record = _triage_record(form, family)
    if record is None:
        return {}, []
    subject = subjects.current("transcription", form, Y)
    blocks = sidecar.pass_blocks(text)
    contents = {key[0]: c for key, _, c in sidecar.log_sections(kind, text, with_content=True)}
    out, held = {}, []
    for s in targets:
        if s["status"] != "DISAGREE" or s["handle"] not in contents:
            continue
        run = sidecar.section_run(kind, text, s["handle"], contents[s["handle"]], blocks)
        line = sidecar.triage_line(record, s["handle"], run)
        if line is None:
            continue
        ruling, _ = triage_equivalence(record, line, subject)
        if ruling is None:
            continue
        if held_for_audit(kind, form, family, s):
            held.append((s["handle"], f"triage-equivalent, held for adjudication (the one-in-{AUDIT_EVERY} audit sample)"))
        else:
            out[s["handle"]] = ruling
    return out, held


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
    rel = f"{_dirs('reviews')[-1]}/{kind}/{stem}.md"  # where the log was committed before the review store
    if origin is None or origin.startswith("git:"):
        rev = "HEAD" if origin is None else origin[4:]
        text, rel, blob = committed_log(kind, form, family, rev)
        label = f"{rel} at {(_git('rev-parse', '--short', rev) or rev).strip()}"
    else:
        blob = None
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
    rev = introducing_commit(rel, blob if blob is not None else text)
    if rev is None:
        subject = recorded(text, "subject sha256")
        rev = subject and subject_commit(kind, form, subject)
    if rev is None:
        return None, "the source log's forms are in no commit", None
    return text, label, snapshot(rev)


def source_logs(kind, form, family, origin):
    """[(source text, label, snapshot)] of the earlier logs, newest first, or ([], reason). By
    default every committed version of the log, each with the forms of the commit that wrote it (a
    pre-commit check holds every committed log current); else the one log `origin` names."""
    if origin is not None:
        text, label, snap = source_log(kind, form, family, origin)
        return ([(text, label, snap)], None) if text is not None else ([], label)
    md, index = _log_rels(kind, form, family)
    out = []
    for rev in (_git("log", "--format=%H", "--", index, md) or "").split():
        text, rel, _ = committed_log(kind, form, family, rev)
        if text is not None:
            out.append((text, f"{rel} at {rev[:8]}", snapshot(rev)))
    return (out, None) if out else ([], "no source log")


def _log_rels(kind, form, family):
    """(the log file a form's review was committed as before the review store, its index)."""
    base = f"{_dirs('reviews')[-1]}/{kind}/{families.stem(form, family)}"
    return base + ".md", base + ".index.json"


def committed_log(kind, form, family, rev):
    """(log text, repository-relative path it was committed under, that file's text) of a form's review at
    a commit: the view of its index and records (review_store), or before the store the log file; Nones
    when the commit holds neither."""
    import review_store
    md, index = _log_rels(kind, form, family)
    raw = _git("show", f"{rev}:{index}")
    if raw is not None:
        return review_store.view(kind, form, family, read=review_store._reader(rev)), index, raw
    text = _git("show", f"{rev}:{md}")
    return text, md, text


_snapshots = {}


def snapshot(rev):
    """One Snapshot per commit, shared by every log carried from it."""
    if rev not in _snapshots:
        _snapshots[rev] = Snapshot(rev)
    return _snapshots[rev]


# ---------------------------------------------------------------- carry

def log_is_current(kind, form, text, current, family=families.DEFAULT):
    """Whether the log describes the document in `current`. Against the working tree this is the test
    check_logs.py applies: review_store.state for a stored review (which reads a whole-form subject carried
    across a rename), else subjects.log_state; a log with line-scoped passes is current when every compared
    line's subject is, whatever its header's whole-form subject records. Against a commit or an in-memory
    snapshot only the header's whole-form subject is compared, which can refuse a current line-scoped log
    but never accepts a stale one."""
    if current.rev is None:
        import review_store
        state = review_store.state(kind, form, family, Y)
        if state is review_store.NO_INDEX:
            state = subjects.log_state(kind, form, Y, text)
        return state is None
    reviewed = current.read(os.path.relpath(subjects.path(kind, form, Y), ROOT))
    return reviewed is not None and recorded(text, "subject sha256") == subjects.of_text(kind, reviewed)


def plan(kind, form, family=families.DEFAULT, origin=None, current=None):
    """(rulings for rule.apply, report counter, [(handle, why)] for every section left open)."""
    stats = collections.Counter()
    text = sidecar.read_log(kind, form, family)
    targets = [s for s in sections(kind, text) if s["ruling"] == sidecar.OPEN]
    stats["open"] = len(targets)
    if not targets:
        return {}, stats, []
    current = current or Snapshot(None)
    if not log_is_current(kind, form, text, current, family):
        return {}, stats, [(s["handle"], "the log is stale; rerun first") for s in targets]
    out = {s["handle"]: m for s in targets for m in [mechanical(kind, s)] if m}
    stats["mechanical"] = len(out)
    targets = [s for s in targets if s["handle"] not in out]
    if not targets:
        return out, stats, []
    srcs, reason = source_logs(kind, form, family, origin)
    left = []
    if not srcs:
        left = [(s["handle"], reason) for s in targets]
    else:
        earlier = []  # per source, newest first: (label, date, snapshot, {handle: [sections]})
        for src, label, snap in srcs:
            by_handle = {}
            for e in sections(kind, src):
                by_handle.setdefault(e["handle"], []).append(e)
            earlier.append((label, recorded(src, "date") or "unknown date", snap, by_handle))
        for s in targets:
            ruled, why = match(kind, form, s, earlier, current)
            if ruled is None:
                left.append((s["handle"], why)); continue
            e, label, date = ruled
            ruling = carried_text(e["ruling"], label, date)
            # A class M model error dropped from the fixture is dropped again (rule.py does it).
            out[s["handle"]] = {"ruling": ruling, "drop": True} if sidecar.split_ruling(e["ruling"])[1] else ruling
    # A repeat whose reply differs from the line as an earlier ruled reply did (triage kinds and witnesses).
    open_left = {h for h, why in left if not why.startswith("earlier ruling not carried")}
    repeats, stopped = triage_repeats(kind, form, family, text, [s for s in targets if s["handle"] in open_left], current)
    for h, ruling in repeats.items():
        out[h] = {"ruling": ruling, "drop": True} if sidecar.split_ruling(ruling)[1] else ruling
    stopped_why = dict(stopped)
    left = [(h, stopped_why.get(h, why)) for h, why in left if h not in repeats]
    stats["carried"] = len(out) - stats["mechanical"]
    stats["by_triage_match"] = len(repeats)
    # Executable triage rules what is left, except a disagreement an earlier ruling of a re-judged class
    # (a finding, a defect, an unsettled class) already answered: that ruling is not overridden.
    open_left = {h for h, why in left if not why.startswith("earlier ruling not carried")}
    ruled, held = triage_rulings(kind, form, family, text, [s for s in targets if s["handle"] in open_left])
    out.update(ruled)
    stats["triage"], stats["held"] = len(ruled), len(held)
    held_why = dict(held)
    left = [(h, held_why.get(h, why)) for h, why in left if h not in ruled]
    return out, stats, left


def match(kind, form, s, earlier, current):
    """((earlier section, label, date), None) for the ruling to carry to open section `s`, else (None, why).
    The sources are searched newest first for a section on the same line with the same disagreement
    content. An open one is passed over; a ruling of a class that is re-judged (excluded) stops the
    search, so a later finding is never overridden by an older settled ruling; a settled ruling
    carries when the line and what it reads were then as they are now, else the search goes on."""
    printed = s["key"][1] if kind == "classm" else s["handle"]
    new = line_subject(kind, current, form, printed)
    if new is None:
        return None, "line not found in the reviewed forms"
    why = "no earlier ruling on the same disagreement"
    for label, date, snap, by_handle in earlier:
        cands = [e for e in by_handle.get(s["handle"], []) if content(kind, e) == content(kind, s)]
        if not cands or cands[0]["ruling"] == sidecar.OPEN:
            continue
        e = cands[0]
        stop = excluded(e["ruling"])
        if stop:
            return None, f"earlier ruling not carried: {stop}"
        old = line_subject(kind, snap, form, printed)
        if old == new:
            return (e, label, date), None
        if old is not None:
            why = "the project line or what it reads changed"
        elif why == "no earlier ruling on the same disagreement":
            why = "line not found in the reviewed forms"
    return None, why


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
    ap.add_argument("--from", dest="origin", help="earlier log, its .rulings.json, an archive directory or git:<rev> (default: every committed version of the log)")
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
            print(f"{families.stem(form, a.family)}: {stats['open']} open, {stats['mechanical']} ruled mechanically, "
                  f"{stats['carried']} carried, {stats['triage']} ruled by triage"
                  + (" (dry run)" if a.dry_run else "") + "".join(f"; {n} {w}" for w, n in sorted(reasons.items())))
        for h, w in left:
            if a.verbose or w.startswith("triage-equivalent, held"):
                print(f"  open {h}: {w}")
    ruled = total["carried"] + total["mechanical"] + total["triage"]
    print(f"{a.kind} [{a.family}]: {total['mechanical']} ruled mechanically, {total['carried']} carried, "
          f"{total['triage']} ruled by triage ({total['held']} held for adjudication), "
          f"{total['open'] - ruled} left open of {total['open']}"
          + (" (dry run; nothing written)" if a.dry_run else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
