# Walk: 05_self_employed

A single self-employed graphic designer, 38, with one business, a car used partly for the business, and an office in her home.

Written by `node engine/dist/main.js draft-walk` from `interview/2025/personas/05_self_employed.yaml`: the built interview (profile `full`, the federal questions, 2025) in its own asking order. Each prompt is as the page shows it to this filer. An answer marked *persona* is the persona's own; *background* is the answer a filer with nothing to report gives. A topic is the form the question's input belongs to; **⟶ topic switch** marks a question whose topic differs from the one before it (**returns** when the walk had already left that topic). Words are counted as `interview-words` counts them. Help is shown and optional to read: only its length and first sentence are given.

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
- Answer: none (an empty list) (background)
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
- Answer: none (an empty list) (background)
- Words: prompt 32, help 84. Help begins: “One entry per distinct employer, not per Form W-2: the excess social security credit turns on the number of employers, so an employer's corrected or additional Forms W-2 are combined under that employer.”

### 15. `$interest`

**⟶ topic switch**

Topic: Schedule B — interest payer entries (`interest`)

> List the payers of your taxable interest, one entry per payer. Leave the list empty if there are none.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 19, help 104. Help begins: “Include every payer of taxable interest, with or without a Form 1099-INT or 1099-OID: a bank or credit union; a bond or note, including original issue discount and accrued market discount (market discount on a tax-exempt bond is taxable interest); U.S.”

### 16. `$f8889@person[taxpayer]`

**⟶ topic switch**

Topic: Form 8889 — Health Savings Accounts (Parts I and II) (`f8889`). About: You

> Did you have a health savings account (HSA) in 2025, or get money from one?

- Offered: “Yes” / “No”
- Answer: “No” (background)
- Words: prompt 15, help 71. Help begins: “Signs that you had one: box 12 of your Form W-2 shows the letter W, or the bank that holds the account sent you a Form 5498-SA (money put in) or a Form 1099-SA (money paid out).”

### 17. `div.any`

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

### 18. `f1040.line25b`

**⟶ topic switch (returns)**

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`), line 25b

> Federal income tax withheld shown on your Forms 1099 (supplied total of box 4 of Forms 1099-R, 1099-INT, 1099-DIV, 1099-G and other Forms 1099, box 6 of Form SSA-1099 and box 10 of Form RRB-1099)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 35, help 27. Help begins: “Total withholding shown in box 4 of your Forms 1099 (1099-R, 1099-INT, 1099-DIV, 1099-G and others), box 6 of Form SSA-1099 and box 10 of Form RRB-1099.”

### 19. `f1040.line25c_other`

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`)

> Federal income tax withheld shown on your Forms W-2G (box 4), Schedules K-1, and Forms 1042-S, 8805 and 8288-A (supplied total; not Additional Medicare Tax, which Form 8959 figures)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 29, help 17. Help begins: “See the line 25c instructions if any other form reports income tax withheld.”

### 20. `f1040.line26`

Topic: Form 1040 — U.S. Individual Income Tax Return (the lines this tool computes) (`f1040`), line 26

> 2025 estimated tax payments you made and amount applied from your 2024 return (supplied total)

- Offered: a dollar amount, zero or more
- Answer: $12,000.00 (persona)
- Words: prompt 15, help 16. Help begins: “Include quarterly payments and any 2024 overpayment you asked to be applied.”

### 21. `f4952.has_interest`

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

### 22. `f4952.line4g`

Topic: Form 4952 — supported investment-interest deduction and election (`f4952`), line 4g

> Amount of qualified dividends and net capital gain elected into investment income. The election must be made on a timely filed return, including extensions. However, if you timely filed your return without making the election, you can make it on an amended return filed within 6 months of the due date of your return (excluding extensions); write "Filed pursuant to section 301.9100-2" on the amended return and file it at the same place you filed the original return. Enter 0 if neither applies.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 83, help 23. Help begins: “Elected income loses preferential rates.”

### 23. `f8863.paid`

**⟶ topic switch**

Topic: Form 8863, Education Credits (American Opportunity and Lifetime Learning Credits) (`f8863`)

> Did anyone pay qualified education expenses in 2025 for you, your spouse if filing jointly, or a dependent you claim, at a college, university, vocational school or other postsecondary school (for tuition, required fees or course materials)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 37, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 24. `f8959.unsupported`

**⟶ topic switch**

Topic: Form 8959 — Additional Medicare Tax on wages and self-employment income (`f8959`)

> Do you have any church employee income or other self-employment income outside Schedule SE as this tool prepares it, RRTA compensation, tips not reported to your employer or allocated tips in Form W-2 box 8 (Form 4137), Form 8919 wages, uncollected Medicare tax in Form W-2 box 12 (codes B or N), or Medicare wages on a wage statement from a U.S. territory (such as Form 499R-2/W-2PR)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 67, help 41. Help begins: “Yes if any of the listed items applies to you: church employee income, RRTA compensation, unreported or allocated tips (Form W-2 box 8), Form 8919 wages, uncollected Medicare tax (Form W-2 box 12 codes B or N), or territory wage statements.”

### 25. `ftc.taxes`

**⟶ topic switch**

Topic: Foreign tax credit — election without Form 1116 (`ftc`)

> Total creditable foreign taxes after required reductions; generally Form 1099-INT box 6 and Form 1099-DIV box 7

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 17, help 25. Help begins: “Foreign income taxes you paid, after any required reductions.”

### 26. `person[taxpayer].age65`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Were you born before January 2, 1961?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 7, help 25. Help begins: “Yes if you were born before January 2, 1961.”

### 27. `person[taxpayer].educator_expenses`

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Qualified educator expenses you paid in 2025 (professional development courses you took that are related to the curriculum you teach or to the students you teach, and books, supplies, equipment (including computer equipment, software and services) and other materials used in the classroom, including personal protective equipment, disinfectant and other supplies used to prevent the spread of coronavirus; not expenses for home schooling or nonathletic supplies for courses in health or physical education), reduced by excludable savings bond interest (Form 8815), nontaxable qualified tuition program or Coverdell earnings or distributions, and reimbursements not reported in box 1 of your Form W-2; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 104, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 28. `person[taxpayer].rrta`

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`), rrta. About: You

> Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or did you file Form CT-2 as an employee representative?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 23, help 36. Help begins: “Yes if any of your Forms W-2 reports railroad retirement (RRTA) compensation or tax in box 14, or you filed Form CT-2 as an employee representative.”

### 29. `refund.received`

**⟶ topic switch**

Topic: State and Local Income Tax Refund Worksheet—Schedule 1, Line 1 (`refund`)

> State or local income tax refunds, credits or offsets you received in 2025: the total of box 2 of your Forms 1099-G (or a similar statement), including any part you chose to apply to your 2025 estimated state or local income tax and any part offset against a debt, and any refund for which you received no Form 1099-G; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 62, help 44. Help begins: “Zero if none.”

### 30. `s1.alimony`

**⟶ topic switch**

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`)

