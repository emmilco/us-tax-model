# Render comparison — sc

The rendered English of every printed line of `Schedule C (Form 1040) — Profit or Loss From Business, one per business` (`rendered/2025/sc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | f60c85ff5ac5ca2b2b0c298e2a08432382365d82f8fa9de1ba12b22c86397f2e |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 131072 |
| subject sha256 | 2c5a09a2034d20b0effa3063dadcb5a2781932e2d7a91cc0e1b81375b42b0377 |
| lines judged | 75 |
| match / mismatch / unclear / missing | 70 / 4 / 0 / 1 |
| verdicts for lines not in the form | 3a (sc.ho_rate) |

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

Model: Matches the Schedule C line 1 statutory employee box and the notary public screening in the instructions.

### G — Did you "materially participate" in the operation of this business during 2025, and is the
Status: **MATCH**

Model: Matches line G: not a rental activity and material participation or the oil and gas exception.

### (screen) (sc.spouse_owned) — Do you own this business together with your spouse (as a qualified joint venture, as commu
Status: **MATCH**

Model: Matches the spouse-owned business screening described under qualified joint venture, community income, and partnership rules.

### F — Do you use an accounting method other than cash or accrual, or did you change your account
Status: **MISMATCH**

Restated: Input — Do you use an accounting method other than cash or accrual, or did you change your accounting method for 2025 (Form 3115 or a section 481(a) adjustment), or must you capitalize costs under the uniform capitalization rules (section 263A) because your average annual gross receipts for the 3 prior years were more than $31 million?

Model: Line F asks only for the accounting method, including cash, accrual, other, and method changes via Form 3115; section 263A capitalization is a Part II/Part III matter, not a line F question.

Ruling: open

### (screen) (sc.special) — For this business, do you have any of these: depletion (line 12); the energy efficient com
Status: **MATCH**

Model: The listed special items correspond to the instructions' special items and line-specific exclusions.

### 1 (sc.line1) — Gross receipts or sales
Status: **MATCH**

Model: Matches line 1 gross receipts, including 1099-NEC and other 1099 business receipts, with the other-income exclusion.

### 2 (sc.line2) — Returns and allowances
Status: **MATCH**

Model: Matches line 2 returns and allowances as a positive number.

### 3 (sc.line3) — Subtract line 2 from line 1
Status: **MATCH**

Model: Matches line 3: subtract line 2 from line 1.

### 4 (sc.line4) — Cost of goods sold (from line 42)
Status: **MATCH**

Model: Matches line 4: cost of goods sold from line 42.

### 5 (sc.line5) — Gross profit. Subtract line 4 from line 3
Status: **MATCH**

Model: Matches line 5: subtract line 4 from line 3.

### 6 — Other income, including federal and state gasoline or fuel tax credit or refund
Status: **MATCH**

Model: Matches line 6 other business income examples; the list is illustrative.

### 7 (sc.line7) — Gross income. Add lines 5 and 6
Status: **MATCH**

Model: Matches line 7: add lines 5 and 6.

### 8 (sc.line8) — Advertising
Status: **MATCH**

Model: Matches line 8 advertising expenses.

### 9 (sc.line9) — Car and truck expenses
Status: **MATCH**

Model: Matches line 9 car and truck expenses by summing confirmed vehicle line 9 amounts.

### 10 (sc.line10) — Commissions and fees
Status: **MATCH**

Model: Matches line 10 commissions and fees not capitalized or deducted elsewhere.

### 11 — Contract labor
Status: **MATCH**

Model: Matches line 11 contract labor, excluding amounts deducted on lines 17, 21, 26, or 37.

### 12 (sc.line12) — Depletion
Status: **MATCH**

Model: Within the supported cases, depletion is screened out, so entering zero matches the line.

### 13 (sc.line13) — Depreciation and section 179 expense deduction (not included in Part III)
Status: **MATCH**

Model: Matches line 13: depreciation other than section 179 plus the section 179 deduction.

### 14 (sc.line14) — Employee benefit programs (other than on line 19)
Status: **MATCH**

Model: Matches line 14 employee benefit programs, excluding the self-employed person's own benefits and pension plans.

### 15 — Insurance (other than health)
Status: **MATCH**

Model: Matches line 15 business insurance premiums, excluding self-insurance reserves and lost-earnings insurance.

### 16a — Interest: mortgage (paid to banks, etc.)
Status: **MATCH**

Model: Matches line 16a mortgage interest paid to financial institutions with Form 1098, excluding capitalized interest.

### 16b — Interest: other
Status: **MATCH**

Model: Matches line 16b other business interest, including mortgage interest without Form 1098 and only the business vehicle-interest part.

### 17 — Legal and professional services
Status: **MATCH**

Model: Matches line 17 legal and professional fees directly related to the business.

### 18 — Office expense
Status: **MATCH**

Model: Matches line 18 office supplies and postage.

### 19 — Pension and profit-sharing plans
Status: **MATCH**

Model: Matches line 19 employee pension, profit-sharing, and annuity contributions, excluding the self-employed person's own contributions.

### 20a — Rent or lease: vehicles, machinery, and equipment
Status: **MATCH**

Model: Matches line 20a vehicle, machinery, and equipment rent or lease amounts.

### 20b — Rent or lease: other business property
Status: **MATCH**

Model: Matches line 20b rent for other business property.

### 21 — Repairs and maintenance
Status: **MATCH**

Model: Matches line 21 incidental repairs and maintenance, excluding own labor and capitalized restorations or replacements.

### 22 — Supplies (not included in Part III)
Status: **MATCH**

Model: Matches line 22 materials and supplies actually consumed and used, with the incidental-supplies rule.

### 23 — Taxes and licenses
Status: **MATCH**

Model: Matches line 23 business taxes and licenses; the wording is a reasonable summary of the listed taxes and exclusions.

### 24a — Travel
Status: **MATCH**

Model: Matches line 24a lodging and transportation for overnight business travel, excluding meals and entertainment.

### 24b — Deductible meals
Status: **MATCH**

Model: Matches line 24b by adding 50% meals, 80% DOT meals, and fully deductible meals.

### 25 — Utilities
Status: **MATCH**

Model: Matches line 25 business utility expenses and the first-home-phone-line limitation.

### 26 — Wages (less employment credits)
Status: **MATCH**

Model: Matches line 26 salaries and wages, excluding amounts paid to yourself and wages deducted elsewhere; employment credits are screened.

### 27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **MATCH**

Model: Within the supported cases, the energy efficient commercial buildings deduction is screened out, so zero matches.

### 48 — Total other expenses
Status: **MATCH**

Model: Matches line 48 total other expenses from Part V, excluding lines 8 through 27a and line 30.

### 27b — Other expenses (from line 48)
Status: **MATCH**

Model: Matches line 27b: other expenses from line 48.

### 28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **MATCH**

Model: Matches line 28 total expenses before home office by adding lines 8 through 27b.

### 29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **MATCH**

Model: Matches line 29: subtract line 28 from line 7.

### (screen) (sc.ho_uses) — Do you claim a deduction for business use of your home for this business?
Status: **MATCH**

Model: Matches the home-office-use question, with the special cases screened elsewhere.

### (screen) (sc.ho_other) — Does any of these apply to your business use of your home for this business?
Status: **MATCH**

Model: Matches the special simplified-method situations that the program declines to handle.

### 30(b) — The part of your home used for business (square feet)
Status: **MATCH**

Model: Matches the part of the home used for business, with the 300-square-foot allocation and special cases refused.

### 30(a) — Total square footage of your home
Status: **MATCH**

Model: Matches the simplified-method entry for total square footage of the home.

### 3a — Maximum allowable amount (per square foot)
Status: **MISSING**

Restated: Enter $5 (sc.ho_rate).

Model: the model returned no verdict for this line

Ruling: open

### 4 (sc.ho_line4) — Multiply line 2 by line 3c
Status: **MATCH**

Model: Matches worksheet line 4: line 2 times line 3c, with the 300-square-foot cap.

### 1 (sc.ho_line1) — Gross income limitation (Schedule C, line 29)
Status: **MATCH**

Model: Within the supported no-other-location/no-gain-loss case, the gross income limitation is line 29.

### 5 (sc.ho_line5) — Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4
Status: **MATCH**

Model: Implements the smaller-of-line-1-or-line-4 limitation with the section 179 ordering and refuses the two-limit case.

### 30 — Expenses for business use of your home
Status: **MATCH**

Model: Matches line 30: use the simplified-method line 5 amount if a home-office deduction is claimed, otherwise zero.

### 31 — Net profit or (loss). Subtract line 30 from line 29
Status: **MATCH**

Model: Matches line 31: subtract line 30 from line 29.

### 32 — If you have a loss, is all your investment in this business at risk (box 32a)?
Status: **MATCH**

Model: Matches line 32 at-risk boxes and the listed non-at-risk investment categories.

### 33 — Method used to value closing inventory: other than cost or lower of cost or market, or a c
Status: **MATCH**

Model: The combined other-method/line 34 change screen is refused on line 35, so within supported cases it matches.

### 35 — Inventory at beginning of year
Status: **MATCH**

Model: Matches beginning inventory, treated as prior-year closing inventory when no inventory method change is present.

### 36 — Purchases less cost of items withdrawn for personal use
Status: **MATCH**

Model: Matches line 36 purchases less personal withdrawals.

### 37 — Cost of labor
Status: **MATCH**

Model: Matches line 37 cost of labor, excluding amounts paid to yourself.

### 38 — Materials and supplies
Status: **MATCH**

Model: Matches line 38 materials and supplies.

### 39 — Other costs
Status: **MATCH**

Model: Matches line 39 other costs.

### 40 — Add lines 35 through 39
Status: **MATCH**

Model: Matches line 40: add lines 35 through 39.

### 41 — Inventory at end of year
Status: **MATCH**

Model: Matches line 41 ending inventory.

### 42 — Cost of goods sold. Subtract line 41 from line 40
Status: **MATCH**

Model: Matches line 42: subtract line 41 from line 40.

### 12 (sc.s179_allowed) — Section 179 expense deduction for this business
Status: **MATCH**

Model: Matches the section 179 deduction allocation for one Schedule C, with the multi-business allocation refused.

### (screen) (sc.hi_uses) — Health insurance established under this business
Status: **MATCH**

Model: Matches the Form 7206 line 1 health insurance coverage question.

### (screen) (sc.hi_screen) — Does any of these apply to this health insurance?
Status: **MATCH**

Model: Matches the Form 7206 and Schedule 1 health insurance situations that require other forms or are outside this tool.

### 1 (sc.f7206_line1) — Health insurance payments (other than long-term care)
Status: **MATCH**

Model: Matches Form 7206 line 1, including Medicare premiums and the employer-subsidy and long-term-care exclusions; screened cases are refused.

### 2 (sc.f7206_line2) — Qualified long-term care insurance (the smaller of payments or the age limit, for each per
Status: **MATCH**

Model: Matches Form 7206 line 2 by totaling each covered person's smaller-of (a) or (b) amount.

### 3 (sc.f7206_line3) — Add lines 1 and 2
Status: **MATCH**

Model: Matches Form 7206 line 3: add lines 1 and 2.

### 4 (sc.f7206_line4) — Net profit from the trade or business under which the insurance plan is established
Status: **MISMATCH**

Restated: Enter the amount from helper "Net profit of this business (zero for a loss)".

Model: IRS line 4 says 'Enter your net profit* and any other earned income** from the trade or business'; the restatement uses only net profit, zero for a loss.

Ruling: open

### 5 (sc.f7206_line5) — Total of all net profits from Schedule C, line 31
Status: **MISMATCH**

Restated: Enter the amount from person helper "Total of all net profits of this person's businesses (losses not included)".

Model: IRS line 5 requires 'the total of all net profits from Schedule C..., Schedule F..., or Schedule K-1..., plus any other income'; the restatement sums only Schedule C net profits.

Ruling: open

### 7 (sc.f7206_line7) — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax, by the p
Status: **MATCH**

Model: Matches Form 7206 line 7: multiply Schedule 1 line 15 by line 4 divided by line 5.

### 8 (sc.f7206_line8) — Subtract line 7 from line 4
Status: **MATCH**

Model: Matches Form 7206 line 8: subtract line 7 from line 4; the zero floor does not affect supported positive-profit cases.

### 9 (sc.f7206_line9) — Schedule 1, line 16, attributable to the same trade or business
Status: **MISMATCH**

Restated: Choose — [helper "Line 4 is more than zero" = true → helper "This person's SEP or SIMPLE deduction times line 4 divided by line 5"] [helper "Line 4 is more than zero" = false → helper "Zero"]

Model: IRS line 9 includes 'Schedule 1..., line 16, self-employed SEP, SIMPLE, and qualified plans'; the restatement uses only the SEP or SIMPLE deduction.

Ruling: open

### 10 (sc.f7206_line10) — Subtract line 9 from line 8
Status: **MATCH**

Model: Matches Form 7206 line 10: subtract line 9 from line 8; the zero floor does not affect supported cases.

### 13 (sc.f7206_line13) — Subtract line 12 from line 10
Status: **MATCH**

Model: Within the supported no-Form-2555/no-S-corporation cases, line 13 is line 10.

### 14 (sc.f7206_line14) — Self-employed health insurance deduction
Status: **MATCH**

Model: Matches Form 7206 line 14: smaller of line 3 or line 13 when the plan is established under the business.

### 1(c) — Qualified business income or (loss) of this business
Status: **MATCH**

Model: Matches Form 8995 QBI by reducing business income by the attributable self-employment tax, retirement plan, and health insurance deductions.

### (screen) (sc.tips_ot) — Tips or overtime in this business to be deducted on Schedule 1-A
Status: **MATCH**

Model: Matches the Schedule 1-A screening for qualified tips and qualified overtime compensation.

## Raw response

```yaml
lines:
  - key: "(screen) (sc.statutory)"
    status: MATCH
    reason: "Matches the Schedule C line 1 statutory employee box and the notary public screening in the instructions."
  - key: "G"
    status: MATCH
    reason: "Matches line G: not a rental activity and material participation or the oil and gas exception."
  - key: "(screen) (sc.spouse_owned)"
    status: MATCH
    reason: "Matches the spouse-owned business screening described under qualified joint venture, community income, and partnership rules."
  - key: "F"
    status: MISMATCH
    reason: "Line F asks only for the accounting method, including cash, accrual, other, and method changes via Form 3115; section 263A capitalization is a Part II/Part III matter, not a line F question."
  - key: "(screen) (sc.special)"
    status: MATCH
    reason: "The listed special items correspond to the instructions' special items and line-specific exclusions."
  - key: "1 (sc.line1)"
    status: MATCH
    reason: "Matches line 1 gross receipts, including 1099-NEC and other 1099 business receipts, with the other-income exclusion."
  - key: "2 (sc.line2)"
    status: MATCH
    reason: "Matches line 2 returns and allowances as a positive number."
  - key: "3 (sc.line3)"
    status: MATCH
    reason: "Matches line 3: subtract line 2 from line 1."
  - key: "4 (sc.line4)"
    status: MATCH
    reason: "Matches line 4: cost of goods sold from line 42."
  - key: "5 (sc.line5)"
    status: MATCH
    reason: "Matches line 5: subtract line 4 from line 3."
  - key: "6"
    status: MATCH
    reason: "Matches line 6 other business income examples; the list is illustrative."
  - key: "7 (sc.line7)"
    status: MATCH
    reason: "Matches line 7: add lines 5 and 6."
  - key: "8 (sc.line8)"
    status: MATCH
    reason: "Matches line 8 advertising expenses."
  - key: "9 (sc.line9)"
    status: MATCH
    reason: "Matches line 9 car and truck expenses by summing confirmed vehicle line 9 amounts."
  - key: "10 (sc.line10)"
    status: MATCH
    reason: "Matches line 10 commissions and fees not capitalized or deducted elsewhere."
  - key: "11"
    status: MATCH
    reason: "Matches line 11 contract labor, excluding amounts deducted on lines 17, 21, 26, or 37."
  - key: "12 (sc.line12)"
    status: MATCH
    reason: "Within the supported cases, depletion is screened out, so entering zero matches the line."
  - key: "13 (sc.line13)"
    status: MATCH
    reason: "Matches line 13: depreciation other than section 179 plus the section 179 deduction."
  - key: "14 (sc.line14)"
    status: MATCH
    reason: "Matches line 14 employee benefit programs, excluding the self-employed person's own benefits and pension plans."
  - key: "15"
    status: MATCH
    reason: "Matches line 15 business insurance premiums, excluding self-insurance reserves and lost-earnings insurance."
  - key: "16a"
    status: MATCH
    reason: "Matches line 16a mortgage interest paid to financial institutions with Form 1098, excluding capitalized interest."
  - key: "16b"
    status: MATCH
    reason: "Matches line 16b other business interest, including mortgage interest without Form 1098 and only the business vehicle-interest part."
  - key: "17"
    status: MATCH
    reason: "Matches line 17 legal and professional fees directly related to the business."
  - key: "18"
    status: MATCH
    reason: "Matches line 18 office supplies and postage."
  - key: "19"
    status: MATCH
    reason: "Matches line 19 employee pension, profit-sharing, and annuity contributions, excluding the self-employed person's own contributions."
  - key: "20a"
    status: MATCH
    reason: "Matches line 20a vehicle, machinery, and equipment rent or lease amounts."
  - key: "20b"
    status: MATCH
    reason: "Matches line 20b rent for other business property."
  - key: "21"
    status: MATCH
    reason: "Matches line 21 incidental repairs and maintenance, excluding own labor and capitalized restorations or replacements."
  - key: "22"
    status: MATCH
    reason: "Matches line 22 materials and supplies actually consumed and used, with the incidental-supplies rule."
  - key: "23"
    status: MATCH
    reason: "Matches line 23 business taxes and licenses; the wording is a reasonable summary of the listed taxes and exclusions."
  - key: "24a"
    status: MATCH
    reason: "Matches line 24a lodging and transportation for overnight business travel, excluding meals and entertainment."
  - key: "24b"
    status: MATCH
    reason: "Matches line 24b by adding 50% meals, 80% DOT meals, and fully deductible meals."
  - key: "25"
    status: MATCH
    reason: "Matches line 25 business utility expenses and the first-home-phone-line limitation."
  - key: "26"
    status: MATCH
    reason: "Matches line 26 salaries and wages, excluding amounts paid to yourself and wages deducted elsewhere; employment credits are screened."
  - key: "27a"
    status: MATCH
    reason: "Within the supported cases, the energy efficient commercial buildings deduction is screened out, so zero matches."
  - key: "48"
    status: MATCH
    reason: "Matches line 48 total other expenses from Part V, excluding lines 8 through 27a and line 30."
  - key: "27b"
    status: MATCH
    reason: "Matches line 27b: other expenses from line 48."
  - key: "28"
    status: MATCH
    reason: "Matches line 28 total expenses before home office by adding lines 8 through 27b."
  - key: "29"
    status: MATCH
    reason: "Matches line 29: subtract line 28 from line 7."
  - key: "(screen) (sc.ho_uses)"
    status: MATCH
    reason: "Matches the home-office-use question, with the special cases screened elsewhere."
  - key: "(screen) (sc.ho_other)"
    status: MATCH
    reason: "Matches the special simplified-method situations that the program declines to handle."
  - key: "30(b)"
    status: MATCH
    reason: "Matches the part of the home used for business, with the 300-square-foot allocation and special cases refused."
  - key: "30(a)"
    status: MATCH
    reason: "Matches the simplified-method entry for total square footage of the home."
  - key: "3a (sc.ho_rate)"
    status: MATCH
    reason: "Matches Simplified Method Worksheet line 3a: $5."
  - key: "4 (sc.ho_line4)"
    status: MATCH
    reason: "Matches worksheet line 4: line 2 times line 3c, with the 300-square-foot cap."
  - key: "1 (sc.ho_line1)"
    status: MATCH
    reason: "Within the supported no-other-location/no-gain-loss case, the gross income limitation is line 29."
  - key: "5 (sc.ho_line5)"
    status: MATCH
    reason: "Implements the smaller-of-line-1-or-line-4 limitation with the section 179 ordering and refuses the two-limit case."
  - key: "30"
    status: MATCH
    reason: "Matches line 30: use the simplified-method line 5 amount if a home-office deduction is claimed, otherwise zero."
  - key: "31"
    status: MATCH
    reason: "Matches line 31: subtract line 30 from line 29."
  - key: "32"
    status: MATCH
    reason: "Matches line 32 at-risk boxes and the listed non-at-risk investment categories."
  - key: "33"
    status: MATCH
    reason: "The combined other-method/line 34 change screen is refused on line 35, so within supported cases it matches."
  - key: "35"
    status: MATCH
    reason: "Matches beginning inventory, treated as prior-year closing inventory when no inventory method change is present."
  - key: "36"
    status: MATCH
    reason: "Matches line 36 purchases less personal withdrawals."
  - key: "37"
    status: MATCH
    reason: "Matches line 37 cost of labor, excluding amounts paid to yourself."
  - key: "38"
    status: MATCH
    reason: "Matches line 38 materials and supplies."
  - key: "39"
    status: MATCH
    reason: "Matches line 39 other costs."
  - key: "40"
    status: MATCH
    reason: "Matches line 40: add lines 35 through 39."
  - key: "41"
    status: MATCH
    reason: "Matches line 41 ending inventory."
  - key: "42"
    status: MATCH
    reason: "Matches line 42: subtract line 41 from line 40."
  - key: "12 (sc.s179_allowed)"
    status: MATCH
    reason: "Matches the section 179 deduction allocation for one Schedule C, with the multi-business allocation refused."
  - key: "(screen) (sc.hi_uses)"
    status: MATCH
    reason: "Matches the Form 7206 line 1 health insurance coverage question."
  - key: "(screen) (sc.hi_screen)"
    status: MATCH
    reason: "Matches the Form 7206 and Schedule 1 health insurance situations that require other forms or are outside this tool."
  - key: "1 (sc.f7206_line1)"
    status: MATCH
    reason: "Matches Form 7206 line 1, including Medicare premiums and the employer-subsidy and long-term-care exclusions; screened cases are refused."
  - key: "2 (sc.f7206_line2)"
    status: MATCH
    reason: "Matches Form 7206 line 2 by totaling each covered person's smaller-of (a) or (b) amount."
  - key: "3 (sc.f7206_line3)"
    status: MATCH
    reason: "Matches Form 7206 line 3: add lines 1 and 2."
  - key: "4 (sc.f7206_line4)"
    status: MISMATCH
    reason: "IRS line 4 says 'Enter your net profit* and any other earned income** from the trade or business'; the restatement uses only net profit, zero for a loss."
  - key: "5 (sc.f7206_line5)"
    status: MISMATCH
    reason: "IRS line 5 requires 'the total of all net profits from Schedule C..., Schedule F..., or Schedule K-1..., plus any other income'; the restatement sums only Schedule C net profits."
  - key: "7 (sc.f7206_line7)"
    status: MATCH
    reason: "Matches Form 7206 line 7: multiply Schedule 1 line 15 by line 4 divided by line 5."
  - key: "8 (sc.f7206_line8)"
    status: MATCH
    reason: "Matches Form 7206 line 8: subtract line 7 from line 4; the zero floor does not affect supported positive-profit cases."
  - key: "9 (sc.f7206_line9)"
    status: MISMATCH
    reason: "IRS line 9 includes 'Schedule 1..., line 16, self-employed SEP, SIMPLE, and qualified plans'; the restatement uses only the SEP or SIMPLE deduction."
  - key: "10 (sc.f7206_line10)"
    status: MATCH
    reason: "Matches Form 7206 line 10: subtract line 9 from line 8; the zero floor does not affect supported cases."
  - key: "13 (sc.f7206_line13)"
    status: MATCH
    reason: "Within the supported no-Form-2555/no-S-corporation cases, line 13 is line 10."
  - key: "14 (sc.f7206_line14)"
    status: MATCH
    reason: "Matches Form 7206 line 14: smaller of line 3 or line 13 when the plan is established under the business."
  - key: "1(c)"
    status: MATCH
    reason: "Matches Form 8995 QBI by reducing business income by the attributable self-employment tax, retirement plan, and health insurance deductions."
  - key: "(screen) (sc.tips_ot)"
    status: MATCH
    reason: "Matches the Schedule 1-A screening for qualified tips and qualified overtime compensation."
```
