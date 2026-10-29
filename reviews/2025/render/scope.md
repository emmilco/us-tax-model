# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-28 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 3ea20cab265b80639a4ea06824bd71d584d241c4dbf819265915d5d6648cc53a |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 7a3e89586d3009c33bd80de620a59b11bb9fb11a90f4892048faaf341a298b8d |
| lines judged | 5 |
| match / mismatch / unclear / missing | 5 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### schedule1 — Any income or adjustment requiring Schedule 1 other than the ones this tool asks about sep
Status: **MATCH**

Model: This is a filer-answered scope question, and the restatement asks exactly what the label says. Form 1040 line 8 ('Additional income from Schedule 1, line 10') and line 10 ('Adjustments to income from Schedule 1, line 26') confirm Schedule 1 feeds the return. The Schedule 1 line numbers it cites (8s, 12, 14, 23) are not in the text provided, so they could not be checked.

### credits — Do you want to claim any credit other than the foreign tax credit claimed without Form 111
Status: **MATCH**

Model: This is a filer-answered scope question whose restatement matches its label. Form 1040 line 20 ('Amount from Schedule 3, line 8') and lines 29–31 (American opportunity credit, refundable adoption credit, 'Amount from Schedule 3, line 15') are the credit entries this question and its refusal exclude. Schedule 3 itself is not in the text provided.

### other_income — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or
Status: **MATCH**

Model: This is a filer-answered scope question whose restatement matches its label. Its list agrees with Form 1040 lines 1b–1d (household wages not on W-2, unreported tips, Medicaid waiver payments) and 1f–1h (adoption benefits, Form 8919 wages, other earned income). It leaves out line 1e, which is consistent with dependent care being supported through Form 2441.

### other_line16 — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no t
Status: **MATCH**

Model: This is a filer-answered scope question whose restatement matches its label. Form 1040 line 16 reads 'Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3', which supports screening out Form 8814, Form 4972 and other line 16 additions.

### ready — All declared scope screens passed
Status: **MATCH**

Model: This is a constant gate whose refusals name each excluded case. The married filing separately refusal agrees with the instructions, which say a separate filer 'can't take ... the student loan interest deduction, or the education credits' and 'can't take the standard deduction if your spouse itemizes deductions.'

## Raw response

```yaml
```yaml
lines:
  - key: "schedule1"
    status: MATCH
    reason: "This is a filer-answered scope question, and the restatement asks exactly what the label says. Form 1040 line 8 ('Additional income from Schedule 1, line 10') and line 10 ('Adjustments to income from Schedule 1, line 26') confirm Schedule 1 feeds the return. The Schedule 1 line numbers it cites (8s, 12, 14, 23) are not in the text provided, so they could not be checked."
  - key: "credits"
    status: MATCH
    reason: "This is a filer-answered scope question whose restatement matches its label. Form 1040 line 20 ('Amount from Schedule 3, line 8') and lines 29–31 (American opportunity credit, refundable adoption credit, 'Amount from Schedule 3, line 15') are the credit entries this question and its refusal exclude. Schedule 3 itself is not in the text provided."
  - key: "other_income"
    status: MATCH
    reason: "This is a filer-answered scope question whose restatement matches its label. Its list agrees with Form 1040 lines 1b–1d (household wages not on W-2, unreported tips, Medicaid waiver payments) and 1f–1h (adoption benefits, Form 8919 wages, other earned income). It leaves out line 1e, which is consistent with dependent care being supported through Form 2441."
  - key: "other_line16"
    status: MATCH
    reason: "This is a filer-answered scope question whose restatement matches its label. Form 1040 line 16 reads 'Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3', which supports screening out Form 8814, Form 4972 and other line 16 additions."
  - key: "ready"
    status: MATCH
    reason: "This is a constant gate whose refusals name each excluded case. The married filing separately refusal agrees with the instructions, which say a separate filer 'can't take ... the student loan interest deduction, or the education credits' and 'can't take the standard deduction if your spouse itemizes deductions.'"
```
```
