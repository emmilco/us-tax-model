# Proposed bug entries (package person-dep: T-119, T-120, T-121, T-123, T-127, T-177, T-184, T-185, T-101 for `household.credit_disallowed`)

Ids are placeholders; the integrator assigns BUG numbers. Dates are 2026-11-03.

## PENDING-1 — Form 2441 lines 18 to 20 left all of line 1e out of earned income, though only line 12 benefits are excluded (T-121)

- **Caught by:** hard1 f2441 L3 (T-092 split, 2026-10-31), T-121; premise checked in the person-dep pass.
- **Source:** i2441 p. 5, Line 18, "however, for purposes of lines 18 and 19, earned income doesn’t include any dependent care benefits shown on line 12"; p. 5, Line 13, "Enter on line 13 the amount you carried forward and used in 2025 during the grace period"; p. 5, Line 15, "Add the amounts on lines 12 and 13 and subtract from that total the amount on line 14"; p. 4, Lines 4 and 5, earned income includes "The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z".
- **Symptom:** `person.dc_earned_b` (lines 18 and 19) is W-2 box 1 plus self-employment earnings, without any of line 1e. Line 1e (line 26) is the taxable part of line 15, which pools line 12 and the line 13 grace-period carryover; the part that comes from line 13 is not "shown on line 12", so the instructions do not exclude it. The instructions give no rule for splitting line 26 between line 12 and line 13, and line 26 depends on line 18 through lines 20 and 25, so the line 18 the instructions intend is not determined. Witness (evaluated before the fix): head of household, wages $3,000, box 10 $4,000, line 13 $500, expenses $4,500: line 18 $3,000, line 25 $3,000, line 26 and Form 1040 line 1e $1,500, completed. Up to $500 of line 26 can be line 13's, which would raise line 18 and line 25 and lower line 26.
- **Fix:** new gate `f2441.line13_earned` (line 13 above zero, line 20 less than both line 17 and line 21, and line 23 more than line 20, which is line 26 above zero); `f2441.line25` refuses on it, and line 26, line 28 and Form 1040 line 1e follow. Only this case can change an amount: with line 20 equal to line 17, or not less than line 21, more earned income cannot change line 25. The gate reads only lines upstream of line 25, so it adds no cycle. The `person.dc_earned_b` label names the reading and the refusal.
- **Fix lines:** `f2441.line13_earned`, `f2441.line25`, `person.dc_earned_b` (label)
- **Siblings checked:** `f2441.line18`, `f2441.line19`, `f2441.spouse_earned_b`, `f2441.line13`, `person.dc_earned`, `person.dc_1e`, `f2441.attrib_gate` (lines 4 and 5 keep line 1e, as i2441 p. 4 directs).
- **Regression predictions:** written from i2441 p. 5 before the evaluator was run, all met. `f2.t121.line13_earned_refused` (the witness): lines 15 and 17 $4,500, line 18 and line 20 $3,000, line 21 $5,000, line 23 $4,500, gate true, line 25 and line 26 refused. `f2.t121.line13_earned_not_limiting` (wages $45,000, box 10 $5,000, line 13 $500, expenses $6,000): line 17 $5,500, line 20 $5,500, gate false, line 25 $5,000, line 26 and line 1e $500, line 1z $45,500, line 28 $5,000, line 29 $0. `f2.t121.line13_line21_binds` (wages $5,200): line 18 $5,200 below line 17 $5,500 but line 20 not below line 21 $5,000, gate false, line 25 $5,000, line 26 $500.
- **Validation:** fixtures in `fixtures/2025/stage8.json`; witness evaluated before and after. Accepted over-refusal: when line 19 (the spouse) is the limiting line and the line 13 carryover is the taxpayer's, more earned income for line 18 cannot change line 20, but the case is still refused. A second family reading (GPT-6 Astra) was not run; the prompt is in `receipts/t121_astra.prompt.txt`.
- **Tags:** amount-affecting; source-silent; refusal-added; existing-form-pass; fixed

## PENDING-2 — The line 16 questions did not tell the filer to leave out the value of employer-furnished care (T-123)

