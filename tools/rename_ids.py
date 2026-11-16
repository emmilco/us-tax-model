#!/usr/bin/env python3
"""Rename ids in the data that names lines and inputs by path, and check that no old id is left there.

    rename_ids.py apply [--map MAP] [FILE...] [--year N] [--jurisdiction ny]
    rename_ids.py check [--map MAP] [--year N] [--jurisdiction ny]
    rename_ids.py --self-test                (tools/test_rename_ids.py)

MAP is tools/year_free_names.json unless given: {"renames": {old: {"to": new, "kind": ...}}}, where kind
"document" renames a document; or the map of tools/transcription/rename_carry.py, {old: new} or
{"renames": [{"old": ..., "new": ...}]}.

An id is named in three forms, and each is renamed and checked:
- whole: `doc.local`, not inside a longer id (`x.doc.local`, `doc.local_more` and `doc.local.more` are other
  ids); a sentence's full stop may follow;
- collection-indexed: `doc[entry].local`, alone or as a step of a path (`person[taxpayer].doc[entry].local`);
  rewritten where the document keeps its name, and reported by check where it does not;
- a renamed document's name, wherever it stands as a whole name or a path step: `$doc`, `doc[entry]`,
  `doc.local`, `$x@doc[entry]`.

The places, for the jurisdiction and year (places()):
- fixtures/<year>/, every .json below it (defaults.json included): every line but those of the fields `id`,
  `description` and `evidence_note` (case labels and review records);
- interview/<year>/coverage/ and interview/<year>/personas/, every .yaml line;
- the rulings sidecars of the default review family (reviews/<year>/{transcription,render,classm}/<form>.rulings.json):
  the witnesses of each ruling's triage stamp only, in their input and instance parts (a witness is
  `<kind>:<case id>@<instance>` or `partial:<case id>-<withheld input>@<instance>`; a case id holds no `-`). The
  ruling texts and keys stay as the reviewer saw them; tools/transcription/rename_carry.py re-keys what it proves.

apply rewrites the places, and each FILE given whole, and lists the files it changed. check lists every old id
left in the places, by file and line (or ruling and witness), and exits 1 when there is one. check-all runs check
with the default map for both jurisdictions (the steps renamed_ids and ny_renamed_ids).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools" / "transcription"))

from taxyear import Y  # noqa: E402
import jurisdiction  # noqa: E402

DEFAULT_MAP = ROOT / "tools" / "year_free_names.json"
ID = r"[A-Za-z0-9_]"
# Where a name starts: not inside a longer id, or as a path step after an entry (`].`).
LEAD = r"(?:(?<=\]\.)|(?<![A-Za-z0-9_.]))"
ENTRY = r"(\[[^\]\s]*\])"
SKIP_FIELDS = ("id", "description", "evidence_note")
SKIP_LINE = re.compile(r'^\s*"(?:' + "|".join(SKIP_FIELDS) + r')":')
KINDS = ("transcription", "render", "classm")


def load_map(path=None):
    """({old line id: new line id}, {old document: new document}) of a map file."""
    path = Path(path or DEFAULT_MAP)
    data = json.loads(path.read_text(encoding="utf-8"))
    renames = data.get("renames", data) if isinstance(data, dict) else None
    if isinstance(renames, list):
        renames = {r["old"]: r["new"] for r in renames}
    if not isinstance(renames, dict):
        raise SystemExit(f"{path}: not a rename map")
    lines, documents = {}, {}
    for old, v in renames.items():
        if isinstance(v, dict) and isinstance(v.get("to"), str):
            (documents if v.get("kind") == "document" else lines)[old] = v["to"]
        elif isinstance(v, str):
            lines[old] = v
        else:
            raise SystemExit(f"{path}: the entry {old!r} names no new id")
    return lines, documents


def _alts(names):
    return "|".join(map(re.escape, sorted(names, key=len, reverse=True)))


def _by_doc(mapping):
    """{doc: {local: new local}} of the renames that keep the document, and {doc: {local}} of every old id."""
    keep, every = {}, {}
    for old, new in mapping.items():
        doc, _, local = old.partition(".")
        ndoc, _, nlocal = new.partition(".")
        if not local:
            continue
        every.setdefault(doc, set()).add(local)
        if doc == ndoc and nlocal:
            keep.setdefault(doc, {})[local] = nlocal
    return keep, every


def substituter(mapping, documents=None):
    """A function renaming, in a text, each line id of `mapping` (old -> new) in the whole and the
    collection-indexed forms, and each document of `documents` (old -> new) as a whole name."""
    documents = documents or {}
    subs = []
    keep, _ = _by_doc(mapping)
    for doc, locals_ in sorted(keep.items()):
        rx = re.compile(LEAD + "(" + re.escape(doc) + ")" + ENTRY + r"\.(" + _alts(locals_) + ")(?!" + ID + ")")
        subs.append((rx, lambda m, l=locals_: m.group(1) + m.group(2) + "." + l[m.group(3)]))
    if mapping:
        whole = re.compile(r"(?<![A-Za-z0-9_.])(" + _alts(mapping) + r")(?!" + ID + r"|\." + ID + ")")
        subs.append((whole, lambda m: mapping[m.group(1)]))
    if documents:
        rx = re.compile(LEAD + "(" + _alts(documents) + ")(?!" + ID + ")")
        subs.append((rx, lambda m: documents[m.group(1)]))

    def sub(text):
        for rx, rep in subs:
            text = rx.sub(rep, text)
        return text
    return sub


def finder(mapping, documents=None):
    """A function listing the old ids a text names, in any of the three forms (the collection-indexed form also
    where the rename moves the document)."""
    documents = documents or {}
    rxs = []
    _, every = _by_doc(mapping)
    for doc, locals_ in sorted(every.items()):
        rxs.append((re.compile(LEAD + "(" + re.escape(doc) + ")" + ENTRY + r"\.(" + _alts(locals_) + ")(?!" + ID + ")"),
                    lambda m: m.group(1) + "." + m.group(3)))
    if mapping:
        rxs.append((re.compile(r"(?<![A-Za-z0-9_.])(" + _alts(mapping) + r")(?!" + ID + r"|\." + ID + ")"),
                    lambda m: m.group(1)))
    if documents:
        rxs.append((re.compile(LEAD + "(" + _alts(documents) + ")(?!" + ID + ")"), lambda m: m.group(1)))

    def find(text):
        return sorted({name(m) for rx, name in rxs for m in rx.finditer(text)})
    return find


# ---------------------------------------------------------------- the places

def places(root=None, ny=None, year=None):
    """[(path, kind)] of the files the rename covers, kind "fixture", "rows" or "rulings" (module doc)."""
    import families
    ny = jurisdiction.NY if ny is None else ny
    year = str(Y if year is None else year)

    def ypath(top, *rest):
        if root is None:
            return jurisdiction.ypath(top, year, *rest) if ny == jurisdiction.NY else \
                (ROOT / top / ("ny" if ny else "") / year).joinpath(*rest)
        return (Path(root) / top / ("ny" if ny else "") / year).joinpath(*rest)

    out = []
    fixtures = ypath("fixtures")
    if fixtures.is_dir():
        out += [(p, "fixture") for p in sorted(fixtures.rglob("*.json"))]
    for sub in ("coverage", "personas"):
        d = ypath("interview", sub)
        if d.is_dir():
            out += [(p, "rows") for p in sorted(d.rglob("*")) if p.suffix in (".yaml", ".yml")]
    for kind in KINDS:
        d = ypath("reviews", kind)
        if d.is_dir():
            for p in sorted(d.glob("*.rulings.json")):
                if families.split_stem(p.name[:-len(".rulings.json")])[1] == families.DEFAULT:
                    out.append((p, "rulings"))
    return out


def witness_parts(w):
    """(prefix kept as it is, [parts that name ids]) of a triage witness (rulings.witness_id)."""
    kind, colon, rest = w.partition(":")
    name, at, instance = rest.rpartition("@")
    if not colon or not at:
        return None
    if kind == "partial":
        base, dash, withheld = name.partition("-")
        if dash:
            return f"{kind}:{base}-", [withheld, instance]
    return f"{kind}:{name}", [instance]


def _witness(w, sub):
    parts = witness_parts(w)
    if parts is None:
        return w
    head, (*names, instance) = parts
    return head + "".join(sub(n) for n in names) + "@" + sub(instance)


def _witnesses(text):
    """[(ruling index, witness)] of a rulings sidecar's text."""
    try:
        data = json.loads(text)
    except ValueError:
        return []
    rows = data.get("rulings", []) if isinstance(data, dict) else []
    out = []
    for i, r in enumerate(rows if isinstance(rows, list) else []):
        triage = r.get("triage") if isinstance(r, dict) else None
        if isinstance(triage, dict):
            out += [(i, w) for w in triage.get("witnesses") or [] if isinstance(w, str)]
    return out


