# Render comparison — household

The rendered English of every printed line of `Household facts for dependents and head of household` (`rendered/2025/household.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-26 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 1513fe523a89ee55045d41da5da479ee6779f21a3d3675ef034492fe04d46d93 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 28881dbede57c2da28839a93115eb41254ae1845f441f47979304319ce659bfc |
| lines judged | 35 |
| match / mismatch / unclear / missing | 33 / 0 / 2 / 0 |
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

Model: Counts the people on the return (you, and your spouse on a joint return). This is a roster count that no IRS line contradicts.

### taxpayers — Number of entries for you
Status: **MATCH**

Model: Counts the entries marked as yours. This is a roster bookkeeping helper and is consistent with the text.

### spouses — Number of entries for your spouse
Status: **MATCH**

Model: Counts the entries marked as your spouse's. This is a roster bookkeeping helper and is consistent with the text.

### roster_ok — One entry for you, and one for your spouse exactly when filing jointly
Status: **MATCH**

Model: It requires one entry for you and one for your spouse only when filing jointly ('If joint return, spouse's first name...'). The under-16 refusal is an owner-declared narrowing that names what it excludes.

### roster_bad — The people entered do not match the filing status
Status: **MATCH**

Model: This is the plain negation of roster_ok.

### hsa_people — Number of people on the return with a Form 8889
Status: **MATCH**

Model: Counts people with a Form 8889, consistent with 'complete a separate Form 8889 for each of you.'

### hsa_both — You and your spouse each have a Form 8889
Status: **MATCH**

Model: It is true when both spouses have a Form 8889, matching 'If both you and your spouse have HSAs... Complete a separate Form 8889 for each spouse.'

### hsa_split_count — Number of Forms 8889 using the spouse rule of line 6
Status: **MATCH**

Model: Counts the Forms 8889 that use the line 6 rule for 'Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025.'

### hsa_agreed_count — Number of Forms 8889 using an agreed allocation
Status: **MATCH**

Model: Counts the line 6 forms that use an allocation the spouses agree on, per 'unless you both agree on a different allocation (such as allocating nothing to one spouse).'

### hsa_step1_sum — Both spouses Step 1 limits added together
Status: **MATCH**

Model: Adds both spouses' Step 1 refigured line 5 amounts. Each amount is figured from 'the total of the worksheet amounts only for the months you were treated as having family coverage' less line 4.

### hsa_share_sum — Both spouses parts of the Step 1 limit added together
Status: **MATCH**

Model: Adds both spouses' Step 2/3 shares, which lets the program check that the shares divide the Step 1 limit 'between you and your spouse.'

### work_ssn_count — Number of people on the return with an SSN valid for employment
Status: **MATCH**

Model: Counts the people whose SSN is 'valid for employment and issued before the due date of your return (including extensions).'

### any_work_ssn — You, or your spouse if filing jointly, have an SSN valid for employment
Status: **MATCH**

Model: Matches 'If you are filing a joint return, only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC.'

### eic_ssn_count — Number of people on the return with an SSN valid for the EIC
Status: **MATCH**

Model: Counts the people with an SSN 'issued on or before the due date of your 2025 return (including extensions) that allows you to work and is valid for EIC purposes.'

### all_eic_ssn — You, and your spouse if filing jointly, have SSNs valid for the EIC
Status: **MATCH**

Model: It requires every person on the return to qualify, matching 'Do you, and your spouse if filing a joint return, have a social security number...'

### under16_count — Number of people on the return under age 16 at the end of 2025
Status: **MATCH**

Model: Counts the filers under age 16 at the end of 2025, which feeds the owner-declared refusal. The IRS text mentions this age only for 'a first-time filer under age 16' using the Self-Select PIN.

### filer_under16 — You, or your spouse if filing jointly, were under age 16 at the end of 2025
Status: **MATCH**

Model: It is true if any filer was under 16 at the end of 2025. It serves only as the refusal gate.

### tin_count — Number of people on the return with an SSN or ITIN, or who have applied for an ITIN
Status: **MATCH**

Model: Matches Step 5 question 1, 'either an SSN or ITIN issued on or before the due date... (Answer "Yes" if you are applying for an ITIN on or before the return due date...)'.

### all_tin — You, and your spouse if filing jointly, have an SSN or ITIN, or have applied for an ITIN
Status: **MATCH**

Model: It requires 'you, and your spouse if filing a joint return' to meet the SSN/ITIN condition.

### id_count — Number of people on the return with an SSN valid for employment or an SSN or ITIN
Status: **MATCH**

Model: Counts the people with an employment-valid SSN or an SSN or ITIN. An employment-valid SSN is itself an SSN, so the count is consistent with the CTC rule.

### ctc_ssn — Child tax credit identification: you, or your spouse if filing jointly, have an SSN valid
Status: **MATCH**

Model: Matches 'only one spouse is required to have a valid SSN... The other spouse must have either an SSN or ITIN, and it must have been issued on or before the due date.' It correctly omits the ITIN-application allowance.

### taxpayer_work_ssn_count — Your entry, if the answer is yes
Status: **MATCH**

Model: Counts your own entry only when it has an SSN valid for employment issued before the due date.

### taxpayer_work_ssn — Do you have an SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: It is true when your own entry has an SSN valid for employment, matching 'you must have a valid SSN, which means it must be valid for employment and issued before the due date.'

### home_cost — Did you pay over half the cost of keeping up your home for 2025?
Status: **MATCH**

Model: This input supplies Test 2's 'You paid over half the cost of keeping up a home in which you lived.'

### unmarried — Were you unmarried, or considered unmarried under the head of household rules, at the end
Status: **MATCH**

Model: This input supplies 'only if you are unmarried (or considered unmarried)' under the head of household rules listed.

### married — Were you married at the end of 2025?
Status: **MATCH**

Model: This input is the filer's marital status at the end of 2025. It is consistent with the text's distinction that married persons may be 'considered unmarried' for head of household.

### community_property — Did you live in a community property state at any time in 2025?
Status: **MATCH**

Model: The states listed match 'Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington, and Wisconsin.'

### hoh_community_property — Married, filing as head of household, and living in a community property state
Status: **MATCH**

Model: This refusal gate covers married HOH filers in community property states, who 'must usually follow state law to determine what is community income... see Form 8958 and Pub. 555.'

### credit_disallowed — Was your EIC for a year after 1996, or your child tax credit, additional child tax credit
Status: **MATCH**

Model: Matches the Form 8862 rules for an 'EIC for a year after 1996' and for 'CTC, ACTC, or ODC for a year after 2015... denied or reduced for any reason other than a math or clerical error.' It also covers the 2- and 10-year disallowance periods.

### test1_persons — Number of parents who qualify you under Test 1
Status: **UNCLEAR**

Restated: Add dependent.one over every confirmed dependent entry for which helper "Qualifies you for head of household under Test 1 through a parent who does not live with you (a parent who lives with you qualifies you through Test 2)" = true, within the current person when parent-bound. An unanswered roster is unknown.

Model: The per-dependent helper that decides Test 1 is not defined in the text given. It cannot be confirmed that the helper checks 'paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent whom you can claim as a dependent, except under a multiple support agreement.'

Ruling: interface gap; the render of household restates the count by the label of the per-entry helper dependent.hoh_test1, whose definition is in rendered/2025/dependent.md, not in the text this review was given, so the model could not judge it. The count itself says what the page says: Test 1 is met if at least one parent qualifies (i1040gi p. 14, Test 1, "You paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent whom you can claim as a dependent, except under a multiple support agreement"). The helper is ruled on its merits in the dependent transcription logs (scope in both families; the multiple-support exception is refused on dependent.qualifying_relative). The pages given (i1040gi pp. 14, 17-19, 23, 39-44, 66) also omit p. 15 and p501 p. 9, which carry the death-year rule now in parent_home_paid.

### test2_persons — Number of persons who qualify you under Test 2
Status: **UNCLEAR**

Restated: Add dependent.one over every confirmed dependent entry for which helper "A Test 2 person who lived with you more than half the year, or of the part of the year a relative was alive (the home-cost condition of Test 2 is tested on the household form)" = true, within the current person when parent-bound. An unanswered roster is unknown.

Model: The per-dependent helper that decides Test 2 is not defined in the text given. It cannot be confirmed that the helper applies Test 2's qualifying-person categories and exclusions (divorced-parent rule, all-year-only dependents, multiple support agreements).

Ruling: interface gap; as test1_persons, the deciding helper dependent.hoh_test2 is defined in rendered/2025/dependent.md, outside the text given, and the pages given omit i1040gi p. 15 and p501 p. 9 (the part-year rule its label now names). Its content checked against i1040gi p. 14, Test 2: it counts a claimed dependent other than one who is a dependent only through the all-year household-member rule (item 1(b)), or an unmarried qualifying child whether or not a dependent (item 2), living with you more than half the year or, for a relative born or dying in 2025, more than half the part of the year alive (p501 p. 9, Death or birth); items 1(a), 1(c), 3 and 4 involve the divorced-parent, multiple-support and married-person rules, which are refused. The dependent transcription logs rule the helper (Claude: model error of the candidate; deepseek: model error of the candidate).

### test1_met — Test 1 met
Status: **MATCH**

Model: Test 1 applies if at least one parent qualifies under Test 1. This is right provided the per-dependent helper includes the parent's-home cost condition.

### test2_met — Test 2 met, having paid over half the cost of keeping up your own home
Status: **MATCH**

Model: Combines 'You paid over half the cost of keeping up a home in which you lived' with at least one qualifying person living there more than half the year.

### hoh_eligible — Unmarried or considered unmarried, and Test 1 or Test 2 applies
Status: **MATCH**

Model: Matches 'Check the "Head of household" box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies.' The community property refusal names what it excludes.

### hoh_fails — Head of household checked without meeting its tests
Status: **MATCH**

Model: It flags a return with head of household checked that does not meet the 'only if' conditions of the instructions.

## Raw response

```yaml
```yaml
lines:
  - key: "persons"
    status: MATCH
    reason: "Counts the people on the return (you, and your spouse on a joint return). This is a roster count that no IRS line contradicts."
  - key: "taxpayers"
    status: MATCH
    reason: "Counts the entries marked as yours. This is a roster bookkeeping helper and is consistent with the text."
  - key: "spouses"
    status: MATCH
    reason: "Counts the entries marked as your spouse's. This is a roster bookkeeping helper and is consistent with the text."
  - key: "roster_ok"
    status: MATCH
    reason: "It requires one entry for you and one for your spouse only when filing jointly ('If joint return, spouse's first name...'). The under-16 refusal is an owner-declared narrowing that names what it excludes."
  - key: "roster_bad"
    status: MATCH
    reason: "This is the plain negation of roster_ok."
  - key: "hsa_people"
    status: MATCH
    reason: "Counts people with a Form 8889, consistent with 'complete a separate Form 8889 for each of you.'"
  - key: "hsa_both"
    status: MATCH
    reason: "It is true when both spouses have a Form 8889, matching 'If both you and your spouse have HSAs... Complete a separate Form 8889 for each spouse.'"
  - key: "hsa_split_count"
    status: MATCH
    reason: "Counts the Forms 8889 that use the line 6 rule for 'Spouses who have separate HSAs and had family coverage under an HDHP at any time during 2025.'"
  - key: "hsa_agreed_count"
    status: MATCH
    reason: "Counts the line 6 forms that use an allocation the spouses agree on, per 'unless you both agree on a different allocation (such as allocating nothing to one spouse).'"
  - key: "hsa_step1_sum"
    status: MATCH
    reason: "Adds both spouses' Step 1 refigured line 5 amounts. Each amount is figured from 'the total of the worksheet amounts only for the months you were treated as having family coverage' less line 4."
  - key: "hsa_share_sum"
    status: MATCH
    reason: "Adds both spouses' Step 2/3 shares, which lets the program check that the shares divide the Step 1 limit 'between you and your spouse.'"
  - key: "work_ssn_count"
    status: MATCH
    reason: "Counts the people whose SSN is 'valid for employment and issued before the due date of your return (including extensions).'"
  - key: "any_work_ssn"
    status: MATCH
    reason: "Matches 'If you are filing a joint return, only one spouse is required to have a valid SSN to be eligible for the CTC and ACTC.'"
  - key: "eic_ssn_count"
    status: MATCH
    reason: "Counts the people with an SSN 'issued on or before the due date of your 2025 return (including extensions) that allows you to work and is valid for EIC purposes.'"
  - key: "all_eic_ssn"
    status: MATCH
    reason: "It requires every person on the return to qualify, matching 'Do you, and your spouse if filing a joint return, have a social security number...'"
  - key: "under16_count"
    status: MATCH
    reason: "Counts the filers under age 16 at the end of 2025, which feeds the owner-declared refusal. The IRS text mentions this age only for 'a first-time filer under age 16' using the Self-Select PIN."
  - key: "filer_under16"
    status: MATCH
    reason: "It is true if any filer was under 16 at the end of 2025. It serves only as the refusal gate."
  - key: "tin_count"
    status: MATCH
    reason: "Matches Step 5 question 1, 'either an SSN or ITIN issued on or before the due date... (Answer \"Yes\" if you are applying for an ITIN on or before the return due date...)'."
  - key: "all_tin"
    status: MATCH
    reason: "It requires 'you, and your spouse if filing a joint return' to meet the SSN/ITIN condition."
  - key: "id_count"
    status: MATCH
    reason: "Counts the people with an employment-valid SSN or an SSN or ITIN. An employment-valid SSN is itself an SSN, so the count is consistent with the CTC rule."
  - key: "ctc_ssn"
    status: MATCH
    reason: "Matches 'only one spouse is required to have a valid SSN... The other spouse must have either an SSN or ITIN, and it must have been issued on or before the due date.' It correctly omits the ITIN-application allowance."
  - key: "taxpayer_work_ssn_count"
    status: MATCH
    reason: "Counts your own entry only when it has an SSN valid for employment issued before the due date."
  - key: "taxpayer_work_ssn"
    status: MATCH
    reason: "It is true when your own entry has an SSN valid for employment, matching 'you must have a valid SSN, which means it must be valid for employment and issued before the due date.'"
  - key: "home_cost"
    status: MATCH
    reason: "This input supplies Test 2's 'You paid over half the cost of keeping up a home in which you lived.'"
  - key: "unmarried"
    status: MATCH
    reason: "This input supplies 'only if you are unmarried (or considered unmarried)' under the head of household rules listed."
  - key: "married"
    status: MATCH
    reason: "This input is the filer's marital status at the end of 2025. It is consistent with the text's distinction that married persons may be 'considered unmarried' for head of household."
  - key: "community_property"
    status: MATCH
    reason: "The states listed match 'Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington, and Wisconsin.'"
  - key: "hoh_community_property"
    status: MATCH
    reason: "This refusal gate covers married HOH filers in community property states, who 'must usually follow state law to determine what is community income... see Form 8958 and Pub. 555.'"
  - key: "credit_disallowed"
    status: MATCH
    reason: "Matches the Form 8862 rules for an 'EIC for a year after 1996' and for 'CTC, ACTC, or ODC for a year after 2015... denied or reduced for any reason other than a math or clerical error.' It also covers the 2- and 10-year disallowance periods."
  - key: "test1_persons"
    status: UNCLEAR
    reason: "The per-dependent helper that decides Test 1 is not defined in the text given. It cannot be confirmed that the helper checks 'paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent whom you can claim as a dependent, except under a multiple support agreement.'"
  - key: "test2_persons"
    status: UNCLEAR
    reason: "The per-dependent helper that decides Test 2 is not defined in the text given. It cannot be confirmed that the helper applies Test 2's qualifying-person categories and exclusions (divorced-parent rule, all-year-only dependents, multiple support agreements)."
  - key: "test1_met"
    status: MATCH
    reason: "Test 1 applies if at least one parent qualifies under Test 1. This is right provided the per-dependent helper includes the parent's-home cost condition."
  - key: "test2_met"
    status: MATCH
    reason: "Combines 'You paid over half the cost of keeping up a home in which you lived' with at least one qualifying person living there more than half the year."
  - key: "hoh_eligible"
    status: MATCH
    reason: "Matches 'Check the \"Head of household\" box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies.' The community property refusal names what it excludes."
  - key: "hoh_fails"
    status: MATCH
    reason: "It flags a return with head of household checked that does not meet the 'only if' conditions of the instructions."
```
```
