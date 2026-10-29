# Transcription agreement — retirement

Second transcription of `Form 1099-R distributions (IRAs, pensions and annuities)` by an isolated model (spec 6.5), compared line by line with `forms/2025/retirement.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 429197e7a87463e33568c623a7d562f20c8756c7b581786ad99304d4aaae58cb |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | d8282414508313a7c0299716cfd79f84ecfc9e061fb8baf8dfa5abb2639ef557 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | e8a1c9d67cd082139c530c2a967cc95f7b7286b013e308b047c029d62be0fa7a |
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

Ruling: representation; i1040gi p. 26, Lines 4a and 4b, IRA Distributions (the IRA lines take traditional and Roth IRA distributions; the account Enum is traditional_ira, roth_ira or plan). The candidate tests account = traditional_ira or roth_ira; the project tests account ≠ plan, the same set over the three-valued Enum. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,374 fixtures, 500 generated returns seed 20261026, 1,085 partial records from 40 bases; 2,387 comparisons): 2,387 of 2,387 agree. Same reply text as round 3. Project stands.

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

Ruling: scope; i1040gi p. 30, Rollovers: "Use lines 5a and 5b to report a rollover, including a direct rollover, from one qualified employer’s plan to another or to an IRA. ... Also check box 1 on line 5c."; i1040gi p. 27, Exception 1: "Enter the total distribution on line 4a if you rolled over part or all of the distribution ... Also check box 1 on line 4c.". The candidate's test (code G, or a rollover amount above zero) is the project's. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,374 fixtures, 500 generated returns seed 20261026, 1,085 partial records from 40 bases; 2,387 comparisons): 1,989 of 2,387 agree; 289 project-refuses (none completed), 109 project-unknown (none completed). Every difference is the project's: it reads retirement.rolled, which carries the cited refusals retirement.special and retirement.bad_code (refused returns, for example classm.w2.1.deepseek on bad_code and classm.f8606.1 on special); the project-unknown are partial records that withhold retirement.account or retirement.special, which the project needs of every entry. No value differs. Same reply as round 3. Project stands.

### retirement.taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}}, {"guard": {"args": [{"args": [{"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost ... or (b) you got your entire cost back tax free before 2025 ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a."; i1040gi p. 29, Simplified Method Worksheet, lines 7 to 9: "Subtract line 6 from line 2", "Enter the smaller of line 5 or line 7", "Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero", and line 11: "If zero, ... The payments you receive next year will generally be fully taxable". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,374 fixtures, 500 generated returns seed 20261026, 1,085 partial records from 40 bases; 2,387 comparisons): 2,055 of 2,387 agree; 229 project-refuses (none completed), 58 project-unknown (none completed), 39 candidate-unknown (16 completed), 6 value (2 completed). (1) Its Simplified Method line 7 is signed, so when the answers put the amount recovered above the cost its line 8 is negative and line 9 exceeds box 1, where the source makes the payments fully taxable: classm.tcw.15 (completed; cost $0, recovered $9,979, box 1 $39,110) project $39,110.00, candidate $49,089.00; generated 395 (completed; box 1 $0) project $0.00, candidate $22,738.41; also classm.tcw.14 and generated 43 and 229 (refused), stage10.smw.recovered_exceeds_cost (incomplete). Same as round 3. (2) It has no account branch, so it reads box 5 and the annuity answer on IRA entries, which the source does not use for line 4b (i1040gi p. 27, line 4b) and the project does not need: partials of classm.s2.3.deepseek withholding retirement.box5 or retirement.annuity (completed; traditional IRA, code 1) project $92.00, candidate unknown. Its round-3 (SMW 4) error is gone. (3) The project-refuses are its cited retirement.bad_code, retirement.annuity_rollover, retirement.special and retirement.screen_refused: scope; the project-unknown are partial records withholding a cited screen the entry is asked. Project stands.

### retirement.amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"input": "retirement.box5"}, {"const": 0}], "test": "le"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.box5"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}], "test": "any"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Ruling: model error and scope; i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost ... or (b) you got your entire cost back tax free before 2025 ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a."; i1040gi p. 30, Rollovers: "Enter on line 5a the distribution from Form 1099-R, box 1. From this amount, subtract any contributions (usually shown in box 5) that were taxable to you when made". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,374 fixtures, 500 generated returns seed 20261026, 1,085 partial records from 40 bases; 2,387 comparisons): 1,973 of 2,387 agree; 254 project-refuses (none completed), 94 project-unknown (none completed), 35 value (3 completed), 31 candidate-unknown (8 completed). The candidate now enters box 1 on line 4a/5a only for a rollover, a code Q or other Roth entry, or a Simplified Method annuity. (1) A plan distribution with employee contributions in box 5 is not fully taxable, so box 1 goes on line 5a as the project enters it; the candidate leaves line 5a blank: classm.ira.2 (completed; plan, code 2, box 1 $20,743, box 5 $661) project $20,743.00, candidate $0.00; stage10.plan.box5 and stage10.mixed.ira_and_plan (incomplete) $12,000.00 against $0.00. (2) It enters box 1 for a Simplified Method annuity whose cost is already recovered and is fully taxable: classm.tcw.15 (completed) project $0.00, candidate $39,110.00; stage10.smw.cost_recovered (incomplete). (3) It reads the annuity answer on IRA entries, which the project does not need: partial of classm.s2.3.deepseek withholding retirement.annuity (completed; traditional IRA) project $0.00, candidate unknown. (4) The project-refuses are cited gates (retirement.bad_code, retirement.annuity_rollover): scope; the project-unknown are partial records withholding retirement.account or a cited screen. The round-3 reply had no completed difference; this one regresses. Project stands.

### retirement.sav_amount — This distribution's amount on Form 8880 line 4
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "eq"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.sav_404k"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.sav_inherited"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.sav_military"}], "test": "eq"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": false}, {"input": "retirement.sav_404k"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.sav_military"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": false}, {"input": "retirement.sav_military"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "eq"}], "test": "all"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; f8880 p. 2, Line 4: "Don’t include any of the following. • Distributions not taxable as the result of a rollover or a trustee-to-trustee transfer ... • Distributions from a military retirement plan (other than the federal TSP). • Distributions from an inherited IRA by a nonspousal beneficiary". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,374 fixtures, 500 generated returns seed 20261026, 1,085 partial records from 40 bases; 2,387 comparisons): 2,086 of 2,387 agree; 159 project-refuses (none completed), 83 candidate-unknown (20 completed), 55 project-unknown (none completed), 4 candidate-refuses (none completed). The amount (box 1 less the rollover, the whole box 1 on a code G entry) is the project's; no value differs. As in round 3 it applies the military-plan and section 404(k) exclusions to IRA entries and the inherited-IRA exclusion to plan entries, so it needs answers the source does not ask of that kind of account: partial of classm.s2.3.deepseek withholding retirement.sav_military or retirement.sav_404k (completed; IRA entry) project $92.00, candidate unknown (the inherited reading is amb.2025.savers_inherited_plans). The project-refuses are its cited retirement.bad_code; the candidate-refuses are retirement.special on partial records where the project needs the withheld answer (classm.dcprov.1, classm.s179.1, classm.clcw.1): scope. Project stands.

### retirement.l1 — Form 5329 line 1 share: the taxable amount of an early distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}}, {"guard": {"args": [{"args": [{"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 3, Line 1: "Enter the amount of early distributions includible in income (other than qualified disaster recovery distributions) that you received from:"; i5329 p. 5, Line 4: "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%. These distributions are included in boxes 1 and 2a of Form 1099-R and are designated with code S in box 7." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,374 fixtures, 500 generated returns seed 20261026, 1,085 partial records from 40 bases; 2,387 comparisons): 1,329 of 2,387 agree; 859 candidate-unknown (52 completed), 175 candidate-refuses (none completed), 21 value (3 completed), 2 project-unknown (none completed), 1 project-refuses (none completed). Round 3's codes 2-4 on line 1 are gone; line 1 is now code 1 only. (1) It leaves code S entries off line 1 and puts them only in its l1_s, but a code S distribution is an early distribution includible in income, so it is on line 1 and line 3 ("If any amount on line 3 was a distribution from a SIMPLE IRA"); the project's retirement.l1 takes code 1 and S entries and person.x_l1 sums it: classm.f5329.2 and classm.f5329.2.deepseek (completed; traditional IRA, code S, box 1 $25,190) project $25,190.00, candidate $0.00; stage21.blind.e2 (completed; code S, $4,000) project $4,000.00, candidate $0.00; classm.retirement.3 (refused) $11,843.00 against $0.00. (2) It declares retirement.special, retirement.early_screen and retirement.code_screen as refusals of every entry, so it needs screen answers on entries the screens do not concern (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7 (decision D3(a), the cited screens of retirement.screen_refused)): classm.dependent.5.deepseek (completed; code 7) project $0.00, candidate unknown; its candidate-refuses are retirement.special on returns the project refuses on the same cited gate elsewhere (classm.f8606.1, classm.w2.1): scope. (3) The project-refuses is the cited retirement.bad_code (stage21.refuse.bad_code_screen_unasked): scope; the project-unknown are partials withholding box 1 or the rollover, answers of every entry. Project stands.

### retirement.l2 — Form 5329 line 2 share before the per-person limits
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"input": "retirement.exc_amount"}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,374 fixtures, 500 generated returns seed 20261026, 1,085 partial records from 40 bases; 2,387 comparisons): 1,276 of 2,387 agree; 871 candidate-unknown (40 completed), 185 candidate-refuses (none completed), 28 value (7 completed), 26 project-unknown (none completed), 1 project-refuses (none completed). (1) It counts only code 1 entries, so the exception amount of a code S entry is left off line 2 (it puts it only in its l2_s), though line 2 excludes from line 1 the code S distributions it holds: classm.retirement.3 (refused; code S, exception 19) project $4,915.00, candidate $0.00. (2) Its excepted amount is the exception amount itself, not capped by the entry's line 1 amount; the project caps it (retirement.exc_capped, the smaller of the exception amount and the taxable amount), since line 2 is the part of the early distribution the tax "doesn’t apply to" and cannot exceed it: classm.retirement.1 (refused; plan annuity, box 1 $0, exception 22, amount $11,724) project $0.00, candidate $11,724.00; classm.retirement.5 (refused; IRA, box 1 $0, exception 23) $0.00 against $1,758.00. The 7 completed value differences are all this cap (checked by re-running the evaluator read-only with every witness kept, which reproduces the record's counts, and explaining each): the official example stage21.example.teacher_education (traditional IRA, code 1, taxable $500, exception 08, AQEE $800) project $500.00, candidate $800.00, decided by p970 p. 56, Example 1: "Because the teacher’s AQEE ($800) is more than the taxable part of their IRA distribution ($500), they don't have to pay the 10% additional tax on any part of this distribution. However, they must include the $500 taxable earnings in their gross income" (line 2 is $500, not $800); the same return on five partial records withholding box 5, annuity, sav_military, sav_404k or sav_inherited (answers line 2 does not need) project $500.00, candidate $800.00; and generated 278 (code 1 plan annuity, worksheet line 9 $0, exception 19, amount $2,648.29) project $0.00, candidate $2,648.29. (3) It declares the screens and retirement.special on every entry, needing answers the source does not ask (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7 (decision D3(a), the cited screens of retirement.screen_refused)): classm.dependent.5.deepseek (completed, code 7). (4) It has no account rule; on stage21.refuse.wrong_kind the project refuses on the cited retirement.wrong_kind (i5329 p. 5, "Qualified retirement plan distributions (doesn’t apply to IRAs)"): scope; the project-unknown are partials withholding box 1, the rollover, the exception or its amount, answers the entry is asked. The exception amount question (retirement.exc_amount) is an input the candidate reads unchanged; its new 09 wording does not enter this comparison. Project stands.

### retirement.l2_e05 — Line 2 share under exception 05
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"input": "retirement.exc_amount"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,374 fixtures, 500 generated returns seed 20261026, 1,085 partial records from 40 bases; 2,387 comparisons): 1,291 of 2,387 agree; 907 candidate-unknown (40 completed), 185 candidate-refuses (none completed), 4 project-unknown (none completed). (1) The exception test is now guarded on a code 1 or S entry, but the candidate declares retirement.special, retirement.early_screen and retirement.code_screen as refusals of every entry, so it needs answers the source does not ask (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7 (decision D3(a), the cited screens of retirement.screen_refused)): classm.dependent.5.deepseek (completed, code 7) project $0.00, candidate unknown; its candidate-refuses are retirement.special on returns the project refuses on that cited gate elsewhere. (2) Its excepted amount is the exception amount itself, not capped by the entry's line 1 amount; the project caps it (retirement.exc_capped, the smaller of the exception amount and the taxable amount), since line 2 is the part of the early distribution the tax "doesn’t apply to" and cannot exceed it: No value differs on the sample. The project-unknown are partials withholding box 1 or the rollover, answers of every entry. Project stands.

### retirement.l2_e09 — Line 2 share under exception 09
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"input": "retirement.exc_amount"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,374 fixtures, 500 generated returns seed 20261026, 1,085 partial records from 40 bases; 2,387 comparisons): 1,290 of 2,387 agree; 907 candidate-unknown (40 completed), 185 candidate-refuses (none completed), 4 project-unknown (none completed), 1 value (none completed). (1) The exception test is now guarded on a code 1 or S entry, but the candidate declares retirement.special, retirement.early_screen and retirement.code_screen as refusals of every entry, so it needs answers the source does not ask (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7 (decision D3(a), the cited screens of retirement.screen_refused)): classm.dependent.5.deepseek (completed, code 7) project $0.00, candidate unknown; its candidate-refuses are retirement.special on returns the project refuses on that cited gate elsewhere. (2) Its excepted amount is the exception amount itself, not capped by the entry's line 1 amount; the project caps it (retirement.exc_capped, the smaller of the exception amount and the taxable amount), since line 2 is the part of the early distribution the tax "doesn’t apply to" and cannot exceed it: generated 286 (refused; traditional IRA, code S, box 1 $0, exception 09, amount $5,412.88) project $0.00, candidate $5,412.88. The new 09 amount wording (p590b p. 27, First home, requirement 1: "It must be used to pay qualified acquisition costs (defined next) before the close of the 120th day after the day you received it") is the input's text; the candidate reads the same input, and the difference is the cap, not the wording. The project-unknown are partials withholding box 1 or the rollover, answers of every entry. Project stands.

### retirement.l2_e19 — Line 2 share under exception 19
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"input": "retirement.exc_amount"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,374 fixtures, 500 generated returns seed 20261026, 1,085 partial records from 40 bases; 2,387 comparisons): 1,289 of 2,387 agree; 903 candidate-unknown (40 completed), 185 candidate-refuses (none completed), 8 project-unknown (none completed), 2 value (1 completed). (1) The exception test is now guarded on a code 1 or S entry, but the candidate declares retirement.special, retirement.early_screen and retirement.code_screen as refusals of every entry, so it needs answers the source does not ask (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7 (decision D3(a), the cited screens of retirement.screen_refused)): classm.dependent.5.deepseek (completed, code 7) project $0.00, candidate unknown; its candidate-refuses are retirement.special on returns the project refuses on that cited gate elsewhere. (2) Its excepted amount is the exception amount itself, not capped by the entry's line 1 amount; the project caps it (retirement.exc_capped, the smaller of the exception amount and the taxable amount), since line 2 is the part of the early distribution the tax "doesn’t apply to" and cannot exceed it: generated 278 (completed; code 1 plan annuity whose worksheet line 9 is $0 because last year's line 4 times 9 months exceeds box 1, exception 19, amount $2,648.29) project $0.00, candidate $2,648.29; generated 31 (refused) $0.00 against $1,863.84. The project-unknown are partials withholding box 1 or the rollover, answers of every entry. Project stands.

### retirement.l2_e22 — Line 2 share under exception 22
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"input": "retirement.exc_amount"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,374 fixtures, 500 generated returns seed 20261026, 1,085 partial records from 40 bases; 2,387 comparisons): 1,285 of 2,387 agree; 915 candidate-unknown (40 completed), 185 candidate-refuses (none completed), 2 value (none completed). (1) The exception test is now guarded on a code 1 or S entry, but the candidate declares retirement.special, retirement.early_screen and retirement.code_screen as refusals of every entry, so it needs answers the source does not ask (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7 (decision D3(a), the cited screens of retirement.screen_refused)): classm.dependent.5.deepseek (completed, code 7) project $0.00, candidate unknown; its candidate-refuses are retirement.special on returns the project refuses on that cited gate elsewhere. (2) Its excepted amount is the exception amount itself, not capped by the entry's line 1 amount; the project caps it (retirement.exc_capped, the smaller of the exception amount and the taxable amount), since line 2 is the part of the early distribution the tax "doesn’t apply to" and cannot exceed it: classm.retirement.1 and classm.retirement.1.deepseek (refused; plan annuity, box 1 $0, amount $11,724) project $0.00, candidate $11,724.00. The project-unknown are partials withholding box 1 or the rollover, answers of every entry. Project stands.

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

Ruling: model error; p590b p. 28, Emergency personal expense distributions, Distribution limits: "You are limited to taking one emergency personal expense distribution per calendar year"; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." The candidate tests retirement.exception = e23 on every entry, so it needs the exception answer on entries it is not asked of: classm.dependent.5.deepseek (completed, code 7) project false, candidate unknown. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,374 fixtures, 500 generated returns seed 20261026, 1,085 partial records from 40 bases; 2,387 comparisons): 1,513 of 2,387 agree; 872 candidate-unknown (33 completed), 2 project-unknown (none completed); the project-unknown are partial records withholding retirement.code, asked of every entry (stage21.refuse.two23). No value differs. Same reply as round 3. Project stands.

### retirement.l2_e23 — Line 2 share under exception 23
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"input": "retirement.exc_amount"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,374 fixtures, 500 generated returns seed 20261026, 1,085 partial records from 40 bases; 2,387 comparisons): 1,289 of 2,387 agree; 907 candidate-unknown (40 completed), 185 candidate-refuses (none completed), 4 project-unknown (none completed), 2 value (none completed). (1) The exception test is now guarded on a code 1 or S entry, but the candidate declares retirement.special, retirement.early_screen and retirement.code_screen as refusals of every entry, so it needs answers the source does not ask (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7 (decision D3(a), the cited screens of retirement.screen_refused)): classm.dependent.5.deepseek (completed, code 7) project $0.00, candidate unknown; its candidate-refuses are retirement.special on returns the project refuses on that cited gate elsewhere. (2) Its excepted amount is the exception amount itself, not capped by the entry's line 1 amount; the project caps it (retirement.exc_capped, the smaller of the exception amount and the taxable amount), since line 2 is the part of the early distribution the tax "doesn’t apply to" and cannot exceed it: classm.retirement.5 and classm.retirement.5.deepseek (refused; IRA, box 1 $0, amount $1,758) project $0.00, candidate $1,758.00. The project-unknown are partials withholding box 1 or the rollover, answers of every entry. Project stands.

### retirement.l1_s — Line 1 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}}, {"guard": {"args": [{"args": [{"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 4: "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%. These distributions are included in boxes 1 and 2a of Form 1099-R and are designated with code S in box 7." The code S share is the project's, but the candidate declares retirement.special, retirement.early_screen and retirement.code_screen as refusals of every entry, so it needs screen answers on entries they do not concern (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7 (decision D3(a), the cited screens of retirement.screen_refused)): classm.dependent.5.deepseek (code 7, completed). executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,374 fixtures, 500 generated returns seed 20261026, 1,085 partial records from 40 bases; 2,387 comparisons): 1,321 of 2,387 agree; 880 candidate-unknown (40 completed), 185 candidate-refuses (none completed), 1 project-refuses (none completed). The candidate-refuses are retirement.special on returns the project refuses on that cited gate elsewhere; 1 project-refuses on the cited retirement.bad_code (stage21.refuse.bad_code_screen_unasked): scope. No value differs. Project stands.

### retirement.l2_s — Line 2 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"input": "retirement.exc_amount"}}, {"guard": {"args": [{"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 4: "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%. These distributions are included in boxes 1 and 2a of Form 1099-R and are designated with code S in box 7."; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,374 fixtures, 500 generated returns seed 20261026, 1,085 partial records from 40 bases; 2,387 comparisons): 1,320 of 2,387 agree; 879 candidate-unknown (40 completed), 185 candidate-refuses (none completed), 2 project-unknown (none completed), 1 value (none completed). (1) It needs the screen answers on every entry, as on retirement.l1_s (classm.dependent.5.deepseek, code 7, completed). (2) Its excepted amount is the exception amount itself, not capped by the entry's line 1 amount; the project caps it (retirement.exc_capped, the smaller of the exception amount and the taxable amount), since line 2 is the part of the early distribution the tax "doesn’t apply to" and cannot exceed it: generated 286 (refused; traditional IRA, code S, box 1 $0, exception 09, amount $5,412.88) project $0.00, candidate $5,412.88. The project-unknown are partials withholding box 1 or the rollover. Project stands.

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": 71, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_160"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"input": "retirement.age"}, {"const": 55, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_360"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"input": "retirement.age"}, {"const": 60, "type": "Count"}], "test": "le"}, {"args": [{"const": 55, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_310"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"input": "retirement.age"}, {"const": 65, "type": "Count"}], "test": "le"}, {"args": [{"const": 60, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_260"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"input": "retirement.age"}, {"const": 70, "type": "Count"}], "test": "le"}, {"args": [{"const": 65, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_210"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": 141, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_210"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 110, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_410"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 120, "type": "Count"}], "test": "le"}, {"args": [{"const": 110, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_360"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 130, "type": "Count"}], "test": "le"}, {"args": [{"const": 120, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_310"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 140, "type": "Count"}], "test": "le"}, {"args": [{"const": 130, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_260"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"input": "retirement.last_line4"}}], "op": "choose"}
```

