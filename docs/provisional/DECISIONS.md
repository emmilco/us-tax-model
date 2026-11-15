# Decisions settled by the coordinator for the redraft

The owner delegated these to the coordinator on 2026-11-14, with the instruction to settle each question in the
direction the coordinator would recommend. Each entry says what was decided, by whom, the lane note it comes from,
and how to reverse it. "As built" means the redraft's lane made the choice and the coordinator kept it.

## 1. Four scope questions: back to what the old screen asked

- **Decided.** Three questions about a deduction ask whether the filer wants to claim it, as the old Schedule 1 screen
  did ("an adjustment on Schedule 1 line 12, 14 or 23"): `scope.reservist_expenses` (reserve or National Guard travel
  more than 100 miles from home), `scope.military_move` (a move under military orders) and
  `scope.performer_expenses` (a qualified performing artist's or fee-basis official's costs). Each help ends "To go
  on without it, answer No." (MAP Part 4.3: the wish is asked where the return is right without the thing wished
  for). The fourth, `scope.recovery`, is income, not a deduction: a return that leaves out a taxable recovery is not
  right, so it cannot be put as a wish. It is put back to the old screen's scope instead, a recovery that has to be
  reported ("requiring Schedule 1"): the question asks about an amount whose earlier deduction lowered the tax, and
  its help says that a recovery of a deduction that did not lower the tax is answered No.
- **By.** The coordinator, under the owner's delegation of 2026-11-14 (the recovery's form: the coordinator's reading
  of the same instruction, recorded here because it is not the wish).
- **From.** `docs/provisional/lanes/l9.md`, "Where I was unsure", item 2.
- **Shown.** Coverage rows in `interview/2025/coverage/scope.yaml`: for each of the four, the row that refuses (as
  before) and a row for the filer the fact-question refused and the old screen did not (the costs, no wish to deduct
  them; a recovery that gave no tax benefit), which completes.
- **To reverse.** Restore the four prompts (`source` and `label` in `forms/2025/scope.yaml`) and helps
  (`interview/2025/questions.yaml`) from the commit before this one, and delete the four completing rows.

## 2. A birth year is range-checked

- **Decided.** A birth year after the tax year, or more than 125 years before it, is refused as conflicting answers
  (the test `person.birth_year_bad`; the refusal `household.birth_year_bad`, explained in
  `interview/2025/conflict_checks.yaml`), not read as a very young or very old person. The bounds are the parameters `age.birth_year_latest` (the tax year) and `age.birth_year_earliest` (125
  years before it).
- **By.** The coordinator, under the owner's delegation of 2026-11-14.
- **From.** `docs/provisional/lanes/l4b.md`, step B ("Nothing checks the year typed ... A consistency check ... is
  not built").
- **Shown.** Coverage rows `opening.birth_year_after_tax_year` and `opening.birth_year_too_early` (refused);
  `opening.birth_year_earliest_accepted` and `opening.birth_year_latest_accepted` (the bounds themselves are not
  refused for the year).
- **To reverse.** Remove the three lines, the refusal entry on the household roster line, the conflict explanation,
  the two parameters and the four rows.

## 3. Choices of the redraft that stand as built

Each was made by the lane named; the coordinator keeps it under the owner's delegation of 2026-11-14.

| Decision | Lane note | To reverse |
|---|---|---|
| Tips from work that is not on the list of tipped occupations: the return completes with no deduction for them (no refusal) | `lanes/l3.md`, "Coverage rows" (`coverage/jobs.yaml`; `tipjob.other_work`) | make `tipjob.other_work` a refusing question |
| The marketplace question asks about the months of Marketplace insurance only ("While on Marketplace insurance ...") | `lanes/l8a.md`, "`f8962.other` ... taken apart" (the map's proposal, as built) | restore the whole-year wording of the question |
| The qualifying-child tie-breaker is asked as one plain question, whose Yes refuses (`dependent.qc_tiebreak`: the tie-breaker rules are outside the tool) | `lanes/l2a.md`, "The tie-breaker gate" and "Places I was unsure" | restore the 297-word screen |
| Five old Form 1099-R items (corrective distributions, recharacterizations, a qualified plan loan offset and the like, and a Form RRB-1099-R) are asked only by the code in box 7 and end at `retirement.bad_code`'s refusal | `lanes/l4a.md`, "Unsure, and review debt", item 3 | give each its own question beneath the code |
| Equipment acquired before September 28, 2017 is refused whatever year it was first used, as the old screen read (`asset.acquired_before_bonus_date`) | `lanes/l6b.md`, "For the owner", item 1 | ask it only of property placed in service this year, as for a vehicle |
| Support is asked in three answers (clearly less than half, clearly more than half, close or not sure), with the full test only on "close or not sure" (`dependent.self_support_view`, `dependent.supported_view`) | `lanes/l2a.md` | ask the full support tests directly |
| Two deduction wishes are asked of everyone: the sales tax election (`sa.sales_tax_wish`) and the choice to itemize (`sa.elect_itemize`) | `lanes/l7a.md`, "Not finished, in rank order", item 3 | ask each only when the return has an amount it acts on |
| New York: the wish to itemize on the New York return is asked of every New York filer (`ny_it201.ask.itemize`) | `lanes/ny.md`, "`ny_it201.ask.itemize`" | ask it only when the federal Schedule A holds an amount New York itemizes |
