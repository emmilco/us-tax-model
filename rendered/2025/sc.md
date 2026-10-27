# Schedule C (Form 1040) — Profit or Loss From Business, one per business

- Document: `sc` (form, tax year 2025)
- Collection: keyed entries within person; [i1040sc] p. 3, Line A, "If you owned more than one business, complete a separate Schedule C for each business" (2025; sha256 b5536db9)
- Note: One entry per business a person operated as a sole proprietor (i1040sc p. 3, Line A, "If you owned more than one business, complete a separate Schedule C for each business"). The screens refuse statutory employee income, notary fees, passive and rental activities, businesses owned with a spouse, accounting method changes and the special items of the instructions; Form 8829, Form 6198 and Form 461 are refused where they apply.

## (helper) — `sc.one`

- **Authored helper label:** One business
- **Encoded (Count):** Enter 1 (sc.one).
- Expr: `{"op":"param","ref":"sc.one"}`
- Cite: [i1040sc] p. 3, Line A, "complete a separate Schedule C for each business" (2025; sha256 b5536db9)

## (helper) — `sc.rrta`

- **Authored helper label:** This business's owner has railroad retirement compensation
- **Encoded (Bool):** Enter the amount from person line rrta.
- Expr: `{"from":"person.rrta","op":"copy"}`
- Cite: [f1040sse] Schedule SE (2025), line 8a, "Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2) and railroad retirement (tier 1) compensation" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `sc.zero`

- **Authored helper label:** Zero
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [f1040sc] Schedule C (2025), Part II (2025; created 2025-04-03; sha256 ddf401db)

## (screen) — `sc.statutory`

- **Authored helper label:** Is this business income you received as a statutory employee (the "Statutory employee" box in box 13 of your Form W-2 was checked), or fees you received as a notary public?
- **Encoded (Bool):** Input — Is this business income you received as a statutory employee (the "Statutory employee" box in box 13 of your Form W-2 was checked), or fees you received as a notary public?
- Expr: `{"op":"input","source":"Is this business income you received as a statutory employee (the \"Statutory employee\" box in box 13 of your Form W-2 was checked), or fees you received as a notary public?"}`
- Cite: [i1040sc] p. 5, Line 1, Statutory employees; p. 14, Line 31, Statutory employees and Notary public (2025; sha256 b5536db9)

## G — `sc.passive`

- **IRS:** Did you "materially participate" in the operation of this business during 2025, and is the business something other than a rental activity?
- **Encoded (Bool):** Input — Did you "materially participate" in the operation of this business during 2025 (for example, you worked in it more than 500 hours, or your work was substantially all the work done in it, or more than 100 hours and at least as much as anyone else; see the seven tests in the instructions for line G), or is it a working interest in an oil or gas well you own directly or through an entity that does not limit your liability (the exception for oil and gas), and is the business something other than a rental activity?
- Expr: `{"op":"input","source":"Did you \"materially participate\" in the operation of this business during 2025 (for example, you worked in it more than 500 hours, or your work was substantially all the work done in it, or more than 100 hours and at least as much as anyone else; see the seven tests in the instructions for line G), or is it a working interest in an oil or gas well you own directly or through an entity that does not limit your liability (the exception for oil and gas), and is the business something other than a rental activity?"}`
- Cite: [i1040sc] p. 4, Line G, Material participation (the seven tests) and Rental of personal property (2025; sha256 b5536db9)

## (screen) — `sc.spouse_owned`

- **Authored helper label:** Do you own this business together with your spouse (as a qualified joint venture, as community property, or as partners)?
- **Encoded (Bool):** Input — Do you own this business together with your spouse (as a qualified joint venture, as community property, or as partners)?
- Expr: `{"op":"input","source":"Do you own this business together with your spouse (as a qualified joint venture, as community property, or as partners)?"}`
- Cite: [i1040sc] p. 2, Business Owned and Operated by Spouses, Qualified Joint Venture and Community Income (2025; sha256 b5536db9)

## F — `sc.method_other`

- **IRS:** Do you use an accounting method other than cash or accrual, or did you change your accounting method for 2025 (Form 3115 or a section 481(a) adjustment), or must you capitalize costs under the uniform capitalization rules (section 263A) because you are not a small business taxpayer?
- **Encoded (Bool):** Input — Do you use an accounting method other than cash or accrual, or did you change your accounting method for 2025 (Form 3115 or a section 481(a) adjustment), or must you capitalize costs under the uniform capitalization rules (section 263A) because your average annual gross receipts for the 3 prior years were more than $31 million?
- Expr: `{"op":"input","source":"Do you use an accounting method other than cash or accrual, or did you change your accounting method for 2025 (Form 3115 or a section 481(a) adjustment), or must you capitalize costs under the uniform capitalization rules (section 263A) because your average annual gross receipts for the 3 prior years were more than $31 million?"}`
- Cite: [i1040sc] p. 4, Line F; p. 6, Part II, Capitalizing costs; p. 15, Part III, Small business taxpayer (2025; sha256 b5536db9)

## (screen) — `sc.special`

- **Authored helper label:** For this business, do you have any of these: depletion (line 12); the energy efficient commercial buildings deduction (Form 7205); wages or benefits reduced by an employment credit (Forms 5884, 8844, 8846, 8932, 8941 or 8994); business interest limited by Form 8990; recapture of depreciation or section 179 on listed property, or an inclusion amount for leased property; a chapter 11 bankruptcy case; extraterritorial income (Form 8873); installment sales of timeshares or residential lots; nontaxable Medicaid waiver payments (Notice 2014-7); research or experimental expenditures you elect to capitalize; a capital construction fund; or contributions you made on your own behalf, as a self-employed person, to a dependent care assistance program (Form 2441, Parts I and III)?
- **Encoded (Bool):** Input — For this business, do you have any of these: depletion (line 12); the energy efficient commercial buildings deduction (Form 7205); wages or benefits reduced by an employment credit (Forms 5884, 8844, 8846, 8932, 8941 or 8994); business interest limited by Form 8990; recapture of depreciation or section 179 on listed property, or an inclusion amount for leased property; a chapter 11 bankruptcy case; extraterritorial income (Form 8873); installment sales of timeshares or residential lots; nontaxable Medicaid waiver payments (Notice 2014-7); research or experimental expenditures you elect to capitalize; a capital construction fund; or contributions you made on your own behalf, as a self-employed person, to a dependent care assistance program (Form 2441, Parts I and III)?
- Expr: `{"op":"input","source":"For this business, do you have any of these: depletion (line 12); the energy efficient commercial buildings deduction (Form 7205); wages or benefits reduced by an employment credit (Forms 5884, 8844, 8846, 8932, 8941 or 8994); business interest limited by Form 8990; recapture of depreciation or section 179 on listed property, or an inclusion amount for leased property; a chapter 11 bankruptcy case; extraterritorial income (Form 8873); installment sales of timeshares or residential lots; nontaxable Medicaid waiver payments (Notice 2014-7); research or experimental expenditures you elect to capitalize; a capital construction fund; or contributions you made on your own behalf, as a self-employed person, to a dependent care assistance program (Form 2441, Parts I and III)?"}`
- Cite: [i1040sc] p. 1, What's New (research and experimental expenditures); p. 3, Capital Construction Fund; p. 5, Part I; p. 6, Medicaid waiver payments and Installment sales; p. 6, Line 6; p. 7, Lines 12 and 14 (including 'If you made contributions on your behalf as a self-employed person to a dependent care assistance program, complete Form 2441, Parts I and III'); p. 8, Lines 16a and 16b; p. 9, Line 23; p. 10, Lines 26 and 27a (2025; sha256 b5536db9)

## (gate) — `sc.screened`

- **Authored helper label:** Something on this Schedule C is outside this tool
- **Encoded (Bool):** (column (screen) (sc.statutory) = true or line G = false or column (screen) (sc.spouse_owned) = true or line F = true or column (screen) (sc.special) = true)
- Expr: `{"any":[{"eq":["sc.statutory",{"const":true}],"op":"test"},{"eq":["sc.passive",{"const":false}],"op":"test"},{"eq":["sc.spouse_owned",{"const":true}],"op":"test"},{"eq":["sc.method_other",{"const":true}],"op":"test"},{"eq":["sc.special",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040sc] pp. 2-15, the items named in the screens of this Schedule C (2025; sha256 b5536db9)

## 1 — `sc.line1`

- **IRS:** Gross receipts or sales
- **Encoded (NonNegDollars):** Input — Gross receipts or sales of this business for 2025, including amounts properly shown on Forms 1099-NEC and any other gross receipts of this business reported to you on a Form 1099 (such as Form 1099-K); not the other business income asked about separately, such as prizes and awards (zero if none)
- **Refusal:** when sc.screened is true, cannot complete Schedule C items outside this tool. Statutory employee and notary income, passive and rental activities, businesses owned with your spouse, accounting method changes and the special items in the screen are outside this tool. Cite: [i1040sc] pp. 2-15, the items named in the screens of this Schedule C (2025; sha256 b5536db9)
- Expr: `{"op":"input","source":"Gross receipts or sales of this business for 2025, including amounts properly shown on Forms 1099-NEC and any other gross receipts of this business reported to you on a Form 1099 (such as Form 1099-K); not the other business income asked about separately, such as prizes and awards (zero if none)"}`
- Cite: [i1040sc] p. 5, Line 1, "Enter gross receipts from your trade or business. Be sure to check any Forms 1099 you received" (2025; sha256 b5536db9)

## 2 — `sc.line2`

- **IRS:** Returns and allowances
- **Encoded (NonNegDollars):** Input — Returns and allowances (refunds and price reductions you gave customers), as a positive number; zero if none
- Expr: `{"op":"input","source":"Returns and allowances (refunds and price reductions you gave customers), as a positive number; zero if none"}`
- Cite: [i1040sc] p. 6, Line 2 (2025; sha256 b5536db9)

## 3 — `sc.line3`

- **IRS:** Subtract line 2 from line 1
- **Encoded (Dollars):** Subtract line 2 (sc.line2) from line 1 (sc.line1).
- Expr: `{"from":"sc.line1","op":"subtract","take":"sc.line2"}`
- Cite: [f1040sc] Schedule C (2025), line 3 (2025; created 2025-04-03; sha256 ddf401db)

## 4 — `sc.line4`

- **IRS:** Cost of goods sold (from line 42)
- **Encoded (Dollars):** Enter the amount from line 42.
- Expr: `{"from":"sc.line42","op":"copy"}`
- Cite: [f1040sc] Schedule C (2025), line 4 (2025; created 2025-04-03; sha256 ddf401db)

## 5 — `sc.line5`

- **IRS:** Gross profit. Subtract line 4 from line 3
- **Encoded (Dollars):** Subtract line 4 (sc.line4) from line 3 (sc.line3).
- Expr: `{"from":"sc.line3","op":"subtract","take":"sc.line4"}`
- Cite: [f1040sc] Schedule C (2025), line 5 (2025; created 2025-04-03; sha256 ddf401db)

## 6 — `sc.line6`

- **IRS:** Other income, including federal and state gasoline or fuel tax credit or refund
- **Encoded (NonNegDollars):** Input — Other business income not in gross receipts, such as scrap sales, bad debts you recovered, interest on accounts receivable, state gasoline or fuel tax refunds, prizes and awards related to the business, and Form 1099-PATR amounts; zero if none
- Expr: `{"op":"input","source":"Other business income not in gross receipts, such as scrap sales, bad debts you recovered, interest on accounts receivable, state gasoline or fuel tax refunds, prizes and awards related to the business, and Form 1099-PATR amounts; zero if none"}`
- Cite: [i1040sc] p. 6, Line 6 (2025; sha256 b5536db9)

## 7 — `sc.line7`

- **IRS:** Gross income. Add lines 5 and 6
- **Encoded (Dollars):** Add line 5 (sc.line5) and line 6.
- Expr: `{"of":["sc.line5","sc.line6"],"op":"sum"}`
- Cite: [f1040sc] Schedule C (2025), line 7 (2025; created 2025-04-03; sha256 ddf401db)

## 8 — `sc.line8`

- **IRS:** Advertising
- **Encoded (NonNegDollars):** Input — Advertising expenses of this business; zero if none
- Expr: `{"op":"input","source":"Advertising expenses of this business; zero if none"}`
- Cite: [i1040sc] p. 6, Part II, Expenses; Schedule C (2025), line 8 (2025; sha256 b5536db9)

## 9 — `sc.line9`

- **IRS:** Car and truck expenses
- **Encoded (NonNegDollars):** Add scveh.line9 over every confirmed scveh entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"scveh","field":"scveh.line9","op":"sum_over"}`
- Cite: [i1040sc] p. 6, Line 9, standard mileage rate or actual expenses, for each vehicle (2025; sha256 b5536db9)

