# Transcription agreement — sd

Second transcription of `Schedule D — securities sales and supplied distribution subtotals` by an isolated model (spec 6.5), compared line by line with `forms/2025/sd.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-27 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 6995153b5da31c2c6dd56c90341fbf55f2c406f252bf69e7c7e4dc08912849ef |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 4e7b46c9c5f38165367ad1fd06c322f9968c8ba5731314780526bcf3a299d4ea |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 14f6c7571f90fea7fd4da5231e18ae13294ab3b969700f9e50a613b3212a083f |
| printed lines compared | 55 |
| agree / disagree / missing | 10 / 45 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | eb461181b39879c79d1c0b7761ca0cd9ade46fdb1531cdee3281053c348f6c41 |
| i1040sd | 2025; printed date 2025-12-11 | 10, 11, 12, 15 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040gi | 2025; printed date 2026-02-25 | 31, 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### sd.line18 — Line 18. 28% Rate Gain Worksheet result, or zero when line 17 is No (lines 18 through 21 s
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}
```

Second:

```json
{"const": 0}
```

Second transcription's note: The 28% Rate Gain Worksheet is not supplied in the interface. The line is zero when no special sale makes the worksheet necessary; it refuses when line 17 is true and any sale is special.

Ruling: interface gap; f1040sd p. 2, line 18: "If you are required to complete the 28% Rate Gain Worksheet (see instructions), enter the amount, if any, from line 7 of that worksheet"; i1040sd p. 11, Line 18: "complete the 28% Rate Gain Worksheet ... if either of the following applies for 2025. • You reported in Part II of Form 8949 a section 1202 exclusion ... • You reported in Part II of Form 8949 a collectibles gain or (loss)." The rule that a Form 1099-DIV box 2d amount also requires the worksheet is under Capital Gain Distributions on i1040sd p. 2, which the reviewer was not given (pages 10, 11, 12, 15). The candidate's constant 0 follows from the pages it had; the project's g28.line7 behind line 17 Yes is the BUG-0149 fix. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,519 of 1,779 comparisons agree; 121 project-unknown, 84 project-refuses, 55 value (by return: {"completed": {"value": 13}, "incomplete": {"project-unknown": 51, "value": 7}, "refused": {"project-refuses": 84, "project-unknown": 70, "value": 35}}). Every recorded value difference has a box 2d amount with line 17 Yes and no special sale (classm.f8889.1.deepseek box 2d $823, project $823; classm.g28.2 $400; classm.qdcg.3 $83; classm.sdtw.2 $927; classm.sdtw.5 $3,800; candidate $0). The 84 project-refuses are cited gates (sales.digital: classm.asset.2; div.bad_components: classm.dcprov.1, classm.f8606.1, classm.refund.1, classm.retirement.1; sales.bad_aggregate: classm.sc.3) and the 121 project-unknown are withheld screen answers or gate-set fixtures without 2024 figures on refused returns (classm.f8889.5, classm.asset.3, classm.carloan.3, UNK clcw.prior_sd15): scope. Project stands.

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

Ruling: model error; f1040sd p. 2, line 17: "Are lines 15 and 16 both gains? Yes. Go to line 18. No. Skip lines 18 through 21, and go to line 22." The candidate copies u1250.line18 on every return, so it shows an amount on line 19 when line 17 is No. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 689 of 1,779 comparisons agree; 1,022 candidate-unknown, 51 project-refuses, 9 value, 8 project-unknown (by return: {"completed": {"candidate-unknown": 413, "value": 1}, "incomplete": {"candidate-unknown": 261, "project-unknown": 2}, "refused": {"candidate-unknown": 348, "project-refuses": 51, "project-unknown": 6, "value": 8}}). The 9 value differences are line-17-No returns with a box 2b amount (generated 162, completed: line 15 −$50,859.91, box 2b $6,330.85, project $0, candidate $6,330.85; generated 188, 196, 201, 205, 223), a nonzero amount on a skipped line. The 1,022 candidate-unknown come from the candidate's unguarded line 14 read by u1250.line16 (ruled on line 14). The 51 project-refuses (sales.digital, sales.bad_aggregate) and 8 project-unknown (withheld sd.carryover) are scope. Project stands.

