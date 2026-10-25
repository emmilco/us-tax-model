# Transcription agreement — se

Second transcription of `Schedule SE (Form 1040) — Self-Employment Tax, one per person` by an isolated model (spec 6.5), compared line by line with `forms/2025/se.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-25 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | e002b9c98bbe7d31c192760197701a2e268dae128f7f2289fb13e224f23cc924 |
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
| subject sha256 | 0c850519b95a0d9a45ff9abb2ddb129d2a5755507a6929f64bfcc1024f606a73 |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |

## Lines

### line13 — Deduction for one-half of self-employment tax. Multiply line 12 by 50% (0.50)
Status: **DISAGREE**

Project:

```json
{"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"from": {"input": "line2"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"from": {"input": "line2"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"from": {"input": "line2"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"from": {"input": "line2"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"from": {"input": "line2"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"from": {"input": "line2"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"input": "line8a"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}
```

Second:

```json
{"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"const": 40000}, {"from": {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"input": "line2"}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"input": "line2"}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"input": "line2"}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, {"const": 40000}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"const": 40000}, {"from": {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"input": "line2"}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "test": "le"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"input": "line2"}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"input": "line2"}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, {"const": 40000}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"input": "line8a"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}
```

Ruling: representation of the exported deduction; f1040sse (2025) p.1 line4c says STOP below$400, with no church employee income in the admitted slice. The returned transcription applies that STOP at line6 rather than on its intermediate line4c, making lines10-13 zero in precisely the stopped cases. Above the threshold both use the same92.35%, wage-base floor,12.4%,2.9% and50% operations. The project floor before the positive-line3 multiplication is also redundant under that branch guard. This adjudicates the exported line13 result only, not identical intermediate printed values in a stopped worksheet. The fresh response passes expression checks.

## Raw second transcription

```yaml
lines:
  - id: line3
    printed: "3"
    label: "Combine lines 1a, 1b, and 2"
    type: Dollars
    expr: {op: copy, from: line2}
    note: "Lines 1a and 1b (farm income and CRP payments) are outside this slice; line 3 therefore equals the supplied Schedule C result on line 2."

  - id: line4a
    printed: "4a"
    label: "If line 3 is more than zero, multiply line 3 by 92.35% (0.9235). Otherwise, enter amount from line 3"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, gt: [line3, {const: 0}]}
          then: se.h_4a_product
        - guard: {op: test, le: [line3, {const: 0}]}
          then: line3

  - id: line4b
    printed: "4b"
    label: "If you elect one or both of the optional methods, enter the total of lines 15 and 17 here"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    note: "The optional methods of Part II are outside this slice, so no amount is added here."

  - id: line4c
    printed: "4c"
    label: "Combine lines 4a and 4b. If less than $400, stop; you don’t owe self-employment tax. Exception: If less than $400 and you had church employee income, enter -0- and continue"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: se.h_4c_combined, take: {const: 0}}
    note: "Line 4c is declared NonNegDollars, so a negative combined amount is floored at zero. The church employee income exception is outside this slice."

  - id: line5b
    printed: "5b"
    label: "Multiply line 5a by 92.35% (0.9235). If less than $100, enter -0-."
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
    note: "Line 5a (church employee income) is outside this slice, so line 5b is zero."

  - id: line6
    printed: "6"
    label: "Add lines 4c and 5b"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, ge: [line4c, {const: 40000}]}
          then: se.h_4c_5b
        - guard: {op: test, lt: [line4c, {const: 40000}]}
          then: se.h_zero
    note: "When line 4c is less than $400 and there is no church employee income, the IRS says to stop; line 6 is shown as zero so the downstream tax is zero."

  - id: line7
    printed: "7"
    label: "Maximum amount of combined wages and self-employment earnings subject to social security tax or the 6.2% portion of the 7.65% railroad retirement (tier 1) tax for 2025"
    type: NonNegDollars
    expr: {op: param, ref: se.wage_base}

  - id: line8d
    printed: "8d"
    label: "Add lines 8a, 8b, and 8c"
    type: NonNegDollars
    expr: {op: copy, from: line8a}
    note: "Lines 8b and 8c (Form 4137 unreported tips and Form 8919 wages) are outside this slice; line 8d therefore equals the supplied line 8a amount."

  - id: line9
    printed: "9"
    label: "Subtract line 8d from line 7. If zero or less, enter -0- here and on line 10 and go to line 11"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: line7, take: line8d}

  - id: line10
    printed: "10"
    label: "Multiply the smaller of line 6 or line 9 by 12.4% (0.124)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: se.h_smaller_6_9, rate: {param: se.rate_124}}

  - id: line11
    printed: "11"
    label: "Multiply line 6 by 2.9% (0.029)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: line6, rate: {param: se.rate_029}}

  - id: line12
    printed: "12"
    label: "Self-employment tax. Add lines 10 and 11. Enter here and on Schedule 2 (Form 1040), line 4, or Form 1040-SS, Part I, line 3"
    type: NonNegDollars
    expr: {op: sum, of: [line10, line11]}

  - id: line13
    printed: "13"
    label: "Deduction for one-half of self-employment tax. Multiply line 12 by 50% (0.50). Enter here and on Schedule 1 (Form 1040), line 15"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: line12, rate: {param: se.rate_50}}

  - id: se.h_4a_product
    printed: "(helper)"
    label: "Line 4a product"
    type: Dollars
    expr: {op: multiply_rate, amount: line3, rate: {param: se.rate_9235}}

  - id: se.h_4c_combined
    printed: "(helper)"
    label: "Combined lines 4a and 4b before the nonnegative floor"
    type: Dollars
    expr: {op: sum, of: [line4a, line4b]}

  - id: se.h_4c_5b
    printed: "(helper)"
    label: "Combined lines 4c and 5b"
    type: NonNegDollars
    expr: {op: sum, of: [line4c, line5b]}

  - id: se.h_zero
    printed: "(helper)"
    label: "Zero amount"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: se.h_smaller_6_9
    printed: "(helper)"
    label: "Smaller of line 6 or line 9"
    type: NonNegDollars
    expr: {op: smaller_of, of: [line6, line9]}
```
