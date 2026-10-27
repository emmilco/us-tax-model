# Transcription agreement — sd

Second transcription of `Schedule D — securities sales and supplied distribution subtotals` by an isolated model (spec 6.5), compared line by line with `forms/2025/sd.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-26 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | a21c9c82a88ee547363f18049fb3a40b2115562a77c41976ef430cf72810d8b7 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 8011e81c8830bf928db25fad10220c8aa49193db41c2aeac336d669031e9a867 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 970194c9c6b868f34407d059bec48ad22672e5fe0cd1bbf4cd15d395f038b5c7 |
| printed lines compared | 54 |
| agree / disagree / missing | 14 / 40 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sd | 2025; created 2025-10-06 | 1, 2 | whole document | 221151530f7cd599e8ad00bc3e1ba62d6b7ff34e402c336f4ae58d698c9f5187 | - | eb461181b39879c79d1c0b7761ca0cd9ade46fdb1531cdee3281053c348f6c41 |
| i1040sd | 2025; printed date 2025-12-11 | 11, 12, 15 | cited pages | 145b3d02ba6ce4257939dfbd8f99d519875224cb4ceb4237a1aa24ed862360f1 | 11, 12 | 0120691acc1fa8bf63941916a3b9423db8fba10d67f098a580fdc518c5fd08ec |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

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

Second transcription's note: This is printed line 18; it is marked (helper) because it is supplied as a result interface. The supplied instructions require the 28% Rate Gain Worksheet only for a section 1202 exclusion or a collectibles gain or (loss) reported in Part II of Form 8949. Those sales are outside this slice: they are screened per entry by sales.special, and gains from other forms by sd.other_forms. The worksheet is therefore never required here and the line is zero. The supplied text does not make Form 1099-DIV box 2d a trigger on its own (that rule would sit in the omitted 'Capital Gain Distributions' instructions), so box 2d is not encoded. This is a limitation.

Ruling: interface gap; f1040sd p. 2, line 18: "If you are required to complete the 28% Rate Gain Worksheet (see instructions), enter the amount, if any, from line 7 of that worksheet". The instruction that makes a Form 1099-DIV box 2d amount part of that worksheet is i1040sd p. 2, Capital Gain Distributions: "If there is an amount in box 2d, include that amount on line 4 of the 28% Rate Gain Worksheet in these instructions if you complete line 18 of Schedule D", a page the reviewer was not given (i1040sd pp. 11, 12, 15). The given p. 11 lists only Form 8949 Part II triggers ("complete the 28% Rate Gain Worksheet ... if either of the following applies"), although the worksheet's own line 4 names "Form 1099-DIV, box 2d"; the candidate enters 0 and its note says the box 2d rule "would sit in the omitted 'Capital Gain Distributions' instructions". Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,390 of 1,714 agree; all 52 value differences have line 17 Yes and g28.line7 positive from box 2d (project, candidate $0): classm.f8889.1.deepseek $823 and classm.tcw.1 $400 (completed returns), stage4.sdtw.special_rates $20,000, generated 90 $2,546.98. None has line 17 No: on those returns both sides now give 0, so the BUG-0149 fix agrees with this candidate. The 115 project-refuses are cited gates read through g28 (sales.one screens 50, sd.other_forms 18, sd.carryover 14, div.bad_components 16, div.section1202 6, div.unsupported 5, div.amt 4, div.bad_special 2; classm.asset.2, classm.carloan.3) and the 157 project-unknown withhold screen answers asked before any Schedule D line (sd.other_forms 77, sd.distributions 40, sd.carryover 39, div.box2c 1), which the constant candidate never reads: scope. Project stands, supported by i1040sd p. 2 and worksheet line 4; a fresh review needs p. 2.

### sd.line19 — Line 19. Unrecaptured Section 1250 Gain Worksheet result, or zero when line 17 is No (line
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"line": "17"}], "test": "eq"}, {"args": [{"const": 0}, {"ref": "div.box2b"}], "test": "lt"}], "test": "all"}, "then": {"ref": "u1250.line18"}}, {"guard": {"args": [{"args": [{"ref": "div.box2b"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"line": "17"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: This is printed line 19; it is marked (helper) because it is supplied as a result interface. Of the worksheet triggers in the supplied text, only the Form 1099-DIV report of unrecaptured section 1250 gain (box 2b) is in scope. Section 1250 property sales, installment sales and Schedule K-1 amounts are screened by sales.special and sd.other_forms. The worksheet applies only if line 17 is Yes.

Ruling: scope; f1040sd p. 2, line 17: "No. Skip lines 18 through 21, and go to line 22"; i1040sd p. 11, Line 19: "If you checked “Yes” on line 17, complete the Unrecaptured Section 1250 Gain Worksheet ... if any of the following apply", p. 12: "You received a Form 1099-DIV ... that reports “unrecaptured section 1250 gain.”" The candidate takes u1250.line18 when line 17 is Yes and box 2b is positive, and 0 otherwise; within scope the other triggers (section 1250 sales, installment sales, Schedule K-1 amounts) are refused by sales.special and sd.other_forms, so u1250.line18 is positive only from box 2b and the values match. Its line 17 guard is the BUG-0149 fix. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,528 of 1,714 agree, no value differs; the 79 project-refuses are cited gates read through u1250 (sales.one screens 50, div.bad_components 14, div.section1202 6, div.unsupported 4, div.amt 4, div.bad_special 1; classm.asset.2, classm.carloan.3) and the 107 project-unknown withhold sd.distributions (36), sd.other_forms (35), sd.carryover (35) or div.box2c (1), answers the interview asks before any Schedule D line, which the candidate skips when box 2b is zero. Project stands.

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
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "eq"}, {"args": [{"ref": "f4952.line5"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line1"}, {"ref": "f4952.line4c"}], "test": "lt"}], "test": "all"}, {"args": [{"ref": "f4952.line1"}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"ref": "f4952.line4c"}, {"ref": "f4952.line1"}], "test": "le"}, {"args": [{"const": 0}, {"ref": "f4952.line5"}], "test": "lt"}, {"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0}, {"ref": "f4952.line1"}], "test": "lt"}], "test": "all"}, {"args": [{"const": 0}, {"ref": "f4952.line4g"}], "test": "lt"}], "test": "any"}, "then": {"ref": "f4952.line4g"}}], "op": "choose"}
```

