# Render comparison — sc

The rendered English of every printed line of `Schedule C (Form 1040) — Profit or Loss From Business, one per business` (`rendered/2025/sc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
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

### (screen) (sc.special) — For this business, do you have any of these?
Status: **MATCH**

Model: The screen is a yes/no input that steers out special items the instructions name, such as depletion, Form 7205, employment credits, Form 8990, recapture, chapter 11, Form 8873, installment sales, Notice 2014-7, capital construction fund, dependent care, PAL, luxury water travel and single-member LLCs taxed as corporations. Each is routed to sc.screened and the line 1 refusal.
Reviewed in: pass 5ea93676fec3

### 1 (sc.line1) — Gross receipts or sales
Status: **MATCH**

Model: The text says to enter gross receipts, include amounts 'properly shown on your Forms 1099-NEC' and business income from any Forms 1099, include collected seller sales tax ('you must also include the amount collected in gross receipts or sales on line 1'), and report non-self-employment NIL on Schedule E. Prizes and awards go on line 6. Statutory employee and other excluded cases are covered by the refusal.
Reviewed in: pass 5ea93676fec3

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

Model: This tracks the line 24a instructions: overnight lodging and transportation away from your tax home, and no employment away from home over 1 year. It also tracks the rules on other persons' travel, the $5-a-day incidental option only on days with no meal expenses and no standard meal allowance, the listed incidental items and exclusions, and the North American area convention rule. Luxury water travel is screened out.
Reviewed in: pass 5ea93676fec3

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

Model: The form says 'Add lines 8 through 27b', and the restatement lists every line from 8 through 27b, including 13, 16a/16b, 20a/20b, 24a/24b and 27a/27b.
Reviewed in: pass 5ea93676fec3

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

Model: The worksheet says 'Enter the smaller of line 1 or line 4... If zero or less, enter -0-.' When line 4 is at or below line 29 less the largest possible section 179 deduction, line 4 is necessarily the smaller amount. With no section 179 possible, the smaller of line 4 or the floored line 29 is used. The circular case with two income-based limits is refused, as Pub. 946 describes it.
Reviewed in: pass 5ea93676fec3

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

Model: Form 4562 line 12 limits apply to the taxpayer, and the deduction 'may allocate... among them'. When the deduction equals the elections, each business takes its own elected cost, which is a permitted allocation. When it differs, the return's line 12 is used only for a sole Schedule C, and allocation among several businesses is refused.
Reviewed in: pass 5ea93676fec3

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

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| (screen) (sc.statutory) | d2f688ee3fcd674f963ab54362478a207a821a94dbfefcc681cbe090a7e701ce |
| G | 9336293c87a3010625acd5ec878f0a51d8d1235bfa2fce813a1742c7fecd6965 |
| (screen) (sc.spouse_owned) | 50e12d17c0ac2c9df9a2a093f8ecbf7b395ecf60a6ae926d89771d9bbbdd97ee |
| F | 64a4b664c7e9c5e00f93761d29f2348d5763768424d47ddb0889ba3785b68039 |
| (screen) (sc.special) | b6054cf6d08de1448607610ff7324be5e50a13132e292f5f5a5fc5dce25a1c89 |
| 1 (sc.line1) | 9fae6f700a00928210f705396ff73c77d764798966bedf9605838efe8f67b144 |
| 2 (sc.line2) | a740eed3e32368c0a0975232c06d42726848f95d06bb1bddc037583ac496e10b |
| 3 (sc.line3) | 32dfb404a18c1f8633e0318597f3f2d8b2053aa400441bccc2b375867c25a6d3 |
| 4 (sc.line4) | 7b85ae1e7bcd8268c76f2f79ad655b96c785b5c0fdd697ebc6f61267b02caa44 |
| 5 (sc.line5) | 47740fe30007eb21334133749240887288f65f6e778209a425ecd20a93f45048 |
| 6 | 1f493718ee3436e80c160291430e5d61df692217454968863ed4adb17c6dad73 |
| 7 (sc.line7) | aaaa2c5c17ffeca5bdda093346fce4ab45952c057bf2ab939301a3e7ad379254 |
| 8 (sc.line8) | d902ac0c28f9c6eac684b610b8143faf793e4e163cda80f03ca2eaca5035c3bf |
| 9 (sc.line9) | 9aefea8c8c0a9be5851271590bfbcab3691e3eb71297df7a8d82235f9baf50cf |
| 10 (sc.line10) | 596b8a3ccc22de340a5b754b6fd63d9263530ce36c7c37aca16cc8ae555de789 |
| 11 | c860f599f3f0b7c2101bfb57cddda3031e0917a5b9d2d3ec935b643942b45930 |
| 12 (sc.line12) | a39929fe1712d2f6d15a1f390a4fc55229124d31030280ae077282980e7dc67c |
| 13 (sc.line13) | e19962e88f0a52f9ecbad7c1a8904d178038ca6bd871bee2ad0c34c76c5a002a |
| 14 (sc.line14) | 7aa0f97754f1d5cdd4f062aa15d5b277af14a0a1cc2e10a94c619a55b3f2fdef |
| 15 | 68445504d79347896522b2b40b5774ea7aabd2b07366884369ebbea6f60d2f9a |
| 16a | 655f63ef4b8c69b66fd0543bf5f126822a11e6a73aefe93c6061236f9362c766 |
| 16b | 932de183ab38295ccc43a9e59f73ae78ab3decf693620fdeca293f5d43f465e9 |
| 17 | 42aa865dbe72d2693ea13a5dceb35a31ca25350fc58cdc2f5901f02a2877d157 |
| 18 | acd5391daa65da1b6e5bb3dda39a15cb428dc31d4ad96d02f6823af5f7453003 |
| 19 | 337923fa22d7496de27efabfdb27b7f8d97a9c68000d4722ded9eacfaa917db5 |
| 20a | 8e4e6556211dd7aed7078cdd15c2ae1202af3b925d4c771c7f8370fd8c9c6083 |
| 20b | 7d5b7ebbdaf7e6563b90dde494a063bdf591e0841121dd6f6b6de1ac0d10771a |
| 21 | 0c641002fd40d82e0b86031578e5cb6fe7150bc98088af93b3e79403e8b4c63c |
| 22 | be932e2a45ec9b9ad7bc7afe6900e0e71f5f82c93ba3dc23e5b498300853251d |
| 23 | 6bd230c2a980411ead0ef77e480a5ab35e21811e887dd12ded3b2b403a23be25 |
| 24a | 827a15912a1ed16a491da4a23f662a63a6a05cf73ae72846314ba376b2844602 |
| 24b | 70b55924d05eb90ead1028c95268bdd9225d2ed1721a9d7abdd224f42158fa0e |
| 25 | a09c6adc64416a35c8a026a4cae38890eb5ccfac787c63a568a96244dbac5164 |
| 26 | a3d438611bbce53f4df601f6e0e2877deac87ec458f3a1c1d49f944563b3a409 |
| 27a | 4543d2ec340b33f1758027df6f9f7e5bc36c55d528e9d8123d43625074a84236 |
| 48 | 2407fa82672e5b3a4962333281572936acbc2ad935216f4cf18202717201cda6 |
| 27b | 6ae07cb4f45d196fb8d96b5f216a6b7ee44a2ca355fbdb1e3b6c2e12f395b42d |
| 28 | 790f6b84fb0f37413b47a58268e5590a45e8bd8b5ce6d83e716eb373b699fe9a |
| 29 | 5e252890f40ebaf167e76d93a87be5b2a3c16bad2464fb510c868ba8b9b3d2b4 |
| (screen) (sc.ho_uses) | ef5c3e8372d70c514df195b4e4fa6991b5208e5280292707d1fc1b3e8a0c05bd |
| (screen) (sc.ho_other) | f4b5d7242f56552080b3617765afc533d194fdc9ec282dc5eb90d8a356eeb249 |
| 30(b) | 8be6705f90cf2410bb97c9f40f3bcaba508b2b02aed286f6d9d25eb8b69a7a07 |
| 30(a) | 13030153eb4fc7138847565a2dd0f31b86210da3fddf1871bf13337c2d2fc447 |
| 3a | f032c1aa616e675b295a4be9748270b4c92a3dca1786e32bc1cd1ed510b6c140 |
| 4 (sc.ho_line4) | c16a11b8934124f13c7226b8945dc16407c6b35e3e0612405a2ad90352ed45cd |
| 1 (sc.ho_line1) | 93604a87acc0da5e391576b70009e23bb7c8d01a2bc4e755bdb9b477e0d452c3 |
| 5 (sc.ho_line5) | 00567f522593e16241e3183efa7321da5b217d4bde8bc477a53e7e734bfc1341 |
| 30 | 2b2454406fde06a52b62715df8f45ee04691af33384cb10429efa6adda93e364 |
| 31 | 1422a43a9afabd8d0b571ce73dc64eb53b2e044a0ae273a7ae4fa0bcf181f6ac |
| 32 | b25d38d7fe4a3729fd765e7af7fd4e8de7a41893f83623de88158cddf985c07b |
| 33 | 50711830f2371d36d966b1736e7b670c93dfd77ae213accbd336eb605498fd3a |
| 35 | de04f0367e91980c5c24c0536a271c0782e32bd6f9ce4cb52653404c5f14911e |
| 36 | b389efa972b467de26b52ac3de52917a94d1ac63227c13c40b3b5c02e259f423 |
| 37 | bf3bbee7cfdb8ecb5d89fe9d0ec0aa16800102f3e43e327b6199cb2da08eed37 |
| 38 | 1f1d505299d54c4175324e87abdf408fb00d21fe7f81fd80003a38fe2476dac8 |
| 39 | 0ef5ce9ed8cf850cc78f66035dabffd60b00d761f00d7d724550f210c37b5a71 |
| 40 | 033bea5099029a14cbec4b858fe135c0c759ace2d8cfbfc7e65d1d15c432984f |
| 41 | ac91ba25000990d92da68710d46ca204aaa6e9d40a7cc2d3bcb6ac1ccb2c4d95 |
| 42 | 278262894b269d7757fb3a8c270656a79d5e44a2dca3b867e8628a5d9490f2e9 |
| 12 (sc.s179_allowed) | faa8ca3276f114ebcbd751574613fbf2f5d8b7cbf3a87fe2e5a89f44855bc83b |
| (screen) (sc.hi_uses) | d780af140ed61b7636e582896ef38a06a901001438731a5df5133ab2e56bb73a |
| (screen) (sc.hi_screen) | a2dec570d2e040adde80c037b79193fe9da036b710becfa33502a71209a7c117 |
| 1 (sc.f7206_line1) | ca22ab0386d35458dca2d715df8e9f925b61ddfda12d1e3708023992f07ff124 |
| 2 (sc.f7206_line2) | 4a8f3bc38b51a3f22cb9c88722a242193ce322c350c38175024a52896c2c7433 |
| 3 (sc.f7206_line3) | ce1706c34d2dd588f8bee4a51e6124f12cc7e138897b6ac75c224aac3a434adb |
| 4 (sc.f7206_line4) | 7185c97a5e68441ae339f83b1976c871b54aeeb3bb98a6229b6488ded57bf79e |
| 5 (sc.f7206_line5) | 1e4d8104b52947e1b606366f9dbbf92ea57041036e8c26f0893f9a9a1b210069 |
| 7 (sc.f7206_line7) | bef18a7fbf8a0cac2e552e60da39d58068257d1449770b432afae5ed4398b24a |
| 8 (sc.f7206_line8) | a25c1b9cfc5a2fb7c531e3ccd16f759b968a4fd1767e2fb9f5ea58c859e6d814 |
| 9 (sc.f7206_line9) | 55682ff4ca61a3c39016a7cda38325fe21a61d302b1b24366bbbe8ee97fab3e4 |
| 10 (sc.f7206_line10) | 4a6fc23293b452a587c8c681fed56f7847ca1a8659fe9eca1087cc54255ba119 |
| 13 (sc.f7206_line13) | 99c5774896376db77445b76f8b1b95eb36cbf116da9176acaca129b728f56de6 |
| 14 (sc.f7206_line14) | 0d0fbf293b1249e6e33b3d7cd621a712654c312e3eb03ec95bddbf2d6a777459 |
| 1(c) | 37936dcc3e8495d753da824fee76a6d1afc169abaaa8f34982a815eb98305bfe |
| (screen) (sc.tips_ot) | fdb948c18792a3f705d0fc12465389f045c5185076bb24a588958840d81e5685 |
| (rest of the document) | ed53d3203d917abafab1d2fe4da410ba4fc100b32f1ed5882f9e7962dd130f66 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 5ea93676fec3

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines (screen) (sc.special), 1 (sc.line1), 24a, 28, 5 (sc.ho_line5), 12 (sc.s179_allowed) |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 5ea93676fec3ab6039f3da6b0874a337a7130246de595ada0fe2a254c1a7518d |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | c0f4544f7ddaef89d4d8b37cf7b8f05b682f49c103848bfb0a584a9282a43960 |
| receipt | .transcription/sc.render.lines-834a550d92b5 |
| lines judged | 6 |
| match / mismatch / unclear / missing | 6 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 31, 32, 33, 34, 37, 39, 41, 59, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 31, 32, 33, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p538 | None | 17 | pages named by another document's citation | 4186d7aaa8f711c9a524b87fac1e3df05640b6d66130093b2469480acb06ef6c | 17 | f500211df18a4aafd843e48bbad4b9102c598cf5ccc0fae96c7814a4bef0ae00 |
| p463 | For use in preparing 2025 returns | 12, 26 | pages named by another document's citation | 153efad2a94bcccadf643b0f28f913d74b7d70b727f73eca540a2ce4d32bbfda | 12, 26 | a0b14576fdb49a7ba3e7a90092c1b8f6b8ba33889c8c35da5629156346581326 |
| i8995 | 2025; printed date 2026-01-26 | 2 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 2 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |

##### Raw response

```yaml
lines:
  - key: "(screen) (sc.special)"
    status: MATCH
    reason: "The screen is a yes/no input that steers out special items the instructions name, such as depletion, Form 7205, employment credits, Form 8990, recapture, chapter 11, Form 8873, installment sales, Notice 2014-7, capital construction fund, dependent care, PAL, luxury water travel and single-member LLCs taxed as corporations. Each is routed to sc.screened and the line 1 refusal."
  - key: "1 (sc.line1)"
    status: MATCH
    reason: "The text says to enter gross receipts, include amounts 'properly shown on your Forms 1099-NEC' and business income from any Forms 1099, include collected seller sales tax ('you must also include the amount collected in gross receipts or sales on line 1'), and report non-self-employment NIL on Schedule E. Prizes and awards go on line 6. Statutory employee and other excluded cases are covered by the refusal."
  - key: "24a"
    status: MATCH
    reason: "This tracks the line 24a instructions: overnight lodging and transportation away from your tax home, and no employment away from home over 1 year. It also tracks the rules on other persons' travel, the $5-a-day incidental option only on days with no meal expenses and no standard meal allowance, the listed incidental items and exclusions, and the North American area convention rule. Luxury water travel is screened out."
  - key: "28"
    status: MATCH
    reason: "The form says 'Add lines 8 through 27b', and the restatement lists every line from 8 through 27b, including 13, 16a/16b, 20a/20b, 24a/24b and 27a/27b."
  - key: "5 (sc.ho_line5)"
    status: MATCH
    reason: "The worksheet says 'Enter the smaller of line 1 or line 4... If zero or less, enter -0-.' When line 4 is at or below line 29 less the largest possible section 179 deduction, line 4 is necessarily the smaller amount. With no section 179 possible, the smaller of line 4 or the floored line 29 is used. The circular case with two income-based limits is refused, as Pub. 946 describes it."
  - key: "12 (sc.s179_allowed)"
    status: MATCH
    reason: "Form 4562 line 12 limits apply to the taxpayer, and the deduction 'may allocate... among them'. When the deduction equals the elections, each business takes its own elected cost, which is a permitted allocation. When it differs, the return's line 12 is used only for a sole Schedule C, and allocation among several businesses is refused."
```

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
