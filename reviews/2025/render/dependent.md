# Render comparison — dependent

The rendered English of every printed line of `Dependents — qualifying child and qualifying relative tests, per person listed` (`rendered/2025/dependent.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 4f4f9e0a59d18cb53ca49b7eb7496cb77da84067127893e2f26b55385f69c2f0 |
| lines judged | 48 |
| match / mismatch / unclear / missing | 42 / 5 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 14, 17, 18, 19, 20, 21, 41, 43, 44, 45, 46 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 17, 18, 19, 20, 21, 41, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |

## Lines

### relationship — Relationship to you
Status: **MATCH**

Model: The categories follow the Step 1 and Step 4 lists. Stepsiblings and other descendants of siblings are placed so that they qualify under Step 1, while under Step 4 a grandniece or a stepsibling's child must meet the 'lived with you all year as a member of your household' condition.

### age — Age at the end of 2025
Status: **MATCH**

Model: Age at the end of 2025 is the quantity the Step 1, Step 3 and EIC age tests use.

### student — Full-time student in 2025?
Status: **MATCH**

Model: Asks whether the person was a full-time student, which is the term defined under 'Full-time student'.

### disabled — Permanently and totally disabled?
Status: **MATCH**

Model: Follows the definition: the person is disabled 'if, at any time in 2025, the person can't engage in any substantial gainful activity...'.

### months — Months lived with you in 2025, counting temporary absences
Status: **MATCH**

Model: Temporary absences count as time lived with you. The born, died, adopted and placed rules (more than half the time for a qualifying child, the entire time for any other person) follow 'Exception to time lived with you'.

### self_support — Provided over half of their own support?
Status: **MATCH**

Model: Restates 'Who didn't provide over half of their own support for 2025'.

### joint_return — Filing a joint return other than only to claim a refund?
Status: **MATCH**

Model: Restates 'isn't filing a joint return for 2025 or is filing a joint return for 2025 only to claim a refund of withheld income tax or estimated tax paid'.

### citizen — U.S. citizen, U.S. national or U.S. resident alien?
Status: **MATCH**

Model: Asks the citizen, national or resident alien question and builds in the 'Exception to citizen test' for an adopted child who lived with a citizen or national all year.

### canada_mexico — Resident of Canada or Mexico (if not a U.S. citizen, national or resident alien)?
Status: **MATCH**

Model: Supplies the 'or a resident of Canada or Mexico' alternative from Step 2, question 1 and Step 4, question 2.

### married — Married?
Status: **UNCLEAR**

Restated: Input — Was this person married at the end of 2025 (a person legally separated under a decree of divorce or separate maintenance is not married), or is this person filing a joint return for 2025 (for example with a spouse who died during 2025)?

Model: The text only asks 'Was the child married?' and refers to 'Married person'. It does not say that a person legally separated under a decree counts as unmarried for this purpose; that rule appears only for your own head of household status.

Ruling: representation; project retained. The question adds that a person legally separated under a decree of divorce or separate maintenance is not married, the instructions' rule for marital status (i1040gi, Filing Status: 'If you were divorced or legally separated under a decree ... you are considered unmarried'); answering yes for such a person would only refuse a case, not compute one wrongly.

### tin — SSN, ITIN or ATIN issued on or before the due date of your return?
Status: **MATCH**

Model: Restates Step 3, question 1 and Step 5, question 2: an SSN, ITIN or ATIN issued on or before the due date, or applied for by then.

### work_ssn — SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: Restates the child's part of Step 3, question 4: 'SSNs valid for employment and issued before the due date of your 2025 return (including extensions)'.

### gross_income — Gross income for 2025
Status: **MATCH**

Model: This is the gross income amount used in the Step 4 gross income test.

### supported — You provided over half of this person's support?
Status: **MATCH**

Model: Restates 'For whom you provided over half of the person's support in 2025'.

### other_claimant — Meets the conditions to be the qualifying child of another person?
Status: **MATCH**

Model: Serves as a refusal gate for 'Qualifying child of more than one person'. It omits 'other than your spouse if filing jointly', but that only makes the refusal broader, which narrows the cases the program handles.

### divorced_rule — Rule for children of divorced or separated parents applies?
Status: **MATCH**

Model: Serves as a refusal gate for the 'Children of divorced or separated parents' rule, including parents who lived apart 'whether or not they are or were married'.

### multiple_support — Claimed under a multiple support agreement?
Status: **MATCH**

Model: Restates 'If no one person contributed over half of the support ... but you and another person(s) provided more than half', and is used only as a refusal gate.

### parent_home_paid — For a parent not living with you, you paid over half the cost of their main home for all o
Status: **MATCH**

Model: Restates Test 1: 'You paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent'.

### one — One person listed
Status: **MATCH**

Model: Program constant counting one listed person. It has no IRS line and does not conflict with the text.

### zero — No amount for this person
Status: **MATCH**

Model: Program constant used as the zero branch of the credit choices. It does not conflict with the text.

### qc_relationship — A child, sibling, or a descendant of either
Status: **MATCH**

Model: Together, child, sibling and sibling_descendant cover 'Son, daughter, stepchild, foster child, brother, sister, stepbrother, stepsister, half brother, half sister, or a descendant of any of them'.

### younger — Younger than you?
Status: **MISMATCH**

Restated: Input — Was this person younger than you?

Model: The text says 'younger than you (or your spouse if filing jointly)'. The input asks only whether the person was younger than you, so on a joint return a person younger only than your spouse would fail the test.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### us_half — Lived with you in the United States for more than half of 2025?
Status: **MATCH**

Model: Covers the EIC test 'Who lived with you in the United States for more than half of 2025'. It also covers the 'United States' definition, the 'Members of the military' rule and the EIC 'Exception to time lived with you'.

### eic_ssn — SSN valid for the EIC, issued on or before the due date of your return?
Status: **MATCH**

Model: Restates the EIC 'Social security number (SSN)' definition, including the 'Not Valid for Employment' and 'Valid for Work Only With DHS Authorization' rules, with the issued-by-the-due-date requirement.

### qc_age — Under 19 and younger than you, under 24 a full-time student and younger than you, or perma
Status: **MATCH**

Model: Gives the three alternatives as stated: under 19 and younger, under 24 and a full-time student and younger, or any age and permanently and totally disabled. The spouse omission is reported under 'younger'.

### lived_half — Lived with you for more than half of 2025
Status: **MATCH**

Model: Because the months input is entered as 7 or more for more than half the year, more than 6 months equals 'lived with you for more than half of 2025'.

### qualifying_child — Qualifying child (Step 1)
Status: **MATCH**

Model: Combines the five Step 1 conditions (relationship, age, support, joint return, residency). The tie-breaker, divorced-parent and married-person cases are refused.

### resident — U.S. citizen, national or resident alien, or a resident of Canada or Mexico
Status: **MATCH**

Model: Restates Step 2, question 1: 'U.S. citizen, U.S. national, U.S. resident alien, or a resident of Canada or Mexico'.

### qc_dependent — Qualifying child who is your dependent (Step 2)
Status: **MISMATCH**

Restated: helper "Qualifying child (Step 1)" = true and helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = true and sa helper "Can someone claim you or your spouse as a dependent for 2025, or are you a dual-status alien? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)" = false

Model: Step 2, question 3 says 'Are you filing a joint return for 2025? Yes. You can claim this child as a dependent', which skips question 4. The restatement requires the dependency answer to be no even on a joint return. It also adds 'dual-status alien', which question 4 does not contain.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### qr_relationship — A relative listed in Step 4, or any other person who lived with you all year
Status: **MATCH**

Model: Covers the listed Step 4 relatives. A grandniece, a stepsibling's child or any other person counts only if the person 'lived with you all year as a member of your household', which the program treats as 12 months.

### qr_income — Gross income under $5,200
Status: **MATCH**

Model: Restates 'Who had gross income of less than $5,200 in 2025'.

### income_exception — Permanently and totally disabled with gross income at or over the limit
Status: **MATCH**

Model: Serves as a refusal gate for 'Exception to gross income test' when the person is disabled and gross income is at or over the limit.

### qualifying_relative — Qualifying relative (Step 4)
Status: **MATCH**

Model: Combines relationship, not a qualifying child, gross income under $5,200 and over-half support. The text's 'wasn't a qualifying child ... of any taxpayer' is covered only through the Step 1 tie-breaker refusal. Multiple support, the gross income exception and married persons are refused.

### qr_dependent — Qualifying relative who is your dependent (Step 4, questions 2 and 5)
Status: **MISMATCH**

Restated: helper "Qualifying relative (Step 4)" = true and helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = true and sa helper "Can someone claim you or your spouse as a dependent for 2025, or are you a dual-status alien? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)" = false

Model: Step 4, question 4 says 'Are you filing a joint return for 2025? Yes. You can claim this person as a dependent', which skips question 5. The restatement requires the dependency answer to be no even on a joint return, and adds 'dual-status alien', which the text does not mention.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### claimed — Your dependent
Status: **MATCH**

Model: The person is your dependent through either Step 2 (qualifying child) or Step 4 (qualifying relative).

### under_ctc_age — Under age 17 at the end of 2025
Status: **MATCH**

Model: Restates Step 3, question 3: 'Was the child under age 17 at the end of 2025?'

### ctc_child — Qualifying child for the child tax credit (Step 3)
Status: **MISMATCH**

Restated: helper "Qualifying child who is your dependent (Step 2)" = true and helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = true and helper "U.S. citizen, U.S. national or U.S. resident alien?" = true and helper "Under age 17 at the end of 2025" = true and helper "SSN valid for employment issued before the due date of your return?" = true and household helper "Do you have an SSN valid for employment issued before the due date of your return?" = true

Model: Step 3, question 4 asks 'Did you, or your spouse if filing a joint return, and this child have SSNs valid for employment'. The restatement tests only your own SSN, so on a joint return where only your spouse holds the valid SSN the child would fail.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### odc_person — Dependent for the credit for other dependents (Steps 3 and 5)
Status: **MISMATCH**

Restated: helper "Your dependent" = true and helper "SSN, ITIN or ATIN issued on or before the due date of your return?" = true and helper "U.S. citizen, U.S. national or U.S. resident alien?" = true and helper "Qualifying child for the child tax credit (Step 3)" = false and household helper "Do you have an SSN or ITIN issued on or before the due date of your return, or have you applied for an ITIN by then?" = true

Model: Step 5, question 1 and 'Before you begin' require that 'you, and your spouse if filing jointly, must have either an SSN or ITIN'. The restatement checks only your own number and omits the spouse.

Ruling: scope; project retained. The spouse variants ("or your spouse if filing jointly"; "only one spouse is required to have a valid SSN"; the joint-return branches of Steps 2 and 4; "other than your spouse if filing jointly" in the tie-breaker caution; "younger than you (or your spouse if filing jointly)") arise only on a joint return, and married filing statuses are refused (`s3.married`). The `sa.dependent` gate also names a dual-status alien, which the instructions refuse for the dependents section too (i1040gi p. 18, Step 2, question 4, and the nonresident and dual-status alien rules); a single filer answers for themself alone. No change to the data.

### ctc_per_child — Year parameter ctc.per_child
Status: **MATCH**

Model: Uses $2,200, matching Schedule 8812 line 5: 'Multiply line 4 by $2,200'.

### ctc_amount — Child tax credit amount for this person before limits ($2,200 for a qualifying child, else
Status: **MATCH**

Model: Gives $2,200 per child who qualifies under Step 3 and $0 otherwise, consistent with Schedule 8812 lines 4–5.

### odc_per_dependent — Year parameter odc.per_dependent
Status: **MATCH**

Model: Uses $500, matching Schedule 8812 line 7: 'Multiply line 6 by $500'.

### odc_amount — Credit for other dependents amount for this person before limits ($500 for an other depend
Status: **MATCH**

Model: Gives $500 per other dependent and $0 otherwise, consistent with Schedule 8812 lines 6–7.

### actc_per_child — Year parameter actc.per_child
Status: **MATCH**

Model: Uses $1,700, matching Schedule 8812 line 16b: 'Number of qualifying children ... x $1,700'.

### actc_amount — Additional child tax credit ceiling for this person ($1,700 for a qualifying child, else 0
Status: **MATCH**

Model: Gives $1,700 per CTC child and $0 otherwise, consistent with line 16b using 'the same as the number of children you used for line 4'.

### hoh_test2 — A Test 2 person who lived with you more than half the year (the home-cost condition of Tes
Status: **MATCH**

Model: Includes your dependents but leaves out those who are dependents 'only because the person lived with you for all of 2025', and adds an 'unmarried qualifying child who isn't your dependent', with residence for more than half the year. The divorced-parent and multiple-support exclusions and the married qualifying child case are refused elsewhere.

### hoh_test1 — Qualifies you for head of household under Test 1 through a parent who does not live with y
Status: **MATCH**

Model: Restates Test 1: a parent 'whom you can claim as a dependent' whose main home you paid over half the cost of for all of 2025. The multiple support case is refused.

### eic_child — Qualifying child for the EIC (relationship, age, not filing a joint return, lived with you
Status: **MATCH**

Model: Combines the EIC Step 3 relationship, age, joint return and 'lived with you in the United States for more than half of 2025' tests, which have no support test. The tie-breaker and 'Married child' cases are refused.

### eic_ssn_child — Qualifying child for the EIC who has a valid SSN
Status: **MATCH**

Model: Applies 'If a child didn't have an SSN issued on or before the due date ... you can't count that child as a qualifying child in figuring the amount of the EIC'.

## Raw response

```yaml
```yaml
lines:
  - key: "relationship"
    status: MATCH
    reason: "The categories follow the Step 1 and Step 4 lists. Stepsiblings and other descendants of siblings are placed so that they qualify under Step 1, while under Step 4 a grandniece or a stepsibling's child must meet the 'lived with you all year as a member of your household' condition."
  - key: "age"
    status: MATCH
    reason: "Age at the end of 2025 is the quantity the Step 1, Step 3 and EIC age tests use."
  - key: "student"
    status: MATCH
    reason: "Asks whether the person was a full-time student, which is the term defined under 'Full-time student'."
  - key: "disabled"
    status: MATCH
    reason: "Follows the definition: the person is disabled 'if, at any time in 2025, the person can't engage in any substantial gainful activity...'."
  - key: "months"
    status: MATCH
    reason: "Temporary absences count as time lived with you. The born, died, adopted and placed rules (more than half the time for a qualifying child, the entire time for any other person) follow 'Exception to time lived with you'."
  - key: "self_support"
    status: MATCH
    reason: "Restates 'Who didn't provide over half of their own support for 2025'."
  - key: "joint_return"
    status: MATCH
    reason: "Restates 'isn't filing a joint return for 2025 or is filing a joint return for 2025 only to claim a refund of withheld income tax or estimated tax paid'."
  - key: "citizen"
    status: MATCH
    reason: "Asks the citizen, national or resident alien question and builds in the 'Exception to citizen test' for an adopted child who lived with a citizen or national all year."
  - key: "canada_mexico"
    status: MATCH
    reason: "Supplies the 'or a resident of Canada or Mexico' alternative from Step 2, question 1 and Step 4, question 2."
  - key: "married"
    status: UNCLEAR
    reason: "The text only asks 'Was the child married?' and refers to 'Married person'. It does not say that a person legally separated under a decree counts as unmarried for this purpose; that rule appears only for your own head of household status."
  - key: "tin"
    status: MATCH
    reason: "Restates Step 3, question 1 and Step 5, question 2: an SSN, ITIN or ATIN issued on or before the due date, or applied for by then."
  - key: "work_ssn"
    status: MATCH
    reason: "Restates the child's part of Step 3, question 4: 'SSNs valid for employment and issued before the due date of your 2025 return (including extensions)'."
  - key: "gross_income"
    status: MATCH
    reason: "This is the gross income amount used in the Step 4 gross income test."
  - key: "supported"
    status: MATCH
    reason: "Restates 'For whom you provided over half of the person's support in 2025'."
  - key: "other_claimant"
    status: MATCH
    reason: "Serves as a refusal gate for 'Qualifying child of more than one person'. It omits 'other than your spouse if filing jointly', but that only makes the refusal broader, which narrows the cases the program handles."
  - key: "divorced_rule"
    status: MATCH
    reason: "Serves as a refusal gate for the 'Children of divorced or separated parents' rule, including parents who lived apart 'whether or not they are or were married'."
  - key: "multiple_support"
    status: MATCH
    reason: "Restates 'If no one person contributed over half of the support ... but you and another person(s) provided more than half', and is used only as a refusal gate."
  - key: "parent_home_paid"
    status: MATCH
    reason: "Restates Test 1: 'You paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent'."
  - key: "one"
    status: MATCH
    reason: "Program constant counting one listed person. It has no IRS line and does not conflict with the text."
  - key: "zero"
    status: MATCH
    reason: "Program constant used as the zero branch of the credit choices. It does not conflict with the text."
  - key: "qc_relationship"
    status: MATCH
    reason: "Together, child, sibling and sibling_descendant cover 'Son, daughter, stepchild, foster child, brother, sister, stepbrother, stepsister, half brother, half sister, or a descendant of any of them'."
  - key: "younger"
    status: MISMATCH
    reason: "The text says 'younger than you (or your spouse if filing jointly)'. The input asks only whether the person was younger than you, so on a joint return a person younger only than your spouse would fail the test."
  - key: "us_half"
    status: MATCH
    reason: "Covers the EIC test 'Who lived with you in the United States for more than half of 2025'. It also covers the 'United States' definition, the 'Members of the military' rule and the EIC 'Exception to time lived with you'."
  - key: "eic_ssn"
    status: MATCH
    reason: "Restates the EIC 'Social security number (SSN)' definition, including the 'Not Valid for Employment' and 'Valid for Work Only With DHS Authorization' rules, with the issued-by-the-due-date requirement."
  - key: "qc_age"
    status: MATCH
    reason: "Gives the three alternatives as stated: under 19 and younger, under 24 and a full-time student and younger, or any age and permanently and totally disabled. The spouse omission is reported under 'younger'."
  - key: "lived_half"
    status: MATCH
    reason: "Because the months input is entered as 7 or more for more than half the year, more than 6 months equals 'lived with you for more than half of 2025'."
  - key: "qualifying_child"
    status: MATCH
    reason: "Combines the five Step 1 conditions (relationship, age, support, joint return, residency). The tie-breaker, divorced-parent and married-person cases are refused."
  - key: "resident"
    status: MATCH
    reason: "Restates Step 2, question 1: 'U.S. citizen, U.S. national, U.S. resident alien, or a resident of Canada or Mexico'."
  - key: "qc_dependent"
    status: MISMATCH
    reason: "Step 2, question 3 says 'Are you filing a joint return for 2025? Yes. You can claim this child as a dependent', which skips question 4. The restatement requires the dependency answer to be no even on a joint return. It also adds 'dual-status alien', which question 4 does not contain."
  - key: "qr_relationship"
    status: MATCH
    reason: "Covers the listed Step 4 relatives. A grandniece, a stepsibling's child or any other person counts only if the person 'lived with you all year as a member of your household', which the program treats as 12 months."
  - key: "qr_income"
    status: MATCH
    reason: "Restates 'Who had gross income of less than $5,200 in 2025'."
  - key: "income_exception"
    status: MATCH
    reason: "Serves as a refusal gate for 'Exception to gross income test' when the person is disabled and gross income is at or over the limit."
  - key: "qualifying_relative"
    status: MATCH
    reason: "Combines relationship, not a qualifying child, gross income under $5,200 and over-half support. The text's 'wasn't a qualifying child ... of any taxpayer' is covered only through the Step 1 tie-breaker refusal. Multiple support, the gross income exception and married persons are refused."
  - key: "qr_dependent"
    status: MISMATCH
    reason: "Step 4, question 4 says 'Are you filing a joint return for 2025? Yes. You can claim this person as a dependent', which skips question 5. The restatement requires the dependency answer to be no even on a joint return, and adds 'dual-status alien', which the text does not mention."
  - key: "claimed"
    status: MATCH
    reason: "The person is your dependent through either Step 2 (qualifying child) or Step 4 (qualifying relative)."
  - key: "under_ctc_age"
    status: MATCH
    reason: "Restates Step 3, question 3: 'Was the child under age 17 at the end of 2025?'"
  - key: "ctc_child"
    status: MISMATCH
    reason: "Step 3, question 4 asks 'Did you, or your spouse if filing a joint return, and this child have SSNs valid for employment'. The restatement tests only your own SSN, so on a joint return where only your spouse holds the valid SSN the child would fail."
  - key: "odc_person"
    status: MISMATCH
    reason: "Step 5, question 1 and 'Before you begin' require that 'you, and your spouse if filing jointly, must have either an SSN or ITIN'. The restatement checks only your own number and omits the spouse."
  - key: "ctc_per_child"
    status: MATCH
    reason: "Uses $2,200, matching Schedule 8812 line 5: 'Multiply line 4 by $2,200'."
  - key: "ctc_amount"
    status: MATCH
    reason: "Gives $2,200 per child who qualifies under Step 3 and $0 otherwise, consistent with Schedule 8812 lines 4–5."
  - key: "odc_per_dependent"
    status: MATCH
    reason: "Uses $500, matching Schedule 8812 line 7: 'Multiply line 6 by $500'."
  - key: "odc_amount"
    status: MATCH
    reason: "Gives $500 per other dependent and $0 otherwise, consistent with Schedule 8812 lines 6–7."
  - key: "actc_per_child"
    status: MATCH
    reason: "Uses $1,700, matching Schedule 8812 line 16b: 'Number of qualifying children ... x $1,700'."
  - key: "actc_amount"
    status: MATCH
    reason: "Gives $1,700 per CTC child and $0 otherwise, consistent with line 16b using 'the same as the number of children you used for line 4'."
  - key: "hoh_test2"
    status: MATCH
    reason: "Includes your dependents but leaves out those who are dependents 'only because the person lived with you for all of 2025', and adds an 'unmarried qualifying child who isn't your dependent', with residence for more than half the year. The divorced-parent and multiple-support exclusions and the married qualifying child case are refused elsewhere."
  - key: "hoh_test1"
    status: MATCH
    reason: "Restates Test 1: a parent 'whom you can claim as a dependent' whose main home you paid over half the cost of for all of 2025. The multiple support case is refused."
  - key: "eic_child"
    status: MATCH
    reason: "Combines the EIC Step 3 relationship, age, joint return and 'lived with you in the United States for more than half of 2025' tests, which have no support test. The tie-breaker and 'Married child' cases are refused."
  - key: "eic_ssn_child"
    status: MATCH
    reason: "Applies 'If a child didn't have an SSN issued on or before the due date ... you can't count that child as a qualifying child in figuring the amount of the EIC'."
```
```
