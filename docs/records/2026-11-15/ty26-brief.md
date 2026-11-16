# Brief shared by the TY2026 wave-1 preparation lanes

You are one lane of the tax year 2026 preparation of the tax-formalization project, run in parallel with about a dozen
other lanes. Your lane id, scope and worktree are in your launch message.

## Where you work
- Only in your worktree `/Users/elliotmilco/Documents/GitHub/tax-formalization/.claude/worktrees/ty26-<lane>`: a detached
  snapshot (`refs/scratch/ty26-base`) of the 2025 interview-redraft landing tree, which is about to be merged to `main`.
  Its review data is cloned in (if `.transcription/` is missing, wait for `/tmp/ty26-cloned-<lane>` to exist, polling with
  a timeout; never copy review data by hand). Never cd to the main checkout or another worktree.
- Build first: `npm run compile --silent && node engine/dist/main.js build && node engine/dist/main.js render`.
- Do not commit (the commit guard refuses untested trees; the coordinator merges your diff after the landing). Do not
  run `tools/claims.py` (the coordinator claims forms at merge).
- No paid reviews (plan decision D10), no model calls from code, no edits to `BUG_INVENTORY.md`, `TASKS.md`,
  `TASKS-DONE.md` or the table in `changes/2026/README.md` (the coordinator's bookkeeping). Defects you find go to
  `bug_pending/` through `python3 tools/new_bug.py "Title" --pending ty26-<lane> --field ...` (never hand-written).
- Do not edit `forms/2025/`, `interview/2025/`, `fixtures/2025/` (the 2025 tree is frozen for its landing), except where
  your scope below names a file explicitly.

## Read first
- Project `CLAUDE.md`; the plan `docs/provisional/lanes/ty26-plan.md` (your lane's row, sections 2 and 4, and the
  decisions D1–D14, which the owner has delegated: apply them as written unless you find one wrong, then say so);
  `docs/2026-11-14_year_change_operations.md`; `changes/2026/README.md`; `tools/README.md` (year operations,
  year_carry, adoption sections); `TASKS.md` rows T-295 to T-298; `research/ty2026/` (the change map `changes.md`
  names some ids from before the year-free renames: map them through `tools/year_free_names.json`).
- Treat every document as testimony: check a claim against the tree before relying on it.

## Verify and report
- Run the checks your deliverable names, plus `python3 tools/year_changes.py --check` (and `--self-test` if you changed
  `tools/year_changes.py`), and the self-tests of every tool you changed. At the end run `tools/check_all.sh --tier fast`
  in your worktree (it waits for one of the machine's two slots; that is fine) and report its failing steps; failures
  of `check_logs`/`ny_check_logs` from pending 2025 reviews in the base are expected and not yours.
- Report concisely: what you did (files, operations, tools), decisions you made and why, what waits on unpublished
  documents (by document), defects recorded, verification commands and outcomes, and anything another lane must know
  (files you touched outside your scope, collisions). Write the same to `docs/provisional/lanes/ty26-<lane>.md`.
