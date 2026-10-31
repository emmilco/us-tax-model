# Render comparison — scope

The rendered English of every printed line of `Proof-of-concept scope screening` (`rendered/2025/scope.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | aeb1093d70c33f816a9820ecad746ef693b7a8040416837294e48b0e253cd30e |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | c19986791d91c8e0df9e7b353fde8f8bdd8aa3c6b766a45862738d604ee64383 |
| lines judged | 5 |
| match / mismatch / unclear / missing | 5 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040 | 2025; created 2025-09-05 | 1, 2 | whole document | ac32f00aed489e0722d0b409c0eb12915801d66f3a2fab05bc8391af61426383 | - | 72926cc2b256a68592e6cf0f2aa384ef8371eec968a0c8c62e050edf5bfea76a |
| i1040gi | 2025; printed date 2026-02-25 | 14, 36, 43 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 36, 43 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### schedule1 — Any income or adjustment requiring Schedule 1 other than the ones this tool asks about sep
Status: **MATCH**

Model: The helper correctly screens for Schedule 1 income or adjustments not separately supported, and the refusal names Schedule 1 as the excluded form.

### credits — Do you want to claim any credit other than the foreign tax credit claimed without Form 111
Status: **MATCH**

Model: The helper correctly screens for unsupported credits and other Schedule 3 Part I amounts, and the refusal names the other credit forms and lines 30/31 as outside the tool.

### other_income — Any nonresident alien status (you or your spouse, for any part of 2025) or other income or
Status: **MATCH**

Model: The helper correctly screens for other income or return treatment outside the supported items, including the Form 1040 line 1 items, and the refusal names additional income/return forms.

### other_line16 — Any additional Form 1040 line 16 tax or filing, including filing Form 8814 (even with no t
Status: **MATCH**

Model: The Form 8615 conditions, including the $2,700 threshold, filing requirement, joint-return bar, parent-alive requirement, and age/earned-income alternatives, track the IRS instructions for line 16; the refusal names additional line 16 tax forms.

### ready — All declared scope screens passed
Status: **MATCH**

Model: The helper is true when the declared scope screens are passed, and each refusal names the excluded case: Schedule 1, other credits, other income/return treatment, additional line 16 tax, or married filing separately.

## Raw response

```yaml
lines:
  - key: "schedule1"
    status: MATCH
    reason: "The helper correctly screens for Schedule 1 income or adjustments not separately supported, and the refusal names Schedule 1 as the excluded form."
  - key: "credits"
    status: MATCH
    reason: "The helper correctly screens for unsupported credits and other Schedule 3 Part I amounts, and the refusal names the other credit forms and lines 30/31 as outside the tool."
  - key: "other_income"
    status: MATCH
    reason: "The helper correctly screens for other income or return treatment outside the supported items, including the Form 1040 line 1 items, and the refusal names additional income/return forms."
  - key: "other_line16"
    status: MATCH
    reason: "The Form 8615 conditions, including the $2,700 threshold, filing requirement, joint-return bar, parent-alive requirement, and age/earned-income alternatives, track the IRS instructions for line 16; the refusal names additional line 16 tax forms."
  - key: "ready"
    status: MATCH
    reason: "The helper is true when the declared scope screens are passed, and each refusal names the excluded case: Schedule 1, other credits, other income/return treatment, additional line 16 tax, or married filing separately."
```
