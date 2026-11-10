#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Fail unless the documents follow the conventions of the consolidation charter (section 6).

- Every Markdown file directly in docs/ is dated (`YYYY-MM-DD_<name>.md`), a point-in-time document, unless it is one
  of the LIVING documents.
- HANDOFF-NEXT-SESSION.md keeps the latest MAX_HANDOFF_ENTRIES entries (top-level `# ` headings); older ones move to
  the monthly archive under handoffs/.

    check_docs_conventions.py [--self-test]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIVING = {"TRUST.md", "COVERAGE.md", "consolidation_charter.md", "ARGON_CLAUDE_DISCUSSION.md"}
DATED = re.compile(r"^\d{4}-\d{2}-\d{2}_[^/]+\.md$")
MAX_HANDOFF_ENTRIES = 2


def problems(doc_names, handoff_text):
    out = [f"docs/{n}: not dated (YYYY-MM-DD_<name>.md) and not a living document ({', '.join(sorted(LIVING))})"
           for n in sorted(doc_names) if n not in LIVING and not DATED.match(n)]
    entries = len(re.findall(r"^# ", handoff_text, re.M))
    if entries > MAX_HANDOFF_ENTRIES:
        out.append(f"HANDOFF-NEXT-SESSION.md: {entries} entries; keep the latest {MAX_HANDOFF_ENTRIES} and move the "
                   "older ones to the monthly archive in handoffs/")
    return out


def main():
    names = [p.name for p in (ROOT / "docs").glob("*.md")]
    handoff = ROOT / "HANDOFF-NEXT-SESSION.md"
    found = problems(names, handoff.read_text(encoding="utf-8") if handoff.exists() else "")
    for p in found:
        print(p, file=sys.stderr)
    if not found:
        print(f"docs conventions OK ({len(names)} documents in docs/; handoff entries within {MAX_HANDOFF_ENTRIES})")
    return 1 if found else 0


def self_test():
    cases = [(problems(["2026-11-10_x.md", "TRUST.md"], "# a\n# b\n"), 0),
             (problems(["notes.md", "2026-1-1_x.md"], ""), 2),
             (problems([], "# a\n## sub\n# b\n# c\n"), 1)]
    bad = [(got, want) for got, want in cases if len(got) != want]
    print("docs conventions self-test: " + ("ok" if not bad else f"FAILED: {bad}"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv else main())