## 10 — `sc.line10`

- **IRS:** Commissions and fees
- **Encoded (NonNegDollars):** Input — Commissions and fees you paid (not capitalized and not deducted elsewhere); zero if none
- Expr: `{"op":"input","source":"Commissions and fees you paid (not capitalized and not deducted elsewhere); zero if none"}`
- Cite: [i1040sc] p. 7, Line 10 (2025; sha256 b5536db9)

## 11 — `sc.line11`

- **IRS:** Contract labor
- **Encoded (NonNegDollars):** Input — Payments to independent contractors and others you do not treat as employees (not included on lines 17, 21, 26 or 37); zero if none
- Expr: `{"op":"input","source":"Payments to independent contractors and others you do not treat as employees (not included on lines 17, 21, 26 or 37); zero if none"}`
- Cite: [i1040sc] p. 7, Line 11 (2025; sha256 b5536db9)

## 12 — `sc.line12`

- **IRS:** Depletion
- **Encoded (NonNegDollars):** Enter the amount from helper "Zero".
- Expr: `{"from":"sc.zero","op":"copy"}`
- Cite: [i1040sc] p. 7, Line 12 (depletion is refused by the screen of this Schedule C) (2025; sha256 b5536db9)

## 13 — `sc.line13`

- **IRS:** Depreciation and section 179 expense deduction (not included in Part III)
- **Encoded (NonNegDollars):** Add helper "Depreciation other than the section 179 deduction (Form 4562 lines 14, 17, 19 and 21)" and line 12 (sc.s179_allowed).
- Expr: `{"of":["sc.dep_other","sc.s179_allowed"],"op":"sum"}`
- Cite: [i1040sc] p. 7, Line 13, "See the Instructions for Form 4562 and Pub. 946 to figure the amount to enter on line 13"; i4562 p. 13, Part IV, line 22 (2025; sha256 b5536db9)

## 14 — `sc.line14`

- **IRS:** Employee benefit programs (other than on line 19)
- **Encoded (NonNegDollars):** Input — Contributions to employee benefit programs for your employees, such as accident and health plans, group-term life insurance and dependent care assistance (not for yourself, and not pension or profit-sharing plans); zero if none
- Expr: `{"op":"input","source":"Contributions to employee benefit programs for your employees, such as accident and health plans, group-term life insurance and dependent care assistance (not for yourself, and not pension or profit-sharing plans); zero if none"}`
- Cite: [i1040sc] pp. 7-8, Line 14 (2025; sha256 b5536db9)

## 15 — `sc.line15`

- **IRS:** Insurance (other than health)
- **Encoded (NonNegDollars):** Input — Premiums for business insurance (not health insurance for yourself, not a reserve for self-insurance, not lost-earnings insurance); zero if none
- Expr: `{"op":"input","source":"Premiums for business insurance (not health insurance for yourself, not a reserve for self-insurance, not lost-earnings insurance); zero if none"}`
- Cite: [i1040sc] p. 8, Line 15 (2025; sha256 b5536db9)

## 16a — `sc.line16a`

- **IRS:** Interest: mortgage (paid to banks, etc.)
- **Encoded (NonNegDollars):** Input — Interest you paid for 2025 on a mortgage on real property used in the business, to banks or other financial institutions for which you received a Form 1098 (only the business part; not interest that must be capitalized); zero if none
- Expr: `{"op":"input","source":"Interest you paid for 2025 on a mortgage on real property used in the business, to banks or other financial institutions for which you received a Form 1098 (only the business part; not interest that must be capitalized); zero if none"}`
- Cite: [i1040sc] p. 8, Lines 16a and 16b, How to report (2025; sha256 b5536db9)

## 16b — `sc.line16b`

- **IRS:** Interest: other
- **Encoded (NonNegDollars):** Input — Other interest on business debt (including mortgage interest not reported on a Form 1098 to you); for a vehicle used for business and personal purposes, only the business part, and none of the interest you deduct on Schedule 1-A; zero if none
- Expr: `{"op":"input","source":"Other interest on business debt (including mortgage interest not reported on a Form 1098 to you); for a vehicle used for business and personal purposes, only the business part, and none of the interest you deduct on Schedule 1-A; zero if none"}`
- Cite: [i1040sc] p. 8, Lines 16a and 16b (2025; sha256 b5536db9)

## 17 — `sc.line17`

- **IRS:** Legal and professional services
- **Encoded (NonNegDollars):** Input — Fees of accountants and attorneys directly related to operating the business, including tax advice and preparation of the business tax forms; zero if none
- Expr: `{"op":"input","source":"Fees of accountants and attorneys directly related to operating the business, including tax advice and preparation of the business tax forms; zero if none"}`
- Cite: [i1040sc] p. 8, Line 17 (2025; sha256 b5536db9)

## 18 — `sc.line18`

- **IRS:** Office expense
- **Encoded (NonNegDollars):** Input — Office supplies and postage; zero if none
- Expr: `{"op":"input","source":"Office supplies and postage; zero if none"}`
- Cite: [i1040sc] p. 8, Line 18 (2025; sha256 b5536db9)

## 19 — `sc.line19`

- **IRS:** Pension and profit-sharing plans
- **Encoded (NonNegDollars):** Input — Contributions you made for your employees to a pension, profit-sharing or annuity plan, including SEP, SIMPLE and SARSEP plans (not contributions for yourself, which go on Schedule 1, line 16); zero if none
- Expr: `{"op":"input","source":"Contributions you made for your employees to a pension, profit-sharing or annuity plan, including SEP, SIMPLE and SARSEP plans (not contributions for yourself, which go on Schedule 1, line 16); zero if none"}`
- Cite: [i1040sc] p. 8, Line 19 (2025; sha256 b5536db9)

## 20a — `sc.line20a`

- **IRS:** Rent or lease: vehicles, machinery, and equipment
- **Encoded (NonNegDollars):** Add helper "Rent or lease of machinery and equipment, and of vehicles not entered as vehicles" and helper "Business part of vehicle lease payments".
- Expr: `{"of":["sc.rent_equipment","sc.veh_lease"],"op":"sum"}`
- Cite: [i1040sc] p. 8, Lines 20a and 20b, "If you rented or leased vehicles, machinery, or equipment, enter on line 20a the business portion of your rental cost" (2025; sha256 b5536db9)

## 20b — `sc.line20b`

- **IRS:** Rent or lease: other business property
- **Encoded (NonNegDollars):** Input — Rent for other business property, such as office space; zero if none
- Expr: `{"op":"input","source":"Rent for other business property, such as office space; zero if none"}`
- Cite: [i1040sc] p. 8, Lines 20a and 20b (2025; sha256 b5536db9)

## 21 — `sc.line21`

- **IRS:** Repairs and maintenance
- **Encoded (NonNegDollars):** Input — Incidental repairs and maintenance that do not add to the property's value or appreciably prolong its life (not your own labor, and not restorations or replacements, which are capitalized); zero if none
- Expr: `{"op":"input","source":"Incidental repairs and maintenance that do not add to the property's value or appreciably prolong its life (not your own labor, and not restorations or replacements, which are capitalized); zero if none"}`
- Cite: [i1040sc] p. 8, Line 21 (2025; sha256 b5536db9)

## 22 — `sc.line22`

- **IRS:** Supplies (not included in Part III)
- **Encoded (NonNegDollars):** Input — Materials and supplies actually consumed and used in the business during 2025 (or incidental supplies purchased during 2025 if you keep no inventory or records of use); zero if none
- Expr: `{"op":"input","source":"Materials and supplies actually consumed and used in the business during 2025 (or incidental supplies purchased during 2025 if you keep no inventory or records of use); zero if none"}`
- Cite: [i1040sc] p. 8, Line 22 (2025; sha256 b5536db9)

## 23 — `sc.line23`

- **IRS:** Taxes and licenses
- **Encoded (NonNegDollars):** Input — Business taxes and licenses: sales tax imposed on you as the seller, real estate and personal property taxes on business assets, licenses and regulatory fees, the employer share of social security and Medicare taxes, federal unemployment tax, federal highway use tax, state unemployment contributions (not income or self-employment tax, and not taxes on property you bought); zero if none
- Expr: `{"op":"input","source":"Business taxes and licenses: sales tax imposed on you as the seller, real estate and personal property taxes on business assets, licenses and regulatory fees, the employer share of social security and Medicare taxes, federal unemployment tax, federal highway use tax, state unemployment contributions (not income or self-employment tax, and not taxes on property you bought); zero if none"}`
- Cite: [i1040sc] p. 9, Line 23 (2025; sha256 b5536db9)

## 24a — `sc.line24a`

- **IRS:** Travel
- **Encoded (NonNegDollars):** Input — Lodging and transportation for overnight business travel away from your tax home (not meals and not entertainment); zero if none
- Expr: `{"op":"input","source":"Lodging and transportation for overnight business travel away from your tax home (not meals and not entertainment); zero if none"}`
- Cite: [i1040sc] p. 9, Line 24a (2025; sha256 b5536db9)

## (helper) — `sc.meals_50`

- **Authored helper label:** Business meals subject to the 50% limit, at their full cost
- **Encoded (NonNegDollars):** Input — The full cost of business meals (actual cost or the standard meal allowance) subject to the 50% limit, before applying the percentage; zero if none
- Expr: `{"op":"input","source":"The full cost of business meals (actual cost or the standard meal allowance) subject to the 50% limit, before applying the percentage; zero if none"}`
- Cite: [i1040sc] pp. 9–10, Line 24b, Business meal expenses, Standard meal allowance and Amount of deduction (2025; sha256 b5536db9)

## (helper) — `sc.meals_80`