- **Caught by:** hard1 f2441 L2 (T-092 split, 2026-10-31), T-123.
- **Source:** i2441 p. 5, Line 16, "Enter the total of all qualified expenses incurred in 2025 for the care of your qualifying person(s)"; p. 3, Columns (a) and (b), "If you were covered by your employer's dependent care plan and your employer furnished the care (either at your workplace or by hiring a care provider), enter your employer's name in column (a)"; BUG-0262 (the archived sources do not say whether that value is a qualified expense incurred).
- **Symptom:** with employer-furnished care, `f2441.employer_care_l16` refuses when line 16 is less than line 15, and otherwise line 16 holds the expenses without the value of the employer's care. With line 16 at least line 15 that reading cannot change an amount (line 17 is line 15 under either reading). But nothing told the filer to leave the value out of `f2441.paid_2026` or `dependent.dc_paid`; a filer who entered it could lift line 16 to line 15, escape the refusal and have benefits excluded under the other reading. `dependent.dc_paid` also said "paid by your employer to the provider", which overlaps care the employer furnishes by hiring a provider.
- **Fix:** `f2441.paid_2026` and `dependent.dc_paid` say not to include the value of care your employer furnished itself (at your workplace or through a care provider it hired); `dependent.dc_paid` now says "paid by your employer to a provider you chose", the wording `f2441.employer_care` uses. Proposed register entry (the integrator owns `ambiguities/2025.yaml`): `amb.2025.dc_employer_care_value`, text at issue i2441 p. 5 Line 16 and p. 3 Columns (a) and (b); readings (1) the value of employer-furnished care is not an expense incurred for line 16, (2) it is; chosen (1) when line 16 is at least line 15 (no amount differs) and refused otherwise (`f2441.employer_care_l16`, BUG-0262); link it from `f2441.line16` and `f2441.paid_2026`.
- **Fix lines:** `f2441.paid_2026`, `dependent.dc_paid`
- **Siblings checked:** `f2441.employer_care`, `f2441.employer_care_gate` (line 30 refusal), `f2441.employer_care_l16`, `f2441.line16`, `f2441.line17`, `dcprov.paid`.
- **Regression predictions:** wording only; no value changes. Existing `stage21.t073.employer_care_nothing_paid_refused` and `stage21.t073.employer_care_paid_equals_benefits` still pass (run).
- **Validation:** source and question inspection.
- **Tags:** source-silent; wording; existing-form-pass; fixed (ambiguity entry pending integrator)

## PENDING-3 — `person.ira_excess` omitted "including extensions" from the withdrawal deadline (T-119)

- **Caught by:** fixr4 person L1 (T-092 split), T-119.
- **Source:** p590a p. 35, Tax on Excess Contributions, "In general, if the excess contributions for a year aren’t withdrawn by the date your return for the year is due (including extensions), you are subject to a 6% tax".
- **Symptom:** the screen asked whether the excess "was not withdrawn with its earnings by the due date of your return"; a filer on extension who withdrew in June 2026 could answer Yes and be refused.
- **Fix:** "(including extensions)" added; the p. 35 sentence added to the locator.
- **Fix lines:** `person.ira_excess`
- **Siblings checked:** `person.ira_excess_gate` (already cites the extension rule), `person.x_other`, `ira.special`, `f8889.line14b` (printed form label, not changed).
- **Regression predictions:** wording only; no value changes.
- **Validation:** source inspection; strict citation check passes.
- **Tags:** wording; over-refusal; fixed

## PENDING-4 — `person.itin_applied`'s label lacked the renewal and its help said it counts for the credit for other dependents only (T-120)

- **Caught by:** fixr4 person L2 (T-092 split), T-120.
- **Source:** i1040gi p. 19, Step 5, question 1, "(Answer 'Yes' if you are applying for an ITIN on or before the return due date (including extensions).)"; p970 p. 11, "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as issued on or before the due date of the return."
- **Symptom:** the question asks about an application or a renewal, but the label said only "applied for an ITIN"; the interview help said the answer "counts for the credit for other dependents only", though `person.edu_student` reads it for the American opportunity credit (and the T-113 gate refuses the lifetime learning credit on it).
- **Fix:** the label names the renewal; the help says the answer counts for the credit for other dependents (not the child tax credit, `amb.2025.ctc_spouse_itin_application`) and for this person as an American opportunity credit student, and that the lifetime learning credit is refused.
- **Fix lines:** `person.itin_applied` (label), `interview/questions-2025.yaml` (help)
- **Siblings checked:** `household.tin_count`, `household.id_count`, `person.edu_student`, `person.edu_llc_tin_refused`, `person.tin`.
- **Regression predictions:** wording only.
- **Validation:** inspection.
- **Tags:** wording; presentation; fixed

