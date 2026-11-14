#!/usr/bin/env python3
"""Year changes as operations keyed by line id.

The operations that take one tax year's definitions to the next are data in changes/<year>/<form>.yaml
(changes/ny/<year>/ for New York): per form, a list of entries, each a change of the change map with its
evidence (archived document, page, quote printed there; draft or verified against a final edition) and its
operations on line ids:

    add_line {after, line}            set {line, field, from, to}        add_form {form}
    remove_line {line}                set_form {field, from, to}
    add_question {input, like | after, entry, profiles}
    remove_question {input}           set_question {input, field, from, to}

`field` is a path of mapping keys (`printed`, `expr.take`, `cite.locator`); `from: null` means absent and
`to: null` removes the field. `add_question` places the new bank entry after `like` or `after`; `like` also lends
its order number and its place in every profile, never its wording. An entry may list lines it `awaits`
({line, change}): lines another change, not yet written as operations, is to add; reading one is reported, not
failed, until adoption, which refuses while one is missing. An entry's `note` is free text. The operations of year N+1 are applied, in memory, to the forms, question bank and
profiles of year N; an operation fails, named with its file, change, position, kind and line, when its line, form
or anchor is gone, the value it expects to replace has changed (stale), it is already applied, it collides with
another operation, it leaves a reference dangling or a gated input read outside its gate, a new input has no
question or a question outlives its input, or its evidence is not printed where it says.

    year_changes.py [--year N] --check             apply changes/<N+1> to the year-N tree; exit 1 on a failure
    year_changes.py [--year N] --check --against DIR   the same on DIR's forms/<N>, interview/<N>, params/<N>.yaml
    year_changes.py [--year N] --record EDITED.yaml    print the operations that turn forms/<N>/<form>.yaml into
                                                       EDITED.yaml (evidence to be written by hand)
    year_changes.py --self-test                    plants each way an operation stops applying

`year_diff.py --adopt` calls check() before copying a year and write() after relocating the copy: the operations'
values are written for the new year, so they replace the relocated values of the fields they set, and every line
block, bank entry and profile line no operation touches keeps the text the copy wrote.
"""

import argparse
import copy
import difflib
import json
import re
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import taxyear  # noqa: E402,F401  (--year)
import jurisdiction  # noqa: E402  (--jurisdiction ny)
from jurisdiction import ypath  # noqa: E402

_Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

KINDS = ("add_line", "remove_line", "set", "add_form", "set_form", "add_question", "remove_question", "set_question")
REQUIRED = {"add_line": ("after", "line"), "remove_line": ("line",), "set": ("line", "field", "from", "to"),
            "add_form": ("form",), "set_form": ("field", "from", "to"), "add_question": ("input",),
            "remove_question": ("input",), "set_question": ("input", "field", "from", "to")}
NOT_REFS = {"cite", "source", "label", "op", "ref", "def", "line", "note"}  # as engine/src/gates.ts refsOf
REF = re.compile(r"^([A-Za-z0-9_$]+)(?:\[[^\]]*\])?\.([A-Za-z0-9_.]+)$")


def load_yaml(text):
    return yaml.load(text, Loader=_Loader)


def short(value, n=160):
    s = json.dumps(value, ensure_ascii=False) if not isinstance(value, str) else repr(value)
    return s if len(s) <= n else s[:n - 3] + "..."


# ---------------------------------------------------------------- a year's tree

class Tree:
    """One year's forms, question bank, profiles, other interview files and parameter ids."""

    def __init__(self, forms_dir, interview_dir, params_file):
        self.forms_dir, self.interview_dir = Path(forms_dir), Path(interview_dir)
        self.forms = {}  # id -> {"path", "key", "doc", "text"}
        for p in sorted(self.forms_dir.glob("*.yaml")):
            text = p.read_text(encoding="utf-8")
            data = load_yaml(text) or {}
            key = "form" if "form" in data else "def"
            self.forms[data[key]["id"]] = {"path": p, "key": key, "doc": data[key], "text": text}
        self.bank_path = self.interview_dir / "questions.yaml"
        self.bank_text = self.bank_path.read_text(encoding="utf-8") if self.bank_path.exists() else ""
        self.bank = (load_yaml(self.bank_text) or {}).get("bank", {"questions": []}) if self.bank_text else {"questions": []}
        self.profiles, self.others = {}, {}
        for p in sorted(self.interview_dir.rglob("*.yaml")) if self.interview_dir.is_dir() else []:
            if p == self.bank_path:
                continue
            text = p.read_text(encoding="utf-8")
            data = load_yaml(text)
            iv = data.get("interview") if isinstance(data, dict) else None
            if isinstance(iv, dict) and isinstance(iv.get("questions"), list):
                self.profiles[p.relative_to(self.interview_dir).as_posix()] = {"path": p, "text": text, "data": data}
            self.others[p.relative_to(self.interview_dir).as_posix()] = data
        params = load_yaml(Path(params_file).read_text(encoding="utf-8")) if Path(params_file).exists() else {}
        self.params = set(((params or {}).get("params") or {}).get("values") or {})


def year_tree(year, root=None):
    """The tree of `year` in this checkout, or in the checkout or export at `root`."""
    if root is None:
        return Tree(ypath("forms", year), jurisdiction.interview_dir(year), jurisdiction.params_file(year))
    root = Path(root)
    rel = lambda p: root / Path(p).relative_to(ROOT)  # noqa: E731
    return Tree(rel(ypath("forms", year)), rel(jurisdiction.interview_dir(year)), rel(jurisdiction.params_file(year)))


# ---------------------------------------------------------------- the operations

class Op:
    def __init__(self, file, change, n, kind, body, entry):
        self.file, self.change, self.n, self.kind, self.body, self.entry = file, change, n, kind, body, entry

    @property
    def target(self):
        b = self.body
        if self.kind == "add_line":
            return (b.get("line") or {}).get("id", "?")
        if self.kind == "add_form":
            doc = b.get("form") or {}
            return (doc.get("form") or doc.get("def") or {}).get("id", "?")
        if self.kind in ("set_form",):
            return f"{self.entry['form']} {b.get('field')}"
        if self.kind in ("set", "set_question"):
            return f"{b.get('line') or b.get('input')} {b.get('field')}"
        return str(b.get("line") or b.get("input"))

    def __str__(self):
        return f"{self.file} {self.change} op {self.n} ({self.kind} {self.target})"


