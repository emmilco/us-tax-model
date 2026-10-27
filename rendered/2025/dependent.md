# Dependents — qualifying child and qualifying relative tests, per person listed

- Document: `dependent` (worksheet, tax year 2025)
- Collection: keyed entries; [f1040] Form 1040 (2025), Dependents, rows (1)–(7) (2025; created 2025-09-05; sha256 3d31c226)
- Note: One entry per person the filer lists. The tests of Steps 1 through 5 of "Who Qualifies as Your Dependent" are encoded per entry; the rules for married persons, children of divorced or separated parents, multiple support agreements and a child who is the qualifying child of another person are refused rather than decided. Temporary absences count as months lived with you, as the instructions say.

## (helper) — `dependent.relationship`

- **Authored helper label:** Relationship to you
- **Encoded (Enum(dependent_relationship)):** Input — Relationship to you: child (son, daughter, stepchild, foster child or their descendant), sibling (brother, sister, half brother, half sister, stepbrother or stepsister, or a son or daughter of a brother, sister, half brother or half sister), sibling_descendant (any other descendant of a sibling, such as a grandniece or a stepsibling's child), parent (father or mother; not a foster parent, who is entered as other), parent_relative (a grandparent, aunt or uncle: an ancestor or sibling of a parent), in_law (step-parent or in-law), household_member (any other person, other than your spouse, who lived with you all year as a member of your household, if your relationship did not violate local law), or other (any other relationship; such a person is a Step 4 relative only if they lived with you all year as a member of your household and the relationship did not violate local law)
- Interpretation: amb.2025.foster_parent_relationship
- Expr: `{"op":"input","source":"Relationship to you: child (son, daughter, stepchild, foster child or their descendant), sibling (brother, sister, half brother, half sister, stepbrother or stepsister, or a son or daughter of a brother, sister, half brother or half sister), sibling_descendant (any other descendant of a sibling, such as a grandniece or a stepsibling's child), parent (father or mother; not a foster parent, who is entered as other), parent_relative (a grandparent, aunt or uncle: an ancestor or sibling of a parent), in_law (step-parent or in-law), household_member (any other person, other than your spouse, who lived with you all year as a member of your household, if your relationship did not violate local law), or other (any other relationship; such a person is a Step 4 relative only if they lived with you all year as a member of your household and the relationship did not violate local law)"}`
- Cite: [i1040gi] pp. 17 and 19, Steps 1 and 4, "A qualifying child is your..." and "A qualifying relative is your..."; p501 p. 19, Relatives who don't have to live with you, "Your father, mother, grandparent, or other direct ancestor, but not foster parent" (2025; printed date 2026-02-25; sha256 482e9c48)

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
- Cite: [i1040gi] p. 17, Step 1, "Who lived with you for more than half of 2025"; p. 21, Exception to time lived with you ("the person is considered to have lived with you for more than half of 2025 if your home was this person's home for more than half the time the person was alive in 2025"; "Any other person is considered to have lived with you for all of 2025 if the person was born or died in 2025 and your home was this person's home for the entire time the person was alive in 2025") (2025; printed date 2026-02-25; sha256 482e9c48)

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

- **Authored helper label:** For a parent not living with you, you paid over half the cost of their main home for all of 2025 (or the part of 2025 they were alive)?
- **Encoded (Bool):** Input — If this person is your parent, did you pay over half the cost of keeping up a home that was their main home for all of 2025 (or, if your parent died in 2025, for the entire part of 2025 your parent was alive)?
- Expr: `{"op":"input","source":"If this person is your parent, did you pay over half the cost of keeping up a home that was their main home for all of 2025 (or, if your parent died in 2025, for the entire part of 2025 your parent was alive)?"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 1; p. 15, "If the person is anyone else, see Pub. 501"; p501 p. 9, Death or birth, "Your parent for whom you paid, for the entire part of the year your parent was alive, more than half the cost of keeping up the home your parent lived in" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.born_died`

- **Authored helper label:** Born or died in 2025?
- **Encoded (Bool):** Input — Was this person born in 2025, or did this person die in 2025?
- Expr: `{"op":"input","source":"Was this person born in 2025, or did this person die in 2025?"}`
- Cite: [i1040gi] p. 15, "If the person for whom you kept up a home was born or died in 2025, you still may be able to file as head of household" (2025; printed date 2026-02-25; sha256 482e9c48)

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

## (helper) — `dependent.hoh_lived_half`

- **Authored helper label:** Lived with you more than half of 2025, or, for a relative other than a qualifying child (whose months already count the part of the year), more than half of the part of 2025 they were alive or since their adoption or placement
- **Encoded (Bool):** (helper "Lived with you for more than half of 2025" = true or helper "Qualifying child (Step 1)" = false and (helper "Born or died in 2025?" = true or helper "Adopted, placed for adoption or placed as a foster child in 2025?" = true) and helper "Lived with you more than half the part of 2025 they were alive, or since the adoption or placement?" = true)
- Expr: `{"any":[{"eq":["dependent.lived_half",{"const":true}],"op":"test"},{"all":[{"eq":["dependent.qualifying_child",{"const":false}],"op":"test"},{"any":[{"eq":["dependent.born_died",{"const":true}],"op":"test"},{"eq":["dependent.placed",{"const":true}],"op":"test"}],"op":"test"},{"eq":["dependent.part_year_home",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
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
- **Encoded (Bool):** (helper "Age at the end of 2025" < 19 (qc.age_limit) and helper "Younger than you (or your spouse if filing jointly)?" = true or helper "Age at the end of 2025" < 24 (qc.student_age_limit) and helper "Full-time student in 2025?" = true and helper "Younger than you (or your spouse if filing jointly)?" = true or helper "Permanently and totally disabled?" = true)
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

## (helper) — `dependent.ctc_child`

- **Authored helper label:** Qualifying child for the child tax credit (Step 3)
- **Encoded (Bool):** helper "Qualifying child who is your dependent (Step 2)" = true and helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = true and helper "U.S. citizen, U.S. national or U.S. resident alien?" = true and helper "Under age 17 at the end of 2025" = true and helper "SSN valid for employment issued before the due date of your return?" = true and household helper "Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid for employment, and each other person on the return has an SSN or ITIN" = true
- Expr: `{"all":[{"eq":["dependent.qc_dependent",{"const":true}],"op":"test"},{"eq":["dependent.tin",{"const":true}],"op":"test"},{"eq":["dependent.citizen",{"const":true}],"op":"test"},{"eq":["dependent.under_ctc_age",{"const":true}],"op":"test"},{"eq":["dependent.work_ssn",{"const":true}],"op":"test"},{"eq":["household.ctc_ssn",{"const":true}],"op":"test"}],"op":"test"}`
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

## (helper) — `dependent.hoh_test2`

- **Authored helper label:** A Test 2 person who lived with you more than half the year, or of the part of the year a relative was alive (the home-cost condition of Test 2 is tested on the household form)
- **Encoded (Bool):** (helper "Your dependent" = true and helper "Relationship to you" ≠ 'household_member' and helper "Relationship to you" ≠ 'sibling_descendant' and helper "Relationship to you" ≠ 'other' and helper "Lived with you more than half of 2025, or, for a relative other than a qualifying child (whose months already count the part of the year), more than half of the part of 2025 they were alive or since their adoption or placement" = true or helper "Qualifying child (Step 1)" = true and helper "Married?" = false and helper "Lived with you for more than half of 2025" = true)
- Expr: `{"any":[{"all":[{"eq":["dependent.claimed",{"const":true}],"op":"test"},{"ne":["dependent.relationship",{"const":"household_member"}],"op":"test"},{"ne":["dependent.relationship",{"const":"sibling_descendant"}],"op":"test"},{"ne":["dependent.relationship",{"const":"other"}],"op":"test"},{"eq":["dependent.hoh_lived_half",{"const":true}],"op":"test"}],"op":"test"},{"all":[{"eq":["dependent.qualifying_child",{"const":true}],"op":"test"},{"eq":["dependent.married",{"const":false}],"op":"test"},{"eq":["dependent.lived_half",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2 (a dependent, other than one who is your dependent only because they lived with you all year, which is any person claimed through the last Step 4 bullet, or your unmarried qualifying child, who lived with you more than half the year) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `dependent.hoh_test1`

- **Authored helper label:** Qualifies you for head of household under Test 1 through a parent who does not live with you (a parent who lives with you qualifies you through Test 2)
- **Encoded (Bool):** helper "Relationship to you" = 'parent' and helper "Your dependent" = true and helper "For a parent not living with you, you paid over half the cost of their main home for all of 2025 (or the part of 2025 they were alive)?" = true
- **Refusal:** when dependent.claimed_no_tin is true, cannot complete Dependent without an SSN, ITIN or ATIN (Form 1040, Dependents, row (3)). Each dependent must be listed with an SSN (or ITIN or ATIN) issued on or before the due date of your return. A dependent child who was born and died in 2025 without an SSN, entered as "Died" on row (3) with a copy of the birth certificate, death certificate or hospital records, is outside this tool. Cite: [i1040gi] p. 22, Social security number, "You must enter each dependent’s social security number (SSN)" and "If your dependent child was born and died in 2025 and you do not have an SSN for the child, enter “Died” on row (3) of the Dependents section and include a copy of the child’s birth certificate, death certificate, or hospital records"; p. 14, Head of Household, "The dependents you claim are those you list by name and SSN ... in the Dependents section on Form 1040 or 1040-SR" (2025; printed date 2026-02-25; sha256 482e9c48)
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

- **Authored helper label:** One qualifying person
- **Encoded (Count):** Enter 1 (dependent.one).
- Expr: `{"op":"param","ref":"dependent.one"}`
- Cite: [i2441] p. 3, Line 2, "Complete columns (a) through (d) for each qualifying person"; p. 3, Column (b), "You must enter the qualifying person's SSN" (a qualifying person is a dependent, and a dependent without an SSN, ITIN or ATIN is refused where the person is counted as a dependent) (2025; sha256 86f0669e)

## (helper) — `dependent.dc_paid`

- **Authored helper label:** Qualified expenses incurred and paid in 2025 for this person's care
- **Encoded (NonNegDollars):** Input — Qualified expenses you incurred and paid in 2025 for this person's care while they were a qualifying person (under age 13, or not able to care for themselves), so that you (and your spouse, if filing jointly) could work or look for work. Include care you prepaid in 2024 for 2025, your share of employment taxes on a care provider's wages, and expenses paid with dependent care benefits (reimbursed from a dependent care account or paid by your employer to the provider); Form 2441 subtracts the benefits you exclude. Do not include 2024 care paid in 2025, 2025 care paid in 2026, payments for care in 2026, amounts reimbursed by a state social services agency, payments to a provider who may not be listed (your spouse, your dependent, your child under 19, or the parent of your child under 13), or expenses you claim as medical expenses; zero if none
- Interpretation: amb.2025.dc_line30
- Expr: `{"op":"input","source":"Qualified expenses you incurred and paid in 2025 for this person's care while they were a qualifying person (under age 13, or not able to care for themselves), so that you (and your spouse, if filing jointly) could work or look for work. Include care you prepaid in 2024 for 2025, your share of employment taxes on a care provider's wages, and expenses paid with dependent care benefits (reimbursed from a dependent care account or paid by your employer to the provider); Form 2441 subtracts the benefits you exclude. Do not include 2024 care paid in 2025, 2025 care paid in 2026, payments for care in 2026, amounts reimbursed by a state social services agency, payments to a provider who may not be listed (your spouse, your dependent, your child under 19, or the parent of your child under 13), or expenses you claim as medical expenses; zero if none"}`
- Cite: [i2441] pp. 3–4, Column (d), "Enter the qualified expenses you incurred and paid in 2025 for the person listed in column (a)" and "Expenses you incurred in 2025 but didn't pay until 2026"; p503 p. 10, Expenses prepaid in an earlier year, "If you pay for services before they are provided, you can count the prepaid expenses only in the year the care is received" (2025; sha256 86f0669e)

## 2(d) — `dependent.dc_line2d`

- **Authored helper label:** Qualified expenses you incurred and paid in 2025 for the person listed in column (a)
- **Encoded (NonNegDollars):** Enter the amount from helper "Qualified expenses incurred and paid in 2025 for this person's care".
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
- Expr: `{"all":[{"eq":["dependent.dc_qp",{"const":true}],"op":"test"},{"eq":["dependent.dc_incapable",{"const":true}],"op":"test"},{"any":[{"gt":["dependent.age",{"param":"dc.child_age"}],"op":"test"},{"all":[{"eq":["dependent.age",{"param":"dc.child_age"}],"op":"test"},{"eq":["dependent.dc_over12_care",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i2441] p. 3, Column (c), "Check the box in column (c) if the qualifying person listed in column (a) was over age 12 at the time the care was provided and was disabled" (2025; sha256 86f0669e)
