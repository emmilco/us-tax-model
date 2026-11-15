# Walk: 08_hsa_marketplace

A single person, 34, who bought Marketplace health insurance for January to April (a Form 1095-A), then started a job with a high-deductible health plan and a health savings account.

Written by `node engine/dist/main.js draft-walk` from `interview/2025/personas/08_hsa_marketplace.yaml`: the built interview (profile `full`, the federal questions, 2025) in its own asking order. Each prompt is as the page shows it to this filer. An answer marked *persona* is the persona's own; *background* is the answer a filer with nothing to report gives. A topic is the form the question's input belongs to; **⟶ topic switch** marks a question whose topic differs from the one before it (**returns** when the walk had already left that topic). Words are counted as `interview-words` counts them. Help is shown and optional to read: only its length and first sentence are given.

## The walk

### 1. `$person`

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`)

> Who is this tax return for?

- Offered: “Just me” / “Me and my husband or wife, together on one return”
- Answer: “Just me” (persona)
- Words: prompt 6, help 51. Help begins: “Choose “together” if you are married and the two of you are filing one return, even if only one of you had income.”

### 2. `f1040.status`

**⟶ topic switch**

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`), Filing Status

> Which of these fits you on December 31, 2025?

- Offered: “Married, and filing apart from my husband or wife (married filing separately)” / “Widowed in 2023 or 2024, not remarried, and my child lived with me all of 2025 (qualifying surviving spouse)” / “I paid over half the cost of the home of my child, or of a relative I support (head of household)” / “None of these: I was not married (single)”
- Answer: “None of these: I was not married (single)” (`single`) (persona)
- Words: prompt 9, help 115. Help begins: “Take the first line that is true for you, with one exception: if you are married but lived apart from your husband or wife for the last six months of 2025 and your child lived with you, look at the line about paying for a home before the first line.”

### 3. `scope.other_line16`

**⟶ topic switch**

Topic: Proof-of-concept scope screening (`scope`)

> Any additional Form 1040 line 16 tax or filing, including any of the following?
>
> A child's unearned income:
> - filing Form 8814 (even with no tax)
> - Form 8615, required if all of these apply:
>   - you had more than $2,700 of unearned income
>   - you are required to file
>   - you do not file jointly
>   - you have a parent who was alive at the end of 2025
>   - you were under 18 at the end of 2025, or 18 with earned income of not more than half your support, or a full-time student 19 to 23 with earned income of not more than half your support
>
> Foreign corporations:
> - a section 962 election
> - Form 8621
> - stock you own, directly or indirectly, in a controlled foreign corporation (CFC) or a passive foreign investment company (PFIC), even with nothing to include in income for 2025 (its distributions, dispositions and related adjustments can make the modified AGI of Form 8960 line 13 differ from AGI)
>
> Other:
> - Form 4972
> - a Form 8978 amount
> - recapture of an education credit
> - income averaging of farming or fishing income on Schedule J (if you choose it)

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 182, help 32. Help begins: “Yes if any tax or filing the question names applies to you, including Schedule J income averaging you choose and stock you own in a CFC or PFIC; Yes refuses the return.”

### 4. `scope.schedule1`

Topic: Proof-of-concept scope screening (`scope`)

> Any income or adjustment requiring Schedule 1 other than the ones this tool asks about separately, including any of the following?
>
> Income:
> - statutory-employee wages or income as a minister, a member of a religious order who has not taken a vow of poverty, or a Christian Science practitioner
> - church employee income (wages from a church or qualified church-controlled organization that elected exemption from social security and Medicare taxes)
> - a refund or other recovery of an amount you deducted or took a credit for in an earlier year, other than a state or local income tax refund, for example:
>   - a refund of general sales tax, real estate tax or personal property tax
>   - a refund of mortgage interest in box 4 of Form 1098
>   - a reimbursement of medical expenses
>   - a payment on a bad debt you deducted
> - sales of business property (Form 4797)
> - a net operating loss deduction
> - rental real estate, royalties, partnerships, S corporations, estates or trusts (Schedule E or a Schedule K-1)
> - rental of personal property
> - farm income (Schedule F)
> - an exclusion of Medicaid waiver payments (Schedule 1 line 8s)
>
> Adjustments:
> - other qualified retirement plans for the self-employed (such as a solo 401(k) or other Keogh plan)
> - an adjustment on Schedule 1 line 12, 14 or 23
>
> The ones this tool asks about separately:
> - business income or loss from Schedule C
> - a taxable state or local income tax refund
> - alimony under an agreement made before 2019
> - unemployment compensation
> - the line 8 items asked one by one
> - educator expenses
> - the HSA deduction
> - the deductible part of self-employment tax
> - self-employed SEP and SIMPLE contributions
> - the self-employed health insurance deduction
> - the penalty on early withdrawal of savings
> - the IRA deduction
> - student loan interest
> - jury duty pay you gave your employer
>
> Schedule 1-A deductions are asked separately.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 293, help 33. Help begins: “Yes if you have any Schedule 1 income or adjustment other than the items in the parentheses, which this tool asks about elsewhere, including the kinds the question names; Yes refuses the return.”

### 5. `scope.other_income`

Topic: Proof-of-concept scope screening (`scope`)

> Any nonresident alien status, or other income or return treatment outside the kinds listed below?
>
> Kinds this question is not about:
> - wages
> - interest
> - dividends
> - supported securities sales
> - Form 1099-R distributions
> - social security benefits
>
> Nonresident alien status:
> - you or your spouse, for any part of 2025
>
> Other income or return treatment, including:
> - wages or tips not on a Form W-2
> - Medicaid waiver payments (whether or not in Form W-2 box 1)
> - adoption benefits
> - dependent care benefits other than those shown in box 10 of a Form W-2 (or a grace-period amount from such a plan)
> - other earned income (Form 1040 lines 1b to 1d and 1f to 1h)
> - income or loss from a passive activity (including gain on selling an interest in one)
> - the 2025 part of a qualified disaster recovery distribution you received in 2023 or 2024, or a 2025 repayment of one (Form 8915-F)
> - a repayment to an IRA of a qualified reservist distribution (Form 8606 line 1)
> - you or your spouse being a debtor in a chapter 11 bankruptcy case open at any time in 2025, even if your only income is wages, interest or dividends

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 188, help 50. Help begins: “Yes if you or your spouse were a nonresident alien for any part of 2025, or you have any income or return treatment the question names, or any other outside the wages, interest, dividends, securities sales, Form 1099-R distributions and social security benefits this tool handles; Yes refuses the return.”

### 6. `$f1095a`

**⟶ topic switch**

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`)

> List each Form 1095-A (Health Insurance Marketplace Statement) you received, one entry per form. Do not list a VOID form, or the form a CORRECTED one replaces, or a form for a catastrophic or stand-alone dental plan. Leave the list empty if you received none.

- Offered: a list the filer builds, naming each entry
- Answer: the list `marketplace_policy` (persona)
- Words: prompt 45, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 7. `$retirement@person[taxpayer]`

**⟶ topic switch**

Topic: Form 1099-R distributions (IRAs, pensions and annuities) (`retirement`). About: You

> List each Form 1099-R you received, one entry per form (for example by payer). Leave the list empty if you received none.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 22, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 8. `$dependent`

**⟶ topic switch**

Topic: Dependents — qualifying child and qualifying relative tests, per person listed (`dependent`)

> List each person you claim as a dependent or who qualifies you for head of household, one entry per person. Leave the list empty if there is none.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 28, help 25. Help begins: “Any label you will recognize will do, such as “Child 1”; a name is not needed.”

### 9. `household.married`

**⟶ topic switch**

Topic: Household facts for dependents and head of household (`household`)

> Were you married at the end of 2025 (including married but considered unmarried for head of household status)?
>
> Use the marriage recognized under the law of the state or territory where it was entered into; a marriage entered into under foreign or American Indian tribal law counts if at least one U.S. state or territory would recognize it as a marriage.
>
> Include a common law marriage recognized in the state where you now live or where it began.
>
> Living apart does not end a marriage; an interlocutory (not final) divorce decree still means married.
>
> Answer No if, by December 31, you were divorced under a final decree, legally separated under a decree of divorce or separate maintenance, or had a court decree of annulment holding that no valid marriage ever existed.
>
> A registered domestic partnership, civil union or similar relationship not denominated as a marriage is not a marriage for federal tax purposes.
>
> This question asks whether you were married at year end; the separate filing-status rules for a spouse who died during 2025 are addressed separately.
>
> When choosing your filing status, also note: if you divorced solely to file as unmarried, intending at the time to remarry each other in the next tax year, and actually do so, you must file as married in both years.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 217, help 34. Help begins: “Married includes a married person who is considered unmarried for head of household status; a person legally separated under a decree of divorce or separate maintenance at the end of 2025 is not married.”

### 10. `household.spouse_died_2025`

Topic: Household facts for dependents and head of household (`household`)

> Did your spouse die in 2025? (Asked when your filing status is single or head of household, or when filing jointly although not married at the end of 2025.)

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 29, help 35. Help begins: “Asked when your filing status is single or head of household; a Yes is refused, since a person whose spouse died in 2025 is considered married for the whole year and files jointly or separately.”

### 11. `person[taxpayer].under16`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Were you under age 16 at the end of 2025?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 10, help 25. Help begins: “A return for a person under age 16 at the end of 2025 (you, or your spouse on a joint return) is outside this tool.”

### 12. `household.community_property`

**⟶ topic switch (returns)**

Topic: Household facts for dependents and head of household (`household`)

> Did you live in a community property state (Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington or Wisconsin) at any time in 2025?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 24, help 50. Help begins: “Asked of every filer not filing jointly; a married filer who files as head of household in one of the nine community property states, or a registered domestic partner in Nevada, Washington or California, is refused, since community income under state law (Form 8958, Pub.”

### 13. `s3.adoption_any`

**⟶ topic switch**

Topic: Schedule 3 — selected lines (`s3`)

> Since the start of 2024, did you adopt a child, or pay costs toward adopting one?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 16, help 18. Help begins: “Costs include agency, lawyer and court fees and travel, also for an adoption that did not go through.”

### 14. `$w2@person[taxpayer]`

**⟶ topic switch**

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`). About: You

> List the employers that gave you a Form W-2, one entry per employer. If one employer gave you more than one Form W-2, list that employer once and enter their boxes combined.

- Offered: a list the filer builds, naming each entry
- Answer: the list `logistics_co` (persona)
- Words: prompt 32, help 84. Help begins: “One entry per distinct employer, not per Form W-2: the excess social security credit turns on the number of employers, so an employer's corrected or additional Forms W-2 are combined under that employer.”

### 15. `person[taxpayer].w2[logistics_co].box1`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 1. About: You › w2 logistics_co

> Wages, tips, other compensation

- Offered: a dollar amount, zero or more
- Answer: $42,000.00 (persona)
- Words: prompt 4, help 23. Help begins: “Box 1 of this Form W-2 is wages, tips and other compensation, which leaves out elective deferrals such as 401(k) or 403(b) contributions.”

### 16. `person[taxpayer].w2[logistics_co].box2`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 2. About: You › w2 logistics_co

