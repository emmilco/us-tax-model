# Foreign tax credit — election without Form 1116, or Form 1116

- Document: `ftc` (form, tax year 2025)
- Note: Creditable foreign tax is a supplied amount after reductions; this slice does not determine foreign-tax law or automate holdings/related-payment tests. The election is made whenever its conditions are met and no carryover is claimed; otherwise the credit is Form 1116 line 35. NIIT is excluded from regular tax.

## (helper) — `ftc.taxes`

- **Authored helper label:** Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7, less any tax that is not creditable (such as tax on a dividend that fails the holding period or must be paid over)
- **Encoded (NonNegDollars):** Input — Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7, leaving out tax withheld on a dividend from stock held fewer than 16 days within the 31-day period that begins 15 days before the ex-dividend date, and tax on a dividend to the extent you have to make related payments
- Expr: `{"op":"input","source":"Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7, leaving out tax withheld on a dividend from stock held fewer than 16 days within the 31-day period that begins 15 days before the ex-dividend date, and tax on a dividend to the extent you have to make related payments"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax; p. 3, Foreign Taxes Not Eligible for a Credit, item 5, "Foreign taxes withheld on a dividend from a corporation, if you haven’t held the stock for at least 16 days within the 31-day period that begins 15 days before the ex-dividend date", and item 6, "Foreign taxes withheld on a dividend to the extent that you have to make related payments on positions in substantially similar or related property" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (gate) — `ftc.asked`

- **Authored helper label:** Shares or a Form 1099-DIV, taxable interest above zero, or income tax ever paid to another country: the filers who can have foreign tax to enter
- **Encoded (Bool):** (div helper "In 2025, did you (or, on a joint return, your spouse) own shares of a company or a fund outside a retirement account, or get a Form 1099-DIV?" = true or sb helper "Taxable interest from all payers, before any Schedule B adjustment" > $0 or s3 helper "Have you (or, on a joint return, your spouse) ever paid income tax to a foreign country or a U.S. territory, had income from sources in a U.S. territory, or owned 10% or more of a foreign corporation?" = true)
- Expr: `{"any":[{"eq":["div.any",{"const":true}],"op":"test"},{"gt":["sb.interest_total",{"const":0}],"op":"test"},{"eq":["s3.foreign_any",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.taxes_if_asked`

- **Authored helper label:** Total creditable foreign taxes after required reductions, when you or your spouse owned shares or received a Form 1099-DIV, were paid taxable interest, or ever paid income tax to another country; zero otherwise
- **Encoded (NonNegDollars):** Choose — [helper "Shares or a Form 1099-DIV, taxable interest above zero, or income tax ever paid to another country: the filers who can have foreign tax to enter" = true → helper "Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7, less any tax that is not creditable (such as tax on a dividend that fails the holding period or must be paid over)"] [helper "Shares or a Form 1099-DIV, taxable interest above zero, or income tax ever paid to another country: the filers who can have foreign tax to enter" = false → helper "Year parameter sales.zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["ftc.asked",{"const":true}],"op":"test"},"then":"ftc.taxes"},{"guard":{"eq":["ftc.asked",{"const":false}],"op":"test"},"then":"ftc.zero"}],"op":"choose"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.carryover`

- **Authored helper label:** Are any of your (or, on a joint return, your spouse's) unused foreign taxes carried to 2025 from another tax year?
- **Encoded (Bool):** Input — Are any of your (or, on a joint return, your spouse's) unused foreign taxes carried to 2025 from another tax year (Schedule B (Form 1116) of 2024, line 8)?
- Expr: `{"op":"input","source":"Are any of your (or, on a joint return, your spouse's) unused foreign taxes carried to 2025 from another tax year (Schedule B (Form 1116) of 2024, line 8)?"}`
- Cite: [i1116] p. 19, Line 10, "Enter the unused foreign taxes in the separate category from another tax year that are eligible to be carried forward to or back to 2025" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.carryover_ask`

- **Authored helper label:** The carryover question is asked: foreign tax, territory income or a foreign corporation at some time, or a 2024 return with a form besides Form 1040 and its schedules
- **Encoded (Bool):** Choose — [s3 helper "Have you (or, on a joint return, your spouse) ever paid income tax to a foreign country or a U.S. territory, had income from sources in a U.S. territory, or owned 10% or more of a foreign corporation?" = true → s3 helper "Have you (or, on a joint return, your spouse) ever paid income tax to a foreign country or a U.S. territory, had income from sources in a U.S. territory, or owned 10% or more of a foreign corporation?"] [s3 helper "Have you (or, on a joint return, your spouse) ever paid income tax to a foreign country or a U.S. territory, had income from sources in a U.S. territory, or owned 10% or more of a foreign corporation?" = false → s3 helper "Does your (or, on a joint return, your spouse's) 2024 federal income tax return include any form other than Form 1040 or 1040-SR and its schedules?"]
- Expr: `{"alternatives":[{"guard":{"eq":["s3.foreign_any",{"const":true}],"op":"test"},"then":"s3.foreign_any"},{"guard":{"eq":["s3.foreign_any",{"const":false}],"op":"test"},"then":"s3.prior_other_forms"}],"op":"choose"}`
- Cite: [i1116] p. 19, Line 10, "Enter the unused foreign taxes in the separate category from another tax year that are eligible to be carried forward to or back to 2025" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (gate) — `ftc.carryover_if_asked`

- **Authored helper label:** Whether a foreign tax credit carried from another year is claimed, asked only of a filer who has paid income tax to a foreign country or a U.S. territory, had territory income or owned part of a foreign corporation, or whose 2024 return includes a form besides Form 1040 and its schedules (false otherwise)
- **Encoded (Bool):** Choose — [helper "The carryover question is asked: foreign tax, territory income or a foreign corporation at some time, or a 2024 return with a form besides Form 1040 and its schedules" = true → helper "Are any of your (or, on a joint return, your spouse's) unused foreign taxes carried to 2025 from another tax year?"] [helper "The carryover question is asked: foreign tax, territory income or a foreign corporation at some time, or a 2024 return with a form besides Form 1040 and its schedules" = false → helper "Year parameter ftc.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["ftc.carryover_ask",{"const":true}],"op":"test"},"then":"ftc.carryover"},{"guard":{"eq":["ftc.carryover_ask",{"const":false}],"op":"test"},"then":"ftc.no"}],"op":"choose"}`
- Cite: [i1116] p. 19, Line 10, "Enter the unused foreign taxes in the separate category from another tax year that are eligible to be carried forward to or back to 2025" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.all_passive`

- **Authored helper label:** Was all foreign-source gross income passive category income under the small-tax election rules (counting high-taxed income and certain export financing interest as passive)?
- **Encoded (Bool):** Input — Was all foreign-source gross income passive category income under the small-tax election rules? For this purpose passive income also includes income subject to the special rule for high-taxed income and certain export financing interest.
- Expr: `{"op":"input","source":"Was all foreign-source gross income passive category income under the small-tax election rules? For this purpose passive income also includes income subject to the special rule for high-taxed income and certain export financing interest."}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax; p. 1, Election To Claim the Foreign Tax Credit Without Filing Form 1116, "However, for this purpose, passive income also includes (a) income subject to the special rule for high-taxed income, described later; and (b) certain export financing interest." (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.statements`

- **Authored helper label:** Were all foreign income and taxes reported on qualified payee statements?
- **Encoded (Bool):** Input — Were all foreign income and taxes reported on qualified payee statements?
- Expr: `{"op":"input","source":"Were all foreign income and taxes reported on qualified payee statements?"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.eligible`

- **Authored helper label:** Is all of the foreign tax entered creditable, after leaving out tax that fails the creditability, holding-period or related-payment rules and making the required foreign-tax reductions?
- **Encoded (Bool):** Input — Is all of the foreign tax entered creditable? Tax that fails the creditability, holding-period or related-payment rules is left out of the amount entered, and the required foreign-tax reductions are made in it, before answering.
- Expr: `{"op":"input","source":"Is all of the foreign tax entered creditable? Tax that fails the creditability, holding-period or related-payment rules is left out of the amount entered, and the required foreign-tax reductions are made in it, before answering."}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax; p. 2, "You are still required to take into account the general rules for determining whether a tax is creditable" and "You are still required to reduce the taxes available for credit by any amount you would have entered on line 12 of Form 1116" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.elect`

- **Authored helper label:** The credit is claimed without Form 1116 whenever the election's conditions are met and no carryover from another year is claimed (that credit, the smaller of the foreign tax and the regular tax, is never less than a Form 1116 credit without a carryover, whose line 21 is at most line 20; foreign tax carried in is used only on Form 1116)
- **Encoded (Bool):** Choose — [helper "Whether a foreign tax credit carried from another year is claimed, asked only of a filer who has paid income tax to a foreign country or a U.S. territory, had territory income or owned part of a foreign corporation, or whose 2024 return includes a form besides Form 1040 and its schedules (false otherwise)" = true → helper "Year parameter ftc.no (false)"] [helper "Whether a foreign tax credit carried from another year is claimed, asked only of a filer who has paid income tax to a foreign country or a U.S. territory, had territory income or owned part of a foreign corporation, or whose 2024 return includes a form besides Form 1040 and its schedules (false otherwise)" = false → helper "Year parameter ftc.yes (true)"]
- Interpretation: amb.2025.f1116_carryover_election
- Expr: `{"alternatives":[{"guard":{"eq":["ftc.carryover_if_asked",{"const":true}],"op":"test"},"then":"ftc.no"},{"guard":{"eq":["ftc.carryover_if_asked",{"const":false}],"op":"test"},"then":"ftc.yes"}],"op":"choose"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax; pp. 1–2, "You can’t carry over to or from any other year any foreign taxes paid or accrued" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.yes`

- **Authored helper label:** Year parameter ftc.yes (true)
- **Encoded (Bool):** Enter true (ftc.yes).
- Expr: `{"op":"param","ref":"ftc.yes"}`
- Cite: [i1116] p. 2, Purpose of Form, "File Form 1116 to claim the foreign tax credit if the election, earlier, doesn’t apply and" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.limit`

- **Authored helper label:** Year parameter ftc.limit
- **Encoded (NonNegDollars):** Enter single $300; mfj $600; mfs $300; hoh $300; qss $300 (ftc.limit).
- Expr: `{"op":"param","ref":"ftc.limit"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.zero`

- **Authored helper label:** Year parameter sales.zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.has_tax`

- **Authored helper label:** Positive foreign taxes
- **Encoded (Bool):** helper "Total creditable foreign taxes after required reductions, when you or your spouse owned shares or received a Form 1099-DIV, were paid taxable interest, or ever paid income tax to another country; zero otherwise" > $0
- Expr: `{"gt":["ftc.taxes_if_asked",{"const":0}],"op":"test"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.no`

- **Authored helper label:** Year parameter ftc.no (false)
- **Encoded (Bool):** Enter false (ftc.no).
- Expr: `{"op":"param","ref":"ftc.no"}`
- Cite: [i1116] p. 2, Purpose of Form, "File Form 1116 to claim the foreign tax credit if the election, earlier, doesn’t apply and", "You paid or accrued certain foreign taxes to a foreign country or U.S. territory" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.all_passive_if_tax`

- **Authored helper label:** Whether all foreign-source gross income was passive category income, asked only with foreign tax (false without foreign tax, where neither the election nor Form 1116 applies)
- **Encoded (Bool):** Choose — [helper "Positive foreign taxes" = true → helper "Was all foreign-source gross income passive category income under the small-tax election rules (counting high-taxed income and certain export financing interest as passive)?"] [helper "Positive foreign taxes" = false → helper "Year parameter ftc.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["ftc.has_tax",{"const":true}],"op":"test"},"then":"ftc.all_passive"},{"guard":{"eq":["ftc.has_tax",{"const":false}],"op":"test"},"then":"ftc.no"}],"op":"choose"}`
- Cite: [i1116] p. 2, Purpose of Form, "File Form 1116 to claim the foreign tax credit if the election, earlier, doesn’t apply and", "You paid or accrued certain foreign taxes to a foreign country or U.S. territory"; p. 1, "This election is available only if you meet all of the following conditions" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.statements_if_tax`

- **Authored helper label:** Whether all foreign income and taxes were reported on qualified payee statements, asked only with foreign tax (false without foreign tax, where neither the election nor Form 1116 applies)
- **Encoded (Bool):** Choose — [helper "Positive foreign taxes" = true → helper "Were all foreign income and taxes reported on qualified payee statements?"] [helper "Positive foreign taxes" = false → helper "Year parameter ftc.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["ftc.has_tax",{"const":true}],"op":"test"},"then":"ftc.statements"},{"guard":{"eq":["ftc.has_tax",{"const":false}],"op":"test"},"then":"ftc.no"}],"op":"choose"}`
- Cite: [i1116] p. 2, Purpose of Form, "File Form 1116 to claim the foreign tax credit if the election, earlier, doesn’t apply and", "You paid or accrued certain foreign taxes to a foreign country or U.S. territory"; p. 1, "This election is available only if you meet all of the following conditions" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.eligible_if_tax`

- **Authored helper label:** Whether the creditability, holding-period, related-payment and reduction rules are met, asked only with foreign tax (false without foreign tax, where neither the election nor Form 1116 applies)
- **Encoded (Bool):** Choose — [helper "Positive foreign taxes" = true → helper "Is all of the foreign tax entered creditable, after leaving out tax that fails the creditability, holding-period or related-payment rules and making the required foreign-tax reductions?"] [helper "Positive foreign taxes" = false → helper "Year parameter ftc.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["ftc.has_tax",{"const":true}],"op":"test"},"then":"ftc.eligible"},{"guard":{"eq":["ftc.has_tax",{"const":false}],"op":"test"},"then":"ftc.no"}],"op":"choose"}`
- Cite: [i1116] p. 2, Purpose of Form, "File Form 1116 to claim the foreign tax credit if the election, earlier, doesn’t apply and", "You paid or accrued certain foreign taxes to a foreign country or U.S. territory"; p. 1, "This election is available only if you meet all of the following conditions" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.elect_if_tax`

- **Authored helper label:** Whether the election without Form 1116 is made, asked only with foreign tax (false without foreign tax, where neither the election nor Form 1116 applies)
- **Encoded (Bool):** Choose — [helper "Positive foreign taxes" = true → helper "The credit is claimed without Form 1116 whenever the election's conditions are met and no carryover from another year is claimed (that credit, the smaller of the foreign tax and the regular tax, is never less than a Form 1116 credit without a carryover, whose line 21 is at most line 20; foreign tax carried in is used only on Form 1116)"] [helper "Positive foreign taxes" = false → helper "Year parameter ftc.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["ftc.has_tax",{"const":true}],"op":"test"},"then":"ftc.elect"},{"guard":{"eq":["ftc.has_tax",{"const":false}],"op":"test"},"then":"ftc.no"}],"op":"choose"}`
- Cite: [i1116] p. 2, Purpose of Form, "File Form 1116 to claim the foreign tax credit if the election, earlier, doesn’t apply and", "You paid or accrued certain foreign taxes to a foreign country or U.S. territory"; p. 1, "This election is available only if you meet all of the following conditions" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.needs1116`

- **Authored helper label:** Foreign tax fails a condition of the election, so the credit is figured on Form 1116
- **Encoded (Bool):** helper "Positive foreign taxes" = true and (helper "Total creditable foreign taxes after required reductions, when you or your spouse owned shares or received a Form 1099-DIV, were paid taxable interest, or ever paid income tax to another country; zero otherwise" > helper "Year parameter ftc.limit" or helper "Whether all foreign-source gross income was passive category income, asked only with foreign tax (false without foreign tax, where neither the election nor Form 1116 applies)" = false or helper "Whether all foreign income and taxes were reported on qualified payee statements, asked only with foreign tax (false without foreign tax, where neither the election nor Form 1116 applies)" = false or helper "Whether the creditability, holding-period, related-payment and reduction rules are met, asked only with foreign tax (false without foreign tax, where neither the election nor Form 1116 applies)" = false or helper "Whether the election without Form 1116 is made, asked only with foreign tax (false without foreign tax, where neither the election nor Form 1116 applies)" = false or sa helper "Do you (or, on a joint return, your spouse) file Form 2555 or Form 4563, or exclude income from sources within Puerto Rico?" = true)
- Expr: `{"all":[{"eq":["ftc.has_tax",{"const":true}],"op":"test"},{"any":[{"gt":["ftc.taxes_if_asked","ftc.limit"],"op":"test"},{"eq":["ftc.all_passive_if_tax",{"const":false}],"op":"test"},{"eq":["ftc.statements_if_tax",{"const":false}],"op":"test"},{"eq":["ftc.eligible_if_tax",{"const":false}],"op":"test"},{"eq":["ftc.elect_if_tax",{"const":false}],"op":"test"},{"eq":["sa.excluded_income",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax; i1040gi p. 115, "You aren’t filing Form 4563 or excluding income from sources within Puerto Rico" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (gate) — `ftc.carryover_no_tax`

- **Authored helper label:** A foreign tax credit carried from another year is claimed, with no foreign tax paid in 2025
- **Encoded (Bool):** helper "Whether a foreign tax credit carried from another year is claimed, asked only of a filer who has paid income tax to a foreign country or a U.S. territory, had territory income or owned part of a foreign corporation, or whose 2024 return includes a form besides Form 1040 and its schedules (false otherwise)" = true and helper "Positive foreign taxes" = false
- Expr: `{"all":[{"eq":["ftc.carryover_if_asked",{"const":true}],"op":"test"},{"eq":["ftc.has_tax",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1116] p. 19, Line 10, "Enter the unused foreign taxes in the separate category from another tax year that are eligible to be carried forward to or back to 2025" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.regular_tax`

- **Authored helper label:** Regular tax for the limit (Form 1040 line 16 plus Schedule 2 line 1z)
- **Encoded (Dollars):** Add f1040 line 16 and s2 line 1z.
- Expr: `{"of":["f1040.line16","s2.line1z"],"op":"sum"}`
- Cite: [i1116] p. 25, Line 20, "Enter the total of Form 1040, 1040-SR, or 1040-NR, line 16, and Schedule 2 (Form 1040), Part I, line 1z, less any tax included on line 16 from Form 4972." (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.limited`

- **Authored helper label:** Smaller of ftc.taxes_if_asked, ftc.regular_tax
- **Encoded (Dollars):** Enter the smaller of helper "Total creditable foreign taxes after required reductions, when you or your spouse owned shares or received a Form 1099-DIV, were paid taxable interest, or ever paid income tax to another country; zero otherwise" or helper "Regular tax for the limit (Form 1040 line 16 plus Schedule 2 line 1z)".
- Expr: `{"of":["ftc.taxes_if_asked","ftc.regular_tax"],"op":"smaller_of"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 25, Line 20, regular tax (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.credit_tax`

- **Authored helper label:** With foreign tax, the credit without Form 1116 when the election's conditions are met, and Form 1116 line 35 when they are not
- **Encoded (Dollars):** Choose — [helper "Foreign tax fails a condition of the election, so the credit is figured on Form 1116" = false → helper "Smaller of ftc.taxes_if_asked, ftc.regular_tax"] [helper "Foreign tax fails a condition of the election, so the credit is figured on Form 1116" = true → f1116 line 35]
- Expr: `{"alternatives":[{"guard":{"eq":["ftc.needs1116",{"const":false}],"op":"test"},"then":"ftc.limited"},{"guard":{"eq":["ftc.needs1116",{"const":true}],"op":"test"},"then":"f1116.line35"}],"op":"choose"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 2, Purpose of Form, "File Form 1116 to claim the foreign tax credit if the election, earlier, doesn’t apply and" (2025; printed date 2025-12-23; sha256 6998cf8c)

## (helper) — `ftc.credit`

- **Authored helper label:** The credit without Form 1116 (the smaller of creditable foreign tax and regular income tax) when the election's conditions are met; Form 1116 line 35 when they are not; zero if no foreign tax
- **Encoded (Dollars):** Choose — [helper "Positive foreign taxes" = true → helper "With foreign tax, the credit without Form 1116 when the election's conditions are met, and Form 1116 line 35 when they are not"] [helper "Positive foreign taxes" = false → helper "Year parameter sales.zero"]
- **Refusal:** when ftc.carryover_no_tax is true, cannot complete Form 1116 (a carryover with no foreign tax in 2025). A foreign tax credit carried from another year, with no foreign tax paid in 2025, is figured on Form 1116 from the year's foreign income, which this tool does not ask for without foreign tax. Cite: [i1116] p. 19, Line 10, "Enter the unused foreign taxes in the separate category from another tax year that are eligible to be carried forward to or back to 2025" (2025; printed date 2025-12-23; sha256 6998cf8c)
- Expr: `{"alternatives":[{"guard":{"eq":["ftc.has_tax",{"const":true}],"op":"test"},"then":"ftc.credit_tax"},{"guard":{"eq":["ftc.has_tax",{"const":false}],"op":"test"},"then":"ftc.zero"}],"op":"choose"}`
- Cite: [i1116] pp. 1–2, election to claim the foreign tax credit without filing Form 1116; p. 2, Purpose of Form, "File Form 1116 to claim the foreign tax credit if the election, earlier, doesn’t apply and" (2025; printed date 2025-12-23; sha256 6998cf8c)
