# Transcription agreement — sd

Second transcription of `Schedule D — securities sales and supplied distribution subtotals` by an isolated model (spec 6.5), compared line by line with `forms/2025/sd.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 10c58a98143cf5cf0a002683bb03cd8d6a8020f41255c0a79a6e357345bc7dbc |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | aa318bc97f4e8e87ef880bceedbcde14d392ea59a8140ccc2ab23f9a5c459393 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 14f6c7571f90fea7fd4da5231e18ae13294ab3b969700f9e50a613b3212a083f |
| printed lines compared | 55 |
| agree / disagree / missing | 16 / 39 / 0 |
| extra printed lines in second | 18, 19 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | eb461181b39879c79d1c0b7761ca0cd9ade46fdb1531cdee3281053c348f6c41 |
| i1040sd | 2025; printed date 2025-12-11 | 10, 11, 12, 15 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040gi | 2025; printed date 2026-02-25 | 31, 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### sd.line18 — Line 18. 28% Rate Gain Worksheet result, or zero when line 17 is No (lines 18 through 21 s
Status: **AGREE**

### sd.line19 — Line 19. Unrecaptured Section 1250 Gain Worksheet result, or zero when line 17 is No (line
Status: **AGREE**

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
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"ref": "f4952.line4c"}, {"ref": "f4952.line1"}], "test": "le"}, {"args": [{"const": 0}, {"ref": "f4952.line5"}], "test": "lt"}, {"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0}, {"ref": "f4952.line3"}], "test": "lt"}], "test": "all"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"ref": "f4952.line4g"}], "test": "lt"}, "then": {"ref": "f4952.line4g"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"args": [{"const": true}, {"input": "f4952.carryover"}], "test": "eq"}, {"args": [{"const": 0}, {"ref": "f4952.line1"}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "f4952.line4g"}], "test": "lt"}], "test": "any"}], "test": "all"}, "then": {"ref": "f4952.line4g"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "eq"}, {"args": [{"ref": "f4952.line5"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line1"}, {"ref": "f4952.line4c"}], "test": "lt"}], "test": "all"}, {"args": [{"ref": "f4952.line3"}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"alternatives": [{"guard": {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"ref": "f4952.line4g"}], "test": "lt"}, "then": {"ref": "f4952.line4g"}}], "op": "choose"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"args": [{"ref": "f4952.line1"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "f4952.carryover"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The Schedule D Tax Worksheet applies 'if you file Form 4952 and you have an amount on line 4g'. Read as the Form 4952 line 4g amount when Form 4952 is filed, zero otherwise.

Ruling: scope; i1040sd p. 15, Schedule D Tax Worksheet: complete it "if you file Form 4952 and you have an amount on line 4g", line 3: "Enter the amount from Form 4952 ..., line 4g". The candidate yields f4952.line4g when Form 4952 is filed or line 4g is positive and 0 otherwise; the project copies f4952.election, line 4g behind its cited gates, so both give line 4g whenever both compute. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,039 of 2,115 comparisons agree; 65 candidate-refuses, 9 project-refuses, 2 project-unknown (by return: {"incomplete": {"project-unknown": 2}, "refused": {"candidate-refuses": 65, "project-refuses": 9}}). No value differs. All 65 candidate-refuses are on returns the project refuses elsewhere (by return: refused): the candidate's filing test reads Form 4952 and Schedule B terms the project does not read at this line (f4952.unsupported 17, sb.line8 11, f4952.alternative_allocation 11, sb.unsupported 10, sb.fbar_required 9, sb.form8938 5, f4952.bad_dividends 2); the 9 project-refuses are cited gates (div.bad_components 6, div.unsupported 1, sales[s2].digital 1, sales[s1].digital 1); the 2 project-unknown withhold sales[s2].aggregate_eligible. Project stands.

### sd.filed — Schedule D required for entered sales, special distribution gains or a capital loss carryo
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sales", "field": "sales.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}], "test": "lt"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "lt"}, {"args": [{"line": "14"}, {"const": 0}], "test": "lt"}, {"args": [{"line": "6"}, {"const": 0}], "test": "lt"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"const": true}, {"input": "sd.carryover"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sd.other_forms"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "sales", "field": "sales.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "div.box2b"}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "div.box2c"}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "div.box2d"}], "test": "lt"}], "test": "any"}
```

Second transcription's note: Form 1040 line 7a Exception 1: Schedule D is not required if there are no capital losses and the only capital gains are capital gain distributions with no amount in Form 1099-DIV boxes 2b, 2c or 2d (and no QOF deferral, outside this tool). Read as filed exactly when that exception does not apply. A capital loss carryover is treated as a capital loss. Filing when not required is not modelled.

