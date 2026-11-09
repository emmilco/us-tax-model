# Consolidation charter

**Status: confirmed by the owner, 2026-11-09.**

This document replaces the planning layer: the integrity plan, the plan revision, the retired backlog plan and the
process optimization doc. It states the project's one architecture, its conventions, its verification system and its
process. Where it conflicts with an older document, this one governs. History stays in git and in
`docs/2026-11-07_process_retrospective/`.

## 1. Goal and order

The artifact is an open, verifiable formalization of the federal individual income tax forms and instructions, with
New York as a second jurisdiction. Its first client is a guided interview that an ordinary person can answer correctly.

The long-run cost is the yearly cycle: forms change every tax year, and each change needs rewiring and verification.
The structure and the process are judged by how cheap one change and one year rollover are.

Order, decided by the owner on 2026-11-07/08:
1. **Consolidation** (T-256): this charter, then phase 1 (one architecture applied everywhere) and phase 2 (process
   rules enforced by tools).
2. **The interview:** the gate wave, alongside phase 1, then the wording pass (phase 3).
3. **Coverage growth** waits until the project is stable. Federal coverage stays at 78.4%; Schedule E (stage 17) and
   the rest wait.
4. **TY2026 adoption** (`docs/ty2026/ADOPTION.md`) proceeds when the final IRS 2026 documents exist.

New York stays at its current scope until phase 2 ends. The web UI (T-236, T-252 PDFs, T-253) gets only what the
interview work needs until then. (Owner, 2026-11-09.)

## 2. The architecture

There is one architecture, unchanged since the day-1 spec. Everything in the repository is one of these layers:

| Layer | What it is | Where |
|---|---|---|
| Sources | Archived official documents, read-only | `sources/`, `tools/sources-*.json` |
| Formal model | Forms and definitions in the DSL. Every line has an expression and a citation. Refusals are values | `forms/<juris>/<year>/`, `params/`, `tables/` |
| Evaluators | The TypeScript evaluator (the product) and the Lean reference evaluator (the check). The two must agree | `engine/src/eval.ts`, `lean/` |
| Interview | Words, formats, order, groups and labels only. It never sets an input. Only the evaluator's reachability hides a question | `interview/` |
| Evidence | Fixtures, reviews, reports and rendered output. All derived from the layers above, or recording a judgment about them | `fixtures/`, `reviews/`, `reports/`, `rendered/` |
| Tooling | Builds, checks and review machinery | `engine/`, `tools/` |

Standing rules of the model and the interview (the formal gates design, 11-06):
- All tax logic lives in the formal model, including applicability. Gates are A (instruction conditions), B
  (existence facts) and C (conditions on computed amounts).
- A gated input keeps its id. A new gate line `<input>_if_<cond>` takes its place, and the input carries `gated_by`.
- Only the evaluator's reachability hides a question. Order never changes a value.
- Partial fixtures' defaults are written in test data (`fixtures/**/defaults.json`), never in the engine.

## 3. Evidence layout (settled)

- **Fixtures** are per form: `fixtures/<juris>/<year>/<doc>.json`. Each case states only the facts that make its
  scenario non-default. Defaults come from `defaults.json`, applied only by the test loader. Every default carries a
  reason.
- **Whole returns** are kept in `returns.json` and walked end to end.
- `classm*.json` and `mutation.json` are tool-managed and take no defaults.
- **Leak detection** is `interview-rules`: the walk checks, minimal returns, and five random orders, plus a shrink-only
  baseline of held templates.
- **Guards:**
  - A new input's default needs the normal tier.
  - A changed existing default needs `Fixture-default-changed:` lines in the commit message.
  - A changed held leak or held asked-unread template must shrink the baseline, never grow it.
- **Generated review output** (88% of churned lines were committed review output later regenerated): review logs
  become content-addressed by subject hash, so an unchanged subject never rewrites a file (owner, 2026-11-09). This
  pairs with carrying review logs across years (section 7).

## 4. Verification system

What each check is for, in each phase. "Building" means a form is being written or restructured. "Maintenance"
means the form is stable and only small changes or year updates happen.

| Check | Building a form | Maintenance | Why |
|---|---|---|---|
| Mechanical checks (fixtures, interview-rules, mutation, Lean comparison, engine differential) | always | always | Free, deterministic, and the strongest guarantee |
| Claude transcription (independent construction) | whole form | changed lines only (line-scoped), and only when the arithmetic changed | About $150 per bug found on stable forms |
| Render review | whole form | changed lines only, and only when the wording changed | About $70 per bug on stable forms |
| Class M (cases) | yes | when the form's arithmetic changes | Found nothing in the ledger window |
| Completeness, screen and false-no reviews | yes | a fixed sample per form per milestone, its union ruled once | $2 to $3 per bug. Completeness behaves like a random sample, so rerunning on every edit only pulls in old low findings |
| Second family (DeepSeek, GPT) | inactive | inactive | 1 bug in 1,488 rulings. Owner, 2026-11-09: Claude-only reviews; machinery kept dormant |
| Human reading | optional | optional | Validation policy, 10-24 |

Budget: the $3.00 owner gate in `rerun_all.py` stays. There is no monthly budget for now: the gate and the
once-per-round rule bound the spend. Revisit after one month of ledger data at maintenance rates.

**The second family is inactive (owner, 2026-11-09).** No DeepSeek or GPT review runs. Its machinery is
disabled, not deleted: an `active` flag in `families.json`, skipped by `rerun_all.py` unless overridden with a recorded
reason, and treated as history by `check_logs.py`. `compare_families.py` and the transport code stay dormant, with
their self-tests, so reactivating a family is a flag change.

