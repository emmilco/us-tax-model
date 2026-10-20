# Transcription agreement — se

Second transcription of `Schedule SE (Form 1040) — Self-Employment Tax, one per person` by an isolated model (spec 6.5), compared line by line with `forms/2025/se.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-19 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 1fe20ea5e43d0f6fe591091dbf05df0647babdac34ccf180edb50e1dd67c63d2 |
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
{"amount": {"of": [{"amount": {"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"input": "line2"}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": 10000}, {"amount": {"const": 0}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"const": 0}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"const": 0}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"const": 10000}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"input": "line2"}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"input": "line2"}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, "op": "multiply_rate", "rate": {"param": "se.rate_029"}}, {"amount": {"of": [{"alternatives": [{"guard": {"args": [{"param": "se.floor"}, {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"input": "line2"}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "test": "le"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"const": 10000}, {"amount": {"const": 0}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}], "test": "le"}, "then": {"amount": {"const": 0}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}, {"guard": {"args": [{"amount": {"const": 0}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}, {"const": 10000}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"input": "line2"}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}], "op": "sum"}}, {"guard": {"args": [{"alternatives": [{"guard": {"args": [{"input": "line2"}, {"const": 0}], "test": "le"}, "then": {"input": "line2"}}, {"guard": {"args": [{"const": 0}, {"input": "line2"}], "test": "lt"}, "then": {"amount": {"input": "line2"}, "op": "multiply_rate", "rate": {"param": "se.rate_9235"}}}], "op": "choose"}, {"param": "se.floor"}], "test": "lt"}, "then": {"const": 0}}], "op": "choose"}, {"from": {"param": "se.wage_base"}, "op": "subtract_floor0", "take": {"input": "line8a"}}], "op": "smaller_of"}, "op": "multiply_rate", "rate": {"param": "se.rate_124"}}], "op": "sum"}, "op": "multiply_rate", "rate": {"param": "se.rate_50"}}
```

Ruling: equivalent within scope; project retained. Both multiply line 12 by 50%. The second keeps line 5b (church employee income) as an explicit zero choose and tests line 3 for a profit where the project floors line 2 before the 92.35% multiplication; the project refuses church employee income through person.se_screen (i1040sse, Line 5a). The values agree for every amount on line 2.

## Raw second transcription

