# Pub. 525 Worksheets 2a and 2 — recoveries of 2024 itemized deductions (Schedule 1, lines 1 and 8z)

- Document: `rec` (worksheet, tax year 2025)
- Note: Used when, besides any state or local income tax refund, an amount deducted on the 2024 Schedule A was paid back in 2025 (a refund of real estate or personal property tax, mortgage interest refunded, a medical bill reimbursed, or another itemized deduction refunded). Worksheet 2a splits the state and local tax refunds under the 2024 limit on the deduction for taxes; Worksheet 2 tests the total against the 2024 itemized deductions over the 2024 standard deduction and against negative 2024 taxable income, and divides the taxable part between line 1 and line 8z. A recovery of an amount paid or deducted before 2024, of a deduction taken without itemizing or of a credit, of general sales tax, of deductions on two 2024 returns on a joint 2025 return, and the 2024 alternative minimum tax, unused credit, 0% capital gain, dependent, nonresident and joint state return cases are refused.

## (helper) — `rec.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [p525] p. 27, Worksheet 2, line 8, "If the result is zero or less, stop here. The amounts on lines 1a, 1b, and 2 aren’t taxable" (2025; sha256 39b0fa5e)

## (helper) — `rec.no`

- **Authored helper label:** Year parameter sa.no (no)
- **Encoded (Bool):** Enter false (sa.no).
- Expr: `{"op":"param","ref":"sa.no"}`
- Cite: [p525] p. 24, Recoveries, "A recovery is a return of an amount you deducted or took a credit for in an earlier year" (2025; sha256 39b0fa5e)

## (gate) — `rec.before_prior_year`

- **Authored helper label:** Was any of the money paid back for something paid or deducted before 2024?
- **Encoded (Bool):** Input — Was any of the money paid back to you (or, on a joint return, your spouse) in 2025 for something you paid or deducted in a year before 2024?
- Expr: `{"op":"input","source":"Was any of the money paid back to you (or, on a joint return, your spouse) in 2025 for something you paid or deducted in a year before 2024?"}`
- Cite: [p525] p. 27, Worksheet 2, "If you recovered amounts from more than 1 year, such as a state income tax refund from 2024 and a casualty loss reimbursement from 2023, complete a separate worksheet for each year"; p. 24, Recovery for 2 or more years, "you must allocate, on a pro rata basis, the recovered amount between the years in which you paid it" (2025; sha256 39b0fa5e)

## (gate) — `rec.before_prior_year_if_any`

