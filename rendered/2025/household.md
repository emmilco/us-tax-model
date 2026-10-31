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

## (helper) — `household.hsa_split_count`

- **Authored helper label:** Number of Forms 8889 using the spouse rule of line 6
- **Encoded (Count):** Add person.hsa_split over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.hsa_split","op":"sum_over"}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, Steps 1 to 3, "Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025, use the following rules to figure the amount on line 6", "Step 1. Refigure the contribution limit that would have been entered on line 5 if you had entered on line 3 the total of the worksheet amounts only for the months you were treated as having family coverage", "Step 2. Divide the refigured contribution limit from Step 1 equally between you and your spouse, unless you both agree on a different allocation (such as allocating nothing to one spouse)", "Step 3. Subtract the part of the contribution limit allocated to your spouse in Step 2 from the amount determined in Step 1" (2025; sha256 da6f2f58)

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

## (helper) — `household.under16_count`

- **Authored helper label:** Number of people on the return under age 16 at the end of 2025
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Were you under age 16 at the end of 2025?" = true, within the current person when parent-bound. An unanswered roster is unknown.
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
- **Encoded (Count):** Add person.one over every confirmed person entry for which (helper "Do you have an SSN or ITIN issued on or before the due date of your return?" = true or helper "If not, have you applied for an ITIN on or before the due date of your return?" = true), within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"any":[{"eq":["person.tin",{"const":true}],"op":"test"},{"eq":["person.itin_applied",{"const":true}],"op":"test"}],"op":"test"}}`
- Cite: [i1040gi] p. 17, Before you begin, "If you want to claim the credit for other dependents, you, and your spouse if filing jointly, must have either an SSN or ITIN"; p. 19, Step 5, question 1, "(Answer 'Yes' if you are applying for an ITIN on or before the return due date (including extensions).)" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.all_tin`