def load_changes(directory):
    """(entries, ops, problems): every entry of every file of a changes directory, in file order."""
    entries, ops, problems = [], [], []
    directory = Path(directory)
    for p in sorted(directory.glob("*.yaml")) if directory.is_dir() else []:
        data = load_yaml(p.read_text(encoding="utf-8")) or {}
        head = data.get("changes")
        if not isinstance(head, dict) or "form" not in head or not isinstance(head.get("entries"), list):
            problems.append(f"{p.name}: not a changes file (changes: tax_year, form, entries)")
            continue
        for e in head["entries"]:
            change = e.get("change", "?")
            entry = {"file": p.name, "form": head["form"],
                     "change": "+".join(change) if isinstance(change, list) else str(change),
                     "evidence": e.get("evidence") or [], "verified": e.get("verified"),
                     "awaits": e.get("awaits") or [], "ops": []}
            entries.append(entry)
            for n, raw in enumerate(e.get("operations") or [], 1):
                kinds = [k for k in KINDS if k in (raw or {})]
                if len(kinds) != 1 or not isinstance(raw[kinds[0]], dict):
                    problems.append(f"{p.name} {entry['change']} op {n}: malformed (one of {', '.join(KINDS)})")
                    continue
                op = Op(p.name, entry["change"], n, kinds[0], raw[kinds[0]], entry)
                missing = [f for f in REQUIRED[op.kind] if f not in op.body]
                if op.kind == "add_question" and not ("like" in op.body or "after" in op.body):
                    missing.append("like or after")
                if missing:
                    problems.append(f"{op}: malformed, missing {', '.join(missing)}")
                    continue
                entry["ops"].append(op)
                ops.append(op)
    return entries, ops, problems


# ---------------------------------------------------------------- applying in memory

def get_path(node, path):
    for k in path:
        if not isinstance(node, dict) or k not in node:
            return None
        node = node[k]
    return node


def set_path(node, path, value):
    for k in path[:-1]:
        node = node.setdefault(k, {})
    if value is None:
        node.pop(path[-1], None)
    else:
        node[path[-1]] = copy.deepcopy(value)


def refs_of(node, out=None):
    """Every string an expression or test can name a line with (engine/src/gates.ts refsOf)."""
    out = set() if out is None else out
    if isinstance(node, str):
        out.add(node)
    elif isinstance(node, list):
        for v in node:
            refs_of(v, out)
    elif isinstance(node, dict):
        for k, v in node.items():
            if k not in NOT_REFS and k != "param":
                refs_of(v, out)
    return out


def reads_of(line):
    out = refs_of(line.get("expr"))
    for r in line.get("refuses") or []:
        if isinstance(r, dict) and "when" in r:
            out.add(r["when"])
    for k in ("shown_when", "gated_by"):
        if isinstance(line.get(k), str):
            out.add(line[k])
    return out


def params_of(node, out=None):
    out = set() if out is None else out
    if isinstance(node, dict):
        if node.get("op") == "param" and isinstance(node.get("ref"), str):
            out.add(node["ref"])
        if isinstance(node.get("param"), str):
            out.add(node["param"])
        for v in node.values():
            params_of(v, out)
    elif isinstance(node, list):
        for v in node:
            params_of(v, out)
    return out


def all_strings(node, out=None):
    out = set() if out is None else out
    if isinstance(node, str):
        out.add(node)
        m = REF.match(node)
        if m:
            out.add(f"{m.group(1)}.{m.group(2)}")
    elif isinstance(node, list):
        for v in node:
            all_strings(v, out)
    elif isinstance(node, dict):
        for k, v in node.items():
            all_strings(k, out)
            all_strings(v, out)
    return out


def is_input(line):
    return isinstance(line.get("expr"), dict) and line["expr"].get("op") == "input"


class State:
    """The tree as data while operations are applied: forms (meta and lines), bank entries, profile lists."""

    def __init__(self, tree):
        self.forms = {}
        for fid, f in tree.forms.items():
            doc = copy.deepcopy(f["doc"])
            self.forms[fid] = {"key": f["key"], "doc": doc, "lines": doc.get("lines") or []}
        self.bank = copy.deepcopy(tree.bank.get("questions") or [])
        self.profiles = {name: list(p["data"]["interview"]["questions"]) for name, p in tree.profiles.items()}

    def line_index(self):
        return {l["id"]: (fid, i) for fid, f in self.forms.items() for i, l in enumerate(f["lines"])}

    def line(self, lid):
        for f in self.forms.values():
            for l in f["lines"]:
                if l["id"] == lid:
                    return l
        return None

    def bank_index(self, inp):
        return next((i for i, q in enumerate(self.bank) if q.get("input") == inp), None)


class Result:
    def __init__(self):
        self.failures = []  # (op or None, message)
        self.notes = []
        self.state = None
        self.touched = {}  # line id -> the last op that added or changed it
        self.removed = {}  # line id -> the op that removed it
        self.new_params = {}  # parameter id -> [op]

    def fail(self, op, msg):
        self.failures.append((op, msg))


def suggest(lid, ids):
    near = difflib.get_close_matches(lid, sorted(ids), n=2, cutoff=0.75)
    return f" (closest: {', '.join(near)})" if near else ""