Ruling: model error; i1040gi p. 31, Line 7a, Exception 1: "1. You have no capital losses, and your only capital gains are capital gain distributions from Form(s) 1099-DIV, box 2a ... and 2. None of the Form(s) 1099-DIV ... have an amount in box 2b ..., box 2c ..., or box 2d"; i1040sd p. 10, Capital Loss Carryover Worksheet: "Use this worksheet to figure your capital loss carryovers from 2024 to 2025 if your 2024 Schedule D, line 21, is a loss and (a) ... or (b) ... Otherwise, you don’t have any carryovers." The candidate requires Schedule D whenever sd.carryover is answered Yes; the project requires it when line 6 or line 14 is a nonzero loss (with the sales count and lines 18 and 19). executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,027 of 2,115 comparisons agree; 43 project-refuses, 41 project-unknown, 4 value (by return: {"incomplete": {"project-unknown": 32, "value": 2}, "refused": {"project-refuses": 43, "project-unknown": 9, "value": 2}}). The 4 value differences, each project false and candidate true with sd.carryover Yes, no sales, lines 6, 14, 18 and 19 all $0: classm.f8863.3.deepseek (refused), classm.f8863.3 (refused), stage20.line21_at_both_bounds (incomplete), stage20.mut.line21_below_limit (incomplete); a Yes with worksheet lines 8 and 13 at $0 leaves no capital loss, so Exception 1 applies and the project is right. None is on a completed return. Project refusals: sd.other_forms 17, div.unsupported 10, div.bad_components 8, div.section1202 3, div.amt 3, div.bad_special 2; project-unknown: sd.distributions 32, sd.other_forms 7, clcw.prior_sd15 1, sd.carryover 1 (withheld screen answers): scope. Same expression and reading as Stage 20. Project stands.

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

Ruling: scope; f1040sd p. 2, line 16: "If line 16 is zero, skip lines 17 through 21 below and enter -0- on Form 1040, 1040-SR, or 1040-NR, line 7a". The candidate's extra zero branch equals line 16 when line 16 is zero; both enter line 16 for a gain and line 21 for a loss. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,043 of 2,115 comparisons agree; 71 project-refuses, 1 project-unknown (by return: {"refused": {"project-refuses": 71, "project-unknown": 1}}). No value differs. Project refusals are cited Schedule D and Form 1099-DIV gates (div.bad_components 18, sales[s1].digital 17, div.unsupported 11, sales[s2].digital 7, sales[a].digital 6, div.section1202 5, div.amt 4, div.bad_special 2, sales[s3].digital 1); the project-unknown withholds div.box2c. Same reading as Stage 20. Project stands.

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

Second transcription's note: Qualified Dividends and Capital Gain Tax Worksheet line 3 (Yes branch). When Schedule D is not required, lines 15 and 16 both equal the capital gain distributions, matching the No branch (Form 1040 line 7a).

Ruling: representation; i1040gi p. 38, Qualified Dividends and Capital Gain Tax Worksheet, line 3: "Enter the smaller of line 15 or line 16 of Schedule D. If either line 15 or line 16 is blank or a loss, enter -0-". The candidate's min(max(line 15, 0), max(line 16, 0)) equals the project's max(min(line 15, line 16), 0) for all values. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,043 of 2,115 comparisons agree; 71 project-refuses, 1 project-unknown (by return: {"refused": {"project-refuses": 71, "project-unknown": 1}}). No value differs; the differences are cited gates (div.bad_components 18, sales[s1].digital 17, div.unsupported 11, sales[s2].digital 7, sales[a].digital 6, div.section1202 5, div.amt 4, div.bad_special 2, sales[s3].digital 1) and one withheld div.box2c. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1a, column (d). The candidate adds the digital-asset boxes (G–L) to box A on the aggregate route without the Schedule D screen; the project sums box A behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1a, column (e). The candidate adds the digital-asset boxes (G–L) to box A on the aggregate route without the Schedule D screen; the project sums box A behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

### 1a(g) — Line 1a, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"const": 0}
```

Second transcription's note: The instructions for line 1a admit only transactions needing no adjustments and compute column (h) as (d) minus (e) (Example 1). Column (g) is therefore held at zero.

Ruling: scope; f1040sd p. 1, line 1a, column (g). The candidate adds the digital-asset boxes (G–L) to box A on the aggregate route without the Schedule D screen; the project sums box A behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,960 of 2,115 comparisons agree; 84 project-unknown, 71 project-refuses (by return: {"incomplete": {"project-unknown": 63}, "refused": {"project-refuses": 71, "project-unknown": 21}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 80, sales[s1].special 2, sales[s2].aggregate_eligible 2 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. The constant column (g) of the aggregate line equals the project's zero because adjustments are not allowed on the aggregate route: the printed line is for transactions "for which you have no adjustments" (f1040sd p. 1, line 1a), and sales.bad_aggregate and sales.bad_code refuse any aggregate entry that would carry one; those refusals and the withheld answers this line reads (sd.other_forms, sales[*].special, sales[*].aggregate_eligible) are its extra 21 refusals and 44 unknowns. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

### 1a(h) — Line 1a, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"from": {"line": "1a(d)"}, "op": "subtract", "take": {"line": "1a(e)"}}
```

Ruling: scope; f1040sd p. 1, line 1a, column (h). The candidate adds the digital-asset boxes (G–L) to box A on the aggregate route without the Schedule D screen; the project sums box A behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1b, column (d). The candidate adds the digital-asset boxes (G–L) to box A on the detail route without the Schedule D screen; the project sums box A behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1b, column (e). The candidate adds the digital-asset boxes (G–L) to box A on the detail route without the Schedule D screen; the project sums box A behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1b, column (g). The candidate adds the digital-asset boxes (G–L) to box A on the detail route without the Schedule D screen; the project sums box A behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