Ruling: representation; i1040gi p. 29, Simplified Method Worksheet, line 4: "Divide line 2 by the number on line 3" and line 2 Note: "If you completed this worksheet last year, skip line 3 and enter the amount from line 4 of last year’s worksheet on line 4 below"; Tables 1 and 2 ("after November 18, 1996" column: 360, 310, 260, 210, 160; Table 2: 410, 360, 310, 260, 210). The candidate now takes last year's line 4 when the worksheet was used last year (round 3's error is gone); ages are whole numbers, so its bands equal the project's; the pre-November-19-1996 column is screened by retirement.special and retirement.annuity. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,374 fixtures, 500 generated returns seed 20261026, 1,085 partial records from 40 bases; 2,387 comparisons): 2,387 of 2,387 agree. Project stands.

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
| retirement.taxable | retirement.h_roth_unhandled, retirement.special | retirement.h_roth_unhandled |
| retirement.amount_a | retirement.special | - |
| retirement.sav_amount | retirement.special | - |
| retirement.l1 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_unhandled, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_unhandled |
| retirement.l2 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_unhandled, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_unhandled |
| retirement.l2_e05 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_unhandled, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_unhandled |
| retirement.l2_e09 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_unhandled, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_unhandled |
| retirement.l2_e19 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_unhandled, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_unhandled |
| retirement.l2_e22 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_unhandled, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_unhandled |
| retirement.l2_e23 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_unhandled, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_unhandled |
| retirement.l1_s | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_unhandled, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_unhandled |
| retirement.l2_s | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_unhandled, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_unhandled |

