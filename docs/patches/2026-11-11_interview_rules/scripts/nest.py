#!/usr/bin/env python3
"""Rewrite a conjunction line as a nested choose on its operands in their original order (the gate-wave convention:
BUG-0471, BUG-0492, docs/2026-11-06_formal_gates_design.md "Leaking conjunctions are rewritten as nested choose").

    python3 -I nest.py <repo> <line id> [<line id> ...]      (scratch copies only)

A line `all(t1, ..., tn)` becomes   choose{ g1 -> <rest>; not g1 -> <doc>.no }   and `any(t1, ..., tn)` becomes
choose{ g1 -> <g1's line>; not g1 -> <rest> }, where g1 is t1's own Bool line when t1 is `<Bool line> = true|false`, and
otherwise a new helper line `<line>_test<i>` holding t1. `<rest>` is the last operand's line, or a helper
`<line>_from<i>` built the same way. A false helper `<doc>.no` (parameter household.no) is added where the document has
none. Helper lines go at the end of the document's lines, each with the rewritten line's citation. The edit is textual,
so comments and anchors elsewhere in the file are untouched.
"""
import pathlib
import re
import sys

import yaml

repo = pathlib.Path(sys.argv[1])
FORMS = sorted((repo / "forms" / "2025").glob("*.yaml"))


def find(line_id):
    pat = re.compile(r"^(\s*)- id: " + re.escape(line_id) + r"\s*$", re.M)
    for f in FORMS:
        text = f.read_text(encoding="utf-8")
        m = pat.search(text)
        if m:
            return f, text, m
    return None, None, None


def block_of(lines, start, indent):
    """[start, end) of the list item starting at `start` whose dash is at `indent`."""
    end = start + 1
    while end < len(lines):
        s = lines[end]
        if s.strip() and (len(s) - len(s.lstrip())) <= indent:
            break
        end += 1
    return end


def key_block(lines, start, end, indent, key):
    """[a, b) of `key:` at column indent+2 inside the item."""
    col = indent + 2
    a = next((i for i in range(start, end) if lines[i].startswith(" " * col + key + ":") or (i == start and False)), None)
    if a is None:
        return None
    b = a + 1
    while b < end and (not lines[b].strip() or (len(lines[b]) - len(lines[b].lstrip())) > col or lines[b].lstrip().startswith("- ") and (len(lines[b]) - len(lines[b].lstrip())) == col):
        b += 1
    return a, b


def scalar(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_.]*", v) and v not in ("true", "false", "null", "yes", "no", "on", "off"):
        return v
    return '"' + v.replace("\\", "\\\\").replace('"', '\\"') + '"'


def emit(node, col):
    """YAML lines for a mapping or list at column `col`."""
    out = []
    pad = " " * col
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(v, (dict, list)):
                out.append(f"{pad}{k}:")
                out.extend(emit(v, col + 2 if isinstance(v, dict) else col))
            else:
                out.append(f"{pad}{k}: {scalar(v)}")
    else:
        for v in node:
            if isinstance(v, (dict, list)):
                sub = emit(v, col + 2)
                out.append(pad + "- " + sub[0].lstrip())
                out.extend(sub[1:])
            else:
                out.append(f"{pad}- {scalar(v)}")
    return out


