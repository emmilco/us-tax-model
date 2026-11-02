# Render comparison — sc

The rendered English of every printed line of `Schedule C (Form 1040) — Profit or Loss From Business, one per business` (`rendered/2025/sc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f60c85ff5ac5ca2b2b0c298e2a08432382365d82f8fa9de1ba12b22c86397f2e |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 2c5a09a2034d20b0effa3063dadcb5a2781932e2d7a91cc0e1b81375b42b0377 |
| lines judged | 75 |
| match / mismatch / unclear / missing | 69 / 4 / 2 / 0 |
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

Model: This screen identifies statutory employee income (box 13 of Form W-2) and notary fees, as the line 1 and line 31 instructions describe. Both cases are excluded by the refusal on line 1.

### G — Did you "materially participate" in the operation of this business during 2025, and is the
Status: **MATCH**

Model: It restates the 'Yes' test: not a rental activity, and any material participation test met or the oil and gas exception applies. The examples given track tests 1, 2 and 3, and it refers to all seven.

### (screen) (sc.spouse_owned) — Do you own this business together with your spouse (as a qualified joint venture, as commu
Status: **MATCH**

Model: This covers the spouse-owned arrangements in the instructions (partnership, qualified joint venture, community property). They are excluded by the refusal on line 1.

### F — Do you use an accounting method other than cash or accrual, or did you change your account
Status: **MATCH**

Model: This is a screen that refuses other accounting methods, method changes (Form 3115 or section 481(a)) and section 263A capitalization above the $31 million test. Those cases are named as excluded, and the threshold agrees with the small business taxpayer definition.

### (screen) (sc.special) — For this business, do you have any of these: depletion (line 12); the energy efficient com
Status: **MATCH**

Model: The listed items (depletion, Form 7205, employment credits, Form 8990, recapture and inclusion amounts, chapter 11, Form 8873, installment sales, Notice 2014-7, capital construction fund and others) appear in the instructions as special cases. All are refused, so they only narrow the supported cases.

### 1 (sc.line1) — Gross receipts or sales
Status: **MATCH**

Model: It asks for gross receipts, including amounts properly shown on Forms 1099-NEC and other Forms 1099, as the line 1 instructions say. Prizes and awards are correctly left for line 6, and excluded cases are refused.

### 2 (sc.line2) — Returns and allowances
Status: **MATCH**

Model: It asks for returns and allowances as a positive number, as the line 2 instructions say.

### 3 (sc.line3) — Subtract line 2 from line 1
Status: **MATCH**

Model: Form: 'Subtract line 2 from line 1.'

### 4 (sc.line4) — Cost of goods sold (from line 42)
Status: **MATCH**

Model: Form: 'Cost of goods sold (from line 42).'

### 5 (sc.line5) — Gross profit. Subtract line 4 from line 3
Status: **MATCH**

Model: Form: 'Subtract line 4 from line 3.'

### 6 — Other income, including federal and state gasoline or fuel tax credit or refund
Status: **MATCH**

Model: The examples are drawn from the line 6 list and are introduced by 'such as', with no change in what the line covers. Recapture and inclusion amounts and section 481(a) adjustments are excluded by the screens.

### 7 (sc.line7) — Gross income. Add lines 5 and 6
Status: **MATCH**

Model: Form: 'Add lines 5 and 6.'

### 8 (sc.line8) — Advertising
Status: **MATCH**

Model: It asks for advertising expense, which is the form's line 8.

### 9 (sc.line9) — Car and truck expenses
Status: **MATCH**

Model: Per vehicle it uses business miles times $0.70 plus parking and tolls, or the business portion of operating expenses plus parking and tolls. This agrees with the line 9 instructions, and depreciation and lease payments are kept off the line.

### 10 (sc.line10) — Commissions and fees
Status: **MATCH**

Model: It asks for commissions and fees, excluding those capitalized or deducted elsewhere, as the line 10 instructions say.

### 11 — Contract labor
Status: **MATCH**

Model: It asks for contract labor paid to persons not treated as employees, excluding amounts on lines 17, 21, 26 or 37, as the line 11 instructions say.

### 12 (sc.line12) — Depletion
Status: **MATCH**

Model: Depletion is entered as zero, and any depletion is refused through the special-items screen.

### 13 (sc.line13) — Depreciation and section 179 expense deduction (not included in Part III)
Status: **MATCH**

Model: It adds the section 179 deduction to depreciation from Form 4562 lines 14, 17, 19 and 21, consistent with Form 4562 line 22. The other line 22 components are excluded by the property screen.

### 14 (sc.line14) — Employee benefit programs (other than on line 19)
Status: **MATCH**

Model: It asks for employee benefit program contributions other than pension plans and excludes self-coverage, as the line 14 instructions say. Form 8941 reductions and self-employed dependent care are refused by the screen.

### 15 — Insurance (other than health)
Status: **MATCH**

Model: It asks for business insurance premiums and excludes self-insurance reserves and lost-earnings policies, as the line 15 instructions say.

### 16a — Interest: mortgage (paid to banks, etc.)
Status: **MATCH**

Model: It asks for mortgage interest on business real property paid to financial institutions with a Form 1098, excluding capitalized interest, as the 'How to report' instructions say.

### 16b — Interest: other
Status: **MATCH**

Model: It asks for other business interest, including mortgage interest not on a Form 1098, and excludes interest deducted on Schedule 1-A. This agrees with the instructions.

### 17 — Legal and professional services
Status: **MATCH**

Model: It asks for accountant and attorney fees directly related to the business, including tax advice and preparation, as the line 17 instructions say.

### 18 — Office expense
Status: **MATCH**

Model: Instructions: 'your expenses for office supplies and postage.'

### 19 — Pension and profit-sharing plans
Status: **MATCH**

Model: It asks for contributions for employees, including SEP, SIMPLE and SARSEP plans, with contributions for yourself sent to Schedule 1, line 16, as the line 19 instructions say.

### 20a — Rent or lease: vehicles, machinery, and equipment
Status: **MATCH**

Model: It adds the business portion of rent for machinery, equipment and vehicles, as the instructions say. The inclusion amount for leased vehicles is refused through the special-items screen.

### 20b — Rent or lease: other business property
Status: **MATCH**

Model: Instructions: 'amounts paid to rent or lease other property, such as office space in a building.'

### 21 — Repairs and maintenance
Status: **MATCH**

Model: It asks for incidental repairs and excludes your own labor and restorations or replacements, as the line 21 instructions say.

### 22 — Supplies (not included in Part III)
Status: **MATCH**

Model: It uses materials and supplies consumed and used, or incidental supplies purchased when no records are kept, as the line 22 instructions say.

### 23 — Taxes and licenses
Status: **MATCH**

Model: The included and excluded taxes follow the line 23 list, and the Form 8846 reduction is refused by the screen. The prompt does not mention the instructions' 'paid family and medical leave program' fund contributions, which is worth a wording fix.

### 24a — Travel
Status: **MATCH**

Model: It asks for lodging and transportation for overnight business travel away from the tax home, excluding meals and entertainment, as the line 24a instructions say.

### 24b — Deductible meals
Status: **UNCLEAR**

Restated: Add helper "50% of the meals subject to the 50% limit", helper "80% of the meals under the hours of service limits", and helper "Meals and incidentals not subject to the 50% limit, deducted in full".

Model: The 50%, 80% and full-deduction structure agrees with 'Amount of deduction', and the employee and nonemployee full-deduction cases are in the text. The other full-deduction categories (client-reimbursed meals, employee recreation, public promotion, meals sold) rest on Pub. 15 chapter 5 and Pub. 334 chapter 8, which are not provided.

Ruling: ambiguity (owner ruling T-042, amb.2025.meals_full_exceptions); restatement accepted. The 50% and 80% rates and the two full-deduction cases match i1040sc p. 10. The other categories come from Pub. 463 p. 16, which the instruction reaches through its references; the model was given the i1040sc pages only.

### 25 — Utilities
Status: **MATCH**

Model: It asks for business utilities and excludes the base rate of the first residential phone line, as the line 25 instructions say.

### 26 — Wages (less employment credits)
Status: **MATCH**

Model: It asks for employee salaries and wages, excluding amounts paid to yourself or deducted elsewhere. Reductions for employment credits are refused by the screen.

### 27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **MATCH**

Model: It is entered as zero, and the Form 7205 deduction is refused through the special-items screen.

### 48 — Total other expenses
Status: **MATCH**

Model: Form Part V: 'business expenses not included on lines 8-27a, or line 30.'

### 27b — Other expenses (from line 48)
Status: **MATCH**

Model: Form: 'Other expenses (from line 48).'

### 28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **MATCH**

Model: It adds every line from 8 through 27b, as the form says.

### 29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **MATCH**

Model: Form: 'Subtract line 28 from line 7.'

### (screen) (sc.ho_uses) — Do you claim a deduction for business use of your home for this business?
Status: **MATCH**

Model: It asks whether a home use deduction is claimed, using the instructions' regular and exclusive use and regular storage tests. Daycare is handled by the next screen.

### (screen) (sc.ho_other) — Does any of these apply to your business use of your home for this business?
Status: **MATCH**

Model: It identifies Form 8829, multiple homes, daycare, shared use, part-year or changed use, income from another location, and related gains or losses. These are the worksheet's special cases, and all are refused.

### 30(b) — The part of your home used for business (square feet)
Status: **MATCH**

Model: It asks for the square feet used for the business, and the refusals name the multi-business and special cases. This agrees with the form's entry space and the simplified method instructions.

### 30(a) — Total square footage of your home
Status: **MATCH**

Model: Form: 'the total square footage of (a) your home.'

### 3a — Maximum allowable amount (per square foot)
Status: **MATCH**

Model: Worksheet line 3a is printed as $5.

### 4 (sc.ho_line4) — Multiply line 2 by line 3c
Status: **MATCH**

Model: It multiplies the smaller of actual square feet or 300 by $5. Line 3b is 1.0 because daycare is refused, so this equals worksheet line 2 times line 3c.

### 1 (sc.ho_line1) — Gross income limitation (Schedule C, line 29)
Status: **MATCH**

Model: Instructions step A uses Schedule C, line 29. The gain, loss and other-location adjustments are excluded by the home office screen.

### 5 (sc.ho_line5) — Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4
Status: **MATCH**

Model: The result equals the worksheet's smaller of line 1 or line 4, floored at zero, where line 4 cannot be limited or no section 179 deduction is possible. The remaining case, with interdependent limits, is refused and cites Pub. 946.

### 30 — Expenses for business use of your home
Status: **MATCH**

Model: It enters worksheet line 5 when the deduction is claimed, as the instructions say: 'Include the amount from line 5 of the Simplified Method Worksheet on line 30.'

### 31 — Net profit or (loss). Subtract line 30 from line 29
Status: **MATCH**

Model: Form: 'Subtract line 30 from line 29.' Passive and at-risk loss limits are refused elsewhere.

### 32 — If you have a loss, is all your investment in this business at risk (box 32a)?
Status: **MATCH**

Model: It restates the box 32a and 32b test and the three not-at-risk examples. It omits the real property nonrecourse exception, but that only leads to a refusal, not a wrong value.

### 33 — Method used to value closing inventory: other than cost or lower of cost or market, or a c
Status: **MATCH**

Model: It combines lines 33 and 34 and sends other valuation methods or changes to a refusal, leaving cost or lower of cost or market.

### 35 — Inventory at beginning of year
Status: **MATCH**

Model: Form: 'Inventory at beginning of year.' A difference from last year's closing inventory arises from cases that are refused.

### 36 — Purchases less cost of items withdrawn for personal use
Status: **MATCH**

Model: Form: 'Purchases less cost of items withdrawn for personal use.'

### 37 — Cost of labor
Status: **MATCH**

Model: Form: 'Cost of labor. Do not include any amounts paid to yourself.'

### 38 — Materials and supplies
Status: **MATCH**

Model: Form: 'Materials and supplies.'

### 39 — Other costs
Status: **MATCH**

Model: Form: 'Other costs.'

### 40 — Add lines 35 through 39
Status: **MATCH**

Model: Form: 'Add lines 35 through 39.'

### 41 — Inventory at end of year
Status: **MATCH**

Model: Form: 'Inventory at end of year.'

### 42 — Cost of goods sold. Subtract line 41 from line 40
Status: **MATCH**

Model: Form: 'Subtract line 41 from line 40.'

### 12 (sc.s179_allowed) — Section 179 expense deduction for this business
Status: **MISMATCH**

Restated: Choose — [s179 helper "The deduction differs from the amounts elected for 2025" = false → helper "Section 179 elected for this business's 2025 property"] [s179 helper "The deduction differs from the amounts elected for 2025" = true → helper "The return's section 179 deduction, for its only Schedule C"]

Model: The return's deduction relies on Form 4562 line 1 being a flat $2,500,000, but Worksheet 1 says to enter the smaller of total section 179 cost or the limit: 'Enter the amount from line 3 here and on Form 4562, line 1.' With a carryover, line 5 and therefore lines 11 and 12 can differ: $10,000 of cost and a $5,000 carryover give $10,000 under the worksheet and $15,000 here.

Ruling: ambiguity (owner ruling T-043, amb.2025.s179_carryover_no_property); s179.line1 is the $2,500,000 limitation on the line 1 instruction's reading, and Worksheet 1's smaller-of reading is the recorded competing one.

### (screen) (sc.hi_uses) — Health insurance established under this business
Status: **MATCH**

Model: It asks about coverage for the persons named in the Form 7206 instructions (including a child under 27) under a policy in the business's or individual's name.

### (screen) (sc.hi_screen) — Does any of these apply to this health insurance?
Status: **MATCH**

Model: It identifies the Marketplace and premium tax credit, Form 2555, S corporation, optional method and retired public safety officer cases, plus long-term care across businesses. All are refused.

### 1 (sc.f7206_line1) — Health insurance payments (other than long-term care)
Status: **MATCH**

Model: It asks for premiums paid for the covered persons and excludes subsidized-plan months and long-term care, as Form 7206 line 1 says. Retirement plan payments are refused by the screen.

### 2 (sc.f7206_line2) — Qualified long-term care insurance (the smaller of payments or the age limit, for each per
Status: **MISMATCH**

Restated: Add ltc.amount over every confirmed ltc entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: The smaller-of test and total per person are right, but the helper excludes months when 'the person' was eligible for a subsidized plan. The form says: 'Don't include payments for any month you were eligible to participate in a long-term care insurance plan subsidized by your employer or your spouse's employer, or the employer of either your dependent or your child.' A covered person's premiums would be wrongly included when the filer is the one eligible.

Ruling: finding (BUG-0304, fixed in this pass); f7206 line 2: "any month you were eligible to participate in a long-term care insurance plan subsidized by your employer or your spouse's employer, or the employer of either your dependent or your child". ltc.payments tested the person covered; it now states the filer's test, and the ltc reviews were rerun on the new wording.

### 3 (sc.f7206_line3) — Add lines 1 and 2
Status: **MATCH**

Model: Form: 'Add lines 1 and 2.'

### 4 (sc.f7206_line4) — Net profit from the trade or business under which the insurance plan is established
Status: **MISMATCH**

Restated: Enter the amount from helper "Net profit of this business (zero for a loss)".

Model: It enters only this business's net profit. The form says: 'Enter your net profit* and any other earned income** from the trade or business,' and earned income includes gains from property you created. No screen excludes that income.

Ruling: scope; f7206 line 4 footnote: "Earned income includes net earnings and gains from the sale, transfer, or licensing of property you created. However, it doesn't include capital gain income." The tool admits no such income outside Schedule C: Form 4797 and other income are refused (sd.other_forms, scope.yaml), and Schedule F and K-1 profits are refused by the self-employment screen (person.x_other).

### 5 (sc.f7206_line5) — Total of all net profits from Schedule C, line 31
Status: **MISMATCH**

Restated: Enter the amount from person helper "Total of all net profits of this person's businesses (losses not included)".

Model: It totals only the Schedule C net profits. The form also adds 'plus any other income allocable to the profitable businesses,' and no screen excludes that income. Schedule F and K-1 profits are excluded by the self-employment screen, but this item is not.

Ruling: scope; f7206 line 4 footnote: "Earned income includes net earnings and gains from the sale, transfer, or licensing of property you created. However, it doesn't include capital gain income." The tool admits no such income outside Schedule C: Form 4797 and other income are refused (sd.other_forms, scope.yaml), and Schedule F and K-1 profits are refused by the self-employment screen (person.x_other). The same holds for "other income allocable to the profitable businesses".

### 7 (sc.f7206_line7) — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax, by the p
Status: **MATCH**

Model: It multiplies the deductible part of self-employment tax (Schedule SE line 13, which is Schedule 1 line 15) by line 4 divided by line 5, as lines 6 and 7 say. The six-decimal rounding is a computational detail.

### 8 (sc.f7206_line8) — Subtract line 7 from line 4
Status: **MATCH**

Model: Form: 'Subtract line 7 from line 4.' Line 7 is a part of the deductible tax on this profit, so the zero floor should not change the result.

### 9 (sc.f7206_line9) — Schedule 1, line 16, attributable to the same trade or business
Status: **MATCH**

Model: The form asks for the Schedule 1 line 16 amount attributable to this business. A plan with more than one Schedule C is refused, so the ratio is 1 and the full amount is attributed to the single business.

### 10 (sc.f7206_line10) — Subtract line 9 from line 8
Status: **MATCH**

Model: Form: 'Subtract line 9 from line 8.' The zero floor is consistent with the nonnegative limit on the deduction and with line 14's use.

### 13 (sc.f7206_line13) — Subtract line 12 from line 10
Status: **MATCH**

Model: The form subtracts line 12 from line 10. Line 12 is the Form 2555 amount, which is refused, so line 13 equals line 10.

### 14 (sc.f7206_line14) — Self-employed health insurance deduction
Status: **MATCH**

Model: Form: 'Enter the smaller of line 3 or line 13.' Zero is used where no plan is established under this business.

### 1(c) — Qualified business income or (loss) of this business
Status: **UNCLEAR**

Restated: Subtract helper "Deductions attributable to this business: self-employment tax, retirement plan and health insurance (Form 7206 for this business)" from helper "The amount for Schedule 1, line 3 and Schedule SE, line 2".

Model: Subtracting the self-employment tax deduction, retirement contributions and health insurance deduction agrees with the Form 8995 instructions on attributable items. The text does not say how to attribute the deductible self-employment tax among several businesses, so the net-profit-share allocation cannot be confirmed; the instructions' full QBI exclusions are also only partly provided.

Ruling: ambiguity (amb.2025.qbi_attribution); i8995 p. 2 names the attributable deductions but no allocation among businesses; the project prorates by net profit, the recorded reading.

### (screen) (sc.tips_ot) — Tips or overtime in this business to be deducted on Schedule 1-A
Status: **MATCH**

Model: It identifies qualified tips received in the business and qualified overtime reported on Form 1099-NEC or 1099-MISC, both deducted on Schedule 1-A, as the Schedule C and Schedule 1-A instructions describe.

## Raw response

```yaml
```yaml
lines:
  - key: "(screen) (sc.statutory)"
    status: MATCH
    reason: "This screen identifies statutory employee income (box 13 of Form W-2) and notary fees, as the line 1 and line 31 instructions describe. Both cases are excluded by the refusal on line 1."
  - key: "G"
    status: MATCH
    reason: "It restates the 'Yes' test: not a rental activity, and any material participation test met or the oil and gas exception applies. The examples given track tests 1, 2 and 3, and it refers to all seven."
  - key: "(screen) (sc.spouse_owned)"
    status: MATCH
    reason: "This covers the spouse-owned arrangements in the instructions (partnership, qualified joint venture, community property). They are excluded by the refusal on line 1."
  - key: "F"
    status: MATCH
    reason: "This is a screen that refuses other accounting methods, method changes (Form 3115 or section 481(a)) and section 263A capitalization above the $31 million test. Those cases are named as excluded, and the threshold agrees with the small business taxpayer definition."
  - key: "(screen) (sc.special)"
    status: MATCH
    reason: "The listed items (depletion, Form 7205, employment credits, Form 8990, recapture and inclusion amounts, chapter 11, Form 8873, installment sales, Notice 2014-7, capital construction fund and others) appear in the instructions as special cases. All are refused, so they only narrow the supported cases."
  - key: "1 (sc.line1)"
    status: MATCH
    reason: "It asks for gross receipts, including amounts properly shown on Forms 1099-NEC and other Forms 1099, as the line 1 instructions say. Prizes and awards are correctly left for line 6, and excluded cases are refused."
  - key: "2 (sc.line2)"
    status: MATCH
    reason: "It asks for returns and allowances as a positive number, as the line 2 instructions say."
  - key: "3 (sc.line3)"
    status: MATCH
    reason: "Form: 'Subtract line 2 from line 1.'"
  - key: "4 (sc.line4)"
    status: MATCH
    reason: "Form: 'Cost of goods sold (from line 42).'"
  - key: "5 (sc.line5)"
    status: MATCH
    reason: "Form: 'Subtract line 4 from line 3.'"
  - key: "6"
    status: MATCH
    reason: "The examples are drawn from the line 6 list and are introduced by 'such as', with no change in what the line covers. Recapture and inclusion amounts and section 481(a) adjustments are excluded by the screens."
  - key: "7 (sc.line7)"
    status: MATCH
    reason: "Form: 'Add lines 5 and 6.'"
  - key: "8 (sc.line8)"
    status: MATCH
    reason: "It asks for advertising expense, which is the form's line 8."
  - key: "9 (sc.line9)"
    status: MATCH
    reason: "Per vehicle it uses business miles times $0.70 plus parking and tolls, or the business portion of operating expenses plus parking and tolls. This agrees with the line 9 instructions, and depreciation and lease payments are kept off the line."
  - key: "10 (sc.line10)"
    status: MATCH
    reason: "It asks for commissions and fees, excluding those capitalized or deducted elsewhere, as the line 10 instructions say."
  - key: "11"
    status: MATCH
    reason: "It asks for contract labor paid to persons not treated as employees, excluding amounts on lines 17, 21, 26 or 37, as the line 11 instructions say."
  - key: "12 (sc.line12)"
    status: MATCH
    reason: "Depletion is entered as zero, and any depletion is refused through the special-items screen."
  - key: "13 (sc.line13)"
    status: MATCH
    reason: "It adds the section 179 deduction to depreciation from Form 4562 lines 14, 17, 19 and 21, consistent with Form 4562 line 22. The other line 22 components are excluded by the property screen."
  - key: "14 (sc.line14)"
    status: MATCH
    reason: "It asks for employee benefit program contributions other than pension plans and excludes self-coverage, as the line 14 instructions say. Form 8941 reductions and self-employed dependent care are refused by the screen."
  - key: "15"
    status: MATCH
    reason: "It asks for business insurance premiums and excludes self-insurance reserves and lost-earnings policies, as the line 15 instructions say."
  - key: "16a"
    status: MATCH
    reason: "It asks for mortgage interest on business real property paid to financial institutions with a Form 1098, excluding capitalized interest, as the 'How to report' instructions say."
  - key: "16b"
    status: MATCH
    reason: "It asks for other business interest, including mortgage interest not on a Form 1098, and excludes interest deducted on Schedule 1-A. This agrees with the instructions."
  - key: "17"
    status: MATCH
    reason: "It asks for accountant and attorney fees directly related to the business, including tax advice and preparation, as the line 17 instructions say."
  - key: "18"
    status: MATCH
    reason: "Instructions: 'your expenses for office supplies and postage.'"
  - key: "19"
    status: MATCH
    reason: "It asks for contributions for employees, including SEP, SIMPLE and SARSEP plans, with contributions for yourself sent to Schedule 1, line 16, as the line 19 instructions say."
  - key: "20a"
    status: MATCH
    reason: "It adds the business portion of rent for machinery, equipment and vehicles, as the instructions say. The inclusion amount for leased vehicles is refused through the special-items screen."
  - key: "20b"
    status: MATCH
    reason: "Instructions: 'amounts paid to rent or lease other property, such as office space in a building.'"
  - key: "21"
    status: MATCH
    reason: "It asks for incidental repairs and excludes your own labor and restorations or replacements, as the line 21 instructions say."
  - key: "22"
    status: MATCH
    reason: "It uses materials and supplies consumed and used, or incidental supplies purchased when no records are kept, as the line 22 instructions say."
  - key: "23"
    status: MATCH
    reason: "The included and excluded taxes follow the line 23 list, and the Form 8846 reduction is refused by the screen. The prompt does not mention the instructions' 'paid family and medical leave program' fund contributions, which is worth a wording fix."
  - key: "24a"
    status: MATCH
    reason: "It asks for lodging and transportation for overnight business travel away from the tax home, excluding meals and entertainment, as the line 24a instructions say."
  - key: "24b"
    status: UNCLEAR
    reason: "The 50%, 80% and full-deduction structure agrees with 'Amount of deduction', and the employee and nonemployee full-deduction cases are in the text. The other full-deduction categories (client-reimbursed meals, employee recreation, public promotion, meals sold) rest on Pub. 15 chapter 5 and Pub. 334 chapter 8, which are not provided."
  - key: "25"
    status: MATCH
    reason: "It asks for business utilities and excludes the base rate of the first residential phone line, as the line 25 instructions say."
  - key: "26"
    status: MATCH
    reason: "It asks for employee salaries and wages, excluding amounts paid to yourself or deducted elsewhere. Reductions for employment credits are refused by the screen."
  - key: "27a"
    status: MATCH
    reason: "It is entered as zero, and the Form 7205 deduction is refused through the special-items screen."
  - key: "48"
    status: MATCH
    reason: "Form Part V: 'business expenses not included on lines 8-27a, or line 30.'"
  - key: "27b"
    status: MATCH
    reason: "Form: 'Other expenses (from line 48).'"
  - key: "28"
    status: MATCH
    reason: "It adds every line from 8 through 27b, as the form says."
  - key: "29"
    status: MATCH
    reason: "Form: 'Subtract line 28 from line 7.'"
  - key: "(screen) (sc.ho_uses)"
    status: MATCH
    reason: "It asks whether a home use deduction is claimed, using the instructions' regular and exclusive use and regular storage tests. Daycare is handled by the next screen."
  - key: "(screen) (sc.ho_other)"
    status: MATCH
    reason: "It identifies Form 8829, multiple homes, daycare, shared use, part-year or changed use, income from another location, and related gains or losses. These are the worksheet's special cases, and all are refused."
  - key: "30(b)"
    status: MATCH
    reason: "It asks for the square feet used for the business, and the refusals name the multi-business and special cases. This agrees with the form's entry space and the simplified method instructions."
  - key: "30(a)"
    status: MATCH
    reason: "Form: 'the total square footage of (a) your home.'"
  - key: "3a"
    status: MATCH
    reason: "Worksheet line 3a is printed as $5."
  - key: "4 (sc.ho_line4)"
    status: MATCH
    reason: "It multiplies the smaller of actual square feet or 300 by $5. Line 3b is 1.0 because daycare is refused, so this equals worksheet line 2 times line 3c."
  - key: "1 (sc.ho_line1)"
    status: MATCH
    reason: "Instructions step A uses Schedule C, line 29. The gain, loss and other-location adjustments are excluded by the home office screen."
  - key: "5 (sc.ho_line5)"
    status: MATCH
    reason: "The result equals the worksheet's smaller of line 1 or line 4, floored at zero, where line 4 cannot be limited or no section 179 deduction is possible. The remaining case, with interdependent limits, is refused and cites Pub. 946."
  - key: "30"
    status: MATCH
    reason: "It enters worksheet line 5 when the deduction is claimed, as the instructions say: 'Include the amount from line 5 of the Simplified Method Worksheet on line 30.'"
  - key: "31"
    status: MATCH
    reason: "Form: 'Subtract line 30 from line 29.' Passive and at-risk loss limits are refused elsewhere."
  - key: "32"
    status: MATCH
    reason: "It restates the box 32a and 32b test and the three not-at-risk examples. It omits the real property nonrecourse exception, but that only leads to a refusal, not a wrong value."
  - key: "33"
    status: MATCH
    reason: "It combines lines 33 and 34 and sends other valuation methods or changes to a refusal, leaving cost or lower of cost or market."
  - key: "35"
    status: MATCH
    reason: "Form: 'Inventory at beginning of year.' A difference from last year's closing inventory arises from cases that are refused."
  - key: "36"
    status: MATCH
    reason: "Form: 'Purchases less cost of items withdrawn for personal use.'"
  - key: "37"
    status: MATCH
    reason: "Form: 'Cost of labor. Do not include any amounts paid to yourself.'"
  - key: "38"
    status: MATCH
    reason: "Form: 'Materials and supplies.'"
  - key: "39"
    status: MATCH
    reason: "Form: 'Other costs.'"
  - key: "40"
    status: MATCH
    reason: "Form: 'Add lines 35 through 39.'"
  - key: "41"
    status: MATCH
    reason: "Form: 'Inventory at end of year.'"
  - key: "42"
    status: MATCH
    reason: "Form: 'Subtract line 41 from line 40.'"
  - key: "12 (sc.s179_allowed)"
    status: MISMATCH
    reason: "The return's deduction relies on Form 4562 line 1 being a flat $2,500,000, but Worksheet 1 says to enter the smaller of total section 179 cost or the limit: 'Enter the amount from line 3 here and on Form 4562, line 1.' With a carryover, line 5 and therefore lines 11 and 12 can differ: $10,000 of cost and a $5,000 carryover give $10,000 under the worksheet and $15,000 here."
  - key: "(screen) (sc.hi_uses)"
    status: MATCH
    reason: "It asks about coverage for the persons named in the Form 7206 instructions (including a child under 27) under a policy in the business's or individual's name."
  - key: "(screen) (sc.hi_screen)"
    status: MATCH
    reason: "It identifies the Marketplace and premium tax credit, Form 2555, S corporation, optional method and retired public safety officer cases, plus long-term care across businesses. All are refused."
  - key: "1 (sc.f7206_line1)"
    status: MATCH
    reason: "It asks for premiums paid for the covered persons and excludes subsidized-plan months and long-term care, as Form 7206 line 1 says. Retirement plan payments are refused by the screen."
  - key: "2 (sc.f7206_line2)"
    status: MISMATCH
    reason: "The smaller-of test and total per person are right, but the helper excludes months when 'the person' was eligible for a subsidized plan. The form says: 'Don't include payments for any month you were eligible to participate in a long-term care insurance plan subsidized by your employer or your spouse's employer, or the employer of either your dependent or your child.' A covered person's premiums would be wrongly included when the filer is the one eligible."
  - key: "3 (sc.f7206_line3)"
    status: MATCH
    reason: "Form: 'Add lines 1 and 2.'"
  - key: "4 (sc.f7206_line4)"
    status: MISMATCH
    reason: "It enters only this business's net profit. The form says: 'Enter your net profit* and any other earned income** from the trade or business,' and earned income includes gains from property you created. No screen excludes that income."
  - key: "5 (sc.f7206_line5)"
    status: MISMATCH
    reason: "It totals only the Schedule C net profits. The form also adds 'plus any other income allocable to the profitable businesses,' and no screen excludes that income. Schedule F and K-1 profits are excluded by the self-employment screen, but this item is not."
  - key: "7 (sc.f7206_line7)"
    status: MATCH
    reason: "It multiplies the deductible part of self-employment tax (Schedule SE line 13, which is Schedule 1 line 15) by line 4 divided by line 5, as lines 6 and 7 say. The six-decimal rounding is a computational detail."
  - key: "8 (sc.f7206_line8)"
    status: MATCH
    reason: "Form: 'Subtract line 7 from line 4.' Line 7 is a part of the deductible tax on this profit, so the zero floor should not change the result."
  - key: "9 (sc.f7206_line9)"
    status: MATCH
    reason: "The form asks for the Schedule 1 line 16 amount attributable to this business. A plan with more than one Schedule C is refused, so the ratio is 1 and the full amount is attributed to the single business."
  - key: "10 (sc.f7206_line10)"
    status: MATCH
    reason: "Form: 'Subtract line 9 from line 8.' The zero floor is consistent with the nonnegative limit on the deduction and with line 14's use."
  - key: "13 (sc.f7206_line13)"
    status: MATCH
    reason: "The form subtracts line 12 from line 10. Line 12 is the Form 2555 amount, which is refused, so line 13 equals line 10."
  - key: "14 (sc.f7206_line14)"
    status: MATCH
    reason: "Form: 'Enter the smaller of line 3 or line 13.' Zero is used where no plan is established under this business."
  - key: "1(c)"
    status: UNCLEAR
    reason: "Subtracting the self-employment tax deduction, retirement contributions and health insurance deduction agrees with the Form 8995 instructions on attributable items. The text does not say how to attribute the deductible self-employment tax among several businesses, so the net-profit-share allocation cannot be confirmed; the instructions' full QBI exclusions are also only partly provided."
  - key: "(screen) (sc.tips_ot)"
    status: MATCH
    reason: "It identifies qualified tips received in the business and qualified overtime reported on Form 1099-NEC or 1099-MISC, both deducted on Schedule 1-A, as the Schedule C and Schedule 1-A instructions describe."
```
```
