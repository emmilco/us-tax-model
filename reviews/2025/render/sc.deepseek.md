# Render comparison — sc

The rendered English of every printed line of `Schedule C (Form 1040) — Profit or Loss From Business, one per business` (`rendered/2025/sc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-01 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 4407ca3a38fca953c1d87062108df157f3514d6a231dbde5b3350aeacc25c167 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 5336eb4d57c28fe3dd4000438183d3f74e9cb1688b8accefbc1ad5426cdab84b |
| lines judged | 75 |
| match / mismatch / unclear / missing | 75 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 34, 37, 39, 41, 59, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| i4562 | 2025 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i1040gi | 2025; printed date 2026-02-25 | 93, 94, 95, 104, 108, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 93, 95, 104, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8995 | 2025; printed date 2026-01-26 | 2, 4, 6 | cited pages | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 2, 4, 6 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| iw2w3 | 2025; printed date 2025-02-19 | 18 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 18 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| p560 | For use in preparing 2025 returns | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 39, 40 | cited pages | 38bbfa2efb2894e2527d66cd3478f33c6ceae4b777f78674c22bec16db9809aa | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 40 | 7ef279c8f34addc2ff13420e35fab4a092bf8027f53907c28a5f46d2c21da737 |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |

## Lines

### (screen) (sc.statutory) — Is this business income you received as a statutory employee (the "Statutory employee" box
Status: **MATCH**

Model: Matches the line 1 statutory-employee instructions; notary public income is likewise treated outside self-employment income per the Schedule SE instructions, and the refusal names it.

### G — Did you "materially participate" in the operation of this business during 2025, and is the
Status: **MATCH**

Model: Tracks line G: not a rental activity and any material participation test met, or the oil and gas working-interest exception.

### (screen) (sc.spouse_owned) — Do you own this business together with your spouse (as a qualified joint venture, as commu
Status: **MATCH**

Model: Reflects the Business Owned and Operated by Spouses / qualified joint venture / community income rules.

### F — Do you use an accounting method other than cash or accrual, or did you change your account
Status: **MATCH**

Model: Tracks line F's cash/accrual/other method, Form 3115 and section 481(a) changes, and the section 263A small-business-taxpayer $31 million threshold.

### (screen) (sc.special) — For this business, do you have any of these: depletion (line 12); the energy efficient com
Status: **MATCH**

Model: All listed items (depletion, Form 7205, employment credits, Form 8990, recapture/inclusion amounts, chapter 11, Form 8873, timeshare/residential-lot sales, Notice 2014-7 payments, capitalized research, capital construction fund, Form 2441 contributions) appear in the instructions.

### 1 (sc.line1) — Gross receipts or sales
Status: **MATCH**

Model: Matches line 1 and its instructions, including Forms 1099-NEC and other 1099 income; statutory employee income is the case screened out.

### 2 (sc.line2) — Returns and allowances
Status: **MATCH**

Model: Returns and allowances reported as a positive number.

### 3 (sc.line3) — Subtract line 2 from line 1
Status: **MATCH**

Model: Subtract line 2 from line 1.

### 4 (sc.line4) — Cost of goods sold (from line 42)
Status: **MATCH**

Model: Cost of goods sold from line 42.

### 5 (sc.line5) — Gross profit. Subtract line 4 from line 3
Status: **MATCH**

Model: Subtract line 4 from line 3.

### 6 — Other income, including federal and state gasoline or fuel tax credit or refund
Status: **MATCH**

Model: Other business income; the listed examples (scrap sales, recovered bad debts, interest, state fuel tax refunds, prizes and awards, 1099-PATR) are all in the line 6 instructions.

### 7 (sc.line7) — Gross income. Add lines 5 and 6
Status: **MATCH**

Model: Add lines 5 and 6.

### 8 (sc.line8) — Advertising
Status: **MATCH**

Model: Advertising expenses.

### 9 (sc.line9) — Car and truck expenses
Status: **MATCH**

Model: Car and truck expenses summed from the vehicles' line 9 computations (standard mileage or actual business expenses plus parking and tolls).

### 10 (sc.line10) — Commissions and fees
Status: **MATCH**

Model: Commissions and fees not capitalized and not deducted elsewhere, as the line 10 instructions say.

### 11 — Contract labor
Status: **MATCH**

Model: Contract labor for nonemployees, excluding amounts on lines 17, 21, 26 or 37.

### 12 (sc.line12) — Depletion
Status: **MATCH**

Model: Line 12 is depletion; the program enters zero and depletion is screened out by the refusal on the income lines.

### 13 (sc.line13) — Depreciation and section 179 expense deduction (not included in Part III)
Status: **MATCH**

Model: Depreciation other than section 179 plus the section 179 deduction, consistent with Form 4562 line 22 and Schedule C line 13.

### 14 (sc.line14) — Employee benefit programs (other than on line 19)
Status: **MATCH**

Model: Employee benefit programs, not for the self and not pension/profit-sharing; credit reductions are screened.

### 15 — Insurance (other than health)
Status: **MATCH**

Model: Business insurance premiums, excluding self-insurance reserves and lost-earnings insurance, as instructed.

### 16a — Interest: mortgage (paid to banks, etc.)
Status: **MATCH**

Model: Mortgage interest on business real property paid to financial institutions with Form 1098, business part only, not capitalized.

### 16b — Interest: other
Status: **MATCH**

Model: Other business interest, including mortgage interest without Form 1098, business part only and excluding Schedule 1-A interest.

### 17 — Legal and professional services
Status: **MATCH**

Model: Accountant and attorney fees directly related to operating the business, including business tax advice and preparation.

### 18 — Office expense
Status: **MATCH**

Model: Office supplies and postage.

### 19 — Pension and profit-sharing plans
Status: **MATCH**

Model: Employee pension/profit-sharing/annuity contributions, including SEP, SIMPLE and SARSEP, not contributions for yourself.

### 20a — Rent or lease: vehicles, machinery, and equipment
Status: **MATCH**

Model: Business rent/lease of machinery, equipment and vehicles; sums the equipment/vehicle rent and the business part of vehicle lease payments.

### 20b — Rent or lease: other business property
Status: **MATCH**

Model: Rent for other business property, such as office space.

### 21 — Repairs and maintenance
Status: **MATCH**

Model: Incidental repairs and maintenance, excluding own labor and capitalized restorations or replacements.

### 22 — Supplies (not included in Part III)
Status: **MATCH**

Model: Materials and supplies actually consumed and used, or incidental supplies purchased where no inventory or records of use are kept.

### 23 — Taxes and licenses
Status: **MATCH**

Model: Taxes and licenses listed match the line 23 instructions; employment-credit reductions and property purchase taxes are screened or excluded.

### 24a — Travel
Status: **MATCH**

Model: Lodging and transportation for overnight business travel away from the tax home, excluding meals and entertainment.

### 24b — Deductible meals
Status: **MATCH**

Model: Sums 50% of normally limited meals, 80% of DOT hours-of-service meals, and fully deductible meals, matching the Amount of deduction discussion.

### 25 — Utilities
Status: **MATCH**

Model: Business utility expenses, excluding the base rate of the first home phone line.

### 26 — Wages (less employment credits)
Status: **MATCH**

Model: Salaries and wages paid to employees, excluding amounts paid to yourself and wages deducted elsewhere; employment credit reductions are screened.

### 27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **MATCH**

Model: Line 27a is the energy efficient commercial buildings deduction; the program enters zero and Form 7205 cases are screened.

### 48 — Total other expenses
Status: **MATCH**

Model: Total of Part V other expenses not included on lines 8 through 27a or line 30.

### 27b — Other expenses (from line 48)
Status: **MATCH**

Model: Other expenses from line 48.

### 28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **MATCH**

Model: Adds lines 8 through 27b, as the form directs.

### 29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **MATCH**

Model: Subtract line 28 from line 7.

### (screen) (sc.ho_uses) — Do you claim a deduction for business use of your home for this business?
Status: **MATCH**

Model: Asks whether a business-use-of-home deduction is claimed, matching the line 30 simplified-method entry.

### (screen) (sc.ho_other) — Does any of these apply to your business use of your home for this business?
Status: **MATCH**

Model: Covers Form 8829 actual expenses, multiple homes, daycare, shared space, part-year/area changes, other place of business, and Form 8949/4797 gains or losses mentioned in the line 30 instructions and worksheet.

### 30(b) — The part of your home used for business (square feet)
Status: **MATCH**

Model: Square footage used regularly and exclusively for the business (or for inventory/product samples), with multiple-business and special-case refusals matching the 300-square-foot allocation rule.

### 30(a) — Total square footage of your home
Status: **MATCH**

Model: Total square footage of the home.

### 3a — Maximum allowable amount (per square foot)
Status: **MATCH**

Model: Simplified Method Worksheet line 3a is $5.

### 4 (sc.ho_line4) — Multiply line 2 by line 3c
Status: **MATCH**

Model: Line 2 times line 3c; the program applies the 300-square-foot cap through its 'more than 300 square feet' condition, giving the same result.

### 1 (sc.ho_line1) — Gross income limitation (Schedule C, line 29)
Status: **MATCH**

Model: In the supported case (all income from the home, no Form 8949/4797 items, covered by the screen), the gross income limitation equals Schedule C line 29.

### 5 (sc.ho_line5) — Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4
Status: **MATCH**

Model: Implements the smaller of line 1 or line 4, with the section 179 interaction and the 'If zero or less, enter -0-' floor and a refusal where the two limits could bind.

### 30 — Expenses for business use of your home
Status: **MATCH**

Model: Line 5 when a home-use deduction is claimed, otherwise zero.

### 31 — Net profit or (loss). Subtract line 30 from line 29
Status: **MATCH**

Model: Subtract line 30 from line 29.

### 32 — If you have a loss, is all your investment in this business at risk (box 32a)?
Status: **MATCH**

Model: Box 32a all investment at risk; the listed nonrecourse, guarantee/stop-loss and insider borrowing items match box 32b.

### 33 — Method used to value closing inventory: other than cost or lower of cost or market, or a c
Status: **MATCH**

Model: Asks the line 33(c)/line 34 valuation and change questions and treats other methods or changes as outside the tool.

### 35 — Inventory at beginning of year
Status: **MATCH**

Model: Beginning inventory equal to prior year's closing inventory, zero if none; other methods or valuation changes are refused.

### 36 — Purchases less cost of items withdrawn for personal use
Status: **MATCH**

Model: Purchases less items withdrawn for personal use.

### 37 — Cost of labor
Status: **MATCH**

Model: Cost of labor, excluding amounts paid to yourself.

### 38 — Materials and supplies
Status: **MATCH**

Model: Materials and supplies.

### 39 — Other costs
Status: **MATCH**

Model: Other costs.

### 40 — Add lines 35 through 39
Status: **MATCH**

Model: Add lines 35 through 39.

### 41 — Inventory at end of year
Status: **MATCH**

Model: Inventory at end of year.

### 42 — Cost of goods sold. Subtract line 41 from line 40
Status: **MATCH**

Model: Subtract line 41 from line 40.

### 12 (sc.s179_allowed) — Section 179 expense deduction for this business
Status: **MATCH**

Model: Uses the elected section 179 amounts when the Form 4562 line 12 deduction equals them, otherwise the return's line 12, with the multiple-business allocation refusal.

### (screen) (sc.hi_uses) — Health insurance established under this business
Status: **MATCH**

Model: Asks whether health insurance for the filer, spouse, dependents or child under 27 was established under the business, policy in the business's or individual's name.

### (screen) (sc.hi_screen) — Does any of these apply to this health insurance?
Status: **MATCH**

Model: Lists the Marketplace/PTC, Form 2555, more-than-2%-S-corporation-shareholder, optional-method, retired-public-safety-officer, and multiple-business long-term-care cases that put the deduction outside the tool.

### 1 (sc.f7206_line1) — Health insurance payments (other than long-term care)
Status: **MATCH**

Model: Total health insurance premiums for the filer, spouse, dependents and child under 27, including voluntary Medicare premiums, excluding subsidized-employer months and long-term care insurance.

### 2 (sc.f7206_line2) — Qualified long-term care insurance (the smaller of payments or the age limit, for each per
Status: **MATCH**

Model: Per-person smaller of premiums paid or the age-based limit, totaled, matching Form 7206 line 2.

### 3 (sc.f7206_line3) — Add lines 1 and 2
Status: **MATCH**

Model: Add lines 1 and 2.

### 4 (sc.f7206_line4) — Net profit from the trade or business under which the insurance plan is established
Status: **MATCH**

Model: Net profit of the business under which the plan is established, floored at zero, consistent with Form 7206 line 4 and its earned-income footnote.

### 5 (sc.f7206_line5) — Total of all net profits from Schedule C, line 31
Status: **MATCH**

Model: Total of all net profits with losses excluded, matching Form 7206 line 5.

### 7 (sc.f7206_line7) — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax, by the p
Status: **MATCH**

Model: Schedule 1 line 15 times line 4 divided by line 5 (line 6), matching Form 7206 lines 6-7.

### 8 (sc.f7206_line8) — Subtract line 7 from line 4
Status: **MATCH**

Model: Subtract line 7 from line 4, not below zero.

### 9 (sc.f7206_line9) — Schedule 1, line 16, attributable to the same trade or business
Status: **MATCH**

Model: Schedule 1 line 16 attributable to this business, allocated by the line 4/line 5 profit share.

### 10 (sc.f7206_line10) — Subtract line 9 from line 8
Status: **MATCH**

Model: Subtract line 9 from line 8, not below zero.

### 13 (sc.f7206_line13) — Subtract line 12 from line 10
Status: **MATCH**

Model: Line 10 (line 12, the Form 2555 amount, is zero for the cases this tool supports and is screened).

### 14 (sc.f7206_line14) — Self-employed health insurance deduction
Status: **MATCH**

Model: Smaller of line 3 or line 13 when the insurance is established under the business, otherwise zero.

### 1(c) — Qualified business income or (loss) of this business
Status: **MATCH**

Model: QBI is the business result reduced by the deductible part of self-employment tax, the SEP/SIMPLE deduction and the Form 7206 health insurance deduction attributable to the business, per the Form 8995 instructions.

### (screen) (sc.tips_ot) — Tips or overtime in this business to be deducted on Schedule 1-A
Status: **MATCH**

Model: Asks about qualified tips and qualified overtime compensation that are deducted on Schedule 1-A rather than on Schedule C.

## Raw response

```yaml
lines:
  - key: "(screen) (sc.statutory)"
    status: MATCH
    reason: "Matches the line 1 statutory-employee instructions; notary public income is likewise treated outside self-employment income per the Schedule SE instructions, and the refusal names it."
  - key: "G"
    status: MATCH
    reason: "Tracks line G: not a rental activity and any material participation test met, or the oil and gas working-interest exception."
  - key: "(screen) (sc.spouse_owned)"
    status: MATCH
    reason: "Reflects the Business Owned and Operated by Spouses / qualified joint venture / community income rules."
  - key: "F"
    status: MATCH
    reason: "Tracks line F's cash/accrual/other method, Form 3115 and section 481(a) changes, and the section 263A small-business-taxpayer $31 million threshold."
  - key: "(screen) (sc.special)"
    status: MATCH
    reason: "All listed items (depletion, Form 7205, employment credits, Form 8990, recapture/inclusion amounts, chapter 11, Form 8873, timeshare/residential-lot sales, Notice 2014-7 payments, capitalized research, capital construction fund, Form 2441 contributions) appear in the instructions."
  - key: "1 (sc.line1)"
    status: MATCH
    reason: "Matches line 1 and its instructions, including Forms 1099-NEC and other 1099 income; statutory employee income is the case screened out."
  - key: "2 (sc.line2)"
    status: MATCH
    reason: "Returns and allowances reported as a positive number."
  - key: "3 (sc.line3)"
    status: MATCH
    reason: "Subtract line 2 from line 1."
  - key: "4 (sc.line4)"
    status: MATCH
    reason: "Cost of goods sold from line 42."
  - key: "5 (sc.line5)"
    status: MATCH
    reason: "Subtract line 4 from line 3."
  - key: "6"
    status: MATCH
    reason: "Other business income; the listed examples (scrap sales, recovered bad debts, interest, state fuel tax refunds, prizes and awards, 1099-PATR) are all in the line 6 instructions."
  - key: "7 (sc.line7)"
    status: MATCH
    reason: "Add lines 5 and 6."
  - key: "8 (sc.line8)"
    status: MATCH
    reason: "Advertising expenses."
  - key: "9 (sc.line9)"
    status: MATCH
    reason: "Car and truck expenses summed from the vehicles' line 9 computations (standard mileage or actual business expenses plus parking and tolls)."
  - key: "10 (sc.line10)"
    status: MATCH
    reason: "Commissions and fees not capitalized and not deducted elsewhere, as the line 10 instructions say."
  - key: "11"
    status: MATCH
    reason: "Contract labor for nonemployees, excluding amounts on lines 17, 21, 26 or 37."
  - key: "12 (sc.line12)"
    status: MATCH
    reason: "Line 12 is depletion; the program enters zero and depletion is screened out by the refusal on the income lines."
  - key: "13 (sc.line13)"
    status: MATCH
    reason: "Depreciation other than section 179 plus the section 179 deduction, consistent with Form 4562 line 22 and Schedule C line 13."
  - key: "14 (sc.line14)"
    status: MATCH
    reason: "Employee benefit programs, not for the self and not pension/profit-sharing; credit reductions are screened."
  - key: "15"
    status: MATCH
    reason: "Business insurance premiums, excluding self-insurance reserves and lost-earnings insurance, as instructed."
  - key: "16a"
    status: MATCH
    reason: "Mortgage interest on business real property paid to financial institutions with Form 1098, business part only, not capitalized."
  - key: "16b"
    status: MATCH
    reason: "Other business interest, including mortgage interest without Form 1098, business part only and excluding Schedule 1-A interest."
  - key: "17"
    status: MATCH
    reason: "Accountant and attorney fees directly related to operating the business, including business tax advice and preparation."
  - key: "18"
    status: MATCH
    reason: "Office supplies and postage."
  - key: "19"
    status: MATCH
    reason: "Employee pension/profit-sharing/annuity contributions, including SEP, SIMPLE and SARSEP, not contributions for yourself."
  - key: "20a"
    status: MATCH
    reason: "Business rent/lease of machinery, equipment and vehicles; sums the equipment/vehicle rent and the business part of vehicle lease payments."
  - key: "20b"
    status: MATCH
    reason: "Rent for other business property, such as office space."
  - key: "21"
    status: MATCH
    reason: "Incidental repairs and maintenance, excluding own labor and capitalized restorations or replacements."
  - key: "22"
    status: MATCH
    reason: "Materials and supplies actually consumed and used, or incidental supplies purchased where no inventory or records of use are kept."
  - key: "23"
    status: MATCH
    reason: "Taxes and licenses listed match the line 23 instructions; employment-credit reductions and property purchase taxes are screened or excluded."
  - key: "24a"
    status: MATCH
    reason: "Lodging and transportation for overnight business travel away from the tax home, excluding meals and entertainment."
  - key: "24b"
    status: MATCH
    reason: "Sums 50% of normally limited meals, 80% of DOT hours-of-service meals, and fully deductible meals, matching the Amount of deduction discussion."
  - key: "25"
    status: MATCH
    reason: "Business utility expenses, excluding the base rate of the first home phone line."
  - key: "26"
    status: MATCH
    reason: "Salaries and wages paid to employees, excluding amounts paid to yourself and wages deducted elsewhere; employment credit reductions are screened."
  - key: "27a"
    status: MATCH
    reason: "Line 27a is the energy efficient commercial buildings deduction; the program enters zero and Form 7205 cases are screened."
  - key: "48"
    status: MATCH
    reason: "Total of Part V other expenses not included on lines 8 through 27a or line 30."
  - key: "27b"
    status: MATCH
    reason: "Other expenses from line 48."
  - key: "28"
    status: MATCH
    reason: "Adds lines 8 through 27b, as the form directs."
  - key: "29"
    status: MATCH
    reason: "Subtract line 28 from line 7."
  - key: "(screen) (sc.ho_uses)"
    status: MATCH
    reason: "Asks whether a business-use-of-home deduction is claimed, matching the line 30 simplified-method entry."
  - key: "(screen) (sc.ho_other)"
    status: MATCH
    reason: "Covers Form 8829 actual expenses, multiple homes, daycare, shared space, part-year/area changes, other place of business, and Form 8949/4797 gains or losses mentioned in the line 30 instructions and worksheet."
  - key: "30(b)"
    status: MATCH
    reason: "Square footage used regularly and exclusively for the business (or for inventory/product samples), with multiple-business and special-case refusals matching the 300-square-foot allocation rule."
  - key: "30(a)"
    status: MATCH
    reason: "Total square footage of the home."
  - key: "3a"
    status: MATCH
    reason: "Simplified Method Worksheet line 3a is $5."
  - key: "4 (sc.ho_line4)"
    status: MATCH
    reason: "Line 2 times line 3c; the program applies the 300-square-foot cap through its 'more than 300 square feet' condition, giving the same result."
  - key: "1 (sc.ho_line1)"
    status: MATCH
    reason: "In the supported case (all income from the home, no Form 8949/4797 items, covered by the screen), the gross income limitation equals Schedule C line 29."
  - key: "5 (sc.ho_line5)"
    status: MATCH
    reason: "Implements the smaller of line 1 or line 4, with the section 179 interaction and the 'If zero or less, enter -0-' floor and a refusal where the two limits could bind."
  - key: "30"
    status: MATCH
    reason: "Line 5 when a home-use deduction is claimed, otherwise zero."
  - key: "31"
    status: MATCH
    reason: "Subtract line 30 from line 29."
  - key: "32"
    status: MATCH
    reason: "Box 32a all investment at risk; the listed nonrecourse, guarantee/stop-loss and insider borrowing items match box 32b."
  - key: "33"
    status: MATCH
    reason: "Asks the line 33(c)/line 34 valuation and change questions and treats other methods or changes as outside the tool."
  - key: "35"
    status: MATCH
    reason: "Beginning inventory equal to prior year's closing inventory, zero if none; other methods or valuation changes are refused."
  - key: "36"
    status: MATCH
    reason: "Purchases less items withdrawn for personal use."
  - key: "37"
    status: MATCH
    reason: "Cost of labor, excluding amounts paid to yourself."
  - key: "38"
    status: MATCH
    reason: "Materials and supplies."
  - key: "39"
    status: MATCH
    reason: "Other costs."
  - key: "40"
    status: MATCH
    reason: "Add lines 35 through 39."
  - key: "41"
    status: MATCH
    reason: "Inventory at end of year."
  - key: "42"
    status: MATCH
    reason: "Subtract line 41 from line 40."
  - key: "12 (sc.s179_allowed)"
    status: MATCH
    reason: "Uses the elected section 179 amounts when the Form 4562 line 12 deduction equals them, otherwise the return's line 12, with the multiple-business allocation refusal."
  - key: "(screen) (sc.hi_uses)"
    status: MATCH
    reason: "Asks whether health insurance for the filer, spouse, dependents or child under 27 was established under the business, policy in the business's or individual's name."
  - key: "(screen) (sc.hi_screen)"
    status: MATCH
    reason: "Lists the Marketplace/PTC, Form 2555, more-than-2%-S-corporation-shareholder, optional-method, retired-public-safety-officer, and multiple-business long-term-care cases that put the deduction outside the tool."
  - key: "1 (sc.f7206_line1)"
    status: MATCH
    reason: "Total health insurance premiums for the filer, spouse, dependents and child under 27, including voluntary Medicare premiums, excluding subsidized-employer months and long-term care insurance."
  - key: "2 (sc.f7206_line2)"
    status: MATCH
    reason: "Per-person smaller of premiums paid or the age-based limit, totaled, matching Form 7206 line 2."
  - key: "3 (sc.f7206_line3)"
    status: MATCH
    reason: "Add lines 1 and 2."
  - key: "4 (sc.f7206_line4)"
    status: MATCH
    reason: "Net profit of the business under which the plan is established, floored at zero, consistent with Form 7206 line 4 and its earned-income footnote."
  - key: "5 (sc.f7206_line5)"
    status: MATCH
    reason: "Total of all net profits with losses excluded, matching Form 7206 line 5."
  - key: "7 (sc.f7206_line7)"
    status: MATCH
    reason: "Schedule 1 line 15 times line 4 divided by line 5 (line 6), matching Form 7206 lines 6-7."
  - key: "8 (sc.f7206_line8)"
    status: MATCH
    reason: "Subtract line 7 from line 4, not below zero."
  - key: "9 (sc.f7206_line9)"
    status: MATCH
    reason: "Schedule 1 line 16 attributable to this business, allocated by the line 4/line 5 profit share."
  - key: "10 (sc.f7206_line10)"
    status: MATCH
    reason: "Subtract line 9 from line 8, not below zero."
  - key: "13 (sc.f7206_line13)"
    status: MATCH
    reason: "Line 10 (line 12, the Form 2555 amount, is zero for the cases this tool supports and is screened)."
  - key: "14 (sc.f7206_line14)"
    status: MATCH
    reason: "Smaller of line 3 or line 13 when the insurance is established under the business, otherwise zero."
  - key: "1(c)"
    status: MATCH
    reason: "QBI is the business result reduced by the deductible part of self-employment tax, the SEP/SIMPLE deduction and the Form 7206 health insurance deduction attributable to the business, per the Form 8995 instructions."
  - key: "(screen) (sc.tips_ot)"
    status: MATCH
    reason: "Asks about qualified tips and qualified overtime compensation that are deducted on Schedule 1-A rather than on Schedule C."
```
