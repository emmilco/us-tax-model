# Render comparison — dependent

The rendered English of every printed line of `Dependents — qualifying child and qualifying relative tests, per person listed` (`rendered/2025/dependent.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 7879c55766cb9faac1e511c86c28bb4e2405595f09f152bace06a02ef26b76e7 |
| lines judged | 48 |
| match / mismatch / unclear / missing | 43 / 4 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 14, 17, 18, 19, 20, 21, 41, 43, 44, 45, 46 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 17, 18, 19, 20, 21, 41, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |

## Lines

### relationship — Relationship to you
Status: **MATCH**

Model: The categories line up with the Step 1 and Step 4 relationship lists. Stepsiblings sit under sibling, which both lists include. A stepsibling's child or a grandniece is only a qualifying child descendant, so under Step 4 that person counts only as an all-year household member, as the text requires.

### age — Age at the end of 2025
Status: **MATCH**

Model: Steps 1 and 3 test age at the end of 2025.

### student — Full-time student in 2025?
Status: **MATCH**

Model: This is the Step 1 full-time student condition, defined in the instructions.

### disabled — Permanently and totally disabled?
Status: **MATCH**

Model: The instructions define the condition as 'at any time in 2025, the person can't engage in any substantial gainful activity'.

### months — Months lived with you in 2025, counting temporary absences
Status: **MATCH**

Model: It follows Exception to time lived with you. Temporary absences count as time lived with you. A qualifying child born, who died, was adopted or was placed with you counts if your home was their home more than half the time. Any other such person counts only if it was their home for the entire time.

### self_support — Provided over half of their own support?
Status: **MATCH**

Model: Step 1: 'Who didn't provide over half of their own support for 2025'.

### joint_return — Filing a joint return other than only to claim a refund?
Status: **MATCH**

Model: Step 1: 'isn't filing a joint return ... or is filing a joint return ... only to claim a refund of withheld income tax or estimated tax paid'.

### citizen — U.S. citizen, U.S. national or U.S. resident alien?
Status: **MATCH**

Model: This matches Step 3 question 2 and Step 5 question 3. It also applies the Exception to citizen test for an adopted child who lived with a U.S. citizen or national all year.

### canada_mexico — Resident of Canada or Mexico (if not a U.S. citizen, national or resident alien)?
Status: **MATCH**

Model: Step 2 question 1 and Step 4 question 2 include 'or a resident of Canada or Mexico'.

### married — Married?
Status: **UNCLEAR**

Restated: Input — Was this person married at the end of 2025 (a person legally separated under a decree of divorce or separate maintenance is not married), or is this person filing a joint return for 2025 (for example with a spouse who died during 2025)?

Model: Steps 2 and 4 ask only 'Was the child married?' and the EIC text says 'married at the end of 2025'. The given text never says that a dependent legally separated under a decree is not married; that wording appears only for the filer's own head of household status.

Ruling: representation; project retained. The question adds that a person legally separated under a decree of divorce or separate maintenance is not married, the instructions' rule for marital status (i1040gi, Filing Status: 'If you were divorced or legally separated under a decree ... you are considered unmarried'); answering yes for such a person would only refuse a case, not compute one wrongly.

### tin — SSN, ITIN or ATIN issued on or before the due date of your return?
Status: **MATCH**

Model: This matches Step 3 question 1 and Step 5 question 2: an SSN, ITIN or ATIN issued on or before the due date, including extensions, or an application made by then.

### work_ssn — SSN valid for employment issued before the due date of your return?
Status: **MATCH**

Model: Step 3 question 4 asks whether the child had an SSN 'valid for employment and issued before the due date of your 2025 return (including extensions)'.

### gross_income — Gross income for 2025
Status: **MATCH**

Model: This is the input for the Step 4 gross income test.

### supported — You provided over half of this person's support?
Status: **MATCH**

Model: Step 4: 'For whom you provided over half of the person's support in 2025'.

### other_claimant — Meets the conditions to be the qualifying child of another person?
Status: **MATCH**

Model: This is the gate for 'Qualifying child of more than one person'. The question leaves out the text's '(other than your spouse if filing jointly)', but as a refusal gate that only makes the program decline more cases.

### divorced_rule — Rule for children of divorced or separated parents applies?
Status: **MATCH**

Model: This is the gate for the Children of divorced or separated parents rule (Form 8332 or a pre-1985 decree), which is outside the tool.

### multiple_support — Claimed under a multiple support agreement?
Status: **MATCH**

Model: Multiple support agreements: 'If no one person contributed over half of the support ... but you and another person(s) provided more than half'.

### parent_home_paid — For a parent not living with you, you paid over half the cost of their main home for all o
Status: **MATCH**

Model: Test 1: 'You paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent'.

### one — One person listed
Status: **MATCH**

Model: This is a counting constant for one listed person and does not conflict with the text.

### zero — No amount for this person
Status: **MATCH**

Model: This is a zero placeholder used when a credit does not apply to the person.

### qc_relationship — A child, sibling, or a descendant of either
Status: **MATCH**

Model: It covers the Step 1 list: son, daughter, stepchild, foster child, brother, sister, stepbrother, stepsister, half brother, half sister, or a descendant of any of them.

### younger — Younger than you?
Status: **MISMATCH**

Restated: Input — Was this person younger than you?

Model: The text says 'younger than you (or your spouse if filing jointly)'. The question asks only whether the person was younger than you, so a child older than you but younger than your joint-filing spouse would fail.

Ruling: second transcription right; data fixed. The question now reads 'Was this person younger than you (or, if you file jointly, younger than you or your spouse; the person need not be younger than both of you)?' (i1040gi p. 17, Step 1, 'and younger than you (or your spouse if filing jointly)'; p501 p. 13). BUG-0047.

### us_half — Lived with you in the United States for more than half of 2025?
Status: **MATCH**

Model: It matches the EIC Step 3 residency test. It includes the United States definition, the Members of the military rule and the EIC Exception to time lived with you.

### eic_ssn — SSN valid for the EIC, issued on or before the due date of your return?
Status: **MATCH**

Model: It matches the EIC definition of an SSN, including the 'Not Valid for Employment' and 'Valid for Work Only With DHS Authorization' rules.

### qc_age — Under 19 and younger than you, under 24 a full-time student and younger than you, or perma
Status: **MATCH**

Model: It applies the Step 1 age test: under 19 and younger, under 24 as a full-time student and younger, or any age and permanently and totally disabled.

### lived_half — Lived with you for more than half of 2025
Status: **MATCH**

Model: More than 6 months is more than half of 2025, given how the months input is defined.

### qualifying_child — Qualifying child (Step 1)
Status: **MATCH**

Model: It combines the five Step 1 conditions. The tie-breaker, divorced-parent and married cases are refused.

### resident — U.S. citizen, national or resident alien, or a resident of Canada or Mexico
Status: **MATCH**

Model: Step 2 question 1: 'U.S. citizen, U.S. national, U.S. resident alien, or a resident of Canada or Mexico'.

### qc_dependent — Qualifying child who is your dependent (Step 2)
Status: **MISMATCH**

Restated: helper "Qualifying child (Step 1)" = true and helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = true and sa helper "Can someone claim you or your spouse as a dependent for 2025, or are you a dual-status alien? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)" = false

Model: The program always requires that no one can claim you. Step 2 question 3 says 'Are you filing a joint return for 2025? Yes. You can claim this child as a dependent.', so joint filers skip question 4.

Ruling: scope; project retained. On a joint return Step 2, question 3 (and Step 4, question 4) lets you claim the person without question 4 ('Could you be claimed as a dependent by another taxpayer?'). The project reads sa.dependent ('Can someone claim you or your spouse as a dependent'), and a yes refuses the standard deduction (Standard Deduction Worksheet for Dependents, i1040gi pp. 34-35) and with it line 12e and every line after it, on a joint return as on any other; so no value the tool computes rests on the skipped question (i1040gi pp. 17-19, Steps 2 and 4).

### qr_relationship — A relative listed in Step 4, or any other person who lived with you all year
Status: **MATCH**

Model: It matches the Step 4 relationship list. Anyone outside the listed relatives must have lived with you all year as a member of your household.

### qr_income — Gross income under $5,200
Status: **MATCH**

Model: Step 4: 'gross income of less than $5,200 in 2025'.

### income_exception — Permanently and totally disabled with gross income at or over the limit
Status: **MATCH**

Model: This is the gate for the Exception to gross income test: a permanently and totally disabled person whose income is at or over the limit.

### qualifying_relative — Qualifying relative (Step 4)
Status: **MISMATCH**

Restated: helper "A relative listed in Step 4, or any other person who lived with you all year" = true and helper "Qualifying child (Step 1)" = false and helper "Gross income under $5,200" = true and helper "You provided over half of this person's support?" = true

Model: Step 4 requires that the person 'wasn't a qualifying child (see Step 1) of any taxpayer for 2025'. The program checks only that the person is not your qualifying child, and has no other_claimant refusal on this line.

Ruling: refusal representation; project retained. Step 4 requires that the person 'wasn't a qualifying child (see Step 1) of any taxpayer for 2025' (i1040gi p. 19). The project asks dependent.other_claimant ('Does this person meet the conditions to be the qualifying child of any other person for 2025 ...?') and refuses dependent.qualifying_child on a yes (tie-breaker rules, p. 21); this line reads dependent.qualifying_child, so such a person is refused rather than claimed.

### qr_dependent — Qualifying relative who is your dependent (Step 4, questions 2 and 5)
Status: **MISMATCH**

Restated: helper "Qualifying relative (Step 4)" = true and helper "U.S. citizen, national or resident alien, or a resident of Canada or Mexico" = true and sa helper "Can someone claim you or your spouse as a dependent for 2025, or are you a dual-status alien? (Answer no if the person who could claim you is not required to file and does not file, or files only to claim a refund of withheld or estimated tax.)" = false

Model: The program always requires that no one can claim you. Step 4 question 4 says 'Are you filing a joint return for 2025? Yes. You can claim this person as a dependent.', so joint filers skip question 5.

Ruling: scope; project retained. On a joint return Step 2, question 3 (and Step 4, question 4) lets you claim the person without question 4 ('Could you be claimed as a dependent by another taxpayer?'). The project reads sa.dependent ('Can someone claim you or your spouse as a dependent'), and a yes refuses the standard deduction (Standard Deduction Worksheet for Dependents, i1040gi pp. 34-35) and with it line 12e and every line after it, on a joint return as on any other; so no value the tool computes rests on the skipped question (i1040gi pp. 17-19, Steps 2 and 4).

### claimed — Your dependent
Status: **MATCH**

Model: The person is a dependent through either Step 2 or Step 4.

### under_ctc_age — Under age 17 at the end of 2025
Status: **MATCH**

Model: Step 3 question 3: 'under age 17 at the end of 2025'.

### ctc_child — Qualifying child for the child tax credit (Step 3)
Status: **MATCH**

Model: It applies Step 3 questions 1 through 4. It also applies 'Before you begin': one spouse must have an SSN valid for employment and the other spouse an SSN or ITIN.

### odc_person — Dependent for the credit for other dependents (Steps 3 and 5)
Status: **MATCH**

Model: The person is a dependent with an SSN, ITIN or ATIN, is a U.S. citizen, national or resident alien, and is not a child tax credit child. You and your spouse must have an SSN or ITIN, per Step 5 and 'Before you begin'.

### ctc_per_child — Year parameter ctc.per_child
Status: **MATCH**

Model: Schedule 8812 line 5: 'Multiply line 4 by $2,200'.

### ctc_amount — Child tax credit amount for this person before limits ($2,200 for a qualifying child, else
Status: **MATCH**

Model: The amount is $2,200 per qualifying child under 17 with the required SSN, per Schedule 8812 lines 4 and 5.

### odc_per_dependent — Year parameter odc.per_dependent
Status: **MATCH**

Model: Schedule 8812 line 7: 'Multiply line 6 by $500'.

### odc_amount — Credit for other dependents amount for this person before limits ($500 for an other depend
Status: **MATCH**

Model: The amount is $500 per other dependent, per Schedule 8812 lines 6 and 7.

### actc_per_child — Year parameter actc.per_child
Status: **MATCH**

Model: Schedule 8812 line 16b: 'x $1,700'.

### actc_amount — Additional child tax credit ceiling for this person ($1,700 for a qualifying child, else 0
Status: **MATCH**

Model: The amount is $1,700 per qualifying child counted on line 4, per the line 16b tip.

### hoh_test2 — A Test 2 person who lived with you more than half the year (the home-cost condition of Tes
Status: **MATCH**

Model: It includes dependents who lived with you more than half the year, excluding those who are dependents only because they lived with you all year. It also includes your unmarried qualifying child. The divorced-parent, multiple support and married cases are refused upstream.

### hoh_test1 — Qualifies you for head of household under Test 1 through a parent who does not live with y
Status: **MATCH**

Model: Test 1: a parent you can claim as a dependent whose main home for all of 2025 you paid over half the cost of keeping up. The multiple support case is refused upstream.

### eic_child — Qualifying child for the EIC (relationship, age, not filing a joint return, lived with you
Status: **MATCH**

Model: It applies the EIC Step 3 tests: relationship, age, not filing a joint return, and lived with you in the United States more than half of 2025. The other-claimant and married-child cases are refused.

### eic_ssn_child — Qualifying child for the EIC who has a valid SSN
Status: **MATCH**

Model: Worksheet A counts 'qualifying children you have who have valid SSNs'. A child without an SSN issued on or before the due date can't be counted.

## Raw response

```yaml
```yaml
lines:
  - key: "relationship"
    status: MATCH
    reason: "The categories line up with the Step 1 and Step 4 relationship lists. Stepsiblings sit under sibling, which both lists include. A stepsibling's child or a grandniece is only a qualifying child descendant, so under Step 4 that person counts only as an all-year household member, as the text requires."
  - key: "age"
    status: MATCH
    reason: "Steps 1 and 3 test age at the end of 2025."
  - key: "student"
    status: MATCH
    reason: "This is the Step 1 full-time student condition, defined in the instructions."
  - key: "disabled"
    status: MATCH
    reason: "The instructions define the condition as 'at any time in 2025, the person can't engage in any substantial gainful activity'."
  - key: "months"
    status: MATCH
    reason: "It follows Exception to time lived with you. Temporary absences count as time lived with you. A qualifying child born, who died, was adopted or was placed with you counts if your home was their home more than half the time. Any other such person counts only if it was their home for the entire time."
  - key: "self_support"
    status: MATCH
    reason: "Step 1: 'Who didn't provide over half of their own support for 2025'."
  - key: "joint_return"
    status: MATCH
    reason: "Step 1: 'isn't filing a joint return ... or is filing a joint return ... only to claim a refund of withheld income tax or estimated tax paid'."
  - key: "citizen"
    status: MATCH
    reason: "This matches Step 3 question 2 and Step 5 question 3. It also applies the Exception to citizen test for an adopted child who lived with a U.S. citizen or national all year."
  - key: "canada_mexico"
    status: MATCH
    reason: "Step 2 question 1 and Step 4 question 2 include 'or a resident of Canada or Mexico'."
  - key: "married"
    status: UNCLEAR
    reason: "Steps 2 and 4 ask only 'Was the child married?' and the EIC text says 'married at the end of 2025'. The given text never says that a dependent legally separated under a decree is not married; that wording appears only for the filer's own head of household status."
  - key: "tin"
    status: MATCH
    reason: "This matches Step 3 question 1 and Step 5 question 2: an SSN, ITIN or ATIN issued on or before the due date, including extensions, or an application made by then."
  - key: "work_ssn"
    status: MATCH
    reason: "Step 3 question 4 asks whether the child had an SSN 'valid for employment and issued before the due date of your 2025 return (including extensions)'."
  - key: "gross_income"
    status: MATCH
    reason: "This is the input for the Step 4 gross income test."
  - key: "supported"
    status: MATCH
    reason: "Step 4: 'For whom you provided over half of the person's support in 2025'."
  - key: "other_claimant"
    status: MATCH
    reason: "This is the gate for 'Qualifying child of more than one person'. The question leaves out the text's '(other than your spouse if filing jointly)', but as a refusal gate that only makes the program decline more cases."
  - key: "divorced_rule"
    status: MATCH
    reason: "This is the gate for the Children of divorced or separated parents rule (Form 8332 or a pre-1985 decree), which is outside the tool."
  - key: "multiple_support"
    status: MATCH
    reason: "Multiple support agreements: 'If no one person contributed over half of the support ... but you and another person(s) provided more than half'."
  - key: "parent_home_paid"
    status: MATCH
    reason: "Test 1: 'You paid over half the cost of keeping up a home that was the main home for all of 2025 of your parent'."
  - key: "one"
    status: MATCH
    reason: "This is a counting constant for one listed person and does not conflict with the text."
  - key: "zero"
    status: MATCH
    reason: "This is a zero placeholder used when a credit does not apply to the person."
  - key: "qc_relationship"
    status: MATCH
    reason: "It covers the Step 1 list: son, daughter, stepchild, foster child, brother, sister, stepbrother, stepsister, half brother, half sister, or a descendant of any of them."
  - key: "younger"
    status: MISMATCH
    reason: "The text says 'younger than you (or your spouse if filing jointly)'. The question asks only whether the person was younger than you, so a child older than you but younger than your joint-filing spouse would fail."
  - key: "us_half"
    status: MATCH
    reason: "It matches the EIC Step 3 residency test. It includes the United States definition, the Members of the military rule and the EIC Exception to time lived with you."
  - key: "eic_ssn"
    status: MATCH
    reason: "It matches the EIC definition of an SSN, including the 'Not Valid for Employment' and 'Valid for Work Only With DHS Authorization' rules."
  - key: "qc_age"
    status: MATCH
    reason: "It applies the Step 1 age test: under 19 and younger, under 24 as a full-time student and younger, or any age and permanently and totally disabled."
  - key: "lived_half"
    status: MATCH
    reason: "More than 6 months is more than half of 2025, given how the months input is defined."
  - key: "qualifying_child"
    status: MATCH
    reason: "It combines the five Step 1 conditions. The tie-breaker, divorced-parent and married cases are refused."
  - key: "resident"
    status: MATCH
    reason: "Step 2 question 1: 'U.S. citizen, U.S. national, U.S. resident alien, or a resident of Canada or Mexico'."
  - key: "qc_dependent"
    status: MISMATCH
    reason: "The program always requires that no one can claim you. Step 2 question 3 says 'Are you filing a joint return for 2025? Yes. You can claim this child as a dependent.', so joint filers skip question 4."
  - key: "qr_relationship"
    status: MATCH
    reason: "It matches the Step 4 relationship list. Anyone outside the listed relatives must have lived with you all year as a member of your household."
  - key: "qr_income"
    status: MATCH
    reason: "Step 4: 'gross income of less than $5,200 in 2025'."
  - key: "income_exception"
    status: MATCH
    reason: "This is the gate for the Exception to gross income test: a permanently and totally disabled person whose income is at or over the limit."
  - key: "qualifying_relative"
    status: MISMATCH
    reason: "Step 4 requires that the person 'wasn't a qualifying child (see Step 1) of any taxpayer for 2025'. The program checks only that the person is not your qualifying child, and has no other_claimant refusal on this line."
  - key: "qr_dependent"
    status: MISMATCH
    reason: "The program always requires that no one can claim you. Step 4 question 4 says 'Are you filing a joint return for 2025? Yes. You can claim this person as a dependent.', so joint filers skip question 5."
  - key: "claimed"
    status: MATCH
    reason: "The person is a dependent through either Step 2 or Step 4."
  - key: "under_ctc_age"
    status: MATCH
    reason: "Step 3 question 3: 'under age 17 at the end of 2025'."
  - key: "ctc_child"
    status: MATCH
    reason: "It applies Step 3 questions 1 through 4. It also applies 'Before you begin': one spouse must have an SSN valid for employment and the other spouse an SSN or ITIN."
  - key: "odc_person"
    status: MATCH
    reason: "The person is a dependent with an SSN, ITIN or ATIN, is a U.S. citizen, national or resident alien, and is not a child tax credit child. You and your spouse must have an SSN or ITIN, per Step 5 and 'Before you begin'."
  - key: "ctc_per_child"
    status: MATCH
    reason: "Schedule 8812 line 5: 'Multiply line 4 by $2,200'."
  - key: "ctc_amount"
    status: MATCH
    reason: "The amount is $2,200 per qualifying child under 17 with the required SSN, per Schedule 8812 lines 4 and 5."
  - key: "odc_per_dependent"
    status: MATCH
    reason: "Schedule 8812 line 7: 'Multiply line 6 by $500'."
  - key: "odc_amount"
    status: MATCH
    reason: "The amount is $500 per other dependent, per Schedule 8812 lines 6 and 7."
  - key: "actc_per_child"
    status: MATCH
    reason: "Schedule 8812 line 16b: 'x $1,700'."
  - key: "actc_amount"
    status: MATCH
    reason: "The amount is $1,700 per qualifying child counted on line 4, per the line 16b tip."
  - key: "hoh_test2"
    status: MATCH
    reason: "It includes dependents who lived with you more than half the year, excluding those who are dependents only because they lived with you all year. It also includes your unmarried qualifying child. The divorced-parent, multiple support and married cases are refused upstream."
  - key: "hoh_test1"
    status: MATCH
    reason: "Test 1: a parent you can claim as a dependent whose main home for all of 2025 you paid over half the cost of keeping up. The multiple support case is refused upstream."
  - key: "eic_child"
    status: MATCH
    reason: "It applies the EIC Step 3 tests: relationship, age, not filing a joint return, and lived with you in the United States more than half of 2025. The other-claimant and married-child cases are refused."
  - key: "eic_ssn_child"
    status: MATCH
    reason: "Worksheet A counts 'qualifying children you have who have valid SSNs'. A child without an SSN issued on or before the due date can't be counted."
```
```
