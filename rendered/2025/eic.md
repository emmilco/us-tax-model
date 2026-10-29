# Earned Income Credit (EIC)—Steps 1 to 6 and Worksheet A—Line 27a

- Document: `eic` (worksheet, tax year 2025)
- Note: The eligibility steps of the Form 1040 instructions (pp. 40–43) as helper lines, in the order the flow chart asks them, and Worksheet A (p. 46) as printed lines 1 to 6. Worksheet B (self-employment, clergy, church employees, statutory employees) is refused with citations; married filers who file separately or as head of household answer Step 3, questions 4 and 5; a filer whose income is at or above the largest Step 1 limit for the filing status stops before any person is counted.

## (helper) — `eic.qc_of_another`

- **Authored helper label:** Could you be a qualifying child of another person for 2025?
- **Encoded (Bool):** Input — Could you be a qualifying child of another person for 2025? Answer no if the other person isn't required to file, and isn't filing, a 2025 tax return or is filing a 2025 return only to claim a refund of withheld income tax or estimated tax paid.
- Expr: `{"op":"input","source":"Could you be a qualifying child of another person for 2025? Answer no if the other person isn't required to file, and isn't filing, a 2025 tax return or is filing a 2025 return only to claim a refund of withheld income tax or estimated tax paid."}`
- Cite: [i1040gi] p. 41, Step 3, question 6, and p. 42, Step 4, question 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.age_range_count`

- **Authored helper label:** Number of people on the return born after December 31, 1960, and before January 2, 2001
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Were you born before January 2, 2001?" = true and helper "Were you born after December 31, 1960?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"all":[{"eq":["person.born_before_2001",{"const":true}],"op":"test"},{"eq":["person.born_after_1960",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] p. 41, Step 4, question 2, "Were you, or your spouse if filing a joint return, at least age 25 but under age 65 at the end of 2025? (Check 'Yes' if you, or your spouse if filing a joint return, were born after December 31, 1960, and before January 2, 2001.)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.age_range`

- **Authored helper label:** You, or your spouse if filing a joint return, were at least age 25 but under age 65 at the end of 2025
- **Encoded (Bool):** helper "Number of people on the return born after December 31, 1960, and before January 2, 2001" > 0 (a count)
- Expr: `{"gt":["eic.age_range_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 41, Step 4, question 2, "Were you, or your spouse if filing a joint return, at least age 25 but under age 65 at the end of 2025?" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.us_home`

