# Transcription agreement — otjob

Second transcription of `Qualified Overtime Compensation From More Than One Employer Worksheet (Schedule 1-A, line 14a) — one row per employer` by an isolated model (spec 6.5), compared line by line with `forms/2025/otjob.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-25 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | d281c181cd4cae12c0c4e7892b05584c811c2200a5b0cc3fc1e4e7849ec8fd01 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | complete-input-context-v1 |
| complete input context | pass |
| type validation policy | project-expression-types-v1 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | edf01867c3eb7f9d68ae0e8d453ccc8889f3e440839bcffcaa42e8a46215fe0a |
| printed lines compared | 2 |
| agree / disagree / missing | 1 / 1 / 0 |
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
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "otjob.flsa"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "otjob.flsa"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "employer_reported"}, {"input": "otjob.method"}], "test": "eq"}, {"args": [{"const": "premium"}, {"input": "otjob.method"}], "test": "eq"}], "test": "any"}, "then": {"input": "otjob.statement"}}, {"guard": {"args": [{"const": "other"}, {"input": "otjob.method"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "premium_double"}, {"input": "otjob.method"}], "test": "eq"}, "then": {"amount": {"input": "otjob.statement"}, "op": "multiply_rate", "rate": {"param": "s1a.ot_half"}}}, {"guard": {"args": [{"const": "total_double"}, {"input": "otjob.method"}], "test": "eq"}, "then": {"amount": {"input": "otjob.statement"}, "op": "multiply_rate", "rate": {"param": "s1a.ot_quarter"}}}, {"guard": {"args": [{"const": "total_time_and_half"}, {"input": "otjob.method"}], "test": "eq"}, "then": {"amount": {"input": "otjob.statement"}, "op": "multiply_rate", "rate": {"param": "s1a.ot_third"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "otjob.flsa"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "otjob.flsa"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "employer_reported"}, {"input": "otjob.method"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "otjob.method"}], "test": "eq"}, {"args": [{"const": "premium"}, {"input": "otjob.method"}], "test": "eq"}], "test": "any"}, "then": {"input": "otjob.statement"}}, {"guard": {"args": [{"const": "premium_double"}, {"input": "otjob.method"}], "test": "eq"}, "then": {"amount": {"input": "otjob.statement"}, "op": "multiply_rate", "rate": {"param": "s1a.ot_half"}}}, {"guard": {"args": [{"const": "total_double"}, {"input": "otjob.method"}], "test": "eq"}, "then": {"amount": {"input": "otjob.statement"}, "op": "multiply_rate", "rate": {"param": "s1a.ot_quarter"}}}, {"guard": {"args": [{"const": "total_time_and_half"}, {"input": "otjob.method"}], "test": "eq"}, "then": {"amount": {"input": "otjob.statement"}, "op": "multiply_rate", "rate": {"param": "s1a.ot_third"}}}], "op": "choose"}}], "op": "choose"}
```

Ruling: representation/scope on admitted methods; i1040gi (2025) pp.106-108 Schedule1-A and Notice2025-69 SectionIII.B.2 give the employer-reported/premium amounts and the one-third, one-half and one-quarter conversions for supported pay statements. Both return zero for FLSA-ineligible employees and the same amount for supported methods. The reply either flattens the FLSA/method guards or uses the statement on method=other. The project refuses special-rule/other methods; no equivalence or admission of that excluded method is claimed. Full partial-input equivalence beyond the declared source cases is not inferred.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 1(b) | otjob.special_rule | otjob.special_rule |

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
        - guard: {op: test, eq: [otjob.flsa, {const: false}]}
          then: otjob.h_zero
        - guard: {op: test, eq: [otjob.flsa, {const: true}]}
          then: otjob.h_figured
  - id: otjob.one
    printed: "(helper)"
    label: "One employer (count)"
    type: Count
    expr: {op: param, ref: person.one}
  - id: otjob.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: otjob.h_by_third
    printed: "(helper)"
    label: "One-third of the statement amount (FLSA Overtime Premium from total time-and-a-half pay)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: otjob.statement, rate: {param: s1a.ot_third}}
  - id: otjob.h_by_half
    printed: "(helper)"
    label: "One-half of the statement amount (FLSA Overtime Premium from pay above regular rate at double time)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: otjob.statement, rate: {param: s1a.ot_half}}
  - id: otjob.h_by_quarter
    printed: "(helper)"
    label: "One-fourth of the statement amount (FLSA Overtime Premium from total double-time pay)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: otjob.statement, rate: {param: s1a.ot_quarter}}
  - id: otjob.h_figured
    printed: "(helper)"
    label: "Qualified overtime compensation for this employer before the FLSA-eligibility check"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [otjob.method, {const: "employer_reported"}]}
          then: otjob.statement
        - guard: {op: test, eq: [otjob.method, {const: "premium"}]}
          then: otjob.statement
        - guard: {op: test, eq: [otjob.method, {const: "total_time_and_half"}]}
          then: otjob.h_by_third
        - guard: {op: test, eq: [otjob.method, {const: "premium_double"}]}
          then: otjob.h_by_half
        - guard: {op: test, eq: [otjob.method, {const: "total_double"}]}
          then: otjob.h_by_quarter
        - guard: {op: test, eq: [otjob.method, {const: "other"}]}
          then: otjob.statement
    refuses: [otjob.special_rule]
    note: "Refuses when otjob.special_rule is true, because the archived text does not supply the alternative FLSA overtime rule computation. For method other, the text permits any reasonable method but does not give a conversion; the supplied full-year statement amount is treated as the qualified overtime compensation for that method."
```