> Federal income tax withheld (box 2 of a Form W-2; on a Form W-2AS, W-2CM, W-2GU or W-2VI, box 2 is American Samoa, CNMI, Guam or U.S. Virgin Islands income tax, not federal income tax, so enter zero for it)

- Offered: a dollar amount, zero or more
- Answer: $4,600.00 (persona)
- Words: prompt 40, help 6. Help begins: “Read iw2w3, p.”

### 17. `$interest`

**⟶ topic switch**

Topic: Schedule B — interest payer entries (`interest`)

> List the payers of your taxable interest, one entry per payer. Leave the list empty if there are none.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 19, help 104. Help begins: “Include every payer of taxable interest, with or without a Form 1099-INT or 1099-OID: a bank or credit union; a bond or note, including original issue discount and accrued market discount (market discount on a tax-exempt bond is taxable interest); U.S.”

### 18. `$f8889@person[taxpayer]`

**⟶ topic switch**

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You

> Did you have a health savings account (HSA) in 2025, or get money from one?

- Offered: “Yes” / “No”
- Answer: “Yes” (persona)
- Words: prompt 15, help 71. Help begins: “Signs that you had one: box 12 of your Form W-2 shows the letter W, or the bank that holds the account sent you a Form 5498-SA (money put in) or a Form 1099-SA (money paid out).”

### 19. `person[taxpayer].f8889[hsa].owner_died`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Did the owner of this HSA die in 2025?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 9, help 31. Help begins: “The owner is the person these questions are about.”

### 20. `person[taxpayer].f8889[hsa].inherited`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Did you get an HSA, or money from one, because its owner died?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 13, help 28. Help begins: “For example, a parent, or a husband or wife who has died, named you as the beneficiary of their HSA.”

### 21. `person[taxpayer].f8889[hsa].archer`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Did you or your spouse have an Archer MSA in 2025?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 11, help 56. Help begins: “An Archer MSA is an older kind of medical savings account; on a Form 1099-SA (box 5) or Form 5498-SA (box 6) for one, the box “Archer MSA” is checked.”

### 22. `person[taxpayer].f8889[hsa].line9`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`), line 9. About: You › HSA

> How much did your employer put into your HSA for 2025, including money taken out of your pay?

- Offered: a dollar amount, zero or more
- Answer: $1,600.00 (persona)
- Words: prompt 18, help 41. Help begins: “Use the amount in box 12 of your Form W-2 next to the letter W.”

### 23. `person[taxpayer].f8889[hsa].line2`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`), line 2. About: You › HSA

> How much did you put into your HSA for 2025 yourself, not counting money in box 12 of your Form W-2?

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 21, help 107. Help begins: “Count deposits by you, or by anyone other than your employer, that were for 2025, made up to April 15, 2026 (later if you served in a combat zone).”

### 24. `person[taxpayer].f8889[hsa].ira_transfer`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Was any money moved into your HSA straight from an IRA in 2025?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 13, help 23. Help begins: “The IRA's custodian sends the money directly to the HSA.”

### 25. `person[taxpayer].f8889[hsa].excess_withdrawn`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> In 2025, or in 2026 before filing this return, did you take money back out of your HSA because too much had been put in?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 25, help 33. Help begins: “This is called withdrawing excess contributions.”

### 26. `person[taxpayer].f8889[hsa].coverage_year`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Was your health plan in 2025 a high-deductible plan that works with an HSA, and the same kind all year?

- Offered: “Yes, all 12 months, covering one person only” / “Yes, all 12 months, covering more than one person” / “No: it started, stopped or changed during 2025, or not sure”
- Answer: “No: it started, stopped or changed during 2025, or not sure” (`changed`) (persona)
- Words: prompt 20, help 90. Help begins: “What counts is the plan you had on the first day of each month; plan papers usually call such a plan “HSA-eligible” or “HDHP”.”

### 27. `person[taxpayer].f8889[hsa].months_eligible`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> On the first day of how many months of 2025 were you covered by an HSA-qualifying plan, with all three of these true?
>
> - you were not enrolled in Medicare
> - you had no other health coverage that pays medical bills, counting a health FSA or HRA at work that pays ordinary medical bills, yours or your spouse's (dental, vision, accident, disability and long-term care insurance do not count)
> - nobody could claim you as a dependent

- Offered: a whole number
- Answer: 8 (persona)
- Words: prompt 74, help 90. Help begins: “Count a month only if everything held on its first day; December counts as one of the months.”

### 28. `person[taxpayer].f8889[hsa].months_family`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> On the first day of how many of those months did your plan cover more than one person, or did your spouse have a high-deductible plan covering more than one person?

- Offered: a whole number
- Answer: 0 (persona)
- Words: prompt 31, help 60. Help begins: “Count a month also if you were covered by someone else's family plan, or had a plan for only you and a family plan at once.”

### 29. `person[taxpayer].f8889[hsa].dec_coverage`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> What did you have on December 1, 2025?

- Offered: “No HSA-qualifying coverage that day” / “An HSA-qualifying plan covering one person only” / “An HSA-qualifying plan covering more than one person”
- Answer: “An HSA-qualifying plan covering one person only” (`self_only`) (persona)
- Words: prompt 8, help 75. Help begins: “Choose the first answer if on December 1 you were enrolled in Medicare, had other health coverage that pays medical bills, or could be claimed as a dependent.”

### 30. `person[taxpayer].f8889[hsa].last_month`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Do you want to be treated as having had your December 1 coverage for all of 2025?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 17, help 75. Help begins: “This is the “last-month rule”.”

### 31. `person[taxpayer].f8889[hsa].age55`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Were you 55 or older on December 31, 2025?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 9, help 0

### 32. `person[taxpayer].f8889[hsa].ira_prior`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Was any money moved into your HSA straight from an IRA during 2024?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 13, help 45. Help begins: “The IRA's custodian sends the money directly to the HSA.”

### 33. `person[taxpayer].f8889[hsa].testing_prior`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> For 2024, was more put into your HSA, by you, your employer or anyone else, than the months you could have an HSA, and the kind of plan you had in each, allowed?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 33, help 175. Help begins: “This is about the “last-month rule”.”

### 34. `person[taxpayer].f8889[hsa].line14a`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`), line 14a. About: You › HSA

> How much came out of your HSA in 2025 in total?

- Offered: a dollar amount, zero or more
- Answer: $450.00 (persona)
- Words: prompt 11, help 56. Help begins: “Add box 1 of your 2025 Forms 1099-SA for HSAs (box 5 marks the kind of account).”

### 35. `person[taxpayer].f8889[hsa].dist_code`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Does box 3 of any of your 2025 Forms 1099-SA for an HSA show a number other than 1 or 3?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 21, help 36. Help begins: “Box 3 is the “distribution code”.”

### 36. `person[taxpayer].f8889[hsa].rollover`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> How much of the money that came out did you put into another HSA of your own within 60 days?

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 20, help 35. Help begins: “An HSA can take in only one such deposit in any 12 months; do not count a second one, or money the bank moved directly (that is not part of the total).”

### 37. `person[taxpayer].f8889[hsa].mistake_repaid`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Was any money paid out of your HSA by mistake and later put back?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 14, help 33. Help begins: “For example, the HSA paid a bill that turned out not to be a medical cost, and you returned the money to the HSA.”

### 38. `person[taxpayer].f8889[hsa].medical_all`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> Did all of the money that came out pay for doctor, dental, vision, hospital or pharmacy costs of you, your spouse, or your dependents?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 24, help 66. Help begins: “Answer No if any of it paid for insurance premiums, for someone else (such as an adult child you do not claim), for costs from before you opened the HSA, or for costs that insurance or anyone else paid back to you.”

### 39. `person[taxpayer].f8889[hsa].loan`

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You › HSA

> In 2025, did you use your HSA as security for a loan, borrow from it, lend to it, or buy from or sell to it yourself?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 26, help 51. Help begins: “It counts whether you did it yourself or through someone else.”

### 40. `div.any`

**⟶ topic switch**

Topic: Form 1099-DIV — distribution components and scope screening (`div`)

> In 2025, did you (or your spouse) receive any dividends or other distributions from a company or a fund, with or without a Form 1099-DIV? Count amounts that were reinvested, credited to an account or paid in shares or other property. Answer Yes if any of these applies:
>
> - a Form 1099-DIV for 2025, or the dividends section of a broker's consolidated statement or another substitute statement, shows an amount in your (or your spouse's) name, even if it was paid in early 2026 or no cash was paid (such as a deemed dividend on a convertible bond)
> - dividends from stock or from a mutual fund, ETF, money market fund or REIT
> - capital gain distributions, exempt-interest dividends, nondividend distributions (a return of capital) or liquidation distributions
> - dividends paid to you as a participant in an employee stock ownership plan (ESOP)
> - dividends received in your name that belong to someone else (as a nominee), or dividends that belong to you but were paid in someone else's name, such as your share of an account you own with a parent or another person
> - a corporation you own paid your personal expenses or gave you property, and the amount is treated as a dividend
> - dividends from a foreign company, dividends reported on a Schedule K-1, or dividends received without any form

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 217, help 104. Help begins: “If you are not sure, answer Yes: the next questions ask for each amount, and you can enter zero for any you did not receive.”

### 41. `f1040.line25b`

**⟶ topic switch (returns)**

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`), line 25b

> Federal income tax withheld shown on your Forms 1099 (supplied total of box 4 of Forms 1099-R, 1099-INT, 1099-DIV, 1099-G and other Forms 1099, box 6 of Form SSA-1099 and box 10 of Form RRB-1099)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 35, help 27. Help begins: “Total withholding shown in box 4 of your Forms 1099 (1099-R, 1099-INT, 1099-DIV, 1099-G and others), box 6 of Form SSA-1099 and box 10 of Form RRB-1099.”

### 42. `f1040.line25c_other`

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`)

> Federal income tax withheld shown on your Forms W-2G (box 4), Schedules K-1, and Forms 1042-S, 8805 and 8288-A (supplied total; not Additional Medicare Tax, which Form 8959 figures)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 29, help 17. Help begins: “See the line 25c instructions if any other form reports income tax withheld.”

