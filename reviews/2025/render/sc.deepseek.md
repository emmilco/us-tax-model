# Render comparison — sc

The rendered English of every printed line of `Schedule C (Form 1040) — Profit or Loss From Business, one per business` (`rendered/2025/sc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | ee875dadc6308766f4d3efe9bf4985526192ef445453bffd14f40e8172f02df5 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 20943341f7390ac694fdb843c313730d5f7ff04a35f9de4ed0fe9ae173076d0b |
| lines judged | 75 |
| match / mismatch / unclear / missing | 71 / 4 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 34, 37, 39, 41, 59, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
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

Model: Matches the statutory employee screen from the Schedule C line 1 and line 31 instructions; notary cases are named as excluded.

### G — Did you "materially participate" in the operation of this business during 2025, and is the
Status: **MATCH**

Model: Matches the line G material participation tests, oil and gas exception, and non-rental activity condition.

### (screen) (sc.spouse_owned) — Do you own this business together with your spouse (as a qualified joint venture, as commu
Status: **MATCH**

Model: Matches the spouse-owned/QJV/community property exclusion described in the Schedule C instructions.

### F — Do you use an accounting method other than cash or accrual, or did you change your account
Status: **MATCH**

Model: Matches the accounting method, Form 3115/section 481(a), small business capitalization, tax shelter, and long-term contract points in the line F instructions.

### (screen) (sc.special) — For this business, do you have any of these: depletion (line 12); the energy efficient com
Status: **MATCH**

Model: The screen enumerates the special items described in the instructions and the program refuses cases it excludes.

### 1 (sc.line1) — Gross receipts or sales
Status: **MATCH**

Model: Matches the line 1 gross receipts rule, including Forms 1099-NEC/1099-K and the NIL and Schedule E exception; the screen refusal names excluded cases.

### 2 (sc.line2) — Returns and allowances
Status: **MATCH**

Model: Matches the line 2 rule to report returns and allowances as a positive number.

### 3 (sc.line3) — Subtract line 2 from line 1
Status: **MATCH**

Model: Matches the line 3 subtraction of line 2 from line 1.

### 4 (sc.line4) — Cost of goods sold (from line 42)
Status: **MATCH**

Model: Matches the line 4 instruction to enter the amount from line 42.

### 5 (sc.line5) — Gross profit. Subtract line 4 from line 3
Status: **MATCH**

Model: Matches the line 5 subtraction of line 4 from line 3.

### 6 — Other income, including federal and state gasoline or fuel tax credit or refund
Status: **MATCH**

Model: Matches the line 6 other business income examples and the retained sales tax rule.

### 7 (sc.line7) — Gross income. Add lines 5 and 6
Status: **MATCH**

Model: Matches the line 7 addition of lines 5 and 6.

### 8 (sc.line8) — Advertising
Status: **MATCH**

Model: Matches the line 8 advertising expense input.

### 9 (sc.line9) — Car and truck expenses
Status: **MATCH**

Model: Matches the line 9 car and truck expense aggregation from the vehicle entries.

### 10 (sc.line10) — Commissions and fees
Status: **MATCH**

Model: Matches the line 10 commissions and fees rule, excluding capitalized or elsewhere-deducted amounts.

### 11 — Contract labor
Status: **MATCH**

Model: Matches the line 11 contract labor rule and the lines 17, 21, 26 and 37 exclusions.

### 12 (sc.line12) — Depletion
Status: **MATCH**

Model: Depletion is excluded by the sc.special screen, so within supported cases line 12 is zero; the refusal names depletion.

### 13 (sc.line13) — Depreciation and section 179 expense deduction (not included in Part III)
Status: **MATCH**

Model: The line adds non-section-179 depreciation and the allowed section 179 deduction, matching line 13 within the supported depreciation cases.

### 14 (sc.line14) — Employee benefit programs (other than on line 19)
Status: **MATCH**

Model: Matches the line 14 employee benefit programs rule, excluding pension/profit-sharing plans and personal contributions.

### 15 — Insurance (other than health)
Status: **MATCH**

Model: Matches the line 15 business insurance rule and its self-insurance and lost-earnings exclusions.

### 16a — Interest: mortgage (paid to banks, etc.)
Status: **MATCH**

Model: Matches the line 16a mortgage interest rule for business real property and Form 1098 reporting.

### 16b — Interest: other
Status: **MATCH**

Model: Matches the line 16b other business interest rules, including the future-year, shared mortgage and Schedule 1-A limitations.

### 17 — Legal and professional services
Status: **MATCH**

Model: Matches the line 17 accountant and attorney fees rule, including business tax advice and preparation.

### 18 — Office expense
Status: **MATCH**

Model: Matches the line 18 office supplies and postage input.

### 19 — Pension and profit-sharing plans
Status: **MATCH**

Model: Matches the line 19 employee pension/profit-sharing/annuity contribution rule and the Schedule 1 line 16 exclusion for self-contributions.

### 20a — Rent or lease: vehicles, machinery, and equipment
Status: **MATCH**

Model: Matches the line 20a vehicle, machinery and equipment rent/lease computation; inclusion-amount cases are screened out.

### 20b — Rent or lease: other business property
Status: **MATCH**

Model: Matches the line 20b rent for other business property input.

### 21 — Repairs and maintenance
Status: **MATCH**

Model: Matches the line 21 incidental repairs and maintenance rule and capitalization exclusions.

### 22 — Supplies (not included in Part III)
Status: **MATCH**

Model: Matches the line 22 materials and supplies rule, including incidental supplies and the capitalization limitation.

### 23 — Taxes and licenses
Status: **MATCH**

Model: Matches the line 23 business taxes and licenses list and the stated exclusions.

### 24a — Travel
Status: **MATCH**

Model: Matches the line 24a travel and incidental expense rules, including the $5 method and convention limitation.

### 24b — Deductible meals
Status: **MATCH**

Model: Matches the line 24b structure: 50% meals, 80% DOT-hours meals, and fully deductible meal and incidental exceptions.

### 25 — Utilities
Status: **MATCH**

Model: Matches the line 25 utility expense rule and home-phone base-rate limitation.

### 26 — Wages (less employment credits)
Status: **MATCH**

Model: Matches the line 26 wages rule, excluding amounts paid to yourself, wages deducted elsewhere, and fringe-benefit amounts claimed elsewhere; credits are screened.

### 27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **MATCH**

Model: The energy efficient commercial buildings deduction is excluded by sc.special, so within supported cases line 27a is zero; the refusal names Form 7205.

### 48 — Total other expenses
Status: **MATCH**

Model: Matches the line 48 total other expenses rule and the Part V exclusion from lines 8-27a and line 30.

### 27b — Other expenses (from line 48)
Status: **MATCH**

Model: Matches the line 27b instruction to enter the amount from line 48.

### 28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **MATCH**

Model: Matches the line 28 addition of lines 8 through 27b.

### 29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **MATCH**

Model: Matches the line 29 subtraction of line 28 from line 7.

### (screen) (sc.ho_uses) — Do you claim a deduction for business use of your home for this business?
Status: **MATCH**

Model: Matches the business-use-of-home screen for a qualifying home office or storage use.

### (screen) (sc.ho_other) — Does any of these apply to your business use of your home for this business?
Status: **MATCH**

Model: Matches the Form 8829, multiple-home, daycare, shared, part-year/change, other-place, Form 8949/4797, and timely-original-return limitations.

### 30(b) — The part of your home used for business (square feet)
Status: **MATCH**

Model: Matches the Schedule C line 30(b) square footage input; multi-business and special simplified-method cases are refused.

### 30(a) — Total square footage of your home
Status: **MATCH**

Model: Matches the Schedule C line 30(a) total square footage input.

### 3a — Maximum allowable amount (per square foot)
Status: **MATCH**

Model: Matches the Simplified Method Worksheet line 3a maximum allowable amount of $5.

### 4 (sc.ho_line4) — Multiply line 2 by line 3c
Status: **MATCH**

Model: Equivalent to worksheet line 4, multiplying the allowed square footage (capped at 300) by line 3c.

### 1 (sc.ho_line1) — Gross income limitation (Schedule C, line 29)
Status: **MATCH**

Model: Within the supported all-home-income case, worksheet line 1 is the Schedule C line 29 gross income limitation; special cases are refused.

### 5 (sc.ho_line5) — Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4
Status: **MATCH**

Model: Matches the smaller-of-line-1-or-line-4 rule within supported cases; cases where both section 179 and home-office limits could bind are refused.

### 30 — Expenses for business use of your home
Status: **MATCH**

Model: Matches the line 30 rule to enter the simplified-method worksheet line 5 amount when the home-office deduction is claimed, otherwise zero.

### 31 — Net profit or (loss). Subtract line 30 from line 29
Status: **MATCH**

Model: Matches the line 31 subtraction of line 30 from line 29.

### 32 — If you have a loss, is all your investment in this business at risk (box 32a)?
Status: **MISMATCH**

Restated: Input — Is all your investment in this business at risk (box 32a)? Answer no if any of these is invested in it: a nonrecourse loan used to finance the business, buy property used in it, or buy the business, that is not secured by your own property other than property used in the business and that you are not personally responsible to repay; cash, property or borrowed money protected against loss by a guarantee, stop-loss agreement or similar arrangement (casualty and tort-liability insurance do not count); money borrowed for use in the business from someone who has an interest in it other than as a creditor, or from a person related (under section 465(b)(3)(C)) to someone other than you who has such an interest

Model: IRS instructions state 'there is an exception for certain nonrecourse financing borrowed by you in connection with holding real property'; the restatement treats any such nonrecourse loan as not at risk and omits that exception.

Ruling: scope; accepted over-refusal. A filer whose only nonrecourse financing is qualified real property financing answers no and is refused through sc.not_at_risk, though that financing is at risk; a refusal, never a wrong amount.

### 33 — Method used to value closing inventory: other than cost or lower of cost or market, or a c
Status: **MATCH**

Model: Matches the cost/lower-of-cost-or-market limitation and combines the line 34 change question as a refusal screen; other methods and changes are refused.

### 35 — Inventory at beginning of year
Status: **MATCH**

Model: Matches the beginning inventory input; other inventory methods or valuation changes are refused.

### 36 — Purchases less cost of items withdrawn for personal use
Status: **MATCH**

Model: Matches the line 36 purchases less personal withdrawals rule.

### 37 — Cost of labor
Status: **MATCH**

Model: Matches the line 37 cost of labor rule and the exclusion of amounts paid to yourself.

### 38 — Materials and supplies
Status: **MATCH**

Model: Matches the line 38 materials and supplies input.

### 39 — Other costs
Status: **MATCH**

Model: Matches the line 39 other costs input.

### 40 — Add lines 35 through 39
Status: **MATCH**

Model: Matches the line 40 addition of lines 35 through 39.

### 41 — Inventory at end of year
Status: **MATCH**

Model: Matches the line 41 ending inventory input.

### 42 — Cost of goods sold. Subtract line 41 from line 40
Status: **MATCH**

Model: Matches the line 42 subtraction of line 41 from line 40.

### 12 (sc.s179_allowed) — Section 179 expense deduction for this business
Status: **MATCH**

Model: Matches the section 179 deduction allocation for line 13: current elected amount if equal to the deduction, otherwise the single-business return deduction; multi-business allocation is refused.

### (screen) (sc.hi_uses) — Health insurance established under this business
Status: **MATCH**

Model: Matches the Form 7206 established-under-the-business and material-income-producing-factor conditions.

### (screen) (sc.hi_screen) — Does any of these apply to this health insurance?
Status: **MATCH**

Model: Matches the Form 7206/Pub. 974 exclusions for Marketplace PTC, Form 2555, S corporation, optional method, retired public safety officer, and multiple LTC business entries.

### 1 (sc.f7206_line1) — Health insurance payments (other than long-term care)
Status: **MATCH**

Model: Matches Form 7206 line 1, including medical/dental/vision and voluntary Medicare premiums, with employer-subsidized months, QSEHRA, and LTC excluded.

### 2 (sc.f7206_line2) — Qualified long-term care insurance (the smaller of payments or the age limit, for each per
Status: **MATCH**

Model: Matches Form 7206 line 2 by summing the per-person smaller-of-(a)-or-(b) long-term care amounts.

### 3 (sc.f7206_line3) — Add lines 1 and 2
Status: **MATCH**

Model: Matches Form 7206 line 3 addition of lines 1 and 2.

### 4 (sc.f7206_line4) — Net profit from the trade or business under which the insurance plan is established
Status: **MISMATCH**

Restated: Enter the amount from helper "Net profit of this business (zero for a loss)".

Model: IRS line 4 says 'Enter your net profit* and any other earned income** from the trade or business'; the restatement uses only a zero-for-loss net profit helper and omits other earned income.

Ruling: scope; f7206 line 4 footnote, "Earned income includes net earnings and gains from the sale, transfer, or licensing of property you created. However, it doesn't include capital gain income". The only earned income from the business the tool admits is its Schedule C net profit; Form 4797 and other income are refused (sd.other_forms, scope.yaml).

### 5 (sc.f7206_line5) — Total of all net profits from Schedule C, line 31
Status: **MISMATCH**

Restated: Enter the amount from person helper "Total of all net profits of this person's businesses (losses not included)".

Model: IRS line 5 requires 'all net profits' from Schedule C, Schedule F, or K-1 code A plus other allocable income; the restatement sums only Schedule C net profits.

Ruling: scope; Schedule F and K-1 profits are refused by the self-employment screen (person.x_other) and other earned income outside Schedule C is refused (sd.other_forms, scope.yaml), so the sum of Schedule C net profits is the line on every computed return.

### 7 (sc.f7206_line7) — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax, by the p
Status: **MATCH**

Model: Matches Form 7206 line 6-7 by multiplying Schedule 1 line 15 by line 4 divided by line 5, with zero when line 4 is not positive.

### 8 (sc.f7206_line8) — Subtract line 7 from line 4
Status: **MATCH**

Model: Matches Form 7206 line 8, subtracting line 7 from line 4 and not going below zero.

### 9 (sc.f7206_line9) — Schedule 1, line 16, attributable to the same trade or business
Status: **MISMATCH**

Restated: Choose — [helper "Line 4 is more than zero" = true → helper "This person's SEP or SIMPLE deduction times line 4 divided by line 5"] [helper "Line 4 is more than zero" = false → helper "Zero"]

Model: IRS line 9 says 'Enter the amount ... from Schedule 1, line 16 ... attributable to the same trade or business'; the restatement instead prorates that amount by line 4 divided by line 5.

Ruling: ambiguity (amb.2025.f7206_plan_attribution, now linked on sc.f7206_line9); the line 16 deduction is attributed in proportion to net profit, the recorded reading.

### 10 (sc.f7206_line10) — Subtract line 9 from line 8
Status: **MATCH**

Model: Matches Form 7206 line 10, subtracting line 9 from line 8 and not going below zero.

### 13 (sc.f7206_line13) — Subtract line 12 from line 10
Status: **MATCH**

Model: For the supported non-S-corporation case with no Form 2555, line 12 is zero, so entering line 10 matches Form 7206 line 13; those exclusions are refused.

### 14 (sc.f7206_line14) — Self-employed health insurance deduction
Status: **MATCH**

Model: Matches Form 7206 line 14 by taking the smaller of line 3 or line 13 when health insurance is established under the business, otherwise zero.

### 1(c) — Qualified business income or (loss) of this business
Status: **MATCH**

Model: Matches QBI computation by starting with the business net profit and subtracting the deductible self-employment tax, retirement plan, and self-employed health insurance deductions attributable to the business.

### (screen) (sc.tips_ot) — Tips or overtime in this business to be deducted on Schedule 1-A
Status: **MATCH**

Model: Matches the new qualified tips/qualified overtime Schedule 1-A screen, distinguishing those amounts from Schedule C income.

## Raw response

```yaml
lines:
  - key: "(screen) (sc.statutory)"
    status: MATCH
    reason: "Matches the statutory employee screen from the Schedule C line 1 and line 31 instructions; notary cases are named as excluded."
  - key: "G"
    status: MATCH
    reason: "Matches the line G material participation tests, oil and gas exception, and non-rental activity condition."
  - key: "(screen) (sc.spouse_owned)"
    status: MATCH
    reason: "Matches the spouse-owned/QJV/community property exclusion described in the Schedule C instructions."
  - key: "F"
    status: MATCH
    reason: "Matches the accounting method, Form 3115/section 481(a), small business capitalization, tax shelter, and long-term contract points in the line F instructions."
  - key: "(screen) (sc.special)"
    status: MATCH
    reason: "The screen enumerates the special items described in the instructions and the program refuses cases it excludes."
  - key: "1 (sc.line1)"
    status: MATCH
    reason: "Matches the line 1 gross receipts rule, including Forms 1099-NEC/1099-K and the NIL and Schedule E exception; the screen refusal names excluded cases."
  - key: "2 (sc.line2)"
    status: MATCH
    reason: "Matches the line 2 rule to report returns and allowances as a positive number."
  - key: "3 (sc.line3)"
    status: MATCH
    reason: "Matches the line 3 subtraction of line 2 from line 1."
  - key: "4 (sc.line4)"
    status: MATCH
    reason: "Matches the line 4 instruction to enter the amount from line 42."
  - key: "5 (sc.line5)"
    status: MATCH
    reason: "Matches the line 5 subtraction of line 4 from line 3."
  - key: "6"
    status: MATCH
    reason: "Matches the line 6 other business income examples and the retained sales tax rule."
  - key: "7 (sc.line7)"
    status: MATCH
    reason: "Matches the line 7 addition of lines 5 and 6."
  - key: "8 (sc.line8)"
    status: MATCH
    reason: "Matches the line 8 advertising expense input."
  - key: "9 (sc.line9)"
    status: MATCH
    reason: "Matches the line 9 car and truck expense aggregation from the vehicle entries."
  - key: "10 (sc.line10)"
    status: MATCH
    reason: "Matches the line 10 commissions and fees rule, excluding capitalized or elsewhere-deducted amounts."
  - key: "11"
    status: MATCH
    reason: "Matches the line 11 contract labor rule and the lines 17, 21, 26 and 37 exclusions."
  - key: "12 (sc.line12)"
    status: MATCH
    reason: "Depletion is excluded by the sc.special screen, so within supported cases line 12 is zero; the refusal names depletion."
  - key: "13 (sc.line13)"
    status: MATCH
    reason: "The line adds non-section-179 depreciation and the allowed section 179 deduction, matching line 13 within the supported depreciation cases."
  - key: "14 (sc.line14)"
    status: MATCH
    reason: "Matches the line 14 employee benefit programs rule, excluding pension/profit-sharing plans and personal contributions."
  - key: "15"
    status: MATCH
    reason: "Matches the line 15 business insurance rule and its self-insurance and lost-earnings exclusions."
  - key: "16a"
    status: MATCH
    reason: "Matches the line 16a mortgage interest rule for business real property and Form 1098 reporting."
  - key: "16b"
    status: MATCH
    reason: "Matches the line 16b other business interest rules, including the future-year, shared mortgage and Schedule 1-A limitations."
  - key: "17"
    status: MATCH
    reason: "Matches the line 17 accountant and attorney fees rule, including business tax advice and preparation."
  - key: "18"
    status: MATCH
    reason: "Matches the line 18 office supplies and postage input."
  - key: "19"
    status: MATCH
    reason: "Matches the line 19 employee pension/profit-sharing/annuity contribution rule and the Schedule 1 line 16 exclusion for self-contributions."
  - key: "20a"
    status: MATCH
    reason: "Matches the line 20a vehicle, machinery and equipment rent/lease computation; inclusion-amount cases are screened out."
  - key: "20b"
    status: MATCH
    reason: "Matches the line 20b rent for other business property input."
  - key: "21"
    status: MATCH
    reason: "Matches the line 21 incidental repairs and maintenance rule and capitalization exclusions."
  - key: "22"
    status: MATCH
    reason: "Matches the line 22 materials and supplies rule, including incidental supplies and the capitalization limitation."
  - key: "23"
    status: MATCH
    reason: "Matches the line 23 business taxes and licenses list and the stated exclusions."
  - key: "24a"
    status: MATCH
    reason: "Matches the line 24a travel and incidental expense rules, including the $5 method and convention limitation."
  - key: "24b"
    status: MATCH
    reason: "Matches the line 24b structure: 50% meals, 80% DOT-hours meals, and fully deductible meal and incidental exceptions."
  - key: "25"
    status: MATCH
    reason: "Matches the line 25 utility expense rule and home-phone base-rate limitation."
  - key: "26"
    status: MATCH
    reason: "Matches the line 26 wages rule, excluding amounts paid to yourself, wages deducted elsewhere, and fringe-benefit amounts claimed elsewhere; credits are screened."
  - key: "27a"
    status: MATCH
    reason: "The energy efficient commercial buildings deduction is excluded by sc.special, so within supported cases line 27a is zero; the refusal names Form 7205."
  - key: "48"
    status: MATCH
    reason: "Matches the line 48 total other expenses rule and the Part V exclusion from lines 8-27a and line 30."
  - key: "27b"
    status: MATCH
    reason: "Matches the line 27b instruction to enter the amount from line 48."
  - key: "28"
    status: MATCH
    reason: "Matches the line 28 addition of lines 8 through 27b."
  - key: "29"
    status: MATCH
    reason: "Matches the line 29 subtraction of line 28 from line 7."
  - key: "(screen) (sc.ho_uses)"
    status: MATCH
    reason: "Matches the business-use-of-home screen for a qualifying home office or storage use."
  - key: "(screen) (sc.ho_other)"
    status: MATCH
    reason: "Matches the Form 8829, multiple-home, daycare, shared, part-year/change, other-place, Form 8949/4797, and timely-original-return limitations."
  - key: "30(b)"
    status: MATCH
    reason: "Matches the Schedule C line 30(b) square footage input; multi-business and special simplified-method cases are refused."
  - key: "30(a)"
    status: MATCH
    reason: "Matches the Schedule C line 30(a) total square footage input."
  - key: "3a"
    status: MATCH
    reason: "Matches the Simplified Method Worksheet line 3a maximum allowable amount of $5."
  - key: "4 (sc.ho_line4)"
    status: MATCH
    reason: "Equivalent to worksheet line 4, multiplying the allowed square footage (capped at 300) by line 3c."
  - key: "1 (sc.ho_line1)"
    status: MATCH
    reason: "Within the supported all-home-income case, worksheet line 1 is the Schedule C line 29 gross income limitation; special cases are refused."
  - key: "5 (sc.ho_line5)"
    status: MATCH
    reason: "Matches the smaller-of-line-1-or-line-4 rule within supported cases; cases where both section 179 and home-office limits could bind are refused."
  - key: "30"
    status: MATCH
    reason: "Matches the line 30 rule to enter the simplified-method worksheet line 5 amount when the home-office deduction is claimed, otherwise zero."
  - key: "31"
    status: MATCH
    reason: "Matches the line 31 subtraction of line 30 from line 29."
  - key: "32"
    status: MISMATCH
    reason: "IRS instructions state 'there is an exception for certain nonrecourse financing borrowed by you in connection with holding real property'; the restatement treats any such nonrecourse loan as not at risk and omits that exception."
  - key: "33"
    status: MATCH
    reason: "Matches the cost/lower-of-cost-or-market limitation and combines the line 34 change question as a refusal screen; other methods and changes are refused."
  - key: "35"
    status: MATCH
    reason: "Matches the beginning inventory input; other inventory methods or valuation changes are refused."
  - key: "36"
    status: MATCH
    reason: "Matches the line 36 purchases less personal withdrawals rule."
  - key: "37"
    status: MATCH
    reason: "Matches the line 37 cost of labor rule and the exclusion of amounts paid to yourself."
  - key: "38"
    status: MATCH
    reason: "Matches the line 38 materials and supplies input."
  - key: "39"
    status: MATCH
    reason: "Matches the line 39 other costs input."
  - key: "40"
    status: MATCH
    reason: "Matches the line 40 addition of lines 35 through 39."
  - key: "41"
    status: MATCH
    reason: "Matches the line 41 ending inventory input."
  - key: "42"
    status: MATCH
    reason: "Matches the line 42 subtraction of line 41 from line 40."
  - key: "12 (sc.s179_allowed)"
    status: MATCH
    reason: "Matches the section 179 deduction allocation for line 13: current elected amount if equal to the deduction, otherwise the single-business return deduction; multi-business allocation is refused."
  - key: "(screen) (sc.hi_uses)"
    status: MATCH
    reason: "Matches the Form 7206 established-under-the-business and material-income-producing-factor conditions."
  - key: "(screen) (sc.hi_screen)"
    status: MATCH
    reason: "Matches the Form 7206/Pub. 974 exclusions for Marketplace PTC, Form 2555, S corporation, optional method, retired public safety officer, and multiple LTC business entries."
  - key: "1 (sc.f7206_line1)"
    status: MATCH
    reason: "Matches Form 7206 line 1, including medical/dental/vision and voluntary Medicare premiums, with employer-subsidized months, QSEHRA, and LTC excluded."
  - key: "2 (sc.f7206_line2)"
    status: MATCH
    reason: "Matches Form 7206 line 2 by summing the per-person smaller-of-(a)-or-(b) long-term care amounts."
  - key: "3 (sc.f7206_line3)"
    status: MATCH
    reason: "Matches Form 7206 line 3 addition of lines 1 and 2."
  - key: "4 (sc.f7206_line4)"
    status: MISMATCH
    reason: "IRS line 4 says 'Enter your net profit* and any other earned income** from the trade or business'; the restatement uses only a zero-for-loss net profit helper and omits other earned income."
  - key: "5 (sc.f7206_line5)"
    status: MISMATCH
    reason: "IRS line 5 requires 'all net profits' from Schedule C, Schedule F, or K-1 code A plus other allocable income; the restatement sums only Schedule C net profits."
  - key: "7 (sc.f7206_line7)"
    status: MATCH
    reason: "Matches Form 7206 line 6-7 by multiplying Schedule 1 line 15 by line 4 divided by line 5, with zero when line 4 is not positive."
  - key: "8 (sc.f7206_line8)"
    status: MATCH
    reason: "Matches Form 7206 line 8, subtracting line 7 from line 4 and not going below zero."
  - key: "9 (sc.f7206_line9)"
    status: MISMATCH
    reason: "IRS line 9 says 'Enter the amount ... from Schedule 1, line 16 ... attributable to the same trade or business'; the restatement instead prorates that amount by line 4 divided by line 5."
  - key: "10 (sc.f7206_line10)"
    status: MATCH
    reason: "Matches Form 7206 line 10, subtracting line 9 from line 8 and not going below zero."
  - key: "13 (sc.f7206_line13)"
    status: MATCH
    reason: "For the supported non-S-corporation case with no Form 2555, line 12 is zero, so entering line 10 matches Form 7206 line 13; those exclusions are refused."
  - key: "14 (sc.f7206_line14)"
    status: MATCH
    reason: "Matches Form 7206 line 14 by taking the smaller of line 3 or line 13 when health insurance is established under the business, otherwise zero."
  - key: "1(c)"
    status: MATCH
    reason: "Matches QBI computation by starting with the business net profit and subtracting the deductible self-employment tax, retirement plan, and self-employed health insurance deductions attributable to the business."
  - key: "(screen) (sc.tips_ot)"
    status: MATCH
    reason: "Matches the new qualified tips/qualified overtime Schedule 1-A screen, distinguishing those amounts from Schedule C income."
```