- **Authored helper label:** Business meals during or incident to a period of duty under the Department of Transportation hours of service limits, at their full cost
- **Encoded (NonNegDollars):** Input — The full cost of business meals consumed during or incident to a period of duty for which you were subject to the Department of Transportation hours of service limits (certain air transportation workers, interstate truck operators, certain merchant mariners), before applying the percentage; zero if none
- Expr: `{"op":"input","source":"The full cost of business meals consumed during or incident to a period of duty for which you were subject to the Department of Transportation hours of service limits (certain air transportation workers, interstate truck operators, certain merchant mariners), before applying the percentage; zero if none"}`
- Cite: [i1040sc] p. 10, Line 24b, Amount of deduction, "the percentage is increased to 80%" (2025; sha256 b5536db9)

## (helper) — `sc.meals_100`

- **Authored helper label:** Meals and incidentals not subject to the 50% limit, deducted in full
- **Encoded (NonNegDollars):** Input — The cost of meals and incidentals not subject to the 50% limit, deducted in full: meals furnished or reimbursed to an employee and treated as wages subject to withholding; meals provided to a nonemployee, to the extent includible in their income and reported on Form 1099-NEC; meals a customer or client reimbursed you for, as an independent contractor, after you gave them adequate records; recreational, social or similar activities for your employees (such as a holiday party or a summer picnic); food and beverages provided to the general public as advertising or to promote goodwill; and meals you sell to the public. Don't include anything entered elsewhere on this Schedule C (for example, in cost of goods sold); zero if none
- Interpretation: amb.2025.meals_full_exceptions
- Expr: `{"op":"input","source":"The cost of meals and incidentals not subject to the 50% limit, deducted in full: meals furnished or reimbursed to an employee and treated as wages subject to withholding; meals provided to a nonemployee, to the extent includible in their income and reported on Form 1099-NEC; meals a customer or client reimbursed you for, as an independent contractor, after you gave them adequate records; recreational, social or similar activities for your employees (such as a holiday party or a summer picnic); food and beverages provided to the general public as advertising or to promote goodwill; and meals you sell to the public. Don't include anything entered elsewhere on this Schedule C (for example, in cost of goods sold); zero if none"}`
- Cite: [i1040sc] p. 10, Line 24b, Amount of deduction, "However, you can fully deduct meals and incidentals furnished or reimbursed to an employee if you properly treat the expense as wages subject to withholding. You can also fully deduct meals and incidentals provided to a nonemployee to the extent the expenses are includible in the gross income of that person and reported on Form 1099-NEC" (2025; sha256 b5536db9)

## (helper) — `sc.meals_50_ded`

- **Authored helper label:** 50% of the meals subject to the 50% limit
- **Encoded (NonNegDollars):** Multiply helper "Business meals subject to the 50% limit, at their full cost" by 50% (0.50) (sc.meals_rate).
- Expr: `{"amount":"sc.meals_50","op":"multiply_rate","rate":{"param":"sc.meals_rate"}}`
- Cite: [i1040sc] p. 10, Line 24b, Amount of deduction, "you can deduct only 50% of your business meal expenses" (2025; sha256 b5536db9)

## (helper) — `sc.meals_80_ded`

- **Authored helper label:** 80% of the meals under the hours of service limits
- **Encoded (NonNegDollars):** Multiply helper "Business meals during or incident to a period of duty under the Department of Transportation hours of service limits, at their full cost" by 80% (0.80) (sc.meals_rate_dot).
- Expr: `{"amount":"sc.meals_80","op":"multiply_rate","rate":{"param":"sc.meals_rate_dot"}}`
- Cite: [i1040sc] p. 10, Line 24b, Amount of deduction (2025; sha256 b5536db9)

## 24b — `sc.line24b`

- **IRS:** Deductible meals
- **Encoded (NonNegDollars):** Add helper "50% of the meals subject to the 50% limit", helper "80% of the meals under the hours of service limits", and helper "Meals and incidentals not subject to the 50% limit, deducted in full".
- Expr: `{"of":["sc.meals_50_ded","sc.meals_80_ded","sc.meals_100"],"op":"sum"}`
- Cite: [i1040sc] p. 9, Line 24b, "Enter your deductible business meal expenses" (2025; sha256 b5536db9)

## 25 — `sc.line25`

- **IRS:** Utilities
- **Encoded (NonNegDollars):** Input — Utility expenses of the business only (for a home phone, not the base rate of the first line into your residence); zero if none
- Expr: `{"op":"input","source":"Utility expenses of the business only (for a home phone, not the base rate of the first line into your residence); zero if none"}`
- Cite: [i1040sc] p. 10, Line 25 (2025; sha256 b5536db9)

## 26 — `sc.line26`

- **IRS:** Wages (less employment credits)
- **Encoded (NonNegDollars):** Input — Salaries and wages you paid your employees in 2025 (not amounts paid to yourself, and not wages deducted elsewhere); zero if none
- Expr: `{"op":"input","source":"Salaries and wages you paid your employees in 2025 (not amounts paid to yourself, and not wages deducted elsewhere); zero if none"}`
- Cite: [i1040sc] p. 10, Line 26 (2025; sha256 b5536db9)

## 27a — `sc.line27a`

- **IRS:** Energy efficient commercial buildings deduction (attach Form 7205)
- **Encoded (NonNegDollars):** Enter the amount from helper "Zero".
- Expr: `{"from":"sc.zero","op":"copy"}`
- Cite: [i1040sc] p. 10, Line 27a (Form 7205 is refused by the screen of this Schedule C) (2025; sha256 b5536db9)

## 48 — `sc.line48`

- **IRS:** Total other expenses
- **Encoded (NonNegDollars):** Input — The total of the other business expenses you list in Part V, not included on lines 8 to 27a or line 30; zero if none
- Expr: `{"op":"input","source":"The total of the other business expenses you list in Part V, not included on lines 8 to 27a or line 30; zero if none"}`
- Cite: [f1040sc] Schedule C (2025), Part V, line 48 (2025; created 2025-04-03; sha256 ddf401db)

## 27b — `sc.line27b`

- **IRS:** Other expenses (from line 48)
- **Encoded (NonNegDollars):** Enter the amount from line 48.
- Expr: `{"from":"sc.line48","op":"copy"}`
- Cite: [f1040sc] Schedule C (2025), line 27b (2025; created 2025-04-03; sha256 ddf401db)

## 28 — `sc.line28`

- **IRS:** Total expenses before expenses for business use of home. Add lines 8 through 27b
- **Encoded (NonNegDollars):** Add line 8 (sc.line8), line 9 (sc.line9), line 10 (sc.line10), line 11, line 12 (sc.line12), line 13 (sc.line13), line 14 (sc.line14), line 15, line 16a, line 16b, line 17, line 18, line 19, line 20a, line 20b, line 21, line 22, line 23, line 24a, line 24b, line 25, line 26, line 27a, and line 27b.
- Expr: `{"of":["sc.line8","sc.line9","sc.line10","sc.line11","sc.line12","sc.line13","sc.line14","sc.line15","sc.line16a","sc.line16b","sc.line17","sc.line18","sc.line19","sc.line20a","sc.line20b","sc.line21","sc.line22","sc.line23","sc.line24a","sc.line24b","sc.line25","sc.line26","sc.line27a","sc.line27b"],"op":"sum"}`
- Cite: [f1040sc] Schedule C (2025), line 28 (2025; created 2025-04-03; sha256 ddf401db)

## 29 — `sc.line29`

- **IRS:** Tentative profit or (loss). Subtract line 28 from line 7
- **Encoded (Dollars):** Subtract line 28 from line 7 (sc.line7).
- Expr: `{"from":"sc.line7","op":"subtract","take":"sc.line28"}`
- Cite: [f1040sc] Schedule C (2025), line 29 (2025; created 2025-04-03; sha256 ddf401db)

## (helper) — `sc.line28_pre179`