> Did you receive or pay alimony or separate maintenance in 2025 under a divorce or separation agreement entered into on or before December 31, 2018 (counting only payments made before any change after 2018 that expressly applies the post-2018 rules, that is, one that states that the post-2018 alimony rules apply, or that alimony isn't deductible by the payer or isn't included in the recipient's income), or must you include or may you deduct a recapture of alimony?
>
> Alimony under an agreement entered into after 2018 is neither income nor deductible; answer false for it.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 95, help 45. Help begins: “Alimony is a payment in cash to or for a spouse or former spouse under a divorce or separation instrument; child support, noncash property settlements and voluntary payments are not alimony (Pub.”

### 31. `s1.line8_other`

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

### 32. `$oi8z`

**⟶ topic switch**

Topic: Schedule 1, line 8z — other income, one entry per item listed (`oi8z`)

> List each item of other income for Schedule 1, line 8z (taxable income not reported elsewhere on your return), one entry per item.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 23, help 18. Help begins: “Leave the list empty if there is none.”

### 33. `s1.cod_any`

**⟶ topic switch (returns)**

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`)

> Was any of your debt canceled or forgiven in 2025 (for example, you received a Form 1099-C, or a lender forgave a debt you owed without one)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 27, help 21. Help begins: “A nonbusiness debt is a personal debt, such as a credit card or personal loan.”

### 34. `s1.gambling_winnings`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`)

> Gambling winnings you had in 2025 that are not attributable to a trade or business: box 1 of every Form W-2G plus winnings with no Form W-2G (lotteries, raffles, fantasy sports leagues, a lump sum from selling a right to future lottery payments, and the fair market value of noncash prizes such as cars), without subtracting any losses; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 61, help 46. Help begins: “Include every Form W-2G box 1 amount; the federal income tax withheld in Form W-2G box 4 goes on Form 1040 line 25c (the supplied total of withholding from other forms).”

### 35. `s1.line8g`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`), line 8g

> Alaska Permanent Fund dividends paid to you (and, on a joint return, your spouse) in 2025, as shown on the document the state of Alaska sends with the payment, without reducing them by any energy relief payment; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 40, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 36. `s1.line8h`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`), line 8h

> Jury duty pay you (and, on a joint return, your spouse) received in 2025, including any you gave to your employer; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 24, help 22. Help begins: “All jury duty pay received in 2025, whether or not a form reported it, including any pay you gave to your employer.”

### 37. `s1.line8i`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`), line 8i

> Prizes and awards you (and, on a joint return, your spouse) received in 2025 that are not gambling winnings, not wages from an employer and not Olympic or Paralympic medals or USOC prize money (for example a contest, quiz or drawing prize, or a scholarship prize you need not use for education), goods or services at their fair market value; leave out a prize you refused and a prize transferred under the section 74(b) rules; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 78, help 29. Help begins: “Olympic and Paralympic medals and USOC prize money (usually in Form 1099-MISC box 3) go on line 8m, which this tool refuses (answer Yes to the line 8 screen).”

### 38. `s1.line8j`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`), line 8j

> Income you (and, on a joint return, your spouse) received in 2025 from an activity not engaged in for profit, such as a hobby (not a business you report on Schedule C and not the rental of personal property); zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 42, help 14. Help begins: “The expenses of an activity not engaged in for profit are not subtracted here.”

### 39. `s1.line8r`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`), line 8r

> Scholarship and fellowship grants you (and, on a joint return, your spouse) received in 2025 that are not reported on a Form W-2; if you were a degree candidate, only the part used for expenses other than tuition and course-related expenses (for example room, board and travel); zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 50, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 40. `s1.uc_paid`

Topic: Schedule 1 — Additional Income and Adjustments to Income (the lines this tool computes) (`s1`)

> Unemployment compensation paid to you in 2025: the total of box 1 of your Forms 1099-G (if box 1 is wrong, the amount actually paid)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 25, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 41. `s1a.carloan`

**⟶ topic switch**

Topic: Schedule 1-A (Form 1040) — Additional Deductions (`s1a`)

> Did you pay or accrue interest in 2025 on a loan taken out after 2024 to buy a new car, minivan, van, SUV, pickup truck or motorcycle for personal use that you want to deduct on Schedule 1-A, Part IV?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 40, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 42. `s2.amt`

**⟶ topic switch**

Topic: Schedule 2 — Additional Taxes (the lines this tool computes) (`s2`)

> Are you required to file Form 6251 or do you have an AMT adjustment requiring its review?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 17, help 17. Help begins: “Yes if you must file Form 6251 or have an alternative minimum tax adjustment that needs review.”

### 43. `s2.other`

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

### 44. `person[taxpayer].x_other`

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

### 45. `s3.credit_bond`

**⟶ topic switch (returns)**

Topic: Schedule 3 — selected lines (`s3`)

> In 2025, did a bond you own, or a fund, give you a federal tax credit?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 16, help 17. Help begins: “Reported on Form 1097-BTC or by the bond’s issuer; a bond that only pays interest gives none.”

### 46. `s3.disability_retired`

Topic: Schedule 3 — selected lines (`s3`)

> Have you retired on permanent and total disability?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 8, help 23. Help begins: “Yes if a person under 65 had to stop working because of a condition a doctor expects to last at least a year.”

### 47. `s3.ev`

Topic: Schedule 3 — selected lines (`s3`)

> In 2025, did you get an electric, plug-in hybrid or fuel-cell vehicle, or install home equipment to charge or fuel a vehicle?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 22, help 19. Help begins: “Count a vehicle you received in 2025, new or used, bought or leased, even if you ordered it earlier.”

### 48. `s3.farmland`

Topic: Schedule 3 — selected lines (`s3`)

> In 2025, did you sell farmland?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 6, help 9. Help begins: “Yes also if you traded it for other property.”

### 49. `s3.foreign_any`

Topic: Schedule 3 — selected lines (`s3`)

> Have you ever paid income tax to another country, had income from a U.S. territory, or owned 10% or more of a foreign company?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 24, help 41. Help begins: “Count foreign tax a fund paid for you (Form 1099-DIV box 7) only if you once filed Form 1116 for it.”

### 50. `s3.kerosene`

Topic: Schedule 3 — selected lines (`s3`)

> In 2025, was kerosene used in your home for heat, light or cooking?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 13, help 0

### 51. `s3.line10`

Topic: Schedule 3 — selected lines (`s3`), line 10

> Amount paid with request for extension to file: the payment you made to get an automatic extension, or any amount you paid with Form 4868 or Form 2350, not counting any fee charged for making the payment; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 40, help 31. Help begins: “The amount paid with Form 4868 or Form 2350, or paid to get an automatic extension of time to file, without any fee charged for making the payment.”

### 52. `s3.prior_other_forms`

Topic: Schedule 3 — selected lines (`s3`)

> Apart from Form 1040 and its schedules, does your 2024 federal tax return include any separate form (a page headed “Form” and a four-digit number)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 25, help 16. Help begins: “For example Form 8962 or Form 8801.”

### 53. `s3.repaid_income`

Topic: Schedule 3 — selected lines (`s3`)

> In 2025, did you pay back more than $3,000 that you had reported as income in an earlier year?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 19, help 35. Help begins: “Add up everything you paid back in 2025, for example wages or a bonus you had to return.”

### 54. `sa.dependent`

