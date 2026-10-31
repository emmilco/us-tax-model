# Transcription agreement — retirement

Second transcription of `Form 1099-R distributions (IRAs, pensions and annuities)` by an isolated model (spec 6.5), compared line by line with `forms/2025/retirement.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 7743c80d0c738ec84ddc1ab7d23fe83f2097f6ca896586f0e86696d62559ea54 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | e6df1a0e401eb149547cb493f9eeea54ae184457d69a853cc0580786551fec07 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | fa349fb28ee871623fe147cb074c50407a0b8df7362d87eb400b780ed0baf272 |
| printed lines compared | 26 |
| agree / disagree / missing | 12 / 14 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099r | 2025 (calendar-year form) | 5, 7 | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | 5, 7 | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| i1040gi | 2025; printed date 2026-02-25 | 26, 27, 28, 29, 30, 31 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 26, 27, 28, 30, 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i5329 | 2025 | 1, 3, 5 | cited pages | bc85a048e4293ab244d68023ac7bb45333ceede0763b3b1cb3430eb4829a18bf | 1, 3, 5 | e46adbf118d780a00b73957b6ef4c6e436e651f6f076a36fa9b6717bd138ee5d |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |

## Lines

### retirement.one — One distribution
Status: **AGREE**

### retirement.is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

### retirement.has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a direct rollov
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}
```

Second:

```json
{"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}
```

Ruling: model error and scope; i1040gi p. 30, Rollovers: "Use lines 5a and 5b to report a rollover, including a direct rollover, from one qualified employer’s plan to another or to an IRA. ... Also check box 1 on line 5c."; i1040gi p. 27, Exception 1: "Enter the total distribution on line 4a if you rolled over part or all of the distribution ... Also check box 1 on line 4c.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,035 partial records from 40 bases; 2,066 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,710 of 2,066 agree; 228 project-refuses (none completed), 95 project-unknown (none completed), 28 value (3 completed), 5 candidate-unknown (none completed). (1) The reply treats a code G direct rollover as rolling over box 1, so a code G entry with $0 in box 1 is not a rollover; the source makes a direct rollover a rollover and checks box 1 on line 4c/5c whatever the amount, as the project does (retirement.direct): the 3 completed values are classm.tcw.5 r1, classm.f1040.3 r2 and classm.f1040.3.deepseek r2 (code G, box 1 $0.00), project true, candidate false; the 25 other values are on refused or incomplete returns. (2) The 228 project-refuses are its cited retirement.bad_code (162) and retirement.special (66) read through retirement.rolled; the project-unknown are partial records withholding retirement.account or retirement.special, which the project asks of every entry; the candidate-unknown are on refused or incomplete returns: scope. Same reading as T-067 round 2. Fix round 2 changed no retirement expression; it widened the retirement.special question (BUG-0243: military disability pension, an annuity received as beneficiary of an employee who died or shared among beneficiaries, a rollover of property other than cash or of a QDRO distribution), which reaches these lines only as a refusal. Project stands.

