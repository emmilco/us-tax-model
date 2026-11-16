# Common rules for tonight's planning lanes (read first)

Context: tax-formalization repo, /Users/elliotmilco/Documents/GitHub/tax-formalization.
- The main checkout is `main` at acde74b5 (fix round B1). The worktree .claude/worktrees/xint holds the coverage
  expansion candidate: uncommitted, with its full check about to run. Bug entries there are now numbered
  BUG-0765..BUG-0922; the map from the old pending names (xrelbiz-01 and so on) is /tmp/xint/assign.out.
- Read CLAUDE.md, then what your brief names.

HARD RULES:
- READ ONLY. Never edit, create or delete any file inside the repository, its worktrees or .git.
  Write ONLY to your own output file under /tmp/nightplan/.
- No builds, no check_all, no node engine runs, no test suites, no CPU-heavy commands. A release-gating check is
  running on this machine. grep, sed, reading files and small python scripts that only read are fine.
- No paid model calls (no claude -p, no review tools that call models). No git commands that write
  (commit, stash, checkout, worktree add, apply).
- Python: ~/.pyenv/versions/3.13.6/bin/python3 (the default python3 lacks yaml).
- Your output: a markdown file at the path your brief gives. Lead with a summary, then the detail.
  Mark each claim as checked against a file (path:line) or inferred.
  Proposals only: describe changes as concrete diffs or sketches; apply none of them.
- Finish within about 50 minutes. If time runs short, write what you have, marked partial.
- Reply to the coordinator with 5 to 10 lines: the file path and the headline findings.

## Round 2 additions (patch-drafting lanes)
- Make your patch from copies: copy each file you change from xint into /tmp/nightplan/scratch/<lane>/b/<path>
  (and an untouched copy into .../a/<path>), edit the b/ copies, then produce the patch with
  `git diff --no-index a b`, rewriting the a/ and b/ prefixes so the paths are relative to the repo root.
  Write it to /tmp/nightplan/patches/<lane>.patch. Never edit xint itself.
- xint is FROZEN: a release-gating check is snapshotting it. Do not write anything inside it.
- With each patch, write /tmp/nightplan/patches/<lane>.md: what each hunk does, the fixtures or coverage rows added
  with hand-predicted values and how you derived them, the siblings checked, what to run to verify (draft-walk,
  test-fixtures, interview-coverage, tick-groups), and the reviews it makes due. Mark anything unverified.
- Follow docs/2026-11-13_interview_construction_protocol.md for every question or help change, and the bug-inventory
  conventions (tools/README.md) for any pending bug entry text, which goes in the .md, not in the patch.

## Round 3 additions (after an incident)
- Never define shell functions or aliases, and never write loops that spawn processes in bulk. A lane spawned
  thousands of processes at 00:05. A release-gating full check is running on this machine; keep the CPU use minimal.
- Corrected patches go to /tmp/nightplan/patches/v2/<name>.patch with <name>.md. Never overwrite the round 2 files.

## Round 4 (Phase A, from 01:05): durable output
- WRITE ALL OUTPUT under /Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/nightplan-2026-11-16/nightplan/
  (round4/ for reports, patches/v3/ for patches, scratch/round4-<lane>/ for scratch). NOT /tmp. This folder is
  inside the repo but locally excluded; writing there is allowed. Nothing else in the repo or its worktrees.
- Every earlier file mentioned as /tmp/nightplan/<x> is also at the path above (identical copies). Read from there.
- A release-gating full check runs until about 02:15: no builds, test runs or CPU-heavy commands. All other round
  1-3 rules apply.

## Round 5 (from ~02:25): drafting for the NEXT units
- Base for anything that edits the question bank or forms: the post-fix-round text in P/scratch/b-chain/work/ (the
  combined fix-round applied to the release candidate). The trims (P/round4/trimA.json and trimB.json) are not
  applied there; if your hunks touch a trimmed field, apply that field's trim to your copy first and say so.
- Output: P/round5/<lane>.md and P/patches/v4/<lane>*.patch (made from copies, with git apply --check against a
  copy of the base). Scratch: P/scratch/round5-<lane>/.
- Still NO builds or runs: the release check and F1's builds need the CPU.
