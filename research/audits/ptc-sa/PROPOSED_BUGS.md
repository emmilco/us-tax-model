# Proposed bug entries, package ptc-sa (2026-11-03)

Entries in BUG_INVENTORY.md format. Ids are placeholders; the integrator assigns numbers.

## PENDING-1 — A covered month with zero in column (b) completed with the month's credit lost (owner decision C1)

- **Caught by:** the C-backlog reproduction of BUG-0298 (T-165), carried to T-180 by owner decision C1, 2026-11-02.
- **Source:** p974 p. 6, "To qualify for a monthly credit amount, at least one individual in your tax family must be enrolled in a qualified health plan on the first day of that month.", "The applicable SLCSP premium is the second lowest cost silver plan premium offered through the Marketplace where you reside that applies to your coverage family", "may report your applicable SLCSP premium as -0-", "In either case, you must determine your correct applicable SLCSP premium."; i8962 p. 16, Column (b), "Enter on lines 12 through 23, column (b), the amount of the monthly applicable SLCSP premium reported on Form 1095-A, lines 21 through 32, column B, for the corresponding month"; i8962 p. 17, "credit amount because your enrollment premiums for the month were unpaid, enter -0- on the appropriate line on Form 8962, column (b)".
- **Symptom:** a month with enrollment premiums in column (a) and zero in column (b) completed with no credit for that month. C-backlog witness: one Form 1095-A, January to June, column A $500, B $450, C $300; March column B entered as 0 gave line 24 $1,485 against $1,782. Pub. 974 (archived) was searched for a legitimate covered month with column A above zero and column B zero. The only one in Pub. 974 and i8962 is a month whose premiums were unpaid (i8962 p. 17), and `f8962.other` already refuses it. Every other case where column B is zero is refused by its own gate: other coverage (an empty coverage family), allocation, the year of marriage, QSEHRA, and a person who is not lawfully present. The other zero is the "-0-" that a Marketplace reports when no APTC was paid, and the filer must replace it with the correct premium.
- **Fix:** new helper `f8962.b_zero`: an applicable taxpayer (`f8962.show_applicable`) with any month of lines 12 to 23 where column (a) is above 0 and column (b) is 0. The uniform route is covered because its monthly lines carry `mo_a`/`mo_b`. The helper is folded into the existing computed gate `f8962.two_counted` (any of the old test or `b_zero`), so the coverage tree's gate placement does not change. The gate's label, the line 24/25 refusal remedy and the refusal cite name the zero column (b) case, and the form note lists it.
- **Fix lines:** `f8962.b_zero`, `f8962.two_counted`, `f8962.line24`, `f8962.line25`
- **Siblings checked:** `f8962.same_state_counted`, `f1095a.b_counted`, `f1095a.b_used`, `f1095a.b_jan` to `f1095a.b_dec`, `f1095a.in_b_jan` to `f1095a.in_b_dec`, `f1095a.mo_b`, `f8962.line11a`, `f8962.line11b`, `f8962.line12a` to `f8962.line23b`, `f8962.other`; also generated, covered by the rerun reviews of their forms: `f1095a.a_jan` to `f1095a.a_dec`, `f1095a.in_a_jan` to `f1095a.in_a_dec`, `f1095a.mo_a`, `f1095a.c_total`, `f8962.aptc_total`
- **Regression predictions:** written before evaluation. `stage18.refuse.b_zero_monthly` (the `stage18.blind.p10` inputs with March column B 0) refuses at `f8962.line24` and `f8962.line25` with gate `f8962.two_counted`. `stage18.refuse.b_zero_uniform` (the `stage18.blind.p1` inputs with `mo_b` 0, line 11 route) refuses the same way. Both matched, and `s3.line9` also refuses. `stage18.refuse.two_counted_same_state` keeps its gate and lines. Only its recorded remedy and cite text were updated to the new wording. No other fixture changed. Fixtures 1,444/1,444.
- **Validation:** source inspection of Pub. 974 and i8962. A GPT-6 Astra second reading (receipts/c1_astra_*.txt) found no legitimate case described. It noted that the text does not prove no such case exists. Any case it missed would be refused, not miscomputed.
- **Tags:** premium-tax-credit; amount-affecting; refusal; fixed

## PENDING-2 — BUG-0321 is settled: Schedule A line 1 takes Marketplace premiums less the credit allowed, not less the advance payments