def apply(tree, ops, strict=True, adopting=False):
    """Apply `ops` in order to a copy of `tree`. With `strict` (the check) a `set` must find its `from` value;
    without it (writing an adopted copy, already checked against the earlier year) the value is replaced as it is.
    A line an entry `awaits` (another change, not yet written, is to add it) may be read while preparing; when
    `adopting` it must exist."""
    r = Result()
    r.ops, r.adopting = ops, adopting
    st = State(tree)
    r.state = st
    base_lines = {lid for lid in st.line_index()}
    set_paths = {}  # (kind, target id) -> [(path, op)]
    added_inputs = {}

    def overlaps(key, path, op):
        for other, o in set_paths.get(key, []):
            n = min(len(other), len(path))
            if other[:n] == path[:n]:
                r.fail(op, f"collision: {o} also sets {'.'.join(other)}")
                return True
        set_paths.setdefault(key, []).append((path, op))
        return False

    def compare(op, cur):
        frm, to = op.body.get("from"), op.body.get("to")
        if cur == frm or not strict:
            return True
        if cur == to:
            r.fail(op, f"already applied: the field already reads {short(to)}")
        else:
            r.fail(op, f"stale: expected {short(frm)}, found {short(cur)}")
        return False

    for op in ops:
        b = op.body
        idx = st.line_index()
        if op.kind == "add_form":
            doc = copy.deepcopy(b["form"])
            key = "form" if "form" in doc else "def"
            fdoc = doc.get(key) or {}
            fid = fdoc.get("id")
            if fid in st.forms:
                same = fdoc == tree.forms.get(fid, {}).get("doc")
                r.fail(op, "already applied: the form exists" if same else f"collision: form {fid} exists")
                continue
            clash = [l["id"] for l in fdoc.get("lines") or [] if l["id"] in idx]
            if clash:
                r.fail(op, f"collision: line(s) {', '.join(clash)} exist")
                continue
            st.forms[fid] = {"key": key, "doc": fdoc, "lines": fdoc.setdefault("lines", []), "new": doc}
            for l in fdoc["lines"]:
                r.touched[l["id"]] = op
            continue
        if op.kind == "set_form":
            fid = op.entry["form"]
            if fid not in st.forms:
                r.fail(op, f"gone: form {fid} does not exist")
                continue
            path = str(b["field"]).split(".")
            if path[0] == "lines" or overlaps(("form", fid), path, op):
                if path[0] == "lines":
                    r.fail(op, "malformed: lines are changed by line operations")
                continue
            if compare(op, get_path(st.forms[fid]["doc"], path)):
                set_path(st.forms[fid]["doc"], path, b["to"])
            continue
        if op.kind in ("add_question", "remove_question", "set_question"):
            inp = b["input"]
            at = st.bank_index(inp)
            if op.kind == "add_question":
                if at is not None:
                    r.fail(op, f"already applied: the bank has a question for {inp}")
                    continue
                anchor = b.get("like") or b.get("after")
                k = st.bank_index(anchor)
                if k is None:
                    r.fail(op, f"gone: no bank question for {anchor}{suggest(anchor, [q.get('input', '') for q in st.bank])}")
                    continue
                # `like` lends its place (the bank's order number, the profiles), never its wording
                entry = {"input": inp, **({"order": st.bank[k]["order"]} if b.get("like") and "order" in st.bank[k] else {})}
                entry.update(copy.deepcopy(b.get("entry") or {}))
                st.bank.insert(k + 1, entry)
                names = set(b.get("profiles") or []) | ({n for n, qs in st.profiles.items() if b.get("like") in qs}
                                                        if b.get("like") else set())
                for name in sorted(names):
                    if name not in st.profiles:
                        r.fail(op, f"gone: no profile {name}")
                        continue
                    qs = st.profiles[name]
                    qs.insert(qs.index(anchor) + 1 if anchor in qs else len(qs), inp)
                added_inputs[inp] = op
            elif op.kind == "remove_question":
                if at is None:
                    r.fail(op, f"gone: no bank question for {inp}")
                    continue
                del st.bank[at]
                for qs in st.profiles.values():
                    while inp in qs:
                        qs.remove(inp)
            else:
                if at is None:
                    r.fail(op, f"gone: no bank question for {inp}{suggest(inp, [q.get('input', '') for q in st.bank])}")
                    continue
                path = str(b["field"]).split(".")
                if path == ["input"] or overlaps(("question", inp), path, op):
                    continue
                if compare(op, get_path(st.bank[at], path)):
                    set_path(st.bank[at], path, b["to"])
            continue

        # line operations
        if op.kind == "add_line":
            line = copy.deepcopy(b["line"])
            lid = line.get("id")
            fid = op.entry["form"]
            if lid in idx:
                if lid in base_lines and tree_line(tree, lid) == line:
                    r.fail(op, "already applied: the line exists as written")
                else:
                    r.fail(op, f"collision: line {lid} exists" + (f" ({r.touched[lid]} adds it)" if lid in r.touched else ""))
                continue
            if lid in r.removed:
                r.fail(op, f"collision: {r.removed[lid]} removes {lid}")
                continue
            if fid not in st.forms:
                r.fail(op, f"gone: form {fid} does not exist")
                continue
            lines = st.forms[fid]["lines"]
            pos = next((i for i, l in enumerate(lines) if l["id"] == b["after"]), None)
            if pos is None:
                r.fail(op, f"gone: anchor {b['after']} is not a line of {fid}"
                           + suggest(b["after"], [l["id"] for l in lines]))
                continue
            lines.insert(pos + 1, line)
            r.touched[lid] = op
            continue
        lid = b["line"]
        if lid in r.removed:
            r.fail(op, f"collision: {r.removed[lid]} removes {lid}")
            continue
        if lid not in idx:
            r.fail(op, f"gone: line {lid} does not exist{suggest(lid, idx)}")
            continue
        fid, i = idx[lid]
        if op.kind == "remove_line":
            if lid in r.touched:
                r.fail(op, f"collision: {r.touched[lid]} adds or changes {lid}")
                continue
            del st.forms[fid]["lines"][i]
            r.removed[lid] = op
            continue
        path = str(b["field"]).split(".")
        if path[0] == "id":
            r.fail(op, "malformed: ids are kept (spec 4.3); a renamed line is a new line")
            continue
        if overlaps(("line", lid), path, op):
            continue
        line = st.forms[fid]["lines"][i]
        if compare(op, get_path(line, path)):
            set_path(line, path, b["to"])
            r.touched[lid] = op

    finish(tree, st, r, added_inputs)
    return r


def tree_line(tree, lid):
    for f in tree.forms.values():
        for l in f["doc"].get("lines") or []:
            if l["id"] == lid:
                return l
    return None