### retirement.taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}
```

Second transcription's note: A Roth IRA reaches zero only with code Q (Exception 2, item 2b, 'enter -0- on line 4b'). Other Roth codes are refused.

Ruling: model error and scope; i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost ... of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a."; i1040gi p. 29, line 11: "If zero, you won’t have to complete this worksheet next year." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,035 partial records from 40 bases; 2,066 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,990 of 2,066 agree; 47 project-unknown (none completed), 12 candidate-unknown (4 completed), 12 value (8 completed), 5 project-refuses (none completed). The reply now takes worksheet line 7 signed (its own note: "If line 6 exceeds line 2, lines 7 and 8 are negative and line 9 exceeds line 1") and has no branch for a cost recovered before 2025 or a $0 cost, which the source makes fully taxable: the 8 completed values are classm.tcw.15 r1 (plan, code 7, cost $0, recovered $9,979: project $39,110.00, candidate $49,089.00) and 6 of its partial records, and generated 395 r2 (cost $25,183.00 below recovered $47,921.41, box 1 $0: project $0.00, candidate $22,738.41); the 4 completed candidate-unknown are partials of classm.tcw.15 withholding used_last_year, joint_life, combined_age or months, worksheet answers the project does not ask once the cost is recovered. The project-refuses are its cited retirement.bad_code, screen_refused and annuity_rollover, and the project-unknown are partial records: scope. Project stands.

### retirement.amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"input": "retirement.box5"}, {"const": 0}], "test": "le"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.box5"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"input": "retirement.box5"}, {"const": 0}], "test": "le"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.box5"}], "test": "lt"}], "test": "all"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Ruling: model error and scope; i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost ... of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a."; i1040gi p. 27, Lines 4a and 4b: "If the distribution from your IRA is fully taxable, enter the total distribution on line 4b; don’t make an entry on line 4a.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,035 partial records from 40 bases; 2,066 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,940 of 2,066 agree; 72 project-unknown (none completed), 36 value (12 completed), 13 candidate-unknown (none completed), 5 project-refuses (none completed). The reply enters box 1 on line 5a for every plan annuity: the 12 completed values are classm.tcw.15 r1 (cost $0, cost recovered: project $0.00, candidate $39,110.00) and 10 of its partial records, and generated 314 r2 (plan, code 4, annuity, cost $0: $0.00 against $46,209.90), all fully taxable, "don’t make an entry on line 5a". The other values are on refused or incomplete returns; the project-refuses are its cited gates and the project-unknown partial records: scope. Project stands.

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

Second transcription's note: Form 8880 line 4 counts distributions received, not their taxable part, so box 5 is not subtracted. Its other exclusions (excess contributions, returned contributions, Roth rollovers, plan loans) fall under the retirement.special and code screens.

Ruling: model error and scope; f8880 p. 2, Line 4: "Don’t include any of the following. • Distributions not taxable as the result of a rollover or a trustee-to-trustee transfer ... • Distributions from a military retirement plan (other than the federal TSP). • Distributions from an inherited IRA by a nonspousal beneficiary". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,035 partial records from 40 bases; 2,066 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,825 of 2,066 agree; 90 project-refuses (none completed), 74 candidate-unknown (23 completed), 50 project-unknown (none completed), 27 candidate-refuses (none completed). No value differs. The 23 completed candidate-unknown are partial records withholding retirement.sav_military (9) or retirement.sav_404k (9) on IRA entries (classm.s2.3.deepseek, classm.f5329.2.deepseek, stage21.example.tom_jones) or retirement.sav_inherited (5) on plan entries (classm.tcw.15, classm.f8962.2, stage21.blind.e3): the reply applies every exclusion to every account kind, where the interview asks each only of the account it concerns (amb.2025.savers_inherited_plans for the inherited reading). The project-refuses are its cited retirement.bad_code; the candidate-refuses (retirement.special 4, its h_other_code 23) and the project-unknown are on refused or incomplete returns: scope. Project stands.

### retirement.l1 — Form 5329 line 1 share: the taxable amount of an early distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 3, Line 1: "Enter the amount of early distributions includible in income (other than qualified disaster recovery distributions) that you received from:". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,035 partial records from 40 bases; 2,066 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,467 of 2,066 agree; 598 candidate-unknown (62 completed), 1 project-refuses (none completed). No value differs: the reply leaves code 2 off line 1, the project's reading of amb.2025.f5329_line1_codes (chosen: line 1 holds only code 1 and S; the other reading puts code 2 on line 1 and offsets it on line 2; owner's decision D8(a)). It declares retirement.early_screen and retirement.code_screen as refusals of every entry (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused): of the 62 completed candidate-unknown, 52 need early_screen on entries of other codes (classm.f8962.2.deepseek, classm.ira.2) and 10 are partial records withholding code_screen on code 1 or S entries (classm.s2.3.deepseek, classm.f5329.2.deepseek, stage21.example.tom_jones). The project-refuses is its cited retirement.bad_code: scope. Project stands.

### retirement.l2 — Form 5329 line 2 share before the per-person limits
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The dollar limits for exceptions 05, 09, 19, 22 and 23 are not applied here. The interface says the tool applies them per person, using the amounts split out below.

Ruling: model error; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,035 partial records from 40 bases; 2,066 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 2,058 of 2,066 agree; 8 candidate-unknown (5 completed). No value differs. The reply reads line 1, which refuses on code_screen, so the 5 completed candidate-unknown are partial records withholding code_screen on code 1 or S entries (stage21.blind.e3, stage21.blind.e7) (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused); the other 3 are on refused returns. Project stands.

### retirement.l2_e05 — Line 2 share under exception 05
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,035 partial records from 40 bases; 2,066 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 2,064 of 2,066 agree; 2 candidate-unknown (2 completed). No value differs; the exception 05 share is the project's. The 2 completed candidate-unknown are partial records of stage21.blind.e7 withholding code_screen on a code 1 entry, a screen asked only for codes 2, 4 and 7, reached through the reply's line 1. Project stands.

### retirement.l2_e09 — Line 2 share under exception 09
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,035 partial records from 40 bases; 2,066 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 2,066 of 2,066 agree. The reply splits line 2 by exception 09 on the project's condition (an exception claimed on a code 1 or S entry, exception = e09); the text differs only in grouping. Project stands.

### retirement.l2_e19 — Line 2 share under exception 19
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,035 partial records from 40 bases; 2,066 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 2,066 of 2,066 agree. The reply splits line 2 by exception 19 on the project's condition (an exception claimed on a code 1 or S entry, exception = e19); the text differs only in grouping. Project stands.

### retirement.l2_e22 — Line 2 share under exception 22
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,035 partial records from 40 bases; 2,066 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 2,066 of 2,066 agree. The reply splits line 2 by exception 22 on the project's condition (an exception claimed on a code 1 or S entry, exception = e22); the text differs only in grouping. Project stands.

### retirement.is_e23 — Exception 23
Status: **AGREE**

### retirement.l2_e23 — Line 2 share under exception 23
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99."; p590b p. 28, Emergency personal expense distributions, Distribution limits: "You are limited to taking one emergency personal expense distribution per calendar year". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,035 partial records from 40 bases; 2,066 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 2,065 of 2,066 agree; 1 candidate-unknown (1 completed). No value differs. The 1 completed candidate-unknown is partial(stage21.mut.e23_over_cap) withholding code_screen on a code 1 entry, needed only through the reply's line 1 refusal. Project stands.

### retirement.l1_s — Line 1 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 4: "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%. These distributions are included in boxes 1 and 2a of Form 1099-R and are designated with code S in box 7.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,035 partial records from 40 bases; 2,066 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 2,064 of 2,066 agree; 1 candidate-unknown (1 completed), 1 project-refuses (none completed). The code S share is the project's; the 1 completed candidate-unknown is partial(classm.f5329.2.deepseek) withholding code_screen on a code S entry, a screen for codes 2, 4 and 7 only; the project-refuses is its cited retirement.bad_code on a refused return: scope. Project stands.

### retirement.l2_s — Line 2 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i5329 p. 5, Line 4: "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%. These distributions are included in boxes 1 and 2a of Form 1099-R and are designated with code S in box 7.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,035 partial records from 40 bases; 2,066 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 2,066 of 2,066 agree. The code S share of line 2 is the project's. Project stands.

### (SMW 1) — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

### (SMW 2) — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

### (SMW 4) — Divide line 2 by the number on line 3 (or, if you completed this worksheet last year, line
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 56, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_360"}}}, {"guard": {"args": [{"args": [{"const": 56, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 61, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_310"}}}, {"guard": {"args": [{"args": [{"const": 61, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 66, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_260"}}}, {"guard": {"args": [{"args": [{"const": 66, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 71, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_210"}}}, {"guard": {"args": [{"const": 71, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_160"}}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 0, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 111, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_410"}}}, {"guard": {"args": [{"args": [{"const": 111, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 121, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_360"}}}, {"guard": {"args": [{"args": [{"const": 121, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 131, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_310"}}}, {"guard": {"args": [{"args": [{"const": 131, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 141, "type": "Count"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_260"}}}, {"guard": {"args": [{"const": 141, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_210"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"input": "retirement.last_line4"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 56, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 60, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_310"}}}, {"guard": {"args": [{"args": [{"const": 61, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 65, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_260"}}}, {"guard": {"args": [{"args": [{"const": 66, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, {"args": [{"input": "retirement.age"}, {"const": 70, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_210"}}}, {"guard": {"args": [{"const": 71, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_160"}}}, {"guard": {"args": [{"input": "retirement.age"}, {"const": 55, "type": "Count"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_360"}}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": 111, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 120, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_360"}}}, {"guard": {"args": [{"args": [{"const": 121, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 130, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_310"}}}, {"guard": {"args": [{"args": [{"const": 131, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, {"args": [{"input": "retirement.combined_age"}, {"const": 140, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_260"}}}, {"guard": {"args": [{"const": 141, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_210"}}}, {"guard": {"args": [{"input": "retirement.combined_age"}, {"const": 110, "type": "Count"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_410"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"input": "retirement.last_line4"}}], "op": "choose"}
```

