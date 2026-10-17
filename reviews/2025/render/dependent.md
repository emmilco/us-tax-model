# Render comparison — dependent

The rendered English of every printed line of `Dependents — qualifying child and qualifying relative tests, per person listed` (`rendered/2025/dependent.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | a91a6d4970af4c89a80e70850272e5d5c36b660fdbe41694d156110a4b004e70 |
| lines judged | 45 |
| match / mismatch / unclear / missing | 40 / 5 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 14, 17, 18, 19, 20, 21 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 17, 18, 19, 20, 21 | 816ff8c5ed82d0349bfa79ae008e9b4492c04005a8702145dcd8cd0139eacc47 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |

## Lines

### relationship — Relationship to you
Status: **MATCH**

Model: The categories cover the Step 1 and Step 4 relationship lists. They separate siblings' children from more remote descendants, which Step 4 does not list, and they put stepparents and in-laws together, as Step 4 does.

### age — Age at the end of 2025
Status: **MATCH**

Model: Age at the end of 2025 is what the Step 1 and Step 3 age tests use.

### student — Full-time student in 2025?
Status: **MATCH**

Model: This asks about full-time student status as defined under Full-time student.

### disabled — Permanently and totally disabled?
Status: **MATCH**

Model: It follows the definition: 'at any time in 2025' the person is permanently and totally disabled.

### months — Months lived with you in 2025, counting temporary absences
Status: **MATCH**

Model: It counts the temporary absences listed in 'Exception to time lived with you'. It applies the more-than-half rule for a qualifying child born, died, adopted or placed in the year, and the entire-time rule for others. Leaving out the adopted or placed case for others has no effect, because such a person is in the child relationship.

### self_support — Provided over half of their own support?
Status: **MATCH**

Model: Matches 'didn't provide over half of their own support for 2025'.

### joint_return — Filing a joint return other than only to claim a refund?
Status: **MATCH**

Model: Matches 'isn't filing a joint return ... or is filing ... only to claim a refund of withheld income tax or estimated tax paid'.

### citizen — U.S. citizen, U.S. national or U.S. resident alien?
Status: **MATCH**

Model: It includes the Exception to citizen test for an adopted child who lived with a U.S. citizen or national all year as a member of the household.

### canada_mexico — Resident of Canada or Mexico (if not a U.S. citizen, national or resident alien)?
Status: **MATCH**

Model: Matches the 'or a resident of Canada or Mexico' alternative in Step 2, question 1 and Step 4, question 2.

### married — Married?
Status: **MATCH**

Model: This asks the 'Was the child married?' and 'Was your qualifying relative married?' questions.

### tin — SSN, ITIN or ATIN issued on or before the due date of your return?
Status: **MATCH**

Model: Matches Step 3, question 1 and Step 5, question 2: an SSN, ITIN or ATIN issued on or before the due date, or applied for by then.

### work_ssn — SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: Matches the child's part of Step 3, question 4: an SSN 'valid for employment and issued before the due date'.

### gross_income — Gross income for 2025
Status: **MATCH**

Model: This is the gross income used in the Step 4 gross income test.

### supported — You provided over half of this person's support?
Status: **MATCH**

Model: Matches 'For whom you provided over half of the person's support in 2025'.

### other_claimant — Meets the conditions to be the qualifying child of another person?
Status: **MATCH**

Model: The IRS text excludes 'your spouse if filing jointly' and asks about any 'taxpayer'. This gate asks more broadly, so it only makes the tie-breaker refusal fire more often, which narrows the cases the program supports.

### divorced_rule — Rule for children of divorced or separated parents applies?
Status: **MATCH**

Model: This is the gate for the excluded rule for Children of divorced or separated parents.

### multiple_support — Claimed under a multiple support agreement?
Status: **MATCH**

Model: This is the gate for the excluded Multiple support agreements rule.

### parent_home_paid — For a parent not living with you, you paid over half the cost of their main home for all o
Status: **MATCH**

Model: Matches Test 1: 'paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent'.

### one — One person listed
Status: **MATCH**

Model: This counts one person toward the per-person counts on Schedule 8812 lines 4 and 6.

### zero — No amount for this person
Status: **MATCH**

Model: This is the $0 amount for a person who does not qualify.

### qc_relationship — A child, sibling, or a descendant of either
Status: **MATCH**

Model: Through the enum, this covers son, daughter, stepchild, foster child, brother, sister, the step and half siblings, 'or a descendant of any of them'.

### younger — Younger than you?
Status: **MISMATCH**

Restated: Input — Was this person younger than you?

Model: The IRS test is 'younger than you (or your spouse if filing jointly)'. The input asks only whether the person is younger than you.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### qc_age — Under 19 and younger than you, under 24 a full-time student and younger than you, or perma
Status: **MATCH**

Model: The structure of the three alternatives matches Step 1, including 'Any age and permanently and totally disabled'. The spouse omission is in the 'younger' input.

### lived_half — Lived with you for more than half of 2025
Status: **MATCH**

Model: It applies 'lived with you for more than half of 2025' to the month count, which already reflects the exceptions.

### qualifying_child — Qualifying child (Step 1)
Status: **MATCH**

Model: It combines the Step 1 relationship, age, support, joint-return and residency tests. The refusals cover the tie-breaker rules, the divorced-parent rule and married persons.

### resident — U.S. citizen, national or resident alien, or a resident of Canada or Mexico
Status: **MATCH**

Model: Matches 'a U.S. citizen, U.S. national, U.S. resident alien, or a resident of Canada or Mexico'.

### qc_dependent — Qualifying child who is your dependent (Step 2)
Status: **MISMATCH**

Restated: helper "Qualifying child (Step 1)" = true and helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = true and sa helper "Can someone claim you or your spouse as a dependent, or are you a dual-status alien?" = false

Model: Step 2 says '3. Are you filing a joint return for 2025? Yes. You can claim this child as a dependent', and question 4 asks only 'Could you be claimed as a dependent'. The restatement bars joint filers too, and adds 'your spouse' and 'dual-status alien' conditions the text does not state.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### qr_relationship — A relative listed in Step 4, or any other person who lived with you all year
Status: **MATCH**

Model: This covers the listed Step 4 relatives. Any other person, including a sibling's more remote descendants, qualifies only if they 'lived with you all year as a member of your household'.

### qr_income — Gross income under $5,200
Status: **MATCH**

Model: Matches 'gross income of less than $5,200 in 2025'.

### income_exception — Permanently and totally disabled with gross income at or over the limit
Status: **MATCH**

Model: This gates the excluded 'Exception to gross income test' for a permanently and totally disabled person whose income fails the limit.

### qualifying_relative — Qualifying relative (Step 4)
Status: **MATCH**

Model: It matches the Step 4 tests: relationship, not a qualifying child, gross income under $5,200, and over half of support provided by you. Qualifying child of another taxpayer, multiple support, the disability income exception and married persons are refused.

### qr_dependent — Qualifying relative who is your dependent (Step 4, questions 2 and 5)
Status: **MISMATCH**

Restated: helper "Qualifying relative (Step 4)" = true and helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = true and sa helper "Can someone claim you or your spouse as a dependent, or are you a dual-status alien?" = false

Model: Step 4 says '4. Are you filing a joint return for 2025? Yes. You can claim this person as a dependent', and question 5 asks only 'Could you be claimed as a dependent'. The restatement bars joint filers too, and adds spouse and dual-status conditions.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### claimed — Your dependent
Status: **MATCH**

Model: A dependent is either a Step 2 qualifying child or a Step 4 qualifying relative who can be claimed.

### under_ctc_age — Under age 17 at the end of 2025
Status: **MATCH**

Model: Matches Step 3, question 3: 'under age 17 at the end of 2025'.

### ctc_child — Qualifying child for the child tax credit (Step 3)
Status: **MISMATCH**

Restated: helper "Qualifying child who is your dependent (Step 2)" = true and helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = true and helper "U.S. citizen, U.S. national or U.S. resident alien?" = true and helper "Under age 17 at the end of 2025" = true and helper "SSN valid for employment issued before the due date of your return?" = true and household helper "Do you have an SSN valid for employment issued before the due date of your return?" = true

Model: Step 3, question 4 asks 'Did you, or your spouse if filing a joint return, and this child have SSNs valid for employment'. 'Before you begin' adds that 'only one spouse is required to have a valid SSN'. The restatement tests only the taxpayer's SSN.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### odc_person — Dependent for the credit for other dependents (Steps 3 and 5)
Status: **MISMATCH**

Restated: helper "Your dependent" = true and helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = true and helper "U.S. citizen, U.S. national or U.S. resident alien?" = true and helper "Qualifying child for the child tax credit (Step 3)" = false and household helper "Do you have an SSN or ITIN issued on or before the due date of your return, or have you applied for an ITIN by then?" = true

Model: Step 5, question 1 requires 'you, and your spouse if filing a joint return' to have an SSN or ITIN. The restatement tests only the taxpayer.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### ctc_per_child — Year parameter ctc.per_child
Status: **MATCH**

Model: Schedule 8812, line 5: 'Multiply line 4 by $2,200'.

### ctc_amount — Child tax credit amount for this person before limits ($2,200 for a qualifying child, else
Status: **MATCH**

Model: This is $2,200 per qualifying child for the child tax credit, which feeds line 4/5.

### odc_per_dependent — Year parameter odc.per_dependent
Status: **MATCH**

Model: Schedule 8812, line 7: 'Multiply line 6 by $500'.

### odc_amount — Credit for other dependents amount for this person before limits ($500 for an other depend
Status: **MATCH**

Model: This is $500 per other dependent, which feeds line 6/7.

### actc_per_child — Year parameter actc.per_child
Status: **MATCH**

Model: Schedule 8812, line 16b: 'x $1,700'.

### actc_amount — Additional child tax credit ceiling for this person ($1,700 for a qualifying child, else 0
Status: **MATCH**

Model: This is $1,700 per qualifying child, the same children used for line 4, as line 16b requires.

### hoh_test2 — A Test 2 person who lived with you more than half the year (the home-cost condition of Tes
Status: **MATCH**

Model: It covers dependents who lived with you more than half the year, excluding persons who are 'your dependent only because the person lived with you for all of 2025'. It also covers unmarried qualifying children. The divorced-parent, multiple-support and married cases are refused.

### hoh_test1 — Qualifies you for head of household under Test 1 (a parent whose main home you kept up)
Status: **MATCH**

Model: Matches Test 1: a parent you can claim as a dependent, whose main home for all of 2025 you paid over half the cost of keeping up. The multiple-support case is refused through the qualifying-relative dependency.

### hoh_person — Qualifies you for head of household (Test 1 or Test 2)
Status: **MATCH**

Model: Matches 'either Test 1 or Test 2 applies'.

## Raw response

```yaml
```yaml
lines:
  - key: "relationship"
    status: MATCH
    reason: "The categories cover the Step 1 and Step 4 relationship lists. They separate siblings' children from more remote descendants, which Step 4 does not list, and they put stepparents and in-laws together, as Step 4 does."
  - key: "age"
    status: MATCH
    reason: "Age at the end of 2025 is what the Step 1 and Step 3 age tests use."
  - key: "student"
    status: MATCH
    reason: "This asks about full-time student status as defined under Full-time student."
  - key: "disabled"
    status: MATCH
    reason: "It follows the definition: 'at any time in 2025' the person is permanently and totally disabled."
  - key: "months"
    status: MATCH
    reason: "It counts the temporary absences listed in 'Exception to time lived with you'. It applies the more-than-half rule for a qualifying child born, died, adopted or placed in the year, and the entire-time rule for others. Leaving out the adopted or placed case for others has no effect, because such a person is in the child relationship."
  - key: "self_support"
    status: MATCH
    reason: "Matches 'didn't provide over half of their own support for 2025'."
  - key: "joint_return"
    status: MATCH
    reason: "Matches 'isn't filing a joint return ... or is filing ... only to claim a refund of withheld income tax or estimated tax paid'."
  - key: "citizen"
    status: MATCH
    reason: "It includes the Exception to citizen test for an adopted child who lived with a U.S. citizen or national all year as a member of the household."
  - key: "canada_mexico"
    status: MATCH
    reason: "Matches the 'or a resident of Canada or Mexico' alternative in Step 2, question 1 and Step 4, question 2."
  - key: "married"
    status: MATCH
    reason: "This asks the 'Was the child married?' and 'Was your qualifying relative married?' questions."
  - key: "tin"
    status: MATCH
    reason: "Matches Step 3, question 1 and Step 5, question 2: an SSN, ITIN or ATIN issued on or before the due date, or applied for by then."
  - key: "work_ssn"
    status: MATCH
    reason: "Matches the child's part of Step 3, question 4: an SSN 'valid for employment and issued before the due date'."
  - key: "gross_income"
    status: MATCH
    reason: "This is the gross income used in the Step 4 gross income test."
  - key: "supported"
    status: MATCH
    reason: "Matches 'For whom you provided over half of the person's support in 2025'."
  - key: "other_claimant"
    status: MATCH
    reason: "The IRS text excludes 'your spouse if filing jointly' and asks about any 'taxpayer'. This gate asks more broadly, so it only makes the tie-breaker refusal fire more often, which narrows the cases the program supports."
  - key: "divorced_rule"
    status: MATCH
    reason: "This is the gate for the excluded rule for Children of divorced or separated parents."
  - key: "multiple_support"
    status: MATCH
    reason: "This is the gate for the excluded Multiple support agreements rule."
  - key: "parent_home_paid"
    status: MATCH
    reason: "Matches Test 1: 'paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent'."
  - key: "one"
    status: MATCH
    reason: "This counts one person toward the per-person counts on Schedule 8812 lines 4 and 6."
  - key: "zero"
    status: MATCH
    reason: "This is the $0 amount for a person who does not qualify."
  - key: "qc_relationship"
    status: MATCH
    reason: "Through the enum, this covers son, daughter, stepchild, foster child, brother, sister, the step and half siblings, 'or a descendant of any of them'."
  - key: "younger"
    status: MISMATCH
    reason: "The IRS test is 'younger than you (or your spouse if filing jointly)'. The input asks only whether the person is younger than you."
  - key: "qc_age"
    status: MATCH
    reason: "The structure of the three alternatives matches Step 1, including 'Any age and permanently and totally disabled'. The spouse omission is in the 'younger' input."
  - key: "lived_half"
    status: MATCH
    reason: "It applies 'lived with you for more than half of 2025' to the month count, which already reflects the exceptions."
  - key: "qualifying_child"
    status: MATCH
    reason: "It combines the Step 1 relationship, age, support, joint-return and residency tests. The refusals cover the tie-breaker rules, the divorced-parent rule and married persons."
  - key: "resident"
    status: MATCH
    reason: "Matches 'a U.S. citizen, U.S. national, U.S. resident alien, or a resident of Canada or Mexico'."
  - key: "qc_dependent"
    status: MISMATCH
    reason: "Step 2 says '3. Are you filing a joint return for 2025? Yes. You can claim this child as a dependent', and question 4 asks only 'Could you be claimed as a dependent'. The restatement bars joint filers too, and adds 'your spouse' and 'dual-status alien' conditions the text does not state."
  - key: "qr_relationship"
    status: MATCH
    reason: "This covers the listed Step 4 relatives. Any other person, including a sibling's more remote descendants, qualifies only if they 'lived with you all year as a member of your household'."
  - key: "qr_income"
    status: MATCH
    reason: "Matches 'gross income of less than $5,200 in 2025'."
  - key: "income_exception"
    status: MATCH
    reason: "This gates the excluded 'Exception to gross income test' for a permanently and totally disabled person whose income fails the limit."
  - key: "qualifying_relative"
    status: MATCH
    reason: "It matches the Step 4 tests: relationship, not a qualifying child, gross income under $5,200, and over half of support provided by you. Qualifying child of another taxpayer, multiple support, the disability income exception and married persons are refused."
  - key: "qr_dependent"
    status: MISMATCH
    reason: "Step 4 says '4. Are you filing a joint return for 2025? Yes. You can claim this person as a dependent', and question 5 asks only 'Could you be claimed as a dependent'. The restatement bars joint filers too, and adds spouse and dual-status conditions."
  - key: "claimed"
    status: MATCH
    reason: "A dependent is either a Step 2 qualifying child or a Step 4 qualifying relative who can be claimed."
  - key: "under_ctc_age"
    status: MATCH
    reason: "Matches Step 3, question 3: 'under age 17 at the end of 2025'."
  - key: "ctc_child"
    status: MISMATCH
    reason: "Step 3, question 4 asks 'Did you, or your spouse if filing a joint return, and this child have SSNs valid for employment'. 'Before you begin' adds that 'only one spouse is required to have a valid SSN'. The restatement tests only the taxpayer's SSN."
  - key: "odc_person"
    status: MISMATCH
    reason: "Step 5, question 1 requires 'you, and your spouse if filing a joint return' to have an SSN or ITIN. The restatement tests only the taxpayer."
  - key: "ctc_per_child"
    status: MATCH
    reason: "Schedule 8812, line 5: 'Multiply line 4 by $2,200'."
  - key: "ctc_amount"
    status: MATCH
    reason: "This is $2,200 per qualifying child for the child tax credit, which feeds line 4/5."
  - key: "odc_per_dependent"
    status: MATCH
    reason: "Schedule 8812, line 7: 'Multiply line 6 by $500'."
  - key: "odc_amount"
    status: MATCH
    reason: "This is $500 per other dependent, which feeds line 6/7."
  - key: "actc_per_child"
    status: MATCH
    reason: "Schedule 8812, line 16b: 'x $1,700'."
  - key: "actc_amount"
    status: MATCH
    reason: "This is $1,700 per qualifying child, the same children used for line 4, as line 16b requires."
  - key: "hoh_test2"
    status: MATCH
    reason: "It covers dependents who lived with you more than half the year, excluding persons who are 'your dependent only because the person lived with you for all of 2025'. It also covers unmarried qualifying children. The divorced-parent, multiple-support and married cases are refused."
  - key: "hoh_test1"
    status: MATCH
    reason: "Matches Test 1: a parent you can claim as a dependent, whose main home for all of 2025 you paid over half the cost of keeping up. The multiple-support case is refused through the qualifying-relative dependency."
  - key: "hoh_person"
    status: MATCH
    reason: "Matches 'either Test 1 or Test 2 applies'."
```
```
