# Render comparison — household

The rendered English of every printed line of `Household facts for dependents and head of household` (`rendered/2025/household.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-31 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | fbd4b937cad4b2ded7217bd601c23cd838c2c54ca2106b75558244e9e2b042f4 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 0f13b65328288794688ba841bdb9a9f05903cfcd2c86461b6b70e636123ccaee |
| lines judged | 41 |
| match / mismatch / unclear / missing | 41 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14, 15, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 15, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 2, 4, 5, 6, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 2, 4, 5, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| p501 | 2025 returns; PDF created 2026-02-04 | 9, 11 | cited pages | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 11 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |
| f8889 | 2025; created 2025-03-28 | 1 | whole document | f1ae3589453f3dd1d5277a79409bd7d0bf4772715fa8bd11d58126e6f387c0cf | - | 85ba6183eb2c35cf7b6d63eb6fd515be7234f5f938da39d7d000a6a7f2359d4e |
| i1040s8812 | 2025; printed date 2026-01-23 | 2 | pages named by another document's citation | fd50a5266cc20aa5a31de0535658793f75c7abbb12fd83b65dc5b21c6ede2765 | 2 | e6ba91f54df679c9c19c23169c369f14bff012ba2fe110c3973bde59676c1d45 |

## Lines

### persons — Number of people on the return (you, and your spouse if filing jointly)
Status: **MATCH**

Model: Counts you, and your spouse on a joint return, as the people on the return. This matches the 'you, and your spouse if filing jointly' wording used throughout the instructions.

### taxpayers — Number of entries for you
Status: **MATCH**

Model: Counts the entries marked as yours. This is a structural count that the text does not contradict.

### spouses — Number of entries for your spouse
Status: **MATCH**

Model: Counts the entries marked as your spouse's. This is a structural count that the text does not contradict.

### roster_ok — One entry for you, and one for your spouse exactly when filing jointly
Status: **MATCH**

Model: Requires one entry for you, plus one spouse entry exactly when the status is 'Married filing jointly'. This fits the Form 1040 filing statuses. The under-16 refusal is openly recorded as an owner-decided entry check and names what it excludes.

### roster_bad — The people entered do not match the filing status
Status: **MATCH**

Model: This is the negation of roster_ok.

### hsa_people — Number of people on the return with a Form 8889
Status: **MATCH**

Model: Counts the people on the return who have a Form 8889. The i8889 text says to 'complete a separate Form 8889 for each spouse'.

### hsa_both — You and your spouse each have a Form 8889
Status: **MATCH**

Model: A count of 2 means both spouses have a Form 8889. That is the case where 'both you and your spouse have HSAs'.

### hsa_split_count — Number of Forms 8889 using the spouse rule of line 6
Status: **MATCH**

Model: Counts the Forms 8889 that use the line 6 rule for 'Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025'.

### hsa_agreed_count — Number of Forms 8889 using an agreed allocation
Status: **MATCH**

Model: Counts the Forms 8889 that use the line 6 option 'unless you both agree on a different allocation'.

### hsa_step1_sum — Both spouses Step 1 limits added together
Status: **MATCH**

Model: Adds each spouse's Step 1 limit. Step 1 is refigured from 'the total of the worksheet amounts only for the months you were treated as having family coverage', and the line 6 instructions support this.

### hsa_share_sum — Both spouses parts of the Step 1 limit added together
Status: **MATCH**

Model: Adds each spouse's share under Steps 2–3. The line 6 instructions divide the Step 1 limit between the spouses.

### work_ssn_count — Number of people on the return with an SSN valid for employment
Status: **MATCH**

Model: Counts the people who have an SSN 'valid for employment and issued before the due date of your return'.

### any_work_ssn — You, or your spouse if filing jointly, have an SSN valid for employment
Status: **MATCH**

Model: Is true when at least one person has a valid SSN. This matches 'only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC'.

### eic_ssn_count — Number of people on the return with an SSN valid for the EIC
Status: **MATCH**

Model: Counts the people who have an SSN 'issued on or before the due date ... that allows you to work and is valid for EIC purposes'.

### all_eic_ssn — You, and your spouse if filing jointly, have SSNs valid for the EIC
Status: **MATCH**

Model: Requires everyone on the return to have such an SSN. This matches EIC Step 1 question 2: 'Do you, and your spouse if filing a joint return, have a social security number...'.

### under16_count — Number of people on the return under age 16 at the end of 2025
Status: **MATCH**

Model: Counts the people on the return who were under 16 at the end of 2025. It supports the owner-decided entry check.

### filer_under16 — You, or your spouse if filing jointly, were under age 16 at the end of 2025
Status: **MATCH**

Model: Is true when any person on the return was under 16. This is consistent with its label.

### tin_count — Number of people on the return with an SSN or ITIN, or who have applied for an ITIN
Status: **MATCH**

Model: Counts the people who have an SSN or ITIN, or who applied for an ITIN. This follows Step 5 question 1: '(Answer “Yes” if you are applying for an ITIN on or before the return due date ...)'.

### all_tin — You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
Status: **MATCH**

Model: Requires you, and your spouse if filing jointly, to have an SSN or ITIN. This matches 'you, and your spouse if filing jointly, must have either an SSN or ITIN' for the credit for other dependents.

### id_count — Number of people on the return with an SSN valid for employment or an SSN or ITIN
Status: **MATCH**

Model: Counts the people who have either an employment-valid SSN or an issued SSN or ITIN. It does not count an applied-for ITIN, which is consistent with the CTC rule that the other spouse's number 'must have been issued on or before the due date'.

### ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid
Status: **MATCH**

Model: Requires at least one valid SSN, with every other person holding an SSN or ITIN. This matches 'only one spouse is required to have a valid SSN ... The other spouse must have either an SSN or ITIN'.

### taxpayer_work_ssn_count — Your entry, if the answer is yes
Status: **MATCH**

Model: Counts your own entry when you have an employment-valid SSN. This is a structural count.

### taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: Is true when your own entry has an SSN 'valid for employment and issued before the due date of your return'.

### home_cost — Did you pay over half the cost of keeping up your home for 2025?
Status: **MATCH**

Model: The included and excluded costs follow Pub. 501's 'Costs you include' and 'Costs you don’t include'. Funds held in a household member's name count as paid by that person, which matches 'considered paid by the child, not you'.

### unmarried — Were you unmarried, or considered unmarried under the head of household rules, at the end
Status: **MATCH**

Model: This is a direct input. It matches 'Check the “Head of household” box only if you are unmarried (or considered unmarried)'.

### married — Were you married at the end of 2025?
Status: **MATCH**

Model: This is a direct input on marital status at year end. The instructions use it for the Form 8889 age-55 rules ('unmarried' versus 'married').

### community_property — Did you live in a community property state at any time in 2025?
Status: **MATCH**

Model: The list of states matches 'Community property states include Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington, and Wisconsin'.

### hoh_community_property — Married, filing as head of household, and living in a community property state
Status: **MATCH**

Model: This is a refusal gate for a married head of household in a community property state. The text says such filers 'must usually follow state law to determine what is community income ... see Form 8958 and Pub. 555'.

### credit_disallowed — Was your EIC for a year after 1996, or your child tax credit, additional child tax credit
Status: **MATCH**

Model: This matches the Form 8862 triggers: an EIC 'for a year after 1996' and the CTC, ACTC or ODC 'for a year after 2015', reduced or disallowed other than for math or clerical error. It also covers the 2- and 10-year bans.

### test1_persons — Number of parents who qualify you under Test 1
Status: **MATCH**

Model: Counts the parents who qualify you under Test 1. The text says 'Your parent didn’t have to live with you'.

### test2_persons — Number of persons who qualify you under Test 2
Status: **MATCH**

Model: Counts the persons who lived with you 'for more than half of the year'. The home-cost part of Test 2 is tested separately in test2_met.

### test2_absence_persons — Number of persons who would qualify you under Test 2 only by counting an absence head of h
Status: **MATCH**

Model: Flags persons who would qualify only through an absence that Pub. 501 does not count. Pub. 501 requires that 'It must be reasonable to assume the absent person will return' and that 'You must continue to keep up the home'.

### hoh_absence — Head of household turns on a person who lived with you more than half the year only by cou
Status: **MATCH**

Model: Gates the refusal for the case where head of household status turns only on a disallowed absence. This is consistent with the Pub. 501 'Temporary absences' rule.

### test1_met — Test 1 met
Status: **MATCH**

Model: Test 1 is met when there is a qualifying parent. This matches 'You paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent whom you can claim as a dependent'.

### test2_met — Test 2 met, having paid over half the cost of keeping up your own home
Status: **MATCH**

Model: Requires both paying over half the home cost and having a qualifying person. This matches 'You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived'.

### hoh_eligible — Unmarried or considered unmarried, and Test 1 or Test 2 applies
Status: **MATCH**

Model: Matches 'only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies'. The refusals name the absence and community property cases that are excluded.

### hoh_fails — Head of household checked without meeting its tests
Status: **MATCH**

Model: Flags a return where the head of household box is checked but hoh_eligible is false. This is consistent with the instructions.

### qss_eligible — Do all five qualifying surviving spouse tests apply to you?
Status: **MATCH**

Model: The input restates the five tests in the instructions and Pub. 501. This includes 'If your spouse died in 2025, you can't file as qualifying surviving spouse' and the rules for absences, births, deaths and adoptions.

### qss_fails — Qualifying surviving spouse checked without meeting its tests
Status: **MATCH**

Model: Flags a return where the qualifying surviving spouse box is checked but not all five tests apply.

### rdp — Were you a registered domestic partner in Nevada, Washington or California at any time in
Status: **MATCH**

Model: This is a direct input. It matches 'Nevada, Washington, and California domestic partners'.

### rdp_community_property — Not filing jointly, living in a community property state, and a registered domestic partne
Status: **MATCH**

Model: Flags registered domestic partners who are not filing jointly. The text says they 'must generally report half the combined community income ... See Form 8958 and Pub. 555'.

## Raw response

```yaml
```yaml
lines:
  - key: "persons"
    status: MATCH
    reason: "Counts you, and your spouse on a joint return, as the people on the return. This matches the 'you, and your spouse if filing jointly' wording used throughout the instructions."
  - key: "taxpayers"
    status: MATCH
    reason: "Counts the entries marked as yours. This is a structural count that the text does not contradict."
  - key: "spouses"
    status: MATCH
    reason: "Counts the entries marked as your spouse's. This is a structural count that the text does not contradict."
  - key: "roster_ok"
    status: MATCH
    reason: "Requires one entry for you, plus one spouse entry exactly when the status is 'Married filing jointly'. This fits the Form 1040 filing statuses. The under-16 refusal is openly recorded as an owner-decided entry check and names what it excludes."
  - key: "roster_bad"
    status: MATCH
    reason: "This is the negation of roster_ok."
  - key: "hsa_people"
    status: MATCH
    reason: "Counts the people on the return who have a Form 8889. The i8889 text says to 'complete a separate Form 8889 for each spouse'."
  - key: "hsa_both"
    status: MATCH
    reason: "A count of 2 means both spouses have a Form 8889. That is the case where 'both you and your spouse have HSAs'."
  - key: "hsa_split_count"
    status: MATCH
    reason: "Counts the Forms 8889 that use the line 6 rule for 'Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025'."
  - key: "hsa_agreed_count"
    status: MATCH
    reason: "Counts the Forms 8889 that use the line 6 option 'unless you both agree on a different allocation'."
  - key: "hsa_step1_sum"
    status: MATCH
    reason: "Adds each spouse's Step 1 limit. Step 1 is refigured from 'the total of the worksheet amounts only for the months you were treated as having family coverage', and the line 6 instructions support this."
  - key: "hsa_share_sum"
    status: MATCH
    reason: "Adds each spouse's share under Steps 2–3. The line 6 instructions divide the Step 1 limit between the spouses."
  - key: "work_ssn_count"
    status: MATCH
    reason: "Counts the people who have an SSN 'valid for employment and issued before the due date of your return'."
  - key: "any_work_ssn"
    status: MATCH
    reason: "Is true when at least one person has a valid SSN. This matches 'only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC'."
  - key: "eic_ssn_count"
    status: MATCH
    reason: "Counts the people who have an SSN 'issued on or before the due date ... that allows you to work and is valid for EIC purposes'."
  - key: "all_eic_ssn"
    status: MATCH
    reason: "Requires everyone on the return to have such an SSN. This matches EIC Step 1 question 2: 'Do you, and your spouse if filing a joint return, have a social security number...'."
  - key: "under16_count"
    status: MATCH
    reason: "Counts the people on the return who were under 16 at the end of 2025. It supports the owner-decided entry check."
  - key: "filer_under16"
    status: MATCH
    reason: "Is true when any person on the return was under 16. This is consistent with its label."
  - key: "tin_count"
    status: MATCH
    reason: "Counts the people who have an SSN or ITIN, or who applied for an ITIN. This follows Step 5 question 1: '(Answer “Yes” if you are applying for an ITIN on or before the return due date ...)'."
  - key: "all_tin"
    status: MATCH
    reason: "Requires you, and your spouse if filing jointly, to have an SSN or ITIN. This matches 'you, and your spouse if filing jointly, must have either an SSN or ITIN' for the credit for other dependents."
  - key: "id_count"
    status: MATCH
    reason: "Counts the people who have either an employment-valid SSN or an issued SSN or ITIN. It does not count an applied-for ITIN, which is consistent with the CTC rule that the other spouse's number 'must have been issued on or before the due date'."
  - key: "ctc_ssn"
    status: MATCH
    reason: "Requires at least one valid SSN, with every other person holding an SSN or ITIN. This matches 'only one spouse is required to have a valid SSN ... The other spouse must have either an SSN or ITIN'."
  - key: "taxpayer_work_ssn_count"
    status: MATCH
    reason: "Counts your own entry when you have an employment-valid SSN. This is a structural count."
  - key: "taxpayer_work_ssn"
    status: MATCH
    reason: "Is true when your own entry has an SSN 'valid for employment and issued before the due date of your return'."
  - key: "home_cost"
    status: MATCH
    reason: "The included and excluded costs follow Pub. 501's 'Costs you include' and 'Costs you don’t include'. Funds held in a household member's name count as paid by that person, which matches 'considered paid by the child, not you'."
  - key: "unmarried"
    status: MATCH
    reason: "This is a direct input. It matches 'Check the “Head of household” box only if you are unmarried (or considered unmarried)'."
  - key: "married"
    status: MATCH
    reason: "This is a direct input on marital status at year end. The instructions use it for the Form 8889 age-55 rules ('unmarried' versus 'married')."
  - key: "community_property"
    status: MATCH
    reason: "The list of states matches 'Community property states include Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington, and Wisconsin'."
  - key: "hoh_community_property"
    status: MATCH
    reason: "This is a refusal gate for a married head of household in a community property state. The text says such filers 'must usually follow state law to determine what is community income ... see Form 8958 and Pub. 555'."
  - key: "credit_disallowed"
    status: MATCH
    reason: "This matches the Form 8862 triggers: an EIC 'for a year after 1996' and the CTC, ACTC or ODC 'for a year after 2015', reduced or disallowed other than for math or clerical error. It also covers the 2- and 10-year bans."
  - key: "test1_persons"
    status: MATCH
    reason: "Counts the parents who qualify you under Test 1. The text says 'Your parent didn’t have to live with you'."
  - key: "test2_persons"
    status: MATCH
    reason: "Counts the persons who lived with you 'for more than half of the year'. The home-cost part of Test 2 is tested separately in test2_met."
  - key: "test2_absence_persons"
    status: MATCH
    reason: "Flags persons who would qualify only through an absence that Pub. 501 does not count. Pub. 501 requires that 'It must be reasonable to assume the absent person will return' and that 'You must continue to keep up the home'."
  - key: "hoh_absence"
    status: MATCH
    reason: "Gates the refusal for the case where head of household status turns only on a disallowed absence. This is consistent with the Pub. 501 'Temporary absences' rule."
  - key: "test1_met"
    status: MATCH
    reason: "Test 1 is met when there is a qualifying parent. This matches 'You paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent whom you can claim as a dependent'."
  - key: "test2_met"
    status: MATCH
    reason: "Requires both paying over half the home cost and having a qualifying person. This matches 'You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived'."
  - key: "hoh_eligible"
    status: MATCH
    reason: "Matches 'only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies'. The refusals name the absence and community property cases that are excluded."
  - key: "hoh_fails"
    status: MATCH
    reason: "Flags a return where the head of household box is checked but hoh_eligible is false. This is consistent with the instructions."
  - key: "qss_eligible"
    status: MATCH
    reason: "The input restates the five tests in the instructions and Pub. 501. This includes 'If your spouse died in 2025, you can't file as qualifying surviving spouse' and the rules for absences, births, deaths and adoptions."
  - key: "qss_fails"
    status: MATCH
    reason: "Flags a return where the qualifying surviving spouse box is checked but not all five tests apply."
  - key: "rdp"
    status: MATCH
    reason: "This is a direct input. It matches 'Nevada, Washington, and California domestic partners'."
  - key: "rdp_community_property"
    status: MATCH
    reason: "Flags registered domestic partners who are not filing jointly. The text says they 'must generally report half the combined community income ... See Form 8958 and Pub. 555'."
```
```
