# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | f72f7820b5cbfd18dd0db93fa0e964ad9c671074ca9d21129ddd269c34236a2b |
| lines judged | 5 |
| match / mismatch / unclear / missing | 2 / 0 / 3 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### schedule1 — Any income or adjustment requiring Schedule 1 other than business income or loss from Sche
Status: **UNCLEAR**

Restated: Input — Any income or adjustment requiring Schedule 1 other than business income or loss from Schedule C, unemployment compensation, educator expenses, the HSA deduction, the deductible part of self-employment tax, self-employed SEP and SIMPLE contributions, the self-employed health insurance deduction and student loan interest, including a taxable state or local tax refund; alimony; an IRA deduction; statutory-employee wages or clergy income; church employee income (wages from a church that elected exemption from social security and Medicare taxes); other qualified retirement plans for the self-employed (such as a solo 401(k) or other Keogh plan); rental real estate, royalties, partnerships, S corporations, estates or trusts (Schedule E or a Schedule K-1); rental of personal property; farm income (Schedule F); gambling winnings, prizes or other income for Schedule 1 line 8; or an exclusion of Medicaid waiver payments (Schedule 1 line 8s)? (Schedule 1-A deductions are asked separately.)

Model: This is a filer-answered scope question, and its label and restatement agree. Form 1040 line 8 ('Additional income from Schedule 1, line 10') and line 10 ('Adjustments to income from Schedule 1, line 26') confirm that Schedule 1 feeds the return. However, Schedule 1 and its instructions are not provided, so the listed items (for example Schedule 1 line 8 and line 8s, Medicaid waiver exclusion, church employee income) cannot be checked against IRS wording.

Ruling: unclear for want of text; restatement accepted. A filer-answered scope question whose wording the model found consistent with the Form 1040 lines it could see; the items it lists are the refusals recorded in spec 2.1 and on the lines that read this question, each cited there. The Schedule 1 and Schedule 3 instructions are cited by those lines, not by the question.

### credits — Do you want to claim any credit other than the foreign tax credit claimed without Form 111
Status: **UNCLEAR**

Restated: Input — Do you want to claim any credit other than the foreign tax credit claimed without Form 1116, the excess social security credit, the child tax credit, the credit for other dependents, the additional child tax credit and the earned income credit, or do you have any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)?

Model: This is a filer-answered scope question, and its label and restatement agree. Form 1040 lines 19, 20, 27a, 28 and 31 confirm the Schedule 8812, Schedule 3 and EIC credit lines. However, Schedule 3, Form 1116 and Form 8978 text are not provided, so the credits excluded and retained cannot be checked against IRS wording.

Ruling: unclear for want of text; restatement accepted. A filer-answered scope question whose wording the model found consistent with the Form 1040 lines it could see; the items it lists are the refusals recorded in spec 2.1 and on the lines that read this question, each cited there. The Schedule 1 and Schedule 3 instructions are cited by those lines, not by the question.

### other_income — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or
Status: **MATCH**

Model: This is a filer-answered scope question, and its label and restatement agree. The items it names that the given text covers match it: Form 1040 lines 1b-1h (for example '1d Medicaid waiver payments not reported on Form(s) W-2', '1e Taxable dependent care benefits', '1f Employer-provided adoption benefits') and the nonresident or dual-status alien spouse rules in the filing status instructions. Excluding these from the program's scope is a permitted narrowing.

### other_line16 — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no t
Status: **UNCLEAR**

Restated: Input — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no tax), Form 4972, Form 8615, a section 962 election, Form 8621, a Form 8978 amount, or recapture of an education credit?

Model: This is a filer-answered scope question, and its label and restatement agree. Form 1040 line 16 shows 'Check if any from Form(s): 1 8814 2 4972 3', which is consistent with the question. However, the line 16 instructions are not provided, so the other listed items (Form 8615, section 962 election, Form 8621, Form 8978, education credit recapture) cannot be verified.

Ruling: unclear for want of text; restatement accepted. A filer-answered scope question whose wording the model found consistent with the Form 1040 lines it could see; the items it lists are the refusals recorded in spec 2.1 and on the lines that read this question, each cited there. The Schedule 1 and Schedule 3 instructions are cited by those lines, not by the question.

### ready — All declared scope screens passed
Status: **MATCH**

Model: The value is a constant true, and the refusals name the excluded cases. The MFS refusal agrees with the IRS text ('You also can't take the standard deduction if your spouse itemizes deductions'; separate filers 'can't take ... the student loan interest deduction, or the education credits'). One inconsistency does not change the value: the Schedule 1 refusal message lists only unemployment, educator expenses, HSA and student loan interest as supported, while the schedule1 screen also allows Schedule C income, SE tax, SEP/SIMPLE and self-employed health insurance.

## Raw response

```yaml
```yaml
lines:
  - key: "schedule1"
    status: UNCLEAR
    reason: "This is a filer-answered scope question, and its label and restatement agree. Form 1040 line 8 ('Additional income from Schedule 1, line 10') and line 10 ('Adjustments to income from Schedule 1, line 26') confirm that Schedule 1 feeds the return. However, Schedule 1 and its instructions are not provided, so the listed items (for example Schedule 1 line 8 and line 8s, Medicaid waiver exclusion, church employee income) cannot be checked against IRS wording."
  - key: "credits"
    status: UNCLEAR
    reason: "This is a filer-answered scope question, and its label and restatement agree. Form 1040 lines 19, 20, 27a, 28 and 31 confirm the Schedule 8812, Schedule 3 and EIC credit lines. However, Schedule 3, Form 1116 and Form 8978 text are not provided, so the credits excluded and retained cannot be checked against IRS wording."
  - key: "other_income"
    status: MATCH
    reason: "This is a filer-answered scope question, and its label and restatement agree. The items it names that the given text covers match it: Form 1040 lines 1b-1h (for example '1d Medicaid waiver payments not reported on Form(s) W-2', '1e Taxable dependent care benefits', '1f Employer-provided adoption benefits') and the nonresident or dual-status alien spouse rules in the filing status instructions. Excluding these from the program's scope is a permitted narrowing."
  - key: "other_line16"
    status: UNCLEAR
    reason: "This is a filer-answered scope question, and its label and restatement agree. Form 1040 line 16 shows 'Check if any from Form(s): 1 8814 2 4972 3', which is consistent with the question. However, the line 16 instructions are not provided, so the other listed items (Form 8615, section 962 election, Form 8621, Form 8978, education credit recapture) cannot be verified."
  - key: "ready"
    status: MATCH
    reason: "The value is a constant true, and the refusals name the excluded cases. The MFS refusal agrees with the IRS text ('You also can't take the standard deduction if your spouse itemizes deductions'; separate filers 'can't take ... the student loan interest deduction, or the education credits'). One inconsistency does not change the value: the Schedule 1 refusal message lists only unemployment, educator expenses, HSA and student loan interest as supported, while the schedule1 screen also allows Schedule C income, SE tax, SEP/SIMPLE and self-employed health insurance."
```
```
