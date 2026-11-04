# Transcription agreement — sd

Second transcription of `Schedule D — securities sales and supplied distribution subtotals` by an isolated model (spec 6.5), compared line by line with `forms/2025/sd.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 10c58a98143cf5cf0a002683bb03cd8d6a8020f41255c0a79a6e357345bc7dbc |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 90467c69e064c50329298b4f941f680cb2def518e72995c405d882ce05374f8d |
| type validation policy | project-expression-types-v3 |
| model type validation | fail |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 14f6c7571f90fea7fd4da5231e18ae13294ab3b969700f9e50a613b3212a083f |
| printed lines compared | 55 |
| agree / disagree / missing | 11 / 44 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | eb461181b39879c79d1c0b7761ca0cd9ade46fdb1531cdee3281053c348f6c41 |
| i1040sd | 2025; printed date 2025-12-11 | 10, 11, 12, 15 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040gi | 2025; printed date 2026-02-25 | 31, 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Host-side model expression type checks

The build's reference/type checker rejected these model expressions; none were executed.
- sd.sd.__type_gate_6: collection reference requires sum_over
- sd.sd.__type_gate_6: comparison operands have incompatible types

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

Second transcription's note: No 28% Rate Gain Worksheet fields are supplied; this line is zero when no collectibles or other unsupported special gain is present, and refuses otherwise.

Ruling: model error; this adjudicates the declaration, not the tax reading. The reply declares a refusal on this line naming the collection field sales.special as a scalar gate; the host check rejects it (sd.sd.__type_gate_6: "collection reference requires sum_over"; "comparison operands have incompatible types"; triage `reviews/2025/transcription/triage/sd.deepseek.json`, invalid_lines sd.line18 and sd.line20), so it was not executed (2,115 candidate-invalid, 332 on completed returns). For the record: its constant 0 omits the Form 1099-DIV box 2d trigger (i1040sd p. 2, Capital Gain Distributions: "If there is an amount in box 2d, include that amount on line 4 of the 28% Rate Gain Worksheet"), a page the reviewer still was not given (i1040sd pp. 10, 11, 12, 15), as in Stage 20 (interface gap there). The project's g28.line7 behind line 17 Yes is the BUG-0149 fix. Project stands.

### sd.line19 — Line 19. Unrecaptured Section 1250 Gain Worksheet result, or zero when line 17 is No (line
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}
```

Second:

```json
{"ref": "u1250.line18"}
```

Ruling: model error; f1040sd p. 2, line 17: "No. Skip lines 18 through 21, and go to line 22"; i1040sd p. 11, Line 19: "If you checked “Yes” on line 17, complete the Unrecaptured Section 1250 Gain Worksheet". The candidate copies u1250.line18 without the line 17 guard, so it shows the worksheet result on a skipped line. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 808 of 2,115 comparisons agree; 1,240 candidate-unknown, 53 project-refuses, 9 value, 4 project-unknown, 1 candidate-refuses (by return: {"completed": {"candidate-unknown": 134, "value": 2}, "incomplete": {"candidate-unknown": 705, "project-unknown": 4}, "refused": {"candidate-refuses": 1, "candidate-unknown": 401, "project-refuses": 53, "value": 7}}). The 9 value differences all have line 17 No (project $0): generated 162 $6,330.85 (completed), generated 188 $9,215.81 (completed), generated 196 $204.79 (refused), generated 201 $7,886.38 (refused), generated 205 $392.17 (refused), generated 223 $9,399.96 (refused), generated 344 $7,402.32 (refused), generated 354 $4,170.32 (refused), generated 474 $0.02 (refused). The 1,240 candidate-unknown (134 on completed returns) all need clcw.spouse_screen: the candidate's lines 6 and 14 (which match the project's expressions, so they are not open) declare refuses: [clcw.spouse_screen], a refusal evaluated on every return, while the screen is asked only through the Capital Loss Carryover Worksheet when sd.carryover is Yes; every one of the 1,240 witnesses is a fixture whose sd.carryover is No (i1040sd p. 10: "Otherwise, you don’t have any carryovers"). A candidate that needs an answer the source does not need is a model error (README). The 53 project-refuses are cited gates read through u1250 (sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[a].special 1, sales[s3].digital 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s3].wash_bad 1, sales[s2].bad_code 1, sales[s1].special 1); the candidate-refuses (sales[a].wash_bad 1) is on a refused return. Project stands.

### sd.filing4952 — Are you filing Form 4952?
Status: **AGREE**

