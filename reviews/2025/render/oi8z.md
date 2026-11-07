# Render comparison — oi8z

The rendered English of every printed line of `Schedule 1, line 8z — other income, one entry per item listed` (`rendered/2025/oi8z.md`) read against the archived IRS pages by an isolated model that saw the rendering and the pages, not the YAML (spec 6.5).

| field | value |
| --- | --- |
| date | 2026-10-22 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
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

Model: Each kind matches an IRS line 8z example. RTAA is 'shown in box 5 of Form 1099-G'. Recoveries are 'Reimbursements or other amounts received for items deducted in an earlier year'. Corrective distributions are 'Loss on certain corrective distributions of excess deferrals'. Insurance dividends are 'if they exceed the total of all net premiums'. Both charitable recaptures (fractional interest, and disposal 'within 3 years') are covered, as are disaster relief, Coverdell/QTP distributions and kickbacks (Pub. 525: line 8z 'or on Schedule C … if from your self-employment activity'), with 'other' covering 'any taxable income not reported elsewhere'. The note sending state or local income tax refunds to line 1 is not in the text given, but it fits the 'not reported elsewhere' rule and does not change what goes on line 8z.
Reviewed in: pass 5abfb5aec596

### 8z (amount) — Amount
Status: **MATCH**

Model: The instructions say to 'List the type and amount of income' for each item, and only taxable amounts belong here ('Don't report any nontaxable income on line 8z'). Entering the amount to include in 2025 income matches. The text given does not say whether the corrective-distribution 'loss' item could be negative, which the non-negative type would exclude.

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
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 5abfb5aec596fec9670bf236492ecc8d8603c7ce641b87a457b2855d88911e3b |
| prompt policy | render-source-comparison-v2+lines-v1 |
| system sha256 | 95fdbb6e2ec61299b6c8deeca3dcf777c61b335eedb7c76706029f6ec83081e4 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | e9c691c41fc2cfb741649a63df8371cf90905dc9e8d6cc22ebc0e3245d7f501b |
| receipt | .transcription/oi8z.render.lines-180d5a4918ae |
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
```yaml
lines:
  - key: "8z (type)"
    status: MATCH
    reason: "Each kind matches an IRS line 8z example. RTAA is 'shown in box 5 of Form 1099-G'. Recoveries are 'Reimbursements or other amounts received for items deducted in an earlier year'. Corrective distributions are 'Loss on certain corrective distributions of excess deferrals'. Insurance dividends are 'if they exceed the total of all net premiums'. Both charitable recaptures (fractional interest, and disposal 'within 3 years') are covered, as are disaster relief, Coverdell/QTP distributions and kickbacks (Pub. 525: line 8z 'or on Schedule C … if from your self-employment activity'), with 'other' covering 'any taxable income not reported elsewhere'. The note sending state or local income tax refunds to line 1 is not in the text given, but it fits the 'not reported elsewhere' rule and does not change what goes on line 8z."
```
```

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
