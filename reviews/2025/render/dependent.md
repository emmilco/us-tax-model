# Render comparison — dependent

The rendered English of every printed line of `Dependents — qualifying child and qualifying relative tests, per person listed` (`rendered/2025/dependent.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 10ac0be72265fc54d112be4cc8351af1dd67d8cc66f8f8377d646a7121a37fa5 |
| lines judged | 48 |
| match / mismatch / unclear / missing | 42 / 6 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 14, 17, 18, 19, 20, 21, 41, 43, 44, 45, 46 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 17, 18, 19, 20, 21, 41, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |

## Lines

### relationship — Relationship to you
Status: **MATCH**

Model: The categories follow the Step 1 and Step 4 lists. Stepsiblings are in 'sibling', and grandnieces or a stepsibling's child fall under Step 4 only through the all-year household rule, which is consistent with Step 4's 'son or daughter of any of them'.

### age — Age at the end of 2025
Status: **MATCH**

Model: Age at the end of 2025 is what Steps 1 and 3 test.

### student — Full-time student in 2025?
Status: **MATCH**

Model: Asks the full-time student question used in Step 1.

### disabled — Permanently and totally disabled?
Status: **MATCH**

Model: Matches 'permanently and totally disabled' at any time in 2025.

### months — Months lived with you in 2025, counting temporary absences
Status: **MATCH**

Model: Covers temporary absences and the birth/death/adoption/placement rules as stated in Exception to time lived with you. That includes 'more than half' for a qualifying child and 'entire time' for any other person.

### self_support — Provided over half of their own support?
Status: **MATCH**

Model: Matches Step 1 'didn't provide over half of their own support for 2025'.

### joint_return — Filing a joint return other than only to claim a refund?
Status: **MATCH**

Model: Matches Step 1 'isn't filing a joint return ... or is filing ... only to claim a refund'.

### citizen — U.S. citizen, U.S. national or U.S. resident alien?
Status: **MATCH**

Model: Matches the citizen/national/resident alien question and the Exception to citizen test for an adopted child who lived with a U.S. citizen or national all year.

### canada_mexico — Resident of Canada or Mexico (if not a U.S. citizen, national or resident alien)?
Status: **MATCH**

Model: Matches the 'or a resident of Canada or Mexico' alternative in Step 2 q1 and Step 4 q2.

### married — Married?
Status: **MATCH**

Model: Matches 'Was the child married?' in Step 2 and Step 4.

### tin — SSN, ITIN or ATIN issued on or before the due date of your return?
Status: **MATCH**

Model: Matches Step 3 q1 and Step 5 q2, including the answer for a pending ITIN or ATIN application.

### work_ssn — SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: Matches Step 3 q4 'SSNs valid for employment and issued before the due date of your 2025 return (including extensions)'.

### gross_income — Gross income for 2025
Status: **MATCH**

Model: Gross income for 2025 is the Step 4 test amount.

### supported — You provided over half of this person's support?
Status: **MATCH**

Model: Matches Step 4 'you provided over half of the person's support in 2025'.

### other_claimant — Meets the conditions to be the qualifying child of another person?
Status: **MATCH**

Model: Matches the caution about meeting 'the conditions to be a qualifying child of any other person'.

### divorced_rule — Rule for children of divorced or separated parents applies?
Status: **MATCH**

Model: This is a gate for the Children of divorced or separated parents rule.

### multiple_support — Claimed under a multiple support agreement?
Status: **MATCH**

Model: This is a gate for Multiple support agreements.

### parent_home_paid — For a parent not living with you, you paid over half the cost of their main home for all o
Status: **MATCH**

Model: Matches the Test 1 condition 'paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent'.

### one — One person listed
Status: **MATCH**

Model: Per-person constant of 1, consistent with Schedule 8812 lines 4 and 6 counting persons.

### zero — No amount for this person
Status: **MATCH**

Model: A $0 constant used when no credit amount applies.

### qc_relationship — A child, sibling, or a descendant of either
Status: **MATCH**

Model: Matches Step 1 'Son, daughter, stepchild, foster child, brother, sister, stepbrother, stepsister, half brother, half sister, or a descendant of any of them'.

### younger — Younger than you?
Status: **MISMATCH**

Restated: Input — Was this person younger than you?

Model: The IRS test is 'younger than you (or your spouse if filing jointly)'. The input asks only whether the person is younger than you, so on a joint return a child older than you but younger than your spouse would wrongly fail.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### us_half — Lived with you in the United States for more than half of 2025?
Status: **MATCH**

Model: Matches EIC Step 3 'lived with you in the United States for more than half of 2025', the definition of United States, and the EIC Exception to time lived with you.

### qc_age — Under 19 and younger than you, under 24 a full-time student and younger than you, or perma
Status: **MATCH**

Model: The structure matches Step 1's three age alternatives. The omission of the spouse comparison comes from the 'younger' input, which is judged separately.

### lived_half — Lived with you for more than half of 2025
Status: **MATCH**

Model: More than 6 months, with absences and exceptions already folded into the months input, equals 'lived with you for more than half of 2025'.

### qualifying_child — Qualifying child (Step 1)
Status: **MATCH**

Model: Combines Step 1's relationship, age, support, joint-return and residency tests. Refusals name the excluded multiple-claimant, divorced-parent and married cases.

### resident — U.S. citizen, national or resident alien, or a resident of Canada or Mexico
Status: **MATCH**

Model: Matches Step 2 q1 'U.S. citizen, U.S. national, U.S. resident alien, or a resident of Canada or Mexico'.

### qc_dependent — Qualifying child who is your dependent (Step 2)
Status: **MISMATCH**

Restated: helper "Qualifying child (Step 1)" = true and helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = true and sa helper "Can someone claim you or your spouse as a dependent, or are you a dual-status alien?" = false

Model: Step 2 says 'Are you filing a joint return for 2025? Yes. You can claim this child as a dependent.' Only otherwise does it ask 'Could you be claimed as a dependent on someone else's 2025 tax return?' The gate instead blocks whenever someone can claim you or your spouse, or you are a dual-status alien, and the text names no dual-status test.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### qr_relationship — A relative listed in Step 4, or any other person who lived with you all year
Status: **MATCH**

Model: Covers the Step 4 relative list, plus 'Any other person (other than your spouse) who lived with you all year as a member of your household'.

### qr_income — Gross income under $5,200
Status: **MATCH**

Model: Matches 'gross income of less than $5,200 in 2025'.

### income_exception — Permanently and totally disabled with gross income at or over the limit
Status: **MATCH**

Model: This gate identifies the case covered by the Exception to gross income test for a permanently and totally disabled person.

### qualifying_relative — Qualifying relative (Step 4)
Status: **MATCH**

Model: Combines the Step 4 relationship, not-a-qualifying-child, gross-income and support tests. Being a qualifying child of another taxpayer, multiple support, the disabled income exception and marriage are excluded by named refusals.

### qr_dependent — Qualifying relative who is your dependent (Step 4, questions 2 and 5)
Status: **MISMATCH**

Restated: helper "Qualifying relative (Step 4)" = true and helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = true and sa helper "Can someone claim you or your spouse as a dependent, or are you a dual-status alien?" = false

Model: Step 4 q4 says 'Are you filing a joint return for 2025? Yes. You can claim this person as a dependent.' Q5 asks only 'Could you be claimed as a dependent on someone else's 2025 tax return?' The gate also blocks when your spouse can be claimed or you are a dual-status alien, which the text does not say.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### claimed — Your dependent
Status: **MATCH**

Model: A dependent is a qualifying child or a qualifying relative who passes Step 2 or Step 4.

### under_ctc_age — Under age 17 at the end of 2025
Status: **MATCH**

Model: Matches Step 3 q3 'under age 17 at the end of 2025'.

### ctc_child — Qualifying child for the child tax credit (Step 3)
Status: **MISMATCH**

Restated: helper "Qualifying child who is your dependent (Step 2)" = true and helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = true and helper "U.S. citizen, U.S. national or U.S. resident alien?" = true and helper "Under age 17 at the end of 2025" = true and helper "SSN valid for employment issued before the due date of your return?" = true and household helper "Do you have an SSN valid for employment issued before the due date of your return?" = true

Model: Step 3 q4 asks 'Did you, or your spouse if filing a joint return, and this child have SSNs valid for employment', and the text adds that on a joint return 'only one spouse is required to have a valid SSN'. The restatement requires the taxpayer's own SSN and ignores the spouse's.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### odc_person — Dependent for the credit for other dependents (Steps 3 and 5)
Status: **MISMATCH**

Restated: helper "Your dependent" = true and helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = true and helper "U.S. citizen, U.S. national or U.S. resident alien?" = true and helper "Qualifying child for the child tax credit (Step 3)" = false and household helper "Do you have an SSN or ITIN issued on or before the due date of your return, or have you applied for an ITIN by then?" = true

Model: The text requires that 'you, and your spouse if filing jointly, must have either an SSN or ITIN issued on or before the due date' (Step 5 q1: 'Did you, and your spouse if filing a joint return'). The restatement checks only the taxpayer's TIN.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### ctc_per_child — Year parameter ctc.per_child
Status: **MATCH**

Model: Schedule 8812 line 5: 'Multiply line 4 by $2,200'.

### ctc_amount — Child tax credit amount for this person before limits ($2,200 for a qualifying child, else
Status: **MATCH**

Model: $2,200 per qualifying child counted on line 4, otherwise 0.

### odc_per_dependent — Year parameter odc.per_dependent
Status: **MATCH**

Model: Schedule 8812 line 7: 'Multiply line 6 by $500'.

### odc_amount — Credit for other dependents amount for this person before limits ($500 for an other depend
Status: **MATCH**

Model: $500 per other dependent counted on line 6, otherwise 0.

### actc_per_child — Year parameter actc.per_child
Status: **MATCH**

Model: Schedule 8812 line 16b: 'Number of qualifying children ... x $1,700'.

### actc_amount — Additional child tax credit ceiling for this person ($1,700 for a qualifying child, else 0
Status: **MATCH**

Model: $1,700 per line-4 qualifying child, otherwise 0, per line 16b and its TIP.

### hoh_test2 — A Test 2 person who lived with you more than half the year (the home-cost condition of Tes
Status: **MATCH**

Model: Covers Test 2 items 1 and 2. It excludes dependents only because of all-year residence, and the divorced-parent, multiple-support and married cases are refused upstream.

### hoh_test1 — Qualifies you for head of household under Test 1 through a parent who does not live with y
Status: **MATCH**

Model: Matches Test 1: a parent you can claim as a dependent whose main home you paid over half the cost of for all of 2025, with the multiple-support case refused.

### hoh_person — Qualifies you for head of household (Test 1 or Test 2)
Status: **MATCH**

Model: Matches 'either Test 1 or Test 2 applies' for this person.

### eic_child — Qualifying child for the EIC (relationship, age, not filing a joint return, lived with you
Status: **MATCH**

Model: Combines EIC Step 3's relationship, age, joint-return and U.S.-residence tests, with no support test. Refusals name the excluded multiple-claimant and married-child cases. The spouse-age issue lies in the 'younger' input.

### eic_ssn_child — Qualifying child for the EIC who has a valid SSN
Status: **MISMATCH**

Restated: helper "Qualifying child for the EIC (relationship, age, not filing a joint return, lived with you in the United States for more than half of 2025)" = true and helper "SSN valid for employment issued before the due date of your return?" = true

Model: The EIC text says 'If a child didn't have an SSN issued on or before the due date of your return (including extensions), you can't count that child'. The helper uses an SSN 'issued before the due date', which excludes an SSN issued on the due date.

Ruling: recorded in the ambiguity register (amb.2025.eic_valid_ssn); project retained pending owner review (T-028). The EIC count reuses the child tax credit question ('an SSN valid for employment, issued before the due date'); the EIC's own definition also admits a number issued on the due date itself and a card marked 'Not Valid for Employment' for a reason other than federally funded benefits.

## Raw response

```yaml
```yaml
lines:
  - key: "relationship"
    status: MATCH
    reason: "The categories follow the Step 1 and Step 4 lists. Stepsiblings are in 'sibling', and grandnieces or a stepsibling's child fall under Step 4 only through the all-year household rule, which is consistent with Step 4's 'son or daughter of any of them'."
  - key: "age"
    status: MATCH
    reason: "Age at the end of 2025 is what Steps 1 and 3 test."
  - key: "student"
    status: MATCH
    reason: "Asks the full-time student question used in Step 1."
  - key: "disabled"
    status: MATCH
    reason: "Matches 'permanently and totally disabled' at any time in 2025."
  - key: "months"
    status: MATCH
    reason: "Covers temporary absences and the birth/death/adoption/placement rules as stated in Exception to time lived with you. That includes 'more than half' for a qualifying child and 'entire time' for any other person."
  - key: "self_support"
    status: MATCH
    reason: "Matches Step 1 'didn't provide over half of their own support for 2025'."
  - key: "joint_return"
    status: MATCH
    reason: "Matches Step 1 'isn't filing a joint return ... or is filing ... only to claim a refund'."
  - key: "citizen"
    status: MATCH
    reason: "Matches the citizen/national/resident alien question and the Exception to citizen test for an adopted child who lived with a U.S. citizen or national all year."
  - key: "canada_mexico"
    status: MATCH
    reason: "Matches the 'or a resident of Canada or Mexico' alternative in Step 2 q1 and Step 4 q2."
  - key: "married"
    status: MATCH
    reason: "Matches 'Was the child married?' in Step 2 and Step 4."
  - key: "tin"
    status: MATCH
    reason: "Matches Step 3 q1 and Step 5 q2, including the answer for a pending ITIN or ATIN application."
  - key: "work_ssn"
    status: MATCH
    reason: "Matches Step 3 q4 'SSNs valid for employment and issued before the due date of your 2025 return (including extensions)'."
  - key: "gross_income"
    status: MATCH
    reason: "Gross income for 2025 is the Step 4 test amount."
  - key: "supported"
    status: MATCH
    reason: "Matches Step 4 'you provided over half of the person's support in 2025'."
  - key: "other_claimant"
    status: MATCH
    reason: "Matches the caution about meeting 'the conditions to be a qualifying child of any other person'."
  - key: "divorced_rule"
    status: MATCH
    reason: "This is a gate for the Children of divorced or separated parents rule."
  - key: "multiple_support"
    status: MATCH
    reason: "This is a gate for Multiple support agreements."
  - key: "parent_home_paid"
    status: MATCH
    reason: "Matches the Test 1 condition 'paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent'."
  - key: "one"
    status: MATCH
    reason: "Per-person constant of 1, consistent with Schedule 8812 lines 4 and 6 counting persons."
  - key: "zero"
    status: MATCH
    reason: "A $0 constant used when no credit amount applies."
  - key: "qc_relationship"
    status: MATCH
    reason: "Matches Step 1 'Son, daughter, stepchild, foster child, brother, sister, stepbrother, stepsister, half brother, half sister, or a descendant of any of them'."
  - key: "younger"
    status: MISMATCH
    reason: "The IRS test is 'younger than you (or your spouse if filing jointly)'. The input asks only whether the person is younger than you, so on a joint return a child older than you but younger than your spouse would wrongly fail."
  - key: "us_half"
    status: MATCH
    reason: "Matches EIC Step 3 'lived with you in the United States for more than half of 2025', the definition of United States, and the EIC Exception to time lived with you."
  - key: "qc_age"
    status: MATCH
    reason: "The structure matches Step 1's three age alternatives. The omission of the spouse comparison comes from the 'younger' input, which is judged separately."
  - key: "lived_half"
    status: MATCH
    reason: "More than 6 months, with absences and exceptions already folded into the months input, equals 'lived with you for more than half of 2025'."
  - key: "qualifying_child"
    status: MATCH
    reason: "Combines Step 1's relationship, age, support, joint-return and residency tests. Refusals name the excluded multiple-claimant, divorced-parent and married cases."
  - key: "resident"
    status: MATCH
    reason: "Matches Step 2 q1 'U.S. citizen, U.S. national, U.S. resident alien, or a resident of Canada or Mexico'."
  - key: "qc_dependent"
    status: MISMATCH
    reason: "Step 2 says 'Are you filing a joint return for 2025? Yes. You can claim this child as a dependent.' Only otherwise does it ask 'Could you be claimed as a dependent on someone else's 2025 tax return?' The gate instead blocks whenever someone can claim you or your spouse, or you are a dual-status alien, and the text names no dual-status test."
  - key: "qr_relationship"
    status: MATCH
    reason: "Covers the Step 4 relative list, plus 'Any other person (other than your spouse) who lived with you all year as a member of your household'."
  - key: "qr_income"
    status: MATCH
    reason: "Matches 'gross income of less than $5,200 in 2025'."
  - key: "income_exception"
    status: MATCH
    reason: "This gate identifies the case covered by the Exception to gross income test for a permanently and totally disabled person."
  - key: "qualifying_relative"
    status: MATCH
    reason: "Combines the Step 4 relationship, not-a-qualifying-child, gross-income and support tests. Being a qualifying child of another taxpayer, multiple support, the disabled income exception and marriage are excluded by named refusals."
  - key: "qr_dependent"
    status: MISMATCH
    reason: "Step 4 q4 says 'Are you filing a joint return for 2025? Yes. You can claim this person as a dependent.' Q5 asks only 'Could you be claimed as a dependent on someone else's 2025 tax return?' The gate also blocks when your spouse can be claimed or you are a dual-status alien, which the text does not say."
  - key: "claimed"
    status: MATCH
    reason: "A dependent is a qualifying child or a qualifying relative who passes Step 2 or Step 4."
  - key: "under_ctc_age"
    status: MATCH
    reason: "Matches Step 3 q3 'under age 17 at the end of 2025'."
  - key: "ctc_child"
    status: MISMATCH
    reason: "Step 3 q4 asks 'Did you, or your spouse if filing a joint return, and this child have SSNs valid for employment', and the text adds that on a joint return 'only one spouse is required to have a valid SSN'. The restatement requires the taxpayer's own SSN and ignores the spouse's."
  - key: "odc_person"
    status: MISMATCH
    reason: "The text requires that 'you, and your spouse if filing jointly, must have either an SSN or ITIN issued on or before the due date' (Step 5 q1: 'Did you, and your spouse if filing a joint return'). The restatement checks only the taxpayer's TIN."
  - key: "ctc_per_child"
    status: MATCH
    reason: "Schedule 8812 line 5: 'Multiply line 4 by $2,200'."
  - key: "ctc_amount"
    status: MATCH
    reason: "$2,200 per qualifying child counted on line 4, otherwise 0."
  - key: "odc_per_dependent"
    status: MATCH
    reason: "Schedule 8812 line 7: 'Multiply line 6 by $500'."
  - key: "odc_amount"
    status: MATCH
    reason: "$500 per other dependent counted on line 6, otherwise 0."
  - key: "actc_per_child"
    status: MATCH
    reason: "Schedule 8812 line 16b: 'Number of qualifying children ... x $1,700'."
  - key: "actc_amount"
    status: MATCH
    reason: "$1,700 per line-4 qualifying child, otherwise 0, per line 16b and its TIP."
  - key: "hoh_test2"
    status: MATCH
    reason: "Covers Test 2 items 1 and 2. It excludes dependents only because of all-year residence, and the divorced-parent, multiple-support and married cases are refused upstream."
  - key: "hoh_test1"
    status: MATCH
    reason: "Matches Test 1: a parent you can claim as a dependent whose main home you paid over half the cost of for all of 2025, with the multiple-support case refused."
  - key: "hoh_person"
    status: MATCH
    reason: "Matches 'either Test 1 or Test 2 applies' for this person."
  - key: "eic_child"
    status: MATCH
    reason: "Combines EIC Step 3's relationship, age, joint-return and U.S.-residence tests, with no support test. Refusals name the excluded multiple-claimant and married-child cases. The spouse-age issue lies in the 'younger' input."
  - key: "eic_ssn_child"
    status: MISMATCH
    reason: "The EIC text says 'If a child didn't have an SSN issued on or before the due date of your return (including extensions), you can't count that child'. The helper uses an SSN 'issued before the due date', which excludes an SSN issued on the due date."
```
```
