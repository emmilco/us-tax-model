# Render comparison — sc

The rendered English of every printed line of `Schedule C (Form 1040) — Profit or Loss From Business, one per business` (`rendered/2025/sc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 8f585e2b145bf3990ac60c8428148c3c83a6e6f0d0f7710497fb74c31e59af5c |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | f549cdf4128550cca1545ae2e6682e8beb1fb0dc78d2706ad94399e87c184bff |
| lines judged | 75 |
| match / mismatch / unclear / missing | 71 / 3 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 34 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 34 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| i4562 | 2025 | 4, 5, 9, 10, 13, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 5, 9, 10, 13, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i1040gi | 2025; printed date 2026-02-25 | 94, 95, 104, 108 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 95, 104 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8995 | 2025; printed date 2026-01-26 | 2, 4, 6 | cited pages | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 2, 4, 6 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |

## Lines

### (screen) (sc.statutory) — Is this business income you received as a statutory employee (the "Statutory employee" box
Status: **MATCH**

Model: The line 1 instructions cover statutory employees, and the line 31 instructions address notary public treatment; the screen narrows out those cases.

### G — Did you "materially participate" in the operation of this business during 2025, and is the
Status: **MATCH**

Model: Matches line G: non-rental activity plus material participation or the oil and gas working-interest exception.

### (screen) (sc.spouse_owned) — Do you own this business together with your spouse (as a qualified joint venture, as commu
Status: **MATCH**

Model: Matches the general instructions on jointly owned spouse businesses, qualified joint ventures, community property, and partnerships.

### F — Do you use an accounting method other than cash or accrual, or did you change your account
Status: **MATCH**

Model: Matches line F and the related instructions on accounting method, Form 3115/section 481(a), and the section 263A small-business threshold.

### (screen) (sc.special) — For this business, do you have any of these: depletion (line 12); the energy efficient com
Status: **MATCH**

Model: The listed special items are the outside-tool items described in the Schedule C instructions; they are screened out.

### 1 (sc.line1) — Gross receipts or sales
Status: **MATCH**

Model: Matches the line 1 instructions, including Forms 1099-NEC and other Forms 1099, with the refusal naming the excluded statutory, passive, spouse, accounting-method, and special cases.

### 2 (sc.line2) — Returns and allowances
Status: **MATCH**

Model: Matches line 2: returns and allowances are reported as a positive number.

### 3 (sc.line3) — Subtract line 2 from line 1
Status: **MATCH**

Model: Matches line 3: subtract line 2 from line 1.

### 4 (sc.line4) — Cost of goods sold (from line 42)
Status: **MATCH**

Model: Matches line 4: enter the amount from line 42.

### 5 (sc.line5) — Gross profit. Subtract line 4 from line 3
Status: **MATCH**

Model: Matches line 5: subtract line 4 from line 3.

### 6 — Other income, including federal and state gasoline or fuel tax credit or refund
Status: **MATCH**

Model: Matches line 6 and the listed other-income examples in the instructions.

### 7 (sc.line7) — Gross income. Add lines 5 and 6
Status: **MATCH**

Model: Matches line 7: add lines 5 and 6.

### 8 (sc.line8) — Advertising
Status: **MATCH**

Model: Matches line 8: advertising expenses.

### 9 (sc.line9) — Car and truck expenses
Status: **MATCH**

Model: Matches line 9 by summing the vehicle line 9 amounts under the standard-mileage or actual-expense method.

### 10 (sc.line10) — Commissions and fees
Status: **MATCH**

Model: Matches line 10: commissions and fees not capitalized or deducted elsewhere.

### 11 — Contract labor
Status: **MATCH**

Model: Matches line 11: contract labor payments to nonemployees, excluding amounts on lines 17, 21, 26, or 37.

### 12 (sc.line12) — Depletion
Status: **MATCH**

Model: Line 12 is depletion; the program returns zero only because depletion is screened out by sc.special.

### 13 (sc.line13) — Depreciation and section 179 expense deduction (not included in Part III)
Status: **MATCH**

Model: The line 13 restatement matches the Schedule C and Form 4562 line 22 components of depreciation plus the section 179 amount.

### 14 (sc.line14) — Employee benefit programs (other than on line 19)
Status: **MATCH**

Model: Matches line 14: employee benefit programs, excluding yourself and pension/profit-sharing plans.

### 15 — Insurance (other than health)
Status: **MATCH**

Model: Matches line 15: business insurance, excluding self-insurance reserves and lost-earnings insurance.

### 16a — Interest: mortgage (paid to banks, etc.)
Status: **MATCH**

Model: Matches line 16a: business mortgage interest paid to banks or financial institutions for which a Form 1098 was received.

### 16b — Interest: other
Status: **MATCH**

Model: Matches line 16b: other business interest, with only the business part of vehicle interest and none of the Schedule 1-A interest.

### 17 — Legal and professional services
Status: **MATCH**

Model: Matches line 17: accountant and attorney fees, including business tax advice and preparation.

### 18 — Office expense
Status: **MATCH**

Model: Matches line 18: office supplies and postage.

### 19 — Pension and profit-sharing plans
Status: **MATCH**

Model: Matches line 19: employee pension, profit-sharing, annuity, SEP, SIMPLE, and SARSEP contributions, not your own contributions.

### 20a — Rent or lease: vehicles, machinery, and equipment
Status: **MATCH**

Model: Matches line 20a: rent or lease of vehicles, machinery, and equipment, with lease inclusion amounts screened out.

### 20b — Rent or lease: other business property
Status: **MATCH**

Model: Matches line 20b: rent or lease of other business property, such as office space.

### 21 — Repairs and maintenance
Status: **MATCH**

Model: Matches line 21: incidental repairs and maintenance, excluding your own labor and capitalized restorations or replacements.

### 22 — Supplies (not included in Part III)
Status: **MATCH**

Model: Matches line 22: materials and supplies actually consumed, or incidental supplies under the no-inventory/records rule.

### 23 — Taxes and licenses
Status: **MISMATCH**

Restated: Input — Business taxes and licenses: sales tax imposed on you as the seller, real estate and personal property taxes on business assets, licenses and regulatory fees, the employer share of social security and Medicare taxes, federal unemployment tax, federal highway use tax, state unemployment contributions (not income or self-employment tax, and not taxes on property you bought); zero if none

Model: IRS line 23 includes 'Contributions to a state unemployment insurance fund, or paid family and medical leave program disability benefit fund if they are considered taxes under state law'; the restatement omits the paid family and medical leave fund.

Ruling: open

### 24a — Travel
Status: **MATCH**

Model: Matches line 24a: lodging and transportation for overnight business travel away from your tax home, excluding meals and entertainment.

### 24b — Deductible meals
Status: **MATCH**

Model: Matches line 24b and the 50%, 80%, and fully deductible meal rules in the instructions.

### 25 — Utilities
Status: **MATCH**

Model: Matches line 25: business utility expenses, with the home-phone first-line base-rate rule.

### 26 — Wages (less employment credits)
Status: **MATCH**

Model: Matches line 26 within the supported cases; employment credits are screened out by sc.special.

### 27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **MATCH**

Model: Line 27a is the energy efficient commercial buildings deduction; the program returns zero only because that item is screened out.

### 48 — Total other expenses
Status: **MATCH**

Model: Matches line 48: total other expenses not included on lines 8 through 27a or line 30.

### 27b — Other expenses (from line 48)
Status: **MATCH**

Model: Matches line 27b: enter the amount from line 48.

### 28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **MATCH**

Model: Matches line 28: add lines 8 through 27b.

### 29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **MATCH**

Model: Matches line 29: subtract line 28 from line 7.

### (screen) (sc.ho_uses) — Do you claim a deduction for business use of your home for this business?
Status: **MATCH**

Model: Matches the line 30 instruction asking whether the business-use-of-home deduction is claimed for this business.

### (screen) (sc.ho_other) — Does any of these apply to your business use of your home for this business?
Status: **MATCH**

Model: The listed cases match the simplified-method exclusions for Form 8829, multiple homes, daycare, shared use, part-year changes, other business locations, and Form 8949/4797 gains or losses.

### 30(b) — The part of your home used for business (square feet)
Status: **MATCH**

Model: Matches the line 30(b) square footage for the business part of the home, with the simplified-method multiple-business and special-case refusals.

### 30(a) — Total square footage of your home
Status: **MATCH**

Model: Matches the line 30(a) total square footage of the home.

### 3a — Maximum allowable amount (per square foot)
Status: **MATCH**

Model: Matches Simplified Method Worksheet line 3a: $5.

### 4 (sc.ho_line4) — Multiply line 2 by line 3c
Status: **MATCH**

Model: Matches Simplified Method Worksheet line 4: multiply the allowable square footage by line 3c, capping at 300 square feet.

### 1 (sc.ho_line1) — Gross income limitation (Schedule C, line 29)
Status: **MATCH**

Model: Within the supported simplified-method cases, line 1 is the amount from Schedule C line 29; other-location and Form 8949/4797 cases are refused.

### 5 (sc.ho_line5) — Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4
Status: **MATCH**

Model: The restatement implements the smaller-of line 1/line 4 rule within the supported cases and refuses the two-limit section 179/home-office interaction.

### 30 — Expenses for business use of your home
Status: **MATCH**

Model: Matches line 30: use the simplified-method line 5 amount when home-office use is claimed, otherwise zero.

### 31 — Net profit or (loss). Subtract line 30 from line 29
Status: **MATCH**

Model: Matches line 31: subtract line 30 from line 29.

### 32 — If you have a loss, is all your investment in this business at risk (box 32a)?
Status: **MATCH**

Model: Matches the box 32a at-risk description and the instructions' list of non-at-risk amounts.

### 33 — Method used to value closing inventory: other than cost or lower of cost or market, or a c
Status: **MATCH**

Model: Matches the line 33/line 34 inventory-method and change screen, with other methods and changes refused.

### 35 — Inventory at beginning of year
Status: **MATCH**

Model: Matches line 35 beginning inventory within the supported no-method-change cases.

### 36 — Purchases less cost of items withdrawn for personal use
Status: **MATCH**

Model: Matches line 36: purchases less personal withdrawals.

### 37 — Cost of labor
Status: **MATCH**

Model: Matches line 37: cost of labor, excluding amounts paid to yourself.

### 38 — Materials and supplies
Status: **MATCH**

Model: Matches line 38: materials and supplies.

### 39 — Other costs
Status: **MATCH**

Model: Matches line 39: other costs.

### 40 — Add lines 35 through 39
Status: **MATCH**

Model: Matches line 40: add lines 35 through 39.

### 41 — Inventory at end of year
Status: **MATCH**

Model: Matches line 41: inventory at end of year.

### 42 — Cost of goods sold. Subtract line 41 from line 40
Status: **MATCH**

Model: Matches line 42: subtract line 41 from line 40.

### 12 (sc.s179_allowed) — Section 179 expense deduction for this business
Status: **MATCH**

Model: Matches the Form 4562 line 12 allocation approach: use the business election when there is no difference, otherwise use the return's only Schedule C section 179 deduction.

### (screen) (sc.hi_uses) — Health insurance established under this business
Status: **MATCH**

Model: Matches Form 7206 and the Schedule 1 instructions on health insurance established under the business.

### (screen) (sc.hi_screen) — Does any of these apply to this health insurance?
Status: **MATCH**

Model: The listed Marketplace, Form 2555, S corporation, optional-method, retired-public-safety-officer, and multiple-business long-term-care cases are the Form 7206/instructions exclusions.

### 1 (sc.f7206_line1) — Health insurance payments (other than long-term care)
Status: **MATCH**

Model: Matches Form 7206 line 1, including medical, dental, vision, voluntary Medicare premiums, and the employer-subsidy and long-term-care exclusions.

### 2 (sc.f7206_line2) — Qualified long-term care insurance (the smaller of payments or the age limit, for each per
Status: **MATCH**

Model: Matches Form 7206 line 2: aggregate each covered person's smaller-of amount for qualified long-term care insurance.

### 3 (sc.f7206_line3) — Add lines 1 and 2
Status: **MATCH**

Model: Matches Form 7206 line 3: add lines 1 and 2.

### 4 (sc.f7206_line4) — Net profit from the trade or business under which the insurance plan is established
Status: **MISMATCH**

Restated: Enter the amount from helper "Net profit of this business (zero for a loss)".

Model: IRS line 4 says 'Enter your net profit* and any other earned income** from the trade or business under which the insurance plan is established'; the restatement uses only this business's net profit.

Ruling: open

### 5 (sc.f7206_line5) — Total of all net profits from Schedule C, line 31
Status: **MISMATCH**

Restated: Enter the amount from person helper "Total of all net profits of this person's businesses (losses not included)".

Model: IRS line 5 says 'total of all net profits* from Schedule C..., Schedule F..., or Schedule K-1..., plus any other income allocable to the profitable businesses'; the restatement uses only this person's Schedule C net profits.

Ruling: open

### 7 (sc.f7206_line7) — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax, by the p
Status: **MATCH**

Model: Matches Form 7206 lines 6 and 7: multiply Schedule 1 line 15 by line 4 divided by line 5, with zero when line 4 is not positive.

### 8 (sc.f7206_line8) — Subtract line 7 from line 4
Status: **MATCH**

Model: Matches Form 7206 line 8: subtract line 7 from line 4.

### 9 (sc.f7206_line9) — Schedule 1, line 16, attributable to the same trade or business
Status: **UNCLEAR**

Restated: Choose — [helper "Line 4 is more than zero" = true → helper "This person's SEP or SIMPLE deduction times line 4 divided by line 5"] [helper "Line 4 is more than zero" = false → helper "Zero"]

Model: IRS line 9 says only to enter the Schedule 1 line 16 amount 'attributable to the same trade or business'; it does not state the line 4/line 5 allocation used here.

Ruling: open

### 10 (sc.f7206_line10) — Subtract line 9 from line 8
Status: **MATCH**

Model: Matches Form 7206 line 10: subtract line 9 from line 8.

### 13 (sc.f7206_line13) — Subtract line 12 from line 10
Status: **MATCH**

Model: Within the supported non-Form 2555, non-S-corporation cases, line 13 equals line 10 because line 12 is zero.

### 14 (sc.f7206_line14) — Self-employed health insurance deduction
Status: **MATCH**

Model: Matches Form 7206 line 14: the smaller of line 3 or line 13, and zero when no health insurance is claimed.

### 1(c) — Qualified business income or (loss) of this business
Status: **MATCH**

Model: The QBI instructions treat the deductible part of self-employment tax, self-employed health insurance, and qualified retirement plan contributions as business deductions; subtracting them matches the QBI computation.

### (screen) (sc.tips_ot) — Tips or overtime in this business to be deducted on Schedule 1-A
Status: **MATCH**

Model: Matches the Schedule C instructions and Schedule 1-A treatment of qualified tips and qualified overtime compensation.

## Raw response

```yaml
lines:
  - key: "(screen) (sc.statutory)"
    status: MATCH
    reason: "The line 1 instructions cover statutory employees, and the line 31 instructions address notary public treatment; the screen narrows out those cases."
  - key: "G"
    status: MATCH
    reason: "Matches line G: non-rental activity plus material participation or the oil and gas working-interest exception."
  - key: "(screen) (sc.spouse_owned)"
    status: MATCH
    reason: "Matches the general instructions on jointly owned spouse businesses, qualified joint ventures, community property, and partnerships."
  - key: "F"
    status: MATCH
    reason: "Matches line F and the related instructions on accounting method, Form 3115/section 481(a), and the section 263A small-business threshold."
  - key: "(screen) (sc.special)"
    status: MATCH
    reason: "The listed special items are the outside-tool items described in the Schedule C instructions; they are screened out."
  - key: "1 (sc.line1)"
    status: MATCH
    reason: "Matches the line 1 instructions, including Forms 1099-NEC and other Forms 1099, with the refusal naming the excluded statutory, passive, spouse, accounting-method, and special cases."
  - key: "2 (sc.line2)"
    status: MATCH
    reason: "Matches line 2: returns and allowances are reported as a positive number."
  - key: "3 (sc.line3)"
    status: MATCH
    reason: "Matches line 3: subtract line 2 from line 1."
  - key: "4 (sc.line4)"
    status: MATCH
    reason: "Matches line 4: enter the amount from line 42."
  - key: "5 (sc.line5)"
    status: MATCH
    reason: "Matches line 5: subtract line 4 from line 3."
  - key: "6"
    status: MATCH
    reason: "Matches line 6 and the listed other-income examples in the instructions."
  - key: "7 (sc.line7)"
    status: MATCH
    reason: "Matches line 7: add lines 5 and 6."
  - key: "8 (sc.line8)"
    status: MATCH
    reason: "Matches line 8: advertising expenses."
  - key: "9 (sc.line9)"
    status: MATCH
    reason: "Matches line 9 by summing the vehicle line 9 amounts under the standard-mileage or actual-expense method."
  - key: "10 (sc.line10)"
    status: MATCH
    reason: "Matches line 10: commissions and fees not capitalized or deducted elsewhere."
  - key: "11"
    status: MATCH
    reason: "Matches line 11: contract labor payments to nonemployees, excluding amounts on lines 17, 21, 26, or 37."
  - key: "12 (sc.line12)"
    status: MATCH
    reason: "Line 12 is depletion; the program returns zero only because depletion is screened out by sc.special."
  - key: "13 (sc.line13)"
    status: MATCH
    reason: "The line 13 restatement matches the Schedule C and Form 4562 line 22 components of depreciation plus the section 179 amount."
  - key: "14 (sc.line14)"
    status: MATCH
    reason: "Matches line 14: employee benefit programs, excluding yourself and pension/profit-sharing plans."
  - key: "15"
    status: MATCH
    reason: "Matches line 15: business insurance, excluding self-insurance reserves and lost-earnings insurance."
  - key: "16a"
    status: MATCH
    reason: "Matches line 16a: business mortgage interest paid to banks or financial institutions for which a Form 1098 was received."
  - key: "16b"
    status: MATCH
    reason: "Matches line 16b: other business interest, with only the business part of vehicle interest and none of the Schedule 1-A interest."
  - key: "17"
    status: MATCH
    reason: "Matches line 17: accountant and attorney fees, including business tax advice and preparation."
  - key: "18"
    status: MATCH
    reason: "Matches line 18: office supplies and postage."
  - key: "19"
    status: MATCH
    reason: "Matches line 19: employee pension, profit-sharing, annuity, SEP, SIMPLE, and SARSEP contributions, not your own contributions."
  - key: "20a"
    status: MATCH
    reason: "Matches line 20a: rent or lease of vehicles, machinery, and equipment, with lease inclusion amounts screened out."
  - key: "20b"
    status: MATCH
    reason: "Matches line 20b: rent or lease of other business property, such as office space."
  - key: "21"
    status: MATCH
    reason: "Matches line 21: incidental repairs and maintenance, excluding your own labor and capitalized restorations or replacements."
  - key: "22"
    status: MATCH
    reason: "Matches line 22: materials and supplies actually consumed, or incidental supplies under the no-inventory/records rule."
  - key: "23"
    status: MISMATCH
    reason: "IRS line 23 includes 'Contributions to a state unemployment insurance fund, or paid family and medical leave program disability benefit fund if they are considered taxes under state law'; the restatement omits the paid family and medical leave fund."
  - key: "24a"
    status: MATCH
    reason: "Matches line 24a: lodging and transportation for overnight business travel away from your tax home, excluding meals and entertainment."
  - key: "24b"
    status: MATCH
    reason: "Matches line 24b and the 50%, 80%, and fully deductible meal rules in the instructions."
  - key: "25"
    status: MATCH
    reason: "Matches line 25: business utility expenses, with the home-phone first-line base-rate rule."
  - key: "26"
    status: MATCH
    reason: "Matches line 26 within the supported cases; employment credits are screened out by sc.special."
  - key: "27a"
    status: MATCH
    reason: "Line 27a is the energy efficient commercial buildings deduction; the program returns zero only because that item is screened out."
  - key: "48"
    status: MATCH
    reason: "Matches line 48: total other expenses not included on lines 8 through 27a or line 30."
  - key: "27b"
    status: MATCH
    reason: "Matches line 27b: enter the amount from line 48."
  - key: "28"
    status: MATCH
    reason: "Matches line 28: add lines 8 through 27b."
  - key: "29"
    status: MATCH
    reason: "Matches line 29: subtract line 28 from line 7."
  - key: "(screen) (sc.ho_uses)"
    status: MATCH
    reason: "Matches the line 30 instruction asking whether the business-use-of-home deduction is claimed for this business."
  - key: "(screen) (sc.ho_other)"
    status: MATCH
    reason: "The listed cases match the simplified-method exclusions for Form 8829, multiple homes, daycare, shared use, part-year changes, other business locations, and Form 8949/4797 gains or losses."
  - key: "30(b)"
    status: MATCH
    reason: "Matches the line 30(b) square footage for the business part of the home, with the simplified-method multiple-business and special-case refusals."
  - key: "30(a)"
    status: MATCH
    reason: "Matches the line 30(a) total square footage of the home."
  - key: "3a"
    status: MATCH
    reason: "Matches Simplified Method Worksheet line 3a: $5."
  - key: "4 (sc.ho_line4)"
    status: MATCH
    reason: "Matches Simplified Method Worksheet line 4: multiply the allowable square footage by line 3c, capping at 300 square feet."
  - key: "1 (sc.ho_line1)"
    status: MATCH
    reason: "Within the supported simplified-method cases, line 1 is the amount from Schedule C line 29; other-location and Form 8949/4797 cases are refused."
  - key: "5 (sc.ho_line5)"
    status: MATCH
    reason: "The restatement implements the smaller-of line 1/line 4 rule within the supported cases and refuses the two-limit section 179/home-office interaction."
  - key: "30"
    status: MATCH
    reason: "Matches line 30: use the simplified-method line 5 amount when home-office use is claimed, otherwise zero."
  - key: "31"
    status: MATCH
    reason: "Matches line 31: subtract line 30 from line 29."
  - key: "32"
    status: MATCH
    reason: "Matches the box 32a at-risk description and the instructions' list of non-at-risk amounts."
  - key: "33"
    status: MATCH
    reason: "Matches the line 33/line 34 inventory-method and change screen, with other methods and changes refused."
  - key: "35"
    status: MATCH
    reason: "Matches line 35 beginning inventory within the supported no-method-change cases."
  - key: "36"
    status: MATCH
    reason: "Matches line 36: purchases less personal withdrawals."
  - key: "37"
    status: MATCH
    reason: "Matches line 37: cost of labor, excluding amounts paid to yourself."
  - key: "38"
    status: MATCH
    reason: "Matches line 38: materials and supplies."
  - key: "39"
    status: MATCH
    reason: "Matches line 39: other costs."
  - key: "40"
    status: MATCH
    reason: "Matches line 40: add lines 35 through 39."
  - key: "41"
    status: MATCH
    reason: "Matches line 41: inventory at end of year."
  - key: "42"
    status: MATCH
    reason: "Matches line 42: subtract line 41 from line 40."
  - key: "12 (sc.s179_allowed)"
    status: MATCH
    reason: "Matches the Form 4562 line 12 allocation approach: use the business election when there is no difference, otherwise use the return's only Schedule C section 179 deduction."
  - key: "(screen) (sc.hi_uses)"
    status: MATCH
    reason: "Matches Form 7206 and the Schedule 1 instructions on health insurance established under the business."
  - key: "(screen) (sc.hi_screen)"
    status: MATCH
    reason: "The listed Marketplace, Form 2555, S corporation, optional-method, retired-public-safety-officer, and multiple-business long-term-care cases are the Form 7206/instructions exclusions."
  - key: "1 (sc.f7206_line1)"
    status: MATCH
    reason: "Matches Form 7206 line 1, including medical, dental, vision, voluntary Medicare premiums, and the employer-subsidy and long-term-care exclusions."
  - key: "2 (sc.f7206_line2)"
    status: MATCH
    reason: "Matches Form 7206 line 2: aggregate each covered person's smaller-of amount for qualified long-term care insurance."
  - key: "3 (sc.f7206_line3)"
    status: MATCH
    reason: "Matches Form 7206 line 3: add lines 1 and 2."
  - key: "4 (sc.f7206_line4)"
    status: MISMATCH
    reason: "IRS line 4 says 'Enter your net profit* and any other earned income** from the trade or business under which the insurance plan is established'; the restatement uses only this business's net profit."
  - key: "5 (sc.f7206_line5)"
    status: MISMATCH
    reason: "IRS line 5 says 'total of all net profits* from Schedule C..., Schedule F..., or Schedule K-1..., plus any other income allocable to the profitable businesses'; the restatement uses only this person's Schedule C net profits."
  - key: "7 (sc.f7206_line7)"
    status: MATCH
    reason: "Matches Form 7206 lines 6 and 7: multiply Schedule 1 line 15 by line 4 divided by line 5, with zero when line 4 is not positive."
  - key: "8 (sc.f7206_line8)"
    status: MATCH
    reason: "Matches Form 7206 line 8: subtract line 7 from line 4."
  - key: "9 (sc.f7206_line9)"
    status: UNCLEAR
    reason: "IRS line 9 says only to enter the Schedule 1 line 16 amount 'attributable to the same trade or business'; it does not state the line 4/line 5 allocation used here."
  - key: "10 (sc.f7206_line10)"
    status: MATCH
    reason: "Matches Form 7206 line 10: subtract line 9 from line 8."
  - key: "13 (sc.f7206_line13)"
    status: MATCH
    reason: "Within the supported non-Form 2555, non-S-corporation cases, line 13 equals line 10 because line 12 is zero."
  - key: "14 (sc.f7206_line14)"
    status: MATCH
    reason: "Matches Form 7206 line 14: the smaller of line 3 or line 13, and zero when no health insurance is claimed."
  - key: "1(c)"
    status: MATCH
    reason: "The QBI instructions treat the deductible part of self-employment tax, self-employed health insurance, and qualified retirement plan contributions as business deductions; subtracting them matches the QBI computation."
  - key: "(screen) (sc.tips_ot)"
    status: MATCH
    reason: "Matches the Schedule C instructions and Schedule 1-A treatment of qualified tips and qualified overtime compensation."
```