### 1b(h) — Line 1b, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"of": [{"line": "1b(g)"}, {"from": {"line": "1b(d)"}, "op": "subtract", "take": {"line": "1b(e)"}}], "op": "sum"}
```

Ruling: scope; f1040sd p. 1, line 1b, column (h). The candidate adds the digital-asset boxes (G–L) to box A on the detail route without the Schedule D screen; the project sums box A behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 2, column (d). The candidate adds the digital-asset boxes (G–L) to box B on the detail route without the Schedule D screen; the project sums box B behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 2, column (e). The candidate adds the digital-asset boxes (G–L) to box B on the detail route without the Schedule D screen; the project sums box B behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 2, column (g). The candidate adds the digital-asset boxes (G–L) to box B on the detail route without the Schedule D screen; the project sums box B behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,026 of 2,115 comparisons agree; 49 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 49, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 1; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

### 2(h) — Line 2, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"of": [{"line": "2(g)"}, {"from": {"line": "2(d)"}, "op": "subtract", "take": {"line": "2(e)"}}], "op": "sum"}
```

Ruling: scope; f1040sd p. 1, line 2, column (h). The candidate adds the digital-asset boxes (G–L) to box B on the detail route without the Schedule D screen; the project sums box B behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,026 of 2,115 comparisons agree; 49 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 49, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 1; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 3, column (d). The candidate adds the digital-asset boxes (G–L) to box C on the detail route without the Schedule D screen; the project sums box C behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 3, column (e). The candidate adds the digital-asset boxes (G–L) to box C on the detail route without the Schedule D screen; the project sums box C behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 3, column (g). The candidate adds the digital-asset boxes (G–L) to box C on the detail route without the Schedule D screen; the project sums box C behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

### 3(h) — Line 3, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"of": [{"line": "3(g)"}, {"from": {"line": "3(d)"}, "op": "subtract", "take": {"line": "3(e)"}}], "op": "sum"}
```

Ruling: scope; f1040sd p. 1, line 3, column (h). The candidate adds the digital-asset boxes (G–L) to box C on the detail route without the Schedule D screen; the project sums box C behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8a, column (d). The candidate adds the digital-asset boxes (G–L) to box D on the aggregate route without the Schedule D screen; the project sums box D behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8a, column (e). The candidate adds the digital-asset boxes (G–L) to box D on the aggregate route without the Schedule D screen; the project sums box D behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

### 8a(g) — Line 8a, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"const": 0}
```

Second transcription's note: The instructions for line 8a admit only transactions needing no adjustments and compute column (h) as (d) minus (e) (Example 1). Column (g) is therefore held at zero.

Ruling: scope; f1040sd p. 1, line 8a, column (g). The candidate adds the digital-asset boxes (G–L) to box D on the aggregate route without the Schedule D screen; the project sums box D behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,960 of 2,115 comparisons agree; 84 project-unknown, 71 project-refuses (by return: {"incomplete": {"project-unknown": 63}, "refused": {"project-refuses": 71, "project-unknown": 21}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s1].bad_aggregate 6, sales[s1].bad_code 4, sales[a].bad_aggregate 3, sales[a].bad_code 2, sales[s3].digital 2, sales[a].special 1, sales[s2].bad_aggregate 1, sales[s3].bad_code 1, sales[s3].bad_aggregate 1, sales[s2].bad_code 1, sales[s1].special 1; project-unknown: sd.other_forms 80, sales[s1].special 2, sales[s2].aggregate_eligible 2 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. The constant column (g) of the aggregate line equals the project's zero because adjustments are not allowed on the aggregate route: the printed line is for transactions "for which you have no adjustments" (f1040sd p. 1, line 8a), and sales.bad_aggregate and sales.bad_code refuse any aggregate entry that would carry one; those refusals and the withheld answers this line reads (sd.other_forms, sales[*].special, sales[*].aggregate_eligible) are its extra 21 refusals and 44 unknowns. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

### 8a(h) — Line 8a, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"from": {"line": "8a(d)"}, "op": "subtract", "take": {"line": "8a(e)"}}
```

Ruling: scope; f1040sd p. 1, line 8a, column (h). The candidate adds the digital-asset boxes (G–L) to box D on the aggregate route without the Schedule D screen; the project sums box D behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8b, column (d). The candidate adds the digital-asset boxes (G–L) to box D on the detail route without the Schedule D screen; the project sums box D behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8b, column (e). The candidate adds the digital-asset boxes (G–L) to box D on the detail route without the Schedule D screen; the project sums box D behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8b, column (g). The candidate adds the digital-asset boxes (G–L) to box D on the detail route without the Schedule D screen; the project sums box D behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

### 8b(h) — Line 8b, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"of": [{"line": "8b(g)"}, {"from": {"line": "8b(d)"}, "op": "subtract", "take": {"line": "8b(e)"}}], "op": "sum"}
```

Ruling: scope; f1040sd p. 1, line 8b, column (h). The candidate adds the digital-asset boxes (G–L) to box D on the detail route without the Schedule D screen; the project sums box D behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 9, column (d). The candidate adds the digital-asset boxes (G–L) to box E on the detail route without the Schedule D screen; the project sums box E behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 9, column (e). The candidate adds the digital-asset boxes (G–L) to box E on the detail route without the Schedule D screen; the project sums box E behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 9, column (g). The candidate adds the digital-asset boxes (G–L) to box E on the detail route without the Schedule D screen; the project sums box E behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

### 9(h) — Line 9, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"of": [{"line": "9(g)"}, {"from": {"line": "9(d)"}, "op": "subtract", "take": {"line": "9(e)"}}], "op": "sum"}
```

Ruling: scope; f1040sd p. 1, line 9, column (h). The candidate adds the digital-asset boxes (G–L) to box E on the detail route without the Schedule D screen; the project sums box E behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 10, column (d). The candidate adds the digital-asset boxes (G–L) to box F on the detail route without the Schedule D screen; the project sums box F behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 10, column (e). The candidate adds the digital-asset boxes (G–L) to box F on the detail route without the Schedule D screen; the project sums box F behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

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

Ruling: scope; f1040sd p. 1, line 10, column (g). The candidate adds the digital-asset boxes (G–L) to box F on the detail route without the Schedule D screen; the project sums box F behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

### 10(h) — Line 10, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"of": [{"line": "10(g)"}, {"from": {"line": "10(d)"}, "op": "subtract", "take": {"line": "10(e)"}}], "op": "sum"}
```

Ruling: scope; f1040sd p. 1, line 10, column (h). The candidate adds the digital-asset boxes (G–L) to box F on the detail route without the Schedule D screen; the project sums box F behind sd.screen (sd.count through sales.one), which refuses digital-asset sales (sales.digital, f8949 Parts I and II, boxes G–L; widening is T-003), special sales, unsupported codes and invalid aggregate use, and sd.other_forms. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,025 of 2,115 comparisons agree; 50 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 50, "project-unknown": 9}}). Project refusals: sd.other_forms 18, sales[s1].digital 17, sales[s2].digital 7, sales[a].digital 6, sales[s3].digital 2; project-unknown: sd.other_forms 40 (partial records withholding the screen the interview asks before any total). No value differs, so no completed return differs; no refusal is the new sales.wash_bad gate. Same expression and the same reading as Stage 20 (scope). Scratch uncapped re-run (/tmp/adj-bklg-income/full/) gives the same counts. Project stands.

