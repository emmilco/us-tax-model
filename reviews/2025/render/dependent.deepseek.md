# Render comparison — dependent

The rendered English of every printed line of `Dependents — qualifying child and qualifying relative tests, per person listed` (`rendered/2025/dependent.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 881d5b4d4da4ee2129872c38908fa9d761d8a0ca8e9103fb0e27648fd74109fb |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 72877d49a2fa507fbeec2880ebde04dba1b4b451d76aee7a6d6e29f0dc8b8ec8 |
| lines judged | 2 |
| match / mismatch / unclear / missing | 0 / 2 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 14, 17, 18, 19, 20, 21, 22, 41, 43, 44, 45, 46 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 14, 17, 18, 19, 20, 21, 22, 41, 43, 44, 45 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1040s8812 | 2025; created 2025-07-30 | 1, 2 | whole document | 9b38295071c42fe489ec8f93e117b31eda11355b5a95e3fe388eeee69601c8c9 | - | 3525d47f51cb713591081610a862cae77eff08a8aa7e2064a96b15cee4fd5cb9 |
| i2441 | 2025 | 1, 3, 4 | cited pages | 361baee739cc7cb7b6a84c7412397cfba901c1a3e5f225a8077cb8716917887e | 1, 3, 4 | 3046d96b0769e20213f700deb20a0de9edc6a4572eda61bd70f5c8c88bc912ee |
| p503 | For use in preparing 2025 returns | 3, 10 | cited pages | a1ff9e2c3120455f6049fc50f0af8c5b8160302c198162dede66b2c8a5640607 | 3, 10 | 44d87f0ddfd4f953ea02cf5cc31e203e754c88aa74627dac5a551f46c6bf65b9 |
| f2441 | 2025; created 2025-03-18 | 1, 2 | whole document | f39ca34d11c156e1ac55f4e2b5f16ef03c919773245cd7e50836e4c1555339c7 | - | 0e24fa891992674b84736c78565752c4a7d6f411fca4e24e5bb1307f239f60d6 |
| p501 | 2025 returns; PDF created 2026-02-04 | 13, 19 | pages named by another document's citation | 6aca9108a08fb6d4725c630023df5e17084d92135c6607cd7c536e8e0c67f19b | 13, 19 | 2e0a281a7d3f73f1334d5f59a39a9fe4c393fd10dd6e6c6b1b8639c5ef038671 |

## Lines

### 2(d) — Qualified expenses you incurred and paid in 2025 for the person listed in column (a)
Status: **MISMATCH**

Restated: Enter the amount from helper "Qualified expenses incurred and paid in 2025 for this person's care".

Model: The IRS column (d) instruction says “If you completed Part III, don't include in column (d) any benefits shown on line 28,” but the helper says to include expenses paid with dependent care benefits and only subtracts excluded benefits later.

Ruling: ambiguity; existing owner ruling amb.2025.dc_line30, Stage 15 decision 6 (T-048). Archived f2441 (2025) p. 2 line 30 and i2441 p. 3 Column (d) request excluding benefits shown on line 28. The project deliberately presents each person's gross expenses and subtracts the excluded benefits once in the aggregate f2441.line30; the register records the owner's choice because the sources give no allocation rule among persons. This is an acknowledged departure in per-person display under that recorded ruling, not model error and not a claim that literal column (d) wording matches. Retain the ambiguity reference and the objection.

### 2(c) — Check here if the qualifying person was over age 12 and was disabled
Status: **MISMATCH**

Restated: helper "A qualifying person for Form 2441 (you have care expenses, and this person is your dependent and either your qualifying child under 13 or not able to care for themselves and living with you for more than half the year)" = true and helper "Age at the end of 2025" ≥ 13 (dc.child_age) and helper "Physically or mentally not able to care for themselves?" = true

Model: The IRS says to check column (c) if the qualifying person “was over age 12 at the time the care was provided and was disabled,” but the restatement tests “Age at the end of 2025” ≥ 13 instead of age at the time care was provided.

Ruling: finding; BUG-0111 open. Archived i2441 (2025) p. 3 qualifying-person Column (c) tests age at the time of care, but dependent.dc_line2c tests age at year-end. Reproduced from stage15.f2441.s8 with age=13 and dc_under13=true: the checkbox is true although these same inputs can describe care entirely before the thirteenth birthday. No input distinguishes the two care timings. Displayed-checkbox defect, no tax amount change; form correction and paired regression fixtures remain pending, with no correctness assertion claimed.

## Raw response

```yaml
lines:
  - key: "2(d)"
    status: MISMATCH
    reason: "The IRS column (d) instruction says “If you completed Part III, don't include in column (d) any benefits shown on line 28,” but the helper says to include expenses paid with dependent care benefits and only subtracts excluded benefits later."
  - key: "2(c)"
    status: MISMATCH
    reason: "The IRS says to check column (c) if the qualifying person “was over age 12 at the time the care was provided and was disabled,” but the restatement tests “Age at the end of 2025” ≥ 13 instead of age at the time care was provided."
```
