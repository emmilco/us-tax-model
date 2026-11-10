# Dependents — qualifying child and qualifying relative tests, per person listed

- Document: `dependent` (worksheet, tax year 2025)
- Collection: keyed entries; [f1040] Form 1040 (2025), Dependents, rows (1)–(7) (2025; created 2025-09-05; sha256 3d31c226)
- Note: One entry per person the filer lists. The tests of Steps 1 through 5 of "Who Qualifies as Your Dependent" are encoded per entry; the rules for married persons, children of divorced or separated parents, multiple support agreements and a child who is the qualifying child of another person are refused rather than decided. Temporary absences count as months lived with you, as the instructions say.

## (helper) — `dependent.relationship`

- **Authored helper label:** Relationship to you
- **Encoded (Enum(dependent_relationship)):** Input — Relationship to you:

  - child (son, daughter, stepchild, eligible foster child, or a descendant of any of them)
    - an adopted child, including a child lawfully placed with you for legal adoption, is your son or daughter
    - an eligible foster child is one placed with you by an authorized placement agency or by judgment, decree, or other order of any court of competent jurisdiction
    - a child in your care without such a placement who is not otherwise your relative is entered as household_member or other
  - sibling (brother, sister, half brother, half sister, stepbrother or stepsister, or a son or daughter of a brother, sister, half brother or half sister)
  - sibling_descendant (any other descendant of a sibling, such as a grandniece or a stepsibling's child)
  - parent (father or mother; not a foster parent, who is entered as other)
  - parent_relative (a grandparent, aunt or uncle: an ancestor or sibling of a parent)
  - in_law (step-parent or in-law, including one whose relationship began with a marriage that has since ended by death or divorce)
  - household_member (any other person, other than a person who was your spouse at any time during 2025, who lived with you all year as a member of your household, if your relationship did not violate local law)
  - other (any other relationship; such a person is a Step 4 relative only if they lived with you all year as a member of your household and the relationship did not violate local law)

  Do not list a person who was your spouse at any time during 2025: that person can't be your qualifying relative.

  Give the relationship to you; on a joint return, a relative of your spouse who is no relative of yours is entered as household_member or other, and a later question asks about the relationship to your spouse.
- Interpretation: amb.2025.foster_parent_relationship
- Expr: `{"op":"input","source":"Relationship to you:\n\n- child (son, daughter, stepchild, eligible foster child, or a descendant of any of them)\n  - an adopted child, including a child lawfully placed with you for legal adoption, is your son or daughter\n  - an eligible foster child is one placed with you by an authorized placement agency or by judgment, decree, or other order of any court of competent jurisdiction\n  - a child in your care without such a placement who is not otherwise your relative is entered as household_member or other\n- sibling (brother, sister, half brother, half sister, stepbrother or stepsister, or a son or daughter of a brother, sister, half brother or half sister)\n- sibling_descendant (any other descendant of a sibling, such as a grandniece or a stepsibling's child)\n- parent (father or mother; not a foster parent, who is entered as other)\n- parent_relative (a grandparent, aunt or uncle: an ancestor or sibling of a parent)\n- in_law (step-parent or in-law, including one whose relationship began with a marriage that has since ended by death or divorce)\n- household_member (any other person, other than a person who was your spouse at any time during 2025, who lived with you all year as a member of your household, if your relationship did not violate local law)\n- other (any other relationship; such a person is a Step 4 relative only if they lived with you all year as a member of your household and the relationship did not violate local law)\n\nDo not list a person who was your spouse at any time during 2025: that person can't be your qualifying relative.\n\nGive the relationship to you; on a joint return, a relative of your spouse who is no relative of yours is entered as household_member or other, and a later question asks about the relationship to your spouse."}`
- Cite: [i1040gi] pp. 17 and 19, Steps 1 and 4, "A qualifying child is your..." and "A qualifying relative is your..."; p. 20, Adopted child, "An adopted child includes a child lawfully placed with you for legal adoption"; p. 21, Foster child, "A foster child is any child placed with you by an authorized placement agency or by judgment, decree, or other order of any court of competent jurisdiction"; p501 p. 19, Relatives who don't have to live with you, "Your father, mother, grandparent, or other direct ancestor, but not foster parent"; p501 p. 19, Member of Household or Relationship Test, "If at any time during the year the person was your spouse, that person can’t be your qualifying relative."; p501 p. 19, "Any of these relationships that were established by marriage aren’t ended by death or divorce." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.age`

- **Authored helper label:** Age at the end of 2025
- **Encoded (Count):** Input — Age at the end of 2025 (whole years)
- Expr: `{"op":"input","source":"Age at the end of 2025 (whole years)"}`
- Cite: [i1040gi] p. 17, Step 1, "Under age 19 at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.student`

- **Authored helper label:** Full-time student in 2025?
- **Encoded (Bool):** Input — Was this person a full-time student in 2025, that is, during any part of 5 calendar months of 2025 (not necessarily consecutive), either of these?

  - enrolled for the hours or courses the school considers full-time attendance at a school that has a regular teaching staff and course of study and a regularly enrolled student body (an elementary school, junior or senior high school, college, university, or technical, trade or mechanical school)
  - taking a full-time, on-farm training course given by such a school or a state, county or local government agency

  A student who works on a "co-op" job in private industry as part of a school's regular course of classroom and practical training is a full-time student.

  An on-the-job training course, a correspondence school or a school offering courses only through the Internet does not count.
- Expr: `{"op":"input","source":"Was this person a full-time student in 2025, that is, during any part of 5 calendar months of 2025 (not necessarily consecutive), either of these?\n\n- enrolled for the hours or courses the school considers full-time attendance at a school that has a regular teaching staff and course of study and a regularly enrolled student body (an elementary school, junior or senior high school, college, university, or technical, trade or mechanical school)\n- taking a full-time, on-farm training course given by such a school or a state, county or local government agency\n\nA student who works on a \"co-op\" job in private industry as part of a school's regular course of classroom and practical training is a full-time student.\n\nAn on-the-job training course, a correspondence school or a school offering courses only through the Internet does not count."}`
- Cite: [i1040gi] p. 17, Step 1, "Under age 24 at the end of 2025, a full-time student (defined later)"; p. 21, Full-time student, "A full-time student is a child who during any part of 5 calendar months of 2025 was enrolled as a full-time student at a school"; p501 p. 13, Student defined, "1. A full-time student at a school that has a regular teaching staff and course of study, and a regularly enrolled student body at the school; or"; p501 p. 13, Full-time student, "A full-time student is a student who is enrolled for the number of hours or courses the school considers to be full-time attendance."; p501 p. 13, Vocational high school students, "Students who work on “co-op” jobs in private industry as a part of a school’s regular course of classroom and practical training are considered full-time students." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.disabled`

- **Authored helper label:** Permanently and totally disabled?
- **Encoded (Bool):** Input — Was this person permanently and totally disabled at any time in 2025, that is, unable to engage in any substantial gainful activity because of a physical or mental condition that a doctor has determined has lasted or can be expected to last continuously for at least a year or can be expected to lead to death?
- Expr: `{"op":"input","source":"Was this person permanently and totally disabled at any time in 2025, that is, unable to engage in any substantial gainful activity because of a physical or mental condition that a doctor has determined has lasted or can be expected to last continuously for at least a year or can be expected to lead to death?"}`
- Cite: [i1040gi] p. 17, Step 1, "Any age and permanently and totally disabled (defined later)"; p. 21, Permanently and totally disabled, "the person can’t engage in any substantial gainful activity because of a physical or mental condition" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.months`

- **Authored helper label:** Months lived with you in 2025, counting temporary absences
- **Encoded (Count):** Input — Months this person lived with you in 2025 (0–12)

  - counting temporary absences for school, vacation, business, medical care, military service or detention in a juvenile facility as time lived with you
  - counting a newborn's required hospital stay following birth as time lived with you
  - but not counting time a child presumed kidnapped was missing because of the kidnapping

  Enter 7 if the person lived with you for more than half of 2025 but fewer than 7 full months.

  For a person born, died, adopted or placed with you in 2025 who meets the other conditions to be your qualifying child, enter 12 if your home was their home for more than half the time they were alive or with you, and 0 otherwise.

  For any other person born or who died in 2025, or adopted, lawfully placed with you for legal adoption, or placed with you as an eligible foster child in 2025, enter 12 only if your home was their home for the entire time they were alive or since the adoption or placement, and 0 otherwise
- Expr: `{"op":"input","source":"Months this person lived with you in 2025 (0–12)\n\n- counting temporary absences for school, vacation, business, medical care, military service or detention in a juvenile facility as time lived with you\n- counting a newborn's required hospital stay following birth as time lived with you\n- but not counting time a child presumed kidnapped was missing because of the kidnapping\n\nEnter 7 if the person lived with you for more than half of 2025 but fewer than 7 full months.\n\nFor a person born, died, adopted or placed with you in 2025 who meets the other conditions to be your qualifying child, enter 12 if your home was their home for more than half the time they were alive or with you, and 0 otherwise.\n\nFor any other person born or who died in 2025, or adopted, lawfully placed with you for legal adoption, or placed with you as an eligible foster child in 2025, enter 12 only if your home was their home for the entire time they were alive or since the adoption or placement, and 0 otherwise"}`
- Cite: [i1040gi] p. 17, Step 1, "Who lived with you for more than half of 2025"; p501 p. 13, Death or birth of child, "The same is true if the child lived with you more than half the year except for any required hospital stay following birth."; p501 p. 13, Kidnapped child, "You can treat your child as meeting the residency test even if the child has been kidnapped, but the following statements must be true."; p. 21, Exception to time lived with you ("the person is considered to have lived with you for more than half of 2025 if your home was this person's home for more than half the time the person was alive in 2025"; "Any other person is considered to have lived with you for all of 2025 if the person was born or died in 2025 and your home was this person's home for the entire time the person was alive in 2025") (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.self_support`

- **Authored helper label:** Provided over half of their own support?
- **Encoded (Bool):** Input — Did this person provide over half of their own support for 2025?

  Total support is the amount spent for their food, lodging, clothing, education, medical and dental care, recreation, transportation and similar necessities, including tax-exempt income, savings and borrowed amounts used for their support and GI Bill tuition payments and allowances.

  It does not include:
  - income, social security or Medicare taxes paid from their own income
  - life insurance premiums
  - funeral expenses
  - medical insurance benefits (including Medicare benefits)
  - Survivors' and Dependents' Educational Assistance payments used for the support of the child who receives them

  Count the person's own funds only if actually spent for their support (support the person paid for with their own wages is theirs, even if you paid the wages, and a person living in their own home provides its fair rental value).

  Count lodging at its fair rental value and property, such as a car the person bought with their own funds, at its fair market value.

  Payments you receive from a child placement agency, state or county for a foster child's support are support provided by the agency, state or county, and benefits a state provides to this person as a needy person (welfare, food benefits, housing, etc.) are support provided by the state, not by the person.

  Do not count a scholarship the person received as a student.

  Social security benefits the person receives and uses for their own support are support the person provided.
- Expr: `{"op":"input","source":"Did this person provide over half of their own support for 2025?\n\nTotal support is the amount spent for their food, lodging, clothing, education, medical and dental care, recreation, transportation and similar necessities, including tax-exempt income, savings and borrowed amounts used for their support and GI Bill tuition payments and allowances.\n\nIt does not include:\n- income, social security or Medicare taxes paid from their own income\n- life insurance premiums\n- funeral expenses\n- medical insurance benefits (including Medicare benefits)\n- Survivors' and Dependents' Educational Assistance payments used for the support of the child who receives them\n\nCount the person's own funds only if actually spent for their support (support the person paid for with their own wages is theirs, even if you paid the wages, and a person living in their own home provides its fair rental value).\n\nCount lodging at its fair rental value and property, such as a car the person bought with their own funds, at its fair market value.\n\nPayments you receive from a child placement agency, state or county for a foster child's support are support provided by the agency, state or county, and benefits a state provides to this person as a needy person (welfare, food benefits, housing, etc.) are support provided by the state, not by the person.\n\nDo not count a scholarship the person received as a student.\n\nSocial security benefits the person receives and uses for their own support are support the person provided."}`
- Cite: [i1040gi] p. 17, Step 1, "Who didn't provide over half of their own support for 2025"; p501 p. 15, Support Test (To Be a Qualifying Child), "However, to see what is or isn’t support, see Support Test (To Be a Qualifying Relative), later."; p501 p. 19, "A person’s own funds aren’t support unless they are actually spent for support."; p501 p. 20, "For lodging, the amount of support is the fair rental value of the lodging."; p501 p. 20, "You can’t include in your contribution to your child’s support any support paid for by the child with the child’s own wages, even if you paid the wages."; p501 p. 15, Foster care payments and expenses, "Payments you receive for the support of a foster child from a child placement agency are considered support provided by the agency."; p501 p. 15, Scholarships, "A scholarship received by a child who is a student isn’t taken into account in determining whether the child provided more than half of their own support."; p501 p. 20, "If a child receives social security benefits and uses them toward their own support, the benefits are considered as provided by the child."; p501 p. 20, Total Support, "Total support includes amounts spent to provide food, lodging, clothing, education, medical and dental care, recreation, transportation, and similar necessities."; p501 p. 20, Tax-exempt income, "In figuring a person’s total support, include tax-exempt income, savings, and borrowed amounts used to support that person."; p501 p. 20, Support provided by the state (welfare, food benefits, housing, etc.), "Benefits provided by the state to a needy person are generally considered support provided by the state."; p501 p. 15, "Similarly, payments you receive for the support of a foster child from a state or county are considered support provided by the state or county."; p501 p. 21, Person living in their own home, "The total fair rental value of a person’s home that the person owns is considered support contributed by that person."; p501 p. 21, Property, "Property provided as support is measured by its fair market value."; p501 p. 21, Capital expenses, "Because the car is bought and owned by your child, the car’s fair market value ($4,500) must be included in your child’s support."; p501 p. 21, Medical insurance benefits, "Medical insurance benefits, including basic and supplementary Medicare benefits, aren’t part of support."; p501 p. 21, Tuition payments and allowances under the GI Bill, "Amounts veterans receive under the GI Bill for tuition payments and allowances while they attend school are included in total support."; p501 p. 21, Don’t Include in Total Support, "1. Federal, state, and local income taxes paid by persons from their own income.", "2. Social security and Medicare taxes paid by persons from their own income.", "3. Life insurance premiums.", "4. Funeral expenses." and "6. Survivors’ and Dependents’ Educational Assistance payments used for the support of the child who receives them." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.joint_return`

- **Authored helper label:** Included on a 2025 joint return filed other than only to claim a refund?
- **Encoded (Bool):** Input — Is a joint return being filed for 2025 that includes this person (including one filed by this person with a spouse who died during 2025, or by this person's surviving spouse after this person died during 2025), other than one filed only to claim a refund of withheld or estimated tax?
- Expr: `{"op":"input","source":"Is a joint return being filed for 2025 that includes this person (including one filed by this person with a spouse who died during 2025, or by this person's surviving spouse after this person died during 2025), other than one filed only to claim a refund of withheld or estimated tax?"}`
- Cite: [i1040gi] p. 17, Step 1, "Who isn't filing a joint return for 2025 or is filing a joint return for 2025 only to claim a refund"; p. 21, Married person, "If the person is married and files a joint return, you can’t claim that person as your dependent." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.citizen`

- **Authored helper label:** U.S. citizen, U.S. national or U.S. resident alien?
- **Encoded (Bool):** Input — Was this person a U.S. citizen, U.S. national or U.S. resident alien? (Answer yes for your adopted child who lived with you all year as a member of your household, if you are a U.S. citizen or U.S. national.)
- Expr: `{"op":"input","source":"Was this person a U.S. citizen, U.S. national or U.S. resident alien? (Answer yes for your adopted child who lived with you all year as a member of your household, if you are a U.S. citizen or U.S. national.)"}`
- Cite: [i1040gi] p. 18, Step 2, question 1, and Step 3, question 2; p. 20, Exception to citizen test ("If you are a U.S. citizen or U.S. national and your adopted child lived with you all year as a member of your household, that child meets the requirement to be a U.S. citizen in Step 2, question 1; Step 3, question 2; Step 4, question 2; and Step 5, question 3") (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.canada_mexico`

- **Authored helper label:** Resident of Canada or Mexico (if not a U.S. citizen, national or resident alien)?
- **Encoded (Bool):** Input — If not a U.S. citizen, national or resident alien, was this person a resident of Canada or Mexico?
- Expr: `{"op":"input","source":"If not a U.S. citizen, national or resident alien, was this person a resident of Canada or Mexico?"}`
- Cite: [i1040gi] p. 18, Step 2, question 1, "or a resident of Canada or Mexico" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.married`

- **Authored helper label:** Married, or included on a 2025 joint return?
- **Encoded (Bool):** Input — Was this person married at the end of 2025 (a person legally separated under a decree of divorce or separate maintenance is not married), or is a joint return being filed for 2025 that includes this person (including one filed by this person with a spouse who died during 2025, or by this person's surviving spouse after this person died during 2025)?
- Expr: `{"op":"input","source":"Was this person married at the end of 2025 (a person legally separated under a decree of divorce or separate maintenance is not married), or is a joint return being filed for 2025 that includes this person (including one filed by this person with a spouse who died during 2025, or by this person's surviving spouse after this person died during 2025)?"}`
- Cite: [i1040gi] p. 18, Step 2, question 2, "Was the child married? Yes. See Married person, later"; p. 21, Married person, "If the person is married and files a joint return, you can’t claim that person as your dependent." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.tin`

- **Authored helper label:** SSN, ITIN or ATIN issued on or before the due date of your return?
- **Encoded (Bool):** Input — Did this person have an SSN, ITIN or ATIN issued on or before the due date of your 2025 return (including extensions), or have you applied for an ITIN or ATIN for this person by then? An ITIN that has expired counts only if it has been renewed, or renewal applied for, by then.
- Expr: `{"op":"input","source":"Did this person have an SSN, ITIN or ATIN issued on or before the due date of your 2025 return (including extensions), or have you applied for an ITIN or ATIN for this person by then? An ITIN that has expired counts only if it has been renewed, or renewal applied for, by then."}`
- Cite: [i1040gi] p. 18, Step 3, question 1, and p. 19, Step 5, question 2; p503 p. 3, "If your ITIN wasn’t included on at least one U.S. federal tax return for the last 3 consecutive tax years, it expires on December 31 of the third consecutive tax year, and must be renewed before being used again on a U.S. federal tax return." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.work_ssn`

- **Authored helper label:** SSN valid for employment issued before the due date of your return?
- **Encoded (Bool):** Input — Did this person have an SSN valid for employment, issued before the due date of your 2025 return (including extensions)? If the card says "Valid for Work Only With DHS Authorization", answer yes only if the DHS authorization is valid.
- Expr: `{"op":"input","source":"Did this person have an SSN valid for employment, issued before the due date of your 2025 return (including extensions)? If the card says \"Valid for Work Only With DHS Authorization\", answer yes only if the DHS authorization is valid."}`
- Cite: [i1040gi] p. 18, Step 3, question 4; p. 22, "if “Valid for Work Only With DHS Authorization” is printed on your child’s social security card, your child has the required SSN only as long as the DHS authorization is valid" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.gross_income`

- **Authored helper label:** Gross income for 2025
- **Encoded (NonNegDollars):** Input — This person's gross income for 2025, which is all income in the form of money, property, and services that isn't exempt from tax. Include gross receipts from rental property without deducting taxes, repairs or other expenses, a partner's share of the gross (not net) partnership income, business sales minus the cost of goods sold in a manufacturing, merchandising or mining business, and all taxable unemployment compensation, taxable social security benefits and certain amounts received as scholarship and fellowship grants. Do not include nontaxable social security benefits or other tax-exempt income.
- Expr: `{"op":"input","source":"This person's gross income for 2025, which is all income in the form of money, property, and services that isn't exempt from tax. Include gross receipts from rental property without deducting taxes, repairs or other expenses, a partner's share of the gross (not net) partnership income, business sales minus the cost of goods sold in a manufacturing, merchandising or mining business, and all taxable unemployment compensation, taxable social security benefits and certain amounts received as scholarship and fellowship grants. Do not include nontaxable social security benefits or other tax-exempt income."}`
- Cite: [i1040gi] p. 19, Step 4, "Who had gross income of less than $5,200 in 2025"; p501 p. 19, Gross income defined, "Gross income is all income in the form of money, property, and services that isn’t exempt from tax."; p501 p. 19, "Gross receipts from rental property are gross income. Don’t deduct taxes, repairs, or other expenses to determine the gross income from rental property."; p501 p. 19, "Gross income includes a partner’s share of the gross (not net) partnership income."; p501 p. 19, "Gross income also includes all taxable unemployment compensation, taxable social security benefits, and certain amounts received as scholarship and fellowship grants." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.supported`

- **Authored helper label:** You provided over half of this person's support?
- **Encoded (Bool):** Input — Did you provide over half of this person's support in 2025?

  Total support is the amount spent for the person's food, lodging, clothing, education, medical and dental care, recreation, transportation and similar necessities, including their tax-exempt income, savings and borrowed amounts used for their support and GI Bill tuition payments and allowances.

  It does not include:
  - income, social security or Medicare taxes the person paid from their own income
  - life insurance premiums
  - funeral expenses
  - a scholarship your child received as a student
  - Survivors' and Dependents' Educational Assistance payments used for the support of the child who receives them

  TANF or other public assistance payments you received and used to support this person count as support you provided.

  Count:
  - lodging at its fair rental value, which includes a reasonable allowance for furniture, appliances, heat and other utilities provided
    - a person living in their own home provides its fair rental value
    - if you provide only part of the lodging and the person supplies the rest, divide the fair rental value by how much each of you provides
    - if you live rent free in this person's home, reduce your support by the fair rental value of the lodging they provide you
  - property at its fair market value
  - expenses for the whole household, such as food, divided among its members

  Medical insurance premiums you pay, including premiums for supplementary Medicare coverage, are support you provide; medical insurance benefits, including Medicare benefits, are not support.

  Count both the government's part and the part taken out of your military pay of an Armed Forces dependency allotment, and a tax-exempt military quarters allowance, as yours, and count payments you make for the person's child or dependent care as yours.

  A lump-sum advance payment to a home for the aged for a relative's care for life, based on their life expectancy, counts each year as the payment divided by that life expectancy.

  A capital item such as furniture, an appliance or a car counts only if bought for the person and given to them, not one the household shares or that you own and let them use.

  The person's own funds are support only if actually spent for their support.

  Payments you receive from a child placement agency, state or county for a foster child's support are support provided by the agency, state or county, not by you; your unreimbursed foster care expenses are not support you provided if you are in the trade or business of providing foster care or if they are deductible as a charitable contribution.

  Support your child paid for with the child's own wages is not yours, even if you paid the wages.

  Benefits a state provides to this person as a needy person (welfare, food benefits, housing, etc.) are support provided by the state, not by you; but payments based on need are not counted entirely as this person's support if part of them can be shown not to have been used for it.

  When spouses receive social security benefits by one check made out to both of them, half is support of each spouse unless they can show otherwise.

  Alimony or separate maintenance payments to a spouse (or similar payments from an estate or trust) are not support of a dependent.

  The year you provide support is the year you pay for it, even with borrowed money you repay later.
- Expr: `{"op":"input","source":"Did you provide over half of this person's support in 2025?\n\nTotal support is the amount spent for the person's food, lodging, clothing, education, medical and dental care, recreation, transportation and similar necessities, including their tax-exempt income, savings and borrowed amounts used for their support and GI Bill tuition payments and allowances.\n\nIt does not include:\n- income, social security or Medicare taxes the person paid from their own income\n- life insurance premiums\n- funeral expenses\n- a scholarship your child received as a student\n- Survivors' and Dependents' Educational Assistance payments used for the support of the child who receives them\n\nTANF or other public assistance payments you received and used to support this person count as support you provided.\n\nCount:\n- lodging at its fair rental value, which includes a reasonable allowance for furniture, appliances, heat and other utilities provided\n  - a person living in their own home provides its fair rental value\n  - if you provide only part of the lodging and the person supplies the rest, divide the fair rental value by how much each of you provides\n  - if you live rent free in this person's home, reduce your support by the fair rental value of the lodging they provide you\n- property at its fair market value\n- expenses for the whole household, such as food, divided among its members\n\nMedical insurance premiums you pay, including premiums for supplementary Medicare coverage, are support you provide; medical insurance benefits, including Medicare benefits, are not support.\n\nCount both the government's part and the part taken out of your military pay of an Armed Forces dependency allotment, and a tax-exempt military quarters allowance, as yours, and count payments you make for the person's child or dependent care as yours.\n\nA lump-sum advance payment to a home for the aged for a relative's care for life, based on their life expectancy, counts each year as the payment divided by that life expectancy.\n\nA capital item such as furniture, an appliance or a car counts only if bought for the person and given to them, not one the household shares or that you own and let them use.\n\nThe person's own funds are support only if actually spent for their support.\n\nPayments you receive from a child placement agency, state or county for a foster child's support are support provided by the agency, state or county, not by you; your unreimbursed foster care expenses are not support you provided if you are in the trade or business of providing foster care or if they are deductible as a charitable contribution.\n\nSupport your child paid for with the child's own wages is not yours, even if you paid the wages.\n\nBenefits a state provides to this person as a needy person (welfare, food benefits, housing, etc.) are support provided by the state, not by you; but payments based on need are not counted entirely as this person's support if part of them can be shown not to have been used for it.\n\nWhen spouses receive social security benefits by one check made out to both of them, half is support of each spouse unless they can show otherwise.\n\nAlimony or separate maintenance payments to a spouse (or similar payments from an estate or trust) are not support of a dependent.\n\nThe year you provide support is the year you pay for it, even with borrowed money you repay later."}`
- Cite: [i1040gi] p. 19, Step 4, "For whom you provided over half of the person's support in 2025"; p. 21, Public assistance payments; p501 p. 20, TANF and other governmental payments, "those payments are considered support you provided for that person"; p501 p. 20, "For lodging, the amount of support is the fair rental value of the lodging."; p501 p. 20, Armed Forces dependency allotments, "The part of the allotment contributed by the government and the part taken out of your military pay are both considered provided by you in figuring whether you provide more than half of the support."; p501 p. 19, "A person’s own funds aren’t support unless they are actually spent for support."; p501 p. 20, Foster care, "Payments you receive for the support of a foster child from a child placement agency are considered support provided by the agency."; p501 p. 15, "Similarly, payments you receive for the support of a foster child from a state or county are considered support provided by the state or county."; p501 p. 20, Child’s wages used for own support, "You can’t include in your contribution to your child’s support any support paid for by the child with the child’s own wages, even if you paid the wages."; p501 p. 20, Support provided by the state (welfare, food benefits, housing, etc.), "Benefits provided by the state to a needy person are generally considered support provided by the state."; p501 p. 20, Total Support, "Total support includes amounts spent to provide food, lodging, clothing, education, medical and dental care, recreation, transportation, and similar necessities."; p501 p. 20, Tax-exempt income, "In figuring a person’s total support, include tax-exempt income, savings, and borrowed amounts used to support that person."; p501 p. 20, "Expenses not directly related to any one member of a household, such as the cost of food for the household, must be divided among the members of the household."; p501 p. 20, Year support is provided, "The year you provide the support is the year you pay for it, even if you do so with borrowed money that you repay in a later year."; p501 p. 20, Tax-exempt military quarters allowances, "These allowances are treated the same way as dependency allotments in figuring support."; p501 p. 20, Home for the aged, "the amount of support you provide each year is the lump-sum payment divided by the relative’s life expectancy"; p501 p. 21, Person living in their own home, "The total fair rental value of a person’s home that the person owns is considered support contributed by that person."; p501 p. 21, Living with someone rent free, "you must reduce the amount you provide for support of that person by the fair rental value of lodging the person provides you"; p501 p. 21, Property, "Property provided as support is measured by its fair market value."; p501 p. 21, Capital expenses, "Because you own the car and don’t give it to your child but merely let your child use it, don’t include the cost of the car in your child’s total support."; p501 p. 21, Medical insurance premiums, "Medical insurance premiums you pay, including premiums for supplementary Medicare coverage, are included in the support you provide."; p501 p. 21, Medical insurance benefits, "Medical insurance benefits, including basic and supplementary Medicare benefits, aren’t part of support."; p501 p. 21, Tuition payments and allowances under the GI Bill, "Amounts veterans receive under the GI Bill for tuition payments and allowances while they attend school are included in total support."; p501 p. 21, Childcare expenses, "If you pay someone to provide child or dependent care, you can include these payments in the amount you provided for the support of your child or disabled dependent"; p501 p. 21, Don’t Include in Total Support, "1. Federal, state, and local income taxes paid by persons from their own income.", "2. Social security and Medicare taxes paid by persons from their own income.", "3. Life insurance premiums.", "4. Funeral expenses.", "5. Scholarships received by your child if your child is a student." and "6. Survivors’ and Dependents’ Educational Assistance payments used for the support of the child who receives them."; p501 p. 15, Foster care payments and expenses, "If you are in the trade or business of providing foster care, your unreimbursed expenses aren’t considered support provided by you."; p501 p. 20, Lodging, "Fair rental value includes a reasonable allowance for the use of furniture and appliances, and for heat and other utilities that are provided."; p501 p. 21, "If you don’t provide the total lodging, the total fair rental value must be divided depending on how much of the total lodging you provide."; p501 p. 20, Support provided by the state, "However, payments based on the needs of the recipient won’t be considered as used entirely for that person’s support if it is shown that part of the payments weren’t used for that purpose."; p501 p. 20, Social security benefits, "If spouses each receive benefits that are paid by one check made out to both of them, half of the total paid is considered to be for the support of each spouse, unless they can show otherwise."; p501 p. 22, Alimony, "Payments to a spouse that are alimony or separate maintenance payments, or similar payments from an estate or trust, aren’t treated as a payment for the support of a dependent." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.kidnapped`

- **Authored helper label:** A child kidnapped by someone who isn't a member of your family or the child's family, presumed kidnapped by law enforcement, and missing because of it at some time in 2025?
- **Encoded (Bool):** Input — Is this person a child who was kidnapped by someone who isn't a member of your family or the child's family, whom law enforcement authorities presume to have been kidnapped, and who was missing because of the kidnapping at some time during 2025 (a kidnapping in 2025, or an earlier kidnapping before the child's return)? Answer yes even if law enforcement first presumed the kidnapping after 2025, or the child has since been returned.
- Expr: `{"op":"input","source":"Is this person a child who was kidnapped by someone who isn't a member of your family or the child's family, whom law enforcement authorities presume to have been kidnapped, and who was missing because of the kidnapping at some time during 2025 (a kidnapping in 2025, or an earlier kidnapping before the child's return)? Answer yes even if law enforcement first presumed the kidnapping after 2025, or the child has since been returned."}`
- Cite: [i1040gi] p. 21, Kidnapped child, "If your child is presumed by law enforcement authorities to have been kidnapped by someone who isn’t a family member, you may be able to take the child into account"; p501 p. 13, Kidnapped child, "1. The child is presumed by law enforcement authorities to have been kidnapped by someone who isn’t a member of your family or the child’s family.", "2. In the year the kidnapping occurred, the child lived with you for more than half of the part of the year before the date of the kidnapping." and "3. In the year of the child’s return, the child lived with you for more than half the part of the year following the date of the child’s return."; p501 p. 13, "This treatment applies for all years until the earlier of"; p501 p. 18, Kidnapped child, "You can treat a child as your qualifying relative even if the child has been kidnapped" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.other_claimant`

- **Authored helper label:** Meets the conditions to be the qualifying child of another person?
- **Encoded (Bool):** Input — Does this person meet the conditions to be the qualifying child of any other person for 2025, under the dependent rules or under the EIC rules (which have no support test)?
- Expr: `{"op":"input","source":"Does this person meet the conditions to be the qualifying child of any other person for 2025, under the dependent rules or under the EIC rules (which have no support test)?"}`
- Cite: [i1040gi] p. 17, Step 1, "If the child meets the conditions to be a qualifying child of any other person ... see Qualifying child of more than one person" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.other_nontaxpayer`

- **Authored helper label:** Every other person this person is a qualifying child of is not a taxpayer?
- **Encoded (Bool):** Input — If this person meets the conditions to be the qualifying child of another person: is every such other person not a taxpayer for 2025? A person is not a taxpayer if they are not required to file a 2025 U.S. income tax return and either do not file one or file only to get a refund of withheld income tax or estimated tax paid (claiming no earned income credit or other tax credit or deduction), or if they are not a U.S. citizen and have no U.S. gross income.
- Expr: `{"op":"input","source":"If this person meets the conditions to be the qualifying child of another person: is every such other person not a taxpayer for 2025? A person is not a taxpayer if they are not required to file a 2025 U.S. income tax return and either do not file one or file only to get a refund of withheld income tax or estimated tax paid (claiming no earned income credit or other tax credit or deduction), or if they are not a U.S. citizen and have no U.S. gross income."}`
- Cite: [i1040gi] p. 19, Step 4, "Who wasn’t a qualifying child (see Step 1) of any taxpayer for 2025. For this purpose, a person isn’t a taxpayer if the person isn’t required to file a U.S. income tax return and either doesn’t file such a return or files only to get a refund of withheld income tax or estimated tax paid."; p501 p. 18, Example 2—return filed to claim refund, "Your friend files a return only to get a refund of the income tax withheld and doesn’t claim the earned income credit or any other tax credits or deductions."; p501 p. 18, Child in Canada or Mexico, "If the persons the child does live with aren’t U.S. citizens and have no U.S. gross income, those persons aren’t “taxpayers,” so the child isn’t the qualifying child of any other taxpayer." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.divorced_rule`

- **Authored helper label:** Rule for children of divorced or separated parents applies?
- **Encoded (Bool):** Input — Does the special rule for children of divorced or separated parents, or parents who lived apart (including parents who never married), apply to this person, for example because a Form 8332 release or a decree lets the noncustodial parent claim the child? Answer yes whether you are the custodial parent who signed the release (or whose decree or agreement lets the other parent claim the child) or the noncustodial parent using it. A release the custodial parent has revoked still applies for 2025 unless written notice of the revocation was given (or reasonable efforts were made to give it) to the noncustodial parent in 2024 or earlier.
- Expr: `{"op":"input","source":"Does the special rule for children of divorced or separated parents, or parents who lived apart (including parents who never married), apply to this person, for example because a Form 8332 release or a decree lets the noncustodial parent claim the child? Answer yes whether you are the custodial parent who signed the release (or whose decree or agreement lets the other parent claim the child) or the noncustodial parent using it. A release the custodial parent has revoked still applies for 2025 unless written notice of the revocation was given (or reasonable efforts were made to give it) to the noncustodial parent in 2024 or earlier."}`
- Cite: [i1040gi] p. 19, Step 4, "But see Children of divorced or separated parents"; p. 20, Children of divorced or separated parents, "If conditions (1) through (4) apply, only the noncustodial parent can claim the child for purposes of the child tax credit and credit for other dependents"; p501 p. 22, Revocation of release of claim to an exemption, "For the revocation to be effective for 2025, the custodial parent must have given (or made reasonable efforts to give) written notice of the revocation to the noncustodial parent in 2024 or earlier." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.multiple_support`

- **Authored helper label:** Claimed under a multiple support agreement?
- **Encoded (Bool):** Input — Did you and others together provide over half of this person's support for 2025, with no one person providing over half (a multiple support situation), whether you or another contributor claims the person?
- Expr: `{"op":"input","source":"Did you and others together provide over half of this person's support for 2025, with no one person providing over half (a multiple support situation), whether you or another contributor claims the person?"}`
- Cite: [i1040gi] p. 19, Step 4, "Multiple support agreements" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.parent_home_paid`

- **Authored helper label:** For a parent not living with you, you paid over half the cost of their main home for all of 2025 (or the part of 2025 they were alive)?
- **Encoded (Bool):** Input — If this person is your parent, did you pay over half the cost of keeping up a home that was their main home for all of 2025 (or, if your parent died in 2025, for the entire part of 2025 your parent was alive)?

  A rest home or home for the elderly counts as your parent's main home if you paid over half the cost of keeping your parent there.

  Cost of keeping up a home includes expenses such as:
  - rent
  - mortgage interest
  - real estate taxes
  - insurance on the home
  - repairs
  - utilities
  - food eaten in the home

  It does not include:
  - the cost of clothing, education, medical treatment, vacations, life insurance, or transportation
  - the value of your services or those of a member of your household

  Money your parent spent on the home out of their own income, such as Social Security, counts as paid by your parent, not by you.

  TANF or other similar payments you received and used to keep up the home count as paid by you.
- Expr: `{"op":"input","source":"If this person is your parent, did you pay over half the cost of keeping up a home that was their main home for all of 2025 (or, if your parent died in 2025, for the entire part of 2025 your parent was alive)?\n\nA rest home or home for the elderly counts as your parent's main home if you paid over half the cost of keeping your parent there.\n\nCost of keeping up a home includes expenses such as:\n- rent\n- mortgage interest\n- real estate taxes\n- insurance on the home\n- repairs\n- utilities\n- food eaten in the home\n\nIt does not include:\n- the cost of clothing, education, medical treatment, vacations, life insurance, or transportation\n- the value of your services or those of a member of your household\n\nMoney your parent spent on the home out of their own income, such as Social Security, counts as paid by your parent, not by you.\n\nTANF or other similar payments you received and used to keep up the home count as paid by you."}`
- Cite: [i1040gi] p. 14, Head of Household, Test 1; p. 15, "If the person is anyone else, see Pub. 501"; p501 p. 9, Death or birth, "Your parent for whom you paid, for the entire part of the year your parent was alive, more than half the cost of keeping up the home your parent lived in"; p501 p. 9, "If you pay more than half the cost of keeping your parent in a rest home or home for the elderly, that counts as paying more than half the cost of keeping up your parent’s main home." p501 p. 9, Keeping Up a Home, "Costs you include. Include in the cost of keeping up a home expenses such as rent, mortgage interest, real estate taxes, insurance on the home, repairs, utilities, and food eaten in the home." p501 p. 9, "Costs you don’t include. Don’t include the cost of clothing, education, medical treatment, vacations, life insurance, or transportation. Also don’t include the value of your services or those of a member of your household." p501 p. 9, Note, "Amounts paid out of funds received in the child’s or qualifying person’s name, such as Social Security, are considered paid by the child, not you."; p501 p. 9, Note, "if you received Temporary Assistance to Needy Families (TANF) payments or other similar payments and used the payment to support another person, those payments are considered support you provided for that person, rather than support provided by the government or other third party." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.born_died`

- **Authored helper label:** Born or died in 2025?
- **Encoded (Bool):** Input — Was this person born in 2025, or did this person die in 2025? A child born in 2025 is born alive only if state or local law treats the child as born alive and an official document, such as a birth certificate, shows the live birth (even if the child lived only for a moment). Do not list a stillborn child.
- Expr: `{"op":"input","source":"Was this person born in 2025, or did this person die in 2025? A child born in 2025 is born alive only if state or local law treats the child as born alive and an official document, such as a birth certificate, shows the live birth (even if the child lived only for a moment). Do not list a stillborn child."}`
- Cite: [i1040gi] p. 15, "If the person for whom you kept up a home was born or died in 2025, you still may be able to file as head of household"; p501 p. 13, Child born alive, "State or local law must treat the child as having been born alive. There must be proof of a live birth shown by an official document, such as a birth certificate."; p501 p. 13, Stillborn child, "You can’t claim a stillborn child as a dependent." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.placed`

- **Authored helper label:** Adopted, placed for adoption or placed as a foster child in 2025?
- **Encoded (Bool):** Input — Did you adopt this person in 2025, or was this person lawfully placed with you for legal adoption by you, or placed with you as an eligible foster child, during 2025?
- Expr: `{"op":"input","source":"Did you adopt this person in 2025, or was this person lawfully placed with you for legal adoption by you, or placed with you as an eligible foster child, during 2025?"}`
- Cite: [i1040gi] p. 15, "Similarly, if you adopted the person for whom you kept up a home in 2025, the person was lawfully placed with you for legal adoption by you in 2025, or the person was an eligible foster child placed with you during 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.part_year_home`

- **Authored helper label:** Lived with you more than half the part of 2025 they were alive, or since the adoption or placement?
- **Encoded (Bool):** Input — Was your home this person's home for more than half of the part of 2025 they were alive (or, for a person adopted or placed with you in 2025, more than half of the time since the adoption or placement), counting temporary absences for school, vacation, business, medical care, military service or detention in a juvenile facility as time lived with you?
- Expr: `{"op":"input","source":"Was your home this person's home for more than half of the part of 2025 they were alive (or, for a person adopted or placed with you in 2025, more than half of the time since the adoption or placement), counting temporary absences for school, vacation, business, medical care, military service or detention in a juvenile facility as time lived with you?"}`
- Cite: [p501] p. 9, Death or birth, "Your qualifying child or qualifying relative who lived with you for more than half the part of the year they were alive"; i1040gi p. 15, "more than half the time since the person was adopted or placed with you in 2025"; i1040gi pp. 14-15, temporary absences, "or detention in a juvenile facility" (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (helper) — `dependent.hoh_part_year`

- **Authored helper label:** For a relative other than a qualifying child who did not live with you more than half of 2025: born or died in 2025, or adopted or placed, and lived with you more than half of the part of the year
- **Encoded (Bool):** Choose — [helper "Qualifying child (Step 1)" = true → helper "Year parameter household.no (false)"] [helper "Qualifying child (Step 1)" = false → helper "Born or died in 2025, or adopted or placed with you in 2025, and lived with you more than half of the part of the year"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.qualifying_child",{"const":true}],"op":"test"},"then":"dependent.no"},{"guard":{"eq":["dependent.qualifying_child",{"const":false}],"op":"test"},"then":"dependent.hoh_part_year_relative"}],"op":"choose"}`
- Cite: [p501] p. 9, Death or birth, "To qualify you for head of household filing status, the qualifying person (as defined in Table 4) must be one of the following"; i1040gi p. 15, "the person is considered to have lived with you for more than half of 2025 if your main home was this person's main home for more than half the time since the person was adopted or placed with you in 2025" (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (helper) — `dependent.hoh_part_year_relative`

- **Authored helper label:** Born or died in 2025, or adopted or placed with you in 2025, and lived with you more than half of the part of the year
- **Encoded (Bool):** Choose — [helper "Born or died in 2025, or adopted or placed with you in 2025" = true → helper "Lived with you more than half the part of 2025 they were alive, or since the adoption or placement?"] [helper "Born or died in 2025, or adopted or placed with you in 2025" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.born_died_or_placed",{"const":true}],"op":"test"},"then":"dependent.part_year_home"},{"guard":{"eq":["dependent.born_died_or_placed",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [p501] p. 9, Death or birth, "To qualify you for head of household filing status, the qualifying person (as defined in Table 4) must be one of the following"; i1040gi p. 15, "the person is considered to have lived with you for more than half of 2025 if your main home was this person's main home for more than half the time since the person was adopted or placed with you in 2025" (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (helper) — `dependent.born_died_or_placed`

- **Authored helper label:** Born or died in 2025, or adopted or placed with you in 2025
- **Encoded (Bool):** Choose — [helper "Born or died in 2025?" = true → helper "Born or died in 2025?"] [helper "Born or died in 2025?" = false → helper "Adopted, placed for adoption or placed as a foster child in 2025?"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.born_died",{"const":true}],"op":"test"},"then":"dependent.born_died"},{"guard":{"eq":["dependent.born_died",{"const":false}],"op":"test"},"then":"dependent.placed"}],"op":"choose"}`
- Cite: [p501] p. 9, Death or birth, "To qualify you for head of household filing status, the qualifying person (as defined in Table 4) must be one of the following"; i1040gi p. 15, "the person is considered to have lived with you for more than half of 2025 if your main home was this person's main home for more than half the time since the person was adopted or placed with you in 2025" (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (helper) — `dependent.hoh_lived_half`

- **Authored helper label:** Lived with you more than half of 2025, or, for a relative other than a qualifying child (whose months already count the part of the year), more than half of the part of 2025 they were alive or since their adoption or placement
- **Encoded (Bool):** Choose — [helper "Lived with you for more than half of 2025" = true → helper "Lived with you for more than half of 2025"] [helper "Lived with you for more than half of 2025" = false → helper "For a relative other than a qualifying child who did not live with you more than half of 2025: born or died in 2025, or adopted or placed, and lived with you more than half of the part of the year"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.lived_half",{"const":true}],"op":"test"},"then":"dependent.lived_half"},{"guard":{"eq":["dependent.lived_half",{"const":false}],"op":"test"},"then":"dependent.hoh_part_year"}],"op":"choose"}`
- Cite: [p501] p. 9, Death or birth, "To qualify you for head of household filing status, the qualifying person (as defined in Table 4) must be one of the following"; i1040gi p. 15, "the person is considered to have lived with you for more than half of 2025 if your main home was this person's main home for more than half the time since the person was adopted or placed with you in 2025" (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (helper) — `dependent.dc_lived_half`

- **Authored helper label:** Lived with you more than half of 2025, or, for a person other than a qualifying child born or who died in 2025, more than half of the part of 2025 they were alive
- **Encoded (Bool):** (helper "Lived with you for more than half of 2025" = true or helper "Qualifying child (Step 1)" = false and helper "Born or died in 2025?" = true and helper "Lived with you more than half the part of 2025 they were alive, or since the adoption or placement?" = true)
- Expr: `{"any":[{"eq":["dependent.lived_half",{"const":true}],"op":"test"},{"all":[{"eq":["dependent.qualifying_child",{"const":false}],"op":"test"},{"eq":["dependent.born_died",{"const":true}],"op":"test"},{"eq":["dependent.part_year_home",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [p503] p. 3, Birth or death of otherwise qualifying person, "a person who was born or died in 2025 is treated as having lived with you for more than half of 2025 if your home was the person's home more than half the time they were alive in 2025" (For use in preparing 2025 returns; sha256 3a00d0c1)

## (helper) — `dependent.one`

- **Authored helper label:** One person listed
- **Encoded (Count):** Enter 1 (dependent.one).
- Expr: `{"op":"param","ref":"dependent.one"}`
- Cite: [f1040s8812] Schedule 8812 (2025), lines 4 and 6 (2025; created 2025-07-30; sha256 6936462d)

## (helper) — `dependent.zero`

- **Authored helper label:** No amount for this person
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [f1040s8812] Schedule 8812 (2025), lines 5 and 7 (2025; created 2025-07-30; sha256 6936462d)

## (helper) — `dependent.qc_relationship`

- **Authored helper label:** A child, sibling, or a descendant of either
- **Encoded (Bool):** (helper "Relationship to you" = 'child' or helper "Relationship to you" = 'sibling' or helper "Relationship to you" = 'sibling_descendant')
- Expr: `{"any":[{"eq":["dependent.relationship",{"const":"child"}],"op":"test"},{"eq":["dependent.relationship",{"const":"sibling"}],"op":"test"},{"eq":["dependent.relationship",{"const":"sibling_descendant"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 17, Step 1, "Son, daughter, stepchild, foster child, brother, sister, stepbrother, stepsister, half brother, half sister, or a descendant of any of them" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.younger`

- **Authored helper label:** Younger than you (or your spouse if filing jointly)?
- **Encoded (Bool):** Input — Was this person younger than you (or, if you file jointly, younger than you or your spouse; the person need not be younger than both of you)?
- Expr: `{"op":"input","source":"Was this person younger than you (or, if you file jointly, younger than you or your spouse; the person need not be younger than both of you)?"}`
- Cite: [i1040gi] p. 17, Step 1, "and younger than you (or your spouse if filing jointly)"; p501 p. 13, "if you are married filing jointly, the child must be younger than you or your spouse but doesn't have to be younger than both of you" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.us_half`

- **Authored helper label:** Lived with you in the United States for more than half of 2025?
- **Encoded (Bool):** Input — Did this person live with you in the United States (the 50 states and the District of Columbia) for more than half of 2025?

  If you were on extended active military duty outside the United States, your main home is considered to be in the United States during that duty.

  Temporary absences for school, vacation, business, medical care, military service or juvenile detention count as time lived with you; time a child presumed kidnapped was missing because of the kidnapping does not.

  A child born or who died in 2025 counts if your home was the child's home for more than half the time the child was alive.

  A child you adopted, who was lawfully placed with you for legal adoption, or who was placed with you as an eligible foster child in 2025 counts if your main home was the child's main home for more than half the time since the adoption or placement.
- Expr: `{"op":"input","source":"Did this person live with you in the United States (the 50 states and the District of Columbia) for more than half of 2025?\n\nIf you were on extended active military duty outside the United States, your main home is considered to be in the United States during that duty.\n\nTemporary absences for school, vacation, business, medical care, military service or juvenile detention count as time lived with you; time a child presumed kidnapped was missing because of the kidnapping does not.\n\nA child born or who died in 2025 counts if your home was the child's home for more than half the time the child was alive.\n\nA child you adopted, who was lawfully placed with you for legal adoption, or who was placed with you as an eligible foster child in 2025 counts if your main home was the child's main home for more than half the time since the adoption or placement."}`
- Cite: [i1040gi] p. 41, Step 3, "Who lived with you in the United States for more than half of 2025"; p. 43, Exception to time lived with you; p. 44, Members of the military; p. 45, United States (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.eic_ssn`

- **Authored helper label:** SSN valid for the EIC, issued on or before the due date of your return?
- **Encoded (Bool):** Input — Did this person have a social security number issued on or before the due date of your 2025 return (including extensions) that is valid for the EIC? Any number issued by the Social Security Administration is valid unless the card says "Not Valid for Employment" and the number was issued solely to apply for or receive a federally funded benefit; a card that says "Valid for Work Only With DHS Authorization" is valid only while the authorization is valid.
- Interpretation: amb.2025.eic_valid_ssn
- Expr: `{"op":"input","source":"Did this person have a social security number issued on or before the due date of your 2025 return (including extensions) that is valid for the EIC? Any number issued by the Social Security Administration is valid unless the card says \"Not Valid for Employment\" and the number was issued solely to apply for or receive a federally funded benefit; a card that says \"Valid for Work Only With DHS Authorization\" is valid only while the authorization is valid."}`
- Cite: [i1040gi] pp. 44–45, Social security number (SSN), EIC (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.under_19`

- **Authored helper label:** Under age 19 at the end of 2025
- **Encoded (Bool):** helper "Age at the end of 2025" < 19 (qc.age_limit)
- Expr: `{"lt":["dependent.age",{"param":"qc.age_limit"}],"op":"test"}`
- Cite: [i1040gi] p. 17, Step 1, the age conditions (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.under_24`

- **Authored helper label:** Under age 24 at the end of 2025
- **Encoded (Bool):** helper "Age at the end of 2025" < 24 (qc.student_age_limit)
- Expr: `{"lt":["dependent.age",{"param":"qc.student_age_limit"}],"op":"test"}`
- Cite: [i1040gi] p. 17, Step 1, the age conditions (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qc_age_younger`

- **Authored helper label:** Younger than you (or your spouse if filing jointly), or permanently and totally disabled
- **Encoded (Bool):** Choose — [helper "Younger than you (or your spouse if filing jointly)?" = true → helper "Younger than you (or your spouse if filing jointly)?"] [helper "Younger than you (or your spouse if filing jointly)?" = false → helper "Permanently and totally disabled?"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.younger",{"const":true}],"op":"test"},"then":"dependent.younger"},{"guard":{"eq":["dependent.younger",{"const":false}],"op":"test"},"then":"dependent.disabled"}],"op":"choose"}`
- Cite: [i1040gi] p. 17, Step 1, the age conditions (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qc_age_19`

- **Authored helper label:** Age test for a person aged 19 or older: under 24, a full-time student and younger than you, or permanently and totally disabled
- **Encoded (Bool):** Choose — [helper "Under age 24 at the end of 2025" = true → helper "Age test for a person aged 19 to 23: a full-time student and younger than you, or permanently and totally disabled"] [helper "Under age 24 at the end of 2025" = false → helper "Permanently and totally disabled?"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.under_24",{"const":true}],"op":"test"},"then":"dependent.qc_age_student"},{"guard":{"eq":["dependent.under_24",{"const":false}],"op":"test"},"then":"dependent.disabled"}],"op":"choose"}`
- Cite: [i1040gi] p. 17, Step 1, the age conditions (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qc_age_student`

- **Authored helper label:** Age test for a person aged 19 to 23: a full-time student and younger than you, or permanently and totally disabled
- **Encoded (Bool):** Choose — [helper "Full-time student in 2025?" = true → helper "Younger than you (or your spouse if filing jointly), or permanently and totally disabled"] [helper "Full-time student in 2025?" = false → helper "Permanently and totally disabled?"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.student",{"const":true}],"op":"test"},"then":"dependent.qc_age_younger"},{"guard":{"eq":["dependent.student",{"const":false}],"op":"test"},"then":"dependent.disabled"}],"op":"choose"}`
- Cite: [i1040gi] p. 17, Step 1, the age conditions (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qc_age`

- **Authored helper label:** Under 19 and younger than you, under 24 a full-time student and younger than you, or permanently and totally disabled
- **Encoded (Bool):** Choose — [helper "Under age 19 at the end of 2025" = true → helper "Younger than you (or your spouse if filing jointly), or permanently and totally disabled"] [helper "Under age 19 at the end of 2025" = false → helper "Age test for a person aged 19 or older: under 24, a full-time student and younger than you, or permanently and totally disabled"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.under_19",{"const":true}],"op":"test"},"then":"dependent.qc_age_younger"},{"guard":{"eq":["dependent.under_19",{"const":false}],"op":"test"},"then":"dependent.qc_age_19"}],"op":"choose"}`
- Cite: [i1040gi] p. 17, Step 1, the age conditions (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.lived_half`

- **Authored helper label:** Lived with you for more than half of 2025
- **Encoded (Bool):** helper "Months lived with you in 2025, counting temporary absences" > 6 (a count)
- **Refusal:** when dependent.kidnap_residency is true, cannot complete Kidnapped child (Pub. 501; Pub. 596 for the EIC). A child presumed kidnapped by someone who isn't a family member, who lived with you for fewer than 7 months of 2025 without counting the time missing, may count as living with you under rules this tool does not apply. Cite: [i1040gi] p. 21, Kidnapped child, "For details, see Pub. 501 (Pub. 596 for the EIC)" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"gt":["dependent.months",{"const":6,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 17, Step 1, "Who lived with you for more than half of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `dependent.kidnap_residency`

- **Authored helper label:** A child presumed kidnapped who lived with you for fewer than 7 months of 2025, not counting the time missing
- **Encoded (Bool):** helper "A child kidnapped by someone who isn't a member of your family or the child's family, presumed kidnapped by law enforcement, and missing because of it at some time in 2025?" = true and helper "Months lived with you in 2025, counting temporary absences" < 7 (a count)
- Expr: `{"all":[{"eq":["dependent.kidnapped",{"const":true}],"op":"test"},{"lt":["dependent.months",{"const":7,"type":"Count"}],"op":"test"}],"op":"test"}`
- Cite: [p501] p. 13, Kidnapped child, "You can treat your child as meeting the residency test even if the child has been kidnapped, but the following statements must be true." (a child who lived with you for more than half of 2025 meets the residency test without this treatment) (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (helper) — `dependent.no`

- **Authored helper label:** Year parameter household.no (false)
- **Encoded (Bool):** Enter false (household.no).
- Expr: `{"op":"param","ref":"household.no"}`
- Cite: [i1040gi] p. 17, Step 1, "Do you have a child who meets the conditions to be your qualifying child?" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qc_tests`

- **Authored helper label:** Qualifying child tests (Step 1): relationship, age, support, joint return and residency, each asked only when the ones before it pass
- **Encoded (Bool):** Choose — [helper "A child, sibling, or a descendant of either" = true → helper "Qualifying child tests (Step 1) from the age test on: age, support, joint return and residency"] [helper "A child, sibling, or a descendant of either" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.qc_relationship",{"const":true}],"op":"test"},"then":"dependent.qc_from_age"},{"guard":{"eq":["dependent.qc_relationship",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 17, Step 1, "Do you have a child who meets the conditions to be your qualifying child?" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qc_from_age`

- **Authored helper label:** Qualifying child tests (Step 1) from the age test on: age, support, joint return and residency
- **Encoded (Bool):** Choose — [helper "Under 19 and younger than you, under 24 a full-time student and younger than you, or permanently and totally disabled" = true → helper "Qualifying child tests (Step 1) from the support test on: support, joint return and residency"] [helper "Under 19 and younger than you, under 24 a full-time student and younger than you, or permanently and totally disabled" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.qc_age",{"const":true}],"op":"test"},"then":"dependent.qc_from_support"},{"guard":{"eq":["dependent.qc_age",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 17, Step 1, "Do you have a child who meets the conditions to be your qualifying child?" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qc_from_support`

- **Authored helper label:** Qualifying child tests (Step 1) from the support test on: support, joint return and residency
- **Encoded (Bool):** Choose — [helper "Provided over half of their own support?" = true → helper "Year parameter household.no (false)"] [helper "Provided over half of their own support?" = false → helper "Qualifying child tests (Step 1) from the joint return test on: joint return and residency"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.self_support",{"const":true}],"op":"test"},"then":"dependent.no"},{"guard":{"eq":["dependent.self_support",{"const":false}],"op":"test"},"then":"dependent.qc_from_joint"}],"op":"choose"}`
- Cite: [i1040gi] p. 17, Step 1, "Do you have a child who meets the conditions to be your qualifying child?" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qc_from_joint`

- **Authored helper label:** Qualifying child tests (Step 1) from the joint return test on: joint return and residency
- **Encoded (Bool):** Choose — [helper "Included on a 2025 joint return filed other than only to claim a refund?" = true → helper "Year parameter household.no (false)"] [helper "Included on a 2025 joint return filed other than only to claim a refund?" = false → helper "Lived with you for more than half of 2025"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.joint_return",{"const":true}],"op":"test"},"then":"dependent.no"},{"guard":{"eq":["dependent.joint_return",{"const":false}],"op":"test"},"then":"dependent.lived_half"}],"op":"choose"}`
- Cite: [i1040gi] p. 17, Step 1, "Do you have a child who meets the conditions to be your qualifying child?" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qualifying_child`

- **Authored helper label:** Qualifying child (Step 1)
- **Encoded (Bool):** helper "Qualifying child tests (Step 1): relationship, age, support, joint return and residency, each asked only when the ones before it pass" = true
- **Refusal:** when dependent.qc_tiebreak is true, cannot complete Qualifying child of more than one person (tie-breaker rules). This person may be the qualifying child of another person. The tie-breaker rules are outside this tool. Cite: [i1040gi] p. 21, Qualifying child of more than one person (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when dependent.divorced_rule is true, cannot complete Children of divorced or separated parents. The rule for children of divorced or separated parents is outside this tool. Cite: [i1040gi] p. 20, Children of divorced or separated parents (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when dependent.married is true, cannot complete Married person rules. A married dependent is outside this tool; see Married person in the instructions. Cite: [i1040gi] p. 21, Married person (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"eq":["dependent.qc_tests",{"const":true}],"op":"test"}`
- Cite: [i1040gi] p. 17, Step 1, "Do you have a child who meets the conditions to be your qualifying child?" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.resident`

- **Authored helper label:** U.S. citizen, national or resident alien, or a resident of Canada or Mexico
- **Encoded (Bool):** Choose — [helper "U.S. citizen, U.S. national or U.S. resident alien?" = true → helper "U.S. citizen, U.S. national or U.S. resident alien?"] [helper "U.S. citizen, U.S. national or U.S. resident alien?" = false → helper "Resident of Canada or Mexico (if not a U.S. citizen, national or resident alien)?"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.citizen",{"const":true}],"op":"test"},"then":"dependent.citizen"},{"guard":{"eq":["dependent.citizen",{"const":false}],"op":"test"},"then":"dependent.canada_mexico"}],"op":"choose"}`
- Cite: [i1040gi] p. 18, Step 2, question 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qc_dependent_resident`

- **Authored helper label:** Qualifying child who is a U.S. citizen, national or resident alien or a resident of Canada or Mexico, and you are not a dependent
- **Encoded (Bool):** Choose — [helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = true → helper "You (and your spouse if filing jointly) cannot be claimed as a dependent"] [helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.resident",{"const":true}],"op":"test"},"then":"dependent.filer_not_dependent"},{"guard":{"eq":["dependent.resident",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 18, Step 2, questions 1 and 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.filer_not_dependent`

- **Authored helper label:** You (and your spouse if filing jointly) cannot be claimed as a dependent
- **Encoded (Bool):** sa helper "Can someone claim you or your spouse as a dependent for 2025, or are you a dual-status alien? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)" = false
- Expr: `{"eq":["sa.dependent",{"const":false}],"op":"test"}`
- Cite: [i1040gi] p. 18, Step 2, questions 1 and 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qc_dependent`

- **Authored helper label:** Qualifying child who is your dependent (Step 2)
- **Encoded (Bool):** Choose — [helper "Qualifying child (Step 1)" = true → helper "Qualifying child who is a U.S. citizen, national or resident alien or a resident of Canada or Mexico, and you are not a dependent"] [helper "Qualifying child (Step 1)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.qualifying_child",{"const":true}],"op":"test"},"then":"dependent.qc_dependent_resident"},{"guard":{"eq":["dependent.qualifying_child",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 18, Step 2, questions 1 and 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qr_listed_relative`

- **Authored helper label:** A child, sibling, parent, other ancestor or in-law listed in Step 4
- **Encoded (Bool):** (helper "Relationship to you" = 'child' or helper "Relationship to you" = 'sibling' or helper "Relationship to you" = 'parent' or helper "Relationship to you" = 'parent_relative' or helper "Relationship to you" = 'in_law')
- Expr: `{"any":[{"eq":["dependent.relationship",{"const":"child"}],"op":"test"},{"eq":["dependent.relationship",{"const":"sibling"}],"op":"test"},{"eq":["dependent.relationship",{"const":"parent"}],"op":"test"},{"eq":["dependent.relationship",{"const":"parent_relative"}],"op":"test"},{"eq":["dependent.relationship",{"const":"in_law"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 19, Step 4, "A qualifying relative is your..." through "Any other person (other than your spouse) who lived with you all year as a member of your household"; p501 p. 19, Joint return, "If you file a joint return, the person can be related to either you or your spouse." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qr_household_member`

- **Authored helper label:** A household member: lived with you all year, or a relative of your spouse on a joint return
- **Encoded (Bool):** (f1040 line Filing Status = 'mfj' and helper "On a joint return, related to your spouse in one of the Step 4 ways" = true or helper "Lived with you all of 2025 as a member of your household (qualifying relative test)" = true)
- Expr: `{"any":[{"all":[{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},{"eq":["dependent.spouse_relative",{"const":true}],"op":"test"}],"op":"test"},{"eq":["dependent.qr_all_year",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 19, Step 4, "A qualifying relative is your..." through "Any other person (other than your spouse) who lived with you all year as a member of your household"; p501 p. 19, Joint return, "If you file a joint return, the person can be related to either you or your spouse." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qr_other_relation`

- **Authored helper label:** A descendant of a sibling or another person: lived with you all year and the relationship did not violate local law, or a relative of your spouse on a joint return
- **Encoded (Bool):** (f1040 line Filing Status = 'mfj' and helper "On a joint return, related to your spouse in one of the Step 4 ways" = true or helper "Lived with you all of 2025 as a member of your household (qualifying relative test)" = true and helper "Your relationship with this person did not violate local law" = true)
- Expr: `{"any":[{"all":[{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},{"eq":["dependent.spouse_relative",{"const":true}],"op":"test"}],"op":"test"},{"all":[{"eq":["dependent.qr_all_year",{"const":true}],"op":"test"},{"eq":["dependent.lawful",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 19, Step 4, "A qualifying relative is your..." through "Any other person (other than your spouse) who lived with you all year as a member of your household"; p501 p. 19, Joint return, "If you file a joint return, the person can be related to either you or your spouse." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qr_relationship`

- **Authored helper label:** A relative listed in Step 4, or any other person who lived with you all year
- **Encoded (Bool):** Choose — [helper "Relationship to you" = 'child' → helper "A child, sibling, parent, other ancestor or in-law listed in Step 4"] [helper "Relationship to you" = 'sibling' → helper "A child, sibling, parent, other ancestor or in-law listed in Step 4"] [helper "Relationship to you" = 'parent' → helper "A child, sibling, parent, other ancestor or in-law listed in Step 4"] [helper "Relationship to you" = 'parent_relative' → helper "A child, sibling, parent, other ancestor or in-law listed in Step 4"] [helper "Relationship to you" = 'in_law' → helper "A child, sibling, parent, other ancestor or in-law listed in Step 4"] [helper "Relationship to you" = 'household_member' → helper "A household member: lived with you all year, or a relative of your spouse on a joint return"] [helper "Relationship to you" = 'sibling_descendant' → helper "A descendant of a sibling or another person: lived with you all year and the relationship did not violate local law, or a relative of your spouse on a joint return"] [helper "Relationship to you" = 'other' → helper "A descendant of a sibling or another person: lived with you all year and the relationship did not violate local law, or a relative of your spouse on a joint return"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.relationship",{"const":"child"}],"op":"test"},"then":"dependent.qr_listed_relative"},{"guard":{"eq":["dependent.relationship",{"const":"sibling"}],"op":"test"},"then":"dependent.qr_listed_relative"},{"guard":{"eq":["dependent.relationship",{"const":"parent"}],"op":"test"},"then":"dependent.qr_listed_relative"},{"guard":{"eq":["dependent.relationship",{"const":"parent_relative"}],"op":"test"},"then":"dependent.qr_listed_relative"},{"guard":{"eq":["dependent.relationship",{"const":"in_law"}],"op":"test"},"then":"dependent.qr_listed_relative"},{"guard":{"eq":["dependent.relationship",{"const":"household_member"}],"op":"test"},"then":"dependent.qr_household_member"},{"guard":{"eq":["dependent.relationship",{"const":"sibling_descendant"}],"op":"test"},"then":"dependent.qr_other_relation"},{"guard":{"eq":["dependent.relationship",{"const":"other"}],"op":"test"},"then":"dependent.qr_other_relation"}],"op":"choose"}`
- Cite: [i1040gi] p. 19, Step 4, "A qualifying relative is your..." through "Any other person (other than your spouse) who lived with you all year as a member of your household"; p501 p. 19, Joint return, "If you file a joint return, the person can be related to either you or your spouse." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.spouse_relative`

- **Authored helper label:** On a joint return, related to your spouse in one of the Step 4 ways
- **Encoded (Bool):** Input — Is this person related to your spouse in one of these ways?

  - your spouse's child, stepchild or foster child, or a descendant of any of them
  - your spouse's brother, sister, half brother, half sister, stepbrother or stepsister
  - your spouse's father, mother, grandparent or other direct ancestor (not a foster parent)
  - your spouse's stepfather or stepmother
  - a son or daughter of your spouse's brother, sister, half brother or half sister
  - a brother or sister of your spouse's father or mother
  - your spouse's son-in-law, daughter-in-law, father-in-law, mother-in-law, brother-in-law or sister-in-law

  A relationship established by marriage is not ended by death or divorce.

  (Asked only on a joint return, for a person who is not one of these relatives of yours.)
- Expr: `{"op":"input","source":"Is this person related to your spouse in one of these ways?\n\n- your spouse's child, stepchild or foster child, or a descendant of any of them\n- your spouse's brother, sister, half brother, half sister, stepbrother or stepsister\n- your spouse's father, mother, grandparent or other direct ancestor (not a foster parent)\n- your spouse's stepfather or stepmother\n- a son or daughter of your spouse's brother, sister, half brother or half sister\n- a brother or sister of your spouse's father or mother\n- your spouse's son-in-law, daughter-in-law, father-in-law, mother-in-law, brother-in-law or sister-in-law\n\nA relationship established by marriage is not ended by death or divorce.\n\n(Asked only on a joint return, for a person who is not one of these relatives of yours.)"}`
- Cite: [p501] p. 19, Joint return, "If you file a joint return, the person can be related to either you or your spouse. Also, the person doesn’t need to be related to the spouse who provides support."; p. 19, Relatives who don't have to live with you, "Your child, stepchild, or foster child, or a descendant of any of them" through "mother-in-law, brother-in-law, or sister-in-law." and "Any of these relationships that were established by marriage aren’t ended by death or divorce." (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (helper) — `dependent.qr_all_year`

- **Authored helper label:** Lived with you all of 2025 as a member of your household (qualifying relative test)
- **Encoded (Bool):** Input — Did this person live with you all of 2025 as a member of your household?

  Count as time lived with you:
  - a temporary absence by you or the person for special circumstances, such as illness, education, business, vacation, military service or detention in a juvenile facility
  - a stay in a nursing home for an indefinite period to receive constant medical care

  Answer Yes also for:
  - a person who died in 2025 and lived with you as a member of your household until death
  - a child born in 2025 who lived with you as a member of your household for the rest of the year, apart from any required hospital stay following birth
  - a person you adopted, who was lawfully placed with you for legal adoption, or who was placed with you as an eligible foster child in 2025, if your main home was the person's main home for the entire time since the adoption or placement
- Expr: `{"op":"input","source":"Did this person live with you all of 2025 as a member of your household?\n\nCount as time lived with you:\n- a temporary absence by you or the person for special circumstances, such as illness, education, business, vacation, military service or detention in a juvenile facility\n- a stay in a nursing home for an indefinite period to receive constant medical care\n\nAnswer Yes also for:\n- a person who died in 2025 and lived with you as a member of your household until death\n- a child born in 2025 who lived with you as a member of your household for the rest of the year, apart from any required hospital stay following birth\n- a person you adopted, who was lawfully placed with you for legal adoption, or who was placed with you as an eligible foster child in 2025, if your main home was the person's main home for the entire time since the adoption or placement"}`
- Cite: [p501] p. 19, Temporary absences, "A person is considered to live with you as a member of your household during periods of time when one of you, or both, is temporarily absent due to special circumstances" and "If the person is placed in a nursing home for an indefinite period of time to receive constant medical care, the absence may be considered temporary."; p. 19, Death or birth, "A person who died during the year, but lived with you as a member of your household until death, will meet this test." through "your main home was the person’s main home for the entire time since the person was adopted or placed with you in 2025."; i1040gi p. 19, Step 4, "Any other person (other than your spouse) who lived with you all year as a member of your household" (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (helper) — `dependent.lawful`

- **Authored helper label:** Your relationship with this person did not violate local law
- **Encoded (Bool):** Input — Did your relationship with this person not violate local law? (Asked for a person who is a Step 4 relative only as a member of your household all year, such as a sibling's grandchild or a step sibling's child, or who is no relative.)
- Expr: `{"op":"input","source":"Did your relationship with this person not violate local law? (Asked for a person who is a Step 4 relative only as a member of your household all year, such as a sibling's grandchild or a step sibling's child, or who is no relative.)"}`
- Cite: [i1040gi] p. 19, Step 4, "Any other person (other than your spouse) who lived with you all year as a member of your household if your relationship didn’t violate local law." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qr_income`

- **Authored helper label:** Gross income under $5,200
- **Encoded (Bool):** helper "Gross income for 2025" < $5,200 (qr.gross_income_limit)
- Expr: `{"lt":["dependent.gross_income",{"param":"qr.gross_income_limit"}],"op":"test"}`
- Cite: [i1040gi] p. 19, Step 4, "Who had gross income of less than $5,200 in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `dependent.income_exception`

- **Authored helper label:** Permanently and totally disabled with gross income at or over the limit
- **Encoded (Bool):** helper "Permanently and totally disabled?" = true and helper "Gross income under $5,200" = false
- Expr: `{"all":[{"eq":["dependent.disabled",{"const":true}],"op":"test"},{"eq":["dependent.qr_income",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 19, Step 4, "If the person was permanently and totally disabled, see Exception to gross income test" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `dependent.qr_kidnapped`

- **Authored helper label:** A child aged 18 or under at the end of 2025 presumed kidnapped by someone who isn't a family member
- **Encoded (Bool):** helper "Age at the end of 2025" < 19 (a count) and helper "A child kidnapped by someone who isn't a member of your family or the child's family, presumed kidnapped by law enforcement, and missing because of it at some time in 2025?" = true
- Expr: `{"all":[{"lt":["dependent.age",{"const":19,"type":"Count"}],"op":"test"},{"eq":["dependent.kidnapped",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [p501] p. 18, Kidnapped child, "This treatment applies for all years until the earlier of: 1. The year there is a determination that the child is dead, or 2. The year the child would have reached age 18." (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (helper) — `dependent.qualifying_relative`

- **Authored helper label:** Qualifying relative (Step 4)
- **Encoded (Bool):** helper "A relative listed in Step 4, or any other person who lived with you all year" = true and helper "Qualifying child (Step 1)" = false and helper "Gross income under $5,200" = true and helper "You provided over half of this person's support?" = true
- **Refusal:** when dependent.multiple_support is true, cannot complete Multiple support agreements. A person claimed under a multiple support agreement is outside this tool. Cite: [i1040gi] p. 20, Multiple support agreements (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when dependent.income_exception is true, cannot complete Exception to gross income test. The sheltered-workshop exception to the gross income test for a disabled person is outside this tool. Cite: [i1040gi] pp. 19–20, Exception to gross income test (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when dependent.married is true, cannot complete Married person rules. A married dependent is outside this tool; see Married person in the instructions. Cite: [i1040gi] p. 21, Married person (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when dependent.qr_kidnapped is true, cannot complete Kidnapped child (Pub. 501). A child presumed kidnapped by someone who isn't a family member may be your qualifying relative under part-year rules this tool does not apply. Cite: [p501] p. 18, Kidnapped child, "You can treat a child as your qualifying relative even if the child has been kidnapped, but the following statements must be true." (2025 returns; PDF created 2026-02-04; sha256 288b62a4)
- Expr: `{"all":[{"eq":["dependent.qr_relationship",{"const":true}],"op":"test"},{"eq":["dependent.qualifying_child",{"const":false}],"op":"test"},{"eq":["dependent.qr_income",{"const":true}],"op":"test"},{"eq":["dependent.supported",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 19, Step 4, "Does any person meet the conditions to be your qualifying relative?" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qr_dependent_resident`

- **Authored helper label:** Qualifying relative who is a U.S. citizen, national or resident alien or a resident of Canada or Mexico, and you are not a dependent
- **Encoded (Bool):** Choose — [helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = true → helper "You (and your spouse if filing jointly) cannot be claimed as a dependent"] [helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.resident",{"const":true}],"op":"test"},"then":"dependent.filer_not_dependent"},{"guard":{"eq":["dependent.resident",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 19, Step 4, questions 2 and 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qr_dependent`

- **Authored helper label:** Qualifying relative who is your dependent (Step 4, questions 2 and 5)
- **Encoded (Bool):** Choose — [helper "Qualifying relative (Step 4)" = true → helper "Qualifying relative who is a U.S. citizen, national or resident alien or a resident of Canada or Mexico, and you are not a dependent"] [helper "Qualifying relative (Step 4)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.qualifying_relative",{"const":true}],"op":"test"},"then":"dependent.qr_dependent_resident"},{"guard":{"eq":["dependent.qualifying_relative",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 19, Step 4, questions 2 and 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `dependent.claimed_no_tin`

- **Authored helper label:** A person who meets the tests to be your dependent but has no SSN, ITIN or ATIN
- **Encoded (Bool):** helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = false and (helper "Qualifying child who is your dependent (Step 2)" = true or helper "Qualifying relative who is your dependent (Step 4, questions 2 and 5)" = true)
- Expr: `{"all":[{"eq":["dependent.tin",{"const":false}],"op":"test"},{"any":[{"eq":["dependent.qc_dependent",{"const":true}],"op":"test"},{"eq":["dependent.qr_dependent",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 22, Social security number, "You must enter each dependent’s social security number (SSN)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.claimed`

- **Authored helper label:** Your dependent
- **Encoded (Bool):** (helper "Qualifying child who is your dependent (Step 2)" = true or helper "Qualifying relative who is your dependent (Step 4, questions 2 and 5)" = true)
- **Refusal:** when dependent.claimed_no_tin is true, cannot complete Dependent without an SSN, ITIN or ATIN (Form 1040, Dependents, row (3)). Each dependent must be listed with an SSN (or ITIN or ATIN) issued on or before the due date of your return. A dependent child who was born and died in 2025 without an SSN, entered as "Died" on row (3) with a copy of the birth certificate, death certificate or hospital records, is outside this tool. Cite: [i1040gi] p. 22, Social security number, "You must enter each dependent’s social security number (SSN)" and "If your dependent child was born and died in 2025 and you do not have an SSN for the child, enter “Died” on row (3) of the Dependents section and include a copy of the child’s birth certificate, death certificate, or hospital records"; p. 14, Head of Household, "The dependents you claim are those you list by name and SSN ... in the Dependents section on Form 1040 or 1040-SR" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"any":[{"eq":["dependent.qc_dependent",{"const":true}],"op":"test"},{"eq":["dependent.qr_dependent",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] pp. 17–19, Who Qualifies as Your Dependent (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.under_ctc_age`

- **Authored helper label:** Under age 17 at the end of 2025
- **Encoded (Bool):** helper "Age at the end of 2025" < 17 (ctc.age_limit)
- Expr: `{"lt":["dependent.age",{"param":"ctc.age_limit"}],"op":"test"}`
- Cite: [i1040gi] p. 18, Step 3, question 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.ctc_from_tin`

- **Authored helper label:** Child tax credit tests (Step 3) from the SSN, ITIN or ATIN test on
- **Encoded (Bool):** Choose — [helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = true → helper "Child tax credit tests (Step 3) from the citizenship test on"] [helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.tin",{"const":true}],"op":"test"},"then":"dependent.ctc_from_citizen"},{"guard":{"eq":["dependent.tin",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 18, Step 3, questions 1–4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.ctc_from_citizen`

- **Authored helper label:** Child tax credit tests (Step 3) from the citizenship test on
- **Encoded (Bool):** Choose — [helper "U.S. citizen, U.S. national or U.S. resident alien?" = true → helper "Child tax credit tests (Step 3) from the age test on"] [helper "U.S. citizen, U.S. national or U.S. resident alien?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.citizen",{"const":true}],"op":"test"},"then":"dependent.ctc_from_age"},{"guard":{"eq":["dependent.citizen",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 18, Step 3, questions 1–4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.ctc_from_age`

- **Authored helper label:** Child tax credit tests (Step 3) from the age test on
- **Encoded (Bool):** Choose — [helper "Under age 17 at the end of 2025" = true → helper "Child tax credit tests (Step 3) from the work SSN test on"] [helper "Under age 17 at the end of 2025" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.under_ctc_age",{"const":true}],"op":"test"},"then":"dependent.ctc_from_work_ssn"},{"guard":{"eq":["dependent.under_ctc_age",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 18, Step 3, questions 1–4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.ctc_from_work_ssn`

- **Authored helper label:** Child tax credit tests (Step 3) from the work SSN test on
- **Encoded (Bool):** Choose — [helper "SSN valid for employment issued before the due date of your return?" = true → household helper "Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid for employment, and each other person on the return has an SSN or ITIN"] [helper "SSN valid for employment issued before the due date of your return?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.work_ssn",{"const":true}],"op":"test"},"then":"household.ctc_ssn"},{"guard":{"eq":["dependent.work_ssn",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 18, Step 3, questions 1–4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.ctc_child`

- **Authored helper label:** Qualifying child for the child tax credit (Step 3)
- **Encoded (Bool):** Choose — [helper "Qualifying child who is your dependent (Step 2)" = true → helper "Child tax credit tests (Step 3) from the SSN, ITIN or ATIN test on"] [helper "Qualifying child who is your dependent (Step 2)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.qc_dependent",{"const":true}],"op":"test"},"then":"dependent.ctc_from_tin"},{"guard":{"eq":["dependent.qc_dependent",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 18, Step 3, questions 1–4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.odc_person`

- **Authored helper label:** Dependent for the credit for other dependents (Steps 3 and 5)
- **Encoded (Bool):** helper "Your dependent" = true and helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = true and helper "U.S. citizen, U.S. national or U.S. resident alien?" = true and helper "Qualifying child for the child tax credit (Step 3)" = false and household helper "You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN" = true
- Expr: `{"all":[{"eq":["dependent.claimed",{"const":true}],"op":"test"},{"eq":["dependent.tin",{"const":true}],"op":"test"},{"eq":["dependent.citizen",{"const":true}],"op":"test"},{"eq":["dependent.ctc_child",{"const":false}],"op":"test"},{"eq":["household.all_tin",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 18, Step 3, question 3, and p. 19, Step 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.ctc_per_child`

- **Authored helper label:** Year parameter ctc.per_child
- **Encoded (NonNegDollars):** Enter $2,200 (ctc.per_child).
- Expr: `{"op":"param","ref":"ctc.per_child"}`
- Cite: [f1040s8812] Schedule 8812 (2025), line 5 (2025; created 2025-07-30; sha256 6936462d)

## (helper) — `dependent.ctc_amount`

- **Authored helper label:** Child tax credit amount for this person before limits ($2,200 for a qualifying child, else 0)
- **Encoded (NonNegDollars):** Choose — [helper "Qualifying child for the child tax credit (Step 3)" = true → helper "Year parameter ctc.per_child"] [helper "Qualifying child for the child tax credit (Step 3)" = false → helper "No amount for this person"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.ctc_child",{"const":true}],"op":"test"},"then":"dependent.ctc_per_child"},{"guard":{"eq":["dependent.ctc_child",{"const":false}],"op":"test"},"then":"dependent.zero"}],"op":"choose"}`
- Cite: [f1040s8812] Schedule 8812 (2025), line 5, "Multiply line 4 by $2,200" (2025; created 2025-07-30; sha256 6936462d)

## (helper) — `dependent.odc_per_dependent`

- **Authored helper label:** Year parameter odc.per_dependent
- **Encoded (NonNegDollars):** Enter $500 (odc.per_dependent).
- Expr: `{"op":"param","ref":"odc.per_dependent"}`
- Cite: [f1040s8812] Schedule 8812 (2025), line 7 (2025; created 2025-07-30; sha256 6936462d)

## (helper) — `dependent.odc_amount`

- **Authored helper label:** Credit for other dependents amount for this person before limits ($500 for an other dependent, else 0)
- **Encoded (NonNegDollars):** Choose — [helper "Dependent for the credit for other dependents (Steps 3 and 5)" = true → helper "Year parameter odc.per_dependent"] [helper "Dependent for the credit for other dependents (Steps 3 and 5)" = false → helper "No amount for this person"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.odc_person",{"const":true}],"op":"test"},"then":"dependent.odc_per_dependent"},{"guard":{"eq":["dependent.odc_person",{"const":false}],"op":"test"},"then":"dependent.zero"}],"op":"choose"}`
- Cite: [f1040s8812] Schedule 8812 (2025), line 7, "Multiply line 6 by $500" (2025; created 2025-07-30; sha256 6936462d)

## (helper) — `dependent.actc_per_child`

- **Authored helper label:** Year parameter actc.per_child
- **Encoded (NonNegDollars):** Enter $1,700 (actc.per_child).
- Expr: `{"op":"param","ref":"actc.per_child"}`
- Cite: [f1040s8812] Schedule 8812 (2025), line 16b (2025; created 2025-07-30; sha256 6936462d)

## (helper) — `dependent.actc_amount`

- **Authored helper label:** Additional child tax credit ceiling for this person ($1,700 for a qualifying child, else 0)
- **Encoded (NonNegDollars):** Choose — [helper "Qualifying child for the child tax credit (Step 3)" = true → helper "Year parameter actc.per_child"] [helper "Qualifying child for the child tax credit (Step 3)" = false → helper "No amount for this person"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.ctc_child",{"const":true}],"op":"test"},"then":"dependent.actc_per_child"},{"guard":{"eq":["dependent.ctc_child",{"const":false}],"op":"test"},"then":"dependent.zero"}],"op":"choose"}`
- Cite: [f1040s8812] p. 2, Part II-A Additional Child Tax Credit for All Filers, line 16b, "b Number of qualifying children under age 17 with the required social security number", "x $1,700. Enter the result" (2025; created 2025-07-30; sha256 6936462d)

## (helper) — `dependent.absence_no_return`

- **Authored helper label:** Counted an absence the person was not expected to return from, or during which you did not keep up the home
- **Encoded (Bool):** Input — In counting the time this person lived with you in 2025, did you count as time lived with you an absence by you or the person from which it was not reasonable to assume the absent person would return to the home, or during which you did not continue to keep up the home? (Asked when this person may qualify you for head of household.)
- Expr: `{"op":"input","source":"In counting the time this person lived with you in 2025, did you count as time lived with you an absence by you or the person from which it was not reasonable to assume the absent person would return to the home, or during which you did not continue to keep up the home? (Asked when this person may qualify you for head of household.)"}`
- Cite: [p501] p. 9, Temporary absences, "It must be reasonable to assume the absent person will return to the home after the temporary absence. You must continue to keep up the home during the absence." (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (helper) — `dependent.hoh_test2_lived`

- **Authored helper label:** A Test 2 person who lived with you more than half the year, or of the part of the year a relative was alive, counting every absence you counted (the home-cost condition of Test 2 is tested on the household form)
- **Encoded (Bool):** (helper "Your dependent" = true and helper "Relationship to you" ≠ 'household_member' and helper "Relationship to you" ≠ 'sibling_descendant' and helper "Relationship to you" ≠ 'other' and helper "Lived with you more than half of 2025, or, for a relative other than a qualifying child (whose months already count the part of the year), more than half of the part of 2025 they were alive or since their adoption or placement" = true or helper "Qualifying child (Step 1)" = true and helper "Married, or included on a 2025 joint return?" = false and helper "Lived with you for more than half of 2025" = true)
- Expr: `{"any":[{"all":[{"eq":["dependent.claimed",{"const":true}],"op":"test"},{"ne":["dependent.relationship",{"const":"household_member"}],"op":"test"},{"ne":["dependent.relationship",{"const":"sibling_descendant"}],"op":"test"},{"ne":["dependent.relationship",{"const":"other"}],"op":"test"},{"eq":["dependent.hoh_lived_half",{"const":true}],"op":"test"}],"op":"test"},{"all":[{"eq":["dependent.qualifying_child",{"const":true}],"op":"test"},{"eq":["dependent.married",{"const":false}],"op":"test"},{"eq":["dependent.lived_half",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2 (a dependent, other than one who is your dependent only because they lived with you all year, which is any person claimed through the last Step 4 bullet, or your unmarried qualifying child, who lived with you more than half the year) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.hoh_absence`

- **Authored helper label:** A Test 2 person only by counting an absence head of household does not count
- **Encoded (Bool):** Choose — [helper "A Test 2 person who lived with you more than half the year, or of the part of the year a relative was alive, counting every absence you counted (the home-cost condition of Test 2 is tested on the household form)" = true → helper "Counted an absence the person was not expected to return from, or during which you did not keep up the home"] [helper "A Test 2 person who lived with you more than half the year, or of the part of the year a relative was alive, counting every absence you counted (the home-cost condition of Test 2 is tested on the household form)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.hoh_test2_lived",{"const":true}],"op":"test"},"then":"dependent.absence_no_return"},{"guard":{"eq":["dependent.hoh_test2_lived",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [p501] p. 9, Temporary absences, "You and your qualifying person are considered to live together even if one or both of you are temporarily absent from your home due to special circumstances" and "It must be reasonable to assume the absent person will return to the home after the temporary absence." (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (helper) — `dependent.hoh_test2`

- **Authored helper label:** A Test 2 person who lived with you more than half the year, or of the part of the year a relative was alive, counting only absences head of household counts (the home-cost condition of Test 2 is tested on the household form)
- **Encoded (Bool):** helper "A Test 2 person who lived with you more than half the year, or of the part of the year a relative was alive, counting every absence you counted (the home-cost condition of Test 2 is tested on the household form)" = true and helper "Counted an absence the person was not expected to return from, or during which you did not keep up the home" = false
- Expr: `{"all":[{"eq":["dependent.hoh_test2_lived",{"const":true}],"op":"test"},{"eq":["dependent.absence_no_return",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2 (a dependent, other than one who is your dependent only because they lived with you all year, which is any person claimed through the last Step 4 bullet, or your unmarried qualifying child, who lived with you more than half the year); p501 p. 9, Temporary absences, "It must be reasonable to assume the absent person will return to the home after the temporary absence. You must continue to keep up the home during the absence." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.hoh_test1`

- **Authored helper label:** Qualifies you for head of household under Test 1 through a parent who does not live with you (a parent who lives with you qualifies you through Test 2)
- **Encoded (Bool):** helper "Relationship to you" = 'parent' and helper "Your dependent" = true and helper "For a parent not living with you, you paid over half the cost of their main home for all of 2025 (or the part of 2025 they were alive)?" = true
- **Refusal:** when dependent.claimed_no_tin is true, cannot complete Dependent without an SSN, ITIN or ATIN (Form 1040, Dependents, row (3)). Each dependent must be listed with an SSN (or ITIN or ATIN) issued on or before the due date of your return. A dependent child who was born and died in 2025 without an SSN, entered as "Died" on row (3) with a copy of the birth certificate, death certificate or hospital records, is outside this tool. Cite: [i1040gi] p. 22, Social security number, "You must enter each dependent’s social security number (SSN)" and "If your dependent child was born and died in 2025 and you do not have an SSN for the child, enter “Died” on row (3) of the Dependents section and include a copy of the child’s birth certificate, death certificate, or hospital records"; p. 14, Head of Household, "The dependents you claim are those you list by name and SSN ... in the Dependents section on Form 1040 or 1040-SR" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"all":[{"eq":["dependent.relationship",{"const":"parent"}],"op":"test"},{"eq":["dependent.claimed",{"const":true}],"op":"test"},{"eq":["dependent.parent_home_paid",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 1, "You paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent whom you can claim as a dependent" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.tiebreak_other`

- **Authored helper label:** With another person who can claim this person: that person is a taxpayer, or this person is also your qualifying child
- **Encoded (Bool):** (helper "Every other person this person is a qualifying child of is not a taxpayer?" = false or helper "Qualifying child tests (Step 1): relationship, age, support, joint return and residency, each asked only when the ones before it pass" = true)
- Expr: `{"any":[{"eq":["dependent.other_nontaxpayer",{"const":false}],"op":"test"},{"eq":["dependent.qc_tests",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [p501] p. 15, Qualifying Child of More Than One Person, "Sometimes, a child meets the relationship, age, residency, support, and joint return tests to be a qualifying child of more than one person."; i1040gi p. 19, Step 4, "For this purpose, a person isn’t a taxpayer if the person isn’t required to file a U.S. income tax return and either doesn’t file such a return or files only to get a refund of withheld income tax or estimated tax paid." (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (gate) — `dependent.qc_tiebreak`

- **Authored helper label:** The qualifying child of another person who is also your qualifying child, or whose other person is a taxpayer
- **Encoded (Bool):** Choose — [helper "Meets the conditions to be the qualifying child of another person?" = true → helper "With another person who can claim this person: that person is a taxpayer, or this person is also your qualifying child"] [helper "Meets the conditions to be the qualifying child of another person?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.other_claimant",{"const":true}],"op":"test"},"then":"dependent.tiebreak_other"},{"guard":{"eq":["dependent.other_claimant",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [p501] p. 15, Qualifying Child of More Than One Person, "Sometimes, a child meets the relationship, age, residency, support, and joint return tests to be a qualifying child of more than one person."; i1040gi p. 19, Step 4, "For this purpose, a person isn’t a taxpayer if the person isn’t required to file a U.S. income tax return and either doesn’t file such a return or files only to get a refund of withheld income tax or estimated tax paid." (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (helper) — `dependent.eic_child_tests`

- **Authored helper label:** EIC qualifying child tests: relationship, age, joint return and residency in the United States, each asked only when the ones before it pass
- **Encoded (Bool):** Choose — [helper "A child, sibling, or a descendant of either" = true → helper "EIC qualifying child tests from the age test on: age, joint return and residency in the United States"] [helper "A child, sibling, or a descendant of either" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.qc_relationship",{"const":true}],"op":"test"},"then":"dependent.eic_child_from_age"},{"guard":{"eq":["dependent.qc_relationship",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 41, Step 3, "A qualifying child for the EIC is your..." (relationship AND age AND not filing a joint return AND lived with you in the United States for more than half of 2025) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.eic_child_from_age`

- **Authored helper label:** EIC qualifying child tests from the age test on: age, joint return and residency in the United States
- **Encoded (Bool):** Choose — [helper "Under 19 and younger than you, under 24 a full-time student and younger than you, or permanently and totally disabled" = true → helper "EIC qualifying child tests from the joint return test on: joint return and residency in the United States"] [helper "Under 19 and younger than you, under 24 a full-time student and younger than you, or permanently and totally disabled" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.qc_age",{"const":true}],"op":"test"},"then":"dependent.eic_child_from_joint"},{"guard":{"eq":["dependent.qc_age",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 41, Step 3, "A qualifying child for the EIC is your..." (relationship AND age AND not filing a joint return AND lived with you in the United States for more than half of 2025) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.eic_child_from_joint`

- **Authored helper label:** EIC qualifying child tests from the joint return test on: joint return and residency in the United States
- **Encoded (Bool):** Choose — [helper "Included on a 2025 joint return filed other than only to claim a refund?" = true → helper "Year parameter household.no (false)"] [helper "Included on a 2025 joint return filed other than only to claim a refund?" = false → helper "Lived with you in the United States for more than half of 2025?"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.joint_return",{"const":true}],"op":"test"},"then":"dependent.no"},{"guard":{"eq":["dependent.joint_return",{"const":false}],"op":"test"},"then":"dependent.us_half"}],"op":"choose"}`
- Cite: [i1040gi] p. 41, Step 3, "A qualifying child for the EIC is your..." (relationship AND age AND not filing a joint return AND lived with you in the United States for more than half of 2025) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.eic_child`

- **Authored helper label:** Qualifying child for the EIC (relationship, age, not filing a joint return, lived with you in the United States for more than half of 2025)
- **Encoded (Bool):** helper "EIC qualifying child tests: relationship, age, joint return and residency in the United States, each asked only when the ones before it pass" = true
- **Refusal:** when dependent.kidnap_eic is true, cannot complete Kidnapped child (Pub. 501; Pub. 596 for the EIC). A child presumed kidnapped by someone who isn't a family member, who did not live with you in the United States for more than half of 2025 without counting the time missing, may count as living with you under rules this tool does not apply. Cite: [i1040gi] p. 21, Kidnapped child, "For details, see Pub. 501 (Pub. 596 for the EIC)" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when dependent.eic_tiebreak is true, cannot complete Qualifying child of more than one person (EIC). The tie-breaker rules for a child who is the qualifying child of more than one person are outside this tool. Cite: [i1040gi] p. 44, Qualifying child of more than one person (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when dependent.married is true, cannot complete Married child (EIC). A married child is a qualifying child for the EIC only under the dependency rules, which are outside this tool for a married person. Cite: [i1040gi] p. 44, Married child (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"eq":["dependent.eic_child_tests",{"const":true}],"op":"test"}`
- Cite: [i1040gi] p. 41, Step 3, "A qualifying child for the EIC is your..." (relationship AND age AND not filing a joint return AND lived with you in the United States for more than half of 2025) (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `dependent.eic_tiebreak`

- **Authored helper label:** The qualifying child of another person who is also your qualifying child for the EIC
- **Encoded (Bool):** Choose — [helper "Meets the conditions to be the qualifying child of another person?" = true → helper "EIC qualifying child tests: relationship, age, joint return and residency in the United States, each asked only when the ones before it pass"] [helper "Meets the conditions to be the qualifying child of another person?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.other_claimant",{"const":true}],"op":"test"},"then":"dependent.eic_child_tests"},{"guard":{"eq":["dependent.other_claimant",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 44, Qualifying child of more than one person, "Even if a child meets the conditions to be the qualifying child of more than one person, only one person can claim the child as a qualifying child for all of the following tax benefits" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.kidnap_eic_related`

- **Authored helper label:** A child presumed kidnapped: meets the EIC relationship test but did not live with you in the United States for more than half of 2025
- **Encoded (Bool):** Choose — [helper "A child, sibling, or a descendant of either" = true → helper "Did not live with you in the United States for more than half of 2025"] [helper "A child, sibling, or a descendant of either" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.qc_relationship",{"const":true}],"op":"test"},"then":"dependent.not_us_half"},{"guard":{"eq":["dependent.qc_relationship",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 21, Kidnapped child, "the credit for other dependents, and the earned income credit (EIC). For details, see Pub. 501 (Pub. 596 for the EIC)." (a child who lived with you in the United States for more than half of 2025 meets the residency test without this treatment) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.not_us_half`

- **Authored helper label:** Did not live with you in the United States for more than half of 2025
- **Encoded (Bool):** helper "Lived with you in the United States for more than half of 2025?" = false
- Expr: `{"eq":["dependent.us_half",{"const":false}],"op":"test"}`
- Cite: [i1040gi] p. 21, Kidnapped child, "the credit for other dependents, and the earned income credit (EIC). For details, see Pub. 501 (Pub. 596 for the EIC)." (a child who lived with you in the United States for more than half of 2025 meets the residency test without this treatment) (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `dependent.kidnap_eic`

- **Authored helper label:** A child presumed kidnapped who meets the EIC relationship test but did not live with you in the United States for more than half of 2025, not counting the time missing
- **Encoded (Bool):** Choose — [helper "A child kidnapped by someone who isn't a member of your family or the child's family, presumed kidnapped by law enforcement, and missing because of it at some time in 2025?" = true → helper "A child presumed kidnapped: meets the EIC relationship test but did not live with you in the United States for more than half of 2025"] [helper "A child kidnapped by someone who isn't a member of your family or the child's family, presumed kidnapped by law enforcement, and missing because of it at some time in 2025?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.kidnapped",{"const":true}],"op":"test"},"then":"dependent.kidnap_eic_related"},{"guard":{"eq":["dependent.kidnapped",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 21, Kidnapped child, "the credit for other dependents, and the earned income credit (EIC). For details, see Pub. 501 (Pub. 596 for the EIC)." (a child who lived with you in the United States for more than half of 2025 meets the residency test without this treatment) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.eic_ssn_child`

- **Authored helper label:** Qualifying child for the EIC who has a valid SSN
- **Encoded (Bool):** Choose — [helper "Qualifying child for the EIC (relationship, age, not filing a joint return, lived with you in the United States for more than half of 2025)" = true → helper "SSN valid for the EIC, issued on or before the due date of your return?"] [helper "Qualifying child for the EIC (relationship, age, not filing a joint return, lived with you in the United States for more than half of 2025)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.eic_child",{"const":true}],"op":"test"},"then":"dependent.eic_ssn"},{"guard":{"eq":["dependent.eic_child",{"const":false}],"op":"test"},"then":"dependent.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 2, "the number of qualifying children you have who have valid SSNs"; pp. 44–45, Social security number (SSN), "For the EIC, a valid SSN is a number issued by the Social Security Administration unless 'Not Valid for Employment' is printed on the social security card" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.dc_child_all_year`

- **Authored helper label:** Your qualifying child who is your dependent and was under age 13 for all of 2025 (age 12 or younger at the end of 2025)
- **Encoded (Bool):** helper "Qualifying child who is your dependent (Step 2)" = true and helper "Age at the end of 2025" < 13 (dc.child_age)
- Expr: `{"all":[{"eq":["dependent.qc_dependent",{"const":true}],"op":"test"},{"lt":["dependent.age",{"param":"dc.child_age"}],"op":"test"}],"op":"test"}`
- Cite: [i2441] p. 1, Qualifying Person(s), "A qualifying child under age 13 whom you can claim as a dependent. If the child turned 13 during the year, the child is a qualifying person for the part of the year they were under age 13" (2025; sha256 86f0669e)

## (helper) — `dependent.dc_age13`

- **Authored helper label:** Your qualifying child who is your dependent and was 13 at the end of 2025 (who may have been under 13 for part of the year)
- **Encoded (Bool):** helper "Qualifying child who is your dependent (Step 2)" = true and helper "Age at the end of 2025" = 13 (dc.child_age)
- Expr: `{"all":[{"eq":["dependent.qc_dependent",{"const":true}],"op":"test"},{"eq":["dependent.age",{"param":"dc.child_age"}],"op":"test"}],"op":"test"}`
- Cite: [i2441] p. 1, Qualifying Person(s), "A qualifying child under age 13 whom you can claim as a dependent. If the child turned 13 during the year, the child is a qualifying person for the part of the year they were under age 13" (2025; sha256 86f0669e)

## (helper) — `dependent.dc_under13`

- **Authored helper label:** Under age 13 for part of 2025 when the care was provided?
- **Encoded (Bool):** Input — Was this child under age 13 for part of 2025, when you paid for their care? (A child who turned 13 in 2025 is a qualifying person only for the part of the year before their 13th birthday.)
- Expr: `{"op":"input","source":"Was this child under age 13 for part of 2025, when you paid for their care? (A child who turned 13 in 2025 is a qualifying person only for the part of the year before their 13th birthday.)"}`
- Cite: [p503] p. 3, Person qualifying for part of year, "You determine a person's qualifying status each day. For example, if your child for whom you pay child and dependent care expenses turns 13 years old and no longer qualifies on September 16, count only those expenses through September 15" (For use in preparing 2025 returns; sha256 3a00d0c1)

## (helper) — `dependent.dc_child`

- **Authored helper label:** Your qualifying child who is your dependent, turned 13 during 2025 and was under 13 for part of 2025 when the care was provided
- **Encoded (Bool):** helper "Your qualifying child who is your dependent and was 13 at the end of 2025 (who may have been under 13 for part of the year)" = true and helper "Under age 13 for part of 2025 when the care was provided?" = true
- Expr: `{"all":[{"eq":["dependent.dc_age13",{"const":true}],"op":"test"},{"eq":["dependent.dc_under13",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i2441] p. 1, Qualifying Person(s), "A qualifying child under age 13 whom you can claim as a dependent. If the child turned 13 during the year, the child is a qualifying person for the part of the year they were under age 13" (2025; sha256 86f0669e)

## (helper) — `dependent.dc_incapable`

- **Authored helper label:** Physically or mentally not able to care for themselves?
- **Encoded (Bool):** Input — In 2025, was this person physically or mentally not able to care for themselves (unable to dress, clean or feed themselves because of a physical or mental disability, or needing constant attention to prevent them from injuring themselves or others)? This is a different test from permanent and total disability.
- Expr: `{"op":"input","source":"In 2025, was this person physically or mentally not able to care for themselves (unable to dress, clean or feed themselves because of a physical or mental disability, or needing constant attention to prevent them from injuring themselves or others)? This is a different test from permanent and total disability."}`
- Cite: [i2441] p. 1, Physically or mentally not able to care for oneself, "Persons who can't dress, clean, or feed themselves because of physical or mental disabilities are considered not able to care for themselves. Also, persons who must have constant attention to prevent them from injuring themselves or others are considered not able to care for themselves" (2025; sha256 86f0669e)

## (helper) — `dependent.dc_disabled_qp`

- **Authored helper label:** Your dependent who lived with you for more than half of 2025 and was not able to care for themselves
- **Encoded (Bool):** helper "Physically or mentally not able to care for themselves?" = true and helper "Lived with you more than half of 2025, or, for a person other than a qualifying child born or who died in 2025, more than half of the part of 2025 they were alive" = true
- Expr: `{"all":[{"eq":["dependent.dc_incapable",{"const":true}],"op":"test"},{"eq":["dependent.dc_lived_half",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i2441] p. 1, Qualifying Person(s), "Any disabled person who wasn't physically or mentally able to care for themselves who lived with you for more than half the year and whom you can claim as a dependent"; p503 p. 3, Birth or death of otherwise qualifying person (2025; sha256 86f0669e)

## (helper) — `dependent.dc_qp`

- **Authored helper label:** A qualifying person for Form 2441 (you have care expenses, and this person is your dependent and either your qualifying child under 13 or not able to care for themselves and living with you for more than half the year)
- **Encoded (Bool):** f2441 helper "Did you pay for the care of a qualifying person so you could work or look for work?" = true and helper "Your dependent" = true and (helper "Your qualifying child who is your dependent and was under age 13 for all of 2025 (age 12 or younger at the end of 2025)" = true or helper "Your dependent who lived with you for more than half of 2025 and was not able to care for themselves" = true or helper "Your qualifying child who is your dependent, turned 13 during 2025 and was under 13 for part of 2025 when the care was provided" = true)
- Expr: `{"all":[{"eq":["f2441.care",{"const":true}],"op":"test"},{"eq":["dependent.claimed",{"const":true}],"op":"test"},{"any":[{"eq":["dependent.dc_child_all_year",{"const":true}],"op":"test"},{"eq":["dependent.dc_disabled_qp",{"const":true}],"op":"test"},{"eq":["dependent.dc_child",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i2441] p. 1, Qualifying Person(s), "A qualifying child under age 13 whom you can claim as a dependent. If the child turned 13 during the year, the child is a qualifying person for the part of the year they were under age 13"; p. 1, Qualifying Person(s), "Any disabled person who wasn't physically or mentally able to care for themselves who lived with you for more than half the year and whom you can claim as a dependent"; p. 3, Line 2, "Don't list a person on line 2 unless they are listed as an eligible person under Qualifying Person(s), earlier" (2025; sha256 86f0669e)

## (helper) — `dependent.dc_count`

- **Authored helper label:** One, for every entry (counted as a qualifying person only where dependent.dc_qp holds)
- **Encoded (Count):** Enter 1 (dependent.one).
- Expr: `{"op":"param","ref":"dependent.one"}`
- Cite: [i2441] p. 3, Line 2, "Complete columns (a) through (d) for each qualifying person"; p. 3, Column (b), "You must enter the qualifying person's SSN" (a qualifying person is a dependent, and a dependent without an SSN, ITIN or ATIN is refused where the person is counted as a dependent) (2025; sha256 86f0669e)

## (helper) — `dependent.dc_paid`

- **Authored helper label:** Qualified expenses incurred and paid in 2025 for this person's care
- **Encoded (NonNegDollars):** Input — Qualified expenses you incurred and paid in 2025 for this person's care while they were a qualifying person (under age 13, or not able to care for themselves), so that you (and your spouse, if filing jointly) could work or look for work (unpaid volunteer work, or work for a nominal salary, is not work)

  Include:
  - care you prepaid in 2024 for 2025
  - your share of employment taxes on a care provider's wages
  - expenses paid with dependent care benefits (reimbursed from a dependent care account or paid by your employer to a provider you chose); Form 2441 subtracts the benefits you exclude

  Include also:
  - household services needed to run your home if they were partly for this person's care (for example a cook, maid, babysitter, housekeeper or cleaning person, but not a chauffeur, bartender or gardener)
  - meals your housekeeper eats in your home because of the job and the extra cost of lodging the housekeeper in your home
  - a care provider's transportation of this person to or from the place of care (but not other transportation, or the cost of bringing the provider to your home)
  - agency fees, deposits, application fees and other indirect costs you had to pay to get care (but not a forfeited deposit for care that was not provided)

  Do not include the value of care your employer furnished itself (at your workplace or through a care provider your employer hired).

  Do not include:
  - 2024 care paid in 2025
  - 2025 care paid in 2026
  - payments for care in 2026
  - amounts reimbursed by a state social services agency
  - payments to a provider who may not be listed (your spouse, your dependent, your child under 19, or the parent of your child under 13)
  - expenses you claim as medical expenses
  - the cost of food, lodging, education, clothing or entertainment other than the housekeeper's meals and lodging above (food or schooling incidental to a child's care that can't be separated from the total cost may be included, but never schooling for a child in kindergarten or above)
  - expenses for an overnight camp, a summer school or a tutoring program
  - care outside your home for a qualifying person other than your dependent under 13 who does not regularly spend at least 8 hours a day in your home
  - care at a dependent care center that does not meet all applicable state and local regulations
  - child support payments

  If you (or your spouse) worked or looked for work during only part of the period the expenses cover, count the expenses only for the days of work or looking for work (a day you work at least 1 hour is a day of work).

  But include:
  - care you had to pay for anyway during a short, temporary absence from work, such as a vacation or minor illness (2 weeks or less, or longer depending on the circumstances)
  - for part-time work, care you must pay for weekly, monthly or in another way that covers both days worked and days not worked

  If part of an expense is work related and part is for other purposes, count only the work-related part, unless only a small part is for other purposes.

  Zero if none
- Interpretation: amb.2025.dc_line30
- Expr: `{"op":"input","source":"Qualified expenses you incurred and paid in 2025 for this person's care while they were a qualifying person (under age 13, or not able to care for themselves), so that you (and your spouse, if filing jointly) could work or look for work (unpaid volunteer work, or work for a nominal salary, is not work)\n\nInclude:\n- care you prepaid in 2024 for 2025\n- your share of employment taxes on a care provider's wages\n- expenses paid with dependent care benefits (reimbursed from a dependent care account or paid by your employer to a provider you chose); Form 2441 subtracts the benefits you exclude\n\nInclude also:\n- household services needed to run your home if they were partly for this person's care (for example a cook, maid, babysitter, housekeeper or cleaning person, but not a chauffeur, bartender or gardener)\n- meals your housekeeper eats in your home because of the job and the extra cost of lodging the housekeeper in your home\n- a care provider's transportation of this person to or from the place of care (but not other transportation, or the cost of bringing the provider to your home)\n- agency fees, deposits, application fees and other indirect costs you had to pay to get care (but not a forfeited deposit for care that was not provided)\n\nDo not include the value of care your employer furnished itself (at your workplace or through a care provider your employer hired).\n\nDo not include:\n- 2024 care paid in 2025\n- 2025 care paid in 2026\n- payments for care in 2026\n- amounts reimbursed by a state social services agency\n- payments to a provider who may not be listed (your spouse, your dependent, your child under 19, or the parent of your child under 13)\n- expenses you claim as medical expenses\n- the cost of food, lodging, education, clothing or entertainment other than the housekeeper's meals and lodging above (food or schooling incidental to a child's care that can't be separated from the total cost may be included, but never schooling for a child in kindergarten or above)\n- expenses for an overnight camp, a summer school or a tutoring program\n- care outside your home for a qualifying person other than your dependent under 13 who does not regularly spend at least 8 hours a day in your home\n- care at a dependent care center that does not meet all applicable state and local regulations\n- child support payments\n\nIf you (or your spouse) worked or looked for work during only part of the period the expenses cover, count the expenses only for the days of work or looking for work (a day you work at least 1 hour is a day of work).\n\nBut include:\n- care you had to pay for anyway during a short, temporary absence from work, such as a vacation or minor illness (2 weeks or less, or longer depending on the circumstances)\n- for part-time work, care you must pay for weekly, monthly or in another way that covers both days worked and days not worked\n\nIf part of an expense is work related and part is for other purposes, count only the work-related part, unless only a small part is for other purposes.\n\nZero if none"}`
- Cite: [i2441] pp. 3–4, Column (d), "Enter the qualified expenses you incurred and paid in 2025 for the person listed in column (a)" and "Expenses you incurred in 2025 but didn't pay until 2026"; p503 p. 10, Expenses prepaid in an earlier year, "If you pay for services before they are provided, you can count the prepaid expenses only in the year the care is received"; p. 2, Care of the qualifying person, "It doesn't include the cost of food, lodging, education, clothing, or entertainment. You can include the cost of care provided outside your home for your dependent under age 13, or any other qualifying person who regularly spends at least 8 hours a day in your home. If the care was provided by a dependent care center, the center must meet all applicable state and local regulations." and "But don't include the cost of schooling for a child in kindergarten or above." and "But don't include any expenses for sending your child to an overnight camp, a summer school, or a tutoring program."; p. 2, "Child support payments aren't qualified expenses." and "Generally, if you worked or actively looked for work during only part of the period in which you incurred the expenses, you must figure your expenses for each day."; p503 p. 6, Temporary absence from work, "An absence of 2 weeks or less is a short, temporary absence."; p503 p. 6, Part-time work, "However, if you are required to pay for care weekly, monthly, or in another way that includes both days worked and days not worked, you can figure your credit including the expenses you paid for days you didn't work. Any day when you work at least 1 hour is a day of work."; p503 p. 8, Expenses partly work related, "If part of an expense is work related (for either household services or the care of a qualifying person) and part is for other purposes, you have to divide the expense." and "However, you don't have to divide the expense if only a small part is for other purposes."; p. 1, Qualified Expenses, "These include amounts paid for household services and care of the qualifying person while you worked or looked for work."; p. 2, Household services, "They include, for example, the services of a cook, maid, babysitter, housekeeper, or cleaning person if the services were partly for the care of the qualifying person. However, they don't include the services of a chauffeur, bartender, or gardener."; p503 p. 6, Volunteer work, "For this purpose, you aren't considered to be working if you do unpaid volunteer work or work for a nominal salary."; p503 p. 7, Transportation, "If a care provider takes a qualifying person to or from a place where care is provided, that transportation is for the care of the qualifying person." and "However, transportation not provided by a care provider isn't for the care of a qualifying person. Also, if you pay the transportation cost for the care provider to come to your home, that expense isn't for care of a qualifying person."; p503 p. 7, Fees and deposits, "Fees you paid to an agency to get the services of a care provider, deposits you paid to an agency or preschool, application fees, and other indirect expenses are work-related expenses if you have to pay them to get care" and "However, a forfeited deposit isn't for the care of a qualifying person if care isn't provided."; p503 p. 8, Meals and lodging provided for housekeeper, "If you have expenses for meals that your housekeeper eats in your home because of their employment, count these as work-related expenses. If you have extra expenses for providing lodging in your home to the housekeeper, count these as work-related expenses also."; p. 3, Columns (a) and (b), "If you were covered by your employer's dependent care plan and your employer furnished the care (either at your workplace or by hiring a care provider), enter your employer's name in column (a)" (2025; sha256 86f0669e)

## 2(d) — `dependent.dc_line2d`

- **Authored helper label:** Qualified expenses you incurred and paid in 2025 for the person listed in column (a)
- **Encoded (NonNegDollars):** Enter the amount from helper "Qualified expenses incurred and paid in 2025 for this person's care".
- **Shown on the values sheet only when:** A qualifying person for Form 2441 (you have care expenses, and this person is your dependent and either your qualifying child under 13 or not able to care for themselves and living with you for more than half the year) (`dependent.dc_qp`)
- Interpretation: amb.2025.dc_line30
- Expr: `{"from":"dependent.dc_paid","op":"copy"}`
- Cite: [f2441] Form 2441 (2025), line 2, column (d) (2025; created 2025-03-18; sha256 6c3c2d19)

## (helper) — `dependent.dc_over12_care`

- **Authored helper label:** Care provided while this qualifying person was age 13 or older and disabled
- **Encoded (Bool):** Input — Of the care expenses included for this person on Form 2441, line 2, was any care provided when the person was age 13 or older and physically or mentally unable to care for themselves? Answer only for the care included on this form, not their age at the end of the year.
- Expr: `{"op":"input","source":"Of the care expenses included for this person on Form 2441, line 2, was any care provided when the person was age 13 or older and physically or mentally unable to care for themselves? Answer only for the care included on this form, not their age at the end of the year."}`
- Cite: [i2441] p. 3, Column (c), "Check the box in column (c) if the qualifying person listed in column (a) was over age 12 at the time the care was provided and was disabled" (2025; sha256 86f0669e)

## 2(c) — `dependent.dc_line2c`

- **Authored helper label:** Check here if the qualifying person was over age 12 and was disabled
- **Encoded (Bool):** helper "A qualifying person for Form 2441 (you have care expenses, and this person is your dependent and either your qualifying child under 13 or not able to care for themselves and living with you for more than half the year)" = true and helper "Physically or mentally not able to care for themselves?" = true and (helper "Age at the end of 2025" > 13 (dc.child_age) or helper "Age at the end of 2025" = 13 (dc.child_age) and helper "Care provided while this qualifying person was age 13 or older and disabled" = true)
- **Shown on the values sheet only when:** A qualifying person for Form 2441 (you have care expenses, and this person is your dependent and either your qualifying child under 13 or not able to care for themselves and living with you for more than half the year) (`dependent.dc_qp`)
- Expr: `{"all":[{"eq":["dependent.dc_qp",{"const":true}],"op":"test"},{"eq":["dependent.dc_incapable",{"const":true}],"op":"test"},{"any":[{"gt":["dependent.age",{"param":"dc.child_age"}],"op":"test"},{"all":[{"eq":["dependent.age",{"param":"dc.child_age"}],"op":"test"},{"eq":["dependent.dc_over12_care",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i2441] p. 3, Column (c), "Check the box in column (c) if the qualifying person listed in column (a) was over age 12 at the time the care was provided and was disabled" (2025; sha256 86f0669e)

## (gate) — `dependent.ptc_files`

- **Authored helper label:** Is this dependent required to file a 2025 return because of their income (Chart B in the Form 1040 instructions)?
- **Encoded (Bool):** Input — Is this dependent required to file a 2025 income tax return because of their income, by Chart B in the Form 1040 instructions (unearned income over $1,350, earned income over $15,750, or gross income over the larger of $1,350 and earned income up to $15,300 plus $450, for a single dependent under 65 and not blind)? Answer no if the dependent files only to claim a refund of withheld or estimated tax.
- Interpretation: amb.2025.ptc_dependent_filing
- Expr: `{"op":"input","source":"Is this dependent required to file a 2025 income tax return because of their income, by Chart B in the Form 1040 instructions (unearned income over $1,350, earned income over $15,750, or gross income over the larger of $1,350 and earned income up to $15,300 plus $450, for a single dependent under 65 and not blind)? Answer no if the dependent files only to claim a refund of withheld or estimated tax."}`
- Cite: [i8962] p. 8, Line 2b, "Only include your dependents who are required to file an income tax return because their income meets the income tax return filing threshold.", "Do not include the modified AGI of dependents who are filing a tax return only to claim a refund of tax withheld or estimated tax."; i1040gi p. 10, Chart B—For Children and Other Dependents, "Your unearned income was over $1,350." (2025; sha256 f4ac86ad)

## (helper) — `dependent.ptc_magi`

- **Authored helper label:** This dependent's modified AGI (Worksheet 1-2)
- **Encoded (Dollars):** Input — This dependent's modified AGI for 2025: the AGI on their return (line 11a), plus their tax-exempt interest (line 2a), plus any Form 2555 amounts, plus the part of their social security benefits that is not taxable (line 6a less line 6b); negative if it was a loss
- Expr: `{"op":"input","source":"This dependent's modified AGI for 2025: the AGI on their return (line 11a), plus their tax-exempt interest (line 2a), plus any Form 2555 amounts, plus the part of their social security benefits that is not taxable (line 6a less line 6b); negative if it was a loss"}`
- Cite: [i8962] p. 8, Worksheet 1-2, "Only include your dependents who are required to file an income tax return because their income meets the income tax return filing threshold." (2025; sha256 f4ac86ad)

## (helper) — `dependent.ptc_magi_counted`

- **Authored helper label:** This dependent's modified AGI counted in household income (zero unless required to file because of income)
- **Encoded (Dollars):** Choose — [helper "Is this dependent required to file a 2025 return because of their income (Chart B in the Form 1040 instructions)?" = true → helper "This dependent's modified AGI (Worksheet 1-2)"] [helper "Is this dependent required to file a 2025 return because of their income (Chart B in the Form 1040 instructions)?" = false → helper "No amount for this person"]
- Interpretation: amb.2025.ptc_dependent_filing
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.ptc_files",{"const":true}],"op":"test"},"then":"dependent.ptc_magi"},{"guard":{"eq":["dependent.ptc_files",{"const":false}],"op":"test"},"then":"dependent.zero"}],"op":"choose"}`
- Cite: [i8962] p. 8, Line 2b, "Only include your dependents who are required to file an income tax return because their income meets the income tax return filing threshold." (2025; sha256 f4ac86ad)

## (gate) — `dependent.edu`

- **Authored helper label:** Qualified education expenses paid in 2025 for this dependent
- **Encoded (Bool):** Input — Did anyone pay qualified education expenses in 2025 for this dependent at an eligible educational institution (a college, university, vocational school, or other postsecondary school eligible for federal student aid)?
- Expr: `{"op":"input","source":"Did anyone pay qualified education expenses in 2025 for this dependent at an eligible educational institution (a college, university, vocational school, or other postsecondary school eligible for federal student aid)?"}`
- Cite: [i8863] p. 2, Who Can Claim an Education Credit, "You may be able to claim an education credit if you, your spouse, or a dependent you claim on your tax return was a student enrolled at or attending an eligible educational institution." (2025; sha256 195cfd5e)

## (gate) — `dependent.edu_1098t`

- **Authored helper label:** The student received a 2025 Form 1098-T from the institution, or an exception applies
- **Encoded (Bool):** Input — Did the student receive a 2025 Form 1098-T from the educational institution? Answer yes also if the institution was not required to furnish one (for example a qualified nonresident alien, expenses paid entirely with scholarships or under a formal billing arrangement, or only courses for which no academic credit is awarded), or if the institution did not furnish it and, after February 2, 2026, but before you file, you or the student requested it, you fully cooperated with the institution's efforts to gather the information needed to furnish it, and you can show the enrollment and the payments.
- Interpretation: amb.2025.edu_1098t_date
- Expr: `{"op":"input","source":"Did the student receive a 2025 Form 1098-T from the educational institution? Answer yes also if the institution was not required to furnish one (for example a qualified nonresident alien, expenses paid entirely with scholarships or under a formal billing arrangement, or only courses for which no academic credit is awarded), or if the institution did not furnish it and, after February 2, 2026, but before you file, you or the student requested it, you fully cooperated with the institution's efforts to gather the information needed to furnish it, and you can show the enrollment and the payments."}`
- Cite: [i8863] p. 1, Form 1098-T requirement, "To be eligible to claim the American opportunity credit or the lifetime learning credit, the law requires a taxpayer (or a dependent) to have received Form 1098-T, Tuition Statement, from an eligible educational institution, whether domestic or foreign."; p. 1, "You must fully cooperate with the educational institution’s efforts to gather the information needed to furnish the Form 1098-T." (2025; sha256 195cfd5e)

## (helper) — `dependent.edu_student`

- **Authored helper label:** An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception), and claimed as your dependent
- **Encoded (Bool):** Choose — [f8863 helper "Qualified education expenses paid in 2025 for you, your spouse or a dependent you claim" = true → helper "With education expenses paid: claimed as your dependent, a student with qualified expenses, a TIN by the due date and a Form 1098-T (or an exception)"] [f8863 helper "Qualified education expenses paid in 2025 for you, your spouse or a dependent you claim" = false → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["f8863.paid",{"const":true}],"op":"test"},"then":"dependent.edu_student_claimed"},{"guard":{"eq":["f8863.paid",{"const":false}],"op":"test"},"then":"dependent.edu_no"}],"op":"choose"}`
- Cite: [i8863] p. 2, Who can claim a dependent’s expenses, "If a student is claimed as a dependent on another person’s tax return, all qualified education expenses of the student are treated as having been paid by that person. Therefore, only that person can claim an education credit for the student." (2025; sha256 195cfd5e)

## (helper) — `dependent.edu_student_claimed`

- **Authored helper label:** With education expenses paid: claimed as your dependent, a student with qualified expenses, a TIN by the due date and a Form 1098-T (or an exception)
- **Encoded (Bool):** Choose — [helper "Your dependent" = true → helper "Your dependent: a student with qualified expenses, a TIN by the due date and a Form 1098-T (or an exception)"] [helper "Your dependent" = false → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.claimed",{"const":true}],"op":"test"},"then":"dependent.edu_student_edu"},{"guard":{"eq":["dependent.claimed",{"const":false}],"op":"test"},"then":"dependent.edu_no"}],"op":"choose"}`
- Cite: [i8863] p. 2, Who can claim a dependent’s expenses, "If a student is claimed as a dependent on another person’s tax return, all qualified education expenses of the student are treated as having been paid by that person. Therefore, only that person can claim an education credit for the student." (2025; sha256 195cfd5e)

## (helper) — `dependent.edu_student_edu`

- **Authored helper label:** Your dependent: a student with qualified expenses, a TIN by the due date and a Form 1098-T (or an exception)
- **Encoded (Bool):** Choose — [helper "Qualified education expenses paid in 2025 for this dependent" = true → helper "A student with qualified expenses: a TIN by the due date and a Form 1098-T (or an exception)"] [helper "Qualified education expenses paid in 2025 for this dependent" = false → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.edu",{"const":true}],"op":"test"},"then":"dependent.edu_student_tin"},{"guard":{"eq":["dependent.edu",{"const":false}],"op":"test"},"then":"dependent.edu_no"}],"op":"choose"}`
- Cite: [i8863] p. 2, Who Can Claim an Education Credit, "You may be able to claim an education credit if you, your spouse, or a dependent you claim on your tax return was a student enrolled at or attending an eligible educational institution." (2025; sha256 195cfd5e)

## (helper) — `dependent.edu_student_tin`

- **Authored helper label:** A student with qualified expenses: a TIN by the due date and a Form 1098-T (or an exception)
- **Encoded (Bool):** Choose — [helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = true → helper "The student received a 2025 Form 1098-T from the institution, or an exception applies"] [helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = false → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.tin",{"const":true}],"op":"test"},"then":"dependent.edu_1098t"},{"guard":{"eq":["dependent.tin",{"const":false}],"op":"test"},"then":"dependent.edu_no"}],"op":"choose"}`
- Cite: [i8863] p. 3, Who cannot claim a credit, "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)." (2025; sha256 195cfd5e)

## (helper) — `dependent.edu_inst`

- **Authored helper label:** Qualified education expenses required to be paid to the institution
- **Encoded (NonNegDollars):** Input — Qualified education expenses paid in 2025 for this student, by anyone, that had to be paid to the institution, for academic periods beginning in 2025 or in the first 3 months of 2026:

  - tuition
  - required enrollment fees
  - books, supplies and equipment required to be paid to the institution as a condition of enrollment or attendance

  Use the amounts actually paid, which may differ from Form 1098-T box 1.

  Do not include:
  - amounts paid in 2024 or 2026
  - room and board
  - insurance
  - medical expenses (including student health fees)
  - transportation
  - expenses deducted elsewhere (for example on Schedule C)
  - expenses used for a tax-free distribution from a Coverdell ESA or qualified tuition program (529 plan)
  - a course or other education involving sports, games or hobbies, or any noncredit course, unless it is part of the student's degree program or, where this student can't get the American opportunity credit, it helps the student acquire or improve job skills

  Zero if none
- Expr: `{"op":"input","source":"Qualified education expenses paid in 2025 for this student, by anyone, that had to be paid to the institution, for academic periods beginning in 2025 or in the first 3 months of 2026:\n\n- tuition\n- required enrollment fees\n- books, supplies and equipment required to be paid to the institution as a condition of enrollment or attendance\n\nUse the amounts actually paid, which may differ from Form 1098-T box 1.\n\nDo not include:\n- amounts paid in 2024 or 2026\n- room and board\n- insurance\n- medical expenses (including student health fees)\n- transportation\n- expenses deducted elsewhere (for example on Schedule C)\n- expenses used for a tax-free distribution from a Coverdell ESA or qualified tuition program (529 plan)\n- a course or other education involving sports, games or hobbies, or any noncredit course, unless it is part of the student's degree program or, where this student can't get the American opportunity credit, it helps the student acquire or improve job skills\n\nZero if none"}`
- Cite: [i8863] p. 4, Qualified Education Expenses, "Generally, qualified education expenses are amounts paid in 2025 for tuition and fees required for the student’s enrollment or attendance at an eligible educational institution."; p. 4, "Any course or other education involving sports, games, or hobbies, or any noncredit course, unless such course or other education is part of the student’s degree program or (for the lifetime learning credit only) helps the student acquire or improve job skills." (2025; sha256 195cfd5e)

## (helper) — `dependent.edu_mat`

- **Authored helper label:** Other course materials (American opportunity credit only)
- **Encoded (NonNegDollars):** Input — Other course materials paid for in 2025 for this student: books, supplies and equipment needed for a course of study that did not have to be paid to the institution (they count for the American opportunity credit only); the same exclusions as for the expenses paid to the institution; zero if none
- Expr: `{"op":"input","source":"Other course materials paid for in 2025 for this student: books, supplies and equipment needed for a course of study that did not have to be paid to the institution (they count for the American opportunity credit only); the same exclusions as for the expenses paid to the institution; zero if none"}`
- Cite: [i8863] p. 4, Qualified Education Expenses, "American opportunity credit: Qualified education expenses include amounts paid for tuition, fees, and course materials, which include books, supplies, and equipment needed for a course of study, whether or not the materials are purchased from the educational institution as a condition of enrollment or attendance." (2025; sha256 195cfd5e)

## (helper) — `dependent.edu_a2025`

- **Authored helper label:** Adjusted Qualified Education Expenses Worksheet, line 2a
- **Encoded (NonNegDollars):** Input — Tax-free educational assistance received in 2025 for this student's 2025 expenses: the tax-free part of scholarships and fellowship grants (including Pell grants; Form 1098-T box 5 may help), tax-free employer-provided educational assistance, veterans' educational assistance, and other tax-free educational assistance. Do not include wages, loans, gifts, inheritances, withdrawals from personal savings, emergency financial aid grants, or a scholarship the student includes in income (for you or your spouse, the amount on Schedule 1 line 8r); zero if none
- Expr: `{"op":"input","source":"Tax-free educational assistance received in 2025 for this student's 2025 expenses: the tax-free part of scholarships and fellowship grants (including Pell grants; Form 1098-T box 5 may help), tax-free employer-provided educational assistance, veterans' educational assistance, and other tax-free educational assistance. Do not include wages, loans, gifts, inheritances, withdrawals from personal savings, emergency financial aid grants, or a scholarship the student includes in income (for you or your spouse, the amount on Schedule 1 line 8r); zero if none"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "a. Tax-free educational assistance received in 2025 allocable to the academic period" (2025; sha256 195cfd5e)

## (helper) — `dependent.edu_a2026`

- **Authored helper label:** Adjusted Qualified Education Expenses Worksheet, line 2b
- **Encoded (NonNegDollars):** Input — Tax-free educational assistance received in 2026, before you file this return, that is allocable to an academic period of these 2025 expenses; zero if none
- Expr: `{"op":"input","source":"Tax-free educational assistance received in 2026, before you file this return, that is allocable to an academic period of these 2025 expenses; zero if none"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "b. Tax-free educational assistance received in 2026 (and before you file your 2025 tax return) allocable to the academic period" (2025; sha256 195cfd5e)

## (helper) — `dependent.edu_refunds`

- **Authored helper label:** Adjusted Qualified Education Expenses Worksheet, line 2c
- **Encoded (NonNegDollars):** Input — Refunds of these 2025 qualified education expenses received in 2025, or in 2026 before you file this return; zero if none
- Expr: `{"op":"input","source":"Refunds of these 2025 qualified education expenses received in 2025, or in 2026 before you file this return; zero if none"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "c. Refunds of qualified education expenses paid in 2025 if the refund is received in 2025 or in 2026 before you file your 2025 tax return" (2025; sha256 195cfd5e)

## (helper) — `dependent.edu_adj_sum`

- **Authored helper label:** Add lines 2a, 2b and 2c
- **Encoded (NonNegDollars):** Add helper "Adjusted Qualified Education Expenses Worksheet, line 2a", helper "Adjusted Qualified Education Expenses Worksheet, line 2b", and helper "Adjusted Qualified Education Expenses Worksheet, line 2c".
- Expr: `{"of":["dependent.edu_a2025","dependent.edu_a2026","dependent.edu_refunds"],"op":"sum"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "3. Total adjustments (add lines 2a, 2b, and 2c)" (2025; sha256 195cfd5e)

## (helper) — `dependent.edu_adj`

- **Authored helper label:** Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c
- **Encoded (NonNegDollars):** Choose — [helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception), and claimed as your dependent" = true → helper "Add lines 2a, 2b and 2c"] [helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception), and claimed as your dependent" = false → helper "No amount for this person"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.edu_student",{"const":true}],"op":"test"},"then":"dependent.edu_adj_sum"},{"guard":{"eq":["dependent.edu_student",{"const":false}],"op":"test"},"then":"dependent.zero"}],"op":"choose"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "3. Total adjustments (add lines 2a, 2b, and 2c)" (2025; sha256 195cfd5e)

## (gate) — `dependent.edu_over`

- **Authored helper label:** An academic period whose tax-free assistance and refunds exceed its expenses paid to the institution
- **Encoded (Bool):** Input — Was there an academic period for which the tax-free educational assistance and refunds allocable to it were more than that period's qualified education expenses that had to be paid to the institution (tuition, required fees and course materials required to be paid to the institution)?
- Expr: `{"op":"input","source":"Was there an academic period for which the tax-free educational assistance and refunds allocable to it were more than that period's qualified education expenses that had to be paid to the institution (tuition, required fees and course materials required to be paid to the institution)?"}`
- Cite: [i8863] p. 4, Tax-free educational assistance, "For tax-free educational assistance received in 2025, reduce the qualified education expenses for each academic period by the amount of tax-free educational assistance allocable to that academic period." (2025; sha256 195cfd5e)

## (helper) — `dependent.edu_has_adj`

- **Authored helper label:** Adjusted qualified education expenses (worksheet line 3) above zero
- **Encoded (Bool):** helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c" > $0
- Expr: `{"gt":["dependent.edu_adj",{"const":0}],"op":"test"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)

## (helper) — `dependent.edu_over_if_adj`

- **Authored helper label:** Adjustments that exceed one academic period's expenses, where adjusted qualified education expenses are above zero
- **Encoded (Bool):** Choose — [helper "Adjusted qualified education expenses (worksheet line 3) above zero" = true → helper "An academic period whose tax-free assistance and refunds exceed its expenses paid to the institution"] [helper "Adjusted qualified education expenses (worksheet line 3) above zero" = false → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.edu_has_adj",{"const":true}],"op":"test"},"then":"dependent.edu_over"},{"guard":{"eq":["dependent.edu_has_adj",{"const":false}],"op":"test"},"then":"dependent.edu_no"}],"op":"choose"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)

## (gate) — `dependent.edu_over_refused`

- **Authored helper label:** Adjustments that exceed one academic period's expenses
- **Encoded (Bool):** Choose — [helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception), and claimed as your dependent" = true → helper "Adjustments that exceed one academic period's expenses, where adjusted qualified education expenses are above zero"] [helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception), and claimed as your dependent" = false → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.edu_student",{"const":true}],"op":"test"},"then":"dependent.edu_over_if_adj"},{"guard":{"eq":["dependent.edu_student",{"const":false}],"op":"test"},"then":"dependent.edu_no"}],"op":"choose"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)

## 23 — `dependent.edu_line23`

- **Authored helper label:** Has the American opportunity credit been claimed for this student for any 4 prior tax years?
- **Encoded (Bool):** Input — Has the American opportunity credit been claimed (by you or anyone else) for this student for any 4 tax years before 2025?
- **Shown on the values sheet only when:** An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception), and claimed as your dependent (`dependent.edu_student`)
- Expr: `{"op":"input","source":"Has the American opportunity credit been claimed (by you or anyone else) for this student for any 4 tax years before 2025?"}`
- Cite: [f8863] p. 2, Part III, line 23, "Has the American opportunity credit been claimed for this student for any 4 prior tax years?"; i8863 p. 8, Line 23 (2025; sha256 a251a1cf)

## (helper) — `dependent.edu_show24`

- **Authored helper label:** Line 24 is reached (line 23 did not stop)
- **Encoded (Bool):** helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception), and claimed as your dependent" = true and line 23 = false
- Expr: `{"all":[{"eq":["dependent.edu_student",{"const":true}],"op":"test"},{"eq":["dependent.edu_line23",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [f8863] p. 2, Part III, line 23, "Yes—Stop! Go to line 31 for this student." (2025; sha256 a251a1cf)

## 24 — `dependent.edu_line24`

- **Authored helper label:** Was the student enrolled at least half-time for at least one academic period that began or is treated as having begun in 2025 at an eligible educational institution in a program leading toward a postsecondary degree, certificate, or other recognized postsecondary educational credential?
- **Encoded (Bool):** Input — Was the student enrolled at least half-time (Form 1098-T box 8) for at least one academic period that began in 2025, or in the first 3 months of 2026 if paid for in 2025, at an eligible educational institution, in a program leading toward a postsecondary degree, certificate or other recognized postsecondary educational credential?
- **Shown on the values sheet only when:** Line 24 is reached (line 23 did not stop) (`dependent.edu_show24`)
- Expr: `{"op":"input","source":"Was the student enrolled at least half-time (Form 1098-T box 8) for at least one academic period that began in 2025, or in the first 3 months of 2026 if paid for in 2025, at an eligible educational institution, in a program leading toward a postsecondary degree, certificate or other recognized postsecondary educational credential?"}`
- Cite: [f8863] p. 2, Part III, line 24, "Was the student enrolled at least half-time for at least one academic period that began or is treated as having begun in 2025 at an eligible educational institution in a program leading toward a postsecondary degree, certificate, or other recognized postsecondary educational credential?"; i8863 p. 8, Line 24 (2025; sha256 a251a1cf)

## (helper) — `dependent.edu_show25`

- **Authored helper label:** Line 25 is reached (line 24 did not stop)
- **Encoded (Bool):** helper "Line 24 is reached (line 23 did not stop)" = true and line 24 = true
- Expr: `{"all":[{"eq":["dependent.edu_show24",{"const":true}],"op":"test"},{"eq":["dependent.edu_line24",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [f8863] p. 2, Part III, line 24, "No—Stop! Go to line 31 for this student." (2025; sha256 a251a1cf)

## 25 — `dependent.edu_line25`

- **Authored helper label:** Did the student complete the first 4 years of postsecondary education before 2025?
- **Encoded (Bool):** Input — Did the student complete the first 4 years of postsecondary education before 2025, as determined by the institution (4 years of academic credit, not counting credit awarded solely for proficiency examinations)?
- **Shown on the values sheet only when:** Line 25 is reached (line 24 did not stop) (`dependent.edu_show25`)
- Expr: `{"op":"input","source":"Did the student complete the first 4 years of postsecondary education before 2025, as determined by the institution (4 years of academic credit, not counting credit awarded solely for proficiency examinations)?"}`
- Cite: [f8863] p. 2, Part III, line 25, "Did the student complete the first 4 years of postsecondary education before 2025?"; i8863 p. 8, Line 25 (2025; sha256 a251a1cf)

## (helper) — `dependent.edu_show26`

- **Authored helper label:** Line 26 is reached (line 25 did not stop)
- **Encoded (Bool):** helper "Line 25 is reached (line 24 did not stop)" = true and line 25 = false
- Expr: `{"all":[{"eq":["dependent.edu_show25",{"const":true}],"op":"test"},{"eq":["dependent.edu_line25",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [f8863] p. 2, Part III, line 25, "Yes—Stop! Go to line 31 for this student." (2025; sha256 a251a1cf)

## 26 — `dependent.edu_line26`

- **Authored helper label:** Was the student convicted, before the end of 2025, of a felony for possession or distribution of a controlled substance?
- **Encoded (Bool):** Input — Was the student convicted, before the end of 2025, of a federal or state felony for possession or distribution of a controlled substance?
- **Shown on the values sheet only when:** Line 26 is reached (line 25 did not stop) (`dependent.edu_show26`)
- Expr: `{"op":"input","source":"Was the student convicted, before the end of 2025, of a federal or state felony for possession or distribution of a controlled substance?"}`
- Cite: [f8863] p. 2, Part III, line 26, "Was the student convicted, before the end of 2025, of a felony for possession or distribution of a controlled substance?"; i8863 p. 8, Line 26 (2025; sha256 a251a1cf)

## (gate) — `dependent.edu_ein`

- **Authored helper label:** The institution's employer identification number (EIN) is available
- **Encoded (Bool):** Input — Do you have the educational institution's employer identification number (EIN), from Form 1098-T or from the institution?
- Expr: `{"op":"input","source":"Do you have the educational institution's employer identification number (EIN), from Form 1098-T or from the institution?"}`
- Cite: [i8863] p. 4, Student qualifications, "7. You must provide the educational institution’s employer identification number (EIN) on your Form 8863." (2025; sha256 195cfd5e)

## (helper) — `dependent.edu_no`

- **Authored helper label:** Year parameter edu.no (false)
- **Encoded (Bool):** Enter false (edu.no).
- Expr: `{"op":"param","ref":"edu.no"}`
- Cite: [f8863] p. 2, Part III, line 23, "Yes—Stop! Go to line 31 for this student." (2025; sha256 a251a1cf)

## (helper) — `dependent.edu_aoc`

- **Authored helper label:** An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available
- **Encoded (Bool):** Choose — [helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception), and claimed as your dependent" = true → helper "For an eligible student, line 23 is No (the American opportunity credit was not claimed for 4 prior tax years), and lines 24 to 26, the TINs and the EIN allow the credit"] [helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception), and claimed as your dependent" = false → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.edu_student",{"const":true}],"op":"test"},"then":"dependent.edu_aoc23"},{"guard":{"eq":["dependent.edu_student",{"const":false}],"op":"test"},"then":"dependent.edu_no"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 26, "No—Complete lines 27 through 30 for this student."; i8863 p. 3, Student qualifications, "5. Filers and students must have been issued a TIN by the due date of their 2025 return (including extensions)." (2025; sha256 a251a1cf)

## (helper) — `dependent.edu_aoc23`

- **Authored helper label:** For an eligible student, line 23 is No (the American opportunity credit was not claimed for 4 prior tax years), and lines 24 to 26, the TINs and the EIN allow the credit
- **Encoded (Bool):** Choose — [line 23 = false → helper "Line 24 is Yes (enrolled at least half-time), and lines 25 and 26, the TINs and the EIN allow the credit"] [line 23 = true → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.edu_line23",{"const":false}],"op":"test"},"then":"dependent.edu_aoc24"},{"guard":{"eq":["dependent.edu_line23",{"const":true}],"op":"test"},"then":"dependent.edu_no"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 23, "Yes—Stop! Go to line 31 for this student." (2025; sha256 a251a1cf)

## (helper) — `dependent.edu_aoc24`

- **Authored helper label:** Line 24 is Yes (enrolled at least half-time), and lines 25 and 26, the TINs and the EIN allow the credit
- **Encoded (Bool):** Choose — [line 24 = true → helper "Line 25 is No (the first 4 years of postsecondary education were not completed before 2025), and line 26, the TINs and the EIN allow the credit"] [line 24 = false → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.edu_line24",{"const":true}],"op":"test"},"then":"dependent.edu_aoc25"},{"guard":{"eq":["dependent.edu_line24",{"const":false}],"op":"test"},"then":"dependent.edu_no"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 24, "No—Stop! Go to line 31 for this student." (2025; sha256 a251a1cf)

## (helper) — `dependent.edu_aoc25`

- **Authored helper label:** Line 25 is No (the first 4 years of postsecondary education were not completed before 2025), and line 26, the TINs and the EIN allow the credit
- **Encoded (Bool):** Choose — [line 25 = false → helper "Line 26 is No (no felony drug conviction), and the TINs and the EIN allow the credit"] [line 25 = true → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.edu_line25",{"const":false}],"op":"test"},"then":"dependent.edu_aoc26"},{"guard":{"eq":["dependent.edu_line25",{"const":true}],"op":"test"},"then":"dependent.edu_no"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 25, "Yes—Stop! Go to line 31 for this student." (2025; sha256 a251a1cf)

## (helper) — `dependent.edu_aoc26`

- **Authored helper label:** Line 26 is No (no felony drug conviction), and the TINs and the EIN allow the credit
- **Encoded (Bool):** Choose — [line 26 = false → helper "You, and your spouse if filing jointly, have a TIN, and the institution's EIN is available"] [line 26 = true → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.edu_line26",{"const":false}],"op":"test"},"then":"dependent.edu_aoc_tin"},{"guard":{"eq":["dependent.edu_line26",{"const":true}],"op":"test"},"then":"dependent.edu_no"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 26, "No—Complete lines 27 through 30 for this student." (2025; sha256 a251a1cf)

## (helper) — `dependent.edu_aoc_tin`

- **Authored helper label:** You, and your spouse if filing jointly, have a TIN, and the institution's EIN is available
- **Encoded (Bool):** Choose — [household helper "You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN" = true → helper "The institution's employer identification number (EIN) is available"] [household helper "You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN" = false → helper "Year parameter edu.no (false)"]
- Interpretation: amb.2025.edu_filer_tin
- Expr: `{"alternatives":[{"guard":{"eq":["household.all_tin",{"const":true}],"op":"test"},"then":"dependent.edu_ein"},{"guard":{"eq":["household.all_tin",{"const":false}],"op":"test"},"then":"dependent.edu_no"}],"op":"choose"}`
- Cite: [i8863] p. 3, Student qualifications, "5. Filers and students must have been issued a TIN by the due date of their 2025 return (including extensions)." (2025; sha256 195cfd5e)

## (helper) — `dependent.edu_llc`

- **Authored helper label:** A lifetime learning credit student: an eligible student who is not an American opportunity credit student
- **Encoded (Bool):** helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception), and claimed as your dependent" = true and helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false
- Expr: `{"all":[{"eq":["dependent.edu_student",{"const":true}],"op":"test"},{"eq":["dependent.edu_aoc",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i8863] p. 4, Tip, "If the requirements above aren’t met for any student, you cannot claim the American opportunity credit for that student. You may be able to claim the lifetime learning credit for part or all of that student’s qualified education expenses instead if certain requirements are met." (2025; sha256 195cfd5e)

## (helper) — `dependent.edu_tin_issued`

- **Authored helper label:** The student's SSN, ITIN or ATIN was issued on or before the due date of your return
- **Encoded (Bool):** Input — Was this student's SSN, ITIN or ATIN issued on or before the due date of your 2025 return (including extensions)? Answer no if an ITIN or ATIN had only been applied for by then, even if it has been or will be issued later.
- Expr: `{"op":"input","source":"Was this student's SSN, ITIN or ATIN issued on or before the due date of your 2025 return (including extensions)? Answer no if an ITIN or ATIN had only been applied for by then, even if it has been or will be issued later."}`
- Cite: [i8863] p. 3, Who cannot claim a credit, "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)."; p. 3, Table 1, "Students must have been issued a TIN by the due date of their 2025 return (including extensions)" (2025; sha256 195cfd5e)

## (gate) — `dependent.edu_llc_tin_refused`

- **Authored helper label:** A lifetime learning credit student whose ITIN or ATIN was only applied for by the due date of the return
- **Encoded (Bool):** helper "A lifetime learning credit student: an eligible student who is not an American opportunity credit student" = true and helper "The student's SSN, ITIN or ATIN was issued on or before the due date of your return" = false
- Expr: `{"all":[{"eq":["dependent.edu_llc",{"const":true}],"op":"test"},{"eq":["dependent.edu_tin_issued",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i8863] p. 3, Who cannot claim a credit, "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)." (2025; sha256 195cfd5e)

## 27 — `dependent.edu_line27`

- **Authored helper label:** Adjusted qualified education expenses. Don't enter more than $4,000
- **Encoded (NonNegDollars):** Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line27" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → helper "No amount for this person"]
- **Refusal:** when dependent.edu_over_refused is true, cannot complete Adjusted Qualified Education Expenses Worksheet for more than one academic period. The worksheet is completed for each academic period, and an academic period whose tax-free educational assistance and refunds exceed its own expenses cannot be netted against another period's expenses. Figure the worksheet period by period. Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)
- **Shown on the values sheet only when:** An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available (`dependent.edu_aoc`)
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.edu_aoc",{"const":true}],"op":"test"},"then":{"bind":{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"},"def":"aqee","line":"line27"}},{"guard":{"eq":["dependent.edu_aoc",{"const":false}],"op":"test"},"then":"dependent.zero"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 27, "Adjusted qualified education expenses (see instructions). Don’t enter more than $4,000"; i8863 p. 9, Line 27 (2025; sha256 a251a1cf)

## 28 — `dependent.edu_line28`

- **Authored helper label:** Subtract $2,000 from line 27. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line28" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → helper "No amount for this person"]
- **Refusal:** when dependent.edu_over_refused is true, cannot complete Adjusted Qualified Education Expenses Worksheet for more than one academic period. The worksheet is completed for each academic period, and an academic period whose tax-free educational assistance and refunds exceed its own expenses cannot be netted against another period's expenses. Figure the worksheet period by period. Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)
- **Shown on the values sheet only when:** An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available (`dependent.edu_aoc`)
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.edu_aoc",{"const":true}],"op":"test"},"then":{"bind":{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"},"def":"aqee","line":"line28"}},{"guard":{"eq":["dependent.edu_aoc",{"const":false}],"op":"test"},"then":"dependent.zero"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 28, "Subtract $2,000 from line 27. If zero or less, enter -0-" (2025; sha256 a251a1cf)

## 29 — `dependent.edu_line29`

- **Authored helper label:** Multiply line 28 by 25% (0.25)
- **Encoded (NonNegDollars):** Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line29" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → helper "No amount for this person"]
- **Refusal:** when dependent.edu_over_refused is true, cannot complete Adjusted Qualified Education Expenses Worksheet for more than one academic period. The worksheet is completed for each academic period, and an academic period whose tax-free educational assistance and refunds exceed its own expenses cannot be netted against another period's expenses. Figure the worksheet period by period. Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)
- **Shown on the values sheet only when:** An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available (`dependent.edu_aoc`)
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.edu_aoc",{"const":true}],"op":"test"},"then":{"bind":{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"},"def":"aqee","line":"line29"}},{"guard":{"eq":["dependent.edu_aoc",{"const":false}],"op":"test"},"then":"dependent.zero"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 29, "Multiply line 28 by 25% (0.25)" (2025; sha256 a251a1cf)

## 30 — `dependent.edu_line30`

- **Authored helper label:** American opportunity credit for this student. If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on line 29
- **Encoded (NonNegDollars):** Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line30" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → helper "No amount for this person"]
- **Refusal:** when dependent.edu_over_refused is true, cannot complete Adjusted Qualified Education Expenses Worksheet for more than one academic period. The worksheet is completed for each academic period, and an academic period whose tax-free educational assistance and refunds exceed its own expenses cannot be netted against another period's expenses. Figure the worksheet period by period. Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)
- **Shown on the values sheet only when:** An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available (`dependent.edu_aoc`)
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.edu_aoc",{"const":true}],"op":"test"},"then":{"bind":{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.edu_mat"},"def":"aqee","line":"line30"}},{"guard":{"eq":["dependent.edu_aoc",{"const":false}],"op":"test"},"then":"dependent.zero"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 30, "If line 28 is zero, enter the amount from line 27.", "Include the total of all amounts from all Parts III, line 30, on Part I, line 1" (2025; sha256 a251a1cf)

## 31 — `dependent.edu_line31`

- **Authored helper label:** Adjusted qualified education expenses for the lifetime learning credit
- **Encoded (NonNegDollars):** Choose — [helper "A lifetime learning credit student: an eligible student who is not an American opportunity credit student" = true → "ws4_llc" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "No amount for this person"] [helper "A lifetime learning credit student: an eligible student who is not an American opportunity credit student" = false → helper "No amount for this person"]
- **Refusal:** when dependent.edu_llc_tin_refused is true, cannot complete Lifetime learning credit for a student whose ITIN or ATIN was only applied for. The lifetime learning credit requires the student to have been issued a TIN by the due date of the return (including extensions); an ITIN or ATIN only applied for by then counts as issued for the American opportunity credit only. This tool does not prepare the return without the lifetime learning credit for this student. Cite: [i8863] p. 3, Who cannot claim a credit, "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)."; p970 p. 11, "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as is- sued on or before the due date of the return." (2025; sha256 195cfd5e)
- **Refusal:** when dependent.edu_over_refused is true, cannot complete Adjusted Qualified Education Expenses Worksheet for more than one academic period. The worksheet is completed for each academic period, and an academic period whose tax-free educational assistance and refunds exceed its own expenses cannot be netted against another period's expenses. Figure the worksheet period by period. Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)
- **Shown on the values sheet only when:** A lifetime learning credit student: an eligible student who is not an American opportunity credit student (`dependent.edu_llc`)
- Expr: `{"alternatives":[{"guard":{"eq":["dependent.edu_llc",{"const":true}],"op":"test"},"then":{"bind":{"adj":"dependent.edu_adj","inst":"dependent.edu_inst","mat":"dependent.zero"},"def":"aqee","line":"ws4_llc"}},{"guard":{"eq":["dependent.edu_llc",{"const":false}],"op":"test"},"then":"dependent.zero"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 31, "Adjusted qualified education expenses (see instructions). Include the total of all amounts from all Parts III, line 31, on Part II, line 10"; i8863 p. 9, Line 31 (2025; sha256 a251a1cf)