**⟶ topic switch**

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Can someone claim you or your spouse as a dependent for 2025, or are you a dual-status alien? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 48, help 41. Help begins: “Yes if someone else can claim you or your spouse as a dependent for 2025, or you are a dual-status alien.”

### 55. `person[taxpayer].blind`

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

### 56. `sa.elect_itemize`

**⟶ topic switch (returns)**

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Elect to itemize even if the standard deduction is larger?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 10, help 13. Help begins: “Yes if you choose to itemize even though the standard deduction is larger.”

### 57. `sa.excluded_income`

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Do you file Form 2555 or Form 4563, or have income excluded as a bona fide resident of Puerto Rico?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 20, help 20. Help begins: “Yes if you file Form 2555 or Form 4563, or exclude income as a bona fide resident of Puerto Rico.”

### 58. `sa.line8a`

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`), line 8a

> Eligible home mortgage interest and points on Form 1098, after confirming the debt/use limits do not apply

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 17, help 21. Help begins: “Home mortgage interest and points reported to you on Form 1098, when no debt or use limit applies.”

### 59. `sa.unsupported`

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`)

> Any casualty or theft loss (including a disaster loss added to the standard deduction); a deduction from the Schedule A line 16 list other than gambling losses; a foreign tax or generation-skipping tax deduction; mortgage interest or points not on Form 1098 or subject to the debt or use limits (loan proceeds not all used to buy, build or improve the home, or debt over the limit); or the sales-tax election?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 71, help 42. Help begins: “Yes if you have a casualty or theft loss, a Schedule A line 16 deduction other than gambling losses, a foreign or generation-skipping tax deduction, mortgage interest or points not on Form 1098 or subject to limits, or you elect sales tax.”

### 60. `sa.gifts`

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

### 61. `sa.line1`

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

### 62. `sa.line5a`

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

### 63. `sa.line5b`

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

### 64. `sa.line5c`

Topic: Schedule A — supported itemized deductions and standard comparison (`sa`), line 5c

> Deductible state/local personal property taxes: only taxes based on value alone and imposed on a yearly basis (for a yearly car registration fee based partly on value, only the part based on value), paid in 2025 and assessed before 2026. Include personal property taxes imposed by a U.S. territory, except those allocable to excluded income.

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 55, help 31. Help begins: “State and local personal property taxes you paid in 2025 that were based on value alone and imposed yearly, such as the value-based part of a car fee.”

### 65. `sb.foreign_any`

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

### 66. `sd.carryover`

**⟶ topic switch**

Topic: Schedule D — securities sales and supplied distribution subtotals (`sd`)

> Did line 21 of your 2024 Schedule D show a loss? On a 2025 joint return, answer for your 2024 joint return, or for either spouse's separate 2024 return.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 29, help 0

### 67. `sd.other_forms`

Topic: Schedule D — securities sales and supplied distribution subtotals (`sd`)

> Are there gains or losses from (or that belong on) Forms 4797, 2439, 6252, 4684, 6781 or 8824, or capital gains or losses on a Schedule K-1? Count section 1256 contracts and a casualty or theft of property whether you held the property directly or through an entity.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 48, help 0

### 68. `$sales`

**⟶ topic switch**

Topic: Form 8949 and Schedule D — manually classified securities transactions (`sales`)

> List each sale you report for 2025, one entry per transaction, including transactions intended for aggregate reporting. Leave the list empty only if there were no sales.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (background)
- Words: prompt 27, help 19. Help begins: “Enter each transaction once; the tool decides whether it goes on Form 8949 or in Schedule D aggregate reporting.”

### 69. `sli.interest`

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

### 70. `ssb.benefits`

**⟶ topic switch**

Topic: Social Security Benefits Worksheet—Lines 6a and 6b (`ssb`)

> Total of box 5 (net benefits) of all your Forms SSA-1099 and RRB-1099 for 2025

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 15, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 71. `$sc@person[taxpayer]`

**⟶ topic switch**

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You

> Did you operate a business or practice a profession as a sole proprietor in 2025 (income reported to you on Forms 1099-NEC, 1099-K or 1099-MISC for your own work is usually such a business)? List each such business, one entry per business; leave the list empty if none.

- Offered: a list the filer builds, naming each entry
- Answer: the list `design_studio` (persona)
- Words: prompt 48, help 0

### 72. `$asset@person[taxpayer].sc[design_studio]`

**⟶ topic switch**

Topic: Form 4562 — one item of depreciable property (other than a vehicle) of a business (`asset`). About: You › sc design_studio

> For this business — List each item of property other than a vehicle that you depreciate or expense under section 179 for 2025 (placed in service from 2005 to 2025), one entry per item; leave the list empty if none. Items with a cost you deduct in full as supplies or under a de minimis rule are not listed here.

- Offered: a list the filer builds, naming each entry
- Answer: none (an empty list) (persona)
- Words: prompt 59, help 0

### 73. `$scveh@person[taxpayer].sc[design_studio]`

**⟶ topic switch**

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio

> For this business — List each car, truck or van you used in the business in 2025 and claim expenses for (standard mileage or actual expenses), one entry per vehicle; leave the list empty if none.

- Offered: a list the filer builds, naming each entry
- Answer: the list `hatchback` (persona)
- Words: prompt 35, help 0

### 74. `person[taxpayer].plan`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Did you contribute for yourself, as a self-employed person, to a SEP IRA (sep) or a SIMPLE IRA (simple) for 2025, or to neither (none)?

- Offered: “none” / “sep” / “simple”
- Answer: `none` (persona)
- Words: prompt 25, help 6. Help begins: “One of the values of retire_plan.”

### 75. `person[taxpayer].sc[design_studio].hi_uses`

**⟶ topic switch (returns)**

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> For this business — Did you pay for health insurance for 2025 (for you, your spouse, your dependents, or your child under age 27 at the end of 2025) that is established under this business: a policy in the name of the business or in your own name? Health insurance here includes medical, dental and vision insurance, qualified long-term care insurance, and Medicare premiums you pay voluntarily for insurance in your name. Answer No if your personal services were not a material income-producing factor in this business.

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 86, help 0

### 76. `person[taxpayer].sc[design_studio].ho_uses`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> For this business — Do you claim a deduction for the business use of your home for this business (a part of your home used regularly and exclusively for the business, or regularly for storing inventory or product samples)?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 38, help 0

### 77. `person[taxpayer].sc[design_studio].ho_other`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> For this business — Does any of these apply: you figure the deduction with actual expenses on Form 8829 instead of the simplified method; you used more than one home for this business; the home is used for daycare; you share the business area with someone else's business; you used the area for only part of 2025 or it changed during the year; some of this business's gross income is from a place of business other than your home; you have a gain or loss on Form 8949 or Form 4797 related to this business; or this is not a timely filed, original return for 2025?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 105, help 0

### 78. `person[taxpayer].sc[design_studio].ho_sqft`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 30(b). About: You › sc design_studio

> For this business — The square feet of your home used regularly and exclusively for this business (or regularly for storing inventory or product samples) throughout 2025

- Offered: a whole number
- Answer: 180 (persona)
- Words: prompt 26, help 0