Second transcription's note: The Schedule D Tax Worksheet applies 'if you file Form 4952 and you have an amount on line 4g', and its line 3 reads Form 4952 line 4g. This reads the interface as that amount when Form 4952 is filed, and zero otherwise.

Ruling: scope; i1040sd p. 15, Schedule D Tax Worksheet: complete it "if you file Form 4952 and you have an amount on line 4g", line 3: "Enter the amount from Form 4952 (used to figure investment interest expense deduction), line 4g". The candidate yields f4952.line4g when Form 4952 is filed or line 4g is positive and 0 otherwise; the project's f4952.line4g is the election behind its cited gates and is 0 when no election is made, so both give line 4g whenever both compute. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,596 of 1,714 agree and no value differs. The 67 project-refuses are f4952.election's gates and the Schedule D and Form 1099-DIV gates its check reads through lines 4b and 4e (sales.one screens 45, div.bad_components 10, div.section1202 4, div.amt 3, div.unsupported 3, div.bad_special 2; classm.asset.2; classm.f8606.1, refusal against the candidate's $2,491); the 34 project-unknown withhold sd.other_forms, sd.carryover and sd.distributions (11 each) or div.box2c (1). The 17 candidate-refuses (sb.unsupported 6, sb.fbar_required 4, sb.line8 4, sb.form8938 3; classm.carloan.1, classm.otjob.2, generated 11) come from its Form 4952 filing test, which reads f4952.line4c and so Schedule B, where the project refuses the same returns. The text names no condition the project leaves unscreened. Project stands.

### sd.filed — Schedule D required for entered sales or special distribution gains
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": 0, "type": "Count"}, {"collection": "sales", "field": "sales.one", "op": "sum_over", "where": null}], "test": "lt"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "g28.line7"}}], "op": "choose"}], "test": "lt"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": false}, {"line": "17"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"line": "17"}], "test": "eq"}, "then": {"ref": "u1250.line18"}}], "op": "choose"}], "test": "lt"}], "test": "any"}
```

Second:

```json
{"args": [{"args": [{"const": true}, {"input": "sd.carryover"}], "test": "eq"}, {"args": [{"const": true}, {"input": "sd.other_forms"}], "test": "eq"}, {"args": [{"const": 0, "type": "Count"}, {"collection": "sales", "field": "sales.one", "op": "sum_over", "where": null}], "test": "lt"}], "test": "any"}
```

Second transcription's note: The supplied text does not state when Schedule D must be filed. It only implies, through the Form 1040 line 7b box, that some filers with capital gain distributions need not file it. The reading chosen: Schedule D is filed when there is any sale, a capital loss carryover, or an amount from another form or a Schedule K-1. Capital gain distributions alone do not make it filed.

Ruling: interface gap; the rule that decides when Schedule D is required is i1040gi p. 31, Line 7a, Exception 1: "You don't have to file Form 8949 or Schedule D if ... 1. You have no capital losses, and your only capital gains are capital gain distributions from Form(s) 1099-DIV, box 2a ...; and 2. None of the Form(s) 1099-DIV ... have an amount in box 2b (unrecaptured section 1250 gain), box 2c (section 1202 gain), or box 2d (collectibles (28%) gain)." That page was not given (i1040gi p. 38 only), and the candidate's note says "The supplied text does not state when Schedule D must be filed"; it treats capital gain distributions as never requiring Schedule D, which the given p. 38 permits ("If you don’t have to file Schedule D and you received capital gain distributions, be sure you checked the box on Form 1040 or 1040-SR, line 7b") but which p. 31 contradicts for boxes 2b and 2d. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,556 of 1,714 agree; all 45 value differences are returns without sales whose sd.line18 or sd.line19 is positive (box 2d or 2b; project true, candidate false): classm.f8889.1.deepseek and classm.f8889.1 (completed), classm.sdtw.3, classm.tcw.12, stage4.sdtw.special_rates, generated 35, 150 and 164 (completed). The source supports the project. The 52 project-refuses are sd.count's screens sd.other_forms (17) and sd.carryover (13), where the candidate answers true, and Form 1099-DIV gates (div.bad_components 9, div.section1202 4, div.unsupported 4, div.amt 3, div.bad_special 2): scope. The 61 project-unknown withhold sd.other_forms (21), sd.carryover (21), sd.distributions (18) or div.box2c (1): scope. After BUG-0149, sd.filed reads lines 18 and 19 that are zero when line 17 is No; with no sales, lines 15 and 16 equal line 13 (box 2a), which div.bad_special keeps at least as large as box 2b or 2d, so line 17 is Yes whenever those boxes are positive and the fix changes no sd.filed value (no witness has line 17 No). Project stands; a fresh review needs i1040gi p. 31.

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
{"alternatives": [{"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": 0}, {"line": "16"}], "test": "lt"}, "then": {"line": "16"}}, {"guard": {"args": [{"line": "16"}, {"const": 0}], "test": "lt"}, "then": {"line": "21"}}], "op": "choose"}
```

Second transcription's note: From the line 16 instructions: if line 16 is a gain, enter it on line 7a. If it is a loss, enter line 21. If it is zero, enter -0-.

