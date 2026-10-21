# Schedule A — supported itemized deductions and standard comparison

- Document: `sa` (form, tax year 2025)
- Note: Income and deduction eligibility are explicit supplied facts. Charity valuation, substantiation and income-limit screening are not computed; an affirmative limitation answer is refused. The SALT formula follows the printed 2025 worksheet, including its MFS halving step.

## (helper) — `sa.unsupported`

- **Authored helper label:** Any casualty or theft loss (including a disaster loss added to the standard deduction); a deduction from the Schedule A line 16 list; a foreign tax or generation-skipping tax deduction; mortgage interest or points not on Form 1098 or subject to the debt or use limits (loan proceeds not all used to buy, build or improve the home, or debt over the limit); or the sales-tax election?
- **Encoded (Bool):** Input — Any casualty or theft loss (including a disaster loss added to the standard deduction); a deduction from the Schedule A line 16 list; a foreign tax or generation-skipping tax deduction; mortgage interest or points not on Form 1098 or subject to the debt or use limits (loan proceeds not all used to buy, build or improve the home, or debt over the limit); or the sales-tax election?
- Expr: `{"op":"input","source":"Any casualty or theft loss (including a disaster loss added to the standard deduction); a deduction from the Schedule A line 16 list; a foreign tax or generation-skipping tax deduction; mortgage interest or points not on Form 1098 or subject to the debt or use limits (loan proceeds not all used to buy, build or improve the home, or debt over the limit); or the sales-tax election?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.charity_limited`

- **Authored helper label:** Are any charitable deductions reduced by income limits, or carried over from a prior year? Determine under Publication 526 before answering.
- **Encoded (Bool):** Input — Are any charitable deductions reduced by income limits, or carried over from a prior year? Determine under Publication 526 before answering.
- Expr: `{"op":"input","source":"Are any charitable deductions reduced by income limits, or carried over from a prior year? Determine under Publication 526 before answering."}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.excluded_income`

- **Authored helper label:** Are you filing Form 2555 or Form 4563, or do you have income excluded as a bona fide resident of Puerto Rico?
- **Encoded (Bool):** Input — Are you filing Form 2555 or Form 4563, or do you have income excluded as a bona fide resident of Puerto Rico?
- Expr: `{"op":"input","source":"Are you filing Form 2555 or Form 4563, or do you have income excluded as a bona fide resident of Puerto Rico?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.dependent`

- **Authored helper label:** Can someone claim you or your spouse as a dependent for 2025, or are you a dual-status alien? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)
- **Encoded (Bool):** Input — Can someone claim you or your spouse as a dependent for 2025, or are you a dual-status alien? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)
- Expr: `{"op":"input","source":"Can someone claim you or your spouse as a dependent for 2025, or are you a dual-status alien? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.spouse_extra`

