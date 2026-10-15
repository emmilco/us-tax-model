# Schedule A — supported itemized deductions and standard comparison

- Document: `sa` (form, tax year 2025)
- Note: Income and deduction eligibility are explicit supplied facts. Charity valuation, substantiation and income-limit screening are not computed; an affirmative limitation answer is refused. The SALT formula follows the printed 2025 worksheet, including its MFS halving step.

## (helper) — `sa.unsupported`

- **Authored helper label:** Any casualty/theft loss, other itemized deduction, foreign tax deduction, mortgage interest not on Form 1098 or subject to debt/use limits, or sales-tax election?
- **Encoded (Bool):** Input — Any casualty/theft loss, other itemized deduction, foreign tax deduction, mortgage interest not on Form 1098 or subject to debt/use limits, or sales-tax election?
- Expr: `{"op":"input","source":"Any casualty/theft loss, other itemized deduction, foreign tax deduction, mortgage interest not on Form 1098 or subject to debt/use limits, or sales-tax election?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.charity_limited`

- **Authored helper label:** Are any charitable deductions reduced by income limits, or carried over from a prior year? Determine under Publication 526 before answering.
- **Encoded (Bool):** Input — Are any charitable deductions reduced by income limits, or carried over from a prior year? Determine under Publication 526 before answering.
- Expr: `{"op":"input","source":"Are any charitable deductions reduced by income limits, or carried over from a prior year? Determine under Publication 526 before answering."}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.excluded_income`

- **Authored helper label:** Any excluded Puerto Rico income, Form 2555 or Form 4563 amounts?
- **Encoded (Bool):** Input — Any excluded Puerto Rico income, Form 2555 or Form 4563 amounts?
- Expr: `{"op":"input","source":"Any excluded Puerto Rico income, Form 2555 or Form 4563 amounts?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.dependent`

- **Authored helper label:** Can someone claim you or your spouse as a dependent, or are you a dual-status alien?
- **Encoded (Bool):** Input — Can someone claim you or your spouse as a dependent, or are you a dual-status alien?
- Expr: `{"op":"input","source":"Can someone claim you or your spouse as a dependent, or are you a dual-status alien?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.spouse_extra`

- **Authored helper label:** Claiming any age/blindness standard-deduction boxes for a spouse?
- **Encoded (Bool):** Input — Claiming any age/blindness standard-deduction boxes for a spouse?
- Expr: `{"op":"input","source":"Claiming any age/blindness standard-deduction boxes for a spouse?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.age65`

- **Authored helper label:** Were you born before January 2, 1961?
- **Encoded (Bool):** Input — Were you born before January 2, 1961?
- Expr: `{"op":"input","source":"Were you born before January 2, 1961?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.blind`

- **Authored helper label:** Are you blind under the standard-deduction instructions?
- **Encoded (Bool):** Input — Are you blind under the standard-deduction instructions?
- Expr: `{"op":"input","source":"Are you blind under the standard-deduction instructions?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.spouse_itemizes`

- **Authored helper label:** Married filing separately with a spouse who itemizes?
- **Encoded (Bool):** Input — Married filing separately with a spouse who itemizes?
- Expr: `{"op":"input","source":"Married filing separately with a spouse who itemizes?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.elect_itemize`

- **Authored helper label:** Elect to itemize even if the standard deduction is larger?
- **Encoded (Bool):** Input — Elect to itemize even if the standard deduction is larger?
- Expr: `{"op":"input","source":"Elect to itemize even if the standard deduction is larger?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.agi`

