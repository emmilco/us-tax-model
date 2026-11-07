# Render comparison — oi8z

The rendered English of every printed line of `Schedule 1, line 8z — other income, one entry per item listed` (`rendered/2025/oi8z.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-23 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
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

Model: The enum categories track the line 8z examples—recoveries, RTAA, corrective distributions, insurance dividends, charitable recapture, disaster relief, and ESA/QTP distributions—and Pub. 525’s kickback treatment; the “other” catch-all matches “any taxable income not reported elsewhere.”
Reviewed in: pass 5abfb5aec596

### 8z (amount) — Amount
Status: **MISMATCH**

Restated: Input — The amount of this item to include in income for 2025

Model: The line is NonNegDollars, but the IRS line 8z examples include a 'Loss on certain corrective distributions of excess deferrals'; a loss cannot be entered as a nonnegative amount to include in income.

Ruling: open

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| 8z (type) | b17bb335f519ea7e57a1b5f86b47fad0219f96a9f0866844ee10335c2ed19a81 |
| 8z (amount) | d08a0d16f93c9b413a4c926f1ba4dcfea4bf4a30e6a3cd45485b5fdbca2076cf |
| (rest of the document) | 88bff9466958832063aaa5eb6d014d9f7e1967406a1c16d9a33bbdc8e315f9de |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 5abfb5aec596

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines 8z (type) |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 5abfb5aec596fec9670bf236492ecc8d8603c7ce641b87a457b2855d88911e3b |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | 65536 |
| subject sha256 | e9c691c41fc2cfb741649a63df8371cf90905dc9e8d6cc22ebc0e3245d7f501b |
| receipt | .transcription/oi8z.deepseek.render.lines-180d5a4918ae |
| lines judged | 1 |
| match / mismatch / unclear / missing | 1 / 0 / 0 / 0 |
| verdicts for lines not in the form | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 92 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 92 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p525 | 2025 | 34 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 34 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

##### Raw response

```yaml
lines:
  - key: "8z (type)"
    status: MATCH
    reason: "The enum categories track the line 8z examples—recoveries, RTAA, corrective distributions, insurance dividends, charitable recapture, disaster relief, and ESA/QTP distributions—and Pub. 525’s kickback treatment; the “other” catch-all matches “any taxable income not reported elsewhere.”"
```

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
