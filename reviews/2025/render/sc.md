# Render comparison — sc

The rendered English of every printed line of `Schedule C (Form 1040) — Profit or Loss From Business, one per business` (`rendered/2025/sc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 4a5a760dd9440b77acff50e01a51a324e65821b1dd5314e468fc83dc1da28f7c |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | bcf2bc57eaed5335fa82db1b7a05d5d76cae7fedb326ebbd7ae8ff9eb4310271 |
| lines judged | 75 |
| match / mismatch / unclear / missing | 75 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 31, 32, 34, 37, 39, 41, 59, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 31, 32, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i1040gi | 2025; printed date 2026-02-25 | 93, 94, 95, 104, 108, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 93, 95, 104, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8995 | 2025; printed date 2026-01-26 | 2, 4, 6 | cited pages | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 2, 4, 6 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| iw2w3 | 2025; printed date 2025-02-19 | 18 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 18 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| p560 | For use in preparing 2025 returns | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 39, 40 | cited pages | 38bbfa2efb2894e2527d66cd3478f33c6ceae4b777f78674c22bec16db9809aa | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 40 | 7ef279c8f34addc2ff13420e35fab4a092bf8027f53907c28a5f46d2c21da737 |
| p538 | None | 17 | pages named by another document's citation | 4186d7aaa8f711c9a524b87fac1e3df05640b6d66130093b2469480acb06ef6c | 17 | f500211df18a4aafd843e48bbad4b9102c598cf5ccc0fae96c7814a4bef0ae00 |
| p463 | For use in preparing 2025 returns | 12 | pages named by another document's citation | 153efad2a94bcccadf643b0f28f913d74b7d70b727f73eca540a2ce4d32bbfda | 12 | a0b14576fdb49a7ba3e7a90092c1b8f6b8ba33889c8c35da5629156346581326 |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |

## Lines

### (screen) (sc.statutory) — Is this business income you received as a statutory employee (the "Statutory employee" box
Status: **MATCH**

Model: This screens out statutory employee income (W-2 box 13 checked) and notary fees. The Schedule C instructions treat both specially, and the sc.screened refusal names them.

### G — Did you "materially participate" in the operation of this business during 2025, and is the
Status: **MATCH**

Model: It follows the line G instruction: not a rental activity and one of the material participation tests is met, or the oil and gas working interest exception applies. The tests it summarizes (500 hours, substantially all, 100 hours and at least as much as anyone) match the seven-test list.

### (screen) (sc.spouse_owned) — Do you own this business together with your spouse (as a qualified joint venture, as commu
Status: **MATCH**

Model: This screens out spouse-owned businesses (qualified joint venture, community property or partnership). The instructions give these special treatment, and the refusal names them.

### F — Do you use an accounting method other than cash or accrual, or did you change your account
Status: **MATCH**

Model: This is a screen for other accounting methods, method changes (Form 3115, section 481(a)), UNICAP for businesses over the $31 million gross receipts test, tax shelters under section 448(d)(3) and section 460 long-term contracts. All of these appear in the line F and Part III text, and the refusal excludes them.

### (screen) (sc.special) — For this business, do you have any of these: depletion (line 12); the energy efficient com
Status: **MATCH**

Model: Each listed item is a special case named in the instructions: depletion, Form 7205, credit reductions, Form 8990, recapture, chapter 11, Form 8873, installment method, Notice 2014-7, CCF, and so on. The refusal excludes all of them.

### 1 (sc.line1) — Gross receipts or sales
Status: **MATCH**

Model: Gross receipts include amounts properly shown on Forms 1099-NEC and sales tax imposed on the seller that was collected from buyers ('you must also include the amount collected in gross receipts'). NIL income that is not self-employment income goes on Schedule E. The screened cases are refused.

### 2 (sc.line2) — Returns and allowances
Status: **MATCH**

Model: This matches 'Report your sales returns and allowances as a positive number on line 2.'

### 3 (sc.line3) — Subtract line 2 from line 1
Status: **MATCH**

Model: This matches 'Subtract line 2 from line 1.'

### 4 (sc.line4) — Cost of goods sold (from line 42)
Status: **MATCH**

Model: This matches 'Cost of goods sold (from line 42).'

### 5 (sc.line5) — Gross profit. Subtract line 4 from line 3
Status: **MATCH**

Model: This matches 'Gross profit. Subtract line 4 from line 3.'

### 6 — Other income, including federal and state gasoline or fuel tax credit or refund
Status: **MATCH**

Model: The items listed come from the line 6 list, including fuel tax refunds, the fuel tax credit, prizes and 1099-PATR amounts. Retained sales tax comes from the line 23 instructions. The list is open-ended ('such as'), and the recapture and 481(a) items are screened.

### 7 (sc.line7) — Gross income. Add lines 5 and 6
Status: **MATCH**

Model: This matches 'Gross income. Add lines 5 and 6.'

### 8 (sc.line8) — Advertising
Status: **MATCH**

Model: This is advertising expense, as printed.

### 9 (sc.line9) — Car and truck expenses
Status: **MATCH**

Model: Under the standard mileage rate it is business miles times $0.70 plus parking fees and tolls. Under actual expenses it is the business portion of operating expenses. Both follow the line 9 instructions, and the cases where the standard rate is unavailable are refused.

### 10 (sc.line10) — Commissions and fees
Status: **MATCH**

Model: This matches 'Do not include commissions or fees that are capitalized or deducted elsewhere.'

### 11 — Contract labor
Status: **MATCH**

Model: Contract labor excludes amounts includible on lines 17, 21, 26 or 37, as the instructions state.

### 12 (sc.line12) — Depletion
Status: **MATCH**

Model: Depletion is zero because depletion is screened out in sc.special and refused.

### 13 (sc.line13) — Depreciation and section 179 expense deduction (not included in Part III)
Status: **MATCH**

Model: It adds Form 4562 lines 14, 17, 19 and the listed-property line 28 to this business's section 179 deduction, which mirrors the line 22 total. The lines 15, 16 and 20 cases (other methods, ADS) are screened.

### 14 (sc.line14) — Employee benefit programs (other than on line 19)
Status: **MATCH**

Model: It covers employee benefit programs other than pension plans (line 19) and excludes contributions for yourself, as the line 14 text says. The Form 8941 and Form 2441 cases are screened.

### 15 — Insurance (other than health)
Status: **MATCH**

Model: It excludes reserves for self-insurance and lost-earnings policies, as line 15 says. Employee health insurance belongs on line 14.

### 16a — Interest: mortgage (paid to banks, etc.)
Status: **MATCH**

Model: This is mortgage interest paid to financial institutions and reported on Form 1098, excluding capitalized interest, as the line 16a instructions describe.

### 16b — Interest: other
Status: **MATCH**

Model: It covers other interest, including mortgage interest without a Form 1098 to you, your share when another person received the Form 1098, only the part that applies to 2025, and no interest claimed on Schedule 1-A. All of this follows the instructions.

### 17 — Legal and professional services
Status: **MATCH**

Model: This is accountant and attorney fees directly related to operating the business, including tax advice and tax preparation. The list is inclusive.

### 18 — Office expense
Status: **MATCH**

Model: This matches 'expenses for office supplies and postage.'

### 19 — Pension and profit-sharing plans
Status: **MATCH**

Model: These are contributions for employees, with contributions for yourself going on Schedule 1, line 16, as the line 19 text says.

### 20a — Rent or lease: vehicles, machinery, and equipment
Status: **MATCH**

Model: It is the business portion of rent for vehicles, machinery and equipment, with lease payments allowed only under actual expenses. The inclusion amount for 30-day-or-longer leases is screened.

### 20b — Rent or lease: other business property
Status: **MATCH**

Model: This matches 'amounts paid to rent or lease other property, such as office space.'

### 21 — Repairs and maintenance
Status: **MATCH**

Model: This follows the line 21 text: incidental repairs only, not your own labor, and not restorations.

### 22 — Supplies (not included in Part III)
Status: **MATCH**

Model: It covers materials consumed and used, or incidental supplies purchased if no records are kept, plus items normally used within a year, as the line 22 text says.

### 23 — Taxes and licenses
Status: **MATCH**

Model: The deductible taxes and the exclusions follow the line 23 lists. The Form 8846 reduction and amortized licenses are screened.

### 24a — Travel
Status: **MATCH**

Model: It follows the line 24a text: lodging and transportation, incidentals at actual cost or $5 a day only on days with no meals, the 1-year limit, the rule for spouses and dependents, and the North American area convention rule. Luxury water travel is screened.

### 24b — Deductible meals
Status: **MATCH**

Model: It applies 50% generally, 80% for meals under the DOT hours of service limits, and 100% for the fully deductible exceptions, as in 'Amount of deduction.'

### 25 — Utilities
Status: **MATCH**

Model: These are business utilities only, excluding the base rate of the first home phone line.

### 26 — Wages (less employment credits)
Status: **MATCH**

Model: Wages exclude amounts paid to yourself, wages deducted elsewhere, and depreciation in fringe benefits. The employment credit reductions are screened.

### 27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **MATCH**

Model: It is zero because the Form 7205 deduction is screened and refused.

### 48 — Total other expenses
Status: **MATCH**

Model: This matches Part V: 'business expenses not included on lines 8-27a, or line 30.'

### 27b — Other expenses (from line 48)
Status: **MATCH**

Model: This matches 'Other expenses (from line 48).'

### 28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **MATCH**

Model: This matches 'Add lines 8 through 27b.'

### 29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **MATCH**

Model: This matches 'Subtract line 28 from line 7.'

### (screen) (sc.ho_uses) — Do you claim a deduction for business use of your home for this business?
Status: **MATCH**

Model: It asks whether a home office deduction is claimed, using the regular-and-exclusive-use or inventory-storage test from the line 30 text.

### (screen) (sc.ho_other) — Does any of these apply to your business use of your home for this business?
Status: **MATCH**

Model: This screens out the actual-expense method, multiple homes, daycare, shared use, part-year use, other places of business, Form 8949 or 4797 gains, and late or amended returns. Each of these changes the simplified method in the instructions, and the refusal names them.

### 30(b) — The part of your home used for business (square feet)
Status: **MATCH**

Model: This is the square feet used regularly and exclusively for the business. Multiple businesses (the 300 square feet must be allocated) and the special cases are refused.

### 30(a) — Total square footage of your home
Status: **MATCH**

Model: This is the total square footage of the home, as the line 30 entry space asks.

### 3a — Maximum allowable amount (per square foot)
Status: **MATCH**

Model: The worksheet line 3a prints $5.

### 4 (sc.ho_line4) — Multiply line 2 by line 3c
Status: **MATCH**

Model: It is the smaller of the square feet used or 300, times $5. Line 3b is 1.0 because daycare is screened, so line 3c equals line 3a.

### 1 (sc.ho_line1) — Gross income limitation (Schedule C, line 29)
Status: **MATCH**

Model: The gross income limitation is line 29 plus home-related gains minus other losses. With those gains, losses and other places of business screened, it equals line 29.

### 5 (sc.ho_line5) — Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4
Status: **MATCH**

Model: The worksheet says 'Enter the smaller of line 1 or line 4… If zero or less, enter -0-.' The program takes line 4 when it cannot exceed line 29 under any section 179 allocation, and otherwise takes min(line 4, line 29 floored at zero) when there is no section 179. The case where both income limits apply is refused, citing Pub. 946.

### 30 — Expenses for business use of your home
Status: **MATCH**

Model: This matches 'Include the amount from line 5 of the Simplified Method Worksheet on line 30', with zero if there is no home office.

### 31 — Net profit or (loss). Subtract line 30 from line 29
Status: **MATCH**

Model: This matches 'Subtract line 30 from line 29.' The passive loss and at-risk limits are screened or refused.

### 32 — If you have a loss, is all your investment in this business at risk (box 32a)?
Status: **MATCH**

Model: The three not-at-risk examples follow the box 32b text: nonrecourse loans, protected amounts excluding casualty and tort insurance, and amounts borrowed from interested or related persons.

### 33 — Method used to value closing inventory: other than cost or lower of cost or market, or a c
Status: **MATCH**

Model: It screens other valuation methods (line 33c) and changes asked about on line 34. These are refused.

### 35 — Inventory at beginning of year
Status: **MATCH**

Model: This is inventory at the beginning of the year, equal to last year's closing inventory. Method changes are refused.

### 36 — Purchases less cost of items withdrawn for personal use
Status: **MATCH**

Model: This matches 'Purchases less cost of items withdrawn for personal use.'

### 37 — Cost of labor
Status: **MATCH**

Model: This matches 'Cost of labor. Do not include any amounts paid to yourself.'

### 38 — Materials and supplies
Status: **MATCH**

Model: This is materials and supplies, as printed.

### 39 — Other costs
Status: **MATCH**

Model: This is other costs, as printed.

### 40 — Add lines 35 through 39
Status: **MATCH**

Model: This matches 'Add lines 35 through 39.'

### 41 — Inventory at end of year
Status: **MATCH**

Model: This is inventory at end of year, as printed.

### 42 — Cost of goods sold. Subtract line 41 from line 40
Status: **MATCH**

Model: This matches 'Subtract line 41 from line 40.'

### 12 (sc.s179_allowed) — Section 179 expense deduction for this business
Status: **MATCH**

Model: If Form 4562 line 12 equals the elected cost (line 8), each business keeps its own elections, which is an allocation the line 12 instructions permit. Otherwise the return's line 12 goes to the only Schedule C, and allocation among several businesses is refused.

### (screen) (sc.hi_uses) — Health insurance established under this business
Status: **MATCH**

Model: The plan must be established under the business, the policy may be in your name or the business's, and personal services must be a material income-producing factor, as the line 17 text and Form 7206 instructions say.

### (screen) (sc.hi_screen) — Does any of these apply to this health insurance?
Status: **MATCH**

Model: This screens out the Marketplace premium tax credit (Pub. 974), Form 2555, S corporations, optional methods, retired public safety officers and long-term care across several businesses. These are the cases the instructions route elsewhere or limit.

### 1 (sc.f7206_line1) — Health insurance payments (other than long-term care)
Status: **MATCH**

Model: It follows Form 7206 line 1: coverage for you, your spouse, dependents and a child under 27, voluntary Medicare premiums, no months eligible for a subsidized employer plan (a QSEHRA counts as one), and no long-term care. The public safety officer case is refused.

### 2 (sc.f7206_line2) — Qualified long-term care insurance (the smaller of payments or the age limit, for each per
Status: **MATCH**

Model: It is the sum over covered persons of the smaller of (a) payments or (b) the age-based amount, as on line 2.

### 3 (sc.f7206_line3) — Add lines 1 and 2
Status: **MATCH**

Model: This matches 'Add lines 1 and 2.'

### 4 (sc.f7206_line4) — Net profit from the trade or business under which the insurance plan is established
Status: **MATCH**

Model: This is the net profit of the business under which the plan is established. Optional methods are screened, and a loss gives no deduction.

### 5 (sc.f7206_line5) — Total of all net profits from Schedule C, line 31
Status: **MATCH**

Model: This is the total of all net profits excluding net losses, as line 5 says. Schedule F and K-1 income are screened.

### 7 (sc.f7206_line7) — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax, by the p
Status: **MATCH**

Model: It is the deductible part of self-employment tax times line 4 divided by line 5, which is lines 6 and 7 combined, using this person's Schedule SE.

### 8 (sc.f7206_line8) — Subtract line 7 from line 4
Status: **MATCH**

Model: This matches 'Subtract line 7 from line 4.'

### 9 (sc.f7206_line9) — Schedule 1, line 16, attributable to the same trade or business
Status: **MATCH**

Model: This is the Schedule 1 line 16 amount attributable to this business. A plan covering more than one Schedule C is screened, so the whole amount goes to the single business.

### 10 (sc.f7206_line10) — Subtract line 9 from line 8
Status: **MATCH**

Model: This matches 'Subtract line 9 from line 8.'

### 13 (sc.f7206_line13) — Subtract line 12 from line 10
Status: **MATCH**

Model: Line 13 subtracts line 12 from line 10. The Form 2555 and S corporation cases (lines 11 and 12) are screened, so line 13 equals line 10.

### 14 (sc.f7206_line14) — Self-employed health insurance deduction
Status: **MATCH**

Model: This matches 'Enter the smaller of line 3 or line 13.'

### 1(c) — Qualified business income or (loss) of this business
Status: **MATCH**

Model: It is net profit or loss reduced by the deductible part of self-employment tax, retirement plan contributions and the self-employed health insurance deduction attributable to the business, as the Form 8995 instructions require for QBI.

### (screen) (sc.tips_ot) — Tips or overtime in this business to be deducted on Schedule 1-A
Status: **MATCH**

Model: This screens out qualified tips and overtime from this business, which are claimed on Schedule 1-A and limited by the business's net income per the Form 1040 instructions.

## Raw response

```yaml
```yaml
lines:
  - key: "(screen) (sc.statutory)"
    status: MATCH
    reason: "This screens out statutory employee income (W-2 box 13 checked) and notary fees. The Schedule C instructions treat both specially, and the sc.screened refusal names them."
  - key: "G"
    status: MATCH
    reason: "It follows the line G instruction: not a rental activity and one of the material participation tests is met, or the oil and gas working interest exception applies. The tests it summarizes (500 hours, substantially all, 100 hours and at least as much as anyone) match the seven-test list."
  - key: "(screen) (sc.spouse_owned)"
    status: MATCH
    reason: "This screens out spouse-owned businesses (qualified joint venture, community property or partnership). The instructions give these special treatment, and the refusal names them."
  - key: "F"
    status: MATCH
    reason: "This is a screen for other accounting methods, method changes (Form 3115, section 481(a)), UNICAP for businesses over the $31 million gross receipts test, tax shelters under section 448(d)(3) and section 460 long-term contracts. All of these appear in the line F and Part III text, and the refusal excludes them."
  - key: "(screen) (sc.special)"
    status: MATCH
    reason: "Each listed item is a special case named in the instructions: depletion, Form 7205, credit reductions, Form 8990, recapture, chapter 11, Form 8873, installment method, Notice 2014-7, CCF, and so on. The refusal excludes all of them."
  - key: "1 (sc.line1)"
    status: MATCH
    reason: "Gross receipts include amounts properly shown on Forms 1099-NEC and sales tax imposed on the seller that was collected from buyers ('you must also include the amount collected in gross receipts'). NIL income that is not self-employment income goes on Schedule E. The screened cases are refused."
  - key: "2 (sc.line2)"
    status: MATCH
    reason: "This matches 'Report your sales returns and allowances as a positive number on line 2.'"
  - key: "3 (sc.line3)"
    status: MATCH
    reason: "This matches 'Subtract line 2 from line 1.'"
  - key: "4 (sc.line4)"
    status: MATCH
    reason: "This matches 'Cost of goods sold (from line 42).'"
  - key: "5 (sc.line5)"
    status: MATCH
    reason: "This matches 'Gross profit. Subtract line 4 from line 3.'"
  - key: "6"
    status: MATCH
    reason: "The items listed come from the line 6 list, including fuel tax refunds, the fuel tax credit, prizes and 1099-PATR amounts. Retained sales tax comes from the line 23 instructions. The list is open-ended ('such as'), and the recapture and 481(a) items are screened."
  - key: "7 (sc.line7)"
    status: MATCH
    reason: "This matches 'Gross income. Add lines 5 and 6.'"
  - key: "8 (sc.line8)"
    status: MATCH
    reason: "This is advertising expense, as printed."
  - key: "9 (sc.line9)"
    status: MATCH
    reason: "Under the standard mileage rate it is business miles times $0.70 plus parking fees and tolls. Under actual expenses it is the business portion of operating expenses. Both follow the line 9 instructions, and the cases where the standard rate is unavailable are refused."
  - key: "10 (sc.line10)"
    status: MATCH
    reason: "This matches 'Do not include commissions or fees that are capitalized or deducted elsewhere.'"
  - key: "11"
    status: MATCH
    reason: "Contract labor excludes amounts includible on lines 17, 21, 26 or 37, as the instructions state."
  - key: "12 (sc.line12)"
    status: MATCH
    reason: "Depletion is zero because depletion is screened out in sc.special and refused."
  - key: "13 (sc.line13)"
    status: MATCH
    reason: "It adds Form 4562 lines 14, 17, 19 and the listed-property line 28 to this business's section 179 deduction, which mirrors the line 22 total. The lines 15, 16 and 20 cases (other methods, ADS) are screened."
  - key: "14 (sc.line14)"
    status: MATCH
    reason: "It covers employee benefit programs other than pension plans (line 19) and excludes contributions for yourself, as the line 14 text says. The Form 8941 and Form 2441 cases are screened."
  - key: "15"
    status: MATCH
    reason: "It excludes reserves for self-insurance and lost-earnings policies, as line 15 says. Employee health insurance belongs on line 14."
  - key: "16a"
    status: MATCH
    reason: "This is mortgage interest paid to financial institutions and reported on Form 1098, excluding capitalized interest, as the line 16a instructions describe."
  - key: "16b"
    status: MATCH
    reason: "It covers other interest, including mortgage interest without a Form 1098 to you, your share when another person received the Form 1098, only the part that applies to 2025, and no interest claimed on Schedule 1-A. All of this follows the instructions."
  - key: "17"
    status: MATCH
    reason: "This is accountant and attorney fees directly related to operating the business, including tax advice and tax preparation. The list is inclusive."
  - key: "18"
    status: MATCH
    reason: "This matches 'expenses for office supplies and postage.'"
  - key: "19"
    status: MATCH
    reason: "These are contributions for employees, with contributions for yourself going on Schedule 1, line 16, as the line 19 text says."
  - key: "20a"
    status: MATCH
    reason: "It is the business portion of rent for vehicles, machinery and equipment, with lease payments allowed only under actual expenses. The inclusion amount for 30-day-or-longer leases is screened."
  - key: "20b"
    status: MATCH
    reason: "This matches 'amounts paid to rent or lease other property, such as office space.'"
  - key: "21"
    status: MATCH
    reason: "This follows the line 21 text: incidental repairs only, not your own labor, and not restorations."
  - key: "22"
    status: MATCH
    reason: "It covers materials consumed and used, or incidental supplies purchased if no records are kept, plus items normally used within a year, as the line 22 text says."
  - key: "23"
    status: MATCH
    reason: "The deductible taxes and the exclusions follow the line 23 lists. The Form 8846 reduction and amortized licenses are screened."
  - key: "24a"
    status: MATCH
    reason: "It follows the line 24a text: lodging and transportation, incidentals at actual cost or $5 a day only on days with no meals, the 1-year limit, the rule for spouses and dependents, and the North American area convention rule. Luxury water travel is screened."
  - key: "24b"
    status: MATCH
    reason: "It applies 50% generally, 80% for meals under the DOT hours of service limits, and 100% for the fully deductible exceptions, as in 'Amount of deduction.'"
  - key: "25"
    status: MATCH
    reason: "These are business utilities only, excluding the base rate of the first home phone line."
  - key: "26"
    status: MATCH
    reason: "Wages exclude amounts paid to yourself, wages deducted elsewhere, and depreciation in fringe benefits. The employment credit reductions are screened."
  - key: "27a"
    status: MATCH
    reason: "It is zero because the Form 7205 deduction is screened and refused."
  - key: "48"
    status: MATCH
    reason: "This matches Part V: 'business expenses not included on lines 8-27a, or line 30.'"
  - key: "27b"
    status: MATCH
    reason: "This matches 'Other expenses (from line 48).'"
  - key: "28"
    status: MATCH
    reason: "This matches 'Add lines 8 through 27b.'"
  - key: "29"
    status: MATCH
    reason: "This matches 'Subtract line 28 from line 7.'"
  - key: "(screen) (sc.ho_uses)"
    status: MATCH
    reason: "It asks whether a home office deduction is claimed, using the regular-and-exclusive-use or inventory-storage test from the line 30 text."
  - key: "(screen) (sc.ho_other)"
    status: MATCH
    reason: "This screens out the actual-expense method, multiple homes, daycare, shared use, part-year use, other places of business, Form 8949 or 4797 gains, and late or amended returns. Each of these changes the simplified method in the instructions, and the refusal names them."
  - key: "30(b)"
    status: MATCH
    reason: "This is the square feet used regularly and exclusively for the business. Multiple businesses (the 300 square feet must be allocated) and the special cases are refused."
  - key: "30(a)"
    status: MATCH
    reason: "This is the total square footage of the home, as the line 30 entry space asks."
  - key: "3a"
    status: MATCH
    reason: "The worksheet line 3a prints $5."
  - key: "4 (sc.ho_line4)"
    status: MATCH
    reason: "It is the smaller of the square feet used or 300, times $5. Line 3b is 1.0 because daycare is screened, so line 3c equals line 3a."
  - key: "1 (sc.ho_line1)"
    status: MATCH
    reason: "The gross income limitation is line 29 plus home-related gains minus other losses. With those gains, losses and other places of business screened, it equals line 29."
  - key: "5 (sc.ho_line5)"
    status: MATCH
    reason: "The worksheet says 'Enter the smaller of line 1 or line 4… If zero or less, enter -0-.' The program takes line 4 when it cannot exceed line 29 under any section 179 allocation, and otherwise takes min(line 4, line 29 floored at zero) when there is no section 179. The case where both income limits apply is refused, citing Pub. 946."
  - key: "30"
    status: MATCH
    reason: "This matches 'Include the amount from line 5 of the Simplified Method Worksheet on line 30', with zero if there is no home office."
  - key: "31"
    status: MATCH
    reason: "This matches 'Subtract line 30 from line 29.' The passive loss and at-risk limits are screened or refused."
  - key: "32"
    status: MATCH
    reason: "The three not-at-risk examples follow the box 32b text: nonrecourse loans, protected amounts excluding casualty and tort insurance, and amounts borrowed from interested or related persons."
  - key: "33"
    status: MATCH
    reason: "It screens other valuation methods (line 33c) and changes asked about on line 34. These are refused."
  - key: "35"
    status: MATCH
    reason: "This is inventory at the beginning of the year, equal to last year's closing inventory. Method changes are refused."
  - key: "36"
    status: MATCH
    reason: "This matches 'Purchases less cost of items withdrawn for personal use.'"
  - key: "37"
    status: MATCH
    reason: "This matches 'Cost of labor. Do not include any amounts paid to yourself.'"
  - key: "38"
    status: MATCH
    reason: "This is materials and supplies, as printed."
  - key: "39"
    status: MATCH
    reason: "This is other costs, as printed."
  - key: "40"
    status: MATCH
    reason: "This matches 'Add lines 35 through 39.'"
  - key: "41"
    status: MATCH
    reason: "This is inventory at end of year, as printed."
  - key: "42"
    status: MATCH
    reason: "This matches 'Subtract line 41 from line 40.'"
  - key: "12 (sc.s179_allowed)"
    status: MATCH
    reason: "If Form 4562 line 12 equals the elected cost (line 8), each business keeps its own elections, which is an allocation the line 12 instructions permit. Otherwise the return's line 12 goes to the only Schedule C, and allocation among several businesses is refused."
  - key: "(screen) (sc.hi_uses)"
    status: MATCH
    reason: "The plan must be established under the business, the policy may be in your name or the business's, and personal services must be a material income-producing factor, as the line 17 text and Form 7206 instructions say."
  - key: "(screen) (sc.hi_screen)"
    status: MATCH
    reason: "This screens out the Marketplace premium tax credit (Pub. 974), Form 2555, S corporations, optional methods, retired public safety officers and long-term care across several businesses. These are the cases the instructions route elsewhere or limit."
  - key: "1 (sc.f7206_line1)"
    status: MATCH
    reason: "It follows Form 7206 line 1: coverage for you, your spouse, dependents and a child under 27, voluntary Medicare premiums, no months eligible for a subsidized employer plan (a QSEHRA counts as one), and no long-term care. The public safety officer case is refused."
  - key: "2 (sc.f7206_line2)"
    status: MATCH
    reason: "It is the sum over covered persons of the smaller of (a) payments or (b) the age-based amount, as on line 2."
  - key: "3 (sc.f7206_line3)"
    status: MATCH
    reason: "This matches 'Add lines 1 and 2.'"
  - key: "4 (sc.f7206_line4)"
    status: MATCH
    reason: "This is the net profit of the business under which the plan is established. Optional methods are screened, and a loss gives no deduction."
  - key: "5 (sc.f7206_line5)"
    status: MATCH
    reason: "This is the total of all net profits excluding net losses, as line 5 says. Schedule F and K-1 income are screened."
  - key: "7 (sc.f7206_line7)"
    status: MATCH
    reason: "It is the deductible part of self-employment tax times line 4 divided by line 5, which is lines 6 and 7 combined, using this person's Schedule SE."
  - key: "8 (sc.f7206_line8)"
    status: MATCH
    reason: "This matches 'Subtract line 7 from line 4.'"
  - key: "9 (sc.f7206_line9)"
    status: MATCH
    reason: "This is the Schedule 1 line 16 amount attributable to this business. A plan covering more than one Schedule C is screened, so the whole amount goes to the single business."
  - key: "10 (sc.f7206_line10)"
    status: MATCH
    reason: "This matches 'Subtract line 9 from line 8.'"
  - key: "13 (sc.f7206_line13)"
    status: MATCH
    reason: "Line 13 subtracts line 12 from line 10. The Form 2555 and S corporation cases (lines 11 and 12) are screened, so line 13 equals line 10."
  - key: "14 (sc.f7206_line14)"
    status: MATCH
    reason: "This matches 'Enter the smaller of line 3 or line 13.'"
  - key: "1(c)"
    status: MATCH
    reason: "It is net profit or loss reduced by the deductible part of self-employment tax, retirement plan contributions and the self-employed health insurance deduction attributable to the business, as the Form 8995 instructions require for QBI."
  - key: "(screen) (sc.tips_ot)"
    status: MATCH
    reason: "This screens out qualified tips and overtime from this business, which are claimed on Schedule 1-A and limited by the business's net income per the Form 1040 instructions."
```
```
