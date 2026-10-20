# Student Loan Interest Deduction Worksheet—Schedule 1, Line 21

- Document: `sli` (form, tax year 2025)
- Note: The worksheet in the Form 1040 instructions; Pub. 970 cases (Form 2555, Form 4563, excluded Puerto Rico income) are refused.

## (helper) — `sli.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 99, Student Loan Interest Deduction Worksheet—Schedule 1, Line 21 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sli.interest`

- **Authored helper label:** Total interest you paid in 2025 on qualified student loans
- **Encoded (NonNegDollars):** Input — Total interest you paid in 2025 on qualified student loans (generally Form 1098-E box 1), not counting any amount paid from tax-free qualified tuition program earnings; zero if none
- Expr: `{"op":"input","source":"Total interest you paid in 2025 on qualified student loans (generally Form 1098-E box 1), not counting any amount paid from tax-free qualified tuition program earnings; zero if none"}`
- Cite: [i1040gi] p. 98, Schedule 1, line 21, 'You paid interest in 2025 on a qualified student loan' and 'Don't include any amount paid from a distribution of earnings made from a qualified tuition program (QTP)' (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sli.has`

- **Authored helper label:** Any student loan interest
- **Encoded (Bool):** helper "Total interest you paid in 2025 on qualified student loans" > $0 (sales.zero)
- Expr: `{"gt":["sli.interest",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 98, Schedule 1, line 21 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sli.claimed`

- **Authored helper label:** Are you claimed as a dependent on someone else's (such as your parent's) 2025 tax return?
- **Encoded (Bool):** Input — Are you claimed as a dependent on someone else's (such as your parent's) 2025 tax return?
- Expr: `{"op":"input","source":"Are you claimed as a dependent on someone else's (such as your parent's) 2025 tax return?"}`
- Cite: [i1040gi] p. 98, Schedule 1, line 21, 'You, or your spouse if filing jointly, aren't claimed as a dependent on someone else's (such as your parent's) 2025 tax return' (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sli.max`

- **Authored helper label:** Year parameter sli.max ($2,500)
- **Encoded (NonNegDollars):** Enter $2,500 (sli.max).
- Expr: `{"op":"param","ref":"sli.max"}`
- Cite: [i1040gi] p. 99, Student Loan Interest Deduction Worksheet—Schedule 1, Line 21, line 1, $2,500 (2025; printed date 2026-02-25; sha256 482e9c48)

## 1 — `sli.line1`

- **IRS:** Enter the total interest you paid in 2025 on qualified student loans (see the instructions for line 21). Don't enter more than $2,500
- **Encoded (NonNegDollars):** Enter the smaller of helper "Total interest you paid in 2025 on qualified student loans" or helper "Year parameter sli.max ($2,500)".
- **Refusal:** when sa.excluded_income is true, cannot complete Pub. 970 (student loan interest with Form 2555 or 4563, or excluded Puerto Rico income). Use Pub. 970 instead of the worksheet; it is outside this tool. Cite: [i1040gi] p. 98, Schedule 1, line 21, Exception (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"of":["sli.interest","sli.max"],"op":"smaller_of"}`
- Cite: [i1040gi] p. 99, Student Loan Interest Deduction Worksheet—Schedule 1, Line 21, line 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## 2 — `sli.line2`

- **IRS:** Enter the amount from Form 1040 or 1040-SR, line 9
- **Encoded (Dollars):** Enter the amount from f1040 line 9.
- Expr: `{"from":"f1040.line9","op":"copy"}`
- Cite: [i1040gi] p. 99, Student Loan Interest Deduction Worksheet—Schedule 1, Line 21, line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## 3 — `sli.line3`

- **IRS:** Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25
- **Encoded (NonNegDollars):** Add s1 line 11, s1 line 13, s1 line 15, s1 line 16, and s1 line 17.
- Expr: `{"of":["s1.line11","s1.line13","s1.line15","s1.line16","s1.line17"],"op":"sum"}`
- Cite: [i1040gi] p. 99, Student Loan Interest Deduction Worksheet—Schedule 1, Line 21, line 3 (lines 12, 14 and 18 to 20, 23 and 25 are outside this tool and refused through line 2, Form 1040 line 9, by scope.schedule1) (2025; printed date 2026-02-25; sha256 482e9c48)

## 4 — `sli.line4`

- **IRS:** Subtract line 3 from line 2
- **Encoded (Dollars):** Subtract line 3 from line 2.
- Expr: `{"from":"sli.line2","op":"subtract","take":"sli.line3"}`
- Cite: [i1040gi] p. 99, Student Loan Interest Deduction Worksheet—Schedule 1, Line 21, line 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sli.base_other`