def finish(tree, st, r, added_inputs):
    """The checks over the tree the operations leave: references, gates, questions, parameters."""
    idx = st.line_index()
    prefixes = set(st.forms)
    lines = {lid: st.forms[f]["lines"][i] for lid, (f, i) in idx.items()}

    def line_like(s):
        m = REF.match(s)
        return m and m.group(1) in prefixes

    def norm(s):
        m = REF.match(s)
        return f"{m.group(1)}.{m.group(2)}" if m else s

    awaited = {}  # line id -> (entry, the change that is to add it)
    for op in r.ops:
        for a in op.entry.get("awaits") or []:
            awaited[a.get("line")] = (op.entry, a.get("change", "?"))
    for aid, (entry, change) in sorted(awaited.items()):
        if aid in lines:
            r.notes.append(f"{entry['file']} {entry['change']} awaits {aid}, which exists now: drop the awaits")
    for lid, op in r.touched.items():
        if lid not in lines:
            continue
        line = lines[lid]
        for ref in sorted(reads_of(line)):
            if line_like(ref) and norm(ref) not in lines and ref not in tree.params and norm(ref) not in r.removed:
                if norm(ref) in awaited and not r.adopting:
                    r.notes.append(f"{op}: {lid} reads {ref}, which {awaited[norm(ref)][1]} is to add (awaited; "
                                   "adoption refuses until it exists)")
                    continue
                r.fail(op, f"dangling: {lid} reads {ref}, which is not a line" + suggest(norm(ref), lines))
        for p in sorted(params_of(line.get("expr"))):
            if p not in tree.params:
                r.new_params.setdefault(p, []).append(op)
    gated = {lid: l["gated_by"] for lid, l in lines.items() if isinstance(l.get("gated_by"), str)}
    for lid, op in r.touched.items():
        if lid not in lines:
            continue
        for ref in reads_of(lines[lid]) - {lines[lid].get("gated_by")}:
            ref = norm(ref)
            if ref in gated and gated[ref] != lid:
                r.fail(op, f"gated read: {lid} reads {ref}, which only its gate {gated[ref]} may read")
    if r.removed:
        for lid, line in lines.items():
            for ref in reads_of(line):
                if norm(ref) in r.removed:
                    r.fail(r.removed[norm(ref)], f"dangling: {lid} still reads the removed {norm(ref)}")
        bank_inputs = {q.get("input") for q in st.bank}
        for rid, op in r.removed.items():
            if rid in bank_inputs:
                r.fail(op, f"question left: the bank still asks the removed input {rid} (remove_question)")
        for name, data in sorted(tree.others.items()):
            if name in st.profiles:
                data = {k: v for k, v in data["interview"].items() if k != "questions"}
                strings = all_strings(data) | set(st.profiles[name])
            else:
                strings = all_strings(data)
            for rid, op in r.removed.items():
                if rid in strings and rid not in bank_inputs:
                    r.fail(op, f"dangling: interview/{name} still names the removed {rid}")
    bank_inputs = {q.get("input") for q in st.bank}
    asked = {lid for lid, (f, _) in idx.items() if st.forms[f]["key"] == "form"}  # a definition's inputs are bound
    r.new_inputs = sorted(lid for lid in r.touched if lid in asked and is_input(lines[lid]) and lid not in base_inputs(tree))
    for lid, op in r.touched.items():
        if lid in asked and is_input(lines[lid]) and lid not in bank_inputs:
            r.fail(op, f"input without question: {lid} is an input with no bank question (add_question)")
    for inp, op in added_inputs.items():
        if inp not in lines or not is_input(lines[inp]):
            r.fail(op, f"question left: {inp} is not an input line once the operations are applied")
    places = {}
    for q in st.bank:
        if "seq" in q:
            places.setdefault((q.get("order"), q["seq"]), []).append(q.get("input"))
    for (order, seq), inputs in sorted(places.items(), key=str):
        for inp in inputs:
            if len(inputs) > 1 and inp in added_inputs:
                r.fail(added_inputs[inp], f"collision: question {inp} takes order {order} seq {seq}, the place of "
                                          f"{', '.join(i for i in inputs if i != inp)}")
    for lid, op in r.touched.items():
        if lid in lines and not is_input(lines[lid]) and lid in bank_inputs and lid in {
                l for l in base_inputs(tree)}:
            r.fail(op, f"question left: {lid} is no longer an input but the bank still asks it (remove_question)")


def base_inputs(tree):
    return {l["id"] for f in tree.forms.values() for l in f["doc"].get("lines") or [] if is_input(l)}


# ---------------------------------------------------------------- evidence

def check_evidence(entries, archive, r):
    """Each entry's evidence printed where it says; `final` only on final editions."""
    import citations as C
    for e in entries:
        label = f"{e['file']} {e['change']}"
        op = e["ops"][0] if e["ops"] else None
        if e["verified"] not in ("draft", "final"):
            r.fail(op, f"evidence: {label} has verified {e['verified']!r}; draft or final")
        if not e["evidence"]:
            r.fail(op, f"evidence: {label} cites no evidence")
            continue
        drafts = []
        for ev in e["evidence"]:
            doc, page, quote = ev.get("doc"), ev.get("page"), ev.get("quote")
            if doc not in archive.docs:
                r.fail(op, f"evidence: {label} cites {doc}, which the archive does not hold")
                continue
            drafts.append(bool(archive.docs[doc].get("draft")))
            parts = C.parts_of(quote or "")
            if not parts:
                r.fail(op, f"evidence: {label} quotes nothing from {doc}")
                continue
            layers = archive.pages(doc)
            if layers is None or page is None:
                whole = archive.whole(doc) or []
                if not any(all(q in t for q in parts) for t in whole):
                    r.fail(op, f"evidence: {label}: {short(quote, 90)} is not printed in {doc}")
                continue
            if not C.on_pages(layers, [int(page)], parts, spill=True):
                where = C.pages_with(layers, parts)
                r.fail(op, f"evidence: {label}: {short(quote, 90)} is not printed on {doc} p. {page}"
                           + (f" (printed on p. {', '.join(map(str, where))})" if where else ""))
        if e["verified"] == "final" and any(drafts):
            r.fail(op, f"evidence: {label} is marked final but cites a draft")
        if e["verified"] == "draft" and drafts and not any(drafts):
            r.notes.append(f"{label}: every document it cites is final now; verify it and mark it final")


# ---------------------------------------------------------------- the check

