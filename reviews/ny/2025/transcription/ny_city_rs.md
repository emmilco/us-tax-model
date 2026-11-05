# Transcription agreement — ny_city_rs

Second transcription of `New York City tax rate schedule` by an isolated model (spec 6.5), compared line by line with `forms/ny/2025/ny_city_rs.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-04 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 1f70e87fa67155f76aed617d6c150881e4e81103ed81116eca8cadf00bb87c3f |
| prompt policy | source-only-computation-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 0d742581b323e1a2741bcada92d16f3f0f210bf549dc499896e393679717255f |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | 83e9ed0ae4edc40db4c301ed52bf00d46afb0b4bd30dea929e35960993911093 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 2b37dbe2f4fa141641dd17385b15dacc57c6f524bc45d4928b736ce32a5b911a |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i-html | Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny) | 1 | cited sections: New York City tax rate schedule | 63863fe461c33d052e26a67c87d000ed70b896c72437350880a9e1c680104982 | - | - |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 4 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 4 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |

## Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | ny_rs, ny_tcw, ny_tcw_first |
| shared page | ny_it201 |

## Lines

### tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"input": "amount"}], "test": "le"}, {"args": [{"input": "amount"}, {"param": "ny.city.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.city.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.city.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.city.mfj.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.city.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b2.rate"}, "unit": 100}, {"param": "ny.city.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.city.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.city.mfj.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.city.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b3.rate"}, "unit": 100}, {"param": "ny.city.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.city.mfj.b3.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.city.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b4.rate"}, "unit": 100}, {"param": "ny.city.mfj.b4.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"input": "amount"}], "test": "le"}, {"args": [{"input": "amount"}, {"param": "ny.city.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.city.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.city.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.city.single.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.city.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b2.rate"}, "unit": 100}, {"param": "ny.city.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.city.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.city.single.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.city.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b3.rate"}, "unit": 100}, {"param": "ny.city.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.city.single.b3.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.city.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b4.rate"}, "unit": 100}, {"param": "ny.city.single.b4.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"input": "amount"}], "test": "le"}, {"args": [{"input": "amount"}, {"param": "ny.city.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.city.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.city.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.city.hoh.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.city.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b2.rate"}, "unit": 100}, {"param": "ny.city.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.city.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.city.hoh.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.city.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b3.rate"}, "unit": 100}, {"param": "ny.city.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.city.hoh.b3.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.city.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b4.rate"}, "unit": 100}, {"param": "ny.city.hoh.b4.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.city.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.city.mfj.b2.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.city.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b2.rate"}}, {"param": "ny.city.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.city.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.city.mfj.b3.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.city.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b3.rate"}}, {"param": "ny.city.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"input": "amount"}, {"param": "ny.city.mfj.b1.upper"}], "test": "le"}, "then": {"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.city.b1.rate"}}}, {"guard": {"args": [{"param": "ny.city.mfj.b4.over"}, {"input": "amount"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.city.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b4.rate"}}, {"param": "ny.city.mfj.b4.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.city.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.city.single.b2.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.city.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b2.rate"}}, {"param": "ny.city.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.city.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.city.single.b3.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.city.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b3.rate"}}, {"param": "ny.city.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"input": "amount"}, {"param": "ny.city.single.b1.upper"}], "test": "le"}, "then": {"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.city.b1.rate"}}}, {"guard": {"args": [{"param": "ny.city.single.b4.over"}, {"input": "amount"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.city.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b4.rate"}}, {"param": "ny.city.single.b4.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.city.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.city.hoh.b2.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.city.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b2.rate"}}, {"param": "ny.city.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.city.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.city.hoh.b3.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.city.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b3.rate"}}, {"param": "ny.city.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"input": "amount"}, {"param": "ny.city.hoh.b1.upper"}], "test": "le"}, "then": {"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.city.b1.rate"}}}, {"guard": {"args": [{"param": "ny.city.hoh.b4.over"}, {"input": "amount"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.city.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.city.b4.rate"}}, {"param": "ny.city.hoh.b4.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}
```

Second transcription's note: The schedule assigns filing status ② and ⑤ (married filing jointly, qualifying surviving spouse) to the first schedule. It assigns ① and ③ (single, married filing separately) to the second and ④ (head of household) to the third. The schedule does not state any rounding of the result to whole dollars, so none is applied.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; IT-201-I p. 7, "Enter only whole dollar amounts on your New York return."; p. 2, "Increase amounts that are 50 cents or more to the next dollar."). Evaluated on a grid of whole-dollar amounts for every status (scratch evaluator, params/ny/2025.yaml): the reply differs from the project only by the cents of the band product, never more than 50 cents; the bands' "over" amounts equal the previous bands' upper limits, so the reordered guards select the same band.

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| tax | 1375f6457f620b10ddc65ea24a408dfb6d075a751a59f7e4d39a2a8e8f25a1c5 |
| (rest of the document) | c7c692de84a1a626df677d175d6b407414322e8610a485411895dfd2800f052c |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| tax | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |

