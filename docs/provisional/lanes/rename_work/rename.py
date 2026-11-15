#!/usr/bin/env python3
"""Apply tools/year_free_names.json to the files given (or, with --compare, verify fixtures before and after).

    rename.py apply FILE...          rewrite each file in place: every whole id of the map, and every path form
                                     `<doc>[key].<local>` of a mapped line id, becomes its new name. In fixture JSON
                                     the lines whose key is "id", "description" or "evidence_note" are left alone
                                     (labels and review records).
    rename.py compare OLD NEW        two fixture files: apply the map to OLD's keys and string values (except those
                                     three fields) and report every remaining difference from NEW.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
MAP = json.loads((ROOT / "tools" / "year_free_names.json").read_text())["renames"]
SKIP_FIELDS = ("id", "description", "evidence_note")

pairs = []  # (regex, replacement)
for old, e in sorted(MAP.items(), key=lambda kv: -len(kv[0])):
    new = e["to"]
    if e["kind"] == "document":
        # the document id, alone or as the head of a dotted id
        pairs.append((re.compile(r"(?<![\w])" + re.escape(old) + r"(?![\w])"), new))
        continue
    pairs.append((re.compile(r"(?<![\w.])" + re.escape(old) + r"(?![\w])"), new))
    doc, local = old.split(".", 1)
    new_local = new.split(".", 1)[1]
    pairs.append((re.compile(r"(?<![\w])(" + re.escape(doc) + r"\[[^\]\[\s]*\]\.)" + re.escape(local) + r"(?![\w])"),
                  r"\g<1>" + new_local))


def rename_text(s):
    for rx, rep in pairs:
        s = rx.sub(rep, s)
    return s


SKIP_LINE = re.compile(r'^\s*"(' + "|".join(SKIP_FIELDS) + r')":')


def apply(path):
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    if p.suffix == ".json" and "fixtures" in p.parts:
        out = "".join(line if SKIP_LINE.match(line) else rename_text(line) for line in text.splitlines(keepends=True))
    else:
        out = rename_text(text)
    if out != text:
        p.write_text(out, encoding="utf-8")
        return True
    return False


def mapped(node, field=None):
    if isinstance(node, dict):
        return {(k if k in SKIP_FIELDS else rename_text(k)): (v if k in SKIP_FIELDS else mapped(v, k)) for k, v in node.items()}
    if isinstance(node, list):
        return [mapped(x, field) for x in node]
    if isinstance(node, str):
        return rename_text(node)
    return node


def diff(a, b, where, out):
    if type(a) is not type(b):
        out.append(f"{where}: {a!r} != {b!r}")
    elif isinstance(a, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                out.append(f"{where}.{k}: only in {'new' if k in b else 'old'}")
            else:
                diff(a[k], b[k], f"{where}.{k}", out)
    elif isinstance(a, list):
        if len(a) != len(b):
            out.append(f"{where}: list length {len(a)} != {len(b)}")
        for i, (x, y) in enumerate(zip(a, b)):
            diff(x, y, f"{where}[{i}]", out)
    elif a != b:
        out.append(f"{where}: {a!r} != {b!r}")


def compare(old, new):
    a = mapped(json.loads(Path(old).read_text(encoding="utf-8")))
    b = json.loads(Path(new).read_text(encoding="utf-8"))
    out = []
    diff(a, b, "$", out)
    return out


if __name__ == "__main__":
    if sys.argv[1] == "apply":
        changed = [f for f in sys.argv[2:] if apply(f)]
        print(f"{len(changed)} of {len(sys.argv) - 2} files changed")
        for f in changed:
            print("  " + f)
    elif sys.argv[1] == "local":
        # also every bare local name (the part after the document id) as a whole word: for code that builds paths
        # from local names (the generators). A local name maps to one new local name throughout the map.
        locs = {}
        for old, e in MAP.items():
            if e["kind"] != "document":
                lo, ln = old.split(".", 1)[1], e["to"].split(".", 1)[1]
                assert locs.setdefault(lo, ln) == ln, lo
        for f in sys.argv[2:]:
            p = Path(f)
            s = rename_text(p.read_text(encoding="utf-8"))
            for lo in sorted(locs, key=len, reverse=True):
                s = re.sub(r"(?<![\w])" + re.escape(lo) + r"(?![\w])", locs[lo], s)
            p.write_text(s, encoding="utf-8")
            print("  " + f)
    elif sys.argv[1] == "compare":
        problems = compare(sys.argv[2], sys.argv[3])
        print(f"{sys.argv[3]}: {len(problems)} difference(s) beyond the map")
        for p in problems[:50]:
            print("  " + p)
        sys.exit(1 if problems else 0)
