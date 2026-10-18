# Handoff: Stage 11 (unemployment compensation and the common Schedule 1 adjustments) done

Read `HANDOFF.md` first, then `TASKS.md`, then this file; `HANDOFF-STAGE-10.md`
describes the stage before and the overnight queue after it. `PROJECT_INDEX.md`
is current; `BUG_INVENTORY.md` has 34 entries.

## What was done (2026-10-18, after `e6f746f`)

1. **Scope (owner-confirmed).** Schedule 1 line 7 (unemployment compensation,
   Form 1099-G box 1, less a 2025 overpayment repaid), line 11 (educator
   expenses, up to $300 for an eligible educator), line 13 (the HSA deduction,
   Form 8889 Part I) and line 21 (student loan interest, its worksheet). Every
   other Schedule 1 item stays refused through the reworded `scope.schedule1`.
2. **The `prorate` atom** (owner's choice over refusing the phase-out range):
   amount times (part / whole), the ratio rounded half-up to a stated number of
   places and kept between 0 and 1, the product half-up to the cent. Lean
   definition, lemmas (non-negative, at most the amount, monotone in the amount
   and the part) and evaluator case; engine, checker, renderer, mutation and
   class M walkers, schema, transcription grammar, spec.
3. **Sources.** `f1040s1`, `f8889`, `i8889` (2025) and `f1099g` (Rev. March 2024,
   the continuous-use form for calendar 2025; the current URL serves the
   December 2026 revision, which was discarded).
4. **Forms.**
   - `forms/2025/s1.yaml`: lines 7, 10, 11, 13, 21, 26 (and the line 7 box and
     amount repaid as display lines). Refused: contributions to a governmental
     unemployment program and repayments of earlier-year unemployment.
   - `forms/2025/f8889.yaml`: Part I for an unmarried filer, with the full Line 3
     Limitation Chart and Worksheet (owner's choice) from two counts (eligible
     months and family months), the age-55 amounts, the rule for a change of
     coverage type and the last-month rule as the filer's election. Refused:
     married filers, Parts II and III, Archer MSAs, qualified HSA funding
     distributions, prior-year excess, inherited HSAs, impossible month counts
     and excess contributions (Form 5329).
   - `forms/2025/sli.yaml`: the worksheet; the ratio rounded to three places
     (owner, `amb.2025.sli_ratio_places`); a separate "claimed as a dependent"
     question (owner); Pub. 970 cases refused through `sa.excluded_income`.
   - Form 1040 lines 8 and 10 copy Schedule 1 lines 10 and 26; the Social
     Security Benefits Worksheet line 6 is Schedule 1 lines 11 and 13.
5. **Readings recorded.** `amb.2025.sli_ratio_places` (owner) and
   `amb.2025.hsa_last_month_change` (rule 4 of the line 3 instructions applied to
   a last-month-rule filer who changed coverage type; found by class M, adopted as
   the strictly accurate reading; the owner confirmed rule 4, T-033).

## Evidence

- `fixtures/2025/stage11.json`: 31 cases, every value predicted by hand before
  recording, including the ratio's rounding boundary for both divisors.
- Engine differential: Form 1040 line 10 against PolicyEngine-US (above-the-line
  deductions less its capital loss allowance) and Tax-Calculator (`c02900`);
  unemployment, educator expenses and the HSA deduction feed both engines.
  Stated limitations: PolicyEngine-US's exact phase-out ratio (16 returns);
  Tax-Calculator's supplied student loan deduction (146 returns). Two cent-level
  float32 differences on line 15 are explained; the old gen-00816 entry was
  replaced because the generated cases moved.
- Mutation: no unexplained survivor on the Stage 11 lines (two equivalences on
  the worksheet's skip, `prorateSkip` in `engine/src/mutate.ts`).
- Evaluator agreement unchanged in kind (Lean and TypeScript agree on every case).
- Reviews: transcription, render and class M of the three new forms, `f1040`,
  `ssb` and `scope`; screen review of `s1.uc_unsupported`, `f8889.unsupported`
  and the reworded `scope.schedule1` (two rounds; one round-1 narrowing of the
  unemployment screen was reverted).

## Facts a fresh session needs

- The Stage 11 generator script is not in the repository; the forms are
  ordinary YAML and can be edited directly.
- `screen_review.py --screens x` rewrites `screen_review.json` with only those
  screens; merge back into the committed file.

## Open items (see TASKS.md)

- T-030 (collection entry lines), T-011 (the 2026 refetch), and the earlier open items.
