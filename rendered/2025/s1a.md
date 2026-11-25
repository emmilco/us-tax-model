# Schedule 1-A (Form 1040) — Additional Deductions

- Document: `s1a` (form, tax year 2025)
- Note: For any filing status; a married filing separately return takes no deduction on lines 13, 21 and 36a (tips, overtime, enhanced senior), as the instructions require. Tips and overtime as an employee only, by the methods the instructions give for 2025; tips or overtime in a trade or business, Form 4137, and excluded Puerto Rico income or Forms 2555 and 4563 are refused. Lines 11, 19 and 28 (a whole number of $1,000 units) are kept as that many thousands of dollars; lines 12, 20 and 29 multiply them by $100 or $200 per thousand.

## (helper) — `s1a.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [f1040s1a] Schedule 1-A (2025) (2025; created 2025-11-04; sha256 64f97b38)

## 1 — `s1a.line1`

- **IRS:** Enter the amount from Form 1040, 1040-SR, or 1040-NR, line 11b
- **Encoded (Dollars):** Enter the amount from f1040 line 11b.
- Expr: `{"from":"f1040.line11b","op":"copy"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 1 (2025; created 2025-11-04; sha256 64f97b38)

## 2a — `s1a.line2a`

- **IRS:** Enter any income from Puerto Rico that you excluded
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule 1-A, Part I, lines 2a to 2d (excluded Puerto Rico income, Form 2555, Form 4563). Modified AGI with excluded Puerto Rico income or Form 2555 or 4563 amounts is outside this tool. Cite: [i1040gi] p. 101, Schedule 1-A, Part I, "If you do have excluded income from Puerto Rico, or you are filing Form 2555 or 4563, complete lines 2a through 2e" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part I; Schedule 1-A (2025), line 2a (zero unless refused through sa.excluded_income) (2025; printed date 2026-02-25; sha256 482e9c48)

## 2b — `s1a.line2b`

- **IRS:** Enter the amount from Form 2555, line 45
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part I; Schedule 1-A (2025), line 2b (zero unless refused through sa.excluded_income) (2025; printed date 2026-02-25; sha256 482e9c48)

## 2c — `s1a.line2c`

- **IRS:** Enter the amount from Form 2555, line 50
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part I; Schedule 1-A (2025), line 2c (zero unless refused through sa.excluded_income) (2025; printed date 2026-02-25; sha256 482e9c48)

## 2d — `s1a.line2d`

- **IRS:** Enter the amount from Form 4563, line 15
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part I; Schedule 1-A (2025), line 2d (zero unless refused through sa.excluded_income) (2025; printed date 2026-02-25; sha256 482e9c48)

## 2e — `s1a.line2e`

- **IRS:** Add lines 2a, 2b, 2c, and 2d
- **Encoded (NonNegDollars):** Add line 2a, line 2b, line 2c, and line 2d.
- Expr: `{"of":["s1a.line2a","s1a.line2b","s1a.line2c","s1a.line2d"],"op":"sum"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 2e (2025; created 2025-11-04; sha256 64f97b38)

## 3 — `s1a.line3`

- **IRS:** Add lines 1 and 2e
- **Encoded (Dollars):** Add line 1 and line 2e.
- Expr: `{"of":["s1a.line1","s1a.line2e"],"op":"sum"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 3 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.tips`

- **Authored helper label:** Did you (or, on a joint return, your spouse) receive qualified tips as an employee in 2025 that you want to deduct?
- **Encoded (Bool):** Input — Did you (or, on a joint return, your spouse) receive tips as an employee in 2025 in an occupation on the IRS list of occupations that customarily and regularly received tips (IRS.gov/TippedOccupations) that you want to deduct on Schedule 1-A, Part II? (Tips received as a non-employee, in your own trade or business, are asked about with Schedule C.)
- Expr: `{"op":"input","source":"Did you (or, on a joint return, your spouse) receive tips as an employee in 2025 in an occupation on the IRS list of occupations that customarily and regularly received tips (IRS.gov/TippedOccupations) that you want to deduct on Schedule 1-A, Part II? (Tips received as a non-employee, in your own trade or business, are asked about with Schedule C.)"}`
- Cite: [i1040gi] pp. 101-103, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if", "You (and/or your spouse if filing a joint return) received qualified tips" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tip_employers`

- **Authored helper label:** Number of employers on the Qualified Tips From More Than One Employer Worksheet
- **Encoded (Count):** Add person.tip_employers over every confirmed person entry for which helper "Do you have an SSN valid for employment issued before the due date of your return?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.tip_employers","op":"sum_over","where":{"eq":["person.work_ssn",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 4c (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tip_total`

- **Authored helper label:** Worksheet line 2. Add lines 1A through 1E, column (d)
- **Encoded (NonNegDollars):** Add person.tip_total over every confirmed person entry for which helper "Do you have an SSN valid for employment issued before the due date of your return?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.tip_total","op":"sum_over","where":{"eq":["person.work_ssn",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 104, Qualified Tips From More Than One Employer Worksheet, line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tip_reported`

- **Authored helper label:** Worksheet column (b) total: qualified tips reported on Form W-2 or on Forms 4070
- **Encoded (NonNegDollars):** Add person.tip_reported over every confirmed person entry for which helper "Do you have an SSN valid for employment issued before the due date of your return?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.tip_reported","op":"sum_over","where":{"eq":["person.work_ssn",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 104, Qualified Tips From More Than One Employer Worksheet, column (b); p. 103, paragraphs 1 through 3, "Enter this amount on line 4a" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tip_multi`

- **Authored helper label:** Tips from more than one employer
- **Encoded (Bool):** helper "Number of employers on the Qualified Tips From More Than One Employer Worksheet" > 1 (ss.one)
- Expr: `{"gt":["s1a.tip_employers",{"param":"ss.one"}],"op":"test"}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 4a, "If you received qualified tips as an employee with respect to employment with more than one employer, enter -0- on line 4a" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tips_over_count`

- **Authored helper label:** Number of people with a valid SSN whose qualified tips entered are more than their Medicare wages and tips (W-2 box 5)
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Do you have an SSN valid for employment issued before the due date of your return?" = true and helper "The qualified tips reported on this person's Forms W-2 or 4070 (worksheet column (b)) are more than the person's Medicare wages and tips (W-2 box 5), of which they are a part" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"all":[{"eq":["person.work_ssn",{"const":true}],"op":"test"},{"eq":["person.tips_over_wages",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [f1040s1a] p. 1, line 4a, "Enter qualified tips included on Form W-2, box 7"; fw2 p. 7, Box 6, "all Medicare wages and tips shown in box 5" (2025; created 2025-11-04; sha256 64f97b38)

## (gate) — `s1a.tips_over_wages`

- **Authored helper label:** For someone on the return, the qualified tips entered are more than the Medicare wages and tips (W-2 box 5) that include them (not tested on a return with Form 4137 tips, which is refused at s1a.f4137)
- **Encoded (Bool):** helper "Someone on the return has tips on Form 4137" = false and helper "Number of people with a valid SSN whose qualified tips entered are more than their Medicare wages and tips (W-2 box 5)" > 0 (a count)
- Expr: `{"all":[{"eq":["s1a.f4137",{"const":false}],"op":"test"},{"gt":["s1a.tips_over_count",{"const":0,"type":"Count"}],"op":"test"}],"op":"test"}`
- Cite: [f1040s1a] p. 1, line 4a, "Enter qualified tips included on Form W-2, box 7"; fw2 p. 7, Box 6, "all Medicare wages and tips shown in box 5" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.tip_ssn_count`

- **Authored helper label:** Number of people with a valid SSN who received qualified tips
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Do you have an SSN valid for employment issued before the due date of your return?" = true and helper "Number of employers that paid this person qualified tips" > 0 (a count), within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"all":[{"eq":["person.work_ssn",{"const":true}],"op":"test"},{"gt":["person.tip_employers",{"const":0,"type":"Count"}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if" and "If you are married filing a joint return, the spouse who received the qualified tips must have a valid SSN" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tip_ssn`

- **Authored helper label:** You have a valid SSN or, if married filing jointly, a spouse who received them has a valid SSN
- **Encoded (Bool):** (f1040 line Filing Status ≠ 'mfj' and household helper "Do you have an SSN valid for employment issued before the due date of your return?" = true or f1040 line Filing Status = 'mfj' and helper "Number of people with a valid SSN who received qualified tips" > 0 (a count))
- Expr: `{"any":[{"all":[{"ne":["f1040.status",{"const":"mfj"}],"op":"test"},{"eq":["household.taxpayer_work_ssn",{"const":true}],"op":"test"}],"op":"test"},{"all":[{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},{"gt":["s1a.tip_ssn_count",{"const":0,"type":"Count"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if" and "If you are married filing a joint return, the spouse who received the qualified tips must have a valid SSN" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.part2`

- **Authored helper label:** Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN
- **Encoded (Bool):** Choose — [helper "Did you (or, on a joint return, your spouse) receive qualified tips as an employee in 2025 that you want to deduct?" = true → helper "Part II, once qualified tips are claimed: not married filing separately, and a person who received them has a valid SSN"] [helper "Did you (or, on a joint return, your spouse) receive qualified tips as an employee in 2025 that you want to deduct?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.tips",{"const":true}],"op":"test"},"then":"s1a.part2_ssn"},{"guard":{"eq":["s1a.tips",{"const":false}],"op":"test"},"then":"s1a.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; p. 101, Part II No Tax on Tips, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line4a_calc`

- **Authored helper label:** Figured: Enter qualified tips included on Form W-2, box 7, but see the instructions if Form W-2, box 5 is more than $176,100 or you received tips that are not subject to social security and Medicare taxes
- **Encoded (NonNegDollars):** Choose — [helper "Tips from more than one employer" = true → helper "Year parameter sales.zero"] [helper "Tips from more than one employer" = false → helper "Worksheet column (b) total: qualified tips reported on Form W-2 or on Forms 4070"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.tip_multi",{"const":true}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.tip_multi",{"const":false}],"op":"test"},"then":"s1a.tip_reported"}],"op":"choose"}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 4a; pp. 103-104, paragraphs 1 through 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## 4a — `s1a.line4a`

- **IRS:** Enter qualified tips included on Form W-2, box 7, but see the instructions if Form W-2, box 5 is more than $176,100 or you received tips that are not subject to social security and Medicare taxes
- **Encoded (NonNegDollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = true → helper "Figured: Enter qualified tips included on Form W-2, box 7, but see the instructions if Form W-2, box 5 is more than $176,100 or you received tips that are not subject to social security and Medicare taxes"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.line4a_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; p. 101, Part II No Tax on Tips, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.f4137_total`

- **Authored helper label:** Cash and charge tips on the Forms 4137 of the people on the return (line 2)
- **Encoded (NonNegDollars):** Add person.f4137_col_c over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.f4137_col_c","op":"sum_over"}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 4b (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `s1a.f4137`

- **Authored helper label:** Someone on the return has tips on Form 4137
- **Encoded (Bool):** helper "Cash and charge tips on the Forms 4137 of the people on the return (line 2)" > $0 (sales.zero)
- Expr: `{"gt":["s1a.f4137_total",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 4b (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line4b_calc`

- **Authored helper label:** Figured: Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed, enter -0-
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- **Refusal:** when s1a.f4137 is true, cannot complete The deduction for qualified tips included on Form 4137 (Schedule 1-A, line 4b). This tool prepares Form 4137 but does not figure the part of its tips that is qualified tips for the deduction. Claim the deduction for tips without this tool, or answer that you do not want the deduction for tips. Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "If you received cash and charge tips of $20 or more in a calendar month and didn't report all of those tips to your employer, you must file Form 4137"; p. 104, line 4b (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 4b (2025; printed date 2026-02-25; sha256 482e9c48)

## 4b — `s1a.line4b`

- **IRS:** Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed, enter -0-
- **Encoded (NonNegDollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = true → helper "Figured: Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed, enter -0-"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.line4b_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; p. 101, Part II No Tax on Tips, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tips_employee_one`

- **Authored helper label:** Line 4c with one employer: the larger of line 4a or line 4b
- **Encoded (NonNegDollars):** Enter the larger of line 4a or line 4b.
- Expr: `{"of":["s1a.line4a","s1a.line4b"],"op":"larger_of"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 4c, "If you only received qualified tips as an employee with respect to employment with one employer, enter the larger of line 4a or line 4b" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.tips_employee_calc`

- **Authored helper label:** Figured: If you only received qualified tips as an employee with respect to employment with one employer, enter the larger of line 4a or line 4b. Otherwise, see the instructions to determine the amount to enter on line 4c
- **Encoded (NonNegDollars):** Choose — [helper "Tips from more than one employer" = true → helper "Worksheet line 2. Add lines 1A through 1E, column (d)"] [helper "Tips from more than one employer" = false → helper "Line 4c with one employer: the larger of line 4a or line 4b"]
- **Refusal:** when s1a.tips_over_wages is true, cannot complete Schedule 1-A, Part II (qualified tips larger than the Medicare wages and tips that include them). The tips entered for a person are more than that person's Form W-2 box 5 Medicare wages and tips, which include them. Correct the tip amounts or the Forms W-2. Cite: [f1040s1a] p. 1, line 4a, "Enter qualified tips included on Form W-2, box 7"; fw2 p. 7, Box 6, "all Medicare wages and tips shown in box 5" (2025; created 2025-11-04; sha256 64f97b38)
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.tip_multi",{"const":true}],"op":"test"},"then":"s1a.tip_total"},{"guard":{"eq":["s1a.tip_multi",{"const":false}],"op":"test"},"then":"s1a.tips_employee_one"}],"op":"choose"}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 4c, and the Qualified Tips From More Than One Employer Worksheet (2025; printed date 2026-02-25; sha256 482e9c48)

## 4c — `s1a.tips_employee`

- **IRS:** If you only received qualified tips as an employee with respect to employment with one employer, enter the larger of line 4a or line 4b. Otherwise, see the instructions to determine the amount to enter on line 4c
- **Encoded (NonNegDollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = true → helper "Figured: If you only received qualified tips as an employee with respect to employment with one employer, enter the larger of line 4a or line 4b. Otherwise, see the instructions to determine the amount to enter on line 4c"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.tips_employee_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; p. 101, Part II No Tax on Tips, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tips_business_calc`

- **Authored helper label:** Figured: Qualified tips received in the course of a trade or business
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- **Refusal:** when scope.schedule1 is true, cannot complete Schedule 1-A, line 5 (qualified tips in a trade or business, with Schedule C, E or F). Income from a trade or business is outside this tool. Cite: [i1040gi] p. 104, Schedule 1-A, line 5, and the Multiple Trades or Businesses Worksheet (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when s1.sc_1a is true, cannot complete Schedule 1-A, line 5 (qualified tips in a trade or business, with Schedule C). Qualified tips received in a trade or business are outside this tool. Cite: [i1040gi] p. 104, Schedule 1-A, line 5, and the Multiple Trades or Businesses Worksheet (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## 5 — `s1a.tips_business`

- **IRS:** Qualified tips received in the course of a trade or business
- **Encoded (NonNegDollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = true → helper "Figured: Qualified tips received in the course of a trade or business"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.tips_business_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; p. 101, Part II No Tax on Tips, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tips_total_calc`

- **Authored helper label:** Figured: Add lines 4c and 5
- **Encoded (NonNegDollars):** Add line 4c and line 5.
- Expr: `{"of":["s1a.tips_employee","s1a.tips_business"],"op":"sum"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 6 (2025; created 2025-11-04; sha256 64f97b38)

## 6 — `s1a.tips_total`

- **IRS:** Add lines 4c and 5
- **Encoded (NonNegDollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = true → helper "Figured: Add lines 4c and 5"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.tips_total_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; p. 101, Part II No Tax on Tips, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tips_capped_calc`

- **Authored helper label:** Figured: Enter the smaller of the amount on line 6 or $25,000
- **Encoded (NonNegDollars):** Enter the smaller of line 6 or helper "Year parameter s1a.tips_max ($25,000)".
- Expr: `{"of":["s1a.tips_total","s1a.tips_max"],"op":"smaller_of"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 7 (2025; created 2025-11-04; sha256 64f97b38)

## 7 — `s1a.tips_capped`

- **IRS:** Enter the smaller of the amount on line 6 or $25,000
- **Encoded (NonNegDollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = true → helper "Figured: Enter the smaller of the amount on line 6 or $25,000"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.tips_capped_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; p. 101, Part II No Tax on Tips, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tips_max`

- **Authored helper label:** Year parameter s1a.tips_max ($25,000)
- **Encoded (NonNegDollars):** Enter $25,000 (s1a.tips_max).
- Expr: `{"op":"param","ref":"s1a.tips_max"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 7, $25,000 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.base_other`

- **Authored helper label:** Year parameter s1a.base_other ($150,000)
- **Encoded (NonNegDollars):** Enter $150,000 (s1a.base_other).
- Expr: `{"op":"param","ref":"s1a.base_other"}`
- Cite: [f1040s1a] Schedule 1-A (2025), lines 9 and 17, $150,000 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.base_joint`

- **Authored helper label:** Year parameter s1a.base_joint ($300,000)
- **Encoded (NonNegDollars):** Enter $300,000 (s1a.base_joint).
- Expr: `{"op":"param","ref":"s1a.base_joint"}`
- Cite: [f1040s1a] Schedule 1-A (2025), lines 9 and 17, $300,000 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.joint`

- **Authored helper label:** Married filing jointly
- **Encoded (Bool):** f1040 line Filing Status = 'mfj'
- Expr: `{"eq":["f1040.status",{"const":"mfj"}],"op":"test"}`
- Cite: [f1040s1a] Schedule 1-A (2025), lines 9, 15, 17 and 32, "if married filing jointly" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.tips_magi_calc`

- **Authored helper label:** Figured: Enter the amount from line 3
- **Encoded (Dollars):** Enter the amount from line 3.
- Expr: `{"from":"s1a.line3","op":"copy"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 8 (2025; created 2025-11-04; sha256 64f97b38)

## 8 — `s1a.tips_magi`

- **IRS:** Enter the amount from line 3
- **Encoded (Dollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = true → helper "Figured: Enter the amount from line 3"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.tips_magi_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; p. 101, Part II No Tax on Tips, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tips_threshold_calc`

- **Authored helper label:** Figured: Enter $150,000 ($300,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [helper "Married filing jointly" = true → helper "Year parameter s1a.base_joint ($300,000)"] [helper "Married filing jointly" = false → helper "Year parameter s1a.base_other ($150,000)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.joint",{"const":true}],"op":"test"},"then":"s1a.base_joint"},{"guard":{"eq":["s1a.joint",{"const":false}],"op":"test"},"then":"s1a.base_other"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 9 (2025; created 2025-11-04; sha256 64f97b38)

## 9 — `s1a.tips_threshold`

- **IRS:** Enter $150,000 ($300,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = true → helper "Figured: Enter $150,000 ($300,000 if married filing jointly)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.tips_threshold_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; p. 101, Part II No Tax on Tips, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tips_over_calc`

- **Authored helper label:** Figured: Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13
- **Encoded (Dollars):** Subtract line 9 from line 8.
- Expr: `{"from":"s1a.tips_magi","op":"subtract","take":"s1a.tips_threshold"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 10 (2025; created 2025-11-04; sha256 64f97b38)

## 10 — `s1a.tips_over`

- **IRS:** Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13
- **Encoded (Dollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = true → helper "Figured: Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.tips_over_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; p. 101, Part II No Tax on Tips, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tips_magi_over`

- **Authored helper label:** Is the amount on line 8 more than the amount on line 9?
- **Encoded (Bool):** line 8 > line 9
- Expr: `{"gt":["s1a.tips_magi","s1a.tips_threshold"],"op":"test"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 10, "If zero or less" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.tips_over_pos`

- **Authored helper label:** Line 10 if more than zero, otherwise zero
- **Encoded (NonNegDollars):** Subtract line 9 from line 8. If zero or less, enter -0-.
- Expr: `{"from":"s1a.tips_magi","op":"subtract_floor0","take":"s1a.tips_threshold"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 10, "Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line11_thousands`

- **Authored helper label:** Line 11. Divide line 10 by $1,000, decreasing the result to the next lower whole number (kept as that many thousands of dollars)
- **Encoded (NonNegDollars):** Round helper "Line 10 if more than zero, otherwise zero" down to a multiple of $1,000.
- Expr: `{"of":"s1a.tips_over_pos","op":"round","rule":"down","unit":100000}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 11 (the whole number of $1,000 units, kept as that many thousands of dollars) (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.tips_reduction_calc`

- **Authored helper label:** Figured: Multiply line 11 by $100
- **Encoded (NonNegDollars):** Multiply helper "Line 11. Divide line 10 by $1,000, decreasing the result to the next lower whole number (kept as that many thousands of dollars)" by 1/10 (s1a.hundred_per_thousand).
- Expr: `{"amount":"s1a.line11_thousands","op":"multiply_rate","rate":{"param":"s1a.hundred_per_thousand"}}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 12, "Multiply line 11 by $100" (2025; created 2025-11-04; sha256 64f97b38)

## 12 — `s1a.tips_reduction`

- **IRS:** Multiply line 11 by $100
- **Encoded (NonNegDollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, and a person who received them has a valid SSN" = true → helper "Figured: Multiply line 11 by $100"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.tips_reduction_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; p. 101, Part II No Tax on Tips, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tips_deduction_figured`

- **Authored helper label:** Subtract line 12 from line 7. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract line 12 from line 7. If zero or less, enter -0-.
- Expr: `{"from":"s1a.tips_capped","op":"subtract_floor0","take":"s1a.tips_reduction"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 13 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.tips_deduction_amount`

- **Authored helper label:** Line 13 when Part II applies
- **Encoded (NonNegDollars):** Choose — [helper "Is the amount on line 8 more than the amount on line 9?" = false → line 7] [helper "Is the amount on line 8 more than the amount on line 9?" = true → helper "Subtract line 12 from line 7. If zero or less, enter -0-"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.tips_magi_over",{"const":false}],"op":"test"},"then":"s1a.tips_capped"},{"guard":{"eq":["s1a.tips_magi_over",{"const":true}],"op":"test"},"then":"s1a.tips_deduction_figured"}],"op":"choose"}`
- Cite: [i1040gi] p. 105, Schedule 1-A, line 10, "If the amount on line 10 is zero or less ... Skip lines 11 and 12 and enter the amount from Schedule 1-A, line 7, on Schedule 1-A, line 13" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tips_deduction_ssn`

- **Authored helper label:** Line 13 with qualified tips: zero unless a person who received them has a valid SSN
- **Encoded (NonNegDollars):** Choose — [helper "You have a valid SSN or, if married filing jointly, a spouse who received them has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "You have a valid SSN or, if married filing jointly, a spouse who received them has a valid SSN" = true → helper "Line 13 when Part II applies"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.tip_ssn",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.tip_ssn",{"const":true}],"op":"test"},"then":"s1a.tips_deduction_amount"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if: ... You have a valid social security number (SSN)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tips_deduction_claim`

- **Authored helper label:** Line 13 with qualified tips: zero for married filing separately
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → helper "Line 13 with qualified tips: zero unless a person who received them has a valid SSN"] [f1040 line Filing Status = 'mfj' → helper "Line 13 with qualified tips: zero unless a person who received them has a valid SSN"] [f1040 line Filing Status = 'mfs' → helper "Year parameter sales.zero"] [f1040 line Filing Status = 'hoh' → helper "Line 13 with qualified tips: zero unless a person who received them has a valid SSN"] [f1040 line Filing Status = 'qss' → helper "Line 13 with qualified tips: zero unless a person who received them has a valid SSN"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"s1a.tips_deduction_ssn"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"s1a.tips_deduction_ssn"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"s1a.tips_deduction_ssn"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"s1a.tips_deduction_ssn"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), Part II caution, "If married, you must file jointly to claim this deduction" (2025; created 2025-11-04; sha256 64f97b38)

## 13 — `s1a.tips_deduction`

- **IRS:** Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Choose — [helper "Did you (or, on a joint return, your spouse) receive qualified tips as an employee in 2025 that you want to deduct?" = false → helper "Year parameter sales.zero"] [helper "Did you (or, on a joint return, your spouse) receive qualified tips as an employee in 2025 that you want to deduct?" = true → helper "Line 13 with qualified tips: zero for married filing separately"]
- **Refusal:** when s1.sc_1a is true, cannot complete Schedule 1-A, lines 5 and 14b (qualified tips received in a trade or business, or qualified overtime reported on Form 1099-NEC or 1099-MISC, with Schedule C). Qualified tips received in a trade or business and qualified overtime reported on Form 1099-NEC or 1099-MISC are outside this tool. Cite: [i1040gi] p. 104, Schedule 1-A, line 5, "Include the qualified tips you and/or your spouse received in the course of a trade or business"; p. 101, "Fill out Schedule 1-A, Part II, only if" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.tips",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.tips",{"const":true}],"op":"test"},"then":"s1a.tips_deduction_claim"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 13; i1040gi p. 101, "Fill out Schedule 1-A, Part II, only if" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.overtime`

- **Authored helper label:** Did you (or, on a joint return, your spouse) receive qualified overtime compensation in 2025 that you want to deduct?
- **Encoded (Bool):** Input — Did you (or, on a joint return, your spouse) receive overtime pay as an employee in 2025 that you want to deduct on Schedule 1-A, Part III (the FLSA Overtime Premium, generally the "half" of time-and-a-half)? (Overtime reported on Form 1099-NEC or 1099-MISC is asked about with Schedule C.)
- Expr: `{"op":"input","source":"Did you (or, on a joint return, your spouse) receive overtime pay as an employee in 2025 that you want to deduct on Schedule 1-A, Part III (the FLSA Overtime Premium, generally the \"half\" of time-and-a-half)? (Overtime reported on Form 1099-NEC or 1099-MISC is asked about with Schedule C.)"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if", "You (and/or your spouse if filing a joint return) received qualified overtime compensation in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.ot_over_count`

- **Authored helper label:** Number of people with a valid SSN whose qualified overtime amounts entered are more than their Medicare wages and tips (W-2 box 5)
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Do you have an SSN valid for employment issued before the due date of your return?" = true and helper "The qualified overtime compensation entered for this person is more than the person's Medicare wages and tips (W-2 box 5), of which it is a part" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"all":[{"eq":["person.work_ssn",{"const":true}],"op":"test"},{"eq":["person.ot_over_wages",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [f1040s1a] p. 1, line 14a, "Qualified overtime compensation included in Form W-2, box 1"; fw2 p. 7, Box 6, "all Medicare wages and tips shown in box 5" (2025; created 2025-11-04; sha256 64f97b38)

## (gate) — `s1a.ot_over_wages`

- **Authored helper label:** For someone on the return, the qualified overtime amounts entered are more than the Medicare wages and tips (W-2 box 5) that include them
- **Encoded (Bool):** helper "Number of people with a valid SSN whose qualified overtime amounts entered are more than their Medicare wages and tips (W-2 box 5)" > 0 (a count)
- Expr: `{"gt":["s1a.ot_over_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [f1040s1a] p. 1, line 14a, "Qualified overtime compensation included in Form W-2, box 1"; fw2 p. 7, Box 6, "all Medicare wages and tips shown in box 5" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.ot_ssn_count`

- **Authored helper label:** Number of people with a valid SSN who received qualified overtime compensation
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Do you have an SSN valid for employment issued before the due date of your return?" = true and helper "Number of employers that paid this person qualified overtime compensation" > 0 (a count), within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"all":[{"eq":["person.work_ssn",{"const":true}],"op":"test"},{"gt":["person.ot_employers",{"const":0,"type":"Count"}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if" and "If you are married filing jointly, the spouse who received the qualified overtime compensation must have a valid SSN" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.ot_ssn`

- **Authored helper label:** You have a valid SSN or, if married filing jointly, a spouse who received it has a valid SSN
- **Encoded (Bool):** (f1040 line Filing Status ≠ 'mfj' and household helper "Do you have an SSN valid for employment issued before the due date of your return?" = true or f1040 line Filing Status = 'mfj' and helper "Number of people with a valid SSN who received qualified overtime compensation" > 0 (a count))
- Expr: `{"any":[{"all":[{"ne":["f1040.status",{"const":"mfj"}],"op":"test"},{"eq":["household.taxpayer_work_ssn",{"const":true}],"op":"test"}],"op":"test"},{"all":[{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},{"gt":["s1a.ot_ssn_count",{"const":0,"type":"Count"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if" and "If you are married filing jointly, the spouse who received the qualified overtime compensation must have a valid SSN" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.part3`

- **Authored helper label:** Part III applies: qualified overtime claimed, not married filing separately, and a person who received it has a valid SSN
- **Encoded (Bool):** Choose — [helper "Did you (or, on a joint return, your spouse) receive qualified overtime compensation in 2025 that you want to deduct?" = true → helper "Part III, once qualified overtime is claimed: not married filing separately, and a person who received it has a valid SSN"] [helper "Did you (or, on a joint return, your spouse) receive qualified overtime compensation in 2025 that you want to deduct?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.overtime",{"const":true}],"op":"test"},"then":"s1a.part3_ssn"},{"guard":{"eq":["s1a.overtime",{"const":false}],"op":"test"},"then":"s1a.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if"; p. 106, Part III No Tax on Overtime, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.ot_w2_calc`

- **Authored helper label:** Figured: Qualified overtime compensation included in Form W-2, box 1. If you received qualified overtime compensation not reported on Form W-2, box 1, see instructions
- **Encoded (NonNegDollars):** Add person.ot_total over every confirmed person entry for which helper "Do you have an SSN valid for employment issued before the due date of your return?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when s1a.ot_over_wages is true, cannot complete Schedule 1-A, Part III (qualified overtime compensation larger than the Medicare wages and tips that include it). The overtime compensation entered for a person is more than that person's Form W-2 box 5 Medicare wages and tips, which include it. Correct the overtime amounts or the Forms W-2. Cite: [f1040s1a] p. 1, line 14a, "Qualified overtime compensation included in Form W-2, box 1"; fw2 p. 7, Box 6, "all Medicare wages and tips shown in box 5" (2025; created 2025-11-04; sha256 64f97b38)
- Expr: `{"collection":"person","field":"person.ot_total","op":"sum_over","where":{"eq":["person.work_ssn",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 108, Schedule 1-A, line 14a, and the Qualified Overtime Compensation From More Than One Employer Worksheet, line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## 14a — `s1a.ot_w2`

- **IRS:** Qualified overtime compensation included in Form W-2, box 1. If you received qualified overtime compensation not reported on Form W-2, box 1, see instructions
- **Encoded (NonNegDollars):** Choose — [helper "Part III applies: qualified overtime claimed, not married filing separately, and a person who received it has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part III applies: qualified overtime claimed, not married filing separately, and a person who received it has a valid SSN" = true → helper "Figured: Qualified overtime compensation included in Form W-2, box 1. If you received qualified overtime compensation not reported on Form W-2, box 1, see instructions"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part3",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part3",{"const":true}],"op":"test"},"then":"s1a.ot_w2_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if"; p. 106, Part III No Tax on Overtime, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.ot_1099_calc`

- **Authored helper label:** Figured: Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- **Refusal:** when scope.schedule1 is true, cannot complete Schedule 1-A, line 14b (qualified overtime reported on Form 1099-NEC or 1099-MISC, with Schedule C). Nonemployee compensation is outside this tool. Cite: [i1040gi] p. 108, Schedule 1-A, line 14b, and the Qualified Overtime Compensation From More Than One Payor Worksheet (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when s1.sc_1a is true, cannot complete Schedule 1-A, line 14b (qualified overtime reported on Form 1099-NEC or 1099-MISC). Qualified overtime compensation reported on Form 1099-NEC or 1099-MISC is outside this tool. Cite: [i1040gi] p. 108, Schedule 1-A, line 14b (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 108, Schedule 1-A, line 14b (2025; printed date 2026-02-25; sha256 482e9c48)

## 14b — `s1a.ot_1099`

- **IRS:** Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3
- **Encoded (NonNegDollars):** Choose — [helper "Part III applies: qualified overtime claimed, not married filing separately, and a person who received it has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part III applies: qualified overtime claimed, not married filing separately, and a person who received it has a valid SSN" = true → helper "Figured: Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part3",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part3",{"const":true}],"op":"test"},"then":"s1a.ot_1099_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if"; p. 106, Part III No Tax on Overtime, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.ot_total_calc`

- **Authored helper label:** Figured: Add lines 14a and 14b
- **Encoded (NonNegDollars):** Add line 14a and line 14b.
- Expr: `{"of":["s1a.ot_w2","s1a.ot_1099"],"op":"sum"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 14c (2025; created 2025-11-04; sha256 64f97b38)

## 14c — `s1a.ot_total`

- **IRS:** Add lines 14a and 14b
- **Encoded (NonNegDollars):** Choose — [helper "Part III applies: qualified overtime claimed, not married filing separately, and a person who received it has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part III applies: qualified overtime claimed, not married filing separately, and a person who received it has a valid SSN" = true → helper "Figured: Add lines 14a and 14b"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part3",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part3",{"const":true}],"op":"test"},"then":"s1a.ot_total_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if"; p. 106, Part III No Tax on Overtime, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.ot_max_other`

- **Authored helper label:** Year parameter s1a.ot_max_other ($12,500)
- **Encoded (NonNegDollars):** Enter $12,500 (s1a.ot_max_other).
- Expr: `{"op":"param","ref":"s1a.ot_max_other"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 15, $12,500 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.ot_max_joint`

- **Authored helper label:** Year parameter s1a.ot_max_joint ($25,000)
- **Encoded (NonNegDollars):** Enter $25,000 (s1a.ot_max_joint).
- Expr: `{"op":"param","ref":"s1a.ot_max_joint"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 15, $25,000 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.ot_max`

- **Authored helper label:** $12,500 ($25,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [helper "Married filing jointly" = true → helper "Year parameter s1a.ot_max_joint ($25,000)"] [helper "Married filing jointly" = false → helper "Year parameter s1a.ot_max_other ($12,500)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.joint",{"const":true}],"op":"test"},"then":"s1a.ot_max_joint"},{"guard":{"eq":["s1a.joint",{"const":false}],"op":"test"},"then":"s1a.ot_max_other"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 15 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.ot_capped_calc`

- **Authored helper label:** Figured: Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)
- **Encoded (NonNegDollars):** Enter the smaller of line 14c or helper "$12,500 ($25,000 if married filing jointly)".
- Expr: `{"of":["s1a.ot_total","s1a.ot_max"],"op":"smaller_of"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 15 (2025; created 2025-11-04; sha256 64f97b38)

## 15 — `s1a.ot_capped`

- **IRS:** Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [helper "Part III applies: qualified overtime claimed, not married filing separately, and a person who received it has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part III applies: qualified overtime claimed, not married filing separately, and a person who received it has a valid SSN" = true → helper "Figured: Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part3",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part3",{"const":true}],"op":"test"},"then":"s1a.ot_capped_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if"; p. 106, Part III No Tax on Overtime, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.ot_magi_calc`

- **Authored helper label:** Figured: Enter the amount from line 3
- **Encoded (Dollars):** Enter the amount from line 3.
- Expr: `{"from":"s1a.line3","op":"copy"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 16 (2025; created 2025-11-04; sha256 64f97b38)

## 16 — `s1a.ot_magi`

- **IRS:** Enter the amount from line 3
- **Encoded (Dollars):** Choose — [helper "Part III applies: qualified overtime claimed, not married filing separately, and a person who received it has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part III applies: qualified overtime claimed, not married filing separately, and a person who received it has a valid SSN" = true → helper "Figured: Enter the amount from line 3"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part3",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part3",{"const":true}],"op":"test"},"then":"s1a.ot_magi_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if"; p. 106, Part III No Tax on Overtime, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.ot_threshold_calc`

- **Authored helper label:** Figured: Enter $150,000 ($300,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [helper "Married filing jointly" = true → helper "Year parameter s1a.base_joint ($300,000)"] [helper "Married filing jointly" = false → helper "Year parameter s1a.base_other ($150,000)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.joint",{"const":true}],"op":"test"},"then":"s1a.base_joint"},{"guard":{"eq":["s1a.joint",{"const":false}],"op":"test"},"then":"s1a.base_other"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 17 (2025; created 2025-11-04; sha256 64f97b38)

## 17 — `s1a.ot_threshold`

- **IRS:** Enter $150,000 ($300,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [helper "Part III applies: qualified overtime claimed, not married filing separately, and a person who received it has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part III applies: qualified overtime claimed, not married filing separately, and a person who received it has a valid SSN" = true → helper "Figured: Enter $150,000 ($300,000 if married filing jointly)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part3",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part3",{"const":true}],"op":"test"},"then":"s1a.ot_threshold_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if"; p. 106, Part III No Tax on Overtime, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.ot_over_calc`

- **Authored helper label:** Figured: Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21
- **Encoded (Dollars):** Subtract line 17 from line 16.
- Expr: `{"from":"s1a.ot_magi","op":"subtract","take":"s1a.ot_threshold"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 18 (2025; created 2025-11-04; sha256 64f97b38)

## 18 — `s1a.ot_over`

- **IRS:** Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21
- **Encoded (Dollars):** Choose — [helper "Part III applies: qualified overtime claimed, not married filing separately, and a person who received it has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part III applies: qualified overtime claimed, not married filing separately, and a person who received it has a valid SSN" = true → helper "Figured: Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part3",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part3",{"const":true}],"op":"test"},"then":"s1a.ot_over_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if"; p. 106, Part III No Tax on Overtime, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.ot_magi_over`

- **Authored helper label:** Is the amount on line 16 more than the amount on line 17?
- **Encoded (Bool):** line 16 > line 17
- Expr: `{"gt":["s1a.ot_magi","s1a.ot_threshold"],"op":"test"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 18, "If zero or less" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.ot_over_pos`

- **Authored helper label:** Line 18 if more than zero, otherwise zero
- **Encoded (NonNegDollars):** Subtract line 17 from line 16. If zero or less, enter -0-.
- Expr: `{"from":"s1a.ot_magi","op":"subtract_floor0","take":"s1a.ot_threshold"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 18, "Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line19_thousands`

- **Authored helper label:** Line 19. Divide line 18 by $1,000, decreasing the result to the next lower whole number (kept as that many thousands of dollars)
- **Encoded (NonNegDollars):** Round helper "Line 18 if more than zero, otherwise zero" down to a multiple of $1,000.
- Expr: `{"of":"s1a.ot_over_pos","op":"round","rule":"down","unit":100000}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 19 (the whole number of $1,000 units, kept as that many thousands of dollars) (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.ot_reduction_calc`

- **Authored helper label:** Figured: Multiply line 19 by $100
- **Encoded (NonNegDollars):** Multiply helper "Line 19. Divide line 18 by $1,000, decreasing the result to the next lower whole number (kept as that many thousands of dollars)" by 1/10 (s1a.hundred_per_thousand).
- Expr: `{"amount":"s1a.line19_thousands","op":"multiply_rate","rate":{"param":"s1a.hundred_per_thousand"}}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 20, "Multiply line 19 by $100" (2025; created 2025-11-04; sha256 64f97b38)

## 20 — `s1a.ot_reduction`

- **IRS:** Multiply line 19 by $100
- **Encoded (NonNegDollars):** Choose — [helper "Part III applies: qualified overtime claimed, not married filing separately, and a person who received it has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part III applies: qualified overtime claimed, not married filing separately, and a person who received it has a valid SSN" = true → helper "Figured: Multiply line 19 by $100"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part3",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part3",{"const":true}],"op":"test"},"then":"s1a.ot_reduction_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if"; p. 106, Part III No Tax on Overtime, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.ot_deduction_figured`

- **Authored helper label:** Subtract line 20 from line 15. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract line 20 from line 15. If zero or less, enter -0-.
- Expr: `{"from":"s1a.ot_capped","op":"subtract_floor0","take":"s1a.ot_reduction"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 21 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.ot_deduction_amount`

- **Authored helper label:** Line 21 when Part III applies
- **Encoded (NonNegDollars):** Choose — [helper "Is the amount on line 16 more than the amount on line 17?" = false → line 15] [helper "Is the amount on line 16 more than the amount on line 17?" = true → helper "Subtract line 20 from line 15. If zero or less, enter -0-"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.ot_magi_over",{"const":false}],"op":"test"},"then":"s1a.ot_capped"},{"guard":{"eq":["s1a.ot_magi_over",{"const":true}],"op":"test"},"then":"s1a.ot_deduction_figured"}],"op":"choose"}`
- Cite: [i1040gi] p. 108, Schedule 1-A, line 18, "If the amount on line 18 is zero or less ... Skip lines 19 and 20 and enter the amount from Schedule 1-A, line 15, on Schedule 1-A, line 21" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.ot_deduction_ssn`

- **Authored helper label:** Line 21 with qualified overtime: zero unless a person who received it has a valid SSN
- **Encoded (NonNegDollars):** Choose — [helper "You have a valid SSN or, if married filing jointly, a spouse who received it has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "You have a valid SSN or, if married filing jointly, a spouse who received it has a valid SSN" = true → helper "Line 21 when Part III applies"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.ot_ssn",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.ot_ssn",{"const":true}],"op":"test"},"then":"s1a.ot_deduction_amount"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if: ... You have a valid social security number (SSN)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.ot_deduction_claim`

- **Authored helper label:** Line 21 with qualified overtime: zero for married filing separately
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → helper "Line 21 with qualified overtime: zero unless a person who received it has a valid SSN"] [f1040 line Filing Status = 'mfj' → helper "Line 21 with qualified overtime: zero unless a person who received it has a valid SSN"] [f1040 line Filing Status = 'mfs' → helper "Year parameter sales.zero"] [f1040 line Filing Status = 'hoh' → helper "Line 21 with qualified overtime: zero unless a person who received it has a valid SSN"] [f1040 line Filing Status = 'qss' → helper "Line 21 with qualified overtime: zero unless a person who received it has a valid SSN"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"s1a.ot_deduction_ssn"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"s1a.ot_deduction_ssn"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"s1a.ot_deduction_ssn"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"s1a.ot_deduction_ssn"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), Part III caution, "If married, you must file jointly to claim this deduction" (2025; created 2025-11-04; sha256 64f97b38)

## 21 — `s1a.ot_deduction`

- **IRS:** Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Choose — [helper "Did you (or, on a joint return, your spouse) receive qualified overtime compensation in 2025 that you want to deduct?" = false → helper "Year parameter sales.zero"] [helper "Did you (or, on a joint return, your spouse) receive qualified overtime compensation in 2025 that you want to deduct?" = true → helper "Line 21 with qualified overtime: zero for married filing separately"]
- **Refusal:** when s1.sc_1a is true, cannot complete Schedule 1-A, lines 5 and 14b (qualified tips received in a trade or business, or qualified overtime reported on Form 1099-NEC or 1099-MISC, with Schedule C). Qualified tips received in a trade or business and qualified overtime reported on Form 1099-NEC or 1099-MISC are outside this tool. Cite: [i1040gi] p. 108, Schedule 1-A, line 14b, "Enter on Line 14b only the qualified overtime compensation amount that is included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3"; p. 106, "Fill out Schedule 1-A, Part III, only if" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.overtime",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.overtime",{"const":true}],"op":"test"},"then":"s1a.ot_deduction_claim"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 21; i1040gi p. 106, "Fill out Schedule 1-A, Part III, only if" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.carloan`

- **Authored helper label:** Did you (or, on a joint return, your spouse) pay or accrue interest in 2025 on a loan to buy a new passenger vehicle that you want to deduct?
- **Encoded (Bool):** Input — Did you (or, on a joint return, your spouse) pay or accrue interest in 2025 on a loan taken out after 2024 to buy a new car, minivan, van, SUV, pickup truck or motorcycle for personal use that you want to deduct on Schedule 1-A, Part IV?
- Expr: `{"op":"input","source":"Did you (or, on a joint return, your spouse) pay or accrue interest in 2025 on a loan taken out after 2024 to buy a new car, minivan, van, SUV, pickup truck or motorcycle for personal use that you want to deduct on Schedule 1-A, Part IV?"}`
- Cite: [i1040gi] p. 109, Schedule 1-A, Part IV, "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025", "if you and/or your spouse paid or accrued qualified passenger vehicle loan interest" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.vli_total_all`

- **Authored helper label:** Add lines 22a and 22b, column (iii), and any further loans on the attached statement
- **Encoded (NonNegDollars):** Add carloan.col_iii over every confirmed carloan entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"carloan","field":"carloan.col_iii","op":"sum_over"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, line 22, "If you need to report more than two VINs, attach a statement" (2025; printed date 2026-02-25; sha256 482e9c48)

## 23 — `s1a.vli_total`

- **IRS:** Add lines 22a and 22b, column (iii)
- **Encoded (NonNegDollars):** Choose — [helper "Did you (or, on a joint return, your spouse) pay or accrue interest in 2025 on a loan to buy a new passenger vehicle that you want to deduct?" = false → helper "Year parameter sales.zero"] [helper "Did you (or, on a joint return, your spouse) pay or accrue interest in 2025 on a loan to buy a new passenger vehicle that you want to deduct?" = true → helper "Add lines 22a and 22b, column (iii), and any further loans on the attached statement"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.carloan",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.carloan",{"const":true}],"op":"test"},"then":"s1a.vli_total_all"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 23 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.car_max`

- **Authored helper label:** Year parameter s1a.car_max ($10,000)
- **Encoded (NonNegDollars):** Enter $10,000 (s1a.car_max).
- Expr: `{"op":"param","ref":"s1a.car_max"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 24, $10,000 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.part4`

- **Authored helper label:** Part IV applies: qualified passenger vehicle loan interest claimed
- **Encoded (Bool):** helper "Did you (or, on a joint return, your spouse) pay or accrue interest in 2025 on a loan to buy a new passenger vehicle that you want to deduct?" = true
- Expr: `{"eq":["s1a.carloan",{"const":true}],"op":"test"}`
- Cite: [i1040gi] p. 109, Schedule 1-A, Part IV, "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.vli_capped_calc`

- **Authored helper label:** Figured: Enter the smaller of the amount on line 23 or $10,000
- **Encoded (NonNegDollars):** Enter the smaller of line 23 or helper "Year parameter s1a.car_max ($10,000)".
- Expr: `{"of":["s1a.vli_total","s1a.car_max"],"op":"smaller_of"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 24 (2025; created 2025-11-04; sha256 64f97b38)

## 24 — `s1a.vli_capped`

- **IRS:** Enter the smaller of the amount on line 23 or $10,000
- **Encoded (NonNegDollars):** Choose — [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = false → helper "Year parameter sales.zero"] [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = true → helper "Figured: Enter the smaller of the amount on line 23 or $10,000"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part4",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part4",{"const":true}],"op":"test"},"then":"s1a.vli_capped_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 109, Schedule 1-A, Part IV, "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.car_base_other`

- **Authored helper label:** Year parameter s1a.car_base_other ($100,000)
- **Encoded (NonNegDollars):** Enter $100,000 (s1a.car_base_other).
- Expr: `{"op":"param","ref":"s1a.car_base_other"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 26, $100,000 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.car_base_joint`

- **Authored helper label:** Year parameter s1a.car_base_joint ($200,000)
- **Encoded (NonNegDollars):** Enter $200,000 (s1a.car_base_joint).
- Expr: `{"op":"param","ref":"s1a.car_base_joint"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 26, $200,000 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.vli_magi_calc`

- **Authored helper label:** Figured: Enter the amount from line 3
- **Encoded (Dollars):** Enter the amount from line 3.
- Expr: `{"from":"s1a.line3","op":"copy"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 25 (2025; created 2025-11-04; sha256 64f97b38)

## 25 — `s1a.vli_magi`

- **IRS:** Enter the amount from line 3
- **Encoded (Dollars):** Choose — [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = false → helper "Year parameter sales.zero"] [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = true → helper "Figured: Enter the amount from line 3"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part4",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part4",{"const":true}],"op":"test"},"then":"s1a.vli_magi_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 109, Schedule 1-A, Part IV, "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.vli_threshold_calc`

- **Authored helper label:** Figured: Enter $100,000 ($200,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → helper "Year parameter s1a.car_base_other ($100,000)"] [f1040 line Filing Status = 'mfj' → helper "Year parameter s1a.car_base_joint ($200,000)"] [f1040 line Filing Status = 'mfs' → helper "Year parameter s1a.car_base_other ($100,000)"] [f1040 line Filing Status = 'hoh' → helper "Year parameter s1a.car_base_other ($100,000)"] [f1040 line Filing Status = 'qss' → helper "Year parameter s1a.car_base_other ($100,000)"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"s1a.car_base_other"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"s1a.car_base_joint"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"s1a.car_base_other"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"s1a.car_base_other"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"s1a.car_base_other"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 26 (2025; created 2025-11-04; sha256 64f97b38)

## 26 — `s1a.vli_threshold`

- **IRS:** Enter $100,000 ($200,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = false → helper "Year parameter sales.zero"] [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = true → helper "Figured: Enter $100,000 ($200,000 if married filing jointly)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part4",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part4",{"const":true}],"op":"test"},"then":"s1a.vli_threshold_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 109, Schedule 1-A, Part IV, "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.vli_over_calc`

- **Authored helper label:** Figured: Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on line 30
- **Encoded (Dollars):** Subtract line 26 from line 25.
- Expr: `{"from":"s1a.vli_magi","op":"subtract","take":"s1a.vli_threshold"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 27 (2025; created 2025-11-04; sha256 64f97b38)

## 27 — `s1a.vli_over`

- **IRS:** Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on line 30
- **Encoded (Dollars):** Choose — [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = false → helper "Year parameter sales.zero"] [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = true → helper "Figured: Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on line 30"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part4",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part4",{"const":true}],"op":"test"},"then":"s1a.vli_over_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 109, Schedule 1-A, Part IV, "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.vli_magi_over`

- **Authored helper label:** Is the amount on line 25 more than the amount on line 26?
- **Encoded (Bool):** line 25 > line 26
- Expr: `{"gt":["s1a.vli_magi","s1a.vli_threshold"],"op":"test"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 27, "If zero or less" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.vli_over_pos`

- **Authored helper label:** Line 27 if more than zero, otherwise zero
- **Encoded (NonNegDollars):** Subtract line 26 from line 25. If zero or less, enter -0-.
- Expr: `{"from":"s1a.vli_magi","op":"subtract_floor0","take":"s1a.vli_threshold"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 27, "Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on line 30" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line28_thousands`

- **Authored helper label:** Line 28. Divide line 27 by $1,000, increasing the result to the next higher whole number (kept as that many thousands of dollars)
- **Encoded (NonNegDollars):** Round helper "Line 27 if more than zero, otherwise zero" up to the next multiple of $1,000.
- Expr: `{"of":"s1a.vli_over_pos","op":"round","rule":"up","unit":100000}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 28 (the whole number of $1,000 units, kept as that many thousands of dollars) (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.vli_reduction_calc`

- **Authored helper label:** Figured: Multiply line 28 by $200
- **Encoded (NonNegDollars):** Multiply helper "Line 28. Divide line 27 by $1,000, increasing the result to the next higher whole number (kept as that many thousands of dollars)" by 1/5 (s1a.two_hundred_per_thousand).
- Expr: `{"amount":"s1a.line28_thousands","op":"multiply_rate","rate":{"param":"s1a.two_hundred_per_thousand"}}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 29, "Multiply line 28 by $200" (2025; created 2025-11-04; sha256 64f97b38)

## 29 — `s1a.vli_reduction`

- **IRS:** Multiply line 28 by $200
- **Encoded (NonNegDollars):** Choose — [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = false → helper "Year parameter sales.zero"] [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = true → helper "Figured: Multiply line 28 by $200"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part4",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part4",{"const":true}],"op":"test"},"then":"s1a.vli_reduction_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 109, Schedule 1-A, Part IV, "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.vli_deduction_figured`

- **Authored helper label:** Subtract line 29 from line 24. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract line 29 from line 24. If zero or less, enter -0-.
- Expr: `{"from":"s1a.vli_capped","op":"subtract_floor0","take":"s1a.vli_reduction"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 30 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.vli_deduction_amount`

- **Authored helper label:** Line 30 when Part IV applies
- **Encoded (NonNegDollars):** Choose — [helper "Is the amount on line 25 more than the amount on line 26?" = false → line 24] [helper "Is the amount on line 25 more than the amount on line 26?" = true → helper "Subtract line 29 from line 24. If zero or less, enter -0-"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.vli_magi_over",{"const":false}],"op":"test"},"then":"s1a.vli_capped"},{"guard":{"eq":["s1a.vli_magi_over",{"const":true}],"op":"test"},"then":"s1a.vli_deduction_figured"}],"op":"choose"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, line 27, "If the amount on line 27 is zero or less ... Skip lines 28 and 29 and enter the amount from Schedule 1-A, line 24, on Schedule 1-A, line 30" (2025; printed date 2026-02-25; sha256 482e9c48)

## 30 — `s1a.vli_deduction`

- **IRS:** Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 24. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Choose — [helper "Did you (or, on a joint return, your spouse) pay or accrue interest in 2025 on a loan to buy a new passenger vehicle that you want to deduct?" = false → helper "Year parameter sales.zero"] [helper "Did you (or, on a joint return, your spouse) pay or accrue interest in 2025 on a loan to buy a new passenger vehicle that you want to deduct?" = true → helper "Line 30 when Part IV applies"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.carloan",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.carloan",{"const":true}],"op":"test"},"then":"s1a.vli_deduction_amount"}],"op":"choose"}`
- Cite: [i1040gi] p. 109, Schedule 1-A, Part IV, "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.senior_count`

- **Authored helper label:** Number of people born before January 2, 1961, with a valid SSN
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Born before January 2, 1961, and has a valid SSN" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"eq":["person.senior_work_ssn",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Fill out Schedule 1-A, Part V, only if" and "If you are married filing jointly, the spouse who is claiming the enhanced deduction for seniors must have a valid SSN" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.senior_any`

- **Authored helper label:** You (and/or your spouse if filing jointly) were born before January 2, 1961, and have a valid SSN
- **Encoded (Bool):** helper "Number of people born before January 2, 1961, with a valid SSN" > 0 (a count)
- Expr: `{"gt":["s1a.senior_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Fill out Schedule 1-A, Part V, only if" and "If you are married filing jointly, the spouse who is claiming the enhanced deduction for seniors must have a valid SSN" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.part5`

- **Authored helper label:** Part V applies: you (and/or your spouse if filing jointly) were born before January 2, 1961, and have a valid SSN, not married filing separately
- **Encoded (Bool):** helper "You (and/or your spouse if filing jointly) were born before January 2, 1961, and have a valid SSN" = true and f1040 line Filing Status ≠ 'mfs'
- Expr: `{"all":[{"eq":["s1a.senior_any",{"const":true}],"op":"test"},{"ne":["f1040.status",{"const":"mfs"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Fill out Schedule 1-A, Part V, only if"; p. 110, Part V Enhanced Deduction for Seniors, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.senior_magi_calc`

- **Authored helper label:** Figured: Enter the amount from line 3
- **Encoded (Dollars):** Enter the amount from line 3.
- Expr: `{"from":"s1a.line3","op":"copy"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 31 (2025; created 2025-11-04; sha256 64f97b38)

## 31 — `s1a.senior_magi`

- **IRS:** Enter the amount from line 3
- **Encoded (Dollars):** Choose — [helper "Part V applies: you (and/or your spouse if filing jointly) were born before January 2, 1961, and have a valid SSN, not married filing separately" = false → helper "Year parameter sales.zero"] [helper "Part V applies: you (and/or your spouse if filing jointly) were born before January 2, 1961, and have a valid SSN, not married filing separately" = true → helper "Figured: Enter the amount from line 3"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part5",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part5",{"const":true}],"op":"test"},"then":"s1a.senior_magi_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Fill out Schedule 1-A, Part V, only if"; p. 110, Part V Enhanced Deduction for Seniors, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.senior_base_other`

- **Authored helper label:** Year parameter s1a.senior_base_other ($75,000)
- **Encoded (NonNegDollars):** Enter $75,000 (s1a.senior_base_other).
- Expr: `{"op":"param","ref":"s1a.senior_base_other"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 32, $75,000 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.senior_base_joint`

- **Authored helper label:** Year parameter s1a.senior_base_joint ($150,000)
- **Encoded (NonNegDollars):** Enter $150,000 (s1a.senior_base_joint).
- Expr: `{"op":"param","ref":"s1a.senior_base_joint"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 32, $150,000 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.senior_threshold_calc`

- **Authored helper label:** Figured: Enter $75,000 ($150,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [helper "Married filing jointly" = true → helper "Year parameter s1a.senior_base_joint ($150,000)"] [helper "Married filing jointly" = false → helper "Year parameter s1a.senior_base_other ($75,000)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.joint",{"const":true}],"op":"test"},"then":"s1a.senior_base_joint"},{"guard":{"eq":["s1a.joint",{"const":false}],"op":"test"},"then":"s1a.senior_base_other"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 32 (2025; created 2025-11-04; sha256 64f97b38)

## 32 — `s1a.senior_threshold`

- **IRS:** Enter $75,000 ($150,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [helper "Part V applies: you (and/or your spouse if filing jointly) were born before January 2, 1961, and have a valid SSN, not married filing separately" = false → helper "Year parameter sales.zero"] [helper "Part V applies: you (and/or your spouse if filing jointly) were born before January 2, 1961, and have a valid SSN, not married filing separately" = true → helper "Figured: Enter $75,000 ($150,000 if married filing jointly)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part5",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part5",{"const":true}],"op":"test"},"then":"s1a.senior_threshold_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Fill out Schedule 1-A, Part V, only if"; p. 110, Part V Enhanced Deduction for Seniors, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.senior_over_calc`

- **Authored helper label:** Figured: Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
- **Encoded (Dollars):** Subtract line 32 from line 31.
- Expr: `{"from":"s1a.senior_magi","op":"subtract","take":"s1a.senior_threshold"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 33 (2025; created 2025-11-04; sha256 64f97b38)

## 33 — `s1a.senior_over`

- **IRS:** Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
- **Encoded (Dollars):** Choose — [helper "Part V applies: you (and/or your spouse if filing jointly) were born before January 2, 1961, and have a valid SSN, not married filing separately" = false → helper "Year parameter sales.zero"] [helper "Part V applies: you (and/or your spouse if filing jointly) were born before January 2, 1961, and have a valid SSN, not married filing separately" = true → helper "Figured: Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part5",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part5",{"const":true}],"op":"test"},"then":"s1a.senior_over_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Fill out Schedule 1-A, Part V, only if"; p. 110, Part V Enhanced Deduction for Seniors, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.senior_magi_over`

- **Authored helper label:** Is the amount on line 31 more than the amount on line 32?
- **Encoded (Bool):** line 31 > line 32
- Expr: `{"gt":["s1a.senior_magi","s1a.senior_threshold"],"op":"test"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 33, "If zero or less, enter $6,000 on line 35" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.senior_over_pos`

- **Authored helper label:** Line 33 if more than zero, otherwise zero
- **Encoded (NonNegDollars):** Subtract line 32 from line 31. If zero or less, enter -0-.
- Expr: `{"from":"s1a.senior_magi","op":"subtract_floor0","take":"s1a.senior_threshold"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 33, "Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.senior_reduction_calc`

- **Authored helper label:** Figured: Multiply line 33 by 6% (0.06)
- **Encoded (NonNegDollars):** Multiply helper "Line 33 if more than zero, otherwise zero" by 6% (0.06) (s1a.senior_rate).
- Expr: `{"amount":"s1a.senior_over_pos","op":"multiply_rate","rate":{"param":"s1a.senior_rate"}}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 34 (2025; created 2025-11-04; sha256 64f97b38)

## 34 — `s1a.senior_reduction`

- **IRS:** Multiply line 33 by 6% (0.06)
- **Encoded (NonNegDollars):** Choose — [helper "Part V applies: you (and/or your spouse if filing jointly) were born before January 2, 1961, and have a valid SSN, not married filing separately" = false → helper "Year parameter sales.zero"] [helper "Part V applies: you (and/or your spouse if filing jointly) were born before January 2, 1961, and have a valid SSN, not married filing separately" = true → helper "Figured: Multiply line 33 by 6% (0.06)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part5",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part5",{"const":true}],"op":"test"},"then":"s1a.senior_reduction_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Fill out Schedule 1-A, Part V, only if"; p. 110, Part V Enhanced Deduction for Seniors, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.senior_amount`

- **Authored helper label:** Year parameter s1a.senior_amount ($6,000)
- **Encoded (NonNegDollars):** Enter $6,000 (s1a.senior_amount).
- Expr: `{"op":"param","ref":"s1a.senior_amount"}`
- Cite: [f1040s1a] Schedule 1-A (2025), lines 33 and 35, $6,000 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.senior_phased_figured`

- **Authored helper label:** Subtract line 34 from $6,000. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract line 34 from helper "Year parameter s1a.senior_amount ($6,000)". If zero or less, enter -0-.
- Expr: `{"from":"s1a.senior_amount","op":"subtract_floor0","take":"s1a.senior_reduction"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 35 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.senior_phased_calc`

- **Authored helper label:** Figured: Subtract line 34 from $6,000. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Choose — [helper "Is the amount on line 31 more than the amount on line 32?" = false → helper "Year parameter s1a.senior_amount ($6,000)"] [helper "Is the amount on line 31 more than the amount on line 32?" = true → helper "Subtract line 34 from $6,000. If zero or less, enter -0-"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.senior_magi_over",{"const":false}],"op":"test"},"then":"s1a.senior_amount"},{"guard":{"eq":["s1a.senior_magi_over",{"const":true}],"op":"test"},"then":"s1a.senior_phased_figured"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 35, "Subtract line 34 from $6,000. If zero or less, enter -0-", line 33, "If zero or less, enter $6,000 on line 35" (2025; created 2025-11-04; sha256 64f97b38)

## 35 — `s1a.senior_phased`

- **IRS:** Subtract line 34 from $6,000. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Choose — [helper "Part V applies: you (and/or your spouse if filing jointly) were born before January 2, 1961, and have a valid SSN, not married filing separately" = false → helper "Year parameter sales.zero"] [helper "Part V applies: you (and/or your spouse if filing jointly) were born before January 2, 1961, and have a valid SSN, not married filing separately" = true → helper "Figured: Subtract line 34 from $6,000. If zero or less, enter -0-"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part5",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part5",{"const":true}],"op":"test"},"then":"s1a.senior_phased_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Fill out Schedule 1-A, Part V, only if"; p. 110, Part V Enhanced Deduction for Seniors, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.died_before_65_count`

- **Authored helper label:** Your entry, if you were born between January 2, 1960, and January 1, 1961, and died in 2025 before reaching age 65
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'taxpayer' and helper "The final return of a person who died in 2025 before reaching age 65 (asked only of a person born in 1960, or on January 1, 1961; otherwise no)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"all":[{"eq":["person.role",{"const":"taxpayer"}],"op":"test"},{"eq":["person.died_before_65",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Death of a taxpayer in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.died_before_65`

- **Authored helper label:** You were born between January 2, 1960, and January 1, 1961, and died in 2025 before reaching age 65
- **Encoded (Bool):** helper "Your entry, if you were born between January 2, 1960, and January 1, 1961, and died in 2025 before reaching age 65" > 0 (a count)
- Expr: `{"gt":["s1a.died_before_65_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Death of a taxpayer in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `s1a.senior_decedent`

- **Authored helper label:** A filer who died in 2025 before reaching age 65
- **Encoded (Bool):** helper "You were born between January 2, 1960, and January 1, 1961, and died in 2025 before reaching age 65" = true
- Expr: `{"eq":["s1a.died_before_65",{"const":true}],"op":"test"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Death of a taxpayer in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.senior_you_born`

- **Authored helper label:** Line 36a for a filer born before January 2, 1961
- **Encoded (NonNegDollars):** Choose — [household helper "Do you have an SSN valid for employment issued before the due date of your return?" = false → helper "Year parameter sales.zero"] [household helper "Do you have an SSN valid for employment issued before the due date of your return?" = true → line 35]
- **Refusal:** when s1a.senior_decedent is true, cannot complete Enhanced deduction for seniors on the final return of a person who died in 2025 before reaching age 65. A person born before January 2, 1961, who died in 2025 before reaching age 65 does not qualify; this case is outside this tool. Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Death of a taxpayer in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"alternatives":[{"guard":{"eq":["household.taxpayer_work_ssn",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["household.taxpayer_work_ssn",{"const":true}],"op":"test"},"then":"s1a.senior_phased"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 36a (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.senior_you_claim`

- **Authored helper label:** Line 36a for a filer born before January 2, 1961: zero for married filing separately
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → helper "Line 36a for a filer born before January 2, 1961"] [f1040 line Filing Status = 'mfj' → helper "Line 36a for a filer born before January 2, 1961"] [f1040 line Filing Status = 'mfs' → helper "Year parameter sales.zero"] [f1040 line Filing Status = 'hoh' → helper "Line 36a for a filer born before January 2, 1961"] [f1040 line Filing Status = 'qss' → helper "Line 36a for a filer born before January 2, 1961"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"s1a.senior_you_born"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"s1a.senior_you_born"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"s1a.senior_you_born"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"s1a.senior_you_born"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), Part V caution, "If married, you must file jointly to claim this deduction" (2025; created 2025-11-04; sha256 64f97b38)

## 36a — `s1a.senior_you`

- **IRS:** If you have a valid social security number (see instructions) and were born before January 2, 1961, enter the amount from line 35
- **Encoded (NonNegDollars):** Choose — [sa helper "Were you born before January 2, 1961?" = false → helper "Year parameter sales.zero"] [sa helper "Were you born before January 2, 1961?" = true → helper "Line 36a for a filer born before January 2, 1961: zero for married filing separately"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.age65",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["sa.age65",{"const":true}],"op":"test"},"then":"s1a.senior_you_claim"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 36a (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.spouse_senior_count`

- **Authored helper label:** Your spouse, if born before January 2, 1961, with a valid SSN
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Your spouse's entry, if your spouse was born before January 2, 1961, and has a valid SSN" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"eq":["person.spouse_senior_work_ssn",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Fill out Schedule 1-A, Part V, only if" and "If you are married filing jointly, the spouse who is claiming the enhanced deduction for seniors must have a valid SSN" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.spouse_senior`

- **Authored helper label:** Your spouse was born before January 2, 1961, and has a valid SSN
- **Encoded (Bool):** helper "Your spouse, if born before January 2, 1961, with a valid SSN" > 0 (a count)
- Expr: `{"gt":["s1a.spouse_senior_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Fill out Schedule 1-A, Part V, only if" and "If you are married filing jointly, the spouse who is claiming the enhanced deduction for seniors must have a valid SSN" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.spouse_died_before_65_count`

- **Authored helper label:** Your spouse's entry, if your spouse was born between January 2, 1960, and January 1, 1961, and died in 2025 before reaching age 65
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'spouse' and helper "The final return of a person who died in 2025 before reaching age 65 (asked only of a person born in 1960, or on January 1, 1961; otherwise no)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"all":[{"eq":["person.role",{"const":"spouse"}],"op":"test"},{"eq":["person.died_before_65",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Death of a taxpayer in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.spouse_died_before_65`

- **Authored helper label:** Your spouse was born between January 2, 1960, and January 1, 1961, and died in 2025 before reaching age 65
- **Encoded (Bool):** helper "Your spouse's entry, if your spouse was born between January 2, 1960, and January 1, 1961, and died in 2025 before reaching age 65" > 0 (a count)
- Expr: `{"gt":["s1a.spouse_died_before_65_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Death of a taxpayer in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `s1a.spouse_senior_decedent`

- **Authored helper label:** A spouse who died in 2025 before reaching age 65
- **Encoded (Bool):** helper "Your spouse was born between January 2, 1960, and January 1, 1961, and died in 2025 before reaching age 65" = true
- Expr: `{"eq":["s1a.spouse_died_before_65",{"const":true}],"op":"test"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Death of a taxpayer in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.senior_spouse_born`

- **Authored helper label:** Line 36b for a spouse born before January 2, 1961, with a valid SSN
- **Encoded (NonNegDollars):** Enter the amount from line 35.
- **Refusal:** when s1a.spouse_senior_decedent is true, cannot complete Enhanced deduction for seniors on the final return of a person who died in 2025 before reaching age 65. A person born before January 2, 1961, who died in 2025 before reaching age 65 does not qualify; this case is outside this tool. Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Death of a taxpayer in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"from":"s1a.senior_phased","op":"copy"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 36b (2025; created 2025-11-04; sha256 64f97b38)

## 36b — `s1a.senior_spouse`

- **IRS:** If you are married filing jointly, your spouse has a valid social security number (see instructions), and your spouse was born before January 2, 1961, enter the amount from line 35
- **Encoded (NonNegDollars):** Choose — [helper "Your spouse was born before January 2, 1961, and has a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Your spouse was born before January 2, 1961, and has a valid SSN" = true → helper "Line 36b for a spouse born before January 2, 1961, with a valid SSN"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.spouse_senior",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.spouse_senior",{"const":true}],"op":"test"},"then":"s1a.senior_spouse_born"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 36b; i1040gi p. 110, "The maximum amount of the enhanced deduction for seniors is $6,000 per person" (2025; created 2025-11-04; sha256 64f97b38)

## 37 — `s1a.senior_deduction`

- **IRS:** Enhanced deduction for seniors. Add lines 36a and 36b
- **Encoded (NonNegDollars):** Add line 36a and line 36b.
- Expr: `{"of":["s1a.senior_you","s1a.senior_spouse"],"op":"sum"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 37 (2025; created 2025-11-04; sha256 64f97b38)

## 38 — `s1a.total_deductions`

- **IRS:** Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, or on Form 1040-NR, line 13c
- **Encoded (NonNegDollars):** Add line 13, line 21, line 30, and line 37.
- Expr: `{"of":["s1a.tips_deduction","s1a.ot_deduction","s1a.vli_deduction","s1a.senior_deduction"],"op":"sum"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 38 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.no`

- **Authored helper label:** Year parameter household.no (false)
- **Encoded (Bool):** Enter false (household.no).
- Expr: `{"op":"param","ref":"household.no"}`
- Cite: [f1040s1a] Schedule 1-A (2025) (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.part2_ssn`

- **Authored helper label:** Part II, once qualified tips are claimed: not married filing separately, and a person who received them has a valid SSN
- **Encoded (Bool):** Choose — [f1040 line Filing Status = 'single' → helper "You have a valid SSN or, if married filing jointly, a spouse who received them has a valid SSN"] [f1040 line Filing Status = 'mfj' → helper "You have a valid SSN or, if married filing jointly, a spouse who received them has a valid SSN"] [f1040 line Filing Status = 'mfs' → helper "Year parameter household.no (false)"] [f1040 line Filing Status = 'hoh' → helper "You have a valid SSN or, if married filing jointly, a spouse who received them has a valid SSN"] [f1040 line Filing Status = 'qss' → helper "You have a valid SSN or, if married filing jointly, a spouse who received them has a valid SSN"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"s1a.tip_ssn"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"s1a.tip_ssn"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"s1a.no"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"s1a.tip_ssn"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"s1a.tip_ssn"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; p. 101, Part II No Tax on Tips, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.part3_ssn`

- **Authored helper label:** Part III, once qualified overtime is claimed: not married filing separately, and a person who received it has a valid SSN
- **Encoded (Bool):** Choose — [f1040 line Filing Status = 'single' → helper "You have a valid SSN or, if married filing jointly, a spouse who received it has a valid SSN"] [f1040 line Filing Status = 'mfj' → helper "You have a valid SSN or, if married filing jointly, a spouse who received it has a valid SSN"] [f1040 line Filing Status = 'mfs' → helper "Year parameter household.no (false)"] [f1040 line Filing Status = 'hoh' → helper "You have a valid SSN or, if married filing jointly, a spouse who received it has a valid SSN"] [f1040 line Filing Status = 'qss' → helper "You have a valid SSN or, if married filing jointly, a spouse who received it has a valid SSN"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"s1a.ot_ssn"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"s1a.ot_ssn"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"s1a.no"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"s1a.ot_ssn"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"s1a.ot_ssn"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if"; p. 106, Part III No Tax on Overtime, "If you are married, you must file a joint return with your spouse to claim this deduction" (2025; printed date 2026-02-25; sha256 482e9c48)