- **Authored helper label:** Year parameter sli.base_other ($85,000)
- **Encoded (NonNegDollars):** Enter $85,000 (sli.base_other).
- Expr: `{"op":"param","ref":"sli.base_other"}`
- Cite: [i1040gi] p. 99, Student Loan Interest Deduction Worksheet—Schedule 1, Line 21, line 5, $85,000 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sli.base_joint`

- **Authored helper label:** Year parameter sli.base_joint ($170,000)
- **Encoded (NonNegDollars):** Enter $170,000 (sli.base_joint).
- Expr: `{"op":"param","ref":"sli.base_joint"}`
- Cite: [i1040gi] p. 99, Student Loan Interest Deduction Worksheet—Schedule 1, Line 21, line 5, $170,000 (2025; printed date 2026-02-25; sha256 482e9c48)

## 5 — `sli.line5`

- **IRS:** Enter the amount shown below for your filing status. Single, head of household, or qualifying surviving spouse—$85,000. Married filing jointly—$170,000
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → helper "Year parameter sli.base_other ($85,000)"] [f1040 line Filing Status = 'mfj' → helper "Year parameter sli.base_joint ($170,000)"] [f1040 line Filing Status = 'mfs' → helper "Year parameter sales.zero"] [f1040 line Filing Status = 'hoh' → helper "Year parameter sli.base_other ($85,000)"] [f1040 line Filing Status = 'qss' → helper "Year parameter sli.base_other ($85,000)"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"sli.base_other"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"sli.base_joint"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"sli.zero"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"sli.base_other"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"sli.base_other"}],"op":"choose"}`
- Cite: [i1040gi] p. 99, Student Loan Interest Deduction Worksheet—Schedule 1, Line 21, line 5 (no amount for married filing separately, which cannot take the deduction) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sli.over`

- **Authored helper label:** Is the amount on line 4 more than the amount on line 5?
- **Encoded (Bool):** line 4 > line 5
- Expr: `{"gt":["sli.line4","sli.line5"],"op":"test"}`
- Cite: [i1040gi] p. 99, Student Loan Interest Deduction Worksheet—Schedule 1, Line 21, line 6 (2025; printed date 2026-02-25; sha256 482e9c48)

## 6 — `sli.line6`

- **IRS:** Subtract line 5 from line 4
- **Encoded (Dollars):** Subtract line 5 from line 4.
- Expr: `{"from":"sli.line4","op":"subtract","take":"sli.line5"}`
- Cite: [i1040gi] p. 99, Student Loan Interest Deduction Worksheet—Schedule 1, Line 21, line 6 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sli.divisor_other`

- **Authored helper label:** Year parameter sli.divisor_other ($15,000)
- **Encoded (NonNegDollars):** Enter $15,000 (sli.divisor_other).
- Expr: `{"op":"param","ref":"sli.divisor_other"}`
- Cite: [i1040gi] p. 99, Student Loan Interest Deduction Worksheet—Schedule 1, Line 21, line 7, $15,000 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sli.divisor_joint`

- **Authored helper label:** Year parameter sli.divisor_joint ($30,000)
- **Encoded (NonNegDollars):** Enter $30,000 (sli.divisor_joint).
- Expr: `{"op":"param","ref":"sli.divisor_joint"}`
- Cite: [i1040gi] p. 99, Student Loan Interest Deduction Worksheet—Schedule 1, Line 21, line 7, $30,000 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sli.divisor`

- **Authored helper label:** $15,000 ($30,000 if married filing jointly)
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → helper "Year parameter sli.divisor_other ($15,000)"] [f1040 line Filing Status = 'mfj' → helper "Year parameter sli.divisor_joint ($30,000)"] [f1040 line Filing Status = 'mfs' → helper "Year parameter sli.divisor_other ($15,000)"] [f1040 line Filing Status = 'hoh' → helper "Year parameter sli.divisor_other ($15,000)"] [f1040 line Filing Status = 'qss' → helper "Year parameter sli.divisor_other ($15,000)"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"sli.divisor_other"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"sli.divisor_joint"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"sli.divisor_other"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"sli.divisor_other"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"sli.divisor_other"}],"op":"choose"}`
- Cite: [i1040gi] p. 99, Student Loan Interest Deduction Worksheet—Schedule 1, Line 21, line 7 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sli.line8_figured`

