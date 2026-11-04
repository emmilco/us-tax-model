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
{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}], "test": "any"}
```

Ruling: representation; i1040gi p. 27, Exception 1, "Enter the total distribution on line 4a if you rolled over part or all of the distribution"; i1040gi p. 30, "Use lines 5a and 5b to report a rollover, including a direct rollover". The reply is code G or an amount rolled over above zero; the project's is the same test (its rollover amount is box 1 for code G, but code G alone already makes it true). The refresh round's model error (a code G entry with $0 in box 1 not a rollover) is gone. Ruled from reading the pass reply (.transcription/retirement.lines-535357ae1261) against the project; triage was not rerun.
Reviewed in: pass 11db066e0fce

### retirement.taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}
```

Second transcription's note: A Roth IRA distribution reaches the -0- branch only with code Q (Exception 2, item 2(b)); any other Roth IRA distribution is refused.

Ruling: model error; i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025." As the earlier ruling of this round: for a plan annuity the reply always takes Simplified Method Worksheet line 9; the project takes box 1 when worksheet line 7 (cost less the amount recovered, signed) is zero or less and line 9 otherwise. Where the amount recovered exceeds the cost, line 7 is negative and line 9 exceeds box 1, so the reply overstates the taxable amount. The new reply also sends a code G annuity to line 9, but refuses it (h_annuity_rollover), as the project does (retirement.annuity_rollover). Elsewhere (plan without annuity: box 1 less box 5 less the rollover, the whole of box 1 for code G; traditional IRA: box 1 less the rollover; Roth IRA: zero, other than code Q refused) the reply is the project's. Ruled from the pass reply (.transcription/retirement.lines-37c350a27fd6) read against the project, with a scratch run of triage.mjs on that reply over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 2,243 agree; all 4 value differences have line 7 negative (fixture stage10.smw.recovered_exceeds_cost, $21,000 against $12,000; generated 43 r2, 229 r1 and 395 r2, the last with box 1 zero and line 9 $22,738.41); the rest are the project's cited refusals (bad_code, screen_refused) and unknowns on partial records, and 2 candidate refusals (h_annuity_rollover) on partial records the project cannot complete.
Reviewed in: pass 11db066e0fce

### retirement.amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"input": "retirement.box5"}, {"const": 0}], "test": "le"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.box5"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"input": "retirement.box1"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"input": "retirement.box1"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}], "test": "ne"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Second transcription's note: Open: 'More than one distribution' says to enter the total of the distributions on line 4a, while a fully taxable distribution makes no entry there. Chosen reading: this entry gives box 1 for a distribution that is not fully taxable and zero for one that is. Combining distributions is left to Form 1040.

Ruling: model error; i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a."; Partially Taxable Pensions and Annuities: "Enter the total pension or annuity payments (from Form 1099-R, box 1) on line 5a." The point of the earlier ruling in a new form: the reply now makes no line 5a entry when its taxable amount equals box 1 and enters box 1 otherwise, where the project tests the source's condition (cost left to recover, worksheet line 7 above zero). The reply errs both ways: with line 7 negative its taxable amount (line 9) exceeds box 1, so it enters box 1 for an annuity whose cost was recovered (fixture stage10.smw.recovered_exceeds_cost; generated 43 r2 and 229 r1); with cost left but worksheet line 8 zero (the prior year's line 4 answered as zero, so line 9 equals box 1) it makes no entry for a partially taxable annuity (generated 421 r1, $29,413.54, and 425 r2, $17,673.46). With line 7 exactly zero it now agrees (the earlier reply entered box 1 for every plan annuity). Rollovers, code G, Roth IRAs and box 5 amounts are as the project. Ruled from the pass reply (.transcription/retirement.lines-37c350a27fd6) read against the project, with a scratch run of triage.mjs on that reply over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 2,180 agree; the 5 value differences above; the rest are the project's cited refusals, unknowns on partial records, and records where the reply needs the answers of its taxable amount that the project's test does not read.
Reviewed in: pass 11db066e0fce

### retirement.sav_amount — This distribution's amount on Form 8880 line 4
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "eq"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; f8880 p. 2, Line 4, "Don’t include any of the following. • Distributions not taxable as the result of a rollover or a trustee-to- trustee transfer." As the earlier ruling of this round: values agree (box 1 less the rollover, the whole of box 1 for code G, so zero then; zero for the excluded kinds), but the reply tests retirement.sav_404k, sav_military and sav_inherited on every entry, where the project asks the first two only of plan entries and the third only of IRA entries. The new reply refuses only on retirement.special; the project's refusals come through retirement.rolled (special and the cited bad_code). Ruled from the pass reply (.transcription/retirement.lines-37c350a27fd6) read against the project, with a scratch run of triage.mjs on that reply over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 2,159 agree, no value difference; 81 candidate-unknown (the unasked Form 8880 answers), 2 candidate refusals on special where the project is unknown, the rest project refusals on its cited gates and unknowns on partial records.
Reviewed in: pass 11db066e0fce

