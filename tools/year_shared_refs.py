#!/usr/bin/env python3
"""The year-shared files that name an id a year's operations remove.

    year_shared_refs.py [--year 2025]     the references, for changes/<year+1> applied to the year's tree
    year_shared_refs.py --self-test

Most of the project's code and tool data serve every tax year: the case generators (tools/engines/generate_cases.py,
engine/src/generate.ts), the mutation pins (engine/src/mutate.ts), the engine adapters (tools/engines/*.py), the
coverage tree (tools/coverage/tree.json). They name line ids of the forms. When the operations of
changes/<year+1>/ remove a line (remove_line), or leave a refusal gate that no refusal uses any more, those files
still name it, and nothing in year_changes.py's dangling rule (which covers the forms, the question bank and the
files under interview/<year>/) sees it. This tool lists every such reference, so the operation lane, or the
adoption lane, decides what each shared file does in the new year (a per-year branch, a skip, a removal once the
old year is retired). It changes nothing: a shared file serves the old year too, and which way it should go is a
judgment.

What is a reference, by strength:

  id        the id itself, `form.local`, not run into a longer id (`f5695.line13` is not read in
            `f5695.line13_positive`); a key such as `operand.f5695.f5695.part1_any.no.then1` holds one
  instance  an instance id, `form[...].local` (`dependent[{k}].edu_tin_issued`, `person[taxpayer].x`)
  local     the line's local name as a quoted string (`"line7a"`) in a file that builds the form's ids from
            names (`f"f5695.{k}"`, `` `f5695.${kind}` ``): a weaker match, for a person to read
  gate      `"gate": "<id>"` (tools/coverage/tree.json) for a line that stays but that no refusal uses after the
            operations (tree.py --check fails on such a placement)

Files read: tools/ and engine/src/, Python, TypeScript, JavaScript, JSON and shell, except files kept per year (a
path part named for a year, such as tools/sources/2025.json), this tool, and the year-change tools whose text names
ids only as examples. Run by year_diff.py --adopt (reports/<to>/shared_refs_from_<from>.{json,md}) and noted by
year_changes.py --check.
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import taxyear  # noqa: E402  (--year, removed from sys.argv here)
import jurisdiction  # noqa: E402  (--jurisdiction ny)

SCAN_DIRS = ("tools", "engine/src")
SUFFIXES = {".py", ".ts", ".js", ".mjs", ".json", ".sh"}
SKIP_PARTS = {"node_modules", "__pycache__", "dist"}
SKIP_FILES = {"tools/year_shared_refs.py", "tools/year_changes.py", "tools/year_diff.py", "tools/year_free_names.json"}
YEAR_PART = re.compile(r"^(?:19|20)\d\d(?:\D|$)")


def shared_files(root=ROOT):
    root = Path(root)
    out = []
    for d in SCAN_DIRS:
        for p in sorted((root / d).rglob("*")):
            rel = p.relative_to(root)
            if (p.is_file() and p.suffix in SUFFIXES and not SKIP_PARTS & set(rel.parts)
                    and rel.as_posix() not in SKIP_FILES and not any(YEAR_PART.match(part) for part in rel.parts)):
                out.append(p)
    return out


def gates_of(forms):
    """The ids a refusal's `when` names, over {form id: [line]}."""
    out = set()
    for lines in forms.values():
        for line in lines:
            for r in line.get("refuses") or []:
                if isinstance(r, dict) and isinstance(r.get("when"), str):
                    out.add(re.sub(r"\[[^\]]*\]", "", r["when"]))
    return out


def lost_ids(tree, r):
    """(ids removed, ids that stop being refusal gates) when the result `r` of year_changes.apply is applied to
    `tree`. A removed id's gate placement is reported with the removal, not again as a lost gate."""
    removed = set(r.removed)
    before = gates_of({fid: f["doc"].get("lines") or [] for fid, f in tree.forms.items()})
    after = gates_of({fid: f["lines"] for fid, f in r.state.forms.items()})
    return removed, (before - after) - removed


def scan(removed, lost_gates, files, root=ROOT):
    """[(file, line number, id, strength, the line)] for every reference in `files` to an id of `removed`, and
    every coverage-tree placement of a gate in `lost_gates`."""
    root = Path(root)
    if not removed and not lost_gates:
        return []
    by_form = {}
    for i in sorted(removed):
        form, _, local = i.partition(".")
        by_form.setdefault(form, []).append(local)
    alt = "|".join(sorted({re.escape(f) for f in by_form}, key=len, reverse=True)) or "(?!)"
    ref = re.compile(rf"(?<![\w$])({alt})(\[[^\]\n]*\])?\.([A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)*)")
    gate = re.compile(r'"gate"\s*:\s*"([^"]+)"')
    out = []
    for p in files:
        text = p.read_text(encoding="utf-8", errors="replace")
        rel = p.relative_to(root).as_posix()
        templated = {f for f in by_form if re.search(rf"(?<![\w$]){re.escape(f)}\.(?:\{{|\$\{{)", text)}
        locals_re = {f: re.compile(r"""(["'])(""" + "|".join(map(re.escape, sorted(by_form[f], key=len, reverse=True)))
                                   + r")\1") for f in templated}
        for n, line in enumerate(text.split("\n"), 1):
            seen = set()
            for m in ref.finditer(line):
                form, inst, tail = m.group(1), m.group(2), m.group(3)
                parts = tail.split(".")
                # the longest dotted prefix that is a removed local (a key may run on past the id: .no.then1)
                hit = next((".".join(parts[:k]) for k in range(len(parts), 0, -1)
                            if ".".join(parts[:k]) in by_form[form]), None)
                if hit is None:
                    continue
                key = (f"{form}.{hit}", "instance" if inst else "id")
                if key not in seen:
                    seen.add(key)
                    out.append((rel, n, key[0], key[1], line.strip()))
            for f, lre in locals_re.items():
                for m in lre.finditer(line):
                    key = (f"{f}.{m.group(2)}", "local")
                    if key not in seen and (key[0], "id") not in seen and (key[0], "instance") not in seen:
                        seen.add(key)
                        out.append((rel, n, key[0], "local", line.strip()))
            for m in gate.finditer(line):
                if m.group(1) in lost_gates:
                    out.append((rel, n, m.group(1), "gate", line.strip()))
    return out


