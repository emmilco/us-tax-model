# Lane sweep-tasks: the task register against the landing tree plus 2026 batches A and B

Agent: claude-opus-5-5, judgment class, year 2025, jurisdiction us. Worktree `.claude/worktrees/sweep-tasks` at
63a20efc (snapshot: landing tree a6e93a1d, then the 2026 batches). Edited only `TASKS.md`, `TASKS-DONE.md` (through
`tools/task_row.py`, plus four hand edits of task or due text: T-300, T-310 twice, T-328, T-329) and this file. No
commit, no build, no check-all, no paid review, no model call. "Landing commit", "2026 batch A" and "2026 batch B" in
a status mean commits that do not exist yet. Lane notes are testimony; every count below was taken on this tree on
2026-11-15 unless a lane note is named as its source.

## Rows moved to TASKS-DONE

| Row | Status | Evidence |
|---|---|---|
| T-295 | done (2026 batch A) | Every item is in the tree. Federal adoption without New York: `years.json` `ny_adopted`, `jurisdiction.py --ny-status`, `build.ts` `dropNyConflicts`. `placed_year` `extends_with_year` and the `recovery_year` re-derivation (`year_diff.py`). Sidecars (`year_carry.py` `write_sidecar`). Coverage, contract-bank and twins carry (`carry_reviews`, `carry_contracts`, `required(year)`). `build_fresh.py --year`. `ny_fixtures.py --out` and its tracked-file refusal. The NY `edition_marker` (4 rows). `check_year_ids.py` refuses a year with no build. The `year_changes` and `year_diff` self-tests pass |
| T-299 | done in part (landing commit) | Adjudication lanes land3-adj1 to adj14; a "Landing round" section in 40 adjudication files. The rest is T-318 |
| T-296 | done in part (batch B) | `year_changes.py --check`: 130 entries, 1256 operations in 56 files, all apply, no `s2.line20` await. 80 of the 83 entries that need operations are written. `carry_defaults`; `amb.2026.gift_floor_base` in `sa.yaml`. The rest is T-319 and T-317 |
| T-297 | done in part (batch A) | D7 and D8 are in `propose_params.py`; the staged file has 307 values and 95 unsourced. The four tables are staged. Line 8 reads `dc_rate` by status (`f2441.yaml`). The qss corrections were made by P1, `tax_year` in the server by R4. The rest is T-320 |
| T-298 | done in part (batch A) | `rate_schedule.yaml`, `params/2025.yaml` and `conjecture.ts` are corrected. The rest is T-321: grep finds `s1.yaml:240,319`, 4 locators in `fixtures/2025/s1.json` and `ambiguities/2025.yaml:84` |

## Rows added

- T-317: the R5 draft-adoption rehearsal. Not run: no `tools/year_rehearse.sh` and no rehearsal doc.
- T-318: the sampled reviews (the rest of T-299).
- T-319: the change-map entries not yet written: C-SCHED-36 (Form 4952; no lane took it) and C-PRI-11's line 14.
- T-320: the 2026 parameters and tables still to do. The i8962 draft is now archived, so the ptc table can be proposed.
- T-321: the Rev. Proc. 2024-40 locators still to correct.
- T-322: draft-to-final flips and the weekly refresh. Two entries are all-final now: C-PEOP-02 and C-SCHED-16.
- T-323: references in year-shared code to removed ids. 414 in 8 files (`year_shared_refs.py`). Also the
  `f8959.line18` meaning change, which the tool does not list.
- T-324: years and amounts written in text at adoption. This was split from T-300. It covers R6's classed list of
  2,875 lines, the birth years, the $5,200 and $5,000 literals, and the generic Schedule 2 locators.
- T-325: the siblings check for fixes made only in operations. The check is not exempted (pending entry ty26-o3b-01, since assigned BUG-0651).
- T-326: 2026 decisions for the owner. They are the plan's D1 to D14 (D12 among them), O2's two decisions, O4's
  wording, O9's `forty`, ty26-o7-01, ty26-o9-01, R3's ambiguity reading, and R2's own-year rule.
- T-327: adoption data that operations do not reach. These are `miles_business` answers, `forty` cases, cases naming
  removed f5695 ids, the twins restatement, coverage rows and personas, the seq of `scveh.loan_interest`, and the
  stale class M lines from changed enums.
- T-328: entries waiting on unpublished documents (O10). The i8962 and p590a items can be written now from the drafts.
- T-329: `tier_paths.py --self-test` fails on 4 entries (draft-walk.ts, tick-groups-check.ts, tick-groups.ts,
  ny_fixtures.py). This fails the bookkeeping self-tests now.

## Rows changed

