# Transcription agreement — sd

Second transcription of `Schedule D — securities sales and supplied distribution subtotals` by an isolated model (spec 6.5), compared line by line with `forms/2025/sd.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | a21c9c82a88ee547363f18049fb3a40b2115562a77c41976ef430cf72810d8b7 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | ab5e2b69c8f5cc07c5ea96e58b0cbce15837c5194bb2a2cafd35890846aa5882 |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 970194c9c6b868f34407d059bec48ad22672e5fe0cd1bbf4cd15d395f038b5c7 |
| printed lines compared | 54 |
| agree / disagree / missing | 9 / 45 / 0 |
| extra printed lines in second | 18, 19 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | eb461181b39879c79d1c0b7761ca0cd9ade46fdb1531cdee3281053c348f6c41 |
| i1040sd | 2025; printed date 2025-12-11 | 11, 12, 15 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Host-side model expression type checks

The build's reference/type checker rejected these model expressions; none were executed.
- sd.sd.__type_gate_6: collection reference requires sum_over
- sd.sd.__type_gate_6: comparison operands have incompatible types
- sd.sd.__type_gate_7: collection reference requires sum_over
- sd.sd.__type_gate_7: comparison operands have incompatible types

## Lines

### sd.line18 — Line 18. 28% Rate Gain Worksheet result, or zero when line 17 is No (lines 18 through 21 s
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}
```

Second:

```json
{"expression": {"const": 0}, "invalid_model_types": [{"line": "sd.line18", "message": "sd.sd.__type_gate_6: collection reference requires sum_over"}, {"line": "sd.line18", "message": "sd.sd.__type_gate_6: comparison operands have incompatible types"}]}
```

Second transcription's note: The 28% Rate Gain Worksheet itself is not in the supplied pages; absent collectibles or QSB stock sales (sales.special false), the amount is taken as zero.

Ruling: model error; this adjudicates the declaration, not the tax reading. The reply declares refuses: [sales.special] on this line, a collection field used as a scalar gate; the host check rejects it as sd.sd.__type_gate_6 ("collection reference requires sum_over"; "comparison operands have incompatible types"; triage/sd.deepseek.json, state invalid), so the line cannot be executed. For the record: its constant 0 agrees with the BUG-0149 fix when line 17 is No but omits box 2d when line 17 is Yes (i1040sd p. 2, Capital Gain Distributions: "If there is an amount in box 2d, include that amount on line 4 of the 28% Rate Gain Worksheet in these instructions if you complete line 18 of Schedule D", a page not given), and its note that the 28% Rate Gain Worksheet "is not in the supplied pages" is wrong (i1040sd p. 11 was given).

### sd.line19 — Line 19. Unrecaptured Section 1250 Gain Worksheet result, or zero when line 17 is No (line
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}
```

Second:

```json
{"expression": {"const": 0}, "invalid_model_types": [{"line": "sd.line19", "message": "sd.sd.__type_gate_7: collection reference requires sum_over"}, {"line": "sd.line19", "message": "sd.sd.__type_gate_7: comparison operands have incompatible types"}]}
```

Second transcription's note: The Unrecaptured Section 1250 Gain Worksheet itself is not in the supplied pages; absent section 1250 property or similar sales (sales.special false), the amount is taken as zero.

Ruling: model error; this adjudicates the declaration, not the tax reading. The reply declares refuses: [sales.special] on this line, a collection field used as a scalar gate; the host check rejects it as sd.sd.__type_gate_7 ("collection reference requires sum_over"; "comparison operands have incompatible types"; triage/sd.deepseek.json, state invalid), so the line cannot be executed. For the record: its constant 0 agrees with the BUG-0149 fix when line 17 is No, but the given i1040sd p. 12 makes the worksheet apply when "You received a Form 1099-DIV ... that reports “unrecaptured section 1250 gain”", so a constant 0 does not follow the given text even though the worksheet itself (i1040sd p. 13) was not supplied.

### sd.filing4952 — Are you filing Form 4952?
Status: **AGREE**

### sd.investment_election — Form 4952 line 4g (supplied subtotal; Form 4952 deferred to Stage 4)
Status: **AGREE**

### sd.filed — Schedule D required for entered sales or special distribution gains
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sales", "field": "sales.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}], "test": "lt"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "lt"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"const": true}, {"input": "sd.carryover"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sd.other_forms"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "sales", "field": "sales.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"input": "sd.distributions"}], "test": "lt"}], "test": "any"}
```