def rewrite(text, kind, sub):
    """The text of a place with the rename applied (module doc: what each kind leaves alone)."""
    if kind == "rulings":
        for _, w in _witnesses(text):
            new = _witness(w, sub)
            if new != w:
                text = text.replace(json.dumps(w, ensure_ascii=False), json.dumps(new, ensure_ascii=False))
        return text
    if kind == "fixture":
        return "".join(line if SKIP_LINE.match(line) else sub(line) for line in text.splitlines(keepends=True))
    return sub(text)


def left(text, kind, find):
    """[(where, [old ids])] of the old ids a place still names."""
    out = []
    if kind == "rulings":
        for i, w in _witnesses(text):
            parts = witness_parts(w)
            found = find(" ".join(parts[1])) if parts else []
            if found:
                out.append((f"ruling {i} witness {w}", found))
        return out
    for n, line in enumerate(text.splitlines(), 1):
        if kind == "fixture" and SKIP_LINE.match(line):
            continue
        found = find(line)
        if found:
            out.append((f"line {n}", found))
    return out


def apply(mapping, documents, files=(), root=None, ny=None, year=None):
    """Rewrite the places and `files`; the paths changed."""
    sub = substituter(mapping, documents)
    changed = []
    for path, kind in places(root, ny, year) + [(Path(f), "file") for f in files]:
        text = path.read_text(encoding="utf-8")
        new = rewrite(text, kind, sub)
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed.append(path)
    return changed


