#!/usr/bin/env python3
"""Rewrite the "## Line subjects" table of every transcription log to the wording-blind subjects
(subjects.transcription_line_subjects: a line's and the document's label, help, note, display and
ambiguity fields left out) of the version of the document the log reviewed. No model call; idempotent.

    migrate_line_subjects.py [--jurisdiction ny] [--forms a,b] [--dry-run]

The reviewed version is found from what the log records, as `transcribe.py --lines auto` finds it:

- a table row (and the rest row) equal to the citation-only hash of the line in a version of the
  document (the working tree, or one of its last 200 revisions in git) is replaced by the wording-blind
  hash of the line in that version; a row already equal to a version's wording-blind hash is kept; a
  row matching no version is kept, and the line stays stale;
- a log with no table whose header subject (subjects.of_form) matches a version gets the table of that
  version, so a later wording edit is judged line by line instead of by the whole-document subject.

Every row is the hash of what the log reviewed, never of the current document. The migration keeps
each log's state: a log is written only when its state after (subjects.log_state) equals its state
before, judged under the citation-only definition its table was written under. A log that would change
state (a stale log whose differences from its reviewed version all lie outside its compared lines, or
in wording alone) is left as it is and named; `transcribe.py --lines auto` decides it. The
foreign-interfaces table and every other part of the log are left as they are.
"""
import argparse
import contextlib
import functools
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE)))
from taxyear import Y  # noqa: E402
import jurisdiction  # noqa: E402  (--jurisdiction ny: the New York documents and logs)
import families  # noqa: E402
import subjects  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
REVISIONS = 200
RAW_HEADING = "## Raw second transcription"
SUBJECT = re.compile(r"^\| subject sha256 \| ([0-9a-f]{64}) \|$", re.M)


def cite_only(o):
    return subjects._without_cites(o)


@contextlib.contextmanager
def citation_only_subjects():
    """subjects.py computing transcription line subjects with only citations left out (wording included)."""
    saved = subjects.transcription_line_subjects
    subjects.transcription_line_subjects = functools.partial(saved, view=cite_only)
    try:
        yield
    finally:
        subjects.transcription_line_subjects = saved


def state_before(fid, text, year=Y):
    with citation_only_subjects():
        return subjects.log_state("transcription", fid, year, text)


class Versions:
    """The versions of one document's YAML, newest first (working tree, then git history), read and
    hashed lazily: per version, the whole subject and the line subjects under both views."""

    def __init__(self, fid, year=Y, root=ROOT, texts=None):
        """`texts` ([(where, YAML text)]), when given, are the only versions searched."""
        self.fid, self.file = fid, subjects.path("transcription", fid, year)
        self.root, self._texts, self._revs, self._hashes = root, texts, [] if texts is not None else None, {}

    def texts(self):
        if self._texts is None:
            self._texts = [("working tree", open(self.file, encoding="utf-8").read())]
            rel = os.path.relpath(self.file, self.root)
            self._revs = subprocess.run(["git", "-C", self.root, "log", "--format=%H", "-n", str(REVISIONS), "--", rel],
                                        capture_output=True, text=True).stdout.split()
        yield from self._texts
        while self._revs:
            rev = self._revs.pop(0)
            rel = os.path.relpath(self.file, self.root)
            proc = subprocess.run(["git", "-C", self.root, "show", f"{rev}:{rel}"], capture_output=True, text=True)
            if proc.returncode == 0:
                self._texts.append((f"revision {rev[:12]}", proc.stdout))
                yield self._texts[-1]

    def hashes(self, where, text, ids):
        """(whole subject, (old rows, old rest), (new rows, new rest)) of one version, by line id."""
        if where not in self._hashes:
            try:
                self._hashes[where] = (subjects.of_form(text),
                                       subjects.transcription_line_subjects(text, ids, view=cite_only),
                                       subjects.transcription_line_subjects(text, ids))
            except Exception:   # a revision that no longer parses as a document names no subject
                self._hashes[where] = (None, ({}, None), ({}, None))
        return self._hashes[where]