### 4 — Line 4: zero only after unsupported source/carryover screening
Status: **AGREE**

### 5 — Line 5: zero only after unsupported source/carryover screening
Status: **AGREE**

### 6 — Short-term capital loss carryover, from line 8 of the Capital Loss Carryover Worksheet (a
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sd.carryover"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sd.carryover"}], "test": "eq"}, "then": {"from": {"const": 0}, "op": "subtract", "take": {"ref": "clcw.line8"}}}], "op": "choose"}
```

Second:

```json
{"from": {"const": 0}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sd.carryover"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sd.carryover"}], "test": "eq"}, "then": {"ref": "clcw.line8"}}], "op": "choose"}}
```

Ruling: scope; f1040sd p. 1, line 6: "Short-term capital loss carryover. Enter the amount, if any, from line 8 of your Capital Loss Carryover Worksheet in the instructions", printed "( )"; line 7: "Combine lines 1a through 6 in column (h)". With the T-140 interface note ("a loss carryover printed in parentheses, held as a negative amount", now in the prompt) the candidate holds the carryover negative, 0 − choose(sd.carryover: clcw.line8, else 0), which is algebraically the project's choose(sd.carryover: 0 − clcw.line8, else 0). executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,057 of 2,115 comparisons agree; 40 project-unknown, 18 project-refuses (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 18, "project-unknown": 9}}). No value differs: the 26 sign-flip value differences of Stage 20 (classm.sd.2 −$16,565.00 against $16,565.00) are gone. The project refuses on sd.other_forms (18) and is unknown on partial records withholding sd.other_forms (40), a cited Schedule D screen the interview asks first; the candidate declares no refusal. Project stands.

### 11 — Line 11: zero only after unsupported source/carryover screening
Status: **AGREE**

### 12 — Line 12: zero only after unsupported source/carryover screening
Status: **AGREE**

### 14 — Long-term capital loss carryover, from line 13 of the Capital Loss Carryover Worksheet (a
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sd.carryover"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sd.carryover"}], "test": "eq"}, "then": {"from": {"const": 0}, "op": "subtract", "take": {"ref": "clcw.line13"}}}], "op": "choose"}
```

Second:

```json
{"from": {"const": 0}, "op": "subtract", "take": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sd.carryover"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sd.carryover"}], "test": "eq"}, "then": {"ref": "clcw.line13"}}], "op": "choose"}}
```

