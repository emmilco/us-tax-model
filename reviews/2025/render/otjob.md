# Render comparison — otjob

The rendered English of every printed line of `Qualified Overtime Compensation From More Than One Employer Worksheet (Schedule 1-A, line 14a) — one row per employer` (`rendered/2025/otjob.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | e625ac4a03d54c3b124d721cbbbc7084bc5cd64bd8fa7a06e582d75f7964c9e3 |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | e2721cf8506da1b69c5a83dee7008cdd3fdeb8551f04a26a506a965f68659361 |
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

Model: The text says qualified overtime must be paid to an FLSA-eligible employee, so entering $0 when the filer is not eligible is right. For an eligible filer, the program allows the employer's box 14 or on-request amount, the separately shown FLSA Overtime Premium (method 1), total overtime pay ÷ 3 (method 2), and the double-time fractions of one-half and one-fourth (methods 3 and 4). It also includes overtime not in box 1 ("enter that amount here"). The refusal names the cases it leaves out: reasonable-method estimates, other overtime rates and special section 7 rules.

## Raw response

```yaml
lines:
  - key: "1(b)"
    status: MATCH
    reason: "The text says qualified overtime must be paid to an FLSA-eligible employee, so entering $0 when the filer is not eligible is right. For an eligible filer, the program allows the employer's box 14 or on-request amount, the separately shown FLSA Overtime Premium (method 1), total overtime pay ÷ 3 (method 2), and the double-time fractions of one-half and one-fourth (methods 3 and 4). It also includes overtime not in box 1 (\"enter that amount here\"). The refusal names the cases it leaves out: reasonable-method estimates, other overtime rates and special section 7 rules."
```