Ruling: scope; f1040sd p. 2, line 16: "If line 16 is zero, skip lines 17 through 21 below and enter -0- on Form 1040, 1040-SR, or 1040-NR, line 7a." The candidate's extra zero branch equals line 16 when line 16 is zero, so both enter line 16 for a gain or zero and line 21 for a loss. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,630 of 1,714 agree, no value differs; the 83 project-refuses are the cited Schedule D and Form 1099-DIV gates reached through lines 16 and 21 (sales.one screens 50, div.bad_components 16, div.section1202 6, div.unsupported 5, div.amt 4, div.bad_special 2; classm.asset.2, a box J sale, where the unscreened candidate gives $6,847) and the 1 project-unknown (stage16.cleanup.f8959_line16_se_refused) withholds the div.box2c screen. Project stands.

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

Second transcription's note: Line 1a holds basis-reported short-term transactions with no adjustments that are not reported on Form 8949. These are short-term entries in box A (Form 1099-B) or box G (Form 1099-DA) that the filer routes to the aggregate totals. If the filer reports them on Form 8949 instead (route detail), they go on line 1b and this line stays blank.

Ruling: scope; f1040sd p. 1, line 1a: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums column (d) proceeds over box A or box G on the aggregate route; the project sums box A on the aggregate route behind sd.screen. Box G (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1a: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums column (e) basis over box A or box G on the aggregate route; the project sums box A on the aggregate route behind sd.screen. Box G (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

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

Second transcription's note: Line 1a covers only transactions with no adjustments, so this total should be zero. It is summed rather than fixed at zero so that column (h) stays consistent with columns (d), (e) and (g).

Ruling: scope; f1040sd p. 1, line 1a: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums column (g) adjustments over box A or box G on the aggregate route; the project sums box A on the aggregate route behind sd.screen. Box G (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

### 1a(h) — Line 1a, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "A"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"of": [{"line": "1a(g)"}, {"from": {"line": "1a(d)"}, "op": "subtract", "take": {"line": "1a(e)"}}], "op": "sum"}
```

Ruling: scope; f1040sd p. 1, line 1a: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate figures column (h) gain or loss as columns (d) minus (e) plus (g) of its own line 1a totals instead of summing sales.h; sales.h is per entry proceeds less basis plus column (g) (i8949 p. 11, column (h)), so the two agree wherever the column filters agree, and its column filters add box G. Box G (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1b: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked". The candidate sums column (d) proceeds over box A or box G on the detail route; the project sums box A on the detail route behind sd.screen. Box G (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1b: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked". The candidate sums column (e) basis over box A or box G on the detail route; the project sums box A on the detail route behind sd.screen. Box G (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1b: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked". The candidate sums column (g) adjustments over box A or box G on the detail route; the project sums box A on the detail route behind sd.screen. Box G (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 1b: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked". The candidate figures column (h) gain or loss as columns (d) minus (e) plus (g) of its own line 1b totals instead of summing sales.h; sales.h is per entry proceeds less basis plus column (g) (i8949 p. 11, column (h)), so the two agree wherever the column filters agree, and its column filters add box G. Box G (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

### 2(d) — Line 2, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "H"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope; f1040sd p. 1, line 2: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked". The candidate sums column (d) proceeds over box B or box H without the detail-route test; the project sums box B on the detail route behind sd.screen. Box H (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. A box B entry on the aggregate route is refused by sales.bad_aggregate (cited i1040sd p. 10, lines 1a and 8a; p. 11, Example 2: "Don’t report this transaction on line 1a or line 8a"), so dropping the route test reaches only refused entries. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

### 2(e) — Line 2, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "H"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope; f1040sd p. 1, line 2: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked". The candidate sums column (e) basis over box B or box H without the detail-route test; the project sums box B on the detail route behind sd.screen. Box H (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. A box B entry on the aggregate route is refused by sales.bad_aggregate (cited i1040sd p. 10, lines 1a and 8a; p. 11, Example 2: "Don’t report this transaction on line 1a or line 8a"), so dropping the route test reaches only refused entries. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

### 2(g) — Line 2, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "B"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "H"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope; f1040sd p. 1, line 2: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked". The candidate sums column (g) adjustments over box B or box H without the detail-route test; the project sums box B on the detail route behind sd.screen. Box H (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. A box B entry on the aggregate route is refused by sales.bad_aggregate (cited i1040sd p. 10, lines 1a and 8a; p. 11, Example 2: "Don’t report this transaction on line 1a or line 8a"), so dropping the route test reaches only refused entries. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 2: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked". The candidate figures column (h) gain or loss as columns (d) minus (e) plus (g) of its own line 2 totals instead of summing sales.h; sales.h is per entry proceeds less basis plus column (g) (i8949 p. 11, column (h)), so the two agree wherever the column filters agree, and its column filters add box H and drop the detail-route test. Box H (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. A box B entry on the aggregate route is refused by sales.bad_aggregate (cited i1040sd p. 10, lines 1a and 8a; p. 11, Example 2: "Don’t report this transaction on line 1a or line 8a"), so dropping the route test reaches only refused entries. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

### 3(d) — Line 3, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "I"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope; f1040sd p. 1, line 3: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked". The candidate sums column (d) proceeds over box C or box I without the detail-route test; the project sums box C on the detail route behind sd.screen. Box I (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. A box C entry on the aggregate route is refused by sales.bad_aggregate (cited i1040sd p. 10, lines 1a and 8a; p. 11, Example 2: "Don’t report this transaction on line 1a or line 8a"), so dropping the route test reaches only refused entries. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

### 3(e) — Line 3, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "I"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope; f1040sd p. 1, line 3: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked". The candidate sums column (e) basis over box C or box I without the detail-route test; the project sums box C on the detail route behind sd.screen. Box I (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. A box C entry on the aggregate route is refused by sales.bad_aggregate (cited i1040sd p. 10, lines 1a and 8a; p. 11, Example 2: "Don’t report this transaction on line 1a or line 8a"), so dropping the route test reaches only refused entries. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

### 3(g) — Line 3, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "C"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "I"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope; f1040sd p. 1, line 3: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked". The candidate sums column (g) adjustments over box C or box I without the detail-route test; the project sums box C on the detail route behind sd.screen. Box I (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. A box C entry on the aggregate route is refused by sales.bad_aggregate (cited i1040sd p. 10, lines 1a and 8a; p. 11, Example 2: "Don’t report this transaction on line 1a or line 8a"), so dropping the route test reaches only refused entries. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 3: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked". The candidate figures column (h) gain or loss as columns (d) minus (e) plus (g) of its own line 3 totals instead of summing sales.h; sales.h is per entry proceeds less basis plus column (g) (i8949 p. 11, column (h)), so the two agree wherever the column filters agree, and its column filters add box I and drop the detail-route test. Box I (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. A box C entry on the aggregate route is refused by sales.bad_aggregate (cited i1040sd p. 10, lines 1a and 8a; p. 11, Example 2: "Don’t report this transaction on line 1a or line 8a"), so dropping the route test reaches only refused entries. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

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

Second transcription's note: Long-term counterpart of line 1a. It holds box D (Form 1099-B) and box J (Form 1099-DA) entries that the filer routes to the aggregate totals.

Ruling: scope; f1040sd p. 1, line 8a: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums column (d) proceeds over box D or box J on the aggregate route; the project sums box D on the aggregate route behind sd.screen. Box J (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8a: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums column (e) basis over box D or box J on the aggregate route; the project sums box D on the aggregate route behind sd.screen. Box J (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

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

Second transcription's note: Line 8a covers only transactions with no adjustments, so this total should be zero. It is summed rather than fixed at zero so that column (h) stays consistent.

Ruling: scope; f1040sd p. 1, line 8a: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate sums column (g) adjustments over box D or box J on the aggregate route; the project sums box D on the aggregate route behind sd.screen. Box J (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

### 8a(h) — Line 8a, column (h) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.h", "op": "sum_over", "where": {"args": [{"args": [{"const": "D"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "aggregate"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"of": [{"line": "8a(g)"}, {"from": {"line": "8a(d)"}, "op": "subtract", "take": {"line": "8a(e)"}}], "op": "sum"}
```

Ruling: scope; f1040sd p. 1, line 8a: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments". The candidate figures column (h) gain or loss as columns (d) minus (e) plus (g) of its own line 8a totals instead of summing sales.h; sales.h is per entry proceeds less basis plus column (g) (i8949 p. 11, column (h)), so the two agree wherever the column filters agree, and its column filters add box J. Box J (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8b: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked". The candidate sums column (d) proceeds over box D or box J on the detail route; the project sums box D on the detail route behind sd.screen. Box J (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8b: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked". The candidate sums column (e) basis over box D or box J on the detail route; the project sums box D on the detail route behind sd.screen. Box J (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8b: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked". The candidate sums column (g) adjustments over box D or box J on the detail route; the project sums box D on the detail route behind sd.screen. Box J (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 8b: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked". The candidate figures column (h) gain or loss as columns (d) minus (e) plus (g) of its own line 8b totals instead of summing sales.h; sales.h is per entry proceeds less basis plus column (g) (i8949 p. 11, column (h)), so the two agree wherever the column filters agree, and its column filters add box J. Box J (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

### 9(d) — Line 9, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "K"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope; f1040sd p. 1, line 9: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked". The candidate sums column (d) proceeds over box E or box K without the detail-route test; the project sums box E on the detail route behind sd.screen. Box K (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. A box E entry on the aggregate route is refused by sales.bad_aggregate (cited i1040sd p. 10, lines 1a and 8a; p. 11, Example 2: "Don’t report this transaction on line 1a or line 8a"), so dropping the route test reaches only refused entries. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

### 9(e) — Line 9, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "K"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope; f1040sd p. 1, line 9: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked". The candidate sums column (e) basis over box E or box K without the detail-route test; the project sums box E on the detail route behind sd.screen. Box K (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. A box E entry on the aggregate route is refused by sales.bad_aggregate (cited i1040sd p. 10, lines 1a and 8a; p. 11, Example 2: "Don’t report this transaction on line 1a or line 8a"), so dropping the route test reaches only refused entries. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

### 9(g) — Line 9, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "E"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "K"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope; f1040sd p. 1, line 9: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked". The candidate sums column (g) adjustments over box E or box K without the detail-route test; the project sums box E on the detail route behind sd.screen. Box K (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. A box E entry on the aggregate route is refused by sales.bad_aggregate (cited i1040sd p. 10, lines 1a and 8a; p. 11, Example 2: "Don’t report this transaction on line 1a or line 8a"), so dropping the route test reaches only refused entries. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 9: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked". The candidate figures column (h) gain or loss as columns (d) minus (e) plus (g) of its own line 9 totals instead of summing sales.h; sales.h is per entry proceeds less basis plus column (g) (i8949 p. 11, column (h)), so the two agree wherever the column filters agree, and its column filters add box K and drop the detail-route test. Box K (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. A box E entry on the aggregate route is refused by sales.bad_aggregate (cited i1040sd p. 10, lines 1a and 8a; p. 11, Example 2: "Don’t report this transaction on line 1a or line 8a"), so dropping the route test reaches only refused entries. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

### 10(d) — Line 10, column (d) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.proceeds", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "L"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope; f1040sd p. 1, line 10: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked". The candidate sums column (d) proceeds over box F or box L without the detail-route test; the project sums box F on the detail route behind sd.screen. Box L (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. A box F entry on the aggregate route is refused by sales.bad_aggregate (cited i1040sd p. 10, lines 1a and 8a; p. 11, Example 2: "Don’t report this transaction on line 1a or line 8a"), so dropping the route test reaches only refused entries. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

### 10(e) — Line 10, column (e) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.e", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "L"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope; f1040sd p. 1, line 10: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked". The candidate sums column (e) basis over box F or box L without the detail-route test; the project sums box F on the detail route behind sd.screen. Box L (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. A box F entry on the aggregate route is refused by sales.bad_aggregate (cited i1040sd p. 10, lines 1a and 8a; p. 11, Example 2: "Don’t report this transaction on line 1a or line 8a"), so dropping the route test reaches only refused entries. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

### 10(g) — Line 10, column (g) totals
Status: **DISAGREE**

Project:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "detail"}, {"ref": "sales.route"}], "test": "eq"}], "test": "all"}}
```

Second:

```json
{"collection": "sales", "field": "sales.g", "op": "sum_over", "where": {"args": [{"args": [{"const": "F"}, {"ref": "sales.box"}], "test": "eq"}, {"args": [{"const": "L"}, {"ref": "sales.box"}], "test": "eq"}], "test": "any"}}
```

Ruling: scope; f1040sd p. 1, line 10: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked". The candidate sums column (g) adjustments over box F or box L without the detail-route test; the project sums box F on the detail route behind sd.screen. Box L (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. A box F entry on the aggregate route is refused by sales.bad_aggregate (cited i1040sd p. 10, lines 1a and 8a; p. 11, Example 2: "Don’t report this transaction on line 1a or line 8a"), so dropping the route test reaches only refused entries. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

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

Ruling: scope; f1040sd p. 1, line 10: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked". The candidate figures column (h) gain or loss as columns (d) minus (e) plus (g) of its own line 10 totals instead of summing sales.h; sales.h is per entry proceeds less basis plus column (g) (i8949 p. 11, column (h)), so the two agree wherever the column filters agree, and its column filters add box L and drop the detail-route test. Box L (digital assets on Form 1099-DA) is refused at the transaction: sales.one refuses when sales.digital is true (f8949 Parts I and II, boxes G–L), so the added box reaches only refused returns; widening the filter is T-003. A box F entry on the aggregate route is refused by sales.bad_aggregate (cited i1040sd p. 10, lines 1a and 8a; p. 11, Example 2: "Don’t report this transaction on line 1a or line 8a"), so dropping the route test reaches only refused entries. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,552 of 1,714 comparisons agree and no value differs; the 82 project-refuses are sd.count's cited screens (sales.one: sales.digital 28, sales.bad_aggregate 12, sales.bad_code 8, sales.special 2; sd.other_forms 18; sd.carryover 14; e.g. classm.asset.2, a box J sale; classm.asset.3, carryover, where the candidate's unscreened total differs), and the 80 project-unknown are partial records withholding sd.other_forms or sd.carryover (40 each), screen answers the interview asks before any Schedule D total: scope. Project stands.

### 4 — Line 4: zero only after unsupported source/carryover screening
Status: **AGREE**

### 5 — Line 5: zero only after unsupported source/carryover screening
Status: **AGREE**

### 6 — Line 6: zero only after unsupported source/carryover screening
Status: **AGREE**

### 11 — Line 11: zero only after unsupported source/carryover screening
Status: **AGREE**

### 12 — Line 12: zero only after unsupported source/carryover screening
Status: **AGREE**

### 14 — Line 14: zero only after unsupported source/carryover screening
Status: **AGREE**

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

Second transcription's note: Line 6 is a parenthesized (negative) amount held as a positive magnitude, so 'combine' subtracts it.

Ruling: scope; f1040sd p. 1, line 7: "Combine lines 1a through 6 in column (h)." Line 6 is the short-term carryover, printed in parentheses; the candidate subtracts it, the project adds it. Carryovers are refused (sd.carryover on line 6 and sd.count), so line 6 is zero within scope; the sign convention is open as T-004. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,664 of 1,714 agree and every in-scope comparison agrees; the 50 project-refuses are sales.one's cited gates (sales.digital 28, e.g. sales.refuse.digital.G, candidate $4,000; sales.bad_aggregate 12; sales.bad_code 8; sales.special 2). Project stands.

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

Second transcription's note: Line 14 is a parenthesized (negative) amount held as a positive magnitude, so 'combine' subtracts it.

Ruling: scope; f1040sd p. 1, line 15: "Combine lines 8a through 14 in column (h)." Line 14 is the long-term carryover, printed in parentheses; the candidate subtracts it, the project adds it. Carryovers are refused (sd.carryover on line 14 and sd.count), so line 14 is zero within scope; the sign convention is open as T-004. Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,630 of 1,714 agree, no value differs; the 83 project-refuses are cited Schedule D and Form 1099-DIV gates (sales.one screens 50, div.bad_components 16, div.section1202 6, div.unsupported 5, div.amt 4, div.bad_special 2; classm.asset.2, candidate $6,847) and the 1 project-unknown (stage16.cleanup.f8959_line16_se_refused) withholds div.box2c. Project stands.

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
{"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "f4952.carryover"}], "test": "eq"}, {"args": [{"ref": "f4952.line5"}, {"const": 0}], "test": "le"}, {"args": [{"ref": "f4952.line1"}, {"ref": "f4952.line4c"}], "test": "lt"}], "test": "all"}, {"args": [{"ref": "f4952.line1"}, {"const": 0}], "test": "le"}], "test": "any"}, {"args": [{"ref": "f4952.line4g"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"const": 0}, {"const": 0}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"line": "17"}], "test": "eq"}, {"args": [{"const": 0}, {"ref": "div.box2b"}], "test": "lt"}], "test": "all"}, "then": {"ref": "u1250.line18"}}, {"guard": {"args": [{"args": [{"ref": "div.box2b"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"line": "17"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}], "test": "eq"}], "test": "all"}
```