## PENDING-5 — Church employee income glossed without qualified church-controlled organizations (T-127)

- **Caught by:** screens group4 PENDING-4-11 (T-092 split), T-127.
- **Source:** i1040sse p. 1, Employees of Churches and Church Organizations, "Church employee income is wages you received as an employee (other than as a minister, member of a religious order, or Christian Science practitioner) of a church or qualified church-controlled organization that has a certificate in effect electing an exemption from employer social security and Medicare taxes."
- **Symptom:** `scope.schedule1` and `person.se_screen` said "wages from a church that elected exemption"; an employee of an electing church school or hospital could answer No and complete a return that should be refused.
- **Fix:** both say "a church or qualified church-controlled organization"; the i1040sse sentence is added to both locators.
- **Fix lines:** `scope.schedule1` (label and question), `person.se_screen`
- **Siblings checked:** `f8959.unsupported`/its screen (says "any church employee income", no gloss), `eic.clergy`, `se.yaml` lines 4c and 5a (notes only), `person.yaml` Worksheet B note.
- **Regression predictions:** wording only; no value changes.
- **Validation:** inspection; the `scope.schedule1` screen review is stale and must be rerun (`check_screens.py`).
- **Tags:** wording; under-refusal; fixed

## PENDING-6 — BUG-0320 is fixed: `person.blind` states the partial-blindness test and the certified statement (T-177)

- **Caught by:** BUG-0320, recorded open; this entry closes it because the inventory is append-only. Owner decision 2026-11-02: wording.
- **Source:** i1040gi p. 33, Blindness, "If you weren’t totally blind as of December 31, 2025, you must get a statement certified by your eye doctor (ophthalmologist or optometrist) that:", "You can't see better than 20/200 in your better eye with glasses or contact lenses, or", "Your field of vision is 20 degrees or less.", the not-likely-to-improve alternative and "You must keep the statement for your records."; p. 33, Line 12d, "were blind at the end of 2025".
- **Symptom:** as recorded in BUG-0320.
- **Fix:** the label and question ask whether you were blind at the end of 2025, totally or with the certified statement, and say to keep it; the cite moves from the generic Schedule A locator to i1040gi p. 33.
- **Fix lines:** `person.blind`
- **Siblings checked:** `sa.boxes_blind`, `sa.extra_blind`, `sa.spouse_extra` (refused), `refund.you_blind` (2024 worksheet question, form `refund`, not owned: it asks "Were you blind at the end of 2024?" without the definition; recorded, not changed).
- **Regression predictions:** wording only.
- **Validation:** inspection. `check_consumers.py` now reports `person.blind@i1040gi:p34` and `p35` (read by `sa.boxes_blind`) as changed and `p33` as stale: proposed verdicts in `consumers_proposed.json`.
- **Tags:** source-definition-debt; standard-deduction; wording; fixed

## PENDING-7 — BUG-0338 is fixed: the care-expense question states household services, housekeeper meals and lodging, provider transportation, agency fees and the volunteer-work rule (T-184)