### retirement.l1 — Form 5329 line 1 share: the taxable amount of an early distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}
```

Ruling: model error; i5329 p. 3, Line 1: "Enter the amount of early distributions includible in income (other than qualified disaster recovery distributions) that you received from:". The earlier ruling's ambiguity (amb.2025.f5329_line1_codes) no longer applies: the new reply puts codes 1 and S only on line 1, the project's chosen reading. As the earlier ruling, it refuses on retirement.early_screen and retirement.code_screen for every entry, whatever the code (retirement.early_screen is asked only for code 1 and S entries, retirement.code_screen only for codes 2, 4 and 7, and retirement.exception only for code 1 and S entries (decision D3(a), the cited screens of retirement.screen_refused)). Its amount is its own taxable amount, so it carries the line 9 overstatement ruled on retirement.taxable (generated 43 r2, code 1 annuity with line 7 negative: $67,007.13 against $22,416.63). Ruled from the pass reply (.transcription/retirement.lines-37c350a27fd6) read against the project, with a scratch run of triage.mjs on that reply over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 1,815 agree; 591 candidate-unknown (the screen answers), the value difference above, 3 candidate refusals on partial records, 1 project refusal (cited bad_code, fixture stage21.refuse.bad_code_screen_unasked), 1 project-unknown.
Reviewed in: pass 11db066e0fce

### retirement.l2 — Form 5329 line 2 share before the per-person limits
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}
```

Second transcription's note: The dollar limits for exceptions 05, 09, 19, 22 and 23 are applied per person outside this entry, which is why those exceptions are also reported separately below.

Ruling: model error; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." The exception table: "Qualified retirement plan distributions (doesn’t apply to IRAs) you received after separation from service". The new reply drops the earlier reply's code 2 and 3 branch, so the earlier ruling's ambiguity no longer applies. As the earlier ruling, it refuses on retirement.early_screen and retirement.code_screen for every entry (retirement.early_screen is asked only for code 1 and S entries, retirement.code_screen only for codes 2, 4 and 7, and retirement.exception only for code 1 and S entries (decision D3(a), the cited screens of retirement.screen_refused)). New in this reply: it tests retirement.exception before the code, so it needs the exception answer on every entry; and it no longer checks the exception against the kind of account, so on fixture stage21.refuse.wrong_kind (exception 01 for a code 1 traditional IRA distribution) it excludes $3,000 where the project refuses (retirement.wrong_kind). Ruled from the pass reply (.transcription/retirement.lines-37c350a27fd6) read against the project, with a scratch run of triage.mjs on that reply over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 1,783 agree; 614 candidate-unknown, 13 candidate refusals on the screens (e.g. fixture stage21.refuse.early_screen, where the project's line is zero on a return it refuses), the wrong_kind record above, 1 project-unknown.
Reviewed in: pass 11db066e0fce

### retirement.l2_e05 — Line 2 share under exception 05
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." As the earlier ruling of this round: the reply tests retirement.exception before the code (exception 05 then line 2), so it needs the exception answer on every entry (retirement.early_screen is asked only for code 1 and S entries, retirement.code_screen only for codes 2, 4 and 7, and retirement.exception only for code 1 and S entries (decision D3(a), the cited screens of retirement.screen_refused)); and its line 2 refuses on the early and code screens for every entry. Values agree where both compute. Ruled from the pass reply (.transcription/retirement.lines-37c350a27fd6) read against the project, with a scratch run of triage.mjs on that reply over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 1,858 agree, no value difference; 554 candidate-unknown.
Reviewed in: pass 11db066e0fce

### retirement.l2_e09 — Line 2 share under exception 09
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." As the earlier ruling of this round: the reply tests retirement.exception before the code (exception 09 then line 2), so it needs the exception answer on every entry (retirement.early_screen is asked only for code 1 and S entries, retirement.code_screen only for codes 2, 4 and 7, and retirement.exception only for code 1 and S entries (decision D3(a), the cited screens of retirement.screen_refused)); and its line 2 refuses on the early and code screens for every entry. Values agree where both compute. Its line 2 no longer checks the kind of account, so exception 09, which the table limits to IRAs ("IRA distributions made for the purchase of a first home, up to $10,000"), would be counted for a plan distribution where the project refuses (retirement.wrong_kind); the sample has no such record. Ruled from the pass reply (.transcription/retirement.lines-37c350a27fd6) read against the project, with a scratch run of triage.mjs on that reply over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 1,856 agree, no value difference; 556 candidate-unknown.
Reviewed in: pass 11db066e0fce

### retirement.l2_e19 — Line 2 share under exception 19
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." As the earlier ruling of this round: the reply tests retirement.exception before the code (exception 19 then line 2), so it needs the exception answer on every entry (retirement.early_screen is asked only for code 1 and S entries, retirement.code_screen only for codes 2, 4 and 7, and retirement.exception only for code 1 and S entries (decision D3(a), the cited screens of retirement.screen_refused)); and its line 2 refuses on the early and code screens for every entry. Values agree where both compute. Ruled from the pass reply (.transcription/retirement.lines-37c350a27fd6) read against the project, with a scratch run of triage.mjs on that reply over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 1,858 agree, no value difference; 554 candidate-unknown.
Reviewed in: pass 11db066e0fce