- **Authored helper label:** Divide line 6 by $15,000 ($30,000 if married filing jointly), rounded to three places, not more than 1.000; multiply line 1 by the result
- **Encoded (NonNegDollars):** Divide line 6 by helper "$15,000 ($30,000 if married filing jointly)", rounded to 3 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply line 1 by the result.
- Interpretation: amb.2025.sli_ratio_places
- Expr: `{"amount":"sli.line1","op":"prorate","part":"sli.line6","places":3,"whole":"sli.divisor"}`
- Cite: [i1040gi] p. 99, Student Loan Interest Deduction Worksheet—Schedule 1, Line 21, lines 7 and 8 ('Enter the result as a decimal (rounded to at least three places). If the result is 1.000 or more, enter 1.000' and 'Multiply line 1 by line 7'; three places, amb.2025.sli_ratio_places) (2025; printed date 2026-02-25; sha256 482e9c48)

## 8 — `sli.line8`

- **IRS:** Multiply line 1 by line 7
- **Encoded (NonNegDollars):** Choose — [helper "Is the amount on line 4 more than the amount on line 5?" = true → helper "Divide line 6 by $15,000 ($30,000 if married filing jointly), rounded to three places, not more than 1.000; multiply line 1 by the result"] [helper "Is the amount on line 4 more than the amount on line 5?" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["sli.over",{"const":true}],"op":"test"},"then":"sli.line8_figured"},{"guard":{"eq":["sli.over",{"const":false}],"op":"test"},"then":"sli.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 99, Student Loan Interest Deduction Worksheet—Schedule 1, Line 21, line 6, 'No. Skip lines 6 and 7, enter -0- on line 8, and go to line 9'; line 8 (2025; printed date 2026-02-25; sha256 482e9c48)

## 9 — `sli.line9`

- **IRS:** Student loan interest deduction. Subtract line 8 from line 1. Enter the result here and on Schedule 1, line 21
- **Encoded (NonNegDollars):** Subtract line 8 from line 1. If zero or less, enter -0-.
- Expr: `{"from":"sli.line1","op":"subtract_floor0","take":"sli.line8"}`
- Cite: [i1040gi] p. 99, Student Loan Interest Deduction Worksheet—Schedule 1, Line 21, line 9 (line 8 never exceeds line 1, since the ratio is at most 1.000) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sli.eligible`

- **Authored helper label:** You can take the deduction: a filing status other than married filing separately, and not claimed as a dependent
- **Encoded (Bool):** f1040 line Filing Status ≠ 'mfs' and helper "Are you claimed as a dependent on someone else's (such as your parent's) 2025 tax return?" = false
- Expr: `{"all":[{"ne":["f1040.status",{"const":"mfs"}],"op":"test"},{"eq":["sli.claimed",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 98, Schedule 1, line 21, 'You can take this deduction only if all of the following apply' (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sli.allowed`

- **Authored helper label:** Student loan interest deduction for an eligible filer
- **Encoded (NonNegDollars):** Choose — [helper "You can take the deduction: a filing status other than married filing separately, and not claimed as a dependent" = true → line 9] [helper "You can take the deduction: a filing status other than married filing separately, and not claimed as a dependent" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["sli.eligible",{"const":true}],"op":"test"},"then":"sli.line9"},{"guard":{"eq":["sli.eligible",{"const":false}],"op":"test"},"then":"sli.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 98, Schedule 1, line 21 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sli.deduction`

- **Authored helper label:** Student loan interest deduction (Schedule 1, line 21)
- **Encoded (NonNegDollars):** Choose — [helper "Any student loan interest" = true → helper "Student loan interest deduction for an eligible filer"] [helper "Any student loan interest" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["sli.has",{"const":true}],"op":"test"},"then":"sli.allowed"},{"guard":{"eq":["sli.has",{"const":false}],"op":"test"},"then":"sli.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 98, Schedule 1, line 21 (2025; printed date 2026-02-25; sha256 482e9c48)
