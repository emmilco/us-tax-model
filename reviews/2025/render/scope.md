# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | fac5a91ee537ee2571dedfcb459a6261e7475692252de107bccccae752ac2e23 |
| lines judged | 5 |
| match / mismatch / unclear / missing | 5 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### schedule1 — Any income or adjustment requiring Schedule 1 other than unemployment compensation, educat
Status: **MATCH**

Model: This is a filer-answered scope question, and its label and restatement are identical. It screens out Schedule 1 items, consistent with Form 1040 line 8 'Additional income from Schedule 1, line 10' and line 10 'Adjustments to income from Schedule 1, line 26', and the refusal names what is excluded.

### credits — Do you want to claim any credit other than the foreign tax credit claimed without Form 111
Status: **MATCH**

Model: This is a filer-answered scope question, and its label and restatement are identical. The refusal names the excluded credits, including Form 1040 lines 29 to 31 ('American opportunity credit from Form 8863', 'Refundable adoption credit from Form 8839', 'Amount from Schedule 3, line 15'), which narrows scope without miscomputing any line.

### other_income — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or
Status: **MATCH**

Model: This is a filer-answered scope question, and its label and restatement are identical. The items it screens match Form 1040 lines 1b-1h (household wages, tips, Medicaid waiver payments, dependent care, adoption benefits, Form 8919 wages, other earned income), and screening out more than needed only narrows scope.

### other_line16 — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no t
Status: **MATCH**

Model: This is a filer-answered scope question, and its label and restatement are identical. It covers the line 16 checkboxes 'Form(s): 1 8814 2 4972 3', and the further items it screens only narrow scope through the named refusal.

### ready — All declared scope screens passed
Status: **MATCH**

Model: The gate value is true, and every unsupported case is excluded by a named refusal. The married-filing-separately refusal is consistent with the instructions ('You also can't take the standard deduction if your spouse itemizes deductions'; the education credits are unavailable) and with line 6d's lived-apart rule.

## Raw response

```yaml
```yaml
lines:
  - key: "schedule1"
    status: MATCH
    reason: "This is a filer-answered scope question, and its label and restatement are identical. It screens out Schedule 1 items, consistent with Form 1040 line 8 'Additional income from Schedule 1, line 10' and line 10 'Adjustments to income from Schedule 1, line 26', and the refusal names what is excluded."
  - key: "credits"
    status: MATCH
    reason: "This is a filer-answered scope question, and its label and restatement are identical. The refusal names the excluded credits, including Form 1040 lines 29 to 31 ('American opportunity credit from Form 8863', 'Refundable adoption credit from Form 8839', 'Amount from Schedule 3, line 15'), which narrows scope without miscomputing any line."
  - key: "other_income"
    status: MATCH
    reason: "This is a filer-answered scope question, and its label and restatement are identical. The items it screens match Form 1040 lines 1b-1h (household wages, tips, Medicaid waiver payments, dependent care, adoption benefits, Form 8919 wages, other earned income), and screening out more than needed only narrows scope."
  - key: "other_line16"
    status: MATCH
    reason: "This is a filer-answered scope question, and its label and restatement are identical. It covers the line 16 checkboxes 'Form(s): 1 8814 2 4972 3', and the further items it screens only narrow scope through the named refusal."
  - key: "ready"
    status: MATCH
    reason: "The gate value is true, and every unsupported case is excluded by a named refusal. The married-filing-separately refusal is consistent with the instructions ('You also can't take the standard deduction if your spouse itemizes deductions'; the education credits are unavailable) and with line 6d's lived-apart rule."
```
```
