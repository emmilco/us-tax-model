# Transcription agreement — retirement

Second transcription of `Form 1099-R distributions (IRAs, pensions and annuities)` by an isolated model (spec 6.5), compared line by line with `forms/2025/retirement.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| line-scoped reviews | 2 (latest 2026-11-04); see Line-scoped reviews |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 5162e8c502e87badadbf77ca44b17819f68113d5f829520705043795019beb41 |
| prompt policy | source-only-computation-v3 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 9f566acc218c1c13d64a9097a7024df9e047335ed59fd0f8cbc0e3b5c7d0adff |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 4510132f2975bf6f271b318714e9936482c16c4c09353ddad9e10ee334c22248 |
| printed lines compared | 26 |
| agree / disagree / missing | 1 / 25 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099r | 2025 (calendar-year form) | 5, 7 | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | 5, 7 | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| i1040gi | 2025; printed date 2026-02-25 | 26, 27, 28, 29, 30, 31 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 26, 27, 28, 30, 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i5329 | 2025 | 1, 3, 5 | cited pages | bc85a048e4293ab244d68023ac7bb45333ceede0763b3b1cb3430eb4829a18bf | 1, 3, 5 | e46adbf118d780a00b73957b6ef4c6e436e651f6f076a36fa9b6717bd138ee5d |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |
| p575 | None | 12, 23, 34, 35 | pages named by another document's citation | 4d6ee3802a2906a4633dcfc104aa33bb3d9ddedebddc9eadbd0393cfdb61e07b | 12, 23, 34, 35 | 3962801dde168fda9f4ee239245d9746b12e2d60bf358b25186ae4a57aa5b837 |
| p590b | 2025 | 28 | pages named by another document's citation | 24de404e77c2a3d1f0540b91ac8c28ca4d45c7fcf968de613407419eba9266f4 | 28 | 464639ba13341fe9c824b6f495922126cb3d158650887bf9beb265fd951c3e77 |

## Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | clcw, clcw26, dependent, div, f8606, f8889, f8960, g28, household, interest, refund, s1, s3, sa, sales, sb, sdtw, u1250 |
| named line | scveh, sli |
| shared page | f1040, f5329, f8880, ira, person, s2, scope, sd, ssb, w2 |

## Lines

### retirement.one — One distribution
Status: **AGREE**

### retirement.is_ira — IRA distribution (lines 4a and 4b)
Status: **DISAGREE**

Project:

```json
{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}
```

Second:

```json
{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}
```

Ruling: representation; i1040gi p. 26, Lines 4a and 4b, IRA Distributions (the IRA lines take traditional and Roth IRA distributions; the account Enum is traditional_ira, roth_ira or plan). The candidate tests account = traditional_ira or roth_ira; the project tests account ≠ plan, the same set over the three-valued Enum. Triage. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`, written by triage.py this round; 1,565 fixtures, 500 generated returns seed 20261026, 999 partial records from 40 bases; 2,160 comparisons): 2,160 agree. Same reply and project as the stage21/bklg ruling, which stands. Project stands.