### sd.filing4952 — Are you filing Form 4952?
Status: **AGREE**

### sd.investment_election — Form 4952 line 4g (supplied subtotal; Form 4952 deferred to Stage 4)
Status: **AGREE**

### sd.filed — Schedule D required for entered sales, special distribution gains or a capital loss carryo
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sales", "field": "sales.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}], "test": "lt"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "lt"}, {"args": [{"line": "14"}, {"const": 0}], "test": "lt"}, {"args": [{"line": "6"}, {"const": 0}], "test": "lt"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"const": 0}, {"ref": "div.box2b"}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "div.box2c"}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "div.box2d"}], "test": "lt"}], "test": "any"}, {"args": [{"const": 0}, {"input": "sd.distributions"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"ref": "clcw.line13"}], "test": "lt"}, {"args": [{"const": 0}, {"ref": "clcw.line8"}], "test": "lt"}], "test": "any"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "sales", "field": "sales.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "any"}
```

Ruling: model error; i1040gi p. 31, Line 7a, Exception 1: "1. You have no capital losses, and your only capital gains are capital gain distributions from Form(s) 1099-DIV, box 2a ...; and 2. None of the Form(s) 1099-DIV ... have an amount in box 2b ..., box 2c ..., or box 2d"; i1040sd p. 10: "Otherwise, you don’t have any carryovers." The candidate tests clcw.line8 and clcw.line13 without the sd.carryover choice, so it needs the 2024 figures on every gate-No return. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 822 of 1,779 comparisons agree; 882 candidate-unknown, 40 project-refuses, 35 project-unknown (by return: {"completed": {"candidate-unknown": 390}, "incomplete": {"candidate-unknown": 206, "project-unknown": 11}, "refused": {"candidate-unknown": 286, "project-refuses": 40, "project-unknown": 24}}). No value differs. The 882 candidate-unknown are gate-No returns (classm.f2441.1.deepseek to .6, completed, UNK clcw.prior_sd7), 390 completed: an answer required that the source does not need. Its other tests (sales, box 2b/2c/2d with a distribution) agree with the project's sales count and line 18/19 tests wherever it computes. The 40 project-refuses (sd.other_forms, div.section1202) and 35 project-unknown (withheld sd.other_forms, sd.carryover, sd.distributions) are scope. Project stands.

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
{"alternatives": [{"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "eq"}, "then": {"from": {"const": 0}, "op": "subtract", "take": {"const": 0}}}, {"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "lt"}, "then": {"line": "16"}}, {"guard": {"args": [{"line": "16"}, {"const": 0}], "test": "lt"}, "then": {"line": "21"}}], "op": "choose"}
```

Ruling: representation; f1040sd p. 2, line 16: "If line 16 is zero, skip lines 17 through 21 below and enter -0- on Form 1040, 1040-SR, or 1040-NR, line 7a". The candidate's three branches (0 − 0 for zero, line 16 for a gain, line 21 for a loss) equal the project's two (line 16 for zero or a gain). Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 663 of 1,779 comparisons agree; 1,022 candidate-unknown, 86 project-refuses, 8 project-unknown (by return: {"completed": {"candidate-unknown": 413}, "incomplete": {"candidate-unknown": 261, "project-unknown": 2}, "refused": {"candidate-unknown": 348, "project-refuses": 86, "project-unknown": 6}}). No value differs. The 1,022 candidate-unknown are inherited from the candidate's unguarded lines 6 and 14 through line 16 (model error, ruled there), not from this expression; the 86 project-refuses and 8 project-unknown are cited gates and withheld answers on refused or incomplete returns: scope. Project stands.

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

