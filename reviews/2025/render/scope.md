# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | cef50ac32d0cb689e9da2b06f2bd71430ce1f9b6ec36e683c61e73b5b1ce6d4b |
| lines judged | 6 |
| match / mismatch / unclear / missing | 6 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 117 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 117 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### schedule1 — Any income or adjustment requiring Schedule 1 other than unemployment compensation, educat
Status: **MATCH**

Model: This is a filer-answered scope screen, and its restatement matches its label. Form 1040 confirms Schedule 1 feeds line 8 ('Additional income from Schedule 1, line 10') and line 10 ('Adjustments to income from Schedule 1, line 26'). The refusal names the excluded Schedule 1 items. The item-by-item Schedule 1 references (such as line 8s) are not in the given text, but they only widen the screen and do not change any computed amount.

### schedule1a — Do you qualify for any Schedule 1-A deduction (qualified tips, qualified overtime compensa
Status: **MATCH**

Model: This is a filer-answered screen, and its restatement matches its label. Form 1040 line 13b reads 'Additional deductions from Schedule 1-A, line 38', and the refusal excludes all Schedule 1-A deductions. The specific deduction types listed are not in the given text, but asking about any of them only widens the screen.

### credits — Do you want to claim any credit other than the foreign tax credit claimed without Form 111
Status: **MATCH**

Model: This is a filer-answered screen, and its restatement matches its label. Form 1040 shows credits entering through line 19 (Schedule 8812), line 20 ('Amount from Schedule 3, line 8'), line 27a (EIC), line 28 (ACTC) and lines 29 to 31. Page 117 covers the excess social security credit. The refusal names the excluded credit lines, so the screen correctly narrows scope to the supported credits.

### other_income — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or
Status: **MATCH**

Model: This is a filer-answered screen, and its restatement matches its label. The items it screens out correspond to Form 1040 lines 1b to 1h (household wages, unreported tips, 'Medicaid waiver payments not reported on Form(s) W-2', dependent care and adoption benefits, Form 8919 wages, other earned income) and to the nonresident alien spouse checkbox. Passive activity treatment is not in the given text, but screening it out only narrows scope, and the refusal names the exclusion.

### other_line16 — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no t
Status: **MATCH**

Model: This is a filer-answered screen, and its restatement matches its label. Form 1040 line 16 reads 'Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3', which is consistent with screening out Form 8814, Form 4972 and other line 16 forms. The other forms listed (8615, 962, 8621, 8978, education credit recapture) are not in the given text, but screening them out only narrows scope, and the refusal names the exclusion.

### ready — All declared scope screens passed
Status: **MATCH**

Model: This is a constant true gate whose refusals name each excluded case. The married-status refusal is supported by the line 11 instruction for excess social security tax: 'Figure this amount separately for you and your spouse.' The s3.married gate covers both married boxes on the Filing Status line: 'Married filing jointly' and 'Married filing separately'.

## Raw response

```yaml
```yaml
lines:
  - key: "schedule1"
    status: MATCH
    reason: "This is a filer-answered scope screen, and its restatement matches its label. Form 1040 confirms Schedule 1 feeds line 8 ('Additional income from Schedule 1, line 10') and line 10 ('Adjustments to income from Schedule 1, line 26'). The refusal names the excluded Schedule 1 items. The item-by-item Schedule 1 references (such as line 8s) are not in the given text, but they only widen the screen and do not change any computed amount."
  - key: "schedule1a"
    status: MATCH
    reason: "This is a filer-answered screen, and its restatement matches its label. Form 1040 line 13b reads 'Additional deductions from Schedule 1-A, line 38', and the refusal excludes all Schedule 1-A deductions. The specific deduction types listed are not in the given text, but asking about any of them only widens the screen."
  - key: "credits"
    status: MATCH
    reason: "This is a filer-answered screen, and its restatement matches its label. Form 1040 shows credits entering through line 19 (Schedule 8812), line 20 ('Amount from Schedule 3, line 8'), line 27a (EIC), line 28 (ACTC) and lines 29 to 31. Page 117 covers the excess social security credit. The refusal names the excluded credit lines, so the screen correctly narrows scope to the supported credits."
  - key: "other_income"
    status: MATCH
    reason: "This is a filer-answered screen, and its restatement matches its label. The items it screens out correspond to Form 1040 lines 1b to 1h (household wages, unreported tips, 'Medicaid waiver payments not reported on Form(s) W-2', dependent care and adoption benefits, Form 8919 wages, other earned income) and to the nonresident alien spouse checkbox. Passive activity treatment is not in the given text, but screening it out only narrows scope, and the refusal names the exclusion."
  - key: "other_line16"
    status: MATCH
    reason: "This is a filer-answered screen, and its restatement matches its label. Form 1040 line 16 reads 'Tax (see instructions). Check if any from Form(s): 1 8814 2 4972 3', which is consistent with screening out Form 8814, Form 4972 and other line 16 forms. The other forms listed (8615, 962, 8621, 8978, education credit recapture) are not in the given text, but screening them out only narrows scope, and the refusal names the exclusion."
  - key: "ready"
    status: MATCH
    reason: "This is a constant true gate whose refusals name each excluded case. The married-status refusal is supported by the line 11 instruction for excess social security tax: 'Figure this amount separately for you and your spouse.' The s3.married gate covers both married boxes on the Filing Status line: 'Married filing jointly' and 'Married filing separately'."
```
```