def check(year, against=None, quiet=False, adopting=False):
    """Apply changes/<year+1> to the year's tree (or the tree under `against`); print the result; return
    (status, result). `adopting`: awaited lines must exist."""
    import citations as C
    to = int(year) + 1
    directory = ypath("changes", to)
    entries, ops, problems = load_changes(directory)
    tree = year_tree(year, against)
    r = apply(tree, ops, adopting=adopting)
    for p in problems:
        r.fail(None, p)
    if entries:
        check_evidence(entries, C.Archive(to), r)
    where = f"{against}/" if against else ""
    rel_dir = directory.relative_to(ROOT)
    head = (f"year changes {to}: {len(entries)} entries, {len(ops)} operations in {rel_dir} "
            f"applied to {where}{Path(tree.forms_dir).relative_to(Path(against) if against else ROOT)}")
    if not quiet:
        print(head + (": all apply" if not r.failures else f": {len(r.failures)} failure(s)"))
        for op, msg in r.failures:
            print(f"  FAIL {op or rel_dir}: {msg}")
        if r.new_params:
            print(f"  note: parameters the operations read that {where}params/{year}.yaml does not define "
                  f"(the {to} parameters must): {', '.join(sorted(r.new_params))}")
        if getattr(r, "new_inputs", None):
            print(f"  note: new inputs, each needing a test-data default at adoption: {', '.join(r.new_inputs)}")
        drafts = sum(1 for e in entries if e["verified"] == "draft")
        if entries:
            print(f"  note: {drafts} of {len(entries)} entries rest on IRS drafts (verified: draft)")
        for n in r.notes:
            print(f"  note: {n}")
    return (1 if r.failures else 0), r


# ---------------------------------------------------------------- writing an adopted year

class Dumper(yaml.SafeDumper):
    pass


class IndentedDumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def dump(obj, indented):
    return yaml.dump(obj, Dumper=IndentedDumper if indented else Dumper, sort_keys=False, allow_unicode=True,
                     width=120, default_flow_style=False)


def indent_of(s):
    return len(s) - len(s.lstrip(" "))


def list_blocks(text, list_key, item_key):
    """(head, items, tail, item_indent, indented): the text of a block list `list_key:` whose items each start
    `- <item_key>: <id>`, split into its items' text blocks [(id, text)]; a comment or blank line belongs to the
    item before it."""
    lines = text.splitlines(True)
    k = next(i for i, l in enumerate(lines) if re.match(rf"^\s*{list_key}:\s*$", l))
    key_indent = indent_of(lines[k])
    first = next(i for i in range(k + 1, len(lines)) if lines[i].strip() and not lines[i].lstrip().startswith("#"))
    item_indent = indent_of(lines[first])
    start = re.compile(rf"^ {{{item_indent}}}- {item_key}: (.+?)\s*$")
    items, cur, cur_id, end = [], [], None, len(lines)
    head = "".join(lines[:first])
    for i in range(first, len(lines)):
        l = lines[i]
        m = start.match(l)
        if m:
            if cur_id is not None:
                items.append((cur_id, "".join(cur)))
            cur, cur_id = [l], m.group(1).strip("'\"")
            continue
        if l.strip() and not l.lstrip().startswith("#") and (
                indent_of(l) < item_indent or (indent_of(l) == item_indent and not l.lstrip().startswith("- "))):
            end = i
            break
        cur.append(l)
    if cur_id is not None:
        items.append((cur_id, "".join(cur)))
    return head, items, "".join(lines[end:]), item_indent, item_indent > key_indent


def item_text(obj, indent, indented):
    s = dump([obj], indented)
    return "".join((" " * indent + l) if l.strip() else l for l in s.splitlines(True))


def rewrite_list(text, list_key, item_key, final, changed):
    """`text` with its list rebuilt in the order of `final` (the items as data): an item not in `changed` keeps its
    text block, a changed or new one is dumped in the file's style."""
    head, items, tail, ind, indented = list_blocks(text, list_key, item_key)
    blocks = dict(items)
    out = []
    for obj in final:
        key = obj[item_key]
        if key in blocks and key not in changed:
            out.append(blocks[key])
        else:
            trailing = re.search(r"(\n(?:[ \t]*#.*\n|[ \t]*\n)*)$", blocks.get(key, "\n")).group(1)
            out.append(item_text(obj, ind, indented).rstrip("\n") + trailing if key in blocks else item_text(obj, ind, indented))
    return head + "".join(out) + tail


def rewrite_key(text, owner_key, key, value):
    """`text` with the mapping key `key` under the top-level `owner_key:` replaced by `value` (None removes it)."""
    lines = text.splitlines(True)
    o = next(i for i, l in enumerate(lines) if re.match(rf"^{owner_key}:\s*$", l))
    ind = next(indent_of(l) for l in lines[o + 1:] if l.strip() and not l.lstrip().startswith("#"))
    pat = re.compile(rf"^ {{{ind}}}{re.escape(key)}:")
    at = next((i for i in range(o + 1, len(lines)) if pat.match(lines[i])), None)
    new = "" if value is None else "".join(" " * ind + l for l in dump({key: value}, False).splitlines(True))
    if at is None:
        lk = next(i for i in range(o + 1, len(lines)) if re.match(rf"^ {{{ind}}}lines:", lines[i]))
        return "".join(lines[:lk]) + new + "".join(lines[lk:])
    end = next((i for i in range(at + 1, len(lines)) if lines[i].strip() and indent_of(lines[i]) <= ind), len(lines))
    return "".join(lines[:at]) + new + "".join(lines[end:])


def rewrite_profile(text, final):
    """A profile's `questions:` list rebuilt in the order of `final`, keeping the text of every item line."""
    lines = text.splitlines(True)
    k = next(i for i, l in enumerate(lines) if re.match(r"^\s*questions:\s*$", l))
    item_re = re.compile(r"^(\s*)- (\S+)\s*$")
    i, items, ind = k + 1, {}, None
    while i < len(lines) and (not lines[i].strip() or lines[i].lstrip().startswith("#") or item_re.match(lines[i])):
        m = item_re.match(lines[i])
        if m:
            ind = m.group(1)
            items[m.group(2)] = lines[i]
        i += 1
    body = [items.get(q, f"{ind}- {q}\n") for q in final]
    kept = [l for l in lines[k + 1:i] if not item_re.match(l)]  # comments and blank lines move to the list's end
    return "".join(lines[:k + 1]) + "".join(body) + "".join(kept) + "".join(lines[i:])


