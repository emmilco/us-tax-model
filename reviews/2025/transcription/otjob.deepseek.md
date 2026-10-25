# Transcription agreement — otjob

Second transcription of `Qualified Overtime Compensation From More Than One Employer Worksheet (Schedule 1-A, line 14a) — one row per employer` by an isolated model (spec 6.5), compared line by line with `forms/2025/otjob.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-24 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 4535973f8b53943253d1de0476aebb4c7eee53abc8990b19626bdf4a7d93e7a9 |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | max |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | edf01867c3eb7f9d68ae0e8d453ccc8889f3e440839bcffcaa42e8a46215fe0a |
| printed lines compared | 2 |
| agree / disagree / missing | 2 / 0 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 106, 107, 108 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 106, 107 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| n-25-69 | Notice 2025-69 (no issue date printed; listed on the IRS Working Families Tax Cuts notices page) | 22, 23, 24, 25 | cited pages | db4956dc478de4c17765edab63a894790718c0e4ba40b904619278f4f63e2667 | - | 9afd51bcb4f5c6848ae5924fcb83f65748da9857f0238574cec9e7a0df2d1837 |

## Lines

### otjob.one — One employer entry
Status: **AGREE**

### 1(b) — Qualified overtime reported on Form W-2, box 1
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 1(b) | otjob.refused | - |

## Raw second transcription

```yaml
lines:
  - id: otjob.col_b
    printed: "1(b)"
    label: "Qualified overtime reported on Form W-2, box 1"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq:
              - otjob.flsa
              - const: true
          then: otjob.figured
        - guard:
            op: test
            eq:
              - otjob.flsa
              - const: false
          then: otjob.zero
    refuses: [otjob.refused]
    note: "The IRS worksheet prints only column (b); the per-employer computation comes from the instructions' methods. The tool enters zero when the employer is not FLSA-eligible and refuses a special FLSA overtime rule or a method other than the listed methods."
  - id: otjob.one
    printed: "(helper)"
    label: "One employer"
    type: Count
    expr: {op: param, ref: person.one}
  - id: otjob.zero
    printed: "(helper)"
    label: "Zero amount"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: otjob.by_third
    printed: "(helper)"
    label: "One third of the statement amount (method 2: total wages for overtime hours)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: otjob.statement
      rate: {param: s1a.ot_third}
  - id: otjob.by_half
    printed: "(helper)"
    label: "One half of the excess overtime premium (method 3: double-time pay above the regular rate)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: otjob.statement
      rate: {param: s1a.ot_half}
  - id: otjob.by_quarter
    printed: "(helper)"
    label: "One quarter of the total overtime pay (method 4: double-time total pay)"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: otjob.statement
      rate: {param: s1a.ot_quarter}
  - id: otjob.figured
    printed: "(helper)"
    label: "Qualified overtime computed for this employer under the chosen method"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq:
              - otjob.method
              - const: "employer_reported"
          then: otjob.statement
        - guard:
            op: test
            eq:
              - otjob.method
              - const: "premium"
          then: otjob.statement
        - guard:
            op: test
            eq:
              - otjob.method
              - const: "total_time_and_half"
          then: otjob.by_third
        - guard:
            op: test
            eq:
              - otjob.method
              - const: "premium_double"
          then: otjob.by_half
        - guard:
            op: test
            eq:
              - otjob.method
              - const: "total_double"
          then: otjob.by_quarter
        - guard:
            op: test
            eq:
              - otjob.method
              - const: "other"
          then: otjob.zero
  - id: otjob.refused
    printed: "(gate)"
    label: "Gate: this employer requires a special FLSA overtime rule or a method the tool does not support"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          eq:
            - otjob.special_rule
            - const: true
        - op: test
          eq:
            - otjob.method
            - const: "other"
    note: "The IRS text permits any reasonable method under a special FLSA overtime rule and permits a reasonable method when the statement does not show the overtime premium. The tool does not compute those cases."
```
