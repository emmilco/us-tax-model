# Lane sweep-docs: the main documents after the landing and the two 2026 batches

Agent: claude-opus-5-5, judgment class, tax year 2025, jurisdiction us. Worktree `.claude/worktrees/sweep-docs`
(detached at `63a20efc`), not committed. Documentation prose only. No build, no check-all, no paid review and no
model call. The register files, `bug_pending/`, `handoffs/` and `HANDOFF-NEXT-SESSION.md` were not touched.

## Files changed

- `README.md`: the ambiguity register has 93 entries, 92 of them linked (was 91 and 79). Citations: 5,767 anchors and
  6,384 quotes (was 3,306 and 2,731). `opaque`: 0 of 4,500 lines (was 2,951). The full-profile walk covers the 11
  whole returns (was "five Stage 5"), plus one sentence on the roughly 500 coverage rows. The completeness review
  now covers every form and is sampled per release (was "3 forms, the rest in a baseline"). Reviews run under Claude
  only; the DeepSeek reviews are inactive and kept. The scoreboard is 559 of 2,913 (19.2%), 446 M and 223 E, from the
  report of 2026-11-14. Second family: 64 of 136 qualified (the report of 2026-11-09). The bug inventory has 630
  entries (was 263). The fast tier skips the interview length report, not "the human-review tooling", and the
  full-path list names the engine differential. The 180-of-188 gate figure now carries its date (2026-11-01) and
  the current 234 gates and 193 situations. The "Now" paragraph follows the charter's order of work. The TY2026
  paragraph describes the operations and line-scoped reviews and gives the finals as December 2026 to January 2027.
  "Not yet" now names the local web page and New York IT-201.
- `PROJECT_INDEX.md`:
  - The intro points at the charter, not the retired integrity plan, and adds the 2026 status.
  - Fixed an unclosed parenthesis in the HANDOFF row.
  - The CLAUDE.md row lists what that file covers now.
  - The docs row: the charter in place of the plan revision and process optimization, both retired; BUG-0111's
    patch is integrated; `ty2026/` and `ny/` described.
  - The New York rows: dropped "branch ny/2025-foundation" and "provisional pending decisions"; listed
    `INTEGRATION.md` and the year-handling doc.
  - The `changes/<year>/` row has all 16 operation kinds, split files and the 2026 counts.
  - The year-tool rows describe what the tools do now: `year_diff.py --adopt` carries, extends enums and lists
    literals and shared refs; `year_changes.py` has its new failures and notes; `check_year_ids.py` refuses a year
    with no build; `fixtures_year.py` writes the new defaults; `propose_params.py` derives two kinds by rule;
    `jurisdiction.py` has `--ny-status`; the steps script skips New York steps.
  - The false-no and completeness review rows: sampled per release, rounds r2 to r8, no baseline left.
  - The sources/2026 row gives the 96/57 count.
  - New rows: `tools/year_shared_refs.py`, `research/ty2026/`, `tools/claims.py`, `tools/claude_hooks/`.
  - The adoption convention mentions `ny_adopted`.
- `docs/TRUST.md`:
  - The intro no longer says "as of 2026-10-31; the reports are current".
  - Figures refreshed from reports present in the tree: citations, `opaque` (coverage.md), second family,
    scoreboard, ambiguity links.
  - Section 10: the interview walks are the `walk`-marked cases (11 whole returns), and one sentence on
    `interview-rules`.
  - Section 12: the completeness review has records for all 62 forms and is sampled per release, and the release
    gate is described.
- `docs/consolidation_charter.md`, section 7, current-state statements only: `years.json` with `ny_adopted`, the 2026
  preparation, "what a rollover cost when measured (11-09)". A "State on 2026-11-15" paragraph says the six procedure
  items are built, with the tool for each. Under item 4, the ambiguity ids keep `amb.2025.*` by `check_year_ids.py`'s
  design. The rules are unchanged.
- `docs/ty2026/ADOPTION.md`:
  - The header states what is staged where and that nothing is adopted.
  - The step tables: 96/57 documents and the 11-14 refresh; staged parameters 307 (123 final, 75 draft, 14 derived,
    95 none; 12 new, 15 retired) and staged tables; `changes/2026/` with 130 entries and 1,256 operations, 90
    change-map entries, 122 on drafts.
  - Steps 3 to 8 are rewritten for operations, carries, defaults, layouts and `ny_adopted`. Removed: the stale
    "`--adopt` refuses while `s2.line20`..." and "make the completeness prompt year-aware first (T-230)" (done).
  - The New York section says the New York steps are skipped, not failed.
  - The order section says which entries are written and which three wording entries have no operation.
  - The missing-documents section adds the 11-14 drafts.
- `changes/2026/README.md`:
  - The "Written" column now marks all 90 entries that have operations (it marked 14). Nothing was un-marked.
  - The prose on origins covers the O and W lanes and `tcw.yaml`.
  - `f1040.form1062` replaced by `s3.farmland`/`s3.farmland_deferral`.
  - The `s2.line20` await is now resolved.
  - Twelve undefined parameters, not five, all staged.
  - The register and interview-file operations by file.
  - The classification is described as made before the operations were written.
  - The per-file table was already correct (verified against `load_changes`).