- **Authored helper label:** A recovery for something paid or deducted before 2024, asked only after a Yes to the question on money paid back (no otherwise)
- **Encoded (Bool):** Choose — [scope helper "In 2025, were you (or, on a joint return, your spouse) paid back an amount whose deduction or credit on an earlier year's return lowered your tax, other than a state or local income tax refund?" = true → helper "Was any of the money paid back for something paid or deducted before 2024?"] [scope helper "In 2025, were you (or, on a joint return, your spouse) paid back an amount whose deduction or credit on an earlier year's return lowered your tax, other than a state or local income tax refund?" = false → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.recovery",{"const":true}],"op":"test"},"then":"rec.before_prior_year"},{"guard":{"eq":["scope.recovery",{"const":false}],"op":"test"},"then":"rec.no"}],"op":"choose"}`
- Cite: [p525] p. 27, Worksheet 2, "complete a separate worksheet for each year. Use information from your tax return for the year the expense was deducted" (2025; sha256 39b0fa5e)

## (gate) — `rec.nonitemized`

- **Authored helper label:** Was any of the money paid back for a deduction taken without itemizing, or for a credit?
- **Encoded (Bool):** Input — Was any of the money paid back to you (or, on a joint return, your spouse) in 2025 for a deduction taken without itemizing (for example a bad debt paid after you deducted it, or a business expense) or for an item on which you claimed a tax credit?
- Expr: `{"op":"input","source":"Was any of the money paid back to you (or, on a joint return, your spouse) in 2025 for a deduction taken without itemizing (for example a bad debt paid after you deducted it, or a business expense) or for an item on which you claimed a tax credit?"}`
- Cite: [p525] p. 24, Recoveries, "You may also have recoveries of nonitemized deductions (such as payments on previously deducted bad debts) and recoveries of items for which you previously claimed a tax credit"; p. 25, Caution, "If you also recovered an amount deducted as a nonitemized deduction, figure the amount of that recovery to include in your income and add it to your adjusted gross income (AGI) before applying the rules explained here" (2025; sha256 39b0fa5e)

## (gate) — `rec.nonitemized_if_any`

- **Authored helper label:** A recovery of a deduction taken without itemizing or of a credit, asked only after a Yes to the question on money paid back (no otherwise)
- **Encoded (Bool):** Choose — [scope helper "In 2025, were you (or, on a joint return, your spouse) paid back an amount whose deduction or credit on an earlier year's return lowered your tax, other than a state or local income tax refund?" = true → helper "Was any of the money paid back for a deduction taken without itemizing, or for a credit?"] [scope helper "In 2025, were you (or, on a joint return, your spouse) paid back an amount whose deduction or credit on an earlier year's return lowered your tax, other than a state or local income tax refund?" = false → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.recovery",{"const":true}],"op":"test"},"then":"rec.nonitemized"},{"guard":{"eq":["scope.recovery",{"const":false}],"op":"test"},"then":"rec.no"}],"op":"choose"}`
- Cite: [p525] p. 28, Nonitemized Deduction Recoveries, "This section discusses recovery of deductions other than itemized deductions"; p. 28, Amounts Recovered for Credits, "you must increase your 2024 tax by the amount of the recovery" (2025; sha256 39b0fa5e)

## (gate) — `rec.sales_tax`

- **Authored helper label:** Was any of the money paid back a refund of general sales tax?
- **Encoded (Bool):** Input — Was any of the money paid back to you (or, on a joint return, your spouse) in 2025 a refund of state or local general sales tax?
- Expr: `{"op":"input","source":"Was any of the money paid back to you (or, on a joint return, your spouse) in 2025 a refund of state or local general sales tax?"}`
- Cite: [p525] p. 27, Worksheet 2, footnote 2, "If you deducted state and local general sales taxes and received a refund of those taxes, include the amount on line 2, but don’t enter more than the excess of your sales tax deduction over your state and local income tax you could have deducted" (2025; sha256 39b0fa5e)

## (gate) — `rec.sales_tax_if_any`

- **Authored helper label:** A refund of general sales tax, asked only after a Yes to the question on money paid back (no otherwise)
- **Encoded (Bool):** Choose — [scope helper "In 2025, were you (or, on a joint return, your spouse) paid back an amount whose deduction or credit on an earlier year's return lowered your tax, other than a state or local income tax refund?" = true → helper "Was any of the money paid back a refund of general sales tax?"] [scope helper "In 2025, were you (or, on a joint return, your spouse) paid back an amount whose deduction or credit on an earlier year's return lowered your tax, other than a state or local income tax refund?" = false → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.recovery",{"const":true}],"op":"test"},"then":"rec.sales_tax"},{"guard":{"eq":["scope.recovery",{"const":false}],"op":"test"},"then":"rec.no"}],"op":"choose"}`
- Cite: [p525] p. 24, Example 27, "The maximum refund that you may have to include in income is $500 because it’s less than the excess of the tax deducted" (2025; sha256 39b0fa5e)

## (helper) — `rec.joint_any`

- **Authored helper label:** Money paid back on a joint 2025 return
- **Encoded (Bool):** scope helper "In 2025, were you (or, on a joint return, your spouse) paid back an amount whose deduction or credit on an earlier year's return lowered your tax, other than a state or local income tax refund?" = true and refund helper "Married filing jointly for 2025" = true
- Expr: `{"all":[{"eq":["scope.recovery",{"const":true}],"op":"test"},{"eq":["refund.joint",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [p525] p. 27, Worksheet 2, "Use information from your tax return for the year the expense was deducted" (2025; sha256 39b0fa5e)

## (gate) — `rec.two_returns`

- **Authored helper label:** Were these amounts for deductions on two 2024 returns, each of you filing your own?
- **Encoded (Bool):** Input — Were the amounts paid back in 2025 for deductions on two 2024 federal returns, each of you filing your own (for example before you married, or as married filing separately)?
- Interpretation: amb.2025.rec_two_returns
- Expr: `{"op":"input","source":"Were the amounts paid back in 2025 for deductions on two 2024 federal returns, each of you filing your own (for example before you married, or as married filing separately)?"}`
- Cite: [p525] p. 27, Worksheet 2, "complete a separate worksheet for each year. Use information from your tax return for the year the expense was deducted" (2025; sha256 39b0fa5e)

## (gate) — `rec.two_returns_if_joint`

- **Authored helper label:** Amounts for deductions on two 2024 returns, asked only on a joint 2025 return after a Yes to the question on money paid back (no otherwise)
- **Encoded (Bool):** Choose — [helper "Money paid back on a joint 2025 return" = true → helper "Were these amounts for deductions on two 2024 returns, each of you filing your own?"] [helper "Money paid back on a joint 2025 return" = false → helper "Year parameter sa.no (no)"]
- Interpretation: amb.2025.rec_two_returns
- Expr: `{"alternatives":[{"guard":{"eq":["rec.joint_any",{"const":true}],"op":"test"},"then":"rec.two_returns"},{"guard":{"eq":["rec.joint_any",{"const":false}],"op":"test"},"then":"rec.no"}],"op":"choose"}`
- Cite: [p525] p. 27, Worksheet 2, "Use information from your tax return for the year the expense was deducted" (2025; sha256 39b0fa5e)

## (helper) — `rec.path`

- **Authored helper label:** Worksheet 2 is used — money was paid back for 2024 and you itemized deductions for 2024
- **Encoded (Bool):** Choose — [scope helper "In 2025, were you (or, on a joint return, your spouse) paid back an amount whose deduction or credit on an earlier year's return lowered your tax, other than a state or local income tax refund?" = false → helper "Year parameter sa.no (no)"] [scope helper "In 2025, were you (or, on a joint return, your spouse) paid back an amount whose deduction or credit on an earlier year's return lowered your tax, other than a state or local income tax refund?" = true → refund helper "Did you itemize deductions on Schedule A for 2024?"]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.recovery",{"const":false}],"op":"test"},"then":"rec.no"},{"guard":{"eq":["scope.recovery",{"const":true}],"op":"test"},"then":"refund.itemized"}],"op":"choose"}`
- Cite: [p525] p. 24, Deductions not itemized, "If you didn’t itemize deductions for the year for which you received the recovery of an expense that was deductible only if you itemized, don’t include any of the recovery amount in your income"; p. 24, Itemized Deduction Recoveries, statement 2, "You received a refund other than an income tax refund, such as a general sales tax or real property tax refund" (2025; sha256 39b0fa5e)

## (helper) — `rec.has_property_tax`

- **Authored helper label:** Was any of it a refund of 2024 real estate or personal property tax?
- **Encoded (Bool):** Input — Was any of it a refund of state or local real estate tax or personal property tax you deducted for 2024?
- Expr: `{"op":"input","source":"Was any of it a refund of state or local real estate tax or personal property tax you deducted for 2024?"}`
- Cite: [p525] p. 26, Worksheet 2a, line 2, "Enter the refunds received for state and local real estate taxes and state and local personal property taxes" (2025; sha256 39b0fa5e)

## (gate) — `rec.has_property_tax_if_path`

- **Authored helper label:** A refund of 2024 real estate or personal property tax, asked only when Worksheet 2 is used (no otherwise)
- **Encoded (Bool):** Choose — [helper "Worksheet 2 is used — money was paid back for 2024 and you itemized deductions for 2024" = true → helper "Was any of it a refund of 2024 real estate or personal property tax?"] [helper "Worksheet 2 is used — money was paid back for 2024 and you itemized deductions for 2024" = false → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rec.path",{"const":true}],"op":"test"},"then":"rec.has_property_tax"},{"guard":{"eq":["rec.path",{"const":false}],"op":"test"},"then":"rec.no"}],"op":"choose"}`
- Cite: [p525] p. 26, Worksheet 2a, line 2, "Enter the refunds received for state and local real estate taxes and state and local personal property taxes" (2025; sha256 39b0fa5e)

## (helper) — `rec.property_tax`

- **Authored helper label:** Refunds of 2024 real estate and personal property taxes received in 2025
- **Encoded (NonNegDollars):** Input — The refunds you (or, on a joint return, your spouse) received in 2025 of state and local real estate taxes and state and local personal property taxes you deducted for 2024
- Expr: `{"op":"input","source":"The refunds you (or, on a joint return, your spouse) received in 2025 of state and local real estate taxes and state and local personal property taxes you deducted for 2024"}`
- Cite: [p525] p. 26, Worksheet 2a, line 2, "Enter the refunds received for state and local real estate taxes and state and local personal property taxes" (2025; sha256 39b0fa5e)

## (gate) — `rec.property_tax_if_has`

- **Authored helper label:** Refunds of 2024 real estate and personal property taxes (zero without one)
- **Encoded (NonNegDollars):** Choose — [helper "A refund of 2024 real estate or personal property tax, asked only when Worksheet 2 is used (no otherwise)" = true → helper "Refunds of 2024 real estate and personal property taxes received in 2025"] [helper "A refund of 2024 real estate or personal property tax, asked only when Worksheet 2 is used (no otherwise)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rec.has_property_tax_if_path",{"const":true}],"op":"test"},"then":"rec.property_tax"},{"guard":{"eq":["rec.has_property_tax_if_path",{"const":false}],"op":"test"},"then":"rec.zero"}],"op":"choose"}`
- Cite: [p525] p. 26, Worksheet 2a, line 2, "Enter the refunds received for state and local real estate taxes and state and local personal property taxes" (2025; sha256 39b0fa5e)

## (helper) — `rec.has_mortgage`

- **Authored helper label:** Was any of it 2024 mortgage interest refunded (Form 1098 box 4)?
- **Encoded (Bool):** Input — Was any of it a refund or credit of home mortgage interest you deducted for 2024 (box 4 of Form 1098)?
- Expr: `{"op":"input","source":"Was any of it a refund or credit of home mortgage interest you deducted for 2024 (box 4 of Form 1098)?"}`
- Cite: [p525] p. 24, Mortgage interest refund, "If you received a refund or credit in 2025 of mortgage interest paid in an earlier year, the amount should be shown in box 4 of Form 1098" (2025; sha256 39b0fa5e)

## (gate) — `rec.has_mortgage_if_path`

- **Authored helper label:** Mortgage interest refunded, asked only when Worksheet 2 is used (no otherwise)
- **Encoded (Bool):** Choose — [helper "Worksheet 2 is used — money was paid back for 2024 and you itemized deductions for 2024" = true → helper "Was any of it 2024 mortgage interest refunded (Form 1098 box 4)?"] [helper "Worksheet 2 is used — money was paid back for 2024 and you itemized deductions for 2024" = false → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rec.path",{"const":true}],"op":"test"},"then":"rec.has_mortgage"},{"guard":{"eq":["rec.path",{"const":false}],"op":"test"},"then":"rec.no"}],"op":"choose"}`
- Cite: [p525] p. 24, Mortgage interest refund, "You may have to include it in your income under the rules explained in the following discussions" (2025; sha256 39b0fa5e)

## (helper) — `rec.mortgage`