- **Authored helper label:** Was your main home, and your spouse's if filing a joint return, in the United States for more than half of 2025?
- **Encoded (Bool):** Input — Was your main home, and your spouse's if filing a joint return, in the United States (the 50 states and the District of Columbia) for more than half of 2025? If you were on extended active military duty outside the United States, that time counts as a main home in the United States.
- Expr: `{"op":"input","source":"Was your main home, and your spouse's if filing a joint return, in the United States (the 50 states and the District of Columbia) for more than half of 2025? If you were on extended active military duty outside the United States, that time counts as a main home in the United States."}`
- Cite: [i1040gi] p. 42, Step 4, question 3; p. 44, Members of the military; p. 45, United States (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.zero`

- **Authored helper label:** No amount
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i1040gi] p. 42, Step 5, worksheet lines 2 and 4 (zero in this tool) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.qc_count`

- **Authored helper label:** Number of qualifying children for the EIC
- **Encoded (Count):** Add dependent.one over every confirmed dependent entry for which helper "Qualifying child for the EIC (relationship, age, not filing a joint return, lived with you in the United States for more than half of 2025)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"dependent","field":"dependent.one","op":"sum_over","where":{"eq":["dependent.eic_child",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 41, Step 3, question 1, "Do you have at least one child who meets the conditions to be your qualifying child for the purpose of claiming the EIC?" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.ssn_count`

- **Authored helper label:** Number of qualifying children for the EIC who have valid SSNs
- **Encoded (Count):** Add dependent.one over every confirmed dependent entry for which helper "Qualifying child for the EIC who has a valid SSN" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"dependent","field":"dependent.one","op":"sum_over","where":{"eq":["dependent.eic_ssn_child",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 40, Step 1, question 1, "children who have valid SSNs lived with you"; p. 46, Worksheet A, line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.has_qc`

- **Authored helper label:** At least one qualifying child for the EIC
- **Encoded (Bool):** helper "Number of qualifying children for the EIC" > 0 (a count)
- Expr: `{"gt":["eic.qc_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 41, Step 3, question 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.married_rules`

- **Authored helper label:** A married filer whose filing status is married filing separately or head of household
- **Encoded (Bool):** (f1040 line Filing Status = 'mfs' or f1040 line Filing Status = 'hoh' and household helper "Were you married at the end of 2025?" = true)
- Expr: `{"any":[{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},{"all":[{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},{"eq":["household.married",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 41, Step 3, question 3, and Step 4, question 1, "Are you a married taxpayer whose filing status is married filing separately or head of household?" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.top_limit`

- **Authored helper label:** Largest Step 1 income limit for the filing status (three or more children)
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → helper "Step 1 and Step 5 limit, 3 or more children"] [f1040 line Filing Status = 'mfj' → helper "Step 1 and Step 5 limit, 3 or more children, married filing jointly"] [f1040 line Filing Status = 'mfs' → helper "Step 1 and Step 5 limit, 3 or more children"] [f1040 line Filing Status = 'hoh' → helper "Step 1 and Step 5 limit, 3 or more children"] [f1040 line Filing Status = 'qss' → helper "Step 1 and Step 5 limit, 3 or more children"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"eic.limit3_other"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"eic.limit3_joint"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"eic.limit3_other"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"eic.limit3_other"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"eic.limit3_other"}],"op":"choose"}`
- Cite: [i1040gi] p. 40, Step 1, question 1, "3 or more children ... less than $61,555 ($68,675 if married filing jointly)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.below_top`

- **Authored helper label:** Adjusted gross income below the largest Step 1 limit (otherwise question 1 is "No" for any number of children)
- **Encoded (Bool):** f1040 line 11b < helper "Largest Step 1 income limit for the filing status (three or more children)"
- Expr: `{"lt":["f1040.line11b","eic.top_limit"],"op":"test"}`
- Cite: [i1040gi] p. 40, Step 1, question 1 (each limit for fewer children is lower than the limit for 3 or more children) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.limit0_other`

- **Authored helper label:** Step 1 and Step 5 limit, no children
- **Encoded (NonNegDollars):** Enter $19,104 (eic.limit0.other).
- Expr: `{"op":"param","ref":"eic.limit0.other"}`
- Cite: [i1040gi] p. 40, Step 1, question 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.limit1_other`

- **Authored helper label:** Step 1 and Step 5 limit, 1 child
- **Encoded (NonNegDollars):** Enter $50,434 (eic.limit1.other).
- Expr: `{"op":"param","ref":"eic.limit1.other"}`
- Cite: [i1040gi] p. 40, Step 1, question 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.limit2_other`

- **Authored helper label:** Step 1 and Step 5 limit, 2 children
- **Encoded (NonNegDollars):** Enter $57,310 (eic.limit2.other).
- Expr: `{"op":"param","ref":"eic.limit2.other"}`
- Cite: [i1040gi] p. 40, Step 1, question 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.limit3_other`

- **Authored helper label:** Step 1 and Step 5 limit, 3 or more children
- **Encoded (NonNegDollars):** Enter $61,555 (eic.limit3.other).
- Expr: `{"op":"param","ref":"eic.limit3.other"}`
- Cite: [i1040gi] p. 40, Step 1, question 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.limit0_joint`

- **Authored helper label:** Step 1 and Step 5 limit, no children, married filing jointly
- **Encoded (NonNegDollars):** Enter $26,214 (eic.limit0.joint).
- Expr: `{"op":"param","ref":"eic.limit0.joint"}`
- Cite: [i1040gi] p. 40, Step 1, question 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.limit1_joint`

- **Authored helper label:** Step 1 and Step 5 limit, 1 child, married filing jointly
- **Encoded (NonNegDollars):** Enter $57,554 (eic.limit1.joint).
- Expr: `{"op":"param","ref":"eic.limit1.joint"}`
- Cite: [i1040gi] p. 40, Step 1, question 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.limit2_joint`

- **Authored helper label:** Step 1 and Step 5 limit, 2 children, married filing jointly
- **Encoded (NonNegDollars):** Enter $64,430 (eic.limit2.joint).
- Expr: `{"op":"param","ref":"eic.limit2.joint"}`
- Cite: [i1040gi] p. 40, Step 1, question 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.limit3_joint`

- **Authored helper label:** Step 1 and Step 5 limit, 3 or more children, married filing jointly
- **Encoded (NonNegDollars):** Enter $68,675 (eic.limit3.joint).
- Expr: `{"op":"param","ref":"eic.limit3.joint"}`
- Cite: [i1040gi] p. 40, Step 1, question 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.limit_other`

- **Authored helper label:** Step 1 and Step 5 limit by the number of qualifying children with valid SSNs
- **Encoded (NonNegDollars):** Choose — [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 0 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 1 (a count) → helper "Step 1 and Step 5 limit, no children"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 1 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 2 (a count) → helper "Step 1 and Step 5 limit, 1 child"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 2 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 3 (a count) → helper "Step 1 and Step 5 limit, 2 children"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 3 (a count) → helper "Step 1 and Step 5 limit, 3 or more children"]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["eic.ssn_count",{"const":0,"type":"Count"}],"op":"test"},{"lt":["eic.ssn_count",{"const":1,"type":"Count"}],"op":"test"}],"op":"test"},"then":"eic.limit0_other"},{"guard":{"all":[{"ge":["eic.ssn_count",{"const":1,"type":"Count"}],"op":"test"},{"lt":["eic.ssn_count",{"const":2,"type":"Count"}],"op":"test"}],"op":"test"},"then":"eic.limit1_other"},{"guard":{"all":[{"ge":["eic.ssn_count",{"const":2,"type":"Count"}],"op":"test"},{"lt":["eic.ssn_count",{"const":3,"type":"Count"}],"op":"test"}],"op":"test"},"then":"eic.limit2_other"},{"guard":{"ge":["eic.ssn_count",{"const":3,"type":"Count"}],"op":"test"},"then":"eic.limit3_other"}],"op":"choose"}`
- Cite: [i1040gi] p. 40, Step 1, question 1, and p. 42, Step 5, question 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.limit_joint`

- **Authored helper label:** Step 1 and Step 5 limit by the number of qualifying children with valid SSNs, married filing jointly
- **Encoded (NonNegDollars):** Choose — [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 0 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 1 (a count) → helper "Step 1 and Step 5 limit, no children, married filing jointly"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 1 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 2 (a count) → helper "Step 1 and Step 5 limit, 1 child, married filing jointly"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 2 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 3 (a count) → helper "Step 1 and Step 5 limit, 2 children, married filing jointly"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 3 (a count) → helper "Step 1 and Step 5 limit, 3 or more children, married filing jointly"]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["eic.ssn_count",{"const":0,"type":"Count"}],"op":"test"},{"lt":["eic.ssn_count",{"const":1,"type":"Count"}],"op":"test"}],"op":"test"},"then":"eic.limit0_joint"},{"guard":{"all":[{"ge":["eic.ssn_count",{"const":1,"type":"Count"}],"op":"test"},{"lt":["eic.ssn_count",{"const":2,"type":"Count"}],"op":"test"}],"op":"test"},"then":"eic.limit1_joint"},{"guard":{"all":[{"ge":["eic.ssn_count",{"const":2,"type":"Count"}],"op":"test"},{"lt":["eic.ssn_count",{"const":3,"type":"Count"}],"op":"test"}],"op":"test"},"then":"eic.limit2_joint"},{"guard":{"ge":["eic.ssn_count",{"const":3,"type":"Count"}],"op":"test"},"then":"eic.limit3_joint"}],"op":"choose"}`
- Cite: [i1040gi] p. 40, Step 1, question 1, and p. 42, Step 5, question 3 (the amounts in parentheses) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.limit`

- **Authored helper label:** Step 1 and Step 5 limit for the filing status and the number of qualifying children with valid SSNs
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → helper "Step 1 and Step 5 limit by the number of qualifying children with valid SSNs"] [f1040 line Filing Status = 'mfj' → helper "Step 1 and Step 5 limit by the number of qualifying children with valid SSNs, married filing jointly"] [f1040 line Filing Status = 'mfs' → helper "Step 1 and Step 5 limit by the number of qualifying children with valid SSNs"] [f1040 line Filing Status = 'hoh' → helper "Step 1 and Step 5 limit by the number of qualifying children with valid SSNs"] [f1040 line Filing Status = 'qss' → helper "Step 1 and Step 5 limit by the number of qualifying children with valid SSNs"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"eic.limit_other"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"eic.limit_joint"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"eic.limit_other"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"eic.limit_other"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"eic.limit_other"}],"op":"choose"}`
- Cite: [i1040gi] p. 40, Step 1, question 1, and p. 42, Step 5, question 3 (the same four limits) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.step1_income`

- **Authored helper label:** Step 1, question 1. Is the amount on Form 1040, line 11b, less than the limit for the number of children who have valid SSNs?
- **Encoded (Bool):** f1040 line 11b < helper "Step 1 and Step 5 limit for the filing status and the number of qualifying children with valid SSNs"
- Expr: `{"lt":["f1040.line11b","eic.limit"],"op":"test"}`
- Cite: [i1040gi] p. 40, Step 1, question 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.step1_ssn`

- **Authored helper label:** Step 1, question 2. Do you have a social security number issued on or before the due date of your return that allows you to work and is valid for EIC purposes?
- **Encoded (Bool):** household helper "You, and your spouse if filing jointly, have SSNs valid for the EIC" = true
- Expr: `{"eq":["household.all_eic_ssn",{"const":true}],"op":"test"}`
- Cite: [i1040gi] p. 40, Step 1, question 2; pp. 44–45, Social security number (SSN), "For the EIC, a valid SSN is a number issued by the Social Security Administration unless “Not Valid for Employment” is printed on the social security card and the number was issued solely to allow the recipient of the SSN to apply for or receive a federally funded benefit" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.step1_foreign`

- **Authored helper label:** Step 1, question 3. Not filing Form 2555 (foreign earned income)
- **Encoded (Bool):** sa helper "Are you filing Form 2555 or Form 4563, or do you have income excluded as a bona fide resident of Puerto Rico?" = false
- **Refusal:** when sa.excluded_income is true, cannot complete Form 2555 (EIC, Step 1, question 3). A filer excluding foreign earned income can't take the EIC; Form 2555 and excluded income are outside this tool. Cite: [i1040gi] p. 40, Step 1, question 3, "Are you filing Form 2555 (relating to foreign earned income)? ... Yes. STOP" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"eq":["sa.excluded_income",{"const":false}],"op":"test"}`
- Cite: [i1040gi] p. 40, Step 1, question 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.step1_resident`

- **Authored helper label:** Step 1, question 4. Not a nonresident alien for any part of 2025
- **Encoded (Bool):** scope helper "Any nonresident alien status (you or your spouse, for any part of 2025) or other income or return treatment outside wages, interest, dividends, supported securities sales, Form 1099-R distributions and social security benefits, including wages or tips not on a Form W-2, Medicaid waiver payments (whether or not in Form W-2 box 1), adoption benefits, dependent care benefits other than those shown in box 10 of a Form W-2 (or a grace-period amount from such a plan), other earned income (Form 1040 lines 1b to 1d and 1f to 1h), or income or loss from a passive activity (including gain on selling an interest in one)?" = false
- **Refusal:** when scope.other_income is true, cannot complete Nonresident aliens (EIC, Step 1, question 4). Nonresident and dual-status treatment is outside this tool. Cite: [i1040gi] p. 40, Step 1, question 4; p. 44, Nonresident aliens (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"eq":["scope.other_income",{"const":false}],"op":"test"}`
- Cite: [i1040gi] p. 40, Step 1, question 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.gain_7a`

- **Authored helper label:** Form 1040, line 7a; if line 7a is a loss, enter -0-
- **Encoded (NonNegDollars):** Subtract helper "No amount" from f1040 line 7a. If zero or less, enter -0-.
- Expr: `{"from":"f1040.line7a","op":"subtract_floor0","take":"eic.zero"}`
- Cite: [i1040gi] p. 40, Step 2, question 1, "*If line 7a is a loss, enter -0-." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.investment_income`

- **Authored helper label:** Step 2, question 1. Investment income: Form 1040, lines 2a, 2b, 3b and 7a
- **Encoded (Dollars):** Add f1040 line 2a, f1040 line 2b, f1040 line 3b, and helper "Form 1040, line 7a; if line 7a is a loss, enter -0-".
- Expr: `{"of":["f1040.line2a","f1040.line2b","f1040.line3b","eic.gain_7a"],"op":"sum"}`
- Cite: [i1040gi] p. 40, Step 2, question 1, "Add the amounts from Form 1040 or 1040-SR: Line 2a ... Line 2b + Line 3b + Line 7a*" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.step2_income`

- **Authored helper label:** Step 2, question 2. Investment income not more than $11,950 (more than $11,950 stops at question 3 without Form 4797)
- **Encoded (Bool):** helper "Step 2, question 1. Investment income: Form 1040, lines 2a, 2b, 3b and 7a" ≤ $11,950 (eic.investment_limit)
- Expr: `{"le":["eic.investment_income",{"param":"eic.investment_limit"}],"op":"test"}`
- Cite: [i1040gi] p. 40, Step 2, questions 2 and 3 (Form 4797 is refused before this question, so question 3 is "No. STOP") (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.step2_other`

- **Authored helper label:** Step 2, question 4. No Schedule E, rental of personal property, Form 8814 or passive activity
- **Encoded (Bool):** scope helper "Any income or adjustment requiring Schedule 1 other than the ones this tool asks about separately (business income or loss from Schedule C; a taxable state or local income tax refund; alimony under an agreement made before 2019; unemployment compensation; the line 8 items asked one by one; educator expenses; the HSA deduction; the deductible part of self-employment tax; self-employed SEP and SIMPLE contributions; the self-employed health insurance deduction; the penalty on early withdrawal of savings; the IRA deduction; student loan interest; jury duty pay you gave your employer), including statutory-employee wages or clergy income; church employee income (wages from a church that elected exemption from social security and Medicare taxes); other qualified retirement plans for the self-employed (such as a solo 401(k) or other Keogh plan); a refund or other recovery of an amount you deducted or took a credit for in an earlier year, other than a state or local income tax refund (for example a refund of general sales tax, real estate tax or personal property tax, a refund of mortgage interest in box 4 of Form 1098, a reimbursement of medical expenses, or a payment on a bad debt you deducted); sales of business property (Form 4797); a net operating loss deduction; rental real estate, royalties, partnerships, S corporations, estates or trusts (Schedule E or a Schedule K-1); rental of personal property; farm income (Schedule F); an exclusion of Medicaid waiver payments (Schedule 1 line 8s); or an adjustment on Schedule 1 line 12, 14 or 23? (Schedule 1-A deductions are asked separately.)" = false and scope helper "Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no tax), Form 4972, Form 8615, a section 962 election, Form 8621, a Form 8978 amount, or recapture of an education credit?" = false
- **Refusal:** when scope.schedule1 is true, cannot complete Pub. 596, Worksheet 1 (EIC, Step 2, question 4). Schedule E, rental of personal property and passive activity income are outside this tool. Cite: [i1040gi] p. 40, Step 2, question 4, "Yes. Use Worksheet 1 ... in Pub. 596" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when scope.other_line16 is true, cannot complete Form 8814 (EIC, Step 2, question 4). Reporting a child's interest and dividends on Form 8814 is outside this tool. Cite: [i1040gi] p. 40, Step 2, question 4 (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"all":[{"eq":["scope.schedule1",{"const":false}],"op":"test"},{"eq":["scope.other_line16",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 40, Step 2, question 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.same_home`

- **Authored helper label:** Did you and your spouse have the same principal residence for the last 6 months of 2025?
- **Encoded (Bool):** Input — Did you and your spouse have the same principal residence for the last 6 months of 2025?
- Expr: `{"op":"input","source":"Did you and your spouse have the same principal residence for the last 6 months of 2025?"}`
- Cite: [i1040gi] p. 41, Step 3, question 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.legally_separated`

- **Authored helper label:** Are you legally separated under a written separation agreement or a decree of separate maintenance, and did you live apart from your spouse at the end of 2025?
- **Encoded (Bool):** Input — Are you legally separated according to your state law under a written separation agreement or a decree of separate maintenance, and did you live apart from your spouse at the end of 2025?
- Expr: `{"op":"input","source":"Are you legally separated according to your state law under a written separation agreement or a decree of separate maintenance, and did you live apart from your spouse at the end of 2025?"}`
- Cite: [i1040gi] p. 41, Step 3, question 5; p. 44, Special rule for separated spouses (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.step3_married`

- **Authored helper label:** Step 3, questions 3 to 5: not a married filer filing separately or as head of household, or one who lived apart from the spouse for the last 6 months of 2025 or is legally separated and lived apart at the end of 2025
- **Encoded (Bool):** (helper "A married filer whose filing status is married filing separately or head of household" = false or helper "Did you and your spouse have the same principal residence for the last 6 months of 2025?" = false or helper "Are you legally separated under a written separation agreement or a decree of separate maintenance, and did you live apart from your spouse at the end of 2025?" = true)
- Expr: `{"any":[{"eq":["eic.married_rules",{"const":false}],"op":"test"},{"eq":["eic.same_home",{"const":false}],"op":"test"},{"eq":["eic.legally_separated",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 41, Step 3, question 3 ("No. Skip questions 4 and 5"), question 4 ("No. Skip question 5"), question 5 ("No. STOP") (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.step3`

- **Authored helper label:** Step 3, questions 2 to 6: filing jointly, or passing questions 3 to 5 and not a qualifying child of another person
- **Encoded (Bool):** (f1040 line Filing Status = 'mfj' or helper "Step 3, questions 3 to 5: not a married filer filing separately or as head of household, or one who lived apart from the spouse for the last 6 months of 2025 or is legally separated and lived apart at the end of 2025" = true and helper "Could you be a qualifying child of another person for 2025?" = false)
- Expr: `{"any":[{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},{"all":[{"eq":["eic.step3_married",{"const":true}],"op":"test"},{"eq":["eic.qc_of_another",{"const":false}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 41, Step 3, questions 2 to 6 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.step4`

- **Authored helper label:** Step 4: not a married filer filing separately or as head of household, aged 25 to 64, main home in the United States, and not a qualifying child or dependent of another person
- **Encoded (Bool):** helper "A married filer whose filing status is married filing separately or head of household" = false and helper "You, or your spouse if filing a joint return, were at least age 25 but under age 65 at the end of 2025" = true and helper "Was your main home, and your spouse's if filing a joint return, in the United States for more than half of 2025?" = true and (f1040 line Filing Status = 'mfj' or helper "Could you be a qualifying child of another person for 2025?" = false and sa helper "Can someone claim you or your spouse as a dependent for 2025, or are you a dual-status alien? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)" = false)
- **Refusal:** when sa.dependent is true, cannot complete Dependent of another person or dual-status alien (EIC, Step 4, question 6). A filer who can be claimed as a dependent, or a dual-status alien, is outside this tool. Cite: [i1040gi] p. 42, Step 4, question 6 (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"all":[{"eq":["eic.married_rules",{"const":false}],"op":"test"},{"eq":["eic.age_range",{"const":true}],"op":"test"},{"eq":["eic.us_home",{"const":true}],"op":"test"},{"any":[{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},{"all":[{"eq":["eic.qc_of_another",{"const":false}],"op":"test"},{"eq":["sa.dependent",{"const":false}],"op":"test"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] pp. 41–42, Step 4, questions 1 to 6 (question 2 "at least age 25 but under age 65", born after December 31, 1960 and before January 2, 2001) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.step34`

- **Authored helper label:** Step 3 for a filer with a qualifying child, Step 4 otherwise
- **Encoded (Bool):** (helper "At least one qualifying child for the EIC" = true and helper "Step 3, questions 2 to 6: filing jointly, or passing questions 3 to 5 and not a qualifying child of another person" = true or helper "At least one qualifying child for the EIC" = false and helper "Step 4: not a married filer filing separately or as head of household, aged 25 to 64, main home in the United States, and not a qualifying child or dependent of another person" = true)
- Expr: `{"any":[{"all":[{"eq":["eic.has_qc",{"const":true}],"op":"test"},{"eq":["eic.step3",{"const":true}],"op":"test"}],"op":"test"},{"all":[{"eq":["eic.has_qc",{"const":false}],"op":"test"},{"eq":["eic.step4",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 41, Step 3, question 1, "No. Skip questions 2 through 6; go to Step 4" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.reached_step5`

- **Authored helper label:** Step 5 is reached (Steps 1 and 2 passed and Step 3 or 4 sends you to Step 5)
- **Encoded (Bool):** helper "Steps 1 and 2 passed, so Step 3 or Step 4 is asked" = true and helper "Step 3 for a filer with a qualifying child, Step 4 otherwise" = true
- Expr: `{"all":[{"eq":["eic.reached_step3",{"const":true}],"op":"test"},{"eq":["eic.step34",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 42, Step 4, "Go to Step 5"; each earlier "STOP You can't take the credit" ends the flowchart (pp. 40-42) (2025; printed date 2026-02-25; sha256 482e9c48)

## (Step 5, 1) — `eic.step5_line1`

- **Authored helper label:** Enter the amount from Form 1040 or 1040-SR, line 1z
- **Encoded (NonNegDollars):** Enter the amount from f1040 line 1z.
- **Refusal:** when scope.schedule1 is true, cannot complete Clergy, church employees and statutory employees (EIC, Step 5, questions 1 and 2; Worksheet B). Clergy, church employee and statutory employee income are outside this tool. Cite: [i1040gi] p. 42, Step 5, questions 1 and 2; p. 43, Clergy and Church employees; p. 47, Worksheet B (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"from":"f1040.line1z","op":"copy"}`
- Cite: [i1040gi] p. 42, Step 5, worksheet line 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (Step 5, 2) — `eic.step5_line2`

- **Authored helper label:** Medicaid waiver payments excluded from income on Schedule 1, line 8s, unless chosen as earned income; zero in this tool
- **Encoded (NonNegDollars):** Enter the amount from helper "No amount".
- **Refusal:** when scope.other_income is true, cannot complete Medicaid waiver payments (EIC, Step 5, line 2). Medicaid waiver payments are outside this tool. Cite: [i1040gi] p. 42, Step 5, worksheet line 2 (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"from":"eic.zero","op":"copy"}`
- Cite: [i1040gi] p. 42, Step 5, worksheet line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (Step 5, 3) — `eic.step5_line3`

- **Authored helper label:** Subtract line 2 from line 1
- **Encoded (Dollars):** Subtract column (Step 5, 2) from column (Step 5, 1).
- Expr: `{"from":"eic.step5_line1","op":"subtract","take":"eic.step5_line2"}`
- Cite: [i1040gi] p. 42, Step 5, worksheet line 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (Step 5, 4) — `eic.step5_line4`

- **Authored helper label:** Nontaxable combat pay you elect to include in earned income; zero in this tool
- **Encoded (NonNegDollars):** Enter the amount from helper "No amount".
- **Refusal:** when s8812.combat_pay is true, cannot complete Nontaxable combat pay (EIC, Step 5, line 4). Nontaxable combat pay is outside this tool. Cite: [i1040gi] p. 42, Step 5, worksheet line 4; p. 43, Combat pay, nontaxable (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"from":"eic.zero","op":"copy"}`
- Cite: [i1040gi] p. 42, Step 5, worksheet line 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (Step 5, 5) — `eic.earned_income`

- **Authored helper label:** Add lines 3 and 4. This is your earned income
- **Encoded (Dollars):** Add column (Step 5, 3) and column (Step 5, 4).
- Expr: `{"of":["eic.step5_line3","eic.step5_line4"],"op":"sum"}`
- Cite: [i1040gi] p. 42, Step 5, worksheet line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.sc_count`

- **Authored helper label:** Number of Schedules C on the return
- **Encoded (Count):** Add person.sc_count over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.sc_count","op":"sum_over"}`
- Cite: [i1040gi] p. 42, Step 5, question 2, "Were you self-employed at any time in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.self_employed`

- **Authored helper label:** Step 5, question 2: self-employed (Worksheet B)
- **Encoded (Bool):** helper "Number of Schedules C on the return" > 0 (a count)
- Expr: `{"gt":["eic.sc_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 42, Step 5, question 2, "Yes. Skip question 3 ... and Step 6; go to Worksheet B" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.wsb_se`

- **Authored helper label:** Worksheet B, lines 1e and 2c (both spouses on a joint return)
- **Encoded (Dollars):** Add person.eic_se over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.eic_se","op":"sum_over"}`
- Cite: [i1040gi] p. 47, Worksheet B, Parts 1 and 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.show_wsb4b`

- **Authored helper label:** Worksheet B is used (Step 5 reached and Step 5 question 2 is Yes)
- **Encoded (Bool):** helper "Step 5 is reached (Steps 1 and 2 passed and Step 3 or 4 sends you to Step 5)" = true and helper "Step 5, question 2: self-employed (Worksheet B)" = true
- Expr: `{"all":[{"eq":["eic.reached_step5",{"const":true}],"op":"test"},{"eq":["eic.self_employed",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 47, Worksheet B, "Use this worksheet if you answered “Yes” to Step 5, question 2" (2025; printed date 2026-02-25; sha256 482e9c48)

## 4b — `eic.wsb_4b`

- **IRS:** Worksheet B, line 4b. Combine lines 1e, 2c, 3, and 4a. This is your total earned income
- **Encoded (Dollars):** Add column (Step 5, 5) and helper "Worksheet B, lines 1e and 2c (both spouses on a joint return)".
- **Shown on the values sheet only when:** Worksheet B is used (Step 5 reached and Step 5 question 2 is Yes) (`eic.show_wsb4b`)
- Expr: `{"of":["eic.earned_income","eic.wsb_se"],"op":"sum"}`
- Cite: [i1040gi] p. 47, Worksheet B, Part 4, line 4b, "4a. Enter your earned income from Step 5", "b. Combine lines 1e, 2c, 3, and 4a. This is your total earned income" (line 3, statutory employees, is refused) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.show_wsb6`

- **Authored helper label:** Worksheet B line 6 is completed (the credit is reached and Worksheet B is used)
- **Encoded (Bool):** helper "Steps 1 to 5 passed in order (Step 6, figure the credit on Worksheet A)" = true and helper "Step 5, question 2: self-employed (Worksheet B)" = true
- Expr: `{"all":[{"eq":["eic.eligible",{"const":true}],"op":"test"},{"eq":["eic.self_employed",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 47, Worksheet B, line 5, "No. You can’t take the credit" (2025; printed date 2026-02-25; sha256 482e9c48)

## 6 — `eic.wsb_6`

- **IRS:** Worksheet B, line 6. Enter your total earned income from Part 4, line 4b (zero if line 4b is zero or less)
- **Encoded (NonNegDollars):** Subtract helper "No amount" from line 4b. If zero or less, enter -0-.
- **Shown on the values sheet only when:** Worksheet B line 6 is completed (the credit is reached and Worksheet B is used) (`eic.show_wsb6`)
- Expr: `{"from":"eic.wsb_4b","op":"subtract_floor0","take":"eic.zero"}`
- Cite: [i1040gi] p. 47, Worksheet B, Part 4, "STOP If line 4b is zero or less, you can't take the credit", and Part 5, line 6 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.earned_for_limit`

- **Authored helper label:** Earned income compared with the limit (Step 5, question 3, or Worksheet B, line 5)
- **Encoded (Dollars):** Choose — [helper "Step 5, question 2: self-employed (Worksheet B)" = false → column (Step 5, 5)] [helper "Step 5, question 2: self-employed (Worksheet B)" = true → line 4b]
- Expr: `{"alternatives":[{"guard":{"eq":["eic.self_employed",{"const":false}],"op":"test"},"then":"eic.earned_income"},{"guard":{"eq":["eic.self_employed",{"const":true}],"op":"test"},"then":"eic.wsb_4b"}],"op":"choose"}`
- Cite: [i1040gi] p. 42, Step 5, question 3; p. 47, Worksheet B, Part 4, line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.step5_income`

- **Authored helper label:** Step 5, question 3. Is your earned income less than the limit for the number of qualifying children with valid SSNs?
- **Encoded (Bool):** helper "Earned income compared with the limit (Step 5, question 3, or Worksheet B, line 5)" < helper "Step 1 and Step 5 limit for the filing status and the number of qualifying children with valid SSNs"
- Expr: `{"lt":["eic.earned_for_limit","eic.limit"],"op":"test"}`
- Cite: [i1040gi] p. 42, Step 5, question 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.eligible`

- **Authored helper label:** Steps 1 to 5 passed in order (Step 6, figure the credit on Worksheet A)
- **Encoded (Bool):** helper "Adjusted gross income below the largest Step 1 limit (otherwise question 1 is "No" for any number of children)" = true and helper "Step 1, question 1. Is the amount on Form 1040, line 11b, less than the limit for the number of children who have valid SSNs?" = true and helper "Step 1, question 2. Do you have a social security number issued on or before the due date of your return that allows you to work and is valid for EIC purposes?" = true and helper "Step 1, question 3. Not filing Form 2555 (foreign earned income)" = true and helper "Step 1, question 4. Not a nonresident alien for any part of 2025" = true and helper "Step 2, question 2. Investment income not more than $11,950 (more than $11,950 stops at question 3 without Form 4797)" = true and helper "Step 2, question 4. No Schedule E, rental of personal property, Form 8814 or passive activity" = true and helper "Step 3 for a filer with a qualifying child, Step 4 otherwise" = true and helper "Step 5, question 3. Is your earned income less than the limit for the number of qualifying children with valid SSNs?" = true
- Expr: `{"all":[{"eq":["eic.below_top",{"const":true}],"op":"test"},{"eq":["eic.step1_income",{"const":true}],"op":"test"},{"eq":["eic.step1_ssn",{"const":true}],"op":"test"},{"eq":["eic.step1_foreign",{"const":true}],"op":"test"},{"eq":["eic.step1_resident",{"const":true}],"op":"test"},{"eq":["eic.step2_income",{"const":true}],"op":"test"},{"eq":["eic.step2_other",{"const":true}],"op":"test"},{"eq":["eic.step34",{"const":true}],"op":"test"},{"eq":["eic.step5_income",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] pp. 40–43, Steps 1 to 6 (each "No. STOP You can't take the credit" ends the flow chart; Step 6, question 1, "No. Go to Worksheet A") (2025; printed date 2026-02-25; sha256 482e9c48)

## 1 — `eic.line1`

- **IRS:** Enter your earned income from Step 5 (Worksheet A, line 1), or Worksheet B, line 6
- **Encoded (Dollars):** Choose — [helper "Step 5, question 2: self-employed (Worksheet B)" = false → column (Step 5, 5)] [helper "Step 5, question 2: self-employed (Worksheet B)" = true → line 6 (eic.wsb_6)]
- **Shown on the values sheet only when:** Steps 1 to 5 passed in order (Step 6, figure the credit on Worksheet A) (`eic.eligible`)
- Expr: `{"alternatives":[{"guard":{"eq":["eic.self_employed",{"const":false}],"op":"test"},"then":"eic.earned_income"},{"guard":{"eq":["eic.self_employed",{"const":true}],"op":"test"},"then":"eic.wsb_6"}],"op":"choose"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 1; p. 48, Worksheet B, Part 5, line 6 (Worksheet A lines 2 to 6 are Worksheet B lines 7 to 11) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.line1_in_table`

- **Authored helper label:** Line 1 is at least $1, the first amount the EIC Table lists
- **Encoded (Bool):** line 1 ≥ $1 (eic.table_start)
- Expr: `{"ge":["eic.line1",{"param":"eic.table_start"}],"op":"test"}`
- Cite: [i1040gi] p. 49, EIC Table, first row "At least 1" (see the ambiguity register, amb.2025.eic_below_table) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.line1_table0`

- **Authored helper label:** EIC Table credit for line 1, no qualifying children with valid SSNs
- **Encoded (NonNegDollars):** Use 2025 Earned Income Credit (EIC) Table — no qualifying children at line 1 for the filing status (f1040 line Filing Status).
- Expr: `{"key":"eic.line1","op":"table_lookup","status":"f1040.status","table":"eic_0"}`
- Cite: [i1040gi] pp. 49–60, EIC Table, column 0 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.line1_table1`

- **Authored helper label:** EIC Table credit for line 1, one qualifying child with a valid SSN
- **Encoded (NonNegDollars):** Use 2025 Earned Income Credit (EIC) Table — one qualifying child at line 1 for the filing status (f1040 line Filing Status).
- Expr: `{"key":"eic.line1","op":"table_lookup","status":"f1040.status","table":"eic_1"}`
- Cite: [i1040gi] pp. 49–60, EIC Table, column 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.line1_table2`

- **Authored helper label:** EIC Table credit for line 1, two qualifying children with valid SSNs
- **Encoded (NonNegDollars):** Use 2025 Earned Income Credit (EIC) Table — two qualifying children at line 1 for the filing status (f1040 line Filing Status).
- Expr: `{"key":"eic.line1","op":"table_lookup","status":"f1040.status","table":"eic_2"}`
- Cite: [i1040gi] pp. 49–60, EIC Table, column 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.line1_table3`

- **Authored helper label:** EIC Table credit for line 1, three or more qualifying children with valid SSNs
- **Encoded (NonNegDollars):** Use 2025 Earned Income Credit (EIC) Table — three or more qualifying children at line 1 for the filing status (f1040 line Filing Status).
- Expr: `{"key":"eic.line1","op":"table_lookup","status":"f1040.status","table":"eic_3"}`
- Cite: [i1040gi] pp. 49–60, EIC Table, column 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.line1_table`

- **Authored helper label:** EIC Table credit for line 1 in the column for the number of qualifying children with valid SSNs
- **Encoded (NonNegDollars):** Choose — [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 0 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 1 (a count) → helper "EIC Table credit for line 1, no qualifying children with valid SSNs"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 1 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 2 (a count) → helper "EIC Table credit for line 1, one qualifying child with a valid SSN"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 2 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 3 (a count) → helper "EIC Table credit for line 1, two qualifying children with valid SSNs"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 3 (a count) → helper "EIC Table credit for line 1, three or more qualifying children with valid SSNs"]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["eic.ssn_count",{"const":0,"type":"Count"}],"op":"test"},{"lt":["eic.ssn_count",{"const":1,"type":"Count"}],"op":"test"}],"op":"test"},"then":"eic.line1_table0"},{"guard":{"all":[{"ge":["eic.ssn_count",{"const":1,"type":"Count"}],"op":"test"},{"lt":["eic.ssn_count",{"const":2,"type":"Count"}],"op":"test"}],"op":"test"},"then":"eic.line1_table1"},{"guard":{"all":[{"ge":["eic.ssn_count",{"const":2,"type":"Count"}],"op":"test"},{"lt":["eic.ssn_count",{"const":3,"type":"Count"}],"op":"test"}],"op":"test"},"then":"eic.line1_table2"},{"guard":{"ge":["eic.ssn_count",{"const":3,"type":"Count"}],"op":"test"},"then":"eic.line1_table3"}],"op":"choose"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 2, "the number of qualifying children you have who have valid SSNs" (2025; printed date 2026-02-25; sha256 482e9c48)

## 2 — `eic.line2`

- **IRS:** Look up the amount on line 1 in the EIC Table to find the credit, using the column for your filing status and the number of qualifying children who have valid SSNs
- **Encoded (NonNegDollars):** Choose — [helper "Line 1 is at least $1, the first amount the EIC Table lists" = true → helper "EIC Table credit for line 1 in the column for the number of qualifying children with valid SSNs"] [helper "Line 1 is at least $1, the first amount the EIC Table lists" = false → helper "No amount"]
- **Shown on the values sheet only when:** Steps 1 to 5 passed in order (Step 6, figure the credit on Worksheet A) (`eic.eligible`)
- Expr: `{"alternatives":[{"guard":{"eq":["eic.line1_in_table",{"const":true}],"op":"test"},"then":"eic.line1_table"},{"guard":{"eq":["eic.line1_in_table",{"const":false}],"op":"test"},"then":"eic.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.show3`

- **Authored helper label:** Worksheet A line 3 is completed (the credit is reached and line 2 is more than zero)
- **Encoded (Bool):** helper "Steps 1 to 5 passed in order (Step 6, figure the credit on Worksheet A)" = true and line 2 > $0 (sales.zero)
- Expr: `{"all":[{"eq":["eic.eligible",{"const":true}],"op":"test"},{"gt":["eic.line2",{"param":"sales.zero"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 2, "If line 2 is zero, You can’t take the credit" (2025; printed date 2026-02-25; sha256 482e9c48)

## 3 — `eic.line3`

- **IRS:** Enter the amount from Form 1040 or 1040-SR, line 11b
- **Encoded (Dollars):** Enter the amount from f1040 line 11b.
- **Shown on the values sheet only when:** Worksheet A line 3 is completed (the credit is reached and line 2 is more than zero) (`eic.show3`)
- Expr: `{"from":"f1040.line11b","op":"copy"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## 4 — `eic.line4`

- **IRS:** Are the amounts on lines 3 and 1 the same?
- **Encoded (Bool):** line 3 = line 1
- Expr: `{"eq":["eic.line3","eic.line1"],"op":"test"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.threshold_other`

- **Authored helper label:** Line 5 amount by whether you have a qualifying child with a valid SSN
- **Encoded (NonNegDollars):** Choose — [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 0 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 1 (a count) → helper "Line 5 amount, no qualifying children"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 1 (a count) → helper "Line 5 amount, 1 or more qualifying children"]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["eic.ssn_count",{"const":0,"type":"Count"}],"op":"test"},{"lt":["eic.ssn_count",{"const":1,"type":"Count"}],"op":"test"}],"op":"test"},"then":"eic.threshold0_other"},{"guard":{"ge":["eic.ssn_count",{"const":1,"type":"Count"}],"op":"test"},"then":"eic.threshold1_other"}],"op":"choose"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.threshold_joint`

- **Authored helper label:** Line 5 amount by whether you have a qualifying child with a valid SSN, married filing jointly
- **Encoded (NonNegDollars):** Choose — [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 0 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 1 (a count) → helper "Line 5 amount, no qualifying children, married filing jointly"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 1 (a count) → helper "Line 5 amount, 1 or more qualifying children, married filing jointly"]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["eic.ssn_count",{"const":0,"type":"Count"}],"op":"test"},{"lt":["eic.ssn_count",{"const":1,"type":"Count"}],"op":"test"}],"op":"test"},"then":"eic.threshold0_joint"},{"guard":{"ge":["eic.ssn_count",{"const":1,"type":"Count"}],"op":"test"},"then":"eic.threshold1_joint"}],"op":"choose"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 5 (the amounts in parentheses) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.line5_threshold`

- **Authored helper label:** Line 5 amount for the filing status and whether you have a qualifying child with a valid SSN
- **Encoded (NonNegDollars):** Choose — [f1040 line Filing Status = 'single' → helper "Line 5 amount by whether you have a qualifying child with a valid SSN"] [f1040 line Filing Status = 'mfj' → helper "Line 5 amount by whether you have a qualifying child with a valid SSN, married filing jointly"] [f1040 line Filing Status = 'mfs' → helper "Line 5 amount by whether you have a qualifying child with a valid SSN"] [f1040 line Filing Status = 'hoh' → helper "Line 5 amount by whether you have a qualifying child with a valid SSN"] [f1040 line Filing Status = 'qss' → helper "Line 5 amount by whether you have a qualifying child with a valid SSN"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"eic.threshold_other"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"eic.threshold_joint"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"eic.threshold_other"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"eic.threshold_other"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"eic.threshold_other"}],"op":"choose"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.threshold0_other`

- **Authored helper label:** Line 5 amount, no qualifying children
- **Encoded (NonNegDollars):** Enter $10,620 (eic.ws_threshold0.other).
- Expr: `{"op":"param","ref":"eic.ws_threshold0.other"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.threshold1_other`

- **Authored helper label:** Line 5 amount, 1 or more qualifying children
- **Encoded (NonNegDollars):** Enter $23,350 (eic.ws_threshold1.other).
- Expr: `{"op":"param","ref":"eic.ws_threshold1.other"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.threshold0_joint`

- **Authored helper label:** Line 5 amount, no qualifying children, married filing jointly
- **Encoded (NonNegDollars):** Enter $17,730 (eic.ws_threshold0.joint).
- Expr: `{"op":"param","ref":"eic.ws_threshold0.joint"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.threshold1_joint`

- **Authored helper label:** Line 5 amount, 1 or more qualifying children, married filing jointly
- **Encoded (NonNegDollars):** Enter $30,470 (eic.ws_threshold1.joint).
- Expr: `{"op":"param","ref":"eic.ws_threshold1.joint"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.line5_blank`

- **Authored helper label:** Line 5. Is the amount on line 3 less than the line 5 amount? (Yes leaves line 5 blank)
- **Encoded (Bool):** line 3 < helper "Line 5 amount for the filing status and whether you have a qualifying child with a valid SSN"
- Expr: `{"lt":["eic.line3","eic.line5_threshold"],"op":"test"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 5, "Yes. Leave line 5 blank; enter the amount from line 2 on line 6" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.line3_table0`

- **Authored helper label:** EIC Table credit for line 3, no qualifying children with valid SSNs
- **Encoded (NonNegDollars):** Use 2025 Earned Income Credit (EIC) Table — no qualifying children at line 3 for the filing status (f1040 line Filing Status).
- Expr: `{"key":"eic.line3","op":"table_lookup","status":"f1040.status","table":"eic_0"}`
- Cite: [i1040gi] pp. 49–60, EIC Table, column 0 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.line3_table1`

- **Authored helper label:** EIC Table credit for line 3, one qualifying child with a valid SSN
- **Encoded (NonNegDollars):** Use 2025 Earned Income Credit (EIC) Table — one qualifying child at line 3 for the filing status (f1040 line Filing Status).
- Expr: `{"key":"eic.line3","op":"table_lookup","status":"f1040.status","table":"eic_1"}`
- Cite: [i1040gi] pp. 49–60, EIC Table, column 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.line3_table2`

- **Authored helper label:** EIC Table credit for line 3, two qualifying children with valid SSNs
- **Encoded (NonNegDollars):** Use 2025 Earned Income Credit (EIC) Table — two qualifying children at line 3 for the filing status (f1040 line Filing Status).
- Expr: `{"key":"eic.line3","op":"table_lookup","status":"f1040.status","table":"eic_2"}`
- Cite: [i1040gi] pp. 49–60, EIC Table, column 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.line3_table3`

- **Authored helper label:** EIC Table credit for line 3, three or more qualifying children with valid SSNs
- **Encoded (NonNegDollars):** Use 2025 Earned Income Credit (EIC) Table — three or more qualifying children at line 3 for the filing status (f1040 line Filing Status).
- Expr: `{"key":"eic.line3","op":"table_lookup","status":"f1040.status","table":"eic_3"}`
- Cite: [i1040gi] pp. 49–60, EIC Table, column 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.show5`

- **Authored helper label:** Worksheet A line 5 is completed (the credit is reached, line 2 is more than zero, line 4 is No and line 5 is not left blank)
- **Encoded (Bool):** helper "Steps 1 to 5 passed in order (Step 6, figure the credit on Worksheet A)" = true and line 4 = false and helper "Line 5. Is the amount on line 3 less than the line 5 amount? (Yes leaves line 5 blank)" = false and line 2 > $0 (sales.zero)
- Expr: `{"all":[{"eq":["eic.eligible",{"const":true}],"op":"test"},{"eq":["eic.line4",{"const":false}],"op":"test"},{"eq":["eic.line5_blank",{"const":false}],"op":"test"},{"gt":["eic.line2",{"param":"sales.zero"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 2, "If line 2 is zero, You can’t take the credit"; line 4, "Yes. Skip line 5; enter the amount from line 2 on line 6"; line 5, "Yes. Leave line 5 blank" (2025; printed date 2026-02-25; sha256 482e9c48)

## 5 — `eic.line5`

- **IRS:** Look up the amount on line 3 in the EIC Table to find the credit, using the column for your filing status and the number of qualifying children who have valid SSNs
- **Encoded (NonNegDollars):** Choose — [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 0 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 1 (a count) → helper "EIC Table credit for line 3, no qualifying children with valid SSNs"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 1 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 2 (a count) → helper "EIC Table credit for line 3, one qualifying child with a valid SSN"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 2 (a count) and helper "Number of qualifying children for the EIC who have valid SSNs" < 3 (a count) → helper "EIC Table credit for line 3, two qualifying children with valid SSNs"] [helper "Number of qualifying children for the EIC who have valid SSNs" ≥ 3 (a count) → helper "EIC Table credit for line 3, three or more qualifying children with valid SSNs"]
- **Shown on the values sheet only when:** Worksheet A line 5 is completed (the credit is reached, line 2 is more than zero, line 4 is No and line 5 is not left blank) (`eic.show5`)
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["eic.ssn_count",{"const":0,"type":"Count"}],"op":"test"},{"lt":["eic.ssn_count",{"const":1,"type":"Count"}],"op":"test"}],"op":"test"},"then":"eic.line3_table0"},{"guard":{"all":[{"ge":["eic.ssn_count",{"const":1,"type":"Count"}],"op":"test"},{"lt":["eic.ssn_count",{"const":2,"type":"Count"}],"op":"test"}],"op":"test"},"then":"eic.line3_table1"},{"guard":{"all":[{"ge":["eic.ssn_count",{"const":2,"type":"Count"}],"op":"test"},{"lt":["eic.ssn_count",{"const":3,"type":"Count"}],"op":"test"}],"op":"test"},"then":"eic.line3_table2"},{"guard":{"ge":["eic.ssn_count",{"const":3,"type":"Count"}],"op":"test"},"then":"eic.line3_table3"}],"op":"choose"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 5, "No. Look up the amount on line 3 in the EIC Table to find the credit" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.smaller`

- **Authored helper label:** The smaller of lines 5 and 2
- **Encoded (NonNegDollars):** Enter the smaller of line 5 or line 2.
- Expr: `{"of":["eic.line5","eic.line2"],"op":"smaller_of"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 5, "Look at the amounts on lines 5 and 2. Then, enter the smaller amount on line 6" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.after_line4`

- **Authored helper label:** When line 4 is No, line 2 if line 5 is left blank and otherwise the smaller of lines 5 and 2
- **Encoded (NonNegDollars):** Choose — [helper "Line 5. Is the amount on line 3 less than the line 5 amount? (Yes leaves line 5 blank)" = true → line 2] [helper "Line 5. Is the amount on line 3 less than the line 5 amount? (Yes leaves line 5 blank)" = false → helper "The smaller of lines 5 and 2"]
- Expr: `{"alternatives":[{"guard":{"eq":["eic.line5_blank",{"const":true}],"op":"test"},"then":"eic.line2"},{"guard":{"eq":["eic.line5_blank",{"const":false}],"op":"test"},"then":"eic.smaller"}],"op":"choose"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## 6 — `eic.line6`

- **IRS:** This is your earned income credit
- **Encoded (NonNegDollars):** Choose — [line 4 = true → line 2] [line 4 = false → helper "When line 4 is No, line 2 if line 5 is left blank and otherwise the smaller of lines 5 and 2"]
- **Shown on the values sheet only when:** Steps 1 to 5 passed in order (Step 6, figure the credit on Worksheet A) (`eic.eligible`)
- Expr: `{"alternatives":[{"guard":{"eq":["eic.line4",{"const":true}],"op":"test"},"then":"eic.line2"},{"guard":{"eq":["eic.line4",{"const":false}],"op":"test"},"then":"eic.after_line4"}],"op":"choose"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 4, "Yes. Skip line 5; enter the amount from line 2 on line 6", and line 6 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.credit`

- **Authored helper label:** Earned income credit for Form 1040, line 27a (Worksheet A, line 6, or Worksheet B, line 11 for a filer who answered Yes to Step 5, question 2, when Steps 1 to 5 are passed; zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "Steps 1 to 5 passed in order (Step 6, figure the credit on Worksheet A)" = true → line 6 (eic.line6)] [helper "Steps 1 to 5 passed in order (Step 6, figure the credit on Worksheet A)" = false → helper "No amount"]
- **Refusal:** when household.credit_disallowed is true, cannot complete Form 8862 and the EIC disallowance period (Form 8862, who must file). Your EIC, child tax credit, additional child tax credit or credit for other dependents for an earlier year was reduced or disallowed, or you are in a disallowance period; Form 8862 and the disallowance period are outside this tool. Cite: [i1040gi] p. 43, Form 8862, who must file, "You must file Form 8862 if your EIC for a year after 1996 was reduced or disallowed for any reason other than a math or clerical error" and "don’t file Form 8862 or take the credit for the ... 2 years after the most recent tax year for which there was a final determination that your EIC claim was due to reckless or intentional disregard of the EIC rules ... 10 years after the most recent tax year for which there was a final determination that your EIC claim was due to fraud" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"alternatives":[{"guard":{"eq":["eic.eligible",{"const":true}],"op":"test"},"then":"eic.line6"},{"guard":{"eq":["eic.eligible",{"const":false}],"op":"test"},"then":"eic.zero"}],"op":"choose"}`
- Cite: [i1040gi] pp. 40–46, each "STOP You can't take the credit"; Worksheet A, line 6, "Enter this amount on Form 1040 or 1040-SR, line 27a" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.reached_step3`

- **Authored helper label:** Steps 1 and 2 passed, so Step 3 or Step 4 is asked
- **Encoded (Bool):** helper "Adjusted gross income below the largest Step 1 limit (otherwise question 1 is "No" for any number of children)" = true and helper "Step 1, question 1. Is the amount on Form 1040, line 11b, less than the limit for the number of children who have valid SSNs?" = true and helper "Step 1, question 2. Do you have a social security number issued on or before the due date of your return that allows you to work and is valid for EIC purposes?" = true and helper "Step 1, question 3. Not filing Form 2555 (foreign earned income)" = true and helper "Step 1, question 4. Not a nonresident alien for any part of 2025" = true and helper "Step 2, question 2. Investment income not more than $11,950 (more than $11,950 stops at question 3 without Form 4797)" = true and helper "Step 2, question 4. No Schedule E, rental of personal property, Form 8814 or passive activity" = true
- Expr: `{"all":[{"eq":["eic.below_top",{"const":true}],"op":"test"},{"eq":["eic.step1_income",{"const":true}],"op":"test"},{"eq":["eic.step1_ssn",{"const":true}],"op":"test"},{"eq":["eic.step1_foreign",{"const":true}],"op":"test"},{"eq":["eic.step1_resident",{"const":true}],"op":"test"},{"eq":["eic.step2_income",{"const":true}],"op":"test"},{"eq":["eic.step2_other",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] pp. 40–41, Steps 1 and 2 ("Go to Step 3") (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.check_27c`

- **Authored helper label:** The instructions say to check the box on line 27c (a STOP that says so, or Worksheet A line 2 is zero); the filer's own choice not to claim the EIC is not asked
- **Encoded (Bool):** (helper "Adjusted gross income below the largest Step 1 limit (otherwise question 1 is "No" for any number of children)" = true and helper "Step 1, question 1. Is the amount on Form 1040, line 11b, less than the limit for the number of children who have valid SSNs?" = true and helper "Step 1, question 2. Do you have a social security number issued on or before the due date of your return that allows you to work and is valid for EIC purposes?" = false or helper "Steps 1 and 2 passed, so Step 3 or Step 4 is asked" = true and helper "At least one qualifying child for the EIC" = true and helper "Step 3, questions 3 to 5: not a married filer filing separately or as head of household, or one who lived apart from the spouse for the last 6 months of 2025 or is legally separated and lived apart at the end of 2025" = true and f1040 line Filing Status ≠ 'mfj' and helper "Could you be a qualifying child of another person for 2025?" = true or helper "Steps 1 and 2 passed, so Step 3 or Step 4 is asked" = true and helper "At least one qualifying child for the EIC" = false and helper "A married filer whose filing status is married filing separately or head of household" = false and helper "You, or your spouse if filing a joint return, were at least age 25 but under age 65 at the end of 2025" = true and helper "Was your main home, and your spouse's if filing a joint return, in the United States for more than half of 2025?" = false or helper "Steps 1 and 2 passed, so Step 3 or Step 4 is asked" = true and helper "At least one qualifying child for the EIC" = false and helper "A married filer whose filing status is married filing separately or head of household" = false and helper "You, or your spouse if filing a joint return, were at least age 25 but under age 65 at the end of 2025" = true and helper "Was your main home, and your spouse's if filing a joint return, in the United States for more than half of 2025?" = true and f1040 line Filing Status ≠ 'mfj' and helper "Could you be a qualifying child of another person for 2025?" = true or helper "Steps 1 to 5 passed in order (Step 6, figure the credit on Worksheet A)" = true and line 2 = $0 (sales.zero) or helper "Worksheet B, line 5 is No (line 4b is not less than the limit), a STOP that says to check line 27c" = true)
- Expr: `{"any":[{"all":[{"eq":["eic.below_top",{"const":true}],"op":"test"},{"eq":["eic.step1_income",{"const":true}],"op":"test"},{"eq":["eic.step1_ssn",{"const":false}],"op":"test"}],"op":"test"},{"all":[{"eq":["eic.reached_step3",{"const":true}],"op":"test"},{"eq":["eic.has_qc",{"const":true}],"op":"test"},{"eq":["eic.step3_married",{"const":true}],"op":"test"},{"ne":["f1040.status",{"const":"mfj"}],"op":"test"},{"eq":["eic.qc_of_another",{"const":true}],"op":"test"}],"op":"test"},{"all":[{"eq":["eic.reached_step3",{"const":true}],"op":"test"},{"eq":["eic.has_qc",{"const":false}],"op":"test"},{"eq":["eic.married_rules",{"const":false}],"op":"test"},{"eq":["eic.age_range",{"const":true}],"op":"test"},{"eq":["eic.us_home",{"const":false}],"op":"test"}],"op":"test"},{"all":[{"eq":["eic.reached_step3",{"const":true}],"op":"test"},{"eq":["eic.has_qc",{"const":false}],"op":"test"},{"eq":["eic.married_rules",{"const":false}],"op":"test"},{"eq":["eic.age_range",{"const":true}],"op":"test"},{"eq":["eic.us_home",{"const":true}],"op":"test"},{"ne":["f1040.status",{"const":"mfj"}],"op":"test"},{"eq":["eic.qc_of_another",{"const":true}],"op":"test"}],"op":"test"},{"all":[{"eq":["eic.eligible",{"const":true}],"op":"test"},{"eq":["eic.line2",{"param":"sales.zero"}],"op":"test"}],"op":"test"},{"eq":["eic.wsb_line5_stop",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 40, Step 1, question 2; p. 41, Step 3, question 6; p. 42, Step 4, questions 3 and 5; p. 43, Line 27c; p. 46, Worksheet A, line 2 ("Check the box on Form 1040 or 1040-SR, line 27c"); p. 47, Worksheet B, line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.wsb_4b_positive`

- **Authored helper label:** Worksheet B, line 4b is more than zero (the worksheet continues to line 5)
- **Encoded (Bool):** line 4b > $0 (sales.zero)
- Expr: `{"gt":["eic.wsb_4b",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 47, Worksheet B, Part 4, "STOP If line 4b is zero or less" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.wsb_line5_stop`

- **Authored helper label:** Worksheet B, line 5 is No (line 4b is not less than the limit), a STOP that says to check line 27c
- **Encoded (Bool):** helper "Adjusted gross income below the largest Step 1 limit (otherwise question 1 is "No" for any number of children)" = true and helper "Step 1, question 1. Is the amount on Form 1040, line 11b, less than the limit for the number of children who have valid SSNs?" = true and helper "Step 1, question 2. Do you have a social security number issued on or before the due date of your return that allows you to work and is valid for EIC purposes?" = true and helper "Step 1, question 3. Not filing Form 2555 (foreign earned income)" = true and helper "Step 1, question 4. Not a nonresident alien for any part of 2025" = true and helper "Step 2, question 2. Investment income not more than $11,950 (more than $11,950 stops at question 3 without Form 4797)" = true and helper "Step 2, question 4. No Schedule E, rental of personal property, Form 8814 or passive activity" = true and helper "Step 3 for a filer with a qualifying child, Step 4 otherwise" = true and helper "Step 5, question 2: self-employed (Worksheet B)" = true and helper "Worksheet B, line 4b is more than zero (the worksheet continues to line 5)" = true and helper "Step 5, question 3. Is your earned income less than the limit for the number of qualifying children with valid SSNs?" = false
- Expr: `{"all":[{"eq":["eic.below_top",{"const":true}],"op":"test"},{"eq":["eic.step1_income",{"const":true}],"op":"test"},{"eq":["eic.step1_ssn",{"const":true}],"op":"test"},{"eq":["eic.step1_foreign",{"const":true}],"op":"test"},{"eq":["eic.step1_resident",{"const":true}],"op":"test"},{"eq":["eic.step2_income",{"const":true}],"op":"test"},{"eq":["eic.step2_other",{"const":true}],"op":"test"},{"eq":["eic.step34",{"const":true}],"op":"test"},{"eq":["eic.self_employed",{"const":true}],"op":"test"},{"eq":["eic.wsb_4b_positive",{"const":true}],"op":"test"},{"eq":["eic.step5_income",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 47, Worksheet B, line 5, "STOP No. You can't take the credit. Check the box on Form 1040 or 1040-SR, line 27c" (reached after Steps 1 to 4 and Step 5, question 2, Yes); p. 42, Step 5, question 3, whose STOP has no such instruction, "is your earned income less than $61,555 ($68,675 if married filing jointly)", "Yes. Go to Step 6. No. STOP You can’t take the credit" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.separated_box`

- **Authored helper label:** A married filer filing separately or as head of household who passes Step 3, questions 4 and 5, and answers No to question 6 (the special rule for separated spouses)
- **Encoded (Bool):** helper "Steps 1 and 2 passed, so Step 3 or Step 4 is asked" = true and helper "At least one qualifying child for the EIC" = true and helper "A married filer whose filing status is married filing separately or head of household" = true and helper "Step 3, questions 3 to 5: not a married filer filing separately or as head of household, or one who lived apart from the spouse for the last 6 months of 2025 or is legally separated and lived apart at the end of 2025" = true and helper "Could you be a qualifying child of another person for 2025?" = false
- Interpretation: amb.2025.separated_spouses_box
- Expr: `{"all":[{"eq":["eic.reached_step3",{"const":true}],"op":"test"},{"eq":["eic.has_qc",{"const":true}],"op":"test"},{"eq":["eic.married_rules",{"const":true}],"op":"test"},{"eq":["eic.step3_married",{"const":true}],"op":"test"},{"eq":["eic.qc_of_another",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 41, Step 3, question 6, "No. Check the box in the Dependents section that discusses the special rule for separated spouses"; p. 44, Special rule for separated spouses (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `eic.clergy`

- **Authored helper label:** A member of the clergy filing Schedule SE with an amount also on Form 1040, line 1z (refused; Schedule SE is outside the tool)
- **Encoded (Bool):** scope helper "Any income or adjustment requiring Schedule 1 other than the ones this tool asks about separately (business income or loss from Schedule C; a taxable state or local income tax refund; alimony under an agreement made before 2019; unemployment compensation; the line 8 items asked one by one; educator expenses; the HSA deduction; the deductible part of self-employment tax; self-employed SEP and SIMPLE contributions; the self-employed health insurance deduction; the penalty on early withdrawal of savings; the IRA deduction; student loan interest; jury duty pay you gave your employer), including statutory-employee wages or clergy income; church employee income (wages from a church that elected exemption from social security and Medicare taxes); other qualified retirement plans for the self-employed (such as a solo 401(k) or other Keogh plan); a refund or other recovery of an amount you deducted or took a credit for in an earlier year, other than a state or local income tax refund (for example a refund of general sales tax, real estate tax or personal property tax, a refund of mortgage interest in box 4 of Form 1098, a reimbursement of medical expenses, or a payment on a bad debt you deducted); sales of business property (Form 4797); a net operating loss deduction; rental real estate, royalties, partnerships, S corporations, estates or trusts (Schedule E or a Schedule K-1); rental of personal property; farm income (Schedule F); an exclusion of Medicaid waiver payments (Schedule 1 line 8s); or an adjustment on Schedule 1 line 12, 14 or 23? (Schedule 1-A deductions are asked separately.)" = true
- **Refusal:** when scope.schedule1 is true, cannot complete Clergy filing Schedule SE (Form 1040, line 27b). Schedule SE is outside this tool. Cite: [i1040gi] p. 43, Line 27b, and Clergy (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"eq":["scope.schedule1",{"const":true}],"op":"test"}`
- Cite: [i1040gi] p. 43, Line 27b (2025; printed date 2026-02-25; sha256 482e9c48)
