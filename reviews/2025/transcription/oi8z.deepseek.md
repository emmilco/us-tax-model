# Transcription agreement — oi8z

Second transcription of `Schedule 1, line 8z — other income, one entry per item listed` by an isolated model (spec 6.5), compared line by line with `forms/2025/oi8z.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 2aec39b00b25204f9eea60b3af13f348ddbe94d664c3cd80d28f9ba600a74f88 |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 0a3972a97621761568f216084d2c414b170914aa8b5e5d68ee32d22416a36b94 |
| printed lines compared | 1 |
| agree / disagree / missing | 1 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 92, 93 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 92, 93 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p525 | 2025 | 34 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 34 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

## Lines

### oi8z.taxable — The amount of this item included on line 8z
Status: **AGREE**

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| oi8z.taxable | ad038942e2cfbe737c83a207437ba13f15e8ad9a97d680d2e88144e80b9cb03b |
| (rest of the document) | 9b11cc29785845924b626fad6f7f0a62bdf1f9b626cc1aab9a2c543ecad4736e |

## Raw second transcription

```yaml
lines:
  - id: oi8z.taxable
    printed: "(helper)"
    label: "Taxable amount of this line 8z item"
    type: NonNegDollars
    expr: {op: copy, from: oi8z.amount}
```