## Raw second transcription

```yaml
lines:
  - id: retirement.smw1
    printed: "(SMW 1)"
    label: "Enter the total pension or annuity payments from Form 1099-R, box 1. Also, enter this amount on Form 1040 or 1040-SR, line 5a."
    type: NonNegDollars
    expr: {op: copy, from: retirement.box1}
  - id: retirement.smw2
    printed: "(SMW 2)"
    label: "Enter your cost in the plan at the annuity starting date."
    type: NonNegDollars
    expr: {op: copy, from: retirement.cost}
  - id: retirement.smw4
    printed: "(SMW 4)"
    label: "Divide line 2 by the number on line 3."
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
              - {op: test, le: [retirement.combined_age, {const: 110, type: Count}]}
          then: retirement.h_l4_t2_410
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: true}]}
              - {op: test, gt: [retirement.combined_age, {const: 110, type: Count}]}
              - {op: test, le: [retirement.combined_age, {const: 120, type: Count}]}
          then: retirement.h_l4_t2_360
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: true}]}
              - {op: test, gt: [retirement.combined_age, {const: 120, type: Count}]}
              - {op: test, le: [retirement.combined_age, {const: 130, type: Count}]}
          then: retirement.h_l4_t2_310
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: true}]}
              - {op: test, gt: [retirement.combined_age, {const: 130, type: Count}]}
              - {op: test, le: [retirement.combined_age, {const: 140, type: Count}]}
          then: retirement.h_l4_t2_260
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: true}]}
              - {op: test, ge: [retirement.combined_age, {const: 141, type: Count}]}
          then: retirement.h_l4_t2_210
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: false}]}
              - {op: test, le: [retirement.age, {const: 55, type: Count}]}
          then: retirement.h_l4_t1_360
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: false}]}
              - {op: test, gt: [retirement.age, {const: 55, type: Count}]}
              - {op: test, le: [retirement.age, {const: 60, type: Count}]}
          then: retirement.h_l4_t1_310
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: false}]}
              - {op: test, gt: [retirement.age, {const: 60, type: Count}]}
              - {op: test, le: [retirement.age, {const: 65, type: Count}]}
          then: retirement.h_l4_t1_260
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: false}]}
              - {op: test, gt: [retirement.age, {const: 65, type: Count}]}
              - {op: test, le: [retirement.age, {const: 70, type: Count}]}
          then: retirement.h_l4_t1_210
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.used_last_year, {const: false}]}
              - {op: test, eq: [retirement.joint_life, {const: false}]}
              - {op: test, ge: [retirement.age, {const: 71, type: Count}]}
          then: retirement.h_l4_t1_160
  - id: retirement.smw5
    printed: "(SMW 5)"
    label: "Multiply line 4 by the number of months for which this year's payments were made. If your annuity starting date was before 1987, skip lines 6 and 7 and enter this amount on line 8. Otherwise, go to line 6."
    type: NonNegDollars
    expr: {op: multiply_count, amount: retirement.smw4, count: retirement.months}
  - id: retirement.smw6
    printed: "(SMW 6)"
    label: "Enter the amount, if any, recovered tax free in years after 1986. If you completed this worksheet last year, enter the amount from line 10 of last year's worksheet."
    type: NonNegDollars
    expr: {op: copy, from: retirement.recovered}
  - id: retirement.smw7
    printed: "(SMW 7)"
    label: "Subtract line 6 from line 2."
    type: Dollars
    expr: {op: subtract, from: retirement.smw2, take: retirement.smw6}
  - id: retirement.smw8
    printed: "(SMW 8)"
    label: "Enter the smaller of line 5 or line 7."
    type: Dollars
    expr: {op: smaller_of, of: [retirement.smw5, retirement.smw7]}
  - id: retirement.smw9
    printed: "(SMW 9)"
    label: "Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero. Also, enter this amount on Form 1040 or 1040-SR, line 5b. If your Form 1099-R shows a larger amount, use the amount on this line instead of the amount from Form 1099-R. If you are a retired public safety officer, see Insurance Premiums for Retired Public Safety Officers before entering an amount on line 5b."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.smw1, take: retirement.smw8}
  - id: retirement.smw10
    printed: "(SMW 10)"
    label: "Was your annuity starting date before 1987? Yes. STOP Do not complete the rest of this worksheet. No. Add lines 6 and 8. This is the amount you have recovered tax free through 2025. You will need this number if you need to fill out this worksheet next year."
    type: Dollars
    expr: {op: sum, of: [retirement.smw6, retirement.smw8]}
    note: "The scoped Simplified Method input requires an annuity starting date after November 18, 1996, so the before-1987 stop does not apply; line 10 is computed as line 6 plus line 8."
  - id: retirement.smw11
    printed: "(SMW 11)"
    label: "Balance of cost to be recovered. Subtract line 10 from line 2. If zero, you won't have to complete this worksheet next year. The payments you receive next year will generally be fully taxable."
    type: Dollars
    expr: {op: subtract, from: retirement.smw2, take: retirement.smw10}
  - id: retirement.one
    printed: "(helper)"
    label: "One, as a count."
    type: Count
    expr: {op: param, ref: person.one}
  - id: retirement.is_ira
    printed: "(helper)"
    label: "Whether this distribution is from an IRA (traditional or Roth)."
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.account, {const: "traditional_ira"}]}
        - {op: test, eq: [retirement.account, {const: "roth_ira"}]}
  - id: retirement.has_rollover
    printed: "(helper)"
    label: "Whether this distribution has a rollover, including a direct rollover."
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [retirement.rollover, {const: 0}]}
        - {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
  - id: retirement.taxable
    printed: "(helper)"
    label: "The taxable amount of this distribution."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "qualified_roth_Q"}]}
          then: retirement.h_zero
        - guard:
            op: test
            all:
              - {op: test, ne: [retirement.code, {const: "qualified_roth_Q"}]}
              - {op: test, eq: [retirement.has_rollover, {const: true}]}
          then: retirement.h_roll_taxable
        - guard:
            op: test
            all:
              - {op: test, ne: [retirement.code, {const: "qualified_roth_Q"}]}
              - {op: test, eq: [retirement.has_rollover, {const: false}]}
              - {op: test, eq: [retirement.annuity, {const: true}]}
          then: retirement.smw9
        - guard:
            op: test
            all:
              - {op: test, ne: [retirement.code, {const: "qualified_roth_Q"}]}
              - {op: test, eq: [retirement.has_rollover, {const: false}]}
              - {op: test, eq: [retirement.annuity, {const: false}]}
          then: retirement.h_after_box5
    refuses: [retirement.special, retirement.h_roth_unhandled]
  - id: retirement.amount_a
    printed: "(helper)"
    label: "The amount to report on Form 1040 line 4a or 5a for this distribution."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.has_rollover, {const: true}]}
          then: retirement.box1
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.has_rollover, {const: false}]}
              - {op: test, eq: [retirement.code, {const: "qualified_roth_Q"}]}
          then: retirement.box1
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.has_rollover, {const: false}]}
              - {op: test, ne: [retirement.code, {const: "qualified_roth_Q"}]}
              - {op: test, eq: [retirement.h_roth_unhandled, {const: true}]}
          then: retirement.box1
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.has_rollover, {const: false}]}
              - {op: test, ne: [retirement.code, {const: "qualified_roth_Q"}]}
              - {op: test, eq: [retirement.h_roth_unhandled, {const: false}]}
              - {op: test, eq: [retirement.annuity, {const: true}]}
          then: retirement.box1
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.has_rollover, {const: false}]}
              - {op: test, ne: [retirement.code, {const: "qualified_roth_Q"}]}
              - {op: test, eq: [retirement.h_roth_unhandled, {const: false}]}
              - {op: test, eq: [retirement.annuity, {const: false}]}
          then: retirement.h_zero
    refuses: [retirement.special]
  - id: retirement.sav_amount
    printed: "(helper)"
    label: "The amount of this distribution to include on Form 8880, line 4."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.sav_military, {const: true}]}
          then: retirement.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.sav_military, {const: false}]}
              - {op: test, eq: [retirement.sav_404k, {const: true}]}
          then: retirement.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.sav_military, {const: false}]}
              - {op: test, eq: [retirement.sav_404k, {const: false}]}
              - {op: test, eq: [retirement.sav_inherited, {const: true}]}
          then: retirement.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.sav_military, {const: false}]}
              - {op: test, eq: [retirement.sav_404k, {const: false}]}
              - {op: test, eq: [retirement.sav_inherited, {const: false}]}
          then: retirement.h_box1_minus_rollover_eff
    refuses: [retirement.special]
  - id: retirement.l1
    printed: "(helper)"
    label: "Form 5329 line 1 amount for this distribution, regular 10% additional tax."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_code_early_1, {const: true}]}
          then: retirement.taxable
        - guard: {op: test, eq: [retirement.h_code_early_1, {const: false}]}
          then: retirement.h_zero
    refuses: [retirement.special, retirement.early_screen, retirement.code_screen, retirement.h_code_other, retirement.h_roth_unhandled]
  - id: retirement.l2
    printed: "(helper)"
    label: "Form 5329 line 2 exception amount for this distribution, regular 10% additional tax."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_regular_exception, {const: true}]}
          then: retirement.exc_amount
        - guard: {op: test, eq: [retirement.h_regular_exception, {const: false}]}
          then: retirement.h_zero
    refuses: [retirement.special, retirement.early_screen, retirement.code_screen, retirement.h_code_other, retirement.h_roth_unhandled]
  - id: retirement.l2_e05
    printed: "(helper)"
    label: "Form 5329 line 2 exception 05 amount for this distribution."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_is_e05, {const: true}]}
          then: retirement.exc_amount
        - guard: {op: test, eq: [retirement.h_is_e05, {const: false}]}
          then: retirement.h_zero
    refuses: [retirement.special, retirement.early_screen, retirement.code_screen, retirement.h_code_other, retirement.h_roth_unhandled]
  - id: retirement.l2_e09
    printed: "(helper)"
    label: "Form 5329 line 2 exception 09 amount for this distribution."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_is_e09, {const: true}]}
          then: retirement.exc_amount
        - guard: {op: test, eq: [retirement.h_is_e09, {const: false}]}
          then: retirement.h_zero
    refuses: [retirement.special, retirement.early_screen, retirement.code_screen, retirement.h_code_other, retirement.h_roth_unhandled]
  - id: retirement.l2_e19
    printed: "(helper)"
    label: "Form 5329 line 2 exception 19 amount for this distribution."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_is_e19, {const: true}]}
          then: retirement.exc_amount
        - guard: {op: test, eq: [retirement.h_is_e19, {const: false}]}
          then: retirement.h_zero
    refuses: [retirement.special, retirement.early_screen, retirement.code_screen, retirement.h_code_other, retirement.h_roth_unhandled]
  - id: retirement.l2_e22
    printed: "(helper)"
    label: "Form 5329 line 2 exception 22 amount for this distribution."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_is_e22, {const: true}]}
          then: retirement.exc_amount
        - guard: {op: test, eq: [retirement.h_is_e22, {const: false}]}
          then: retirement.h_zero
    refuses: [retirement.special, retirement.early_screen, retirement.code_screen, retirement.h_code_other, retirement.h_roth_unhandled]
  - id: retirement.is_e23
    printed: "(helper)"
    label: "Whether exception 23 applies to this distribution."
    type: Bool
    expr: {op: test, eq: [retirement.exception, {const: "e23"}]}
  - id: retirement.l2_e23
    printed: "(helper)"
    label: "Form 5329 line 2 exception 23 amount for this distribution."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_is_e23, {const: true}]}
          then: retirement.exc_amount
        - guard: {op: test, eq: [retirement.h_is_e23, {const: false}]}
          then: retirement.h_zero
    refuses: [retirement.special, retirement.early_screen, retirement.code_screen, retirement.h_code_other, retirement.h_roth_unhandled]
  - id: retirement.l1_s
    printed: "(helper)"
    label: "Form 5329 line 1 amount for this distribution, SIMPLE IRA 25% additional tax."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_code_simple, {const: true}]}
          then: retirement.taxable
        - guard: {op: test, eq: [retirement.h_code_simple, {const: false}]}
          then: retirement.h_zero
    refuses: [retirement.special, retirement.early_screen, retirement.code_screen, retirement.h_code_other, retirement.h_roth_unhandled]
  - id: retirement.l2_s
    printed: "(helper)"
    label: "Form 5329 line 2 exception amount for this distribution, SIMPLE IRA 25% additional tax."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_simple_exception, {const: true}]}
          then: retirement.exc_amount
        - guard: {op: test, eq: [retirement.h_simple_exception, {const: false}]}
          then: retirement.h_zero
    refuses: [retirement.special, retirement.early_screen, retirement.code_screen, retirement.h_code_other, retirement.h_roth_unhandled]
  - id: retirement.h_zero
    printed: "(helper)"
    label: "Zero."
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: retirement.h_l4_t1_360
    printed: "(helper)"
    label: "Line 4 candidate using Table 1 divisor 360."
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_360}}
  - id: retirement.h_l4_t1_310
    printed: "(helper)"
    label: "Line 4 candidate using Table 1 divisor 310."
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_310}}
  - id: retirement.h_l4_t1_260
    printed: "(helper)"
    label: "Line 4 candidate using Table 1 divisor 260."
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_260}}
  - id: retirement.h_l4_t1_210
    printed: "(helper)"
    label: "Line 4 candidate using Table 1 divisor 210."
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_210}}
  - id: retirement.h_l4_t1_160
    printed: "(helper)"
    label: "Line 4 candidate using Table 1 divisor 160."
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_160}}
  - id: retirement.h_l4_t2_410
    printed: "(helper)"
    label: "Line 4 candidate using Table 2 divisor 410."
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_410}}
  - id: retirement.h_l4_t2_360
    printed: "(helper)"
    label: "Line 4 candidate using Table 2 divisor 360."
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_360}}
  - id: retirement.h_l4_t2_310
    printed: "(helper)"
    label: "Line 4 candidate using Table 2 divisor 310."
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_310}}
  - id: retirement.h_l4_t2_260
    printed: "(helper)"
    label: "Line 4 candidate using Table 2 divisor 260."
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_260}}
  - id: retirement.h_l4_t2_210
    printed: "(helper)"
    label: "Line 4 candidate using Table 2 divisor 210."
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_210}}
  - id: retirement.h_rollover_effective
    printed: "(helper)"
    label: "Effective rollover amount, treating a code G direct rollover as rolling over the whole distribution."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
          then: retirement.box1
        - guard: {op: test, ne: [retirement.code, {const: "direct_rollover_G"}]}
          then: retirement.rollover
  - id: retirement.h_box1_minus_rollover_eff
    printed: "(helper)"
    label: "Box 1 less the effective rollover amount."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.h_rollover_effective}
  - id: retirement.h_after_box5
    printed: "(helper)"
    label: "Box 1 less box 5."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.box5}
  - id: retirement.h_roll_taxable
    printed: "(helper)"
    label: "Box 1 less box 5 and the effective rollover amount."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_after_box5, take: retirement.h_rollover_effective}
  - id: retirement.h_roth_unhandled
    printed: "(helper)"
    label: "Whether this is a Roth IRA distribution, other than a qualified distribution or direct rollover, requiring Form 8606 outside this tool."
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.account, {const: "roth_ira"}]}
        - op: test
          not:
            op: test
            any:
              - {op: test, eq: [retirement.code, {const: "qualified_roth_Q"}]}
              - {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
  - id: retirement.h_code_other
    printed: "(helper)"
    label: "Whether the distribution code is other."
    type: Bool
    expr: {op: test, eq: [retirement.code, {const: "other"}]}
  - id: retirement.h_code_early_1
    printed: "(helper)"
    label: "Whether the distribution code is early_1."
    type: Bool
    expr: {op: test, eq: [retirement.code, {const: "early_1"}]}
  - id: retirement.h_code_simple
    printed: "(helper)"
    label: "Whether the distribution code is simple_S."
    type: Bool
    expr: {op: test, eq: [retirement.code, {const: "simple_S"}]}
  - id: retirement.h_early_subject
    printed: "(helper)"
    label: "Whether the distribution is an early distribution subject to an additional tax."
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.code, {const: "early_1"}]}
        - {op: test, eq: [retirement.code, {const: "simple_S"}]}
  - id: retirement.h_regular_exception
    printed: "(helper)"
    label: "Whether an exception applies to an early_1 distribution."
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.code, {const: "early_1"}]}
        - {op: test, ne: [retirement.exception, {const: "none"}]}
  - id: retirement.h_simple_exception
    printed: "(helper)"
    label: "Whether an exception applies to a simple_S distribution."
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.code, {const: "simple_S"}]}
        - {op: test, ne: [retirement.exception, {const: "none"}]}
  - id: retirement.h_is_e05
    printed: "(helper)"
    label: "Whether exception 05 applies to an early distribution."
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.exception, {const: "e05"}]}
        - {op: test, eq: [retirement.h_early_subject, {const: true}]}
  - id: retirement.h_is_e09
    printed: "(helper)"
    label: "Whether exception 09 applies to an early distribution."
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.exception, {const: "e09"}]}
        - {op: test, eq: [retirement.h_early_subject, {const: true}]}
  - id: retirement.h_is_e19
    printed: "(helper)"
    label: "Whether exception 19 applies to an early distribution."
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.exception, {const: "e19"}]}
        - {op: test, eq: [retirement.h_early_subject, {const: true}]}
  - id: retirement.h_is_e22
    printed: "(helper)"
    label: "Whether exception 22 applies to an early distribution."
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.exception, {const: "e22"}]}
        - {op: test, eq: [retirement.h_early_subject, {const: true}]}
  - id: retirement.h_is_e23
    printed: "(helper)"
    label: "Whether exception 23 applies to an early distribution."
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.exception, {const: "e23"}]}
        - {op: test, eq: [retirement.h_early_subject, {const: true}]}
```