### sd.investment_election — Form 4952 line 4g (supplied subtotal; Form 4952 deferred to Stage 4)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"ref": "f4952.line4g"}], "test": "lt"}, "then": {"ref": "f4952.line4g"}}], "op": "choose"}
```

Second:

```json
{"ref": "f4952.line4g"}
```

Ruling: scope; i1040sd p. 15, Schedule D Tax Worksheet, line 3: "Enter the amount from Form 4952 ..., line 4g". The candidate copies the Form 4952 line 4g answer; the project copies f4952.election, the same amount behind Form 4952's cited gates (f4952.bad_election, f4952.unsupported, f4952.alternative_allocation) and the Schedule D and Form 1099-DIV screens its check reads. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,037 of 2,115 comparisons agree; 74 project-refuses, 4 project-unknown (by return: {"incomplete": {"project-unknown": 3}, "refused": {"project-refuses": 74, "project-unknown": 1}}). No value differs. Project refusals: f4952.bad_election 43, div.bad_components 9, f4952.unsupported 5, sd.other_forms 5, f4952.alternative_allocation 3, div.unsupported 2, sales[s1].digital 2, sales[s1].bad_aggregate 1, sales[s1].bad_code 1, sales[s3].digital 1, sales[s3].wash_bad 1, sales[s2].digital 1 (the one sales[s3].wash_bad refusal is generated 310, a generated invalid wash-sale entry the generator keeps raw on purpose so the new entry-error gate is exercised; refused return); project-unknown: sales[s2].aggregate_eligible 2, f4952.alternative_allocation 1, sd.distributions 1. Project stands.

### sd.filed — Schedule D required for entered sales, special distribution gains or a capital loss carryo
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sales", "field": "sales.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}], "test": "lt"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "lt"}, {"args": [{"line": "14"}, {"const": 0}], "test": "lt"}, {"args": [{"line": "6"}, {"const": 0}], "test": "lt"}], "test": "any"}
```

Second:

```json
{"ref": "qdcg.schedule_d_filed"}
```

Ruling: model error; i1040gi p. 31, Line 7a, Exception 1 ("You have no capital losses, and your only capital gains are capital gain distributions ... None of the Form(s) 1099-DIV ... have an amount in box 2b ..., box 2c ..., or box 2d"). The candidate copies qdcg.schedule_d_filed, which is itself a copy of sd.filed (forms/2025/qdcg.yaml, "Are you filing Schedule D?"), so the line is defined by itself and states no filing rule. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 148 of 2,115 comparisons agree; 1,870 candidate-unknown, 97 project-refuses (by return: {"completed": {"candidate-unknown": 332}, "incomplete": {"candidate-unknown": 728}, "refused": {"candidate-unknown": 810, "project-refuses": 97}}); every candidate-unknown is "cycle at sd.filed" (332 on completed returns). The project refusals are cited gates. Project stands.

### sd.zero — No amount on an inapplicable line
Status: **AGREE**

### sd.has_loss — Line 16 is a loss
Status: **AGREE**

