# Transcription agreement — ny_rs

Second transcription of `New York State tax rate schedule` by an isolated model (spec 6.5), compared line by line with `forms/ny/2025/ny_rs.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-04 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 36926b82af5d2c2ef35fe173705b9d170f23d321209b7e7803a88b936cad8c38 |
| prompt policy | source-only-computation-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 9b661c42b350cccec24de8ea3283bf6001be9efbe99d448db8f4c3ebcf0eda7a |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | 83e9ed0ae4edc40db4c301ed52bf00d46afb0b4bd30dea929e35960993911093 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 22e5d742305ec04854f9893f945ec9f50bbb06818d468b3e3f8f5bb47e166041 |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i-html | Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny) | 1 | cited sections: New York State tax rate schedule | 63863fe461c33d052e26a67c87d000ed70b896c72437350880a9e1c680104982 | - | - |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 4 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 4 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |

## Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | ny_city_rs, ny_tcw, ny_tcw_first |
| shared page | ny_it201 |

## Lines

### tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"input": "amount"}], "test": "le"}, {"args": [{"input": "amount"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b8.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.mfj.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"input": "amount"}], "test": "le"}, {"args": [{"input": "amount"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.single.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.single.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.single.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.single.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.single.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.single.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.single.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b8.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.single.b9.base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"input": "amount"}], "test": "le"}, {"args": [{"input": "amount"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}], "test": "all"}, "then": {"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}, "unit": 100}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b1.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b2.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b3.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b4.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b5.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b6.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b7.base"}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.upper"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b8.base"}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b8.upper"}, {"input": "amount"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}, "unit": 100}, {"param": "ny.rs.hoh.b9.base"}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.mfj.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b2.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}}, {"from": {"param": "ny.rs.mfj.b2.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.mfj.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b3.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}}, {"from": {"param": "ny.rs.mfj.b3.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.mfj.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b4.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}}, {"from": {"param": "ny.rs.mfj.b4.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.mfj.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b5.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}}, {"from": {"param": "ny.rs.mfj.b5.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.mfj.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b6.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}}, {"from": {"param": "ny.rs.mfj.b6.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.mfj.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b7.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}}, {"from": {"param": "ny.rs.mfj.b7.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.mfj.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.mfj.b8.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}}, {"from": {"param": "ny.rs.mfj.b8.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"input": "amount"}, {"param": "ny.rs.mfj.b1.upper"}], "test": "le"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}}, {"from": {"const": 0}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.mfj.b9.over"}, {"input": "amount"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.mfj.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}}, {"from": {"param": "ny.rs.mfj.b9.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"input": "status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.single.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b2.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}}, {"from": {"param": "ny.rs.single.b2.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.single.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b3.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}}, {"from": {"param": "ny.rs.single.b3.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.single.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b4.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}}, {"from": {"param": "ny.rs.single.b4.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.single.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b5.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}}, {"from": {"param": "ny.rs.single.b5.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.single.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b6.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}}, {"from": {"param": "ny.rs.single.b6.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.single.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b7.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}}, {"from": {"param": "ny.rs.single.b7.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.single.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.single.b8.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}}, {"from": {"param": "ny.rs.single.b8.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"input": "amount"}, {"param": "ny.rs.single.b1.upper"}], "test": "le"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}}, {"from": {"const": 0}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.single.b9.over"}, {"input": "amount"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.single.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}}, {"from": {"param": "ny.rs.single.b9.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"const": "hoh"}, {"input": "status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.hoh.b2.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b2.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b2.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b2.rate"}}, {"from": {"param": "ny.rs.hoh.b2.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.hoh.b3.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b3.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b3.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b3.rate"}}, {"from": {"param": "ny.rs.hoh.b3.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.hoh.b4.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b4.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b4.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b4.rate"}}, {"from": {"param": "ny.rs.hoh.b4.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.hoh.b5.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b5.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b5.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b5.rate"}}, {"from": {"param": "ny.rs.hoh.b5.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.hoh.b6.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b6.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b6.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b6.rate"}}, {"from": {"param": "ny.rs.hoh.b6.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.hoh.b7.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b7.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b7.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b7.rate"}}, {"from": {"param": "ny.rs.hoh.b7.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"args": [{"input": "amount"}, {"param": "ny.rs.hoh.b8.upper"}], "test": "le"}, {"args": [{"param": "ny.rs.hoh.b8.over"}, {"input": "amount"}], "test": "lt"}], "test": "all"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b8.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b8.rate"}}, {"from": {"param": "ny.rs.hoh.b8.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"input": "amount"}, {"param": "ny.rs.hoh.b1.upper"}], "test": "le"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"const": 0}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b1.rate"}}, {"from": {"const": 0}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}, {"guard": {"args": [{"param": "ny.rs.hoh.b9.over"}, {"input": "amount"}], "test": "lt"}, "then": {"of": [{"amount": {"from": {"input": "amount"}, "op": "subtract_floor0", "take": {"param": "ny.rs.hoh.b9.over"}}, "op": "multiply_rate", "rate": {"param": "ny.rs.b9.rate"}}, {"from": {"param": "ny.rs.hoh.b9.base"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}}], "op": "choose"}}], "op": "choose"}
```

Second transcription's note: Open points. (1) The schedule does not say how to round the percentage of the excess. I chose half-up to the cent, with no rounding to the dollar. (2) The schedule's opening sentence sends filers whose New York AGI (IT-201 line 33) is more than $107,650 to the tax computation worksheets. I left that routing to the calling line, because this schedule is computed only from line 38 (amount) and the filing status. (3) The schedule bands are 'over / but not over'. I encoded band 1 as amount not over its upper bound, since line 38 is not negative. (4) Filing status mfs uses the single schedule and qss uses the joint schedule, as the headings say.

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; IT-201-I p. 7, "Enter only whole dollar amounts on your New York return."; p. 2, "Increase amounts that are 50 cents or more to the next dollar."). Evaluated on a grid of whole-dollar amounts for every status (scratch evaluator, params/ny/2025.yaml): the reply differs from the project only by the cents of the band product, never more than 50 cents; the bands' "over" amounts equal the previous bands' upper limits, so the reordered guards select the same band.

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| tax | 988c7ec172c334b54735490aaf793e7e79e81464fff39e7bb68374b15aadc21e |
| (rest of the document) | 6200916731ed24feafad3e6652cd7d8c54a30ebee414a737a8936aebd61e84b7 |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| tax | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |

## Raw second transcription