- **Authored helper label:** Line 28 without the section 179 expense deduction
- **Encoded (NonNegDollars):** Add line 8 (sc.line8), line 9 (sc.line9), line 10 (sc.line10), line 11, line 12 (sc.line12), line 14 (sc.line14), line 15, line 16a, line 16b, line 17, line 18, line 19, line 20a, line 20b, line 21, line 22, line 23, line 24a, line 24b, line 25, line 26, line 27a, line 27b, and helper "Depreciation other than the section 179 deduction (Form 4562 lines 14, 17, 19 and 21)".
- Expr: `{"of":["sc.line8","sc.line9","sc.line10","sc.line11","sc.line12","sc.line14","sc.line15","sc.line16a","sc.line16b","sc.line17","sc.line18","sc.line19","sc.line20a","sc.line20b","sc.line21","sc.line22","sc.line23","sc.line24a","sc.line24b","sc.line25","sc.line26","sc.line27a","sc.line27b","sc.dep_other"],"op":"sum"}`
- Cite: [p946] pp. 17-19, Business Income Limit, Taxable income, "figure taxable income without regard to ... The section 179 deduction" (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `sc.line29_pre179`

- **Authored helper label:** Line 29 without the section 179 expense deduction
- **Encoded (Dollars):** Subtract helper "Line 28 without the section 179 expense deduction" from line 7 (sc.line7).
- Expr: `{"from":"sc.line7","op":"subtract","take":"sc.line28_pre179"}`
- Cite: [p946] pp. 17-19, Business Income Limit, Taxable income (For use in preparing 2025 returns; sha256 07fadfb2)

## (screen) — `sc.ho_uses`

- **Authored helper label:** Do you claim a deduction for business use of your home for this business?
- **Encoded (Bool):** Input — Do you claim a deduction for the business use of your home for this business (a part of your home used regularly and exclusively for the business, or regularly for storing inventory or product samples)?
- Expr: `{"op":"input","source":"Do you claim a deduction for the business use of your home for this business (a part of your home used regularly and exclusively for the business, or regularly for storing inventory or product samples)?"}`
- Cite: [i1040sc] p. 10, Line 30, Business use of your home; Pub. 587 referenced (2025; sha256 b5536db9)

## (screen) — `sc.ho_other`

- **Authored helper label:** Does any of these apply to your business use of your home for this business?
- **Encoded (Bool):** Input — Does any of these apply: you figure the deduction with actual expenses on Form 8829 instead of the simplified method; you used more than one home for this business; the home is used for daycare; you share the business area with someone else's business; you used the area for only part of 2025 or it changed during the year; some of this business's gross income is from a place of business other than your home; or you have a gain or loss on Form 8949 or Form 4797 related to this business?
- Expr: `{"op":"input","source":"Does any of these apply: you figure the deduction with actual expenses on Form 8829 instead of the simplified method; you used more than one home for this business; the home is used for daycare; you share the business area with someone else's business; you used the area for only part of 2025 or it changed during the year; some of this business's gross income is from a place of business other than your home; or you have a gain or loss on Form 8949 or Form 4797 related to this business?"}`
- Cite: [i1040sc] p. 10, Line 30; pp. 10-13, Instructions for the Simplified Method Worksheet, Daycare Facility Worksheet, Business use of more than one home, Shared use and Part-year use or area changes (2025; sha256 b5536db9)

## (gate) — `sc.ho_screened`

- **Authored helper label:** The home office deduction is outside the simplified method this tool covers
- **Encoded (Bool):** column (screen) (sc.ho_uses) = true and column (screen) (sc.ho_other) = true
- Expr: `{"all":[{"eq":["sc.ho_uses",{"const":true}],"op":"test"},{"eq":["sc.ho_other",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040sc] pp. 10-13, Line 30 and the Simplified Method Worksheet (2025; sha256 b5536db9)

## (gate) — `sc.ho_multi`

- **Authored helper label:** This person claims the business use of the home for more than one business
- **Encoded (Bool):** column (screen) (sc.ho_uses) = true and person helper "Number of this person's Schedules C that claim the business use of the home" > 1 (a count)
- Expr: `{"all":[{"eq":["sc.ho_uses",{"const":true}],"op":"test"},{"gt":["person.ho_count",{"const":1,"type":"Count"}],"op":"test"}],"op":"test"}`
- Cite: [i1040sc] p. 10, Simplified method, "If you conduct more than one business that qualifies for this deduction in your home, your election to use the simplified method applies to all your qualified business uses of your home. You are limited to a maximum of 300 square feet for all of the businesses you conduct in your home" (owner: refused) (2025; sha256 b5536db9)

## 30(b) — `sc.ho_sqft`

- **IRS:** The part of your home used for business (square feet)
- **Encoded (Count):** Input — The square feet of your home used regularly and exclusively for this business (or regularly for storing inventory or product samples) throughout 2025
- **Refusal:** when sc.ho_multi is true, cannot complete The simplified method for more than one of your businesses in your home (300 square feet allocated among them). The 300 square feet apply to all the businesses you conduct in your home together and must be allocated among them; that is outside this tool. Cite: [i1040sc] p. 10, Simplified method, "You are limited to a maximum of 300 square feet for all of the businesses you conduct in your home ... Allocate the actual square footage used (up to the maximum 300 square feet) among your qualified business uses" (2025; sha256 b5536db9)
- **Refusal:** when sc.ho_screened is true, cannot complete Form 8829, or the simplified method with daycare, shared, part-year or multiple homes. The actual-expense method (Form 8829) and the special simplified-method cases are outside this tool. Cite: [i1040sc] pp. 10-13, Line 30, the Simplified Method Worksheet and its instructions (2025; sha256 b5536db9)
- Expr: `{"op":"input","source":"The square feet of your home used regularly and exclusively for this business (or regularly for storing inventory or product samples) throughout 2025"}`
- Cite: [i1040sc] p. 12, Simplified Method Worksheet, line 2, and line 30 entry spaces; p. 10, Simplified method (2025; sha256 b5536db9)

## 30(a) — `sc.ho_home_sqft`

- **IRS:** Total square footage of your home
- **Encoded (Count):** Input — The total square footage of your home
- Expr: `{"op":"input","source":"The total square footage of your home"}`
- Cite: [f1040sc] Schedule C (2025), line 30, "Simplified method filers only: Enter the total square footage of (a) your home" (2025; created 2025-04-03; sha256 ddf401db)

## 3a — `sc.ho_rate`

- **IRS:** Maximum allowable amount (per square foot)
- **Encoded (NonNegDollars):** Enter $5 (sc.ho_rate).
- Expr: `{"op":"param","ref":"sc.ho_rate"}`
- Cite: [i1040sc] p. 12, Simplified Method Worksheet, line 3a, "$5" (2025; sha256 b5536db9)

## (helper) — `sc.ho_cap_sqft`

- **Authored helper label:** Square feet not to be exceeded on line 2
- **Encoded (Count):** Enter 300 (sc.ho_max_sqft).
- Expr: `{"op":"param","ref":"sc.ho_max_sqft"}`
- Cite: [i1040sc] p. 12, Simplified Method Worksheet, line 2, "Don't enter more than 300 square feet" (2025; sha256 b5536db9)

## (helper) — `sc.ho_over`

- **Authored helper label:** More than 300 square feet
- **Encoded (Bool):** line 30(b) > helper "Square feet not to be exceeded on line 2"
- Expr: `{"gt":["sc.ho_sqft","sc.ho_cap_sqft"],"op":"test"}`
- Cite: [i1040sc] p. 12, Simplified Method Worksheet, line 2 (2025; sha256 b5536db9)

## (helper) — `sc.ho_line4_actual`

- **Authored helper label:** Line 2 (the square feet used) times line 3c
- **Encoded (NonNegDollars):** Multiply line 3a by the number on line 30(b).
- Expr: `{"amount":"sc.ho_rate","count":"sc.ho_sqft","op":"multiply_count"}`
- Cite: [i1040sc] p. 12, Simplified Method Worksheet, lines 3c and 4 (line 3b is 1.0 without daycare) (2025; sha256 b5536db9)

## (helper) — `sc.ho_line4_cap`

- **Authored helper label:** 300 square feet times line 3c
- **Encoded (NonNegDollars):** Multiply line 3a by the number on helper "Square feet not to be exceeded on line 2".
- Expr: `{"amount":"sc.ho_rate","count":"sc.ho_cap_sqft","op":"multiply_count"}`
- Cite: [i1040sc] p. 12, Simplified Method Worksheet, lines 2 to 4 (2025; sha256 b5536db9)

## 4 — `sc.ho_line4`

- **IRS:** Multiply line 2 by line 3c
- **Encoded (NonNegDollars):** Choose — [helper "More than 300 square feet" = false → helper "Line 2 (the square feet used) times line 3c"] [helper "More than 300 square feet" = true → helper "300 square feet times line 3c"]
- Expr: `{"alternatives":[{"guard":{"eq":["sc.ho_over",{"const":false}],"op":"test"},"then":"sc.ho_line4_actual"},{"guard":{"eq":["sc.ho_over",{"const":true}],"op":"test"},"then":"sc.ho_line4_cap"}],"op":"choose"}`
- Cite: [i1040sc] p. 12, Simplified Method Worksheet, line 4, with line 2 not more than 300 square feet (2025; sha256 b5536db9)

## 1 — `sc.ho_line1`

- **IRS:** Gross income limitation (Schedule C, line 29)
- **Encoded (Dollars):** Enter the amount from line 29.
- Expr: `{"from":"sc.line29","op":"copy"}`
- Cite: [i1040sc] p. 11, Instructions for the Simplified Method Worksheet, Line 1, A to E ("Enter the amount from Schedule C, line 29"; lines B and D are zero under the screen) (2025; sha256 b5536db9)

## (helper) — `sc.ho_room`

- **Authored helper label:** Line 29 without the section 179 deduction, less the most section 179 deduction the business could take
- **Encoded (Dollars):** Subtract helper "The most section 179 deduction this business could take, its 2025 elections plus the carryover from 2024 (Form 4562 line 10)" from helper "Line 29 without the section 179 expense deduction".
- Expr: `{"from":"sc.line29_pre179","op":"subtract","take":"sc.ho_s179_max"}`
- Cite: [p946] p. 19, Business Income Limit, Two different taxable income limits (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `sc.ho_unlimited`

- **Authored helper label:** Line 4 is not more than the smallest line 29 any section 179 allocation could give
- **Encoded (Bool):** line 4 (sc.ho_line4) ≤ helper "Line 29 without the section 179 deduction, less the most section 179 deduction the business could take"
- Expr: `{"le":["sc.ho_line4","sc.ho_room"],"op":"test"}`
- Cite: [p946] p. 19, Business Income Limit, Two different taxable income limits (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `sc.ho_s179_max`

- **Authored helper label:** The most section 179 deduction this business could take, its 2025 elections plus the carryover from 2024 (Form 4562 line 10)
- **Encoded (NonNegDollars):** Add helper "Section 179 elected for this business's 2025 property" and s179 line 10.
- Expr: `{"of":["sc.s179_elected","s179.line10"],"op":"sum"}`
- Cite: [f4562] Form 4562 (2025), line 12, "Add lines 9 and 10, but don’t enter more than line 11" (2025; created 2025-10-09; sha256 c05f9d1f)

## (helper) — `sc.ho_no179`

- **Authored helper label:** No section 179 deduction is possible for this business (no 2025 election and no carryover)
- **Encoded (Bool):** helper "The most section 179 deduction this business could take, its 2025 elections plus the carryover from 2024 (Form 4562 line 10)" = $0
- Expr: `{"eq":["sc.ho_s179_max",{"const":0}],"op":"test"}`
- Cite: [p946] p. 19, Business Income Limit, Two different taxable income limits (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `sc.ho_limited`

- **Authored helper label:** The smaller of line 1 or line 4, with no section 179 election (line 1 is line 29 without the section 179 deduction)
- **Encoded (NonNegDollars):** Enter the smaller of line 4 (sc.ho_line4) or helper "Line 29 without the section 179 deduction, if zero or less zero".
- Expr: `{"of":["sc.ho_line4","sc.ho_pre179_floor"],"op":"smaller_of"}`
- Cite: [i1040sc] p. 12, Simplified Method Worksheet, line 5, "Enter the smaller of line 1 or line 4 ... If zero or less, enter -0-" (2025; sha256 b5536db9)

## (helper) — `sc.ho_pre179_floor`

- **Authored helper label:** Line 29 without the section 179 deduction, if zero or less zero
- **Encoded (NonNegDollars):** Subtract helper "Zero" from helper "Line 29 without the section 179 expense deduction". If zero or less, enter -0-.
- Expr: `{"from":"sc.line29_pre179","op":"subtract_floor0","take":"sc.zero"}`
- Cite: [i1040sc] p. 12, Simplified Method Worksheet, line 5, "If zero or less, enter -0-" (2025; sha256 b5536db9)

## (gate) — `sc.ho_both_limits`

- **Authored helper label:** The gross income limitation could bind together with the section 179 business income limit
- **Encoded (Bool):** helper "Line 4 is not more than the smallest line 29 any section 179 allocation could give" = false and helper "No section 179 deduction is possible for this business (no 2025 election and no carryover)" = false
- Expr: `{"all":[{"eq":["sc.ho_unlimited",{"const":false}],"op":"test"},{"eq":["sc.ho_no179",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [p946] p. 19, Business Income Limit, Two different taxable income limits, Steps 1 to 8 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `sc.ho_both`

- **Authored helper label:** Line 5 when both income limits could bind
- **Encoded (NonNegDollars):** Enter the amount from helper "Zero".
- **Refusal:** when sc.ho_both_limits is true, cannot complete Section 179 deduction with a home office deduction limited by gross income (Pub. 946, two different taxable income limits). Figuring two income-based limits in the order of Pub. 946 is outside this tool. Cite: [p946] p. 19, Business Income Limit, Two different taxable income limits, Steps 1 to 8 (For use in preparing 2025 returns; sha256 07fadfb2)
- Expr: `{"from":"sc.zero","op":"copy"}`
- Cite: [p946] p. 19, Business Income Limit, Two different taxable income limits (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `sc.ho_line5_lim`

- **Authored helper label:** Line 5 when line 4 is more than the room left by the section 179 elections
- **Encoded (NonNegDollars):** Choose — [helper "No section 179 deduction is possible for this business (no 2025 election and no carryover)" = true → helper "The smaller of line 1 or line 4, with no section 179 election (line 1 is line 29 without the section 179 deduction)"] [helper "No section 179 deduction is possible for this business (no 2025 election and no carryover)" = false → helper "Line 5 when both income limits could bind"]
- Expr: `{"alternatives":[{"guard":{"eq":["sc.ho_no179",{"const":true}],"op":"test"},"then":"sc.ho_limited"},{"guard":{"eq":["sc.ho_no179",{"const":false}],"op":"test"},"then":"sc.ho_both"}],"op":"choose"}`
- Cite: [i1040sc] p. 12, Simplified Method Worksheet, line 5; p946 p. 19, Business Income Limit, Two different taxable income limits (2025; sha256 b5536db9)

## 5 — `sc.ho_line5`

- **IRS:** Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4
- **Encoded (NonNegDollars):** Choose — [helper "Line 4 is not more than the smallest line 29 any section 179 allocation could give" = true → line 4 (sc.ho_line4)] [helper "Line 4 is not more than the smallest line 29 any section 179 allocation could give" = false → helper "Line 5 when line 4 is more than the room left by the section 179 elections"]
- Expr: `{"alternatives":[{"guard":{"eq":["sc.ho_unlimited",{"const":true}],"op":"test"},"then":"sc.ho_line4"},{"guard":{"eq":["sc.ho_unlimited",{"const":false}],"op":"test"},"then":"sc.ho_line5_lim"}],"op":"choose"}`
- Cite: [i1040sc] p. 12, Simplified Method Worksheet, line 5 (2025; sha256 b5536db9)

## 30 — `sc.line30`

- **IRS:** Expenses for business use of your home
- **Encoded (NonNegDollars):** Choose — [column (screen) (sc.ho_uses) = true → line 5 (sc.ho_line5)] [column (screen) (sc.ho_uses) = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["sc.ho_uses",{"const":true}],"op":"test"},"then":"sc.ho_line5"},{"guard":{"eq":["sc.ho_uses",{"const":false}],"op":"test"},"then":"sc.zero"}],"op":"choose"}`
- Cite: [i1040sc] p. 14, Reporting your expenses for business use of the home, "Include the amount from line 5 of the Simplified Method Worksheet on line 30" (2025; sha256 b5536db9)

## 31 — `sc.line31`

- **IRS:** Net profit or (loss). Subtract line 30 from line 29
- **Encoded (Dollars):** Subtract line 30 from line 29.
- Expr: `{"from":"sc.line29","op":"subtract","take":"sc.line30"}`
- Cite: [f1040sc] Schedule C (2025), line 31 (2025; created 2025-04-03; sha256 ddf401db)

## (helper) — `sc.line31_pre179`

- **Authored helper label:** Line 31 without the section 179 expense deduction
- **Encoded (Dollars):** Subtract line 30 from helper "Line 29 without the section 179 expense deduction".
- Expr: `{"from":"sc.line29_pre179","op":"subtract","take":"sc.line30"}`
- Cite: [p946] pp. 17-19, Business Income Limit, Taxable income (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `sc.loss`

- **Authored helper label:** Line 31 is a loss
- **Encoded (Bool):** line 31 < helper "Zero"
- Expr: `{"lt":["sc.line31","sc.zero"],"op":"test"}`
- Cite: [i1040sc] p. 14, Line 31, "If your expenses ... are more than your gross income"; p. 14, Line 32, "At-risk rules. In most cases, if you have a business loss and amounts invested in the business for which you are not at risk" (2025; sha256 b5536db9)

## 32 — `sc.at_risk`

- **IRS:** If you have a loss, is all your investment in this business at risk (box 32a)?
- **Encoded (Bool):** Input — All your investment in this business is at risk: you have no nonrecourse loans not secured by your own property, no amounts protected against loss by a guarantee or stop-loss agreement, and no amounts borrowed from someone with an interest in the business (box 32a)
- Expr: `{"op":"input","source":"All your investment in this business is at risk: you have no nonrecourse loans not secured by your own property, no amounts protected against loss by a guarantee or stop-loss agreement, and no amounts borrowed from someone with an interest in the business (box 32a)"}`
- Cite: [i1040sc] pp. 14-15, Line 32, At-risk rules and Figuring your loss (2025; sha256 b5536db9)

## (gate) — `sc.not_at_risk`

- **Authored helper label:** Some investment is not at risk (box 32b)
- **Encoded (Bool):** line 32 = false
- Expr: `{"eq":["sc.at_risk",{"const":false}],"op":"test"}`
- Cite: [i1040sc] p. 15, Line 32, Some investment is not at risk (2025; sha256 b5536db9)

## (helper) — `sc.loss_allowed`

- **Authored helper label:** The loss on line 31 when all investment is at risk
- **Encoded (Dollars):** Enter the amount from line 31.
- **Refusal:** when sc.not_at_risk is true, cannot complete Form 6198 (At-Risk Limitations). A loss with amounts not at risk is outside this tool. Cite: [i1040sc] p. 15, Line 32, Some investment is not at risk, "Be sure to attach Form 6198" (2025; sha256 b5536db9)
- Expr: `{"from":"sc.line31","op":"copy"}`
- Cite: [i1040sc] p. 15, Line 32, All investment is at risk, "your loss will not be reduced by the at-risk rules or the passive activity loss rules" (2025; sha256 b5536db9)

## (helper) — `sc.result`

- **Authored helper label:** The amount for Schedule 1, line 3 and Schedule SE, line 2
- **Encoded (Dollars):** Choose — [helper "Line 31 is a loss" = false → line 31] [helper "Line 31 is a loss" = true → helper "The loss on line 31 when all investment is at risk"]
- Expr: `{"alternatives":[{"guard":{"eq":["sc.loss",{"const":false}],"op":"test"},"then":"sc.line31"},{"guard":{"eq":["sc.loss",{"const":true}],"op":"test"},"then":"sc.loss_allowed"}],"op":"choose"}`
- Cite: [i1040sc] p. 14, Line 31, Individuals, "Enter your net profit or loss on line 31 and include it on Schedule 1 (Form 1040), line 3. Also, include your net profit or loss on Schedule SE (Form 1040), line 2" (2025; sha256 b5536db9)

## 33 — `sc.inventory_other`

- **IRS:** Method used to value closing inventory: other than cost or lower of cost or market, or a change between opening and closing inventory (line 34)?
- **Encoded (Bool):** Input — Do you value closing inventory by a method other than cost or lower of cost or market, or was there any change in determining quantities, costs or valuations between opening and closing inventory (line 34)? Answer No if you have no inventory
- Expr: `{"op":"input","source":"Do you value closing inventory by a method other than cost or lower of cost or market, or was there any change in determining quantities, costs or valuations between opening and closing inventory (line 34)? Answer No if you have no inventory"}`
- Cite: [i1040sc] p. 15, Part III, Line 33; Schedule C (2025), lines 33 and 34 (2025; sha256 b5536db9)

## 35 — `sc.line35`

- **IRS:** Inventory at beginning of year
- **Encoded (NonNegDollars):** Input — Inventory at the beginning of 2025 (the same as your closing inventory for 2024); zero if none
- **Refusal:** when sc.inventory_other is true, cannot complete Schedule C, Part III, other inventory methods or a change in valuation. Inventory valued other than at cost or lower of cost or market, or changed between opening and closing, is outside this tool. Cite: [i1040sc] p. 15, Lines 33 and 35 (2025; sha256 b5536db9)
- Expr: `{"op":"input","source":"Inventory at the beginning of 2025 (the same as your closing inventory for 2024); zero if none"}`
- Cite: [i1040sc] p. 15, Line 35 (2025; sha256 b5536db9)

## 36 — `sc.line36`

- **IRS:** Purchases less cost of items withdrawn for personal use
- **Encoded (NonNegDollars):** Input — Purchases of merchandise or materials for sale, less the cost of items you withdrew for personal use; zero if none
- Expr: `{"op":"input","source":"Purchases of merchandise or materials for sale, less the cost of items you withdrew for personal use; zero if none"}`
- Cite: [f1040sc] Schedule C (2025), line 36 (2025; created 2025-04-03; sha256 ddf401db)

## 37 — `sc.line37`

- **IRS:** Cost of labor
- **Encoded (NonNegDollars):** Input — Cost of labor for producing goods for sale (not amounts paid to yourself); zero if none
- Expr: `{"op":"input","source":"Cost of labor for producing goods for sale (not amounts paid to yourself); zero if none"}`
- Cite: [f1040sc] Schedule C (2025), line 37 (2025; created 2025-04-03; sha256 ddf401db)

## 38 — `sc.line38`

- **IRS:** Materials and supplies
- **Encoded (NonNegDollars):** Input — Materials and supplies used in producing goods for sale; zero if none
- Expr: `{"op":"input","source":"Materials and supplies used in producing goods for sale; zero if none"}`
- Cite: [f1040sc] Schedule C (2025), line 38 (2025; created 2025-04-03; sha256 ddf401db)

## 39 — `sc.line39`

- **IRS:** Other costs
- **Encoded (NonNegDollars):** Input — Other costs of goods sold; zero if none
- Expr: `{"op":"input","source":"Other costs of goods sold; zero if none"}`
- Cite: [f1040sc] Schedule C (2025), line 39 (2025; created 2025-04-03; sha256 ddf401db)

## 40 — `sc.line40`

- **IRS:** Add lines 35 through 39
- **Encoded (NonNegDollars):** Add line 35, line 36, line 37, line 38, and line 39.
- Expr: `{"of":["sc.line35","sc.line36","sc.line37","sc.line38","sc.line39"],"op":"sum"}`
- Cite: [f1040sc] Schedule C (2025), line 40 (2025; created 2025-04-03; sha256 ddf401db)

## 41 — `sc.line41`

- **IRS:** Inventory at end of year
- **Encoded (NonNegDollars):** Input — Inventory at the end of 2025; zero if none
- Expr: `{"op":"input","source":"Inventory at the end of 2025; zero if none"}`
- Cite: [f1040sc] Schedule C (2025), line 41 (2025; created 2025-04-03; sha256 ddf401db)

## 42 — `sc.line42`

- **IRS:** Cost of goods sold. Subtract line 41 from line 40
- **Encoded (Dollars):** Subtract line 41 from line 40.
- Expr: `{"from":"sc.line40","op":"subtract","take":"sc.line41"}`
- Cite: [f1040sc] Schedule C (2025), line 42 (2025; created 2025-04-03; sha256 ddf401db)

## (helper) — `sc.f6`

- **Authored helper label:** Section 179 elected on property other than listed property
- **Encoded (NonNegDollars):** Add asset.s179_2025 over every confirmed asset entry for which helper "Is this listed property?" = false, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"asset","field":"asset.s179_2025","op":"sum_over","where":{"eq":["asset.listed",{"const":false}],"op":"test"}}`
- Cite: [i4562] p. 5, Line 6 (2025; sha256 5c1c95b7)

## (helper) — `sc.f14`

- **Authored helper label:** Special allowance on property other than listed property
- **Encoded (NonNegDollars):** Add asset.bonus_2025 over every confirmed asset entry for which helper "Is this listed property?" = false, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"asset","field":"asset.bonus_2025","op":"sum_over","where":{"eq":["asset.listed",{"const":false}],"op":"test"}}`
- Cite: [i4562] p. 5, Line 14 (2025; sha256 5c1c95b7)

## (helper) — `sc.f17`

- **Authored helper label:** MACRS on earlier property other than listed property
- **Encoded (NonNegDollars):** Add asset.dep_prior over every confirmed asset entry for which helper "Is this listed property?" = false, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"asset","field":"asset.dep_prior","op":"sum_over","where":{"eq":["asset.listed",{"const":false}],"op":"test"}}`
- Cite: [i4562] p. 9, Line 17 (2025; sha256 5c1c95b7)

## (helper) — `sc.f19_y3`

- **Authored helper label:** MACRS on 2025 property of period y3 other than listed property
- **Encoded (NonNegDollars):** Add asset.dep_2025 over every confirmed asset entry for which helper "Is this listed property?" = false and column (d) = 'y3', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"asset","field":"asset.dep_2025","op":"sum_over","where":{"all":[{"eq":["asset.listed",{"const":false}],"op":"test"},{"eq":["asset.period",{"const":"y3"}],"op":"test"}],"op":"test"}}`
- Cite: [i4562] pp. 9-10, Lines 19a Through 19j, Column (a)—Classification of property (2025; sha256 5c1c95b7)

## (helper) — `sc.f19_y5`

- **Authored helper label:** MACRS on 2025 property of period y5 other than listed property
- **Encoded (NonNegDollars):** Add asset.dep_2025 over every confirmed asset entry for which helper "Is this listed property?" = false and column (d) = 'y5', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"asset","field":"asset.dep_2025","op":"sum_over","where":{"all":[{"eq":["asset.listed",{"const":false}],"op":"test"},{"eq":["asset.period",{"const":"y5"}],"op":"test"}],"op":"test"}}`
- Cite: [i4562] pp. 9-10, Lines 19a Through 19j, Column (a)—Classification of property (2025; sha256 5c1c95b7)

## (helper) — `sc.f19_y7`

- **Authored helper label:** MACRS on 2025 property of period y7 other than listed property
- **Encoded (NonNegDollars):** Add asset.dep_2025 over every confirmed asset entry for which helper "Is this listed property?" = false and column (d) = 'y7', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"asset","field":"asset.dep_2025","op":"sum_over","where":{"all":[{"eq":["asset.listed",{"const":false}],"op":"test"},{"eq":["asset.period",{"const":"y7"}],"op":"test"}],"op":"test"}}`
- Cite: [i4562] pp. 9-10, Lines 19a Through 19j, Column (a)—Classification of property (2025; sha256 5c1c95b7)

## (helper) — `sc.f19_y10`

- **Authored helper label:** MACRS on 2025 property of period y10 other than listed property
- **Encoded (NonNegDollars):** Add asset.dep_2025 over every confirmed asset entry for which helper "Is this listed property?" = false and column (d) = 'y10', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"asset","field":"asset.dep_2025","op":"sum_over","where":{"all":[{"eq":["asset.listed",{"const":false}],"op":"test"},{"eq":["asset.period",{"const":"y10"}],"op":"test"}],"op":"test"}}`
- Cite: [i4562] pp. 9-10, Lines 19a Through 19j, Column (a)—Classification of property (2025; sha256 5c1c95b7)