def check(mapping, documents, root=None, ny=None, year=None):
    """[(path, where, [old ids])] of every old id left in the places."""
    find = finder(mapping, documents)
    out = []
    for path, kind in places(root, ny, year):
        out += [(path, where, ids) for where, ids in left(path.read_text(encoding="utf-8"), kind, find)]
    return out


def _rel(path):
    try:
        return str(Path(path).resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def main(argv):
    if argv == ["--self-test"]:
        import test_rename_ids
        return test_rename_ids.main()
    if not argv or argv[0] not in ("apply", "check"):
        sys.exit(__doc__)
    command, rest, map_path, files = argv[0], argv[1:], None, []
    while rest:
        if rest[0] == "--map" and len(rest) > 1:
            map_path, rest = rest[1], rest[2:]
        elif rest[0].startswith("-"):
            sys.exit(f"rename_ids: unknown option {rest[0]}\n{__doc__}")
        else:
            files.append(rest.pop(0))
    mapping, documents = load_map(map_path)
    if command == "apply":
        changed = apply(mapping, documents, files)
        print(f"rename_ids: {len(changed)} file(s) changed")
        for p in changed:
            print("  " + _rel(p))
        return 0
    if files:
        sys.exit("rename_ids: check takes no files; it reads the places the module doc lists")
    found = check(mapping, documents)
    n = len(places())
    where = f"{len(mapping)} ids and {len(documents)} documents renamed, {n} files"
    if found:
        print(f"rename_ids: old ids left ({where}); rename them with `python3 tools/rename_ids.py apply`, or by "
              "hand where the document moved:")
        for path, at, ids in found:
            print(f"  {_rel(path)}: {at}: {', '.join(ids)}")
        return 1
    print(f"rename_ids: no old id left ({where})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
