# IRA Deduction Worksheet — Schedule 1, Line 20

- Document: `ira` (worksheet, tax year 2025)
- Note: Columns "Your IRA" and "Spouse's IRA" (a joint return); each column's facts and lines 2, 6, 7, 11 and 12 are that person's (person.ira_*), and lines 3 to 5 and 8 to 10 are figured once for the return. Contributions to both a traditional and a Roth IRA on a joint return, line 10 under the Kay Bailey Hutchison amounts, excess or recharacterized contributions, nonqualified deferred compensation, fellowships not on a Form W-2, reservist repayments, difficulty of care payments, nontaxable combat pay, nondeductible contributions with a 2025 distribution or conversion, and the election to deduct less than the most you can are refused. A placeholder stands for each Schedule 1 line another part of the stage computes (2a, 18, 19a, 25).

## (helper) — `ira.zero`

- **Authored helper label:** Zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.joint`

- **Authored helper label:** Married filing jointly
- **Encoded (Bool):** f1040 line Filing Status = 'mfj'
- Expr: `{"eq":["f1040.status",{"const":"mfj"}],"op":"test"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "If married filing jointly, was your spouse covered by a retirement plan?" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.joint_type`

- **Authored helper label:** Married filing jointly or qualifying surviving spouse
- **Encoded (Bool):** (f1040 line Filing Status = 'mfj' or f1040 line Filing Status = 'qss')
- Expr: `{"any":[{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},{"eq":["f1040.status",{"const":"qss"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "If married filing jointly or qualifying surviving spouse" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.contrib_total`

- **Authored helper label:** Traditional IRA contributions for 2025 on this return (you and your spouse)
- **Encoded (NonNegDollars):** Add person.ira_contrib over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.ira_contrib","op":"sum_over"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 11 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.roth_total`

- **Authored helper label:** Roth IRA contributions for 2025 on this return (you and your spouse)
- **Encoded (NonNegDollars):** Add person.sav_roth over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.sav_roth","op":"sum_over"}`
- Cite: [i1040gi] p. 95, Line 20, "You can’t deduct contributions to a Roth IRA" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.any_trad`

- **Authored helper label:** Anyone on the return made traditional IRA contributions for 2025
- **Encoded (Bool):** helper "Traditional IRA contributions for 2025 on this return (you and your spouse)" > $0 (sales.zero)
- Expr: `{"gt":["ira.contrib_total",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 95, Line 20, "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.cov_count`

- **Authored helper label:** Number of persons on the return covered by a retirement plan
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Covered by a retirement plan (worksheet line 1a or 1b for this person)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Interpretation: amb.2025.ira_covered
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"eq":["person.ira_cov",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.anyone_covered`

- **Authored helper label:** You (or, on a joint return, your spouse) were covered by a retirement plan (Yes on line 1a or 1b)
- **Encoded (Bool):** helper "Number of persons on the return covered by a retirement plan" > 0 (a count)
- Expr: `{"gt":["ira.cov_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "If you checked “No” on line 1a (and “No” on line 1b if married filing jointly), skip lines 2 through 6" and "Otherwise, go to line 2" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.lines2to6`

- **Authored helper label:** Lines 2 through 6 are completed (traditional IRA contributions, and someone is covered by a retirement plan)
- **Encoded (Bool):** helper "Anyone on the return made traditional IRA contributions for 2025" = true and helper "You (or, on a joint return, your spouse) were covered by a retirement plan (Yes on line 1a or 1b)" = true
- Expr: `{"all":[{"eq":["ira.any_trad",{"const":true}],"op":"test"},{"eq":["ira.anyone_covered",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "skip lines 2 through 6" and "Otherwise, go to line 2" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `ira.cov_gate`

- **Authored helper label:** Social security benefits, traditional IRA contributions for 2025, and you or your spouse covered by a retirement plan
- **Encoded (Bool):** ssb helper "Any social security benefits (otherwise the worksheet is not needed)" = true and helper "Anyone on the return made traditional IRA contributions for 2025" = true and helper "You (or, on a joint return, your spouse) were covered by a retirement plan (Yes on line 1a or 1b)" = true
- Interpretation: amb.2025.ira_ssb_copy
- Expr: `{"all":[{"eq":["ssb.has_benefits",{"const":true}],"op":"test"},{"eq":["ira.any_trad",{"const":true}],"op":"test"},{"eq":["ira.anyone_covered",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 31, Lines 6a and 6b, Exception (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.cov_you`

- **Authored helper label:** You were covered by a retirement plan (1 if Yes)
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'taxpayer' and helper "Covered by a retirement plan (worksheet line 1a or 1b for this person)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"all":[{"eq":["person.role",{"const":"taxpayer"}],"op":"test"},{"eq":["person.ira_cov",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 1a (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.cov_spouse`

- **Authored helper label:** Your spouse was covered by a retirement plan (1 if Yes)
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'spouse' and helper "Covered by a retirement plan (worksheet line 1a or 1b for this person)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"all":[{"eq":["person.role",{"const":"spouse"}],"op":"test"},{"eq":["person.ira_cov",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 1b (2025; printed date 2026-02-25; sha256 482e9c48)

## 1a — `ira.line1a`

- **IRS:** Were you covered by a retirement plan (see Were You Covered by a Retirement Plan)?
- **Encoded (Bool):** helper "Anyone on the return made traditional IRA contributions for 2025" = true and helper "You were covered by a retirement plan (1 if Yes)" > 0 (a count)
- Expr: `{"all":[{"eq":["ira.any_trad",{"const":true}],"op":"test"},{"gt":["ira.cov_you",{"const":0,"type":"Count"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 1a, "Were you covered by a retirement plan (see Were You Covered by a Retirement Plan)?" (2025; printed date 2026-02-25; sha256 482e9c48)

## 1b — `ira.line1b`

- **IRS:** If married filing jointly, was your spouse covered by a retirement plan?
- **Encoded (Bool):** helper "Anyone on the return made traditional IRA contributions for 2025" = true and helper "Your spouse was covered by a retirement plan (1 if Yes)" > 0 (a count)
- Expr: `{"all":[{"eq":["ira.any_trad",{"const":true}],"op":"test"},{"gt":["ira.cov_spouse",{"const":0,"type":"Count"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 1b, "If married filing jointly, was your spouse covered by a retirement plan?" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.line2a_sum`

- **Authored helper label:** Line 2, your column
- **Encoded (NonNegDollars):** Add person.ira_line2 over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'taxpayer', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.ira_line2","op":"sum_over","where":{"eq":["person.role",{"const":"taxpayer"}],"op":"test"}}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.line2b_sum`

- **Authored helper label:** Line 2, your spouse's column
- **Encoded (NonNegDollars):** Add person.ira_line2 over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'spouse', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.ira_line2","op":"sum_over","where":{"eq":["person.role",{"const":"spouse"}],"op":"test"}}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## 2a — `ira.line2a`

- **IRS:** Enter the amount shown below that applies to you (your IRA)
- **Encoded (NonNegDollars):** Choose — [helper "Lines 2 through 6 are completed (traditional IRA contributions, and someone is covered by a retirement plan)" = true → helper "Line 2, your column"] [helper "Lines 2 through 6 are completed (traditional IRA contributions, and someone is covered by a retirement plan)" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["ira.lines2to6",{"const":true}],"op":"test"},"then":"ira.line2a_sum"},{"guard":{"eq":["ira.lines2to6",{"const":false}],"op":"test"},"then":"ira.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 2, "Enter the amount shown below that applies to you" (2025; printed date 2026-02-25; sha256 482e9c48)

## 2b — `ira.line2b`

- **IRS:** Enter the amount shown below that applies to you (your spouse's IRA)
- **Encoded (NonNegDollars):** Choose — [helper "Lines 2 through 6 are completed (traditional IRA contributions, and someone is covered by a retirement plan)" = true → helper "Line 2, your spouse's column"] [helper "Lines 2 through 6 are completed (traditional IRA contributions, and someone is covered by a retirement plan)" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["ira.lines2to6",{"const":true}],"op":"test"},"then":"ira.line2b_sum"},{"guard":{"eq":["ira.lines2to6",{"const":false}],"op":"test"},"then":"ira.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 2, "Married filing jointly, enter $146,000 in both columns" (2025; printed date 2026-02-25; sha256 482e9c48)

## 3 — `ira.line3`

- **IRS:** Enter the amount from Form 1040 or 1040-SR, line 9
- **Encoded (Dollars):** Enter the amount from f1040 line 9.
- Expr: `{"from":"f1040.line9","op":"copy"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 3, "Enter the amount from Form 1040 or 1040-SR, line 9" (2025; printed date 2026-02-25; sha256 482e9c48)

## 4 — `ira.line4`

- **IRS:** Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25
- **Encoded (NonNegDollars):** Add s1 line 11, s1 line 13, s1 line 15, s1 line 16, s1 line 17, s1 line 18, s1 line 19a, and s1 line 25.
- Expr: `{"of":["s1.line11","s1.line13","s1.line15","s1.line16","s1.line17","s1.line18","s1.line19a","s1.line25"],"op":"sum"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 4, "Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25" (lines 12, 14 and 23 are outside this tool and refused by scope.schedule1) (2025; printed date 2026-02-25; sha256 482e9c48)

## 5 — `ira.line5`

- **IRS:** Subtract line 4 from line 3. If married filing jointly, enter the result in both columns
- **Encoded (Dollars):** Subtract line 4 from line 3.
- Expr: `{"from":"ira.line3","op":"subtract","take":"ira.line4"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 5, "Subtract line 4 from line 3. If married filing jointly, enter the result in both columns" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.line6a_sum`

- **Authored helper label:** Line 6, your column
- **Encoded (NonNegDollars):** Add person.ira_line6 over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'taxpayer', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.ira_line6","op":"sum_over","where":{"eq":["person.role",{"const":"taxpayer"}],"op":"test"}}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.line6b_sum`

- **Authored helper label:** Line 6, your spouse's column
- **Encoded (NonNegDollars):** Add person.ira_line6 over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'spouse', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.ira_line6","op":"sum_over","where":{"eq":["person.role",{"const":"spouse"}],"op":"test"}}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6 (2025; printed date 2026-02-25; sha256 482e9c48)

## 6a — `ira.line6a`

- **IRS:** Is the amount on line 5 less than the amount on line 2? If yes, subtract line 5 from line 2 (your IRA); if no, none of your IRA contributions are deductible
- **Encoded (NonNegDollars):** Choose — [helper "Lines 2 through 6 are completed (traditional IRA contributions, and someone is covered by a retirement plan)" = true → helper "Line 6, your column"] [helper "Lines 2 through 6 are completed (traditional IRA contributions, and someone is covered by a retirement plan)" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["ira.lines2to6",{"const":true}],"op":"test"},"then":"ira.line6a_sum"},{"guard":{"eq":["ira.lines2to6",{"const":false}],"op":"test"},"then":"ira.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "Is the amount on line 5 less than the amount on line 2?" and "Subtract line 5 from line 2 in each column" (2025; printed date 2026-02-25; sha256 482e9c48)

## 6b — `ira.line6b`

- **IRS:** Is the amount on line 5 less than the amount on line 2? If yes, subtract line 5 from line 2 (your spouse's IRA)
- **Encoded (NonNegDollars):** Choose — [helper "Lines 2 through 6 are completed (traditional IRA contributions, and someone is covered by a retirement plan)" = true → helper "Line 6, your spouse's column"] [helper "Lines 2 through 6 are completed (traditional IRA contributions, and someone is covered by a retirement plan)" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["ira.lines2to6",{"const":true}],"op":"test"},"then":"ira.line6b_sum"},{"guard":{"eq":["ira.lines2to6",{"const":false}],"op":"test"},"then":"ira.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "Subtract line 5 from line 2 in each column" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.line7a_sum`

- **Authored helper label:** Line 7, your column
- **Encoded (NonNegDollars):** Add person.ira_line7 over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'taxpayer', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.ira_line7","op":"sum_over","where":{"eq":["person.role",{"const":"taxpayer"}],"op":"test"}}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.line7b_sum`

- **Authored helper label:** Line 7, your spouse's column
- **Encoded (NonNegDollars):** Add person.ira_line7 over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'spouse', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.ira_line7","op":"sum_over","where":{"eq":["person.role",{"const":"spouse"}],"op":"test"}}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7 (2025; printed date 2026-02-25; sha256 482e9c48)

## 7a — `ira.line7a`

- **IRS:** Multiply line 6a by the percentage that applies to you, increased to a multiple of $10 and at least $200 (or the applicable amount, when lines 2 through 6 are skipped or line 6 is at or above the threshold) (your IRA)
- **Encoded (NonNegDollars):** Choose — [helper "Anyone on the return made traditional IRA contributions for 2025" = true → helper "Line 7, your column"] [helper "Anyone on the return made traditional IRA contributions for 2025" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["ira.any_trad",{"const":true}],"op":"test"},"then":"ira.line7a_sum"},{"guard":{"eq":["ira.any_trad",{"const":false}],"op":"test"},"then":"ira.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "Multiply lines 6a and 6b by the percentage below that applies to you" (2025; printed date 2026-02-25; sha256 482e9c48)

## 7b — `ira.line7b`

- **IRS:** Multiply line 6b by the percentage that applies to you, increased to a multiple of $10 and at least $200 (or the applicable amount) (your spouse's IRA)
- **Encoded (NonNegDollars):** Choose — [helper "Anyone on the return made traditional IRA contributions for 2025" = true → helper "Line 7, your spouse's column"] [helper "Anyone on the return made traditional IRA contributions for 2025" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["ira.any_trad",{"const":true}],"op":"test"},"then":"ira.line7b_sum"},{"guard":{"eq":["ira.any_trad",{"const":false}],"op":"test"},"then":"ira.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "Multiply lines 6a and 6b by the percentage below that applies to you" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.wages`

- **Authored helper label:** Wages, salaries, tips, etc. (box 1 of the Forms W-2 of you and your spouse)
- **Encoded (NonNegDollars):** Add person.box1 over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.box1","op":"sum_over"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 8, "Wages, salaries, tips, etc. Generally, this is the amount reported in box 1 of Form W-2" (2025; printed date 2026-02-25; sha256 482e9c48)

## 8 — `ira.line8`

- **IRS:** Enter the total of your (and your spouse's if filing jointly): wages, salaries, tips, etc.; alimony and separate maintenance payments reported on Schedule 1, line 2a; and nontaxable combat pay
- **Encoded (NonNegDollars):** Add helper "Wages, salaries, tips, etc. (box 1 of the Forms W-2 of you and your spouse)" and s1 line 2a.
- Expr: `{"of":["ira.wages","s1.line2a"],"op":"sum"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 8, "Enter the total of your (and your spouse’s if filing jointly)" (nontaxable combat pay is refused, ira.combat_gate) (2025; printed date 2026-02-25; sha256 482e9c48)

## 9 — `ira.line9`

- **IRS:** Enter the earned income you (and your spouse if filing jointly) received as a self-employed individual or a partner, minus any deductions on Schedule 1, lines 15 and 16. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Add person.ira_se over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Interpretation: amb.2025.ira_se_floor
- Expr: `{"collection":"person","field":"person.ira_se","op":"sum_over"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 9, "Enter the earned income you (and your spouse if filing jointly) received as a self-employed individual or a partner" and "If zero or less, enter -0-" (2025; printed date 2026-02-25; sha256 482e9c48)

## 10 — `ira.line10`

- **IRS:** Add lines 8 and 9
- **Encoded (NonNegDollars):** Add line 8 and line 9.
- Expr: `{"of":["ira.line8","ira.line9"],"op":"sum"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 10, "Add lines 8 and 9" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.age50_count`

- **Authored helper label:** Number of spouses age 50 or older at the end of 2025
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Were you age 50 or older at the end of 2025?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"eq":["person.ira_age50",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, Caution, "($15,000 if one spouse is age 50 or older at the end of 2025; $16,000 if both spouses are age 50 or older at the end of 2025)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.kbh_none`

- **Authored helper label:** $14,000
- **Encoded (NonNegDollars):** Enter $14,000 (ira.kbh_none).
- Expr: `{"op":"param","ref":"ira.kbh_none"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, Caution, "If married filing jointly and line 10 is less than $14,000" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.kbh_one`

- **Authored helper label:** $15,000
- **Encoded (NonNegDollars):** Enter $15,000 (ira.kbh_one).
- Expr: `{"op":"param","ref":"ira.kbh_one"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, Caution, "($15,000 if one spouse is age 50 or older at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.kbh_both`

- **Authored helper label:** $16,000
- **Encoded (NonNegDollars):** Enter $16,000 (ira.kbh_both).
- Expr: `{"op":"param","ref":"ira.kbh_both"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, Caution, "$16,000 if both spouses are age 50 or older at the end of 2025)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.kbh_amount`

- **Authored helper label:** The amount in the caution below line 10 ($14,000; $15,000 if one spouse is age 50 or older; $16,000 if both are)
- **Encoded (NonNegDollars):** Choose — [helper "Number of spouses age 50 or older at the end of 2025" ≥ 0 (a count) and helper "Number of spouses age 50 or older at the end of 2025" < 1 (a count) → helper "$14,000"] [helper "Number of spouses age 50 or older at the end of 2025" ≥ 1 (a count) and helper "Number of spouses age 50 or older at the end of 2025" < 2 (a count) → helper "$15,000"] [helper "Number of spouses age 50 or older at the end of 2025" ≥ 2 (a count) → helper "$16,000"]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["ira.age50_count",{"const":0,"type":"Count"}],"op":"test"},{"lt":["ira.age50_count",{"const":1,"type":"Count"}],"op":"test"}],"op":"test"},"then":"ira.kbh_none"},{"guard":{"all":[{"ge":["ira.age50_count",{"const":1,"type":"Count"}],"op":"test"},{"lt":["ira.age50_count",{"const":2,"type":"Count"}],"op":"test"}],"op":"test"},"then":"ira.kbh_one"},{"guard":{"ge":["ira.age50_count",{"const":2,"type":"Count"}],"op":"test"},"then":"ira.kbh_both"}],"op":"choose"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, Caution, "If married filing jointly and line 10 is less than $14,000 ($15,000 if one spouse is age 50 or older at the end of 2025; $16,000 if both spouses are age 50 or older at the end of 2025)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `ira.kbh_short`

- **Authored helper label:** Married filing jointly with traditional IRA contributions and line 10 less than the amount in the caution
- **Encoded (Bool):** helper "Anyone on the return made traditional IRA contributions for 2025" = true and helper "Married filing jointly" = true and line 10 < helper "The amount in the caution below line 10 ($14,000; $15,000 if one spouse is age 50 or older; $16,000 if both are)"
- Expr: `{"all":[{"eq":["ira.any_trad",{"const":true}],"op":"test"},{"eq":["ira.joint",{"const":true}],"op":"test"},{"lt":["ira.line10","ira.kbh_amount"],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, Caution, "stop here and use the worksheet in Pub. 590-A to figure your IRA deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `ira.both_kinds`

- **Authored helper label:** A joint return on which you or your spouse made contributions to both a traditional IRA and a Roth IRA for 2025
- **Encoded (Bool):** helper "Married filing jointly" = true and helper "Anyone on the return made traditional IRA contributions for 2025" = true and helper "Roth IRA contributions for 2025 on this return (you and your spouse)" > $0 (sales.zero)
- Interpretation: amb.2025.ira_both_kinds
- Expr: `{"all":[{"eq":["ira.joint",{"const":true}],"op":"test"},{"eq":["ira.any_trad",{"const":true}],"op":"test"},{"gt":["ira.roth_total",{"param":"sales.zero"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 95, Line 20, "If you are filing a joint return and you or your spouse made contributions to both a traditional IRA and a Roth IRA for 2025, don’t use the IRA Deduction Worksheet in these instructions" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.all_total`

- **Authored helper label:** Traditional and Roth IRA contributions for 2025 on this return
- **Encoded (NonNegDollars):** Add helper "Traditional IRA contributions for 2025 on this return (you and your spouse)" and helper "Roth IRA contributions for 2025 on this return (you and your spouse)".
- Expr: `{"of":["ira.contrib_total","ira.roth_total"],"op":"sum"}`
- Cite: [i8606] p. 5, Overall Contribution Limit for Traditional and Roth IRAs, "your limit on contributions to traditional and Roth IRAs is generally the smaller of $7,000 ($8,000 if age 50 or older at the end of 2025) or your taxable compensation" (2025; sha256 735fb7ae)

## (gate) — `ira.over_comp`

- **Authored helper label:** Traditional and Roth IRA contributions for 2025 more than the compensation on line 10
- **Encoded (Bool):** helper "Anyone on the return made traditional IRA contributions for 2025" = true and helper "Traditional and Roth IRA contributions for 2025 on this return" > line 10
- Expr: `{"all":[{"eq":["ira.any_trad",{"const":true}],"op":"test"},{"gt":["ira.all_total","ira.line10"],"op":"test"}],"op":"test"}`
- Cite: [p590a] p. 35, Excess Contributions, "Generally, an excess contribution is the amount contributed to your traditional IRAs for the year that is more than the smaller of: • $7,000 ($8,000 if you are age 50 or older), or • Your taxable compensation for the year" (2025; sha256 ca0e4287)

## (screen) — `ira.special`

- **Authored helper label:** Does any of these apply to you or your spouse (the IRA deduction special cases)?
- **Encoded (Bool):** Input — Does any of these apply to you (or your spouse on a joint return): income from a nonqualified deferred compensation plan or a nongovernmental section 457 plan (an amount in box 11 of your Form W-2, in box 12 with code Z, or in box 15 of Form 1099-MISC); taxable non-tuition fellowship or stipend payments for graduate or postdoctoral study not reported on a Form W-2; a repayment to an IRA of a qualified reservist distribution; or difficulty of care payments (qualified foster care payments) used to increase your nondeductible IRA contribution limit?
- Interpretation: amb.2025.ira_fellowship
- Expr: `{"op":"input","source":"Does any of these apply to you (or your spouse on a joint return): income from a nonqualified deferred compensation plan or a nongovernmental section 457 plan (an amount in box 11 of your Form W-2, in box 12 with code Z, or in box 15 of Form 1099-MISC); taxable non-tuition fellowship or stipend payments for graduate or postdoctoral study not reported on a Form W-2; a repayment to an IRA of a qualified reservist distribution; or difficulty of care payments (qualified foster care payments) used to increase your nondeductible IRA contribution limit?"}`
- Cite: [i1040gi] p. 95, Line 20, "The income should be shown in (a) box 11 of your Form W-2, (b) box 12 of your Form W-2 with code Z, or (c) box 15 of Form 1099-MISC" and "Don’t include any repayments of qualified reservist distributions"; p590a p. 6, What Is Compensation?, "certain non-tuition fellowship and stipend payments not reported to you on Form W-2 are treated as taxable compensation for IRA purposes"; p590a p. 16, Difficulty of care payments (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `ira.special_gate`

- **Authored helper label:** Traditional IRA contributions with an IRA deduction special case (screen)
- **Encoded (Bool):** helper "Anyone on the return made traditional IRA contributions for 2025" = true and column (screen) (ira.special) = true
- Expr: `{"all":[{"eq":["ira.any_trad",{"const":true}],"op":"test"},{"eq":["ira.special",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 95, Line 20, "But read the following list before you fill in the worksheet" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `ira.combat_gate`

- **Authored helper label:** Traditional IRA contributions with nontaxable combat pay
- **Encoded (Bool):** helper "Anyone on the return made traditional IRA contributions for 2025" = true and s8812 helper "Any nontaxable combat pay (Form W-2, box 12, code Q)?" = true
- Expr: `{"all":[{"eq":["ira.any_trad",{"const":true}],"op":"test"},{"eq":["s8812.combat_pay",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 95, Line 20, "If you were a member of the U.S. Armed Forces, earned income includes any nontaxable combat pay you received" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `ira.excl_gate`

- **Authored helper label:** Traditional IRA contributions, someone covered by a retirement plan, and Form 2555 or 4563 or income excluded as a bona fide resident of Puerto Rico
- **Encoded (Bool):** helper "Anyone on the return made traditional IRA contributions for 2025" = true and helper "You (or, on a joint return, your spouse) were covered by a retirement plan (Yes on line 1a or 1b)" = true and sa helper "Are you filing Form 2555 or Form 4563, or do you have income excluded as a bona fide resident of Puerto Rico?" = true
- Expr: `{"all":[{"eq":["ira.any_trad",{"const":true}],"op":"test"},{"eq":["ira.anyone_covered",{"const":true}],"op":"test"},{"eq":["sa.excluded_income",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 96, Were You Covered by a Retirement Plan?, "If you were covered by a retirement plan and you file Form 2555 or 8815, or you exclude employer-provided adoption benefits, see Pub. 590-A to figure the amount, if any, of your IRA deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## 11a — `ira.line11a`

- **IRS:** Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions, for 2025 to your IRA
- **Encoded (NonNegDollars):** Add person.ira_contrib over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'taxpayer', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.ira_contrib","op":"sum_over","where":{"eq":["person.role",{"const":"taxpayer"}],"op":"test"}}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 11, "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions (April 15, 2026, for most people), for 2025 to your IRA on line 11a" (2025; printed date 2026-02-25; sha256 482e9c48)

## 11b — `ira.line11b`

- **IRS:** Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions, for 2025 to your spouse's IRA
- **Encoded (NonNegDollars):** Add person.ira_contrib over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'spouse', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.ira_contrib","op":"sum_over","where":{"eq":["person.role",{"const":"spouse"}],"op":"test"}}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 11, "and to your spouse’s IRA on line 11b" (2025; printed date 2026-02-25; sha256 482e9c48)

## 12a — `ira.line12a`

- **IRS:** Enter the smallest of line 7a, 10, or 11a. This is the most you can deduct (your IRA)
- **Encoded (NonNegDollars):** Add person.ira_deduction over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'taxpayer', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.ira_deduction","op":"sum_over","where":{"eq":["person.role",{"const":"taxpayer"}],"op":"test"}}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 12, "On line 12a, enter the smallest of line 7a, 10, or 11a" (2025; printed date 2026-02-25; sha256 482e9c48)

## 12b — `ira.line12b`

- **IRS:** Enter the smallest of line 7b, 10, or 11b. This is the most you can deduct (your spouse's IRA)
- **Encoded (NonNegDollars):** Add person.ira_deduction over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'spouse', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.ira_deduction","op":"sum_over","where":{"eq":["person.role",{"const":"spouse"}],"op":"test"}}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 12, "On line 12b, enter the smallest of line 7b, 10, or 11b" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.total`

- **Authored helper label:** Add the amounts on lines 12a and 12b
- **Encoded (NonNegDollars):** Add person.ira_deduction over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.ira_deduction","op":"sum_over"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 12, "Add the amounts on lines 12a and 12b and enter the total on Schedule 1, line 20" (2025; printed date 2026-02-25; sha256 482e9c48)

## (screen) — `ira.deduct_less`

- **Authored helper label:** Do you want to deduct less than the most you can deduct, treating the rest as a nondeductible contribution?
- **Encoded (Bool):** Input — The most you (and your spouse) can deduct for your traditional IRA contributions is figured on line 12 of the IRA Deduction Worksheet. Do you want to deduct a smaller amount and treat the rest as a nondeductible contribution?
- Interpretation: amb.2025.ira_deduct_less
- Expr: `{"op":"input","source":"The most you (and your spouse) can deduct for your traditional IRA contributions is figured on line 12 of the IRA Deduction Worksheet. Do you want to deduct a smaller amount and treat the rest as a nondeductible contribution?"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 12, "Or, if you want, you can deduct a smaller amount and treat the rest as a nondeductible contribution (see Form 8606)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `ira.less_gate`

- **Authored helper label:** An IRA deduction above zero and the election to deduct less
- **Encoded (Bool):** helper "Add the amounts on lines 12a and 12b" > $0 (sales.zero) and column (screen) (ira.deduct_less) = true
- Expr: `{"all":[{"gt":["ira.total",{"param":"sales.zero"}],"op":"test"},{"eq":["ira.deduct_less",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [p590a] p. 16, Form 8606, "When you file, you can even designate otherwise deductible contributions as nondeductible contributions" (2025; sha256 ca0e4287)

## (helper) — `ira.line20`

- **Authored helper label:** The total of lines 12a and 12b for Schedule 1, line 20
- **Encoded (NonNegDollars):** Enter the amount from helper "Add the amounts on lines 12a and 12b".
- **Refusal:** when ira.less_gate is true, cannot complete An IRA deduction smaller than the most you can deduct (Form 8606). Deducting less than the most you can and treating the rest as nondeductible is outside this tool; the tool takes the most you can deduct. Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 12, "Or, if you want, you can deduct a smaller amount and treat the rest as a nondeductible contribution (see Form 8606)" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"from":"ira.total","op":"copy"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 12, "Add the amounts on lines 12a and 12b and enter the total on Schedule 1, line 20" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `ira.basis_total`

- **Authored helper label:** Total basis in traditional IRAs on the Forms 8606 of this return (line 14 of each); a target of the interview, so that each Form 8606 is completed
- **Encoded (NonNegDollars):** Add person.ira_8606_line14 over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.ira_8606_line14","op":"sum_over"}`
- Cite: [f8606] Form 8606 (2025), line 14, "This is your total basis in traditional IRAs for 2025 and earlier years" (2025; sha256 748a2bf2)
