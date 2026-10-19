# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 0ed77fa7cfec4684291d378c63c113bab22eb3cecb66f715575e002d44363199 |
| lines judged | 5 |
| match / mismatch / unclear / missing | 5 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### schedule1 — Any income or adjustment requiring Schedule 1 other than unemployment compensation, educat
Status: **MATCH**

Model: The restatement asks exactly what the label describes, so the input captures the intended screen. The pages given show only Form 1040 line 8 ('Additional income from Schedule 1, line 10') and line 10 ('Adjustments to income from Schedule 1, line 26'), which fit routing any Schedule 1 item out of scope; Schedule 1's own line items, such as line 8s, are not in the text and cannot be checked further.

### credits — Do you want to claim any credit other than the foreign tax credit claimed without Form 111
Status: **MATCH**

Model: The input matches its label, and the refusal names the excluded credit lines. These include Form 1040 lines 29 to 31, which the form shows as 'American opportunity credit from Form 8863, line 8', 'Refundable adoption credit from Form 8839, line 13' and 'Amount from Schedule 3, line 15'. The kept excess social security credit appears in the instructions as Schedule 3 line 11.

### other_income — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or
Status: **MATCH**

Model: The input matches its label, and the items it screens out match Form 1040 lines 1b through 1h as printed. Those are household employee wages, tips not on line 1a, Medicaid waiver payments not on W-2, taxable dependent care benefits, adoption benefits, Form 8919 wages and other earned income.

### other_line16 — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no t
Status: **MATCH**

Model: The input matches its label. Form 1040 line 16 reads 'Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3', which fits refusing any additional line 16 form or tax. The other items listed (Form 8615, section 962, Form 8621) are not in the given text but only widen the refusal.

### ready — All declared scope screens passed
Status: **MATCH**

Model: Ready is always true once every refusal gate is false, and each refusal names the excluded form. The s3.married refusal is supported by the Schedule 3 line 11 instruction 'Figure this amount separately for you and your spouse', and its gate correctly tests for the married filing jointly or married filing separately statuses.

## Raw response

```yaml
```yaml
lines:
  - key: "schedule1"
    status: MATCH
    reason: "The restatement asks exactly what the label describes, so the input captures the intended screen. The pages given show only Form 1040 line 8 ('Additional income from Schedule 1, line 10') and line 10 ('Adjustments to income from Schedule 1, line 26'), which fit routing any Schedule 1 item out of scope; Schedule 1's own line items, such as line 8s, are not in the text and cannot be checked further."
  - key: "credits"
    status: MATCH
    reason: "The input matches its label, and the refusal names the excluded credit lines. These include Form 1040 lines 29 to 31, which the form shows as 'American opportunity credit from Form 8863, line 8', 'Refundable adoption credit from Form 8839, line 13' and 'Amount from Schedule 3, line 15'. The kept excess social security credit appears in the instructions as Schedule 3 line 11."
  - key: "other_income"
    status: MATCH
    reason: "The input matches its label, and the items it screens out match Form 1040 lines 1b through 1h as printed. Those are household employee wages, tips not on line 1a, Medicaid waiver payments not on W-2, taxable dependent care benefits, adoption benefits, Form 8919 wages and other earned income."
  - key: "other_line16"
    status: MATCH
    reason: "The input matches its label. Form 1040 line 16 reads 'Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3', which fits refusing any additional line 16 form or tax. The other items listed (Form 8615, section 962, Form 8621) are not in the given text but only widen the refusal."
  - key: "ready"
    status: MATCH
    reason: "Ready is always true once every refusal gate is false, and each refusal names the excluded form. The s3.married refusal is supported by the Schedule 3 line 11 instruction 'Figure this amount separately for you and your spouse', and its gate correctly tests for the married filing jointly or married filing separately statuses."
```
```
