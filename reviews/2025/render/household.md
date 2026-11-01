# Render comparison — household

The rendered English of every printed line of `Household facts for dependents and head of household` (`rendered/2025/household.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-11-01 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | df6151787808a2ac957687d9d27bf9909149bbc896bdbecb8ea19e94f09252d8 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | d84684dc95dd51253995ab05880f95d98a4e73a17ec5923e876209598d9fdefc |
| lines judged | 46 |
| match / mismatch / unclear / missing | 44 / 2 / 0 / 0 |
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

Model: Counts one entry per person on the return, which fits the text's treatment of you, and your spouse if filing jointly, as the people tested.

### taxpayers — Number of entries for you
Status: **MATCH**

Model: This is a plain count of the entries marked as yours, and nothing in the text conflicts with it.

### spouses — Number of entries for your spouse
Status: **MATCH**

Model: This is a plain count of the entries marked as your spouse's, and nothing in the text conflicts with it.

### roster_ok — One entry for you, and one for your spouse exactly when filing jointly
Status: **MATCH**

Model: It requires a spouse entry only on a joint return, consistent with the text's 'you, and your spouse if filing jointly'. The under-16 refusal names its exclusion and correctly says it is an owner decision; the text mentions under-16 filers only for the Self-Select PIN.

### roster_bad — The people entered do not match the filing status
Status: **MATCH**

Model: This is the direct negation of roster_ok, as the label says.

### hsa_people — Number of people on the return with a Form 8889
Status: **MATCH**

Model: Counts people with at least one Form 8889, consistent with 'complete a separate Form 8889 for each' spouse with an HSA.

### hsa_both — You and your spouse each have a Form 8889
Status: **MATCH**

Model: A count of two people with Forms 8889 means each spouse has one, as the label says.

### hsa_split_count — Number of Forms 8889 using the spouse rule of line 6
Status: **MATCH**

Model: Counts Forms 8889 for spouses with separate HSAs and family coverage at any time during 2025, the condition in the line 6 instructions.

### hsa_agreed_count — Number of Forms 8889 using an agreed allocation
Status: **MATCH**

Model: Counts Forms 8889 under the line 6 rule that use the option 'unless you both agree on a different allocation'.

### hsa_step1_sum — Both spouses Step 1 limits added together
Status: **MATCH**

Model: Adds the refigured line 5 limits, which follow Step 1 (family-coverage months only, 'use the same amount you previously entered on line 4'). The glossary fixes line 4 at $0, and any f8889 refusal for Archer MSA filers is not shown here, so this judgment assumes such filers are excluded.

### hsa_share_sum — Both spouses parts of the Step 1 limit added together
Status: **MATCH**

Model: Adds each spouse's part, taken as half or as the agreed amount, which agrees with line 6 Steps 2 and 3.

### work_ssn_count — Number of people on the return with an SSN valid for employment
Status: **MATCH**

Model: Counts people with an SSN valid for employment, the text's definition of a valid SSN. The question omits '(including extensions)' after the due date, which is treated as wording.

### any_work_ssn — You, or your spouse if filing jointly, have an SSN valid for employment
Status: **MATCH**

Model: Requires at least one such person, matching 'only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC'.

### eic_ssn_count — Number of people on the return with an SSN valid for the EIC
Status: **MATCH**

Model: Counts people with an SSN valid for the EIC and issued on or before the due date, as in EIC Step 1, question 2.

### all_eic_ssn — You, and your spouse if filing jointly, have SSNs valid for the EIC
Status: **MATCH**

Model: Requires every person on the return to qualify, matching 'Do you, and your spouse if filing a joint return, have a social security number' valid for EIC purposes.

### under16_count — Number of people on the return under age 16 at the end of 2025
Status: **MATCH**

Model: This is a plain count supporting the owner's under-16 entry check, and it computes what its label says.

### filer_under16 — You, or your spouse if filing jointly, were under age 16 at the end of 2025
Status: **MATCH**

Model: True when any person on the return was under 16 at the end of 2025, as the label says.

### tin_count — Number of people on the return with an SSN or ITIN, or who have applied for an ITIN
Status: **MATCH**

Model: Counts an SSN or ITIN, or an application for an ITIN, matching Step 5, question 1: 'Answer Yes if you are applying for an ITIN on or before the return due date'.

### all_tin — You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
Status: **MATCH**

Model: Requires every person to qualify, matching 'you, and your spouse if filing jointly, must have either an SSN or ITIN'.

### id_count — Number of people on the return with an SSN valid for employment or an SSN or ITIN
Status: **MATCH**

Model: Counts people with either a work-valid SSN or an issued SSN or ITIN, the two identification types in the CTC rule, and it computes what its label says.

### ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid
Status: **MATCH**

Model: Requires one work-valid SSN and identification for everyone, matching 'only one spouse is required to have a valid SSN' and 'The other spouse must have either an SSN or ITIN'.

### taxpayer_work_ssn_count — Your entry, if the answer is yes
Status: **MATCH**

Model: Counts your own entry only when your SSN is valid for employment, as the label means.

### taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: A count above zero gives the yes answer for your own entry, matching 'you must have a valid SSN, which means it must be valid for employment'.

### home_cost — Did you pay over half the cost of keeping up your home for 2025?
Status: **MATCH**

Model: The included and excluded costs follow Pub. 501's 'Keeping Up a Home', and the treatment of TANF and of a person's own funds follows its Worksheet 1 note.

### unmarried — Were you unmarried, or considered unmarried under the head of household rules, at the end
Status: **MATCH**

Model: The three cases, the interlocutory-decree exception and the answer for a spouse who died in 2025 follow the Form 1040 instructions and Pub. 501 (Marital Status, Considered Unmarried, Temporary absences).

### married — Were you married at the end of 2025?
Status: **MATCH**

Model: The tests for recognized marriages, common law marriage, decrees, annulment, domestic partnerships and divorce-and-remarriage follow Pub. 501's Marital Status section. The question defers the rule for a spouse who died during the year to separate handling.

### community_property — Did you live in a community property state at any time in 2025?
Status: **MATCH**

Model: The nine states listed are those named in the text.

### hoh_community_property — Married, filing as head of household, and living in a community property state
Status: **MATCH**

Model: This gate combines HOH status, marriage and community property residence as its label says, supporting a refusal that points to Form 8958 and Pub. 555.

### credit_disallowed — Was your EIC for a year after 1996, or your child tax credit, additional child tax credit
Status: **MATCH**

Model: It tracks 'for a year after 1996' for the EIC, 'for a year after 2015' for the CTC, ACTC and ODC, the math or clerical error exception, and the 2- and 10-year periods. It asks only the fact and does not decide the Form 8862 exceptions.

### test1_persons — Number of parents who qualify you under Test 1
Status: **MATCH**

Model: Counts parents who qualify under Test 1, where 'Your parent didn't have to live with you'. Routing a parent who lives with you to Test 2 does not change the combined Test 1 or Test 2 result on ordinary facts, since such a parent also lives in the home you keep up.

### test2_persons — Number of persons who qualify you under Test 2
Status: **MATCH**

Model: Counts persons who lived with you for more than half the year, or the part of the year a relative was alive, under Pub. 501's Death or birth and Temporary absences rules. The home-cost condition is tested separately.

### test2_absence_persons — Number of persons who would qualify you under Test 2 only by counting an absence head of h
Status: **MATCH**

Model: Counts persons who pass only through an absence failing Pub. 501's rule: 'It must be reasonable to assume the absent person will return' and 'You must continue to keep up the home'.

### hoh_absence — Head of household turns on a person who lived with you more than half the year only by cou
Status: **MATCH**

Model: It is true only when the other HOH conditions are met and the outcome depends on such an absence, which is the case the refusal names.

### test1_met — Test 1 met
Status: **MATCH**

Model: Test 1 is met when at least one parent qualifies under it, consistent with the Test 1 text.

### test2_met — Test 2 met, having paid over half the cost of keeping up your own home
Status: **MATCH**

Model: Combines 'You paid over half the cost of keeping up a home in which you lived' with a qualifying person who lived there.

### hoh_eligible — Unmarried or considered unmarried, and Test 1 or Test 2 applies
Status: **MATCH**

Model: Matches 'only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies'. Both refusals name what they exclude, and their stated rules agree with Pub. 501 and the community property text.

### hoh_fails — Head of household checked without meeting its tests
Status: **MATCH**

Model: It flags HOH checked when the condition in 'only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies' is not met.

### qss_eligible — Do all five qualifying surviving spouse tests apply to you?
Status: **MISMATCH**

Restated: Input — Do all five of these tests apply to you? 1. Your spouse died in 2023 or 2024 and you didn't remarry before the end of 2025 (if your spouse died in 2025, answer No). 2. You have a child or stepchild (not a foster child) whom you can claim as a dependent, or could claim as a dependent except that, for 2025, the child had gross income of $5,200 or more, the child filed a joint return, or you could be claimed as a dependent on someone else's return; an adopted child, including a child lawfully placed with you for legal adoption, is always your own child. 3. This child lived in your home for all of 2025, counting temporary absences by you or the child for special circumstances, such as school, vacation, business, medical care, military service or detention in a juvenile facility, as time lived in the home, but only an absence from which it was reasonable to assume the absent person would return and during which you kept up the home; a child born or who died in 2025, or adopted or lawfully placed with you for legal adoption in 2025, lived with you all year if your home was the child's home for the entire time the child was alive, or since the adoption or placement; if the child did not live with you all of 2025 because the child was presumed by law enforcement authorities to have been kidnapped by someone who isn't a member of your family or the child's family, answer No (the kidnapped-child rule of Pub. 501 is outside this tool). 4. You paid over half the cost of keeping up your home (rent, mortgage interest, real estate taxes, insurance on the home, repairs, utilities and food eaten in the home; not clothing, education, medical treatment, vacations, life insurance, transportation, or the value of your own or a household member’s services; amounts paid from a household member’s own funds, such as Social Security, count as paid by them; TANF or similar payments you received and used for the home count as paid by you). 5. You could have filed a joint return with your spouse the year your spouse died, even if you didn't actually do so.

Model: The input tells a filer whose child was kidnapped to answer No, but Pub. 501 says 'You may be eligible to file as a qualifying surviving spouse even if the child who qualifies you for this filing status has been kidnapped'. No refusal applies, so a qualifying filer gets a false value and is flagged by qss_fails instead of being declined.

Ruling: scope — p501 p. 11 allows the kidnapped-child exception, which the owner explicitly kept outside this tool (BUG-0273). The question names that exclusion, and `f1040.line12e` refuses through `household.qss_fails` with the kidnapped-child remedy. BUG-0276 limits the instruction to a kidnapping that kept the child away during 2025; the exclusion is not a claim that the IRS forbids QSS.

### qss_fails — Qualifying surviving spouse checked without meeting its tests
Status: **MATCH**

Model: It flags QSS checked when the five-test answer is No, which follows 'if all of the following apply'. The kidnapped-child defect belongs to its input, qss_eligible.

### rdp — Were you a registered domestic partner in Nevada, Washington or California at any time in
Status: **MATCH**

Model: It asks about the three states named in 'A registered domestic partner in Nevada, Washington, or California'.

### spouse_died_2025 — Did your spouse die in 2025?
Status: **MATCH**

Model: This is a direct factual question that the text's filing status rules depend on, for example 'Your spouse died in 2025'.

### widowed_2025 — Filing as single or head of household although your spouse died in 2025
Status: **MATCH**

Model: It computes exactly what its label describes, and the text makes the fact relevant: 'If your spouse died during the year, you are considered married for the whole year for filing status purposes'.

### cp_married — Married at any time in 2025 while living in a community property state, though not married
Status: **MATCH**

Model: It asks the fact relevant to Pub. 501's caution: 'If you were considered married for part of the year and lived in a community property state', special rules may apply.

### cp_marriage_ended — Not filing jointly, and married for part of 2025 while living in a community property stat
Status: **MATCH**

Model: It combines the listed facts as its label says, identifying the part-year marriage case in that Pub. 501 caution.

### rdp_community_property — Not filing jointly, living in a community property state, and a registered domestic partne
Status: **MATCH**

Model: It combines the listed facts as its label says, identifying filers within the rule that a registered domestic partner 'must generally report half the combined community income'.

### filing_status_conflict — The filing status conflicts with the marriage facts entered
Status: **MISMATCH**

Restated: (f1040 line Filing Status = 'single' and helper "Were you married at the end of 2025?" = true or f1040 line Filing Status = 'mfj' and helper "Were you married at the end of 2025?" = false and helper "Did your spouse die in 2025?" = false)

Model: It tests only Single and Married filing jointly, so a filer who is divorced at year end and checks Married filing separately is not flagged. The instructions say to check that box 'if you are married at the end of 2025 and file a separate return', so the label's conflict is left undetected.

Ruling: scope — i1040gi p. 14, Married Filing Separately: a separate return is refused for the whole return by `s3.mfs` on `scope.ready`, so a still-married filer who checks MFS never reaches line 12e and cannot produce the conflict the reviewer describes. The gate covers the two supported statuses that can contradict the marriage facts (Single with a year-end marriage, and a joint return with no year-end marriage and no death in 2025); HOH and QSS have their own tests. BUG-0286 records the entry check.

## Raw response

```yaml
```yaml
lines:
  - key: "persons"
    status: MATCH
    reason: "Counts one entry per person on the return, which fits the text's treatment of you, and your spouse if filing jointly, as the people tested."
  - key: "taxpayers"
    status: MATCH
    reason: "This is a plain count of the entries marked as yours, and nothing in the text conflicts with it."
  - key: "spouses"
    status: MATCH
    reason: "This is a plain count of the entries marked as your spouse's, and nothing in the text conflicts with it."
  - key: "roster_ok"
    status: MATCH
    reason: "It requires a spouse entry only on a joint return, consistent with the text's 'you, and your spouse if filing jointly'. The under-16 refusal names its exclusion and correctly says it is an owner decision; the text mentions under-16 filers only for the Self-Select PIN."
  - key: "roster_bad"
    status: MATCH
    reason: "This is the direct negation of roster_ok, as the label says."
  - key: "hsa_people"
    status: MATCH
    reason: "Counts people with at least one Form 8889, consistent with 'complete a separate Form 8889 for each' spouse with an HSA."
  - key: "hsa_both"
    status: MATCH
    reason: "A count of two people with Forms 8889 means each spouse has one, as the label says."
  - key: "hsa_split_count"
    status: MATCH
    reason: "Counts Forms 8889 for spouses with separate HSAs and family coverage at any time during 2025, the condition in the line 6 instructions."
  - key: "hsa_agreed_count"
    status: MATCH
    reason: "Counts Forms 8889 under the line 6 rule that use the option 'unless you both agree on a different allocation'."
  - key: "hsa_step1_sum"
    status: MATCH
    reason: "Adds the refigured line 5 limits, which follow Step 1 (family-coverage months only, 'use the same amount you previously entered on line 4'). The glossary fixes line 4 at $0, and any f8889 refusal for Archer MSA filers is not shown here, so this judgment assumes such filers are excluded."
  - key: "hsa_share_sum"
    status: MATCH
    reason: "Adds each spouse's part, taken as half or as the agreed amount, which agrees with line 6 Steps 2 and 3."
  - key: "work_ssn_count"
    status: MATCH
    reason: "Counts people with an SSN valid for employment, the text's definition of a valid SSN. The question omits '(including extensions)' after the due date, which is treated as wording."
  - key: "any_work_ssn"
    status: MATCH
    reason: "Requires at least one such person, matching 'only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC'."
  - key: "eic_ssn_count"
    status: MATCH
    reason: "Counts people with an SSN valid for the EIC and issued on or before the due date, as in EIC Step 1, question 2."
  - key: "all_eic_ssn"
    status: MATCH
    reason: "Requires every person on the return to qualify, matching 'Do you, and your spouse if filing a joint return, have a social security number' valid for EIC purposes."
  - key: "under16_count"
    status: MATCH
    reason: "This is a plain count supporting the owner's under-16 entry check, and it computes what its label says."
  - key: "filer_under16"
    status: MATCH
    reason: "True when any person on the return was under 16 at the end of 2025, as the label says."
  - key: "tin_count"
    status: MATCH
    reason: "Counts an SSN or ITIN, or an application for an ITIN, matching Step 5, question 1: 'Answer Yes if you are applying for an ITIN on or before the return due date'."
  - key: "all_tin"
    status: MATCH
    reason: "Requires every person to qualify, matching 'you, and your spouse if filing jointly, must have either an SSN or ITIN'."
  - key: "id_count"
    status: MATCH
    reason: "Counts people with either a work-valid SSN or an issued SSN or ITIN, the two identification types in the CTC rule, and it computes what its label says."
  - key: "ctc_ssn"
    status: MATCH
    reason: "Requires one work-valid SSN and identification for everyone, matching 'only one spouse is required to have a valid SSN' and 'The other spouse must have either an SSN or ITIN'."
  - key: "taxpayer_work_ssn_count"
    status: MATCH
    reason: "Counts your own entry only when your SSN is valid for employment, as the label means."
  - key: "taxpayer_work_ssn"
    status: MATCH
    reason: "A count above zero gives the yes answer for your own entry, matching 'you must have a valid SSN, which means it must be valid for employment'."
  - key: "home_cost"
    status: MATCH
    reason: "The included and excluded costs follow Pub. 501's 'Keeping Up a Home', and the treatment of TANF and of a person's own funds follows its Worksheet 1 note."
  - key: "unmarried"
    status: MATCH
    reason: "The three cases, the interlocutory-decree exception and the answer for a spouse who died in 2025 follow the Form 1040 instructions and Pub. 501 (Marital Status, Considered Unmarried, Temporary absences)."
  - key: "married"
    status: MATCH
    reason: "The tests for recognized marriages, common law marriage, decrees, annulment, domestic partnerships and divorce-and-remarriage follow Pub. 501's Marital Status section. The question defers the rule for a spouse who died during the year to separate handling."
  - key: "community_property"
    status: MATCH
    reason: "The nine states listed are those named in the text."
  - key: "hoh_community_property"
    status: MATCH
    reason: "This gate combines HOH status, marriage and community property residence as its label says, supporting a refusal that points to Form 8958 and Pub. 555."
  - key: "credit_disallowed"
    status: MATCH
    reason: "It tracks 'for a year after 1996' for the EIC, 'for a year after 2015' for the CTC, ACTC and ODC, the math or clerical error exception, and the 2- and 10-year periods. It asks only the fact and does not decide the Form 8862 exceptions."
  - key: "test1_persons"
    status: MATCH
    reason: "Counts parents who qualify under Test 1, where 'Your parent didn't have to live with you'. Routing a parent who lives with you to Test 2 does not change the combined Test 1 or Test 2 result on ordinary facts, since such a parent also lives in the home you keep up."
  - key: "test2_persons"
    status: MATCH
    reason: "Counts persons who lived with you for more than half the year, or the part of the year a relative was alive, under Pub. 501's Death or birth and Temporary absences rules. The home-cost condition is tested separately."
  - key: "test2_absence_persons"
    status: MATCH
    reason: "Counts persons who pass only through an absence failing Pub. 501's rule: 'It must be reasonable to assume the absent person will return' and 'You must continue to keep up the home'."
  - key: "hoh_absence"
    status: MATCH
    reason: "It is true only when the other HOH conditions are met and the outcome depends on such an absence, which is the case the refusal names."
  - key: "test1_met"
    status: MATCH
    reason: "Test 1 is met when at least one parent qualifies under it, consistent with the Test 1 text."
  - key: "test2_met"
    status: MATCH
    reason: "Combines 'You paid over half the cost of keeping up a home in which you lived' with a qualifying person who lived there."
  - key: "hoh_eligible"
    status: MATCH
    reason: "Matches 'only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies'. Both refusals name what they exclude, and their stated rules agree with Pub. 501 and the community property text."
  - key: "hoh_fails"
    status: MATCH
    reason: "It flags HOH checked when the condition in 'only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies' is not met."
  - key: "qss_eligible"
    status: MISMATCH
    reason: "The input tells a filer whose child was kidnapped to answer No, but Pub. 501 says 'You may be eligible to file as a qualifying surviving spouse even if the child who qualifies you for this filing status has been kidnapped'. No refusal applies, so a qualifying filer gets a false value and is flagged by qss_fails instead of being declined."
  - key: "qss_fails"
    status: MATCH
    reason: "It flags QSS checked when the five-test answer is No, which follows 'if all of the following apply'. The kidnapped-child defect belongs to its input, qss_eligible."
  - key: "rdp"
    status: MATCH
    reason: "It asks about the three states named in 'A registered domestic partner in Nevada, Washington, or California'."
  - key: "spouse_died_2025"
    status: MATCH
    reason: "This is a direct factual question that the text's filing status rules depend on, for example 'Your spouse died in 2025'."
  - key: "widowed_2025"
    status: MATCH
    reason: "It computes exactly what its label describes, and the text makes the fact relevant: 'If your spouse died during the year, you are considered married for the whole year for filing status purposes'."
  - key: "cp_married"
    status: MATCH
    reason: "It asks the fact relevant to Pub. 501's caution: 'If you were considered married for part of the year and lived in a community property state', special rules may apply."
  - key: "cp_marriage_ended"
    status: MATCH
    reason: "It combines the listed facts as its label says, identifying the part-year marriage case in that Pub. 501 caution."
  - key: "rdp_community_property"
    status: MATCH
    reason: "It combines the listed facts as its label says, identifying filers within the rule that a registered domestic partner 'must generally report half the combined community income'."
  - key: "filing_status_conflict"
    status: MISMATCH
    reason: "It tests only Single and Married filing jointly, so a filer who is divorced at year end and checks Married filing separately is not flagged. The instructions say to check that box 'if you are married at the end of 2025 and file a separate return', so the label's conflict is left undetected."
```
```
