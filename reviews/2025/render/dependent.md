# Render comparison — dependent

The rendered English of every printed line of `Dependents — qualifying child and qualifying relative tests, per person listed` (`rendered/2025/dependent.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | b8944f24f288ce1dc4e3a24f1959f446f6da5a26d8da5dd898fb78ef400176d0 |
| lines judged | 45 |
| match / mismatch / unclear / missing | 40 / 5 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 14, 17, 18, 19, 20, 21 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 17, 18, 19, 20, 21 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |

## Lines

### relationship — Relationship to you
Status: **MATCH**

Model: The categories line up with the Step 1 and Step 4 relationship lists. Stepsiblings count as siblings for Step 1 and are listed in Step 4. A grandniece or a stepsibling's child is a Step 1 descendant but is not named in Step 4, so it needs the all-year household test. Household members follow the 'Any other person (other than your spouse) who lived with you all year' wording.

### age — Age at the end of 2025
Status: **MATCH**

Model: Step 1 and Step 3 test age 'at the end of 2025'.

### student — Full-time student in 2025?
Status: **MATCH**

Model: Step 1 uses 'a full-time student (defined later)'.

### disabled — Permanently and totally disabled?
Status: **MATCH**

Model: Matches the definition: disabled 'at any time in 2025'.

### months — Months lived with you in 2025, counting temporary absences
Status: **MATCH**

Model: This follows Exception to time lived with you. Temporary absences count as time lived with you. For a qualifying child born, died, adopted or placed in 2025, the test is more than half the time alive or with you; for anyone else born or died, it is the entire time alive. The restatement leaves out adopted or placed persons who are not qualifying children. Those persons fall in the 'child' category, which does not use months, so the value does not change.

### self_support — Provided over half of their own support?
Status: **MATCH**

Model: Step 1: 'didn't provide over half of their own support for 2025'.

### joint_return — Filing a joint return other than only to claim a refund?
Status: **MATCH**

Model: Step 1: 'isn't filing a joint return ... or is filing ... only to claim a refund of withheld income tax or estimated tax paid'.

### citizen — U.S. citizen, U.S. national or U.S. resident alien?
Status: **MATCH**

Model: Asks the U.S. citizen, national or resident alien question and applies the Exception to citizen test for an adopted child who lived with you all year.

### canada_mexico — Resident of Canada or Mexico (if not a U.S. citizen, national or resident alien)?
Status: **MATCH**

Model: Step 2 Q1 and Step 4 Q2 include 'or a resident of Canada or Mexico'.

### married — Married?
Status: **MATCH**

Model: Step 2 Q2 and Step 4 Q3 ask 'Was the child/qualifying relative married?'. Married persons are handled by refusal.

### tin — SSN, ITIN or ATIN issued on or before the due date of your return?
Status: **MATCH**

Model: Matches Step 3 Q1 and Step 5 Q2, including the 'Answer Yes if you are applying' rule.

### work_ssn — SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: Matches Step 3 Q4 for the child's SSN: 'valid for employment and issued before the due date of your 2025 return (including extensions)'.

### gross_income — Gross income for 2025
Status: **MATCH**

Model: This is the input for the Step 4 gross income test.

### supported — You provided over half of this person's support?
Status: **MATCH**

Model: Step 4: 'you provided over half of the person's support in 2025'.

### other_claimant — Meets the conditions to be the qualifying child of another person?
Status: **MATCH**

Model: This gates a refusal for 'Qualifying child of more than one person'. The IRS text excludes 'your spouse if filing jointly', but the broader question can only cause extra refusals, not wrong values.

### divorced_rule — Rule for children of divorced or separated parents applies?
Status: **MATCH**

Model: This gates a refusal for Children of divorced or separated parents.

### multiple_support — Claimed under a multiple support agreement?
Status: **MATCH**

Model: This gates a refusal for Multiple support agreements.

### parent_home_paid — For a parent not living with you, you paid over half the cost of their main home for all o
Status: **MATCH**

Model: Test 1: 'paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent'.

### one — One person listed
Status: **MATCH**

Model: A constant of 1 for one person listed, consistent with counting persons on Schedule 8812 lines 4 and 6.

### zero — No amount for this person
Status: **MATCH**

Model: A constant $0 used when no credit amount applies.

### qc_relationship — A child, sibling, or a descendant of either
Status: **MATCH**

Model: Step 1 covers a son, daughter, stepchild, foster child, sibling, step- or half-sibling, 'or a descendant of any of them'.

### younger — Younger than you?
Status: **MISMATCH**

Restated: Input — Was this person younger than you?

Model: The input asks only whether the person was younger than you. Step 1 says 'younger than you (or your spouse if filing jointly)'.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### qc_age — Under 19 and younger than you, under 24 a full-time student and younger than you, or perma
Status: **MATCH**

Model: Matches Step 1: under 19 and younger, or under 24, a full-time student and younger, or 'Any age and permanently and totally disabled'. Any error comes from the 'younger' input, not this line.

### lived_half — Lived with you for more than half of 2025
Status: **MATCH**

Model: Step 1: 'lived with you for more than half of 2025'. With whole months, this means more than 6.

### qualifying_child — Qualifying child (Step 1)
Status: **MATCH**

Model: This combines the Step 1 relationship, age, support, joint-return and residency tests. Refusals exclude the more-than-one-person, divorced-parent and married cases.

### resident — U.S. citizen, national or resident alien, or a resident of Canada or Mexico
Status: **MATCH**

Model: Step 2 Q1: 'a U.S. citizen, U.S. national, U.S. resident alien, or a resident of Canada or Mexico'.

### qc_dependent — Qualifying child who is your dependent (Step 2)
Status: **MISMATCH**

Restated: helper "Qualifying child (Step 1)" = true and helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = true and sa helper "Can someone claim you or your spouse as a dependent, or are you a dual-status alien?" = false

Model: The program's gate also fails if your spouse can be claimed or you are dual-status, even on a joint return. Step 2 says '3. Are you filing a joint return for 2025? Yes. You can claim this child as a dependent', and Q4 asks only 'Could you be claimed as a dependent on someone else's 2025 tax return?'. Dual-status is not mentioned.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### qr_relationship — A relative listed in Step 4, or any other person who lived with you all year
Status: **MATCH**

Model: Matches the Step 4 relative list plus 'Any other person (other than your spouse) who lived with you all year as a member of your household'.

### qr_income — Gross income under $5,200
Status: **MATCH**

Model: Step 4: 'gross income of less than $5,200 in 2025'.

### income_exception — Permanently and totally disabled with gross income at or over the limit
Status: **MATCH**

Model: This flags disabled persons at or over the limit for refusal under Exception to gross income test.

### qualifying_relative — Qualifying relative (Step 4)
Status: **MATCH**

Model: Combines the Step 4 relationship, income and support tests with 'wasn't a qualifying child ... of any taxpayer'. The case of being another person's qualifying child is excluded through the qualifying_child refusal. Multiple support, the disability income exception and married persons are refused.

### qr_dependent — Qualifying relative who is your dependent (Step 4, questions 2 and 5)
Status: **MISMATCH**

Restated: helper "Qualifying relative (Step 4)" = true and helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = true and sa helper "Can someone claim you or your spouse as a dependent, or are you a dual-status alien?" = false

Model: Same gate problem as qc_dependent: it blocks on a spouse who can be claimed or on dual-status even for joint filers. Step 4 says '4. Are you filing a joint return for 2025? Yes. You can claim this person as a dependent', and Q5 asks only whether 'you' could be claimed.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### claimed — Your dependent
Status: **MATCH**

Model: A dependent under either Step 2 or Step 4.

### under_ctc_age — Under age 17 at the end of 2025
Status: **MATCH**

Model: Step 3 Q3: 'under age 17 at the end of 2025'.

### ctc_child — Qualifying child for the child tax credit (Step 3)
Status: **MISMATCH**

Restated: helper "Qualifying child who is your dependent (Step 2)" = true and helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = true and helper "U.S. citizen, U.S. national or U.S. resident alien?" = true and helper "Under age 17 at the end of 2025" = true and helper "SSN valid for employment issued before the due date of your return?" = true and household helper "Do you have an SSN valid for employment issued before the due date of your return?" = true

Model: This requires the taxpayer's own work-valid SSN. Step 3 Q4 says 'Did you, or your spouse if filing a joint return, and this child have SSNs valid for employment', and the instructions add 'only one spouse is required to have a valid SSN'.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### odc_person — Dependent for the credit for other dependents (Steps 3 and 5)
Status: **MISMATCH**

Restated: helper "Your dependent" = true and helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = true and helper "U.S. citizen, U.S. national or U.S. resident alien?" = true and helper "Qualifying child for the child tax credit (Step 3)" = false and household helper "Do you have an SSN or ITIN issued on or before the due date of your return, or have you applied for an ITIN by then?" = true

Model: This tests only the taxpayer's SSN or ITIN. The IRS says 'you, and your spouse if filing jointly, must have either an SSN or ITIN issued on or before the due date' (Before you begin; Step 5 Q1), so a joint filer's spouse lacking one is missed.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### ctc_per_child — Year parameter ctc.per_child
Status: **MATCH**

Model: Schedule 8812 line 5: 'Multiply line 4 by $2,200'.

### ctc_amount — Child tax credit amount for this person before limits ($2,200 for a qualifying child, else
Status: **MATCH**

Model: $2,200 per qualifying child under 17 with the required SSN, else 0, per line 5.

### odc_per_dependent — Year parameter odc.per_dependent
Status: **MATCH**

Model: Schedule 8812 line 7: 'Multiply line 6 by $500'.

### odc_amount — Credit for other dependents amount for this person before limits ($500 for an other depend
Status: **MATCH**

Model: $500 per other dependent, else 0, per line 7.

### actc_per_child — Year parameter actc.per_child
Status: **MATCH**

Model: Schedule 8812 line 16b: 'x $1,700'.

### actc_amount — Additional child tax credit ceiling for this person ($1,700 for a qualifying child, else 0
Status: **MATCH**

Model: $1,700 per qualifying child counted on line 4, per line 16b.

### hoh_test2 — A Test 2 person who lived with you more than half the year (the home-cost condition of Tes
Status: **MATCH**

Model: Matches Test 2. It covers dependents who lived with you over half the year, except those who are dependents only because they lived with you all year. It also covers unmarried qualifying children who are not dependents. The divorced-parent, multiple support and married cases are refused upstream.

### hoh_test1 — Qualifies you for head of household under Test 1 (a parent whose main home you kept up)
Status: **MATCH**

Model: Test 1: a parent you can claim as a dependent whose main home for all of 2025 you paid over half to keep up. The multiple support case is refused upstream.

### hoh_person — Qualifies you for head of household (Test 1 or Test 2)
Status: **MATCH**

Model: 'either Test 1 or Test 2 applies'.

## Raw response

```yaml
```yaml
lines:
  - key: "relationship"
    status: MATCH
    reason: "The categories line up with the Step 1 and Step 4 relationship lists. Stepsiblings count as siblings for Step 1 and are listed in Step 4. A grandniece or a stepsibling's child is a Step 1 descendant but is not named in Step 4, so it needs the all-year household test. Household members follow the 'Any other person (other than your spouse) who lived with you all year' wording."
  - key: "age"
    status: MATCH
    reason: "Step 1 and Step 3 test age 'at the end of 2025'."
  - key: "student"
    status: MATCH
    reason: "Step 1 uses 'a full-time student (defined later)'."
  - key: "disabled"
    status: MATCH
    reason: "Matches the definition: disabled 'at any time in 2025'."
  - key: "months"
    status: MATCH
    reason: "This follows Exception to time lived with you. Temporary absences count as time lived with you. For a qualifying child born, died, adopted or placed in 2025, the test is more than half the time alive or with you; for anyone else born or died, it is the entire time alive. The restatement leaves out adopted or placed persons who are not qualifying children. Those persons fall in the 'child' category, which does not use months, so the value does not change."
  - key: "self_support"
    status: MATCH
    reason: "Step 1: 'didn't provide over half of their own support for 2025'."
  - key: "joint_return"
    status: MATCH
    reason: "Step 1: 'isn't filing a joint return ... or is filing ... only to claim a refund of withheld income tax or estimated tax paid'."
  - key: "citizen"
    status: MATCH
    reason: "Asks the U.S. citizen, national or resident alien question and applies the Exception to citizen test for an adopted child who lived with you all year."
  - key: "canada_mexico"
    status: MATCH
    reason: "Step 2 Q1 and Step 4 Q2 include 'or a resident of Canada or Mexico'."
  - key: "married"
    status: MATCH
    reason: "Step 2 Q2 and Step 4 Q3 ask 'Was the child/qualifying relative married?'. Married persons are handled by refusal."
  - key: "tin"
    status: MATCH
    reason: "Matches Step 3 Q1 and Step 5 Q2, including the 'Answer Yes if you are applying' rule."
  - key: "work_ssn"
    status: MATCH
    reason: "Matches Step 3 Q4 for the child's SSN: 'valid for employment and issued before the due date of your 2025 return (including extensions)'."
  - key: "gross_income"
    status: MATCH
    reason: "This is the input for the Step 4 gross income test."
  - key: "supported"
    status: MATCH
    reason: "Step 4: 'you provided over half of the person's support in 2025'."
  - key: "other_claimant"
    status: MATCH
    reason: "This gates a refusal for 'Qualifying child of more than one person'. The IRS text excludes 'your spouse if filing jointly', but the broader question can only cause extra refusals, not wrong values."
  - key: "divorced_rule"
    status: MATCH
    reason: "This gates a refusal for Children of divorced or separated parents."
  - key: "multiple_support"
    status: MATCH
    reason: "This gates a refusal for Multiple support agreements."
  - key: "parent_home_paid"
    status: MATCH
    reason: "Test 1: 'paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent'."
  - key: "one"
    status: MATCH
    reason: "A constant of 1 for one person listed, consistent with counting persons on Schedule 8812 lines 4 and 6."
  - key: "zero"
    status: MATCH
    reason: "A constant $0 used when no credit amount applies."
  - key: "qc_relationship"
    status: MATCH
    reason: "Step 1 covers a son, daughter, stepchild, foster child, sibling, step- or half-sibling, 'or a descendant of any of them'."
  - key: "younger"
    status: MISMATCH
    reason: "The input asks only whether the person was younger than you. Step 1 says 'younger than you (or your spouse if filing jointly)'."
  - key: "qc_age"
    status: MATCH
    reason: "Matches Step 1: under 19 and younger, or under 24, a full-time student and younger, or 'Any age and permanently and totally disabled'. Any error comes from the 'younger' input, not this line."
  - key: "lived_half"
    status: MATCH
    reason: "Step 1: 'lived with you for more than half of 2025'. With whole months, this means more than 6."
  - key: "qualifying_child"
    status: MATCH
    reason: "This combines the Step 1 relationship, age, support, joint-return and residency tests. Refusals exclude the more-than-one-person, divorced-parent and married cases."
  - key: "resident"
    status: MATCH
    reason: "Step 2 Q1: 'a U.S. citizen, U.S. national, U.S. resident alien, or a resident of Canada or Mexico'."
  - key: "qc_dependent"
    status: MISMATCH
    reason: "The program's gate also fails if your spouse can be claimed or you are dual-status, even on a joint return. Step 2 says '3. Are you filing a joint return for 2025? Yes. You can claim this child as a dependent', and Q4 asks only 'Could you be claimed as a dependent on someone else's 2025 tax return?'. Dual-status is not mentioned."
  - key: "qr_relationship"
    status: MATCH
    reason: "Matches the Step 4 relative list plus 'Any other person (other than your spouse) who lived with you all year as a member of your household'."
  - key: "qr_income"
    status: MATCH
    reason: "Step 4: 'gross income of less than $5,200 in 2025'."
  - key: "income_exception"
    status: MATCH
    reason: "This flags disabled persons at or over the limit for refusal under Exception to gross income test."
  - key: "qualifying_relative"
    status: MATCH
    reason: "Combines the Step 4 relationship, income and support tests with 'wasn't a qualifying child ... of any taxpayer'. The case of being another person's qualifying child is excluded through the qualifying_child refusal. Multiple support, the disability income exception and married persons are refused."
  - key: "qr_dependent"
    status: MISMATCH
    reason: "Same gate problem as qc_dependent: it blocks on a spouse who can be claimed or on dual-status even for joint filers. Step 4 says '4. Are you filing a joint return for 2025? Yes. You can claim this person as a dependent', and Q5 asks only whether 'you' could be claimed."
  - key: "claimed"
    status: MATCH
    reason: "A dependent under either Step 2 or Step 4."
  - key: "under_ctc_age"
    status: MATCH
    reason: "Step 3 Q3: 'under age 17 at the end of 2025'."
  - key: "ctc_child"
    status: MISMATCH
    reason: "This requires the taxpayer's own work-valid SSN. Step 3 Q4 says 'Did you, or your spouse if filing a joint return, and this child have SSNs valid for employment', and the instructions add 'only one spouse is required to have a valid SSN'."
  - key: "odc_person"
    status: MISMATCH
    reason: "This tests only the taxpayer's SSN or ITIN. The IRS says 'you, and your spouse if filing jointly, must have either an SSN or ITIN issued on or before the due date' (Before you begin; Step 5 Q1), so a joint filer's spouse lacking one is missed."
  - key: "ctc_per_child"
    status: MATCH
    reason: "Schedule 8812 line 5: 'Multiply line 4 by $2,200'."
  - key: "ctc_amount"
    status: MATCH
    reason: "$2,200 per qualifying child under 17 with the required SSN, else 0, per line 5."
  - key: "odc_per_dependent"
    status: MATCH
    reason: "Schedule 8812 line 7: 'Multiply line 6 by $500'."
  - key: "odc_amount"
    status: MATCH
    reason: "$500 per other dependent, else 0, per line 7."
  - key: "actc_per_child"
    status: MATCH
    reason: "Schedule 8812 line 16b: 'x $1,700'."
  - key: "actc_amount"
    status: MATCH
    reason: "$1,700 per qualifying child counted on line 4, per line 16b."
  - key: "hoh_test2"
    status: MATCH
    reason: "Matches Test 2. It covers dependents who lived with you over half the year, except those who are dependents only because they lived with you all year. It also covers unmarried qualifying children who are not dependents. The divorced-parent, multiple support and married cases are refused upstream."
  - key: "hoh_test1"
    status: MATCH
    reason: "Test 1: a parent you can claim as a dependent whose main home for all of 2025 you paid over half to keep up. The multiple support case is refused upstream."
  - key: "hoh_person"
    status: MATCH
    reason: "'either Test 1 or Test 2 applies'."
```
```