### 79. `person[taxpayer].sc[design_studio].inventory_other`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 33. About: You › sc design_studio

> For this business — Do you value closing inventory by a method other than cost or lower of cost or market, or was there any change in determining quantities, costs or valuations between opening and closing inventory (line 34)? Answer No if you have no inventory

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 45, help 0

### 80. `person[taxpayer].sc[design_studio].line10`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 10. About: You › sc design_studio

> For this business — Commissions and fees of this business for 2025 under your accounting method (with the cash method, the amounts you paid in 2025; with an accrual method, the amounts incurred for 2025), not capitalized and not deducted elsewhere; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 43, help 0

### 81. `person[taxpayer].sc[design_studio].line11`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 11. About: You › sc design_studio

> For this business — The cost of contract labor of this business for 2025 under your accounting method (with the cash method, the amounts you paid in 2025; with an accrual method, the amounts incurred for 2025) for services of independent contractors and others you do not treat as employees (not included on lines 17, 21, 26 or 37); zero if none

- Offered: a dollar amount, zero or more
- Answer: $4,500.00 (persona)
- Words: prompt 61, help 0

### 82. `person[taxpayer].sc[design_studio].line14`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 14. About: You › sc design_studio

> For this business — Contributions to employee benefit programs for your employees, such as accident and health plans, group-term life insurance and dependent care assistance (not for yourself, and not pension or profit-sharing plans); zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 36, help 0

### 83. `person[taxpayer].sc[design_studio].line15`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 15. About: You › sc design_studio

