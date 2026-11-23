#!/usr/bin/env python3
"""Year changes as operations keyed by line id.

The operations that take one tax year's definitions to the next are data in changes/<year>/<form>.yaml
(changes/ny/<year>/ for New York): per form, a list of entries, each a change of the change map with its
evidence (archived document, page, quote printed there; draft or verified against a final edition) and its
operations on line ids:

    add_line {after, line}            set {line, field, from, to}        add_form {form}
    remove_line {line}                set_form {field, from, to}
    add_question {input, like | after, entry, profiles, default, reason}
    remove_question {input}           set_question {input, field, from, to}
    add_ambiguity {entry, after?}     set_ambiguity {id, field, from, to}   remove_ambiguity {id}
    set_interview {file, field, from, to, list?, item?}                   add_interview_file {file, data}
    add_interview_item {file, list, item, after?}   remove_interview_item {file, list, item}   remove_interview_file {file}

`field` is a path of mapping keys (`printed`, `expr.take`, `cite.locator`); `from: null` means absent and
`to: null` removes the field. `add_question` places the new bank entry after `like` or `after`; `like` also lends
its order number and its place in every profile, never its wording; a question for an input line carries the input's
test-data `default` and its one-line `reason`, which fixtures_year.py writes to fixtures/<year>/defaults.json. The
ambiguity operations act on the register (ambiguities/<year>.yaml) by entry id; after them every line's `ambiguity`
must name an entry, and an added entry must be linked by a line or say why not (`unlinked`). The interview operations
act on the other files of interview/<year>/ (profiles' targets, coverage rows and sets, personas, gate frequencies,
the bank's groups) by file and path: `list` is a path to a list, whose `item` is an entry's id or a plain value. An entry may list lines it `awaits`
({line, change}): lines another change, not yet written as operations, is to add; reading one is reported, not
failed, until adoption, which refuses while one is missing. An entry's `note` is free text. The operations of year N+1 are applied, in memory, to the forms, question bank and
profiles of year N; an operation fails, named with its file, change, position, kind and line, when its line, form
or anchor is gone, the value it expects to replace has changed (stale), it is already applied, it collides with
another operation, it leaves a reference dangling or a gated input read outside its gate, a new input has no
question or a question outlives its input, or its evidence is not printed where it says.

    year_changes.py [--year N] --check [--no-static]   apply changes/<N+1> to the year-N tree; exit 1 on a failure;
                                                       when they apply, run the engine's static checks
                                                       (engine/src/check.ts, `main.js check`) on the tree they
                                                       produce, with the staged parameters and tables of
                                                       research/ty<N+1>/ (static_check)
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

KINDS = ("add_line", "remove_line", "set", "add_form", "set_form", "add_question", "remove_question", "set_question",
         "add_ambiguity", "set_ambiguity", "remove_ambiguity")
REQUIRED = {"add_line": ("after", "line"), "remove_line": ("line",), "set": ("line", "field", "from", "to"),
            "add_form": ("form",), "set_form": ("field", "from", "to"), "add_question": ("input",),
            "remove_question": ("input",), "set_question": ("input", "field", "from", "to"),
            "add_ambiguity": ("entry",), "set_ambiguity": ("id", "field", "from", "to"), "remove_ambiguity": ("id",)}
AMB_KINDS = ("add_ambiguity", "set_ambiguity", "remove_ambiguity")
IV_KINDS = ("set_interview", "add_interview_item", "remove_interview_item", "add_interview_file", "remove_interview_file")
KINDS += IV_KINDS
REQUIRED.update({"set_interview": ("file", "field", "from", "to"), "add_interview_item": ("file", "list", "item"),
                 "remove_interview_item": ("file", "list", "item"), "add_interview_file": ("file", "data"),
                 "remove_interview_file": ("file",)})
BANK_FILE = "questions.yaml"
REGISTER_REQUIRED = ("id", "text_at_issue", "readings", "chosen", "reason", "cite")  # schema/data.schema.json registerEntry
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

    def __init__(self, forms_dir, interview_dir, params_file, register_file=None):
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
        self.profiles, self.others, self.other_texts = {}, {}, {}
        for p in sorted(self.interview_dir.rglob("*.yaml")) if self.interview_dir.is_dir() else []:
            if p == self.bank_path:
                continue
            text = p.read_text(encoding="utf-8")
            data = load_yaml(text)
            iv = data.get("interview") if isinstance(data, dict) else None
            if isinstance(iv, dict) and isinstance(iv.get("questions"), list):
                self.profiles[p.relative_to(self.interview_dir).as_posix()] = {"path": p, "text": text, "data": data}
            self.others[p.relative_to(self.interview_dir).as_posix()] = data
            self.other_texts[p.relative_to(self.interview_dir).as_posix()] = text
        params = load_yaml(Path(params_file).read_text(encoding="utf-8")) if Path(params_file).exists() else {}
        self.params = set(((params or {}).get("params") or {}).get("values") or {})
        self.enums = {k: (v or {}).get("values") or [] for k, v in (((params or {}).get("params") or {}).get("enums") or {}).items()}
        self.register_path = Path(register_file) if register_file else None
        self.register_text = self.register_path.read_text(encoding="utf-8") if self.register_path and self.register_path.exists() else ""
        self.register = ((load_yaml(self.register_text) or {}).get("register") or {}).get("entries") or [] if self.register_text else []


def year_tree(year, root=None):
    """The tree of `year` in this checkout, or in the checkout or export at `root`."""
    if root is None:
        return Tree(ypath("forms", year), jurisdiction.interview_dir(year), jurisdiction.params_file(year),
                    jurisdiction.register_file(year))
    root = Path(root)
    rel = lambda p: root / Path(p).relative_to(ROOT)  # noqa: E731
    return Tree(rel(ypath("forms", year)), rel(jurisdiction.interview_dir(year)), rel(jurisdiction.params_file(year)),
                rel(jurisdiction.register_file(year)))


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
        if self.kind in ("set", "set_question", "set_ambiguity"):
            return f"{b.get('line') or b.get('input') or b.get('id')} {b.get('field')}"
        if self.kind == "add_ambiguity":
            return str((b.get("entry") or {}).get("id", "?"))
        if self.kind in IV_KINDS:
            item = b.get("item")
            item = item.get("id", "?") if isinstance(item, dict) else item
            return " ".join(str(x) for x in (b.get("file"), b.get("list"), item, b.get("field")) if x is not None)
        return str(b.get("line") or b.get("input") or b.get("id"))

    def __str__(self):
        return f"{self.file} {self.change} op {self.n} ({self.kind} {self.target})"


def load_changes(directory):
    """(entries, ops, problems): every entry of every file of a changes directory, in file order: by the form part of
    the name, a form's own file `<form>.yaml` before its split files `<form>.<topic>.yaml` (sorted), so a split file
    may build on what the form's own file adds. A file's form is its `form:` field, not its name."""
    entries, ops, problems = [], [], []
    directory = Path(directory)
    files = sorted(directory.glob("*.yaml"), key=lambda p: (p.name.split(".")[0], p.name.count(".") > 1, p.name)) \
        if directory.is_dir() else []
    for p in files:
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
                if op.kind == "add_ambiguity" and isinstance(op.body.get("entry"), dict):
                    missing += [f"entry.{f}" for f in REGISTER_REQUIRED if f not in op.body["entry"]]
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
        self.register = copy.deepcopy(tree.register)
        self.others = copy.deepcopy(tree.others)  # every interview file but the bank, by its path under interview/<year>
        self.bank_meta = {k: copy.deepcopy(v) for k, v in tree.bank.items() if k != "questions"}

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

    def register_index(self, aid):
        return next((i for i, e in enumerate(self.register) if e.get("id") == aid), None)


class Result:
    def __init__(self):
        self.failures = []  # (op or None, message)
        self.notes = []
        self.state = None
        self.touched = {}  # line id -> the last op that added or changed it
        self.removed = {}  # line id -> the op that removed it
        self.new_params = {}  # parameter id -> [op]
        self.amb_touched = {}  # register id -> the last op that added or changed it
        self.amb_removed = {}  # register id -> the op that removed it
        self.iv_touched = {}  # interview file -> [(op, path of keys and "#item" steps)]
        self.iv_removed_names = {}  # (file, an item id or mapping key removed) -> op

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
        if op.kind in AMB_KINDS:
            apply_ambiguity(op, st, r, tree, overlaps, compare)
            continue
        if op.kind in IV_KINDS:
            apply_interview(op, st, r, overlaps, compare)
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


def apply_ambiguity(op, st, r, tree, overlaps, compare):
    """An operation on the ambiguity register, keyed by entry id."""
    b = op.body
    aid = (b.get("entry") or {}).get("id") if op.kind == "add_ambiguity" else b.get("id")
    if aid in r.amb_removed:
        r.fail(op, f"collision: {r.amb_removed[aid]} removes {aid}")
        return
    at = st.register_index(aid)
    if op.kind == "add_ambiguity":
        if at is not None:
            same = any(e == b["entry"] for e in tree.register)
            r.fail(op, "already applied: the register has the entry as written" if same
                   else f"collision: the register has an entry {aid}"
                   + (f" ({r.amb_touched[aid]} adds it)" if aid in r.amb_touched else ""))
            return
        entry = copy.deepcopy(b["entry"])
        if b.get("after") is not None:
            k = st.register_index(b["after"])
            if k is None:
                r.fail(op, f"gone: anchor {b['after']} is not a register entry"
                           + suggest(b["after"], [e.get("id", "") for e in st.register]))
                return
            st.register.insert(k + 1, entry)
        else:
            st.register.append(entry)
        r.amb_touched[aid] = op
        return
    if at is None:
        r.fail(op, f"gone: no register entry {aid}{suggest(aid, [e.get('id', '') for e in st.register])}")
        return
    if op.kind == "remove_ambiguity":
        if aid in r.amb_touched:
            r.fail(op, f"collision: {r.amb_touched[aid]} adds or changes {aid}")
            return
        del st.register[at]
        r.amb_removed[aid] = op
        return
    path = str(b["field"]).split(".")
    if path[0] == "id":
        r.fail(op, "malformed: register ids are kept; a new reading is a new entry (add_ambiguity)")
        return
    if overlaps(("ambiguity", aid), path, op):
        return
    if compare(op, get_path(st.register[at], path)):
        set_path(st.register[at], path, b["to"])
        r.amb_touched[aid] = op


def item_key(x):
    return x.get("id") if isinstance(x, dict) else x


def apply_interview(op, st, r, overlaps, compare):
    """An operation on an interview file other than through the question operations, by file and path."""
    b = op.body
    name = str(b["file"])
    if op.kind == "add_interview_file":
        if name in st.others or name == BANK_FILE:
            r.fail(op, "already applied: the file exists as written" if st.others.get(name) == b["data"]
                   else f"collision: interview/{name} exists")
            return
        if overlaps(("interview", name), [], op):
            return
        st.others[name] = copy.deepcopy(b["data"])
        r.iv_touched.setdefault(name, []).append((op, []))
        return
    if name == BANK_FILE:
        data = {"bank": st.bank_meta}
    elif name in st.others:
        data = st.others[name]
    else:
        r.fail(op, f"gone: no interview file {name}" + suggest(name, list(st.others) + [BANK_FILE]))
        return
    if op.kind == "remove_interview_file":
        if name == BANK_FILE or name in st.profiles:
            r.fail(op, "malformed: the bank and the profiles are not removed by an operation")
            return
        if overlaps(("interview", name), [], op):
            return
        del st.others[name]
        r.iv_touched.setdefault(name, []).append((op, []))
        return
    lpath = str(b["list"]).split(".") if b.get("list") is not None else []
    guarded = ["bank", "questions"] if name == BANK_FILE else (["interview", "questions"] if name in st.profiles else None)
    if guarded and (lpath or str(b.get("field", "")).split("."))[:2] == guarded:
        r.fail(op, "malformed: questions are changed by the question operations")
        return
    if op.kind == "set_interview" and "item" not in b:
        path = str(b["field"]).split(".")
        if overlaps(("interview", name), path, op):
            return
        if compare(op, get_path(data, path)):
            set_path(data, path, b["to"])
            r.iv_touched.setdefault(name, []).append((op, path))
            if b["to"] is None:
                r.iv_removed_names[(name, path[-1])] = op
        return
    seq = get_path(data, lpath)
    if not isinstance(seq, list):
        r.fail(op, f"gone: interview/{name} has no list {b.get('list')}")
        return
    want = item_key(b["item"])
    at = next((i for i, x in enumerate(seq) if item_key(x) == want), None)
    step = lpath + [f"#{want}"]
    if op.kind == "add_interview_item":
        if at is not None:
            r.fail(op, "already applied: the item exists as written" if seq[at] == b["item"]
                   else f"collision: {b['list']} of interview/{name} has an item {want}")
            return
        if overlaps(("interview", name), step, op):
            return
        k = len(seq) - 1
        if b.get("after") is not None:
            k = next((i for i, x in enumerate(seq) if item_key(x) == b["after"]), None)
            if k is None:
                r.fail(op, f"gone: anchor {b['after']} is not an item of {b['list']} in interview/{name}")
                return
        seq.insert(k + 1, copy.deepcopy(b["item"]))
        r.iv_touched.setdefault(name, []).append((op, step))
        return
    if at is None:
        r.fail(op, f"gone: {b['list']} of interview/{name} has no item {want}"
                   + suggest(str(want), [str(item_key(x)) for x in seq]))
        return
    if op.kind == "remove_interview_item":
        if overlaps(("interview", name), step, op):
            return
        if isinstance(seq[at], dict):  # an entry with an id: what still names the id dangles
            r.iv_removed_names[(name, want)] = op
        del seq[at]
        r.iv_touched.setdefault(name, []).append((op, step))
        return
    path = str(b["field"]).split(".")
    if not isinstance(seq[at], dict) or path[0] == "id":
        r.fail(op, "malformed: set_interview with an item sets a field of an entry with an id, never the id")
        return
    if overlaps(("interview", name), step + path, op):
        return
    if compare(op, get_path(seq[at], path)):
        set_path(seq[at], path, b["to"])
        r.iv_touched.setdefault(name, []).append((op, step + path))


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
        for name, strings in interview_strings(st):
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
    for inp, op in added_inputs.items():
        if inp in lines and inp in asked and is_input(lines[inp]):
            for msg in default_problems(lines[inp], op.body, tree):
                r.fail(op, f"default: {inp} {msg}")
    finish_register(tree, st, r, lines)
    finish_interview(tree, st, r, lines, line_like, norm)


def interview_strings(st):
    """(file, every string it holds) of each interview file as the operations leave it; a profile's questions are
    its list in the state."""
    for name, data in sorted(st.others.items()):
        if name in st.profiles:
            data = {k: v for k, v in data["interview"].items() if k != "questions"}
            yield name, all_strings(data) | set(st.profiles[name])
        else:
            yield name, all_strings(data)
    yield BANK_FILE, all_strings(st.bank_meta)


def values_of(node, out=None):
    """The strings of a node that are values, not mapping keys."""
    out = set() if out is None else out
    if isinstance(node, str):
        out.add(node)
    elif isinstance(node, list):
        for v in node:
            values_of(v, out)
    elif isinstance(node, dict):
        for v in node.values():
            values_of(v, out)
    return out


def finish_interview(tree, st, r, lines, line_like, norm):
    """The interview files the operations leave: what an interview operation writes names lines that exist; an item
    or key it removes is not still named in its file; every tick-box group of the bank is named by a question and
    every question's group is declared (engine/src/tick-groups.ts)."""
    for name, touched in sorted(r.iv_touched.items()):
        for op, path in touched:
            new = op.body.get("to") if op.kind == "set_interview" else op.body.get("item", op.body.get("data"))
            if op.kind in ("remove_interview_item", "remove_interview_file"):
                continue
            for s in sorted(all_strings(new)):
                if line_like(s) and norm(s) not in lines and s not in tree.params and norm(s) not in r.removed:
                    r.fail(op, f"dangling: interview/{name} would name {s}, which is not a line" + suggest(norm(s), lines))
    named = {}
    for name, data in st.others.items():
        named[name] = values_of(data)
    for (name, gone), op in sorted(r.iv_removed_names.items(), key=str):
        if name in named and gone in named[name]:
            r.fail(op, f"dangling: interview/{name} still names {gone}, which {op} removes")
    declared = [g.get("id") for g in st.bank_meta.get("groups") or [] if isinstance(g, dict)]
    members = {q.get("group") for q in st.bank if q.get("group")}
    base_members = {}
    for q in tree.bank.get("questions") or []:
        if q.get("group"):
            base_members.setdefault(q["group"], []).append(q.get("input"))
    removing = {op.body["input"]: op for op in r.ops if op.kind == "remove_question"}
    for g in declared:
        if g not in members:
            op = next((removing[i] for i in base_members.get(g, []) if i in removing), None)
            r.fail(op, f"group left: tick-box group {g} of the bank: no question names it (remove_interview_item "
                       "{file: questions.yaml, list: bank.groups})")
    for q in st.bank:
        if q.get("group") and q["group"] not in declared:
            op = r.iv_removed_names.get((BANK_FILE, q["group"]))
            r.fail(op, f"dangling: question {q.get('input')} names the tick-box group {q['group']}, which the bank "
                       "does not declare")


