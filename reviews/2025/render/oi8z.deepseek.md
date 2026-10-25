# Render comparison — oi8z

The rendered English of every printed line of `Schedule 1, line 8z — other income, one entry per item listed` (`rendered/2025/oi8z.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | b4a4e26919fbc56fdf4e1fce071f349c5872b6154e98c3d79d85e563b0daa25f |
| prompt policy | render-source-comparison-v2 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | a014c9fd9862c6b21589c58fa436747110bf15cac686d08338ff8d8e81adec74 |
| lines judged | 2 |
| match / mismatch / unclear / missing | 1 / 1 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 92, 93 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 92, 93 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p525 | 2025 | 34 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 34 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

## Lines

### 8z (type) — Type of other income
Status: **MATCH**

Model: The listed categories track the IRS line 8z examples, including RTAA, recoveries, corrective-distribution losses, insurance dividends above net premiums, charitable recapture, disaster relief, Coverdell/QTP distributions, and kickbacks; the Schedule C exclusion for self-employment kickbacks is also stated in Pub. 525.

### 8z (amount) — Amount
Status: **MISMATCH**

Restated: Input — The amount of this item to include in income for 2025

Model: The line is NonNegDollars, but the IRS line 8z examples include a 'Loss on certain corrective distributions of excess deferrals'; a loss cannot be entered as a nonnegative amount to include in income.

Ruling: open

## Raw response

```yaml
lines:
  - key: "8z (type)"
    status: MATCH
    reason: "The listed categories track the IRS line 8z examples, including RTAA, recoveries, corrective-distribution losses, insurance dividends above net premiums, charitable recapture, disaster relief, Coverdell/QTP distributions, and kickbacks; the Schedule C exclusion for self-employment kickbacks is also stated in Pub. 525."
  - key: "8z (amount)"
    status: MISMATCH
    reason: "The line is NonNegDollars, but the IRS line 8z examples include a 'Loss on certain corrective distributions of excess deferrals'; a loss cannot be entered as a nonnegative amount to include in income."
```
