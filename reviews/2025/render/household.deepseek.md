# Render comparison — household

The rendered English of every printed line of `Household facts for dependents and head of household` (`rendered/2025/household.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 35ac203fbe0e3f9b0cfa33f92670c3d285fd3572a0d4760dbc392fac0f0fedf6 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | a5bd6e3c9e95f8583342f999922ecc4572444abdc34430e88d691017d623522d |
| lines judged | 35 |
| match / mismatch / unclear / missing | 31 / 4 / 0 / 0 |
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

Model: Counts one for each confirmed person entry, corresponding to you and your spouse if filing jointly; an unanswered roster is treated as unknown.

### taxpayers — Number of entries for you
Status: **MATCH**

Model: Counts confirmed person entries marked as the taxpayer's entry, matching the roster role split.

### spouses — Number of entries for your spouse
Status: **MATCH**

Model: Counts confirmed person entries marked as the spouse's entry, matching the roster role split.

### roster_ok — One entry for you, and one for your spouse exactly when filing jointly
Status: **MATCH**

Model: Requires one taxpayer entry and one spouse entry only for MFJ; the under-16 refusal names the excluded case.

### roster_bad — The people entered do not match the filing status
Status: **MATCH**

Model: Correctly negates roster_ok.

### hsa_people — Number of people on the return with a Form 8889
Status: **MATCH**

Model: Counts people with a Form 8889; the IRS requires a separate Form 8889 for each spouse with an HSA.

### hsa_both — You and your spouse each have a Form 8889
Status: **MISMATCH**

Restated: helper "Number of people on the return with a Form 8889" = 2 (a count)

Model: It detects both spouses only through hsa_people = 2, which counts people on the return; the IRS says the family-coverage spouse rule applies regardless of whether spouses file jointly or separately.

Ruling: open

### hsa_split_count — Number of Forms 8889 using the spouse rule of line 6
Status: **MATCH**

Model: Counts Forms 8889 using the line 6 spouse rule when spouses have separate HSAs and family coverage at any time.

### hsa_agreed_count — Number of Forms 8889 using an agreed allocation
Status: **MATCH**

Model: Counts Forms 8889 using an agreed allocation, which the line 6 spouse rule permits.

### hsa_step1_sum — Both spouses Step 1 limits added together
Status: **MISMATCH**

Restated: Add person.hsa_step1 over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: It adds both spouses' Step 1 limits, but IRS line 6 Step 2 says to divide the refigured contribution limit from Step 1 equally between you and your spouse.

Ruling: open

### hsa_share_sum — Both spouses parts of the Step 1 limit added together
Status: **MATCH**

Model: Sums the spouses' parts of the Step 1 limit, consistent with the line 6 division of that limit.

### work_ssn_count — Number of people on the return with an SSN valid for employment
Status: **MATCH**

Model: Counts persons with an SSN valid for employment issued before the due date, as used for the CTC identification rule.

### any_work_ssn — You, or your spouse if filing jointly, have an SSN valid for employment
Status: **MATCH**

Model: Returns true when at least one person has a valid work SSN, matching the joint-return CTC rule that only one spouse need have a valid SSN.

### eic_ssn_count — Number of people on the return with an SSN valid for the EIC
Status: **MATCH**

Model: Counts persons with an SSN valid for the EIC issued on or before the due date.

### all_eic_ssn — You, and your spouse if filing jointly, have SSNs valid for the EIC
Status: **MATCH**

Model: Checks that you, and your spouse if filing jointly, each have an EIC-valid SSN.

### under16_count — Number of people on the return under age 16 at the end of 2025
Status: **MATCH**

Model: Counts persons on the return who were under age 16 at the end of 2025.

### filer_under16 — You, or your spouse if filing jointly, were under age 16 at the end of 2025
Status: **MATCH**

Model: Returns true when you, or your spouse if filing jointly, are under age 16 at the end of 2025.

### tin_count — Number of people on the return with an SSN or ITIN, or who have applied for an ITIN
Status: **MATCH**

Model: Counts persons with an SSN or ITIN issued on or before the due date, or an applied-for ITIN, matching the credit identification rules.

### all_tin — You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
Status: **MATCH**

Model: Checks that you, and your spouse if filing jointly, each have an SSN or ITIN, or have applied for an ITIN.

### id_count — Number of people on the return with an SSN valid for employment or an SSN or ITIN
Status: **MATCH**

Model: Counts persons with a valid work SSN or an SSN/ITIN issued by the due date.

### ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid 
Status: **MATCH**

Model: Requires at least one valid work SSN and that each other taxpayer/spouse has a work SSN or SSN/ITIN, matching the CTC identification rule.

### taxpayer_work_ssn_count — Your entry, if the answer is yes
Status: **MATCH**

Model: Counts the taxpayer entry when the work-SSN answer is yes.

### taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: Returns true when the taxpayer entry has a work SSN issued before the due date.

### home_cost — Did you pay over half the cost of keeping up your home for 2025?
Status: **MATCH**

Model: Asks whether the filer paid over half the cost of keeping up the home for 2025, matching the home-cost condition used in the HOH tests.

### unmarried — Were you unmarried, or considered unmarried under the head of household rules, at the end 
Status: **MATCH**

Model: Asks whether the filer was unmarried or considered unmarried under the head of household rules at the end of 2025.

### married — Were you married at the end of 2025?
Status: **MATCH**

Model: Asks whether the filer was married at the end of 2025, including married but considered unmarried for HOH.

### community_property — Did you live in a community property state at any time in 2025?
Status: **MATCH**

Model: Uses the IRS list of community property states and asks whether the filer lived in one in 2025.

### hoh_community_property — Married, filing as head of household, and living in a community property state
Status: **MATCH**

Model: Flags a married HOH filer in a community property state, matching the Form 8958/Pub. 555 refusal condition.

### credit_disallowed — Was your EIC for a year after 1996, or your child tax credit, additional child tax credit 
Status: **MATCH**

Model: Tracks the EIC after-1996 and CTC/ACTC/ODC after-2015 disallowance rules, including 2- and 10-year periods.

### test1_persons — Number of parents who qualify you under Test 1
Status: **MISMATCH**

Restated: Add dependent.one over every confirmed dependent entry for which helper "Qualifies you for head of household under Test 1 through a parent who does not live with you (a parent who lives with you qualifies you through Test 2)" = true, within the current person when parent-bound. An unanswered roster is unknown.

Model: It excludes a parent who lives with the filer from Test 1, but the IRS says 'Your parent didn’t have to live with you.'

Ruling: open

### test2_persons — Number of persons who qualify you under Test 2
Status: **MATCH**

Model: Counts Test 2 persons who lived with the filer more than half the year, with the home-cost condition handled separately.

### test1_met — Test 1 met
Status: **MISMATCH**

Restated: helper "Number of parents who qualify you under Test 1" > 0 (a count)

Model: Because it depends on test1_persons, it can be false when IRS Test 1 is met by a parent who lives with the filer; the IRS says 'Your parent didn’t have to live with you.'

Ruling: open

### test2_met — Test 2 met, having paid over half the cost of keeping up your own home
Status: **MATCH**

Model: Requires both the home-cost condition and at least one Test 2 person who lived with the filer more than half the year.

### hoh_eligible — Unmarried or considered unmarried, and Test 1 or Test 2 applies
Status: **MATCH**

Model: Requires unmarried or considered-unmarried status and Test 1 or Test 2, matching the IRS head of household rule.

### hoh_fails — Head of household checked without meeting its tests
Status: **MATCH**

Model: Flags a HOH filing status when the HOH tests are not met, matching the instruction to check HOH only if the tests apply.

## Raw response

```yaml
lines:
  - key: "persons"
    status: MATCH
    reason: "Counts one for each confirmed person entry, corresponding to you and your spouse if filing jointly; an unanswered roster is treated as unknown."
  - key: "taxpayers"
    status: MATCH
    reason: "Counts confirmed person entries marked as the taxpayer's entry, matching the roster role split."
  - key: "spouses"
    status: MATCH
    reason: "Counts confirmed person entries marked as the spouse's entry, matching the roster role split."
  - key: "roster_ok"
    status: MATCH
    reason: "Requires one taxpayer entry and one spouse entry only for MFJ; the under-16 refusal names the excluded case."
  - key: "roster_bad"
    status: MATCH
    reason: "Correctly negates roster_ok."
  - key: "hsa_people"
    status: MATCH
    reason: "Counts people with a Form 8889; the IRS requires a separate Form 8889 for each spouse with an HSA."
  - key: "hsa_both"
    status: MISMATCH
    reason: "It detects both spouses only through hsa_people = 2, which counts people on the return; the IRS says the family-coverage spouse rule applies regardless of whether spouses file jointly or separately."
  - key: "hsa_split_count"
    status: MATCH
    reason: "Counts Forms 8889 using the line 6 spouse rule when spouses have separate HSAs and family coverage at any time."
  - key: "hsa_agreed_count"
    status: MATCH
    reason: "Counts Forms 8889 using an agreed allocation, which the line 6 spouse rule permits."
  - key: "hsa_step1_sum"
    status: MISMATCH
    reason: "It adds both spouses' Step 1 limits, but IRS line 6 Step 2 says to divide the refigured contribution limit from Step 1 equally between you and your spouse."
  - key: "hsa_share_sum"
    status: MATCH
    reason: "Sums the spouses' parts of the Step 1 limit, consistent with the line 6 division of that limit."
  - key: "work_ssn_count"
    status: MATCH
    reason: "Counts persons with an SSN valid for employment issued before the due date, as used for the CTC identification rule."
  - key: "any_work_ssn"
    status: MATCH
    reason: "Returns true when at least one person has a valid work SSN, matching the joint-return CTC rule that only one spouse need have a valid SSN."
  - key: "eic_ssn_count"
    status: MATCH
    reason: "Counts persons with an SSN valid for the EIC issued on or before the due date."
  - key: "all_eic_ssn"
    status: MATCH
    reason: "Checks that you, and your spouse if filing jointly, each have an EIC-valid SSN."
  - key: "under16_count"
    status: MATCH
    reason: "Counts persons on the return who were under age 16 at the end of 2025."
  - key: "filer_under16"
    status: MATCH
    reason: "Returns true when you, or your spouse if filing jointly, are under age 16 at the end of 2025."
  - key: "tin_count"
    status: MATCH
    reason: "Counts persons with an SSN or ITIN issued on or before the due date, or an applied-for ITIN, matching the credit identification rules."
  - key: "all_tin"
    status: MATCH
    reason: "Checks that you, and your spouse if filing jointly, each have an SSN or ITIN, or have applied for an ITIN."
  - key: "id_count"
    status: MATCH
    reason: "Counts persons with a valid work SSN or an SSN/ITIN issued by the due date."
  - key: "ctc_ssn"
    status: MATCH
    reason: "Requires at least one valid work SSN and that each other taxpayer/spouse has a work SSN or SSN/ITIN, matching the CTC identification rule."
  - key: "taxpayer_work_ssn_count"
    status: MATCH
    reason: "Counts the taxpayer entry when the work-SSN answer is yes."
  - key: "taxpayer_work_ssn"
    status: MATCH
    reason: "Returns true when the taxpayer entry has a work SSN issued before the due date."
  - key: "home_cost"
    status: MATCH
    reason: "Asks whether the filer paid over half the cost of keeping up the home for 2025, matching the home-cost condition used in the HOH tests."
  - key: "unmarried"
    status: MATCH
    reason: "Asks whether the filer was unmarried or considered unmarried under the head of household rules at the end of 2025."
  - key: "married"
    status: MATCH
    reason: "Asks whether the filer was married at the end of 2025, including married but considered unmarried for HOH."
  - key: "community_property"
    status: MATCH
    reason: "Uses the IRS list of community property states and asks whether the filer lived in one in 2025."
  - key: "hoh_community_property"
    status: MATCH
    reason: "Flags a married HOH filer in a community property state, matching the Form 8958/Pub. 555 refusal condition."
  - key: "credit_disallowed"
    status: MATCH
    reason: "Tracks the EIC after-1996 and CTC/ACTC/ODC after-2015 disallowance rules, including 2- and 10-year periods."
  - key: "test1_persons"
    status: MISMATCH
    reason: "It excludes a parent who lives with the filer from Test 1, but the IRS says 'Your parent didn’t have to live with you.'"
  - key: "test2_persons"
    status: MATCH
    reason: "Counts Test 2 persons who lived with the filer more than half the year, with the home-cost condition handled separately."
  - key: "test1_met"
    status: MISMATCH
    reason: "Because it depends on test1_persons, it can be false when IRS Test 1 is met by a parent who lives with the filer; the IRS says 'Your parent didn’t have to live with you.'"
  - key: "test2_met"
    status: MATCH
    reason: "Requires both the home-cost condition and at least one Test 2 person who lived with the filer more than half the year."
  - key: "hoh_eligible"
    status: MATCH
    reason: "Requires unmarried or considered-unmarried status and Test 1 or Test 2, matching the IRS head of household rule."
  - key: "hoh_fails"
    status: MATCH
    reason: "Flags a HOH filing status when the HOH tests are not met, matching the instruction to check HOH only if the tests apply."
```