def default_problems(line, body, tree):
    """A new input's test-data default as add_question states it (engine/src/fixture-inputs.ts defaultsProblems):
    a value the input accepts and a one-line reason."""
    if "default" not in body or "reason" not in body:
        return ["has no test-data default (add_question: default and reason, for fixtures/<year>/defaults.json)"]
    v, reason, t = body["default"], body["reason"], str(line.get("type", ""))
    out = []
    if not isinstance(reason, str) or not reason.strip() or "\n" in reason.strip():
        out.append("needs a one-line reason for its default")
    if t == "Bool":
        ok = isinstance(v, bool)
    elif t.startswith("Enum("):
        ok = isinstance(v, str) and v in tree.enums.get(t[5:-1], [v])  # an enum the from-year lacks: the parameter lane's
    else:
        ok = isinstance(v, int) and not isinstance(v, bool) and (t == "Dollars" or v >= 0)
    if not ok:
        out.append(f"default {short(v)} is not a value of {t}")
    return out


def finish_register(tree, st, r, lines):
    """The register the operations leave: every line's ambiguity names an entry; an added entry is linked or says why
    not; an entry whose last linking line goes is removed or says why it stands unlinked (engine/src/check.ts)."""
    if tree.register_path is None or not tree.register_path.exists():
        return
    ids = {e.get("id"): e for e in st.register}
    linked = {}
    for lid, line in lines.items():
        if isinstance(line.get("ambiguity"), str):
            linked.setdefault(line["ambiguity"], []).append(lid)
    for aid, lids in sorted(linked.items()):
        if aid in ids:
            continue
        if aid in r.amb_removed:
            r.fail(r.amb_removed[aid], f"dangling: {', '.join(lids)} still links the removed ambiguity {aid}")
            continue
        for lid in lids:
            if lid in r.touched:
                r.fail(r.touched[lid], f"dangling: {lid} links the ambiguity {aid}, which the register does not hold "
                                       "(add_ambiguity)")
    for aid, op in r.amb_removed.items():
        for name, data in sorted(tree.others.items()):
            if aid in all_strings(data):
                r.fail(op, f"dangling: interview/{name} still names the removed ambiguity {aid}")
    base_linked = {}
    for f in tree.forms.values():
        for l in f["doc"].get("lines") or []:
            if isinstance(l.get("ambiguity"), str):
                base_linked.setdefault(l["ambiguity"], []).append(l["id"])
    for aid, e in ids.items():
        if aid in linked or (isinstance(e.get("unlinked"), str) and e["unlinked"].strip()):
            continue
        if aid in r.amb_touched and r.amb_touched[aid].kind == "add_ambiguity":
            r.fail(r.amb_touched[aid], f"unlinked: no line links the added ambiguity {aid} (link it with ambiguity:, "
                                       "or say why it stands unlinked in unlinked:)")
        elif aid in base_linked:
            op = next((r.removed.get(l) or r.touched.get(l) for l in base_linked[aid] if l in r.removed or l in r.touched), None)
            r.fail(op, f"unlinked: no line links {aid} once the operations apply (it was linked by "
                       f"{', '.join(base_linked[aid])}); remove_ambiguity, or set_ambiguity its unlinked reason")
    for aid, e in ids.items():
        if aid in linked and "unlinked" in e and aid in r.amb_touched:
            r.fail(r.amb_touched[aid], f"unlinked: {aid} carries an unlinked reason, but {', '.join(linked[aid])} links it")


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

