# Transcription agreement — sd

Second transcription of `Schedule D — securities sales and supplied distribution subtotals` by an isolated model (spec 6.5), compared line by line with `forms/2025/sd.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 6995153b5da31c2c6dd56c90341fbf55f2c406f252bf69e7c7e4dc08912849ef |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 95af1552490362a6fb1747f63af8c126a8d25e5949b008f15250dacf3ee49e45 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 14f6c7571f90fea7fd4da5231e18ae13294ab3b969700f9e50a613b3212a083f |
| printed lines compared | 55 |
| agree / disagree / missing | 15 / 40 / 0 |
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
{"ref": "f4952.line4g"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "eq"}, {"args": [{"ref": "f4952.line5"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line1"}, {"ref": "f4952.line4c"}], "test": "lt"}], "test": "all"}, {"args": [{"ref": "f4952.line3"}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"ref": "f4952.line4c"}, {"ref": "f4952.line1"}], "test": "le"}, {"args": [{"const": 0}, {"ref": "f4952.line5"}], "test": "lt"}, {"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0}, {"ref": "f4952.line3"}], "test": "lt"}], "test": "all"}, {"args": [{"const": 0}, {"ref": "f4952.line4g"}], "test": "lt"}], "test": "any"}, "then": {"ref": "f4952.line4g"}}], "op": "choose"}
```

Second transcription's note: Schedule D Tax Worksheet: 'if you file Form 4952 and you have an amount on line 4g'. This is the line 4g amount when Form 4952 is filed, and zero otherwise.

Ruling: scope; i1040sd p. 15, Schedule D Tax Worksheet, applicability: "if you file Form 4952 and you have an amount on line 4g", line 3: "Enter the amount from Form 4952 (used to figure investment interest expense deduction), line 4g". The candidate gives f4952.line4g when Form 4952 is filed or line 4g is positive and 0 otherwise, using the published Form 4952 filing test (now with line 3 and the 2024 carryforward); the project copies f4952.election, which is line 4g behind its cited gates and 0 when no election is made, so both give line 4g whenever both compute. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,642 of 1,779 comparisons agree; 58 project-refuses, 55 project-unknown, 24 candidate-refuses (by return: {"incomplete": {"project-unknown": 24}, "refused": {"candidate-refuses": 24, "project-refuses": 58, "project-unknown": 31}}); no value differs. The 58 project-refuses are the election's cited gates and the Schedule D and Form 1099-DIV gates its check reads (classm.asset.2, sales.digital; classm.dcprov.1, classm.f8606.1, classm.refund.1, div.bad_components, against the candidate's $2,491; classm.se.1, div.section1202). The 24 candidate-refuses (sb.fbar_required, sb.form8938, sb.unsupported, sb.line8; classm.w2.1.deepseek, classm.otjob.2, generated 11 and 16) come from its filing test reading f4952.line4c and so Schedule B; all 24 are on returns the full interview refuses. The 55 project-unknown withhold sd.other_forms, sd.carryover or sd.distributions (partials of classm.f4952.3.deepseek, classm.g28.1.deepseek) or are fixtures that set the gate without the 2024 figures (classm.asset.3, UNK clcw.prior_sd7, a refused return). The text names no condition the project leaves unscreened. Project stands.

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

Second transcription's note: Exception 1: no Schedule D if you have no capital losses, your only capital gains are Form 1099-DIV box 2a distributions, and no Form 1099-DIV shows boxes 2b, 2c or 2d (and no qualified opportunity fund deferral, which has no input here). A sale, a carryover loss, another-form item or a box 2b/2c/2d amount means you must file. Filing anyway with only distributions is optional; I treat it as not filed.

