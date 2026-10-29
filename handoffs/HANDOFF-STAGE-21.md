# Handoff: Stage 21 (Form 5329), built and reviewed

The fourth and last stage of the route to the first coverage goal (`docs/2026-10-26_plan_revision.md` section E). The
owner's decisions are in `research/premises/stage21-form-5329.decisions.md` (all recommended, 2026-10-29);
`sources/2025/PREMISES.md` records them; TASKS.md T-082. With it the estimate is **82.2%** (from 79.6%): the 80% goal of
the route is reached.

## Scope

- **D1:** Form 1099-R entries are children of `person`, as Form W-2 is; Form 1040 lines 4a to 5b and Form 8880's
  distributions sum over person. 107 entries in 77 cases were re-keyed (the decision batch said 115 in 83; the tree had
  107), 18 of them on joint returns, all left with the taxpayer; no value changed.
- **Computed:** Form 5329 Part I per person (`forms/2025/f5329.yaml`, an implicit per-person form) for codes 1 and S, with
  one exception per entry and the per-person limits of exceptions 05 (Schedule A line 4), 09 ($10,000 less earlier
  first-home distributions), 19 ($5,000 a birth or adoption), 22 ($10,300) and 23 ($1,000, one distribution a year), the
  25% rate on code S; the no-form path with the Schedule 2 line 8 box (D5); Part VII for the 2025 HSA excess with the
  year-end value; Schedule 2 line 8 and line 21. Code 3 on an IRA is accepted.
- **Refused:** each Form 1099-R's special cases (`retirement.screen_refused`: disaster recovery, a modified series of
  substantially equal payments, annuity or modified endowment contracts, repayments, the December 30-31 long-term care
  window, more than one exception; a code 2 exception covering only part, a code 4 or 7 that does not fit); exceptions on
  the wrong kind of account; Parts II to VI, VIII, IX and earlier-year excesses (`person.x_other`); employer HSA excess not
  in box 1; spouses whose medical exceptions together exceed Schedule A line 4; exception 23 on more than one distribution;
  and, as a session reading (`amb.2025.f5329_simple_limits`), a code S distribution beside a limited exception over its limit.

## How it was built

- Forms written by `/tmp/s21/gen.py` and `/tmp/s21/edits.py` (scratch; the YAML is authoritative), with every quote checked
  against the archived page. Sources `usc-26-72` and `usc-26-4973` archived as second printings (statutes stay uncleared for
  line citations; the lines cite p590b and i5329).
- **Official examples:** Tom Jones (p590b p. 29) and the teacher (p970 p. 56) agree with the evaluator; Tom Jones is put on
  the no-form path the instructions allow, where the example files the form (the tax is the same).
- **Blind predictions** (`reviews/2025/blind/stage21/`): ten returns, two predictors. After BUG-0201 both agree with the
  evaluator on every value but one predictor's arithmetic slip on E4 (145 values asserted).
- **Reviews:** fresh Claude and deepseek-flash reviews of f5329, retirement, person, f8889, s2, f1040 and f8880,
  adjudicated under `.transcription/proposed/stage21/BRIEF.md` in three rounds (f8889 and retirement re-reviewed after each
  round's fixes). Archives: `.transcription/archive/before-stage21-2026-10-29/`, `stage21-before-round2-2026-10-29/`,
  `stage21-before-round3-2026-10-29/`.
- **Mutation:** 19 survivors killed by targeted cases in `fixtures/2025/stage21.json` (18 Stage 21 lines, and
  `retirement.sav_gross`, whose earlier kill was lost, by `stage21.mut.sav_partial_rollover`).
- **Engines:** the generator draws early distributions (`putEarly`; `add_early`); UsTaxes compares Schedule 2 line 8 and
  Form 5329 lines 1 and 4 (limitations `early_exception`, `early_simple`, `early_spouse`, `early_tax_cents`,
  `hsa_excess_tax`); PolicyEngine, Tax-Calculator and OpenTaxSolver are excluded (`early_distribution_tax`).

## Findings (all in BUG_INVENTORY.md)

- BUG-0200 (over-refusal): the joint medical-exception refusal fired on single returns; caught by the scenario builder.
- BUG-0201 (value): more than one emergency distribution a year was excepted; caught by the blind predictions.
- BUG-0202 (value): a 2025 HSA excess withdrawn by the due date was taxed (D6's rewording had not been made).
- BUG-0203, 0205 (question wording, value): the account-value limits of exceptions 22 and 23, the 07 and 08 amounts,
  the three-year bar on 23, and a use test the source does not have on 05, 19 and 22.
- BUG-0204 (question wording): the code question did not offer codes 1, S and 3.
- BUG-0206 (reference evaluator, value-neutral): the Lean evaluator named a refusal gate on the enclosing person entry
  without the entry's key; caught by the evaluator comparison, the first run on Stage 21.
- Recorded in T-081: the Simplified Method and Credit Limit Worksheet helper lines stay visible where the worksheet does
  not apply (F3), and the Form 8880 lines after its line 7 stop.

## Facts a fresh session needs

- An implicit per-person form takes no inputs: put inputs on `person` (`person.x_hsa_value`), as eval rejects
  `person[p].f5329[form].<input>`.
- `choose` returns money only; count a person with `sum_over ... where` (`person.x_must`).
- Dump generated YAML without anchors (`/tmp/s19/gen.py` `_NoAlias`): two generated blocks in one file each define
  `&id001`, which the engine's YAML parser accepts and PyYAML (the estimator, the review tools) rejects.
- Statutes archived for Stages 18 to 21 are "pending inspection" in the manifest and cannot be cited by a line.