### 43. `f1040.line26`

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`), line 26

> 2025 estimated tax payments you made and amount applied from your 2024 return (supplied total)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 15, help 16. Help begins: “Include quarterly payments and any 2024 overpayment you asked to be applied.”

### 44. `f4952.has_interest`

**⟶ topic switch**

Topic: Form 4952 — supported investment-interest deduction and election (`f4952`)

> Did you or your spouse pay or accrue any interest in 2025 on money borrowed for investments (even if the interest was for an earlier period), or does either of you have investment interest expense carried forward from an earlier year? Answer Yes if any of these applies:
>
> - interest on any loan of which any part was used to buy or hold property held for investment, such as stocks, bonds, funds, land held for appreciation, royalty interests, collectibles, cryptocurrency, a loan you made to someone else, an oil or gas working interest you do not materially participate in, or any other property held for investment; this includes brokerage margin interest, and a home equity loan, personal or family loan or credit card used that way, even if you received a Form 1098 for it
> - interest on a loan used to buy an interest in a partnership or S corporation
> - investment interest expense reported to you on a Schedule K-1 from a partnership or an S corporation
> - investment interest expense disallowed in 2024 or an earlier year and not yet deducted, by either of you, on a joint or separate return (line 7 of a 2024 Form 4952, or of the latest Form 4952 filed)

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 204, help 20. Help begins: “Answer Yes if you are not sure; the following questions ask for the amounts, and zero is a valid answer.”

### 45. `f4952.line4g`

Topic: Form 4952 — supported investment-interest deduction and election (`f4952`), line 4g

> Amount of qualified dividends and net capital gain elected into investment income. The election must be made on a timely filed return, including extensions. However, if you timely filed your return without making the election, you can make it on an amended return filed within 6 months of the due date of your return (excluding extensions); write "Filed pursuant to section 301.9100-2" on the amended return and file it at the same place you filed the original return. Enter 0 if neither applies.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 83, help 23. Help begins: “Elected income loses preferential rates.”

### 46. `f8863.paid`

**⟶ topic switch**

Topic: Form 8863, Education Credits (American Opportunity and Lifetime Learning Credits) (`f8863`)

> Did anyone pay qualified education expenses in 2025 for you, your spouse if filing jointly, or a dependent you claim, at a college, university, vocational school or other postsecondary school (for tuition, required fees or course materials)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 37, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 47. `f8959.unsupported`

**⟶ topic switch**

Topic: Form 8959 — Additional Medicare Tax on wages and self-employment income (`f8959`)

> Do you have any church employee income or other self-employment income outside Schedule SE as this tool prepares it, RRTA compensation, tips not reported to your employer or allocated tips in Form W-2 box 8 (Form 4137), Form 8919 wages, uncollected Medicare tax in Form W-2 box 12 (codes B or N), or Medicare wages on a wage statement from a U.S. territory (such as Form 499R-2/W-2PR)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 67, help 41. Help begins: “Yes if any of the listed items applies to you: church employee income, RRTA compensation, unreported or allocated tips (Form W-2 box 8), Form 8919 wages, uncollected Medicare tax (Form W-2 box 12 codes B or N), or territory wage statements.”

### 48. `f8962.alloc`

**⟶ topic switch**

Topic: Form 8962, Premium Tax Credit (Parts I to III) (`f8962`)

> Did any Marketplace policy, including one whose Form 1095-A went only to someone else, cover someone in your tax family and also someone who is not in it (for example a former spouse, a child someone else claims, or a child you claim whom someone else enrolled), or were you divorced or legally separated during 2025 while enrolled in a policy with your former spouse?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 65, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 49. `f8962.other`

Topic: Form 8962, Premium Tax Credit (Parts I to III) (`f8962`)

> Does any of these apply?
>
> - someone enrolled in a Marketplace policy was not lawfully present in the United States
> - for any month, anyone in your tax family was eligible for minimum essential coverage other than coverage in the individual market, including:
>   - Medicare Part A or Part C
>   - Medicaid
>   - the Children's Health Insurance Program (CHIP)
>   - TRICARE
>   - certain benefits for veterans and their families
>   - health coverage for Peace Corps volunteers
>   - employer-sponsored coverage that was offered and was affordable and provided minimum value (other than during a waiting period before the benefits begin; the offer is affordable for the employee if the employee's share of the annual cost of self-only coverage is not more than 9.02% of household income (Form 8962, line 3), whatever family coverage costs, and for another member of the tax family allowed to enroll if the employee's share of the annual cost of coverage for the employee and the family members allowed to enroll is not more than 9.02% of household income)
>   - employer-sponsored coverage the person actually enrolled in (including COBRA or retiree coverage) even if it was not affordable or did not provide minimum value
>   - other health coverage the Department of Health and Human Services designates as minimum essential coverage
> - you or a family member were offered or covered by a qualified small employer HRA (QSEHRA, W-2 box 12 code FF) or an individual coverage HRA for 2025
> - any part of a month's premium was not paid by the due date of your return, not including extensions (or, for coverage you enrolled in retroactively after a successful eligibility appeal, by the 120th day after the appeals decision), or a Form 1095-A shows zero in column A for a month whose premium you paid
> - advance payments were made for someone who is in no one's tax family
> - a Marketplace determination that you or a family member was ineligible for Medicaid or CHIP was later found to be based on incorrect information given with intentional or reckless disregard for the facts
> - someone enrolled was incarcerated, other than pending disposition of charges such as awaiting trial
>
> Do not count coverage bought in the individual market outside the Marketplace.

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 357, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 50. `f8962.premium_adjust`

Topic: Form 8962, Premium Tax Credit (Parts I to III) (`f8962`)

> Did either of these happen?
>
> - Marketplace coverage reported on a Form 1095-A (a qualified health plan) for anyone in your tax family began after the first day of a 2025 month, other than coverage effective on the date of a birth, adoption, or placement for adoption or in foster care, or on the effective date of a court order placing the individual with your family (those count from the first day of the month)
> - any premiums for a 2025 month of that Marketplace coverage were refunded in 2025
>
> A start date of other coverage (employer, Medicaid, or a catastrophic, stand-alone dental or SHOP plan) does not count here.

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 108, help 76. Help begins: “Answer yes if Marketplace coverage reported on a Form 1095-A began after the first day of a 2025 month (a birth, adoption, placement for adoption or foster care, or a court order placing the child with you counts from the first day) or premiums for a 2025 month of that coverage were refunded in 2025.”

### 51. `f1095a[marketplace_policy].void`

**⟶ topic switch (returns)**

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — Is this Form 1095-A marked VOID, or is it an original for the same policy that a later Form 1095-A marked VOID or CORRECTED supersedes? Do not enter a void or replaced form; enter only the form the Marketplace says to use.

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 50, help 37. Help begins: “Answer yes only if you entered a form you should not have.”

### 52. `f8962.fpl_table`

**⟶ topic switch (returns)**

Topic: Form 8962, Premium Tax Credit (Parts I to III) (`f8962`)

> Which federal poverty table applies: alaska if you, or your spouse on a joint return, lived in Alaska during 2025; otherwise hawaii if either of you lived in Hawaii during 2025; otherwise contiguous (the 48 contiguous states and the District of Columbia)

- Offered: “Neither of you lived in Alaska or Hawaii during 2025 (the 48 contiguous states and the District of Columbia)” / “You, or your spouse on a joint return, lived in Alaska during 2025” / “Either of you lived in Hawaii during 2025, and neither of you in Alaska”
- Answer: “Neither of you lived in Alaska or Hawaii during 2025 (the 48 contiguous states and the District of Columbia)” (`contiguous`) (persona)
- Words: prompt 42, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 53. `ftc.taxes`

**⟶ topic switch**

Topic: Foreign tax credit — election without Form 1116 (`ftc`)

> Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 17, help 25. Help begins: “Foreign income taxes you paid, after any required reductions.”

### 54. `person[taxpayer].age65`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Were you born before January 2, 1961?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 7, help 25. Help begins: “Yes if you were born before January 2, 1961.”

### 55. `person[taxpayer].educator_expenses`

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Qualified educator expenses you paid in 2025 (professional development courses you took that are related to the curriculum you teach or to the students you teach, and books, supplies, equipment (including computer equipment, software and services) and other materials used in the classroom, including personal protective equipment, disinfectant and other supplies used to prevent the spread of coronavirus; not expenses for home schooling or nonathletic supplies for courses in health or physical education), reduced by excludable savings bond interest (Form 8815), nontaxable qualified tuition program or Coverdell earnings or distributions, and reimbursements not reported in box 1 of your Form W-2; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 104, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 56. `person[taxpayer].rrta`

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`), rrta. About: You

> Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or did you file Form CT-2 as an employee representative?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 23, help 36. Help begins: “Yes if any of your Forms W-2 reports railroad retirement (RRTA) compensation or tax in box 14, or you filed Form CT-2 as an employee representative.”

### 57. `person[taxpayer].w2[logistics_co].box4`

**⟶ topic switch (returns)**

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 4. About: You › w2 logistics_co

> Social security tax withheld

- Offered: a dollar amount, zero or more
- Answer: $2,604.00 (persona)
- Words: prompt 4, help 13. Help begins: “Box 4 of this Form W-2 is the employee social security tax withheld.”

### 58. `person[taxpayer].w2[logistics_co].box5`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 5. About: You › w2 logistics_co

> Form W-2 box 5

- Offered: a dollar amount, zero or more
- Answer: $42,000.00 (persona)
- Words: prompt 4, help 27. Help begins: “Box 5 of this Form W-2 is Medicare wages and tips, which have no wage base limit and so can be more than boxes 3 and 7.”

### 59. `person[taxpayer].w2[logistics_co].box6`

Topic: Form W-2 — wage, withholding and Social Security boxes by employer (`w2`), line 6. About: You › w2 logistics_co

> Form W-2 box 6

- Offered: a dollar amount, zero or more
- Answer: $609.00 (persona)
- Words: prompt 4, help 17. Help begins: “Box 6 of this Form W-2 is the employee Medicare tax withheld, including any Additional Medicare Tax.”

### 60. `refund.received`

**⟶ topic switch**

Topic: State and Local Income Tax Refund Worksheet—Schedule 1, Line 1 (`refund`)

> State or local income tax refunds, credits or offsets you received in 2025: the total of box 2 of your Forms 1099-G (or a similar statement), including any part you chose to apply to your 2025 estimated state or local income tax and any part offset against a debt, and any refund for which you received no Form 1099-G; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 62, help 44. Help begins: “Zero if none.”

### 61. `s1.alimony`

**⟶ topic switch**

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`)

> Did you receive or pay alimony or separate maintenance in 2025 under a divorce or separation agreement entered into on or before December 31, 2018 (counting only payments made before any change after 2018 that expressly applies the post-2018 rules, that is, one that states that the post-2018 alimony rules apply, or that alimony isn't deductible by the payer or isn't included in the recipient's income), or must you include or may you deduct a recapture of alimony?
>
> Alimony under an agreement entered into after 2018 is neither income nor deductible; answer false for it.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 95, help 45. Help begins: “Alimony is a payment in cash to or for a spouse or former spouse under a divorce or separation instrument; child support, noncash property settlements and voluntary payments are not alimony (Pub.”

### 62. `s1.line8_other`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`)

> Do you have any income (or loss or exclusion) for Schedule 1, line 8, other than the following?
>
> - gambling winnings (line 8b)
> - canceled debt (line 8c)
> - income from Form 8889 (line 8f)
> - Alaska Permanent Fund dividends (line 8g)
> - jury duty pay (line 8h)
> - prizes and awards (line 8i)
> - income from an activity not engaged in for profit (line 8j)
> - scholarship and fellowship grants not reported on Form W-2 (line 8r)
> - the other income asked item by item for line 8z
>
> Other income, loss or exclusion, for example:
> - a net operating loss deduction (8a)
> - the foreign earned income or housing exclusion from Form 2555 (8d)
> - income from Form 8853 (8e)
> - stock options (8k)
> - income from the rental of personal property (8l)
> - Olympic and Paralympic medals or USOC prize money (8m)
> - a section 951(a) or 951A(a) inclusion (8n, 8o)
> - a section 461(l) excess business loss adjustment (8p)
> - taxable distributions from an ABLE account (8q)
> - nontaxable Medicaid waiver payments (8s)
> - a pension or annuity from a nonqualified deferred compensation plan or a nongovernmental section 457 plan (8t)
> - wages earned while incarcerated (8u)
> - digital assets received as ordinary income not reported elsewhere (8v)

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 189, help 52. Help begins: “Income from self-employment, or nonemployee compensation on Form 1099-MISC, 1099-NEC or 1099-K that is self-employment income, belongs on Schedule C, not on line 8.”