- **Caught by:** T-180 (BUG-0321's open question on a net premium tax credit), reading Pub. 502.
- **Source:** p502 p. 12, Premium Tax Credit, "You can’t include in medical expenses the amount of health insurance premiums paid by or through the premium tax credit", "You also can’t include in medical expenses any amount of advance payments of the premium tax credit made that you did not have to pay back", "However, any amount of advance payments of the premium tax credit that you did have to pay back can be included in medical expenses", Example 1, "You are treated as paying $5,100 ($8,700 less the allowed premium tax credit of $3,600)"; i8962 p. 2, "You cannot deduct the portion of your health insurance premium on your tax return that is paid for by the PTC or APTC (after you determine how much of any excess APTC you must repay)"; i1040sca p. 2, "fill out Form 8962 before filling out Schedule A, line 1".
- **Symptom:** the BUG-0321 wording told the filer to "leave out premiums paid by advance payments of the premium tax credit". That is right only when the credit allowed equals the advance payments. On Pub. 502's own examples it gave $4,500 where the rule gives $5,100 when excess advance payments are repaid (Example 1), and $4,500 where the rule gives $3,800 when a net credit is claimed (Example 2). Line 1 is a supplied amount, so the error passes into line 4 whenever medical expenses exceed 7.5% of AGI. Not reproduced by evaluation, because the defect is in the wording.
- **Fix:** wording only (owner decision 2026-11-02: not a computed split). For Marketplace coverage, `sa.line1` now takes the total premiums (including the part paid by advance payments), minus the credit allowed on Form 8962 line 24, minus any excess advance payments not repaid because of the repayment limit (line 27 minus line 29). Advance payments that are repaid count as premiums paid. Checked against both Pub. 502 examples (8,700 − 3,600 − 0 = 5,100; 8,700 − 4,900 = 3,800) and against a capped-repayment case. The self-employed health insurance with premium tax credit case stays refused by `sc.hi_screen` (Pub. 974 iterative method).
- **Fix lines:** `sa.line1`
- **Siblings checked:** `sa.line4`, `sa.agi_floor`, `f8962.line24`, `f8962.line27`, `f8962.line29`, `s1.line17`, `sc.hi_screen`
- **Regression predictions:** wording only. No expression changed and no fixture value moves.
- **Validation:** source inspection; arithmetic on the two Pub. 502 examples.
- **Tags:** source-definition-debt; wording; schedule-a; premium-tax-credit; cross-form; fixed

## PENDING-3 — BUG-0327 is closed: three of its four parts were already refused; the corrected-SLCSP situations are stated

- **Caught by:** BUG-0327, recorded open (T-180). This entry closes it because the inventory is append-only.
- **Source:** i8962 p. 14, "If the correct applicable SLCSP premium is not the same for every month of 2025, check “No”"; p. 15, "Examples of changes in circumstances that may affect your applicable SLCSP premium include the following", "You moved during 2025", "If any of the above apply and you did not notify the Marketplace or if you have reason to believe the Marketplace reported the wrong applicable SLCSP premium, determine the correct applicable SLCSP premium for the months affected".
- **Symptom (premise check):** The `f8962.other` question already asks whether "someone enrolled in a Marketplace policy was not lawfully present" and whether "any part of a month's premium was not paid by the due date of your return", and it refuses both. So the not-lawfully-present part, the unpaid-share part and the partial-payment part of BUG-0327 are refused, not missed. A partial payment that kept coverage in force is refused, an over-refusal already accepted in the `f8962.other` ruling. What remained was the list of situations that make column B wrong. The questions said only "blank, wrong, or zero".
- **Fix:** wording only. The `f1095a.uniform` question now says to answer no if the correct column B is not the same every month. It lists the i8962 p. 15 changes in circumstances, and the no-APTC case, that make column B wrong for the months affected. The twelve `f1095a.in_b_<month>` questions and `f1095a.mo_b` add "for example after a move or a change in your tax or coverage family that you did not report to the Marketplace". The shared cites (`f1095a.months`/`f1095a.uniform`; the column B lines) add the p. 14 and p. 15 sentences. PENDING-1 catches a zero that remains.
- **Fix lines:** `f1095a.uniform`, `f1095a.in_b_jan` through `f1095a.in_b_dec`, `f1095a.mo_b`
- **Siblings checked:** `f1095a.months`, `f1095a.b_jan` to `f1095a.b_dec` (share the column B cite), `f1095a.b_counted`, `f8962.line10`, `f8962.nonuniform`, `f8962.show_annual`, `f8962.other`; also generated, covered by the rerun reviews of their forms: `f1095a.line33a`, `f1095a.line33b`, `f1095a.line33c`, `f1095a.yr_b_monthly`, `f1095a.yr_b_uniform`
- **Regression predictions:** wording only. No expression changed and fixtures pass unchanged.
- **Validation:** source and implementation inspection.
- **Tags:** source-definition-debt; wording; premium-tax-credit; fixed

## PENDING-4 — BUG-0326, Schedule A part: whose medical expenses count and the line 5a to 5c rules are stated

- **Caught by:** BUG-0326 (the sa completeness claims sa#1 to sa#4), recorded open (T-183). This entry closes its Schedule A part. The sc, scveh and asset parts stay open.
- **Source:** i1040sca p. 2, "You can include medical and dental bills you paid in 2025 for anyone who was one of the following either when the services were provided or when you paid for them", "Your child whom you don't claim as a dependent because of the rules for children of divorced or separated parents", "Any person you could have claimed as a dependent on your return except that person received $5,200 or more of gross income or filed a joint return", "You can't deduct any premiums attributable to this individual unless", "However, if you had family coverage when you added this individual to your policy and your premiums didn't increase", "If you received a reimbursement in 2025 for prior year medical or dental expenses, don't reduce your 2025 expenses by this amount", "(cafeteria plan) unless the premiums are included in box 1 of your Form(s) W-2"; p. 3, Line 5a (withholding deducted elsewhere, estimated payments, "Don't include penalties or interest.", the mandatory disability, unemployment and family leave fund contributions, refunds not reducing, the state-tax-credit safe harbor); p. 6, Line 5b (business use, uniform general-purpose levies, foreign taxes, service charges, improvement assessments and the maintenance exception, escrow, tax charged to the buyer, refunds and rebates); p. 6, Line 5c ("based on value alone and were imposed on a yearly basis", the car-fee example); p. 7, "Only taxes paid in 2025 and assessed prior to 2026 can be deducted for 2025".
- **Symptom:** as recorded in BUG-0326 for Schedule A.
- **Fix:** wording only.
  - `sa.line1` names whose expenses count and leaves out premiums for a nondependent on the policy (except with family coverage whose premiums did not increase). It also leaves out amounts paid by a cafeteria plan unless included in W-2 box 1, and says a 2025 reimbursement of an earlier year's expenses does not reduce 2025 expenses.
  - `sa.line5a` states the payments that count, excludes penalties and interest, and includes the mandatory fund contributions. It says refunds do not reduce the amount, and it states the state-tax-credit safe harbor.
  - `sa.line5b` states the business-use, uniform-levy and general-purpose tests. It also states the foreign tax, service charge and improvement exclusions (and the maintenance exception), the escrow rule, tax charged to the buyer, and the refund rules.
  - `sa.line5c` states the value-only yearly test, the car-fee example and the paid/assessed rule.
  - The person who can be claimed by someone else (the third i1040sca list item) is not stated, because `sa.dependent` refuses the whole return.
- **Fix lines:** `sa.line1`, `sa.line5a`, `sa.line5b`, `sa.line5c`
- **Siblings checked:** `sa.line4`, `sa.line5d`, `sa.agi_floor`, `sa.dependent`, `sa.unsupported` (sales-tax election and foreign taxes), `sa.line11` (charitable gifts reduced by a state tax credit), `ltc.payments`
- **Regression predictions:** wording only. No expression changed and no fixture value moves.
- **Validation:** source inspection; every added quote is checked by `citations.py --strict`.
- **Tags:** source-definition-debt; wording; schedule-a; fixed

## PENDING-5 — BUG-0308 is fixed: the long-term care question states who may be covered

- **Caught by:** BUG-0308, recorded open (T-171). This entry closes it.
- **Source:** i7206 p. 1, "You may be able to deduct the amount you paid for health insurance, which includes medical, dental, and vision insurance and qualified long-term care insurance for yourself, your spouse, and your dependents.", "The health insurance can cover your child who was under age 27 at the end of 2025, even if the child wasn’t your dependent.", "A child includes your son, daughter, stepchild, adopted child, or foster child."
- **Symptom:** as recorded in BUG-0308.
- **Fix:** wording only. `ltc.payments` says the person must be the filer, the spouse, a dependent, or a child (son, daughter, stepchild, adopted or foster child) under age 27 at the end of 2025, and to enter zero for anyone else. The cite adds the three i7206 p. 1 sentences. The health insurance questions `sc.hi_uses` and `sc.f7206_line1` already name the same people.
- **Fix lines:** `ltc.payments`
- **Siblings checked:** `ltc.amount`, `ltc.limit`, `sc.hi_uses`, `sc.f7206_line1`, `sc.hi_screen` (the retired public safety officer and multiple-business ltc claims are refused there)
- **Regression predictions:** wording only. No expression changed.
- **Validation:** source inspection.
- **Tags:** source-definition-debt; wording; fixed

## PENDING-6 — BUG-0314, premise check: most Form 5329 Part I items are already refused; two remain, in a form this package does not own (open)

- **Caught by:** the T-175 premise check, 2026-11-03.
- **Source:** i5329 p. 1 and p. 3, Line 1; p. 5, Line 2 (the exception conditions); p590b p. 28, "If you received a distribution to buy, build, or rebuild a first home and the purchase or construction was canceled or delayed".
- **Symptom (premise check, inspected in `forms/2025/retirement.yaml`):**
  - Already refused:
    - a Roth IRA distribution other than code Q, so any Form 8606 line 25c or recapture amount (`retirement.bad_code`);
    - a modified series of substantially equal periodic payments (`retirement.early_screen`);
    - a returned 2024 or 2025 IRA contribution, with its earnings (`retirement.special`).
  - Already computed: the rolled-over part is taken out of the taxable amount (`retirement.rolled`, `retirement.l1`).
  - Open:
    - the recontribution within 120 days of a first-home distribution whose purchase was canceled or delayed;
    - the exception conditions. `retirement.exception` names the exceptions but does not state their conditions, for example separation from service in or after the year the person reached 55 (plans only), the disability proof, and the series that must begin after separation from an employer plan.
- **Disposition:** needs `retirement.rollover` and `retirement.exception` (form `retirement`), outside this package's forms. Proposed wording is in REPORT.md (T-175). `f5329` lines only copy `person.x_*`, which sum `retirement.*`.
- **Validation:** implementation inspection.
- **Tags:** source-definition-debt; explicitly-deferred
