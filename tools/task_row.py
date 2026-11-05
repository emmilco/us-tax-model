#!/usr/bin/env python3
"""Add, update, or finish rows of the TASKS.md table without loading the register.

    python3 tools/task_row.py add --task "Text" --source "Where from" --due "any time" [--status open]
    python3 tools/task_row.py status T-240 "in progress"
    python3 tools/task_row.py done T-240 "done 2026-11-05 (abc1234)"

add:    assigns the next T-NNN id (one more than the highest id in TASKS.md and
        TASKS-DONE.md, since ids are never reused), appends the row, prints the id.
status: replaces the status cell of the row with that id.
done:   sets the status cell and moves the row, text unchanged, from TASKS.md to
        the end of TASKS-DONE.md.
Cell text may not contain newlines; `|` is written as `\\|`. --file selects the
task register (default: TASKS.md at the repository root); --done-file the done
register (default: TASKS-DONE.md beside --file).
"""
import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ROW_RE = re.compile(r"^\| (T-(\d+)) \|")


def fail(msg):
    print(f"task_row: {msg}", file=sys.stderr)
    sys.exit(1)


def cell(text, what):
    text = text.strip()
    if not text:
        fail(f"empty {what}")
    if "\n" in text or "\r" in text:
        fail(f"{what} must be one line")
    return re.sub(r"(?<!\\)\|", r"\\|", text)


def read_lines(path):
    return pathlib.Path(path).read_text(encoding="utf-8").split("\n")


def ids_in(lines):
    return [int(m.group(2)) for m in map(ROW_RE.match, lines) if m]


def with_status(row, status):
    """Replace the last cell: the text after the last unescaped '|' before the closing one."""
    if not row.endswith(" |"):
        fail("row does not end with ' |'")
    inner = row[:-1]
    cut = max((m.start() for m in re.finditer(r"(?<!\\)\|", inner)), default=-1)
    if cut < 0:
        fail("malformed row")
    return f"{inner[:cut + 1]} {status} |"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--file", default=str(ROOT / "TASKS.md"))
    ap.add_argument("--done-file")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("add")
    p.add_argument("--task", required=True)
    p.add_argument("--source", required=True)
    p.add_argument("--due", required=True)
    p.add_argument("--status", default="open")
    p = sub.add_parser("status")
    p.add_argument("id")
    p.add_argument("status")
    p = sub.add_parser("done")
    p.add_argument("id")
    p.add_argument("status")
    a = ap.parse_args(argv)

    path = pathlib.Path(a.file)
    done_path = pathlib.Path(a.done_file) if a.done_file else path.with_name("TASKS-DONE.md")
    lines = read_lines(path)
    if lines[-1] != "":
        fail("TASKS file does not end with a newline")

    if a.cmd == "add":
        cells = [cell(a.task, "task"), cell(a.source, "source"), cell(a.due, "due"), cell(a.status, "status")]
        done_lines = read_lines(done_path) if done_path.exists() else []
        existing = ids_in(lines) + ids_in(done_lines)
        new_id = max(existing, default=0) + 1
        row = f"| T-{new_id:03d} | " + " | ".join(cells) + " |"
        if any(ROW_RE.match(l) and ROW_RE.match(l).group(1) == f"T-{new_id:03d}" for l in lines + done_lines):
            fail(f"id collision on T-{new_id:03d}")
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(row + "\n")
        print(f"T-{new_id:03d}")
        return

    if not re.fullmatch(r"T-\d+", a.id):
        fail(f"bad id {a.id!r}")
    status = cell(a.status, "status")
    hits = [i for i, l in enumerate(lines) if (m := ROW_RE.match(l)) and m.group(1) == a.id]
    if len(hits) != 1:
        fail(f"{a.id}: {len(hits)} matching rows in {path.name}")
    i = hits[0]
    new_row = with_status(lines[i], status)
    if a.cmd == "status":
        lines[i] = new_row
        path.write_text("\n".join(lines), encoding="utf-8")
    else:
        done_text = done_path.read_text(encoding="utf-8")
        if not done_text.endswith("\n"):
            fail("done file does not end with a newline")
        if any((m := ROW_RE.match(l)) and m.group(1) == a.id for l in done_text.split("\n")):
            fail(f"id collision: {a.id} already in {done_path.name}")
        with open(done_path, "a", encoding="utf-8") as fh:
            fh.write(new_row + "\n")
        del lines[i]
        path.write_text("\n".join(lines), encoding="utf-8")
    print(a.id)


if __name__ == "__main__":
    main()