### 63. `$oi8z`

**⟶ topic switch**

Topic: Schedule 1, line 8z — other income, one entry per item listed (`oi8z`)

> List each item of other income for Schedule 1, line 8z (taxable income not reported elsewhere on your return), one entry per item.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 23, help 18. Help begins: “Leave the list empty if there is none.”

### 64. `s1.cod_any`

**⟶ topic switch (returns)**

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`)

> Was any of your debt canceled or forgiven in 2025 (for example, you received a Form 1099-C, or a lender forgave a debt you owed without one)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 27, help 21. Help begins: “A nonbusiness debt is a personal debt, such as a credit card or personal loan.”

### 65. `s1.gambling_winnings`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`)

> Gambling winnings you had in 2025 that are not attributable to a trade or business: box 1 of every Form W-2G plus winnings with no Form W-2G (lotteries, raffles, fantasy sports leagues, a lump sum from selling a right to future lottery payments, and the fair market value of noncash prizes such as cars), without subtracting any losses; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 61, help 46. Help begins: “Include every Form W-2G box 1 amount; the federal income tax withheld in Form W-2G box 4 goes on Form 1040 line 25c (the supplied total of withholding from other forms).”

### 66. `s1.line8g`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`), line 8g

> Alaska Permanent Fund dividends paid to you (and, on a joint return, your spouse) in 2025, as shown on the document the state of Alaska sends with the payment, without reducing them by any energy relief payment; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 40, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 67. `s1.line8h`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`), line 8h

> Jury duty pay you (and, on a joint return, your spouse) received in 2025, including any you gave to your employer; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 24, help 22. Help begins: “All jury duty pay received in 2025, whether or not a form reported it, including any pay you gave to your employer.”

### 68. `s1.line8i`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`), line 8i

> Prizes and awards you (and, on a joint return, your spouse) received in 2025 that are not gambling winnings, not wages from an employer and not Olympic or Paralympic medals or USOC prize money (for example a contest, quiz or drawing prize, or a scholarship prize you need not use for education), goods or services at their fair market value; leave out a prize you refused and a prize transferred under the section 74(b) rules; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 78, help 29. Help begins: “Olympic and Paralympic medals and USOC prize money (usually in Form 1099-MISC box 3) go on line 8m, which this tool refuses (answer Yes to the line 8 screen).”

### 69. `s1.line8j`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`), line 8j

> Income you (and, on a joint return, your spouse) received in 2025 from an activity not engaged in for profit, such as a hobby (not a business you report on Schedule C and not the rental of personal property); zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 42, help 14. Help begins: “The expenses of an activity not engaged in for profit are not subtracted here.”

### 70. `s1.line8r`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`), line 8r

> Scholarship and fellowship grants you (and, on a joint return, your spouse) received in 2025 that are not reported on a Form W-2; if you were a degree candidate, only the part used for expenses other than tuition and course-related expenses (for example room, board and travel); zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 50, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 71. `s1.uc_paid`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`)

> Unemployment compensation paid to you in 2025: the total of box 1 of your Forms 1099-G (if box 1 is wrong, the amount actually paid)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 25, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 72. `s1a.carloan`

**⟶ topic switch**

Topic: Schedule 1-A (Form 1040) — Additional Deductions (`s1a`)

> Did you pay or accrue interest in 2025 on a loan taken out after 2024 to buy a new car, minivan, van, SUV, pickup truck or motorcycle for personal use that you want to deduct on Schedule 1-A, Part IV?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 40, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 73. `s2.amt`

**⟶ topic switch**

Topic: Schedule 2 — Additional Taxes (the lines this tool computes) (`s2`)

> Are you required to file Form 6251 or do you have an AMT adjustment requiring its review?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 17, help 17. Help begins: “Yes if you must file Form 6251 or have an alternative minimum tax adjustment that needs review.”

### 74. `s2.other`

Topic: Schedule 2 — Additional Taxes (the lines this tool computes) (`s2`)

> Any amount on Schedule 2 other than the following?
>
> - self-employment tax from Schedule SE
> - Additional Medicare Tax
> - Net Investment Income Tax
> - the additional 20% tax on taxable HSA distributions (Form 8889 line 17b, which this tool figures)
>
> Other amounts, for example:
> - the alternative minimum tax
> - repayment of a clean vehicle credit
> - household employment taxes
> - the additional tax on an HSA you did not keep as an eligible individual (Form 8889 Part III)
> - uncollected social security or Medicare tax on tips or group-term life insurance (W-2 box 12 codes A, B, M or N)
> - tax on unreported tips (Form 4137)
> - interest on deferred tax
>
> Form 5329 Part I, early distributions, and the 2025 HSA excess are figured by this tool and are not other amounts.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 124, help 30. Help begins: “Yes if Schedule 2 has any amount this tool does not figure, such as alternative minimum tax, a clean vehicle credit repayment, household employment taxes, or tax on unreported tips.”

### 75. `person[taxpayer].x_other`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Does any of these apply to you?
>
> - a taxable distribution from a Coverdell ESA, a qualified tuition program (529 plan) or an ABLE account
> - excess contributions to a traditional or Roth IRA for an earlier year that remained in the IRA at the end of 2025 (whether or not you contributed for 2025)
> - excess contributions to a Coverdell ESA, an Archer MSA or an ABLE account
> - excess HSA contributions from an earlier year that you had not removed or used up before 2025 (including any amount on line 48 of your 2024 Form 5329, or an excess you never reported), whether or not you have a Form 8889 for 2025
> - a required minimum distribution from an IRA or plan that you did not receive in full by its deadline (including a shortfall you made up later)

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 136, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 76. `s3.credit_bond`

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`)

> In 2025, did a bond you own, or a fund, give you a federal tax credit?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 16, help 17. Help begins: “Reported on Form 1097-BTC or by the bond’s issuer; a bond that only pays interest gives none.”

### 77. `s3.disability_retired`

Topic: Schedule 3 — selected lines (`s3`)

> Have you retired on permanent and total disability?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 8, help 23. Help begins: “Yes if a person under 65 had to stop working because of a condition a doctor expects to last at least a year.”

### 78. `s3.ev`

Topic: Schedule 3 — selected lines (`s3`)

> In 2025, did you get an electric, plug-in hybrid or fuel-cell vehicle, or install home equipment to charge or fuel a vehicle?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 22, help 19. Help begins: “Count a vehicle you received in 2025, new or used, bought or leased, even if you ordered it earlier.”

### 79. `s3.farmland`

Topic: Schedule 3 — selected lines (`s3`)

> In 2025, did you sell farmland?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 6, help 9. Help begins: “Yes also if you traded it for other property.”

### 80. `s3.foreign_any`

Topic: Schedule 3 — selected lines (`s3`)

> Have you ever paid income tax to another country, had income from a U.S. territory, or owned 10% or more of a foreign company?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 24, help 41. Help begins: “Count foreign tax a fund paid for you (Form 1099-DIV box 7) only if you once filed Form 1116 for it.”

### 81. `s3.kerosene`

Topic: Schedule 3 — selected lines (`s3`)

> In 2025, was kerosene used in your home for heat, light or cooking?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 13, help 0

### 82. `s3.line10`

Topic: Schedule 3 — selected lines (`s3`), line 10

> Amount paid with request for extension to file: the payment you made to get an automatic extension, or any amount you paid with Form 4868 or Form 2350, not counting any fee charged for making the payment; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 40, help 31. Help begins: “The amount paid with Form 4868 or Form 2350, or paid to get an automatic extension of time to file, without any fee charged for making the payment.”

### 83. `s3.prior_other_forms`

Topic: Schedule 3 — selected lines (`s3`)

> Apart from Form 1040 and its schedules, does your 2024 federal tax return include any separate form (a page headed “Form” and a four-digit number)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 16. Help begins: “For example Form 8962 or Form 8801.”

### 84. `s3.repaid_income`

Topic: Schedule 3 — selected lines (`s3`)

> In 2025, did you pay back more than $3,000 that you had reported as income in an earlier year?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 19, help 35. Help begins: “Add up everything you paid back in 2025, for example wages or a bonus you had to return.”

### 85. `sa.dependent`

**⟶ topic switch**

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Can someone claim you or your spouse as a dependent for 2025, or are you a dual-status alien? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 48, help 41. Help begins: “Yes if someone else can claim you or your spouse as a dependent for 2025, or you are a dual-status alien.”

### 86. `person[taxpayer].blind`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Were you blind at the end of 2025?
>
> Answer yes if you were totally blind as of December 31, 2025.
>
> If you weren't totally blind, answer yes only if you have a statement certified by your eye doctor (ophthalmologist or optometrist) that you can't see better than 20/200 in your better eye with glasses or contact lenses, or that your field of vision is 20 degrees or less (or, if your eye condition isn't likely to improve beyond these conditions, a certified statement to that effect).
>
> If your vision can be corrected beyond these limits only by contact lenses that you can wear only briefly because of pain, infection or ulcers, answer yes.
>
> Keep the statement for your records.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 119, help 39. Help begins: “Yes if you were blind at the end of 2025, as the question defines it; if not totally blind, a statement certified by an eye doctor is needed.”

### 87. `sa.elect_itemize`

**⟶ topic switch (returns)**

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Elect to itemize even if the standard deduction is larger?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 10, help 13. Help begins: “Yes if you choose to itemize even though the standard deduction is larger.”

### 88. `sa.excluded_income`

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Do you file Form 2555 or Form 4563, or have income excluded as a bona fide resident of Puerto Rico?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 20, help 20. Help begins: “Yes if you file Form 2555 or Form 4563, or exclude income as a bona fide resident of Puerto Rico.”

### 89. `sa.line8a`

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`), line 8a

> Eligible home mortgage interest and points on Form 1098, after confirming the debt/use limits do not apply

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 17, help 21. Help begins: “Home mortgage interest and points reported to you on Form 1098, when no debt or use limit applies.”

### 90. `sa.unsupported`

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Any casualty or theft loss (including a disaster loss added to the standard deduction); a deduction from the Schedule A line 16 list other than gambling losses; a foreign tax or generation-skipping tax deduction; mortgage interest or points not on Form 1098 or subject to the debt or use limits (loan proceeds not all used to buy, build or improve the home, or debt over the limit); or the sales-tax election?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 71, help 42. Help begins: “Yes if you have a casualty or theft loss, a Schedule A line 16 deduction other than gambling losses, a foreign or generation-skipping tax deduction, mortgage interest or points not on Form 1098 or subject to limits, or you elect sales tax.”

### 91. `sa.gifts`

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Did you or your spouse make any charitable contribution in 2025, or does either of you have a charitable contribution carried over from an earlier year? Answer Yes if any of these applies:
>
> - money given to a charity by cash, check, card or payroll deduction, including money put into a donor-advised fund
> - a payment to a charity that got you something back (such as a fundraising dinner, an auction item or a membership), or that earned you a state or local tax credit
> - property given to a charity, such as clothing, household items, a vehicle or stock, or property sold to a charity for less than its value
> - out-of-pocket costs of volunteer work for a charity, such as mileage, parking, supplies or uniforms, or unreimbursed costs of hosting a student or a foster child placed by a charitable organization
> - a charitable contribution shown on a Schedule K-1 from a partnership, S corporation, estate or trust
> - expenses you paid as a whaling captain for Native Alaskan subsistence bowhead whale hunting
> - a contribution from an earlier year (in most cases one of the five years before 2025) that was more than you could deduct that year, by either of you, on a joint or separate return; if you itemized in any of those years, check that return and any carryover worksheet or statement kept with it
>
> A charity here is any organization that is religious, charitable, educational, scientific or literary in purpose (such as a church, a school, a nonprofit hospital, a veterans' group or a fraternal order's charitable work), one that works to prevent cruelty to children or animals, or a federal, state, local or Indian tribal government receiving a gift for public purposes; nonprofit cemetery companies and other qualified organizations count too.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 292, help 20. Help begins: “Answer Yes if you are not sure; the following questions ask for the amounts, and zero is a valid answer.”

### 92. `sa.line1`

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`), line 1

