# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | facade160f252502b7cf33e77ae17024a055de9eaa832fc13ba3fc03fcb0c123 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 010ba9a7b461a08d13c0cd702103c54b9cbec9f921017321522508db869c1b94 |
| lines judged | 5 |
| match / mismatch / unclear / missing | 0 / 0 / 5 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### schedule1 — Any income or adjustment requiring Schedule 1 other than the ones this tool asks about sep
Status: **UNCLEAR**

Restated: Input — Any income or adjustment requiring Schedule 1 other than the ones this tool asks about separately (business income or loss from Schedule C; a taxable state or local income tax refund; alimony under an agreement made before 2019; unemployment compensation; the line 8 items asked one by one; educator expenses; the HSA deduction; the deductible part of self-employment tax; self-employed SEP and SIMPLE contributions; the self-employed health insurance deduction; the penalty on early withdrawal of savings; the IRA deduction; student loan interest; jury duty pay you gave your employer), including statutory-employee wages or clergy income; church employee income (wages from a church that elected exemption from social security and Medicare taxes); other qualified retirement plans for the self-employed (such as a solo 401(k) or other Keogh plan); a refund or other recovery of an amount you deducted or took a credit for in an earlier year, other than a state or local income tax refund (for example a refund of general sales tax, real estate tax or personal property tax, a refund of mortgage interest in box 4 of Form 1098, a reimbursement of medical expenses, or a payment on a bad debt you deducted); sales of business property (Form 4797); a net operating loss deduction; rental real estate, royalties, partnerships, S corporations, estates or trusts (Schedule E or a Schedule K-1); rental of personal property; farm income (Schedule F); an exclusion of Medicaid waiver payments (Schedule 1 line 8s); or an adjustment on Schedule 1 line 12, 14 or 23? (Schedule 1-A deductions are asked separately.)

Model: The provided IRS text only shows Form 1040 lines 8 and 10 referring to Schedule 1; it does not include the Schedule 1 line 8/12/14/23 item lists needed to verify the enumerated income and adjustments.

Ruling: interface gap; f1040 (2025) line 8, "Additional income from Schedule 1, line 10", and line 10, "Adjustments to income from Schedule 1, line 26". The pages given were Form 1040 pp. 1-2 and i1040gi p. 14 only; the text that would decide the listed items is not among them: interface gap (a coverage gap of the review). Checked against Schedule 1 in the earlier rulings (f1040s1 p. 1, line 8s; p. 2, lines 12, 14 and 23): the line numbers the question names are right and its supported list is the Stage 16 slice; the refusal for a yes names the same items (BUG-0081). Stage 19 did not change this question. Restatement accepted.

### credits — Do you want to claim any credit other than the foreign tax credit claimed without Form 111
Status: **UNCLEAR**

Restated: Input — Do you want to claim any credit other than the foreign tax credit claimed without Form 1116, the excess social security credit, the child tax credit, the credit for other dependents, the additional child tax credit, the earned income credit, the credit for child and dependent care expenses (Form 2441), the retirement savings contributions credit (Form 8880), the residential energy credits (Form 5695), the net premium tax credit this tool figures on Form 8962 from your Forms 1095-A (Schedule 3 line 9) and the education credits this tool figures on Form 8863 (the American opportunity and lifetime learning credits), or do you have any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)?

Model: The provided text shows only Form 1040 line references to Schedule 3 and other credit forms, not the Schedule 3 Part I or credit-eligibility text needed to verify this list.

Ruling: interface gap; f1040s3 p. 1: Part I is lines 1 to 8, line 3 "Education credits from Form 8863, line 19" and lines 6a to 6z the other nonrefundable credits; Part II line 9 "Net premium tax credit. Attach Form 8962"; Form 1040 line 29, "American opportunity credit from Form 8863, line 8". The pages given were Form 1040 pp. 1-2 and i1040gi p. 14 only; the text that would decide the listed items is not among them: interface gap (a coverage gap of the review). Checked against Schedule 3 and the Stage 19 data: the question now lists "the education credits this tool figures on Form 8863 (the American opportunity and lifetime learning credits)" among the supported credits, which matches s3.line3 (Form 8863 line 19 when f8863.eligible) and f1040.line29 (Form 8863 line 8 when eligible, its refusal removed); the refusal shown for a yes (scope.ready, f1040.line30, s3.line8) now reads "Other credit forms (Schedule 3 lines 6a to 6z; Form 1040 lines 30 and 31)", no longer naming line 3 or line 29, and its remedy names "the net premium tax credit figured on Form 8962 and the education credits (Form 8863)", so Stage 18’s F3 and BUG-0193 are fixed. Education situations that stay refused (Form 8862 or a ban, an academic period with excess assistance, excluded foreign or possession income, recapture) have their own cited screens (f8863.ban, the per-student D3 screens person.edu_over_refused and dependent.edu_over_refused, sa.excluded_income on Form 8863 lines 3 and 14, scope.other_line16), so a filer with such a case who answers no here is still refused. Restatement accepted.

