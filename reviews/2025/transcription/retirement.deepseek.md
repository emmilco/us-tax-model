# Transcription agreement — retirement

Second transcription of `Form 1099-R distributions (IRAs, pensions and annuities)` by an isolated model (spec 6.5), compared line by line with `forms/2025/retirement.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
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
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | fa349fb28ee871623fe147cb074c50407a0b8df7362d87eb400b780ed0baf272 |
| printed lines compared | 26 |
| agree / disagree / missing | 10 / 16 / 0 |
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
Status: **DISAGREE**

Project:

```json
{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}
```

Second:

```json
{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}
```

Ruling: representation; i1040gi p. 26, Lines 4a and 4b, IRA Distributions. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,026 partial records from 40 bases; 1,963 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,963 of 1,963 agree. Traditional or Roth IRA is the project's "account ≠ plan" over the three-valued Enum. Project stands.

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

Ruling: scope; i1040gi p. 30, Rollovers: "Use lines 5a and 5b to report a rollover, including a direct rollover, from one qualified employer’s plan to another or to an IRA. ... Also check box 1 on line 5c."; i1040gi p. 27, Exception 1: "Enter the total distribution on line 4a if you rolled over part or all of the distribution ... Also check box 1 on line 4c.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,026 partial records from 40 bases; 1,963 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,655 of 1,963 agree; 204 project-refuses (none completed), 104 project-unknown (none completed). No value differs and nothing differs on a completed return: the project-refuses are its cited retirement.bad_code (138) and retirement.special (66) read through retirement.rolled; the project-unknown are partial records withholding account, special or code, asked of every entry. Fix round 2 changed no retirement expression; it widened the retirement.special question (BUG-0243: military disability pension, an annuity received as beneficiary of an employee who died or shared among beneficiaries, a rollover of property other than cash or of a QDRO distribution), which reaches these lines only as a refusal. Project stands.

### retirement.taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: A Roth IRA distribution other than a qualified distribution generally requires Form 8606; the archived text does not supply the needed basis, so this line refuses the listed screening inputs and otherwise uses the distribution reduced by rollover and box 5.

Ruling: model error and scope; i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost ... of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a."; i1040gi p. 27, Lines 4a and 4b: "If the distribution from your IRA is fully taxable, enter the total distribution on line 4b; don’t make an entry on line 4a."; i1040gi p. 29, line 11. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,026 partial records from 40 bases; 1,963 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,679 of 1,963 agree; 137 project-refuses (none completed), 99 project-unknown (none completed), 36 candidate-unknown (14 completed), 12 value (8 completed). (1) Signed worksheet line 7 with no branch for a recovered or $0 cost: the 8 completed values are classm.tcw.15 r1 ($39,110.00 against $49,089.00) and 6 of its partials, and generated 395 r2 ($0.00 against $22,738.41). (2) It subtracts box 5 on every entry, IRAs included, so the 10 completed candidate-unknown on box 5 are partial records withholding it on IRA entries, where the interview does not ask it and p. 27 takes no box 5 (classm.s2.3.deepseek r1 traditional IRA code 1, project $92.00; classm.f5329.2.deepseek code S, $25,190.00; stage21.blind.e2); the other 4 completed are partials of classm.tcw.15 withholding worksheet answers. The project-refuses are its cited bad_code, annuity_rollover and screen_refused, and the project-unknown partial records: scope. Project stands.

### retirement.amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"input": "retirement.box5"}, {"const": 0}], "test": "le"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.box5"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Second:

```json
{"input": "retirement.box1"}
```

Ruling: model error and scope; i1040gi p. 27, Lines 4a and 4b: "If the distribution from your IRA is fully taxable, enter the total distribution on line 4b; don’t make an entry on line 4a."; i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost ... of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,026 partial records from 40 bases; 1,963 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 670 of 1,963 agree; 770 value (222 completed), 283 project-unknown (none completed), 211 project-refuses (none completed), 29 candidate-unknown (none completed). The reply copies box 1 to line 4a/5a on every entry. Each of the 222 completed values was checked against its record: in all 222 the project is $0.00 and the candidate equals box 1 on a fully taxable entry (traditional IRA codes 1, S, 7, 3, 4 and 2: 197; plan codes 7, 1, 2 and 4 with annuity false or a $0 or recovered cost: 25), e.g. classm.s2.3.deepseek $0.00 against $92.00, classm.tcw.15 $0.00 against $39,110.00. The other values are on refused or incomplete returns; the project-refuses are its cited gates and the project-unknown partial records: scope. Project stands.

### retirement.sav_amount — This distribution's amount on Form 8880 line 4
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "eq"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; f8880 p. 2, Line 4: "Don’t include any of the following. • Distributions not taxable as the result of a rollover or a trustee-to-trustee transfer ... • Distributions from a military retirement plan (other than the federal TSP). • Distributions from an inherited IRA by a nonspousal beneficiary". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,026 partial records from 40 bases; 1,963 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,703 of 1,963 agree; 126 project-refuses (none completed), 70 candidate-unknown (27 completed), 59 project-unknown (none completed), 5 candidate-refuses (none completed). No value differs. The 27 completed candidate-unknown are partial records withholding sav_military (12) or sav_404k (12) on IRA entries, or sav_inherited (3) on plan entries (amb.2025.savers_inherited_plans for the inherited reading). The project-refuses are its cited retirement.bad_code; the candidate-refuses and the project-unknown are on refused or incomplete returns: scope. Project stands.

### retirement.l1 — Form 5329 line 1 share: the taxable amount of an early distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 3, Line 1: "Enter the amount of early distributions includible in income (other than qualified disaster recovery distributions) that you received from:"; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99."; i5329 p. 5, exceptions to the additional tax: "Distributions due to death (doesn’t apply to modified endowment contracts)." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,026 partial records from 40 bases; 1,963 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,041 of 1,963 agree; 689 candidate-unknown (74 completed), 212 value (6 completed), 11 project-unknown (none completed), 9 candidate-refuses (none completed), 1 project-refuses (none completed). (1) The reply puts codes 2, 3 and 4 on line 1 and its line 2 sums only answered exception amounts, so nothing offsets them and line 3 bears the additional tax on distributions the code itself exempts: the 6 completed values are generated 22 (traditional IRA, code 4: $0.00 against $18,218.60), generated 175 (plan, code 2: $0.00 against $52,095.29), generated 314 r2 (plan, code 4: $0.00 against $46,209.90), generated 348 (code 2: $0.00 against $4,784.11), generated 381 (code 4: $0.00 against $42,337.61) and generated 421 (plan, code 4: $0.00 against $29,413.54); the 206 refused-return values are the same. This is not the second reading of amb.2025.f5329_line1_codes (chosen: line 1 holds only code 1 and S; the other reading puts code 2 on line 1 and offsets it on line 2; owner's decision D8(a)), which offsets the amount on line 2. (2) It declares early_screen, code_screen, special and its h_code_other as refusals of every entry (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused): 57 completed candidate-unknown need early_screen on other codes, 10 are partials withholding code_screen on code 1 or S entries, and 7 need box 5 on IRA entries through its taxable amount. The candidate-refuses are on refused returns and the project-refuses is its cited bad_code: scope. Project stands.

### retirement.l2 — Form 5329 line 2 share before the per-person limits
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Ruling: model error and scope; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,026 partial records from 40 bases; 1,963 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,236 of 1,963 agree; 712 candidate-unknown (76 completed), 10 candidate-refuses (none completed), 4 project-unknown (none completed), 1 project-refuses (none completed). No value differs. The reply declares early_screen, code_screen, special and h_code_other as refusals of every entry (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused) and tests the exception answer on every entry: of the 76 completed candidate-unknown, 57 need early_screen on other codes, 10 code_screen on code 1 or S entries, 7 the exception on entries it is not asked of (partials of generated 49, 90, 148, 181 and 199: codes 7, Q and 4) and 2 box 5 on IRA entries. The candidate-refuses are on refused returns; the project-refuses is its cited retirement.wrong_kind: scope. Project stands.

### retirement.l2_e05 — Line 2 share under exception 05
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,026 partial records from 40 bases; 1,963 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,233 of 1,963 agree; 719 candidate-unknown (75 completed), 10 candidate-refuses (none completed), 1 project-unknown (none completed). No value differs; the share is the project's wherever both compute. The reply declares early_screen, code_screen, special and h_code_other as refusals of the line on every entry (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused) and tests the exception on every entry: the completed candidate-unknown need early_screen on other codes (57), code_screen on code 1 or S entries (10), the exception on entries it is not asked of (7) or, for some, box 5 on an IRA entry through line 1. The candidate-refuses are on refused returns and the project-unknown partial records: scope. Project stands.

### retirement.l2_e09 — Line 2 share under exception 09
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,026 partial records from 40 bases; 1,963 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,232 of 1,963 agree; 721 candidate-unknown (74 completed), 10 candidate-refuses (none completed). No value differs; the share is the project's wherever both compute. The reply declares early_screen, code_screen, special and h_code_other as refusals of the line on every entry (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused) and tests the exception on every entry: the completed candidate-unknown need early_screen on other codes (57), code_screen on code 1 or S entries (10), the exception on entries it is not asked of (7) or, for some, box 5 on an IRA entry through line 1. The candidate-refuses are on refused returns and the project-unknown partial records: scope. Project stands.

### retirement.l2_e19 — Line 2 share under exception 19
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,026 partial records from 40 bases; 1,963 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,233 of 1,963 agree; 719 candidate-unknown (75 completed), 10 candidate-refuses (none completed), 1 project-unknown (none completed). No value differs; the share is the project's wherever both compute. The reply declares early_screen, code_screen, special and h_code_other as refusals of the line on every entry (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused) and tests the exception on every entry: the completed candidate-unknown need early_screen on other codes (57), code_screen on code 1 or S entries (10), the exception on entries it is not asked of (7) or, for some, box 5 on an IRA entry through line 1. The candidate-refuses are on refused returns and the project-unknown partial records: scope. Project stands.

### retirement.l2_e22 — Line 2 share under exception 22
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,026 partial records from 40 bases; 1,963 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,232 of 1,963 agree; 721 candidate-unknown (74 completed), 10 candidate-refuses (none completed). No value differs; the share is the project's wherever both compute. The reply declares early_screen, code_screen, special and h_code_other as refusals of the line on every entry (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused) and tests the exception on every entry: the completed candidate-unknown need early_screen on other codes (57), code_screen on code 1 or S entries (10), the exception on entries it is not asked of (7) or, for some, box 5 on an IRA entry through line 1. The candidate-refuses are on refused returns and the project-unknown partial records: scope. Project stands.

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

Ruling: model error; p590b p. 28, Emergency personal expense distributions, Distribution limits: "You are limited to taking one emergency personal expense distribution per calendar year"; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,026 partial records from 40 bases; 1,963 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,375 of 1,963 agree; 588 candidate-unknown (57 completed). It tests retirement.exception = e23 on every entry, so the 57 completed candidate-unknown need the exception answer on entries it is not asked of (classm.f8962.2.deepseek, classm.ira.2; project false). No value differs. Same reply as T-067 round 2. Project stands.

### retirement.l2_e23 — Line 2 share under exception 23
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99."; p590b p. 28, Emergency personal expense distributions, Distribution limits: "You are limited to taking one emergency personal expense distribution per calendar year". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,026 partial records from 40 bases; 1,963 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,232 of 1,963 agree; 721 candidate-unknown (74 completed), 10 candidate-refuses (none completed). No value differs; the share is the project's wherever both compute. The reply declares early_screen, code_screen, special and h_code_other as refusals of the line on every entry (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused) and tests the exception on every entry: the completed candidate-unknown need early_screen on other codes (57), code_screen on code 1 or S entries (10), the exception on entries it is not asked of (7) or, for some, box 5 on an IRA entry through line 1. The candidate-refuses are on refused returns and the project-unknown partial records: scope. Project stands.

### retirement.l1_s — Line 1 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 4: "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%. These distributions are included in boxes 1 and 2a of Form 1099-R and are designated with code S in box 7.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,026 partial records from 40 bases; 1,963 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,287 of 1,963 agree; 663 candidate-unknown (69 completed), 10 candidate-refuses (none completed), 2 project-unknown (none completed), 1 project-refuses (none completed). No value differs; the code S share is the project's. The reply declares early_screen, code_screen, special and h_code_other as refusals of every entry (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused): the completed candidate-unknown need early_screen on other codes (57), code_screen on code 1 or S entries (10) or box 5 on an IRA entry (2). The candidate-refuses are on refused returns; the project-refuses is its cited bad_code: scope. Project stands.

### retirement.l2_s — Line 2 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"input": "retirement.rollover"}], "op": "sum"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 4: "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%. These distributions are included in boxes 1 and 2a of Form 1099-R and are designated with code S in box 7.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,026 partial records from 40 bases; 1,963 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,287 of 1,963 agree; 666 candidate-unknown (67 completed), 10 candidate-refuses (none completed). No value differs; the code S share is the project's. The reply declares early_screen, code_screen, special and h_code_other as refusals of every entry (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused): the completed candidate-unknown need early_screen on other codes (57), code_screen on code 1 or S entries (10). The candidate-refuses are on refused returns; the project-refuses is its cited bad_code: scope. Project stands.

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
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"input": "retirement.last_line4"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.used_last_year"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 110, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"input": "retirement.cost"}, "op": "multiply_rate", "rate": {"param": "smw.table2_410"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 120, "type": "Count"}], "test": "le"}, {"args": [{"const": 110, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"input": "retirement.cost"}, "op": "multiply_rate", "rate": {"param": "smw.table2_360"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 130, "type": "Count"}], "test": "le"}, {"args": [{"const": 120, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"input": "retirement.cost"}, "op": "multiply_rate", "rate": {"param": "smw.table2_310"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 140, "type": "Count"}], "test": "le"}, {"args": [{"const": 130, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"input": "retirement.cost"}, "op": "multiply_rate", "rate": {"param": "smw.table2_260"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": 140, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"input": "retirement.cost"}, "op": "multiply_rate", "rate": {"param": "smw.table2_210"}}}, {"guard": {"args": [{"args": [{"input": "retirement.age"}, {"const": 55, "type": "Count"}], "test": "le"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"input": "retirement.cost"}, "op": "multiply_rate", "rate": {"param": "smw.table1_360"}}}, {"guard": {"args": [{"args": [{"input": "retirement.age"}, {"const": 60, "type": "Count"}], "test": "le"}, {"args": [{"const": 55, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"input": "retirement.cost"}, "op": "multiply_rate", "rate": {"param": "smw.table1_310"}}}, {"guard": {"args": [{"args": [{"input": "retirement.age"}, {"const": 65, "type": "Count"}], "test": "le"}, {"args": [{"const": 60, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"input": "retirement.cost"}, "op": "multiply_rate", "rate": {"param": "smw.table1_260"}}}, {"guard": {"args": [{"args": [{"input": "retirement.age"}, {"const": 70, "type": "Count"}], "test": "le"}, {"args": [{"const": 65, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"input": "retirement.cost"}, "op": "multiply_rate", "rate": {"param": "smw.table1_210"}}}, {"guard": {"args": [{"args": [{"const": 70, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "ne"}], "test": "all"}, "then": {"amount": {"input": "retirement.cost"}, "op": "multiply_rate", "rate": {"param": "smw.table1_160"}}}], "op": "choose"}}], "op": "choose"}
```

