# Render comparison — dependent

The rendered English of every printed line of `Dependents — qualifying child and qualifying relative tests, per person listed` (`rendered/2025/dependent.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 2ce66f778092a7f6f2d6dac68d4e04ee3068220b931522993e9a7377a8561d46 |
| lines judged | 49 |
| match / mismatch / unclear / missing | 44 / 5 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 14, 17, 18, 19, 20, 21, 41, 43, 44, 45, 46 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 17, 18, 19, 20, 21, 41, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |

## Lines

### relationship — Relationship to you
Status: **MATCH**

Model: The categories map onto the Step 1 and Step 4 relationship lists. Stepsiblings are in 'sibling' (listed in both steps). Grandnieces and stepsiblings' children are in 'sibling_descendant', which counts for Step 1 ('a descendant of any of them') but needs a full year in the household for Step 4. Step-parents and in-laws match the Step 4 list.

### age — Age at the end of 2025
Status: **MATCH**

Model: Step 1 and Step 3 test age 'at the end of 2025'.

### student — Full-time student in 2025?
Status: **MATCH**

Model: Step 1 asks whether the person is 'a full-time student (defined later)'; the definition is applied when answering.

### disabled — Permanently and totally disabled?
Status: **MATCH**

Model: This matches the definition: 'at any time in 2025, the person can't engage in any substantial gainful activity...'.

### months — Months lived with you in 2025, counting temporary absences
Status: **MATCH**

Model: It follows 'Exception to time lived with you': temporary absences count as time lived with you, and the more-than-half rule applies to a qualifying child who was born, died, adopted or placed in 2025. For any other person, entering 12 requires the entire time alive or since adoption or placement, which matches the IRS rule.

### self_support — Provided over half of their own support?
Status: **MATCH**

Model: Step 1: 'Who didn't provide over half of their own support for 2025.'

### joint_return — Filing a joint return other than only to claim a refund?
Status: **MATCH**

Model: Step 1: 'isn't filing a joint return for 2025 or is filing a joint return for 2025 only to claim a refund of withheld income tax or estimated tax paid.'

### citizen — U.S. citizen, U.S. national or U.S. resident alien?
Status: **MATCH**

Model: Step 3 Q2 and Step 5 Q3 ask this question. The adopted-child note follows 'Exception to citizen test' (you are a U.S. citizen or national and the child lived with you all year).

### canada_mexico — Resident of Canada or Mexico (if not a U.S. citizen, national or resident alien)?
Status: **MATCH**

Model: Step 2 Q1 and Step 4 Q2 accept 'a resident of Canada or Mexico.'

### married — Married?
Status: **MATCH**

Model: Step 2 Q2 and Step 4 Q3 ask 'Was the child [qualifying relative] married?'. The EIC 'Married child' rule uses 'married at the end of 2025.'

### tin — SSN, ITIN or ATIN issued on or before the due date of your return?
Status: **MATCH**

Model: Step 3 Q1 and Step 5 Q2 ask about an SSN, ITIN or ATIN 'issued on or before the due date of your return (including extensions)', with 'Yes' if you are applying for an ITIN or ATIN by then.

### work_ssn — SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: Step 3 Q4 asks whether the child has an SSN 'valid for employment and issued before the due date of your 2025 return (including extensions).'

### gross_income — Gross income for 2025
Status: **MATCH**

Model: This is the input to the Step 4 gross income test.

### supported — You provided over half of this person's support?
Status: **MATCH**

Model: Step 4: 'For whom you provided over half of the person's support in 2025.'

### other_claimant — Meets the conditions to be the qualifying child of another person?
Status: **MATCH**

Model: Step 1 caution: 'If the child meets the conditions to be a qualifying child of any other person... see Qualifying child of more than one person.'

### divorced_rule — Rule for children of divorced or separated parents applies?
Status: **MATCH**

Model: This gates the 'Children of divorced or separated parents' rule, which the text refers to in Step 4 and in the definitions.

### multiple_support — Claimed under a multiple support agreement?
Status: **MATCH**

Model: This gates 'Multiple support agreements', which the text refers to in Step 4 and in head of household Test 1 and Test 2.

### parent_home_paid — For a parent not living with you, you paid over half the cost of their main home for all o
Status: **MATCH**

Model: Test 1: 'You paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent.'

### one — One person listed
Status: **MATCH**

Model: This is a bookkeeping count of one person per form. The IRS text has nothing that conflicts with it.

### zero — No amount for this person
Status: **MATCH**

Model: This is a $0 constant used when no credit amount applies to the person.

### qc_relationship — A child, sibling, or a descendant of either
Status: **MATCH**

Model: Step 1: 'Son, daughter, stepchild, foster child, brother, sister, stepbrother, stepsister, half brother, half sister, or a descendant of any of them.'

### younger — Younger than you?
Status: **MISMATCH**

Restated: Input — Was this person younger than you?

Model: The IRS test is 'younger than you (or your spouse if filing jointly)'. The input asks only whether the person is younger than you, so a child older than you but younger than your joint-filing spouse fails.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### us_half — Lived with you in the United States for more than half of 2025?
Status: **MATCH**

Model: It follows the EIC Step 3 test 'lived with you in the United States for more than half of 2025', including the definitions of 'United States' and 'Members of the military' and the EIC 'Exception to time lived with you.'

### eic_ssn — SSN valid for the EIC, issued on or before the due date of your return?
Status: **MATCH**

Model: It follows the EIC 'Social security number (SSN)' definition, including the 'Not Valid for Employment' and 'Valid for Work Only With DHS Authorization' rules, and the requirement that the SSN be issued on or before the due date.

### qc_age — Under 19 and younger than you, under 24 a full-time student and younger than you, or perma
Status: **MATCH**

Model: The structure matches Step 1: under 19 and younger, or under 24, a full-time student and younger, or 'Any age and permanently and totally disabled.' It inherits the missing spouse alternative from the 'younger' helper.

### lived_half — Lived with you for more than half of 2025
Status: **MATCH**

Model: More than 6 months is 'more than half of 2025'. The months input already applies the exceptions to time lived with you.

### qualifying_child — Qualifying child (Step 1)
Status: **MATCH**

Model: This is the conjunction of the Step 1 tests: relationship, age, support, joint return and residency. The refusals cover the other-claimant tie-breaker, the divorced or separated parents rule and the married person rules.

### resident — U.S. citizen, national or resident alien, or a resident of Canada or Mexico
Status: **MATCH**

Model: Step 2 Q1 and Step 4 Q2: 'U.S. citizen, U.S. national, U.S. resident alien, or a resident of Canada or Mexico.'

### qc_dependent — Qualifying child who is your dependent (Step 2)
Status: **MISMATCH**

Restated: helper "Qualifying child (Step 1)" = true and helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = true and sa helper "Can someone claim you or your spouse as a dependent, or are you a dual-status alien?" = false

Model: Step 2 asks only 'Could you be claimed as a dependent on someone else's 2025 tax return?', and Q3 lets a joint filer claim the child without asking that. It also says to answer 'No' if the claimer isn't required to file and isn't filing, or files only for a refund. The gate adds 'or your spouse' and 'dual-status alien' conditions that the text does not contain.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### qr_relationship — A relative listed in Step 4, or any other person who lived with you all year
Status: **MATCH**

Model: The listed relatives match Step 4. Other people, including more distant sibling descendants, qualify only if they 'lived with you all year as a member of your household', which is tested as months = 12.

### qr_income — Gross income under $5,200
Status: **MATCH**

Model: Step 4: 'gross income of less than $5,200 in 2025.'

### income_exception — Permanently and totally disabled with gross income at or over the limit
Status: **MATCH**

Model: It flags the 'Exception to gross income test' case for a permanently and totally disabled person whose income fails the limit, which the program refuses.

### qualifying_relative — Qualifying relative (Step 4)
Status: **MATCH**

Model: These are the Step 4 tests. The 'qualifying child of any taxpayer' test is covered by requiring that the person not be your qualifying child, together with the other-claimant refusal inherited from qualifying_child. Multiple support, the income exception and married persons are refused.

### qr_dependent — Qualifying relative who is your dependent (Step 4, questions 2 and 5)
Status: **MISMATCH**

Restated: helper "Qualifying relative (Step 4)" = true and helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = true and sa helper "Can someone claim you or your spouse as a dependent, or are you a dual-status alien?" = false

Model: Step 4 Q5 asks only 'Could you be claimed as a dependent on someone else's 2025 tax return?', and Q4 skips it for joint filers. The gate also tests 'your spouse' and 'dual-status alien', which are not in the text.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### claimed — Your dependent
Status: **MATCH**

Model: A dependent is either a qualifying child who passes Step 2 or a qualifying relative who passes Step 4.

### under_ctc_age — Under age 17 at the end of 2025
Status: **MATCH**

Model: Step 3 Q3: 'Was the child under age 17 at the end of 2025?'

### ctc_child — Qualifying child for the child tax credit (Step 3)
Status: **MISMATCH**

Restated: helper "Qualifying child who is your dependent (Step 2)" = true and helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = true and helper "U.S. citizen, U.S. national or U.S. resident alien?" = true and helper "Under age 17 at the end of 2025" = true and helper "SSN valid for employment issued before the due date of your return?" = true and household helper "Do you have an SSN valid for employment issued before the due date of your return?" = true

Model: Step 3 Q4 asks 'Did you, or your spouse if filing a joint return, and this child have SSNs valid for employment', and 'only one spouse is required to have a valid SSN'. The restatement requires your own work-valid SSN and ignores the spouse alternative.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### odc_person — Dependent for the credit for other dependents (Steps 3 and 5)
Status: **MISMATCH**

Restated: helper "Your dependent" = true and helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = true and helper "U.S. citizen, U.S. national or U.S. resident alien?" = true and helper "Qualifying child for the child tax credit (Step 3)" = false and household helper "Do you have an SSN or ITIN issued on or before the due date of your return, or have you applied for an ITIN by then?" = true

Model: Step 5 Q1 requires 'you, and your spouse if filing a joint return' to have an SSN or ITIN. The restatement tests only your own TIN, so it allows the credit when a joint-filing spouse has none.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### ctc_per_child — Year parameter ctc.per_child
Status: **MATCH**

Model: Schedule 8812 line 5: 'Multiply line 4 by $2,200.'

### ctc_amount — Child tax credit amount for this person before limits ($2,200 for a qualifying child, else
Status: **MATCH**

Model: This is $2,200 per child counted on line 4, consistent with line 5.

### odc_per_dependent — Year parameter odc.per_dependent
Status: **MATCH**

Model: Schedule 8812 line 7: 'Multiply line 6 by $500.'

### odc_amount — Credit for other dependents amount for this person before limits ($500 for an other depend
Status: **MATCH**

Model: This is $500 per other dependent counted on line 6, which excludes anyone included on line 4.

### actc_per_child — Year parameter actc.per_child
Status: **MATCH**

Model: Schedule 8812 line 16b: 'Number of qualifying children under age 17 with the required social security number: x $1,700.'

### actc_amount — Additional child tax credit ceiling for this person ($1,700 for a qualifying child, else 0
Status: **MATCH**

Model: This is $1,700 per child counted on line 4, consistent with line 16b ('same as the number of children you used for line 4').

### hoh_test2 — A Test 2 person who lived with you more than half the year (the home-cost condition of Tes
Status: **MATCH**

Model: Test 2 covers a dependent who lived with you more than half the year, excluding one who is 'your dependent only because the person lived with you for all of 2025', or 'Your unmarried qualifying child who isn't your dependent'. The divorced-rule, multiple-support and married cases are refused.

### hoh_test1 — Qualifies you for head of household under Test 1 through a parent who does not live with y
Status: **MATCH**

Model: Test 1 requires a parent 'whom you can claim as a dependent' and that you paid over half the cost of the parent's main home for all of 2025. Multiple support agreements are refused.

### hoh_person — Qualifies you for head of household (Test 1 or Test 2)
Status: **MATCH**

Model: Head of household applies if 'either Test 1 or Test 2 applies'. The home-cost condition of Test 2 is tested elsewhere.

### eic_child — Qualifying child for the EIC (relationship, age, not filing a joint return, lived with you
Status: **MATCH**

Model: These are the EIC Step 3 tests: relationship, age, joint return and U.S. residence for more than half the year. The tie-breaker and married child cases are refused. It inherits the missing spouse alternative from the 'younger' helper.

### eic_ssn_child — Qualifying child for the EIC who has a valid SSN
Status: **MATCH**

Model: Worksheet A counts 'qualifying children you have who have valid SSNs', and the text says a child without a timely SSN can't be counted.

## Raw response

```yaml
```yaml
lines:
  - key: "relationship"
    status: MATCH
    reason: "The categories map onto the Step 1 and Step 4 relationship lists. Stepsiblings are in 'sibling' (listed in both steps). Grandnieces and stepsiblings' children are in 'sibling_descendant', which counts for Step 1 ('a descendant of any of them') but needs a full year in the household for Step 4. Step-parents and in-laws match the Step 4 list."
  - key: "age"
    status: MATCH
    reason: "Step 1 and Step 3 test age 'at the end of 2025'."
  - key: "student"
    status: MATCH
    reason: "Step 1 asks whether the person is 'a full-time student (defined later)'; the definition is applied when answering."
  - key: "disabled"
    status: MATCH
    reason: "This matches the definition: 'at any time in 2025, the person can't engage in any substantial gainful activity...'."
  - key: "months"
    status: MATCH
    reason: "It follows 'Exception to time lived with you': temporary absences count as time lived with you, and the more-than-half rule applies to a qualifying child who was born, died, adopted or placed in 2025. For any other person, entering 12 requires the entire time alive or since adoption or placement, which matches the IRS rule."
  - key: "self_support"
    status: MATCH
    reason: "Step 1: 'Who didn't provide over half of their own support for 2025.'"
  - key: "joint_return"
    status: MATCH
    reason: "Step 1: 'isn't filing a joint return for 2025 or is filing a joint return for 2025 only to claim a refund of withheld income tax or estimated tax paid.'"
  - key: "citizen"
    status: MATCH
    reason: "Step 3 Q2 and Step 5 Q3 ask this question. The adopted-child note follows 'Exception to citizen test' (you are a U.S. citizen or national and the child lived with you all year)."
  - key: "canada_mexico"
    status: MATCH
    reason: "Step 2 Q1 and Step 4 Q2 accept 'a resident of Canada or Mexico.'"
  - key: "married"
    status: MATCH
    reason: "Step 2 Q2 and Step 4 Q3 ask 'Was the child [qualifying relative] married?'. The EIC 'Married child' rule uses 'married at the end of 2025.'"
  - key: "tin"
    status: MATCH
    reason: "Step 3 Q1 and Step 5 Q2 ask about an SSN, ITIN or ATIN 'issued on or before the due date of your return (including extensions)', with 'Yes' if you are applying for an ITIN or ATIN by then."
  - key: "work_ssn"
    status: MATCH
    reason: "Step 3 Q4 asks whether the child has an SSN 'valid for employment and issued before the due date of your 2025 return (including extensions).'"
  - key: "gross_income"
    status: MATCH
    reason: "This is the input to the Step 4 gross income test."
  - key: "supported"
    status: MATCH
    reason: "Step 4: 'For whom you provided over half of the person's support in 2025.'"
  - key: "other_claimant"
    status: MATCH
    reason: "Step 1 caution: 'If the child meets the conditions to be a qualifying child of any other person... see Qualifying child of more than one person.'"
  - key: "divorced_rule"
    status: MATCH
    reason: "This gates the 'Children of divorced or separated parents' rule, which the text refers to in Step 4 and in the definitions."
  - key: "multiple_support"
    status: MATCH
    reason: "This gates 'Multiple support agreements', which the text refers to in Step 4 and in head of household Test 1 and Test 2."
  - key: "parent_home_paid"
    status: MATCH
    reason: "Test 1: 'You paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent.'"
  - key: "one"
    status: MATCH
    reason: "This is a bookkeeping count of one person per form. The IRS text has nothing that conflicts with it."
  - key: "zero"
    status: MATCH
    reason: "This is a $0 constant used when no credit amount applies to the person."
  - key: "qc_relationship"
    status: MATCH
    reason: "Step 1: 'Son, daughter, stepchild, foster child, brother, sister, stepbrother, stepsister, half brother, half sister, or a descendant of any of them.'"
  - key: "younger"
    status: MISMATCH
    reason: "The IRS test is 'younger than you (or your spouse if filing jointly)'. The input asks only whether the person is younger than you, so a child older than you but younger than your joint-filing spouse fails."
  - key: "us_half"
    status: MATCH
    reason: "It follows the EIC Step 3 test 'lived with you in the United States for more than half of 2025', including the definitions of 'United States' and 'Members of the military' and the EIC 'Exception to time lived with you.'"
  - key: "eic_ssn"
    status: MATCH
    reason: "It follows the EIC 'Social security number (SSN)' definition, including the 'Not Valid for Employment' and 'Valid for Work Only With DHS Authorization' rules, and the requirement that the SSN be issued on or before the due date."
  - key: "qc_age"
    status: MATCH
    reason: "The structure matches Step 1: under 19 and younger, or under 24, a full-time student and younger, or 'Any age and permanently and totally disabled.' It inherits the missing spouse alternative from the 'younger' helper."
  - key: "lived_half"
    status: MATCH
    reason: "More than 6 months is 'more than half of 2025'. The months input already applies the exceptions to time lived with you."
  - key: "qualifying_child"
    status: MATCH
    reason: "This is the conjunction of the Step 1 tests: relationship, age, support, joint return and residency. The refusals cover the other-claimant tie-breaker, the divorced or separated parents rule and the married person rules."
  - key: "resident"
    status: MATCH
    reason: "Step 2 Q1 and Step 4 Q2: 'U.S. citizen, U.S. national, U.S. resident alien, or a resident of Canada or Mexico.'"
  - key: "qc_dependent"
    status: MISMATCH
    reason: "Step 2 asks only 'Could you be claimed as a dependent on someone else's 2025 tax return?', and Q3 lets a joint filer claim the child without asking that. It also says to answer 'No' if the claimer isn't required to file and isn't filing, or files only for a refund. The gate adds 'or your spouse' and 'dual-status alien' conditions that the text does not contain."
  - key: "qr_relationship"
    status: MATCH
    reason: "The listed relatives match Step 4. Other people, including more distant sibling descendants, qualify only if they 'lived with you all year as a member of your household', which is tested as months = 12."
  - key: "qr_income"
    status: MATCH
    reason: "Step 4: 'gross income of less than $5,200 in 2025.'"
  - key: "income_exception"
    status: MATCH
    reason: "It flags the 'Exception to gross income test' case for a permanently and totally disabled person whose income fails the limit, which the program refuses."
  - key: "qualifying_relative"
    status: MATCH
    reason: "These are the Step 4 tests. The 'qualifying child of any taxpayer' test is covered by requiring that the person not be your qualifying child, together with the other-claimant refusal inherited from qualifying_child. Multiple support, the income exception and married persons are refused."
  - key: "qr_dependent"
    status: MISMATCH
    reason: "Step 4 Q5 asks only 'Could you be claimed as a dependent on someone else's 2025 tax return?', and Q4 skips it for joint filers. The gate also tests 'your spouse' and 'dual-status alien', which are not in the text."
  - key: "claimed"
    status: MATCH
    reason: "A dependent is either a qualifying child who passes Step 2 or a qualifying relative who passes Step 4."
  - key: "under_ctc_age"
    status: MATCH
    reason: "Step 3 Q3: 'Was the child under age 17 at the end of 2025?'"
  - key: "ctc_child"
    status: MISMATCH
    reason: "Step 3 Q4 asks 'Did you, or your spouse if filing a joint return, and this child have SSNs valid for employment', and 'only one spouse is required to have a valid SSN'. The restatement requires your own work-valid SSN and ignores the spouse alternative."
  - key: "odc_person"
    status: MISMATCH
    reason: "Step 5 Q1 requires 'you, and your spouse if filing a joint return' to have an SSN or ITIN. The restatement tests only your own TIN, so it allows the credit when a joint-filing spouse has none."
  - key: "ctc_per_child"
    status: MATCH
    reason: "Schedule 8812 line 5: 'Multiply line 4 by $2,200.'"
  - key: "ctc_amount"
    status: MATCH
    reason: "This is $2,200 per child counted on line 4, consistent with line 5."
  - key: "odc_per_dependent"
    status: MATCH
    reason: "Schedule 8812 line 7: 'Multiply line 6 by $500.'"
  - key: "odc_amount"
    status: MATCH
    reason: "This is $500 per other dependent counted on line 6, which excludes anyone included on line 4."
  - key: "actc_per_child"
    status: MATCH
    reason: "Schedule 8812 line 16b: 'Number of qualifying children under age 17 with the required social security number: x $1,700.'"
  - key: "actc_amount"
    status: MATCH
    reason: "This is $1,700 per child counted on line 4, consistent with line 16b ('same as the number of children you used for line 4')."
  - key: "hoh_test2"
    status: MATCH
    reason: "Test 2 covers a dependent who lived with you more than half the year, excluding one who is 'your dependent only because the person lived with you for all of 2025', or 'Your unmarried qualifying child who isn't your dependent'. The divorced-rule, multiple-support and married cases are refused."
  - key: "hoh_test1"
    status: MATCH
    reason: "Test 1 requires a parent 'whom you can claim as a dependent' and that you paid over half the cost of the parent's main home for all of 2025. Multiple support agreements are refused."
  - key: "hoh_person"
    status: MATCH
    reason: "Head of household applies if 'either Test 1 or Test 2 applies'. The home-cost condition of Test 2 is tested elsewhere."
  - key: "eic_child"
    status: MATCH
    reason: "These are the EIC Step 3 tests: relationship, age, joint return and U.S. residence for more than half the year. The tie-breaker and married child cases are refused. It inherits the missing spouse alternative from the 'younger' helper."
  - key: "eic_ssn_child"
    status: MATCH
    reason: "Worksheet A counts 'qualifying children you have who have valid SSNs', and the text says a child without a timely SSN can't be counted."
```
```
