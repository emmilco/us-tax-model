# Excess Social Security credit — separately per person

- Document: `person` (worksheet, tax year 2025)
- Collection: keyed entries; [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)
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
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025; Steps 1 to 3 (2025; sha256 da6f2f58)

## (helper) — `person.hsa_agreed`

- **Authored helper label:** This persons Form 8889 uses an agreed allocation under the spouse rule of line 6
- **Encoded (Count):** Add f8889.one over every confirmed f8889 entry for which helper "Spouses with separate HSAs, treated as having family coverage at any time during 2025" = true and helper "Do you and your spouse divide the family contribution limit equally, or by a different allocation you both agree on?" = 'agreed', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8889","field":"f8889.one","op":"sum_over","where":{"all":[{"eq":["f8889.split",{"const":true}],"op":"test"},{"eq":["f8889.allocation",{"const":"agreed"}],"op":"test"}],"op":"test"}}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025; Steps 1 to 3 (2025; sha256 da6f2f58)

## (helper) — `person.hsa_step1`

- **Authored helper label:** This persons Step 1 limit under the spouse rule of line 6
- **Encoded (NonNegDollars):** Add f8889.step1 over every confirmed f8889 entry for which helper "Spouses with separate HSAs, treated as having family coverage at any time during 2025" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8889","field":"f8889.step1","op":"sum_over","where":{"eq":["f8889.split",{"const":true}],"op":"test"}}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025; Steps 1 to 3 (2025; sha256 da6f2f58)

## (helper) — `person.hsa_share`

- **Authored helper label:** This persons part of the Step 1 limit under the spouse rule of line 6
- **Encoded (NonNegDollars):** Add f8889.share_raw over every confirmed f8889 entry for which helper "Spouses with separate HSAs, treated as having family coverage at any time during 2025" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8889","field":"f8889.share_raw","op":"sum_over","where":{"eq":["f8889.split",{"const":true}],"op":"test"}}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025; Steps 1 to 3 (2025; sha256 da6f2f58)

## (helper) — `person.hsa_deduction`

- **Authored helper label:** Form 8889 line 13 for this person
- **Encoded (NonNegDollars):** Add f8889.line13 over every confirmed f8889 entry, within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when person.hsa_repeated is true, cannot complete More than one Form 8889 for one person. Enter one Form 8889 per person, combining all of that person's own HSAs on it. A separate Form 8889 for each HSA (with a controlling Form 8889) is required only for an inherited HSA, which is outside this tool. Cite: [i8889] p. 3, "If, during the tax year, you are the beneficiary of two or more HSAs or you are a beneficiary of an HSA and you have your own HSA, you must complete a separate Form 8889 for each HSA" (2025; sha256 da6f2f58)
- Expr: `{"collection":"f8889","field":"f8889.line13","op":"sum_over"}`
- Cite: [i8889] p. 4, "Combine the amounts on line 13 of both Forms 8889 and enter this amount on Schedule 1 (Form 1040), line 13" (2025; sha256 da6f2f58)

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
- Cite: [f1040] Form 1040 (2025), line 25a (2025; created 2025-09-05; sha256 3d31c226)

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
- Cite: [f8959] Form 8959 (2025), lines 1–24; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004)

## (helper) — `person.medicare6`

- **Authored helper label:** Total W-2 box 6 for this person
- **Encoded (NonNegDollars):** Add w2.box6 over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when person.rrta is true, cannot complete Form 8959 RRTA computation. RRTA compensation is outside the supported wage-only path. Cite: [f8959] Form 8959 (2025), lines 1–24; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004)
- Expr: `{"collection":"w2","field":"w2.box6","op":"sum_over"}`
- Cite: [f8959] Form 8959 (2025), lines 1–24; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004)