Second transcription's note: Yes means complete the Qualified Dividends and Capital Gain Tax Worksheet. No means complete the Schedule D Tax Worksheet. The form reaches this line only when line 17 is Yes; the value is computed either way.

Ruling: interface gap; f1040sd p. 2, line 20: "Are lines 18 and 19 both zero or blank and you are not filing Form 4952? Yes. Complete the Qualified Dividends and Capital Gain Tax Worksheet ... No. Complete the Schedule D Tax Worksheet". The candidate's predicate is the project's except that it reads its own line 18, which is 0 because the box 2d rule (i1040sd p. 2, Capital Gain Distributions: "If there is an amount in box 2d, include that amount on line 4 of the 28% Rate Gain Worksheet in these instructions if you complete line 18 of Schedule D") was not on the pages given (see sd.line18). Triage executable-triage-v2 (triage/sd.json; 1,094 fixtures, 500 generated returns seed 20261026, 120 partial records): 1,624 of 1,714 agree; all 22 value differences are returns where the project's line 18 is positive (project false, candidate true): classm.tcw.1 ($400 on line 18; completed), classm.tcw.12, classm.sa.2, classm.eic.5, sales.select.sdtw.28pct, generated 90, 100, 257 and 392 (completed); the source sends them to the Schedule D Tax Worksheet. When line 17 is No both sides now read lines 18 and 19 as zero (BUG-0149), so the 963 differences on such returns in the round-1 record are gone; the line is a Boolean flow predicate, shown by the documented convention. The 63 project-refuses are cited gates read through g28 and u1250 (sales.one screens 45, div.bad_components 8, div.section1202 4, div.amt 3, div.unsupported 2, div.bad_special 1); the 4 candidate-refuses (generated 51, 273, 284, 472: f4952.bad_election, f4952.alternative_allocation, sb.unsupported, f4952.unsupported) arise because the candidate's zero line 18 sends it on to the Form 4952 terms, on returns the project refuses; the 1 project-unknown withholds div.box2c: scope. Project stands.

