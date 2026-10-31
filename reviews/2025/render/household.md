# Render comparison — household

The rendered English of every printed line of `Household facts for dependents and head of household` (`rendered/2025/household.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 48d1697b32ed44c87f616892fa7274b2288930ee3d158a0c0715fc8299d14339 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 6c07c8cf3e4ccbb17ac1cfbccb02fef0bdc91feb9169993b37332b137c0f686d |
| lines judged | 39 |
| match / mismatch / unclear / missing | 38 / 0 / 1 / 0 |
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

Model: Counts one entry each for you and, on a joint return, your spouse, which fits the form's taxpayer and spouse structure. It is a plain count of the people on the return.

### taxpayers — Number of entries for you
Status: **MATCH**

Model: Counts the entries identified as yours, as the label says.

### spouses — Number of entries for your spouse
Status: **MATCH**

Model: Counts the entries identified as your spouse's, as the label says.

### roster_ok — One entry for you, and one for your spouse exactly when filing jointly
Status: **MATCH**

Model: Requires one taxpayer entry, plus one spouse entry exactly when married filing jointly, consistent with the Form 1040 filing status and spouse lines. The under-16 refusal is a named narrowing, and it correctly says the rule is not in the instructions; the only under-16 text given is the Self-Select PIN caution for first-time filers.

### roster_bad — The people entered do not match the filing status
Status: **MATCH**

Model: This is the direct negation of roster_ok, as labeled.

### hsa_people — Number of people on the return with a Form 8889
Status: **MATCH**

Model: Counts people with at least one Form 8889, consistent with 'complete a separate Form 8889 for each of you.'

### hsa_both — You and your spouse each have a Form 8889
Status: **MATCH**

Model: A count of two people with Forms 8889 means you and your spouse each have one, as labeled.

### hsa_split_count — Number of Forms 8889 using the spouse rule of line 6
Status: **MATCH**

Model: Counts Forms 8889 flagged for spouses with separate HSAs and family coverage at any time during 2025, the condition stated in the line 6 instructions.

### hsa_agreed_count — Number of Forms 8889 using an agreed allocation
Status: **MATCH**

Model: Counts flagged forms using an agreed allocation, which matches 'unless you both agree on a different allocation.'

### hsa_step1_sum — Both spouses Step 1 limits added together
Status: **MATCH**

Model: Adds each spouse's Step 1 limit, refigured from the worksheet amounts for family-coverage months less line 4, as the line 6 instructions describe. The glossary sets f8889 line 4 to $0 with no refusal shown, although the form says to enter Archer MSA contributions from Form 8853; that issue belongs to f8889 line 4 but flows into this sum.

### hsa_share_sum — Both spouses parts of the Step 1 limit added together
Status: **MATCH**

Model: Adds each spouse's part of the Step 1 limit, using an equal split or an agreed allocation as in Steps 2 and 3 of the line 6 instructions. It inherits the same f8889 line 4 $0 issue when the split is equal.

### work_ssn_count — Number of people on the return with an SSN valid for employment
Status: **MATCH**

Model: Counts people with an SSN 'valid for employment and issued before the due date of your return (including extensions).' The label's omission of extensions is only wording.

### any_work_ssn — You, or your spouse if filing jointly, have an SSN valid for employment
Status: **MATCH**

Model: Matches 'only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC.'

### eic_ssn_count — Number of people on the return with an SSN valid for the EIC
Status: **MATCH**

Model: Counts people with an SSN valid for the EIC and issued on or before the due date, as in EIC Step 1, question 2.

### all_eic_ssn — You, and your spouse if filing jointly, have SSNs valid for the EIC
Status: **MATCH**

Model: Requiring every person on the return to qualify matches 'Do you, and your spouse if filing a joint return, have a social security number' valid for EIC purposes.

### under16_count — Number of people on the return under age 16 at the end of 2025
Status: **MATCH**

Model: Counts people on the return who were under age 16 at the end of 2025, as labeled. The count supports the program's own entry check.

### filer_under16 — You, or your spouse if filing jointly, were under age 16 at the end of 2025
Status: **MATCH**

Model: True when at least one person on the return was under 16, as labeled. It serves as the named gate for the roster_ok refusal.

### tin_count — Number of people on the return with an SSN or ITIN, or who have applied for an ITIN
Status: **MATCH**

Model: Counts people with an SSN or ITIN issued on or before the due date or an ITIN application, matching Step 5: 'Answer “Yes” if you are applying for an ITIN on or before the return due date.'

### all_tin — You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
Status: **MATCH**

Model: Requiring all people on the return to qualify matches 'you, and your spouse if filing jointly, must have either an SSN or ITIN' for the credit for other dependents.

### id_count — Number of people on the return with an SSN valid for employment or an SSN or ITIN
Status: **MATCH**

Model: Counts people holding either an SSN valid for employment or an SSN or ITIN, the two identifications named in the child tax credit rule. It is correct as a supporting count for ctc_ssn.

### ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid
Status: **MATCH**

Model: Requires one valid-for-employment SSN and identification for everyone on the return. This matches 'only one spouse is required to have a valid SSN' and 'The other spouse must have either an SSN or ITIN.'

### taxpayer_work_ssn_count — Your entry, if the answer is yes
Status: **MATCH**

Model: Counts your own entry when it has an SSN valid for employment, which is the condition the label describes.

### taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: True when your own entry has an SSN valid for employment and issued before the due date, matching the SSN definition in the instructions.

### home_cost — Did you pay over half the cost of keeping up your home for 2025?
Status: **MATCH**

Model: The included and excluded costs match Pub. 501. Its 'person who lives in the home' wording is slightly broader than Pub. 501's 'child’s or qualifying person’s name' but keeps the same meaning that such funds are not paid by you.

### unmarried — Were you unmarried, or considered unmarried under the head of household rules, at the end
Status: **MATCH**

Model: The input asks the condition stated in the instructions: 'only if you are unmarried (or considered unmarried).'

### married — Were you married at the end of 2025?
Status: **MATCH**

Model: The input asks about marital status at the end of 2025 and includes married people considered unmarried, a category the head of household instructions recognize.

### community_property — Did you live in a community property state at any time in 2025?
Status: **MATCH**

Model: The nine states match the list under Community Property States in the instructions.

### hoh_community_property — Married, filing as head of household, and living in a community property state
Status: **MATCH**

Model: Combines head of household status, marriage and community property residence, as labeled. It serves as the gate for the named Form 8958 and Pub. 555 refusal, which the instructions support.

### credit_disallowed — Was your EIC for a year after 1996, or your child tax credit, additional child tax credit
Status: **MATCH**

Model: The years, credits, math or clerical error carve-out, and 2- and 10-year periods match the Form 8862 and improper-claim text. 'Disallowed' versus 'denied' for the post-2015 credits is only wording.

### test1_persons — Number of parents who qualify you under Test 1
Status: **MATCH**

Model: Counts parents who qualify you under Test 1, which covers a parent you can claim whose main home you paid over half the cost of keeping up; 'Your parent didn't have to live with you.' The per-dependent helper is not defined in the glossary, so only its label and the count could be checked.

### test2_persons — Number of persons who qualify you under Test 2
Status: **MATCH**

Model: Counts persons who lived with you for more than half the year, or more than half the part of the year they were alive, matching Test 2 and Pub. 501. The per-dependent helper is not defined in the glossary, so only its label and the count could be checked.

### test1_met — Test 1 met
Status: **MATCH**

Model: At least one qualifying parent under Test 1 means the test is met. The home-cost condition is carried in the per-parent helper, which is appropriate because the home may be the parent's own.

### test2_met — Test 2 met, having paid over half the cost of keeping up your own home
Status: **MATCH**

Model: Requires a Test 2 person and over half the cost of your home, matching 'You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived.'

### hoh_eligible — Unmarried or considered unmarried, and Test 1 or Test 2 applies
Status: **MATCH**

Model: Matches 'only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies.' The refusal names the excluded community property case and Form 8958 and Pub. 555, which the instructions cite.

### hoh_fails — Head of household checked without meeting its tests
Status: **MATCH**

Model: True when the head of household box is selected and the eligibility test fails, as labeled.

### qss_eligible — Do all five qualifying surviving spouse tests apply to you?
Status: **MATCH**

Model: The five tests track the Qualifying Surviving Spouse instructions, including the 2023 or 2024 death, the $5,200 and joint-return exceptions, and the time-lived and adoption rules. The home-cost wording also agrees with Pub. 501 in substance.

### qss_fails — Qualifying surviving spouse checked without meeting its tests
Status: **MATCH**

Model: True when the qualifying surviving spouse box is selected and the five-test answer is no, as labeled.

### rdp — Were you a registered domestic partner in Nevada, Washington or California at any time in
Status: **MATCH**

Model: The input asks about the status named in the instructions: 'A registered domestic partner in Nevada, Washington, or California.' The text gives no timing rule that contradicts 'at any time in 2025.'

### rdp_community_property — Not filing jointly, living in a community property state, and a registered domestic partne
Status: **UNCLEAR**

Restated: f1040 line Filing Status ≠ 'mfj' and helper "Did you live in a community property state at any time in 2025?" = true and helper "Were you a registered domestic partner in Nevada, Washington or California at any time in 2025?" = true

Model: The text says a registered domestic partner in these states 'must generally report half the combined community income' but states no exception for joint filers. The pages given do not show whether this gate's 'not filing jointly' condition is correct; Form 8958 and Pub. 555 would be needed.

Ruling: interface gap; i1040gi p. 23, Community Property States: "Nevada, Washington, and California domestic partners. A registered domestic partner in Nevada, Washington, or California must generally report half the combined community income of the individual and their domestic partner. See Form 8958 and Pub. 555." The model asks whether the gate's 'not filing jointly' condition is right and says the pages given do not decide it. What decides it is p501 p. 6, not among the pages given (the render had p501 p. 9 only): "Individuals who have entered into a registered domestic partnership, civil union, or other similar relationship that isn't denominated as a marriage under the law of the state ... aren't lawfully married for federal tax purposes", and a joint return requires that "You were married at the end of 2025" or that your spouse died in 2025 (i1040gi p. 13, Married Filing Jointly). A joint filer is therefore filing with a spouse, not a domestic partner, and the joint return already reports both spouses' combined income; the partner rule reaches a partner on a single, head of household or qualifying surviving spouse return, which is where the gate refuses (the separate married-filing-separately refusal, s3.mfs, covers the remaining status). The restatement (status not mfj, community property state, registered domestic partner) is otherwise the source's condition. The line is unchanged since fix round 2, where it was checked against p. 23, p525 p. 24 and p501 p. 6. Project stands.

## Raw response

```yaml
```yaml
lines:
  - key: "persons"
    status: MATCH
    reason: "Counts one entry each for you and, on a joint return, your spouse, which fits the form's taxpayer and spouse structure. It is a plain count of the people on the return."
  - key: "taxpayers"
    status: MATCH
    reason: "Counts the entries identified as yours, as the label says."
  - key: "spouses"
    status: MATCH
    reason: "Counts the entries identified as your spouse's, as the label says."
  - key: "roster_ok"
    status: MATCH
    reason: "Requires one taxpayer entry, plus one spouse entry exactly when married filing jointly, consistent with the Form 1040 filing status and spouse lines. The under-16 refusal is a named narrowing, and it correctly says the rule is not in the instructions; the only under-16 text given is the Self-Select PIN caution for first-time filers."
  - key: "roster_bad"
    status: MATCH
    reason: "This is the direct negation of roster_ok, as labeled."
  - key: "hsa_people"
    status: MATCH
    reason: "Counts people with at least one Form 8889, consistent with 'complete a separate Form 8889 for each of you.'"
  - key: "hsa_both"
    status: MATCH
    reason: "A count of two people with Forms 8889 means you and your spouse each have one, as labeled."
  - key: "hsa_split_count"
    status: MATCH
    reason: "Counts Forms 8889 flagged for spouses with separate HSAs and family coverage at any time during 2025, the condition stated in the line 6 instructions."
  - key: "hsa_agreed_count"
    status: MATCH
    reason: "Counts flagged forms using an agreed allocation, which matches 'unless you both agree on a different allocation.'"
  - key: "hsa_step1_sum"
    status: MATCH
    reason: "Adds each spouse's Step 1 limit, refigured from the worksheet amounts for family-coverage months less line 4, as the line 6 instructions describe. The glossary sets f8889 line 4 to $0 with no refusal shown, although the form says to enter Archer MSA contributions from Form 8853; that issue belongs to f8889 line 4 but flows into this sum."
  - key: "hsa_share_sum"
    status: MATCH
    reason: "Adds each spouse's part of the Step 1 limit, using an equal split or an agreed allocation as in Steps 2 and 3 of the line 6 instructions. It inherits the same f8889 line 4 $0 issue when the split is equal."
  - key: "work_ssn_count"
    status: MATCH
    reason: "Counts people with an SSN 'valid for employment and issued before the due date of your return (including extensions).' The label's omission of extensions is only wording."
  - key: "any_work_ssn"
    status: MATCH
    reason: "Matches 'only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC.'"
  - key: "eic_ssn_count"
    status: MATCH
    reason: "Counts people with an SSN valid for the EIC and issued on or before the due date, as in EIC Step 1, question 2."
  - key: "all_eic_ssn"
    status: MATCH
    reason: "Requiring every person on the return to qualify matches 'Do you, and your spouse if filing a joint return, have a social security number' valid for EIC purposes."
  - key: "under16_count"
    status: MATCH
    reason: "Counts people on the return who were under age 16 at the end of 2025, as labeled. The count supports the program's own entry check."
  - key: "filer_under16"
    status: MATCH
    reason: "True when at least one person on the return was under 16, as labeled. It serves as the named gate for the roster_ok refusal."
  - key: "tin_count"
    status: MATCH
    reason: "Counts people with an SSN or ITIN issued on or before the due date or an ITIN application, matching Step 5: 'Answer “Yes” if you are applying for an ITIN on or before the return due date.'"
  - key: "all_tin"
    status: MATCH
    reason: "Requiring all people on the return to qualify matches 'you, and your spouse if filing jointly, must have either an SSN or ITIN' for the credit for other dependents."
  - key: "id_count"
    status: MATCH
    reason: "Counts people holding either an SSN valid for employment or an SSN or ITIN, the two identifications named in the child tax credit rule. It is correct as a supporting count for ctc_ssn."
  - key: "ctc_ssn"
    status: MATCH
    reason: "Requires one valid-for-employment SSN and identification for everyone on the return. This matches 'only one spouse is required to have a valid SSN' and 'The other spouse must have either an SSN or ITIN.'"
  - key: "taxpayer_work_ssn_count"
    status: MATCH
    reason: "Counts your own entry when it has an SSN valid for employment, which is the condition the label describes."
  - key: "taxpayer_work_ssn"
    status: MATCH
    reason: "True when your own entry has an SSN valid for employment and issued before the due date, matching the SSN definition in the instructions."
  - key: "home_cost"
    status: MATCH
    reason: "The included and excluded costs match Pub. 501. Its 'person who lives in the home' wording is slightly broader than Pub. 501's 'child’s or qualifying person’s name' but keeps the same meaning that such funds are not paid by you."
  - key: "unmarried"
    status: MATCH
    reason: "The input asks the condition stated in the instructions: 'only if you are unmarried (or considered unmarried).'"
  - key: "married"
    status: MATCH
    reason: "The input asks about marital status at the end of 2025 and includes married people considered unmarried, a category the head of household instructions recognize."
  - key: "community_property"
    status: MATCH
    reason: "The nine states match the list under Community Property States in the instructions."
  - key: "hoh_community_property"
    status: MATCH
    reason: "Combines head of household status, marriage and community property residence, as labeled. It serves as the gate for the named Form 8958 and Pub. 555 refusal, which the instructions support."
  - key: "credit_disallowed"
    status: MATCH
    reason: "The years, credits, math or clerical error carve-out, and 2- and 10-year periods match the Form 8862 and improper-claim text. 'Disallowed' versus 'denied' for the post-2015 credits is only wording."
  - key: "test1_persons"
    status: MATCH
    reason: "Counts parents who qualify you under Test 1, which covers a parent you can claim whose main home you paid over half the cost of keeping up; 'Your parent didn't have to live with you.' The per-dependent helper is not defined in the glossary, so only its label and the count could be checked."
  - key: "test2_persons"
    status: MATCH
    reason: "Counts persons who lived with you for more than half the year, or more than half the part of the year they were alive, matching Test 2 and Pub. 501. The per-dependent helper is not defined in the glossary, so only its label and the count could be checked."
  - key: "test1_met"
    status: MATCH
    reason: "At least one qualifying parent under Test 1 means the test is met. The home-cost condition is carried in the per-parent helper, which is appropriate because the home may be the parent's own."
  - key: "test2_met"
    status: MATCH
    reason: "Requires a Test 2 person and over half the cost of your home, matching 'You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived.'"
  - key: "hoh_eligible"
    status: MATCH
    reason: "Matches 'only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies.' The refusal names the excluded community property case and Form 8958 and Pub. 555, which the instructions cite."
  - key: "hoh_fails"
    status: MATCH
    reason: "True when the head of household box is selected and the eligibility test fails, as labeled."
  - key: "qss_eligible"
    status: MATCH
    reason: "The five tests track the Qualifying Surviving Spouse instructions, including the 2023 or 2024 death, the $5,200 and joint-return exceptions, and the time-lived and adoption rules. The home-cost wording also agrees with Pub. 501 in substance."
  - key: "qss_fails"
    status: MATCH
    reason: "True when the qualifying surviving spouse box is selected and the five-test answer is no, as labeled."
  - key: "rdp"
    status: MATCH
    reason: "The input asks about the status named in the instructions: 'A registered domestic partner in Nevada, Washington, or California.' The text gives no timing rule that contradicts 'at any time in 2025.'"
  - key: "rdp_community_property"
    status: UNCLEAR
    reason: "The text says a registered domestic partner in these states 'must generally report half the combined community income' but states no exception for joint filers. The pages given do not show whether this gate's 'not filing jointly' condition is correct; Form 8958 and Pub. 555 would be needed."
```
```
