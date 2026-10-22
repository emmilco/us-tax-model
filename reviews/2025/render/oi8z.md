# Render comparison — oi8z

The rendered English of every printed line of `Schedule 1, line 8z — other income, one entry per item listed` (`rendered/2025/oi8z.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | b4a4e26919fbc56fdf4e1fce071f349c5872b6154e98c3d79d85e563b0daa25f |
| subject sha256 | a014c9fd9862c6b21589c58fa436747110bf15cac686d08338ff8d8e81adec74 |
| lines judged | 2 |
| match / mismatch / unclear / missing | 2 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 92, 93 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 92, 93 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p525 | 2025 | 34 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 34 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

## Lines

### 8z (type) — Type of other income
Status: **MATCH**

Model: Each category follows the i1040gi line 8z examples: recoveries, RTAA payments in 'box 5 of Form 1099-G', loss on corrective distributions, insurance dividends that 'exceed the total of all net premiums', both charitable recaptures, the taxable part of disaster relief, and taxable Coverdell ESA/QTP distributions. Kickbacks and the Schedule C carve-out follow Pub. 525, and 'other' covers 'any taxable income not reported elsewhere.' The note that a state or local income tax refund belongs on line 1 is not stated in the text given, but it does not change the value and fits 'not reported elsewhere on your return.'

### 8z (amount) — Amount
Status: **MATCH**

Model: The instructions say to 'List the type and amount of income' for each item, and only taxable amounts belong here ('Don't report any nontaxable income on line 8z'). Entering the amount to include in 2025 income matches. The text given does not say whether the corrective-distribution 'loss' item could be negative, which the non-negative type would exclude.

## Raw response

```yaml
```yaml
lines:
  - key: "8z (type)"
    status: MATCH
    reason: "Each category follows the i1040gi line 8z examples: recoveries, RTAA payments in 'box 5 of Form 1099-G', loss on corrective distributions, insurance dividends that 'exceed the total of all net premiums', both charitable recaptures, the taxable part of disaster relief, and taxable Coverdell ESA/QTP distributions. Kickbacks and the Schedule C carve-out follow Pub. 525, and 'other' covers 'any taxable income not reported elsewhere.' The note that a state or local income tax refund belongs on line 1 is not stated in the text given, but it does not change the value and fits 'not reported elsewhere on your return.'"
  - key: "8z (amount)"
    status: MATCH
    reason: "The instructions say to 'List the type and amount of income' for each item, and only taxable amounts belong here ('Don't report any nontaxable income on line 8z'). Entering the amount to include in 2025 income matches. The text given does not say whether the corrective-distribution 'loss' item could be negative, which the non-negative type would exclude."
```
```