Ruling: representation; i1040gi p. 38, Qualified Dividends and Capital Gain Tax Worksheet, line 3: "Enter the smaller of line 15 or line 16 of Schedule D. If either line 15 or line 16 is blank or a loss, enter -0-". min(max(15, 0), max(16, 0)) equals max(min(15, 16), 0) for all values. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 663 of 1,779 comparisons agree; 1,022 candidate-unknown, 86 project-refuses, 8 project-unknown (by return: {"completed": {"candidate-unknown": 413}, "incomplete": {"candidate-unknown": 261, "project-unknown": 2}, "refused": {"candidate-unknown": 348, "project-refuses": 86, "project-unknown": 6}}). No value differs; the 1,022 candidate-unknown are inherited from the candidate's unguarded lines 6 and 14 (ruled there); the refusals and withheld answers are scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1a: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums the column over box A or box G on the aggregate route; the project sums box A on the aggregate route behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1a: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums the column over box A or box G on the aggregate route; the project sums box A on the aggregate route behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1a: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums the column over box A or box G on the aggregate route; the project sums box A on the aggregate route behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1a: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums the column over box A or box G on the aggregate route; the project sums box A on the aggregate route behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1b: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked". The candidate sums the column over box A or box G (detail route); the project sums box A behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1b: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked". The candidate sums the column over box A or box G (detail route); the project sums box A behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1b: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked". The candidate sums the column over box A or box G (detail route); the project sums box A behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1b: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked". The candidate sums the column over box A or box G (detail route); the project sums box A behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 2: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked". The candidate sums the column over box B or box H (detail route); the project sums box B behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 2: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked". The candidate sums the column over box B or box H (detail route); the project sums box B behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 2: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked". The candidate sums the column over box B or box H (detail route); the project sums box B behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 2: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked". The candidate sums the column over box B or box H (detail route); the project sums box B behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 3: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked". The candidate sums the column over box C or box I (detail route); the project sums box C behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 3: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked". The candidate sums the column over box C or box I (detail route); the project sums box C behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 3: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked". The candidate sums the column over box C or box I (detail route); the project sums box C behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 3: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked". The candidate sums the column over box C or box I (detail route); the project sums box C behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8a: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums the column over box D or box J on the aggregate route; the project sums box D on the aggregate route behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8a: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums the column over box D or box J on the aggregate route; the project sums box D on the aggregate route behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8a: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums the column over box D or box J on the aggregate route; the project sums box D on the aggregate route behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8a: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums the column over box D or box J on the aggregate route; the project sums box D on the aggregate route behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8b: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked". The candidate sums the column over box D or box J (detail route); the project sums box D behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8b: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked". The candidate sums the column over box D or box J (detail route); the project sums box D behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8b: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked". The candidate sums the column over box D or box J (detail route); the project sums box D behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8b: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked". The candidate sums the column over box D or box J (detail route); the project sums box D behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 9: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked". The candidate sums the column over box E or box K (detail route); the project sums box E behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 9: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked". The candidate sums the column over box E or box K (detail route); the project sums box E behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 9: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked". The candidate sums the column over box E or box K (detail route); the project sums box E behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 9: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked". The candidate sums the column over box E or box K (detail route); the project sums box E behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 10: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked". The candidate sums the column over box F or box L (detail route); the project sums box F behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 10: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked". The candidate sums the column over box F or box L (detail route); the project sums box F behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 10: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked". The candidate sums the column over box F or box L (detail route); the project sums box F behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 10: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked". The candidate sums the column over box F or box L (detail route); the project sums box F behind sd.screen. Boxes G–L (digital assets on Form 1099-DA) are refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), the refusal propagates through sd.count to sd.screen, so the added boxes reach only refused returns; widening the filters is T-003. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,667 of 1,779 comparisons agree; 72 project-refuses, 40 project-unknown (by return: {"incomplete": {"project-unknown": 17}, "refused": {"project-refuses": 72, "project-unknown": 23}}); no value differs. The project-refuses are sd.count/sd.screen's cited screens (sd.other_forms, e.g. classm.f8889.4.deepseek, classm.clcw.1.deepseek, classm.f8959.1; sales.one gates sales.digital and sales.bad_aggregate, e.g. classm.asset.2, classm.sc.3), all on returns the full interview refuses; the project-unknown are partial records withholding sd.other_forms (the screen the interview asks before any Schedule D total) or fixtures that leave it unanswered on refused returns: scope. Project stands.

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

