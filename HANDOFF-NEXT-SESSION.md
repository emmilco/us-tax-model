# Night 2026-11-09/10: gate wave finished, phase 1 closed, eight defects fixed

**State:** `main` is pushed through the interview-layout commit below. No release has been cut since `r2026.11.06.1`.
Review spend this session (Claude only, `.transcription/costs.jsonl`): about $117. No open rulings; every review,
completeness and screen check current; interview-rules baseline empty (0/0/0).

**Landed (first-parent):**
- `8ff9b742` eic.zero reviewed (BUG-0468 closed for eic); carry.py judges log currency with `subjects.log_state` (BUG-0469).
- `20edb6bb` phase 1 remainder merged: human_review docs fast tier; the 22 held tech-debt rows decided (inventory 5.1:
  1 fixed, 2 partly, 4 proposals, 4 deferred, 11 won't fix); scripts run by hand documented; source catalogs under
  `tools/sources/<year>.json` and `tools/sources/ny/<year>.json`; charter renamed `docs/consolidation_charter.md`;
  proposals T-259 to T-263.
- `bed2d176` gate wave (BUG-0471): 62/11/4 held templates to 8/6/2; reviews of the changed forms ($65); completeness
  `elsewhere()` no longer reads a param as a line; mutation survivors killed (29 cases) or pinned.
- `164ca7a2` BUG-0479 (line-scoped catalog lists summed collections) and BUG-0470 (review scope parsed outside
  parentheses) fixed.
- `62c47c07` BUG-0474 to BUG-0478 fixed (s179 working-capital interest, Schedule C home expenses, market discount and
  contingent payment refusal, final-return carryover, Form 5695 installed date); open BUG-0487, 0488, 0489.
- `b9c5b37d` T-264: the last four held families, operand order, `person.work_ssn`, BUG-0473; baseline 0/0/0; BUG-0466
  resolved. Owner-accepted fixture changes: refusal or false to unknown on five incomplete-state fixtures. Open
  BUG-0490, 0491.
- `96ef8a7b` BUG-0472 fixed (chapter 11 debtor refused at return level); BUG-0495 fixed (siblings.py found entries
  renumbered at a merge).
- `436261d6` interview layout: `interview/<year>/` and `interview/ny/<year>/` (files named by profile); BUG-0496 fixed
  (siblings.py matched a quoted heading).

**Owner decisions (2026-11-09/10):** charter undated; New York catalog moved; the five phase 1 proposals are T-259 to
T-263; the unknown-on-incomplete trade-off of nested `choose` accepted (BUG-0471, BUG-0492); the five T-264 fixture
changes accepted; Claude review spend uncapped for the night; push without asking.

**Process lessons (now in the tools or worth keeping):**
- Renumber BUG ids in a branch commit before merging, not inside the merge commit (BUG-0495, BUG-0496).
- Rebuild (`npm run compile`, `build`, `render`) on main after every merge before running review checks or triage; a
  stale `canonical/` or `rendered/` gives false failures and wrong fixture counts.
- Only one check-all run per clone at a time; a refused start means wait and retry. The detached runner, not the
  launcher, is the pid to wait on.
- A merge commit must equal the tested tree: copy the run's regenerated reports into the index before committing.

**Open, for the owner:**
- BUG-0487 (Form 8962 question order), BUG-0488 (three sales rules), BUG-0489 (Schedule C refusal display), BUG-0490
  (SIMPLE salary reduction due date), BUG-0491 (New York use tax and DMV-paid vehicle tax): all open, unfixed.
- T-259 to T-263 (phase 1 proposals). Phase 2 (process rules enforced by tools) is next in the charter.
- `reports/2025/coverage.md` is 53 MB; GitHub warns above 50 MB. Consider trimming or Git LFS.
- Two old agent worktrees remain (`agent-a64a29b0e8ab56370`, `agent-ada089006890714fc`): merged and clean, holding only
  older derived review files (log views, triage) that differ from main's; safe to remove.

- The 51 tracked-but-ignored `.transcription/` and `.classm/` files are untracked (they stay on disk; check-all copies those folders in).

# Overnight 2026-11-09: T-257, phase 0 inventory, step (c) built

**State:** `main` is pushed through `182800b1`. Landed overnight (owner asleep, working from the owner's 1:05 plan):
`e2252227` bookkeeping; `695e6ef7` T-257 (triage evaluates line-scoped sections against their own pass reply;
refusal kept as fallback); `182800b1` phase 0 inventory (`docs/2026-11-09_consolidation_inventory.md`).

**Step (c) merged (`ea25cc6a`, owner 2026-11-09):** fixtures are per-form with test-data defaults
(`fixtures/2025/defaults.json`, `fixtures/ny/2025/defaults.json`, applied only by the test loader); 178.7 to 13.3
inputs per case; a changed existing default needs a `Fixture-default-changed: <input> (<n> cases)` commit line
(`tools/hooks/commit-msg`). Argon did not review it; the owner merged without that review.

**Owner decisions (2026-11-09):** all morning recommendations accepted. Step (c) merged; the T-257 prompt change
(name the condition of `shown_when` lines in line-scoped requests) is in progress; the 16 true-valued defaults
and the 94 restated mutation-killing inputs are accepted; the safe pruning is applied (backlog plan retired,
`README.md.orig` and `tools/structural_leaks.mjs` removed; untracking the 51 tracked-but-ignored `.transcription/`
and `.classm/` files is deferred: `commit_tested.sh` commits the tested working-tree snapshot, which still holds
them, so it needs a deliberate `git rm --cached` outside that flow); finished agent
worktrees are being removed. Kept after checking: `extract_tax_table.py`, `extract_macrs_tables.py`
(yearly table extraction), `ny_policyengine.py` (NY engine differential report), `migrate_completeness_debt.py`
(documented in tools/README.md).
