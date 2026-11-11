#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Twin check: lines the form data states twice must stay in step, offline, in check-all.

Form 8863 Part III is written once for a person on the return (person.edu*) and once for a dependent
(dependent.edu*), because a student is either and no line can range over both collections. The check pairs
the two blocks by local id and compares every pair, field by field, after normalizing only what must differ:
a reference to a line of the side's own document (person.edu_no and dependent.edu_no are the same reference)
and, for a line that reads the block from outside, the collection it ranges over.

Compared for each pair, as flat fields named by their path:
  - the form line (forms/<year>/<doc>.yaml): printed, label, type, shown_when, expr (structure, operands and
    the question wording expr.source), cite, refuses (gate, form, remedy, cite), ambiguity and any other key;
  - the question bank entry (interview/<year>/questions.yaml), as interview.<key> (order, help, ...);
  - the test-data default (fixtures/<year>/defaults.json), as fixture_default.value and .reason.

reviews/<year>/twins.json declares what is compared and every intended difference:
  sides        the two documents, and `local`, the pattern of the local ids that form the blocks
  readers      pairs of lines outside the blocks that read them, one per side, compared the same way
  one_sided    ids of a block that have no twin, each with its reason and source
  differences  one entry per pair and field that differs on purpose: both sides' values (null for a field
               one side lacks; {"pattern": REGEX} to accept any value the pattern fully matches), the
               reason, and its source

The check fails, naming the pair, the field and both texts, on: a difference that is not declared; a declared
difference that no longer exists, or whose values are no longer the declared ones; an id of a block with no
twin that is not declared one-sided; and a declared one-sided id that is gone or has a twin. So a change to
one side must be made on the other or declared, and the declarations cannot outlive what they describe.

    check_twins.py                                  check (exit 1 on any problem)
    check_twins.py --sync-from SIDE [--pair NAME]... [--write]
                                                    for each undeclared difference, show the change that copies
                                                    SIDE's field to the other side; --write makes it
    check_twins.py --self-test

--sync-from copies whole top-level fields of a form line (label, expr, cite, ...) or of a question bank entry,
as text, renaming the references. It never copies a field that holds a declared difference, never creates or
deletes a line, and leaves fixture defaults alone (tools/defaults_guard.mjs governs them); those are edited by
hand. Before anything is written the result is parsed and compared with the data as it was: only the copied
fields may differ, and they must now agree.
"""
import copy
import difflib
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402

MISSING = object()
# Fields of a pair that come from outside the form line, by their first path component.
BANK, DEFAULT = "interview", "fixture_default"


def config_path(root, year):
    return Path(root) / "reviews" / year / "twins.json"


def form_path(root, year, doc):
    return Path(root) / "forms" / year / f"{doc}.yaml"


def bank_path(root, year):
    return Path(root) / "interview" / year / "questions.yaml"


def defaults_path(root, year):
    return Path(root) / "fixtures" / year / "defaults.json"


def read_config(root=ROOT, year=Y):
    path = config_path(root, year)
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def documents(config):
    """The form documents the declarations name: the two sides and the readers' documents."""
    docs = list(config["sides"])
    for reader in config.get("readers", []):
        for side in config["sides"]:
            doc = reader[side].split(".", 1)[0]
            if doc not in docs:
                docs.append(doc)
    return docs


def files(root, year, config):
    return [config_path(root, year), bank_path(root, year), defaults_path(root, year)] + \
        [form_path(root, year, doc) for doc in documents(config)]


