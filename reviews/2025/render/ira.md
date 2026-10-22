# Render comparison — ira

The rendered English of every printed line of `IRA Deduction Worksheet — Schedule 1, Line 20` (`rendered/2025/ira.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 965407be3f9b9677b985db16c1530a00b5332dc509b6b3d70708df2f529427bb |
| subject sha256 | 7ed94ed95355b32558ece2f6f4945c15fe8a98659bab2f180970bbe7ec2175e3 |
| lines judged | 21 |
| match / mismatch / unclear / missing | 12 / 4 / 5 / 0 |
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
Status: **MATCH**

Model: Worksheet line 1a asks "Were you covered by a retirement plan?" The restatement answers Yes when your entry is marked covered. Gating on traditional contributions only matters when the worksheet itself is unused.

### 1b — If married filing jointly, was your spouse covered by a retirement plan?
Status: **MATCH**

Model: Line 1b asks "If married filing jointly, was your spouse covered by a retirement plan?" The restatement answers Yes when the spouse's entry is marked covered. A spouse entry exists only on a joint return.

### 2a — Enter the amount shown below that applies to you (your IRA)
Status: **MATCH**

Model: Line 2 is a filer-selected threshold ("Enter the amount shown below that applies to you"). It is skipped (zero) when "No" is checked on line 1a and 1b, which the lines2to6 gate reproduces.

### 2b — Enter the amount shown below that applies to you (your spouse's IRA)
Status: **MATCH**

Model: This is the spouse's column of the same threshold lookup. It is skipped when no one is covered, as the worksheet's "skip lines 2 through 6" instruction directs.

### 3 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **MATCH**

Model: The worksheet says "Enter the amount from Form 1040 or 1040-SR, line 9."

### 4 — Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25
Status: **MISMATCH**

Restated: Add s1 line 11, s1 line 13, s1 line 15, s1 line 16, s1 line 17, s1 line 18, s1 line 19a, and s1 line 25.

Model: The IRS says "Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25." The restatement omits Schedule 1 lines 12, 14 and 23.

Ruling: refusal located elsewhere; project retained. Schedule 1 lines 12, 14 and 23 are outside this tool: scope.schedule1 asks about "an adjustment on Schedule 1 line 12, 14 or 23" and refuses Form 1040 lines 8 and 10, so worksheet line 3 (Form 1040 line 9) refuses whenever one applies and within scope they are zero, as the line's citation says. The lines in scope (11, 13, 15 to 19a and 25) are all added. i1040gi p. 97, line 4, "Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25".

### 5 — Subtract line 4 from line 3. If married filing jointly, enter the result in both columns
Status: **MATCH**

Model: The worksheet says "Subtract line 4 from line 3. If married filing jointly, enter the result in both columns." One value serves both columns.

### 6a — Is the amount on line 5 less than the amount on line 2? If yes, subtract line 5 from line 
Status: **UNCLEAR**

Restated: Choose — [helper "Lines 2 through 6 are completed (traditional IRA contributions, and someone is covered by a retirement plan)" = true → helper "Line 6, your column"] [helper "Lines 2 through 6 are completed (traditional IRA contributions, and someone is covered by a retirement plan)" = false → helper "Zero"]

Model: The IRS line is computed: "Subtract line 5 from line 2 in each column," with a stop if line 5 is not less than line 2. The restatement sums a filer-supplied person.ira_line6 that is not defined, so whether it equals line 2 minus line 5 cannot be judged.

Ruling: representation; project retained (model error). person.ira_line6 is not an entered amount: it is the column's line 2 less line 5, floored at zero (zero on the No answer), defined per person on the person worksheet and compared operand by operand in the transcription log for person, where it is ruled; the restatement names it by field because it is another worksheet's line. i1040gi p. 97, line 6, "Subtract line 5 from line 2 in each column".

### 6b — Is the amount on line 5 less than the amount on line 2? If yes, subtract line 5 from line 
Status: **UNCLEAR**

Restated: Choose — [helper "Lines 2 through 6 are completed (traditional IRA contributions, and someone is covered by a retirement plan)" = true → helper "Line 6, your spouse's column"] [helper "Lines 2 through 6 are completed (traditional IRA contributions, and someone is covered by a retirement plan)" = false → helper "Zero"]

Model: Same as 6a for the spouse's column. person.ira_line6 is undefined, so the "Subtract line 5 from line 2" computation and the STOP case are not shown.

Ruling: representation; project retained (model error). As line 6a: person.ira_line6 of the spouse entry is line 2b less line 5, floored at zero, defined per person on the person worksheet and compared operand by operand in the transcription log for person, where it is ruled. i1040gi p. 97, line 6, "Subtract line 5 from line 2 in each column".

### 7a — Multiply line 6a by the percentage that applies to you, increased to a multiple of $10 and
Status: **UNCLEAR**

Restated: Choose — [helper "Anyone on the return made traditional IRA contributions for 2025" = true → helper "Line 7, your column"] [helper "Anyone on the return made traditional IRA contributions for 2025" = false → helper "Zero"]

Model: Line 7 is either $7,000/$8,000 or line 6 "multiplied by the percentage," rounded up to a multiple of $10, with a $200 minimum. The restatement sums an undefined person.ira_line7, so none of this can be checked.

Ruling: representation; project retained (model error). person.ira_line7 is not an entered amount: it is $7,000 or $8,000 when no one is covered or line 6 is at least $20,000 ($10,000 for a single filer or the column of a person not covered), zero on line 6's No, and otherwise line 6 times 35% or 40% (joint or qualifying surviving spouse, covered column) or 70% or 80%, increased to the next multiple of $10 and at least $200 (person.ira_prod, person.ira_rounded, person.ira_floor), defined per person on the person worksheet and compared operand by operand in the transcription log for person, where it is ruled. i1040gi p. 98, line 7, "If the result isn’t a multiple of $10, increase it to the next multiple of $10 ... But if it is less than $200, enter $200".

### 7b — Multiply line 6b by the percentage that applies to you, increased to a multiple of $10 and
Status: **UNCLEAR**

Restated: Choose — [helper "Anyone on the return made traditional IRA contributions for 2025" = true → helper "Line 7, your spouse's column"] [helper "Anyone on the return made traditional IRA contributions for 2025" = false → helper "Zero"]

Model: Same as 7a for the spouse's column. The percentage, rounding and $200 minimum are not shown because person.ira_line7 is undefined.

Ruling: representation; project retained (model error). As line 7a, for the spouse entry: person.ira_line7 applies the percentages, the rounding up to a multiple of $10 and the $200 minimum, defined per person on the person worksheet and compared operand by operand in the transcription log for person, where it is ruled. i1040gi p. 98, line 7, "Multiply lines 6a and 6b by the percentage below that applies to you".

### 8 — Enter the total of your (and your spouse's if filing jointly): wages, salaries, tips, etc.
Status: **MISMATCH**

Restated: Add helper "Wages, salaries, tips, etc. (box 1 of the Forms W-2 of you and your spouse)" and s1 line 2a.

Model: Line 8 also includes "Nontaxable combat pay. This amount should be reported in box 12 of Form W-2 with code Q." The restatement adds only box 1 wages and Schedule 1 line 2a. It also does not remove the nonqualified deferred compensation that item 5 says not to include on line 8, and no refusal covers that case.

Ruling: refusal located elsewhere; project retained. Nontaxable combat pay is refused: ira.combat_gate (traditional IRA contributions and s8812.combat_pay, "Did you receive any nontaxable combat pay in 2025 (it is generally shown in Form W-2, box 12, code Q)?") refuses person.ira_line11, so line 12 and Schedule 1 line 20, on every return that has it; within scope line 8 is wages and line 2a, as the line's citation says. i1040gi p. 98, line 8, "Nontaxable combat pay. This amount should be reported in box 12 of Form W-2 with code Q".

### 9 — Enter the earned income you (and your spouse if filing jointly) received as a self-employe
Status: **UNCLEAR**

Restated: Add person.ira_se over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: The refusal properly excludes income where personal services are not "a material income-producing factor." But person.ira_se is undefined, so it cannot be confirmed that it is net self-employment earnings "minus any deductions on Schedule 1, lines 15 and 16" with "If zero or less, enter -0-."

Ruling: representation; project retained. person.ira_se is defined per person in forms/2025/person.yaml: the person's Schedule C net profit or loss (person.sc_total) less that person's deductions on Schedule 1 lines 15 and 16 (person.ira_se_take), floored at zero for each person (person.ira_se_figured, the owner's reading amb.2025.ira_se_floor), and zero without a Schedule C; that is i1040gi p. 98, IRA Deduction Worksheet line 9, "Enter the earned income you (and your spouse if filing jointly) received as a self-employed individual or a partner, minus any deductions on Schedule 1, lines 15 and 16. If zero or less, enter -0-". The transcription comparison of person compares these helpers operand by operand; the render glossary does not follow a collection field into its definition (TASKS.md T-055). The new refusal (ira.se_capital_gate) is as the model reads it (p590a pp. 6–7).

### 10 — Add lines 8 and 9
Status: **MATCH**

Model: The worksheet says "Add lines 8 and 9."

### (screen) (ira.special) — Does any of these apply to you or your spouse (the IRA deduction special cases)?
Status: **MATCH**

Model: The question restates cases named in the IRS text: deferred compensation in W-2 box 11, box 12 code Z, or 1099-MISC box 15 (item 5); non-tuition fellowship and stipend payments; repayments of qualified reservist distributions (item 9); and difficulty of care payments (Pub. 590-A).

### (screen) (ira.se_capital) — Is any Schedule C income on this return from a business in which your (or your spouse's) p
Status: **MATCH**

Model: This matches the IRS condition that self-employment earnings count only "if your personal services were a material income-producing factor."

### 11a — Enter traditional IRA contributions made, or that will be made by the due date of your 202
Status: **MATCH**

Model: The worksheet says "Enter traditional IRA contributions made, or that will be made by the due date ... for 2025 to your IRA on line 11a." The restatement sums the taxpayer's contributions.

### 11b — Enter traditional IRA contributions made, or that will be made by the due date of your 202
Status: **MATCH**

Model: The spouse's traditional IRA contributions, as for "your spouse's IRA on line 11b."

### 12a — Enter the smallest of line 7a, 10, or 11a. This is the most you can deduct (your IRA)
Status: **MISMATCH**

Restated: Add person.ira_deduction over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'taxpayer', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS says "On line 12a, enter the smallest of line 7a, 10, or 11a." The restatement sums a filer-supplied person.ira_deduction instead of taking that minimum. There is also no refusal for the caution "If married filing jointly and line 10 is less than $14,000 ... stop here and use the worksheet in Pub. 590-A."

Ruling: representation; project retained (model error). person.ira_deduction is not an entered amount: it is the smallest of the person's line 7, line 10 and line 11 (person.ira_line12; zero without traditional contributions, when line 11 is zero), defined per person on the person worksheet and compared operand by operand in the transcription log for person, where it is ruled. i1040gi p. 98, line 12, "On line 12a, enter the smallest of line 7a, 10, or 11a".

### 12b — Enter the smallest of line 7b, 10, or 11b. This is the most you can deduct (your spouse's 
Status: **MISMATCH**

Restated: Add person.ira_deduction over every confirmed person entry for which helper "Whose entry is this, yours or your spouse's?" = 'spouse', within the current person when parent-bound. An unanswered roster is unknown.

Model: The IRS says "On line 12b, enter the smallest of line 7b, 10, or 11b." The restatement sums a filer-supplied person.ira_deduction rather than that minimum, and the MFJ line 10 < $14,000 stop is not refused.

Ruling: representation; project retained (model error). As line 12a, for the spouse entry: the smallest of line 7b, line 10 and line 11b (person.ira_line12), defined per person on the person worksheet and compared operand by operand in the transcription log for person, where it is ruled. i1040gi p. 98, line 12, "On line 12b, enter the smallest of line 7b, 10, or 11b".

### (screen) (ira.deduct_less) — Do you want to deduct less than the most you can deduct, treating the rest as a nondeducti
Status: **MATCH**

Model: This restates "Or, if you want, you can deduct a smaller amount and treat the rest as a nondeductible contribution (see Form 8606)."

## Raw response

```yaml
```yaml
lines:
  - key: "1a"
    status: MATCH
    reason: "Worksheet line 1a asks \"Were you covered by a retirement plan?\" The restatement answers Yes when your entry is marked covered. Gating on traditional contributions only matters when the worksheet itself is unused."
  - key: "1b"
    status: MATCH
    reason: "Line 1b asks \"If married filing jointly, was your spouse covered by a retirement plan?\" The restatement answers Yes when the spouse's entry is marked covered. A spouse entry exists only on a joint return."
  - key: "2a"
    status: MATCH
    reason: "Line 2 is a filer-selected threshold (\"Enter the amount shown below that applies to you\"). It is skipped (zero) when \"No\" is checked on line 1a and 1b, which the lines2to6 gate reproduces."
  - key: "2b"
    status: MATCH
    reason: "This is the spouse's column of the same threshold lookup. It is skipped when no one is covered, as the worksheet's \"skip lines 2 through 6\" instruction directs."
  - key: "3"
    status: MATCH
    reason: "The worksheet says \"Enter the amount from Form 1040 or 1040-SR, line 9.\""
  - key: "4"
    status: MISMATCH
    reason: "The IRS says \"Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25.\" The restatement omits Schedule 1 lines 12, 14 and 23."
  - key: "5"
    status: MATCH
    reason: "The worksheet says \"Subtract line 4 from line 3. If married filing jointly, enter the result in both columns.\" One value serves both columns."
  - key: "6a"
    status: UNCLEAR
    reason: "The IRS line is computed: \"Subtract line 5 from line 2 in each column,\" with a stop if line 5 is not less than line 2. The restatement sums a filer-supplied person.ira_line6 that is not defined, so whether it equals line 2 minus line 5 cannot be judged."
  - key: "6b"
    status: UNCLEAR
    reason: "Same as 6a for the spouse's column. person.ira_line6 is undefined, so the \"Subtract line 5 from line 2\" computation and the STOP case are not shown."
  - key: "7a"
    status: UNCLEAR
    reason: "Line 7 is either $7,000/$8,000 or line 6 \"multiplied by the percentage,\" rounded up to a multiple of $10, with a $200 minimum. The restatement sums an undefined person.ira_line7, so none of this can be checked."
  - key: "7b"
    status: UNCLEAR
    reason: "Same as 7a for the spouse's column. The percentage, rounding and $200 minimum are not shown because person.ira_line7 is undefined."
  - key: "8"
    status: MISMATCH
    reason: "Line 8 also includes \"Nontaxable combat pay. This amount should be reported in box 12 of Form W-2 with code Q.\" The restatement adds only box 1 wages and Schedule 1 line 2a. It also does not remove the nonqualified deferred compensation that item 5 says not to include on line 8, and no refusal covers that case."
  - key: "9"
    status: UNCLEAR
    reason: "The refusal properly excludes income where personal services are not \"a material income-producing factor.\" But person.ira_se is undefined, so it cannot be confirmed that it is net self-employment earnings \"minus any deductions on Schedule 1, lines 15 and 16\" with \"If zero or less, enter -0-.\""
  - key: "10"
    status: MATCH
    reason: "The worksheet says \"Add lines 8 and 9.\""
  - key: "(screen) (ira.special)"
    status: MATCH
    reason: "The question restates cases named in the IRS text: deferred compensation in W-2 box 11, box 12 code Z, or 1099-MISC box 15 (item 5); non-tuition fellowship and stipend payments; repayments of qualified reservist distributions (item 9); and difficulty of care payments (Pub. 590-A)."
  - key: "(screen) (ira.se_capital)"
    status: MATCH
    reason: "This matches the IRS condition that self-employment earnings count only \"if your personal services were a material income-producing factor.\""
  - key: "11a"
    status: MATCH
    reason: "The worksheet says \"Enter traditional IRA contributions made, or that will be made by the due date ... for 2025 to your IRA on line 11a.\" The restatement sums the taxpayer's contributions."
  - key: "11b"
    status: MATCH
    reason: "The spouse's traditional IRA contributions, as for \"your spouse's IRA on line 11b.\""
  - key: "12a"
    status: MISMATCH
    reason: "The IRS says \"On line 12a, enter the smallest of line 7a, 10, or 11a.\" The restatement sums a filer-supplied person.ira_deduction instead of taking that minimum. There is also no refusal for the caution \"If married filing jointly and line 10 is less than $14,000 ... stop here and use the worksheet in Pub. 590-A.\""
  - key: "12b"
    status: MISMATCH
    reason: "The IRS says \"On line 12b, enter the smallest of line 7b, 10, or 11b.\" The restatement sums a filer-supplied person.ira_deduction rather than that minimum, and the MFJ line 10 < $14,000 stop is not refused."
  - key: "(screen) (ira.deduct_less)"
    status: MATCH
    reason: "This restates \"Or, if you want, you can deduct a smaller amount and treat the rest as a nondeductible contribution (see Form 8606).\""
```
```
