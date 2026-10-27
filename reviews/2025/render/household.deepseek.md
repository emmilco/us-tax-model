# Render comparison — household

The rendered English of every printed line of `Household facts for dependents and head of household` (`rendered/2025/household.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-26 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 1513fe523a89ee55045d41da5da479ee6779f21a3d3675ef034492fe04d46d93 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 28881dbede57c2da28839a93115eb41254ae1845f441f47979304319ce659bfc |
| lines judged | 35 |
| match / mismatch / unclear / missing | 34 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 2, 4, 5, 6, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 2, 4, 5, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |
| f8889 | 2025; created 2025-03-28 | 1 | whole document | f1ae3589453f3dd1d5277a79409bd7d0bf4772715fa8bd11d58126e6f387c0cf | - | 85ba6183eb2c35cf7b6d63eb6fd515be7234f5f938da39d7d000a6a7f2359d4e |
| i1040s8812 | 2025; printed date 2026-01-23 | 2 | pages named by another document's citation | fd50a5266cc20aa5a31de0535658793f75c7abbb12fd83b65dc5b21c6ede2765 | 2 | e6ba91f54df679c9c19c23169c369f14bff012ba2fe110c3973bde59676c1d45 |

## Lines

### persons — Number of people on the return (you, and your spouse if filing jointly)
Status: **MATCH**

Model: Counts the taxpayer and, on a joint return, the spouse, which is the set of people on the return as defined for this helper.

### taxpayers — Number of entries for you
Status: **MATCH**

Model: Counts the confirmed entries identified as the taxpayer's entry.

### spouses — Number of entries for your spouse
Status: **MATCH**

Model: Counts the confirmed entries identified as the spouse's entry.

### roster_ok — One entry for you, and one for your spouse exactly when filing jointly
Status: **MATCH**

Model: Requires one taxpayer entry and one spouse entry exactly for married filing jointly; the under-16 refusal is an allowed narrowing.

### roster_bad — The people entered do not match the filing status
Status: **MATCH**

Model: Negates the roster-ok result, so it flags a roster that does not match the filing status.

### hsa_people — Number of people on the return with a Form 8889
Status: **MATCH**

Model: Counts confirmed people with at least one Form 8889, matching the Form 8889 separate-form-per-spouse rule.

### hsa_both — You and your spouse each have a Form 8889
Status: **MATCH**

Model: True when exactly two people on the return have a Form 8889, i.e. both spouses each have one.

### hsa_split_count — Number of Forms 8889 using the spouse rule of line 6
Status: **MATCH**

Model: Counts Form 8889 entries using the spouse rule for separate HSAs with family coverage, matching Form 8889 line 6.

### hsa_agreed_count — Number of Forms 8889 using an agreed allocation
Status: **MATCH**

Model: Counts Form 8889 entries using an agreed allocation under the line 6 spouse rule.

### hsa_step1_sum — Both spouses Step 1 limits added together
Status: **MATCH**

Model: Adds the Step 1 refigured line 5 amounts under the line 6 spouse rule.

### hsa_share_sum — Both spouses parts of the Step 1 limit added together
Status: **MATCH**

Model: Adds each spouse's Step 2/3 part of the Step 1 limit under the line 6 spouse rule.

### work_ssn_count — Number of people on the return with an SSN valid for employment
Status: **MATCH**

Model: Counts confirmed people with an SSN valid for employment issued before the due date, matching the CTC SSN definition.

### any_work_ssn — You, or your spouse if filing jointly, have an SSN valid for employment
Status: **MATCH**

Model: True if any taxpayer or joint spouse has a work-valid SSN, matching the CTC rule that only one spouse need have one.

### eic_ssn_count — Number of people on the return with an SSN valid for the EIC
Status: **MATCH**

Model: Counts confirmed people with an EIC-valid SSN issued by the due date, matching the EIC SSN requirement.

### all_eic_ssn — You, and your spouse if filing jointly, have SSNs valid for the EIC
Status: **MATCH**

Model: Requires each taxpayer and joint spouse to have an EIC-valid SSN, matching the EIC Step 1 requirement.

### under16_count — Number of people on the return under age 16 at the end of 2025
Status: **MATCH**

Model: Counts confirmed people whose under-16 answer is true; the under-16 fact is used for the stated refusal.

### filer_under16 — You, or your spouse if filing jointly, were under age 16 at the end of 2025
Status: **MATCH**

Model: True when any taxpayer or joint spouse is under 16, matching the helper label and the refusal gate.

### tin_count — Number of people on the return with an SSN or ITIN, or who have applied for an ITIN
Status: **MATCH**

Model: Counts confirmed people with an SSN or ITIN or an ITIN application, matching the helper definition.

### all_tin — You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
Status: **MATCH**

Model: Requires each taxpayer and joint spouse to have an SSN/ITIN or ITIN application, matching the ODC identification rule.

### id_count — Number of people on the return with an SSN valid for employment or an SSN or ITIN
Status: **MATCH**

Model: Counts confirmed people with a work-valid SSN or an SSN/ITIN, matching the helper's stated definition.

### ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid
Status: **MATCH**

Model: Checks that at least one taxpayer or joint spouse has a work-valid SSN and the other person on the return has SSN or ITIN, matching the taxpayer/spouse CTC identification rule.

### taxpayer_work_ssn_count — Your entry, if the answer is yes
Status: **MATCH**

Model: Counts the taxpayer entry when the work-valid SSN answer is yes.

### taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: True when the taxpayer's work-valid SSN count is positive.

### home_cost — Did you pay over half the cost of keeping up your home for 2025?
Status: **MATCH**

Model: Directly asks whether the filer paid over half the cost of keeping up the home, matching the HOH home-cost condition.

### unmarried — Were you unmarried, or considered unmarried under the head of household rules, at the end
Status: **MATCH**

Model: Directly asks whether the filer was unmarried or considered unmarried under the HOH rules.

### married — Were you married at the end of 2025?
Status: **MATCH**

Model: Directly asks whether the filer was married at the end of 2025, including married but considered unmarried for HOH status.

### community_property — Did you live in a community property state at any time in 2025?
Status: **MATCH**

Model: Uses the IRS list of community property states and asks whether the filer lived in one during 2025.

### hoh_community_property — Married, filing as head of household, and living in a community property state
Status: **MATCH**

Model: Flags a married head-of-household filer in a community property state, matching the community income concern identified in the IRS text.

### credit_disallowed — Was your EIC for a year after 1996, or your child tax credit, additional child tax credit
Status: **MATCH**

Model: Combines the EIC and CTC/ACTC/ODC disallowance facts and the 2- or 10-year period, consistent with the IRS Form 8862 and CTC instructions.

### test1_persons — Number of parents who qualify you under Test 1
Status: **MATCH**

Model: The helper narrows Test 1 to non-co-resident parents and expressly routes a parent who lives with you to Test 2, so the supported cases are handled under the IRS alternatives.

### test2_persons — Number of persons who qualify you under Test 2
Status: **MISMATCH**

Restated: Add dependent.one over every confirmed dependent entry for which helper "A Test 2 person who lived with you more than half the year, or of the part of the year a relative was alive (the home-cost condition of Test 2 is tested on the household form)" = true, within the current person when parent-bound. An unanswered roster is unknown.

Model: The restatement counts only confirmed dependent entries, but IRS Test 2 expressly includes 'Your unmarried qualifying child who isn’t your dependent' and other qualifying children who are not dependents.

Ruling: model error; the model read "every confirmed dependent entry" as every person who is your dependent. It is the renderer's wording for every entry of the dependent collection (every person listed, as the round-1 ruling on the same text found), and the helper dependent.hoh_test2 it sums has a second branch for "Your unmarried qualifying child who isn't your dependent" (i1040gi p. 14, Test 2, item 2): qualifying_child, not married, lived with you more than half the year, with no dependency condition. Items 3 and 4 (a married child not your dependent only because you can be claimed, and the custodial parent's released child) are refused through dependent.married and dependent.divorced_rule.

### test1_met — Test 1 met
Status: **MATCH**

Model: True when the Test 1 parent count is positive, matching 'Test 1 met'.

### test2_met — Test 2 met, having paid over half the cost of keeping up your own home
Status: **MATCH**

Model: Requires both home cost and a Test 2 person, matching the IRS Test 2 home-and-person conditions.

### hoh_eligible — Unmarried or considered unmarried, and Test 1 or Test 2 applies
Status: **MATCH**

Model: Requires unmarried or considered unmarried plus Test 1 or Test 2, matching the IRS HOH filing-status rule.

### hoh_fails — Head of household checked without meeting its tests
Status: **MATCH**

Model: Flags an HOH filing status when the HOH eligibility test is false, matching the IRS requirement that HOH be checked only if the tests apply.

## Raw response

```yaml
lines:
  - key: "persons"
    status: MATCH
    reason: "Counts the taxpayer and, on a joint return, the spouse, which is the set of people on the return as defined for this helper."
  - key: "taxpayers"
    status: MATCH
    reason: "Counts the confirmed entries identified as the taxpayer's entry."
  - key: "spouses"
    status: MATCH
    reason: "Counts the confirmed entries identified as the spouse's entry."
  - key: "roster_ok"
    status: MATCH
    reason: "Requires one taxpayer entry and one spouse entry exactly for married filing jointly; the under-16 refusal is an allowed narrowing."
  - key: "roster_bad"
    status: MATCH
    reason: "Negates the roster-ok result, so it flags a roster that does not match the filing status."
  - key: "hsa_people"
    status: MATCH
    reason: "Counts confirmed people with at least one Form 8889, matching the Form 8889 separate-form-per-spouse rule."
  - key: "hsa_both"
    status: MATCH
    reason: "True when exactly two people on the return have a Form 8889, i.e. both spouses each have one."
  - key: "hsa_split_count"
    status: MATCH
    reason: "Counts Form 8889 entries using the spouse rule for separate HSAs with family coverage, matching Form 8889 line 6."
  - key: "hsa_agreed_count"
    status: MATCH
    reason: "Counts Form 8889 entries using an agreed allocation under the line 6 spouse rule."
  - key: "hsa_step1_sum"
    status: MATCH
    reason: "Adds the Step 1 refigured line 5 amounts under the line 6 spouse rule."
  - key: "hsa_share_sum"
    status: MATCH
    reason: "Adds each spouse's Step 2/3 part of the Step 1 limit under the line 6 spouse rule."
  - key: "work_ssn_count"
    status: MATCH
    reason: "Counts confirmed people with an SSN valid for employment issued before the due date, matching the CTC SSN definition."
  - key: "any_work_ssn"
    status: MATCH
    reason: "True if any taxpayer or joint spouse has a work-valid SSN, matching the CTC rule that only one spouse need have one."
  - key: "eic_ssn_count"
    status: MATCH
    reason: "Counts confirmed people with an EIC-valid SSN issued by the due date, matching the EIC SSN requirement."
  - key: "all_eic_ssn"
    status: MATCH
    reason: "Requires each taxpayer and joint spouse to have an EIC-valid SSN, matching the EIC Step 1 requirement."
  - key: "under16_count"
    status: MATCH
    reason: "Counts confirmed people whose under-16 answer is true; the under-16 fact is used for the stated refusal."
  - key: "filer_under16"
    status: MATCH
    reason: "True when any taxpayer or joint spouse is under 16, matching the helper label and the refusal gate."
  - key: "tin_count"
    status: MATCH
    reason: "Counts confirmed people with an SSN or ITIN or an ITIN application, matching the helper definition."
  - key: "all_tin"
    status: MATCH
    reason: "Requires each taxpayer and joint spouse to have an SSN/ITIN or ITIN application, matching the ODC identification rule."
  - key: "id_count"
    status: MATCH
    reason: "Counts confirmed people with a work-valid SSN or an SSN/ITIN, matching the helper's stated definition."
  - key: "ctc_ssn"
    status: MATCH
    reason: "Checks that at least one taxpayer or joint spouse has a work-valid SSN and the other person on the return has SSN or ITIN, matching the taxpayer/spouse CTC identification rule."
  - key: "taxpayer_work_ssn_count"
    status: MATCH
    reason: "Counts the taxpayer entry when the work-valid SSN answer is yes."
  - key: "taxpayer_work_ssn"
    status: MATCH
    reason: "True when the taxpayer's work-valid SSN count is positive."
  - key: "home_cost"
    status: MATCH
    reason: "Directly asks whether the filer paid over half the cost of keeping up the home, matching the HOH home-cost condition."
  - key: "unmarried"
    status: MATCH
    reason: "Directly asks whether the filer was unmarried or considered unmarried under the HOH rules."
  - key: "married"
    status: MATCH
    reason: "Directly asks whether the filer was married at the end of 2025, including married but considered unmarried for HOH status."
  - key: "community_property"
    status: MATCH
    reason: "Uses the IRS list of community property states and asks whether the filer lived in one during 2025."
  - key: "hoh_community_property"
    status: MATCH
    reason: "Flags a married head-of-household filer in a community property state, matching the community income concern identified in the IRS text."
  - key: "credit_disallowed"
    status: MATCH
    reason: "Combines the EIC and CTC/ACTC/ODC disallowance facts and the 2- or 10-year period, consistent with the IRS Form 8862 and CTC instructions."
  - key: "test1_persons"
    status: MATCH
    reason: "The helper narrows Test 1 to non-co-resident parents and expressly routes a parent who lives with you to Test 2, so the supported cases are handled under the IRS alternatives."
  - key: "test2_persons"
    status: MISMATCH
    reason: "The restatement counts only confirmed dependent entries, but IRS Test 2 expressly includes 'Your unmarried qualifying child who isn’t your dependent' and other qualifying children who are not dependents."
  - key: "test1_met"
    status: MATCH
    reason: "True when the Test 1 parent count is positive, matching 'Test 1 met'."
  - key: "test2_met"
    status: MATCH
    reason: "Requires both home cost and a Test 2 person, matching the IRS Test 2 home-and-person conditions."
  - key: "hoh_eligible"
    status: MATCH
    reason: "Requires unmarried or considered unmarried plus Test 1 or Test 2, matching the IRS HOH filing-status rule."
  - key: "hoh_fails"
    status: MATCH
    reason: "Flags an HOH filing status when the HOH eligibility test is false, matching the IRS requirement that HOH be checked only if the tests apply."
```