Second transcription's note: The worksheet states no rounding for the division. Chosen reading: half-up to the cent, which is how multiply_rate rounds. Line 3 has no line of its own because each table number is carried as a 1/N rate.

Ruling: model error (+ scope); i1040gi p. 29, Simplified Method Worksheet, line 4; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity."; i1040gi p. 28, Fully Taxable Pensions and Annuities: "(a) you didn’t contribute to the cost ... or (b) you got your entire cost back tax free before 2025". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,035 partial records from 40 bases; 2,066 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,428 of 2,066 agree; 529 candidate-unknown (155 completed), 70 candidate-shows-skipped (1 completed), 39 candidate-refuses (none completed). All differences but 4 are on entries where the project hides the line (retirement.smw_shown false: an IRA, a non-annuity plan entry, or an annuity whose cost is $0 or was recovered before 2025). The reply gives the worksheet lines no hiding condition, so it shows or asks for line 4 on entries the source never takes through the worksheet: the 1 completed candidate-shows-skipped is generated 395 r2 (cost recovered: $1,550.08 from last year's line 4); the completed candidate-unknown need used_last_year or other worksheet answers on such entries (stage15.f8880.s1, stage21.example.tom_jones, partials of classm.s2.3.deepseek and classm.tcw.15). The 4 shown differences of the Claude record are partial records withholding retirement.special on refused or incomplete returns (classm.retirement.2.deepseek, classm.retirement.4, classm.f8962.2, stage10.smw.joint_six_months), where the reply refuses on the unanswered screen: scope. Its value is the project's wherever the project shows the line. retirement.smw_shown is unchanged since T-067 round 2. Project stands.