```yaml
```yaml
lines:
  - id: se.h_line1a
    printed: "(helper)"
    label: "Net farm profit or (loss) from Schedule F, line 34, and farm partnerships, Schedule K-1 (Form 1065), box 14, code A"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    note: "Open: the tool takes self-employment income only from Schedule C (line2), and no input or screening input exists for farm income. Chosen: line 1a is zero (year parameter sales.zero). No screening input for SE farm income was provided, so this line cannot refuse."
  - id: se.h_line1b
    printed: "(helper)"
    label: "If you received social security retirement or disability benefits, enter the amount of Conservation Reserve Program payments included on Schedule F, line 4b, or listed on Schedule K-1 (Form 1065), box 20, code AQ"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    note: "Open: CRP payments come from Schedule F or a partnership K-1, which the tool does not compute, and no input or screening input exists for them. The form prints this line in parentheses, so it enters line 3 as a negative amount. Chosen: zero."
  - id: se.line3
    printed: "3"
    label: "Combine lines 1a, 1b, and 2"
    type: Dollars
    expr: {op: sum, of: [se.h_line1a, se.h_line1b, line2]}
    note: "Open: the instructions add amounts on the dotted line, such as Chapter 11 bankruptcy income, community income and notary income. Chosen: these are not encoded, because no inputs exist for them."
  - id: se.h_line4a_positive
    printed: "(helper)"
    label: "Line 3 is more than zero"
    type: Bool
    expr: {op: test, gt: [se.line3, {const: 0}]}
  - id: se.h_line4a_product
    printed: "(helper)"
    label: "Multiply line 3 by 92.35% (0.9235)"
    type: Dollars
    expr: {op: multiply_rate, amount: se.line3, rate: {param: se.rate_9235}}
  - id: se.line4a
    printed: "4a"
    label: "If line 3 is more than zero, multiply line 3 by 92.35% (0.9235). Otherwise, enter amount from line 3"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [se.h_line4a_positive, {const: true}]}
          then: se.h_line4a_product
        - guard: {op: test, eq: [se.h_line4a_positive, {const: false}]}
          then: se.line3
  - id: se.line4b
    printed: "4b"
    label: "If you elect one or both of the optional methods, enter the total of lines 15 and 17"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "Open: the tool does not compute the optional methods in Part II, and no election input or screening input exists for them. Chosen: no election, so line 4b is zero."
  - id: se.line4c
    printed: "4c"
    label: "Combine lines 4a and 4b. If less than $400, stop; you don't owe self-employment tax"
    type: Dollars
    expr: {op: sum, of: [se.line4a, se.line4b]}
    note: "Chosen: the stop below $400 is applied at line 6 through the helper se.h_owes, so lines 6 through 13 are zero when line 4c is less than $400. The church-employee-income exception (enter -0- and continue) is not encoded, because church employee income is outside the tool."
  - id: se.h_owes
    printed: "(helper)"
    label: "Line 4c is $400 or more (otherwise stop; you don't owe self-employment tax)"
    type: Bool
    expr: {op: test, ge: [se.line4c, {param: se.floor}]}
  - id: se.h_line5a
    printed: "(helper)"
    label: "Enter your church employee income from Form W-2"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "Open: church employee income is outside the tool, and no input or screening input exists for it. Chosen: zero."
  - id: se.h_line5b_product
    printed: "(helper)"
    label: "Multiply line 5a by 92.35% (0.9235)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: se.h_line5a, rate: {param: se.rate_9235}}
  - id: se.h_line5b_small
    printed: "(helper)"
    label: "Line 5a times 92.35% is less than $100"
    type: Bool
    expr: {op: test, lt: [se.h_line5b_product, {const: 10000}]}
  - id: se.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: se.line5b
    printed: "5b"
    label: "Multiply line 5a by 92.35% (0.9235). If less than $100, enter -0-"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [se.h_line5b_small, {const: true}]}
          then: se.h_zero
        - guard: {op: test, eq: [se.h_line5b_small, {const: false}]}
          then: se.h_line5b_product
  - id: se.h_line6_sum
    printed: "(helper)"
    label: "Add lines 4c and 5b"
    type: Dollars
    expr: {op: sum, of: [se.line4c, se.line5b]}
  - id: se.line6
    printed: "6"
    label: "Add lines 4c and 5b"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [se.h_owes, {const: true}]}
          then: se.h_line6_sum
        - guard: {op: test, eq: [se.h_owes, {const: false}]}
          then: se.h_zero
    note: "Chosen: the stop at line 4c (less than $400, no self-employment tax) is encoded here as zero for line 6 and therefore for lines 10 through 13."
  - id: se.line7
    printed: "7"
    label: "Maximum amount of combined wages and self-employment earnings subject to social security tax or the 6.2% portion of the 7.65% railroad retirement (tier 1) tax for 2025"
    type: NonNegDollars
    expr: {op: param, ref: se.wage_base}
  - id: se.h_line8b
    printed: "(helper)"
    label: "Unreported tips subject to social security tax from Form 4137, line 10"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "Open: the tool does not prepare Form 4137, and no input or screening input exists for it. Chosen: zero."
  - id: se.h_line8c
    printed: "(helper)"
    label: "Wages subject to social security tax from Form 8919, line 10"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "Open: the tool does not prepare Form 8919, and no input or screening input exists for it. Chosen: zero."
  - id: se.line8d
    printed: "8d"
    label: "Add lines 8a, 8b, and 8c"
    type: NonNegDollars
    expr: {op: sum, of: [line8a, se.h_line8b, se.h_line8c]}
  - id: se.line9
    printed: "9"
    label: "Subtract line 8d from line 7. If zero or less, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: se.line7, take: se.line8d}
    note: "Line 8a's instruction to skip lines 8b through 10 when it is $176,100 or more gives the same result as this floor: line 9 is zero, so line 10 is zero."
  - id: se.h_line10_base
    printed: "(helper)"
    label: "The smaller of line 6 or line 9"
    type: NonNegDollars
    expr: {op: smaller_of, of: [se.line6, se.line9]}
  - id: se.line10
    printed: "10"
    label: "Multiply the smaller of line 6 or line 9 by 12.4% (0.124)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: se.h_line10_base, rate: {param: se.rate_124}}
  - id: se.line11
    printed: "11"
    label: "Multiply line 6 by 2.9% (0.029)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: se.line6, rate: {param: se.rate_029}}
  - id: se.line12
    printed: "12"
    label: "Self-employment tax. Add lines 10 and 11"
    type: NonNegDollars
    expr: {op: sum, of: [se.line10, se.line11]}
  - id: se.line13
    printed: "13"
    label: "Deduction for one-half of self-employment tax. Multiply line 12 by 50% (0.50)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: se.line12, rate: {param: se.rate_50}}
  - id: line13
    printed: "(helper)"
    label: "Deduction for one-half of self-employment tax. Multiply line 12 by 50% (0.50)"
    type: NonNegDollars
    expr: {op: copy, from: se.line13}
```
```