Ruling: model error; Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. The candidate requires Schedule D whenever any capital gain distribution is entered (sd.distributions > 0), besides sales, other source forms and a carryover. The page it was given contradicts that: i1040gi p. 38, "If you don’t have to file Schedule D and you received capital gain distributions, be sure you checked the box on Form 1040 or 1040-SR, line 7b", and the deciding rule is i1040gi p. 31, Line 7a, Exception 1: "You don't have to file Form 8949 or Schedule D if ... 1. You have no capital losses, and your only capital gains are capital gain distributions from Form(s) 1099-DIV, box 2a ...; and 2. None of the Form(s) 1099-DIV ... have an amount in box 2b (unrecaptured section 1250 gain), box 2c (section 1202 gain), or box 2d (collectibles (28%) gain)." (p. 31, not given). On a return whose only capital gains are box 2a distributions with no amount in boxes 2b–2d the candidate reports Schedule D required where the source does not; with boxes 2b or 2d it agrees with the project, whose sd.line18 and sd.line19 tests capture them. Project stands.

### sd.zero — No amount on an inapplicable line
Status: **AGREE**

### sd.to1040 — Capital gain or limited capital loss for Form 1040 line 7a
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "le"}, "then": {"line": "16"}}, {"guard": {"args": [{"line": "16"}, {"const": 0}], "test": "lt"}, "then": {"line": "21"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "eq"}, "then": {"from": {"const": 0}, "op": "subtract", "take": {"const": 0}}}, {"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "lt"}, "then": {"line": "16"}}, {"guard": {"args": [{"line": "16"}, {"const": 0}], "test": "lt"}, "then": {"line": "21"}}], "op": "choose"}
```

Ruling: representation; f1040sd p. 2, line 16: "If line 16 is zero, skip lines 17 through 21 below and enter -0- on Form 1040, 1040-SR, or 1040-NR, line 7a." Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. The candidate's zero branch (0 − 0) equals line 16 when line 16 is zero; otherwise it enters line 16 for a gain and line 21 for a loss, as the project does. Its line 16 agrees with the project's and its line 21 equals the project's on every input (see 21), so the expressions agree in value; the identical Claude expression agreed on every in-scope comparison (triage/sd.json, 1,630 of 1,714; only cited refusals). Project stands.

### sd.net_gain — Nonnegative net capital gain for QDCGT
Status: **DISAGREE**

Project:

```json
{"from": {"of": [{"line": "15"}, {"line": "16"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second:

```json
{"of": [{"from": {"line": "15"}, "op": "subtract_floor0", "take": {"const": 0}}, {"from": {"line": "16"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}
```

Ruling: representation; i1040gi p. 38, Qualified Dividends and Capital Gain Tax Worksheet line 3: "Yes. Enter the smaller of line 15 or line 16 of Schedule D. If either line 15 or line 16 is blank or a loss, enter -0-." Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. The candidate floors each of lines 15 and 16 at zero and takes the smaller; the project takes the smaller and floors it. min(max(a,0), max(b,0)) = max(min(a,b), 0) for every a and b, so the two are equal on every input. Project stands.

### 1a(d) — Line 1a, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 1a: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums column (d) proceeds over box A or box G on the aggregate route as printed, with no screening; the project sums box A on the aggregate route behind sd.screen, which refuses box G entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 1a(e) — Line 1a, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 1a: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums column (e) basis over box A or box G on the aggregate route as printed, with no screening; the project sums box A on the aggregate route behind sd.screen, which refuses box G entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 1a(g) — Line 1a, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 1a: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums column (g) adjustments over box A or box G on the aggregate route as printed, with no screening; the project sums box A on the aggregate route behind sd.screen, which refuses box G entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 1a(h) — Line 1a, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 1a: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums column (h) gain or loss over box A or box G on the aggregate route as printed, with no screening; the project sums box A on the aggregate route behind sd.screen, which refuses box G entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 1b(d) — Line 1b, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 1b: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked". The candidate sums column (d) proceeds over box A or box G on the detail route as printed, with no screening; the project sums box A on the detail route behind sd.screen, which refuses box G entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 1b(e) — Line 1b, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 1b: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked". The candidate sums column (e) basis over box A or box G on the detail route as printed, with no screening; the project sums box A on the detail route behind sd.screen, which refuses box G entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 1b(g) — Line 1b, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 1b: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked". The candidate sums column (g) adjustments over box A or box G on the detail route as printed, with no screening; the project sums box A on the detail route behind sd.screen, which refuses box G entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 1b(h) — Line 1b, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "G"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 1b: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked". The candidate sums column (h) gain or loss over box A or box G on the detail route as printed, with no screening; the project sums box A on the detail route behind sd.screen, which refuses box G entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 2(d) — Line 2, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "H"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 2: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked". The candidate sums column (d) proceeds over box B or box H on the detail route as printed, with no screening; the project sums box B on the detail route behind sd.screen, which refuses box H entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 2(e) — Line 2, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "H"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 2: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked". The candidate sums column (e) basis over box B or box H on the detail route as printed, with no screening; the project sums box B on the detail route behind sd.screen, which refuses box H entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 2(g) — Line 2, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "H"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 2: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked". The candidate sums column (g) adjustments over box B or box H on the detail route as printed, with no screening; the project sums box B on the detail route behind sd.screen, which refuses box H entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 2(h) — Line 2, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "H"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 2: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked". The candidate sums column (h) gain or loss over box B or box H on the detail route as printed, with no screening; the project sums box B on the detail route behind sd.screen, which refuses box H entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 3(d) — Line 3, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "I"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 3: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked". The candidate sums column (d) proceeds over box C or box I on the detail route as printed, with no screening; the project sums box C on the detail route behind sd.screen, which refuses box I entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 3(e) — Line 3, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "I"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 3: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked". The candidate sums column (e) basis over box C or box I on the detail route as printed, with no screening; the project sums box C on the detail route behind sd.screen, which refuses box I entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 3(g) — Line 3, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "I"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 3: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked". The candidate sums column (g) adjustments over box C or box I on the detail route as printed, with no screening; the project sums box C on the detail route behind sd.screen, which refuses box I entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 3(h) — Line 3, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "I"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 3: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked". The candidate sums column (h) gain or loss over box C or box I on the detail route as printed, with no screening; the project sums box C on the detail route behind sd.screen, which refuses box I entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 8a(d) — Line 8a, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 8a: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums column (d) proceeds over box D or box J on the aggregate route as printed, with no screening; the project sums box D on the aggregate route behind sd.screen, which refuses box J entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 8a(e) — Line 8a, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 8a: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums column (e) basis over box D or box J on the aggregate route as printed, with no screening; the project sums box D on the aggregate route behind sd.screen, which refuses box J entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 8a(g) — Line 8a, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 8a: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums column (g) adjustments over box D or box J on the aggregate route as printed, with no screening; the project sums box D on the aggregate route behind sd.screen, which refuses box J entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 8a(h) — Line 8a, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 8a: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums column (h) gain or loss over box D or box J on the aggregate route as printed, with no screening; the project sums box D on the aggregate route behind sd.screen, which refuses box J entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 8b(d) — Line 8b, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 8b: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked". The candidate sums column (d) proceeds over box D or box J on the detail route as printed, with no screening; the project sums box D on the detail route behind sd.screen, which refuses box J entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 8b(e) — Line 8b, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 8b: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked". The candidate sums column (e) basis over box D or box J on the detail route as printed, with no screening; the project sums box D on the detail route behind sd.screen, which refuses box J entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 8b(g) — Line 8b, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 8b: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked". The candidate sums column (g) adjustments over box D or box J on the detail route as printed, with no screening; the project sums box D on the detail route behind sd.screen, which refuses box J entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 8b(h) — Line 8b, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "J"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 8b: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked". The candidate sums column (h) gain or loss over box D or box J on the detail route as printed, with no screening; the project sums box D on the detail route behind sd.screen, which refuses box J entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 9(d) — Line 9, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "K"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 9: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked". The candidate sums column (d) proceeds over box E or box K on the detail route as printed, with no screening; the project sums box E on the detail route behind sd.screen, which refuses box K entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 9(e) — Line 9, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "K"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 9: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked". The candidate sums column (e) basis over box E or box K on the detail route as printed, with no screening; the project sums box E on the detail route behind sd.screen, which refuses box K entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 9(g) — Line 9, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "K"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 9: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked". The candidate sums column (g) adjustments over box E or box K on the detail route as printed, with no screening; the project sums box E on the detail route behind sd.screen, which refuses box K entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 9(h) — Line 9, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "K"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 9: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked". The candidate sums column (h) gain or loss over box E or box K on the detail route as printed, with no screening; the project sums box E on the detail route behind sd.screen, which refuses box K entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 10(d) — Line 10, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "L"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 10: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked". The candidate sums column (d) proceeds over box F or box L on the detail route as printed, with no screening; the project sums box F on the detail route behind sd.screen, which refuses box L entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 10(e) — Line 10, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "L"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 10: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked". The candidate sums column (e) basis over box F or box L on the detail route as printed, with no screening; the project sums box F on the detail route behind sd.screen, which refuses box L entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 10(g) — Line 10, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "L"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 10: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked". The candidate sums column (g) adjustments over box F or box L on the detail route as printed, with no screening; the project sums box F on the detail route behind sd.screen, which refuses box L entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 10(h) — Line 10, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "L"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Ruling: scope; f1040sd p. 1, line 10: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked". The candidate sums column (h) gain or loss over box F or box L on the detail route as printed, with no screening; the project sums box F on the detail route behind sd.screen, which refuses box L entries through sales.one (sales.digital, f8949 Parts I and II, boxes G–L). Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. Within scope both sum the same entries; the filters differ only on digital-asset entries the project refuses (T-003). Corroboration: the Claude candidate's filter for this line, which adds the same box, agreed on every in-scope comparison (triage/sd.json: 1,552 of 1,714, no value difference, 82 project-refuses, 80 project-unknown). Project stands.

### 4 — Line 4: zero only after unsupported source/carryover screening
Status: **DISAGREE**

Project:

```json
{"const": 0}
```

Second:

```json
{"from": {"const": 0}, "op": "subtract", "take": {"const": 0}}
```

Ruling: representation; f1040sd p. 1, line 4: "Short-term gain from Form 6252 and short-term gain or (loss) from Forms 4684, 6781, and 8824". Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. The candidate enters 0 − 0 and declares refuses: [sd.other_forms]; the project enters 0 behind the same screen, which sd.count and sd.screen apply before any Schedule D amount (sd.other_forms answered yes refuses the return). The values are identical on every input; only the expression's form differs. Project stands.

### 5 — Line 5: zero only after unsupported source/carryover screening
Status: **DISAGREE**

Project:

```json
{"const": 0}
```

Second:

```json
{"from": {"const": 0}, "op": "subtract", "take": {"const": 0}}
```

Ruling: representation; f1040sd p. 1, line 5: "Net short-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1". Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. The candidate enters 0 − 0 and declares refuses: [sd.other_forms]; the project enters 0 behind the same screen, which sd.count and sd.screen apply before any Schedule D amount (sd.other_forms answered yes refuses the return). The values are identical on every input; only the expression's form differs. Project stands.

### 6 — Line 6: zero only after unsupported source/carryover screening
Status: **DISAGREE**

Project:

```json
{"const": 0}
```

Second:

```json
{"from": {"const": 0}, "op": "subtract", "take": {"const": 0}}
```

Ruling: representation; f1040sd p. 1, line 6: "Short-term capital loss carryover". Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. The candidate enters 0 − 0 and declares refuses: [sd.carryover]; the project enters 0 behind the same screen, which sd.count and sd.screen apply before any Schedule D amount (sd.carryover answered yes refuses the return). The values are identical on every input; only the expression's form differs. Project stands.

### 11 — Line 11: zero only after unsupported source/carryover screening
Status: **DISAGREE**

Project:

```json
{"const": 0}
```

Second:

```json
{"from": {"const": 0}, "op": "subtract", "take": {"const": 0}}
```

Ruling: representation; f1040sd p. 1, line 11: "Gain from Form 4797, Part I; long-term gain from Forms 2439 and 6252; and long-term gain or (loss) from Forms 4684, 6781, and 8824". Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. The candidate enters 0 − 0 and declares refuses: [sd.other_forms]; the project enters 0 behind the same screen, which sd.count and sd.screen apply before any Schedule D amount (sd.other_forms answered yes refuses the return). The values are identical on every input; only the expression's form differs. Project stands.

### 12 — Line 12: zero only after unsupported source/carryover screening
Status: **DISAGREE**

Project:

```json
{"const": 0}
```

Second:

```json
{"from": {"const": 0}, "op": "subtract", "take": {"const": 0}}
```

Ruling: representation; f1040sd p. 1, line 12: "Net long-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1". Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. The candidate enters 0 − 0 and declares refuses: [sd.other_forms]; the project enters 0 behind the same screen, which sd.count and sd.screen apply before any Schedule D amount (sd.other_forms answered yes refuses the return). The values are identical on every input; only the expression's form differs. Project stands.

### 14 — Line 14: zero only after unsupported source/carryover screening
Status: **DISAGREE**

Project:

```json
{"const": 0}
```

Second:

```json
{"from": {"const": 0}, "op": "subtract", "take": {"const": 0}}
```

Ruling: representation; f1040sd p. 1, line 14: "Long-term capital loss carryover". Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. The candidate enters 0 − 0 and declares refuses: [sd.carryover]; the project enters 0 behind the same screen, which sd.count and sd.screen apply before any Schedule D amount (sd.carryover answered yes refuses the return). The values are identical on every input; only the expression's form differs. Project stands.

### 13 — Capital gain distributions
Status: **AGREE**

### 7 — Combine the amounts for Schedule D line 7
Status: **AGREE**

### 15 — Combine the amounts for Schedule D line 15
Status: **AGREE**

### 16 — Combine the amounts for Schedule D line 16
Status: **AGREE**

### 17 — Are lines 15 and 16 both gains?
Status: **AGREE**

### 20 — Are lines 18 and 19 zero and are you not filing Form 4952?
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "eq"}, {"args": [{"ref": "f4952.line5"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line1"}, {"ref": "f4952.line4c"}], "test": "lt"}], "test": "all"}, {"args": [{"ref": "f4952.line1"}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"expression": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "eq"}, {"args": [{"ref": "f4952.line5"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line1"}, {"ref": "f4952.line4c"}], "test": "lt"}], "test": "all"}, {"args": [{"ref": "f4952.line1"}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"line": "18"}, {"const": 0}], "test": "le"}, {"args": [{"line": "19"}, {"const": 0}], "test": "le"}], "test": "all"}, "invalid_model_types": [{"line": "sd.line18", "message": "sd.sd.__type_gate_6: collection reference requires sum_over"}, {"line": "sd.line18", "message": "sd.sd.__type_gate_6: comparison operands have incompatible types"}, {"line": "sd.line19", "message": "sd.sd.__type_gate_7: collection reference requires sum_over"}, {"line": "sd.line19", "message": "sd.sd.__type_gate_7: comparison operands have incompatible types"}]}
```

Ruling: model error; this adjudicates the declaration, not the tax reading. f1040sd p. 2, line 20: "Are lines 18 and 19 both zero or blank and you are not filing Form 4952?" The candidate's predicate reads its lines 18 and 19, whose refusal declarations (refuses: [sales.special]) fail the host checks as sd.sd.__type_gate_6 and __type_gate_7 (triage/sd.deepseek.json, state invalid), so this line's dependency closure carries the validation failure and cannot be executed.

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "16"}, {"const": 0}], "test": "lt"}, "then": {"of": [{"line": "16"}, {"param": "sd.loss_limit"}], "op": "larger_of"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "le"}, "then": {"from": {"const": 0}, "op": "subtract", "take": {"const": 0}}}, {"guard": {"args": [{"line": "16"}, {"const": 0}], "test": "lt"}, "then": {"from": {"const": 0}, "op": "subtract", "take": {"of": [{"from": {"const": 0}, "op": "subtract", "take": {"line": "16"}}, {"from": {"const": 0}, "op": "subtract", "take": {"param": "sd.loss_limit"}}], "op": "smaller_of"}}}], "op": "choose"}
```