- **Authored helper label:** Mortgage interest deducted for 2024 and refunded in 2025
- **Encoded (NonNegDollars):** Input — The refund or credit received in 2025 of home mortgage interest deducted on your (or, on a joint return, your and your spouse's) 2024 Schedule A (box 4 of Form 1098), but not more than the mortgage interest deducted
- Interpretation: amb.2025.rec_mortgage_cap
- Expr: `{"op":"input","source":"The refund or credit received in 2025 of home mortgage interest deducted on your (or, on a joint return, your and your spouse's) 2024 Schedule A (box 4 of Form 1098), but not more than the mortgage interest deducted"}`
- Cite: [p525] p. 24, Mortgage interest refund, "the amount should be shown in box 4 of Form 1098"; p. 27, Worksheet 2, footnote 2, "Don’t enter more than the amount deducted for the prior year" (2025; sha256 39b0fa5e)

## (gate) — `rec.mortgage_if_has`

- **Authored helper label:** Mortgage interest refunded (zero without one)
- **Encoded (NonNegDollars):** Choose — [helper "Mortgage interest refunded, asked only when Worksheet 2 is used (no otherwise)" = true → helper "Mortgage interest deducted for 2024 and refunded in 2025"] [helper "Mortgage interest refunded, asked only when Worksheet 2 is used (no otherwise)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rec.has_mortgage_if_path",{"const":true}],"op":"test"},"then":"rec.mortgage"},{"guard":{"eq":["rec.has_mortgage_if_path",{"const":false}],"op":"test"},"then":"rec.zero"}],"op":"choose"}`
- Cite: [p525] p. 27, Worksheet 2, line 2, "Enter the total of all other Schedule A (Form 1040) refunds or reimbursements" (2025; sha256 39b0fa5e)

## (helper) — `rec.has_medical`

- **Authored helper label:** Was any of it a reimbursement of 2024 medical or dental expenses?
- **Encoded (Bool):** Input — Was any of it a reimbursement, for example from insurance, of 2024 medical or dental expenses you deducted on your 2024 Schedule A?
- Expr: `{"op":"input","source":"Was any of it a reimbursement, for example from insurance, of 2024 medical or dental expenses you deducted on your 2024 Schedule A?"}`
- Cite: [p525] p. 26, Example 34, "In 2025, you received a $500 reimbursement from your medical insurance for your 2024 expenses" (2025; sha256 39b0fa5e)

## (gate) — `rec.has_medical_if_path`

- **Authored helper label:** A medical reimbursement, asked only when Worksheet 2 is used (no otherwise)
- **Encoded (Bool):** Choose — [helper "Worksheet 2 is used — money was paid back for 2024 and you itemized deductions for 2024" = true → helper "Was any of it a reimbursement of 2024 medical or dental expenses?"] [helper "Worksheet 2 is used — money was paid back for 2024 and you itemized deductions for 2024" = false → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rec.path",{"const":true}],"op":"test"},"then":"rec.has_medical"},{"guard":{"eq":["rec.path",{"const":false}],"op":"test"},"then":"rec.no"}],"op":"choose"}`
- Cite: [p525] p. 25, Example 30, "Medical expenses" (2025; sha256 39b0fa5e)

## (helper) — `rec.medical`

- **Authored helper label:** Reimbursements in 2025 of 2024 medical and dental expenses
- **Encoded (NonNegDollars):** Input — The reimbursements you (or, on a joint return, your spouse) received in 2025 of medical and dental expenses paid in 2024
- Expr: `{"op":"input","source":"The reimbursements you (or, on a joint return, your spouse) received in 2025 of medical and dental expenses paid in 2024"}`
- Cite: [p525] p. 26, Example 34, "In 2025, you received a $500 reimbursement from your medical insurance for your 2024 expenses" (2025; sha256 39b0fa5e)

## (helper) — `rec.medical_deducted`

- **Authored helper label:** The medical and dental expense deduction on your 2024 Schedule A, line 4
- **Encoded (NonNegDollars):** Input — The amount on line 4 of your 2024 Schedule A (the medical and dental expenses you deducted)
- Expr: `{"op":"input","source":"The amount on line 4 of your 2024 Schedule A (the medical and dental expenses you deducted)"}`
- Cite: [p525] p. 26, Example 34, "The only amount of the $500 reimbursement that must be included in your income for 2025 is $200, the amount actually deducted"; p. 26, Recovery limited to deduction, "The amount you include in your income is limited to the smaller of: • The amount deducted, or • The amount recovered" (2025; sha256 39b0fa5e)

## (gate) — `rec.medical_if_has`

- **Authored helper label:** Medical reimbursements (zero without one)
- **Encoded (NonNegDollars):** Choose — [helper "A medical reimbursement, asked only when Worksheet 2 is used (no otherwise)" = true → helper "Reimbursements in 2025 of 2024 medical and dental expenses"] [helper "A medical reimbursement, asked only when Worksheet 2 is used (no otherwise)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rec.has_medical_if_path",{"const":true}],"op":"test"},"then":"rec.medical"},{"guard":{"eq":["rec.has_medical_if_path",{"const":false}],"op":"test"},"then":"rec.zero"}],"op":"choose"}`
- Cite: [p525] p. 27, Worksheet 2, line 2, "Enter the total of all other Schedule A (Form 1040) refunds or reimbursements" (2025; sha256 39b0fa5e)

## (gate) — `rec.medical_deducted_if_has`

- **Authored helper label:** The 2024 medical deduction, asked only with a medical reimbursement (zero without one)
- **Encoded (NonNegDollars):** Choose — [helper "A medical reimbursement, asked only when Worksheet 2 is used (no otherwise)" = true → helper "The medical and dental expense deduction on your 2024 Schedule A, line 4"] [helper "A medical reimbursement, asked only when Worksheet 2 is used (no otherwise)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rec.has_medical_if_path",{"const":true}],"op":"test"},"then":"rec.medical_deducted"},{"guard":{"eq":["rec.has_medical_if_path",{"const":false}],"op":"test"},"then":"rec.zero"}],"op":"choose"}`
- Cite: [p525] p. 26, Recovery limited to deduction, "You don’t include in your income any amount of your recovery that is more than the amount you deducted in the earlier year" (2025; sha256 39b0fa5e)

## (helper) — `rec.medical_counted`

- **Authored helper label:** Medical reimbursements counted, not more than the 2024 medical deduction
- **Encoded (NonNegDollars):** Enter the smaller of helper "Medical reimbursements (zero without one)" or helper "The 2024 medical deduction, asked only with a medical reimbursement (zero without one)".
- Expr: `{"of":["rec.medical_if_has","rec.medical_deducted_if_has"],"op":"smaller_of"}`
- Cite: [p525] p. 26, Recovery limited to deduction, "The amount you include in your income is limited to the smaller of: • The amount deducted, or • The amount recovered"; p. 27, Worksheet 2, footnote 2, "Don’t enter more than the amount deducted for the prior year" (2025; sha256 39b0fa5e)

## (helper) — `rec.has_other`

- **Authored helper label:** Was any of it a refund of something else you itemized for 2024?
- **Encoded (Bool):** Input — Was any of it a refund or reimbursement of something else you deducted on your 2024 Schedule A (not state or local income, real estate, personal property or sales tax, mortgage interest, or medical expenses), such as a casualty loss reimbursed?
- Expr: `{"op":"input","source":"Was any of it a refund or reimbursement of something else you deducted on your 2024 Schedule A (not state or local income, real estate, personal property or sales tax, mortgage interest, or medical expenses), such as a casualty loss reimbursed?"}`
- Cite: [p525] p. 27, Worksheet 2, line 2, "Enter the total of all other Schedule A (Form 1040) refunds or reimbursements (excluding the amounts you entered on lines 1a and 1b)" (2025; sha256 39b0fa5e)