Ruling: model error; i1040gi p. 29, Simplified Method Worksheet, line 4; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity."; i1040gi p. 28, Fully Taxable Pensions and Annuities: "(a) you didn’t contribute to the cost ... or (b) you got your entire cost back tax free before 2025". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 1,026 partial records from 40 bases; 1,963 comparisons; every witness re-read from an uncapped scratch re-run of triage.mjs, same counts): 1,600 of 1,963 agree; 318 candidate-unknown (106 completed), 45 candidate-shows-skipped (1 completed). All differences are on entries where the project hides the line (retirement.smw_shown false: an IRA, a non-annuity plan entry, or an annuity whose cost is $0 or was recovered before 2025). The reply gives the worksheet lines no hiding condition, so it shows or asks for line 4 on entries the source never takes through the worksheet: the 1 completed candidate-shows-skipped is generated 395 r2 (cost recovered: $1,550.08 from last year's line 4); the completed candidate-unknown need used_last_year or other worksheet answers on such entries (stage15.f8880.s1, stage21.example.tom_jones, partials of classm.s2.3.deepseek and classm.tcw.15). Its value is the project's wherever the project shows the line. retirement.smw_shown is unchanged since T-067 round 2. Project stands.

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
| retirement.taxable | retirement.h_code_other, retirement.special | retirement.h_code_other |
| retirement.sav_amount | retirement.h_code_other, retirement.special | retirement.h_code_other |
| retirement.l1 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other |
| retirement.l2 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other |
| retirement.l2_e05 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other |
| retirement.l2_e09 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other |
| retirement.l2_e19 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other |
| retirement.l2_e22 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other |
| retirement.l2_e23 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other |
| retirement.l1_s | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other |
| retirement.l2_s | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other |

