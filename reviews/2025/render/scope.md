# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 42fdc9a37fb87bca3d7ad1910241acd235f313584c848cfb76b4efe99dc1faa3 |
| lines judged | 6 |
| match / mismatch / unclear / missing | 6 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### schedule1 — Any income or adjustment requiring Schedule 1, including a taxable state or local tax refu
Status: **MATCH**

Model: This is a filer-supplied scope screen, and its label matches its restatement word for word. Form 1040 line 8 ('Additional income from Schedule 1, line 10') and line 10 ('Adjustments to income from Schedule 1, line 26') confirm that Schedule 1 items flow into the return, so excluding them by refusal is a valid narrowing. The Schedule 1 line 8s reference cannot be checked against the pages given.

### schedule1a — Do you qualify for any Schedule 1-A deduction (qualified tips, qualified overtime compensa
Status: **MATCH**

Model: The label matches the restatement. Form 1040 line 13b ('Additional deductions from Schedule 1-A, line 38') and line 12d ('Were born before January 2, 1961') support this as the Schedule 1-A screen, and the refusal names the excluded schedule.

### credits — Do you want to claim any credit other than the foreign tax credit claimed without Form 111
Status: **MATCH**

Model: The label matches the restatement. Form 1040 lines 19, 20, 27a, 28 and 29–31 show that the credits kept in scope (Schedule 8812 credits, EIC, and excess social security on Schedule 3 line 11) are separate from the other credits, which are excluded by refusal.

### other_income — Any retirement, Social Security, nonresident alien (you or your spouse, for any part of 20
Status: **MATCH**

Model: The label matches the restatement. It screens out income outside the supported items, including Form 1040 lines 1b–1h (for example '1d Medicaid waiver payments not reported on Form(s) W-2' and '1h Other earned income'), and lines 4–6 for IRA distributions, pensions and social security, with a refusal naming the exclusion.

### other_line16 — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no t
Status: **MATCH**

Model: The label matches the restatement. Form 1040 line 16 ('Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3') supports screening out filings of additional line 16 tax, and the refusal names what is excluded.

### ready — All declared scope screens passed
Status: **MATCH**

Model: The helper is constant true, and each refusal names an excluded case. The s3.married refusal is supported by the Schedule 3 line 11 instruction ('Figure this amount separately for you and your spouse'), and that gate correctly tests the two married filing statuses on Form 1040.

## Raw response

```yaml
```yaml
lines:
  - key: "schedule1"
    status: MATCH
    reason: "This is a filer-supplied scope screen, and its label matches its restatement word for word. Form 1040 line 8 ('Additional income from Schedule 1, line 10') and line 10 ('Adjustments to income from Schedule 1, line 26') confirm that Schedule 1 items flow into the return, so excluding them by refusal is a valid narrowing. The Schedule 1 line 8s reference cannot be checked against the pages given."
  - key: "schedule1a"
    status: MATCH
    reason: "The label matches the restatement. Form 1040 line 13b ('Additional deductions from Schedule 1-A, line 38') and line 12d ('Were born before January 2, 1961') support this as the Schedule 1-A screen, and the refusal names the excluded schedule."
  - key: "credits"
    status: MATCH
    reason: "The label matches the restatement. Form 1040 lines 19, 20, 27a, 28 and 29–31 show that the credits kept in scope (Schedule 8812 credits, EIC, and excess social security on Schedule 3 line 11) are separate from the other credits, which are excluded by refusal."
  - key: "other_income"
    status: MATCH
    reason: "The label matches the restatement. It screens out income outside the supported items, including Form 1040 lines 1b–1h (for example '1d Medicaid waiver payments not reported on Form(s) W-2' and '1h Other earned income'), and lines 4–6 for IRA distributions, pensions and social security, with a refusal naming the exclusion."
  - key: "other_line16"
    status: MATCH
    reason: "The label matches the restatement. Form 1040 line 16 ('Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3') supports screening out filings of additional line 16 tax, and the refusal names what is excluded."
  - key: "ready"
    status: MATCH
    reason: "The helper is constant true, and each refusal names an excluded case. The s3.married refusal is supported by the Schedule 3 line 11 instruction ('Figure this amount separately for you and your spouse'), and that gate correctly tests the two married filing statuses on Form 1040."
```
```