def migrated_rows(text, keys, versions):
    """(rows {log key: subject}, rest, how) of a log's migrated table, or None when nothing is to be
    recorded (no table and no version whose whole subject the header records). `keys` are the current
    [(log key, line id)]."""
    ids = [i for _, i in keys]
    id_of = dict(keys)
    rec = subjects.recorded(text)
    if rec is None:
        header = SUBJECT.search(text)
        if not header:
            return None
        for where, version in versions.texts():
            whole, _, (new, new_rest) = versions.hashes(where, version, ids)
            if whole == header.group(1):
                return {k: new[i] for k, i in keys if i in new}, new_rest, f"table recorded from the {where}"
        return None
    rows, rest = rec
    out, out_rest, todo, rest_done = dict(rows), rest, {k for k in rows if k in id_of}, rest is None
    sources = set()
    for where, version in versions.texts():
        if not todo and rest_done:
            break
        _, (old, old_rest), (new, new_rest) = versions.hashes(where, version, ids)
        for k in list(todo):
            i = id_of[k]
            if i in new and rows[k] == new[i]:
                todo.discard(k)
            elif i in old and rows[k] == old[i]:
                out[k] = new[i]
                todo.discard(k)
                sources.add(where)
        if not rest_done:
            if rest == new_rest:
                rest_done = True
            elif rest == old_rest:
                out_rest, rest_done = new_rest, True
                sources.add(where)
    unmatched = sorted(todo) + ([] if rest_done else [subjects.REST_KEY])
    how = ("rows rewritten from the " + ", ".join(sorted(sources)) if sources else "already wording-blind") + \
          (f"; matching no version, kept: {', '.join(unmatched)}" if unmatched else "")
    return out, out_rest, how


def with_table(text, rows, rest):
    """The log with its "## Line subjects" section replaced by (or, absent, given) this table."""
    table = "\n".join(subjects.table(rows, rest)) + "\n"
    start = text.find("\n" + subjects.LINE_SUBJECTS + "\n")
    if start >= 0:
        end = text.find("\n## ", start + 1)
        return text[:start + 1] + table + text[end + 1:]
    lines_at = text.index("\n## Lines\n")
    at = min(i for i in (text.find("\n" + h + "\n", lines_at) for h in (subjects.FOREIGN, "## Line-scoped reviews", RAW_HEADING))
             if i >= 0)
    return text[:at + 1] + table + text[at + 1:]


def migrate_log(fid, text, year=Y, versions=None, keys=None):
    """(new text, how) of one transcription log; the text is unchanged when nothing is recorded."""
    versions = versions or Versions(fid, year)
    keys = keys if keys is not None else subjects.target_keys("transcription", fid)
    found = migrated_rows(text, keys, versions)
    if found is None:
        return text, "no table and no version of the document matches its subject; left as it is"
    rows, rest, how = found
    return with_table(text, rows, rest), how


def migrate_one(fid, text, year=Y, versions=None, keys=None):
    """(text to write, how, state before, state after) of one log: the migrated text when the log's
    state (stale or current) is unchanged by it, else the log as it is. A log the migration leaves
    unchanged (already migrated) is judged under the current definition only."""
    new, how = migrate_log(fid, text, year, versions, keys)
    after = subjects.log_state("transcription", fid, year, new)
    if new == text:
        return text, how, after, after
    before = state_before(fid, text, year)
    if (before is None) != (after is None):
        word = lambda s: "current" if s is None else "stale"
        return text, f"{how}; would turn {word(before)} -> {word(after)}, left as it is", before, before
    return new, how, before, after


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--forms", help="only these documents (comma-separated)")
    ap.add_argument("--dry-run", action="store_true", help="report; write nothing")
    a = ap.parse_args()
    logs = str(jurisdiction.ypath("reviews", Y, "transcription"))
    only = set(a.forms.split(",")) if a.forms else None
    counts = {"logs": 0, "changed": 0, "stale before": 0, "stale after": 0}
    held, cache = [], {}
    import rulings
    for fid, family in rulings.forms_with_logs("transcription"):
        name = families.stem(fid, family) + ".md"
        if only and fid not in only:
            continue
        if not os.path.exists(subjects.path("transcription", fid, Y)):
            print(f"{name}: no document {fid}; left as it is")
            continue
        text = rulings.read_log("transcription", fid, family)
        versions = cache.setdefault(fid, Versions(fid, Y))
        new, how, before, after = migrate_one(fid, text, Y, versions)
        state = lambda s: "current" if s is None else "stale"
        if "; would turn " in how:
            held.append(name)
        counts["logs"] += 1
        counts["stale before"] += before is not None
        counts["stale after"] += after is not None
        if new != text:
            counts["changed"] += 1
            if not a.dry_run:
                rulings.write_log("transcription", fid, new, family)
        print(f"{name}: {how}; {state(before)} -> {state(after)}" + (f" ({after})" if after else ""))
    print(f"\n{counts['logs']} logs; {counts['changed']} {'would change' if a.dry_run else 'changed'}; "
          f"stale before {counts['stale before']}, after {counts['stale after']}; "
          f"left as they are because their state would change: {', '.join(held) if held else 'none'}")


if __name__ == "__main__":
    main()