## Raw second transcription

```yaml
lines:
  - id: retirement.smw1
    printed: "(SMW 1)"
    label: "Enter the total pension or annuity payments from Form 1099-R, box 1. Also, enter this amount on Form 1040 or 1040-SR, line 5a"
    type: NonNegDollars
    expr:
      op: copy
      from: retirement.box1
  - id: retirement.smw2
    printed: "(SMW 2)"
    label: "Enter your cost in the plan at the annuity starting date"
    type: NonNegDollars
    expr:
      op: copy
      from: retirement.cost
  - id: retirement.smw4
    printed: "(SMW 4)"
    label: "Divide line 2 by the number on line 3"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [retirement.h_used_last, {const: true}]
          then: retirement.last_line4
        - guard:
            op: test
            eq: [retirement.h_used_last, {const: false}]
          then: retirement.h_smw4_calc
  - id: retirement.smw5
    printed: "(SMW 5)"
    label: "Multiply line 4 by the number of months for which this year's payments were made. If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8. Otherwise, go to line 6"
    type: NonNegDollars
    expr:
      op: multiply_count
      amount: retirement.smw4
      count: retirement.months
  - id: retirement.smw6
    printed: "(SMW 6)"
    label: "Enter the amount, if any, recovered tax free in years after 1986. If you completed this worksheet last year, enter the amount from line 10 of last year's worksheet"
    type: NonNegDollars
    expr:
      op: copy
      from: retirement.recovered
  - id: retirement.smw7
    printed: "(SMW 7)"
    label: "Subtract line 6 from line 2"
    type: Dollars
    expr:
      op: subtract
      from: retirement.smw2
      take: retirement.smw6
  - id: retirement.smw8
    printed: "(SMW 8)"
    label: "Enter the smaller of line 5 or line 7"
    type: Dollars
    expr:
      op: smaller_of
      of: [retirement.smw5, retirement.smw7]
  - id: retirement.smw9
    printed: "(SMW 9)"
    label: "Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero. Also, enter this amount on Form 1040 or 1040-SR, line 5b. If your Form 1099-R shows a larger amount, use the amount on this line instead of the amount from Form 1099-R. If you are a retired public safety officer, see Insurance Premiums for Retired Public Safety Officers before entering an amount on line 5b"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: retirement.smw1
      take: retirement.smw8
  - id: retirement.smw10
    printed: "(SMW 10)"
    label: "Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet. No. Add lines 6 and 8. This is the amount you have recovered tax free through 2025. You will need this number if you need to fill out this worksheet next year"
    type: Dollars
    expr:
      op: sum
      of: [retirement.smw6, retirement.smw8]
  - id: retirement.smw11
    printed: "(SMW 11)"
    label: "Balance of cost to be recovered. Subtract line 10 from line 2. If zero, you won't have to complete this worksheet next year. The payments you receive next year will generally be fully taxable"
    type: Dollars
    expr:
      op: subtract
      from: retirement.smw2
      take: retirement.smw10
  - id: retirement.one
    printed: "(helper)"
    label: "Number of this Form 1099-R distribution"
    type: Count
    expr:
      op: param
      ref: person.one
  - id: retirement.is_ira
    printed: "(helper)"
    label: "Is this distribution from an IRA (traditional or Roth)?"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          eq: [retirement.h_is_traditional, {const: true}]
        - op: test
          eq: [retirement.h_is_roth, {const: true}]
  - id: retirement.has_rollover
    printed: "(helper)"
    label: "Was any part of this distribution rolled over, including a direct rollover?"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          eq: [retirement.h_code_direct, {const: true}]
        - op: test
          eq: [retirement.h_rollover_pos, {const: true}]
  - id: retirement.taxable
    printed: "(helper)"
    label: "Taxable amount of this distribution"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [retirement.h_taxable_zero_case, {const: true}]
          then: retirement.h_zero
        - guard:
            op: test
            eq: [retirement.h_taxable_annuity_case, {const: true}]
          then: retirement.smw9
        - guard:
            op: test
            all:
              - op: test
                eq: [retirement.h_taxable_zero_case, {const: false}]
              - op: test
                eq: [retirement.h_taxable_annuity_case, {const: false}]
          then: retirement.h_after_reductions
    refuses: [retirement.special, retirement.h_code_other]
    note: "A Roth IRA distribution other than a qualified distribution generally requires Form 8606; the archived text does not supply the needed basis, so this line refuses the listed screening inputs and otherwise uses the distribution reduced by rollover and box 5."
  - id: retirement.amount_a
    printed: "(helper)"
    label: "Amount of this distribution to report on Form 1040 line 4a or 5a"
    type: NonNegDollars
    expr:
      op: copy
      from: retirement.box1
  - id: retirement.sav_amount
    printed: "(helper)"
    label: "Amount of this distribution included in Form 8880 line 4"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [retirement.h_sav_excluded, {const: true}]
          then: retirement.h_zero
        - guard:
            op: test
            eq: [retirement.h_sav_excluded, {const: false}]
          then: retirement.h_sav_after_rollover
    refuses: [retirement.special, retirement.h_code_other]
  - id: retirement.l1
    printed: "(helper)"
    label: "Form 5329 line 1 early distribution amount"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [retirement.h_early_subject, {const: true}]
          then: retirement.taxable
        - guard:
            op: test
            eq: [retirement.h_early_subject, {const: false}]
          then: retirement.h_zero
    refuses: [retirement.early_screen, retirement.code_screen, retirement.special, retirement.h_code_other]
  - id: retirement.l2
    printed: "(helper)"
    label: "Form 5329 line 2 exception amount"
    type: NonNegDollars
    expr:
      op: sum
      of: [retirement.h_exc_other, retirement.l2_e05, retirement.l2_e09, retirement.l2_e19, retirement.l2_e22, retirement.l2_e23]
    refuses: [retirement.early_screen, retirement.code_screen, retirement.special, retirement.h_code_other]
  - id: retirement.l2_e05
    printed: "(helper)"
    label: "Form 5329 line 2 amount for exception 05"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [retirement.h_exc_e05, {const: true}]
          then: retirement.h_exc_capped
        - guard:
            op: test
            eq: [retirement.h_exc_e05, {const: false}]
          then: retirement.h_zero
    refuses: [retirement.early_screen, retirement.code_screen, retirement.special, retirement.h_code_other]
  - id: retirement.l2_e09
    printed: "(helper)"
    label: "Form 5329 line 2 amount for exception 09"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [retirement.h_exc_e09, {const: true}]
          then: retirement.h_exc_capped
        - guard:
            op: test
            eq: [retirement.h_exc_e09, {const: false}]
          then: retirement.h_zero
    refuses: [retirement.early_screen, retirement.code_screen, retirement.special, retirement.h_code_other]
  - id: retirement.l2_e19
    printed: "(helper)"
    label: "Form 5329 line 2 amount for exception 19"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [retirement.h_exc_e19, {const: true}]
          then: retirement.h_exc_capped
        - guard:
            op: test
            eq: [retirement.h_exc_e19, {const: false}]
          then: retirement.h_zero
    refuses: [retirement.early_screen, retirement.code_screen, retirement.special, retirement.h_code_other]
  - id: retirement.l2_e22
    printed: "(helper)"
    label: "Form 5329 line 2 amount for exception 22"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [retirement.h_exc_e22, {const: true}]
          then: retirement.h_exc_capped
        - guard:
            op: test
            eq: [retirement.h_exc_e22, {const: false}]
          then: retirement.h_zero
    refuses: [retirement.early_screen, retirement.code_screen, retirement.special, retirement.h_code_other]
  - id: retirement.is_e23
    printed: "(helper)"
    label: "Is exception 23, emergency personal expense distribution, claimed?"
    type: Bool
    expr:
      op: copy
      from: retirement.h_exc_e23
  - id: retirement.l2_e23
    printed: "(helper)"
    label: "Form 5329 line 2 amount for exception 23"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [retirement.h_exc_e23, {const: true}]
          then: retirement.h_exc_capped
        - guard:
            op: test
            eq: [retirement.h_exc_e23, {const: false}]
          then: retirement.h_zero
    refuses: [retirement.early_screen, retirement.code_screen, retirement.special, retirement.h_code_other]
  - id: retirement.l1_s
    printed: "(helper)"
    label: "SIMPLE IRA portion of Form 5329 line 1"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [retirement.h_code_simple, {const: true}]
          then: retirement.l1
        - guard:
            op: test
            eq: [retirement.h_code_simple, {const: false}]
          then: retirement.h_zero
    refuses: [retirement.early_screen, retirement.code_screen, retirement.special, retirement.h_code_other]
  - id: retirement.l2_s
    printed: "(helper)"
    label: "SIMPLE IRA portion of Form 5329 line 2"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [retirement.h_code_simple, {const: true}]
          then: retirement.l2
        - guard:
            op: test
            eq: [retirement.h_code_simple, {const: false}]
          then: retirement.h_zero
    refuses: [retirement.early_screen, retirement.code_screen, retirement.special, retirement.h_code_other]
  - id: retirement.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr:
      op: param
      ref: ss.zero
  - id: retirement.h_code_direct
    printed: "(helper)"
    label: "Distribution code is direct rollover G"
    type: Bool
    expr:
      op: test
      eq: [retirement.code, {const: "direct_rollover_G"}]
  - id: retirement.h_code_q
    printed: "(helper)"
    label: "Distribution code is qualified Roth Q"
    type: Bool
    expr:
      op: test
      eq: [retirement.code, {const: "qualified_roth_Q"}]
  - id: retirement.h_code_early1
    printed: "(helper)"
    label: "Distribution code is early distribution 1"
    type: Bool
    expr:
      op: test
      eq: [retirement.code, {const: "early_1"}]
  - id: retirement.h_code_simple
    printed: "(helper)"
    label: "Distribution code is SIMPLE IRA S"
    type: Bool
    expr:
      op: test
      eq: [retirement.code, {const: "simple_S"}]
  - id: retirement.h_code_2
    printed: "(helper)"
    label: "Distribution code is early distribution with exception 2"
    type: Bool
    expr:
      op: test
      eq: [retirement.code, {const: "early_exception_2"}]
  - id: retirement.h_code_disability
    printed: "(helper)"
    label: "Distribution code is disability 3"
    type: Bool
    expr:
      op: test
      eq: [retirement.code, {const: "disability_3"}]
  - id: retirement.h_code_death
    printed: "(helper)"
    label: "Distribution code is death 4"
    type: Bool
    expr:
      op: test
      eq: [retirement.code, {const: "death_4"}]
  - id: retirement.h_code_other
    printed: "(helper)"
    label: "Distribution code is other"
    type: Bool
    expr:
      op: test
      eq: [retirement.code, {const: "other"}]
  - id: retirement.h_rollover_pos
    printed: "(helper)"
    label: "Rollover amount is greater than zero"
    type: Bool
    expr:
      op: test
      gt: [retirement.rollover, {const: 0}]
  - id: retirement.h_is_traditional
    printed: "(helper)"
    label: "Account is a traditional IRA"
    type: Bool
    expr:
      op: test
      eq: [retirement.account, {const: "traditional_ira"}]
  - id: retirement.h_is_roth
    printed: "(helper)"
    label: "Account is a Roth IRA"
    type: Bool
    expr:
      op: test
      eq: [retirement.account, {const: "roth_ira"}]
  - id: retirement.h_is_plan
    printed: "(helper)"
    label: "Account is a pension or plan"
    type: Bool
    expr:
      op: test
      eq: [retirement.account, {const: "plan"}]
  - id: retirement.h_reductions
    printed: "(helper)"
    label: "Box 5 plus rollover amount"
    type: NonNegDollars
    expr:
      op: sum
      of: [retirement.box5, retirement.rollover]
  - id: retirement.h_after_reductions
    printed: "(helper)"
    label: "Box 1 less box 5 and rollover"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: retirement.box1
      take: retirement.h_reductions
  - id: retirement.h_taxable_zero_case
    printed: "(helper)"
    label: "Taxable amount is zero because of a qualified Roth distribution or direct rollover"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          eq: [retirement.h_code_q, {const: true}]
        - op: test
          eq: [retirement.h_code_direct, {const: true}]
  - id: retirement.h_taxable_annuity_case
    printed: "(helper)"
    label: "Taxable amount comes from the Simplified Method"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          eq: [retirement.h_is_plan, {const: true}]
        - op: test
          eq: [retirement.annuity, {const: true}]
  - id: retirement.h_sav_excluded
    printed: "(helper)"
    label: "Distribution excluded from Form 8880 line 4"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          eq: [retirement.sav_military, {const: true}]
        - op: test
          eq: [retirement.sav_404k, {const: true}]
        - op: test
          eq: [retirement.sav_inherited, {const: true}]
        - op: test
          eq: [retirement.h_code_direct, {const: true}]
  - id: retirement.h_sav_after_rollover
    printed: "(helper)"
    label: "Distribution less rollover for Form 8880 line 4"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: retirement.box1
      take: retirement.rollover
  - id: retirement.h_early_subject
    printed: "(helper)"
    label: "Distribution is an early distribution type for Form 5329"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          eq: [retirement.h_code_early1, {const: true}]
        - op: test
          eq: [retirement.h_code_simple, {const: true}]
        - op: test
          eq: [retirement.h_code_2, {const: true}]
        - op: test
          eq: [retirement.h_code_disability, {const: true}]
        - op: test
          eq: [retirement.h_code_death, {const: true}]
  - id: retirement.h_exc_capped
    printed: "(helper)"
    label: "Exception amount limited to the early distribution amount"
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [retirement.exc_amount, retirement.l1]
  - id: retirement.h_exc_e05
    printed: "(helper)"
    label: "Exception is 05"
    type: Bool
    expr:
      op: test
      eq: [retirement.exception, {const: "e05"}]
  - id: retirement.h_exc_e09
    printed: "(helper)"
    label: "Exception is 09"
    type: Bool
    expr:
      op: test
      eq: [retirement.exception, {const: "e09"}]
  - id: retirement.h_exc_e19
    printed: "(helper)"
    label: "Exception is 19"
    type: Bool
    expr:
      op: test
      eq: [retirement.exception, {const: "e19"}]
  - id: retirement.h_exc_e22
    printed: "(helper)"
    label: "Exception is 22"
    type: Bool
    expr:
      op: test
      eq: [retirement.exception, {const: "e22"}]
  - id: retirement.h_exc_e23
    printed: "(helper)"
    label: "Exception is 23"
    type: Bool
    expr:
      op: test
      eq: [retirement.exception, {const: "e23"}]
  - id: retirement.h_exc_specific
    printed: "(helper)"
    label: "Exception is one of the separately reported exceptions"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          eq: [retirement.h_exc_e05, {const: true}]
        - op: test
          eq: [retirement.h_exc_e09, {const: true}]
        - op: test
          eq: [retirement.h_exc_e19, {const: true}]
        - op: test
          eq: [retirement.h_exc_e22, {const: true}]
        - op: test
          eq: [retirement.h_exc_e23, {const: true}]
  - id: retirement.h_exc_none
    printed: "(helper)"
    label: "Exception is none"
    type: Bool
    expr:
      op: test
      eq: [retirement.exception, {const: "none"}]
  - id: retirement.h_exc_other_case
    printed: "(helper)"
    label: "Exception is another exception not separately reported"
    type: Bool
    expr:
      op: test
      all:
        - op: test
          eq: [retirement.h_exc_none, {const: false}]
        - op: test
          eq: [retirement.h_exc_specific, {const: false}]
  - id: retirement.h_exc_other
    printed: "(helper)"
    label: "Exception amount for exceptions other than 05, 09, 19, 22 and 23"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            eq: [retirement.h_exc_other_case, {const: true}]
          then: retirement.h_exc_capped
        - guard:
            op: test
            eq: [retirement.h_exc_other_case, {const: false}]
          then: retirement.h_zero
  - id: retirement.h_used_last
    printed: "(helper)"
    label: "Simplified Method Worksheet was completed last year"
    type: Bool
    expr:
      op: test
      eq: [retirement.used_last_year, {const: true}]
  - id: retirement.h_age_le55
    printed: "(helper)"
    label: "Age at annuity starting date is 55 or under"
    type: Bool
    expr:
      op: test
      le: [retirement.age, {const: 55, type: Count}]
  - id: retirement.h_age_le60
    printed: "(helper)"
    label: "Age at annuity starting date is 60 or under"
    type: Bool
    expr:
      op: test
      le: [retirement.age, {const: 60, type: Count}]
  - id: retirement.h_age_le65
    printed: "(helper)"
    label: "Age at annuity starting date is 65 or under"
    type: Bool
    expr:
      op: test
      le: [retirement.age, {const: 65, type: Count}]
  - id: retirement.h_age_le70
    printed: "(helper)"
    label: "Age at annuity starting date is 70 or under"
    type: Bool
    expr:
      op: test
      le: [retirement.age, {const: 70, type: Count}]
  - id: retirement.h_comb_le110
    printed: "(helper)"
    label: "Combined ages at annuity starting date are 110 or under"
    type: Bool
    expr:
      op: test
      le: [retirement.combined_age, {const: 110, type: Count}]
  - id: retirement.h_comb_le120
    printed: "(helper)"
    label: "Combined ages at annuity starting date are 120 or under"
    type: Bool
    expr:
      op: test
      le: [retirement.combined_age, {const: 120, type: Count}]
  - id: retirement.h_comb_le130
    printed: "(helper)"
    label: "Combined ages at annuity starting date are 130 or under"
    type: Bool
    expr:
      op: test
      le: [retirement.combined_age, {const: 130, type: Count}]
  - id: retirement.h_comb_le140
    printed: "(helper)"
    label: "Combined ages at annuity starting date are 140 or under"
    type: Bool
    expr:
      op: test
      le: [retirement.combined_age, {const: 140, type: Count}]
  - id: retirement.h_table2
    printed: "(helper)"
    label: "Use Table 2 for joint and survivor annuity"
    type: Bool
    expr:
      op: test
      eq: [retirement.joint_life, {const: true}]
  - id: retirement.h_smw_t1_360
    printed: "(helper)"
    label: "Cost times 1/360"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: retirement.cost
      rate: {param: smw.table1_360}
  - id: retirement.h_smw_t1_310
    printed: "(helper)"
    label: "Cost times 1/310"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: retirement.cost
      rate: {param: smw.table1_310}
  - id: retirement.h_smw_t1_260
    printed: "(helper)"
    label: "Cost times 1/260"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: retirement.cost
      rate: {param: smw.table1_260}
  - id: retirement.h_smw_t1_210
    printed: "(helper)"
    label: "Cost times 1/210"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: retirement.cost
      rate: {param: smw.table1_210}
  - id: retirement.h_smw_t1_160
    printed: "(helper)"
    label: "Cost times 1/160"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: retirement.cost
      rate: {param: smw.table1_160}
  - id: retirement.h_smw_t2_410
    printed: "(helper)"
    label: "Cost times 1/410"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: retirement.cost
      rate: {param: smw.table2_410}
  - id: retirement.h_smw_t2_360
    printed: "(helper)"
    label: "Cost times 1/360"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: retirement.cost
      rate: {param: smw.table2_360}
  - id: retirement.h_smw_t2_310
    printed: "(helper)"
    label: "Cost times 1/310"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: retirement.cost
      rate: {param: smw.table2_310}
  - id: retirement.h_smw_t2_260
    printed: "(helper)"
    label: "Cost times 1/260"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: retirement.cost
      rate: {param: smw.table2_260}
  - id: retirement.h_smw_t2_210
    printed: "(helper)"
    label: "Cost times 1/210"
    type: NonNegDollars
    expr:
      op: multiply_rate
      amount: retirement.cost
      rate: {param: smw.table2_210}
  - id: retirement.h_smw4_calc
    printed: "(helper)"
    label: "Line 4 amount before the last-year override"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - op: test
                eq: [retirement.h_table2, {const: true}]
              - op: test
                eq: [retirement.h_comb_le110, {const: true}]
          then: retirement.h_smw_t2_410
        - guard:
            op: test
            all:
              - op: test
                eq: [retirement.h_table2, {const: true}]
              - op: test
                eq: [retirement.h_comb_le110, {const: false}]
              - op: test
                eq: [retirement.h_comb_le120, {const: true}]
          then: retirement.h_smw_t2_360
        - guard:
            op: test
            all:
              - op: test
                eq: [retirement.h_table2, {const: true}]
              - op: test
                eq: [retirement.h_comb_le120, {const: false}]
              - op: test
                eq: [retirement.h_comb_le130, {const: true}]
          then: retirement.h_smw_t2_310
        - guard:
            op: test
            all:
              - op: test
                eq: [retirement.h_table2, {const: true}]
              - op: test
                eq: [retirement.h_comb_le130, {const: false}]
              - op: test
                eq: [retirement.h_comb_le140, {const: true}]
          then: retirement.h_smw_t2_260
        - guard:
            op: test
            all:
              - op: test
                eq: [retirement.h_table2, {const: true}]
              - op: test
                eq: [retirement.h_comb_le140, {const: false}]
          then: retirement.h_smw_t2_210
        - guard:
            op: test
            all:
              - op: test
                eq: [retirement.h_table2, {const: false}]
              - op: test
                eq: [retirement.h_age_le55, {const: true}]
          then: retirement.h_smw_t1_360
        - guard:
            op: test
            all:
              - op: test
                eq: [retirement.h_table2, {const: false}]
              - op: test
                eq: [retirement.h_age_le55, {const: false}]
              - op: test
                eq: [retirement.h_age_le60, {const: true}]
          then: retirement.h_smw_t1_310
        - guard:
            op: test
            all:
              - op: test
                eq: [retirement.h_table2, {const: false}]
              - op: test
                eq: [retirement.h_age_le60, {const: false}]
              - op: test
                eq: [retirement.h_age_le65, {const: true}]
          then: retirement.h_smw_t1_260
        - guard:
            op: test
            all:
              - op: test
                eq: [retirement.h_table2, {const: false}]
              - op: test
                eq: [retirement.h_age_le65, {const: false}]
              - op: test
                eq: [retirement.h_age_le70, {const: true}]
          then: retirement.h_smw_t1_210
        - guard:
            op: test
            all:
              - op: test
                eq: [retirement.h_table2, {const: false}]
              - op: test
                eq: [retirement.h_age_le70, {const: false}]
          then: retirement.h_smw_t1_160
```
