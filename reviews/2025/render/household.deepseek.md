# Render comparison — household

The rendered English of every printed line of `Household facts for dependents and head of household` (`rendered/2025/household.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 17422f5dec7c2102012a5d0047e50131b253903349a5dc9f0d163bb74d1e6512 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | e89c8acf56b6ac52b1f4b39d5fe29e0394cfc792d6fdc49ad1a313ec2e57f213 |
| lines judged | 48 |
| match / mismatch / unclear / missing | 41 / 7 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 13, 14, 15, 17, 19, 23, 36, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 66, 93, 94, 95, 101, 104, 108, 110, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 13, 14, 15, 17, 19, 23, 36, 39, 40, 41, 42, 43, 44, 45, 66, 93, 95, 101, 104, 110, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
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
| p946 | For use in preparing 2025 returns | 17, 18, 19, 31, 32, 34, 37, 39, 41, 59, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 31, 32, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p560 | For use in preparing 2025 returns | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 39, 40 | cited pages | 38bbfa2efb2894e2527d66cd3478f33c6ceae4b777f78674c22bec16db9809aa | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 40 | 7ef279c8f34addc2ff13420e35fab4a092bf8027f53907c28a5f46d2c21da737 |
| p575 | None | 35 | pages named by another document's citation | 4d6ee3802a2906a4633dcfc104aa33bb3d9ddedebddc9eadbd0393cfdb61e07b | 35 | 3962801dde168fda9f4ee239245d9746b12e2d60bf358b25186ae4a57aa5b837 |
| p538 | None | 17 | pages named by another document's citation | 4186d7aaa8f711c9a524b87fac1e3df05640b6d66130093b2469480acb06ef6c | 17 | f500211df18a4aafd843e48bbad4b9102c598cf5ccc0fae96c7814a4bef0ae00 |

## Lines

### persons — Number of people on the return (you, and your spouse if filing jointly)
Status: **MATCH**

Model: Counts confirmed person entries; the label limits them to you and your spouse if filing jointly.

### taxpayers — Number of entries for you
Status: **MATCH**

Model: Counts entries identified as the taxpayer; consistent with one entry for you.

### spouses — Number of entries for your spouse
Status: **MATCH**

Model: Counts entries identified as the spouse; consistent with spouse only on a joint return.

### roster_ok — One entry for you, and one for your spouse exactly when filing jointly
Status: **MATCH**

Model: Implements one taxpayer entry and a spouse entry exactly for MFJ; the age-16 refusal is a named program-scope check.

### roster_bad — The people entered do not match the filing status
Status: **MATCH**

Model: Boolean complement of roster_ok.

### hsa_people — Number of people on the return with a Form 8889
Status: **MATCH**

Model: Form 8889 instructions require a separate Form 8889 for each spouse with an HSA.

### hsa_both — You and your spouse each have a Form 8889
Status: **MATCH**

Model: Two people with Form 8889 means both spouses have one on a joint roster.

### hsa_split_count — Number of Forms 8889 using the spouse rule of line 6
Status: **MATCH**

Model: Counts Forms 8889 where the line 6 spouse rule for separate HSAs with family coverage applies.

### hsa_agreed_count — Number of Forms 8889 using an agreed allocation
Status: **MATCH**

Model: Counts spouse-rule forms using an agreed allocation, as line 6 permits.

### hsa_step1_sum — Both spouses Step 1 limits added together
Status: **MISMATCH**

Restated: Add person.hsa_step1 over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS line 6 Step 2 says 'Divide the refigured contribution limit from Step 1 equally between you and your spouse' and Step 3 subtracts the spouse's part; no step adds both spouses' Step 1 limits together.

Ruling: interface gap; i8889 p. 7, Line 6, Step 1: "When refiguring line 5, use the same amount you previously entered on line 4". As the prior rulings: the line is unchanged by R4, which reworded only household.married, household.unmarried and household.qss_eligible; the sum is not line 6: it checks an agreed allocation (f8889.allocation_bad refuses when the spouses' Step 1 limits differ or their shares exceed one Step 1 limit; i8889 p. 7, Step 2), and line 4 (Archer MSA contributions) is zero on every computed return because f8889.unsupported refuses them, a Form 8889 screen outside the household render. Project stands.
Reviewed in: pass 43add74104ac

### hsa_share_sum — Both spouses parts of the Step 1 limit added together
Status: **MISMATCH**

Restated: Add person.hsa_share over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS line 6 Step 3 says 'Subtract the part of the contribution limit allocated to your spouse in Step 2 from the amount determined in Step 1'; line 6 is one spouse's share, not the sum of both spouses' shares.

Ruling: interface gap; i8889 p. 7, Line 6, Steps 1 to 3. As the prior rulings and hsa_step1_sum: the line is unchanged by R4; the sum of the shares is the check f8889.allocation_bad makes on an agreed allocation, not line 6, and is computed with line 4 zero (f8889.unsupported refuses Archer MSA contributions). Project stands.
Reviewed in: pass 43add74104ac

### work_ssn_count — Number of people on the return with an SSN valid for employment
Status: **MATCH**

Model: Counts persons whose answer to the valid-for-employment SSN question is yes.

### any_work_ssn — You, or your spouse if filing jointly, have an SSN valid for employment
Status: **MATCH**

Model: True when at least one person has a valid-for-employment SSN; matches the CTC joint-spouse rule.

### eic_ssn_count — Number of people on the return with an SSN valid for the EIC
Status: **MATCH**

Model: Counts persons with an SSN valid for EIC issued on or before the due date.

### all_eic_ssn — You, and your spouse if filing jointly, have SSNs valid for the EIC
Status: **MATCH**

Model: All filer/spouse entries have EIC-valid SSNs when the EIC SSN count equals persons.

### under16_count — Number of people on the return under age 16 at the end of 2025
Status: **MATCH**

Model: Counts person entries under age 16 at the end of 2025; no contrary IRS text is given.

### filer_under16 — You, or your spouse if filing jointly, were under age 16 at the end of 2025
Status: **MATCH**

Model: Boolean count for the program's age-16 entry check.

### tin_count — Number of people on the return with an SSN or ITIN, or who have applied for an ITIN
Status: **MATCH**

Model: Counts SSN/ITIN or timely ITIN application, matching the ODC filer TIN question.

### all_tin — You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
Status: **MATCH**

Model: All filer/spouse entries have SSN/ITIN or timely ITIN application.

### id_count — Number of people on the return with an SSN valid for employment or an SSN or ITIN
Status: **MATCH**

Model: Counts person entries with work-valid SSN or SSN/ITIN, as used in the CTC identification helper.

### ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid
Status: **MISMATCH**

Restated: helper "You, or your spouse if filing jointly, have an SSN valid for employment" = true and helper "Number of people on the return with an SSN valid for employment or an SSN or ITIN" = helper "Number of people on the return (you, and your spouse if filing jointly)"

Model: The IRS says 'To claim the child tax credit, you must have a valid SSN, which means it must be valid for employment' and 'If your qualifying child didn’t have an SSN valid for employment... you can’t claim the child tax credit for that child'; the restatement allows SSN or ITIN for each other person and does not check the qualifying children.

Ruling: model error; i1040gi p. 7, "If you are filing a joint return, only one spouse is required to have a valid SSN in order to be eligible for the CTC and ACTC. The other spouse must have either an SSN or ITIN" (amb.2025.ctc_spouse_itin_application). The helper is the filer-side test; the qualifying child's SSN valid for employment is tested per child in dependent.ctc_child, which the reviewer reads as missing here. Project stands.

### taxpayer_work_ssn_count — Your entry, if the answer is yes
Status: **MATCH**

Model: Counts the taxpayer entry when the work-valid SSN answer is yes.

### taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: Boolean from the taxpayer-only work-valid SSN count.

### home_cost — Did you pay over half the cost of keeping up your home for 2025?
Status: **MISMATCH**

Restated: Input — Did you pay over half the cost of keeping up your home for 2025? Cost of keeping up a home includes expenses such as rent, mortgage interest, real estate taxes, insurance on the home, repairs, utilities, and food eaten in the home. It does not include the cost of clothing, education, medical treatment, vacations, life insurance, or transportation, or the value of your services or those of a member of your household. Amounts paid out of funds received in the name of a person who lives in the home, such as their Social Security, count as paid by that person, not you. TANF or similar payments you received and used for the home count as paid by you.

Model: The IRS note says TANF used 'to support another person' is considered support you provided for that person, and amounts in a child's or qualifying person's name are considered paid by the child; the restatement instead treats TANF used for the home as paid by you and refers to any person living in the home.

Ruling: model error; p501 p. 9, Keeping Up a Home, Note: "if you received Temporary Assistance to Needy Families (TANF) payments or other similar payments and used the payment to support another person, those payments are considered support you provided ... Amounts paid out of funds received in the child's or qualifying person's name, such as Social Security, are considered paid by the child, not you. If the total amount you paid is more than the amount others paid, you meet the requirement". The note sits in the cost-of-keeping-up-a-home test, so TANF used for the home counts as paid by you, as the question says (BUG-0258); funds in any other household member's name are paid by that member, not by you, so "a person who lives in the home" changes no answer to "over half". Project stands.

### unmarried — Were you unmarried, or considered unmarried under the head of household rules, at the end
Status: **MATCH**

Model: The restatement tracks the head of household considered-unmarried rules in the Form 1040 instructions and Pub. 501, including legal separation, living apart, nonresident alien spouse, and temporary absences.
Reviewed in: pass 43add74104ac

### married — Were you married at the end of 2025?
Status: **MATCH**

Model: The restatement matches Pub. 501 marital status rules: state or territory recognition, common law marriage, final divorce, legal separation, annulment, interlocutory decrees, and domestic partnerships not being marriages.
Reviewed in: pass 43add74104ac

### community_property — Did you live in a community property state at any time in 2025?
Status: **MATCH**

Model: Lists exactly the community property states in the IRS text.

### hoh_community_property — Married, filing as head of household, and living in a community property state
Status: **MATCH**

Model: Pub. 501 says special community-property rules may apply if you were considered married for part of the year and lived in a community property state; the helper captures a married HOH filer in such a state.
Reviewed in: pass 43add74104ac

### credit_disallowed — Was your EIC for a year after 1996, or your child tax credit, additional child tax credit
Status: **MATCH**

Model: Restates the EIC/CTC/ODC prior-disallowance and 2/10-year period questions.

### ctc_disallowed_claim — An earlier credit was reduced or disallowed (or a disallowance period applies) and Schedul
Status: **MATCH**

Model: Uses the Schedule 8812 line 12 condition: line 8 more than line 11 after the prior-disallowance answer.

### eic_disallowed_claim — An earlier credit was reduced or disallowed (or a disallowance period applies) and Steps 1
Status: **MATCH**

Model: The Form 8862 who-must-file rules use an earlier EIC reduction or disallowance other than math or clerical error, or a 2- or 10-year period, plus a current credit; the helper matches that condition with a positive Worksheet A line 6.
Reviewed in: pass 43add74104ac

### test1_persons — Number of parents who qualify you under Test 1
Status: **MATCH**

Model: Counts Test 1 parent cases; IRS Test 1 is the parent test where the parent need not live with you.

### test2_persons — Number of persons who qualify you under Test 2
Status: **MISMATCH**

Restated: Add dependent.one over every confirmed dependent entry for which helper "A Test 2 person who lived with you more than half the year, or of the part of the year a relative was alive, counting only absences head of household counts (the home-cost condition of Test 2 is tested on the household form)" = true, within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS Test 2 includes 'Your unmarried qualifying child who isn’t your dependent,' a married qualifying child who isn’t your dependent, and certain divorced/separated-parent children; counting only dependent entries misses those non-dependent Test 2 persons.

Ruling: representation; i1040gi p. 14, Test 2, items 2 to 4 (qualifying children who are not your dependent). The dependent collection holds every person evaluated for Test 2, and dependent.hoh_test2 counts a qualifying child not claimed as a dependent (its derivation reads dependent.qualifying_child beside dependent.claimed), so the non-dependent Test 2 persons the reviewer names are counted. Project stands.

### test2_absence_persons — Number of persons who would qualify you under Test 2 only by counting an absence head of h
Status: **MISMATCH**

Restated: Add dependent.one over every confirmed dependent entry for which helper "A Test 2 person only by counting an absence head of household does not count" = true, within the current person when parent-bound. An unanswered roster is unknown.

Model: The same omission exists for non-dependent Test 2 persons: the IRS Test 2 can turn on a qualifying child who isn’t your dependent, but the restatement counts only dependent entries.

Ruling: representation; i1040gi p. 14, Test 2; p501 p. 9 (BUG-0267). As test2_persons and the prior ruling: dependent.hoh_absence does not require dependent.claimed where Test 2 allows an unclaimed qualifying child. Project stands.

### hoh_absence — Head of household turns on a person who lived with you more than half the year only by cou
Status: **MATCH**

Model: Pub. 501 temporary absences count as time lived in the home only if it was reasonable to assume the absent person would return and the home was kept up; the helper flags HOH qualification depending on an absence HOH does not count.
Reviewed in: pass 43add74104ac

### test1_met — Test 1 met
Status: **MATCH**

Model: True when any Test 1 parent qualifies.

### test2_met — Test 2 met, having paid over half the cost of keeping up your own home
Status: **MATCH**

Model: True when the home-cost test is met and any Test 2 person qualifies.

### hoh_eligible — Unmarried or considered unmarried, and Test 1 or Test 2 applies
Status: **MATCH**

Model: The Form 1040 HOH instructions say check HOH only if unmarried or considered unmarried and either Test 1 or Test 2 applies; the refusal gates name the excluded temporary-absence and community-property cases.
Reviewed in: pass 43add74104ac

### hoh_fails — Head of household checked without meeting its tests
Status: **MATCH**

Model: Complement of HOH eligibility for a return checked as HOH.

### qss_eligible — Do all five qualifying surviving spouse tests apply to you?
Status: **MATCH**

Model: The five tests match the qualifying surviving spouse rules in Pub. 501 and the Form 1040 instructions; the kidnapped-child exception is expressly noted as outside the tool.
Reviewed in: pass 43add74104ac

### qss_fails — Qualifying surviving spouse checked without meeting its tests
Status: **MATCH**

Model: Pub. 501 and the Form 1040 instructions allow QSS only if all five tests apply, so checking QSS when qss_eligible is false is a conflict.
Reviewed in: pass 43add74104ac

### rdp — Were you a registered domestic partner in Nevada, Washington or California at any time in
Status: **MATCH**

Model: Matches the registered-domestic-partner question for Nevada, Washington, and California.

### spouse_died_2025 — Did your spouse die in 2025?
Status: **MATCH**

Model: Fact question used to apply the spouse-died-in-2025 filing-status rules.

### widowed_2025 — Filing as single or head of household although your spouse died in 2025
Status: **MATCH**

Model: Flags single/HOH status when the spouse died in 2025, contrary to the considered-married rule.

### cp_married — Married at any time in 2025 while living in a community property state, though not married
Status: **MATCH**

Model: Matches the part-year community-property marriage question.

### cp_marriage_ended — Not filing jointly, and married for part of 2025 while living in a community property stat
Status: **MATCH**

Model: Pub. 501 says special community-property rules may apply when you were considered married for part of the year and lived in a community property state; the helper captures not-MFJ, CP, not married at year end, but married during 2025.
Reviewed in: pass 43add74104ac

### rdp_community_property — Not filing jointly, living in a community property state, and a registered domestic partne
Status: **MATCH**

Model: Matches the RDP community-property rule for NV, WA, and CA.

### filing_status_conflict — The filing status conflicts with the marriage facts entered
Status: **MISMATCH**

Restated: (f1040 line Filing Status = 'single' and helper "Were you married at the end of 2025?" = true or f1040 line Filing Status = 'mfj' and helper "Were you married at the end of 2025?" = false and helper "Did your spouse die in 2025?" = false)

Model: The helper omits a married-filing-separately return when the filer was not married at year end, although the IRS says 'Check the Married filing separately box ... if you are married at the end of 2025'; it also does not flag single when the spouse died in 2025, whom the IRS treats as married for the whole year.

Ruling: scope; i1040gi p. 14, Married Filing Separately; p501 p. 6, Spouse died during the year. As the prior ruling: a separate return is refused for the whole return by s3.mfs on scope.ready, so the married-filing-separately case never reaches line 12e; a single return in the year of a spouse's death is refused by household.widowed_2025. The gate covers the single and joint contradictions (BUG-0286). The R4 rewording of household.married (paragraphs, no word lost) changed no condition. Project stands.
Reviewed in: pass 43add74104ac

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| persons | 9d27206b964b69630b3746b27911e13be4cf759946a8d56ff5673f93680ae538 |
| taxpayers | 782df83519f374a0a0ae75c282568871ace0949664b2c443bb933b9b69341d78 |
| spouses | 796bc0e83786b1de3d3b9abc5a0d79fe8bc2648b31914ab8113f2f3d34db1556 |
| roster_ok | 96e5a1665099a37f97bad0caff16d27e6c64aa1127f01feb9aec0368ac4fc30e |
| roster_bad | 2ed3edf7ee500562d6142caf694eb41c72a6cdfe1226ec4a78fca57e4b8f453d |
| hsa_people | b712295f60780bb4df59fbe5983088cc1b27b031df2a712b045322c2222f71fd |
| hsa_both | 5643d209813ddc56e96f1c0472f68ae949bcd0394600aaa6e8ebeeafc65e7309 |
| hsa_split_count | 3650b4b4a5e850662cd14bacdd8455fcd39fc3200f4799f02194eaa975e17ed8 |
| hsa_agreed_count | 441f9eca79300f70379e218b893f92e2029c444a4d07020be12c94cadf8dc0ec |
| hsa_step1_sum | 0a7b2ca32202e8d6bf7f5398eb5afc6aecf9505237540b92b329efa800077a04 |
| hsa_share_sum | 9c9a4e884a80abaac2071c736643ab280c84858829dca3ca13064fa13d715501 |
| work_ssn_count | efdfc01b4332a0ffb4659f0de610718d633f11889eb5aa52bdb47482a52102fe |
| any_work_ssn | 8cf5c050a092dedf06e47acf5700fc9d4570bc0bf751538a98207bfe6dff1288 |
| eic_ssn_count | 9e4db7de07306c30eea28273af6049c0e51d09f93fe3c09705d4308faf50400d |
| all_eic_ssn | 79c4eddec538dbb09af42480cc9c2c4854201db7d404d531a70003d119fb37cf |
| under16_count | 8f3f202d279edafc323c441449a347616b3a1eb5907cf6c0ade3a6ec939bae8c |
| filer_under16 | 5d4f9632063f50fb7e49376eaf5700fa9ce247d27019c394986546ab1ad0d41a |
| tin_count | 4368f99f1c0c575c26aa7799c96a05e47b810d98891fdb81c6448247682faa93 |
| all_tin | af34290d4377e65f616a5cac6cc32191c9d9f7734f084b273a907c6a5e22e6e2 |
| id_count | 01d48500a4c174fa9fc94bb598d34112c719e6f0f0ed94d7a475f61772dcf845 |
| ctc_ssn | 6db1ea6e6bf0997fe35cdba42f550f7d8f5364c0c879a3e4840dc16cb2735d06 |
| taxpayer_work_ssn_count | 5068464ee7473e72ce4ced8b1fd28f82d248aced4e6d7af55067d91f3a3c274b |
| taxpayer_work_ssn | 5068464ee7473e72ce4ced8b1fd28f82d248aced4e6d7af55067d91f3a3c274b |
| home_cost | eb66faee704155180e7a0405c09ffc7b275a7f6d24d4dbc5728c431b67db38e8 |
| unmarried | b687b58de22b6968b0b213dbadc07b6306c306109730ab10780b098737071212 |
| married | 2d20e6ac24216b13d34a9e8a4c579dc854b0e47935eed788dabcf90dd9b86fd7 |
| community_property | b9aff9b390e2a39a45d6d12d52893607f842b1ed5bef3be8d1561f5b1cd099b3 |
| hoh_community_property | e2566e71d47655f6c2406035873f820859bb85fa8082259b0a7545c8f60b3e8f |
| credit_disallowed | 8485b83c733a6701e3e9a3c627d4eba39fe966958915d4b8c4ab8b8ceab69f17 |
| ctc_disallowed_claim | 1e81abeb3d880d4d1476c80abf1e06e003d69d3efadf284ff11a2d256c4ce8f6 |
| eic_disallowed_claim | 60a97eba03f3522969bf1ef925e40868de1eeaf8977ab508b4fc9182af988223 |
| test1_persons | 61eba99c99a2954329aae0987e04656665117574a385f2411b3d8a05bbd064b6 |
| test2_persons | 1d35fdd798dd9a81ca48f308819882a59628f8aa6ff5b53f9d8cc9ca342486f5 |
| test2_absence_persons | e3a1d693ed3c732ef3d443dfe9d56839b0bd3174ead47afc92e93275b833d8ea |
| hoh_absence | 9b7aeeec84fb23ac45cddf97cfd71262e74a9beddb97dc2048b54107a24d8e42 |
| test1_met | 5ef108d86b78c027a5b671c9e0d775022de60ef74103e4b9252697f9f76ffe1f |
| test2_met | b114dc2c4be9cb5368c0bafcbcfd3693bc2b537358a6b82c83449829c9a00bf4 |
| hoh_eligible | fe6fd3d53dd4956541b1301a6451b709315b8d019168a6d1e37eff4c2f5f1a9f |
| hoh_fails | f132fdaebf093a6209c082ec2ba21290e1fe55ab3e12b7d1bba194b5b3aced6f |
| qss_eligible | a60fbc2d99325bfe450cb0a60b674633604e0387ca4b5c31aa53252d60ec8690 |
| qss_fails | 876bc8582890356064ee02a68759c1f5e14ac51780b4b94dc1a51c90085770cb |
| rdp | f5b3282a090b3ea7717369f71c18e431a3f483e60e79e3e3374419283293fa99 |
| spouse_died_2025 | ed9ee674679bf195b762d0b7b440d47d762a3626fa0957a0c2c93ec9749bc17d |
| widowed_2025 | 9315d0120ebcd1cdf1759865fa10bc9526596b0a4b7ab5f4599bed28130849ef |
| cp_married | 9e9b1b5b0c0497e24d3359e9174343c28509afffa37acc7bd8837ee487b0e113 |
| cp_marriage_ended | 1f38f9d3857c80f7634fbda0dfc9d272a23b86d3ee2e7e7ca9b2314c6ee406d8 |
| rdp_community_property | a457c28da276619b0ca48859c82d583a1101e0dffaa3a325cee46978d24be5b9 |
| filing_status_conflict | 7aafae4e2b5bd4d0b53dd7dd2201fe48163cab9a7783da40f948b7452afb2c90 |
| (rest of the document) | cb5c9ecba569eb410b0a79967c0b3d9cd7c9c97721476ca24d67e84169c728d8 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 43add74104ac

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines hsa_step1_sum, hsa_share_sum, unmarried, married, hoh_community_property, eic_disallowed_claim, hoh_absence, hoh_eligible, qss_eligible, qss_fails, cp_marriage_ended, filing_status_conflict |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 43add74104ac70f75e182f8a53913020ba47d143a4ab3c422ed51d224c25579c |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 40398c41a62ad93cedca7505d139c57c6bbaeb58f277b14d8b7e78bc6c5f41b2 |
| receipt | .transcription/household.deepseek.render.lines-c756fe33737c |
| lines judged | 12 |
| match / mismatch / unclear / missing | 9 / 3 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8889 | 2025 | 2, 4, 5, 6, 7 | cited pages | bfbdc8bbe0b85d088325243f176d4c8261b0ca2428f75f4f41e4a339ecb5495c | 2, 4, 5, 7 | 533a42f870f12dc6c1984815eae1a4bf59d6fde28cbc909d9a4e76ff41c6eda7 |
| i1040gi | 2025; printed date 2026-02-25 | 13, 14, 15, 23, 36, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 93, 94, 95, 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 13, 14, 15, 23, 36, 39, 40, 41, 42, 43, 44, 45, 93, 95, 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p501 | 2025 returns; PDF created 2026-02-04 | 6, 8, 9, 11 | cited pages | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 6, 8, 11 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |
| f8889 | 2025; created 2025-03-28 | 1 | whole document | f1ae3589453f3dd1d5277a79409bd7d0bf4772715fa8bd11d58126e6f387c0cf | - | 85ba6183eb2c35cf7b6d63eb6fd515be7234f5f938da39d7d000a6a7f2359d4e |
| f1040sa | 2025; created 2025-11-20 | 1 | whole document | 225b3ec4aa83600179f177807a26d8976343af5c2664b8eb6614fb6abcf8fadd | - | bfe55c01a948d1f96bacf363a8b5cbb1bf7273cbc8672598f1a66c31504a59fe |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |
| i1040sc | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| i1040s8812 | 2025; printed date 2026-01-23 | 2, 8 | cited pages | fd50a5266cc20aa5a31de0535658793f75c7abbb12fd83b65dc5b21c6ede2765 | 2 | e6ba91f54df679c9c19c23169c369f14bff012ba2fe110c3973bde59676c1d45 |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| iw2w3 | 2025; printed date 2025-02-19 | 18 | cited pages | 27ad850a44d58d9186afcccb33b8a32f4747911e2b1b3138de515f44d4de33f3 | 18 | 3876738db222e8abe6103f29d8a8654a3139b9896f97e325d50e80b87ed5b26a |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 31, 32, 33, 34, 37, 39, 41, 59, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 31, 32, 33, 34, 37, 39, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p560 | For use in preparing 2025 returns | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 39, 40 | cited pages | 38bbfa2efb2894e2527d66cd3478f33c6ceae4b777f78674c22bec16db9809aa | 7, 8, 9, 10, 11, 14, 15, 16, 17, 38, 40 | 7ef279c8f34addc2ff13420e35fab4a092bf8027f53907c28a5f46d2c21da737 |
| p575 | None | 35 | pages named by another document's citation | 4d6ee3802a2906a4633dcfc104aa33bb3d9ddedebddc9eadbd0393cfdb61e07b | 35 | 3962801dde168fda9f4ee239245d9746b12e2d60bf358b25186ae4a57aa5b837 |
| i8606 | 2025 | 9 | pages named by another document's citation | 242e712835ef634f3af8f1d0f19435b236e9c54b80921d6017c153b3e6c2aec6 | 9 | 805e59f2458d33a3fc0a1d17ebede2ecd59e18d911069bbe84987e53e297ec79 |
| i8960 | 2025; printed date 2026-02-04 | 22 | pages named by another document's citation | fcae098ebc1ad79343de101a66765d3b3597f664dc744de3a7588be123c900a1 | - | d6dc1f475c511790abb02d6d6cfff554a59b40c0da1c56eb2f26af4e3cb7fa51 |
| p463 | For use in preparing 2025 returns | 25, 26 | pages named by another document's citation | 153efad2a94bcccadf643b0f28f913d74b7d70b727f73eca540a2ce4d32bbfda | 25, 26 | a0b14576fdb49a7ba3e7a90092c1b8f6b8ba33889c8c35da5629156346581326 |
| p538 | None | 17 | pages named by another document's citation | 4186d7aaa8f711c9a524b87fac1e3df05640b6d66130093b2469480acb06ef6c | 17 | f500211df18a4aafd843e48bbad4b9102c598cf5ccc0fae96c7814a4bef0ae00 |

##### Raw response

```yaml
lines:
  - key: "hsa_step1_sum"
    status: MISMATCH
    reason: "IRS line 6 Step 2 says 'Divide the refigured contribution limit from Step 1 equally between you and your spouse' and Step 3 subtracts the spouse's part; no step adds both spouses' Step 1 limits together."
  - key: "hsa_share_sum"
    status: MISMATCH
    reason: "IRS line 6 Step 3 says 'Subtract the part of the contribution limit allocated to your spouse in Step 2 from the amount determined in Step 1'; line 6 is one spouse's share, not the sum of both spouses' shares."
  - key: "unmarried"
    status: MATCH
    reason: "The restatement tracks the head of household considered-unmarried rules in the Form 1040 instructions and Pub. 501, including legal separation, living apart, nonresident alien spouse, and temporary absences."
  - key: "married"
    status: MATCH
    reason: "The restatement matches Pub. 501 marital status rules: state or territory recognition, common law marriage, final divorce, legal separation, annulment, interlocutory decrees, and domestic partnerships not being marriages."
  - key: "hoh_community_property"
    status: MATCH
    reason: "Pub. 501 says special community-property rules may apply if you were considered married for part of the year and lived in a community property state; the helper captures a married HOH filer in such a state."
  - key: "eic_disallowed_claim"
    status: MATCH
    reason: "The Form 8862 who-must-file rules use an earlier EIC reduction or disallowance other than math or clerical error, or a 2- or 10-year period, plus a current credit; the helper matches that condition with a positive Worksheet A line 6."
  - key: "hoh_absence"
    status: MATCH
    reason: "Pub. 501 temporary absences count as time lived in the home only if it was reasonable to assume the absent person would return and the home was kept up; the helper flags HOH qualification depending on an absence HOH does not count."
  - key: "hoh_eligible"
    status: MATCH
    reason: "The Form 1040 HOH instructions say check HOH only if unmarried or considered unmarried and either Test 1 or Test 2 applies; the refusal gates name the excluded temporary-absence and community-property cases."
  - key: "qss_eligible"
    status: MATCH
    reason: "The five tests match the qualifying surviving spouse rules in Pub. 501 and the Form 1040 instructions; the kidnapped-child exception is expressly noted as outside the tool."
  - key: "qss_fails"
    status: MATCH
    reason: "Pub. 501 and the Form 1040 instructions allow QSS only if all five tests apply, so checking QSS when qss_eligible is false is a conflict."
  - key: "cp_marriage_ended"
    status: MATCH
    reason: "Pub. 501 says special community-property rules may apply when you were considered married for part of the year and lived in a community property state; the helper captures not-MFJ, CP, not married at year end, but married during 2025."
  - key: "filing_status_conflict"
    status: MISMATCH
    reason: "The helper omits a married-filing-separately return when the filer was not married at year end, although the IRS says 'Check the Married filing separately box ... if you are married at the end of 2025'; it also does not flag single when the spouse died in 2025, whom the IRS treats as married for the whole year."
```

## Raw response

```yaml
lines:
  - key: "persons"
    status: MATCH
    reason: "Counts confirmed person entries; the label limits them to you and your spouse if filing jointly."
  - key: "taxpayers"
    status: MATCH
    reason: "Counts entries identified as the taxpayer; consistent with one entry for you."
  - key: "spouses"
    status: MATCH
    reason: "Counts entries identified as the spouse; consistent with spouse only on a joint return."
  - key: "roster_ok"
    status: MATCH
    reason: "Implements one taxpayer entry and a spouse entry exactly for MFJ; the age-16 refusal is a named program-scope check."
  - key: "roster_bad"
    status: MATCH
    reason: "Boolean complement of roster_ok."
  - key: "hsa_people"
    status: MATCH
    reason: "Form 8889 instructions require a separate Form 8889 for each spouse with an HSA."
  - key: "hsa_both"
    status: MATCH
    reason: "Two people with Form 8889 means both spouses have one on a joint roster."
  - key: "hsa_split_count"
    status: MATCH
    reason: "Counts Forms 8889 where the line 6 spouse rule for separate HSAs with family coverage applies."
  - key: "hsa_agreed_count"
    status: MATCH
    reason: "Counts spouse-rule forms using an agreed allocation, as line 6 permits."
  - key: "hsa_step1_sum"
    status: MATCH
    reason: "Sums the per-spouse Step 1 refigured line 5 amounts under the line 6 spouse rule."
  - key: "hsa_share_sum"
    status: MATCH
    reason: "Sums the per-spouse allocated parts of the Step 1 limit under line 6."
  - key: "work_ssn_count"
    status: MATCH
    reason: "Counts persons whose answer to the valid-for-employment SSN question is yes."
  - key: "any_work_ssn"
    status: MATCH
    reason: "True when at least one person has a valid-for-employment SSN; matches the CTC joint-spouse rule."
  - key: "eic_ssn_count"
    status: MATCH
    reason: "Counts persons with an SSN valid for EIC issued on or before the due date."
  - key: "all_eic_ssn"
    status: MATCH
    reason: "All filer/spouse entries have EIC-valid SSNs when the EIC SSN count equals persons."
  - key: "under16_count"
    status: MATCH
    reason: "Counts person entries under age 16 at the end of 2025; no contrary IRS text is given."
  - key: "filer_under16"
    status: MATCH
    reason: "Boolean count for the program's age-16 entry check."
  - key: "tin_count"
    status: MATCH
    reason: "Counts SSN/ITIN or timely ITIN application, matching the ODC filer TIN question."
  - key: "all_tin"
    status: MATCH
    reason: "All filer/spouse entries have SSN/ITIN or timely ITIN application."
  - key: "id_count"
    status: MATCH
    reason: "Counts person entries with work-valid SSN or SSN/ITIN, as used in the CTC identification helper."
  - key: "ctc_ssn"
    status: MISMATCH
    reason: "The IRS says 'To claim the child tax credit, you must have a valid SSN, which means it must be valid for employment' and 'If your qualifying child didn’t have an SSN valid for employment... you can’t claim the child tax credit for that child'; the restatement allows SSN or ITIN for each other person and does not check the qualifying children."
  - key: "taxpayer_work_ssn_count"
    status: MATCH
    reason: "Counts the taxpayer entry when the work-valid SSN answer is yes."
  - key: "taxpayer_work_ssn"
    status: MATCH
    reason: "Boolean from the taxpayer-only work-valid SSN count."
  - key: "home_cost"
    status: MISMATCH
    reason: "The IRS note says TANF used 'to support another person' is considered support you provided for that person, and amounts in a child's or qualifying person's name are considered paid by the child; the restatement instead treats TANF used for the home as paid by you and refers to any person living in the home."
  - key: "unmarried"
    status: MATCH
    reason: "Restates the HOH considered-unmarried rules, including the spouse-died-in-2025 rule."
  - key: "married"
    status: MATCH
    reason: "Restates the marital-status rules from Pub. 501 and the Form 1040 instructions."
  - key: "community_property"
    status: MATCH
    reason: "Lists exactly the community property states in the IRS text."
  - key: "hoh_community_property"
    status: MISMATCH
    reason: "The IRS says 'If you were considered married for part of the year and lived in a community property state... special rules may apply'; this helper requires married at the end of 2025, missing part-year married HOH filers."
  - key: "credit_disallowed"
    status: MATCH
    reason: "Restates the EIC/CTC/ODC prior-disallowance and 2/10-year period questions."
  - key: "ctc_disallowed_claim"
    status: MATCH
    reason: "Uses the Schedule 8812 line 12 condition: line 8 more than line 11 after the prior-disallowance answer."
  - key: "eic_disallowed_claim"
    status: MATCH
    reason: "Requires prior disallowance, EIC Steps 1-5 passed, and Worksheet A line 6 above zero."
  - key: "test1_persons"
    status: MATCH
    reason: "Counts Test 1 parent cases; IRS Test 1 is the parent test where the parent need not live with you."
  - key: "test2_persons"
    status: MISMATCH
    reason: "IRS Test 2 includes 'Your unmarried qualifying child who isn’t your dependent,' a married qualifying child who isn’t your dependent, and certain divorced/separated-parent children; counting only dependent entries misses those non-dependent Test 2 persons."
  - key: "test2_absence_persons"
    status: MISMATCH
    reason: "The same omission exists for non-dependent Test 2 persons: the IRS Test 2 can turn on a qualifying child who isn’t your dependent, but the restatement counts only dependent entries."
  - key: "hoh_absence"
    status: MATCH
    reason: "Identifies the noncounted-absence case when Test 1 is not met and no counted Test 2 person exists."
  - key: "test1_met"
    status: MATCH
    reason: "True when any Test 1 parent qualifies."
  - key: "test2_met"
    status: MATCH
    reason: "True when the home-cost test is met and any Test 2 person qualifies."
  - key: "hoh_eligible"
    status: MATCH
    reason: "Unmarried/considered unmarried plus Test 1 or Test 2 matches the HOH requirements."
  - key: "hoh_fails"
    status: MATCH
    reason: "Complement of HOH eligibility for a return checked as HOH."
  - key: "qss_eligible"
    status: MISMATCH
    reason: "It tells the filer to answer No if the child was presumed kidnapped, but Pub. 501 says 'You may be eligible to file as a qualifying surviving spouse even if the child... has been kidnapped'; it also repeats the TANF home-cost statement."
  - key: "qss_fails"
    status: MATCH
    reason: "Complement of QSS eligibility for a return checked as QSS."
  - key: "rdp"
    status: MATCH
    reason: "Matches the registered-domestic-partner question for Nevada, Washington, and California."
  - key: "spouse_died_2025"
    status: MATCH
    reason: "Fact question used to apply the spouse-died-in-2025 filing-status rules."
  - key: "widowed_2025"
    status: MATCH
    reason: "Flags single/HOH status when the spouse died in 2025, contrary to the considered-married rule."
  - key: "cp_married"
    status: MATCH
    reason: "Matches the part-year community-property marriage question."
  - key: "cp_marriage_ended"
    status: MATCH
    reason: "Combines non-MFJ, community property, not married at end, and part-year CP marriage."
  - key: "rdp_community_property"
    status: MATCH
    reason: "Matches the RDP community-property rule for NV, WA, and CA."
  - key: "filing_status_conflict"
    status: MISMATCH
    reason: "It omits MFS: the IRS says 'Check the “Married filing separately” box... if you are married at the end of 2025 and file a separate return,' so MFS with married false and no 2025 spouse death is also a conflict."
```
