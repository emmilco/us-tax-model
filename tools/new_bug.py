#!/usr/bin/env python3
"""Append the next BUG-NNNN entry to BUG_INVENTORY.md and print its id.

    python3 tools/new_bug.py "Title" \
        --field "Caught by=the owner, 2026-11-05." --field "Symptom=..." \
        --field "Tags=tool change"
    python3 tools/new_bug.py "Title" --body-file entry_body.md   # or --body-file -

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
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ID_RE = re.compile(r"^## BUG-(\d{4}) ", re.M)


def fail(msg):
    print(f"new_bug: {msg}", file=sys.stderr)
    sys.exit(1)


def build_entry(bug_id, title, fields, body):
    head = f"\n## BUG-{bug_id:04d} — {title}\n\n"
    if body is not None:
        return head + body.rstrip("\n") + "\n"
    return head + "".join(f"- **{n}:** {v}\n" for n, v in fields)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("title")
    ap.add_argument("--field", action="append", default=[], metavar="NAME=VALUE")
    ap.add_argument("--body-file", metavar="PATH", help="entry body; '-' reads stdin")
    ap.add_argument("--file", default=str(ROOT / "BUG_INVENTORY.md"))
    a = ap.parse_args(argv)

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

    path = pathlib.Path(a.file)
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
