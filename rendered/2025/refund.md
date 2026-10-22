# State and Local Income Tax Refund Worksheet—Schedule 1, Line 1

- Document: `refund` (form, tax year 2025)
- Note: The worksheet in the Form 1040 instructions, for a 2025 refund of 2024 state or local income tax deducted on the 2024 Schedule A. None of a refund is taxable when you did not itemize in 2024 or deducted general sales taxes instead of income taxes. The Pub. 525 exceptions, Form 1099-G box 8 and other recoveries are refused (Pub. 525 Worksheet 2 is not encoded).

## (helper) — `refund.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, "None of your refund is taxable" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.received`

- **Authored helper label:** State or local income tax refunds, credits or offsets you received in 2025
- **Encoded (NonNegDollars):** Input — State or local income tax refunds, credits or offsets you received in 2025: the total of box 2 of your Forms 1099-G (or a similar statement), including any part you chose to apply to your 2025 estimated state or local income tax and any part offset against a debt, and any refund for which you received no Form 1099-G; zero if none
- Expr: `{"op":"input","source":"State or local income tax refunds, credits or offsets you received in 2025: the total of box 2 of your Forms 1099-G (or a similar statement), including any part you chose to apply to your 2025 estimated state or local income tax and any part offset against a debt, and any refund for which you received no Form 1099-G; zero if none"}`
- Cite: [i1040gi] p. 88, Line 1, "If you received a refund, credit, or offset of state or local income taxes in 2025, you may be required to report this amount", "Report any taxable refund you received even if you didn’t receive Form 1099-G" and "If you chose to apply part or all of the refund to your 2025 estimated state or local income tax, the amount applied is treated as received in 2025"; f1099g p. 5, Instructions for Recipient, "Box 2. Shows refunds, credits, or offsets of state or local income tax you received" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.has`

- **Authored helper label:** Any state or local income tax refund received in 2025
- **Encoded (Bool):** helper "State or local income tax refunds, credits or offsets you received in 2025" > $0 (sales.zero)
- Expr: `{"gt":["refund.received",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 88, Line 1, "If you received a refund, credit, or offset of state or local income taxes in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `refund.box8`

- **Authored helper label:** Is box 8 ("If checked, box 2 is trade or business income") checked on any Form 1099-G that reports these refunds?
- **Encoded (Bool):** Input — Is box 8 ("If checked, box 2 is trade or business income") checked on any Form 1099-G that reports these refunds?
- Expr: `{"op":"input","source":"Is box 8 (\"If checked, box 2 is trade or business income\") checked on any Form 1099-G that reports these refunds?"}`
- Cite: [f1099g] p. 5, Instructions for Recipient, "Box 8. If this box is checked, the amount in box 2 is attributable to an income tax that applies exclusively to income from a trade or business" and "If taxable, report the amount in box 2 on Schedule C or F (Form 1040), as appropriate" (Rev. March 2024 (continuous-use form for calendar year 2025; the December 2026 revision is first used for 2026); sha256 fe46acb4)

## (gate) — `refund.not_2024`

- **Authored helper label:** Is any of these refunds for a tax year other than 2024 (box 3 of Form 1099-G), or did you make your last payment of 2024 estimated state or local income tax in 2025?
- **Encoded (Bool):** Input — Is any of these refunds for a tax year other than 2024 (box 3 of Form 1099-G), or did you make your last payment of 2024 estimated state or local income tax in 2025?
- Interpretation: amb.2025.refund_exceptions
- Expr: `{"op":"input","source":"Is any of these refunds for a tax year other than 2024 (box 3 of Form 1099-G), or did you make your last payment of 2024 estimated state or local income tax in 2025?"}`
- Cite: [i1040gi] p. 89, Line 1, "1. You received a refund in 2025 that is for a tax year other than 2024" and "5. You made your last payment of 2024 estimated state or local income tax in 2025"; f1099g p. 5, Instructions for Recipient, "Box 3. Identifies the tax year for which the box 2 refunds, credits, or offsets shown were made" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.itemized`

- **Authored helper label:** Did you itemize deductions on Schedule A for 2024?
- **Encoded (Bool):** Input — Did you itemize deductions on Schedule A for 2024?
- Expr: `{"op":"input","source":"Did you itemize deductions on Schedule A for 2024?"}`
- Cite: [i1040gi] p. 88, Line 1, "None of your refund is taxable if, in the year you paid the tax, ... you either (a) didn’t itemize deductions"; p525 p. 24, Deductions not itemized, "If you didn’t itemize deductions for the year for which you received the recovery of an expense that was deductible only if you itemized, don’t include any of the recovery amount in your income" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.sales`

- **Authored helper label:** On your 2024 Schedule A, did you deduct state and local general sales taxes instead of state and local income taxes (the box on line 5a checked)?
- **Encoded (Bool):** Input — On your 2024 Schedule A, did you deduct state and local general sales taxes instead of state and local income taxes (the box on line 5a checked)?
- Expr: `{"op":"input","source":"On your 2024 Schedule A, did you deduct state and local general sales taxes instead of state and local income taxes (the box on line 5a checked)?"}`
- Cite: [i1040gi] p. 88, Line 1, "or (b) elected to deduct state and local general sales taxes instead of state and local income taxes"; p525 p. 24, State tax refund, "Because you didn’t choose to deduct the state income tax, you don’t include the state income tax refund in income" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.worksheet`

- **Authored helper label:** You itemized deductions for 2024 and deducted state and local income taxes, so the worksheet is used
- **Encoded (Bool):** helper "Did you itemize deductions on Schedule A for 2024?" = true and helper "On your 2024 Schedule A, did you deduct state and local general sales taxes instead of state and local income taxes (the box on line 5a checked)?" = false
- Interpretation: amb.2025.refund_not_itemized
- Expr: `{"all":[{"eq":["refund.itemized",{"const":true}],"op":"test"},{"eq":["refund.sales",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 88, Line 1, "If the refund was for a tax you paid in 2024 and you deducted state and local income taxes on your 2024 Schedule A, use the State and Local Income Tax Refund Worksheet" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `refund.exc_tax`

- **Authored helper label:** For 2024: did you owe alternative minimum tax; were you unable to use the full amount of credits you were entitled to because the total credits were more than the amount on your 2024 Form 1040 or 1040-SR, line 18; did you have taxable income on your 2024 Form 1040 or 1040-SR, line 15, but no tax on line 16 because of the 0% tax rate on net capital gain and qualified dividends; or is your 2024 state and local income tax refund more than your 2024 state and local income tax deduction minus the amount you could have deducted as your 2024 state and local general sales taxes?
- **Encoded (Bool):** Input — For 2024: did you owe alternative minimum tax; were you unable to use the full amount of credits you were entitled to because the total credits were more than the amount on your 2024 Form 1040 or 1040-SR, line 18; did you have taxable income on your 2024 Form 1040 or 1040-SR, line 15, but no tax on line 16 because of the 0% tax rate on net capital gain and qualified dividends; or is your 2024 state and local income tax refund more than your 2024 state and local income tax deduction minus the amount you could have deducted as your 2024 state and local general sales taxes?
- Expr: `{"op":"input","source":"For 2024: did you owe alternative minimum tax; were you unable to use the full amount of credits you were entitled to because the total credits were more than the amount on your 2024 Form 1040 or 1040-SR, line 18; did you have taxable income on your 2024 Form 1040 or 1040-SR, line 15, but no tax on line 16 because of the 0% tax rate on net capital gain and qualified dividends; or is your 2024 state and local income tax refund more than your 2024 state and local income tax deduction minus the amount you could have deducted as your 2024 state and local general sales taxes?"}`
- Cite: [i1040gi] p. 89, Line 1, "3. You had taxable income on your 2024 Form 1040 or 1040-SR, line 15, but no tax on your Form 1040 or 1040-SR, line 16, because of the 0% tax rate on net capital gain and qualified dividends in certain situations", "4. Your 2024 state and local income tax refund is more than your 2024 state and local income tax deduction minus the amount you could have deducted as your 2024 state and local general sales taxes", "6. You owed alternative minimum tax in 2024" and "7. You couldn’t use the full amount of credits you were entitled to in 2024" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `refund.exc_who`

- **Authored helper label:** Could you be claimed as a dependent by someone else in 2024; were you a nonresident alien filing Form 1040-NR for 2024; or did you receive any of these refunds because of a jointly filed state or local income tax return when you are not filing a joint 2025 Form 1040 or 1040-SR with the same person?
- **Encoded (Bool):** Input — Could you be claimed as a dependent by someone else in 2024; were you a nonresident alien filing Form 1040-NR for 2024; or did you receive any of these refunds because of a jointly filed state or local income tax return when you are not filing a joint 2025 Form 1040 or 1040-SR with the same person?
- Interpretation: amb.2025.refund_exceptions
- Expr: `{"op":"input","source":"Could you be claimed as a dependent by someone else in 2024; were you a nonresident alien filing Form 1040-NR for 2024; or did you receive any of these refunds because of a jointly filed state or local income tax return when you are not filing a joint 2025 Form 1040 or 1040-SR with the same person?"}`
- Cite: [i1040gi] p. 89, Line 1, "8. You could be claimed as a dependent by someone else in 2024" and "9. You received a refund because of a jointly filed state or local income tax return, but you aren’t filing a joint 2025 Form 1040 or 1040-SR with the same person"; p525 p. 24, Itemized Deduction Recoveries, "You can’t use the State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, and must use this discussion if you’re a nonresident alien" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.line5d_2024`

- **Authored helper label:** The amount on your 2024 Schedule A, line 5d
- **Encoded (NonNegDollars):** Input — The amount on your 2024 Schedule A, line 5d (your state and local income or general sales taxes, real estate taxes and personal property taxes, added together)
- Interpretation: amb.2025.refund_paid_5d
- Expr: `{"op":"input","source":"The amount on your 2024 Schedule A, line 5d (your state and local income or general sales taxes, real estate taxes and personal property taxes, added together)"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 1, "your state and local income taxes shown on your 2024 Schedule A, line 5d", and line 2, "(generally, this is the amount reported on your 2024 Schedule A, line 5d)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.line5e_2024`

- **Authored helper label:** The amount on your 2024 Schedule A, line 5e
- **Encoded (NonNegDollars):** Input — The amount on your 2024 Schedule A, line 5e
- Expr: `{"op":"input","source":"The amount on your 2024 Schedule A, line 5e"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 2, "more than the amount on your 2024 Schedule A, line 5e" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `refund.line5e_bad`

- **Authored helper label:** The amount entered for 2024 Schedule A line 5e is more than the amount entered for line 5d
- **Encoded (Bool):** helper "The amount on your 2024 Schedule A, line 5e" > helper "The amount on your 2024 Schedule A, line 5d"
- Expr: `{"gt":["refund.line5e_2024","refund.line5d_2024"],"op":"test"}`
- Cite: [i1040sca] p. 7, Line 5e, "enter the smaller of line 5d or $40,000 ($20,000 if married filing separately)" (2025; printed date 2025-12-08; sha256 b0999b12)

## 1 — `refund.line1`

- **IRS:** Enter the income tax refund from Form(s) 1099-G (or similar statement). But don’t enter more than the amount of your state and local income taxes shown on your 2024 Schedule A, line 5d
- **Encoded (NonNegDollars):** Enter the smaller of helper "State or local income tax refunds, credits or offsets you received in 2025" or helper "The amount on your 2024 Schedule A, line 5d".
- **Refusal:** when refund.exc_tax is true, cannot complete Pub. 525, Itemized Deduction Recoveries (Worksheet 2). Your 2024 alternative minimum tax, unused credits, 0% capital gain rate or sales tax choice means the refund is figured with Pub. 525 instead of the Form 1040 worksheet; that is outside this tool. Cite: [i1040gi] pp. 88–89, Line 1, "Exception. See Itemized Deduction Recoveries in Pub. 525 instead of using the State and Local Income Tax Refund Worksheet in these instructions if any of the following applies", items 3, 4, 6 and 7 (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when refund.exc_who is true, cannot complete Pub. 525, Itemized Deduction Recoveries (Worksheet 2). A 2024 return on which you could be claimed as a dependent, a 2024 Form 1040-NR, or a refund from a joint state or local return with someone you are not filing jointly with for 2025 is figured with Pub. 525 instead of the Form 1040 worksheet; that is outside this tool. Cite: [i1040gi] pp. 88–89, Line 1, "Exception. See Itemized Deduction Recoveries in Pub. 525 instead of using the State and Local Income Tax Refund Worksheet in these instructions if any of the following applies", items 8 and 9; p525 p. 24, Itemized Deduction Recoveries, "if you’re a nonresident alien" (2025; printed date 2026-02-25; sha256 482e9c48)
- Interpretation: amb.2025.refund_cap_5d
- Expr: `{"of":["refund.received","refund.line5d_2024"],"op":"smaller_of"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 1, "Enter the income tax refund from Form(s) 1099-G (or similar statement). But don’t enter more than the amount of your state and local income taxes shown on your 2024 Schedule A, line 5d" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.line2_more`

- **Authored helper label:** Is the amount of state and local income taxes (or general sales taxes), real estate taxes, and personal property taxes paid in 2024 (generally, this is the amount reported on your 2024 Schedule A, line 5d) more than the amount on your 2024 Schedule A, line 5e?
- **Encoded (Bool):** helper "The amount on your 2024 Schedule A, line 5d" > helper "The amount on your 2024 Schedule A, line 5e"
- Expr: `{"gt":["refund.line5d_2024","refund.line5e_2024"],"op":"test"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 2, "Is the amount of state and local income taxes (or general sales taxes), real estate taxes, and personal property taxes paid in 2024" (2025; printed date 2026-02-25; sha256 482e9c48)

## 2 — `refund.line2`

- **IRS:** Subtract the amount on your 2024 Schedule A, line 5e, from the amount of state and local income taxes (or general sales taxes), real estate taxes, and personal property taxes paid in 2024 (generally, this is the amount reported on your 2024 Schedule A, line 5d)
- **Encoded (NonNegDollars):** Subtract helper "The amount on your 2024 Schedule A, line 5e" from helper "The amount on your 2024 Schedule A, line 5d". If zero or less, enter -0-.
- **Refusal:** when refund.line5e_bad is true, cannot complete State and Local Income Tax Refund Worksheet, line 2 (2024 Schedule A lines 5d and 5e). The amount on 2024 Schedule A line 5e cannot be more than line 5d, since line 5e is the smaller of line 5d and the limit. Check both amounts against your 2024 Schedule A. Cite: [i1040sca] p. 7, Line 5e, "enter the smaller of line 5d or $40,000 ($20,000 if married filing separately)" (2025; printed date 2025-12-08; sha256 b0999b12)
- Expr: `{"from":"refund.line5d_2024","op":"subtract_floor0","take":"refund.line5e_2024"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 2, "No. Enter the amount from line 1 on line 3 and go to line 4. Yes. Subtract the amount on your 2024 Schedule A, line 5e" (zero on No, so that line 3 is line 1) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.line3_more`

- **Authored helper label:** Is the amount on line 1 more than the amount on line 2?
- **Encoded (Bool):** line 1 > line 2
- Expr: `{"gt":["refund.line1","refund.line2"],"op":"test"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 3, "Is the amount on line 1 more than the amount on line 2?" and "No. STOP None of your refund is taxable" (2025; printed date 2026-02-25; sha256 482e9c48)

## 3 — `refund.line3`

- **IRS:** Subtract line 2 from line 1
- **Encoded (NonNegDollars):** Subtract line 2 from line 1. If zero or less, enter -0-.
- Expr: `{"from":"refund.line1","op":"subtract_floor0","take":"refund.line2"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 3, "Yes. Subtract line 2 from line 1" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.line17_2024`

- **Authored helper label:** Your total itemized deductions from your 2024 Schedule A, line 17
- **Encoded (NonNegDollars):** Input — Your total itemized deductions from your 2024 Schedule A, line 17
- Expr: `{"op":"input","source":"Your total itemized deductions from your 2024 Schedule A, line 17"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 4, "Enter your total itemized deductions from your 2024 Schedule A, line 17" (2025; printed date 2026-02-25; sha256 482e9c48)

## 4 — `refund.line4`

- **IRS:** Enter your total itemized deductions from your 2024 Schedule A, line 17
- **Encoded (NonNegDollars):** Enter the amount from helper "Your total itemized deductions from your 2024 Schedule A, line 17".
- Expr: `{"from":"refund.line17_2024","op":"copy"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.status`

- **Authored helper label:** The filing status claimed on your 2024 Form 1040 or 1040-SR
- **Encoded (Enum(filing_status)):** Input — The filing status claimed on your 2024 Form 1040 or 1040-SR
- Expr: `{"op":"input","source":"The filing status claimed on your 2024 Form 1040 or 1040-SR"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 5, "Enter the amount shown below for the filing status claimed on your 2024 Form 1040 or 1040-SR" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.mfs_spouse_itemized`

- **Authored helper label:** Did your spouse itemize deductions in 2024?
- **Encoded (Bool):** Input — Did your spouse itemize deductions in 2024?
- Expr: `{"op":"input","source":"Did your spouse itemize deductions in 2024?"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, Note, "If the filing status on your 2024 Form 1040 or 1040-SR was married filing separately and your spouse itemized deductions in 2024" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.std_single`

- **Authored helper label:** Year parameter refund.std_single ($14,600)
- **Encoded (NonNegDollars):** Enter $14,600 (refund.std_single).
- Expr: `{"op":"param","ref":"refund.std_single"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 5, "Single or married filing separately—$14,600" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.std_joint`

- **Authored helper label:** Year parameter refund.std_joint ($29,200)
- **Encoded (NonNegDollars):** Enter $29,200 (refund.std_joint).
- Expr: `{"op":"param","ref":"refund.std_joint"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 5, "Married filing jointly or qualifying surviving spouse—$29,200" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.std_hoh`

- **Authored helper label:** Year parameter refund.std_hoh ($21,900)
- **Encoded (NonNegDollars):** Enter $21,900 (refund.std_hoh).
- Expr: `{"op":"param","ref":"refund.std_hoh"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 5, "Head of household—$21,900" (2025; printed date 2026-02-25; sha256 482e9c48)

## 5 — `refund.line5`

- **IRS:** Enter the amount shown below for the filing status claimed on your 2024 Form 1040 or 1040-SR. Single or married filing separately—$14,600. Married filing jointly or qualifying surviving spouse—$29,200. Head of household—$21,900
- **Encoded (NonNegDollars):** Choose — [helper "The filing status claimed on your 2024 Form 1040 or 1040-SR" = 'single' → helper "Year parameter refund.std_single ($14,600)"] [helper "The filing status claimed on your 2024 Form 1040 or 1040-SR" = 'mfj' → helper "Year parameter refund.std_joint ($29,200)"] [helper "The filing status claimed on your 2024 Form 1040 or 1040-SR" = 'mfs' → helper "Year parameter refund.std_single ($14,600)"] [helper "The filing status claimed on your 2024 Form 1040 or 1040-SR" = 'hoh' → helper "Year parameter refund.std_hoh ($21,900)"] [helper "The filing status claimed on your 2024 Form 1040 or 1040-SR" = 'qss' → helper "Year parameter refund.std_joint ($29,200)"]
- Expr: `{"alternatives":[{"guard":{"eq":["refund.status",{"const":"single"}],"op":"test"},"then":"refund.std_single"},{"guard":{"eq":["refund.status",{"const":"mfj"}],"op":"test"},"then":"refund.std_joint"},{"guard":{"eq":["refund.status",{"const":"mfs"}],"op":"test"},"then":"refund.std_single"},{"guard":{"eq":["refund.status",{"const":"hoh"}],"op":"test"},"then":"refund.std_hoh"},{"guard":{"eq":["refund.status",{"const":"qss"}],"op":"test"},"then":"refund.std_joint"}],"op":"choose"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.box_married`

- **Authored helper label:** Year parameter refund.box_married ($1,550)
- **Encoded (NonNegDollars):** Enter $1,550 (refund.box_married).
- Expr: `{"op":"param","ref":"refund.box_married"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 6, "Multiply the number of boxes checked by $1,550" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.box_unmarried`

- **Authored helper label:** Year parameter refund.box_unmarried ($1,950)
- **Encoded (NonNegDollars):** Enter $1,950 (refund.box_unmarried).
- Expr: `{"op":"param","ref":"refund.box_unmarried"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 6, "($1,950 if your 2024 filing status was single or head of household)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.per_box`

- **Authored helper label:** The amount for each box checked, $1,550 ($1,950 if your 2024 filing status was single or head of household)
- **Encoded (NonNegDollars):** Choose — [helper "The filing status claimed on your 2024 Form 1040 or 1040-SR" = 'single' → helper "Year parameter refund.box_unmarried ($1,950)"] [helper "The filing status claimed on your 2024 Form 1040 or 1040-SR" = 'mfj' → helper "Year parameter refund.box_married ($1,550)"] [helper "The filing status claimed on your 2024 Form 1040 or 1040-SR" = 'mfs' → helper "Year parameter refund.box_married ($1,550)"] [helper "The filing status claimed on your 2024 Form 1040 or 1040-SR" = 'hoh' → helper "Year parameter refund.box_unmarried ($1,950)"] [helper "The filing status claimed on your 2024 Form 1040 or 1040-SR" = 'qss' → helper "Year parameter refund.box_married ($1,550)"]
- Expr: `{"alternatives":[{"guard":{"eq":["refund.status",{"const":"single"}],"op":"test"},"then":"refund.box_unmarried"},{"guard":{"eq":["refund.status",{"const":"mfj"}],"op":"test"},"then":"refund.box_married"},{"guard":{"eq":["refund.status",{"const":"mfs"}],"op":"test"},"then":"refund.box_married"},{"guard":{"eq":["refund.status",{"const":"hoh"}],"op":"test"},"then":"refund.box_unmarried"},{"guard":{"eq":["refund.status",{"const":"qss"}],"op":"test"},"then":"refund.box_married"}],"op":"choose"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 6, "Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.you_born`

- **Authored helper label:** Were you born before January 2, 1960?
- **Encoded (Bool):** Input — Were you born before January 2, 1960?
- Interpretation: amb.2025.refund_boxes_2024
- Expr: `{"op":"input","source":"Were you born before January 2, 1960?"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 6, "You were born before January 2, 1960" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.you_blind`

- **Authored helper label:** Were you blind at the end of 2024?
- **Encoded (Bool):** Input — Were you blind at the end of 2024?
- Interpretation: amb.2025.refund_boxes_2024
- Expr: `{"op":"input","source":"Were you blind at the end of 2024?"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 6, "You are blind" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.spouse_born`

- **Authored helper label:** Was the spouse on your 2024 return born before January 2, 1960? If your 2024 filing status was married filing separately, answer yes only if your spouse also had no income, wasn't filing a return, and couldn't be claimed as a dependent on another person's return.
- **Encoded (Bool):** Input — Was the spouse on your 2024 return born before January 2, 1960? If your 2024 filing status was married filing separately, answer yes only if your spouse also had no income, wasn't filing a return, and couldn't be claimed as a dependent on another person's return.
- Interpretation: amb.2025.refund_boxes_2024
- Expr: `{"op":"input","source":"Was the spouse on your 2024 return born before January 2, 1960? If your 2024 filing status was married filing separately, answer yes only if your spouse also had no income, wasn't filing a return, and couldn't be claimed as a dependent on another person's return."}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 6, "Spouse was born before January 2, 1960" and "If your filing status is married filing separately, you can check the boxes for your spouse only if your spouse had no income, isn’t filing a return, and can’t be claimed as a dependent on another person’s return" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.spouse_blind`

- **Authored helper label:** Was the spouse on your 2024 return blind at the end of 2024? If your 2024 filing status was married filing separately, answer yes only if your spouse also had no income, wasn't filing a return, and couldn't be claimed as a dependent on another person's return.
- **Encoded (Bool):** Input — Was the spouse on your 2024 return blind at the end of 2024? If your 2024 filing status was married filing separately, answer yes only if your spouse also had no income, wasn't filing a return, and couldn't be claimed as a dependent on another person's return.
- Interpretation: amb.2025.refund_boxes_2024
- Expr: `{"op":"input","source":"Was the spouse on your 2024 return blind at the end of 2024? If your 2024 filing status was married filing separately, answer yes only if your spouse also had no income, wasn't filing a return, and couldn't be claimed as a dependent on another person's return."}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 6, "Spouse is blind" and "If your filing status is married filing separately, you can check the boxes for your spouse only if your spouse had no income, isn’t filing a return, and can’t be claimed as a dependent on another person’s return" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.spouse_boxes`

- **Authored helper label:** Your 2024 filing status was married filing jointly or married filing separately (the spouse boxes can apply)
- **Encoded (Bool):** (helper "The filing status claimed on your 2024 Form 1040 or 1040-SR" = 'mfj' or helper "The filing status claimed on your 2024 Form 1040 or 1040-SR" = 'mfs')
- Interpretation: amb.2025.refund_boxes_2024
- Expr: `{"any":[{"eq":["refund.status",{"const":"mfj"}],"op":"test"},{"eq":["refund.status",{"const":"mfs"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 6, "If your filing status is married filing separately, you can check the boxes for your spouse only if"; p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return)" and "Don’t check any boxes for your spouse if your filing status is head of household" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.amt_you_born`

- **Authored helper label:** The amount for the box "You were born before January 2, 1960" (zero if not checked)
- **Encoded (NonNegDollars):** Choose — [helper "Were you born before January 2, 1960?" = true → helper "The amount for each box checked, $1,550 ($1,950 if your 2024 filing status was single or head of household)"] [helper "Were you born before January 2, 1960?" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["refund.you_born",{"const":true}],"op":"test"},"then":"refund.per_box"},{"guard":{"eq":["refund.you_born",{"const":false}],"op":"test"},"then":"refund.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 6, "Multiply the number of boxes checked by $1,550" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.amt_you_blind`

- **Authored helper label:** The amount for the box "You are blind" (zero if not checked)
- **Encoded (NonNegDollars):** Choose — [helper "Were you blind at the end of 2024?" = true → helper "The amount for each box checked, $1,550 ($1,950 if your 2024 filing status was single or head of household)"] [helper "Were you blind at the end of 2024?" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["refund.you_blind",{"const":true}],"op":"test"},"then":"refund.per_box"},{"guard":{"eq":["refund.you_blind",{"const":false}],"op":"test"},"then":"refund.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 6, "Multiply the number of boxes checked by $1,550" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.amt_spouse_born`

- **Authored helper label:** The amount for the box "Spouse was born before January 2, 1960" (zero if not checked, and when your 2024 filing status was not married filing jointly or married filing separately)
- **Encoded (NonNegDollars):** Choose — [helper "Your 2024 filing status was married filing jointly or married filing separately (the spouse boxes can apply)" = false → helper "Year parameter sales.zero"] [helper "Your 2024 filing status was married filing jointly or married filing separately (the spouse boxes can apply)" = true → helper "The amount for the box "Spouse was born before January 2, 1960" when the spouse boxes can apply (zero if not checked)"]
- Interpretation: amb.2025.refund_boxes_2024
- Expr: `{"alternatives":[{"guard":{"eq":["refund.spouse_boxes",{"const":false}],"op":"test"},"then":"refund.zero"},{"guard":{"eq":["refund.spouse_boxes",{"const":true}],"op":"test"},"then":"refund.amt_spouse_born_checked"}],"op":"choose"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 6, "Multiply the number of boxes checked by $1,550" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.amt_spouse_born_checked`

- **Authored helper label:** The amount for the box "Spouse was born before January 2, 1960" when the spouse boxes can apply (zero if not checked)
- **Encoded (NonNegDollars):** Choose — [helper "Was the spouse on your 2024 return born before January 2, 1960? If your 2024 filing status was married filing separately, answer yes only if your spouse also had no income, wasn't filing a return, and couldn't be claimed as a dependent on another person's return." = true → helper "The amount for each box checked, $1,550 ($1,950 if your 2024 filing status was single or head of household)"] [helper "Was the spouse on your 2024 return born before January 2, 1960? If your 2024 filing status was married filing separately, answer yes only if your spouse also had no income, wasn't filing a return, and couldn't be claimed as a dependent on another person's return." = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["refund.spouse_born",{"const":true}],"op":"test"},"then":"refund.per_box"},{"guard":{"eq":["refund.spouse_born",{"const":false}],"op":"test"},"then":"refund.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 6, "Multiply the number of boxes checked by $1,550" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.amt_spouse_blind`

- **Authored helper label:** The amount for the box "Spouse is blind" (zero if not checked, and when your 2024 filing status was not married filing jointly or married filing separately)
- **Encoded (NonNegDollars):** Choose — [helper "Your 2024 filing status was married filing jointly or married filing separately (the spouse boxes can apply)" = false → helper "Year parameter sales.zero"] [helper "Your 2024 filing status was married filing jointly or married filing separately (the spouse boxes can apply)" = true → helper "The amount for the box "Spouse is blind" when the spouse boxes can apply (zero if not checked)"]
- Interpretation: amb.2025.refund_boxes_2024
- Expr: `{"alternatives":[{"guard":{"eq":["refund.spouse_boxes",{"const":false}],"op":"test"},"then":"refund.zero"},{"guard":{"eq":["refund.spouse_boxes",{"const":true}],"op":"test"},"then":"refund.amt_spouse_blind_checked"}],"op":"choose"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 6, "Multiply the number of boxes checked by $1,550" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.amt_spouse_blind_checked`

- **Authored helper label:** The amount for the box "Spouse is blind" when the spouse boxes can apply (zero if not checked)
- **Encoded (NonNegDollars):** Choose — [helper "Was the spouse on your 2024 return blind at the end of 2024? If your 2024 filing status was married filing separately, answer yes only if your spouse also had no income, wasn't filing a return, and couldn't be claimed as a dependent on another person's return." = true → helper "The amount for each box checked, $1,550 ($1,950 if your 2024 filing status was single or head of household)"] [helper "Was the spouse on your 2024 return blind at the end of 2024? If your 2024 filing status was married filing separately, answer yes only if your spouse also had no income, wasn't filing a return, and couldn't be claimed as a dependent on another person's return." = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["refund.spouse_blind",{"const":true}],"op":"test"},"then":"refund.per_box"},{"guard":{"eq":["refund.spouse_blind",{"const":false}],"op":"test"},"then":"refund.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 6, "Multiply the number of boxes checked by $1,550" (2025; printed date 2026-02-25; sha256 482e9c48)

## 6 — `refund.line6`

- **IRS:** Check any boxes that apply. Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household). No boxes checked, enter -0-
- **Encoded (NonNegDollars):** Add helper "The amount for the box "You were born before January 2, 1960" (zero if not checked)", helper "The amount for the box "You are blind" (zero if not checked)", helper "The amount for the box "Spouse was born before January 2, 1960" (zero if not checked, and when your 2024 filing status was not married filing jointly or married filing separately)", and helper "The amount for the box "Spouse is blind" (zero if not checked, and when your 2024 filing status was not married filing jointly or married filing separately)".
- Expr: `{"of":["refund.amt_you_born","refund.amt_you_blind","refund.amt_spouse_born","refund.amt_spouse_blind"],"op":"sum"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 6, "Check any boxes that apply" and "No boxes checked. Enter -0-" (the amount for each box checked, added; the same as the number of boxes times the amount) (2025; printed date 2026-02-25; sha256 482e9c48)

## 7 — `refund.line7`

- **IRS:** Add lines 5 and 6
- **Encoded (NonNegDollars):** Add line 5 and line 6.
- Expr: `{"of":["refund.line5","refund.line6"],"op":"sum"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 7, "Add lines 5 and 6" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.line8_figured`

- **Authored helper label:** Is the amount on line 7 less than the amount on line 4? Subtract line 7 from line 4 (zero if not)
- **Encoded (NonNegDollars):** Subtract line 7 from line 4. If zero or less, enter -0-.
- Expr: `{"from":"refund.line4","op":"subtract_floor0","take":"refund.line7"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 8, "Is the amount on line 7 less than the amount on line 4?", "No. STOP None of your refund is taxable" and "Yes. Subtract line 7 from line 4" (2025; printed date 2026-02-25; sha256 482e9c48)

## 8 — `refund.line8`

- **IRS:** Subtract line 7 from line 4 (if your 2024 filing status was married filing separately and your spouse itemized deductions in 2024, the amount from line 4)
- **Encoded (NonNegDollars):** Choose — [helper "The filing status claimed on your 2024 Form 1040 or 1040-SR" = 'single' → helper "Is the amount on line 7 less than the amount on line 4? Subtract line 7 from line 4 (zero if not)"] [helper "The filing status claimed on your 2024 Form 1040 or 1040-SR" = 'mfj' → helper "Is the amount on line 7 less than the amount on line 4? Subtract line 7 from line 4 (zero if not)"] [helper "The filing status claimed on your 2024 Form 1040 or 1040-SR" = 'mfs' → helper "Married filing separately in 2024: the amount from line 4 if your spouse itemized deductions in 2024 (lines 5 through 7 skipped), otherwise line 4 less line 7"] [helper "The filing status claimed on your 2024 Form 1040 or 1040-SR" = 'hoh' → helper "Is the amount on line 7 less than the amount on line 4? Subtract line 7 from line 4 (zero if not)"] [helper "The filing status claimed on your 2024 Form 1040 or 1040-SR" = 'qss' → helper "Is the amount on line 7 less than the amount on line 4? Subtract line 7 from line 4 (zero if not)"]
- Expr: `{"alternatives":[{"guard":{"eq":["refund.status",{"const":"single"}],"op":"test"},"then":"refund.line8_figured"},{"guard":{"eq":["refund.status",{"const":"mfj"}],"op":"test"},"then":"refund.line8_figured"},{"guard":{"eq":["refund.status",{"const":"mfs"}],"op":"test"},"then":"refund.line8_mfs"},{"guard":{"eq":["refund.status",{"const":"hoh"}],"op":"test"},"then":"refund.line8_figured"},{"guard":{"eq":["refund.status",{"const":"qss"}],"op":"test"},"then":"refund.line8_figured"}],"op":"choose"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 8; Note, "skip lines 5 through 7, enter the amount from line 4 on line 8, and go to line 9" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.line8_mfs`

- **Authored helper label:** Married filing separately in 2024: the amount from line 4 if your spouse itemized deductions in 2024 (lines 5 through 7 skipped), otherwise line 4 less line 7
- **Encoded (NonNegDollars):** Choose — [helper "Did your spouse itemize deductions in 2024?" = true → line 4] [helper "Did your spouse itemize deductions in 2024?" = false → helper "Is the amount on line 7 less than the amount on line 4? Subtract line 7 from line 4 (zero if not)"]
- Expr: `{"alternatives":[{"guard":{"eq":["refund.mfs_spouse_itemized",{"const":true}],"op":"test"},"then":"refund.line4"},{"guard":{"eq":["refund.mfs_spouse_itemized",{"const":false}],"op":"test"},"then":"refund.line8_figured"}],"op":"choose"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, Note, "If the filing status on your 2024 Form 1040 or 1040-SR was married filing separately and your spouse itemized deductions in 2024, skip lines 5 through 7, enter the amount from line 4 on line 8, and go to line 9" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.line9_figured`

- **Authored helper label:** The smaller of line 3 or line 8
- **Encoded (NonNegDollars):** Enter the smaller of line 3 or line 8.
- Expr: `{"of":["refund.line3","refund.line8"],"op":"smaller_of"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 9, "Enter the smaller of line 3 or line 8" (2025; printed date 2026-02-25; sha256 482e9c48)

## 9 — `refund.line9`

- **IRS:** Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on Schedule 1, line 1
- **Encoded (NonNegDollars):** Choose — [helper "Is the amount on line 1 more than the amount on line 2?" = false → helper "Year parameter sales.zero"] [helper "Is the amount on line 1 more than the amount on line 2?" = true → helper "The smaller of line 3 or line 8"]
- Expr: `{"alternatives":[{"guard":{"eq":["refund.line3_more",{"const":false}],"op":"test"},"then":"refund.zero"},{"guard":{"eq":["refund.line3_more",{"const":true}],"op":"test"},"then":"refund.line9_figured"}],"op":"choose"}`
- Cite: [i1040gi] p. 90, State and Local Income Tax Refund Worksheet—Schedule 1, Line 1, line 9, "Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on Schedule 1, line 1"; line 3, "No. STOP None of your refund is taxable" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `refund.taxable`

- **Authored helper label:** Taxable part of your refund (zero when you did not itemize for 2024 or deducted general sales taxes)
- **Encoded (NonNegDollars):** Choose — [helper "You itemized deductions for 2024 and deducted state and local income taxes, so the worksheet is used" = false → helper "Year parameter sales.zero"] [helper "You itemized deductions for 2024 and deducted state and local income taxes, so the worksheet is used" = true → line 9]
- **Refusal:** when refund.box8 is true, cannot complete Form 1099-G box 8 (a refund of a tax on trade or business income, Schedule C or F). A refund of an income tax that applies only to trade or business income is reported, if taxable, on Schedule C or F; that is outside this tool. Cite: [f1099g] p. 5, Instructions for Recipient, "Box 8. If this box is checked, the amount in box 2 is attributable to an income tax that applies exclusively to income from a trade or business" (Rev. March 2024 (continuous-use form for calendar year 2025; the December 2026 revision is first used for 2026); sha256 fe46acb4)
- **Refusal:** when refund.not_2024 is true, cannot complete Pub. 525, Itemized Deduction Recoveries (Worksheet 2). A refund for a tax year other than 2024, or a refund when your last 2024 estimated state or local tax payment was made in 2025, is figured with Pub. 525 (and may reduce your 2025 deduction for taxes); that is outside this tool. Cite: [i1040gi] pp. 88–89, Line 1, "Exception. See Itemized Deduction Recoveries in Pub. 525 instead of using the State and Local Income Tax Refund Worksheet in these instructions if any of the following applies", items 1 and 5; p525 p. 24, Recovery for 2 or more years, "you must allocate, on a pro rata basis, the recovered amount between the years in which you paid it" (2025; printed date 2026-02-25; sha256 482e9c48)
- Interpretation: amb.2025.refund_not_itemized
- Expr: `{"alternatives":[{"guard":{"eq":["refund.worksheet",{"const":false}],"op":"test"},"then":"refund.zero"},{"guard":{"eq":["refund.worksheet",{"const":true}],"op":"test"},"then":"refund.line9"}],"op":"choose"}`
- Cite: [i1040gi] p. 88, Line 1, "None of your refund is taxable if, in the year you paid the tax, ... you either (a) didn’t itemize deductions, or (b) elected to deduct state and local general sales taxes instead of state and local income taxes" (2025; printed date 2026-02-25; sha256 482e9c48)