Ruling: representation; f1040sd p. 1, line 4: "Short-term gain from Form 6252 and short-term gain or (loss) from Forms 4684, 6781, and 8824". The candidate's 0 − 0 equals the project's 0, and the source forms are refused by sd.other_forms in both. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,779 of 1,779 comparisons agree; no difference (by return: {}). Algebraically equal. Project stands.

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

Ruling: representation; f1040sd p. 1, line 5: "Net short-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1". The candidate's 0 − 0 equals the project's 0, and the source forms are refused by sd.other_forms in both. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,779 of 1,779 comparisons agree; no difference (by return: {}). Algebraically equal. Project stands.

### 6 — Short-term capital loss carryover, from line 8 of the Capital Loss Carryover Worksheet (a
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sd.carryover"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sd.carryover"}], "test": "eq"}, "then": {"from": {"const": 0}, "op": "subtract", "take": {"ref": "clcw.line8"}}}], "op": "choose"}
```

Second:

```json
{"from": {"const": 0}, "op": "subtract", "take": {"ref": "clcw.line8"}}
```

Ruling: model error; f1040sd p. 1, line 6: "Enter the amount, if any, from line 8 of your Capital Loss Carryover Worksheet in the instructions"; i1040sd p. 10: "Use this worksheet to figure your capital loss carryovers from 2024 to 2025 if your 2024 Schedule D, line 21, is a loss ... Otherwise, you don’t have any carryovers." The candidate drops the sd.carryover choice, so it reads worksheet line 8 (and through it clcw.spouse_screen and the five 2024 figures) on every return, including the returns whose answer to "Did line 21 of your 2024 Schedule D show a loss?" is No, where the interview asks none of them; i1040sd p. 10: "Otherwise, you don’t have any carryovers." Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 662 of 1,779 comparisons agree; 1,081 candidate-unknown, 20 project-refuses, 16 project-unknown (by return: {"completed": {"candidate-unknown": 413}, "incomplete": {"candidate-unknown": 276, "project-unknown": 4}, "refused": {"candidate-unknown": 392, "project-refuses": 20, "project-unknown": 12}}). No value differs: where the 2024 figures are supplied the candidate's 0 − clcw.line8 is the project's. The 1,081 candidate-unknown are returns with the gate No (e.g. classm.f2441.1.deepseek to classm.f2441.6.deepseek, completed, sd.carryover false, UNK clcw.spouse_screen), 413 of them completed: an answer required that the source does not need. The 20 project-refuses (sd.other_forms) and 16 project-unknown (withheld sd.other_forms or sd.carryover) are scope. Project stands.

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

Ruling: representation; f1040sd p. 1, line 11: "Gain from Form 4797, Part I; long-term gain from Forms 2439 and 6252; and long-term gain or (loss) from Forms 4684, 6781, and 8824". The candidate's 0 − 0 equals the project's 0, and the source forms are refused by sd.other_forms in both. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,779 of 1,779 comparisons agree; no difference (by return: {}). Algebraically equal. Project stands.

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

Ruling: representation; f1040sd p. 1, line 12: "Net long-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1". The candidate's 0 − 0 equals the project's 0, and the source forms are refused by sd.other_forms in both. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,779 of 1,779 comparisons agree; no difference (by return: {}). Algebraically equal. Project stands.

### 14 — Long-term capital loss carryover, from line 13 of the Capital Loss Carryover Worksheet (a
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "sd.carryover"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "sd.carryover"}], "test": "eq"}, "then": {"from": {"const": 0}, "op": "subtract", "take": {"ref": "clcw.line13"}}}], "op": "choose"}
```

Second:

```json
{"from": {"const": 0}, "op": "subtract", "take": {"ref": "clcw.line13"}}
```