## Raw second transcription

```yaml
```yaml
lines:
  - id: single.b1.excess
    printed: "(band 1) (single.b1.excess)"
    label: "Single and married filing separately—filing status ① and ③: If line 47 is over $0 but not over $12,000: line 47"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.city.single.b1.over}}
  - id: single.b1.product
    printed: "(band 1) (single.b1.product)"
    label: "3.078% of line 47"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: single.b1.excess, rate: {param: ny.city.b1.rate}}
    note: "The schedule does not say how to round the product. Chosen: half-up to the cent."
  - id: single.b1.base
    printed: "(band 1) (single.b1.base)"
    label: "(no fixed amount printed for the first band)"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.single.b1.base}
  - id: single.b1.tax
    printed: "The tax is (single.b1.tax)"
    label: "The tax is: 3.078% of line 47"
    type: NonNegDollars
    expr: {op: sum, of: [single.b1.base, single.b1.product]}
  - id: single.b2.excess
    printed: "(band 2) (single.b2.excess)"
    label: "If line 47 is over 12,000 but not over 25,000: the excess over $12,000"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.city.single.b2.over}}
  - id: single.b2.product
    printed: "(band 2) (single.b2.product)"
    label: "3.762% of the excess over $12,000"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: single.b2.excess, rate: {param: ny.city.b2.rate}}
  - id: single.b2.base
    printed: "(band 2) (single.b2.base)"
    label: "$369"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.single.b2.base}
  - id: single.b2.tax
    printed: "The tax is (single.b2.tax)"
    label: "The tax is: $369 plus 3.762% of the excess over $12,000"
    type: NonNegDollars
    expr: {op: sum, of: [single.b2.base, single.b2.product]}
  - id: single.b3.excess
    printed: "(band 3) (single.b3.excess)"
    label: "If line 47 is over 25,000 but not over 50,000: the excess over 25,000"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.city.single.b3.over}}
  - id: single.b3.product
    printed: "(band 3) (single.b3.product)"
    label: "3.819% of the excess over 25,000"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: single.b3.excess, rate: {param: ny.city.b3.rate}}
  - id: single.b3.base
    printed: "(band 3) (single.b3.base)"
    label: "858"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.single.b3.base}
  - id: single.b3.tax
    printed: "The tax is (single.b3.tax)"
    label: "The tax is: 858 plus 3.819% of the excess over 25,000"
    type: NonNegDollars
    expr: {op: sum, of: [single.b3.base, single.b3.product]}
  - id: single.b4.excess
    printed: "(band 4) (single.b4.excess)"
    label: "If line 47 is over 50,000: the excess over 50,000"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.city.single.b4.over}}
  - id: single.b4.product
    printed: "(band 4) (single.b4.product)"
    label: "3.876% of the excess over 50,000"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: single.b4.excess, rate: {param: ny.city.b4.rate}}
  - id: single.b4.base
    printed: "(band 4) (single.b4.base)"
    label: "1,813"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.single.b4.base}
  - id: single.b4.tax
    printed: "The tax is (single.b4.tax)"
    label: "The tax is: 1,813 plus 3.876% of the excess over 50,000"
    type: NonNegDollars
    expr: {op: sum, of: [single.b4.base, single.b4.product]}
  - id: single.result
    printed: "The tax is (single.result)"
    label: "Single and married filing separately—filing status ① and ③: The tax is"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [amount, {param: ny.city.single.b1.upper}]}
          then: single.b1.tax
        - guard:
            op: test
            all:
              - {op: test, gt: [amount, {param: ny.city.single.b2.over}]}
              - {op: test, le: [amount, {param: ny.city.single.b2.upper}]}
          then: single.b2.tax
        - guard:
            op: test
            all:
              - {op: test, gt: [amount, {param: ny.city.single.b3.over}]}
              - {op: test, le: [amount, {param: ny.city.single.b3.upper}]}
          then: single.b3.tax
        - guard: {op: test, gt: [amount, {param: ny.city.single.b4.over}]}
          then: single.b4.tax
  - id: mfj.b1.excess
    printed: "(band 1) (mfj.b1.excess)"
    label: "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤: If line 47 is over $0 but not over $21,600: line 47"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.city.mfj.b1.over}}
  - id: mfj.b1.product
    printed: "(band 1) (mfj.b1.product)"
    label: "3.078% of line 47"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: mfj.b1.excess, rate: {param: ny.city.b1.rate}}
  - id: mfj.b1.base
    printed: "(band 1) (mfj.b1.base)"
    label: "(no fixed amount printed for the first band)"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.mfj.b1.base}
  - id: mfj.b1.tax
    printed: "The tax is (mfj.b1.tax)"
    label: "The tax is: 3.078% of line 47"
    type: NonNegDollars
    expr: {op: sum, of: [mfj.b1.base, mfj.b1.product]}
  - id: mfj.b2.excess
    printed: "(band 2) (mfj.b2.excess)"
    label: "If line 47 is over 21,600 but not over 45,000: the excess over $21,600"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.city.mfj.b2.over}}
  - id: mfj.b2.product
    printed: "(band 2) (mfj.b2.product)"
    label: "3.762% of the excess over $21,600"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: mfj.b2.excess, rate: {param: ny.city.b2.rate}}
  - id: mfj.b2.base
    printed: "(band 2) (mfj.b2.base)"
    label: "$665"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.mfj.b2.base}
  - id: mfj.b2.tax
    printed: "The tax is (mfj.b2.tax)"
    label: "The tax is: $665 plus 3.762% of the excess over $21,600"
    type: NonNegDollars
    expr: {op: sum, of: [mfj.b2.base, mfj.b2.product]}
  - id: mfj.b3.excess
    printed: "(band 3) (mfj.b3.excess)"
    label: "If line 47 is over 45,000 but not over 90,000: the excess over 45,000"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.city.mfj.b3.over}}
  - id: mfj.b3.product
    printed: "(band 3) (mfj.b3.product)"
    label: "3.819% of the excess over 45,000"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: mfj.b3.excess, rate: {param: ny.city.b3.rate}}
  - id: mfj.b3.base
    printed: "(band 3) (mfj.b3.base)"
    label: "1,545"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.mfj.b3.base}
  - id: mfj.b3.tax
    printed: "The tax is (mfj.b3.tax)"
    label: "The tax is: 1,545 plus 3.819% of the excess over 45,000"
    type: NonNegDollars
    expr: {op: sum, of: [mfj.b3.base, mfj.b3.product]}
  - id: mfj.b4.excess
    printed: "(band 4) (mfj.b4.excess)"
    label: "If line 47 is over 90,000: the excess over 90,000"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.city.mfj.b4.over}}
  - id: mfj.b4.product
    printed: "(band 4) (mfj.b4.product)"
    label: "3.876% of the excess over 90,000"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: mfj.b4.excess, rate: {param: ny.city.b4.rate}}
  - id: mfj.b4.base
    printed: "(band 4) (mfj.b4.base)"
    label: "3,264"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.mfj.b4.base}
  - id: mfj.b4.tax
    printed: "The tax is (mfj.b4.tax)"
    label: "The tax is: 3,264 plus 3.876% of the excess over 90,000"
    type: NonNegDollars
    expr: {op: sum, of: [mfj.b4.base, mfj.b4.product]}
  - id: mfj.result
    printed: "The tax is (mfj.result)"
    label: "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤: The tax is"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [amount, {param: ny.city.mfj.b1.upper}]}
          then: mfj.b1.tax
        - guard:
            op: test
            all:
              - {op: test, gt: [amount, {param: ny.city.mfj.b2.over}]}
              - {op: test, le: [amount, {param: ny.city.mfj.b2.upper}]}
          then: mfj.b2.tax
        - guard:
            op: test
            all:
              - {op: test, gt: [amount, {param: ny.city.mfj.b3.over}]}
              - {op: test, le: [amount, {param: ny.city.mfj.b3.upper}]}
          then: mfj.b3.tax
        - guard: {op: test, gt: [amount, {param: ny.city.mfj.b4.over}]}
          then: mfj.b4.tax
  - id: hoh.b1.excess
    printed: "(band 1) (hoh.b1.excess)"
    label: "Head of household—filing status ④: If line 47 is over $0 but not over $14,400: line 47"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.city.hoh.b1.over}}
  - id: hoh.b1.product
    printed: "(band 1) (hoh.b1.product)"
    label: "3.078% of line 47"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: hoh.b1.excess, rate: {param: ny.city.b1.rate}}
  - id: hoh.b1.base
    printed: "(band 1) (hoh.b1.base)"
    label: "(no fixed amount printed for the first band)"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.hoh.b1.base}
  - id: hoh.b1.tax
    printed: "The tax is (hoh.b1.tax)"
    label: "The tax is: 3.078% of line 47"
    type: NonNegDollars
    expr: {op: sum, of: [hoh.b1.base, hoh.b1.product]}
  - id: hoh.b2.excess
    printed: "(band 2) (hoh.b2.excess)"
    label: "If line 47 is over 14,400 but not over 30,000: the excess over $14,400"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.city.hoh.b2.over}}
  - id: hoh.b2.product
    printed: "(band 2) (hoh.b2.product)"
    label: "3.762% of the excess over $14,400"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: hoh.b2.excess, rate: {param: ny.city.b2.rate}}
  - id: hoh.b2.base
    printed: "(band 2) (hoh.b2.base)"
    label: "$443"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.hoh.b2.base}
  - id: hoh.b2.tax
    printed: "The tax is (hoh.b2.tax)"
    label: "The tax is: $443 plus 3.762% of the excess over $14,400"
    type: NonNegDollars
    expr: {op: sum, of: [hoh.b2.base, hoh.b2.product]}
  - id: hoh.b3.excess
    printed: "(band 3) (hoh.b3.excess)"
    label: "If line 47 is over 30,000 but not over 60,000: the excess over 30,000"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.city.hoh.b3.over}}
  - id: hoh.b3.product
    printed: "(band 3) (hoh.b3.product)"
    label: "3.819% of the excess over 30,000"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: hoh.b3.excess, rate: {param: ny.city.b3.rate}}
  - id: hoh.b3.base
    printed: "(band 3) (hoh.b3.base)"
    label: "1,030"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.hoh.b3.base}
  - id: hoh.b3.tax
    printed: "The tax is (hoh.b3.tax)"
    label: "The tax is: 1,030 plus 3.819% of the excess over 30,000"
    type: NonNegDollars
    expr: {op: sum, of: [hoh.b3.base, hoh.b3.product]}
  - id: hoh.b4.excess
    printed: "(band 4) (hoh.b4.excess)"
    label: "If line 47 is over 60,000: the excess over 60,000"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.city.hoh.b4.over}}
  - id: hoh.b4.product
    printed: "(band 4) (hoh.b4.product)"
    label: "3.876% of the excess over 60,000"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: hoh.b4.excess, rate: {param: ny.city.b4.rate}}
  - id: hoh.b4.base
    printed: "(band 4) (hoh.b4.base)"
    label: "2,176"
    type: NonNegDollars
    expr: {op: param, ref: ny.city.hoh.b4.base}
  - id: hoh.b4.tax
    printed: "The tax is (hoh.b4.tax)"
    label: "The tax is: 2,176 plus 3.876% of the excess over 60,000"
    type: NonNegDollars
    expr: {op: sum, of: [hoh.b4.base, hoh.b4.product]}
  - id: hoh.result
    printed: "The tax is (hoh.result)"
    label: "Head of household—filing status ④: The tax is"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [amount, {param: ny.city.hoh.b1.upper}]}
          then: hoh.b1.tax
        - guard:
            op: test
            all:
              - {op: test, gt: [amount, {param: ny.city.hoh.b2.over}]}
              - {op: test, le: [amount, {param: ny.city.hoh.b2.upper}]}
          then: hoh.b2.tax
        - guard:
            op: test
            all:
              - {op: test, gt: [amount, {param: ny.city.hoh.b3.over}]}
              - {op: test, le: [amount, {param: ny.city.hoh.b3.upper}]}
          then: hoh.b3.tax
        - guard: {op: test, gt: [amount, {param: ny.city.hoh.b4.over}]}
          then: hoh.b4.tax
  - id: tax
    printed: "The tax is (tax)"
    label: "New York City tax rate schedule: The tax is"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            any:
              - {op: test, eq: [status, {const: "mfj"}]}
              - {op: test, eq: [status, {const: "qss"}]}
          then: mfj.result
        - guard:
            op: test
            any:
              - {op: test, eq: [status, {const: "single"}]}
              - {op: test, eq: [status, {const: "mfs"}]}
          then: single.result
        - guard: {op: test, eq: [status, {const: "hoh"}]}
          then: hoh.result
    note: "The schedule assigns filing status ② and ⑤ (married filing jointly, qualifying surviving spouse) to the first schedule. It assigns ① and ③ (single, married filing separately) to the second and ④ (head of household) to the third. The schedule does not state any rounding of the result to whole dollars, so none is applied."
```
```
