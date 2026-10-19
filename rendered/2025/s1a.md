# Schedule 1-A (Form 1040) — Additional Deductions

- Document: `s1a` (form, tax year 2025)
- Note: For an unmarried filer (married filing statuses are refused through s3.married). Tips and overtime as an employee only, by the methods the instructions give for 2025; tips or overtime in a trade or business, Form 4137, and excluded Puerto Rico income or Forms 2555 and 4563 are refused. Lines 11, 19 and 28 (a whole number of $1,000 units) are kept as that many thousands of dollars; lines 12, 20 and 29 multiply them by $100 or $200 per thousand.

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

- **Authored helper label:** Did you receive qualified tips as an employee in 2025 that you want to deduct?
- **Encoded (Bool):** Input — Did you receive tips as an employee in 2025 in an occupation on the IRS list of occupations that customarily and regularly received tips (IRS.gov/TippedOccupations) that you want to deduct on Schedule 1-A, Part II? (Tips received as a non-employee, in your own trade or business, are asked about with Schedule C.)
- Expr: `{"op":"input","source":"Did you receive tips as an employee in 2025 in an occupation on the IRS list of occupations that customarily and regularly received tips (IRS.gov/TippedOccupations) that you want to deduct on Schedule 1-A, Part II? (Tips received as a non-employee, in your own trade or business, are asked about with Schedule C.)"}`
- Cite: [i1040gi] pp. 101-103, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tip_employers`

- **Authored helper label:** Number of employers on the Qualified Tips From More Than One Employer Worksheet
- **Encoded (Count):** Add tipjob.one over every confirmed tipjob entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"tipjob","field":"tipjob.one","op":"sum_over"}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 4c (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tip_total`

- **Authored helper label:** Worksheet line 2. Add lines 1A through 1E, column (d)
- **Encoded (NonNegDollars):** Add tipjob.col_d over every confirmed tipjob entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"tipjob","field":"tipjob.col_d","op":"sum_over"}`
- Cite: [i1040gi] p. 104, Qualified Tips From More Than One Employer Worksheet, line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tip_reported`

- **Authored helper label:** Worksheet column (b) total: qualified tips reported on Form W-2 or on Forms 4070
- **Encoded (NonNegDollars):** Add tipjob.amount over every confirmed tipjob entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"tipjob","field":"tipjob.amount","op":"sum_over"}`
- Cite: [i1040gi] p. 104, Qualified Tips From More Than One Employer Worksheet, column (b); p. 103, methods 1 to 3, "Enter this amount on line 4a" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.tip_multi`

- **Authored helper label:** Tips from more than one employer
- **Encoded (Bool):** helper "Number of employers on the Qualified Tips From More Than One Employer Worksheet" > 1 (ss.one)
- Expr: `{"gt":["s1a.tip_employers",{"param":"ss.one"}],"op":"test"}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 4a, "If you received qualified tips as an employee with respect to employment with more than one employer, enter -0- on line 4a" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.part2`

- **Authored helper label:** Part II applies: qualified tips claimed, not married filing separately, a valid SSN
- **Encoded (Bool):** helper "Did you receive qualified tips as an employee in 2025 that you want to deduct?" = true and f1040 line Filing Status ≠ 'mfs' and household helper "Do you have an SSN valid for employment issued before the due date of your return?" = true
- Expr: `{"all":[{"eq":["s1a.tips",{"const":true}],"op":"test"},{"ne":["f1040.status",{"const":"mfs"}],"op":"test"},{"eq":["household.taxpayer_work_ssn",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; Part II caution, "If married, you must file jointly" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line4a_calc`

- **Authored helper label:** Figured: Enter qualified tips included on Form W-2, box 7, but see the instructions if Form W-2, box 5 is more than $176,100 or you received tips that are not subject to social security and Medicare taxes
- **Encoded (NonNegDollars):** Choose — [helper "Tips from more than one employer" = true → helper "Year parameter sales.zero"] [helper "Tips from more than one employer" = false → helper "Worksheet column (b) total: qualified tips reported on Form W-2 or on Forms 4070"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.tip_multi",{"const":true}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.tip_multi",{"const":false}],"op":"test"},"then":"s1a.tip_reported"}],"op":"choose"}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 4a; pp. 103-104, methods 1 to 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## 4a — `s1a.line4a`

