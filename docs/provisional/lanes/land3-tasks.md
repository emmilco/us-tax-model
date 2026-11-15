# Lane land3-tasks: the task register after the landing

Agent: claude-opus-5-5, judgment class, year 2025, jurisdiction us. Worktree `.claude/worktrees/landing`. Edited only
`TASKS.md`, `TASKS-DONE.md` (through `tools/task_row.py`, plus one hand edit of T-268's task text) and this file. No
commit, no build, no model call. "Landing commit" in a status means the commit that lands this tree; it does not exist
yet. Inputs: `/tmp/claude-task-audit-2.md` (an audit written at 01:45 against an older main), read as testimony.
Each claim used was checked against this tree, or is kept with its lane note named as its source.

## Rows moved to TASKS-DONE

| Row | Status | Evidence in the tree |
|---|---|---|
| T-282 | done | steps 0-3 on main (abf7d60a); the owner walked on 11-12 and 11-13 (both docs exist); step 5 is this landing (850 questions; DECISIONS.md) |
| T-265 | closed, superseded | `sb.foreign_any` is now a computed gate line; `f5695.any`, `f1040.withheld_other_any` and `estimated_any` (group `paid_already`), and the five `s1.*_any` parents are in the bank; `umbrella-what-if.ts` RECOMMENDED = `s1.line8_any` |
| T-266 | done | the boilerplate sentence is on 1 bank entry (`person.x_hsa_value`, T-288) |
| T-261 | done | `tools/year_free_names.json` applied; `check_year_ids.py`: 5101 ids, none carries a year, 0 listed; `year_ids.json` baseline emptied; carry in landing.md section 3 and land3-clcw.md |
| T-281 | done in part | 30 inputs marked (rename.md Part 3; checked: `f8962.estimate_100`, `scope.care_benefits_other` carry `gated_by`); the rest is T-301 |
| T-284 | done in part | 850 of 850 questions state `order` and `seq`; `interview-order.ts`; re-entries went from 3.1 to 0.3 (integration_v2.md); the rest is T-302 |
| T-285 | done in part | 43 groups in the bank; `tick-groups.ts` and the `tick_groups` step; the rest is T-303 |
| T-286 | done in part | `household.ever_married`, `married_dec31` and `considered_unmarried` in the bank; the rest is T-304 |
| T-287 | done in part | 494 rows in 19 files of `interview/2025/coverage/`; `opening.unmarried_with_child`, `opening.widowed_with_child`; the rest is T-305 |

## Rows changed (status, or task text)

- T-253: removed "person.birth_year, which is not range-checked". The landing range-checks it by a refusal
  (`household.birth_year_bad`, DECISIONS.md section 2).
- T-256: phase 3 says the redraft landed in the landing commit, with its review round in T-299. Year-free ids are
  applied (T-261).
- T-268: the task text now says the clause is in `sb.line8`'s label, source and bank help (checked). Its trigger
  (Schedule B's next substantive change) fires with the landing.
- T-272: counted in the landing's built full profile: 6 parenthesised variants, 2 "you or your spouse", 2
  "either of you". The audit counted about 20, 10 and 4 on main. My regex may miss a few.
- T-276: the hold ends with the landing commit. The catalog sweep is to be rerun on the landed tree first.
- T-280: the pins were renewed. Per land3-mutate.md: federal 7480 mutants, 361 surviving, 0 stale; NY 878, 52
  surviving. `pinned(` calls in `mutate.ts`: 90. The mechanical backing is still open.
- T-288: `x_hsa_value` is now at 190/23, inside the block, and the prior-year excess is at 192/1. `f8889.age55` is
  derived from the birth year. The rest stands.
- T-291: its trigger fired (the landing changed Form 8889 without it).
- T-294: due with the landing commit (`filer_coverage.md` is not regenerated).
- T-296: the three operations the redraft made stale are mended (`changes/2026/README.md`).
- Left as they were (already current from 83c7d1c0, re-checked): T-262 (11 of 266 and 8 of 113 still hold;
  `generate.ts:417` still draws `unmarried` freely), T-270, T-289, T-290.

## Rows added (T-299 to T-314)

T-299 the review round (in progress); T-300 to T-305, the rest of T-261, T-281, T-284, T-285, T-286 and T-287; T-306
fixtures that describe impossible people (18 from l4b, 42 from v3_age, and 16 dependent-age cases from l2a); T-307
AMT asked of everyone; T-308 facts asked twice (N7 and N8 together); T-309 long questions and help above the baseline
(N9 and N10 together); T-310 gaps found and not fixed, with BUG-0642 and -08 and the N11 items; T-311 the
mutation lanes' observations (the `sb.unsupported_if_income` label; Schedule A lines 13 and 15 refusing a carryover on
different lists; the `eic.clergy` wording; `qc_tiebreak` refusing when the other claimants are not taxpayers; 232 of
the 245 `mutation.json` cases without `f1040.withheld_other_any`, all re-measured); T-312 the redraft's choices that
DECISIONS.md does not settle (the rest of N5); T-313 the missing personas (N12); T-314 the rest of the New York lane
(N13).

## Audit proposals rejected or changed

- **N1 (land the redraft):** this landing is that work, so no row was added.
- **N3 (stale tools):** overtaken. The landing mended `ui/test_browser.mjs`, `tools/engines/*`, `umbrella-what-if.ts`,
  `tools/coverage/tree.json` and `docs/COVERAGE.md`, `gate_frequencies.yaml`, `limits.json` and `serve-check.ts`
  (landing.md section 3). Some items were not added:
  - `research/audits/.../f5695_no_part2.json` is a historical audit record.
  - `fix_rows.py` does not exist at `tools/coverage/`.
  - The `scope.schedule1` pin names a line that still exists as a computed line.
- **N5:** most items are settled in DECISIONS.md (the four scope questions, the birth-year range, and the eight items
  in its table). Only the unsettled items went to T-312.
- **N4 / T-262:** kept as separate rows that cross-refer, because T-262 is a generator fix.
- **Audit T-260, T-258, T-263, T-273, T-274, T-275, T-279, T-283:** already applied on main (83c7d1c0 or earlier).
- **Original-handoff observations:**
  - The `f8959.unsupported` mislabel is fixed in the tree (both the label and the note), so no row was added.
  - The `asset.bonus` observation (m4) is fixed by the mutation patch (land3-mutate.md), so no row was added.
  - The "112 cases" became the measured 232 of 245.
- **landing-01 to -13:** only 05 and 08 remain in `bug_pending/`. land3-consumers.md says the others were fixed. Its
  note about amending pending entries is for the coordinator, not for the register.

## Checks

- `python3 tools/check_docs_conventions.py`: OK.
- `python3 tools/self_tests.py --group bookkeeping`: 8 passed.
- `python3 tools/test_bookkeeping_tools.py`: 17 tests OK.

## Inferred, not verified

The rest-of-work lists in T-302, T-303, T-305 and T-308 to T-314 relay the lanes' notes and the audit, with their
sources named. I did not re-walk them on the landed tree. Some may have been changed by the landing's later fixes;
for example land3-consumers widened `scope.archer_msa`, which bears on T-308's Archer item. T-299's status ("paid
reviews running") comes from the caller's brief.
