# Draft: additions to docs/2026-11-15_coverage_expansion_protocol.md section 8.10

To be applied in the docs commit after release r2026.11.15.1, under the existing "Operating facts learned on
2026-11-15" list. Change the lead-in to "learned on 2026-11-15 and 16". Each item was observed on the night of
2026-11-15/16 (coordinator notes: docs/records/2026-11-16/coordinator/morning-report-notes.md).

- **A step on the release or commit path names its check and its time.** Before putting a step between a finished
  tree and its gating check, name the check step that fails without it, and its measured run time. A step no check
  requires stays off the path. On 2026-11-16 the coordinator asked for every generated report to be regenerated
  before the release check. The interview-length what-if report (`reports/2025/umbrella_savings.md`, a one-off design
  measurement that no step reads) then ran more than 30 minutes and delayed the release by about 35. The plain
  `interview-length --write` was redundant too: the release-mode check rewrites `interview_length.md` itself
  (`release_steps` in `tools/check_all_steps.sh`). To find out whether a report is required, grep
  `tools/check_all_steps.sh` and `tools/tier_paths.py` for its path. Task T-337 replaces this rule with a script.
- **Run the release review gate early.** `tools/release_reviews.sh` fails when a form's content changed after its
  sampled reviews: lines, citations or cited pages. Late fixes and citation corrections make samples due. Run it, or
  its separate checks without `set -e`, as soon as a candidate tree's content is final, before the reports and the
  full check, so the due reviews run in parallel with other work.
- **Several patches: check them in sequence, not together.** `git apply --check a.patch b.patch` passed a pair whose
  second patch then failed after the first was applied. Prove a set of patches fits by applying them one after
  another to a scratch copy.
- **Red-team wording before drafting patches, not alongside.** Five of the bug entries' own proposed fixes, and
  fourteen proposals in the fix plans, would have given a wrong value. A patch lane drafting from a plan that the red
  team has not yet checked writes those errors into its patch. Run the wording check first, or reconcile every patch
  against it before landing.
- **Lane briefs forbid shell functions and bulk process spawning.** A read-only lane defined a shell function `wc`
  that called itself and spawned about 6,700 processes on the machine running a gating check.
- **Rebuilt commits leave claims behind.** A commit rebuilt onto `main`, instead of merged, does not release its
  branch's form claims: the post-commit hook releases only the claims of branches HEAD merged. Release them with
  `tools/claims.py release` once the branch tip is confirmed on `main`.
- **Keep coordinator state out of `/tmp`.** Plans, notes and patches meant for a later session go in the project
  (`docs/records/<date>/`, or `.claude/` until committed; `.claude/` is excluded locally, so it doesn't block a
  release). `/tmp` does not survive a restart.

- **Run the steps that fail fast before a full check.** On a new candidate tree, run check_extraction (us and ny),
  check_limits, year_changes --check, check_logs (us and ny), release_reviews.sh, test-fixtures (us and --ny),
  coverage, interview-rules and the quick self-tests directly first. On 2026-11-16 one full check failed after 13
  minutes in wave 1, and the next after 52 minutes in wave 2, on defects a direct run would have shown in minutes.
- **A rename late in a round is followed at once by test-fixtures and coverage.** The 9 year-id renames of 2026-11-16
  missed fixture keys written with a collection index (`f8853c[p0].pre1996`), because the rename pattern excluded a
  `].` prefix. Five check steps failed on it. `rename_carry.py` and the rename step must cover collection-indexed keys
  (task T-338).
- **A coverage change updates the tests that encode the old refusals.** When an area moves from refused to computed
  (married filing separately on 2026-11-15), grep the tests (test_serve, test_integration, classm job seeds,
  interview_rules baselines, ny_mutate arguments) for cases that relied on the refusal, and re-point them in the
  area's own lane.

# Draft TASKS row (add with tools/task_row.py in the same commit)

T-337: a release-preparation script. It runs exactly what a candidate tree needs before its release-mode check:
release_reviews (all checks, reporting every due item before stopping), the reports and checks that check_all's
steps verify, and nothing else. It prints each step's time and stops at the first failure. It replaces the 8.10
rule above, and the coordinator's improvised sequence, with one command. Source: the what-if report delay of
2026-11-16 and the release-gate surprise at 23:55 the same night.

T-338: renames cover collection-indexed keys. `rename_carry.py` and the year-id rename step also rewrite
`<form>[<entry>].<old id>` in fixtures, coverage rows, personas and rulings, and the rename's check greps for any
old id left in those forms. Source: the missed `f8853c[p0].pre1996` of 2026-11-16, which failed five check steps.