## (gate) — `rec.has_other_if_path`

- **Authored helper label:** Another itemized deduction refunded, asked only when Worksheet 2 is used (no otherwise)
- **Encoded (Bool):** Choose — [helper "Worksheet 2 is used — money was paid back for 2024 and you itemized deductions for 2024" = true → helper "Was any of it a refund of something else you itemized for 2024?"] [helper "Worksheet 2 is used — money was paid back for 2024 and you itemized deductions for 2024" = false → helper "Year parameter sa.no (no)"]
- Expr: `{"alternatives":[{"guard":{"eq":["rec.path",{"const":true}],"op":"test"},"then":"rec.has_other"},{"guard":{"eq":["rec.path",{"const":false}],"op":"test"},"then":"rec.no"}],"op":"choose"}`
- Cite: [p525] p. 27, Worksheet 2, line 2, "Enter the total of all other Schedule A (Form 1040) refunds or reimbursements" (2025; sha256 39b0fa5e)

## (helper) — `rec.other`

- **Authored helper label:** Other 2024 itemized deductions refunded or reimbursed in 2025
- **Encoded (NonNegDollars):** Input — The refunds and reimbursements you (or, on a joint return, your spouse) received in 2025 of other deductions on your 2024 Schedule A (not state or local taxes, mortgage interest or medical expenses)
- Expr: `{"op":"input","source":"The refunds and reimbursements you (or, on a joint return, your spouse) received in 2025 of other deductions on your 2024 Schedule A (not state or local taxes, mortgage interest or medical expenses)"}`
- Cite: [p525] p. 27, Worksheet 2, line 2, "Enter the total of all other Schedule A (Form 1040) refunds or reimbursements (excluding the amounts you entered on lines 1a and 1b)" (2025; sha256 39b0fa5e)

## (helper) — `rec.other_deducted`

- **Authored helper label:** The amount deducted on your 2024 Schedule A for the items refunded
- **Encoded (NonNegDollars):** Input — The amount deducted on your 2024 Schedule A for the items so refunded or reimbursed
- Expr: `{"op":"input","source":"The amount deducted on your 2024 Schedule A for the items so refunded or reimbursed"}`
- Cite: [p525] p. 27, Worksheet 2, footnote 2, "Don’t enter more than the amount deducted for the prior year" (2025; sha256 39b0fa5e)

## (gate) — `rec.other_if_has`

- **Authored helper label:** Other itemized deductions refunded (zero without one)
- **Encoded (NonNegDollars):** Choose — [helper "Another itemized deduction refunded, asked only when Worksheet 2 is used (no otherwise)" = true → helper "Other 2024 itemized deductions refunded or reimbursed in 2025"] [helper "Another itemized deduction refunded, asked only when Worksheet 2 is used (no otherwise)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rec.has_other_if_path",{"const":true}],"op":"test"},"then":"rec.other"},{"guard":{"eq":["rec.has_other_if_path",{"const":false}],"op":"test"},"then":"rec.zero"}],"op":"choose"}`
- Cite: [p525] p. 27, Worksheet 2, line 2, "Enter the total of all other Schedule A (Form 1040) refunds or reimbursements" (2025; sha256 39b0fa5e)

## (gate) — `rec.other_deducted_if_has`

- **Authored helper label:** The 2024 deduction for those items, asked only with such a refund (zero without one)
- **Encoded (NonNegDollars):** Choose — [helper "Another itemized deduction refunded, asked only when Worksheet 2 is used (no otherwise)" = true → helper "The amount deducted on your 2024 Schedule A for the items refunded"] [helper "Another itemized deduction refunded, asked only when Worksheet 2 is used (no otherwise)" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rec.has_other_if_path",{"const":true}],"op":"test"},"then":"rec.other_deducted"},{"guard":{"eq":["rec.has_other_if_path",{"const":false}],"op":"test"},"then":"rec.zero"}],"op":"choose"}`
- Cite: [p525] p. 27, Worksheet 2, footnote 2, "Don’t enter more than the amount deducted for the prior year" (2025; sha256 39b0fa5e)

## (helper) — `rec.other_counted`

- **Authored helper label:** Other refunds counted, not more than the 2024 deduction for them
- **Encoded (NonNegDollars):** Enter the smaller of helper "Other itemized deductions refunded (zero without one)" or helper "The 2024 deduction for those items, asked only with such a refund (zero without one)".
- Expr: `{"of":["rec.other_if_has","rec.other_deducted_if_has"],"op":"smaller_of"}`
- Cite: [p525] p. 27, Worksheet 2, footnote 2, "Don’t enter more than the amount deducted for the prior year" (2025; sha256 39b0fa5e)

## 2a:1 — `rec.w2a_line1`

- **IRS:** Enter the income tax refund from Form(s) 1099-G (or similar statement)
- **Encoded (NonNegDollars):** Choose — [refund helper "Any state or local income tax refund received in 2025" = false → helper "Year parameter sales.zero"] [refund helper "Any state or local income tax refund received in 2025" = true → refund helper "State or local income tax refunds, credits or offsets received in 2025 (zero when you did not itemize deductions for 2024 or deducted general sales taxes, since none of the refund is then taxable)"]
- Expr: `{"alternatives":[{"guard":{"eq":["refund.has",{"const":false}],"op":"test"},"then":"rec.zero"},{"guard":{"eq":["refund.has",{"const":true}],"op":"test"},"then":"refund.received_if_worksheet"}],"op":"choose"}`
- Cite: [p525] p. 26, Worksheet 2a, line 1, "Enter the income tax refund from Form(s) 1099-G (or similar statement)"; p. 24, State tax refund, "Because you didn’t choose to deduct the state income tax, you don’t include the state income tax refund in income" (2025; sha256 39b0fa5e)

## 2a:2 — `rec.w2a_line2`

- **IRS:** Enter the refunds received for state and local real estate taxes and state and local personal property taxes
- **Encoded (NonNegDollars):** Enter the amount from helper "Refunds of 2024 real estate and personal property taxes (zero without one)".
- Expr: `{"from":"rec.property_tax_if_has","op":"copy"}`
- Cite: [p525] p. 26, Worksheet 2a, line 2, "Enter the refunds received for state and local real estate taxes and state and local personal property taxes" (2025; sha256 39b0fa5e)

## 2a:6 — `rec.w2a_line6`

- **IRS:** Add lines 1 and 2 and enter the result here
- **Encoded (NonNegDollars):** Add line 2a:1 and line 2a:2.
- Expr: `{"of":["rec.w2a_line1","rec.w2a_line2"],"op":"sum"}`
- Cite: [p525] p. 26, Worksheet 2a, line 6, "Add lines 1 and 2 and enter the result here" (2025; sha256 39b0fa5e)

## 2a:3 — `rec.w2a_line3`

- **IRS:** Total state and local refunds. Add lines 1 and 2. But don’t enter more than the amount of your state and local taxes shown on your 2024 Schedule A, line 5d
- **Encoded (NonNegDollars):** Enter the smaller of line 2a:6 or refund helper "The amount on your 2024 Schedule A, line 5d".
- Expr: `{"of":["rec.w2a_line6","refund.line5d_prior_year"],"op":"smaller_of"}`
- Cite: [p525] p. 26, Worksheet 2a, line 3, "Total state and local refunds. Add lines 1 and 2. But don’t enter more than the amount of your state and local taxes shown on your 2024 Schedule A (Form 1040), line 5d" (2025; sha256 39b0fa5e)

## (helper) — `rec.w2a_cap`

