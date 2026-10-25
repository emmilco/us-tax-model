# Render comparison — otjob

The rendered English of every printed line of `Qualified Overtime Compensation From More Than One Employer Worksheet (Schedule 1-A, line 14a) — one row per employer` (`rendered/2025/otjob.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | dc033648850121e23c70671204ec9c4ce848708225343b3390b4ae3de86644c4 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | 0c8625ff1305a43dc91f9975f63aeae7e8cd9091a03cc32579cf0ea8f4707e1d |
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

Model: The IRS line asks for qualified overtime compensation reported on Form W-2, box 1; qualified overtime is the FLSA overtime premium, and the restatement computes that premium by the chosen allowed method, with zero when the employee is not FLSA-eligible.

## Raw response

```yaml
lines:
  - key: "1(b)"
    status: MATCH
    reason: "The IRS line asks for qualified overtime compensation reported on Form W-2, box 1; qualified overtime is the FLSA overtime premium, and the restatement computes that premium by the chosen allowed method, with zero when the employee is not FLSA-eligible."
```