## (helper) — `sc.f19_y15`

- **Authored helper label:** MACRS on 2025 property of period y15 other than listed property
- **Encoded (NonNegDollars):** Add asset.dep_2025 over every confirmed asset entry for which helper "Is this listed property?" = false and column (d) = 'y15', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"asset","field":"asset.dep_2025","op":"sum_over","where":{"all":[{"eq":["asset.listed",{"const":false}],"op":"test"},{"eq":["asset.period",{"const":"y15"}],"op":"test"}],"op":"test"}}`
- Cite: [i4562] pp. 9-10, Lines 19a Through 19j, Column (a)—Classification of property (2025; sha256 5c1c95b7)

## (helper) — `sc.f19_y20`

- **Authored helper label:** MACRS on 2025 property of period y20 other than listed property
- **Encoded (NonNegDollars):** Add asset.dep_2025 over every confirmed asset entry for which helper "Is this listed property?" = false and column (d) = 'y20', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"asset","field":"asset.dep_2025","op":"sum_over","where":{"all":[{"eq":["asset.listed",{"const":false}],"op":"test"},{"eq":["asset.period",{"const":"y20"}],"op":"test"}],"op":"test"}}`
- Cite: [i4562] pp. 9-10, Lines 19a Through 19j, Column (a)—Classification of property (2025; sha256 5c1c95b7)

