# Transcription agreement — carloan

Second transcription of `Qualified passenger vehicle loan interest (Schedule 1-A, line 22) — one entry per loan` by an isolated model (spec 6.5), compared line by line with `forms/2025/carloan.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 833a8a54ffa30755896dae43b479c31dde6f27748919ef74e44885067e5d4d72 |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 242f7244bf2433fd7b9d62a477efcd1831165cee975a648155aba2c673a2494a |
| printed lines compared | 1 |
| agree / disagree / missing | 0 / 1 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 109, 110 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 109, 110 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| fr-2025-24154 | Federal Register Vol. 91, No. 1 (2026-01-02), proposed rules REG-113515-25 (Car Loan Interest Deduction), FR Doc. 2025-24154 | 20, 21, 22 | cited pages | eccaf8550a66615e5932726cb4e98cab002b31b9f13c5d4ffec11f0619af479e | 20, 21, 22 | 1bb1f46bab043ddeabc4cb276a0d67fa478ae7aa38088b47ecfae848df4954c9 |
| i1040sc | 2025 | 6 | pages named by another document's citation | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |

## Lines

### 22(iii) — Qualified passenger vehicle loan interest less the amount in column (ii)
Status: **DISAGREE**

Project:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death"}, {"input": "carloan.kind"}], "test": "eq"}, {"args": [{"const": "original"}, {"input": "carloan.kind"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"input": "carloan.interest"}}, {"guard": {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"from": {"input": "carloan.nonqualifying"}, "op": "subtract_floor0", "take": {"input": "carloan.down"}}}, "places": 6, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"of": [{"input": "carloan.financed"}, {"input": "carloan.refi_balance"}], "op": "smaller_of"}, "places": 6, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "ne"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"line": "22(ii)"}}], "op": "choose"}}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "eq"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death"}, {"input": "carloan.kind"}], "test": "eq"}, {"args": [{"const": "original"}, {"input": "carloan.kind"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"input": "carloan.interest"}}, {"guard": {"args": [{"const": true}, {"input": "carloan.mixed"}], "test": "eq"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"from": {"input": "carloan.financed"}, "op": "subtract_floor0", "take": {"from": {"input": "carloan.nonqualifying"}, "op": "subtract_floor0", "take": {"input": "carloan.down"}}}, "places": 6, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"const": "refinanced"}, {"input": "carloan.kind"}], "test": "eq"}, "then": {"amount": {"input": "carloan.interest"}, "op": "prorate", "part": {"of": [{"input": "carloan.financed"}, {"input": "carloan.refi_balance"}], "op": "smaller_of"}, "places": 6, "whole": {"input": "carloan.financed"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "carloan.requirements"}], "test": "ne"}, {"args": [{"const": true}, {"input": "carloan.vehicle"}], "test": "ne"}], "test": "any"}, "then": {"param": "sales.zero"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}, {"const": 0}], "test": "le"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"const": 0}, {"collection": "person", "field": "person.sc_count", "op": "sum_over", "where": null}], "test": "lt"}, "then": {"ref": "carloan.col_ii_input"}}], "op": "choose"}}
```

Ruling: representation; replacing only param sales.zero with its declared NonNegDollars value zero and ref carloan.col_ii_input with its printed input marker 22(ii) makes the canonical trees exactly equal. The raw input is the same published question; every eligibility, method, allocation, rounding and ScheduleC guard remains untouched. i1040gi (2025) p.110 line22 columns(ii)/(iii) subtracts the elsewhere-deducted amount. This ruling addresses identifiers/constant aliases, not a new tax interpretation.

## Raw second transcription

```yaml
lines:
  - id: carloan.col_iii
    printed: "22(iii)"
    label: "Enter the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii)."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: carloan.qpvli, take: carloan.col_ii}
```
