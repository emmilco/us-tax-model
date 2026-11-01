# Render comparison — household

The rendered English of every printed line of `Household facts for dependents and head of household` (`rendered/2025/household.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-31 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | fbd4b937cad4b2ded7217bd601c23cd838c2c54ca2106b75558244e9e2b042f4 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 0f13b65328288794688ba841bdb9a9f05903cfcd2c86461b6b70e636123ccaee |
| lines judged | 41 |
| match / mismatch / unclear / missing | 38 / 3 / 0 / 0 |
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

Model: Restatement counts you and your spouse if filing jointly, matching the return's persons.

### taxpayers — Number of entries for you
Status: **MATCH**

Model: Restatement counts entries identified as yours.

### spouses — Number of entries for your spouse
Status: **MATCH**

Model: Restatement counts entries identified as your spouse's.

### roster_ok — One entry for you, and one for your spouse exactly when filing jointly
Status: **MATCH**

Model: Restatement requires one taxpayer entry and one spouse entry exactly for married filing jointly; the under-16 refusal is an entry check that names the exclusion.

### roster_bad — The people entered do not match the filing status
Status: **MATCH**

Model: Restatement is the negation of roster_ok.

### hsa_people — Number of people on the return with a Form 8889
Status: **MATCH**

Model: Restatement counts people with at least one Form 8889, matching the separate Form 8889 requirement for spouses with HSAs.

### hsa_both — You and your spouse each have a Form 8889
Status: **MATCH**

Model: Restatement is true when both people on the return have a Form 8889, matching the two-spouse HSA case.

### hsa_split_count — Number of Forms 8889 using the spouse rule of line 6
Status: **MATCH**

Model: Restatement counts Forms 8889 using the line 6 spouse rule when the spouses have separate HSAs and family coverage.

### hsa_agreed_count — Number of Forms 8889 using an agreed allocation
Status: **MATCH**

Model: Restatement counts Forms 8889 using an agreed allocation under the line 6 spouse rule.

### hsa_step1_sum — Both spouses Step 1 limits added together
Status: **MATCH**

Model: Restatement sums the per-spouse Step 1 refigured line 5 amounts under the line 6 spouse rule.

### hsa_share_sum — Both spouses parts of the Step 1 limit added together
Status: **MATCH**

Model: Restatement sums each spouse's Step 2/3 share of the Step 1 limit.

### work_ssn_count — Number of people on the return with an SSN valid for employment
Status: **MATCH**

Model: Restatement counts people with an SSN valid for employment issued before the due date, matching the CTC SSN rule.

### any_work_ssn — You, or your spouse if filing jointly, have an SSN valid for employment
Status: **MATCH**

Model: Restatement is true when at least one person on the return has a work-valid SSN.

### eic_ssn_count — Number of people on the return with an SSN valid for the EIC
Status: **MATCH**

Model: Restatement counts people with an SSN valid for the EIC issued on or before the due date.

### all_eic_ssn — You, and your spouse if filing jointly, have SSNs valid for the EIC
Status: **MATCH**

Model: Restatement requires every person on the return to have an EIC-valid SSN.

### under16_count — Number of people on the return under age 16 at the end of 2025
Status: **MATCH**

Model: Restatement counts people on the return under age 16 at the end of 2025.

### filer_under16 — You, or your spouse if filing jointly, were under age 16 at the end of 2025
Status: **MATCH**

Model: Restatement is true when any person on the return is under age 16 at the end of 2025.

### tin_count — Number of people on the return with an SSN or ITIN, or who have applied for an ITIN
Status: **MATCH**

Model: Restatement counts people with an SSN or ITIN issued on or before the due date or an ITIN application by the due date.

### all_tin — You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
Status: **MATCH**

Model: Restatement requires every person on the return to have a TIN or pending ITIN application.

### id_count — Number of people on the return with an SSN valid for employment or an SSN or ITIN
Status: **MATCH**

Model: Restatement counts people with a work-valid SSN or an SSN/ITIN.

### ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid
Status: **MATCH**

Model: Restatement requires at least one spouse to have a work-valid SSN and the other person(s) to have an SSN or ITIN, matching the CTC identification rule.

### taxpayer_work_ssn_count — Your entry, if the answer is yes
Status: **MATCH**

Model: Restatement counts your entry when you have a work-valid SSN.

### taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: Restatement is true when your entry has a work-valid SSN.

### home_cost — Did you pay over half the cost of keeping up your home for 2025?
Status: **MATCH**

Model: Restatement matches the IRS/Pub. 501 cost-of-keeping-up-a-home definition and exclusions.

### unmarried — Were you unmarried, or considered unmarried under the head of household rules, at the end
Status: **MATCH**

Model: Restatement matches the HOH requirement to be unmarried or considered unmarried.

### married — Were you married at the end of 2025?
Status: **MATCH**

Model: Restatement asks whether married at the end of 2025, including married but considered unmarried for HOH.

### community_property — Did you live in a community property state at any time in 2025?
Status: **MATCH**

Model: Restatement lists the same community property states as the IRS text.

### hoh_community_property — Married, filing as head of household, and living in a community property state
Status: **MATCH**

Model: Restatement identifies a married HOH filer in a community property state, matching the Form 8958/Pub. 555 refusal.

### credit_disallowed — Was your EIC for a year after 1996, or your child tax credit, additional child tax credit
Status: **MATCH**

Model: Restatement matches the EIC/CTC/ACTC/ODC disallowance and 2- or 10-year period rules.

### test1_persons — Number of parents who qualify you under Test 1
Status: **MATCH**

Model: Restatement counts dependents for whom the Test 1 parent-qualification helper is true.

### test2_persons — Number of persons who qualify you under Test 2
Status: **MISMATCH**

Restated: Add dependent.one over every confirmed dependent entry for which helper "A Test 2 person who lived with you more than half the year, or of the part of the year a relative was alive, counting only absences head of household counts (the home-cost condition of Test 2 is tested on the household form)" = true, within the current person when parent-bound. An unanswered roster is unknown.

Model: It counts time lived as more than half the year or part of the year alive with HOH-counted absences, but omits the IRS rule that an adopted, lawfully placed, or eligible foster child (and kidnapped child) is treated as living with you for the required time.

Ruling: interface gap; p501 p. 9, Adopted child or foster child: "The person is considered to have lived with you for more than half of 2025 if your main home was this person's main home for more than half the time since the child was adopted or placed with you in 2025."; p501 p. 9, Kidnapped child: "You may be eligible to file as head of household even if the child who is your qualifying person has been kidnapped." The model says the restatement omits the adoption, placement and foster-child rule and the kidnapped-child rule. The restatement names the per-entry helper dependent.hoh_test2 by its label. The T-091 correction changed only the label, adding "counting only absences head of household counts", which is accurate: hoh_test2 is hoh_test2_lived and absence_no_return no. The helper and its parts are defined in rendered/2025/dependent.md, outside the text given. There dependent.hoh_lived_half carries the adoption and placement rule (dependent.placed with dependent.part_year_home, "more than half the time since the person was adopted or placed with you in 2025"), dependent.months carries it for a qualifying child, and a kidnapped child is refused at dependent.lived_half (BUG-0213), which hoh_lived_half reads. The omission is in the label only and predates T-091; the fix-round-2 render ruled the same objection an interface gap. The new lines test2_absence_persons and hoh_absence and the new refusal on hoh_eligible were judged MATCH. Project stands.

### test2_absence_persons — Number of persons who would qualify you under Test 2 only by counting an absence head of h
Status: **MATCH**

Model: Restatement counts persons who would qualify only by counting an absence that HOH does not count.

### hoh_absence — Head of household turns on a person who lived with you more than half the year only by cou
Status: **MATCH**

Model: Restatement is true when HOH turns on an HOH-counted absence and Test 1 is not met.

### test1_met — Test 1 met
Status: **MATCH**

Model: Restatement is true when the Test 1 parent count is greater than zero.

### test2_met — Test 2 met, having paid over half the cost of keeping up your own home
Status: **MATCH**

Model: Restatement requires paying over half the home cost and having a Test 2 person.

### hoh_eligible — Unmarried or considered unmarried, and Test 1 or Test 2 applies
Status: **MATCH**

Model: Restatement matches the IRS rule: unmarried or considered unmarried and either Test 1 or Test 2 applies; refusals name the excluded absence and community-property cases.

### hoh_fails — Head of household checked without meeting its tests
Status: **MATCH**

Model: Restatement is true when HOH is checked but the eligibility helper is false.

### qss_eligible — Do all five qualifying surviving spouse tests apply to you?
Status: **MISMATCH**

Restated: Input — Do all five of these tests apply to you? 1. Your spouse died in 2023 or 2024 and you didn't remarry before the end of 2025 (if your spouse died in 2025, answer No). 2. You have a child or stepchild (not a foster child) whom you can claim as a dependent, or could claim as a dependent except that, for 2025, the child had gross income of $5,200 or more, the child filed a joint return, or you could be claimed as a dependent on someone else's return; an adopted child, including a child lawfully placed with you for legal adoption, is always your own child. 3. This child lived in your home for all of 2025, counting temporary absences by you or the child for special circumstances, such as school, vacation, business, medical care, military service or detention in a juvenile facility, as time lived in the home, but only an absence from which it was reasonable to assume the absent person would return and during which you kept up the home; a child born or who died in 2025, or adopted or lawfully placed with you for legal adoption in 2025, lived with you all year if your home was the child's home for the entire time the child was alive, or since the adoption or placement. 4. You paid over half the cost of keeping up your home (rent, mortgage interest, real estate taxes, insurance on the home, repairs, utilities and food eaten in the home; not clothing, education, medical treatment, vacations, life insurance, transportation or anyone’s services; amounts paid from a household member’s own funds, such as Social Security, count as paid by them). 5. You could have filed a joint return with your spouse the year your spouse died, even if you didn't actually do so.

Model: Test 3 omits the IRS exception that a kidnapped child may still qualify the filer for QSS; the IRS text says you may be eligible even if the qualifying child has been kidnapped.

Ruling: finding; p501 p. 11, Qualifying Surviving Spouse, Kidnapped child: "You may be eligible to file as a qualifying surviving spouse even if the child who qualifies you for this filing status has been kidnapped." The model is right: test 3 of the question has no kidnapped-child exception. This is fix round 2's household F1 (.transcription/proposed/fixr2/household.findings.md), a low over-refusal batched by the owner in TASKS.md T-092. It is not re-raised as new. T-091 added only the expected-return clause to test 3 (p501 pp. 9, 11), which the T-091 round found no wider and no narrower than the source. The kidnapped-child gap predates T-091 and is unaffected by the correction. Project stands pending T-092.

### qss_fails — Qualifying surviving spouse checked without meeting its tests
Status: **MATCH**

Model: Restatement is true when QSS is checked but the five-test helper is false.

### rdp — Were you a registered domestic partner in Nevada, Washington or California at any time in
Status: **MATCH**

Model: Restatement asks the same Nevada, Washington, or California registered-domestic-partner question as the IRS text.

### rdp_community_property — Not filing jointly, living in a community property state, and a registered domestic partne
Status: **MISMATCH**

Restated: f1040 line Filing Status ≠ 'mfj' and helper "Did you live in a community property state at any time in 2025?" = true and helper "Were you a registered domestic partner in Nevada, Washington or California at any time in 2025?" = true

Model: It adds a 'not filing jointly' condition; the IRS text says a registered domestic partner in Nevada, Washington, or California must generally report half the combined community income, with no filing-status limitation.

Ruling: interface gap; i1040gi p. 23, Community Property States: "A registered domestic partner in Nevada, Washington, or California must generally report half the combined community income of the individual and their domestic partner. See Form 8958 and Pub. 555." The model says the gate's not-joint condition has no basis in the text given. What decides it is p501 p. 6, not among the pages given (p501 pp. 9 and 11): registered domestic partners "aren't lawfully married for federal tax purposes". A joint return needs a spouse (i1040gi p. 13, Married Filing Jointly) and already reports both spouses' combined income. So the partner rule reaches a partner on a single, head of household or qualifying surviving spouse return, where the gate refuses, and s3.mfs refuses married filing separately. The line is unchanged since fix round 2. As the fix-round-5 ruling of the Claude render. Project stands.

## Raw response

```yaml
lines:
  - key: "persons"
    status: MATCH
    reason: "Restatement counts you and your spouse if filing jointly, matching the return's persons."
  - key: "taxpayers"
    status: MATCH
    reason: "Restatement counts entries identified as yours."
  - key: "spouses"
    status: MATCH
    reason: "Restatement counts entries identified as your spouse's."
  - key: "roster_ok"
    status: MATCH
    reason: "Restatement requires one taxpayer entry and one spouse entry exactly for married filing jointly; the under-16 refusal is an entry check that names the exclusion."
  - key: "roster_bad"
    status: MATCH
    reason: "Restatement is the negation of roster_ok."
  - key: "hsa_people"
    status: MATCH
    reason: "Restatement counts people with at least one Form 8889, matching the separate Form 8889 requirement for spouses with HSAs."
  - key: "hsa_both"
    status: MATCH
    reason: "Restatement is true when both people on the return have a Form 8889, matching the two-spouse HSA case."
  - key: "hsa_split_count"
    status: MATCH
    reason: "Restatement counts Forms 8889 using the line 6 spouse rule when the spouses have separate HSAs and family coverage."
  - key: "hsa_agreed_count"
    status: MATCH
    reason: "Restatement counts Forms 8889 using an agreed allocation under the line 6 spouse rule."
  - key: "hsa_step1_sum"
    status: MATCH
    reason: "Restatement sums the per-spouse Step 1 refigured line 5 amounts under the line 6 spouse rule."
  - key: "hsa_share_sum"
    status: MATCH
    reason: "Restatement sums each spouse's Step 2/3 share of the Step 1 limit."
  - key: "work_ssn_count"
    status: MATCH
    reason: "Restatement counts people with an SSN valid for employment issued before the due date, matching the CTC SSN rule."
  - key: "any_work_ssn"
    status: MATCH
    reason: "Restatement is true when at least one person on the return has a work-valid SSN."
  - key: "eic_ssn_count"
    status: MATCH
    reason: "Restatement counts people with an SSN valid for the EIC issued on or before the due date."
  - key: "all_eic_ssn"
    status: MATCH
    reason: "Restatement requires every person on the return to have an EIC-valid SSN."
  - key: "under16_count"
    status: MATCH
    reason: "Restatement counts people on the return under age 16 at the end of 2025."
  - key: "filer_under16"
    status: MATCH
    reason: "Restatement is true when any person on the return is under age 16 at the end of 2025."
  - key: "tin_count"
    status: MATCH
    reason: "Restatement counts people with an SSN or ITIN issued on or before the due date or an ITIN application by the due date."
  - key: "all_tin"
    status: MATCH
    reason: "Restatement requires every person on the return to have a TIN or pending ITIN application."
  - key: "id_count"
    status: MATCH
    reason: "Restatement counts people with a work-valid SSN or an SSN/ITIN."
  - key: "ctc_ssn"
    status: MATCH
    reason: "Restatement requires at least one spouse to have a work-valid SSN and the other person(s) to have an SSN or ITIN, matching the CTC identification rule."
  - key: "taxpayer_work_ssn_count"
    status: MATCH
    reason: "Restatement counts your entry when you have a work-valid SSN."
  - key: "taxpayer_work_ssn"
    status: MATCH
    reason: "Restatement is true when your entry has a work-valid SSN."
  - key: "home_cost"
    status: MATCH
    reason: "Restatement matches the IRS/Pub. 501 cost-of-keeping-up-a-home definition and exclusions."
  - key: "unmarried"
    status: MATCH
    reason: "Restatement matches the HOH requirement to be unmarried or considered unmarried."
  - key: "married"
    status: MATCH
    reason: "Restatement asks whether married at the end of 2025, including married but considered unmarried for HOH."
  - key: "community_property"
    status: MATCH
    reason: "Restatement lists the same community property states as the IRS text."
  - key: "hoh_community_property"
    status: MATCH
    reason: "Restatement identifies a married HOH filer in a community property state, matching the Form 8958/Pub. 555 refusal."
  - key: "credit_disallowed"
    status: MATCH
    reason: "Restatement matches the EIC/CTC/ACTC/ODC disallowance and 2- or 10-year period rules."
  - key: "test1_persons"
    status: MATCH
    reason: "Restatement counts dependents for whom the Test 1 parent-qualification helper is true."
  - key: "test2_persons"
    status: MISMATCH
    reason: "It counts time lived as more than half the year or part of the year alive with HOH-counted absences, but omits the IRS rule that an adopted, lawfully placed, or eligible foster child (and kidnapped child) is treated as living with you for the required time."
  - key: "test2_absence_persons"
    status: MATCH
    reason: "Restatement counts persons who would qualify only by counting an absence that HOH does not count."
  - key: "hoh_absence"
    status: MATCH
    reason: "Restatement is true when HOH turns on an HOH-counted absence and Test 1 is not met."
  - key: "test1_met"
    status: MATCH
    reason: "Restatement is true when the Test 1 parent count is greater than zero."
  - key: "test2_met"
    status: MATCH
    reason: "Restatement requires paying over half the home cost and having a Test 2 person."
  - key: "hoh_eligible"
    status: MATCH
    reason: "Restatement matches the IRS rule: unmarried or considered unmarried and either Test 1 or Test 2 applies; refusals name the excluded absence and community-property cases."
  - key: "hoh_fails"
    status: MATCH
    reason: "Restatement is true when HOH is checked but the eligibility helper is false."
  - key: "qss_eligible"
    status: MISMATCH
    reason: "Test 3 omits the IRS exception that a kidnapped child may still qualify the filer for QSS; the IRS text says you may be eligible even if the qualifying child has been kidnapped."
  - key: "qss_fails"
    status: MATCH
    reason: "Restatement is true when QSS is checked but the five-test helper is false."
  - key: "rdp"
    status: MATCH
    reason: "Restatement asks the same Nevada, Washington, or California registered-domestic-partner question as the IRS text."
  - key: "rdp_community_property"
    status: MISMATCH
    reason: "It adds a 'not filing jointly' condition; the IRS text says a registered domestic partner in Nevada, Washington, or California must generally report half the combined community income, with no filing-status limitation."
```
