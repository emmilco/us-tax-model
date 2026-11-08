# Transcription agreement — qbi

Second transcription of `Qualified business income and section 199A dividends — amounts and the choice of Form 8995` by an isolated model (spec 6.5), compared line by line with `forms/2025/qbi.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-21 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 27b850dd1c9eed6fc84f589cfdfd3fd170e6c8a834f07e525106a72efd0fdf42 |
| subject sha256 | 36aa33266cb50e80371e8f00f5728e2e75f9c427ce3ec58b5e6171f44216bbb6 |
| printed lines compared | 6 |
| agree / disagree / missing | 3 / 3 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |
| i8995 | 2025; printed date 2026-01-26 | 1, 3, 4 | cited pages | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 1, 3, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |
| f8995a | 2025; created 2025-09-12 | 1, 2 | whole document | 240927847d55e46348a41276d2bb81438c6fecae38b8106523444e56688c95b1 | - | c6abd31f2fb127536ba771d57a44e1487beebf502d934a3ebb8614e0508370d4 |
| i8995a | 2025; printed date 2026-01-26 | 1 | cited pages | 83411868381d4f5edbb455d348b480a63d96586bcb4f821f67acc0e027d5401d | 1 | 1843d02e5f17b6a3f1ba9d1ab3304a5c0b6862916c5ff0e622e3ccb411a89af3 |
| i8995-correction | Post-release correction to the 2025 Instructions for Form 8995 (published 2026-02-13); page last reviewed 2026-06-28 | 1 | whole document | 879132e6955e44a171e1d163d25d817e0c1a0d004bb9ab14b79e424dd3ab75eb | - | - |

## Lines

### qbi.zero — Year parameter sales.zero
Status: **AGREE**

### qbi.eligible — Amount from qbi.dividends_if_ordinary
Status: **AGREE**
Reviewed in: pass ae70b408bf57

### qbi.taxable_before — Taxable income before the QBI deduction; Form 1040 line 11a minus lines 12e and 13b, floor
Status: **DISAGREE**

Project:

```json
{"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"ref": "sa.line17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"ref": "sa.line17"}], "test": "lt"}], "test": "any"}, "then": {"ref": "sa.line17"}}], "op": "choose"}, {"ref": "f1040.line13b"}], "op": "sum"}}
```

Second:

```json
{"from": {"ref": "f1040.line11a"}, "op": "subtract_floor0", "take": {"of": [{"ref": "f1040.line12e"}, {"ref": "f1040.line13b"}], "op": "sum"}}
```

Second transcription's note: The line 11 instruction, as corrected after release, says line 11a minus lines 12e and 13b. It does not say what to do if the result is negative. The specification asks for a floor at zero, so this line enters zero when the result is zero or less.

Ruling: representation; project retained. As ruled before: the project reads Form 1040 line 11b (line 11a for a filer without the Schedule 1-A deduction, which is refused) and subtracts the Schedule A choice plus line 13b, the zero behind the Schedule 1-A refusal, as the corrected instruction reads (i8995-correction); the second subtracts lines 12e and 13b from line 11a directly, equal in value within the slice. Stage 14 did not change this line.

### qbi.net_capital_gain — Add sd.net_gain, f1040.line3a
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "div.any"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "div.any"}], "test": "eq"}, "then": {"input": "sb.ordinary_dividends"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "div.any"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "div.any"}], "test": "eq"}, "then": {"input": "sb.ordinary_dividends"}}], "op": "choose"}], "test": "lt"}, "then": {"ref": "f1040.line3a"}}], "op": "choose"}, {"from": {"of": [{"ref": "sd.line15"}, {"ref": "sd.line16"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "sum"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": 0}, {"ref": "sd.line14"}], "test": "le"}, {"args": [{"const": 0}, {"ref": "sd.line6"}], "test": "le"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"collection": "sales", "field": "sales.one", "op": "sum_over", "where": null}, {"const": 0, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "div.any"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "div.any"}], "test": "eq"}, "then": {"input": "sd.distributions"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sales", "field": "sales.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}], "test": "lt"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "sd.line17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "lt"}, {"args": [{"ref": "sd.line14"}, {"const": 0}], "test": "lt"}, {"args": [{"ref": "sd.line6"}, {"const": 0}], "test": "lt"}], "test": "any"}, "then": {"from": {"of": [{"ref": "sd.line15"}, {"ref": "sd.line16"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}
```

Second transcription's note: The supplied catalog has no Form 1040 line 7a. When Schedule D is not filed, I read line 7a as the capital gain distributions reported directly on Form 1040, which is sd.distributions_if_dividends. sd.filed is read as whether Schedule D is filed.