## (helper) — `sc.f19_y15sl`

- **Authored helper label:** MACRS on 2025 property of period y15sl other than listed property
- **Encoded (NonNegDollars):** Add asset.dep_2025 over every confirmed asset entry for which helper "Is this listed property?" = false and column (d) = 'y15sl', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"asset","field":"asset.dep_2025","op":"sum_over","where":{"all":[{"eq":["asset.listed",{"const":false}],"op":"test"},{"eq":["asset.period",{"const":"y15sl"}],"op":"test"}],"op":"test"}}`
- Cite: [i4562] pp. 9-10, Lines 19a Through 19j, Column (a)—Classification of property (2025; sha256 5c1c95b7)

## (helper) — `sc.f25_assets`

- **Authored helper label:** Special allowance on listed property other than vehicles
- **Encoded (NonNegDollars):** Add asset.bonus_2025 over every confirmed asset entry for which helper "Is this listed property?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"asset","field":"asset.bonus_2025","op":"sum_over","where":{"eq":["asset.listed",{"const":true}],"op":"test"}}`
- Cite: [i4562] p. 13, Line 25 (2025; sha256 5c1c95b7)

## (helper) — `sc.f25_veh`

- **Authored helper label:** Special allowance on vehicles
- **Encoded (NonNegDollars):** Add scveh.bonus over every confirmed scveh entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"scveh","field":"scveh.bonus","op":"sum_over"}`
- Cite: [i4562] p. 13, Line 25 (2025; sha256 5c1c95b7)

## (helper) — `sc.f25`

- **Authored helper label:** Line 25 for this business
- **Encoded (NonNegDollars):** Add helper "Special allowance on listed property other than vehicles" and helper "Special allowance on vehicles".
- Expr: `{"of":["sc.f25_assets","sc.f25_veh"],"op":"sum"}`
- Cite: [i4562] p. 13, Line 25 (2025; sha256 5c1c95b7)

## (helper) — `sc.f26_assets`

- **Authored helper label:** Column (h) of listed property other than vehicles
- **Encoded (NonNegDollars):** Add asset.dep_listed over every confirmed asset entry for which helper "Is this listed property?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"asset","field":"asset.dep_listed","op":"sum_over","where":{"eq":["asset.listed",{"const":true}],"op":"test"}}`
- Cite: [i4562] p. 15, Column (h) (2025; sha256 5c1c95b7)

## (helper) — `sc.f26_veh`

- **Authored helper label:** Column (h) of vehicles
- **Encoded (NonNegDollars):** Add scveh.macrs over every confirmed scveh entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"scveh","field":"scveh.macrs","op":"sum_over"}`
- Cite: [i4562] p. 15, Column (h) (2025; sha256 5c1c95b7)

## (helper) — `sc.f26h`

- **Authored helper label:** Column (h), line 26, for this business
- **Encoded (NonNegDollars):** Add helper "Column (h) of listed property other than vehicles" and helper "Column (h) of vehicles".
- Expr: `{"of":["sc.f26_assets","sc.f26_veh"],"op":"sum"}`
- Cite: [i4562] p. 15, Column (h) (2025; sha256 5c1c95b7)

## (helper) — `sc.f28`

- **Authored helper label:** Line 28 for this business
- **Encoded (NonNegDollars):** Add helper "Line 25 for this business" and helper "Column (h), line 26, for this business".
- Expr: `{"of":["sc.f25","sc.f26h"],"op":"sum"}`
- Cite: [f4562] p. 2, Part V, "Add amounts in column (h), lines 25 through 27. Enter here and on line 21" (line 28) (2025; created 2025-10-09; sha256 c05f9d1f)

## (helper) — `sc.f29_assets`

- **Authored helper label:** Section 179 elected on listed property other than vehicles
- **Encoded (NonNegDollars):** Add asset.s179_2025 over every confirmed asset entry for which helper "Is this listed property?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"asset","field":"asset.s179_2025","op":"sum_over","where":{"eq":["asset.listed",{"const":true}],"op":"test"}}`
- Cite: [i4562] p. 16, Column (i) (2025; sha256 5c1c95b7)

## (helper) — `sc.f29_veh`

- **Authored helper label:** Section 179 on vehicles
- **Encoded (NonNegDollars):** Add scveh.s179_2025 over every confirmed scveh entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"scveh","field":"scveh.s179_2025","op":"sum_over"}`
- Cite: [i4562] p. 16, Column (i) (2025; sha256 5c1c95b7)

## (helper) — `sc.f29`

- **Authored helper label:** Line 29 for this business
- **Encoded (NonNegDollars):** Add helper "Section 179 elected on listed property other than vehicles" and helper "Section 179 on vehicles".
- Expr: `{"of":["sc.f29_assets","sc.f29_veh"],"op":"sum"}`
- Cite: [f4562] p. 2, Part V, "Add amounts in column (i), line 26. Enter here and on line 7" (line 29) (2025; created 2025-10-09; sha256 c05f9d1f)

## (helper) — `sc.s179_elected`

- **Authored helper label:** Section 179 elected for this business's 2025 property
- **Encoded (NonNegDollars):** Add helper "Section 179 elected on property other than listed property" and helper "Line 29 for this business".
- Expr: `{"of":["sc.f6","sc.f29"],"op":"sum"}`
- Cite: [i4562] p. 5, Lines 6 to 8 (2025; sha256 5c1c95b7)

## (helper) — `sc.dep_other`

- **Authored helper label:** Depreciation other than the section 179 deduction (Form 4562 lines 14, 17, 19 and 21)
- **Encoded (NonNegDollars):** Add helper "Special allowance on property other than listed property", helper "MACRS on earlier property other than listed property", helper "MACRS on 2025 property of period y3 other than listed property", helper "MACRS on 2025 property of period y5 other than listed property", helper "MACRS on 2025 property of period y7 other than listed property", helper "MACRS on 2025 property of period y10 other than listed property", helper "MACRS on 2025 property of period y15 other than listed property", helper "MACRS on 2025 property of period y20 other than listed property", helper "MACRS on 2025 property of period y15sl other than listed property", and helper "Line 28 for this business".
- Expr: `{"of":["sc.f14","sc.f17","sc.f19_y3","sc.f19_y5","sc.f19_y7","sc.f19_y10","sc.f19_y15","sc.f19_y20","sc.f19_y15sl","sc.f28"],"op":"sum"}`
- Cite: [f4562] p. 2, Part IV, "Total. Add amounts from line 12, lines 14 through 17, lines 19 and 20 in column (g), and line 21" (line 22, less line 12) (2025; created 2025-10-09; sha256 c05f9d1f)

## (helper) — `sc.s179_return`

- **Authored helper label:** The return's section 179 deduction, for its only Schedule C
- **Encoded (NonNegDollars):** Enter the amount from s179 line 12.
- **Refusal:** when s179.multi is true, cannot complete Section 179 deduction to allocate among more than one business. Allocating a limited or carried-over section 179 deduction among businesses is outside this tool. Cite: [i4562] p. 5, Line 12 (2025; sha256 5c1c95b7)
- Expr: `{"from":"s179.line12","op":"copy"}`
- Cite: [i4562] p. 5, Line 12 (2025; sha256 5c1c95b7)

## 12 — `sc.s179_allowed`

- **IRS:** Section 179 expense deduction for this business
- **Encoded (NonNegDollars):** Choose — [s179 helper "The deduction differs from the amounts elected for 2025" = false → helper "Section 179 elected for this business's 2025 property"] [s179 helper "The deduction differs from the amounts elected for 2025" = true → helper "The return's section 179 deduction, for its only Schedule C"]
- Expr: `{"alternatives":[{"guard":{"eq":["s179.differs",{"const":false}],"op":"test"},"then":"sc.s179_elected"},{"guard":{"eq":["s179.differs",{"const":true}],"op":"test"},"then":"sc.s179_return"}],"op":"choose"}`
- Cite: [i4562] p. 5, Line 12 (2025; sha256 5c1c95b7)

## (helper) — `sc.mq_q4_a`

- **Authored helper label:** mq_q4 of this business's property
- **Encoded (NonNegDollars):** Add asset.mq_q4 over every confirmed asset entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"asset","field":"asset.mq_q4","op":"sum_over"}`
- Cite: [p946] p. 34, Which Convention Applies?; i4562 p. 4, Line 2 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `sc.mq_q4_v`