### sd.to1040 — Capital gain or limited capital loss for Form 1040 line 7a
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "le"}, "then": {"line": "16"}}, {"guard": {"args": [{"line": "16"}, {"const": 0}], "test": "lt"}, "then": {"line": "21"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "lt"}, "then": {"line": "16"}}, {"guard": {"args": [{"line": "16"}, {"const": 0}], "test": "lt"}, "then": {"line": "21"}}], "op": "choose"}
```

Ruling: model error; f1040sd p. 2, line 16: "If line 16 is zero, skip lines 17 through 21 below and enter -0- on Form 1040, 1040-SR, or 1040-NR, line 7a". The expression is algebraically the project's (an extra zero branch equal to line 16 when line 16 is zero), and no value differs, but the candidate cannot compute on gate-No returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 779 of 2,115 comparisons agree; 1,240 candidate-unknown, 92 project-refuses, 4 project-unknown (by return: {"completed": {"candidate-unknown": 134}, "incomplete": {"candidate-unknown": 705, "project-unknown": 4}, "refused": {"candidate-unknown": 401, "project-refuses": 92}}). The 1,240 candidate-unknown (134 on completed returns) all need clcw.spouse_screen: the candidate's lines 6 and 14 (which match the project's expressions, so they are not open) declare refuses: [clcw.spouse_screen], a refusal evaluated on every return, while the screen is asked only through the Capital Loss Carryover Worksheet when sd.carryover is Yes; every one of the 1,240 witnesses is a fixture whose sd.carryover is No (i1040sd p. 10: "Otherwise, you don’t have any carryovers"). A candidate that needs an answer the source does not need is a model error (README). The project refusals are cited Schedule D and Form 1099-DIV gates (div.bad_components 18, sales[s1].digital 17, div.unsupported 11, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, div.section1202 5, div.amt 4, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, div.bad_special 2, sales[a].special 1, sales[s3].digital 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1); the project-unknown withhold sales screen answers. Project stands.

### sd.net_gain — Nonnegative net capital gain for QDCGT
Status: **DISAGREE**

Project:

```json
{"from": {"of": [{"line": "15"}, {"line": "16"}], "op": "smaller_of"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second:

```json
{"from": {"line": "16"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Ruling: model error; i1040gi p. 38, Qualified Dividends and Capital Gain Tax Worksheet, line 3: "Enter the smaller of line 15 or line 16 of Schedule D. If either line 15 or line 16 is blank or a loss, enter -0-". The candidate enters line 16 floored at zero and ignores line 15, so it overstates the net capital gain whenever line 15 is less than line 16 (a net short-term loss). executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 690 of 2,115 comparisons agree; 1,240 candidate-unknown, 92 project-refuses, 89 value, 4 project-unknown (by return: {"completed": {"candidate-unknown": 134, "value": 32}, "incomplete": {"candidate-unknown": 705, "project-unknown": 4, "value": 2}, "refused": {"candidate-unknown": 401, "project-refuses": 92, "value": 55}}). In all 89 value differences the candidate is larger than the project. The 32 on completed returns (project against candidate): classm.f4952.2.deepseek $3,358.00 against $9,316.00; classm.f1040.2.deepseek $1,237.00 against $50,930.00; classm.s8812.2.deepseek $18,447.00 against $21,701.00; classm.s8812.3.deepseek $71,995.00 against $156,839.00; classm.f1040.2 $1,237.00 against $50,930.00; mutation.t2.mfj_sdtw_skip23 $3,358.00 against $9,316.00; generated 22 $0.18 against $0.25; generated 29 $51,144.32 against $81,681.40; generated 89 $36,654.85 against $44,606.42; generated 101 $0.17 against $4,967.01; generated 148 $15,173.73 against $34,090.59; generated 149 $0.00 against $19,656.22; generated 174 $14,804.39 against $61,973.49; generated 188 $0.00 against $2,677.79; generated 224 $9,994.36 against $13,365.38; generated 236 $18,417.36 against $45,250.56; generated 255 $5,632.14 against $75,507.35; generated 257 $53,455.18 against $53,455.33; generated 269 $0.14 against $38,142.35; generated 312 $0.00 against $85,581.52; generated 345 $0.00 against $0.15; generated 346 $410.55 against $20,131.12; generated 348 $10,998.32 against $43,497.84; generated 366 $178.09 against $11,781.62; generated 367 $76,541.23 against $104,048.88; generated 373 $0.00 against $37,432.25; generated 396 $42,991.32 against $60,354.44; generated 433 $0.00 against $22,406.16; generated 436 $15,925.23 against $77,744.10; generated 437 $0.14 against $41,775.04; generated 445 $0.00 against $31,251.60; generated 447 $0.04 against $3,219.67; the other 57 are on refused or incomplete returns (e.g. classm.g28.2 $16,981.00 against $64,515.00). The 1,240 candidate-unknown (134 on completed returns) all need clcw.spouse_screen: the candidate's lines 6 and 14 (which match the project's expressions, so they are not open) declare refuses: [clcw.spouse_screen], a refusal evaluated on every return, while the screen is asked only through the Capital Loss Carryover Worksheet when sd.carryover is Yes; every one of the 1,240 witnesses is a fixture whose sd.carryover is No (i1040sd p. 10: "Otherwise, you don’t have any carryovers"). A candidate that needs an answer the source does not need is a model error (README). Project stands.

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

Ruling: scope; f1040sd p. 1, line 1a, column (d). The candidate sums box A or its digital-asset counterpart on the aggregate route; the project sums box A behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 1a, column (e). The candidate sums box A or its digital-asset counterpart on the aggregate route; the project sums box A behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 1a, column (g). The candidate sums box A or its digital-asset counterpart on the aggregate route; the project sums box A behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 1a, column (h). The candidate sums box A or its digital-asset counterpart on the aggregate route; the project sums box A behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 1b, column (d). The candidate sums box A or its digital-asset counterpart on the detail route; the project sums box A behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 1b, column (e). The candidate sums box A or its digital-asset counterpart on the detail route; the project sums box A behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 1b, column (g). The candidate sums box A or its digital-asset counterpart on the detail route; the project sums box A behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 1b, column (h). The candidate sums box A or its digital-asset counterpart on the detail route; the project sums box A behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 2, column (d). The candidate sums box B or its digital-asset counterpart on the detail route; the project sums box B behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 2, column (e). The candidate sums box B or its digital-asset counterpart on the detail route; the project sums box B behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 2, column (g). The candidate sums box B or its digital-asset counterpart on the detail route; the project sums box B behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,001 of 2,115 comparisons agree; 70 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 70, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[a].special 1, sales[s3].digital 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 2, column (h). The candidate sums box B or its digital-asset counterpart on the detail route; the project sums box B behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,001 of 2,115 comparisons agree; 70 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 70, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[a].special 1, sales[s3].digital 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 3, column (d). The candidate sums box C or its digital-asset counterpart on the detail route; the project sums box C behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 3, column (e). The candidate sums box C or its digital-asset counterpart on the detail route; the project sums box C behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 3, column (g). The candidate sums box C or its digital-asset counterpart on the detail route; the project sums box C behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 3, column (h). The candidate sums box C or its digital-asset counterpart on the detail route; the project sums box C behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 8a, column (d). The candidate sums box D or its digital-asset counterpart on the aggregate route; the project sums box D behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 8a, column (e). The candidate sums box D or its digital-asset counterpart on the aggregate route; the project sums box D behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 8a, column (g). The candidate sums box D or its digital-asset counterpart on the aggregate route; the project sums box D behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 8a, column (h). The candidate sums box D or its digital-asset counterpart on the aggregate route; the project sums box D behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 8b, column (d). The candidate sums box D or its digital-asset counterpart on the detail route; the project sums box D behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 8b, column (e). The candidate sums box D or its digital-asset counterpart on the detail route; the project sums box D behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 8b, column (g). The candidate sums box D or its digital-asset counterpart on the detail route; the project sums box D behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 8b, column (h). The candidate sums box D or its digital-asset counterpart on the detail route; the project sums box D behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 9, column (d). The candidate sums box E or its digital-asset counterpart on the detail route; the project sums box E behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 9, column (e). The candidate sums box E or its digital-asset counterpart on the detail route; the project sums box E behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 9, column (g). The candidate sums box E or its digital-asset counterpart on the detail route; the project sums box E behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 9, column (h). The candidate sums box E or its digital-asset counterpart on the detail route; the project sums box E behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 10, column (d). The candidate sums box F or its digital-asset counterpart on the detail route; the project sums box F behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 10, column (e). The candidate sums box F or its digital-asset counterpart on the detail route; the project sums box F behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 10, column (g). The candidate sums box F or its digital-asset counterpart on the detail route; the project sums box F behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: scope; f1040sd p. 1, line 10, column (h). The candidate sums box F or its digital-asset counterpart on the detail route; the project sums box F behind sd.screen. Boxes G–L are refused at the transaction (sales.one through sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), so the added boxes reach only refused returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,000 of 2,115 comparisons agree; 71 project-refuses, 44 project-unknown (by return: {"incomplete": {"project-unknown": 35}, "refused": {"project-refuses": 71, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 40, sales[s1].special 2, sales[s2].aggregate_eligible 2 (withheld screen answers). No value differs. Same expression as Stage 20 (scope). Project stands.

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

Ruling: representation; f1040sd p. 1, line 4: "Short-term gain from Form 6252 and short-term gain or (loss) from Forms 4684, 6781, and 8824". The candidate's 0 − 0 equals the project's 0; the source forms are refused by sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,115 of 2,115 comparisons agree; no difference (by return: {}). Algebraically equal. Project stands.

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

Ruling: representation; f1040sd p. 1, line 5: "Net short-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1". The candidate's 0 − 0 equals the project's 0; the source forms are refused by sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,115 of 2,115 comparisons agree; no difference (by return: {}). Algebraically equal. Project stands.

### 6 — Short-term capital loss carryover, from line 8 of the Capital Loss Carryover Worksheet (a
Status: **AGREE**

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

Ruling: representation; f1040sd p. 1, line 11: "Gain from Form 4797, Part I; long-term gain from Forms 2439 and 6252; and long-term gain or (loss) from Forms 4684, 6781, and 8824". The candidate's 0 − 0 equals the project's 0; the source forms are refused by sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,115 of 2,115 comparisons agree; no difference (by return: {}). Algebraically equal. Project stands.

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

Ruling: representation; f1040sd p. 1, line 12: "Net long-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1". The candidate's 0 − 0 equals the project's 0; the source forms are refused by sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,115 of 2,115 comparisons agree; no difference (by return: {}). Algebraically equal. Project stands.

### 14 — Long-term capital loss carryover, from line 13 of the Capital Loss Carryover Worksheet (a
Status: **AGREE**

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
{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "eq"}, {"args": [{"ref": "f4952.line5"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line1"}, {"ref": "f4952.line4c"}], "test": "lt"}], "test": "all"}, {"args": [{"ref": "f4952.line3"}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"alternatives": [{"guard": {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"ref": "f4952.line4g"}], "test": "lt"}, "then": {"ref": "f4952.line4g"}}], "op": "choose"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"args": [{"ref": "f4952.line1"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "f4952.carryover"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"expression": {"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "eq"}, {"args": [{"ref": "f4952.line5"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line1"}, {"ref": "f4952.line4c"}], "test": "lt"}], "test": "all"}, {"args": [{"ref": "f4952.line3"}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"alternatives": [{"guard": {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"ref": "f4952.line4g"}], "test": "lt"}, "then": {"ref": "f4952.line4g"}}], "op": "choose"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"args": [{"ref": "f4952.line1"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "f4952.carryover"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"const": 0}, {"const": 0}], "test": "eq"}, {"args": [{"ref": "u1250.line18"}, {"const": 0}], "test": "le"}], "test": "all"}, "invalid_model_types": [{"line": "sd.line18", "message": "sd.sd.__type_gate_6: collection reference requires sum_over"}, {"line": "sd.line18", "message": "sd.sd.__type_gate_6: comparison operands have incompatible types"}]}
```

Ruling: model error; this adjudicates the declaration, not the tax reading. f1040sd p. 2, line 20: "Are lines 18 and 19 both zero or blank and you are not filing Form 4952?". The candidate's predicate reads its line 18, whose refusal declaration fails the host check (sd.sd.__type_gate_6, "collection reference requires sum_over"), so the line was not executed (triage `reviews/2025/transcription/triage/sd.deepseek.json`: 2,115 candidate-invalid, 332 on completed returns). For the record it also tests 0 = 0 in place of line 18 and an unguarded u1250.line18 in place of line 19; the project's line 20 reads both behind line 17 (BUG-0149). Project stands.

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "16"}, {"const": 0}], "test": "lt"}, "then": {"of": [{"line": "16"}, {"param": "sd.loss_limit"}], "op": "larger_of"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "16"}, {"const": 0}], "test": "lt"}, "then": {"from": {"const": 0}, "op": "subtract", "take": {"of": [{"from": {"const": 0}, "op": "subtract", "take": {"line": "16"}}, {"from": {"const": 0}, "op": "subtract", "take": {"param": "sd.loss_limit"}}], "op": "smaller_of"}}}], "op": "choose"}
```

Ruling: model error; f1040sd p. 2, line 21: "If line 16 is a loss, enter here and on Form 1040 ... the smaller of: • The loss on line 16; or • ($3,000), or if married filing separately, ($1,500) ... treat both amounts as positive numbers." The expression, 0 − smaller_of(0 − line 16, 0 − sd.loss_limit), equals the project's larger_of(line 16, sd.loss_limit) because sd.loss_limit is negative (params/2025.yaml), and no value differs, but the candidate cannot compute on gate-No returns. executable-triage-v2 (`reviews/2025/transcription/triage/sd.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 779 of 2,115 comparisons agree; 1,240 candidate-unknown, 92 project-refuses, 4 project-unknown (by return: {"completed": {"candidate-unknown": 134}, "incomplete": {"candidate-unknown": 705, "project-unknown": 4}, "refused": {"candidate-unknown": 401, "project-refuses": 92}}). The 1,240 candidate-unknown (134 on completed returns) all need clcw.spouse_screen: the candidate's lines 6 and 14 (which match the project's expressions, so they are not open) declare refuses: [clcw.spouse_screen], a refusal evaluated on every return, while the screen is asked only through the Capital Loss Carryover Worksheet when sd.carryover is Yes; every one of the 1,240 witnesses is a fixture whose sd.carryover is No (i1040sd p. 10: "Otherwise, you don’t have any carryovers"). A candidate that needs an answer the source does not need is a model error (README). The project refusals are cited gates. Project stands.

