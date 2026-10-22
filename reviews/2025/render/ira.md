# Render comparison — ira

The rendered English of every printed line of `IRA Deduction Worksheet — Schedule 1, Line 20` (`rendered/2025/ira.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | a2746e6673a2d4fcd2095a8499f330f0975255b86532f6477cef146d7bf393d0 |
| subject sha256 | 7ed94ed95355b32558ece2f6f4945c15fe8a98659bab2f180970bbe7ec2175e3 |
| lines judged | 21 |
| match / mismatch / unclear / missing | 17 / 3 / 1 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 31, 95, 96, 97, 98 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31, 95, 96, 98 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p590a | 2025 | 6, 7, 16, 35 | cited pages | be942a345a01a8f875a2a625b400d7760221e1a55a2c85dca5ab75826e6c801a | 6, 7, 35 | cbe3b3b920a64ff514424a52a467ab8efabacfe958197d1ca8aabaee71ca5a3b |
| i8606 | 2025 | 5 | cited pages | 242e712835ef634f3af8f1d0f19435b236e9c54b80921d6017c153b3e6c2aec6 | 5 | 805e59f2458d33a3fc0a1d17ebede2ecd59e18d911069bbe84987e53e297ec79 |
| f8606 | 2025 | 1, 2 | whole document | 1e2747fd38afcfefc11564f9673556808470614c153f2d34458afe98a560cb2c | - | 47a023b69eb81610f8bf73059c609131854d900f1694660f8496a7791f974233 |

## Lines

### 1a — Were you covered by a retirement plan (see Were You Covered by a Retirement Plan)?
Status: **MISMATCH**

Restated: helper "Anyone on the return made traditional IRA contributions for 2025" = true and helper "You were covered by a retirement plan (1 if Yes)" > 0 (a count)

Model: Coverage comes only from the filer's own work plan or self-employed SEP/SIMPLE. The program has no rule or refusal for the married-filing-separately case, where the instructions say 'If you weren't covered by a retirement plan but your spouse was, you are considered covered by a plan unless you lived apart from your spouse for all of 2025.'

Ruling: refusal located elsewhere; project retained. Married filing separately is refused for the whole return before the worksheet is reached: scope.ready refuses on s3.mfs (Form 1040 filing status married filing separately; i1040gi p. 14, Married Filing Separately), so the worksheet's married-filing-separately rule (i1040gi p. 97, "If you weren't covered by a retirement plan but your spouse was, you are considered covered by a plan unless you lived apart from your spouse for all of 2025") is never needed; on the statuses the tool completes, line 1a is the filer's own coverage, as the line asks.

### 1b — If married filing jointly, was your spouse covered by a retirement plan?
Status: **MATCH**

Model: This asks whether the spouse was covered by a retirement plan, read from the spouse's work plan or self-employed SEP/SIMPLE. Spouse entries exist only on a joint return, so it follows 'If married filing jointly, was your spouse covered by a retirement plan?'

### 2a — Enter the amount shown below that applies to you (your IRA)
Status: **MISMATCH**

Restated: Choose — [helper "Lines 2 through 6 are completed (traditional IRA contributions, and someone is covered by a retirement plan)" = true → helper "Line 2, your column"] [helper "Lines 2 through 6 are completed (traditional IRA contributions, and someone is covered by a retirement plan)" = false → helper "Zero"]

Model: The line 2 table always gives MFS $10,000. The worksheet says 'married filing separately and you lived apart from your spouse for all of 2025, enter $89,000', and only 'Married filing separately and you lived with your spouse at any time in 2025, enter $10,000.' The other amounts ($89,000 single/HOH, $146,000 QSS/MFJ, $246,000 for the person not covered on a joint return) match.

Ruling: refusal located elsewhere; project retained. Married filing separately is refused for the whole return before the worksheet is reached: scope.ready refuses on s3.mfs (Form 1040 filing status married filing separately; i1040gi p. 14, Married Filing Separately), so the $89,000 amount for a married filer who lived apart all year and the $10,000 amount (i1040gi p. 97, line 2) are never read; the single, head of household, qualifying surviving spouse and joint amounts agree, as the model says.

### 2b — Enter the amount shown below that applies to you (your spouse's IRA)
Status: **MATCH**

Model: The spouse column exists only on a joint return. It gets $146,000, or $246,000 if the spouse was not covered, as in 'Married filing jointly, enter $146,000 in both columns. But if you checked No on either line 1a or 1b, enter $246,000 for the person who wasn't covered.' It is completed only when lines 2 through 6 apply.

### 3 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **MATCH**

Model: This is 'Enter the amount from Form 1040 or 1040-SR, line 9.'

### 4 — Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25
Status: **MISMATCH**

Restated: Add s1 line 11, s1 line 13, s1 line 15, s1 line 16, s1 line 17, s1 line 18, s1 line 19a, and s1 line 25.

Model: The worksheet says 'Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25.' The restatement leaves out Schedule 1 lines 12, 14 and 23, and no refusal covers them.

Ruling: refusal located elsewhere; project retained (as ruled before). Schedule 1 lines 12, 14 and 23 are outside this tool: scope.schedule1 asks about "an adjustment on Schedule 1 line 12, 14 or 23" and refuses Form 1040 lines 8 and 10, so worksheet line 3 (Form 1040 line 9) refuses whenever one applies and within scope they are zero, as the line's citation says. The lines in scope (11, 13, 15 to 19a and 25) are all added. i1040gi p. 97, line 4, "Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25".

### 5 — Subtract line 4 from line 3. If married filing jointly, enter the result in both columns
Status: **MATCH**

Model: This is 'Subtract line 4 from line 3.' On a joint return the single result serves both columns.

### 6a — Is the amount on line 5 less than the amount on line 2? If yes, subtract line 5 from line 
Status: **MATCH**

Model: Line 2 minus line 5, with zero or less meaning 'No' (none deductible), follows 'Is the amount on line 5 less than the amount on line 2? ... Subtract line 5 from line 2 in each column.' It is completed only when someone is covered. It does inherit the MFS lived-apart error from line 2a.

### 6b — Is the amount on line 5 less than the amount on line 2? If yes, subtract line 5 from line 
Status: **MATCH**

Model: The spouse column of 'Subtract line 5 from line 2 in each column', with zero when line 5 is not less than line 2.

### 7a — Multiply line 6a by the percentage that applies to you, increased to a multiple of $10 and
Status: **MATCH**

Model: These all follow lines 1, 6 and 7 of the worksheet:
- No one covered: $7,000 ($8,000 if age 50 or older).
- Otherwise the applicable amount at line 6 of $10,000 or more, or $20,000 or more for MFJ/QSS ($10,000 in the column of a person not covered).
- Below that: line 6 × 70%/80% or 35%/40%, rounded up to the next $10, with a $200 minimum.
- Zero when line 6 is No.

### 7b — Multiply line 6b by the percentage that applies to you, increased to a multiple of $10 and
Status: **MATCH**

Model: The spouse column uses the same rules as 7a: the applicable amount, the $10,000/$20,000 thresholds, the percentages, the round-up to $10 and the $200 minimum, as the worksheet gives them.

### 8 — Enter the total of your (and your spouse's if filing jointly): wages, salaries, tips, etc.
Status: **MATCH**

Model: W-2 box 1 wages of both spouses plus Schedule 1 line 2a alimony. Nontaxable combat pay is refused (combat_gate), and nonqualified deferred compensation in box 1 is refused (special_gate). Within the supported cases this matches line 8.

### 9 — Enter the earned income you (and your spouse if filing jointly) received as a self-employe
Status: **UNCLEAR**

Restated: Add person.ira_se over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: The worksheet says 'Enter the earned income you (and your spouse if filing jointly) received as a self-employed individual or a partner ... If zero or less, enter -0-', applying the floor to the combined amount. The program floors each spouse separately and counts only Schedule C income. The text does not settle whether one spouse's loss nets against the other's earnings, and partnership earned income has no refusal shown here.

Ruling: owner ruling (register entry amb.2025.ira_se_floor); project retained. person.ira_se, now shown in the glossary, is each person's Schedule C profit or loss less that person's Schedule 1 lines 15 and 16 deductions, floored at zero per person (i1040gi p. 98, line 9, "Enter the earned income you (and your spouse if filing jointly) received as a self-employed individual or a partner, minus any deductions on Schedule 1, lines 15 and 16. If zero or less, enter -0-"); whether one spouse's loss nets against the other's earnings is the ambiguity the owner settled. Partnership earned income is refused before this line by the Schedule SE screen (person.se_screened, 'partnership and other self-employment income'), so only Schedule C earnings reach it.

### 10 — Add lines 8 and 9
Status: **MATCH**

Model: This is 'Add lines 8 and 9.'

### (screen) (ira.special) — Does any of these apply to you or your spouse (the IRA deduction special cases)?
Status: **MATCH**

Model: The question covers the special cases the instructions and Pub. 590-A name:
- nonqualified deferred compensation or nongovernmental section 457 plan income (W-2 box 11, box 12 code Z, 1099-MISC box 15)
- non-tuition fellowship and stipend payments not on a W-2
- repayments of qualified reservist distributions
- difficulty of care payments

### (screen) (ira.se_capital) — Is any Schedule C income on this return from a business in which your (or your spouse's) p
Status: **MATCH**

Model: This screens for the condition 'net earnings from self-employment if your personal services were a material income-producing factor'. The excluded case is refused.

### 11a — Enter traditional IRA contributions made, or that will be made by the due date of your 202
Status: **MATCH**

Model: These are the taxpayer's traditional IRA contributions for 2025 made by April 15, 2026, without rollovers, amounts deducted for 2024, trustees' fees or employer SEP/SIMPLE contributions. That follows 'Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return ... to your IRA on line 11a.'

### 11b — Enter traditional IRA contributions made, or that will be made by the due date of your 202
Status: **MATCH**

Model: The same definition applied to the spouse's entries, as in 'to your spouse's IRA on line 11b.'

### 12a — Enter the smallest of line 7a, 10, or 11a. This is the most you can deduct (your IRA)
Status: **MATCH**

Model: The smaller of line 7a and line 10, then the smaller of that and line 11a, matches 'On line 12a, enter the smallest of line 7a, 10, or 11a.' The Kay Bailey Hutchison spousal limit, traditional-plus-Roth on a joint return, and excess-contribution cases are refused.

### 12b — Enter the smallest of line 7b, 10, or 11b. This is the most you can deduct (your spouse's 
Status: **MATCH**

Model: This matches 'On line 12b, enter the smallest of line 7b, 10, or 11b' for the spouse's entries, with the same refusals.

### (screen) (ira.deduct_less) — Do you want to deduct less than the most you can deduct, treating the rest as a nondeducti
Status: **MATCH**

Model: This matches 'Or, if you want, you can deduct a smaller amount and treat the rest as a nondeductible contribution (see Form 8606).'

## Raw response

```yaml
```yaml
lines:
  - key: "1a"
    status: MISMATCH
    reason: "Coverage comes only from the filer's own work plan or self-employed SEP/SIMPLE. The program has no rule or refusal for the married-filing-separately case, where the instructions say 'If you weren't covered by a retirement plan but your spouse was, you are considered covered by a plan unless you lived apart from your spouse for all of 2025.'"
  - key: "1b"
    status: MATCH
    reason: "This asks whether the spouse was covered by a retirement plan, read from the spouse's work plan or self-employed SEP/SIMPLE. Spouse entries exist only on a joint return, so it follows 'If married filing jointly, was your spouse covered by a retirement plan?'"
  - key: "2a"
    status: MISMATCH
    reason: "The line 2 table always gives MFS $10,000. The worksheet says 'married filing separately and you lived apart from your spouse for all of 2025, enter $89,000', and only 'Married filing separately and you lived with your spouse at any time in 2025, enter $10,000.' The other amounts ($89,000 single/HOH, $146,000 QSS/MFJ, $246,000 for the person not covered on a joint return) match."
  - key: "2b"
    status: MATCH
    reason: "The spouse column exists only on a joint return. It gets $146,000, or $246,000 if the spouse was not covered, as in 'Married filing jointly, enter $146,000 in both columns. But if you checked No on either line 1a or 1b, enter $246,000 for the person who wasn't covered.' It is completed only when lines 2 through 6 apply."
  - key: "3"
    status: MATCH
    reason: "This is 'Enter the amount from Form 1040 or 1040-SR, line 9.'"
  - key: "4"
    status: MISMATCH
    reason: "The worksheet says 'Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25.' The restatement leaves out Schedule 1 lines 12, 14 and 23, and no refusal covers them."
  - key: "5"
    status: MATCH
    reason: "This is 'Subtract line 4 from line 3.' On a joint return the single result serves both columns."
  - key: "6a"
    status: MATCH
    reason: "Line 2 minus line 5, with zero or less meaning 'No' (none deductible), follows 'Is the amount on line 5 less than the amount on line 2? ... Subtract line 5 from line 2 in each column.' It is completed only when someone is covered. It does inherit the MFS lived-apart error from line 2a."
  - key: "6b"
    status: MATCH
    reason: "The spouse column of 'Subtract line 5 from line 2 in each column', with zero when line 5 is not less than line 2."
  - key: "7a"
    status: MATCH
    reason: "These all follow lines 1, 6 and 7 of the worksheet:\n- No one covered: $7,000 ($8,000 if age 50 or older).\n- Otherwise the applicable amount at line 6 of $10,000 or more, or $20,000 or more for MFJ/QSS ($10,000 in the column of a person not covered).\n- Below that: line 6 × 70%/80% or 35%/40%, rounded up to the next $10, with a $200 minimum.\n- Zero when line 6 is No."
  - key: "7b"
    status: MATCH
    reason: "The spouse column uses the same rules as 7a: the applicable amount, the $10,000/$20,000 thresholds, the percentages, the round-up to $10 and the $200 minimum, as the worksheet gives them."
  - key: "8"
    status: MATCH
    reason: "W-2 box 1 wages of both spouses plus Schedule 1 line 2a alimony. Nontaxable combat pay is refused (combat_gate), and nonqualified deferred compensation in box 1 is refused (special_gate). Within the supported cases this matches line 8."
  - key: "9"
    status: UNCLEAR
    reason: "The worksheet says 'Enter the earned income you (and your spouse if filing jointly) received as a self-employed individual or a partner ... If zero or less, enter -0-', applying the floor to the combined amount. The program floors each spouse separately and counts only Schedule C income. The text does not settle whether one spouse's loss nets against the other's earnings, and partnership earned income has no refusal shown here."
  - key: "10"
    status: MATCH
    reason: "This is 'Add lines 8 and 9.'"
  - key: "(screen) (ira.special)"
    status: MATCH
    reason: "The question covers the special cases the instructions and Pub. 590-A name:\n- nonqualified deferred compensation or nongovernmental section 457 plan income (W-2 box 11, box 12 code Z, 1099-MISC box 15)\n- non-tuition fellowship and stipend payments not on a W-2\n- repayments of qualified reservist distributions\n- difficulty of care payments"
  - key: "(screen) (ira.se_capital)"
    status: MATCH
    reason: "This screens for the condition 'net earnings from self-employment if your personal services were a material income-producing factor'. The excluded case is refused."
  - key: "11a"
    status: MATCH
    reason: "These are the taxpayer's traditional IRA contributions for 2025 made by April 15, 2026, without rollovers, amounts deducted for 2024, trustees' fees or employer SEP/SIMPLE contributions. That follows 'Enter traditional IRA contributions made, or that will be made by the due date of your 2025 return ... to your IRA on line 11a.'"
  - key: "11b"
    status: MATCH
    reason: "The same definition applied to the spouse's entries, as in 'to your spouse's IRA on line 11b.'"
  - key: "12a"
    status: MATCH
    reason: "The smaller of line 7a and line 10, then the smaller of that and line 11a, matches 'On line 12a, enter the smallest of line 7a, 10, or 11a.' The Kay Bailey Hutchison spousal limit, traditional-plus-Roth on a joint return, and excess-contribution cases are refused."
  - key: "12b"
    status: MATCH
    reason: "This matches 'On line 12b, enter the smallest of line 7b, 10, or 11b' for the spouse's entries, with the same refusals."
  - key: "(screen) (ira.deduct_less)"
    status: MATCH
    reason: "This matches 'Or, if you want, you can deduct a smaller amount and treat the rest as a nondeductible contribution (see Form 8606).'"
```
```