def check(year, against=None, quiet=False, adopting=False, static=False):
    """Apply changes/<year+1> to the year's tree (or the tree under `against`); print the result; return
    (status, result). `adopting`: awaited lines must exist. `static`: when the operations apply, also run the
    engine's static checks on the tree they produce (static_check; federal, this checkout only)."""
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
    if r.state is not None:  # code and tool data kept for every year that name what goes
        import year_shared_refs
        refs = year_shared_refs.references(tree, r)
        if refs:
            r.notes.append(f"{len(refs)} reference(s) in {len({x[0] for x in refs})} year-shared file(s) (code and tool "
                           "data) name ids these operations remove or gates they retire: tools/year_shared_refs.py "
                           f"--year {year} lists them, as adoption does in {ypath('reports', to).relative_to(ROOT)}/")
    if static and r.state is not None and not r.failures and ops:
        if jurisdiction.NY or against:
            r.notes.append("static checks of the applied tree: run federally on this checkout only")
        else:
            errors, notes = static_check(year, r)
            static_findings(errors, to, adopting, r)
            r.notes += [f"static checks of the applied {to} tree: {n}" for n in notes]
            if not errors:
                r.notes.append(f"static checks of the applied {to} tree (engine/src/check.ts: references, cycles, "
                               "types, guard tiling, gates, citations, tables): pass")
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
            print(f"  note: new inputs (their add_question defaults go to fixtures/{to}/defaults.json at adoption, "
                  f"tools/fixtures_year.py): {', '.join(r.new_inputs)}")
        drafts = sum(1 for e in entries if e["verified"] == "draft")
        if entries:
            print(f"  note: {drafts} of {len(entries)} entries rest on IRS drafts (verified: draft)")
        for n in r.notes:
            print(f"  note: {n}")
    return (1 if r.failures else 0), r


# ---------------------------------------------------------------- static checks of the applied tree

# Fields of a staged parameter that record its preparation, not its value (dropped at adoption: docs/ty2026/ADOPTION.md).
STAGED_ONLY = ("source", "note", "derived", "new_in_2026", "unsourced", "retired")
NOT_ARCHIVED = "0" * 64  # the snapshot given to a citation of a document the new year's archive does not hold


