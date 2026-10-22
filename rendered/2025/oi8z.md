# Schedule 1, line 8z — other income, one entry per item listed

- Document: `oi8z` (worksheet, tax year 2025)
- Collection: keyed entries; [i1040gi] p. 92, Line 8z, "List the type and amount of income. If necessary, include a statement showing the required information" (2025; printed date 2026-02-25; sha256 482e9c48)
- Note: One entry per item of other income listed on line 8z, each with its type (a kind from a fixed list, shown on the values sheet in place of the type written on the form) and its amount. Two kinds are computed, reemployment trade adjustment assistance (RTAA) payments and kickbacks; every other kind is refused at the entry.

## 8z (type) — `oi8z.kind`

- **Authored helper label:** Type of other income
- **Encoded (Enum(other_income_kind)):** Input — What kind of income is this line 8z item? rtaa (reemployment trade adjustment assistance (RTAA) payments from a state agency, shown in box 5 of Form 1099-G); kickbacks (kickbacks, side commissions, push money or similar payments you received; those from your self-employment activity go on Schedule C instead); insurance_dividends (dividends on insurance policies that are more than the total of all net premiums you paid for the contract); recovery (a reimbursement or other amount received for an item deducted in an earlier year, such as medical expenses, real estate taxes, general sales taxes or home mortgage interest; a state or local income tax refund belongs on line 1 instead); corrective_distribution (a loss on certain corrective distributions of excess deferrals); charitable_recapture (recapture of a charitable contribution deduction, for a fractional interest in tangible personal property or property the charity disposed of within 3 years); disaster_relief (the taxable part of disaster relief payments); education_distribution (taxable distributions from a Coverdell education savings account or a qualified tuition program); or other (any other taxable income for line 8z)
- Expr: `{"op":"input","source":"What kind of income is this line 8z item? rtaa (reemployment trade adjustment assistance (RTAA) payments from a state agency, shown in box 5 of Form 1099-G); kickbacks (kickbacks, side commissions, push money or similar payments you received; those from your self-employment activity go on Schedule C instead); insurance_dividends (dividends on insurance policies that are more than the total of all net premiums you paid for the contract); recovery (a reimbursement or other amount received for an item deducted in an earlier year, such as medical expenses, real estate taxes, general sales taxes or home mortgage interest; a state or local income tax refund belongs on line 1 instead); corrective_distribution (a loss on certain corrective distributions of excess deferrals); charitable_recapture (recapture of a charitable contribution deduction, for a fractional interest in tangible personal property or property the charity disposed of within 3 years); disaster_relief (the taxable part of disaster relief payments); education_distribution (taxable distributions from a Coverdell education savings account or a qualified tuition program); or other (any other taxable income for line 8z)"}`
- Cite: [i1040gi] p. 92, Line 8z, "Examples of income to report on line 8z include the following"; p525 p. 34, Kickbacks, "You must include kickbacks, side commissions, push money, or similar payments you receive in your income on Schedule 1 (Form 1040), line 8z; or on Schedule C (Form 1040) if from your self-employment activity" (2025; printed date 2026-02-25; sha256 482e9c48)

## 8z (amount) — `oi8z.amount`

- **Authored helper label:** Amount
- **Encoded (NonNegDollars):** Input — The amount of this item to include in income for 2025
- Expr: `{"op":"input","source":"The amount of this item to include in income for 2025"}`
- Cite: [i1040gi] p. 92, Line 8z, "List the type and amount of income" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `oi8z.recovery`

- **Authored helper label:** The item is a recovery of an amount deducted in an earlier year
- **Encoded (Bool):** line 8z (type) = 'recovery'
- Expr: `{"eq":["oi8z.kind",{"const":"recovery"}],"op":"test"}`
- Cite: [i1040gi] p. 92, Line 8z, "Reimbursements or other amounts received for items deducted in an earlier year" and "See Recoveries in Pub. 525 for details on how to figure the amount to report" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `oi8z.additional_tax`

- **Authored helper label:** The item carries an additional tax or interest (a charitable deduction recapture, or a taxable Coverdell ESA or qualified tuition program distribution)
- **Encoded (Bool):** (line 8z (type) = 'charitable_recapture' or line 8z (type) = 'education_distribution')
- Expr: `{"any":[{"eq":["oi8z.kind",{"const":"charitable_recapture"}],"op":"test"},{"eq":["oi8z.kind",{"const":"education_distribution"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 92, Line 8z, "Interest and an additional 10% tax apply to the amount of the recapture. See the instructions for Schedule 2, line 17g"; p. 93, Line 8z, "You may have to pay an additional tax if you received a taxable distribution from a Coverdell ESA or a QTP. See the Instructions for Form 5329" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `oi8z.figured`

- **Authored helper label:** The item's taxable amount is figured under rules this tool does not encode (a corrective distribution, disaster relief payments, insurance dividends, or any other kind)
- **Encoded (Bool):** (line 8z (type) = 'corrective_distribution' or line 8z (type) = 'disaster_relief' or line 8z (type) = 'insurance_dividends' or line 8z (type) = 'other')
- Interpretation: amb.2025.line8z_kinds
- Expr: `{"any":[{"eq":["oi8z.kind",{"const":"corrective_distribution"}],"op":"test"},{"eq":["oi8z.kind",{"const":"disaster_relief"}],"op":"test"},{"eq":["oi8z.kind",{"const":"insurance_dividends"}],"op":"test"},{"eq":["oi8z.kind",{"const":"other"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 92, Line 8z, "See Retirement Plan Contributions in Pub. 525" and "See Pub. 525 to figure the taxable part, if any" and "Dividends on insurance policies if they exceed the total of all net premiums you paid for the contract" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `oi8z.taxable`

- **Authored helper label:** The amount of this item included on line 8z
- **Encoded (NonNegDollars):** Enter the amount from line 8z (amount).
- **Refusal:** when oi8z.recovery is true, cannot complete Pub. 525, Recoveries (Schedule 1, line 8z). Figuring the taxable part of a recovery of an amount deducted in an earlier year is outside this tool. Cite: [i1040gi] p. 92, Line 8z, "See Recoveries in Pub. 525 for details on how to figure the amount to report" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when oi8z.additional_tax is true, cannot complete Schedule 2, line 17g, or Form 5329 (Schedule 1, line 8z). A charitable deduction recapture and taxable Coverdell ESA or qualified tuition program distributions, with their additional tax, are outside this tool. Cite: [i1040gi] p. 92, Line 8z, "See the instructions for Schedule 2, line 17g"; p. 93, Line 8z, "See the Instructions for Form 5329" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when oi8z.figured is true, cannot complete Pub. 525, Miscellaneous Income (Schedule 1, line 8z). Line 8z items other than RTAA payments and kickbacks are outside this tool. Cite: [i1040gi] p. 92, Line 8z, "For more details, see Miscellaneous Income in Pub. 525" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"from":"oi8z.amount","op":"copy"}`
- Cite: [i1040gi] p. 92, Line 8z, "List the type and amount of income" (2025; printed date 2026-02-25; sha256 482e9c48)