- **Authored helper label:** Form 1040 line 11b adjusted gross income (supplied subtotal until Stage 5)
- **Encoded (Dollars):** Input — Form 1040 line 11b adjusted gross income (supplied subtotal until Stage 5)
- Expr: `{"op":"input","source":"Form 1040 line 11b adjusted gross income (supplied subtotal until Stage 5)"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 1 — `sa.line1`

- **IRS:** Unreimbursed eligible medical and dental expenses
- **Encoded (NonNegDollars):** Input — Unreimbursed eligible medical and dental expenses
- Expr: `{"op":"input","source":"Unreimbursed eligible medical and dental expenses"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 5a — `sa.line5a`

- **IRS:** State/local income taxes paid, including withholding; no sales-tax election
- **Encoded (NonNegDollars):** Input — State/local income taxes paid, including withholding; no sales-tax election
- Expr: `{"op":"input","source":"State/local income taxes paid, including withholding; no sales-tax election"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 5b — `sa.line5b`

- **IRS:** Deductible state/local real estate taxes
- **Encoded (NonNegDollars):** Input — Deductible state/local real estate taxes
- Expr: `{"op":"input","source":"Deductible state/local real estate taxes"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 5c — `sa.line5c`

- **IRS:** Deductible state/local personal property taxes
- **Encoded (NonNegDollars):** Input — Deductible state/local personal property taxes
- Expr: `{"op":"input","source":"Deductible state/local personal property taxes"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 8a — `sa.line8a`

- **IRS:** Eligible home mortgage interest and points on Form 1098, after confirming the debt/use limits do not apply
- **Encoded (NonNegDollars):** Input — Eligible home mortgage interest and points on Form 1098, after confirming the debt/use limits do not apply
- Expr: `{"op":"input","source":"Eligible home mortgage interest and points on Form 1098, after confirming the debt/use limits do not apply"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 11 — `sa.line11`

- **IRS:** Deductible cash/check charitable gifts before income limits, after benefits received and required substantiation
- **Encoded (NonNegDollars):** Input — Deductible cash/check charitable gifts before income limits, after benefits received and required substantiation
- Expr: `{"op":"input","source":"Deductible cash/check charitable gifts before income limits, after benefits received and required substantiation"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 2 — `sa.line2`

- **IRS:** Amount from sa.agi
- **Encoded (Dollars):** Enter the amount from line (helper).
- Expr: `{"from":"sa.agi","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 3 — `sa.line3`

- **IRS:** Multiply sa.line2 by sa.medical_rate
- **Encoded (Dollars):** Multiply line 2 by 75/1000 (sa.medical_rate).
- Interpretation: amb.2025.multiplication_subcent
- Expr: `{"amount":"sa.line2","op":"multiply_rate","rate":{"param":"sa.medical_rate"}}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 4 — `sa.line4`

- **IRS:** Subtract sa.line3 from sa.line1; if zero or less, enter zero
- **Encoded (NonNegDollars):** Subtract line 3 from line 1. If zero or less, enter -0-.
- Expr: `{"from":"sa.line1","op":"subtract_floor0","take":"sa.line3"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 5d — `sa.line5d`

- **IRS:** Add sa.line5a, sa.line5b, sa.line5c
- **Encoded (NonNegDollars):** Add line 5a, line 5b, and line 5c.
- Expr: `{"of":["sa.line5a","sa.line5b","sa.line5c"],"op":"sum"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltbase`

- **Authored helper label:** Year parameter sa.salt_base
- **Encoded (NonNegDollars):** Enter $40,000 (sa.salt_base).
- Expr: `{"op":"param","ref":"sa.salt_base"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltfloor`

- **Authored helper label:** Year parameter sa.salt_floor
- **Encoded (NonNegDollars):** Enter $10,000 (sa.salt_floor).
- Expr: `{"op":"param","ref":"sa.salt_floor"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltthreshold`

- **Authored helper label:** Year parameter sa.salt_threshold
- **Encoded (NonNegDollars):** Enter single $500,000; mfj $500,000; mfs $250,000; hoh $500,000; qss $500,000 (sa.salt_threshold).
- Expr: `{"op":"param","ref":"sa.salt_threshold"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltexcess`

- **Authored helper label:** Subtract sa.saltthreshold from sa.agi; if zero or less, enter zero
- **Encoded (NonNegDollars):** Subtract line (helper) from line (helper). If zero or less, enter -0-.
- Expr: `{"from":"sa.agi","op":"subtract_floor0","take":"sa.saltthreshold"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltreduction`

- **Authored helper label:** Multiply sa.saltexcess by sa.salt_rate
- **Encoded (NonNegDollars):** Multiply line (helper) by 3/10 (sa.salt_rate).
- Interpretation: amb.2025.multiplication_subcent
- Expr: `{"amount":"sa.saltexcess","op":"multiply_rate","rate":{"param":"sa.salt_rate"}}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltremaining`

- **Authored helper label:** Subtract sa.saltreduction from sa.saltbase; if zero or less, enter zero
- **Encoded (NonNegDollars):** Subtract line (helper) from line (helper). If zero or less, enter -0-.
- Expr: `{"from":"sa.saltbase","op":"subtract_floor0","take":"sa.saltreduction"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltfloor_applied`

- **Authored helper label:** Larger of remaining ceiling and $10,000
- **Encoded (NonNegDollars):** Enter the larger of line (helper) or line (helper).
- Expr: `{"of":["sa.saltremaining","sa.saltfloor"],"op":"larger_of"}`
- Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.salthalf`

- **Authored helper label:** Multiply sa.saltfloor_applied by sa.half
- **Encoded (NonNegDollars):** Multiply line (helper) by 1/2 (sa.half).
- Interpretation: amb.2025.multiplication_subcent
- Expr: `{"amount":"sa.saltfloor_applied","op":"multiply_rate","rate":{"param":"sa.half"}}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.mfs`

- **Authored helper label:** Married filing separately
- **Encoded (Bool):** f1040 "Filing Status" = 'mfs'
- Expr: `{"eq":["f1040.status",{"const":"mfs"}],"op":"test"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltlimit`

- **Authored helper label:** Half the worksheet ceiling if married filing separately
- **Encoded (NonNegDollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.mfs",{"const":true}],"op":"test"},"then":"sa.salthalf"},{"guard":{"eq":["sa.mfs",{"const":false}],"op":"test"},"then":"sa.saltfloor_applied"}],"op":"choose"}`
- Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)

## 5e — `sa.line5e`

- **IRS:** Smaller of sa.line5d, sa.saltlimit
- **Encoded (NonNegDollars):** Enter the smaller of line 5d or line (helper).
- Expr: `{"of":["sa.line5d","sa.saltlimit"],"op":"smaller_of"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 6 — `sa.line6`

- **IRS:** Amount from sa.zero
- **Encoded (NonNegDollars):** Enter the amount from line (helper).
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item / Form 4684. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.charity_limited is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"from":"sa.zero","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 8b — `sa.line8b`

- **IRS:** Amount from sa.zero
- **Encoded (NonNegDollars):** Enter the amount from line (helper).
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item / Form 4684. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.charity_limited is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"from":"sa.zero","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 8c — `sa.line8c`

- **IRS:** Amount from sa.zero
- **Encoded (NonNegDollars):** Enter the amount from line (helper).
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item / Form 4684. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.charity_limited is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"from":"sa.zero","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 13 — `sa.line13`

- **IRS:** Amount from sa.zero
- **Encoded (NonNegDollars):** Enter the amount from line (helper).
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item / Form 4684. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.charity_limited is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"from":"sa.zero","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 15 — `sa.line15`

- **IRS:** Amount from sa.zero
- **Encoded (NonNegDollars):** Enter the amount from line (helper).
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item / Form 4684. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.charity_limited is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"from":"sa.zero","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 16 — `sa.line16`

- **IRS:** Amount from sa.zero
- **Encoded (NonNegDollars):** Enter the amount from line (helper).
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item / Form 4684. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.charity_limited is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"from":"sa.zero","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 7 — `sa.line7`

- **IRS:** Add sa.line5e, sa.line6
- **Encoded (NonNegDollars):** Add line 5e and line 6.
- Expr: `{"of":["sa.line5e","sa.line6"],"op":"sum"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 8e — `sa.line8e`

- **IRS:** Add sa.line8a, sa.line8b, sa.line8c
- **Encoded (NonNegDollars):** Add line 8a, line 8b, and line 8c.
- Expr: `{"of":["sa.line8a","sa.line8b","sa.line8c"],"op":"sum"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 9 — `sa.line9`

- **IRS:** Amount from f4952.line8
- **Encoded (NonNegDollars):** Enter the amount from f4952 line 8.
- Expr: `{"from":"f4952.line8","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 10 — `sa.line10`

- **IRS:** Add sa.line8e, sa.line9
- **Encoded (NonNegDollars):** Add line 8e and line 9.
- Expr: `{"of":["sa.line8e","sa.line9"],"op":"sum"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 12 — `sa.line12`

- **IRS:** Total supported noncash donations before income limits
- **Encoded (NonNegDollars):** Add gift.allowed over every confirmed gift entry, within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item / Form 4684. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.charity_limited is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"collection":"gift","field":"gift.allowed","op":"sum_over"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.form8283`

- **Authored helper label:** Noncash total exceeds $500; Form 8283 attachment required
- **Encoded (Bool):** line 12 > $500
- Expr: `{"gt":["sa.line12",{"const":50000}],"op":"test"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 14 — `sa.line14`

- **IRS:** Add sa.line11, sa.line12, sa.line13
- **Encoded (NonNegDollars):** Add line 11, line 12, and line 13.
- Expr: `{"of":["sa.line11","sa.line12","sa.line13"],"op":"sum"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 17 — `sa.line17`

- **IRS:** Add sa.line4, sa.line7, sa.line10, sa.line14, sa.line15, sa.line16
- **Encoded (NonNegDollars):** Add line 4, line 7, line 10, line 14, line 15, and line 16.
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item / Form 4684. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.charity_limited is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"of":["sa.line4","sa.line7","sa.line10","sa.line14","sa.line15","sa.line16"],"op":"sum"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.standardbase`

- **Authored helper label:** Year parameter sa.standard_base
- **Encoded (NonNegDollars):** Enter single $15,750; mfj $31,500; mfs $15,750; hoh $23,625; qss $31,500 (sa.standard_base).
- Expr: `{"op":"param","ref":"sa.standard_base"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.extra`

- **Authored helper label:** Year parameter sa.standard_extra
- **Encoded (NonNegDollars):** Enter single $2,000; mfj $1,600; mfs $1,600; hoh $2,000; qss $1,600 (sa.standard_extra).
- Expr: `{"op":"param","ref":"sa.standard_extra"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.extra_age65`

- **Authored helper label:** Additional standard deduction for age65
- **Encoded (NonNegDollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.age65",{"const":true}],"op":"test"},"then":"sa.extra"},{"guard":{"eq":["sa.age65",{"const":false}],"op":"test"},"then":"sa.zero"}],"op":"choose"}`
- Cite: [i1040gi] pp. 34–35, line 12e and Standard Deduction Chart (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.extra_blind`

- **Authored helper label:** Additional standard deduction for blind
- **Encoded (NonNegDollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.blind",{"const":true}],"op":"test"},"then":"sa.extra"},{"guard":{"eq":["sa.blind",{"const":false}],"op":"test"},"then":"sa.zero"}],"op":"choose"}`
- Cite: [i1040gi] pp. 34–35, line 12e and Standard Deduction Chart (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.standardraw`

- **Authored helper label:** Add sa.standardbase, sa.extra_age65, sa.extra_blind
- **Encoded (NonNegDollars):** Add line (helper), line (helper), and line (helper).
- Expr: `{"of":["sa.standardbase","sa.extra_age65","sa.extra_blind"],"op":"sum"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.standard`

- **Authored helper label:** Standard deduction, zero when MFS spouse itemizes
- **Encoded (NonNegDollars):** Choose — [line (helper) = true → line (helper)] [line (helper) = false → line (helper)]
- **Refusal:** when sa.dependent is true, cannot complete Standard Deduction Worksheet for Dependents / dual-status rules. Dependent and dual-status standard deductions are outside this resident nondependent slice. Cite: [i1040gi] pp. 34–35, line 12e and Standard Deduction Chart (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when sa.spouse_extra is true, cannot complete Standard Deduction Chart spouse boxes. Spouse age/blindness claims require the unsupported per-spouse interview. Cite: [i1040gi] pp. 34–35, line 12e and Standard Deduction Chart (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"alternatives":[{"guard":{"eq":["sa.mfs_spouse_itemizes",{"const":true}],"op":"test"},"then":"sa.zero"},{"guard":{"eq":["sa.mfs_spouse_itemizes",{"const":false}],"op":"test"},"then":"sa.standardraw"}],"op":"choose"}`
- Cite: [i1040gi] pp. 34–35, line 12e and Standard Deduction Chart (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.itemizes`

- **Authored helper label:** Itemize if elected, required, or itemized total exceeds standard
- **Encoded (Bool):** (line (helper) = true or line (helper) = true or line 17 > line (helper))
- Expr: `{"any":[{"eq":["sa.elect_itemize",{"const":true}],"op":"test"},{"eq":["sa.mfs_spouse_itemizes",{"const":true}],"op":"test"},{"gt":["sa.line17","sa.standard"],"op":"test"}],"op":"test"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.deduction`

- **Authored helper label:** Deduction selected for Form 1040 line 12e
- **Encoded (NonNegDollars):** Choose — [line (helper) = true → line 17] [line (helper) = false → line (helper)]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.itemizes",{"const":true}],"op":"test"},"then":"sa.line17"},{"guard":{"eq":["sa.itemizes",{"const":false}],"op":"test"},"then":"sa.standard"}],"op":"choose"}`
- Cite: [i1040gi] pp. 34–35, line 12e and Standard Deduction Chart (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.mfs_spouse_itemizes`

- **Authored helper label:** MFS with spouse itemizing
- **Encoded (Bool):** line (helper) = true and line (helper) = true
- Expr: `{"all":[{"eq":["sa.mfs",{"const":true}],"op":"test"},{"eq":["sa.spouse_itemizes",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 34, line 12e exception 2 (2025; printed date 2026-02-25; sha256 482e9c48)