> Unreimbursed eligible medical and dental expenses paid in 2025 (Pub. 502 lists what counts) for these people:
>
> - yourself
> - your spouse
> - your dependents
> - your child whom you do not claim only because of the rules for children of divorced or separated parents
> - anyone you could have claimed as a dependent except that the person had gross income of $5,200 or more or filed a joint return
>
> Reduce them by payments from insurance or other sources, but do not reduce them by a 2025 reimbursement of expenses paid in an earlier year.
>
> Leave out:
> - amounts equal to tax-free distributions from a health savings account (HSA) or an Archer MSA
> - insurance premiums paid by a pretax reduction of your pay, and premiums and other medical and dental expenses paid by an employer-sponsored health plan (cafeteria plan) unless they are included in box 1 of your Form W-2
> - premiums for someone on your policy who is not one of the people listed above (for example a nondependent child under age 27), unless you had family coverage when you added that person and your premiums did not increase
> - if you are a retired public safety officer, premiums to the extent paid with a tax-free distribution from your retirement plan
> - the housework part of pay to someone who did both nursing and housework (only the nursing help counts)
> - meals while away from home for medical care, other than hospital care, which includes its meals and lodging (other lodging for medical care counts at no more than $50 a night for each person who meets the Pub. 502 lodging requirements)
>
> Reduce health insurance premiums by any self-employed health insurance deduction on Schedule 1 (Form 1040), line 17.
>
> For Marketplace coverage on a Form 1095-A, include the total premiums (including the part paid by advance payments of the premium tax credit), minus the premium tax credit allowed on Form 8962, line 24, and minus any excess advance payments you do not have to repay because of the repayment limit (Form 8962, line 27 minus line 29); advance payments you do repay count as premiums you paid.
>
> Include qualified long-term care insurance premiums only up to the limit for the age at the end of 2025 of the person for whom they were paid:
>
> - $480 if 40 or under
> - $900 if 41 to 50
> - $1,800 if 51 to 60
> - $4,810 if 61 to 70
> - $6,020 if 71 or older
>
> On the final return of a person who died in 2025, include the medical expenses paid out of that person's estate that Pub. 502 allows on the final return.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 429, help 24. Help begins: “Your unreimbursed medical and dental expenses for 2025, such as hospital care, clinic costs, lab fees, and premiums not paid pretax.”

### 93. `sa.line5a`

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`), line 5a

> State/local income taxes you paid, including withholding; no sales-tax election.
>
> Include state and local income taxes withheld in 2025 (but not withholding you deducted on another form, such as Schedule C), estimated payments made in 2025 (including a prior-year refund credited to 2025), and taxes paid in 2025 for a prior year, but not penalties or interest.
>
> Include mandatory contributions to:
> - the California, New Jersey or New York Nonoccupational Disability Benefit Fund
> - the Rhode Island Temporary Disability Benefit Fund
> - the Washington State Supplemental Workmen's Compensation Fund
> - the Alaska, California, New Jersey or Pennsylvania state unemployment fund
> - state family leave programs (such as New Jersey Family Leave Insurance or California Paid Family Leave)
>
> Do not reduce the amount by a state or local income tax refund or credit you expect for 2025, or by a refund or credit of prior-year state and local income taxes received in 2025.
>
> If you made a cash charitable contribution in return for a state or local tax credit and reduced your charitable deduction by that credit, you may include here (or on line 5b or 5c, whichever tax the credit offsets) the part of the credit you applied to your 2025 or an earlier year's state or local tax liability.
>
> Include income taxes imposed by a U.S. territory here (not as foreign taxes), except territory taxes allocable to excluded income and territory taxes you take as a credit instead of a deduction.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 237, help 21. Help begins: “State and local income taxes paid in 2025, including withholding, estimated payments, and prior-year taxes paid this year.”

### 94. `sa.line5b`

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`), line 5b

> Deductible state/local real estate taxes on real estate you own that was not used for business, only if the taxes are assessed uniformly at a like rate on all real property in the community and used for general community or governmental purposes.
>
> Leave out:
> - foreign real estate taxes
> - itemized charges for services to specific property or persons (for example trash collection, water use or mowing charges)
> - charges for improvements that tend to increase the property's value (for example an assessment to build a new sidewalk), except a charge used only to maintain an existing public facility (for example to repair an existing sidewalk)
>
> If your mortgage payments include real estate taxes, include only what the mortgage company actually paid to the taxing authority in 2025.
>
> Reduce the amount by a 2025 refund or rebate of real estate taxes paid in 2025, and by real estate tax charged to the buyer if you sold your home in 2025 (settlement statement, Form 1099-S box 6); do not reduce it by a refund of taxes paid in an earlier year.
>
> Only taxes paid in 2025 and assessed before 2026 count (state or local law determines when a tax is assessed, generally when you become liable for it), so leave out a prepayment of 2026 property tax not assessed before 2026.
>
> Include real estate taxes imposed by a U.S. territory, except those allocable to excluded income.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 232, help 23. Help begins: “State and local real estate taxes you paid in 2025 on property you own that is not used for business.”

### 95. `sa.line5c`

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`), line 5c

> Deductible state/local personal property taxes: only taxes based on value alone and imposed on a yearly basis (for a yearly car registration fee based partly on value, only the part based on value), paid in 2025 and assessed before 2026. Include personal property taxes imposed by a U.S. territory, except those allocable to excluded income.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 55, help 31. Help begins: “State and local personal property taxes you paid in 2025 that were based on value alone and imposed yearly, such as the value-based part of a car fee.”

### 96. `sb.foreign_any`

**⟶ topic switch**

Topic: Schedule B — supported interest and ordinary dividends (`sb`)

> At any time in 2025, did you have a foreign account, any other foreign financial asset, a connection to a foreign trust, or a role in a foreign corporation? Count an account or asset you had for only part of the year, including one closed, emptied or sold during 2025, and count it whatever its value. Count what you hold directly or indirectly: through an agent or nominee, a single-member LLC or other disregarded entity, a trust you are treated as owning (such as a revocable living trust), or a corporation, partnership or other entity in which you own more than 50% of the value, the voting power, the profits or the capital, directly or through other companies, partnerships or trusts. Answer Yes if any of these applies to you:
>
> - a financial interest in, or signature authority over, an account located outside the United States: a bank, savings, checking, deposit, brokerage, securities, mutual fund, pension or retirement, or commodity futures or options account, or an insurance or annuity policy with a cash value (an account at a branch of a US bank located abroad counts, and so does a cash-value policy issued by an insurer organized outside the United States, even if you bought it or pay for it from the United States)
> - signature authority means you could direct the institution to move the account's assets, alone or together with someone else, even with no money of your own in it, such as an account of your employer, a relative, a business or an organization
> - a financial interest also includes an account of a trust in which you have more than a 50% present beneficial interest
> - an account with a financial institution organized in a US territory (such as Puerto Rico or Guam), or any other account or balance with a business outside the United States that holds money or assets for customers, such as an online payment, mobile-money, cryptocurrency exchange, online betting or gaming, precious-metals custody, or prepaid or stored-value account
> - held outside an account at a US financial institution, counting a company, partnership or other entity organized in Puerto Rico, Guam or another US territory as foreign: stock, bonds or other securities issued by a non-US company or person; an interest in a foreign partnership, company, estate or other entity; a foreign pension or deferred compensation plan; a swap, option or other contract with a foreign counterparty; a loan you made to, or other debt owed to you by, someone who is not a US citizen or resident, or a foreign company or government, even if they live or operate in the United States (including a personal loan to a relative or friend abroad); or being an heir or beneficiary of an estate probated or administered outside the United States, or of someone who lived or died outside the United States, even if nothing has been paid to you yet
> - any of the above held by a child whose interest and dividends you report on your return (Form 8814)
> - a distribution from a foreign trust, including money or property that reached you through another person or company (a loan of cash or marketable securities counts, and so does free or below-market use of a home, car or other property the trust owns); being the grantor of, or a transferor to, a foreign trust that existed at any time during 2025, even one created or funded in an earlier year (a transferor is anyone who gave, sold, lent or otherwise transferred money or property to the trust, directly or through another person, in 2025 or any earlier year); or being a beneficiary of a foreign trust
> - a foreign foundation (such as a Stiftung or Anstalt), a waqf or another arrangement that holds property for beneficiaries counts as a trust; a trust counts as foreign if a court outside the 50 states and the District of Columbia (including one in Puerto Rico, Guam or another US territory) supervises it, or if any trustee or anyone who controls a substantial trust decision is not a US citizen or resident (such as a relative abroad), even if the trust was set up under US law or has a US address; if you are not sure whether an arrangement is a trust or whether a trust is foreign, answer Yes
> - being an officer, director, managing director or manager of a foreign corporation or other company, whatever it is called (such as a Ltd, plc, GmbH, AG, SA, SARL or BV), that is organized outside the 50 states and the District of Columbia, including in Puerto Rico, Guam or another US territory (such as an employer's subsidiary there); or owning 10% or more of the total value, or of the combined voting power, of a foreign corporation's stock, counting shares owned by your spouse, children, grandchildren or parents and by partnerships, corporations, trusts or estates you have an interest in, and shares any of you could acquire through options or warrants

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 827, help 98. Help begins: “If you are not sure, answer Yes.”

### 97. `sd.carryover`

**⟶ topic switch**

Topic: Schedule D — securities sales and supplied distribution subtotals (`sd`)

> Did line 21 of your 2024 Schedule D show a loss? On a 2025 joint return, answer for your 2024 joint return, or for either spouse's separate 2024 return.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 29, help 0

### 98. `sd.other_forms`

Topic: Schedule D — securities sales and supplied distribution subtotals (`sd`)

> Are there gains or losses from (or that belong on) Forms 4797, 2439, 6252, 4684, 6781 or 8824, or capital gains or losses on a Schedule K-1? Count section 1256 contracts and a casualty or theft of property whether you held the property directly or through an entity.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 48, help 0

### 99. `$sales`

**⟶ topic switch**

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`)