def load(root=ROOT, year=Y):
    """The declarations and everything they are compared with, parsed."""
    config = read_config(root, year)
    if config is None:
        raise SystemExit(f"twins: {config_path(root, year)} is missing; it declares the year's twin blocks")
    data = {"config": config, "file": str(config_path(root, year).relative_to(root)), "forms": {}, "lines": {}, "order": {}}
    for doc in documents(config):
        form = yaml.safe_load(form_path(root, year, doc).read_text(encoding="utf-8"))
        data["forms"][doc] = form
        lines = next(iter(form.values()))["lines"]
        data["order"][doc] = [line["id"] for line in lines]
        data["lines"].update({line["id"]: line for line in lines})
    bank = yaml.safe_load(bank_path(root, year).read_text(encoding="utf-8"))
    data["bank_doc"] = bank
    data["bank"] = {q["input"]: q for q in bank["bank"]["questions"]}
    defaults = json.loads(defaults_path(root, year).read_text(encoding="utf-8"))
    data["defaults_doc"] = defaults
    data["defaults"] = {d["input"]: d for d in defaults["defaults"]}
    return data


def local_ids(data, side):
    pattern = re.compile(data["config"]["local"])
    return [i.split(".", 1)[1] for i in data["order"][side] if pattern.fullmatch(i.split(".", 1)[1])]


def pairs(data):
    """[(name, {side: line id})]: the block pairs by local id, then the declared reader pairs."""
    left, right = data["config"]["sides"]
    on_right = set(local_ids(data, right))
    found = [(local, {left: f"{left}.{local}", right: f"{right}.{local}"}) for local in local_ids(data, left) if local in on_right]
    for reader in data["config"].get("readers", []):
        found.append((reader["pair"], {left: reader[left], right: reader[right]}))
    return found


def one_sided(data):
    left, right = data["config"]["sides"]
    on_left, on_right = local_ids(data, left), local_ids(data, right)
    return [f"{left}.{i}" for i in on_left if i not in set(on_right)] + [f"{right}.{i}" for i in on_right if i not in set(on_left)]


def twin_of(line_id, config=None):
    """The id that pairs with `line_id` under the year's declarations (it may not exist), or None."""
    config = read_config() if config is None else config
    if not config:
        return None
    left, right = config["sides"]
    for reader in config.get("readers", []):
        if line_id in (reader[left], reader[right]):
            return reader[right] if line_id == reader[left] else reader[left]
    doc, _, local = line_id.partition(".")
    if doc in (left, right) and re.fullmatch(config["local"], local):
        return f"{right if doc == left else left}.{local}"
    return None


def flatten(value, path, out):
    if isinstance(value, dict) and value:
        for key, item in value.items():
            flatten(item, f"{path}.{key}" if path else str(key), out)
    elif isinstance(value, list) and value:
        for i, item in enumerate(value):
            flatten(item, f"{path}[{i}]", out)
    else:
        out[path] = value
    return out


def view(data, line_id):
    """The flat fields of one side of a pair: its form line, its bank entry and its test-data default."""
    out = {}
    if line_id in data["lines"]:
        flatten({k: v for k, v in data["lines"][line_id].items() if k != "id"}, "", out)
    if line_id in data["bank"]:
        flatten({k: v for k, v in data["bank"][line_id].items() if k != "input"}, BANK, out)
    if line_id in data["defaults"]:
        flatten({k: v for k, v in data["defaults"][line_id].items() if k != "input"}, DEFAULT, out)
    return out


def normalized(field, value, side):
    """`value` with what must differ between the sides removed: a whole-string reference to a line of the
    side's own document, and the collection a reader ranges over. Prose is compared as written."""
    if isinstance(value, str):
        if value == side and field.split(".")[-1] == "collection":
            return "X"
        m = re.fullmatch(rf"{re.escape(side)}\.(\w+)", value)
        if m:
            return f"X.{m.group(1)}"
    return value


def differing(data):
    """{(pair name, field): (left value, right value)} for every field whose normalized values differ."""
    left, right = data["config"]["sides"]
    out = {}
    for name, ids in pairs(data):
        a, b = view(data, ids[left]), view(data, ids[right])
        for field in list(a) + [f for f in b if f not in a]:
            va, vb = a.get(field, MISSING), b.get(field, MISSING)
            if va is MISSING and vb is MISSING:
                continue
            if va is MISSING or vb is MISSING or normalized(field, va, left) != normalized(field, vb, right):
                out[(name, field)] = (va, vb)
    return out


