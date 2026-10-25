# Transcription agreement — otjob

Second transcription of `Qualified Overtime Compensation From More Than One Employer Worksheet (Schedule 1-A, line 14a) — one row per employer` by an isolated model (spec 6.5), compared line by line with `forms/2025/otjob.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-25 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | d281c181cd4cae12c0c4e7892b05584c811c2200a5b0cc3fc1e4e7849ec8fd01 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | complete-input-context-v1 |
| complete input context | pass |
| type validation policy | project-expression-types-v1 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
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
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "employer_reported"}, {"input": "otjob.method"}], "test": "eq"}, {"args": [{"const": "premium"}, {"input": "otjob.method"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "otjob.flsa"}], "test": "eq"}], "test": "all"}, "then": {"input": "otjob.statement"}}, {"guard": {"args": [{"args": [{"const": "premium_double"}, {"input": "otjob.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "otjob.flsa"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "otjob.statement"}, "op": "multiply_rate", "rate": {"param": "s1a.ot_half"}}}, {"guard": {"args": [{"args": [{"const": "total_double"}, {"input": "otjob.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "otjob.flsa"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "otjob.statement"}, "op": "multiply_rate", "rate": {"param": "s1a.ot_quarter"}}}, {"guard": {"args": [{"args": [{"const": "total_time_and_half"}, {"input": "otjob.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "otjob.flsa"}], "test": "eq"}], "test": "all"}, "then": {"amount": {"input": "otjob.statement"}, "op": "multiply_rate", "rate": {"param": "s1a.ot_third"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "other"}, {"input": "otjob.method"}], "test": "eq"}, {"args": [{"const": true}, {"input": "otjob.flsa"}], "test": "eq"}], "test": "all"}, {"args": [{"const": false}, {"input": "otjob.flsa"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Qualified overtime must be paid to an FLSA-eligible employee. Overtime paid to an FLSA-ineligible employee 'is not qualified overtime compensation', so that case is zero. An employer-reported amount (Form W-2 box 14, or an amount given on request) 'can generally rely on', and the paragraph 1 premium, are used as shown. The 'other' branch is zero only to keep the guards exhaustive; that case is always refused through otjob.h_refused and never used. The worksheet heading says 'reported on Form W-2, box 1', but the line 14a text adds overtime not included in box 1 (for example deferred overtime). The statement input includes that amount, so it is read as included.

Ruling: representation/scope on admitted methods; i1040gi (2025) pp.106-108 Schedule1-A and Notice2025-69 SectionIII.B.2 give the employer-reported/premium amounts and the one-third, one-half and one-quarter conversions for supported pay statements. Both return zero for FLSA-ineligible employees and the same amount for supported methods. The reply either flattens the FLSA/method guards or uses the statement on method=other. The project refuses special-rule/other methods; no equivalence or admission of that excluded method is claimed. Full partial-input equivalence beyond the declared source cases is not inferred.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 1(b) | otjob.h_refused | otjob.h_refused |

## Raw second transcription

```yaml
```yaml
lines:
  - id: otjob.one
    printed: "(helper)"
    label: "One employer (counts this row of the Qualified Overtime Compensation From More Than One Employer Worksheet, lines 1A through 1E)"
    type: Count
    expr: {op: param, ref: person.one}
    note: "The IRS pages do not define this interface. Read as the count of one for this employer row, used to count the worksheet's employer rows (lines 1A to 1E). No otjob-specific count parameter is supplied, so the value 1 comes from the Count parameter person.one."
  - id: otjob.h_zero
    printed: "(helper)"
    label: "Zero (no qualified overtime compensation from this employer)"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: otjob.h_refused
    printed: "(helper)"
    label: "The tool cannot figure this employer's qualified overtime: the employer is covered by an FLSA overtime rule other than section 7(a), or a method other than paragraphs 1 to 4 (or an employer-reported amount) is used"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [otjob.flsa, {const: true}]}
        - op: test
          any:
            - {op: test, eq: [otjob.special_rule, {const: true}]}
            - {op: test, eq: [otjob.method, {const: "other"}]}
    note: "Under the instructions, an employer covered by a section 7 rule other than 7(a) requires computing overtime under that rule. The paragraph methods may be used only 'so long as it produces a reasonable result under the rule that applies to you' (Notice 2025-69 (G)). Paragraph 5 is a 'reasonable method' based on the regular rate and hours (Notice (F)), and so is the adjustment in the TIP and Notice (E). The tool cannot verify any of these, so it refuses them. This applies only for FLSA-eligible employees, because for anyone else the amount is not qualified overtime compensation at all."
  - id: otjob.h_third
    printed: "(helper)"
    label: "Total of all wages for the overtime hours divided by three (paragraph 2)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: otjob.statement, rate: {param: s1a.ot_third}}
  - id: otjob.h_half
    printed: "(helper)"
    label: "Portion of overtime earnings above the regular wage rate, overtime paid at double time, multiplied by the appropriate fraction, one-half (paragraph 3)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: otjob.statement, rate: {param: s1a.ot_half}}
    note: "The instructions say 'the appropriate fraction' and Notice 2025-69 (C) gives one-half for double time. Example 2 is consistent: $10,000 of premium gives $5,000. The tool supports only double time; other rates fall under 'other' and are refused."
  - id: otjob.h_quarter
    printed: "(helper)"
    label: "Total of all pay for the overtime hours, overtime paid at double time, multiplied by the appropriate fraction, one-fourth (paragraph 4)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: otjob.statement, rate: {param: s1a.ot_quarter}}
    note: "Notice 2025-69 (D) gives one-fourth for double time. Example 3 is consistent: $20,000 of total pay gives $5,000."
  - id: otjob.col_b
    printed: "1(b)"
    label: "Qualified overtime reported on Form W-2, box 1 (including qualified overtime compensation not included in box 1 of Form W-2, for example overtime amounts deferred under a qualified retirement plan)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [otjob.flsa, {const: false}]}
          then: otjob.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [otjob.flsa, {const: true}]}
              - op: test
                any:
                  - {op: test, eq: [otjob.method, {const: "employer_reported"}]}
                  - {op: test, eq: [otjob.method, {const: "premium"}]}
          then: otjob.statement
        - guard:
            op: test
            all:
              - {op: test, eq: [otjob.flsa, {const: true}]}
              - {op: test, eq: [otjob.method, {const: "total_time_and_half"}]}
          then: otjob.h_third
        - guard:
            op: test
            all:
              - {op: test, eq: [otjob.flsa, {const: true}]}
              - {op: test, eq: [otjob.method, {const: "premium_double"}]}
          then: otjob.h_half
        - guard:
            op: test
            all:
              - {op: test, eq: [otjob.flsa, {const: true}]}
              - {op: test, eq: [otjob.method, {const: "total_double"}]}
          then: otjob.h_quarter
        - guard:
            op: test
            all:
              - {op: test, eq: [otjob.flsa, {const: true}]}
              - {op: test, eq: [otjob.method, {const: "other"}]}
          then: otjob.h_zero
    refuses: [otjob.h_refused]
    note: "Qualified overtime must be paid to an FLSA-eligible employee. Overtime paid to an FLSA-ineligible employee 'is not qualified overtime compensation', so that case is zero. An employer-reported amount (Form W-2 box 14, or an amount given on request) 'can generally rely on', and the paragraph 1 premium, are used as shown. The 'other' branch is zero only to keep the guards exhaustive; that case is always refused through otjob.h_refused and never used. The worksheet heading says 'reported on Form W-2, box 1', but the line 14a text adds overtime not included in box 1 (for example deferred overtime). The statement input includes that amount, so it is read as included."
```
```
