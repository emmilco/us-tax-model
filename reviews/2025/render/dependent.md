# Render comparison — dependent

The rendered English of every printed line of `Dependents — qualifying child and qualifying relative tests, per person listed` (`rendered/2025/dependent.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 90b045dd4d809155a3c79392925477f93605684f24d540d3f68079253541d275 |
| lines judged | 45 |
| match / mismatch / unclear / missing | 37 / 8 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 |
| --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 14, 17, 18, 19, 20, 21 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 |

## Lines

### relationship — Relationship to you
Status: **MATCH**

Model: The enum covers the relatives listed in Steps 1 and 4 (child, sibling and step/half sibling, descendants, parent, ancestors or siblings of a parent, step-parents and in-laws) plus other household members. How the categories are used is judged at qr_relationship.

### age — Age at the end of 2025
Status: **MATCH**

Model: Steps 1 and 3 test age at the end of 2025.

### student — Full-time student in 2025?
Status: **MATCH**

Model: Step 1 asks whether the child was a full-time student, as defined under Full-time student.

### disabled — Permanently and totally disabled?
Status: **MATCH**

Model: The definition reads "at any time in 2025, the person can't engage in any substantial gainful activity", which matches "at any time in 2025".

### months — Months lived with you in 2025, counting temporary absences
Status: **MATCH**

Model: Exception to time lived with you counts temporary absences for school, vacation, business, medical care, military service, or detention in a juvenile facility as time lived with you.

### self_support — Provided over half of their own support?
Status: **MATCH**

Model: Step 1 reads "Who didn't provide over half of their own support for 2025."

### joint_return — Filing a joint return other than only to claim a refund?
Status: **MATCH**

Model: Step 1 reads "isn't filing a joint return for 2025 or is filing a joint return for 2025 only to claim a refund of withheld income tax or estimated tax paid."

### citizen — U.S. citizen, U.S. national or U.S. resident alien?
Status: **MATCH**

Model: Step 3 question 2 and Step 5 question 3 ask whether the person was a U.S. citizen, U.S. national, or U.S. resident alien.

### canada_mexico — Resident of Canada or Mexico (if not a U.S. citizen, national or resident alien)?
Status: **MATCH**

Model: Step 2 question 1 and Step 4 question 2 also accept "a resident of Canada or Mexico."

### married — Married?
Status: **MATCH**

Model: Step 2 question 2 and Step 4 question 3 ask "Was the child/your qualifying relative married?" The text gives no date, so "at the end of 2025" is a reasonable reading.

### tin — SSN, ITIN or ATIN issued on or before the due date of your return?
Status: **MATCH**

Model: Step 3 question 1 and Step 5 question 2 ask about an SSN, ITIN, or ATIN issued on or before the due date (including extensions). They also say to answer "Yes" if you are applying for an ITIN or ATIN by then.

### work_ssn — SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: Step 3 question 4 asks whether the child has an SSN valid for employment, issued before the due date of the 2025 return (including extensions).

### gross_income — Gross income for 2025
Status: **MATCH**

Model: Step 4 tests the person's gross income in 2025.

### supported — You provided over half of this person's support?
Status: **MATCH**

Model: Step 4 reads "For whom you provided over half of the person's support in 2025."

### other_claimant — Meets the conditions to be the qualifying child of another person?
Status: **MATCH**

Model: The Step 1 caution reads "If the child meets the conditions to be a qualifying child of any other person ... see Qualifying child of more than one person."

### divorced_rule — Rule for children of divorced or separated parents applies?
Status: **MATCH**

Model: This is an input that gates the Children of divorced or separated parents rule, which the text describes.

### multiple_support — Claimed under a multiple support agreement?
Status: **MATCH**

Model: This is an input that gates Multiple support agreements, which the text describes.

### parent_home_paid — For a parent not living with you, you paid over half the cost of their main home for all o
Status: **MATCH**

Model: Test 1 reads "You paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent ... Your parent didn't have to live with you."

### one — One person listed
Status: **MATCH**

Model: This is a per-person count of 1, which is consistent with counting each person on Schedule 8812 lines 4 and 6.

### zero — No amount for this person
Status: **MATCH**

Model: This is a constant $0, used when no credit amount applies to the person.

### qc_relationship — A child, sibling, or a descendant of either
Status: **MATCH**

Model: Step 1 lists son, daughter, stepchild, foster child, brother, sister, stepbrother, stepsister, half brother, half sister, "or a descendant of any of them."

### younger — Younger than you
Status: **MISMATCH**

Restated: helper "Age at the end of 2025" < household helper "Your age at the end of 2025"

Model: The program compares the child only with your own age. Step 1 reads "younger than you (or your spouse if filing jointly)".

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4) arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themselves alone. No change to the data.

### qc_age — Under 19 and younger than you, under 24 a full-time student and younger than you, or perma
Status: **MATCH**

Model: The line matches Step 1: under 19 and younger, under 24 and a full-time student and younger, or any age and permanently and totally disabled. It inherits the spouse omission in the younger helper.

### lived_half — Lived with you for more than half of 2025
Status: **MISMATCH**

Restated: helper "Months lived with you in 2025, counting temporary absences" > 6 (a count)

Model: Counting more than 6 whole months ignores the exception for a person born or died in 2025. The text reads "the person is considered to have lived with you for more than half of 2025 if your home was this person's home for more than half the time the person was alive in 2025." The same applies to adoption or foster placement in 2025.

Ruling: second reading right; data changed under BUG-0014. The months question now tells the filer to enter 12 for a person born, died, adopted or placed in 2025 whose home was the filer's for more than half the time alive or with them (i1040gi p. 14, Exception to time lived with you); the test itself is unchanged.

### qualifying_child — Qualifying child (Step 1)
Status: **MATCH**

Model: The line combines the Step 1 relationship, age, support, joint-return and residency tests. Refusals exclude the tie-breaker case, the divorced-parent case and the married case.

### resident — U.S. citizen, national or resident alien, or a resident of Canada or Mexico
Status: **MATCH**

Model: Step 2 question 1 and Step 4 question 2 read "U.S. citizen, U.S. national, U.S. resident alien, or a resident of Canada or Mexico."

### qc_dependent — Qualifying child who is your dependent (Step 2)
Status: **MISMATCH**

Restated: helper "Qualifying child (Step 1)" = true and helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = true and sa helper "Can someone claim you or your spouse as a dependent, or are you a dual-status alien?" = false

Model: Step 2 question 3 reads "Are you filing a joint return for 2025? Yes. You can claim this child as a dependent." The program still requires the sa answer to be false in that case. Step 2 question 4 asks only "Could you be claimed as a dependent on someone else's 2025 tax return?", but the sa helper also includes your spouse and dual-status aliens.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4) arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themselves alone. No change to the data.

### qr_relationship — A relative listed in Step 4, or any other person who lived with you all year
Status: **MISMATCH**

Restated: (helper "Relationship to you" = 'child' or helper "Relationship to you" = 'sibling' or helper "Relationship to you" = 'parent' or helper "Relationship to you" = 'parent_relative' or helper "Relationship to you" = 'in_law' or (helper "Relationship to you" = 'household_member' or helper "Relationship to you" = 'sibling_descendant' or helper "Relationship to you" = 'other') and helper "Months lived with you in 2025, counting temporary absences" = 12 (a count))

Model: The 'sibling' category includes a step sibling's son or daughter, but Step 4 lists only "Brother, sister, half brother, half sister, or a son or daughter of any of them". The line also excludes a sibling_descendant who lived with you all year, although Step 4 includes "Any other person (other than your spouse) who lived with you all year as a member of your household."

Ruling: second reading right; data changed under BUG-0015. The `sibling` value now ends at the children of a brother, sister, half brother or half sister, and any other relationship (`sibling_descendant`, `household_member`, `other`) is a Step 4 relative when the person lived with the filer all year (i1040gi p. 19, Step 4, the last bullet). The restatement in this log predates the fix.

### qr_income — Gross income under $5,200
Status: **MATCH**

Model: Step 4 reads "Who had gross income of less than $5,200 in 2025."

### income_exception — Permanently and totally disabled with gross income at or over the limit
Status: **MATCH**

Model: This gate identifies the disabled-person case covered by Exception to gross income test (sheltered workshop income), which the program refuses.

### qualifying_relative — Qualifying relative (Step 4)
Status: **MATCH**

Model: The line combines the Step 4 relationship, gross income and support tests, plus "wasn't a qualifying child ... of any taxpayer". Your own qualifying child is excluded by the line, and qualifying children of others fall under the other_claimant refusal on the qualifying_child line it depends on. Refusals cover multiple support, the gross income exception and married persons.

### qr_dependent — Qualifying relative who is your dependent (Step 4, questions 2 and 5)
Status: **MISMATCH**

Restated: helper "Qualifying relative (Step 4)" = true and helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = true and sa helper "Can someone claim you or your spouse as a dependent, or are you a dual-status alien?" = false

Model: Step 4 question 4 reads "Are you filing a joint return for 2025? Yes. You can claim this person as a dependent." The program still requires the sa answer to be false in that case. Question 5 asks only whether you could be claimed as a dependent, not about your spouse or dual-status aliens.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4) arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themselves alone. No change to the data.

### claimed — Your dependent
Status: **MATCH**

Model: A person is your dependent through either the Step 2 path or the Step 4 path.

### under_ctc_age — Under age 17 at the end of 2025
Status: **MATCH**

Model: Step 3 question 3 reads "Was the child under age 17 at the end of 2025?"

### ctc_child — Qualifying child for the child tax credit (Step 3)
Status: **MISMATCH**

Restated: helper "Qualifying child who is your dependent (Step 2)" = true and helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = true and helper "U.S. citizen, U.S. national or U.S. resident alien?" = true and helper "Under age 17 at the end of 2025" = true and helper "SSN valid for employment issued before the due date of your return?" = true and household helper "Do you have an SSN valid for employment issued before the due date of your return?" = true

Model: The program requires your own SSN valid for employment. Step 3 question 4 reads "Did you, or your spouse if filing a joint return, and this child have SSNs valid for employment". The text adds that "only one spouse is required to have a valid SSN."

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4) arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themselves alone. No change to the data.

### odc_person — Dependent for the credit for other dependents (Steps 3 and 5)
Status: **MISMATCH**

Restated: helper "Your dependent" = true and helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = true and helper "U.S. citizen, U.S. national or U.S. resident alien?" = true and helper "Qualifying child for the child tax credit (Step 3)" = false and household helper "Do you have an SSN or ITIN issued on or before the due date of your return, or have you applied for an ITIN by then?" = true

Model: The program checks only your own SSN or ITIN. The text reads "you, and your spouse if filing jointly, must have either an SSN or ITIN issued on or before the due date," and Step 5 question 1 says the same.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4) arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themselves alone. No change to the data.

### ctc_per_child — Year parameter ctc.per_child
Status: **MATCH**

Model: Schedule 8812 line 5 reads "Multiply line 4 by $2,200."

### ctc_amount — Child tax credit amount for this person before limits ($2,200 for a qualifying child, else
Status: **MATCH**

Model: The amount is $2,200 per qualifying child counted on line 4, and $0 otherwise.

### odc_per_dependent — Year parameter odc.per_dependent
Status: **MATCH**

Model: Schedule 8812 line 7 reads "Multiply line 6 by $500."

### odc_amount — Credit for other dependents amount for this person before limits ($500 for an other depend
Status: **MATCH**

Model: The amount is $500 per other dependent counted on line 6, and $0 otherwise.

### actc_per_child — Year parameter actc.per_child
Status: **MATCH**

Model: Schedule 8812 line 16b reads "Number of qualifying children under age 17 with the required social security number: x $1,700."

### actc_amount — Additional child tax credit ceiling for this person ($1,700 for a qualifying child, else 0
Status: **MATCH**

Model: The amount is $1,700 per child counted on line 16b, which is the same count as line 4, and $0 otherwise.

### hoh_test2 — A Test 2 person who lived with you more than half the year (the home-cost condition of Tes
Status: **MISMATCH**

Restated: (helper "Your dependent" = true and helper "Lived with you for more than half of 2025" = true and helper "Relationship to you" ≠ 'household_member' or helper "Qualifying child (Step 1)" = true and helper "Married?" = false and helper "Lived with you for more than half of 2025" = true)

Model: The label says the person qualifies you, but Test 2 requires "You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived". The program has no cost-of-home condition, unlike its hoh_test1.

Ruling: representation; project retained; label clarified. The home-cost condition of Test 2 is tested once on the household form (`household.test2_met`), not per person; the per-person line carries the residency and category conditions, and its label now says so. No change to the expression.

### hoh_test1 — Qualifies you for head of household under Test 1 (a parent whose main home you kept up)
Status: **MATCH**

Model: Test 1 reads "You paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent whom you can claim as a dependent, except under a multiple support agreement." The multiple support case is refused.

### hoh_person — Qualifies you for head of household (Test 1 or Test 2)
Status: **MATCH**

Model: The text reads "Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies." This per-person line combines Test 1 or Test 2.

## Raw response

```yaml
```yaml
lines:
  - key: "relationship"
    status: MATCH
    reason: "The enum covers the relatives listed in Steps 1 and 4 (child, sibling and step/half sibling, descendants, parent, ancestors or siblings of a parent, step-parents and in-laws) plus other household members. How the categories are used is judged at qr_relationship."
  - key: "age"
    status: MATCH
    reason: "Steps 1 and 3 test age at the end of 2025."
  - key: "student"
    status: MATCH
    reason: "Step 1 asks whether the child was a full-time student, as defined under Full-time student."
  - key: "disabled"
    status: MATCH
    reason: "The definition reads \"at any time in 2025, the person can't engage in any substantial gainful activity\", which matches \"at any time in 2025\"."
  - key: "months"
    status: MATCH
    reason: "Exception to time lived with you counts temporary absences for school, vacation, business, medical care, military service, or detention in a juvenile facility as time lived with you."
  - key: "self_support"
    status: MATCH
    reason: "Step 1 reads \"Who didn't provide over half of their own support for 2025.\""
  - key: "joint_return"
    status: MATCH
    reason: "Step 1 reads \"isn't filing a joint return for 2025 or is filing a joint return for 2025 only to claim a refund of withheld income tax or estimated tax paid.\""
  - key: "citizen"
    status: MATCH
    reason: "Step 3 question 2 and Step 5 question 3 ask whether the person was a U.S. citizen, U.S. national, or U.S. resident alien."
  - key: "canada_mexico"
    status: MATCH
    reason: "Step 2 question 1 and Step 4 question 2 also accept \"a resident of Canada or Mexico.\""
  - key: "married"
    status: MATCH
    reason: "Step 2 question 2 and Step 4 question 3 ask \"Was the child/your qualifying relative married?\" The text gives no date, so \"at the end of 2025\" is a reasonable reading."
  - key: "tin"
    status: MATCH
    reason: "Step 3 question 1 and Step 5 question 2 ask about an SSN, ITIN, or ATIN issued on or before the due date (including extensions). They also say to answer \"Yes\" if you are applying for an ITIN or ATIN by then."
  - key: "work_ssn"
    status: MATCH
    reason: "Step 3 question 4 asks whether the child has an SSN valid for employment, issued before the due date of the 2025 return (including extensions)."
  - key: "gross_income"
    status: MATCH
    reason: "Step 4 tests the person's gross income in 2025."
  - key: "supported"
    status: MATCH
    reason: "Step 4 reads \"For whom you provided over half of the person's support in 2025.\""
  - key: "other_claimant"
    status: MATCH
    reason: "The Step 1 caution reads \"If the child meets the conditions to be a qualifying child of any other person ... see Qualifying child of more than one person.\""
  - key: "divorced_rule"
    status: MATCH
    reason: "This is an input that gates the Children of divorced or separated parents rule, which the text describes."
  - key: "multiple_support"
    status: MATCH
    reason: "This is an input that gates Multiple support agreements, which the text describes."
  - key: "parent_home_paid"
    status: MATCH
    reason: "Test 1 reads \"You paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent ... Your parent didn't have to live with you.\""
  - key: "one"
    status: MATCH
    reason: "This is a per-person count of 1, which is consistent with counting each person on Schedule 8812 lines 4 and 6."
  - key: "zero"
    status: MATCH
    reason: "This is a constant $0, used when no credit amount applies to the person."
  - key: "qc_relationship"
    status: MATCH
    reason: "Step 1 lists son, daughter, stepchild, foster child, brother, sister, stepbrother, stepsister, half brother, half sister, \"or a descendant of any of them.\""
  - key: "younger"
    status: MISMATCH
    reason: "The program compares the child only with your own age. Step 1 reads \"younger than you (or your spouse if filing jointly)\"."
  - key: "qc_age"
    status: MATCH
    reason: "The line matches Step 1: under 19 and younger, under 24 and a full-time student and younger, or any age and permanently and totally disabled. It inherits the spouse omission in the younger helper."
  - key: "lived_half"
    status: MISMATCH
    reason: "Counting more than 6 whole months ignores the exception for a person born or died in 2025. The text reads \"the person is considered to have lived with you for more than half of 2025 if your home was this person's home for more than half the time the person was alive in 2025.\" The same applies to adoption or foster placement in 2025."
  - key: "qualifying_child"
    status: MATCH
    reason: "The line combines the Step 1 relationship, age, support, joint-return and residency tests. Refusals exclude the tie-breaker case, the divorced-parent case and the married case."
  - key: "resident"
    status: MATCH
    reason: "Step 2 question 1 and Step 4 question 2 read \"U.S. citizen, U.S. national, U.S. resident alien, or a resident of Canada or Mexico.\""
  - key: "qc_dependent"
    status: MISMATCH
    reason: "Step 2 question 3 reads \"Are you filing a joint return for 2025? Yes. You can claim this child as a dependent.\" The program still requires the sa answer to be false in that case. Step 2 question 4 asks only \"Could you be claimed as a dependent on someone else's 2025 tax return?\", but the sa helper also includes your spouse and dual-status aliens."
  - key: "qr_relationship"
    status: MISMATCH
    reason: "The 'sibling' category includes a step sibling's son or daughter, but Step 4 lists only \"Brother, sister, half brother, half sister, or a son or daughter of any of them\". The line also excludes a sibling_descendant who lived with you all year, although Step 4 includes \"Any other person (other than your spouse) who lived with you all year as a member of your household.\""
  - key: "qr_income"
    status: MATCH
    reason: "Step 4 reads \"Who had gross income of less than $5,200 in 2025.\""
  - key: "income_exception"
    status: MATCH
    reason: "This gate identifies the disabled-person case covered by Exception to gross income test (sheltered workshop income), which the program refuses."
  - key: "qualifying_relative"
    status: MATCH
    reason: "The line combines the Step 4 relationship, gross income and support tests, plus \"wasn't a qualifying child ... of any taxpayer\". Your own qualifying child is excluded by the line, and qualifying children of others fall under the other_claimant refusal on the qualifying_child line it depends on. Refusals cover multiple support, the gross income exception and married persons."
  - key: "qr_dependent"
    status: MISMATCH
    reason: "Step 4 question 4 reads \"Are you filing a joint return for 2025? Yes. You can claim this person as a dependent.\" The program still requires the sa answer to be false in that case. Question 5 asks only whether you could be claimed as a dependent, not about your spouse or dual-status aliens."
  - key: "claimed"
    status: MATCH
    reason: "A person is your dependent through either the Step 2 path or the Step 4 path."
  - key: "under_ctc_age"
    status: MATCH
    reason: "Step 3 question 3 reads \"Was the child under age 17 at the end of 2025?\""
  - key: "ctc_child"
    status: MISMATCH
    reason: "The program requires your own SSN valid for employment. Step 3 question 4 reads \"Did you, or your spouse if filing a joint return, and this child have SSNs valid for employment\". The text adds that \"only one spouse is required to have a valid SSN.\""
  - key: "odc_person"
    status: MISMATCH
    reason: "The program checks only your own SSN or ITIN. The text reads \"you, and your spouse if filing jointly, must have either an SSN or ITIN issued on or before the due date,\" and Step 5 question 1 says the same."
  - key: "ctc_per_child"
    status: MATCH
    reason: "Schedule 8812 line 5 reads \"Multiply line 4 by $2,200.\""
  - key: "ctc_amount"
    status: MATCH
    reason: "The amount is $2,200 per qualifying child counted on line 4, and $0 otherwise."
  - key: "odc_per_dependent"
    status: MATCH
    reason: "Schedule 8812 line 7 reads \"Multiply line 6 by $500.\""
  - key: "odc_amount"
    status: MATCH
    reason: "The amount is $500 per other dependent counted on line 6, and $0 otherwise."
  - key: "actc_per_child"
    status: MATCH
    reason: "Schedule 8812 line 16b reads \"Number of qualifying children under age 17 with the required social security number: x $1,700.\""
  - key: "actc_amount"
    status: MATCH
    reason: "The amount is $1,700 per child counted on line 16b, which is the same count as line 4, and $0 otherwise."
  - key: "hoh_test2"
    status: MISMATCH
    reason: "The label says the person qualifies you, but Test 2 requires \"You paid over half the cost of keeping up a home in which you lived and in which one of the following also lived\". The program has no cost-of-home condition, unlike its hoh_test1."
  - key: "hoh_test1"
    status: MATCH
    reason: "Test 1 reads \"You paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent whom you can claim as a dependent, except under a multiple support agreement.\" The multiple support case is refused."
  - key: "hoh_person"
    status: MATCH
    reason: "The text reads \"Check the 'Head of household' box only if you are unmarried (or considered unmarried) and either Test 1 or Test 2 applies.\" This per-person line combines Test 1 or Test 2."
```
```