### other_income — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or
Status: **UNCLEAR**

Restated: Input — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or return treatment outside wages, interest, dividends, supported securities sales, Form 1099-R distributions and social security benefits, including wages or tips not on a Form W-2, Medicaid waiver payments (whether or not in Form W-2 box 1), adoption benefits, dependent care benefits other than those shown in box 10 of a Form W-2 (or a grace-period amount from such a plan), other earned income (Form 1040 lines 1b to 1d and 1f to 1h), or income or loss from a passive activity (including gain on selling an interest in one)?

Model: There is no IRS text given for the nonresident-alien scope screen or for the listed other income/return treatments beyond general Form 1040 line labels.

Ruling: interface gap; f1040 (2025) lines 1b to 1h. The pages given were Form 1040 pp. 1-2 and i1040gi p. 14 only; the text that would decide the listed items is not among them: interface gap (a coverage gap of the review). The items are those of the earlier rulings (line 1e left to Form 2441; nonresident alien status and passive activities refusals recorded in spec 2.1). Its nonresident alien clause also carries i1040gi p. 115’s education-credit bar ("You, or your spouse, were a nonresident alien for any part of 2025 unless your filing status is married filing jointly") for Stage 19, more widely than the bar (it refuses a joint return with an electing nonresident spouse too): a refusal, so scope, not a defect of the computed line. Stage 19 did not change the question. Restatement accepted.

### other_line16 — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no t
Status: **UNCLEAR**

Restated: Input — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no tax), Form 4972, Form 8615, a section 962 election, Form 8621, a Form 8978 amount, or recapture of an education credit?

Model: Form 1040 line 16 says only 'Tax (see instructions)' and names forms 8814 and 4972; the referenced instructions and the other listed line 16 items are not provided.

Ruling: interface gap; f1040 (2025) line 16, the Form 8814 and Form 4972 boxes. The pages given were Form 1040 pp. 1-2 and i1040gi p. 14 only; the text that would decide the listed items is not among them: interface gap (a coverage gap of the review). The listed forms are refusals cited on the lines that read this question (f1040.line16). Its "recapture of an education credit" item keeps Form 8863 recapture refused, as Stage 19’s D1 decided. Unchanged. Restatement accepted.

### ready — All declared scope screens passed
Status: **UNCLEAR**

Restated: true = true

Model: This is an internal program gate ('All declared scope screens passed'), not an IRS form or worksheet line; the provided text does not define when all such screens pass.

Ruling: interface gap; the married filing separately refusal matches i1040gi p. 14, Married Filing Separately, and the other screens are filer-answered declarations whose items are cited on the lines that read them; for those the pages given (Form 1040, i1040gi p. 14) lack the deciding text. Checked against the data: Stage 18’s F3 is fixed (the scope.credits remedy on scope.ready now says "the net premium tax credit figured on Form 8962 and the education credits (Form 8863)", and its form text "Other credit forms (Schedule 3 lines 6a to 6z; Form 1040 lines 30 and 31)" no longer names line 29). The gate is the constant test true = true carrying the five refusals, as restated. Restatement accepted.

## Raw response

```yaml
lines:
  - key: "schedule1"
    status: UNCLEAR
    reason: "The provided IRS text only shows Form 1040 lines 8 and 10 referring to Schedule 1; it does not include the Schedule 1 line 8/12/14/23 item lists needed to verify the enumerated income and adjustments."
  - key: "credits"
    status: UNCLEAR
    reason: "The provided text shows only Form 1040 line references to Schedule 3 and other credit forms, not the Schedule 3 Part I or credit-eligibility text needed to verify this list."
  - key: "other_income"
    status: UNCLEAR
    reason: "There is no IRS text given for the nonresident-alien scope screen or for the listed other income/return treatments beyond general Form 1040 line labels."
  - key: "other_line16"
    status: UNCLEAR
    reason: "Form 1040 line 16 says only 'Tax (see instructions)' and names forms 8814 and 4972; the referenced instructions and the other listed line 16 items are not provided."
  - key: "ready"
    status: UNCLEAR
    reason: "This is an internal program gate ('All declared scope screens passed'), not an IRS form or worksheet line; the provided text does not define when all such screens pass."
```
