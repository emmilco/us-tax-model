# Render comparison — sc

The rendered English of every printed line of `Schedule C (Form 1040) — Profit or Loss From Business, one per business` (`rendered/2025/sc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 154a524f08413f04ce5c6066b295d913a8c18232ba91749dfe5708b74df3e46e |
| lines judged | 75 |
| match / mismatch / unclear / missing | 71 / 1 / 3 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
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

Model: Matches the line 1 instruction: 'the "Statutory employee" box in box 13 of that form was checked.' The notary public case comes from the line 31 instructions. Both cases are refused through sc.screened.

### G — Did you "materially participate" in the operation of this business during 2025, and is the
Status: **MATCH**

Model: Follows the line G instruction: 'If your business activity is not a rental activity and you meet any of the material participation tests... or the exception for oil and gas applies, check the "Yes" box.' The examples paraphrase tests 1–3 correctly.

### (screen) (sc.spouse_owned) — Do you own this business together with your spouse (as a qualified joint venture, as commu
Status: **MATCH**

Model: Screens out the qualified joint venture, community property and partnership cases described under 'Business Owned and Operated by Spouses'. These are refused through sc.screened.

### F — Do you use an accounting method other than cash or accrual, or did you change your account
Status: **MATCH**

Model: Screens out 'any other method' and accounting method changes ('Form 3115', 'section 481(a) adjustment'). It also screens out uniform capitalization for businesses that are not small business taxpayers ('$31 million or less').

### (screen) (sc.special) — For this business, do you have any of these: depletion (line 12); the energy efficient com
Status: **MATCH**

Model: Each listed item is a case the instructions send elsewhere: depletion, Form 7205, the credits that reduce lines 14/23/26, Form 8990, listed property recapture, chapter 11, Form 8873, installment election, Notice 2014-7, R&E, CCF and Form 2441. All are refused through sc.screened.

### 1 (sc.line1) — Gross receipts or sales
Status: **MATCH**

Model: Gross receipts including 'amounts properly shown on your Forms 1099-NEC' and other Forms 1099. Prizes and awards are correctly sent to line 6. The screened items are refused.

### 2 (sc.line2) — Returns and allowances
Status: **MATCH**

Model: 'Report your sales returns and allowances as a positive number on line 2.'

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

Model: Input of other business income. The examples are taken from the line 6 list (scrap sales, bad debts recovered, interest, fuel tax refunds, prizes and awards, Form 1099-PATR). The 481(a) and recapture items are screened.

### 7 (sc.line7) — Gross income. Add lines 5 and 6
Status: **MATCH**

Model: 'Gross income. Add lines 5 and 6.'

### 8 (sc.line8) — Advertising
Status: **MATCH**

Model: Advertising expenses, entered as an input.

### 9 (sc.line9) — Car and truck expenses
Status: **MATCH**

Model: Car and truck expenses are summed per vehicle, which fits 'Enter the total on line 9' for each vehicle's standard mileage or actual expenses. The per-vehicle amount (scveh.line9) is not shown here.

### 10 (sc.line10) — Commissions and fees
Status: **MATCH**

Model: 'Do not include commissions or fees that are capitalized or deducted elsewhere on your return.'

### 11 — Contract labor
Status: **MATCH**

Model: Contract labor 'Do not include... contract labor includible on line 17, 21, 26, or 37.'

### 12 (sc.line12) — Depletion
Status: **MATCH**

Model: Depletion is set to zero. Any depletion is screened by sc.special and refused.

### 13 (sc.line13) — Depreciation and section 179 expense deduction (not included in Part III)
Status: **MISMATCH**

Restated: Add helper "Depreciation other than the section 179 deduction (Form 4562 lines 14, 17, 19 and 21)" and line 12 (sc.s179_allowed).

Model: Form 4562 line 22 totals 'line 12, lines 14 through 17, lines 19 and 20 in column (g), and line 21'. The helper takes only lines 14, 17, 19 (seven periods; no 25-year, residential or nonresidential real property) and 21. It omits line 15, line 16 ('Other depreciation (including ACRS)') and line 20 (ADS), and no refusal names these exclusions.

Ruling: refusal located elsewhere; restatement accepted. As Form 4562 line 22: The omitted lines are refused on the asset: line 15 (property elected out of MACRS) and line 16 (other depreciation, including ACRS) through asset.screen ('by a method other than the MACRS percentage tables') and the years placed in service the tool offers; lines 19g to 19j (25-year, residential rental, nonresidential real property) through asset.screen (real property) and the recovery-class lookup ('outside'); line 20 (ADS) through asset.screen ('you depreciate it under ADS'). With those refused the total is the lines listed.

### 14 (sc.line14) — Employee benefit programs (other than on line 19)
Status: **MATCH**

Model: Employee benefit programs, excluding 'contributions you made on your behalf' and pension plans on line 19. The Form 8941 reduction and self-employed dependent care contributions are screened.

### 15 — Insurance (other than health)
Status: **MATCH**

Model: 'Do not deduct amounts credited to a reserve for self-insurance or premiums paid for a policy that pays for your lost earnings.'

### 16a — Interest: mortgage (paid to banks, etc.)
Status: **MATCH**

Model: Restates 'enter on line 16a the interest you paid for 2025 to banks or other financial institutions for which you received a Form 1098', excluding interest that must be capitalized.

### 16b — Interest: other
Status: **MATCH**

Model: Covers mortgage interest without a Form 1098 and other business interest. It excludes vehicle interest deducted on Schedule 1-A, as the caution requires.

### 17 — Legal and professional services
Status: **MATCH**

Model: Fees of accountants and attorneys 'directly related to operating your business', including tax advice and preparation.

### 18 — Office expense
Status: **MATCH**

Model: 'Include on this line your expenses for office supplies and postage.'

### 19 — Pension and profit-sharing plans
Status: **MATCH**

Model: Contributions for employees. Self-employed contributions go on 'Schedule 1 (Form 1040), line 16, not on Schedule C.'

### 20a — Rent or lease: vehicles, machinery, and equipment
Status: **MATCH**

Model: 'If you rented or leased vehicles, machinery, or equipment, enter on line 20a the business portion of your rental cost.' Vehicle leases come from the vehicle roster.

### 20b — Rent or lease: other business property
Status: **MATCH**

Model: 'Enter on line 20b amounts paid to rent or lease other property, such as office space.'

### 21 — Repairs and maintenance
Status: **MATCH**

Model: Follows the line 21 wording on incidental repairs, own labor, and restorations or replacements.

### 22 — Supplies (not included in Part III)
Status: **MATCH**

Model: Follows the line 22 instruction on materials consumed and used, and on incidental supplies purchased when no records of use are kept.

### 23 — Taxes and licenses
Status: **MATCH**

Model: Lists the deductible taxes and licenses and the excluded taxes from the line 23 instructions. The Form 8846 reduction is screened.

### 24a — Travel
Status: **MATCH**

Model: 'Lodging and transportation connected with overnight travel... Do not include expenses for meals... Do not include entertainment.'

### 24b — Deductible meals
Status: **MATCH**

Model: Applies 50% generally, 80% for 'DOT hours of service limits', and full deduction for wage-treated and Form 1099-NEC meals. The text also refers to 'other exceptions' in Pub. 15.

### 25 — Utilities
Status: **MATCH**

Model: Business utilities only; 'do not deduct the base rate (including taxes) of the first phone line into your residence.'

### 26 — Wages (less employment credits)
Status: **MATCH**

Model: Wages excluding 'amounts paid to yourself' and wages deducted elsewhere. Reductions for employment credits are screened.

### 27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **MATCH**

Model: Set to zero. The Form 7205 deduction is screened by sc.special.

### 48 — Total other expenses
Status: **MATCH**

Model: Part V: 'business expenses not included on lines 8-27a, or line 30'.

### 27b — Other expenses (from line 48)
Status: **MATCH**

Model: 'Other expenses (from line 48).'

### 28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **MATCH**

Model: 'Add lines 8 through 27b'; all of lines 8 through 27b are included.

### 29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **MATCH**

Model: 'Subtract line 28 from line 7.'

### (screen) (sc.ho_uses) — Do you claim a deduction for business use of your home for this business?
Status: **MATCH**

Model: Asks whether a business use of home deduction is claimed, using the instructions' description of qualifying use.

### (screen) (sc.ho_other) — Does any of these apply to your business use of your home for this business?
Status: **MATCH**

Model: Screens out the cases the simplified worksheet handles specially: Form 8829, more than one home, daycare, shared use, part-year use or area changes, income from another location, and Form 8949/4797 gains or losses. These are refused via sc.ho_screened.

### 30(b) — The part of your home used for business (square feet)
Status: **MATCH**

Model: The area 'used regularly and exclusively for business... or regularly for storage of inventory or product samples'. The multi-business allocation and special cases are refused.

### 30(a) — Total square footage of your home
Status: **MATCH**

Model: 'Enter the total square footage of (a) your home.'

### 3a — Maximum allowable amount (per square foot)
Status: **MATCH**

Model: Worksheet line 3a 'Maximum allowable amount... $5'. Line 3b is 1.0 because daycare is screened.

### 4 (sc.ho_line4) — Multiply line 2 by line 3c
Status: **MATCH**

Model: Line 2 is 'the smaller of the square feet you actually used or 300', and line 4 is 'Multiply line 2 by line 3c'.

### 1 (sc.ho_line1) — Gross income limitation (Schedule C, line 29)
Status: **MATCH**

Model: Gross income limitation line A is 'Schedule C, line 29'. Lines B and D (Form 8949/4797 items) are screened.

### 5 (sc.ho_line5) — Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4
Status: **MATCH**

Model: Gives 'the smaller of line 1 or line 4... If zero or less, enter -0-' in the supported cases. The interaction with the section 179 income limit is refused per Pub. 946 'Two different taxable income limits'.

### 30 — Expenses for business use of your home
Status: **MATCH**

Model: 'Include the amount from line 5 of the Simplified Method Worksheet on line 30'; zero if no home office.

### 31 — Net profit or (loss). Subtract line 30 from line 29
Status: **MATCH**

Model: 'Net profit or (loss). Subtract line 30 from line 29.' Passive and at-risk limits are screened or refused.

### 32 — If you have a loss, is all your investment in this business at risk (box 32a)?
Status: **MATCH**

Model: Box 32a/32b at-risk question, using the instruction's examples of amounts not at risk. A not-at-risk loss is refused for Form 6198.

### 33 — Method used to value closing inventory: other than cost or lower of cost or market, or a c
Status: **MATCH**

Model: Combines line 33 'Other' and line 34 'any change... between opening and closing inventory'. Both are refused.

### 35 — Inventory at beginning of year
Status: **MATCH**

Model: 'Inventory at beginning of year. If different from last year's closing inventory, attach explanation.' Changes are refused.

### 36 — Purchases less cost of items withdrawn for personal use
Status: **MATCH**

Model: 'Purchases less cost of items withdrawn for personal use.'

### 37 — Cost of labor
Status: **MATCH**

Model: 'Cost of labor. Do not include any amounts paid to yourself.'

### 38 — Materials and supplies
Status: **MATCH**

Model: 'Materials and supplies.'

### 39 — Other costs
Status: **MATCH**

Model: 'Other costs.'

### 40 — Add lines 35 through 39
Status: **MATCH**

Model: 'Add lines 35 through 39.'

### 41 — Inventory at end of year
Status: **MATCH**

Model: 'Inventory at end of year.'

### 42 — Cost of goods sold. Subtract line 41 from line 40
Status: **MATCH**

Model: 'Cost of goods sold. Subtract line 41 from line 40.'

### 12 (sc.s179_allowed) — Section 179 expense deduction for this business
Status: **MATCH**

Model: Uses this business's elected amounts when the deduction equals the elected total. Otherwise it uses Form 4562 line 12 for a single business. Allocation among businesses ('you may allocate your allowable section 179 expense deduction among them') is refused.

### (screen) (sc.hi_uses) — Health insurance established under this business
Status: **MATCH**

Model: 'The insurance plan must be established... under your business'; for Schedule C 'a policy can be either in the name of the business or in the name of the individual.'

### (screen) (sc.hi_screen) — Does any of these apply to this health insurance?
Status: **MATCH**

Model: Screens the Pub. 974 premium tax credit case, Form 2555, S corporation, optional methods and retired public safety officer cases. It also screens long-term care entered for more than one business ('total... on line 2 of all Form(s) 7206 can't be more than the appropriate limit').

### 1 (sc.f7206_line1) — Health insurance payments (other than long-term care)
Status: **MATCH**

Model: Restates Form 7206 line 1 with its exclusions for subsidized-plan months and long-term care. It includes voluntarily paid Medicare premiums, which the instructions allow.

### 2 (sc.f7206_line2) — Qualified long-term care insurance (the smaller of payments or the age limit, for each per
Status: **MATCH**

Model: 'figure separately the amount to enter for each person. Then enter the total of those amounts'. The per-person age-limited amount (ltc.amount) is not shown here.

### 3 (sc.f7206_line3) — Add lines 1 and 2
Status: **MATCH**

Model: 'Add lines 1 and 2.'

### 4 (sc.f7206_line4) — Net profit from the trade or business under which the insurance plan is established
Status: **MATCH**

Model: 'Enter your net profit... from the trade or business under which the insurance plan is established.' Other earned income and optional methods are screened.

### 5 (sc.f7206_line5) — Total of all net profits from Schedule C, line 31
Status: **MATCH**

Model: 'Enter the total of all net profits from Schedule C... Don't include any net losses.' Schedule F and K-1 income are screened by the Schedule SE screen.

### 7 (sc.f7206_line7) — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax, by the p
Status: **UNCLEAR**

Restated: Choose — [helper "Line 4 is more than zero" = true → helper "Schedule 1, line 15 (this person's), times line 4 divided by line 5"] [helper "Line 4 is more than zero" = false → helper "Zero"]

Model: The form multiplies 'Schedule 1 (Form 1040), line 15' by line 6. The program uses this person's Schedule SE line 13. The given text does not say how to treat a joint return where both spouses owe self-employment tax.

Ruling: owner accepted (amb.2025.f7206_line15_person, T-041); restatement accepted. On a joint return Schedule 1 line 15 combines both spouses; Form 7206 is figured for the person whose business establishes the plan, and line 9 looks to 'the same trade or business', so the project uses that person's own Schedule SE line 13. The readings agree when only one spouse is self-employed.

### 8 (sc.f7206_line8) — Subtract line 7 from line 4
Status: **MATCH**

Model: 'Subtract line 7 from line 4'. The floor at zero cannot bind because line 7 is a fraction of line 4's share.

### 9 (sc.f7206_line9) — Schedule 1, line 16, attributable to the same trade or business
Status: **UNCLEAR**

Restated: Choose — [helper "Line 4 is more than zero" = true → helper "This person's SEP or SIMPLE deduction times line 4 divided by line 5"] [helper "Line 4 is more than zero" = false → helper "Zero"]

Model: The form asks for the Schedule 1 line 16 amount 'attributable to the same trade or business in which the insurance plan is established'. The program prorates by share of net profits, but the text gives no proration method.

Ruling: agent reading for the owner (amb.2025.f7206_plan_attribution, TASKS.md T-041); restatement accepted. The form gives no method for the part of Schedule 1 line 16 attributable to the business; the project prorates by the business's share of net profits, as Form 7206 lines 6 and 7 do for the self-employment tax.

### 10 (sc.f7206_line10) — Subtract line 9 from line 8
Status: **MATCH**

Model: 'Subtract line 9 from line 8.'

### 13 (sc.f7206_line13) — Subtract line 12 from line 10
Status: **MATCH**

Model: 'Subtract line 12 from line 10'. Line 12 (Form 2555) is zero because Form 2555 is screened.

### 14 (sc.f7206_line14) — Self-employed health insurance deduction
Status: **MATCH**

Model: 'Enter the smaller of line 3 or line 13'; zero when no plan is established under this business.

### 1(c) — Qualified business income or (loss) of this business
Status: **UNCLEAR**

Restated: Subtract helper "Deductions attributable to this business: self-employment tax, retirement plan and health insurance (Form 7206 for this business)" from helper "The amount for Schedule 1, line 3 and Schedule SE, line 2".

Model: Form 8995 QBI must account for the 'deductible part of self-employment tax, self-employment health insurance deduction, and contributions to qualified retirement plans' attributable to the business. The text gives no method for attributing the SE tax or plan deductions among businesses, so the profit-share proration cannot be verified.

Ruling: owner accepted (amb.2025.qbi_attribution, T-041); restatement accepted. i8995 p. 2 says QBI accounts for the deductible part of self-employment tax, the self-employment health insurance deduction and contributions to qualified retirement plans attributable to the business but gives no method; the project attributes them by the business's share of net profits (Form 7206 lines 7 and 9) and its own Form 7206 line 14.

### (screen) (sc.tips_ot) — Tips or overtime in this business to be deducted on Schedule 1-A
Status: **MATCH**

Model: Asks about qualified tips and qualified overtime reported on Form 1099-NEC or 1099-MISC, which 'is claimed on Schedule 1-A (Form 1040) not on your Schedule C.'

## Raw response

```yaml
```yaml
lines:
  - key: "(screen) (sc.statutory)"
    status: MATCH
    reason: "Matches the line 1 instruction: 'the \"Statutory employee\" box in box 13 of that form was checked.' The notary public case comes from the line 31 instructions. Both cases are refused through sc.screened."
  - key: "G"
    status: MATCH
    reason: "Follows the line G instruction: 'If your business activity is not a rental activity and you meet any of the material participation tests... or the exception for oil and gas applies, check the \"Yes\" box.' The examples paraphrase tests 1–3 correctly."
  - key: "(screen) (sc.spouse_owned)"
    status: MATCH
    reason: "Screens out the qualified joint venture, community property and partnership cases described under 'Business Owned and Operated by Spouses'. These are refused through sc.screened."
  - key: "F"
    status: MATCH
    reason: "Screens out 'any other method' and accounting method changes ('Form 3115', 'section 481(a) adjustment'). It also screens out uniform capitalization for businesses that are not small business taxpayers ('$31 million or less')."
  - key: "(screen) (sc.special)"
    status: MATCH
    reason: "Each listed item is a case the instructions send elsewhere: depletion, Form 7205, the credits that reduce lines 14/23/26, Form 8990, listed property recapture, chapter 11, Form 8873, installment election, Notice 2014-7, R&E, CCF and Form 2441. All are refused through sc.screened."
  - key: "1 (sc.line1)"
    status: MATCH
    reason: "Gross receipts including 'amounts properly shown on your Forms 1099-NEC' and other Forms 1099. Prizes and awards are correctly sent to line 6. The screened items are refused."
  - key: "2 (sc.line2)"
    status: MATCH
    reason: "'Report your sales returns and allowances as a positive number on line 2.'"
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
    reason: "Input of other business income. The examples are taken from the line 6 list (scrap sales, bad debts recovered, interest, fuel tax refunds, prizes and awards, Form 1099-PATR). The 481(a) and recapture items are screened."
  - key: "7 (sc.line7)"
    status: MATCH
    reason: "'Gross income. Add lines 5 and 6.'"
  - key: "8 (sc.line8)"
    status: MATCH
    reason: "Advertising expenses, entered as an input."
  - key: "9 (sc.line9)"
    status: MATCH
    reason: "Car and truck expenses are summed per vehicle, which fits 'Enter the total on line 9' for each vehicle's standard mileage or actual expenses. The per-vehicle amount (scveh.line9) is not shown here."
  - key: "10 (sc.line10)"
    status: MATCH
    reason: "'Do not include commissions or fees that are capitalized or deducted elsewhere on your return.'"
  - key: "11"
    status: MATCH
    reason: "Contract labor 'Do not include... contract labor includible on line 17, 21, 26, or 37.'"
  - key: "12 (sc.line12)"
    status: MATCH
    reason: "Depletion is set to zero. Any depletion is screened by sc.special and refused."
  - key: "13 (sc.line13)"
    status: MISMATCH
    reason: "Form 4562 line 22 totals 'line 12, lines 14 through 17, lines 19 and 20 in column (g), and line 21'. The helper takes only lines 14, 17, 19 (seven periods; no 25-year, residential or nonresidential real property) and 21. It omits line 15, line 16 ('Other depreciation (including ACRS)') and line 20 (ADS), and no refusal names these exclusions."
  - key: "14 (sc.line14)"
    status: MATCH
    reason: "Employee benefit programs, excluding 'contributions you made on your behalf' and pension plans on line 19. The Form 8941 reduction and self-employed dependent care contributions are screened."
  - key: "15"
    status: MATCH
    reason: "'Do not deduct amounts credited to a reserve for self-insurance or premiums paid for a policy that pays for your lost earnings.'"
  - key: "16a"
    status: MATCH
    reason: "Restates 'enter on line 16a the interest you paid for 2025 to banks or other financial institutions for which you received a Form 1098', excluding interest that must be capitalized."
  - key: "16b"
    status: MATCH
    reason: "Covers mortgage interest without a Form 1098 and other business interest. It excludes vehicle interest deducted on Schedule 1-A, as the caution requires."
  - key: "17"
    status: MATCH
    reason: "Fees of accountants and attorneys 'directly related to operating your business', including tax advice and preparation."
  - key: "18"
    status: MATCH
    reason: "'Include on this line your expenses for office supplies and postage.'"
  - key: "19"
    status: MATCH
    reason: "Contributions for employees. Self-employed contributions go on 'Schedule 1 (Form 1040), line 16, not on Schedule C.'"
  - key: "20a"
    status: MATCH
    reason: "'If you rented or leased vehicles, machinery, or equipment, enter on line 20a the business portion of your rental cost.' Vehicle leases come from the vehicle roster."
  - key: "20b"
    status: MATCH
    reason: "'Enter on line 20b amounts paid to rent or lease other property, such as office space.'"
  - key: "21"
    status: MATCH
    reason: "Follows the line 21 wording on incidental repairs, own labor, and restorations or replacements."
  - key: "22"
    status: MATCH
    reason: "Follows the line 22 instruction on materials consumed and used, and on incidental supplies purchased when no records of use are kept."
  - key: "23"
    status: MATCH
    reason: "Lists the deductible taxes and licenses and the excluded taxes from the line 23 instructions. The Form 8846 reduction is screened."
  - key: "24a"
    status: MATCH
    reason: "'Lodging and transportation connected with overnight travel... Do not include expenses for meals... Do not include entertainment.'"
  - key: "24b"
    status: MATCH
    reason: "Applies 50% generally, 80% for 'DOT hours of service limits', and full deduction for wage-treated and Form 1099-NEC meals. The text also refers to 'other exceptions' in Pub. 15."
  - key: "25"
    status: MATCH
    reason: "Business utilities only; 'do not deduct the base rate (including taxes) of the first phone line into your residence.'"
  - key: "26"
    status: MATCH
    reason: "Wages excluding 'amounts paid to yourself' and wages deducted elsewhere. Reductions for employment credits are screened."
  - key: "27a"
    status: MATCH
    reason: "Set to zero. The Form 7205 deduction is screened by sc.special."
  - key: "48"
    status: MATCH
    reason: "Part V: 'business expenses not included on lines 8-27a, or line 30'."
  - key: "27b"
    status: MATCH
    reason: "'Other expenses (from line 48).'"
  - key: "28"
    status: MATCH
    reason: "'Add lines 8 through 27b'; all of lines 8 through 27b are included."
  - key: "29"
    status: MATCH
    reason: "'Subtract line 28 from line 7.'"
  - key: "(screen) (sc.ho_uses)"
    status: MATCH
    reason: "Asks whether a business use of home deduction is claimed, using the instructions' description of qualifying use."
  - key: "(screen) (sc.ho_other)"
    status: MATCH
    reason: "Screens out the cases the simplified worksheet handles specially: Form 8829, more than one home, daycare, shared use, part-year use or area changes, income from another location, and Form 8949/4797 gains or losses. These are refused via sc.ho_screened."
  - key: "30(b)"
    status: MATCH
    reason: "The area 'used regularly and exclusively for business... or regularly for storage of inventory or product samples'. The multi-business allocation and special cases are refused."
  - key: "30(a)"
    status: MATCH
    reason: "'Enter the total square footage of (a) your home.'"
  - key: "3a"
    status: MATCH
    reason: "Worksheet line 3a 'Maximum allowable amount... $5'. Line 3b is 1.0 because daycare is screened."
  - key: "4 (sc.ho_line4)"
    status: MATCH
    reason: "Line 2 is 'the smaller of the square feet you actually used or 300', and line 4 is 'Multiply line 2 by line 3c'."
  - key: "1 (sc.ho_line1)"
    status: MATCH
    reason: "Gross income limitation line A is 'Schedule C, line 29'. Lines B and D (Form 8949/4797 items) are screened."
  - key: "5 (sc.ho_line5)"
    status: MATCH
    reason: "Gives 'the smaller of line 1 or line 4... If zero or less, enter -0-' in the supported cases. The interaction with the section 179 income limit is refused per Pub. 946 'Two different taxable income limits'."
  - key: "30"
    status: MATCH
    reason: "'Include the amount from line 5 of the Simplified Method Worksheet on line 30'; zero if no home office."
  - key: "31"
    status: MATCH
    reason: "'Net profit or (loss). Subtract line 30 from line 29.' Passive and at-risk limits are screened or refused."
  - key: "32"
    status: MATCH
    reason: "Box 32a/32b at-risk question, using the instruction's examples of amounts not at risk. A not-at-risk loss is refused for Form 6198."
  - key: "33"
    status: MATCH
    reason: "Combines line 33 'Other' and line 34 'any change... between opening and closing inventory'. Both are refused."
  - key: "35"
    status: MATCH
    reason: "'Inventory at beginning of year. If different from last year's closing inventory, attach explanation.' Changes are refused."
  - key: "36"
    status: MATCH
    reason: "'Purchases less cost of items withdrawn for personal use.'"
  - key: "37"
    status: MATCH
    reason: "'Cost of labor. Do not include any amounts paid to yourself.'"
  - key: "38"
    status: MATCH
    reason: "'Materials and supplies.'"
  - key: "39"
    status: MATCH
    reason: "'Other costs.'"
  - key: "40"
    status: MATCH
    reason: "'Add lines 35 through 39.'"
  - key: "41"
    status: MATCH
    reason: "'Inventory at end of year.'"
  - key: "42"
    status: MATCH
    reason: "'Cost of goods sold. Subtract line 41 from line 40.'"
  - key: "12 (sc.s179_allowed)"
    status: MATCH
    reason: "Uses this business's elected amounts when the deduction equals the elected total. Otherwise it uses Form 4562 line 12 for a single business. Allocation among businesses ('you may allocate your allowable section 179 expense deduction among them') is refused."
  - key: "(screen) (sc.hi_uses)"
    status: MATCH
    reason: "'The insurance plan must be established... under your business'; for Schedule C 'a policy can be either in the name of the business or in the name of the individual.'"
  - key: "(screen) (sc.hi_screen)"
    status: MATCH
    reason: "Screens the Pub. 974 premium tax credit case, Form 2555, S corporation, optional methods and retired public safety officer cases. It also screens long-term care entered for more than one business ('total... on line 2 of all Form(s) 7206 can't be more than the appropriate limit')."
  - key: "1 (sc.f7206_line1)"
    status: MATCH
    reason: "Restates Form 7206 line 1 with its exclusions for subsidized-plan months and long-term care. It includes voluntarily paid Medicare premiums, which the instructions allow."
  - key: "2 (sc.f7206_line2)"
    status: MATCH
    reason: "'figure separately the amount to enter for each person. Then enter the total of those amounts'. The per-person age-limited amount (ltc.amount) is not shown here."
  - key: "3 (sc.f7206_line3)"
    status: MATCH
    reason: "'Add lines 1 and 2.'"
  - key: "4 (sc.f7206_line4)"
    status: MATCH
    reason: "'Enter your net profit... from the trade or business under which the insurance plan is established.' Other earned income and optional methods are screened."
  - key: "5 (sc.f7206_line5)"
    status: MATCH
    reason: "'Enter the total of all net profits from Schedule C... Don't include any net losses.' Schedule F and K-1 income are screened by the Schedule SE screen."
  - key: "7 (sc.f7206_line7)"
    status: UNCLEAR
    reason: "The form multiplies 'Schedule 1 (Form 1040), line 15' by line 6. The program uses this person's Schedule SE line 13. The given text does not say how to treat a joint return where both spouses owe self-employment tax."
  - key: "8 (sc.f7206_line8)"
    status: MATCH
    reason: "'Subtract line 7 from line 4'. The floor at zero cannot bind because line 7 is a fraction of line 4's share."
  - key: "9 (sc.f7206_line9)"
    status: UNCLEAR
    reason: "The form asks for the Schedule 1 line 16 amount 'attributable to the same trade or business in which the insurance plan is established'. The program prorates by share of net profits, but the text gives no proration method."
  - key: "10 (sc.f7206_line10)"
    status: MATCH
    reason: "'Subtract line 9 from line 8.'"
  - key: "13 (sc.f7206_line13)"
    status: MATCH
    reason: "'Subtract line 12 from line 10'. Line 12 (Form 2555) is zero because Form 2555 is screened."
  - key: "14 (sc.f7206_line14)"
    status: MATCH
    reason: "'Enter the smaller of line 3 or line 13'; zero when no plan is established under this business."
  - key: "1(c)"
    status: UNCLEAR
    reason: "Form 8995 QBI must account for the 'deductible part of self-employment tax, self-employment health insurance deduction, and contributions to qualified retirement plans' attributable to the business. The text gives no method for attributing the SE tax or plan deductions among businesses, so the profit-share proration cannot be verified."
  - key: "(screen) (sc.tips_ot)"
    status: MATCH
    reason: "Asks about qualified tips and qualified overtime reported on Form 1099-NEC or 1099-MISC, which 'is claimed on Schedule 1-A (Form 1040) not on your Schedule C.'"
```
```
