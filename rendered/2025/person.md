# Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)

- Document: `person` (worksheet, tax year 2025)
- Collection: keyed entries; [f1040] Form 1040 (2025), page 1, "Your first name and middle initial" and "If joint return, spouse’s first name and middle initial" (2025; created 2025-09-05; sha256 3d31c226)
- Note: Helper worksheet. Wages means boxes 3 plus 7 under approved interpretation amb.2025.ss_wages. Independent lines may compute while credit and dependent totals are refused.

## (helper) — `person.role`

- **Authored helper label:** Whose entry is this, yours or your spouse's?
- **Encoded (Enum(person_role)):** Input — Whose entry is this, yours (the taxpayer) or your spouse's?
- Expr: `{"op":"input","source":"Whose entry is this, yours (the taxpayer) or your spouse's?"}`
- Cite: [f1040] Form 1040 (2025), page 1, "Your first name and middle initial" and "If joint return, spouse’s first name and middle initial" (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `person.one`

- **Authored helper label:** One entry for this person
- **Encoded (Count):** Enter 1 (person.one).
- Expr: `{"op":"param","ref":"person.one"}`
- Cite: [f1040] Form 1040 (2025), page 1, one entry for you and, if joint return, one for your spouse (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `person.age65`

- **Authored helper label:** Were you born before January 2, 1961?
- **Encoded (Bool):** Input — Were you born before January 2, 1961?
- Expr: `{"op":"input","source":"Were you born before January 2, 1961?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `person.blind`

- **Authored helper label:** Are you blind under the standard-deduction instructions?
- **Encoded (Bool):** Input — Are you blind under the standard-deduction instructions?
- Expr: `{"op":"input","source":"Are you blind under the standard-deduction instructions?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `person.tin`

- **Authored helper label:** Do you have an SSN or ITIN issued on or before the due date of your return?
- **Encoded (Bool):** Input — Do you have an SSN or ITIN issued on or before the due date of your 2025 return (including extensions)?
- Expr: `{"op":"input","source":"Do you have an SSN or ITIN issued on or before the due date of your 2025 return (including extensions)?"}`
- Cite: [i1040gi] p. 17, Before you begin, "The other spouse must have either an SSN or ITIN, and it must have been issued on or before the due date of the return (including extensions)"; p. 19, Step 5, question 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.itin_applied`

- **Authored helper label:** If not, have you applied for an ITIN on or before the due date of your return?
- **Encoded (Bool):** Input — If you have neither, have you applied for an ITIN on or before the due date of your 2025 return (including extensions)?
- Expr: `{"op":"input","source":"If you have neither, have you applied for an ITIN on or before the due date of your 2025 return (including extensions)?"}`
- Cite: [i1040gi] p. 19, Step 5, question 1, "(Answer 'Yes' if you are applying for an ITIN on or before the return due date (including extensions).)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.work_ssn`

- **Authored helper label:** Do you have an SSN valid for employment issued before the due date of your return?
- **Encoded (Bool):** Input — Do you have an SSN valid for employment, issued before the due date of your 2025 return (including extensions)?
- Expr: `{"op":"input","source":"Do you have an SSN valid for employment, issued before the due date of your 2025 return (including extensions)?"}`
- Cite: [i1040gi] p. 18, Step 3, question 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.eic_ssn`

- **Authored helper label:** Do you have an SSN valid for the EIC, issued on or before the due date of your return?
- **Encoded (Bool):** Input — Do you have a social security number issued on or before the due date of your 2025 return (including extensions) that is valid for the EIC? Any number issued by the Social Security Administration is valid unless the card says "Not Valid for Employment" and the number was issued solely to apply for or receive a federally funded benefit; a card that says "Valid for Work Only With DHS Authorization" is valid only while the authorization is valid.
- Expr: `{"op":"input","source":"Do you have a social security number issued on or before the due date of your 2025 return (including extensions) that is valid for the EIC? Any number issued by the Social Security Administration is valid unless the card says \"Not Valid for Employment\" and the number was issued solely to apply for or receive a federally funded benefit; a card that says \"Valid for Work Only With DHS Authorization\" is valid only while the authorization is valid."}`
- Cite: [i1040gi] p. 40, Step 1, question 2; pp. 44–45, Social security number (SSN), "For the EIC, a valid SSN is a number issued by the Social Security Administration unless “Not Valid for Employment” is printed on the social security card and the number was issued solely to allow the recipient of the SSN to apply for or receive a federally funded benefit" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.under16`

- **Authored helper label:** Were you under age 16 at the end of 2025?
- **Encoded (Bool):** Input — Were you under age 16 at the end of 2025?
- Interpretation: amb.2025.filer_under_16
- Expr: `{"op":"input","source":"Were you under age 16 at the end of 2025?"}`
- Cite: [i1040gi] p. 66, Self-Select PIN, "You can’t use the Self-Select PIN method if you are a first-time filer under age 16 at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.educator_expenses`

- **Authored helper label:** Qualified educator expenses you paid in 2025
- **Encoded (NonNegDollars):** Input — Qualified educator expenses you paid in 2025 (professional development courses, and books, supplies, equipment and other materials used in the classroom), reduced by excludable savings bond interest (Form 8815), nontaxable qualified tuition program or Coverdell earnings or distributions, and reimbursements not reported in box 1 of your Form W-2; zero if none
- Expr: `{"op":"input","source":"Qualified educator expenses you paid in 2025 (professional development courses, and books, supplies, equipment and other materials used in the classroom), reduced by excludable savings bond interest (Form 8815), nontaxable qualified tuition program or Coverdell earnings or distributions, and reimbursements not reported in box 1 of your Form W-2; zero if none"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 11, Qualified expenses and 'You must reduce your qualified expenses by the following amounts' (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.eligible_educator`

- **Authored helper label:** Were you an eligible educator in 2025 (a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who worked in a school for at least 900 hours during a school year)?
- **Encoded (Bool):** Input — Were you an eligible educator in 2025 (a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who worked in a school for at least 900 hours during a school year)?
- Expr: `{"op":"input","source":"Were you an eligible educator in 2025 (a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who worked in a school for at least 900 hours during a school year)?"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 11, 'An eligible educator is a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who worked in a school for at least 900 hours during a school year' (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.born_before_2001`

- **Authored helper label:** Were you born before January 2, 2001?
- **Encoded (Bool):** Input — Were you born before January 2, 2001?
- Expr: `{"op":"input","source":"Were you born before January 2, 2001?"}`
- Cite: [i1040gi] p. 41, Step 4, question 2, "Check 'Yes' if you ... were born after December 31, 1960, and before January 2, 2001" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.born_after_1960`

- **Authored helper label:** Were you born after December 31, 1960?
- **Encoded (Bool):** Input — Were you born after December 31, 1960?
- Expr: `{"op":"input","source":"Were you born after December 31, 1960?"}`
- Cite: [i1040gi] p. 41, Step 4, question 2, "Check 'Yes' if you ... were born after December 31, 1960, and before January 2, 2001" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.died_before_65`

- **Authored helper label:** Is this the final return of a person born between January 2, 1960, and January 1, 1961, who died in 2025 before reaching age 65?
- **Encoded (Bool):** Input — Is this the final return of a person born between January 2, 1960, and January 1, 1961, who died in 2025 before reaching age 65? (A person reaches age 65 on the day before the 65th birthday.)
- Expr: `{"op":"input","source":"Is this the final return of a person born between January 2, 1960, and January 1, 1961, who died in 2025 before reaching age 65? (A person reaches age 65 on the day before the 65th birthday.)"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Death of a taxpayer in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.educator_max`

- **Authored helper label:** Year parameter s1.educator_max ($300)
- **Encoded (NonNegDollars):** Enter $300 (s1.educator_max).
- Expr: `{"op":"param","ref":"s1.educator_max"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 11, "If you and your spouse are filing jointly and both of you were eligible educators, the maximum deduction is $600. However, neither spouse can deduct more than $300 of their qualified expenses" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.has_educator_expenses`

- **Authored helper label:** Any qualified educator expenses for this person
- **Encoded (Bool):** helper "Qualified educator expenses you paid in 2025" > $0 (sales.zero)
- Expr: `{"gt":["person.educator_expenses",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 11 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.educator_limited`

- **Authored helper label:** This person's qualified educator expenses, up to $300
- **Encoded (NonNegDollars):** Enter the smaller of helper "Qualified educator expenses you paid in 2025" or helper "Year parameter s1.educator_max ($300)".
- Expr: `{"of":["person.educator_expenses","person.educator_max"],"op":"smaller_of"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 11, "If you and your spouse are filing jointly and both of you were eligible educators, the maximum deduction is $600. However, neither spouse can deduct more than $300 of their qualified expenses" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.educator_eligible_amount`

- **Authored helper label:** This person's qualified educator expenses up to $300 if an eligible educator, else zero
- **Encoded (NonNegDollars):** Choose — [helper "Were you an eligible educator in 2025 (a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who worked in a school for at least 900 hours during a school year)?" = true → helper "This person's qualified educator expenses, up to $300"] [helper "Were you an eligible educator in 2025 (a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who worked in a school for at least 900 hours during a school year)?" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.eligible_educator",{"const":true}],"op":"test"},"then":"person.educator_limited"},{"guard":{"eq":["person.eligible_educator",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 11, "If you were an eligible educator in 2025, you can deduct on line 11 up to $300 of qualified expenses you paid in 2025"; "If you and your spouse are filing jointly and both of you were eligible educators, the maximum deduction is $600. However, neither spouse can deduct more than $300 of their qualified expenses" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.educator_deduction`

- **Authored helper label:** This person's educator expense deduction
- **Encoded (NonNegDollars):** Choose — [helper "Any qualified educator expenses for this person" = true → helper "This person's qualified educator expenses up to $300 if an eligible educator, else zero"] [helper "Any qualified educator expenses for this person" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_educator_expenses",{"const":true}],"op":"test"},"then":"person.educator_eligible_amount"},{"guard":{"eq":["person.has_educator_expenses",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 11, "If you were an eligible educator in 2025, you can deduct on line 11 up to $300 of qualified expenses you paid in 2025"; "If you and your spouse are filing jointly and both of you were eligible educators, the maximum deduction is $600. However, neither spouse can deduct more than $300 of their qualified expenses" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.hsa_forms`

- **Authored helper label:** Number of Forms 8889 entered for this person
- **Encoded (Count):** Add f8889.one over every confirmed f8889 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8889","field":"f8889.one","op":"sum_over"}`
- Cite: [i8889] p. 4, Name and social security number (SSN), "complete a separate Form 8889 for each of you" (2025; sha256 da6f2f58)

## (gate) — `person.hsa_repeated`

- **Authored helper label:** More than one Form 8889 entered for this person
- **Encoded (Bool):** helper "Number of Forms 8889 entered for this person" > 1 (a count)
- Expr: `{"gt":["person.hsa_forms",{"const":1,"type":"Count"}],"op":"test"}`
- Cite: [i8889] p. 4, Name and social security number (SSN), "complete a separate Form 8889 for each of you" (2025; sha256 da6f2f58)

## (helper) — `person.hsa_split`

- **Authored helper label:** This persons Form 8889 uses the spouse rule of line 6
- **Encoded (Count):** Add f8889.one over every confirmed f8889 entry for which helper "Spouses with separate HSAs, treated as having family coverage at any time during 2025" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8889","field":"f8889.one","op":"sum_over","where":{"eq":["f8889.split",{"const":true}],"op":"test"}}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, Steps 1 to 3, "Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, use the following rules to figure the amount on line 6", "Step 1. Refigure the contribution limit that would have been entered on line 5 if you had entered on line 3 the total of the worksheet amounts only for the months you were treated as having family coverage", "Step 2. Divide the refigured contribution limit from Step 1 equally between you and your spouse, unless you both agree on a different allocation (such as allocating nothing to one spouse)", "Step 3. Subtract the part of the contribution limit allocated to your spouse in Step 2 from the amount determined in Step 1" (2025; sha256 da6f2f58)

## (helper) — `person.hsa_agreed`

- **Authored helper label:** This persons Form 8889 uses an agreed allocation under the spouse rule of line 6
- **Encoded (Count):** Add f8889.one over every confirmed f8889 entry for which helper "Spouses with separate HSAs, treated as having family coverage at any time during 2025" = true and helper "Do you and your spouse divide the family contribution limit equally, or by a different allocation you both agree on?" = 'agreed', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8889","field":"f8889.one","op":"sum_over","where":{"all":[{"eq":["f8889.split",{"const":true}],"op":"test"},{"eq":["f8889.allocation",{"const":"agreed"}],"op":"test"}],"op":"test"}}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, Steps 1 to 3, "Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, use the following rules to figure the amount on line 6", "Step 1. Refigure the contribution limit that would have been entered on line 5 if you had entered on line 3 the total of the worksheet amounts only for the months you were treated as having family coverage", "Step 2. Divide the refigured contribution limit from Step 1 equally between you and your spouse, unless you both agree on a different allocation (such as allocating nothing to one spouse)", "Step 3. Subtract the part of the contribution limit allocated to your spouse in Step 2 from the amount determined in Step 1" (2025; sha256 da6f2f58)

## (helper) — `person.hsa_step1`

- **Authored helper label:** This persons Step 1 limit under the spouse rule of line 6
- **Encoded (NonNegDollars):** Add f8889.step1 over every confirmed f8889 entry for which helper "Spouses with separate HSAs, treated as having family coverage at any time during 2025" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8889","field":"f8889.step1","op":"sum_over","where":{"eq":["f8889.split",{"const":true}],"op":"test"}}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, Steps 1 to 3, "Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, use the following rules to figure the amount on line 6", "Step 1. Refigure the contribution limit that would have been entered on line 5 if you had entered on line 3 the total of the worksheet amounts only for the months you were treated as having family coverage", "Step 2. Divide the refigured contribution limit from Step 1 equally between you and your spouse, unless you both agree on a different allocation (such as allocating nothing to one spouse)", "Step 3. Subtract the part of the contribution limit allocated to your spouse in Step 2 from the amount determined in Step 1" (2025; sha256 da6f2f58)

## (helper) — `person.hsa_share`

- **Authored helper label:** This persons part of the Step 1 limit under the spouse rule of line 6
- **Encoded (NonNegDollars):** Add f8889.share_raw over every confirmed f8889 entry for which helper "Spouses with separate HSAs, treated as having family coverage at any time during 2025" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8889","field":"f8889.share_raw","op":"sum_over","where":{"eq":["f8889.split",{"const":true}],"op":"test"}}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, Steps 1 to 3, "Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, use the following rules to figure the amount on line 6", "Step 1. Refigure the contribution limit that would have been entered on line 5 if you had entered on line 3 the total of the worksheet amounts only for the months you were treated as having family coverage", "Step 2. Divide the refigured contribution limit from Step 1 equally between you and your spouse, unless you both agree on a different allocation (such as allocating nothing to one spouse)", "Step 3. Subtract the part of the contribution limit allocated to your spouse in Step 2 from the amount determined in Step 1" (2025; sha256 da6f2f58)

## (helper) — `person.hsa_deduction`

- **Authored helper label:** Form 8889 line 13 for this person
- **Encoded (NonNegDollars):** Add f8889.line13 over every confirmed f8889 entry, within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when person.hsa_repeated is true, cannot complete More than one Form 8889 for one person. Enter one Form 8889 per person, combining all of that person's own HSAs on it. A separate Form 8889 for each HSA (with a controlling Form 8889) is required only for an inherited HSA, which is outside this tool. Cite: [i8889] p. 3, "If, during the tax year, you are the beneficiary of two or more HSAs or you are a beneficiary of an HSA and you have your own HSA, you must complete a separate Form 8889 for each HSA" (2025; sha256 da6f2f58)
- Expr: `{"collection":"f8889","field":"f8889.line13","op":"sum_over"}`
- Cite: [i8889] p. 4, "Combine the amounts on line 13 of both Forms 8889 and enter this amount on Schedule 1 (Form 1040), line 13" (2025; sha256 da6f2f58)

## (helper) — `person.hsa_taxable`

- **Authored helper label:** Form 8889 line 16 for this person
- **Encoded (NonNegDollars):** Add f8889.line16 over every confirmed f8889 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8889","field":"f8889.line16","op":"sum_over"}`
- Cite: [f8889] p. 1, Part II, "HSA Distributions. If you are filing jointly and both you and your spouse each have separate HSAs, complete a separate Part II for each spouse", line 16, "Taxable HSA distributions. Subtract line 15 from line 14c. If zero or less, enter -0-" (2025; created 2025-03-28; sha256 15ed4587)

## (helper) — `person.hsa_addtax`

- **Authored helper label:** Form 8889 line 17b for this person
- **Encoded (NonNegDollars):** Add f8889.line17b over every confirmed f8889 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8889","field":"f8889.line17b","op":"sum_over"}`
- Cite: [f8889] Form 8889 (2025), line 17b, "Also, include this amount in the total on Schedule 2 (Form 1040), Part II, line 17c" (2025; created 2025-03-28; sha256 15ed4587)

## (helper) — `person.tip_employers`

- **Authored helper label:** Number of employers that paid this person qualified tips
- **Encoded (Count):** Add tipjob.one over every confirmed tipjob entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"tipjob","field":"tipjob.one","op":"sum_over"}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 4c (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.tip_total`

- **Authored helper label:** This person's worksheet column (d) total
- **Encoded (NonNegDollars):** Add tipjob.col_d over every confirmed tipjob entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"tipjob","field":"tipjob.col_d","op":"sum_over"}`
- Cite: [i1040gi] p. 104, Qualified Tips From More Than One Employer Worksheet, line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.tip_reported`

- **Authored helper label:** This person's worksheet column (b) total
- **Encoded (NonNegDollars):** Add tipjob.amount over every confirmed tipjob entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"tipjob","field":"tipjob.amount","op":"sum_over"}`
- Cite: [i1040gi] p. 104, Qualified Tips From More Than One Employer Worksheet, column (b) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ot_employers`

- **Authored helper label:** Number of employers that paid this person qualified overtime compensation
- **Encoded (Count):** Add otjob.one over every confirmed otjob entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"otjob","field":"otjob.one","op":"sum_over"}`
- Cite: [i1040gi] p. 108, Schedule 1-A, line 14a, and the Qualified Overtime Compensation From More Than One Employer Worksheet (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ot_total`

- **Authored helper label:** This person's overtime worksheet column (b) total
- **Encoded (NonNegDollars):** Add otjob.col_b over every confirmed otjob entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"otjob","field":"otjob.col_b","op":"sum_over"}`
- Cite: [i1040gi] p. 108, Schedule 1-A, line 14a, and the Qualified Overtime Compensation From More Than One Employer Worksheet, line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## rrta — `person.rrta`

- **Authored helper label:** Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or did you file Form CT-2 as an employee representative?
- **Encoded (Bool):** Input — Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or did you file Form CT-2 as an employee representative?
- Expr: `{"op":"input","source":"Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or did you file Form CT-2 as an employee representative?"}`
- Cite: [iw2w3] pp. 12–13, Railroad employers: RRTA compensation and taxes in box 14; boxes 3–7 are not used for RRTA (2025; printed date 2025-02-19; sha256 bfecbc99)

## (helper) — `person.sc_rrta_count`

- **Authored helper label:** Number of this person's Schedules C while this person has railroad retirement compensation
- **Encoded (Count):** Add sc.one over every confirmed sc entry for which helper "This business's owner has railroad retirement compensation" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.one","op":"sum_over","where":{"eq":["sc.rrta",{"const":true}],"op":"test"}}`
- Cite: [f1040sse] Schedule SE (2025), line 8a, "Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2) and railroad retirement (tier 1) compensation" (2025; created 2025-05-07; sha256 05bc2b3e)

## (gate) — `person.se_rrta`

- **Authored helper label:** Self-employment and railroad retirement compensation together
- **Encoded (Bool):** helper "Number of this person's Schedules C while this person has railroad retirement compensation" > 0 (a count)
- Note: Counted through the person's Schedules C, so the railroad question is asked only of a person with a business.
- Expr: `{"gt":["person.sc_rrta_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [f1040sse] Schedule SE (2025), line 8a, "Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2) and railroad retirement (tier 1) compensation" (2025; created 2025-05-07; sha256 05bc2b3e)

## employers — `person.employers`

- **Authored helper label:** Total w2.one for this person
- **Encoded (Count):** Add w2.one over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"w2","field":"w2.one","op":"sum_over"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## overcount — `person.overcount`

- **Authored helper label:** Number of employers that withheld more than the limit
- **Encoded (Count):** Add w2.one over every confirmed w2 entry for which helper "Did this employer withhold more than $10,918.20?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"w2","field":"w2.one","op":"sum_over","where":{"eq":["w2.over",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## over — `person.over`

- **Authored helper label:** Any employer withheld more than the limit
- **Encoded (Bool):** line overcount > 0 (a count)
- Expr: `{"gt":["person.overcount",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## wages — `person.wages`

- **Authored helper label:** Total w2.wages for this person
- **Encoded (NonNegDollars):** Add w2.wages over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Interpretation: amb.2025.ss_wages
- Expr: `{"collection":"w2","field":"w2.wages","op":"sum_over"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## withheld — `person.withheld`

- **Authored helper label:** Total w2.box4 for this person
- **Encoded (NonNegDollars):** Add w2.box4 over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"w2","field":"w2.box4","op":"sum_over"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.box1`

- **Authored helper label:** Total W-2 box 1 for this person
- **Encoded (NonNegDollars):** Add w2.box1 over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"w2","field":"w2.box1","op":"sum_over"}`
- Cite: [f1040] Form 1040 (2025), line 1a (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `person.box2`

- **Authored helper label:** Total W-2 box 2 for this person
- **Encoded (NonNegDollars):** Add w2.box2 over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"w2","field":"w2.box2","op":"sum_over"}`
- Cite: [f1040] p. 2, Payments and Refundable Credits, line 25a, "Federal income tax withheld from:", "Form(s) W-2" (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `person.ira_amount_a`

- **Authored helper label:** IRA distributions on this person's Forms 1099-R (line 4a amounts)
- **Encoded (NonNegDollars):** Add retirement.amount_a over every confirmed retirement entry for which helper "IRA distribution (lines 4a and 4b)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.amount_a","op":"sum_over","where":{"eq":["retirement.is_ira",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] pp. 26-27, Lines 4a and 4b (total distributions where an exception applies; 'More than one distribution') (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_taxable`

- **Authored helper label:** Taxable IRA distributions on this person's Forms 1099-R (line 4b amounts)
- **Encoded (NonNegDollars):** Add retirement.taxable over every confirmed retirement entry for which helper "IRA distribution (lines 4a and 4b)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.taxable","op":"sum_over","where":{"eq":["retirement.is_ira",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 27, line 4b, 'figure the taxable amount of each distribution and enter the total of the taxable amounts on line 4b' (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_rollovers`

- **Authored helper label:** Number of this person's IRA distributions with a rollover
- **Encoded (Count):** Add retirement.one over every confirmed retirement entry for which helper "IRA distribution (lines 4a and 4b)" = true and helper "Part or all of the distribution was rolled over (an amount rolled over, or a direct rollover, code G)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.one","op":"sum_over","where":{"all":[{"eq":["retirement.is_ira",{"const":true}],"op":"test"},{"eq":["retirement.has_rollover",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] p. 27, Exception 1, 'Also check box 1 on line 4c' (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.plan_amount_a`

- **Authored helper label:** Pension and annuity distributions on this person's Forms 1099-R (line 5a amounts)
- **Encoded (NonNegDollars):** Add retirement.amount_a over every confirmed retirement entry for which helper "IRA distribution (lines 4a and 4b)" = false, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.amount_a","op":"sum_over","where":{"eq":["retirement.is_ira",{"const":false}],"op":"test"}}`
- Cite: [i1040gi] pp. 28-30, Lines 5a and 5b (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.plan_taxable`

- **Authored helper label:** Taxable pension and annuity distributions on this person's Forms 1099-R (line 5b amounts)
- **Encoded (NonNegDollars):** Add retirement.taxable over every confirmed retirement entry for which helper "IRA distribution (lines 4a and 4b)" = false, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.taxable","op":"sum_over","where":{"eq":["retirement.is_ira",{"const":false}],"op":"test"}}`
- Cite: [i1040gi] pp. 28-30, Lines 5a and 5b; p. 29, Simplified Method Worksheet, 'Enter the total of the taxable parts on Form 1040 or 1040-SR, line 5b' (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.plan_rollovers`

- **Authored helper label:** Number of this person's pension distributions with a rollover
- **Encoded (Count):** Add retirement.one over every confirmed retirement entry for which helper "IRA distribution (lines 4a and 4b)" = false and helper "Part or all of the distribution was rolled over (an amount rolled over, or a direct rollover, code G)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.one","op":"sum_over","where":{"all":[{"eq":["retirement.is_ira",{"const":false}],"op":"test"},{"eq":["retirement.has_rollover",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] p. 30, Rollovers, 'Also check box 1 on line 5c' (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.sav_dist`

- **Authored helper label:** Distributions received in 2025 that Form 8880 line 4 counts, on this person's Forms 1099-R
- **Encoded (NonNegDollars):** Add retirement.sav_amount over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.sav_amount","op":"sum_over"}`
- Cite: [f8880] p. 2, Line 4, "Enter the total amount of distributions you, and your spouse if filing jointly, received after 2022 and before the due date of your 2025 return (including extensions)" (2025; created 2025-11-04; sha256 ba2b2877)

## eligible — `person.eligible`

- **Authored helper label:** More than one employer and total social security wages over $176,100
- **Encoded (Bool):** line employers > 1 (a count) and line wages > $176,100 (ss.base)
- Expr: `{"all":[{"gt":["person.employers",{"const":1,"type":"Count"}],"op":"test"},{"gt":["person.wages",{"param":"ss.base"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## excess — `person.excess`

- **Authored helper label:** Withholding above $10,918.20, if any
- **Encoded (NonNegDollars):** Subtract $10,918.20 (ss.limit) from line withheld. If zero or less, enter -0-.
- Expr: `{"from":"person.withheld","op":"subtract_floor0","take":{"param":"ss.limit"}}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## zero — `person.zero`

- **Authored helper label:** No excess credit
- **Encoded (NonNegDollars):** Enter $0 (ss.zero).
- Expr: `{"op":"param","ref":"ss.zero"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## credit — `person.credit`

- **Authored helper label:** Excess social security tax withheld, figured separately for this person
- **Encoded (NonNegDollars):** Choose — [line eligible = true → line excess] [line eligible = false → line zero]
- **Refusal:** when person.rrta is true, cannot complete Schedule 3 line 11 (RRTA path). This stage handles Social Security only. Use the railroad retirement instructions; excess Tier 2 tax uses Form 843 rather than Form 1040. Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when person.over is true, cannot complete Form 843. An employer withheld more than $10,918.20. Ask that employer to adjust the tax. If the employer does not adjust the overcollection, you can file a refund claim using Form 843. This tool cannot complete the credit until the overcollection is resolved. Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"alternatives":[{"guard":{"eq":["person.eligible",{"const":true}],"op":"test"},"then":"person.excess"},{"guard":{"eq":["person.eligible",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.medicare5`

- **Authored helper label:** Total W-2 box 5 for this person
- **Encoded (NonNegDollars):** Add w2.box5 over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when person.rrta is true, cannot complete Form 8959 RRTA computation. RRTA compensation is outside the supported wage-only path. Cite: [f8959] Form 8959 (2025), lines 1–24; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004)
- Expr: `{"collection":"w2","field":"w2.box5","op":"sum_over"}`
- Cite: [f8959] Form 8959 (2025), line 1, "Medicare wages and tips from Form W-2, box 5", "enter the total of the amounts from box 5"; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004)

## (helper) — `person.medicare6`

- **Authored helper label:** Total W-2 box 6 for this person
- **Encoded (NonNegDollars):** Add w2.box6 over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when person.rrta is true, cannot complete Form 8959 RRTA computation. RRTA compensation is outside the supported wage-only path. Cite: [f8959] Form 8959 (2025), lines 1–24; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004)
- Expr: `{"collection":"w2","field":"w2.box6","op":"sum_over"}`
- Cite: [f8959] Form 8959 (2025), line 19, "Medicare tax withheld from Form W-2, box 6", "enter the total of the amounts from box 6"; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004)

## (helper) — `person.sc_count`

- **Authored helper label:** Number of Schedules C for this person
- **Encoded (Count):** Add sc.one over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.one","op":"sum_over"}`
- Cite: [i1040sc] p. 14, Line 31; i4562 p. 4, Part I (2025; sha256 b5536db9)

## (helper) — `person.ho_count`

- **Authored helper label:** Number of this person's Schedules C that claim the business use of the home
- **Encoded (Count):** Add sc.one over every confirmed sc entry for which column (screen) (sc.ho_uses) = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.one","op":"sum_over","where":{"eq":["sc.ho_uses",{"const":true}],"op":"test"}}`
- Cite: [i1040sc] p. 10, Simplified method, "You are limited to a maximum of 300 square feet for all of the businesses you conduct in your home that qualify for this deduction" (2025; sha256 b5536db9)

## (helper) — `person.mq_q4`

- **Authored helper label:** Mid-quarter test basis, fourth quarter, this person
- **Encoded (NonNegDollars):** Add sc.mq_q4 over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.mq_q4","op":"sum_over"}`
- Cite: [i1040sc] p. 14, Line 31; i4562 p. 4, Part I (2025; sha256 b5536db9)

## (helper) — `person.mq_total`

- **Authored helper label:** Mid-quarter test basis, 2025, this person
- **Encoded (NonNegDollars):** Add sc.mq_total over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.mq_total","op":"sum_over"}`
- Cite: [i1040sc] p. 14, Line 31; i4562 p. 4, Part I (2025; sha256 b5536db9)

## (helper) — `person.cost179`

- **Authored helper label:** Cost of section 179 property, this person
- **Encoded (NonNegDollars):** Add sc.cost179 over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.cost179","op":"sum_over"}`
- Cite: [i1040sc] p. 14, Line 31; i4562 p. 4, Part I (2025; sha256 b5536db9)

## (helper) — `person.s179_nonlisted`

- **Authored helper label:** Section 179 elected, other than listed property, this person
- **Encoded (NonNegDollars):** Add sc.f6 over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.f6","op":"sum_over"}`
- Cite: [i1040sc] p. 14, Line 31; i4562 p. 4, Part I (2025; sha256 b5536db9)

## (helper) — `person.s179_listed`

- **Authored helper label:** Section 179 elected on listed property, this person
- **Encoded (NonNegDollars):** Add sc.f29 over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.f29","op":"sum_over"}`
- Cite: [i1040sc] p. 14, Line 31; i4562 p. 4, Part I (2025; sha256 b5536db9)

## (helper) — `person.income179`

- **Authored helper label:** Business net profit or loss without section 179, this person
- **Encoded (Dollars):** Add sc.line31_pre179 over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.line31_pre179","op":"sum_over"}`
- Cite: [i1040sc] p. 14, Line 31; i4562 p. 4, Part I (2025; sha256 b5536db9)

## (helper) — `person.has_sc`

- **Authored helper label:** This person has at least one Schedule C
- **Encoded (Bool):** helper "Number of Schedules C for this person" > 0 (a count)
- Expr: `{"gt":["person.sc_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040sse] p. 1, Who Must File Schedule SE; p. 2, Joint Returns, "If both spouses have self-employment income, each must file a separate Schedule SE" (2025; sha256 ea9e3120)

## (helper) — `person.sc_total`

- **Authored helper label:** This person's Schedule C net profit or loss (all businesses)
- **Encoded (Dollars):** Add sc.result over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.result","op":"sum_over"}`
- Cite: [i1040sse] p. 2, More Than One Business, "Figure the combined SE tax on one Schedule SE" (2025; sha256 ea9e3120)

## (screen) — `person.se_screen`

- **Authored helper label:** Does any of these apply to this person's self-employment?
- **Encoded (Bool):** Input — Does any of these apply to this person: church employee income (wages from a church that elected exemption from social security and Medicare taxes); being a minister, a member of a religious order or a Christian Science practitioner, or having an approved Form 4361 or Form 4029; net earnings from self-employment from a partnership (Schedule K-1, box 14, code A) or other self-employment income not on a Schedule C (such as director's fees, fiduciary fees, or fees as a fee-basis state or local government employee); farm income (Schedule F) or Conservation Reserve Program payments; electing an optional method (Schedule SE Part II); a chapter 11 bankruptcy case; community income on a separate return; self-employment income exempt under an international social security agreement or earned as a U.S. citizen employed by a foreign government; or tips reported on Form 4137 or wages on Form 8919?
- Expr: `{"op":"input","source":"Does any of these apply to this person: church employee income (wages from a church that elected exemption from social security and Medicare taxes); being a minister, a member of a religious order or a Christian Science practitioner, or having an approved Form 4361 or Form 4029; net earnings from self-employment from a partnership (Schedule K-1, box 14, code A) or other self-employment income not on a Schedule C (such as director's fees, fiduciary fees, or fees as a fee-basis state or local government employee); farm income (Schedule F) or Conservation Reserve Program payments; electing an optional method (Schedule SE Part II); a chapter 11 bankruptcy case; community income on a separate return; self-employment income exempt under an international social security agreement or earned as a U.S. citizen employed by a foreign government; or tips reported on Form 4137 or wages on Form 8919?"}`
- Cite: [i1040sse] pp. 1-5, Who Must Pay Self-Employment (SE) Tax, Net Earnings From Self-Employment, Instructions for Part II; f1040sse lines 1a, 1b, 5a, 8b and 8c (2025; sha256 ea9e3120)

## (gate) — `person.se_screened`

- **Authored helper label:** This person's self-employment tax is outside this tool
- **Encoded (Bool):** column (screen) (person.se_screen) = true
- Expr: `{"eq":["person.se_screen",{"const":true}],"op":"test"}`
- Cite: [i1040sse] pp. 1-5 (2025; sha256 ea9e3120)

## (helper) — `person.se_line2`

- **Authored helper label:** Schedule SE line 2 for this person
- **Encoded (Dollars):** Enter the amount from helper "This person's Schedule C net profit or loss (all businesses)".
- **Refusal:** when person.se_screened is true, cannot complete Schedule SE items outside this tool (church employee income, clergy, Forms 4361 and 4029, partnership and other self-employment income, farm income, optional methods, chapter 11, community income, exempt income, Forms 4137 and 8919). These self-employment tax items are outside this tool. Cite: [i1040sse] pp. 1-5 (2025; sha256 ea9e3120)
- Expr: `{"from":"person.sc_total","op":"copy"}`
- Cite: [f1040sse] Schedule SE (2025), line 2, "Net profit or (loss) from Schedule C, line 31" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `person.se_line6`

- **Authored helper label:** Schedule SE line 6 for this person
- **Encoded (NonNegDollars):** Choose — [helper "This person has at least one Schedule C" = true → "line6" of Schedule SE (Form 1040) — Self-Employment Tax, one per person with line2 = helper "Schedule SE line 2 for this person" and line8a = line wages] [helper "This person has at least one Schedule C" = false → line zero]
- **Refusal:** when person.se_rrta is true, cannot complete Schedule SE with railroad retirement (tier 1) compensation. Schedule SE line 8a adds railroad retirement (tier 1) compensation to the social security wages, and this tool does not take railroad compensation. Prepare Schedule SE with the railroad retirement instructions. Cite: [f1040sse] Schedule SE (2025), line 8a, "Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2) and railroad retirement (tier 1) compensation" (2025; created 2025-05-07; sha256 05bc2b3e)
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":{"bind":{"line2":"person.se_line2","line8a":"person.wages"},"def":"se","line":"line6"}},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f1040sse] Schedule SE (2025), line 6, "Add lines 4c and 5b"; i8959 p. 3, Line 8, "Enter your self-employment income from Schedule SE (Form 1040), Part I, line 6" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `person.se_line12`

- **Authored helper label:** Schedule SE line 12 (self-employment tax) for this person
- **Encoded (NonNegDollars):** Choose — [helper "This person has at least one Schedule C" = true → "line12" of Schedule SE (Form 1040) — Self-Employment Tax, one per person with line2 = helper "Schedule SE line 2 for this person" and line8a = line wages] [helper "This person has at least one Schedule C" = false → line zero]
- **Refusal:** when person.se_rrta is true, cannot complete Schedule SE with railroad retirement (tier 1) compensation. Schedule SE line 8a adds railroad retirement (tier 1) compensation to the social security wages, and this tool does not take railroad compensation. Prepare Schedule SE with the railroad retirement instructions. Cite: [f1040sse] Schedule SE (2025), line 8a, "Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2) and railroad retirement (tier 1) compensation" (2025; created 2025-05-07; sha256 05bc2b3e)
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":{"bind":{"line2":"person.se_line2","line8a":"person.wages"},"def":"se","line":"line12"}},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f1040sse] Schedule SE (2025), line 12, "Enter here and on Schedule 2 (Form 1040), line 4" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `person.se_line13`

- **Authored helper label:** Schedule SE line 13 (deduction for one-half of self-employment tax) for this person
- **Encoded (NonNegDollars):** Choose — [helper "This person has at least one Schedule C" = true → "line13" of Schedule SE (Form 1040) — Self-Employment Tax, one per person with line2 = helper "Schedule SE line 2 for this person" and line8a = line wages] [helper "This person has at least one Schedule C" = false → line zero]
- **Refusal:** when person.se_rrta is true, cannot complete Schedule SE with railroad retirement (tier 1) compensation. Schedule SE line 8a adds railroad retirement (tier 1) compensation to the social security wages, and this tool does not take railroad compensation. Prepare Schedule SE with the railroad retirement instructions. Cite: [f1040sse] Schedule SE (2025), line 8a, "Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2) and railroad retirement (tier 1) compensation" (2025; created 2025-05-07; sha256 05bc2b3e)
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":{"bind":{"line2":"person.se_line2","line8a":"person.wages"},"def":"se","line":"line13"}},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f1040sse] Schedule SE (2025), line 13, "Enter here and on Schedule 1 (Form 1040), line 15" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `person.se_line4c`

- **Authored helper label:** Schedule SE line 4c for this person
- **Encoded (NonNegDollars):** Choose — [helper "This person has at least one Schedule C" = true → "line4c" of Schedule SE (Form 1040) — Self-Employment Tax, one per person with line2 = helper "Schedule SE line 2 for this person" and line8a = line wages] [helper "This person has at least one Schedule C" = false → line zero]
- **Refusal:** when person.se_rrta is true, cannot complete Schedule SE with railroad retirement (tier 1) compensation. Schedule SE line 8a adds railroad retirement (tier 1) compensation to the social security wages, and this tool does not take railroad compensation. Prepare Schedule SE with the railroad retirement instructions. Cite: [f1040sse] Schedule SE (2025), line 8a, "Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2) and railroad retirement (tier 1) compensation" (2025; created 2025-05-07; sha256 05bc2b3e)
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":{"bind":{"line2":"person.se_line2","line8a":"person.wages"},"def":"se","line":"line4c"}},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f1040sse] Schedule SE (2025), line 4c, "Combine lines 4a and 4b. If less than $400, stop; you don’t owe self-employment tax" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `person.plan`

- **Authored helper label:** Retirement plan of this self-employed person
- **Encoded (Enum(retire_plan)):** Input — Did you (this person) contribute for yourself, as a self-employed person, to a SEP IRA (sep) or a SIMPLE IRA (simple) for 2025, or to neither (none)?
- Expr: `{"op":"input","source":"Did you (this person) contribute for yourself, as a self-employed person, to a SEP IRA (sep) or a SIMPLE IRA (simple) for 2025, or to neither (none)?"}`
- Cite: [p560] pp. 8–11, 14–17, chapter 2, Simplified Employee Pension (SEP); chapter 3, SIMPLE IRA Plan; i1040gi Schedule 1, line 16 (For use in preparing 2025 returns; sha256 1f1f7abe)

## (screen) — `person.plan_screen`

- **Authored helper label:** Does any of these apply to this person's retirement contributions?
- **Encoded (Bool):** Input — Does any of these apply: a SARSEP; a SEP plan whose contribution rate is not a whole percentage or is more than 25%; a SIMPLE IRA plan of an employer that allows the higher contribution limits of section 117 of the SECURE 2.0 Act; contributions for yourself to more than one plan, or to a qualified plan (such as a solo 401(k)); salary reduction contributions or elective deferrals to any other plan in 2025 (such as a 401(k) or 403(b) through an employer); Roth SEP or Roth SIMPLE contributions; or contributions that are more than the maximum deductible amount?
- Expr: `{"op":"input","source":"Does any of these apply: a SARSEP; a SEP plan whose contribution rate is not a whole percentage or is more than 25%; a SIMPLE IRA plan of an employer that allows the higher contribution limits of section 117 of the SECURE 2.0 Act; contributions for yourself to more than one plan, or to a qualified plan (such as a solo 401(k)); salary reduction contributions or elective deferrals to any other plan in 2025 (such as a 401(k) or 403(b) through an employer); Roth SEP or Roth SIMPLE contributions; or contributions that are more than the maximum deductible amount?"}`
- Cite: [p560] pp. 11, 16, 38, chapter 2, Salary Reduction Simplified Employee Pension (SARSEP); chapter 3, Salary reduction contributions; chapter 5, Caution, "apply only to self-employed individuals who have only one defined contribution plan" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (gate) — `person.plan_screened`

- **Authored helper label:** This person's retirement contributions are outside this tool (screened, or a plan with more than one Schedule C)
- **Encoded (Bool):** (column (screen) (person.plan_screen) = true or not helper "Retirement plan of this self-employed person" = 'none' and helper "Number of Schedules C for this person" > 1 (a count))
- Expr: `{"any":[{"eq":["person.plan_screen",{"const":true}],"op":"test"},{"all":[{"not":{"eq":["person.plan",{"const":"none"}],"op":"test"},"op":"test"},{"gt":["person.sc_count",{"const":1,"type":"Count"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [p560] pp. 8–11, 14–17, 38–40, chapters 2, 3 and 5; p. 7, "If you have more than one business, but only one has a retirement plan, only the earned income from that business is considered for that plan" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.cent`

- **Authored helper label:** One cent
- **Encoded (NonNegDollars):** Enter $0.01 (sc.one_cent).
- Expr: `{"op":"param","ref":"sc.one_cent"}`
- Cite: [p560] pp. 38–40, chapter 5, Rate Table for Self-Employed (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.hundred`

- **Authored helper label:** 100%, as cents
- **Encoded (NonNegDollars):** Enter $1 (sc.hundred_cents).
- Expr: `{"op":"param","ref":"sc.hundred_cents"}`
- Cite: [p560] pp. 38–40, chapter 5, Rate Worksheet for Self-Employed, "Rate in line 1 plus 1" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.sep_rate`

- **Authored helper label:** Plan contribution rate (whole percent)
- **Encoded (Count):** Input — The contribution rate stated in your SEP plan, as a whole percent (for example 10)
- Expr: `{"op":"input","source":"The contribution rate stated in your SEP plan, as a whole percent (for example 10)"}`
- Cite: [p560] pp. 38–40, chapter 5, Rate Table for Self-Employed, "find your plan contribution rate (the contribution rate stated in your plan)" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.sep_contrib`

- **Authored helper label:** Contributions to your own SEP IRA for 2025
- **Encoded (NonNegDollars):** Input — The contributions you made for yourself to your SEP IRA for 2025 (by the due date of the return, including extensions)
- **Refusal:** when person.plan_screened is true, cannot complete Retirement plan contributions outside this tool (SARSEP, other plan rates, higher SIMPLE limits, more than one plan, a plan with more than one Schedule C, other elective deferrals, Roth contributions, excess contributions). These retirement contributions are outside this tool. Cite: [p560] pp. 8–11, 14–17, 38–40, chapters 2, 3 and 5 (For use in preparing 2025 returns; sha256 1f1f7abe)
- Expr: `{"op":"input","source":"The contributions you made for yourself to your SEP IRA for 2025 (by the due date of the return, including extensions)"}`
- Cite: [p560] pp. 11, 39, chapter 2, Deduction Limit for Self-Employed Individuals; chapter 5, Deduction Worksheet for Self-Employed, "Next: Enter your actual contribution" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.sep_rate_c`

- **Authored helper label:** The plan rate, as cents
- **Encoded (NonNegDollars):** Multiply helper "One cent" by the number on helper "Plan contribution rate (whole percent)".
- Expr: `{"amount":"person.cent","count":"person.sep_rate","op":"multiply_count"}`
- Cite: [p560] pp. 38–40, chapter 5, Rate Worksheet for Self-Employed, line 1 (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.sep_rate_plus`

- **Authored helper label:** The plan rate plus 100%, as cents
- **Encoded (NonNegDollars):** Add helper "The plan rate, as cents" and helper "100%, as cents".
- Expr: `{"of":["person.sep_rate_c","person.hundred"],"op":"sum"}`
- Cite: [p560] pp. 38–40, chapter 5, Rate Worksheet for Self-Employed, line 2, "Rate in line 1 plus 1" (For use in preparing 2025 returns; sha256 1f1f7abe)

## Step 1 — `person.sep_s1`

- **Authored helper label:** Net profit from Schedule C, line 31
- **Encoded (Dollars):** Enter the amount from helper "This person's Schedule C net profit or loss (all businesses)".
- **Refusal:** when person.se_screened is true, cannot complete SEP Deduction Worksheet Step 1 with self-employment income not on a Schedule C (Schedule F, Schedule K-1 box 14 code A and the other items of the self-employment screen). These self-employment items are outside this tool. Cite: [p560] p. 39, chapter 5, Deduction Worksheet for Self-Employed, Step 1, "Enter your net profit from" (For use in preparing 2025 returns; sha256 1f1f7abe)
- Expr: `{"from":"person.sc_total","op":"copy"}`
- Cite: [p560] p. 39, chapter 5, Deduction Worksheet for Self-Employed, Step 1 (For use in preparing 2025 returns; sha256 1f1f7abe)

## Step 2 — `person.sep_s2`

- **Authored helper label:** Deduction for self-employment tax from Schedule 1, line 15
- **Encoded (NonNegDollars):** Enter the amount from helper "Schedule SE line 13 (deduction for one-half of self-employment tax) for this person".
- Expr: `{"from":"person.se_line13","op":"copy"}`
- Cite: [p560] p. 39, chapter 5, Deduction Worksheet for Self-Employed, Step 2 (this person's own Schedule SE, line 13) (For use in preparing 2025 returns; sha256 1f1f7abe)

## Step 3 — `person.sep_s3`

- **Authored helper label:** Net earnings from self-employment. Subtract step 2 from step 1
- **Encoded (NonNegDollars):** Subtract line Step 2 from line Step 1. If zero or less, enter -0-.
- Expr: `{"from":"person.sep_s1","op":"subtract_floor0","take":"person.sep_s2"}`
- Cite: [p560] p. 39, chapter 5, Deduction Worksheet for Self-Employed, Step 3 (For use in preparing 2025 returns; sha256 1f1f7abe)

## Step 5 — `person.sep_s5`

- **Authored helper label:** Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six decimal places)
- **Encoded (NonNegDollars):** Divide helper "The plan rate, as cents" by helper "The plan rate plus 100%, as cents", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply line Step 3 by the result.
- Expr: `{"amount":"person.sep_s3","op":"prorate","part":"person.sep_rate_c","places":6,"whole":"person.sep_rate_plus"}`
- Cite: [p560] pp. 39–40, chapter 5, Deduction Worksheet for Self-Employed, Steps 4 and 5, "Enter your rate from the Rate Table for Self-Employed or Rate Worksheet for Self-Employed", "Multiply step 3 by step 4"; p. 38, chapter 5, Rate Table for Self-Employed, "If your plan's contribution rate is 10% of a participant's compensation, your rate is 0.090909" (amb.2025.sep_rate_places) (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.comp_limit`

- **Authored helper label:** $350,000
- **Encoded (NonNegDollars):** Enter $350,000 (ret.comp_limit).
- Expr: `{"op":"param","ref":"ret.comp_limit"}`
- Cite: [p560] p. 39, chapter 5, Deduction Worksheet for Self-Employed, Step 6, "Multiply $350,000" (For use in preparing 2025 returns; sha256 1f1f7abe)

## Step 6 — `person.sep_s6`

- **Authored helper label:** Multiply $350,000 by your plan contribution rate (not the reduced rate)
- **Encoded (NonNegDollars):** Divide helper "The plan rate, as cents" by helper "100%, as cents", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "$350,000" by the result.
- Expr: `{"amount":"person.comp_limit","op":"prorate","part":"person.sep_rate_c","places":6,"whole":"person.hundred"}`
- Cite: [p560] p. 39, chapter 5, Deduction Worksheet for Self-Employed, Step 6 (For use in preparing 2025 returns; sha256 1f1f7abe)

## Step 7 — `person.sep_s7`

- **Authored helper label:** Enter the smaller of step 5 or step 6
- **Encoded (NonNegDollars):** Enter the smaller of line Step 5 or line Step 6.
- Expr: `{"of":["person.sep_s5","person.sep_s6"],"op":"smaller_of"}`
- Cite: [p560] p. 39, chapter 5, Deduction Worksheet for Self-Employed, Step 7 (For use in preparing 2025 returns; sha256 1f1f7abe)

## Step 8 — `person.sep_s8`

- **Authored helper label:** Contribution dollar limit
- **Encoded (NonNegDollars):** Enter $70,000 (ret.sep_dollar_limit).
- Expr: `{"op":"param","ref":"ret.sep_dollar_limit"}`
- Cite: [p560] p. 39, chapter 5, Deduction Worksheet for Self-Employed, Step 8, "$70,000" (For use in preparing 2025 returns; sha256 1f1f7abe)

## Step 21 — `person.sep_s21`

- **Authored helper label:** Maximum deductible contribution (the smaller of step 7 or step 8; no elective deferrals)
- **Encoded (NonNegDollars):** Enter the smaller of line Step 7 or line Step 8.
- Expr: `{"of":["person.sep_s7","person.sep_s8"],"op":"smaller_of"}`
- Cite: [p560] p. 39, chapter 5, Deduction Worksheet for Self-Employed, Step 8 note, "Otherwise, skip steps 9 through 20 and enter the smaller of step 7 or step 8 on step 21" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (gate) — `person.sep_excess`

- **Authored helper label:** The SEP contributions are more than the maximum deductible contribution
- **Encoded (Bool):** helper "Contributions to your own SEP IRA for 2025" > line Step 21
- Expr: `{"gt":["person.sep_contrib","person.sep_s21"],"op":"test"}`
- Cite: [p560] p. 39, chapter 5, "Enter your actual contribution, not to exceed your maximum deductible contribution"; p. 11, chapter 2, Carryover of Excess SEP Contributions, "If you made SEP contributions that are more than the deduction limit (nondeductible contributions), you can carry over and deduct the difference in later years" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.sep_deduction`

- **Authored helper label:** SEP deduction for yourself
- **Encoded (NonNegDollars):** Enter the amount from helper "Contributions to your own SEP IRA for 2025".
- **Refusal:** when person.sep_excess is true, cannot complete SEP contributions above the maximum deductible contribution. Excess SEP contributions are outside this tool. Cite: [p560] pp. 11, 39, chapter 2, Excess contributions; chapter 5 (For use in preparing 2025 returns; sha256 1f1f7abe)
- Expr: `{"from":"person.sep_contrib","op":"copy"}`
- Cite: [p560] p. 39, chapter 5, "Enter your actual contribution, not to exceed your maximum deductible contribution, on Schedule 1 (Form 1040), line 16" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_deferral`

- **Authored helper label:** Salary reduction contributions for yourself to your SIMPLE IRA (including catch-up)
- **Encoded (NonNegDollars):** Input — The salary reduction contributions you made for yourself to your SIMPLE IRA for 2025, including any catch-up contributions
- **Refusal:** when person.plan_screened is true, cannot complete Retirement plan contributions outside this tool. These retirement contributions are outside this tool. Cite: [p560] pp. 8–11, 14–17, 38–40, chapters 2, 3 and 5 (For use in preparing 2025 returns; sha256 1f1f7abe)
- Expr: `{"op":"input","source":"The salary reduction contributions you made for yourself to your SIMPLE IRA for 2025, including any catch-up contributions"}`
- Cite: [p560] p. 16, chapter 3, Salary reduction contributions and Catch-up contributions (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_age`

- **Authored helper label:** Catch-up eligibility
- **Encoded (Enum(catchup_age)):** Input — Your age at the end of 2025 for SIMPLE catch-up contributions: under 50 (under50), 50 to 59 or 64 and over (age50), or 60, 61, 62 or 63 (age60_63)
- Expr: `{"op":"input","source":"Your age at the end of 2025 for SIMPLE catch-up contributions: under 50 (under50), 50 to 59 or 64 and over (age50), or 60, 61, 62 or 63 (age60_63)"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "age 50 or over at the end of the calendar year" and "in a tax year in which they attain age 60, 61, 62, or 63" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_kind`

- **Authored helper label:** Employer contribution formula of your SIMPLE IRA plan
- **Encoded (Enum(simple_formula)):** Input — The employer contribution formula of your SIMPLE IRA plan for 2025: matching contributions (match) or 2% nonelective contributions (nonelective)
- Expr: `{"op":"input","source":"The employer contribution formula of your SIMPLE IRA plan for 2025: matching contributions (match) or 2% nonelective contributions (nonelective)"}`
- Cite: [p560] pp. 16–17, chapter 3, Employer matching contributions and Nonelective contributions (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_employer`

- **Authored helper label:** Employer contributions for yourself to your SIMPLE IRA
- **Encoded (NonNegDollars):** Input — The employer matching or nonelective contributions you made for yourself to your SIMPLE IRA for 2025
- Expr: `{"op":"input","source":"The employer matching or nonelective contributions you made for yourself to your SIMPLE IRA for 2025"}`
- Cite: [p560] pp. 16–17, chapter 3, Employer matching contributions and Nonelective contributions (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_comp`

- **Authored helper label:** Compensation: net earnings from self-employment (Schedule SE, line 4)
- **Encoded (NonNegDollars):** Enter the amount from helper "Schedule SE line 4c for this person".
- Expr: `{"from":"person.se_line4c","op":"copy"}`
- Cite: [p560] p. 15, chapter 3, Compensation, "If you are self-employed, compensation is your net earnings from self-employment (line 4 of Schedule SE (Form 1040)) before subtracting any contributions made to the SIMPLE IRA plan for yourself" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_cap`

- **Authored helper label:** Salary reduction limit
- **Encoded (NonNegDollars):** Enter $16,500 (ret.simple_limit).
- Expr: `{"op":"param","ref":"ret.simple_limit"}`
- Cite: [p560] p. 16, chapter 3, Salary reduction contributions, "can't be more than $16,500 for 2025" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_regular`

- **Authored helper label:** Salary reduction contributions that are not catch-up contributions
- **Encoded (NonNegDollars):** Enter the smaller of helper "Salary reduction contributions for yourself to your SIMPLE IRA (including catch-up)" or helper "Salary reduction limit".
- Expr: `{"of":["person.simple_deferral","person.simple_cap"],"op":"smaller_of"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "Salary reduction contributions aren't treated as catch-up contributions until they exceed $16,500 for 2025" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_catchup`

- **Authored helper label:** Catch-up contributions
- **Encoded (NonNegDollars):** Subtract helper "Salary reduction contributions that are not catch-up contributions" from helper "Salary reduction contributions for yourself to your SIMPLE IRA (including catch-up)". If zero or less, enter -0-.
- Expr: `{"from":"person.simple_deferral","op":"subtract_floor0","take":"person.simple_regular"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.catchup_limit`

- **Authored helper label:** Catch-up contribution limit
- **Encoded (NonNegDollars):** Find the entry in SIMPLE IRA catch-up contribution limit, 2025 (Pub. 560, chapter 3) for age helper "Catch-up eligibility".
- Expr: `{"keys":["person.simple_age"],"op":"keyed_lookup","table":"simple_catchup"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "generally $3,500 for 2025" and "the higher limit on catch-up contributions ... is $5,250" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.comp_after_regular`

- **Authored helper label:** Compensation less the salary reduction contributions that are not catch-up contributions
- **Encoded (NonNegDollars):** Subtract helper "Salary reduction contributions that are not catch-up contributions" from helper "Compensation: net earnings from self-employment (Schedule SE, line 4)". If zero or less, enter -0-.
- Expr: `{"from":"person.simple_comp","op":"subtract_floor0","take":"person.simple_regular"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "The excess of the participant's compensation over the salary reduction contributions that aren't catch-up contributions" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.catchup_max`

- **Authored helper label:** Maximum catch-up contribution
- **Encoded (NonNegDollars):** Enter the smaller of helper "Catch-up contribution limit" or helper "Compensation less the salary reduction contributions that are not catch-up contributions".
- Expr: `{"of":["person.catchup_limit","person.comp_after_regular"],"op":"smaller_of"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "can't exceed the lesser of the following amounts" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.rate3`

- **Authored helper label:** 3%
- **Encoded (Rate):** Enter 3% (0.03) (ret.match_rate).
- Expr: `{"op":"param","ref":"ret.match_rate"}`
- Cite: [p560] p. 16, chapter 3, Employer matching contributions, "up to 3% of the employee's compensation" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.rate2`

- **Authored helper label:** 2%
- **Encoded (Rate):** Enter 2% (0.02) (ret.nonelective_rate).
- Expr: `{"op":"param","ref":"ret.nonelective_rate"}`
- Cite: [p560] p. 17, chapter 3, Nonelective contributions, "nonelective contributions of 2% of compensation" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.match_3pct`

- **Authored helper label:** 3% of compensation
- **Encoded (NonNegDollars):** Multiply helper "Compensation: net earnings from self-employment (Schedule SE, line 4)" by helper "3%".
- Expr: `{"amount":"person.simple_comp","op":"multiply_rate","rate":"person.rate3"}`
- Cite: [p560] p. 16, chapter 3, Employer matching contributions (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.deferrals_total`

- **Authored helper label:** Salary reduction contributions (allowed)
- **Encoded (NonNegDollars):** Add helper "Salary reduction contributions that are not catch-up contributions" and helper "Catch-up contributions".
- Expr: `{"of":["person.simple_regular","person.simple_catchup"],"op":"sum"}`
- Cite: [p560] p. 16, chapter 3, Employer matching contributions, "match each employee's salary reduction contribution(s) on a dollar-for-dollar basis" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.match_max`

- **Authored helper label:** Maximum matching contribution
- **Encoded (NonNegDollars):** Enter the smaller of helper "Salary reduction contributions (allowed)" or helper "3% of compensation".
- Expr: `{"of":["person.deferrals_total","person.match_3pct"],"op":"smaller_of"}`
- Cite: [p560] p. 16, chapter 3, Employer matching contributions (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.ne_comp`

- **Authored helper label:** Compensation taken into account (not more than $350,000)
- **Encoded (NonNegDollars):** Enter the smaller of helper "Compensation: net earnings from self-employment (Schedule SE, line 4)" or helper "$350,000".
- Expr: `{"of":["person.simple_comp","person.comp_limit"],"op":"smaller_of"}`
- Cite: [p560] p. 17, chapter 3, Nonelective contributions, "Only $350,000 of the employee's compensation can be taken into account" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.ne_max`

- **Authored helper label:** Maximum nonelective contribution
- **Encoded (NonNegDollars):** Multiply helper "Compensation taken into account (not more than $350,000)" by helper "2%".
- Expr: `{"amount":"person.ne_comp","op":"multiply_rate","rate":"person.rate2"}`
- Cite: [p560] p. 17, chapter 3, Nonelective contributions (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.employer_max`

- **Authored helper label:** Maximum employer contribution for the plan's formula
- **Encoded (NonNegDollars):** Choose — [helper "Employer contribution formula of your SIMPLE IRA plan" = 'match' → helper "Maximum matching contribution"] [helper "Employer contribution formula of your SIMPLE IRA plan" = 'nonelective' → helper "Maximum nonelective contribution"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.simple_kind",{"const":"match"}],"op":"test"},"then":"person.match_max"},{"guard":{"eq":["person.simple_kind",{"const":"nonelective"}],"op":"test"},"then":"person.ne_max"}],"op":"choose"}`
- Cite: [p560] pp. 16–17, chapter 3, Employer matching contributions and Nonelective contributions (For use in preparing 2025 returns; sha256 1f1f7abe)

## (gate) — `person.simple_excess`

- **Authored helper label:** Contributions above the SIMPLE limits
- **Encoded (Bool):** (helper "Catch-up contributions" > helper "Maximum catch-up contribution" or helper "Employer contributions for yourself to your SIMPLE IRA" > helper "Maximum employer contribution for the plan's formula" or helper "Salary reduction contributions that are not catch-up contributions" > helper "Compensation: net earnings from self-employment (Schedule SE, line 4)")
- Expr: `{"any":[{"gt":["person.simple_catchup","person.catchup_max"],"op":"test"},{"gt":["person.simple_employer","person.employer_max"],"op":"test"},{"gt":["person.simple_regular","person.simple_comp"],"op":"test"}],"op":"test"}`
- Cite: [p560] p. 16, chapter 3, Salary reduction contributions, Catch-up contributions and Employer matching contributions (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_deduction`

- **Authored helper label:** SIMPLE deduction for yourself
- **Encoded (NonNegDollars):** Add helper "Salary reduction contributions (allowed)" and helper "Employer contributions for yourself to your SIMPLE IRA".
- **Refusal:** when person.simple_excess is true, cannot complete SIMPLE contributions above the limits. Excess SIMPLE contributions are outside this tool. Cite: [p560] pp. 14–17, chapter 3 (For use in preparing 2025 returns; sha256 1f1f7abe)
- Expr: `{"of":["person.deferrals_total","person.simple_employer"],"op":"sum"}`
- Cite: [p560] p. 17, chapter 3, Where To Deduct Contributions, "Sole proprietors and partners deduct contributions for themselves on line 16 of Schedule 1" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.plan_deduction`

- **Authored helper label:** Self-employed SEP or SIMPLE deduction for this person
- **Encoded (NonNegDollars):** Choose — [helper "Retirement plan of this self-employed person" = 'none' → line zero] [helper "Retirement plan of this self-employed person" = 'sep' → helper "SEP deduction for yourself"] [helper "Retirement plan of this self-employed person" = 'simple' → helper "SIMPLE deduction for yourself"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.plan",{"const":"none"}],"op":"test"},"then":"person.zero"},{"guard":{"eq":["person.plan",{"const":"sep"}],"op":"test"},"then":"person.sep_deduction"},{"guard":{"eq":["person.plan",{"const":"simple"}],"op":"test"},"then":"person.simple_deduction"}],"op":"choose"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 16, Self-Employed SEP, SIMPLE, and Qualified Plans; p560 p. 38, chapter 5, "if you are self-employed, you must use the rate table or rate worksheet and deduction worksheet to figure your deduction for contributions you made for yourself to a SEP IRA or qualified plan" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.s16`

- **Authored helper label:** Schedule 1 line 16 for this person
- **Encoded (NonNegDollars):** Choose — [helper "This person has at least one Schedule C" = true → helper "Self-employed SEP or SIMPLE deduction for this person"] [helper "This person has at least one Schedule C" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":"person.plan_deduction"},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 16, "If you were self-employed or a partner, you may be able to take this" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.positive_profits`

- **Authored helper label:** Total of all net profits of this person's businesses (losses not included)
- **Encoded (NonNegDollars):** Add sc.profit_pos over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.profit_pos","op":"sum_over"}`
- Cite: [i7206] f7206 Form 7206 (2025), line 5, "Enter the total of all net profits* from Schedule C (Form 1040), line 31; Schedule F (Form 1040), line 34; or Schedule K-1 (Form 1065), box 14, code A", "Don’t include any net losses shown on these schedules" (2025; sha256 9cbf92b3)

## (helper) — `person.sehi`

- **Authored helper label:** Self-employed health insurance deduction, this person
- **Encoded (NonNegDollars):** Add sc.f7206_line14 over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.f7206_line14","op":"sum_over"}`
- Cite: [f7206] Form 7206 (2025), line 14 (2025; created 2025-10-02; sha256 822203c9)

## (helper) — `person.qbi`

- **Authored helper label:** Qualified business income or loss of this person's businesses
- **Encoded (Dollars):** Add sc.qbi over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.qbi","op":"sum_over"}`
- Cite: [i8995] pp. 2, 4, Determining Your Qualified Business Income; p. 4, Line 1, "Enter on line 1(c) the net QBI or (loss) for the trade, business, or aggregation reported in the corresponding row" (2025; printed date 2026-01-26; sha256 875843ba)

## (helper) — `person.eic_part1`

- **Authored helper label:** Worksheet B, Part 1 for this person: Schedule SE line 3 less line 13
- **Encoded (Dollars):** Subtract helper "Schedule SE line 13 (deduction for one-half of self-employment tax) for this person" from helper "This person's Schedule C net profit or loss (all businesses)".
- Expr: `{"from":"person.sc_total","op":"subtract","take":"person.se_line13"}`
- Cite: [i1040gi] p. 47, Worksheet B, Part 1, lines 1a to 1e (line 1b is zero: the optional methods and church employee income are refused) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.files_se`

- **Authored helper label:** This person files Schedule SE (line 4c is $400 or more)
- **Encoded (Bool):** helper "Schedule SE line 4c for this person" > $0 (sales.zero)
- Expr: `{"gt":["person.se_line4c",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 47, Worksheet B, Part 1 and Part 2, "Self-Employed NOT Required To File Schedule SE" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.eic_se_has`

- **Authored helper label:** This person's self-employment earned income for Worksheet B
- **Encoded (Dollars):** Choose — [helper "This person files Schedule SE (line 4c is $400 or more)" = true → helper "Worksheet B, Part 1 for this person: Schedule SE line 3 less line 13"] [helper "This person files Schedule SE (line 4c is $400 or more)" = false → helper "This person's Schedule C net profit or loss (all businesses)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.files_se",{"const":true}],"op":"test"},"then":"person.eic_part1"},{"guard":{"eq":["person.files_se",{"const":false}],"op":"test"},"then":"person.sc_total"}],"op":"choose"}`
- Cite: [i1040gi] p. 47, Worksheet B, Part 1, line 1e, and Part 2, line 2b (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.eic_se`

- **Authored helper label:** Worksheet B, Parts 1 and 2, for this person
- **Encoded (Dollars):** Choose — [helper "This person has at least one Schedule C" = true → helper "This person's self-employment earned income for Worksheet B"] [helper "This person has at least one Schedule C" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":"person.eic_se_has"},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 47, Worksheet B, "If you are married filing a joint return, include your spouse's amounts, if any, with yours" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.sc_1a`

- **Authored helper label:** This person's Schedules C with Schedule 1-A tips or overtime
- **Encoded (Count):** Add sc.one over every confirmed sc entry for which column (screen) (sc.tips_ot) = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.one","op":"sum_over","where":{"eq":["sc.tips_ot",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.dc_benefits`

- **Authored helper label:** This person's dependent care benefits from Forms W-2 box 10, less the part reported in box 1
- **Encoded (NonNegDollars):** Add w2.dc_benefits over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"w2","field":"w2.dc_benefits","op":"sum_over"}`
- Cite: [i2441] p. 5, Line 12, "Amounts you received as an employee should be shown in box 10 of your Form(s) W-2" (2025; sha256 86f0669e)

## (helper) — `person.dc_box10`

- **Authored helper label:** Total of box 10 of this person's Forms W-2
- **Encoded (NonNegDollars):** Add w2.box10 over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Interpretation: amb.2025.dc_line1e_attribution
- Expr: `{"collection":"w2","field":"w2.box10","op":"sum_over"}`
- Cite: [i2441] p. 5, Line 12, "Amounts you received as an employee should be shown in box 10 of your Form(s) W-2" (2025; sha256 86f0669e)

## (helper) — `person.dc_has_box10`

- **Authored helper label:** This person's Forms W-2 show dependent care benefits in box 10
- **Encoded (Bool):** helper "Total of box 10 of this person's Forms W-2" > $0 (sales.zero)
- Interpretation: amb.2025.dc_line1e_attribution
- Expr: `{"gt":["person.dc_box10",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i2441] p. 4, Lines 4 and 5, "If filing jointly, figure your and your spouse's earned income separately" and "The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z" (2025; sha256 86f0669e)

## (helper) — `person.dc_1e_mine`

- **Authored helper label:** Form 1040 line 1e is counted in this person's earned income: the only person whose Forms W-2 show box 10, or, when there is no such single person, the taxpayer
- **Encoded (Bool):** (f2441 helper "Exactly one person on the return has Forms W-2 showing box 10" = true and helper "This person's Forms W-2 show dependent care benefits in box 10" = true or f2441 helper "Exactly one person on the return has Forms W-2 showing box 10" = false and helper "Whose entry is this, yours or your spouse's?" = 'taxpayer')
- Interpretation: amb.2025.dc_line1e_attribution
- Expr: `{"any":[{"all":[{"eq":["f2441.one_box10",{"const":true}],"op":"test"},{"eq":["person.dc_has_box10",{"const":true}],"op":"test"}],"op":"test"},{"all":[{"eq":["f2441.one_box10",{"const":false}],"op":"test"},{"eq":["person.role",{"const":"taxpayer"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i2441] p. 4, Lines 4 and 5, "If filing jointly, figure your and your spouse's earned income separately" and "The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z" (2025; sha256 86f0669e)

## (helper) — `person.dc_1e_counted`

- **Authored helper label:** Form 1040 line 1e is more than zero and is counted in this person's earned income
- **Encoded (Bool):** f2441 helper "Form 1040 line 1e (taxable dependent care benefits) is more than zero" = true and helper "Form 1040 line 1e is counted in this person's earned income: the only person whose Forms W-2 show box 10, or, when there is no such single person, the taxpayer" = true
- Interpretation: amb.2025.dc_line1e_attribution
- Expr: `{"all":[{"eq":["f2441.has_1e",{"const":true}],"op":"test"},{"eq":["person.dc_1e_mine",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i2441] p. 4, Lines 4 and 5, "If filing jointly, figure your and your spouse's earned income separately" and "The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z" (2025; sha256 86f0669e)

## (helper) — `person.dc_zero`

- **Authored helper label:** No taxable dependent care benefits counted for this person
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i2441] p. 4, Lines 4 and 5, "If filing jointly, figure your and your spouse's earned income separately" and "The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z" (2025; sha256 86f0669e)

## (helper) — `person.dc_1e`

- **Authored helper label:** This person's share of Form 1040 line 1e (taxable dependent care benefits) in Form 2441 earned income
- **Encoded (NonNegDollars):** Choose — [helper "Form 1040 line 1e is more than zero and is counted in this person's earned income" = true → f1040 line 1e] [helper "Form 1040 line 1e is more than zero and is counted in this person's earned income" = false → helper "No taxable dependent care benefits counted for this person"]
- Interpretation: amb.2025.dc_line1e_attribution
- Expr: `{"alternatives":[{"guard":{"eq":["person.dc_1e_counted",{"const":true}],"op":"test"},"then":"f1040.line1e"},{"guard":{"eq":["person.dc_1e_counted",{"const":false}],"op":"test"},"then":"person.dc_zero"}],"op":"choose"}`
- Cite: [i2441] p. 4, Lines 4 and 5, "If filing jointly, figure your and your spouse's earned income separately" and "The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z" (2025; sha256 86f0669e)

## (helper) — `person.dc_earned`

- **Authored helper label:** This person's earned income for Form 2441 lines 4 and 5: Form W-2 box 1, the person's share of line 1e, and Schedule SE line 3 less the deduction on Schedule 1 line 15 (or the Schedule C profit or loss when no Schedule SE is filed)
- **Encoded (Dollars):** Add helper "Total W-2 box 1 for this person", helper "This person's share of Form 1040 line 1e (taxable dependent care benefits) in Form 2441 earned income", and helper "Worksheet B, Parts 1 and 2, for this person".
- Interpretation: amb.2025.dc_line1e_attribution
- Expr: `{"of":["person.box1","person.dc_1e","person.eic_se"],"op":"sum"}`
- Cite: [i2441] p. 4, Lines 4 and 5, "The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z" and "The amount shown on Schedule SE (Form 1040), line 3, minus any deduction you claim on Schedule 1 (Form 1040), line 15"; p503 p. 11, Self-employment earnings, "Include your self-employment earnings in earned income, even if they are less than $400 and you didn't file Schedule SE (Form 1040)" (2025; sha256 86f0669e)

## (helper) — `person.dc_earned_b`

- **Authored helper label:** This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5, without the dependent care benefits of line 12 (so without line 1e)
- **Encoded (Dollars):** Add helper "Total W-2 box 1 for this person" and helper "Worksheet B, Parts 1 and 2, for this person".
- Expr: `{"of":["person.box1","person.eic_se"],"op":"sum"}`
- Cite: [i2441] p. 5, Line 18, "Earned income for figuring the amount of dependent care benefits you are able to exclude or deduct from your income is determined in the same way as earned income for figuring the credit is determined" and "for purposes of lines 18 and 19, earned income doesn’t include any dependent care benefits shown on line 12" (2025; sha256 86f0669e)

## (helper) — `person.sav_born`

- **Authored helper label:** Were you born before January 2, 2008?
- **Encoded (Bool):** Input — Were you born before January 2, 2008?
- Expr: `{"op":"input","source":"Were you born before January 2, 2008?"}`
- Cite: [f8880] p. 2, Who Can Take This Credit, "The person(s) who made the qualified contribution or elective deferral (a) was born after January 1, 2008" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_student`

- **Authored helper label:** Were you a student in 2025 (during any part of 5 calendar months, enrolled as a full-time student at a school, or taking a full-time, on-farm training course given by a school or a state, county, or local government agency)?
- **Encoded (Bool):** Input — Were you a student in 2025: during any part of 5 calendar months of 2025, were you enrolled as a full-time student at a school, or did you take a full-time, on-farm training course given by a school or a state, county, or local government agency? (A school includes technical, trade, and mechanical schools. It does not include on-the-job training courses, correspondence schools, or schools offering courses only through the Internet.)
- Expr: `{"op":"input","source":"Were you a student in 2025: during any part of 5 calendar months of 2025, were you enrolled as a full-time student at a school, or did you take a full-time, on-farm training course given by a school or a state, county, or local government agency? (A school includes technical, trade, and mechanical schools. It does not include on-the-job training courses, correspondence schools, or schools offering courses only through the Internet.)"}`
- Cite: [f8880] p. 2, Who Can Take This Credit, "You were a student if during any part of 5 calendar months of 2025 you: • Were enrolled as a full-time student at a school; or • Took a full-time, on-farm training course given by a school or a state, county, or local government agency" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_claimed`

- **Authored helper label:** Are you claimed as a dependent on someone else's 2025 tax return?
- **Encoded (Bool):** Input — Are you claimed as a dependent on someone else's 2025 tax return?
- Expr: `{"op":"input","source":"Are you claimed as a dependent on someone else's 2025 tax return?"}`
- Cite: [f8880] p. 2, Who Can Take This Credit, "(b) is claimed as a dependent on someone else’s 2025 tax return" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_ineligible`

- **Authored helper label:** Born after January 1, 2008, claimed as a dependent on someone else's 2025 return, or a student (the dependent question is asked only if someone can claim you or your spouse as a dependent)
- **Encoded (Bool):** (helper "Were you born before January 2, 2008?" = false or helper "Were you a student in 2025 (during any part of 5 calendar months, enrolled as a full-time student at a school, or taking a full-time, on-farm training course given by a school or a state, county, or local government agency)?" = true or sa helper "Can someone claim you or your spouse as a dependent for 2025, or are you a dual-status alien? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)" = true and helper "Are you claimed as a dependent on someone else's 2025 tax return?" = true)
- Expr: `{"any":[{"eq":["person.sav_born",{"const":false}],"op":"test"},{"eq":["person.sav_student",{"const":true}],"op":"test"},{"all":[{"eq":["sa.dependent",{"const":true}],"op":"test"},{"eq":["person.sav_claimed",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [f8880] p. 2, Who Can Take This Credit, "The person(s) who made the qualified contribution or elective deferral (a) was born after January 1, 2008; (b) is claimed as a dependent on someone else’s 2025 tax return; or (c) was a student" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_trad`

- **Authored helper label:** Did you make contributions (other than rollover contributions) to a traditional IRA for 2025?
- **Encoded (Bool):** Input — Did you make contributions (other than rollover contributions) to a traditional IRA for 2025, deductible or not, including contributions made by the due date of your 2025 return for 2025?
- Expr: `{"op":"input","source":"Did you make contributions (other than rollover contributions) to a traditional IRA for 2025, deductible or not, including contributions made by the due date of your 2025 return for 2025?"}`
- Cite: [f8880] Form 8880 (2025), line 1, "Traditional and Roth IRA contributions"; i1040gi p. 95, Line 20, "If you made any nondeductible contributions to a traditional" (2025; created 2025-11-04; sha256 ba2b2877)

## (screen) — `person.sav_able`

- **Authored helper label:** As the designated beneficiary of an ABLE account, did you contribute to it for 2025, or did you receive a distribution from an ABLE account after 2022 (through the due date of your 2025 return)?
- **Encoded (Bool):** Input — As the designated beneficiary of an ABLE account, did you contribute to it for 2025, or did you receive any distribution from an ABLE account after 2022 and before the due date of your 2025 return (including extensions)?
- Expr: `{"op":"input","source":"As the designated beneficiary of an ABLE account, did you contribute to it for 2025, or did you receive any distribution from an ABLE account after 2022 and before the due date of your 2025 return (including extensions)?"}`
- Cite: [f8880] Form 8880 (2025), line 1, "ABLE account contributions by the designated beneficiary"; p. 2, Line 4, "Traditional or Roth IRAs, or ABLE accounts" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_roth`

- **Authored helper label:** Your contributions to a Roth IRA for 2025 (not rollovers or conversions)
- **Encoded (NonNegDollars):** Input — Your contributions to a Roth IRA for 2025, including contributions made by the due date of your 2025 return that are for 2025; do not include rollover contributions or conversions; zero if none
- Expr: `{"op":"input","source":"Your contributions to a Roth IRA for 2025, including contributions made by the due date of your 2025 return that are for 2025; do not include rollover contributions or conversions; zero if none"}`
- Cite: [f8880] Form 8880 (2025), line 1, "Do not include rollover contributions"; p. 2, Who Can Take This Credit, "(a) contributions (other than rollover contributions) to a traditional or Roth IRA" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_line1`

- **Authored helper label:** Form 8880 line 1 for this person (traditional IRA contributions for 2025, deductible or not, and Roth IRA contributions for 2025)
- **Encoded (NonNegDollars):** Add helper "This person's traditional IRA contributions for 2025 (zero if the traditional IRA question was answered No)" and helper "Your contributions to a Roth IRA for 2025 (not rollovers or conversions)".
- **Refusal:** when person.ira_excess_gate is true, cannot complete Excess or recharacterized IRA contributions (Form 5329 Parts III and IV, Pub. 590-A). Traditional or Roth IRA contributions for 2025 that are more than allowed or were recharacterized, and an excess contribution from an earlier year still in an IRA, are outside this tool. Cite: [p590a] p. 35, Excess Contributions, "Generally, an excess contribution is the amount contributed to your traditional IRAs for the year that is more than the smaller of" (2025; sha256 ca0e4287)
- **Refusal:** when person.sav_able is true, cannot complete ABLE account contributions or distributions on Form 8880 (Pub. 907). Contributions to an ABLE account by its designated beneficiary (line 1) and ABLE distributions (line 4) are outside this tool. Cite: [f8880] p. 2, What’s New, "See Pub. 907, Tax Highlights for Persons With Disabilities, for more information about ABLE accounts" (2025; created 2025-11-04; sha256 ba2b2877)
- Interpretation: amb.2025.savers_traditional
- Expr: `{"of":["person.ira_contrib","person.sav_roth"],"op":"sum"}`
- Cite: [f8880] Form 8880 (2025), line 1, "Traditional and Roth IRA contributions"; p. 2, Who Can Take This Credit, "(a) contributions (other than rollover contributions) to a traditional or Roth IRA" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_w2`

- **Authored helper label:** Elective deferrals and designated Roth contributions for 2025 from this person's Forms W-2, box 12
- **Encoded (NonNegDollars):** Add w2.sav_deferral over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"w2","field":"w2.sav_deferral","op":"sum_over"}`
- Cite: [f8880] p. 2, Line 2, "These amounts may be shown in box 12 of your Form(s) W-2 for 2025" (2025; created 2025-11-04; sha256 ba2b2877)

## (screen) — `person.sav_excess`

- **Authored helper label:** Were your elective deferrals and designated Roth contributions for 2025 more than the limit for your plans?
- **Encoded (Bool):** Input — Is the total of your elective deferrals and designated Roth contributions for 2025 (Form W-2 box 12, from all your employers) more than the limit that applies to you (for a 401(k) plan, $23,500 plus any catch-up contributions your plan allows), so that you have excess deferrals?
- Expr: `{"op":"input","source":"Is the total of your elective deferrals and designated Roth contributions for 2025 (Form W-2 box 12, from all your employers) more than the limit that applies to you (for a 401(k) plan, $23,500 plus any catch-up contributions your plan allows), so that you have excess deferrals?"}`
- Cite: [iw2w3] p. 20, Box 12—Codes, "Even though the 2025 limit for elective deferrals and designated Roth contributions is $23,500, Alex's total elective deferral amount of $26,500 is reported in box 12 with code D" (2025; printed date 2025-02-19; sha256 bfecbc99)

## (gate) — `person.sav_excess_gate`

- **Authored helper label:** Elective deferrals in box 12 over the limit for 2025
- **Encoded (Bool):** helper "Elective deferrals and designated Roth contributions for 2025 from this person's Forms W-2, box 12" > $0 (sales.zero) and column (screen) (person.sav_excess) = true
- Expr: `{"all":[{"gt":["person.sav_w2",{"param":"sales.zero"}],"op":"test"},{"eq":["person.sav_excess",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [iw2w3] p. 20, Box 12—Codes, "Even though the 2025 limit for elective deferrals and designated Roth contributions is $23,500, Alex's total elective deferral amount of $26,500 is reported in box 12 with code D" (2025; printed date 2025-02-19; sha256 bfecbc99)

## (helper) — `person.sav_voluntary`

- **Authored helper label:** Voluntary employee contributions for 2025 to a qualified retirement plan (after-tax, not designated Roth)
- **Encoded (NonNegDollars):** Input — Voluntary after-tax employee contributions you made for 2025 to a qualified retirement plan (including the federal Thrift Savings Plan), which may be shown in box 14 of your Form W-2; not designated Roth contributions, and not contributions designated under section 414(h)(2) (treated as employer contributions); zero if none
- Expr: `{"op":"input","source":"Voluntary after-tax employee contributions you made for 2025 to a qualified retirement plan (including the federal Thrift Savings Plan), which may be shown in box 14 of your Form W-2; not designated Roth contributions, and not contributions designated under section 414(h)(2) (treated as employer contributions); zero if none"}`
- Cite: [f8880] p. 2, Line 2, "Voluntary employee contributions to a qualified retirement plan, as defined in section 4974(c) (including the federal TSP)"; "Contributions designated under section 414(h)(2) are treated as employer contributions" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_simple_plan`

- **Authored helper label:** This self-employed person's own SIMPLE IRA salary reduction contributions, by plan
- **Encoded (NonNegDollars):** Choose — [helper "Retirement plan of this self-employed person" = 'none' → line zero] [helper "Retirement plan of this self-employed person" = 'sep' → line zero] [helper "Retirement plan of this self-employed person" = 'simple' → helper "Salary reduction contributions for yourself to your SIMPLE IRA (including catch-up)"]
- Interpretation: amb.2025.savers_sep_contrib
- Expr: `{"alternatives":[{"guard":{"eq":["person.plan",{"const":"none"}],"op":"test"},"then":"person.zero"},{"guard":{"eq":["person.plan",{"const":"sep"}],"op":"test"},"then":"person.zero"},{"guard":{"eq":["person.plan",{"const":"simple"}],"op":"test"},"then":"person.simple_deferral"}],"op":"choose"}`
- Cite: [f8880] p. 2, Line 2, "Elective deferrals (including designated Roth contributions under section 402A, if applicable) to a 401(k), 403(b), governmental 457(b), SEP, SIMPLE, or the federal TSP" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_simple`

- **Authored helper label:** This person's own SIMPLE IRA salary reduction contributions as a self-employed person
- **Encoded (NonNegDollars):** Choose — [helper "This person has at least one Schedule C" = true → helper "This self-employed person's own SIMPLE IRA salary reduction contributions, by plan"] [helper "This person has at least one Schedule C" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":"person.sav_simple_plan"},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f8880] p. 2, Line 2, "Elective deferrals (including designated Roth contributions under section 402A, if applicable) to a 401(k), 403(b), governmental 457(b), SEP, SIMPLE, or the federal TSP" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_line2`

- **Authored helper label:** Form 8880 line 2 for this person (box 12 deferrals, voluntary contributions and own SIMPLE salary reduction contributions)
- **Encoded (NonNegDollars):** Add helper "Elective deferrals and designated Roth contributions for 2025 from this person's Forms W-2, box 12", helper "Voluntary employee contributions for 2025 to a qualified retirement plan (after-tax, not designated Roth)", and helper "This person's own SIMPLE IRA salary reduction contributions as a self-employed person".
- **Refusal:** when person.sav_excess_gate is true, cannot complete Excess elective deferrals on Form 8880 line 2. Elective deferrals over the limit for the year, and their later distribution, are outside this tool. Cite: [iw2w3] p. 20, Box 12—Codes, "Even though the 2025 limit for elective deferrals and designated Roth contributions is $23,500" (2025; printed date 2025-02-19; sha256 bfecbc99)
- Expr: `{"of":["person.sav_w2","person.sav_voluntary","person.sav_simple"],"op":"sum"}`
- Cite: [f8880] Form 8880 (2025), line 2, "Elective deferrals to a 401(k) or other qualified employer plan, voluntary employee contributions, and 501(c)(18)(D) plan contributions for 2025"; p. 2, Line 2, "Include on line 2 any of the following amounts" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_prior_joint`

- **Authored helper label:** Your distributions in 2023 and 2024 from years for which you and your spouse filed a joint return, and in 2026 before the due date of your 2025 return (a joint return only)
- **Encoded (NonNegDollars):** Input — On a joint return: the distributions you received in 2023 and 2024 in a year for which you and your spouse filed a joint return, plus those you receive in 2026 before the due date of your 2025 return (including extensions), from a traditional or Roth IRA; a 401(k), 403(b), governmental 457(b), 501(c)(18)(D), SEP or SIMPLE plan, or the federal TSP; or another qualified retirement plan. Do not include rollovers or trustee-to-trustee transfers, in-plan Roth rollovers, amounts rolled over or converted to a Roth IRA, plan loans treated as distributions, distributions of excess contributions or deferrals, IRA contributions returned by the due date, section 404(k) dividends, distributions from a military retirement plan (other than the TSP), or distributions from an inherited IRA as a nonspouse beneficiary; zero if none
- **Refusal:** when person.sav_able is true, cannot complete ABLE account contributions or distributions on Form 8880 (Pub. 907). Contributions to an ABLE account by its designated beneficiary (line 1) and ABLE distributions (line 4) are outside this tool. Cite: [f8880] p. 2, What’s New, "See Pub. 907, Tax Highlights for Persons With Disabilities, for more information about ABLE accounts" (2025; created 2025-11-04; sha256 ba2b2877)
- Interpretation: amb.2025.savers_2026_joint
- Expr: `{"op":"input","source":"On a joint return: the distributions you received in 2023 and 2024 in a year for which you and your spouse filed a joint return, plus those you receive in 2026 before the due date of your 2025 return (including extensions), from a traditional or Roth IRA; a 401(k), 403(b), governmental 457(b), 501(c)(18)(D), SEP or SIMPLE plan, or the federal TSP; or another qualified retirement plan. Do not include rollovers or trustee-to-trustee transfers, in-plan Roth rollovers, amounts rolled over or converted to a Roth IRA, plan loans treated as distributions, distributions of excess contributions or deferrals, IRA contributions returned by the due date, section 404(k) dividends, distributions from a military retirement plan (other than the TSP), or distributions from an inherited IRA as a nonspouse beneficiary; zero if none"}`
- Cite: [f8880] p. 2, Line 4, "If you’re filing a joint return, include both spouses’ amounts in both columns. Exception. Don’t include your spouse’s distributions with yours when entering an amount on line 4 if you and your spouse didn’t file a joint return for the year the distribution was received" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_prior_other`

- **Authored helper label:** Your distributions in 2023 and 2024 from years for which you did not file a joint return with your spouse on this return (on a return that is not joint, all of your 2023, 2024 and early-2026 distributions)
- **Encoded (NonNegDollars):** Input — The distributions you received in 2023 and 2024 in a year for which you did not file a joint return with your spouse on this return (on a return that is not a joint return: all your distributions in 2023 and 2024, and in 2026 before the due date of your 2025 return, including extensions), from a traditional or Roth IRA; a 401(k), 403(b), governmental 457(b), 501(c)(18)(D), SEP or SIMPLE plan, or the federal TSP; or another qualified retirement plan. Do not include rollovers or trustee-to-trustee transfers, in-plan Roth rollovers, amounts rolled over or converted to a Roth IRA, plan loans treated as distributions, distributions of excess contributions or deferrals, IRA contributions returned by the due date, section 404(k) dividends, distributions from a military retirement plan (other than the TSP), or distributions from an inherited IRA as a nonspouse beneficiary; zero if none
- **Refusal:** when person.sav_able is true, cannot complete ABLE account contributions or distributions on Form 8880 (Pub. 907). Contributions to an ABLE account by its designated beneficiary (line 1) and ABLE distributions (line 4) are outside this tool. Cite: [f8880] p. 2, What’s New, "See Pub. 907, Tax Highlights for Persons With Disabilities, for more information about ABLE accounts" (2025; created 2025-11-04; sha256 ba2b2877)
- Expr: `{"op":"input","source":"The distributions you received in 2023 and 2024 in a year for which you did not file a joint return with your spouse on this return (on a return that is not a joint return: all your distributions in 2023 and 2024, and in 2026 before the due date of your 2025 return, including extensions), from a traditional or Roth IRA; a 401(k), 403(b), governmental 457(b), 501(c)(18)(D), SEP or SIMPLE plan, or the federal TSP; or another qualified retirement plan. Do not include rollovers or trustee-to-trustee transfers, in-plan Roth rollovers, amounts rolled over or converted to a Roth IRA, plan loans treated as distributions, distributions of excess contributions or deferrals, IRA contributions returned by the due date, section 404(k) dividends, distributions from a military retirement plan (other than the TSP), or distributions from an inherited IRA as a nonspouse beneficiary; zero if none"}`
- Cite: [f8880] p. 2, Line 4, "Enter the total amount of distributions you, and your spouse if filing jointly, received after 2022 and before the due date of your 2025 return (including extensions)"; "Exception. Don’t include your spouse’s distributions with yours when entering an amount on line 4 if you and your spouse didn’t file a joint return for the year the distribution was received" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.ira_trad`

- **Authored helper label:** Your traditional IRA contributions for 2025 (not rollovers)
- **Encoded (NonNegDollars):** Input — Your contributions to your traditional IRAs for 2025, made in 2025 or made by April 15, 2026, and designated for 2025; do not include rollover contributions, contributions made in 2025 that you deducted for 2024, contributions withdrawn (with their earnings) by the due date of your return, trustees' fees billed separately, or employer contributions to a SEP or SIMPLE IRA
- Expr: `{"op":"input","source":"Your contributions to your traditional IRAs for 2025, made in 2025 or made by April 15, 2026, and designated for 2025; do not include rollover contributions, contributions made in 2025 that you deducted for 2024, contributions withdrawn (with their earnings) by the due date of your return, trustees' fees billed separately, or employer contributions to a SEP or SIMPLE IRA"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 11, "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions (April 15, 2026, for most people), for 2025"; p. 95, Line 20, "If you made contributions to your IRA in 2025 that you deducted for 2024, don’t include them in the worksheet", "Don’t include rollover contributions in figuring your deduction" and "Don’t include trustees’ fees that were billed separately" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_contrib`

- **Authored helper label:** This person's traditional IRA contributions for 2025 (zero if the traditional IRA question was answered No)
- **Encoded (NonNegDollars):** Choose — [helper "Did you make contributions (other than rollover contributions) to a traditional IRA for 2025?" = true → helper "Your traditional IRA contributions for 2025 (not rollovers)"] [helper "Did you make contributions (other than rollover contributions) to a traditional IRA for 2025?" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.sav_trad",{"const":true}],"op":"test"},"then":"person.ira_trad"},{"guard":{"eq":["person.sav_trad",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 11, "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions (April 15, 2026, for most people), for 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_has`

- **Authored helper label:** This person made traditional IRA contributions for 2025
- **Encoded (Bool):** helper "This person's traditional IRA contributions for 2025 (zero if the traditional IRA question was answered No)" > $0 (sales.zero)
- Expr: `{"gt":["person.ira_contrib",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 95, Line 20, "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_any_contrib`

- **Authored helper label:** This person made traditional or Roth IRA contributions for 2025
- **Encoded (Bool):** (helper "This person made traditional IRA contributions for 2025" = true or helper "Your contributions to a Roth IRA for 2025 (not rollovers or conversions)" > $0 (sales.zero))
- Expr: `{"any":[{"eq":["person.ira_has",{"const":true}],"op":"test"},{"gt":["person.sav_roth",{"param":"sales.zero"}],"op":"test"}],"op":"test"}`
- Cite: [f8880] Form 8880 (2025), line 1, "Traditional and Roth IRA contributions" (2025; created 2025-11-04; sha256 ba2b2877)

## (screen) — `person.ira_excess`

- **Authored helper label:** Were your 2025 IRA contributions more than allowed, recharacterized, or is an earlier excess contribution still in your IRA?
- **Encoded (Bool):** Input — Does any of these apply to you: your contributions for 2025 to traditional and Roth IRAs together were more than you were allowed to contribute (more than $7,000, or $8,000 if age 50 or older at the end of 2025, or more than your taxable compensation, or a Roth contribution above the limit for your income), and the excess was not withdrawn with its earnings by the due date of your return; you recharacterized a 2025 contribution (moved it from a traditional to a Roth IRA or the reverse); or an excess contribution from an earlier year is still in your traditional or Roth IRA?
- Expr: `{"op":"input","source":"Does any of these apply to you: your contributions for 2025 to traditional and Roth IRAs together were more than you were allowed to contribute (more than $7,000, or $8,000 if age 50 or older at the end of 2025, or more than your taxable compensation, or a Roth contribution above the limit for your income), and the excess was not withdrawn with its earnings by the due date of your return; you recharacterized a 2025 contribution (moved it from a traditional to a Roth IRA or the reverse); or an excess contribution from an earlier year is still in your traditional or Roth IRA?"}`
- Cite: [p590a] p. 35, Excess Contributions, "Generally, an excess contribution is the amount contributed to your traditional IRAs for the year that is more than the smaller of"; p. 30, "Recharacterizing excess contributions"; i1040gi p. 95, Line 20, "If the total of your IRA deduction on line 20 plus any nondeductible contributions to your traditional IRAs shown on Form 8606 is less than your total traditional IRA contributions for 2025, see Pub. 590-A for special rules" (2025; sha256 ca0e4287)

## (gate) — `person.ira_excess_gate`

- **Authored helper label:** This person's IRA contributions for 2025 are excess or recharacterized, or an earlier excess remains (screen)
- **Encoded (Bool):** helper "This person made traditional or Roth IRA contributions for 2025" = true and column (screen) (person.ira_excess) = true
- Expr: `{"all":[{"eq":["person.ira_any_contrib",{"const":true}],"op":"test"},{"eq":["person.ira_excess",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [p590a] p. 35, Excess Contributions, "In general, if the excess contributions for a year aren’t withdrawn by the date your return for the year is due (including extensions), you are subject to a 6% tax" (2025; sha256 ca0e4287)

## (helper) — `person.ira_age50`

- **Authored helper label:** Were you age 50 or older at the end of 2025?
- **Encoded (Bool):** Input — Were you age 50 or older at the end of 2025?
- Interpretation: amb.2025.ira_age50
- Expr: `{"op":"input","source":"Were you age 50 or older at the end of 2025?"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "$8,000 if age 50 or older at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_work_plan`

- **Authored helper label:** Were you covered by a retirement plan at work in 2025?
- **Encoded (Bool):** Input — Were you covered by a retirement plan at work for 2025 (a qualified pension, profit-sharing or 401(k), annuity, SEP, SIMPLE or other employer plan), even if you were not vested in it?
- Interpretation: amb.2025.ira_covered
- Expr: `{"op":"input","source":"Were you covered by a retirement plan at work for 2025 (a qualified pension, profit-sharing or 401(k), annuity, SEP, SIMPLE or other employer plan), even if you were not vested in it?"}`
- Cite: [i1040gi] p. 96, Were You Covered by a Retirement Plan?, "profit-sharing (including 401(k)), annuity, SEP, SIMPLE, etc.) at work or through self-employment" and "The “Retirement plan” box in box 13 of your Form W-2 should be checked if you were covered by a plan at work even if you weren’t vested in the plan" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_se_plan`

- **Authored helper label:** This person contributed for themselves to a SEP or SIMPLE IRA as a self-employed person (person.plan)
- **Encoded (Bool):** helper "This person has at least one Schedule C" = true and not helper "Retirement plan of this self-employed person" = 'none'
- Interpretation: amb.2025.ira_covered
- Expr: `{"all":[{"eq":["person.has_sc",{"const":true}],"op":"test"},{"not":{"eq":["person.plan",{"const":"none"}],"op":"test"},"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 96, Were You Covered by a Retirement Plan?, "You are also covered by a plan if you were self-employed and had a SEP, SIMPLE, or qualified retirement plan" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_cov`

- **Authored helper label:** Covered by a retirement plan (worksheet line 1a or 1b for this person)
- **Encoded (Bool):** (helper "Were you covered by a retirement plan at work in 2025?" = true or helper "This person contributed for themselves to a SEP or SIMPLE IRA as a self-employed person (person.plan)" = true)
- Interpretation: amb.2025.ira_covered
- Expr: `{"any":[{"eq":["person.ira_work_plan",{"const":true}],"op":"test"},{"eq":["person.ira_se_plan",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 1, "Were you covered by a retirement plan (see Were You Covered by a Retirement Plan)?" and "If married filing jointly, was your spouse covered by a retirement plan?" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_limit_under50`

- **Authored helper label:** $7,000
- **Encoded (NonNegDollars):** Enter $7,000 (ira.limit).
- Expr: `{"op":"param","ref":"ira.limit"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "$7,000 if under age 50 at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_limit_over50`

- **Authored helper label:** $8,000
- **Encoded (NonNegDollars):** Enter $8,000 (ira.limit_50).
- Expr: `{"op":"param","ref":"ira.limit_50"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "$8,000 if age 50 or older at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_limit`

- **Authored helper label:** The applicable amount for this person ($7,000 if under age 50 at the end of 2025; $8,000 if age 50 or older)
- **Encoded (NonNegDollars):** Choose — [helper "Were you age 50 or older at the end of 2025?" = true → helper "$8,000"] [helper "Were you age 50 or older at the end of 2025?" = false → helper "$7,000"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_age50",{"const":true}],"op":"test"},"then":"person.ira_limit_over50"},{"guard":{"eq":["person.ira_age50",{"const":false}],"op":"test"},"then":"person.ira_limit_under50"}],"op":"choose"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "$7,000 if under age 50 at the end of 2025" and "$8,000 if age 50 or older at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_not_covered_joint`

- **Authored helper label:** Married filing jointly and this person was not covered by a retirement plan
- **Encoded (Bool):** ira helper "Married filing jointly" = true and helper "Covered by a retirement plan (worksheet line 1a or 1b for this person)" = false
- Expr: `{"all":[{"eq":["ira.joint",{"const":true}],"op":"test"},{"eq":["person.ira_cov",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 2, "But if you checked “No” on either line 1a or 1b, enter $246,000 for the person who wasn’t covered by a plan" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_line2_status`

- **Authored helper label:** The line 2 amount for the filing status ($89,000; $146,000 if married filing jointly or qualifying surviving spouse)
- **Encoded (NonNegDollars):** Enter single $89,000; mfj $146,000; mfs $10,000; hoh $89,000; qss $146,000 (ira.line2).
- Expr: `{"op":"param","ref":"ira.line2"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 2, "Enter the amount shown below that applies to you" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_line2_nc`

- **Authored helper label:** $246,000
- **Encoded (NonNegDollars):** Enter $246,000 (ira.line2_not_covered).
- Expr: `{"op":"param","ref":"ira.line2_not_covered"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 2, "enter $246,000 for the person who wasn’t covered by a plan" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_line2`

- **Authored helper label:** Worksheet line 2 for this person's column
- **Encoded (NonNegDollars):** Choose — [helper "Married filing jointly and this person was not covered by a retirement plan" = true → helper "$246,000"] [helper "Married filing jointly and this person was not covered by a retirement plan" = false → helper "The line 2 amount for the filing status ($89,000; $146,000 if married filing jointly or qualifying surviving spouse)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_not_covered_joint",{"const":true}],"op":"test"},"then":"person.ira_line2_nc"},{"guard":{"eq":["person.ira_not_covered_joint",{"const":false}],"op":"test"},"then":"person.ira_line2_status"}],"op":"choose"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 2, "Married filing jointly, enter $146,000 in both columns. But if you checked “No” on either line 1a or 1b, enter $246,000 for the person who wasn’t covered by a plan" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_line6`

- **Authored helper label:** Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, subtract line 5 from line 2 (if no, zero: none of the contributions are deductible)
- **Encoded (NonNegDollars):** Subtract ira line 5 from helper "Worksheet line 2 for this person's column". If zero or less, enter -0-.
- Expr: `{"from":"person.ira_line2","op":"subtract_floor0","take":"ira.line5"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "Is the amount on line 5 less than the amount on line 2?", "None of your IRA contributions are deductible" and "Subtract line 5 from line 2 in each column" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_line6_yes`

- **Authored helper label:** Line 5 is less than line 2 in this person's column (line 6, Yes)
- **Encoded (Bool):** helper "Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, subtract line 5 from line 2 (if no, zero: none of the contributions are deductible)" > $0 (sales.zero)
- Expr: `{"gt":["person.ira_line6",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "Is the amount on line 5 less than the amount on line 2?" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_wide`

- **Authored helper label:** This column takes the single rule (70% or 80%, the $10,000 threshold) — not married filing jointly or qualifying surviving spouse, or the column of a person who wasn't covered by a retirement plan
- **Encoded (Bool):** (ira helper "Married filing jointly or qualifying surviving spouse" = false or helper "Covered by a retirement plan (worksheet line 1a or 1b for this person)" = false)
- Expr: `{"any":[{"eq":["ira.joint_type",{"const":false}],"op":"test"},{"eq":["person.ira_cov",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "($10,000 or more in the column for the IRA of a person who wasn’t covered by a retirement plan)"; p. 98, IRA Deduction Worksheet—Continued, line 7, "then in the column for the IRA of the person who wasn’t covered by a retirement plan, multiply by 70% (0.70)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_full_narrow`

- **Authored helper label:** $10,000
- **Encoded (NonNegDollars):** Enter $10,000 (ira.full_narrow).
- Expr: `{"op":"param","ref":"ira.full_narrow"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "and the result is $10,000 or more" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_full_joint`

- **Authored helper label:** $20,000
- **Encoded (NonNegDollars):** Enter $20,000 (ira.full_joint).
- Expr: `{"op":"param","ref":"ira.full_joint"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "and the result is $20,000 or more" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_full`

- **Authored helper label:** The line 6 result at or above which this column takes the applicable amount ($10,000 or $20,000)
- **Encoded (NonNegDollars):** Choose — [helper "This column takes the single rule (70% or 80%, the $10,000 threshold) — not married filing jointly or qualifying surviving spouse, or the column of a person who wasn't covered by a retirement plan" = true → helper "$10,000"] [helper "This column takes the single rule (70% or 80%, the $10,000 threshold) — not married filing jointly or qualifying surviving spouse, or the column of a person who wasn't covered by a retirement plan" = false → helper "$20,000"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_wide",{"const":true}],"op":"test"},"then":"person.ira_full_narrow"},{"guard":{"eq":["person.ira_wide",{"const":false}],"op":"test"},"then":"person.ira_full_joint"}],"op":"choose"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "If single, head of household, or married filing separately, and the result is $10,000 or more" and "If married filing jointly or qualifying surviving spouse, and the result is $20,000 or more ($10,000 or more in the column for the IRA of a person who wasn’t covered by a retirement plan)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_at_full`

- **Authored helper label:** The line 6 result is at or above the threshold (enter the applicable amount on line 7)
- **Encoded (Bool):** helper "Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, subtract line 5 from line 2 (if no, zero: none of the contributions are deductible)" ≥ helper "The line 6 result at or above which this column takes the applicable amount ($10,000 or $20,000)"
- Expr: `{"ge":["person.ira_line6","person.ira_full"],"op":"test"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "enter the applicable amount below on line 7 for that column and go to line 8" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_p70`

- **Authored helper label:** Line 6 multiplied by 70% (0.70)
- **Encoded (NonNegDollars):** Multiply helper "Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, subtract line 5 from line 2 (if no, zero: none of the contributions are deductible)" by 70% (0.70) (ira.rate_70).
- Expr: `{"amount":"person.ira_line6","op":"multiply_rate","rate":{"param":"ira.rate_70"}}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "multiply by 70% (0.70)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_p80`

- **Authored helper label:** Line 6 multiplied by 80% (0.80)
- **Encoded (NonNegDollars):** Multiply helper "Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, subtract line 5 from line 2 (if no, zero: none of the contributions are deductible)" by 80% (0.80) (ira.rate_80).
- Expr: `{"amount":"person.ira_line6","op":"multiply_rate","rate":{"param":"ira.rate_80"}}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "or by 80% (0.80)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_p35`

- **Authored helper label:** Line 6 multiplied by 35% (0.35)
- **Encoded (NonNegDollars):** Multiply helper "Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, subtract line 5 from line 2 (if no, zero: none of the contributions are deductible)" by 35% (0.35) (ira.rate_35).
- Expr: `{"amount":"person.ira_line6","op":"multiply_rate","rate":{"param":"ira.rate_35"}}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "multiply by 35% (0.35)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_p40`

- **Authored helper label:** Line 6 multiplied by 40% (0.40)
- **Encoded (NonNegDollars):** Multiply helper "Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, subtract line 5 from line 2 (if no, zero: none of the contributions are deductible)" by 40% (0.40) (ira.rate_40).
- Expr: `{"amount":"person.ira_line6","op":"multiply_rate","rate":{"param":"ira.rate_40"}}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "or by 40% (0.40)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_prod_wide`

- **Authored helper label:** Line 6 multiplied by 70% (0.70), or by 80% (0.80) for a person age 50 or older at the end of 2025
- **Encoded (NonNegDollars):** Choose — [helper "Were you age 50 or older at the end of 2025?" = true → helper "Line 6 multiplied by 80% (0.80)"] [helper "Were you age 50 or older at the end of 2025?" = false → helper "Line 6 multiplied by 70% (0.70)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_age50",{"const":true}],"op":"test"},"then":"person.ira_p80"},{"guard":{"eq":["person.ira_age50",{"const":false}],"op":"test"},"then":"person.ira_p70"}],"op":"choose"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "Single, head of household, or married filing separately, multiply by 70% (0.70) (or by 80% (0.80) in the column for the IRA of a person who is age 50 or older at the end of 2025)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_prod_joint`

- **Authored helper label:** Line 6 multiplied by 35% (0.35), or by 40% (0.40) for a person age 50 or older at the end of 2025
- **Encoded (NonNegDollars):** Choose — [helper "Were you age 50 or older at the end of 2025?" = true → helper "Line 6 multiplied by 40% (0.40)"] [helper "Were you age 50 or older at the end of 2025?" = false → helper "Line 6 multiplied by 35% (0.35)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_age50",{"const":true}],"op":"test"},"then":"person.ira_p40"},{"guard":{"eq":["person.ira_age50",{"const":false}],"op":"test"},"then":"person.ira_p35"}],"op":"choose"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "Married filing jointly or qualifying surviving spouse, multiply by 35% (0.35) (or by 40% (0.40) in the column for the IRA of a person who is age 50 or older at the end of 2025)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_prod`

- **Authored helper label:** Line 6 multiplied by the percentage that applies to this column
- **Encoded (NonNegDollars):** Choose — [helper "This column takes the single rule (70% or 80%, the $10,000 threshold) — not married filing jointly or qualifying surviving spouse, or the column of a person who wasn't covered by a retirement plan" = true → helper "Line 6 multiplied by 70% (0.70), or by 80% (0.80) for a person age 50 or older at the end of 2025"] [helper "This column takes the single rule (70% or 80%, the $10,000 threshold) — not married filing jointly or qualifying surviving spouse, or the column of a person who wasn't covered by a retirement plan" = false → helper "Line 6 multiplied by 35% (0.35), or by 40% (0.40) for a person age 50 or older at the end of 2025"]
- Interpretation: amb.2025.ira_line7_cents
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_wide",{"const":true}],"op":"test"},"then":"person.ira_prod_wide"},{"guard":{"eq":["person.ira_wide",{"const":false}],"op":"test"},"then":"person.ira_prod_joint"}],"op":"choose"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "Multiply lines 6a and 6b by the percentage below that applies to you" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_rounded`

- **Authored helper label:** If the result isn't a multiple of $10, increase it to the next multiple of $10
- **Encoded (NonNegDollars):** Round helper "Line 6 multiplied by the percentage that applies to this column" up to the next multiple of $10.
- Expr: `{"of":"person.ira_prod","op":"round","rule":"up","unit":1000}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "If the result isn’t a multiple of $10, increase it to the next multiple of $10 (for example, increase $490.30 to $500)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_min`

- **Authored helper label:** $200
- **Encoded (NonNegDollars):** Enter $200 (ira.min).
- Expr: `{"op":"param","ref":"ira.min"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "But if it is less than $200, enter $200" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_floor`

- **Authored helper label:** If the result is $200 or more, enter the result; but if it is less than $200, enter $200
- **Encoded (NonNegDollars):** Enter the larger of helper "If the result isn't a multiple of $10, increase it to the next multiple of $10" or helper "$200".
- Expr: `{"of":["person.ira_rounded","person.ira_min"],"op":"larger_of"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "If the result is $200 or more, enter the result. But if it is less than $200, enter $200" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_below`

- **Authored helper label:** Line 7 when the line 6 result is under the threshold (zero when line 6 is No)
- **Encoded (NonNegDollars):** Choose — [helper "Line 5 is less than line 2 in this person's column (line 6, Yes)" = true → helper "If the result is $200 or more, enter the result; but if it is less than $200, enter $200"] [helper "Line 5 is less than line 2 in this person's column (line 6, Yes)" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_line6_yes",{"const":true}],"op":"test"},"then":"person.ira_floor"},{"guard":{"eq":["person.ira_line6_yes",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "None of your IRA contributions are deductible"; p. 98, IRA Deduction Worksheet—Continued, line 7 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_line7_figured`

- **Authored helper label:** Line 7 when someone is covered by a retirement plan (lines 2 through 6 completed)
- **Encoded (NonNegDollars):** Choose — [helper "The line 6 result is at or above the threshold (enter the applicable amount on line 7)" = true → helper "The applicable amount for this person ($7,000 if under age 50 at the end of 2025; $8,000 if age 50 or older)"] [helper "The line 6 result is at or above the threshold (enter the applicable amount on line 7)" = false → helper "Line 7 when the line 6 result is under the threshold (zero when line 6 is No)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_at_full",{"const":true}],"op":"test"},"then":"person.ira_limit"},{"guard":{"eq":["person.ira_at_full",{"const":false}],"op":"test"},"then":"person.ira_below"}],"op":"choose"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "enter the applicable amount below on line 7 for that column and go to line 8" and "Otherwise, go to line 7" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_line7`

- **Authored helper label:** Worksheet line 7 for this person's column
- **Encoded (NonNegDollars):** Choose — [ira helper "You (or, on a joint return, your spouse) were covered by a retirement plan (Yes on line 1a or 1b)" = true → helper "Line 7 when someone is covered by a retirement plan (lines 2 through 6 completed)"] [ira helper "You (or, on a joint return, your spouse) were covered by a retirement plan (Yes on line 1a or 1b)" = false → helper "The applicable amount for this person ($7,000 if under age 50 at the end of 2025; $8,000 if age 50 or older)"]
- Expr: `{"alternatives":[{"guard":{"eq":["ira.anyone_covered",{"const":true}],"op":"test"},"then":"person.ira_line7_figured"},{"guard":{"eq":["ira.anyone_covered",{"const":false}],"op":"test"},"then":"person.ira_limit"}],"op":"choose"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "If you checked “No” on line 1a (and “No” on line 1b if married filing jointly), skip lines 2 through 6, enter the applicable amount below on line 7a (and line 7b, if applicable), and go to line 8" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `person.ira_over_limit`

- **Authored helper label:** This person's traditional and Roth IRA contributions for 2025 together are more than the applicable amount
- **Encoded (Bool):** helper "This person made traditional IRA contributions for 2025" = true and helper "This person's traditional and Roth IRA contributions for 2025" > helper "The applicable amount for this person ($7,000 if under age 50 at the end of 2025; $8,000 if age 50 or older)"
- Expr: `{"all":[{"eq":["person.ira_has",{"const":true}],"op":"test"},{"gt":["person.ira_own_total","person.ira_limit"],"op":"test"}],"op":"test"}`
- Cite: [p590a] p. 35, Excess Contributions, "Generally, an excess contribution is the amount contributed to your traditional IRAs for the year that is more than the smaller of: • $7,000 ($8,000 if you are age 50 or older), or • Your taxable compensation for the year" (2025; sha256 ca0e4287)

## (helper) — `person.ira_own_total`

- **Authored helper label:** This person's traditional and Roth IRA contributions for 2025
- **Encoded (NonNegDollars):** Add helper "This person's traditional IRA contributions for 2025 (zero if the traditional IRA question was answered No)" and helper "Your contributions to a Roth IRA for 2025 (not rollovers or conversions)".
- Expr: `{"of":["person.ira_contrib","person.sav_roth"],"op":"sum"}`
- Cite: [i8606] p. 5, Overall Contribution Limit for Traditional and Roth IRAs, "your limit on contributions to traditional and Roth IRAs is generally the smaller of $7,000 ($8,000 if age 50 or older at the end of 2025) or your taxable compensation" (2025; sha256 735fb7ae)

## (helper) — `person.ira_line11`

- **Authored helper label:** Worksheet line 11 for this person's column (traditional IRA contributions for 2025)
- **Encoded (NonNegDollars):** Enter the amount from helper "This person's traditional IRA contributions for 2025 (zero if the traditional IRA question was answered No)".
- **Refusal:** when ira.both_kinds is true, cannot complete Traditional and Roth IRA contributions on a joint return (Pub. 590-A). On a joint return where you or your spouse made contributions to both a traditional IRA and a Roth IRA for 2025, the IRA deduction is figured with Pub. 590-A, which this tool does not prepare. Cite: [i1040gi] p. 95, Line 20, "If you are filing a joint return and you or your spouse made contributions to both a traditional IRA and a Roth IRA for 2025, don’t use the IRA Deduction Worksheet in these instructions" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when ira.kbh_short is true, cannot complete IRA deduction on a joint return with little compensation (Pub. 590-A worksheet). On a joint return with line 10 of the IRA Deduction Worksheet under $14,000 ($15,000 or $16,000 with spouses age 50 or older), the IRA deduction is figured with the worksheet in Pub. 590-A, which this tool does not prepare. Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, Caution, "stop here and use the worksheet in Pub. 590-A to figure your IRA deduction" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when person.ira_excess_gate is true, cannot complete Excess or recharacterized IRA contributions (Form 5329 Parts III and IV, Pub. 590-A). Traditional or Roth IRA contributions for 2025 that are more than allowed or were recharacterized, and an excess contribution from an earlier year still in an IRA, are outside this tool. Cite: [i1040gi] p. 95, Line 20, "If the total of your IRA deduction on line 20 plus any nondeductible contributions to your traditional IRAs shown on Form 8606 is less than your total traditional IRA contributions for 2025, see Pub. 590-A for special rules" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when person.ira_over_limit is true, cannot complete Excess IRA contributions (Form 5329 Part III, Pub. 590-A). Your traditional and Roth IRA contributions for 2025 are together more than $7,000 ($8,000 if age 50 or older), an excess contribution, which is outside this tool. Cite: [p590a] p. 35, Excess Contributions, "Generally, an excess contribution is the amount contributed to your traditional IRAs for the year that is more than the smaller of" (2025; sha256 ca0e4287)
- **Refusal:** when ira.over_comp is true, cannot complete Excess IRA contributions (Form 5329 Part III, Pub. 590-A). The traditional and Roth IRA contributions for 2025 on this return are more than the compensation on line 10 of the IRA Deduction Worksheet, an excess contribution, which is outside this tool. Cite: [p590a] p. 35, Excess Contributions, "Your taxable compensation for the year" (2025; sha256 ca0e4287)
- **Refusal:** when ira.special_gate is true, cannot complete IRA deduction special cases (Pub. 590-A). Nonqualified deferred compensation in box 1 (Form W-2 box 11 or code Z, Form 1099-MISC box 15), fellowship or stipend payments not on a Form W-2, repayments of qualified reservist distributions and difficulty of care payments change the IRA compensation or contribution limits; they are outside this tool. Cite: [i1040gi] p. 95, Line 20, "don’t include that income on line 8 of the worksheet" and "Don’t include any repayments of qualified reservist distributions"; p590a p. 6, What Is Compensation?, "certain non-tuition fellowship and stipend payments not reported to you on Form W-2 are treated as taxable compensation for IRA purposes" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when ira.excl_gate is true, cannot complete IRA deduction with excluded foreign or possession income (Pub. 590-A). With a retirement plan coverage and Form 2555 (or excluded income from Form 4563 or Puerto Rico), the IRA deduction is figured with Pub. 590-A, which this tool does not prepare. Cite: [i1040gi] p. 96, Were You Covered by a Retirement Plan?, "If you were covered by a retirement plan and you file Form 2555 or 8815, or you exclude employer-provided adoption benefits, see Pub. 590-A to figure the amount, if any, of your IRA deduction" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when ira.combat_gate is true, cannot complete Nontaxable combat pay in IRA compensation (IRA Deduction Worksheet, line 8). Nontaxable combat pay counts as compensation for the IRA deduction; it is outside this tool. Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 8, "Nontaxable combat pay. This amount should be reported in box 12 of Form W-2 with code Q or reported on Form 1040, line 1i" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"from":"person.ira_contrib","op":"copy"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 11, "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions (April 15, 2026, for most people), for 2025 to your IRA on line 11a and to your spouse’s IRA on line 11b" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_7or10`

- **Authored helper label:** The smaller of line 7 for this column and line 10
- **Encoded (NonNegDollars):** Enter the smaller of helper "Worksheet line 7 for this person's column" or ira line 10.
- Expr: `{"of":["person.ira_line7","ira.line10"],"op":"smaller_of"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 12, "On line 12a, enter the smallest of line 7a, 10, or 11a" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_line12`

- **Authored helper label:** Worksheet line 12 for this person's column (the smallest of line 7, 10 or 11). This is the most you can deduct
- **Encoded (NonNegDollars):** Enter the smaller of helper "The smaller of line 7 for this column and line 10" or helper "Worksheet line 11 for this person's column (traditional IRA contributions for 2025)".
- Interpretation: amb.2025.ira_deduct_less
- Expr: `{"of":["person.ira_7or10","person.ira_line11"],"op":"smaller_of"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 12, "On line 12a, enter the smallest of line 7a, 10, or 11a. On line 12b, enter the smallest of line 7b, 10, or 11b. This is the most you can deduct" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_deduction`

- **Authored helper label:** This person's IRA deduction (worksheet line 12; zero with no traditional IRA contributions)
- **Encoded (NonNegDollars):** Choose — [helper "This person made traditional IRA contributions for 2025" = true → helper "Worksheet line 12 for this person's column (the smallest of line 7, 10 or 11). This is the most you can deduct"] [helper "This person made traditional IRA contributions for 2025" = false → line zero]
- **Refusal:** when person.ira_dist_gate is true, cannot complete Nondeductible IRA contributions with a 2025 distribution or conversion (Form 8606 lines 4 to 13, Pub. 590-B). With nondeductible traditional IRA contributions for 2025 and a 2025 traditional IRA distribution or Roth conversion, the taxable part of the distribution is figured on Form 8606 lines 4 to 13 (Pub. 590-B Worksheet 1-1), which this tool does not prepare. Cite: [p590a] p. 15, Both contributions for 2025 and distributions in 2025, "you must figure the taxable part of the traditional IRA distribution before you can figure your modified AGI" (2025; sha256 ca0e4287)
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_has",{"const":true}],"op":"test"},"then":"person.ira_line12"},{"guard":{"eq":["person.ira_has",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 12, "Add the amounts on lines 12a and 12b and enter the total on Schedule 1, line 20" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_10or11`

- **Authored helper label:** The smaller of line 10 or line 11 of the worksheet for this person
- **Encoded (NonNegDollars):** Enter the smaller of ira line 10 or helper "Worksheet line 11 for this person's column (traditional IRA contributions for 2025)".
- Expr: `{"of":["ira.line10","person.ira_line11"],"op":"smaller_of"}`
- Cite: [i8606] p. 9, Line 1, "subtract line 12 of the worksheet (or the amount you chose to deduct on Schedule 1 (Form 1040), line 20, if less) from the smaller of line 10 or line 11 of the worksheet" (2025; sha256 735fb7ae)

## (helper) — `person.ira_nd_figured`

- **Authored helper label:** Nondeductible contributions figured from the worksheet (the smaller of line 10 or 11, less line 12)
- **Encoded (NonNegDollars):** Subtract helper "Worksheet line 12 for this person's column (the smallest of line 7, 10 or 11). This is the most you can deduct" from helper "The smaller of line 10 or line 11 of the worksheet for this person". If zero or less, enter -0-.
- Expr: `{"from":"person.ira_10or11","op":"subtract_floor0","take":"person.ira_line12"}`
- Cite: [i8606] p. 9, Line 1, "subtract line 12 of the worksheet (or the amount you chose to deduct on Schedule 1 (Form 1040), line 20, if less) from the smaller of line 10 or line 11 of the worksheet. Enter the result on line 1 of Form 8606" (2025; sha256 735fb7ae)

## (helper) — `person.ira_nondeductible`

- **Authored helper label:** This person's nondeductible traditional IRA contributions for 2025 (Form 8606 line 1)
- **Encoded (NonNegDollars):** Choose — [helper "This person made traditional IRA contributions for 2025" = true → helper "Nondeductible contributions figured from the worksheet (the smaller of line 10 or 11, less line 12)"] [helper "This person made traditional IRA contributions for 2025" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_has",{"const":true}],"op":"test"},"then":"person.ira_nd_figured"},{"guard":{"eq":["person.ira_has",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f8606] Form 8606 (2025), line 1, "Enter your nondeductible contributions to traditional IRAs for 2025, including those made for 2025 from January 1, 2026, through April 15, 2026" (2025; sha256 748a2bf2)

## (helper) — `person.ira_files_8606`

- **Authored helper label:** This person files Form 8606 for nondeductible contributions to a traditional IRA for 2025
- **Encoded (Bool):** helper "This person's nondeductible traditional IRA contributions for 2025 (Form 8606 line 1)" > $0 (sales.zero)
- Expr: `{"gt":["person.ira_nondeductible",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i8606] p. 2, Who Must File, "You made nondeductible contributions to a traditional IRA for 2025" (2025; sha256 735fb7ae)

## (helper) — `person.ira_basis`

- **Authored helper label:** Your total basis in traditional IRAs before 2025 (Form 8606 line 2)
- **Encoded (NonNegDollars):** Input — Your total basis in traditional IRAs (Form 8606 line 2): zero if this is the first year you file Form 8606; otherwise the amount the Total Basis Chart in the Form 8606 instructions gives for the last Form 8606 you filed (generally line 14 of that form)
- Expr: `{"op":"input","source":"Your total basis in traditional IRAs (Form 8606 line 2): zero if this is the first year you file Form 8606; otherwise the amount the Total Basis Chart in the Form 8606 instructions gives for the last Form 8606 you filed (generally line 14 of that form)"}`
- Cite: [i8606] p. 9, Line 2, "Generally, if this is the first year you are required to file Form 8606, enter -0-. Otherwise, use the Total Basis Chart to find the amount to enter on line 2" (2025; sha256 735fb7ae)

## (helper) — `person.ira_basis_adjusted`

- **Authored helper label:** Your traditional IRA basis changed other than by nondeductible contributions
- **Encoded (Bool):** Input — Did your traditional IRA basis change other than by nondeductible contributions? That is: did the last Form 8606 you filed with Part I completed have a Line 15c Worksheet with an amount on line 6; did you have a return of excess traditional IRA contributions; did you transfer or receive a traditional IRA incident to divorce; or did you roll over a nontaxable part of a qualified retirement plan to a traditional IRA that wasn't previously reported on Form 8606, line 2?
- Expr: `{"op":"input","source":"Did your traditional IRA basis change other than by nondeductible contributions? That is: did the last Form 8606 you filed with Part I completed have a Line 15c Worksheet with an amount on line 6; did you have a return of excess traditional IRA contributions; did you transfer or receive a traditional IRA incident to divorce; or did you roll over a nontaxable part of a qualified retirement plan to a traditional IRA that wasn't previously reported on Form 8606, line 2?"}`
- Cite: [i8606] p. 9, Line 2, "you may need to enter an amount that is more than -0- (even if this is the first year you are required to file Form 8606) or increase or decrease the amount from the chart"; p. 9, Total Basis Chart, "the amount from line 14 of that Form 8606 as adjusted to include the amount from line 6 of the Line 15c Worksheet, if any" (2025; sha256 735fb7ae)

## (gate) — `person.ira_basis_gate`

- **Authored helper label:** A person who files Form 8606 and whose traditional IRA basis changed other than by nondeductible contributions
- **Encoded (Bool):** helper "This person files Form 8606 for nondeductible contributions to a traditional IRA for 2025" = true and helper "Your traditional IRA basis changed other than by nondeductible contributions" = true
- Expr: `{"all":[{"eq":["person.ira_files_8606",{"const":true}],"op":"test"},{"eq":["person.ira_basis_adjusted",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i8606] p. 9, Line 2, "increase or decrease the amount from the chart" (2025; sha256 735fb7ae)

## (helper) — `person.ira_8606_line2`

- **Authored helper label:** Form 8606 line 2 for this person (asked only when the person files Form 8606)
- **Encoded (NonNegDollars):** Choose — [helper "This person files Form 8606 for nondeductible contributions to a traditional IRA for 2025" = true → helper "Your total basis in traditional IRAs before 2025 (Form 8606 line 2)"] [helper "This person files Form 8606 for nondeductible contributions to a traditional IRA for 2025" = false → line zero]
- **Refusal:** when person.ira_basis_gate is true, cannot complete Form 8606, line 2 (basis adjustments). Adjusting the Form 8606 line 2 basis for a Line 15c Worksheet amount, a return of excess contributions, a transfer incident to divorce or a rollover of a nontaxable part of a qualified plan is outside this tool. Cite: [i8606] p. 9, Line 2, "you may need to enter an amount that is more than -0- (even if this is the first year you are required to file Form 8606) or increase or decrease the amount from the chart" (2025; sha256 735fb7ae)
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_files_8606",{"const":true}],"op":"test"},"then":"person.ira_basis"},{"guard":{"eq":["person.ira_files_8606",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f8606] Form 8606 (2025), line 2, "Enter your total basis in traditional IRAs" (2025; sha256 748a2bf2)

## (helper) — `person.ira_dist`

- **Authored helper label:** In 2025, did you take a distribution from a traditional IRA, or make a Roth IRA conversion?
- **Encoded (Bool):** Input — In 2025, did you take a distribution from a traditional IRA (including a SEP or SIMPLE IRA), or make a Roth IRA conversion? Do not count rollovers, qualified charitable distributions, a one-time distribution to fund an HSA, recharacterizations, or returns of contributions made by the due date of the return.
- Expr: `{"op":"input","source":"In 2025, did you take a distribution from a traditional IRA (including a SEP or SIMPLE IRA), or make a Roth IRA conversion? Do not count rollovers, qualified charitable distributions, a one-time distribution to fund an HSA, recharacterizations, or returns of contributions made by the due date of the return."}`
- Cite: [f8606] Form 8606 (2025), Part I, "In 2025, did you take a distribution from a traditional IRA, or make a Roth IRA conversion?" and "For this purpose, “distributions” does not include rollovers" (2025; sha256 748a2bf2)

## (gate) — `person.ira_dist_gate`

- **Authored helper label:** Nondeductible contributions for 2025 with a 2025 traditional IRA distribution or Roth conversion
- **Encoded (Bool):** helper "This person made traditional IRA contributions for 2025" = true and helper "This person files Form 8606 for nondeductible contributions to a traditional IRA for 2025" = true and helper "In 2025, did you take a distribution from a traditional IRA, or make a Roth IRA conversion?" = true
- Expr: `{"all":[{"eq":["person.ira_has",{"const":true}],"op":"test"},{"eq":["person.ira_files_8606",{"const":true}],"op":"test"},{"eq":["person.ira_dist",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [f8606] Form 8606 (2025), Part I, "In 2025, did you take a distribution from a traditional IRA, or make a Roth IRA conversion?" and "Go to line 4" (2025; sha256 748a2bf2)

## (helper) — `person.ira_8606_line14`

- **Authored helper label:** Form 8606 line 14 for this person (total basis in traditional IRAs for 2025 and earlier years)
- **Encoded (NonNegDollars):** Add f8606.line14 over every confirmed f8606 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8606","field":"f8606.line14","op":"sum_over"}`
- Cite: [f8606] Form 8606 (2025), line 14 (2025; sha256 748a2bf2)

## (helper) — `person.ira_ssb_lim`

- **Authored helper label:** Social Security Benefits Worksheet copy of the IRA deduction: the smaller of the applicable amount and line 10
- **Encoded (NonNegDollars):** Enter the smaller of helper "The applicable amount for this person ($7,000 if under age 50 at the end of 2025; $8,000 if age 50 or older)" or ira line 10.
- Interpretation: amb.2025.ira_ssb_copy
- Expr: `{"of":["person.ira_limit","ira.line10"],"op":"smaller_of"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "skip lines 2 through 6, enter the applicable amount below on line 7a"; p. 98, IRA Deduction Worksheet—Continued, line 12, "enter the smallest of line 7a, 10, or 11a" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_ssb_figured`

- **Authored helper label:** Social Security Benefits Worksheet copy of the IRA deduction when no one is covered by a retirement plan: the smallest of the applicable amount, line 10 and line 11
- **Encoded (NonNegDollars):** Enter the smaller of helper "Social Security Benefits Worksheet copy of the IRA deduction: the smaller of the applicable amount and line 10" or helper "Worksheet line 11 for this person's column (traditional IRA contributions for 2025)".
- **Refusal:** when ira.cov_gate is true, cannot complete Social security benefits with an IRA deduction and retirement plan coverage (Pub. 590-A Appendix B). With social security benefits, traditional IRA contributions for 2025 and you or your spouse covered by a retirement plan, the taxable benefits and the IRA deduction are figured with the worksheets in Pub. 590-A, which this tool does not prepare. Cite: [i1040gi] p. 31, Lines 6a and 6b, Exception (2025; printed date 2026-02-25; sha256 482e9c48)
- Interpretation: amb.2025.ira_ssb_copy
- Expr: `{"of":["person.ira_ssb_lim","person.ira_line11"],"op":"smaller_of"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 12, "enter the smallest of line 7a, 10, or 11a" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_ssb`

- **Authored helper label:** This person's IRA deduction as the Social Security Benefits Worksheet reads it (zero with no traditional IRA contributions)
- **Encoded (NonNegDollars):** Choose — [helper "This person made traditional IRA contributions for 2025" = true → helper "Social Security Benefits Worksheet copy of the IRA deduction when no one is covered by a retirement plan: the smallest of the applicable amount, line 10 and line 11"] [helper "This person made traditional IRA contributions for 2025" = false → line zero]
- Interpretation: amb.2025.ira_ssb_copy
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_has",{"const":true}],"op":"test"},"then":"person.ira_ssb_figured"},{"guard":{"eq":["person.ira_has",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 6 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_se_take`

- **Authored helper label:** This person's deductions on Schedule 1, lines 15 and 16
- **Encoded (NonNegDollars):** Add helper "Schedule SE line 13 (deduction for one-half of self-employment tax) for this person" and helper "Schedule 1 line 16 for this person".
- Expr: `{"of":["person.se_line13","person.s16"],"op":"sum"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 9, "minus any deductions on Schedule 1, lines 15 and 16" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_se_figured`

- **Authored helper label:** This person's earned income as a self-employed individual, less Schedule 1 lines 15 and 16 (zero or less, zero)
- **Encoded (NonNegDollars):** Subtract helper "This person's deductions on Schedule 1, lines 15 and 16" from helper "This person's Schedule C net profit or loss (all businesses)". If zero or less, enter -0-.
- Interpretation: amb.2025.ira_se_floor
- Expr: `{"from":"person.sc_total","op":"subtract_floor0","take":"person.ira_se_take"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 9, "Enter the earned income you (and your spouse if filing jointly) received as a self-employed individual or a partner" and "If zero or less, enter -0-" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_se`

- **Authored helper label:** This person's part of worksheet line 9 (zero without a Schedule C)
- **Encoded (NonNegDollars):** Choose — [helper "This person has at least one Schedule C" = true → helper "This person's earned income as a self-employed individual, less Schedule 1 lines 15 and 16 (zero or less, zero)"] [helper "This person has at least one Schedule C" = false → line zero]
- Interpretation: amb.2025.ira_se_earned
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":"person.ira_se_figured"},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 9, "Generally, this is your (and your spouse’s if filing jointly) net earnings from self-employment if your personal services were a material income-producing factor" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `person.edu`

- **Authored helper label:** Qualified education expenses paid in 2025 for this person
- **Encoded (Bool):** Input — Did anyone pay qualified education expenses in 2025 for this person at an eligible educational institution (a college, university, vocational school, or other postsecondary school eligible for federal student aid)?
- Expr: `{"op":"input","source":"Did anyone pay qualified education expenses in 2025 for this person at an eligible educational institution (a college, university, vocational school, or other postsecondary school eligible for federal student aid)?"}`
- Cite: [i8863] p. 2, Who Can Claim an Education Credit, "You may be able to claim an education credit if you, your spouse, or a dependent you claim on your tax return was a student enrolled at or attending an eligible educational institution." (2025; sha256 195cfd5e)

## (gate) — `person.edu_1098t`

- **Authored helper label:** The student received a 2025 Form 1098-T from the institution, or an exception applies
- **Encoded (Bool):** Input — Did the student receive a 2025 Form 1098-T from the educational institution? Answer yes also if the institution was not required to furnish one (for example a qualified nonresident alien, expenses paid entirely with scholarships or under a formal billing arrangement, or only courses for which no academic credit is awarded), or if the institution did not furnish it and, after February 2, 2026, but before you file, you or the student requested it and you can show the enrollment and the payments.
- Interpretation: amb.2025.edu_1098t_date
- Expr: `{"op":"input","source":"Did the student receive a 2025 Form 1098-T from the educational institution? Answer yes also if the institution was not required to furnish one (for example a qualified nonresident alien, expenses paid entirely with scholarships or under a formal billing arrangement, or only courses for which no academic credit is awarded), or if the institution did not furnish it and, after February 2, 2026, but before you file, you or the student requested it and you can show the enrollment and the payments."}`
- Cite: [i8863] p. 1, Form 1098-T requirement, "To be eligible to claim the American opportunity credit or the lifetime learning credit, the law requires a taxpayer (or a dependent) to have received Form 1098-T, Tuition Statement, from an eligible educational institution, whether domestic or foreign." (2025; sha256 195cfd5e)

## (helper) — `person.edu_student`

- **Authored helper label:** An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception)
- **Encoded (Bool):** f8863 helper "Qualified education expenses paid in 2025 for you, your spouse or a dependent you claim" = true and helper "Qualified education expenses paid in 2025 for this person" = true and (helper "Do you have an SSN or ITIN issued on or before the due date of your return?" = true or helper "If not, have you applied for an ITIN on or before the due date of your return?" = true) and helper "The student received a 2025 Form 1098-T from the institution, or an exception applies" = true
- Expr: `{"all":[{"eq":["f8863.paid",{"const":true}],"op":"test"},{"eq":["person.edu",{"const":true}],"op":"test"},{"any":[{"eq":["person.tin",{"const":true}],"op":"test"},{"eq":["person.itin_applied",{"const":true}],"op":"test"}],"op":"test"},{"eq":["person.edu_1098t",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i8863] p. 3, Who cannot claim a credit, "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)." (2025; sha256 195cfd5e)

## (helper) — `person.edu_inst`

- **Authored helper label:** Qualified education expenses required to be paid to the institution
- **Encoded (NonNegDollars):** Input — Qualified education expenses paid in 2025 for this student, by anyone, that had to be paid to the institution: tuition, required enrollment fees, and books, supplies and equipment required to be paid to the institution as a condition of enrollment or attendance, for academic periods beginning in 2025 or in the first 3 months of 2026. Use the amounts actually paid, which may differ from Form 1098-T box 1. Do not include amounts paid in 2024 or 2026, room and board, insurance, medical expenses (including student health fees), transportation, expenses deducted elsewhere (for example on Schedule C), or expenses used for a tax-free distribution from a Coverdell ESA or qualified tuition program (529 plan); zero if none
- Expr: `{"op":"input","source":"Qualified education expenses paid in 2025 for this student, by anyone, that had to be paid to the institution: tuition, required enrollment fees, and books, supplies and equipment required to be paid to the institution as a condition of enrollment or attendance, for academic periods beginning in 2025 or in the first 3 months of 2026. Use the amounts actually paid, which may differ from Form 1098-T box 1. Do not include amounts paid in 2024 or 2026, room and board, insurance, medical expenses (including student health fees), transportation, expenses deducted elsewhere (for example on Schedule C), or expenses used for a tax-free distribution from a Coverdell ESA or qualified tuition program (529 plan); zero if none"}`
- Cite: [i8863] p. 4, Qualified Education Expenses, "Generally, qualified education expenses are amounts paid in 2025 for tuition and fees required for the student’s enrollment or attendance at an eligible educational institution." (2025; sha256 195cfd5e)

## (helper) — `person.edu_mat`

- **Authored helper label:** Other course materials (American opportunity credit only)
- **Encoded (NonNegDollars):** Input — Other course materials paid for in 2025 for this student: books, supplies and equipment needed for a course of study that did not have to be paid to the institution (they count for the American opportunity credit only); the same exclusions as for the expenses paid to the institution; zero if none
- Expr: `{"op":"input","source":"Other course materials paid for in 2025 for this student: books, supplies and equipment needed for a course of study that did not have to be paid to the institution (they count for the American opportunity credit only); the same exclusions as for the expenses paid to the institution; zero if none"}`
- Cite: [i8863] p. 4, Qualified Education Expenses, "American opportunity credit: Qualified education expenses include amounts paid for tuition, fees, and course materials, which include books, supplies, and equipment needed for a course of study, whether or not the materials are purchased from the educational institution as a condition of enrollment or attendance." (2025; sha256 195cfd5e)

## (helper) — `person.edu_a2025`

- **Authored helper label:** Adjusted Qualified Education Expenses Worksheet, line 2a
- **Encoded (NonNegDollars):** Input — Tax-free educational assistance received in 2025 for this student's 2025 expenses: the tax-free part of scholarships and fellowship grants (including Pell grants; Form 1098-T box 5 may help), tax-free employer-provided educational assistance, veterans' educational assistance, and other tax-free educational assistance. Do not include wages, loans, gifts, inheritances, withdrawals from personal savings, emergency financial aid grants, or a scholarship the student includes in income (for you or your spouse, the amount on Schedule 1 line 8r); zero if none
- Expr: `{"op":"input","source":"Tax-free educational assistance received in 2025 for this student's 2025 expenses: the tax-free part of scholarships and fellowship grants (including Pell grants; Form 1098-T box 5 may help), tax-free employer-provided educational assistance, veterans' educational assistance, and other tax-free educational assistance. Do not include wages, loans, gifts, inheritances, withdrawals from personal savings, emergency financial aid grants, or a scholarship the student includes in income (for you or your spouse, the amount on Schedule 1 line 8r); zero if none"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "a. Tax-free educational assistance received in 2025 allocable to the academic period" (2025; sha256 195cfd5e)

## (helper) — `person.edu_a2026`

- **Authored helper label:** Adjusted Qualified Education Expenses Worksheet, line 2b
- **Encoded (NonNegDollars):** Input — Tax-free educational assistance received in 2026, before you file this return, that is allocable to an academic period of these 2025 expenses; zero if none
- Expr: `{"op":"input","source":"Tax-free educational assistance received in 2026, before you file this return, that is allocable to an academic period of these 2025 expenses; zero if none"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "b. Tax-free educational assistance received in 2026 (and before you file your 2025 tax return) allocable to the academic period" (2025; sha256 195cfd5e)

## (helper) — `person.edu_refunds`

- **Authored helper label:** Adjusted Qualified Education Expenses Worksheet, line 2c
- **Encoded (NonNegDollars):** Input — Refunds of these 2025 qualified education expenses received in 2025, or in 2026 before you file this return; zero if none
- Expr: `{"op":"input","source":"Refunds of these 2025 qualified education expenses received in 2025, or in 2026 before you file this return; zero if none"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "c. Refunds of qualified education expenses paid in 2025 if the refund is received in 2025 or in 2026 before you file your 2025 tax return" (2025; sha256 195cfd5e)

## (helper) — `person.edu_adj_sum`

- **Authored helper label:** Add lines 2a, 2b and 2c
- **Encoded (NonNegDollars):** Add helper "Adjusted Qualified Education Expenses Worksheet, line 2a", helper "Adjusted Qualified Education Expenses Worksheet, line 2b", and helper "Adjusted Qualified Education Expenses Worksheet, line 2c".
- Expr: `{"of":["person.edu_a2025","person.edu_a2026","person.edu_refunds"],"op":"sum"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "3. Total adjustments (add lines 2a, 2b, and 2c)" (2025; sha256 195cfd5e)

## (helper) — `person.edu_adj`

- **Authored helper label:** Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c
- **Encoded (NonNegDollars):** Choose — [helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception)" = true → helper "Add lines 2a, 2b and 2c"] [helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception)" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_student",{"const":true}],"op":"test"},"then":"person.edu_adj_sum"},{"guard":{"eq":["person.edu_student",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "3. Total adjustments (add lines 2a, 2b, and 2c)" (2025; sha256 195cfd5e)

## (gate) — `person.edu_over`

- **Authored helper label:** An academic period whose tax-free assistance and refunds exceed its expenses paid to the institution
- **Encoded (Bool):** Input — Was there an academic period for which the tax-free educational assistance and refunds allocable to it were more than that period's qualified education expenses that had to be paid to the institution (tuition, required fees and course materials required to be paid to the institution)?
- Expr: `{"op":"input","source":"Was there an academic period for which the tax-free educational assistance and refunds allocable to it were more than that period's qualified education expenses that had to be paid to the institution (tuition, required fees and course materials required to be paid to the institution)?"}`
- Cite: [i8863] p. 4, Tax-free educational assistance, "For tax-free educational assistance received in 2025, reduce the qualified education expenses for each academic period by the amount of tax-free educational assistance allocable to that academic period." (2025; sha256 195cfd5e)

## (gate) — `person.edu_over_refused`

- **Authored helper label:** Adjustments that exceed one academic period's expenses
- **Encoded (Bool):** helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception)" = true and helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c" > $0 and helper "An academic period whose tax-free assistance and refunds exceed its expenses paid to the institution" = true
- Expr: `{"all":[{"eq":["person.edu_student",{"const":true}],"op":"test"},{"gt":["person.edu_adj",{"const":0}],"op":"test"},{"eq":["person.edu_over",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)

## 23 — `person.edu_line23`

- **Authored helper label:** Has the American opportunity credit been claimed for this student for any 4 prior tax years?
- **Encoded (Bool):** Input — Has the American opportunity credit been claimed (by you or anyone else) for this student for any 4 tax years before 2025?
- **Shown on the values sheet only when:** An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception) (`person.edu_student`)
- Expr: `{"op":"input","source":"Has the American opportunity credit been claimed (by you or anyone else) for this student for any 4 tax years before 2025?"}`
- Cite: [f8863] p. 2, Part III, line 23, "Has the American opportunity credit been claimed for this student for any 4 prior tax years?" (2025; sha256 a251a1cf)

## (helper) — `person.edu_show24`

- **Authored helper label:** Line 24 is reached (line 23 did not stop)
- **Encoded (Bool):** helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception)" = true and line 23 = false
- Expr: `{"all":[{"eq":["person.edu_student",{"const":true}],"op":"test"},{"eq":["person.edu_line23",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [f8863] p. 2, Part III, line 23, "Yes—Stop! Go to line 31 for this student." (2025; sha256 a251a1cf)

## 24 — `person.edu_line24`

- **Authored helper label:** Was the student enrolled at least half-time for at least one academic period that began or is treated as having begun in 2025 at an eligible educational institution in a program leading toward a postsecondary degree, certificate, or other recognized postsecondary educational credential?
- **Encoded (Bool):** Input — Was the student enrolled at least half-time (Form 1098-T box 8) for at least one academic period that began in 2025, or in the first 3 months of 2026 if paid for in 2025, at an eligible educational institution, in a program leading toward a postsecondary degree, certificate or other recognized postsecondary educational credential?
- **Shown on the values sheet only when:** Line 24 is reached (line 23 did not stop) (`person.edu_show24`)
- Expr: `{"op":"input","source":"Was the student enrolled at least half-time (Form 1098-T box 8) for at least one academic period that began in 2025, or in the first 3 months of 2026 if paid for in 2025, at an eligible educational institution, in a program leading toward a postsecondary degree, certificate or other recognized postsecondary educational credential?"}`
- Cite: [f8863] p. 2, Part III, line 24, "Was the student enrolled at least half-time for at least one academic period that began or is treated as having begun in 2025 at an eligible educational institution in a program leading toward a postsecondary degree, certificate, or other recognized postsecondary educational credential?" (2025; sha256 a251a1cf)

## (helper) — `person.edu_show25`

- **Authored helper label:** Line 25 is reached (line 24 did not stop)
- **Encoded (Bool):** helper "Line 24 is reached (line 23 did not stop)" = true and line 24 = true
- Expr: `{"all":[{"eq":["person.edu_show24",{"const":true}],"op":"test"},{"eq":["person.edu_line24",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [f8863] p. 2, Part III, line 24, "No—Stop! Go to line 31 for this student." (2025; sha256 a251a1cf)

## 25 — `person.edu_line25`

- **Authored helper label:** Did the student complete the first 4 years of postsecondary education before 2025?
- **Encoded (Bool):** Input — Did the student complete the first 4 years of postsecondary education before 2025, as determined by the institution (4 years of academic credit, not counting credit awarded solely for proficiency examinations)?
- **Shown on the values sheet only when:** Line 25 is reached (line 24 did not stop) (`person.edu_show25`)
- Expr: `{"op":"input","source":"Did the student complete the first 4 years of postsecondary education before 2025, as determined by the institution (4 years of academic credit, not counting credit awarded solely for proficiency examinations)?"}`
- Cite: [f8863] p. 2, Part III, line 25, "Did the student complete the first 4 years of postsecondary education before 2025?" (2025; sha256 a251a1cf)

## (helper) — `person.edu_show26`

- **Authored helper label:** Line 26 is reached (line 25 did not stop)
- **Encoded (Bool):** helper "Line 25 is reached (line 24 did not stop)" = true and line 25 = false
- Expr: `{"all":[{"eq":["person.edu_show25",{"const":true}],"op":"test"},{"eq":["person.edu_line25",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [f8863] p. 2, Part III, line 25, "Yes—Stop! Go to line 31 for this student." (2025; sha256 a251a1cf)

## 26 — `person.edu_line26`

- **Authored helper label:** Was the student convicted, before the end of 2025, of a felony for possession or distribution of a controlled substance?
- **Encoded (Bool):** Input — Was the student convicted, before the end of 2025, of a federal or state felony for possession or distribution of a controlled substance?
- **Shown on the values sheet only when:** Line 26 is reached (line 25 did not stop) (`person.edu_show26`)
- Expr: `{"op":"input","source":"Was the student convicted, before the end of 2025, of a federal or state felony for possession or distribution of a controlled substance?"}`
- Cite: [f8863] p. 2, Part III, line 26, "Was the student convicted, before the end of 2025, of a felony for possession or distribution of a controlled substance?" (2025; sha256 a251a1cf)

## (gate) — `person.edu_ein`

- **Authored helper label:** The institution's employer identification number (EIN) is available
- **Encoded (Bool):** Input — Do you have the educational institution's employer identification number (EIN), from Form 1098-T or from the institution?
- Expr: `{"op":"input","source":"Do you have the educational institution's employer identification number (EIN), from Form 1098-T or from the institution?"}`
- Cite: [i8863] p. 4, Student qualifications, "7. You must provide the educational institution’s employer identification number (EIN) on your Form 8863." (2025; sha256 195cfd5e)

## (helper) — `person.edu_aoc`

- **Authored helper label:** An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available
- **Encoded (Bool):** helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception)" = true and line 23 = false and line 24 = true and line 25 = false and line 26 = false and household helper "You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN" = true and helper "The institution's employer identification number (EIN) is available" = true
- Interpretation: amb.2025.edu_filer_tin
- Expr: `{"all":[{"eq":["person.edu_student",{"const":true}],"op":"test"},{"eq":["person.edu_line23",{"const":false}],"op":"test"},{"eq":["person.edu_line24",{"const":true}],"op":"test"},{"eq":["person.edu_line25",{"const":false}],"op":"test"},{"eq":["person.edu_line26",{"const":false}],"op":"test"},{"eq":["household.all_tin",{"const":true}],"op":"test"},{"eq":["person.edu_ein",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [f8863] p. 2, Part III, line 26, "No—Complete lines 27 through 30 for this student."; i8863 p. 3, Student qualifications, "5. Filers and students must have been issued a TIN by the due date of their 2025 return (including extensions)." (2025; sha256 a251a1cf)

## (helper) — `person.edu_llc`

- **Authored helper label:** A lifetime learning credit student: an eligible student who is not an American opportunity credit student
- **Encoded (Bool):** helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception)" = true and helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false
- Expr: `{"all":[{"eq":["person.edu_student",{"const":true}],"op":"test"},{"eq":["person.edu_aoc",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i8863] p. 4, Tip, "If the requirements above aren’t met for any student, you cannot claim the American opportunity credit for that student. You may be able to claim the lifetime learning credit for part or all of that student’s qualified education expenses instead if certain requirements are met." (2025; sha256 195cfd5e)

## 27 — `person.edu_line27`

- **Authored helper label:** Adjusted qualified education expenses. Don't enter more than $4,000
- **Encoded (NonNegDollars):** Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line27" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → line zero]
- **Refusal:** when person.edu_over_refused is true, cannot complete Adjusted Qualified Education Expenses Worksheet for more than one academic period. The worksheet is completed for each academic period, and an academic period whose tax-free educational assistance and refunds exceed its own expenses cannot be netted against another period's expenses. Figure the worksheet period by period. Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)
- **Shown on the values sheet only when:** An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available (`person.edu_aoc`)
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_aoc",{"const":true}],"op":"test"},"then":{"bind":{"adj":"person.edu_adj","inst":"person.edu_inst","mat":"person.edu_mat"},"def":"aqee","line":"line27"}},{"guard":{"eq":["person.edu_aoc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 27, "Adjusted qualified education expenses (see instructions). Don’t enter more than $4,000" (2025; sha256 a251a1cf)

## 28 — `person.edu_line28`

- **Authored helper label:** Subtract $2,000 from line 27. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line28" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → line zero]
- **Refusal:** when person.edu_over_refused is true, cannot complete Adjusted Qualified Education Expenses Worksheet for more than one academic period. The worksheet is completed for each academic period, and an academic period whose tax-free educational assistance and refunds exceed its own expenses cannot be netted against another period's expenses. Figure the worksheet period by period. Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)
- **Shown on the values sheet only when:** An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available (`person.edu_aoc`)
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_aoc",{"const":true}],"op":"test"},"then":{"bind":{"adj":"person.edu_adj","inst":"person.edu_inst","mat":"person.edu_mat"},"def":"aqee","line":"line28"}},{"guard":{"eq":["person.edu_aoc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 28, "Subtract $2,000 from line 27. If zero or less, enter -0-" (2025; sha256 a251a1cf)

## 29 — `person.edu_line29`

- **Authored helper label:** Multiply line 28 by 25% (0.25)
- **Encoded (NonNegDollars):** Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line29" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → line zero]
- **Refusal:** when person.edu_over_refused is true, cannot complete Adjusted Qualified Education Expenses Worksheet for more than one academic period. The worksheet is completed for each academic period, and an academic period whose tax-free educational assistance and refunds exceed its own expenses cannot be netted against another period's expenses. Figure the worksheet period by period. Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)
- **Shown on the values sheet only when:** An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available (`person.edu_aoc`)
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_aoc",{"const":true}],"op":"test"},"then":{"bind":{"adj":"person.edu_adj","inst":"person.edu_inst","mat":"person.edu_mat"},"def":"aqee","line":"line29"}},{"guard":{"eq":["person.edu_aoc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 29, "Multiply line 28 by 25% (0.25)" (2025; sha256 a251a1cf)

## 30 — `person.edu_line30`

- **Authored helper label:** American opportunity credit for this student. If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on line 29
- **Encoded (NonNegDollars):** Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line30" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → line zero]
- **Refusal:** when person.edu_over_refused is true, cannot complete Adjusted Qualified Education Expenses Worksheet for more than one academic period. The worksheet is completed for each academic period, and an academic period whose tax-free educational assistance and refunds exceed its own expenses cannot be netted against another period's expenses. Figure the worksheet period by period. Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)
- **Shown on the values sheet only when:** An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available (`person.edu_aoc`)
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_aoc",{"const":true}],"op":"test"},"then":{"bind":{"adj":"person.edu_adj","inst":"person.edu_inst","mat":"person.edu_mat"},"def":"aqee","line":"line30"}},{"guard":{"eq":["person.edu_aoc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 30, "If line 28 is zero, enter the amount from line 27.", "Include the total of all amounts from all Parts III, line 30, on Part I, line 1" (2025; sha256 a251a1cf)

## 31 — `person.edu_line31`

- **Authored helper label:** Adjusted qualified education expenses for the lifetime learning credit
- **Encoded (NonNegDollars):** Choose — [helper "A lifetime learning credit student: an eligible student who is not an American opportunity credit student" = true → "ws4_llc" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "A lifetime learning credit student: an eligible student who is not an American opportunity credit student" = false → line zero]
- **Refusal:** when person.edu_over_refused is true, cannot complete Adjusted Qualified Education Expenses Worksheet for more than one academic period. The worksheet is completed for each academic period, and an academic period whose tax-free educational assistance and refunds exceed its own expenses cannot be netted against another period's expenses. Figure the worksheet period by period. Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)
- **Shown on the values sheet only when:** A lifetime learning credit student: an eligible student who is not an American opportunity credit student (`person.edu_llc`)
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_llc",{"const":true}],"op":"test"},"then":{"bind":{"adj":"person.edu_adj","inst":"person.edu_inst","mat":"person.edu_mat"},"def":"aqee","line":"ws4_llc"}},{"guard":{"eq":["person.edu_llc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 31, "Adjusted qualified education expenses (see instructions). Include the total of all amounts from all Parts III, line 31, on Part II, line 10" (2025; sha256 a251a1cf)

## (helper) — `person.edu_born_2007`

- **Authored helper label:** Were you born before January 2, 2007?
- **Encoded (Bool):** Input — Were you born before January 2, 2007?
- Interpretation: amb.2025.edu_age_rule
- Expr: `{"op":"input","source":"Were you born before January 2, 2007?"}`
- Cite: [i8863] p. 7, Line 7, "b. Age 18 at the end of 2025 and your earned income (defined later) was less than one-half of your support (defined later), or" (2025; sha256 195cfd5e)

## (helper) — `person.edu_born_2002`

- **Authored helper label:** Were you born before January 2, 2002?
- **Encoded (Bool):** Input — Were you born before January 2, 2002?
- Interpretation: amb.2025.edu_age_rule
- Expr: `{"op":"input","source":"Were you born before January 2, 2002?"}`
- Cite: [i8863] p. 7, Line 7, "1. Were you under age 24 at the end of 2025?" (2025; sha256 195cfd5e)

## (helper) — `person.edu_fulltime`

- **Authored helper label:** A full-time student for 2025 (any part of 5 calendar months at an eligible educational institution)
- **Encoded (Bool):** Input — Were you a full-time student for 2025: during any part of any 5 calendar months of 2025, were you enrolled as a full-time student at an eligible educational institution, or did you take a full-time, on-farm training course given by such an institution or by a state, county, or local government agency?
- Interpretation: amb.2025.edu_fulltime
- Expr: `{"op":"input","source":"Were you a full-time student for 2025: during any part of any 5 calendar months of 2025, were you enrolled as a full-time student at an eligible educational institution, or did you take a full-time, on-farm training course given by such an institution or by a state, county, or local government agency?"}`
- Cite: [i8863] p. 7, Full-time student, "you were a full-time student for 2025 if during any part of any 5 calendar months during the year you were enrolled as a full-time student at an eligible educational institution (defined earlier), or took a full-time, on-farm training course given by such an institution or by a state, county, or local government agency." (2025; sha256 195cfd5e)

## (helper) — `person.edu_half_support`

- **Authored helper label:** Your earned income was less than one-half of your support for 2025
- **Encoded (Bool):** Input — Was your earned income for 2025 less than one-half of your support? Earned income is wages, salaries, professional fees and other pay for personal services (including the part of a scholarship that pays for teaching, research or other required services). Support includes food, shelter, clothing, medical and dental care, education and the like, provided by you, your parents and others; a scholarship is not support if you were a full-time student.
- Expr: `{"op":"input","source":"Was your earned income for 2025 less than one-half of your support? Earned income is wages, salaries, professional fees and other pay for personal services (including the part of a scholarship that pays for teaching, research or other required services). Support includes food, shelter, clothing, medical and dental care, education and the like, provided by you, your parents and others; a scholarship is not support if you were a full-time student."}`
- Cite: [i8863] p. 7, Earned income, "Earned income includes wages, salaries, professional fees, and other payments received for personal services actually performed." (2025; sha256 195cfd5e)

## (helper) — `person.edu_parent`

- **Authored helper label:** At least one of your parents was alive at the end of 2025
- **Encoded (Bool):** Input — Was at least one of your parents alive at the end of 2025?
- Expr: `{"op":"input","source":"Was at least one of your parents alive at the end of 2025?"}`
- Cite: [i8863] p. 7, Line 7, "2. At least one of your parents was alive at the end of 2025." (2025; sha256 195cfd5e)

## (helper) — `person.edu_kid`

- **Authored helper label:** Line 7 conditions 1 and 2 for you: under 18; or 18 with earned income less than half of your support; or over 18 and under 24, a full-time student, with earned income less than half of your support; and a parent alive
- **Encoded (Bool):** f8863 helper "Line 7 is above zero on a return that is not joint (the line 7 conditions are asked)" = true and (helper "Were you born before January 2, 2008?" = false or helper "Were you born before January 2, 2007?" = false and helper "Your earned income was less than one-half of your support for 2025" = true or helper "Were you born before January 2, 2002?" = false and helper "A full-time student for 2025 (any part of 5 calendar months at an eligible educational institution)" = true and helper "Your earned income was less than one-half of your support for 2025" = true) and helper "At least one of your parents was alive at the end of 2025" = true
- Interpretation: amb.2025.edu_age_rule
- Expr: `{"all":[{"eq":["f8863.kid_needed",{"const":true}],"op":"test"},{"any":[{"eq":["person.sav_born",{"const":false}],"op":"test"},{"all":[{"eq":["person.edu_born_2007",{"const":false}],"op":"test"},{"eq":["person.edu_half_support",{"const":true}],"op":"test"}],"op":"test"},{"all":[{"eq":["person.edu_born_2002",{"const":false}],"op":"test"},{"eq":["person.edu_fulltime",{"const":true}],"op":"test"},{"eq":["person.edu_half_support",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"},{"eq":["person.edu_parent",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i8863] p. 7, Line 7, "You don’t qualify for a refundable American opportunity credit if 1 (a, b, or c), 2, and 3 below apply to you." (2025; sha256 195cfd5e)

## (helper) — `person.x_l1`

- **Authored helper label:** Form 5329 line 1 for this person: early distributions includible in income
- **Encoded (NonNegDollars):** Add retirement.l1 over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.l1","op":"sum_over"}`
- Cite: [i5329] p. 3, Line 1, "Enter the amount of early distributions includible in income (other than qualified disaster recovery distributions) that you received from:" (2025; sha256 aec3d325)

## (helper) — `person.x_l2_all`

- **Authored helper label:** Exception amounts before the per-person limits
- **Encoded (NonNegDollars):** Add retirement.l2 over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.l2","op":"sum_over"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (helper) — `person.x_l1_s`

- **Authored helper label:** Line 1 amounts from code S distributions
- **Encoded (NonNegDollars):** Add retirement.l1_s over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.l1_s","op":"sum_over"}`
- Cite: [i5329] p. 5, Line 4, "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%." (2025; sha256 aec3d325)

## (helper) — `person.x_l2_s`

- **Authored helper label:** Line 2 amounts from code S distributions
- **Encoded (NonNegDollars):** Add retirement.l2_s over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.l2_s","op":"sum_over"}`
- Cite: [i5329] p. 5, Line 4, "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%." (2025; sha256 aec3d325)

## (helper) — `person.x_e05`

- **Authored helper label:** Exception 05 amounts
- **Encoded (NonNegDollars):** Add retirement.l2_e05 over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.l2_e05","op":"sum_over"}`
- Cite: [i5329] p. 5, Line 2, "Qualified retirement plan distributions up to the amount you paid for unreimbursed medical expenses during the year minus 7.5% of your adjusted gross income (AGI) for the year." (2025; sha256 aec3d325)

## (helper) — `person.x_e09`

- **Authored helper label:** Exception 09 amounts
- **Encoded (NonNegDollars):** Add retirement.l2_e09 over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.l2_e09","op":"sum_over"}`
- Cite: [p590b] p. 27, First home, "you don't have to pay the 10% additional tax on up to $10,000 of distributions you receive to buy, build, or rebuild a first home." (2025; sha256 d18a592e)

## (helper) — `person.x_e19`

- **Authored helper label:** Exception 19 amounts
- **Encoded (NonNegDollars):** Add retirement.l2_e19 over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.l2_e19","op":"sum_over"}`
- Cite: [p590b] p. 28, Qualified birth or adoption distribution, "A qualified birth or adoption distribution must not exceed $5,000 per taxpayer." (2025; sha256 d18a592e)

## (helper) — `person.x_e22`

- **Authored helper label:** Exception 22 amounts
- **Encoded (NonNegDollars):** Add retirement.l2_e22 over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.l2_e22","op":"sum_over"}`
- Cite: [p590b] p. 28, Distributions to domestic abuse victims, "on to a domestic abuse victim must not exceed the lesser of $10,300 for 2025 or 50% of the present value of the IRA." (2025; sha256 d18a592e)

## (helper) — `person.x_e23`

- **Authored helper label:** Exception 23 amounts
- **Encoded (NonNegDollars):** Add retirement.l2_e23 over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.l2_e23","op":"sum_over"}`
- Cite: [p590b] p. 28, Emergency personal expense distributions, "personal expense distribution must not exceed the lesser of $1,000 or your total interest in the IRA minus $1,000." (2025; sha256 d18a592e)

## (helper) — `person.x_tax`

- **Authored helper label:** This person's Form 5329 taxes
- **Encoded (NonNegDollars):** Add f5329.tax over every confirmed f5329 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f5329","field":"f5329.tax","op":"sum_over"}`
- Cite: [f1040s2] p. 1, Part II, line 8, "Additional tax on IRAs or other tax-favored accounts. Attach Form 5329 if required." (2025; created 2025-05-08; sha256 64d867b6)

## (helper) — `person.x_must`

- **Authored helper label:** One if this person must file Form 5329
- **Encoded (Count):** Add f5329.one over every confirmed f5329 entry for which helper "This person must file Form 5329 (an exception claimed, a code S distribution, or HSA excess)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f5329","field":"f5329.one","op":"sum_over","where":{"eq":["f5329.must",{"const":true}],"op":"test"}}`
- Cite: [i5329] p. 1, Who Must File, "However, if distribution code 1 is correctly shown in box 7 of all your Forms 1099-R and you owe the additional tax on the full amount shown on each Form 1099-R, you don’t have to file Form 5329." (2025; sha256 aec3d325)

## (helper) — `person.x_prior09`

- **Authored helper label:** Earlier first-home distributions excluded from the additional tax
- **Encoded (NonNegDollars):** Input — Total of your earlier IRA distributions (before 2025) for which the first-home exception was used; zero if none
- Expr: `{"op":"input","source":"Total of your earlier IRA distributions (before 2025) for which the first-home exception was used; zero if none"}`
- Cite: [p590b] p. 27, First home, "you don't have to pay the 10% additional tax on up to $10,000 of distributions you receive to buy, build, or rebuild a first home." (2025; sha256 d18a592e)

## (helper) — `person.x_cap09_base`

- **Authored helper label:** Year parameter f5329.cap_first_home ($10,000)
- **Encoded (NonNegDollars):** Enter $10,000 (f5329.cap_first_home).
- Expr: `{"op":"param","ref":"f5329.cap_first_home"}`
- Cite: [p590b] p. 27, First home, "you don't have to pay the 10% additional tax on up to $10,000 of distributions you receive to buy, build, or rebuild a first home." (2025; sha256 d18a592e)

## (helper) — `person.x_cap09`

- **Authored helper label:** First-home limit left: $10,000 less earlier first-home distributions
- **Encoded (NonNegDollars):** Subtract helper "Earlier first-home distributions excluded from the additional tax" from helper "Year parameter f5329.cap_first_home ($10,000)". If zero or less, enter -0-.
- Expr: `{"from":"person.x_cap09_base","op":"subtract_floor0","take":"person.x_prior09"}`
- Cite: [p590b] p. 27, First home, "you don't have to pay the 10% additional tax on up to $10,000 of distributions you receive to buy, build, or rebuild a first home." (2025; sha256 d18a592e)

## (helper) — `person.x_births`

- **Authored helper label:** Number of births or adoptions the distributions were for
- **Encoded (Count):** Input — For how many births or adoptions (children born or adopted, each counted once) did you take the birth or adoption distributions?
- Expr: `{"op":"input","source":"For how many births or adoptions (children born or adopted, each counted once) did you take the birth or adoption distributions?"}`
- Cite: [p590b] p. 28, Qualified birth or adoption distribution, "A qualified birth or adoption distribution must not exceed $5,000 per taxpayer." (2025; sha256 d18a592e)

## (helper) — `person.x_cap19_one`

- **Authored helper label:** Year parameter f5329.cap_birth ($5,000)
- **Encoded (NonNegDollars):** Enter $5,000 (f5329.cap_birth).
- Expr: `{"op":"param","ref":"f5329.cap_birth"}`
- Cite: [p590b] p. 28, Qualified birth or adoption distribution, "A qualified birth or adoption distribution must not exceed $5,000 per taxpayer." (2025; sha256 d18a592e)

## (helper) — `person.x_cap19`

- **Authored helper label:** $5,000 for each birth or adoption
- **Encoded (NonNegDollars):** Multiply helper "Year parameter f5329.cap_birth ($5,000)" by the number on helper "Number of births or adoptions the distributions were for".
- Interpretation: amb.2025.f5329_birth_cap
- Expr: `{"amount":"person.x_cap19_one","count":"person.x_births","op":"multiply_count"}`
- Cite: [p590b] p. 28, Qualified birth or adoption distribution, "A qualified birth or adoption distribution must not exceed $5,000 per taxpayer." (2025; sha256 d18a592e)

## (helper) — `person.x_cap22`

- **Authored helper label:** Year parameter f5329.cap_abuse ($10,300)
- **Encoded (NonNegDollars):** Enter $10,300 (f5329.cap_abuse).
- Expr: `{"op":"param","ref":"f5329.cap_abuse"}`
- Cite: [p590b] p. 28, Distributions to domestic abuse victims, "on to a domestic abuse victim must not exceed the lesser of $10,300 for 2025 or 50% of the present value of the IRA." (2025; sha256 d18a592e)

## (helper) — `person.x_cap23`

- **Authored helper label:** Year parameter f5329.cap_emergency ($1,000)
- **Encoded (NonNegDollars):** Enter $1,000 (f5329.cap_emergency).
- Expr: `{"op":"param","ref":"f5329.cap_emergency"}`
- Cite: [p590b] p. 28, Emergency personal expense distributions, "personal expense distribution must not exceed the lesser of $1,000 or your total interest in the IRA minus $1,000." (2025; sha256 d18a592e)

## (helper) — `person.x_c05`

- **Authored helper label:** Exception 05 limited to the medical expenses above 7.5% of AGI (Schedule A line 4)
- **Encoded (NonNegDollars):** Choose — [helper "Any exception 05 amount" = true → helper "Smaller of the exception 05 amounts and Schedule A line 4"] [helper "Any exception 05 amount" = false → line zero]
- Interpretation: amb.2025.f5329_medical_joint
- Expr: `{"alternatives":[{"guard":{"eq":["person.x_has05",{"const":true}],"op":"test"},"then":"person.x_c05_min"},{"guard":{"eq":["person.x_has05",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 2, "Qualified retirement plan distributions up to the amount you paid for unreimbursed medical expenses during the year minus 7.5% of your adjusted gross income (AGI) for the year." (2025; sha256 aec3d325)

## (helper) — `person.x_has05`

- **Authored helper label:** Any exception 05 amount
- **Encoded (Bool):** helper "Exception 05 amounts" > $0
- Expr: `{"gt":["person.x_e05",{"const":0}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "Qualified retirement plan distributions up to the amount you paid for unreimbursed medical expenses during the year minus 7.5% of your adjusted gross income (AGI) for the year." (2025; sha256 aec3d325)

## (helper) — `person.x_c05_min`

- **Authored helper label:** Smaller of the exception 05 amounts and Schedule A line 4
- **Encoded (NonNegDollars):** Enter the smaller of helper "Exception 05 amounts" or sa line 4.
- Expr: `{"of":["person.x_e05","sa.line4"],"op":"smaller_of"}`
- Cite: [i5329] p. 5, Line 2, "Qualified retirement plan distributions up to the amount you paid for unreimbursed medical expenses during the year minus 7.5% of your adjusted gross income (AGI) for the year." (2025; sha256 aec3d325)

## (helper) — `person.x_has09`

- **Authored helper label:** Any exception 09 amount
- **Encoded (Bool):** helper "Exception 09 amounts" > $0
- Expr: `{"gt":["person.x_e09",{"const":0}],"op":"test"}`
- Cite: [p590b] p. 27, First home, "you don't have to pay the 10% additional tax on up to $10,000 of distributions you receive to buy, build, or rebuild a first home." (2025; sha256 d18a592e)

## (helper) — `person.x_c09_min`

- **Authored helper label:** Smaller of the exception 09 amounts and the limit left
- **Encoded (NonNegDollars):** Enter the smaller of helper "Exception 09 amounts" or helper "First-home limit left: $10,000 less earlier first-home distributions".
- Expr: `{"of":["person.x_e09","person.x_cap09"],"op":"smaller_of"}`
- Cite: [p590b] p. 27, First home, "you don't have to pay the 10% additional tax on up to $10,000 of distributions you receive to buy, build, or rebuild a first home." (2025; sha256 d18a592e)

## (helper) — `person.x_c09`

- **Authored helper label:** Exception 09 within the $10,000 first-home limit
- **Encoded (NonNegDollars):** Choose — [helper "Any exception 09 amount" = true → helper "Smaller of the exception 09 amounts and the limit left"] [helper "Any exception 09 amount" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.x_has09",{"const":true}],"op":"test"},"then":"person.x_c09_min"},{"guard":{"eq":["person.x_has09",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [p590b] p. 27, First home, "you don't have to pay the 10% additional tax on up to $10,000 of distributions you receive to buy, build, or rebuild a first home." (2025; sha256 d18a592e)

## (helper) — `person.x_has19`

- **Authored helper label:** Any exception 19 amount
- **Encoded (Bool):** helper "Exception 19 amounts" > $0
- Expr: `{"gt":["person.x_e19",{"const":0}],"op":"test"}`
- Cite: [p590b] p. 28, Qualified birth or adoption distribution, "A qualified birth or adoption distribution must not exceed $5,000 per taxpayer." (2025; sha256 d18a592e)

## (helper) — `person.x_c19_min`

- **Authored helper label:** Smaller of the exception 19 amounts and $5,000 a birth or adoption
- **Encoded (NonNegDollars):** Enter the smaller of helper "Exception 19 amounts" or helper "$5,000 for each birth or adoption".
- Expr: `{"of":["person.x_e19","person.x_cap19"],"op":"smaller_of"}`
- Cite: [p590b] p. 28, Qualified birth or adoption distribution, "A qualified birth or adoption distribution must not exceed $5,000 per taxpayer." (2025; sha256 d18a592e)

## (helper) — `person.x_c19`

- **Authored helper label:** Exception 19 within $5,000 a birth or adoption
- **Encoded (NonNegDollars):** Choose — [helper "Any exception 19 amount" = true → helper "Smaller of the exception 19 amounts and $5,000 a birth or adoption"] [helper "Any exception 19 amount" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.x_has19",{"const":true}],"op":"test"},"then":"person.x_c19_min"},{"guard":{"eq":["person.x_has19",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [p590b] p. 28, Qualified birth or adoption distribution, "A qualified birth or adoption distribution must not exceed $5,000 per taxpayer." (2025; sha256 d18a592e)

## (helper) — `person.x_c22`

- **Authored helper label:** Exception 22 within $10,300
- **Encoded (NonNegDollars):** Enter the smaller of helper "Exception 22 amounts" or helper "Year parameter f5329.cap_abuse ($10,300)".
- Expr: `{"of":["person.x_e22","person.x_cap22"],"op":"smaller_of"}`
- Cite: [p590b] p. 28, Distributions to domestic abuse victims, "on to a domestic abuse victim must not exceed the lesser of $10,300 for 2025 or 50% of the present value of the IRA." (2025; sha256 d18a592e)

## (helper) — `person.x_c23`

- **Authored helper label:** Exception 23 within $1,000
- **Encoded (NonNegDollars):** Enter the smaller of helper "Exception 23 amounts" or helper "Year parameter f5329.cap_emergency ($1,000)".
- Expr: `{"of":["person.x_e23","person.x_cap23"],"op":"smaller_of"}`
- Cite: [p590b] p. 28, Emergency personal expense distributions, "personal expense distribution must not exceed the lesser of $1,000 or your total interest in the IRA minus $1,000." (2025; sha256 d18a592e)

## (helper) — `person.x_n23`

- **Authored helper label:** Forms 1099-R claiming exception 23
- **Encoded (Count):** Add retirement.one over every confirmed retirement entry for which helper "Exception 23" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.one","op":"sum_over","where":{"eq":["retirement.is_e23",{"const":true}],"op":"test"}}`
- Cite: [p590b] p. 28, Distribution limits, "You are limited to taking one emergency personal expense distribution per calendar year" (2025; sha256 d18a592e)

## (gate) — `person.x_two23`

- **Authored helper label:** Exception 23 claimed on more than one distribution
- **Encoded (Bool):** helper "Forms 1099-R claiming exception 23" > 1 (a count)
- Expr: `{"gt":["person.x_n23",{"const":1,"type":"Count"}],"op":"test"}`
- Cite: [p590b] p. 28, Distribution limits, "You are limited to taking one emergency personal expense distribution per calendar year" (2025; sha256 d18a592e)

## (helper) — `person.x_capped_sum`

- **Authored helper label:** Exceptions 05, 09, 19, 22 and 23 before their limits
- **Encoded (NonNegDollars):** Add helper "Exception 05 amounts", helper "Exception 09 amounts", helper "Exception 19 amounts", helper "Exception 22 amounts", and helper "Exception 23 amounts".
- Expr: `{"of":["person.x_e05","person.x_e09","person.x_e19","person.x_e22","person.x_e23"],"op":"sum"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (helper) — `person.x_limited_sum`

- **Authored helper label:** Exceptions 05, 09, 19, 22 and 23 within their limits
- **Encoded (NonNegDollars):** Add helper "Exception 05 limited to the medical expenses above 7.5% of AGI (Schedule A line 4)", helper "Exception 09 within the $10,000 first-home limit", helper "Exception 19 within $5,000 a birth or adoption", helper "Exception 22 within $10,300", and helper "Exception 23 within $1,000".
- Expr: `{"of":["person.x_c05","person.x_c09","person.x_c19","person.x_c22","person.x_c23"],"op":"sum"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (helper) — `person.x_other_exc`

- **Authored helper label:** Exceptions without a fixed limit
- **Encoded (NonNegDollars):** Subtract helper "Exceptions 05, 09, 19, 22 and 23 before their limits" from helper "Exception amounts before the per-person limits". If zero or less, enter -0-.
- Expr: `{"from":"person.x_l2_all","op":"subtract_floor0","take":"person.x_capped_sum"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (gate) — `person.x_limit_binds`

- **Authored helper label:** A limited exception over its limit on a person with a code S distribution
- **Encoded (Bool):** helper "Line 1 amounts from code S distributions" > $0 and helper "Exceptions 05, 09, 19, 22 and 23 before their limits" > helper "Exceptions 05, 09, 19, 22 and 23 within their limits"
- Interpretation: amb.2025.f5329_simple_limits
- Expr: `{"all":[{"gt":["person.x_l1_s",{"const":0}],"op":"test"},{"gt":["person.x_capped_sum","person.x_limited_sum"],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 4, "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%." (2025; sha256 aec3d325)

## (gate) — `person.x_other`

- **Authored helper label:** Form 5329 parts this tool does not prepare
- **Encoded (Bool):** Input — Does any of these apply to you: a taxable distribution from a Coverdell ESA, a qualified tuition program (529 plan) or an ABLE account; excess contributions to a traditional or Roth IRA for an earlier year that are still in the IRA (whether or not you contributed for 2025); excess contributions to a Coverdell ESA, an Archer MSA or an ABLE account; excess HSA contributions from an earlier year when you have no Form 8889 for 2025; or a required minimum distribution from an IRA or plan that you did not take?
- Expr: `{"op":"input","source":"Does any of these apply to you: a taxable distribution from a Coverdell ESA, a qualified tuition program (529 plan) or an ABLE account; excess contributions to a traditional or Roth IRA for an earlier year that are still in the IRA (whether or not you contributed for 2025); excess contributions to a Coverdell ESA, an Archer MSA or an ABLE account; excess HSA contributions from an earlier year when you have no Form 8889 for 2025; or a required minimum distribution from an IRA or plan that you did not take?"}`
- Cite: [f5329] p. 1, Part II, "Complete this part if you included an amount in income, on Schedule 1 (Form 1040), line 8z, from a Coverdell education savings account (ESA) or a qualified tuition program (QTP), or on Schedule 1 (Form 1040), line 8q, from an ABLE account." (2025; sha256 2ad77023)

## (helper) — `person.x_hsa_value`

- **Authored helper label:** Value of your HSAs on December 31, 2025 (including 2025 contributions made in 2026)
- **Encoded (NonNegDollars):** Input — Total value of your HSAs on December 31, 2025, including contributions for 2025 that you made in 2026 (asked only when you have excess HSA contributions)
- Expr: `{"op":"input","source":"Total value of your HSAs on December 31, 2025, including contributions for 2025 that you made in 2026 (asked only when you have excess HSA contributions)"}`
- Cite: [f5329] p. 2, Part VII, line 49, "Additional tax. Enter 6% (0.06) of the smaller of line 48 or the value of your HSAs on December 31, 2025 (including 2025 contributions made in 2026)." (2025; sha256 2ad77023)

## (helper) — `person.x_hsa_excess`

- **Authored helper label:** This person's 2025 HSA excess contributions (Form 8889)
- **Encoded (NonNegDollars):** Add f8889.excess_amt over every confirmed f8889 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8889","field":"f8889.excess_amt","op":"sum_over"}`
- Cite: [i5329] p. 8, Line 47, "Enter the excess of your contributions (made by you or on your behalf) to your HSAs for 2025 from Form 8889, line 2 (unless withdrawn—discussed next), over your contribution limit (Form 8889, line 12)." (2025; sha256 aec3d325)