### (SMW 5) — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

### (SMW 6) — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

### (SMW 7) — Subtract line 6 from line 2
Status: **AGREE**

### (SMW 8) — Enter the smaller of line 5 or line 7
Status: **AGREE**

### (SMW 9) — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero
Status: **AGREE**

### (SMW 10) — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

### (SMW 11) — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| retirement.has_rollover | retirement.h_rollover_over | retirement.h_rollover_over |
| retirement.taxable | retirement.h_annuity_rollover, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606, retirement.special | retirement.h_annuity_rollover, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606 |
| retirement.amount_a | retirement.h_annuity_rollover, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606, retirement.special | retirement.h_annuity_rollover, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606 |
| retirement.sav_amount | retirement.h_other_code, retirement.h_rollover_over, retirement.special | retirement.h_other_code, retirement.h_rollover_over |
| retirement.l1 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606 |
| retirement.l2 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_exception_misplaced, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_exception_misplaced, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606 |
| retirement.l2_e05 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_exception_misplaced, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_exception_misplaced, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606 |
| retirement.l2_e09 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_exception_misplaced, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_exception_misplaced, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606 |
| retirement.l2_e19 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_exception_misplaced, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_exception_misplaced, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606 |
| retirement.l2_e22 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_exception_misplaced, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_exception_misplaced, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606 |
| retirement.l2_e23 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_exception_misplaced, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_exception_misplaced, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606 |
| retirement.l1_s | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606 |
| retirement.l2_s | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_exception_misplaced, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_exception_misplaced, retirement.h_other_code, retirement.h_q_not_roth, retirement.h_rollover_over, retirement.h_roth_8606 |
| (SMW 2) | retirement.special | retirement.special |
| (SMW 4) | retirement.special | retirement.special |
| (SMW 5) | retirement.special | retirement.special |
| (SMW 7) | retirement.special | retirement.special |
| (SMW 8) | retirement.special | retirement.special |
| (SMW 9) | retirement.special | retirement.special |
| (SMW 10) | retirement.special | retirement.special |
| (SMW 11) | retirement.special | retirement.special |

## Raw second transcription

