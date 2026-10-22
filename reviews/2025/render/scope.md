# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 1942cb5c02933898482481ba41d8d4e0c9209945f755952eb8cd7c045345a9d8 |
| subject sha256 | a6590ce20b73459fafe2166962a4ab35b6a3426f7a6647e8c3492a8b740fb48c |
| lines judged | 5 |
| match / mismatch / unclear / missing | 1 / 0 / 4 / 0 |
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

Model: The Form 1040 text only says line 8 is 'Additional income from Schedule 1, line 10' and line 10 is 'Adjustments to income from Schedule 1, line 26'. The Schedule 1 line items this question carves out or lists, such as Schedule C, line 8s and alimony, aren't in the text given. Note that the question treats Schedule C income, the SE tax deduction, SEP/SIMPLE and SE health insurance as supported, but the matching refusal says everything except unemployment compensation, educator expenses, the HSA deduction and student loan interest is outside the tool.

Ruling: second construction right in part; proposed finding (wording of a refusal; no value changes). The question is filer-answered and its list of supported items matches what the project computes; the Schedule 1 lines it names are cited by the lines that read them, not by the question, and Form 1040 line 8, "Additional income from Schedule 1, line 10", and line 10, "Adjustments to income from Schedule 1, line 26" (f1040 (2025), lines 8 and 10), are all the given text shows (unclear for want of text; restatement accepted, as the prior ruling). The model's note is right: the refusal text shown for a Yes, under scope.ready and on Form 1040 lines 8 and 10 (scope.yaml; f1040.line8 and line10), still reads "Schedule 1 income and adjustments other than unemployment compensation, educator expenses, the HSA deduction and student loan interest are outside this tool", which leaves out the items the question itself carves out as supported (business income or loss from Schedule C, the deductible part of self-employment tax, self-employed SEP and SIMPLE contributions, the self-employed health insurance deduction). A filer told the refusal would read Schedule C income as outside the tool. Proposed fix: the remedy names the same supported items as the question. Recorded as BUG-0081 and TASKS.md T-050; the wording is corrected there, with the reviews of scope and f1040 rerun after.

### credits — Do you want to claim any credit other than the foreign tax credit claimed without Form 111
Status: **UNCLEAR**

Restated: Input — Do you want to claim any credit other than the foreign tax credit claimed without Form 1116, the excess social security credit, the child tax credit, the credit for other dependents, the additional child tax credit, the earned income credit, the credit for child and dependent care expenses (Form 2441), the retirement savings contributions credit (Form 8880) and the residential energy credits (Form 5695), or do you have any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)?

Model: The text shows Form 1040 lines 19, 20 ('Amount from Schedule 3, line 8'), 27a, 28, 29 (Form 8863), 30 (Form 8839) and 31 ('Amount from Schedule 3, line 15'). Schedule 3 and its credit lines aren't provided, so I can't confirm that the excluded set of credits is complete or correct. Education and adoption credits do fall under 'any credit other than', so they are screened out.

Ruling: unclear for want of text; restatement accepted (as the prior ruling). A filer-answered scope question whose wording the model found consistent with the Form 1040 lines it could see (lines 19, 20 'Amount from Schedule 3, line 8', 29 and 30); the credits it lists as supported are the Stage 15 slice (owner decisions in sources/2025/PREMISES.md, Stage 15 premise maps), and its refusal names what stays refused, Schedule 3 lines 3 and 6a to 6z and Form 1040 lines 29 to 31, each cited on the lines that read this question. No change.

### other_income — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or
Status: **UNCLEAR**

Restated: Input — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or return treatment outside wages, interest, dividends, supported securities sales, Form 1099-R distributions and social security benefits, including wages or tips not on a Form W-2, Medicaid waiver payments (whether or not in Form W-2 box 1), adoption benefits, dependent care benefits other than those shown in box 10 of a Form W-2 (or a grace-period amount from such a plan), other earned income (Form 1040 lines 1b to 1d and 1f to 1h), or income or loss from a passive activity (including gain on selling an interest in one)?

Model: This fits the Form 1040 income lines shown: 1b–1d and 1f–1h are screened, and 1e is left to Form 2441 ('Taxable dependent care benefits from Form 2441, line 26'). Nonresident alien status and passive-activity rules aren't in the text given. Line 1i, 'Nontaxable combat pay election', isn't named and is covered only by the general phrase 'other … return treatment'.