> List each sale you report for 2025, one entry per transaction, including transactions intended for aggregate reporting. Leave the list empty only if there were no sales.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 27, help 19. Help begins: “Enter each transaction once; the tool decides whether it goes on Form 8949 or in Schedule D aggregate reporting.”

### 100. `sli.interest`

**⟶ topic switch**

Topic: Student Loan Interest Deduction Worksheet—Schedule 1, Line 21 (`sli`)

> Total interest you paid in 2025 on qualified student loans (generally Form 1098-E box 1), not counting the amounts below; zero if none.
>
> Not counted:
> - any amount paid from tax-free qualified tuition program earnings
> - any amount paid through tax-free student loan repayment assistance (the National Health Service Corps Loan Repayment Program, a state education loan repayment program eligible for funds under the Public Health Service Act, or another state loan repayment or loan forgiveness program intended to increase the availability of health services in underserved or health professional shortage areas)
>
> A qualified student loan is a loan you took out to pay the qualified higher education expenses (tuition, fees, room and board, and related expenses such as books and supplies, for education in a degree, certificate or similar program at an eligible educational institution) of an eligible student who was any of these:
>
> - you
> - your spouse
> - a person who was your dependent when the loan was taken out
> - a person you could have claimed as a dependent for that year except that the person filed a joint return, had gross income of at least the exemption amount for that year, or you could be claimed as a dependent
>
> It is not a qualified student loan if any of its proceeds were used for other purposes, or if it was from a related person or from a person who borrowed the proceeds under a qualified employer plan or a contract purchased under such a plan.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 244, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 101. `ssb.benefits`

**⟶ topic switch**

Topic: Social Security Benefits Worksheet—Lines 6a and 6b (`ssb`)

> Total of box 5 (net benefits) of all your Forms SSA-1099 and RRB-1099 for 2025

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 15, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 102. `$sc@person[taxpayer]`

**⟶ topic switch**

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You

> Did you operate a business or practice a profession as a sole proprietor in 2025 (income reported to you on Forms 1099-NEC, 1099-K or 1099-MISC for your own work is usually such a business)? List each such business, one entry per business; leave the list empty if none.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 48, help 0

### 103. `s1a.overtime`

**⟶ topic switch (returns)**

Topic: Schedule 1-A (Form 1040) — Additional Deductions (`s1a`)

> Did you receive overtime pay as an employee in 2025 that you want to deduct on Schedule 1-A, Part III (the FLSA Overtime Premium, generally the "half" of time-and-a-half)? (Overtime reported on Form 1099-NEC or 1099-MISC is asked about with Schedule C.)

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 42, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 104. `s1a.tips`

Topic: Schedule 1-A (Form 1040) — Additional Deductions (`s1a`)

> Did you receive tips as an employee in 2025 in an occupation on the IRS list of occupations that customarily and regularly received tips (IRS.gov/TippedOccupations) that you want to deduct on Schedule 1-A, Part II? (Tips received as a non-employee, in your own trade or business, are asked about with Schedule C.)

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 52, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 105. `s179.line10`

**⟶ topic switch**

Topic: Form 4562, Part I — Election To Expense Certain Property Under Section 179 (Summary for the return) (`s179`), line 10

> The carryover of disallowed section 179 deduction from line 13 of your (and, on a joint return, your spouse's) 2024 Form 4562 (zero if none). If you did not file a 2024 Form 4562 (it is required only when a deduction is claimed), use line 13 of the last Form 4562 you filed (section 179 cost elected in an earlier year and not yet allowed because of the business income limit carries over until it is deducted)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 77, help 0

### 106. `f2441.benefits`

**⟶ topic switch**

Topic: Form 2441 — Child and Dependent Care Expenses (Parts I to III) (`f2441`)

> Did you (or your spouse, if filing jointly) receive dependent care benefits for 2025 — amounts shown in box 10 of a Form W-2, or an amount from your 2024 dependent care plan that you used in 2025 during a grace period?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 41, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 107. `f2441.care`

Topic: Form 2441 — Child and Dependent Care Expenses (Parts I to III) (`f2441`)

> In 2025, did you pay for, or incur expenses for, the care of a qualifying person so that you (and your spouse) could work or look for work? A qualifying person is your child under age 13; your spouse who was not able to care for themselves; or any other person who was not able to care for themselves, lived with you for more than half of 2025, and is your dependent or would be except that they had gross income of $5,200 or more, they filed a joint return, or you could be claimed as a dependent on someone else's 2025 return. Include 2024 care you paid for in 2025 and 2025 care you will pay for in 2026.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 120, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 108. `person[taxpayer].sav_trad`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Did you make contributions (other than rollover contributions) to a traditional IRA for 2025, deductible or not, including contributions made by the due date of your 2025 return for 2025? Do not count contributions made under a SEP or SIMPLE IRA plan, including those you made for yourself as a self-employed person.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 52, help 79. Help begins: “Contributions to a traditional IRA for 2025, which may be made until April 15, 2026.”

### 109. `qbi.unsupported`

**⟶ topic switch**

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> Do you have any of these: qualified business income or loss, or PTP income or loss, other than section 199A dividends and the Schedule C businesses entered in this tool; a prior-year REIT or PTP loss carryforward, or losses or deductions suspended in an earlier year by another provision and allowed this year; or are you a patron of any agricultural or horticultural cooperative, specified or not (including any qualified payments from one on Form 1099-PATR)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 76, help 34. Help begins: “Yes if you have qualified business or PTP income or loss other than section 199A dividends and your Schedule C businesses, a prior-year REIT or PTP loss carryforward, or agricultural cooperative patronage (Form 1099-PATR).”

### 110. `qbi.carryforward`

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`), line 3

> The qualified business loss carryforward from line 16 of your 2024 Form 8995 (or the corresponding line of your 2024 Form 8995-A), entered as a positive amount (zero if none)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 30, help 0

### 111. `f5695.part1_any`

**⟶ topic switch**

Topic: Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`)

> Did you have 2025 costs for solar electric, solar water heating, small wind energy, geothermal heat pump, battery storage or fuel cell property for a home in the United States, or a residential clean energy credit carryforward from line 16 of a 2024 Form 5695? Include your proportionate share of such costs paid by the condominium management association of a condominium you own, or by a cooperative housing corporation in which you are a tenant-stockholder. A cost of an item counts in 2025 when its original installation is completed in 2025, whenever it was paid; but a cost connected with constructing or reconstructing a home counts when your original use of that home begins (for example, solar panels installed in 2024 on a newly built home you first lived in in 2025 count in 2025). An item installed after 2025 does not qualify.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 143, help 14. Help begins: “Answer Yes also if the only Part I amount is a carryforward from 2024.”

### 112. `f5695.part2_any`

Topic: Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`)

> Did you have 2025 costs for insulation or air sealing, exterior doors, exterior windows or skylights, central air conditioners, natural gas, propane or oil water heaters, furnaces or hot water boilers, electric or natural gas heat pumps or heat pump water heaters, biomass stoves or boilers, panelboards, subpanelboards, branch circuits or feeders, or a home energy audit, for a home in the United States? Include your proportionate share of such costs paid by the condominium management association of a condominium you own, or by a cooperative housing corporation in which you are a tenant-stockholder. A cost of an item counts in 2025 when its original installation is completed in 2025 (for a cost connected with the reconstruction of your home, when your original use of the reconstructed home begins), whenever it was paid; an item installed after 2025 does not qualify.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 141, help 11. Help begins: “There is no carryforward of this credit from an earlier year.”

### 113. `f1040.tax_exempt_interest`

**⟶ topic switch (returns)**

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`)

> Total tax-exempt interest and tax-exempt OID for 2025 (Form 1099-INT box 8; Form 1099-OID boxes 2 and 11), net of amortized bond premium and acquisition premium; do not include exempt-interest dividends (Form 1099-DIV box 12) or interest earned in an IRA, HSA, Archer or Medicare Advantage MSA, or Coverdell education savings account

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 52, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 114. `f1095a[marketplace_policy].uniform`

**⟶ topic switch (returns)**

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — Does this Form 1095-A show coverage in all 12 months of 2025, with the same amount in column A (monthly enrollment premiums) every month and the same amount in column B (monthly SLCSP premium) every month?
>
> Use the corrected column B if column B is blank, zero or wrong, and answer no if the correct amount is not the same every month.
>
> Column B can be blank, zero or wrong if no advance payments of the premium tax credit were made.
>
> It is wrong for the months affected if, during 2025, any of these happened and you did not tell the Marketplace:
>
> - you enrolled someone newly added to your tax family (for example a newborn)
> - someone in your tax family was enrolled for only part of the year
> - someone in your coverage family became eligible, or stopped being eligible, for employer coverage or other minimum essential coverage
> - you include someone in your tax family whom you did not tell the Marketplace you would include, or leave out someone you said you would include
> - an enrolled person died
> - you moved
>
> Get the correct amount from the Marketplace's tool, for example HealthCare.gov/Tax-Tool.

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 198, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 115. `f1095a[marketplace_policy].in_a_apr`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — April 2025, column A (monthly enrollment premiums): the amount in column A; if column A is blank or zero but you paid that month's enrollment premiums by the due date of your return (not including extensions), the premiums you paid; zero only if no premiums were paid for that month by that date

- Offered: a dollar amount, zero or more
- Answer: $385.00 (persona)
- Words: prompt 61, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 116. `f1095a[marketplace_policy].in_a_aug`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — August 2025, column A (monthly enrollment premiums): the amount in column A; if column A is blank or zero but you paid that month's enrollment premiums by the due date of your return (not including extensions), the premiums you paid; zero only if no premiums were paid for that month by that date

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 61, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 117. `f1095a[marketplace_policy].in_a_dec`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — December 2025, column A (monthly enrollment premiums): the amount in column A; if column A is blank or zero but you paid that month's enrollment premiums by the due date of your return (not including extensions), the premiums you paid; zero only if no premiums were paid for that month by that date

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 61, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 118. `f1095a[marketplace_policy].in_a_feb`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — February 2025, column A (monthly enrollment premiums): the amount in column A; if column A is blank or zero but you paid that month's enrollment premiums by the due date of your return (not including extensions), the premiums you paid; zero only if no premiums were paid for that month by that date

- Offered: a dollar amount, zero or more
- Answer: $385.00 (persona)
- Words: prompt 61, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 119. `f1095a[marketplace_policy].in_a_jan`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — January 2025, column A (monthly enrollment premiums): the amount in column A; if column A is blank or zero but you paid that month's enrollment premiums by the due date of your return (not including extensions), the premiums you paid; zero only if no premiums were paid for that month by that date