def shown(value):
    if value is MISSING or value is None:
        return "(absent)"
    return value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)


def accepts(declared, actual):
    if declared is None:
        return actual is MISSING or actual is None
    if actual is MISSING:
        return False
    if isinstance(declared, dict) and set(declared) == {"pattern"}:
        return re.fullmatch(declared["pattern"], shown(actual), re.S) is not None
    return declared == actual


def both(sides, values):
    width = max(len(s) for s in sides) + 1
    return "".join(f"\n    {(side + ':').ljust(width)} {shown(value)}" for side, value in zip(sides, values))


def problems(data):
    """Every way the declarations and the data disagree, as messages."""
    config, where = data["config"], data["file"]
    sides = config["sides"]
    left, right = sides
    found = []
    pair_ids = dict(pairs(data))
    actual = differing(data)

    declared = {}
    for n, entry in enumerate(config.get("differences", [])):
        key = (entry.get("pair"), entry.get("field"))
        lacking = [k for k in ("pair", "field", left, right, "reason", "source") if k not in entry or entry[k] == ""]
        if lacking:
            found.append(f"twins: {where}: differences[{n}] ({key[0]}, {key[1]}) lacks {', '.join(lacking)}")
        elif key in declared:
            found.append(f"twins: {where}: {key[0]}, field {key[1]}: declared twice")
        else:
            declared[key] = entry

    def title(name, field):
        ids = pair_ids[name]
        return f"twins: {name} ({ids[left]} / {ids[right]}), field {field}"

    for (name, field), values in actual.items():
        entry = declared.get((name, field))
        if entry is None:
            found.append(f"{title(name, field)}: the sides differ and the difference is not declared{both(sides, values)}"
                         f"\n    Make the sides agree (check_twins.py --sync-from SIDE shows the copy), or declare the difference"
                         f" with its reason and source in {where}.")
        elif not (accepts(entry[left], values[0]) and accepts(entry[right], values[1])):
            found.append(f"{title(name, field)}: the sides no longer hold the declared values{both(sides, values)}"
                         f"\n    declared in {where}:{both(sides, (entry[left], entry[right]))}"
                         f"\n    A declared difference is reread when either side changes: bring the twin into step, then update the entry.")
    for (name, field), entry in declared.items():
        if name not in pair_ids:
            found.append(f"twins: {where}: {name}, field {field}: a difference is declared for a pair that does not exist; remove the entry")
        elif (name, field) not in actual:
            ids = pair_ids[name]
            value = view(data, ids[left]).get(field, MISSING)
            found.append(f"{title(name, field)}: declared as a difference, but the sides no longer differ{both(sides, (value, value))}"
                         f"\n    Remove the entry from {where}.")

    declared_one = config.get("one_sided", {})
    actual_one = one_sided(data)
    for line_id in actual_one:
        if line_id not in declared_one:
            found.append(f"twins: {line_id} has no twin ({twin_of(line_id, config)} does not exist) and is not declared one-sided"
                         f"\n    Add the twin, or declare the id in {where} (one_sided) with its reason and source.")
    for line_id, entry in declared_one.items():
        if not isinstance(entry, dict) or not entry.get("reason") or not entry.get("source"):
            found.append(f"twins: {where}: one_sided {line_id} lacks a reason or a source")
        if line_id not in actual_one:
            state = "has a twin" if line_id in data["lines"] else "does not exist"
            found.append(f"twins: {where}: {line_id} is declared one-sided but {state}; remove the entry")
    return found


def summary(data):
    blocks = len(pairs(data)) - len(data["config"].get("readers", []))
    return (f"{blocks} pairs and {len(data['config'].get('readers', []))} reader pairs compared; "
            f"{len(data['config'].get('differences', []))} declared differences; {len(one_sided(data))} one-sided ids")


