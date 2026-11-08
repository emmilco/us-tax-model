# Transcription agreement — sd

Second transcription of `Schedule D — securities sales and supplied distribution subtotals` by an isolated model (spec 6.5), compared line by line with `forms/2025/sd.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 1 (latest 2026-11-07); see Line-scoped reviews |
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
| printed lines compared | 56 |
| agree / disagree / missing | 16 / 40 / 0 |
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

### sd.distributions_if_dividends — Capital gain distributions, generally Form 1099-DIV box 2a, when you or your spouse receiv
Status: **AGREE**
Reviewed in: pass 17f7a05c3e95

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
Reviewed in: pass 17f7a05c3e95

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
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "div.any"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "div.any"}], "test": "eq"}, "then": {"input": "sb.ordinary_dividends"}}], "op": "choose"}, {"const": 0}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"ref": "div.any"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"ref": "div.any"}], "test": "eq"}, "then": {"input": "sb.ordinary_dividends"}}], "op": "choose"}], "test": "lt"}, "then": {"ref": "f1040.line3a"}}], "op": "choose"}], "test": "lt"}
```

Second:

```json
{"args": [{"const": 0}, {"ref": "f1040.line3a"}], "test": "lt"}
```

Ruling: model error; the candidate reads f1040.line3a whatever box 1a is above zero, so it needs that answer where the source does not: i1040gi p. 25, Line 3a, "Qualified dividends are also included in the ordinary dividend total required to be shown on line 3b": with box 1a (line 3b) zero, line 3a is zero. The project reads the gate line f1040.line3a_if_ordinary, which takes f1040.line3a when box 1a is above zero holds and zero otherwise; the interview asks f1040.line3a only then (gated_by f1040.line3a_if_ordinary), so on every return the interview can produce with the condition true the two sides agree. Ruled by reading: the scoped reply names interfaces the candidate bank does not resolve, as in the earlier line-scoped passes of this lane.
Reviewed in: pass 17f7a05c3e95

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

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| sd.line18 | 2bbae14fd67622e88c468eacec973d73b3b9ed389fb0401a7e07aded80c90926 |
| sd.line19 | b653bf85615a8a9a33689a866188bc4740382a75c6c28c008f27bbd7bf9181a4 |
| sd.filing4952 | c463919a506118918868fb38826faafbd33315376d7f29963f6e818120502b75 |
| sd.investment_election | a3d91ae14f27d51f584ab503205e59279759a061e193355b00ebdf9732585be4 |
| sd.filed | 2809343429f80f68a2596485238d1f8e2f2d7c8ff67ec1d4b394d2e8bf49b38d |
| sd.zero | ce16c7c938fea13ef80d3f7cf152cea6dd84d856dea677c44b6e24fbc5cc60fd |
| sd.has_loss | 1e2c8c7df8ec4dc8a21e5ed72420311c4ae2a7b2895ded86e2213151661ada7f |
| sd.to1040 | c6be714faee43a2731a8e84b3fdbc9673314f85a90a3ddff50bd1fcc4a556678 |
| sd.net_gain | 9975d7415b27cc117455a94113d2867f95c94c61be4bc016b9faae8e92704ab9 |
| sd.distributions_if_dividends | e298b33df964936239e1aa4a899b76c8308e3041094d52235a155aab067750ae |
| 1a(d) | db323fdbca8ec838dd92e590ab5d32425bb9ad0a4ac875d70448d368a9a769f1 |
| 1a(e) | 4dbf6fdf6081e979d40efde9dbedb81fccfaea20f72c5a7a5d3cff390d9fbe4f |
| 1a(g) | a91699e17121d70da04ce1c520b0b5fffafa11141dc42b49fc132f94f3cb0a94 |
| 1a(h) | 1135af99d26f8eb86dd39d56926262ba5188731fb97d0eb2ae241d3d6e391610 |
| 1b(d) | 80c37dd3668f64aed9767cc78d73eef9fd24370f8ffb9f3e2be9b8769c8f4aa6 |
| 1b(e) | 55013dc3fb051eb21d7540f1d0b97672683670877a71a3a8d57d257e9b6a2152 |
| 1b(g) | 3c300eaa8758756e0c4d62de7e13e2e54105e1f3c9282c0e1a41b3a01267a833 |
| 1b(h) | 2e61606e0aca606976b8510b886b627d58318c385610aae1f88bc562d3ec2d43 |
| 2(d) | 70161a5b47a0923cbd563f0b70305694fbff1d73468b691eb5d4e9dde928979a |
| 2(e) | a625bce4a4ac5a41e71ac077a67c620e6db1eb9a1bb49b32e6eeeebbf29f78c8 |
| 2(g) | 309c10eb1735f926b0a285026842312945ab72ef6740824b673f70e98e059ef3 |
| 2(h) | acfbf57cf9a80970159ac4ce7a3699f6b35a0326cd57e008955dfd33493a9e02 |
| 3(d) | 3881906eb8acf70950703449d5f85a7341942d8c8f43b14eabab9f5ac97fc55b |
| 3(e) | d0c09a53ddb33c0d5766d0fcd690cee8df1c39cdd58f1e1d5e8de336b8ce7a95 |
| 3(g) | 18d700d521cc805dd90a43823c5558f4ebb57c4b16311bbc9c7c4fab8f8fec52 |
| 3(h) | 392b77525528ba1c0b2803cd4c1d6d5acee6fd5bd3dc8e206e79aa42c80cc840 |
| 8a(d) | 569a8311e92e3c0dba2aa6455ed621ea3c57c0361d0f1ed01ec74f5f0aaa8e87 |
| 8a(e) | 24c93ba85d3424ff1bc186ac2456fd471d57f8e9b378e1fca241d67781ec2697 |
| 8a(g) | 1a21469a74deebf480b3c6eaae4f7cb5f96b2f776d1633e7d31c2949f805dacd |
| 8a(h) | 06e8b78e1bc01658881cb8c82fd48553a2eded4c96e656bd5a597afff29a7afb |
| 8b(d) | 0a0a0864cf2acba9df092c565ea5756e67ed3636cb76797e46712a31c94af64a |
| 8b(e) | 7498b03f9a311d8a41cdb477fb8717403ac7cdf28202a2f0bc3de32fffe31e73 |
| 8b(g) | 3a4b75bf8c999a14258b4926f04608d9752a7c3a0299a652569793e5acabac6f |
| 8b(h) | 49b59614ab30770e9f6707ee914b636af6e2b7b9de95b18b1045a915692f5a98 |
| 9(d) | 5275f33fb72d1ea09ed99aa8359ac5e8ff86a7bc8eaa6be94795c373852d5383 |
| 9(e) | 2b01e0ce5107814c7b2bee68bffd7554b5cdef98dde2cef7f5ebbdfa1e60e905 |
| 9(g) | 6293f156eb58ecd309f515a267e91bb88e4f122da763b9d917a8f1ca1d05df41 |
| 9(h) | 6919b99cf7c94932c022cd1e6bc626ab7837d52258d3ed42913c18079bb8d260 |
| 10(d) | e601c2e7c50aba93bdcf87196a54a0da79f5da2714658316306292a4dacb1792 |
| 10(e) | 61e121db7dcbe3863d2c89c20706748c87ec1ee6f94a322442fa81a0b42b3627 |
| 10(g) | ae933c2ed14216bc750f70461c6e3f29ce64cf060eeab652478769b373a98f9a |
| 10(h) | 1b2f74ba7158600e7e443826aa59bded6b107da86d8cbbc8298f8df5683539a3 |
| 4 | 8443fdc5d500eee152c93b8ac69b9e0be5abbbeea079cb21ed743de3113ee688 |
| 5 | d2e3c99b1256da39cb9edb3b970d05980cba8a8f018c68f4a618bacc43e0a0d2 |
| 6 | e635ea08698589bfff629738a5a8bd7dddf7a260aeae4eaf8c46c4a0c54bb9d7 |
| 11 | df971d64bc79d90427e3786ce033c8847772e0a83e9172ee90e24a06204419c5 |
| 12 | b671b3f19b0d13b3d41295c28f916c47f9d85e9b983e57fb290fc2546c88a0d0 |
| 14 | 852949d5edfbbdcb954882a21b06e4cf555493d6cb93c30e7ea3372c6a3d9c3c |
| 13 | 919862ce6dea30eb0676331db28b397ec864ae318355df9f2156e996cae20b36 |
| 7 | a9899e1cb09a90f27e64f53f7ca4eb6bf3bb50aeead5c209cd3f6ae267790ef3 |
| 15 | 0db746e2ca06bdedba11c108bf05789daab7e6242607bc4d0572996b6b0cdc01 |
| 16 | b8dbb7d8e80124667bc28ec012ef66fb86be6ecbd9d4a9306e7686c76a56db45 |
| 17 | 9f04394cf47348ce817245c55c2e34211aea92c3fdb2faa27a605060397de9b7 |
| 20 | 8cf2ccba61ffc9bb1201307f724b0a77f616641dda4bdc38d073d2caae531f68 |
| 21 | 462bcca25b8919800e51951ff48b8e68fc1da54a6bbce933ad2a870576d270a8 |
| 22 | 5cc1ac47b2b535c6dbfa51b2449db78e1d2bb875c542c56b67fb5a6b62209fa9 |
| (rest of the document) | 428de7b0aecb0ec58b80e6b99fb756277616bb08aed9f21f90e6accedff64e84 |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| sd.distributions_if_dividends | 972cf38c15d80da0f8de2081225037cf0d43af899903b01f148edc4104ceee2a |
| 13 | 50d638b3489ec9106a7903e3fe89f538c4938a1c481a3921f285f376d8cb4b74 |
| 22 | 5d5fac7682b7a2fa13c2250bae25effb6239a504e9095246e6b2c15009ed77b2 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 17f7a05c3e95