```yaml
lines:
  - id: retirement.one
    printed: "(helper)"
    label: "One (counts this Form 1099-R distribution)"
    type: Count
    expr: {op: param, ref: person.one}
  - id: retirement.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: retirement.is_ira
    printed: "(helper)"
    label: "IRA distribution, reported on lines 4a and 4b rather than lines 5a and 5b"
    type: Bool
    expr: {op: test, ne: [retirement.account, {const: "plan"}]}
  - id: retirement.smw1
    printed: "(SMW 1)"
    label: "Enter the total pension or annuity payments from Form 1099-R, box 1. Also, enter this amount on Form 1040 or 1040-SR, line 5a"
    type: NonNegDollars
    expr: {op: copy, from: retirement.box1}
  - id: retirement.smw2
    printed: "(SMW 2)"
    label: "Enter your cost in the plan at the annuity starting date"
    type: NonNegDollars
    expr: {op: copy, from: retirement.cost}
    refuses: [retirement.special]
    note: "The worksheet adds any death benefit exclusion to this line. The retirement.special screen covers that case, so only the cost is encoded."
  - id: retirement.h_t1_360
    printed: "(helper)"
    label: "Line 2 divided by 360 (Table 1, age 55 or under)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_360}}
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
  - id: retirement.h_t1
    printed: "(helper)"
    label: "Divide line 2 by the number from Table 1 for line 3"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [retirement.age, {const: 55, type: Count}]}
          then: retirement.h_t1_360
        - guard: {op: test, all: [{op: test, ge: [retirement.age, {const: 56, type: Count}]}, {op: test, le: [retirement.age, {const: 60, type: Count}]}]}
          then: retirement.h_t1_310
        - guard: {op: test, all: [{op: test, ge: [retirement.age, {const: 61, type: Count}]}, {op: test, le: [retirement.age, {const: 65, type: Count}]}]}
          then: retirement.h_t1_260
        - guard: {op: test, all: [{op: test, ge: [retirement.age, {const: 66, type: Count}]}, {op: test, le: [retirement.age, {const: 70, type: Count}]}]}
          then: retirement.h_t1_210
        - guard: {op: test, ge: [retirement.age, {const: 71, type: Count}]}
          then: retirement.h_t1_160
    note: "Only the 'after November 18, 1996' column of Table 1 is encoded. The retirement.special and retirement.annuity questions put earlier starting dates out of scope."
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
  - id: retirement.h_t2
    printed: "(helper)"
    label: "Divide line 2 by the number from Table 2 for line 3"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [retirement.combined_age, {const: 110, type: Count}]}
          then: retirement.h_t2_410
        - guard: {op: test, all: [{op: test, ge: [retirement.combined_age, {const: 111, type: Count}]}, {op: test, le: [retirement.combined_age, {const: 120, type: Count}]}]}
          then: retirement.h_t2_360
        - guard: {op: test, all: [{op: test, ge: [retirement.combined_age, {const: 121, type: Count}]}, {op: test, le: [retirement.combined_age, {const: 130, type: Count}]}]}
          then: retirement.h_t2_310
        - guard: {op: test, all: [{op: test, ge: [retirement.combined_age, {const: 131, type: Count}]}, {op: test, le: [retirement.combined_age, {const: 140, type: Count}]}]}
          then: retirement.h_t2_260
        - guard: {op: test, ge: [retirement.combined_age, {const: 141, type: Count}]}
          then: retirement.h_t2_210
  - id: retirement.h_line4_figured
    printed: "(helper)"
    label: "Divide line 2 by the number on line 3 (Table 2 if the annuity starting date was after 1997 and the payments are for your life and that of your beneficiary; otherwise Table 1)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.joint_life, {const: true}]}
          then: retirement.h_t2
        - guard: {op: test, eq: [retirement.joint_life, {const: false}]}
          then: retirement.h_t1
  - id: retirement.smw4
    printed: "(SMW 4)"
    label: "Divide line 2 by the number on line 3. If you completed this worksheet last year, skip line 3 and enter the amount from line 4 of last year's worksheet"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.used_last_year, {const: true}]}
          then: retirement.last_line4
        - guard: {op: test, eq: [retirement.used_last_year, {const: false}]}
          then: retirement.h_line4_figured
    note: "The worksheet states no rounding for the division. Chosen reading: half-up to the cent, which is how multiply_rate rounds. Line 3 has no line of its own because each table number is carried as a 1/N rate."
  - id: retirement.smw5
    printed: "(SMW 5)"
    label: "Multiply line 4 by the number of months for which this year's payments were made"
    type: NonNegDollars
    expr: {op: multiply_count, amount: retirement.smw4, count: retirement.months}
  - id: retirement.smw6
    printed: "(SMW 6)"
    label: "Enter the amount, if any, recovered tax free in years after 1986. If you completed this worksheet last year, enter the amount from line 10 of last year's worksheet"
    type: NonNegDollars
    expr: {op: copy, from: retirement.recovered}
  - id: retirement.smw7
    printed: "(SMW 7)"
    label: "Subtract line 6 from line 2"
    type: Dollars
    expr: {op: subtract, from: retirement.smw2, take: retirement.smw6}
    note: "The worksheet states no floor, so the subtraction is literal. If line 6 exceeds line 2, lines 7 and 8 are negative and line 9 exceeds line 1. The text gives no rule for that case, and none is added."
  - id: retirement.smw8
    printed: "(SMW 8)"
    label: "Enter the smaller of line 5 or line 7"
    type: Dollars
    expr: {op: smaller_of, of: [retirement.smw5, retirement.smw7]}
  - id: retirement.smw9
    printed: "(SMW 9)"
    label: "Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero. Also, enter this amount on Form 1040 or 1040-SR, line 5b"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.smw1, take: retirement.smw8}
  - id: retirement.smw10
    printed: "(SMW 10)"
    label: "Was your annuity starting date before 1987? No. Add lines 6 and 8. This is the amount you have recovered tax free through 2025"
    type: Dollars
    expr: {op: sum, of: [retirement.smw6, retirement.smw8]}
    note: "Only the 'No' branch is encoded. Starting dates before 1987 are out of scope under the retirement.annuity and retirement.special questions, so the STOP on 'Yes' and the skip at line 5 cannot be reached."
  - id: retirement.smw11
    printed: "(SMW 11)"
    label: "Balance of cost to be recovered. Subtract line 10 from line 2"
    type: Dollars
    expr: {op: subtract, from: retirement.smw2, take: retirement.smw10}
  - id: retirement.h_rollover_over
    printed: "(helper)"
    label: "Check: the amount entered as rolled over is more than the distribution in box 1"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, ne: [retirement.code, {const: "direct_rollover_G"}]}
        - {op: test, gt: [retirement.rollover, retirement.box1]}
  - id: retirement.h_rolled
    printed: "(helper)"
    label: "Amount of the distribution rolled over (the whole distribution for a direct rollover, code G)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
          then: retirement.box1
        - guard: {op: test, ne: [retirement.code, {const: "direct_rollover_G"}]}
          then: retirement.rollover
    refuses:
      - {when: retirement.h_rollover_over, when_known: true}
  - id: retirement.has_rollover
    printed: "(helper)"
    label: "A rollover is reported: check box 1 on line 4c or line 5c"
    type: Bool
    expr: {op: test, gt: [retirement.h_rolled, {const: 0}]}
  - id: retirement.h_roth_8606
    printed: "(helper)"
    label: "A distribution from a Roth IRA without code Q: see Form 8606 and its instructions to figure the amount for line 4b"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.account, {const: "roth_ira"}]}
        - {op: test, ne: [retirement.code, {const: "qualified_roth_Q"}]}
    note: "The instructions also allow -0- on line 4b for code T with a Roth contribution for 2020 or earlier. The interface has no code T value or contribution-year fact, so code T arrives as 'other' and is refused."
  - id: retirement.h_q_not_roth
    printed: "(helper)"
    label: "Code Q on a distribution that is not from a Roth IRA"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.code, {const: "qualified_roth_Q"}]}
        - {op: test, ne: [retirement.account, {const: "roth_ira"}]}
    note: "The supplied pages give a code Q rule only for Roth IRAs (Exception 2, item 2b). They do not determine the taxable amount for code Q on a plan or a traditional IRA, so this case is refused."
  - id: retirement.h_other_code
    printed: "(helper)"
    label: "Box 7 shows another code, or two codes, whose treatment this slice does not determine"
    type: Bool
    expr: {op: test, eq: [retirement.code, {const: "other"}]}
  - id: retirement.h_annuity_rollover
    printed: "(helper)"
    label: "Check: a rollover is entered for payments figured on the Simplified Method Worksheet"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.account, {const: "plan"}]}
        - {op: test, eq: [retirement.annuity, {const: true}]}
        - {op: test, gt: [retirement.h_rolled, {const: 0}]}
    note: "The Simplified Method Worksheet has no line for a rollover, and the instructions do not combine the two computations. Chosen reading: treat the combination as a consistency failure and refuse it."
  - id: retirement.h_ira_taxable
    printed: "(helper)"
    label: "IRA other than a Roth IRA: the part not rolled over (line 4b)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.h_rolled}
  - id: retirement.h_plan_after_box5
    printed: "(helper)"
    label: "From box 1, subtract any contributions (usually shown in box 5) that were taxable to you when made"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.box5}
  - id: retirement.h_plan_remaining
    printed: "(helper)"
    label: "From that result, subtract the amount of the rollover. Enter the remaining amount on line 5b"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_plan_after_box5, take: retirement.h_rolled}
    note: "The text gives the box 5 subtraction only for rollovers. With no rollover and box 5 above zero, outside the Simplified Method and the General Rule screen, the pages do not state a formula. Chosen reading: box 1 minus box 5, reported as partially taxable. With box 5 and the rollover both zero, the result is the fully taxable box 1."
  - id: retirement.h_plan_taxable
    printed: "(helper)"
    label: "Pension or annuity: taxable amount for line 5b"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.annuity, {const: true}]}
          then: retirement.smw9
        - guard: {op: test, eq: [retirement.annuity, {const: false}]}
          then: retirement.h_plan_remaining
  - id: retirement.taxable
    printed: "(helper)"
    label: "Taxable amount of this distribution (Form 1040, line 4b or line 5b)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.account, {const: "roth_ira"}]}
          then: retirement.h_zero
        - guard: {op: test, eq: [retirement.account, {const: "traditional_ira"}]}
          then: retirement.h_ira_taxable
        - guard: {op: test, eq: [retirement.account, {const: "plan"}]}
          then: retirement.h_plan_taxable
    refuses:
      - retirement.special
      - retirement.h_roth_8606
      - retirement.h_q_not_roth
      - retirement.h_other_code
      - {when: retirement.h_annuity_rollover, when_known: true}
    note: "A Roth IRA reaches zero only with code Q (Exception 2, item 2b, 'enter -0- on line 4b'). Other Roth codes are refused."
  - id: retirement.h_partial
    printed: "(helper)"
    label: "The total distribution is entered on line 4a or line 5a (it is not simply fully taxable)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.account, {const: "roth_ira"}]}
        - {op: test, all: [{op: test, eq: [retirement.account, {const: "plan"}]}, {op: test, eq: [retirement.annuity, {const: true}]}]}
        - {op: test, eq: [retirement.has_rollover, {const: true}]}
        - {op: test, all: [{op: test, eq: [retirement.account, {const: "plan"}]}, {op: test, gt: [retirement.box5, {const: 0}]}]}
  - id: retirement.amount_a
    printed: "(helper)"
    label: "Amount for Form 1040, line 4a or line 5a. If the distribution is fully taxable, enter it on line 4b or 5b and make no entry on line 4a or 5a"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_partial, {const: true}]}
          then: retirement.box1
        - guard: {op: test, eq: [retirement.h_partial, {const: false}]}
          then: retirement.h_zero
    refuses:
      - retirement.special
      - retirement.h_roth_8606
      - retirement.h_q_not_roth
      - retirement.h_other_code
      - {when: retirement.h_annuity_rollover, when_known: true}
  - id: retirement.h_sav_excluded
    printed: "(helper)"
    label: "Form 8880, line 4: do not include distributions from a military retirement plan (other than the federal TSP), dividends under section 404(k), or distributions from an inherited IRA by a nonspousal beneficiary"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.sav_military, {const: true}]}
        - {op: test, eq: [retirement.sav_404k, {const: true}]}
        - {op: test, eq: [retirement.sav_inherited, {const: true}]}
  - id: retirement.h_sav_net
    printed: "(helper)"
    label: "Distribution less the part not taxable as the result of a rollover"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.h_rolled}
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
          then: retirement.h_sav_net
    refuses: [retirement.special, retirement.h_other_code]
    note: "Form 8880 line 4 counts distributions received, not their taxable part, so box 5 is not subtracted. Its other exclusions (excess contributions, returned contributions, Roth rollovers, plan loans) fall under the retirement.special and code screens."
  - id: retirement.h_early
    printed: "(helper)"
    label: "Box 7 shows an early distribution subject to the additional tax unless an exception is claimed (code 1 or code S)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.code, {const: "early_1"}]}
        - {op: test, eq: [retirement.code, {const: "simple_S"}]}
    note: "Open point: whether a code 2 distribution belongs on lines 1 and 2 when Form 5329 is filed for another reason. Chosen reading: leave it off both lines, because retirement.code_screen establishes that the exception covers all of it. Line 3 is the same either way."
  - id: retirement.l1
    printed: "(helper)"
    label: "Form 5329, line 1: early distributions includible in income"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_early, {const: true}]}
          then: retirement.taxable
        - guard: {op: test, eq: [retirement.h_early, {const: false}]}
          then: retirement.h_zero
    refuses: [retirement.early_screen, retirement.code_screen]
  - id: retirement.h_has_exception
    printed: "(helper)"
    label: "An exception to the additional tax on early distributions is claimed for this early distribution"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.h_early, {const: true}]}
        - {op: test, ne: [retirement.exception, {const: "none"}]}
  - id: retirement.h_exception_misplaced
    printed: "(helper)"
    label: "Check: exception 01 or 06 (does not apply to IRAs) on an IRA, or exception 07, 08 or 09 (IRA distributions) on a plan"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.h_early, {const: true}]}
        - op: test
          any:
            - op: test
              all:
                - {op: test, eq: [retirement.is_ira, {const: true}]}
                - {op: test, any: [{op: test, eq: [retirement.exception, {const: "e01"}]}, {op: test, eq: [retirement.exception, {const: "e06"}]}]}
            - op: test
              all:
                - {op: test, eq: [retirement.is_ira, {const: false}]}
                - {op: test, any: [{op: test, eq: [retirement.exception, {const: "e07"}]}, {op: test, eq: [retirement.exception, {const: "e08"}]}, {op: test, eq: [retirement.exception, {const: "e09"}]}]}
  - id: retirement.h_l2_amount
    printed: "(helper)"
    label: "Amount the exception covers, not more than the amount on line 1 for this distribution"
    type: NonNegDollars
    expr: {op: smaller_of, of: [retirement.exc_amount, retirement.l1]}
  - id: retirement.l2
    printed: "(helper)"
    label: "Form 5329, line 2: early distributions not subject to the additional tax, before the per-person dollar limits"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_has_exception, {const: true}]}
          then: retirement.h_l2_amount
        - guard: {op: test, eq: [retirement.h_has_exception, {const: false}]}
          then: retirement.h_zero
    refuses:
      - {when: retirement.h_exception_misplaced, when_known: true}
    note: "The dollar limits for exceptions 05, 09, 19, 22 and 23 are not applied here. The interface says the tool applies them per person, using the amounts split out below."
  - id: retirement.h_is_e05
    printed: "(helper)"
    label: "Exception 05 (medical expenses) is claimed for this early distribution"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [retirement.h_has_exception, {const: true}]}, {op: test, eq: [retirement.exception, {const: "e05"}]}]}
  - id: retirement.l2_e05
    printed: "(helper)"
    label: "Part of Form 5329, line 2 under exception 05"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_is_e05, {const: true}]}
          then: retirement.l2
        - guard: {op: test, eq: [retirement.h_is_e05, {const: false}]}
          then: retirement.h_zero
  - id: retirement.h_is_e09
    printed: "(helper)"
    label: "Exception 09 (first home) is claimed for this early distribution"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [retirement.h_has_exception, {const: true}]}, {op: test, eq: [retirement.exception, {const: "e09"}]}]}
  - id: retirement.l2_e09
    printed: "(helper)"
    label: "Part of Form 5329, line 2 under exception 09"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_is_e09, {const: true}]}
          then: retirement.l2
        - guard: {op: test, eq: [retirement.h_is_e09, {const: false}]}
          then: retirement.h_zero
  - id: retirement.h_is_e19
    printed: "(helper)"
    label: "Exception 19 (birth or adoption) is claimed for this early distribution"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [retirement.h_has_exception, {const: true}]}, {op: test, eq: [retirement.exception, {const: "e19"}]}]}
  - id: retirement.l2_e19
    printed: "(helper)"
    label: "Part of Form 5329, line 2 under exception 19"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_is_e19, {const: true}]}
          then: retirement.l2
        - guard: {op: test, eq: [retirement.h_is_e19, {const: false}]}
          then: retirement.h_zero
  - id: retirement.h_is_e22
    printed: "(helper)"
    label: "Exception 22 (victims of domestic abuse) is claimed for this early distribution"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [retirement.h_has_exception, {const: true}]}, {op: test, eq: [retirement.exception, {const: "e22"}]}]}
  - id: retirement.l2_e22
    printed: "(helper)"
    label: "Part of Form 5329, line 2 under exception 22"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_is_e22, {const: true}]}
          then: retirement.l2
        - guard: {op: test, eq: [retirement.h_is_e22, {const: false}]}
          then: retirement.h_zero
  - id: retirement.is_e23
    printed: "(helper)"
    label: "Exception 23 (eligible emergency expense distribution) is claimed for this early distribution"
    type: Bool
    expr: {op: test, all: [{op: test, eq: [retirement.h_has_exception, {const: true}]}, {op: test, eq: [retirement.exception, {const: "e23"}]}]}
  - id: retirement.l2_e23
    printed: "(helper)"
    label: "Part of Form 5329, line 2 under exception 23"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.is_e23, {const: true}]}
          then: retirement.l2
        - guard: {op: test, eq: [retirement.is_e23, {const: false}]}
          then: retirement.h_zero
  - id: retirement.h_is_s
    printed: "(helper)"
    label: "Designated with code S in box 7 (SIMPLE IRA distribution within 2 years of first participating)"
    type: Bool
    expr: {op: test, eq: [retirement.code, {const: "simple_S"}]}
  - id: retirement.l1_s
    printed: "(helper)"
    label: "Part of Form 5329, line 1 that is a code S distribution (line 4: multiply by 25% instead of 10%)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_is_s, {const: true}]}
          then: retirement.l1
        - guard: {op: test, eq: [retirement.h_is_s, {const: false}]}
          then: retirement.h_zero
  - id: retirement.l2_s
    printed: "(helper)"
    label: "Part of Form 5329, line 2 that is a code S distribution"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_is_s, {const: true}]}
          then: retirement.l2
        - guard: {op: test, eq: [retirement.h_is_s, {const: false}]}
          then: retirement.h_zero
```