- **Authored helper label:** You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
- **Encoded (Bool):** helper "Number of people on the return with an SSN or ITIN, or who have applied for an ITIN" = helper "Number of people on the return (you, and your spouse if filing jointly)"
- Expr: `{"eq":["household.tin_count","household.persons"],"op":"test"}`
- Cite: [i1040gi] p. 17, Before you begin, "If you want to claim the credit for other dependents, you, and your spouse if filing jointly, must have either an SSN or ITIN" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.id_count`

- **Authored helper label:** Number of people on the return with an SSN valid for employment or an SSN or ITIN
- **Encoded (Count):** Add person.one over every confirmed person entry for which (helper "Do you have an SSN valid for employment issued before the due date of your return?" = true or helper "Do you have an SSN or ITIN issued on or before the due date of your return?" = true), within the current person when parent-bound. An unanswered roster is unknown.
- Interpretation: amb.2025.ctc_spouse_itin_application
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"any":[{"eq":["person.work_ssn",{"const":true}],"op":"test"},{"eq":["person.tin",{"const":true}],"op":"test"}],"op":"test"}}`
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
- Cite: [i1040gi] p. 18, Step 3, question 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.taxpayer_work_ssn`

- **Authored helper label:** Do you have an SSN valid for employment issued before the due date of your return?
- **Encoded (Bool):** helper "Your entry, if the answer is yes" > 0 (a count)
- Expr: `{"gt":["household.taxpayer_work_ssn_count",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 18, Step 3, question 4 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.home_cost`

- **Authored helper label:** Did you pay over half the cost of keeping up your home for 2025?
- **Encoded (Bool):** Input — Did you pay over half the cost of keeping up your home for 2025? Cost of keeping up a home includes expenses such as rent, mortgage interest, real estate taxes, insurance on the home, repairs, utilities, and food eaten in the home. It does not include the cost of clothing, education, medical treatment, vacations, life insurance, or transportation, or the value of your services or those of a member of your household. Amounts paid out of funds received in the name of a person who lives in the home, such as their Social Security, count as paid by that person, not you.
- Expr: `{"op":"input","source":"Did you pay over half the cost of keeping up your home for 2025? Cost of keeping up a home includes expenses such as rent, mortgage interest, real estate taxes, insurance on the home, repairs, utilities, and food eaten in the home. It does not include the cost of clothing, education, medical treatment, vacations, life insurance, or transportation, or the value of your services or those of a member of your household. Amounts paid out of funds received in the name of a person who lives in the home, such as their Social Security, count as paid by that person, not you."}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2; p. 15, "Keeping up a home. To find out what is included in the cost of keeping up a home, see Pub. 501."; p501 p. 9, Keeping Up a Home, "Costs you include. Include in the cost of keeping up a home expenses such as rent, mortgage interest, real estate taxes, insurance on the home, repairs, utilities, and food eaten in the home." p501 p. 9, "Costs you don’t include. Don’t include the cost of clothing, education, medical treatment, vacations, life insurance, or transportation. Also don’t include the value of your services or those of a member of your household." p501 p. 9, Note, "Amounts paid out of funds received in the child’s or qualifying person’s name, such as Social Security, are considered paid by the child, not you." (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.unmarried`

- **Authored helper label:** Were you unmarried, or considered unmarried under the head of household rules, at the end of 2025?
- **Encoded (Bool):** Input — Were you unmarried, or considered unmarried under the head of household rules, at the end of 2025?
- Expr: `{"op":"input","source":"Were you unmarried, or considered unmarried under the head of household rules, at the end of 2025?"}`
- Cite: [i1040gi] p. 14, Head of Household, "You are considered unmarried for this purpose if any of the following applies" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.married`

- **Authored helper label:** Were you married at the end of 2025?
- **Encoded (Bool):** Input — Were you married at the end of 2025 (including married but considered unmarried for head of household status)?
- Expr: `{"op":"input","source":"Were you married at the end of 2025 (including married but considered unmarried for head of household status)?"}`
- Cite: [i1040gi] p. 41, Step 3, question 3, and Step 4, question 1, "Are you a married taxpayer whose filing status is married filing separately or head of household?"; i8889 p. 4, Line 3, rule 6, "If, at the end of 2025, you were age 55 or older and unmarried or married with self-only HDHP coverage for the entire year" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.community_property`

- **Authored helper label:** Did you live in a community property state at any time in 2025?
- **Encoded (Bool):** Input — Did you live in a community property state (Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington or Wisconsin) at any time in 2025?
- Expr: `{"op":"input","source":"Did you live in a community property state (Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington or Wisconsin) at any time in 2025?"}`
- Cite: [i1040gi] p. 23, Community Property States, "Community property states include Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington, and Wisconsin" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `household.hoh_community_property`

- **Authored helper label:** Married, filing as head of household, and living in a community property state
- **Encoded (Bool):** f1040 line Filing Status = 'hoh' and helper "Were you married at the end of 2025?" = true and helper "Did you live in a community property state at any time in 2025?" = true
- Interpretation: amb.2025.hoh_community_property
- Expr: `{"all":[{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},{"eq":["household.married",{"const":true}],"op":"test"},{"eq":["household.community_property",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 23, Community Property States, "If you and your spouse lived in a community property state, you must usually follow state law to determine what is community income and what is separate income" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.credit_disallowed`

- **Authored helper label:** Was your EIC for a year after 1996, or your child tax credit, additional child tax credit or credit for other dependents for a year after 2015, reduced or disallowed other than for a math or clerical error, or are you in a 2- or 10-year disallowance period?
- **Encoded (Bool):** Input — Was your earned income credit for any year after 1996, or your child tax credit, additional child tax credit or credit for other dependents for any year after 2015, reduced or disallowed for any reason other than a math or clerical error, or are you in a 2- or 10-year period during which you can't take one of these credits because an earlier claim was found to be reckless, intentional or fraudulent?
- Expr: `{"op":"input","source":"Was your earned income credit for any year after 1996, or your child tax credit, additional child tax credit or credit for other dependents for any year after 2015, reduced or disallowed for any reason other than a math or clerical error, or are you in a 2- or 10-year period during which you can't take one of these credits because an earlier claim was found to be reckless, intentional or fraudulent?"}`
- Cite: [i1040gi] p. 43, Form 8862, who must file, "You must file Form 8862 if your EIC for a year after 1996 was reduced or disallowed for any reason other than a math or clerical error" and "don’t file Form 8862 or take the credit for the ... 2 years after the most recent tax year for which there was a final determination that your EIC claim was due to reckless or intentional disregard of the EIC rules ... 10 years after the most recent tax year for which there was a final determination that your EIC claim was due to fraud"; p. 39, Form 8862, who must file, "You must file Form 8862 to claim the child tax credit or credit for other dependents if your child tax credit (refundable or nonrefundable depending on the tax year), additional child tax credit, or credit for other dependents for a year after 2015 was denied or reduced for any reason other than a math or clerical error"; i1040s8812 p. 2, Form 8862 may be required, "If your CTC, ACTC, or ODC for a year after 2015 was denied or reduced for any reason other than a math or clerical error, you must attach Form 8862 to your tax return to claim the CTC, ACTC, or ODC unless an exception applies" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.test1_persons`

- **Authored helper label:** Number of parents who qualify you under Test 1
- **Encoded (Count):** Add dependent.one over every confirmed dependent entry for which helper "Qualifies you for head of household under Test 1 through a parent who does not live with you (a parent who lives with you qualifies you through Test 2)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"dependent","field":"dependent.one","op":"sum_over","where":{"eq":["dependent.hoh_test1",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 14, Head of Household, Test 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.test2_persons`

- **Authored helper label:** Number of persons who qualify you under Test 2
- **Encoded (Count):** Add dependent.one over every confirmed dependent entry for which helper "A Test 2 person who lived with you more than half the year, or of the part of the year a relative was alive (the home-cost condition of Test 2 is tested on the household form)" = true, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"dependent","field":"dependent.one","op":"sum_over","where":{"eq":["dependent.hoh_test2",{"const":true}],"op":"test"}}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.test1_met`

- **Authored helper label:** Test 1 met
- **Encoded (Bool):** helper "Number of parents who qualify you under Test 1" > 0 (a count)
- Expr: `{"gt":["household.test1_persons",{"const":0,"type":"Count"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 1 (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.test2_met`

- **Authored helper label:** Test 2 met, having paid over half the cost of keeping up your own home
- **Encoded (Bool):** helper "Did you pay over half the cost of keeping up your home for 2025?" = true and helper "Number of persons who qualify you under Test 2" > 0 (a count)
- Expr: `{"all":[{"eq":["household.home_cost",{"const":true}],"op":"test"},{"gt":["household.test2_persons",{"const":0,"type":"Count"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2, "You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived for more than half of the year" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.hoh_eligible`

- **Authored helper label:** Unmarried or considered unmarried, and Test 1 or Test 2 applies
- **Encoded (Bool):** helper "Were you unmarried, or considered unmarried under the head of household rules, at the end of 2025?" = true and (helper "Test 1 met" = true or helper "Test 2 met, having paid over half the cost of keeping up your own home" = true)
- **Refusal:** when household.hoh_community_property is true, cannot complete Community income on a married head of household return in a community property state (Form 8958; Pub. 555). A married person filing as head of household who lived in a community property state may have to report community income under state law; Form 8958 and the community property rules of Pub. 555 are outside this tool. Cite: [i1040gi] p. 23, Community Property States, "If you and your spouse lived in a community property state, you must usually follow state law to determine what is community income and what is separate income. For details, see Form 8958 and Pub. 555" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"all":[{"eq":["household.unmarried",{"const":true}],"op":"test"},{"any":[{"eq":["household.test1_met",{"const":true}],"op":"test"},{"eq":["household.test2_met",{"const":true}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household, "Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `household.hoh_fails`

- **Authored helper label:** Head of household checked without meeting its tests
- **Encoded (Bool):** f1040 line Filing Status = 'hoh' and helper "Unmarried or considered unmarried, and Test 1 or Test 2 applies" = false
- Expr: `{"all":[{"eq":["f1040.status",{"const":"hoh"}],"op":"test"},{"eq":["household.hoh_eligible",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 14, Head of Household (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.qss_eligible`

- **Authored helper label:** Do all five qualifying surviving spouse tests apply to you?
- **Encoded (Bool):** Input — Do all five of these tests apply to you? 1. Your spouse died in 2023 or 2024 and you didn't remarry before the end of 2025 (if your spouse died in 2025, answer No). 2. You have a child or stepchild (not a foster child) whom you can claim as a dependent, or could claim as a dependent except that, for 2025, the child had gross income of $5,200 or more, the child filed a joint return, or you could be claimed as a dependent on someone else's return; an adopted child, including a child lawfully placed with you for legal adoption, is always your own child. 3. This child lived in your home for all of 2025, counting temporary absences by you or the child for special circumstances, such as school, vacation, business, medical care, military service or detention in a juvenile facility, as time lived in the home; a child born or who died in 2025, or adopted or lawfully placed with you for legal adoption in 2025, lived with you all year if your home was the child's home for the entire time the child was alive, or since the adoption or placement. 4. You paid over half the cost of keeping up your home (rent, mortgage interest, real estate taxes, insurance on the home, repairs, utilities and food eaten in the home; not clothing, education, medical treatment, vacations, life insurance, transportation or anyone’s services; amounts paid from a household member’s own funds, such as Social Security, count as paid by them). 5. You could have filed a joint return with your spouse the year your spouse died, even if you didn't actually do so.
- Expr: `{"op":"input","source":"Do all five of these tests apply to you? 1. Your spouse died in 2023 or 2024 and you didn't remarry before the end of 2025 (if your spouse died in 2025, answer No). 2. You have a child or stepchild (not a foster child) whom you can claim as a dependent, or could claim as a dependent except that, for 2025, the child had gross income of $5,200 or more, the child filed a joint return, or you could be claimed as a dependent on someone else's return; an adopted child, including a child lawfully placed with you for legal adoption, is always your own child. 3. This child lived in your home for all of 2025, counting temporary absences by you or the child for special circumstances, such as school, vacation, business, medical care, military service or detention in a juvenile facility, as time lived in the home; a child born or who died in 2025, or adopted or lawfully placed with you for legal adoption in 2025, lived with you all year if your home was the child's home for the entire time the child was alive, or since the adoption or placement. 4. You paid over half the cost of keeping up your home (rent, mortgage interest, real estate taxes, insurance on the home, repairs, utilities and food eaten in the home; not clothing, education, medical treatment, vacations, life insurance, transportation or anyone’s services; amounts paid from a household member’s own funds, such as Social Security, count as paid by them). 5. You could have filed a joint return with your spouse the year your spouse died, even if you didn't actually do so."}`
- Cite: [i1040gi] p. 15, Qualifying Surviving Spouse, "You can check the “Qualifying surviving spouse” box in the Filing Status section on page 1 of Form 1040 or 1040-SR and use joint return tax rates for 2025 if all of the following apply. 1. Your spouse died in 2023 or 2024 and you didn’t remarry before the end of 2025. 2. You have a child or stepchild (not a foster child) whom you can claim as a dependent or could claim as a dependent except that, for 2025: a. The child had gross income of $5,200 or more, b. The child filed a joint return, or c. You could be claimed as a dependent on someone else’s return." and "3. This child lived in your home for all of 2025. If the child didn’t live with you for the required time, see Exception to time lived with you, later. 4. You paid over half the cost of keeping up your home. 5. You could have filed a joint return with your spouse the year your spouse died, even if you didn’t actually do so."; "If your spouse died in 2025, you can't file as qualifying surviving spouse"; "An adopted child is always treated as your own child. An adopted child includes a child lawfully placed with you for legal adoption"; Exception to time lived with you, "Temporary absences by you or the child for special circumstances, such as school, vacation, business, medical care, military service, or detention in a juvenile facility, count as time lived in the home" and "A child is considered to have lived with you for all of 2025 if the child was born or died in 2025 and your home was the child’s home for the entire time the child was alive"; p501 p. 9, Note, "Amounts paid out of funds received in the child’s or qualifying person’s name, such as Social Security, are considered paid by the child, not you." (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `household.qss_fails`

- **Authored helper label:** Qualifying surviving spouse checked without meeting its tests
- **Encoded (Bool):** f1040 line Filing Status = 'qss' and helper "Do all five qualifying surviving spouse tests apply to you?" = false
- Expr: `{"all":[{"eq":["f1040.status",{"const":"qss"}],"op":"test"},{"eq":["household.qss_eligible",{"const":false}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 15, Qualifying Surviving Spouse, "use joint return tax rates for 2025 if all of the following apply" (2025; printed date 2026-02-25; sha256 482e9c48)

## (helper) — `household.rdp`

- **Authored helper label:** Were you a registered domestic partner in Nevada, Washington or California at any time in 2025?
- **Encoded (Bool):** Input — Were you a registered domestic partner in Nevada, Washington or California at any time in 2025?
- Expr: `{"op":"input","source":"Were you a registered domestic partner in Nevada, Washington or California at any time in 2025?"}`
- Cite: [i1040gi] p. 23, Community Property States, Nevada, Washington, and California domestic partners, "A registered domestic partner in Nevada, Washington, or California must generally report half the combined community income of the individual and their domestic partner" (2025; printed date 2026-02-25; sha256 482e9c48)

## (gate) — `household.rdp_community_property`

- **Authored helper label:** Not filing jointly, living in a community property state, and a registered domestic partner in Nevada, Washington or California
- **Encoded (Bool):** f1040 line Filing Status ≠ 'mfj' and helper "Did you live in a community property state at any time in 2025?" = true and helper "Were you a registered domestic partner in Nevada, Washington or California at any time in 2025?" = true
- Expr: `{"all":[{"ne":["f1040.status",{"const":"mfj"}],"op":"test"},{"eq":["household.community_property",{"const":true}],"op":"test"},{"eq":["household.rdp",{"const":true}],"op":"test"}],"op":"test"}`
- Cite: [i1040gi] p. 23, Community Property States, Nevada, Washington, and California domestic partners, "A registered domestic partner in Nevada, Washington, or California must generally report half the combined community income of the individual and their domestic partner. See Form 8958 and Pub. 555" (2025; printed date 2026-02-25; sha256 482e9c48)