- **IRS:** Enter qualified tips included on Form W-2, box 7, but see the instructions if Form W-2, box 5 is more than $176,100 or you received tips that are not subject to social security and Medicare taxes
- **Encoded (NonNegDollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = true → helper "Figured: Enter qualified tips included on Form W-2, box 7, but see the instructions if Form W-2, box 5 is more than $176,100 or you received tips that are not subject to social security and Medicare taxes"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.line4a_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; Part II caution, "If married, you must file jointly" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line4b_calc`

- **Authored helper label:** Figured: Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed, enter -0-
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- **Refusal:** when s2.other is true, cannot complete Form 4137 (Social Security and Medicare Tax on Unreported Tip Income). Tips reported on Form 4137 are outside this tool. Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "If you received cash and charge tips of $20 or more in a calendar month and didn't report all of those tips to your employer, you must file Form 4137"; p. 104, line 4b (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 4b (2025; printed date 2026-02-25; sha256 482e9c48)

## 4b — `s1a.line4b`

- **IRS:** Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed, enter -0-
- **Encoded (NonNegDollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = true → helper "Figured: Qualified tips included on Form 4137, line 1, row A, column (c). If Form 4137 is not filed, enter -0-"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.line4b_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; Part II caution, "If married, you must file jointly" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line4c_one`

- **Authored helper label:** Line 4c with one employer: the larger of line 4a or line 4b
- **Encoded (NonNegDollars):** Enter the larger of line 4a or line 4b.
- Expr: `{"of":["s1a.line4a","s1a.line4b"],"op":"larger_of"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 4c (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line4c_calc`

- **Authored helper label:** Figured: If you only received qualified tips as an employee with respect to employment with one employer, enter the larger of line 4a or line 4b. Otherwise, see the instructions to determine the amount to enter on line 4c
- **Encoded (NonNegDollars):** Choose — [helper "Tips from more than one employer" = true → helper "Worksheet line 2. Add lines 1A through 1E, column (d)"] [helper "Tips from more than one employer" = false → helper "Line 4c with one employer: the larger of line 4a or line 4b"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.tip_multi",{"const":true}],"op":"test"},"then":"s1a.tip_total"},{"guard":{"eq":["s1a.tip_multi",{"const":false}],"op":"test"},"then":"s1a.line4c_one"}],"op":"choose"}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 4c, and the Qualified Tips From More Than One Employer Worksheet (2025; printed date 2026-02-25; sha256 482e9c48)

## 4c — `s1a.line4c`

- **IRS:** If you only received qualified tips as an employee with respect to employment with one employer, enter the larger of line 4a or line 4b. Otherwise, see the instructions to determine the amount to enter on line 4c
- **Encoded (NonNegDollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = true → helper "Figured: If you only received qualified tips as an employee with respect to employment with one employer, enter the larger of line 4a or line 4b. Otherwise, see the instructions to determine the amount to enter on line 4c"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.line4c_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; Part II caution, "If married, you must file jointly" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line5_calc`

- **Authored helper label:** Figured: Qualified tips received in the course of a trade or business
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- **Refusal:** when scope.schedule1 is true, cannot complete Schedule 1-A, line 5 (qualified tips in a trade or business, with Schedule C, E or F). Income from a trade or business is outside this tool. Cite: [i1040gi] p. 104, Schedule 1-A, line 5, and the Multiple Trades or Businesses Worksheet (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## 5 — `s1a.line5`

- **IRS:** Qualified tips received in the course of a trade or business
- **Encoded (NonNegDollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = true → helper "Figured: Qualified tips received in the course of a trade or business"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.line5_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; Part II caution, "If married, you must file jointly" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line6_calc`

- **Authored helper label:** Figured: Add lines 4c and 5
- **Encoded (NonNegDollars):** Add line 4c and line 5.
- Expr: `{"of":["s1a.line4c","s1a.line5"],"op":"sum"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 6 (2025; created 2025-11-04; sha256 64f97b38)

## 6 — `s1a.line6`

- **IRS:** Add lines 4c and 5
- **Encoded (NonNegDollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = true → helper "Figured: Add lines 4c and 5"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.line6_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; Part II caution, "If married, you must file jointly" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line7_calc`

- **Authored helper label:** Figured: Enter the smaller of the amount on line 6 or $25,000
- **Encoded (NonNegDollars):** Enter the smaller of line 6 or helper "Year parameter s1a.tips_max ($25,000)".
- Expr: `{"of":["s1a.line6","s1a.tips_max"],"op":"smaller_of"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 7 (2025; created 2025-11-04; sha256 64f97b38)

## 7 — `s1a.line7`

- **IRS:** Enter the smaller of the amount on line 6 or $25,000
- **Encoded (NonNegDollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = true → helper "Figured: Enter the smaller of the amount on line 6 or $25,000"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.line7_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; Part II caution, "If married, you must file jointly" (2025; printed date 2026-02-25; sha256 482e9c48)

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

## (helper) — `s1a.line8_calc`

- **Authored helper label:** Figured: Enter the amount from line 3
- **Encoded (Dollars):** Enter the amount from line 3.
- Expr: `{"from":"s1a.line3","op":"copy"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 8 (2025; created 2025-11-04; sha256 64f97b38)

## 8 — `s1a.line8`

- **IRS:** Enter the amount from line 3
- **Encoded (Dollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = true → helper "Figured: Enter the amount from line 3"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.line8_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; Part II caution, "If married, you must file jointly" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line9_calc`

- **Authored helper label:** Figured: Enter $150,000 ($300,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → helper "Year parameter s1a.base_other ($150,000)"] [f1040 line Filing Status = 'mfj' → helper "Year parameter s1a.base_joint ($300,000)"] [f1040 line Filing Status = 'mfs' → helper "Year parameter s1a.base_other ($150,000)"] [f1040 line Filing Status = 'hoh' → helper "Year parameter s1a.base_other ($150,000)"] [f1040 line Filing Status = 'qss' → helper "Year parameter s1a.base_other ($150,000)"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"s1a.base_other"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"s1a.base_joint"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"s1a.base_other"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"s1a.base_other"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"s1a.base_other"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 9 (2025; created 2025-11-04; sha256 64f97b38)

## 9 — `s1a.line9`

- **IRS:** Enter $150,000 ($300,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = true → helper "Figured: Enter $150,000 ($300,000 if married filing jointly)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.line9_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; Part II caution, "If married, you must file jointly" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line10_calc`

- **Authored helper label:** Figured: Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13
- **Encoded (Dollars):** Subtract line 9 from line 8.
- Expr: `{"from":"s1a.line8","op":"subtract","take":"s1a.line9"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 10 (2025; created 2025-11-04; sha256 64f97b38)

## 10 — `s1a.line10`

- **IRS:** Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13
- **Encoded (Dollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = true → helper "Figured: Subtract line 9 from line 8. If zero or less, enter the amount from line 7 on line 13"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.line10_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; Part II caution, "If married, you must file jointly" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line10_over`

- **Authored helper label:** Is the amount on line 8 more than the amount on line 9?
- **Encoded (Bool):** line 8 > line 9
- Expr: `{"gt":["s1a.line8","s1a.line9"],"op":"test"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 10, "If zero or less" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line10_pos`

- **Authored helper label:** Line 10 if more than zero, otherwise zero
- **Encoded (NonNegDollars):** Subtract line 9 from line 8. If zero or less, enter -0-.
- Expr: `{"from":"s1a.line8","op":"subtract_floor0","take":"s1a.line9"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 10 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line11_thousands`

- **Authored helper label:** Line 11. Divide line 10 by $1,000, decreasing the result to the next lower whole number (kept as that many thousands of dollars)
- **Encoded (NonNegDollars):** Round helper "Line 10 if more than zero, otherwise zero" down to a multiple of $1,000.
- Expr: `{"of":"s1a.line10_pos","op":"round","rule":"down","unit":100000}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 11 (the whole number of $1,000 units, kept as that many thousands of dollars) (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line12_calc`

- **Authored helper label:** Figured: Multiply line 11 by $100
- **Encoded (NonNegDollars):** Multiply helper "Line 11. Divide line 10 by $1,000, decreasing the result to the next lower whole number (kept as that many thousands of dollars)" by 1/10 (s1a.hundred_per_thousand).
- Expr: `{"amount":"s1a.line11_thousands","op":"multiply_rate","rate":{"param":"s1a.hundred_per_thousand"}}`
- Cite: [f1040s1a] Schedule 1-A (2025), lines 11 and 12 (2025; created 2025-11-04; sha256 64f97b38)

## 12 — `s1a.line12`

- **IRS:** Multiply line 11 by $100
- **Encoded (NonNegDollars):** Choose — [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part II applies: qualified tips claimed, not married filing separately, a valid SSN" = true → helper "Figured: Multiply line 11 by $100"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part2",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part2",{"const":true}],"op":"test"},"then":"s1a.line12_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if"; Part II caution, "If married, you must file jointly" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line13_figured`

- **Authored helper label:** Subtract line 12 from line 7. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract line 12 from line 7. If zero or less, enter -0-.
- Expr: `{"from":"s1a.line7","op":"subtract_floor0","take":"s1a.line12"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 13 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line13_amount`

- **Authored helper label:** Line 13 when Part II applies
- **Encoded (NonNegDollars):** Choose — [helper "Is the amount on line 8 more than the amount on line 9?" = false → line 7] [helper "Is the amount on line 8 more than the amount on line 9?" = true → helper "Subtract line 12 from line 7. If zero or less, enter -0-"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.line10_over",{"const":false}],"op":"test"},"then":"s1a.line7"},{"guard":{"eq":["s1a.line10_over",{"const":true}],"op":"test"},"then":"s1a.line13_figured"}],"op":"choose"}`
- Cite: [i1040gi] p. 105, Schedule 1-A, line 10, "If the amount on line 10 is zero or less ... Skip lines 11 and 12 and enter the amount from Schedule 1-A, line 7, on Schedule 1-A, line 13" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line13_ssn`

- **Authored helper label:** Line 13 with qualified tips: zero without a valid SSN
- **Encoded (NonNegDollars):** Choose — [household helper "Do you have an SSN valid for employment issued before the due date of your return?" = false → helper "Year parameter sales.zero"] [household helper "Do you have an SSN valid for employment issued before the due date of your return?" = true → helper "Line 13 when Part II applies"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.taxpayer_work_ssn",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["household.taxpayer_work_ssn",{"const":true}],"op":"test"},"then":"s1a.line13_amount"}],"op":"choose"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "Fill out Schedule 1-A, Part II, only if: ... You have a valid social security number (SSN)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line13_claim`

- **Authored helper label:** Line 13 with qualified tips: zero for married filing separately
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → helper "Line 13 with qualified tips: zero without a valid SSN"] [f1040 line Filing Status = 'mfj' → helper "Line 13 with qualified tips: zero without a valid SSN"] [f1040 line Filing Status = 'mfs' → helper "Year parameter sales.zero"] [f1040 line Filing Status = 'hoh' → helper "Line 13 with qualified tips: zero without a valid SSN"] [f1040 line Filing Status = 'qss' → helper "Line 13 with qualified tips: zero without a valid SSN"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"s1a.line13_ssn"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"s1a.line13_ssn"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"s1a.line13_ssn"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"s1a.line13_ssn"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), Part II caution, "If married, you must file jointly to claim this deduction" (2025; created 2025-11-04; sha256 64f97b38)

## 13 — `s1a.line13`

- **IRS:** Qualified tips deduction. Subtract line 12 from line 7. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Choose — [helper "Did you receive qualified tips as an employee in 2025 that you want to deduct?" = false → helper "Year parameter sales.zero"] [helper "Did you receive qualified tips as an employee in 2025 that you want to deduct?" = true → helper "Line 13 with qualified tips: zero for married filing separately"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.tips",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.tips",{"const":true}],"op":"test"},"then":"s1a.line13_claim"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 13; i1040gi p. 101, "Fill out Schedule 1-A, Part II, only if" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.overtime`

- **Authored helper label:** Did you receive qualified overtime compensation in 2025 that you want to deduct?
- **Encoded (Bool):** Input — Did you receive overtime pay as an employee in 2025 that you want to deduct on Schedule 1-A, Part III (the FLSA Overtime Premium, generally the "half" of time-and-a-half)? (Overtime reported to you on Form 1099-NEC or 1099-MISC is asked about with Schedule C.)
- Expr: `{"op":"input","source":"Did you receive overtime pay as an employee in 2025 that you want to deduct on Schedule 1-A, Part III (the FLSA Overtime Premium, generally the \"half\" of time-and-a-half)? (Overtime reported to you on Form 1099-NEC or 1099-MISC is asked about with Schedule C.)"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.part3`

- **Authored helper label:** Part III applies: qualified overtime claimed, not married filing separately, a valid SSN
- **Encoded (Bool):** helper "Did you receive qualified overtime compensation in 2025 that you want to deduct?" = true and f1040 line Filing Status ≠ 'mfs' and household helper "Do you have an SSN valid for employment issued before the due date of your return?" = true
- Expr: `{"all":[{"eq":["s1a.overtime",{"const":true}],"op":"test"},{"ne":["f1040.status",{"const":"mfs"}],"op":"test"},{"eq":["household.taxpayer_work_ssn",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if"; Part III caution (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line14a_calc`

- **Authored helper label:** Figured: Qualified overtime compensation included in Form W-2, box 1. If you received qualified overtime compensation not reported on Form W-2, box 1, see instructions
- **Encoded (NonNegDollars):** Add otjob.col_b over every confirmed otjob entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"otjob","field":"otjob.col_b","op":"sum_over"}`
- Cite: [i1040gi] p. 108, Schedule 1-A, line 14a, and the Qualified Overtime Compensation From More Than One Employer Worksheet, line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## 14a — `s1a.line14a`

- **IRS:** Qualified overtime compensation included in Form W-2, box 1. If you received qualified overtime compensation not reported on Form W-2, box 1, see instructions
- **Encoded (NonNegDollars):** Choose — [helper "Part III applies: qualified overtime claimed, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part III applies: qualified overtime claimed, not married filing separately, a valid SSN" = true → helper "Figured: Qualified overtime compensation included in Form W-2, box 1. If you received qualified overtime compensation not reported on Form W-2, box 1, see instructions"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part3",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part3",{"const":true}],"op":"test"},"then":"s1a.line14a_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if"; Part III caution (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line14b_calc`

- **Authored helper label:** Figured: Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- **Refusal:** when scope.schedule1 is true, cannot complete Schedule 1-A, line 14b (qualified overtime reported on Form 1099-NEC or 1099-MISC, with Schedule C). Nonemployee compensation is outside this tool. Cite: [i1040gi] p. 108, Schedule 1-A, line 14b, and the Qualified Overtime Compensation From More Than One Payor Worksheet (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 108, Schedule 1-A, line 14b (2025; printed date 2026-02-25; sha256 482e9c48)

## 14b — `s1a.line14b`

- **IRS:** Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3
- **Encoded (NonNegDollars):** Choose — [helper "Part III applies: qualified overtime claimed, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part III applies: qualified overtime claimed, not married filing separately, a valid SSN" = true → helper "Figured: Qualified overtime compensation included in Form 1099-NEC, box 1, or Form 1099-MISC, box 3"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part3",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part3",{"const":true}],"op":"test"},"then":"s1a.line14b_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if"; Part III caution (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line14c_calc`

- **Authored helper label:** Figured: Add lines 14a and 14b
- **Encoded (NonNegDollars):** Add line 14a and line 14b.
- Expr: `{"of":["s1a.line14a","s1a.line14b"],"op":"sum"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 14c (2025; created 2025-11-04; sha256 64f97b38)

## 14c — `s1a.line14c`

- **IRS:** Add lines 14a and 14b
- **Encoded (NonNegDollars):** Choose — [helper "Part III applies: qualified overtime claimed, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part III applies: qualified overtime claimed, not married filing separately, a valid SSN" = true → helper "Figured: Add lines 14a and 14b"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part3",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part3",{"const":true}],"op":"test"},"then":"s1a.line14c_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if"; Part III caution (2025; printed date 2026-02-25; sha256 482e9c48)

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
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → helper "Year parameter s1a.ot_max_other ($12,500)"] [f1040 line Filing Status = 'mfj' → helper "Year parameter s1a.ot_max_joint ($25,000)"] [f1040 line Filing Status = 'mfs' → helper "Year parameter s1a.ot_max_other ($12,500)"] [f1040 line Filing Status = 'hoh' → helper "Year parameter s1a.ot_max_other ($12,500)"] [f1040 line Filing Status = 'qss' → helper "Year parameter s1a.ot_max_other ($12,500)"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"s1a.ot_max_other"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"s1a.ot_max_joint"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"s1a.ot_max_other"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"s1a.ot_max_other"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"s1a.ot_max_other"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 15 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line15_calc`

- **Authored helper label:** Figured: Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)
- **Encoded (NonNegDollars):** Enter the smaller of line 14c or helper "$12,500 ($25,000 if married filing jointly)".
- Expr: `{"of":["s1a.line14c","s1a.ot_max"],"op":"smaller_of"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 15 (2025; created 2025-11-04; sha256 64f97b38)

## 15 — `s1a.line15`

- **IRS:** Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [helper "Part III applies: qualified overtime claimed, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part III applies: qualified overtime claimed, not married filing separately, a valid SSN" = true → helper "Figured: Enter the smaller of the amount on line 14c or $12,500 ($25,000 if married filing jointly)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part3",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part3",{"const":true}],"op":"test"},"then":"s1a.line15_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if"; Part III caution (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line16_calc`

- **Authored helper label:** Figured: Enter the amount from line 3
- **Encoded (Dollars):** Enter the amount from line 3.
- Expr: `{"from":"s1a.line3","op":"copy"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 16 (2025; created 2025-11-04; sha256 64f97b38)

## 16 — `s1a.line16`

- **IRS:** Enter the amount from line 3
- **Encoded (Dollars):** Choose — [helper "Part III applies: qualified overtime claimed, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part III applies: qualified overtime claimed, not married filing separately, a valid SSN" = true → helper "Figured: Enter the amount from line 3"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part3",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part3",{"const":true}],"op":"test"},"then":"s1a.line16_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if"; Part III caution (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line17_calc`

- **Authored helper label:** Figured: Enter $150,000 ($300,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → helper "Year parameter s1a.base_other ($150,000)"] [f1040 line Filing Status = 'mfj' → helper "Year parameter s1a.base_joint ($300,000)"] [f1040 line Filing Status = 'mfs' → helper "Year parameter s1a.base_other ($150,000)"] [f1040 line Filing Status = 'hoh' → helper "Year parameter s1a.base_other ($150,000)"] [f1040 line Filing Status = 'qss' → helper "Year parameter s1a.base_other ($150,000)"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"s1a.base_other"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"s1a.base_joint"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"s1a.base_other"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"s1a.base_other"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"s1a.base_other"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 17 (2025; created 2025-11-04; sha256 64f97b38)

## 17 — `s1a.line17`

- **IRS:** Enter $150,000 ($300,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [helper "Part III applies: qualified overtime claimed, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part III applies: qualified overtime claimed, not married filing separately, a valid SSN" = true → helper "Figured: Enter $150,000 ($300,000 if married filing jointly)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part3",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part3",{"const":true}],"op":"test"},"then":"s1a.line17_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if"; Part III caution (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line18_calc`

- **Authored helper label:** Figured: Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21
- **Encoded (Dollars):** Subtract line 17 from line 16.
- Expr: `{"from":"s1a.line16","op":"subtract","take":"s1a.line17"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 18 (2025; created 2025-11-04; sha256 64f97b38)

## 18 — `s1a.line18`

- **IRS:** Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21
- **Encoded (Dollars):** Choose — [helper "Part III applies: qualified overtime claimed, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part III applies: qualified overtime claimed, not married filing separately, a valid SSN" = true → helper "Figured: Subtract line 17 from line 16. If zero or less, enter the amount from line 15 on line 21"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part3",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part3",{"const":true}],"op":"test"},"then":"s1a.line18_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if"; Part III caution (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line18_over`

- **Authored helper label:** Is the amount on line 16 more than the amount on line 17?
- **Encoded (Bool):** line 16 > line 17
- Expr: `{"gt":["s1a.line16","s1a.line17"],"op":"test"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 18, "If zero or less" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line18_pos`

- **Authored helper label:** Line 18 if more than zero, otherwise zero
- **Encoded (NonNegDollars):** Subtract line 17 from line 16. If zero or less, enter -0-.
- Expr: `{"from":"s1a.line16","op":"subtract_floor0","take":"s1a.line17"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 18 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line19_thousands`

- **Authored helper label:** Line 19. Divide line 18 by $1,000, decreasing the result to the next lower whole number (kept as that many thousands of dollars)
- **Encoded (NonNegDollars):** Round helper "Line 18 if more than zero, otherwise zero" down to a multiple of $1,000.
- Expr: `{"of":"s1a.line18_pos","op":"round","rule":"down","unit":100000}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 19 (the whole number of $1,000 units, kept as that many thousands of dollars) (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line20_calc`

- **Authored helper label:** Figured: Multiply line 19 by $100
- **Encoded (NonNegDollars):** Multiply helper "Line 19. Divide line 18 by $1,000, decreasing the result to the next lower whole number (kept as that many thousands of dollars)" by 1/10 (s1a.hundred_per_thousand).
- Expr: `{"amount":"s1a.line19_thousands","op":"multiply_rate","rate":{"param":"s1a.hundred_per_thousand"}}`
- Cite: [f1040s1a] Schedule 1-A (2025), lines 19 and 20 (2025; created 2025-11-04; sha256 64f97b38)

## 20 — `s1a.line20`

- **IRS:** Multiply line 19 by $100
- **Encoded (NonNegDollars):** Choose — [helper "Part III applies: qualified overtime claimed, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part III applies: qualified overtime claimed, not married filing separately, a valid SSN" = true → helper "Figured: Multiply line 19 by $100"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part3",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part3",{"const":true}],"op":"test"},"then":"s1a.line20_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if"; Part III caution (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line21_figured`

- **Authored helper label:** Subtract line 20 from line 15. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract line 20 from line 15. If zero or less, enter -0-.
- Expr: `{"from":"s1a.line15","op":"subtract_floor0","take":"s1a.line20"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 21 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line21_amount`

- **Authored helper label:** Line 21 when Part III applies
- **Encoded (NonNegDollars):** Choose — [helper "Is the amount on line 16 more than the amount on line 17?" = false → line 15] [helper "Is the amount on line 16 more than the amount on line 17?" = true → helper "Subtract line 20 from line 15. If zero or less, enter -0-"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.line18_over",{"const":false}],"op":"test"},"then":"s1a.line15"},{"guard":{"eq":["s1a.line18_over",{"const":true}],"op":"test"},"then":"s1a.line21_figured"}],"op":"choose"}`
- Cite: [i1040gi] p. 108, Schedule 1-A, line 18, "If the amount on line 18 is zero or less ... Skip lines 19 and 20 and enter the amount from Schedule 1-A, line 15, on Schedule 1-A, line 21" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line21_ssn`

- **Authored helper label:** Line 21 with qualified overtime: zero without a valid SSN
- **Encoded (NonNegDollars):** Choose — [household helper "Do you have an SSN valid for employment issued before the due date of your return?" = false → helper "Year parameter sales.zero"] [household helper "Do you have an SSN valid for employment issued before the due date of your return?" = true → helper "Line 21 when Part III applies"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.taxpayer_work_ssn",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["household.taxpayer_work_ssn",{"const":true}],"op":"test"},"then":"s1a.line21_amount"}],"op":"choose"}`
- Cite: [i1040gi] p. 106, Schedule 1-A, Part III, "Fill out Schedule 1-A, Part III, only if: ... You have a valid social security number (SSN)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line21_claim`

- **Authored helper label:** Line 21 with qualified overtime: zero for married filing separately
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → helper "Line 21 with qualified overtime: zero without a valid SSN"] [f1040 line Filing Status = 'mfj' → helper "Line 21 with qualified overtime: zero without a valid SSN"] [f1040 line Filing Status = 'mfs' → helper "Year parameter sales.zero"] [f1040 line Filing Status = 'hoh' → helper "Line 21 with qualified overtime: zero without a valid SSN"] [f1040 line Filing Status = 'qss' → helper "Line 21 with qualified overtime: zero without a valid SSN"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"s1a.line21_ssn"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"s1a.line21_ssn"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"s1a.line21_ssn"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"s1a.line21_ssn"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), Part III caution, "If married, you must file jointly to claim this deduction" (2025; created 2025-11-04; sha256 64f97b38)

## 21 — `s1a.line21`

- **IRS:** Qualified overtime compensation deduction. Subtract line 20 from line 15. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Choose — [helper "Did you receive qualified overtime compensation in 2025 that you want to deduct?" = false → helper "Year parameter sales.zero"] [helper "Did you receive qualified overtime compensation in 2025 that you want to deduct?" = true → helper "Line 21 with qualified overtime: zero for married filing separately"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.overtime",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.overtime",{"const":true}],"op":"test"},"then":"s1a.line21_claim"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 21; i1040gi p. 106, "Fill out Schedule 1-A, Part III, only if" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.carloan`

- **Authored helper label:** Did you pay or accrue interest in 2025 on a loan to buy a new passenger vehicle that you want to deduct?
- **Encoded (Bool):** Input — Did you pay or accrue interest in 2025 on a loan taken out after 2024 to buy a new car, minivan, van, SUV, pickup truck or motorcycle for personal use that you want to deduct on Schedule 1-A, Part IV?
- Expr: `{"op":"input","source":"Did you pay or accrue interest in 2025 on a loan taken out after 2024 to buy a new car, minivan, van, SUV, pickup truck or motorcycle for personal use that you want to deduct on Schedule 1-A, Part IV?"}`
- Cite: [i1040gi] p. 109, Schedule 1-A, Part IV, "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line23_total`

- **Authored helper label:** Add lines 22a and 22b, column (iii), and any further loans on the attached statement
- **Encoded (NonNegDollars):** Add carloan.col_iii over every confirmed carloan entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"carloan","field":"carloan.col_iii","op":"sum_over"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, line 22, "If you need to report more than two VINs, attach a statement" (2025; printed date 2026-02-25; sha256 482e9c48)

## 23 — `s1a.line23`

- **IRS:** Add lines 22a and 22b, column (iii)
- **Encoded (NonNegDollars):** Choose — [helper "Did you pay or accrue interest in 2025 on a loan to buy a new passenger vehicle that you want to deduct?" = false → helper "Year parameter sales.zero"] [helper "Did you pay or accrue interest in 2025 on a loan to buy a new passenger vehicle that you want to deduct?" = true → helper "Add lines 22a and 22b, column (iii), and any further loans on the attached statement"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.carloan",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.carloan",{"const":true}],"op":"test"},"then":"s1a.line23_total"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 23 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.car_max`

- **Authored helper label:** Year parameter s1a.car_max ($10,000)
- **Encoded (NonNegDollars):** Enter $10,000 (s1a.car_max).
- Expr: `{"op":"param","ref":"s1a.car_max"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 24, $10,000 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.part4`

- **Authored helper label:** Part IV applies: qualified passenger vehicle loan interest claimed
- **Encoded (Bool):** helper "Did you pay or accrue interest in 2025 on a loan to buy a new passenger vehicle that you want to deduct?" = true
- Expr: `{"eq":["s1a.carloan",{"const":true}],"op":"test"}`
- Cite: [i1040gi] p. 109, Schedule 1-A, Part IV, "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line24_calc`

- **Authored helper label:** Figured: Enter the smaller of the amount on line 23 or $10,000
- **Encoded (NonNegDollars):** Enter the smaller of line 23 or helper "Year parameter s1a.car_max ($10,000)".
- Expr: `{"of":["s1a.line23","s1a.car_max"],"op":"smaller_of"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 24 (2025; created 2025-11-04; sha256 64f97b38)

## 24 — `s1a.line24`

- **IRS:** Enter the smaller of the amount on line 23 or $10,000
- **Encoded (NonNegDollars):** Choose — [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = false → helper "Year parameter sales.zero"] [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = true → helper "Figured: Enter the smaller of the amount on line 23 or $10,000"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part4",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part4",{"const":true}],"op":"test"},"then":"s1a.line24_calc"}],"op":"choose"}`
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

## (helper) — `s1a.line25_calc`

- **Authored helper label:** Figured: Enter the amount from line 3
- **Encoded (Dollars):** Enter the amount from line 3.
- Expr: `{"from":"s1a.line3","op":"copy"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 25 (2025; created 2025-11-04; sha256 64f97b38)

## 25 — `s1a.line25`

- **IRS:** Enter the amount from line 3
- **Encoded (Dollars):** Choose — [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = false → helper "Year parameter sales.zero"] [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = true → helper "Figured: Enter the amount from line 3"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part4",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part4",{"const":true}],"op":"test"},"then":"s1a.line25_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 109, Schedule 1-A, Part IV, "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line26_calc`

- **Authored helper label:** Figured: Enter $100,000 ($200,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → helper "Year parameter s1a.car_base_other ($100,000)"] [f1040 line Filing Status = 'mfj' → helper "Year parameter s1a.car_base_joint ($200,000)"] [f1040 line Filing Status = 'mfs' → helper "Year parameter s1a.car_base_other ($100,000)"] [f1040 line Filing Status = 'hoh' → helper "Year parameter s1a.car_base_other ($100,000)"] [f1040 line Filing Status = 'qss' → helper "Year parameter s1a.car_base_other ($100,000)"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"s1a.car_base_other"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"s1a.car_base_joint"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"s1a.car_base_other"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"s1a.car_base_other"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"s1a.car_base_other"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 26 (2025; created 2025-11-04; sha256 64f97b38)

## 26 — `s1a.line26`

- **IRS:** Enter $100,000 ($200,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = false → helper "Year parameter sales.zero"] [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = true → helper "Figured: Enter $100,000 ($200,000 if married filing jointly)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part4",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part4",{"const":true}],"op":"test"},"then":"s1a.line26_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 109, Schedule 1-A, Part IV, "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line27_calc`

- **Authored helper label:** Figured: Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on line 30
- **Encoded (Dollars):** Subtract line 26 from line 25.
- Expr: `{"from":"s1a.line25","op":"subtract","take":"s1a.line26"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 27 (2025; created 2025-11-04; sha256 64f97b38)

## 27 — `s1a.line27`

- **IRS:** Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on line 30
- **Encoded (Dollars):** Choose — [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = false → helper "Year parameter sales.zero"] [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = true → helper "Figured: Subtract line 26 from line 25. If zero or less, enter the amount from line 24 on line 30"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part4",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part4",{"const":true}],"op":"test"},"then":"s1a.line27_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 109, Schedule 1-A, Part IV, "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line27_over`

- **Authored helper label:** Is the amount on line 25 more than the amount on line 26?
- **Encoded (Bool):** line 25 > line 26
- Expr: `{"gt":["s1a.line25","s1a.line26"],"op":"test"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 27, "If zero or less" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line27_pos`

- **Authored helper label:** Line 27 if more than zero, otherwise zero
- **Encoded (NonNegDollars):** Subtract line 26 from line 25. If zero or less, enter -0-.
- Expr: `{"from":"s1a.line25","op":"subtract_floor0","take":"s1a.line26"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 27 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line28_thousands`

- **Authored helper label:** Line 28. Divide line 27 by $1,000, increasing the result to the next higher whole number (kept as that many thousands of dollars)
- **Encoded (NonNegDollars):** Round helper "Line 27 if more than zero, otherwise zero" up to the next multiple of $1,000.
- Expr: `{"of":"s1a.line27_pos","op":"round","rule":"up","unit":100000}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 28 (the whole number of $1,000 units, kept as that many thousands of dollars) (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line29_calc`

- **Authored helper label:** Figured: Multiply line 28 by $200
- **Encoded (NonNegDollars):** Multiply helper "Line 28. Divide line 27 by $1,000, increasing the result to the next higher whole number (kept as that many thousands of dollars)" by 1/5 (s1a.two_hundred_per_thousand).
- Expr: `{"amount":"s1a.line28_thousands","op":"multiply_rate","rate":{"param":"s1a.two_hundred_per_thousand"}}`
- Cite: [f1040s1a] Schedule 1-A (2025), lines 28 and 29 (2025; created 2025-11-04; sha256 64f97b38)

## 29 — `s1a.line29`

- **IRS:** Multiply line 28 by $200
- **Encoded (NonNegDollars):** Choose — [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = false → helper "Year parameter sales.zero"] [helper "Part IV applies: qualified passenger vehicle loan interest claimed" = true → helper "Figured: Multiply line 28 by $200"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part4",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part4",{"const":true}],"op":"test"},"then":"s1a.line29_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 109, Schedule 1-A, Part IV, "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line30_figured`

- **Authored helper label:** Subtract line 29 from line 24. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract line 29 from line 24. If zero or less, enter -0-.
- Expr: `{"from":"s1a.line24","op":"subtract_floor0","take":"s1a.line29"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 30 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line30_amount`

- **Authored helper label:** Line 30 when Part IV applies
- **Encoded (NonNegDollars):** Choose — [helper "Is the amount on line 25 more than the amount on line 26?" = false → line 24] [helper "Is the amount on line 25 more than the amount on line 26?" = true → helper "Subtract line 29 from line 24. If zero or less, enter -0-"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.line27_over",{"const":false}],"op":"test"},"then":"s1a.line24"},{"guard":{"eq":["s1a.line27_over",{"const":true}],"op":"test"},"then":"s1a.line30_figured"}],"op":"choose"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, line 27, "If the amount on line 27 is zero or less ... Skip lines 28 and 29 and enter the amount from Schedule 1-A, line 24, on Schedule 1-A, line 30" (2025; printed date 2026-02-25; sha256 482e9c48)

## 30 — `s1a.line30`

- **IRS:** Qualified passenger vehicle loan interest deduction. Subtract line 29 from line 24. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Choose — [helper "Did you pay or accrue interest in 2025 on a loan to buy a new passenger vehicle that you want to deduct?" = false → helper "Year parameter sales.zero"] [helper "Did you pay or accrue interest in 2025 on a loan to buy a new passenger vehicle that you want to deduct?" = true → helper "Line 30 when Part IV applies"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.carloan",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.carloan",{"const":true}],"op":"test"},"then":"s1a.line30_amount"}],"op":"choose"}`
- Cite: [i1040gi] p. 109, Schedule 1-A, Part IV, "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.part5`

- **Authored helper label:** Part V applies: born before January 2, 1961, not married filing separately, a valid SSN
- **Encoded (Bool):** sa helper "Were you born before January 2, 1961?" = true and f1040 line Filing Status ≠ 'mfs' and household helper "Do you have an SSN valid for employment issued before the due date of your return?" = true
- Expr: `{"all":[{"eq":["sa.age65",{"const":true}],"op":"test"},{"ne":["f1040.status",{"const":"mfs"}],"op":"test"},{"eq":["household.taxpayer_work_ssn",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Fill out Schedule 1-A, Part V, only if"; Part V caution (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line31_calc`

- **Authored helper label:** Figured: Enter the amount from line 3
- **Encoded (Dollars):** Enter the amount from line 3.
- Expr: `{"from":"s1a.line3","op":"copy"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 31 (2025; created 2025-11-04; sha256 64f97b38)

## 31 — `s1a.line31`

- **IRS:** Enter the amount from line 3
- **Encoded (Dollars):** Choose — [helper "Part V applies: born before January 2, 1961, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part V applies: born before January 2, 1961, not married filing separately, a valid SSN" = true → helper "Figured: Enter the amount from line 3"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part5",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part5",{"const":true}],"op":"test"},"then":"s1a.line31_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Fill out Schedule 1-A, Part V, only if"; Part V caution (2025; printed date 2026-02-25; sha256 482e9c48)

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

## (helper) — `s1a.line32_calc`

- **Authored helper label:** Figured: Enter $75,000 ($150,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → helper "Year parameter s1a.senior_base_other ($75,000)"] [f1040 line Filing Status = 'mfj' → helper "Year parameter s1a.senior_base_joint ($150,000)"] [f1040 line Filing Status = 'mfs' → helper "Year parameter s1a.senior_base_other ($75,000)"] [f1040 line Filing Status = 'hoh' → helper "Year parameter s1a.senior_base_other ($75,000)"] [f1040 line Filing Status = 'qss' → helper "Year parameter s1a.senior_base_other ($75,000)"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"s1a.senior_base_other"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"s1a.senior_base_joint"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"s1a.senior_base_other"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"s1a.senior_base_other"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"s1a.senior_base_other"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 32 (2025; created 2025-11-04; sha256 64f97b38)

## 32 — `s1a.line32`

- **IRS:** Enter $75,000 ($150,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [helper "Part V applies: born before January 2, 1961, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part V applies: born before January 2, 1961, not married filing separately, a valid SSN" = true → helper "Figured: Enter $75,000 ($150,000 if married filing jointly)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part5",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part5",{"const":true}],"op":"test"},"then":"s1a.line32_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Fill out Schedule 1-A, Part V, only if"; Part V caution (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line33_calc`

- **Authored helper label:** Figured: Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
- **Encoded (Dollars):** Subtract line 32 from line 31.
- Expr: `{"from":"s1a.line31","op":"subtract","take":"s1a.line32"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 33 (2025; created 2025-11-04; sha256 64f97b38)

## 33 — `s1a.line33`

- **IRS:** Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35
- **Encoded (Dollars):** Choose — [helper "Part V applies: born before January 2, 1961, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part V applies: born before January 2, 1961, not married filing separately, a valid SSN" = true → helper "Figured: Subtract line 32 from line 31. If zero or less, enter $6,000 on line 35"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part5",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part5",{"const":true}],"op":"test"},"then":"s1a.line33_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Fill out Schedule 1-A, Part V, only if"; Part V caution (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line33_over`

- **Authored helper label:** Is the amount on line 31 more than the amount on line 32?
- **Encoded (Bool):** line 31 > line 32
- Expr: `{"gt":["s1a.line31","s1a.line32"],"op":"test"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 33, "If zero or less, enter $6,000 on line 35" (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line33_pos`

- **Authored helper label:** Line 33 if more than zero, otherwise zero
- **Encoded (NonNegDollars):** Subtract line 32 from line 31. If zero or less, enter -0-.
- Expr: `{"from":"s1a.line31","op":"subtract_floor0","take":"s1a.line32"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 33 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line34_calc`

- **Authored helper label:** Figured: Multiply line 33 by 6% (0.06)
- **Encoded (NonNegDollars):** Multiply helper "Line 33 if more than zero, otherwise zero" by 6% (0.06) (s1a.senior_rate).
- Expr: `{"amount":"s1a.line33_pos","op":"multiply_rate","rate":{"param":"s1a.senior_rate"}}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 34 (2025; created 2025-11-04; sha256 64f97b38)

## 34 — `s1a.line34`

- **IRS:** Multiply line 33 by 6% (0.06)
- **Encoded (NonNegDollars):** Choose — [helper "Part V applies: born before January 2, 1961, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part V applies: born before January 2, 1961, not married filing separately, a valid SSN" = true → helper "Figured: Multiply line 33 by 6% (0.06)"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part5",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part5",{"const":true}],"op":"test"},"then":"s1a.line34_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Fill out Schedule 1-A, Part V, only if"; Part V caution (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.senior_amount`

- **Authored helper label:** Year parameter s1a.senior_amount ($6,000)
- **Encoded (NonNegDollars):** Enter $6,000 (s1a.senior_amount).
- Expr: `{"op":"param","ref":"s1a.senior_amount"}`
- Cite: [f1040s1a] Schedule 1-A (2025), lines 33 and 35, $6,000 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line35_figured`

- **Authored helper label:** Subtract line 34 from $6,000. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Subtract line 34 from helper "Year parameter s1a.senior_amount ($6,000)". If zero or less, enter -0-.
- Expr: `{"from":"s1a.senior_amount","op":"subtract_floor0","take":"s1a.line34"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 35 (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line35_calc`

- **Authored helper label:** Figured: Subtract line 34 from $6,000. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Choose — [helper "Is the amount on line 31 more than the amount on line 32?" = false → helper "Year parameter s1a.senior_amount ($6,000)"] [helper "Is the amount on line 31 more than the amount on line 32?" = true → helper "Subtract line 34 from $6,000. If zero or less, enter -0-"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.line33_over",{"const":false}],"op":"test"},"then":"s1a.senior_amount"},{"guard":{"eq":["s1a.line33_over",{"const":true}],"op":"test"},"then":"s1a.line35_figured"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), lines 33 and 35 (2025; created 2025-11-04; sha256 64f97b38)

## 35 — `s1a.line35`

- **IRS:** Subtract line 34 from $6,000. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Choose — [helper "Part V applies: born before January 2, 1961, not married filing separately, a valid SSN" = false → helper "Year parameter sales.zero"] [helper "Part V applies: born before January 2, 1961, not married filing separately, a valid SSN" = true → helper "Figured: Subtract line 34 from $6,000. If zero or less, enter -0-"]
- Expr: `{"alternatives":[{"guard":{"eq":["s1a.part5",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["s1a.part5",{"const":true}],"op":"test"},"then":"s1a.line35_calc"}],"op":"choose"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Fill out Schedule 1-A, Part V, only if"; Part V caution (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.died_before_65`

- **Authored helper label:** Is this the final return of a person born between January 2, 1960, and January 1, 1961, who died in 2025 before reaching age 65?
- **Encoded (Bool):** Input — Is this the final return of a person born between January 2, 1960, and January 1, 1961, who died in 2025 before reaching age 65? (A person reaches age 65 on the day before the 65th birthday.)
- Expr: `{"op":"input","source":"Is this the final return of a person born between January 2, 1960, and January 1, 1961, who died in 2025 before reaching age 65? (A person reaches age 65 on the day before the 65th birthday.)"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Death of a taxpayer in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `s1a.senior_decedent`

- **Authored helper label:** A filer who died in 2025 before reaching age 65
- **Encoded (Bool):** helper "Is this the final return of a person born between January 2, 1960, and January 1, 1961, who died in 2025 before reaching age 65?" = true
- Expr: `{"eq":["s1a.died_before_65",{"const":true}],"op":"test"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Death of a taxpayer in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `s1a.line36a_senior`

- **Authored helper label:** Line 36a for a filer born before January 2, 1961
- **Encoded (NonNegDollars):** Choose — [household helper "Do you have an SSN valid for employment issued before the due date of your return?" = false → helper "Year parameter sales.zero"] [household helper "Do you have an SSN valid for employment issued before the due date of your return?" = true → line 35]
- **Refusal:** when s1a.senior_decedent is true, cannot complete Enhanced deduction for seniors on the final return of a person who died in 2025 before reaching age 65. A person born before January 2, 1961, who died in 2025 before reaching age 65 does not qualify; this case is outside this tool. Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Death of a taxpayer in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"alternatives":[{"guard":{"eq":["household.taxpayer_work_ssn",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["household.taxpayer_work_ssn",{"const":true}],"op":"test"},"then":"s1a.line35"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 36a (2025; created 2025-11-04; sha256 64f97b38)

## (helper) — `s1a.line36a_claim`

- **Authored helper label:** Line 36a for a filer born before January 2, 1961: zero for married filing separately
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → helper "Line 36a for a filer born before January 2, 1961"] [f1040 line Filing Status = 'mfj' → helper "Line 36a for a filer born before January 2, 1961"] [f1040 line Filing Status = 'mfs' → helper "Year parameter sales.zero"] [f1040 line Filing Status = 'hoh' → helper "Line 36a for a filer born before January 2, 1961"] [f1040 line Filing Status = 'qss' → helper "Line 36a for a filer born before January 2, 1961"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"s1a.line36a_senior"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"s1a.line36a_senior"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"s1a.line36a_senior"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"s1a.line36a_senior"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), Part V caution, "If married, you must file jointly to claim this deduction" (2025; created 2025-11-04; sha256 64f97b38)

## 36a — `s1a.line36a`

- **IRS:** If you have a valid social security number (see instructions) and were born before January 2, 1961, enter the amount from line 35
- **Encoded (NonNegDollars):** Choose — [sa helper "Were you born before January 2, 1961?" = false → helper "Year parameter sales.zero"] [sa helper "Were you born before January 2, 1961?" = true → helper "Line 36a for a filer born before January 2, 1961: zero for married filing separately"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.age65",{"const":false}],"op":"test"},"then":"s1a.zero"},{"guard":{"eq":["sa.age65",{"const":true}],"op":"test"},"then":"s1a.line36a_claim"}],"op":"choose"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 36a (2025; created 2025-11-04; sha256 64f97b38)

## 36b — `s1a.line36b`

- **IRS:** If you are married filing jointly, your spouse has a valid social security number (see instructions), and your spouse was born before January 2, 1961, enter the amount from line 35
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- **Refusal:** when sa.spouse_extra is true, cannot complete Schedule 1-A, line 36b (a spouse born before January 2, 1961, on a joint return). A spouse's age and blindness boxes, and the spouse's enhanced deduction for seniors, are outside this tool. Cite: [f1040s1a] Schedule 1-A (2025), line 36b (2025; created 2025-11-04; sha256 64f97b38)
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 36b (2025; created 2025-11-04; sha256 64f97b38)

## 37 — `s1a.line37`

- **IRS:** Enhanced deduction for seniors. Add lines 36a and 36b
- **Encoded (NonNegDollars):** Add line 36a and line 36b.
- Expr: `{"of":["s1a.line36a","s1a.line36b"],"op":"sum"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 37 (2025; created 2025-11-04; sha256 64f97b38)

## 38 — `s1a.line38`

- **IRS:** Add lines 13, 21, 30, and 37. Enter here and on Form 1040 or 1040-SR, line 13b, or on Form 1040-NR, line 13c
- **Encoded (NonNegDollars):** Add line 13, line 21, line 30, and line 37.
- Expr: `{"of":["s1a.line13","s1a.line21","s1a.line30","s1a.line37"],"op":"sum"}`
- Cite: [f1040s1a] Schedule 1-A (2025), line 38 (2025; created 2025-11-04; sha256 64f97b38)