# --sync-from: copying a top-level field of an entry as text.

def entry_span(lines, start_key, ident):
    """(first line, end, indent of the dash) of the list entry `- <start_key>: <ident>` in a YAML file's lines."""
    head = re.compile(rf"^(\s*)- {start_key}: {re.escape(ident)}\s*$")
    for i, line in enumerate(lines):
        m = head.match(line)
        if m:
            indent = len(m.group(1))
            end = i + 1
            while end < len(lines) and (not lines[end].strip() or len(lines[end]) - len(lines[end].lstrip()) > indent):
                end += 1
            while not lines[end - 1].strip():
                end -= 1
            return i, end, indent
    return None


def chunks(lines, first, end, indent):
    """[(key, start, end)] for the entry's top-level keys after the one on its dash line."""
    key = re.compile(rf"^ {{{indent + 2}}}([A-Za-z_]\w*):")
    starts = [(m.group(1), i) for i in range(first + 1, end) if (m := key.match(lines[i]))]
    return [(k, s, starts[n + 1][1] if n + 1 < len(starts) else end) for n, (k, s) in enumerate(starts)]


def renamed(text_lines, src, dst):
    out = []
    for line in text_lines:
        line = re.sub(rf"(?<![\w.\[]){re.escape(src)}\.(?=\w)", f"{dst}.", line)
        out.append(re.sub(rf"^(\s*collection: ){re.escape(src)}\s*$", rf"\g<1>{dst}", line))
    return out


def copy_field(path, start_key, src_id, dst_id, key, src_path, sides):
    """Rewrite `path` so that entry `dst_id`'s top-level `key` is entry `src_id`'s (from `src_path`), renamed."""
    src_side, dst_side = sides
    src_lines = src_path.read_text(encoding="utf-8").split("\n")
    lines = path.read_text(encoding="utf-8").split("\n") if path != src_path else src_lines
    src_span, dst_span = entry_span(src_lines, start_key, src_id), entry_span(lines, start_key, dst_id)
    if not src_span or not dst_span:
        return f"entry {src_id if not src_span else dst_id} not found as text"
    src_chunks, dst_chunks = chunks(src_lines, *src_span), chunks(lines, *dst_span)
    src_at = {k: (s, e) for k, s, e in src_chunks}
    dst_at = {k: (s, e) for k, s, e in dst_chunks}
    new = renamed(src_lines[slice(*src_at[key])], src_side, dst_side) if key in src_at else []
    if src_span[2] != dst_span[2]:
        return "the two entries are indented differently"
    if key in dst_at:
        s, e = dst_at[key]
    else:
        before = [k for k, _, _ in src_chunks[:[k for k, _, _ in src_chunks].index(key)] if k in dst_at]
        s = e = dst_at[before[-1]][1] if before else dst_span[0] + 1
    lines[s:e] = new
    path.write_text("\n".join(lines), encoding="utf-8")
    return None


def top_field(field):
    """The top-level field a flat field belongs to, the unit --sync-from copies: label, expr, cite, interview.help."""
    parts = re.split(r"[.\[]", field)
    return f"{BANK}.{parts[1]}" if parts[0] == BANK and len(parts) > 1 else parts[0]


def plan(data, only):
    """([(pair, top-level field, [fields])] that can be copied, [(pair, field, why)] that cannot)."""
    declared = {(e["pair"], e["field"]) for e in data["config"].get("differences", [])}
    pair_ids = dict(pairs(data))
    todo, by_hand = {}, []
    for name, field in differing(data):
        if (name, field) in declared or (only and name not in only):
            continue
        key = top_field(field)
        ids = pair_ids[name]
        if key == DEFAULT:
            by_hand.append((name, field, "a test-data default; change it by hand (tools/defaults_guard.mjs)"))
        elif key.startswith(BANK) and not all(i in data["bank"] for i in ids.values()):
            by_hand.append((name, field, "one side has no question bank entry; add or remove the entry by hand"))
        elif not all(i in data["lines"] for i in ids.values()):
            by_hand.append((name, field, "one side has no such line"))
        elif any(n == name and top_field(f) == key for n, f in declared):
            by_hand.append((name, field, f"{key} also holds a declared difference, which a copy would overwrite; edit it by hand"))
        else:
            todo.setdefault((name, key), []).append(field)
    return [(name, key, fields) for (name, key), fields in todo.items()], by_hand


