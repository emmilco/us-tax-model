# Handoff: the queue cleared; Stage 9 (earned income credit) done

Read `HANDOFF.md` first, then `TASKS.md`, then this file; `HANDOFF-STAGE-8.md`
and `HANDOFF-STAGE-7.md` describe the earlier stages. `PROJECT_INDEX.md` is
current; `BUG_INVENTORY.md` has 29 entries.

## What was done (2026-10-17, after `289d583`)

1. **T-021 commit guard.** `npm run check-all` runs `tools/check_all.sh`, which
   records the tested tree's hash in `.git/check-all-green` (green only if
   nothing outside `reports/` and `rendered/` changed during the run).
   `tools/hooks/pre-commit` refuses any other tree, partial stages included.
   Enable once per clone: `git config core.hooksPath tools/hooks`.
2. **T-016.** The Stage 2 interview check walks the questions the interview
   asks instead of every flag combination.
3. **T-025 extraction.** Mixed pages are cut into bands with their own gutters;
   a line starting inside a gutter belongs to the column on its right (the
   flow-chart pages of the EIC and dependent instructions now read in order).
   Every review was rerun and ruled; BUG-0025 (review tools parsed a draft
   YAML block) was fixed.
4. **T-015 class M** for the collections (per entry) and for `tax_on_amount`
   and `tcw` (per instance).
5. **Stage 9, the earned income credit (T-018).**
   - `forms/2025/eic.yaml`: Steps 1 to 5 as helpers in flow-chart order, then
     Worksheet A lines 1 to 6; `eic.credit` feeds Form 1040 line 27a. A filer
     whose AGI is at or above the largest Step 1 limit stops before any person
     is counted, so high-income filers are never asked EIC questions (the
     interview orders the EIC questions after income).
   - The EIC Table: `tables/2025/eic_0.yaml` to `eic_3.yaml`, written by
     `tools/extract_eic_table.py` (footnoted rows split at their amounts) and
     checked cell by cell against Rev. Proc. 2024-40 in the `conjecture` step
     (11,008 cells, none more than $1 from the formula; the bands containing the
     earned income amount print the maximum).
   - Inputs added: Form 1040 line 2a; per person, lived with you in the United
     States for more than half of 2025; for the filer, could be a qualifying
     child of another person, born before January 2, 2001, main home in the
     United States, married (head of household only).
   - Schedule 8812 line 18a follows the Earned Income Chart.
   - Refused with citations: Worksheet B (self-employment, clergy, church
     employees, statutory employees), married filers (Step 3 questions 3 to 5,
     the separated-spouse rule), Form 2555, nonresident aliens, Schedule E and
     Form 8814, combat pay, Medicaid waiver payments, the tie-breaker and
     married-child rules.
   - Evidence: `fixtures/2025/stage9.json` (38 cases, every value predicted by
     hand from the printed pages before recording); class M on `eic`, `f1040`,
     `s8812`, `dependent` (new jobs; Worksheet lines past a STOP are a standing
     representation ruling); transcription and render reviews of every changed
     document; the engine differential now compares line 27a (Tax-Calculator:
     820 exact, 180 within the table-versus-formula explanation, none
     unexplained; PolicyEngine-US excludes the returns with 17- to 23-year-old
     students, as for T-019); evaluator agreement clean; mutation 87.9% raw,
     95.2% adjusted, no unexplained survivor on the Stage 9 lines.
   - Defects caught: BUG-0026 (`table_lookup` turned a refused key into an
     unknown), BUG-0027 to BUG-0029 (wording of the months-lived and
     lived-in-the-United-States questions).

## Facts a fresh session needs

- Stage 8 fixtures with low-wage returns now carry the EIC inputs; their notes
  say how each EIC figure was read from the table.
- The engine differential's Tax-Calculator adapter turns off both random
  take-up draws (`actc_claim_prob_scale`, `eitc_claim_prob_scale`).
- `tools/transcription/check_logs.py` expects a class M log for every
  collection with a computed line and every shared definition.

## Open items (see TASKS.md)

- T-028: owner review of the Stage 9 choices (two ambiguity-register entries,
  refusing married head of household filers, the AGI shortcut).
- T-026 (an unread dependent helper), T-027 (Form 1040 lines 27b and 27c).
- T-011 the 2026 refetch; T-019 PolicyEngine students; the earlier open items.