Ruling: model error; i1040gi p. 31, Line 7a, Exception 1: "You don’t have to file Form 8949 or Schedule D if ... 1. You have no capital losses, and your only capital gains are capital gain distributions from Form(s) 1099-DIV, box 2a ... and 2. None of the Form(s) 1099-DIV ... have an amount in box 2b ..., box 2c ..., or box 2d"; i1040sd p. 10, Capital Loss Carryover Worksheet: "Use this worksheet to figure your capital loss carryovers from 2024 to 2025 if your 2024 Schedule D, line 21, is a loss and (a) that loss is a smaller loss than the loss on your 2024 Schedule D, line 16; or (b) ... line 15 would be less than zero ... Otherwise, you don’t have any carryovers." The candidate requires Schedule D whenever sd.carryover is answered Yes; the project requires it when line 6 or line 14 is a nonzero loss (with the sales count and lines 18 and 19). A Yes to the gate with neither (a) nor (b) gives no carryover, so no capital loss and no Schedule D. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,694 of 1,779 comparisons agree; 44 project-unknown, 40 project-refuses, 1 value (by return: {"completed": {"value": 1}, "incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 40, "project-unknown": 27}}). The 1 value difference is fixture stage20.line21_at_both_bounds (completed): sd.carryover true, no sales, worksheet lines 8 and 13 both $0 (lines 6 and 14 $0), project false, candidate true; the source says this filer has no carryover, so the project is right. The candidate's box 2b/2c/2d tests agree with the project's line 18/19 tests on every computed return (box 2c is refused by div.section1202, classm.se.1). The 40 project-refuses are cited gates (sd.other_forms, which the candidate treats as a filing trigger: classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1, classm.s179.1, classm.scveh.6; div.section1202), and the 44 project-unknown are withheld screen answers (sd.distributions, sd.other_forms) or gate-set fixtures without 2024 figures on refused returns (classm.f8889.5, classm.carloan.3, UNK clcw.prior_sd15): scope. Project stands.

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
{"alternatives": [{"guard": {"args": [{"line": "16"}, {"const": 0}], "test": "le"}, "then": {"line": "21"}}, {"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "lt"}, "then": {"line": "16"}}], "op": "choose"}
```

Ruling: scope; f1040sd p. 2, line 16: "If line 16 is a gain, enter the amount from line 16 on Form 1040 ... line 7a", "If line 16 is zero, skip lines 17 through 21 below and enter -0- on Form 1040, 1040-SR, or 1040-NR, line 7a", "If line 16 is a loss, ... Then, go to line 21". The candidate sends line 16 ≤ 0 to line 21 and a gain to line 16; line 21 is $0 when line 16 is not a loss, so both enter line 16 for a gain or zero and line 21 for a loss. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,704 of 1,779 comparisons agree; 74 project-refuses, 1 project-unknown (by return: {"refused": {"project-refuses": 74, "project-unknown": 1}}); every in-scope comparison but one withheld answer agrees and no value differs. The 74 project-refuses are the cited Schedule D and Form 1099-DIV gates reached through lines 16 and 21 (classm.asset.2, sales.digital, candidate $6,847; classm.dcprov.1, classm.f8606.1, classm.refund.1, classm.retirement.1, div.bad_components; classm.se.1, div.section1202); the 1 project-unknown (stage16.cleanup.f8959_line16_se_refused) withholds the div.box2c screen. Project stands.

### sd.net_gain — Nonnegative net capital gain for QDCGT
Status: **AGREE**

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

Second transcription's note: Line 1a is for short-term transactions with basis reported to the IRS (the Box A/G kind) that the filer chose to report in aggregate. Entries routed to aggregate with any other box are refused, not dropped.

Ruling: scope; f1040sd p. 1, line 1a: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums the column over box A or box G on the aggregate route; the project sums box A on the aggregate route behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,679 of 1,779 comparisons agree; 60 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 60, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1a: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums the column over box A or box G on the aggregate route; the project sums box A on the aggregate route behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,679 of 1,779 comparisons agree; 60 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 60, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1a: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate enters 0 in column (g), reading "no adjustments"; the project sums sales.g over box A on the aggregate route, and an aggregate entry with an adjustment is refused by sales.bad_aggregate (classm.sc.3), so the project's column (g) is 0 on every return it computes. No value differs. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,628 of 1,779 comparisons agree; 79 project-unknown, 72 project-refuses (by return: {"incomplete": {"project-unknown": 44}, "refused": {"project-refuses": 72, "project-unknown": 35}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1a: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate computes column (h) as (d) − (e) + (g) (f1040sd p. 1, column (h): "Subtract column (e) from column (d) and combine the result with column (g)") over box A or G on the aggregate route; the project sums sales.h over box A. Column (h) is that arithmetic per entry, and box G is refused. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,679 of 1,779 comparisons agree; 60 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 60, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1b: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked". The candidate sums the column over box A or box G (detail route); the project sums box A behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1b: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked". The candidate sums the column over box A or box G (detail route); the project sums box A behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1b: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked". The candidate sums the column over box A or box G (detail route); the project sums box A behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1b: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked". The candidate computes column (h) as (g) + (d) − (e) (f1040sd p. 1, column (h): "Subtract column (e) from column (d) and combine the result with column (g)") over boxes A or G on the detail route; the project sums sales.h over box A on the detail route. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 2: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked". The candidate sums the column over box B or box H (detail route); the project sums box B behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 2: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked". The candidate sums the column over box B or box H (detail route); the project sums box B behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 2: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked". The candidate sums the column over box B or box H (detail route); the project sums box B behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 2: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked". The candidate computes column (h) as (g) + (d) − (e) (f1040sd p. 1, column (h): "Subtract column (e) from column (d) and combine the result with column (g)") over boxes B or H on the detail route; the project sums sales.h over box B on the detail route. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 3: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked". The candidate sums the column over box C or box I (detail route); the project sums box C behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 3: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked". The candidate sums the column over box C or box I (detail route); the project sums box C behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 3: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked". The candidate sums the column over box C or box I (detail route); the project sums box C behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 3: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked". The candidate computes column (h) as (g) + (d) − (e) (f1040sd p. 1, column (h): "Subtract column (e) from column (d) and combine the result with column (g)") over boxes C or I on the detail route; the project sums sales.h over box C on the detail route. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8a: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums the column over box D or box J on the aggregate route; the project sums box D on the aggregate route behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,679 of 1,779 comparisons agree; 60 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 60, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8a: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums the column over box D or box J on the aggregate route; the project sums box D on the aggregate route behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,679 of 1,779 comparisons agree; 60 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 60, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8a: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate enters 0 in column (g), reading "no adjustments"; the project sums sales.g over box D on the aggregate route, and an aggregate entry with an adjustment is refused by sales.bad_aggregate (classm.sc.3), so the project's column (g) is 0 on every return it computes. No value differs. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,628 of 1,779 comparisons agree; 79 project-unknown, 72 project-refuses (by return: {"incomplete": {"project-unknown": 44}, "refused": {"project-refuses": 72, "project-unknown": 35}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8a: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate computes column (h) as (d) − (e) + (g) (f1040sd p. 1, column (h): "Subtract column (e) from column (d) and combine the result with column (g)") over box D or J on the aggregate route; the project sums sales.h over box D. Column (h) is that arithmetic per entry, and box J is refused. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,679 of 1,779 comparisons agree; 60 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 60, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8b: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked". The candidate sums the column over box D or box J (detail route); the project sums box D behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8b: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked". The candidate sums the column over box D or box J (detail route); the project sums box D behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8b: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked". The candidate sums the column over box D or box J (detail route); the project sums box D behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8b: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked". The candidate computes column (h) as (g) + (d) − (e) (f1040sd p. 1, column (h): "Subtract column (e) from column (d) and combine the result with column (g)") over boxes D or J on the detail route; the project sums sales.h over box D on the detail route. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 9: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked". The candidate sums the column over box E or box K (detail route); the project sums box E behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 9: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked". The candidate sums the column over box E or box K (detail route); the project sums box E behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 9: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked". The candidate sums the column over box E or box K (detail route); the project sums box E behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 9: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked". The candidate computes column (h) as (g) + (d) − (e) (f1040sd p. 1, column (h): "Subtract column (e) from column (d) and combine the result with column (g)") over boxes E or K on the detail route; the project sums sales.h over box E on the detail route. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 10: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked". The candidate sums the column over box F or box L (detail route); the project sums box F behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 10: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked". The candidate sums the column over box F or box L (detail route); the project sums box F behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 10: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked". The candidate sums the column over box F or box L (detail route); the project sums box F behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 10: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked". The candidate computes column (h) as (g) + (d) − (e) (f1040sd p. 1, column (h): "Subtract column (e) from column (d) and combine the result with column (g)") over boxes F or L on the detail route; the project sums sales.h over box F on the detail route. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sd.carryover"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sd.carryover"}], "test": "eq"}, "then": {"ref": "clcw.line8"}}], "op": "choose"}
```

Second transcription's note: The worksheet applies only if 2024 Schedule D line 21 is a loss (otherwise you have no carryovers). Line 6 is shown here as a positive amount and subtracted on line 7, because it is printed in parentheses.

Ruling: representation; f1040sd p. 1, line 6: "Short-term capital loss carryover. Enter the amount, if any, from line 8 of your Capital Loss Carryover Worksheet in the instructions", printed in the column (h) parentheses "( )"; line 7: "Combine lines 1a through 6 in column (h)". Both take worksheet line 8 behind the same sd.carryover choice; the candidate holds it positive and subtracts it on line 7, the project holds it negative (sd.line6_ws = 0 − clcw.line8) and adds it, the owner's sign decision (Stage 20 decisions, Settled 1, T-004). Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,695 of 1,779 comparisons agree; 38 project-unknown, 26 value, 20 project-refuses (by return: {"completed": {"value": 7}, "incomplete": {"project-unknown": 17, "value": 1}, "refused": {"project-refuses": 20, "project-unknown": 21, "value": 18}}). Every one of the 26 value differences is the same amount with the opposite sign (candidate clcw.line8, project 0 − clcw.line8; e.g. classm.sd.2, −$16,565 against $16,565; classm.clcw.2.deepseek, −$24,626 against $24,626; classm.clcw.4.deepseek, −$6,401 against $6,401), and line 7 agrees on every in-scope comparison, so the printed amount in parentheses is the same. The worksheet value was checked by hand on classm.sd.2 (2024 line 7 −$19,565, line 2 $3,000, line 4 $3,000, line 6 $0, line 8 $16,565). The 20 project-refuses are sd.other_forms (classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1, classm.s179.1, classm.scveh.6) and the 38 project-unknown withhold sd.other_forms or sd.carryover: scope. The candidate's sign is also read by the project's g28.line5 and u1250.line16, which expect a negative line 14; that effect is ruled on line 20. Project stands.

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
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sd.carryover"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sd.carryover"}], "test": "eq"}, "then": {"ref": "clcw.line13"}}], "op": "choose"}
```

Second transcription's note: Shown as a positive amount and subtracted on line 15, because it is printed in parentheses.

Ruling: representation; f1040sd p. 1, line 14: "Long-term capital loss carryover. Enter the amount, if any, from line 13 of your Capital Loss Carryover Worksheet in the instructions", printed "14 ( )"; line 15: "Combine lines 8a through 14 in column (h)". Both take worksheet line 13 behind the sd.carryover choice; the candidate holds it positive and subtracts it on line 15, the project holds it negative (sd.line14_ws = 0 − clcw.line13), the owner's sign decision (Stage 20 decisions, Settled 1, T-004). Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,699 of 1,779 comparisons agree; 38 project-unknown, 22 value, 20 project-refuses (by return: {"completed": {"value": 6}, "incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 20, "project-unknown": 21, "value": 16}}). Every one of the 22 value differences is the same amount with the opposite sign (e.g. classm.sd.2, −$17,835 against $17,835; classm.sd.3, −$28,659 against $28,659; classm.clcw.3.deepseek, −$2,216 against $2,216), and line 15 agrees on every in-scope comparison. The 20 project-refuses are sd.other_forms and the 38 project-unknown withhold sd.other_forms or sd.carryover: scope. Project stands.

### 13 — Capital gain distributions
Status: **AGREE**

### 7 — Combine the amounts for Schedule D line 7
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "1a(h)"}, {"line": "1b(h)"}, {"line": "2(h)"}, {"line": "3(h)"}, {"line": "4"}, {"line": "5"}, {"line": "6"}], "op": "sum"}
```