- **Authored helper label:** mq_q4 of this business's vehicles
- **Encoded (NonNegDollars):** Add scveh.mq_q4 over every confirmed scveh entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"scveh","field":"scveh.mq_q4","op":"sum_over"}`
- Cite: [p946] p. 34, Which Convention Applies?; i4562 p. 4, Line 2 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `sc.mq_q4`

- **Authored helper label:** mq_q4 of this business
- **Encoded (NonNegDollars):** Add helper "mq_q4 of this business's property" and helper "mq_q4 of this business's vehicles".
- Expr: `{"of":["sc.mq_q4_a","sc.mq_q4_v"],"op":"sum"}`
- Cite: [p946] p. 34, Which Convention Applies?; i4562 p. 4, Line 2 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `sc.mq_total_a`

- **Authored helper label:** mq_total of this business's property
- **Encoded (NonNegDollars):** Add asset.mq_total over every confirmed asset entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"asset","field":"asset.mq_total","op":"sum_over"}`
- Cite: [p946] p. 34, Which Convention Applies?; i4562 p. 4, Line 2 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `sc.mq_total_v`

- **Authored helper label:** mq_total of this business's vehicles
- **Encoded (NonNegDollars):** Add scveh.mq_total over every confirmed scveh entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"scveh","field":"scveh.mq_total","op":"sum_over"}`
- Cite: [p946] p. 34, Which Convention Applies?; i4562 p. 4, Line 2 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `sc.mq_total`

- **Authored helper label:** mq_total of this business
- **Encoded (NonNegDollars):** Add helper "mq_total of this business's property" and helper "mq_total of this business's vehicles".
- Expr: `{"of":["sc.mq_total_a","sc.mq_total_v"],"op":"sum"}`
- Cite: [p946] p. 34, Which Convention Applies?; i4562 p. 4, Line 2 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `sc.cost179_a`

- **Authored helper label:** cost179 of this business's property
- **Encoded (NonNegDollars):** Add asset.cost179 over every confirmed asset entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"asset","field":"asset.cost179","op":"sum_over"}`
- Cite: [p946] p. 34, Which Convention Applies?; i4562 p. 4, Line 2 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `sc.cost179_v`

- **Authored helper label:** cost179 of this business's vehicles
- **Encoded (NonNegDollars):** Add scveh.cost179 over every confirmed scveh entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"scveh","field":"scveh.cost179","op":"sum_over"}`
- Cite: [p946] p. 34, Which Convention Applies?; i4562 p. 4, Line 2 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `sc.cost179`

- **Authored helper label:** cost179 of this business
- **Encoded (NonNegDollars):** Add helper "cost179 of this business's property" and helper "cost179 of this business's vehicles".
- Expr: `{"of":["sc.cost179_a","sc.cost179_v"],"op":"sum"}`
- Cite: [p946] p. 34, Which Convention Applies?; i4562 p. 4, Line 2 (For use in preparing 2025 returns; sha256 07fadfb2)

## (helper) — `sc.rent_equipment`

- **Authored helper label:** Rent or lease of machinery and equipment, and of vehicles not entered as vehicles
- **Encoded (NonNegDollars):** Input — The business part of rent for machinery and equipment (and for any vehicle you rented for a term of less than 30 days and do not enter as a vehicle); zero if none
- Expr: `{"op":"input","source":"The business part of rent for machinery and equipment (and for any vehicle you rented for a term of less than 30 days and do not enter as a vehicle); zero if none"}`
- Cite: [i1040sc] p. 8, Lines 20a and 20b (2025; sha256 b5536db9)

## (helper) — `sc.veh_lease`

- **Authored helper label:** Business part of vehicle lease payments
- **Encoded (NonNegDollars):** Add scveh.line20a over every confirmed scveh entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"scveh","field":"scveh.line20a","op":"sum_over"}`
- Cite: [i1040sc] p. 8, Lines 20a and 20b (2025; sha256 b5536db9)

## (helper) — `sc.profit_pos`

- **Authored helper label:** Net profit of this business (zero for a loss)
- **Encoded (NonNegDollars):** Subtract helper "Zero" from helper "The amount for Schedule 1, line 3 and Schedule SE, line 2". If zero or less, enter -0-.
- Expr: `{"from":"sc.result","op":"subtract_floor0","take":"sc.zero"}`
- Cite: [f7206] p. 1, "Enter your net profit* and any other earned income** from the trade or business under which the insurance plan is established" (line 4), "Don’t include any net losses shown on these schedules" (line 5) (2025; created 2025-10-02; sha256 822203c9)

## (screen) — `sc.hi_uses`

- **Authored helper label:** Health insurance established under this business
- **Encoded (Bool):** Input — Did you pay for health insurance for 2025 (for you, your spouse, your dependents, or your child under age 27 at the end of 2025) that is established under this business: a policy in the name of the business or in your own name?
- Expr: `{"op":"input","source":"Did you pay for health insurance for 2025 (for you, your spouse, your dependents, or your child under age 27 at the end of 2025) that is established under this business: a policy in the name of the business or in your own name?"}`
- Cite: [i1040gi] pp. 94–95, Schedule 1, line 17, "The insurance plan must be established under your business ... the policy can be either in your name or in the name of the business" (2025; printed date 2026-02-25; sha256 482e9c48)

## (screen) — `sc.hi_screen`

- **Authored helper label:** Does any of these apply to this health insurance?
- **Encoded (Bool):** Input — Does any of these apply: the insurance was obtained through the Marketplace and advance payments of the premium tax credit were made or you are claiming the premium tax credit; you file Form 2555; you were a more-than-2% shareholder of an S corporation; you used an optional method for net earnings from self-employment; you are a retired public safety officer who paid premiums from retirement plan distributions; or anyone is covered by qualified long-term care insurance entered for more than one business on this return (yours or your spouse's)?
- Expr: `{"op":"input","source":"Does any of these apply: the insurance was obtained through the Marketplace and advance payments of the premium tax credit were made or you are claiming the premium tax credit; you file Form 2555; you were a more-than-2% shareholder of an S corporation; you used an optional method for net earnings from self-employment; you are a retired public safety officer who paid premiums from retirement plan distributions; or anyone is covered by qualified long-term care insurance entered for more than one business on this return (yours or your spouse's)?"}`
- Cite: [i1040gi] p. 95, Schedule 1, line 17, Exceptions, "Use Pub. 974 instead of the worksheet ... if the insurance plan ... was obtained through the Marketplace, and advance payments of the premium tax credit were made or you are claiming the premium tax credit"; i7206 pp. 1–2, "the total of the amounts entered for each person on line 2 of all Form(s) 7206 can’t be more than the appropriate limit shown on line 2 for that person" (refused, owner ruling) (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `sc.hi_screened`

- **Authored helper label:** This health insurance deduction is outside this tool
- **Encoded (Bool):** column (screen) (sc.hi_screen) = true
- Expr: `{"eq":["sc.hi_screen",{"const":true}],"op":"test"}`
- Cite: [i1040gi] p. 95, Schedule 1, line 17, Exceptions (2025; printed date 2026-02-25; sha256 482e9c48)

## 1 — `sc.f7206_line1`

- **IRS:** Health insurance payments (other than long-term care)
- **Encoded (NonNegDollars):** Input — The total you paid in 2025 for health insurance coverage (medical, dental and vision; including Medicare premiums you paid voluntarily) established under this business for you, your spouse and your dependents, and your child under age 27 at the end of 2025; but not amounts for any month you were eligible to participate in a health plan subsidized by your employer or your spouse's employer (or the employer of your dependent or of your child under age 27), and not long-term care insurance
- **Refusal:** when sc.hi_screened is true, cannot complete Self-employed health insurance with the premium tax credit (Pub. 974), Form 2555, an S corporation, an optional method or retirement plan payments. This health insurance deduction is outside this tool. Cite: [i1040gi] p. 95, Schedule 1, line 17, Exceptions; i7206 pp. 1–2 (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"op":"input","source":"The total you paid in 2025 for health insurance coverage (medical, dental and vision; including Medicare premiums you paid voluntarily) established under this business for you, your spouse and your dependents, and your child under age 27 at the end of 2025; but not amounts for any month you were eligible to participate in a health plan subsidized by your employer or your spouse's employer (or the employer of your dependent or of your child under age 27), and not long-term care insurance"}`
- Cite: [f7206] Form 7206 (2025), line 1; i7206 pp. 1–2 (2025; created 2025-10-02; sha256 822203c9)

## 2 — `sc.f7206_line2`

- **IRS:** Qualified long-term care insurance (the smaller of payments or the age limit, for each person covered)
- **Encoded (NonNegDollars):** Add ltc.amount over every confirmed ltc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"ltc","field":"ltc.amount","op":"sum_over"}`
- Cite: [f7206] Form 7206 (2025), line 2; i7206 pp. 1–2 (2025; created 2025-10-02; sha256 822203c9)

## 3 — `sc.f7206_line3`

- **IRS:** Add lines 1 and 2
- **Encoded (NonNegDollars):** Add line 1 (sc.f7206_line1) and line 2 (sc.f7206_line2).
- Expr: `{"of":["sc.f7206_line1","sc.f7206_line2"],"op":"sum"}`
- Cite: [f7206] Form 7206 (2025), line 3 (2025; created 2025-10-02; sha256 822203c9)

## 4 — `sc.f7206_line4`

- **IRS:** Net profit from the trade or business under which the insurance plan is established
- **Encoded (NonNegDollars):** Enter the amount from helper "Net profit of this business (zero for a loss)".
- Expr: `{"from":"sc.profit_pos","op":"copy"}`
- Cite: [f7206] Form 7206 (2025), line 4 (no other earned income from the business: Schedule C income only) (2025; created 2025-10-02; sha256 822203c9)

## 5 — `sc.f7206_line5`

- **IRS:** Total of all net profits from Schedule C, line 31
- **Encoded (NonNegDollars):** Enter the amount from person helper "Total of all net profits of this person's businesses (losses not included)".
- Expr: `{"from":"person.positive_profits","op":"copy"}`
- Cite: [f7206] Form 7206 (2025), line 5 (2025; created 2025-10-02; sha256 822203c9)

## (helper) — `sc.f7206_has`

- **Authored helper label:** Line 4 is more than zero
- **Encoded (Bool):** line 4 (sc.f7206_line4) > helper "Zero"
- Expr: `{"gt":["sc.f7206_line4","sc.zero"],"op":"test"}`
- Cite: [f7206] p. 1, "Divide line 4 by line 5" (line 6) (2025; created 2025-10-02; sha256 822203c9)

## (helper) — `sc.f7206_line7_pos`

- **Authored helper label:** Schedule 1, line 15 (this person's), times line 4 divided by line 5
- **Encoded (NonNegDollars):** Divide line 4 (sc.f7206_line4) by line 5 (sc.f7206_line5), rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply person helper "Schedule SE line 13 (deduction for one-half of self-employment tax) for this person" by the result.
- Expr: `{"amount":"person.se_line13","op":"prorate","part":"sc.f7206_line4","places":6,"whole":"sc.f7206_line5"}`
- Cite: [f7206] p. 1, "Divide line 4 by line 5" (line 6), "Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax, by the percentage on line 6" (line 7, amb.2025.f7206_line15_person, amb.2025.f7206_ratio_places) (2025; created 2025-10-02; sha256 822203c9)

## 7 — `sc.f7206_line7`

- **IRS:** Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax, by the percentage on line 6
- **Encoded (NonNegDollars):** Choose — [helper "Line 4 is more than zero" = true → helper "Schedule 1, line 15 (this person's), times line 4 divided by line 5"] [helper "Line 4 is more than zero" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["sc.f7206_has",{"const":true}],"op":"test"},"then":"sc.f7206_line7_pos"},{"guard":{"eq":["sc.f7206_has",{"const":false}],"op":"test"},"then":"sc.zero"}],"op":"choose"}`
- Cite: [f7206] Form 7206 (2025), line 7 (2025; created 2025-10-02; sha256 822203c9)

## 8 — `sc.f7206_line8`

- **IRS:** Subtract line 7 from line 4
- **Encoded (NonNegDollars):** Subtract line 7 (sc.f7206_line7) from line 4 (sc.f7206_line4). If zero or less, enter -0-.
- Expr: `{"from":"sc.f7206_line4","op":"subtract_floor0","take":"sc.f7206_line7"}`
- Cite: [f7206] Form 7206 (2025), line 8 (2025; created 2025-10-02; sha256 822203c9)

## (helper) — `sc.f7206_line9_pos`

- **Authored helper label:** This person's SEP or SIMPLE deduction times line 4 divided by line 5
- **Encoded (NonNegDollars):** Divide line 4 (sc.f7206_line4) by line 5 (sc.f7206_line5), rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply person helper "Schedule 1 line 16 for this person" by the result.
- Expr: `{"amount":"person.s16","op":"prorate","part":"sc.f7206_line4","places":6,"whole":"sc.f7206_line5"}`
- Cite: [f7206] p. 1, "Enter the amount, if any, from Schedule 1 (Form 1040), line 16, self-employed SEP, SIMPLE, and qualified plans, attributable to the same trade or business in which the insurance plan is established" (line 9, amb.2025.f7206_plan_attribution) (2025; created 2025-10-02; sha256 822203c9)

## 9 — `sc.f7206_line9`

- **IRS:** Schedule 1, line 16, attributable to the same trade or business
- **Encoded (NonNegDollars):** Choose — [helper "Line 4 is more than zero" = true → helper "This person's SEP or SIMPLE deduction times line 4 divided by line 5"] [helper "Line 4 is more than zero" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["sc.f7206_has",{"const":true}],"op":"test"},"then":"sc.f7206_line9_pos"},{"guard":{"eq":["sc.f7206_has",{"const":false}],"op":"test"},"then":"sc.zero"}],"op":"choose"}`
- Cite: [f7206] Form 7206 (2025), line 9 (2025; created 2025-10-02; sha256 822203c9)

