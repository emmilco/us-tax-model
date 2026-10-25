# Form 2441, Part I — persons or organizations who provided the care, one entry per care provider

- Document: `dcprov` (worksheet, tax year 2025)
- Collection: keyed entries; [i2441] p. 2, Line 1, "Complete columns (a) through (e) for each person or organization that provided the care" (2025; sha256 86f0669e)
- Note: One entry per care provider. The provider's name and address (columns (a) and (b)) are written on the form by the filer and are not modelled; the identifying number is modelled by its kind, the household-employee box and the amount paid as given. A provider who is an ineligible related person is refused.

## (helper) — `dcprov.one`

- **Authored helper label:** One care provider
- **Encoded (Count):** Enter 1 (dc.one).
- Expr: `{"op":"param","ref":"dc.one"}`
- Cite: [i2441] p. 2, Line 1, "Complete columns (a) through (e) for each person or organization that provided the care" (2025; sha256 86f0669e)

## 1(c) — `dcprov.tin_kind`

- **Authored helper label:** Identifying number (SSN or EIN)
- **Encoded (Enum(dc_tin_kind)):** Input — What do you enter in column (c), the provider's identifying number? tin (you have the provider's SSN, ITIN or EIN and enter it), tax_exempt (a tax-exempt organization: enter "Tax-Exempt"), lafcp (you live abroad and the foreign provider has no U.S. taxpayer identification number and is not required to get one: enter "LAFCP"), see_statement (the provider did not give you the information: enter "See Attached Statement" and attach a statement saying so), or employer (your employer furnished the care under its dependent care plan: enter "See W-2" in column (b), leave column (c) blank and enter -0- in column (e))
- Expr: `{"op":"input","source":"What do you enter in column (c), the provider's identifying number? tin (you have the provider's SSN, ITIN or EIN and enter it), tax_exempt (a tax-exempt organization: enter \"Tax-Exempt\"), lafcp (you live abroad and the foreign provider has no U.S. taxpayer identification number and is not required to get one: enter \"LAFCP\"), see_statement (the provider did not give you the information: enter \"See Attached Statement\" and attach a statement saying so), or employer (your employer furnished the care under its dependent care plan: enter \"See W-2\" in column (b), leave column (c) blank and enter -0- in column (e))"}`
- Cite: [i2441] p. 3, Column (c), "If the care provider is an individual, enter their SSN or individual taxpayer identification number (ITIN). Otherwise, enter the provider's employer identification number (EIN)"; p. 3, Due Diligence, "Enter “See Attached Statement” in the columns for which you don't have the information. Then, attach a statement to your return explaining that the provider didn't give you the information you requested"; p. 3, Columns (a) and (b), "enter “See W-2” in column (b), leave column (c) blank, check the “No” box in column (d), and enter -0- in column (e)"; p. 3, U.S. citizens and resident aliens living abroad, "may not have, and may not be required to get, a U.S. taxpayer identification number" (2025; sha256 86f0669e)

## 1(d) — `dcprov.household`

- **Authored helper label:** Was the care provider your household employee in 2025?
- **Encoded (Bool):** Input — Was this care provider your household employee in 2025? (Someone you pay to care for your dependent or spouse in your home, controlling not only what work is done but how it is done, is probably a household employee; nannies generally are, daycare centers are not.)
- Expr: `{"op":"input","source":"Was this care provider your household employee in 2025? (Someone you pay to care for your dependent or spouse in your home, controlling not only what work is done but how it is done, is probably a household employee; nannies generally are, daycare centers are not.)"}`
- Cite: [i2441] p. 3, Column (d), "You must check either the "Yes" or "No" box in column (d) to indicate whether or not the care provider listed in column (a) was your household employee during the year" and "For example, nannies are generally household employees, while daycare centers are not" (2025; sha256 86f0669e)

## 1(e) — `dcprov.paid`

- **Authored helper label:** Amount paid
- **Encoded (NonNegDollars):** Input — The total amount you actually paid this provider in 2025, including amounts your employer paid to the provider on your behalf, whenever the care was provided and without reducing it by any reimbursement; zero if your employer furnished the care
- Expr: `{"op":"input","source":"The total amount you actually paid this provider in 2025, including amounts your employer paid to the provider on your behalf, whenever the care was provided and without reducing it by any reimbursement; zero if your employer furnished the care"}`
- Cite: [i2441] p. 3, Column (e), "Enter the total amount you actually paid in 2025 to the care provider. Also, include amounts your employer paid to a third party on your behalf. It doesn't matter when the expenses were incurred. Don't reduce this amount by any reimbursement you received" (2025; sha256 86f0669e)

## (helper) — `dcprov.related`

- **Authored helper label:** Was the provider a person to whom payments do not count (a person you or your spouse can claim as a dependent, your child under 19 at the end of 2025, a person who was your spouse at any time in 2025, or the parent of your qualifying child under 13)?
- **Encoded (Bool):** Input — Was this provider any of these: a person you (or your spouse, if filing jointly) can claim as a dependent; your child (including a stepchild or foster child) who was under age 19 at the end of 2025, even if not your dependent; a person who was your spouse at any time during 2025; or the parent of your qualifying person, if that person is your child under age 13?
- Interpretation: amb.2025.dc_ineligible_providers
- Expr: `{"op":"input","source":"Was this provider any of these: a person you (or your spouse, if filing jointly) can claim as a dependent; your child (including a stepchild or foster child) who was under age 19 at the end of 2025, even if not your dependent; a person who was your spouse at any time during 2025; or the parent of your qualifying person, if that person is your child under age 13?"}`
- Cite: [p503] p. 8, Payments to Relatives or Dependents, "However, don't count any amounts you pay to" and "The parent of your qualifying person if your qualifying person is your child and under age 13" (For use in preparing 2025 returns; sha256 3a00d0c1)

## (helper) — `dcprov.see_statement`

- **Authored helper label:** Column (c) reads "See Attached Statement"
- **Encoded (Bool):** line 1(c) = 'see_statement'
- Expr: `{"eq":["dcprov.tin_kind",{"const":"see_statement"}],"op":"test"}`
- Cite: [i2441] p. 3, Due Diligence, "Enter “See Attached Statement” in the columns for which you don't have the information" (2025; sha256 86f0669e)
