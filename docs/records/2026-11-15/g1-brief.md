# Brief shared by the goal-1 lanes (consolidation remainder and meaningful bug fixes)

You are one lane of a parallel round in the tax-formalization project. Your lane id, scope and worktree are in your
launch message; the round plan is `docs/provisional/lanes/g1-plan.md` in your worktree (section (c), your lane's row;
section (b), the bugs it names; section (d), the decisions D1–D15, which the coordinator has adopted as recommended:
apply them).

## Where you work
- Only in your worktree `/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/nx-<lane>`: a detached
  snapshot (`refs/scratch/g1-base`) of the state main is about to have (the 2025 interview-redraft landing plus the 2026
  preparation batches A and B). Review data is being cloned in: wait until `/tmp/nx-cloned-<lane>` exists (poll with a
  timeout; never copy review data by hand). Never cd elsewhere.
- Build first: `npm run compile --silent && node engine/dist/main.js build && node engine/dist/main.js render &&
  node engine/dist/main.js render --ny`.
- Do not commit. Do not run `tools/claims.py` (the coordinator claims at merge). Your deliverable is your working-tree
  diff plus a report; the coordinator integrates all lanes in one merge batch and runs one full check-all.
- **Do not run `tools/check_all.sh`** (about 20 lanes share two machine slots). Verify with the targeted checks your
  change needs: `node engine/dist/main.js test-fixtures` (+ `--ny`), `interview-rules`, `tick-groups`,
  `interview-coverage` (only if you changed questions or coverage rows), `python3 tools/citations.py --strict`,
  `check_consumers.py`, `check_questions.py`, `check_screens.py`, `check_false_no.py`, `siblings.py --check`,
  `check_bug_inventory.py`, `year_changes.py --check` (after any edit to a form a 2026 operation names: mend the
  operation in `changes/2026/`), the self-tests of any tool you changed (`tools/self_tests.py`), and `mutate` only if
  you changed expressions (it is slow; say if you skipped it).
- **No paid reviews in this wave** (round 2 runs after the merge). No model calls from code.
- Defects you find: `python3 tools/new_bug.py "Title" --pending g1-<lane> --field ...` (never hand-written). Fixing an
  existing BUG: write a closure the way the inventory does it for this tree (read tools/README.md on bug entries and
  `check_bug_inventory.py`; the inventory is append-only — if a closure needs a new entry, record it as a pending entry
  with Fix / Fix lines / Siblings checked (from `python3 tools/siblings.py <ids>`, actually read; avoid the word "none"
  in that field: the checker treats such a field as empty; list your own changed lines there too) / Regression
  predictions). Do not edit `BUG_INVENTORY.md`, `TASKS.md`, `TASKS-DONE.md` or the `changes/2026/README.md` table.

## Rules of the work
- Read first: project `CLAUDE.md`; `docs/2026-11-13_interview_construction_protocol.md` (normative for any question
  change); the BUG entries your row names (in `BUG_INVENTORY.md`) and their sources; the form YAML.
- Treat every claim in a bug entry, task row or lane note as testimony: verify against the tree and the archived
  sources before acting. If a bug is already fixed or not real, say so with evidence and close it.
- No expected value of an existing fixture is edited to make it pass. If your fix changes a value of an existing
  fixture, stop and report it (that is a finding about the fixture or the fix, for the coordinator).
- New behaviour gets a hand-predicted regression fixture written from the source before running.
- Lows on your forms ride along (D4): fix them in the same change.
- Shared files (`interview/2025/questions.yaml`, `fixtures/2025/defaults.json`, `fixtures/2025/classm.json`,
  `interview/2025/coverage/*.yaml`, `tools/coverage/tree.json`) are merged by entry / case / row id at integration:
  change only entries of your own forms, and never reformat or reorder others.
- Generated files (`rendered/`, `reports/`, `canonical/`, `docs/COVERAGE.md`) are regenerated at integration: you may
  regenerate them to run checks, but say which you regenerated.

## Report
Concisely: per bug, real or not (evidence), the fix (files, line ids, question text), closures written; new pending
bugs; verification commands and outcomes; the forms whose reviews round 2 must run (transcription / render / class M
per form, and why); anything the coordinator must decide or merge carefully. Write the same to
`docs/provisional/lanes/g1-<lane>.md`.