## 10 — `sc.f7206_line10`

- **IRS:** Subtract line 9 from line 8
- **Encoded (NonNegDollars):** Subtract line 9 (sc.f7206_line9) from line 8 (sc.f7206_line8). If zero or less, enter -0-.
- Expr: `{"from":"sc.f7206_line8","op":"subtract_floor0","take":"sc.f7206_line9"}`
- Cite: [f7206] Form 7206 (2025), line 10 (2025; created 2025-10-02; sha256 822203c9)

## 13 — `sc.f7206_line13`

- **IRS:** Subtract line 12 from line 10
- **Encoded (NonNegDollars):** Enter the amount from line 10 (sc.f7206_line10).
- Expr: `{"from":"sc.f7206_line10","op":"copy"}`
- Cite: [f7206] Form 7206 (2025), lines 11 to 13 (lines 11 and 12, an S corporation and Form 2555, are refused) (2025; created 2025-10-02; sha256 822203c9)

## (helper) — `sc.f7206_min`

- **Authored helper label:** The smaller of line 3 or line 13
- **Encoded (NonNegDollars):** Enter the smaller of line 3 (sc.f7206_line3) or line 13 (sc.f7206_line13).
- Expr: `{"of":["sc.f7206_line3","sc.f7206_line13"],"op":"smaller_of"}`
- Cite: [f7206] Form 7206 (2025), line 14 (2025; created 2025-10-02; sha256 822203c9)

## 14 — `sc.f7206_line14`

- **IRS:** Self-employed health insurance deduction
- **Encoded (NonNegDollars):** Choose — [column (screen) (sc.hi_uses) = true → helper "The smaller of line 3 or line 13"] [column (screen) (sc.hi_uses) = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["sc.hi_uses",{"const":true}],"op":"test"},"then":"sc.f7206_min"},{"guard":{"eq":["sc.hi_uses",{"const":false}],"op":"test"},"then":"sc.zero"}],"op":"choose"}`
- Cite: [f7206] Form 7206 (2025), line 14, "Enter the smaller of line 3 or line 13 here and on Schedule 1 (Form 1040), line 17" (2025; created 2025-10-02; sha256 822203c9)

## (helper) — `sc.qbi_has`

- **Authored helper label:** This business has a net profit
- **Encoded (Bool):** helper "Net profit of this business (zero for a loss)" > helper "Zero"
- Expr: `{"gt":["sc.profit_pos","sc.zero"],"op":"test"}`
- Cite: [i8995] p. 2, Determining Your Qualified Business Income (2025; printed date 2026-01-26; sha256 875843ba)

## (helper) — `sc.qbi_se_pos`

- **Authored helper label:** This person's deductible part of self-employment tax attributable to this business (by share of net profits)
- **Encoded (NonNegDollars):** Divide helper "Net profit of this business (zero for a loss)" by person helper "Total of all net profits of this person's businesses (losses not included)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply person helper "Schedule SE line 13 (deduction for one-half of self-employment tax) for this person" by the result.
- Expr: `{"amount":"person.se_line13","op":"prorate","part":"sc.profit_pos","places":6,"whole":"person.positive_profits"}`
- Cite: [i8995] p. 2, Determining Your Qualified Business Income, "To figure the total amount of QBI, you must consider all items that are attributable to the trade or business. This includes ... deductible part of self-employment tax ... and contributions to qualified retirement plans" (amb.2025.qbi_attribution) (2025; printed date 2026-01-26; sha256 875843ba)

## (helper) — `sc.qbi_se`

- **Authored helper label:** Deductible part of self-employment tax attributable to this business
- **Encoded (NonNegDollars):** Choose — [helper "This business has a net profit" = true → helper "This person's deductible part of self-employment tax attributable to this business (by share of net profits)"] [helper "This business has a net profit" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["sc.qbi_has",{"const":true}],"op":"test"},"then":"sc.qbi_se_pos"},{"guard":{"eq":["sc.qbi_has",{"const":false}],"op":"test"},"then":"sc.zero"}],"op":"choose"}`
- Cite: [i8995] p. 2, Determining Your Qualified Business Income (amb.2025.qbi_attribution) (2025; printed date 2026-01-26; sha256 875843ba)

## (helper) — `sc.qbi_plan_pos`

- **Authored helper label:** This person's SEP or SIMPLE deduction attributable to this business (by share of net profits)
- **Encoded (NonNegDollars):** Divide helper "Net profit of this business (zero for a loss)" by person helper "Total of all net profits of this person's businesses (losses not included)", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply person helper "Schedule 1 line 16 for this person" by the result.
- Expr: `{"amount":"person.s16","op":"prorate","part":"sc.profit_pos","places":6,"whole":"person.positive_profits"}`
- Cite: [i8995] p. 2, Determining Your Qualified Business Income (amb.2025.qbi_attribution) (2025; printed date 2026-01-26; sha256 875843ba)

## (helper) — `sc.qbi_plan`

- **Authored helper label:** SEP or SIMPLE deduction attributable to this business
- **Encoded (NonNegDollars):** Choose — [helper "This business has a net profit" = true → helper "This person's SEP or SIMPLE deduction attributable to this business (by share of net profits)"] [helper "This business has a net profit" = false → helper "Zero"]
- Expr: `{"alternatives":[{"guard":{"eq":["sc.qbi_has",{"const":true}],"op":"test"},"then":"sc.qbi_plan_pos"},{"guard":{"eq":["sc.qbi_has",{"const":false}],"op":"test"},"then":"sc.zero"}],"op":"choose"}`
- Cite: [i8995] p. 2, Determining Your Qualified Business Income (amb.2025.qbi_attribution) (2025; printed date 2026-01-26; sha256 875843ba)

## (helper) — `sc.qbi_ded`

- **Authored helper label:** Deductions attributable to this business: self-employment tax, retirement plan and health insurance (Form 7206 for this business)
- **Encoded (NonNegDollars):** Add helper "Deductible part of self-employment tax attributable to this business", helper "SEP or SIMPLE deduction attributable to this business", and line 14 (sc.f7206_line14).
- Expr: `{"of":["sc.qbi_se","sc.qbi_plan","sc.f7206_line14"],"op":"sum"}`
- Cite: [i8995] pp. 2, 6, Determining Your Qualified Business Income and Figure 1, QBI Flow Chart, "self-employment health insurance deduction" (2025; printed date 2026-01-26; sha256 875843ba)

## 1(c) — `sc.qbi`

- **IRS:** Qualified business income or (loss) of this business
- **Encoded (Dollars):** Subtract helper "Deductions attributable to this business: self-employment tax, retirement plan and health insurance (Form 7206 for this business)" from helper "The amount for Schedule 1, line 3 and Schedule SE, line 2".
- Expr: `{"from":"sc.result","op":"subtract","take":"sc.qbi_ded"}`
- Cite: [i8995] p. 4, Line 1, column (c); f8995 p. 1, "(c) Qualified business income or (loss)" (line 1(c)) (2025; printed date 2026-01-26; sha256 875843ba)

## (screen) — `sc.tips_ot`

- **Authored helper label:** Tips or overtime in this business to be deducted on Schedule 1-A
- **Encoded (Bool):** Input — Does this business's income include qualified tips you received in the course of this business, or qualified overtime compensation reported to you on Form 1099-NEC or 1099-MISC, that you would deduct on Schedule 1-A?
- Expr: `{"op":"input","source":"Does this business's income include qualified tips you received in the course of this business, or qualified overtime compensation reported to you on Form 1099-NEC or 1099-MISC, that you would deduct on Schedule 1-A?"}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 5, "the qualified tips you and/or your spouse received in the course of a trade or business"; p. 108, line 14b (2025; printed date 2026-02-25; sha256 482e9c48)