| field | value |
| --- | --- |
| date | 2026-11-07 |
| review scope | lines sd.distributions_if_dividends, 13, 22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 17f7a05c3e95520dda86ec4817e51e72f9ddfc036f8dc0142ae5b70732bc99f6 |
| prompt policy | source-only-computation-v3+lines-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | fail |
| required input context sha256 | e0886dcde09d48dcd5c3e1c0cc2f107ce21eec356f66079436069b15cb8c206d |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 26b28332cff62995fd42207fa482dda8d718811fd78f700fcc2cf8ebc3067f56 |
| receipt | .transcription/sd.lines-3c1e462d90db |
| printed lines compared | 3 |
| agree / disagree / missing | 2 / 1 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sd | 2025; printed date 2025-12-11 | 11 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | eb461181b39879c79d1c0b7761ca0cd9ade46fdb1531cdee3281053c348f6c41 |
| f1099div | January 2024 (continuous-use form) | 1, 2, 3, 4, 5, 6 | whole document | 833d93e5f2d0bfcc8c9d720c0e8cb8e623cd2c6a8ee25f364f1f69f49fa490e3 | 5 | 617419bd079b1520174ceca8549065c9e4001f2b06a16d1425c5469bbe49fa3d |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | clcw, clcw26, sdtw |
| named form, inputs and named lines: f1040.line16, f1040.line25b, f1040.line25c_other, f1040.line26, f1040.line35a, f1040.line36, f1040.line3a, f1040.status, f1040.tax_exempt_interest | f1040 |
| named form, inputs and named lines: f4952.alternative_allocation, f4952.carryover, f4952.line1, f4952.line4g, f4952.prior_7, f4952.unsupported | f4952 |
| named form, inputs and named lines: household.community_property, household.cp_married, household.credit_disallowed, household.home_cost, household.married, household.qss_eligible, household.rdp, household.spouse_died_2025, household.unmarried | household |
| named form, inputs and named lines: sb.fbar_required, sb.form5471, sb.form8938, sb.line7a, sb.line8, sb.ordinary_dividends, sb.unsupported | sb |
| named form, inputs and named lines: scope.credits, scope.other_income, scope.other_line16, scope.schedule1 | scope |
| named line | ftc |
| shared page | div, g28, qbi, sales, u1250 |
| worksheet | qdcg |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: sd.h_zero
    printed: "(helper)"
    label: "Zero (no capital gain distributions)"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: sd.distributions_if_dividends
    printed: "(helper)"
    label: "Capital gain distributions (Form 1099-DIV, box 2a), when any dividends or other distributions were received"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [div.any, {const: true}]}
          then: sd.distributions
        - guard: {op: test, eq: [div.any, {const: false}]}
          then: sd.h_zero
    note: "The supplied pages don't define this interface. The Form 1099-DIV instructions say box 2a shows total capital gain distributions. The catalog question div.any asks whether any dividends or other distributions, including capital gain distributions, were received. I read the interface as the supplied distributions (sd.distributions) when div.any is Yes, and zero when it is No. The IRS text does not fix this gating; it is inferred."

  - id: sd.line13
    printed: "13"
    label: "Capital gain distributions. See the instructions"
    type: NonNegDollars
    expr: {op: copy, from: sd.distributions_if_dividends}
    note: "The line 13 instructions say only \"See Capital Gain Distributions, earlier\", and that section is not in the supplied text. From Form 1099-DIV box 2a (\"See How To Report in the Instructions for Schedule D\"), I take the amount to be the total capital gain distributions, held in the supplied input sd.distributions. Any other sources the omitted section may list, such as Form 2439, are not encoded here."

  - id: sd.h_show22
    printed: "(helper)"
    label: "Line 22 is reached: line 17 is not Yes (lines 18 through 20 were not completed)"
    type: Bool
    expr: {op: test, eq: [sd.line17, {const: false}]}
    note: "Line 20 says \"Don't complete lines 21 and 22 below\" whichever way it is answered, and line 20 is reached only when line 17 is Yes. Line 16 being a loss or zero, or line 17 being No, sends the filer to line 22. So line 22 is shown exactly when line 17 is false. This assumes sd.line17 is false, not unknown, when line 16 is a loss or zero."

  - id: sd.line22
    printed: "22"
    label: "Do you have qualified dividends on Form 1040, 1040-SR, or 1040-NR, line 3a?"
    type: Bool
    expr: {op: test, gt: [f1040.line3a, {const: 0}]}
    shown_when: sd.h_show22
```
```

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
