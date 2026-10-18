# Handoff: Stage 10 (retirement income) done

Read `HANDOFF.md` first, then `TASKS.md`, then this file; `HANDOFF-STAGE-9.md`
describes the stage before. `PROJECT_INDEX.md` is current; `BUG_INVENTORY.md`
has 34 entries.

## What was done (2026-10-18, after `3a37103`)

1. **Scope (owner-confirmed).** Form 1099-R distributions (taxable amounts,
   rollovers, the Simplified Method) and the Social Security Benefits
   Worksheet. Refused with citations: Form 5329, Form 8606, the lump-sum
   election, and every special case on the per-distribution screen.
2. **The `multiply_count` atom** (owner's choice over restricting the
   Simplified Method to 12-month years): money times a Count, exact. Lean
   definition, five lemmas and the evaluator case; engine type rule (NonNeg
   when the amount is NonNeg), renderer, mutation and class M walkers, schema,
   transcription grammar, spec atom table and 6.3 property line.
3. **Sources.** `f1099r` and `i1099r` (2025 editions from the irs-prior URLs;
   the first fetch returned 2026 editions and was discarded).
4. **`forms/2025/retirement.yaml`**, one entry per Form 1099-R (collection
   `$retirement`):
   - IRA distributions go to Form 1040 lines 4a and 4b, pensions and annuities
     to 5a and 5b; a qualified Roth distribution (code Q) is $0 taxable; a
     rollover within 60 days or a direct rollover (code G, a rollover even
     with $0 in box 1) is subtracted and checks box 1 on line 4c or 5c; box 5
     is subtracted for a plan distribution outside the Simplified Method.
   - Simplified Method Worksheet lines 1 to 9 for an annuity with after-tax
     cost and a starting date after November 18, 1996 (Tables 1 and 2 as rate
     parameters `smw.table*`). Once the cost has been recovered in earlier
     years, the payments are fully taxable (box 1 on line 5b, no line 5a entry).
     Lines 10 and 11 (next year's carry-forward) are not encoded: collection
     lines are not shown on the values sheet (BUG-0033, T-030).
   - Refused: the special-cases screen (early distributions without an
     exception, QCDs, HSA funding, Form 8606 matters, Roth rollovers, Form 4972,
     nonqualified annuities, the public safety officer exclusion, death benefit
     exclusions, loan offsets, RRB-1099-R, the Civil Service alternative annuity,
     disability pensions partly excludable after a terrorist attack, returned
     and excess contributions, annuities starting before November 19, 1996 or
     under the General Rule); codes other than 7, 4, 2, G and Q, and a
     Roth IRA without code Q; a rollover of a Simplified Method annuity
     (owner's ruling: the text defers to Pub. 575).
5. **`forms/2025/ssb.yaml`**, the Social Security Benefits Worksheet (lines 1
   to 18), Form 1040 lines 6a to 6d. Asked only of filers with benefits;
   refused: the Pub. 915 exceptions, the lump-sum election, disability
   payments for injuries from a terrorist attack (`ssb.terror_disability`,
   added from the screen review), and line 6 (Schedule 1 adjustments).
6. **EIC fix (BUG-0034).** Step 4 asks `eic.born_after_1960` in the
   instructions' words instead of reading `sa.age65`, whose boundary is one day
   later (owner's ruling).
7. **Build check (BUG-0033).** `display` is rejected on any line of a
   collection form.

## Evidence

- `fixtures/2025/stage10.json`: 34 cases, every asserted value predicted by
  hand from the printed pages before recording (IRA and plan distributions
  together, partial and direct rollovers, Roth, every Table 1 and Table 2 rate,
  later-year and short-year annuities, cost recovered (with and without box 5),
  a code G distribution of $0, the worksheet's three
  paths, married filing separately together and apart, tax-exempt interest,
  every refusal). `stage9.eic.no_child.born_jan1_1961` for BUG-0034.
- Engine differential: Form 1040 line 6b against PolicyEngine-US
  (`tax_unit_taxable_social_security`) and Tax-Calculator (`c02500`), no
  unexplained difference; one 2-cent PolicyEngine difference on line 16 of a
  case with benefits (gen-00816) is explained in
  `fixtures/2025/differential/engine_investigations.json`.
- Mutation: no unexplained survivor on the Stage 10 lines. Three duplicate
  refusal gates are classed equivalent by `firstReadCarries` in
  `engine/src/mutate.ts` (structural facts re-checked on every run).
- Reviews: transcription and render comparison of `retirement`, `ssb`,
  `f1040`, `scope` and `eic`; class M on `retirement`, `ssb`, `f1040` and
  `eic`; the screen review of the reworded `retirement.special`. Findings that changed the encoding: the
  fully recovered cost (class M), the rollover of a Simplified Method annuity
  and annuities starting before November 19, 1996 (render; owner's rulings),
  code G as a rollover (class M), box 5 for recovered annuities
  (transcription), the EIC birth date (render, BUG-0034), and the screen
  additions above. The rest were ruled as equivalent, covered by a screen or
  input, or the standing STOP representation; the final retirement reviews ran
  before the box 5 change, which its ruling records. Cost of all review runs
  about $23 by the CLI estimate.

## Facts a fresh session needs

- Lines of a collection form are evaluated only when a reader reaches them;
  `eval` targets are the lines of non-collection forms. A fixture cannot
  assert an entry line that nothing reads.
- `screen_review.py --screens x` rewrites `reviews/2025/screens/screen_review.json`
  with only the screens it ran; merge the entry back into the committed file.
- The generators keep `eic.born_after_1960` consistent with `sa.age65`.

## Open items (see TASKS.md)

- T-030 (show collection entry lines; would bring back Simplified Method lines
  10 and 11).
- T-029, T-011 the 2026 refetch, T-019 PolicyEngine students, and the earlier
  open items.

## After Stage 10 (the owner's overnight queue: small fixes, Lean proofs, T-019, then the next coverage stage)

- T-029: Form 1040 line 2a is tax-exempt interest plus Form 1099-DIV box 12.
- T-014: the `g28` and `u1250` printed lines carry the worksheets' words.
- T-009: the render glossary includes invoked shared definitions.
- T-017: Lean lemmas for the `up` and `down` round rules; T-013: the Lean
  monotonicity table is complete and property `tax_monotone_by_method`
  checks each worksheet's tax separately. Termination and determinism of
  evaluation remain open (the Lean evaluator is a `partial def`).