> For this business — Premiums for business insurance (not health insurance for yourself, not a reserve for self-insurance, not lost-earnings insurance, not insurance on a car, truck or van you list for this business, which its car and truck expenses already include under either the standard mileage rate or actual expenses, and not insurance on your home, because with the simplified method for business use of the home, line 30 replaces the business part of your home's expenses); zero if none

- Offered: a dollar amount, zero or more
- Answer: $600.00 (persona)
- Words: prompt 80, help 0

### 84. `person[taxpayer].sc[design_studio].line16a`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 16a. About: You › sc design_studio

> For this business — Interest you paid for 2025 on a mortgage on real property used in the business, to banks or other financial institutions for which you received a Form 1098 (only the business part; not interest that must be capitalized, and not mortgage interest on your home, which with the simplified method for business use of the home you can deduct only on Schedule A); zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 69, help 0

### 85. `person[taxpayer].sc[design_studio].line16b`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 16b. About: You › sc design_studio

> For this business — Other interest on business debt (including mortgage interest not reported on a Form 1098 to you); for a vehicle used for business and personal purposes, only the business part, and none of the interest you deduct on Schedule 1-A; for interest paid in 2025 that also applies to future years, only the part that applies to 2025; for a mortgage on which you and another person (other than your spouse on a joint return) were liable and paid interest and the other person received the Form 1098, only your share; not mortgage interest on your home; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 102, help 0

### 86. `person[taxpayer].sc[design_studio].line17`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 17. About: You › sc design_studio

> For this business — Fees of accountants and attorneys directly related to operating the business, including tax advice and preparation of the business tax forms; zero if none

- Offered: a dollar amount, zero or more
- Answer: $850.00 (persona)
- Words: prompt 27, help 0

### 87. `person[taxpayer].sc[design_studio].line18`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 18. About: You › sc design_studio

> For this business — Office supplies and postage; zero if none

- Offered: a dollar amount, zero or more
- Answer: $420.00 (persona)
- Words: prompt 10, help 0

### 88. `person[taxpayer].sc[design_studio].line19`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 19. About: You › sc design_studio

> For this business — Contributions you made for your employees to a pension, profit-sharing or annuity plan, including SEP, SIMPLE and SARSEP plans (not contributions for yourself, which go on Schedule 1, line 16); zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 36, help 0

### 89. `person[taxpayer].sc[design_studio].line2`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 2. About: You › sc design_studio

> For this business — Returns and allowances (refunds and price reductions you gave customers), as a positive number; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 20, help 0

### 90. `person[taxpayer].sc[design_studio].line20b`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 20b. About: You › sc design_studio

> For this business — Rent for other business property, such as office space (not rent for your home, because with the simplified method for business use of the home, line 30 replaces the business part of your home's expenses); zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 41, help 0

### 91. `person[taxpayer].sc[design_studio].line21`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 21. About: You › sc design_studio

> For this business — Incidental repairs and maintenance that do not add to the property's value or appreciably prolong its life (not your own labor, not restorations or replacements, which are capitalized, not repairs or maintenance of a car, truck or van you list for this business, which its car and truck expenses already include under either the standard mileage rate or actual expenses, and not repairs or maintenance of your home, because with the simplified method for business use of the home, line 30 replaces the business part of your home's expenses); zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 95, help 0

### 92. `person[taxpayer].sc[design_studio].line22`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 22. About: You › sc design_studio

> For this business — Materials and supplies actually consumed and used in the business during 2025 (or incidental supplies purchased during 2025 if you keep no inventory or records of use), and books, professional instruments, equipment and similar items you normally use up within a year; not items whose usefulness extends substantially beyond a year, which you generally depreciate, and not materials and supplies used in producing goods for sale, which are entered in cost of goods sold (Part III); zero if none

- Offered: a dollar amount, zero or more
- Answer: $1,300.00 (persona)
- Words: prompt 82, help 0

### 93. `person[taxpayer].sc[design_studio].line23`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 23. About: You › sc design_studio

> For this business — Business taxes and licenses: sales tax imposed on you as the seller, real estate and personal property taxes on business assets, licenses and regulatory fees paid each year (not licenses you must amortize, such as some liquor licenses, and not license plates for a car, truck or van you list for this business, which its car and truck expenses already include), the employer share of social security and Medicare taxes, federal unemployment tax, federal highway use tax, contributions to a state unemployment insurance fund or a paid family and medical leave program disability benefit fund if they are taxes under state law (not income or self-employment tax, not taxes on property you bought, and not real estate taxes on your home, which with the simplified method for business use of the home you can deduct only on Schedule A); zero if none

- Offered: a dollar amount, zero or more
- Answer: $150.00 (persona)
- Words: prompt 145, help 0

### 94. `person[taxpayer].sc[design_studio].line24a`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 24a. About: You › sc design_studio

> For this business — Lodging and transportation for overnight business travel away from your tax home, and incidental expenses of that travel, as described below; zero if none.
>
> Incidental expenses of that travel:
> - fees and tips to porters, baggage carriers, bellhops, hotel maids, stewards and others on ships, and hotel servants in foreign countries
> - not laundry, cleaning and pressing of clothing, lodging taxes, or the costs of telegrams or telephone calls
> - either at their actual cost or, for a travel day on which you paid or incurred no meal expenses and did not use the standard meal allowance, at $5 for that day (not meals and not entertainment; on a day you use the standard meal allowance, incidental expenses are part of that allowance)
>
> Other limits:
> - not expenses of employment away from home for a period of more than 1 year
> - not travel expenses for your spouse, your dependent or any other person unless that person is your employee, the travel is for a bona fide business purpose and the expenses would otherwise be deductible by that person
> - not a convention, seminar or similar meeting held outside the North American area unless it is directly related to your business and it is as reasonable to hold it outside the North American area as within it

- Offered: a dollar amount, zero or more
- Answer: $950.00 (persona)
- Words: prompt 214, help 0

### 95. `person[taxpayer].sc[design_studio].line25`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 25. About: You › sc design_studio

> For this business — Utility expenses of the business only (for a home phone, not the base rate of the first line into your residence; not utilities of your home, such as electricity, gas, water or heating, because with the simplified method for business use of the home, line 30 replaces the business part of your home's expenses); zero if none

- Offered: a dollar amount, zero or more
- Answer: $720.00 (persona)
- Words: prompt 60, help 0

### 96. `person[taxpayer].sc[design_studio].line26`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 26. About: You › sc design_studio

> For this business — Salaries and wages of your employees for 2025 under your accounting method (with the cash method, the amounts you paid in 2025; with an accrual method, the amounts incurred for 2025) (not amounts paid to yourself, not wages deducted elsewhere, and not the part of a taxable fringe benefit, such as personal use of a car, that is depreciation or other expenses you claim elsewhere); zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 71, help 0

### 97. `person[taxpayer].sc[design_studio].line35`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 35. About: You › sc design_studio

> For this business — Inventory at the beginning of 2025 (the same as your closing inventory for 2024); zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 20, help 0

### 98. `person[taxpayer].sc[design_studio].line36`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 36. About: You › sc design_studio

> For this business — Purchases of merchandise or materials for sale, less the cost of items you withdrew for personal use; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 23, help 0

### 99. `person[taxpayer].sc[design_studio].line37`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 37. About: You › sc design_studio

> For this business — Cost of labor for producing goods for sale (not amounts paid to yourself); zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 19, help 0

### 100. `person[taxpayer].sc[design_studio].line38`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 38. About: You › sc design_studio

> For this business — Materials and supplies used in producing goods for sale; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 15, help 0

### 101. `person[taxpayer].sc[design_studio].line39`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 39. About: You › sc design_studio

> For this business — Other costs of goods sold; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 11, help 0

### 102. `person[taxpayer].sc[design_studio].line41`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 41. About: You › sc design_studio

> For this business — Inventory at the end of 2025; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 12, help 0

### 103. `person[taxpayer].sc[design_studio].line48`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 48. About: You › sc design_studio

> For this business — The total of the other business expenses you list in Part V, not included on lines 8 to 27a or line 30; zero if none

- Offered: a dollar amount, zero or more
- Answer: $2,400.00 (persona)
- Words: prompt 28, help 0

### 104. `person[taxpayer].sc[design_studio].line6`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 6. About: You › sc design_studio

> For this business — Other business income not in gross receipts, such as scrap sales, bad debts you recovered, interest on accounts receivable, state gasoline or fuel tax refunds, the credit for federal tax paid on fuels claimed on your 2024 Form 1040 or 1040-SR, sales tax the state or local government allowed you to retain, prizes and awards related to the business, and Form 1099-PATR amounts; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 69, help 0

### 105. `person[taxpayer].sc[design_studio].line8`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 8. About: You › sc design_studio

> For this business — Advertising expenses of this business; zero if none

- Offered: a dollar amount, zero or more
- Answer: $1,100.00 (persona)
- Words: prompt 11, help 0

### 106. `person[taxpayer].sc[design_studio].meals_100`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> For this business — The cost of meals and incidentals not subject to the 50% limit, deducted in full: meals furnished or reimbursed to an employee and treated as wages subject to withholding; meals provided to a nonemployee, to the extent includible in their income and reported on Form 1099-NEC; meals a customer or client reimbursed you for, as an independent contractor, after you gave them adequate records; recreational, social or similar activities for your employees (such as a holiday party or a summer picnic); food and beverages provided to the general public as advertising or to promote goodwill; meals you sell to the public; and, if you run a daycare, the food consumed by the children in your care (actual cost or, for eligible children in family daycare, the standard meal and snack rates; not food consumed by you or your family), less any reimbursement under a food program of the Department of Agriculture. Don't include anything entered elsewhere on this Schedule C (for example, in cost of goods sold); zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 173, help 0

### 107. `person[taxpayer].sc[design_studio].meals_50`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> For this business — The full cost of business meals (actual cost or the standard meal allowance) subject to the 50% limit, before applying the percentage: meals while you or your employees travel away from home on business, including your employees' travel meals you pay for or reimburse other than as wages; and meals with a current or potential business customer, client, consultant or similar business contact that were ordinary and necessary in your business, not lavish or extravagant, with you or your employee present, and, at an entertainment event, bought separately from the entertainment or stated separately on the bill. Do not include entertainment, meals during a period of duty under the Department of Transportation hours of service limits, or food for the children in your daycare, which are asked about separately; zero if none

- Offered: a dollar amount, zero or more
- Answer: $360.00 (persona)
- Words: prompt 135, help 0

### 108. `person[taxpayer].sc[design_studio].meals_80`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> For this business — The full cost of business meals consumed by you or your employees during or incident to a period of duty for which the person who ate the meal was subject to the Department of Transportation hours of service limits (certain air transportation workers, interstate truck operators, certain merchant mariners), including your employees' duty meals you pay for or reimburse other than as wages, before applying the percentage; zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 73, help 0

### 109. `person[taxpayer].sc[design_studio].method_other`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), F. About: You › sc design_studio

> For this business — Do you use an accounting method other than cash or accrual, or did you change your accounting method for 2025 (Form 3115 or a section 481(a) adjustment), or must you capitalize costs under the uniform capitalization rules (section 263A) because your average annual gross receipts for the 3 prior years were more than $31 million, or is this business a tax shelter (as defined in section 448(d)(3)), or does it have long-term contracts (section 460)?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 78, help 0

### 110. `person[taxpayer].sc[design_studio].passive`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), G. About: You › sc design_studio

> For this business — Did you "materially participate" in the operation of this business during 2025 (for example, you worked in it more than 500 hours, or your work was substantially all the work done in it, or more than 100 hours and at least as much as anyone else; see the seven tests in the instructions for line G), or is it a working interest in an oil or gas well you own directly or through an entity that does not limit your liability (the exception for oil and gas), and is the business something other than a rental activity?

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 100, help 0

### 111. `person[taxpayer].sc[design_studio].rent_equipment`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> For this business — The business part of rent for machinery and equipment (and for any vehicle you rented for a term of less than 30 days and do not enter as a vehicle); zero if none

- Offered: a dollar amount, zero or more
- Answer: $0.00 (persona)
- Words: prompt 36, help 0

### 112. `person[taxpayer].sc[design_studio].scveh[hatchback].method`

**⟶ topic switch (returns)**

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh hatchback

> For this vehicle — For this vehicle, do you take the standard mileage rate (standard) or deduct actual expenses (actual)?

- Offered: “standard” / “actual”
- Answer: `standard` (persona)
- Words: prompt 19, help 6. Help begins: “One of the values of vehicle_method.”

### 113. `person[taxpayer].sc[design_studio].scveh[hatchback].parking`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh hatchback

> For this vehicle — Parking fees and tolls for this vehicle's business use in 2025 (zero if none)

- Offered: a dollar amount, zero or more
- Answer: $210.00 (persona)
- Words: prompt 17, help 0

### 114. `person[taxpayer].sc[design_studio].scveh[hatchback].smr_ok`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`). About: You › sc design_studio › scveh hatchback

> For this vehicle — If you own this vehicle: did you use the standard mileage rate for it in the first year you used it for business? If you lease it: are you using the standard mileage rate for the entire lease period? (Answer No if this is one of five or more vehicles you used in the business at the same time.)

- Offered: Yes / No
- Answer: Yes (persona)
- Words: prompt 62, help 0

### 115. `person[taxpayer].sc[design_studio].scveh[hatchback].miles_business`

Topic: Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business (`scveh`), line 44a. About: You › sc design_studio › scveh hatchback

> For this vehicle — The miles you drove this vehicle in 2025 for this business (not commuting)

- Offered: a whole number
- Answer: 4200 (persona)
- Words: prompt 16, help 0

### 116. `person[taxpayer].sc[design_studio].special`

**⟶ topic switch (returns)**

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> For this business — For this business, do you have any of these?
>
> - depletion (line 12)
> - the energy efficient commercial buildings deduction (Form 7205)
> - wages or benefits reduced by an employment credit (Forms 5884, 8844, 8846, 8932, 8941 or 8994)
> - business interest limited by Form 8990
> - recapture of depreciation or section 179 on listed property, recapture of section 179 on other property no longer used more than 50% in the business, or an inclusion amount for leased property
> - a chapter 11 bankruptcy case
> - extraterritorial income (Form 8873)
> - income you report under the installment method (including installment sales of timeshares or residential lots)
> - nontaxable Medicaid waiver payments (Notice 2014-7)
> - research or experimental expenditures you elect to capitalize
> - a capital construction fund
> - contributions you made on your own behalf, as a self-employed person, to a dependent care assistance program (Form 2441, Parts I and III)
> - qualified sound recording production costs you elect to deduct under section 181
> - prior year unallowed passive activity losses from this activity
> - services you provide to a business that employed you within the last 3 years, substantially the same as the services you provided as its employee
> - Form 1099-PATR amounts in this business's income that the cooperative did not report to you as qualified items of income
> - an activity that is not a business (for example a sporadic activity, a not-for-profit activity or a hobby)
> - licenses or other costs you must amortize (for example, some liquor licenses)
> - travel by ocean liner, cruise ship or other luxury water transportation
> - a domestic LLC of which you are the sole member that elected to be treated as a corporation

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 267, help 0

### 117. `person[taxpayer].sc[design_studio].spouse_owned`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> For this business — Do you own this business together with your spouse (as a qualified joint venture, as community property, or as partners)?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 23, help 0

### 118. `person[taxpayer].sc[design_studio].statutory`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> For this business — Is this business income you received as a statutory employee (the "Statutory employee" box in box 13 of your Form W-2 was checked), or fees you received as a notary public?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 34, help 0

### 119. `person[taxpayer].sc[design_studio].business_credit`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> For this business — Does this business claim any business tax credit, for example for research, for starting a retirement plan, or for making the premises accessible?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 26, help 36. Help begins: “Business credits are claimed on Form 3800.”

### 120. `person[taxpayer].sc[design_studio].fuel_credit`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> For this business — Did this business use gasoline, diesel or another taxed fuel off the road, such as in equipment or a boat, and want the federal fuel tax back?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 30, help 22. Help begins: “The credit is claimed on Form 4136.”

### 121. `person[taxpayer].sc[design_studio].line1`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`), line 1. About: You › sc design_studio

> For this business — Gross receipts or sales of this business for 2025, including amounts properly shown on Forms 1099-NEC and any other gross receipts of this business reported to you on a Form 1099 (such as Form 1099-K), and state and local sales tax imposed on you as the seller that you collected from buyers; not the other business income asked about separately, such as prizes and awards, and not royalties or other name, image and likeness (NIL) income that is not self-employment income, which is reported on Schedule E (zero if none)

- Offered: a dollar amount, zero or more
- Answer: $88,000.00 (persona)
- Words: prompt 93, help 0

### 122. `person[taxpayer].sc[design_studio].tips_ot`

Topic: Schedule C (Form 1040) — Profit or Loss From Business, one per business (`sc`). About: You › sc design_studio

> For this business — Does this business's income include qualified tips you received in the course of this business, or qualified overtime compensation reported to you on Form 1099-NEC or 1099-MISC, that you would deduct on Schedule 1-A?

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 37, help 0

### 123. `s1a.overtime`

**⟶ topic switch (returns)**

Topic: Schedule 1-A (Form 1040) — Additional Deductions (`s1a`)

> Did you receive overtime pay as an employee in 2025 that you want to deduct on Schedule 1-A, Part III (the FLSA Overtime Premium, generally the "half" of time-and-a-half)? (Overtime reported on Form 1099-NEC or 1099-MISC is asked about with Schedule C.)

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 42, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 124. `s1a.tips`

Topic: Schedule 1-A (Form 1040) — Additional Deductions (`s1a`)

> Did you receive tips as an employee in 2025 in an occupation on the IRS list of occupations that customarily and regularly received tips (IRS.gov/TippedOccupations) that you want to deduct on Schedule 1-A, Part II? (Tips received as a non-employee, in your own trade or business, are asked about with Schedule C.)

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 52, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 125. `person[taxpayer].se_screen`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Does any of these apply to you?
>
> - church employee income (wages from a church or qualified church-controlled organization that elected exemption from social security and Medicare taxes)
> - being a minister, a member of a religious order or a Christian Science practitioner, or having an approved Form 4361 or Form 4029
> - net earnings from self-employment from a partnership (Schedule K-1, box 14, code A) or other self-employment income not on a Schedule C (such as director's fees, fiduciary fees, or fees as a fee-basis state or local government employee)
> - farm income (Schedule F) or Conservation Reserve Program payments
> - electing an optional method (Schedule SE Part II)
> - a chapter 11 bankruptcy case
> - community income on a separate return
> - self-employment income exempt under an international social security agreement or earned as a U.S. citizen employed by a foreign government
> - tips reported on Form 4137 or wages on Form 8919

- Offered: Yes / No
- Answer: No (persona)
- Words: prompt 146, help 0

### 126. `s179.line10`

**⟶ topic switch**

Topic: Form 4562, Part I — Election To Expense Certain Property Under Section 179 (Summary for the return) (`s179`), line 10

> The carryover of disallowed section 179 deduction from line 13 of your (and, on a joint return, your spouse's) 2024 Form 4562 (zero if none). If you did not file a 2024 Form 4562 (it is required only when a deduction is claimed), use line 13 of the last Form 4562 you filed (section 179 cost elected in an earlier year and not yet allowed because of the business income limit carries over until it is deducted)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 77, help 0

### 127. `f2441.benefits`

**⟶ topic switch**

Topic: Form 2441 — Child and Dependent Care Expenses (Parts I to III) (`f2441`)

> Did you (or your spouse, if filing jointly) receive dependent care benefits for 2025 — amounts shown in box 10 of a Form W-2, or an amount from your 2024 dependent care plan that you used in 2025 during a grace period?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 41, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 128. `f2441.care`

Topic: Form 2441 — Child and Dependent Care Expenses (Parts I to III) (`f2441`)

> In 2025, did you pay for, or incur expenses for, the care of a qualifying person so that you (and your spouse) could work or look for work? A qualifying person is your child under age 13; your spouse who was not able to care for themselves; or any other person who was not able to care for themselves, lived with you for more than half of 2025, and is your dependent or would be except that they had gross income of $5,200 or more, they filed a joint return, or you could be claimed as a dependent on someone else's 2025 return. Include 2024 care you paid for in 2025 and 2025 care you will pay for in 2026.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 120, help 10. Help begins: “Married filing separately and unsupported items are refused with citations.”

### 129. `person[taxpayer].sav_trad`

**⟶ topic switch (returns)**

Topic: Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others) (`person`). About: You

> Did you make contributions (other than rollover contributions) to a traditional IRA for 2025, deductible or not, including contributions made by the due date of your 2025 return for 2025? Do not count contributions made under a SEP or SIMPLE IRA plan, including those you made for yourself as a self-employed person.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 52, help 79. Help begins: “Contributions to a traditional IRA for 2025, which may be made until April 15, 2026.”

### 130. `qbi.unsupported`

**⟶ topic switch**

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`)

> Do you have any of these: qualified business income or loss, or PTP income or loss, other than section 199A dividends and the Schedule C businesses entered in this tool; a prior-year REIT or PTP loss carryforward, or losses or deductions suspended in an earlier year by another provision and allowed this year; or are you a patron of any agricultural or horticultural cooperative, specified or not (including any qualified payments from one on Form 1099-PATR)?

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 76, help 34. Help begins: “Yes if you have qualified business or PTP income or loss other than section 199A dividends and your Schedule C businesses, a prior-year REIT or PTP loss carryforward, or agricultural cooperative patronage (Form 1099-PATR).”

### 131. `qbi.carryforward`

Topic: Qualified business income and section 199A dividends — amounts and the choice of Form 8995 (`qbi`), line 3

> The qualified business loss carryforward from line 16 of your 2024 Form 8995 (or the corresponding line of your 2024 Form 8995-A), entered as a positive amount (zero if none)

- Offered: a dollar amount, zero or more
- Answer: $0.00 (background)
- Words: prompt 30, help 0

### 132. `f5695.part1_any`

**⟶ topic switch**

Topic: Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`)

> Did you have 2025 costs for solar electric, solar water heating, small wind energy, geothermal heat pump, battery storage or fuel cell property for a home in the United States, or a residential clean energy credit carryforward from line 16 of a 2024 Form 5695? Include your proportionate share of such costs paid by the condominium management association of a condominium you own, or by a cooperative housing corporation in which you are a tenant-stockholder. A cost of an item counts in 2025 when its original installation is completed in 2025, whenever it was paid; but a cost connected with constructing or reconstructing a home counts when your original use of that home begins (for example, solar panels installed in 2024 on a newly built home you first lived in in 2025 count in 2025). An item installed after 2025 does not qualify.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 143, help 14. Help begins: “Answer Yes also if the only Part I amount is a carryforward from 2024.”

### 133. `f5695.part2_any`

Topic: Form 5695 — Residential Energy Credits (Parts I and II) (`f5695`)

> Did you have 2025 costs for insulation or air sealing, exterior doors, exterior windows or skylights, central air conditioners, natural gas, propane or oil water heaters, furnaces or hot water boilers, electric or natural gas heat pumps or heat pump water heaters, biomass stoves or boilers, panelboards, subpanelboards, branch circuits or feeders, or a home energy audit, for a home in the United States? Include your proportionate share of such costs paid by the condominium management association of a condominium you own, or by a cooperative housing corporation in which you are a tenant-stockholder. A cost of an item counts in 2025 when its original installation is completed in 2025 (for a cost connected with the reconstruction of your home, when your original use of the reconstructed home begins), whenever it was paid; an item installed after 2025 does not qualify.

- Offered: Yes / No
- Answer: No (background)
- Words: prompt 141, help 11. Help begins: “There is no carryforward of this credit from an earlier year.”

## The end reached

**Complete.** The return is completed after 133 questions.

## Totals

| | |
|---|---|
| Questions asked | 133 |
| Answered by the persona / by the background / opened and unanswered | 56 / 77 / 0 |
| Prompt words | 9905 |
| Help words (optional to read) | 2360 |
| Words of the answers offered (Yes and No not counted) | 79 |
| Questions answered no, zero or none | 108 |
| Topics met | 34 |
| Topic switches | 49 |
| of them, returns to a topic already left | 16 |

## The 10 longest prompts met

| # | Question | Prompt words | Answer |
|---|---|---|---|
| 65 | `sb.foreign_any` | 827 | No |
| 61 | `sa.line1` | 429 | $0.00 |
| 4 | `scope.schedule1` | 293 | No |
| 60 | `sa.gifts` | 292 | No |
| 116 | `person[taxpayer].sc[design_studio].special` | 267 | No |
| 69 | `sli.interest` | 244 | $0.00 |
| 62 | `sa.line5a` | 237 | $0.00 |
| 63 | `sa.line5b` | 232 | $0.00 |
| 9 | `household.married` | 217 | No |
| 17 | `div.any` | 217 | No |

## The whole walk, one line per question

Number, question id, prompt words, answer. `>` begins a new topic (`>>` a return to a topic already left), named at the right; `*` marks the persona's own answer, `!` an opened and unanswered question.

```
> *  1  $person                                                       6w  ["taxpayer"]                  [person]
> *  2  f1040.status                                                  9w  "single"                      [f1040]
>    3  scope.other_line16                                          182w  false                         [scope]
     4  scope.schedule1                                             293w  false
     5  scope.other_income                                          188w  false
>    6  $f1095a                                                      45w  []                            [f1095a]
>    7  $retirement@person[taxpayer]                                 22w  []                            [retirement]
>    8  $dependent                                                   28w  []                            [dependent]
>    9  household.married                                           217w  false                         [household]
    10  household.spouse_died_2025                                   29w  false
>>  11  person[taxpayer].under16                                     10w  false                         [person]
>>  12  household.community_property                                 24w  false                         [household]
>   13  s3.adoption_any                                              16w  false                         [s3]
>   14  $w2@person[taxpayer]                                         32w  []                            [w2]
>   15  $interest                                                    19w  []                            [interest]
>   16  $f8889@person[taxpayer]                                      15w  []                            [f8889]
>   17  div.any                                                     217w  false                         [div]
>>  18  f1040.line25b                                                35w  0                             [f1040]
    19  f1040.line25c_other                                          29w  0
  * 20  f1040.line26                                                 15w  1200000
>   21  f4952.has_interest                                          204w  false                         [f4952]
    22  f4952.line4g                                                 83w  0
>   23  f8863.paid                                                   37w  false                         [f8863]
>   24  f8959.unsupported                                            67w  false                         [f8959]
>   25  ftc.taxes                                                    17w  0                             [ftc]
>>  26  person[taxpayer].age65                                        7w  false                         [person]
    27  person[taxpayer].educator_expenses                          104w  0
    28  person[taxpayer].rrta                                        23w  false
>   29  refund.received                                              62w  0                             [refund]
>   30  s1.alimony                                                   95w  false                         [s1]
    31  s1.line8_other                                              189w  false
>   32  $oi8z                                                        23w  []                            [oi8z]
>>  33  s1.cod_any                                                   27w  false                         [s1]
    34  s1.gambling_winnings                                         61w  0
    35  s1.line8g                                                    40w  0
    36  s1.line8h                                                    24w  0
    37  s1.line8i                                                    78w  0
    38  s1.line8j                                                    42w  0
    39  s1.line8r                                                    50w  0
    40  s1.uc_paid                                                   25w  0
>   41  s1a.carloan                                                  40w  false                         [s1a]
>   42  s2.amt                                                       17w  false                         [s2]
    43  s2.other                                                    124w  false
>>  44  person[taxpayer].x_other                                    136w  false                         [person]
>>  45  s3.credit_bond                                               16w  false                         [s3]
    46  s3.disability_retired                                         8w  false
    47  s3.ev                                                        22w  false
    48  s3.farmland                                                   6w  false
    49  s3.foreign_any                                               24w  false
    50  s3.kerosene                                                  13w  false
    51  s3.line10                                                    40w  0
    52  s3.prior_other_forms                                         25w  false
    53  s3.repaid_income                                             19w  false
>   54  sa.dependent                                                 48w  false                         [sa]
>>  55  person[taxpayer].blind                                      119w  false                         [person]
>>  56  sa.elect_itemize                                             10w  false                         [sa]
    57  sa.excluded_income                                           20w  false
    58  sa.line8a                                                    17w  0
    59  sa.unsupported                                               71w  false
    60  sa.gifts                                                    292w  false
    61  sa.line1                                                    429w  0
    62  sa.line5a                                                   237w  0
    63  sa.line5b                                                   232w  0
    64  sa.line5c                                                    55w  0
>   65  sb.foreign_any                                              827w  false                         [sb]
>   66  sd.carryover                                                 29w  false                         [sd]
    67  sd.other_forms                                               48w  false
>   68  $sales                                                       27w  []                            [sales]
>   69  sli.interest                                                244w  0                             [sli]
>   70  ssb.benefits                                                 15w  0                             [ssb]
> * 71  $sc@person[taxpayer]                                         48w  ["design_studio"]             [sc]
> * 72  $asset@person[taxpayer].sc[design_studio]                    59w  []                            [asset]
> * 73  $scveh@person[taxpayer].sc[design_studio]                    35w  ["hatchback"]                 [scveh]
>>* 74  person[taxpayer].plan                                        25w  "none"                        [person]
>>* 75  person[taxpayer].sc[design_studio].hi_uses                   86w  false                         [sc]
  * 76  person[taxpayer].sc[design_studio].ho_uses                   38w  true
  * 77  person[taxpayer].sc[design_studio].ho_other                 105w  false
  * 78  person[taxpayer].sc[design_studio].ho_sqft                   26w  180
  * 79  person[taxpayer].sc[design_studio].inventory_other           45w  false
  * 80  person[taxpayer].sc[design_studio].line10                    43w  0
  * 81  person[taxpayer].sc[design_studio].line11                    61w  450000
  * 82  person[taxpayer].sc[design_studio].line14                    36w  0
  * 83  person[taxpayer].sc[design_studio].line15                    80w  60000
  * 84  person[taxpayer].sc[design_studio].line16a                   69w  0
  * 85  person[taxpayer].sc[design_studio].line16b                  102w  0
  * 86  person[taxpayer].sc[design_studio].line17                    27w  85000
  * 87  person[taxpayer].sc[design_studio].line18                    10w  42000
  * 88  person[taxpayer].sc[design_studio].line19                    36w  0
  * 89  person[taxpayer].sc[design_studio].line2                     20w  0
  * 90  person[taxpayer].sc[design_studio].line20b                   41w  0
  * 91  person[taxpayer].sc[design_studio].line21                    95w  0
  * 92  person[taxpayer].sc[design_studio].line22                    82w  130000
  * 93  person[taxpayer].sc[design_studio].line23                   145w  15000
  * 94  person[taxpayer].sc[design_studio].line24a                  214w  95000
  * 95  person[taxpayer].sc[design_studio].line25                    60w  72000
  * 96  person[taxpayer].sc[design_studio].line26                    71w  0
  * 97  person[taxpayer].sc[design_studio].line35                    20w  0
  * 98  person[taxpayer].sc[design_studio].line36                    23w  0
  * 99  person[taxpayer].sc[design_studio].line37                    19w  0
  *100  person[taxpayer].sc[design_studio].line38                    15w  0
  *101  person[taxpayer].sc[design_studio].line39                    11w  0
  *102  person[taxpayer].sc[design_studio].line41                    12w  0
  *103  person[taxpayer].sc[design_studio].line48                    28w  240000
  *104  person[taxpayer].sc[design_studio].line6                     69w  0
  *105  person[taxpayer].sc[design_studio].line8                     11w  110000
  *106  person[taxpayer].sc[design_studio].meals_100                173w  0
  *107  person[taxpayer].sc[design_studio].meals_50                 135w  36000
  *108  person[taxpayer].sc[design_studio].meals_80                  73w  0
  *109  person[taxpayer].sc[design_studio].method_other              78w  false
  *110  person[taxpayer].sc[design_studio].passive                  100w  true
  *111  person[taxpayer].sc[design_studio].rent_equipment            36w  0
>>*112  person[taxpayer].sc[design_studio].scveh[hatchback].method   19w  "standard"                    [scveh]
  *113  person[taxpayer].sc[design_studio].scveh[hatchback].parking   17w  21000
  *114  person[taxpayer].sc[design_studio].scveh[hatchback].smr_ok   62w  true
  *115  person[taxpayer].sc[design_studio].scveh[hatchback].miles_business   16w  4200
>>*116  person[taxpayer].sc[design_studio].special                  267w  false                         [sc]
  *117  person[taxpayer].sc[design_studio].spouse_owned              23w  false
  *118  person[taxpayer].sc[design_studio].statutory                 34w  false
  *119  person[taxpayer].sc[design_studio].business_credit           26w  false
  *120  person[taxpayer].sc[design_studio].fuel_credit               30w  false
  *121  person[taxpayer].sc[design_studio].line1                     93w  8800000
  *122  person[taxpayer].sc[design_studio].tips_ot                   37w  false
>> 123  s1a.overtime                                                 42w  false                         [s1a]
   124  s1a.tips                                                     52w  false
>>*125  person[taxpayer].se_screen                                  146w  false                         [person]
>  126  s179.line10                                                  77w  0                             [s179]
>  127  f2441.benefits                                               41w  false                         [f2441]
   128  f2441.care                                                  120w  false
>> 129  person[taxpayer].sav_trad                                    52w  false                         [person]
>  130  qbi.unsupported                                              76w  false                         [qbi]
   131  qbi.carryforward                                             30w  0
>  132  f5695.part1_any                                             143w  false                         [f5695]
   133  f5695.part2_any                                             141w  false
```