- Offered: a dollar amount, zero or more
- Answer: $385.00 (persona)
- Words: prompt 61, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 120. `f1095a[marketplace_policy].in_a_jul`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — July 2025, column A (monthly enrollment premiums): the amount in column A; if column A is blank or zero but you paid that month's enrollment premiums by the due date of your return (not including extensions), the premiums you paid; zero only if no premiums were paid for that month by that date

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 61, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 121. `f1095a[marketplace_policy].in_a_jun`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — June 2025, column A (monthly enrollment premiums): the amount in column A; if column A is blank or zero but you paid that month's enrollment premiums by the due date of your return (not including extensions), the premiums you paid; zero only if no premiums were paid for that month by that date

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 61, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 122. `f1095a[marketplace_policy].in_a_mar`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — March 2025, column A (monthly enrollment premiums): the amount in column A; if column A is blank or zero but you paid that month's enrollment premiums by the due date of your return (not including extensions), the premiums you paid; zero only if no premiums were paid for that month by that date

- Offered: a dollar amount, zero or more
- Answer: $385.00 (persona)
- Words: prompt 61, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 123. `f1095a[marketplace_policy].in_a_may`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — May 2025, column A (monthly enrollment premiums): the amount in column A; if column A is blank or zero but you paid that month's enrollment premiums by the due date of your return (not including extensions), the premiums you paid; zero only if no premiums were paid for that month by that date

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 61, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 124. `f1095a[marketplace_policy].in_a_nov`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — November 2025, column A (monthly enrollment premiums): the amount in column A; if column A is blank or zero but you paid that month's enrollment premiums by the due date of your return (not including extensions), the premiums you paid; zero only if no premiums were paid for that month by that date

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 61, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 125. `f1095a[marketplace_policy].in_a_oct`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — October 2025, column A (monthly enrollment premiums): the amount in column A; if column A is blank or zero but you paid that month's enrollment premiums by the due date of your return (not including extensions), the premiums you paid; zero only if no premiums were paid for that month by that date

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 61, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 126. `f1095a[marketplace_policy].in_a_sep`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — September 2025, column A (monthly enrollment premiums): the amount in column A; if column A is blank or zero but you paid that month's enrollment premiums by the due date of your return (not including extensions), the premiums you paid; zero only if no premiums were paid for that month by that date

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 61, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 127. `f1095a[marketplace_policy].in_b_apr`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — April 2025, column B (monthly SLCSP premium): the amount in column B, or the correct applicable SLCSP premium if column B is blank, wrong (for example after a move or a change in your tax or coverage family that you did not report to the Marketplace), or zero for a month whose premiums were paid by the due date of your return (from the Marketplace's tool, for example HealthCare.gov/Tax-Tool); zero if no one was enrolled in this policy that month (column A blank) or if that month's premiums were not paid by the due date of your return (not including extensions)

- Offered: a dollar amount, zero or more
- Answer: $410.00 (persona)
- Words: prompt 109, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 128. `f1095a[marketplace_policy].in_b_feb`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — February 2025, column B (monthly SLCSP premium): the amount in column B, or the correct applicable SLCSP premium if column B is blank, wrong (for example after a move or a change in your tax or coverage family that you did not report to the Marketplace), or zero for a month whose premiums were paid by the due date of your return (from the Marketplace's tool, for example HealthCare.gov/Tax-Tool); zero if no one was enrolled in this policy that month (column A blank) or if that month's premiums were not paid by the due date of your return (not including extensions)

- Offered: a dollar amount, zero or more
- Answer: $410.00 (persona)
- Words: prompt 109, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 129. `f1095a[marketplace_policy].in_b_jan`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — January 2025, column B (monthly SLCSP premium): the amount in column B, or the correct applicable SLCSP premium if column B is blank, wrong (for example after a move or a change in your tax or coverage family that you did not report to the Marketplace), or zero for a month whose premiums were paid by the due date of your return (from the Marketplace's tool, for example HealthCare.gov/Tax-Tool); zero if no one was enrolled in this policy that month (column A blank) or if that month's premiums were not paid by the due date of your return (not including extensions)

- Offered: a dollar amount, zero or more
- Answer: $410.00 (persona)
- Words: prompt 109, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 130. `f1095a[marketplace_policy].in_b_mar`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — March 2025, column B (monthly SLCSP premium): the amount in column B, or the correct applicable SLCSP premium if column B is blank, wrong (for example after a move or a change in your tax or coverage family that you did not report to the Marketplace), or zero for a month whose premiums were paid by the due date of your return (from the Marketplace's tool, for example HealthCare.gov/Tax-Tool); zero if no one was enrolled in this policy that month (column A blank) or if that month's premiums were not paid by the due date of your return (not including extensions)

- Offered: a dollar amount, zero or more
- Answer: $410.00 (persona)
- Words: prompt 109, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 131. `f1095a[marketplace_policy].in_b_aug`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — August 2025, column B (monthly SLCSP premium): the amount in column B, or the correct applicable SLCSP premium if column B is blank, wrong (for example after a move or a change in your tax or coverage family that you did not report to the Marketplace), or zero for a month whose premiums were paid by the due date of your return (from the Marketplace's tool, for example HealthCare.gov/Tax-Tool); zero if no one was enrolled in this policy that month (column A blank) or if that month's premiums were not paid by the due date of your return (not including extensions)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 109, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 132. `f1095a[marketplace_policy].in_b_dec`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — December 2025, column B (monthly SLCSP premium): the amount in column B, or the correct applicable SLCSP premium if column B is blank, wrong (for example after a move or a change in your tax or coverage family that you did not report to the Marketplace), or zero for a month whose premiums were paid by the due date of your return (from the Marketplace's tool, for example HealthCare.gov/Tax-Tool); zero if no one was enrolled in this policy that month (column A blank) or if that month's premiums were not paid by the due date of your return (not including extensions)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 109, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 133. `f1095a[marketplace_policy].in_b_jul`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — July 2025, column B (monthly SLCSP premium): the amount in column B, or the correct applicable SLCSP premium if column B is blank, wrong (for example after a move or a change in your tax or coverage family that you did not report to the Marketplace), or zero for a month whose premiums were paid by the due date of your return (from the Marketplace's tool, for example HealthCare.gov/Tax-Tool); zero if no one was enrolled in this policy that month (column A blank) or if that month's premiums were not paid by the due date of your return (not including extensions)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 109, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 134. `f1095a[marketplace_policy].in_b_jun`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — June 2025, column B (monthly SLCSP premium): the amount in column B, or the correct applicable SLCSP premium if column B is blank, wrong (for example after a move or a change in your tax or coverage family that you did not report to the Marketplace), or zero for a month whose premiums were paid by the due date of your return (from the Marketplace's tool, for example HealthCare.gov/Tax-Tool); zero if no one was enrolled in this policy that month (column A blank) or if that month's premiums were not paid by the due date of your return (not including extensions)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 109, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 135. `f1095a[marketplace_policy].in_b_may`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — May 2025, column B (monthly SLCSP premium): the amount in column B, or the correct applicable SLCSP premium if column B is blank, wrong (for example after a move or a change in your tax or coverage family that you did not report to the Marketplace), or zero for a month whose premiums were paid by the due date of your return (from the Marketplace's tool, for example HealthCare.gov/Tax-Tool); zero if no one was enrolled in this policy that month (column A blank) or if that month's premiums were not paid by the due date of your return (not including extensions)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 109, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 136. `f1095a[marketplace_policy].in_b_nov`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — November 2025, column B (monthly SLCSP premium): the amount in column B, or the correct applicable SLCSP premium if column B is blank, wrong (for example after a move or a change in your tax or coverage family that you did not report to the Marketplace), or zero for a month whose premiums were paid by the due date of your return (from the Marketplace's tool, for example HealthCare.gov/Tax-Tool); zero if no one was enrolled in this policy that month (column A blank) or if that month's premiums were not paid by the due date of your return (not including extensions)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 109, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 137. `f1095a[marketplace_policy].in_b_oct`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — October 2025, column B (monthly SLCSP premium): the amount in column B, or the correct applicable SLCSP premium if column B is blank, wrong (for example after a move or a change in your tax or coverage family that you did not report to the Marketplace), or zero for a month whose premiums were paid by the due date of your return (from the Marketplace's tool, for example HealthCare.gov/Tax-Tool); zero if no one was enrolled in this policy that month (column A blank) or if that month's premiums were not paid by the due date of your return (not including extensions)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 109, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 138. `f1095a[marketplace_policy].in_b_sep`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — September 2025, column B (monthly SLCSP premium): the amount in column B, or the correct applicable SLCSP premium if column B is blank, wrong (for example after a move or a change in your tax or coverage family that you did not report to the Marketplace), or zero for a month whose premiums were paid by the due date of your return (from the Marketplace's tool, for example HealthCare.gov/Tax-Tool); zero if no one was enrolled in this policy that month (column A blank) or if that month's premiums were not paid by the due date of your return (not including extensions)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 109, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 139. `f1095a[marketplace_policy].in_c_apr`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — April 2025, column C (monthly advance payment of premium tax credit); zero if blank

- Offered: a dollar amount, zero or more
- Answer: $210.00 (persona)
- Words: prompt 22, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 140. `f1095a[marketplace_policy].in_c_aug`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — August 2025, column C (monthly advance payment of premium tax credit); zero if blank

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 22, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 141. `f1095a[marketplace_policy].in_c_dec`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — December 2025, column C (monthly advance payment of premium tax credit); zero if blank

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 22, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 142. `f1095a[marketplace_policy].in_c_feb`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — February 2025, column C (monthly advance payment of premium tax credit); zero if blank

- Offered: a dollar amount, zero or more
- Answer: $210.00 (persona)
- Words: prompt 22, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 143. `f1095a[marketplace_policy].in_c_jan`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — January 2025, column C (monthly advance payment of premium tax credit); zero if blank

- Offered: a dollar amount, zero or more
- Answer: $210.00 (persona)
- Words: prompt 22, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 144. `f1095a[marketplace_policy].in_c_jul`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — July 2025, column C (monthly advance payment of premium tax credit); zero if blank

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 22, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 145. `f1095a[marketplace_policy].in_c_jun`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — June 2025, column C (monthly advance payment of premium tax credit); zero if blank

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 22, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 146. `f1095a[marketplace_policy].in_c_mar`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — March 2025, column C (monthly advance payment of premium tax credit); zero if blank

- Offered: a dollar amount, zero or more
- Answer: $210.00 (persona)
- Words: prompt 22, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 147. `f1095a[marketplace_policy].in_c_may`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — May 2025, column C (monthly advance payment of premium tax credit); zero if blank

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 22, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 148. `f1095a[marketplace_policy].in_c_nov`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — November 2025, column C (monthly advance payment of premium tax credit); zero if blank

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 22, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 149. `f1095a[marketplace_policy].in_c_oct`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — October 2025, column C (monthly advance payment of premium tax credit); zero if blank

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 22, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 150. `f1095a[marketplace_policy].in_c_sep`

Topic: Form 1095-A, Health Insurance Marketplace Statement (one entry per form) (`f1095a`). About: f1095a marketplace_policy

> For this Form 1095-A (Health Insurance Marketplace Statement) — September 2025, column C (monthly advance payment of premium tax credit); zero if blank

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 22, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

## The end reached

**Complete.** The return is completed after 150 questions.

## Totals

| | |
|---|---|
| Questions asked | 150 |
| Answered by the persona / by the background / opened and unanswered | 74 / 76 / 0 |
| Prompt words | 10384 |
| Help words (optional to read) | 4105 |
| Words of the answers offered (Yes and No not counted) | 168 |
| Questions answered no, zero or none | 121 |
| Topics met | 33 |
| Topic switches | 48 |
| of them, returns to a topic already left | 16 |

## The 10 longest prompts met

| # | Question | Prompt words | Answer |
|---|---|---|---|
| 96 | `sb.foreign_any` | 827 | No |
| 92 | `sa.line1` | 429 | $0.00 |
| 49 | `f8962.other` | 357 | No |
| 4 | `scope.schedule1` | 293 | No |
| 91 | `sa.gifts` | 292 | No |
| 100 | `sli.interest` | 244 | $0.00 |
| 93 | `sa.line5a` | 237 | $0.00 |
| 94 | `sa.line5b` | 232 | $0.00 |
| 9 | `household.married` | 217 | No |
| 40 | `div.any` | 217 | No |

## The whole walk, one line per question

Number, question id, prompt words, answer. `>` begins a new topic (`>>` a return to a topic already left), named at the right; `*` marks the persona's own answer, `!` an opened and unanswered question.

```
> *  1  $person                                         6w  ["taxpayer"]                  [person]
> *  2  f1040.status                                    9w  "single"                      [f1040]
>    3  scope.other_line16                            182w  false                         [scope]
     4  scope.schedule1                               293w  false
     5  scope.other_income                            188w  false
> *  6  $f1095a                                        45w  ["marketplace_policy"]        [f1095a]
>    7  $retirement@person[taxpayer]                   22w  []                            [retirement]
>    8  $dependent                                     28w  []                            [dependent]
>    9  household.married                             217w  false                         [household]
    10  household.spouse_died_2025                     29w  false
>>  11  person[taxpayer].under16                       10w  false                         [person]
>>  12  household.community_property                   24w  false                         [household]
>   13  s3.adoption_any                                16w  false                         [s3]
> * 14  $w2@person[taxpayer]                           32w  ["logistics_co"]              [w2]
  * 15  person[taxpayer].w2[logistics_co].box1          4w  4200000
  * 16  person[taxpayer].w2[logistics_co].box2         40w  460000
>   17  $interest                                      19w  []                            [interest]
> * 18  $f8889@person[taxpayer]                        15w  ["hsa"]                       [f8889]
  * 19  person[taxpayer].f8889[hsa].owner_died          9w  false
  * 20  person[taxpayer].f8889[hsa].inherited          13w  false
  * 21  person[taxpayer].f8889[hsa].archer             11w  false
  * 22  person[taxpayer].f8889[hsa].line9              18w  160000
  * 23  person[taxpayer].f8889[hsa].line2              21w  0
  * 24  person[taxpayer].f8889[hsa].ira_transfer       13w  false
  * 25  person[taxpayer].f8889[hsa].excess_withdrawn   25w  false
  * 26  person[taxpayer].f8889[hsa].coverage_year      20w  "changed"
  * 27  person[taxpayer].f8889[hsa].months_eligible    74w  8
  * 28  person[taxpayer].f8889[hsa].months_family      31w  0
  * 29  person[taxpayer].f8889[hsa].dec_coverage        8w  "self_only"
  * 30  person[taxpayer].f8889[hsa].last_month         17w  false
  * 31  person[taxpayer].f8889[hsa].age55               9w  false
  * 32  person[taxpayer].f8889[hsa].ira_prior          13w  false
  * 33  person[taxpayer].f8889[hsa].testing_prior      33w  false
  * 34  person[taxpayer].f8889[hsa].line14a            11w  45000
  * 35  person[taxpayer].f8889[hsa].dist_code          21w  false
  * 36  person[taxpayer].f8889[hsa].rollover           20w  0
  * 37  person[taxpayer].f8889[hsa].mistake_repaid     14w  false
  * 38  person[taxpayer].f8889[hsa].medical_all        24w  true
  * 39  person[taxpayer].f8889[hsa].loan               26w  false
>   40  div.any                                       217w  false                         [div]
>>  41  f1040.line25b                                  35w  0                             [f1040]
    42  f1040.line25c_other                            29w  0
    43  f1040.line26                                   15w  0
>   44  f4952.has_interest                            204w  false                         [f4952]
    45  f4952.line4g                                   83w  0
>   46  f8863.paid                                     37w  false                         [f8863]
>   47  f8959.unsupported                              67w  false                         [f8959]
> * 48  f8962.alloc                                    65w  false                         [f8962]
  * 49  f8962.other                                   357w  false
  * 50  f8962.premium_adjust                          108w  false
>>* 51  f1095a[marketplace_policy].void                50w  false                         [f1095a]
>>* 52  f8962.fpl_table                                42w  "contiguous"                  [f8962]
>   53  ftc.taxes                                      17w  0                             [ftc]
>>  54  person[taxpayer].age65                          7w  false                         [person]
    55  person[taxpayer].educator_expenses            104w  0
    56  person[taxpayer].rrta                          23w  false
>>* 57  person[taxpayer].w2[logistics_co].box4          4w  260400                        [w2]
  * 58  person[taxpayer].w2[logistics_co].box5          4w  4200000
  * 59  person[taxpayer].w2[logistics_co].box6          4w  60900
>   60  refund.received                                62w  0                             [refund]
>   61  s1.alimony                                     95w  false                         [s1]
    62  s1.line8_other                                189w  false
>   63  $oi8z                                          23w  []                            [oi8z]
>>  64  s1.cod_any                                     27w  false                         [s1]
    65  s1.gambling_winnings                           61w  0
    66  s1.line8g                                      40w  0
    67  s1.line8h                                      24w  0
    68  s1.line8i                                      78w  0
    69  s1.line8j                                      42w  0
    70  s1.line8r                                      50w  0
    71  s1.uc_paid                                     25w  0
>   72  s1a.carloan                                    40w  false                         [s1a]
>   73  s2.amt                                         17w  false                         [s2]
    74  s2.other                                      124w  false
>>  75  person[taxpayer].x_other                      136w  false                         [person]
>>  76  s3.credit_bond                                 16w  false                         [s3]
    77  s3.disability_retired                           8w  false
    78  s3.ev                                          22w  false
    79  s3.farmland                                     6w  false
    80  s3.foreign_any                                 24w  false
    81  s3.kerosene                                    13w  false
    82  s3.line10                                      40w  0
    83  s3.prior_other_forms                           25w  false
    84  s3.repaid_income                               19w  false
>   85  sa.dependent                                   48w  false                         [sa]
>>  86  person[taxpayer].blind                        119w  false                         [person]
>>  87  sa.elect_itemize                               10w  false                         [sa]
    88  sa.excluded_income                             20w  false
    89  sa.line8a                                      17w  0
    90  sa.unsupported                                 71w  false
    91  sa.gifts                                      292w  false
    92  sa.line1                                      429w  0
    93  sa.line5a                                     237w  0
    94  sa.line5b                                     232w  0
    95  sa.line5c                                      55w  0
>   96  sb.foreign_any                                827w  false                         [sb]
>   97  sd.carryover                                   29w  false                         [sd]
    98  sd.other_forms                                 48w  false
>   99  $sales                                         27w  []                            [sales]
>  100  sli.interest                                  244w  0                             [sli]
>  101  ssb.benefits                                   15w  0                             [ssb]
>  102  $sc@person[taxpayer]                           48w  []                            [sc]
>> 103  s1a.overtime                                   42w  false                         [s1a]
   104  s1a.tips                                       52w  false
>  105  s179.line10                                    77w  0                             [s179]
>  106  f2441.benefits                                 41w  false                         [f2441]
   107  f2441.care                                    120w  false
>> 108  person[taxpayer].sav_trad                      52w  false                         [person]
>  109  qbi.unsupported                                76w  false                         [qbi]
   110  qbi.carryforward                               30w  0
>  111  f5695.part1_any                               143w  false                         [f5695]
   112  f5695.part2_any                               141w  false
>>*113  f1040.tax_exempt_interest                      52w  0                             [f1040]
>>*114  f1095a[marketplace_policy].uniform            198w  false                         [f1095a]
  *115  f1095a[marketplace_policy].in_a_apr            61w  38500
  *116  f1095a[marketplace_policy].in_a_aug            61w  0
  *117  f1095a[marketplace_policy].in_a_dec            61w  0
  *118  f1095a[marketplace_policy].in_a_feb            61w  38500
  *119  f1095a[marketplace_policy].in_a_jan            61w  38500
  *120  f1095a[marketplace_policy].in_a_jul            61w  0
  *121  f1095a[marketplace_policy].in_a_jun            61w  0
  *122  f1095a[marketplace_policy].in_a_mar            61w  38500
  *123  f1095a[marketplace_policy].in_a_may            61w  0
  *124  f1095a[marketplace_policy].in_a_nov            61w  0
  *125  f1095a[marketplace_policy].in_a_oct            61w  0
  *126  f1095a[marketplace_policy].in_a_sep            61w  0
  *127  f1095a[marketplace_policy].in_b_apr           109w  41000
  *128  f1095a[marketplace_policy].in_b_feb           109w  41000
  *129  f1095a[marketplace_policy].in_b_jan           109w  41000
  *130  f1095a[marketplace_policy].in_b_mar           109w  41000
  *131  f1095a[marketplace_policy].in_b_aug           109w  0
  *132  f1095a[marketplace_policy].in_b_dec           109w  0
  *133  f1095a[marketplace_policy].in_b_jul           109w  0
  *134  f1095a[marketplace_policy].in_b_jun           109w  0
  *135  f1095a[marketplace_policy].in_b_may           109w  0
  *136  f1095a[marketplace_policy].in_b_nov           109w  0
  *137  f1095a[marketplace_policy].in_b_oct           109w  0
  *138  f1095a[marketplace_policy].in_b_sep           109w  0
  *139  f1095a[marketplace_policy].in_c_apr            22w  21000
  *140  f1095a[marketplace_policy].in_c_aug            22w  0
  *141  f1095a[marketplace_policy].in_c_dec            22w  0
  *142  f1095a[marketplace_policy].in_c_feb            22w  21000
  *143  f1095a[marketplace_policy].in_c_jan            22w  21000
  *144  f1095a[marketplace_policy].in_c_jul            22w  0
  *145  f1095a[marketplace_policy].in_c_jun            22w  0
  *146  f1095a[marketplace_policy].in_c_mar            22w  21000
  *147  f1095a[marketplace_policy].in_c_may            22w  0
  *148  f1095a[marketplace_policy].in_c_nov            22w  0
  *149  f1095a[marketplace_policy].in_c_oct            22w  0
  *150  f1095a[marketplace_policy].in_c_sep            22w  0
```