def copy_tree(root, year, dest):
    """Copy the files the check reads into `dest`, laid out as under `root`."""
    for path in files(root, year, read_config(root, year)):
        target = Path(dest) / path.relative_to(root)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)


def sync(root, year, source, only, write, out=print):
    """Show, and with `write` make, the copies from side `source` that remove undeclared differences. Returns the exit status."""
    data = load(root, year)
    sides = data["config"]["sides"]
    if source not in sides:
        out(f"twins: --sync-from takes one of: {', '.join(sides)}")
        return 2
    target = sides[1 - sides.index(source)]
    pair_ids = dict(pairs(data))
    todo, by_hand = plan(data, only)
    for name, field, why in by_hand:
        out(f"twins: {name}, field {field}: not copied: {why}")
    if not todo:
        out("twins: nothing to copy" if not by_hand else "twins: nothing else to copy")
        return 1 if by_hand else 0
    with tempfile.TemporaryDirectory() as tmp:
        copy_tree(root, year, tmp)
        allowed = set()
        for name, key, _ in todo:
            src_id, dst_id = pair_ids[name][source], pair_ids[name][target]
            if key.startswith(BANK + "."):
                args = (bank_path(tmp, year), "input", src_id, dst_id, key.split(".", 1)[1], bank_path(tmp, year))
                allowed.add(("bank", dst_id, key.split(".", 1)[1]))
            else:
                args = (form_path(tmp, year, dst_id.split(".", 1)[0]), "id", src_id, dst_id, key, form_path(tmp, year, src_id.split(".", 1)[0]))
                allowed.add(("lines", dst_id, key))
            error = copy_field(*args, (source, target))
            if error:
                out(f"twins: {name}, field {key}: not copied: {error}")
                return 1
        try:
            after = load(tmp, year)
        except yaml.YAMLError as e:
            out(f"twins: the copy does not parse ({e}); nothing written")
            return 1
        error = unintended(data, after, allowed) or next(
            (f"{name}, field {f} still differs after the copy" for (name, f) in differing(after) for n, key, fields in todo if n == name and f in fields), None)
        if error:
            out(f"twins: {error}; nothing written. Edit the field by hand.")
            return 1
        changed = []
        for path in files(root, year, data["config"]):
            new = Path(tmp) / path.relative_to(root)
            old_text, new_text = path.read_text(encoding="utf-8"), new.read_text(encoding="utf-8")
            if old_text != new_text:
                rel = str(path.relative_to(root))
                out("".join(difflib.unified_diff(old_text.splitlines(True), new_text.splitlines(True), rel, f"{rel} (from {source})", n=1)).rstrip("\n"))
                changed.append((path, new_text))
        if write:
            for path, text in changed:
                path.write_text(text, encoding="utf-8")
        out(f"twins: {len(todo)} field(s) {'copied' if write else 'would be copied (pass --write)'} from {source} to {target}, in {len(changed)} file(s)")
    return 1 if by_hand else 0


def unintended(before, after, allowed):
    """A message if `after` differs from `before` anywhere but the top-level fields in `allowed`."""
    for kind, start in (("lines", "id"), ("bank", "input")):
        if list(before[kind]) != list(after[kind]):
            return f"the copy changed which {kind} exist"
        for ident, entry in before[kind].items():
            new = after[kind][ident]
            for key in list(entry) + [k for k in new if k not in entry]:
                if entry.get(key, MISSING) != new.get(key, MISSING) and (kind, ident, key) not in allowed:
                    return f"the copy changed {ident} {key}, which it was not copying"
    for doc, form in before["forms"].items():
        strip = lambda f: {k: v for k, v in next(iter(f.values())).items() if k != "lines"}  # noqa: E731
        if strip(form) != strip(after["forms"][doc]):
            return f"the copy changed {doc}'s header"
    return None


