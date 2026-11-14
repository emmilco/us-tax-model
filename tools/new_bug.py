#!/usr/bin/env python3
"""Append the next BUG-NNNN entry to BUG_INVENTORY.md, or record a pending entry, and print its id.

    python3 tools/new_bug.py "Title" \
        --field "Caught by=the owner, 2026-11-05." --field "Symptom=..." \
        --field "Tags=tool change"
    python3 tools/new_bug.py "Title" --body-file entry_body.md   # or --body-file -
    python3 tools/new_bug.py "Title" --pending [PREFIX] --field ...
    python3 tools/new_bug.py --assign

--pending writes the entry, unnumbered, to bug_pending/PREFIX-NN.md (NN the next number for that
prefix, two digits or more; PREFIX defaults to the current branch's name) and prints its
placeholder BUG-NEW-PREFIX-NN, which the branch cites wherever it would cite the id. A branch that
runs alongside others records its defects this way and never writes the inventory.

--assign, run in the merge that brings pending entries onto main (`git merge --no-ff --no-commit`,
then this, `git add -A`, check-all and `git commit`), appends every pending entry to the inventory
in name order (numbers compared as numbers), each with the next id, rewrites each placeholder to
its id in every tracked file, deletes the pending files, and prints one line per entry,
`BUG-NEW-<name> -> BUG-NNNN`, for the merge's commit message. tools/check_bug_inventory.py --merge
(pre-commit) accepts a merge only when it appends exactly this.

Each --field NAME=VALUE becomes a bullet `- **NAME:** VALUE`, in the order given.
A body file replaces the fields and is written as given (trailing newlines
trimmed). The id is one more than the highest id in the file; the existing text
is never rewritten, only appended to, so tools/check_bug_inventory.py still
passes. --file selects another inventory (default: BUG_INVENTORY.md at the
repository root).
"""
import argparse
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import check_bug_inventory as rule  # noqa: E402

ID_RE = re.compile(r"^## BUG-(\d{4}) ", re.M)


def fail(msg):
    print(f"new_bug: {msg}", file=sys.stderr)
    sys.exit(1)


def build_entry(bug_id, title, fields, body):
    return "\n" + entry_text(f"BUG-{bug_id:04d}", title, fields, body)


def entry_text(heading_id, title, fields, body):
    head = f"## {heading_id} — {title}\n\n"
    if body is not None:
        return head + body.rstrip("\n") + "\n"
    return head + "".join(f"- **{n}:** {v}\n" for n, v in fields)


def git(*args, cwd):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def branch_prefix(cwd):
    name = git("symbolic-ref", "--short", "-q", "HEAD", cwd=cwd).stdout.strip()
    prefix = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    if not prefix or prefix == "head":
        fail("no branch to name the pending entry by; give --pending PREFIX")
    return prefix


def write_pending(pending_dir, prefix, title, fields, body):
    if not rule.NAME_RE.match(prefix):
        fail(f"prefix must be lower-case letters and digits joined by '-': {prefix!r}")
    pending_dir.mkdir(parents=True, exist_ok=True)
    taken = [int(m.group(1)) for p in pending_dir.glob("*.md")
             if (m := re.fullmatch(rf"{re.escape(prefix)}-(\d+)", p.stem))]
    name = f"{prefix}-{max(taken, default=0) + 1:02d}"
    placeholder = "BUG-" + "NEW-" + name
    (pending_dir / f"{name}.md").write_text(entry_text(placeholder, title, fields, body), encoding="utf-8")
    print(placeholder)


