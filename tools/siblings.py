#!/usr/bin/env python3
"""List the fix-sibling set of changed lines, and the ripple of a new input.

A fix-sibling is another line or question that shares the changed rule but was not changed:
a reader of the same input or gate (through helper lines), a predicate testing the same enum
value, a line or question whose citation anchors the same (document, page, heading), or, for
a Form 8863 Part III line (person.edu* or dependent.edu*), its twin in the other student block. The
2026-10-29 root-cause analysis (P3) found nine bugs where the reported instance was fixed and
its siblings were not.

    siblings.py <line id> [<line id> ...]      print the sibling set
    siblings.py --input <input id>              print where a new input must be added
    siblings.py --check                         validate the bug entries' Siblings checked field
    siblings.py --self-test

`--check` requires every new bug entry (BUG-0290 onward) that has a Fix field to name its
Fix lines and the generated Siblings checked set; it does not grandfather older entries.
The review-refresh half of T-150 (fail check-all when a sibling form's logs were not rerun)
is `--reviews-since <rev>`: it reports sibling forms with no review log changed since <rev>.
"""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from taxyear import Y  # noqa: E402
import citations  # noqa: E402

CANON = ROOT / "canonical" / Y
BUGS = Path(os.environ.get("SIBLINGS_BUGS", ROOT / "BUG_INVENTORY.md"))
ENTRY_RE = re.compile(r"^## (BUG-(\d{4})) — (.*)$", re.M)
REQUIRED_FROM = 290


def load_docs():
    docs = {}
    for path in sorted(CANON.glob("*.json")):
        raw = json.loads(path.read_text(encoding="utf-8"))
        doc = raw.get("form") or raw.get("def")
        if doc:
            docs[doc["id"]] = doc
    return docs


def walk_strings(value, out):
    if isinstance(value, str):
        out.append(value)
    elif isinstance(value, dict):
        for v in value.values():
            walk_strings(v, out)
    elif isinstance(value, list):
        for v in value:
            walk_strings(v, out)


def line_refs(docs, line):
    """Strings in the line's expression or refusal gates that name a line in these documents."""
    raw = []
    walk_strings(line.get("expr"), raw)
    for refusal in line.get("refuses") or []:
        if refusal.get("when"):
            raw.append(refusal["when"])
    return sorted({r for r in raw if any(r in d.get("_ids", set()) for d in docs.values())})


def index(docs):
    ids = {}
    for doc in docs.values():
        doc["_ids"] = {line["id"] for line in doc.get("lines", [])}
        for line in doc.get("lines", []):
            ids[line["id"]] = (doc, line)
    return ids


def readers(docs, ids):
    out = {}
    for doc in docs.values():
        for line in doc.get("lines", []):
            for ref in line_refs(docs, line):
                out.setdefault(ref, set()).add(line["id"])
    return out


def leaves(docs, ids, target, seen=None):
    """The input or gate lines a changed line directly reads.

    A rule input is its own leaf. A computed line contributes the input and gate lines it
    reads; recursing through every computed operand would pull in unrelated inputs and the
    whole return, which is not a sibling set."""
    if target not in ids:
        return {target}
    doc, line = ids[target]
    if (line.get("expr") or {}).get("op") == "input" or line.get("printed") in ("(gate)", "(screen)"):
        return {target}
    out = set()
    for ref in line_refs(docs, line):
        if ref in ids and ids[ref][0] is doc:
            ref_line = ids[ref][1]
            if (ref_line.get("expr") or {}).get("op") == "input" or ref_line.get("printed") in ("(gate)", "(screen)"):
                out.add(ref)
    return out or {target}


# Form 8863 Part III is written twice, for a filer or spouse (person.edu*) and for a dependent
# (dependent.edu*), line for line; a change to one block is checked on its twin in the other.
EDU_TWIN = re.compile(r"^(person|dependent)\.(edu(?:_\w+)?)$")


def edu_twin(ids, target):
    """The same Form 8863 Part III line in the other student block, if it has one."""
    m = EDU_TWIN.match(target)
    if not m:
        return None
    twin = f"{'dependent' if m.group(1) == 'person' else 'person'}.{m.group(2)}"
    return twin if twin in ids else None