# --self-test: each kind of drift, planted on a copy of the year's data.

def set_path(obj, path, value):
    """Set the leaf at a flat field path (label, expr.alternatives[0].then) of a parsed line."""
    tokens = [int(t[1:-1]) if t.startswith("[") else t for t in re.findall(r"[^.\[\]]+|\[\d+\]", path)]
    for token in tokens[:-1]:
        obj = obj[token]
    obj[tokens[-1]] = value


def self_test():
    base = load()
    assert not problems(base), "self-test: the year's data must pass the check before drift is planted"
    config = base["config"]
    left, right = config["sides"]
    declared_pairs = {e["pair"] for e in config["differences"]}
    block = [(n, ids) for n, ids in pairs(base) if n not in {r["pair"] for r in config.get("readers", [])}]
    clean = [(n, ids) for n, ids in block if n not in declared_pairs]

    def first(test, what):
        found = next(((n, ids) for n, ids in clean if test(base["lines"][ids[left]], ids)), None)
        assert found, f"self-test: no pair without declared differences {what}"
        return found

    asked = first(lambda line, ids: line["expr"].get("op") == "input" and all(i in base["bank"] and i in base["defaults"] for i in ids.values()),
                  "is an asked input with bank entries and defaults")
    computed = first(lambda line, ids: line["expr"].get("op") == "choose", "is a choose")
    gated = first(lambda line, ids: "shown_when" in line, "has shown_when")
    refusing = first(lambda line, ids: line.get("refuses"), "has a refusal")

    def ref_field(line, side):
        return next(f for f, v in flatten(line["expr"], "expr", {}).items() if isinstance(v, str) and v.startswith(side + "."))

    cases = []

    def case(name, mutate, *expected):
        data = copy.deepcopy(base)
        mutate(data)
        found = problems(data)
        hit = next((p for p in found if all(e in p for e in expected)), None)
        assert hit, f"self-test: {name}: expected a problem containing {expected}, got {found}"
        cases.append(name)
        print(f"-- {name}\n{hit}")

    def line(data, pair, side):
        return data["lines"][pair[1][side]]

    case("an operand changed on one side",
         lambda d: set_path(line(d, computed, right), ref_field(line(d, computed, right), right), f"{right}.twin_self_test"),
         computed[0], "field expr.", "not declared", f"{left}.", f"{right}.twin_self_test")
    case("a question reworded on one side",
         lambda d: set_path(line(d, asked, left), "expr.source", line(d, asked, left)["expr"]["source"] + " Reworded."),
         asked[0], "field expr.source", "not declared", "Reworded.")
    case("a citation changed on one side",
         lambda d: set_path(line(d, asked, right), "cite.locator", line(d, asked, right)["cite"]["locator"] + "; p. 99"),
         asked[0], "field cite.locator", "not declared", "; p. 99")
    case("a label changed on one side", lambda d: set_path(line(d, computed, right), "label", "Another label"),
         computed[0], "field label", "not declared", "Another label")
    case("a type changed on one side", lambda d: set_path(line(d, asked, left), "type", "Text"), asked[0], "field type", "not declared")
    case("a shown_when changed on one side", lambda d: set_path(line(d, gated, right), "shown_when", f"{right}.twin_self_test"),
         gated[0], "field shown_when", "not declared")
    case("a shown_when dropped on one side", lambda d: line(d, gated, right).pop("shown_when"), gated[0], "field shown_when", "(absent)")
    case("a refusal's text changed on one side", lambda d: set_path(line(d, refusing, left), "refuses[0].remedy", "Another remedy."),
         refusing[0], "field refuses[0].remedy", "not declared", "Another remedy.")
    case("a refusal's gate changed on one side", lambda d: set_path(line(d, refusing, right), "refuses[0].when", f"{right}.twin_self_test"),
         refusing[0], "field refuses[0].when", "not declared")
    case("a refusal added on one side",
         lambda d: line(d, refusing, right)["refuses"].append({"when": f"{right}.twin_self_test", "form": "Planted", "remedy": "Planted."}),
         refusing[0], "not declared", "Planted")

    def new_line(d):
        d["lines"][f"{left}.edu_twin_self_test"] = {"id": f"{left}.edu_twin_self_test"}
        d["order"][left].append(f"{left}.edu_twin_self_test")
    case("a new line on one side", new_line, f"{left}.edu_twin_self_test has no twin", "not declared one-sided")

    def drop_line(d):
        d["lines"].pop(computed[1][right])
        d["order"][right].remove(computed[1][right])
    case("a line removed from one side", drop_line, f"{computed[1][left]} has no twin", "not declared one-sided")

    entry = next(e for e in config["differences"] if e["pair"] in dict(block) and isinstance(e[left], str) and e["field"].split(".")[0] not in (BANK, DEFAULT))
    ids = dict(block)[entry["pair"]]
    twin_value = re.sub(rf"^{re.escape(left)}\.", f"{right}.", entry[left]) if normalized(entry["field"], entry[left], left) != entry[left] else entry[left]
    case("a declared difference that no longer exists", lambda d: set_path(d["lines"][ids[right]], entry["field"], twin_value),
         entry["pair"], f"field {entry['field']}", "no longer differ", "Remove the entry")
    case("a declared difference whose text changed on one side", lambda d: set_path(d["lines"][ids[left]], entry["field"], entry[left] + " changed"),
         entry["pair"], f"field {entry['field']}", "no longer hold the declared values", " changed")

    lone = next(iter(config["one_sided"]))

    def drop_lone(d):
        d["lines"].pop(lone)
        d["order"][lone.split(".")[0]].remove(lone)
    case("a declared one-sided id that is gone", drop_lone, lone, "declared one-sided but does not exist")

    def twin_lone(d):
        twin = twin_of(lone, config)
        d["lines"][twin] = copy.deepcopy(d["lines"][lone])
        d["order"][twin.split(".")[0]].append(twin)
    case("a declared one-sided id that gained a twin", twin_lone, lone, "declared one-sided but has a twin")
    case("a declaration without a reason", lambda d: d["config"]["differences"][0].pop("reason"), "lacks reason")
    case("a help text changed on one side", lambda d: d["bank"][asked[1][left]].update(help="Another help."),
         asked[0], f"field {BANK}.help", "not declared", "Another help.")
    case("a question bank entry removed on one side", lambda d: d["bank"].pop(asked[1][right]), asked[0], f"field {BANK}.order", "(absent)")
    case("a test-data default changed on one side", lambda d: d["defaults"][asked[1][right]].update(value="planted"),
         asked[0], f"field {DEFAULT}.value", "not declared", "planted")
    assert accepts({"pattern": "p\\. \\d+, .*"}, "p. 3, Line 5") and not accepts({"pattern": "p\\. \\d+"}, "p. 3, Line 5"), "a pattern matches fully"
    assert accepts(None, MISSING) and not accepts(None, "text") and not accepts("text", MISSING), "null declares an absent field"
    if config.get("readers"):
        reader = config["readers"][0]
        case("a reader of the block changed on one side", lambda d: set_path(d["lines"][reader[right]], "cite.locator", "p. 99"),
             reader["pair"], "field cite.locator", "not declared", "p. 99")
        case("a reader ranging over the other side's collection", lambda d: set_path(d["lines"][reader[right]], "expr.collection", left),
             reader["pair"], "field expr.collection", "not declared")

    # --sync-from on a copy of the files: the planted drift is copied away, and declared differences stay.
    quiet = []
    with tempfile.TemporaryDirectory() as tmp:
        copy_tree(ROOT, Y, tmp)

        def edit(path, start_key, ident, change):
            lines = path.read_text(encoding="utf-8").split("\n")
            first_line, end, indent = entry_span(lines, start_key, ident)
            change(lines, first_line, end, {k: (s, e) for k, s, e in chunks(lines, first_line, end, indent)}, indent)
            path.write_text("\n".join(lines), encoding="utf-8")

        target = form_path(tmp, Y, right)

        def plant(lines, first_line, end, at, indent):
            s, e = at["cite"]
            del lines[s:e]                                             # the citation is gone: the copy inserts it
            s, e = at["label"]
            lines[s:e] = [" " * (indent + 2) + "label: A planted label", " " * (indent + 2) + f"ambiguity: {right}.planted"]
        edit(target, "id", computed[1][right], plant)
        edit(bank_path(tmp, Y), "input", asked[1][right],
             lambda lines, f, e, at, indent: lines.__setitem__(slice(*at["help"]), [" " * (indent + 2) + "help: Planted help."]))
        planted = problems(load(tmp, Y))
        fields = sorted(p.split(", field ")[1].split(":")[0] for p in planted)
        assert fields == ["ambiguity", "cite.doc", "cite.locator", f"{BANK}.help", "label"], f"self-test: planted in the files, found {planted}"
        assert sync(tmp, Y, left, None, False, quiet.append) == 0 and len(problems(load(tmp, Y))) == len(planted), "self-test: without --write nothing is written"
        quiet.clear()
        assert sync(tmp, Y, left, None, True, quiet.append) == 0, f"self-test: the copy failed: {quiet}"
        after = load(tmp, Y)
        assert not problems(after), f"self-test: problems remain after the copy: {problems(after)}"
        assert after["lines"] == base["lines"] and after["bank"] == base["bank"], "self-test: the copy did not restore the data"
        print(f"-- --sync-from {left} --write copies a planted label, citation, extra field and help text back\n" + "\n".join(quiet))

        # An undeclared difference inside a field that also holds a declared one is not copied.
        mixed = next(e for e in config["differences"] if e["pair"] in dict(block) and e["field"].startswith("expr.alternatives"))
        mixed_id = dict(block)[mixed["pair"]][right]

        def flip(lines, first_line, end, at, indent):
            s, e = at["expr"]
            i = next(i for i in range(s, e) if lines[i].strip() == "- const: true")
            lines[i] = lines[i].replace("true", "false")
        edit(target, "id", mixed_id, flip)
        text = target.read_text(encoding="utf-8")
        quiet.clear()
        assert sync(tmp, Y, left, None, True, quiet.append) == 1 and target.read_text(encoding="utf-8") == text, "self-test: a declared difference was overwritten"
        assert any("also holds a declared difference" in q for q in quiet), quiet
        print(f"-- --sync-from never copies a field that holds a declared difference\n{quiet[0]}")
    print(f"twins self-test: {len(cases)} planted drifts reported; sync copies and refuses as described")
    return 0


def main(argv):
    if "--self-test" in argv:
        return self_test()
    source, only, write = None, [], False
    i = 0
    while i < len(argv):
        if argv[i] == "--sync-from" and i + 1 < len(argv):
            source = argv[i + 1]; i += 2
        elif argv[i] == "--pair" and i + 1 < len(argv):
            only.append(argv[i + 1]); i += 2
        elif argv[i] == "--write":
            write = True; i += 1
        else:
            sys.exit(f"check_twins: unknown argument {argv[i]!r}\n{__doc__}")
    if source is None and (only or write):
        sys.exit("check_twins: --pair and --write go with --sync-from SIDE")
    if source is not None:
        return sync(ROOT, Y, source, only, write)
    data = load()
    found = problems(data)
    for message in found:
        print(message)
    print(f"twins: {summary(data)}; {len(found)} problem(s)")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
