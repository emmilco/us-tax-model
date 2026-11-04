# Render comparison — sc

The rendered English of every printed line of `Schedule C (Form 1040) — Profit or Loss From Business, one per business` (`rendered/2025/sc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | ee875dadc6308766f4d3efe9bf4985526192ef445453bffd14f40e8172f02df5 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 20943341f7390ac694fdb843c313730d5f7ff04a35f9de4ed0fe9ae173076d0b |
| lines judged | 75 |
| match / mismatch / unclear / missing | 73 / 1 / 1 / 0 |
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

Model: Screens statutory employee income (the W-2 box 13 'Statutory employee' box) and notary fees, which the line 1 and line 31 instructions treat differently. The refusal names this exclusion.

### G — Did you "materially participate" in the operation of this business during 2025, and is the
Status: **MATCH**

Model: Restates line G: not a rental activity and meets any of the seven material participation tests, or the oil and gas working interest exception applies. Answering No triggers the refusal.

### (screen) (sc.spouse_owned) — Do you own this business together with your spouse (as a qualified joint venture, as commu
Status: **MATCH**

Model: Screens qualified joint venture, community property and partnership ownership, which the 'Business Owned and Operated by Spouses' instructions handle separately. The refusal names this.

### F — Do you use an accounting method other than cash or accrual, or did you change your account
Status: **MATCH**

Model: Screens other accounting methods, a change of method (Form 3115 or section 481(a)), uniform capitalization above the $31 million small business taxpayer test, tax shelters and section 460 long-term contracts. These match the line F, Part II and Part III instructions, and the refusal names them.

### (screen) (sc.special) — For this business, do you have any of these: depletion (line 12); the energy efficient com
Status: **MATCH**

Model: Each listed item (depletion, Form 7205, employment credits, Form 8990, recapture and inclusion amounts, chapter 11, Form 8873, installment method, Medicaid waiver, CCF, Form 2441, PAL, etc.) appears in the instructions. Screening them out is a narrowing that the refusal names.

### 1 (sc.line1) — Gross receipts or sales
Status: **MATCH**

Model: Gross receipts include amounts properly shown on Forms 1099-NEC. Seller-imposed sales tax collected from buyers is included, per the line 23 instruction 'you must also include the amount collected in gross receipts or sales on line 1'. NIL income that is not self-employment income goes on Schedule E.

### 2 (sc.line2) — Returns and allowances
Status: **MATCH**

Model: Returns and allowances are entered as a positive number, as the line 2 instructions say.

### 3 (sc.line3) — Subtract line 2 from line 1
Status: **MATCH**

Model: 'Subtract line 2 from line 1.'

### 4 (sc.line4) — Cost of goods sold (from line 42)
Status: **MATCH**

Model: 'Cost of goods sold (from line 42).'

### 5 (sc.line5) — Gross profit. Subtract line 4 from line 3
Status: **MATCH**

Model: 'Gross profit. Subtract line 4 from line 3.'

### 6 — Other income, including federal and state gasoline or fuel tax credit or refund
Status: **MATCH**

Model: The list (scrap sales, recovered bad debts, interest, fuel tax refunds and credits, prizes, 1099-PATR, retained sales tax) follows the line 6 and line 23 instructions. Section 481(a) items and recapture are screened elsewhere.

### 7 (sc.line7) — Gross income. Add lines 5 and 6
Status: **MATCH**

Model: 'Gross income. Add lines 5 and 6.'

### 8 (sc.line8) — Advertising
Status: **MATCH**

Model: Advertising expenses are entered directly.

### 9 (sc.line9) — Car and truck expenses
Status: **MATCH**

Model: Standard rate: business miles × 0.70 plus parking fees and tolls. Actual: the business portion of operating expenses, with depreciation and lease payments excluded and shown on lines 13 and 20a. A refusal covers the cases where the standard mileage rate is unavailable.

### 10 (sc.line10) — Commissions and fees
Status: **MATCH**

Model: 'Do not include commissions or fees that are capitalized or deducted elsewhere.'

### 11 — Contract labor
Status: **MATCH**

Model: Contract labor excludes amounts 'includible on line 17, 21, 26, or 37'.

### 12 (sc.line12) — Depletion
Status: **MATCH**

Model: Depletion is set to zero, and depletion is screened out by sc.special with a refusal.

### 13 (sc.line13) — Depreciation and section 179 expense deduction (not included in Part III)
Status: **MATCH**

Model: Uses Form 4562 lines 14, 17, 19 and line 21 (listed property line 28) plus this business's section 179 deduction. That matches the line 22 total, with lines 15, 16 and 20 (other methods and ADS) screened out.

### 14 (sc.line14) — Employee benefit programs (other than on line 19)
Status: **MATCH**

Model: Employee benefit programs other than pension plans, excluding contributions for yourself. The Form 8941 reduction is screened.

### 15 — Insurance (other than health)
Status: **MATCH**

Model: Business insurance, excluding a self-insurance reserve and lost-earnings policies, as the line 15 instructions say.

### 16a — Interest: mortgage (paid to banks, etc.)
Status: **MATCH**

Model: Mortgage interest reported on Form 1098 for business real property, excluding capitalized interest. Home mortgage interest goes to Schedule A under the simplified method, per the line 30 instructions.

### 16b — Interest: other
Status: **MATCH**

Model: Covers mortgage interest without a Form 1098, your share when the other person received the 1098, only the 2025 portion of prepaid interest, and excludes interest deducted on Schedule 1-A. All of these follow the line 16 instructions.

### 17 — Legal and professional services
Status: **MATCH**

Model: Legal and professional fees directly related to operating the business, including tax advice and preparation of business tax forms.

### 18 — Office expense
Status: **MATCH**

Model: 'Include on this line your expenses for office supplies and postage.'

### 19 — Pension and profit-sharing plans
Status: **MATCH**

Model: Plan contributions for employees go on line 19. Contributions for yourself go on Schedule 1, line 16, as the line 19 instructions say.

### 20a — Rent or lease: vehicles, machinery, and equipment
Status: **MATCH**

Model: Uses the business portion of rent for vehicles, machinery and equipment. Leased vehicles count only under actual expenses ('Do not deduct ... rent or lease payments' under the standard rate). The inclusion amount is screened.

### 20b — Rent or lease: other business property
Status: **MATCH**

Model: 'Amounts paid to rent or lease other property, such as office space.'

### 21 — Repairs and maintenance
Status: **MATCH**

Model: Incidental repairs only. Excludes your own labor and restorations or replacements, which must be capitalized.

### 22 — Supplies (not included in Part III)
Status: **MATCH**

Model: Materials and supplies actually consumed, or incidental supplies purchased when no records are kept. Books and instruments used up within a year are included; longer-lived items are depreciated.

### 23 — Taxes and licenses
Status: **MISMATCH**

Restated: Input — Business taxes and licenses: sales tax imposed on you as the seller, real estate and personal property taxes on business assets, licenses and regulatory fees paid each year (not licenses you must amortize, such as some liquor licenses), the employer share of social security and Medicare taxes, federal unemployment tax, federal highway use tax, state unemployment contributions (not income or self-employment tax, not taxes on property you bought, and not real estate taxes on your home, which with the simplified method for business use of the home you can deduct only on Schedule A); zero if none

Model: The IRS list includes 'Contributions to a state unemployment insurance fund, or paid family and medical leave program disability benefit fund if they are considered taxes under state law'. The restatement keeps only 'state unemployment contributions' and omits paid family and medical leave fund contributions.

Ruling: finding (low; pre-existing, not introduced by the package); i1040sc p. 9, Line 23, "Contributions to a state unemployment insurance fund, or paid family and medical leave program disability benefit fund if they are considered taxes under state law". The question names state unemployment contributions only, so a filer may leave out paid family and medical leave fund contributions (an understated deduction). The package changed only the license wording ("not licenses you must amortize"), which matches p. 9. See bklg/sc.findings.md.

### 24a — Travel
Status: **MATCH**

Model: Lodging, transportation and incidentals, either actual or $5 a day on no-meal days, excluding the standard meal allowance days. Includes the 1-year employment limit, the companion travel rule and the North American area convention rule. Luxury water travel is screened.

### 24b — Deductible meals
Status: **UNCLEAR**

Restated: Add helper "50% of the meals subject to the 50% limit", helper "80% of the meals under the hours of service limits", and helper "Meals and incidentals not subject to the 50% limit, deducted in full".

Model: The 50% and 80% DOT parts and the employee-wage and 1099-NEC full-deduction exceptions match the instructions. The added 100% categories (client-reimbursed meals, employee recreation, food for the public, meals sold) come from 'chapter 5 of Pub. 15 ... other exceptions', which was not provided.

Ruling: ambiguity (amb.2025.meals_full_exceptions); i1040sc p. 10, Line 24b, "See chapter 5 of Pub. 15, Employer's Tax Guide, for details and other exceptions". The added full-deduction categories are the register's recorded reading of those exceptions; the review pages did not include Pub. 15.

### 25 — Utilities
Status: **MATCH**

Model: Business-only utilities, excluding the base rate of the first residential phone line.

### 26 — Wages (less employment credits)
Status: **MATCH**

Model: Wages excluding amounts paid to yourself and fringe-benefit depreciation claimed elsewhere. The employment credit reductions are screened.

### 27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **MATCH**

Model: Set to zero, and the Form 7205 deduction is screened with a refusal.

### 48 — Total other expenses
Status: **MATCH**

Model: Part V: 'business expenses not included on lines 8-27a, or line 30'.

### 27b — Other expenses (from line 48)
Status: **MATCH**

Model: 'Other expenses (from line 48).'

### 28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **MATCH**

Model: 'Add lines 8 through 27b.'

### 29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **MATCH**

Model: 'Subtract line 28 from line 7.'

### (screen) (sc.ho_uses) — Do you claim a deduction for business use of your home for this business?
Status: **MATCH**

Model: Qualifying use is regular and exclusive business use, or regular storage of inventory or product samples. Daycare is screened separately.

### (screen) (sc.ho_other) — Does any of these apply to your business use of your home for this business?
Status: **MATCH**

Model: Screens Form 8829, multiple homes, daycare, shared use, part-year use or area changes, other places of business, related 4797/8949 gains or losses, and a return that is not timely and original. All are special cases in the line 30 instructions, and the refusal names them.

### 30(b) — The part of your home used for business (square feet)
Status: **MATCH**

Model: Square footage used for business throughout the year. The multiple-business 300 square foot allocation and the special cases are refused.

### 30(a) — Total square footage of your home
Status: **MATCH**

Model: Total square footage of the home, an informational entry for simplified method filers.

### 3a — Maximum allowable amount (per square foot)
Status: **MATCH**

Model: Worksheet line 3a is printed as $5.

### 4 (sc.ho_line4) — Multiply line 2 by line 3c
Status: **MATCH**

Model: Line 2 (the smaller of square feet used or 300) times line 3c. Line 3c equals line 3a because line 3b is 1.0 when daycare is screened out.

### 1 (sc.ho_line1) — Gross income limitation (Schedule C, line 29)
Status: **MATCH**

Model: Gross income limitation line A is Schedule C line 29. Lines B and D (gains and losses on 8949/4797) and income from other locations are screened, so line E equals line 29.

### 5 (sc.ho_line5) — Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4
Status: **MATCH**

Model: Gives the smaller of line 1 or line 4, floored at zero, in every case the program computes. The case where the section 179 business income limit and this limit interact is refused, citing the Pub. 946 two-income-limit procedure.

### 30 — Expenses for business use of your home
Status: **MATCH**

Model: 'Include the amount from line 5 of the Simplified Method Worksheet on line 30.' Zero when no home office is claimed.

### 31 — Net profit or (loss). Subtract line 30 from line 29
Status: **MATCH**

Model: 'Subtract line 30 from line 29.' Passive activities and prior-year PAL are screened; at-risk losses are refused through Form 6198.

### 32 — If you have a loss, is all your investment in this business at risk (box 32a)?
Status: **MATCH**

Model: Box 32b covers nonrecourse loans, guaranteed or stop-loss amounts (excluding casualty and tort insurance), and amounts borrowed from interested or related persons, as the line 32 instructions say.

### 33 — Method used to value closing inventory: other than cost or lower of cost or market, or a c
Status: **MATCH**

Model: Cost or lower of cost or market are supported. Other methods and line 34 changes are refused.

### 35 — Inventory at beginning of year
Status: **MATCH**

Model: Beginning inventory equals last year's closing inventory. Method changes are screened.

### 36 — Purchases less cost of items withdrawn for personal use
Status: **MATCH**

Model: 'Purchases less cost of items withdrawn for personal use.'

### 37 — Cost of labor
Status: **MATCH**

Model: 'Cost of labor. Do not include any amounts paid to yourself.'

### 38 — Materials and supplies
Status: **MATCH**

Model: Materials and supplies (line 38).

### 39 — Other costs
Status: **MATCH**

Model: Other costs (line 39).

### 40 — Add lines 35 through 39
Status: **MATCH**

Model: 'Add lines 35 through 39.'

### 41 — Inventory at end of year
Status: **MATCH**

Model: Inventory at end of year.

### 42 — Cost of goods sold. Subtract line 41 from line 40
Status: **MATCH**

Model: 'Subtract line 41 from line 40.'

### 12 (sc.s179_allowed) — Section 179 expense deduction for this business
Status: **MATCH**

Model: Uses this business's elected amount when Form 4562 line 12 equals the elected total. Otherwise uses line 12 for a single Schedule C. Allocating a limited deduction among several businesses ('you may allocate your allowable section 179 expense deduction among them') is refused.

### (screen) (sc.hi_uses) — Health insurance established under this business
Status: **MATCH**

Model: The plan must be established under the business, with the policy in your name or the business's name, and personal services must be a material income-producing factor.

### (screen) (sc.hi_screen) — Does any of these apply to this health insurance?
Status: **MATCH**

Model: Screens the Pub. 974 Marketplace/PTC case, Form 2555, S corporation shareholders, optional methods, retired public safety officers, and long-term care across plans. These are the special cases in the 7206 instructions, and the refusal names them.

### 1 (sc.f7206_line1) — Health insurance payments (other than long-term care)
Status: **MATCH**

Model: Follows Form 7206 line 1: medical, dental and vision coverage, voluntary Medicare premiums, and children under 27. Excludes subsidized-plan months (QSEHRA counts as subsidized) and long-term care.

### 2 (sc.f7206_line2) — Qualified long-term care insurance (the smaller of payments or the age limit, for each per
Status: **MATCH**

Model: For each covered person, the smaller of (a) payments or (b) the age limit, then totaled, as line 2 says.

### 3 (sc.f7206_line3) — Add lines 1 and 2
Status: **MATCH**

Model: 'Add lines 1 and 2.'

### 4 (sc.f7206_line4) — Net profit from the trade or business under which the insurance plan is established
Status: **MATCH**

Model: Net profit from the business under which the plan is established, using the Schedule C line 31 result and zero for a loss.

### 5 (sc.f7206_line5) — Total of all net profits from Schedule C, line 31
Status: **MATCH**

Model: 'Total of all net profits ... Don't include any net losses.' Schedule F and K-1 income are screened through the SE screen.

### 7 (sc.f7206_line7) — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax, by the p
Status: **MATCH**

Model: Deductible part of SE tax (Schedule SE line 13 = Schedule 1 line 15) multiplied by line 4 ÷ line 5, which is line 6. The program uses this person's own SE deduction.

### 8 (sc.f7206_line8) — Subtract line 7 from line 4
Status: **MATCH**

Model: 'Subtract line 7 from line 4.'

### 9 (sc.f7206_line9) — Schedule 1, line 16, attributable to the same trade or business
Status: **MATCH**

Model: Schedule 1 line 16 attributable to this business. Plans covering more than one Schedule C are refused, so the share is the whole deduction.

### 10 (sc.f7206_line10) — Subtract line 9 from line 8
Status: **MATCH**

Model: 'Subtract line 9 from line 8.'

### 13 (sc.f7206_line13) — Subtract line 12 from line 10
Status: **MATCH**

Model: Line 10 less line 12. Form 2555 is screened, so line 12 is zero.

### 14 (sc.f7206_line14) — Self-employed health insurance deduction
Status: **MATCH**

Model: 'Enter the smaller of line 3 or line 13.'

### 1(c) — Qualified business income or (loss) of this business
Status: **MATCH**

Model: Per the Form 8995 instructions, QBI from the Schedule C result is reduced by attributable items: 'deductible part of self-employment tax, self-employment health insurance deduction, and contributions to qualified retirement plans'.

### (screen) (sc.tips_ot) — Tips or overtime in this business to be deducted on Schedule 1-A
Status: **MATCH**

Model: Flags qualified tips and overtime deducted on Schedule 1-A, which the What's New section says are claimed there and not on Schedule C.

## Raw response

```yaml
```yaml
lines:
  - key: "(screen) (sc.statutory)"
    status: MATCH
    reason: "Screens statutory employee income (the W-2 box 13 'Statutory employee' box) and notary fees, which the line 1 and line 31 instructions treat differently. The refusal names this exclusion."
  - key: "G"
    status: MATCH
    reason: "Restates line G: not a rental activity and meets any of the seven material participation tests, or the oil and gas working interest exception applies. Answering No triggers the refusal."
  - key: "(screen) (sc.spouse_owned)"
    status: MATCH
    reason: "Screens qualified joint venture, community property and partnership ownership, which the 'Business Owned and Operated by Spouses' instructions handle separately. The refusal names this."
  - key: "F"
    status: MATCH
    reason: "Screens other accounting methods, a change of method (Form 3115 or section 481(a)), uniform capitalization above the $31 million small business taxpayer test, tax shelters and section 460 long-term contracts. These match the line F, Part II and Part III instructions, and the refusal names them."
  - key: "(screen) (sc.special)"
    status: MATCH
    reason: "Each listed item (depletion, Form 7205, employment credits, Form 8990, recapture and inclusion amounts, chapter 11, Form 8873, installment method, Medicaid waiver, CCF, Form 2441, PAL, etc.) appears in the instructions. Screening them out is a narrowing that the refusal names."
  - key: "1 (sc.line1)"
    status: MATCH
    reason: "Gross receipts include amounts properly shown on Forms 1099-NEC. Seller-imposed sales tax collected from buyers is included, per the line 23 instruction 'you must also include the amount collected in gross receipts or sales on line 1'. NIL income that is not self-employment income goes on Schedule E."
  - key: "2 (sc.line2)"
    status: MATCH
    reason: "Returns and allowances are entered as a positive number, as the line 2 instructions say."
  - key: "3 (sc.line3)"
    status: MATCH
    reason: "'Subtract line 2 from line 1.'"
  - key: "4 (sc.line4)"
    status: MATCH
    reason: "'Cost of goods sold (from line 42).'"
  - key: "5 (sc.line5)"
    status: MATCH
    reason: "'Gross profit. Subtract line 4 from line 3.'"
  - key: "6"
    status: MATCH
    reason: "The list (scrap sales, recovered bad debts, interest, fuel tax refunds and credits, prizes, 1099-PATR, retained sales tax) follows the line 6 and line 23 instructions. Section 481(a) items and recapture are screened elsewhere."
  - key: "7 (sc.line7)"
    status: MATCH
    reason: "'Gross income. Add lines 5 and 6.'"
  - key: "8 (sc.line8)"
    status: MATCH
    reason: "Advertising expenses are entered directly."
  - key: "9 (sc.line9)"
    status: MATCH
    reason: "Standard rate: business miles × 0.70 plus parking fees and tolls. Actual: the business portion of operating expenses, with depreciation and lease payments excluded and shown on lines 13 and 20a. A refusal covers the cases where the standard mileage rate is unavailable."
  - key: "10 (sc.line10)"
    status: MATCH
    reason: "'Do not include commissions or fees that are capitalized or deducted elsewhere.'"
  - key: "11"
    status: MATCH
    reason: "Contract labor excludes amounts 'includible on line 17, 21, 26, or 37'."
  - key: "12 (sc.line12)"
    status: MATCH
    reason: "Depletion is set to zero, and depletion is screened out by sc.special with a refusal."
  - key: "13 (sc.line13)"
    status: MATCH
    reason: "Uses Form 4562 lines 14, 17, 19 and line 21 (listed property line 28) plus this business's section 179 deduction. That matches the line 22 total, with lines 15, 16 and 20 (other methods and ADS) screened out."
  - key: "14 (sc.line14)"
    status: MATCH
    reason: "Employee benefit programs other than pension plans, excluding contributions for yourself. The Form 8941 reduction is screened."
  - key: "15"
    status: MATCH
    reason: "Business insurance, excluding a self-insurance reserve and lost-earnings policies, as the line 15 instructions say."
  - key: "16a"
    status: MATCH
    reason: "Mortgage interest reported on Form 1098 for business real property, excluding capitalized interest. Home mortgage interest goes to Schedule A under the simplified method, per the line 30 instructions."
  - key: "16b"
    status: MATCH
    reason: "Covers mortgage interest without a Form 1098, your share when the other person received the 1098, only the 2025 portion of prepaid interest, and excludes interest deducted on Schedule 1-A. All of these follow the line 16 instructions."
  - key: "17"
    status: MATCH
    reason: "Legal and professional fees directly related to operating the business, including tax advice and preparation of business tax forms."
  - key: "18"
    status: MATCH
    reason: "'Include on this line your expenses for office supplies and postage.'"
  - key: "19"
    status: MATCH
    reason: "Plan contributions for employees go on line 19. Contributions for yourself go on Schedule 1, line 16, as the line 19 instructions say."
  - key: "20a"
    status: MATCH
    reason: "Uses the business portion of rent for vehicles, machinery and equipment. Leased vehicles count only under actual expenses ('Do not deduct ... rent or lease payments' under the standard rate). The inclusion amount is screened."
  - key: "20b"
    status: MATCH
    reason: "'Amounts paid to rent or lease other property, such as office space.'"
  - key: "21"
    status: MATCH
    reason: "Incidental repairs only. Excludes your own labor and restorations or replacements, which must be capitalized."
  - key: "22"
    status: MATCH
    reason: "Materials and supplies actually consumed, or incidental supplies purchased when no records are kept. Books and instruments used up within a year are included; longer-lived items are depreciated."
  - key: "23"
    status: MISMATCH
    reason: "The IRS list includes 'Contributions to a state unemployment insurance fund, or paid family and medical leave program disability benefit fund if they are considered taxes under state law'. The restatement keeps only 'state unemployment contributions' and omits paid family and medical leave fund contributions."
  - key: "24a"
    status: MATCH
    reason: "Lodging, transportation and incidentals, either actual or $5 a day on no-meal days, excluding the standard meal allowance days. Includes the 1-year employment limit, the companion travel rule and the North American area convention rule. Luxury water travel is screened."
  - key: "24b"
    status: UNCLEAR
    reason: "The 50% and 80% DOT parts and the employee-wage and 1099-NEC full-deduction exceptions match the instructions. The added 100% categories (client-reimbursed meals, employee recreation, food for the public, meals sold) come from 'chapter 5 of Pub. 15 ... other exceptions', which was not provided."
  - key: "25"
    status: MATCH
    reason: "Business-only utilities, excluding the base rate of the first residential phone line."
  - key: "26"
    status: MATCH
    reason: "Wages excluding amounts paid to yourself and fringe-benefit depreciation claimed elsewhere. The employment credit reductions are screened."
  - key: "27a"
    status: MATCH
    reason: "Set to zero, and the Form 7205 deduction is screened with a refusal."
  - key: "48"
    status: MATCH
    reason: "Part V: 'business expenses not included on lines 8-27a, or line 30'."
  - key: "27b"
    status: MATCH
    reason: "'Other expenses (from line 48).'"
  - key: "28"
    status: MATCH
    reason: "'Add lines 8 through 27b.'"
  - key: "29"
    status: MATCH
    reason: "'Subtract line 28 from line 7.'"
  - key: "(screen) (sc.ho_uses)"
    status: MATCH
    reason: "Qualifying use is regular and exclusive business use, or regular storage of inventory or product samples. Daycare is screened separately."
  - key: "(screen) (sc.ho_other)"
    status: MATCH
    reason: "Screens Form 8829, multiple homes, daycare, shared use, part-year use or area changes, other places of business, related 4797/8949 gains or losses, and a return that is not timely and original. All are special cases in the line 30 instructions, and the refusal names them."
  - key: "30(b)"
    status: MATCH
    reason: "Square footage used for business throughout the year. The multiple-business 300 square foot allocation and the special cases are refused."
  - key: "30(a)"
    status: MATCH
    reason: "Total square footage of the home, an informational entry for simplified method filers."
  - key: "3a"
    status: MATCH
    reason: "Worksheet line 3a is printed as $5."
  - key: "4 (sc.ho_line4)"
    status: MATCH
    reason: "Line 2 (the smaller of square feet used or 300) times line 3c. Line 3c equals line 3a because line 3b is 1.0 when daycare is screened out."
  - key: "1 (sc.ho_line1)"
    status: MATCH
    reason: "Gross income limitation line A is Schedule C line 29. Lines B and D (gains and losses on 8949/4797) and income from other locations are screened, so line E equals line 29."
  - key: "5 (sc.ho_line5)"
    status: MATCH
    reason: "Gives the smaller of line 1 or line 4, floored at zero, in every case the program computes. The case where the section 179 business income limit and this limit interact is refused, citing the Pub. 946 two-income-limit procedure."
  - key: "30"
    status: MATCH
    reason: "'Include the amount from line 5 of the Simplified Method Worksheet on line 30.' Zero when no home office is claimed."
  - key: "31"
    status: MATCH
    reason: "'Subtract line 30 from line 29.' Passive activities and prior-year PAL are screened; at-risk losses are refused through Form 6198."
  - key: "32"
    status: MATCH
    reason: "Box 32b covers nonrecourse loans, guaranteed or stop-loss amounts (excluding casualty and tort insurance), and amounts borrowed from interested or related persons, as the line 32 instructions say."
  - key: "33"
    status: MATCH
    reason: "Cost or lower of cost or market are supported. Other methods and line 34 changes are refused."
  - key: "35"
    status: MATCH
    reason: "Beginning inventory equals last year's closing inventory. Method changes are screened."
  - key: "36"
    status: MATCH
    reason: "'Purchases less cost of items withdrawn for personal use.'"
  - key: "37"
    status: MATCH
    reason: "'Cost of labor. Do not include any amounts paid to yourself.'"
  - key: "38"
    status: MATCH
    reason: "Materials and supplies (line 38)."
  - key: "39"
    status: MATCH
    reason: "Other costs (line 39)."
  - key: "40"
    status: MATCH
    reason: "'Add lines 35 through 39.'"
  - key: "41"
    status: MATCH
    reason: "Inventory at end of year."
  - key: "42"
    status: MATCH
    reason: "'Subtract line 41 from line 40.'"
  - key: "12 (sc.s179_allowed)"
    status: MATCH
    reason: "Uses this business's elected amount when Form 4562 line 12 equals the elected total. Otherwise uses line 12 for a single Schedule C. Allocating a limited deduction among several businesses ('you may allocate your allowable section 179 expense deduction among them') is refused."
  - key: "(screen) (sc.hi_uses)"
    status: MATCH
    reason: "The plan must be established under the business, with the policy in your name or the business's name, and personal services must be a material income-producing factor."
  - key: "(screen) (sc.hi_screen)"
    status: MATCH
    reason: "Screens the Pub. 974 Marketplace/PTC case, Form 2555, S corporation shareholders, optional methods, retired public safety officers, and long-term care across plans. These are the special cases in the 7206 instructions, and the refusal names them."
  - key: "1 (sc.f7206_line1)"
    status: MATCH
    reason: "Follows Form 7206 line 1: medical, dental and vision coverage, voluntary Medicare premiums, and children under 27. Excludes subsidized-plan months (QSEHRA counts as subsidized) and long-term care."
  - key: "2 (sc.f7206_line2)"
    status: MATCH
    reason: "For each covered person, the smaller of (a) payments or (b) the age limit, then totaled, as line 2 says."
  - key: "3 (sc.f7206_line3)"
    status: MATCH
    reason: "'Add lines 1 and 2.'"
  - key: "4 (sc.f7206_line4)"
    status: MATCH
    reason: "Net profit from the business under which the plan is established, using the Schedule C line 31 result and zero for a loss."
  - key: "5 (sc.f7206_line5)"
    status: MATCH
    reason: "'Total of all net profits ... Don't include any net losses.' Schedule F and K-1 income are screened through the SE screen."
  - key: "7 (sc.f7206_line7)"
    status: MATCH
    reason: "Deductible part of SE tax (Schedule SE line 13 = Schedule 1 line 15) multiplied by line 4 ÷ line 5, which is line 6. The program uses this person's own SE deduction."
  - key: "8 (sc.f7206_line8)"
    status: MATCH
    reason: "'Subtract line 7 from line 4.'"
  - key: "9 (sc.f7206_line9)"
    status: MATCH
    reason: "Schedule 1 line 16 attributable to this business. Plans covering more than one Schedule C are refused, so the share is the whole deduction."
  - key: "10 (sc.f7206_line10)"
    status: MATCH
    reason: "'Subtract line 9 from line 8.'"
  - key: "13 (sc.f7206_line13)"
    status: MATCH
    reason: "Line 10 less line 12. Form 2555 is screened, so line 12 is zero."
  - key: "14 (sc.f7206_line14)"
    status: MATCH
    reason: "'Enter the smaller of line 3 or line 13.'"
  - key: "1(c)"
    status: MATCH
    reason: "Per the Form 8995 instructions, QBI from the Schedule C result is reduced by attributable items: 'deductible part of self-employment tax, self-employment health insurance deduction, and contributions to qualified retirement plans'."
  - key: "(screen) (sc.tips_ot)"
    status: MATCH
    reason: "Flags qualified tips and overtime deducted on Schedule 1-A, which the What's New section says are claimed there and not on Schedule C."
```
```
