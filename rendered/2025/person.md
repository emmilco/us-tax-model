# Each person on the return — per-person facts and totals (excess Social Security tax, Schedule SE, SEP and SIMPLE plans, health insurance and others)

- Document: `person` (worksheet, tax year 2025)
- Collection: keyed entries; [f1040] Form 1040 (2025), page 1, "Your first name and middle initial" and "If joint return, spouse’s first name and middle initial" (2025; created 2025-09-05; sha256 3d31c226)
- Note: Helper worksheet. Wages means boxes 3 plus 7 under approved interpretation amb.2025.ss_wages. Independent lines may compute while credit and dependent totals are refused.

## (helper) — `person.role`

- **Authored helper label:** Whose entry is this, yours or your spouse's?
- **Encoded (Enum(person_role)):** Input — Whose entry is this, yours (the taxpayer) or your spouse's?
- Expr: `{"op":"input","source":"Whose entry is this, yours (the taxpayer) or your spouse's?"}`
- Cite: [f1040] Form 1040 (2025), page 1, "Your first name and middle initial" and "If joint return, spouse’s first name and middle initial" (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `person.one`

- **Authored helper label:** One entry for this person
- **Encoded (Count):** Enter 1 (person.one).
- Expr: `{"op":"param","ref":"person.one"}`
- Cite: [f1040] Form 1040 (2025), page 1, one entry for you and, if joint return, one for your spouse (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `person.birth_year`

- **Authored helper label:** The year you were born
- **Encoded (Count):** Input — In what year were you born?
- Expr: `{"op":"input","source":"In what year were you born?"}`
- Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)"; p. 33, Blindness, "If you weren’t totally blind as of December 31, 2025, you must get a statement certified by your eye doctor (ophthalmologist or optometrist) that:", "You can't see better than 20/200 in your better eye with glasses or contact lenses, or", "Your field of vision is 20 degrees or less.", "If your eye condition isn’t likely to improve beyond the conditions listed above, you can get a statement certified by your eye doctor (ophthalmologist or optometrist) to this effect instead." and "You must keep the statement for your records."; p501 p. 23, Not totally blind, "If your vision can be corrected beyond these limits only by contact lenses that you can wear only briefly because of pain, infection, or ulcers, you can take the higher standard deduction for blindness if you otherwise qualify." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.birth_cut_year`

- **Authored helper label:** Born in a year in which a birth on January 1 changes an age test of this return (1961, 2001, 2002, 2007 or 2008)
- **Encoded (Bool):** (helper "The year you were born" = 1961 (age.cut_65) or helper "The year you were born" = 2001 (age.cut_25) or helper "The year you were born" = 2002 (age.cut_24) or helper "The year you were born" = 2007 (age.cut_19) or helper "The year you were born" = 2008 (age.cut_18))
- Expr: `{"any":[{"eq":["person.birth_year",{"param":"age.cut_65"}],"op":"test"},{"eq":["person.birth_year",{"param":"age.cut_25"}],"op":"test"},{"eq":["person.birth_year",{"param":"age.cut_24"}],"op":"test"},{"eq":["person.birth_year",{"param":"age.cut_19"}],"op":"test"},{"eq":["person.birth_year",{"param":"age.cut_18"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)"; p. 33, Blindness, "If you weren’t totally blind as of December 31, 2025, you must get a statement certified by your eye doctor (ophthalmologist or optometrist) that:", "You can't see better than 20/200 in your better eye with glasses or contact lenses, or", "Your field of vision is 20 degrees or less.", "If your eye condition isn’t likely to improve beyond the conditions listed above, you can get a statement certified by your eye doctor (ophthalmologist or optometrist) to this effect instead." and "You must keep the statement for your records."; p501 p. 23, Not totally blind, "If your vision can be corrected beyond these limits only by contact lenses that you can wear only briefly because of pain, infection, or ulcers, you can take the higher standard deduction for blindness if you otherwise qualify." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.born_jan1`

- **Authored helper label:** Were you born on January 1?
- **Encoded (Bool):** Input — Were you born on January 1?
- Expr: `{"op":"input","source":"Were you born on January 1?"}`
- Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)"; p. 33, Blindness, "If you weren’t totally blind as of December 31, 2025, you must get a statement certified by your eye doctor (ophthalmologist or optometrist) that:", "You can't see better than 20/200 in your better eye with glasses or contact lenses, or", "Your field of vision is 20 degrees or less.", "If your eye condition isn’t likely to improve beyond the conditions listed above, you can get a statement certified by your eye doctor (ophthalmologist or optometrist) to this effect instead." and "You must keep the statement for your records."; p501 p. 23, Not totally blind, "If your vision can be corrected beyond these limits only by contact lenses that you can wear only briefly because of pain, infection, or ulcers, you can take the higher standard deduction for blindness if you otherwise qualify." (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `person.born_jan1_if_cut_year`

- **Authored helper label:** Born on January 1 (asked only of a person born in 1961, 2001, 2002, 2007 or 2008; otherwise no)
- **Encoded (Bool):** Choose — [helper "Born in a year in which a birth on January 1 changes an age test of this return (1961, 2001, 2002, 2007 or 2008)" = true → helper "Were you born on January 1?"] [helper "Born in a year in which a birth on January 1 changes an age test of this return (1961, 2001, 2002, 2007 or 2008)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.birth_cut_year",{"const":true}],"op":"test"},"then":"person.born_jan1"},{"guard":{"eq":["person.birth_cut_year",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)"; p. 33, Blindness, "If you weren’t totally blind as of December 31, 2025, you must get a statement certified by your eye doctor (ophthalmologist or optometrist) that:", "You can't see better than 20/200 in your better eye with glasses or contact lenses, or", "Your field of vision is 20 degrees or less.", "If your eye condition isn’t likely to improve beyond the conditions listed above, you can get a statement certified by your eye doctor (ophthalmologist or optometrist) to this effect instead." and "You must keep the statement for your records."; p501 p. 23, Not totally blind, "If your vision can be corrected beyond these limits only by contact lenses that you can wear only briefly because of pain, infection, or ulcers, you can take the higher standard deduction for blindness if you otherwise qualify." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.birth_year_bad`

- **Authored helper label:** The year of birth entered is after the tax year, or more than 125 years before it
- **Encoded (Bool):** (helper "The year you were born" > 2025 (age.birth_year_latest) or helper "The year you were born" < 1900 (age.birth_year_earliest))
- Expr: `{"any":[{"gt":["person.birth_year",{"param":"age.birth_year_latest"}],"op":"test"},{"lt":["person.birth_year",{"param":"age.birth_year_earliest"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.age65`

- **Authored helper label:** Born before January 2, 1961
- **Encoded (Bool):** (helper "The year you were born" < 1961 (age.cut_65) or helper "The year you were born" = 1961 (age.cut_65) and helper "Born on January 1 (asked only of a person born in 1961, 2001, 2002, 2007 or 2008; otherwise no)" = true)
- Expr: `{"any":[{"lt":["person.birth_year",{"param":"age.cut_65"}],"op":"test"},{"all":[{"eq":["person.birth_year",{"param":"age.cut_65"}],"op":"test"},{"eq":["person.born_jan1_if_cut_year",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.under24`

- **Authored helper label:** Under age 24 at the end of 2025 (born after January 1, 2002)
- **Encoded (Bool):** (helper "The year you were born" > 2002 (age.cut_24) or helper "The year you were born" = 2002 (age.cut_24) and helper "Born on January 1 (asked only of a person born in 1961, 2001, 2002, 2007 or 2008; otherwise no)" = false)
- Expr: `{"any":[{"gt":["person.birth_year",{"param":"age.cut_24"}],"op":"test"},{"all":[{"eq":["person.birth_year",{"param":"age.cut_24"}],"op":"test"},{"eq":["person.born_jan1_if_cut_year",{"const":false}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i8615] p. 1, Certain January 1 birthdays, "Use the following chart to determine whether certain children with January 1 birthdays meet condition 3 under Who Must File" (a child born on "January 1, 2002" is considered to be 24 at the end of 2025: "Don’t use Form 8615 for this child.") (2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 902ca736)

## (helper) — `person.blind`

- **Authored helper label:** Were you blind at the end of 2025 (totally blind, or partly blind with a statement certified by your eye doctor)?
- **Encoded (Bool):** Input — Were you blind at the end of 2025?

  Answer yes if you were totally blind as of December 31, 2025.

  If you weren't totally blind, answer yes only if you have a statement certified by your eye doctor (ophthalmologist or optometrist) that you can't see better than 20/200 in your better eye with glasses or contact lenses, or that your field of vision is 20 degrees or less (or, if your eye condition isn't likely to improve beyond these conditions, a certified statement to that effect).

  If your vision can be corrected beyond these limits only by contact lenses that you can wear only briefly because of pain, infection or ulcers, those lenses do not count as correcting it: answer yes if you have the certified statement described above.

  Keep the statement for your records.
- Expr: `{"op":"input","source":"Were you blind at the end of 2025?\n\nAnswer yes if you were totally blind as of December 31, 2025.\n\nIf you weren't totally blind, answer yes only if you have a statement certified by your eye doctor (ophthalmologist or optometrist) that you can't see better than 20/200 in your better eye with glasses or contact lenses, or that your field of vision is 20 degrees or less (or, if your eye condition isn't likely to improve beyond these conditions, a certified statement to that effect).\n\nIf your vision can be corrected beyond these limits only by contact lenses that you can wear only briefly because of pain, infection or ulcers, those lenses do not count as correcting it: answer yes if you have the certified statement described above.\n\nKeep the statement for your records."}`
- Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)"; p. 33, Blindness, "If you weren’t totally blind as of December 31, 2025, you must get a statement certified by your eye doctor (ophthalmologist or optometrist) that:", "You can't see better than 20/200 in your better eye with glasses or contact lenses, or", "Your field of vision is 20 degrees or less.", "If your eye condition isn’t likely to improve beyond the conditions listed above, you can get a statement certified by your eye doctor (ophthalmologist or optometrist) to this effect instead." and "You must keep the statement for your records."; p501 p. 23, Not totally blind, "If your vision can be corrected beyond these limits only by contact lenses that you can wear only briefly because of pain, infection, or ulcers, you can take the higher standard deduction for blindness if you otherwise qualify." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.tin`

- **Authored helper label:** Do you have an SSN or ITIN issued on or before the due date of your return?
- **Encoded (Bool):** Input — Do you have an SSN or ITIN issued on or before the due date of your 2025 return (including extensions)? An ITIN that has expired counts only if it has been renewed by then (a renewal only applied for does not count here).
- Expr: `{"op":"input","source":"Do you have an SSN or ITIN issued on or before the due date of your 2025 return (including extensions)? An ITIN that has expired counts only if it has been renewed by then (a renewal only applied for does not count here)."}`
- Cite: [i1040gi] p. 17, Before you begin, "The other spouse must have either an SSN or ITIN, and it must have been issued on or before the due date of the return (including extensions)"; p. 19, Step 5, question 1; p503 p. 3, "If your ITIN wasn’t included on at least one U.S. federal tax return for the last 3 consecutive tax years, it expires on December 31 of the third consecutive tax year, and must be renewed before being used again on a U.S. federal tax return." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.itin_applied`

- **Authored helper label:** If not, have you applied, or are you applying, for an ITIN, or for the renewal of your expired ITIN, on or before the due date of your return?
- **Encoded (Bool):** Input — If you have neither (or your ITIN has expired and was not renewed), have you applied, or are you applying, for an ITIN, or for the renewal of your expired ITIN, on or before the due date of your 2025 return (including extensions)? Answer Yes if you are applying with this return, for example by filing Form W-7 with it.
- Expr: `{"op":"input","source":"If you have neither (or your ITIN has expired and was not renewed), have you applied, or are you applying, for an ITIN, or for the renewal of your expired ITIN, on or before the due date of your 2025 return (including extensions)? Answer Yes if you are applying with this return, for example by filing Form W-7 with it."}`
- Cite: [i1040gi] p. 19, Step 5, question 1, "(Answer 'Yes' if you are applying for an ITIN on or before the return due date (including extensions).)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.work_ssn`

- **Authored helper label:** Do you have an SSN valid for employment issued before the due date of your return?
- **Encoded (Bool):** Input — Do you have an SSN valid for employment, issued before the due date of your 2025 return (including extensions)? If your card says "Valid for Work Only With DHS Authorization", answer yes only if the DHS authorization is valid.
- Expr: `{"op":"input","source":"Do you have an SSN valid for employment, issued before the due date of your 2025 return (including extensions)? If your card says \"Valid for Work Only With DHS Authorization\", answer yes only if the DHS authorization is valid."}`
- Cite: [i1040gi] p. 18, Step 3, question 4; p. 104, Valid SSN for No Tax on Tips, "However, if “Valid for Work Only with DHS Authorization” is printed on your social security card, your SSN is valid only as long as the DHS authorization is valid"; p. 108, Valid SSN, "see Valid SSN for No Tax on Tips, earlier"; p. 110, Valid SSN, "see Valid SSN for No Tax on Tips, earlier" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.eic_ssn`

- **Authored helper label:** Do you have an SSN valid for the EIC, issued on or before the due date of your return?
- **Encoded (Bool):** Input — Do you have a social security number issued on or before the due date of your 2025 return (including extensions) that is valid for the EIC? Any number issued by the Social Security Administration is valid unless the card says "Not Valid for Employment" and the number was issued solely to apply for or receive a federally funded benefit; a card that says "Valid for Work Only With DHS Authorization" is valid only while the authorization is valid.
- Expr: `{"op":"input","source":"Do you have a social security number issued on or before the due date of your 2025 return (including extensions) that is valid for the EIC? Any number issued by the Social Security Administration is valid unless the card says \"Not Valid for Employment\" and the number was issued solely to apply for or receive a federally funded benefit; a card that says \"Valid for Work Only With DHS Authorization\" is valid only while the authorization is valid."}`
- Cite: [i1040gi] p. 40, Step 1, question 2; pp. 44–45, Social security number (SSN), "For the EIC, a valid SSN is a number issued by the Social Security Administration unless “Not Valid for Employment” is printed on the social security card and the number was issued solely to allow the recipient of the SSN to apply for or receive a federally funded benefit" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.under16`

- **Authored helper label:** Under age 16 at the end of 2025
- **Encoded (Bool):** (helper "The year you were born" > 2010 (age.cut_16) or helper "The year you were born" = 2010 (age.cut_16) and helper "Under age 16 at the end of 2025, as stated by a person born in 2010 (otherwise no)" = true)
- Interpretation: amb.2025.filer_under_16
- Expr: `{"any":[{"gt":["person.birth_year",{"param":"age.cut_16"}],"op":"test"},{"all":[{"eq":["person.birth_year",{"param":"age.cut_16"}],"op":"test"},{"eq":["person.under16_at_year_end_if_open_year",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 66, Self-Select PIN, "You can’t use the Self-Select PIN method if you are a first-time filer under age 16 at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.under16_open_year`

- **Authored helper label:** Born in 2010
- **Encoded (Bool):** helper "The year you were born" = 2010 (age.cut_16)
- Expr: `{"eq":["person.birth_year",{"param":"age.cut_16"}],"op":"test"}`
- Cite: [i1040gi] p. 66, Self-Select PIN, "You can’t use the Self-Select PIN method if you are a first-time filer under age 16 at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.under16_at_year_end`

- **Authored helper label:** Were you under age 16 at the end of 2025?
- **Encoded (Bool):** Input — Were you under age 16 at the end of 2025?
- Interpretation: amb.2025.filer_under_16
- Expr: `{"op":"input","source":"Were you under age 16 at the end of 2025?"}`
- Cite: [i1040gi] p. 66, Self-Select PIN, "You can’t use the Self-Select PIN method if you are a first-time filer under age 16 at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `person.under16_at_year_end_if_open_year`

- **Authored helper label:** Under age 16 at the end of 2025, as stated by a person born in 2010 (otherwise no)
- **Encoded (Bool):** Choose — [helper "Born in 2010" = true → helper "Were you under age 16 at the end of 2025?"] [helper "Born in 2010" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.under16_open_year",{"const":true}],"op":"test"},"then":"person.under16_at_year_end"},{"guard":{"eq":["person.under16_open_year",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 66, Self-Select PIN, "You can’t use the Self-Select PIN method if you are a first-time filer under age 16 at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.educator_expenses`

- **Authored helper label:** Qualified educator expenses you paid in 2025
- **Encoded (NonNegDollars):** Input — Qualified educator expenses you paid in 2025 (professional development courses you took that are related to the curriculum you teach or to the students you teach, and books, supplies, equipment (including computer equipment, software and services) and other materials used in the classroom, including personal protective equipment, disinfectant and other supplies used to prevent the spread of coronavirus; not expenses for home schooling or nonathletic supplies for courses in health or physical education), reduced by excludable savings bond interest (Form 8815), nontaxable qualified tuition program or Coverdell earnings or distributions, and reimbursements not reported in box 1 of your Form W-2; zero if none
- Expr: `{"op":"input","source":"Qualified educator expenses you paid in 2025 (professional development courses you took that are related to the curriculum you teach or to the students you teach, and books, supplies, equipment (including computer equipment, software and services) and other materials used in the classroom, including personal protective equipment, disinfectant and other supplies used to prevent the spread of coronavirus; not expenses for home schooling or nonathletic supplies for courses in health or physical education), reduced by excludable savings bond interest (Form 8815), nontaxable qualified tuition program or Coverdell earnings or distributions, and reimbursements not reported in box 1 of your Form W-2; zero if none"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 11, Qualified expenses, 'For professional development courses you have taken related to the curriculum you teach or to the students you teach', 'equipment (including computer equipment, software, and services)', 'for personal protective equipment, disinfectant, and other supplies used for the prevention of the spread of coronavirus', and 'You must reduce your qualified expenses by the following amounts'; p. 93, 'Qualified expenses don’t include expenses for home schooling or for nonathletic supplies for courses in health or physical education.' (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.eligible_educator`

- **Authored helper label:** Were you an eligible educator in 2025 (a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who worked in a school for at least 900 hours during a school year)?
- **Encoded (Bool):** Input — Were you an eligible educator in 2025 (a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who worked in a school for at least 900 hours during a school year)?
- Expr: `{"op":"input","source":"Were you an eligible educator in 2025 (a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who worked in a school for at least 900 hours during a school year)?"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 11, 'An eligible educator is a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who worked in a school for at least 900 hours during a school year' (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `person.educator_expenses_if_educator`

- **Authored helper label:** Qualified educator expenses paid in 2025 (asked only of an eligible educator; otherwise zero)
- **Encoded (NonNegDollars):** Choose — [helper "Were you an eligible educator in 2025 (a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who worked in a school for at least 900 hours during a school year)?" = true → helper "Qualified educator expenses you paid in 2025"] [helper "Were you an eligible educator in 2025 (a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who worked in a school for at least 900 hours during a school year)?" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.eligible_educator",{"const":true}],"op":"test"},"then":"person.educator_expenses"},{"guard":{"eq":["person.eligible_educator",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 11, Qualified expenses, 'For professional development courses you have taken related to the curriculum you teach or to the students you teach', 'equipment (including computer equipment, software, and services)', 'for personal protective equipment, disinfectant, and other supplies used for the prevention of the spread of coronavirus', and 'You must reduce your qualified expenses by the following amounts'; p. 93, 'Qualified expenses don’t include expenses for home schooling or for nonathletic supplies for courses in health or physical education.' (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.eic_age25`

- **Authored helper label:** Born before January 2, 2001
- **Encoded (Bool):** (helper "The year you were born" < 2001 (age.cut_25) or helper "The year you were born" = 2001 (age.cut_25) and helper "Born on January 1 (asked only of a person born in 1961, 2001, 2002, 2007 or 2008; otherwise no)" = true)
- Expr: `{"any":[{"lt":["person.birth_year",{"param":"age.cut_25"}],"op":"test"},{"all":[{"eq":["person.birth_year",{"param":"age.cut_25"}],"op":"test"},{"eq":["person.born_jan1_if_cut_year",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 41, Step 4, question 2, "Check 'Yes' if you ... were born after December 31, 1960, and before January 2, 2001" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.eic_under65`

- **Authored helper label:** Born after December 31, 1960
- **Encoded (Bool):** helper "The year you were born" ≥ 1961 (age.cut_65)
- Expr: `{"ge":["person.birth_year",{"param":"age.cut_65"}],"op":"test"}`
- Cite: [i1040gi] p. 41, Step 4, question 2, "Check 'Yes' if you ... were born after December 31, 1960, and before January 2, 2001" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.age65_box`

- **Authored helper label:** Born before January 2, 1961, and not a person who died in 2025 before reaching 65 (a box checked for age)
- **Encoded (Bool):** Choose — [helper "Born before January 2, 1961" = true → helper "Not a person who died in 2025 before reaching 65"] [helper "Born before January 2, 1961" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.age65",{"const":true}],"op":"test"},"then":"person.not_died_before_65"},{"guard":{"eq":["person.age65",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)"; pp. 34–35, Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.not_died_before_65`

- **Authored helper label:** Not a person who died in 2025 before reaching 65
- **Encoded (Bool):** helper "The final return of a person who died in 2025 before reaching age 65 (asked only of a person born in 1960, or on January 1, 1961; otherwise no)" = false
- Expr: `{"eq":["person.died_before_65",{"const":false}],"op":"test"}`
- Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)"; pp. 34–35, Standard Deduction Chart for People Who Were Born Before January 2, 1961, or Were Blind (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.tin_or_itin_applied`

- **Authored helper label:** An SSN or ITIN, or applied for an ITIN
- **Encoded (Bool):** Choose — [helper "Do you have an SSN or ITIN issued on or before the due date of your return?" = true → helper "Do you have an SSN or ITIN issued on or before the due date of your return?"] [helper "Do you have an SSN or ITIN issued on or before the due date of your return?" = false → helper "If not, have you applied, or are you applying, for an ITIN, or for the renewal of your expired ITIN, on or before the due date of your return?"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.tin",{"const":true}],"op":"test"},"then":"person.tin"},{"guard":{"eq":["person.tin",{"const":false}],"op":"test"},"then":"person.itin_applied"}],"op":"choose"}`
- Cite: [i1040gi] p. 17, Before you begin, "If you want to claim the credit for other dependents, you, and your spouse if filing jointly, must have either an SSN or ITIN"; p. 19, Step 5, question 1, "(Answer 'Yes' if you are applying for an ITIN on or before the return due date (including extensions).)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.work_ssn_or_tin`

- **Authored helper label:** An SSN valid for employment, or an SSN or ITIN
- **Encoded (Bool):** Choose — [helper "Do you have an SSN or ITIN issued on or before the due date of your return?" = true → helper "Do you have an SSN or ITIN issued on or before the due date of your return?"] [helper "Do you have an SSN or ITIN issued on or before the due date of your return?" = false → helper "Do you have an SSN valid for employment issued before the due date of your return?"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.tin",{"const":true}],"op":"test"},"then":"person.tin"},{"guard":{"eq":["person.tin",{"const":false}],"op":"test"},"then":"person.work_ssn"}],"op":"choose"}`
- Cite: [i1040gi] p. 17, Before you begin, "The other spouse must have either an SSN or ITIN" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.turned_65_this_year`

- **Authored helper label:** Born in 1960, or on January 1, 1961 (a person whose 65th birthday, or the day before it, fell in 2025)
- **Encoded (Bool):** (helper "The year you were born" = 1960 (age.turning_65) or helper "The year you were born" = 1961 (age.cut_65) and helper "Born on January 1 (asked only of a person born in 1961, 2001, 2002, 2007 or 2008; otherwise no)" = true)
- Expr: `{"any":[{"eq":["person.birth_year",{"param":"age.turning_65"}],"op":"test"},{"all":[{"eq":["person.birth_year",{"param":"age.cut_65"}],"op":"test"},{"eq":["person.born_jan1_if_cut_year",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Death of a taxpayer in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.died_before_65`

- **Authored helper label:** The final return of a person who died in 2025 before reaching age 65 (asked only of a person born in 1960, or on January 1, 1961; otherwise no)
- **Encoded (Bool):** Choose — [helper "Born in 1960, or on January 1, 1961 (a person whose 65th birthday, or the day before it, fell in 2025)" = true → helper "Is this the final return of a person who died in 2025 before reaching age 65?"] [helper "Born in 1960, or on January 1, 1961 (a person whose 65th birthday, or the day before it, fell in 2025)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.turned_65_this_year",{"const":true}],"op":"test"},"then":"person.died_at_64"},{"guard":{"eq":["person.turned_65_this_year",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Death of a taxpayer in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.died_at_64`

- **Authored helper label:** Is this the final return of a person who died in 2025 before reaching age 65?
- **Encoded (Bool):** Input — Is this the final return of a person who died in 2025 before reaching age 65? (A person reaches age 65 on the day before the 65th birthday.)
- Expr: `{"op":"input","source":"Is this the final return of a person who died in 2025 before reaching age 65? (A person reaches age 65 on the day before the 65th birthday.)"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Death of a taxpayer in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.educator_max`

- **Authored helper label:** Year parameter s1.educator_max ($300)
- **Encoded (NonNegDollars):** Enter $300 (s1.educator_max).
- Expr: `{"op":"param","ref":"s1.educator_max"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 11, "If you and your spouse are filing jointly and both of you were eligible educators, the maximum deduction is $600. However, neither spouse can deduct more than $300 of their qualified expenses" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.has_educator_expenses`

- **Authored helper label:** Any qualified educator expenses for this person
- **Encoded (Bool):** helper "Qualified educator expenses paid in 2025 (asked only of an eligible educator; otherwise zero)" > $0 (sales.zero)
- Expr: `{"gt":["person.educator_expenses_if_educator",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 11 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.educator_limited`

- **Authored helper label:** This person's qualified educator expenses, up to $300
- **Encoded (NonNegDollars):** Enter the smaller of helper "Qualified educator expenses paid in 2025 (asked only of an eligible educator; otherwise zero)" or helper "Year parameter s1.educator_max ($300)".
- Expr: `{"of":["person.educator_expenses_if_educator","person.educator_max"],"op":"smaller_of"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 11, "If you and your spouse are filing jointly and both of you were eligible educators, the maximum deduction is $600. However, neither spouse can deduct more than $300 of their qualified expenses" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.educator_eligible_amount`

- **Authored helper label:** This person's qualified educator expenses up to $300 if an eligible educator, else zero
- **Encoded (NonNegDollars):** Choose — [helper "Were you an eligible educator in 2025 (a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who worked in a school for at least 900 hours during a school year)?" = true → helper "This person's qualified educator expenses, up to $300"] [helper "Were you an eligible educator in 2025 (a kindergarten through grade 12 teacher, instructor, counselor, principal, or aide who worked in a school for at least 900 hours during a school year)?" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.eligible_educator",{"const":true}],"op":"test"},"then":"person.educator_limited"},{"guard":{"eq":["person.eligible_educator",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 11, "If you were an eligible educator in 2025, you can deduct on line 11 up to $300 of qualified expenses you paid in 2025"; "If you and your spouse are filing jointly and both of you were eligible educators, the maximum deduction is $600. However, neither spouse can deduct more than $300 of their qualified expenses" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.educator_deduction`

- **Authored helper label:** This person's educator expense deduction
- **Encoded (NonNegDollars):** Choose — [helper "Any qualified educator expenses for this person" = true → helper "This person's qualified educator expenses up to $300 if an eligible educator, else zero"] [helper "Any qualified educator expenses for this person" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_educator_expenses",{"const":true}],"op":"test"},"then":"person.educator_eligible_amount"},{"guard":{"eq":["person.has_educator_expenses",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 11, "If you were an eligible educator in 2025, you can deduct on line 11 up to $300 of qualified expenses you paid in 2025"; "If you and your spouse are filing jointly and both of you were eligible educators, the maximum deduction is $600. However, neither spouse can deduct more than $300 of their qualified expenses" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.hsa_forms`

- **Authored helper label:** Number of Forms 8889 entered for this person
- **Encoded (Count):** Add f8889.one over every confirmed f8889 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8889","field":"f8889.one","op":"sum_over"}`
- Cite: [i8889] p. 4, Name and social security number (SSN), "complete a separate Form 8889 for each of you" (2025; sha256 da6f2f58)

## (gate) — `person.hsa_repeated`

- **Authored helper label:** More than one Form 8889 entered for this person
- **Encoded (Bool):** helper "Number of Forms 8889 entered for this person" > 1 (a count)
- Expr: `{"gt":["person.hsa_forms",{"const":1,"type":"Count"}],"op":"test"}`
- Cite: [i8889] p. 4, Name and social security number (SSN), "complete a separate Form 8889 for each of you" (2025; sha256 da6f2f58)

## (helper) — `person.hsa_split`

- **Authored helper label:** This persons Form 8889 uses the spouse rule of line 6
- **Encoded (Count):** Add f8889.one over every confirmed f8889 entry for which helper "Spouses with separate HSAs, treated as having family coverage at any time during 2025" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8889","field":"f8889.one","op":"sum_over","where":{"eq":["f8889.split",{"const":true}],"op":"test"}}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, Steps 1 to 3, "Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, use the following rules to figure the amount on line 6", "Step 1. Refigure the contribution limit that would have been entered on line 5 if you had entered on line 3 the total of the worksheet amounts only for the months you were treated as having family coverage", "Step 2. Divide the refigured contribution limit from Step 1 equally between you and your spouse, unless you both agree on a different allocation (such as allocating nothing to one spouse)", "Step 3. Subtract the part of the contribution limit allocated to your spouse in Step 2 from the amount determined in Step 1" (2025; sha256 da6f2f58)

## (helper) — `person.hsa_agreed`

- **Authored helper label:** This persons Form 8889 uses an agreed allocation under the spouse rule of line 6
- **Encoded (Count):** Add f8889.one over every confirmed f8889 entry for which helper "Spouses with separate HSAs, treated as having family coverage at any time during 2025" = true and helper "Do you and your spouse divide the family contribution limit equally, or by a different allocation you both agree on?" = 'agreed', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8889","field":"f8889.one","op":"sum_over","where":{"all":[{"eq":["f8889.split",{"const":true}],"op":"test"},{"eq":["f8889.allocation",{"const":"agreed"}],"op":"test"}],"op":"test"}}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, Steps 1 to 3, "Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, use the following rules to figure the amount on line 6", "Step 1. Refigure the contribution limit that would have been entered on line 5 if you had entered on line 3 the total of the worksheet amounts only for the months you were treated as having family coverage", "Step 2. Divide the refigured contribution limit from Step 1 equally between you and your spouse, unless you both agree on a different allocation (such as allocating nothing to one spouse)", "Step 3. Subtract the part of the contribution limit allocated to your spouse in Step 2 from the amount determined in Step 1" (2025; sha256 da6f2f58)

## (helper) — `person.hsa_step1`

- **Authored helper label:** This persons Step 1 limit under the spouse rule of line 6
- **Encoded (NonNegDollars):** Add f8889.step1 over every confirmed f8889 entry for which helper "Spouses with separate HSAs, treated as having family coverage at any time during 2025" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8889","field":"f8889.step1","op":"sum_over","where":{"eq":["f8889.split",{"const":true}],"op":"test"}}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, Steps 1 to 3, "Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, use the following rules to figure the amount on line 6", "Step 1. Refigure the contribution limit that would have been entered on line 5 if you had entered on line 3 the total of the worksheet amounts only for the months you were treated as having family coverage", "Step 2. Divide the refigured contribution limit from Step 1 equally between you and your spouse, unless you both agree on a different allocation (such as allocating nothing to one spouse)", "Step 3. Subtract the part of the contribution limit allocated to your spouse in Step 2 from the amount determined in Step 1" (2025; sha256 da6f2f58)

## (helper) — `person.hsa_share`

- **Authored helper label:** This persons part of the Step 1 limit under the spouse rule of line 6
- **Encoded (NonNegDollars):** Add f8889.share_raw over every confirmed f8889 entry for which helper "Spouses with separate HSAs, treated as having family coverage at any time during 2025" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8889","field":"f8889.share_raw","op":"sum_over","where":{"eq":["f8889.split",{"const":true}],"op":"test"}}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, Steps 1 to 3, "Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, use the following rules to figure the amount on line 6", "Step 1. Refigure the contribution limit that would have been entered on line 5 if you had entered on line 3 the total of the worksheet amounts only for the months you were treated as having family coverage", "Step 2. Divide the refigured contribution limit from Step 1 equally between you and your spouse, unless you both agree on a different allocation (such as allocating nothing to one spouse)", "Step 3. Subtract the part of the contribution limit allocated to your spouse in Step 2 from the amount determined in Step 1" (2025; sha256 da6f2f58)

## (helper) — `person.hsa_deduction`

- **Authored helper label:** Form 8889 line 13 for this person
- **Encoded (NonNegDollars):** Add f8889.line13 over every confirmed f8889 entry, within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when person.hsa_repeated is true, cannot complete More than one Form 8889 for one person. Enter one Form 8889 per person, combining all of that person's own HSAs on it. A separate Form 8889 for each HSA (with a controlling Form 8889) is required only for an inherited HSA, which is outside this tool. Cite: [i8889] p. 3, "If, during the tax year, you are the beneficiary of two or more HSAs or you are a beneficiary of an HSA and you have your own HSA, you must complete a separate Form 8889 for each HSA" (2025; sha256 da6f2f58)
- Expr: `{"collection":"f8889","field":"f8889.line13","op":"sum_over"}`
- Cite: [i8889] p. 4, "Combine the amounts on line 13 of both Forms 8889 and enter this amount on Schedule 1 (Form 1040), line 13" (2025; sha256 da6f2f58)

## (helper) — `person.hsa_taxable`

- **Authored helper label:** Form 8889 line 16 for this person
- **Encoded (NonNegDollars):** Add f8889.line16 over every confirmed f8889 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8889","field":"f8889.line16","op":"sum_over"}`
- Cite: [f8889] p. 1, Part II, "HSA Distributions. If you are filing jointly and both you and your spouse each have separate HSAs, complete a separate Part II for each spouse", line 16, "Taxable HSA distributions. Subtract line 15 from line 14c. If zero or less, enter -0-" (2025; created 2025-03-28; sha256 15ed4587)

## (helper) — `person.hsa_addtax`

- **Authored helper label:** Form 8889 line 17b for this person
- **Encoded (NonNegDollars):** Add f8889.line17b over every confirmed f8889 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8889","field":"f8889.line17b","op":"sum_over"}`
- Cite: [f8889] Form 8889 (2025), line 17b, "Also, include this amount in the total on Schedule 2 (Form 1040), Part II, line 17c" (2025; created 2025-03-28; sha256 15ed4587)

## (helper) — `person.tip_employers`

- **Authored helper label:** Number of employers that paid this person qualified tips
- **Encoded (Count):** Add tipjob.one over every confirmed tipjob entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"tipjob","field":"tipjob.one","op":"sum_over"}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 4c (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.tip_total`

- **Authored helper label:** This person's worksheet column (d) total
- **Encoded (NonNegDollars):** Add tipjob.col_d over every confirmed tipjob entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"tipjob","field":"tipjob.col_d","op":"sum_over"}`
- Cite: [i1040gi] p. 104, Qualified Tips From More Than One Employer Worksheet, line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.tip_reported`

- **Authored helper label:** This person's worksheet column (b) total
- **Encoded (NonNegDollars):** Add tipjob.amount over every confirmed tipjob entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"tipjob","field":"tipjob.amount","op":"sum_over"}`
- Cite: [i1040gi] p. 104, Qualified Tips From More Than One Employer Worksheet, column (b) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ot_employers`

- **Authored helper label:** Number of employers that paid this person qualified overtime compensation
- **Encoded (Count):** Add otjob.one over every confirmed otjob entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"otjob","field":"otjob.one","op":"sum_over"}`
- Cite: [i1040gi] p. 108, Schedule 1-A, line 14a, and the Qualified Overtime Compensation From More Than One Employer Worksheet (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ot_total`

- **Authored helper label:** This person's overtime worksheet column (b) total
- **Encoded (NonNegDollars):** Add otjob.col_b over every confirmed otjob entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"otjob","field":"otjob.col_b","op":"sum_over"}`
- Cite: [i1040gi] p. 108, Schedule 1-A, line 14a, and the Qualified Overtime Compensation From More Than One Employer Worksheet, line 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## rrta — `person.rrta`

- **Authored helper label:** Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or did you file Form CT-2 as an employee representative?
- **Encoded (Bool):** Input — Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or did you file Form CT-2 as an employee representative?
- Expr: `{"op":"input","source":"Do any wage statements report railroad retirement compensation or taxes (W-2 box 14), or did you file Form CT-2 as an employee representative?"}`
- Cite: [iw2w3] pp. 12–13, Railroad employers: RRTA compensation and taxes in box 14; boxes 3–7 are not used for RRTA (2025; printed date 2025-02-19; sha256 bfecbc99)

## (helper) — `person.sc_rrta_count`

- **Authored helper label:** Number of this person's Schedules C while this person has railroad retirement compensation
- **Encoded (Count):** Add sc.one over every confirmed sc entry for which helper "This business's owner has railroad retirement compensation" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.one","op":"sum_over","where":{"eq":["sc.rrta",{"const":true}],"op":"test"}}`
- Cite: [f1040sse] Schedule SE (2025), line 8a, "Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2) and railroad retirement (tier 1) compensation" (2025; created 2025-05-07; sha256 05bc2b3e)

## (gate) — `person.se_rrta`

- **Authored helper label:** Self-employment and railroad retirement compensation together
- **Encoded (Bool):** helper "Number of this person's Schedules C while this person has railroad retirement compensation" > 0 (a count)
- Note: Counted through the person's Schedules C, so the railroad question is asked only of a person with a business.
- Expr: `{"gt":["person.sc_rrta_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [f1040sse] Schedule SE (2025), line 8a, "Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2) and railroad retirement (tier 1) compensation" (2025; created 2025-05-07; sha256 05bc2b3e)

## employers — `person.employers`

- **Authored helper label:** Total w2.one for this person
- **Encoded (Count):** Add w2.one over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"w2","field":"w2.one","op":"sum_over"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## overcount — `person.overcount`

- **Authored helper label:** Number of employers that withheld more than the limit
- **Encoded (Count):** Add w2.one over every confirmed w2 entry for which helper "Did this employer withhold more than $10,918.20?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"w2","field":"w2.one","op":"sum_over","where":{"eq":["w2.over",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## over — `person.over`

- **Authored helper label:** Any employer withheld more than the limit
- **Encoded (Bool):** line overcount > 0 (a count)
- Expr: `{"gt":["person.overcount",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## wages — `person.wages`

- **Authored helper label:** Total w2.wages for this person
- **Encoded (NonNegDollars):** Add w2.wages over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Interpretation: amb.2025.ss_wages
- Expr: `{"collection":"w2","field":"w2.wages","op":"sum_over"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## withheld — `person.withheld`

- **Authored helper label:** Total w2.box4 for this person
- **Encoded (NonNegDollars):** Add w2.box4 over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"w2","field":"w2.box4","op":"sum_over"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.box1`

- **Authored helper label:** Total W-2 box 1 for this person
- **Encoded (NonNegDollars):** Add w2.box1 over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"w2","field":"w2.box1","op":"sum_over"}`
- Cite: [f1040] Form 1040 (2025), line 1a (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `person.box2`

- **Authored helper label:** Total W-2 box 2 for this person
- **Encoded (NonNegDollars):** Add w2.box2 over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"w2","field":"w2.box2","op":"sum_over"}`
- Cite: [f1040] p. 2, Payments and Refundable Credits, line 25a, "Federal income tax withheld from:", "Form(s) W-2" (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `person.f8919_firms`

- **Authored helper label:** Total of column (f) of this person's firms (Form 8919, lines 1 to 5)
- **Encoded (NonNegDollars):** Add f8919firm.wages over every confirmed f8919firm entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8919firm","field":"f8919firm.wages","op":"sum_over"}`
- Cite: [f8919] p. 1, line 6, "Total wages. Combine lines 1 through 5 in column (f)" (2025; created 2025-10-22 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 84102b12)

## (helper) — `person.f8919_wages`

- **Authored helper label:** This person's Form 8919 line 6 (the column (f) wages of the firms listed; zero for a person not paid by such a firm)
- **Encoded (NonNegDollars):** Choose — [scope helper "Wages from a firm that treated the worker as an independent contractor (Form 8919) (asked only after a Yes to pay not on a W-2; otherwise no)" = true → helper "Total of column (f) of this person's firms (Form 8919, lines 1 to 5)"] [scope helper "Wages from a firm that treated the worker as an independent contractor (Form 8919) (asked only after a Yes to pay not on a W-2; otherwise no)" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.contractor_pay_if_pay",{"const":true}],"op":"test"},"then":"person.f8919_firms"},{"guard":{"eq":["scope.contractor_pay_if_pay",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f8919] p. 1, line 6, "Total wages. Combine lines 1 through 5 in column (f)" (2025; created 2025-10-22 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 84102b12)

## (helper) — `person.f8919_any`

- **Authored helper label:** This person has wages on Form 8919 (line 6 more than zero)
- **Encoded (Bool):** helper "This person's Form 8919 line 6 (the column (f) wages of the firms listed; zero for a person not paid by such a firm)" > $0 (sales.zero)
- Expr: `{"gt":["person.f8919_wages",{"param":"sales.zero"}],"op":"test"}`
- Cite: [f8919] p. 1, Who must file, "You must file Form 8919 if all of the following apply" (2025; created 2025-10-22 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 84102b12)

## (helper) — `person.f8919_line10_figured`

- **Authored helper label:** This person's Form 8919 line 10 (wages subject to social security tax)
- **Encoded (NonNegDollars):** Add f8919.line10 over every confirmed f8919 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8919","field":"f8919.line10","op":"sum_over"}`
- Cite: [f1040sse] Schedule SE (2025), line 8c, "Wages subject to social security tax from Form 8919, line 10" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `person.f8919_line10`

- **Authored helper label:** This person's Form 8919 line 10 (wages subject to social security tax) (only when Form 8919 is filed; zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "This person has wages on Form 8919 (line 6 more than zero)" = true → helper "This person's Form 8919 line 10 (wages subject to social security tax)"] [helper "This person has wages on Form 8919 (line 6 more than zero)" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.f8919_any",{"const":true}],"op":"test"},"then":"person.f8919_line10_figured"},{"guard":{"eq":["person.f8919_any",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f1040sse] Schedule SE (2025), line 8c, "Wages subject to social security tax from Form 8919, line 10" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `person.f8919_tax_figured`

- **Authored helper label:** This person's Form 8919 line 13 (uncollected social security and Medicare tax on wages)
- **Encoded (NonNegDollars):** Add f8919.line13 over every confirmed f8919 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8919","field":"f8919.line13","op":"sum_over"}`
- Cite: [f1040s2] Schedule 2 (2025), line 6, "Uncollected social security and Medicare tax on wages. Attach Form 8919" (2025; created 2025-05-08; sha256 64d867b6)

## (helper) — `person.f8919_tax`

- **Authored helper label:** This person's Form 8919 line 13 (uncollected social security and Medicare tax on wages) (only when Form 8919 is filed; zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "This person has wages on Form 8919 (line 6 more than zero)" = true → helper "This person's Form 8919 line 13 (uncollected social security and Medicare tax on wages)"] [helper "This person has wages on Form 8919 (line 6 more than zero)" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.f8919_any",{"const":true}],"op":"test"},"then":"person.f8919_tax_figured"},{"guard":{"eq":["person.f8919_any",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f1040s2] Schedule 2 (2025), line 6, "Uncollected social security and Medicare tax on wages. Attach Form 8919" (2025; created 2025-05-08; sha256 64d867b6)

## (helper) — `person.f4137_rows_c`

- **Authored helper label:** Total of column (c) of this person's employer rows (Form 4137, line 1)
- **Encoded (NonNegDollars):** Add f4137row.col_c over every confirmed f4137row entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f4137row","field":"f4137row.col_c","op":"sum_over"}`
- Cite: [f4137] p. 1, line 2, "Total cash and charge tips you received in 2025. Add the amounts from line 1" (2025; created 2025-03-27 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 f2f7a822)

## (helper) — `person.f4137_col_c`

- **Authored helper label:** This person's Form 4137 line 2 (the column (c) tips of the employers listed; zero for a person with no unreported tips)
- **Encoded (NonNegDollars):** Choose — [scope helper "Tips not reported in full to an employer, or noncash tips (Form 4137 and line 1c) (asked only after a Yes to pay not on a W-2; otherwise no)" = true → helper "Total of column (c) of this person's employer rows (Form 4137, line 1)"] [scope helper "Tips not reported in full to an employer, or noncash tips (Form 4137 and line 1c) (asked only after a Yes to pay not on a W-2; otherwise no)" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.tips_unreported_if_pay",{"const":true}],"op":"test"},"then":"person.f4137_rows_c"},{"guard":{"eq":["scope.tips_unreported_if_pay",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f4137] p. 1, line 2, "Total cash and charge tips you received in 2025. Add the amounts from line 1" (2025; created 2025-03-27 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 f2f7a822)

## (helper) — `person.f4137_rows_d`

- **Authored helper label:** Total of column (d) of this person's employer rows (Form 4137, line 1)
- **Encoded (NonNegDollars):** Add f4137row.col_d over every confirmed f4137row entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f4137row","field":"f4137row.col_d","op":"sum_over"}`
- Cite: [f4137] p. 1, line 3, "Total cash and charge tips you reported to your employer(s) in 2025. Add the amounts from line 1" (2025; created 2025-03-27 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 f2f7a822)

## (helper) — `person.f4137_col_d`

- **Authored helper label:** This person's Form 4137 line 3 (the column (d) tips of the employers listed; zero for a person with no unreported tips)
- **Encoded (NonNegDollars):** Choose — [scope helper "Tips not reported in full to an employer, or noncash tips (Form 4137 and line 1c) (asked only after a Yes to pay not on a W-2; otherwise no)" = true → helper "Total of column (d) of this person's employer rows (Form 4137, line 1)"] [scope helper "Tips not reported in full to an employer, or noncash tips (Form 4137 and line 1c) (asked only after a Yes to pay not on a W-2; otherwise no)" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.tips_unreported_if_pay",{"const":true}],"op":"test"},"then":"person.f4137_rows_d"},{"guard":{"eq":["scope.tips_unreported_if_pay",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f4137] p. 1, line 3, "Total cash and charge tips you reported to your employer(s) in 2025. Add the amounts from line 1" (2025; created 2025-03-27 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 f2f7a822)

## (helper) — `person.f4137_under20`

- **Authored helper label:** Cash and charge tips you received but did not report to your employer because the total was less than $20 in a calendar month
- **Encoded (NonNegDollars):** Input — Of the cash and charge tips you did not report, how much did you not have to report because the tips at one job came to less than $20 in a calendar month? Zero if none.
- Expr: `{"op":"input","source":"Of the cash and charge tips you did not report, how much did you not have to report because the tips at one job came to less than $20 in a calendar month? Zero if none."}`
- Cite: [f4137] p. 2, Line 5, "Enter only the tips you weren’t required to report to your employer because the total received was less than $20 in a calendar month"; p. 2, Tips you must report to your employer, "the $20 rule applies separately to the tips you received while working for each employer" (2025; created 2025-03-27 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 f2f7a822)

## (gate) — `person.f4137_under20_if_rows`

- **Authored helper label:** Form 4137 line 5 (asked only of a person with an employer row on Form 4137; otherwise zero)
- **Encoded (NonNegDollars):** Choose — [helper "This person has tips on Form 4137 (line 2 more than zero)" = true → helper "Cash and charge tips you received but did not report to your employer because the total was less than $20 in a calendar month"] [helper "This person has tips on Form 4137 (line 2 more than zero)" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.f4137_filed",{"const":true}],"op":"test"},"then":"person.f4137_under20"},{"guard":{"eq":["person.f4137_filed",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f4137] p. 2, Line 5, "Enter only the tips you weren’t required to report to your employer because the total received was less than $20 in a calendar month" (2025; created 2025-03-27 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 f2f7a822)

## (helper) — `person.tips_gov`

- **Authored helper label:** Did you receive any of these unreported tips for work as a federal, state or local government employee whose pay was subject only to the 1.45% Medicare tax?
- **Encoded (Bool):** Input — Did you receive any of these unreported tips for work as a federal, state or local government employee whose pay was subject only to the 1.45% Medicare tax?
- Expr: `{"op":"input","source":"Did you receive any of these unreported tips for work as a federal, state or local government employee whose pay was subject only to the 1.45% Medicare tax?"}`
- Cite: [f4137] p. 2, Line 10, "If line 6 includes tips you received for work you did as a federal, state, or local government employee and your pay was subject only to the 1.45% Medicare tax" (2025; created 2025-03-27 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 f2f7a822)

## (gate) — `person.tips_gov_if_rows`

- **Authored helper label:** Unreported tips received as a government employee whose pay was subject only to the 1.45% Medicare tax (asked only of a person with an employer row on Form 4137; otherwise no)
- **Encoded (Bool):** Choose — [helper "This person has tips on Form 4137 (line 2 more than zero)" = true → helper "Did you receive any of these unreported tips for work as a federal, state or local government employee whose pay was subject only to the 1.45% Medicare tax?"] [helper "This person has tips on Form 4137 (line 2 more than zero)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.f4137_filed",{"const":true}],"op":"test"},"then":"person.tips_gov"},{"guard":{"eq":["person.f4137_filed",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [f4137] p. 2, Line 10, "If line 6 includes tips you received for work you did as a federal, state, or local government employee and your pay was subject only to the 1.45% Medicare tax" (2025; created 2025-03-27 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 f2f7a822)

## (helper) — `person.tips_noncash`

- **Authored helper label:** The value of noncash tips you received, such as tickets, passes, or other items of value
- **Encoded (NonNegDollars):** Input — What was the value of the tips you received in 2025 that were not money, such as tickets, passes or other items of value? Zero if none.
- Expr: `{"op":"input","source":"What was the value of the tips you received in 2025 that were not money, such as tickets, passes or other items of value? Zero if none."}`
- Cite: [i1040gi] p. 24, Line 1c, "Also, include the value of any noncash tips you received, such as tickets, passes, or other items of value. Although you don’t report these noncash tips to your employer, you must report them on line 1c" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `person.tips_noncash_if_unreported`

- **Authored helper label:** Noncash tips (asked only when unreported or noncash tips are reported for the return; otherwise zero)
- **Encoded (NonNegDollars):** Choose — [scope helper "Tips not reported in full to an employer, or noncash tips (Form 4137 and line 1c) (asked only after a Yes to pay not on a W-2; otherwise no)" = true → helper "The value of noncash tips you received, such as tickets, passes, or other items of value"] [scope helper "Tips not reported in full to an employer, or noncash tips (Form 4137 and line 1c) (asked only after a Yes to pay not on a W-2; otherwise no)" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.tips_unreported_if_pay",{"const":true}],"op":"test"},"then":"person.tips_noncash"},{"guard":{"eq":["scope.tips_unreported_if_pay",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 24, Line 1c, "Also, include the value of any noncash tips you received, such as tickets, passes, or other items of value" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.f4137_line4`

- **Authored helper label:** This person's Form 4137 line 4 (unreported cash and charge tips)
- **Encoded (NonNegDollars):** Add f4137.line4 over every confirmed f4137 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f4137","field":"f4137.line4","op":"sum_over"}`
- Cite: [f4137] p. 1, line 4, "Subtract line 3 from line 2. Include as income on Form 1040, 1040-SR, or 1040-NR, line 1c" (2025; created 2025-03-27 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 f2f7a822)

## (helper) — `person.f4137_line6_figured`

- **Authored helper label:** This person's Form 4137 line 6 (unreported tips subject to Medicare tax)
- **Encoded (NonNegDollars):** Add f4137.line6 over every confirmed f4137 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f4137","field":"f4137.line6","op":"sum_over"}`
- Cite: [f4137] p. 2, Line 6, "Enter this amount on Form 8959, line 2, if you’re required to file that form" (2025; created 2025-03-27 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 f2f7a822)

## (helper) — `person.f4137_line6`

- **Authored helper label:** This person's Form 4137 line 6 (unreported tips subject to Medicare tax) (only when Form 4137 is filed; zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "This person has tips on Form 4137 (line 2 more than zero)" = true → helper "This person's Form 4137 line 6 (unreported tips subject to Medicare tax)"] [helper "This person has tips on Form 4137 (line 2 more than zero)" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.f4137_filed",{"const":true}],"op":"test"},"then":"person.f4137_line6_figured"},{"guard":{"eq":["person.f4137_filed",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f4137] p. 2, Line 6, "Enter this amount on Form 8959, line 2, if you’re required to file that form" (2025; created 2025-03-27 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 f2f7a822)

## (helper) — `person.f4137_line10_figured`

- **Authored helper label:** This person's Form 4137 line 10 (unreported tips subject to social security tax)
- **Encoded (NonNegDollars):** Add f4137.line10 over every confirmed f4137 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f4137","field":"f4137.line10","op":"sum_over"}`
- Cite: [f1040sse] Schedule SE (2025), line 8b, "Unreported tips subject to social security tax from Form 4137, line 10" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `person.f4137_line10`

- **Authored helper label:** This person's Form 4137 line 10 (unreported tips subject to social security tax) (only when Form 4137 is filed; zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "This person has tips on Form 4137 (line 2 more than zero)" = true → helper "This person's Form 4137 line 10 (unreported tips subject to social security tax)"] [helper "This person has tips on Form 4137 (line 2 more than zero)" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.f4137_filed",{"const":true}],"op":"test"},"then":"person.f4137_line10_figured"},{"guard":{"eq":["person.f4137_filed",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f1040sse] Schedule SE (2025), line 8b, "Unreported tips subject to social security tax from Form 4137, line 10" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `person.f4137_tax_figured`

- **Authored helper label:** This person's Form 4137 line 13 (social security and Medicare tax on unreported tips)
- **Encoded (NonNegDollars):** Add f4137.line13 over every confirmed f4137 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f4137","field":"f4137.line13","op":"sum_over"}`
- Cite: [f1040s2] Schedule 2 (2025), line 5, "Social security and Medicare tax on unreported tip income. Attach Form 4137" (2025; created 2025-05-08; sha256 64d867b6)

## (helper) — `person.f4137_tax`

- **Authored helper label:** This person's Form 4137 line 13 (social security and Medicare tax on unreported tips) (only when Form 4137 is filed; zero otherwise)
- **Encoded (NonNegDollars):** Choose — [helper "This person has tips on Form 4137 (line 2 more than zero)" = true → helper "This person's Form 4137 line 13 (social security and Medicare tax on unreported tips)"] [helper "This person has tips on Form 4137 (line 2 more than zero)" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.f4137_filed",{"const":true}],"op":"test"},"then":"person.f4137_tax_figured"},{"guard":{"eq":["person.f4137_filed",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f1040s2] Schedule 2 (2025), line 5, "Social security and Medicare tax on unreported tip income. Attach Form 4137" (2025; created 2025-05-08; sha256 64d867b6)

## (helper) — `person.line1c`

- **Authored helper label:** This person's tip income not reported on line 1a (Form 4137 line 4 and noncash tips)
- **Encoded (NonNegDollars):** Add helper "This person's Form 4137 line 4 (unreported cash and charge tips)" and helper "Noncash tips (asked only when unreported or noncash tips are reported for the return; otherwise zero)".
- Expr: `{"of":["person.f4137_line4","person.tips_noncash_if_unreported"],"op":"sum"}`
- Cite: [i1040gi] p. 24, Line 1c, "This should include any tip income you didn’t report to your employer", "Also, include the value of any noncash tips you received" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `person.f4137_filed`

- **Authored helper label:** This person has tips on Form 4137 (line 2 more than zero)
- **Encoded (Bool):** helper "This person's Form 4137 line 2 (the column (c) tips of the employers listed; zero for a person with no unreported tips)" > $0 (sales.zero)
- Expr: `{"gt":["person.f4137_col_c",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 104, Qualified Tips From More Than One Employer Worksheet, column (c) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.household_wages`

- **Authored helper label:** Wages you received as a household employee that were not reported on Form(s) W-2
- **Encoded (NonNegDollars):** Input — How much were you paid in 2025 for work in someone else's home by households that did not give a W-2 for it? Zero if none.
- Expr: `{"op":"input","source":"How much were you paid in 2025 for work in someone else's home by households that did not give a W-2 for it? Zero if none."}`
- Cite: [i1040gi] p. 24, Line 1b, "Enter the total of your wages received as a household employee that was not reported on Form(s) W-2", "An employer isn’t required to provide a Form W-2 to you if they paid you wages of less than $2,800 in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `person.household_wages_if_pay`

- **Authored helper label:** Household employee wages not on a W-2 (asked only when such wages are reported for the return; otherwise zero)
- **Encoded (NonNegDollars):** Choose — [scope helper "Wages as a household employee not reported on a W-2 (asked only after a Yes to pay not on a W-2; otherwise no)" = true → helper "Wages you received as a household employee that were not reported on Form(s) W-2"] [scope helper "Wages as a household employee not reported on a W-2 (asked only after a Yes to pay not on a W-2; otherwise no)" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.household_pay_if_pay",{"const":true}],"op":"test"},"then":"person.household_wages"},{"guard":{"eq":["scope.household_pay_if_pay",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 24, Line 1b, "Enter the total of your wages received as a household employee that was not reported on Form(s) W-2" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.strike`

- **Authored helper label:** Strike or lockout benefits you received (other than bona fide gifts)
- **Encoded (NonNegDollars):** Input — How much did you get in 2025 in strike or lockout benefits from a union? Leave out true gifts. Zero if none.
- Expr: `{"op":"input","source":"How much did you get in 2025 in strike or lockout benefits from a union? Leave out true gifts. Zero if none."}`
- Cite: [i1040gi] p. 24, Line 1h, "The following types of income must be included in the total on line 1h", "Strike or lockout benefits (other than bona fide gifts)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `person.strike_if_pay`

- **Authored helper label:** Strike or lockout benefits (asked only when such benefits are reported for the return; otherwise zero)
- **Encoded (NonNegDollars):** Choose — [scope helper "Strike or lockout benefits (asked only after a Yes to pay not on a W-2; otherwise no)" = true → helper "Strike or lockout benefits you received (other than bona fide gifts)"] [scope helper "Strike or lockout benefits (asked only after a Yes to pay not on a W-2; otherwise no)" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.strike_pay_if_pay",{"const":true}],"op":"test"},"then":"person.strike"},{"guard":{"eq":["scope.strike_pay_if_pay",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 24, Line 1h, "Strike or lockout benefits (other than bona fide gifts)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.mw_box1`

- **Authored helper label:** Nontaxable Medicaid waiver payments reported in box 1 of Form(s) W-2
- **Encoded (NonNegDollars):** Input — How much of the Medicaid pay you received in 2025 for caring for someone who lived with you in your home appears in box 1 of your W-2s? Zero if none.
- Expr: `{"op":"input","source":"How much of the Medicaid pay you received in 2025 for caring for someone who lived with you in your home appears in box 1 of your W-2s? Zero if none."}`
- Cite: [i1040gi] p. 92, Line 8s, "Nontaxable amount of Medicaid waiver payments included on Form 1040, line 1a or 1d", "If nontaxable payments were reported to you in box 1 of Form(s) W-2, report the amount on Form 1040 or 1040-SR, line 1a" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `person.mw_box1_if_mw`

- **Authored helper label:** Medicaid waiver payments in W-2 box 1 (asked only when Medicaid waiver payments are reported for the return; otherwise zero)
- **Encoded (NonNegDollars):** Choose — [scope helper "In 2025, did a state Medicaid program pay you (or, on a joint return, your spouse) to care for someone who lives in your home?" = true → helper "Nontaxable Medicaid waiver payments reported in box 1 of Form(s) W-2"] [scope helper "In 2025, did a state Medicaid program pay you (or, on a joint return, your spouse) to care for someone who lives in your home?" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.medicaid_waiver",{"const":true}],"op":"test"},"then":"person.mw_box1"},{"guard":{"eq":["scope.medicaid_waiver",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 92, Line 8s, "Nontaxable amount of Medicaid waiver payments included on Form 1040, line 1a or 1d", "If nontaxable payments were reported to you in box 1 of Form(s) W-2, report the amount on Form 1040 or 1040-SR, line 1a" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.mw_not_box1`

- **Authored helper label:** Nontaxable Medicaid waiver payments not reported in box 1 of a Form W-2
- **Encoded (NonNegDollars):** Input — How much of that Medicaid pay is not in box 1 of a W-2: shown only in box 12 with code II, on a Form 1099-MISC or 1099-NEC, or on no form? Zero if none.
- Expr: `{"op":"input","source":"How much of that Medicaid pay is not in box 1 of a W-2: shown only in box 12 with code II, on a Form 1099-MISC or 1099-NEC, or on no form? Zero if none."}`
- Cite: [i1040gi] p. 24, Line 1d, "Also enter the total of your taxable and nontaxable Medicaid waiver payments that were not reported on Form(s) W-2, or not reported in box 1 of Form(s) W-2"; p. 92, Line 8s, "Your nontaxable Medicaid waiver payments should be reported to you on Form(s) W-2 in box 12, Code II" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `person.mw_not_box1_if_mw`

- **Authored helper label:** Medicaid waiver payments not in W-2 box 1 (asked only when Medicaid waiver payments are reported for the return; otherwise zero)
- **Encoded (NonNegDollars):** Choose — [scope helper "In 2025, did a state Medicaid program pay you (or, on a joint return, your spouse) to care for someone who lives in your home?" = true → helper "Nontaxable Medicaid waiver payments not reported in box 1 of a Form W-2"] [scope helper "In 2025, did a state Medicaid program pay you (or, on a joint return, your spouse) to care for someone who lives in your home?" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["scope.medicaid_waiver",{"const":true}],"op":"test"},"then":"person.mw_not_box1"},{"guard":{"eq":["scope.medicaid_waiver",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 24, Line 1d, "Also enter the total of your taxable and nontaxable Medicaid waiver payments that were not reported on Form(s) W-2, or not reported in box 1 of Form(s) W-2" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.mw_has_not_box1`

- **Authored helper label:** Medicaid waiver payments not in W-2 box 1 are more than zero
- **Encoded (Bool):** helper "Medicaid waiver payments not in W-2 box 1 (asked only when Medicaid waiver payments are reported for the return; otherwise zero)" > $0 (sales.zero)
- Expr: `{"gt":["person.mw_not_box1_if_mw",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 24, Line 1d, "Also enter the total of your taxable and nontaxable Medicaid waiver payments that were not reported on Form(s) W-2, or not reported in box 1 of Form(s) W-2" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.mw_1099`

- **Authored helper label:** Medicaid waiver payments reported on Form 1099-MISC or Form 1099-NEC
- **Encoded (NonNegDollars):** Input — How much of that was reported on a Form 1099-MISC or 1099-NEC? Zero if none.
- Expr: `{"op":"input","source":"How much of that was reported on a Form 1099-MISC or 1099-NEC? Zero if none."}`
- Cite: [i1040gi] p. 24, Line 1d, "If you do not have a separate trade or business of providing these services, enter on Form 1040, line 1d, your Medicaid waiver payments reported on Form 1099-MISC or Form 1099-NEC" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `person.mw_1099_if_not_box1`

- **Authored helper label:** Medicaid waiver payments on Form 1099-MISC or 1099-NEC (asked only when some payments are not in W-2 box 1; otherwise zero)
- **Encoded (NonNegDollars):** Choose — [helper "Medicaid waiver payments not in W-2 box 1 are more than zero" = true → helper "Medicaid waiver payments reported on Form 1099-MISC or Form 1099-NEC"] [helper "Medicaid waiver payments not in W-2 box 1 are more than zero" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.mw_has_not_box1",{"const":true}],"op":"test"},"then":"person.mw_1099"},{"guard":{"eq":["person.mw_has_not_box1",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 24, Line 1d, "If you do not have a separate trade or business of providing these services, enter on Form 1040, line 1d, your Medicaid waiver payments reported on Form 1099-MISC or Form 1099-NEC" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.mw_has_1099`

- **Authored helper label:** Medicaid waiver payments on Form 1099-MISC or 1099-NEC are more than zero
- **Encoded (Bool):** helper "Medicaid waiver payments on Form 1099-MISC or 1099-NEC (asked only when some payments are not in W-2 box 1; otherwise zero)" > $0 (sales.zero)
- Expr: `{"gt":["person.mw_1099_if_not_box1",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 24, Line 1d, "If you do not have a separate trade or business of providing these services, enter on Form 1040, line 1d, your Medicaid waiver payments reported on Form 1099-MISC or Form 1099-NEC" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `person.mw_1099_over`

- **Authored helper label:** The Medicaid waiver payments on Form 1099 are more than the payments not in W-2 box 1
- **Encoded (Bool):** helper "Medicaid waiver payments on Form 1099-MISC or 1099-NEC (asked only when some payments are not in W-2 box 1; otherwise zero)" > helper "Medicaid waiver payments not in W-2 box 1 (asked only when Medicaid waiver payments are reported for the return; otherwise zero)"
- Expr: `{"gt":["person.mw_1099_if_not_box1","person.mw_not_box1_if_mw"],"op":"test"}`
- Cite: [i1040gi] p. 24, Line 1d, "If you do not have a separate trade or business of providing these services, enter on Form 1040, line 1d, your Medicaid waiver payments reported on Form 1099-MISC or Form 1099-NEC" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.mw_business`

- **Authored helper label:** Do you run a business of providing home care services, as a sole proprietor?
- **Encoded (Bool):** Input — Do you run a business of your own that provides home care, with this pay reported on a business schedule (Schedule C)?
- Expr: `{"op":"input","source":"Do you run a business of your own that provides home care, with this pay reported on a business schedule (Schedule C)?"}`
- Cite: [i1040gi] p. 24, Line 1d, "If you are a sole proprietor in a business of providing home care services, see the Schedule C instructions for how to report these amounts" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `person.mw_business_if_1099`

- **Authored helper label:** A home-care business of your own (asked only with Medicaid waiver payments on Form 1099; otherwise no)
- **Encoded (Bool):** Choose — [helper "Medicaid waiver payments on Form 1099-MISC or 1099-NEC are more than zero" = true → helper "Do you run a business of providing home care services, as a sole proprietor?"] [helper "Medicaid waiver payments on Form 1099-MISC or 1099-NEC are more than zero" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.mw_has_1099",{"const":true}],"op":"test"},"then":"person.mw_business"},{"guard":{"eq":["person.mw_has_1099",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 24, Line 1d, "If you are a sole proprietor in a business of providing home care services, see the Schedule C instructions for how to report these amounts" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.mw_total`

- **Authored helper label:** This person's Medicaid waiver payments (in W-2 box 1 and not in box 1)
- **Encoded (NonNegDollars):** Add helper "Medicaid waiver payments in W-2 box 1 (asked only when Medicaid waiver payments are reported for the return; otherwise zero)" and helper "Medicaid waiver payments not in W-2 box 1 (asked only when Medicaid waiver payments are reported for the return; otherwise zero)".
- Expr: `{"of":["person.mw_box1_if_mw","person.mw_not_box1_if_mw"],"op":"sum"}`
- Cite: [i1040gi] p. 92, Line 8s, "Nontaxable amount of Medicaid waiver payments included on Form 1040, line 1a or 1d", "If nontaxable payments were reported to you in box 1 of Form(s) W-2, report the amount on Form 1040 or 1040-SR, line 1a" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.mw_paid`

- **Authored helper label:** This person had Medicaid waiver payments
- **Encoded (Bool):** helper "This person's Medicaid waiver payments (in W-2 box 1 and not in box 1)" > $0 (sales.zero)
- Expr: `{"gt":["person.mw_total",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 92, Line 8s, "Nontaxable amount of Medicaid waiver payments included on Form 1040, line 1a or 1d", "If nontaxable payments were reported to you in box 1 of Form(s) W-2, report the amount on Form 1040 or 1040-SR, line 1a" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.mw_earned`

- **Authored helper label:** Do you choose to include your nontaxable Medicaid waiver payments in earned income for purposes of claiming a credit or other tax benefit?
- **Encoded (Bool):** Input — Do you choose to count this Medicaid pay as earned income? It is not taxed either way; counting it can raise credits such as the earned income credit.
- Expr: `{"op":"input","source":"Do you choose to count this Medicaid pay as earned income? It is not taxed either way; counting it can raise credits such as the earned income credit."}`
- Cite: [i1040gi] p. 24, Line 1d, "if you choose to include nontaxable payments in earned income for purposes of claiming a credit or other tax benefit", "If you and your spouse both received nontaxable Medicaid waiver payments during the year, you and your spouse can make different choices about including payments in earned income" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `person.mw_earned_if_paid`

- **Authored helper label:** The choice to count Medicaid waiver payments as earned income (asked only of a person with such payments; otherwise no)
- **Encoded (Bool):** Choose — [helper "This person had Medicaid waiver payments" = true → helper "Do you choose to include your nontaxable Medicaid waiver payments in earned income for purposes of claiming a credit or other tax benefit?"] [helper "This person had Medicaid waiver payments" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.mw_paid",{"const":true}],"op":"test"},"then":"person.mw_earned"},{"guard":{"eq":["person.mw_paid",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 24, Line 1d, "if you choose to include nontaxable payments in earned income for purposes of claiming a credit or other tax benefit", "If you and your spouse both received nontaxable Medicaid waiver payments during the year, you and your spouse can make different choices about including payments in earned income" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.mw_other`

- **Authored helper label:** Medicaid waiver payments not in W-2 box 1 and not on Form 1099 (shown only in box 12 with code II, or on no form)
- **Encoded (NonNegDollars):** Subtract helper "Medicaid waiver payments on Form 1099-MISC or 1099-NEC (asked only when some payments are not in W-2 box 1; otherwise zero)" from helper "Medicaid waiver payments not in W-2 box 1 (asked only when Medicaid waiver payments are reported for the return; otherwise zero)". If zero or less, enter -0-.
- Expr: `{"from":"person.mw_not_box1_if_mw","op":"subtract_floor0","take":"person.mw_1099_if_not_box1"}`
- Cite: [i1040gi] p. 92, Line 8s, "If you did not receive a Form W-2 for nontaxable payments, or you received nontaxable payments that you didn’t report on line 1a, and choose to include nontaxable amounts in earned income for purposes of claiming a credit or other tax benefit, report the amount on Form 1040 or 1040-SR, line 1d" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.mw_other_1d`

- **Authored helper label:** Medicaid waiver payments not in W-2 box 1 or on Form 1099 that go on line 1d (only when chosen as earned income; otherwise zero)
- **Encoded (NonNegDollars):** Choose — [helper "The choice to count Medicaid waiver payments as earned income (asked only of a person with such payments; otherwise no)" = true → helper "Medicaid waiver payments not in W-2 box 1 and not on Form 1099 (shown only in box 12 with code II, or on no form)"] [helper "The choice to count Medicaid waiver payments as earned income (asked only of a person with such payments; otherwise no)" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.mw_earned_if_paid",{"const":true}],"op":"test"},"then":"person.mw_other"},{"guard":{"eq":["person.mw_earned_if_paid",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 92, Line 8s, "and choose to include nontaxable amounts in earned income for purposes of claiming a credit or other tax benefit, report the amount on Form 1040 or 1040-SR, line 1d" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.line1d`

- **Authored helper label:** This person's Medicaid waiver payments on Form 1040 line 1d
- **Encoded (NonNegDollars):** Add helper "Medicaid waiver payments on Form 1099-MISC or 1099-NEC (asked only when some payments are not in W-2 box 1; otherwise zero)" and helper "Medicaid waiver payments not in W-2 box 1 or on Form 1099 that go on line 1d (only when chosen as earned income; otherwise zero)".
- **Refusal:** when person.mw_1099_over is true, cannot complete Medicaid waiver payments on Form 1099 more than the payments not in W-2 box 1. The Medicaid pay reported on Form 1099-MISC or 1099-NEC is part of the pay not in box 1 of a W-2, so it cannot be more. Check the two amounts. Cite: [i1040gi] p. 24, Line 1d, "If you do not have a separate trade or business of providing these services, enter on Form 1040, line 1d, your Medicaid waiver payments reported on Form 1099-MISC or Form 1099-NEC" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when person.mw_business_if_1099 is true, cannot complete Medicaid waiver payments in a home-care business (Schedule C). A sole proprietor in a business of providing home care services reports these payments as the Schedule C instructions say; this tool does not prepare that. Cite: [i1040gi] p. 24, Line 1d, "If you are a sole proprietor in a business of providing home care services, see the Schedule C instructions for how to report these amounts" (2025; printed date 2026-02-25; sha256 482e9c48)
- Interpretation: amb.2025.mw_all_nontaxable
- Expr: `{"of":["person.mw_1099_if_not_box1","person.mw_other_1d"],"op":"sum"}`
- Cite: [i1040gi] p. 24, Line 1d, "enter on Form 1040, line 1d, your Medicaid waiver payments reported on Form 1099-MISC or Form 1099-NEC", "Also enter the total of your taxable and nontaxable Medicaid waiver payments that were not reported on Form(s) W-2, or not reported in box 1 of Form(s) W-2, if you choose to include nontaxable payments in earned income" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.line8s`

- **Authored helper label:** This person's nontaxable Medicaid waiver payments included on Form 1040 line 1a or 1d (Schedule 1 line 8s)
- **Encoded (NonNegDollars):** Add helper "Medicaid waiver payments in W-2 box 1 (asked only when Medicaid waiver payments are reported for the return; otherwise zero)" and helper "This person's Medicaid waiver payments on Form 1040 line 1d".
- Expr: `{"of":["person.mw_box1_if_mw","person.line1d"],"op":"sum"}`
- Cite: [i1040gi] p. 92, Line 8s, "Then, on line 8s, enter the total amount of the nontaxable payments reported on Form 1040 or 1040-SR, line 1a or 1d" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.mw_not_earned`

- **Authored helper label:** This person's Medicaid waiver payments on Schedule 1 line 8s not chosen as earned income
- **Encoded (NonNegDollars):** Choose — [helper "The choice to count Medicaid waiver payments as earned income (asked only of a person with such payments; otherwise no)" = true → line zero] [helper "The choice to count Medicaid waiver payments as earned income (asked only of a person with such payments; otherwise no)" = false → helper "This person's nontaxable Medicaid waiver payments included on Form 1040 line 1a or 1d (Schedule 1 line 8s)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.mw_earned_if_paid",{"const":true}],"op":"test"},"then":"person.zero"},{"guard":{"eq":["person.mw_earned_if_paid",{"const":false}],"op":"test"},"then":"person.line8s"}],"op":"choose"}`
- Cite: [i1040gi] p. 42, Step 5, "Enter the Medicaid waiver payment amounts excluded from income on Schedule 1, line 8s, unless you choose to include these amounts in earned income, in which case enter -0-" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.earned_not_w2`

- **Authored helper label:** This person's pay on Form 1040 lines 1b, 1c, 1d, 1g and 1h (wages, tips and other earned income not in W-2 box 1)
- **Encoded (NonNegDollars):** Add helper "Household employee wages not on a W-2 (asked only when such wages are reported for the return; otherwise zero)", helper "This person's tip income not reported on line 1a (Form 4137 line 4 and noncash tips)", helper "This person's Medicaid waiver payments on Form 1040 line 1d", helper "This person's Form 8919 line 6 (the column (f) wages of the firms listed; zero for a person not paid by such a firm)", and helper "This person's other earned income on Form 1040 line 1h (strike or lockout benefits and disability pensions paid before the minimum retirement age)".
- Expr: `{"of":["person.household_wages_if_pay","person.line1c","person.line1d","person.f8919_wages","person.line1h"],"op":"sum"}`
- Cite: [i2441] p. 4, Lines 4 and 5, "The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z" (2025; sha256 86f0669e)

## (helper) — `person.ira_amount_a`

- **Authored helper label:** IRA distributions on this person's Forms 1099-R (line 4a amounts)
- **Encoded (NonNegDollars):** Add retirement.amount_a over every confirmed retirement entry for which helper "IRA distribution (lines 4a and 4b)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.amount_a","op":"sum_over","where":{"eq":["retirement.is_ira",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] pp. 26-27, Lines 4a and 4b (total distributions where an exception applies; 'More than one distribution') (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_taxable`

- **Authored helper label:** Taxable IRA distributions on this person's Forms 1099-R (line 4b amounts)
- **Encoded (NonNegDollars):** Add retirement.taxable over every confirmed retirement entry for which helper "IRA distribution (lines 4a and 4b)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.taxable","op":"sum_over","where":{"eq":["retirement.is_ira",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 27, line 4b, 'figure the taxable amount of each distribution and enter the total of the taxable amounts on line 4b' (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_rollovers`

- **Authored helper label:** Number of this person's IRA distributions with a rollover
- **Encoded (Count):** Add retirement.one over every confirmed retirement entry for which helper "IRA distribution (lines 4a and 4b)" = true and helper "Part or all of the distribution was rolled over (an amount rolled over, or a direct rollover, code G)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.one","op":"sum_over","where":{"all":[{"eq":["retirement.is_ira",{"const":true}],"op":"test"},{"eq":["retirement.has_rollover",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] p. 27, Exception 1, 'Also check box 1 on line 4c' (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.plan_amount_a`

- **Authored helper label:** Pension and annuity distributions on this person's Forms 1099-R (line 5a amounts)
- **Encoded (NonNegDollars):** Add retirement.amount_a over every confirmed retirement entry for which helper "IRA distribution (lines 4a and 4b)" = false and helper "A disability pension paid wholly before the minimum retirement age: its taxable amount is wages on Form 1040, line 1h, not a pension on lines 5a and 5b" = false, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.amount_a","op":"sum_over","where":{"all":[{"eq":["retirement.is_ira",{"const":false}],"op":"test"},{"eq":["retirement.dis_wages",{"const":false}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] pp. 28-30, Lines 5a and 5b (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.plan_taxable`

- **Authored helper label:** Taxable pension and annuity distributions on this person's Forms 1099-R (line 5b amounts)
- **Encoded (NonNegDollars):** Add retirement.taxable over every confirmed retirement entry for which helper "IRA distribution (lines 4a and 4b)" = false and helper "A disability pension paid wholly before the minimum retirement age: its taxable amount is wages on Form 1040, line 1h, not a pension on lines 5a and 5b" = false, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.taxable","op":"sum_over","where":{"all":[{"eq":["retirement.is_ira",{"const":false}],"op":"test"},{"eq":["retirement.dis_wages",{"const":false}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] pp. 28-30, Lines 5a and 5b; p. 29, Simplified Method Worksheet, 'Enter the total of the taxable parts on Form 1040 or 1040-SR, line 5b' (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.dis_wages`

- **Authored helper label:** Taxable disability pensions on this person's Forms 1099-R paid before the minimum retirement age (line 1h amounts)
- **Encoded (NonNegDollars):** Add retirement.taxable over every confirmed retirement entry for which helper "A disability pension paid wholly before the minimum retirement age: its taxable amount is wages on Form 1040, line 1h, not a pension on lines 5a and 5b" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.taxable","op":"sum_over","where":{"eq":["retirement.dis_wages",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 25, "Disability pensions shown on Form 1099-R if you haven’t reached the minimum retirement age set by your employer"; p575 p. 6, Disability Pensions, "You must report your taxable disability payments as wages on Form 1040, 1040-SR, or 1040-NR, line 1h, until you reach minimum retirement age" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.line1h`

- **Authored helper label:** This person's other earned income on Form 1040 line 1h (strike or lockout benefits and disability pensions paid before the minimum retirement age)
- **Encoded (NonNegDollars):** Add helper "Strike or lockout benefits (asked only when such benefits are reported for the return; otherwise zero)" and helper "Taxable disability pensions on this person's Forms 1099-R paid before the minimum retirement age (line 1h amounts)".
- Expr: `{"of":["person.strike_if_pay","person.dis_wages"],"op":"sum"}`
- Cite: [i1040gi] p. 24, Line 1h, "The following types of income must be included in the total on line 1h", "Strike or lockout benefits (other than bona fide gifts)"; p. 25, "Disability pensions shown on Form 1099-R if you haven’t reached the minimum retirement age set by your employer" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.plan_rollovers`

- **Authored helper label:** Number of this person's pension distributions with a rollover
- **Encoded (Count):** Add retirement.one over every confirmed retirement entry for which helper "IRA distribution (lines 4a and 4b)" = false and helper "Part or all of the distribution was rolled over (an amount rolled over, or a direct rollover, code G)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.one","op":"sum_over","where":{"all":[{"eq":["retirement.is_ira",{"const":false}],"op":"test"},{"eq":["retirement.has_rollover",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] p. 30, Rollovers, 'Also check box 1 on line 5c' (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.sav_dist`

- **Authored helper label:** Distributions received in 2025 that Form 8880 line 4 counts, on this person's Forms 1099-R
- **Encoded (NonNegDollars):** Add retirement.sav_amount over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.sav_amount","op":"sum_over"}`
- Cite: [f8880] p. 2, Line 4, "Enter the total amount of distributions you, and your spouse if filing jointly, received after 2022 and before the due date of your 2025 return (including extensions)" (2025; created 2025-11-04; sha256 ba2b2877)

## eligible — `person.eligible`

- **Authored helper label:** More than one employer and total social security wages over $176,100
- **Encoded (Bool):** line employers > 1 (a count) and line wages > $176,100 (ss.base)
- Expr: `{"all":[{"gt":["person.employers",{"const":1,"type":"Count"}],"op":"test"},{"gt":["person.wages",{"param":"ss.base"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## excess — `person.excess`

- **Authored helper label:** Withholding above $10,918.20, if any
- **Encoded (NonNegDollars):** Subtract $10,918.20 (ss.limit) from line withheld. If zero or less, enter -0-.
- Expr: `{"from":"person.withheld","op":"subtract_floor0","take":{"param":"ss.limit"}}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## zero — `person.zero`

- **Authored helper label:** No excess credit
- **Encoded (NonNegDollars):** Enter $0 (ss.zero).
- Expr: `{"op":"param","ref":"ss.zero"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## credit — `person.credit`

- **Authored helper label:** Excess social security tax withheld, figured separately for this person
- **Encoded (NonNegDollars):** Choose — [line eligible = true → line excess] [line eligible = false → line zero]
- **Refusal:** when person.rrta is true, cannot complete Schedule 3 line 11 (RRTA path). This stage handles Social Security only. Use the railroad retirement instructions; excess Tier 2 tax uses Form 843 rather than Form 1040. Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when person.over is true, cannot complete Form 843. An employer withheld more than $10,918.20. Ask that employer to adjust the tax. If the employer does not adjust the overcollection, you can file a refund claim using Form 843. This tool cannot complete the credit until the overcollection is resolved. Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"alternatives":[{"guard":{"eq":["person.eligible",{"const":true}],"op":"test"},"then":"person.excess"},{"guard":{"eq":["person.eligible",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 117, Schedule 3 line 11 — Excess Social Security and Tier 1 RRTA Tax Withheld (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.medicare5`

- **Authored helper label:** Total W-2 box 5 for this person
- **Encoded (NonNegDollars):** Add w2.box5 over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when person.rrta is true, cannot complete Form 8959 RRTA computation. RRTA compensation is outside the supported wage-only path. Cite: [f8959] Form 8959 (2025), lines 1–24; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004)
- Expr: `{"collection":"w2","field":"w2.box5","op":"sum_over"}`
- Cite: [f8959] Form 8959 (2025), line 1, "Medicare wages and tips from Form W-2, box 5", "enter the total of the amounts from box 5"; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004)

## (helper) — `person.medicare6`

- **Authored helper label:** Total W-2 box 6 for this person
- **Encoded (NonNegDollars):** Add w2.box6 over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- **Refusal:** when person.rrta is true, cannot complete Form 8959 RRTA computation. RRTA compensation is outside the supported wage-only path. Cite: [f8959] Form 8959 (2025), lines 1–24; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004)
- Expr: `{"collection":"w2","field":"w2.box6","op":"sum_over"}`
- Cite: [f8959] Form 8959 (2025), line 19, "Medicare tax withheld from Form W-2, box 6", "enter the total of the amounts from box 6"; i8959 pp. 1–3 (2025; created 2025-04-30; sha256 13e64004)

## (helper) — `person.sc_count`

- **Authored helper label:** Number of Schedules C for this person
- **Encoded (Count):** Add sc.one over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.one","op":"sum_over"}`
- Cite: [i1040sc] p. 14, Line 31; i4562 p. 4, Part I (2025; sha256 b5536db9)

## (helper) — `person.ho_count`

- **Authored helper label:** Number of this person's Schedules C that claim the business use of the home
- **Encoded (Count):** Add sc.one over every confirmed sc entry for which helper "Do you claim a deduction for business use of your home for this business?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.one","op":"sum_over","where":{"eq":["sc.ho_uses",{"const":true}],"op":"test"}}`
- Cite: [i1040sc] p. 10, Simplified method, "You are limited to a maximum of 300 square feet for all of the businesses you conduct in your home that qualify for this deduction" (2025; sha256 b5536db9)

## (helper) — `person.sc_credit_count`

- **Authored helper label:** Number of this person's Schedules C that claim a general business credit (Form 3800); a refusal of that Schedule C (its line 1) is carried
- **Encoded (Count):** Add sc.one over every confirmed sc entry for which helper "Does this business claim a general business credit for 2025 (Form 3800), other than the employment credits asked about with the special items of this Schedule C?" = true and line 1 (sc.line1) ≥ $0 (sales.zero), within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.one","op":"sum_over","where":{"all":[{"eq":["sc.business_credit",{"const":true}],"op":"test"},{"ge":["sc.line1",{"param":"sales.zero"}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] p. 116, Lines 6a Through 6z, "See Form 3800 or Pub. 334" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.sc_fuel_count`

- **Authored helper label:** Number of this person's Schedules C that claim the credit for federal tax paid on fuels (Form 4136); a refusal of that Schedule C (its line 1) is carried
- **Encoded (Count):** Add sc.one over every confirmed sc entry for which helper "Does this business claim a credit for federal excise tax paid on fuel used for a nontaxable purpose, such as an off-highway business use (Form 4136)?" = true and line 1 (sc.line1) ≥ $0 (sales.zero), within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.one","op":"sum_over","where":{"all":[{"eq":["sc.fuel_credit",{"const":true}],"op":"test"},{"ge":["sc.line1",{"param":"sales.zero"}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] p. 117, Line 12, "Attach Form 4136" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.mq_q4`

- **Authored helper label:** Mid-quarter test basis, fourth quarter, this person
- **Encoded (NonNegDollars):** Add sc.mq_q4 over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.mq_q4","op":"sum_over"}`
- Cite: [i1040sc] p. 14, Line 31; i4562 p. 4, Part I (2025; sha256 b5536db9)

## (helper) — `person.mq_total`

- **Authored helper label:** Mid-quarter test basis, 2025, this person
- **Encoded (NonNegDollars):** Add sc.mq_total over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.mq_total","op":"sum_over"}`
- Cite: [i1040sc] p. 14, Line 31; i4562 p. 4, Part I (2025; sha256 b5536db9)

## (helper) — `person.cost179`

- **Authored helper label:** Cost of section 179 property, this person
- **Encoded (NonNegDollars):** Add sc.cost179 over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.cost179","op":"sum_over"}`
- Cite: [i1040sc] p. 14, Line 31; i4562 p. 4, Part I (2025; sha256 b5536db9)

## (helper) — `person.s179_nonlisted`

- **Authored helper label:** Section 179 elected, other than listed property, this person
- **Encoded (NonNegDollars):** Add sc.f6 over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.f6","op":"sum_over"}`
- Cite: [i1040sc] p. 14, Line 31; i4562 p. 4, Part I (2025; sha256 b5536db9)

## (helper) — `person.s179_listed`

- **Authored helper label:** Section 179 elected on listed property, this person
- **Encoded (NonNegDollars):** Add sc.f29 over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.f29","op":"sum_over"}`
- Cite: [i1040sc] p. 14, Line 31; i4562 p. 4, Part I (2025; sha256 b5536db9)

## (helper) — `person.income179`

- **Authored helper label:** Business net profit or loss without section 179, this person
- **Encoded (Dollars):** Add sc.line31_pre179 over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.line31_pre179","op":"sum_over"}`
- Cite: [i1040sc] p. 14, Line 31; i4562 p. 4, Part I (2025; sha256 b5536db9)

## (helper) — `person.has_sc`

- **Authored helper label:** This person has at least one Schedule C
- **Encoded (Bool):** helper "Number of Schedules C for this person" > 0 (a count)
- Expr: `{"gt":["person.sc_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040sse] p. 1, Who Must File Schedule SE; p. 2, Joint Returns, "If both spouses have self-employment income, each must file a separate Schedule SE" (2025; sha256 ea9e3120)

## (helper) — `person.sc_total`

- **Authored helper label:** This person's Schedule C net profit or loss (all businesses)
- **Encoded (Dollars):** Add sc.result over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.result","op":"sum_over"}`
- Cite: [i1040sse] p. 2, More Than One Business, "Figure the combined SE tax on one Schedule SE" (2025; sha256 ea9e3120)

## (screen) — `person.se_screen`

- **Authored helper label:** Does any of these apply to this person's self-employment?
- **Encoded (Bool):** Input — Does any of these apply to this person?

  - church employee income (wages from a church or qualified church-controlled organization that elected exemption from social security and Medicare taxes)
  - being a minister, a member of a religious order or a Christian Science practitioner, or having an approved Form 4361 or Form 4029
  - net earnings from self-employment from a partnership (Schedule K-1, box 14, code A) or other self-employment income not on a Schedule C (such as director's fees, fiduciary fees, or fees as a fee-basis state or local government employee)
  - farm income (Schedule F) or Conservation Reserve Program payments
  - electing an optional method (Schedule SE Part II)
  - a chapter 11 bankruptcy case
  - community income on a separate return
  - self-employment income exempt under an international social security agreement or earned as a U.S. citizen employed by a foreign government
- Expr: `{"op":"input","source":"Does any of these apply to this person?\n\n- church employee income (wages from a church or qualified church-controlled organization that elected exemption from social security and Medicare taxes)\n- being a minister, a member of a religious order or a Christian Science practitioner, or having an approved Form 4361 or Form 4029\n- net earnings from self-employment from a partnership (Schedule K-1, box 14, code A) or other self-employment income not on a Schedule C (such as director's fees, fiduciary fees, or fees as a fee-basis state or local government employee)\n- farm income (Schedule F) or Conservation Reserve Program payments\n- electing an optional method (Schedule SE Part II)\n- a chapter 11 bankruptcy case\n- community income on a separate return\n- self-employment income exempt under an international social security agreement or earned as a U.S. citizen employed by a foreign government"}`
- Cite: [i1040sse] pp. 1-5, Who Must Pay Self-Employment (SE) Tax, Net Earnings From Self-Employment, Instructions for Part II; f1040sse lines 1a, 1b and 5a; p. 1, Employees of Churches and Church Organizations, "Church employee income is wages you received as an employee (other than as a minister, member of a religious order, or Christian Science practitioner) of a church or qualified church-controlled organization that has a certificate in effect electing an exemption from employer social security and Medicare taxes." (2025; sha256 ea9e3120)

## (gate) — `person.se_screened`

- **Authored helper label:** This person's self-employment tax is outside this tool
- **Encoded (Bool):** helper "Does any of these apply to this person's self-employment?" = true
- Expr: `{"eq":["person.se_screen",{"const":true}],"op":"test"}`
- Cite: [i1040sse] pp. 1-5 (2025; sha256 ea9e3120)

## (helper) — `person.se_line2`

- **Authored helper label:** Schedule SE line 2 for this person
- **Encoded (Dollars):** Enter the amount from helper "This person's Schedule C net profit or loss (all businesses)".
- **Refusal:** when person.se_screened is true, cannot complete Schedule SE items outside this tool (church employee income, clergy, Forms 4361 and 4029, partnership and other self-employment income, farm income, optional methods, chapter 11, community income, exempt income, Forms 4137 and 8919). These self-employment tax items are outside this tool. Cite: [i1040sse] pp. 1-5 (2025; sha256 ea9e3120)
- Expr: `{"from":"person.sc_total","op":"copy"}`
- Cite: [f1040sse] Schedule SE (2025), line 2, "Net profit or (loss) from Schedule C, line 31" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `person.se_line6`

- **Authored helper label:** Schedule SE line 6 for this person
- **Encoded (NonNegDollars):** Choose — [helper "This person has at least one Schedule C" = true → "line6" of Schedule SE (Form 1040) — Self-Employment Tax, one per person with line2 = helper "Schedule SE line 2 for this person", line8a = line wages, line8b = helper "This person's Form 4137 line 10 (unreported tips subject to social security tax) (only when Form 4137 is filed; zero otherwise)", and line8c = helper "This person's Form 8919 line 10 (wages subject to social security tax) (only when Form 8919 is filed; zero otherwise)"] [helper "This person has at least one Schedule C" = false → line zero]
- **Refusal:** when person.se_rrta is true, cannot complete Schedule SE with railroad retirement (tier 1) compensation. Schedule SE line 8a adds railroad retirement (tier 1) compensation to the social security wages, and this tool does not take railroad compensation. Prepare Schedule SE with the railroad retirement instructions. Cite: [f1040sse] Schedule SE (2025), line 8a, "Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2) and railroad retirement (tier 1) compensation" (2025; created 2025-05-07; sha256 05bc2b3e)
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":{"bind":{"line2":"person.se_line2","line8a":"person.wages","line8b":"person.f4137_line10","line8c":"person.f8919_line10"},"def":"se","line":"line6"}},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f1040sse] Schedule SE (2025), line 6, "Add lines 4c and 5b"; i8959 p. 3, Line 8, "Enter your self-employment income from Schedule SE (Form 1040), Part I, line 6" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `person.se_line12`

- **Authored helper label:** Schedule SE line 12 (self-employment tax) for this person
- **Encoded (NonNegDollars):** Choose — [helper "This person has at least one Schedule C" = true → "line12" of Schedule SE (Form 1040) — Self-Employment Tax, one per person with line2 = helper "Schedule SE line 2 for this person", line8a = line wages, line8b = helper "This person's Form 4137 line 10 (unreported tips subject to social security tax) (only when Form 4137 is filed; zero otherwise)", and line8c = helper "This person's Form 8919 line 10 (wages subject to social security tax) (only when Form 8919 is filed; zero otherwise)"] [helper "This person has at least one Schedule C" = false → line zero]
- **Refusal:** when person.se_rrta is true, cannot complete Schedule SE with railroad retirement (tier 1) compensation. Schedule SE line 8a adds railroad retirement (tier 1) compensation to the social security wages, and this tool does not take railroad compensation. Prepare Schedule SE with the railroad retirement instructions. Cite: [f1040sse] Schedule SE (2025), line 8a, "Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2) and railroad retirement (tier 1) compensation" (2025; created 2025-05-07; sha256 05bc2b3e)
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":{"bind":{"line2":"person.se_line2","line8a":"person.wages","line8b":"person.f4137_line10","line8c":"person.f8919_line10"},"def":"se","line":"line12"}},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f1040sse] Schedule SE (2025), line 12, "Enter here and on Schedule 2 (Form 1040), line 4" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `person.se_line13`

- **Authored helper label:** Schedule SE line 13 (deduction for one-half of self-employment tax) for this person
- **Encoded (NonNegDollars):** Choose — [helper "This person has at least one Schedule C" = true → "line13" of Schedule SE (Form 1040) — Self-Employment Tax, one per person with line2 = helper "Schedule SE line 2 for this person", line8a = line wages, line8b = helper "This person's Form 4137 line 10 (unreported tips subject to social security tax) (only when Form 4137 is filed; zero otherwise)", and line8c = helper "This person's Form 8919 line 10 (wages subject to social security tax) (only when Form 8919 is filed; zero otherwise)"] [helper "This person has at least one Schedule C" = false → line zero]
- **Refusal:** when person.se_rrta is true, cannot complete Schedule SE with railroad retirement (tier 1) compensation. Schedule SE line 8a adds railroad retirement (tier 1) compensation to the social security wages, and this tool does not take railroad compensation. Prepare Schedule SE with the railroad retirement instructions. Cite: [f1040sse] Schedule SE (2025), line 8a, "Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2) and railroad retirement (tier 1) compensation" (2025; created 2025-05-07; sha256 05bc2b3e)
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":{"bind":{"line2":"person.se_line2","line8a":"person.wages","line8b":"person.f4137_line10","line8c":"person.f8919_line10"},"def":"se","line":"line13"}},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f1040sse] Schedule SE (2025), line 13, "Enter here and on Schedule 1 (Form 1040), line 15" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `person.se_line4c`

- **Authored helper label:** Schedule SE line 4c for this person
- **Encoded (NonNegDollars):** Choose — [helper "This person has at least one Schedule C" = true → "line4c" of Schedule SE (Form 1040) — Self-Employment Tax, one per person with line2 = helper "Schedule SE line 2 for this person", line8a = line wages, line8b = helper "This person's Form 4137 line 10 (unreported tips subject to social security tax) (only when Form 4137 is filed; zero otherwise)", and line8c = helper "This person's Form 8919 line 10 (wages subject to social security tax) (only when Form 8919 is filed; zero otherwise)"] [helper "This person has at least one Schedule C" = false → line zero]
- **Refusal:** when person.se_rrta is true, cannot complete Schedule SE with railroad retirement (tier 1) compensation. Schedule SE line 8a adds railroad retirement (tier 1) compensation to the social security wages, and this tool does not take railroad compensation. Prepare Schedule SE with the railroad retirement instructions. Cite: [f1040sse] Schedule SE (2025), line 8a, "Total social security wages and tips (total of boxes 3 and 7 on Form(s) W-2) and railroad retirement (tier 1) compensation" (2025; created 2025-05-07; sha256 05bc2b3e)
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":{"bind":{"line2":"person.se_line2","line8a":"person.wages","line8b":"person.f4137_line10","line8c":"person.f8919_line10"},"def":"se","line":"line4c"}},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f1040sse] Schedule SE (2025), line 4c, "Combine lines 4a and 4b. If less than $400, stop; you don’t owe self-employment tax" (2025; created 2025-05-07; sha256 05bc2b3e)

## (helper) — `person.plan`

- **Authored helper label:** Retirement plan of this self-employed person
- **Encoded (Enum(retire_plan)):** Input — Did you (this person) contribute for yourself, as a self-employed person, to a SEP IRA (sep) or a SIMPLE IRA (simple) for 2025, or to neither (none)?
- Expr: `{"op":"input","source":"Did you (this person) contribute for yourself, as a self-employed person, to a SEP IRA (sep) or a SIMPLE IRA (simple) for 2025, or to neither (none)?"}`
- Cite: [p560] pp. 8–11, 14–17, chapter 2, Simplified Employee Pension (SEP); chapter 3, SIMPLE IRA Plan; i1040gi Schedule 1, line 16 (For use in preparing 2025 returns; sha256 1f1f7abe)

## (screen) — `person.plan_screen`

- **Authored helper label:** Does any of these apply to this person's retirement contributions?
- **Encoded (Bool):** Input — Does any of these apply: a SARSEP; a SEP plan whose contribution rate is not a whole percentage or is more than 25%; a SIMPLE IRA plan of an employer that allows the higher contribution limits of section 117 of the SECURE 2.0 Act; contributions for yourself to more than one plan of your own business, or to a qualified plan (such as a solo 401(k)); with a SIMPLE IRA, salary reduction contributions or elective deferrals to any other plan in 2025 (such as a 401(k) or 403(b) through an employer); Roth SEP or Roth SIMPLE contributions; or contributions that are more than the maximum deductible amount, including an excess contributions carryover from an earlier year?
- Expr: `{"op":"input","source":"Does any of these apply: a SARSEP; a SEP plan whose contribution rate is not a whole percentage or is more than 25%; a SIMPLE IRA plan of an employer that allows the higher contribution limits of section 117 of the SECURE 2.0 Act; contributions for yourself to more than one plan of your own business, or to a qualified plan (such as a solo 401(k)); with a SIMPLE IRA, salary reduction contributions or elective deferrals to any other plan in 2025 (such as a 401(k) or 403(b) through an employer); Roth SEP or Roth SIMPLE contributions; or contributions that are more than the maximum deductible amount, including an excess contributions carryover from an earlier year?"}`
- Cite: [p560] pp. 11, 16, 38, chapter 2, Salary Reduction Simplified Employee Pension (SARSEP); chapter 3, Salary reduction contributions; chapter 5, Caution, "apply only to self-employed individuals who have only one defined contribution plan"; p. 11, chapter 2, Deduction Limit for Contributions for Participants, "Your contributions (including any excess contributions carryover)", and Carryover of Excess SEP Contributions (For use in preparing 2025 returns; sha256 1f1f7abe)

## (gate) — `person.plan_screened`

- **Authored helper label:** This person's retirement contributions are outside this tool (screened, or a plan with more than one Schedule C)
- **Encoded (Bool):** (helper "Does any of these apply to this person's retirement contributions?" = true or not helper "Retirement plan of this self-employed person" = 'none' and helper "Number of Schedules C for this person" > 1 (a count))
- Expr: `{"any":[{"eq":["person.plan_screen",{"const":true}],"op":"test"},{"all":[{"not":{"eq":["person.plan",{"const":"none"}],"op":"test"},"op":"test"},{"gt":["person.sc_count",{"const":1,"type":"Count"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [p560] pp. 8–11, 14–17, 38–40, chapters 2, 3 and 5; p. 7, "If you have more than one business, but only one has a retirement plan, only the earned income from that business is considered for that plan" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.cent`

- **Authored helper label:** One cent
- **Encoded (NonNegDollars):** Enter $0.01 (sc.one_cent).
- Expr: `{"op":"param","ref":"sc.one_cent"}`
- Cite: [p560] pp. 38–40, chapter 5, Rate Table for Self-Employed (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.hundred`

- **Authored helper label:** 100%, as cents
- **Encoded (NonNegDollars):** Enter $1 (sc.hundred_cents).
- Expr: `{"op":"param","ref":"sc.hundred_cents"}`
- Cite: [p560] pp. 38–40, chapter 5, Rate Worksheet for Self-Employed, "Rate in line 1 plus 1" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.sep_rate`

- **Authored helper label:** Plan contribution rate (whole percent)
- **Encoded (Count):** Input — The contribution rate stated in your SEP plan, as a whole percent (for example 10)
- Expr: `{"op":"input","source":"The contribution rate stated in your SEP plan, as a whole percent (for example 10)"}`
- Cite: [p560] pp. 38–40, chapter 5, Rate Table for Self-Employed, "find your plan contribution rate (the contribution rate stated in your plan)" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.sep_contrib`

- **Authored helper label:** Contributions to your own SEP IRA for 2025
- **Encoded (NonNegDollars):** Input — The contributions you made for yourself to your SEP IRA for 2025 (by the due date of the return, including extensions)
- **Refusal:** when person.plan_screened is true, cannot complete Retirement plan contributions outside this tool (SARSEP, other plan rates, higher SIMPLE limits, more than one plan, a plan with more than one Schedule C, other elective deferrals, Roth contributions, excess contributions). These retirement contributions are outside this tool. Cite: [p560] pp. 8–11, 14–17, 38–40, chapters 2, 3 and 5 (For use in preparing 2025 returns; sha256 1f1f7abe)
- Expr: `{"op":"input","source":"The contributions you made for yourself to your SEP IRA for 2025 (by the due date of the return, including extensions)"}`
- Cite: [p560] pp. 11, 39, chapter 2, Deduction Limit for Self-Employed Individuals; chapter 5, Deduction Worksheet for Self-Employed, "Next: Enter your actual contribution" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.sep_rate_c`

- **Authored helper label:** The plan rate, as cents
- **Encoded (NonNegDollars):** Multiply helper "One cent" by the number on helper "Plan contribution rate (whole percent)".
- Expr: `{"amount":"person.cent","count":"person.sep_rate","op":"multiply_count"}`
- Cite: [p560] pp. 38–40, chapter 5, Rate Worksheet for Self-Employed, line 1 (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.sep_rate_plus`

- **Authored helper label:** The plan rate plus 100%, as cents
- **Encoded (NonNegDollars):** Add helper "The plan rate, as cents" and helper "100%, as cents".
- Expr: `{"of":["person.sep_rate_c","person.hundred"],"op":"sum"}`
- Cite: [p560] pp. 38–40, chapter 5, Rate Worksheet for Self-Employed, line 2, "Rate in line 1 plus 1" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.sep_shown`

- **Authored helper label:** This person contributed to a SEP IRA for themselves (the SEP deduction worksheet is completed)
- **Encoded (Bool):** helper "Retirement plan of this self-employed person" = 'sep'
- Expr: `{"eq":["person.plan",{"const":"sep"}],"op":"test"}`
- Cite: [p560] p. 38, chapter 5, "if you are self-employed, you must use the rate table or rate worksheet and deduction worksheet to figure your deduction for contributions you made for yourself to a SEP IRA or qualified plan" (For use in preparing 2025 returns; sha256 1f1f7abe)

## Step 1 — `person.sep_s1`

- **Authored helper label:** Net profit from Schedule C, line 31
- **Encoded (Dollars):** Enter the amount from helper "This person's Schedule C net profit or loss (all businesses)".
- **Refusal:** when person.se_screened is true, cannot complete SEP Deduction Worksheet Step 1 with self-employment income not on a Schedule C (Schedule F, Schedule K-1 box 14 code A and the other items of the self-employment screen). These self-employment items are outside this tool. Cite: [p560] p. 39, chapter 5, Deduction Worksheet for Self-Employed, Step 1, "Enter your net profit from" (For use in preparing 2025 returns; sha256 1f1f7abe)
- **Shown on the values sheet only when:** This person contributed to a SEP IRA for themselves (the SEP deduction worksheet is completed) (`person.sep_shown`)
- Expr: `{"from":"person.sc_total","op":"copy"}`
- Cite: [p560] p. 39, chapter 5, Deduction Worksheet for Self-Employed, Step 1 (For use in preparing 2025 returns; sha256 1f1f7abe)

## Step 2 — `person.sep_s2`

- **Authored helper label:** Deduction for self-employment tax from Schedule 1, line 15
- **Encoded (NonNegDollars):** Enter the amount from helper "Schedule SE line 13 (deduction for one-half of self-employment tax) for this person".
- **Shown on the values sheet only when:** This person contributed to a SEP IRA for themselves (the SEP deduction worksheet is completed) (`person.sep_shown`)
- Expr: `{"from":"person.se_line13","op":"copy"}`
- Cite: [p560] p. 39, chapter 5, Deduction Worksheet for Self-Employed, Step 2 (this person's own Schedule SE, line 13) (For use in preparing 2025 returns; sha256 1f1f7abe)

## Step 3 — `person.sep_s3`

- **Authored helper label:** Net earnings from self-employment. Subtract step 2 from step 1
- **Encoded (NonNegDollars):** Subtract line Step 2 from line Step 1. If zero or less, enter -0-.
- **Shown on the values sheet only when:** This person contributed to a SEP IRA for themselves (the SEP deduction worksheet is completed) (`person.sep_shown`)
- Interpretation: amb.2025.sep_loss_floor
- Expr: `{"from":"person.sep_s1","op":"subtract_floor0","take":"person.sep_s2"}`
- Cite: [p560] p. 39, chapter 5, Deduction Worksheet for Self-Employed, Step 3 (For use in preparing 2025 returns; sha256 1f1f7abe)

## Step 5 — `person.sep_s5`

- **Authored helper label:** Multiply step 3 by step 4 (the plan rate divided by the plan rate plus 1, to six decimal places)
- **Encoded (NonNegDollars):** Divide helper "The plan rate, as cents" by helper "The plan rate plus 100%, as cents", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply line Step 3 by the result.
- **Shown on the values sheet only when:** This person contributed to a SEP IRA for themselves (the SEP deduction worksheet is completed) (`person.sep_shown`)
- Interpretation: amb.2025.sep_rate_places
- Expr: `{"amount":"person.sep_s3","op":"prorate","part":"person.sep_rate_c","places":6,"whole":"person.sep_rate_plus"}`
- Cite: [p560] pp. 39–40, chapter 5, Deduction Worksheet for Self-Employed, Steps 4 and 5, "Enter your rate from the Rate Table for Self-Employed or Rate Worksheet for Self-Employed", "Multiply step 3 by step 4"; p. 38, chapter 5, Rate Table for Self-Employed, "If your plan's contribution rate is 10% of a participant's compensation, your rate is 0.090909" (amb.2025.sep_rate_places) (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.comp_limit`

- **Authored helper label:** $350,000
- **Encoded (NonNegDollars):** Enter $350,000 (ret.comp_limit).
- Expr: `{"op":"param","ref":"ret.comp_limit"}`
- Cite: [p560] p. 39, chapter 5, Deduction Worksheet for Self-Employed, Step 6, "Multiply $350,000" (For use in preparing 2025 returns; sha256 1f1f7abe)

## Step 6 — `person.sep_s6`

- **Authored helper label:** Multiply $350,000 by your plan contribution rate (not the reduced rate)
- **Encoded (NonNegDollars):** Divide helper "The plan rate, as cents" by helper "100%, as cents", rounded to 6 decimal places; if the result is 1 or more, use 1 (and 0 if it is less than 0). Multiply helper "$350,000" by the result.
- **Shown on the values sheet only when:** This person contributed to a SEP IRA for themselves (the SEP deduction worksheet is completed) (`person.sep_shown`)
- Expr: `{"amount":"person.comp_limit","op":"prorate","part":"person.sep_rate_c","places":6,"whole":"person.hundred"}`
- Cite: [p560] p. 39, chapter 5, Deduction Worksheet for Self-Employed, Step 6 (For use in preparing 2025 returns; sha256 1f1f7abe)

## Step 7 — `person.sep_s7`

- **Authored helper label:** Enter the smaller of step 5 or step 6
- **Encoded (NonNegDollars):** Enter the smaller of line Step 5 or line Step 6.
- **Shown on the values sheet only when:** This person contributed to a SEP IRA for themselves (the SEP deduction worksheet is completed) (`person.sep_shown`)
- Expr: `{"of":["person.sep_s5","person.sep_s6"],"op":"smaller_of"}`
- Cite: [p560] p. 39, chapter 5, Deduction Worksheet for Self-Employed, Step 7 (For use in preparing 2025 returns; sha256 1f1f7abe)

## Step 8 — `person.sep_s8`

- **Authored helper label:** Contribution dollar limit
- **Encoded (NonNegDollars):** Enter $70,000 (ret.sep_dollar_limit).
- **Shown on the values sheet only when:** This person contributed to a SEP IRA for themselves (the SEP deduction worksheet is completed) (`person.sep_shown`)
- Expr: `{"op":"param","ref":"ret.sep_dollar_limit"}`
- Cite: [p560] p. 39, chapter 5, Deduction Worksheet for Self-Employed, Step 8, "$70,000" (For use in preparing 2025 returns; sha256 1f1f7abe)

## Step 21 — `person.sep_s21`

- **Authored helper label:** Maximum deductible contribution (the smaller of step 7 or step 8; no elective deferrals)
- **Encoded (NonNegDollars):** Enter the smaller of line Step 7 or line Step 8.
- **Shown on the values sheet only when:** This person contributed to a SEP IRA for themselves (the SEP deduction worksheet is completed) (`person.sep_shown`)
- Expr: `{"of":["person.sep_s7","person.sep_s8"],"op":"smaller_of"}`
- Cite: [p560] p. 39, chapter 5, Deduction Worksheet for Self-Employed, Step 8 note, "Otherwise, skip steps 9 through 20 and enter the smaller of step 7 or step 8 on step 21" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (gate) — `person.sep_excess`

- **Authored helper label:** The SEP contributions are more than the maximum deductible contribution
- **Encoded (Bool):** helper "Contributions to your own SEP IRA for 2025" > line Step 21
- Expr: `{"gt":["person.sep_contrib","person.sep_s21"],"op":"test"}`
- Cite: [p560] p. 39, chapter 5, "Enter your actual contribution, not to exceed your maximum deductible contribution"; p. 11, chapter 2, Carryover of Excess SEP Contributions, "If you made SEP contributions that are more than the deduction limit (nondeductible contributions), you can carry over and deduct the difference in later years" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.sep_deduction`

- **Authored helper label:** SEP deduction for yourself
- **Encoded (NonNegDollars):** Enter the amount from helper "Contributions to your own SEP IRA for 2025".
- **Refusal:** when person.sep_excess is true, cannot complete SEP contributions above the maximum deductible contribution. Excess SEP contributions are outside this tool. Cite: [p560] pp. 11, 39, chapter 2, Excess contributions; chapter 5 (For use in preparing 2025 returns; sha256 1f1f7abe)
- Expr: `{"from":"person.sep_contrib","op":"copy"}`
- Cite: [p560] p. 39, chapter 5, "Enter your actual contribution, not to exceed your maximum deductible contribution, on Schedule 1 (Form 1040), line 16" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_deferral`

- **Authored helper label:** Salary reduction contributions for yourself to your SIMPLE IRA (including catch-up)
- **Encoded (NonNegDollars):** Input — The salary reduction contributions you made for yourself to your SIMPLE IRA for 2025 (by the due date of the return, including extensions), including any catch-up contributions your plan allows
- **Refusal:** when person.plan_screened is true, cannot complete Retirement plan contributions outside this tool. These retirement contributions are outside this tool. Cite: [p560] pp. 8–11, 14–17, 38–40, chapters 2, 3 and 5 (For use in preparing 2025 returns; sha256 1f1f7abe)
- Expr: `{"op":"input","source":"The salary reduction contributions you made for yourself to your SIMPLE IRA for 2025 (by the due date of the return, including extensions), including any catch-up contributions your plan allows"}`
- Cite: [p560] p. 16, chapter 3, Salary reduction contributions and Catch-up contributions, "A SIMPLE IRA plan can permit participants who are age 50 or over at the end of the calendar year to also make catch-up contributions"; p. 17, When To Deduct Contributions, "You can deduct contributions for a particular tax year if they are made for that tax year and are made by the due date (including extensions) of your federal income tax return for that year" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_age`

- **Authored helper label:** Catch-up eligibility from the year of birth: 64 or older or 50 to 59 age50, 60 to 63 age60_63, under 50 under50; for a person born in a year in which only the birth date decides the band, as that person states
- **Encoded (Enum(catchup_age)):** Choose — [helper "The year you were born" ≥ 0 (a count) and helper "The year you were born" < 1962 (age.cut_64) → helper "Year parameter ret.catchup_age50 (age50)"] [helper "The year you were born" ≥ 1962 (age.cut_64) and helper "The year you were born" < 1966 (age.cut_60) → helper "Catch-up band of a person born from the year age.cut_64 up to the year before age.cut_60: 60 to 63, or for a person born in the year age.cut_64 as that person states"] [helper "The year you were born" ≥ 1966 (age.cut_60) and helper "The year you were born" < 1976 (age.cut_50) → helper "Catch-up band of a person born from the year age.cut_60 up to the year before age.cut_50: 50 to 59, or for a person born in the year age.cut_60 as that person states"] [helper "The year you were born" ≥ 1976 (age.cut_50) → helper "Catch-up band of a person born in the year age.cut_50 or later: under 50, or for a person born in the year age.cut_50 from that person's age-50 answer"]
- Expr: `{"alternatives":[{"guard":{"all":[{"ge":["person.birth_year",{"const":0,"type":"Count"}],"op":"test"},{"lt":["person.birth_year",{"param":"age.cut_64"}],"op":"test"}],"op":"test"},"then":"person.catchup_age50"},{"guard":{"all":[{"ge":["person.birth_year",{"param":"age.cut_64"}],"op":"test"},{"lt":["person.birth_year",{"param":"age.cut_60"}],"op":"test"}],"op":"test"},"then":"person.simple_age_60_63_years"},{"guard":{"all":[{"ge":["person.birth_year",{"param":"age.cut_60"}],"op":"test"},{"lt":["person.birth_year",{"param":"age.cut_50"}],"op":"test"}],"op":"test"},"then":"person.simple_age_50_59_years"},{"guard":{"ge":["person.birth_year",{"param":"age.cut_50"}],"op":"test"},"then":"person.simple_age_under50_years"}],"op":"choose"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "age 50 or over at the end of the calendar year" and "in a tax year in which they attain age 60, 61, 62, or 63" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_age_60_63_years`

- **Authored helper label:** Catch-up band of a person born from the year age.cut_64 up to the year before age.cut_60: 60 to 63, or for a person born in the year age.cut_64 as that person states
- **Encoded (Enum(catchup_age)):** Choose — [helper "Born in 1962 or 1966 (a year in which the birth date decides whether the SIMPLE catch-up age band is 60 to 63)" = true → helper "Catch-up eligibility as stated by a person born in 1962 or 1966 (otherwise 50 to 59 or 64 and over; read only for those years)"] [helper "Born in 1962 or 1966 (a year in which the birth date decides whether the SIMPLE catch-up age band is 60 to 63)" = false → helper "Year parameter ret.catchup_age60_63 (age60_63)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.simple_open_year",{"const":true}],"op":"test"},"then":"person.simple_age_if_open_year"},{"guard":{"eq":["person.simple_open_year",{"const":false}],"op":"test"},"then":"person.catchup_age60_63"}],"op":"choose"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "age 50 or over at the end of the calendar year" and "in a tax year in which they attain age 60, 61, 62, or 63" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_age_50_59_years`

- **Authored helper label:** Catch-up band of a person born from the year age.cut_60 up to the year before age.cut_50: 50 to 59, or for a person born in the year age.cut_60 as that person states
- **Encoded (Enum(catchup_age)):** Choose — [helper "Born in 1962 or 1966 (a year in which the birth date decides whether the SIMPLE catch-up age band is 60 to 63)" = true → helper "Catch-up eligibility as stated by a person born in 1962 or 1966 (otherwise 50 to 59 or 64 and over; read only for those years)"] [helper "Born in 1962 or 1966 (a year in which the birth date decides whether the SIMPLE catch-up age band is 60 to 63)" = false → helper "Year parameter ret.catchup_age50 (age50)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.simple_open_year",{"const":true}],"op":"test"},"then":"person.simple_age_if_open_year"},{"guard":{"eq":["person.simple_open_year",{"const":false}],"op":"test"},"then":"person.catchup_age50"}],"op":"choose"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "age 50 or over at the end of the calendar year" and "in a tax year in which they attain age 60, 61, 62, or 63" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_age_under50_years`

- **Authored helper label:** Catch-up band of a person born in the year age.cut_50 or later: under 50, or for a person born in the year age.cut_50 from that person's age-50 answer
- **Encoded (Enum(catchup_age)):** Choose — [helper "Born in 1976" = true → helper "Catch-up eligibility of a person born in 1976 (50 or over at the end of 2025 as that person states, otherwise under 50)"] [helper "Born in 1976" = false → helper "Year parameter ret.catchup_under50 (under50)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.age50_open_year",{"const":true}],"op":"test"},"then":"person.simple_age_from_age50"},{"guard":{"eq":["person.age50_open_year",{"const":false}],"op":"test"},"then":"person.catchup_under50"}],"op":"choose"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "age 50 or over at the end of the calendar year" and "in a tax year in which they attain age 60, 61, 62, or 63" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_open_year`

- **Authored helper label:** Born in 1962 or 1966 (a year in which the birth date decides whether the SIMPLE catch-up age band is 60 to 63)
- **Encoded (Bool):** (helper "The year you were born" = 1962 (age.cut_64) or helper "The year you were born" = 1966 (age.cut_60))
- Expr: `{"any":[{"eq":["person.birth_year",{"param":"age.cut_64"}],"op":"test"},{"eq":["person.birth_year",{"param":"age.cut_60"}],"op":"test"}],"op":"test"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "age 50 or over at the end of the calendar year" and "in a tax year in which they attain age 60, 61, 62, or 63" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_age_at_year_end`

- **Authored helper label:** Catch-up eligibility, as stated by a person born in 1962 or 1966
- **Encoded (Enum(catchup_age)):** Input — Your age at the end of 2025 for SIMPLE catch-up contributions: under 50 (under50), 50 to 59 or 64 and over (age50), or 60, 61, 62 or 63 (age60_63)
- Expr: `{"op":"input","source":"Your age at the end of 2025 for SIMPLE catch-up contributions: under 50 (under50), 50 to 59 or 64 and over (age50), or 60, 61, 62 or 63 (age60_63)"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "age 50 or over at the end of the calendar year" and "in a tax year in which they attain age 60, 61, 62, or 63" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (gate) — `person.simple_age_if_open_year`

- **Authored helper label:** Catch-up eligibility as stated by a person born in 1962 or 1966 (otherwise 50 to 59 or 64 and over; read only for those years)
- **Encoded (Enum(catchup_age)):** Choose — [helper "Born in 1962 or 1966 (a year in which the birth date decides whether the SIMPLE catch-up age band is 60 to 63)" = true → helper "Catch-up eligibility, as stated by a person born in 1962 or 1966"] [helper "Born in 1962 or 1966 (a year in which the birth date decides whether the SIMPLE catch-up age band is 60 to 63)" = false → helper "Year parameter ret.catchup_age50 (age50)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.simple_open_year",{"const":true}],"op":"test"},"then":"person.simple_age_at_year_end"},{"guard":{"eq":["person.simple_open_year",{"const":false}],"op":"test"},"then":"person.catchup_age50"}],"op":"choose"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "age 50 or over at the end of the calendar year" and "in a tax year in which they attain age 60, 61, 62, or 63" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_age_from_age50`

- **Authored helper label:** Catch-up eligibility of a person born in 1976 (50 or over at the end of 2025 as that person states, otherwise under 50)
- **Encoded (Enum(catchup_age)):** Choose — [helper "Age 50 or older at the end of 2025, as stated by a person born in 1976 (otherwise no)" = true → helper "Year parameter ret.catchup_age50 (age50)"] [helper "Age 50 or older at the end of 2025, as stated by a person born in 1976 (otherwise no)" = false → helper "Year parameter ret.catchup_under50 (under50)"]
- Interpretation: amb.2025.ira_age50
- Expr: `{"alternatives":[{"guard":{"eq":["person.age50_at_year_end_if_open_year",{"const":true}],"op":"test"},"then":"person.catchup_age50"},{"guard":{"eq":["person.age50_at_year_end_if_open_year",{"const":false}],"op":"test"},"then":"person.catchup_under50"}],"op":"choose"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "age 50 or over at the end of the calendar year" and "in a tax year in which they attain age 60, 61, 62, or 63" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.catchup_under50`

- **Authored helper label:** Year parameter ret.catchup_under50 (under50)
- **Encoded (Enum(catchup_age)):** Enter under50 (ret.catchup_under50).
- Expr: `{"op":"param","ref":"ret.catchup_under50"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "age 50 or over at the end of the calendar year" and "in a tax year in which they attain age 60, 61, 62, or 63" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.catchup_age50`

- **Authored helper label:** Year parameter ret.catchup_age50 (age50)
- **Encoded (Enum(catchup_age)):** Enter age50 (ret.catchup_age50).
- Expr: `{"op":"param","ref":"ret.catchup_age50"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "age 50 or over at the end of the calendar year" and "in a tax year in which they attain age 60, 61, 62, or 63" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.catchup_age60_63`

- **Authored helper label:** Year parameter ret.catchup_age60_63 (age60_63)
- **Encoded (Enum(catchup_age)):** Enter age60_63 (ret.catchup_age60_63).
- Expr: `{"op":"param","ref":"ret.catchup_age60_63"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "age 50 or over at the end of the calendar year" and "in a tax year in which they attain age 60, 61, 62, or 63" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_kind`

- **Authored helper label:** Employer contribution formula of your SIMPLE IRA plan
- **Encoded (Enum(simple_formula)):** Input — The employer contribution formula of your SIMPLE IRA plan for 2025: matching contributions (match) or 2% nonelective contributions (nonelective)
- Expr: `{"op":"input","source":"The employer contribution formula of your SIMPLE IRA plan for 2025: matching contributions (match) or 2% nonelective contributions (nonelective)"}`
- Cite: [p560] pp. 16–17, chapter 3, Employer matching contributions and Nonelective contributions (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_employer`

- **Authored helper label:** Employer contributions for yourself to your SIMPLE IRA
- **Encoded (NonNegDollars):** Input — The employer matching or nonelective contributions you made for yourself to your SIMPLE IRA for 2025 (by the due date of the return, including extensions)
- Expr: `{"op":"input","source":"The employer matching or nonelective contributions you made for yourself to your SIMPLE IRA for 2025 (by the due date of the return, including extensions)"}`
- Cite: [p560] pp. 16–17, chapter 3, Employer matching contributions and Nonelective contributions; p. 17, Time limits for contributing funds, "You must make matching contributions or nonelective contributions by the due date (including extensions) for filing your federal income tax return for the year." (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_comp`

- **Authored helper label:** Compensation: net earnings from self-employment (Schedule SE, line 4)
- **Encoded (NonNegDollars):** Enter the amount from helper "Schedule SE line 4c for this person".
- Expr: `{"from":"person.se_line4c","op":"copy"}`
- Cite: [p560] p. 15, chapter 3, Compensation, "If you are self-employed, compensation is your net earnings from self-employment (line 4 of Schedule SE (Form 1040)) before subtracting any contributions made to the SIMPLE IRA plan for yourself" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_cap`

- **Authored helper label:** Salary reduction limit
- **Encoded (NonNegDollars):** Enter $16,500 (ret.simple_limit).
- Expr: `{"op":"param","ref":"ret.simple_limit"}`
- Cite: [p560] p. 16, chapter 3, Salary reduction contributions, "can't be more than $16,500 for 2025" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_regular`

- **Authored helper label:** Salary reduction contributions that are not catch-up contributions
- **Encoded (NonNegDollars):** Enter the smaller of helper "Salary reduction contributions for yourself to your SIMPLE IRA (including catch-up)" or helper "Salary reduction limit".
- Expr: `{"of":["person.simple_deferral","person.simple_cap"],"op":"smaller_of"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "Salary reduction contributions aren't treated as catch-up contributions until they exceed $16,500 for 2025" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_catchup`

- **Authored helper label:** Catch-up contributions
- **Encoded (NonNegDollars):** Subtract helper "Salary reduction contributions that are not catch-up contributions" from helper "Salary reduction contributions for yourself to your SIMPLE IRA (including catch-up)". If zero or less, enter -0-.
- Expr: `{"from":"person.simple_deferral","op":"subtract_floor0","take":"person.simple_regular"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.catchup_limit`

- **Authored helper label:** Catch-up contribution limit
- **Encoded (NonNegDollars):** Find the entry in SIMPLE IRA catch-up contribution limit, 2025 (Pub. 560, chapter 3) for age helper "Catch-up eligibility from the year of birth: 64 or older or 50 to 59 age50, 60 to 63 age60_63, under 50 under50; for a person born in a year in which only the birth date decides the band, as that person states".
- Expr: `{"keys":["person.simple_age"],"op":"keyed_lookup","table":"simple_catchup"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "generally $3,500 for 2025" and "the higher limit on catch-up contributions ... is $5,250" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.comp_after_regular`

- **Authored helper label:** Compensation less the salary reduction contributions that are not catch-up contributions
- **Encoded (NonNegDollars):** Subtract helper "Salary reduction contributions that are not catch-up contributions" from helper "Compensation: net earnings from self-employment (Schedule SE, line 4)". If zero or less, enter -0-.
- Expr: `{"from":"person.simple_comp","op":"subtract_floor0","take":"person.simple_regular"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "The excess of the participant's compensation over the salary reduction contributions that aren't catch-up contributions" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.catchup_max`

- **Authored helper label:** Maximum catch-up contribution
- **Encoded (NonNegDollars):** Enter the smaller of helper "Catch-up contribution limit" or helper "Compensation less the salary reduction contributions that are not catch-up contributions".
- Expr: `{"of":["person.catchup_limit","person.comp_after_regular"],"op":"smaller_of"}`
- Cite: [p560] p. 16, chapter 3, Catch-up contributions, "can't exceed the lesser of the following amounts" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.rate3`

- **Authored helper label:** 3%
- **Encoded (Rate):** Enter 3% (0.03) (ret.match_rate).
- Expr: `{"op":"param","ref":"ret.match_rate"}`
- Cite: [p560] p. 16, chapter 3, Employer matching contributions, "up to 3% of the employee's compensation" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.rate2`

- **Authored helper label:** 2%
- **Encoded (Rate):** Enter 2% (0.02) (ret.nonelective_rate).
- Expr: `{"op":"param","ref":"ret.nonelective_rate"}`
- Cite: [p560] p. 17, chapter 3, Nonelective contributions, "nonelective contributions of 2% of compensation" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.match_3pct`

- **Authored helper label:** 3% of compensation
- **Encoded (NonNegDollars):** Multiply helper "Compensation: net earnings from self-employment (Schedule SE, line 4)" by helper "3%".
- Expr: `{"amount":"person.simple_comp","op":"multiply_rate","rate":"person.rate3"}`
- Cite: [p560] p. 16, chapter 3, Employer matching contributions (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.deferrals_total`

- **Authored helper label:** Salary reduction contributions (allowed)
- **Encoded (NonNegDollars):** Add helper "Salary reduction contributions that are not catch-up contributions" and helper "Catch-up contributions".
- Expr: `{"of":["person.simple_regular","person.simple_catchup"],"op":"sum"}`
- Cite: [p560] p. 16, chapter 3, Employer matching contributions, "match each employee's salary reduction contribution(s) on a dollar-for-dollar basis" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.match_max`

- **Authored helper label:** Maximum matching contribution
- **Encoded (NonNegDollars):** Enter the smaller of helper "Salary reduction contributions (allowed)" or helper "3% of compensation".
- Expr: `{"of":["person.deferrals_total","person.match_3pct"],"op":"smaller_of"}`
- Cite: [p560] p. 16, chapter 3, Employer matching contributions (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.ne_comp`

- **Authored helper label:** Compensation taken into account (not more than $350,000)
- **Encoded (NonNegDollars):** Enter the smaller of helper "Compensation: net earnings from self-employment (Schedule SE, line 4)" or helper "$350,000".
- Expr: `{"of":["person.simple_comp","person.comp_limit"],"op":"smaller_of"}`
- Cite: [p560] p. 17, chapter 3, Nonelective contributions, "Only $350,000 of the employee's compensation can be taken into account" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.ne_max`

- **Authored helper label:** Maximum nonelective contribution
- **Encoded (NonNegDollars):** Multiply helper "Compensation taken into account (not more than $350,000)" by helper "2%".
- Expr: `{"amount":"person.ne_comp","op":"multiply_rate","rate":"person.rate2"}`
- Cite: [p560] p. 17, chapter 3, Nonelective contributions (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.employer_max`

- **Authored helper label:** Maximum employer contribution for the plan's formula
- **Encoded (NonNegDollars):** Choose — [helper "Employer contribution formula of your SIMPLE IRA plan" = 'match' → helper "Maximum matching contribution"] [helper "Employer contribution formula of your SIMPLE IRA plan" = 'nonelective' → helper "Maximum nonelective contribution"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.simple_kind",{"const":"match"}],"op":"test"},"then":"person.match_max"},{"guard":{"eq":["person.simple_kind",{"const":"nonelective"}],"op":"test"},"then":"person.ne_max"}],"op":"choose"}`
- Cite: [p560] pp. 16–17, chapter 3, Employer matching contributions and Nonelective contributions (For use in preparing 2025 returns; sha256 1f1f7abe)

## (gate) — `person.simple_excess`

- **Authored helper label:** Contributions above the SIMPLE limits
- **Encoded (Bool):** (helper "Catch-up contributions" > helper "Maximum catch-up contribution" or helper "Employer contributions for yourself to your SIMPLE IRA" > helper "Maximum employer contribution for the plan's formula" or helper "Salary reduction contributions that are not catch-up contributions" > helper "Compensation: net earnings from self-employment (Schedule SE, line 4)")
- Expr: `{"any":[{"gt":["person.simple_catchup","person.catchup_max"],"op":"test"},{"gt":["person.simple_employer","person.employer_max"],"op":"test"},{"gt":["person.simple_regular","person.simple_comp"],"op":"test"}],"op":"test"}`
- Cite: [p560] p. 16, chapter 3, Salary reduction contributions, Catch-up contributions and Employer matching contributions (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.simple_deduction`

- **Authored helper label:** SIMPLE deduction for yourself
- **Encoded (NonNegDollars):** Add helper "Salary reduction contributions (allowed)" and helper "Employer contributions for yourself to your SIMPLE IRA".
- **Refusal:** when person.simple_excess is true, cannot complete SIMPLE contributions above the limits. Excess SIMPLE contributions are outside this tool. Cite: [p560] pp. 14–17, chapter 3 (For use in preparing 2025 returns; sha256 1f1f7abe)
- Expr: `{"of":["person.deferrals_total","person.simple_employer"],"op":"sum"}`
- Cite: [p560] p. 17, chapter 3, Where To Deduct Contributions, "Sole proprietors and partners deduct contributions for themselves on line 16 of Schedule 1" (For use in preparing 2025 returns; sha256 1f1f7abe)

## (helper) — `person.plan_deduction`

- **Authored helper label:** Self-employed SEP or SIMPLE deduction for this person
- **Encoded (NonNegDollars):** Choose — [helper "Retirement plan of this self-employed person" = 'none' → line zero] [helper "Retirement plan of this self-employed person" = 'sep' → helper "SEP deduction for yourself"] [helper "Retirement plan of this self-employed person" = 'simple' → helper "SIMPLE deduction for yourself"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.plan",{"const":"none"}],"op":"test"},"then":"person.zero"},{"guard":{"eq":["person.plan",{"const":"sep"}],"op":"test"},"then":"person.sep_deduction"},{"guard":{"eq":["person.plan",{"const":"simple"}],"op":"test"},"then":"person.simple_deduction"}],"op":"choose"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 16, Self-Employed SEP, SIMPLE, and Qualified Plans; p560 p. 38, chapter 5, "if you are self-employed, you must use the rate table or rate worksheet and deduction worksheet to figure your deduction for contributions you made for yourself to a SEP IRA or qualified plan" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.s16`

- **Authored helper label:** Schedule 1 line 16 for this person
- **Encoded (NonNegDollars):** Choose — [helper "This person has at least one Schedule C" = true → helper "Self-employed SEP or SIMPLE deduction for this person"] [helper "This person has at least one Schedule C" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":"person.plan_deduction"},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 93, Schedule 1, line 16, "If you were self-employed or a partner, you may be able to take this" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.positive_profits`

- **Authored helper label:** Total of all net profits of this person's businesses (losses not included)
- **Encoded (NonNegDollars):** Add sc.profit_pos over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.profit_pos","op":"sum_over"}`
- Cite: [i7206] f7206 Form 7206 (2025), line 5, "Enter the total of all net profits* from Schedule C (Form 1040), line 31; Schedule F (Form 1040), line 34; or Schedule K-1 (Form 1065), box 14, code A", "Don’t include any net losses shown on these schedules" (2025; sha256 9cbf92b3)

## (helper) — `person.sehi`

- **Authored helper label:** Self-employed health insurance deduction, this person
- **Encoded (NonNegDollars):** Add sc.f7206_line14 over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.f7206_line14","op":"sum_over"}`
- Cite: [f7206] Form 7206 (2025), line 14 (2025; created 2025-10-02; sha256 822203c9)

## (helper) — `person.amt_dep_f17`

- **Authored helper label:** MACRS deductions on property placed in service before 2025 other than listed property (Form 4562 line 17), all of this person's businesses
- **Encoded (NonNegDollars):** Add sc.f17 over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.f17","op":"sum_over"}`
- Cite: [i6251] p. 5, Line 2l—Post-1986 Depreciation, "Property placed in service after 1998 that is depreciated for the regular tax using the 200% declining balance method (generally 3-, 5-, 7-, and 10-year property under the modified accelerated cost recovery system (MACRS)" (2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 b130e873)

## (helper) — `person.amt_dep_y3`

- **Authored helper label:** MACRS deductions on 3-year property placed in service in 2025 (Form 4562 line 19a), all of this person's businesses
- **Encoded (NonNegDollars):** Add sc.f19_y3 over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.f19_y3","op":"sum_over"}`
- Cite: [i6251] p. 5, Line 2l—Post-1986 Depreciation, "Property placed in service after 1998 that is depreciated for the regular tax using the 200% declining balance method (generally 3-, 5-, 7-, and 10-year property under the modified accelerated cost recovery system (MACRS)" (2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 b130e873)

## (helper) — `person.amt_dep_y5`

- **Authored helper label:** MACRS deductions on 5-year property placed in service in 2025 (Form 4562 line 19b), all of this person's businesses
- **Encoded (NonNegDollars):** Add sc.f19_y5 over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.f19_y5","op":"sum_over"}`
- Cite: [i6251] p. 5, Line 2l—Post-1986 Depreciation, "Property placed in service after 1998 that is depreciated for the regular tax using the 200% declining balance method (generally 3-, 5-, 7-, and 10-year property under the modified accelerated cost recovery system (MACRS)" (2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 b130e873)

## (helper) — `person.amt_dep_y7`

- **Authored helper label:** MACRS deductions on 7-year property placed in service in 2025 (Form 4562 line 19c), all of this person's businesses
- **Encoded (NonNegDollars):** Add sc.f19_y7 over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.f19_y7","op":"sum_over"}`
- Cite: [i6251] p. 5, Line 2l—Post-1986 Depreciation, "Property placed in service after 1998 that is depreciated for the regular tax using the 200% declining balance method (generally 3-, 5-, 7-, and 10-year property under the modified accelerated cost recovery system (MACRS)" (2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 b130e873)

## (helper) — `person.amt_dep_y10`

- **Authored helper label:** MACRS deductions on 10-year property placed in service in 2025 (Form 4562 line 19d), all of this person's businesses
- **Encoded (NonNegDollars):** Add sc.f19_y10 over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.f19_y10","op":"sum_over"}`
- Cite: [i6251] p. 5, Line 2l—Post-1986 Depreciation, "Property placed in service after 1998 that is depreciated for the regular tax using the 200% declining balance method (generally 3-, 5-, 7-, and 10-year property under the modified accelerated cost recovery system (MACRS)" (2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 b130e873)

## (helper) — `person.amt_dep_listed`

- **Authored helper label:** Depreciation of listed property, vehicles included (Form 4562 line 26 column (h)), all of this person's businesses
- **Encoded (NonNegDollars):** Add sc.f26h over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.f26h","op":"sum_over"}`
- Cite: [i6251] p. 5, Line 2l—Post-1986 Depreciation, "Property placed in service after 1998 that is depreciated for the regular tax using the 200% declining balance method (generally 3-, 5-, 7-, and 10-year property under the modified accelerated cost recovery system (MACRS)" (2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 b130e873)

## (helper) — `person.amt_dep`

- **Authored helper label:** Regular-tax MACRS depreciation of this person's businesses that the alternative minimum tax may refigure (Form 4562 lines 17, 19a to 19d and 26 column (h)); the line 2l adjustment of Form 6251 is at most this amount
- **Encoded (NonNegDollars):** Add helper "MACRS deductions on property placed in service before 2025 other than listed property (Form 4562 line 17), all of this person's businesses", helper "MACRS deductions on 3-year property placed in service in 2025 (Form 4562 line 19a), all of this person's businesses", helper "MACRS deductions on 5-year property placed in service in 2025 (Form 4562 line 19b), all of this person's businesses", helper "MACRS deductions on 7-year property placed in service in 2025 (Form 4562 line 19c), all of this person's businesses", helper "MACRS deductions on 10-year property placed in service in 2025 (Form 4562 line 19d), all of this person's businesses", and helper "Depreciation of listed property, vehicles included (Form 4562 line 26 column (h)), all of this person's businesses".
- Expr: `{"of":["person.amt_dep_f17","person.amt_dep_y3","person.amt_dep_y5","person.amt_dep_y7","person.amt_dep_y10","person.amt_dep_listed"],"op":"sum"}`
- Cite: [i6251] p. 6, Line 2l, How Is the Adjustment Figured?, "Subtract the AMT deduction for depreciation from the regular tax deduction and enter the result" (2025 (the revision for tax year 2025, archived from irs-prior after irs.gov posted a later revision); sha256 b130e873)

## (helper) — `person.qbi`

- **Authored helper label:** Qualified business income or loss of this person's businesses
- **Encoded (Dollars):** Add sc.qbi over every confirmed sc entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.qbi","op":"sum_over"}`
- Cite: [i8995] pp. 2, 4, Determining Your Qualified Business Income; p. 4, Line 1, "Enter on line 1(c) the net QBI or (loss) for the trade, business, or aggregation reported in the corresponding row" (2025; printed date 2026-01-26; sha256 875843ba)

## (helper) — `person.eic_part1`

- **Authored helper label:** Worksheet B, Part 1 for this person: Schedule SE line 3 less line 13
- **Encoded (Dollars):** Subtract helper "Schedule SE line 13 (deduction for one-half of self-employment tax) for this person" from helper "This person's Schedule C net profit or loss (all businesses)".
- Expr: `{"from":"person.sc_total","op":"subtract","take":"person.se_line13"}`
- Cite: [i1040gi] p. 47, Worksheet B, Part 1, lines 1a to 1e (line 1b is zero: the optional methods and church employee income are refused) (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.files_se`

- **Authored helper label:** This person files Schedule SE (line 4c is $400 or more)
- **Encoded (Bool):** helper "Schedule SE line 4c for this person" > $0 (sales.zero)
- Expr: `{"gt":["person.se_line4c",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 47, Worksheet B, Part 1 and Part 2, "Self-Employed NOT Required To File Schedule SE" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.eic_se_has`

- **Authored helper label:** This person's self-employment earned income for Worksheet B
- **Encoded (Dollars):** Choose — [helper "This person files Schedule SE (line 4c is $400 or more)" = true → helper "Worksheet B, Part 1 for this person: Schedule SE line 3 less line 13"] [helper "This person files Schedule SE (line 4c is $400 or more)" = false → helper "This person's Schedule C net profit or loss (all businesses)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.files_se",{"const":true}],"op":"test"},"then":"person.eic_part1"},{"guard":{"eq":["person.files_se",{"const":false}],"op":"test"},"then":"person.sc_total"}],"op":"choose"}`
- Cite: [i1040gi] p. 47, Worksheet B, Part 1, line 1e, and Part 2, line 2b (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.eic_se`

- **Authored helper label:** Worksheet B, Parts 1 and 2, for this person
- **Encoded (Dollars):** Choose — [helper "This person has at least one Schedule C" = true → helper "This person's self-employment earned income for Worksheet B"] [helper "This person has at least one Schedule C" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":"person.eic_se_has"},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 47, Worksheet B, "If you are married filing a joint return, include your spouse's amounts, if any, with yours" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.sc_1a`

- **Authored helper label:** This person's Schedules C with Schedule 1-A tips or overtime
- **Encoded (Count):** Add sc.one over every confirmed sc entry for which helper "Tips or overtime in this business to be deducted on Schedule 1-A" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"sc","field":"sc.one","op":"sum_over","where":{"eq":["sc.tips_ot",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 104, Schedule 1-A, line 5 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.dc_benefits`

- **Authored helper label:** This person's dependent care benefits from Forms W-2 box 10, less the part reported in box 1
- **Encoded (NonNegDollars):** Add w2.dc_benefits over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"w2","field":"w2.dc_benefits","op":"sum_over"}`
- Cite: [i2441] p. 5, Line 12, "Amounts you received as an employee should be shown in box 10 of your Form(s) W-2" (2025; sha256 86f0669e)

## (helper) — `person.dc_box10`

- **Authored helper label:** Total of box 10 of this person's Forms W-2
- **Encoded (NonNegDollars):** Add w2.box10 over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Interpretation: amb.2025.dc_line1e_attribution
- Expr: `{"collection":"w2","field":"w2.box10","op":"sum_over"}`
- Cite: [i2441] p. 5, Line 12, "Amounts you received as an employee should be shown in box 10 of your Form(s) W-2" (2025; sha256 86f0669e)

## (helper) — `person.dc_has_box10`

- **Authored helper label:** This person's Forms W-2 show dependent care benefits in box 10
- **Encoded (Bool):** helper "Total of box 10 of this person's Forms W-2" > $0 (sales.zero)
- Interpretation: amb.2025.dc_line1e_attribution
- Expr: `{"gt":["person.dc_box10",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i2441] p. 4, Lines 4 and 5, "If filing jointly, figure your and your spouse's earned income separately" and "The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z" (2025; sha256 86f0669e)

## (helper) — `person.dc_1e_mine`

- **Authored helper label:** Form 1040 line 1e is counted in this person's earned income: the only person whose Forms W-2 show box 10, or, when there is no such single person, the taxpayer
- **Encoded (Bool):** (f2441 helper "Exactly one person on the return has Forms W-2 showing box 10" = true and helper "This person's Forms W-2 show dependent care benefits in box 10" = true or f2441 helper "Exactly one person on the return has Forms W-2 showing box 10" = false and helper "Whose entry is this, yours or your spouse's?" = 'taxpayer')
- Interpretation: amb.2025.dc_line1e_attribution
- Expr: `{"any":[{"all":[{"eq":["f2441.one_box10",{"const":true}],"op":"test"},{"eq":["person.dc_has_box10",{"const":true}],"op":"test"}],"op":"test"},{"all":[{"eq":["f2441.one_box10",{"const":false}],"op":"test"},{"eq":["person.role",{"const":"taxpayer"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i2441] p. 4, Lines 4 and 5, "If filing jointly, figure your and your spouse's earned income separately" and "The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z" (2025; sha256 86f0669e)

## (helper) — `person.dc_1e_counted`

- **Authored helper label:** Form 1040 line 1e is more than zero and is counted in this person's earned income
- **Encoded (Bool):** f2441 helper "Form 1040 line 1e (taxable dependent care benefits) is more than zero" = true and helper "Form 1040 line 1e is counted in this person's earned income: the only person whose Forms W-2 show box 10, or, when there is no such single person, the taxpayer" = true
- Interpretation: amb.2025.dc_line1e_attribution
- Expr: `{"all":[{"eq":["f2441.has_1e",{"const":true}],"op":"test"},{"eq":["person.dc_1e_mine",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i2441] p. 4, Lines 4 and 5, "If filing jointly, figure your and your spouse's earned income separately" and "The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z" (2025; sha256 86f0669e)

## (helper) — `person.dc_zero`

- **Authored helper label:** No taxable dependent care benefits counted for this person
- **Encoded (NonNegDollars):** Enter $0 (sales.zero).
- Expr: `{"op":"param","ref":"sales.zero"}`
- Cite: [i2441] p. 4, Lines 4 and 5, "If filing jointly, figure your and your spouse's earned income separately" and "The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z" (2025; sha256 86f0669e)

## (helper) — `person.dc_1e`

- **Authored helper label:** This person's share of Form 1040 line 1e (taxable dependent care benefits) in Form 2441 earned income
- **Encoded (NonNegDollars):** Choose — [helper "Form 1040 line 1e is more than zero and is counted in this person's earned income" = true → f1040 line 1e] [helper "Form 1040 line 1e is more than zero and is counted in this person's earned income" = false → helper "No taxable dependent care benefits counted for this person"]
- Interpretation: amb.2025.dc_line1e_attribution
- Expr: `{"alternatives":[{"guard":{"eq":["person.dc_1e_counted",{"const":true}],"op":"test"},"then":"f1040.line1e"},{"guard":{"eq":["person.dc_1e_counted",{"const":false}],"op":"test"},"then":"person.dc_zero"}],"op":"choose"}`
- Cite: [i2441] p. 4, Lines 4 and 5, "If filing jointly, figure your and your spouse's earned income separately" and "The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z" (2025; sha256 86f0669e)

## (helper) — `person.dc_earned`

- **Authored helper label:** This person's earned income for Form 2441 lines 4 and 5: Form W-2 box 1, the person's share of line 1e, and Schedule SE line 3 less the deduction on Schedule 1 line 15 (or the Schedule C profit or loss when no Schedule SE is filed)
- **Encoded (Dollars):** Add helper "Total W-2 box 1 for this person", helper "This person's pay on Form 1040 lines 1b, 1c, 1d, 1g and 1h (wages, tips and other earned income not in W-2 box 1)", helper "This person's share of Form 1040 line 1e (taxable dependent care benefits) in Form 2441 earned income", and helper "Worksheet B, Parts 1 and 2, for this person".
- Interpretation: amb.2025.dc_line1e_attribution
- Expr: `{"of":["person.box1","person.earned_not_w2","person.dc_1e","person.eic_se"],"op":"sum"}`
- Cite: [i2441] p. 4, Lines 4 and 5, "The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z" and "The amount shown on Schedule SE (Form 1040), line 3, minus any deduction you claim on Schedule 1 (Form 1040), line 15"; p503 p. 11, Self-employment earnings, "Include your self-employment earnings in earned income, even if they are less than $400 and you didn't file Schedule SE (Form 1040)" (2025; sha256 86f0669e)

## (helper) — `person.dc_earned_b`

- **Authored helper label:** This person's earned income for Form 2441 lines 18 and 19: as for lines 4 and 5, without line 1e (the taxable benefits of line 12; when a line 13 grace-period amount could make part of line 1e earned income and change the excluded benefits, Form 2441 line 25 refuses)
- **Encoded (Dollars):** Add helper "Total W-2 box 1 for this person", helper "This person's pay on Form 1040 lines 1b, 1c, 1d, 1g and 1h (wages, tips and other earned income not in W-2 box 1)", and helper "Worksheet B, Parts 1 and 2, for this person".
- Expr: `{"of":["person.box1","person.earned_not_w2","person.eic_se"],"op":"sum"}`
- Cite: [i2441] p. 5, Line 18, "Earned income for figuring the amount of dependent care benefits you are able to exclude or deduct from your income is determined in the same way as earned income for figuring the credit is determined" and "for purposes of lines 18 and 19, earned income doesn’t include any dependent care benefits shown on line 12" (2025; sha256 86f0669e)

## (helper) — `person.sav_born`

- **Authored helper label:** Born before January 2, 2008
- **Encoded (Bool):** (helper "The year you were born" < 2008 (age.cut_18) or helper "The year you were born" = 2008 (age.cut_18) and helper "Born on January 1 (asked only of a person born in 1961, 2001, 2002, 2007 or 2008; otherwise no)" = true)
- Expr: `{"any":[{"lt":["person.birth_year",{"param":"age.cut_18"}],"op":"test"},{"all":[{"eq":["person.birth_year",{"param":"age.cut_18"}],"op":"test"},{"eq":["person.born_jan1_if_cut_year",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [f8880] p. 2, Who Can Take This Credit, "The person(s) who made the qualified contribution or elective deferral (a) was born after January 1, 2008" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_student`

- **Authored helper label:** Were you a student in 2025 (during any part of 5 calendar months, enrolled as a full-time student at a school, or taking a full-time, on-farm training course given by a school or a state, county, or local government agency)?
- **Encoded (Bool):** Input — Were you a student in 2025: during any part of 5 calendar months of 2025, were you enrolled as a full-time student at a school, or did you take a full-time, on-farm training course given by a school or a state, county, or local government agency? (A school includes technical, trade, and mechanical schools. It does not include on-the-job training courses, correspondence schools, or schools offering courses only through the Internet.)
- Expr: `{"op":"input","source":"Were you a student in 2025: during any part of 5 calendar months of 2025, were you enrolled as a full-time student at a school, or did you take a full-time, on-farm training course given by a school or a state, county, or local government agency? (A school includes technical, trade, and mechanical schools. It does not include on-the-job training courses, correspondence schools, or schools offering courses only through the Internet.)"}`
- Cite: [f8880] p. 2, Who Can Take This Credit, "You were a student if during any part of 5 calendar months of 2025 you: • Were enrolled as a full-time student at a school; or • Took a full-time, on-farm training course given by a school or a state, county, or local government agency" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_claimed`

- **Authored helper label:** Are you claimed as a dependent on someone else's 2025 tax return?
- **Encoded (Bool):** Input — Are you claimed as a dependent on someone else's 2025 tax return?
- Expr: `{"op":"input","source":"Are you claimed as a dependent on someone else's 2025 tax return?"}`
- Cite: [f8880] p. 2, Who Can Take This Credit, "(b) is claimed as a dependent on someone else’s 2025 tax return"; i1040gi p. 98, Line 21, "You, or your spouse if filing jointly, aren’t claimed as a dependent on someone else's (such as your parent’s) 2025 tax return" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_ineligible`

- **Authored helper label:** Born after January 1, 2008, claimed as a dependent on someone else's 2025 return, or a student (the dependent question is asked only if someone can claim you or your spouse as a dependent)
- **Encoded (Bool):** (helper "Born before January 2, 2008" = false or helper "Were you a student in 2025 (during any part of 5 calendar months, enrolled as a full-time student at a school, or taking a full-time, on-farm training course given by a school or a state, county, or local government agency)?" = true or sa helper "Can someone claim you or your spouse as a dependent for 2025? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)" = true and helper "Are you claimed as a dependent on someone else's 2025 tax return?" = true)
- Expr: `{"any":[{"eq":["person.sav_born",{"const":false}],"op":"test"},{"eq":["person.sav_student",{"const":true}],"op":"test"},{"all":[{"eq":["sa.dependent",{"const":true}],"op":"test"},{"eq":["person.sav_claimed",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [f8880] p. 2, Who Can Take This Credit, "The person(s) who made the qualified contribution or elective deferral (a) was born after January 1, 2008; (b) is claimed as a dependent on someone else’s 2025 tax return; or (c) was a student" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.ira_owner`

- **Authored helper label:** Had an IRA of any kind at any time in 2025, or has one now (traditional, Roth, SEP or SIMPLE, inherited, or opened in 2026 for 2025)
- **Encoded (Bool):** Input — Did you have an individual retirement arrangement (IRA) of any kind at any time in 2025, or do you have one now: traditional, Roth, SEP or SIMPLE, including an inherited IRA and one opened in 2026 for 2025?
- Expr: `{"op":"input","source":"Did you have an individual retirement arrangement (IRA) of any kind at any time in 2025, or do you have one now: traditional, Roth, SEP or SIMPLE, including an inherited IRA and one opened in 2026 for 2025?"}`
- Cite: [f8880] Form 8880 (2025), line 1, "Traditional and Roth IRA contributions"; i1040gi p. 95, Line 20, "If you made any nondeductible contributions to a traditional" (2025; created 2025-11-04; sha256 ba2b2877)

## (gate) — `person.sav_trad_if_ira_owner`

- **Authored helper label:** Made traditional IRA contributions for 2025 (asked only of a person with an IRA; otherwise no)
- **Encoded (Bool):** Choose — [helper "Had an IRA of any kind at any time in 2025, or has one now (traditional, Roth, SEP or SIMPLE, inherited, or opened in 2026 for 2025)" = true → helper "Did you make contributions (other than rollover contributions) to a traditional IRA for 2025?"] [helper "Had an IRA of any kind at any time in 2025, or has one now (traditional, Roth, SEP or SIMPLE, inherited, or opened in 2026 for 2025)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_owner",{"const":true}],"op":"test"},"then":"person.sav_trad"},{"guard":{"eq":["person.ira_owner",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [f8880] Form 8880 (2025), line 1, "Traditional and Roth IRA contributions"; i1040gi p. 95, Line 20, "If you made any nondeductible contributions to a traditional" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_trad`

- **Authored helper label:** Did you make contributions (other than rollover contributions) to a traditional IRA for 2025?
- **Encoded (Bool):** Input — Did you make contributions (other than rollover contributions) to a traditional IRA for 2025, deductible or not, including contributions made by the due date of your 2025 return for 2025? Do not count contributions made under a SEP or SIMPLE IRA plan, including those you made for yourself as a self-employed person.
- Expr: `{"op":"input","source":"Did you make contributions (other than rollover contributions) to a traditional IRA for 2025, deductible or not, including contributions made by the due date of your 2025 return for 2025? Do not count contributions made under a SEP or SIMPLE IRA plan, including those you made for yourself as a self-employed person."}`
- Cite: [f8880] Form 8880 (2025), line 1, "Traditional and Roth IRA contributions"; i1040gi p. 95, Line 20, "If you made any nondeductible contributions to a traditional" (2025; created 2025-11-04; sha256 ba2b2877)

## (screen) — `person.sav_able`

- **Authored helper label:** As the designated beneficiary of an ABLE account, did you contribute to it for 2025, or did you receive a distribution from an ABLE account after 2022 (through the due date of your 2025 return)?
- **Encoded (Bool):** Input — As the designated beneficiary of an ABLE account, did you contribute to it for 2025, or did you receive any distribution from an ABLE account after 2022 and before the due date of your 2025 return (including extensions)?
- Expr: `{"op":"input","source":"As the designated beneficiary of an ABLE account, did you contribute to it for 2025, or did you receive any distribution from an ABLE account after 2022 and before the due date of your 2025 return (including extensions)?"}`
- Cite: [f8880] Form 8880 (2025), line 1, "ABLE account contributions by the designated beneficiary"; p. 2, Line 4, "Traditional or Roth IRAs, or ABLE accounts" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_roth`

- **Authored helper label:** Your contributions to a Roth IRA for 2025 (not rollovers or conversions)
- **Encoded (NonNegDollars):** Input — Your contributions to a Roth IRA for 2025, including contributions made by the due date of your 2025 return that are for 2025; do not include rollover contributions (a repayment of a qualified disaster, birth or adoption, emergency personal expense, domestic abuse or terminal illness distribution is treated as one), conversions, or contributions returned to you with their earnings by the due date of your return (including extensions); zero if none
- Expr: `{"op":"input","source":"Your contributions to a Roth IRA for 2025, including contributions made by the due date of your 2025 return that are for 2025; do not include rollover contributions (a repayment of a qualified disaster, birth or adoption, emergency personal expense, domestic abuse or terminal illness distribution is treated as one), conversions, or contributions returned to you with their earnings by the due date of your return (including extensions); zero if none"}`
- Cite: [f8880] Form 8880 (2025), line 1, "Do not include rollover contributions"; p. 2, Who Can Take This Credit, "(a) contributions (other than rollover contributions) to a traditional or Roth IRA"; i8606 p. 4, Special Terms, Certain 2025 retirement plan distribution repayments treated as rollovers; p590a p. 31, Contributions Returned Before Due Date of Return (2025; created 2025-11-04; sha256 ba2b2877)

## (gate) — `person.sav_roth_if_ira_owner`

- **Authored helper label:** Roth IRA contributions for 2025 (asked only of a person with an IRA; otherwise zero)
- **Encoded (NonNegDollars):** Choose — [helper "Had an IRA of any kind at any time in 2025, or has one now (traditional, Roth, SEP or SIMPLE, inherited, or opened in 2026 for 2025)" = true → helper "Your contributions to a Roth IRA for 2025 (not rollovers or conversions)"] [helper "Had an IRA of any kind at any time in 2025, or has one now (traditional, Roth, SEP or SIMPLE, inherited, or opened in 2026 for 2025)" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_owner",{"const":true}],"op":"test"},"then":"person.sav_roth"},{"guard":{"eq":["person.ira_owner",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f8880] Form 8880 (2025), line 1, "Do not include rollover contributions"; p. 2, Who Can Take This Credit, "(a) contributions (other than rollover contributions) to a traditional or Roth IRA" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_line1`

- **Authored helper label:** Form 8880 line 1 for this person (traditional IRA contributions for 2025, deductible or not, and Roth IRA contributions for 2025)
- **Encoded (NonNegDollars):** Add helper "This person's traditional IRA contributions for 2025 (zero if the traditional IRA question was answered No)" and helper "Roth IRA contributions for 2025 (asked only of a person with an IRA; otherwise zero)".
- **Refusal:** when person.ira_excess_gate is true, cannot complete Excess or recharacterized IRA contributions (Form 5329 Parts III and IV, Pub. 590-A). Traditional or Roth IRA contributions for 2025 that are more than allowed or were recharacterized, and an excess contribution from an earlier year that remained in an IRA at the end of 2025, are outside this tool. Cite: [p590a] p. 35, Excess Contributions, "Generally, an excess contribution is the amount contributed to your traditional IRAs for the year that is more than the smaller of" (2025; sha256 ca0e4287)
- **Refusal:** when person.sav_able is true, cannot complete ABLE account contributions or distributions on Form 8880 (Pub. 907). Contributions to an ABLE account by its designated beneficiary (line 1) and ABLE distributions (line 4) are outside this tool. Cite: [f8880] p. 2, What’s New, "See Pub. 907, Tax Highlights for Persons With Disabilities, for more information about ABLE accounts" (2025; created 2025-11-04; sha256 ba2b2877)
- Interpretation: amb.2025.savers_traditional
- Expr: `{"of":["person.ira_contrib","person.sav_roth_if_ira_owner"],"op":"sum"}`
- Cite: [f8880] Form 8880 (2025), line 1, "Traditional and Roth IRA contributions"; p. 2, Who Can Take This Credit, "(a) contributions (other than rollover contributions) to a traditional or Roth IRA" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_w2`

- **Authored helper label:** Elective deferrals and designated Roth contributions for 2025 from this person's Forms W-2, box 12
- **Encoded (NonNegDollars):** Add w2.sav_deferral over every confirmed w2 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"w2","field":"w2.sav_deferral","op":"sum_over"}`
- Cite: [f8880] p. 2, Line 2, "These amounts may be shown in box 12 of your Form(s) W-2 for 2025" (2025; created 2025-11-04; sha256 ba2b2877)

## (screen) — `person.sav_excess`

- **Authored helper label:** Were your elective deferrals and designated Roth contributions for 2025 more than the limit for your plans?
- **Encoded (Bool):** scope helper "The answer to scope.excess_deferral, asked only when a Form W-2 is listed (false otherwise)" = true
- Expr: `{"eq":["scope.excess_deferral_if_w2",{"const":true}],"op":"test"}`
- Cite: [iw2w3] p. 20, Box 12—Codes, "Even though the 2025 limit for elective deferrals and designated Roth contributions is $23,500, Alex's total elective deferral amount of $26,500 is reported in box 12 with code D" (2025; printed date 2025-02-19; sha256 bfecbc99)

## (helper) — `person.no`

- **Authored helper label:** Year parameter household.no (false)
- **Encoded (Bool):** Enter false (household.no).
- Expr: `{"op":"param","ref":"household.no"}`
- Cite: [iw2w3] p. 20, Box 12—Codes, "Even though the 2025 limit for elective deferrals and designated Roth contributions is $23,500, Alex's total elective deferral amount of $26,500 is reported in box 12 with code D" (2025; printed date 2025-02-19; sha256 bfecbc99)

## (helper) — `person.sav_has_w2`

- **Authored helper label:** Elective deferrals or designated Roth contributions in this person's Forms W-2, box 12
- **Encoded (Bool):** helper "Elective deferrals and designated Roth contributions for 2025 from this person's Forms W-2, box 12" > $0 (sales.zero)
- Expr: `{"gt":["person.sav_w2",{"param":"sales.zero"}],"op":"test"}`
- Cite: [iw2w3] p. 20, Box 12—Codes, "Even though the 2025 limit for elective deferrals and designated Roth contributions is $23,500, Alex's total elective deferral amount of $26,500 is reported in box 12 with code D" (2025; printed date 2025-02-19; sha256 bfecbc99)

## (gate) — `person.sav_excess_gate`

- **Authored helper label:** Elective deferrals in box 12 over the limit for 2025
- **Encoded (Bool):** Choose — [helper "Elective deferrals or designated Roth contributions in this person's Forms W-2, box 12" = true → helper "Were your elective deferrals and designated Roth contributions for 2025 more than the limit for your plans?"] [helper "Elective deferrals or designated Roth contributions in this person's Forms W-2, box 12" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.sav_has_w2",{"const":true}],"op":"test"},"then":"person.sav_excess"},{"guard":{"eq":["person.sav_has_w2",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [iw2w3] p. 20, Box 12—Codes, "Even though the 2025 limit for elective deferrals and designated Roth contributions is $23,500, Alex's total elective deferral amount of $26,500 is reported in box 12 with code D" (2025; printed date 2025-02-19; sha256 bfecbc99)

## (helper) — `person.sav_voluntary`

- **Authored helper label:** Voluntary employee contributions for 2025 to a qualified retirement plan (after-tax, not designated Roth)
- **Encoded (NonNegDollars):** Input — Voluntary after-tax employee contributions you made for 2025 to a qualified retirement plan (including the federal Thrift Savings Plan), which may be shown in box 14 of your Form W-2; not designated Roth contributions, and not contributions designated under section 414(h)(2) (treated as employer contributions); zero if none
- Expr: `{"op":"input","source":"Voluntary after-tax employee contributions you made for 2025 to a qualified retirement plan (including the federal Thrift Savings Plan), which may be shown in box 14 of your Form W-2; not designated Roth contributions, and not contributions designated under section 414(h)(2) (treated as employer contributions); zero if none"}`
- Cite: [f8880] p. 2, Line 2, "Voluntary employee contributions to a qualified retirement plan, as defined in section 4974(c) (including the federal TSP)"; "Contributions designated under section 414(h)(2) are treated as employer contributions" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_simple_plan`

- **Authored helper label:** This self-employed person's own SIMPLE IRA salary reduction contributions, by plan
- **Encoded (NonNegDollars):** Choose — [helper "Retirement plan of this self-employed person" = 'none' → line zero] [helper "Retirement plan of this self-employed person" = 'sep' → line zero] [helper "Retirement plan of this self-employed person" = 'simple' → helper "Salary reduction contributions for yourself to your SIMPLE IRA (including catch-up)"]
- Interpretation: amb.2025.savers_sep_contrib
- Expr: `{"alternatives":[{"guard":{"eq":["person.plan",{"const":"none"}],"op":"test"},"then":"person.zero"},{"guard":{"eq":["person.plan",{"const":"sep"}],"op":"test"},"then":"person.zero"},{"guard":{"eq":["person.plan",{"const":"simple"}],"op":"test"},"then":"person.simple_deferral"}],"op":"choose"}`
- Cite: [f8880] p. 2, Line 2, "Elective deferrals (including designated Roth contributions under section 402A, if applicable) to a 401(k), 403(b), governmental 457(b), SEP, SIMPLE, or the federal TSP" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_simple`

- **Authored helper label:** This person's own SIMPLE IRA salary reduction contributions as a self-employed person
- **Encoded (NonNegDollars):** Choose — [helper "This person has at least one Schedule C" = true → helper "This self-employed person's own SIMPLE IRA salary reduction contributions, by plan"] [helper "This person has at least one Schedule C" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":"person.sav_simple_plan"},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f8880] p. 2, Line 2, "Elective deferrals (including designated Roth contributions under section 402A, if applicable) to a 401(k), 403(b), governmental 457(b), SEP, SIMPLE, or the federal TSP" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_line2`

- **Authored helper label:** Form 8880 line 2 for this person (box 12 deferrals, voluntary contributions and own SIMPLE salary reduction contributions)
- **Encoded (NonNegDollars):** Add helper "Elective deferrals and designated Roth contributions for 2025 from this person's Forms W-2, box 12", helper "Voluntary employee contributions for 2025 to a qualified retirement plan (after-tax, not designated Roth)", and helper "This person's own SIMPLE IRA salary reduction contributions as a self-employed person".
- **Refusal:** when person.sav_excess_gate is true, cannot complete Excess elective deferrals on Form 8880 line 2. Elective deferrals over the limit for the year, and their later distribution, are outside this tool. Cite: [iw2w3] p. 20, Box 12—Codes, "Even though the 2025 limit for elective deferrals and designated Roth contributions is $23,500" (2025; printed date 2025-02-19; sha256 bfecbc99)
- Expr: `{"of":["person.sav_w2","person.sav_voluntary","person.sav_simple"],"op":"sum"}`
- Cite: [f8880] Form 8880 (2025), line 2, "Elective deferrals to a 401(k) or other qualified employer plan, voluntary employee contributions, and 501(c)(18)(D) plan contributions for 2025"; p. 2, Line 2, "Include on line 2 any of the following amounts" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_prior_joint`

- **Authored helper label:** Your distributions in 2023 and 2024 from years for which you and your spouse filed a joint return, and in 2026 before the due date of your 2025 return (a joint return only)
- **Encoded (NonNegDollars):** Input — On a joint return: the distributions you received in 2023 and 2024 in a year for which you and your spouse filed a joint return, plus those you receive in 2026 before the due date of your 2025 return (including extensions), from any of the following; zero if none

  - a traditional or Roth IRA
  - a 401(k), 403(b), governmental 457(b), 501(c)(18)(D), SEP or SIMPLE plan, or the federal TSP
  - another qualified retirement plan

  Do not include:
  - rollovers or trustee-to-trustee transfers
  - in-plan Roth rollovers
  - amounts rolled over or converted to a Roth IRA
  - plan loans treated as distributions
  - distributions of excess contributions or deferrals
  - IRA contributions returned by the due date
  - section 404(k) dividends
  - distributions from a military retirement plan (other than the TSP)
  - distributions from an inherited IRA as a nonspouse beneficiary
- **Refusal:** when person.sav_able is true, cannot complete ABLE account contributions or distributions on Form 8880 (Pub. 907). Contributions to an ABLE account by its designated beneficiary (line 1) and ABLE distributions (line 4) are outside this tool. Cite: [f8880] p. 2, What’s New, "See Pub. 907, Tax Highlights for Persons With Disabilities, for more information about ABLE accounts" (2025; created 2025-11-04; sha256 ba2b2877)
- Interpretation: amb.2025.savers_2026_joint
- Expr: `{"op":"input","source":"On a joint return: the distributions you received in 2023 and 2024 in a year for which you and your spouse filed a joint return, plus those you receive in 2026 before the due date of your 2025 return (including extensions), from any of the following; zero if none\n\n- a traditional or Roth IRA\n- a 401(k), 403(b), governmental 457(b), 501(c)(18)(D), SEP or SIMPLE plan, or the federal TSP\n- another qualified retirement plan\n\nDo not include:\n- rollovers or trustee-to-trustee transfers\n- in-plan Roth rollovers\n- amounts rolled over or converted to a Roth IRA\n- plan loans treated as distributions\n- distributions of excess contributions or deferrals\n- IRA contributions returned by the due date\n- section 404(k) dividends\n- distributions from a military retirement plan (other than the TSP)\n- distributions from an inherited IRA as a nonspouse beneficiary"}`
- Cite: [f8880] p. 2, Line 4, "If you’re filing a joint return, include both spouses’ amounts in both columns. Exception. Don’t include your spouse’s distributions with yours when entering an amount on line 4 if you and your spouse didn’t file a joint return for the year the distribution was received" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.sav_prior_other`

- **Authored helper label:** Your distributions in 2023 and 2024 from years for which you did not file a joint return with your spouse on this return (on a return that is not joint, all of your 2023, 2024 and early-2026 distributions)
- **Encoded (NonNegDollars):** Input — The distributions you received in 2023 and 2024 in a year for which you did not file a joint return with your spouse on this return (on a return that is not a joint return: all your distributions in 2023 and 2024, and in 2026 before the due date of your 2025 return, including extensions), from any of the following; zero if none

  - a traditional or Roth IRA
  - a 401(k), 403(b), governmental 457(b), 501(c)(18)(D), SEP or SIMPLE plan, or the federal TSP
  - another qualified retirement plan

  Do not include:
  - rollovers or trustee-to-trustee transfers
  - in-plan Roth rollovers
  - amounts rolled over or converted to a Roth IRA
  - plan loans treated as distributions
  - distributions of excess contributions or deferrals
  - IRA contributions returned by the due date
  - section 404(k) dividends
  - distributions from a military retirement plan (other than the TSP)
  - distributions from an inherited IRA as a nonspouse beneficiary
- **Refusal:** when person.sav_able is true, cannot complete ABLE account contributions or distributions on Form 8880 (Pub. 907). Contributions to an ABLE account by its designated beneficiary (line 1) and ABLE distributions (line 4) are outside this tool. Cite: [f8880] p. 2, What’s New, "See Pub. 907, Tax Highlights for Persons With Disabilities, for more information about ABLE accounts" (2025; created 2025-11-04; sha256 ba2b2877)
- Expr: `{"op":"input","source":"The distributions you received in 2023 and 2024 in a year for which you did not file a joint return with your spouse on this return (on a return that is not a joint return: all your distributions in 2023 and 2024, and in 2026 before the due date of your 2025 return, including extensions), from any of the following; zero if none\n\n- a traditional or Roth IRA\n- a 401(k), 403(b), governmental 457(b), 501(c)(18)(D), SEP or SIMPLE plan, or the federal TSP\n- another qualified retirement plan\n\nDo not include:\n- rollovers or trustee-to-trustee transfers\n- in-plan Roth rollovers\n- amounts rolled over or converted to a Roth IRA\n- plan loans treated as distributions\n- distributions of excess contributions or deferrals\n- IRA contributions returned by the due date\n- section 404(k) dividends\n- distributions from a military retirement plan (other than the TSP)\n- distributions from an inherited IRA as a nonspouse beneficiary"}`
- Cite: [f8880] p. 2, Line 4, "Enter the total amount of distributions you, and your spouse if filing jointly, received after 2022 and before the due date of your 2025 return (including extensions)"; "Exception. Don’t include your spouse’s distributions with yours when entering an amount on line 4 if you and your spouse didn’t file a joint return for the year the distribution was received" (2025; created 2025-11-04; sha256 ba2b2877)

## (helper) — `person.ira_trad`

- **Authored helper label:** Your traditional IRA contributions for 2025 (not rollovers)
- **Encoded (NonNegDollars):** Input — Your contributions to your traditional IRAs for 2025, made in 2025 or by the due date of your 2025 return not counting extensions (April 15, 2026, for most people), and designated for 2025; do not include rollover contributions, repayments of qualified reservist distributions, contributions made in 2025 that you deducted for 2024, contributions withdrawn (with their earnings) by the due date of your return, trustees' fees billed separately, or contributions made under a SEP or SIMPLE IRA plan, by your employer or by you for yourself as a self-employed person
- Expr: `{"op":"input","source":"Your contributions to your traditional IRAs for 2025, made in 2025 or by the due date of your 2025 return not counting extensions (April 15, 2026, for most people), and designated for 2025; do not include rollover contributions, repayments of qualified reservist distributions, contributions made in 2025 that you deducted for 2024, contributions withdrawn (with their earnings) by the due date of your return, trustees' fees billed separately, or contributions made under a SEP or SIMPLE IRA plan, by your employer or by you for yourself as a self-employed person"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 11, "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions (April 15, 2026, for most people), for 2025"; p. 95, Line 20, "If you made contributions to your IRA in 2025 that you deducted for 2024, don’t include them in the worksheet", "Don’t include rollover contributions in figuring your deduction", "Don’t include trustees’ fees that were billed separately" and "Don’t include any repayments of qualified reservist distributions" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_contrib`

- **Authored helper label:** This person's traditional IRA contributions for 2025 (zero if the traditional IRA question was answered No)
- **Encoded (NonNegDollars):** Choose — [helper "Made traditional IRA contributions for 2025 (asked only of a person with an IRA; otherwise no)" = true → helper "Your traditional IRA contributions for 2025 (not rollovers)"] [helper "Made traditional IRA contributions for 2025 (asked only of a person with an IRA; otherwise no)" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.sav_trad_if_ira_owner",{"const":true}],"op":"test"},"then":"person.ira_trad"},{"guard":{"eq":["person.sav_trad_if_ira_owner",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 11, "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions (April 15, 2026, for most people), for 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_has`

- **Authored helper label:** This person made traditional IRA contributions for 2025
- **Encoded (Bool):** helper "This person's traditional IRA contributions for 2025 (zero if the traditional IRA question was answered No)" > $0 (sales.zero)
- Expr: `{"gt":["person.ira_contrib",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 95, Line 20, "If you made contributions to a traditional IRA for 2025, you may be able to take an IRA deduction" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_any_contrib`

- **Authored helper label:** This person made traditional or Roth IRA contributions for 2025
- **Encoded (Bool):** (helper "This person made traditional IRA contributions for 2025" = true or helper "Roth IRA contributions for 2025 (asked only of a person with an IRA; otherwise zero)" > $0 (sales.zero))
- Expr: `{"any":[{"eq":["person.ira_has",{"const":true}],"op":"test"},{"gt":["person.sav_roth_if_ira_owner",{"param":"sales.zero"}],"op":"test"}],"op":"test"}`
- Cite: [f8880] Form 8880 (2025), line 1, "Traditional and Roth IRA contributions" (2025; created 2025-11-04; sha256 ba2b2877)

## (screen) — `person.ira_excess`

- **Authored helper label:** This person's 2025 IRA contributions were more than allowed and not withdrawn, or were recharacterized
- **Encoded (Bool):** (helper "Were the contributions for 2025 to your traditional and Roth IRAs together (made by you, your spouse or an employer, other than under a SEP or SIMPLE IRA plan, and any rollover that did not qualify) more than you were allowed to contribute (more than $7,000, or $8,000 if age 50 or older at the end of 2025, or more than your taxable compensation, or, on a joint return, the couple's taxable compensation less the other spouse's IRA contributions, or a Roth contribution above the limit for your income), with the excess not withdrawn with its earnings by the due date of your return (including extensions)?" = true or helper "Did you recharacterize a 2025 contribution (move it from a traditional to a Roth IRA or the reverse)?" = true)
- Expr: `{"any":[{"eq":["person.ira_extra_left",{"const":true}],"op":"test"},{"eq":["person.ira_recharacterized",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [p590a] p. 35, Excess Contributions, "Generally, an excess contribution is the amount contributed to your traditional IRAs for the year that is more than the smaller of"; p. 35, Tax on Excess Contributions, "In general, if the excess contributions for a year aren’t withdrawn by the date your return for the year is due (including extensions), you are subject to a 6% tax"; p. 30, "Recharacterizing excess contributions"; i1040gi p. 95, Line 20, "If the total of your IRA deduction on line 20 plus any nondeductible contributions to your traditional IRAs shown on Form 8606 is less than your total traditional IRA contributions for 2025, see Pub. 590-A for special rules" (2025; sha256 ca0e4287)

## (screen) — `person.ira_extra_left`

- **Authored helper label:** Were the contributions for 2025 to your traditional and Roth IRAs together (made by you, your spouse or an employer, other than under a SEP or SIMPLE IRA plan, and any rollover that did not qualify) more than you were allowed to contribute (more than $7,000, or $8,000 if age 50 or older at the end of 2025, or more than your taxable compensation, or, on a joint return, the couple's taxable compensation less the other spouse's IRA contributions, or a Roth contribution above the limit for your income), with the excess not withdrawn with its earnings by the due date of your return (including extensions)?
- **Encoded (Bool):** Input — Were the contributions for 2025 to your traditional and Roth IRAs together (made by you, your spouse or an employer, other than under a SEP or SIMPLE IRA plan, and any rollover that did not qualify) more than you were allowed to contribute (more than $7,000, or $8,000 if age 50 or older at the end of 2025, or more than your taxable compensation, or, on a joint return, the couple's taxable compensation less the other spouse's IRA contributions, or a Roth contribution above the limit for your income), with the excess not withdrawn with its earnings by the due date of your return (including extensions)?
- Expr: `{"op":"input","source":"Were the contributions for 2025 to your traditional and Roth IRAs together (made by you, your spouse or an employer, other than under a SEP or SIMPLE IRA plan, and any rollover that did not qualify) more than you were allowed to contribute (more than $7,000, or $8,000 if age 50 or older at the end of 2025, or more than your taxable compensation, or, on a joint return, the couple's taxable compensation less the other spouse's IRA contributions, or a Roth contribution above the limit for your income), with the excess not withdrawn with its earnings by the due date of your return (including extensions)?"}`
- Cite: [p590a] p. 35, Excess Contributions, "Generally, an excess contribution is the amount contributed to your traditional IRAs for the year that is more than the smaller of"; p. 35, Tax on Excess Contributions, "In general, if the excess contributions for a year aren’t withdrawn by the date your return for the year is due (including extensions), you are subject to a 6% tax"; p. 30, "Recharacterizing excess contributions"; i1040gi p. 95, Line 20, "If the total of your IRA deduction on line 20 plus any nondeductible contributions to your traditional IRAs shown on Form 8606 is less than your total traditional IRA contributions for 2025, see Pub. 590-A for special rules" (2025; sha256 ca0e4287)

## (screen) — `person.ira_recharacterized`

- **Authored helper label:** Did you recharacterize a 2025 contribution (move it from a traditional to a Roth IRA or the reverse)?
- **Encoded (Bool):** Input — Did you recharacterize a 2025 contribution (move it from a traditional to a Roth IRA or the reverse)?
- Expr: `{"op":"input","source":"Did you recharacterize a 2025 contribution (move it from a traditional to a Roth IRA or the reverse)?"}`
- Cite: [p590a] p. 35, Excess Contributions, "Generally, an excess contribution is the amount contributed to your traditional IRAs for the year that is more than the smaller of"; p. 35, Tax on Excess Contributions, "In general, if the excess contributions for a year aren’t withdrawn by the date your return for the year is due (including extensions), you are subject to a 6% tax"; p. 30, "Recharacterizing excess contributions"; i1040gi p. 95, Line 20, "If the total of your IRA deduction on line 20 plus any nondeductible contributions to your traditional IRAs shown on Form 8606 is less than your total traditional IRA contributions for 2025, see Pub. 590-A for special rules" (2025; sha256 ca0e4287)

## (gate) — `person.ira_excess_gate`

- **Authored helper label:** This person's IRA contributions for 2025 are excess or recharacterized, or an earlier excess remained at the end of 2025 (screen)
- **Encoded (Bool):** Choose — [helper "This person made traditional or Roth IRA contributions for 2025" = true → helper "This person's 2025 IRA contributions were more than allowed and not withdrawn, or were recharacterized"] [helper "This person made traditional or Roth IRA contributions for 2025" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_any_contrib",{"const":true}],"op":"test"},"then":"person.ira_excess"},{"guard":{"eq":["person.ira_any_contrib",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [p590a] p. 35, Excess Contributions, "In general, if the excess contributions for a year aren’t withdrawn by the date your return for the year is due (including extensions), you are subject to a 6% tax" (2025; sha256 ca0e4287)

## (helper) — `person.ira_age50`

- **Authored helper label:** Age 50 or older at the end of 2025
- **Encoded (Bool):** (helper "The year you were born" < 1976 (age.cut_50) or helper "The year you were born" = 1976 (age.cut_50) and helper "Age 50 or older at the end of 2025, as stated by a person born in 1976 (otherwise no)" = true)
- Interpretation: amb.2025.ira_age50
- Expr: `{"any":[{"lt":["person.birth_year",{"param":"age.cut_50"}],"op":"test"},{"all":[{"eq":["person.birth_year",{"param":"age.cut_50"}],"op":"test"},{"eq":["person.age50_at_year_end_if_open_year",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "$8,000 if age 50 or older at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.age50_open_year`

- **Authored helper label:** Born in 1976
- **Encoded (Bool):** helper "The year you were born" = 1976 (age.cut_50)
- Expr: `{"eq":["person.birth_year",{"param":"age.cut_50"}],"op":"test"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "$8,000 if age 50 or older at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.age50_at_year_end`

- **Authored helper label:** Were you age 50 or older at the end of 2025?
- **Encoded (Bool):** Input — Were you age 50 or older at the end of 2025?
- Interpretation: amb.2025.ira_age50
- Expr: `{"op":"input","source":"Were you age 50 or older at the end of 2025?"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "$8,000 if age 50 or older at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `person.age50_at_year_end_if_open_year`

- **Authored helper label:** Age 50 or older at the end of 2025, as stated by a person born in 1976 (otherwise no)
- **Encoded (Bool):** Choose — [helper "Born in 1976" = true → helper "Were you age 50 or older at the end of 2025?"] [helper "Born in 1976" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.age50_open_year",{"const":true}],"op":"test"},"then":"person.age50_at_year_end"},{"guard":{"eq":["person.age50_open_year",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "$8,000 if age 50 or older at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.age55_open_year`

- **Authored helper label:** Born in 1971
- **Encoded (Bool):** helper "The year you were born" = 1971 (age.cut_55)
- Expr: `{"eq":["person.birth_year",{"param":"age.cut_55"}],"op":"test"}`
- Cite: [i8889] p. 4, Line 3, rule 6, "If, at the end of 2025, you were age 55 or older"; p. 6, Line 3 Limitation Chart, "If you were age 55 or older at the end of 2025" (2025; sha256 da6f2f58)

## (helper) — `person.age55_at_year_end`

- **Authored helper label:** Were you age 55 or older at the end of 2025?
- **Encoded (Bool):** Input — Were you age 55 or older at the end of 2025?
- Expr: `{"op":"input","source":"Were you age 55 or older at the end of 2025?"}`
- Cite: [i8889] p. 4, Line 3, rule 6, "If, at the end of 2025, you were age 55 or older"; p. 6, Line 3 Limitation Chart, "If you were age 55 or older at the end of 2025" (2025; sha256 da6f2f58)

## (gate) — `person.age55_at_year_end_if_open_year`

- **Authored helper label:** Age 55 or older at the end of 2025, as stated by a person born in 1971 (otherwise no)
- **Encoded (Bool):** Choose — [helper "Born in 1971" = true → helper "Were you age 55 or older at the end of 2025?"] [helper "Born in 1971" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.age55_open_year",{"const":true}],"op":"test"},"then":"person.age55_at_year_end"},{"guard":{"eq":["person.age55_open_year",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [i8889] p. 4, Line 3, rule 6, "If, at the end of 2025, you were age 55 or older"; p. 6, Line 3 Limitation Chart, "If you were age 55 or older at the end of 2025" (2025; sha256 da6f2f58)

## (helper) — `person.ira_work_plan`

- **Authored helper label:** Were you covered by a retirement plan at work in 2025?
- **Encoded (Bool):** Input — Were you covered by a retirement plan at work for 2025 (a qualified pension, profit-sharing or 401(k), annuity, SEP, SIMPLE or other employer plan), even if you were not vested in it?
- Interpretation: amb.2025.ira_covered
- Expr: `{"op":"input","source":"Were you covered by a retirement plan at work for 2025 (a qualified pension, profit-sharing or 401(k), annuity, SEP, SIMPLE or other employer plan), even if you were not vested in it?"}`
- Cite: [i1040gi] p. 96, Were You Covered by a Retirement Plan?, "profit-sharing (including 401(k)), annuity, SEP, SIMPLE, etc.) at work or through self-employment" and "The “Retirement plan” box in box 13 of your Form W-2 should be checked if you were covered by a plan at work even if you weren’t vested in the plan" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_se_plan`

- **Authored helper label:** This person contributed for themselves to a SEP or SIMPLE IRA as a self-employed person (person.plan)
- **Encoded (Bool):** helper "This person has at least one Schedule C" = true and not helper "Retirement plan of this self-employed person" = 'none'
- Interpretation: amb.2025.ira_covered
- Expr: `{"all":[{"eq":["person.has_sc",{"const":true}],"op":"test"},{"not":{"eq":["person.plan",{"const":"none"}],"op":"test"},"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 96, Were You Covered by a Retirement Plan?, "You are also covered by a plan if you were self-employed and had a SEP, SIMPLE, or qualified retirement plan" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_cov`

- **Authored helper label:** Covered by a retirement plan (worksheet line 1a or 1b for this person)
- **Encoded (Bool):** (helper "Were you covered by a retirement plan at work in 2025?" = true or helper "This person contributed for themselves to a SEP or SIMPLE IRA as a self-employed person (person.plan)" = true)
- Interpretation: amb.2025.ira_covered
- Expr: `{"any":[{"eq":["person.ira_work_plan",{"const":true}],"op":"test"},{"eq":["person.ira_se_plan",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 1, "Were you covered by a retirement plan (see Were You Covered by a Retirement Plan)?" and "If married filing jointly, was your spouse covered by a retirement plan?" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_limit_under50`

- **Authored helper label:** $7,000
- **Encoded (NonNegDollars):** Enter $7,000 (ira.limit).
- Expr: `{"op":"param","ref":"ira.limit"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "$7,000 if under age 50 at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_limit_over50`

- **Authored helper label:** $8,000
- **Encoded (NonNegDollars):** Enter $8,000 (ira.limit_50).
- Expr: `{"op":"param","ref":"ira.limit_50"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "$8,000 if age 50 or older at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_limit`

- **Authored helper label:** The applicable amount for this person ($7,000 if under age 50 at the end of 2025; $8,000 if age 50 or older)
- **Encoded (NonNegDollars):** Choose — [helper "Age 50 or older at the end of 2025" = true → helper "$8,000"] [helper "Age 50 or older at the end of 2025" = false → helper "$7,000"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_age50",{"const":true}],"op":"test"},"then":"person.ira_limit_over50"},{"guard":{"eq":["person.ira_age50",{"const":false}],"op":"test"},"then":"person.ira_limit_under50"}],"op":"choose"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "$7,000 if under age 50 at the end of 2025" and "$8,000 if age 50 or older at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_not_covered_joint`

- **Authored helper label:** Married filing jointly and this person was not covered by a retirement plan
- **Encoded (Bool):** ira helper "Married filing jointly" = true and helper "Covered by a retirement plan (worksheet line 1a or 1b for this person)" = false
- Expr: `{"all":[{"eq":["ira.joint",{"const":true}],"op":"test"},{"eq":["person.ira_cov",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 2, "But if you checked “No” on either line 1a or 1b, enter $246,000 for the person who wasn’t covered by a plan" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_line2_table`

- **Authored helper label:** The line 2 amount for the filing status ($89,000; $146,000 if married filing jointly or qualifying surviving spouse; $10,000 if married filing separately)
- **Encoded (NonNegDollars):** Enter single $89,000; mfj $146,000; mfs $10,000; hoh $89,000; qss $146,000 (ira.line2).
- Expr: `{"op":"param","ref":"ira.line2"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 2, "Enter the amount shown below that applies to you" and "Married filing separately and you lived with your spouse at any time in 2025, enter $10,000" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_line2_apart`

- **Authored helper label:** $89,000 (married filing separately and lived apart from your spouse for all of 2025)
- **Encoded (NonNegDollars):** Enter $89,000 (ira.line2_apart).
- Expr: `{"op":"param","ref":"ira.line2_apart"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 2, "Single, head of household, or married filing separately and you lived apart from your spouse for all of 2025, enter $89,000" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_line2_status`

- **Authored helper label:** The line 2 amount for the filing status ($89,000; $146,000 if married filing jointly or qualifying surviving spouse; married filing separately, $89,000 if you lived apart from your spouse for all of 2025 and $10,000 otherwise)
- **Encoded (NonNegDollars):** Choose — [household helper "Married filing separately, and you lived apart from your spouse for all of 2025" = true → helper "$89,000 (married filing separately and lived apart from your spouse for all of 2025)"] [household helper "Married filing separately, and you lived apart from your spouse for all of 2025" = false → helper "The line 2 amount for the filing status ($89,000; $146,000 if married filing jointly or qualifying surviving spouse; $10,000 if married filing separately)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.mfs_apart_all_year",{"const":true}],"op":"test"},"then":"person.ira_line2_apart"},{"guard":{"eq":["household.mfs_apart_all_year",{"const":false}],"op":"test"},"then":"person.ira_line2_table"}],"op":"choose"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 2, "Single, head of household, or married filing separately and you lived apart from your spouse for all of 2025, enter $89,000" and "Married filing separately and you lived with your spouse at any time in 2025, enter $10,000" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_line2_nc`

- **Authored helper label:** $246,000
- **Encoded (NonNegDollars):** Enter $246,000 (ira.line2_not_covered).
- Expr: `{"op":"param","ref":"ira.line2_not_covered"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 2, "enter $246,000 for the person who wasn’t covered by a plan" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_line2`

- **Authored helper label:** Worksheet line 2 for this person's column
- **Encoded (NonNegDollars):** Choose — [helper "Married filing jointly and this person was not covered by a retirement plan" = true → helper "$246,000"] [helper "Married filing jointly and this person was not covered by a retirement plan" = false → helper "The line 2 amount for the filing status ($89,000; $146,000 if married filing jointly or qualifying surviving spouse; married filing separately, $89,000 if you lived apart from your spouse for all of 2025 and $10,000 otherwise)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_not_covered_joint",{"const":true}],"op":"test"},"then":"person.ira_line2_nc"},{"guard":{"eq":["person.ira_not_covered_joint",{"const":false}],"op":"test"},"then":"person.ira_line2_status"}],"op":"choose"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 2, "Married filing jointly, enter $146,000 in both columns. But if you checked “No” on either line 1a or 1b, enter $246,000 for the person who wasn’t covered by a plan" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_line6`

- **Authored helper label:** Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, subtract line 5 from line 2 (if no, zero: none of the contributions are deductible)
- **Encoded (NonNegDollars):** Subtract ira line 5 from helper "Worksheet line 2 for this person's column". If zero or less, enter -0-.
- Expr: `{"from":"person.ira_line2","op":"subtract_floor0","take":"ira.line5"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "Is the amount on line 5 less than the amount on line 2?", "None of your IRA contributions are deductible" and "Subtract line 5 from line 2 in each column" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_line6_yes`

- **Authored helper label:** Line 5 is less than line 2 in this person's column (line 6, Yes)
- **Encoded (Bool):** helper "Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, subtract line 5 from line 2 (if no, zero: none of the contributions are deductible)" > $0 (sales.zero)
- Expr: `{"gt":["person.ira_line6",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "Is the amount on line 5 less than the amount on line 2?" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_wide`

- **Authored helper label:** This column takes the single rule (70% or 80%, the $10,000 threshold) — not married filing jointly or qualifying surviving spouse, or the column of a person who wasn't covered by a retirement plan
- **Encoded (Bool):** (ira helper "Married filing jointly or qualifying surviving spouse" = false or helper "Covered by a retirement plan (worksheet line 1a or 1b for this person)" = false)
- Expr: `{"any":[{"eq":["ira.joint_type",{"const":false}],"op":"test"},{"eq":["person.ira_cov",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "($10,000 or more in the column for the IRA of a person who wasn’t covered by a retirement plan)"; p. 98, IRA Deduction Worksheet—Continued, line 7, "then in the column for the IRA of the person who wasn’t covered by a retirement plan, multiply by 70% (0.70)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_full_narrow`

- **Authored helper label:** $10,000
- **Encoded (NonNegDollars):** Enter $10,000 (ira.full_narrow).
- Expr: `{"op":"param","ref":"ira.full_narrow"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "and the result is $10,000 or more" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_full_joint`

- **Authored helper label:** $20,000
- **Encoded (NonNegDollars):** Enter $20,000 (ira.full_joint).
- Expr: `{"op":"param","ref":"ira.full_joint"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "and the result is $20,000 or more" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_full`

- **Authored helper label:** The line 6 result at or above which this column takes the applicable amount ($10,000 or $20,000)
- **Encoded (NonNegDollars):** Choose — [helper "This column takes the single rule (70% or 80%, the $10,000 threshold) — not married filing jointly or qualifying surviving spouse, or the column of a person who wasn't covered by a retirement plan" = true → helper "$10,000"] [helper "This column takes the single rule (70% or 80%, the $10,000 threshold) — not married filing jointly or qualifying surviving spouse, or the column of a person who wasn't covered by a retirement plan" = false → helper "$20,000"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_wide",{"const":true}],"op":"test"},"then":"person.ira_full_narrow"},{"guard":{"eq":["person.ira_wide",{"const":false}],"op":"test"},"then":"person.ira_full_joint"}],"op":"choose"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "If single, head of household, or married filing separately, and the result is $10,000 or more" and "If married filing jointly or qualifying surviving spouse, and the result is $20,000 or more ($10,000 or more in the column for the IRA of a person who wasn’t covered by a retirement plan)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_at_full`

- **Authored helper label:** The line 6 result is at or above the threshold (enter the applicable amount on line 7)
- **Encoded (Bool):** helper "Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, subtract line 5 from line 2 (if no, zero: none of the contributions are deductible)" ≥ helper "The line 6 result at or above which this column takes the applicable amount ($10,000 or $20,000)"
- Expr: `{"ge":["person.ira_line6","person.ira_full"],"op":"test"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "enter the applicable amount below on line 7 for that column and go to line 8" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_p70`

- **Authored helper label:** Line 6 multiplied by 70% (0.70)
- **Encoded (NonNegDollars):** Multiply helper "Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, subtract line 5 from line 2 (if no, zero: none of the contributions are deductible)" by 70% (0.70) (ira.rate_70).
- Expr: `{"amount":"person.ira_line6","op":"multiply_rate","rate":{"param":"ira.rate_70"}}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "multiply by 70% (0.70)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_p80`

- **Authored helper label:** Line 6 multiplied by 80% (0.80)
- **Encoded (NonNegDollars):** Multiply helper "Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, subtract line 5 from line 2 (if no, zero: none of the contributions are deductible)" by 80% (0.80) (ira.rate_80).
- Expr: `{"amount":"person.ira_line6","op":"multiply_rate","rate":{"param":"ira.rate_80"}}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "or by 80% (0.80)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_p35`

- **Authored helper label:** Line 6 multiplied by 35% (0.35)
- **Encoded (NonNegDollars):** Multiply helper "Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, subtract line 5 from line 2 (if no, zero: none of the contributions are deductible)" by 35% (0.35) (ira.rate_35).
- Expr: `{"amount":"person.ira_line6","op":"multiply_rate","rate":{"param":"ira.rate_35"}}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "multiply by 35% (0.35)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_p40`

- **Authored helper label:** Line 6 multiplied by 40% (0.40)
- **Encoded (NonNegDollars):** Multiply helper "Worksheet line 6 for this person's column: is line 5 less than line 2? If yes, subtract line 5 from line 2 (if no, zero: none of the contributions are deductible)" by 40% (0.40) (ira.rate_40).
- Expr: `{"amount":"person.ira_line6","op":"multiply_rate","rate":{"param":"ira.rate_40"}}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "or by 40% (0.40)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_prod_wide`

- **Authored helper label:** Line 6 multiplied by 70% (0.70), or by 80% (0.80) for a person age 50 or older at the end of 2025
- **Encoded (NonNegDollars):** Choose — [helper "Age 50 or older at the end of 2025" = true → helper "Line 6 multiplied by 80% (0.80)"] [helper "Age 50 or older at the end of 2025" = false → helper "Line 6 multiplied by 70% (0.70)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_age50",{"const":true}],"op":"test"},"then":"person.ira_p80"},{"guard":{"eq":["person.ira_age50",{"const":false}],"op":"test"},"then":"person.ira_p70"}],"op":"choose"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "Single, head of household, or married filing separately, multiply by 70% (0.70) (or by 80% (0.80) in the column for the IRA of a person who is age 50 or older at the end of 2025)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_prod_joint`

- **Authored helper label:** Line 6 multiplied by 35% (0.35), or by 40% (0.40) for a person age 50 or older at the end of 2025
- **Encoded (NonNegDollars):** Choose — [helper "Age 50 or older at the end of 2025" = true → helper "Line 6 multiplied by 40% (0.40)"] [helper "Age 50 or older at the end of 2025" = false → helper "Line 6 multiplied by 35% (0.35)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_age50",{"const":true}],"op":"test"},"then":"person.ira_p40"},{"guard":{"eq":["person.ira_age50",{"const":false}],"op":"test"},"then":"person.ira_p35"}],"op":"choose"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "Married filing jointly or qualifying surviving spouse, multiply by 35% (0.35) (or by 40% (0.40) in the column for the IRA of a person who is age 50 or older at the end of 2025)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_prod`

- **Authored helper label:** Line 6 multiplied by the percentage that applies to this column
- **Encoded (NonNegDollars):** Choose — [helper "This column takes the single rule (70% or 80%, the $10,000 threshold) — not married filing jointly or qualifying surviving spouse, or the column of a person who wasn't covered by a retirement plan" = true → helper "Line 6 multiplied by 70% (0.70), or by 80% (0.80) for a person age 50 or older at the end of 2025"] [helper "This column takes the single rule (70% or 80%, the $10,000 threshold) — not married filing jointly or qualifying surviving spouse, or the column of a person who wasn't covered by a retirement plan" = false → helper "Line 6 multiplied by 35% (0.35), or by 40% (0.40) for a person age 50 or older at the end of 2025"]
- Interpretation: amb.2025.ira_line7_cents
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_wide",{"const":true}],"op":"test"},"then":"person.ira_prod_wide"},{"guard":{"eq":["person.ira_wide",{"const":false}],"op":"test"},"then":"person.ira_prod_joint"}],"op":"choose"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "Multiply lines 6a and 6b by the percentage below that applies to you" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_rounded`

- **Authored helper label:** If the result isn't a multiple of $10, increase it to the next multiple of $10
- **Encoded (NonNegDollars):** Round helper "Line 6 multiplied by the percentage that applies to this column" up to the next multiple of $10.
- Expr: `{"of":"person.ira_prod","op":"round","rule":"up","unit":1000}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "If the result isn’t a multiple of $10, increase it to the next multiple of $10 (for example, increase $490.30 to $500)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_min`

- **Authored helper label:** $200
- **Encoded (NonNegDollars):** Enter $200 (ira.min).
- Expr: `{"op":"param","ref":"ira.min"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "But if it is less than $200, enter $200" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_floor`

- **Authored helper label:** If the result is $200 or more, enter the result; but if it is less than $200, enter $200
- **Encoded (NonNegDollars):** Enter the larger of helper "If the result isn't a multiple of $10, increase it to the next multiple of $10" or helper "$200".
- Expr: `{"of":["person.ira_rounded","person.ira_min"],"op":"larger_of"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 7, "If the result is $200 or more, enter the result. But if it is less than $200, enter $200" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_below`

- **Authored helper label:** Line 7 when the line 6 result is under the threshold (zero when line 6 is No)
- **Encoded (NonNegDollars):** Choose — [helper "Line 5 is less than line 2 in this person's column (line 6, Yes)" = true → helper "If the result is $200 or more, enter the result; but if it is less than $200, enter $200"] [helper "Line 5 is less than line 2 in this person's column (line 6, Yes)" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_line6_yes",{"const":true}],"op":"test"},"then":"person.ira_floor"},{"guard":{"eq":["person.ira_line6_yes",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "None of your IRA contributions are deductible"; p. 98, IRA Deduction Worksheet—Continued, line 7 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_line7_figured`

- **Authored helper label:** Line 7 when someone is covered by a retirement plan (lines 2 through 6 completed)
- **Encoded (NonNegDollars):** Choose — [helper "The line 6 result is at or above the threshold (enter the applicable amount on line 7)" = true → helper "The applicable amount for this person ($7,000 if under age 50 at the end of 2025; $8,000 if age 50 or older)"] [helper "The line 6 result is at or above the threshold (enter the applicable amount on line 7)" = false → helper "Line 7 when the line 6 result is under the threshold (zero when line 6 is No)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_at_full",{"const":true}],"op":"test"},"then":"person.ira_limit"},{"guard":{"eq":["person.ira_at_full",{"const":false}],"op":"test"},"then":"person.ira_below"}],"op":"choose"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 6, "enter the applicable amount below on line 7 for that column and go to line 8" and "Otherwise, go to line 7" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_line7`

- **Authored helper label:** Worksheet line 7 for this person's column
- **Encoded (NonNegDollars):** Choose — [ira helper "You (or, on a joint return, your spouse) were covered by a retirement plan, or, married filing separately, are considered covered through your spouse (Yes on line 1a or 1b)" = true → helper "Line 7 when someone is covered by a retirement plan (lines 2 through 6 completed)"] [ira helper "You (or, on a joint return, your spouse) were covered by a retirement plan, or, married filing separately, are considered covered through your spouse (Yes on line 1a or 1b)" = false → helper "The applicable amount for this person ($7,000 if under age 50 at the end of 2025; $8,000 if age 50 or older)"]
- Expr: `{"alternatives":[{"guard":{"eq":["ira.anyone_covered",{"const":true}],"op":"test"},"then":"person.ira_line7_figured"},{"guard":{"eq":["ira.anyone_covered",{"const":false}],"op":"test"},"then":"person.ira_limit"}],"op":"choose"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "If you checked “No” on line 1a (and “No” on line 1b if married filing jointly), skip lines 2 through 6, enter the applicable amount below on line 7a (and line 7b, if applicable), and go to line 8" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `person.ira_over_limit`

- **Authored helper label:** This person's traditional and Roth IRA contributions for 2025 together are more than the applicable amount
- **Encoded (Bool):** helper "This person made traditional IRA contributions for 2025" = true and helper "This person's traditional and Roth IRA contributions for 2025" > helper "The applicable amount for this person ($7,000 if under age 50 at the end of 2025; $8,000 if age 50 or older)"
- Expr: `{"all":[{"eq":["person.ira_has",{"const":true}],"op":"test"},{"gt":["person.ira_own_total","person.ira_limit"],"op":"test"}],"op":"test"}`
- Cite: [p590a] p. 35, Excess Contributions, "Generally, an excess contribution is the amount contributed to your traditional IRAs for the year that is more than the smaller of: • $7,000 ($8,000 if you are age 50 or older), or • Your taxable compensation for the year" (2025; sha256 ca0e4287)

## (helper) — `person.ira_own_total`

- **Authored helper label:** This person's traditional and Roth IRA contributions for 2025
- **Encoded (NonNegDollars):** Add helper "This person's traditional IRA contributions for 2025 (zero if the traditional IRA question was answered No)" and helper "Roth IRA contributions for 2025 (asked only of a person with an IRA; otherwise zero)".
- Expr: `{"of":["person.ira_contrib","person.sav_roth_if_ira_owner"],"op":"sum"}`
- Cite: [i8606] p. 5, Overall Contribution Limit for Traditional and Roth IRAs, "your limit on contributions to traditional and Roth IRAs is generally the smaller of $7,000 ($8,000 if age 50 or older at the end of 2025) or your taxable compensation" (2025; sha256 735fb7ae)

## (helper) — `person.ira_line11`

- **Authored helper label:** Worksheet line 11 for this person's column (traditional IRA contributions for 2025)
- **Encoded (NonNegDollars):** Enter the amount from helper "This person's traditional IRA contributions for 2025 (zero if the traditional IRA question was answered No)".
- **Refusal:** when ira.both_kinds is true, cannot complete Traditional and Roth IRA contributions on a joint return (Pub. 590-A). On a joint return where you or your spouse made contributions to both a traditional IRA and a Roth IRA for 2025, the IRA deduction is figured with Pub. 590-A, which this tool does not prepare. Cite: [i1040gi] p. 95, Line 20, "If you are filing a joint return and you or your spouse made contributions to both a traditional IRA and a Roth IRA for 2025, don’t use the IRA Deduction Worksheet in these instructions" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when ira.kbh_short is true, cannot complete IRA deduction on a joint return with little compensation (Pub. 590-A worksheet). On a joint return with line 10 of the IRA Deduction Worksheet under $14,000 ($15,000 or $16,000 with spouses age 50 or older), the IRA deduction is figured with the worksheet in Pub. 590-A, which this tool does not prepare. Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, Caution, "stop here and use the worksheet in Pub. 590-A to figure your IRA deduction" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when person.ira_excess_gate is true, cannot complete Excess or recharacterized IRA contributions (Form 5329 Parts III and IV, Pub. 590-A). Traditional or Roth IRA contributions for 2025 that are more than allowed or were recharacterized, and an excess contribution from an earlier year that remained in an IRA at the end of 2025, are outside this tool. Cite: [i1040gi] p. 95, Line 20, "If the total of your IRA deduction on line 20 plus any nondeductible contributions to your traditional IRAs shown on Form 8606 is less than your total traditional IRA contributions for 2025, see Pub. 590-A for special rules" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when person.ira_over_limit is true, cannot complete Excess IRA contributions (Form 5329 Part III, Pub. 590-A). Your traditional and Roth IRA contributions for 2025 are together more than $7,000 ($8,000 if age 50 or older), an excess contribution, which is outside this tool. Cite: [p590a] p. 35, Excess Contributions, "Generally, an excess contribution is the amount contributed to your traditional IRAs for the year that is more than the smaller of" (2025; sha256 ca0e4287)
- **Refusal:** when ira.over_comp is true, cannot complete Excess IRA contributions (Form 5329 Part III, Pub. 590-A). The traditional and Roth IRA contributions for 2025 on this return are more than the compensation on line 10 of the IRA Deduction Worksheet, an excess contribution, which is outside this tool. Cite: [p590a] p. 35, Excess Contributions, "Your taxable compensation for the year" (2025; sha256 ca0e4287)
- **Refusal:** when ira.special_gate is true, cannot complete IRA deduction special cases (Pub. 590-A). Nonqualified deferred compensation in box 1 (Form W-2 box 11 or code Z, Form 1099-MISC box 15), fellowship or stipend payments not on a Form W-2, repayments of qualified reservist distributions and difficulty of care payments change the IRA compensation or contribution limits; they are outside this tool. Cite: [i1040gi] p. 95, Line 20, "don’t include that income on line 8 of the worksheet" and "Don’t include any repayments of qualified reservist distributions"; p590a p. 6, What Is Compensation?, "certain non-tuition fellowship and stipend payments not reported to you on Form W-2 are treated as taxable compensation for IRA purposes" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when ira.excl_gate is true, cannot complete IRA deduction with excluded foreign or possession income (Pub. 590-A). With a retirement plan coverage and Form 2555 (or excluded income from Form 4563 or Puerto Rico), the IRA deduction is figured with Pub. 590-A, which this tool does not prepare. Cite: [i1040gi] p. 96, Were You Covered by a Retirement Plan?, "If you were covered by a retirement plan and you file Form 2555 or 8815, or you exclude employer-provided adoption benefits, see Pub. 590-A to figure the amount, if any, of your IRA deduction" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when ira.combat_gate is true, cannot complete Nontaxable combat pay in IRA compensation (IRA Deduction Worksheet, line 8). Nontaxable combat pay counts as compensation for the IRA deduction; it is outside this tool. Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 8, "Nontaxable combat pay. This amount should be reported in box 12 of Form W-2 with code Q or reported on Form 1040, line 1i" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"from":"person.ira_contrib","op":"copy"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 11, "Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return not counting extensions (April 15, 2026, for most people), for 2025 to your IRA on line 11a and to your spouse’s IRA on line 11b" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_7or10`

- **Authored helper label:** The smaller of line 7 for this column and line 10
- **Encoded (NonNegDollars):** Enter the smaller of helper "Worksheet line 7 for this person's column" or ira line 10.
- Expr: `{"of":["person.ira_line7","ira.line10"],"op":"smaller_of"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 12, "On line 12a, enter the smallest of line 7a, 10, or 11a" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_line12`

- **Authored helper label:** Worksheet line 12 for this person's column (the smallest of line 7, 10 or 11). This is the most you can deduct
- **Encoded (NonNegDollars):** Enter the smaller of helper "The smaller of line 7 for this column and line 10" or helper "Worksheet line 11 for this person's column (traditional IRA contributions for 2025)".
- Interpretation: amb.2025.ira_deduct_less
- Expr: `{"of":["person.ira_7or10","person.ira_line11"],"op":"smaller_of"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 12, "On line 12a, enter the smallest of line 7a, 10, or 11a. On line 12b, enter the smallest of line 7b, 10, or 11b. This is the most you can deduct" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_deduction`

- **Authored helper label:** This person's IRA deduction (worksheet line 12; zero with no traditional IRA contributions)
- **Encoded (NonNegDollars):** Choose — [helper "This person made traditional IRA contributions for 2025" = true → helper "Worksheet line 12 for this person's column (the smallest of line 7, 10 or 11). This is the most you can deduct"] [helper "This person made traditional IRA contributions for 2025" = false → line zero]
- **Refusal:** when person.ira_dist_gate is true, cannot complete Nondeductible IRA contributions with a 2025 distribution or conversion (Form 8606 lines 4 to 13, Pub. 590-B). With nondeductible traditional IRA contributions for 2025 and a 2025 traditional IRA distribution or Roth conversion, the taxable part of the distribution is figured on Form 8606 lines 4 to 13 (Pub. 590-B Worksheet 1-1), which this tool does not prepare. Cite: [p590a] p. 15, Both contributions for 2025 and distributions in 2025, "you must figure the taxable part of the traditional IRA distribution before you can figure your modified AGI" (2025; sha256 ca0e4287)
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_has",{"const":true}],"op":"test"},"then":"person.ira_line12"},{"guard":{"eq":["person.ira_has",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 12, "Add the amounts on lines 12a and 12b and enter the total on Schedule 1, line 20" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_10or11`

- **Authored helper label:** The smaller of line 10 or line 11 of the worksheet for this person
- **Encoded (NonNegDollars):** Enter the smaller of ira line 10 or helper "Worksheet line 11 for this person's column (traditional IRA contributions for 2025)".
- Expr: `{"of":["ira.line10","person.ira_line11"],"op":"smaller_of"}`
- Cite: [i8606] p. 9, Line 1, "subtract line 12 of the worksheet (or the amount you chose to deduct on Schedule 1 (Form 1040), line 20, if less) from the smaller of line 10 or line 11 of the worksheet" (2025; sha256 735fb7ae)

## (helper) — `person.ira_nd_figured`

- **Authored helper label:** Nondeductible contributions figured from the worksheet (the smaller of line 10 or 11, less line 12)
- **Encoded (NonNegDollars):** Subtract helper "Worksheet line 12 for this person's column (the smallest of line 7, 10 or 11). This is the most you can deduct" from helper "The smaller of line 10 or line 11 of the worksheet for this person". If zero or less, enter -0-.
- Expr: `{"from":"person.ira_10or11","op":"subtract_floor0","take":"person.ira_line12"}`
- Cite: [i8606] p. 9, Line 1, "subtract line 12 of the worksheet (or the amount you chose to deduct on Schedule 1 (Form 1040), line 20, if less) from the smaller of line 10 or line 11 of the worksheet. Enter the result on line 1 of Form 8606" (2025; sha256 735fb7ae)

## (helper) — `person.ira_nondeductible`

- **Authored helper label:** This person's nondeductible traditional IRA contributions for 2025 (Form 8606 line 1)
- **Encoded (NonNegDollars):** Choose — [helper "This person made traditional IRA contributions for 2025" = true → helper "Nondeductible contributions figured from the worksheet (the smaller of line 10 or 11, less line 12)"] [helper "This person made traditional IRA contributions for 2025" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_has",{"const":true}],"op":"test"},"then":"person.ira_nd_figured"},{"guard":{"eq":["person.ira_has",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f8606] Form 8606 (2025), line 1, "Enter your nondeductible contributions to traditional IRAs for 2025, including those made for 2025 from January 1, 2026, through April 15, 2026" (2025; sha256 748a2bf2)

## (helper) — `person.ira_files_8606`

- **Authored helper label:** This person files Form 8606 for nondeductible contributions to a traditional IRA for 2025
- **Encoded (Bool):** helper "This person's nondeductible traditional IRA contributions for 2025 (Form 8606 line 1)" > $0 (sales.zero)
- Expr: `{"gt":["person.ira_nondeductible",{"param":"sales.zero"}],"op":"test"}`
- Cite: [i8606] p. 2, Who Must File, "You made nondeductible contributions to a traditional IRA for 2025" (2025; sha256 735fb7ae)

## (helper) — `person.ira_basis`

- **Authored helper label:** Your total basis in traditional IRAs before 2025 (Form 8606 line 2)
- **Encoded (NonNegDollars):** Input — Your total basis in traditional IRAs (Form 8606 line 2): zero if this is the first year you are required to file Form 8606 (you made no nondeductible traditional IRA contributions before 2025); otherwise the amount the Total Basis Chart in the Form 8606 instructions gives for the last Form 8606 you filed (generally line 14 of that form)
- Expr: `{"op":"input","source":"Your total basis in traditional IRAs (Form 8606 line 2): zero if this is the first year you are required to file Form 8606 (you made no nondeductible traditional IRA contributions before 2025); otherwise the amount the Total Basis Chart in the Form 8606 instructions gives for the last Form 8606 you filed (generally line 14 of that form)"}`
- Cite: [i8606] p. 9, Line 2, "Generally, if this is the first year you are required to file Form 8606, enter -0-. Otherwise, use the Total Basis Chart to find the amount to enter on line 2" (2025; sha256 735fb7ae)

## (helper) — `person.ira_basis_adjusted`

- **Authored helper label:** Your traditional IRA basis changed other than by nondeductible contributions
- **Encoded (Bool):** Input — Did your traditional IRA basis change other than by nondeductible contributions? That is: did the last Form 8606 you filed with Part I completed have a Line 15c Worksheet with an amount on line 6; or, since the last Form 8606 you filed (ever, if you have filed none), did you have a return of excess traditional IRA contributions, transfer or receive a traditional IRA incident to divorce, or roll over a nontaxable part of a qualified retirement plan to a traditional IRA that wasn't previously reported on Form 8606, line 2?
- Expr: `{"op":"input","source":"Did your traditional IRA basis change other than by nondeductible contributions? That is: did the last Form 8606 you filed with Part I completed have a Line 15c Worksheet with an amount on line 6; or, since the last Form 8606 you filed (ever, if you have filed none), did you have a return of excess traditional IRA contributions, transfer or receive a traditional IRA incident to divorce, or roll over a nontaxable part of a qualified retirement plan to a traditional IRA that wasn't previously reported on Form 8606, line 2?"}`
- Cite: [i8606] p. 9, Line 2, "you may need to enter an amount that is more than -0- (even if this is the first year you are required to file Form 8606) or increase or decrease the amount from the chart"; p. 9, Total Basis Chart, "the amount from line 14 of that Form 8606 as adjusted to include the amount from line 6 of the Line 15c Worksheet, if any" (2025; sha256 735fb7ae)

## (gate) — `person.ira_basis_gate`

- **Authored helper label:** A person who files Form 8606 and whose traditional IRA basis changed other than by nondeductible contributions
- **Encoded (Bool):** helper "This person files Form 8606 for nondeductible contributions to a traditional IRA for 2025" = true and helper "Your traditional IRA basis changed other than by nondeductible contributions" = true
- Expr: `{"all":[{"eq":["person.ira_files_8606",{"const":true}],"op":"test"},{"eq":["person.ira_basis_adjusted",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i8606] p. 9, Line 2, "increase or decrease the amount from the chart" (2025; sha256 735fb7ae)

## (helper) — `person.ira_8606_line2`

- **Authored helper label:** Form 8606 line 2 for this person (asked only when the person files Form 8606)
- **Encoded (NonNegDollars):** Choose — [helper "This person files Form 8606 for nondeductible contributions to a traditional IRA for 2025" = true → helper "Your total basis in traditional IRAs before 2025 (Form 8606 line 2)"] [helper "This person files Form 8606 for nondeductible contributions to a traditional IRA for 2025" = false → line zero]
- **Refusal:** when person.ira_basis_gate is true, cannot complete Form 8606, line 2 (basis adjustments). Adjusting the Form 8606 line 2 basis for a Line 15c Worksheet amount, a return of excess contributions, a transfer incident to divorce or a rollover of a nontaxable part of a qualified plan is outside this tool. Cite: [i8606] p. 9, Line 2, "you may need to enter an amount that is more than -0- (even if this is the first year you are required to file Form 8606) or increase or decrease the amount from the chart" (2025; sha256 735fb7ae)
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_files_8606",{"const":true}],"op":"test"},"then":"person.ira_basis"},{"guard":{"eq":["person.ira_files_8606",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f8606] Form 8606 (2025), line 2, "Enter your total basis in traditional IRAs" (2025; sha256 748a2bf2)

## (helper) — `person.ira_dist`

- **Authored helper label:** In 2025, did you take a distribution from a traditional IRA, or make a Roth IRA conversion?
- **Encoded (Bool):** Input — In 2025, did you take a distribution from a traditional IRA (including a SEP or SIMPLE IRA), or make a Roth IRA conversion? Do not count rollovers (but count a repayment, treated as a rollover, of a 2025 qualified disaster, birth or adoption, emergency personal expense, domestic abuse or terminal illness distribution), qualified charitable distributions, a one-time distribution to fund an HSA, recharacterizations, or returns of contributions made by the due date of the return.
- Expr: `{"op":"input","source":"In 2025, did you take a distribution from a traditional IRA (including a SEP or SIMPLE IRA), or make a Roth IRA conversion? Do not count rollovers (but count a repayment, treated as a rollover, of a 2025 qualified disaster, birth or adoption, emergency personal expense, domestic abuse or terminal illness distribution), qualified charitable distributions, a one-time distribution to fund an HSA, recharacterizations, or returns of contributions made by the due date of the return."}`
- Cite: [f8606] Form 8606 (2025), Part I, "In 2025, did you take a distribution from a traditional IRA, or make a Roth IRA conversion?" and "For this purpose, “distributions” does not include rollovers (but does include certain 2025 retirement plan distribution repayments treated as rollovers (see instructions))"; i8606 p. 4, Special Terms, Certain 2025 retirement plan distribution repayments treated as rollovers (2025; sha256 748a2bf2)

## (helper) — `person.ira_dist_if_files`

- **Authored helper label:** This person files Form 8606 for nondeductible contributions for 2025 and took a 2025 traditional IRA distribution or Roth conversion
- **Encoded (Bool):** Choose — [helper "This person files Form 8606 for nondeductible contributions to a traditional IRA for 2025" = true → helper "In 2025, did you take a distribution from a traditional IRA, or make a Roth IRA conversion?"] [helper "This person files Form 8606 for nondeductible contributions to a traditional IRA for 2025" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_files_8606",{"const":true}],"op":"test"},"then":"person.ira_dist"},{"guard":{"eq":["person.ira_files_8606",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [f8606] Form 8606 (2025), Part I, "In 2025, did you take a distribution from a traditional IRA, or make a Roth IRA conversion?" and "Go to line 4" (2025; sha256 748a2bf2)

## (gate) — `person.ira_dist_gate`

- **Authored helper label:** Nondeductible contributions for 2025 with a 2025 traditional IRA distribution or Roth conversion
- **Encoded (Bool):** Choose — [helper "This person made traditional IRA contributions for 2025" = true → helper "This person files Form 8606 for nondeductible contributions for 2025 and took a 2025 traditional IRA distribution or Roth conversion"] [helper "This person made traditional IRA contributions for 2025" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_has",{"const":true}],"op":"test"},"then":"person.ira_dist_if_files"},{"guard":{"eq":["person.ira_has",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [f8606] Form 8606 (2025), Part I, "In 2025, did you take a distribution from a traditional IRA, or make a Roth IRA conversion?" and "Go to line 4" (2025; sha256 748a2bf2)

## (helper) — `person.ira_8606_line14`

- **Authored helper label:** Form 8606 line 14 for this person (total basis in traditional IRAs for 2025 and earlier years)
- **Encoded (NonNegDollars):** Add f8606.line14 over every confirmed f8606 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8606","field":"f8606.line14","op":"sum_over"}`
- Cite: [f8606] Form 8606 (2025), line 14 (2025; sha256 748a2bf2)

## (helper) — `person.ira_ssb_lim`

- **Authored helper label:** Social Security Benefits Worksheet copy of the IRA deduction: the smaller of the applicable amount and line 10
- **Encoded (NonNegDollars):** Enter the smaller of helper "The applicable amount for this person ($7,000 if under age 50 at the end of 2025; $8,000 if age 50 or older)" or ira line 10.
- Interpretation: amb.2025.ira_ssb_copy
- Expr: `{"of":["person.ira_limit","ira.line10"],"op":"smaller_of"}`
- Cite: [i1040gi] p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, "skip lines 2 through 6, enter the applicable amount below on line 7a"; p. 98, IRA Deduction Worksheet—Continued, line 12, "enter the smallest of line 7a, 10, or 11a" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_ssb_figured`

- **Authored helper label:** Social Security Benefits Worksheet copy of the IRA deduction when no one is covered by a retirement plan: the smallest of the applicable amount, line 10 and line 11
- **Encoded (NonNegDollars):** Enter the smaller of helper "Social Security Benefits Worksheet copy of the IRA deduction: the smaller of the applicable amount and line 10" or helper "Worksheet line 11 for this person's column (traditional IRA contributions for 2025)".
- **Refusal:** when ira.cov_gate is true, cannot complete Social security benefits with an IRA deduction and retirement plan coverage (Pub. 590-A Appendix B). With social security benefits, traditional IRA contributions for 2025 and you or your spouse covered by a retirement plan, the taxable benefits and the IRA deduction are figured with the worksheets in Pub. 590-A, which this tool does not prepare. Cite: [i1040gi] p. 31, Lines 6a and 6b, Exception (2025; printed date 2026-02-25; sha256 482e9c48)
- Interpretation: amb.2025.ira_ssb_copy
- Expr: `{"of":["person.ira_ssb_lim","person.ira_line11"],"op":"smaller_of"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 12, "enter the smallest of line 7a, 10, or 11a" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_ssb`

- **Authored helper label:** This person's IRA deduction as the Social Security Benefits Worksheet reads it (zero with no traditional IRA contributions)
- **Encoded (NonNegDollars):** Choose — [helper "This person made traditional IRA contributions for 2025" = true → helper "Social Security Benefits Worksheet copy of the IRA deduction when no one is covered by a retirement plan: the smallest of the applicable amount, line 10 and line 11"] [helper "This person made traditional IRA contributions for 2025" = false → line zero]
- Interpretation: amb.2025.ira_ssb_copy
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_has",{"const":true}],"op":"test"},"then":"person.ira_ssb_figured"},{"guard":{"eq":["person.ira_has",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 6 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_se_take`

- **Authored helper label:** This person's deductions on Schedule 1, lines 15 and 16
- **Encoded (NonNegDollars):** Add helper "Schedule SE line 13 (deduction for one-half of self-employment tax) for this person" and helper "Schedule 1 line 16 for this person".
- Expr: `{"of":["person.se_line13","person.s16"],"op":"sum"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 9, "minus any deductions on Schedule 1, lines 15 and 16" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_se_figured`

- **Authored helper label:** This person's earned income as a self-employed individual, less Schedule 1 lines 15 and 16 (zero or less, zero)
- **Encoded (NonNegDollars):** Subtract helper "This person's deductions on Schedule 1, lines 15 and 16" from helper "This person's Schedule C net profit or loss (all businesses)". If zero or less, enter -0-.
- Interpretation: amb.2025.ira_se_floor
- Expr: `{"from":"person.sc_total","op":"subtract_floor0","take":"person.ira_se_take"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 9, "Enter the earned income you (and your spouse if filing jointly) received as a self-employed individual or a partner" and "If zero or less, enter -0-" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.ira_se`

- **Authored helper label:** This person's part of worksheet line 9 (zero without a Schedule C)
- **Encoded (NonNegDollars):** Choose — [helper "This person has at least one Schedule C" = true → helper "This person's earned income as a self-employed individual, less Schedule 1 lines 15 and 16 (zero or less, zero)"] [helper "This person has at least one Schedule C" = false → line zero]
- Interpretation: amb.2025.ira_se_earned
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_sc",{"const":true}],"op":"test"},"then":"person.ira_se_figured"},{"guard":{"eq":["person.has_sc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i1040gi] p. 98, IRA Deduction Worksheet—Continued, line 9, "Generally, this is your (and your spouse’s if filing jointly) net earnings from self-employment if your personal services were a material income-producing factor" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `person.edu`

- **Authored helper label:** Qualified education expenses paid in 2025 for this person
- **Encoded (Bool):** Input — Did anyone pay qualified education expenses in 2025 for this person as a student at an eligible educational institution (a college, university, vocational school, or other postsecondary school eligible for federal student aid), counting books, supplies and equipment needed for a course of study wherever they were bought?
- Expr: `{"op":"input","source":"Did anyone pay qualified education expenses in 2025 for this person as a student at an eligible educational institution (a college, university, vocational school, or other postsecondary school eligible for federal student aid), counting books, supplies and equipment needed for a course of study wherever they were bought?"}`
- Cite: [i8863] p. 2, Who Can Claim an Education Credit, "You may be able to claim an education credit if you, your spouse, or a dependent you claim on your tax return was a student enrolled at or attending an eligible educational institution." (2025; sha256 195cfd5e)

## (gate) — `person.edu_1098t`

- **Authored helper label:** The student received a 2025 Form 1098-T from the institution, or an exception applies
- **Encoded (Bool):** Input — Did the student receive a 2025 Form 1098-T from the educational institution? Answer yes also, if you can show the enrollment and the payments, when the institution was not required to furnish one (for example a qualified nonresident alien, expenses paid entirely with scholarships or under a formal billing arrangement, or only courses for which no academic credit is awarded), or when the institution did not furnish it and, after February 2, 2026, but before you file, you or the student requested it and you fully cooperated with the institution's efforts to gather the information needed to furnish it.
- Interpretation: amb.2025.edu_1098t_date
- Expr: `{"op":"input","source":"Did the student receive a 2025 Form 1098-T from the educational institution? Answer yes also, if you can show the enrollment and the payments, when the institution was not required to furnish one (for example a qualified nonresident alien, expenses paid entirely with scholarships or under a formal billing arrangement, or only courses for which no academic credit is awarded), or when the institution did not furnish it and, after February 2, 2026, but before you file, you or the student requested it and you fully cooperated with the institution's efforts to gather the information needed to furnish it."}`
- Cite: [i8863] p. 1, Form 1098-T requirement, "To be eligible to claim the American opportunity credit or the lifetime learning credit, the law requires a taxpayer (or a dependent) to have received Form 1098-T, Tuition Statement, from an eligible educational institution, whether domestic or foreign."; p. 1, "You must fully cooperate with the educational institution’s efforts to gather the information needed to furnish the Form 1098-T." (2025; sha256 195cfd5e)

## (helper) — `person.edu_student`

- **Authored helper label:** An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception)
- **Encoded (Bool):** Choose — [f8863 helper "Qualified education expenses paid in 2025 for you, your spouse or a dependent you claim" = true → helper "With education expenses paid: this person was a student with qualified expenses, has a TIN by the due date and a Form 1098-T (or an exception)"] [f8863 helper "Qualified education expenses paid in 2025 for you, your spouse or a dependent you claim" = false → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["f8863.paid",{"const":true}],"op":"test"},"then":"person.edu_student_edu"},{"guard":{"eq":["f8863.paid",{"const":false}],"op":"test"},"then":"person.edu_no"}],"op":"choose"}`
- Cite: [i8863] p. 3, Who cannot claim a credit, "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)." (2025; sha256 195cfd5e)

## (helper) — `person.edu_student_edu`

- **Authored helper label:** With education expenses paid: this person was a student with qualified expenses, has a TIN by the due date and a Form 1098-T (or an exception)
- **Encoded (Bool):** Choose — [helper "Qualified education expenses paid in 2025 for this person" = true → helper "A student with qualified expenses: an SSN or ITIN (or an ITIN applied for by the due date), and a Form 1098-T (or an exception)"] [helper "Qualified education expenses paid in 2025 for this person" = false → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu",{"const":true}],"op":"test"},"then":"person.edu_student_tin"},{"guard":{"eq":["person.edu",{"const":false}],"op":"test"},"then":"person.edu_no"}],"op":"choose"}`
- Cite: [i8863] p. 2, Who Can Claim an Education Credit, "You may be able to claim an education credit if you, your spouse, or a dependent you claim on your tax return was a student enrolled at or attending an eligible educational institution." (2025; sha256 195cfd5e)

## (helper) — `person.edu_student_tin`

- **Authored helper label:** A student with qualified expenses: an SSN or ITIN (or an ITIN applied for by the due date), and a Form 1098-T (or an exception)
- **Encoded (Bool):** Choose — [helper "Do you have an SSN or ITIN issued on or before the due date of your return?" = true → helper "The student received a 2025 Form 1098-T from the institution, or an exception applies"] [helper "Do you have an SSN or ITIN issued on or before the due date of your return?" = false → helper "A student without an SSN or ITIN: an ITIN applied for by the due date, and a Form 1098-T (or an exception)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.tin",{"const":true}],"op":"test"},"then":"person.edu_1098t"},{"guard":{"eq":["person.tin",{"const":false}],"op":"test"},"then":"person.edu_student_itin"}],"op":"choose"}`
- Cite: [i8863] p. 3, Who cannot claim a credit, "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)." (2025; sha256 195cfd5e)

## (helper) — `person.edu_student_itin`

- **Authored helper label:** A student without an SSN or ITIN: an ITIN applied for by the due date, and a Form 1098-T (or an exception)
- **Encoded (Bool):** Choose — [helper "If not, have you applied, or are you applying, for an ITIN, or for the renewal of your expired ITIN, on or before the due date of your return?" = true → helper "The student received a 2025 Form 1098-T from the institution, or an exception applies"] [helper "If not, have you applied, or are you applying, for an ITIN, or for the renewal of your expired ITIN, on or before the due date of your return?" = false → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.itin_applied",{"const":true}],"op":"test"},"then":"person.edu_1098t"},{"guard":{"eq":["person.itin_applied",{"const":false}],"op":"test"},"then":"person.edu_no"}],"op":"choose"}`
- Cite: [i8863] p. 3, Who cannot claim a credit, "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)." (2025; sha256 195cfd5e)

## (helper) — `person.edu_inst`

- **Authored helper label:** Qualified education expenses required to be paid to the institution
- **Encoded (NonNegDollars):** Input — Qualified education expenses paid in 2025 for this student, by anyone, that had to be paid to the institution, for academic periods beginning in 2025 or in the first 3 months of 2026:

  - tuition
  - fees required for enrollment or attendance, including nonacademic fees (such as student activity or athletic fees) that must be paid to the institution as a condition of enrollment or attendance
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
- Expr: `{"op":"input","source":"Qualified education expenses paid in 2025 for this student, by anyone, that had to be paid to the institution, for academic periods beginning in 2025 or in the first 3 months of 2026:\n\n- tuition\n- fees required for enrollment or attendance, including nonacademic fees (such as student activity or athletic fees) that must be paid to the institution as a condition of enrollment or attendance\n- books, supplies and equipment required to be paid to the institution as a condition of enrollment or attendance\n\nUse the amounts actually paid, which may differ from Form 1098-T box 1.\n\nDo not include:\n- amounts paid in 2024 or 2026\n- room and board\n- insurance\n- medical expenses (including student health fees)\n- transportation\n- expenses deducted elsewhere (for example on Schedule C)\n- expenses used for a tax-free distribution from a Coverdell ESA or qualified tuition program (529 plan)\n- a course or other education involving sports, games or hobbies, or any noncredit course, unless it is part of the student's degree program or, where this student can't get the American opportunity credit, it helps the student acquire or improve job skills\n\nZero if none"}`
- Cite: [i8863] p. 4, Qualified Education Expenses, "Generally, qualified education expenses are amounts paid in 2025 for tuition and fees required for the student’s enrollment or attendance at an eligible educational institution."; p. 4, "Any course or other education involving sports, games, or hobbies, or any noncredit course, unless such course or other education is part of the student’s degree program or (for the lifetime learning credit only) helps the student acquire or improve job skills." (2025; sha256 195cfd5e)

## (helper) — `person.edu_mat`

- **Authored helper label:** Other course materials (American opportunity credit only)
- **Encoded (NonNegDollars):** Input — Other course materials paid for in 2025 for this student: books, supplies and equipment needed for a course of study that did not have to be paid to the institution (they count for the American opportunity credit only), paid in 2025; do not include amounts paid in 2024 or 2026, expenses deducted elsewhere (for example on Schedule C), expenses used for a tax-free distribution from a Coverdell ESA or qualified tuition program (529 plan), or materials for a course involving sports, games or hobbies or a noncredit course that is not part of the student's degree program; zero if none
- Expr: `{"op":"input","source":"Other course materials paid for in 2025 for this student: books, supplies and equipment needed for a course of study that did not have to be paid to the institution (they count for the American opportunity credit only), paid in 2025; do not include amounts paid in 2024 or 2026, expenses deducted elsewhere (for example on Schedule C), expenses used for a tax-free distribution from a Coverdell ESA or qualified tuition program (529 plan), or materials for a course involving sports, games or hobbies or a noncredit course that is not part of the student's degree program; zero if none"}`
- Cite: [i8863] p. 4, Qualified Education Expenses, "American opportunity credit: Qualified education expenses include amounts paid for tuition, fees, and course materials, which include books, supplies, and equipment needed for a course of study, whether or not the materials are purchased from the educational institution as a condition of enrollment or attendance." (2025; sha256 195cfd5e)

## (helper) — `person.edu_a_this_year`

- **Authored helper label:** Adjusted Qualified Education Expenses Worksheet, line 2a
- **Encoded (NonNegDollars):** Input — Tax-free educational assistance received in 2025 that is allocable to the academic periods of the expenses entered for this student (periods beginning in 2025 or in the first 3 months of 2026): the tax-free part of scholarships and fellowship grants (including Pell grants; Form 1098-T box 5 may help), tax-free employer-provided educational assistance, veterans' educational assistance, and other tax-free educational assistance. Do not include wages, loans, gifts, inheritances, withdrawals from personal savings, emergency financial aid grants, or a scholarship the student includes in income (for you or your spouse, the amount on Schedule 1 line 8r); a scholarship or fellowship grant can be included in income only if its terms allow it to be used for expenses other than qualified education expenses (such as room and board), and never one provided by an Indian tribal government and excluded under the Tribal General Welfare Exclusion Act of 2014; zero if none
- Expr: `{"op":"input","source":"Tax-free educational assistance received in 2025 that is allocable to the academic periods of the expenses entered for this student (periods beginning in 2025 or in the first 3 months of 2026): the tax-free part of scholarships and fellowship grants (including Pell grants; Form 1098-T box 5 may help), tax-free employer-provided educational assistance, veterans' educational assistance, and other tax-free educational assistance. Do not include wages, loans, gifts, inheritances, withdrawals from personal savings, emergency financial aid grants, or a scholarship the student includes in income (for you or your spouse, the amount on Schedule 1 line 8r); a scholarship or fellowship grant can be included in income only if its terms allow it to be used for expenses other than qualified education expenses (such as room and board), and never one provided by an Indian tribal government and excluded under the Tribal General Welfare Exclusion Act of 2014; zero if none"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "a. Tax-free educational assistance received in 2025 allocable to the academic period"; p. 5, Coordination with Pell grants and other scholarships or fellowship grants, "A student cannot choose to include in income a scholarship or fellowship grant provided by an Indian tribal government that is excluded from income under the Tribal General Welfare Exclusion Act of 2014" and "the scholarship or fellowship grant must be one that may (by its terms) be used for expenses other than qualified education expenses (such as room and board)" (2025; sha256 195cfd5e)

## (helper) — `person.edu_a_next_year`

- **Authored helper label:** Adjusted Qualified Education Expenses Worksheet, line 2b
- **Encoded (NonNegDollars):** Input — Tax-free educational assistance received in 2026, before you file this return, that is allocable to an academic period of these 2025 expenses; zero if none
- Expr: `{"op":"input","source":"Tax-free educational assistance received in 2026, before you file this return, that is allocable to an academic period of these 2025 expenses; zero if none"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "b. Tax-free educational assistance received in 2026 (and before you file your 2025 tax return) allocable to the academic period" (2025; sha256 195cfd5e)

## (helper) — `person.edu_refunds`

- **Authored helper label:** Adjusted Qualified Education Expenses Worksheet, line 2c
- **Encoded (NonNegDollars):** Input — Refunds of these 2025 qualified education expenses received in 2025, or in 2026 before you file this return; zero if none
- Expr: `{"op":"input","source":"Refunds of these 2025 qualified education expenses received in 2025, or in 2026 before you file this return; zero if none"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "c. Refunds of qualified education expenses paid in 2025 if the refund is received in 2025 or in 2026 before you file your 2025 tax return" (2025; sha256 195cfd5e)

## (helper) — `person.edu_adj_sum`

- **Authored helper label:** Add lines 2a, 2b and 2c
- **Encoded (NonNegDollars):** Add helper "Adjusted Qualified Education Expenses Worksheet, line 2a", helper "Adjusted Qualified Education Expenses Worksheet, line 2b", and helper "Adjusted Qualified Education Expenses Worksheet, line 2c".
- Expr: `{"of":["person.edu_a_this_year","person.edu_a_next_year","person.edu_refunds"],"op":"sum"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "3. Total adjustments (add lines 2a, 2b, and 2c)" (2025; sha256 195cfd5e)

## (helper) — `person.edu_adj`

- **Authored helper label:** Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c
- **Encoded (NonNegDollars):** Choose — [helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception)" = true → helper "Add lines 2a, 2b and 2c"] [helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception)" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_student",{"const":true}],"op":"test"},"then":"person.edu_adj_sum"},{"guard":{"eq":["person.edu_student",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "3. Total adjustments (add lines 2a, 2b, and 2c)" (2025; sha256 195cfd5e)

## (gate) — `person.edu_over`

- **Authored helper label:** An academic period whose tax-free assistance and refunds exceed its expenses paid to the institution
- **Encoded (Bool):** Input — Was there an academic period for which the tax-free educational assistance and refunds allocable to it (received in 2025, or in 2026 before you file) were more than that period's qualified education expenses paid in 2025 (tuition and required fees, and course materials, which for a student who can get the American opportunity credit are those needed for a course of study wherever bought, and otherwise those required to be paid to the institution)?
- Expr: `{"op":"input","source":"Was there an academic period for which the tax-free educational assistance and refunds allocable to it (received in 2025, or in 2026 before you file) were more than that period's qualified education expenses paid in 2025 (tuition and required fees, and course materials, which for a student who can get the American opportunity credit are those needed for a course of study wherever bought, and otherwise those required to be paid to the institution)?"}`
- Cite: [i8863] p. 4, Tax-free educational assistance, "For tax-free educational assistance received in 2025, reduce the qualified education expenses for each academic period by the amount of tax-free educational assistance allocable to that academic period." (2025; sha256 195cfd5e)

## (helper) — `person.edu_has_adj`

- **Authored helper label:** Adjusted qualified education expenses (worksheet line 3) above zero
- **Encoded (Bool):** helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c" > $0
- Expr: `{"gt":["person.edu_adj",{"const":0}],"op":"test"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)

## (helper) — `person.edu_over_if_adj`

- **Authored helper label:** Adjustments that exceed one academic period's expenses, where adjusted qualified education expenses are above zero
- **Encoded (Bool):** Choose — [helper "Adjusted qualified education expenses (worksheet line 3) above zero" = true → helper "An academic period whose tax-free assistance and refunds exceed its expenses paid to the institution"] [helper "Adjusted qualified education expenses (worksheet line 3) above zero" = false → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_has_adj",{"const":true}],"op":"test"},"then":"person.edu_over"},{"guard":{"eq":["person.edu_has_adj",{"const":false}],"op":"test"},"then":"person.edu_no"}],"op":"choose"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)

## (gate) — `person.edu_over_refused`

- **Authored helper label:** Adjustments that exceed one academic period's expenses
- **Encoded (Bool):** Choose — [helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception)" = true → helper "Adjustments that exceed one academic period's expenses, where adjusted qualified education expenses are above zero"] [helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception)" = false → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_student",{"const":true}],"op":"test"},"then":"person.edu_over_if_adj"},{"guard":{"eq":["person.edu_student",{"const":false}],"op":"test"},"then":"person.edu_no"}],"op":"choose"}`
- Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)

## 23 — `person.edu_line23`

- **Authored helper label:** Has the American opportunity credit been claimed for this student for any 4 prior tax years?
- **Encoded (Bool):** Input — Has the American opportunity credit been claimed (by you or anyone else) for this student for any 4 tax years before 2025?
- **Shown on the values sheet only when:** An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception) (`person.edu_student`)
- Expr: `{"op":"input","source":"Has the American opportunity credit been claimed (by you or anyone else) for this student for any 4 tax years before 2025?"}`
- Cite: [f8863] p. 2, Part III, line 23, "Has the American opportunity credit been claimed for this student for any 4 prior tax years?"; i8863 p. 8, Line 23 (2025; sha256 a251a1cf)

## (helper) — `person.edu_show24`

- **Authored helper label:** Line 24 is reached (line 23 did not stop)
- **Encoded (Bool):** helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception)" = true and line 23 = false
- Expr: `{"all":[{"eq":["person.edu_student",{"const":true}],"op":"test"},{"eq":["person.edu_line23",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [f8863] p. 2, Part III, line 23, "Yes—Stop! Go to line 31 for this student." (2025; sha256 a251a1cf)

## 24 — `person.edu_line24`

- **Authored helper label:** Was the student enrolled at least half-time for at least one academic period that began or is treated as having begun in 2025 at an eligible educational institution in a program leading toward a postsecondary degree, certificate, or other recognized postsecondary educational credential?
- **Encoded (Bool):** Input — Was the student enrolled at least half-time (Form 1098-T box 8) for at least one academic period that began in 2025, or in the first 3 months of 2026 if paid for in 2025, at an eligible educational institution, in a program leading toward a postsecondary degree, certificate or other recognized postsecondary educational credential?
- **Shown on the values sheet only when:** Line 24 is reached (line 23 did not stop) (`person.edu_show24`)
- Expr: `{"op":"input","source":"Was the student enrolled at least half-time (Form 1098-T box 8) for at least one academic period that began in 2025, or in the first 3 months of 2026 if paid for in 2025, at an eligible educational institution, in a program leading toward a postsecondary degree, certificate or other recognized postsecondary educational credential?"}`
- Cite: [f8863] p. 2, Part III, line 24, "Was the student enrolled at least half-time for at least one academic period that began or is treated as having begun in 2025 at an eligible educational institution in a program leading toward a postsecondary degree, certificate, or other recognized postsecondary educational credential?"; i8863 p. 8, Line 24 (2025; sha256 a251a1cf)

## (helper) — `person.edu_show25`

- **Authored helper label:** Line 25 is reached (line 24 did not stop)
- **Encoded (Bool):** helper "Line 24 is reached (line 23 did not stop)" = true and line 24 = true
- Expr: `{"all":[{"eq":["person.edu_show24",{"const":true}],"op":"test"},{"eq":["person.edu_line24",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [f8863] p. 2, Part III, line 24, "No—Stop! Go to line 31 for this student." (2025; sha256 a251a1cf)

## 25 — `person.edu_line25`

- **Authored helper label:** Did the student complete the first 4 years of postsecondary education before 2025?
- **Encoded (Bool):** Input — Did the student complete the first 4 years of postsecondary education before 2025, as determined by the institution (4 years of academic credit, not counting credit awarded solely for proficiency examinations)?
- **Shown on the values sheet only when:** Line 25 is reached (line 24 did not stop) (`person.edu_show25`)
- Expr: `{"op":"input","source":"Did the student complete the first 4 years of postsecondary education before 2025, as determined by the institution (4 years of academic credit, not counting credit awarded solely for proficiency examinations)?"}`
- Cite: [f8863] p. 2, Part III, line 25, "Did the student complete the first 4 years of postsecondary education before 2025?"; i8863 p. 8, Line 25 (2025; sha256 a251a1cf)

## (helper) — `person.edu_show26`

- **Authored helper label:** Line 26 is reached (line 25 did not stop)
- **Encoded (Bool):** helper "Line 25 is reached (line 24 did not stop)" = true and line 25 = false
- Expr: `{"all":[{"eq":["person.edu_show25",{"const":true}],"op":"test"},{"eq":["person.edu_line25",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [f8863] p. 2, Part III, line 25, "Yes—Stop! Go to line 31 for this student." (2025; sha256 a251a1cf)

## 26 — `person.edu_line26`

- **Authored helper label:** Was the student convicted, before the end of 2025, of a felony for possession or distribution of a controlled substance?
- **Encoded (Bool):** Input — Was the student convicted, before the end of 2025, of a federal or state felony for possession or distribution of a controlled substance?
- **Shown on the values sheet only when:** Line 26 is reached (line 25 did not stop) (`person.edu_show26`)
- Expr: `{"op":"input","source":"Was the student convicted, before the end of 2025, of a federal or state felony for possession or distribution of a controlled substance?"}`
- Cite: [f8863] p. 2, Part III, line 26, "Was the student convicted, before the end of 2025, of a felony for possession or distribution of a controlled substance?"; i8863 p. 8, Line 26 (2025; sha256 a251a1cf)

## (gate) — `person.edu_ein`

- **Authored helper label:** The institution's employer identification number (EIN) is available
- **Encoded (Bool):** Input — Do you have the educational institution's employer identification number (EIN), from Form 1098-T or from the institution?
- Expr: `{"op":"input","source":"Do you have the educational institution's employer identification number (EIN), from Form 1098-T or from the institution?"}`
- Cite: [i8863] p. 4, Student qualifications, "7. You must provide the educational institution’s employer identification number (EIN) on your Form 8863." (2025; sha256 195cfd5e)

## (helper) — `person.edu_no`

- **Authored helper label:** Year parameter edu.no (false)
- **Encoded (Bool):** Enter false (edu.no).
- Expr: `{"op":"param","ref":"edu.no"}`
- Cite: [f8863] p. 2, Part III, line 23, "Yes—Stop! Go to line 31 for this student." (2025; sha256 a251a1cf)

## (helper) — `person.edu_aoc`

- **Authored helper label:** An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available
- **Encoded (Bool):** Choose — [helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception)" = true → helper "For an eligible student, line 23 is No (the American opportunity credit was not claimed for 4 prior tax years), and lines 24 to 26, the TINs and the EIN allow the credit"] [helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception)" = false → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_student",{"const":true}],"op":"test"},"then":"person.edu_aoc23"},{"guard":{"eq":["person.edu_student",{"const":false}],"op":"test"},"then":"person.edu_no"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 26, "No—Complete lines 27 through 30 for this student."; i8863 p. 3, Student qualifications, "5. Filers and students must have been issued a TIN by the due date of their 2025 return (including extensions)." (2025; sha256 a251a1cf)

## (helper) — `person.edu_aoc23`

- **Authored helper label:** For an eligible student, line 23 is No (the American opportunity credit was not claimed for 4 prior tax years), and lines 24 to 26, the TINs and the EIN allow the credit
- **Encoded (Bool):** Choose — [line 23 = false → helper "Line 24 is Yes (enrolled at least half-time), and lines 25 and 26, the TINs and the EIN allow the credit"] [line 23 = true → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_line23",{"const":false}],"op":"test"},"then":"person.edu_aoc24"},{"guard":{"eq":["person.edu_line23",{"const":true}],"op":"test"},"then":"person.edu_no"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 23, "Yes—Stop! Go to line 31 for this student." (2025; sha256 a251a1cf)

## (helper) — `person.edu_aoc24`

- **Authored helper label:** Line 24 is Yes (enrolled at least half-time), and lines 25 and 26, the TINs and the EIN allow the credit
- **Encoded (Bool):** Choose — [line 24 = true → helper "Line 25 is No (the first 4 years of postsecondary education were not completed before 2025), and line 26, the TINs and the EIN allow the credit"] [line 24 = false → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_line24",{"const":true}],"op":"test"},"then":"person.edu_aoc25"},{"guard":{"eq":["person.edu_line24",{"const":false}],"op":"test"},"then":"person.edu_no"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 24, "No—Stop! Go to line 31 for this student." (2025; sha256 a251a1cf)

## (helper) — `person.edu_aoc25`

- **Authored helper label:** Line 25 is No (the first 4 years of postsecondary education were not completed before 2025), and line 26, the TINs and the EIN allow the credit
- **Encoded (Bool):** Choose — [line 25 = false → helper "Line 26 is No (no felony drug conviction), and the TINs and the EIN allow the credit"] [line 25 = true → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_line25",{"const":false}],"op":"test"},"then":"person.edu_aoc26"},{"guard":{"eq":["person.edu_line25",{"const":true}],"op":"test"},"then":"person.edu_no"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 25, "Yes—Stop! Go to line 31 for this student." (2025; sha256 a251a1cf)

## (helper) — `person.edu_aoc26`

- **Authored helper label:** Line 26 is No (no felony drug conviction), and the TINs and the EIN allow the credit
- **Encoded (Bool):** Choose — [line 26 = false → helper "You, and your spouse if filing jointly, have a TIN, and the institution's EIN is available"] [line 26 = true → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_line26",{"const":false}],"op":"test"},"then":"person.edu_aoc_tin"},{"guard":{"eq":["person.edu_line26",{"const":true}],"op":"test"},"then":"person.edu_no"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 26, "No—Complete lines 27 through 30 for this student." (2025; sha256 a251a1cf)

## (helper) — `person.edu_aoc_tin`

- **Authored helper label:** You, and your spouse if filing jointly, have a TIN, and the institution's EIN is available
- **Encoded (Bool):** Choose — [household helper "You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN" = true → helper "The institution's employer identification number (EIN) is available"] [household helper "You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN" = false → helper "Year parameter edu.no (false)"]
- Interpretation: amb.2025.edu_filer_tin
- Expr: `{"alternatives":[{"guard":{"eq":["household.all_tin",{"const":true}],"op":"test"},"then":"person.edu_ein"},{"guard":{"eq":["household.all_tin",{"const":false}],"op":"test"},"then":"person.edu_no"}],"op":"choose"}`
- Cite: [i8863] p. 3, Student qualifications, "5. Filers and students must have been issued a TIN by the due date of their 2025 return (including extensions)." (2025; sha256 195cfd5e)

## (helper) — `person.edu_llc`

- **Authored helper label:** A lifetime learning credit student: an eligible student who is not an American opportunity credit student
- **Encoded (Bool):** helper "An eligible student of this return: expenses paid, a TIN by the due date and a Form 1098-T (or an exception)" = true and helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false
- Expr: `{"all":[{"eq":["person.edu_student",{"const":true}],"op":"test"},{"eq":["person.edu_aoc",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i8863] p. 4, Tip, "If the requirements above aren’t met for any student, you cannot claim the American opportunity credit for that student. You may be able to claim the lifetime learning credit for part or all of that student’s qualified education expenses instead if certain requirements are met." (2025; sha256 195cfd5e)

## (gate) — `person.edu_llc_tin_refused`

- **Authored helper label:** A lifetime learning credit student whose ITIN was only applied for by the due date of the return
- **Encoded (Bool):** helper "A lifetime learning credit student: an eligible student who is not an American opportunity credit student" = true and helper "Do you have an SSN or ITIN issued on or before the due date of your return?" = false
- Expr: `{"all":[{"eq":["person.edu_llc",{"const":true}],"op":"test"},{"eq":["person.tin",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i8863] p. 3, Who cannot claim a credit, "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)." (2025; sha256 195cfd5e)

## 27 — `person.edu_line27`

- **Authored helper label:** Adjusted qualified education expenses. Don't enter more than $4,000
- **Encoded (NonNegDollars):** Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line27" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → line zero]
- **Refusal:** when person.edu_over_refused is true, cannot complete Adjusted Qualified Education Expenses Worksheet for more than one academic period. The worksheet is completed for each academic period, and an academic period whose tax-free educational assistance and refunds exceed its own expenses cannot be netted against another period's expenses. Figure the worksheet period by period. Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)
- **Shown on the values sheet only when:** An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available (`person.edu_aoc`)
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_aoc",{"const":true}],"op":"test"},"then":{"bind":{"adj":"person.edu_adj","inst":"person.edu_inst","mat":"person.edu_mat"},"def":"aqee","line":"line27"}},{"guard":{"eq":["person.edu_aoc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 27, "Adjusted qualified education expenses (see instructions). Don’t enter more than $4,000"; i8863 p. 9, Line 27 (2025; sha256 a251a1cf)

## 28 — `person.edu_line28`

- **Authored helper label:** Subtract $2,000 from line 27. If zero or less, enter -0-
- **Encoded (NonNegDollars):** Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line28" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → line zero]
- **Refusal:** when person.edu_over_refused is true, cannot complete Adjusted Qualified Education Expenses Worksheet for more than one academic period. The worksheet is completed for each academic period, and an academic period whose tax-free educational assistance and refunds exceed its own expenses cannot be netted against another period's expenses. Figure the worksheet period by period. Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)
- **Shown on the values sheet only when:** An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available (`person.edu_aoc`)
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_aoc",{"const":true}],"op":"test"},"then":{"bind":{"adj":"person.edu_adj","inst":"person.edu_inst","mat":"person.edu_mat"},"def":"aqee","line":"line28"}},{"guard":{"eq":["person.edu_aoc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 28, "Subtract $2,000 from line 27. If zero or less, enter -0-" (2025; sha256 a251a1cf)

## 29 — `person.edu_line29`

- **Authored helper label:** Multiply line 28 by 25% (0.25)
- **Encoded (NonNegDollars):** Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line29" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → line zero]
- **Refusal:** when person.edu_over_refused is true, cannot complete Adjusted Qualified Education Expenses Worksheet for more than one academic period. The worksheet is completed for each academic period, and an academic period whose tax-free educational assistance and refunds exceed its own expenses cannot be netted against another period's expenses. Figure the worksheet period by period. Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)
- **Shown on the values sheet only when:** An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available (`person.edu_aoc`)
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_aoc",{"const":true}],"op":"test"},"then":{"bind":{"adj":"person.edu_adj","inst":"person.edu_inst","mat":"person.edu_mat"},"def":"aqee","line":"line29"}},{"guard":{"eq":["person.edu_aoc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 29, "Multiply line 28 by 25% (0.25)" (2025; sha256 a251a1cf)

## 30 — `person.edu_line30`

- **Authored helper label:** American opportunity credit for this student. If line 28 is zero, enter the amount from line 27. Otherwise, add $2,000 to the amount on line 29
- **Encoded (NonNegDollars):** Choose — [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = true → "line30" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = helper "Other course materials (American opportunity credit only)"] [helper "An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available" = false → line zero]
- **Refusal:** when person.edu_over_refused is true, cannot complete Adjusted Qualified Education Expenses Worksheet for more than one academic period. The worksheet is completed for each academic period, and an academic period whose tax-free educational assistance and refunds exceed its own expenses cannot be netted against another period's expenses. Figure the worksheet period by period. Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)
- **Shown on the values sheet only when:** An American opportunity credit student: lines 23 to 26 allow it, the filers have TINs, and the institution's EIN is available (`person.edu_aoc`)
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_aoc",{"const":true}],"op":"test"},"then":{"bind":{"adj":"person.edu_adj","inst":"person.edu_inst","mat":"person.edu_mat"},"def":"aqee","line":"line30"}},{"guard":{"eq":["person.edu_aoc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 30, "If line 28 is zero, enter the amount from line 27.", "Include the total of all amounts from all Parts III, line 30, on Part I, line 1" (2025; sha256 a251a1cf)

## 31 — `person.edu_line31`

- **Authored helper label:** Adjusted qualified education expenses for the lifetime learning credit
- **Encoded (NonNegDollars):** Choose — [helper "A lifetime learning credit student: an eligible student who is not an American opportunity credit student" = true → "ws4_llc" of Form 8863, Part III lines 27 to 31 with the Adjusted Qualified Education Expenses Worksheet, one per student with adj = helper "Adjusted Qualified Education Expenses Worksheet, line 3 for an eligible student: add lines 2a, 2b and 2c", inst = helper "Qualified education expenses required to be paid to the institution", and mat = line zero] [helper "A lifetime learning credit student: an eligible student who is not an American opportunity credit student" = false → line zero]
- **Refusal:** when person.edu_llc_tin_refused is true, cannot complete Lifetime learning credit for a student whose ITIN was only applied for. The lifetime learning credit requires the student to have been issued a TIN by the due date of the return (including extensions); an ITIN only applied for by then counts as issued for the American opportunity credit only. This tool does not prepare the return without the lifetime learning credit for this student. Cite: [i8863] p. 3, Who cannot claim a credit, "5. The student has not been issued a TIN by the due date of his or her 2025 return (including extensions)."; p970 p. 11, "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as is- sued on or before the due date of the return." (2025; sha256 195cfd5e)
- **Refusal:** when person.edu_over_refused is true, cannot complete Adjusted Qualified Education Expenses Worksheet for more than one academic period. The worksheet is completed for each academic period, and an academic period whose tax-free educational assistance and refunds exceed its own expenses cannot be netted against another period's expenses. Figure the worksheet period by period. Cite: [i8863] p. 9, Adjusted Qualified Education Expenses Worksheet, "Complete a separate worksheet for each student for each academic period beginning or treated as beginning (see below) in 2025 for which you paid (or are treated as having paid) qualified education expenses in 2025." (2025; sha256 195cfd5e)
- **Shown on the values sheet only when:** A lifetime learning credit student: an eligible student who is not an American opportunity credit student (`person.edu_llc`)
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_llc",{"const":true}],"op":"test"},"then":{"bind":{"adj":"person.edu_adj","inst":"person.edu_inst","mat":"person.zero"},"def":"aqee","line":"ws4_llc"}},{"guard":{"eq":["person.edu_llc",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [f8863] p. 2, Part III, line 31, "Adjusted qualified education expenses (see instructions). Include the total of all amounts from all Parts III, line 31, on Part II, line 10"; i8863 p. 9, Line 31 (2025; sha256 a251a1cf)

## (helper) — `person.edu_over18`

- **Authored helper label:** Born before January 2, 2007
- **Encoded (Bool):** (helper "The year you were born" < 2007 (age.cut_19) or helper "The year you were born" = 2007 (age.cut_19) and helper "Born on January 1 (asked only of a person born in 1961, 2001, 2002, 2007 or 2008; otherwise no)" = true)
- Interpretation: amb.2025.edu_age_rule
- Expr: `{"any":[{"lt":["person.birth_year",{"param":"age.cut_19"}],"op":"test"},{"all":[{"eq":["person.birth_year",{"param":"age.cut_19"}],"op":"test"},{"eq":["person.born_jan1_if_cut_year",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i8863] p. 7, Line 7, "b. Age 18 at the end of 2025 and your earned income (defined later) was less than one-half of your support (defined later), or" (2025; sha256 195cfd5e)

## (helper) — `person.edu_age24`

- **Authored helper label:** Born before January 2, 2002
- **Encoded (Bool):** (helper "The year you were born" < 2002 (age.cut_24) or helper "The year you were born" = 2002 (age.cut_24) and helper "Born on January 1 (asked only of a person born in 1961, 2001, 2002, 2007 or 2008; otherwise no)" = true)
- Interpretation: amb.2025.edu_age_rule
- Expr: `{"any":[{"lt":["person.birth_year",{"param":"age.cut_24"}],"op":"test"},{"all":[{"eq":["person.birth_year",{"param":"age.cut_24"}],"op":"test"},{"eq":["person.born_jan1_if_cut_year",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i8863] p. 7, Line 7, "1. Were you under age 24 at the end of 2025?" (2025; sha256 195cfd5e)

## (helper) — `person.edu_fulltime`

- **Authored helper label:** A full-time student for 2025 (any part of 5 calendar months at an eligible educational institution)
- **Encoded (Bool):** Input — Were you a full-time student for 2025: during any part of any 5 calendar months of 2025, were you enrolled as a full-time student at an eligible educational institution, or did you take a full-time, on-farm training course given by such an institution or by a state, county, or local government agency?
- Interpretation: amb.2025.edu_fulltime
- Expr: `{"op":"input","source":"Were you a full-time student for 2025: during any part of any 5 calendar months of 2025, were you enrolled as a full-time student at an eligible educational institution, or did you take a full-time, on-farm training course given by such an institution or by a state, county, or local government agency?"}`
- Cite: [i8863] p. 7, Full-time student, "you were a full-time student for 2025 if during any part of any 5 calendar months during the year you were enrolled as a full-time student at an eligible educational institution (defined earlier), or took a full-time, on-farm training course given by such an institution or by a state, county, or local government agency." (2025; sha256 195cfd5e)

## (helper) — `person.edu_half_support`

- **Authored helper label:** Your earned income was less than one-half of your support for 2025
- **Encoded (Bool):** Input — Was your earned income for 2025 less than one-half of your support? Earned income is wages, salaries, professional fees and other pay for personal services (including the part of a scholarship that pays for teaching, research or other required services), but not the part of pay from a corporation that is a distribution of its profits; from a business in which both your services and capital produce the income, a reasonable allowance for your services, not more than 30% of your share of its net profit (after the deduction for one-half of self-employment tax). Support includes food, shelter, clothing, medical and dental care, education and the like, provided by you, your parents and others, lodging or property counted at its fair market value; a scholarship is not support if you were a full-time student (during some part of 5 calendar months of 2025).
- Expr: `{"op":"input","source":"Was your earned income for 2025 less than one-half of your support? Earned income is wages, salaries, professional fees and other pay for personal services (including the part of a scholarship that pays for teaching, research or other required services), but not the part of pay from a corporation that is a distribution of its profits; from a business in which both your services and capital produce the income, a reasonable allowance for your services, not more than 30% of your share of its net profit (after the deduction for one-half of self-employment tax). Support includes food, shelter, clothing, medical and dental care, education and the like, provided by you, your parents and others, lodging or property counted at its fair market value; a scholarship is not support if you were a full-time student (during some part of 5 calendar months of 2025)."}`
- Cite: [i8863] p. 7, Earned income, "Earned income includes wages, salaries, professional fees, and other payments received for personal services actually performed.", "not more than 30% of your share of the net profits from that trade or business"; p. 7, Support, "If the item of support is in the form of property or lodging, measure the amount of such item of support by its fair market value"; p. 7, Full-time student (2025; sha256 195cfd5e)

## (helper) — `person.edu_parent`

- **Authored helper label:** At least one of your parents was alive at the end of 2025
- **Encoded (Bool):** Input — Was at least one of your parents alive at the end of 2025?
- Expr: `{"op":"input","source":"Was at least one of your parents alive at the end of 2025?"}`
- Cite: [i8863] p. 7, Line 7, "2. At least one of your parents was alive at the end of 2025." (2025; sha256 195cfd5e)

## (helper) — `person.edu_kid_age`

- **Authored helper label:** Line 7 conditions 1 and 2 for you (under 18 and a parent alive, or the tests for 18 to 23)
- **Encoded (Bool):** Choose — [helper "Born before January 2, 2008" = true → helper "Line 7 conditions 1b, 1c and 2 for you, born before January 2, 2008 (age 18 with earned income less than half of your support and a parent alive, or the tests for 19 to 23)"] [helper "Born before January 2, 2008" = false → helper "At least one of your parents was alive at the end of 2025"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.sav_born",{"const":true}],"op":"test"},"then":"person.edu_kid_18"},{"guard":{"eq":["person.sav_born",{"const":false}],"op":"test"},"then":"person.edu_parent"}],"op":"choose"}`
- Cite: [i8863] p. 7, Line 7, "You don’t qualify for a refundable American opportunity credit if 1 (a, b, or c), 2, and 3 below apply to you." (2025; sha256 195cfd5e)

## (helper) — `person.edu_kid_18`

- **Authored helper label:** Line 7 conditions 1b, 1c and 2 for you, born before January 2, 2008 (age 18 with earned income less than half of your support and a parent alive, or the tests for 19 to 23)
- **Encoded (Bool):** Choose — [helper "Born before January 2, 2007" = true → helper "Line 7 conditions 1c and 2 for you, born before January 2, 2007 (born after January 1, 2002, first)"] [helper "Born before January 2, 2007" = false → helper "Line 7 conditions 1b and 2 for you, age 18: earned income less than half of your support and a parent alive"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_over18",{"const":true}],"op":"test"},"then":"person.edu_kid_student_age"},{"guard":{"eq":["person.edu_over18",{"const":false}],"op":"test"},"then":"person.edu_kid_18_support"}],"op":"choose"}`
- Cite: [i8863] p. 7, Line 7, "You don’t qualify for a refundable American opportunity credit if 1 (a, b, or c), 2, and 3 below apply to you." (2025; sha256 195cfd5e)

## (helper) — `person.edu_kid_18_support`

- **Authored helper label:** Line 7 conditions 1b and 2 for you, age 18: earned income less than half of your support and a parent alive
- **Encoded (Bool):** Choose — [helper "Your earned income was less than one-half of your support for 2025" = true → helper "At least one of your parents was alive at the end of 2025"] [helper "Your earned income was less than one-half of your support for 2025" = false → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_half_support",{"const":true}],"op":"test"},"then":"person.edu_parent"},{"guard":{"eq":["person.edu_half_support",{"const":false}],"op":"test"},"then":"person.edu_no"}],"op":"choose"}`
- Cite: [i8863] p. 7, Line 7, "You don’t qualify for a refundable American opportunity credit if 1 (a, b, or c), 2, and 3 below apply to you." (2025; sha256 195cfd5e)

## (helper) — `person.edu_kid_student_age`

- **Authored helper label:** Line 7 conditions 1c and 2 for you, born before January 2, 2007 (born after January 1, 2002, first)
- **Encoded (Bool):** Choose — [helper "Born before January 2, 2002" = true → helper "Year parameter edu.no (false)"] [helper "Born before January 2, 2002" = false → helper "Line 7 conditions 1c and 2 for you, born after January 1, 2002, and before January 2, 2007 (earned income less than half of your support first)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_age24",{"const":true}],"op":"test"},"then":"person.edu_no"},{"guard":{"eq":["person.edu_age24",{"const":false}],"op":"test"},"then":"person.edu_kid_support"}],"op":"choose"}`
- Cite: [i8863] p. 7, Line 7, "You don’t qualify for a refundable American opportunity credit if 1 (a, b, or c), 2, and 3 below apply to you." (2025; sha256 195cfd5e)

## (helper) — `person.edu_kid_support`

- **Authored helper label:** Line 7 conditions 1c and 2 for you, born after January 1, 2002, and before January 2, 2007 (earned income less than half of your support first)
- **Encoded (Bool):** Choose — [helper "Your earned income was less than one-half of your support for 2025" = true → helper "Line 7 conditions 1c and 2 for you, born after January 1, 2002, and before January 2, 2007, with earned income less than half of your support: a full-time student and a parent alive"] [helper "Your earned income was less than one-half of your support for 2025" = false → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_half_support",{"const":true}],"op":"test"},"then":"person.edu_kid_fulltime"},{"guard":{"eq":["person.edu_half_support",{"const":false}],"op":"test"},"then":"person.edu_no"}],"op":"choose"}`
- Cite: [i8863] p. 7, Line 7, "You don’t qualify for a refundable American opportunity credit if 1 (a, b, or c), 2, and 3 below apply to you." (2025; sha256 195cfd5e)

## (helper) — `person.edu_kid_fulltime`

- **Authored helper label:** Line 7 conditions 1c and 2 for you, born after January 1, 2002, and before January 2, 2007, with earned income less than half of your support: a full-time student and a parent alive
- **Encoded (Bool):** Choose — [helper "A full-time student for 2025 (any part of 5 calendar months at an eligible educational institution)" = true → helper "At least one of your parents was alive at the end of 2025"] [helper "A full-time student for 2025 (any part of 5 calendar months at an eligible educational institution)" = false → helper "Year parameter edu.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.edu_fulltime",{"const":true}],"op":"test"},"then":"person.edu_parent"},{"guard":{"eq":["person.edu_fulltime",{"const":false}],"op":"test"},"then":"person.edu_no"}],"op":"choose"}`
- Cite: [i8863] p. 7, Line 7, "You don’t qualify for a refundable American opportunity credit if 1 (a, b, or c), 2, and 3 below apply to you." (2025; sha256 195cfd5e)

## (helper) — `person.edu_kid`

- **Authored helper label:** Line 7 conditions 1 and 2 for you: under 18; or 18 with earned income less than half of your support; or over 18 and under 24, a full-time student, with earned income less than half of your support; and a parent alive
- **Encoded (Bool):** Choose — [f8863 helper "Line 7 is above zero on a return that is not joint (the line 7 conditions are asked)" = true → helper "Line 7 conditions 1 and 2 for you (under 18 and a parent alive, or the tests for 18 to 23)"] [f8863 helper "Line 7 is above zero on a return that is not joint (the line 7 conditions are asked)" = false → helper "Year parameter edu.no (false)"]
- Interpretation: amb.2025.edu_age_rule
- Expr: `{"alternatives":[{"guard":{"eq":["f8863.kid_needed",{"const":true}],"op":"test"},"then":"person.edu_kid_age"},{"guard":{"eq":["f8863.kid_needed",{"const":false}],"op":"test"},"then":"person.edu_no"}],"op":"choose"}`
- Cite: [i8863] p. 7, Line 7, "You don’t qualify for a refundable American opportunity credit if 1 (a, b, or c), 2, and 3 below apply to you." (2025; sha256 195cfd5e)

## (helper) — `person.x_l1`

- **Authored helper label:** Form 5329 line 1 for this person: early distributions includible in income
- **Encoded (NonNegDollars):** Add retirement.l1 over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.l1","op":"sum_over"}`
- Cite: [i5329] p. 3, Line 1, "Enter the amount of early distributions includible in income (other than qualified disaster recovery distributions) that you received from:" (2025; sha256 aec3d325)

## (helper) — `person.x_l2_all`

- **Authored helper label:** Exception amounts before the per-person limits
- **Encoded (NonNegDollars):** Add retirement.l2 over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.l2","op":"sum_over"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (helper) — `person.x_l1_s`

- **Authored helper label:** Line 1 amounts from code S distributions
- **Encoded (NonNegDollars):** Add retirement.l1_s over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.l1_s","op":"sum_over"}`
- Cite: [i5329] p. 5, Line 4, "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%." (2025; sha256 aec3d325)

## (helper) — `person.x_l2_s`

- **Authored helper label:** Line 2 amounts from code S distributions
- **Encoded (NonNegDollars):** Add retirement.l2_s over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.l2_s","op":"sum_over"}`
- Cite: [i5329] p. 5, Line 4, "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%." (2025; sha256 aec3d325)

## (helper) — `person.x_e05`

- **Authored helper label:** Exception 05 amounts
- **Encoded (NonNegDollars):** Add retirement.l2_e05 over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.l2_e05","op":"sum_over"}`
- Cite: [i5329] p. 5, Line 2, "Qualified retirement plan distributions up to the amount you paid for unreimbursed medical expenses during the year minus 7.5% of your adjusted gross income (AGI) for the year." (2025; sha256 aec3d325)

## (helper) — `person.x_e09`

- **Authored helper label:** Exception 09 amounts
- **Encoded (NonNegDollars):** Add retirement.l2_e09 over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.l2_e09","op":"sum_over"}`
- Cite: [p590b] p. 27, First home, "you don't have to pay the 10% additional tax on up to $10,000 of distributions you receive to buy, build, or rebuild a first home." (2025; sha256 d18a592e)

## (helper) — `person.x_e19`

- **Authored helper label:** Exception 19 amounts
- **Encoded (NonNegDollars):** Add retirement.l2_e19 over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.l2_e19","op":"sum_over"}`
- Cite: [p590b] p. 28, Qualified birth or adoption distribution, "A qualified birth or adoption distribution must not exceed $5,000 per taxpayer." (2025; sha256 d18a592e)

## (helper) — `person.x_e22`

- **Authored helper label:** Exception 22 amounts
- **Encoded (NonNegDollars):** Add retirement.l2_e22 over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.l2_e22","op":"sum_over"}`
- Cite: [p590b] p. 28, Distributions to domestic abuse victims, "on to a domestic abuse victim must not exceed the lesser of $10,300 for 2025 or 50% of the present value of the IRA." (2025; sha256 d18a592e)

## (helper) — `person.x_e23`

- **Authored helper label:** Exception 23 amounts
- **Encoded (NonNegDollars):** Add retirement.l2_e23 over every confirmed retirement entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.l2_e23","op":"sum_over"}`
- Cite: [p590b] p. 28, Emergency personal expense distributions, "personal expense distribution must not exceed the lesser of $1,000 or your total interest in the IRA minus $1,000." (2025; sha256 d18a592e)

## (helper) — `person.x_tax`

- **Authored helper label:** This person's Form 5329 taxes
- **Encoded (NonNegDollars):** Add f5329.tax over every confirmed f5329 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f5329","field":"f5329.tax","op":"sum_over"}`
- Cite: [f1040s2] p. 1, Part II, line 8, "Additional tax on IRAs or other tax-favored accounts. Attach Form 5329 if required." (2025; created 2025-05-08; sha256 64d867b6)

## (helper) — `person.x_must`

- **Authored helper label:** One if this person must file Form 5329
- **Encoded (Count):** Add f5329.one over every confirmed f5329 entry for which helper "This person must file Form 5329 (an exception claimed, a code S distribution, or HSA excess)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f5329","field":"f5329.one","op":"sum_over","where":{"eq":["f5329.must",{"const":true}],"op":"test"}}`
- Cite: [i5329] p. 1, Who Must File, "However, if distribution code 1 is correctly shown in box 7 of all your Forms 1099-R and you owe the additional tax on the full amount shown on each Form 1099-R, you don’t have to file Form 5329." (2025; sha256 aec3d325)

## (helper) — `person.x_prior09`

- **Authored helper label:** Earlier first-home distributions excluded from the additional tax
- **Encoded (NonNegDollars):** Input — Total of your earlier IRA distributions (before 2025) for which the first-home exception was used; zero if none
- Expr: `{"op":"input","source":"Total of your earlier IRA distributions (before 2025) for which the first-home exception was used; zero if none"}`
- Cite: [p590b] p. 27, First home, "you don't have to pay the 10% additional tax on up to $10,000 of distributions you receive to buy, build, or rebuild a first home." (2025; sha256 d18a592e)

## (helper) — `person.x_cap09_base`

- **Authored helper label:** Year parameter f5329.cap_first_home ($10,000)
- **Encoded (NonNegDollars):** Enter $10,000 (f5329.cap_first_home).
- Expr: `{"op":"param","ref":"f5329.cap_first_home"}`
- Cite: [p590b] p. 27, First home, "you don't have to pay the 10% additional tax on up to $10,000 of distributions you receive to buy, build, or rebuild a first home." (2025; sha256 d18a592e)

## (helper) — `person.x_cap09`

- **Authored helper label:** First-home limit left: $10,000 less earlier first-home distributions
- **Encoded (NonNegDollars):** Subtract helper "Earlier first-home distributions excluded from the additional tax" from helper "Year parameter f5329.cap_first_home ($10,000)". If zero or less, enter -0-.
- Expr: `{"from":"person.x_cap09_base","op":"subtract_floor0","take":"person.x_prior09"}`
- Cite: [p590b] p. 27, First home, "you don't have to pay the 10% additional tax on up to $10,000 of distributions you receive to buy, build, or rebuild a first home." (2025; sha256 d18a592e)

## (helper) — `person.x_births`

- **Authored helper label:** Number of births or adoptions the distributions were for
- **Encoded (Count):** Input — For how many births or adoptions (children born or adopted, each counted once) did you take the 2025 birth or adoption distributions? Count only a child for whom a 2025 distribution was taken within 1 year of the birth or of the date the adoption became final.
- Expr: `{"op":"input","source":"For how many births or adoptions (children born or adopted, each counted once) did you take the 2025 birth or adoption distributions? Count only a child for whom a 2025 distribution was taken within 1 year of the birth or of the date the adoption became final."}`
- Cite: [p590b] p. 28, Qualified birth or adoption distribution, "A qualified birth or adoption distribution is any distribution from an applicable eligible retirement plan if made during the 1-year period beginning on the date on which your child was born or the date on which the legal adoption of your child was finalized" and "A qualified birth or adoption distribution must not exceed $5,000 per taxpayer." (2025; sha256 d18a592e)

## (helper) — `person.x_cap19_one`

- **Authored helper label:** Year parameter f5329.cap_birth ($5,000)
- **Encoded (NonNegDollars):** Enter $5,000 (f5329.cap_birth).
- Expr: `{"op":"param","ref":"f5329.cap_birth"}`
- Cite: [p590b] p. 28, Qualified birth or adoption distribution, "A qualified birth or adoption distribution must not exceed $5,000 per taxpayer." (2025; sha256 d18a592e)

## (helper) — `person.x_cap19`

- **Authored helper label:** $5,000 for each birth or adoption
- **Encoded (NonNegDollars):** Multiply helper "Year parameter f5329.cap_birth ($5,000)" by the number on helper "Number of births or adoptions the distributions were for".
- Interpretation: amb.2025.f5329_birth_cap
- Expr: `{"amount":"person.x_cap19_one","count":"person.x_births","op":"multiply_count"}`
- Cite: [p590b] p. 28, Qualified birth or adoption distribution, "A qualified birth or adoption distribution must not exceed $5,000 per taxpayer." (2025; sha256 d18a592e)

## (helper) — `person.x_cap22`

- **Authored helper label:** Year parameter f5329.cap_abuse ($10,300)
- **Encoded (NonNegDollars):** Enter $10,300 (f5329.cap_abuse).
- Expr: `{"op":"param","ref":"f5329.cap_abuse"}`
- Cite: [p590b] p. 28, Distributions to domestic abuse victims, "on to a domestic abuse victim must not exceed the lesser of $10,300 for 2025 or 50% of the present value of the IRA." (2025; sha256 d18a592e)

## (helper) — `person.x_cap23`

- **Authored helper label:** Year parameter f5329.cap_emergency ($1,000)
- **Encoded (NonNegDollars):** Enter $1,000 (f5329.cap_emergency).
- Expr: `{"op":"param","ref":"f5329.cap_emergency"}`
- Cite: [p590b] p. 28, Emergency personal expense distributions, "personal expense distribution must not exceed the lesser of $1,000 or your total interest in the IRA minus $1,000." (2025; sha256 d18a592e)

## (helper) — `person.x_c05`

- **Authored helper label:** Exception 05 limited to the medical expenses above 7.5% of AGI (Schedule A line 4)
- **Encoded (NonNegDollars):** Choose — [helper "Any exception 05 amount" = true → helper "Smaller of the exception 05 amounts and Schedule A line 4"] [helper "Any exception 05 amount" = false → line zero]
- Interpretation: amb.2025.f5329_medical_joint
- Expr: `{"alternatives":[{"guard":{"eq":["person.x_has05",{"const":true}],"op":"test"},"then":"person.x_c05_min"},{"guard":{"eq":["person.x_has05",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [i5329] p. 5, Line 2, "Qualified retirement plan distributions up to the amount you paid for unreimbursed medical expenses during the year minus 7.5% of your adjusted gross income (AGI) for the year." (2025; sha256 aec3d325)

## (helper) — `person.x_has05`

- **Authored helper label:** Any exception 05 amount
- **Encoded (Bool):** helper "Exception 05 amounts" > $0
- Expr: `{"gt":["person.x_e05",{"const":0}],"op":"test"}`
- Cite: [i5329] p. 5, Line 2, "Qualified retirement plan distributions up to the amount you paid for unreimbursed medical expenses during the year minus 7.5% of your adjusted gross income (AGI) for the year." (2025; sha256 aec3d325)

## (helper) — `person.x_c05_min`

- **Authored helper label:** Smaller of the exception 05 amounts and Schedule A line 4
- **Encoded (NonNegDollars):** Enter the smaller of helper "Exception 05 amounts" or sa line 4.
- Expr: `{"of":["person.x_e05","sa.line4"],"op":"smaller_of"}`
- Cite: [i5329] p. 5, Line 2, "Qualified retirement plan distributions up to the amount you paid for unreimbursed medical expenses during the year minus 7.5% of your adjusted gross income (AGI) for the year." (2025; sha256 aec3d325)

## (helper) — `person.x_has09`

- **Authored helper label:** Any exception 09 amount
- **Encoded (Bool):** helper "Exception 09 amounts" > $0
- Expr: `{"gt":["person.x_e09",{"const":0}],"op":"test"}`
- Cite: [p590b] p. 27, First home, "you don't have to pay the 10% additional tax on up to $10,000 of distributions you receive to buy, build, or rebuild a first home." (2025; sha256 d18a592e)

## (helper) — `person.x_c09_min`

- **Authored helper label:** Smaller of the exception 09 amounts and the limit left
- **Encoded (NonNegDollars):** Enter the smaller of helper "Exception 09 amounts" or helper "First-home limit left: $10,000 less earlier first-home distributions".
- Expr: `{"of":["person.x_e09","person.x_cap09"],"op":"smaller_of"}`
- Cite: [p590b] p. 27, First home, "you don't have to pay the 10% additional tax on up to $10,000 of distributions you receive to buy, build, or rebuild a first home." (2025; sha256 d18a592e)

## (helper) — `person.x_c09`

- **Authored helper label:** Exception 09 within the $10,000 first-home limit
- **Encoded (NonNegDollars):** Choose — [helper "Any exception 09 amount" = true → helper "Smaller of the exception 09 amounts and the limit left"] [helper "Any exception 09 amount" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.x_has09",{"const":true}],"op":"test"},"then":"person.x_c09_min"},{"guard":{"eq":["person.x_has09",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [p590b] p. 27, First home, "you don't have to pay the 10% additional tax on up to $10,000 of distributions you receive to buy, build, or rebuild a first home." (2025; sha256 d18a592e)

## (helper) — `person.x_has19`

- **Authored helper label:** Any exception 19 amount
- **Encoded (Bool):** helper "Exception 19 amounts" > $0
- Expr: `{"gt":["person.x_e19",{"const":0}],"op":"test"}`
- Cite: [p590b] p. 28, Qualified birth or adoption distribution, "A qualified birth or adoption distribution must not exceed $5,000 per taxpayer." (2025; sha256 d18a592e)

## (helper) — `person.x_c19_min`

- **Authored helper label:** Smaller of the exception 19 amounts and $5,000 a birth or adoption
- **Encoded (NonNegDollars):** Enter the smaller of helper "Exception 19 amounts" or helper "$5,000 for each birth or adoption".
- Expr: `{"of":["person.x_e19","person.x_cap19"],"op":"smaller_of"}`
- Cite: [p590b] p. 28, Qualified birth or adoption distribution, "A qualified birth or adoption distribution must not exceed $5,000 per taxpayer." (2025; sha256 d18a592e)

## (helper) — `person.x_c19`

- **Authored helper label:** Exception 19 within $5,000 a birth or adoption
- **Encoded (NonNegDollars):** Choose — [helper "Any exception 19 amount" = true → helper "Smaller of the exception 19 amounts and $5,000 a birth or adoption"] [helper "Any exception 19 amount" = false → line zero]
- Expr: `{"alternatives":[{"guard":{"eq":["person.x_has19",{"const":true}],"op":"test"},"then":"person.x_c19_min"},{"guard":{"eq":["person.x_has19",{"const":false}],"op":"test"},"then":"person.zero"}],"op":"choose"}`
- Cite: [p590b] p. 28, Qualified birth or adoption distribution, "A qualified birth or adoption distribution must not exceed $5,000 per taxpayer." (2025; sha256 d18a592e)

## (helper) — `person.x_c22`

- **Authored helper label:** Exception 22 within $10,300
- **Encoded (NonNegDollars):** Enter the smaller of helper "Exception 22 amounts" or helper "Year parameter f5329.cap_abuse ($10,300)".
- Expr: `{"of":["person.x_e22","person.x_cap22"],"op":"smaller_of"}`
- Cite: [p590b] p. 28, Distributions to domestic abuse victims, "on to a domestic abuse victim must not exceed the lesser of $10,300 for 2025 or 50% of the present value of the IRA." (2025; sha256 d18a592e)

## (helper) — `person.x_c23`

- **Authored helper label:** Exception 23 within $1,000
- **Encoded (NonNegDollars):** Enter the smaller of helper "Exception 23 amounts" or helper "Year parameter f5329.cap_emergency ($1,000)".
- Expr: `{"of":["person.x_e23","person.x_cap23"],"op":"smaller_of"}`
- Cite: [p590b] p. 28, Emergency personal expense distributions, "personal expense distribution must not exceed the lesser of $1,000 or your total interest in the IRA minus $1,000." (2025; sha256 d18a592e)

## (helper) — `person.x_n23`

- **Authored helper label:** Forms 1099-R claiming exception 23
- **Encoded (Count):** Add retirement.one over every confirmed retirement entry for which helper "Exception 23" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"retirement","field":"retirement.one","op":"sum_over","where":{"eq":["retirement.is_e23",{"const":true}],"op":"test"}}`
- Cite: [p590b] p. 28, Distribution limits, "You are limited to taking one emergency personal expense distribution per calendar year" (2025; sha256 d18a592e)

## (gate) — `person.x_two23`

- **Authored helper label:** Exception 23 claimed on more than one distribution
- **Encoded (Bool):** helper "Forms 1099-R claiming exception 23" > 1 (a count)
- Expr: `{"gt":["person.x_n23",{"const":1,"type":"Count"}],"op":"test"}`
- Cite: [p590b] p. 28, Distribution limits, "You are limited to taking one emergency personal expense distribution per calendar year" (2025; sha256 d18a592e)

## (helper) — `person.x_capped_sum`

- **Authored helper label:** Exceptions 05, 09, 19, 22 and 23 before their limits
- **Encoded (NonNegDollars):** Add helper "Exception 05 amounts", helper "Exception 09 amounts", helper "Exception 19 amounts", helper "Exception 22 amounts", and helper "Exception 23 amounts".
- Expr: `{"of":["person.x_e05","person.x_e09","person.x_e19","person.x_e22","person.x_e23"],"op":"sum"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (helper) — `person.x_limited_sum`

- **Authored helper label:** Exceptions 05, 09, 19, 22 and 23 within their limits
- **Encoded (NonNegDollars):** Add helper "Exception 05 limited to the medical expenses above 7.5% of AGI (Schedule A line 4)", helper "Exception 09 within the $10,000 first-home limit", helper "Exception 19 within $5,000 a birth or adoption", helper "Exception 22 within $10,300", and helper "Exception 23 within $1,000".
- Expr: `{"of":["person.x_c05","person.x_c09","person.x_c19","person.x_c22","person.x_c23"],"op":"sum"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (helper) — `person.x_other_exc`

- **Authored helper label:** Exceptions without a fixed limit
- **Encoded (NonNegDollars):** Subtract helper "Exceptions 05, 09, 19, 22 and 23 before their limits" from helper "Exception amounts before the per-person limits". If zero or less, enter -0-.
- Expr: `{"from":"person.x_l2_all","op":"subtract_floor0","take":"person.x_capped_sum"}`
- Cite: [i5329] p. 5, Line 2, "Enter on line 2 the amount that you can exclude.", "In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." (2025; sha256 aec3d325)

## (gate) — `person.x_limit_binds`

- **Authored helper label:** A limited exception over its limit on a person with a code S distribution
- **Encoded (Bool):** helper "Line 1 amounts from code S distributions" > $0 and helper "Exceptions 05, 09, 19, 22 and 23 before their limits" > helper "Exceptions 05, 09, 19, 22 and 23 within their limits"
- Interpretation: amb.2025.f5329_simple_limits
- Expr: `{"all":[{"gt":["person.x_l1_s",{"const":0}],"op":"test"},{"gt":["person.x_capped_sum","person.x_limited_sum"],"op":"test"}],"op":"test"}`
- Cite: [i5329] p. 5, Line 4, "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%." (2025; sha256 aec3d325)

## (gate) — `person.x_other`

- **Authored helper label:** Form 5329 parts this tool does not prepare
- **Encoded (Bool):** (helper "A required minimum distribution not received in full by its deadline (asked only of a person born in 1952 or earlier or with an inherited account; otherwise no)" = true or helper "A taxable distribution from a Coverdell ESA, a qualified tuition program or an ABLE account (asked only with such an account; otherwise no)" = true or helper "Excess contributions to a Coverdell ESA or an ABLE account (asked only with such an account; otherwise no)" = true or helper "Do you have excess contributions to an Archer MSA?" = true or helper "An earlier year's excess IRA contributions remained at the end of 2025 (asked only of a person with an IRA; otherwise no)" = true or helper "An earlier year's excess HSA contributions not removed or used up before 2025 (asked only of a person who listed a health savings account; otherwise no)" = true)
- Expr: `{"any":[{"eq":["person.rmd_missed_if_possible",{"const":true}],"op":"test"},{"eq":["person.x_edu_taxable_if_account",{"const":true}],"op":"test"},{"eq":["person.x_edu_excess_if_account",{"const":true}],"op":"test"},{"eq":["person.x_archer_excess",{"const":true}],"op":"test"},{"eq":["person.x_ira_prior_excess_if_ira_owner",{"const":true}],"op":"test"},{"eq":["person.x_hsa_prior_excess_if_hsa",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [f5329] p. 1, Part II, "Complete this part if you included an amount in income, on Schedule 1 (Form 1040), line 8z, from a Coverdell education savings account (ESA) or a qualified tuition program (QTP), or on Schedule 1 (Form 1040), line 8q, from an ABLE account."; p. 3, Part IX, "Complete this part if you did not receive the minimum required distribution from your qualified retirement plan."; i5329 p. 9, "The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed." (2025; sha256 2ad77023)

## (helper) — `person.x_edu_account`

- **Authored helper label:** A 529 plan, Coverdell ESA or ABLE account of this person had contributions or distributions in 2025
- **Encoded (Bool):** Input — In 2025, was money put into or taken out of a qualified tuition program (529 plan), a Coverdell ESA or an ABLE account that is yours or is held for you?
- Expr: `{"op":"input","source":"In 2025, was money put into or taken out of a qualified tuition program (529 plan), a Coverdell ESA or an ABLE account that is yours or is held for you?"}`
- Cite: [f5329] p. 1, Part II, "Complete this part if you included an amount in income, on Schedule 1 (Form 1040), line 8z, from a Coverdell education savings account (ESA) or a qualified tuition program (QTP), or on Schedule 1 (Form 1040), line 8q, from an ABLE account."; p. 3, Part IX, "Complete this part if you did not receive the minimum required distribution from your qualified retirement plan."; i5329 p. 9, "The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed." (2025; sha256 2ad77023)

## (helper) — `person.x_edu_taxable`

- **Authored helper label:** Did you receive a taxable distribution from a Coverdell ESA, a qualified tuition program (529 plan) or an ABLE account?
- **Encoded (Bool):** Input — Did you receive a taxable distribution from a Coverdell ESA, a qualified tuition program (529 plan) or an ABLE account?
- Expr: `{"op":"input","source":"Did you receive a taxable distribution from a Coverdell ESA, a qualified tuition program (529 plan) or an ABLE account?"}`
- Cite: [f5329] p. 1, Part II, "Complete this part if you included an amount in income, on Schedule 1 (Form 1040), line 8z, from a Coverdell education savings account (ESA) or a qualified tuition program (QTP), or on Schedule 1 (Form 1040), line 8q, from an ABLE account."; p. 3, Part IX, "Complete this part if you did not receive the minimum required distribution from your qualified retirement plan."; i5329 p. 9, "The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed." (2025; sha256 2ad77023)

## (gate) — `person.x_edu_taxable_if_account`

- **Authored helper label:** A taxable distribution from a Coverdell ESA, a qualified tuition program or an ABLE account (asked only with such an account; otherwise no)
- **Encoded (Bool):** Choose — [helper "A 529 plan, Coverdell ESA or ABLE account of this person had contributions or distributions in 2025" = true → helper "Did you receive a taxable distribution from a Coverdell ESA, a qualified tuition program (529 plan) or an ABLE account?"] [helper "A 529 plan, Coverdell ESA or ABLE account of this person had contributions or distributions in 2025" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.x_edu_account",{"const":true}],"op":"test"},"then":"person.x_edu_taxable"},{"guard":{"eq":["person.x_edu_account",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [f5329] p. 1, Part II, "Complete this part if you included an amount in income, on Schedule 1 (Form 1040), line 8z, from a Coverdell education savings account (ESA) or a qualified tuition program (QTP), or on Schedule 1 (Form 1040), line 8q, from an ABLE account."; p. 3, Part IX, "Complete this part if you did not receive the minimum required distribution from your qualified retirement plan."; i5329 p. 9, "The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed." (2025; sha256 2ad77023)

## (helper) — `person.x_edu_excess`

- **Authored helper label:** Do you have excess contributions to a Coverdell ESA or an ABLE account?
- **Encoded (Bool):** Input — Do you have excess contributions to a Coverdell ESA or an ABLE account?
- Expr: `{"op":"input","source":"Do you have excess contributions to a Coverdell ESA or an ABLE account?"}`
- Cite: [f5329] p. 1, Part II, "Complete this part if you included an amount in income, on Schedule 1 (Form 1040), line 8z, from a Coverdell education savings account (ESA) or a qualified tuition program (QTP), or on Schedule 1 (Form 1040), line 8q, from an ABLE account."; p. 3, Part IX, "Complete this part if you did not receive the minimum required distribution from your qualified retirement plan."; i5329 p. 9, "The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed." (2025; sha256 2ad77023)

## (gate) — `person.x_edu_excess_if_account`

- **Authored helper label:** Excess contributions to a Coverdell ESA or an ABLE account (asked only with such an account; otherwise no)
- **Encoded (Bool):** Choose — [helper "A 529 plan, Coverdell ESA or ABLE account of this person had contributions or distributions in 2025" = true → helper "Do you have excess contributions to a Coverdell ESA or an ABLE account?"] [helper "A 529 plan, Coverdell ESA or ABLE account of this person had contributions or distributions in 2025" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.x_edu_account",{"const":true}],"op":"test"},"then":"person.x_edu_excess"},{"guard":{"eq":["person.x_edu_account",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [f5329] p. 1, Part II, "Complete this part if you included an amount in income, on Schedule 1 (Form 1040), line 8z, from a Coverdell education savings account (ESA) or a qualified tuition program (QTP), or on Schedule 1 (Form 1040), line 8q, from an ABLE account."; p. 3, Part IX, "Complete this part if you did not receive the minimum required distribution from your qualified retirement plan."; i5329 p. 9, "The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed." (2025; sha256 2ad77023)

## (helper) — `person.x_archer_excess`

- **Authored helper label:** Do you have excess contributions to an Archer MSA?
- **Encoded (Bool):** Input — Do you have excess contributions to an Archer MSA?
- Expr: `{"op":"input","source":"Do you have excess contributions to an Archer MSA?"}`
- Cite: [f5329] p. 1, Part II, "Complete this part if you included an amount in income, on Schedule 1 (Form 1040), line 8z, from a Coverdell education savings account (ESA) or a qualified tuition program (QTP), or on Schedule 1 (Form 1040), line 8q, from an ABLE account."; p. 3, Part IX, "Complete this part if you did not receive the minimum required distribution from your qualified retirement plan."; i5329 p. 9, "The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed." (2025; sha256 2ad77023)

## (helper) — `person.x_ira_prior_excess`

- **Authored helper label:** Did excess contributions to a traditional or Roth IRA for an earlier year remain in the IRA at the end of 2025 (whether or not you contributed for 2025)?
- **Encoded (Bool):** Input — Did excess contributions to a traditional or Roth IRA for an earlier year remain in the IRA at the end of 2025 (whether or not you contributed for 2025)?
- Expr: `{"op":"input","source":"Did excess contributions to a traditional or Roth IRA for an earlier year remain in the IRA at the end of 2025 (whether or not you contributed for 2025)?"}`
- Cite: [f5329] p. 1, Part II, "Complete this part if you included an amount in income, on Schedule 1 (Form 1040), line 8z, from a Coverdell education savings account (ESA) or a qualified tuition program (QTP), or on Schedule 1 (Form 1040), line 8q, from an ABLE account."; p. 3, Part IX, "Complete this part if you did not receive the minimum required distribution from your qualified retirement plan."; i5329 p. 9, "The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed." (2025; sha256 2ad77023)

## (gate) — `person.x_ira_prior_excess_if_ira_owner`

- **Authored helper label:** An earlier year's excess IRA contributions remained at the end of 2025 (asked only of a person with an IRA; otherwise no)
- **Encoded (Bool):** Choose — [helper "Had an IRA of any kind at any time in 2025, or has one now (traditional, Roth, SEP or SIMPLE, inherited, or opened in 2026 for 2025)" = true → helper "Did excess contributions to a traditional or Roth IRA for an earlier year remain in the IRA at the end of 2025 (whether or not you contributed for 2025)?"] [helper "Had an IRA of any kind at any time in 2025, or has one now (traditional, Roth, SEP or SIMPLE, inherited, or opened in 2026 for 2025)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.ira_owner",{"const":true}],"op":"test"},"then":"person.x_ira_prior_excess"},{"guard":{"eq":["person.ira_owner",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [f5329] p. 1, Part II, "Complete this part if you included an amount in income, on Schedule 1 (Form 1040), line 8z, from a Coverdell education savings account (ESA) or a qualified tuition program (QTP), or on Schedule 1 (Form 1040), line 8q, from an ABLE account."; p. 3, Part IX, "Complete this part if you did not receive the minimum required distribution from your qualified retirement plan."; i5329 p. 9, "The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed." (2025; sha256 2ad77023)

## (helper) — `person.has_hsa`

- **Authored helper label:** This person listed a health savings account
- **Encoded (Bool):** helper "Number of Forms 8889 entered for this person" > 0 (a count)
- Expr: `{"gt":["person.hsa_forms",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [f5329] p. 1, Part II, "Complete this part if you included an amount in income, on Schedule 1 (Form 1040), line 8z, from a Coverdell education savings account (ESA) or a qualified tuition program (QTP), or on Schedule 1 (Form 1040), line 8q, from an ABLE account."; p. 3, Part IX, "Complete this part if you did not receive the minimum required distribution from your qualified retirement plan."; i5329 p. 9, "The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed." (2025; sha256 2ad77023)

## (helper) — `person.x_hsa_prior_excess`

- **Authored helper label:** Do you have excess HSA contributions from an earlier year that you had not removed or used up before 2025 (including any amount on line 48 of your 2024 Form 5329, or an excess you never reported)?
- **Encoded (Bool):** Input — Do you have excess HSA contributions from an earlier year that you had not removed or used up before 2025 (including any amount on line 48 of your 2024 Form 5329, or an excess you never reported)?
- Expr: `{"op":"input","source":"Do you have excess HSA contributions from an earlier year that you had not removed or used up before 2025 (including any amount on line 48 of your 2024 Form 5329, or an excess you never reported)?"}`
- Cite: [f5329] p. 1, Part II, "Complete this part if you included an amount in income, on Schedule 1 (Form 1040), line 8z, from a Coverdell education savings account (ESA) or a qualified tuition program (QTP), or on Schedule 1 (Form 1040), line 8q, from an ABLE account."; p. 3, Part IX, "Complete this part if you did not receive the minimum required distribution from your qualified retirement plan."; i5329 p. 9, "The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed." (2025; sha256 2ad77023)

## (gate) — `person.x_hsa_prior_excess_if_hsa`

- **Authored helper label:** An earlier year's excess HSA contributions not removed or used up before 2025 (asked only of a person who listed a health savings account; otherwise no)
- **Encoded (Bool):** Choose — [helper "This person listed a health savings account" = true → helper "Do you have excess HSA contributions from an earlier year that you had not removed or used up before 2025 (including any amount on line 48 of your 2024 Form 5329, or an excess you never reported)?"] [helper "This person listed a health savings account" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.has_hsa",{"const":true}],"op":"test"},"then":"person.x_hsa_prior_excess"},{"guard":{"eq":["person.has_hsa",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [f5329] p. 1, Part II, "Complete this part if you included an amount in income, on Schedule 1 (Form 1040), line 8z, from a Coverdell education savings account (ESA) or a qualified tuition program (QTP), or on Schedule 1 (Form 1040), line 8q, from an ABLE account."; p. 3, Part IX, "Complete this part if you did not receive the minimum required distribution from your qualified retirement plan."; i5329 p. 9, "The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed." (2025; sha256 2ad77023)

## (helper) — `person.rmd_age`

- **Authored helper label:** Born in 1952 or earlier (age 73 or older at the end of 2025)
- **Encoded (Bool):** helper "The year you were born" < 1953 (age.cut_73)
- Expr: `{"lt":["person.birth_year",{"param":"age.cut_73"}],"op":"test"}`
- Cite: [f5329] p. 1, Part II, "Complete this part if you included an amount in income, on Schedule 1 (Form 1040), line 8z, from a Coverdell education savings account (ESA) or a qualified tuition program (QTP), or on Schedule 1 (Form 1040), line 8q, from an ABLE account."; p. 3, Part IX, "Complete this part if you did not receive the minimum required distribution from your qualified retirement plan."; i5329 p. 9, "The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed." (2025; sha256 2ad77023)

## (helper) — `person.inherited_account`

- **Authored helper label:** Have you inherited an IRA or an account in a retirement plan from someone who died?
- **Encoded (Bool):** Input — Have you inherited an IRA or an account in a retirement plan from someone who died?
- Expr: `{"op":"input","source":"Have you inherited an IRA or an account in a retirement plan from someone who died?"}`
- Cite: [f5329] p. 1, Part II, "Complete this part if you included an amount in income, on Schedule 1 (Form 1040), line 8z, from a Coverdell education savings account (ESA) or a qualified tuition program (QTP), or on Schedule 1 (Form 1040), line 8q, from an ABLE account."; p. 3, Part IX, "Complete this part if you did not receive the minimum required distribution from your qualified retirement plan."; i5329 p. 9, "The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed." (2025; sha256 2ad77023)

## (gate) — `person.inherited_account_if_under_73`

- **Authored helper label:** Inherited an IRA or a retirement plan account (asked only of a person born after 1952; otherwise no)
- **Encoded (Bool):** Choose — [helper "Born in 1952 or earlier (age 73 or older at the end of 2025)" = false → helper "Have you inherited an IRA or an account in a retirement plan from someone who died?"] [helper "Born in 1952 or earlier (age 73 or older at the end of 2025)" = true → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.rmd_age",{"const":false}],"op":"test"},"then":"person.inherited_account"},{"guard":{"eq":["person.rmd_age",{"const":true}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [f5329] p. 1, Part II, "Complete this part if you included an amount in income, on Schedule 1 (Form 1040), line 8z, from a Coverdell education savings account (ESA) or a qualified tuition program (QTP), or on Schedule 1 (Form 1040), line 8q, from an ABLE account."; p. 3, Part IX, "Complete this part if you did not receive the minimum required distribution from your qualified retirement plan."; i5329 p. 9, "The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed." (2025; sha256 2ad77023)

## (helper) — `person.rmd_possible`

- **Authored helper label:** A required minimum distribution is possible for this person (born in 1952 or earlier, or inherited an account)
- **Encoded (Bool):** (helper "Born in 1952 or earlier (age 73 or older at the end of 2025)" = true or helper "Inherited an IRA or a retirement plan account (asked only of a person born after 1952; otherwise no)" = true)
- Expr: `{"any":[{"eq":["person.rmd_age",{"const":true}],"op":"test"},{"eq":["person.inherited_account_if_under_73",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [f5329] p. 1, Part II, "Complete this part if you included an amount in income, on Schedule 1 (Form 1040), line 8z, from a Coverdell education savings account (ESA) or a qualified tuition program (QTP), or on Schedule 1 (Form 1040), line 8q, from an ABLE account."; p. 3, Part IX, "Complete this part if you did not receive the minimum required distribution from your qualified retirement plan."; i5329 p. 9, "The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed." (2025; sha256 2ad77023)

## (helper) — `person.rmd_missed`

- **Authored helper label:** Was there a required minimum distribution from an IRA or plan that you did not receive in full by its deadline (including a shortfall you made up later)?
- **Encoded (Bool):** Input — Was there a required minimum distribution from an IRA or plan that you did not receive in full by its deadline (including a shortfall you made up later)?
- Expr: `{"op":"input","source":"Was there a required minimum distribution from an IRA or plan that you did not receive in full by its deadline (including a shortfall you made up later)?"}`
- Cite: [f5329] p. 1, Part II, "Complete this part if you included an amount in income, on Schedule 1 (Form 1040), line 8z, from a Coverdell education savings account (ESA) or a qualified tuition program (QTP), or on Schedule 1 (Form 1040), line 8q, from an ABLE account."; p. 3, Part IX, "Complete this part if you did not receive the minimum required distribution from your qualified retirement plan."; i5329 p. 9, "The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed." (2025; sha256 2ad77023)

## (gate) — `person.rmd_missed_if_possible`

- **Authored helper label:** A required minimum distribution not received in full by its deadline (asked only of a person born in 1952 or earlier or with an inherited account; otherwise no)
- **Encoded (Bool):** Choose — [helper "A required minimum distribution is possible for this person (born in 1952 or earlier, or inherited an account)" = true → helper "Was there a required minimum distribution from an IRA or plan that you did not receive in full by its deadline (including a shortfall you made up later)?"] [helper "A required minimum distribution is possible for this person (born in 1952 or earlier, or inherited an account)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.rmd_possible",{"const":true}],"op":"test"},"then":"person.rmd_missed"},{"guard":{"eq":["person.rmd_possible",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [f5329] p. 1, Part II, "Complete this part if you included an amount in income, on Schedule 1 (Form 1040), line 8z, from a Coverdell education savings account (ESA) or a qualified tuition program (QTP), or on Schedule 1 (Form 1040), line 8q, from an ABLE account."; p. 3, Part IX, "Complete this part if you did not receive the minimum required distribution from your qualified retirement plan."; i5329 p. 9, "The additional tax is 25% of the excess accumulation, which is the difference between the amount that was required to be distributed and the amount that was actually distributed." (2025; sha256 2ad77023)

## (helper) — `person.x_hsa_value`

- **Authored helper label:** Value of your HSAs on December 31, 2025 (including 2025 contributions made in 2026)
- **Encoded (NonNegDollars):** Input — Total value of your HSAs on December 31, 2025, including contributions for 2025 that you made in 2026 (asked only when you have excess HSA contributions)
- Expr: `{"op":"input","source":"Total value of your HSAs on December 31, 2025, including contributions for 2025 that you made in 2026 (asked only when you have excess HSA contributions)"}`
- Cite: [f5329] p. 2, Part VII, line 49, "Additional tax. Enter 6% (0.06) of the smaller of line 48 or the value of your HSAs on December 31, 2025 (including 2025 contributions made in 2026)." (2025; sha256 2ad77023)

## (helper) — `person.x_hsa_excess`

- **Authored helper label:** This person's 2025 HSA excess contributions (Form 8889)
- **Encoded (NonNegDollars):** Add f8889.excess_amt over every confirmed f8889 entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"f8889","field":"f8889.excess_amt","op":"sum_over"}`
- Cite: [i5329] p. 8, Line 47, "Enter the excess of your contributions (made by you or on your behalf) to your HSAs for 2025 from Form 8889, line 2 (unless withdrawn—discussed next), over your contribution limit (Form 8889, line 12)." (2025; sha256 aec3d325)

## (helper) — `person.senior_work_ssn`

- **Authored helper label:** Born before January 2, 1961, and has a valid SSN
- **Encoded (Bool):** Choose — [helper "Born before January 2, 1961" = true → helper "Do you have an SSN valid for employment issued before the due date of your return?"] [helper "Born before January 2, 1961" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.age65",{"const":true}],"op":"test"},"then":"person.work_ssn"},{"guard":{"eq":["person.age65",{"const":false}],"op":"test"},"then":"person.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Fill out Schedule 1-A, Part V, only if" and "If you are married filing jointly, the spouse who is claiming the enhanced deduction for seniors must have a valid SSN" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.spouse_senior_work_ssn`

- **Authored helper label:** Your spouse's entry, if your spouse was born before January 2, 1961, and has a valid SSN
- **Encoded (Bool):** Choose — [helper "Whose entry is this, yours or your spouse's?" = 'taxpayer' → helper "Year parameter household.no (false)"] [helper "Whose entry is this, yours or your spouse's?" = 'spouse' → helper "Born before January 2, 1961, and has a valid SSN"]
- Expr: `{"alternatives":[{"guard":{"eq":["person.role",{"const":"taxpayer"}],"op":"test"},"then":"person.no"},{"guard":{"eq":["person.role",{"const":"spouse"}],"op":"test"},"then":"person.senior_work_ssn"}],"op":"choose"}`
- Cite: [i1040gi] p. 110, Schedule 1-A, Part V, "Fill out Schedule 1-A, Part V, only if" and "If you are married filing jointly, the spouse who is claiming the enhanced deduction for seniors must have a valid SSN" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `person.k1p_total_passive_income`

- **Authored helper label:** Schedule E line 28 column (h), all partnership K-1s
- **Encoded (NonNegDollars):** Add k1p.col_h over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.col_h","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_nonpassive_income`

- **Authored helper label:** Schedule E line 28 column (k), all partnership K-1s
- **Encoded (NonNegDollars):** Add k1p.col_k over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.col_k","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_nonpassive_loss`

- **Authored helper label:** Schedule E line 28 column (i), all partnership K-1s (as a positive amount)
- **Encoded (NonNegDollars):** Add k1p.col_i over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.col_i","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_nonpassive`

- **Authored helper label:** Nonpassive income less nonpassive loss, all partnership K-1s
- **Encoded (Dollars):** Add k1p.nonpassive_net over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.nonpassive_net","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_p4_income`

- **Authored helper label:** Form 8582 Part IV column (a), partnership K-1s
- **Encoded (NonNegDollars):** Add k1p.p4_income over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.p4_income","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_p4_loss`

- **Authored helper label:** Form 8582 Part IV column (b), partnership K-1s
- **Encoded (NonNegDollars):** Add k1p.p4_loss over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.p4_loss","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_p4_prior`

- **Authored helper label:** Form 8582 Part IV column (c), partnership K-1s
- **Encoded (NonNegDollars):** Add k1p.p4_prior over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.p4_prior","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_p5_income`

- **Authored helper label:** Form 8582 Part V column (a), partnership K-1s
- **Encoded (NonNegDollars):** Add k1p.p5_income over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.p5_income","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_p5_loss`

- **Authored helper label:** Form 8582 Part V column (b), partnership K-1s
- **Encoded (NonNegDollars):** Add k1p.p5_loss over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.p5_loss","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_p5_prior`

- **Authored helper label:** Form 8582 Part V column (c), partnership K-1s
- **Encoded (NonNegDollars):** Add k1p.p5_prior over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.p5_prior","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_p6_loss`

- **Authored helper label:** Form 8582 Part VI column (a), partnership K-1s
- **Encoded (NonNegDollars):** Add k1p.p6_loss over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.p6_loss","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_prior`

- **Authored helper label:** Prior years unallowed losses, partnership K-1s
- **Encoded (NonNegDollars):** Add k1p.prior_total over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.prior_total","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_interest`

- **Authored helper label:** Interest income (K-1 box 5), all partnership K-1s
- **Encoded (NonNegDollars):** Add k1p.box5_if_any over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.box5_if_any","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_ord_div`

- **Authored helper label:** Ordinary dividends (K-1 box 6a), all partnership K-1s
- **Encoded (NonNegDollars):** Add k1p.box6a_if_any over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.box6a_if_any","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_qual_div`

- **Authored helper label:** Qualified dividends (K-1 box 6b), all partnership K-1s
- **Encoded (NonNegDollars):** Add k1p.box6b_if_any over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.box6b_if_any","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_st_gain`

- **Authored helper label:** Net short-term capital gain or loss (K-1 box 8), all partnership K-1s
- **Encoded (Dollars):** Add k1p.box8_if_any over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.box8_if_any","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_lt_gain`

- **Authored helper label:** Net long-term capital gain or loss (K-1 box 9a), all partnership K-1s
- **Encoded (Dollars):** Add k1p.box9a_if_any over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.box9a_if_any","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_collectibles`

- **Authored helper label:** Collectibles (28%) gain or loss (K-1 box 9b), all partnership K-1s
- **Encoded (Dollars):** Add k1p.box9b_if_any over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.box9b_if_any","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_unrecap_1250`

- **Authored helper label:** Unrecaptured section 1250 gain (K-1 box 9c), all partnership K-1s
- **Encoded (NonNegDollars):** Add k1p.box9c_if_any over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.box9c_if_any","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_se_earnings`

- **Authored helper label:** Net earnings from self-employment (K-1 box 14, code A), all partnership K-1s
- **Encoded (Dollars):** Add k1p.box14a_if_any over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.box14a_if_any","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_se_pos`

- **Authored helper label:** Positive net earnings from self-employment (K-1 box 14, code A), all partnership K-1s
- **Encoded (NonNegDollars):** Add k1p.se_pos over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.se_pos","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_backup_wh`

- **Authored helper label:** Backup withholding (K-1 box 15, code O), all partnership K-1s
- **Encoded (NonNegDollars):** Add k1p.box15o_if_any over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.box15o_if_any","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_taxexempt_int`

- **Authored helper label:** Tax-exempt interest (K-1 box 18, code A), all partnership K-1s
- **Encoded (NonNegDollars):** Add k1p.box18a_if_any over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.box18a_if_any","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_total_qbi_stmt`

- **Authored helper label:** QBI or loss from the section 199A statements (K-1 box 20, code Z), all partnership K-1s
- **Encoded (Dollars):** Add k1p.box20z_if_any over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.box20z_if_any","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_count`

- **Authored helper label:** Number of partnership K-1s
- **Encoded (Count):** Add k1p.one over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.one","op":"sum_over","where":{"eq":["k1p.screened",{"const":true}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_count_sche`

- **Authored helper label:** Number of partnership K-1s with a row on Schedule E line 28
- **Encoded (Count):** Add k1p.one over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true and helper "The K-1 puts a row on Schedule E line 28 (an amount in box 1, 2, 3 or 4a, or a held-back loss)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.one","op":"sum_over","where":{"all":[{"eq":["k1p.screened",{"const":true}],"op":"test"},{"eq":["k1p.sche_row",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_count_passive_loss`

- **Authored helper label:** Number of partnership K-1s with a passive net loss or held-back loss
- **Encoded (Count):** Add k1p.one over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true and helper "A passive activity of this K-1 has a net loss or a prior years unallowed loss" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.one","op":"sum_over","where":{"all":[{"eq":["k1p.screened",{"const":true}],"op":"test"},{"eq":["k1p.passive_loss",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_count_inv`

- **Authored helper label:** Number of partnership K-1s with box 20, code A or B
- **Encoded (Count):** Add k1p.one over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true and helper "Box 20 shows code A or B: investment income or expenses" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.one","op":"sum_over","where":{"all":[{"eq":["k1p.screened",{"const":true}],"op":"test"},{"eq":["k1p.has_b20ab",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1p_count_general`

- **Authored helper label:** Number of partnership K-1s held as a general partner
- **Encoded (Count):** Add k1p.one over every confirmed k1p entry for which helper "This Schedule K-1 passed every screen (true; the refusals of a K-1 are told here)" = true and helper "General partner or LLC member-manager (item G)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1p","field":"k1p.one","op":"sum_over","where":{"all":[{"eq":["k1p.screened",{"const":true}],"op":"test"},{"eq":["k1p.general",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [i1065sk1] p. 14, Codes, "report items from each partnership’s Schedule K-1 on a separate line 28 of Schedule E" (2025; sha256 659063e0)

## (helper) — `person.k1s_total_interest`

- **Authored helper label:** Interest income from Schedules K-1 (Form 1120-S), box 4
- **Encoded (NonNegDollars):** Add k1s.int over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.int","op":"sum_over"}`
- Cite: [i1120ssk] p. 7, Box 4. Interest Income, "Report interest income on Form 1040 or 1040-SR, line 2b" (2025; sha256 fb6194da)

## (helper) — `person.k1s_total_ord_div`

- **Authored helper label:** Ordinary dividends from Schedules K-1 (Form 1120-S), box 5a
- **Encoded (NonNegDollars):** Add k1s.ord_div over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.ord_div","op":"sum_over"}`
- Cite: [i1120ssk] p. 7, Box 5a. Ordinary Dividends, "Report ordinary dividends on Form 1040 or 1040-SR, line 3b" (2025; sha256 fb6194da)

## (helper) — `person.k1s_total_qual_div`

- **Authored helper label:** Qualified dividends from Schedules K-1 (Form 1120-S), box 5b
- **Encoded (NonNegDollars):** Add k1s.qual_div over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.qual_div","op":"sum_over"}`
- Cite: [i1120ssk] p. 7, Box 5b. Qualified Dividends, "Report any qualified dividends on Form 1040 or 1040-SR, line 3a" (2025; sha256 fb6194da)

## (helper) — `person.k1s_total_st_gain`

- **Authored helper label:** Net short-term capital gain (loss) from Schedules K-1 (Form 1120-S), box 7
- **Encoded (Dollars):** Add k1s.st over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.st","op":"sum_over"}`
- Cite: [i1120ssk] p. 7, Box 7. Net Short-Term Capital Gain (Loss), "report the net short-term capital gain (loss) on Schedule D (Form 1040), Capital Gains and Losses, line 5" (2025; sha256 fb6194da)

## (helper) — `person.k1s_total_lt_gain`

- **Authored helper label:** Net long-term capital gain (loss) from Schedules K-1 (Form 1120-S), box 8a
- **Encoded (Dollars):** Add k1s.lt over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.lt","op":"sum_over"}`
- Cite: [i1120ssk] p. 7, Box 8a. Net Long-Term Capital Gain (Loss), "report the net long-term capital gain (loss) on Schedule D (Form 1040), line 12" (2025; sha256 fb6194da)

## (helper) — `person.k1s_total_collectibles`

- **Authored helper label:** Collectibles (28%) gain (loss) from Schedules K-1 (Form 1120-S), box 8b
- **Encoded (Dollars):** Add k1s.g28 over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.g28","op":"sum_over"}`
- Cite: [i1120ssk] p. 7, Box 8b. Collectibles (28%) Gain (Loss), "report collectibles gain or loss on line 4 of the 28% Rate Gain Worksheet" (2025; sha256 fb6194da)

## (helper) — `person.k1s_total_unrecap_1250`

- **Authored helper label:** Unrecaptured section 1250 gain from Schedules K-1 (Form 1120-S), box 8c
- **Encoded (NonNegDollars):** Add k1s.u1250 over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.u1250","op":"sum_over"}`
- Cite: [i1120ssk] p. 7, Box 8c. Unrecaptured Section 1250 Gain, "Report unrecaptured section 1250 gain from the sale or exchange of the corporation’s business assets on line 5" (2025; sha256 fb6194da)

## (helper) — `person.k1s_total_backup_wh`

- **Authored helper label:** Backup withholding from Schedules K-1 (Form 1120-S), box 13, code O
- **Encoded (NonNegDollars):** Add k1s.backup over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.backup","op":"sum_over"}`
- Cite: [i1120ssk] p. 13, Code O. Backup withholding, "Include this amount in the total you enter on Form 1040 or 1040-SR, line 25c" (2025; sha256 fb6194da)

## (helper) — `person.k1s_total_taxexempt_int`

- **Authored helper label:** Tax-exempt interest from Schedules K-1 (Form 1120-S), box 16, code A
- **Encoded (NonNegDollars):** Add k1s.taxexempt over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.taxexempt","op":"sum_over"}`
- Cite: [i1120ssk] p. 15, Code A. Tax-exempt interest income, "Individual shareholders include this amount on Form 1040 or 1040-SR, line 2a" (2025; sha256 fb6194da)

## (helper) — `person.k1s_total_passive_income`

- **Authored helper label:** Schedule E line 28, column (h) total of the S corporation rows: passive income
- **Encoded (NonNegDollars):** Add k1s.col_h over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.col_h","op":"sum_over"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "If income is reported in box 1, report the income in column (h) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## (helper) — `person.k1s_total_nonpassive_loss`

- **Authored helper label:** Schedule E line 28, column (i) total of the S corporation rows: nonpassive loss allowed, as a positive amount
- **Encoded (NonNegDollars):** Add k1s.col_i over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.col_i","op":"sum_over"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "Report box 1 income (loss) from corporate trade or business activities in which you materially participated in column (i) or (k) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## (helper) — `person.k1s_total_nonpassive_income`

- **Authored helper label:** Schedule E line 28, column (k) total of the S corporation rows: nonpassive income
- **Encoded (NonNegDollars):** Add k1s.col_k over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.col_k","op":"sum_over"}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "Report box 1 income (loss) from corporate trade or business activities in which you materially participated in column (i) or (k) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)

## (helper) — `person.k1s_total_nonpassive`

- **Authored helper label:** Nonpassive trade or business income (loss) after basis from Schedules K-1 (Form 1120-S), box 1
- **Encoded (Dollars):** Add k1s.nonpassive over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.nonpassive","op":"sum_over"}`
- Cite: [i1120ssk] p. 5, Effect of determination, "Income (loss), deductions, and credits from an activity are nonpassive if you determine that" (2025; sha256 fb6194da)

## (helper) — `person.k1s_total_p4_income`

- **Authored helper label:** Form 8582 Part IV column (a) total of the S corporation box 2 activities with active participation
- **Encoded (NonNegDollars):** Add k1s.p4_income over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.p4_income","op":"sum_over"}`
- Cite: [i8582] p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities must include the income or loss from those activities in Part IV" (2025; sha256 76787e11)

## (helper) — `person.k1s_total_p4_loss`

- **Authored helper label:** Form 8582 Part IV column (b) total of the S corporation box 2 activities with active participation
- **Encoded (NonNegDollars):** Add k1s.p4_loss over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.p4_loss","op":"sum_over"}`
- Cite: [i8582] p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities must include the income or loss from those activities in Part IV" (2025; sha256 76787e11)

## (helper) — `person.k1s_total_p4_prior`

- **Authored helper label:** Form 8582 Part IV column (c) total of the S corporation box 2 activities with active participation
- **Encoded (NonNegDollars):** Add k1s.p4_prior over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.p4_prior","op":"sum_over"}`
- Cite: [i8582] p. 10, Part IV, "Individuals and qualifying estates who actively participated in rental real estate activities must include the income or loss from those activities in Part IV" (2025; sha256 76787e11)

## (helper) — `person.k1s_total_p5_income`

- **Authored helper label:** Form 8582 Part V column (a) total of the S corporation passive activities
- **Encoded (NonNegDollars):** Add k1s.p5_income over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.p5_income","op":"sum_over"}`
- Cite: [i8582] p. 10, Part V, "Use Part V to figure the amounts to enter on Part I, lines 2a through 2c" (2025; sha256 76787e11)

## (helper) — `person.k1s_total_p5_loss`

- **Authored helper label:** Form 8582 Part V column (b) total of the S corporation passive activities
- **Encoded (NonNegDollars):** Add k1s.p5_loss over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.p5_loss","op":"sum_over"}`
- Cite: [i8582] p. 10, Part V, "Use Part V to figure the amounts to enter on Part I, lines 2a through 2c" (2025; sha256 76787e11)

## (helper) — `person.k1s_total_p5_prior`

- **Authored helper label:** Form 8582 Part V column (c) total of the S corporation passive activities
- **Encoded (NonNegDollars):** Add k1s.p5_prior over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.p5_prior","op":"sum_over"}`
- Cite: [i8582] p. 10, Part V, "Use Part V to figure the amounts to enter on Part I, lines 2a through 2c" (2025; sha256 76787e11)

## (helper) — `person.k1s_total_qbi`

- **Authored helper label:** Qualified business income (loss) from Schedules K-1 (Form 1120-S), box 17, code V, before the passive activity limitation
- **Encoded (Dollars):** Add k1s.qbi over every confirmed k1s entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.qbi","op":"sum_over"}`
- Cite: [i1120ssk] p. 17, Code V. Section 199A information, "The S corporation will provide the information you need to figure your deduction" (2025; sha256 fb6194da)

## (helper) — `person.k1s_count_sche`

- **Authored helper label:** Number of Schedules K-1 (Form 1120-S) with an amount in box 1, 2 or 3 (a row on Schedule E, line 28)
- **Encoded (Count):** Add k1s.one over every confirmed k1s entry for which helper "Box 1, 2 or 3 of this K-1 shows an amount (a row on Schedule E, line 28)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"k1s","field":"k1s.one","op":"sum_over","where":{"eq":["k1s.sche_any",{"const":true}],"op":"test"}}`
- Cite: [i1120ssk] p. 6, Box 1. Ordinary Business Income (Loss), "Report box 1 income (loss) from corporate trade or business activities in which you materially participated in column (i) or (k) of Schedule E (Form 1040), line 28" (2025; sha256 fb6194da)