- **Authored helper label:** Is the amount of state and local taxes paid in 2024 (generally, your 2024 Schedule A, line 5d) more than the amount on your 2024 Schedule A, line 5e?
- **Encoded (Bool):** refund helper "The amount on your 2024 Schedule A, line 5d" > refund helper "The amount on your 2024 Schedule A, line 5e"
- Expr: `{"gt":["refund.line5d_prior_year","refund.line5e_prior_year"],"op":"test"}`
- Cite: [p525] p. 26, Worksheet 2a, line 4, "Is the amount of state and local income taxes (or general sales taxes), real estate taxes, and personal property taxes paid in 2024" (2025; sha256 39b0fa5e)

## 2a:4 — `rec.w2a_line4`

- **IRS:** Is the amount of state and local taxes paid in 2024 (generally, your 2024 Schedule A, line 5d) more than the amount on your 2024 Schedule A, line 5e? No: the amount from line 3. Yes: subtract line 5e from line 5d
- **Encoded (NonNegDollars):** Choose — [helper "Is the amount of state and local taxes paid in 2024 (generally, your 2024 Schedule A, line 5d) more than the amount on your 2024 Schedule A, line 5e?" = true → refund line 2] [helper "Is the amount of state and local taxes paid in 2024 (generally, your 2024 Schedule A, line 5d) more than the amount on your 2024 Schedule A, line 5e?" = false → line 2a:3]
- Expr: `{"alternatives":[{"guard":{"eq":["rec.w2a_cap",{"const":true}],"op":"test"},"then":"refund.line2"},{"guard":{"eq":["rec.w2a_cap",{"const":false}],"op":"test"},"then":"rec.w2a_line3"}],"op":"choose"}`
- Cite: [p525] p. 26, Worksheet 2a, line 4, "No. Enter the amount from line 3 on line 4 and go to line 6" and "Yes. Subtract the amount on your 2024 Schedule A (Form 1040), line 5e" (2025; sha256 39b0fa5e)

## (helper) — `rec.w2a_line5_more`

- **Authored helper label:** Is the amount on line 3 more than the amount on line 4?
- **Encoded (Bool):** line 2a:3 > line 2a:4
- Expr: `{"gt":["rec.w2a_line3","rec.w2a_line4"],"op":"test"}`
- Cite: [p525] p. 26, Worksheet 2a, line 5, "Is the amount on line 3 more than the amount on line 4?" and "No. [STOP] None of the refunds on line 1 or 2 are taxable" (2025; sha256 39b0fa5e)

## 2a:5 — `rec.w2a_line5`

- **IRS:** Subtract line 4 from line 3
- **Encoded (NonNegDollars):** Subtract line 2a:4 from line 2a:3. If zero or less, enter -0-.
- Expr: `{"from":"rec.w2a_line3","op":"subtract_floor0","take":"rec.w2a_line4"}`
- Cite: [p525] p. 26, Worksheet 2a, line 5, "Yes. Subtract line 4 from line 3 and enter the result here" (2025; sha256 39b0fa5e)

## (helper) — `rec.w2a_line7_share`

- **Authored helper label:** Divide line 1 by line 6, then multiply by the amount on line 5
- **Encoded (NonNegDollars):** Divide line 2a:1 by line 2a:6, rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply line 2a:5 by the result.
- Interpretation: amb.2025.rec_ratio_places
- Expr: `{"amount":"rec.w2a_line5","op":"prorate","part":"rec.w2a_line1","places":6,"whole":"rec.w2a_line6"}`
- Cite: [p525] p. 26, Worksheet 2a, line 7, "If there is an amount on line 5, divide line 1 by line 6. Then multiply by the amount on line 5" (2025; sha256 39b0fa5e)

## (helper) — `rec.w2a_line7_capped`