Ruling: scope; f1040sd p. 1, line 14: "Long-term capital loss carryover. Enter the amount, if any, from line 13 of your Capital Loss Carryover Worksheet in the instructions", printed "( )"; line 15: "Combine lines 8a through 14 in column (h)". With the T-140 interface note ("a loss carryover printed in parentheses, held as a negative amount", now in the prompt) the candidate holds the carryover negative, 0 − choose(sd.carryover: clcw.line13, else 0), which is algebraically the project's choose(sd.carryover: 0 − clcw.line13, else 0). executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,057 of 2,115 comparisons agree; 40 project-unknown, 18 project-refuses (by return: {"incomplete": {"project-unknown": 31}, "refused": {"project-refuses": 18, "project-unknown": 9}}). No value differs: the 22 sign-flip value differences of Stage 20 (classm.sd.2 −$17,835.00 against $17,835.00) are gone. The project refuses on sd.other_forms (18) and is unknown on partial records withholding sd.other_forms (40), a cited Schedule D screen the interview asks first; the candidate declares no refusal. Project stands.

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
{"args": [{"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "eq"}, {"args": [{"ref": "f4952.line5"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line1"}, {"ref": "f4952.line4c"}], "test": "lt"}], "test": "all"}, {"args": [{"ref": "f4952.line3"}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"alternatives": [{"guard": {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"ref": "f4952.line4g"}], "test": "lt"}, "then": {"ref": "f4952.line4g"}}], "op": "choose"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"args": [{"ref": "f4952.line1"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "f4952.carryover"}], "test": "ne"}], "test": "all"}], "test": "any"}, {"args": [{"line": "18"}, {"const": 0}], "test": "le"}, {"args": [{"line": "19"}, {"const": 0}], "test": "le"}], "test": "all"}
```

Ruling: scope; f1040sd p. 2, line 20: "Are lines 18 and 19 both zero or blank and you are not filing Form 4952?". The candidate's predicate is the project's with lines 18 and 19 read as its own lines 18 and 19 (which now agree with the project's: the candidate takes g28.line7 and u1250.line18 behind line 17), so it is the same test. executable-triage-v2 (`reviews/2025/transcription/triage/sd.json`; 1,495 fixtures, 500 generated returns seed 20261026, 120 partial records): 2,070 of 2,115 comparisons agree; 44 project-refuses, 1 project-unknown (by return: {"refused": {"project-refuses": 44, "project-unknown": 1}}). No value differs: the 4 Stage 20 value differences (classm.sd.2, stage20.blind.r7, generated 235), caused by the candidate's positive line 14 entering g28.line5, are gone after the T-140 sign note. Project refusals are cited gates read through g28/u1250 and Form 4952 (sales[s1].digital 16, div.bad_components 9, sales[a].digital 6, sales[s2].digital 4, div.amt 3, div.section1202 2, div.unsupported 2, div.bad_special 1, sales[s3].digital 1); the project-unknown withholds div.box2c. Project stands.

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **AGREE**

### 22 — Do you have qualified dividends?
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sd.line18 | sd.h_bad, sd.other_forms | sd.h_bad |
| sd.line19 | sd.h_bad, sd.other_forms | sd.h_bad |
| sd.has_loss | sd.h_bad, sd.other_forms | sd.h_bad |
| sd.to1040 | sd.h_bad, sd.other_forms | sd.h_bad |
| sd.net_gain | sd.h_bad, sd.other_forms | sd.h_bad |
| 1a(d) | sd.h_bad | sd.h_bad |
| 1a(e) | sd.h_bad | sd.h_bad |
| 1a(h) | sd.h_bad | sd.h_bad |
| 1b(d) | sd.h_bad | sd.h_bad |
| 1b(e) | sd.h_bad | sd.h_bad |
| 1b(g) | sd.h_bad | sd.h_bad |
| 1b(h) | sd.h_bad | sd.h_bad |
| 2(d) | sd.h_bad | sd.h_bad |
| 2(e) | sd.h_bad | sd.h_bad |
| 2(g) | sd.h_bad | sd.h_bad |
| 2(h) | sd.h_bad | sd.h_bad |
| 3(d) | sd.h_bad | sd.h_bad |
| 3(e) | sd.h_bad | sd.h_bad |
| 3(g) | sd.h_bad | sd.h_bad |
| 3(h) | sd.h_bad | sd.h_bad |
| 8a(d) | sd.h_bad | sd.h_bad |
| 8a(e) | sd.h_bad | sd.h_bad |
| 8a(h) | sd.h_bad | sd.h_bad |
| 8b(d) | sd.h_bad | sd.h_bad |
| 8b(e) | sd.h_bad | sd.h_bad |
| 8b(g) | sd.h_bad | sd.h_bad |
| 8b(h) | sd.h_bad | sd.h_bad |
| 9(d) | sd.h_bad | sd.h_bad |
| 9(e) | sd.h_bad | sd.h_bad |
| 9(g) | sd.h_bad | sd.h_bad |
| 9(h) | sd.h_bad | sd.h_bad |
| 10(d) | sd.h_bad | sd.h_bad |
| 10(e) | sd.h_bad | sd.h_bad |
| 10(g) | sd.h_bad | sd.h_bad |
| 10(h) | sd.h_bad | sd.h_bad |
| 4 | sd.other_forms | - |
| 5 | sd.other_forms | - |
| 11 | sd.other_forms | - |
| 12 | sd.other_forms | - |
| 7 | sd.h_bad, sd.other_forms | sd.h_bad |
| 15 | sd.h_bad, sd.other_forms | sd.h_bad |
| 16 | sd.h_bad, sd.other_forms | sd.h_bad |
| 17 | sd.h_bad, sd.other_forms | sd.h_bad |
| 20 | sd.h_bad, sd.other_forms | sd.h_bad |
| 21 | sd.h_bad, sd.other_forms | sd.h_bad |

## Raw second transcription

```yaml
```yaml
lines:
  - id: sd.zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: sd.h_bad_count
    printed: "(helper)"
    label: "Number of sales entries this tool cannot report: collectibles, section 1202 or section 1250 property, unsupported adjustment codes, or aggregate entries that do not qualify for line 1a or 8a"
    type: Count
    expr:
      op: sum_over
      collection: sales
      field: sales.one
      where:
        op: test
        any:
          - {op: test, eq: [sales.special, {const: true}]}
          - {op: test, eq: [sales.bad_code, {const: true}]}
          - {op: test, eq: [sales.bad_aggregate, {const: true}]}

  - id: sd.h_bad
    printed: "(gate)"
    label: "Some sale cannot be reported by this tool"
    type: Bool
    expr: {op: test, gt: [sd.h_bad_count, {const: 0, type: Count}]}

  # ---------------- Part I ----------------
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
          - {op: test, eq: [sales.route, {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "A"}]}
              - {op: test, eq: [sales.box, {const: "G"}]}
    refuses: [sd.h_bad]

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
          - {op: test, eq: [sales.route, {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "A"}]}
              - {op: test, eq: [sales.box, {const: "G"}]}
    refuses: [sd.h_bad]

  - id: sd.line1a.g
    printed: "1a(g)"
    label: "Line 1a — Adjustments to gain or loss"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    display: "Line 1a covers only transactions with no adjustments; column (g) is zero and line 1a(h) is (d) minus (e)."
    note: "The instructions for line 1a admit only transactions needing no adjustments and compute column (h) as (d) minus (e) (Example 1). Column (g) is therefore held at zero."

  - id: sd.line1a.h
    printed: "1a(h)"
    label: "Line 1a — Gain or (loss). Subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line1a.d, take: sd.line1a.e}
    refuses: [sd.h_bad]

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
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "A"}]}
              - {op: test, eq: [sales.box, {const: "G"}]}
    refuses: [sd.h_bad]

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
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "A"}]}
              - {op: test, eq: [sales.box, {const: "G"}]}
    refuses: [sd.h_bad]

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
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "A"}]}
              - {op: test, eq: [sales.box, {const: "G"}]}
    refuses: [sd.h_bad]

  - id: sd.h_1b_de
    printed: "(helper)"
    label: "Line 1b: subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line1b.d, take: sd.line1b.e}

  - id: sd.line1b.h
    printed: "1b(h)"
    label: "Line 1b — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_1b_de, sd.line1b.g]}
    refuses: [sd.h_bad]

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
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "B"}]}
              - {op: test, eq: [sales.box, {const: "H"}]}
    refuses: [sd.h_bad]

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
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "B"}]}
              - {op: test, eq: [sales.box, {const: "H"}]}
    refuses: [sd.h_bad]

  - id: sd.line2.g
    printed: "2(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked — Adjustments to gain or loss"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "B"}]}
              - {op: test, eq: [sales.box, {const: "H"}]}
    refuses: [sd.h_bad]

  - id: sd.h_2_de
    printed: "(helper)"
    label: "Line 2: subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line2.d, take: sd.line2.e}

  - id: sd.line2.h
    printed: "2(h)"
    label: "Line 2 — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_2_de, sd.line2.g]}
    refuses: [sd.h_bad]

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
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "C"}]}
              - {op: test, eq: [sales.box, {const: "I"}]}
    refuses: [sd.h_bad]

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
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "C"}]}
              - {op: test, eq: [sales.box, {const: "I"}]}
    refuses: [sd.h_bad]

  - id: sd.line3.g
    printed: "3(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked — Adjustments to gain or loss"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "C"}]}
              - {op: test, eq: [sales.box, {const: "I"}]}
    refuses: [sd.h_bad]

  - id: sd.h_3_de
    printed: "(helper)"
    label: "Line 3: subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line3.d, take: sd.line3.e}

  - id: sd.line3.h
    printed: "3(h)"
    label: "Line 3 — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_3_de, sd.line3.g]}
    refuses: [sd.h_bad]

  # ---------------- Part II sales ----------------
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
          - {op: test, eq: [sales.route, {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "D"}]}
              - {op: test, eq: [sales.box, {const: "J"}]}
    refuses: [sd.h_bad]

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
          - {op: test, eq: [sales.route, {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "D"}]}
              - {op: test, eq: [sales.box, {const: "J"}]}
    refuses: [sd.h_bad]

  - id: sd.line8a.g
    printed: "8a(g)"
    label: "Line 8a — Adjustments to gain or loss"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    display: "Line 8a covers only transactions with no adjustments; column (g) is zero and line 8a(h) is (d) minus (e)."
    note: "The instructions for line 8a admit only transactions needing no adjustments and compute column (h) as (d) minus (e) (Example 1). Column (g) is therefore held at zero."

  - id: sd.line8a.h
    printed: "8a(h)"
    label: "Line 8a — Gain or (loss). Subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line8a.d, take: sd.line8a.e}
    refuses: [sd.h_bad]

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
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "D"}]}
              - {op: test, eq: [sales.box, {const: "J"}]}
    refuses: [sd.h_bad]

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
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "D"}]}
              - {op: test, eq: [sales.box, {const: "J"}]}
    refuses: [sd.h_bad]

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
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "D"}]}
              - {op: test, eq: [sales.box, {const: "J"}]}
    refuses: [sd.h_bad]

  - id: sd.h_8b_de
    printed: "(helper)"
    label: "Line 8b: subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line8b.d, take: sd.line8b.e}

  - id: sd.line8b.h
    printed: "8b(h)"
    label: "Line 8b — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_8b_de, sd.line8b.g]}
    refuses: [sd.h_bad]

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
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "E"}]}
              - {op: test, eq: [sales.box, {const: "K"}]}
    refuses: [sd.h_bad]

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
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "E"}]}
              - {op: test, eq: [sales.box, {const: "K"}]}
    refuses: [sd.h_bad]

  - id: sd.line9.g
    printed: "9(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked — Adjustments to gain or loss"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "E"}]}
              - {op: test, eq: [sales.box, {const: "K"}]}
    refuses: [sd.h_bad]

  - id: sd.h_9_de
    printed: "(helper)"
    label: "Line 9: subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line9.d, take: sd.line9.e}

  - id: sd.line9.h
    printed: "9(h)"
    label: "Line 9 — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_9_de, sd.line9.g]}
    refuses: [sd.h_bad]

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
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "F"}]}
              - {op: test, eq: [sales.box, {const: "L"}]}
    refuses: [sd.h_bad]

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
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "F"}]}
              - {op: test, eq: [sales.box, {const: "L"}]}
    refuses: [sd.h_bad]

  - id: sd.line10.g
    printed: "10(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked — Adjustments to gain or loss"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "detail"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "F"}]}
              - {op: test, eq: [sales.box, {const: "L"}]}
    refuses: [sd.h_bad]

  - id: sd.h_10_de
    printed: "(helper)"
    label: "Line 10: subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line10.d, take: sd.line10.e}

  - id: sd.line10.h
    printed: "10(h)"
    label: "Line 10 — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_10_de, sd.line10.g]}
    refuses: [sd.h_bad]

  # ---------------- Other Part I / Part II lines ----------------
  - id: sd.line4
    printed: "4"
    label: "Short-term gain from Form 6252 and short-term gain or (loss) from Forms 4684, 6781, and 8824"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    refuses: [sd.other_forms]
    note: "Forms 6252, 4684, 6781 and 8824 are outside this tool; when sd.other_forms is yes the line refuses, otherwise it is zero."

  - id: sd.line5
    printed: "5"
    label: "Net short-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    refuses: [sd.other_forms]

  - id: sd.h_st_carry
    printed: "(helper)"
    label: "Short-term capital loss carryover for 2025 (Capital Loss Carryover Worksheet, line 8), as a positive amount"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sd.carryover, {const: true}]}
          then: clcw.line8
        - guard: {op: test, eq: [sd.carryover, {const: false}]}
          then: sd.zero

  - id: sd.line6
    printed: "6"
    label: "Short-term capital loss carryover. Enter the amount, if any, from line 8 of your Capital Loss Carryover Worksheet in the instructions"
    type: Dollars
    expr: {op: subtract, from: sd.zero, take: sd.h_st_carry}

  - id: sd.line11
    printed: "11"
    label: "Gain from Form 4797, Part I; long-term gain from Forms 2439 and 6252; and long-term gain or (loss) from Forms 4684, 6781, and 8824"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    refuses: [sd.other_forms]

  - id: sd.line12
    printed: "12"
    label: "Net long-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    refuses: [sd.other_forms]

  - id: sd.h_lt_carry
    printed: "(helper)"
    label: "Long-term capital loss carryover for 2025 (Capital Loss Carryover Worksheet, line 13), as a positive amount"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sd.carryover, {const: true}]}
          then: clcw.line13
        - guard: {op: test, eq: [sd.carryover, {const: false}]}
          then: sd.zero

  - id: sd.line14
    printed: "14"
    label: "Long-term capital loss carryover. Enter the amount, if any, from line 13 of your Capital Loss Carryover Worksheet in the instructions"
    type: Dollars
    expr: {op: subtract, from: sd.zero, take: sd.h_lt_carry}

  - id: sd.line13
    printed: "13"
    label: "Capital gain distributions"
    type: NonNegDollars
    expr: {op: copy, from: sd.distributions}

  - id: sd.line7
    printed: "7"
    label: "Net short-term capital gain or (loss). Combine lines 1a through 6 in column (h)"
    type: Dollars
    expr: {op: sum, of: [sd.line1a.h, sd.line1b.h, sd.line2.h, sd.line3.h, sd.line4, sd.line5, sd.line6]}

  - id: sd.line15
    printed: "15"
    label: "Net long-term capital gain or (loss). Combine lines 8a through 14 in column (h)"
    type: Dollars
    expr: {op: sum, of: [sd.line8a.h, sd.line8b.h, sd.line9.h, sd.line10.h, sd.line11, sd.line12, sd.line13, sd.line14]}

  # ---------------- Part III ----------------
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

  - id: sd.line18
    printed: "18"
    label: "If you are required to complete the 28% Rate Gain Worksheet, enter the amount, if any, from line 7 of that worksheet"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sd.line17, {const: true}]}
          then: g28.line7
        - guard: {op: test, eq: [sd.line17, {const: false}]}
          then: sd.zero
    note: "Line 18 is completed only when line 17 is Yes. Whether the worksheet is required (and otherwise zero) is left to the 28% Rate Gain Worksheet's own line 7; this line takes that amount when line 17 is Yes and zero (blank) otherwise."

  - id: sd.line19
    printed: "19"
    label: "If you are required to complete the Unrecaptured Section 1250 Gain Worksheet, enter the amount, if any, from line 18 of that worksheet"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sd.line17, {const: true}]}
          then: u1250.line18
        - guard: {op: test, eq: [sd.line17, {const: false}]}
          then: sd.zero
    note: "Line 19 is completed only when line 17 is Yes; the worksheet's line 18 is taken then, zero (blank) otherwise."

  - id: sd.filing4952
    printed: "(helper)"
    label: "Are you filing Form 4952?"
    type: Bool
    expr: {op: copy, from: f4952.required}
    note: "Line 20 asks whether you are 'not filing Form 4952'. Read as whether Form 4952 is filed, taken from the Form 4952 filing determination (f4952.required)."

  - id: sd.investment_election
    printed: "(helper)"
    label: "Amount from Form 4952, line 4g (qualified dividends and net capital gain elected into investment income)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sd.filing4952, {const: true}]}
          then: f4952.line4g
        - guard: {op: test, eq: [sd.filing4952, {const: false}]}
          then: sd.zero
    note: "The Schedule D Tax Worksheet applies 'if you file Form 4952 and you have an amount on line 4g'. Read as the Form 4952 line 4g amount when Form 4952 is filed, zero otherwise."

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

  - id: sd.h_loss_limit
    printed: "(helper)"
    label: "($3,000), or if married filing separately, ($1,500)"
    type: Dollars
    expr: {op: param, ref: sd.loss_limit}

  - id: sd.h_21_loss
    printed: "(helper)"
    label: "The smaller loss of line 16 or the limit (treating both as positive numbers)"
    type: Dollars
    expr: {op: larger_of, of: [sd.line16, sd.h_loss_limit]}

  - id: sd.line21
    printed: "21"
    label: "If line 16 is a loss, enter here and on Form 1040, 1040-SR, or 1040-NR, line 7a, the smaller of: the loss on line 16; or ($3,000), or if married filing separately, ($1,500)"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, lt: [sd.line16, {const: 0}]}
          then: sd.h_21_loss
        - guard: {op: test, ge: [sd.line16, {const: 0}]}
          then: sd.zero

  - id: sd.line22
    printed: "22"
    label: "Do you have qualified dividends on Form 1040, 1040-SR, or 1040-NR, line 3a?"
    type: Bool
    expr: {op: test, gt: [f1040.line3a, {const: 0}]}

  # ---------------- Result interfaces ----------------
  - id: sd.has_loss
    printed: "(helper)"
    label: "Line 16 is a loss"
    type: Bool
    expr: {op: test, lt: [sd.line16, {const: 0}]}

  - id: sd.to1040
    printed: "(helper)"
    label: "Amount for Form 1040, line 7a: line 16 if a gain; line 21 if line 16 is a loss; -0- if line 16 is zero"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, gt: [sd.line16, {const: 0}]}
          then: sd.line16
        - guard: {op: test, lt: [sd.line16, {const: 0}]}
          then: sd.line21
        - guard: {op: test, eq: [sd.line16, {const: 0}]}
          then: sd.zero

  - id: sd.h_15_pos
    printed: "(helper)"
    label: "Line 15, or -0- if blank or a loss"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sd.line15, take: sd.zero}

  - id: sd.h_16_pos
    printed: "(helper)"
    label: "Line 16, or -0- if blank or a loss"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sd.line16, take: sd.zero}

  - id: sd.net_gain
    printed: "(helper)"
    label: "The smaller of line 15 or line 16 of Schedule D; if either line 15 or line 16 is blank or a loss, -0-"
    type: NonNegDollars
    expr: {op: smaller_of, of: [sd.h_15_pos, sd.h_16_pos]}
    note: "Qualified Dividends and Capital Gain Tax Worksheet line 3 (Yes branch). When Schedule D is not required, lines 15 and 16 both equal the capital gain distributions, matching the No branch (Form 1040 line 7a)."

  - id: sd.h_sales_count
    printed: "(helper)"
    label: "Number of sales entered"
    type: Count
    expr: {op: sum_over, collection: sales, field: sales.one}

  - id: sd.filed
    printed: "(helper)"
    label: "Must you file Schedule D?"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [sd.h_sales_count, {const: 0, type: Count}]}
        - {op: test, eq: [sd.other_forms, {const: true}]}
        - {op: test, eq: [sd.carryover, {const: true}]}
        - {op: test, gt: [div.box2b, {const: 0}]}
        - {op: test, gt: [div.box2c, {const: 0}]}
        - {op: test, gt: [div.box2d, {const: 0}]}
    note: "Form 1040 line 7a Exception 1: Schedule D is not required if there are no capital losses and the only capital gains are capital gain distributions with no amount in Form 1099-DIV boxes 2b, 2c or 2d (and no QOF deferral, outside this tool). Read as filed exactly when that exception does not apply. A capital loss carryover is treated as a capital loss. Filing when not required is not modelled."
```
```
