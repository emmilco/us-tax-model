# Render comparison — ira

The rendered English of every printed line of `IRA Deduction Worksheet — Schedule 1, Line 20` (`rendered/2025/ira.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | a2746e6673a2d4fcd2095a8499f330f0975255b86532f6477cef146d7bf393d0 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 7ed94ed95355b32558ece2f6f4945c15fe8a98659bab2f180970bbe7ec2175e3 |
| lines judged | 21 |
| match / mismatch / unclear / missing | 16 / 5 / 0 / 0 |
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

Model: IRS says if you weren't covered but your spouse was, you are considered covered unless you lived apart for all of 2025; cov_you counts only actual work or self-employed plan coverage, so the deemed-coverage case is omitted.

Ruling: open

### 1b — If married filing jointly, was your spouse covered by a retirement plan?
Status: **MATCH**

Model: On a joint return the restatement tests spouse retirement-plan coverage, which matches line 1b's spouse-covered question.

### 2a — Enter the amount shown below that applies to you (your IRA)
Status: **MISMATCH**

Restated: Choose — [helper "Lines 2 through 6 are completed (traditional IRA contributions, and someone is covered by a retirement plan)" = true → helper "Line 2, your column"] [helper "Lines 2 through 6 are completed (traditional IRA contributions, and someone is covered by a retirement plan)" = false → helper "Zero"]

Model: IRS line 2 says married filing separately and lived apart from your spouse for all of 2025 enter $89,000; the line 2 helper maps every MFS return to $10,000.

Ruling: open

### 2b — Enter the amount shown below that applies to you (your spouse's IRA)
Status: **MISMATCH**

Restated: Choose — [helper "Lines 2 through 6 are completed (traditional IRA contributions, and someone is covered by a retirement plan)" = true → helper "Line 2, your spouse's column"] [helper "Lines 2 through 6 are completed (traditional IRA contributions, and someone is covered by a retirement plan)" = false → helper "Zero"]

Model: IRS line 2 says married filing separately and lived apart from your spouse for all of 2025 enter $89,000; the line 2 helper maps every MFS return to $10,000.

Ruling: open

### 3 — Enter the amount from Form 1040 or 1040-SR, line 9
Status: **MATCH**

Model: Enters the amount from Form 1040 line 9, as line 3 instructs.

### 4 — Enter the total of the amounts from Schedule 1, lines 11 through 19a, plus 23 and 25
Status: **MISMATCH**

Restated: Add s1 line 11, s1 line 13, s1 line 15, s1 line 16, s1 line 17, s1 line 18, s1 line 19a, and s1 line 25.

Model: IRS line 4 is the total of Schedule 1 'lines 11 through 19a, plus 23 and 25'; the restatement omits lines 12, 14, and 23 and lists only selected lines.

Ruling: open

### 5 — Subtract line 4 from line 3. If married filing jointly, enter the result in both columns
Status: **MATCH**

Model: Subtracts line 4 from line 3, matching line 5; the same result applies to both joint columns.

### 6a — Is the amount on line 5 less than the amount on line 2? If yes, subtract line 5 from line 
Status: **MATCH**

Model: When lines 2 through 6 apply, it subtracts line 5 from the line 2 taxpayer column and floors at zero, matching line 6's Yes/No result; otherwise it uses zero.

### 6b — Is the amount on line 5 less than the amount on line 2? If yes, subtract line 5 from line 
Status: **MATCH**

Model: When lines 2 through 6 apply, it subtracts line 5 from the line 2 spouse column and floors at zero, matching line 6's Yes/No result; otherwise it uses zero.

### 7a — Multiply line 6a by the percentage that applies to you, increased to a multiple of $10 and
Status: **MATCH**

Model: Uses the line 7 threshold, applicable amount, percentage, rounding up to the next $10, and $200 floor for the taxpayer column.

### 7b — Multiply line 6b by the percentage that applies to you, increased to a multiple of $10 and
Status: **MATCH**

Model: Uses the line 7 threshold, applicable amount, percentage, rounding up to the next $10, and $200 floor for the spouse column.

### 8 — Enter the total of your (and your spouse's if filing jointly): wages, salaries, tips, etc.
Status: **MATCH**

Model: Adds W-2 box 1 wages and Schedule 1 line 2a; nontaxable combat pay, which the IRS also includes, is excluded by the ira.combat_gate refusal.

### 9 — Enter the earned income you (and your spouse if filing jointly) received as a self-employe
Status: **MISMATCH**

Restated: Add person.ira_se over every confirmed person entry, within the current person when parent-bound. An unanswered roster is unknown.

Model: IRS line 9 includes earned income received 'as a self-employed individual or a partner'; person.ira_se is zero without a Schedule C, so partner or other self-employment income not on Schedule C is omitted, and the stated refusal covers only Schedule C income not from personal services.

Ruling: open

### 10 — Add lines 8 and 9
Status: **MATCH**

Model: Adds line 8 and line 9, as line 10 instructs.

### (screen) (ira.special) — Does any of these apply to you or your spouse (the IRA deduction special cases)?
Status: **MATCH**

Model: The screen lists the nonqualified deferred compensation/457, fellowship or stipend, qualified reservist repayment, and difficulty-of-care special cases reflected in the line 20 instructions.

### (screen) (ira.se_capital) — Is any Schedule C income on this return from a business in which your (or your spouse's) p
Status: **MATCH**

Model: Asks whether Schedule C income is from a business where personal services are not a material income-producing factor, matching the line 9 rule.

### 11a — Enter traditional IRA contributions made, or that will be made by the due date of your 202
Status: **MATCH**

Model: Sums the taxpayer's traditional IRA contributions for 2025, excluding rollovers and other noncontributions as the line 20 instructions require.

### 11b — Enter traditional IRA contributions made, or that will be made by the due date of your 202
Status: **MATCH**

Model: Sums the spouse's traditional IRA contributions for 2025, excluding rollovers and other noncontributions as the line 20 instructions require.

### 12a — Enter the smallest of line 7a, 10, or 11a. This is the most you can deduct (your IRA)
Status: **MATCH**

Model: Computes the smallest of line 7a, line 10, and line 11a for the taxpayer's column, as line 12a instructs, with refusals narrowing unsupported cases.

### 12b — Enter the smallest of line 7b, 10, or 11b. This is the most you can deduct (your spouse's 
Status: **MATCH**

Model: Computes the smallest of line 7b, line 10, and line 11b for the spouse's column, as line 12b instructs, with refusals narrowing unsupported cases.

### (screen) (ira.deduct_less) — Do you want to deduct less than the most you can deduct, treating the rest as a nondeducti
Status: **MATCH**

Model: Matches line 12's option to deduct a smaller amount and treat the rest as a nondeductible contribution under Form 8606.

## Raw response

```yaml
lines:
  - key: "1a"
    status: MISMATCH
    reason: "IRS says if you weren't covered but your spouse was, you are considered covered unless you lived apart for all of 2025; cov_you counts only actual work or self-employed plan coverage, so the deemed-coverage case is omitted."
  - key: "1b"
    status: MATCH
    reason: "On a joint return the restatement tests spouse retirement-plan coverage, which matches line 1b's spouse-covered question."
  - key: "2a"
    status: MISMATCH
    reason: "IRS line 2 says married filing separately and lived apart from your spouse for all of 2025 enter $89,000; the line 2 helper maps every MFS return to $10,000."
  - key: "2b"
    status: MISMATCH
    reason: "IRS line 2 says married filing separately and lived apart from your spouse for all of 2025 enter $89,000; the line 2 helper maps every MFS return to $10,000."
  - key: "3"
    status: MATCH
    reason: "Enters the amount from Form 1040 line 9, as line 3 instructs."
  - key: "4"
    status: MISMATCH
    reason: "IRS line 4 is the total of Schedule 1 'lines 11 through 19a, plus 23 and 25'; the restatement omits lines 12, 14, and 23 and lists only selected lines."
  - key: "5"
    status: MATCH
    reason: "Subtracts line 4 from line 3, matching line 5; the same result applies to both joint columns."
  - key: "6a"
    status: MATCH
    reason: "When lines 2 through 6 apply, it subtracts line 5 from the line 2 taxpayer column and floors at zero, matching line 6's Yes/No result; otherwise it uses zero."
  - key: "6b"
    status: MATCH
    reason: "When lines 2 through 6 apply, it subtracts line 5 from the line 2 spouse column and floors at zero, matching line 6's Yes/No result; otherwise it uses zero."
  - key: "7a"
    status: MATCH
    reason: "Uses the line 7 threshold, applicable amount, percentage, rounding up to the next $10, and $200 floor for the taxpayer column."
  - key: "7b"
    status: MATCH
    reason: "Uses the line 7 threshold, applicable amount, percentage, rounding up to the next $10, and $200 floor for the spouse column."
  - key: "8"
    status: MATCH
    reason: "Adds W-2 box 1 wages and Schedule 1 line 2a; nontaxable combat pay, which the IRS also includes, is excluded by the ira.combat_gate refusal."
  - key: "9"
    status: MISMATCH
    reason: "IRS line 9 includes earned income received 'as a self-employed individual or a partner'; person.ira_se is zero without a Schedule C, so partner or other self-employment income not on Schedule C is omitted, and the stated refusal covers only Schedule C income not from personal services."
  - key: "10"
    status: MATCH
    reason: "Adds line 8 and line 9, as line 10 instructs."
  - key: "(screen) (ira.special)"
    status: MATCH
    reason: "The screen lists the nonqualified deferred compensation/457, fellowship or stipend, qualified reservist repayment, and difficulty-of-care special cases reflected in the line 20 instructions."
  - key: "(screen) (ira.se_capital)"
    status: MATCH
    reason: "Asks whether Schedule C income is from a business where personal services are not a material income-producing factor, matching the line 9 rule."
  - key: "11a"
    status: MATCH
    reason: "Sums the taxpayer's traditional IRA contributions for 2025, excluding rollovers and other noncontributions as the line 20 instructions require."
  - key: "11b"
    status: MATCH
    reason: "Sums the spouse's traditional IRA contributions for 2025, excluding rollovers and other noncontributions as the line 20 instructions require."
  - key: "12a"
    status: MATCH
    reason: "Computes the smallest of line 7a, line 10, and line 11a for the taxpayer's column, as line 12a instructs, with refusals narrowing unsupported cases."
  - key: "12b"
    status: MATCH
    reason: "Computes the smallest of line 7b, line 10, and line 11b for the spouse's column, as line 12b instructs, with refusals narrowing unsupported cases."
  - key: "(screen) (ira.deduct_less)"
    status: MATCH
    reason: "Matches line 12's option to deduct a smaller amount and treat the rest as a nondeductible contribution under Form 8606."
```