def siblings_of(docs, ids, target, reader_map):
    found = set()
    for leaf in leaves(docs, ids, target):
        found |= reader_map.get(leaf, set())
    twin = edu_twin(ids, target)
    if twin:
        found.add(twin)
    found.discard(target)
    return found


def enum_predicates(docs, ids, target):
    """(line id, compared constant) for every test that compares `target` to a constant."""
    out = []
    def walk(value, owner):
        if isinstance(value, dict):
            if value.get("op") == "test":
                for key in ("eq", "ne", "lt", "le", "gt", "ge"):
                    pair = value.get(key)
                    if isinstance(pair, list) and len(pair) == 2:
                        for a, b in (pair, pair[::-1]):
                            if a == target and isinstance(b, dict) and "const" in b:
                                out.append((owner, str(b["const"])))
            for v in value.values():
                walk(v, owner)
        elif isinstance(value, list):
            for v in value:
                walk(v, owner)
    for doc in docs.values():
        for line in doc.get("lines", []):
            walk(line.get("expr"), line["id"])
            for refusal in line.get("refuses") or []:
                walk(refusal.get("when"), line["id"])
    return sorted(set(out))


def anchors(line):
    out = set()
    cites = [line.get("cite")] + [r.get("cite") for r in line.get("refuses") or []]
    for cite in cites:
        if not cite or not cite.get("doc") or not cite.get("locator"):
            continue
        try:
            for doc, pages, anchor, _quotes, _span in citations.segments(cite["doc"], cite["locator"]):
                if pages and anchor:
                    out.add((doc, tuple(pages), anchor))
        except Exception:
            continue
    return out


def anchor_index(docs):
    out = {}
    for doc in docs.values():
        for line in doc.get("lines", []):
            for key in anchors(line):
                out.setdefault(key, set()).add(line["id"])
    questions = []
    for path in sorted((ROOT / "interview").glob(f"questions-{Y}.yaml")):
        import yaml
        bank = yaml.safe_load(path.read_text(encoding="utf-8"))
        for q in (bank.get("bank") or {}).get("questions") or []:
            cite = q.get("cite")
            if not cite or not cite.get("locator"):
                continue
            try:
                for doc, pages, anchor, _quotes, _span in citations.segments(cite.get("doc", ""), cite["locator"]):
                    if pages and anchor:
                        out.setdefault((doc, tuple(pages), anchor), set()).add(f"question:{q['input']}")
            except Exception:
                continue
    return out


def print_set(title, ids, limit):
    ids = sorted(ids)
    print(f"\n{title} ({len(ids)})")
    for item in ids[:limit]:
        print(f"  {item}")
    if len(ids) > limit:
        print(f"  ... and {len(ids) - limit} more")


def report(docs, ids, targets, anchor_map, limit):
    reader_map = readers(docs, ids)
    for target in targets:
        if target not in ids:
            print(f"{target}: not a line in canonical/{Y}")
            continue
        doc, line = ids[target]
        print(f"\n## {target} — {line.get('label', '')}")
        found = {}
        found["readers"] = siblings_of(docs, ids, target, reader_map)
        found["enum values"] = {f"{owner} = {value}" for owner, value in enum_predicates(docs, ids, target)}
        target_anchors = anchors(line)
        anchor_hits = set()
        for key in target_anchors:
            anchor_hits |= anchor_map.get(key, set())
        found["same anchor"] = anchor_hits - {target}
        print_set("(a) lines that read it, through helpers (and its Form 8863 Part III twin)", found["readers"], limit)
        print_set("(c) predicates testing the same enum values", found["enum values"], limit)
        print_set("(b) lines and questions anchored on the same doc/page/heading", found["same anchor"], limit)


