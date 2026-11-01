# Render comparison — sc

The rendered English of every printed line of `Schedule C (Form 1040) — Profit or Loss From Business, one per business` (`rendered/2025/sc.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-01 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 4407ca3a38fca953c1d87062108df157f3514d6a231dbde5b3350aeacc25c167 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 5336eb4d57c28fe3dd4000438183d3f74e9cb1688b8accefbc1ad5426cdab84b |
| lines judged | 75 |
| match / mismatch / unclear / missing | 71 / 2 / 2 / 0 |
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

Model: This screen identifies statutory employee income (box 13 of Form W-2) and notary fees, both of which have special treatment under the line 1 and line 31 instructions. The refusal names the exclusion.

### G — Did you "materially participate" in the operation of this business during 2025, and is the
Status: **MATCH**

Model: It follows the line G instruction: not a rental activity and meets a material participation test, or the oil and gas exception applies. The hour-based tests are given as examples and the seven tests are referenced.

### (screen) (sc.spouse_owned) — Do you own this business together with your spouse (as a qualified joint venture, as commu
Status: **MATCH**

Model: This screen covers the spouse-owned cases described in the instructions (qualified joint venture, community property, partnership), and the refusal names them.

### F — Do you use an accounting method other than cash or accrual, or did you change your account
Status: **MATCH**

Model: The program uses line F as a screen for other accounting methods, method changes (Form 3115, section 481(a)) and uniform capitalization above the $31 million small business threshold, and refuses those cases. The tax shelter limb of the small business definition is not asked, but the rule stated is right for the supported cases.

### (screen) (sc.special) — For this business, do you have any of these: depletion (line 12); the energy efficient com
Status: **MATCH**

Model: The listed items correspond to special cases in the instructions, and the refusal excludes them. These include depletion, Form 7205, the employment credits, Form 8990, recapture and inclusion amounts, chapter 11, Form 8873, installment sales, Notice 2014-7, capitalized research costs, the capital construction fund and Form 2441 contributions.

### 1 (sc.line1) — Gross receipts or sales
Status: **MATCH**

Model: It matches 'Enter gross receipts from your trade or business', including amounts properly shown on Forms 1099-NEC and other Forms 1099. Prizes and awards go to line 6 as the instructions say, and screened cases are refused.

### 2 (sc.line2) — Returns and allowances
Status: **MATCH**

Model: The instructions say to report sales returns and allowances as a positive number, defined as refunds and reductions in selling price.

### 3 (sc.line3) — Subtract line 2 from line 1
Status: **MATCH**

Model: It matches 'Subtract line 2 from line 1'.

### 4 (sc.line4) — Cost of goods sold (from line 42)
Status: **MATCH**

Model: It matches 'Cost of goods sold (from line 42)'.

### 5 (sc.line5) — Gross profit. Subtract line 4 from line 3
Status: **MATCH**

Model: It matches 'Gross profit. Subtract line 4 from line 3'.

### 6 — Other income, including federal and state gasoline or fuel tax credit or refund
Status: **MATCH**

Model: The examples come from the line 6 list of business income not reported elsewhere in Part I, and the list is framed with 'such as'. The recapture and section 481(a) items are excluded by screens.

### 7 (sc.line7) — Gross income. Add lines 5 and 6
Status: **MATCH**

Model: It matches 'Gross income. Add lines 5 and 6'.

### 8 (sc.line8) — Advertising
Status: **MATCH**

Model: The input is the amount for the form's Advertising line.

### 9 (sc.line9) — Car and truck expenses
Status: **MATCH**

Model: Each vehicle uses either 70 cents per business mile plus parking and tolls, or the business portion of actual expenses plus parking and tolls, as the line 9 instructions state. Vehicles barred from the standard rate are refused.

### 10 (sc.line10) — Commissions and fees
Status: **MATCH**

Model: It matches the instruction to enter total commissions and fees, excluding those capitalized or deducted elsewhere.

### 11 — Contract labor
Status: **MATCH**

Model: It matches the contract labor instruction, including the exclusion of amounts on lines 17, 21, 26 or 37.

### 12 (sc.line12) — Depletion
Status: **MATCH**

Model: Line 12 is depletion. The program enters zero and refuses any depletion through the special-items screen.

### 13 (sc.line13) — Depreciation and section 179 expense deduction (not included in Part III)
Status: **MATCH**

Model: The restated sum is Form 4562 line 12 plus lines 14, 17, 19 and 21 (through line 28), which is the depreciation and section 179 total for line 13, with other categories screened out. Any error in its section 179 component is reported on '12 (sc.s179_allowed)'.

### 14 (sc.line14) — Employee benefit programs (other than on line 19)
Status: **MATCH**

Model: It matches the line 14 instruction on employee benefit programs, excluding pension plans and contributions for yourself. Form 8941 reductions and self-employed dependent care are screened.

### 15 — Insurance (other than health)
Status: **MATCH**

Model: It follows the form's 'Insurance (other than health)' and the exclusions for self-insurance reserves and lost-earnings policies. The wording excludes only health insurance for yourself, but line 14's prompt directs employee accident and health plans to that line, as the instructions require.

### 16a — Interest: mortgage (paid to banks, etc.)
Status: **MATCH**

Model: It matches 'the interest you paid for 2025 to banks or other financial institutions for which you received a Form 1098', excluding capitalized interest. Form 8990 limits are screened.

### 16b — Interest: other
Status: **MATCH**

Model: It covers other interest, including mortgage interest with no Form 1098 received. It also applies the caution against deducting vehicle interest claimed on Schedule 1-A.

### 17 — Legal and professional services
Status: **MATCH**

Model: It matches the line 17 instruction on accountant and attorney fees directly related to operating the business, including tax advice and business tax form preparation.

### 18 — Office expense
Status: **MATCH**

Model: It matches 'your expenses for office supplies and postage'.

### 19 — Pension and profit-sharing plans
Status: **MATCH**

Model: It matches the instruction on contributions for employees to pension, profit-sharing or annuity plans, with contributions for yourself going to Schedule 1, line 16.

### 20a — Rent or lease: vehicles, machinery, and equipment
Status: **MATCH**

Model: It enters the business portion of rent for vehicles, machinery and equipment. Leased vehicles on actual expenses use the business-mile share, and inclusion amounts are screened.

### 20b — Rent or lease: other business property
Status: **MATCH**

Model: It matches 'amounts paid to rent or lease other property, such as office space'.

### 21 — Repairs and maintenance
Status: **MATCH**

Model: It matches the line 21 instruction, including the exclusions for your own labor and for restorations or replacements.

### 22 — Supplies (not included in Part III)
Status: **MATCH**

Model: It matches the line 22 rule: materials and supplies consumed and used, or incidental supplies purchased when no inventories or records of use are kept.

### 23 — Taxes and licenses
Status: **MATCH**

Model: The included and excluded taxes follow the line 23 lists. The Form 8846 reduction is screened.

### 24a — Travel
Status: **MATCH**

Model: It matches 'expenses for lodging and transportation connected with overnight travel for business while away from your tax home', excluding meals and entertainment.

### 24b — Deductible meals
Status: **UNCLEAR**

Restated: Add helper "50% of the meals subject to the 50% limit", helper "80% of the meals under the hours of service limits", and helper "Meals and incidentals not subject to the 50% limit, deducted in full".

Model: The 50% and 80% rates and the first two full-deduction categories match 'Amount of deduction'. The text only points to Pub. 15 and Pub. 334 for 'other exceptions', so the customer-reimbursed, employee-recreation, public-promotion and sold-to-public categories need those missing sources.

Ruling: owner ruling (T-042; amb.2025.meals_full_exceptions); restatement accepted. The 50% and 80% rates and the two full-deduction cases match i1040sc p. 10 as the model says. The other categories come from Pub. 463 (2025) p. 16, Exception to the 50% Limit for Meals, which the instruction reaches through 'See chapter 5 of Pub. 15 ... for details and other exceptions. See also chapter 8 of Pub. 334': Pub. 15 chapter 5 lists no exceptions and Pub. 334 refers to Pub. 463. The model was given the i1040sc pages only, so it could not see that list.

### 25 — Utilities
Status: **MATCH**

Model: It matches the line 25 instruction on business utilities and the bar on deducting the base rate of the first residential phone line.

### 26 — Wages (less employment credits)
Status: **MATCH**

Model: It enters salaries and wages, excluding amounts paid to yourself or deducted elsewhere. Employment credit reductions are refused through the screen.

### 27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **MATCH**

Model: Line 27a is the Form 7205 deduction. The program enters zero and refuses Form 7205 cases through the screen.

### 48 — Total other expenses
Status: **MATCH**

Model: It matches Part V, 'business expenses not included on lines 8-27a, or line 30', and the line 48 total.

### 27b — Other expenses (from line 48)
Status: **MATCH**

Model: It matches 'Other expenses (from line 48)'.

### 28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **MATCH**

Model: It adds every expense line from 8 through 27b, as the form directs.

### 29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **MATCH**

Model: It matches 'Tentative profit or (loss). Subtract line 28 from line 7'.

### (screen) (sc.ho_uses) — Do you claim a deduction for business use of your home for this business?
Status: **MATCH**

Model: It asks about the qualifying uses in the simplified method text. Daycare use is handled by the separate screen.

### (screen) (sc.ho_other) — Does any of these apply to your business use of your home for this business?
Status: **MATCH**

Model: It screens the actual-expense method and the special cases in the line 30 and worksheet instructions (multiple homes, daycare, shared space, part-year or changed area, income from elsewhere, Form 8949 or 4797 items).

### 30(b) — The part of your home used for business (square feet)
Status: **MATCH**

Model: It matches the form's 'the part of your home used for business' and the qualifying-use test. The refusals name the multi-business allocation and the special simplified-method cases.

### 30(a) — Total square footage of your home
Status: **MATCH**

Model: It matches the form's 'total square footage of (a) your home'.

### 3a — Maximum allowable amount (per square foot)
Status: **MATCH**

Model: The worksheet prints $5 on line 3a.

### 4 (sc.ho_line4) — Multiply line 2 by line 3c
Status: **MATCH**

Model: It computes line 2 (the smaller of square feet used or 300) times line 3c. With daycare screened out, line 3b is 1.0, so line 3c equals $5.

### 1 (sc.ho_line1) — Gross income limitation (Schedule C, line 29)
Status: **MATCH**

Model: With gains, losses and income from other locations screened out, worksheet line 1 reduces to 'the amount from Schedule C, line 29'.

### 5 (sc.ho_line5) — Allowable expenses using the simplified method. Enter the smaller of line 1 or line 4
Status: **MATCH**

Model: It gives the smaller of line 1 or line 4, floored at zero, when that result is determinable. Cases needing the Pub. 946 'Two different taxable income limits' procedure are refused and named.

### 30 — Expenses for business use of your home
Status: **MATCH**

Model: It enters worksheet line 5 when the deduction is claimed, as the instructions direct, and zero otherwise.

### 31 — Net profit or (loss). Subtract line 30 from line 29
Status: **MATCH**

Model: It matches 'Net profit or (loss). Subtract line 30 from line 29'. At-risk losses are refused, and passive cases are screened through line G.

### 32 — If you have a loss, is all your investment in this business at risk (box 32a)?
Status: **MISMATCH**

Restated: Input — All your investment in this business is at risk: you have no nonrecourse loans not secured by your own property, no amounts protected against loss by a guarantee or stop-loss agreement, and no amounts borrowed from someone with an interest in the business (box 32a)

Model: The box 32b test omits part of the IRS condition: amounts borrowed 'from a person who has an interest in the business other than as a creditor or who is related under section 465(b)(3)(C) to a person (other than you) having such an interest'. A related-party loan would pass as at risk, while an ordinary creditor could be read as disqualifying.

Ruling: finding — i1040sc p. 15, Line 32, Some investment is not at risk: "Amounts borrowed for use in the business from a person who has an interest in the business other than as a creditor or who is related under section 465(b)(3)(C) to a person (other than you) having such an interest." The box 32a question names a lender with an interest in the business but omits the related-party prong, so a related-party loan can answer Yes and deduct a loss the at-risk rules would limit. BUG-0290; fix the question with the Schedule C form pass (T-157).

### 33 — Method used to value closing inventory: other than cost or lower of cost or market, or a c
Status: **MATCH**

Model: It combines the line 33 'Other' method and the line 34 change question into a screen, and refuses those cases.

### 35 — Inventory at beginning of year
Status: **MATCH**

Model: It matches 'Inventory at beginning of year', with accounting method changes screened. The form's case of an opening amount different from last year's closing inventory is not separately provided for.

### 36 — Purchases less cost of items withdrawn for personal use
Status: **MATCH**

Model: It matches 'Purchases less cost of items withdrawn for personal use'.

### 37 — Cost of labor
Status: **MATCH**

Model: It matches 'Cost of labor. Do not include any amounts paid to yourself'.

### 38 — Materials and supplies
Status: **MATCH**

Model: It matches the form's 'Materials and supplies' line within cost of goods sold.

### 39 — Other costs
Status: **MATCH**

Model: It matches the form's 'Other costs' line.

### 40 — Add lines 35 through 39
Status: **MATCH**

Model: It matches 'Add lines 35 through 39'.

### 41 — Inventory at end of year
Status: **MATCH**

Model: It matches 'Inventory at end of year'.

### 42 — Cost of goods sold. Subtract line 41 from line 40
Status: **MATCH**

Model: It matches 'Subtract line 41 from line 40'.

### 12 (sc.s179_allowed) — Section 179 expense deduction for this business
Status: **MISMATCH**

Restated: Choose — [s179 helper "The deduction differs from the amounts elected for 2025" = false → helper "Section 179 elected for this business's 2025 property"] [s179 helper "The deduction differs from the amounts elected for 2025" = true → helper "The return's section 179 deduction, for its only Schedule C"]

Model: The program sets Form 4562 line 1 to a flat $2,500,000, but Worksheet 1 says 'Enter the smaller of line 1 or line 2' and 'Enter the amount from line 3 here and on Form 4562, line 1'. When 2025 section 179 cost is below $2,500,000, this overstates lines 5 and 11, so a carryover can raise the line 12 deduction and Schedule C line 13 too much.

Ruling: ambiguity — T-043 / amb.2025.s179_carryover_no_property (owner adopted): s179.line1 is the $2,500,000 limitation, not the smaller of the limitation and the 2025 cost, on the line 1 instruction's reading. Worksheet 1's "Enter the smaller of line 1 or line 2" is the recorded competing reading; the project keeps the owner's adopted line 1. The render complaint repeats it.

### (screen) (sc.hi_uses) — Health insurance established under this business
Status: **MATCH**

Model: It matches the Form 7206 instructions on coverage established under the business, a policy in the business's or individual's name, and covered persons including a child under 27.

### (screen) (sc.hi_screen) — Does any of these apply to this health insurance?
Status: **MATCH**

Model: It screens the Marketplace and premium tax credit case, Form 2555, S corporation status, optional methods, public safety officer payments and multi-business long-term care limits. All of these appear in the instructions and are refused.

### 1 (sc.f7206_line1) — Health insurance payments (other than long-term care)
Status: **MATCH**

Model: It matches Form 7206 line 1 and its exclusions for subsidized-plan months and long-term care, and includes voluntary Medicare premiums as the instructions allow. The public safety officer exclusion is screened.

### 2 (sc.f7206_line2) — Qualified long-term care insurance (the smaller of payments or the age limit, for each per
Status: **MATCH**

Model: It totals, per person, the smaller of payments or the age-based amount, as line 2 directs.

### 3 (sc.f7206_line3) — Add lines 1 and 2
Status: **MATCH**

Model: It matches 'Add lines 1 and 2'.

### 4 (sc.f7206_line4) — Net profit from the trade or business under which the insurance plan is established
Status: **MATCH**

Model: It enters this business's net profit, with zero for a loss. Other earned income and optional methods are outside the supported cases.

### 5 (sc.f7206_line5) — Total of all net profits from Schedule C, line 31
Status: **MATCH**

Model: It totals net profits and excludes net losses, as line 5 directs, with the other income types screened out. The limit to this person's businesses is addressed under line 7.

### 7 (sc.f7206_line7) — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax, by the p
Status: **UNCLEAR**

Restated: Choose — [helper "Line 4 is more than zero" = true → helper "Schedule 1, line 15 (this person's), times line 4 divided by line 5"] [helper "Line 4 is more than zero" = false → helper "Zero"]

Model: Form 7206 says to multiply 'Schedule 1 (Form 1040), line 15' by line 6, while the program uses only this person's Schedule SE line 13 and this person's profits. The text does not say how to apply lines 5 and 7 on a joint return where both spouses have self-employment income; the computation is otherwise right.

Ruling: owner accepted (amb.2025.f7206_line15_person, T-041); restatement accepted. On a joint return Schedule 1 line 15 combines both spouses; Form 7206 is figured for the person whose business establishes the plan, and line 9 looks to 'the same trade or business', so the project uses that person's own Schedule SE line 13. The readings agree when only one spouse is self-employed.

### 8 (sc.f7206_line8) — Subtract line 7 from line 4
Status: **MATCH**

Model: It matches 'Subtract line 7 from line 4'. The zero floor only prevents a negative deduction base.

### 9 (sc.f7206_line9) — Schedule 1, line 16, attributable to the same trade or business
Status: **MATCH**

Model: Line 9 asks for the Schedule 1, line 16 amount attributable to this business. Plans with more than one Schedule C are refused, so the program's ratio assigns the whole deduction to the single profitable business.

### 10 (sc.f7206_line10) — Subtract line 9 from line 8
Status: **MATCH**

Model: It matches 'Subtract line 9 from line 8'. The zero floor only prevents a negative deduction base.

### 13 (sc.f7206_line13) — Subtract line 12 from line 10
Status: **MATCH**

Model: Form 2555 and S corporation cases are screened, so line 12 is zero and 'Subtract line 12 from line 10' equals line 10.

### 14 (sc.f7206_line14) — Self-employed health insurance deduction
Status: **MATCH**

Model: It matches 'Enter the smaller of line 3 or line 13', and is zero when no insurance is established under this business.

### 1(c) — Qualified business income or (loss) of this business
Status: **MATCH**

Model: It reduces Schedule C profit or loss by the items Form 8995's instructions name: the deductible part of self-employment tax, self-employed health insurance and retirement plan contributions. Allocating these by share of net profits is consistent with counting items attributable to the business.

### (screen) (sc.tips_ot) — Tips or overtime in this business to be deducted on Schedule 1-A
Status: **MATCH**

Model: It identifies qualified tips and qualified overtime reported on Form 1099-NEC or 1099-MISC, which the instructions say are deducted on Schedule 1-A rather than on Schedule C.

## Raw response

```yaml
```yaml
lines:
  - key: "(screen) (sc.statutory)"
    status: MATCH
    reason: "This screen identifies statutory employee income (box 13 of Form W-2) and notary fees, both of which have special treatment under the line 1 and line 31 instructions. The refusal names the exclusion."
  - key: "G"
    status: MATCH
    reason: "It follows the line G instruction: not a rental activity and meets a material participation test, or the oil and gas exception applies. The hour-based tests are given as examples and the seven tests are referenced."
  - key: "(screen) (sc.spouse_owned)"
    status: MATCH
    reason: "This screen covers the spouse-owned cases described in the instructions (qualified joint venture, community property, partnership), and the refusal names them."
  - key: "F"
    status: MATCH
    reason: "The program uses line F as a screen for other accounting methods, method changes (Form 3115, section 481(a)) and uniform capitalization above the $31 million small business threshold, and refuses those cases. The tax shelter limb of the small business definition is not asked, but the rule stated is right for the supported cases."
  - key: "(screen) (sc.special)"
    status: MATCH
    reason: "The listed items correspond to special cases in the instructions, and the refusal excludes them. These include depletion, Form 7205, the employment credits, Form 8990, recapture and inclusion amounts, chapter 11, Form 8873, installment sales, Notice 2014-7, capitalized research costs, the capital construction fund and Form 2441 contributions."
  - key: "1 (sc.line1)"
    status: MATCH
    reason: "It matches 'Enter gross receipts from your trade or business', including amounts properly shown on Forms 1099-NEC and other Forms 1099. Prizes and awards go to line 6 as the instructions say, and screened cases are refused."
  - key: "2 (sc.line2)"
    status: MATCH
    reason: "The instructions say to report sales returns and allowances as a positive number, defined as refunds and reductions in selling price."
  - key: "3 (sc.line3)"
    status: MATCH
    reason: "It matches 'Subtract line 2 from line 1'."
  - key: "4 (sc.line4)"
    status: MATCH
    reason: "It matches 'Cost of goods sold (from line 42)'."
  - key: "5 (sc.line5)"
    status: MATCH
    reason: "It matches 'Gross profit. Subtract line 4 from line 3'."
  - key: "6"
    status: MATCH
    reason: "The examples come from the line 6 list of business income not reported elsewhere in Part I, and the list is framed with 'such as'. The recapture and section 481(a) items are excluded by screens."
  - key: "7 (sc.line7)"
    status: MATCH
    reason: "It matches 'Gross income. Add lines 5 and 6'."
  - key: "8 (sc.line8)"
    status: MATCH
    reason: "The input is the amount for the form's Advertising line."
  - key: "9 (sc.line9)"
    status: MATCH
    reason: "Each vehicle uses either 70 cents per business mile plus parking and tolls, or the business portion of actual expenses plus parking and tolls, as the line 9 instructions state. Vehicles barred from the standard rate are refused."
  - key: "10 (sc.line10)"
    status: MATCH
    reason: "It matches the instruction to enter total commissions and fees, excluding those capitalized or deducted elsewhere."
  - key: "11"
    status: MATCH
    reason: "It matches the contract labor instruction, including the exclusion of amounts on lines 17, 21, 26 or 37."
  - key: "12 (sc.line12)"
    status: MATCH
    reason: "Line 12 is depletion. The program enters zero and refuses any depletion through the special-items screen."
  - key: "13 (sc.line13)"
    status: MATCH
    reason: "The restated sum is Form 4562 line 12 plus lines 14, 17, 19 and 21 (through line 28), which is the depreciation and section 179 total for line 13, with other categories screened out. Any error in its section 179 component is reported on '12 (sc.s179_allowed)'."
  - key: "14 (sc.line14)"
    status: MATCH
    reason: "It matches the line 14 instruction on employee benefit programs, excluding pension plans and contributions for yourself. Form 8941 reductions and self-employed dependent care are screened."
  - key: "15"
    status: MATCH
    reason: "It follows the form's 'Insurance (other than health)' and the exclusions for self-insurance reserves and lost-earnings policies. The wording excludes only health insurance for yourself, but line 14's prompt directs employee accident and health plans to that line, as the instructions require."
  - key: "16a"
    status: MATCH
    reason: "It matches 'the interest you paid for 2025 to banks or other financial institutions for which you received a Form 1098', excluding capitalized interest. Form 8990 limits are screened."
  - key: "16b"
    status: MATCH
    reason: "It covers other interest, including mortgage interest with no Form 1098 received. It also applies the caution against deducting vehicle interest claimed on Schedule 1-A."
  - key: "17"
    status: MATCH
    reason: "It matches the line 17 instruction on accountant and attorney fees directly related to operating the business, including tax advice and business tax form preparation."
  - key: "18"
    status: MATCH
    reason: "It matches 'your expenses for office supplies and postage'."
  - key: "19"
    status: MATCH
    reason: "It matches the instruction on contributions for employees to pension, profit-sharing or annuity plans, with contributions for yourself going to Schedule 1, line 16."
  - key: "20a"
    status: MATCH
    reason: "It enters the business portion of rent for vehicles, machinery and equipment. Leased vehicles on actual expenses use the business-mile share, and inclusion amounts are screened."
  - key: "20b"
    status: MATCH
    reason: "It matches 'amounts paid to rent or lease other property, such as office space'."
  - key: "21"
    status: MATCH
    reason: "It matches the line 21 instruction, including the exclusions for your own labor and for restorations or replacements."
  - key: "22"
    status: MATCH
    reason: "It matches the line 22 rule: materials and supplies consumed and used, or incidental supplies purchased when no inventories or records of use are kept."
  - key: "23"
    status: MATCH
    reason: "The included and excluded taxes follow the line 23 lists. The Form 8846 reduction is screened."
  - key: "24a"
    status: MATCH
    reason: "It matches 'expenses for lodging and transportation connected with overnight travel for business while away from your tax home', excluding meals and entertainment."
  - key: "24b"
    status: UNCLEAR
    reason: "The 50% and 80% rates and the first two full-deduction categories match 'Amount of deduction'. The text only points to Pub. 15 and Pub. 334 for 'other exceptions', so the customer-reimbursed, employee-recreation, public-promotion and sold-to-public categories need those missing sources."
  - key: "25"
    status: MATCH
    reason: "It matches the line 25 instruction on business utilities and the bar on deducting the base rate of the first residential phone line."
  - key: "26"
    status: MATCH
    reason: "It enters salaries and wages, excluding amounts paid to yourself or deducted elsewhere. Employment credit reductions are refused through the screen."
  - key: "27a"
    status: MATCH
    reason: "Line 27a is the Form 7205 deduction. The program enters zero and refuses Form 7205 cases through the screen."
  - key: "48"
    status: MATCH
    reason: "It matches Part V, 'business expenses not included on lines 8-27a, or line 30', and the line 48 total."
  - key: "27b"
    status: MATCH
    reason: "It matches 'Other expenses (from line 48)'."
  - key: "28"
    status: MATCH
    reason: "It adds every expense line from 8 through 27b, as the form directs."
  - key: "29"
    status: MATCH
    reason: "It matches 'Tentative profit or (loss). Subtract line 28 from line 7'."
  - key: "(screen) (sc.ho_uses)"
    status: MATCH
    reason: "It asks about the qualifying uses in the simplified method text. Daycare use is handled by the separate screen."
  - key: "(screen) (sc.ho_other)"
    status: MATCH
    reason: "It screens the actual-expense method and the special cases in the line 30 and worksheet instructions (multiple homes, daycare, shared space, part-year or changed area, income from elsewhere, Form 8949 or 4797 items)."
  - key: "30(b)"
    status: MATCH
    reason: "It matches the form's 'the part of your home used for business' and the qualifying-use test. The refusals name the multi-business allocation and the special simplified-method cases."
  - key: "30(a)"
    status: MATCH
    reason: "It matches the form's 'total square footage of (a) your home'."
  - key: "3a"
    status: MATCH
    reason: "The worksheet prints $5 on line 3a."
  - key: "4 (sc.ho_line4)"
    status: MATCH
    reason: "It computes line 2 (the smaller of square feet used or 300) times line 3c. With daycare screened out, line 3b is 1.0, so line 3c equals $5."
  - key: "1 (sc.ho_line1)"
    status: MATCH
    reason: "With gains, losses and income from other locations screened out, worksheet line 1 reduces to 'the amount from Schedule C, line 29'."
  - key: "5 (sc.ho_line5)"
    status: MATCH
    reason: "It gives the smaller of line 1 or line 4, floored at zero, when that result is determinable. Cases needing the Pub. 946 'Two different taxable income limits' procedure are refused and named."
  - key: "30"
    status: MATCH
    reason: "It enters worksheet line 5 when the deduction is claimed, as the instructions direct, and zero otherwise."
  - key: "31"
    status: MATCH
    reason: "It matches 'Net profit or (loss). Subtract line 30 from line 29'. At-risk losses are refused, and passive cases are screened through line G."
  - key: "32"
    status: MISMATCH
    reason: "The box 32b test omits part of the IRS condition: amounts borrowed 'from a person who has an interest in the business other than as a creditor or who is related under section 465(b)(3)(C) to a person (other than you) having such an interest'. A related-party loan would pass as at risk, while an ordinary creditor could be read as disqualifying."
  - key: "33"
    status: MATCH
    reason: "It combines the line 33 'Other' method and the line 34 change question into a screen, and refuses those cases."
  - key: "35"
    status: MATCH
    reason: "It matches 'Inventory at beginning of year', with accounting method changes screened. The form's case of an opening amount different from last year's closing inventory is not separately provided for."
  - key: "36"
    status: MATCH
    reason: "It matches 'Purchases less cost of items withdrawn for personal use'."
  - key: "37"
    status: MATCH
    reason: "It matches 'Cost of labor. Do not include any amounts paid to yourself'."
  - key: "38"
    status: MATCH
    reason: "It matches the form's 'Materials and supplies' line within cost of goods sold."
  - key: "39"
    status: MATCH
    reason: "It matches the form's 'Other costs' line."
  - key: "40"
    status: MATCH
    reason: "It matches 'Add lines 35 through 39'."
  - key: "41"
    status: MATCH
    reason: "It matches 'Inventory at end of year'."
  - key: "42"
    status: MATCH
    reason: "It matches 'Subtract line 41 from line 40'."
  - key: "12 (sc.s179_allowed)"
    status: MISMATCH
    reason: "The program sets Form 4562 line 1 to a flat $2,500,000, but Worksheet 1 says 'Enter the smaller of line 1 or line 2' and 'Enter the amount from line 3 here and on Form 4562, line 1'. When 2025 section 179 cost is below $2,500,000, this overstates lines 5 and 11, so a carryover can raise the line 12 deduction and Schedule C line 13 too much."
  - key: "(screen) (sc.hi_uses)"
    status: MATCH
    reason: "It matches the Form 7206 instructions on coverage established under the business, a policy in the business's or individual's name, and covered persons including a child under 27."
  - key: "(screen) (sc.hi_screen)"
    status: MATCH
    reason: "It screens the Marketplace and premium tax credit case, Form 2555, S corporation status, optional methods, public safety officer payments and multi-business long-term care limits. All of these appear in the instructions and are refused."
  - key: "1 (sc.f7206_line1)"
    status: MATCH
    reason: "It matches Form 7206 line 1 and its exclusions for subsidized-plan months and long-term care, and includes voluntary Medicare premiums as the instructions allow. The public safety officer exclusion is screened."
  - key: "2 (sc.f7206_line2)"
    status: MATCH
    reason: "It totals, per person, the smaller of payments or the age-based amount, as line 2 directs."
  - key: "3 (sc.f7206_line3)"
    status: MATCH
    reason: "It matches 'Add lines 1 and 2'."
  - key: "4 (sc.f7206_line4)"
    status: MATCH
    reason: "It enters this business's net profit, with zero for a loss. Other earned income and optional methods are outside the supported cases."
  - key: "5 (sc.f7206_line5)"
    status: MATCH
    reason: "It totals net profits and excludes net losses, as line 5 directs, with the other income types screened out. The limit to this person's businesses is addressed under line 7."
  - key: "7 (sc.f7206_line7)"
    status: UNCLEAR
    reason: "Form 7206 says to multiply 'Schedule 1 (Form 1040), line 15' by line 6, while the program uses only this person's Schedule SE line 13 and this person's profits. The text does not say how to apply lines 5 and 7 on a joint return where both spouses have self-employment income; the computation is otherwise right."
  - key: "8 (sc.f7206_line8)"
    status: MATCH
    reason: "It matches 'Subtract line 7 from line 4'. The zero floor only prevents a negative deduction base."
  - key: "9 (sc.f7206_line9)"
    status: MATCH
    reason: "Line 9 asks for the Schedule 1, line 16 amount attributable to this business. Plans with more than one Schedule C are refused, so the program's ratio assigns the whole deduction to the single profitable business."
  - key: "10 (sc.f7206_line10)"
    status: MATCH
    reason: "It matches 'Subtract line 9 from line 8'. The zero floor only prevents a negative deduction base."
  - key: "13 (sc.f7206_line13)"
    status: MATCH
    reason: "Form 2555 and S corporation cases are screened, so line 12 is zero and 'Subtract line 12 from line 10' equals line 10."
  - key: "14 (sc.f7206_line14)"
    status: MATCH
    reason: "It matches 'Enter the smaller of line 3 or line 13', and is zero when no insurance is established under this business."
  - key: "1(c)"
    status: MATCH
    reason: "It reduces Schedule C profit or loss by the items Form 8995's instructions name: the deductible part of self-employment tax, self-employed health insurance and retirement plan contributions. Allocating these by share of net profits is consistent with counting items attributable to the business."
  - key: "(screen) (sc.tips_ot)"
    status: MATCH
    reason: "It identifies qualified tips and qualified overtime reported on Form 1099-NEC or 1099-MISC, which the instructions say are deducted on Schedule 1-A rather than on Schedule C."
```
```