Ruling: representation; f1040sd p. 2, line 21: "If line 16 is a loss, enter here and on Form 1040 ... the smaller of: • The loss on line 16; or • ($3,000), or if married filing separately, ($1,500) ... Note: When figuring which amount is smaller, treat both amounts as positive numbers." Triage could not execute this reply (triage/sd.deepseek.json, state invalid: the refusal declarations of sd.line18 and sd.line19 name the collection field sales.special and fail the host checks as sd.sd.__type_gate_6 and __type_gate_7); this line's expression and dependency closure contain neither, so it is ruled by reading. The project enters larger_of(line 16, sd.loss_limit) for a loss; the candidate enters 0 − smaller_of(0 − line 16, 0 − sd.loss_limit). sd.loss_limit is negative (params/2025.yaml: −$3,000, −$1,500 married filing separately), so the candidate's value is −min(|loss|, |limit|) = max(line 16, limit), the project's value; both enter 0 when line 16 is not a loss. Project stands.

### 22 — Do you have qualified dividends?
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sd.line18 | sales.special | sales.special |
| sd.line19 | sales.special | sales.special |
| sd.to1040 | sd.carryover, sd.other_forms | - |
| sd.net_gain | sd.carryover, sd.other_forms | - |
| 4 | sd.other_forms | - |
| 5 | sd.other_forms | - |
| 6 | sd.carryover | - |
| 11 | sd.other_forms | - |
| 12 | sd.other_forms | - |
| 14 | sd.carryover | - |
| 7 | sd.carryover, sd.other_forms | - |
| 15 | sd.carryover, sd.other_forms | - |
| 16 | sd.carryover, sd.other_forms | - |
| 17 | sd.carryover, sd.other_forms | - |
| 20 | sales.special | sales.special |
| 21 | sd.carryover, sd.other_forms | - |