def input_ripple(key):
    """Where a new input must be added: forms, questions, fixtures, generators, contracts."""
    stem = key.split("[")[0]
    paths = [
        ("forms", ROOT / "forms" / Y),
        ("interview", ROOT / "interview"),
        ("fixtures", ROOT / "fixtures" / Y),
        ("generator", ROOT / "engine" / "src" / "generate.ts"),
        ("engine cases", ROOT / "tools" / "engines" / "generate_cases.py"),
        ("input contracts", ROOT / "tools" / "transcription" / "input_contracts"),
        ("classm jobs", ROOT / ".classm"),
    ]
    print(f"Ripple for {key!r} (search stem {stem!r}):")
    for label, path in paths:
        hits = []
        files = [path] if path.is_file() else sorted(p for p in path.rglob("*") if p.is_file()) if path.exists() else []
        for file in files:
            try:
                text = file.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            if stem in text:
                hits.append(str(file.relative_to(ROOT)))
        print(f"  {label:14} {len(hits):4} file(s)" + (": " + ", ".join(hits[:4]) + (" ..." if len(hits) > 4 else "") if hits else ""))
    print("  checklist: form line + input question + interview profile + fixtures (all stages) +")
    print("             engine/src/generate.ts + tools/engines/generate_cases.py + input_contracts + classm jobs")


def bug_entries():
    text = BUGS.read_text(encoding="utf-8")
    marks = list(ENTRY_RE.finditer(text))
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        body = text[m.end():end]
        fields = {}
        for field in ("Fix", "Fix lines", "Siblings checked"):
            hit = re.search(rf"^- \*\*{re.escape(field)}:\*\* (.*)$", body, re.M)
            if hit:
                fields[field] = hit.group(1).strip()
        yield m.group(1), int(m.group(2)), m.group(3), fields


def checked_ids(text):
    if not text:
        return set()
    if re.search(r"\bnone\b", text, re.I):
        return set()
    return set(re.findall(r"`([a-zA-Z0-9_.\[\]-]+)`", text)) | set(re.findall(r"\b([a-z][a-zA-Z0-9_]*(?:\.[a-zA-Z0-9_]+)+)\b", text))


def entry_base(bug, head_text):
    """The revision the entry's change is measured from: HEAD for an uncommitted entry,
    else the parent of the commit that added it."""
    if f"## {bug} " not in head_text:
        return "HEAD"
    out = subprocess.run(["git", "log", "-1", "--format=%H", "-S", f"## {bug} ", "--",
                          str(BUGS.relative_to(ROOT))], capture_output=True, text=True, check=False).stdout.strip()
    return f"{out}^" if out else "HEAD"


def line_ids_at(rev):
    """Line ids declared in the year's forms at revision `rev`."""
    out = subprocess.run(["git", "grep", "-h", "-o", "-E", r"- id: [A-Za-z0-9_.]+", rev, "--", f"forms/{Y}"],
                         capture_output=True, text=True, check=False).stdout
    return {line.split("id: ", 1)[1] for line in out.splitlines() if "id: " in line}


def changed_logs(base):
    changed = subprocess.run(["git", "diff", "--name-only", base, "--",
                              f"reviews/{Y}/transcription", f"reviews/{Y}/render",
                              f"reviews/ny/{Y}/transcription", f"reviews/ny/{Y}/render"],
                             capture_output=True, text=True, check=False).stdout
    forms = set()
    for path in changed.splitlines():
        name = Path(path).name
        if name.endswith(".index.json"):  # a review in the review store (tools/transcription/review_store.py)
            stem = name[:-len(".index.json")]
        elif name.endswith(".md"):  # a review log committed before the store
            stem = name[:-3]
        else:
            continue
        if stem.endswith(".deepseek"):
            stem = stem[: -len(".deepseek")]
        forms.add(stem.split(".")[0])
    return forms