Second:

```json
{"from": {"of": [{"line": "1a(h)"}, {"line": "1b(h)"}, {"line": "2(h)"}, {"line": "3(h)"}, {"line": "4"}, {"line": "5"}], "op": "sum"}, "op": "subtract", "take": {"line": "6"}}
```

Ruling: scope; f1040sd p. 1, line 7: "Net short-term capital gain or (loss). Combine lines 1a through 6 in column (h)". The candidate subtracts its positive line 6; the project adds its negative line 6 (T-004, owner's sign decision): the same sum. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,739 of 1,779 comparisons agree; 40 project-refuses (by return: {"refused": {"project-refuses": 40}}); every in-scope comparison agrees (1,704 of 1,704), including every return with a short-term carryover. The 40 project-refuses are sales.one's cited gates (sales.digital: classm.asset.2, stage14.sep.step1_other_se_income, sales.refuse.digital.G/H/I/J, candidate $4,000) and sd.other_forms. Project stands.

### 15 — Combine the amounts for Schedule D line 15
Status: **DISAGREE**

Project:

```json
{"of": [{"line": "10(h)"}, {"line": "11"}, {"line": "12"}, {"line": "13"}, {"line": "14"}, {"line": "8a(h)"}, {"line": "8b(h)"}, {"line": "9(h)"}], "op": "sum"}
```

Second:

```json
{"from": {"of": [{"line": "10(h)"}, {"line": "11"}, {"line": "12"}, {"line": "13"}, {"line": "8a(h)"}, {"line": "8b(h)"}, {"line": "9(h)"}], "op": "sum"}, "op": "subtract", "take": {"line": "14"}}
```

Ruling: scope; f1040sd p. 1, line 15: "Net long-term capital gain or (loss). Combine lines 8a through 14 in column (h)". The candidate subtracts its positive line 14; the project adds its negative line 14 (T-004): the same sum. Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,704 of 1,779 comparisons agree; 74 project-refuses, 1 project-unknown (by return: {"refused": {"project-refuses": 74, "project-unknown": 1}}); no value differs. The 74 project-refuses are the cited Schedule D and Form 1099-DIV gates (classm.asset.2, sales.digital, candidate $6,847; classm.dcprov.1, classm.f8606.1, classm.refund.1, classm.retirement.1, div.bad_components; classm.se.1, div.section1202) and the 1 project-unknown withholds div.box2c (stage16.cleanup.f8959_line16_se_refused). Project stands.

### 16 — Combine the amounts for Schedule D line 16
Status: **AGREE**

### 17 — Are lines 15 and 16 both gains?
Status: **AGREE**

### 20 — Are lines 18 and 19 zero and are you not filing Form 4952?
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "eq"}, {"args": [{"ref": "f4952.line5"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line1"}, {"ref": "f4952.line4c"}], "test": "lt"}], "test": "all"}, {"args": [{"ref": "f4952.line3"}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "eq"}, {"args": [{"ref": "f4952.line5"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line1"}, {"ref": "f4952.line4c"}], "test": "lt"}], "test": "all"}, {"args": [{"ref": "f4952.line3"}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"line": "18"}, {"const": 0}], "test": "le"}, {"args": [{"line": "19"}, {"const": 0}], "test": "le"}], "test": "all"}
```

Ruling: interface gap; f1040sd p. 2, line 20: "Are lines 18 and 19 both zero or blank and you are not filing Form 4952?"; i1040sd p. 11, 28% Rate Gain Worksheet line 5: "Enter your long-term capital loss carryovers from Schedule D, line 14", printed "5. ( )". The candidate's own line 20 test is the project's (line 18 ≤ 0 and line 19 ≤ 0 on NonNegDollars lines, the same Form 4952 filing test). Triage executable-triage-v2 (triage/sd.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,721 of 1,779 comparisons agree; 53 project-refuses, 4 value, 1 project-unknown (by return: {"completed": {"value": 2}, "refused": {"project-refuses": 53, "project-unknown": 1, "value": 2}}). All 4 value differences (classm.sd.2 and its deepseek twin, stage20.blind.r7, generated 235; project true, candidate false) come from the candidate's positive line 14 entering the project's g28.line5, which copies sd.line14 and expects a loss held negative: with it the 28% worksheet line 7 becomes $1,270 (classm.sd.2), $12,000 (stage20.blind.r7) or $321.34 (generated 235) where the project's is $0, so the candidate's line 18 is positive. The published interface gives g28.line5 and u1250.line16 only as "type Dollars", not their reading of sd.line14 or its sign, so the candidate could not keep its sign consistent with them; the worksheet's own parentheses do not settle the project's encoding. The 53 project-refuses are cited gates (sales.digital: classm.asset.2, stage14.sep.step1_other_se_income; div.bad_components: classm.dcprov.1, classm.f8606.1, classm.refund.1; div.section1202: classm.se.1) and the 1 project-unknown withholds div.box2c: scope. Project stands.

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **AGREE**

### 22 — Do you have qualified dividends?
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sd.line18 | sd.h_bad_agg, sd.h_special, sd.other_forms | sd.h_bad_agg, sd.h_special |
| sd.line19 | sd.h_bad_agg, sd.h_special, sd.other_forms | sd.h_bad_agg, sd.h_special |
| sd.has_loss | sd.h_bad_agg, sd.other_forms | sd.h_bad_agg |
| sd.to1040 | sd.h_bad_agg, sd.other_forms | sd.h_bad_agg |
| sd.net_gain | sd.h_bad_agg, sd.other_forms | sd.h_bad_agg |
| 1a(d) | sd.h_bad_agg | sd.h_bad_agg |
| 1a(e) | sd.h_bad_agg | sd.h_bad_agg |
| 1a(h) | sd.h_bad_agg | sd.h_bad_agg |
| 8a(d) | sd.h_bad_agg | sd.h_bad_agg |
| 8a(e) | sd.h_bad_agg | sd.h_bad_agg |
| 8a(h) | sd.h_bad_agg | sd.h_bad_agg |
| 4 | sd.other_forms | - |
| 5 | sd.other_forms | - |
| 11 | sd.other_forms | - |
| 12 | sd.other_forms | - |
| 7 | sd.h_bad_agg, sd.other_forms | sd.h_bad_agg |
| 15 | sd.h_bad_agg, sd.other_forms | sd.h_bad_agg |
| 16 | sd.h_bad_agg, sd.other_forms | sd.h_bad_agg |
| 17 | sd.h_bad_agg, sd.other_forms | sd.h_bad_agg |
| 20 | sd.h_bad_agg, sd.h_special, sd.other_forms | sd.h_bad_agg, sd.h_special |
| 21 | sd.h_bad_agg, sd.other_forms | sd.h_bad_agg |

## Raw second transcription

```yaml
```yaml
lines:
  - id: sd.zero
    printed: "(helper)"
    label: "Zero (blank line or -0- entry on Schedule D)"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: sd.h_bad_agg_count
    printed: "(helper)"
    label: "Number of transactions routed to lines 1a/8a whose box does not show basis reported to the IRS (not Box A, D, G or J)"
    type: Count
    expr:
      op: sum_over
      collection: sales
      field: sales.one
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "aggregate"}]}
          - op: test
            not:
              op: test
              any:
                - {op: test, eq: [sales.box, {const: "A"}]}
                - {op: test, eq: [sales.box, {const: "D"}]}
                - {op: test, eq: [sales.box, {const: "G"}]}
                - {op: test, eq: [sales.box, {const: "J"}]}

  - id: sd.h_bad_agg
    printed: "(helper)"
    label: "A transaction routed to lines 1a/8a is not one for which basis was reported to the IRS"
    type: Bool
    expr: {op: test, gt: [sd.h_bad_agg_count, {const: 0, type: Count}]}

  - id: sd.h_special_count
    printed: "(helper)"
    label: "Number of sales involving collectibles, section 1202 stock or section 1250 property"
    type: Count
    expr:
      op: sum_over
      collection: sales
      field: sales.one
      where: {op: test, eq: [sales.special, {const: true}]}

  - id: sd.h_special
    printed: "(helper)"
    label: "Any sale involving collectibles, section 1202 stock or section 1250 property"
    type: Bool
    expr: {op: test, gt: [sd.h_special_count, {const: 0, type: Count}]}

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
    refuses: [sd.h_bad_agg]
    note: "Line 1a is for short-term transactions with basis reported to the IRS (the Box A/G kind) that the filer chose to report in aggregate. Entries routed to aggregate with any other box are refused, not dropped."

  - id: sd.line1a.e
    printed: "1a(e)"
    label: "Line 1a — Cost (or other basis)"
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
    refuses: [sd.h_bad_agg]

  - id: sd.line1a.g
    printed: "1a(g)"
    label: "Line 1a — Adjustments (no adjustments for line 1a transactions)"
    type: Dollars
    expr: {op: param, ref: sales.zero}

  - id: sd.line1a.h
    printed: "1a(h)"
    label: "Line 1a — Gain or (loss). Subtract the cost or other basis in column (e) from the proceeds (sales price) in column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line1a.d, take: sd.line1a.e}

  - id: sd.line1b.d
    printed: "1b(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked — Proceeds"
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

  - id: sd.line1b.e
    printed: "1b(e)"
    label: "Line 1b — Cost (or other basis)"
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

  - id: sd.line1b.g
    printed: "1b(g)"
    label: "Line 1b — Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
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

  - id: sd.h_1b_de
    printed: "(helper)"
    label: "Line 1b — subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line1b.d, take: sd.line1b.e}

  - id: sd.line1b.h
    printed: "1b(h)"
    label: "Line 1b — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_1b_de, sd.line1b.g]}

  - id: sd.line2.d
    printed: "2(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked — Proceeds"
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

  - id: sd.line2.e
    printed: "2(e)"
    label: "Line 2 — Cost (or other basis)"
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

  - id: sd.line2.g
    printed: "2(g)"
    label: "Line 2 — Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
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

  - id: sd.h_2_de
    printed: "(helper)"
    label: "Line 2 — subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line2.d, take: sd.line2.e}

  - id: sd.line2.h
    printed: "2(h)"
    label: "Line 2 — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_2_de, sd.line2.g]}

  - id: sd.line3.d
    printed: "3(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked — Proceeds"
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

  - id: sd.line3.e
    printed: "3(e)"
    label: "Line 3 — Cost (or other basis)"
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

  - id: sd.line3.g
    printed: "3(g)"
    label: "Line 3 — Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
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

  - id: sd.h_3_de
    printed: "(helper)"
    label: "Line 3 — subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line3.d, take: sd.line3.e}

  - id: sd.line3.h
    printed: "3(h)"
    label: "Line 3 — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_3_de, sd.line3.g]}

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
    refuses: [sd.h_bad_agg]

  - id: sd.line8a.e
    printed: "8a(e)"
    label: "Line 8a — Cost (or other basis)"
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
    refuses: [sd.h_bad_agg]

  - id: sd.line8a.g
    printed: "8a(g)"
    label: "Line 8a — Adjustments (no adjustments for line 8a transactions)"
    type: Dollars
    expr: {op: param, ref: sales.zero}

  - id: sd.line8a.h
    printed: "8a(h)"
    label: "Line 8a — Gain or (loss). Subtract the cost or other basis in column (e) from the proceeds (sales price) in column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line8a.d, take: sd.line8a.e}

  - id: sd.line8b.d
    printed: "8b(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked — Proceeds"
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

  - id: sd.line8b.e
    printed: "8b(e)"
    label: "Line 8b — Cost (or other basis)"
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

  - id: sd.line8b.g
    printed: "8b(g)"
    label: "Line 8b — Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
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

  - id: sd.h_8b_de
    printed: "(helper)"
    label: "Line 8b — subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line8b.d, take: sd.line8b.e}

  - id: sd.line8b.h
    printed: "8b(h)"
    label: "Line 8b — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_8b_de, sd.line8b.g]}

  - id: sd.line9.d
    printed: "9(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked — Proceeds"
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

  - id: sd.line9.e
    printed: "9(e)"
    label: "Line 9 — Cost (or other basis)"
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

  - id: sd.line9.g
    printed: "9(g)"
    label: "Line 9 — Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
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

  - id: sd.h_9_de
    printed: "(helper)"
    label: "Line 9 — subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line9.d, take: sd.line9.e}

  - id: sd.line9.h
    printed: "9(h)"
    label: "Line 9 — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_9_de, sd.line9.g]}

  - id: sd.line10.d
    printed: "10(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked — Proceeds"
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

  - id: sd.line10.e
    printed: "10(e)"
    label: "Line 10 — Cost (or other basis)"
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

  - id: sd.line10.g
    printed: "10(g)"
    label: "Line 10 — Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
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

  - id: sd.h_10_de
    printed: "(helper)"
    label: "Line 10 — subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line10.d, take: sd.line10.e}

  - id: sd.line10.h
    printed: "10(h)"
    label: "Line 10 — Gain or (loss). Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_10_de, sd.line10.g]}

  - id: sd.line4
    printed: "4"
    label: "Short-term gain from Form 6252 and short-term gain or (loss) from Forms 4684, 6781, and 8824"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    refuses: [sd.other_forms]

  - id: sd.line5
    printed: "5"
    label: "Net short-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    refuses: [sd.other_forms]

  - id: sd.line6
    printed: "6"
    label: "Short-term capital loss carryover. Enter the amount, if any, from line 8 of your Capital Loss Carryover Worksheet in the instructions"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sd.carryover, {const: true}]}
          then: clcw.line8
        - guard: {op: test, eq: [sd.carryover, {const: false}]}
          then: sd.zero
    note: "The worksheet applies only if 2024 Schedule D line 21 is a loss (otherwise you have no carryovers). Line 6 is shown here as a positive amount and subtracted on line 7, because it is printed in parentheses."

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

  - id: sd.line14
    printed: "14"
    label: "Long-term capital loss carryover. Enter the amount, if any, from line 13 of your Capital Loss Carryover Worksheet in the instructions"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sd.carryover, {const: true}]}
          then: clcw.line13
        - guard: {op: test, eq: [sd.carryover, {const: false}]}
          then: sd.zero
    note: "Shown as a positive amount and subtracted on line 15, because it is printed in parentheses."

  - id: sd.line13
    printed: "13"
    label: "Capital gain distributions"
    type: NonNegDollars
    expr: {op: copy, from: sd.distributions}

  - id: sd.h_7_sum
    printed: "(helper)"
    label: "Lines 1a through 5, column (h), added together"
    type: Dollars
    expr: {op: sum, of: [sd.line1a.h, sd.line1b.h, sd.line2.h, sd.line3.h, sd.line4, sd.line5]}

  - id: sd.line7
    printed: "7"
    label: "Net short-term capital gain or (loss). Combine lines 1a through 6 in column (h)"
    type: Dollars
    expr: {op: subtract, from: sd.h_7_sum, take: sd.line6}

  - id: sd.h_15_sum
    printed: "(helper)"
    label: "Lines 8a through 13, column (h), added together"
    type: Dollars
    expr: {op: sum, of: [sd.line8a.h, sd.line8b.h, sd.line9.h, sd.line10.h, sd.line11, sd.line12, sd.line13]}

  - id: sd.line15
    printed: "15"
    label: "Net long-term capital gain or (loss). Combine lines 8a through 14 in column (h)"
    type: Dollars
    expr: {op: subtract, from: sd.h_15_sum, take: sd.line14}

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
    label: "If you are required to complete the 28% Rate Gain Worksheet (see instructions), enter the amount, if any, from line 7 of that worksheet"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sd.line17, {const: true}]}
          then: g28.line7
        - guard: {op: test, eq: [sd.line17, {const: false}]}
          then: sd.zero
    refuses: [sd.h_special]
    note: "Open point: the line 18 instructions require the worksheet only after 'Yes' on line 17 and for Form 8949 collectibles gain or a section 1202 exclusion. Those sales are refused here (sales.special). The worksheet's line 4 also takes collectibles gain from Form 1099-DIV box 2d. I read it as completed whenever line 17 is Yes. With no 8949 collectibles or 1202 items and no box 2d, its line 7 is zero, so this matches the strict reading. If line 17 is No, the line is blank (zero)."

  - id: sd.line19
    printed: "19"
    label: "If you are required to complete the Unrecaptured Section 1250 Gain Worksheet (see instructions), enter the amount, if any, from line 18 of that worksheet"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sd.line17, {const: true}]}
          then: u1250.line18
        - guard: {op: test, eq: [sd.line17, {const: false}]}
          then: sd.zero
    refuses: [sd.h_special]
    note: "The worksheet is required after 'Yes' on line 17 if any listed condition applies. In this scope the only one left is a Form 1099-DIV reporting unrecaptured section 1250 gain (box 2b); the others are refused by sd.other_forms or sales.special. I read the worksheet as completed whenever line 17 is Yes; with no box 2b amount, its line 18 should be zero. If line 17 is No, the line is blank (zero)."

  - id: sd.filing4952
    printed: "(helper)"
    label: "You are filing Form 4952"
    type: Bool
    expr: {op: copy, from: f4952.required}
    note: "Schedule D does not say when Form 4952 is filed. I take it from the Form 4952 interface's own filing determination (f4952.required)."

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

  - id: sd.investment_election
    printed: "(helper)"
    label: "Amount on Form 4952, line 4g, if you file Form 4952 (Schedule D Tax Worksheet trigger and line 3)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sd.filing4952, {const: true}]}
          then: f4952.line4g
        - guard: {op: test, eq: [sd.filing4952, {const: false}]}
          then: sd.zero
    note: "Schedule D Tax Worksheet: 'if you file Form 4952 and you have an amount on line 4g'. This is the line 4g amount when Form 4952 is filed, and zero otherwise."

  - id: sd.h_loss_limit
    printed: "(helper)"
    label: "($3,000), or if married filing separately, ($1,500)"
    type: Dollars
    expr: {op: param, ref: sd.loss_limit}

  - id: sd.h_21_figured
    printed: "(helper)"
    label: "The smaller of the loss on line 16 or the loss limit, treating both as positive numbers"
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
          then: sd.h_21_figured
        - guard: {op: test, ge: [sd.line16, {const: 0}]}
          then: sd.zero
    note: "The amounts are negative, so the smaller loss (treated as positive) is the larger signed value. Line 21 is skipped (zero) when line 16 is zero or a gain."

  - id: sd.line22
    printed: "22"
    label: "Do you have qualified dividends on Form 1040, 1040-SR, or 1040-NR, line 3a?"
    type: Bool
    expr: {op: test, gt: [f1040.line3a, {const: 0}]}

  - id: sd.to1040
    printed: "(helper)"
    label: "Amount for Form 1040, line 7a: line 16 if a gain; line 21 if a loss; -0- if line 16 is zero"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, gt: [sd.line16, {const: 0}]}
          then: sd.line16
        - guard: {op: test, le: [sd.line16, {const: 0}]}
          then: sd.line21

  - id: sd.has_loss
    printed: "(helper)"
    label: "Line 16 is a loss"
    type: Bool
    expr: {op: test, lt: [sd.line16, {const: 0}]}

  - id: sd.h_min_15_16
    printed: "(helper)"
    label: "The smaller of line 15 or line 16 of Schedule D"
    type: Dollars
    expr: {op: smaller_of, of: [sd.line15, sd.line16]}

  - id: sd.net_gain
    printed: "(helper)"
    label: "The smaller of line 15 or line 16 of Schedule D; if either is blank or a loss, -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sd.h_min_15_16, take: {const: 0}}
    note: "Follows Qualified Dividends and Capital Gain Tax Worksheet line 3 ('Yes'): if either line is a loss, the smaller one is a loss and the floor gives -0-."

  - id: sd.h_sales_count
    printed: "(helper)"
    label: "Number of securities sales entered"
    type: Count
    expr: {op: sum_over, collection: sales, field: sales.one}

  - id: sd.filed
    printed: "(helper)"
    label: "You must file Schedule D (Exception 1 to the Form 1040 line 7a instructions does not apply)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [sd.h_sales_count, {const: 0, type: Count}]}
        - {op: test, eq: [sd.carryover, {const: true}]}
        - {op: test, eq: [sd.other_forms, {const: true}]}
        - {op: test, gt: [div.box2b, {const: 0}]}
        - {op: test, gt: [div.box2c, {const: 0}]}
        - {op: test, gt: [div.box2d, {const: 0}]}
    note: "Exception 1: no Schedule D if you have no capital losses, your only capital gains are Form 1099-DIV box 2a distributions, and no Form 1099-DIV shows boxes 2b, 2c or 2d (and no qualified opportunity fund deferral, which has no input here). A sale, a carryover loss, another-form item or a box 2b/2c/2d amount means you must file. Filing anyway with only distributions is optional; I treat it as not filed."
```
```
