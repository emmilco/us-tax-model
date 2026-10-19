# Render comparison — otjob

The rendered English of every printed line of `Qualified Overtime Compensation From More Than One Employer Worksheet (Schedule 1-A, line 14a) — one row per employer` (`rendered/2025/otjob.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 5fe7b4a99a022289e3126ddc426150754204ca00a5b0125120b375b095f9732f |
| lines judged | 1 |
| match / mismatch / unclear / missing | 1 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 106, 107, 108 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 106, 107 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| n-25-69 | Notice 2025-69 (no issue date printed; listed on the IRS Working Families Tax Cuts notices page) | 22, 23, 24, 25 | cited pages | db4956dc478de4c17765edab63a894790718c0e4ba40b904619278f4f63e2667 | - | 9afd51bcb4f5c6848ae5924fcb83f65748da9857f0238574cec9e7a0df2d1837 |

## Lines

### 1(b) — Qualified overtime reported on Form W-2, box 1
Status: **MATCH**

Model: The restatement enters $0 for an employee who is not FLSA-eligible, since overtime paid to "FLSA-ineligible employees is not qualified overtime compensation." Otherwise it uses the amount the employer reported in box 14 or gave on request, or applies methods 1–4 (the premium as shown, total ÷ 3, double-time premium × 1/2, double-time total × 1/4), as in paragraphs 1–4 and Notice 2025-69 (A)–(D). It refuses the reasonable-method estimate, adjustments, other rates and special section 7 rules, and names what it excludes.

## Raw response

```yaml
```yaml
lines:
  - key: "1(b)"
    status: MATCH
    reason: "The restatement enters $0 for an employee who is not FLSA-eligible, since overtime paid to \"FLSA-ineligible employees is not qualified overtime compensation.\" Otherwise it uses the amount the employer reported in box 14 or gave on request, or applies methods 1–4 (the premium as shown, total ÷ 3, double-time premium × 1/2, double-time total × 1/4), as in paragraphs 1–4 and Notice 2025-69 (A)–(D). It refuses the reasonable-method estimate, adjustments, other rates and special section 7 rules, and names what it excludes."
```
```