def check(docs, ids):
    reader_map = readers(docs, ids)
    problems = []
    head_text = subprocess.run(["git", "show", "HEAD:BUG_INVENTORY.md"], capture_output=True, text=True, check=False).stdout
    logged = {}
    existed = {}
    for bug, number, title, fields in bug_entries():
        if number < REQUIRED_FROM or "Fix" not in fields:
            continue
        if "Fix lines" not in fields:
            problems.append(f"{bug}: has a Fix field but no '- **Fix lines:**' list")
            continue
        if "Siblings checked" not in fields:
            problems.append(f"{bug}: has a Fix field but no '- **Siblings checked:**' field")
            continue
        fix = checked_ids(fields["Fix lines"]) & set(ids)
        if not fix:
            problems.append(f"{bug}: Fix lines names no line in canonical/{Y}")
            continue
        siblings = set()
        for target in fix:
            siblings |= siblings_of(docs, ids, target, reader_map)
        checked = checked_ids(fields["Siblings checked"])
        unknown = checked - set(ids)
        if unknown:
            problems.append(f"{bug}: Siblings checked names unknown line(s): {', '.join(sorted(unknown))}")
        base = entry_base(bug, head_text)
        missing = siblings - checked
        if base != "HEAD":
            # A committed entry cannot be edited (the inventory is append-only), so a sibling
            # line added after it was written is not counted against it.
            if base not in existed:
                existed[base] = line_ids_at(base[:-1])
            missing &= existed[base]
        if missing:
            problems.append(f"{bug}: Siblings checked omits {len(missing)} generated sibling(s): "
                            f"{', '.join(sorted(missing)[:8])}{' ...' if len(missing) > 8 else ''}")
        if base not in logged:
            logged[base] = changed_logs(base)
        forms = {target.split(".")[0] for target in siblings}
        unrefreshed = sorted(forms - logged[base])
        if unrefreshed:
            problems.append(f"{bug}: no review log changed since {base} for sibling form(s): "
                            f"{', '.join(unrefreshed)}")
    if problems:
        print("siblings: bug-entry problems", file=sys.stderr)
        for p in problems:
            print(f"  {p}", file=sys.stderr)
        return 1
    print(f"siblings: bug entries from BUG-{REQUIRED_FROM:04d} with a Fix field name their generated siblings")
    return 0


def reviews_since(docs, ids, rev):
    """Report sibling forms whose transcription or render logs did not change since `rev`."""
    reader_map = readers(docs, ids)
    forms = set()
    for target in ids:
        forms.add(target.split(".")[0])
    changed = subprocess.run(["git", "diff", "--name-only", rev], capture_output=True, text=True, check=False).stdout
    refreshed = set(re.findall(r"reviews/\d+/(?:transcription|render)/[^/]*?([a-z0-9_]+)(?:\.deepseek)?(?:\.index\.json|\.md)", changed))
    missing = sorted(f for f in forms if f not in refreshed)
    if missing:
        print(f"siblings: no review log changed since {rev} for: {', '.join(missing)}", file=sys.stderr)
        return 1
    print(f"siblings: every sibling form has a review log changed since {rev}")
    return 0


def self_test(docs, ids):
    reader_map = readers(docs, ids)
    eic = siblings_of(docs, ids, "sa.dependent", reader_map)
    assert "eic.step4" in eic, "sa.dependent should reach eic.step4"
    assert "sa.standard" in eic, "sa.dependent should reach sa.standard"
    assert "dependent.edu_line31" in siblings_of(docs, ids, "person.edu_line31", reader_map), "person.edu_line31's twin"
    assert "person.edu" in siblings_of(docs, ids, "dependent.edu", reader_map), "dependent.edu's twin"
    assert edu_twin(ids, "person.educator_expenses") is None and edu_twin(ids, "person.edu_kid") is None, "no twin"
    assert any(q for q in anchor_index(docs).values() if any(x.startswith("question:") for x in q)), "question anchors"
    assert "household.community_property" in anchor_index(docs).get(
        ("i1040gi", (23,), "Community Property States"), set()), "f1040.line1a's community-property anchor"
    if check(docs, ids) != 0:
        raise SystemExit("siblings self-test: bug-entry check failed")
    print("siblings self-test: ok")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("lines", nargs="*", help="line ids whose sibling set to list")
    ap.add_argument("--input", help="input id whose ripple to list")
    ap.add_argument("--check", action="store_true", help="validate the bug entries' Siblings checked field")
    ap.add_argument("--reviews-since", metavar="REV", help="report sibling forms with no review log changed since REV")
    ap.add_argument("--limit", type=int, default=40, help="maximum ids printed per section (default 40)")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    docs = load_docs()
    ids = index(docs)
    if a.self_test:
        self_test(docs, ids)
        return
    if a.input:
        input_ripple(a.input)
        return
    if a.check:
        raise SystemExit(check(docs, ids))
    if a.reviews_since:
        raise SystemExit(reviews_since(docs, ids, a.reviews_since))
    if not a.lines:
        ap.error("give at least one line id, or --input, --check or --self-test")
    report(docs, ids, a.lines, anchor_index(docs), a.limit)


if __name__ == "__main__":
    main()
