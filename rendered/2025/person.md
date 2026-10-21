# Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)

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
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":{"bind":{"line2":"person.se_line2","line8a":"person.wages"},"def":"se","line":"line6"}},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f1040sse] Schedule SE (2025), line 6; i8959 Line 8, "Schedule SE, line 6" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `person.se_line12`

- **Authored helper label:** Schedule SE line 12 (self-employment tax) for this person
- **Encoded (NonNegDollars):** Choose — [helper "This person has at least one Schedule C" = true → "line12" of Schedule SE (Form 1040) — Self-Employment Tax, one per person with line2 = helper "Schedule SE line 2 for this person" and line8a = line wages] [helper "This person has at least one Schedule C" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":{"bind":{"line2":"person.se_line2","line8a":"person.wages"},"def":"se","line":"line12"}},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f1040sse] Schedule SE (2025), line 12, "Enter here and on Schedule 2 (Form 1040), line 4" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `person.se_line13`

- **Authored helper label:** Schedule SE line 13 (deduction for one-half of self-employment tax) for this person
- **Encoded (NonNegDollars):** Choose — [helper "This person has at least one Schedule C" = true → "line13" of Schedule SE (Form 1040) — Self-Employment Tax, one per person with line2 = helper "Schedule SE line 2 for this person" and line8a = line wages] [helper "This person has at least one Schedule C" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":{"bind":{"line2":"person.se_line2","line8a":"person.wages"},"def":"se","line":"line13"}},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f1040sse] Schedule SE (2025), line 13, "Enter here and on Schedule 1 (Form 1040), line 15" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `person.se_line4c`

- **Authored helper label:** Schedule SE line 4c for this person
- **Encoded (NonNegDollars):** Choose — [helper "This person has at least one Schedule C" = true → "line4c" of Schedule SE (Form 1040) — Self-Employment Tax, one per person with line2 = helper "Schedule SE line 2 for this person" and line8a = line wages] [helper "This person has at least one Schedule C" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":{"bind":{"line2":"person.se_line2","line8a":"person.wages"},"def":"se","line":"line4c"}},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f1040sse] Schedule SE (2025), line 4c (2025; created 2025-05-07; sha256 05bc2b3e)

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

- **Authored helper label:** This person's retirement contributions are outside this tool
- **Encoded (Bool):** column (screen) (person.plan_screen) = true
- Expr: `{"eq":["person.plan_screen",{"const":true}],"op":"test"}`
- Cite: [p560] pp. 8–11, 14–17, 38–40, chapters 2, 3 and 5 (For use in preparing 2025 returns; sha256 1f1f7abe)

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
- **Refusal:** when person.plan_screened is true, cannot complete Retirement plan contributions outside this tool (SARSEP, other plan rates, higher SIMPLE limits, more than one plan, other elective deferrals, Roth contributions, excess contributions). These retirement contributions are outside this tool. Cite: [p560] pp. 8–11, 14–17, 38–40, chapters 2, 3 and 5 (For use in preparing 2025 returns; sha256 1f1f7abe)
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
- Cite: [p560] pp. 39–40, chapter 5, Deduction Worksheet for Self-Employed, Steps 4 and 5; Rate Table for Self-Employed (for example 10% gives 0.090909) (amb.2025.sep_rate_places) (For use in preparing 2025 returns; sha256 1f1f7abe)

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
- Cite: [p560] p. 39, chapter 5, "Enter your actual contribution, not to exceed your maximum deductible contribution"; chapter 2, Excess contributions (For use in preparing 2025 returns; sha256 1f1f7abe)

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
- Cite: [i1040gi] p. 93, Schedule 1, line 16, Self-Employed SEP, SIMPLE, and Qualified Plans; p560 chapter 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.s16`

- **Authored helper label:** Schedule 1 line 16 for this person
- **Encoded (NonNegDollars):** Choose — [helper "This person has at least one Schedule C" = true → helper "Self-employed SEP or SIMPLE deduction for this person"] [helper "This person has at least one Schedule C" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":"person.plan_deduction"},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 16, "If you were self-employed or a partner, you may be able to take this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.positive_profits`

- **Authored helper label:** Total of all net profits of this person's businesses (losses not included)
- **Encoded (NonNegDollars):** Add sc.profit_pos over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.profit_pos","op":"sum_over"}`
- Cite: [i7206] Line 5, Form 7206 (2025), "Don't include any net losses" (2025; sha256 9cbf92b3)

## (helper) — `person.sehi`

- **Authored helper label:** Self-employed health insurance deduction, this person
- **Encoded (NonNegDollars):** Add sc.f7206_line14 over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.f7206_line14","op":"sum_over"}`
- Cite: [f7206] Form 7206 (2025), line 14 (2025; created 2025-10-02; sha256 822203c9)

## (helper) — `person.qbi`

- **Authored helper label:** Qualified business income or loss of this person's businesses
- **Encoded (Dollars):** Add sc.qbi over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.qbi","op":"sum_over"}`
- Cite: [i8995] pp. 2, 4, Determining Your Qualified Business Income; Line 1 (2025; printed date 2026-01-26; sha256 875843ba)

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