| Row | Change |
|---|---|
| T-011 | Status: the preparation now runs by ty26-plan.md. Archive state per S1. |
| T-094 | Counts: 526, not 588 (consumers 307, instruction_cites 120, limits 67, operands 19, input_quotes 6, signs 5, screens 2). |
| T-256 | Phase 3: the paid round is done (T-299) and the sampled reviews are T-318. The 2026 batches are named. |
| T-262 | Counts: 7 of 279 cases in `classm.json`, not 11 of 266. `classm.deepseek.json` still has 8 of 113. `generate.ts:417` is unchanged. |
| T-283 | Now names BUG-0625. |
| T-300 | Narrowed to `clcw26.json` (still present), year-carrying case ids and the five names. The year literals moved to T-324, the 2025-tree decision to T-326. |
| T-303 | The review of the headings points at T-318. |
| T-305, T-312 | Due: the paid round finished without them. None of T-312's items is in DECISIONS.md (grep). |
| T-310 | The pending entries landing-05 and -08 (since assigned BUG-0642 and BUG-0643) are removed: the landing fixed them (`scope.nol_if_business_before` is gone, `s2.iso_vested` is in s2; the pending entries' Fix fields are filled). The due cell was changed to match. |

Left as they were, with what was checked:
- T-002: `f1040.line1z` is 1a plus 1e.
- T-003: `sd.filed` still reads `sd.line18` and `sd.line19`.
- T-005: line 8 copies line 6.
- T-034, T-294: `filer_coverage.md` was last generated 2026-11-01.
- T-268: no 301.7701-7 in `sources/2025`.
- T-270: neither input is in `generate.ts`.
- T-280: 90 `pinned(`.
- T-308: the Archer MSA is still asked three times (`scope.archer_msa`, `person.x_archer_excess`, `f8889.archer`).
- T-316: two persona files numbered 13; the `none` test is in `siblings.py:283`.

## Rows not verified, and why

- T-301, T-302, T-304, T-306, T-307, T-309, T-311, T-313 and T-314: their item lists relay redraft-lane notes. I did
  not re-walk them. The batches did not touch `forms/2025` or `interview/2025` (the only 2025 data the batches changed
  are `params/2025.yaml` and `tables/2025/rate_schedule.yaml`), so the landing-time state stands as land3-tasks.md
  recorded it.
- T-272: its counts need the built full profile, and the worktree has no build.
- T-276 and T-290: the catalog sweep was not rerun.
- T-012, T-040, T-151, T-181, T-208, T-236, T-244, T-246, T-247, T-249, T-250, T-252, T-253, T-288, T-289, T-291 and
  T-292: unaffected by the batches, and not re-measured.
- T-320's "75 draft, 35 derived" comes from the ty26-p2.md note. The 95 unsourced is counted.

## Open bugs not covered by any open row

Method: parse `BUG_INVENTORY.md` (630 entries). An entry counts as open when its Fix (or Status, Disposition or
Proposed disposition) says open, or when it has no fix field. It is set aside when a later entry closes it (a
`Closes` field, or a later entry that names it as fixed or resolved, such as BUG-0271, BUG-0492, BUG-0577, BUG-0590)
or when a done row closed it (BUG-0094 by T-086, BUG-0138 by T-065). Heuristic: an entry closed only in prose I did not
match is listed wrongly. I did not check whether the landing's redraft fixed any of these without a closing entry,
and many say "at the form's next substantive change", which the landing was for most forms.

70 entries:

- BUG-0092, 0100, 0184, 0432
- BUG-0433 to 0435, 0438, 0439, 0445, 0447, 0449 to 0451, 0453, 0455, 0456, 0458, 0465, 0488, 0489
- BUG-0502 to 0511, 0515, 0517 to 0521, 0530 to 0532, 0535, 0537, 0539 to 0541, 0546 to 0549, 0551, 0554, 0555, 0559,
  0560, 0562, 0563, 0565, 0569 to 0573, 0575, 0576
- BUG-0593 to 0595, 0597
- BUG-0605, 0606: T-277 left them open; T-306 is related.

Two entries have no fix and no open marker: BUG-0314 (probably closed by BUG-0369 and BUG-0393) and BUG-0341. I did
not settle them.

Pending entries (`bug_pending/`, ids assigned at the merge):
- ty26-o2-01 and ty26-o6-01 (one defect) and ty26-o3a-01: fixed by R3's anchor fix and interview operation kinds
  (`year_changes.py`, self-test 56 cases). Their Fix fields still read as proposals or "not fixed", which the
  coordinator should complete.
- ty26-o5-02: half open (T-327).
- ty26-o7-01 and ty26-o9-01: owner decisions (T-326).
- The land3 lows: T-315.

## Checks

- `python3 tools/check_docs_conventions.py`: OK (35 documents).
- `python3 tools/self_tests.py --group bookkeeping`: two failures, both not from this lane's edits.
  - `green_self_test`: `tier_paths.py --self-test` fails on the four entries of T-329, a defect of the tree.
  - `siblings_self_test`: it asserts "sa.dependent should reach eic.step4". `siblings.py` reads `canonical/2025`
    (`load_docs`), which this worktree lacks, because the brief forbids a build. Inferred, not verified: it would pass
    with a build.
  - The rest pass, among them `test_bookkeeping_tools` (17 OK), claims, bug_inventory, docs_conventions, agent runs
    and the hooks.
- My own parse of the tables: every TASKS.md row has 5 cells, and no id is in both registers. In TASKS-DONE.md, T-219
  has 6 cells, from before this lane.

## For the coordinator (not register work)

- The "Written" column of `changes/2026/README.md` predates batch B. Its prose still names `f1040.form1062` and
  "five parameters". `ADOPTION.md` counts 91 documents and 55 drafts, where S1 counted 96 and 57. These are for the
  docs lane.