Ruling: model error; f8995 p. 1, line 12, "Enter your net capital gain, if any, increased by any qualified dividends", and i8995 p. 4, Line 12, "line 3a, plus your net capital gain": the candidate omits the qualified dividends (Form 1040 line 3a), which the project adds through f1040.line3a_if_ordinary. Ruled by reading: the scoped reply names interfaces the candidate bank does not resolve, as in the earlier line-scoped passes of this lane.
Reviewed in: pass ae70b408bf57

### qbi.deduction — Select Form 8995 or dividend-only Form 8995-A
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"ref": "sa.line17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"ref": "sa.line17"}], "test": "lt"}], "test": "any"}, "then": {"ref": "sa.line17"}}], "op": "choose"}, {"ref": "f1040.line13b"}], "op": "sum"}}, {"param": "qbi.threshold"}], "test": "le"}, "then": {"ref": "f8995.line15"}}, {"guard": {"args": [{"param": "qbi.threshold"}, {"from": {"ref": "f1040.line11b"}, "op": "subtract_floor0", "take": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, {"args": [{"ref": "sa.line17"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}], "test": "le"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "sa.elect_itemize"}], "test": "eq"}, {"args": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "eq"}], "test": "all"}, "then": {"param": "sales.zero"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"ref": "f1040.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "sa.spouse_itemizes"}], "test": "ne"}], "test": "any"}, "then": {"of": [{"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.age65"}], "test": "eq"}}, "op": "multiply_count"}, {"amount": {"param": "sa.standard_extra"}, "count": {"collection": "person", "field": "person.one", "op": "sum_over", "where": {"args": [{"const": true}, {"ref": "person.blind"}], "test": "eq"}}, "op": "multiply_count"}, {"param": "sa.standard_base"}], "op": "sum"}}], "op": "choose"}, {"ref": "sa.line17"}], "test": "lt"}], "test": "any"}, "then": {"ref": "sa.line17"}}], "op": "choose"}, {"ref": "f1040.line13b"}], "op": "sum"}}], "test": "lt"}, "then": {"ref": "f8995a.line39"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"from": {"ref": "f1040.line11a"}, "op": "subtract_floor0", "take": {"of": [{"ref": "f1040.line12e"}, {"ref": "f1040.line13b"}], "op": "sum"}}, {"param": "qbi.threshold"}], "test": "le"}, "then": {"ref": "f8995.line15"}}, {"guard": {"args": [{"param": "qbi.threshold"}, {"from": {"ref": "f1040.line11a"}, "op": "subtract_floor0", "take": {"of": [{"ref": "f1040.line12e"}, {"ref": "f1040.line13b"}], "op": "sum"}}], "test": "lt"}, "then": {"ref": "f8995a.line39"}}], "op": "choose"}
```

Second transcription's note: Form 8995 applies when taxable income is 'at or below' the threshold and you aren't a patron of a cooperative. Form 8995-A applies when it is 'above' the threshold, or when you are a patron. Patron status is covered by the qbi.unsupported screen. The 8995-A here is the dividend-only version, and its line 27 is zero. The text does not cover a Schedule C business whose QBI component needs Part II above the threshold; this transcription does not resolve that case.

Ruling: representation; project retained. The difference is that of qbi.taxable_before (line 11b and the Schedule A choice plus line 13b against line 11a less line 12e), equal in value within the slice; the Stage 14 selection between Form 8995 and Form 8995-A agrees on both sides.

### qbi.dividends_if_ordinary — Qualified section 199A dividends (Form 1099-DIV box 5), when ordinary dividends (box 1a) a
Status: **AGREE**
Reviewed in: pass ae70b408bf57

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| qbi.eligible | qbi.unsupported | - |
| qbi.deduction | qbi.unsupported | - |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| qbi.zero | d351e905679017dd4f47fae49b296df613ed439c812435776e137e37960346b9 |
| qbi.eligible | 9b7e22d855a63c8f95d7331310fe85280374f4e6ceb576fd806d13ac4095fcec |
| qbi.taxable_before | b83f0cad61a74d71f14d043cea5f54ced08d9f944f7c5fa4e5bb4d6b5a4302f0 |
| qbi.net_capital_gain | 7a116174b72815c5db82b7c6151c282b32fc369ff97504259084e21f7e00f4e4 |
| qbi.deduction | 8ad77c43b32b60307aca48df5f4cf13e85a666d68b12b6eb9508b6cadcb82f65 |
| qbi.dividends_if_ordinary | 6d42183163f2eea811b903beb9c5c3f876b45e26c0fac768ceb48a2618ac63d8 |
| (rest of the document) | 3ecd850aa0c9743f71e02cf3a8fda571cbba92fac4295ed77a1231fbce2a3a92 |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| qbi.eligible | e66873f691171d72092552d4220f3c910ccd051a8111596cd19a931d5e006938 |
| qbi.net_capital_gain | 108c0b63626e81123a19c71dbe5d2b7018d5e76ea04202a93685cfac2616d4a9 |
| qbi.dividends_if_ordinary | e66873f691171d72092552d4220f3c910ccd051a8111596cd19a931d5e006938 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass ae70b408bf57

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines qbi.eligible, qbi.net_capital_gain, qbi.dividends_if_ordinary |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | ae70b408bf573f1eb45ce0028f18786f0afe9ec5e9436f1b540eba9ccfd89de9 |
| prompt policy | source-only-computation-v3+lines-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | fail |
| required input context sha256 | e82a69c933ca712b34f24e69b49e44fb969e83e381c41c9cfe414cf853bdc5e7 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | e38c49bd38ae9425083dfea965f53460adc91e3096fbeeacd70169c6988bbe38 |
| receipt | .transcription/qbi.lines-ae59d28a6be3 |
| printed lines compared | 3 |
| agree / disagree / missing | 2 / 1 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f8995 | 2025; created 2025-09-12 | 1 | whole document | 49922587df3bd093e24470f5b42d0e3382ef8f5210b3cedccb02ccb864f2f65a | - | 8e2e78d7610e1d45e93c10c8b03f9026d46a1166678c6ed93f852569c382f346 |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |
| i8995 | 2025; printed date 2026-01-26 | 3, 4 | pages named by another document's citation | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 3, 4 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form, inputs and named lines: clcw.line10, clcw.prior_11, clcw.prior_14, clcw.prior_sd15, clcw.prior_sd21, clcw.prior_sd7, clcw.spouse_screen | clcw |
| named form, inputs and named lines: clcw26.line10 | clcw26 |
| named form, inputs and named lines: f1040.line11a, f1040.line25b, f1040.line25c_other, f1040.line26, f1040.line35a, f1040.line36, f1040.line3a, f1040.status, f1040.tax_exempt_interest | f1040 |
| named form, inputs and named lines: household.community_property, household.cp_married, household.credit_disallowed, household.home_cost, household.married, household.qss_eligible, household.rdp, household.spouse_died_2025, household.unmarried | household |
| named form, inputs and named lines: sa.charity_limited, sa.dependent, sa.elect_itemize, sa.excluded_income, sa.gambling_losses, sa.line1, sa.line11, sa.line5a, sa.line5b, sa.line5c, sa.line8a, sa.spouse_extra, sa.spouse_itemizes, sa.unsupported | sa |
| named form, inputs and named lines: sb.fbar_required, sb.form5471, sb.form8938, sb.line7a, sb.line8, sb.ordinary_dividends, sb.unsupported | sb |
| named form, inputs and named lines: scope.credits, scope.other_income, scope.other_line16, scope.schedule1 | scope |
| named form, inputs and named lines: sdtw.line10, sdtw.line15 | sdtw |
| named form, inputs and named lines: u1250.line10, u1250.line15 | u1250 |
| shared page | div, f8995, f8995a, person, sc, sd |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: qbi.dividends_if_ordinary
    printed: "(helper)"
    label: "Section 199A dividends (Form 1099-DIV box 5), the portion of box 1a that may be eligible for the 20% qualified business income deduction; counted only when there are ordinary dividends"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [div.has_ordinary, {const: true}]}
          then: qbi.dividends
        - guard: {op: test, eq: [div.has_ordinary, {const: false}]}
          then: div.zero
    note: "Form 1099-DIV says box 5 shows the portion of the amount in box 1a that may be eligible for the QBI deduction. So the box 5 amount is used only when box 1a dividends exist (div.has_ordinary). Otherwise the result is zero."

  - id: qbi.eligible
    printed: "(helper)"
    label: "Qualified REIT dividends and publicly traded partnership (PTP) income or (loss) (Form 8995, line 6): qualified REIT dividends reported on Form 1099-DIV, line 5"
    type: NonNegDollars
    expr: {op: copy, from: qbi.dividends_if_ordinary}
    refuses: [qbi.unsupported]
    note: "The IRS pages do not say what this interface name means. I read it as the qualified REIT dividends eligible for Form 8995 line 6. The i8995 text says these are reported on Form 1099-DIV, line 5. PTP income or loss and prior-year REIT/PTP loss carryforwards are outside the tool's scope, so the line refuses on qbi.unsupported. Under that reading the amount is the section 199A dividends. If another meaning was intended, such as total QBI, this line would need to be revised."

  - id: qbi.h_sd_smaller
    printed: "(helper)"
    label: "The smaller of Schedule D (Form 1040), line 15 or 16"
    type: Dollars
    expr: {op: smaller_of, of: [sd.line15, sd.line16]}

  - id: qbi.h_sd_gain
    printed: "(helper)"
    label: "Net capital gain when filing Schedule D: the smaller of Schedule D line 15 or 16, unless line 15 or 16 is zero or less, in which case nothing is added"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: qbi.h_sd_smaller, take: {const: 0}}

  - id: qbi.net_capital_gain
    printed: "(helper)"
    label: "Your net capital gain (Form 8995, line 12): if you're not required to file Schedule D, the amount on Form 1040 line 7a; if you file Schedule D, the smaller of Schedule D line 15 or 16, unless line 15 or 16 is zero or less, in which case nothing is added to the qualified dividends"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sd.filed, {const: true}]}
          then: qbi.h_sd_gain
        - guard: {op: test, eq: [sd.filed, {const: false}]}
          then: sd.distributions_if_dividends
    note: "The supplied catalog has no Form 1040 line 7a. When Schedule D is not filed, I read line 7a as the capital gain distributions reported directly on Form 1040, which is sd.distributions_if_dividends. sd.filed is read as whether Schedule D is filed."
```
```

## Raw second transcription

```yaml
```yaml
lines:
  - id: qbi.zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: qbi.eligible
    printed: "(helper)"
    label: "Qualified REIT dividends and publicly traded partnership (PTP) income or (loss) (Form 8995, line 6; Form 8995-A, line 28): qualified REIT dividends reported on Form 1099-DIV, box 5"
    type: NonNegDollars
    expr: {op: copy, from: qbi.dividends}
    refuses: [qbi.unsupported]
    note: "The instructions define qualified REIT dividends as the amount reported on Form 1099-DIV, line 5. PTP income or loss and other cases are covered by the qbi.unsupported screen. With that screen answered no, the amount is the section 199A dividends alone."

  - id: qbi.h_deductions_12e_13b
    printed: "(helper)"
    label: "Form 1040, lines 12e and 13b added together"
    type: NonNegDollars
    expr: {op: sum, of: [f1040.line12e, f1040.line13b]}

  - id: qbi.taxable_before
    printed: "(helper)"
    label: "Taxable income before qualified business income deduction: Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: f1040.line11a, take: qbi.h_deductions_12e_13b}
    note: "The line 11 instruction, as corrected after release, says line 11a minus lines 12e and 13b. It does not say what to do if the result is negative. The specification asks for a floor at zero, so this line enters zero when the result is zero or less."

  - id: qbi.net_capital_gain
    printed: "(helper)"
    label: "Enter your net capital gain, if any, increased by any qualified dividends: Form 1040, line 3a, plus your net capital gain"
    type: NonNegDollars
    expr: {op: sum, of: [sd.net_gain, f1040.line3a]}
    note: "Line 12 instructions: if Schedule D is filed, net capital gain is the smaller of Schedule D line 15 or 16, or nothing if either is zero or less. If Schedule D is not required, it is Form 1040 line 7a. This line relies on sd.net_gain to supply the non-negative net capital gain in both cases."

  - id: qbi.h_threshold
    printed: "(helper)"
    label: "Taxable income threshold for Form 8995: $197,300 ($394,600 if married filing jointly)"
    type: NonNegDollars
    expr: {op: param, ref: qbi.threshold}

  - id: qbi.h_at_or_below
    printed: "(helper)"
    label: "Taxable income before the QBI deduction is at or below $197,300 ($394,600 if married filing jointly)"
    type: Bool
    expr: {op: test, le: [qbi.taxable_before, qbi.h_threshold]}

  - id: qbi.h_above
    printed: "(helper)"
    label: "Taxable income before the QBI deduction is above $197,300 ($394,600 if married filing jointly)"
    type: Bool
    expr: {op: test, gt: [qbi.taxable_before, qbi.h_threshold]}

  - id: qbi.deduction
    printed: "(helper)"
    label: "Qualified business income deduction: Form 8995, line 15, if taxable income before the QBI deduction is at or below $197,300 ($394,600 if married filing jointly); otherwise Form 8995-A, line 39"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - {guard: qbi.h_at_or_below, then: f8995.line15}
        - {guard: qbi.h_above, then: f8995a.line39}
    refuses: [qbi.unsupported]
    note: "Form 8995 applies when taxable income is 'at or below' the threshold and you aren't a patron of a cooperative. Form 8995-A applies when it is 'above' the threshold, or when you are a patron. Patron status is covered by the qbi.unsupported screen. The 8995-A here is the dividend-only version, and its line 27 is zero. The text does not cover a Schedule C business whose QBI component needs Part II above the threshold; this transcription does not resolve that case."
```
```
