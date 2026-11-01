# Render comparison — household

The rendered English of every printed line of `Household facts for dependents and head of household` (`rendered/2025/household.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-01 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | df6151787808a2ac957687d9d27bf9909149bbc896bdbecb8ea19e94f09252d8 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | d84684dc95dd51253995ab05880f95d98a4e73a17ec5923e876209598d9fdefc |
| lines judged | 46 |
| match / mismatch / unclear / missing | 45 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 13, 14, 15, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 13, 14, 15, 17, 18, 19, 23, 39, 40, 41, 43, 44, 66 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 2, 4, 5, 6, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 2, 4, 5, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| p501 | 2025 returns; PDF created 2026-02-04 | 6, 8, 9, 11 | cited pages | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 6, 8, 11 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |
| f8889 | 2025; created 2025-03-28 | 1 | whole document | f1ae3589453f3dd1d5277a79409bd7d0bf4772715fa8bd11d58126e6f387c0cf | - | 85ba6183eb2c35cf7b6d63eb6fd515be7234f5f938da39d7d000a6a7f2359d4e |
| i1040s8812 | 2025; printed date 2026-01-23 | 2 | pages named by another document's citation | fd50a5266cc20aa5a31de0535658793f75c7abbb12fd83b65dc5b21c6ede2765 | 2 | e6ba91f54df679c9c19c23169c369f14bff012ba2fe110c3973bde59676c1d45 |

## Lines

### persons — Number of people on the return (you, and your spouse if filing jointly)
Status: **MATCH**

Model: Counts the taxpayer and spouse on a joint return as described.

### taxpayers — Number of entries for you
Status: **MATCH**

Model: Counts the taxpayer entries, one for the filer.

### spouses — Number of entries for your spouse
Status: **MATCH**

Model: Counts spouse entries, which exist only on a joint return.

### roster_ok — One entry for you, and one for your spouse exactly when filing jointly
Status: **MATCH**

Model: Checks one filer and one spouse only for MFJ; the under-16 refusal is a named program entry check.

### roster_bad — The people entered do not match the filing status
Status: **MATCH**

Model: Correctly negates the roster check.

### hsa_people — Number of people on the return with a Form 8889
Status: **MATCH**

Model: Counts people with a Form 8889, consistent with the separate Form 8889 rule for spouses.

### hsa_both — You and your spouse each have a Form 8889
Status: **MATCH**

Model: Two people with Forms 8889 means both spouses have one on a joint return.

### hsa_split_count — Number of Forms 8889 using the spouse rule of line 6
Status: **MATCH**

Model: Counts Forms 8889 using the line 6 spouse rule for separate HSAs with family coverage.

### hsa_agreed_count — Number of Forms 8889 using an agreed allocation
Status: **MATCH**

Model: Counts Forms 8889 using an agreed allocation under the line 6 spouse rule.

### hsa_step1_sum — Both spouses Step 1 limits added together
Status: **MATCH**

Model: Adds the spouses' Step 1 refigured line 5 limits.

### hsa_share_sum — Both spouses parts of the Step 1 limit added together
Status: **MATCH**

Model: Adds the spouses' allocated parts of the Step 1 limit.

### work_ssn_count — Number of people on the return with an SSN valid for employment
Status: **MATCH**

Model: Counts people with an SSN valid for employment issued before the due date.

### any_work_ssn — You, or your spouse if filing jointly, have an SSN valid for employment
Status: **MATCH**

Model: True when at least one filer or spouse has a work-valid SSN.

### eic_ssn_count — Number of people on the return with an SSN valid for the EIC
Status: **MATCH**

Model: Counts people with an SSN valid for EIC purposes issued by the due date.

### all_eic_ssn — You, and your spouse if filing jointly, have SSNs valid for the EIC
Status: **MATCH**

Model: Requires every filer/spouse on the return to have an EIC-valid SSN.

### under16_count — Number of people on the return under age 16 at the end of 2025
Status: **MATCH**

Model: Counts people on the return entered as under age 16 at the end of 2025.

### filer_under16 — You, or your spouse if filing jointly, were under age 16 at the end of 2025
Status: **MATCH**

Model: True when any filer or spouse entry is under age 16.

### tin_count — Number of people on the return with an SSN or ITIN, or who have applied for an ITIN
Status: **MATCH**

Model: Counts people with an SSN or ITIN, including an ITIN application, as the CTC/ODC identity rules allow.

### all_tin — You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
Status: **MATCH**

Model: Requires every filer/spouse to have an SSN or ITIN or an ITIN application.

### id_count — Number of people on the return with an SSN valid for employment or an SSN or ITIN
Status: **MATCH**

Model: Counts people satisfying the work-valid SSN or SSN/ITIN identification tests.

### ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid
Status: **MATCH**

Model: Matches the CTC/ODC filer identification rule: at least one work-valid SSN and the other persons have SSN/ITIN identification.

### taxpayer_work_ssn_count — Your entry, if the answer is yes
Status: **MATCH**

Model: Counts the taxpayer entry when the work-valid SSN answer is yes.

### taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: True when the taxpayer has a work-valid SSN.

### home_cost — Did you pay over half the cost of keeping up your home for 2025?
Status: **MATCH**

Model: Matches the Pub. 501 cost-of-keeping-up-a-home definition and exclusions.

### unmarried — Were you unmarried, or considered unmarried under the head of household rules, at the end
Status: **MATCH**

Model: Matches the head-of-household considered-unmarried rules, including spouse death and married-living-apart.

### married — Were you married at the end of 2025?
Status: **MATCH**

Model: Matches the Pub. 501 marital-status rules, including common law, annulment, and interlocutory divorce.

### community_property — Did you live in a community property state at any time in 2025?
Status: **MATCH**

Model: Lists the community property states named in the IRS text.

### hoh_community_property — Married, filing as head of household, and living in a community property state
Status: **MATCH**

Model: Identifies a married HOH filer in a community property state, matching the special-rules caution.

### credit_disallowed — Was your EIC for a year after 1996, or your child tax credit, additional child tax credit
Status: **MATCH**

Model: Matches the Form 8862 disallowance periods for EIC and CTC/ACTC/ODC.

### test1_persons — Number of parents who qualify you under Test 1
Status: **MATCH**

Model: Counts parents qualifying under HOH Test 1, with parents living with the filer routed to Test 2.

### test2_persons — Number of persons who qualify you under Test 2
Status: **MATCH**

Model: Counts Test 2 persons who lived with the filer long enough, with home cost tested on the household form.

### test2_absence_persons — Number of persons who would qualify you under Test 2 only by counting an absence head of h
Status: **MATCH**

Model: Counts persons who would qualify only by counting an absence the program does not count.

### hoh_absence — Head of household turns on a person who lived with you more than half the year only by cou
Status: **MATCH**

Model: Flags HOH eligibility that turns on an uncounted temporary absence, matching the named refusal.

### test1_met — Test 1 met
Status: **MATCH**

Model: True when at least one parent qualifies under Test 1.

### test2_met — Test 2 met, having paid over half the cost of keeping up your own home
Status: **MATCH**

Model: True when the filer paid over half the home cost and at least one Test 2 person qualifies.

### hoh_eligible — Unmarried or considered unmarried, and Test 1 or Test 2 applies
Status: **MATCH**

Model: Matches the HOH rule: unmarried or considered unmarried and Test 1 or Test 2 applies, with named exclusions.

### hoh_fails — Head of household checked without meeting its tests
Status: **MATCH**

Model: Flags an HOH filing status without meeting the HOH tests.

### qss_eligible — Do all five qualifying surviving spouse tests apply to you?
Status: **MATCH**

Model: Matches the five QSS tests; the kidnapped-child rule is expressly excluded as outside this tool.

### qss_fails — Qualifying surviving spouse checked without meeting its tests
Status: **MATCH**

Model: Flags a QSS filing status when the five QSS tests are not met.

### rdp — Were you a registered domestic partner in Nevada, Washington or California at any time in
Status: **MATCH**

Model: Matches the registered-domestic-partner question for Nevada, Washington, and California.

### spouse_died_2025 — Did your spouse die in 2025?
Status: **MATCH**

Model: Records whether the spouse died in 2025, a fact relevant to filing status.

### widowed_2025 — Filing as single or head of household although your spouse died in 2025
Status: **MATCH**

Model: Flags single or HOH status when the spouse died in 2025, who is considered married for the year.

### cp_married — Married at any time in 2025 while living in a community property state, though not married
Status: **MATCH**

Model: Matches the community property rule for a marriage during the year before divorce or separation.

### cp_marriage_ended — Not filing jointly, and married for part of 2025 while living in a community property stat
Status: **MATCH**

Model: Identifies a non-joint filer married during 2025 in a community property state.

### rdp_community_property — Not filing jointly, living in a community property state, and a registered domestic partne
Status: **MATCH**

Model: Identifies a non-joint filer in a community property state who is a Nevada, Washington, or California registered domestic partner.

### filing_status_conflict — The filing status conflicts with the marriage facts entered
Status: **MISMATCH**

Restated: (f1040 line Filing Status = 'single' and helper "Were you married at the end of 2025?" = true or f1040 line Filing Status = 'mfj' and helper "Were you married at the end of 2025?" = false and helper "Did your spouse die in 2025?" = false)

Model: The restatement only flags single and MFJ conflicts; IRS says "Check the 'Married filing separately' box ... if you are married at the end of 2025 and file a separate return," so MFS with not married should also be flagged.

Ruling: scope — i1040gi p. 14, Married Filing Separately: a separate return is refused for the whole return by `s3.mfs` on `scope.ready`, so a still-married filer who checks MFS never reaches line 12e and cannot produce the conflict the reviewer describes. The gate covers the single and joint contradictions; HOH and QSS have their own tests, and a joint death-year return stays supported. BUG-0286 records the entry check.

## Raw response

```yaml
lines:
  - key: "persons"
    status: MATCH
    reason: "Counts the taxpayer and spouse on a joint return as described."
  - key: "taxpayers"
    status: MATCH
    reason: "Counts the taxpayer entries, one for the filer."
  - key: "spouses"
    status: MATCH
    reason: "Counts spouse entries, which exist only on a joint return."
  - key: "roster_ok"
    status: MATCH
    reason: "Checks one filer and one spouse only for MFJ; the under-16 refusal is a named program entry check."
  - key: "roster_bad"
    status: MATCH
    reason: "Correctly negates the roster check."
  - key: "hsa_people"
    status: MATCH
    reason: "Counts people with a Form 8889, consistent with the separate Form 8889 rule for spouses."
  - key: "hsa_both"
    status: MATCH
    reason: "Two people with Forms 8889 means both spouses have one on a joint return."
  - key: "hsa_split_count"
    status: MATCH
    reason: "Counts Forms 8889 using the line 6 spouse rule for separate HSAs with family coverage."
  - key: "hsa_agreed_count"
    status: MATCH
    reason: "Counts Forms 8889 using an agreed allocation under the line 6 spouse rule."
  - key: "hsa_step1_sum"
    status: MATCH
    reason: "Adds the spouses' Step 1 refigured line 5 limits."
  - key: "hsa_share_sum"
    status: MATCH
    reason: "Adds the spouses' allocated parts of the Step 1 limit."
  - key: "work_ssn_count"
    status: MATCH
    reason: "Counts people with an SSN valid for employment issued before the due date."
  - key: "any_work_ssn"
    status: MATCH
    reason: "True when at least one filer or spouse has a work-valid SSN."
  - key: "eic_ssn_count"
    status: MATCH
    reason: "Counts people with an SSN valid for EIC purposes issued by the due date."
  - key: "all_eic_ssn"
    status: MATCH
    reason: "Requires every filer/spouse on the return to have an EIC-valid SSN."
  - key: "under16_count"
    status: MATCH
    reason: "Counts people on the return entered as under age 16 at the end of 2025."
  - key: "filer_under16"
    status: MATCH
    reason: "True when any filer or spouse entry is under age 16."
  - key: "tin_count"
    status: MATCH
    reason: "Counts people with an SSN or ITIN, including an ITIN application, as the CTC/ODC identity rules allow."
  - key: "all_tin"
    status: MATCH
    reason: "Requires every filer/spouse to have an SSN or ITIN or an ITIN application."
  - key: "id_count"
    status: MATCH
    reason: "Counts people satisfying the work-valid SSN or SSN/ITIN identification tests."
  - key: "ctc_ssn"
    status: MATCH
    reason: "Matches the CTC/ODC filer identification rule: at least one work-valid SSN and the other persons have SSN/ITIN identification."
  - key: "taxpayer_work_ssn_count"
    status: MATCH
    reason: "Counts the taxpayer entry when the work-valid SSN answer is yes."
  - key: "taxpayer_work_ssn"
    status: MATCH
    reason: "True when the taxpayer has a work-valid SSN."
  - key: "home_cost"
    status: MATCH
    reason: "Matches the Pub. 501 cost-of-keeping-up-a-home definition and exclusions."
  - key: "unmarried"
    status: MATCH
    reason: "Matches the head-of-household considered-unmarried rules, including spouse death and married-living-apart."
  - key: "married"
    status: MATCH
    reason: "Matches the Pub. 501 marital-status rules, including common law, annulment, and interlocutory divorce."
  - key: "community_property"
    status: MATCH
    reason: "Lists the community property states named in the IRS text."
  - key: "hoh_community_property"
    status: MATCH
    reason: "Identifies a married HOH filer in a community property state, matching the special-rules caution."
  - key: "credit_disallowed"
    status: MATCH
    reason: "Matches the Form 8862 disallowance periods for EIC and CTC/ACTC/ODC."
  - key: "test1_persons"
    status: MATCH
    reason: "Counts parents qualifying under HOH Test 1, with parents living with the filer routed to Test 2."
  - key: "test2_persons"
    status: MATCH
    reason: "Counts Test 2 persons who lived with the filer long enough, with home cost tested on the household form."
  - key: "test2_absence_persons"
    status: MATCH
    reason: "Counts persons who would qualify only by counting an absence the program does not count."
  - key: "hoh_absence"
    status: MATCH
    reason: "Flags HOH eligibility that turns on an uncounted temporary absence, matching the named refusal."
  - key: "test1_met"
    status: MATCH
    reason: "True when at least one parent qualifies under Test 1."
  - key: "test2_met"
    status: MATCH
    reason: "True when the filer paid over half the home cost and at least one Test 2 person qualifies."
  - key: "hoh_eligible"
    status: MATCH
    reason: "Matches the HOH rule: unmarried or considered unmarried and Test 1 or Test 2 applies, with named exclusions."
  - key: "hoh_fails"
    status: MATCH
    reason: "Flags an HOH filing status without meeting the HOH tests."
  - key: "qss_eligible"
    status: MATCH
    reason: "Matches the five QSS tests; the kidnapped-child rule is expressly excluded as outside this tool."
  - key: "qss_fails"
    status: MATCH
    reason: "Flags a QSS filing status when the five QSS tests are not met."
  - key: "rdp"
    status: MATCH
    reason: "Matches the registered-domestic-partner question for Nevada, Washington, and California."
  - key: "spouse_died_2025"
    status: MATCH
    reason: "Records whether the spouse died in 2025, a fact relevant to filing status."
  - key: "widowed_2025"
    status: MATCH
    reason: "Flags single or HOH status when the spouse died in 2025, who is considered married for the year."
  - key: "cp_married"
    status: MATCH
    reason: "Matches the community property rule for a marriage during the year before divorce or separation."
  - key: "cp_marriage_ended"
    status: MATCH
    reason: "Identifies a non-joint filer married during 2025 in a community property state."
  - key: "rdp_community_property"
    status: MATCH
    reason: "Identifies a non-joint filer in a community property state who is a Nevada, Washington, or California registered domestic partner."
  - key: "filing_status_conflict"
    status: MISMATCH
    reason: "The restatement only flags single and MFJ conflicts; IRS says \"Check the 'Married filing separately' box ... if you are married at the end of 2025 and file a separate return,\" so MFS with not married should also be flagged."
```
