# Household facts for dependents and head of household

- Document: `household` (form, tax year 2025)
- Note: Facts about the people on the return that the dependent tests, the credits and the head of household status read; "unmarried" here is the instructions' unmarried or considered unmarried at the end of 2025.

## (helper) — `household.persons`

- **Authored helper label:** Number of people on the return (you, and your spouse if filing jointly)
- **Encoded (Count):** Add person.one over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over"}`
- Cite: [f1040] Form 1040 (2025), page 1, "Your first name and middle initial" and "If joint return, spouse’s first name and middle initial"; Filing Status (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `household.taxpayers`

- **Authored helper label:** Number of entries for you
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'taxpayer', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"eq":["person.role",{"const":"taxpayer"}],"op":"test"}}`
- Cite: [f1040] Form 1040 (2025), page 1, "Your first name and middle initial" and "If joint return, spouse’s first name and middle initial"; Filing Status (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `household.spouses`

- **Authored helper label:** Number of entries for your spouse
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'spouse', within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"eq":["person.role",{"const":"spouse"}],"op":"test"}}`
- Cite: [f1040] Form 1040 (2025), page 1, "Your first name and middle initial" and "If joint return, spouse’s first name and middle initial"; Filing Status (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `household.roster_ok`

- **Authored helper label:** One entry for you, and one for your spouse exactly when filing jointly
- **Encoded (Bool):** (f1040 line Filing Status = 'mfj' and helper "Number of entries for you" = 1 (a count) and helper "Number of entries for your spouse" = 1 (a count) or f1040 line Filing Status ≠ 'mfj' and helper "Number of entries for you" = 1 (a count) and helper "Number of entries for your spouse" = 0 (a count))
- **Refusal:** when household.filer_under16 is true, cannot complete A filer under age 16 at the end of 2025. A return for a person under age 16 at the end of 2025 (you, or your spouse on a joint return) is outside this tool. The archived instructions state no such rule; this is an entry check the owner decided on, recorded in the ambiguity register (amb.2025.filer_under_16). Cite: [i1040gi] p. 66, Self-Select PIN, "You can’t use the Self-Select PIN method if you are a first-time filer under age 16 at the end of 2025" (2025; printed date 2026-02-25; sha256 482e9c48)
- Expr: `{"any":[{"all":[{"eq":["f1040.status",{"const":"mfj"}],"op":"test"},{"eq":["household.taxpayers",{"const":1,"type":"Count"}],"op":"test"},{"eq":["household.spouses",{"const":1,"type":"Count"}],"op":"test"}],"op":"test"},{"all":[{"ne":["f1040.status",{"const":"mfj"}],"op":"test"},{"eq":["household.taxpayers",{"const":1,"type":"Count"}],"op":"test"},{"eq":["household.spouses",{"const":0,"type":"Count"}],"op":"test"}],"op":"test"}],"op":"test"}`
- Cite: [f1040] Form 1040 (2025), page 1, "Your first name and middle initial" and "If joint return, spouse’s first name and middle initial"; Filing Status (2025; created 2025-09-05; sha256 3d31c226)

## (gate) — `household.roster_bad`

- **Authored helper label:** The people entered do not match the filing status
- **Encoded (Bool):** helper "One entry for you, and one for your spouse exactly when filing jointly" = false
- Expr: `{"eq":["household.roster_ok",{"const":false}],"op":"test"}`
- Cite: [f1040] Form 1040 (2025), page 1, "Your first name and middle initial" and "If joint return, spouse’s first name and middle initial"; Filing Status (2025; created 2025-09-05; sha256 3d31c226)

## (helper) — `household.hsa_people`

- **Authored helper label:** Number of people on the return with a Form 8889
- **Encoded (Count):** Add person.one over every confirmed person entry for which helper "Number of Forms 8889 entered for this person" > 0 (a count), within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.one","op":"sum_over","where":{"gt":["person.hsa_forms",{"const":0,"type":"Count"}],"op":"test"}}`
- Cite: [i8889] p. 4, Name and social security number (SSN), "If married filing jointly and both you and your spouse have HSAs, complete a separate Form 8889 for each of you" (2025; sha256 da6f2f58)

## (helper) — `household.hsa_both`

- **Authored helper label:** You and your spouse each have a Form 8889
- **Encoded (Bool):** helper "Number of people on the return with a Form 8889" = 2 (a count)
- Expr: `{"eq":["household.hsa_people",{"const":2,"type":"Count"}],"op":"test"}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025; Steps 1 to 3 (2025; sha256 da6f2f58)

## (helper) — `household.hsa_split_count`

- **Authored helper label:** Number of Forms 8889 using the spouse rule of line 6
- **Encoded (Count):** Add person.hsa_split over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.hsa_split","op":"sum_over"}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025; Steps 1 to 3 (2025; sha256 da6f2f58)

## (helper) — `household.hsa_agreed_count`

- **Authored helper label:** Number of Forms 8889 using an agreed allocation
- **Encoded (Count):** Add person.hsa_agreed over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.hsa_agreed","op":"sum_over"}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025; Steps 1 to 3 (2025; sha256 da6f2f58)

## (helper) — `household.hsa_step1_sum`

- **Authored helper label:** Both spouses Step 1 limits added together
- **Encoded (NonNegDollars):** Add person.hsa_step1 over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.hsa_step1","op":"sum_over"}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025; Steps 1 to 3 (2025; sha256 da6f2f58)

## (helper) — `household.hsa_share_sum`

- **Authored helper label:** Both spouses parts of the Step 1 limit added together
- **Encoded (NonNegDollars):** Add person.hsa_share over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.
- Expr: `{"collection":"person","field":"person.hsa_share","op":"sum_over"}`
- Cite: [i8889] p. 7, Line 6, Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025; Steps 1 to 3 (2025; sha256 da6f2f58)

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
- **Encoded (Bool):** Input — Did you pay over half the cost of keeping up your home for 2025?
- Expr: `{"op":"input","source":"Did you pay over half the cost of keeping up your home for 2025?"}`
- Cite: [i1040gi] p. 14, Head of Household, Test 2 (2025; printed date 2026-02-25; sha256 482e9c48)

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
- **Encoded (Count):** Add dependent.one over every confirmed dependent entry for which helper "A Test 2 person who lived with you more than half the year (the home-cost condition of Test 2 is tested on the household form)" = true, within the current person when parent-bound. An unanswered roster is unknown.
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
