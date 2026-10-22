# Render comparison — sc

The rendered English of every printed line of `Schedule C (Form 1040) — Profit or Loss From Business, one per business` (`rendered/2025/sc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-21 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 819a12a1dec9d68ecbed66b3783a9561f0dd8e6fd60d15a6fe10faabeaeb48e6 |
| subject sha256 | f549cdf4128550cca1545ae2e6682e8beb1fb0dc78d2706ad94399e87c184bff |
| lines judged | 75 |
| match / mismatch / unclear / missing | 71 / 1 / 3 / 0 |
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

Model: The line 1 instructions route statutory employee income (W-2 box 13 checked) to Schedule C, and the line 31 instructions treat statutory employees and notaries separately. The screen asks about exactly these cases.

### G — Did you "materially participate" in the operation of this business during 2025, and is the
Status: **MATCH**

Model: This follows the line G instruction: 'If your business activity is not a rental activity and you meet any of the material participation tests... or the exception for oil and gas applies, check the Yes box.' The examples given are tests 1-3 of the seven.

### (screen) (sc.spouse_owned) — Do you own this business together with your spouse (as a qualified joint venture, as commu
Status: **MATCH**

Model: The instructions cover spouse-owned businesses as qualified joint ventures, community property, or partnerships. The screen excludes these cases.

### F — Do you use an accounting method other than cash or accrual, or did you change your account
Status: **MATCH**

Model: This reflects the line F instructions (other methods, Form 3115, section 481(a)) and the Part II and Part III small business taxpayer rule of average gross receipts of $31 million or less.

### (screen) (sc.special) — For this business, do you have any of these: depletion (line 12); the energy efficient com
Status: **MATCH**

Model: Every listed item appears in the instructions as a special treatment: depletion, Form 7205, the employment credit reductions, Form 8990, recapture and inclusion amounts, chapter 11, Form 8873, timeshare installment sales, Notice 2014-7, R&E capitalization, the capital construction fund, and Form 2441 self contributions.

### 1 (sc.line1) — Gross receipts or sales
Status: **MATCH**

Model: Line 1 says 'Enter gross receipts from your trade or business... be sure line 1 includes amounts properly shown on your Forms 1099-NEC.' The refusal names the screened cases.

### 2 (sc.line2) — Returns and allowances
Status: **MATCH**

Model: The line 2 instruction reads 'Report your sales returns and allowances as a positive number on line 2.'

### 3 (sc.line3) — Subtract line 2 from line 1
Status: **MATCH**

Model: Line 3 on the form reads 'Subtract line 2 from line 1.'

### 4 (sc.line4) — Cost of goods sold (from line 42)
Status: **MATCH**

Model: Line 4 on the form reads 'Cost of goods sold (from line 42).'

### 5 (sc.line5) — Gross profit. Subtract line 4 from line 3
Status: **MATCH**

Model: Line 5 on the form reads 'Gross profit. Subtract line 4 from line 3.'

### 6 — Other income, including federal and state gasoline or fuel tax credit or refund
Status: **MATCH**

Model: The examples (scrap sales, recovered bad debts, interest, fuel tax refunds, prizes and awards, 1099-PATR) come from the line 6 instruction list. The list is given as 'such as', so it is not exclusive.

### 7 (sc.line7) — Gross income. Add lines 5 and 6
Status: **MATCH**

Model: Line 7 on the form reads 'Gross income. Add lines 5 and 6.'

### 8 (sc.line8) — Advertising
Status: **MATCH**

Model: Line 8 is advertising.

### 9 (sc.line9) — Car and truck expenses
Status: **MATCH**

Model: Line 9 is car and truck expenses. Summing the per-vehicle line 9 amounts gives the line total.

### 10 (sc.line10) — Commissions and fees
Status: **MATCH**

Model: The line 10 instruction reads 'Do not include commissions or fees that are capitalized or deducted elsewhere on your return.'

### 11 — Contract labor
Status: **MATCH**

Model: The line 11 instruction covers payments to persons you do not treat as employees, excluding 'contract labor includible on line 17, 21, 26, or 37.'

### 12 (sc.line12) — Depletion
Status: **MATCH**

Model: Line 12 is depletion. Depletion is excluded by the special screen, so zero is correct within the supported cases.

### 13 (sc.line13) — Depreciation and section 179 expense deduction (not included in Part III)
Status: **MISMATCH**

Restated: Add helper "Depreciation other than the section 179 deduction (Form 4562 lines 14, 17, 19 and 21)" and line 12 (sc.s179_allowed).

Model: Form 4562 line 28 says 'Add amounts in column (h), lines 25 through 27', but the helper adds only line 25 and column (h) of line 26, omitting line 27. Line 22 also adds 'lines 14 through 17, lines 19 and 20', while the helper omits lines 15, 16 and 20 and names no refusal for them.

Ruling: refusal located elsewhere; restatement accepted. As Form 4562 lines 22 and 28: the omitted lines are refused on the asset: line 15 (property elected out of MACRS) and line 16 (other depreciation, including ACRS) through asset.screen ('by a method other than the MACRS percentage tables') and the years placed in service the tool offers; line 20 (ADS) through asset.screen ('you depreciate it under ADS'); and line 27 (listed property used 50% or less in a qualified business use) through the asset's and the vehicle's low-use refusal ('Listed property used 50% or less in a qualified business use (Form 4562 line 27)', asset.yaml, scveh.yaml). With those refused the total is the lines listed.

### 14 (sc.line14) — Employee benefit programs (other than on line 19)
Status: **MATCH**

Model: This follows the line 14 instructions: employee programs such as accident and health plans, group-term life and dependent care, excluding self contributions and pension plans. The Form 8941 reduction and the Form 2441 self contributions are screened.

### 15 — Insurance (other than health)
Status: **MATCH**

Model: The line 15 instruction excludes 'amounts credited to a reserve for self-insurance or premiums paid for a policy that pays for your lost earnings.'

### 16a — Interest: mortgage (paid to banks, etc.)
Status: **MATCH**

Model: This follows the instruction: 'enter on line 16a the interest you paid for 2025 to banks or other financial institutions for which you received a Form 1098', excluding capitalized interest. The Form 8990 limit is screened.

### 16b — Interest: other
Status: **MATCH**

Model: The instructions direct mortgage interest without a Form 1098 to line 16b. The Schedule 1-A vehicle interest caution also matches.

### 17 — Legal and professional services
Status: **MATCH**

Model: The line 17 instruction covers fees 'directly related to operating your business', including tax advice and preparation of business tax forms.

### 18 — Office expense
Status: **MATCH**

Model: The line 18 instruction reads 'Include on this line your expenses for office supplies and postage.'

### 19 — Pension and profit-sharing plans
Status: **MATCH**

Model: This follows the line 19 instructions: employee contributions, including SEP, SIMPLE and SARSEP, with contributions for yourself going on Schedule 1, line 16.

### 20a — Rent or lease: vehicles, machinery, and equipment
Status: **MATCH**

Model: Line 20a takes 'the business portion of your rental cost' for vehicles, machinery and equipment. The inclusion amount for leases of 30 days or more is screened.

### 20b — Rent or lease: other business property
Status: **MATCH**

Model: The instruction reads 'Enter on line 20b amounts paid to rent or lease other property, such as office space.'

### 21 — Repairs and maintenance
Status: **MATCH**

Model: This follows the line 21 instruction: incidental repairs only, not your own labor, and not restorations or replacements.

### 22 — Supplies (not included in Part III)
Status: **MATCH**

Model: This follows the line 22 instruction: materials and supplies consumed and used, or incidental supplies purchased when no records of use are kept.

### 23 — Taxes and licenses
Status: **MATCH**

Model: The listed taxes and the exclusions follow the line 23 instructions. The Form 8846 reduction is screened.

### 24a — Travel
Status: **MATCH**

Model: The line 24a instruction covers lodging and transportation for overnight travel away from your tax home and excludes meals and entertainment.

### 24b — Deductible meals
Status: **MATCH**

Model: This applies 50%, 80% for DOT hours-of-service duty periods, and full deduction for meals treated as wages or reported on 1099-NEC, per 'Amount of deduction'. The text refers to Pub. 15 for 'other exceptions'.

### 25 — Utilities
Status: **MATCH**

Model: This follows the line 25 instructions: business utilities only, without the base rate of the first home phone line.

### 26 — Wages (less employment credits)
Status: **MATCH**

Model: Line 26 is salaries and wages, excluding amounts paid to yourself and wages deducted elsewhere. The employment credits are screened.

### 27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **MATCH**

Model: Line 27a is the energy efficient commercial buildings deduction (Form 7205). Form 7205 is screened, so zero is correct.

### 48 — Total other expenses
Status: **MATCH**

Model: Part V lists 'business expenses not included on lines 8-27a, or line 30', and line 48 is their total.

### 27b — Other expenses (from line 48)
Status: **MATCH**

Model: Line 27b on the form reads 'Other expenses (from line 48).'

### 28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **MATCH**

Model: Line 28 on the form reads 'Add lines 8 through 27b.'

### 29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **MATCH**

Model: Line 29 on the form reads 'Subtract line 28 from line 7.'

### (screen) (sc.ho_uses) — Do you claim a deduction for business use of your home for this business?
Status: **MATCH**

Model: This asks whether the filer claims the business use of home deduction. The line 30 text describes regular and exclusive use or storage of inventory.

### (screen) (sc.ho_other) — Does any of these apply to your business use of your home for this business?
Status: **MATCH**

Model: Each listed case (Form 8829, more than one home, daycare, shared use, part-year use, income from another location, Form 8949 or 4797 items) is a special case in the line 30 and worksheet instructions.

### 30(b) — The part of your home used for business (square feet)
Status: **MATCH**

Model: This asks for 'the part of your home used for business'. The refusals name the multiple-business 300 square foot allocation and the screened cases.

### 30(a) — Total square footage of your home
Status: **MATCH**

Model: The form asks for 'the total square footage of (a) your home.'

### 3a — Maximum allowable amount (per square foot)
Status: **MATCH**

Model: Worksheet line 3a reads 'Maximum allowable amount... $5.'

### 4 (sc.ho_line4) — Multiply line 2 by line 3c
Status: **MATCH**

Model: Line 4 is line 2 times line 3c, where line 2 is 'the smaller of the square feet you actually used or 300.' Line 3b is 1.0 because daycare is screened, so line 3c equals line 3a.

### 1 (sc.ho_line1) — Gross income limitation (Schedule C, line 29)
Status: **MATCH**

Model: Gross income limitation line A is Schedule C line 29. Lines B and D (Form 8949/4797 items) and income from another location are screened.

### 5 (sc.ho_line5) — Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4
Status: **MATCH**

Model: The worksheet says 'Enter the smaller of line 1 or line 4... If zero or less, enter -0-.' The branches give that result, and the circular section 179 case is refused under Pub. 946's two income limits.

### 30 — Expenses for business use of your home
Status: **MATCH**

Model: The instruction reads 'Include the amount from line 5 of the Simplified Method Worksheet on line 30.' The line is zero when no home use is claimed.

### 31 — Net profit or (loss). Subtract line 30 from line 29
Status: **MATCH**

Model: Line 31 on the form reads 'Subtract line 30 from line 29.' The passive and at-risk cases are screened or refused.

### 32 — If you have a loss, is all your investment in this business at risk (box 32a)?
Status: **MATCH**

Model: This restates the box 32b examples (nonrecourse loans, guarantees or stop-loss, amounts borrowed from interested persons) as their negation for box 32a.

### 33 — Method used to value closing inventory: other than cost or lower of cost or market, or a c
Status: **MATCH**

Model: Lines 33 and 34 ask about cost, lower of cost or market, or other methods, and about changes between opening and closing inventory. This combines them as the refusal gate.

### 35 — Inventory at beginning of year
Status: **MATCH**

Model: Line 35 reads 'Inventory at beginning of year. If different from last year's closing inventory, attach explanation.' Other methods are refused.

### 36 — Purchases less cost of items withdrawn for personal use
Status: **MATCH**

Model: Line 36 reads 'Purchases less cost of items withdrawn for personal use.'

### 37 — Cost of labor
Status: **MATCH**

Model: Line 37 reads 'Cost of labor. Do not include any amounts paid to yourself.'

### 38 — Materials and supplies
Status: **MATCH**

Model: Line 38 is materials and supplies.

### 39 — Other costs
Status: **MATCH**

Model: Line 39 is other costs.

### 40 — Add lines 35 through 39
Status: **MATCH**

Model: Line 40 reads 'Add lines 35 through 39.'

### 41 — Inventory at end of year
Status: **MATCH**

Model: Line 41 reads 'Inventory at end of year.'

### 42 — Cost of goods sold. Subtract line 41 from line 40
Status: **MATCH**

Model: Line 42 reads 'Cost of goods sold. Subtract line 41 from line 40.'

### 12 (sc.s179_allowed) — Section 179 expense deduction for this business
Status: **MATCH**

Model: This uses the elected amounts when Form 4562 line 12 equals line 8, or the return's line 12 when there is only one Schedule C. Multi-business allocation is refused, consistent with the line 12 instructions on allocating among businesses.

### (screen) (sc.hi_uses) — Health insurance established under this business
Status: **MATCH**

Model: The text says the plan must be 'established under your business', with the policy 'either in the name of the business or in the name of the individual.' Coverage includes your child under age 27.

### (screen) (sc.hi_screen) — Does any of these apply to this health insurance?
Status: **MATCH**

Model: Each listed case is named in the Form 7206 instructions as requiring special handling: Pub. 974 Marketplace/PTC, Form 2555, S corporation, optional methods, retired public safety officer, and LTC limits across multiple Forms 7206.

### 1 (sc.f7206_line1) — Health insurance payments (other than long-term care)
Status: **MATCH**

Model: This matches Form 7206 line 1 and the instructions: coverage under this business for you, your spouse, dependents and child under 27, Medicare premiums included, subsidized-plan months excluded, LTC excluded. Retirement plan payments are refused.

### 2 (sc.f7206_line2) — Qualified long-term care insurance (the smaller of payments or the age limit, for each per
Status: **UNCLEAR**

Restated: Add ltc.amount over every confirmed ltc entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: Line 2 requires 'for each person covered the smaller of (a) or (b)', with the age-based limits. The definition of ltc.amount is not given, so it cannot be confirmed that each entry is capped.

Ruling: representation; restatement accepted. ltc.amount is the smaller of the payments and the age limit for each person covered under this business's plan (ltc.yaml, Form 7206 line 2(a), 2(b)); the sum is over this business's entries, which are children of the sc entry. A person covered under more than one business is refused since BUG-0063.

### 3 (sc.f7206_line3) — Add lines 1 and 2
Status: **MATCH**

Model: Line 3 reads 'Add lines 1 and 2.'

### 4 (sc.f7206_line4) — Net profit from the trade or business under which the insurance plan is established
Status: **MATCH**

Model: Line 4 is the net profit from the business under which the plan is established. Optional methods are screened.

### 5 (sc.f7206_line5) — Total of all net profits from Schedule C, line 31
Status: **MATCH**

Model: Line 5 is the 'total of all net profits... Don't include any net losses.' Farm and partnership income are screened by the Schedule SE refusal.

### 7 (sc.f7206_line7) — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax, by the p
Status: **MATCH**

Model: This multiplies Schedule 1, line 15 (Schedule SE line 13) by line 6 (line 4 divided by line 5), with zero when line 4 is zero.

### 8 (sc.f7206_line8) — Subtract line 7 from line 4
Status: **MATCH**

Model: Line 8 reads 'Subtract line 7 from line 4.' The floor at zero does not change the value because line 7 cannot exceed line 4.

### 9 (sc.f7206_line9) — Schedule 1, line 16, attributable to the same trade or business
Status: **UNCLEAR**

Restated: Choose — [helper "Line 4 is more than zero" = true → helper "This person's SEP or SIMPLE deduction times line 4 divided by line 5"] [helper "Line 4 is more than zero" = false → helper "Zero"]

Model: Line 9 asks for the Schedule 1 line 16 amount 'attributable to the same trade or business in which the insurance plan is established.' The program prorates the person's whole deduction by share of net profits, and the text does not say whether proration equals that attribution.

Ruling: owner accepted (amb.2025.f7206_plan_attribution, T-041); restatement accepted. The form gives no method for the part of Schedule 1 line 16 attributable to the business; the project prorates by the business's share of net profits, as Form 7206 lines 6 and 7 do for the self-employment tax. (The register entry's premise that the plan limits are figured on all businesses is questioned under the person render log, Step 1.)

### 10 (sc.f7206_line10) — Subtract line 9 from line 8
Status: **MATCH**

Model: Line 10 reads 'Subtract line 9 from line 8.'

### 13 (sc.f7206_line13) — Subtract line 12 from line 10
Status: **MATCH**

Model: Line 13 subtracts line 12 (Form 2555) from line 10. Form 2555 and the S corporation case on line 11 are screened, so line 13 equals line 10.

### 14 (sc.f7206_line14) — Self-employed health insurance deduction
Status: **MATCH**

Model: Line 14 reads 'Enter the smaller of line 3 or line 13.' The line is zero when no plan is established under this business.

### 1(c) — Qualified business income or (loss) of this business
Status: **UNCLEAR**

Restated: Subtract helper "Deductions attributable to this business: self-employment tax, retirement plan and health insurance (Form 7206 for this business)" from helper "The amount for Schedule 1, line 3 and Schedule SE, line 2".

Model: Form 8995 QBI must account for the 'deductible part of self-employment tax, self-employment health insurance deduction, and contributions to qualified retirement plans' attributable to the business. The text gives no method for attributing these to a business, so the profit-share proration cannot be confirmed.

Ruling: owner accepted (amb.2025.qbi_attribution, T-041); restatement accepted. i8995 p. 2 says QBI accounts for the deductible part of self-employment tax, the self-employment health insurance deduction and contributions to qualified retirement plans attributable to the business but gives no method; the project attributes them by the business's share of net profits (Form 7206 lines 7 and 9) and its own Form 7206 line 14.

### (screen) (sc.tips_ot) — Tips or overtime in this business to be deducted on Schedule 1-A
Status: **MATCH**

Model: The What's New and Schedule 1-A text say qualified tips from a business and qualified overtime reported on 1099-NEC or 1099-MISC are deducted on Schedule 1-A. The screen asks about these.

## Raw response

```yaml
```yaml
lines:
  - key: "(screen) (sc.statutory)"
    status: MATCH
    reason: "The line 1 instructions route statutory employee income (W-2 box 13 checked) to Schedule C, and the line 31 instructions treat statutory employees and notaries separately. The screen asks about exactly these cases."
  - key: "G"
    status: MATCH
    reason: "This follows the line G instruction: 'If your business activity is not a rental activity and you meet any of the material participation tests... or the exception for oil and gas applies, check the Yes box.' The examples given are tests 1-3 of the seven."
  - key: "(screen) (sc.spouse_owned)"
    status: MATCH
    reason: "The instructions cover spouse-owned businesses as qualified joint ventures, community property, or partnerships. The screen excludes these cases."
  - key: "F"
    status: MATCH
    reason: "This reflects the line F instructions (other methods, Form 3115, section 481(a)) and the Part II and Part III small business taxpayer rule of average gross receipts of $31 million or less."
  - key: "(screen) (sc.special)"
    status: MATCH
    reason: "Every listed item appears in the instructions as a special treatment: depletion, Form 7205, the employment credit reductions, Form 8990, recapture and inclusion amounts, chapter 11, Form 8873, timeshare installment sales, Notice 2014-7, R&E capitalization, the capital construction fund, and Form 2441 self contributions."
  - key: "1 (sc.line1)"
    status: MATCH
    reason: "Line 1 says 'Enter gross receipts from your trade or business... be sure line 1 includes amounts properly shown on your Forms 1099-NEC.' The refusal names the screened cases."
  - key: "2 (sc.line2)"
    status: MATCH
    reason: "The line 2 instruction reads 'Report your sales returns and allowances as a positive number on line 2.'"
  - key: "3 (sc.line3)"
    status: MATCH
    reason: "Line 3 on the form reads 'Subtract line 2 from line 1.'"
  - key: "4 (sc.line4)"
    status: MATCH
    reason: "Line 4 on the form reads 'Cost of goods sold (from line 42).'"
  - key: "5 (sc.line5)"
    status: MATCH
    reason: "Line 5 on the form reads 'Gross profit. Subtract line 4 from line 3.'"
  - key: "6"
    status: MATCH
    reason: "The examples (scrap sales, recovered bad debts, interest, fuel tax refunds, prizes and awards, 1099-PATR) come from the line 6 instruction list. The list is given as 'such as', so it is not exclusive."
  - key: "7 (sc.line7)"
    status: MATCH
    reason: "Line 7 on the form reads 'Gross income. Add lines 5 and 6.'"
  - key: "8 (sc.line8)"
    status: MATCH
    reason: "Line 8 is advertising."
  - key: "9 (sc.line9)"
    status: MATCH
    reason: "Line 9 is car and truck expenses. Summing the per-vehicle line 9 amounts gives the line total."
  - key: "10 (sc.line10)"
    status: MATCH
    reason: "The line 10 instruction reads 'Do not include commissions or fees that are capitalized or deducted elsewhere on your return.'"
  - key: "11"
    status: MATCH
    reason: "The line 11 instruction covers payments to persons you do not treat as employees, excluding 'contract labor includible on line 17, 21, 26, or 37.'"
  - key: "12 (sc.line12)"
    status: MATCH
    reason: "Line 12 is depletion. Depletion is excluded by the special screen, so zero is correct within the supported cases."
  - key: "13 (sc.line13)"
    status: MISMATCH
    reason: "Form 4562 line 28 says 'Add amounts in column (h), lines 25 through 27', but the helper adds only line 25 and column (h) of line 26, omitting line 27. Line 22 also adds 'lines 14 through 17, lines 19 and 20', while the helper omits lines 15, 16 and 20 and names no refusal for them."
  - key: "14 (sc.line14)"
    status: MATCH
    reason: "This follows the line 14 instructions: employee programs such as accident and health plans, group-term life and dependent care, excluding self contributions and pension plans. The Form 8941 reduction and the Form 2441 self contributions are screened."
  - key: "15"
    status: MATCH
    reason: "The line 15 instruction excludes 'amounts credited to a reserve for self-insurance or premiums paid for a policy that pays for your lost earnings.'"
  - key: "16a"
    status: MATCH
    reason: "This follows the instruction: 'enter on line 16a the interest you paid for 2025 to banks or other financial institutions for which you received a Form 1098', excluding capitalized interest. The Form 8990 limit is screened."
  - key: "16b"
    status: MATCH
    reason: "The instructions direct mortgage interest without a Form 1098 to line 16b. The Schedule 1-A vehicle interest caution also matches."
  - key: "17"
    status: MATCH
    reason: "The line 17 instruction covers fees 'directly related to operating your business', including tax advice and preparation of business tax forms."
  - key: "18"
    status: MATCH
    reason: "The line 18 instruction reads 'Include on this line your expenses for office supplies and postage.'"
  - key: "19"
    status: MATCH
    reason: "This follows the line 19 instructions: employee contributions, including SEP, SIMPLE and SARSEP, with contributions for yourself going on Schedule 1, line 16."
  - key: "20a"
    status: MATCH
    reason: "Line 20a takes 'the business portion of your rental cost' for vehicles, machinery and equipment. The inclusion amount for leases of 30 days or more is screened."
  - key: "20b"
    status: MATCH
    reason: "The instruction reads 'Enter on line 20b amounts paid to rent or lease other property, such as office space.'"
  - key: "21"
    status: MATCH
    reason: "This follows the line 21 instruction: incidental repairs only, not your own labor, and not restorations or replacements."
  - key: "22"
    status: MATCH
    reason: "This follows the line 22 instruction: materials and supplies consumed and used, or incidental supplies purchased when no records of use are kept."
  - key: "23"
    status: MATCH
    reason: "The listed taxes and the exclusions follow the line 23 instructions. The Form 8846 reduction is screened."
  - key: "24a"
    status: MATCH
    reason: "The line 24a instruction covers lodging and transportation for overnight travel away from your tax home and excludes meals and entertainment."
  - key: "24b"
    status: MATCH
    reason: "This applies 50%, 80% for DOT hours-of-service duty periods, and full deduction for meals treated as wages or reported on 1099-NEC, per 'Amount of deduction'. The text refers to Pub. 15 for 'other exceptions'."
  - key: "25"
    status: MATCH
    reason: "This follows the line 25 instructions: business utilities only, without the base rate of the first home phone line."
  - key: "26"
    status: MATCH
    reason: "Line 26 is salaries and wages, excluding amounts paid to yourself and wages deducted elsewhere. The employment credits are screened."
  - key: "27a"
    status: MATCH
    reason: "Line 27a is the energy efficient commercial buildings deduction (Form 7205). Form 7205 is screened, so zero is correct."
  - key: "48"
    status: MATCH
    reason: "Part V lists 'business expenses not included on lines 8-27a, or line 30', and line 48 is their total."
  - key: "27b"
    status: MATCH
    reason: "Line 27b on the form reads 'Other expenses (from line 48).'"
  - key: "28"
    status: MATCH
    reason: "Line 28 on the form reads 'Add lines 8 through 27b.'"
  - key: "29"
    status: MATCH
    reason: "Line 29 on the form reads 'Subtract line 28 from line 7.'"
  - key: "(screen) (sc.ho_uses)"
    status: MATCH
    reason: "This asks whether the filer claims the business use of home deduction. The line 30 text describes regular and exclusive use or storage of inventory."
  - key: "(screen) (sc.ho_other)"
    status: MATCH
    reason: "Each listed case (Form 8829, more than one home, daycare, shared use, part-year use, income from another location, Form 8949 or 4797 items) is a special case in the line 30 and worksheet instructions."
  - key: "30(b)"
    status: MATCH
    reason: "This asks for 'the part of your home used for business'. The refusals name the multiple-business 300 square foot allocation and the screened cases."
  - key: "30(a)"
    status: MATCH
    reason: "The form asks for 'the total square footage of (a) your home.'"
  - key: "3a"
    status: MATCH
    reason: "Worksheet line 3a reads 'Maximum allowable amount... $5.'"
  - key: "4 (sc.ho_line4)"
    status: MATCH
    reason: "Line 4 is line 2 times line 3c, where line 2 is 'the smaller of the square feet you actually used or 300.' Line 3b is 1.0 because daycare is screened, so line 3c equals line 3a."
  - key: "1 (sc.ho_line1)"
    status: MATCH
    reason: "Gross income limitation line A is Schedule C line 29. Lines B and D (Form 8949/4797 items) and income from another location are screened."
  - key: "5 (sc.ho_line5)"
    status: MATCH
    reason: "The worksheet says 'Enter the smaller of line 1 or line 4... If zero or less, enter -0-.' The branches give that result, and the circular section 179 case is refused under Pub. 946's two income limits."
  - key: "30"
    status: MATCH
    reason: "The instruction reads 'Include the amount from line 5 of the Simplified Method Worksheet on line 30.' The line is zero when no home use is claimed."
  - key: "31"
    status: MATCH
    reason: "Line 31 on the form reads 'Subtract line 30 from line 29.' The passive and at-risk cases are screened or refused."
  - key: "32"
    status: MATCH
    reason: "This restates the box 32b examples (nonrecourse loans, guarantees or stop-loss, amounts borrowed from interested persons) as their negation for box 32a."
  - key: "33"
    status: MATCH
    reason: "Lines 33 and 34 ask about cost, lower of cost or market, or other methods, and about changes between opening and closing inventory. This combines them as the refusal gate."
  - key: "35"
    status: MATCH
    reason: "Line 35 reads 'Inventory at beginning of year. If different from last year's closing inventory, attach explanation.' Other methods are refused."
  - key: "36"
    status: MATCH
    reason: "Line 36 reads 'Purchases less cost of items withdrawn for personal use.'"
  - key: "37"
    status: MATCH
    reason: "Line 37 reads 'Cost of labor. Do not include any amounts paid to yourself.'"
  - key: "38"
    status: MATCH
    reason: "Line 38 is materials and supplies."
  - key: "39"
    status: MATCH
    reason: "Line 39 is other costs."
  - key: "40"
    status: MATCH
    reason: "Line 40 reads 'Add lines 35 through 39.'"
  - key: "41"
    status: MATCH
    reason: "Line 41 reads 'Inventory at end of year.'"
  - key: "42"
    status: MATCH
    reason: "Line 42 reads 'Cost of goods sold. Subtract line 41 from line 40.'"
  - key: "12 (sc.s179_allowed)"
    status: MATCH
    reason: "This uses the elected amounts when Form 4562 line 12 equals line 8, or the return's line 12 when there is only one Schedule C. Multi-business allocation is refused, consistent with the line 12 instructions on allocating among businesses."
  - key: "(screen) (sc.hi_uses)"
    status: MATCH
    reason: "The text says the plan must be 'established under your business', with the policy 'either in the name of the business or in the name of the individual.' Coverage includes your child under age 27."
  - key: "(screen) (sc.hi_screen)"
    status: MATCH
    reason: "Each listed case is named in the Form 7206 instructions as requiring special handling: Pub. 974 Marketplace/PTC, Form 2555, S corporation, optional methods, retired public safety officer, and LTC limits across multiple Forms 7206."
  - key: "1 (sc.f7206_line1)"
    status: MATCH
    reason: "This matches Form 7206 line 1 and the instructions: coverage under this business for you, your spouse, dependents and child under 27, Medicare premiums included, subsidized-plan months excluded, LTC excluded. Retirement plan payments are refused."
  - key: "2 (sc.f7206_line2)"
    status: UNCLEAR
    reason: "Line 2 requires 'for each person covered the smaller of (a) or (b)', with the age-based limits. The definition of ltc.amount is not given, so it cannot be confirmed that each entry is capped."
  - key: "3 (sc.f7206_line3)"
    status: MATCH
    reason: "Line 3 reads 'Add lines 1 and 2.'"
  - key: "4 (sc.f7206_line4)"
    status: MATCH
    reason: "Line 4 is the net profit from the business under which the plan is established. Optional methods are screened."
  - key: "5 (sc.f7206_line5)"
    status: MATCH
    reason: "Line 5 is the 'total of all net profits... Don't include any net losses.' Farm and partnership income are screened by the Schedule SE refusal."
  - key: "7 (sc.f7206_line7)"
    status: MATCH
    reason: "This multiplies Schedule 1, line 15 (Schedule SE line 13) by line 6 (line 4 divided by line 5), with zero when line 4 is zero."
  - key: "8 (sc.f7206_line8)"
    status: MATCH
    reason: "Line 8 reads 'Subtract line 7 from line 4.' The floor at zero does not change the value because line 7 cannot exceed line 4."
  - key: "9 (sc.f7206_line9)"
    status: UNCLEAR
    reason: "Line 9 asks for the Schedule 1 line 16 amount 'attributable to the same trade or business in which the insurance plan is established.' The program prorates the person's whole deduction by share of net profits, and the text does not say whether proration equals that attribution."
  - key: "10 (sc.f7206_line10)"
    status: MATCH
    reason: "Line 10 reads 'Subtract line 9 from line 8.'"
  - key: "13 (sc.f7206_line13)"
    status: MATCH
    reason: "Line 13 subtracts line 12 (Form 2555) from line 10. Form 2555 and the S corporation case on line 11 are screened, so line 13 equals line 10."
  - key: "14 (sc.f7206_line14)"
    status: MATCH
    reason: "Line 14 reads 'Enter the smaller of line 3 or line 13.' The line is zero when no plan is established under this business."
  - key: "1(c)"
    status: UNCLEAR
    reason: "Form 8995 QBI must account for the 'deductible part of self-employment tax, self-employment health insurance deduction, and contributions to qualified retirement plans' attributable to the business. The text gives no method for attributing these to a business, so the profit-share proration cannot be confirmed."
  - key: "(screen) (sc.tips_ot)"
    status: MATCH
    reason: "The What's New and Schedule 1-A text say qualified tips from a business and qualified overtime reported on 1099-NEC or 1099-MISC are deducted on Schedule 1-A. The screen asks about these."
```
```
