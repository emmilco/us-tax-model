# Household facts for dependents and head of household

- Document: `household` (form, tax year 2025)
- Note: Facts about the people on the return that the dependent tests, the credits and the head of household status read; "unmarried" here is the instructions' unmarried or considered unmarried at the end of 2025.

## (helper) — `household.persons`

- **Authored helper label:** Number of people on the return (you, and your spouse if filing jointly)
- **Encoded (Count):** Add person.one over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over"}`
- Cite: [f1040] Form 1040 (2025), page 1, "Your first name and middle initial" and "If joint return, spouse’s first name and middle initial"; p. 1, Filing Status, "Married filing jointly (even if only one had income)" (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `household.taxpayers`

- **Authored helper label:** Number of entries for you
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'taxpayer', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"eq":["person.role",{"const":"taxpayer"}],"op":"test"}}`
- Cite: [f1040] Form 1040 (2025), page 1, "Your first name and middle initial" and "If joint return, spouse’s first name and middle initial"; p. 1, Filing Status, "Married filing jointly (even if only one had income)" (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `household.spouses`

- **Authored helper label:** Number of entries for your spouse
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'spouse', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"eq":["person.role",{"const":"spouse"}],"op":"test"}}`
- Cite: [f1040] Form 1040 (2025), page 1, "Your first name and middle initial" and "If joint return, spouse’s first name and middle initial"; p. 1, Filing Status, "Married filing jointly (even if only one had income)" (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `household.roster_ok`

- **Authored helper label:** One entry for you, and one for your spouse exactly when filing jointly
- **Encoded (Bool):** (f1040 line Filing Status = 'mfj' and helper "Number of entries for you" = 1 (a count) and helper "Number of entries for your spouse" = 1 (a count) or f1040 line Filing Status ≠ 'mfj' and helper "Number of entries for you" = 1 (a count) and helper "Number of entries for your spouse" = 0 (a count))
- **Refusal:** when household.birth_year_bad is true, cannot complete Year of birth not possible. Correct the year of birth. A person on a return for 2025 was born in 2025 or earlier, and a year more than 125 years before 2025 is taken for a mistyped year. Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when household.filer_under16 is true, cannot complete A filer under age 16 at the end of 2025. A return for a person under age 16 at the end of 2025 (you, or your spouse on a joint return) is outside this tool. The archived instructions state no such rule; this is an entry check the owner decided on, recorded in the ambiguity register (amb.2025.filer_under_16). Cite: [i1040gi] p. 66, Self-Select PIN, "You can’t use the Self-Select PIN method if you are a first-time filer under age 16 at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"any":[{"all":[{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},{"eq":["household.taxpayers",{"const":1,"type":"Count"}],"op":"test"},{"eq":["household.spouses",{"const":1,"type":"Count"}],"op":"test"}],"op":"test"},{"all":[{"ne":["f1040.status",{"const":"mfj"}],"op":"test"},{"eq":["household.taxpayers",{"const":1,"type":"Count"}],"op":"test"},{"eq":["household.spouses",{"const":0,"type":"Count"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [f1040] Form 1040 (2025), page 1, "Your first name and middle initial" and "If joint return, spouse’s first name and middle initial"; p. 1, Filing Status, "Married filing jointly (even if only one had income)" (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `household.roster_bad`

- **Authored helper label:** The people entered do not match the filing status
- **Encoded (Bool):** helper "One entry for you, and one for your spouse exactly when filing jointly" = false
- Expr: `{"eq":["household.roster_ok",{"const":false}],"op":"test"}`
- Cite: [f1040] Form 1040 (2025), page 1, "Your first name and middle initial" and "If joint return, spouse’s first name and middle initial"; p. 1, Filing Status, "Married filing jointly (even if only one had income)" (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `household.hsa_people`

- **Authored helper label:** Number of people on the return with a Form 8889
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Number of Forms 8889 entered for this person" > 0 (a count), within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"gt":["person.hsa_forms",{"const":0,"type":"Count"}],"op":"test"}}`
- Cite: [i8889] p. 4, Name and social security number (SSN), "If married filing jointly and both you and your spouse have HSAs, complete a separate Form 8889 for each of you" (2025; sha256 da6f2f58)

## (helper) — `household.hsa_both`

- **Authored helper label:** You and your spouse each have a Form 8889
- **Encoded (Bool):** helper "Number of people on the return with a Form 8889" = 2 (a count)
- Expr: `{"eq":["household.hsa_people",{"const":2,"type":"Count"}],"op":"test"}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, Steps 1 to 3, "Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, use the following rules to figure the amount on line 6", "Step 1. Refigure the contribution limit that would have been entered on line 5 if you had entered on line 3 the total of the worksheet amounts only for the months you were treated as having family coverage", "Step 2. Divide the refigured contribution limit from Step 1 equally between you and your spouse, unless you both agree on a different allocation (such as allocating nothing to one spouse)", "Step 3. Subtract the part of the contribution limit allocated to your spouse in Step 2 from the amount determined in Step 1" (2025; sha256 da6f2f58)

## (helper) — `household.hsa_family_sum`

- **Authored helper label:** Both spouses family amounts for the months each was treated as having family coverage, added together
- **Encoded (NonNegDollars):** Add person.hsa_family over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.hsa_family","op":"sum_over"}`
- Cite: [i8889] p. 7, Line 6, Step 1, "Refigure the contribution limit that would have been entered on line 5 if you had entered on line 3 the total of the worksheet amounts only for the months you were treated as having family coverage"; p969 p. 6, Rules for married people, "Caution: The rules for married people apply only if both spouses are eligible individuals" (2025; sha256 da6f2f58)

## (helper) — `household.hsa_self_sum`

- **Authored helper label:** Both spouses self-only amounts for their eligible months without family coverage, added together
- **Encoded (NonNegDollars):** Add person.hsa_self over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.hsa_self","op":"sum_over"}`
- Cite: [i8889] p. 4, How To Complete Part I, "if you and your spouse are both eligible individuals and either of you has an HDHP with family coverage, you both are treated as having only the family coverage plan"; p. 7, Line 6, Step 4, "Determine any other contribution limits that apply for the tax year" (2025; sha256 da6f2f58)

## (helper) — `household.hsa_agreed_count`

- **Authored helper label:** Number of Forms 8889 using an agreed allocation
- **Encoded (Count):** Add person.hsa_agreed over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.hsa_agreed","op":"sum_over"}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, Steps 1 to 3, "Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, use the following rules to figure the amount on line 6", "Step 1. Refigure the contribution limit that would have been entered on line 5 if you had entered on line 3 the total of the worksheet amounts only for the months you were treated as having family coverage", "Step 2. Divide the refigured contribution limit from Step 1 equally between you and your spouse, unless you both agree on a different allocation (such as allocating nothing to one spouse)", "Step 3. Subtract the part of the contribution limit allocated to your spouse in Step 2 from the amount determined in Step 1" (2025; sha256 da6f2f58)

## (helper) — `household.hsa_step1_sum`

- **Authored helper label:** Both spouses Step 1 limits added together
- **Encoded (NonNegDollars):** Add person.hsa_step1 over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.hsa_step1","op":"sum_over"}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, Steps 1 to 3, "Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, use the following rules to figure the amount on line 6", "Step 1. Refigure the contribution limit that would have been entered on line 5 if you had entered on line 3 the total of the worksheet amounts only for the months you were treated as having family coverage", "Step 2. Divide the refigured contribution limit from Step 1 equally between you and your spouse, unless you both agree on a different allocation (such as allocating nothing to one spouse)", "Step 3. Subtract the part of the contribution limit allocated to your spouse in Step 2 from the amount determined in Step 1" (2025; sha256 da6f2f58)

## (helper) — `household.hsa_share_sum`

- **Authored helper label:** Both spouses parts of the Step 1 limit added together
- **Encoded (NonNegDollars):** Add person.hsa_share over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.hsa_share","op":"sum_over"}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, Steps 1 to 3, "Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, use the following rules to figure the amount on line 6", "Step 1. Refigure the contribution limit that would have been entered on line 5 if you had entered on line 3 the total of the worksheet amounts only for the months you were treated as having family coverage", "Step 2. Divide the refigured contribution limit from Step 1 equally between you and your spouse, unless you both agree on a different allocation (such as allocating nothing to one spouse)", "Step 3. Subtract the part of the contribution limit allocated to your spouse in Step 2 from the amount determined in Step 1" (2025; sha256 da6f2f58)

## (helper) — `household.work_ssn_count`

- **Authored helper label:** Number of people on the return with an SSN valid for employment
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Do you have an SSN valid for employment issued before the due date of your return?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"eq":["person.work_ssn",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 17, Before you begin, and p. 40, Step 1, question 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.any_work_ssn`

- **Authored helper label:** You, or your spouse if filing jointly, have an SSN valid for employment
- **Encoded (Bool):** helper "Number of people on the return with an SSN valid for employment" > 0 (a count)
- Expr: `{"gt":["household.work_ssn_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 17, Before you begin, "If you are filing a joint return, only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.eic_ssn_count`

- **Authored helper label:** Number of people on the return with an SSN valid for the EIC
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Do you have an SSN valid for the EIC, issued on or before the due date of your return?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"eq":["person.eic_ssn",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 40, Step 1, question 2; p. 44, Social security number (SSN), "For the EIC, a valid SSN is a number issued by the Social Security Administration unless “Not Valid for Employment” is printed on the social security card and the number was issued solely to allow the recipient of the SSN to apply for or receive a federally funded benefit" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.all_eic_ssn`

- **Authored helper label:** You, and your spouse if filing jointly, have SSNs valid for the EIC
- **Encoded (Bool):** helper "Number of people on the return with an SSN valid for the EIC" = helper "Number of people on the return (you, and your spouse if filing jointly)"
- Expr: `{"eq":["household.eic_ssn_count","household.persons"],"op":"test"}`
- Cite: [i1040gi] p. 40, Step 1, question 2, "Do you, and your spouse if filing a joint return, have a social security number ... that allows you to work and is valid for EIC purposes"; p. 44, Social security number (SSN), "For the EIC, a valid SSN is a number issued by the Social Security Administration unless “Not Valid for Employment” is printed on the social security card and the number was issued solely to allow the recipient of the SSN to apply for or receive a federally funded benefit" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.birth_year_bad_count`

- **Authored helper label:** Number of people on the return whose year of birth entered is not possible (person.birth_year_bad)
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "The year of birth entered is after the tax year, or more than 125 years before it" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"eq":["person.birth_year_bad",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `household.birth_year_bad`

- **Authored helper label:** A year of birth entered for you, or your spouse on a joint return, is after the tax year or more than 125 years before it
- **Encoded (Bool):** helper "Number of people on the return whose year of birth entered is not possible (person.birth_year_bad)" > 0 (a count)
- Expr: `{"gt":["household.birth_year_bad_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 33, Line 12d, "If you or your spouse (if you are married and filing a joint return) were born before January 2, 1961, or were blind at the end of 2025, check the appropriate box(es)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.under16_count`

- **Authored helper label:** Number of people on the return under age 16 at the end of 2025
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Under age 16 at the end of 2025" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"eq":["person.under16",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 66, Self-Select PIN, "You can’t use the Self-Select PIN method if you are a first-time filer under age 16 at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `household.filer_under16`

- **Authored helper label:** You, or your spouse if filing jointly, were under age 16 at the end of 2025
- **Encoded (Bool):** helper "Number of people on the return under age 16 at the end of 2025" > 0 (a count)
- Interpretation: amb.2025.filer_under_16
- Expr: `{"gt":["household.under16_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 66, Self-Select PIN, "You can’t use the Self-Select PIN method if you are a first-time filer under age 16 at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.tin_count`

- **Authored helper label:** Number of people on the return with an SSN or ITIN, or who have applied for an ITIN
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "An SSN or ITIN, or applied for an ITIN" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"eq":["person.tin_or_itin_applied",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 17, Before you begin, "If you want to claim the credit for other dependents, you, and your spouse if filing jointly, must have either an SSN or ITIN"; p. 19, Step 5, question 1, "(Answer 'Yes' if you are applying for an ITIN on or before the return due date (including extensions).)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.all_tin`

- **Authored helper label:** You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
- **Encoded (Bool):** helper "Number of people on the return with an SSN or ITIN, or who have applied for an ITIN" = helper "Number of people on the return (you, and your spouse if filing jointly)"
- Expr: `{"eq":["household.tin_count","household.persons"],"op":"test"}`
- Cite: [i1040gi] p. 17, Before you begin, "If you want to claim the credit for other dependents, you, and your spouse if filing jointly, must have either an SSN or ITIN" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.id_count`

- **Authored helper label:** Number of people on the return with an SSN valid for employment or an SSN or ITIN
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "An SSN valid for employment, or an SSN or ITIN" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Interpretation: amb.2025.ctc_spouse_itin_application
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"eq":["person.work_ssn_or_tin",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 17, Before you begin, "The other spouse must have either an SSN or ITIN" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.ctc_ssn`

- **Authored helper label:** Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid for employment, and each other person on the return has an SSN or ITIN
- **Encoded (Bool):** helper "You, or your spouse if filing jointly, have an SSN valid for employment" = true and helper "Number of people on the return with an SSN valid for employment or an SSN or ITIN" = helper "Number of people on the return (you, and your spouse if filing jointly)"
- Expr: `{"all":[{"eq":["household.any_work_ssn",{"const":true}],"op":"test"},{"eq":["household.id_count","household.persons"],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 17, Before you begin, "If you are filing a joint return, only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC. The other spouse must have either an SSN or ITIN" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.taxpayer_work_ssn_count`

- **Authored helper label:** Your entry, if the answer is yes
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'taxpayer' and helper "Do you have an SSN valid for employment issued before the due date of your return?" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"all":[{"eq":["person.role",{"const":"taxpayer"}],"op":"test"},{"eq":["person.work_ssn",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "You have a valid social security number (SSN)"; p. 104, Valid SSN for No Tax on Tips, "A valid SSN for purposes of the deduction for qualified tips is one that is valid for employment and that is issued by the Social Security Administration (SSA) before the due date of your 2025 return (including extensions)"; p. 108, Valid SSN, "A valid SSN for purposes of the deduction for qualified overtime compensation is one that is valid for employment"; p. 110, Valid SSN, "A valid SSN for purposes of the enhanced deduction for seniors is one that is valid for employment" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.taxpayer_work_ssn`

- **Authored helper label:** Do you have an SSN valid for employment issued before the due date of your return?
- **Encoded (Bool):** helper "Your entry, if the answer is yes" > 0 (a count)
- Expr: `{"gt":["household.taxpayer_work_ssn_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 101, Schedule 1-A, Part II, "You have a valid social security number (SSN)"; p. 104, Valid SSN for No Tax on Tips, "A valid SSN for purposes of the deduction for qualified tips is one that is valid for employment and that is issued by the Social Security Administration (SSA) before the due date of your 2025 return (including extensions)"; p. 108, Valid SSN, "A valid SSN for purposes of the deduction for qualified overtime compensation is one that is valid for employment"; p. 110, Valid SSN, "A valid SSN for purposes of the enhanced deduction for seniors is one that is valid for employment" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.home_cost`

- **Authored helper label:** Did you pay over half the cost of keeping up your home for 2025?
- **Encoded (Bool):** Input — Did you pay over half the cost of keeping up your home for 2025? Cost of keeping up a home includes expenses such as rent, mortgage interest, real estate taxes, insurance on the home, repairs, utilities, and food eaten in the home. It does not include the cost of clothing, education, medical treatment, vacations, life insurance, or transportation, or the value of your services or those of a member of your household. Amounts paid out of funds received in the name of a person who lives in the home, such as their Social Security, count as paid by that person, not you. TANF or similar payments you received and used for the home count as paid by you.
- Expr: `{"op":"input","source":"Did you pay over half the cost of keeping up your home for 2025? Cost of keeping up a home includes expenses such as rent, mortgage interest, real estate taxes, insurance on the home, repairs, utilities, and food eaten in the home. It does not include the cost of clothing, education, medical treatment, vacations, life insurance, or transportation, or the value of your services or those of a member of your household. Amounts paid out of funds received in the name of a person who lives in the home, such as their Social Security, count as paid by that person, not you. TANF or similar payments you received and used for the home count as paid by you."}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2; p. 15, "Keeping up a home. To find out what is included in the cost of keeping up a home, see Pub. 501."; p501 p. 9, Keeping Up a Home, "Costs you include. Include in the cost of keeping up a home expenses such as rent, mortgage interest, real estate taxes, insurance on the home, repairs, utilities, and food eaten in the home." p501 p. 9, "Costs you don’t include. Don’t include the cost of clothing, education, medical treatment, vacations, life insurance, or transportation. Also don’t include the value of your services or those of a member of your household." p501 p. 9, Note, "Amounts paid out of funds received in the child’s or qualifying person’s name, such as Social Security, are considered paid by the child, not you."; p501 p. 9, Note, "if you received Temporary Assistance to Needy Families (TANF) payments or other similar payments and used the payment to support another person, those payments are considered support you provided for that person" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.considered_unmarried`

- **Authored helper label:** Married at the end of 2025 but considered unmarried under the head of household rules
- **Encoded (Bool):** Input — Although you were married at the end of 2025, are you considered unmarried for head of household?

  You are considered unmarried if either of these applies (if your spouse died in 2025, you are considered married for the whole year: answer No).

  - You lived apart from your spouse for the last 6 months of 2025, and all of these apply:
    - you file a separate return from your spouse
    - you paid over half the cost of keeping up your home for 2025
    - your home was the main home of your child, stepchild or foster child for more than half of 2025 (temporary absences by you or the child for special circumstances count as time lived in the home; a child born or who died in 2025 meets this if the child lived with you for more than half the part of the year the child was alive; a child adopted, lawfully placed with you for legal adoption or placed as an eligible foster child in 2025 meets it if your main home was the child's main home for more than half the time since)
    - you can claim this child as your dependent, or could except that the child's other parent can claim the child under the rule for children of divorced or separated parents
  - Your spouse was a nonresident alien at any time during 2025 and no election to treat your spouse as a resident alien is in effect for 2025 (an election made for an earlier year remains in effect until terminated).

  Your spouse counts as living in your home during a temporary absence for special circumstances, such as business, medical care, school or military service, if it was reasonable to assume your spouse would return and you kept up the home during the absence.
- Expr: `{"op":"input","source":"Although you were married at the end of 2025, are you considered unmarried for head of household?\n\nYou are considered unmarried if either of these applies (if your spouse died in 2025, you are considered married for the whole year: answer No).\n\n- You lived apart from your spouse for the last 6 months of 2025, and all of these apply:\n  - you file a separate return from your spouse\n  - you paid over half the cost of keeping up your home for 2025\n  - your home was the main home of your child, stepchild or foster child for more than half of 2025 (temporary absences by you or the child for special circumstances count as time lived in the home; a child born or who died in 2025 meets this if the child lived with you for more than half the part of the year the child was alive; a child adopted, lawfully placed with you for legal adoption or placed as an eligible foster child in 2025 meets it if your main home was the child's main home for more than half the time since)\n  - you can claim this child as your dependent, or could except that the child's other parent can claim the child under the rule for children of divorced or separated parents\n- Your spouse was a nonresident alien at any time during 2025 and no election to treat your spouse as a resident alien is in effect for 2025 (an election made for an earlier year remains in effect until terminated).\n\nYour spouse counts as living in your home during a temporary absence for special circumstances, such as business, medical care, school or military service, if it was reasonable to assume your spouse would return and you kept up the home during the absence."}`
- Cite: [i1040gi] p. 14, Head of Household, "You are considered unmarried for this purpose if any of the following applies" through "the election to treat the alien spouse as a resident alien is not made"; p. 15, Married persons who live apart, "Even if you weren’t divorced or legally separated at the end of 2025, you are considered unmarried if all of the following apply" through "under the rule for Children of divorced or separated parents"; p. 14, Exception to time lived with you, "Temporary absences by you or the other person for special circumstances"; p. 15, Exception to time lived with you, "If the person is your qualifying child, the child must have lived with you for more than half the part of the year the child was alive" through "for more than half the time since the person was adopted or placed with you in 2025"; p501 p. 6, Spouse died during the year, "If your spouse died during the year, you are considered married for the whole year for filing status purposes."; p501 p. 8, Considered Unmarried, "Your spouse is considered to live in your home even if your spouse is temporarily absent due to special circumstances. See Temporary absences, later."; p501 p. 9, Temporary absences, "It must be reasonable to assume the absent person will return to the home after the temporary absence. You must continue to keep up the home during the absence."; i1040gi p. 13, Nonresident aliens and dual-status aliens, "This choice remains in effect in subsequent years until terminated" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.considered_unmarried_if_married`

- **Authored helper label:** Considered unmarried under the head of household rules, asked only of a person married at the end of 2025 (false otherwise)
- **Encoded (Bool):** Choose — [helper "Married at the end of 2025 (false for a person filing as single or head of household who has never been married)" = true → helper "Married at the end of 2025 but considered unmarried under the head of household rules"] [helper "Married at the end of 2025 (false for a person filing as single or head of household who has never been married)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.married",{"const":true}],"op":"test"},"then":"household.considered_unmarried"},{"guard":{"eq":["household.married",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 14, Head of Household, "You are considered unmarried for this purpose if any of the following applies" through "the election to treat the alien spouse as a resident alien is not made"; p. 15, Married persons who live apart, "Even if you weren’t divorced or legally separated at the end of 2025, you are considered unmarried if all of the following apply" through "under the rule for Children of divorced or separated parents"; p. 14, Exception to time lived with you, "Temporary absences by you or the other person for special circumstances"; p. 15, Exception to time lived with you, "If the person is your qualifying child, the child must have lived with you for more than half the part of the year the child was alive" through "for more than half the time since the person was adopted or placed with you in 2025"; p501 p. 6, Spouse died during the year, "If your spouse died during the year, you are considered married for the whole year for filing status purposes."; p501 p. 8, Considered Unmarried, "Your spouse is considered to live in your home even if your spouse is temporarily absent due to special circumstances. See Temporary absences, later."; p501 p. 9, Temporary absences, "It must be reasonable to assume the absent person will return to the home after the temporary absence. You must continue to keep up the home during the absence." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.not_married`

- **Authored helper label:** Not married at the end of 2025
- **Encoded (Bool):** helper "Married at the end of 2025 (false for a person filing as single or head of household who has never been married)" = false
- Expr: `{"eq":["household.married",{"const":false}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, "You are considered unmarried for this purpose if any of the following applies" through "the election to treat the alien spouse as a resident alien is not made"; p. 15, Married persons who live apart, "Even if you weren’t divorced or legally separated at the end of 2025, you are considered unmarried if all of the following apply" through "under the rule for Children of divorced or separated parents"; p. 14, Exception to time lived with you, "Temporary absences by you or the other person for special circumstances"; p. 15, Exception to time lived with you, "If the person is your qualifying child, the child must have lived with you for more than half the part of the year the child was alive" through "for more than half the time since the person was adopted or placed with you in 2025"; p501 p. 6, Spouse died during the year, "If your spouse died during the year, you are considered married for the whole year for filing status purposes."; p501 p. 8, Considered Unmarried, "Your spouse is considered to live in your home even if your spouse is temporarily absent due to special circumstances. See Temporary absences, later."; p501 p. 9, Temporary absences, "It must be reasonable to assume the absent person will return to the home after the temporary absence. You must continue to keep up the home during the absence." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.unmarried`

- **Authored helper label:** Unmarried, or considered unmarried under the head of household rules, at the end of 2025
- **Encoded (Bool):** (helper "Not married at the end of 2025" = true or helper "Considered unmarried under the head of household rules, asked only of a person married at the end of 2025 (false otherwise)" = true)
- Expr: `{"any":[{"eq":["household.not_married",{"const":true}],"op":"test"},{"eq":["household.considered_unmarried_if_married",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, "You are considered unmarried for this purpose if any of the following applies" through "the election to treat the alien spouse as a resident alien is not made"; p. 15, Married persons who live apart, "Even if you weren’t divorced or legally separated at the end of 2025, you are considered unmarried if all of the following apply" through "under the rule for Children of divorced or separated parents"; p. 14, Exception to time lived with you, "Temporary absences by you or the other person for special circumstances"; p. 15, Exception to time lived with you, "If the person is your qualifying child, the child must have lived with you for more than half the part of the year the child was alive" through "for more than half the time since the person was adopted or placed with you in 2025"; p501 p. 6, Spouse died during the year, "If your spouse died during the year, you are considered married for the whole year for filing status purposes."; p501 p. 8, Considered Unmarried, "Your spouse is considered to live in your home even if your spouse is temporarily absent due to special circumstances. See Temporary absences, later."; p501 p. 9, Temporary absences, "It must be reasonable to assume the absent person will return to the home after the temporary absence. You must continue to keep up the home during the absence." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.ever_married`

- **Authored helper label:** Have you ever been married?
- **Encoded (Bool):** Input — Have you ever been married? (Asked when your filing status is single or head of household. A common law marriage recognized in the state where you now live or where it began is a marriage; a registered domestic partnership, civil union or similar relationship not denominated as a marriage is not.)
- Expr: `{"op":"input","source":"Have you ever been married? (Asked when your filing status is single or head of household. A common law marriage recognized in the state where you now live or where it began is a marriage; a registered domestic partnership, civil union or similar relationship not denominated as a marriage is not.)"}`
- Cite: [i1040gi] p. 13, Filing Status, Single, "You were never married" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.status_states_marriage`

- **Authored helper label:** The filing status is one only a person who is or was married takes (married filing jointly, married filing separately or qualifying surviving spouse)
- **Encoded (Bool):** (f1040 line Filing Status = 'mfj' or f1040 line Filing Status = 'mfs' or f1040 line Filing Status = 'qss')
- Expr: `{"any":[{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},{"eq":["f1040.status",{"const":"qss"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 13, Filing Status, Single, "You were never married" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.marriage_possible`

- **Authored helper label:** A marriage is possible: the filing status states one, or a person filing as single or head of household has been married at some time
- **Encoded (Bool):** Choose — [f1040 line Filing Status = 'single' → helper "Have you ever been married?"] [f1040 line Filing Status = 'mfj' → helper "The filing status is one only a person who is or was married takes (married filing jointly, married filing separately or qualifying surviving spouse)"] [f1040 line Filing Status = 'mfs' → helper "The filing status is one only a person who is or was married takes (married filing jointly, married filing separately or qualifying surviving spouse)"] [f1040 line Filing Status = 'hoh' → helper "Have you ever been married?"] [f1040 line Filing Status = 'qss' → helper "The filing status is one only a person who is or was married takes (married filing jointly, married filing separately or qualifying surviving spouse)"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"household.ever_married"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"household.status_states_marriage"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"household.status_states_marriage"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"household.ever_married"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"household.status_states_marriage"}],"op":"choose"}`
- Cite: [i1040gi] p. 13, Filing Status, Single, "You were never married" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.married_dec31`

- **Authored helper label:** Were you married at the end of 2025?
- **Encoded (Bool):** Input — Were you married at the end of 2025 (including married but considered unmarried for head of household status)?

  Use the marriage recognized under the law of the state or territory where it was entered into; a marriage entered into under foreign or American Indian tribal law counts if at least one U.S. state or territory would recognize it as a marriage.

  Include a common law marriage recognized in the state where you now live or where it began.

  Living apart does not end a marriage; an interlocutory (not final) divorce decree still means married.

  Answer No if, by December 31, you were divorced under a final decree, legally separated under a decree of divorce or separate maintenance, or had a court decree of annulment holding that no valid marriage ever existed.

  A registered domestic partnership, civil union or similar relationship not denominated as a marriage is not a marriage for federal tax purposes.

  This question asks whether you were married at year end; the separate filing-status rules for a spouse who died during 2025 are addressed separately.

  When choosing your filing status, also note: if you divorced solely to file as unmarried, intending at the time to remarry each other in the next tax year, and actually do so, you must file as married in both years.
- Expr: `{"op":"input","source":"Were you married at the end of 2025 (including married but considered unmarried for head of household status)?\n\nUse the marriage recognized under the law of the state or territory where it was entered into; a marriage entered into under foreign or American Indian tribal law counts if at least one U.S. state or territory would recognize it as a marriage.\n\nInclude a common law marriage recognized in the state where you now live or where it began.\n\nLiving apart does not end a marriage; an interlocutory (not final) divorce decree still means married.\n\nAnswer No if, by December 31, you were divorced under a final decree, legally separated under a decree of divorce or separate maintenance, or had a court decree of annulment holding that no valid marriage ever existed.\n\nA registered domestic partnership, civil union or similar relationship not denominated as a marriage is not a marriage for federal tax purposes.\n\nThis question asks whether you were married at year end; the separate filing-status rules for a spouse who died during 2025 are addressed separately.\n\nWhen choosing your filing status, also note: if you divorced solely to file as unmarried, intending at the time to remarry each other in the next tax year, and actually do so, you must file as married in both years."}`
- Cite: [i1040gi] p. 41, Step 3, question 3, and Step 4, question 1, "Are you a married taxpayer whose filing status is married filing separately or head of household?"; i8889 p. 4, Line 3, rule 6, "If, at the end of 2025, you were age 55 or older and unmarried or married with self-only HDHP coverage for the entire year"; p501 p. 6, Marital Status, "State law governs whether you are married or legally separated under a divorce or separate maintenance decree."; p501 p. 6, Definition of marriage, "Individuals who have entered into a registered domestic partnership, civil union, or other similar relationship"; p501 p. 6, Considered married, "You are living together in a common law marriage recognized in the state where you now live or in the state where the common law marriage began."; p501 p. 6, Divorce and remarriage, "you and your spouse must file as married individuals in both years."; p501 p. 6, Annulled marriages, "you are considered unmarried even if you filed joint returns for earlier years." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.married`

- **Authored helper label:** Married at the end of 2025 (false for a person filing as single or head of household who has never been married)
- **Encoded (Bool):** Choose — [helper "A marriage is possible: the filing status states one, or a person filing as single or head of household has been married at some time" = true → helper "Were you married at the end of 2025?"] [helper "A marriage is possible: the filing status states one, or a person filing as single or head of household has been married at some time" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.marriage_possible",{"const":true}],"op":"test"},"then":"household.married_dec31"},{"guard":{"eq":["household.marriage_possible",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 41, Step 3, question 3, and Step 4, question 1, "Are you a married taxpayer whose filing status is married filing separately or head of household?"; i8889 p. 4, Line 3, rule 6, "If, at the end of 2025, you were age 55 or older and unmarried or married with self-only HDHP coverage for the entire year"; p501 p. 6, Marital Status, "State law governs whether you are married or legally separated under a divorce or separate maintenance decree."; p501 p. 6, Definition of marriage, "Individuals who have entered into a registered domestic partnership, civil union, or other similar relationship"; p501 p. 6, Considered married, "You are living together in a common law marriage recognized in the state where you now live or in the state where the common law marriage began."; p501 p. 6, Divorce and remarriage, "you and your spouse must file as married individuals in both years."; p501 p. 6, Annulled marriages, "you are considered unmarried even if you filed joint returns for earlier years." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.community_property`

- **Authored helper label:** Did you live in, or have your permanent home (domicile) in, a community property state at any time in 2025?
- **Encoded (Bool):** Input — Did you live in, or have your permanent home (domicile) in, a community property state (Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington or Wisconsin) at any time in 2025?
- Expr: `{"op":"input","source":"Did you live in, or have your permanent home (domicile) in, a community property state (Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington or Wisconsin) at any time in 2025?"}`
- Cite: [i1040gi] p. 23, Community Property States, "Community property states include Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington, and Wisconsin"; p555 p. 2, Domicile, "The law of the state, or the law of the foreign country, where you are domiciled will determine if you have community property, community income, or both"; p555 p. 3, Domicile, "you intend to use for an indefinite or unlimited period, and to which, when absent, you intend to return" and "When this publication refers to where you live, it means your domicile." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.spouse_cp_domicile`

- **Authored helper label:** At some time in 2025 while married, the husband or wife lived in, or had a permanent home (domicile) in, a community property state
- **Encoded (Bool):** Input — At any time in 2025 while you were married, did your husband or wife live in, or have their permanent home (domicile) in, a community property state (Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington or Wisconsin)? (Asked when you are not filing jointly, a marriage is possible, and you did not live or have your permanent home in one of those states yourself.)
- Expr: `{"op":"input","source":"At any time in 2025 while you were married, did your husband or wife live in, or have their permanent home (domicile) in, a community property state (Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington or Wisconsin)? (Asked when you are not filing jointly, a marriage is possible, and you did not live or have your permanent home in one of those states yourself.)"}`
- Cite: [p555] p. 2, Domicile, "If you and your spouse (or your RDP) have different domiciles, check the laws of each to see if you have community property, community income, or both"; p. 6, Military retirement pay, "Active military pay earned while married and domiciled in a community property state is also community income" (Rev. December 2024 (Publication 555 (Rev. 12-2024), Catalog Number 15103C, Feb 18, 2025); current irs-pdf edition, not year-specific; sha256 7a1e1f3a)

## (helper) — `household.ask_spouse_cp_domicile`

- **Authored helper label:** A marriage is possible and the filing status is not qualifying surviving spouse
- **Encoded (Bool):** helper "A marriage is possible: the filing status states one, or a person filing as single or head of household has been married at some time" = true and f1040 line Filing Status ≠ 'qss'
- Expr: `{"all":[{"eq":["household.marriage_possible",{"const":true}],"op":"test"},{"ne":["f1040.status",{"const":"qss"}],"op":"test"}],"op":"test"}`
- Cite: [p555] p. 2, Domicile, "If you and your spouse (or your RDP) have different domiciles, check the laws of each to see if you have community property, community income, or both" (Rev. December 2024 (Publication 555 (Rev. 12-2024), Catalog Number 15103C, Feb 18, 2025); current irs-pdf edition, not year-specific; sha256 7a1e1f3a)

## (helper) — `household.spouse_cp_domicile_if_asked`

- **Authored helper label:** The husband or wife lived in, or had a permanent home in, a community property state in 2025, asked only where a marriage is possible and the filing status is not qualifying surviving spouse (false otherwise)
- **Encoded (Bool):** Choose — [helper "A marriage is possible and the filing status is not qualifying surviving spouse" = true → helper "At some time in 2025 while married, the husband or wife lived in, or had a permanent home (domicile) in, a community property state"] [helper "A marriage is possible and the filing status is not qualifying surviving spouse" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.ask_spouse_cp_domicile",{"const":true}],"op":"test"},"then":"household.spouse_cp_domicile"},{"guard":{"eq":["household.ask_spouse_cp_domicile",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [p555] p. 2, Domicile, "If you and your spouse (or your RDP) have different domiciles, check the laws of each to see if you have community property, community income, or both" (Rev. December 2024 (Publication 555 (Rev. 12-2024), Catalog Number 15103C, Feb 18, 2025); current irs-pdf edition, not year-specific; sha256 7a1e1f3a)

## (helper) — `household.cp_retirement`

- **Authored helper label:** In 2025, either spouse received a pension, annuity or military retirement pay earned while the two were married and living in a community property state
- **Encoded (Bool):** Input — In 2025, did you or your husband or wife receive a pension, annuity or military retirement pay earned while the two of you were married and either of you lived or had your permanent home in a community property state (Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington or Wisconsin)?
- Expr: `{"op":"input","source":"In 2025, did you or your husband or wife receive a pension, annuity or military retirement pay earned while the two of you were married and either of you lived or had your permanent home in a community property state (Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington or Wisconsin)?"}`
- Cite: [p555] p. 5, Pensions, "distributions from pensions will be characterized as community or separate income depending on the respective periods of participation in the pension while married (or during the registered domestic partnership) and domiciled in a community property state"; p. 6, Civil service retirement, "Even if you now live in a noncommunity property state and you receive a civil service annuity, it may be community income if it is based on services you performed while married (or during the registered domestic partnership) and domiciled in a community property state"; p. 6, Military retirement pay, "military retirement pay for services performed during marriage and domicile in a community property state is community income" (Rev. December 2024 (Publication 555 (Rev. 12-2024), Catalog Number 15103C, Feb 18, 2025); current irs-pdf edition, not year-specific; sha256 7a1e1f3a)

## (helper) — `household.cp_retirement_if_asked`

- **Authored helper label:** Retirement pay earned while married and living in a community property state, asked only where a marriage is possible and the filing status is not qualifying surviving spouse (false otherwise)
- **Encoded (Bool):** Choose — [helper "A marriage is possible and the filing status is not qualifying surviving spouse" = true → helper "In 2025, either spouse received a pension, annuity or military retirement pay earned while the two were married and living in a community property state"] [helper "A marriage is possible and the filing status is not qualifying surviving spouse" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.ask_spouse_cp_domicile",{"const":true}],"op":"test"},"then":"household.cp_retirement"},{"guard":{"eq":["household.ask_spouse_cp_domicile",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [p555] p. 6, Civil service retirement, "Even if you now live in a noncommunity property state and you receive a civil service annuity, it may be community income" (Rev. December 2024 (Publication 555 (Rev. 12-2024), Catalog Number 15103C, Feb 18, 2025); current irs-pdf edition, not year-specific; sha256 7a1e1f3a)

## (helper) — `household.cp_spouse_or_retirement`

- **Authored helper label:** Your husband or wife lived in, or had a permanent home in, a community property state in 2025, or (asked when neither of you did) retirement pay was earned while married and living in one
- **Encoded (Bool):** Choose — [helper "The husband or wife lived in, or had a permanent home in, a community property state in 2025, asked only where a marriage is possible and the filing status is not qualifying surviving spouse (false otherwise)" = true → helper "The husband or wife lived in, or had a permanent home in, a community property state in 2025, asked only where a marriage is possible and the filing status is not qualifying surviving spouse (false otherwise)"] [helper "The husband or wife lived in, or had a permanent home in, a community property state in 2025, asked only where a marriage is possible and the filing status is not qualifying surviving spouse (false otherwise)" = false → helper "Retirement pay earned while married and living in a community property state, asked only where a marriage is possible and the filing status is not qualifying surviving spouse (false otherwise)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.spouse_cp_domicile_if_asked",{"const":true}],"op":"test"},"then":"household.spouse_cp_domicile_if_asked"},{"guard":{"eq":["household.spouse_cp_domicile_if_asked",{"const":false}],"op":"test"},"then":"household.cp_retirement_if_asked"}],"op":"choose"}`
- Cite: [p555] p. 2, Domicile, "If you and your spouse (or your RDP) have different domiciles, check the laws of each to see if you have community property, community income, or both"; p. 6, Civil service retirement, "Even if you now live in a noncommunity property state and you receive a civil service annuity, it may be community income" (Rev. December 2024 (Publication 555 (Rev. 12-2024), Catalog Number 15103C, Feb 18, 2025); current irs-pdf edition, not year-specific; sha256 7a1e1f3a)

## (helper) — `household.cp_any`

- **Authored helper label:** You lived in, or had your permanent home in, a community property state in 2025, or (asked when you did not) your husband or wife did, or (asked when neither did) retirement pay received in 2025 was earned while married and living in one
- **Encoded (Bool):** Choose — [helper "Did you live in, or have your permanent home (domicile) in, a community property state at any time in 2025?" = true → helper "Did you live in, or have your permanent home (domicile) in, a community property state at any time in 2025?"] [helper "Did you live in, or have your permanent home (domicile) in, a community property state at any time in 2025?" = false → helper "Your husband or wife lived in, or had a permanent home in, a community property state in 2025, or (asked when neither of you did) retirement pay was earned while married and living in one"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.community_property",{"const":true}],"op":"test"},"then":"household.community_property"},{"guard":{"eq":["household.community_property",{"const":false}],"op":"test"},"then":"household.cp_spouse_or_retirement"}],"op":"choose"}`
- Cite: [p555] p. 2, Domicile, "The law of the state, or the law of the foreign country, where you are domiciled will determine if you have community property, community income, or both. If you and your spouse (or your RDP) have different domiciles, check the laws of each"; p. 6, Civil service retirement, "Even if you now live in a noncommunity property state and you receive a civil service annuity, it may be community income if it is based on services you performed while married (or during the registered domestic partnership) and domiciled in a community property state" (Rev. December 2024 (Publication 555 (Rev. 12-2024), Catalog Number 15103C, Feb 18, 2025); current irs-pdf edition, not year-specific; sha256 7a1e1f3a)

## (helper) — `household.hoh_cp_married`

- **Authored helper label:** Filing as head of household: married at the end of 2025, and you or your husband or wife lived in, or had a permanent home in, a community property state
- **Encoded (Bool):** Choose — [helper "Married at the end of 2025 (false for a person filing as single or head of household who has never been married)" = true → helper "You lived in, or had your permanent home in, a community property state in 2025, or (asked when you did not) your husband or wife did, or (asked when neither did) retirement pay received in 2025 was earned while married and living in one"] [helper "Married at the end of 2025 (false for a person filing as single or head of household who has never been married)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.married",{"const":true}],"op":"test"},"then":"household.cp_any"},{"guard":{"eq":["household.married",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 23, Community Property States, "If you and your spouse lived in a community property state, you must usually follow state law to determine what is community income and what is separate income" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `household.hoh_community_property`

- **Authored helper label:** Married, filing as head of household, and living in a community property state
- **Encoded (Bool):** Choose — [f1040 line Filing Status = 'single' → helper "Year parameter household.no (false)"] [f1040 line Filing Status = 'mfj' → helper "Year parameter household.no (false)"] [f1040 line Filing Status = 'mfs' → helper "Year parameter household.no (false)"] [f1040 line Filing Status = 'hoh' → helper "Filing as head of household: married at the end of 2025, and you or your husband or wife lived in, or had a permanent home in, a community property state"] [f1040 line Filing Status = 'qss' → helper "Year parameter household.no (false)"]
- Interpretation: amb.2025.hoh_community_property
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"household.no"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"household.no"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"household.no"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"household.hoh_cp_married"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 23, Community Property States, "If you and your spouse lived in a community property state, you must usually follow state law to determine what is community income and what is separate income" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.credit_disallowed`

- **Authored helper label:** Was your (or, on a joint return, your spouse's) EIC for a year after 1996, or child tax credit, additional child tax credit or credit for other dependents for a year after 2015, reduced or disallowed other than for a math or clerical error, or are you (or, on a joint return, your spouse) in a 2- or 10-year disallowance period?
- **Encoded (Bool):** Input — Was your (or, on a joint return, your spouse's) earned income credit for any year after 1996, or child tax credit, additional child tax credit or credit for other dependents for any year after 2015, reduced or disallowed for any reason other than a math or clerical error, or are you (or, on a joint return, your spouse) in a 2- or 10-year period during which one of these credits can't be taken because an earlier claim was found to be reckless, intentional or fraudulent?
- Expr: `{"op":"input","source":"Was your (or, on a joint return, your spouse's) earned income credit for any year after 1996, or child tax credit, additional child tax credit or credit for other dependents for any year after 2015, reduced or disallowed for any reason other than a math or clerical error, or are you (or, on a joint return, your spouse) in a 2- or 10-year period during which one of these credits can't be taken because an earlier claim was found to be reckless, intentional or fraudulent?"}`
- Cite: [i1040gi] p. 43, Form 8862, who must file, "You must file Form 8862 if your EIC for a year after 1996 was reduced or disallowed for any reason other than a math or clerical error" and "don’t file Form 8862 or take the credit for the ... 2 years after the most recent tax year for which there was a final determination that your EIC claim was due to reckless or intentional disregard of the EIC rules ... 10 years after the most recent tax year for which there was a final determination that your EIC claim was due to fraud"; p. 39, Form 8862, who must file, "You must file Form 8862 to claim the child tax credit or credit for other dependents if your child tax credit (refundable or nonrefundable depending on the tax year), additional child tax credit, or credit for other dependents for a year after 2015 was denied or reduced for any reason other than a math or clerical error"; i1040s8812 p. 2, Form 8862 may be required, "If your CTC, ACTC, or ODC for a year after 2015 was denied or reduced for any reason other than a math or clerical error, you must attach Form 8862 to your tax return to claim the CTC, ACTC, or ODC unless an exception applies" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.no`

- **Authored helper label:** Year parameter household.no (false)
- **Encoded (Bool):** Enter false (household.no).
- Expr: `{"op":"param","ref":"household.no"}`
- Cite: [i1040gi] p. 39, Form 8862, who must file, "You must file Form 8862 to claim the child tax credit or credit for other dependents if your child tax credit"; p. 43, Form 8862, who must file, "You must file Form 8862 if your EIC for a year after 1996 was reduced or disallowed for any reason other than a math or clerical error" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.eic_above_zero`

- **Authored helper label:** The earned income credit figured in Step 6 (Worksheet A line 6, or Worksheet B line 11 for a filer who answered Yes to Step 5, question 2) is more than zero
- **Encoded (Bool):** eic line 6 (eic.line6) > eic helper "No amount"
- Expr: `{"gt":["eic.line6","eic.zero"],"op":"test"}`
- Cite: [i1040gi] p. 43, Form 8862, who must file, "You must file Form 8862 if your EIC for a year after 1996 was reduced or disallowed for any reason other than a math or clerical error" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.eic_claimed`

- **Authored helper label:** The earned income credit is claimed (Steps 1 to 5 are passed and the credit figured in Step 6, Worksheet A line 6 or Worksheet B line 11, is more than zero; false when Steps 1 to 5 are not passed)
- **Encoded (Bool):** Choose — [eic helper "Steps 1 to 5 passed in order (Step 6, figure the credit on Worksheet A)" = true → helper "The earned income credit figured in Step 6 (Worksheet A line 6, or Worksheet B line 11 for a filer who answered Yes to Step 5, question 2) is more than zero"] [eic helper "Steps 1 to 5 passed in order (Step 6, figure the credit on Worksheet A)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["eic.eligible",{"const":true}],"op":"test"},"then":"household.eic_above_zero"},{"guard":{"eq":["eic.eligible",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 43, Form 8862, who must file, "You must file Form 8862 if your EIC for a year after 1996 was reduced or disallowed for any reason other than a math or clerical error" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.claims_8862_credit`

- **Authored helper label:** The return claims the earned income credit, the child tax credit, the credit for other dependents or the additional child tax credit (the earned income credit is claimed, or Schedule 8812 line 8 is more than line 11)
- **Encoded (Bool):** (s8812 line 8 > s8812 line 11 or helper "The earned income credit is claimed (Steps 1 to 5 are passed and the credit figured in Step 6, Worksheet A line 6 or Worksheet B line 11, is more than zero; false when Steps 1 to 5 are not passed)" = true)
- Expr: `{"any":[{"gt":["s8812.line8","s8812.line11"],"op":"test"},{"eq":["household.eic_claimed",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 39, Form 8862, who must file, "You must file Form 8862 to claim the child tax credit or credit for other dependents if your child tax credit"; p. 43, Form 8862, who must file, "You must file Form 8862 if your EIC for a year after 1996 was reduced or disallowed for any reason other than a math or clerical error"; i1040s8812 p. 2, Form 8862 may be required, "you must attach Form 8862 to your tax return to claim the CTC, ACTC, or ODC unless an exception applies" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.credit_disallowed_if_claimed`

- **Authored helper label:** Whether an earlier earned income credit, child tax credit, additional child tax credit or credit for other dependents was reduced or disallowed (or a disallowance period applies), asked only when the return claims one of these credits (false otherwise, where Form 8862 does not apply)
- **Encoded (Bool):** Choose — [helper "The return claims the earned income credit, the child tax credit, the credit for other dependents or the additional child tax credit (the earned income credit is claimed, or Schedule 8812 line 8 is more than line 11)" = true → helper "Was your (or, on a joint return, your spouse's) EIC for a year after 1996, or child tax credit, additional child tax credit or credit for other dependents for a year after 2015, reduced or disallowed other than for a math or clerical error, or are you (or, on a joint return, your spouse) in a 2- or 10-year disallowance period?"] [helper "The return claims the earned income credit, the child tax credit, the credit for other dependents or the additional child tax credit (the earned income credit is claimed, or Schedule 8812 line 8 is more than line 11)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.claims_8862_credit",{"const":true}],"op":"test"},"then":"household.credit_disallowed"},{"guard":{"eq":["household.claims_8862_credit",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 39, Form 8862, who must file, "You must file Form 8862 to claim the child tax credit or credit for other dependents if your child tax credit"; p. 43, Form 8862, who must file, "You must file Form 8862 if your EIC for a year after 1996 was reduced or disallowed for any reason other than a math or clerical error" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `household.ctc_disallowed_claim`

- **Authored helper label:** Schedule 8812 line 8 is more than line 11 (a child tax credit or credit for other dependents is figured) and an earlier credit was reduced or disallowed (or a disallowance period applies)
- **Encoded (Bool):** s8812 line 8 > s8812 line 11 and helper "Whether an earlier earned income credit, child tax credit, additional child tax credit or credit for other dependents was reduced or disallowed (or a disallowance period applies), asked only when the return claims one of these credits (false otherwise, where Form 8862 does not apply)" = true
- Expr: `{"all":[{"gt":["s8812.line8","s8812.line11"],"op":"test"},{"eq":["household.credit_disallowed_if_claimed",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040s8812] p. 2, Form 8862 may be required, "If your CTC, ACTC, or ODC for a year after 2015 was denied or reduced for any reason other than a math or clerical error, you must attach Form 8862 to your tax return to claim the CTC, ACTC, or ODC unless an exception applies" (2025; printed date 2026-01-23; sha256 bb9788cd)

## (gate) — `household.eic_disallowed_claim`

- **Authored helper label:** The earned income credit is claimed (Steps 1 to 5 are passed with a credit above zero on Worksheet A line 6 or Worksheet B line 11) and an earlier credit was reduced or disallowed (or a disallowance period applies)
- **Encoded (Bool):** helper "The earned income credit is claimed (Steps 1 to 5 are passed and the credit figured in Step 6, Worksheet A line 6 or Worksheet B line 11, is more than zero; false when Steps 1 to 5 are not passed)" = true and helper "Whether an earlier earned income credit, child tax credit, additional child tax credit or credit for other dependents was reduced or disallowed (or a disallowance period applies), asked only when the return claims one of these credits (false otherwise, where Form 8862 does not apply)" = true
- Expr: `{"all":[{"eq":["household.eic_claimed",{"const":true}],"op":"test"},{"eq":["household.credit_disallowed_if_claimed",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 43, Form 8862, who must file, "You must file Form 8862 if your EIC for a year after 1996 was reduced or disallowed for any reason other than a math or clerical error" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.test1_persons`

- **Authored helper label:** Number of parents who qualify you under Test 1
- **Encoded (Count):** Add dependent.one over every confirmed dependent entry for which helper "Qualifies you for head of household under Test 1 through a parent who does not live with you (a parent who lives with you qualifies you through Test 2)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"dependent","field":"dependent.one","op":"sum_over","where":{"eq":["dependent.hoh_test1",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 14, Head of Household, Test 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.test2_persons`

- **Authored helper label:** Number of persons who qualify you under Test 2
- **Encoded (Count):** Add dependent.one over every confirmed dependent entry for which helper "A Test 2 person who lived with you more than half the year, or of the part of the year a relative was alive, counting only absences head of household counts (the home-cost condition of Test 2 is tested on the household form)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"dependent","field":"dependent.one","op":"sum_over","where":{"eq":["dependent.hoh_test2",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.test2_absence_persons`

- **Authored helper label:** Number of persons who would qualify you under Test 2 only by counting an absence head of household does not count
- **Encoded (Count):** Add dependent.one over every confirmed dependent entry for which helper "A Test 2 person only by counting an absence head of household does not count" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"dependent","field":"dependent.one","op":"sum_over","where":{"eq":["dependent.hoh_absence",{"const":true}],"op":"test"}}`
- Cite: [p501] p. 9, Temporary absences, "It must be reasonable to assume the absent person will return to the home after the temporary absence. You must continue to keep up the home during the absence." (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (helper) — `household.hoh_absence_from_test1`

- **Authored helper label:** Head of household turns on an absence head of household does not count, from Test 1 on: Test 1 not met, home cost paid, no Test 2 person, and a person who would be one only by counting an absence
- **Encoded (Bool):** Choose — [helper "Test 1 met" = true → helper "Year parameter household.no (false)"] [helper "Test 1 met" = false → helper "Head of household turns on an absence head of household does not count, from the home cost on: home cost paid, no Test 2 person, and a person who would be one only by counting an absence"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.test1_met",{"const":true}],"op":"test"},"then":"household.no"},{"guard":{"eq":["household.test1_met",{"const":false}],"op":"test"},"then":"household.hoh_absence_from_cost"}],"op":"choose"}`
- Cite: [p501] p. 9, Temporary absences, "You and your qualifying person are considered to live together even if one or both of you are temporarily absent from your home due to special circumstances" and "It must be reasonable to assume the absent person will return to the home after the temporary absence. You must continue to keep up the home during the absence." (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (helper) — `household.hoh_absence_from_cost`

- **Authored helper label:** Head of household turns on an absence head of household does not count, from the home cost on: home cost paid, no Test 2 person, and a person who would be one only by counting an absence
- **Encoded (Bool):** Choose — [helper "Did you pay over half the cost of keeping up your home for 2025?" = true → helper "Head of household turns on an absence head of household does not count, from Test 2 on: no Test 2 person, and a person who would be one only by counting an absence"] [helper "Did you pay over half the cost of keeping up your home for 2025?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.home_cost",{"const":true}],"op":"test"},"then":"household.hoh_absence_from_test2"},{"guard":{"eq":["household.home_cost",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [p501] p. 9, Temporary absences, "You and your qualifying person are considered to live together even if one or both of you are temporarily absent from your home due to special circumstances" and "It must be reasonable to assume the absent person will return to the home after the temporary absence. You must continue to keep up the home during the absence." (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (helper) — `household.hoh_absence_from_test2`

- **Authored helper label:** Head of household turns on an absence head of household does not count, from Test 2 on: no Test 2 person, and a person who would be one only by counting an absence
- **Encoded (Bool):** Choose — [helper "No person qualifies you under Test 2" = true → helper "A person would qualify you under Test 2 only by counting an absence head of household does not count"] [helper "No person qualifies you under Test 2" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.no_test2_persons",{"const":true}],"op":"test"},"then":"household.any_test2_absence"},{"guard":{"eq":["household.no_test2_persons",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [p501] p. 9, Temporary absences, "You and your qualifying person are considered to live together even if one or both of you are temporarily absent from your home due to special circumstances" and "It must be reasonable to assume the absent person will return to the home after the temporary absence. You must continue to keep up the home during the absence." (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (helper) — `household.no_test2_persons`

- **Authored helper label:** No person qualifies you under Test 2
- **Encoded (Bool):** helper "Number of persons who qualify you under Test 2" = 0 (a count)
- Expr: `{"eq":["household.test2_persons",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [p501] p. 9, Temporary absences, "You and your qualifying person are considered to live together even if one or both of you are temporarily absent from your home due to special circumstances" and "It must be reasonable to assume the absent person will return to the home after the temporary absence. You must continue to keep up the home during the absence." (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (helper) — `household.any_test2_absence`

- **Authored helper label:** A person would qualify you under Test 2 only by counting an absence head of household does not count
- **Encoded (Bool):** helper "Number of persons who would qualify you under Test 2 only by counting an absence head of household does not count" > 0 (a count)
- Expr: `{"gt":["household.test2_absence_persons",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [p501] p. 9, Temporary absences, "You and your qualifying person are considered to live together even if one or both of you are temporarily absent from your home due to special circumstances" and "It must be reasonable to assume the absent person will return to the home after the temporary absence. You must continue to keep up the home during the absence." (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (gate) — `household.hoh_absence`

- **Authored helper label:** Head of household turns on a person who lived with you more than half the year only by counting an absence head of household does not count
- **Encoded (Bool):** Choose — [helper "Unmarried, or considered unmarried under the head of household rules, at the end of 2025" = true → helper "Head of household turns on an absence head of household does not count, from Test 1 on: Test 1 not met, home cost paid, no Test 2 person, and a person who would be one only by counting an absence"] [helper "Unmarried, or considered unmarried under the head of household rules, at the end of 2025" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.unmarried",{"const":true}],"op":"test"},"then":"household.hoh_absence_from_test1"},{"guard":{"eq":["household.unmarried",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [p501] p. 9, Temporary absences, "You and your qualifying person are considered to live together even if one or both of you are temporarily absent from your home due to special circumstances" and "It must be reasonable to assume the absent person will return to the home after the temporary absence. You must continue to keep up the home during the absence." (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (helper) — `household.test1_met`

- **Authored helper label:** Test 1 met
- **Encoded (Bool):** helper "Number of parents who qualify you under Test 1" > 0 (a count)
- Expr: `{"gt":["household.test1_persons",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.any_test2_person`

- **Authored helper label:** A person qualifies you under Test 2
- **Encoded (Bool):** helper "Number of persons who qualify you under Test 2" > 0 (a count)
- Expr: `{"gt":["household.test2_persons",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2, "You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived for more than half of the year" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.test2_met`

- **Authored helper label:** Test 2 met, having paid over half the cost of keeping up your own home
- **Encoded (Bool):** Choose — [helper "Did you pay over half the cost of keeping up your home for 2025?" = true → helper "A person qualifies you under Test 2"] [helper "Did you pay over half the cost of keeping up your home for 2025?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.home_cost",{"const":true}],"op":"test"},"then":"household.any_test2_person"},{"guard":{"eq":["household.home_cost",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2, "You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived for more than half of the year" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.hoh_eligible`

- **Authored helper label:** Unmarried or considered unmarried, and Test 1 or Test 2 applies
- **Encoded (Bool):** helper "Unmarried, or considered unmarried under the head of household rules, at the end of 2025" = true and (helper "Test 1 met" = true or helper "Test 2 met, having paid over half the cost of keeping up your own home" = true)
- **Refusal:** when household.hoh_absence is true, cannot complete Temporary absences for head of household (Pub. 501). For head of household, an absence counts as time lived with you only if it was reasonable to assume the absent person would return and you kept up the home; the time the person who would qualify you lived with you must be recounted under that rule, which this tool does not do. Cite: [p501] p. 9, Temporary absences, "It must be reasonable to assume the absent person will return to the home after the temporary absence. You must continue to keep up the home during the absence." (2025 returns; PDF created 2026-02-04; sha256 288b62a4)
- **Refusal:** when household.hoh_community_property is true, cannot complete Community income on a married head of household return in a community property state (Form 8958; Pub. 555). A married person filing as head of household, where either spouse lived in or had a permanent home in a community property state, may have to report community income under state law; Form 8958 and the community property rules of Pub. 555 are outside this tool. Cite: [i1040gi] p. 23, Community Property States, "If you and your spouse lived in a community property state, you must usually follow state law to determine what is community income and what is separate income. For details, see Form 8958 and Pub. 555" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"all":[{"eq":["household.unmarried",{"const":true}],"op":"test"},{"any":[{"eq":["household.test1_met",{"const":true}],"op":"test"},{"eq":["household.test2_met",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, "Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `household.hoh_fails`

- **Authored helper label:** Head of household checked without meeting its tests
- **Encoded (Bool):** f1040 line Filing Status = 'hoh' and helper "Unmarried or considered unmarried, and Test 1 or Test 2 applies" = false
- **Refusal:** when household.hoh_missed is true, cannot complete Head of household filing status fits you. You chose single, but your answers meet the head of household tests (you were unmarried, and you paid over half the cost of keeping up a home for a person who qualifies you). Head of household gives a lower tax than single on the same income. Go back and choose head of household. If your spouse died in 2023 or 2024 and you did not remarry, look first at the line about being widowed (qualifying surviving spouse), which may give a lower tax. Cite: [i1040gi] p. 13, Filing Status, "The ones that will usually give you the lowest tax are listed last"; p. 13, Single, "You were widowed before January 1, 2025, and didn’t remarry before the end of 2025. But if you have a child, you may be able to use the qualifying surviving spouse filing status"; p. 14, Head of Household, "Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies" (2025; printed date 2026-02-25; sha256 482e9c48)
- **Refusal:** when household.hoh_missed_mfs is true, cannot complete Head of household filing status fits you. You chose married filing separately, but your answers meet the head of household tests (you lived apart from your spouse for the last 6 months of 2025 and are considered unmarried, and you paid over half the cost of keeping up a home for a person who qualifies you). Head of household gives a lower tax than married filing separately on the same income. Go back and choose head of household. Cite: [i1040gi] p. 13, Filing Status, "The ones that will usually give you the lowest tax are listed last"; p. 14, Married Filing Separately, "You may be able to file as head of household if you had a child living with you and you lived apart from your spouse during the last 6 months of 2025"; p. 15, Married persons who live apart, "Even if you weren’t divorced or legally separated at the end of 2025, you are considered unmarried if all of the following apply" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"all":[{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},{"eq":["household.hoh_eligible",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.dependents_listed`

- **Authored helper label:** Number of people listed as dependents
- **Encoded (Count):** Add dependent.one over every confirmed dependent entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"dependent","field":"dependent.one","op":"sum_over"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.dependents_any`

- **Authored helper label:** At least one person is listed as a dependent
- **Encoded (Bool):** helper "Number of people listed as dependents" > 0 (a count)
- Expr: `{"gt":["household.dependents_listed",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.hoh_missed_cost`

- **Authored helper label:** You paid over half the cost of keeping up your home and a person who qualifies you under Test 2 lived with you (the home cost asked first, so the dependent tests are read only when it was paid)
- **Encoded (Bool):** Choose — [helper "Did you pay over half the cost of keeping up your home for 2025?" = true → helper "A person qualifies you under Test 2: more persons lived with you than the ones who did only by counting an absence head of household does not count (the absence is asked only of a person who lived with you)"] [helper "Did you pay over half the cost of keeping up your home for 2025?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.home_cost",{"const":true}],"op":"test"},"then":"household.hoh_missed_person"},{"guard":{"eq":["household.home_cost",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2, "You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived for more than half of the year" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.test2_lived_persons`

- **Authored helper label:** Number of persons who would qualify you under Test 2, counting every absence you counted
- **Encoded (Count):** Add dependent.one over every confirmed dependent entry for which helper "A Test 2 person who lived with you more than half the year, or of the part of the year a relative was alive, counting every absence you counted (the home-cost condition of Test 2 is tested on the household form)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"dependent","field":"dependent.one","op":"sum_over","where":{"eq":["dependent.hoh_test2_lived",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.hoh_missed_person`

- **Authored helper label:** A person qualifies you under Test 2: more persons lived with you than the ones who did only by counting an absence head of household does not count (the absence is asked only of a person who lived with you)
- **Encoded (Bool):** helper "Number of persons who would qualify you under Test 2, counting every absence you counted" > helper "Number of persons who would qualify you under Test 2 only by counting an absence head of household does not count"
- Expr: `{"gt":["household.test2_lived_persons","household.test2_absence_persons"],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2; p501 p. 9, Temporary absences, "It must be reasonable to assume the absent person will return to the home after the temporary absence." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.hoh_missed_test2`

- **Authored helper label:** Test 2 met on a single or married filing separately return: asked only when a dependent is listed (false with none)
- **Encoded (Bool):** Choose — [helper "At least one person is listed as a dependent" = true → helper "You paid over half the cost of keeping up your home and a person who qualifies you under Test 2 lived with you (the home cost asked first, so the dependent tests are read only when it was paid)"] [helper "At least one person is listed as a dependent" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.dependents_any",{"const":true}],"op":"test"},"then":"household.hoh_missed_cost"},{"guard":{"eq":["household.dependents_any",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2, "You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived for more than half of the year" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `household.hoh_missed`

- **Authored helper label:** Single checked, though you were unmarried and Test 2 of head of household is met (Test 1, a parent's separate home, is not checked)
- **Encoded (Bool):** f1040 line Filing Status = 'single' and helper "Unmarried, or considered unmarried under the head of household rules, at the end of 2025" = true and helper "Test 2 met on a single or married filing separately return: asked only when a dependent is listed (false with none)" = true
- Expr: `{"all":[{"eq":["f1040.status",{"const":"single"}],"op":"test"},{"eq":["household.unmarried",{"const":true}],"op":"test"},{"eq":["household.hoh_missed_test2",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, "Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `household.hoh_missed_mfs`

- **Authored helper label:** Married filing separately checked, though a dependent is listed, you lived apart from your spouse for the last 6 months of 2025, Test 2 of head of household is met, and you are considered unmarried (each asked only after the one before it holds)
- **Encoded (Bool):** Choose — [helper "Filing status married filing separately" = true → helper "Married filing separately: a dependent is listed, and the rest of the head of household test holds (false with no one listed)"] [helper "Filing status married filing separately" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.mfs",{"const":true}],"op":"test"},"then":"household.hoh_missed_mfs_listed"},{"guard":{"eq":["household.mfs",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 14, Head of Household, "You are married but lived apart from your spouse for the last 6 months of 2025 and you meet the other rules under Married persons who live apart" and "Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies"; p501 p. 7, Married Filing Separately, "If you qualify to file as head of household, instead of as married filing separately, your tax may be lower" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.hoh_missed_mfs_listed`

- **Authored helper label:** Married filing separately: a dependent is listed, and the rest of the head of household test holds (false with no one listed)
- **Encoded (Bool):** Choose — [helper "At least one person is listed as a dependent" = true → helper "Married filing separately with a dependent listed: you lived apart from your spouse for the last 6 months of 2025, and the rest of the head of household test holds"] [helper "At least one person is listed as a dependent" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.dependents_any",{"const":true}],"op":"test"},"then":"household.hoh_missed_mfs_apart"},{"guard":{"eq":["household.dependents_any",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 15, Married persons who live apart, "You lived apart from your spouse for the last 6 months of 2025", "You paid over half the cost of keeping up your home for 2025" and "Your home was the main home of your child, stepchild, or foster child for more than half of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.hoh_missed_mfs_apart`

- **Authored helper label:** Married filing separately with a dependent listed: you lived apart from your spouse for the last 6 months of 2025, and the rest of the head of household test holds
- **Encoded (Bool):** Choose — [helper "Married filing separately, and your spouse did not live with you at any time in the last 6 months of 2025" = true → helper "Married filing separately and living apart: Test 2 of head of household is met and you are considered unmarried (the considered-unmarried question asked only once Test 2 is met)"] [helper "Married filing separately, and your spouse did not live with you at any time in the last 6 months of 2025" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.mfs_apart_last6",{"const":true}],"op":"test"},"then":"household.hoh_missed_mfs_test2"},{"guard":{"eq":["household.mfs_apart_last6",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 15, Married persons who live apart, "You lived apart from your spouse for the last 6 months of 2025", "You paid over half the cost of keeping up your home for 2025" and "Your home was the main home of your child, stepchild, or foster child for more than half of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.hoh_missed_mfs_test2`

- **Authored helper label:** Married filing separately and living apart: Test 2 of head of household is met and you are considered unmarried (the considered-unmarried question asked only once Test 2 is met)
- **Encoded (Bool):** Choose — [helper "Test 2 met on a single or married filing separately return: asked only when a dependent is listed (false with none)" = true → helper "Unmarried, or considered unmarried under the head of household rules, at the end of 2025"] [helper "Test 2 met on a single or married filing separately return: asked only when a dependent is listed (false with none)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.hoh_missed_test2",{"const":true}],"op":"test"},"then":"household.unmarried"},{"guard":{"eq":["household.hoh_missed_test2",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 15, Married persons who live apart, "You lived apart from your spouse for the last 6 months of 2025", "You paid over half the cost of keeping up your home for 2025" and "Your home was the main home of your child, stepchild, or foster child for more than half of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.qss_eligible`

- **Authored helper label:** Do all five qualifying surviving spouse tests apply to you?
- **Encoded (Bool):** Input — Do all five of these tests apply to you?

  - Your spouse died in 2023 or 2024 and you didn't remarry before the end of 2025 (if your spouse died in 2025, answer No).
  - You have a child or stepchild (not a foster child) whom you can claim as a dependent, or could claim as a dependent except that, for 2025, the child had gross income of $5,200 or more, the child filed a joint return, or you could be claimed as a dependent on someone else's return; an adopted child, including a child lawfully placed with you for legal adoption, is always your own child.
  - This child lived in your home for all of 2025, counting temporary absences by you or the child for special circumstances, such as school, vacation, business, medical care, military service or detention in a juvenile facility, as time lived in the home, but only an absence from which it was reasonable to assume the absent person would return and during which you kept up the home; a child born or who died in 2025, or adopted or lawfully placed with you for legal adoption in 2025, lived with you all year if your home was the child's home for the entire time the child was alive, or since the adoption or placement; if the child did not live with you all of 2025 because the child was presumed by law enforcement authorities to have been kidnapped by someone who isn't a member of your family or the child's family, answer No (the kidnapped-child rule of Pub. 501 is outside this tool).
  - You paid over half the cost of keeping up your home (rent, mortgage interest, real estate taxes, insurance on the home, repairs, utilities and food eaten in the home; not clothing, education, medical treatment, vacations, life insurance, transportation, or the value of your own or a household member’s services; amounts paid from a household member’s own funds, such as Social Security, count as paid by them; TANF or similar payments you received and used for the home count as paid by you).
  - You could have filed a joint return with your spouse the year your spouse died, even if you didn't actually do so.
- Expr: `{"op":"input","source":"Do all five of these tests apply to you?\n\n- Your spouse died in 2023 or 2024 and you didn't remarry before the end of 2025 (if your spouse died in 2025, answer No).\n- You have a child or stepchild (not a foster child) whom you can claim as a dependent, or could claim as a dependent except that, for 2025, the child had gross income of $5,200 or more, the child filed a joint return, or you could be claimed as a dependent on someone else's return; an adopted child, including a child lawfully placed with you for legal adoption, is always your own child.\n- This child lived in your home for all of 2025, counting temporary absences by you or the child for special circumstances, such as school, vacation, business, medical care, military service or detention in a juvenile facility, as time lived in the home, but only an absence from which it was reasonable to assume the absent person would return and during which you kept up the home; a child born or who died in 2025, or adopted or lawfully placed with you for legal adoption in 2025, lived with you all year if your home was the child's home for the entire time the child was alive, or since the adoption or placement; if the child did not live with you all of 2025 because the child was presumed by law enforcement authorities to have been kidnapped by someone who isn't a member of your family or the child's family, answer No (the kidnapped-child rule of Pub. 501 is outside this tool).\n- You paid over half the cost of keeping up your home (rent, mortgage interest, real estate taxes, insurance on the home, repairs, utilities and food eaten in the home; not clothing, education, medical treatment, vacations, life insurance, transportation, or the value of your own or a household member’s services; amounts paid from a household member’s own funds, such as Social Security, count as paid by them; TANF or similar payments you received and used for the home count as paid by you).\n- You could have filed a joint return with your spouse the year your spouse died, even if you didn't actually do so."}`
- Cite: [i1040gi] p. 15, Qualifying Surviving Spouse, "You can check the “Qualifying surviving spouse” box in the Filing Status section on page 1 of Form 1040 or 1040-SR and use joint return tax rates for 2025 if all of the following apply. 1. Your spouse died in 2023 or 2024 and you didn’t remarry before the end of 2025. 2. You have a child or stepchild (not a foster child) whom you can claim as a dependent or could claim as a dependent except that, for 2025: a. The child had gross income of $5,200 or more, b. The child filed a joint return, or c. You could be claimed as a dependent on someone else’s return." and "3. This child lived in your home for all of 2025. If the child didn’t live with you for the required time, see Exception to time lived with you, later. 4. You paid over half the cost of keeping up your home. 5. You could have filed a joint return with your spouse the year your spouse died, even if you didn’t actually do so."; "If your spouse died in 2025, you can't file as qualifying surviving spouse"; "An adopted child is always treated as your own child. An adopted child includes a child lawfully placed with you for legal adoption"; Exception to time lived with you, "Temporary absences by you or the child for special circumstances, such as school, vacation, business, medical care, military service, or detention in a juvenile facility, count as time lived in the home" and "A child is considered to have lived with you for all of 2025 if the child was born or died in 2025 and your home was the child’s home for the entire time the child was alive"; p501 p. 9, Note, "Amounts paid out of funds received in the child’s or qualifying person’s name, such as Social Security, are considered paid by the child, not you."; p501 p. 11, Qualifying Surviving Spouse, "4. This child lived in your home all year, except for temporary absences. See Temporary absences, earlier, under Head of Household."; p501 p. 9, Temporary absences, "It must be reasonable to assume the absent person will return to the home after the temporary absence. You must continue to keep up the home during the absence."; p501 p. 9, "Also don’t include the value of your services or those of a member of your household."; p501 p. 9, Note, "if you received Temporary Assistance to Needy Families (TANF) payments or other similar payments and used the payment to support another person, those payments are considered support you provided for that person"; p501 p. 11, Kidnapped child, "You may be eligible to file as a qualifying surviving spouse even if the child who qualifies you for this filing status has been kidnapped." (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `household.qss_fails`

- **Authored helper label:** Qualifying surviving spouse checked without meeting its tests
- **Encoded (Bool):** f1040 line Filing Status = 'qss' and helper "Do all five qualifying surviving spouse tests apply to you?" = false
- **Refusal:** when household.qss_child_not_all_year is true, cannot complete Qualifying surviving spouse filing status. Qualifying surviving spouse needs a child or stepchild of yours who lived in your home for all of 2025, but none of the children you listed lived with you all year. Correct the answer about where the child lived, or choose another filing status. Cite: [i1040gi] p. 15, Qualifying Surviving Spouse, "3. This child lived in your home for all of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"all":[{"eq":["f1040.status",{"const":"qss"}],"op":"test"},{"eq":["household.qss_eligible",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 15, Qualifying Surviving Spouse, "use joint return tax rates for 2025 if all of the following apply" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.qss`

- **Authored helper label:** Filing status qualifying surviving spouse
- **Encoded (Bool):** f1040 line Filing Status = 'qss'
- Expr: `{"eq":["f1040.status",{"const":"qss"}],"op":"test"}`
- Cite: [i1040gi] p. 15, Qualifying Surviving Spouse, "You can check the “Qualifying surviving spouse” box in the Filing Status section on page 1 of Form 1040 or 1040-SR" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.qss_claimed`

- **Authored helper label:** Qualifying surviving spouse checked and its tests answered Yes (false for any other filing status)
- **Encoded (Bool):** Choose — [helper "Filing status qualifying surviving spouse" = true → helper "Do all five qualifying surviving spouse tests apply to you?"] [helper "Filing status qualifying surviving spouse" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.qss",{"const":true}],"op":"test"},"then":"household.qss_eligible"},{"guard":{"eq":["household.qss",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 15, Qualifying Surviving Spouse, "use joint return tax rates for 2025 if all of the following apply" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.qss_no_child`

- **Authored helper label:** No son, daughter or stepchild is listed
- **Encoded (Bool):** helper "Number of people listed as your son, daughter or stepchild (not a foster child, grandchild or other descendant)" = 0 (a count)
- Expr: `{"eq":["household.qss_children_listed",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 15, Qualifying Surviving Spouse, "2. You have a child or stepchild (not a foster child) whom you can claim as a dependent or could claim as a dependent" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.qss_no_child_notice`

- **Authored helper label:** Notice: qualifying surviving spouse needs a son, daughter or stepchild of yours (not a foster child) who lived in your home for all of 2025, and none is listed among the people who lived with you. List that child (even one you cannot claim as a dependent), or choose another filing status.
- **Encoded (Bool):** Choose — [helper "Qualifying surviving spouse checked and its tests answered Yes (false for any other filing status)" = true → helper "No son, daughter or stepchild is listed"] [helper "Qualifying surviving spouse checked and its tests answered Yes (false for any other filing status)" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.qss_claimed",{"const":true}],"op":"test"},"then":"household.qss_no_child"},{"guard":{"eq":["household.qss_claimed",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 15, Qualifying Surviving Spouse, "2. You have a child or stepchild (not a foster child) whom you can claim as a dependent or could claim as a dependent" and "3. This child lived in your home for all of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.qss_children_listed`

- **Authored helper label:** Number of people listed as your son, daughter or stepchild (not a foster child, grandchild or other descendant)
- **Encoded (Count):** Add dependent.one over every confirmed dependent entry for which helper "Listed as your child and your son, daughter or stepchild, asked only when qualifying surviving spouse is checked and its tests answered Yes (false otherwise)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"dependent","field":"dependent.one","op":"sum_over","where":{"eq":["dependent.own_child_if_qss",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 15, Qualifying Surviving Spouse, "2. You have a child or stepchild (not a foster child) whom you can claim as a dependent or could claim as a dependent" and "3. This child lived in your home for all of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.qss_children_all_year`

- **Authored helper label:** Number of people listed as your son, daughter or stepchild who lived with you for all of 2025
- **Encoded (Count):** Add dependent.one over every confirmed dependent entry for which helper "Listed as your child and your son, daughter or stepchild, asked only when qualifying surviving spouse is checked and its tests answered Yes (false otherwise)" = true and helper "Listed as your child, and lived with you for all of 2025 (the lived-all-year answer is read only for a child)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"dependent","field":"dependent.one","op":"sum_over","where":{"all":[{"eq":["dependent.own_child_if_qss",{"const":true}],"op":"test"},{"eq":["dependent.child_all_year",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] p. 15, Qualifying Surviving Spouse, "2. You have a child or stepchild (not a foster child) whom you can claim as a dependent or could claim as a dependent" and "3. This child lived in your home for all of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `household.qss_child_not_all_year`

- **Authored helper label:** Qualifying surviving spouse checked and its tests answered Yes, but a child is listed and none of the children listed lived with you for all of 2025
- **Encoded (Bool):** helper "Number of people listed as your son, daughter or stepchild (not a foster child, grandchild or other descendant)" > 0 (a count) and helper "Number of people listed as your son, daughter or stepchild who lived with you for all of 2025" = 0 (a count)
- Note: A child is counted only through dependent.own_child_if_qss, which is asked only when qualifying surviving spouse is checked and its tests answered Yes and is false otherwise, so no child is listed on any other return.
- Expr: `{"all":[{"gt":["household.qss_children_listed",{"const":0,"type":"Count"}],"op":"test"},{"eq":["household.qss_children_all_year",{"const":0,"type":"Count"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 15, Qualifying Surviving Spouse, "2. You have a child or stepchild (not a foster child) whom you can claim as a dependent or could claim as a dependent" and "3. This child lived in your home for all of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.rdp`

- **Authored helper label:** Were you a registered domestic partner in Nevada, Washington or California at any time in 2025?
- **Encoded (Bool):** Input — Were you a registered domestic partner in Nevada, Washington or California at any time in 2025?
- Expr: `{"op":"input","source":"Were you a registered domestic partner in Nevada, Washington or California at any time in 2025?"}`
- Cite: [i1040gi] p. 23, Community Property States, Nevada, Washington, and California domestic partners, "A registered domestic partner in Nevada, Washington, or California must generally report half the combined community income of the individual and their domestic partner" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.spouse_died_this_year`

- **Authored helper label:** Did your spouse die in 2025?
- **Encoded (Bool):** Input — Did your spouse die in 2025? (Asked when your filing status is single or head of household, when filing jointly although not married at the end of 2025, and on a joint return with child or dependent care expenses, Form 2441.)
- Expr: `{"op":"input","source":"Did your spouse die in 2025? (Asked when your filing status is single or head of household, when filing jointly although not married at the end of 2025, and on a joint return with child or dependent care expenses, Form 2441.)"}`
- Cite: [p501] p. 6, Spouse died during the year, "If your spouse died during the year, you are considered married for the whole year for filing status purposes." (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (helper) — `household.spouse_died_this_year_if_ever_married`

- **Authored helper label:** Your spouse died in 2025, asked only where a marriage is possible (false for a person never married)
- **Encoded (Bool):** Choose — [helper "A marriage is possible: the filing status states one, or a person filing as single or head of household has been married at some time" = true → helper "Did your spouse die in 2025?"] [helper "A marriage is possible: the filing status states one, or a person filing as single or head of household has been married at some time" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.marriage_possible",{"const":true}],"op":"test"},"then":"household.spouse_died_this_year"},{"guard":{"eq":["household.marriage_possible",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [p501] p. 6, Spouse died during the year, "If your spouse died during the year, you are considered married for the whole year for filing status purposes." (2025 returns; PDF created 2026-02-04; sha256 288b62a4)

## (gate) — `household.widowed_this_year`

- **Authored helper label:** Filing as single or head of household although your spouse died in 2025
- **Encoded (Bool):** Choose — [f1040 line Filing Status = 'single' → helper "Your spouse died in 2025, asked only where a marriage is possible (false for a person never married)"] [f1040 line Filing Status = 'mfj' → helper "Year parameter household.no (false)"] [f1040 line Filing Status = 'mfs' → helper "Year parameter household.no (false)"] [f1040 line Filing Status = 'hoh' → helper "Your spouse died in 2025, asked only where a marriage is possible (false for a person never married)"] [f1040 line Filing Status = 'qss' → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"household.spouse_died_this_year_if_ever_married"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"household.no"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"household.no"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"household.spouse_died_this_year_if_ever_married"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 13, Single, "You were widowed before January 1, 2025, and didn’t remarry before the end of 2025"; p. 13, Married Filing Jointly, "Your spouse died in 2025 and you didn’t remarry in 2025."; p501 p. 6, Spouse died during the year, "If your spouse died during the year, you are considered married for the whole year for filing status purposes." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.cp_married`

- **Authored helper label:** Married at any time in 2025 while living in, or having your permanent home in, a community property state, though not married at the end of 2025
- **Encoded (Bool):** Input — Were you married at any time during 2025, before a divorce or legal separation, while you lived in, or had your permanent home (domicile) in, a community property state (Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington or Wisconsin)? (Asked when you lived in, or had your permanent home in, a community property state in 2025, are not filing jointly and were not married at the end of 2025.)
- Expr: `{"op":"input","source":"Were you married at any time during 2025, before a divorce or legal separation, while you lived in, or had your permanent home (domicile) in, a community property state (Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington or Wisconsin)? (Asked when you lived in, or had your permanent home in, a community property state in 2025, are not filing jointly and were not married at the end of 2025.)"}`
- Cite: [i1040gi] p. 23, Community Property States, "If you and your spouse lived in a community property state, you must usually follow state law to determine what is community income and what is separate income. For details, see Form 8958 and Pub. 555." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.cp_married_if_ever_married`

- **Authored helper label:** Married for part of 2025 while living in a community property state, asked only where a marriage is possible (false for a person never married)
- **Encoded (Bool):** Choose — [helper "A marriage is possible: the filing status states one, or a person filing as single or head of household has been married at some time" = true → helper "Married at any time in 2025 while living in, or having your permanent home in, a community property state, though not married at the end of 2025"] [helper "A marriage is possible: the filing status states one, or a person filing as single or head of household has been married at some time" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.marriage_possible",{"const":true}],"op":"test"},"then":"household.cp_married"},{"guard":{"eq":["household.marriage_possible",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 23, Community Property States, "If you and your spouse lived in a community property state, you must usually follow state law to determine what is community income and what is separate income. For details, see Form 8958 and Pub. 555." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.cp_not_joint`

- **Authored helper label:** Not filing jointly: lived in a community property state, not married at the end of 2025, and married for part of 2025 while living there
- **Encoded (Bool):** Choose — [helper "Did you live in, or have your permanent home (domicile) in, a community property state at any time in 2025?" = true → helper "Not filing jointly and lived in a community property state: not married at the end of 2025, and married for part of 2025 while living there"] [helper "Did you live in, or have your permanent home (domicile) in, a community property state at any time in 2025?" = false → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.community_property",{"const":true}],"op":"test"},"then":"household.cp_unmarried"},{"guard":{"eq":["household.community_property",{"const":false}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 23, Community Property States, "If you and your spouse lived in a community property state, you must usually follow state law to determine what is community income and what is separate income. For details, see Form 8958 and Pub. 555." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.cp_unmarried`

- **Authored helper label:** Not filing jointly and lived in a community property state: not married at the end of 2025, and married for part of 2025 while living there
- **Encoded (Bool):** Choose — [helper "Married at the end of 2025 (false for a person filing as single or head of household who has never been married)" = true → helper "Year parameter household.no (false)"] [helper "Married at the end of 2025 (false for a person filing as single or head of household who has never been married)" = false → helper "Married for part of 2025 while living in a community property state, asked only where a marriage is possible (false for a person never married)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.married",{"const":true}],"op":"test"},"then":"household.no"},{"guard":{"eq":["household.married",{"const":false}],"op":"test"},"then":"household.cp_married_if_ever_married"}],"op":"choose"}`
- Cite: [i1040gi] p. 23, Community Property States, "If you and your spouse lived in a community property state, you must usually follow state law to determine what is community income and what is separate income. For details, see Form 8958 and Pub. 555." (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `household.cp_marriage_ended`

- **Authored helper label:** Not filing jointly, and married for part of 2025 while living in a community property state
- **Encoded (Bool):** Choose — [f1040 line Filing Status = 'single' → helper "Not filing jointly: lived in a community property state, not married at the end of 2025, and married for part of 2025 while living there"] [f1040 line Filing Status = 'mfj' → helper "Year parameter household.no (false)"] [f1040 line Filing Status = 'mfs' → helper "Not filing jointly: lived in a community property state, not married at the end of 2025, and married for part of 2025 while living there"] [f1040 line Filing Status = 'hoh' → helper "Not filing jointly: lived in a community property state, not married at the end of 2025, and married for part of 2025 while living there"] [f1040 line Filing Status = 'qss' → helper "Not filing jointly: lived in a community property state, not married at the end of 2025, and married for part of 2025 while living there"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"household.cp_not_joint"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"household.no"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"household.cp_not_joint"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"household.cp_not_joint"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"household.cp_not_joint"}],"op":"choose"}`
- Cite: [i1040gi] p. 23, Community Property States, "If you and your spouse lived in a community property state, you must usually follow state law to determine what is community income and what is separate income. For details, see Form 8958 and Pub. 555." (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `household.rdp_community_property`

- **Authored helper label:** Not filing jointly, and a registered domestic partner in Nevada, Washington or California at any time in 2025 (wherever you lived)
- **Encoded (Bool):** f1040 line Filing Status ≠ 'mfj' and helper "Were you a registered domestic partner in Nevada, Washington or California at any time in 2025?" = true
- Expr: `{"all":[{"ne":["f1040.status",{"const":"mfj"}],"op":"test"},{"eq":["household.rdp",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 23, Community Property States, Nevada, Washington, and California domestic partners, "A registered domestic partner in Nevada, Washington, or California must generally report half the combined community income of the individual and their domestic partner. See Form 8958 and Pub. 555"; p555 p. 2, Domicile, "If you and your spouse (or your RDP) have different domiciles, check the laws of each to see if you have community property, community income, or both." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.joint_unmarried`

- **Authored helper label:** Not married at the end of 2025, and no spouse who died in 2025 (read for a joint or a separate return)
- **Encoded (Bool):** Choose — [helper "Married at the end of 2025 (false for a person filing as single or head of household who has never been married)" = true → helper "Year parameter household.no (false)"] [helper "Married at the end of 2025 (false for a person filing as single or head of household who has never been married)" = false → helper "Your spouse did not die in 2025"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.married",{"const":true}],"op":"test"},"then":"household.no"},{"guard":{"eq":["household.married",{"const":false}],"op":"test"},"then":"household.no_spouse_died"}],"op":"choose"}`
- Cite: [i1040gi] p. 13, Single, "But if, at the end of 2025, your divorce wasn’t final (an interlocutory decree), you are considered married and can’t check the box."; p. 13, Married Filing Jointly, "You were married at the end of 2025"; p. 13, "Your spouse died in 2025 and you didn’t remarry in 2025." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.no_spouse_died`

- **Authored helper label:** Your spouse did not die in 2025
- **Encoded (Bool):** helper "Your spouse died in 2025, asked only where a marriage is possible (false for a person never married)" = false
- Expr: `{"eq":["household.spouse_died_this_year_if_ever_married",{"const":false}],"op":"test"}`
- Cite: [i1040gi] p. 13, Single, "But if, at the end of 2025, your divorce wasn’t final (an interlocutory decree), you are considered married and can’t check the box."; p. 13, Married Filing Jointly, "You were married at the end of 2025"; p. 13, "Your spouse died in 2025 and you didn’t remarry in 2025." (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `household.filing_status_conflict`

- **Authored helper label:** The filing status conflicts with the marriage facts entered
- **Encoded (Bool):** Choose — [f1040 line Filing Status = 'single' → helper "Married at the end of 2025 (false for a person filing as single or head of household who has never been married)"] [f1040 line Filing Status = 'mfj' → helper "Not married at the end of 2025, and no spouse who died in 2025 (read for a joint or a separate return)"] [f1040 line Filing Status = 'mfs' → helper "Not married at the end of 2025, and no spouse who died in 2025 (read for a joint or a separate return)"] [f1040 line Filing Status = 'hoh' → helper "Year parameter household.no (false)"] [f1040 line Filing Status = 'qss' → helper "Year parameter household.no (false)"]
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"household.married"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"household.joint_unmarried"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"household.joint_unmarried"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"household.no"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 13, Single, "But if, at the end of 2025, your divorce wasn’t final (an interlocutory decree), you are considered married and can’t check the box."; p. 13, Married Filing Jointly, "You were married at the end of 2025"; p. 13, "Your spouse died in 2025 and you didn’t remarry in 2025."; p. 14, Married Filing Separately, "if you are married at the end of 2025 and file a separate return"; p501 p. 6, Spouse died during the year, "If your spouse died during the year, you are considered married for the whole year for filing status purposes." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.mfs`

- **Authored helper label:** Filing status married filing separately
- **Encoded (Bool):** f1040 line Filing Status = 'mfs'
- Expr: `{"eq":["f1040.status",{"const":"mfs"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Married Filing Separately, "Check the “Married filing separately” box in the Filing Status section on page 1 of Form 1040 or 1040-SR if you are married at the end of 2025 and file a separate return" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.mfs_spouse_notice`

- **Authored helper label:** Notice: on a married filing separately return, enter your spouse's name in the entry space beside the box, and your spouse's SSN or ITIN in the space for the spouse's SSN ("NRA" if your spouse has none and needs none)
- **Encoded (Bool):** Enter the amount from helper "Filing status married filing separately".
- Expr: `{"from":"household.mfs","op":"copy"}`
- Cite: [i1040gi] p. 14, Married Filing Separately, "Enter your spouse’s name in the entry space. Be sure to enter your spouse’s SSN or ITIN in the space for spouse’s SSN on Form 1040 or 1040-SR. If your spouse doesn’t have and isn’t required to have an SSN or ITIN, enter “NRA” in the entry space." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.mfs_living`

- **Authored helper label:** Married filing separately: when you lived with your spouse in 2025 (together_late: at some time from July through December; apart_last6: only before July; apart_all_year: not at any time)
- **Encoded (Enum(mfs_living)):** Input — Married filing separately: did you live with your spouse at any time in 2025? together_late if you lived together at some time from July 1 through December 31, 2025; apart_last6 if you lived together only before July 1, 2025; apart_all_year if you did not live together at any time in 2025. A temporary absence for special circumstances, such as business, medical care, school or military service, counts as time lived together, and so does time you shared a home while separated.
- Interpretation: amb.2025.mfs_lived_apart
- Expr: `{"op":"input","source":"Married filing separately: did you live with your spouse at any time in 2025? together_late if you lived together at some time from July 1 through December 31, 2025; apart_last6 if you lived together only before July 1, 2025; apart_all_year if you did not live together at any time in 2025. A temporary absence for special circumstances, such as business, medical care, school or military service, counts as time lived together, and so does time you shared a home while separated."}`
- Cite: [i1040gi] p. 15, Married persons who live apart, "You lived apart from your spouse for the last 6 months of 2025. Temporary absences for special circumstances, such as for business, medical care, school, or military service, count as time lived in the home"; p. 32, Social Security Benefits Worksheet, line 8, "Married filing separately and you lived with your spouse at any time in 2025"; p. 31, Line 6d, "If you are married filing separately and you lived apart from your spouse for all of 2025, check the box on line 6d"; p501 p. 8, Considered Unmarried, "Your spouse didn't live in your home during the last 6 months of the tax year" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.mfs_living_else`

- **Authored helper label:** Year parameter household.mfs_living_else (together_late)
- **Encoded (Enum(mfs_living)):** Enter together_late (household.mfs_living_else).
- Expr: `{"op":"param","ref":"household.mfs_living_else"}`
- Cite: [i1040gi] p. 32, Social Security Benefits Worksheet, line 8, "Married filing separately and you lived with your spouse at any time in 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.mfs_living_if_mfs`

- **Authored helper label:** When you lived with your spouse in 2025, asked only on a married filing separately return (together_late otherwise, so that neither lived-apart test is met)
- **Encoded (Enum(mfs_living)):** Choose — [helper "Filing status married filing separately" = true → helper "Married filing separately: when you lived with your spouse in 2025 (together_late: at some time from July through December; apart_last6: only before July; apart_all_year: not at any time)"] [helper "Filing status married filing separately" = false → helper "Year parameter household.mfs_living_else (together_late)"]
- Expr: `{"alternatives":[{"guard":{"eq":["household.mfs",{"const":true}],"op":"test"},"then":"household.mfs_living"},{"guard":{"eq":["household.mfs",{"const":false}],"op":"test"},"then":"household.mfs_living_else"}],"op":"choose"}`
- Cite: [i1040gi] p. 31, Line 6d, "If you are married filing separately and you lived apart from your spouse for all of 2025, check the box on line 6d"; p. 15, Married persons who live apart, "You lived apart from your spouse for the last 6 months of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.mfs_apart_all_year`

- **Authored helper label:** Married filing separately, and you lived apart from your spouse for all of 2025
- **Encoded (Bool):** helper "When you lived with your spouse in 2025, asked only on a married filing separately return (together_late otherwise, so that neither lived-apart test is met)" = 'apart_all_year'
- Interpretation: amb.2025.mfs_lived_apart
- Expr: `{"eq":["household.mfs_living_if_mfs",{"const":"apart_all_year"}],"op":"test"}`
- Cite: [i1040gi] p. 31, Line 6d, "If you are married filing separately and you lived apart from your spouse for all of 2025, check the box on line 6d"; p. 97, IRA Deduction Worksheet—Schedule 1, Line 20, line 2, "married filing separately and you lived apart from your spouse for all of 2025, enter $89,000" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.mfs_apart_last6`

- **Authored helper label:** Married filing separately, and your spouse did not live with you at any time in the last 6 months of 2025
- **Encoded (Bool):** (helper "When you lived with your spouse in 2025, asked only on a married filing separately return (together_late otherwise, so that neither lived-apart test is met)" = 'apart_last6' or helper "When you lived with your spouse in 2025, asked only on a married filing separately return (together_late otherwise, so that neither lived-apart test is met)" = 'apart_all_year')
- Interpretation: amb.2025.mfs_lived_apart
- Expr: `{"any":[{"eq":["household.mfs_living_if_mfs",{"const":"apart_last6"}],"op":"test"},{"eq":["household.mfs_living_if_mfs",{"const":"apart_all_year"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 15, Married persons who live apart, "You lived apart from your spouse for the last 6 months of 2025"; p. 44, Special rule for separated spouses, "You lived apart from your spouse for the last 6 months of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `household.mfs_community_property`

- **Authored helper label:** Married filing separately, and you or your husband or wife lived in, or had a permanent home in, a community property state at some time in 2025
- **Encoded (Bool):** Choose — [f1040 line Filing Status = 'single' → helper "Year parameter household.no (false)"] [f1040 line Filing Status = 'mfj' → helper "Year parameter household.no (false)"] [f1040 line Filing Status = 'mfs' → helper "You lived in, or had your permanent home in, a community property state in 2025, or (asked when you did not) your husband or wife did, or (asked when neither did) retirement pay received in 2025 was earned while married and living in one"] [f1040 line Filing Status = 'hoh' → helper "Year parameter household.no (false)"] [f1040 line Filing Status = 'qss' → helper "Year parameter household.no (false)"]
- Interpretation: amb.2025.mfs_community_property
- Expr: `{"alternatives":[{"guard":{"eq":["f1040.status",{"const":"single"}],"op":"test"},"then":"household.no"},{"guard":{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},"then":"household.no"},{"guard":{"eq":["f1040.status",{"const":"mfs"}],"op":"test"},"then":"household.cp_any"},{"guard":{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},"then":"household.no"},{"guard":{"eq":["f1040.status",{"const":"qss"}],"op":"test"},"then":"household.no"}],"op":"choose"}`
- Cite: [i1040gi] p. 14, Married Filing Separately, "Different rules apply to people in community property states; see Pub. 555"; p. 23, Community Property States, "If you and your spouse lived in a community property state, you must usually follow state law to determine what is community income and what is separate income" (2025; printed date 2026-02-25; sha256 482e9c48)