def assign_pending(inventory, pending_dir):
    """Append every pending entry to `inventory`, rewrite placeholders in tracked files, delete the files."""
    files = {p.stem: p for p in sorted(pending_dir.glob("*.md"))} if pending_dir.is_dir() else {}
    pending = {name: p.read_text(encoding="utf-8") for name, p in files.items()}
    text = inventory.read_text(encoding="utf-8")
    problems = rule.pending_problems(pending)
    ids = [int(m) for m in ID_RE.findall(text)]
    if ids != list(range(1, len(ids) + 1)):
        problems.append("existing ids are not gapless from BUG-0001")
    if not text.endswith("\n"):
        problems.append("the inventory does not end with a newline")
    if problems:
        fail("refusing to assign: " + "; ".join(problems))
    if not pending:
        print("new_bug: no pending entries", file=sys.stderr)
        return
    new, mapping = rule.assign(text, pending)
    cwd = inventory.parent
    cited = git("grep", "-I", "-l", "-E", rule.PLACEHOLDER_ERE, cwd=cwd).stdout.split()
    for rel in cited:
        f = cwd / rel
        if f.resolve() == inventory.resolve() or f.parent.resolve() == pending_dir.resolve():
            continue
        old = f.read_text(encoding="utf-8")
        if (changed := rule.substitute(old, mapping)) != old:
            f.write_text(changed, encoding="utf-8")
    for name, p in files.items():
        p.unlink()
    if not any(pending_dir.iterdir()):
        pending_dir.rmdir()
    inventory.write_text(new, encoding="utf-8")
    for name in sorted(mapping, key=rule.natural_key):
        print(f"BUG-NEW-{name} -> {mapping[name]}")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("title", nargs="?")
    ap.add_argument("--field", action="append", default=[], metavar="NAME=VALUE")
    ap.add_argument("--body-file", metavar="PATH", help="entry body; '-' reads stdin")
    ap.add_argument("--file", default=str(ROOT / "BUG_INVENTORY.md"))
    ap.add_argument("--pending", nargs="?", const="", metavar="PREFIX",
                    help="record the entry as bug_pending/PREFIX-NN.md (default prefix: the branch)")
    ap.add_argument("--assign", action="store_true", help="number and append every pending entry")
    ap.add_argument("--pending-dir", help="the pending entries' directory (default: bug_pending beside --file)")
    a = ap.parse_args(argv)
    path = pathlib.Path(a.file)
    pending_dir = pathlib.Path(a.pending_dir) if a.pending_dir else path.parent / rule.PENDING_DIR

    if a.assign:
        if a.title is not None or a.field or a.body_file is not None or a.pending is not None:
            fail("--assign takes no entry")
        assign_pending(path, pending_dir)
        return
    if a.title is None:
        fail("no title")
    title = a.title.strip()
    if not title:
        fail("empty title")
    if "\n" in title:
        fail("title must be one line")

    body = None
    fields = []
    if a.body_file is not None:
        if a.field:
            fail("use either --field or --body-file, not both")
        body = sys.stdin.read() if a.body_file == "-" else pathlib.Path(a.body_file).read_text(encoding="utf-8")
        if not body.strip():
            fail("empty body")
        if re.search(r"^## ", body, re.M):
            fail("body must not contain a '## ' heading")
    else:
        for f in a.field:
            name, sep, value = f.partition("=")
            name, value = name.strip(), value.strip()
            if not sep or not name or not value:
                fail(f"field must be NAME=VALUE with both parts non-empty: {f!r}")
            if "\n" in name or "\n" in value:
                fail(f"field must be one line: {name!r}")
            fields.append((name, value))
        if not fields:
            fail("no fields and no body")

    if a.pending is not None:
        write_pending(pending_dir, a.pending or branch_prefix(path.parent), title, fields, body)
        return
    text = path.read_text(encoding="utf-8")
    ids = [int(m) for m in ID_RE.findall(text)]
    if ids != list(range(1, len(ids) + 1)):
        fail("existing ids are not gapless from BUG-0001; refusing to append")
    if not text.endswith("\n"):
        fail("file does not end with a newline; refusing to append")
    new_id = len(ids) + 1
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(build_entry(new_id, title, fields, body))
    print(f"BUG-{new_id:04d}")


if __name__ == "__main__":
    main()