- **Caught by:** BUG-0338, recorded open; this entry closes it because the inventory is append-only.
- **Source:** i2441 p. 1, "These include amounts paid for household services and care of the qualifying person while you worked or looked for work."; p. 2, Household services, the cook/maid/babysitter/housekeeper/cleaning person sentence and "they don't include the services of a chauffeur, bartender, or gardener"; p503 p. 6, Volunteer work; p503 p. 7, Transportation and Fees and deposits; p503 p. 8, Meals and lodging provided for housekeeper.
- **Symptom:** as recorded in BUG-0338.
- **Fix:** `dependent.dc_paid` states the household-services rule with its examples and exclusions, the housekeeper's meals and extra lodging (excepted from the food-and-lodging exclusion), the care provider's transportation (not other transportation or the provider's travel to your home), agency fees, deposits and application fees (not a forfeited deposit), and that unpaid volunteer work or work for a nominal salary is not work.
- **Fix lines:** `dependent.dc_paid`
- **Siblings checked:** `dependent.dc_line2d`, `f2441.paid_2026`, `f2441.line16`, `dcprov.paid`, `dcprov.household`; the limits baseline entries for `dependent.dc_paid` (`limit:p503:p6:463a57ef`, `limit:p503:p6:ea477d7e`) still hold (`check_limits.py` 0 new).
- **Regression predictions:** wording only; no value changes.
- **Validation:** inspection; strict citation check passes.
- **Tags:** source-definition-debt; dependent; wording; fixed

## PENDING-8 — BUG-0339 is fixed: the support question states the five residual rules (T-185)

- **Caught by:** BUG-0339, recorded open; this entry closes it because the inventory is append-only.
- **Source:** p501 p. 20, Lodging, "Fair rental value includes a reasonable allowance for the use of furniture and appliances, and for heat and other utilities that are provided."; p. 21, "If you don’t provide the total lodging, the total fair rental value must be divided depending on how much of the total lodging you provide."; p. 20, "However, payments based on the needs of the recipient won’t be considered as used entirely for that person’s support if it is shown that part of the payments weren’t used for that purpose."; p. 20, Social security benefits, the one-check sentence; p. 22, Alimony, "Payments to a spouse that are alimony or separate maintenance payments, or similar payments from an estate or trust, aren’t treated as a payment for the support of a dependent."
- **Symptom:** as recorded in BUG-0339.
- **Fix:** `dependent.supported` states all five rules.
- **Fix lines:** `dependent.supported`
- **Siblings checked:** `dependent.self_support` (the qualifying-child test; it already counts the person's own home and state support; the one-check and alimony rules bear on the qualifying-relative support split, so it is unchanged), `dependent.multiple_support`, `dependent.divorced_rule`.
- **Regression predictions:** wording only.
- **Validation:** inspection; strict citation check passes.
- **Tags:** source-definition-debt; dependent; wording; fixed

## PENDING-9 — An earlier credit disallowance refuses the whole return when no credit is claimed (T-101, `household.credit_disallowed`) — fix proposed as a patch, not applied

- **Caught by:** T-101 (coverage tree build, 2026-10-31); premise checked in the person-dep pass.
- **Source:** i1040s8812 p. 2, "you must attach Form 8862 to your tax return to claim the CTC, ACTC, or ODC unless an exception applies"; i1040gi p. 43, "You must file Form 8862 if your EIC for a year after 1996 was reduced or disallowed for any reason other than a math or clerical error".
- **Symptom:** `s8812.line12` and the EIC credit line refuse on `household.credit_disallowed` alone. Witness (evaluated): `stage5.return.owed` (single, no dependents, EIC Steps not passed) with the answer Yes refuses Form 1040 lines 19, 24, 27a and 37; with the gate narrowed it completes with line 24 $18,500, line 27a $0, line 37 $1,500, the values it records with the answer No.
- **Fix (proposed):** gates `household.ctc_disallowed_claim` (the answer Yes and Schedule 8812 line 8 more than line 11, that is line 12 above zero, read without line 12 to avoid a cycle) and `household.eic_disallowed_claim` (the answer Yes and `eic.eligible`), used by the existing refusals in `s8812.yaml` and `eic.yaml`. The refusal sites are in forms this package does not own, so the change is `t101_credit_disallowed.patch` (household, s8812, eic, `tools/coverage/tree.json`, two audit fixtures and one new regression); apply after `coverage_tree_line13.patch`.
- **Fix lines:** `household.ctc_disallowed_claim`, `household.eic_disallowed_claim`, `s8812.line12`, `eic.credit` (proposed)
- **Siblings checked:** `household.credit_disallowed` (input, unchanged), `f8863.ban_refused` (the education-credit ban, a separate input), `s8812.line8`, `s8812.line11`, `eic.eligible`.
- **Regression predictions:** `f2.t101.credit_disallowed_no_credit_claimed` completes with stage5.return.owed's 45 values; `audit.s8812.credit_disallowed` keeps its Schedule 8812 refusals under the new gate id and its line 27a becomes $0 (EIC not eligible there); `audit.eic.credit_disallowed` keeps its refusals under the new ids. Tested in a scratch copy of this worktree with the patch applied: 1,443/1,445 before the two audit fixtures were updated (only those two, gate ids and the line 27a narrowing), all three pass after.
- **Validation:** scratch-copy evaluation; `tree.py --check` accepts the placements (only the generated outputs are then out of date). Not run with the patch: the other per-check scripts.
- **Accepted over-refusal that remains:** the question pools the EIC and the child tax credits, so a filer whose only disallowance was the EIC is still refused on Schedule 8812 when claiming the child tax credit (and the reverse).
- **Tags:** over-refusal; whole-return-screen; T-101; proposed