### 22 — Do you have qualified dividends?
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sd.line18 | sales.special, sd.other_forms | sales.special |
| sd.has_loss | clcw.spouse_screen, sd.other_forms | - |
| sd.to1040 | clcw.spouse_screen, sd.other_forms | - |
| sd.net_gain | clcw.spouse_screen, sd.other_forms | - |
| 4 | sd.other_forms | - |
| 5 | sd.other_forms | - |
| 6 | clcw.spouse_screen | - |
| 11 | sd.other_forms | - |
| 12 | sd.other_forms | - |
| 14 | clcw.spouse_screen | - |
| 7 | clcw.spouse_screen, sd.other_forms | - |
| 15 | clcw.spouse_screen, sd.other_forms | - |
| 16 | clcw.spouse_screen, sd.other_forms | - |
| 17 | clcw.spouse_screen, sd.other_forms | - |
| 20 | sales.special, sd.other_forms | sales.special |
| 21 | clcw.spouse_screen, sd.other_forms | - |

## Raw second transcription

```yaml
lines:
  - id: sd.line1a.d
    printed: "1a(d)"
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments — Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "A"}]
              - op: test
                eq: [sales.box, {const: "G"}]
          - op: test
            eq: [sales.route, {const: "aggregate"}]
  - id: sd.line1a.e
    printed: "1a(e)"
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments — Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "A"}]
              - op: test
                eq: [sales.box, {const: "G"}]
          - op: test
            eq: [sales.route, {const: "aggregate"}]
  - id: sd.line1a.g
    printed: "1a(g)"
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments — Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "A"}]
              - op: test
                eq: [sales.box, {const: "G"}]
          - op: test
            eq: [sales.route, {const: "aggregate"}]
  - id: sd.line1a.h
    printed: "1a(h)"
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "A"}]
              - op: test
                eq: [sales.box, {const: "G"}]
          - op: test
            eq: [sales.route, {const: "aggregate"}]
  - id: sd.line1b.d
    printed: "1b(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked — Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "A"}]
              - op: test
                eq: [sales.box, {const: "G"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line1b.e
    printed: "1b(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked — Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "A"}]
              - op: test
                eq: [sales.box, {const: "G"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line1b.g
    printed: "1b(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked — Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "A"}]
              - op: test
                eq: [sales.box, {const: "G"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line1b.h
    printed: "1b(h)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "A"}]
              - op: test
                eq: [sales.box, {const: "G"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line2.d
    printed: "2(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked — Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "B"}]
              - op: test
                eq: [sales.box, {const: "H"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line2.e
    printed: "2(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked — Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "B"}]
              - op: test
                eq: [sales.box, {const: "H"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line2.g
    printed: "2(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked — Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "B"}]
              - op: test
                eq: [sales.box, {const: "H"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line2.h
    printed: "2(h)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "B"}]
              - op: test
                eq: [sales.box, {const: "H"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line3.d
    printed: "3(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked — Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "C"}]
              - op: test
                eq: [sales.box, {const: "I"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line3.e
    printed: "3(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked — Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "C"}]
              - op: test
                eq: [sales.box, {const: "I"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line3.g
    printed: "3(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked — Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "C"}]
              - op: test
                eq: [sales.box, {const: "I"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line3.h
    printed: "3(h)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "C"}]
              - op: test
                eq: [sales.box, {const: "I"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line8a.d
    printed: "8a(d)"
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments — Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "D"}]
              - op: test
                eq: [sales.box, {const: "J"}]
          - op: test
            eq: [sales.route, {const: "aggregate"}]
  - id: sd.line8a.e
    printed: "8a(e)"
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments — Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "D"}]
              - op: test
                eq: [sales.box, {const: "J"}]
          - op: test
            eq: [sales.route, {const: "aggregate"}]
  - id: sd.line8a.g
    printed: "8a(g)"
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments — Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "D"}]
              - op: test
                eq: [sales.box, {const: "J"}]
          - op: test
            eq: [sales.route, {const: "aggregate"}]
  - id: sd.line8a.h
    printed: "8a(h)"
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "D"}]
              - op: test
                eq: [sales.box, {const: "J"}]
          - op: test
            eq: [sales.route, {const: "aggregate"}]
  - id: sd.line8b.d
    printed: "8b(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked — Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "D"}]
              - op: test
                eq: [sales.box, {const: "J"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line8b.e
    printed: "8b(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked — Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "D"}]
              - op: test
                eq: [sales.box, {const: "J"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line8b.g
    printed: "8b(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked — Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "D"}]
              - op: test
                eq: [sales.box, {const: "J"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line8b.h
    printed: "8b(h)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "D"}]
              - op: test
                eq: [sales.box, {const: "J"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line9.d
    printed: "9(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked — Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "E"}]
              - op: test
                eq: [sales.box, {const: "K"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line9.e
    printed: "9(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked — Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "E"}]
              - op: test
                eq: [sales.box, {const: "K"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line9.g
    printed: "9(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked — Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "E"}]
              - op: test
                eq: [sales.box, {const: "K"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line9.h
    printed: "9(h)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "E"}]
              - op: test
                eq: [sales.box, {const: "K"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line10.d
    printed: "10(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked — Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "F"}]
              - op: test
                eq: [sales.box, {const: "L"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line10.e
    printed: "10(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked — Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "F"}]
              - op: test
                eq: [sales.box, {const: "L"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line10.g
    printed: "10(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked — Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "F"}]
              - op: test
                eq: [sales.box, {const: "L"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line10.h
    printed: "10(h)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.h
      where:
        op: test
        all:
          - op: test
            any:
              - op: test
                eq: [sales.box, {const: "F"}]
              - op: test
                eq: [sales.box, {const: "L"}]
          - op: test
            eq: [sales.route, {const: "detail"}]
  - id: sd.line4
    printed: "4"
    label: "Short-term gain from Form 6252 and short-term gain or (loss) from Forms 4684, 6781, and 8824"
    type: Dollars
    expr:
      op: subtract
      from: sd.zero
      take: sd.zero
    refuses: [sd.other_forms]
  - id: sd.line5
    printed: "5"
    label: "Net short-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1"
    type: Dollars
    expr:
      op: subtract
      from: sd.zero
      take: sd.zero
    refuses: [sd.other_forms]
  - id: sd.line6
    printed: "6"
    label: "Short-term capital loss carryover. Enter the amount, if any, from line 8 of your Capital Loss Carryover Worksheet in the instructions"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [sd.carryover, {const: true}]
          then: sd.h_st_carryover_neg
        - guard:
            op: test
            eq: [sd.carryover, {const: false}]
          then: sd.zero
    refuses: [clcw.spouse_screen]
  - id: sd.line11
    printed: "11"
    label: "Gain from Form 4797, Part I; long-term gain from Forms 2439 and 6252; and long-term gain or (loss) from Forms 4684, 6781, and 8824"
    type: Dollars
    expr:
      op: subtract
      from: sd.zero
      take: sd.zero
    refuses: [sd.other_forms]
  - id: sd.line12
    printed: "12"
    label: "Net long-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1"
    type: Dollars
    expr:
      op: subtract
      from: sd.zero
      take: sd.zero
    refuses: [sd.other_forms]
  - id: sd.line14
    printed: "14"
    label: "Long-term capital loss carryover. Enter the amount, if any, from line 13 of your Capital Loss Carryover Worksheet in the instructions"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [sd.carryover, {const: true}]
          then: sd.h_lt_carryover_neg
        - guard:
            op: test
            eq: [sd.carryover, {const: false}]
          then: sd.zero
    refuses: [clcw.spouse_screen]
  - id: sd.line13
    printed: "13"
    label: "Capital gain distributions. See the instructions"
    type: NonNegDollars
    expr:
      op: copy
      from: sd.distributions
  - id: sd.line7
    printed: "7"
    label: "Net short-term capital gain or (loss). Combine lines 1a through 6 in column (h)"
    type: Dollars
    expr:
      op: sum
      of: [sd.line1a.h, sd.line1b.h, sd.line2.h, sd.line3.h, sd.line4, sd.line5, sd.line6]
  - id: sd.line15
    printed: "15"
    label: "Net long-term capital gain or (loss). Combine lines 8a through 14 in column (h)"
    type: Dollars
    expr:
      op: sum
      of: [sd.line8a.h, sd.line8b.h, sd.line9.h, sd.line10.h, sd.line11, sd.line12, sd.line13, sd.line14]
  - id: sd.line16
    printed: "16"
    label: "Combine lines 7 and 15 and enter the result"
    type: Dollars
    expr:
      op: sum
      of: [sd.line7, sd.line15]
  - id: sd.line17
    printed: "17"
    label: "Are lines 15 and 16 both gains?"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          gt: [sd.line15, {const: 0}]
        - op: test
          gt: [sd.line16, {const: 0}]
  - id: sd.line20
    printed: "20"
    label: "Are lines 18 and 19 both zero or blank and you are not filing Form 4952?"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          eq: [sd.line18, {const: 0}]
        - op: test
          eq: [sd.line19, {const: 0}]
        - op: test
          eq: [sd.filing4952, {const: false}]
  - id: sd.line21
    printed: "21"
    label: "If line 16 is a loss, enter here and on Form 1040, 1040-SR, or 1040-NR, line 7a, the smaller of: the loss on line 16; or ($3,000), or if married filing separately, ($1,500)"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            lt: [sd.line16, {const: 0}]
          then: sd.h_line21_neg
        - guard:
            op: test
            ge: [sd.line16, {const: 0}]
          then: sd.zero
  - id: sd.line22
    printed: "22"
    label: "Do you have qualified dividends on Form 1040, 1040-SR, or 1040-NR, line 3a?"
    type: Bool
    expr:
      op: test
      gt: [f1040.line3a, {const: 0}]
  - id: sd.zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr:
      op: param
      ref: sales.zero
  - id: sd.h_st_carryover_neg
    printed: "(helper)"
    label: "Short-term capital loss carryover entered as a negative amount"
    type: Dollars
    expr:
      op: subtract
      from: sd.zero
      take: clcw.line8
  - id: sd.h_lt_carryover_neg
    printed: "(helper)"
    label: "Long-term capital loss carryover entered as a negative amount"
    type: Dollars
    expr:
      op: subtract
      from: sd.zero
      take: clcw.line13
  - id: sd.h_loss_abs
    printed: "(helper)"
    label: "Absolute amount of the Schedule D line 16 loss"
    type: Dollars
    expr:
      op: subtract
      from: sd.zero
      take: sd.line16
  - id: sd.h_limit_pos
    printed: "(helper)"
    label: "Positive amount of the capital loss limitation"
    type: Dollars
    expr:
      op: subtract
      from: sd.zero
      take: {param: sd.loss_limit}
  - id: sd.h_line21_abs
    printed: "(helper)"
    label: "Smaller of the line 16 loss and the capital loss limitation, as a positive amount"
    type: Dollars
    expr:
      op: smaller_of
      of: [sd.h_loss_abs, sd.h_limit_pos]
  - id: sd.h_line21_neg
    printed: "(helper)"
    label: "Allowed capital loss entered as a negative amount"
    type: Dollars
    expr:
      op: subtract
      from: sd.zero
      take: sd.h_line21_abs
  - id: sd.line18
    printed: "(helper)"
    label: "If required, amount from line 7 of the 28% Rate Gain Worksheet"
    type: NonNegDollars
    expr:
      op: copy
      from: sd.zero
    refuses: [sales.special, sd.other_forms]
    note: "No 28% Rate Gain Worksheet fields are supplied; this line is zero when no collectibles or other unsupported special gain is present, and refuses otherwise."
  - id: sd.line19
    printed: "(helper)"
    label: "Amount from line 18 of the Unrecaptured Section 1250 Gain Worksheet"
    type: NonNegDollars
    expr:
      op: copy
      from: u1250.line18
  - id: sd.filing4952
    printed: "(helper)"
    label: "Form 4952 is filed"
    type: Bool
    expr:
      op: copy
      from: f4952.required
  - id: sd.investment_election
    printed: "(helper)"
    label: "Amount from Form 4952, line 4g, qualified dividends and net capital gain elected into investment income"
    type: NonNegDollars
    expr:
      op: copy
      from: f4952.line4g
  - id: sd.filed
    printed: "(helper)"
    label: "Schedule D is filed"
    type: Bool
    expr:
      op: copy
      from: qdcg.schedule_d_filed
  - id: sd.has_loss
    printed: "(helper)"
    label: "Schedule D line 16 is a loss"
    type: Bool
    expr:
      op: test
      lt: [sd.line16, {const: 0}]
  - id: sd.to1040
    printed: "(helper)"
    label: "Amount from Schedule D to Form 1040, 1040-SR, or 1040-NR, line 7a"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            gt: [sd.line16, {const: 0}]
          then: sd.line16
        - guard:
            op: test
            lt: [sd.line16, {const: 0}]
          then: sd.line21
        - guard:
            op: test
            eq: [sd.line16, {const: 0}]
          then: sd.zero
  - id: sd.net_gain
    printed: "(helper)"
    label: "Net capital gain from Schedule D line 16"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: sd.line16
      take: sd.zero
```