## 5. Process rules and their enforcement

Every process rule is either enforced by a tool or marked advisory. No new prose-only rules.

| Rule | Enforced by | Status |
|---|---|---|
| Commit only exactly tested trees | `commit_tested.sh`, hooks | enforced |
| One review per form per round; cost estimate; owner gate above $3 | `rerun_all.py` | enforced. Completeness and screen reruns are NOT yet guarded |
| Carry repeat disagreements mechanically | `carry.py` | enforced |
| Review data moves only through the tool | `worktree_data.py` clone, fill, carry-back | enforced |
| Background waits on a pid or a status, never `pgrep -f` | none | advisory |
| Mechanical agent work runs on Sonnet | none | advisory. Proposal: an agent-launch wrapper that requires model and class, and logs the `agent_runs.jsonl` row automatically |
| Two lanes never edit the same form at once | none | Proposal: a form-claim registry checked by `commit_tested.sh` |
| Fixture defaults are visible test data | `defaults_guard.mjs`, commit-msg hook | enforced |

## 6. Conventions (from the phase 0 inventory)

Proposed. Each is a phase 1 cleanup item, not a rewrite:
- **Jurisdiction and year:** federal unprefixed (`<kind>/<year>/`), New York as `<kind>/ny/<year>/` (owner,
  2026-11-09). Fix the stragglers: `tools/sources-ny-2025.json`, `adapter_contracts/2025/`, and interview files
  with the year in the filename.
- **Docs:** dated `YYYY-MM-DD_` for point-in-time documents. Undated only for living documents (`TRUST.md`,
  `COVERAGE.md`, this charter once confirmed, `ARGON_CLAUDE_DISCUSSION.md`).
- **Tests:** engine tests as CLI commands. Python tests beside the code as `test_*.py`, each run by a check-all
  step, or deleted.
- **Engine file names:** kebab-case for multi-word names (already the majority).
- **Handoffs:** `HANDOFF-NEXT-SESSION.md` keeps the latest two entries. Older entries move to the monthly archive.

## 7. Year rollover

Source: `docs/2026-11-09_ty2026_rollover_measurement.md`. No year has actually been rolled over. TY2026 is preparation
on IRS drafts (`d6017626`) plus a 10-27 rehearsal (`713a5662`); `years.json` is still `[2025]`.

What a rollover costs today:
- **Missed changes.** 49 of 135 changes (36%) are found only by reading the drafts, because `year_diff` cannot see new
  lines.
- **Parameters.** 45 of 273 are filled mechanically.
- **Tables.** 10 of 19 federal tables and 17 of 19 New York tables are made by hand.
- **Hard-coded years.** 7 page-layout settings know only 2025.
- **Re-recording.** About 97% of fixtures would be re-recorded.
- **Reviews.** `check_logs` demands a fresh review of every form for the new year, because the source snapshots
  change. That is roughly $140 to $400 a year (estimate).
- **New York** has no rollover path at all.
- **Decay.** Preparation work decays while it waits: since 11-04 the 2025 forms changed by +6,777/−2,445 lines, and
  2 of 10 hunks of one proposal no longer apply.

The rollover procedure, which phase 1 builds:
1. **Year changes are operations keyed by line id,** not copies and diffs. They are kept beside the forms and checked
   on every commit, so a prepared change cannot silently decay.
2. **New amounts are found mechanically.** The parameter-proposal scripts move from `research/` into `tools/`. Page
   layouts are read from data, not code.
3. **Review logs carry across years** when the subject and the cited text are unchanged once years are normalised. Only
   forms with real changes are reviewed again. This makes `check_logs` agree with ADOPTION.md.
4. **No year literals in ids or text** (30 input ids and 93 ambiguity ids carry one today). The engine is already clean.
5. **New York gets the same year handling** as federal: four New York tools hard-code 2025.
6. **Both cost ledgers record year and jurisdiction,** so the next rollover can be measured.

## 8. Phase 1 scope

In order of yearly cost saved:
1. The rollover procedure in section 7, ledger fields first (cheap, and the measurement depends on them), then review
   carry across years, year changes as operations, mechanical parameters, year-free ids, and New York year handling.
2. Content-addressed review logs (section 3), with the cross-year carry.
3. Disabling the second family (section 4): inactive flag, dormant code kept.
4. Check-all: fold the 34 self-tests into fewer steps, and parameterize the 16 New York mirrors. Drop or demote
   `human_review` (packets are optional) and the stage-named `review_stage2..5`.
5. The 22 tech-debt items that still hold, including the dangling commit per background run, the Python
   reimplementations of evaluator and renderer logic, and the duplicated Form 8863 logic.
6. `tools/`: 125 scripts. Retire or document the unreferenced ones.
7. The conventions in section 6.
8. Untrack the 51 tracked-but-ignored review files.

## 9. Retired by this charter

Once confirmed, these become historical (kept in git, banner added):
- `docs/2026-10-22_integrity_plan.md`
- `docs/2026-10-26_plan_revision.md`
- `docs/2026-11-04_process_optimization.md`, whose live cost rules move here and into `CLAUDE.md`
- `docs/2026-11-06_question_structure_design.md`, superseded by the formal gates design

The validation policy (10-24), the release gating design (11-05), the formal gates design (11-06) and the web UI design
(11-06) remain current. This charter cites them rather than restating them.