def rewrite(line_id):
    f, text, m = find(line_id)
    if not f:
        sys.exit(f"nest: no line {line_id}")
    doc = yaml.safe_load(text)
    root = doc.get("form") or doc.get("def") or doc
    by_id = {l["id"]: l for l in root["lines"]}
    line = by_id[line_id]
    expr = line["expr"]
    if expr.get("op") != "test" or not ("all" in expr or "any" in expr):
        sys.exit(f"nest: {line_id} is not an all/any test: {expr.get('op')}")
    kind = "all" if "all" in expr else "any"
    tests = expr[kind]
    doc_id = root["id"]
    indent = len(m.group(1))
    lines = text.split("\n")
    start = text[: m.start()].count("\n")
    end = block_of(lines, start, indent)
    ea, eb = key_block(lines, start, end, indent, "expr")
    cite = key_block(lines, start, end, indent, "cite")
    ca, cb = cite
    head = lines[ca].strip()
    anchor = re.match(r"cite: [&*](\S+)", head)
    cite_lines = [" " * (indent + 2) + f"cite: *{anchor.group(1)}"] if anchor else lines[ca:cb]
    while cite_lines and not cite_lines[-1].strip():
        cite_lines.pop()
    helpers = []  # (id, label, expr)
    label = " ".join(str(line.get("label", line_id)).split())

    def guard_line(i, t):
        """The Bool line a guard on operand i reads, and the constant that makes the operand true."""
        if set(t.keys()) == {"op", "eq"} and isinstance(t["eq"][0], str) and isinstance(t["eq"][1], dict) and isinstance(t["eq"][1].get("const"), bool) and len(t["eq"][1]) == 1:
            ref = t["eq"][0]
            target = by_id.get(ref)
            if target is None or target.get("type") == "Bool":
                return ref, t["eq"][1]["const"]
        hid = f"{line_id}_test{i + 1}"
        helpers.append((hid, f"{label}: condition {i + 1}", t))
        return hid, True

    def is_true(ref, c):
        return {"op": "test", "eq": [ref, {"const": c}]}

    def value_line(i, ref, c):
        """A line whose value is operand i's truth."""
        if c:
            return ref
        hid = f"{line_id}_test{i + 1}"
        if not any(h[0] == hid for h in helpers):
            helpers.append((hid, f"{label}: condition {i + 1}", is_true(ref, False)))
        return hid

    no = f"{doc_id}.no"
    need_no = kind == "all" and no not in by_id

    def chain(i):
        """The expression of all/any over operands i.. (i < n-1)."""
        ref, c = guard_line(i, tests[i])
        if i + 1 == len(tests) - 1:
            r2, c2 = guard_line(i + 1, tests[i + 1])
            rest = value_line(i + 1, r2, c2)
        else:
            rest = f"{line_id}_from{i + 2}"
            helpers.append((rest, f"{label}: conditions {i + 2} to {len(tests)}", chain(i + 1)))
        if kind == "all":
            alts = [{"guard": is_true(ref, c), "then": rest}, {"guard": is_true(ref, not c), "then": no}]
        else:
            alts = [{"guard": is_true(ref, c), "then": value_line(i, ref, c)}, {"guard": is_true(ref, not c), "then": rest}]
        return {"op": "choose", "alternatives": alts}

    new_expr = chain(0)
    col = indent + 2
    new_block = [" " * col + "expr:"] + emit(new_expr, col + 2)
    lines[ea:eb] = new_block
    # the end of the list this item is in: the first later line indented less than the dash
    shift = len(new_block) - (eb - ea)
    k = end + shift
    def in_list(s):
        if not s.strip():
            return True
        ind = len(s) - len(s.lstrip())
        return ind > indent or (ind == indent and (s.lstrip().startswith("- ") or s.lstrip().startswith("#")))
    while k < len(lines) and in_list(lines[k]):
        k += 1
    while k > 0 and not lines[k - 1].strip():
        k -= 1
    add = []
    pad = " " * indent
    if need_no:
        add += [f"{pad}- id: {no}", f"{pad}  printed: (helper)", f"{pad}  label: Year parameter household.no (false)", f"{pad}  type: Bool", f"{pad}  expr:", f"{pad}    op: param", f"{pad}    ref: household.no"] + cite_lines
    for hid, hlabel, hexpr in helpers:
        add += [f"{pad}- id: {hid}", f"{pad}  printed: (helper)", f"{pad}  label: " + '"' + hlabel.replace('\\', '\\\\').replace('"', '\\"') + '"', f"{pad}  type: Bool", f"{pad}  expr:"] + emit(hexpr, indent + 4) + cite_lines
    lines[k:k] = add
    f.write_text("\n".join(lines), encoding="utf-8")
    print(f"nest: {line_id} ({kind} of {len(tests)}) in {f.name}: helpers {', '.join(h[0] for h in helpers) or 'none'}{'; added ' + no if need_no else ''}")
    return [h[0] for h in helpers if h[2].get("op") == "test" and ("all" in h[2] or "any" in h[2])]


# A line id ending in "!" is rewritten at its top level only (its nested all/any operands stay as helper tests).
queue = list(sys.argv[2:])
while queue:
    lid = queue.pop(0)
    more = rewrite(lid.rstrip("!")) or []
    if not lid.endswith("!"):
        queue.extend(more)