### 21 — Deductible loss, signed; zero when line 21 is skipped
Status: **AGREE**

### 22 — Do you have qualified dividends?
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| sd.line19 | sd.carryover, sd.other_forms | - |
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
| 20 | sd.carryover, sd.other_forms | - |
| 21 | sd.carryover, sd.other_forms | - |

## Raw second transcription

```yaml
```yaml
lines:
  - id: sd.line1a.d
    printed: "1a(d)"
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments: (d) Proceeds (sales price)"
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
    note: "Line 1a holds basis-reported short-term transactions with no adjustments that are not reported on Form 8949. These are short-term entries in box A (Form 1099-B) or box G (Form 1099-DA) that the filer routes to the aggregate totals. If the filer reports them on Form 8949 instead (route detail), they go on line 1b and this line stays blank."

  - id: sd.line1a.e
    printed: "1a(e)"
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments: (e) Cost (or other basis)"
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

  - id: sd.line1a.g
    printed: "1a(g)"
    label: "Totals for all short-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments: (g) Adjustments to gain or loss"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "A"}]}
              - {op: test, eq: [sales.box, {const: "G"}]}
    note: "Line 1a covers only transactions with no adjustments, so this total should be zero. It is summed rather than fixed at zero so that column (h) stays consistent with columns (d), (e) and (g)."

  - id: sd.h_1a_de
    printed: "(helper)"
    label: "Line 1a: subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line1a.d, take: sd.line1a.e}

  - id: sd.line1a.h
    printed: "1a(h)"
    label: "Line 1a (h) Gain or (loss): Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_1a_de, sd.line1a.g]}

  - id: sd.line1b.d
    printed: "1b(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked: (d) Proceeds (sales price)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked: (e) Cost (or other basis)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box A or Box G checked: (g) Adjustments to gain or loss from Form(s) 8949, Part I, line 2, column (g)"
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
    label: "Line 1b: subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line1b.d, take: sd.line1b.e}

  - id: sd.line1b.h
    printed: "1b(h)"
    label: "Line 1b (h) Gain or (loss): Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_1b_de, sd.line1b.g]}

  - id: sd.line2.d
    printed: "2(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked: (d) Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "B"}]}
          - {op: test, eq: [sales.box, {const: "H"}]}

  - id: sd.line2.e
    printed: "2(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked: (e) Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "B"}]}
          - {op: test, eq: [sales.box, {const: "H"}]}

  - id: sd.line2.g
    printed: "2(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box B or Box H checked: (g) Adjustments to gain or loss"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "B"}]}
          - {op: test, eq: [sales.box, {const: "H"}]}

  - id: sd.h_2_de
    printed: "(helper)"
    label: "Line 2: subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line2.d, take: sd.line2.e}

  - id: sd.line2.h
    printed: "2(h)"
    label: "Line 2 (h) Gain or (loss): Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_2_de, sd.line2.g]}

  - id: sd.line3.d
    printed: "3(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked: (d) Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "C"}]}
          - {op: test, eq: [sales.box, {const: "I"}]}

  - id: sd.line3.e
    printed: "3(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked: (e) Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "C"}]}
          - {op: test, eq: [sales.box, {const: "I"}]}

  - id: sd.line3.g
    printed: "3(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box C or Box I checked: (g) Adjustments to gain or loss"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "C"}]}
          - {op: test, eq: [sales.box, {const: "I"}]}

  - id: sd.h_3_de
    printed: "(helper)"
    label: "Line 3: subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line3.d, take: sd.line3.e}

  - id: sd.line3.h
    printed: "3(h)"
    label: "Line 3 (h) Gain or (loss): Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_3_de, sd.line3.g]}

  - id: sd.line8a.d
    printed: "8a(d)"
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments: (d) Proceeds (sales price)"
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
    note: "Long-term counterpart of line 1a. It holds box D (Form 1099-B) and box J (Form 1099-DA) entries that the filer routes to the aggregate totals."

  - id: sd.line8a.e
    printed: "8a(e)"
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments: (e) Cost (or other basis)"
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

  - id: sd.line8a.g
    printed: "8a(g)"
    label: "Totals for all long-term transactions reported on Form 1099-B or Form 1099-DA for which basis was reported to the IRS and for which you have no adjustments: (g) Adjustments to gain or loss"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        all:
          - {op: test, eq: [sales.route, {const: "aggregate"}]}
          - op: test
            any:
              - {op: test, eq: [sales.box, {const: "D"}]}
              - {op: test, eq: [sales.box, {const: "J"}]}
    note: "Line 8a covers only transactions with no adjustments, so this total should be zero. It is summed rather than fixed at zero so that column (h) stays consistent."

  - id: sd.h_8a_de
    printed: "(helper)"
    label: "Line 8a: subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line8a.d, take: sd.line8a.e}

  - id: sd.line8a.h
    printed: "8a(h)"
    label: "Line 8a (h) Gain or (loss): Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_8a_de, sd.line8a.g]}

  - id: sd.line8b.d
    printed: "8b(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked: (d) Proceeds (sales price)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked: (e) Cost (or other basis)"
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
    label: "Totals for all transactions reported on Form(s) 8949 with Box D or Box J checked: (g) Adjustments to gain or loss from Form(s) 8949, Part II, line 2, column (g)"
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
    label: "Line 8b: subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line8b.d, take: sd.line8b.e}

  - id: sd.line8b.h
    printed: "8b(h)"
    label: "Line 8b (h) Gain or (loss): Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_8b_de, sd.line8b.g]}

  - id: sd.line9.d
    printed: "9(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked: (d) Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "E"}]}
          - {op: test, eq: [sales.box, {const: "K"}]}

  - id: sd.line9.e
    printed: "9(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked: (e) Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "E"}]}
          - {op: test, eq: [sales.box, {const: "K"}]}

  - id: sd.line9.g
    printed: "9(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box E or Box K checked: (g) Adjustments to gain or loss"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "E"}]}
          - {op: test, eq: [sales.box, {const: "K"}]}

  - id: sd.h_9_de
    printed: "(helper)"
    label: "Line 9: subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line9.d, take: sd.line9.e}

  - id: sd.line9.h
    printed: "9(h)"
    label: "Line 9 (h) Gain or (loss): Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_9_de, sd.line9.g]}

  - id: sd.line10.d
    printed: "10(d)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked: (d) Proceeds (sales price)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.proceeds
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "F"}]}
          - {op: test, eq: [sales.box, {const: "L"}]}

  - id: sd.line10.e
    printed: "10(e)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked: (e) Cost (or other basis)"
    type: NonNegDollars
    expr:
      op: sum_over
      collection: sales
      field: sales.e
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "F"}]}
          - {op: test, eq: [sales.box, {const: "L"}]}

  - id: sd.line10.g
    printed: "10(g)"
    label: "Totals for all transactions reported on Form(s) 8949 with Box F or Box L checked: (g) Adjustments to gain or loss"
    type: Dollars
    expr:
      op: sum_over
      collection: sales
      field: sales.g
      where:
        op: test
        any:
          - {op: test, eq: [sales.box, {const: "F"}]}
          - {op: test, eq: [sales.box, {const: "L"}]}

  - id: sd.h_10_de
    printed: "(helper)"
    label: "Line 10: subtract column (e) from column (d)"
    type: Dollars
    expr: {op: subtract, from: sd.line10.d, take: sd.line10.e}

  - id: sd.line10.h
    printed: "10(h)"
    label: "Line 10 (h) Gain or (loss): Subtract column (e) from column (d) and combine the result with column (g)"
    type: Dollars
    expr: {op: sum, of: [sd.h_10_de, sd.line10.g]}

  - id: sd.zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: sd.line4
    printed: "4"
    label: "Short-term gain from Form 6252 and short-term gain or (loss) from Forms 4684, 6781, and 8824"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    refuses: [sd.other_forms]
    note: "Amounts from Forms 6252, 4684, 6781 and 8824 are outside this slice and are screened by sd.other_forms. The line is zero in the computed case."

  - id: sd.line5
    printed: "5"
    label: "Net short-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    refuses: [sd.other_forms]
    note: "Schedule K-1 capital gains and losses are screened by sd.other_forms. The line is zero in the computed case."

  - id: sd.line6
    printed: "6"
    label: "Short-term capital loss carryover. Enter the amount, if any, from line 8 of your Capital Loss Carryover Worksheet in the instructions"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    refuses: [sd.carryover]
    note: "A capital loss carryover is screened by sd.carryover. The amount is entered in parentheses; it is held here as a positive magnitude, and line 7 subtracts it. The line is zero in the computed case."

  - id: sd.line11
    printed: "11"
    label: "Gain from Form 4797, Part I; long-term gain from Forms 2439 and 6252; and long-term gain or (loss) from Forms 4684, 6781, and 8824"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    refuses: [sd.other_forms]
    note: "These forms are screened by sd.other_forms. The line is zero in the computed case."

  - id: sd.line12
    printed: "12"
    label: "Net long-term gain or (loss) from partnerships, S corporations, estates, and trusts from Schedule(s) K-1"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    refuses: [sd.other_forms]
    note: "Schedule K-1 capital gains and losses are screened by sd.other_forms. The line is zero in the computed case."

  - id: sd.line14
    printed: "14"
    label: "Long-term capital loss carryover. Enter the amount, if any, from line 13 of your Capital Loss Carryover Worksheet in the instructions"
    type: Dollars
    expr: {op: param, ref: sales.zero}
    refuses: [sd.carryover]
    note: "A capital loss carryover is screened by sd.carryover. The amount is entered in parentheses; it is held here as a positive magnitude, and line 15 subtracts it. The line is zero in the computed case."

  - id: sd.line13
    printed: "13"
    label: "Capital gain distributions. See the instructions"
    type: NonNegDollars
    expr: {op: copy, from: sd.distributions}
    note: "The instructions refer to 'Capital Gain Distributions, earlier', which is not in the supplied text. The line uses the supplied capital gain distributions subtotal (generally Form 1099-DIV box 2a)."

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
    note: "Line 6 is a parenthesized (negative) amount held as a positive magnitude, so 'combine' subtracts it."

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
    note: "Line 14 is a parenthesized (negative) amount held as a positive magnitude, so 'combine' subtracts it."

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
    note: "The form reaches line 17 only when line 16 is a gain. When it is not, the answer computed here is No, which agrees with skipping lines 18 to 21."

  - id: sd.line18
    printed: "(helper)"
    label: "Schedule D line 18: If you are required to complete the 28% Rate Gain Worksheet (see instructions), enter the amount, if any, from line 7 of that worksheet"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
    note: "This is printed line 18; it is marked (helper) because it is supplied as a result interface. The supplied instructions require the 28% Rate Gain Worksheet only for a section 1202 exclusion or a collectibles gain or (loss) reported in Part II of Form 8949. Those sales are outside this slice: they are screened per entry by sales.special, and gains from other forms by sd.other_forms. The worksheet is therefore never required here and the line is zero. The supplied text does not make Form 1099-DIV box 2d a trigger on its own (that rule would sit in the omitted 'Capital Gain Distributions' instructions), so box 2d is not encoded. This is a limitation."

  - id: sd.line19
    printed: "(helper)"
    label: "Schedule D line 19: If you are required to complete the Unrecaptured Section 1250 Gain Worksheet (see instructions), enter the amount, if any, from line 18 of that worksheet"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [sd.line17, {const: true}]}
              - {op: test, gt: [div.box2b, {const: 0}]}
          then: u1250.line18
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [sd.line17, {const: true}]}
                - {op: test, gt: [div.box2b, {const: 0}]}
          then: sd.zero
    note: "This is printed line 19; it is marked (helper) because it is supplied as a result interface. Of the worksheet triggers in the supplied text, only the Form 1099-DIV report of unrecaptured section 1250 gain (box 2b) is in scope. Section 1250 property sales, installment sales and Schedule K-1 amounts are screened by sales.special and sd.other_forms. The worksheet applies only if line 17 is Yes."

  - id: sd.filing4952
    printed: "(helper)"
    label: "Are you filing Form 4952?"
    type: Bool
    expr: {op: copy, from: f4952.required}
    note: "Line 20 asks whether you are filing Form 4952. The supplied Schedule D text does not define when Form 4952 is filed. This reads it as Form 4952's own required determination (f4952.required)."

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
    note: "Yes means complete the Qualified Dividends and Capital Gain Tax Worksheet. No means complete the Schedule D Tax Worksheet. The form reaches this line only when line 17 is Yes; the value is computed either way."

  - id: sd.h_loss_limit
    printed: "(helper)"
    label: "($3,000), or if married filing separately, ($1,500)"
    type: Dollars
    expr: {op: param, ref: sd.loss_limit}

  - id: sd.h_21_loss
    printed: "(helper)"
    label: "The smaller of the loss on line 16 or the loss limit, treating both amounts as positive numbers"
    type: Dollars
    expr: {op: larger_of, of: [sd.line16, sd.h_loss_limit]}
    note: "Both amounts are negative, so the smaller magnitude is the larger signed value."

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
    note: "Held as a negative amount, as it is entered on Form 1040 line 7a. It is zero when line 16 is not a loss, because the line is then skipped."

  - id: sd.line22
    printed: "22"
    label: "Do you have qualified dividends on Form 1040, 1040-SR, or 1040-NR, line 3a?"
    type: Bool
    expr: {op: test, gt: [f1040.line3a, {const: 0}]}

  - id: sd.investment_election
    printed: "(helper)"
    label: "Amount from Form 4952, line 4g, if you file Form 4952"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [sd.filing4952, {const: true}]}
          then: f4952.line4g
        - guard: {op: test, eq: [sd.filing4952, {const: false}]}
          then: sd.zero
    note: "The Schedule D Tax Worksheet applies 'if you file Form 4952 and you have an amount on line 4g', and its line 3 reads Form 4952 line 4g. This reads the interface as that amount when Form 4952 is filed, and zero otherwise."

  - id: sd.h_sales_count
    printed: "(helper)"
    label: "Number of securities sales entered"
    type: Count
    expr: {op: sum_over, collection: sales, field: sales.one}

  - id: sd.filed
    printed: "(helper)"
    label: "Are you filing Schedule D?"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [sd.h_sales_count, {const: 0, type: Count}]}
        - {op: test, eq: [sd.carryover, {const: true}]}
        - {op: test, eq: [sd.other_forms, {const: true}]}
    note: "The supplied text does not state when Schedule D must be filed. It only implies, through the Form 1040 line 7b box, that some filers with capital gain distributions need not file it. The reading chosen: Schedule D is filed when there is any sale, a capital loss carryover, or an amount from another form or a Schedule K-1. Capital gain distributions alone do not make it filed."

  - id: sd.to1040
    printed: "(helper)"
    label: "Amount for Form 1040, 1040-SR, or 1040-NR, line 7a"
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
    note: "From the line 16 instructions: if line 16 is a gain, enter it on line 7a. If it is a loss, enter line 21. If it is zero, enter -0-."

  - id: sd.h_small_15_16
    printed: "(helper)"
    label: "The smaller of line 15 or line 16 of Schedule D"
    type: Dollars
    expr: {op: smaller_of, of: [sd.line15, sd.line16]}

  - id: sd.net_gain
    printed: "(helper)"
    label: "The smaller of line 15 or line 16 of Schedule D. If either line 15 or line 16 is blank or a loss, enter -0-"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: sd.h_small_15_16, take: {const: 0}}
    note: "Read from Qualified Dividends and Capital Gain Tax Worksheet line 3 (Yes branch); Schedule D Tax Worksheet line 7 uses the same smaller-of amount. If either line is zero or a loss, the smaller is zero or less and the floor gives -0-."
```
```