Ruling: model error; f1040sd p. 1, line 14: "Enter the amount, if any, from line 13 of your Capital Loss Carryover Worksheet in the instructions"; i1040sd p. 10: "Otherwise, you don’t have any carryovers." The candidate drops the sd.carryover choice and reads worksheet line 13 on every return, so it needs clcw.spouse_screen and the 2024 figures where the gate is No and the interview asks none of them. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 662 of 1,779 comparisons agree; 1,081 candidate-unknown, 20 project-refuses, 16 project-unknown (by return: {"completed": {"candidate-unknown": 413}, "incomplete": {"candidate-unknown": 276, "project-unknown": 4}, "refused": {"candidate-unknown": 392, "project-refuses": 20, "project-unknown": 12}}). No value differs; the 1,081 candidate-unknown are gate-No returns (classm.f2441.1.deepseek and others, 413 completed): an answer required that the source does not need. The 20 project-refuses (sd.other_forms) and 16 project-unknown are scope. Project stands.

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
{"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "eq"}, {"args": [{"ref": "f4952.line5"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line1"}, {"ref": "f4952.line4c"}], "test": "lt"}], "test": "all"}, {"args": [{"ref": "f4952.line3"}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "eq"}, {"args": [{"ref": "f4952.line5"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line1"}, {"ref": "f4952.line4c"}], "test": "lt"}], "test": "all"}, {"args": [{"ref": "f4952.line3"}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"const": 0}, {"const": 0}], "test": "eq"}, {"args": [{"ref": "u1250.line18"}, {"const": 0}], "test": "le"}], "test": "all"}
```

Ruling: interface gap; f1040sd p. 2, line 20: "Are lines 18 and 19 both zero or blank and you are not filing Form 4952?"; line 17: "No. Skip lines 18 through 21, and go to line 22." The candidate uses its constant line 18 (0) and u1250.line18 for line 19 with the project's Form 4952 test. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 758 of 1,779 comparisons agree; 945 candidate-unknown, 51 project-refuses, 20 value, 4 candidate-refuses, 1 project-unknown (by return: {"completed": {"candidate-unknown": 384, "value": 5}, "incomplete": {"candidate-unknown": 255}, "refused": {"candidate-refuses": 4, "candidate-unknown": 306, "project-refuses": 51, "project-unknown": 1, "value": 15}}). The recorded value differences are line-17-Yes returns with a box 2d amount, where the project's line 18 is positive and the candidate's 0 (classm.g28.2 and its deepseek twin, box 2d $400; generated 0, 78, 90, 100; project false, candidate true): they follow from line 18, whose box 2d rule is on i1040sd p. 2, not given (see sd.line18). The candidate's unguarded u1250.line18 can also make it false on a line-17-No return (inferred from generated 162 on line 19); line 20 is skipped there and, as a Boolean flow predicate, is exempt from the skipped-line rule, and no amount reads it on that path. The 945 candidate-unknown are inherited from its unguarded line 14 (ruled there). The 4 candidate-refuses (f4952.bad_election, f4952.alternative_allocation, f4952.unsupported, sb.unsupported; generated 51, 273, 284, 472) and 51 project-refuses (f4952.bad_election: classm.oi8z.1, classm.otjob.1, classm.eic.3; sales.digital; sales.bad_aggregate) are evaluation-order differences on refused returns, and the 1 project-unknown withholds sd.carryover: scope. Project stands.

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "16"}, {"const": 0}], "test": "lt"}, "then": {"of": [{"line": "16"}, {"param": "sd.loss_limit"}], "op": "larger_of"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "le"}, "then": {"from": {"const": 0}, "op": "subtract", "take": {"const": 0}}}, {"guard": {"args": [{"line": "16"}, {"const": 0}], "test": "lt"}, "then": {"of": [{"line": "16"}, {"param": "sd.loss_limit"}], "op": "larger_of"}}], "op": "choose"}
```

Ruling: representation; f1040sd p. 2, line 21: "If line 16 is a loss, enter here and on Form 1040, 1040-SR, or 1040-NR, line 7a, the smaller of: • The loss on line 16; or • ($3,000), or if married filing separately, ($1,500)". The candidate's 0 − 0 in the not-a-loss branch equals the project's 0; the loss branch is identical. Triage executable-triage-v2 (triage/sd.deepseek.json; 1,159 fixtures, 500 generated returns seed 20261026, 120 partial records): 663 of 1,779 comparisons agree; 1,022 candidate-unknown, 86 project-refuses, 8 project-unknown (by return: {"completed": {"candidate-unknown": 413}, "incomplete": {"candidate-unknown": 261, "project-unknown": 2}, "refused": {"candidate-unknown": 348, "project-refuses": 86, "project-unknown": 6}}). No value differs; the 1,022 candidate-unknown are inherited from the candidate's unguarded lines 6 and 14 through line 16 (ruled there); the 86 project-refuses and 8 project-unknown are scope. Project stands.

### 22 — Do you have qualified dividends?
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sd.line18 | sd.h_line18_gate | sd.h_line18_gate |
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
| 20 | sd.h_line18_gate | sd.h_line18_gate |
| 21 | clcw.spouse_screen, sd.other_forms | - |

## Raw second transcription

```yaml
lines:
  - id: sd.line1a.d
    printed: "1a(d)"
    label: "Proceeds (sales price)"
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
    label: "Cost (or other basis)"
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
    label: "Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
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
    label: "Gain or (loss) Subtract column (e) from column (d) and combine the result with column (g)"
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
    label: "Proceeds (sales price)"
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
    label: "Cost (or other basis)"
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
    label: "Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
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
    label: "Gain or (loss) Subtract column (e) from column (d) and combine the result with column (g)"
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
    label: "Proceeds (sales price)"
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
    label: "Cost (or other basis)"
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
    label: "Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
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
    label: "Gain or (loss) Subtract column (e) from column (d) and combine the result with column (g)"
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
    label: "Proceeds (sales price)"
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
    label: "Cost (or other basis)"
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
    label: "Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
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
    label: "Gain or (loss) Subtract column (e) from column (d) and combine the result with column (g)"
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
    label: "Proceeds (sales price)"
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
    label: "Cost (or other basis)"
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
    label: "Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
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
    label: "Gain or (loss) Subtract column (e) from column (d) and combine the result with column (g)"
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
    label: "Proceeds (sales price)"
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
    label: "Cost (or other basis)"
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
    label: "Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
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
    label: "Gain or (loss) Subtract column (e) from column (d) and combine the result with column (g)"
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
    label: "Proceeds (sales price)"
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
    label: "Cost (or other basis)"
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
    label: "Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
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
    label: "Gain or (loss) Subtract column (e) from column (d) and combine the result with column (g)"
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
    label: "Proceeds (sales price)"
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
    label: "Cost (or other basis)"
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
    label: "Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
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
    label: "Gain or (loss) Subtract column (e) from column (d) and combine the result with column (g)"
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
    expr: {op: subtract, from: sd.zero, take: clcw.line8}
    refuses: [clcw.spouse_screen]
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
    expr: {op: subtract, from: sd.zero, take: clcw.line13}
    refuses: [clcw.spouse_screen]
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
    label: "If line 16 is a loss, enter here and on Form 1040, 1040-SR, or 1040-NR, line 7a, the smaller of: The loss on line 16; or ($3,000), or if married filing separately, ($1,500)"
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            lt: [sd.line16, {const: 0}]
          then: sd.h_line21_loss
        - guard:
            op: test
            ge: [sd.line16, {const: 0}]
          then: sd.h_zero_dollars
  - id: sd.line22
    printed: "22"
    label: "Do you have qualified dividends on Form 1040, 1040-SR, or 1040-NR, line 3a?"
    type: Bool
    expr:
      op: test
      gt: [f1040.line3a, {const: 0}]
  - id: sd.line18
    printed: "(helper)"
    label: "If you are required to complete the 28% Rate Gain Worksheet (see instructions), enter the amount, if any, from line 7 of that worksheet"
    type: NonNegDollars
    expr: {op: copy, from: sd.zero}
    refuses: [sd.h_line18_gate]
    note: "The 28% Rate Gain Worksheet is not supplied in the interface. The line is zero when no special sale makes the worksheet necessary; it refuses when line 17 is true and any sale is special."
  - id: sd.line19
    printed: "(helper)"
    label: "If you are required to complete the Unrecaptured Section 1250 Gain Worksheet (see instructions), enter the amount, if any, from line 18 of that worksheet"
    type: NonNegDollars
    expr: {op: copy, from: u1250.line18}
  - id: sd.filing4952
    printed: "(helper)"
    label: "Filing Form 4952"
    type: Bool
    expr: {op: copy, from: f4952.required}
  - id: sd.investment_election
    printed: "(helper)"
    label: "Amount from Form 4952 line 4g elected into investment income"
    type: NonNegDollars
    expr: {op: copy, from: f4952.line4g}
  - id: sd.filed
    printed: "(helper)"
    label: "Schedule D is filed"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          eq: [sd.h_has_sales, {const: true}]
        - op: test
          eq: [sd.h_has_dist_special, {const: true}]
        - op: test
          eq: [sd.h_has_carryover, {const: true}]
  - id: sd.zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: sd.has_loss
    printed: "(helper)"
    label: "Line 16 is a loss"
    type: Bool
    expr:
      op: test
      lt: [sd.line16, {const: 0}]
  - id: sd.to1040
    printed: "(helper)"
    label: "Amount to enter on Form 1040, line 7a"
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
          then: sd.h_zero_dollars
  - id: sd.net_gain
    printed: "(helper)"
    label: "Net capital gain for the Qualified Dividends and Capital Gain Tax Worksheet"
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [sd.h_line15_pos, sd.h_line16_pos]
  - id: sd.h_zero_dollars
    printed: "(helper)"
    label: "Zero dollars"
    type: Dollars
    expr: {op: subtract, from: sd.zero, take: sd.zero}
  - id: sd.h_loss_limit
    printed: "(helper)"
    label: "Capital loss limit by filing status"
    type: Dollars
    expr: {op: param, ref: sd.loss_limit}
  - id: sd.h_line21_loss
    printed: "(helper)"
    label: "Smaller capital loss limitation, as a signed amount"
    type: Dollars
    expr:
      op: larger_of
      of: [sd.line16, sd.h_loss_limit]
  - id: sd.h_sales_count
    printed: "(helper)"
    label: "Number of sales entries"
    type: Count
    expr:
      op: sum_over
      collection: sales
      field: sales.one
  - id: sd.h_has_sales
    printed: "(helper)"
    label: "Any sales entry"
    type: Bool
    expr:
      op: test
      gt: [sd.h_sales_count, {const: 0, type: Count}]
  - id: sd.h_has_dist_special
    printed: "(helper)"
    label: "Capital gain distributions with a 28% or 1250 or 1202 amount"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          gt: [sd.distributions, {const: 0}]
        - op: test
          any:
            - op: test
              gt: [div.box2b, {const: 0}]
            - op: test
              gt: [div.box2c, {const: 0}]
            - op: test
              gt: [div.box2d, {const: 0}]
  - id: sd.h_has_carryover
    printed: "(helper)"
    label: "Any capital loss carryover"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          gt: [clcw.line8, {const: 0}]
        - op: test
          gt: [clcw.line13, {const: 0}]
  - id: sd.h_special_count
    printed: "(helper)"
    label: "Number of special sales entries"
    type: Count
    expr:
      op: sum_over
      collection: sales
      field: sales.one
      where:
        op: test
        eq: [sales.special, {const: true}]
  - id: sd.h_any_special
    printed: "(helper)"
    label: "Any special sale"
    type: Bool
    expr:
      op: test
      gt: [sd.h_special_count, {const: 0, type: Count}]
  - id: sd.h_line18_gate
    printed: "(helper)"
    label: "Line 18 needs the 28% Rate Gain Worksheet"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          eq: [sd.line17, {const: true}]
        - op: test
          eq: [sd.h_any_special, {const: true}]
  - id: sd.h_line15_pos
    printed: "(helper)"
    label: "Line 15 if positive, otherwise zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sd.line15, take: {const: 0}}
  - id: sd.h_line16_pos
    printed: "(helper)"
    label: "Line 16 if positive, otherwise zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sd.line16, take: {const: 0}}
```
