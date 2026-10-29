# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | facade160f252502b7cf33e77ae17024a055de9eaa832fc13ba3fc03fcb0c123 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 010ba9a7b461a08d13c0cd702103c54b9cbec9f921017321522508db869c1b94 |
| lines judged | 5 |
| match / mismatch / unclear / missing | 3 / 0 / 2 / 0 |
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

Model: The text given confirms only that Form 1040 line 8 takes 'Additional income from Schedule 1, line 10' and line 10 takes 'Adjustments to income from Schedule 1, line 26'. Schedule 1 and its instructions are not provided, so the cited Schedule 1 lines (8s, 12, 14, 23) and the list of items the screen excludes cannot be checked.

Ruling: interface gap; f1040 (2025) line 8, "Additional income from Schedule 1, line 10", and line 10, "Adjustments to income from Schedule 1, line 26". The pages given were Form 1040 pp. 1-2 and i1040gi p. 14 only; the text that would decide the listed items is not among them: interface gap (a coverage gap of the review). Checked against Schedule 1 in the earlier rulings (f1040s1 p. 1, line 8s; p. 2, lines 12, 14 and 23): the line numbers the question names are right and its supported list is the Stage 16 slice; the refusal for a yes names the same items (BUG-0081). Stage 19 did not change this question. Restatement accepted.

### credits — Do you want to claim any credit other than the foreign tax credit claimed without Form 111
Status: **UNCLEAR**

Restated: Input — Do you want to claim any credit other than the foreign tax credit claimed without Form 1116, the excess social security credit, the child tax credit, the credit for other dependents, the additional child tax credit, the earned income credit, the credit for child and dependent care expenses (Form 2441), the retirement savings contributions credit (Form 8880), the residential energy credits (Form 5695), the net premium tax credit this tool figures on Form 8962 from your Forms 1095-A (Schedule 3 line 9) and the education credits this tool figures on Form 8863 (the American opportunity and lifetime learning credits), or do you have any other amount for Schedule 3 Part I (for example a Form 8978 adjustment)?

Model: The Form 1040 text confirms line 20 ('Amount from Schedule 3, line 8'), line 29 ('American opportunity credit from Form 8863, line 8'), line 30 ('Refundable adoption credit from Form 8839, line 13') and line 31 ('Amount from Schedule 3, line 15'). Schedule 3 is not provided, so its Part I lines and the line 9 net premium tax credit reference cannot be checked.

Ruling: interface gap; f1040s3 p. 1: Part I is lines 1 to 8, line 3 "Education credits from Form 8863, line 19" and lines 6a to 6z the other nonrefundable credits; Part II line 9 "Net premium tax credit. Attach Form 8962"; Form 1040 line 29, "American opportunity credit from Form 8863, line 8". The pages given were Form 1040 pp. 1-2 and i1040gi p. 14 only; the text that would decide the listed items is not among them: interface gap (a coverage gap of the review). Checked against Schedule 3 and the Stage 19 data: the question now lists "the education credits this tool figures on Form 8863 (the American opportunity and lifetime learning credits)" among the supported credits, which matches s3.line3 (Form 8863 line 19 when f8863.eligible) and f1040.line29 (Form 8863 line 8 when eligible, its refusal removed); the refusal shown for a yes (scope.ready, f1040.line30, s3.line8) now reads "Other credit forms (Schedule 3 lines 6a to 6z; Form 1040 lines 30 and 31)", no longer naming line 3 or line 29, and its remedy names "the net premium tax credit figured on Form 8962 and the education credits (Form 8863)", so Stage 18’s F3 and BUG-0193 are fixed. Education situations that stay refused (Form 8862 or a ban, an academic period with excess assistance, excluded foreign or possession income, recapture) have their own cited screens (f8863.ban, the per-student D3 screens person.edu_over_refused and dependent.edu_over_refused, sa.excluded_income on Form 8863 lines 3 and 14, scope.other_line16), so a filer with such a case who answers no here is still refused. Restatement accepted.

### other_income — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or
Status: **MATCH**

Model: Form 1040 line 1b is household employee wages, 1c tip income, 1d Medicaid waiver payments, 1f adoption benefits, 1g Form 8919 wages and 1h other earned income, which agrees with 'lines 1b to 1d and 1f to 1h'. Line 1e ('Taxable dependent care benefits from Form 2441, line 26') is consistently left out, with only non-box-10 dependent care benefits screened.

### other_line16 — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no t
Status: **MATCH**

Model: Line 16 reads 'Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3', and the screen catches Form 8814 and Form 4972 plus any other line 16 tax or filing. That correctly flags cases outside the basic tax computation.

### ready — All declared scope screens passed
Status: **MATCH**

Model: The helper is true when the screens pass, and each refusal names what is excluded. The MFS refusal agrees with the instructions that a separate filer 'can't take ... the student loan interest deduction, or the education credits' and 'can't take the standard deduction if your spouse itemizes deductions'. The credits refusal's references to Form 1040 lines 30 and 31 agree with the form.

## Raw response

```yaml
```yaml
lines:
  - key: "schedule1"
    status: UNCLEAR
    reason: "The text given confirms only that Form 1040 line 8 takes 'Additional income from Schedule 1, line 10' and line 10 takes 'Adjustments to income from Schedule 1, line 26'. Schedule 1 and its instructions are not provided, so the cited Schedule 1 lines (8s, 12, 14, 23) and the list of items the screen excludes cannot be checked."
  - key: "credits"
    status: UNCLEAR
    reason: "The Form 1040 text confirms line 20 ('Amount from Schedule 3, line 8'), line 29 ('American opportunity credit from Form 8863, line 8'), line 30 ('Refundable adoption credit from Form 8839, line 13') and line 31 ('Amount from Schedule 3, line 15'). Schedule 3 is not provided, so its Part I lines and the line 9 net premium tax credit reference cannot be checked."
  - key: "other_income"
    status: MATCH
    reason: "Form 1040 line 1b is household employee wages, 1c tip income, 1d Medicaid waiver payments, 1f adoption benefits, 1g Form 8919 wages and 1h other earned income, which agrees with 'lines 1b to 1d and 1f to 1h'. Line 1e ('Taxable dependent care benefits from Form 2441, line 26') is consistently left out, with only non-box-10 dependent care benefits screened."
  - key: "other_line16"
    status: MATCH
    reason: "Line 16 reads 'Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3', and the screen catches Form 8814 and Form 4972 plus any other line 16 tax or filing. That correctly flags cases outside the basic tax computation."
  - key: "ready"
    status: MATCH
    reason: "The helper is true when the screens pass, and each refusal names what is excluded. The MFS refusal agrees with the instructions that a separate filer 'can't take ... the student loan interest deduction, or the education credits' and 'can't take the standard deduction if your spouse itemizes deductions'. The credits refusal's references to Form 1040 lines 30 and 31 agree with the form."
```
```