```yaml
```yaml
lines:
  - id: ny_rs.h_is_single
    printed: "(helper)"
    label: "Single and married filing separately—filing status ① and ③"
    type: Bool
    expr: {op: test, any: [{op: test, eq: [status, {const: "single"}]}, {op: test, eq: [status, {const: "mfs"}]}]}
  - id: ny_rs.h_is_mfj
    printed: "(helper)"
    label: "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤"
    type: Bool
    expr: {op: test, any: [{op: test, eq: [status, {const: "mfj"}]}, {op: test, eq: [status, {const: "qss"}]}]}
  - id: ny_rs.h_is_hoh
    printed: "(helper)"
    label: "Head of household—filing status ④"
    type: Bool
    expr: {op: test, eq: [status, {const: "hoh"}]}

  # ---------------- Single and married filing separately ----------------
  - id: ny_rs.h_single_in_b1
    printed: "(helper)"
    label: "If line 38 is over $0 but not over $8,500"
    type: Bool
    expr: {op: test, le: [amount, {param: ny.rs.single.b1.upper}]}
  - id: ny_rs.h_single_show_b1
    printed: "(helper)"
    label: "Single schedule applies and line 38 is not over $8,500"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_single, {const: true}]}, {op: test, eq: [ny_rs.h_single_in_b1, {const: true}]}]}
  - id: single.b1.excess
    printed: "(band 1) (single.b1.excess)"
    label: "Line 38 (over $0)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.single.b1.over}}
    shown_when: ny_rs.h_single_show_b1
  - id: single.b1.product
    printed: "(band 1) (single.b1.product)"
    label: "4% of line 38"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: single.b1.excess, rate: {param: ny.rs.b1.rate}}
    shown_when: ny_rs.h_single_show_b1
  - id: ny_rs.h_single_b1_base_amt
    printed: "(helper)"
    label: "Base amount, band 1 ($0)"
    type: Dollars
    expr: {op: param, ref: ny.rs.single.b1.base}
  - id: single.b1.base
    printed: "(band 1) (single.b1.base)"
    label: "Base amount ($0)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_single_b1_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_single_show_b1
  - id: single.b1.tax
    printed: "The tax is (single.b1.tax)"
    label: "The tax is: 4% of line 38"
    type: NonNegDollars
    expr: {op: sum, of: [single.b1.base, single.b1.product]}
    shown_when: ny_rs.h_single_show_b1

  - id: ny_rs.h_single_in_b2
    printed: "(helper)"
    label: "If line 38 is over $8,500 but not over $11,700"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.single.b2.over}]}, {op: test, le: [amount, {param: ny.rs.single.b2.upper}]}]}
  - id: ny_rs.h_single_show_b2
    printed: "(helper)"
    label: "Single schedule applies and line 38 is in band 2"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_single, {const: true}]}, {op: test, eq: [ny_rs.h_single_in_b2, {const: true}]}]}
  - id: single.b2.excess
    printed: "(band 2) (single.b2.excess)"
    label: "The excess over $8,500"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.single.b2.over}}
    shown_when: ny_rs.h_single_show_b2
  - id: single.b2.product
    printed: "(band 2) (single.b2.product)"
    label: "4.5% of the excess over $8,500"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: single.b2.excess, rate: {param: ny.rs.b2.rate}}
    shown_when: ny_rs.h_single_show_b2
  - id: ny_rs.h_single_b2_base_amt
    printed: "(helper)"
    label: "$340"
    type: Dollars
    expr: {op: param, ref: ny.rs.single.b2.base}
  - id: single.b2.base
    printed: "(band 2) (single.b2.base)"
    label: "$340"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_single_b2_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_single_show_b2
  - id: single.b2.tax
    printed: "The tax is (single.b2.tax)"
    label: "The tax is: $340 plus 4.5% of the excess over $8,500"
    type: NonNegDollars
    expr: {op: sum, of: [single.b2.base, single.b2.product]}
    shown_when: ny_rs.h_single_show_b2

  - id: ny_rs.h_single_in_b3
    printed: "(helper)"
    label: "If line 38 is over $11,700 but not over $13,900"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.single.b3.over}]}, {op: test, le: [amount, {param: ny.rs.single.b3.upper}]}]}
  - id: ny_rs.h_single_show_b3
    printed: "(helper)"
    label: "Single schedule applies and line 38 is in band 3"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_single, {const: true}]}, {op: test, eq: [ny_rs.h_single_in_b3, {const: true}]}]}
  - id: single.b3.excess
    printed: "(band 3) (single.b3.excess)"
    label: "The excess over $11,700"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.single.b3.over}}
    shown_when: ny_rs.h_single_show_b3
  - id: single.b3.product
    printed: "(band 3) (single.b3.product)"
    label: "5.25% of the excess over $11,700"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: single.b3.excess, rate: {param: ny.rs.b3.rate}}
    shown_when: ny_rs.h_single_show_b3
  - id: ny_rs.h_single_b3_base_amt
    printed: "(helper)"
    label: "$484"
    type: Dollars
    expr: {op: param, ref: ny.rs.single.b3.base}
  - id: single.b3.base
    printed: "(band 3) (single.b3.base)"
    label: "$484"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_single_b3_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_single_show_b3
  - id: single.b3.tax
    printed: "The tax is (single.b3.tax)"
    label: "The tax is: $484 plus 5.25% of the excess over $11,700"
    type: NonNegDollars
    expr: {op: sum, of: [single.b3.base, single.b3.product]}
    shown_when: ny_rs.h_single_show_b3

  - id: ny_rs.h_single_in_b4
    printed: "(helper)"
    label: "If line 38 is over $13,900 but not over $80,650"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.single.b4.over}]}, {op: test, le: [amount, {param: ny.rs.single.b4.upper}]}]}
  - id: ny_rs.h_single_show_b4
    printed: "(helper)"
    label: "Single schedule applies and line 38 is in band 4"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_single, {const: true}]}, {op: test, eq: [ny_rs.h_single_in_b4, {const: true}]}]}
  - id: single.b4.excess
    printed: "(band 4) (single.b4.excess)"
    label: "The excess over $13,900"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.single.b4.over}}
    shown_when: ny_rs.h_single_show_b4
  - id: single.b4.product
    printed: "(band 4) (single.b4.product)"
    label: "5.5% of the excess over $13,900"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: single.b4.excess, rate: {param: ny.rs.b4.rate}}
    shown_when: ny_rs.h_single_show_b4
  - id: ny_rs.h_single_b4_base_amt
    printed: "(helper)"
    label: "$600"
    type: Dollars
    expr: {op: param, ref: ny.rs.single.b4.base}
  - id: single.b4.base
    printed: "(band 4) (single.b4.base)"
    label: "$600"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_single_b4_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_single_show_b4
  - id: single.b4.tax
    printed: "The tax is (single.b4.tax)"
    label: "The tax is: $600 plus 5.5% of the excess over $13,900"
    type: NonNegDollars
    expr: {op: sum, of: [single.b4.base, single.b4.product]}
    shown_when: ny_rs.h_single_show_b4

  - id: ny_rs.h_single_in_b5
    printed: "(helper)"
    label: "If line 38 is over $80,650 but not over $215,400"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.single.b5.over}]}, {op: test, le: [amount, {param: ny.rs.single.b5.upper}]}]}
  - id: ny_rs.h_single_show_b5
    printed: "(helper)"
    label: "Single schedule applies and line 38 is in band 5"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_single, {const: true}]}, {op: test, eq: [ny_rs.h_single_in_b5, {const: true}]}]}
  - id: single.b5.excess
    printed: "(band 5) (single.b5.excess)"
    label: "The excess over $80,650"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.single.b5.over}}
    shown_when: ny_rs.h_single_show_b5
  - id: single.b5.product
    printed: "(band 5) (single.b5.product)"
    label: "6% of the excess over $80,650"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: single.b5.excess, rate: {param: ny.rs.b5.rate}}
    shown_when: ny_rs.h_single_show_b5
  - id: ny_rs.h_single_b5_base_amt
    printed: "(helper)"
    label: "$4,271"
    type: Dollars
    expr: {op: param, ref: ny.rs.single.b5.base}
  - id: single.b5.base
    printed: "(band 5) (single.b5.base)"
    label: "$4,271"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_single_b5_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_single_show_b5
  - id: single.b5.tax
    printed: "The tax is (single.b5.tax)"
    label: "The tax is: $4,271 plus 6% of the excess over $80,650"
    type: NonNegDollars
    expr: {op: sum, of: [single.b5.base, single.b5.product]}
    shown_when: ny_rs.h_single_show_b5

  - id: ny_rs.h_single_in_b6
    printed: "(helper)"
    label: "If line 38 is over $215,400 but not over $1,077,550"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.single.b6.over}]}, {op: test, le: [amount, {param: ny.rs.single.b6.upper}]}]}
  - id: ny_rs.h_single_show_b6
    printed: "(helper)"
    label: "Single schedule applies and line 38 is in band 6"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_single, {const: true}]}, {op: test, eq: [ny_rs.h_single_in_b6, {const: true}]}]}
  - id: single.b6.excess
    printed: "(band 6) (single.b6.excess)"
    label: "The excess over $215,400"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.single.b6.over}}
    shown_when: ny_rs.h_single_show_b6
  - id: single.b6.product
    printed: "(band 6) (single.b6.product)"
    label: "6.85% of the excess over $215,400"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: single.b6.excess, rate: {param: ny.rs.b6.rate}}
    shown_when: ny_rs.h_single_show_b6
  - id: ny_rs.h_single_b6_base_amt
    printed: "(helper)"
    label: "$12,356"
    type: Dollars
    expr: {op: param, ref: ny.rs.single.b6.base}
  - id: single.b6.base
    printed: "(band 6) (single.b6.base)"
    label: "$12,356"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_single_b6_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_single_show_b6
  - id: single.b6.tax
    printed: "The tax is (single.b6.tax)"
    label: "The tax is: $12,356 plus 6.85% of the excess over $215,400"
    type: NonNegDollars
    expr: {op: sum, of: [single.b6.base, single.b6.product]}
    shown_when: ny_rs.h_single_show_b6

  - id: ny_rs.h_single_in_b7
    printed: "(helper)"
    label: "If line 38 is over $1,077,550 but not over $5,000,000"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.single.b7.over}]}, {op: test, le: [amount, {param: ny.rs.single.b7.upper}]}]}
  - id: ny_rs.h_single_show_b7
    printed: "(helper)"
    label: "Single schedule applies and line 38 is in band 7"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_single, {const: true}]}, {op: test, eq: [ny_rs.h_single_in_b7, {const: true}]}]}
  - id: single.b7.excess
    printed: "(band 7) (single.b7.excess)"
    label: "The excess over $1,077,550"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.single.b7.over}}
    shown_when: ny_rs.h_single_show_b7
  - id: single.b7.product
    printed: "(band 7) (single.b7.product)"
    label: "9.65% of the excess over $1,077,550"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: single.b7.excess, rate: {param: ny.rs.b7.rate}}
    shown_when: ny_rs.h_single_show_b7
  - id: ny_rs.h_single_b7_base_amt
    printed: "(helper)"
    label: "$71,413"
    type: Dollars
    expr: {op: param, ref: ny.rs.single.b7.base}
  - id: single.b7.base
    printed: "(band 7) (single.b7.base)"
    label: "$71,413"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_single_b7_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_single_show_b7
  - id: single.b7.tax
    printed: "The tax is (single.b7.tax)"
    label: "The tax is: $71,413 plus 9.65% of the excess over $1,077,550"
    type: NonNegDollars
    expr: {op: sum, of: [single.b7.base, single.b7.product]}
    shown_when: ny_rs.h_single_show_b7

  - id: ny_rs.h_single_in_b8
    printed: "(helper)"
    label: "If line 38 is over $5,000,000 but not over $25,000,000"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.single.b8.over}]}, {op: test, le: [amount, {param: ny.rs.single.b8.upper}]}]}
  - id: ny_rs.h_single_show_b8
    printed: "(helper)"
    label: "Single schedule applies and line 38 is in band 8"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_single, {const: true}]}, {op: test, eq: [ny_rs.h_single_in_b8, {const: true}]}]}
  - id: single.b8.excess
    printed: "(band 8) (single.b8.excess)"
    label: "The excess over $5,000,000"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.single.b8.over}}
    shown_when: ny_rs.h_single_show_b8
  - id: single.b8.product
    printed: "(band 8) (single.b8.product)"
    label: "10.3% of the excess over $5,000,000"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: single.b8.excess, rate: {param: ny.rs.b8.rate}}
    shown_when: ny_rs.h_single_show_b8
  - id: ny_rs.h_single_b8_base_amt
    printed: "(helper)"
    label: "$449,929"
    type: Dollars
    expr: {op: param, ref: ny.rs.single.b8.base}
  - id: single.b8.base
    printed: "(band 8) (single.b8.base)"
    label: "$449,929"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_single_b8_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_single_show_b8
  - id: single.b8.tax
    printed: "The tax is (single.b8.tax)"
    label: "The tax is: $449,929 plus 10.3% of the excess over $5,000,000"
    type: NonNegDollars
    expr: {op: sum, of: [single.b8.base, single.b8.product]}
    shown_when: ny_rs.h_single_show_b8

  - id: ny_rs.h_single_in_b9
    printed: "(helper)"
    label: "If line 38 is over $25,000,000"
    type: Bool
    expr: {op: test, gt: [amount, {param: ny.rs.single.b9.over}]}
  - id: ny_rs.h_single_show_b9
    printed: "(helper)"
    label: "Single schedule applies and line 38 is over $25,000,000"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_single, {const: true}]}, {op: test, eq: [ny_rs.h_single_in_b9, {const: true}]}]}
  - id: single.b9.excess
    printed: "(band 9) (single.b9.excess)"
    label: "The excess over $25,000,000"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.single.b9.over}}
    shown_when: ny_rs.h_single_show_b9
  - id: single.b9.product
    printed: "(band 9) (single.b9.product)"
    label: "10.9% of the excess over $25,000,000"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: single.b9.excess, rate: {param: ny.rs.b9.rate}}
    shown_when: ny_rs.h_single_show_b9
  - id: ny_rs.h_single_b9_base_amt
    printed: "(helper)"
    label: "$2,509,929"
    type: Dollars
    expr: {op: param, ref: ny.rs.single.b9.base}
  - id: single.b9.base
    printed: "(band 9) (single.b9.base)"
    label: "$2,509,929"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_single_b9_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_single_show_b9
  - id: single.b9.tax
    printed: "The tax is (single.b9.tax)"
    label: "The tax is: $2,509,929 plus 10.9% of the excess over $25,000,000"
    type: NonNegDollars
    expr: {op: sum, of: [single.b9.base, single.b9.product]}
    shown_when: ny_rs.h_single_show_b9

  - id: single.result
    printed: "The tax is (single.result)"
    label: "Single and married filing separately—filing status ① and ③: The tax is"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [ny_rs.h_single_in_b1, {const: true}]}, then: single.b1.tax}
        - {guard: {op: test, eq: [ny_rs.h_single_in_b2, {const: true}]}, then: single.b2.tax}
        - {guard: {op: test, eq: [ny_rs.h_single_in_b3, {const: true}]}, then: single.b3.tax}
        - {guard: {op: test, eq: [ny_rs.h_single_in_b4, {const: true}]}, then: single.b4.tax}
        - {guard: {op: test, eq: [ny_rs.h_single_in_b5, {const: true}]}, then: single.b5.tax}
        - {guard: {op: test, eq: [ny_rs.h_single_in_b6, {const: true}]}, then: single.b6.tax}
        - {guard: {op: test, eq: [ny_rs.h_single_in_b7, {const: true}]}, then: single.b7.tax}
        - {guard: {op: test, eq: [ny_rs.h_single_in_b8, {const: true}]}, then: single.b8.tax}
        - {guard: {op: test, eq: [ny_rs.h_single_in_b9, {const: true}]}, then: single.b9.tax}
    shown_when: ny_rs.h_is_single

  # ---------------- Married filing jointly / qualifying surviving spouse ----------------
  - id: ny_rs.h_mfj_in_b1
    printed: "(helper)"
    label: "If line 38 is over $0 but not over $17,150"
    type: Bool
    expr: {op: test, le: [amount, {param: ny.rs.mfj.b1.upper}]}
  - id: ny_rs.h_mfj_show_b1
    printed: "(helper)"
    label: "Joint schedule applies and line 38 is in band 1"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_mfj, {const: true}]}, {op: test, eq: [ny_rs.h_mfj_in_b1, {const: true}]}]}
  - id: mfj.b1.excess
    printed: "(band 1) (mfj.b1.excess)"
    label: "Line 38 (over $0)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.mfj.b1.over}}
    shown_when: ny_rs.h_mfj_show_b1
  - id: mfj.b1.product
    printed: "(band 1) (mfj.b1.product)"
    label: "4% of line 38"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: mfj.b1.excess, rate: {param: ny.rs.b1.rate}}
    shown_when: ny_rs.h_mfj_show_b1
  - id: ny_rs.h_mfj_b1_base_amt
    printed: "(helper)"
    label: "Base amount, band 1 ($0)"
    type: Dollars
    expr: {op: param, ref: ny.rs.mfj.b1.base}
  - id: mfj.b1.base
    printed: "(band 1) (mfj.b1.base)"
    label: "Base amount ($0)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_mfj_b1_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_mfj_show_b1
  - id: mfj.b1.tax
    printed: "The tax is (mfj.b1.tax)"
    label: "The tax is: 4% of line 38"
    type: NonNegDollars
    expr: {op: sum, of: [mfj.b1.base, mfj.b1.product]}
    shown_when: ny_rs.h_mfj_show_b1

  - id: ny_rs.h_mfj_in_b2
    printed: "(helper)"
    label: "If line 38 is over $17,150 but not over $23,600"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.mfj.b2.over}]}, {op: test, le: [amount, {param: ny.rs.mfj.b2.upper}]}]}
  - id: ny_rs.h_mfj_show_b2
    printed: "(helper)"
    label: "Joint schedule applies and line 38 is in band 2"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_mfj, {const: true}]}, {op: test, eq: [ny_rs.h_mfj_in_b2, {const: true}]}]}
  - id: mfj.b2.excess
    printed: "(band 2) (mfj.b2.excess)"
    label: "The excess over $17,150"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.mfj.b2.over}}
    shown_when: ny_rs.h_mfj_show_b2
  - id: mfj.b2.product
    printed: "(band 2) (mfj.b2.product)"
    label: "4.5% of the excess over $17,150"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: mfj.b2.excess, rate: {param: ny.rs.b2.rate}}
    shown_when: ny_rs.h_mfj_show_b2
  - id: ny_rs.h_mfj_b2_base_amt
    printed: "(helper)"
    label: "$686"
    type: Dollars
    expr: {op: param, ref: ny.rs.mfj.b2.base}
  - id: mfj.b2.base
    printed: "(band 2) (mfj.b2.base)"
    label: "$686"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_mfj_b2_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_mfj_show_b2
  - id: mfj.b2.tax
    printed: "The tax is (mfj.b2.tax)"
    label: "The tax is: $686 plus 4.5% of the excess over $17,150"
    type: NonNegDollars
    expr: {op: sum, of: [mfj.b2.base, mfj.b2.product]}
    shown_when: ny_rs.h_mfj_show_b2

  - id: ny_rs.h_mfj_in_b3
    printed: "(helper)"
    label: "If line 38 is over $23,600 but not over $27,900"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.mfj.b3.over}]}, {op: test, le: [amount, {param: ny.rs.mfj.b3.upper}]}]}
  - id: ny_rs.h_mfj_show_b3
    printed: "(helper)"
    label: "Joint schedule applies and line 38 is in band 3"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_mfj, {const: true}]}, {op: test, eq: [ny_rs.h_mfj_in_b3, {const: true}]}]}
  - id: mfj.b3.excess
    printed: "(band 3) (mfj.b3.excess)"
    label: "The excess over $23,600"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.mfj.b3.over}}
    shown_when: ny_rs.h_mfj_show_b3
  - id: mfj.b3.product
    printed: "(band 3) (mfj.b3.product)"
    label: "5.25% of the excess over $23,600"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: mfj.b3.excess, rate: {param: ny.rs.b3.rate}}
    shown_when: ny_rs.h_mfj_show_b3
  - id: ny_rs.h_mfj_b3_base_amt
    printed: "(helper)"
    label: "$976"
    type: Dollars
    expr: {op: param, ref: ny.rs.mfj.b3.base}
  - id: mfj.b3.base
    printed: "(band 3) (mfj.b3.base)"
    label: "$976"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_mfj_b3_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_mfj_show_b3
  - id: mfj.b3.tax
    printed: "The tax is (mfj.b3.tax)"
    label: "The tax is: $976 plus 5.25% of the excess over $23,600"
    type: NonNegDollars
    expr: {op: sum, of: [mfj.b3.base, mfj.b3.product]}
    shown_when: ny_rs.h_mfj_show_b3

  - id: ny_rs.h_mfj_in_b4
    printed: "(helper)"
    label: "If line 38 is over $27,900 but not over $161,550"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.mfj.b4.over}]}, {op: test, le: [amount, {param: ny.rs.mfj.b4.upper}]}]}
  - id: ny_rs.h_mfj_show_b4
    printed: "(helper)"
    label: "Joint schedule applies and line 38 is in band 4"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_mfj, {const: true}]}, {op: test, eq: [ny_rs.h_mfj_in_b4, {const: true}]}]}
  - id: mfj.b4.excess
    printed: "(band 4) (mfj.b4.excess)"
    label: "The excess over $27,900"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.mfj.b4.over}}
    shown_when: ny_rs.h_mfj_show_b4
  - id: mfj.b4.product
    printed: "(band 4) (mfj.b4.product)"
    label: "5.5% of the excess over $27,900"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: mfj.b4.excess, rate: {param: ny.rs.b4.rate}}
    shown_when: ny_rs.h_mfj_show_b4
  - id: ny_rs.h_mfj_b4_base_amt
    printed: "(helper)"
    label: "$1,202"
    type: Dollars
    expr: {op: param, ref: ny.rs.mfj.b4.base}
  - id: mfj.b4.base
    printed: "(band 4) (mfj.b4.base)"
    label: "$1,202"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_mfj_b4_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_mfj_show_b4
  - id: mfj.b4.tax
    printed: "The tax is (mfj.b4.tax)"
    label: "The tax is: $1,202 plus 5.5% of the excess over $27,900"
    type: NonNegDollars
    expr: {op: sum, of: [mfj.b4.base, mfj.b4.product]}
    shown_when: ny_rs.h_mfj_show_b4

  - id: ny_rs.h_mfj_in_b5
    printed: "(helper)"
    label: "If line 38 is over $161,550 but not over $323,200"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.mfj.b5.over}]}, {op: test, le: [amount, {param: ny.rs.mfj.b5.upper}]}]}
  - id: ny_rs.h_mfj_show_b5
    printed: "(helper)"
    label: "Joint schedule applies and line 38 is in band 5"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_mfj, {const: true}]}, {op: test, eq: [ny_rs.h_mfj_in_b5, {const: true}]}]}
  - id: mfj.b5.excess
    printed: "(band 5) (mfj.b5.excess)"
    label: "The excess over $161,550"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.mfj.b5.over}}
    shown_when: ny_rs.h_mfj_show_b5
  - id: mfj.b5.product
    printed: "(band 5) (mfj.b5.product)"
    label: "6% of the excess over $161,550"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: mfj.b5.excess, rate: {param: ny.rs.b5.rate}}
    shown_when: ny_rs.h_mfj_show_b5
  - id: ny_rs.h_mfj_b5_base_amt
    printed: "(helper)"
    label: "$8,553"
    type: Dollars
    expr: {op: param, ref: ny.rs.mfj.b5.base}
  - id: mfj.b5.base
    printed: "(band 5) (mfj.b5.base)"
    label: "$8,553"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_mfj_b5_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_mfj_show_b5
  - id: mfj.b5.tax
    printed: "The tax is (mfj.b5.tax)"
    label: "The tax is: $8,553 plus 6% of the excess over $161,550"
    type: NonNegDollars
    expr: {op: sum, of: [mfj.b5.base, mfj.b5.product]}
    shown_when: ny_rs.h_mfj_show_b5

  - id: ny_rs.h_mfj_in_b6
    printed: "(helper)"
    label: "If line 38 is over $323,200 but not over $2,155,350"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.mfj.b6.over}]}, {op: test, le: [amount, {param: ny.rs.mfj.b6.upper}]}]}
  - id: ny_rs.h_mfj_show_b6
    printed: "(helper)"
    label: "Joint schedule applies and line 38 is in band 6"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_mfj, {const: true}]}, {op: test, eq: [ny_rs.h_mfj_in_b6, {const: true}]}]}
  - id: mfj.b6.excess
    printed: "(band 6) (mfj.b6.excess)"
    label: "The excess over $323,200"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.mfj.b6.over}}
    shown_when: ny_rs.h_mfj_show_b6
  - id: mfj.b6.product
    printed: "(band 6) (mfj.b6.product)"
    label: "6.85% of the excess over $323,200"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: mfj.b6.excess, rate: {param: ny.rs.b6.rate}}
    shown_when: ny_rs.h_mfj_show_b6
  - id: ny_rs.h_mfj_b6_base_amt
    printed: "(helper)"
    label: "$18,252"
    type: Dollars
    expr: {op: param, ref: ny.rs.mfj.b6.base}
  - id: mfj.b6.base
    printed: "(band 6) (mfj.b6.base)"
    label: "$18,252"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_mfj_b6_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_mfj_show_b6
  - id: mfj.b6.tax
    printed: "The tax is (mfj.b6.tax)"
    label: "The tax is: $18,252 plus 6.85% of the excess over $323,200"
    type: NonNegDollars
    expr: {op: sum, of: [mfj.b6.base, mfj.b6.product]}
    shown_when: ny_rs.h_mfj_show_b6

  - id: ny_rs.h_mfj_in_b7
    printed: "(helper)"
    label: "If line 38 is over $2,155,350 but not over $5,000,000"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.mfj.b7.over}]}, {op: test, le: [amount, {param: ny.rs.mfj.b7.upper}]}]}
  - id: ny_rs.h_mfj_show_b7
    printed: "(helper)"
    label: "Joint schedule applies and line 38 is in band 7"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_mfj, {const: true}]}, {op: test, eq: [ny_rs.h_mfj_in_b7, {const: true}]}]}
  - id: mfj.b7.excess
    printed: "(band 7) (mfj.b7.excess)"
    label: "The excess over $2,155,350"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.mfj.b7.over}}
    shown_when: ny_rs.h_mfj_show_b7
  - id: mfj.b7.product
    printed: "(band 7) (mfj.b7.product)"
    label: "9.65% of the excess over $2,155,350"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: mfj.b7.excess, rate: {param: ny.rs.b7.rate}}
    shown_when: ny_rs.h_mfj_show_b7
  - id: ny_rs.h_mfj_b7_base_amt
    printed: "(helper)"
    label: "$143,754"
    type: Dollars
    expr: {op: param, ref: ny.rs.mfj.b7.base}
  - id: mfj.b7.base
    printed: "(band 7) (mfj.b7.base)"
    label: "$143,754"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_mfj_b7_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_mfj_show_b7
  - id: mfj.b7.tax
    printed: "The tax is (mfj.b7.tax)"
    label: "The tax is: $143,754 plus 9.65% of the excess over $2,155,350"
    type: NonNegDollars
    expr: {op: sum, of: [mfj.b7.base, mfj.b7.product]}
    shown_when: ny_rs.h_mfj_show_b7

  - id: ny_rs.h_mfj_in_b8
    printed: "(helper)"
    label: "If line 38 is over $5,000,000 but not over $25,000,000"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.mfj.b8.over}]}, {op: test, le: [amount, {param: ny.rs.mfj.b8.upper}]}]}
  - id: ny_rs.h_mfj_show_b8
    printed: "(helper)"
    label: "Joint schedule applies and line 38 is in band 8"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_mfj, {const: true}]}, {op: test, eq: [ny_rs.h_mfj_in_b8, {const: true}]}]}
  - id: mfj.b8.excess
    printed: "(band 8) (mfj.b8.excess)"
    label: "The excess over $5,000,000"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.mfj.b8.over}}
    shown_when: ny_rs.h_mfj_show_b8
  - id: mfj.b8.product
    printed: "(band 8) (mfj.b8.product)"
    label: "10.3% of the excess over $5,000,000"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: mfj.b8.excess, rate: {param: ny.rs.b8.rate}}
    shown_when: ny_rs.h_mfj_show_b8
  - id: ny_rs.h_mfj_b8_base_amt
    printed: "(helper)"
    label: "$418,263"
    type: Dollars
    expr: {op: param, ref: ny.rs.mfj.b8.base}
  - id: mfj.b8.base
    printed: "(band 8) (mfj.b8.base)"
    label: "$418,263"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_mfj_b8_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_mfj_show_b8
  - id: mfj.b8.tax
    printed: "The tax is (mfj.b8.tax)"
    label: "The tax is: $418,263 plus 10.3% of the excess over $5,000,000"
    type: NonNegDollars
    expr: {op: sum, of: [mfj.b8.base, mfj.b8.product]}
    shown_when: ny_rs.h_mfj_show_b8

  - id: ny_rs.h_mfj_in_b9
    printed: "(helper)"
    label: "If line 38 is over $25,000,000"
    type: Bool
    expr: {op: test, gt: [amount, {param: ny.rs.mfj.b9.over}]}
  - id: ny_rs.h_mfj_show_b9
    printed: "(helper)"
    label: "Joint schedule applies and line 38 is over $25,000,000"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_mfj, {const: true}]}, {op: test, eq: [ny_rs.h_mfj_in_b9, {const: true}]}]}
  - id: mfj.b9.excess
    printed: "(band 9) (mfj.b9.excess)"
    label: "The excess over $25,000,000"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.mfj.b9.over}}
    shown_when: ny_rs.h_mfj_show_b9
  - id: mfj.b9.product
    printed: "(band 9) (mfj.b9.product)"
    label: "10.9% of the excess over $25,000,000"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: mfj.b9.excess, rate: {param: ny.rs.b9.rate}}
    shown_when: ny_rs.h_mfj_show_b9
  - id: ny_rs.h_mfj_b9_base_amt
    printed: "(helper)"
    label: "$2,478,263"
    type: Dollars
    expr: {op: param, ref: ny.rs.mfj.b9.base}
  - id: mfj.b9.base
    printed: "(band 9) (mfj.b9.base)"
    label: "$2,478,263"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_mfj_b9_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_mfj_show_b9
  - id: mfj.b9.tax
    printed: "The tax is (mfj.b9.tax)"
    label: "The tax is: $2,478,263 plus 10.9% of the excess over $25,000,000"
    type: NonNegDollars
    expr: {op: sum, of: [mfj.b9.base, mfj.b9.product]}
    shown_when: ny_rs.h_mfj_show_b9

  - id: mfj.result
    printed: "The tax is (mfj.result)"
    label: "Married filing jointly and qualifying surviving spouse—filing status ② and ⑤: The tax is"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [ny_rs.h_mfj_in_b1, {const: true}]}, then: mfj.b1.tax}
        - {guard: {op: test, eq: [ny_rs.h_mfj_in_b2, {const: true}]}, then: mfj.b2.tax}
        - {guard: {op: test, eq: [ny_rs.h_mfj_in_b3, {const: true}]}, then: mfj.b3.tax}
        - {guard: {op: test, eq: [ny_rs.h_mfj_in_b4, {const: true}]}, then: mfj.b4.tax}
        - {guard: {op: test, eq: [ny_rs.h_mfj_in_b5, {const: true}]}, then: mfj.b5.tax}
        - {guard: {op: test, eq: [ny_rs.h_mfj_in_b6, {const: true}]}, then: mfj.b6.tax}
        - {guard: {op: test, eq: [ny_rs.h_mfj_in_b7, {const: true}]}, then: mfj.b7.tax}
        - {guard: {op: test, eq: [ny_rs.h_mfj_in_b8, {const: true}]}, then: mfj.b8.tax}
        - {guard: {op: test, eq: [ny_rs.h_mfj_in_b9, {const: true}]}, then: mfj.b9.tax}
    shown_when: ny_rs.h_is_mfj

  # ---------------- Head of household ----------------
  - id: ny_rs.h_hoh_in_b1
    printed: "(helper)"
    label: "If line 38 is over $0 but not over $12,800"
    type: Bool
    expr: {op: test, le: [amount, {param: ny.rs.hoh.b1.upper}]}
  - id: ny_rs.h_hoh_show_b1
    printed: "(helper)"
    label: "Head of household schedule applies and line 38 is in band 1"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_hoh, {const: true}]}, {op: test, eq: [ny_rs.h_hoh_in_b1, {const: true}]}]}
  - id: hoh.b1.excess
    printed: "(band 1) (hoh.b1.excess)"
    label: "Line 38 (over $0)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.hoh.b1.over}}
    shown_when: ny_rs.h_hoh_show_b1
  - id: hoh.b1.product
    printed: "(band 1) (hoh.b1.product)"
    label: "4% of line 38"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: hoh.b1.excess, rate: {param: ny.rs.b1.rate}}
    shown_when: ny_rs.h_hoh_show_b1
  - id: ny_rs.h_hoh_b1_base_amt
    printed: "(helper)"
    label: "Base amount, band 1 ($0)"
    type: Dollars
    expr: {op: param, ref: ny.rs.hoh.b1.base}
  - id: hoh.b1.base
    printed: "(band 1) (hoh.b1.base)"
    label: "Base amount ($0)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_hoh_b1_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_hoh_show_b1
  - id: hoh.b1.tax
    printed: "The tax is (hoh.b1.tax)"
    label: "The tax is: 4% of line 38"
    type: NonNegDollars
    expr: {op: sum, of: [hoh.b1.base, hoh.b1.product]}
    shown_when: ny_rs.h_hoh_show_b1

  - id: ny_rs.h_hoh_in_b2
    printed: "(helper)"
    label: "If line 38 is over $12,800 but not over $17,650"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.hoh.b2.over}]}, {op: test, le: [amount, {param: ny.rs.hoh.b2.upper}]}]}
  - id: ny_rs.h_hoh_show_b2
    printed: "(helper)"
    label: "Head of household schedule applies and line 38 is in band 2"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_hoh, {const: true}]}, {op: test, eq: [ny_rs.h_hoh_in_b2, {const: true}]}]}
  - id: hoh.b2.excess
    printed: "(band 2) (hoh.b2.excess)"
    label: "The excess over $12,800"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.hoh.b2.over}}
    shown_when: ny_rs.h_hoh_show_b2
  - id: hoh.b2.product
    printed: "(band 2) (hoh.b2.product)"
    label: "4.5% of the excess over $12,800"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: hoh.b2.excess, rate: {param: ny.rs.b2.rate}}
    shown_when: ny_rs.h_hoh_show_b2
  - id: ny_rs.h_hoh_b2_base_amt
    printed: "(helper)"
    label: "$512"
    type: Dollars
    expr: {op: param, ref: ny.rs.hoh.b2.base}
  - id: hoh.b2.base
    printed: "(band 2) (hoh.b2.base)"
    label: "$512"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_hoh_b2_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_hoh_show_b2
  - id: hoh.b2.tax
    printed: "The tax is (hoh.b2.tax)"
    label: "The tax is: $512 plus 4.5% of the excess over $12,800"
    type: NonNegDollars
    expr: {op: sum, of: [hoh.b2.base, hoh.b2.product]}
    shown_when: ny_rs.h_hoh_show_b2

  - id: ny_rs.h_hoh_in_b3
    printed: "(helper)"
    label: "If line 38 is over $17,650 but not over $20,900"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.hoh.b3.over}]}, {op: test, le: [amount, {param: ny.rs.hoh.b3.upper}]}]}
  - id: ny_rs.h_hoh_show_b3
    printed: "(helper)"
    label: "Head of household schedule applies and line 38 is in band 3"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_hoh, {const: true}]}, {op: test, eq: [ny_rs.h_hoh_in_b3, {const: true}]}]}
  - id: hoh.b3.excess
    printed: "(band 3) (hoh.b3.excess)"
    label: "The excess over $17,650"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.hoh.b3.over}}
    shown_when: ny_rs.h_hoh_show_b3
  - id: hoh.b3.product
    printed: "(band 3) (hoh.b3.product)"
    label: "5.25% of the excess over $17,650"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: hoh.b3.excess, rate: {param: ny.rs.b3.rate}}
    shown_when: ny_rs.h_hoh_show_b3
  - id: ny_rs.h_hoh_b3_base_amt
    printed: "(helper)"
    label: "$730"
    type: Dollars
    expr: {op: param, ref: ny.rs.hoh.b3.base}
  - id: hoh.b3.base
    printed: "(band 3) (hoh.b3.base)"
    label: "$730"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_hoh_b3_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_hoh_show_b3
  - id: hoh.b3.tax
    printed: "The tax is (hoh.b3.tax)"
    label: "The tax is: $730 plus 5.25% of the excess over $17,650"
    type: NonNegDollars
    expr: {op: sum, of: [hoh.b3.base, hoh.b3.product]}
    shown_when: ny_rs.h_hoh_show_b3

  - id: ny_rs.h_hoh_in_b4
    printed: "(helper)"
    label: "If line 38 is over $20,900 but not over $107,650"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.hoh.b4.over}]}, {op: test, le: [amount, {param: ny.rs.hoh.b4.upper}]}]}
  - id: ny_rs.h_hoh_show_b4
    printed: "(helper)"
    label: "Head of household schedule applies and line 38 is in band 4"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_hoh, {const: true}]}, {op: test, eq: [ny_rs.h_hoh_in_b4, {const: true}]}]}
  - id: hoh.b4.excess
    printed: "(band 4) (hoh.b4.excess)"
    label: "The excess over $20,900"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.hoh.b4.over}}
    shown_when: ny_rs.h_hoh_show_b4
  - id: hoh.b4.product
    printed: "(band 4) (hoh.b4.product)"
    label: "5.5% of the excess over $20,900"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: hoh.b4.excess, rate: {param: ny.rs.b4.rate}}
    shown_when: ny_rs.h_hoh_show_b4
  - id: ny_rs.h_hoh_b4_base_amt
    printed: "(helper)"
    label: "$901"
    type: Dollars
    expr: {op: param, ref: ny.rs.hoh.b4.base}
  - id: hoh.b4.base
    printed: "(band 4) (hoh.b4.base)"
    label: "$901"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_hoh_b4_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_hoh_show_b4
  - id: hoh.b4.tax
    printed: "The tax is (hoh.b4.tax)"
    label: "The tax is: $901 plus 5.5% of the excess over $20,900"
    type: NonNegDollars
    expr: {op: sum, of: [hoh.b4.base, hoh.b4.product]}
    shown_when: ny_rs.h_hoh_show_b4

  - id: ny_rs.h_hoh_in_b5
    printed: "(helper)"
    label: "If line 38 is over $107,650 but not over $269,300"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.hoh.b5.over}]}, {op: test, le: [amount, {param: ny.rs.hoh.b5.upper}]}]}
  - id: ny_rs.h_hoh_show_b5
    printed: "(helper)"
    label: "Head of household schedule applies and line 38 is in band 5"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_hoh, {const: true}]}, {op: test, eq: [ny_rs.h_hoh_in_b5, {const: true}]}]}
  - id: hoh.b5.excess
    printed: "(band 5) (hoh.b5.excess)"
    label: "The excess over $107,650"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.hoh.b5.over}}
    shown_when: ny_rs.h_hoh_show_b5
  - id: hoh.b5.product
    printed: "(band 5) (hoh.b5.product)"
    label: "6% of the excess over $107,650"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: hoh.b5.excess, rate: {param: ny.rs.b5.rate}}
    shown_when: ny_rs.h_hoh_show_b5
  - id: ny_rs.h_hoh_b5_base_amt
    printed: "(helper)"
    label: "$5,672"
    type: Dollars
    expr: {op: param, ref: ny.rs.hoh.b5.base}
  - id: hoh.b5.base
    printed: "(band 5) (hoh.b5.base)"
    label: "$5,672"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_hoh_b5_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_hoh_show_b5
  - id: hoh.b5.tax
    printed: "The tax is (hoh.b5.tax)"
    label: "The tax is: $5,672 plus 6% of the excess over $107,650"
    type: NonNegDollars
    expr: {op: sum, of: [hoh.b5.base, hoh.b5.product]}
    shown_when: ny_rs.h_hoh_show_b5

  - id: ny_rs.h_hoh_in_b6
    printed: "(helper)"
    label: "If line 38 is over $269,300 but not over $1,616,450"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.hoh.b6.over}]}, {op: test, le: [amount, {param: ny.rs.hoh.b6.upper}]}]}
  - id: ny_rs.h_hoh_show_b6
    printed: "(helper)"
    label: "Head of household schedule applies and line 38 is in band 6"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_hoh, {const: true}]}, {op: test, eq: [ny_rs.h_hoh_in_b6, {const: true}]}]}
  - id: hoh.b6.excess
    printed: "(band 6) (hoh.b6.excess)"
    label: "The excess over $269,300"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.hoh.b6.over}}
    shown_when: ny_rs.h_hoh_show_b6
  - id: hoh.b6.product
    printed: "(band 6) (hoh.b6.product)"
    label: "6.85% of the excess over $269,300"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: hoh.b6.excess, rate: {param: ny.rs.b6.rate}}
    shown_when: ny_rs.h_hoh_show_b6
  - id: ny_rs.h_hoh_b6_base_amt
    printed: "(helper)"
    label: "$15,371"
    type: Dollars
    expr: {op: param, ref: ny.rs.hoh.b6.base}
  - id: hoh.b6.base
    printed: "(band 6) (hoh.b6.base)"
    label: "$15,371"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_hoh_b6_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_hoh_show_b6
  - id: hoh.b6.tax
    printed: "The tax is (hoh.b6.tax)"
    label: "The tax is: $15,371 plus 6.85% of the excess over $269,300"
    type: NonNegDollars
    expr: {op: sum, of: [hoh.b6.base, hoh.b6.product]}
    shown_when: ny_rs.h_hoh_show_b6

  - id: ny_rs.h_hoh_in_b7
    printed: "(helper)"
    label: "If line 38 is over $1,616,450 but not over $5,000,000"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.hoh.b7.over}]}, {op: test, le: [amount, {param: ny.rs.hoh.b7.upper}]}]}
  - id: ny_rs.h_hoh_show_b7
    printed: "(helper)"
    label: "Head of household schedule applies and line 38 is in band 7"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_hoh, {const: true}]}, {op: test, eq: [ny_rs.h_hoh_in_b7, {const: true}]}]}
  - id: hoh.b7.excess
    printed: "(band 7) (hoh.b7.excess)"
    label: "The excess over $1,616,450"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.hoh.b7.over}}
    shown_when: ny_rs.h_hoh_show_b7
  - id: hoh.b7.product
    printed: "(band 7) (hoh.b7.product)"
    label: "9.65% of the excess over $1,616,450"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: hoh.b7.excess, rate: {param: ny.rs.b7.rate}}
    shown_when: ny_rs.h_hoh_show_b7
  - id: ny_rs.h_hoh_b7_base_amt
    printed: "(helper)"
    label: "$107,651"
    type: Dollars
    expr: {op: param, ref: ny.rs.hoh.b7.base}
  - id: hoh.b7.base
    printed: "(band 7) (hoh.b7.base)"
    label: "$107,651"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_hoh_b7_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_hoh_show_b7
  - id: hoh.b7.tax
    printed: "The tax is (hoh.b7.tax)"
    label: "The tax is: $107,651 plus 9.65% of the excess over $1,616,450"
    type: NonNegDollars
    expr: {op: sum, of: [hoh.b7.base, hoh.b7.product]}
    shown_when: ny_rs.h_hoh_show_b7

  - id: ny_rs.h_hoh_in_b8
    printed: "(helper)"
    label: "If line 38 is over $5,000,000 but not over $25,000,000"
    type: Bool
    expr: {op: test, all: [{op: test, gt: [amount, {param: ny.rs.hoh.b8.over}]}, {op: test, le: [amount, {param: ny.rs.hoh.b8.upper}]}]}
  - id: ny_rs.h_hoh_show_b8
    printed: "(helper)"
    label: "Head of household schedule applies and line 38 is in band 8"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_hoh, {const: true}]}, {op: test, eq: [ny_rs.h_hoh_in_b8, {const: true}]}]}
  - id: hoh.b8.excess
    printed: "(band 8) (hoh.b8.excess)"
    label: "The excess over $5,000,000"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.hoh.b8.over}}
    shown_when: ny_rs.h_hoh_show_b8
  - id: hoh.b8.product
    printed: "(band 8) (hoh.b8.product)"
    label: "10.3% of the excess over $5,000,000"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: hoh.b8.excess, rate: {param: ny.rs.b8.rate}}
    shown_when: ny_rs.h_hoh_show_b8
  - id: ny_rs.h_hoh_b8_base_amt
    printed: "(helper)"
    label: "$434,163"
    type: Dollars
    expr: {op: param, ref: ny.rs.hoh.b8.base}
  - id: hoh.b8.base
    printed: "(band 8) (hoh.b8.base)"
    label: "$434,163"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_hoh_b8_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_hoh_show_b8
  - id: hoh.b8.tax
    printed: "The tax is (hoh.b8.tax)"
    label: "The tax is: $434,163 plus 10.3% of the excess over $5,000,000"
    type: NonNegDollars
    expr: {op: sum, of: [hoh.b8.base, hoh.b8.product]}
    shown_when: ny_rs.h_hoh_show_b8

  - id: ny_rs.h_hoh_in_b9
    printed: "(helper)"
    label: "If line 38 is over $25,000,000"
    type: Bool
    expr: {op: test, gt: [amount, {param: ny.rs.hoh.b9.over}]}
  - id: ny_rs.h_hoh_show_b9
    printed: "(helper)"
    label: "Head of household schedule applies and line 38 is over $25,000,000"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [ny_rs.h_is_hoh, {const: true}]}, {op: test, eq: [ny_rs.h_hoh_in_b9, {const: true}]}]}
  - id: hoh.b9.excess
    printed: "(band 9) (hoh.b9.excess)"
    label: "The excess over $25,000,000"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: amount, take: {param: ny.rs.hoh.b9.over}}
    shown_when: ny_rs.h_hoh_show_b9
  - id: hoh.b9.product
    printed: "(band 9) (hoh.b9.product)"
    label: "10.9% of the excess over $25,000,000"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: hoh.b9.excess, rate: {param: ny.rs.b9.rate}}
    shown_when: ny_rs.h_hoh_show_b9
  - id: ny_rs.h_hoh_b9_base_amt
    printed: "(helper)"
    label: "$2,494,163"
    type: Dollars
    expr: {op: param, ref: ny.rs.hoh.b9.base}
  - id: hoh.b9.base
    printed: "(band 9) (hoh.b9.base)"
    label: "$2,494,163"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: ny_rs.h_hoh_b9_base_amt, take: {const: 0}}
    shown_when: ny_rs.h_hoh_show_b9
  - id: hoh.b9.tax
    printed: "The tax is (hoh.b9.tax)"
    label: "The tax is: $2,494,163 plus 10.9% of the excess over $25,000,000"
    type: NonNegDollars
    expr: {op: sum, of: [hoh.b9.base, hoh.b9.product]}
    shown_when: ny_rs.h_hoh_show_b9

  - id: hoh.result
    printed: "The tax is (hoh.result)"
    label: "Head of household—filing status ④: The tax is"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [ny_rs.h_hoh_in_b1, {const: true}]}, then: hoh.b1.tax}
        - {guard: {op: test, eq: [ny_rs.h_hoh_in_b2, {const: true}]}, then: hoh.b2.tax}
        - {guard: {op: test, eq: [ny_rs.h_hoh_in_b3, {const: true}]}, then: hoh.b3.tax}
        - {guard: {op: test, eq: [ny_rs.h_hoh_in_b4, {const: true}]}, then: hoh.b4.tax}
        - {guard: {op: test, eq: [ny_rs.h_hoh_in_b5, {const: true}]}, then: hoh.b5.tax}
        - {guard: {op: test, eq: [ny_rs.h_hoh_in_b6, {const: true}]}, then: hoh.b6.tax}
        - {guard: {op: test, eq: [ny_rs.h_hoh_in_b7, {const: true}]}, then: hoh.b7.tax}
        - {guard: {op: test, eq: [ny_rs.h_hoh_in_b8, {const: true}]}, then: hoh.b8.tax}
        - {guard: {op: test, eq: [ny_rs.h_hoh_in_b9, {const: true}]}, then: hoh.b9.tax}
    shown_when: ny_rs.h_is_hoh

  - id: tax
    printed: "The tax is (tax)"
    label: "New York State tax rate schedule: The tax is (from the schedule for your filing status)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: {op: test, eq: [ny_rs.h_is_mfj, {const: true}]}, then: mfj.result}
        - {guard: {op: test, eq: [ny_rs.h_is_single, {const: true}]}, then: single.result}
        - {guard: {op: test, eq: [ny_rs.h_is_hoh, {const: true}]}, then: hoh.result}
    note: "Open points. (1) The schedule does not say how to round the percentage of the excess. I chose half-up to the cent, with no rounding to the dollar. (2) The schedule's opening sentence sends filers whose New York AGI (IT-201 line 33) is more than $107,650 to the tax computation worksheets. I left that routing to the calling line, because this schedule is computed only from line 38 (amount) and the filing status. (3) The schedule bands are 'over / but not over'. I encoded band 1 as amount not over its upper bound, since line 38 is not negative. (4) Filing status mfs uses the single schedule and qss uses the joint schedule, as the headings say."
```
```