- **Authored helper label:** Line 7 when the 2024 limit on taxes applied: zero if line 3 is not more than line 4 (none of the refunds is taxable), otherwise line 1 divided by line 6 times line 5
- **Encoded (NonNegDollars):** Choose — [helper "Is the amount on line 3 more than the amount on line 4?" = true → helper "Divide line 1 by line 6, then multiply by the amount on line 5"] [helper "Is the amount on line 3 more than the amount on line 4?" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rec.w2a_line5_more",{"const":true}],"op":"test"},"then":"rec.w2a_line7_share"},{"guard":{"eq":["rec.w2a_line5_more",{"const":false}],"op":"test"},"then":"rec.zero"}],"op":"choose"}`
- Cite: [p525] p. 26, Worksheet 2a, line 5, "No. [STOP] None of the refunds on line 1 or 2 are taxable"; line 7, "If there is an amount on line 5, divide line 1 by line 6" (2025; sha256 39b0fa5e)

## 2a:7 — `rec.w2a_line7`

- **IRS:** Amount to include on Worksheet 2, line 1a: if line 5 is blank, the amount from line 1; if there is an amount on line 5, line 1 divided by line 6 times line 5
- **Encoded (NonNegDollars):** Choose — [helper "Is the amount of state and local taxes paid in 2024 (generally, your 2024 Schedule A, line 5d) more than the amount on your 2024 Schedule A, line 5e?" = false → line 2a:1] [helper "Is the amount of state and local taxes paid in 2024 (generally, your 2024 Schedule A, line 5d) more than the amount on your 2024 Schedule A, line 5e?" = true → helper "Line 7 when the 2024 limit on taxes applied: zero if line 3 is not more than line 4 (none of the refunds is taxable), otherwise line 1 divided by line 6 times line 5"]
- Expr: `{"alternatives":[{"guard":{"eq":["rec.w2a_cap",{"const":false}],"op":"test"},"then":"rec.w2a_line1"},{"guard":{"eq":["rec.w2a_cap",{"const":true}],"op":"test"},"then":"rec.w2a_line7_capped"}],"op":"choose"}`
- Cite: [p525] p. 26, Worksheet 2a, line 7, "Amount to include on Worksheet 2, line 1a: • If line 5 is blank, enter the amount from line 1" (2025; sha256 39b0fa5e)

## (helper) — `rec.w2a_line8_share`

- **Authored helper label:** Divide line 2 by line 6, then multiply by the amount on line 5
- **Encoded (NonNegDollars):** Divide line 2a:2 by line 2a:6, rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply line 2a:5 by the result.
- Interpretation: amb.2025.rec_ratio_places
- Expr: `{"amount":"rec.w2a_line5","op":"prorate","part":"rec.w2a_line2","places":6,"whole":"rec.w2a_line6"}`
- Cite: [p525] p. 26, Worksheet 2a, line 8, "If there is an amount on line 5, divide line 2 by line 6. Then multiply by the amount on line 5" (2025; sha256 39b0fa5e)

## (helper) — `rec.w2a_line8_capped`

- **Authored helper label:** Line 8 when the 2024 limit on taxes applied: zero if line 3 is not more than line 4, otherwise line 2 divided by line 6 times line 5
- **Encoded (NonNegDollars):** Choose — [helper "Is the amount on line 3 more than the amount on line 4?" = true → helper "Divide line 2 by line 6, then multiply by the amount on line 5"] [helper "Is the amount on line 3 more than the amount on line 4?" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rec.w2a_line5_more",{"const":true}],"op":"test"},"then":"rec.w2a_line8_share"},{"guard":{"eq":["rec.w2a_line5_more",{"const":false}],"op":"test"},"then":"rec.zero"}],"op":"choose"}`
- Cite: [p525] p. 26, Worksheet 2a, line 5, "No. [STOP] None of the refunds on line 1 or 2 are taxable"; line 8, "If there is an amount on line 5, divide line 2 by line 6" (2025; sha256 39b0fa5e)

## 2a:8 — `rec.w2a_line8`

- **IRS:** Amount to include on Worksheet 2, line 1b: if line 5 is blank, the amount from line 2; if there is an amount on line 5, line 2 divided by line 6 times line 5
- **Encoded (NonNegDollars):** Choose — [helper "Is the amount of state and local taxes paid in 2024 (generally, your 2024 Schedule A, line 5d) more than the amount on your 2024 Schedule A, line 5e?" = false → line 2a:2] [helper "Is the amount of state and local taxes paid in 2024 (generally, your 2024 Schedule A, line 5d) more than the amount on your 2024 Schedule A, line 5e?" = true → helper "Line 8 when the 2024 limit on taxes applied: zero if line 3 is not more than line 4, otherwise line 2 divided by line 6 times line 5"]
- Expr: `{"alternatives":[{"guard":{"eq":["rec.w2a_cap",{"const":false}],"op":"test"},"then":"rec.w2a_line2"},{"guard":{"eq":["rec.w2a_cap",{"const":true}],"op":"test"},"then":"rec.w2a_line8_capped"}],"op":"choose"}`
- Cite: [p525] p. 26, Worksheet 2a, line 8, "Amount to include on Worksheet 2, line 1b: • If line 5 is blank, enter the amount from line 2" (2025; sha256 39b0fa5e)

## 1a — `rec.line1a`

- **IRS:** State/local income tax refund or credit
- **Encoded (NonNegDollars):** Enter the amount from line 2a:7.
- Expr: `{"from":"rec.w2a_line7","op":"copy"}`
- Cite: [p525] p. 27, Worksheet 2, line 1a, "State/local income tax refund or credit"; p. 27, NOTE, "Before completing lines 1a and 1b, see Worksheet 2a" (2025; sha256 39b0fa5e)

## 1b — `rec.line1b`

- **IRS:** State/local real estate and personal property taxes
- **Encoded (NonNegDollars):** Enter the amount from line 2a:8.
- Expr: `{"from":"rec.w2a_line8","op":"copy"}`
- Cite: [p525] p. 27, Worksheet 2, line 1b, "State/local real estate and personal property taxes" (2025; sha256 39b0fa5e)

## 2 — `rec.line2`

- **IRS:** Enter the total of all other Schedule A (Form 1040) refunds or reimbursements (excluding the amounts you entered on lines 1a and 1b)
- **Encoded (NonNegDollars):** Add helper "Mortgage interest refunded (zero without one)", helper "Medical reimbursements counted, not more than the 2024 medical deduction", and helper "Other refunds counted, not more than the 2024 deduction for them".
- Expr: `{"of":["rec.mortgage_if_has","rec.medical_counted","rec.other_counted"],"op":"sum"}`
- Cite: [p525] p. 27, Worksheet 2, line 2, "Enter the total of all other Schedule A (Form 1040) refunds or reimbursements (excluding the amounts you entered on lines 1a and 1b)"; footnote 2, "Don’t enter more than the amount deducted for the prior year" (2025; sha256 39b0fa5e)

## 3 — `rec.line3`

- **IRS:** Add lines 1a, 1b, and 2
- **Encoded (NonNegDollars):** Add line 1a, line 1b, and line 2.
- Expr: `{"of":["rec.line1a","rec.line1b","rec.line2"],"op":"sum"}`
- Cite: [p525] p. 27, Worksheet 2, line 3, "Add lines 1a, 1b, and 2" (2025; sha256 39b0fa5e)

## 4 — `rec.line4`

- **IRS:** Itemized deductions for the prior year. For 2024: Schedule A (Form 1040), line 17
- **Encoded (NonNegDollars):** Enter the amount from refund helper "Your total itemized deductions from your 2024 Schedule A, line 17".
- Expr: `{"from":"refund.line17_prior_year","op":"copy"}`
- Cite: [p525] p. 27, Worksheet 2, line 4, "Itemized deductions for the prior year. For 2024: • Schedule A (Form 1040), line 17" (2025; sha256 39b0fa5e)

## 5 — `rec.line5`

- **IRS:** Enter any amount previously refunded to you (don’t enter an amount from line 1a, 1b, or 2)
- **Encoded (NonNegDollars):** Enter the amount from helper "Year parameter sales.zero".
- Interpretation: amb.2025.rec_line5
- Expr: `{"from":"rec.zero","op":"copy"}`
- Cite: [p525] p. 27, Worksheet 2, line 5, "Enter any amount previously refunded to you (don’t enter an amount from line 1a, 1b, or 2)"; p. 24, Recovery and expense in same year, "If the refund or other recovery and the expense occur in the same year, the recovery reduces the deduction or credit and isn’t reported as income" (2025; sha256 39b0fa5e)

## 6 — `rec.line6`

- **IRS:** Subtract line 5 from line 4
- **Encoded (NonNegDollars):** Subtract line 5 from line 4. If zero or less, enter -0-.
- Expr: `{"from":"rec.line4","op":"subtract_floor0","take":"rec.line5"}`
- Cite: [p525] p. 27, Worksheet 2, line 6, "Subtract line 5 from line 4" (2025; sha256 39b0fa5e)

## (helper) — `rec.line7_mfs`

- **Authored helper label:** Married filing separately in 2024: zero if your spouse itemized deductions in 2024, otherwise the 2024 standard deduction
- **Encoded (NonNegDollars):** Choose — [refund helper "Did your spouse itemize deductions in 2024?" = true → helper "Year parameter sales.zero"] [refund helper "Did your spouse itemize deductions in 2024?" = false → refund line 7]
- Expr: `{"alternatives":[{"guard":{"eq":["refund.mfs_spouse_itemized",{"const":true}],"op":"test"},"then":"rec.zero"},{"guard":{"eq":["refund.mfs_spouse_itemized",{"const":false}],"op":"test"},"then":"refund.line7"}],"op":"choose"}`
- Cite: [p525] p. 25, Standard deduction limit, "Only your itemized deductions that are more than your standard deduction are subject to the recovery rule (unless you’re required to itemize your deductions)" (2025; sha256 39b0fa5e)

## (helper) — `rec.prior_mfs`

- **Authored helper label:** Your 2024 filing status was married filing separately
- **Encoded (Bool):** refund helper "The filing status claimed on your 2024 Form 1040 or 1040-SR" = 'mfs'
- Expr: `{"eq":["refund.status",{"const":"mfs"}],"op":"test"}`
- Cite: [p525] p. 25, Standard deduction for earlier years, "you must know the standard deduction for your filing status for the year the deduction was claimed" (2025; sha256 39b0fa5e)

## 7 — `rec.line7`

- **IRS:** Standard deduction for the prior year
- **Encoded (NonNegDollars):** Choose — [helper "Your 2024 filing status was married filing separately" = true → helper "Married filing separately in 2024: zero if your spouse itemized deductions in 2024, otherwise the 2024 standard deduction"] [helper "Your 2024 filing status was married filing separately" = false → refund line 7]
- Expr: `{"alternatives":[{"guard":{"eq":["rec.prior_mfs",{"const":true}],"op":"test"},"then":"rec.line7_mfs"},{"guard":{"eq":["rec.prior_mfs",{"const":false}],"op":"test"},"then":"refund.line7"}],"op":"choose"}`
- Cite: [p525] p. 27, Worksheet 2, line 7, "Standard deduction for the prior year"; footnote 3, "See the instructions for prior-year forms at IRS.gov for prior-year standard deduction"; p. 25, Standard deduction for earlier years, "you must know the standard deduction for your filing status for the year the deduction was claimed" (2025; sha256 39b0fa5e)

## 8 — `rec.line8`

- **IRS:** Subtract line 7 from line 6. If the result is zero or less, stop here. The amounts on lines 1a, 1b, and 2 aren’t taxable
- **Encoded (NonNegDollars):** Subtract line 7 from line 6. If zero or less, enter -0-.
- Expr: `{"from":"rec.line6","op":"subtract_floor0","take":"rec.line7"}`
- Cite: [p525] p. 27, Worksheet 2, line 8, "Subtract line 7 from line 6. If the result is zero or less, stop here. The amounts on lines 1a, 1b, and 2 aren’t taxable" (2025; sha256 39b0fa5e)

## 9 — `rec.line9`

- **IRS:** Enter the smaller of line 3 or line 8
- **Encoded (NonNegDollars):** Enter the smaller of line 3 or line 8.
- Expr: `{"of":["rec.line3","rec.line8"],"op":"smaller_of"}`
- Cite: [p525] p. 27, Worksheet 2, line 9, "Enter the smaller of line 3 or line 8"; p. 25, Example 32, "This is the smaller of your recoveries ($2,100) or the amount by which your itemized deductions were more than the standard deduction" (2025; sha256 39b0fa5e)

## (helper) — `rec.ti_positive`

- **Authored helper label:** Was your 2024 taxable income (Form 1040, line 15) more than zero?
- **Encoded (Bool):** Input — Is the amount on line 15 (taxable income) of your 2024 Form 1040 more than zero?
- Expr: `{"op":"input","source":"Is the amount on line 15 (taxable income) of your 2024 Form 1040 more than zero?"}`
- Cite: [p525] p. 27, Worksheet 2, line 10, "Taxable income for prior year" and "(2024 Form 1040, line 15"; footnote 4, "If taxable income is a negative amount, enter that amount in brackets. Don’t enter zero unless your taxable income is exactly zero" (2025; sha256 39b0fa5e)

## (helper) — `rec.agi_prior`

- **Authored helper label:** The amount on your 2024 Form 1040, line 11 (adjusted gross income)
- **Encoded (Dollars):** Input — The amount on line 11 (adjusted gross income) of your 2024 Form 1040, as a negative number if it is a loss
- Interpretation: amb.2025.rec_prior_taxable
- Expr: `{"op":"input","source":"The amount on line 11 (adjusted gross income) of your 2024 Form 1040, as a negative number if it is a loss"}`
- Cite: [p525] p. 26, Negative taxable income, "You have a negative taxable income for 2024 if your: • Form 1040, the sum of lines 12 and 13, was more than line 11" (2025; sha256 39b0fa5e)

## (helper) — `rec.ded_prior`

- **Authored helper label:** The amount on your 2024 Form 1040, line 14 (lines 12 and 13 added)
- **Encoded (NonNegDollars):** Input — The amount on line 14 of your 2024 Form 1040 (lines 12 and 13 added)
- Interpretation: amb.2025.rec_prior_taxable
- Expr: `{"op":"input","source":"The amount on line 14 of your 2024 Form 1040 (lines 12 and 13 added)"}`
- Cite: [p525] p. 26, Negative taxable income, "You have a negative taxable income for 2024 if your: • Form 1040, the sum of lines 12 and 13, was more than line 11" (2025; sha256 39b0fa5e)

## 10 — `rec.line10`

- **IRS:** Taxable income for prior year (2024 Form 1040, line 15), as a negative amount when the sum of lines 12 and 13 was more than line 11
- **Encoded (Dollars):** Subtract helper "The amount on your 2024 Form 1040, line 14 (lines 12 and 13 added)" from helper "The amount on your 2024 Form 1040, line 11 (adjusted gross income)".
- Interpretation: amb.2025.rec_prior_taxable
- Expr: `{"from":"rec.agi_prior","op":"subtract","take":"rec.ded_prior"}`
- Cite: [p525] p. 27, Worksheet 2, line 10, "Taxable income for prior year"; footnote 4, "If taxable income is a negative amount, enter that amount in brackets"; p. 26, Negative taxable income, "the sum of lines 12 and 13, was more than line 11" (2025; sha256 39b0fa5e)

## (helper) — `rec.negative_ti`

- **Authored helper label:** The amount by which 2024 taxable income was negative (line 14 less line 11 of the 2024 Form 1040, zero if not more)
- **Encoded (NonNegDollars):** Subtract helper "The amount on your 2024 Form 1040, line 11 (adjusted gross income)" from helper "The amount on your 2024 Form 1040, line 14 (lines 12 and 13 added)". If zero or less, enter -0-.
- Expr: `{"from":"rec.ded_prior","op":"subtract_floor0","take":"rec.agi_prior"}`
- Cite: [p525] p. 25, Negative taxable income, "If your taxable income for the prior year (Worksheet 2, line 10) was a negative amount, the recovery you must include in income is reduced by that amount" (2025; sha256 39b0fa5e)

## (helper) — `rec.line11_negative`

- **Authored helper label:** Add lines 9 and 10 (line 10 negative), but not less than zero
- **Encoded (NonNegDollars):** Subtract helper "The amount by which 2024 taxable income was negative (line 14 less line 11 of the 2024 Form 1040, zero if not more)" from line 9. If zero or less, enter -0-.
- Expr: `{"from":"rec.line9","op":"subtract_floor0","take":"rec.negative_ti"}`
- Cite: [p525] p. 27, Worksheet 2, line 11, "add lines 9 and 10 and enter the result (but not less than zero)"; p. 26, Example 33, "You must include $50 in your 2025 income, rather than $250" (2025; sha256 39b0fa5e)

## (gate) — `rec.nol_negative`

- **Authored helper label:** Negative 2024 taxable income while a net operating loss is carried into 2025
- **Encoded (Bool):** helper "Was your 2024 taxable income (Form 1040, line 15) more than zero?" = false and helper "The amount by which 2024 taxable income was negative (line 14 less line 11 of the 2024 Form 1040, zero if not more)" > $0 and scope helper "Are you (or, on a joint return, your spouse) carrying a loss from an earlier year into 2025 as a 'net operating loss' deduction?" = true
- Expr: `{"all":[{"eq":["rec.ti_positive",{"const":false}],"op":"test"},{"gt":["rec.negative_ti",{"const":0}],"op":"test"},{"eq":["scope.nol",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [p525] p. 27, Worksheet 2, footnote 4, "Taxable income will have to be adjusted for any net operating loss carryover. For more information, see the Instructions for Form 172" (2025; sha256 39b0fa5e)

## 11 — `rec.line11`

- **IRS:** Amount to include in income for 2025: if line 10 is zero or more, the amount from line 9; if line 10 is a negative amount, lines 9 and 10 added (but not less than zero)
- **Encoded (NonNegDollars):** Choose — [helper "Was your 2024 taxable income (Form 1040, line 15) more than zero?" = true → line 9] [helper "Was your 2024 taxable income (Form 1040, line 15) more than zero?" = false → helper "Add lines 9 and 10 (line 10 negative), but not less than zero"]
- **Refusal:** when refund.exc_tax is true, cannot complete Pub. 525, Itemized Deduction Recoveries (Unused tax credits, Subject to AMT, Capital gains). Your 2024 alternative minimum tax, unused credits, 0% capital gain rate or sales tax choice means the 2024 tax is refigured to find how much of what was paid back is taxable; that is outside this tool. Cite: [p525] p. 27, Worksheet 2, "If you were subject to the AMT or your tax credits reduced your tax to zero, see Unused tax credits and Subject to AMT under Itemized Deduction Recoveries"; p. 25, Capital gains, "you’ll have to refigure your tax for the earlier year to determine if the recovery must be included in your income" (2025; sha256 39b0fa5e)
- **Refusal:** when refund.exc_who is true, cannot complete Pub. 525, Itemized Deduction Recoveries (Worksheet 2). A 2024 return on which you could be claimed as a dependent, a 2024 Form 1040-NR, or a refund from a joint state or local return with someone you are not filing jointly with for 2025 changes the 2024 standard deduction or the refund to count; that is outside this tool. Cite: [p525] p. 25, Itemized Deduction Recoveries, "You could be claimed as a dependent by someone else in 2024" and "You received a refund because of a jointly filed state or local income tax return"; p. 25, Nonresident aliens, "you can’t claim the standard deduction" (2025; sha256 39b0fa5e)
- **Refusal:** when rec.nol_negative is true, cannot complete Pub. 525, Worksheet 2, line 10, and Form 172 (a net operating loss carryover). Negative 2024 taxable income while a net operating loss is carried into 2025 must be adjusted for the carryover under the Instructions for Form 172; that is outside this tool. Cite: [p525] p. 27, Worksheet 2, footnote 4, "Taxable income will have to be adjusted for any net operating loss carryover" (2025; sha256 39b0fa5e)
- Expr: `{"alternatives":[{"guard":{"eq":["rec.ti_positive",{"const":true}],"op":"test"},"then":"rec.line9"},{"guard":{"eq":["rec.ti_positive",{"const":false}],"op":"test"},"then":"rec.line11_negative"}],"op":"choose"}`
- Cite: [p525] p. 27, Worksheet 2, line 11, "Amount to include in income for 2025: • If line 10 is zero or more, enter the amount from line 9" (2025; sha256 39b0fa5e)

## (helper) — `rec.line11_is_line3`

- **Authored helper label:** Line 11 equals line 3
- **Encoded (Bool):** line 11 = line 3
- Expr: `{"eq":["rec.line11","rec.line3"],"op":"test"}`
- Cite: [p525] p. 27, Worksheet 2, "If line 11 equals line 3: Enter the amount from line 1a on Schedule 1 (Form 1040), line 1" (2025; sha256 39b0fa5e)

## (helper) — `rec.line_b_share`

- **Authored helper label:** Divide line 1a by line 3 (line A) and multiply line 11 by that percentage
- **Encoded (NonNegDollars):** Divide line 1a by line 3, rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply line 11 by the result.
- Interpretation: amb.2025.rec_ratio_places
- Expr: `{"amount":"rec.line11","op":"prorate","part":"rec.line1a","places":6,"whole":"rec.line3"}`
- Cite: [p525] p. 27, Worksheet 2, line A, "Divide the amount on line 1a by the amount on line 3. Enter the percentage"; line B, "Multiply the amount on line 11 by the percentage on line A"; p. 25, Example 31, "$300 [($500 ÷ $2,500) × $1,500]" (2025; sha256 39b0fa5e)

## B — `rec.line_b`

- **IRS:** The amount for Schedule 1, line 1: line 1a when line 11 equals line 3; otherwise line 11 times line 1a divided by line 3 (all of line 11 when lines 1b and 2 are zero, none when line 1a is zero)
- **Encoded (NonNegDollars):** Choose — [helper "Line 11 equals line 3" = true → line 1a] [helper "Line 11 equals line 3" = false → helper "Divide line 1a by line 3 (line A) and multiply line 11 by that percentage"]
- Expr: `{"alternatives":[{"guard":{"eq":["rec.line11_is_line3",{"const":true}],"op":"test"},"then":"rec.line1a"},{"guard":{"eq":["rec.line11_is_line3",{"const":false}],"op":"test"},"then":"rec.line_b_share"}],"op":"choose"}`
- Cite: [p525] p. 27, Worksheet 2, "If line 11 is less than line 3 and either line 1a or line 1b or line 2 is zero: If there is an amount on line 1a, enter the amount from line 11 on Schedule 1 (Form 1040), line 1" and line B, "Enter the result here and on Schedule 1 (Form 1040), line 1" (2025; sha256 39b0fa5e)

## C — `rec.line_c`

- **IRS:** Subtract the amount on line B from the amount on line 11. Enter the result here and on Schedule 1 (Form 1040), line 8z
- **Encoded (NonNegDollars):** Subtract line B from line 11. If zero or less, enter -0-.
- Expr: `{"from":"rec.line11","op":"subtract_floor0","take":"rec.line_b"}`
- Cite: [p525] p. 27, Worksheet 2, line C, "Subtract the amount on line B from the amount on line 11. Enter the result here and on Schedule 1 (Form 1040), line 8z"; p. 25, Where to report, "the total of all other recoveries as other income on Schedule 1 (Form 1040), line 8z" (2025; sha256 39b0fa5e)

## (helper) — `rec.to_line1`

- **Authored helper label:** The taxable state or local income tax refund for Schedule 1, line 1, when Worksheet 2 is used
- **Encoded (NonNegDollars):** Choose — [helper "Worksheet 2 is used — money was paid back for 2024 and you itemized deductions for 2024" = true → line B] [helper "Worksheet 2 is used — money was paid back for 2024 and you itemized deductions for 2024" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["rec.path",{"const":true}],"op":"test"},"then":"rec.line_b"},{"guard":{"eq":["rec.path",{"const":false}],"op":"test"},"then":"rec.zero"}],"op":"choose"}`
- Cite: [p525] p. 25, Where to report, "Enter your state or local income tax refund on Schedule 1 (Form 1040), line 1" (2025; sha256 39b0fa5e)

## (helper) — `rec.to_line8z`

- **Authored helper label:** The taxable recoveries other than the state or local income tax refund, for Schedule 1, line 8z
- **Encoded (NonNegDollars):** Choose — [helper "Worksheet 2 is used — money was paid back for 2024 and you itemized deductions for 2024" = true → line C] [helper "Worksheet 2 is used — money was paid back for 2024 and you itemized deductions for 2024" = false → helper "Year parameter sales.zero"]
- **Refusal:** when rec.before_prior_year_if_any is true, cannot complete Pub. 525, Worksheet 2 (a recovery for an earlier year). Money paid back for something paid or deducted before 2024 is figured on a separate worksheet with that year's return; that is outside this tool. Cite: [p525] p. 27, Worksheet 2, "If you recovered amounts from more than 1 year, such as a state income tax refund from 2024 and a casualty loss reimbursement from 2023, complete a separate worksheet for each year" (2025; sha256 39b0fa5e)
- **Refusal:** when rec.nonitemized_if_any is true, cannot complete Pub. 525, Nonitemized Deduction Recoveries and Amounts Recovered for Credits. Money paid back for a deduction taken without itemizing (such as a bad debt) or for an item on which a credit was claimed is outside this tool. Cite: [p525] p. 28, Nonitemized Deduction Recoveries, "If you recover an amount that you deducted in an earlier year when you were figuring your AGI, you must generally include the full amount"; p. 28, Amounts Recovered for Credits (2025; sha256 39b0fa5e)
- **Refusal:** when rec.sales_tax_if_any is true, cannot complete Pub. 525, Worksheet 2, line 2 (a refund of general sales tax). A refund of general sales tax is limited by the sales tax and income tax you could have deducted for 2024; that is outside this tool. Cite: [p525] p. 27, Worksheet 2, footnote 2, "don’t enter more than the excess of your sales tax deduction over your state and local income tax you could have deducted" (2025; sha256 39b0fa5e)
- **Refusal:** when rec.two_returns_if_joint is true, cannot complete Pub. 525, Worksheet 2 (deductions on two 2024 returns). Amounts paid back for deductions on two 2024 returns, one for each of you, are tested against each 2024 return in turn; that is outside this tool. Cite: [p525] p. 27, Worksheet 2, "Use information from your tax return for the year the expense was deducted" (2025; sha256 39b0fa5e)
- Expr: `{"alternatives":[{"guard":{"eq":["rec.path",{"const":true}],"op":"test"},"then":"rec.line_c"},{"guard":{"eq":["rec.path",{"const":false}],"op":"test"},"then":"rec.zero"}],"op":"choose"}`
- Cite: [p525] p. 25, Where to report, "the total of all other recoveries as other income on Schedule 1 (Form 1040), line 8z"; i1040gi p. 92, Line 8z, "See Recoveries in Pub. 525 for details on how to figure the amount to report" (2025; sha256 39b0fa5e)