def write(year, changes_year=None, root=None):
    """Apply changes/<changes_year or year> to the files of `year` (an adopted copy) under `root` (this checkout by
    default), editing only the blocks the operations touch. Returns the result of the apply."""
    cy = changes_year or year
    entries, ops, problems = load_changes(ypath("changes", cy) if root is None else
                                          Path(root) / ypath("changes", cy).relative_to(ROOT))
    if problems:
        raise SystemExit("year changes: " + "; ".join(problems))
    tree = year_tree(year, root)
    r = apply(tree, ops, strict=False)
    if r.failures:
        raise SystemExit("year changes: cannot apply to the copied year: "
                         + "; ".join(f"{op}: {m}" for op, m in r.failures))
    write_state(tree, r)
    return r


def write_state(tree, r):
    st = r.state
    changed_lines = set(r.touched)
    for fid, f in st.forms.items():
        if "new" in f:
            path = tree.forms_dir / f"{fid}.yaml"
            path.write_text(dump(f["new"], False), encoding="utf-8")
            continue
        orig = tree.forms[fid]
        text = orig["text"]
        old_meta = {k: v for k, v in orig["doc"].items() if k != "lines"}
        new_meta = {k: v for k, v in f["doc"].items() if k != "lines"}
        for k in list(old_meta) + [k for k in new_meta if k not in old_meta]:
            if old_meta.get(k) != new_meta.get(k):
                text = rewrite_key(text, orig["key"], k, new_meta.get(k))
        old_ids = [l["id"] for l in orig["doc"].get("lines") or []]
        new_ids = [l["id"] for l in f["lines"]]
        mine = changed_lines & set(new_ids)
        if old_ids != new_ids or mine:
            text = rewrite_list(text, "lines", "id", f["lines"], mine)
        if text != orig["text"]:
            orig["path"].write_text(text, encoding="utf-8")
    old_bank = tree.bank.get("questions") or []
    if st.bank != old_bank:
        old = {q.get("input"): q for q in old_bank}
        changed = {q.get("input") for q in st.bank if old.get(q.get("input")) != q}
        tree.bank_path.write_text(rewrite_list(tree.bank_text, "questions", "input", st.bank, changed), encoding="utf-8")
    for name, p in tree.profiles.items():
        if st.profiles[name] != p["data"]["interview"]["questions"]:
            p["path"].write_text(rewrite_profile(p["text"], st.profiles[name]), encoding="utf-8")


# ---------------------------------------------------------------- recording operations from an edited copy

def record(year, edited):
    """The operations that turn forms/<year>/<form>.yaml into `edited` (a copy of it with the next year's changes),
    as a changes-file entry to complete with evidence."""
    data = load_yaml(Path(edited).read_text(encoding="utf-8"))
    key = "form" if "form" in data else "def"
    new = data[key]
    tree = year_tree(year)
    if new["id"] not in tree.forms:
        return {"changes": {"tax_year": int(year) + 1, "form": new["id"], "entries": [
            {"change": "?", "evidence": [], "verified": "draft", "operations": [{"add_form": {"form": data}}]}]}}
    return {"changes": {"tax_year": int(year) + 1, "form": new["id"], "entries": [
        {"change": "?", "evidence": [], "verified": "draft",
         "operations": diff_ops(tree.forms[new["id"]]["doc"], new)}]}}


def diff_ops(old, new):
    ops = []
    for k in [k for k in new if k != "lines"] + [k for k in old if k not in new and k != "lines"]:
        if k not in ("tax_year",) and old.get(k) != new.get(k):
            ops.append({"set_form": {"field": k, "from": old.get(k), "to": new.get(k)}})
    a = {l["id"]: l for l in old.get("lines") or []}
    b = {l["id"]: l for l in new.get("lines") or []}
    order = [l["id"] for l in new.get("lines") or []]
    for lid in [l["id"] for l in old.get("lines") or []]:
        if lid not in b:
            ops.append({"remove_line": {"line": lid}})
    for i, lid in enumerate(order):
        if lid not in a:
            ops.append({"add_line": {"after": order[i - 1] if i else None, "line": b[lid]}})
            continue
        for field in [f for f in b[lid] if f != "id"] + [f for f in a[lid] if f not in b[lid]]:
            x, y = a[lid].get(field), b[lid].get(field)
            if x == y:
                continue
            if isinstance(x, dict) and isinstance(y, dict) and x.get("op") == y.get("op"):
                for sub in [s for s in y] + [s for s in x if s not in y]:
                    if x.get(sub) != y.get(sub):
                        ops.append({"set": {"line": lid, "field": f"{field}.{sub}", "from": x.get(sub), "to": y.get(sub)}})
            else:
                ops.append({"set": {"line": lid, "field": field, "from": x, "to": y}})
    return ops


# ---------------------------------------------------------------- self-test

SELF_FORMS = {
    "fa": """form:
  id: fa
  kind: form
  title: Form A
  tax_year: 2025
  lines:
    - id: fa.wages
      printed: "1"
      label: Wages
      type: Dollars
      expr:
        op: input
        source: Wages
      cite:
        doc: fx
        locator: p. 2, Line 1
    # a comment kept with the line before it
    - id: fa.flag
      printed: (helper)
      label: Any flag?
      type: Bool
      expr:
        op: input
        source: Any flag?
      cite:
        doc: fx
        locator: p. 2, Line 1
      gated_by: fa.flag_if
    - id: fa.flag_if
      printed: (gate)
      label: The flag, when wages are positive
      type: Bool
      expr:
        op: choose
        alternatives:
          - guard: {op: test, gt: [fa.wages, {const: 0}]}
            then: fa.flag
          - guard: {op: test, le: [fa.wages, {const: 0}]}
            then: fa.no
      cite:
        doc: fx
        locator: p. 2, Line 1
    - id: fa.no
      printed: (helper)
      label: No
      type: Bool
      expr:
        op: param
        ref: fa.false
      cite:
        doc: fx
        locator: p. 2, Line 1
    - id: fa.line2
      printed: "2"
      label: Add line 1 and the bonus
      type: Dollars
      expr:
        op: sum
        of:
          - fa.wages
          - fa.bonus
      cite:
        doc: fx
        locator: p. 2, Line 2, "Add line 1 and the bonus"
    - id: fa.bonus
      printed: (helper)
      label: Bonus
      type: Dollars
      expr:
        op: input
        source: Bonus
      cite:
        doc: fx
        locator: p. 2, Line 2
""",
}
SELF_BANK = """bank:
  tax_year: 2025
  questions:
  - input: fa.wages
    order: 1
  - input: fa.flag
    order: 2
    help: Answer yes if flagged.
  - input: fa.bonus
    order: 3
"""
SELF_PROFILE = """interview:
  tax_year: 2025
  targets:
  - fa.line2
  questions:
  - fa.wages
  - fa.bonus
"""
SELF_PARAMS = "params:\n  tax_year: 2025\n  values:\n    fa.false: {type: Bool, value: false}\n"
SELF_PAGES = ["The draft you are looking for begins on the next page", "Line 1 Wages. Line 2 Add line 1 and the bonus.",
              "Line 3 Add lines 2 and 2b. Line 2b Tips."]
