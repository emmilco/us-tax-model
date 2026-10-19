# Transcription agreement — otjob

Second transcription of `Qualified Overtime Compensation From More Than One Employer Worksheet (Schedule 1-A, line 14a) — one row per employer` by an isolated model (spec 6.5), compared line by line with `forms/2025/otjob.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | b9bed8656c188fb7a1994d585d1f5d6233831ab696cb31ef87c4e57202166884 |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 106, 107, 108 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 106, 107 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| n-25-69 | Notice 2025-69 (no issue date printed; listed on the IRS Working Families Tax Cuts notices page) | 22, 23, 24, 25 | cited pages | db4956dc478de4c17765edab63a894790718c0e4ba40b904619278f4f63e2667 | - | 9afd51bcb4f5c6848ae5924fcb83f65748da9857f0238574cec9e7a0df2d1837 |

## Lines

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

Second transcription's note: Open point: the worksheet column only says 'Qualified overtime reported on Form W-2, box 1'. The amount is figured under 'Determining the amount of qualified overtime compensation for 2025'. A Form W-2 box 14 amount, or an amount the employer gives on request, can be relied on (employer_reported). An FLSA Overtime Premium shown separately is used as is (paragraph 1, premium). The other methods are paragraph 2 (divide by 3), paragraph 3 (one-half at double time) and paragraph 4 (one-fourth at double time). Pay to an employee who is not FLSA-eligible is not qualified overtime compensation, so the line is zero for that employee. The 'other' alternative only keeps the guards exhaustive; it is never reached, because otjob.h_refused stops the line first. Only overtime included in Form W-2, box 1, is entered; the text gives no way to check this, so otjob.statement is taken as that amount.

Ruling: equivalent representation; project retained. Both enter zero for an employee who is not FLSA-eligible and figure the FLSA Overtime Premium by the same methods (the amount as reported, one-third, one-half or one-fourth). The second's 'other' branch is never reached, as its note says, because the refusal (otjob.refused) stops the line first. Its reading that only overtime included in box 1 is entered is resolved by the line 14a instruction, now in the otjob.statement question: overtime not in box 1 is included.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| 1(b) | otjob.h_refused | otjob.h_refused |

## Raw second transcription

```yaml
lines:
  - id: otjob.h_zero
    printed: "(helper)"
    label: "No qualified overtime from this employer"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: otjob.h_by_third
    printed: "(helper)"
    label: "Statement shows the overtime premium and regular wages: divide the total amount by three (3)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: otjob.statement, rate: {param: s1a.ot_third}}

  - id: otjob.h_by_half
    printed: "(helper)"
    label: "Statement shows the portion of the overtime earnings that is more than your regular wage rate, paid at double time: multiply that portion by the appropriate fraction (one-half)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: otjob.statement, rate: {param: s1a.ot_half}}
    note: "Open point: the instructions only say to use 'the appropriate fraction'. Notice 2025-69 (C) gives one-half for double time, which matches Example 2. The tool handles only the double-time version of this method (method premium_double). Any other rate is sent to method 'other' and refused."

  - id: otjob.h_by_quarter
    printed: "(helper)"
    label: "Statement shows the total of all pay for the overtime hours, paid at double time: multiply the total amount by the appropriate fraction (one-fourth)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: otjob.statement, rate: {param: s1a.ot_quarter}}
    note: "Open point: the instructions only say to use 'the appropriate fraction'. Notice 2025-69 (D) gives one-fourth for double time, which matches Example 3 ($20,000 / 2 x 1.5 / 3 = $5,000). The tool handles only the double-time version of this method (method total_double). Any other rate is sent to method 'other' and refused."

  - id: otjob.h_refused
    printed: "(helper)"
    label: "FLSA-eligible employee whose overtime must be figured under a different FLSA section 7 rule, or by a reasonable method (paragraph 5) or an adjusted method, which the tool does not compute"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [otjob.flsa, {const: true}]}
        - op: test
          any:
            - {op: test, eq: [otjob.special_rule, {const: true}]}
            - {op: test, eq: [otjob.method, {const: "other"}]}
    note: "Open point: the instructions say that if an employer is covered by a different overtime rule in section 7, you must figure overtime under that rule and may use any of the methods 'so long as it produces a reasonable result'. Whether a result is reasonable is a judgment the tool cannot check, so these cases are refused. Paragraph 5 (reasonable method) and the adjustment in the TIP (underestimation) are refused the same way, through method 'other'. Nothing is refused for an employee who is not FLSA-eligible, because none of that pay is qualified overtime."

  - id: otjob.line1(b)
    printed: "1(b)"
    label: "Qualified overtime reported on Form W-2, box 1"
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
          then: otjob.h_by_third
        - guard:
            op: test
            all:
              - {op: test, eq: [otjob.flsa, {const: true}]}
              - {op: test, eq: [otjob.method, {const: "premium_double"}]}
          then: otjob.h_by_half
        - guard:
            op: test
            all:
              - {op: test, eq: [otjob.flsa, {const: true}]}
              - {op: test, eq: [otjob.method, {const: "total_double"}]}
          then: otjob.h_by_quarter
        - guard:
            op: test
            all:
              - {op: test, eq: [otjob.flsa, {const: true}]}
              - {op: test, eq: [otjob.method, {const: "other"}]}
          then: otjob.h_zero
    refuses: [otjob.h_refused]
    note: "Open point: the worksheet column only says 'Qualified overtime reported on Form W-2, box 1'. The amount is figured under 'Determining the amount of qualified overtime compensation for 2025'. A Form W-2 box 14 amount, or an amount the employer gives on request, can be relied on (employer_reported). An FLSA Overtime Premium shown separately is used as is (paragraph 1, premium). The other methods are paragraph 2 (divide by 3), paragraph 3 (one-half at double time) and paragraph 4 (one-fourth at double time). Pay to an employee who is not FLSA-eligible is not qualified overtime compensation, so the line is zero for that employee. The 'other' alternative only keeps the guards exhaustive; it is never reached, because otjob.h_refused stops the line first. Only overtime included in Form W-2, box 1, is entered; the text gives no way to check this, so otjob.statement is taken as that amount."
```