def staged_params(year, to):
    """The parameters of the applied tree: params/<year>.yaml with the staged values of
    research/ty<to>/params-<to>.proposed.yaml laid over it (an entry's value, type and citation, its preparation
    fields dropped; an entry staged with no value keeps the year's), the enumerations it changes replaced, and the
    parameters it retires removed; params/<year>.yaml alone when nothing is staged."""
    base = load_yaml(Path(jurisdiction.params_file(year)).read_text(encoding="utf-8"))["params"]
    params = {"tax_year": int(to), "enums": copy.deepcopy(base.get("enums") or {}),
              "values": copy.deepcopy(base.get("values") or {})}
    staged_file = ROOT / "research" / f"ty{to}" / f"params-{to}.proposed.yaml"
    if jurisdiction.NY or not staged_file.exists():
        return params, None
    staged = load_yaml(staged_file.read_text(encoding="utf-8"))["params"]
    for name, entry in (staged.get("values") or {}).items():
        if entry.get("value") is None and name in params["values"]:
            continue  # no source for the new year yet: the year's value stands in
        params["values"][name] = {**params["values"].get(name, {}), **{k: v for k, v in entry.items() if k not in STAGED_ONLY}}
    for name in staged.get("retired") or {}:
        params["values"].pop(name, None)
    for name, entry in ((staged.get("enums") or {}).get("changed") or {}).items():
        params["enums"][name] = {k: v for k, v in entry.items() if k not in STAGED_ONLY}
    return params, staged_file


def staged_tables(year, to):
    """The tables of the applied tree: tables/<year>/ with the staged tables of research/ty<to>/tables-<to>/ in
    place of those of the same id."""
    tables = {}
    dirs = [ypath("tables", year)]
    staged_dir = ROOT / "research" / f"ty{to}" / f"tables-{to}"
    if not jurisdiction.NY and staged_dir.is_dir():
        dirs.append(staged_dir)
    for d in dirs:
        for p in sorted(Path(d).glob("*.yaml")):
            table = load_yaml(p.read_text(encoding="utf-8"))["table"]
            tables[table["id"]] = table
    return list(tables.values()), staged_dir if len(dirs) > 1 else None


def canonical_of(year, r):
    """The canonical data (engine/src/types.ts CanonicalData) of the tree the operations produce from `year`, as
    the build would make it for year+1, with three differences: the parameters and tables are the staged ones
    (staged_params, staged_tables), and a citation of a document the year+1 archive does not hold is given an
    all-zero snapshot and a revision saying so, since the build's snapshot check cannot apply to it yet. Returns
    (data, notes)."""
    to = int(year) + 1
    st = r.state
    archive = {}
    for d in jurisdiction.read_dirs("sources", to):
        path = Path(d) / "manifest.json"
        if path.exists():
            m = json.loads(path.read_text(encoding="utf-8"))
            archive.update({e["id"]: e for e in (m["documents"] if isinstance(m, dict) else m)})
    unarchived = set()

    def fill(cite):
        if not isinstance(cite, dict) or "doc" not in cite or "locator" not in cite:
            return cite
        entry = archive.get(cite["doc"])
        if entry is None:
            unarchived.add(cite["doc"])
        out = {"doc": cite["doc"], "tax_year": to, "locator": cite["locator"],
               "revision": (entry or {}).get("revision") or ("?" if entry else f"not archived for {to}"),
               "snapshot": entry["sha256"] if entry else NOT_ARCHIVED}
        if "quote" in cite:
            out["quote"] = cite["quote"]
        return out

    forms, defs = [], []
    for fid, f in sorted(st.forms.items()):
        doc = copy.deepcopy(f["doc"])
        doc["tax_year"] = to
        if (doc.get("collection") or {}).get("cite") is not None:
            doc["collection"]["cite"] = fill(doc["collection"]["cite"])
        for line in doc.get("lines") or []:
            line["cite"] = fill(line.get("cite"))
            for refusal in line.get("refuses") or []:
                refusal["cite"] = fill(refusal.get("cite"))
        (defs if f["key"] == "def" else forms).append(doc)
    params, staged_file = staged_params(year, to)
    for group in ("values", "enums"):
        for entry in params[group].values():
            if isinstance(entry, dict) and "cite" in entry:
                entry["cite"] = fill(entry["cite"])
    tables, staged_dir = staged_tables(year, to)
    for t in tables:
        t["cite"] = fill(t.get("cite"))
    register = {"tax_year": to, "entries": [{**copy.deepcopy(e), "cite": fill(e.get("cite"))} for e in st.register]}
    notes = []
    if staged_file:
        notes.append(f"parameters: {Path(jurisdiction.params_file(year)).relative_to(ROOT)} with the staged values of "
                     f"{staged_file.relative_to(ROOT)}")
    if staged_dir:
        notes.append(f"tables: {ypath('tables', year).relative_to(ROOT)} with the staged tables of {staged_dir.relative_to(ROOT)}")
    if unarchived:
        notes.append(f"{len(unarchived)} cited document(s) not archived for {to}, their snapshot check skipped: "
                     + ", ".join(sorted(unarchived)))
    return {"forms": forms, "defs": defs, "tables": tables, "params": params, "register": register}, notes


# engine/src/check.ts lineIdProblems: an id `.line<N>` that names another number than the line prints.
ID_DRIFT = re.compile(r"^\S+: the id names line \S+, but the line is printed ")


def static_findings(errors, to, adopting, r):
    """Record the engine's static errors on the applied tree in `r`: each fails, except an id that names another
    printed number (ID_DRIFT), which `--check` counts in a note (renaming them is T-353, due before adoption) and
    adoption (`adopting`) fails like the rest."""
    drift = [e for e in errors if ID_DRIFT.match(e)]
    for e in errors:
        if adopting or e not in drift:
            r.fail(None, f"static check of the applied {to} tree: {e}")
    if drift and not adopting:
        ids = ", ".join(e.split(":", 1)[0] for e in drift[:5]) + (", ..." if len(drift) > 5 else "")
        r.notes.append(f"static checks of the applied {to} tree: {len(drift)} id(s) name another printed number "
                       f"({ids}); rename them before adoption (T-353), which refuses them")


def static_check(year, r):
    """The engine's static checks (engine/src/check.ts runChecks: references, cycles, types, guard tiling, gates,
    citations, tables) on the tree the operations produce from `year` (canonical_of), through `main.js check`.
    Returns (errors, notes); errors holds one entry naming the problem when the engine cannot be run."""
    import subprocess
    main = ROOT / "engine" / "dist" / "main.js"
    if not main.exists():
        return [f"engine/dist/main.js is not built (npm run compile)"], []
    data, notes = canonical_of(year, r)
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(data, f)
        path = f.name
    out = path + ".out"
    try:
        with open(out, "w", encoding="utf-8") as f:  # a file, not a pipe: the engine exits before a pipe drains
            run = subprocess.run(["node", str(main), "check", path, "--year", str(year)], cwd=ROOT, stdout=f,
                                 stderr=subprocess.PIPE, text=True)
        text = Path(out).read_text(encoding="utf-8")
    finally:
        Path(path).unlink()
        Path(out).unlink(missing_ok=True)
    try:
        result = json.loads(text.strip().splitlines()[-1])
    except (ValueError, IndexError):
        return [f"main.js check did not report (exit {run.returncode}): {(run.stderr or text).strip()[:500]}"], notes
    return result["errors"], notes


# ---------------------------------------------------------------- writing an adopted year

class Dumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # a rewritten block stands alone: no anchor or alias another block could depend on
        return True