GOOD = """changes:
  tax_year: 2026
  form: fa
  entries:
  - change: C-1
    evidence:
    - {doc: fx, page: 3, quote: "Line 3 Add lines 2 and 2b"}
    verified: draft
    operations:
    - add_line:
        after: fa.line2
        line:
          id: fa.tips
          printed: 2b
          label: Tips
          type: Dollars
          expr: {op: input, source: Tips}
          cite: {doc: fx, locator: p. 3, Line 2b}
    - add_question: {input: fa.tips, like: fa.bonus, entry: {help: Tips you were paid.}}
    - set: {line: fa.line2, field: printed, from: "2", to: "3"}
    - set: {line: fa.line2, field: expr.of, from: [fa.wages, fa.bonus], to: [fa.wages, fa.bonus, fa.tips]}
    - set_question: {input: fa.flag, field: help, from: Answer yes if flagged., to: Answer yes if you are flagged.}
"""


def self_test():
    import citations as C
    status = 0

    def make(tmp, forms=None, bank=SELF_BANK, profile=SELF_PROFILE, changes=GOOD):
        tmp = Path(tmp)
        (tmp / "forms").mkdir(parents=True, exist_ok=True)
        (tmp / "interview").mkdir(exist_ok=True)
        (tmp / "changes").mkdir(exist_ok=True)
        (tmp / "sources").mkdir(exist_ok=True)
        for name, text in (forms or SELF_FORMS).items():
            (tmp / "forms" / f"{name}.yaml").write_text(text, encoding="utf-8")
        (tmp / "interview" / "questions.yaml").write_text(bank, encoding="utf-8")
        (tmp / "interview" / "basic.yaml").write_text(profile, encoding="utf-8")
        (tmp / "params.yaml").write_text(SELF_PARAMS, encoding="utf-8")
        for p in (tmp / "changes").glob("*.yaml"):
            p.unlink()
        if changes is not None:
            (tmp / "changes" / "fa.yaml").write_text(changes, encoding="utf-8")
        planted = tmp / "sources"  # the synthetic archive's one text layer, written for the evidence check
        (planted / "fx.txt").write_text("\f".join(SELF_PAGES), encoding="utf-8")
        (tmp / "sources" / "manifest.json").write_text(json.dumps({"documents": [
            {"id": "fx", "file": "fx.pdf", "text_file": "fx.txt", "draft": True}]}), encoding="utf-8")
        return Tree(tmp / "forms", tmp / "interview", tmp / "params.yaml")

    def run(tmp, adopting=False, **kw):
        tree = make(tmp, **kw)
        entries, ops, problems = load_changes(Path(tmp) / "changes")
        r = apply(tree, ops, adopting=adopting)
        for p in problems:
            r.fail(None, p)
        check_evidence(entries, C.Archive(sources=Path(tmp) / "sources"), r)
        return r, tree

    def expect(name, r, needle):
        nonlocal status
        hit = [m for _, m in r.failures if needle in m]
        ok = bool(hit) if needle else not r.failures
        status = status or (0 if ok else 1)
        got = "; ".join(f"{o}: {m}" for o, m in r.failures) or "none"
        print(f"year-changes self-test: {name}: " + ("as expected" if ok else f"WRONG (failures: {got})"))

    with tempfile.TemporaryDirectory() as tmp:
        r, tree = run(tmp)
        expect("the planted operations apply", r, None)
        F = SELF_FORMS["fa"]
        cases = [
            ("the line an operation sets is gone (renamed)", {"forms": {"fa": F.replace("fa.line2", "fa.line2x")}},
             "gone: line fa.line2 does not exist (closest: fa.line2x)"),
            ("the text an operation expects to replace has changed",
             {"forms": {"fa": F.replace('printed: "2"', 'printed: "2a"')}}, "stale: expected '2', found '2a'"),
            ("the change is already in the earlier year", {"forms": {"fa": F.replace('printed: "2"', 'printed: "3"')}},
             "already applied"),
            ("the anchor of a new line is gone", {"changes": GOOD.replace("after: fa.line2", "after: fa.line9")},
             "gone: anchor fa.line9"),
            ("a new line collides with an existing id", {"changes": GOOD.replace("id: fa.tips", "id: fa.bonus")},
             "collision: line fa.bonus exists"),
            ("two operations set the same field", {"changes": GOOD + "    - set: {line: fa.line2, field: expr, from: x, to: y}\n"},
             "collision"),
            ("an operation on a line another removes",
             {"changes": GOOD.replace("    - set: {line: fa.line2, field: printed",
                                      "    - remove_line: {line: fa.line2}\n    - set: {line: fa.line2, field: printed")},
             "collision"),
            ("a removed line still read", {"changes": GOOD + "    - remove_line: {line: fa.wages}\n"
                                           "    - remove_question: {input: fa.wages}\n"},
             "dangling: fa.line2 still reads the removed fa.wages"),
            ("a removed input still asked", {"changes": GOOD + "    - remove_line: {line: fa.bonus}\n"
                                             "    - set: {line: fa.line2, field: label, from: Add line 1 and the bonus, to: x}\n"},
             "question left"),
            ("a removed line still named by a profile", {"changes": GOOD + "    - remove_line: {line: fa.bonus}\n"
                                                        "    - remove_question: {input: fa.bonus}\n",
                                                        "profile": SELF_PROFILE.replace("- fa.line2", "- fa.bonus")},
             "dangling: interview/basic.yaml still names the removed fa.bonus"),
            ("a new line reads a line that does not exist",
             {"changes": GOOD.replace("to: [fa.wages, fa.bonus, fa.tips]", "to: [fa.wages, fa.bonus, fa.tipz]")},
             "dangling: fa.line2 reads fa.tipz"),
            ("a gated input read outside its gate",
             {"changes": GOOD.replace("to: [fa.wages, fa.bonus, fa.tips]", "to: [fa.wages, fa.flag, fa.tips]")},
             "gated read: fa.line2 reads fa.flag"),
            ("a new input with no question", {"changes": GOOD.replace(
                "    - add_question: {input: fa.tips, like: fa.bonus, entry: {help: Tips you were paid.}}\n", "")},
             "input without question: fa.tips"),
            ("a question whose anchor is gone", {"changes": GOOD.replace("like: fa.bonus", "like: fa.bonuz")},
             "gone: no bank question for fa.bonuz"),
            ("a bank text an operation expects has changed", {"bank": SELF_BANK.replace("if flagged.", "if marked.")},
             "stale"),
            ("evidence not printed on its page", {"changes": GOOD.replace("page: 3", "page: 2")},
             "is not printed on fx p. 2 (printed on p. 3)"),
            ("evidence from a document not archived", {"changes": GOOD.replace("{doc: fx, page: 3", "{doc: fy, page: 3")},
             "the archive does not hold"),
            ("evidence marked final on a draft", {"changes": GOOD.replace("verified: draft", "verified: final")},
             "marked final but cites a draft"),
            ("a malformed operation", {"changes": GOOD + "    - rename: {line: fa.line2}\n"}, "malformed"),
            ("a new question takes another's place in its topic",
             {"bank": SELF_BANK.replace("    order: 3\n", "    order: 3\n    seq: 1\n"),
              "changes": GOOD.replace("entry: {help: Tips you were paid.}", "entry: {help: Tips you were paid., seq: 1}")},
             "collision: question fa.tips takes order 3 seq 1, the place of fa.bonus"),
        ]
        for name, kw, needle in cases:
            r, _ = run(tmp, **kw)
            expect(name, r, needle)
        # A line another change is to add, declared as awaited: a note while preparing, a failure at adoption.
        awaiting = GOOD.replace("to: [fa.wages, fa.bonus, fa.tips]", "to: [fa.wages, fa.bonus, fa.tips, fa.later]")
        awaiting = awaiting.replace("    verified: draft\n", "    verified: draft\n    awaits:\n    - {line: fa.later, change: C-2}\n")
        r, _ = run(tmp, changes=awaiting)
        ok = not r.failures and any("fa.later, which C-2 is to add" in n for n in r.notes)
        status = status or (0 if ok else 1)
        print("year-changes self-test: an awaited line read while preparing: " + ("a note, as expected" if ok else "WRONG"))
        r, _ = run(tmp, changes=awaiting, adopting=True)
        expect("an awaited line still missing at adoption", r, "dangling: fa.line2 reads fa.later")

        # Writing: the files edited block by block equal the data applied in memory, and every untouched line
        # block keeps its text.
        r, tree = run(tmp)
        before = {p.name: p.read_text() for p in (Path(tmp) / "forms").glob("*.yaml")}
        bank_before = (Path(tmp) / "interview" / "questions.yaml").read_text()
        write_state(tree, r)
        after = Tree(Path(tmp) / "forms", Path(tmp) / "interview", Path(tmp) / "params.yaml")
        same = (after.forms["fa"]["doc"]["lines"] == r.state.forms["fa"]["lines"]
                and after.bank["questions"] == r.state.bank
                and after.profiles["basic.yaml"]["data"]["interview"]["questions"] == r.state.profiles["basic.yaml"])
        _, old_items, _, _, _ = list_blocks(before["fa.yaml"], "lines", "id")
        _, new_items, _, _, _ = list_blocks(after.forms["fa"]["text"], "lines", "id")
        new_items = dict(new_items)
        kept = all(new_items.get(i) == t for i, t in old_items if i not in r.touched)
        _, old_q, _, _, _ = list_blocks(bank_before, "questions", "input")
        _, new_q, _, _, _ = list_blocks(after.bank_text, "questions", "input")
        kept_q = all(dict(new_q).get(i) == t for i, t in old_q if i != "fa.flag")
        styled = "        of:\n          - fa.wages\n          - fa.bonus\n          - fa.tips\n" in after.forms["fa"]["text"]
        ok = same and kept and kept_q and styled and "# a comment kept" in after.forms["fa"]["text"]
        status = status or (0 if ok else 1)
        print("year-changes self-test: written files equal the applied data, untouched blocks byte-for-byte: "
              + ("as expected" if ok else f"WRONG (data {same}, lines kept {kept}, questions kept {kept_q})"))
        # Recording: the operations recorded from an edited copy reproduce it.
        tree = make(tmp)
        edited = copy.deepcopy(tree.forms["fa"]["doc"])
        edited["lines"][4]["printed"] = "3"
        edited["lines"].insert(5, {"id": "fa.new", "printed": "(helper)", "label": "x", "type": "Dollars",
                                   "expr": {"op": "copy", "from": "fa.line2"}, "cite": {"doc": "fx", "locator": "p. 3"}})
        del edited["lines"][6]
        ops = [Op("r", "?", n, next(iter(o)), next(iter(o.values())), {"form": "fa"})
               for n, o in enumerate(diff_ops(tree.forms["fa"]["doc"], edited), 1)]
        st = apply(tree, ops).state
        ok = st.forms["fa"]["lines"] == edited["lines"]
        status = status or (0 if ok else 1)
        print("year-changes self-test: operations recorded from an edited copy reproduce it: "
              + ("as expected" if ok else "WRONG"))
    return status


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--against", help="a checkout or export whose forms/, interview/ and params/ to check instead")
    ap.add_argument("--record", metavar="EDITED_YAML")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        sys.exit(self_test())
    if a.record:
        sys.stdout.write(dump(record(taxyear.Y, a.record), False))
        return
    if a.check:
        sys.exit(check(taxyear.Y, a.against)[0])
    ap.error("one of --check, --record, --self-test")


if __name__ == "__main__":
    main()
