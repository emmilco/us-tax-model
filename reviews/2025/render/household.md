# Render comparison — household

The rendered English of every printed line of `Household facts for dependents and head of household` (`rendered/2025/household.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | ceffdf7bb06d34d65c553103d422cbf6a3c33937807d371f2d61d6d68d20c631 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | e89c8acf56b6ac52b1f4b39d5fe29e0394cfc792d6fdc49ad1a313ec2e57f213 |
| lines judged | 48 |
| match / mismatch / unclear / missing | 48 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 13, 14, 15, 17, 18, 19, 23, 36, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 66, 93, 94, 95, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 13, 14, 15, 17, 18, 19, 23, 36, 39, 40, 41, 42, 43, 44, 45, 66, 93, 95, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8889 | 2025 | 2, 4, 5, 6, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 2, 4, 5, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| i1040s8812 | 2025; printed date 2026-01-23 | 2, 8 | cited pages | fd50a5266cc20aa5a31de0535658793f75c7abbb12fd83b65dc5b21c6ede2765 | 2 | e6ba91f54df679c9c19c23169c369f14bff012ba2fe110c3973bde59676c1d45 |
| p501 | 2025 returns; PDF created 2026-02-04 | 6, 8, 9, 11 | cited pages | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 6, 8, 11 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |
| f8889 | 2025; created 2025-03-28 | 1 | whole document | f1ae3589453f3dd1d5277a79409bd7d0bf4772715fa8bd11d58126e6f387c0cf | - | 85ba6183eb2c35cf7b6d63eb6fd515be7234f5f938da39d7d000a6a7f2359d4e |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| i1040sc | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| iw2w3 | 2025; printed date 2025-02-19 | 18 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 18 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 34, 37, 39, 41, 59, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p560 | For use in preparing 2025 returns | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 39, 40 | cited pages | 38bbfa2efb2894e2527d66cd3478f33c6ceae4b777f78674c22bec16db9809aa | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 40 | 7ef279c8f34addc2ff13420e35fab4a092bf8027f53907c28a5f46d2c21da737 |
| p538 | None | 17 | pages named by another document's citation | 4186d7aaa8f711c9a524b87fac1e3df05640b6d66130093b2469480acb06ef6c | 17 | f500211df18a4aafd843e48bbad4b9102c598cf5ccc0fae96c7814a4bef0ae00 |

## Lines

### persons — Number of people on the return (you, and your spouse if filing jointly)
Status: **MATCH**

Model: Counts one entry per person on the return, which is you and, on a joint return, your spouse. This is the population the SSN/ITIN tests apply to: 'you, and your spouse if filing jointly'.

### taxpayers — Number of entries for you
Status: **MATCH**

Model: Counts the filer's own entries. This supports the roster consistency check and needs no IRS operand.

### spouses — Number of entries for your spouse
Status: **MATCH**

Model: Counts the spouse's entries. This supports the roster consistency check and needs no IRS operand.

### roster_ok — One entry for you, and one for your spouse exactly when filing jointly
Status: **MATCH**

Model: Requires one taxpayer entry, plus one spouse entry exactly when the status is married filing jointly, as joint-return reporting requires. The under-16 refusal is an owner-chosen entry check; it is disclosed as not drawn from the instructions and names what it excludes.

### roster_bad — The people entered do not match the filing status
Status: **MATCH**

Model: This is the negation of roster_ok.

### hsa_people — Number of people on the return with a Form 8889
Status: **MATCH**

Model: Counts people with a Form 8889. The i8889 says 'If married filing jointly and both you and your spouse have HSAs, complete a separate Form 8889 for each of you.'

### hsa_both — You and your spouse each have a Form 8889
Status: **MATCH**

Model: Both spouses have a Form 8889 when the count equals 2, which is the separate-HSAs case of line 6.

### hsa_split_count — Number of Forms 8889 using the spouse rule of line 6
Status: **MATCH**

Model: Counts the Forms 8889 that use the line 6 rule for 'Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025'.

### hsa_agreed_count — Number of Forms 8889 using an agreed allocation
Status: **MATCH**

Model: Counts the line 6 forms that use the alternative 'unless you both agree on a different allocation'.

### hsa_step1_sum — Both spouses Step 1 limits added together
Status: **MATCH**

Model: Adds both spouses' Step 1 refigured limits. This supports checking that the Step 2 division between spouses is consistent.

### hsa_share_sum — Both spouses parts of the Step 1 limit added together
Status: **MATCH**

Model: Adds both spouses' allocated parts. Under line 6 Steps 2–3 these should total the Step 1 limit.

### work_ssn_count — Number of people on the return with an SSN valid for employment
Status: **MATCH**

Model: Counts people whose SSN is 'valid for employment and issued before the due date of your return (including extensions)', the CTC definition of a valid SSN.

### any_work_ssn — You, or your spouse if filing jointly, have an SSN valid for employment
Status: **MATCH**

Model: Matches 'If you are filing a joint return, only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC.'

### eic_ssn_count — Number of people on the return with an SSN valid for the EIC
Status: **MATCH**

Model: Counts people with an SSN valid for the EIC, per Step 1 question 2: 'Do you, and your spouse if filing a joint return, have a social security number issued on or before the due date...'.

### all_eic_ssn — You, and your spouse if filing jointly, have SSNs valid for the EIC
Status: **MATCH**

Model: Step 1 question 2 requires both you and your spouse on a joint return to have such an SSN. Requiring the count to equal the number of people on the return does this.

### under16_count — Number of people on the return under age 16 at the end of 2025
Status: **MATCH**

Model: Counts filers under age 16. It only feeds the owner-declared refusal gate, which is disclosed.

### filer_under16 — You, or your spouse if filing jointly, were under age 16 at the end of 2025
Status: **MATCH**

Model: This is the gate for the disclosed under-16 refusal: any person on the return under age 16.

### tin_count — Number of people on the return with an SSN or ITIN, or who have applied for an ITIN
Status: **MATCH**

Model: Matches Step 5 question 1: 'have either an SSN or ITIN issued on or before the due date ... (Answer "Yes" if you are applying for an ITIN...)'.

### all_tin — You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
Status: **MATCH**

Model: The ODC requires 'you, and your spouse if filing jointly' to have an SSN/ITIN. Every person on the return must qualify, and this checks that.

### id_count — Number of people on the return with an SSN valid for employment or an SSN or ITIN
Status: **MATCH**

Model: Counts people with either a work-valid SSN or an SSN/ITIN issued by the due date. These are the two acceptable identifications for the spouses under the CTC rule.

### ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid
Status: **MATCH**

Model: Matches 'only one spouse is required to have a valid SSN... The other spouse must have either an SSN or ITIN... issued on or before the due date'. The applied-for ITIN is correctly not counted.

### taxpayer_work_ssn_count — Your entry, if the answer is yes
Status: **MATCH**

Model: Restricts the work-valid SSN count to the filer's own entry.

### taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: This is the filer's own work-valid SSN, taken from the count above.

### home_cost — Did you pay over half the cost of keeping up your home for 2025?
Status: **MATCH**

Model: The included and excluded costs follow Pub. 501, Keeping Up a Home. The treatment of funds received in another person's name and of TANF payments follows the Worksheet 1 note.

### unmarried — Were you unmarried, or considered unmarried under the head of household rules, at the end
Status: **MATCH**

Model: The three 'considered unmarried' cases follow i1040gi Head of Household and Pub. 501 Considered Unmarried, including the temporary-absence rule for the spouse. The rule that a spouse who died in 2025 makes you married for the whole year follows Pub. 501 'Spouse died during the year'.

### married — Were you married at the end of 2025?
Status: **MATCH**

Model: Follows the Pub. 501 definition of marriage, common-law marriage, interlocutory decrees, final divorce, separate maintenance, annulment, the domestic partnership exclusion, and the divorce-and-remarriage rule.

### community_property — Did you live in a community property state at any time in 2025?
Status: **MATCH**

Model: Lists the nine community property states named in i1040gi and Pub. 501.

### hoh_community_property — Married, filing as head of household, and living in a community property state
Status: **MATCH**

Model: This is the gate for the Pub. 555/Form 8958 refusal. Pub. 501 warns that 'If you were considered married for part of the year and lived in a community property state ... special rules may apply.'

### credit_disallowed — Was your EIC for a year after 1996, or your child tax credit, additional child tax credit
Status: **MATCH**

Model: Combines the Form 8862 triggers (EIC after 1996, CTC/ACTC/ODC after 2015, reduced or disallowed other than math/clerical error) with the 2- and 10-year bans.

### ctc_disallowed_claim — An earlier credit was reduced or disallowed (or a disallowance period applies) and Schedul
Status: **MATCH**

Model: A CTC/ODC is figured only if Schedule 8812 line 12 is 'Yes': 'Is the amount on line 8 more than the amount on line 11?'.

### eic_disallowed_claim — An earlier credit was reduced or disallowed (or a disallowance period applies) and Steps 1
Status: **MATCH**

Model: An EIC is claimed when Steps 1–5 are passed and the Worksheet line 6 credit is more than zero. It is combined with the prior-disallowance flag.

### test1_persons — Number of parents who qualify you under Test 1
Status: **MATCH**

Model: Test 1 covers a dependent parent whose home was the main home 'for all of 2025'; 'Your parent didn't have to live with you'. A parent living with you is covered through Test 2 instead.

### test2_persons — Number of persons who qualify you under Test 2
Status: **MATCH**

Model: Test 2 covers a qualifying person who lived with you more than half the year. The home-cost condition is tested separately, as the label states.

### test2_absence_persons — Number of persons who would qualify you under Test 2 only by counting an absence head of h
Status: **MATCH**

Model: Counts persons who would qualify only by an absence that fails Pub. 501's rule: 'reasonable to assume the absent person will return ... continue to keep up the home'.

### hoh_absence — Head of household turns on a person who lived with you more than half the year only by cou
Status: **MATCH**

Model: This is the gate for the temporary-absence refusal. It fires only when HOH eligibility turns solely on such a person.

### test1_met — Test 1 met
Status: **MATCH**

Model: Test 1 is met when at least one qualifying parent exists. Paying over half the cost of the parent's home is part of the per-parent test.

### test2_met — Test 2 met, having paid over half the cost of keeping up your own home
Status: **MATCH**

Model: Matches 'You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived for more than half of the year'.

### hoh_eligible — Unmarried or considered unmarried, and Test 1 or Test 2 applies
Status: **MATCH**

Model: Matches 'Check the "Head of household" box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies'. The refusals name the absence and community-property cases they exclude.

### hoh_fails — Head of household checked without meeting its tests
Status: **MATCH**

Model: Flags a head of household status checked without the eligibility tests being met.

### qss_eligible — Do all five qualifying surviving spouse tests apply to you?
Status: **MATCH**

Model: The five tests follow i1040gi and Pub. 501 Qualifying Surviving Spouse, including the exceptions for absences, birth/death and adoption. The kidnapped-child case is disclosed as outside the tool.

### qss_fails — Qualifying surviving spouse checked without meeting its tests
Status: **MATCH**

Model: Flags a qualifying surviving spouse status checked without all five tests being met.

### rdp — Were you a registered domestic partner in Nevada, Washington or California at any time in
Status: **MATCH**

Model: Matches i1040gi: 'Nevada, Washington, and California domestic partners'.

### spouse_died_2025 — Did your spouse die in 2025?
Status: **MATCH**

Model: This is a simple fact input used for the filing status consistency checks.

### widowed_2025 — Filing as single or head of household although your spouse died in 2025
Status: **MATCH**

Model: Pub. 501: 'If your spouse died during the year, you are considered married for the whole year for filing status purposes'. Single or HOH with a 2025 death therefore conflicts.

### cp_married — Married at any time in 2025 while living in a community property state, though not married
Status: **MATCH**

Model: Asks whether you were married for part of the year while living in a community property state, the condition in Pub. 501's community-property caution.

### cp_marriage_ended — Not filing jointly, and married for part of 2025 while living in a community property stat
Status: **MATCH**

Model: Matches Pub. 501: 'If you were considered married for part of the year and lived in a community property state ... special rules may apply'.

### rdp_community_property — Not filing jointly, living in a community property state, and a registered domestic partne
Status: **MATCH**

Model: Matches i1040gi: 'A registered domestic partner in Nevada, Washington, or California must generally report half the combined community income'.

### filing_status_conflict — The filing status conflicts with the marriage facts entered
Status: **MATCH**

Model: Single requires being unmarried on December 31. Married filing jointly requires being married at year end or a spouse who died in 2025, per i1040gi Single and Married Filing Jointly.

## Raw response

```yaml
```yaml
lines:
  - key: "persons"
    status: MATCH
    reason: "Counts one entry per person on the return, which is you and, on a joint return, your spouse. This is the population the SSN/ITIN tests apply to: 'you, and your spouse if filing jointly'."
  - key: "taxpayers"
    status: MATCH
    reason: "Counts the filer's own entries. This supports the roster consistency check and needs no IRS operand."
  - key: "spouses"
    status: MATCH
    reason: "Counts the spouse's entries. This supports the roster consistency check and needs no IRS operand."
  - key: "roster_ok"
    status: MATCH
    reason: "Requires one taxpayer entry, plus one spouse entry exactly when the status is married filing jointly, as joint-return reporting requires. The under-16 refusal is an owner-chosen entry check; it is disclosed as not drawn from the instructions and names what it excludes."
  - key: "roster_bad"
    status: MATCH
    reason: "This is the negation of roster_ok."
  - key: "hsa_people"
    status: MATCH
    reason: "Counts people with a Form 8889. The i8889 says 'If married filing jointly and both you and your spouse have HSAs, complete a separate Form 8889 for each of you.'"
  - key: "hsa_both"
    status: MATCH
    reason: "Both spouses have a Form 8889 when the count equals 2, which is the separate-HSAs case of line 6."
  - key: "hsa_split_count"
    status: MATCH
    reason: "Counts the Forms 8889 that use the line 6 rule for 'Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025'."
  - key: "hsa_agreed_count"
    status: MATCH
    reason: "Counts the line 6 forms that use the alternative 'unless you both agree on a different allocation'."
  - key: "hsa_step1_sum"
    status: MATCH
    reason: "Adds both spouses' Step 1 refigured limits. This supports checking that the Step 2 division between spouses is consistent."
  - key: "hsa_share_sum"
    status: MATCH
    reason: "Adds both spouses' allocated parts. Under line 6 Steps 2–3 these should total the Step 1 limit."
  - key: "work_ssn_count"
    status: MATCH
    reason: "Counts people whose SSN is 'valid for employment and issued before the due date of your return (including extensions)', the CTC definition of a valid SSN."
  - key: "any_work_ssn"
    status: MATCH
    reason: "Matches 'If you are filing a joint return, only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC.'"
  - key: "eic_ssn_count"
    status: MATCH
    reason: "Counts people with an SSN valid for the EIC, per Step 1 question 2: 'Do you, and your spouse if filing a joint return, have a social security number issued on or before the due date...'."
  - key: "all_eic_ssn"
    status: MATCH
    reason: "Step 1 question 2 requires both you and your spouse on a joint return to have such an SSN. Requiring the count to equal the number of people on the return does this."
  - key: "under16_count"
    status: MATCH
    reason: "Counts filers under age 16. It only feeds the owner-declared refusal gate, which is disclosed."
  - key: "filer_under16"
    status: MATCH
    reason: "This is the gate for the disclosed under-16 refusal: any person on the return under age 16."
  - key: "tin_count"
    status: MATCH
    reason: "Matches Step 5 question 1: 'have either an SSN or ITIN issued on or before the due date ... (Answer \"Yes\" if you are applying for an ITIN...)'."
  - key: "all_tin"
    status: MATCH
    reason: "The ODC requires 'you, and your spouse if filing jointly' to have an SSN/ITIN. Every person on the return must qualify, and this checks that."
  - key: "id_count"
    status: MATCH
    reason: "Counts people with either a work-valid SSN or an SSN/ITIN issued by the due date. These are the two acceptable identifications for the spouses under the CTC rule."
  - key: "ctc_ssn"
    status: MATCH
    reason: "Matches 'only one spouse is required to have a valid SSN... The other spouse must have either an SSN or ITIN... issued on or before the due date'. The applied-for ITIN is correctly not counted."
  - key: "taxpayer_work_ssn_count"
    status: MATCH
    reason: "Restricts the work-valid SSN count to the filer's own entry."
  - key: "taxpayer_work_ssn"
    status: MATCH
    reason: "This is the filer's own work-valid SSN, taken from the count above."
  - key: "home_cost"
    status: MATCH
    reason: "The included and excluded costs follow Pub. 501, Keeping Up a Home. The treatment of funds received in another person's name and of TANF payments follows the Worksheet 1 note."
  - key: "unmarried"
    status: MATCH
    reason: "The three 'considered unmarried' cases follow i1040gi Head of Household and Pub. 501 Considered Unmarried, including the temporary-absence rule for the spouse. The rule that a spouse who died in 2025 makes you married for the whole year follows Pub. 501 'Spouse died during the year'."
  - key: "married"
    status: MATCH
    reason: "Follows the Pub. 501 definition of marriage, common-law marriage, interlocutory decrees, final divorce, separate maintenance, annulment, the domestic partnership exclusion, and the divorce-and-remarriage rule."
  - key: "community_property"
    status: MATCH
    reason: "Lists the nine community property states named in i1040gi and Pub. 501."
  - key: "hoh_community_property"
    status: MATCH
    reason: "This is the gate for the Pub. 555/Form 8958 refusal. Pub. 501 warns that 'If you were considered married for part of the year and lived in a community property state ... special rules may apply.'"
  - key: "credit_disallowed"
    status: MATCH
    reason: "Combines the Form 8862 triggers (EIC after 1996, CTC/ACTC/ODC after 2015, reduced or disallowed other than math/clerical error) with the 2- and 10-year bans."
  - key: "ctc_disallowed_claim"
    status: MATCH
    reason: "A CTC/ODC is figured only if Schedule 8812 line 12 is 'Yes': 'Is the amount on line 8 more than the amount on line 11?'."
  - key: "eic_disallowed_claim"
    status: MATCH
    reason: "An EIC is claimed when Steps 1–5 are passed and the Worksheet line 6 credit is more than zero. It is combined with the prior-disallowance flag."
  - key: "test1_persons"
    status: MATCH
    reason: "Test 1 covers a dependent parent whose home was the main home 'for all of 2025'; 'Your parent didn't have to live with you'. A parent living with you is covered through Test 2 instead."
  - key: "test2_persons"
    status: MATCH
    reason: "Test 2 covers a qualifying person who lived with you more than half the year. The home-cost condition is tested separately, as the label states."
  - key: "test2_absence_persons"
    status: MATCH
    reason: "Counts persons who would qualify only by an absence that fails Pub. 501's rule: 'reasonable to assume the absent person will return ... continue to keep up the home'."
  - key: "hoh_absence"
    status: MATCH
    reason: "This is the gate for the temporary-absence refusal. It fires only when HOH eligibility turns solely on such a person."
  - key: "test1_met"
    status: MATCH
    reason: "Test 1 is met when at least one qualifying parent exists. Paying over half the cost of the parent's home is part of the per-parent test."
  - key: "test2_met"
    status: MATCH
    reason: "Matches 'You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived for more than half of the year'."
  - key: "hoh_eligible"
    status: MATCH
    reason: "Matches 'Check the \"Head of household\" box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies'. The refusals name the absence and community-property cases they exclude."
  - key: "hoh_fails"
    status: MATCH
    reason: "Flags a head of household status checked without the eligibility tests being met."
  - key: "qss_eligible"
    status: MATCH
    reason: "The five tests follow i1040gi and Pub. 501 Qualifying Surviving Spouse, including the exceptions for absences, birth/death and adoption. The kidnapped-child case is disclosed as outside the tool."
  - key: "qss_fails"
    status: MATCH
    reason: "Flags a qualifying surviving spouse status checked without all five tests being met."
  - key: "rdp"
    status: MATCH
    reason: "Matches i1040gi: 'Nevada, Washington, and California domestic partners'."
  - key: "spouse_died_2025"
    status: MATCH
    reason: "This is a simple fact input used for the filing status consistency checks."
  - key: "widowed_2025"
    status: MATCH
    reason: "Pub. 501: 'If your spouse died during the year, you are considered married for the whole year for filing status purposes'. Single or HOH with a 2025 death therefore conflicts."
  - key: "cp_married"
    status: MATCH
    reason: "Asks whether you were married for part of the year while living in a community property state, the condition in Pub. 501's community-property caution."
  - key: "cp_marriage_ended"
    status: MATCH
    reason: "Matches Pub. 501: 'If you were considered married for part of the year and lived in a community property state ... special rules may apply'."
  - key: "rdp_community_property"
    status: MATCH
    reason: "Matches i1040gi: 'A registered domestic partner in Nevada, Washington, or California must generally report half the combined community income'."
  - key: "filing_status_conflict"
    status: MATCH
    reason: "Single requires being unmarried on December 31. Married filing jointly requires being married at year end or a spouse who died in 2025, per i1040gi Single and Married Filing Jointly."
```
```