class IndentedDumper(Dumper):
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
    # A rewritten block loses its YAML anchors, so a kept block that aliases one of them is rewritten too (its alias
    # expanded), until no kept block names an anchor of a rewritten one.
    changed = set(changed)
    final_keys = {obj[item_key] for obj in final}
    while True:
        lost = {a for k, t in blocks.items() if k in changed or k not in final_keys for a in re.findall(r"&([\w-]+)", t)}
        more = {k for k, t in blocks.items() if k not in changed and k in final_keys
                and any(re.search(rf"\*{re.escape(a)}\b", t) for a in lost)}
        if not more:
            break
        changed |= more
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
    bank_text = tree.bank_text
    if st.bank != old_bank:
        old = {q.get("input"): q for q in old_bank}
        changed = {q.get("input") for q in st.bank if old.get(q.get("input")) != q}
        bank_text = rewrite_list(bank_text, "questions", "input", st.bank, changed)
    if BANK_FILE in r.iv_touched:
        bank_text = write_interview_edits(bank_text, {"bank": {**st.bank_meta, "questions": st.bank}},
                                          r.iv_touched[BANK_FILE], BANK_FILE)
    if bank_text != tree.bank_text:
        tree.bank_path.write_text(bank_text, encoding="utf-8")
    texts = {}
    for name, p in tree.profiles.items():
        if st.profiles[name] != p["data"]["interview"]["questions"]:
            texts[name] = rewrite_profile(p["text"], st.profiles[name])
    for name, touched in r.iv_touched.items():
        if name == BANK_FILE:
            continue
        path = tree.interview_dir / name
        if name not in st.others:
            path.unlink()
            continue
        if name not in tree.other_texts:
            path.parent.mkdir(parents=True, exist_ok=True)
            texts[name] = dump(st.others[name], False)
            continue
        data = st.others[name]
        if name in st.profiles:
            data = copy.deepcopy(data)
            data["interview"]["questions"] = st.profiles[name]
        texts[name] = write_interview_edits(texts.get(name, tree.other_texts[name]), data, touched, name)
    for name, text in texts.items():
        (tree.interview_dir / name).write_text(text, encoding="utf-8")
    if st.register != tree.register:
        old = {e.get("id"): e for e in tree.register}
        changed = {e.get("id") for e in st.register if old.get(e.get("id")) != e}
        tree.register_path.write_text(rewrite_list(tree.register_text, "entries", "id", st.register, changed),
                                      encoding="utf-8")


def write_interview_edits(text, final, touched, name):
    """An interview file's text with the paths the operations touched rewritten to their final values, block by
    block: an item of a list of entries with ids keeps or takes its own block; any other path is rewritten whole at
    its key. The result must load as the applied data."""
    done = set()
    for _, path in touched:
        k = next((i for i, p in enumerate(path) if p.startswith("#")), None)
        steps = path if k is None else path[:k]
        seq = get_path(final, steps) if k is not None else None
        if (k is not None and isinstance(seq, list) and seq and all(isinstance(x, dict) and "id" in x for x in seq)
                and len(re.findall(rf"(?m)^\s*{re.escape(steps[-1])}:\s*$", text)) == 1):
            if ("list", tuple(steps)) in done:
                continue
            done.add(("list", tuple(steps)))
            changed = {p2[k][1:] for _, p2 in touched if p2[:k] == steps and len(p2) > k}
            text = rewrite_list(text, steps[-1], "id", seq, changed)
            continue
        if ("path", tuple(steps)) in done:
            continue
        done.add(("path", tuple(steps)))
        value = get_path(final, steps)
        if k is not None and isinstance(value, list) and all(isinstance(x, (str, int, float)) for x in value):
            kept = rewrite_scalar_list(text, steps, value)
            if kept is not None:
                text = kept
                continue
        text = rewrite_path(text, steps, value, steps_present(final, steps))
    got = load_yaml(text)
    if got != final:
        raise SystemExit(f"year changes: writing interview/{name} block by block did not give the applied data")
    return text


def rewrite_scalar_list(text, path, final):
    """`text` with the block list of plain values at `path` edited line by line to `final`: an item no longer in it
    loses its line, a new one takes a line after the item before it; comments and the other items keep their lines.
    None when the list is not a block list of one-line items (rewrite_path then rewrites it whole)."""
    lines = text.splitlines(True)
    at, end = locate(lines, path)
    if at is None or lines[at].split(":", 1)[1].strip():
        return None
    item = re.compile(r"^( *)- (.+?)\s*$")
    have, ind = {}, None
    for i in range(at + 1, end):
        m = item.match(lines[i])
        if m:
            have[load_yaml(m.group(2))] = i
            ind = m.group(1)
        elif lines[i].strip() and not lines[i].lstrip().startswith("#"):
            return None
    if ind is None:
        return None
    drop = {i for v, i in have.items() if v not in final}
    add = {}  # line index after which -> [new item lines]
    prev = at
    for v in final:
        if v in have:
            prev = have[v]
        else:
            add.setdefault(prev, []).append(f"{ind}- {yaml.dump(v, Dumper=Dumper, width=100000).strip().removesuffix(chr(10) + '...')}\n")
    out = []
    for i, l in enumerate(lines):
        if i not in drop:
            out.append(l)
        out += add.get(i, [])
    return "".join(out)


def locate(lines, path):
    """(the line of the key at `path`, the end of its block) in a file's lines; (None, None) if it is not there."""
    lo, hi, parent, at = 0, len(lines), -1, None
    content = lambda l: l.strip() and not l.lstrip().startswith("#")  # noqa: E731
    for k in path:
        child = next((indent_of(lines[i]) for i in range(lo, hi) if content(lines[i])), None)
        if child is None or child <= parent:
            return None, None
        pat = re.compile(rf"^ {{{child}}}{re.escape(k)}:(\s|$)")
        at = next((i for i in range(lo, hi) if pat.match(lines[i])), None)
        if at is None:
            return None, None
        end = next((i for i in range(at + 1, hi) if content(lines[i]) and (indent_of(lines[i]) < child or (
            indent_of(lines[i]) == child and not lines[i].lstrip().startswith("- ")))), hi)
        while end > at + 1 and not content(lines[end - 1]):
            end -= 1
        lo, hi, parent = at + 1, end, child
    return at, hi


def steps_present(node, path):
    for k in path:
        if not isinstance(node, dict) or k not in node:
            return False
        node = node[k]
    return True


def rewrite_path(text, path, value, present):
    """`text` with the mapping key at `path` (keys from the top) rewritten to `value`, in the style the key had (a
    one-line [list] or {map} stays one line); `present` False removes the key; a key not there yet is added at the
    end of its parent's block."""
    lines = text.splitlines(True)
    lo, hi, parent = 0, len(lines), -1
    content = lambda l: l.strip() and not l.lstrip().startswith("#")  # noqa: E731
    at = None
    for depth, k in enumerate(path):
        child = next((indent_of(lines[i]) for i in range(lo, hi) if content(lines[i])), None)
        if child is None or child <= parent:
            child = parent + 2
        pat = re.compile(rf"^ {{{child}}}{re.escape(k)}:(\s|$)")
        at = next((i for i in range(lo, hi) if pat.match(lines[i])), None)
        if at is None:
            if depth != len(path) - 1:
                raise SystemExit(f"year changes: no key {'.'.join(path[:depth + 1])} to write")
            if not present:
                return text
            new = "".join(" " * child + l for l in dump({k: value}, False).splitlines(True))
            end = hi
            while end > lo and not content(lines[end - 1]):
                end -= 1
            return "".join(lines[:end]) + new + "".join(lines[end:])
        end = next((i for i in range(at + 1, hi) if content(lines[i]) and (indent_of(lines[i]) < child or (
            indent_of(lines[i]) == child and not lines[i].lstrip().startswith("- ")))), hi)  # an indentless list
        while end > at + 1 and not content(lines[end - 1]):
            end -= 1
        lo, hi, parent = at + 1, end, child
    head = lines[at]
    ind = indent_of(head)
    if not present:
        new = ""
    elif re.match(rf"^ *{re.escape(path[-1])}:\s*[\[{{]", head) and isinstance(value, (list, dict)):
        flow = yaml.dump(value, Dumper=Dumper, default_flow_style=True, allow_unicode=True, width=100000).strip()
        new = f"{' ' * ind}{path[-1]}: {flow}\n"
    else:
        new = "".join(" " * ind + l for l in dump({path[-1]: value}, False).splitlines(True))
    return "".join(lines[:at]) + new + "".join(lines[hi:])


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
      ambiguity: amb.2025.bonus
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
SELF_REGISTER = """register:
  tax_year: 2025
  entries:
    - id: amb.2025.bonus
      text_at_issue: Whether a bonus is wages.
      readings:
        - It is.
        - It is not.
      chosen: It is.
      reason: The form adds it.
      cite:
        doc: fx
        locator: p. 2, Line 2
      status: Applied.
    # a comment kept with the entry before it
    - id: amb.2025.old
      text_at_issue: An old question.
      readings:
        - One reading.
      chosen: One reading.
      reason: Only one.
      cite:
        doc: fx
        locator: p. 2
      unlinked: Superseded.
"""
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
          ambiguity: amb.2026.tips
    - add_question: {input: fa.tips, like: fa.bonus, entry: {help: Tips you were paid.}, default: 0,
                     reason: "Closed: no amount unless the scenario states one."}
    - set: {line: fa.line2, field: printed, from: "2", to: "3"}
    - set: {line: fa.line2, field: expr.of, from: [fa.wages, fa.bonus], to: [fa.wages, fa.bonus, fa.tips]}
    - set_question: {input: fa.flag, field: help, from: Answer yes if flagged., to: Answer yes if you are flagged.}
    - add_ambiguity:
        entry:
          id: amb.2026.tips
          text_at_issue: Whether tips include service charges.
          readings: [They do., They do not.]
          chosen: They do not.
          reason: Line 2b says tips.
          cite: {doc: fx, locator: p. 3, Line 2b}
    - set_ambiguity: {id: amb.2025.bonus, field: status, from: Applied., to: Applied; recheck in 2026.}