- `interview/README.md`: "Checks" names the `walk`-marked cases, not the deleted `stage2.json` to `stage5.json`. The
  API table has `tax_year` (R4). "Before the provisional redraft" becomes "before the redraft of 2026-11-12/13".
- `tools/README.md`: the EIC Table section cites Rev. Proc. 2024-40 section 2.06(1) (P1), not 3.06(1). "Toolchain
  inspected" says the Lean toolchain is pinned. "Process hooks" says class M builds only when the build is stale.
- `docs/ny/INTEGRATION.md`: a "Historical" banner (the branch is on main, `bdac4121`).
- Pointers in dated documents: `docs/ny/2026-11-14_ny_year_handling.md` (D1 reversed; steps 18, 22 and 24, Y15 and
  Y19 done) and `docs/2026-11-14_year_change_operations.md` (built and extended; 130/1,256).

Already current (checked, not changed):
- `CLAUDE.md` (the landing had updated it; its cutoff, slot default, `--whole`, hooks and Fable facts verified).
- Every check-all step name cited in the in-scope docs exists in `check_all_steps.sh`.
- `tools/README.md`'s "New York years", "Year changes as operations", "Proposing a year's parameters", "Page
  layouts", sampled reviews and rerun guards.
- `tools/transcription/README.md`'s year carry, `(screen)` keying, class M build skip and inactive families.

## Stale report figures left as they are (refresh after the final check-all)

`reports/2025/evaluator_agreement.md` in the tree counts 1,854 fixture cases. The tree holds 2,003 federal cases
(every `fixtures/2025/*.json` but `defaults.json` and `differential/`; 357 New York), so the report predates the
landing's fixtures. The figures that rest on it, and on the other full-tier reports, were not quoted:
- README "6,114,183 line values across 2,168 cases" and the same in TRUST section 6. The report says 7,671,870 and
  2,254.
- README "2,722 mutants, 113 survive, each with a written argument" and TRUST section 10 "2,722, 113, 95.8% / 100.0%".
  `mutation.md` says 7,476 mutants and 558 surviving, 299 of them provably equivalent. Mutation pins are being redone,
  so "each with a written argument" is not true of the tree's report either.
- The engine differential (1,700 returns, four engines, versions) agrees with its report. That report is also
  full-tier, so it may predate the tree.

The figures I did quote (citations, `coverage.md`'s `opaque` count, evidence) are fast-tier reports, regenerated on
every check-all, in the snapshot of 2026-11-14. `citations.md` counts 2,582 computed lines and the YAML has 2,581
federal, so it is close to current. That `evidence.md` matches the tree's fixtures is inferred, not verified.
`filer_coverage.md` (hand-run, 2026-11-01) is stale against 234 gates; the README now dates it.

## Not verified

- `docs/COVERAGE.md` (generated) was not regenerated or checked, because `tree.py --check` needs a build. Since the
  landing snapshot, the only change among its inputs is `params/2025.yaml` (citation locators and flags). Its gate
  text cites form lines, not parameters, so it is probably current, but that is inferred.
- `opaque`: 4,500 is `coverage.md`'s count. The YAML has 3,979 federal plus 525 New York lines, 4,504 in all, so the
  report is a few lines old.
- ADOPTION step 7 "check_logs must read a carried record's source snapshot rows against the 2025 manifest (not yet
  built)" was left as it was. `check_logs.py` compares a log's snapshot rows with the current year's manifest, and R2's
  rehearsal used unchanged sources, so the claim looks still true, but no real new edition has tested it.
- C-SCHED-36 ("assigned to no lane") rests on a grep of the ty26 lane notes.
- The TCW defect description in `changes/2026/README.md` is from the P2 note, not re-read in rp-25-32.
- The many remaining sections of `tools/README.md` and `tools/transcription/README.md` that batches A and B did not
  touch were spot-checked, not read line by line.

## Judged historical, left alone

- Every dated doc in `docs/` except the two pointers above.
- `docs/ny/DECISIONS.md` (a decided batch, 2026-11-04), `docs/ny/LOG.md` and `docs/ty2026/LOG.md` (session logs).
- `docs/ARGON_CLAUDE_DISCUSSION.md` (append-only).
- `docs/provisional/` (STATUS has its banner; NORMS, MAP and DECISIONS are working records).
- `research/`.

## For the coordinator

- Charter section 1 item 3 ("Federal coverage stays at 78.4%") and section 8 (phase 1 scope counts: 34 self-tests,
  125 scripts, 51 tracked-ignored files) were not re-measured. They are the owner's scope list.
- `rendered/2025/params.md` still prints "section 3.06(1)" and "3.32" for Rev. Proc. 2024-40, and is stale against
  `params/2025.yaml` (R6 noted it). It needs a render, not a prose edit.

## Check

`python3 tools/check_docs_conventions.py`: "docs conventions OK (35 documents in docs/; handoff entries within 2)",
exit 0; `--self-test` ok.
