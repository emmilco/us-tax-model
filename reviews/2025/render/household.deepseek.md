# Render comparison — household

The rendered English of every printed line of `Household facts for dependents and head of household` (`rendered/2025/household.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 48d1697b32ed44c87f616892fa7274b2288930ee3d158a0c0715fc8299d14339 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 6c07c8cf3e4ccbb17ac1cfbccb02fef0bdc91feb9169993b37332b137c0f686d |
| lines judged | 39 |
| match / mismatch / unclear / missing | 37 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14, 15, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 15, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 2, 4, 5, 6, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 2, 4, 5, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |
| f8889 | 2025; created 2025-03-28 | 1 | whole document | f1ae3589453f3dd1d5277a79409bd7d0bf4772715fa8bd11d58126e6f387c0cf | - | 85ba6183eb2c35cf7b6d63eb6fd515be7234f5f938da39d7d000a6a7f2359d4e |
| p501 | 2025 returns; PDF created 2026-02-04 | 9 | pages named by another document's citation | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | - | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| i1040s8812 | 2025; printed date 2026-01-23 | 2 | pages named by another document's citation | fd50a5266cc20aa5a31de0535658793f75c7abbb12fd83b65dc5b21c6ede2765 | 2 | e6ba91f54df679c9c19c23169c369f14bff012ba2fe110c3973bde59676c1d45 |

## Lines

### persons — Number of people on the return (you, and your spouse if filing jointly)
Status: **MATCH**

Model: Counts one per confirmed person entry for the filer/spouse roster, consistent with the Form 1040 taxpayer/spouse entries.

### taxpayers — Number of entries for you
Status: **MATCH**

Model: Counts entries marked as the taxpayer's entry.

### spouses — Number of entries for your spouse
Status: **MATCH**

Model: Counts entries marked as the spouse's entry.

### roster_ok — One entry for you, and one for your spouse exactly when filing jointly
Status: **MATCH**

Model: Requires one taxpayer entry and one spouse entry only for MFJ; the under-16 refusal names the excluded case.

### roster_bad — The people entered do not match the filing status
Status: **MATCH**

Model: Correctly negates roster_ok.

### hsa_people — Number of people on the return with a Form 8889
Status: **MATCH**

Model: Counts people with a Form 8889, matching the helper label.

### hsa_both — You and your spouse each have a Form 8889
Status: **MATCH**

Model: True when two people on the return have Forms 8889.

### hsa_split_count — Number of Forms 8889 using the spouse rule of line 6
Status: **MATCH**

Model: Counts Forms 8889 using the line 6 spouse rule.

### hsa_agreed_count — Number of Forms 8889 using an agreed allocation
Status: **MATCH**

Model: Counts Forms 8889 using an agreed allocation under the line 6 spouse rule.

### hsa_step1_sum — Both spouses Step 1 limits added together
Status: **MATCH**

Model: Sums the Step 1 limits for spouse-rule Forms 8889 as labeled.

### hsa_share_sum — Both spouses parts of the Step 1 limit added together
Status: **MATCH**

Model: Sums the spouses' allocated parts of the Step 1 limit as labeled.

### work_ssn_count — Number of people on the return with an SSN valid for employment
Status: **MATCH**

Model: Counts people with an SSN valid for employment issued before the due date.

### any_work_ssn — You, or your spouse if filing jointly, have an SSN valid for employment
Status: **MATCH**

Model: True when at least one taxpayer/spouse entry has a work-valid SSN.

### eic_ssn_count — Number of people on the return with an SSN valid for the EIC
Status: **MATCH**

Model: Counts people with an SSN valid for the EIC.

### all_eic_ssn — You, and your spouse if filing jointly, have SSNs valid for the EIC
Status: **MATCH**

Model: True when every taxpayer/spouse entry has an EIC-valid SSN.

### under16_count — Number of people on the return under age 16 at the end of 2025
Status: **MATCH**

Model: Counts people under age 16 at the end of 2025.

### filer_under16 — You, or your spouse if filing jointly, were under age 16 at the end of 2025
Status: **MATCH**

Model: True when a taxpayer/spouse entry is under age 16 at the end of 2025.

### tin_count — Number of people on the return with an SSN or ITIN, or who have applied for an ITIN
Status: **MATCH**

Model: Counts people with an SSN/ITIN or an ITIN application.

### all_tin — You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
Status: **MATCH**

Model: True when every taxpayer/spouse entry has an SSN/ITIN or ITIN application.

### id_count — Number of people on the return with an SSN valid for employment or an SSN or ITIN
Status: **MATCH**

Model: Counts people with a work-valid SSN or an SSN/ITIN.

### ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid
Status: **MATCH**

Model: Within the taxpayer/spouse roster, matches the CTC rule that one spouse needs a work-valid SSN and the other needs SSN or ITIN.

### taxpayer_work_ssn_count — Your entry, if the answer is yes
Status: **MATCH**

Model: Counts the taxpayer's yes entry for a work-valid SSN.

### taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: True when the taxpayer has a work-valid SSN.

### home_cost — Did you pay over half the cost of keeping up your home for 2025?
Status: **MATCH**

Model: Mirrors Pub. 501's cost-of-keeping-up-a-home list and the rule that a person's own funds count as paid by that person.

### unmarried — Were you unmarried, or considered unmarried under the head of household rules, at the end
Status: **MATCH**

Model: Asks the HOH unmarried/considered-unmarried condition.

### married — Were you married at the end of 2025?
Status: **MATCH**

Model: Asks legal marital status at year end, including married-but-considered-unmarried for HOH.

### community_property — Did you live in a community property state at any time in 2025?
Status: **MATCH**

Model: Lists the community property states from the IRS text.

### hoh_community_property — Married, filing as head of household, and living in a community property state
Status: **MATCH**

Model: Flags married HOH filers in community property states; the refusal names Form 8958/Pub. 555.

### credit_disallowed — Was your EIC for a year after 1996, or your child tax credit, additional child tax credit
Status: **MATCH**

Model: Mirrors the Form 8862/EIC/CTC/ODC disallowance question.

### test1_persons — Number of parents who qualify you under Test 1
Status: **MISMATCH**

Restated: Add dependent.one over every confirmed dependent entry for which helper "Qualifies you for head of household under Test 1 through a parent who does not live with you (a parent who lives with you qualifies you through Test 2)" = true, within the current person when parent-bound. An unanswered roster is unknown.

Model: The restatement limits Test 1 to a parent 'who does not live with you,' but the IRS text says 'Your parent didn't have to live with you,' so a live-in parent can still meet Test 1.

Ruling: representation; i1040gi p. 14, Test 1: "You paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent whom you can claim as a dependent ... Your parent didn't have to live with you." The model reads the helper's label ("through a parent who does not live with you (a parent who lives with you qualifies you through Test 2)") as excluding a co-resident parent. The helper's expression (dependent.hoh_test1: parent, your dependent, dependent.parent_home_paid) has no residence condition, and parent_home_paid asks about "a home that was their main home" without one, so such a parent counts under Test 1. Were a filer to answer no for that parent because of the label, Test 2 qualifies on the same facts (household.home_cost for the home you share, which since BUG-0258 and BUG-0260 carries the same p501 p. 9 cost definition and own-funds rule as parent_home_paid; the parent your dependent and living with you more than half the year). The label is imprecise, not wrong in effect. The restatement and the objection are those ruled in fix round 2 and the completeness-fixes round. Project stands.

### test2_persons — Number of persons who qualify you under Test 2
Status: **MATCH**

Model: Counts Test 2 persons who lived with you more than half the year, with the birth/death exception.

### test1_met — Test 1 met
Status: **MISMATCH**

Restated: helper "Number of parents who qualify you under Test 1" > 0 (a count)

Model: Because it is test1_persons > 0, it inherits the live-in-parent exclusion and can report Test 1 not met even though the IRS text says 'Your parent didn't have to live with you.'

Ruling: representation; i1040gi p. 14, Test 1: "Your parent didn't have to live with you." The objection is test1_persons' (the helper label read as excluding a parent who lives with you), inherited through the count: Test 1 met is test1_persons above 0, which is the source's "either Test 1 or Test 2 applies" for Test 1. As ruled for test1_persons, the helper dependent.hoh_test1 has no residence condition, and a co-resident parent who fails Test 1 on the label's reading meets Test 2 on the same facts. Project stands.

### test2_met — Test 2 met, having paid over half the cost of keeping up your own home
Status: **MATCH**

Model: Requires paying over half the home cost and a Test 2 person.

### hoh_eligible — Unmarried or considered unmarried, and Test 1 or Test 2 applies
Status: **MATCH**

Model: Mirrors the rule: unmarried (or considered unmarried) and either Test 1 or Test 2 applies.

### hoh_fails — Head of household checked without meeting its tests
Status: **MATCH**

Model: True when HOH is checked but hoh_eligible is false.

### qss_eligible — Do all five qualifying surviving spouse tests apply to you?
Status: **MATCH**

Model: Restates all five QSS tests from the instructions.

### qss_fails — Qualifying surviving spouse checked without meeting its tests
Status: **MATCH**

Model: True when QSS is checked but the five tests do not all apply.

### rdp — Were you a registered domestic partner in Nevada, Washington or California at any time in
Status: **MATCH**

Model: Asks the Nevada/Washington/California registered domestic partner fact.

### rdp_community_property — Not filing jointly, living in a community property state, and a registered domestic partne
Status: **MATCH**

Model: Flags a non-MFJ registered domestic partner in a community property state; the IRS text says such partners generally report half combined community income.

## Raw response

```yaml
lines:
  - key: "persons"
    status: MATCH
    reason: "Counts one per confirmed person entry for the filer/spouse roster, consistent with the Form 1040 taxpayer/spouse entries."
  - key: "taxpayers"
    status: MATCH
    reason: "Counts entries marked as the taxpayer's entry."
  - key: "spouses"
    status: MATCH
    reason: "Counts entries marked as the spouse's entry."
  - key: "roster_ok"
    status: MATCH
    reason: "Requires one taxpayer entry and one spouse entry only for MFJ; the under-16 refusal names the excluded case."
  - key: "roster_bad"
    status: MATCH
    reason: "Correctly negates roster_ok."
  - key: "hsa_people"
    status: MATCH
    reason: "Counts people with a Form 8889, matching the helper label."
  - key: "hsa_both"
    status: MATCH
    reason: "True when two people on the return have Forms 8889."
  - key: "hsa_split_count"
    status: MATCH
    reason: "Counts Forms 8889 using the line 6 spouse rule."
  - key: "hsa_agreed_count"
    status: MATCH
    reason: "Counts Forms 8889 using an agreed allocation under the line 6 spouse rule."
  - key: "hsa_step1_sum"
    status: MATCH
    reason: "Sums the Step 1 limits for spouse-rule Forms 8889 as labeled."
  - key: "hsa_share_sum"
    status: MATCH
    reason: "Sums the spouses' allocated parts of the Step 1 limit as labeled."
  - key: "work_ssn_count"
    status: MATCH
    reason: "Counts people with an SSN valid for employment issued before the due date."
  - key: "any_work_ssn"
    status: MATCH
    reason: "True when at least one taxpayer/spouse entry has a work-valid SSN."
  - key: "eic_ssn_count"
    status: MATCH
    reason: "Counts people with an SSN valid for the EIC."
  - key: "all_eic_ssn"
    status: MATCH
    reason: "True when every taxpayer/spouse entry has an EIC-valid SSN."
  - key: "under16_count"
    status: MATCH
    reason: "Counts people under age 16 at the end of 2025."
  - key: "filer_under16"
    status: MATCH
    reason: "True when a taxpayer/spouse entry is under age 16 at the end of 2025."
  - key: "tin_count"
    status: MATCH
    reason: "Counts people with an SSN/ITIN or an ITIN application."
  - key: "all_tin"
    status: MATCH
    reason: "True when every taxpayer/spouse entry has an SSN/ITIN or ITIN application."
  - key: "id_count"
    status: MATCH
    reason: "Counts people with a work-valid SSN or an SSN/ITIN."
  - key: "ctc_ssn"
    status: MATCH
    reason: "Within the taxpayer/spouse roster, matches the CTC rule that one spouse needs a work-valid SSN and the other needs SSN or ITIN."
  - key: "taxpayer_work_ssn_count"
    status: MATCH
    reason: "Counts the taxpayer's yes entry for a work-valid SSN."
  - key: "taxpayer_work_ssn"
    status: MATCH
    reason: "True when the taxpayer has a work-valid SSN."
  - key: "home_cost"
    status: MATCH
    reason: "Mirrors Pub. 501's cost-of-keeping-up-a-home list and the rule that a person's own funds count as paid by that person."
  - key: "unmarried"
    status: MATCH
    reason: "Asks the HOH unmarried/considered-unmarried condition."
  - key: "married"
    status: MATCH
    reason: "Asks legal marital status at year end, including married-but-considered-unmarried for HOH."
  - key: "community_property"
    status: MATCH
    reason: "Lists the community property states from the IRS text."
  - key: "hoh_community_property"
    status: MATCH
    reason: "Flags married HOH filers in community property states; the refusal names Form 8958/Pub. 555."
  - key: "credit_disallowed"
    status: MATCH
    reason: "Mirrors the Form 8862/EIC/CTC/ODC disallowance question."
  - key: "test1_persons"
    status: MISMATCH
    reason: "The restatement limits Test 1 to a parent 'who does not live with you,' but the IRS text says 'Your parent didn't have to live with you,' so a live-in parent can still meet Test 1."
  - key: "test2_persons"
    status: MATCH
    reason: "Counts Test 2 persons who lived with you more than half the year, with the birth/death exception."
  - key: "test1_met"
    status: MISMATCH
    reason: "Because it is test1_persons > 0, it inherits the live-in-parent exclusion and can report Test 1 not met even though the IRS text says 'Your parent didn't have to live with you.'"
  - key: "test2_met"
    status: MATCH
    reason: "Requires paying over half the home cost and a Test 2 person."
  - key: "hoh_eligible"
    status: MATCH
    reason: "Mirrors the rule: unmarried (or considered unmarried) and either Test 1 or Test 2 applies."
  - key: "hoh_fails"
    status: MATCH
    reason: "True when HOH is checked but hoh_eligible is false."
  - key: "qss_eligible"
    status: MATCH
    reason: "Restates all five QSS tests from the instructions."
  - key: "qss_fails"
    status: MATCH
    reason: "True when QSS is checked but the five tests do not all apply."
  - key: "rdp"
    status: MATCH
    reason: "Asks the Nevada/Washington/California registered domestic partner fact."
  - key: "rdp_community_property"
    status: MATCH
    reason: "Flags a non-MFJ registered domestic partner in a community property state; the IRS text says such partners generally report half combined community income."
```