"""
SELF_BANK_GROUPS = SELF_BANK.replace("  questions:\n", "  groups:\n  - id: g1\n    heading: Any of these?\n  questions:\n").replace(
    "    help: Answer yes if flagged.\n", "    help: Answer yes if flagged.\n    group: g1\n")
SELF_PROFILE_IV = SELF_PROFILE.replace("  - fa.line2\n", "  # the form's result\n  - fa.line2\n  - fa.wages\n")
SELF_IV = {
    "coverage/fa.yaml": """# Coverage rows of form A.
tax_year: 2025
sets:
  earner:
    says: A person with wages.
    answers:
      fa.wages: 100
rows:
- id: r1
  situation: Wages only.
  uses: [earner]
  answers:
    fa.bonus: 0
  expect:
    proceeds:
      fa.wages: 100
# a comment kept with r1
- id: r2
  situation: A bonus.
  answers:
    fa.bonus: 5
  expect:
    proceeds:
      fa.bonus: 5
""",
    "freq.yaml": """# Gate frequencies.
situations:
  s1:
    label: Wages
    refs: [fa.wages]
    share: 0.5
  s2:
    label: Bonus
    refs: [fa.bonus]
    share: 0.1
""",
    "personas/p1.yaml": "name: p1\nwho: A person with a bonus.\nanswers:\n  fa.bonus: 5\n",
}
GOOD_IV = GOOD + """    - add_interview_item: {file: basic.yaml, list: interview.targets, item: fa.tips}
    - remove_interview_item: {file: basic.yaml, list: interview.targets, item: fa.wages}
    - set_interview: {file: coverage/fa.yaml, list: rows, item: r1, field: answers, from: {fa.bonus: 0},
                      to: {fa.bonus: 0, fa.tips: 0}}
    - remove_interview_item: {file: coverage/fa.yaml, list: rows, item: r2}
    - add_interview_item: {file: freq.yaml, list: situations.s2.refs, item: fa.tips}
    - set_interview: {file: freq.yaml, field: situations.s1.share, from: 0.5, to: 0.6}
    - remove_interview_file: {file: personas/p1.yaml}
    - add_interview_file: {file: personas/p2.yaml, data: {name: p2, who: A person with tips., answers: {fa.tips: 7}}}
"""
SPLIT = """changes:
  tax_year: 2026
  form: fa
  entries:
  - change: C-3
    evidence:
    - {doc: fx, page: 3, quote: "Line 2b Tips"}
    verified: draft
    operations:
    - set: {line: fa.wages, field: label, from: Wages, to: Wages and salaries}
