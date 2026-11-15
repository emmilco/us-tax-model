# Lane land3-docs: current-state documents after the landing of the interview redraft

Agent: claude-opus-5-5, judgment class, tax year 2025, jurisdiction us. Worktree `.claude/worktrees/landing`, not
committed. Documentation prose only; no build, render, check-all, review or model call.

## Files changed

- `interview/README.md`: the `full` profile's targets as `interview/2025/full.yaml` lists them (adds the
  `clcw_next_year` lines, `clcw.figures_notice`, `s179.line13`, and `s1.line10`, `s1a.line7`, `s1a.line15`,
  `sa.line17`, `s2.other`); "Coverage rows" names the files as they now are (19, `ny.yaml` for the New York part),
  its example row answers `household.ever_married`/`married_dec31` (as `opening.married_picks_single` now does), the
  example answer key is `person[taxpayer].birth_year` (`age65` is no longer a question); the HSA block is order 190
  (was 9) and includes `person.age55_at_year_end`; "Question data" names `seq`, `group` and `tick`.
- `tools/README.md`: the withholding example in "Test-data defaults" reads `household.married_dec31` (the default as
  `fixtures/2025/defaults.json` has it); `household.married` is no longer an input.
- `tools/transcription/README.md`: "What is compared" says how a shared marker is keyed, `(screen)` qualified as
  `(screen) (<id>)` only where two or more computed lines carry it, shown bare in the request, matched back by id
  (`marker_keys`, `prompt_marker`, `second_keys`), and that duplicate keys and duplicate record parts are refused.
- `PROJECT_INDEX.md`: the bank's `order`/`seq` and tick-box fields; what a persona is; the protocol "since landed on
  `main`"; a description of `docs/provisional/`; `interview-order`'s self-test in check-all; tick-groups as the
  check-all step `tick_groups` (was "in `tools/draft_check.sh`") over `full` and `ny`; the empty 2025 year-id list; a
  new row for `tools/year_free_names.json`; the `age.cut_<N>` parameters; a naming convention for year-free ids.
- `docs/TRUST.md`, section 10: the coverage-row walk and the tick-box group check, and what neither shows.
- `docs/2026-11-13_interview_construction_protocol.md`: one "Since written" line (dated document; pointer only):
  the redraft is on `main`, `tools/draft_check.sh` is removed, its checks run in check-all.
- `docs/provisional/STATUS.md`: one "Historical" line at the head, pointing at `lanes/landing.md`, `lanes/land3-*.md`
  and the current documents. Judged historical rather than rewritten: it is the coordinator's 2026-11-13 status of
  drafts 1 and 2 in the clone, and the landing's own record is `lanes/landing.md`.

Already current before this lane (checked, not changed): the tick-box, blocks and persona sections of
`interview/README.md`, the renamed-document carry in `tools/README.md`, the README coverage table and
`docs/COVERAGE.md` (generated: 234 gates, 193 situations).

## Grounded

Counted or read in the tree: coverage rows 496 in 19 files; fixture cases 1987 federal, 357 New York; bank 851 questions, 44 groups, 84 order numbers, 32 questions at order 190; `rare_credits` at order 290
with three members; tick-group limits 2 to 6 members, 12-word labels, 25-word headings (`tick-groups.ts`);
`tick_groups` in `check_all_steps.sh` and the three self-test rows in `self_tests.py`; `tools/year_ids.json` 2025
`ids` empty; `tools/year_free_names.json` 55 entries (16 input, 38 computed, 1 document); `age.cut_*` in
`params/2025.yaml`, read by `person.yaml` and `f8889.yaml`; `draft-walk`'s default output `docs/provisional/walks/after`;
the `(screen)` key code in `transcribe.py` and the duplicate-part refusal in `review_store.py`; every check of the
removed `draft_check.sh` (copy in `landing_work/removed_tools/`) is a check-all step or a `self_tests.py` row.

## Not verified, or left stale on purpose

- Report-quoted figures in `README.md` and `docs/TRUST.md` are stale, but were already stale at `83c7d1c0` and the
  reports are being regenerated: "6,114,183 line values across 2,168 cases" (the report at HEAD said 6,550,210 and
  2,254; the tree's report now says 7,671,870 and 2,254, but counts 1854 fixture cases where the tree has 1987, so it
  predates the landing's fixtures), TRUST's "2,722 mutants, 113 surviving" (report: 7,476 and 558; mutation pins still
  being redone). Update after the final check-all run.
- `README.md` "180 of the 188 refusal gates" quotes `reports/2025/filer_coverage.md` of 2026-11-01 (hand-run
  `estimate.py`). By the tool's own definition the tree now has 234 gates, 18 mapped, 216 unmeasured. Needs a rerun
  of the estimate, not a prose edit.
- `CLAUDE.md` still says the redraft is provisional "until the owner adopts it"; outside this lane's files.
- `interview/2025/personas/` has two files numbered 13 (`13_ira_saver`, `13_self_employed_actual_vehicle_computer`).
- The coverage-row example in `interview/README.md` is illustrative; it was not walked.

## Historical, left alone

All dated documents in `docs/` except the protocol's pointer line (including the 2026-11-11 redesign, year-free ids
and rules-catalog documents, which describe the pre-landing tree as of their dates); `docs/provisional/` other than
`STATUS.md` (`NORMS.md`, `MAP.md`, `DECISIONS.md`, lane notes, walks); `research/`; the files this lane may not touch
(handoffs, `TASKS*.md`, `BUG_INVENTORY.md`, `bug_pending/`, `changes/2026/README.md`).

## Check

`python3 tools/check_docs_conventions.py`: "docs conventions OK (35 documents in docs/; handoff entries within 2)",
exit 0; `--self-test` ok.
