#!/usr/bin/env python3
"""Fail unless BUG_INVENTORY.md is an append-only extension of its committed version.

The committed content (git HEAD) must be a byte-for-byte prefix of the working
file, and entry ids must be sequential from BUG-0001 with no gaps or repeats.

    check_bug_inventory.py                       the working file against HEAD
    check_bug_inventory.py --merge TREE PARENT...  pre-commit, concluding a merge: every entry heading in TREE
                                                   is one of a parent's, word for word (a merge combines entries;
                                                   ids that collide are renumbered on the branch, before merging)
    check_bug_inventory.py --self-test
"""
import pathlib
import re
import subprocess
import sys
import tempfile

root = pathlib.Path(__file__).resolve().parent.parent
path = root / "BUG_INVENTORY.md"
HEADING = re.compile(r"^## BUG-\d{4} .*$", re.M)


def show(tree, cwd=root):
    r = subprocess.run(["git", "show", f"{tree}:BUG_INVENTORY.md"], cwd=cwd, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def check_working():
    current = path.read_text(encoding="utf-8")
    head = subprocess.run(["git", "show", "HEAD:BUG_INVENTORY.md"], cwd=root, capture_output=True, text=True)
    if head.returncode == 0 and not current.startswith(head.stdout):
        print("BUG_INVENTORY.md: committed content was modified; the file is append-only", file=sys.stderr)
        return 1
    ids = [int(m) for m in re.findall(r"^## BUG-(\d{4}) ", current, flags=re.M)]
    if ids != list(range(1, len(ids) + 1)):
        print(f"BUG_INVENTORY.md: entry ids must run BUG-0001.. without gaps; found {ids}", file=sys.stderr)
        return 1
    print(f"bug inventory OK ({len(ids)} entries, append-only)")
    return 0


def merge_problems(result, parents):
    """The entry headings of a merge's result that no parent has word for word."""
    known = {h for p in parents for h in HEADING.findall(p)}
    return [h for h in HEADING.findall(result) if h not in known]


def check_merge(tree, parents, cwd=root):
    new = merge_problems(show(tree, cwd), [show(p, cwd) for p in parents])
    if new:
        print("pre-commit: this merge creates or renames BUG entries (" + "; ".join(h[3:60] for h in new[:3])
              + "); renumber them in a commit on the branch, then merge (BUG-0495)", file=sys.stderr)
        return 1
    return 0


def self_test():
    a = "## BUG-0001 — one\n\nx\n"
    b = a + "## BUG-0002 — two\n"
    c = a + "## BUG-0002 — other\n"
    cases = [(merge_problems(b, [a, b]), []), (merge_problems(b + "## BUG-0003 — other\n", [b, c]), ["## BUG-0003 — other"]),
             (merge_problems(a + "## BUG-0002 — two\n## BUG-0003 — other\n", [b, a + "## BUG-0003 — other\n"]), [])]
    bad = [got for got, want in cases if got != want]
    print("bug inventory self-test: " + ("ok" if not bad else f"FAILED: {bad}"))
    return 1 if bad else 0


if __name__ == "__main__":
    if sys.argv[1:2] == ["--self-test"]:
        sys.exit(self_test())
    if sys.argv[1:2] == ["--merge"]:
        sys.exit(check_merge(sys.argv[2], sys.argv[3:]))
    sys.exit(check_working())