## Raw second transcription

```yaml
lines:
  - id: sd.line1a.d
    printed: "1a(d)"
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments, column (d), Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "A"}]}
              - {op: test, eq: ["sales.box", {const: "G"}]}
  - id: sd.line1a.e
    printed: "1a(e)"
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments, column (e), Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "A"}]}
              - {op: test, eq: ["sales.box", {const: "G"}]}
  - id: sd.line1a.g
    printed: "1a(g)"
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments, column (g), Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "A"}]}
              - {op: test, eq: ["sales.box", {const: "G"}]}
  - id: sd.line1a.h
    printed: "1a(h)"
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments, column (h), Gain or (loss)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "A"}]}
              - {op: test, eq: ["sales.box", {const: "G"}]}
  - id: sd.line1b.d
    printed: "1b(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked, column (d), Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "A"}]}
              - {op: test, eq: ["sales.box", {const: "G"}]}
  - id: sd.line1b.e
    printed: "1b(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked, column (e), Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "A"}]}
              - {op: test, eq: ["sales.box", {const: "G"}]}
  - id: sd.line1b.g
    printed: "1b(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked, column (g), Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "A"}]}
              - {op: test, eq: ["sales.box", {const: "G"}]}
  - id: sd.line1b.h
    printed: "1b(h)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked, column (h), Gain or (loss)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "A"}]}
              - {op: test, eq: ["sales.box", {const: "G"}]}
  - id: sd.line2.d
    printed: "2(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked, column (d), Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "B"}]}
              - {op: test, eq: ["sales.box", {const: "H"}]}
  - id: sd.line2.e
    printed: "2(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked, column (e), Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "B"}]}
              - {op: test, eq: ["sales.box", {const: "H"}]}
  - id: sd.line2.g
    printed: "2(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked, column (g), Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "B"}]}
              - {op: test, eq: ["sales.box", {const: "H"}]}
  - id: sd.line2.h
    printed: "2(h)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked, column (h), Gain or (loss)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "B"}]}
              - {op: test, eq: ["sales.box", {const: "H"}]}
  - id: sd.line3.d
    printed: "3(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked, column (d), Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "C"}]}
              - {op: test, eq: ["sales.box", {const: "I"}]}
  - id: sd.line3.e
    printed: "3(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked, column (e), Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "C"}]}
              - {op: test, eq: ["sales.box", {const: "I"}]}
  - id: sd.line3.g
    printed: "3(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked, column (g), Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "C"}]}
              - {op: test, eq: ["sales.box", {const: "I"}]}
  - id: sd.line3.h
    printed: "3(h)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked, column (h), Gain or (loss)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "C"}]}
              - {op: test, eq: ["sales.box", {const: "I"}]}
  - id: sd.line8a.d
    printed: "8a(d)"
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments, column (d), Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "D"}]}
              - {op: test, eq: ["sales.box", {const: "J"}]}
  - id: sd.line8a.e
    printed: "8a(e)"
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments, column (e), Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "D"}]}
              - {op: test, eq: ["sales.box", {const: "J"}]}
  - id: sd.line8a.g
    printed: "8a(g)"
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments, column (g), Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "D"}]}
              - {op: test, eq: ["sales.box", {const: "J"}]}
  - id: sd.line8a.h
    printed: "8a(h)"
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments, column (h), Gain or (loss)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "D"}]}
              - {op: test, eq: ["sales.box", {const: "J"}]}
  - id: sd.line8b.d
    printed: "8b(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked, column (d), Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "D"}]}
              - {op: test, eq: ["sales.box", {const: "J"}]}
  - id: sd.line8b.e
    printed: "8b(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked, column (e), Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "D"}]}
              - {op: test, eq: ["sales.box", {const: "J"}]}
  - id: sd.line8b.g
    printed: "8b(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked, column (g), Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "D"}]}
              - {op: test, eq: ["sales.box", {const: "J"}]}
  - id: sd.line8b.h
    printed: "8b(h)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked, column (h), Gain or (loss)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "D"}]}
              - {op: test, eq: ["sales.box", {const: "J"}]}
  - id: sd.line9.d
    printed: "9(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked, column (d), Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "E"}]}
              - {op: test, eq: ["sales.box", {const: "K"}]}
  - id: sd.line9.e
    printed: "9(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked, column (e), Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "E"}]}
              - {op: test, eq: ["sales.box", {const: "K"}]}
  - id: sd.line9.g
    printed: "9(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked, column (g), Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "E"}]}
              - {op: test, eq: ["sales.box", {const: "K"}]}
  - id: sd.line9.h
    printed: "9(h)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked, column (h), Gain or (loss)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "E"}]}
              - {op: test, eq: ["sales.box", {const: "K"}]}
  - id: sd.line10.d
    printed: "10(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked, column (d), Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "F"}]}
              - {op: test, eq: ["sales.box", {const: "L"}]}
  - id: sd.line10.e
    printed: "10(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked, column (e), Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "F"}]}
              - {op: test, eq: ["sales.box", {const: "L"}]}
  - id: sd.line10.g
    printed: "10(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked, column (g), Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "F"}]}
              - {op: test, eq: ["sales.box", {const: "L"}]}
  - id: sd.line10.h
    printed: "10(h)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked, column (h), Gain or (loss)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - {op: test, eq: ["sales.route", {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: ["sales.box", {const: "F"}]}
              - {op: test, eq: ["sales.box", {const: "L"}]}
  - id: sd.line4
    printed: "4"
    label: "Short-term gain from Form 6252 and short-term gain or (loss) from Forms 4684, 6781, and 8824"
    type: Dollars
    expr: {op: copy, from: sd.h_zero_dollars}
    refuses: [sd.other_forms]
  - id: sd.line5
    printed: "5"
    label: "Net short-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1"
    type: Dollars
    expr: {op: copy, from: sd.h_zero_dollars}
    refuses: [sd.other_forms]
  - id: sd.line6
    printed: "6"
    label: "Short-term capital loss carryover. Enter the amount, if any, from line 8 of your Capital Loss Carryover Worksheet in the instructions"
    type: Dollars
    expr: {op: copy, from: sd.h_zero_dollars}
    refuses: [sd.carryover]
  - id: sd.line11
    printed: "11"
    label: "Gain from Form 4797, Part I; long-term gain from Forms 2439 and 6252; and long-term gain or (loss) from Forms 4684, 6781, and 8824"
    type: Dollars
    expr: {op: copy, from: sd.h_zero_dollars}
    refuses: [sd.other_forms]
  - id: sd.line12
    printed: "12"
    label: "Net long-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1"
    type: Dollars
    expr: {op: copy, from: sd.h_zero_dollars}
    refuses: [sd.other_forms]
  - id: sd.line14
    printed: "14"
    label: "Long-term capital loss carryover. Enter the amount, if any, from line 13 of your Capital Loss Carryover Worksheet in the instructions"
    type: Dollars
    expr: {op: copy, from: sd.h_zero_dollars}
    refuses: [sd.carryover]
  - id: sd.line13
    printed: "13"
    label: "Capital gain distributions. See the instructions"
    type: NonNegDollars
    expr: {op: copy, from: sd.distributions}
  - id: sd.line7
    printed: "7"
    label: "Net short-term capital gain or (loss). Combine lines 1a through 6 in column (h). If you have any long-term capital gains or losses, go to Part II below. Otherwise, go to Part III on the back"
    type: Dollars
    expr:
      op: sum
      of: [sd.line1a.h, sd.line1b.h, sd.line2.h, sd.line3.h, sd.line4, sd.line5, sd.line6]
  - id: sd.line15
    printed: "15"
    label: "Net long-term capital gain or (loss). Combine lines 8a through 14 in column (h). Then, go to Part III on the back"
    type: Dollars
    expr:
      op: sum
      of: [sd.line8a.h, sd.line8b.h, sd.line9.h, sd.line10.h, sd.line11, sd.line12, sd.line13, sd.line14]
  - id: sd.line16
    printed: "16"
    label: "Combine lines 7 and 15 and enter the result"
    type: Dollars
    expr: {op: sum, of: [sd.line7, sd.line15]}
  - id: sd.line17
    printed: "17"
    label: "Are lines 15 and 16 both gains?"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, gt: [sd.line15, {const: 0}]}
        - {op: test, gt: [sd.line16, {const: 0}]}
  - id: sd.line20
    printed: "20"
    label: "Are lines 18 and 19 both zero or blank and you are not filing Form 4952?"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [sd.line18, {const: 0}]}
        - {op: test, eq: [sd.line19, {const: 0}]}
        - {op: test, eq: [sd.filing4952, {const: false}]}
  - id: sd.line21
    printed: "21"
    label: "If line 16 is a loss, enter here and on Form 1040, 1040-SR, or 1040-NR, line 7a, the smaller of the loss on line 16 or ($3,000), or if married filing separately, ($1,500). When figuring which amount is smaller, treat both amounts as positive numbers"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, lt: [sd.line16, {const: 0}]}
          then: sd.h_line21_negative
        - guard: {op: test, ge: [sd.line16, {const: 0}]}
          then: sd.h_zero_dollars
  - id: sd.line22
    printed: "22"
    label: "Do you have qualified dividends on Form 1040, 1040-SR, or 1040-NR, line 3a?"
    type: Bool
    expr: {op: test, gt: [f1040.line3a, {const: 0}]}
  - id: sd.line18
    printed: "18"
    label: "If you are required to complete the 28% Rate Gain Worksheet (see instructions), enter the amount, if any, from line 7 of that worksheet"
    type: NonNegDollars
    expr: {op: copy, from: sd.zero}
    refuses: [sales.special]
    note: "The 28% Rate Gain Worksheet itself is not in the supplied pages; absent collectibles or QSB stock sales (sales.special false), the amount is taken as zero."
  - id: sd.line19
    printed: "19"
    label: "If you are required to complete the Unrecaptured Section 1250 Gain Worksheet (see instructions), enter the amount, if any, from line 18 of that worksheet"
    type: NonNegDollars
    expr: {op: copy, from: sd.zero}
    refuses: [sales.special]
    note: "The Unrecaptured Section 1250 Gain Worksheet itself is not in the supplied pages; absent section 1250 property or similar sales (sales.special false), the amount is taken as zero."
  - id: sd.filing4952
    printed: "(helper)"
    label: "Whether Form 4952 is filed"
    type: Bool
    expr: {op: copy, from: f4952.required}
  - id: sd.investment_election
    printed: "(helper)"
    label: "Amount from Form 4952, line 4g, elected into investment income"
    type: NonNegDollars
    expr: {op: copy, from: f4952.line4g}
  - id: sd.filed
    printed: "(helper)"
    label: "Whether Schedule D is filed"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [sd.h_sales_count, {const: 0, type: Count}]}
        - {op: test, gt: [sd.distributions, {const: 0}]}
        - {op: test, eq: [sd.other_forms, {const: true}]}
        - {op: test, eq: [sd.carryover, {const: true}]}
  - id: sd.zero
    printed: "(helper)"
    label: "Zero dollars"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: sd.to1040
    printed: "(helper)"
    label: "Amount from Schedule D to enter on Form 1040, line 7a"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, gt: [sd.line16, {const: 0}]}
          then: sd.line16
        - guard: {op: test, lt: [sd.line16, {const: 0}]}
          then: sd.line21
        - guard: {op: test, eq: [sd.line16, {const: 0}]}
          then: sd.h_zero_dollars
  - id: sd.net_gain
    printed: "(helper)"
    label: "Net capital gain for the qualified dividends and capital gain tax worksheet"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sd.h_line15_pos, sd.h_line16_pos]}
  - id: sd.h_zero_dollars
    printed: "(helper)"
    label: "Zero dollars"
    type: Dollars
    expr: {op: subtract, from: sd.zero, take: {param: sales.zero}}
  - id: sd.h_sales_count
    printed: "(helper)"
    label: "Number of sales entries"
    type: Count
    expr: {op: sum_over, collection: sales, field: sales.one}
  - id: sd.h_line15_pos
    printed: "(helper)"
    label: "Schedule D line 15 floored at zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sd.line15, take: {const: 0}}
  - id: sd.h_line16_pos
    printed: "(helper)"
    label: "Schedule D line 16 floored at zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sd.line16, take: {const: 0}}
  - id: sd.h_loss16_abs
    printed: "(helper)"
    label: "Absolute amount of the line 16 loss"
    type: Dollars
    expr: {op: subtract, from: sd.zero, take: sd.line16}
  - id: sd.h_loss_limit_abs
    printed: "(helper)"
    label: "Absolute amount of the capital loss limit"
    type: Dollars
    expr: {op: subtract, from: sd.zero, take: {param: sd.loss_limit}}
  - id: sd.h_loss_capped_abs
    printed: "(helper)"
    label: "Smaller of the line 16 loss and the capital loss limit, as a positive amount"
    type: Dollars
    expr: {op: smaller_of, of: [sd.h_loss16_abs, sd.h_loss_limit_abs]}
  - id: sd.h_line21_negative
    printed: "(helper)"
    label: "Line 21 loss amount"
    type: Dollars
    expr: {op: subtract, from: sd.zero, take: sd.h_loss_capped_abs}
```