- **Authored helper label:** Married filing separately and claiming age or blindness boxes for your spouse (who had no income, isn't filing a return and can't be claimed as a dependent)?
- **Encoded (Bool):** Input — Married filing separately and claiming age or blindness boxes for your spouse (who had no income, isn't filing a return and can't be claimed as a dependent)?
- Expr: `{"op":"input","source":"Married filing separately and claiming age or blindness boxes for your spouse (who had no income, isn't filing a return and can't be claimed as a dependent)?"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (gate) — `sa.mfs_spouse_extra`

- **Authored helper label:** Married filing separately and claiming age or blindness boxes for your spouse
- **Encoded (Bool):** f1040 line Filing Status = 'mfs' and helper "Married filing separately and claiming age or blindness boxes for your spouse (who had no income, isn't filing a return and can't be claimed as a dependent)?" = true
- Expr: `{"all":[{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},{"eq":["sa.spouse_extra",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 33, Line 12d, "If your filing status is married filing separately and your spouse was born before January 2, 1961, or was blind at the end of 2025, you can check the appropriate box(es) on line 12d if your spouse had no income, isn't filing a return, and can't be claimed as a dependent on another person's return" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.age65_count`

- **Authored helper label:** Your entry, if the answer is yes
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'taxpayer' and helper "Were you born before January 2, 1961?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"all":[{"eq":["person.role",{"const":"taxpayer"}],"op":"test"},{"eq":["person.age65",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.age65`

- **Authored helper label:** Were you born before January 2, 1961?
- **Encoded (Bool):** helper "Your entry, if the answer is yes" > 0 (a count)
- Expr: `{"gt":["sa.age65_count",{"const":0,"type":"Count"}],"op":"test"}`
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

- **Authored helper label:** Form 1040 line 11b adjusted gross income
- **Encoded (Dollars):** Enter the amount from f1040 line 11b.
- Expr: `{"from":"f1040.line11b","op":"copy"}`
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
- **Encoded (Dollars):** Enter the amount from helper "Form 1040 line 11b adjusted gross income".
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
- **Encoded (NonNegDollars):** Subtract helper "Year parameter sa.salt_threshold" from helper "Form 1040 line 11b adjusted gross income". If zero or less, enter -0-.
- Expr: `{"from":"sa.agi","op":"subtract_floor0","take":"sa.saltthreshold"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltreduction`

- **Authored helper label:** Multiply sa.saltexcess by sa.salt_rate
- **Encoded (NonNegDollars):** Multiply helper "Subtract sa.saltthreshold from sa.agi; if zero or less, enter zero" by 3/10 (sa.salt_rate).
- Interpretation: amb.2025.multiplication_subcent
- Expr: `{"amount":"sa.saltexcess","op":"multiply_rate","rate":{"param":"sa.salt_rate"}}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltremaining`

- **Authored helper label:** Subtract sa.saltreduction from sa.saltbase; if zero or less, enter zero
- **Encoded (NonNegDollars):** Subtract helper "Multiply sa.saltexcess by sa.salt_rate" from helper "Year parameter sa.salt_base". If zero or less, enter -0-.
- Expr: `{"from":"sa.saltbase","op":"subtract_floor0","take":"sa.saltreduction"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltfloor_applied`

- **Authored helper label:** Larger of remaining ceiling and $10,000
- **Encoded (NonNegDollars):** Enter the larger of helper "Subtract sa.saltreduction from sa.saltbase; if zero or less, enter zero" or helper "Year parameter sa.salt_floor".
- Expr: `{"of":["sa.saltremaining","sa.saltfloor"],"op":"larger_of"}`
- Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)

## (helper) — `sa.salthalf`

- **Authored helper label:** Multiply sa.saltfloor_applied by sa.half
- **Encoded (NonNegDollars):** Multiply helper "Larger of remaining ceiling and $10,000" by 1/2 (sa.half).
- Interpretation: amb.2025.multiplication_subcent
- Expr: `{"amount":"sa.saltfloor_applied","op":"multiply_rate","rate":{"param":"sa.half"}}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.mfs`

- **Authored helper label:** Married filing separately
- **Encoded (Bool):** f1040 line Filing Status = 'mfs'
- Expr: `{"eq":["f1040.status",{"const":"mfs"}],"op":"test"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.saltlimit`

- **Authored helper label:** Half the worksheet ceiling if married filing separately
- **Encoded (NonNegDollars):** Choose — [helper "Married filing separately" = true → helper "Multiply sa.saltfloor_applied by sa.half"] [helper "Married filing separately" = false → helper "Larger of remaining ceiling and $10,000"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.mfs",{"const":true}],"op":"test"},"then":"sa.salthalf"},{"guard":{"eq":["sa.mfs",{"const":false}],"op":"test"},"then":"sa.saltfloor_applied"}],"op":"choose"}`
- Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)

## 5e — `sa.line5e`

- **IRS:** Smaller of sa.line5d, sa.saltlimit
- **Encoded (NonNegDollars):** Enter the smaller of line 5d or helper "Half the worksheet ceiling if married filing separately".
- Expr: `{"of":["sa.line5d","sa.saltlimit"],"op":"smaller_of"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 6 — `sa.line6`

- **IRS:** Amount from sa.zero
- **Encoded (NonNegDollars):** Enter the amount from helper "Year parameter sales.zero".
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item / Form 4684. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.charity_limited is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"from":"sa.zero","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 8b — `sa.line8b`

- **IRS:** Amount from sa.zero
- **Encoded (NonNegDollars):** Enter the amount from helper "Year parameter sales.zero".
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item / Form 4684. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.charity_limited is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"from":"sa.zero","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 8c — `sa.line8c`

- **IRS:** Amount from sa.zero
- **Encoded (NonNegDollars):** Enter the amount from helper "Year parameter sales.zero".
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item / Form 4684. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.charity_limited is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"from":"sa.zero","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 13 — `sa.line13`

- **IRS:** Amount from sa.zero
- **Encoded (NonNegDollars):** Enter the amount from helper "Year parameter sales.zero".
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item / Form 4684. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.charity_limited is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"from":"sa.zero","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 15 — `sa.line15`

- **IRS:** Amount from sa.zero
- **Encoded (NonNegDollars):** Enter the amount from helper "Year parameter sales.zero".
- **Refusal:** when sa.unsupported is true, cannot complete Schedule A unsupported item / Form 4684. Prepare the applicable deduction or limitation; only the listed Schedule A items are supported. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.charity_limited is true, cannot complete Schedule A charitable limitation / carryover. Income-limited and carried-over charitable deductions are outside scope. Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)
- **Refusal:** when sa.excluded_income is true, cannot complete Schedule A SALT Worksheet / Forms 2555 and 4563. Excluded-income addbacks are outside scope. Cite: [i1040sca] p. 7, State and Local Tax Deduction Worksheet (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"from":"sa.zero","op":"copy"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## 16 — `sa.line16`

- **IRS:** Amount from sa.zero
- **Encoded (NonNegDollars):** Enter the amount from helper "Year parameter sales.zero".
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

## (helper) — `sa.boxes_age65`

- **Authored helper label:** Number of boxes checked for born before January 2, 1961 (you, and your spouse if filing jointly)
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Were you born before January 2, 1961?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"eq":["person.age65",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)"; pp. 34–35, Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.extra_age65`

- **Authored helper label:** Additional standard deduction for each box checked for age
- **Encoded (NonNegDollars):** Multiply helper "Year parameter sa.standard_extra" by the number on helper "Number of boxes checked for born before January 2, 1961 (you, and your spouse if filing jointly)".
- Expr: `{"amount":"sa.extra","count":"sa.boxes_age65","op":"multiply_count"}`
- Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)"; pp. 34–35, Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.boxes_blind`

- **Authored helper label:** Number of boxes checked for blindness (you, and your spouse if filing jointly)
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Are you blind under the standard-deduction instructions?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"eq":["person.blind",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)"; pp. 34–35, Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.extra_blind`

- **Authored helper label:** Additional standard deduction for each box checked for blindness
- **Encoded (NonNegDollars):** Multiply helper "Year parameter sa.standard_extra" by the number on helper "Number of boxes checked for blindness (you, and your spouse if filing jointly)".
- Expr: `{"amount":"sa.extra","count":"sa.boxes_blind","op":"multiply_count"}`
- Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)"; pp. 34–35, Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.standardraw`

- **Authored helper label:** Add sa.standardbase, sa.extra_age65, sa.extra_blind
- **Encoded (NonNegDollars):** Add helper "Year parameter sa.standard_base", helper "Additional standard deduction for each box checked for age", and helper "Additional standard deduction for each box checked for blindness".
- Expr: `{"of":["sa.standardbase","sa.extra_age65","sa.extra_blind"],"op":"sum"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.standard`

- **Authored helper label:** Standard deduction, zero when MFS spouse itemizes
- **Encoded (NonNegDollars):** Choose — [helper "MFS with spouse itemizing" = true → helper "Year parameter sales.zero"] [helper "MFS with spouse itemizing" = false → helper "Add sa.standardbase, sa.extra_age65, sa.extra_blind"]
- **Refusal:** when sa.dependent is true, cannot complete Standard Deduction Worksheet for Dependents / dual-status rules. Dependent and dual-status standard deductions are outside this resident nondependent slice. Cite: [i1040gi] pp. 34–35, line 12e and Standard Deduction Chart (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when sa.mfs_spouse_extra is true, cannot complete Standard Deduction Chart spouse boxes on a separate return. Checking age or blindness boxes for your spouse on a married filing separately return is outside this tool. Cite: [i1040gi] pp. 34–35, line 12e and Standard Deduction Chart (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"alternatives":[{"guard":{"eq":["sa.mfs_spouse_itemizes",{"const":true}],"op":"test"},"then":"sa.zero"},{"guard":{"eq":["sa.mfs_spouse_itemizes",{"const":false}],"op":"test"},"then":"sa.standardraw"}],"op":"choose"}`
- Cite: [i1040gi] pp. 34–35, line 12e and Standard Deduction Chart (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.itemizes`

- **Authored helper label:** Itemize if elected, required, or itemized total exceeds standard
- **Encoded (Bool):** (helper "Elect to itemize even if the standard deduction is larger?" = true or helper "MFS with spouse itemizing" = true or line 17 > helper "Standard deduction, zero when MFS spouse itemizes")
- Expr: `{"any":[{"eq":["sa.elect_itemize",{"const":true}],"op":"test"},{"eq":["sa.mfs_spouse_itemizes",{"const":true}],"op":"test"},{"gt":["sa.line17","sa.standard"],"op":"test"}],"op":"test"}`
- Cite: [f1040sa] Schedule A (2025), lines 1–18 (2025; created 2025-11-20; sha256 c14acf34)

## (helper) — `sa.deduction`

- **Authored helper label:** Deduction selected for Form 1040 line 12e
- **Encoded (NonNegDollars):** Choose — [helper "Itemize if elected, required, or itemized total exceeds standard" = true → line 17] [helper "Itemize if elected, required, or itemized total exceeds standard" = false → helper "Standard deduction, zero when MFS spouse itemizes"]
- Expr: `{"alternatives":[{"guard":{"eq":["sa.itemizes",{"const":true}],"op":"test"},"then":"sa.line17"},{"guard":{"eq":["sa.itemizes",{"const":false}],"op":"test"},"then":"sa.standard"}],"op":"choose"}`
- Cite: [i1040gi] pp. 34–35, line 12e and Standard Deduction Chart (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `sa.mfs_spouse_itemizes`

- **Authored helper label:** MFS with spouse itemizing
- **Encoded (Bool):** helper "Married filing separately" = true and helper "Married filing separately with a spouse who itemizes?" = true
- Expr: `{"all":[{"eq":["sa.mfs",{"const":true}],"op":"test"},{"eq":["sa.spouse_itemizes",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 34, Line 12e, Exception 2 (2025; printed date 2026-02-25; sha256 482e9c48)