### retirement.has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a direct rollov
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}
```

Second:

```json
{"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}
```

Ruling: model error; New in this reply: it drops the code G branch and reads retirement.rollover alone, so a code G direct rollover whose rollover answer is $0 is not rolled over to it; i1040gi p. 30, Rollovers, "Use lines 5a and 5b to report a rollover, including a direct rollover"; the project treats code G as rolling over box 1 (retirement.direct; the question says "for a direct rollover, code G, the whole distribution is treated as rolled over"), the point of the refresh-round ruling, which the round-2 reply had fixed. The round-3 rollover wording fix (non-eligible distributions, nonspouse beneficiaries, code S) keeps that sentence and does not bear on it. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc) over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 1,900 agree; on completed returns 90 value differences, every one project true and reply false with the rollover answer $0 on a code G entry (e.g. classm.f1040.3 r2 and .deepseek, box 1 $0.00; classm.aqee.1 r1, box 1 $45,285.00), and 6 candidate-unknown where the rollover answer is withheld; the rest are the project's cited retirement.special, bad_code and screen refusals and unknowns on partial records. Project stands.
Reviewed in: pass 3b3828e7c41f

### retirement.taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}
```

Second transcription's note: Roth IRA with code Q: enter -0- (Exception 2(b)); other Roth IRA distributions are refused (Form 8606). Code T, which may also give -0-, falls under 'other' and is refused. Traditional IRA: the part not rolled over (Exception 1); the Exception 2 to 4 cases are screened by retirement.special.

Ruling: model error; i1040gi p. 30, Rollovers, and p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn't contribute to the cost ... or (b) you got your entire cost back tax free before 2025." New in this reply: it drops the code G branch and reads retirement.rollover alone, so a code G direct rollover whose rollover answer is $0 is not rolled over to it; its taxable amount is box 1 less the rollover answer. Also new: for a plan annuity whose amount recovered exceeds the cost (worksheet line 7 negative) it now refuses (its h_recovered_over gate), where the project enters box 1 as fully taxable; the earlier overstatement of line 9 is gone. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc) over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 2,100 agree; on completed returns 26 value differences, all code G with the rollover answer $0 (23 plan entries, e.g. classm.aqee.1 r1, $0.00 against $45,285.00; 3 traditional IRA entries, e.g. generated 147 r2, $0.00 against $41,985.98), 2 candidate refusals on line 7 negative (generated 229 r1, project $28,082.59), 6 candidate-unknown on the withheld rollover answer. Project stands.
Reviewed in: pass 3b3828e7c41f

### retirement.amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"input": "retirement.box5"}, {"const": 0}], "test": "le"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.box5"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 1)"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"input": "retirement.box5"}, {"const": 0}], "test": "le"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}], "test": "all"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": 0}, {"input": "retirement.box5"}], "test": "lt"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Second transcription's note: Lump-sum distributions ('Enter the total distribution on line 5a') cannot be identified from the inputs (box 2b is not supplied); a fully taxable plan distribution without rollover or box 5 amount is treated as having no line 5a entry.

Ruling: model error; i1040gi p. 28: "If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don't make an entry on line 5a", and p. 30, Rollovers. The reply enters box 1 on line 5a for every plan annuity, also one with no cost left (generated 229 r1: project none, reply $28,082.59, the earlier rounds' point), and, new, makes no line 5a entry for a code G direct rollover whose rollover answer is $0 (see retirement.has_rollover). Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc) over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 2,006 agree; on completed returns 28 value differences (26 code G: 23 plan, e.g. classm.aqee.1 r1, $45,285.00 against $0.00, and 3 traditional IRA, e.g. generated 147 r2; 2 the no-cost annuity above) and 6 candidate-unknown on the withheld rollover answer. Project stands.
Reviewed in: pass 3b3828e7c41f

### retirement.sav_amount — This distribution's amount on Form 8880 line 4
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "eq"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; f8880 p. 2, Line 4: "Don't include any of the following. • Distributions not taxable as the result of a rollover or a trustee-to-trustee transfer." New in this reply: a code G direct rollover with a $0 rollover answer counts in full. As before it asks retirement.sav_404k, sav_military and sav_inherited of every entry, where the project asks the first two of plan entries and the third of IRA entries. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc) over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 2,067 agree; on completed returns 23 value differences, all code G (e.g. classm.aqee.1 r1, project $0.00, reply $45,285.00), and 17 candidate-unknown on the unasked Form 8880 answers. Project stands.
Reviewed in: pass 3b3828e7c41f

### retirement.l1 — Form 5329 line 1 share: the taxable amount of an early distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}
```

Second transcription's note: Codes 1, 2, 3 and S are treated as early distributions. Codes 4 (death), 7, G and Q are not. Code 'other' cannot be classified from the inputs, so it is refused here.

Ruling: ambiguity and model error; i5329 p. 3, Line 1, "Enter the amount of early distributions includible in income (other than qualified disaster recovery distributions) that you received from:" (amb.2025.f5329_line1_codes, owner decision D8(a): codes 1 and S only). The reply now puts codes 1, 2, 3 and S on line 1, the register's reading 2 (it offsets codes 2 and 3 in full on line 2, so the tax is the same). As the earlier rulings, it asks retirement.early_screen and code_screen of every entry (retirement.early_screen is asked only for code 1 and S, code_screen only for codes 2, 4 and 7). Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc) over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 1,688 agree; on completed returns 80 candidate-unknown (the unasked screens) and 2 value differences, both the code 2 entry generated 175 r1 (project $0.00, reply $52,095.29). Project stands.
Reviewed in: pass 3b3828e7c41f

### retirement.l2 — Form 5329 line 2 share before the per-person limits
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Open: whether l2 holds all exceptions or only those without a dollar limit. Chosen: l2 is the whole entry-level exclusion before per-person limits, and l2_eNN gives the part under each capped exception. For codes 2 and 3 the payer's exception covers the whole line 1 amount (partial coverage is refused by code_screen), and no capped-exception split is made.

Ruling: ambiguity and model error; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude." With codes 2 and 3 on line 1 (amb.2025.f5329_line1_codes reading 2, see retirement.l1) the reply excludes the whole line 1 amount for those codes on line 2, so the tax agrees; it carries line 1's unasked screens. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc) over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 2,154 agree; on completed returns 25 candidate-unknown and 2 value differences, both generated 175 r1 (code 2, $0.00 against $52,095.29). The earlier ruling's wrong_kind point is not in this sample's completed returns. Project stands.
Reviewed in: pass 3b3828e7c41f

### retirement.l2_e05 — Line 2 share under exception 05
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i5329 p. 5, Line 2: "enter the applicable exception number (01–23). If more than one exception applies, enter 99." The reply now tests the code before exception 05, so the earlier ruling's need of the exception answer on every entry is gone; its codes 2 and 3 branch never reaches an exception share. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc) over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): no completed-return difference; the few others are unknowns on partial records. Project stands.
Reviewed in: pass 3b3828e7c41f

### retirement.l2_e09 — Line 2 share under exception 09
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i5329 p. 5, Line 2: "enter the applicable exception number (01–23). If more than one exception applies, enter 99." The reply now tests the code before exception 09, so the earlier ruling's need of the exception answer on every entry is gone; its codes 2 and 3 branch never reaches an exception share. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc) over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): no completed-return difference; the few others are unknowns on partial records. Project stands.
Reviewed in: pass 3b3828e7c41f

### retirement.l2_e19 — Line 2 share under exception 19
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i5329 p. 5, Line 2: "enter the applicable exception number (01–23). If more than one exception applies, enter 99." The reply now tests the code before exception 19, so the earlier ruling's need of the exception answer on every entry is gone; its codes 2 and 3 branch never reaches an exception share. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc) over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): no completed-return difference; the few others are unknowns on partial records. Project stands.
Reviewed in: pass 3b3828e7c41f

### retirement.l2_e22 — Line 2 share under exception 22
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i5329 p. 5, Line 2: "enter the applicable exception number (01–23). If more than one exception applies, enter 99." The reply now tests the code before exception 22, so the earlier ruling's need of the exception answer on every entry is gone; its codes 2 and 3 branch never reaches an exception share. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc) over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): no completed-return difference; the few others are unknowns on partial records. Project stands.
Reviewed in: pass 3b3828e7c41f

### retirement.is_e23 — Exception 23
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}
```

Ruling: model error; p590b p. 28, Emergency personal expense distributions; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." The reply's test is the exception answer alone, so it needs retirement.exception on entries where it is not asked (retirement.early_screen is asked only for code 1 and S entries, retirement.code_screen only for codes 2, 4 and 7, and retirement.exception only for code 1 and S entries (decision D3(a), the cited screens of retirement.screen_refused)); the project tests the code first. Same point as the refresh-round ruling. Ruled from reading the pass reply (.transcription/retirement.lines-535357ae1261) against the project; triage was not rerun.
Reviewed in: pass 136337bdca28

### retirement.l2_e23 — Line 2 share under exception 23
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i5329 p. 5, Line 2: "enter the applicable exception number (01–23). If more than one exception applies, enter 99." The reply now tests the code before exception 23, so the earlier ruling's need of the exception answer on every entry is gone; its codes 2 and 3 branch never reaches an exception share. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc) over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): no completed-return difference; the few others are unknowns on partial records. Project stands.
Reviewed in: pass 3b3828e7c41f

### retirement.l1_s — Line 1 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: scope; i5329 p. 5, Line 4 (25% for a code S distribution in the first 2 years). As the earlier ruling: for a code S entry the share is line 1, zero otherwise. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc) over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 2,411 agree; the one difference is the project's cited retirement.bad_code refusal (fixture stage21.refuse.bad_code_screen_unasked). Project stands.
Reviewed in: pass 3b3828e7c41f

### retirement.l2_s — Line 2 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i5329 p. 5, Line 2 and Line 4. For a code S entry the share is line 2, zero otherwise, as the project. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc) over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 2,412 of 2,412 agree. Project stands.
Reviewed in: pass 3b3828e7c41f

### (SMW 1) — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, "value": {"input": "retirement.box1"}}
```

Second:

```json
{"shown_when": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "value": {"input": "retirement.box1"}}
```

Ruling: model error; same reply and project as the earlier ruling. i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet"; i1040gi p. 28: "Your payments are fully taxable if (a) you didn't contribute to the cost ... or (b) you got your entire cost back tax free before 2025." The reply shows the worksheet for every plan annuity (shown_when plan and annuity), the project only with cost left to recover (worksheet line 7 above zero, retirement.smw_shown); the line's expression is unchanged from the earlier ruling. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc; 1,578 fixtures, 500 generated returns seed 20261026, 1,030 partial records; 2,342 comparisons per line): the differences are candidate-shows-skipped and candidate-unknown records (values the reply's display condition shows or its unasked worksheet answers), project-unknown partial records, and, from line 7 on, up to 6 candidate refusals on the reply's h_recovered_over gate (amount recovered above cost; ruled on retirement.taxable). Project stands.
Reviewed in: pass 3b3828e7c41f

### (SMW 2) — Enter your cost in the plan at the annuity starting date
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, "value": {"input": "retirement.cost"}}
```

Second:

```json
{"shown_when": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "value": {"input": "retirement.cost"}}
```

Second transcription's note: The death benefit exclusion that 'Before you begin' adds to line 2 is screened out by retirement.special, so line 2 is the cost alone.

Ruling: model error; same reply and project as the earlier ruling. i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet"; i1040gi p. 28: "Your payments are fully taxable if (a) you didn't contribute to the cost ... or (b) you got your entire cost back tax free before 2025." The reply shows the worksheet for every plan annuity (shown_when plan and annuity), the project only with cost left to recover (worksheet line 7 above zero, retirement.smw_shown); the line's expression is unchanged from the earlier ruling. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc; 1,578 fixtures, 500 generated returns seed 20261026, 1,030 partial records; 2,342 comparisons per line): the differences are candidate-shows-skipped and candidate-unknown records (values the reply's display condition shows or its unasked worksheet answers), project-unknown partial records, and, from line 7 on, up to 6 candidate refusals on the reply's h_recovered_over gate (amount recovered above cost; ruled on retirement.taxable). Project stands.
Reviewed in: pass 3b3828e7c41f

### (SMW 4) — Divide line 2 by the number on line 3 (or, if you completed this worksheet last year, line
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 56, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_360"}}}, {"guard": {"args": [{"args": [{"const": 56, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 61, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_310"}}}, {"guard": {"args": [{"args": [{"const": 61, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 66, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_260"}}}, {"guard": {"args": [{"args": [{"const": 66, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 71, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_210"}}}, {"guard": {"args": [{"const": 71, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_160"}}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 111, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_410"}}}, {"guard": {"args": [{"args": [{"const": 111, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 121, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_360"}}}, {"guard": {"args": [{"args": [{"const": 121, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 131, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_310"}}}, {"guard": {"args": [{"args": [{"const": 131, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 141, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_260"}}}, {"guard": {"args": [{"const": 141, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_210"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"input": "retirement.last_line4"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": 56, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 60, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_310"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": 61, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 65, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_260"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": 66, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 70, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_210"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": 71, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_160"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"input": "retirement.age"}, {"const": 55, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_360"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": 111, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 120, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_360"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": 121, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 130, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_310"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": 131, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 140, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_260"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": 141, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_210"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 110, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_410"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"input": "retirement.last_line4"}}], "op": "choose"}
```

Second transcription's note: The worksheet does not say how to round the quotient on line 4; chosen: half-up to the cent (multiply_rate by 1/n). Only the 'after November 18, 1996' column of Table 1 is used, because earlier starting dates are screened out by retirement.annuity and retirement.special. Line 3 is folded into this choice.

Ruling: equivalent; project retained. i1040gi p. 29, Simplified Method Worksheet, line 4 and Tables 1 and 2 ("after November 18, 1996" column). The reply repeats the not-used-last-year test in every band instead of nesting it; ages are whole numbers, so its bands (56 to 60 as 56 <= age <= 60) are the project's. Same as the earlier ruling.
Reviewed in: pass 3b3828e7c41f

### (SMW 5) — Multiply line 4 by the number of months for which this year's payments were made
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, "value": {"amount": {"line": "(SMW 4)"}, "count": {"input": "retirement.months"}, "op": "multiply_count"}}
```

Second:

```json
{"shown_when": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "value": {"amount": {"line": "(SMW 4)"}, "count": {"input": "retirement.months"}, "op": "multiply_count"}}
```

Second transcription's note: The instruction to skip lines 6 and 7 when the annuity starting date was before 1987 never applies, because retirement.annuity requires a starting date after November 18, 1996.

Ruling: model error; same reply and project as the earlier ruling. i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet"; i1040gi p. 28: "Your payments are fully taxable if (a) you didn't contribute to the cost ... or (b) you got your entire cost back tax free before 2025." The reply shows the worksheet for every plan annuity (shown_when plan and annuity), the project only with cost left to recover (worksheet line 7 above zero, retirement.smw_shown); the line's expression is unchanged from the earlier ruling. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc; 1,578 fixtures, 500 generated returns seed 20261026, 1,030 partial records; 2,342 comparisons per line): the differences are candidate-shows-skipped and candidate-unknown records (values the reply's display condition shows or its unasked worksheet answers), project-unknown partial records, and, from line 7 on, up to 6 candidate refusals on the reply's h_recovered_over gate (amount recovered above cost; ruled on retirement.taxable). Project stands.
Reviewed in: pass 3b3828e7c41f

### (SMW 6) — Enter the amount, if any, recovered tax free in years after 1986
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, "value": {"input": "retirement.recovered"}}
```

Second:

```json
{"shown_when": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "value": {"input": "retirement.recovered"}}
```

Ruling: model error; same reply and project as the earlier ruling. i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet"; i1040gi p. 28: "Your payments are fully taxable if (a) you didn't contribute to the cost ... or (b) you got your entire cost back tax free before 2025." The reply shows the worksheet for every plan annuity (shown_when plan and annuity), the project only with cost left to recover (worksheet line 7 above zero, retirement.smw_shown); the line's expression is unchanged from the earlier ruling. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc; 1,578 fixtures, 500 generated returns seed 20261026, 1,030 partial records; 2,342 comparisons per line): the differences are candidate-shows-skipped and candidate-unknown records (values the reply's display condition shows or its unasked worksheet answers), project-unknown partial records, and, from line 7 on, up to 6 candidate refusals on the reply's h_recovered_over gate (amount recovered above cost; ruled on retirement.taxable). Project stands.
Reviewed in: pass 3b3828e7c41f

### (SMW 7) — Subtract line 6 from line 2
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, "value": {"from": {"line": "(SMW 2)"}, "op": "subtract", "take": {"line": "(SMW 6)"}}}
```

Second:

```json
{"shown_when": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "value": {"from": {"line": "(SMW 2)"}, "op": "subtract", "take": {"line": "(SMW 6)"}}}
```

Ruling: model error; same reply and project as the earlier ruling. i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet"; i1040gi p. 28: "Your payments are fully taxable if (a) you didn't contribute to the cost ... or (b) you got your entire cost back tax free before 2025." The reply shows the worksheet for every plan annuity (shown_when plan and annuity), the project only with cost left to recover (worksheet line 7 above zero, retirement.smw_shown); the line's expression is unchanged from the earlier ruling. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc; 1,578 fixtures, 500 generated returns seed 20261026, 1,030 partial records; 2,342 comparisons per line): the differences are candidate-shows-skipped and candidate-unknown records (values the reply's display condition shows or its unasked worksheet answers), project-unknown partial records, and, from line 7 on, up to 6 candidate refusals on the reply's h_recovered_over gate (amount recovered above cost; ruled on retirement.taxable). Project stands.
Reviewed in: pass 3b3828e7c41f

### (SMW 8) — Enter the smaller of line 5 or line 7
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, "value": {"of": [{"line": "(SMW 5)"}, {"line": "(SMW 7)"}], "op": "smaller_of"}}
```

Second:

```json
{"shown_when": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "value": {"of": [{"line": "(SMW 5)"}, {"line": "(SMW 7)"}], "op": "smaller_of"}}
```

Ruling: model error; same reply and project as the earlier ruling. i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet"; i1040gi p. 28: "Your payments are fully taxable if (a) you didn't contribute to the cost ... or (b) you got your entire cost back tax free before 2025." The reply shows the worksheet for every plan annuity (shown_when plan and annuity), the project only with cost left to recover (worksheet line 7 above zero, retirement.smw_shown); the line's expression is unchanged from the earlier ruling. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc; 1,578 fixtures, 500 generated returns seed 20261026, 1,030 partial records; 2,342 comparisons per line): the differences are candidate-shows-skipped and candidate-unknown records (values the reply's display condition shows or its unasked worksheet answers), project-unknown partial records, and, from line 7 on, up to 6 candidate refusals on the reply's h_recovered_over gate (amount recovered above cost; ruled on retirement.taxable). Project stands.
Reviewed in: pass 3b3828e7c41f

### (SMW 9) — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, "value": {"from": {"line": "(SMW 1)"}, "op": "subtract_floor0", "take": {"line": "(SMW 8)"}}}
```

Second:

```json
{"shown_when": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "value": {"from": {"line": "(SMW 1)"}, "op": "subtract_floor0", "take": {"line": "(SMW 8)"}}}
```

Ruling: model error; same reply and project as the earlier ruling. i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet"; i1040gi p. 28: "Your payments are fully taxable if (a) you didn't contribute to the cost ... or (b) you got your entire cost back tax free before 2025." The reply shows the worksheet for every plan annuity (shown_when plan and annuity), the project only with cost left to recover (worksheet line 7 above zero, retirement.smw_shown); the line's expression is unchanged from the earlier ruling. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc; 1,578 fixtures, 500 generated returns seed 20261026, 1,030 partial records; 2,342 comparisons per line): the differences are candidate-shows-skipped and candidate-unknown records (values the reply's display condition shows or its unasked worksheet answers), project-unknown partial records, and, from line 7 on, up to 6 candidate refusals on the reply's h_recovered_over gate (amount recovered above cost; ruled on retirement.taxable). Project stands.
Reviewed in: pass 3b3828e7c41f

### (SMW 10) — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, "value": {"of": [{"line": "(SMW 6)"}, {"line": "(SMW 8)"}], "op": "sum"}}
```

Second:

```json
{"shown_when": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "value": {"of": [{"line": "(SMW 6)"}, {"line": "(SMW 8)"}], "op": "sum"}}
```

Second transcription's note: The 'Yes. STOP' branch (starting date before 1987) cannot occur within the scope of retirement.annuity, so line 10 is always completed.

Ruling: model error; same reply and project as the earlier ruling. i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet"; i1040gi p. 28: "Your payments are fully taxable if (a) you didn't contribute to the cost ... or (b) you got your entire cost back tax free before 2025." The reply shows the worksheet for every plan annuity (shown_when plan and annuity), the project only with cost left to recover (worksheet line 7 above zero, retirement.smw_shown); the line's expression is unchanged from the earlier ruling. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc; 1,578 fixtures, 500 generated returns seed 20261026, 1,030 partial records; 2,342 comparisons per line): the differences are candidate-shows-skipped and candidate-unknown records (values the reply's display condition shows or its unasked worksheet answers), project-unknown partial records, and, from line 7 on, up to 6 candidate refusals on the reply's h_recovered_over gate (amount recovered above cost; ruled on retirement.taxable). Project stands.
Reviewed in: pass 3b3828e7c41f

### (SMW 11) — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **DISAGREE**

Project:

```json
{"shown_when": {"args": [{"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, "value": {"from": {"line": "(SMW 2)"}, "op": "subtract", "take": {"line": "(SMW 10)"}}}
```

Second:

```json
{"shown_when": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "value": {"from": {"line": "(SMW 2)"}, "op": "subtract", "take": {"line": "(SMW 10)"}}}
```

Ruling: model error; same reply and project as the earlier ruling. i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet"; i1040gi p. 28: "Your payments are fully taxable if (a) you didn't contribute to the cost ... or (b) you got your entire cost back tax free before 2025." The reply shows the worksheet for every plan annuity (shown_when plan and annuity), the project only with cost left to recover (worksheet line 7 above zero, retirement.smw_shown); the line's expression is unchanged from the earlier ruling. Scratch run of triage.mjs on the round-3 pass reply (.transcription/retirement.lines-fede9ff2eecc; 1,578 fixtures, 500 generated returns seed 20261026, 1,030 partial records; 2,342 comparisons per line): the differences are candidate-shows-skipped and candidate-unknown records (values the reply's display condition shows or its unasked worksheet answers), project-unknown partial records, and, from line 7 on, up to 6 candidate refusals on the reply's h_recovered_over gate (amount recovered above cost; ruled on retirement.taxable). Project stands.
Reviewed in: pass 3b3828e7c41f

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| retirement.taxable | retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused, retirement.special | retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused |
| retirement.amount_a | retirement.special | - |
| retirement.sav_amount | retirement.special | - |
| retirement.l1 | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused |
| retirement.l2 | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused |
| retirement.l2_e05 | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused |
| retirement.l2_e09 | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused |
| retirement.l2_e19 | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused |
| retirement.l2_e22 | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused |
| retirement.l2_e23 | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused |
| retirement.l1_s | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused |
| retirement.l2_s | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_recovered_over, retirement.h_rollover_over, retirement.h_roth_refused |
| (SMW 7) | retirement.h_recovered_over | retirement.h_recovered_over |
| (SMW 8) | retirement.h_recovered_over | retirement.h_recovered_over |
| (SMW 9) | retirement.h_recovered_over | retirement.h_recovered_over |
| (SMW 10) | retirement.h_recovered_over | retirement.h_recovered_over |
| (SMW 11) | retirement.h_recovered_over | retirement.h_recovered_over |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| retirement.one | 76b9f2cffa363962328538b47981396fbfe500bba0758d5db5018ea61d1d0a64 |
| retirement.is_ira | 346a3e8d9e9bd5fd570df6652d6d72eac3cf20ec1a8149eb316e81b972dcde84 |
| retirement.has_rollover | 57f84842cd86f21cd76b6eee02e37a265c9376e2a24193807d005ab1ac3eebc7 |
| retirement.taxable | 92a5bb155b007e5a4053b3344ff0527d09f75da0af998d99cbe4c62bf97c4908 |
| retirement.amount_a | 9ce16ecff00c8e8fd3c76ee9c87d6adb9bfb19c9a23948f8646368da4eeac6fd |
| retirement.sav_amount | 68ffb1fd05cf1c89a06fde40284e3ef05a8144794f46f604412b57caddc9ac12 |
| retirement.l1 | cd8fc50d367fb2d572fb7137bfb486e391b53cd3d9df711bab431b67057603af |
| retirement.l2 | 66a8a49074b529ddada15467c76f0d559e9e859d06f7091d51b86c50ae79809a |
| retirement.l2_e05 | beef2eed103684e4b8fe52d76e6cfd33cb9244ffeb4f87c257855b6d534f9b50 |
| retirement.l2_e09 | 4231db7935ae5e52c296ed2343c5ae4b25049e7518eb3056e8f02408f01546f3 |
| retirement.l2_e19 | cd2b5261c1db0c3eb5de2ac610f3cc30d267c7338360d6f9810f380fd9966e1a |
| retirement.l2_e22 | cdf76007dd231b1d8204fdd5c4a1c4b1b56be8f715f4a5564e7eb04fd15132a6 |
| retirement.is_e23 | 151da4ea1cf7523a5250e3721213041ba27dbf450919e153878989530f23b923 |
| retirement.l2_e23 | 54c039efe0da74e039ffe2f287f7a3e39438b119ff5a27772c41b10ca47a4872 |
| retirement.l1_s | 9389e242d3d022eb2b68d45e1bde6e8dc8d787fe4017212a3d8f0719b113cd51 |
| retirement.l2_s | 96134e1ee93968b047cf3f62d058c11adee9b4f61e96dee16395ee1b2ea0a78a |
| (SMW 1) | e612dc8ae5ffa3d35a1e2e8b0e155aa8cf7160fce566acc68f734c00c26f56de |
| (SMW 2) | 184d88edfe0d150dafe5316ab400b4335d9f0f6f0a2e3ee3b49a683d4dc3a582 |
| (SMW 4) | e28d091e1987fb872c6f41ff5b1a4659c75944c920476292868c06c141a430ac |
| (SMW 5) | 19a8297ec91ce1f69613251c1f6c5dc2db8ac6013892f53e4363a5af8701de21 |
| (SMW 6) | 1f2631d4bf3826b15ac14ead1e412dfaada541b0da973100d6177622521f7bd8 |
| (SMW 7) | 770265a57683fb32a4461602d4177b355a1084f3221a2f0b7cf208c7c3a45f49 |
| (SMW 8) | ccbe2932b8767f8481219d72b5de831ae66fc018033abed608375bbc39b4d09c |
| (SMW 9) | d1b393ea07917134fe1ae4cb3ecdb5b5e91852f885ab74da6634d64a59490355 |
| (SMW 10) | 5cfa9dc2a8e6728088ad53b8b2f38418aa45ceab7cd69ff652b6d5c0a65cc23f |
| (SMW 11) | 4f59cb86dcd837a03614e5c9ffbed1ced101a0145ca3cbb7ebb7846437536849 |
| (rest of the document) | 753d6dcac87a3c80fc66eda9e36c1de83ff170ac41b64253534cb38b1e178e2d |

## Foreign interfaces

The interfaces (id, printed marker, type, input question) of other documents' lines that each compared line reads, as the request carried them (tools/transcription/subjects.py); a changed row stales that line.

| line | foreign interfaces sha256 |
| --- | --- |
| retirement.has_rollover | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| retirement.taxable | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| retirement.amount_a | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| retirement.sav_amount | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| retirement.l1 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| retirement.l2 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| retirement.l2_e05 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| retirement.l2_e09 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| retirement.l2_e19 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| retirement.l2_e22 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| retirement.is_e23 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| retirement.l2_e23 | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| retirement.l1_s | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| retirement.l2_s | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| (SMW 1) | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| (SMW 2) | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| (SMW 4) | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| (SMW 5) | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| (SMW 6) | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| (SMW 7) | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| (SMW 8) | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| (SMW 9) | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| (SMW 10) | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |
| (SMW 11) | 24437f0ae25c96e08f723cc22bfd2479b7d086195d47d1dbab794b000d4bb325 |

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 136337bdca28

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines retirement.has_rollover, retirement.taxable, retirement.amount_a, retirement.sav_amount, retirement.l1, retirement.l2, retirement.l2_e05, retirement.l2_e09, retirement.l2_e19, retirement.l2_e22, retirement.is_e23, retirement.l2_e23, retirement.l1_s, retirement.l2_s |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 136337bdca2834bbd6aeec28ac0e735aa482f004fc5db202094cf8bfa986e98a |
| prompt policy | source-only-computation-v3+lines-v1 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 0c89f23597f74ec13312ebd3fbebe528e79cc4d4eabf880fcdd53fd91654330d |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 1c375407b194405d7c70ae78d4e1118d1ac7dfd40efd4acad96180401c0bb054 |
| receipt | .transcription/retirement.lines-535357ae1261 |
| printed lines compared | 14 |
| agree / disagree / missing | 0 / 14 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099r | 2025 (calendar-year form) | 5, 7, 9 | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | 5, 7, 9 | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| i1040gi | 2025; printed date 2026-02-25 | 26, 27, 28, 29, 30, 31 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 26, 27, 28, 30, 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i5329 | 2025 | 1, 3, 5 | cited pages | bc85a048e4293ab244d68023ac7bb45333ceede0763b3b1cb3430eb4829a18bf | 1, 3, 5 | e46adbf118d780a00b73957b6ef4c6e436e651f6f076a36fa9b6717bd138ee5d |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |
| p575 | None | 21, 23, 34, 35 | pages named by another document's citation | 4d6ee3802a2906a4633dcfc104aa33bb3d9ddedebddc9eadbd0393cfdb61e07b | 21, 23, 34, 35 | 3962801dde168fda9f4ee239245d9746b12e2d60bf358b25186ae4a57aa5b837 |
| p590b | 2025 | 6, 28 | pages named by another document's citation | 24de404e77c2a3d1f0540b91ac8c28ca4d45c7fcf968de613407419eba9266f4 | 6, 28 | 464639ba13341fe9c824b6f495922126cb3d158650887bf9beb265fd951c3e77 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | clcw, clcw26, dependent, div, f8606, f8889, g28, household, interest, s1, s3, sa, sales, sb, sdtw, u1250 |
| named line | scveh, sli |
| shared page | f1040, f5329, f8880, ira, person, s2, scope, sd, ssb, w2 |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: retirement.h_zero
    printed: "(helper)"
    label: "Zero (enter -0-)"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: retirement.h_is_g
    printed: "(helper)"
    label: "Box 7 shows code G, direct rollover of a distribution to a qualified plan, a section 403(b) plan, a governmental section 457(b) plan, or an IRA"
    type: Bool
    expr: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}

  - id: retirement.h_is_trad
    printed: "(helper)"
    label: "Distribution from an IRA other than a Roth IRA (IRA/SEP/SIMPLE box checked)"
    type: Bool
    expr: {op: test, eq: [retirement.account, {const: "traditional_ira"}]}

  - id: retirement.h_is_roth
    printed: "(helper)"
    label: "Distribution from a Roth IRA or Roth SIMPLE IRA"
    type: Bool
    expr: {op: test, eq: [retirement.account, {const: "roth_ira"}]}

  - id: retirement.h_is_plan
    printed: "(helper)"
    label: "Pension or annuity payment (including 401(k), 403(b) and governmental 457(b) plans)"
    type: Bool
    expr: {op: test, eq: [retirement.account, {const: "plan"}]}

  - id: retirement.h_annuity_plan
    printed: "(helper)"
    label: "You must use the Simplified Method for this pension or annuity"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.h_is_plan, {const: true}]}
        - {op: test, eq: [retirement.annuity, {const: true}]}

  - id: retirement.has_rollover
    printed: "(helper)"
    label: "Rollover, including a direct rollover (check box 1 on line 4c or line 5c)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.h_is_g, {const: true}]}
        - {op: test, gt: [retirement.rollover, {const: 0}]}

  - id: retirement.h_rollover_over
    printed: "(helper)"
    label: "Consistency check: amount rolled over is more than the total distribution in box 1"
    type: Bool
    expr: {op: test, gt: [retirement.rollover, retirement.box1]}

  - id: retirement.h_roth_unsupported
    printed: "(helper)"
    label: "Roth IRA distribution other than one with distribution code Q (see Form 8606 and its instructions)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.h_is_roth, {const: true}]}
        - {op: test, ne: [retirement.code, {const: "qualified_roth_Q"}]}

  - id: retirement.h_annuity_rollover
    printed: "(helper)"
    label: "A rollover reported for a pension or annuity figured with the Simplified Method"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.h_annuity_plan, {const: true}]}
        - {op: test, eq: [retirement.has_rollover, {const: true}]}
    note: "The Simplified Method Worksheet does not address a rollover of part of an annuity payment; the tool refuses that combination rather than guessing."

  - id: retirement.h_not_rolled
    printed: "(helper)"
    label: "If the total distribution wasn't rolled over, the part not rolled over"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.rollover}

  - id: retirement.h_plan_net5
    printed: "(helper)"
    label: "From this amount, subtract any contributions (usually shown in box 5) that were taxable to you when made"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.box5}

  - id: retirement.h_plan_taxable
    printed: "(helper)"
    label: "From that result, subtract the amount of the rollover. Enter the remaining amount on line 5b"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_plan_net5, take: retirement.rollover}
    note: "The text gives this subtraction for rollovers; for a plan distribution that is not an annuity under the Simplified Method and has no rollover, the same formula (box 1 less box 5) is used, which with box 5 zero is the fully taxable amount."

  - id: retirement.taxable
    printed: "(helper)"
    label: "Taxable amount of this distribution (Form 1040, line 4b or line 5b)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_is_g, {const: true}]}
          then: retirement.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.h_is_g, {const: false}]}
              - {op: test, eq: [retirement.h_is_roth, {const: true}]}
          then: retirement.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.h_is_g, {const: false}]}
              - {op: test, eq: [retirement.h_is_trad, {const: true}]}
          then: retirement.h_not_rolled
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.h_is_g, {const: false}]}
              - {op: test, eq: [retirement.h_annuity_plan, {const: true}]}
          then: retirement.smw9
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.h_is_g, {const: false}]}
              - {op: test, eq: [retirement.h_is_plan, {const: true}]}
              - {op: test, eq: [retirement.annuity, {const: false}]}
          then: retirement.h_plan_taxable
    refuses:
      - retirement.special
      - retirement.h_roth_unsupported
      - retirement.h_annuity_rollover
      - {when: retirement.h_rollover_over, when_known: true}
    note: "Code G: Form 1099-R says zero should be shown and you must enter -0- on the Taxable amount line. Roth IRA with code Q: enter -0- on line 4b. Other Roth IRA distributions need Form 8606 and are refused. Distribution code 'other' is not refused here: the text ties the taxable amount only to codes G, Q and T; other codes are computed by the same rules."

  - id: retirement.h_show_a
    printed: "(helper)"
    label: "Total distribution is entered on line 4a or 5a (not a fully taxable distribution entered only on line 4b or 5b)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.has_rollover, {const: true}]}
        - {op: test, eq: [retirement.h_is_roth, {const: true}]}
        - {op: test, eq: [retirement.h_annuity_plan, {const: true}]}
        - op: test
          all:
            - {op: test, eq: [retirement.h_is_plan, {const: true}]}
            - {op: test, gt: [retirement.box5, {const: 0}]}

  - id: retirement.amount_a
    printed: "(helper)"
    label: "Amount of this distribution entered on Form 1040, line 4a or line 5a"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_show_a, {const: true}]}
          then: retirement.box1
        - guard: {op: test, eq: [retirement.h_show_a, {const: false}]}
          then: retirement.h_zero
    refuses:
      - retirement.special
      - retirement.h_roth_unsupported
      - retirement.h_annuity_rollover
    note: "If the distribution is fully taxable, enter it on line 4b/5b and don't make an entry on line 4a/5a; so the line 4a/5a amount is zero then. Rollovers (Exception 1), Roth IRA distributions (Exception 2) and partially taxable pensions (Simplified Method, or box 5 after-tax contributions) put box 1 on line 4a/5a."

  - id: retirement.h_sav_excluded
    printed: "(helper)"
    label: "Form 8880 line 4 exclusion: section 404(k) dividends, a military retirement plan (other than the TSP), or an inherited IRA by a nonspousal beneficiary"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.sav_military, {const: true}]}
        - {op: test, eq: [retirement.sav_404k, {const: true}]}
        - {op: test, eq: [retirement.sav_inherited, {const: true}]}

  - id: retirement.sav_amount
    printed: "(helper)"
    label: "Amount of this distribution counted on Form 8880, line 4 (not including distributions not taxable as the result of a rollover)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_sav_excluded, {const: true}]}
          then: retirement.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.h_sav_excluded, {const: false}]}
              - {op: test, eq: [retirement.h_is_g, {const: true}]}
          then: retirement.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.h_sav_excluded, {const: false}]}
              - {op: test, eq: [retirement.h_is_g, {const: false}]}
          then: retirement.h_not_rolled
    refuses:
      - retirement.special
      - retirement.h_roth_unsupported
      - {when: retirement.h_rollover_over, when_known: true}

  - id: retirement.h_is_early
    printed: "(helper)"
    label: "Early distribution (box 7 code 1, 2, 3 or S)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.code, {const: "early_1"}]}
        - {op: test, eq: [retirement.code, {const: "early_exception_2"}]}
        - {op: test, eq: [retirement.code, {const: "simple_S"}]}
        - {op: test, eq: [retirement.code, {const: "disability_3"}]}
    note: "Code 3 (disability) is read as an early distribution to which exception 03 applies in full; codes 4 and 7 are not early unless the code is wrong, which code_screen refuses."

  - id: retirement.l1
    printed: "(helper)"
    label: "Early distributions includible in income from this distribution (Form 5329, line 1)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_is_early, {const: true}]}
          then: retirement.taxable
        - guard: {op: test, eq: [retirement.h_is_early, {const: false}]}
          then: retirement.h_zero
    refuses:
      - retirement.early_screen
      - retirement.code_screen

  - id: retirement.l1_s
    printed: "(helper)"
    label: "Part of line 1 that is a distribution from a SIMPLE IRA within 2 years of first participation (code S)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "simple_S"}]}
          then: retirement.l1
        - guard: {op: test, ne: [retirement.code, {const: "simple_S"}]}
          then: retirement.h_zero

  - id: retirement.h_code_excepted
    printed: "(helper)"
    label: "Box 7 indicates an exception applies (code 2 or code 3)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.code, {const: "early_exception_2"}]}
        - {op: test, eq: [retirement.code, {const: "disability_3"}]}

  - id: retirement.h_has_exc
    printed: "(helper)"
    label: "An exception to the additional tax on early distributions is entered"
    type: Bool
    expr: {op: test, ne: [retirement.exception, {const: "none"}]}

  - id: retirement.h_exc_mismatch
    printed: "(helper)"
    label: "Consistency check: exception 01 or 06 (doesn't apply to IRAs) for an IRA, or exception 07, 08 or 09 (IRA distributions) for a plan"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          all:
            - {op: test, eq: [retirement.h_is_trad, {const: true}]}
            - op: test
              any:
                - {op: test, eq: [retirement.exception, {const: "e01"}]}
                - {op: test, eq: [retirement.exception, {const: "e06"}]}
        - op: test
          all:
            - {op: test, eq: [retirement.h_is_plan, {const: true}]}
            - op: test
              any:
                - {op: test, eq: [retirement.exception, {const: "e07"}]}
                - {op: test, eq: [retirement.exception, {const: "e08"}]}
                - {op: test, eq: [retirement.exception, {const: "e09"}]}

  - id: retirement.h_exc_capped
    printed: "(helper)"
    label: "Amount the exception covers, not more than the early distribution on line 1"
    type: NonNegDollars
    expr: {op: smaller_of, of: [retirement.exc_amount, retirement.l1]}

  - id: retirement.l2
    printed: "(helper)"
    label: "Early distributions from this distribution not subject to additional tax (Form 5329, line 2)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_code_excepted, {const: true}]}
          then: retirement.l1
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.h_code_excepted, {const: false}]}
              - {op: test, eq: [retirement.h_has_exc, {const: true}]}
          then: retirement.h_exc_capped
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.h_code_excepted, {const: false}]}
              - {op: test, eq: [retirement.h_has_exc, {const: false}]}
          then: retirement.h_zero
    refuses:
      - retirement.early_screen
      - retirement.code_screen
      - {when: retirement.h_exc_mismatch, when_known: true}
    note: "With code 2 or 3 the exception is read as covering the whole distribution (a partial exception is refused by code_screen). This amount includes exceptions with dollar limits (05, 09, 19, 22, 23) before the per-person limits, which are applied at the person level from the l2_eNN amounts."

  - id: retirement.l2_s
    printed: "(helper)"
    label: "Part of line 2 for a code S SIMPLE IRA distribution"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "simple_S"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.code, {const: "simple_S"}]}
          then: retirement.h_zero

  - id: retirement.l2_e05
    printed: "(helper)"
    label: "Line 2 amount under exception 05 (unreimbursed medical expenses)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e05"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e05"}]}
          then: retirement.h_zero

  - id: retirement.l2_e09
    printed: "(helper)"
    label: "Line 2 amount under exception 09 (IRA distributions for the purchase of a first home, up to $10,000)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e09"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e09"}]}
          then: retirement.h_zero

  - id: retirement.l2_e19
    printed: "(helper)"
    label: "Line 2 amount under exception 19 (qualified birth or adoption distributions, up to $5,000)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e19"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e19"}]}
          then: retirement.h_zero

  - id: retirement.l2_e22
    printed: "(helper)"
    label: "Line 2 amount under exception 22 (qualified distributions to victims of domestic abuse)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e22"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e22"}]}
          then: retirement.h_zero

  - id: retirement.is_e23
    printed: "(helper)"
    label: "Exception 23 (eligible emergency personal expense distribution) is entered for this distribution"
    type: Bool
    expr: {op: test, eq: [retirement.exception, {const: "e23"}]}

  - id: retirement.l2_e23
    printed: "(helper)"
    label: "Line 2 amount under exception 23 (emergency personal expense distributions)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.is_e23, {const: true}]}
          then: retirement.l2
        - guard: {op: test, eq: [retirement.is_e23, {const: false}]}
          then: retirement.h_zero
```
```

#### Pass 3b3828e7c41f

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines retirement.has_rollover, retirement.taxable, retirement.amount_a, retirement.sav_amount, retirement.l1, retirement.l2, retirement.l2_e05, retirement.l2_e09, retirement.l2_e19, retirement.l2_e22, retirement.l2_e23, retirement.l1_s, retirement.l2_s, (SMW 1), (SMW 2), (SMW 4), (SMW 5), (SMW 6), (SMW 7), (SMW 8), (SMW 9), (SMW 10), (SMW 11) |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 3b3828e7c41f195bcb69dffda8dfd546904ebdc748ce347f1a11b92caf86721a |
| prompt policy | source-only-computation-v3+lines-v1 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 3db718b7f1b61a38e312f9e52d8600cf067d93aa8a65526122717921d0844206 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 5f8a4e6da6c3d74f05b1ccf24a7f0cdfa62ed2ea0297fec35205f1d43c3cd942 |
| receipt | .transcription/retirement.lines-fede9ff2eecc |
| printed lines compared | 23 |
| agree / disagree / missing | 0 / 23 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099r | 2025 (calendar-year form) | 5, 7, 9 | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | 5, 7, 9 | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| i1040gi | 2025; printed date 2026-02-25 | 26, 27, 28, 29, 30, 31 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 26, 27, 28, 30, 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i5329 | 2025 | 1, 2, 3, 5 | cited pages | bc85a048e4293ab244d68023ac7bb45333ceede0763b3b1cb3430eb4829a18bf | 1, 2, 3, 5 | e46adbf118d780a00b73957b6ef4c6e436e651f6f076a36fa9b6717bd138ee5d |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |
| p575 | None | 12, 16, 17, 21, 23, 24, 34, 35 | pages named by another document's citation | 4d6ee3802a2906a4633dcfc104aa33bb3d9ddedebddc9eadbd0393cfdb61e07b | 12, 16, 17, 21, 23, 24, 34, 35 | 3962801dde168fda9f4ee239245d9746b12e2d60bf358b25186ae4a57aa5b837 |
| p590b | 2025 | 5, 6, 28 | pages named by another document's citation | 24de404e77c2a3d1f0540b91ac8c28ca4d45c7fcf968de613407419eba9266f4 | 5, 6, 28 | 464639ba13341fe9c824b6f495922126cb3d158650887bf9beb265fd951c3e77 |
| p560 | For use in preparing 2025 returns | 18 | pages named by another document's citation | 38bbfa2efb2894e2527d66cd3478f33c6ceae4b777f78674c22bec16db9809aa | 18 | 7ef279c8f34addc2ff13420e35fab4a092bf8027f53907c28a5f46d2c21da737 |

##### Other documents in the catalog

Chosen from the source pages above (catalog_selection); refusal-gate inputs are in the screening list.

| reason | documents |
| --- | --- |
| definition | aqee, se, tax_on_amount, tcw |
| named form | clcw, clcw26, dependent, div, f8606, f8889, g28, household, interest, s1, s3, sa, sales, sb, sdtw, u1250 |
| named line | scveh, sli |
| shared page | f1040, f5329, f8880, ira, person, s2, scope, sd, ssb, w2 |

##### Raw second transcription

```yaml
```yaml
lines:
  - id: retirement.h_smw_used
    printed: "(helper)"
    label: "Simplified Method applies: a pension or annuity from a qualified plan with after-tax cost and an annuity starting date after November 18, 1996 (Simplified Method Worksheet—Lines 5a and 5b is completed)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.account, {const: "plan"}]}
        - {op: test, eq: [retirement.annuity, {const: true}]}

  - id: retirement.smw1
    printed: "(SMW 1)"
    label: "Enter the total pension or annuity payments from Form 1099-R, box 1. Also, enter this amount on Form 1040 or 1040-SR, line 5a"
    type: NonNegDollars
    expr: {op: copy, from: retirement.box1}
    shown_when: retirement.h_smw_used

  - id: retirement.smw2
    printed: "(SMW 2)"
    label: "Enter your cost in the plan at the annuity starting date"
    type: NonNegDollars
    expr: {op: copy, from: retirement.cost}
    shown_when: retirement.h_smw_used
    note: "The death benefit exclusion that 'Before you begin' adds to line 2 is screened out by retirement.special, so line 2 is the cost alone."

  - id: retirement.h_t1_360
    printed: "(helper)"
    label: "Line 2 divided by 360 (Table 1, age 55 or under, annuity starting date after November 18, 1996)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_360}}
  - id: retirement.h_t1_310
    printed: "(helper)"
    label: "Line 2 divided by 310 (Table 1, age 56–60)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_310}}
  - id: retirement.h_t1_260
    printed: "(helper)"
    label: "Line 2 divided by 260 (Table 1, age 61–65)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_260}}
  - id: retirement.h_t1_210
    printed: "(helper)"
    label: "Line 2 divided by 210 (Table 1, age 66–70)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_210}}
  - id: retirement.h_t1_160
    printed: "(helper)"
    label: "Line 2 divided by 160 (Table 1, age 71 or older)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_160}}
  - id: retirement.h_t2_410
    printed: "(helper)"
    label: "Line 2 divided by 410 (Table 2, combined ages 110 or under)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_410}}
  - id: retirement.h_t2_360
    printed: "(helper)"
    label: "Line 2 divided by 360 (Table 2, combined ages 111–120)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_360}}
  - id: retirement.h_t2_310
    printed: "(helper)"
    label: "Line 2 divided by 310 (Table 2, combined ages 121–130)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_310}}
  - id: retirement.h_t2_260
    printed: "(helper)"
    label: "Line 2 divided by 260 (Table 2, combined ages 131–140)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_260}}
  - id: retirement.h_t2_210
    printed: "(helper)"
    label: "Line 2 divided by 210 (Table 2, combined ages 141 or older)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_210}}

  - id: retirement.smw4
    printed: "(SMW 4)"
    label: "Divide line 2 by the number on line 3 (if you completed this worksheet last year, enter the amount from line 4 of last year's worksheet)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.used_last_year, {const: true}]}
          then: retirement.last_line4
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: false}]}
              - {op: test, le: [retirement.age, {const: 55, type: Count}]}
          then: retirement.h_t1_360
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: false}]}
              - {op: test, ge: [retirement.age, {const: 56, type: Count}]}
              - {op: test, le: [retirement.age, {const: 60, type: Count}]}
          then: retirement.h_t1_310
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: false}]}
              - {op: test, ge: [retirement.age, {const: 61, type: Count}]}
              - {op: test, le: [retirement.age, {const: 65, type: Count}]}
          then: retirement.h_t1_260
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: false}]}
              - {op: test, ge: [retirement.age, {const: 66, type: Count}]}
              - {op: test, le: [retirement.age, {const: 70, type: Count}]}
          then: retirement.h_t1_210
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: false}]}
              - {op: test, ge: [retirement.age, {const: 71, type: Count}]}
          then: retirement.h_t1_160
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: true}]}
              - {op: test, le: [retirement.combined_age, {const: 110, type: Count}]}
          then: retirement.h_t2_410
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: true}]}
              - {op: test, ge: [retirement.combined_age, {const: 111, type: Count}]}
              - {op: test, le: [retirement.combined_age, {const: 120, type: Count}]}
          then: retirement.h_t2_360
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: true}]}
              - {op: test, ge: [retirement.combined_age, {const: 121, type: Count}]}
              - {op: test, le: [retirement.combined_age, {const: 130, type: Count}]}
          then: retirement.h_t2_310
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: true}]}
              - {op: test, ge: [retirement.combined_age, {const: 131, type: Count}]}
              - {op: test, le: [retirement.combined_age, {const: 140, type: Count}]}
          then: retirement.h_t2_260
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: true}]}
              - {op: test, ge: [retirement.combined_age, {const: 141, type: Count}]}
          then: retirement.h_t2_210
    shown_when: retirement.h_smw_used
    note: "The worksheet does not say how to round the quotient on line 4; chosen: half-up to the cent (multiply_rate by 1/n). Only the 'after November 18, 1996' column of Table 1 is used, because earlier starting dates are screened out by retirement.annuity and retirement.special. Line 3 is folded into this choice."

  - id: retirement.smw5
    printed: "(SMW 5)"
    label: "Multiply line 4 by the number of months for which this year's payments were made"
    type: NonNegDollars
    expr: {op: multiply_count, amount: retirement.smw4, count: retirement.months}
    shown_when: retirement.h_smw_used
    note: "The instruction to skip lines 6 and 7 when the annuity starting date was before 1987 never applies, because retirement.annuity requires a starting date after November 18, 1996."

  - id: retirement.smw6
    printed: "(SMW 6)"
    label: "Enter the amount, if any, recovered tax free in years after 1986. If you completed this worksheet last year, enter the amount from line 10 of last year's worksheet"
    type: NonNegDollars
    expr: {op: copy, from: retirement.recovered}
    shown_when: retirement.h_smw_used

  - id: retirement.h_recovered_over
    printed: "(helper)"
    label: "Consistency check: the amount recovered tax free (line 6) is more than the cost (line 2)"
    type: Bool
    expr: {op: test, gt: [retirement.recovered, retirement.cost]}

  - id: retirement.smw7
    printed: "(SMW 7)"
    label: "Subtract line 6 from line 2"
    type: Dollars
    expr: {op: subtract, from: retirement.smw2, take: retirement.smw6}
    refuses:
      - {when: retirement.h_recovered_over, when_known: true}
    shown_when: retirement.h_smw_used

  - id: retirement.smw8
    printed: "(SMW 8)"
    label: "Enter the smaller of line 5 or line 7"
    type: Dollars
    expr: {op: smaller_of, of: [retirement.smw5, retirement.smw7]}
    shown_when: retirement.h_smw_used

  - id: retirement.smw9
    printed: "(SMW 9)"
    label: "Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero. Also, enter this amount on Form 1040 or 1040-SR, line 5b"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.smw1, take: retirement.smw8}
    shown_when: retirement.h_smw_used

  - id: retirement.smw10
    printed: "(SMW 10)"
    label: "Was your annuity starting date before 1987? No. Add lines 6 and 8. This is the amount you have recovered tax free through 2025"
    type: Dollars
    expr: {op: sum, of: [retirement.smw6, retirement.smw8]}
    shown_when: retirement.h_smw_used
    note: "The 'Yes. STOP' branch (starting date before 1987) cannot occur within the scope of retirement.annuity, so line 10 is always completed."

  - id: retirement.smw11
    printed: "(SMW 11)"
    label: "Balance of cost to be recovered. Subtract line 10 from line 2"
    type: Dollars
    expr: {op: subtract, from: retirement.smw2, take: retirement.smw10}
    shown_when: retirement.h_smw_used

  - id: retirement.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: retirement.has_rollover
    printed: "(helper)"
    label: "You rolled over part or all of the distribution (Exception 1; check box 1 on line 4c or 5c)"
    type: Bool
    expr: {op: test, gt: [retirement.rollover, {const: 0}]}

  - id: retirement.h_rollover_over
    printed: "(helper)"
    label: "Consistency check: the amount rolled over is more than the gross distribution in box 1"
    type: Bool
    expr: {op: test, gt: [retirement.rollover, retirement.box1]}

  - id: retirement.h_roth_refused
    printed: "(gate)"
    label: "Distribution from a Roth IRA without distribution code Q: see Form 8606 and its instructions to figure the amount for line 4b (Exception 2)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.account, {const: "roth_ira"}]}
        - {op: test, ne: [retirement.code, {const: "qualified_roth_Q"}]}

  - id: retirement.h_not_rolled
    printed: "(helper)"
    label: "The part of the distribution not rolled over (box 1 minus the amount rolled over, not less than zero)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.rollover}

  - id: retirement.h_plan_after5
    printed: "(helper)"
    label: "From the box 1 amount, subtract any contributions (usually shown in box 5) that were taxable to you when made"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.box5}

  - id: retirement.h_plan_taxable
    printed: "(helper)"
    label: "From that result, subtract the amount of the rollover. Enter the remaining amount on line 5b"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_plan_after5, take: retirement.rollover}
    note: "The Rollovers instruction (box 1 minus box 5 minus rollover) is also used for nonperiodic plan distributions that were not rolled over; with no box 5 amount this is the fully taxable box 1 amount. Pub. 575's allocation formula for a distribution before the annuity starting date is not applied; box 5 is read as the tax-free amount."

  - id: retirement.taxable
    printed: "(helper)"
    label: "Taxable amount of this distribution (Form 1040, line 4b or 5b)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.account, {const: "roth_ira"}]}
          then: retirement.h_zero
        - guard: {op: test, eq: [retirement.account, {const: "traditional_ira"}]}
          then: retirement.h_not_rolled
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.account, {const: "plan"}]}
              - {op: test, eq: [retirement.annuity, {const: true}]}
          then: retirement.smw9
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.account, {const: "plan"}]}
              - {op: test, eq: [retirement.annuity, {const: false}]}
          then: retirement.h_plan_taxable
    refuses:
      - retirement.special
      - retirement.h_roth_refused
      - {when: retirement.h_rollover_over, when_known: true}
    note: "Roth IRA with code Q: enter -0- (Exception 2(b)); other Roth IRA distributions are refused (Form 8606). Code T, which may also give -0-, falls under 'other' and is refused. Traditional IRA: the part not rolled over (Exception 1); the Exception 2 to 4 cases are screened by retirement.special."

  - id: retirement.h_partial
    printed: "(helper)"
    label: "Plan distribution that is not fully taxable (rollover, or contributions in box 5), so the total goes on line 5a"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.has_rollover, {const: true}]}
        - {op: test, gt: [retirement.box5, {const: 0}]}

  - id: retirement.amount_a
    printed: "(helper)"
    label: "Total distribution entered on Form 1040, line 4a or 5a (no entry when the distribution is fully taxable)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.account, {const: "roth_ira"}]}
          then: retirement.box1
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.account, {const: "traditional_ira"}]}
              - {op: test, eq: [retirement.has_rollover, {const: true}]}
          then: retirement.box1
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.account, {const: "traditional_ira"}]}
              - {op: test, eq: [retirement.has_rollover, {const: false}]}
          then: retirement.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.account, {const: "plan"}]}
              - {op: test, eq: [retirement.annuity, {const: true}]}
          then: retirement.smw1
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.account, {const: "plan"}]}
              - {op: test, eq: [retirement.annuity, {const: false}]}
              - {op: test, eq: [retirement.h_partial, {const: true}]}
          then: retirement.box1
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.account, {const: "plan"}]}
              - {op: test, eq: [retirement.annuity, {const: false}]}
              - {op: test, eq: [retirement.h_partial, {const: false}]}
          then: retirement.h_zero
    refuses:
      - retirement.special
    note: "Lump-sum distributions ('Enter the total distribution on line 5a') cannot be identified from the inputs (box 2b is not supplied); a fully taxable plan distribution without rollover or box 5 amount is treated as having no line 5a entry."

  - id: retirement.sav_amount
    printed: "(helper)"
    label: "Distribution counted on Form 8880, line 4 (excluding distributions not taxable as the result of a rollover, section 404(k) dividends, military retirement plan distributions, and inherited IRA distributions to a nonspousal beneficiary)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            any:
              - {op: test, eq: [retirement.sav_military, {const: true}]}
              - {op: test, eq: [retirement.sav_404k, {const: true}]}
              - {op: test, eq: [retirement.sav_inherited, {const: true}]}
          then: retirement.h_zero
        - guard:
            op: test
            not:
              op: test
              any:
                - {op: test, eq: [retirement.sav_military, {const: true}]}
                - {op: test, eq: [retirement.sav_404k, {const: true}]}
                - {op: test, eq: [retirement.sav_inherited, {const: true}]}
          then: retirement.h_not_rolled
    refuses:
      - retirement.special

  - id: retirement.h_early
    printed: "(helper)"
    label: "Early distribution (box 7 code 1, 2, 3 or S)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.code, {const: "early_1"}]}
        - {op: test, eq: [retirement.code, {const: "early_exception_2"}]}
        - {op: test, eq: [retirement.code, {const: "disability_3"}]}
        - {op: test, eq: [retirement.code, {const: "simple_S"}]}

  - id: retirement.h_payer_exc
    printed: "(helper)"
    label: "Box 7 shows that an exception applies (code 2, or code 3 disability)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.code, {const: "early_exception_2"}]}
        - {op: test, eq: [retirement.code, {const: "disability_3"}]}

  - id: retirement.h_other_code
    printed: "(gate)"
    label: "Box 7 shows another code or two codes; whether the distribution is an early distribution cannot be determined"
    type: Bool
    expr: {op: test, eq: [retirement.code, {const: "other"}]}

  - id: retirement.l1
    printed: "(helper)"
    label: "Early distributions includible in income (Form 5329, line 1) from this distribution"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_early, {const: true}]}
          then: retirement.taxable
        - guard: {op: test, eq: [retirement.h_early, {const: false}]}
          then: retirement.h_zero
    refuses:
      - retirement.early_screen
      - retirement.code_screen
      - retirement.h_other_code
    note: "Codes 1, 2, 3 and S are treated as early distributions. Codes 4 (death), 7, G and Q are not. Code 'other' cannot be classified from the inputs, so it is refused here."

  - id: retirement.h_has_exc
    printed: "(helper)"
    label: "An exception number (01–23) is entered for this distribution"
    type: Bool
    expr: {op: test, ne: [retirement.exception, {const: "none"}]}

  - id: retirement.h_exc_covered
    printed: "(helper)"
    label: "Amount the exception covers, not more than the early distribution on line 1"
    type: NonNegDollars
    expr: {op: smaller_of, of: [retirement.exc_amount, retirement.l1]}

  - id: retirement.l2
    printed: "(helper)"
    label: "Early distributions not subject to additional tax (Form 5329, line 2) from this distribution, before the per-person dollar limits"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_early, {const: false}]}
          then: retirement.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.h_early, {const: true}]}
              - {op: test, eq: [retirement.h_payer_exc, {const: true}]}
          then: retirement.l1
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.h_early, {const: true}]}
              - {op: test, eq: [retirement.h_payer_exc, {const: false}]}
              - {op: test, eq: [retirement.h_has_exc, {const: true}]}
          then: retirement.h_exc_covered
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.h_early, {const: true}]}
              - {op: test, eq: [retirement.h_payer_exc, {const: false}]}
              - {op: test, eq: [retirement.h_has_exc, {const: false}]}
          then: retirement.h_zero
    note: "Open: whether l2 holds all exceptions or only those without a dollar limit. Chosen: l2 is the whole entry-level exclusion before per-person limits, and l2_eNN gives the part under each capped exception. For codes 2 and 3 the payer's exception covers the whole line 1 amount (partial coverage is refused by code_screen), and no capped-exception split is made."

  - id: retirement.l2_e05
    printed: "(helper)"
    label: "Part of line 2 under exception 05 (medical expenses)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.h_early, {const: true}]}
              - {op: test, eq: [retirement.h_payer_exc, {const: false}]}
              - {op: test, eq: [retirement.exception, {const: "e05"}]}
          then: retirement.h_exc_covered
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [retirement.h_early, {const: true}]}
                - {op: test, eq: [retirement.h_payer_exc, {const: false}]}
                - {op: test, eq: [retirement.exception, {const: "e05"}]}
          then: retirement.h_zero

  - id: retirement.l2_e09
    printed: "(helper)"
    label: "Part of line 2 under exception 09 (first home, up to $10,000)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.h_early, {const: true}]}
              - {op: test, eq: [retirement.h_payer_exc, {const: false}]}
              - {op: test, eq: [retirement.exception, {const: "e09"}]}
          then: retirement.h_exc_covered
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [retirement.h_early, {const: true}]}
                - {op: test, eq: [retirement.h_payer_exc, {const: false}]}
                - {op: test, eq: [retirement.exception, {const: "e09"}]}
          then: retirement.h_zero

  - id: retirement.l2_e19
    printed: "(helper)"
    label: "Part of line 2 under exception 19 (qualified birth or adoption, up to $5,000)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.h_early, {const: true}]}
              - {op: test, eq: [retirement.h_payer_exc, {const: false}]}
              - {op: test, eq: [retirement.exception, {const: "e19"}]}
          then: retirement.h_exc_covered
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [retirement.h_early, {const: true}]}
                - {op: test, eq: [retirement.h_payer_exc, {const: false}]}
                - {op: test, eq: [retirement.exception, {const: "e19"}]}
          then: retirement.h_zero

  - id: retirement.l2_e22
    printed: "(helper)"
    label: "Part of line 2 under exception 22 (victims of domestic abuse)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.h_early, {const: true}]}
              - {op: test, eq: [retirement.h_payer_exc, {const: false}]}
              - {op: test, eq: [retirement.exception, {const: "e22"}]}
          then: retirement.h_exc_covered
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [retirement.h_early, {const: true}]}
                - {op: test, eq: [retirement.h_payer_exc, {const: false}]}
                - {op: test, eq: [retirement.exception, {const: "e22"}]}
          then: retirement.h_zero

  - id: retirement.l2_e23
    printed: "(helper)"
    label: "Part of line 2 under exception 23 (emergency personal expense distributions)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.h_early, {const: true}]}
              - {op: test, eq: [retirement.h_payer_exc, {const: false}]}
              - {op: test, eq: [retirement.exception, {const: "e23"}]}
          then: retirement.h_exc_covered
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, eq: [retirement.h_early, {const: true}]}
                - {op: test, eq: [retirement.h_payer_exc, {const: false}]}
                - {op: test, eq: [retirement.exception, {const: "e23"}]}
          then: retirement.h_zero

  - id: retirement.l1_s
    printed: "(helper)"
    label: "Part of line 1 that is a distribution from a SIMPLE IRA within 2 years of first participating (code S; 25% instead of 10%)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "simple_S"}]}
          then: retirement.l1
        - guard: {op: test, ne: [retirement.code, {const: "simple_S"}]}
          then: retirement.h_zero

  - id: retirement.l2_s
    printed: "(helper)"
    label: "Part of line 2 that is from a code S SIMPLE IRA distribution"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "simple_S"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.code, {const: "simple_S"}]}
          then: retirement.h_zero
```
```

## Raw second transcription

```yaml
```yaml
lines:
  - id: retirement.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: retirement.h_smw
    printed: "(helper)"
    label: "The Simplified Method Worksheet is used for this distribution (a pension or annuity from a qualified plan, section 403(b) plan or tax-sheltered annuity with an annuity starting date after November 18, 1996, under age 75 or fewer than 5 years of guaranteed payments)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.annuity, {const: true}]}
        - {op: test, eq: [retirement.account, {const: "plan"}]}
    note: "The annuity question is about a qualified plan, section 403(b) plan or tax-sheltered annuity. A Yes for an IRA entry is treated as inconsistent, so the worksheet is used only for account = plan."

  - id: retirement.smw1
    printed: "(SMW 1)"
    label: "Enter the total pension or annuity payments from Form 1099-R, box 1. Also, enter this amount on Form 1040 or 1040-SR, line 5a"
    type: NonNegDollars
    expr: {op: copy, from: retirement.box1}
    shown_when: retirement.h_smw

  - id: retirement.smw2
    printed: "(SMW 2)"
    label: "Enter your cost in the plan at the annuity starting date"
    type: NonNegDollars
    expr: {op: copy, from: retirement.cost}
    shown_when: retirement.h_smw
    note: "The death benefit exclusion that 'Before you begin' adds to line 2 is screened out by retirement.special, so line 2 is the cost alone."

  - id: retirement.h_t1_360
    printed: "(helper)"
    label: "Line 2 divided by 360 (Table 1, age 55 or under, annuity starting date after November 18, 1996)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_360}}
    note: "The IRS text does not say how to round the quotient on line 4. The quotient is rounded half-up to the cent."

  - id: retirement.h_t1_310
    printed: "(helper)"
    label: "Line 2 divided by 310 (Table 1, age 56-60)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_310}}

  - id: retirement.h_t1_260
    printed: "(helper)"
    label: "Line 2 divided by 260 (Table 1, age 61-65)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_260}}

  - id: retirement.h_t1_210
    printed: "(helper)"
    label: "Line 2 divided by 210 (Table 1, age 66-70)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_210}}

  - id: retirement.h_t1_160
    printed: "(helper)"
    label: "Line 2 divided by 160 (Table 1, age 71 or older)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_160}}

  - id: retirement.h_t2_410
    printed: "(helper)"
    label: "Line 2 divided by 410 (Table 2, combined ages 110 or under)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_410}}

  - id: retirement.h_t2_360
    printed: "(helper)"
    label: "Line 2 divided by 360 (Table 2, combined ages 111-120)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_360}}

  - id: retirement.h_t2_310
    printed: "(helper)"
    label: "Line 2 divided by 310 (Table 2, combined ages 121-130)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_310}}

  - id: retirement.h_t2_260
    printed: "(helper)"
    label: "Line 2 divided by 260 (Table 2, combined ages 131-140)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_260}}

  - id: retirement.h_t2_210
    printed: "(helper)"
    label: "Line 2 divided by 210 (Table 2, combined ages 141 or older)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_210}}

  - id: retirement.h_t1
    printed: "(helper)"
    label: "Line 2 divided by the number from Table 1 (annuity starting date after November 18, 1996)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [retirement.age, {const: 55, type: Count}]}
          then: retirement.h_t1_360
        - guard:
            op: test
            all:
              - {op: test, gt: [retirement.age, {const: 55, type: Count}]}
              - {op: test, le: [retirement.age, {const: 60, type: Count}]}
          then: retirement.h_t1_310
        - guard:
            op: test
            all:
              - {op: test, gt: [retirement.age, {const: 60, type: Count}]}
              - {op: test, le: [retirement.age, {const: 65, type: Count}]}
          then: retirement.h_t1_260
        - guard:
            op: test
            all:
              - {op: test, gt: [retirement.age, {const: 65, type: Count}]}
              - {op: test, le: [retirement.age, {const: 70, type: Count}]}
          then: retirement.h_t1_210
        - guard: {op: test, gt: [retirement.age, {const: 70, type: Count}]}
          then: retirement.h_t1_160
    note: "Only the 'after November 18, 1996' column of Table 1 is reachable. Annuity starting dates before November 19, 1996 are screened out by retirement.special."

  - id: retirement.h_t2
    printed: "(helper)"
    label: "Line 2 divided by the number from Table 2 (combined ages)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [retirement.combined_age, {const: 110, type: Count}]}
          then: retirement.h_t2_410
        - guard:
            op: test
            all:
              - {op: test, gt: [retirement.combined_age, {const: 110, type: Count}]}
              - {op: test, le: [retirement.combined_age, {const: 120, type: Count}]}
          then: retirement.h_t2_360
        - guard:
            op: test
            all:
              - {op: test, gt: [retirement.combined_age, {const: 120, type: Count}]}
              - {op: test, le: [retirement.combined_age, {const: 130, type: Count}]}
          then: retirement.h_t2_310
        - guard:
            op: test
            all:
              - {op: test, gt: [retirement.combined_age, {const: 130, type: Count}]}
              - {op: test, le: [retirement.combined_age, {const: 140, type: Count}]}
          then: retirement.h_t2_260
        - guard: {op: test, gt: [retirement.combined_age, {const: 140, type: Count}]}
          then: retirement.h_t2_210

  - id: retirement.smw4
    printed: "(SMW 4)"
    label: "Divide line 2 by the number on line 3 (if you completed this worksheet last year, enter the amount from line 4 of last year's worksheet)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.used_last_year, {const: true}]}
          then: retirement.last_line4
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: true}]}
          then: retirement.h_t2
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: false}]}
          then: retirement.h_t1
    shown_when: retirement.h_smw
    note: "Line 3 (the table number) is not a requested line. A choose cannot return a number, so line 3 is folded into the table-specific quotients."

  - id: retirement.h_months_bad
    printed: "(helper)"
    label: "Consistency check: more than 12 months of payments entered for 2025"
    type: Bool
    expr: {op: test, gt: [retirement.months, {const: 12, type: Count}]}

  - id: retirement.smw5
    printed: "(SMW 5)"
    label: "Multiply line 4 by the number of months for which this year's payments were made"
    type: NonNegDollars
    expr: {op: multiply_count, amount: retirement.smw4, count: retirement.months}
    refuses:
      - {when: retirement.h_months_bad, when_known: true}
    shown_when: retirement.h_smw
    note: "The 'annuity starting date before 1987' branch (skip lines 6 and 7) is outside scope. Such dates are screened out by retirement.special and the annuity question."

  - id: retirement.smw6
    printed: "(SMW 6)"
    label: "Enter the amount, if any, recovered tax free in years after 1986. If you completed this worksheet last year, enter the amount from line 10 of last year's worksheet"
    type: NonNegDollars
    expr: {op: copy, from: retirement.recovered}
    shown_when: retirement.h_smw

  - id: retirement.smw7
    printed: "(SMW 7)"
    label: "Subtract line 6 from line 2"
    type: Dollars
    expr: {op: subtract, from: retirement.smw2, take: retirement.smw6}
    shown_when: retirement.h_smw

  - id: retirement.smw8
    printed: "(SMW 8)"
    label: "Enter the smaller of line 5 or line 7"
    type: Dollars
    expr: {op: smaller_of, of: [retirement.smw5, retirement.smw7]}
    shown_when: retirement.h_smw

  - id: retirement.smw9
    printed: "(SMW 9)"
    label: "Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero. Also, enter this amount on Form 1040 or 1040-SR, line 5b"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.smw1, take: retirement.smw8}
    shown_when: retirement.h_smw

  - id: retirement.smw10
    printed: "(SMW 10)"
    label: "Add lines 6 and 8. This is the amount you have recovered tax free through 2025"
    type: Dollars
    expr: {op: sum, of: [retirement.smw6, retirement.smw8]}
    shown_when: retirement.h_smw

  - id: retirement.smw11
    printed: "(SMW 11)"
    label: "Balance of cost to be recovered. Subtract line 10 from line 2"
    type: Dollars
    expr: {op: subtract, from: retirement.smw2, take: retirement.smw10}
    shown_when: retirement.h_smw

  - id: retirement.one
    printed: "(helper)"
    label: "One (this Form 1099-R distribution, counted once)"
    type: Count
    expr: {op: param, ref: person.one}
    note: "The IRS pages do not define this interface. It is read as the constant count 1 per entry, used to count distributions such as rollovers."

  - id: retirement.is_ira
    printed: "(helper)"
    label: "This distribution is from an IRA (reported on lines 4a and 4b) rather than a pension or annuity (lines 5a and 5b)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.account, {const: "traditional_ira"}]}
        - {op: test, eq: [retirement.account, {const: "roth_ira"}]}

  - id: retirement.h_rolled
    printed: "(helper)"
    label: "Amount rolled over (the whole distribution for a direct rollover, code G)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
          then: retirement.box1
        - guard: {op: test, ne: [retirement.code, {const: "direct_rollover_G"}]}
          then: retirement.rollover

  - id: retirement.h_rollover_bad
    printed: "(helper)"
    label: "Consistency check: amount rolled over is more than the gross distribution"
    type: Bool
    expr: {op: test, gt: [retirement.rollover, retirement.box1]}

  - id: retirement.has_rollover
    printed: "(helper)"
    label: "Part or all of the distribution was rolled over (check box 1 on line 4c or 5c)"
    type: Bool
    expr: {op: test, gt: [retirement.h_rolled, {const: 0}]}

  - id: retirement.h_unsupported_code
    printed: "(helper)"
    label: "Distribution this tool does not compute: a Roth IRA distribution without code Q (Form 8606), or a plan distribution with code Q"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          all:
            - {op: test, eq: [retirement.account, {const: "roth_ira"}]}
            - {op: test, ne: [retirement.code, {const: "qualified_roth_Q"}]}
        - op: test
          all:
            - {op: test, eq: [retirement.account, {const: "plan"}]}
            - {op: test, eq: [retirement.code, {const: "qualified_roth_Q"}]}
    note: "Exception 2 sends Roth IRA distributions to Form 8606 unless code Q (or code T in a case that cannot be confirmed here). The supplied text gives no treatment for a qualified designated Roth account distribution (code Q from a plan), so both cases are refused."

  - id: retirement.h_ira_taxable
    printed: "(helper)"
    label: "Traditional IRA: the part not rolled over"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.h_rolled}

  - id: retirement.h_plan_after5
    printed: "(helper)"
    label: "Pension: box 1 minus contributions taxable when made (box 5)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.box5}

  - id: retirement.h_plan_taxable
    printed: "(helper)"
    label: "Pension not under the Simplified Method: box 1 minus box 5 minus the amount rolled over"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_plan_after5, take: retirement.h_rolled}
    note: "The Rollovers instruction subtracts box 5 and then the rollover. The same box 5 subtraction is applied when there is no rollover. A box-5 amount on a non-annuity distribution under the General Rule is screened out by retirement.special."

  - id: retirement.taxable
    printed: "(helper)"
    label: "Taxable amount of this distribution (Form 1040 line 4b or 5b)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.account, {const: "roth_ira"}]}
          then: retirement.h_zero
        - guard: {op: test, eq: [retirement.account, {const: "traditional_ira"}]}
          then: retirement.h_ira_taxable
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.account, {const: "plan"}]}
              - {op: test, eq: [retirement.h_smw, {const: true}]}
          then: retirement.smw9
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.account, {const: "plan"}]}
              - {op: test, eq: [retirement.h_smw, {const: false}]}
          then: retirement.h_plan_taxable
    refuses:
      - retirement.special
      - retirement.h_unsupported_code
      - {when: retirement.h_rollover_bad, when_known: true}
    note: "A Roth IRA distribution reaches zero only with code Q (Exception 2(b)); other Roth codes are refused. Under the Simplified Method any rollover entry is disregarded, because periodic annuity payments are taken from SMW line 9."

  - id: retirement.h_on_line_a
    printed: "(helper)"
    label: "The total distribution is entered on line 4a or 5a (rollover, Roth IRA, or partially taxable pension)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.account, {const: "roth_ira"}]}
        - {op: test, eq: [retirement.has_rollover, {const: true}]}
        - {op: test, eq: [retirement.h_smw, {const: true}]}
        - op: test
          all:
            - {op: test, eq: [retirement.account, {const: "plan"}]}
            - {op: test, gt: [retirement.box5, {const: 0}]}

  - id: retirement.amount_a
    printed: "(helper)"
    label: "Amount of this distribution entered on Form 1040 line 4a or 5a"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_on_line_a, {const: true}]}
          then: retirement.box1
        - guard: {op: test, eq: [retirement.h_on_line_a, {const: false}]}
          then: retirement.h_zero
    refuses:
      - retirement.special
    note: "A fully taxable distribution goes only on line 4b or 5b ('don't make an entry on line 4a/5a'). This is read per distribution: a fully taxable distribution adds nothing to line 4a or 5a even when other distributions are reported there."

  - id: retirement.h_not_rolled
    printed: "(helper)"
    label: "Distribution not rolled over"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.h_rolled}

  - id: retirement.sav_amount
    printed: "(helper)"
    label: "Amount of this distribution counted on Form 8880, line 4"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            any:
              - {op: test, eq: [retirement.sav_military, {const: true}]}
              - {op: test, eq: [retirement.sav_404k, {const: true}]}
              - {op: test, eq: [retirement.sav_inherited, {const: true}]}
          then: retirement.h_zero
        - guard:
            op: test
            not:
              op: test
              any:
                - {op: test, eq: [retirement.sav_military, {const: true}]}
                - {op: test, eq: [retirement.sav_404k, {const: true}]}
                - {op: test, eq: [retirement.sav_inherited, {const: true}]}
          then: retirement.h_not_rolled
    refuses:
      - retirement.special
      - {when: retirement.h_rollover_bad, when_known: true}
    note: "Distributions not taxable as the result of a rollover are excluded. Roth conversions, plan loans treated as distributions, distributions of excess contributions and returned contributions are screened out by retirement.special."

  - id: retirement.h_early
    printed: "(helper)"
    label: "Box 7 shows an early or disability distribution (code 1, 2, 3 or S)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.code, {const: "early_1"}]}
        - {op: test, eq: [retirement.code, {const: "early_exception_2"}]}
        - {op: test, eq: [retirement.code, {const: "simple_S"}]}
        - {op: test, eq: [retirement.code, {const: "disability_3"}]}
    note: "Code 3 (disability) is treated as an early distribution whose exception (03) covers it entirely, the same way as code 2."

  - id: retirement.h_code_other
    printed: "(helper)"
    label: "Box 7 shows another code or two codes, so it cannot be determined whether this is an early distribution"
    type: Bool
    expr: {op: test, eq: [retirement.code, {const: "other"}]}
    note: "The text does not let the tool tell whether an 'other' code (for example two codes) marks an early distribution, so Form 5329 line 1 is refused for it."

  - id: retirement.l1
    printed: "(helper)"
    label: "Early distributions includible in income (Form 5329, line 1) from this distribution"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_early, {const: true}]}
          then: retirement.taxable
        - guard: {op: test, eq: [retirement.h_early, {const: false}]}
          then: retirement.h_zero
    refuses:
      - retirement.early_screen
      - retirement.code_screen
      - retirement.h_code_other

  - id: retirement.h_exc_capped
    printed: "(helper)"
    label: "Amount the exception covers, not more than the early distribution included on line 1"
    type: NonNegDollars
    expr: {op: smaller_of, of: [retirement.exc_amount, retirement.l1]}

  - id: retirement.h_l2_user
    printed: "(helper)"
    label: "Line 2 amount from the exception you entered (codes 1 and S)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "none"}]}
          then: retirement.h_zero
        - guard: {op: test, ne: [retirement.exception, {const: "none"}]}
          then: retirement.h_exc_capped

  - id: retirement.l2
    printed: "(helper)"
    label: "Early distributions not subject to the additional tax (Form 5329, line 2) from this distribution, before the per-person dollar limits"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            any:
              - {op: test, eq: [retirement.code, {const: "early_exception_2"}]}
              - {op: test, eq: [retirement.code, {const: "disability_3"}]}
          then: retirement.l1
        - guard:
            op: test
            not:
              op: test
              any:
                - {op: test, eq: [retirement.code, {const: "early_exception_2"}]}
                - {op: test, eq: [retirement.code, {const: "disability_3"}]}
          then: retirement.h_l2_user
    refuses:
      - retirement.early_screen
      - retirement.code_screen
    note: "For codes 2 and 3, box 7 indicates an exception, and partial coverage is refused by code_screen, so the whole line 1 amount is excepted. For codes 1 and S, the amount is the entered exception amount (exception 12: the part received at age 59 1/2 or older), capped at line 1. The dollar limits for 05, 09, 19, 22 and 23 are applied per person outside this entry."

  - id: retirement.l2_e05
    printed: "(helper)"
    label: "Line 2 amount under exception 05 (medical expenses)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e05"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e05"}]}
          then: retirement.h_zero

  - id: retirement.l2_e09
    printed: "(helper)"
    label: "Line 2 amount under exception 09 (first home, up to $10,000)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e09"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e09"}]}
          then: retirement.h_zero

  - id: retirement.l2_e19
    printed: "(helper)"
    label: "Line 2 amount under exception 19 (qualified birth or adoption, up to $5,000)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e19"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e19"}]}
          then: retirement.h_zero

  - id: retirement.l2_e22
    printed: "(helper)"
    label: "Line 2 amount under exception 22 (victims of domestic abuse)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e22"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e22"}]}
          then: retirement.h_zero

  - id: retirement.is_e23
    printed: "(helper)"
    label: "This is an early distribution claimed as an emergency personal expense distribution (exception 23)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.exception, {const: "e23"}]}
        - {op: test, eq: [retirement.h_early, {const: true}]}

  - id: retirement.l2_e23
    printed: "(helper)"
    label: "Line 2 amount under exception 23 (emergency personal expense distributions)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e23"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e23"}]}
          then: retirement.h_zero

  - id: retirement.l1_s
    printed: "(helper)"
    label: "Line 1 amount from a SIMPLE IRA distribution within 2 years of first participation (code S, 25% rate)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "simple_S"}]}
          then: retirement.l1
        - guard: {op: test, ne: [retirement.code, {const: "simple_S"}]}
          then: retirement.h_zero

  - id: retirement.l2_s
    printed: "(helper)"
    label: "Line 2 amount from a SIMPLE IRA distribution within 2 years of first participation (code S)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "simple_S"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.code, {const: "simple_S"}]}
          then: retirement.h_zero
```
```