def references(tree, r, root=ROOT):
    removed, lost_gates = lost_ids(tree, r)
    return scan(removed, lost_gates, shared_files(root), root)


def write_report(refs, from_year, to_year, out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = out_dir / f"shared_refs_from_{from_year}"
    rows = [{"file": f, "line": n, "id": i, "strength": s, "text": t} for f, n, i, s, t in refs]
    stem.with_suffix(".json").write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [f"# Year-shared files naming ids the {to_year} operations remove", "",
             f"Generated by `tools/year_shared_refs.py`: {len(rows)} reference(s) in code and tool data kept for every "
             f"year (not under a year directory) to a line that changes/{to_year}/ removes from the {from_year} "
             "definitions, or to a refusal gate no refusal uses after them. Each shared file serves both years; decide "
             "per file what it does for each.", ""]
    for f in sorted({r["file"] for r in rows}):
        mine = [r for r in rows if r["file"] == f]
        lines += [f"## `{f}` ({len(mine)})", ""]
        lines += [f"- line {r['line']}, {r['strength']} `{r['id']}`: `{r['text'][:140]}`" for r in mine] + [""]
    stem.with_suffix(".md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return stem


# ---------- self-test ----------

def self_test():
    """Plant each kind of reference in a scratch tree and check what is found and what is not."""
    import tempfile
    from types import SimpleNamespace as NS
    files = {
        "tools/engines/gen.py": (
            'inputs["fx.gone"] = 1\n'                                  # 1 id
            'inputs["fx.gone_too_long"] = 1\n'                         # 2 a longer id: not a reference
            'inputs[f"dep[{k}].tin"] = True\n'                         # 3 instance
            'for k in ("gone", "kept"):\n'                             # 4 local (the file templates fx.)
            '    inputs.setdefault(f"fx.{k}", False)\n'                # 5
            'x = "fy.gone"\n'),                                        # 6 another form's same local: not removed
        "engine/src/mutate.ts": '  "operand.fx.fx.gone.no.then1": pinned("...", ["fx.kept", "fx.gone"]),\n',
        "engine/src/plain.ts": 'const k = "gone";\n',                  # no fx. template here: not a reference
        "tools/coverage/tree.json": '{"gate": "fx.gate_only", "topic": "t"},\n{"gate": "fx.still_gate"},\n',
        "tools/sources/2025.json": '"fx.gone"\n',                       # kept per year: not read
    }
    forms_before = {"fx": [{"id": "fx.gone"}, {"id": "fx.kept"}, {"id": "fx.gate_only"}, {"id": "fx.still_gate"},
                           {"id": "fx.r", "refuses": [{"when": "fx.gate_only"}, {"when": "fx.still_gate"}]}],
                    "dep": [{"id": "dep.tin"}]}
    forms_after = {"fx": [{"id": "fx.kept"}, {"id": "fx.gate_only"}, {"id": "fx.still_gate"},
                          {"id": "fx.r", "refuses": [{"when": "fx.still_gate"}]}], "dep": []}
    tree = NS(forms={k: {"doc": {"lines": v}} for k, v in forms_before.items()})
    r = NS(removed={"fx.gone": None, "dep.tin": None},
           state=NS(forms={k: {"lines": v} for k, v in forms_after.items()}))
    with tempfile.TemporaryDirectory() as tmp:
        for rel, text in files.items():
            (Path(tmp) / rel).parent.mkdir(parents=True, exist_ok=True)
            (Path(tmp) / rel).write_text(text, encoding="utf-8")
        got = {(f, n, i, s) for f, n, i, s, _ in references(tree, r, tmp)}
        stem = write_report(references(tree, r, tmp), 2025, 2026, Path(tmp) / "reports")
        written = json.loads(stem.with_suffix(".json").read_text())
    want = {("tools/engines/gen.py", 1, "fx.gone", "id"), ("tools/engines/gen.py", 3, "dep.tin", "instance"),
            ("tools/engines/gen.py", 4, "fx.gone", "local"), ("engine/src/mutate.ts", 1, "fx.gone", "id"),
            ("tools/coverage/tree.json", 1, "fx.gate_only", "gate")}
    ok = got == want and len(written) == len(want)
    print("year-shared-refs self-test: an id, an instance id, a templated local name, a mutation key and a lost gate "
          "found; a longer id, another form's local, an untemplated local, a gate still used and a per-year file "
          "not: " + ("as expected" if ok else f"WRONG\n  missed {sorted(want - got)}\n  extra {sorted(got - want)}"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        sys.exit(self_test())
    import year_changes
    year = int(taxyear.Y)
    status, r = year_changes.check(year, quiet=True)
    if r.state is None:
        sys.exit("year-shared-refs: the operations did not apply; run year_changes.py --check")
    refs = references(year_changes.year_tree(year), r)
    stem = write_report(refs, year, year + 1, jurisdiction.ypath("reports", year + 1))
    for f, n, i, s, t in refs:
        print(f"{f}:{n}: {s} {i}")
    print(f"year-shared-refs: {len(refs)} reference(s) to ids the {year + 1} operations remove "
          f"({stem.relative_to(ROOT)}.md)")


if __name__ == "__main__":
    main()
