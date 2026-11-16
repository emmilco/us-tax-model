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

## 4. A single filer whose answers meet the head of household tests is told to choose it

- **Decided.** A filer who chose "None of these: I was not married (single)", is unmarried, lists a dependent, paid
  over half the cost of keeping up the home, and has a person who qualifies them under Test 2 of head of household is
  refused with the remedy "Go back and choose head of household" (gate `household.hoh_missed`; helpers
  `household.dependents_listed`, `household.dependents_any`, `household.hoh_missed_test2`, `household.hoh_missed_cost`,
  `household.test2_lived_persons`, `household.hoh_missed_person`; the refusal hangs on `household.hoh_fails`, so it
  reaches Form 1040 line 12e). The tests are read in that order (a choose at each step), so a single filer with no
  dependent is asked nothing new, one with a dependent is asked `household.home_cost`, and only after a Yes are the
  dependent's head of household facts read; no existing expectation of the six fixtures first reported moved. Test 1
  (a parent's separate home) is not checked: reading it per dependent before the relationship is known made
  `interview-rules` fail, and doing it in order needs a line in `dependent.yaml` (another lane's form). Class M cases
  that list a dependent on a single return were given one input, `household.home_cost: false` (inputs only):
  `classm.f8880.4`, `classm.f8863.4`, `classm.s3.2`, `classm.tcw.3`, `classm.tcw.7`, `classm.tcw.8`, `classm.tcw.10`
  and, in `classm.deepseek.json`, `classm.s3.4`, `classm.f8880.4`, `classm.f8863.4`. One case is left for the coordinator: `classm.sdtw.5` states a single filer who paid over half the home cost
  for a sibling who lived with them 10 months, so it is now refused (it was a head of household filer computed at
  single rates).
- **By.** The coordinator of the goal-1 round, 2026-11-15, approving lane g1-f9's design (T-304 item 1); the order of
  the tests and the omission of Test 1 are the lane's.
- **From.** `docs/provisional/lanes/g1-f9.md`, "T-304 (1)".
- **Shown.** Coverage rows `household.single_entitled_hoh` (refused at `household.hoh_missed`) and
  `household.single_parent_home_not_paid` (goes on past the head of household details) in
  `interview/2025/coverage/household_payments.yaml`.
- **To reverse.** Remove the refusal entry from `household.hoh_fails`, the helper lines and the gate, the two rows,
  and the inputs added to the class M cases.

## 5. Schedule 2: where the alternative minimum tax and the other Schedule 2 taxes refuse

- **Decided.** Each refusal sits on the line its tax belongs to, so neither waits for the other.
  - Line 21 no longer refuses on `s2.amt`. f1040s2 (2025) line 21 reads "Add lines 4, 7 through 16, 18, and 19. These
    are your total other taxes". The AMT is line 2, which only line 3 adds.
  - Line 2 refuses on `s2.amt` only.
  - Line 1z refuses on `s2.other` (the same refusal entry).
  - Line 3 has no refusal entries of its own. It is the sum of lines 1z and 2, and a sum returns its operands' first
    refusal, a refusal outranking an unknown (spec 4.7.2). So an `s2.other` item and an incentive stock option item
    are each told as soon as it is answered, and when both are true they arrive together on line 3, as line 1z's
    `s2.other` refusal.
- **Why.** With the AMT computed (T-307), `s2.amt` is settled only once the return's tax is known. Any refusal listed
  after it on one line would wait for the whole return, which conflicts with N11 (a refusal is told at its topic). The
  order first approved, line 3 refusing on `[s2.other, s2.amt]`, removed that wait for the `s2.other` items. It moved
  the wait onto the incentive stock option items instead (coverage rows `other.iso_kept`, `other.iso_vested_2025`).
- **By.** The coordinator of the goal-1 round, 2026-11-15, choosing option (b) of lane g1-f7b's report (section 7).
  Applied at integration B1.
- **Restated.** Expected values, each from f1040s2 (2025) and the case's facts:
  - `stage4.refuse.s2.amt` and `s2.reg.iso_vested_2025`: `s2.line21`, from refusal(s2.amt) to $0 (lane g1-f7b).
  - `stage4.refuse.s2.amt.simultaneous`: `s2.line21`, from refusal(s2.amt) to refusal(s2.other), and `s2.line3` to
    refusal(s2.other) (lane g1-f7b; line 1z comes first in line 3's sum).
  - `stage4.refuse.s2.other`: `s2.line2`, from refusal(s2.other) to $0 (B1). No AMT is owed on $100,000 of wages,
    single, so line 2 (Form 6251 line 11) is $0. Lines 3 and 21 still refuse on `s2.other`.
- **Shown.** Coverage rows `other.iso_kept` and `other.iso_vested_2025` (refused at `s2.amt` without waiting) and the
  `s2.other` rows of `interview/2025/coverage/other.yaml`.
- **To reverse.** Restore line 3's refusal list `[s2.other, s2.amt]`, drop line 1z's refusal, give line 2 back
  `s2.other`, and restate the expectations above.