"""


def self_test():
    import citations as C
    status = 0

    def make(tmp, forms=None, bank=SELF_BANK, profile=SELF_PROFILE, changes=GOOD, register=SELF_REGISTER, split=None,
             iv=None):
        import shutil
        tmp = Path(tmp)
        shutil.rmtree(tmp / "interview", ignore_errors=True)
        (tmp / "forms").mkdir(parents=True, exist_ok=True)
        (tmp / "interview").mkdir(exist_ok=True)
        (tmp / "changes").mkdir(exist_ok=True)
        (tmp / "sources").mkdir(exist_ok=True)
        for name, text in (forms or SELF_FORMS).items():
            (tmp / "forms" / f"{name}.yaml").write_text(text, encoding="utf-8")
        (tmp / "interview" / "questions.yaml").write_text(bank, encoding="utf-8")
        (tmp / "interview" / "basic.yaml").write_text(profile, encoding="utf-8")
        for name, text in (iv or {}).items():
            (tmp / "interview" / name).parent.mkdir(parents=True, exist_ok=True)
            (tmp / "interview" / name).write_text(text, encoding="utf-8")
        (tmp / "params.yaml").write_text(SELF_PARAMS, encoding="utf-8")
        for p in (tmp / "changes").glob("*.yaml"):
            p.unlink()
        if changes is not None:
            (tmp / "changes" / "fa.yaml").write_text(changes, encoding="utf-8")
        if split is not None:  # a split file: changes/<form>.<topic>.yaml, keyed by its form: field
            (tmp / "changes" / "fa.more.yaml").write_text(split, encoding="utf-8")
        (tmp / "register.yaml").write_text(register, encoding="utf-8")
        planted = tmp / "sources"  # the synthetic archive's one text layer, written for the evidence check
        (planted / "fx.txt").write_text("\f".join(SELF_PAGES), encoding="utf-8")
        (tmp / "sources" / "manifest.json").write_text(json.dumps({"documents": [
            {"id": "fx", "file": "fx.pdf", "text_file": "fx.txt", "draft": True}]}), encoding="utf-8")
        return Tree(tmp / "forms", tmp / "interview", tmp / "params.yaml", tmp / "register.yaml")

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
        hit = [m for _, m in r.failures if needle and needle in m]
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
                "    - add_question: {input: fa.tips, like: fa.bonus, entry: {help: Tips you were paid.}, default: 0,\n"
                "                     reason: \"Closed: no amount unless the scenario states one.\"}\n", "")},
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
            # a new input's test-data default (add_question default and reason)
            ("a new input with no default", {"changes": GOOD.replace(" default: 0,", "")},
             "default: fa.tips has no test-data default"),
            ("a new input's default of the wrong type", {"changes": GOOD.replace(" default: 0,", " default: true,")},
             "default: fa.tips default true is not a value of Dollars"),
            ("a new input's default with no one-line reason",
             {"changes": GOOD.replace('"Closed: no amount unless the scenario states one."', '""')},
             "default: fa.tips needs a one-line reason"),
            # the ambiguity register
            ("an added ambiguity whose id the register holds",
             {"changes": GOOD.replace("id: amb.2026.tips", "id: amb.2025.old")}, "collision: the register has an entry amb.2025.old"),
            ("an added ambiguity missing a field", {"changes": GOOD.replace("          chosen: They do not.\n", "")},
             "malformed, missing entry.chosen"),
            ("an added ambiguity no line links", {"changes": GOOD.replace("          ambiguity: amb.2026.tips\n", "")},
             "unlinked: no line links the added ambiguity amb.2026.tips"),
            ("a line links an ambiguity the register does not hold",
             {"changes": GOOD.replace("          ambiguity: amb.2026.tips\n", "          ambiguity: amb.2026.tipz\n")},
             "dangling: fa.tips links the ambiguity amb.2026.tipz"),
            ("an ambiguity an operation sets is gone", {"changes": GOOD.replace("{id: amb.2025.bonus,", "{id: amb.2025.bonuz,")},
             "gone: no register entry amb.2025.bonuz (closest: amb.2025.bonus"),
            ("a register text an operation expects has changed",
             {"register": SELF_REGISTER.replace("status: Applied.", "status: Applied to 2025.")},
             "stale: expected 'Applied.', found 'Applied to 2025.'"),
            ("a register id set", {"changes": GOOD + "    - set_ambiguity: {id: amb.2025.old, field: id, from: amb.2025.old, to: x}\n"},
             "malformed: register ids are kept"),
            ("an ambiguity removed after an operation changed it",
             {"changes": GOOD + "    - remove_ambiguity: {id: amb.2025.bonus}\n"},
             "collision: fa.yaml C-1 op 7 (set_ambiguity amb.2025.bonus status) adds or changes amb.2025.bonus"),
            ("a removed ambiguity a line still links", {"changes": GOOD.replace(
                "    - set_ambiguity: {id: amb.2025.bonus, field: status, from: Applied., to: Applied; recheck in 2026.}\n",
                "    - remove_ambiguity: {id: amb.2025.bonus}\n")},
             "dangling: fa.bonus still links the removed ambiguity amb.2025.bonus"),
            ("an operation on an ambiguity another removes", {"changes": GOOD.replace(
                "    - set_ambiguity:", "    - remove_ambiguity: {id: amb.2025.bonus}\n    - set_ambiguity:")},
             "collision: fa.yaml C-1 op 7 (remove_ambiguity amb.2025.bonus) removes amb.2025.bonus"),
            ("an entry left with no line linking it", {"changes": GOOD + "    - set: {line: fa.bonus, field: ambiguity, "
                                                        "from: amb.2025.bonus, to: null}\n"},
             "unlinked: no line links amb.2025.bonus once the operations apply"),
            # split files: changes/<form>.<topic>.yaml, applied in file order, collisions across files
            ("two files set the same field",
             {"split": SPLIT.replace("field: label, from: Wages, to: Wages and salaries",
                                     "field: printed, from: \"2\", to: \"4\"").replace("fa.wages", "fa.line2")},
             "collision: fa.yaml C-1 op 3 (set fa.line2 printed) also sets printed"),
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
        # A split file for the same form applies after fa.yaml, as one list.
        r, _ = run(tmp, split=SPLIT)
        ok = (not r.failures and len(r.ops) == len(load_changes(Path(tmp) / "changes")[1])
              and r.state.line("fa.wages")["label"] == "Wages and salaries")
        status = status or (0 if ok else 1)
        print("year-changes self-test: a split file changes/fa.more.yaml (form: fa) applies with fa.yaml: "
              + ("as expected" if ok else f"WRONG ({r.failures})"))

        # Writing: the files edited block by block equal the data applied in memory, and every untouched line
        # block keeps its text.
        r, tree = run(tmp)
        before = {p.name: p.read_text() for p in (Path(tmp) / "forms").glob("*.yaml")}
        bank_before = (Path(tmp) / "interview" / "questions.yaml").read_text()
        register_before = (Path(tmp) / "register.yaml").read_text()
        write_state(tree, r)
        after = Tree(Path(tmp) / "forms", Path(tmp) / "interview", Path(tmp) / "params.yaml", Path(tmp) / "register.yaml")
        same = (after.forms["fa"]["doc"]["lines"] == r.state.forms["fa"]["lines"]
                and after.bank["questions"] == r.state.bank
                and after.profiles["basic.yaml"]["data"]["interview"]["questions"] == r.state.profiles["basic.yaml"]
                and after.register == r.state.register)
        _, old_items, _, _, _ = list_blocks(before["fa.yaml"], "lines", "id")
        _, new_items, _, _, _ = list_blocks(after.forms["fa"]["text"], "lines", "id")
        new_items = dict(new_items)
        kept = all(new_items.get(i) == t for i, t in old_items if i not in r.touched)
        _, old_q, _, _, _ = list_blocks(bank_before, "questions", "input")
        _, new_q, _, _, _ = list_blocks(after.bank_text, "questions", "input")
        kept_q = all(dict(new_q).get(i) == t for i, t in old_q if i != "fa.flag")
        styled = "        of:\n          - fa.wages\n          - fa.bonus\n          - fa.tips\n" in after.forms["fa"]["text"]
        _, old_a, _, _, _ = list_blocks(register_before, "entries", "id")
        _, new_a, _, _, _ = list_blocks(after.register_text, "entries", "id")
        kept_a = all(dict(new_a).get(i) == t for i, t in old_a if i not in r.amb_touched)
        ok = same and kept and kept_q and kept_a and styled and "# a comment kept" in after.forms["fa"]["text"]
        status = status or (0 if ok else 1)
        print("year-changes self-test: written files equal the applied data, untouched blocks byte-for-byte: "
              + ("as expected" if ok else f"WRONG (data {same}, lines kept {kept}, questions kept {kept_q}, "
                                          f"register kept {kept_a})"))
        # A YAML anchor in a rewritten line that a kept line aliases: the kept line is rewritten with the alias
        # expanded, so the written file loads (the writer drops the anchor of a block it rewrites).
        anchored = SELF_FORMS["fa"].replace(
            '        locator: p. 2, Line 2, "Add line 1 and the bonus"\n',
            '        locator: p. 2, Line 2, "Add line 1 and the bonus"\n      refuses: &r1\n        - when: fa.wages\n'
            '          form: Form Z\n').replace(
            "      ambiguity: amb.2025.bonus\n", "      ambiguity: amb.2025.bonus\n      refuses: *r1\n")
        r, tree = run(tmp, forms={"fa": anchored})
        write_state(tree, r)
        try:
            after = Tree(Path(tmp) / "forms", Path(tmp) / "interview", Path(tmp) / "params.yaml", Path(tmp) / "register.yaml")
            ok = (not r.failures and "*r1" in anchored and after.forms["fa"]["doc"]["lines"] == r.state.forms["fa"]["lines"]
                  and "*r1" not in after.forms["fa"]["text"])
        except yaml.YAMLError as e:
            ok = f"does not load: {e}"
        status = status or (0 if ok is True else 1)
        print("year-changes self-test: a kept line aliasing an anchor of a rewritten line is written expanded: "
              + ("as expected" if ok is True else f"WRONG ({ok or r.failures})"))
        # The interview operations: profiles' targets, coverage rows and sets, gate frequencies, personas, groups.
        ivkw = {"iv": SELF_IV, "bank": SELF_BANK_GROUPS, "profile": SELF_PROFILE_IV, "changes": GOOD_IV}
        r, _ = run(tmp, **ivkw)
        expect("the planted interview operations apply", r, None)
        iv_cases = [
            ("an interview file that is gone", {"changes": GOOD_IV.replace("file: freq.yaml, list", "file: freqs.yaml, list")},
             "gone: no interview file freqs.yaml (closest: freq.yaml)"),
            ("an item that is gone", {"changes": GOOD_IV.replace("list: rows, item: r2", "list: rows, item: r3")},
             "gone: rows of interview/coverage/fa.yaml has no item r3"),
            ("an interview value an operation expects has changed",
             {"iv": {**SELF_IV, "freq.yaml": SELF_IV["freq.yaml"].replace("share: 0.5", "share: 0.4")}},
             "stale: expected 0.5, found 0.4"),
            ("an interview item already there", {"profile": SELF_PROFILE_IV.replace("  - fa.wages\n", "  - fa.wages\n  - fa.tips\n")},
             "already applied: the item exists as written"),
            ("two operations on one interview item", {"changes": GOOD_IV + "    - remove_interview_item: {file: coverage/fa.yaml, "
                                                      "list: rows, item: r1}\n"}, "collision"),
            ("an operation on an interview file another removes",
             {"changes": GOOD_IV + "    - set_interview: {file: personas/p1.yaml, field: who, from: x, to: y}\n"},
             "gone: no interview file personas/p1.yaml"),
            ("an interview operation writes a line that does not exist",
             {"changes": GOOD_IV.replace("to: {fa.bonus: 0, fa.tips: 0}", "to: {fa.bonus: 0, fa.tipz: 0}")},
             "dangling: interview/coverage/fa.yaml would name fa.tipz"),
            ("a removed line still named by a coverage row, a persona, a gate frequency",
             {"changes": GOOD_IV.replace("    - remove_interview_file: {file: personas/p1.yaml}\n", "")
              + "    - remove_line: {line: fa.bonus}\n    - remove_question: {input: fa.bonus}\n"},
             "dangling: interview/personas/p1.yaml still names the removed fa.bonus"),
            ("a coverage set removed while a row uses it",
             {"changes": GOOD_IV + "    - set_interview: {file: coverage/fa.yaml, field: sets.earner, "
                                   "from: {says: A person with wages., answers: {fa.wages: 100}}, to: null}\n"},
             "dangling: interview/coverage/fa.yaml still names earner"),
            ("a group removed while a question names it",
             {"changes": GOOD_IV + "    - remove_interview_item: {file: questions.yaml, list: bank.groups, item: g1}\n"},
             "dangling: question fa.flag names the tick-box group g1"),
            ("a profile's questions set by an interview operation",
             {"changes": GOOD_IV + "    - set_interview: {file: basic.yaml, field: interview.questions, from: [], to: []}\n"},
             "malformed: questions are changed by the question operations"),
        ]
        for name, kw, needle in iv_cases:
            r, _ = run(tmp, **{**ivkw, **kw})
            expect(name, r, needle)
        # The last question of a group goes: its group is left with no member.
        r, _ = run(tmp, **{**ivkw, "changes": GOOD_IV.replace(
            "    - set_question: {input: fa.flag, field: help, from: Answer yes if flagged., to: Answer yes if you are flagged.}\n",
            "    - set_question: {input: fa.flag, field: group, from: g1, to: null}\n")})
        expect("a tick-box group no question names", r, "group left: tick-box group g1")
        # Writing the interview files: equal to the applied data; comments and untouched blocks kept.
        r, tree = run(tmp, **ivkw)
        cov_before = (Path(tmp) / "interview" / "coverage" / "fa.yaml").read_text()
        write_state(tree, r)
        after = Tree(Path(tmp) / "forms", Path(tmp) / "interview", Path(tmp) / "params.yaml", Path(tmp) / "register.yaml")
        want = {k: v for k, v in r.state.others.items()}
        want["basic.yaml"] = {**want["basic.yaml"], "interview": {**want["basic.yaml"]["interview"],
                                                                  "questions": r.state.profiles["basic.yaml"]}}
        ftext = (Path(tmp) / "interview" / "freq.yaml").read_text()
        ok = (after.others == want and "personas/p1.yaml" not in after.others
              and "  # the form's result\n" in after.other_texts["basic.yaml"]
              and "    refs: [fa.bonus, fa.tips]\n" in ftext and "# Gate frequencies." in ftext
              and cov_before.split("# a comment kept with r1")[0].split("- id: r1")[0] in after.other_texts["coverage/fa.yaml"]
              and [g["id"] for g in after.bank["groups"]] == ["g1"])
        status = status or (0 if ok else 1)
        print("year-changes self-test: interview files written equal the applied data, comments kept: "
              + ("as expected" if ok else "WRONG"))
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
    status = static_findings_self_test() or status
    status = static_self_test() or status
    return status


def static_findings_self_test():
    """static_findings: an id-drift error is a counted note naming T-353 under --check and a failure in adoption;
    every other static error fails in both."""
    drift = "f9.line4: the id names line 4, but the line is printed 5; give it an id that names no number (tools/rename_ids.py)"
    other = "f9.line6: declared count but computes money"
    status = 0
    for adopting, want_fail, want_note in ((False, 1, True), (True, 2, False)):
        r = Result()
        static_findings([drift, other], 2026, adopting, r)
        noted = any("1 id(s) name another printed number (f9.line4)" in n and "T-353" in n for n in r.notes)
        ok = len(r.failures) == want_fail and noted == want_note and any("f9.line6" in m for _, m in r.failures)
        status = status or (0 if ok else 1)
        print(f"year-changes self-test: id drift {'in adoption fails' if adopting else 'under --check is a counted note'}, "
              f"other static errors fail: " + ("ok" if ok else f"WRONG (failures {r.failures}, notes {r.notes})"))
    return status


def static_self_test():
    """static_check on this checkout's applied next year with one planted defect per kind the operations' own
    checks cannot see (a line declared Count that computes money; a line that reads itself), each found by the
    engine and named by its line. Runs only where the engine is built and there are operations."""
    import taxyear
    year = taxyear.Y
    if jurisdiction.NY or not (ROOT / "engine" / "dist" / "main.js").exists():
        print("year-changes self-test: static checks of the applied tree: skipped (New York, or the engine is not built)")
        return 0
    _, r = check(year, quiet=True)
    if r.failures or r.state is None or not r.touched:
        print("year-changes self-test: static checks of the applied tree: skipped (no operations apply)")
        return 0
    status = 0
    drift_lid = next((l for l in sorted(r.touched) if re.search(r"\.line\d+[a-z]?$", l)
                      and re.match(r"^\d", str((r.state.line(l) or {}).get("printed", "")))), None)
    if drift_lid:
        dline = r.state.line(drift_lid)
        dsaved = copy.deepcopy(dline)
        number = int(re.search(r"\.line(\d+)", drift_lid).group(1))
        dline["printed"] = str(number + 100)
        errors, _ = static_check(year, r)
        dline.clear(); dline.update(copy.deepcopy(dsaved))
        ok = any(ID_DRIFT.match(e) and e.startswith(f"{drift_lid}:") for e in errors)
        status = status or (0 if ok else 1)
        print(f"year-changes self-test: static checks of the applied tree, an id naming another printed number "
              f"({drift_lid}): " + ("found" if ok else f"WRONG ({'; '.join(errors[:3]) or 'nothing found'})"))
    lid = next(l for l in sorted(r.touched) if (r.state.line(l) or {}).get("type") in ("Dollars", "NonNegDollars")
               and (r.state.line(l).get("expr") or {}).get("op") in ("sum", "copy", "subtract"))
    line = r.state.line(lid)
    saved = copy.deepcopy(line)
    plants = [("a line declared Count that computes money", lambda: line.update(type="Count"), "declared count"),
              ("a line that reads itself", lambda: line.update(expr={"op": "copy", "from": lid}), "cycle")]
    for name, plant, needle in plants:
        plant()
        errors, _ = static_check(year, r)
        line.clear(); line.update(copy.deepcopy(saved))
        ok = any(needle in e and lid in e for e in errors)
        status = status or (0 if ok else 1)
        print(f"year-changes self-test: static checks of the applied tree, {name} ({lid}): "
              + ("found" if ok else f"WRONG ({'; '.join(errors[:3]) or 'nothing found'})"))
    return status


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--against", help="a checkout or export whose forms/, interview/ and params/ to check instead")
    ap.add_argument("--no-static", action="store_true", help="skip the engine's static checks of the applied tree")
    ap.add_argument("--record", metavar="EDITED_YAML")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        sys.exit(self_test())
    if a.record:
        sys.stdout.write(dump(record(taxyear.Y, a.record), False))
        return
    if a.check:
        sys.exit(check(taxyear.Y, a.against, static=not a.no_static)[0])
    ap.error("one of --check, --record, --self-test")


if __name__ == "__main__":
    main()
