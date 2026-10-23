# Render comparison — household

The rendered English of every printed line of `Household facts for dependents and head of household` (`rendered/2025/household.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 35ac203fbe0e3f9b0cfa33f92670c3d285fd3572a0d4760dbc392fac0f0fedf6 |
| subject sha256 | a5bd6e3c9e95f8583342f999922ecc4572444abdc34430e88d691017d623522d |
| lines judged | 35 |
| match / mismatch / unclear / missing | 35 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 4, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 4, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| i1040s8812 | 2025; printed date 2026-01-23 | 2 | pages named by another document's citation | fd50a5266cc20aa5a31de0535658793f75c7abbb12fd83b65dc5b21c6ede2765 | 2 | e6ba91f54df679c9c19c23169c369f14bff012ba2fe110c3973bde59676c1d45 |

## Lines

### persons — Number of people on the return (you, and your spouse if filing jointly)
Status: **MATCH**

Model: Counts the people on the return: you, plus your spouse on a joint return. This matches how the instructions use "you, and your spouse if filing jointly" throughout.

### taxpayers — Number of entries for you
Status: **MATCH**

Model: Counts the entries for you. It is a roster check with no conflicting IRS text.

### spouses — Number of entries for your spouse
Status: **MATCH**

Model: Counts the entries for your spouse. It is a roster check with no conflicting IRS text.

### roster_ok — One entry for you, and one for your spouse exactly when filing jointly
Status: **MATCH**

Model: Requires one entry for each spouse on a joint return ("Married filing jointly") and only your own entry otherwise. The under-16 refusal is an owner-set entry check that names what it excludes, which narrows the line but does not misstate it.

### roster_bad — The people entered do not match the filing status
Status: **MATCH**

Model: This is the negation of roster_ok, as labeled.

### hsa_people — Number of people on the return with a Form 8889
Status: **MATCH**

Model: Counts the people with a Form 8889. This fits "If married filing jointly and both you and your spouse have HSAs, complete a separate Form 8889 for each of you."

### hsa_both — You and your spouse each have a Form 8889
Status: **MATCH**

Model: True when two people on the return each have a Form 8889, which is "Complete a separate Form 8889 for each spouse."

### hsa_split_count — Number of Forms 8889 using the spouse rule of line 6
Status: **MATCH**

Model: Counts the Forms 8889 that use the Line 6 rule for "Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025."

### hsa_agreed_count — Number of Forms 8889 using an agreed allocation
Status: **MATCH**

Model: Counts the Forms 8889 where the spouses "both agree on a different allocation" under the Line 6 rule.

### hsa_step1_sum — Both spouses Step 1 limits added together
Status: **MATCH**

Model: Adds each spouse's refigured Step 1 limit ("Refigure the contribution limit that would have been entered on line 5") under the Line 6 rule.

### hsa_share_sum — Both spouses parts of the Step 1 limit added together
Status: **MATCH**

Model: Adds each spouse's share after Steps 2 and 3, which lets the program check that the shares together equal the divided Step 1 limit.

### work_ssn_count — Number of people on the return with an SSN valid for employment
Status: **MATCH**

Model: Counts the people with an SSN "valid for employment and issued before the due date of your return."

### any_work_ssn — You, or your spouse if filing jointly, have an SSN valid for employment
Status: **MATCH**

Model: "If you are filing a joint return, only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC."

### eic_ssn_count — Number of people on the return with an SSN valid for the EIC
Status: **MATCH**

Model: Counts the people with a "social security number issued on or before the due date ... that allows you to work and is valid for EIC purposes."

### all_eic_ssn — You, and your spouse if filing jointly, have SSNs valid for the EIC
Status: **MATCH**

Model: Requires everyone on the return to have one: "Do you, and your spouse if filing a joint return, have a social security number ... valid for EIC purposes?"

### under16_count — Number of people on the return under age 16 at the end of 2025
Status: **MATCH**

Model: Counts the people on the return under age 16 at the end of 2025. This is an owner-defined entry check with no conflicting IRS text.

### filer_under16 — You, or your spouse if filing jointly, were under age 16 at the end of 2025
Status: **MATCH**

Model: True when anyone on the return was under 16. It serves as the gate for the owner's documented refusal.

### tin_count — Number of people on the return with an SSN or ITIN, or who have applied for an ITIN
Status: **MATCH**

Model: Counts the people with an SSN or ITIN, or who applied for an ITIN. This follows "Answer 'Yes' if you are applying for an ITIN on or before the return due date."

### all_tin — You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
Status: **MATCH**

Model: "Did you, and your spouse if filing a joint return, have either an SSN or ITIN issued on or before the due date of your 2025 return?"

### id_count — Number of people on the return with an SSN valid for employment or an SSN or ITIN
Status: **MATCH**

Model: Counts the people with a work-valid SSN or an SSN or ITIN. This is the identification count needed for the CTC rule.

### ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid 
Status: **MATCH**

Model: One spouse must have a valid SSN, and "The other spouse must have either an SSN or ITIN, and it must have been issued on or before the due date of the return."

### taxpayer_work_ssn_count — Your entry, if the answer is yes
Status: **MATCH**

Model: Counts your own entry when it has an SSN valid for employment issued before the due date. The label is odd, but the computation is correct.

### taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: True when your own entry has an SSN "valid for employment and issued before the due date of your return."

### home_cost — Did you pay over half the cost of keeping up your home for 2025?
Status: **MATCH**

Model: This is the Test 2 input: "You paid over half the cost of keeping up a home in which you lived."

### unmarried — Were you unmarried, or considered unmarried under the head of household rules, at the end 
Status: **MATCH**

Model: This is the input for "only if you are unmarried (or considered unmarried)."

### married — Were you married at the end of 2025?
Status: **MATCH**

Model: This is an input for being married at the end of 2025, including spouses considered unmarried for head of household. No IRS text conflicts with it.

### community_property — Did you live in a community property state at any time in 2025?
Status: **MATCH**

Model: The states listed match "Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington, and Wisconsin."

### hoh_community_property — Married, filing as head of household, and living in a community property state
Status: **MATCH**

Model: Gates the refusal for married head of household filers in community property states, where "you must usually follow state law ... see Form 8958 and Pub. 555."

### credit_disallowed — Was your EIC for a year after 1996, or your child tax credit, additional child tax credit 
Status: **MATCH**

Model: Restates the Form 8862 triggers: "EIC for a year after 1996 was reduced or disallowed" and "CTC, ACTC, or ODC for a year after 2015 was denied or reduced" other than for math or clerical error. It also includes the 2- and 10-year bans.

### test1_persons — Number of parents who qualify you under Test 1
Status: **MATCH**

Model: Counts the parents who qualify you under Test 1 ("Your parent didn't have to live with you"). Routing a parent who lives with you to Test 2 gives the same result, because Test 2 also requires that you paid over half the cost of your home.

### test2_persons — Number of persons who qualify you under Test 2
Status: **MATCH**

Model: Counts the Test 2 persons who "also lived for more than half of the year." The home-cost condition is tested separately in test2_met.

### test1_met — Test 1 met
Status: **MATCH**

Model: Test 1 applies when at least one parent qualifies under it.

### test2_met — Test 2 met, having paid over half the cost of keeping up your own home
Status: **MATCH**

Model: Test 2 applies when "You paid over half the cost of keeping up a home in which you lived" and at least one qualifying person lived there.

### hoh_eligible — Unmarried or considered unmarried, and Test 1 or Test 2 applies
Status: **MATCH**

Model: "Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies." The community property refusal names what it excludes.

### hoh_fails — Head of household checked without meeting its tests
Status: **MATCH**

Model: True when head of household is checked but the eligibility conditions are not met.

## Raw response

```yaml
```yaml
lines:
  - key: "persons"
    status: MATCH
    reason: "Counts the people on the return: you, plus your spouse on a joint return. This matches how the instructions use \"you, and your spouse if filing jointly\" throughout."
  - key: "taxpayers"
    status: MATCH
    reason: "Counts the entries for you. It is a roster check with no conflicting IRS text."
  - key: "spouses"
    status: MATCH
    reason: "Counts the entries for your spouse. It is a roster check with no conflicting IRS text."
  - key: "roster_ok"
    status: MATCH
    reason: "Requires one entry for each spouse on a joint return (\"Married filing jointly\") and only your own entry otherwise. The under-16 refusal is an owner-set entry check that names what it excludes, which narrows the line but does not misstate it."
  - key: "roster_bad"
    status: MATCH
    reason: "This is the negation of roster_ok, as labeled."
  - key: "hsa_people"
    status: MATCH
    reason: "Counts the people with a Form 8889. This fits \"If married filing jointly and both you and your spouse have HSAs, complete a separate Form 8889 for each of you.\""
  - key: "hsa_both"
    status: MATCH
    reason: "True when two people on the return each have a Form 8889, which is \"Complete a separate Form 8889 for each spouse.\""
  - key: "hsa_split_count"
    status: MATCH
    reason: "Counts the Forms 8889 that use the Line 6 rule for \"Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025.\""
  - key: "hsa_agreed_count"
    status: MATCH
    reason: "Counts the Forms 8889 where the spouses \"both agree on a different allocation\" under the Line 6 rule."
  - key: "hsa_step1_sum"
    status: MATCH
    reason: "Adds each spouse's refigured Step 1 limit (\"Refigure the contribution limit that would have been entered on line 5\") under the Line 6 rule."
  - key: "hsa_share_sum"
    status: MATCH
    reason: "Adds each spouse's share after Steps 2 and 3, which lets the program check that the shares together equal the divided Step 1 limit."
  - key: "work_ssn_count"
    status: MATCH
    reason: "Counts the people with an SSN \"valid for employment and issued before the due date of your return.\""
  - key: "any_work_ssn"
    status: MATCH
    reason: "\"If you are filing a joint return, only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC.\""
  - key: "eic_ssn_count"
    status: MATCH
    reason: "Counts the people with a \"social security number issued on or before the due date ... that allows you to work and is valid for EIC purposes.\""
  - key: "all_eic_ssn"
    status: MATCH
    reason: "Requires everyone on the return to have one: \"Do you, and your spouse if filing a joint return, have a social security number ... valid for EIC purposes?\""
  - key: "under16_count"
    status: MATCH
    reason: "Counts the people on the return under age 16 at the end of 2025. This is an owner-defined entry check with no conflicting IRS text."
  - key: "filer_under16"
    status: MATCH
    reason: "True when anyone on the return was under 16. It serves as the gate for the owner's documented refusal."
  - key: "tin_count"
    status: MATCH
    reason: "Counts the people with an SSN or ITIN, or who applied for an ITIN. This follows \"Answer 'Yes' if you are applying for an ITIN on or before the return due date.\""
  - key: "all_tin"
    status: MATCH
    reason: "\"Did you, and your spouse if filing a joint return, have either an SSN or ITIN issued on or before the due date of your 2025 return?\""
  - key: "id_count"
    status: MATCH
    reason: "Counts the people with a work-valid SSN or an SSN or ITIN. This is the identification count needed for the CTC rule."
  - key: "ctc_ssn"
    status: MATCH
    reason: "One spouse must have a valid SSN, and \"The other spouse must have either an SSN or ITIN, and it must have been issued on or before the due date of the return.\""
  - key: "taxpayer_work_ssn_count"
    status: MATCH
    reason: "Counts your own entry when it has an SSN valid for employment issued before the due date. The label is odd, but the computation is correct."
  - key: "taxpayer_work_ssn"
    status: MATCH
    reason: "True when your own entry has an SSN \"valid for employment and issued before the due date of your return.\""
  - key: "home_cost"
    status: MATCH
    reason: "This is the Test 2 input: \"You paid over half the cost of keeping up a home in which you lived.\""
  - key: "unmarried"
    status: MATCH
    reason: "This is the input for \"only if you are unmarried (or considered unmarried).\""
  - key: "married"
    status: MATCH
    reason: "This is an input for being married at the end of 2025, including spouses considered unmarried for head of household. No IRS text conflicts with it."
  - key: "community_property"
    status: MATCH
    reason: "The states listed match \"Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington, and Wisconsin.\""
  - key: "hoh_community_property"
    status: MATCH
    reason: "Gates the refusal for married head of household filers in community property states, where \"you must usually follow state law ... see Form 8958 and Pub. 555.\""
  - key: "credit_disallowed"
    status: MATCH
    reason: "Restates the Form 8862 triggers: \"EIC for a year after 1996 was reduced or disallowed\" and \"CTC, ACTC, or ODC for a year after 2015 was denied or reduced\" other than for math or clerical error. It also includes the 2- and 10-year bans."
  - key: "test1_persons"
    status: MATCH
    reason: "Counts the parents who qualify you under Test 1 (\"Your parent didn't have to live with you\"). Routing a parent who lives with you to Test 2 gives the same result, because Test 2 also requires that you paid over half the cost of your home."
  - key: "test2_persons"
    status: MATCH
    reason: "Counts the Test 2 persons who \"also lived for more than half of the year.\" The home-cost condition is tested separately in test2_met."
  - key: "test1_met"
    status: MATCH
    reason: "Test 1 applies when at least one parent qualifies under it."
  - key: "test2_met"
    status: MATCH
    reason: "Test 2 applies when \"You paid over half the cost of keeping up a home in which you lived\" and at least one qualifying person lived there."
  - key: "hoh_eligible"
    status: MATCH
    reason: "\"Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies.\" The community property refusal names what it excludes."
  - key: "hoh_fails"
    status: MATCH
    reason: "True when head of household is checked but the eligibility conditions are not met."
```
```