### retirement.l2_e22 — Line 2 share under exception 22
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." As the earlier ruling of this round: the reply tests retirement.exception before the code (exception 22 then line 2), so it needs the exception answer on every entry (retirement.early_screen is asked only for code 1 and S entries, retirement.code_screen only for codes 2, 4 and 7, and retirement.exception only for code 1 and S entries (decision D3(a), the cited screens of retirement.screen_refused)); and its line 2 refuses on the early and code screens for every entry. Values agree where both compute. Ruled from the pass reply (.transcription/retirement.lines-37c350a27fd6) read against the project, with a scratch run of triage.mjs on that reply over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 1,858 agree, no value difference; 553 candidate-unknown but 1 project-unknown.
Reviewed in: pass 11db066e0fce

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
{"alternatives": [{"guard": {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." As the earlier ruling of this round: the reply tests retirement.exception before the code (exception 23 then line 2), so it needs the exception answer on every entry (retirement.early_screen is asked only for code 1 and S entries, retirement.code_screen only for codes 2, 4 and 7, and retirement.exception only for code 1 and S entries (decision D3(a), the cited screens of retirement.screen_refused)); and its line 2 refuses on the early and code screens for every entry. Values agree where both compute. Ruled from the pass reply (.transcription/retirement.lines-37c350a27fd6) read against the project, with a scratch run of triage.mjs on that reply over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 1,858 agree, no value difference; 554 candidate-unknown.
Reviewed in: pass 11db066e0fce

### retirement.l1_s — Line 1 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: scope; i5329 p. 5, Line 4: "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%." As the earlier ruling of this round: for a code S entry the reply's share is its line 1, the taxable amount, as the project's; for other codes zero. Ruled from the pass reply (.transcription/retirement.lines-37c350a27fd6) read against the project, with a scratch run of triage.mjs on that reply over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 2,411 agree; the one difference is the project's cited retirement.bad_code refusal (fixture stage21.refuse.bad_code_screen_unasked, code S from a plan), where the reply's line 1 lacks retirement.early_screen. The reply's line 1 screen refusals are ruled on retirement.l1.
Reviewed in: pass 11db066e0fce

### retirement.l2_s — Line 2 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: scope; i5329 p. 5, Line 4 (25% for code S in the first 2 years); i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." As the earlier ruling of this round: for a code S entry the reply's share is its line 2 (the smaller of the excepted amount and line 1), the project's; for other codes zero. Ruled from the pass reply (.transcription/retirement.lines-37c350a27fd6) read against the project, with a scratch run of triage.mjs on that reply over the project's other lines (1,578 fixtures, 500 generated returns seed 20261026, 1,080 partial records; 2,412 comparisons per line): 2,411 agree; the one difference is candidate-unknown on fixture stage21.refuse.bad_code_screen_unasked, a return the project refuses (retirement.bad_code, code S from a plan). The reply's line 2 needs are ruled on retirement.l2.
Reviewed in: pass 11db066e0fce

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

Ruling: model error; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`, written by triage.py this round; 1,565 fixtures, 500 generated returns seed 20261026, 999 partial records from 40 bases; 2,160 comparisons): 705 agree; 1,358 candidate-shows-skipped, 52 candidate-unknown, 45 project-unknown (on completed returns: 135 candidate-shows-skipped, 2 candidate-unknown). The reply now declares shown_when plan and annuity, the project plan, annuity and worksheet line 7 above zero (retirement.smw_shown, BUG-0207/0208). By reading, the reply hides the worksheet wherever the project does except for a plan annuity with no cost left, where i1040gi p. 28 makes the payments fully taxable and the worksheet is not used ("Your payments are fully taxable if (a) you didn’t contribute to the cost ... or (b) you got your entire cost back tax free before 2025"); showing it there is the reply's defect (generated 395 r2 in the earlier rounds). triage applies only the project's shown_when (tools/transcription/triage.mjs), so its candidate-shows-skipped and candidate-unknown counts on IRA and non-annuity plan entries are values the reply's own shown_when hides. The value expression is the project's. Project stands.

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

Ruling: model error; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`, written by triage.py this round; 1,565 fixtures, 500 generated returns seed 20261026, 999 partial records from 40 bases; 2,160 comparisons): 1,674 agree; 415 candidate-unknown, 43 candidate-shows-skipped, 28 project-unknown (on completed returns: 1 candidate-shows-skipped, 19 candidate-unknown). The reply now declares shown_when plan and annuity, the project plan, annuity and worksheet line 7 above zero (retirement.smw_shown, BUG-0207/0208). By reading, the reply hides the worksheet wherever the project does except for a plan annuity with no cost left, where i1040gi p. 28 makes the payments fully taxable and the worksheet is not used ("Your payments are fully taxable if (a) you didn’t contribute to the cost ... or (b) you got your entire cost back tax free before 2025"); showing it there is the reply's defect (generated 395 r2 in the earlier rounds). triage applies only the project's shown_when (tools/transcription/triage.mjs), so its candidate-shows-skipped and candidate-unknown counts on IRA and non-annuity plan entries are values the reply's own shown_when hides. The value expression is the project's. Project stands.

### (SMW 4) — Divide line 2 by the number on line 3 (or, if you completed this worksheet last year, line
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 56, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_360"}}}, {"guard": {"args": [{"args": [{"const": 56, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 61, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_310"}}}, {"guard": {"args": [{"args": [{"const": 61, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 66, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_260"}}}, {"guard": {"args": [{"args": [{"const": 66, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 71, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_210"}}}, {"guard": {"args": [{"const": 71, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_160"}}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 111, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_410"}}}, {"guard": {"args": [{"args": [{"const": 111, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 121, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_360"}}}, {"guard": {"args": [{"args": [{"const": 121, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 131, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_310"}}}, {"guard": {"args": [{"args": [{"const": 131, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 141, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_260"}}}, {"guard": {"args": [{"const": 141, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_210"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"input": "retirement.last_line4"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "retirement.age"}, {"const": 60, "type": "Count"}], "test": "le"}, {"args": [{"const": 55, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_310"}}}, {"guard": {"args": [{"args": [{"input": "retirement.age"}, {"const": 65, "type": "Count"}], "test": "le"}, {"args": [{"const": 60, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_260"}}}, {"guard": {"args": [{"args": [{"input": "retirement.age"}, {"const": 70, "type": "Count"}], "test": "le"}, {"args": [{"const": 65, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_210"}}}, {"guard": {"args": [{"input": "retirement.age"}, {"const": 55, "type": "Count"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_360"}}}, {"guard": {"args": [{"const": 70, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_160"}}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "retirement.combined_age"}, {"const": 120, "type": "Count"}], "test": "le"}, {"args": [{"const": 110, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_360"}}}, {"guard": {"args": [{"args": [{"input": "retirement.combined_age"}, {"const": 130, "type": "Count"}], "test": "le"}, {"args": [{"const": 120, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_310"}}}, {"guard": {"args": [{"args": [{"input": "retirement.combined_age"}, {"const": 140, "type": "Count"}], "test": "le"}, {"args": [{"const": 130, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_260"}}}, {"guard": {"args": [{"input": "retirement.combined_age"}, {"const": 110, "type": "Count"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_410"}}}, {"guard": {"args": [{"const": 140, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_210"}}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"input": "retirement.last_line4"}}], "op": "choose"}
```

Second transcription's note: Line 3 (the table number) is not a requested line. A choose cannot return a number, so line 3 is folded into the table-specific quotients.

Ruling: model error; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`, written by triage.py this round; 1,565 fixtures, 500 generated returns seed 20261026, 999 partial records from 40 bases; 2,160 comparisons): 1,632 agree; 477 candidate-unknown, 29 project-unknown, 22 candidate-shows-skipped (on completed returns: 1 candidate-shows-skipped, 25 candidate-unknown). The reply's line 4 has no shown_when, so it shows the quotient on entries without the worksheet, and the completed candidate-unknown need used_last_year on IRA and non-annuity entries (classm.f8962.2.deepseek, classm.f5695.7 and others) where the project hides the line. The value expression is the project's (line 3 folded into the table quotients, as the reply notes). Project stands.

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

Second transcription's note: The 'annuity starting date before 1987' branch (skip lines 6 and 7) is outside scope. Such dates are screened out by retirement.special and the annuity question.

Ruling: model error; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`, written by triage.py this round; 1,565 fixtures, 500 generated returns seed 20261026, 999 partial records from 40 bases; 2,160 comparisons): 1,603 agree; 507 candidate-unknown, 29 project-unknown, 21 candidate-shows-skipped (on completed returns: 1 candidate-shows-skipped, 29 candidate-unknown). The reply now declares shown_when plan and annuity, the project plan, annuity and worksheet line 7 above zero (retirement.smw_shown, BUG-0207/0208). By reading, the reply hides the worksheet wherever the project does except for a plan annuity with no cost left, where i1040gi p. 28 makes the payments fully taxable and the worksheet is not used ("Your payments are fully taxable if (a) you didn’t contribute to the cost ... or (b) you got your entire cost back tax free before 2025"); showing it there is the reply's defect (generated 395 r2 in the earlier rounds). triage applies only the project's shown_when (tools/transcription/triage.mjs), so its candidate-shows-skipped and candidate-unknown counts on IRA and non-annuity plan entries are values the reply's own shown_when hides. The value expression is the project's. Project stands.

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

Ruling: model error; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`, written by triage.py this round; 1,565 fixtures, 500 generated returns seed 20261026, 999 partial records from 40 bases; 2,160 comparisons): 1,675 agree; 415 candidate-unknown, 42 candidate-shows-skipped, 28 project-unknown (on completed returns: 1 candidate-shows-skipped, 19 candidate-unknown). The reply now declares shown_when plan and annuity, the project plan, annuity and worksheet line 7 above zero (retirement.smw_shown, BUG-0207/0208). By reading, the reply hides the worksheet wherever the project does except for a plan annuity with no cost left, where i1040gi p. 28 makes the payments fully taxable and the worksheet is not used ("Your payments are fully taxable if (a) you didn’t contribute to the cost ... or (b) you got your entire cost back tax free before 2025"); showing it there is the reply's defect (generated 395 r2 in the earlier rounds). triage applies only the project's shown_when (tools/transcription/triage.mjs), so its candidate-shows-skipped and candidate-unknown counts on IRA and non-annuity plan entries are values the reply's own shown_when hides. The value expression is the project's. Project stands.

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

Ruling: model error; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`, written by triage.py this round; 1,565 fixtures, 500 generated returns seed 20261026, 999 partial records from 40 bases; 2,160 comparisons): 1,673 agree; 444 candidate-unknown, 25 candidate-shows-skipped, 18 project-unknown (on completed returns: 1 candidate-shows-skipped, 23 candidate-unknown). The reply now declares shown_when plan and annuity, the project plan, annuity and worksheet line 7 above zero (retirement.smw_shown, BUG-0207/0208). By reading, the reply hides the worksheet wherever the project does except for a plan annuity with no cost left, where i1040gi p. 28 makes the payments fully taxable and the worksheet is not used ("Your payments are fully taxable if (a) you didn’t contribute to the cost ... or (b) you got your entire cost back tax free before 2025"); showing it there is the reply's defect (generated 395 r2 in the earlier rounds). triage applies only the project's shown_when (tools/transcription/triage.mjs), so its candidate-shows-skipped and candidate-unknown counts on IRA and non-annuity plan entries are values the reply's own shown_when hides. The value expression is the project's. Project stands.

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

Ruling: model error; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`, written by triage.py this round; 1,565 fixtures, 500 generated returns seed 20261026, 999 partial records from 40 bases; 2,160 comparisons): 1,584 agree; 550 candidate-unknown, 18 project-unknown, 8 candidate-shows-skipped (on completed returns: 1 candidate-shows-skipped, 36 candidate-unknown). The reply now declares shown_when plan and annuity, the project plan, annuity and worksheet line 7 above zero (retirement.smw_shown, BUG-0207/0208). By reading, the reply hides the worksheet wherever the project does except for a plan annuity with no cost left, where i1040gi p. 28 makes the payments fully taxable and the worksheet is not used ("Your payments are fully taxable if (a) you didn’t contribute to the cost ... or (b) you got your entire cost back tax free before 2025"); showing it there is the reply's defect (generated 395 r2 in the earlier rounds). triage applies only the project's shown_when (tools/transcription/triage.mjs), so its candidate-shows-skipped and candidate-unknown counts on IRA and non-annuity plan entries are values the reply's own shown_when hides. The value expression is the project's. Project stands.

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

Ruling: model error; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`, written by triage.py this round; 1,565 fixtures, 500 generated returns seed 20261026, 999 partial records from 40 bases; 2,160 comparisons): 697 agree; 865 candidate-shows-skipped, 580 candidate-unknown, 18 project-unknown (on completed returns: 110 candidate-shows-skipped, 36 candidate-unknown). The reply now declares shown_when plan and annuity, the project plan, annuity and worksheet line 7 above zero (retirement.smw_shown, BUG-0207/0208). By reading, the reply hides the worksheet wherever the project does except for a plan annuity with no cost left, where i1040gi p. 28 makes the payments fully taxable and the worksheet is not used ("Your payments are fully taxable if (a) you didn’t contribute to the cost ... or (b) you got your entire cost back tax free before 2025"); showing it there is the reply's defect (generated 395 r2 in the earlier rounds). triage applies only the project's shown_when (tools/transcription/triage.mjs), so its candidate-shows-skipped and candidate-unknown counts on IRA and non-annuity plan entries are values the reply's own shown_when hides. The value expression is the project's. Project stands.

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

Ruling: model error; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`, written by triage.py this round; 1,565 fixtures, 500 generated returns seed 20261026, 999 partial records from 40 bases; 2,160 comparisons): 1,557 agree; 550 candidate-unknown, 35 candidate-shows-skipped, 18 project-unknown (on completed returns: 1 candidate-shows-skipped, 36 candidate-unknown). The reply now declares shown_when plan and annuity, the project plan, annuity and worksheet line 7 above zero (retirement.smw_shown, BUG-0207/0208). By reading, the reply hides the worksheet wherever the project does except for a plan annuity with no cost left, where i1040gi p. 28 makes the payments fully taxable and the worksheet is not used ("Your payments are fully taxable if (a) you didn’t contribute to the cost ... or (b) you got your entire cost back tax free before 2025"); showing it there is the reply's defect (generated 395 r2 in the earlier rounds). triage applies only the project's shown_when (tools/transcription/triage.mjs), so its candidate-shows-skipped and candidate-unknown counts on IRA and non-annuity plan entries are values the reply's own shown_when hides. The value expression is the project's. Project stands.

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

Ruling: model error; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity." i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost (see Cost, later) of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a." i1040gi p. 29, Simplified Method Worksheet. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`, written by triage.py this round; 1,565 fixtures, 500 generated returns seed 20261026, 999 partial records from 40 bases; 2,160 comparisons): 1,576 agree; 550 candidate-unknown, 18 project-unknown, 16 candidate-shows-skipped (on completed returns: 36 candidate-unknown). The reply now declares shown_when plan and annuity, the project plan, annuity and worksheet line 7 above zero (retirement.smw_shown, BUG-0207/0208). By reading, the reply hides the worksheet wherever the project does except for a plan annuity with no cost left, where i1040gi p. 28 makes the payments fully taxable and the worksheet is not used ("Your payments are fully taxable if (a) you didn’t contribute to the cost ... or (b) you got your entire cost back tax free before 2025"); showing it there is the reply's defect (generated 395 r2 in the earlier rounds). triage applies only the project's shown_when (tools/transcription/triage.mjs), so its candidate-shows-skipped and candidate-unknown counts on IRA and non-annuity plan entries are values the reply's own shown_when hides. The value expression is the project's. Project stands.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| retirement.taxable | retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq, retirement.special | retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq |
| retirement.amount_a | retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq, retirement.special | retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq |
| retirement.sav_amount | retirement.special | - |
| retirement.l1 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq |
| retirement.l2 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq |
| retirement.l2_e05 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq |
| retirement.l2_e09 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq |
| retirement.l2_e19 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq |
| retirement.l2_e22 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq |
| retirement.l2_e23 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq |
| retirement.l1_s | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq |
| retirement.l2_s | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_rollover_over, retirement.h_roth_nonq |
| (SMW 5) | retirement.h_months_bad | retirement.h_months_bad |
| (SMW 8) | retirement.h_months_bad | retirement.h_months_bad |
| (SMW 9) | retirement.h_months_bad | retirement.h_months_bad |
| (SMW 10) | retirement.h_months_bad | retirement.h_months_bad |
| (SMW 11) | retirement.h_months_bad | retirement.h_months_bad |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| retirement.one | 5fa3f6c5f390bb42e4ce3d9f6e006a5a7c53fc361e72a92b97f71714ba5f9525 |
| retirement.is_ira | 9f2826800762b8340d4733f77dbd698e2ebf2332a3da29812efed8929f1e085f |
| retirement.has_rollover | 05ce16395e07b1260eff7c035df3649d3b02b8ea824206096a8837a0c67c45d7 |
| retirement.taxable | 51c5ec17fcf85292364c0678f65b01302571c14840bc8f2b39d7e24c3bad489c |
| retirement.amount_a | 1cc4c2636d5967a5a57ae4773d2cfd88809c2d1665d4e8b331533691da4b1cd6 |
| retirement.sav_amount | 4665e57446b3719c51c16355de4698979ed2e564d73710ceea2358621afcb2fc |
| retirement.l1 | 416c32c92b535deeec46328b8a037b550fe28dc00244dbffc2b17f054d870bd5 |
| retirement.l2 | b1ca905120a242a76df9790351edf9264a9ae19ed31c6c4de314b5953597347c |
| retirement.l2_e05 | 833e4f14aa2c88740a78d120b9c291a4c2e6787f3410d32aa004f5037df2406b |
| retirement.l2_e09 | 2e46142b8da1e6ef5aa55aa27a0274ea76c35ff26e5cff97d7fd484d075d0cbd |
| retirement.l2_e19 | 4fa3f6500975ef3d928769360a48e8ab5b75560dedbc32fc067acfc6f031f023 |
| retirement.l2_e22 | f3b272997e9091b0c1251853c9dc706ce4c6842a4bc3ee787de3ad496a51dda4 |
| retirement.is_e23 | 613c679f37ab039c30591dbe95ee45b118a40c1346da403cff3e41ef89dfe50e |
| retirement.l2_e23 | 93a819ad1233cca0e06cbc405320a514e4549d3332169c4dfad64712cc1fb55e |
| retirement.l1_s | f9fef6b2684e8c1ffeb12aa5dee0491b059de1071a4fb9a0b62d6bf22e9b50d8 |
| retirement.l2_s | 9b39845550adc714aa5d3a6794dea638062c3dcce2a222daa0cb9e662be80851 |
| (SMW 1) | e6b315fcb27eb69cad85d1a865acafde5731988ef6fbb7d08fd205f55955d007 |
| (SMW 2) | bbf56905dc9f58de0e992f5d97671190c8cbbb5e600708967b4af439a2c073f7 |
| (SMW 4) | 7c3c87f2d3cdbe3364bbd3d4037e98e082b2dc9a36c5e2a70b2b02fee8cb8341 |
| (SMW 5) | 3a24f10ddcde2a2b6a43bab3b2c553da356029d932abb30497539c7d243eb1ab |
| (SMW 6) | 9c44c18961cab22e277b2645812c8133de4359488c47c527f1331a7f806b09af |
| (SMW 7) | 122f232d63a9a5e363119a1e36c1d9103eade0b140e348d53a5f2ab3ece8d02b |
| (SMW 8) | 79f5979b9ae77a69f74a9801bc0078fdafa3ed95239b4865760811091101b42c |
| (SMW 9) | 9cc350ae62299d98f2ef8746936e945a25d081f3646ed6fe8662dd4b805aadee |
| (SMW 10) | 6cc054c92a70f4f6a5f55b204cd1d317ebdf9f8eac445eb28ac83a0c005d9cec |
| (SMW 11) | 30bf66fc17a4425a945a01fdb2e1245adf7df08990e3c5a2b6dde161d3df564a |
| (rest of the document) | dad95e78da2dc7428fc3b3c16abeed081b887004d12534553cb9167e6500a41f |

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

## Line-scoped reviews

Lines reviewed again after a change, each pass by its own isolated request (transcribe.py or render_compare.py --lines). A section marked "Reviewed in: pass <id>" was judged in the pass of that id below; every other section in the review recorded at the top of this log.

#### Pass 11db066e0fce

| field | value |
| --- | --- |
| date | 2026-11-04 |
| review scope | lines retirement.has_rollover, retirement.taxable, retirement.amount_a, retirement.sav_amount, retirement.l1, retirement.l2, retirement.l2_e05, retirement.l2_e09, retirement.l2_e19, retirement.l2_e22, retirement.l2_e23, retirement.l1_s, retirement.l2_s |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 11db066e0fce8612b1b3728635b5b2d72c83e6280adfbb4d94a1b4d9705dabb9 |
| prompt policy | source-only-computation-v3+lines-v1 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 9b6a617d195836ddbdeb2f808e81ea67e3a3d96919aea0c94ffe6ef8e6a5f832 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | b94122b6412a237852141ff52874daf3d40db6e6ad197f2cfa505c842034a879 |
| receipt | .transcription/retirement.lines-37c350a27fd6 |
| printed lines compared | 13 |
| agree / disagree / missing | 0 / 13 / 0 |
| extra printed lines in second | none |

##### Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099r | 2025 (calendar-year form) | 5, 7, 9 | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | 5, 7, 9 | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| i1040gi | 2025; printed date 2026-02-25 | 26, 27, 28, 29, 30, 31 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 26, 27, 28, 30, 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i5329 | 2025 | 1, 3, 5 | cited pages | bc85a048e4293ab244d68023ac7bb45333ceede0763b3b1cb3430eb4829a18bf | 1, 3, 5 | e46adbf118d780a00b73957b6ef4c6e436e651f6f076a36fa9b6717bd138ee5d |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |
| p575 | None | 16, 21, 23, 34, 35 | pages named by another document's citation | 4d6ee3802a2906a4633dcfc104aa33bb3d9ddedebddc9eadbd0393cfdb61e07b | 16, 21, 23, 34, 35 | 3962801dde168fda9f4ee239245d9746b12e2d60bf358b25186ae4a57aa5b837 |
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
    label: "Zero (no entry)"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: retirement.h_is_g
    printed: "(helper)"
    label: "Code G in box 7: direct rollover of a distribution to a qualified plan, a section 403(b) plan, a governmental section 457(b) plan, or an IRA"
    type: Bool
    expr: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}

  - id: retirement.h_eff_rollover
    printed: "(helper)"
    label: "Amount of the distribution rolled over (for a direct rollover, code G, the whole distribution)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_is_g, {const: true}]}
          then: retirement.box1
        - guard: {op: test, eq: [retirement.h_is_g, {const: false}]}
          then: retirement.rollover
    note: "Open: whether the filer enters the whole of a code G distribution as the rollover amount. Chosen reading: for code G the whole of box 1 is treated as rolled over, whatever the rollover input says."

  - id: retirement.has_rollover
    printed: "(helper)"
    label: "Exception 1 / Rollovers: you rolled over part or all of the distribution (check box 1 on line 4c or 5c)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
        - {op: test, gt: [retirement.rollover, {const: 0}]}

  - id: retirement.h_rollover_over
    printed: "(gate)"
    label: "Consistency check: the amount rolled over is more than the gross distribution in box 1"
    type: Bool
    expr: {op: test, gt: [retirement.rollover, retirement.box1]}

  - id: retirement.h_annuity_rollover
    printed: "(gate)"
    label: "Consistency check: periodic annuity payments figured with the Simplified Method are also reported as rolled over"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.account, {const: "plan"}]}
        - {op: test, eq: [retirement.annuity, {const: true}]}
        - {op: test, eq: [retirement.has_rollover, {const: true}]}
    note: "Open: the text does not say how a rollover combines with periodic annuity payments under the Simplified Method. Chosen reading: the combination is flagged as a consistency check, and the Simplified Method result is used."

  - id: retirement.h_roth_nonq
    printed: "(gate)"
    label: "Exception 2, item 2: a distribution from a Roth IRA, other than one with code Q, is figured on Form 8606"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.account, {const: "roth_ira"}]}
        - {op: test, ne: [retirement.code, {const: "qualified_roth_Q"}]}
    note: "Open: code T with a Roth contribution for 2020 or earlier also gives -0- on line 4b, but the input interface has no code T or contribution-year question. Chosen reading: every Roth IRA distribution without code Q is sent to Form 8606."

  - id: retirement.h_ira_taxable
    printed: "(helper)"
    label: "IRA: if the total distribution wasn't rolled over, enter the part not rolled over on line 4b (otherwise the total distribution, fully taxable)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.h_eff_rollover}

  - id: retirement.h_plan_net5
    printed: "(helper)"
    label: "Distribution from Form 1099-R, box 1, minus contributions (usually shown in box 5) that were taxable to you when made"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.box5}

  - id: retirement.h_plan_taxable
    printed: "(helper)"
    label: "From that result, subtract the amount of the rollover. Enter the remaining amount on line 5b"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_plan_net5, take: retirement.h_eff_rollover}
    note: "Open: the box 5 subtraction is printed only for rollovers. Chosen reading: it is applied to every pension distribution that is not figured with the Simplified Method, with a rollover of zero when nothing was rolled over. Distributions needing the General Rule are refused through retirement.special."

  - id: retirement.taxable
    printed: "(helper)"
    label: "Taxable amount of this distribution (Form 1040, line 4b or 5b)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.account, {const: "traditional_ira"}]}
          then: retirement.h_ira_taxable
        - guard: {op: test, eq: [retirement.account, {const: "roth_ira"}]}
          then: retirement.h_zero
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
      - retirement.h_roth_nonq
      - {when: retirement.h_rollover_over, when_known: true}
      - {when: retirement.h_annuity_rollover, when_known: true}
    note: "A Roth IRA distribution reaches the -0- branch only with code Q (Exception 2, item 2(b)); any other Roth IRA distribution is refused."

  - id: retirement.h_fully_taxable
    printed: "(helper)"
    label: "The distribution is fully taxable (enter it on line 4b or 5b; don't make an entry on line 4a or 5a)"
    type: Bool
    expr: {op: test, eq: [retirement.taxable, retirement.box1]}

  - id: retirement.amount_a
    printed: "(helper)"
    label: "Amount of this distribution for Form 1040, line 4a or 5a (total distribution from Form 1099-R, box 1)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_fully_taxable, {const: true}]}
          then: retirement.h_zero
        - guard: {op: test, eq: [retirement.h_fully_taxable, {const: false}]}
          then: retirement.box1
    note: "Open: 'More than one distribution' says to enter the total of the distributions on line 4a, while a fully taxable distribution makes no entry there. Chosen reading: this entry gives box 1 for a distribution that is not fully taxable and zero for one that is. Combining distributions is left to Form 1040."

  - id: retirement.h_sav_excluded
    printed: "(helper)"
    label: "Form 8880 line 4 exclusions: military retirement plan (other than TSP), section 404(k) dividends, inherited IRA by a nonspousal beneficiary"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.sav_military, {const: true}]}
        - {op: test, eq: [retirement.sav_404k, {const: true}]}
        - {op: test, eq: [retirement.sav_inherited, {const: true}]}

  - id: retirement.h_sav_base
    printed: "(helper)"
    label: "Distribution, not including distributions not taxable as the result of a rollover"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.h_eff_rollover}

  - id: retirement.sav_amount
    printed: "(helper)"
    label: "Amount of this distribution counted on Form 8880, line 4"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_sav_excluded, {const: true}]}
          then: retirement.h_zero
        - guard: {op: test, eq: [retirement.h_sav_excluded, {const: false}]}
          then: retirement.h_sav_base
    refuses: [retirement.special]

  - id: retirement.h_early
    printed: "(helper)"
    label: "Early distribution with no known exception shown in box 7 (code 1, or code S)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.code, {const: "early_1"}]}
        - {op: test, eq: [retirement.code, {const: "simple_S"}]}
    note: "Open: which codes feed Form 5329 line 1. Chosen reading: codes 1 and S only. Codes 2, 3 and 4 already show an exception that covers the whole distribution (a partial code 2 exception is refused through code_screen), so they add no tax. Roth IRA early distributions are refused through Form 8606."

  - id: retirement.l1
    printed: "(helper)"
    label: "Form 5329 line 1: early distributions includible in income from this distribution"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_early, {const: true}]}
          then: retirement.taxable
        - guard: {op: test, eq: [retirement.h_early, {const: false}]}
          then: retirement.h_zero
    refuses: [retirement.early_screen, retirement.code_screen]

  - id: retirement.h_is_s
    printed: "(helper)"
    label: "Code S: distribution from a SIMPLE IRA received within 2 years from the date you first participated"
    type: Bool
    expr: {op: test, eq: [retirement.code, {const: "simple_S"}]}

  - id: retirement.l1_s
    printed: "(helper)"
    label: "Part of Form 5329 line 1 that is a code S SIMPLE IRA distribution (25% instead of 10%)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_is_s, {const: true}]}
          then: retirement.l1
        - guard: {op: test, eq: [retirement.h_is_s, {const: false}]}
          then: retirement.h_zero

  - id: retirement.h_has_exc
    printed: "(helper)"
    label: "An exception to the additional tax on early distributions applies"
    type: Bool
    expr: {op: test, ne: [retirement.exception, {const: "none"}]}

  - id: retirement.h_l2_cap
    printed: "(helper)"
    label: "Amount the exception covers, not more than the early distribution includible in income"
    type: NonNegDollars
    expr: {op: smaller_of, of: [retirement.exc_amount, retirement.l1]}

  - id: retirement.l2
    printed: "(helper)"
    label: "Form 5329 line 2: early distributions not subject to additional tax (amount you can exclude), before the per-person dollar limits"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_has_exc, {const: true}]}
          then: retirement.h_l2_cap
        - guard: {op: test, eq: [retirement.h_has_exc, {const: false}]}
          then: retirement.h_zero
    refuses: [retirement.early_screen, retirement.code_screen]
    note: "The dollar limits for exceptions 05, 09, 19, 22 and 23 are applied per person outside this entry, which is why those exceptions are also reported separately below."

  - id: retirement.l2_s
    printed: "(helper)"
    label: "Part of Form 5329 line 2 that is a code S SIMPLE IRA distribution"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_is_s, {const: true}]}
          then: retirement.l2
        - guard: {op: test, eq: [retirement.h_is_s, {const: false}]}
          then: retirement.h_zero

  - id: retirement.l2_e05
    printed: "(helper)"
    label: "Form 5329 line 2 amount under exception 05 (unreimbursed medical expenses minus 7.5% of AGI)"
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
    label: "Form 5329 line 2 amount under exception 09 (IRA distributions for the purchase of a first home, up to $10,000)"
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
    label: "Form 5329 line 2 amount under exception 19 (qualified birth or adoption distributions, up to $5,000)"
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
    label: "Form 5329 line 2 amount under exception 22 (qualified distributions to victims of domestic abuse)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e22"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e22"}]}
          then: retirement.h_zero

  - id: retirement.l2_e23
    printed: "(helper)"
    label: "Form 5329 line 2 amount under exception 23 (eligible emergency personal expense distributions)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e23"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e23"}]}
          then: retirement.h_zero
```
```

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