Ruling: unclear for want of text; restatement accepted. A filer-answered scope question; the model found its income items consistent with Form 1040 lines 1b to 1h, line 1e being left to Form 2441 ("Taxable dependent care benefits from Form 2441, line 26"). Line 1i needs no mention here: it is the nontaxable combat pay election for the EIC (i1040gi p. 25, Line 1i, "If you elect to include your nontaxable combat pay in your earned income when figuring the EIC, enter the amount on line 1i"), and any nontaxable combat pay is refused through s8812.combat_pay (on eic.step5_line4, Schedule 8812 line 18b and Form 2441 lines 4, 5, 18 and 19), so line 1i is never above zero. Nonresident alien status and passive activities are refusals recorded in spec 2.1. No change.

### other_line16 — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no t
Status: **MATCH**

Model: Form 1040 line 16 reads 'Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3'. The question screens out Form 8814 (even with no tax), Form 4972 and any other line-16 tax or filing, which covers the box 3 category.

### ready — All declared scope screens passed
Status: **UNCLEAR**

Restated: true = true

Model: The MFS refusal matches the text: 'Spouse itemizes on a separate return' (12b), line 6d's 'married filing separately and lived apart', and the instruction that MFS filers 'can't take … the student loan interest deduction, or the education credits' and get EIC and dependent care credit only 'in very limited circumstances'. The other refusals depend on Schedule 1, Schedule 3 and line 16 instructions that aren't provided, and the Schedule 1 refusal's list of supported items doesn't match the carve-outs in the schedule1 question.

Ruling: second construction right in part; proposed finding (the same as on schedule1; wording of a refusal; no value changes). The married filing separately refusal matches the text, as the model says (i1040gi p. 14, Married Filing Separately). The other refusals are filer-answered declarations whose items are cited on the lines that read them (unclear for want of text; accepted). But the refusal text shown for a Yes, under scope.ready and on Form 1040 lines 8 and 10 (scope.yaml; f1040.line8 and line10), still reads "Schedule 1 income and adjustments other than unemployment compensation, educator expenses, the HSA deduction and student loan interest are outside this tool", which leaves out the items the question itself carves out as supported (business income or loss from Schedule C, the deductible part of self-employment tax, self-employed SEP and SIMPLE contributions, the self-employed health insurance deduction). Proposed fix: the remedy names the same supported items as the question. Recorded as BUG-0081 and TASKS.md T-050; the wording is corrected there, with the reviews of scope and f1040 rerun after.

## Raw response

```yaml
```yaml
lines:
  - key: "schedule1"
    status: UNCLEAR
    reason: "The Form 1040 text only says line 8 is 'Additional income from Schedule 1, line 10' and line 10 is 'Adjustments to income from Schedule 1, line 26'. The Schedule 1 line items this question carves out or lists, such as Schedule C, line 8s and alimony, aren't in the text given. Note that the question treats Schedule C income, the SE tax deduction, SEP/SIMPLE and SE health insurance as supported, but the matching refusal says everything except unemployment compensation, educator expenses, the HSA deduction and student loan interest is outside the tool."
  - key: "credits"
    status: UNCLEAR
    reason: "The text shows Form 1040 lines 19, 20 ('Amount from Schedule 3, line 8'), 27a, 28, 29 (Form 8863), 30 (Form 8839) and 31 ('Amount from Schedule 3, line 15'). Schedule 3 and its credit lines aren't provided, so I can't confirm that the excluded set of credits is complete or correct. Education and adoption credits do fall under 'any credit other than', so they are screened out."
  - key: "other_income"
    status: UNCLEAR
    reason: "This fits the Form 1040 income lines shown: 1b–1d and 1f–1h are screened, and 1e is left to Form 2441 ('Taxable dependent care benefits from Form 2441, line 26'). Nonresident alien status and passive-activity rules aren't in the text given. Line 1i, 'Nontaxable combat pay election', isn't named and is covered only by the general phrase 'other … return treatment'."
  - key: "other_line16"
    status: MATCH
    reason: "Form 1040 line 16 reads 'Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3'. The question screens out Form 8814 (even with no tax), Form 4972 and any other line-16 tax or filing, which covers the box 3 category."
  - key: "ready"
    status: UNCLEAR
    reason: "The MFS refusal matches the text: 'Spouse itemizes on a separate return' (12b), line 6d's 'married filing separately and lived apart', and the instruction that MFS filers 'can't take … the student loan interest deduction, or the education credits' and get EIC and dependent care credit only 'in very limited circumstances'. The other refusals depend on Schedule 1, Schedule 3 and line 16 instructions that aren't provided, and the Schedule 1 refusal's list of supported items doesn't match the carve-outs in the schedule1 question."
```
```
