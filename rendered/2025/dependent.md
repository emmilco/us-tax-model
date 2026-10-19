# Dependents — qualifying child and qualifying relative tests, per person listed

- Document: `dependent` (worksheet, tax year 2025)
- Collection: keyed entries; [f1040] Form 1040 (2025), Dependents, rows (1)–(7) (2025; created 2025-09-05; sha256 3d31c226)
- Note: One entry per person the filer lists. The tests of Steps 1 through 5 of "Who Qualifies as Your Dependent" are encoded per entry; the rules for married persons, children of divorced or separated parents, multiple support agreements and a child who is the qualifying child of another person are refused rather than decided. Temporary absences count as months lived with you, as the instructions say.

## (helper) — `dependent.relationship`

- **Authored helper label:** Relationship to you
- **Encoded (Enum(dependent_relationship)):** Input — Relationship to you: child (son, daughter, stepchild, foster child or their descendant), sibling (brother, sister, half brother, half sister, stepbrother or stepsister, or a son or daughter of a brother, sister, half brother or half sister), sibling_descendant (any other descendant of a sibling, such as a grandniece or a stepsibling's child), parent (father or mother), parent_relative (a grandparent, aunt or uncle: an ancestor or sibling of a parent), in_law (step-parent or in-law), household_member (any other person, other than your spouse, who lived with you all year as a member of your household, if your relationship did not violate local law), or other (any other relationship; such a person is a Step 4 relative only if they lived with you all year as a member of your household and the relationship did not violate local law)
- Expr: `{"op":"input","source":"Relationship to you: child (son, daughter, stepchild, foster child or their descendant), sibling (brother, sister, half brother, half sister, stepbrother or stepsister, or a son or daughter of a brother, sister, half brother or half sister), sibling_descendant (any other descendant of a sibling, such as a grandniece or a stepsibling's child), parent (father or mother), parent_relative (a grandparent, aunt or uncle: an ancestor or sibling of a parent), in_law (step-parent or in-law), household_member (any other person, other than your spouse, who lived with you all year as a member of your household, if your relationship did not violate local law), or other (any other relationship; such a person is a Step 4 relative only if they lived with you all year as a member of your household and the relationship did not violate local law)"}`
- Cite: [i1040gi] pp. 17 and 19, Steps 1 and 4, "A qualifying child is your..." and "A qualifying relative is your..." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.age`

- **Authored helper label:** Age at the end of 2025
- **Encoded (Count):** Input — Age at the end of 2025 (whole years)
- Expr: `{"op":"input","source":"Age at the end of 2025 (whole years)"}`
- Cite: [i1040gi] p. 17, Step 1, "Under age 19 at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.student`

- **Authored helper label:** Full-time student in 2025?
- **Encoded (Bool):** Input — Was this person a full-time student in 2025?
- Expr: `{"op":"input","source":"Was this person a full-time student in 2025?"}`
- Cite: [i1040gi] p. 17, Step 1, "Under age 24 at the end of 2025, a full-time student (defined later)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.disabled`

- **Authored helper label:** Permanently and totally disabled?
- **Encoded (Bool):** Input — Was this person permanently and totally disabled at any time in 2025?
- Expr: `{"op":"input","source":"Was this person permanently and totally disabled at any time in 2025?"}`
- Cite: [i1040gi] p. 17, Step 1, "Any age and permanently and totally disabled (defined later)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.months`

- **Authored helper label:** Months lived with you in 2025, counting temporary absences
- **Encoded (Count):** Input — Months this person lived with you in 2025, counting temporary absences for school, vacation, business, medical care, military service or detention in a juvenile facility as time lived with you (0–12); enter 7 if the person lived with you for more than half of 2025 but fewer than 7 full months. For a person born, died, adopted or placed with you in 2025 who meets the other conditions to be your qualifying child, enter 12 if your home was their home for more than half the time they were alive or with you, and 0 otherwise; for any other person born or who died in 2025, or adopted, lawfully placed with you for legal adoption, or placed with you as an eligible foster child in 2025, enter 12 only if your home was their home for the entire time they were alive or since the adoption or placement, and 0 otherwise
- Expr: `{"op":"input","source":"Months this person lived with you in 2025, counting temporary absences for school, vacation, business, medical care, military service or detention in a juvenile facility as time lived with you (0–12); enter 7 if the person lived with you for more than half of 2025 but fewer than 7 full months. For a person born, died, adopted or placed with you in 2025 who meets the other conditions to be your qualifying child, enter 12 if your home was their home for more than half the time they were alive or with you, and 0 otherwise; for any other person born or who died in 2025, or adopted, lawfully placed with you for legal adoption, or placed with you as an eligible foster child in 2025, enter 12 only if your home was their home for the entire time they were alive or since the adoption or placement, and 0 otherwise"}`
- Cite: [i1040gi] p. 17, Step 1, "Who lived with you for more than half of 2025", and p. 21, Exception to time lived with you ("the child ... for more than half the part of the year the child was alive"; "Any other person is considered to have lived with you for all of 2025 if the person was born or died in 2025 and your home was this person's home for the entire time the person was alive in 2025") (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.self_support`

- **Authored helper label:** Provided over half of their own support?
- **Encoded (Bool):** Input — Did this person provide over half of their own support for 2025?
- Expr: `{"op":"input","source":"Did this person provide over half of their own support for 2025?"}`
- Cite: [i1040gi] p. 17, Step 1, "Who didn't provide over half of their own support for 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.joint_return`

- **Authored helper label:** Filing a joint return other than only to claim a refund?
- **Encoded (Bool):** Input — Is this person filing a joint return for 2025, other than only to claim a refund of withheld or estimated tax?
- Expr: `{"op":"input","source":"Is this person filing a joint return for 2025, other than only to claim a refund of withheld or estimated tax?"}`
- Cite: [i1040gi] p. 17, Step 1, "Who isn't filing a joint return for 2025 or is filing a joint return for 2025 only to claim a refund" (2025; printed date 2026-02-25; sha256 482e9c48)

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

- **Authored helper label:** Married?
- **Encoded (Bool):** Input — Was this person married at the end of 2025 (a person legally separated under a decree of divorce or separate maintenance is not married), or is this person filing a joint return for 2025 (for example with a spouse who died during 2025)?
- Expr: `{"op":"input","source":"Was this person married at the end of 2025 (a person legally separated under a decree of divorce or separate maintenance is not married), or is this person filing a joint return for 2025 (for example with a spouse who died during 2025)?"}`
- Cite: [i1040gi] p. 18, Step 2, question 2, "Was the child married? Yes. See Married person, later" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.tin`

- **Authored helper label:** SSN, ITIN or ATIN issued on or before the due date of your return?
- **Encoded (Bool):** Input — Did this person have an SSN, ITIN or ATIN issued on or before the due date of your 2025 return (including extensions), or have you applied for an ITIN or ATIN for this person by then?
- Expr: `{"op":"input","source":"Did this person have an SSN, ITIN or ATIN issued on or before the due date of your 2025 return (including extensions), or have you applied for an ITIN or ATIN for this person by then?"}`
- Cite: [i1040gi] p. 18, Step 3, question 1, and p. 19, Step 5, question 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.work_ssn`

- **Authored helper label:** SSN valid for employment issued before the due date of your return?
- **Encoded (Bool):** Input — Did this person have an SSN valid for employment, issued before the due date of your 2025 return (including extensions)?
- Expr: `{"op":"input","source":"Did this person have an SSN valid for employment, issued before the due date of your 2025 return (including extensions)?"}`
- Cite: [i1040gi] p. 18, Step 3, question 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.gross_income`

- **Authored helper label:** Gross income for 2025
- **Encoded (NonNegDollars):** Input — This person's gross income for 2025
- Expr: `{"op":"input","source":"This person's gross income for 2025"}`
- Cite: [i1040gi] p. 19, Step 4, "Who had gross income of less than $5,200 in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.supported`

- **Authored helper label:** You provided over half of this person's support?
- **Encoded (Bool):** Input — Did you provide over half of this person's support in 2025?
- Expr: `{"op":"input","source":"Did you provide over half of this person's support in 2025?"}`
- Cite: [i1040gi] p. 19, Step 4, "For whom you provided over half of the person's support in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.other_claimant`

- **Authored helper label:** Meets the conditions to be the qualifying child of another person?
- **Encoded (Bool):** Input — Does this person meet the conditions to be the qualifying child of any other person for 2025, under the dependent rules or under the EIC rules (which have no support test)?
- Expr: `{"op":"input","source":"Does this person meet the conditions to be the qualifying child of any other person for 2025, under the dependent rules or under the EIC rules (which have no support test)?"}`
- Cite: [i1040gi] p. 17, Step 1, "If the child meets the conditions to be a qualifying child of any other person ... see Qualifying child of more than one person" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.divorced_rule`

- **Authored helper label:** Rule for children of divorced or separated parents applies?
- **Encoded (Bool):** Input — Does the special rule for children of divorced or separated parents, or parents who lived apart (including parents who never married), apply to this person, for example because a Form 8332 release or a decree lets the noncustodial parent claim the child?
- Expr: `{"op":"input","source":"Does the special rule for children of divorced or separated parents, or parents who lived apart (including parents who never married), apply to this person, for example because a Form 8332 release or a decree lets the noncustodial parent claim the child?"}`
- Cite: [i1040gi] p. 19, Step 4, "But see Children of divorced or separated parents" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.multiple_support`

- **Authored helper label:** Claimed under a multiple support agreement?
- **Encoded (Bool):** Input — Did you and others together provide over half of this person's support for 2025, with no one person providing over half (a multiple support situation), whether you or another contributor claims the person?
- Expr: `{"op":"input","source":"Did you and others together provide over half of this person's support for 2025, with no one person providing over half (a multiple support situation), whether you or another contributor claims the person?"}`
- Cite: [i1040gi] p. 19, Step 4, "Multiple support agreements" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.parent_home_paid`

- **Authored helper label:** For a parent not living with you, you paid over half the cost of their main home for all of 2025?
- **Encoded (Bool):** Input — If this person is your parent, did you pay over half the cost of keeping up a home that was their main home for all of 2025?
- Expr: `{"op":"input","source":"If this person is your parent, did you pay over half the cost of keeping up a home that was their main home for all of 2025?"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 1 (2025; printed date 2026-02-25; sha256 482e9c48)

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

- **Authored helper label:** Younger than you?
- **Encoded (Bool):** Input — Was this person younger than you?
- Expr: `{"op":"input","source":"Was this person younger than you?"}`
- Cite: [i1040gi] p. 17, Step 1, "and younger than you (or your spouse if filing jointly)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.us_half`

- **Authored helper label:** Lived with you in the United States for more than half of 2025?
- **Encoded (Bool):** Input — Did this person live with you in the United States (the 50 states and the District of Columbia) for more than half of 2025? If you were on extended active military duty outside the United States, your main home is considered to be in the United States during that duty. Temporary absences for school, vacation, business, medical care, military service or juvenile detention count as time lived with you. A child born or who died in 2025 counts if your home was the child's home for more than half the time the child was alive, and a child you adopted, who was lawfully placed with you for legal adoption, or who was placed with you as an eligible foster child in 2025 counts if your main home was the child's main home for more than half the time since the adoption or placement.
- Expr: `{"op":"input","source":"Did this person live with you in the United States (the 50 states and the District of Columbia) for more than half of 2025? If you were on extended active military duty outside the United States, your main home is considered to be in the United States during that duty. Temporary absences for school, vacation, business, medical care, military service or juvenile detention count as time lived with you. A child born or who died in 2025 counts if your home was the child's home for more than half the time the child was alive, and a child you adopted, who was lawfully placed with you for legal adoption, or who was placed with you as an eligible foster child in 2025 counts if your main home was the child's main home for more than half the time since the adoption or placement."}`
- Cite: [i1040gi] p. 41, Step 3, "Who lived with you in the United States for more than half of 2025"; p. 43, Exception to time lived with you; p. 44, Members of the military; p. 45, United States (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.eic_ssn`

- **Authored helper label:** SSN valid for the EIC, issued on or before the due date of your return?
- **Encoded (Bool):** Input — Did this person have a social security number issued on or before the due date of your 2025 return (including extensions) that is valid for the EIC? Any number issued by the Social Security Administration is valid unless the card says "Not Valid for Employment" and the number was issued solely to apply for or receive a federally funded benefit; a card that says "Valid for Work Only With DHS Authorization" is valid only while the authorization is valid.
- Expr: `{"op":"input","source":"Did this person have a social security number issued on or before the due date of your 2025 return (including extensions) that is valid for the EIC? Any number issued by the Social Security Administration is valid unless the card says \"Not Valid for Employment\" and the number was issued solely to apply for or receive a federally funded benefit; a card that says \"Valid for Work Only With DHS Authorization\" is valid only while the authorization is valid."}`
- Cite: [i1040gi] pp. 44–45, Social security number (SSN), EIC (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qc_age`

- **Authored helper label:** Under 19 and younger than you, under 24 a full-time student and younger than you, or permanently and totally disabled
- **Encoded (Bool):** (helper "Age at the end of 2025" < 19 (qc.age_limit) and helper "Younger than you?" = true or helper "Age at the end of 2025" < 24 (qc.student_age_limit) and helper "Full-time student in 2025?" = true and helper "Younger than you?" = true or helper "Permanently and totally disabled?" = true)
- Expr: `{"any":[{"all":[{"lt":["dependent.age",{"param":"qc.age_limit"}],"op":"test"},{"eq":["dependent.younger",{"const":true}],"op":"test"}],"op":"test"},{"all":[{"lt":["dependent.age",{"param":"qc.student_age_limit"}],"op":"test"},{"eq":["dependent.student",{"const":true}],"op":"test"},{"eq":["dependent.younger",{"const":true}],"op":"test"}],"op":"test"},{"eq":["dependent.disabled",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 17, Step 1, the age conditions (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.lived_half`

- **Authored helper label:** Lived with you for more than half of 2025
- **Encoded (Bool):** helper "Months lived with you in 2025, counting temporary absences" > 6 (a count)
- Expr: `{"gt":["dependent.months",{"const":6,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 17, Step 1, "Who lived with you for more than half of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qualifying_child`

- **Authored helper label:** Qualifying child (Step 1)
- **Encoded (Bool):** helper "A child, sibling, or a descendant of either" = true and helper "Under 19 and younger than you, under 24 a full-time student and younger than you, or permanently and totally disabled" = true and helper "Provided over half of their own support?" = false and helper "Filing a joint return other than only to claim a refund?" = false and helper "Lived with you for more than half of 2025" = true
- **Refusal:** when dependent.other_claimant is true, cannot complete Qualifying child of more than one person (tie-breaker rules). This person may be the qualifying child of another person. The tie-breaker rules are outside this tool. Cite: [i1040gi] p. 21, Qualifying child of more than one person (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when dependent.divorced_rule is true, cannot complete Children of divorced or separated parents. The rule for children of divorced or separated parents is outside this tool. Cite: [i1040gi] p. 20, Children of divorced or separated parents (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when dependent.married is true, cannot complete Married person rules. A married dependent is outside this tool; see Married person in the instructions. Cite: [i1040gi] p. 21, Married person (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"all":[{"eq":["dependent.qc_relationship",{"const":true}],"op":"test"},{"eq":["dependent.qc_age",{"const":true}],"op":"test"},{"eq":["dependent.self_support",{"const":false}],"op":"test"},{"eq":["dependent.joint_return",{"const":false}],"op":"test"},{"eq":["dependent.lived_half",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 17, Step 1, "Do you have a child who meets the conditions to be your qualifying child?" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.resident`

- **Authored helper label:** U.S. citizen, national or resident alien, or a resident of Canada or Mexico
- **Encoded (Bool):** (helper "U.S. citizen, U.S. national or U.S. resident alien?" = true or helper "Resident of Canada or Mexico (if not a U.S. citizen, national or resident alien)?" = true)
- Expr: `{"any":[{"eq":["dependent.citizen",{"const":true}],"op":"test"},{"eq":["dependent.canada_mexico",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 18, Step 2, question 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qc_dependent`

- **Authored helper label:** Qualifying child who is your dependent (Step 2)
- **Encoded (Bool):** helper "Qualifying child (Step 1)" = true and helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = true and sa helper "Can someone claim you or your spouse as a dependent for 2025, or are you a dual-status alien? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)" = false
- Expr: `{"all":[{"eq":["dependent.qualifying_child",{"const":true}],"op":"test"},{"eq":["dependent.resident",{"const":true}],"op":"test"},{"eq":["sa.dependent",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 18, Step 2, questions 1 and 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qr_relationship`

- **Authored helper label:** A relative listed in Step 4, or any other person who lived with you all year
- **Encoded (Bool):** (helper "Relationship to you" = 'child' or helper "Relationship to you" = 'sibling' or helper "Relationship to you" = 'parent' or helper "Relationship to you" = 'parent_relative' or helper "Relationship to you" = 'in_law' or (helper "Relationship to you" = 'household_member' or helper "Relationship to you" = 'sibling_descendant' or helper "Relationship to you" = 'other') and helper "Months lived with you in 2025, counting temporary absences" = 12 (a count))
- Expr: `{"any":[{"eq":["dependent.relationship",{"const":"child"}],"op":"test"},{"eq":["dependent.relationship",{"const":"sibling"}],"op":"test"},{"eq":["dependent.relationship",{"const":"parent"}],"op":"test"},{"eq":["dependent.relationship",{"const":"parent_relative"}],"op":"test"},{"eq":["dependent.relationship",{"const":"in_law"}],"op":"test"},{"all":[{"any":[{"eq":["dependent.relationship",{"const":"household_member"}],"op":"test"},{"eq":["dependent.relationship",{"const":"sibling_descendant"}],"op":"test"},{"eq":["dependent.relationship",{"const":"other"}],"op":"test"}],"op":"test"},{"eq":["dependent.months",{"const":12,"type":"Count"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 19, Step 4, "A qualifying relative is your..." through "Any other person (other than your spouse) who lived with you all year as a member of your household" (2025; printed date 2026-02-25; sha256 482e9c48)

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

## (helper) — `dependent.qualifying_relative`

- **Authored helper label:** Qualifying relative (Step 4)
- **Encoded (Bool):** helper "A relative listed in Step 4, or any other person who lived with you all year" = true and helper "Qualifying child (Step 1)" = false and helper "Gross income under $5,200" = true and helper "You provided over half of this person's support?" = true
- **Refusal:** when dependent.multiple_support is true, cannot complete Multiple support agreements. A person claimed under a multiple support agreement is outside this tool. Cite: [i1040gi] p. 20, Multiple support agreements (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when dependent.income_exception is true, cannot complete Exception to gross income test. The sheltered-workshop exception to the gross income test for a disabled person is outside this tool. Cite: [i1040gi] pp. 19–20, Exception to gross income test (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when dependent.married is true, cannot complete Married person rules. A married dependent is outside this tool; see Married person in the instructions. Cite: [i1040gi] p. 21, Married person (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"all":[{"eq":["dependent.qr_relationship",{"const":true}],"op":"test"},{"eq":["dependent.qualifying_child",{"const":false}],"op":"test"},{"eq":["dependent.qr_income",{"const":true}],"op":"test"},{"eq":["dependent.supported",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 19, Step 4, "Does any person meet the conditions to be your qualifying relative?" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.qr_dependent`

- **Authored helper label:** Qualifying relative who is your dependent (Step 4, questions 2 and 5)
- **Encoded (Bool):** helper "Qualifying relative (Step 4)" = true and helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = true and sa helper "Can someone claim you or your spouse as a dependent for 2025, or are you a dual-status alien? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)" = false
- Expr: `{"all":[{"eq":["dependent.qualifying_relative",{"const":true}],"op":"test"},{"eq":["dependent.resident",{"const":true}],"op":"test"},{"eq":["sa.dependent",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 19, Step 4, questions 2 and 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.claimed`

- **Authored helper label:** Your dependent
- **Encoded (Bool):** (helper "Qualifying child who is your dependent (Step 2)" = true or helper "Qualifying relative who is your dependent (Step 4, questions 2 and 5)" = true)
- Expr: `{"any":[{"eq":["dependent.qc_dependent",{"const":true}],"op":"test"},{"eq":["dependent.qr_dependent",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] pp. 17–19, Who Qualifies as Your Dependent (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.under_ctc_age`

- **Authored helper label:** Under age 17 at the end of 2025
- **Encoded (Bool):** helper "Age at the end of 2025" < 17 (ctc.age_limit)
- Expr: `{"lt":["dependent.age",{"param":"ctc.age_limit"}],"op":"test"}`
- Cite: [i1040gi] p. 18, Step 3, question 3 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.ctc_child`

- **Authored helper label:** Qualifying child for the child tax credit (Step 3)
- **Encoded (Bool):** helper "Qualifying child who is your dependent (Step 2)" = true and helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = true and helper "U.S. citizen, U.S. national or U.S. resident alien?" = true and helper "Under age 17 at the end of 2025" = true and helper "SSN valid for employment issued before the due date of your return?" = true and household helper "Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid for employment, and each other person on the return has an SSN or ITIN" = true
- Expr: `{"all":[{"eq":["dependent.qc_dependent",{"const":true}],"op":"test"},{"eq":["dependent.tin",{"const":true}],"op":"test"},{"eq":["dependent.citizen",{"const":true}],"op":"test"},{"eq":["dependent.under_ctc_age",{"const":true}],"op":"test"},{"eq":["dependent.work_ssn",{"const":true}],"op":"test"},{"eq":["household.ctc_ssn",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 18, Step 3, questions 1–4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.odc_person`

- **Authored helper label:** Dependent for the credit for other dependents (Steps 3 and 5)
- **Encoded (Bool):** helper "Your dependent" = true and helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = true and helper "U.S. citizen, U.S. national or U.S. resident alien?" = true and helper "Qualifying child for the child tax credit (Step 3)" = false and household helper "You, and your spouse if filing jointly, have an SSN or ITIN" = true
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
- Cite: [f1040s8812] Schedule 8812 (2025), line 16b, "Number of qualifying children under age 17 with the required social security number x $1,700" (2025; created 2025-07-30; sha256 6936462d)

## (helper) — `dependent.hoh_test2`

- **Authored helper label:** A Test 2 person who lived with you more than half the year (the home-cost condition of Test 2 is tested on the household form)
- **Encoded (Bool):** (helper "Your dependent" = true and helper "Lived with you for more than half of 2025" = true and helper "Relationship to you" ≠ 'household_member' and helper "Relationship to you" ≠ 'sibling_descendant' and helper "Relationship to you" ≠ 'other' or helper "Qualifying child (Step 1)" = true and helper "Married?" = false and helper "Lived with you for more than half of 2025" = true)
- Expr: `{"any":[{"all":[{"eq":["dependent.claimed",{"const":true}],"op":"test"},{"eq":["dependent.lived_half",{"const":true}],"op":"test"},{"ne":["dependent.relationship",{"const":"household_member"}],"op":"test"},{"ne":["dependent.relationship",{"const":"sibling_descendant"}],"op":"test"},{"ne":["dependent.relationship",{"const":"other"}],"op":"test"}],"op":"test"},{"all":[{"eq":["dependent.qualifying_child",{"const":true}],"op":"test"},{"eq":["dependent.married",{"const":false}],"op":"test"},{"eq":["dependent.lived_half",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2 (a dependent, other than one who is your dependent only because they lived with you all year, which is any person claimed through the last Step 4 bullet, or your unmarried qualifying child, who lived with you more than half the year) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.hoh_test1`

- **Authored helper label:** Qualifies you for head of household under Test 1 through a parent who does not live with you (a parent who lives with you qualifies you through Test 2)
- **Encoded (Bool):** helper "Relationship to you" = 'parent' and helper "Your dependent" = true and helper "For a parent not living with you, you paid over half the cost of their main home for all of 2025?" = true
- Expr: `{"all":[{"eq":["dependent.relationship",{"const":"parent"}],"op":"test"},{"eq":["dependent.claimed",{"const":true}],"op":"test"},{"eq":["dependent.parent_home_paid",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 1, "You paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent whom you can claim as a dependent" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.eic_child`

- **Authored helper label:** Qualifying child for the EIC (relationship, age, not filing a joint return, lived with you in the United States for more than half of 2025)
- **Encoded (Bool):** helper "A child, sibling, or a descendant of either" = true and helper "Under 19 and younger than you, under 24 a full-time student and younger than you, or permanently and totally disabled" = true and helper "Filing a joint return other than only to claim a refund?" = false and helper "Lived with you in the United States for more than half of 2025?" = true
- **Refusal:** when dependent.other_claimant is true, cannot complete Qualifying child of more than one person (EIC). The tie-breaker rules for a child who is the qualifying child of more than one person are outside this tool. Cite: [i1040gi] p. 44, Qualifying child of more than one person (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when dependent.married is true, cannot complete Married child (EIC). A married child is a qualifying child for the EIC only under the dependency rules, which are outside this tool for a married person. Cite: [i1040gi] p. 44, Married child (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"all":[{"eq":["dependent.qc_relationship",{"const":true}],"op":"test"},{"eq":["dependent.qc_age",{"const":true}],"op":"test"},{"eq":["dependent.joint_return",{"const":false}],"op":"test"},{"eq":["dependent.us_half",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 41, Step 3, "A qualifying child for the EIC is your..." (relationship AND age AND not filing a joint return AND lived with you in the United States for more than half of 2025) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.eic_ssn_child`

- **Authored helper label:** Qualifying child for the EIC who has a valid SSN
- **Encoded (Bool):** helper "Qualifying child for the EIC (relationship, age, not filing a joint return, lived with you in the United States for more than half of 2025)" = true and helper "SSN valid for the EIC, issued on or before the due date of your return?" = true
- Expr: `{"all":[{"eq":["dependent.eic_child",{"const":true}],"op":"test"},{"eq":["dependent.eic_ssn",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 46, Worksheet A, line 2, "the number of qualifying children you have who have valid SSNs"; pp. 44–45, Social security number (SSN), "For the EIC, a valid SSN is a number issued by the Social Security Administration unless 'Not Valid for Employment' is printed on the social security card" (2025; printed date 2026-02-25; sha256 482e9c48)
