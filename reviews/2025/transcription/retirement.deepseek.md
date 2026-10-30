# Transcription agreement — retirement

Second transcription of `Form 1099-R distributions (IRAs, pensions and annuities)` by an isolated model (spec 6.5), compared line by line with `forms/2025/retirement.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | e0a80a75e88aad56ca4a2ad6f776034b5c76ac7e78d379c87d90198099046413 |
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
| subject sha256 | 93e00fade97386483f3b31fe4ce287c1425476dbf8edcde3a93a3c251a78cd1f |
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

Ruling: representation; i1040gi p. 26, Lines 4a and 4b, IRA Distributions. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,894 of 1,894 agree. Project stands.

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

Ruling: scope; i1040gi p. 30, Rollovers: "Use lines 5a and 5b to report a rollover, including a direct rollover, from one qualified employer’s plan to another or to an IRA. ... Also check box 1 on line 5c."; i1040gi p. 27, Exception 1: "Enter the total distribution on line 4a if you rolled over part or all of the distribution ... Also check box 1 on line 4c.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,574 of 1,894 agree; 228 project-refuses (none completed), 92 project-unknown (none completed). No value differs and nothing differs on a completed return: the project-refuses are its cited retirement.special and retirement.bad_code read through retirement.rolled, the project-unknown partial records withholding answers asked of every entry. Project stands.

### retirement.taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}
```

Second transcription's note: Nonqualified Roth IRA distributions require Form 8606 and are refused. The zero branch for a nonqualified Roth IRA is unreachable when the refusal gate is true.

Ruling: model error and scope; i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost ... of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a."; i1040gi p. 29, line 11: "If zero, you won’t have to complete this worksheet next year." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,619 of 1,894 agree; 199 project-refuses (none completed), 48 project-unknown (none completed), 16 candidate-unknown (4 completed), 12 value (8 completed). It takes worksheet line 9 on every annuity with no branch for a recovered cost, so a negative line 7 makes line 9 exceed box 1: the 8 completed values are classm.tcw.15 (project $39,110.00, candidate $49,089.00) and 6 of its partial records, and generated 395 r2 ($0.00 against $22,738.41); the 4 completed candidate-unknown are partials of classm.tcw.15 withholding worksheet answers (used_last_year, joint_life, combined_age, months) the project does not need once the cost is recovered. Project-refuses are its cited gates and the unknowns partial records: scope. Project stands.

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

Ruling: model error and scope; i1040gi p. 27, Lines 4a and 4b: "If the distribution from your IRA is fully taxable, enter the total distribution on line 4b; don’t make an entry on line 4a."; i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost ... of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 612 of 1,894 agree; 709 value (157 completed), 275 project-refuses (none completed), 270 project-unknown (none completed), 28 candidate-unknown (none completed). The reply copies box 1 to line 4a/5a on every entry; all 157 completed value differences are project $0.00 against box 1 on fully taxable entries (the 37 fixture and 82 fixture-based partial witnesses checked against their box 1; the 22 generated and 16 generated-based partials follow from the copy expression), e.g. classm.s2.3 (IRA, code 1) $0.00 against $92.00, classm.tcw.15 $0.00 against $39,110.00, stage21.example.teacher_education $0.00 against $500.00. Project-refuses are its cited gates: scope. Project stands.

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

Second transcription's note: The Form 8880 line 4 exclusion for conversions or rollovers to Roth accounts is not separately identified by the supplied inputs; only the 60-day non-Roth rollover amount and the listed military, 404(k) and inherited-IRA exclusions are applied.

Ruling: model error and scope; f8880 p. 2, Line 4: "Don’t include any of the following. • Distributions not taxable as the result of a rollover or a trustee-to-trustee transfer ... • Distributions from a military retirement plan (other than the federal TSP). • Distributions from an inherited IRA by a nonspousal beneficiary". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,532 of 1,894 agree; 199 project-refuses (none completed), 109 project-unknown (none completed), 54 candidate-unknown (18 completed). No value differs. The 18 completed candidate-unknown are partial records withholding sav_military (8) or sav_404k (8) on IRA entries, or sav_inherited (2) on plan entries (amb.2025.savers_inherited_plans for the inherited reading). Project-refuses are its cited retirement.bad_code: scope. Project stands.

### retirement.l1 — Form 5329 line 1 share: the taxable amount of an early distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 3, Line 1: "Enter the amount of early distributions includible in income (other than qualified disaster recovery distributions) that you received from:". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,184 of 1,894 agree; 643 candidate-unknown (61 completed), 66 candidate-refuses (none completed), 1 project-refuses (none completed). No value differs; the amount is the project's. The reply declares retirement.special, early_screen and code_screen as refusals of every entry, so its completed candidate-unknown need early_screen on other codes (54; classm.dependent.5.deepseek, code 7) or code_screen on code 1 or S entries (7; partial of classm.s2.3.deepseek) (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused). The candidate-refuses are on refused returns only and the project-refuses is the cited retirement.bad_code: scope. Project stands.

### retirement.l2 — Form 5329 line 2 share before the per-person limits
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,130 of 1,894 agree; 696 candidate-unknown (62 completed), 67 candidate-refuses (none completed), 1 project-refuses (none completed). No value differs; the amount is the project's. The reply declares retirement.special, early_screen and code_screen as refusals of every entry, so its completed candidate-unknown need early_screen on other codes (54; classm.dependent.5.deepseek, code 7) or code_screen on code 1 or S entries (7; partial of classm.s2.3.deepseek), and 1 the exception answer (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused). The candidate-refuses are on refused returns only and the project-refuses is the cited retirement.bad_code: scope. Project stands.

### retirement.l2_e05 — Line 2 share under exception 05
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,125 of 1,894 agree; 702 candidate-unknown (62 completed), 67 candidate-refuses (none completed). No value differs; the amount is the project's. The reply declares retirement.special, early_screen and code_screen as refusals of every entry, so its completed candidate-unknown need early_screen on other codes (54; classm.dependent.5.deepseek, code 7) or code_screen on code 1 or S entries (7; partial of classm.s2.3.deepseek), and 1 the exception answer (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused). The candidate-refuses are on refused returns only and the project-refuses is the cited retirement.bad_code: scope. Project stands.

### retirement.l2_e09 — Line 2 share under exception 09
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,123 of 1,894 agree; 704 candidate-unknown (62 completed), 67 candidate-refuses (none completed). No value differs; the amount is the project's. The reply declares retirement.special, early_screen and code_screen as refusals of every entry, so its completed candidate-unknown need early_screen on other codes (54; classm.dependent.5.deepseek, code 7) or code_screen on code 1 or S entries (7; partial of classm.s2.3.deepseek), and 1 the exception answer (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused). The candidate-refuses are on refused returns only and the project-refuses is the cited retirement.bad_code: scope. Project stands.

### retirement.l2_e19 — Line 2 share under exception 19
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,125 of 1,894 agree; 702 candidate-unknown (62 completed), 67 candidate-refuses (none completed). No value differs; the amount is the project's. The reply declares retirement.special, early_screen and code_screen as refusals of every entry, so its completed candidate-unknown need early_screen on other codes (54; classm.dependent.5.deepseek, code 7) or code_screen on code 1 or S entries (7; partial of classm.s2.3.deepseek), and 1 the exception answer (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused). The candidate-refuses are on refused returns only and the project-refuses is the cited retirement.bad_code: scope. Project stands.

### retirement.l2_e22 — Line 2 share under exception 22
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,123 of 1,894 agree; 704 candidate-unknown (62 completed), 67 candidate-refuses (none completed). No value differs; the amount is the project's. The reply declares retirement.special, early_screen and code_screen as refusals of every entry, so its completed candidate-unknown need early_screen on other codes (54; classm.dependent.5.deepseek, code 7) or code_screen on code 1 or S entries (7; partial of classm.s2.3.deepseek), and 1 the exception answer (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused). The candidate-refuses are on refused returns only and the project-refuses is the cited retirement.bad_code: scope. Project stands.

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

Ruling: model error; p590b p. 28, Emergency personal expense distributions, Distribution limits: "You are limited to taking one emergency personal expense distribution per calendar year"; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,282 of 1,894 agree; 612 candidate-unknown (54 completed). It tests retirement.exception = e23 on every entry, so the 54 completed candidate-unknown need the exception answer on entries it is not asked of (classm.dependent.5.deepseek, code 7, project false). No value differs. Project stands.

### retirement.l2_e23 — Line 2 share under exception 23
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99."; p590b p. 28, Emergency personal expense distributions, Distribution limits: "You are limited to taking one emergency personal expense distribution per calendar year". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,123 of 1,894 agree; 704 candidate-unknown (62 completed), 67 candidate-refuses (none completed). No value differs; the amount is the project's. The reply declares retirement.special, early_screen and code_screen as refusals of every entry, so its completed candidate-unknown need early_screen on other codes (54; classm.dependent.5.deepseek, code 7) or code_screen on code 1 or S entries (7; partial of classm.s2.3.deepseek), and 1 the exception answer (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused). The candidate-refuses are on refused returns only and the project-refuses is the cited retirement.bad_code: scope. Project stands.

### retirement.l1_s — Line 1 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 4: "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%. These distributions are included in boxes 1 and 2a of Form 1099-R and are designated with code S in box 7.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,174 of 1,894 agree; 652 candidate-unknown (61 completed), 67 candidate-refuses (none completed), 1 project-refuses (none completed). No value differs; the amount is the project's. The reply declares retirement.special, early_screen and code_screen as refusals of every entry, so its completed candidate-unknown need early_screen on other codes (54; classm.dependent.5.deepseek, code 7) or code_screen on code 1 or S entries (7; partial of classm.s2.3.deepseek) (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused). The candidate-refuses are on refused returns only and the project-refuses is the cited retirement.bad_code: scope. Project stands.

### retirement.l2_s — Line 2 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"input": "retirement.rollover"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": 0}, {"input": "retirement.rollover"}], "test": "lt"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 4: "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%. These distributions are included in boxes 1 and 2a of Form 1099-R and are designated with code S in box 7.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,172 of 1,894 agree; 655 candidate-unknown (61 completed), 67 candidate-refuses (none completed). No value differs; the amount is the project's. The reply declares retirement.special, early_screen and code_screen as refusals of every entry, so its completed candidate-unknown need early_screen on other codes (54; classm.dependent.5.deepseek, code 7) or code_screen on code 1 or S entries (7; partial of classm.s2.3.deepseek) (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused). The candidate-refuses are on refused returns only and the project-refuses is the cited retirement.bad_code: scope. Project stands.

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
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "retirement.age"}, {"const": 60, "type": "Count"}], "test": "le"}, {"args": [{"const": 55, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_310"}}}, {"guard": {"args": [{"args": [{"input": "retirement.age"}, {"const": 65, "type": "Count"}], "test": "le"}, {"args": [{"const": 60, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_260"}}}, {"guard": {"args": [{"args": [{"input": "retirement.age"}, {"const": 70, "type": "Count"}], "test": "le"}, {"args": [{"const": 65, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_210"}}}, {"guard": {"args": [{"const": 71, "type": "Count"}, {"input": "retirement.age"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_160"}}}, {"guard": {"args": [{"input": "retirement.age"}, {"const": 55, "type": "Count"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_360"}}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "retirement.combined_age"}, {"const": 120, "type": "Count"}], "test": "le"}, {"args": [{"const": 110, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_360"}}}, {"guard": {"args": [{"args": [{"input": "retirement.combined_age"}, {"const": 130, "type": "Count"}], "test": "le"}, {"args": [{"const": 120, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_310"}}}, {"guard": {"args": [{"args": [{"input": "retirement.combined_age"}, {"const": 140, "type": "Count"}], "test": "le"}, {"args": [{"const": 130, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_260"}}}, {"guard": {"args": [{"const": 141, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_210"}}}, {"guard": {"args": [{"input": "retirement.combined_age"}, {"const": 110, "type": "Count"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_410"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"input": "retirement.last_line4"}}], "op": "choose"}
```

Ruling: model error; i1040gi p. 29, Simplified Method Worksheet, line 4 and the note under line 2; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity."; i1040gi p. 28, Fully Taxable Pensions and Annuities: "(a) you didn’t contribute to the cost ... or (b) you got your entire cost back tax free before 2025"; i1040gi p. 29, line 11: "If zero, you won’t have to complete this worksheet next year." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,496 of 1,894 agree; 313 candidate-unknown (87 completed), 85 candidate-shows-skipped (1 completed). All 398 differences are on entries where the project hides the line (retirement.smw_shown false). The reply gives the worksheet lines no hiding condition, so it shows line 4 on entries the source never takes through the worksheet: the 85 candidate-shows-skipped are cost-recovered annuities (generated 395 r2, completed, $1,550.08 from last year's line 4; stage10.smw.cost_recovered[_box5], stage10.smw.recovered_exceeds_cost, stage21.t067.smw_hidden_cost_recovered and partials, $119.23; generated 184, 214 and 229, refused) and the IRA entry of classm.dcprov.1 ($624.31, refused); the 313 candidate-unknown (87 completed) need worksheet answers on IRA and non-annuity plan entries. Its value is the project's wherever the project shows the line. The worksheet lines now carry shown_when retirement.smw_shown (is_ira false, tested first, and annuity_with_cost true; BUG-0207, BUG-0208). Checked by evaluating: classm.s2.3.deepseek without the worksheet answers and stage21.t067.smw_hidden_ira (IRA, annuity unasked; interview complete) show no (SMW n) line; stage10.smw.cost_recovered, stage10.smw.recovered_exceeds_cost, stage21.t067.smw_hidden_cost_recovered, classm.tcw.15 and generated 395 (cost recovered or $0) show none, with 5a $0 and 5b box 1; a code 7 plan pension with annuity false shows none (5b $20,000); stage10.smw.first_year and a variant with $500 of cost left show all ten lines, (SMW 9) equal to 5b. A sweep of all 1,376 fixtures and 500 generated returns found smw_shown equal to (plan, annuity true, cost above recovered) on every entry where those are answered, false on every IRA entry (answered or not); the only unknown is a plan entry on a return refused on retirement.special before annuity is asked (stage16.cleanup.refuse.retirement.special_first). The project's hiding condition is right; no finding. Project stands.

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
| retirement.taxable | retirement.h_roth_requires_8606, retirement.special | retirement.h_roth_requires_8606 |
| retirement.l1 | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_roth_requires_8606, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_roth_requires_8606 |
| retirement.l2 | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_roth_requires_8606, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_roth_requires_8606 |
| retirement.l2_e05 | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_roth_requires_8606, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_roth_requires_8606 |
| retirement.l2_e09 | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_roth_requires_8606, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_roth_requires_8606 |
| retirement.l2_e19 | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_roth_requires_8606, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_roth_requires_8606 |
| retirement.l2_e22 | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_roth_requires_8606, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_roth_requires_8606 |
| retirement.l2_e23 | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_roth_requires_8606, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_roth_requires_8606 |
| retirement.l1_s | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_roth_requires_8606, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_roth_requires_8606 |
| retirement.l2_s | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_roth_requires_8606, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_roth_requires_8606 |

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
        - guard: {op: test, eq: [retirement.used_last_year, {const: false}]}
          then: retirement.h_smw4_new
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
    label: "Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero. Also, enter this amount on Form 1040 or 1040-SR, line 5b."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.smw1, take: retirement.smw8}
  - id: retirement.smw10
    printed: "(SMW 10)"
    label: "Was your annuity starting date before 1987? Yes. STOP. No. Add lines 6 and 8. This is the amount you have recovered tax free through 2025."
    type: Dollars
    expr: {op: sum, of: [retirement.smw6, retirement.smw8]}
    note: "The worksheet stops without line 10 when the annuity starting date was before 1987; the supplied inputs do not identify that date, so this line encodes the No branch (add lines 6 and 8)."
  - id: retirement.smw11
    printed: "(SMW 11)"
    label: "Balance of cost to be recovered. Subtract line 10 from line 2. If zero, you won't have to complete this worksheet next year."
    type: Dollars
    expr: {op: subtract, from: retirement.smw2, take: retirement.smw10}
  - id: retirement.one
    printed: "(helper)"
    label: "One"
    type: Count
    expr: {op: param, ref: person.one}
  - id: retirement.is_ira
    printed: "(helper)"
    label: "Whether this distribution is from an IRA"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.account, {const: "traditional_ira"}]}
        - {op: test, eq: [retirement.account, {const: "roth_ira"}]}
  - id: retirement.has_rollover
    printed: "(helper)"
    label: "Whether this distribution has a rollover"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [retirement.rollover, {const: 0}]}
        - {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
  - id: retirement.taxable
    printed: "(helper)"
    label: "Taxable amount of this distribution"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, eq: [retirement.account, {const: "roth_ira"}]}
              - {op: test, eq: [retirement.code, {const: "qualified_roth_Q"}]}
          then: retirement.h_zero
        - guard: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
          then: retirement.h_zero
        - guard:
            op: test
            all:
              - {op: test, not: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}}
              - {op: test, gt: [retirement.rollover, {const: 0}]}
              - {op: test, eq: [retirement.account, {const: "plan"}]}
          then: retirement.h_plan_rollover
        - guard:
            op: test
            all:
              - {op: test, not: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}}
              - {op: test, gt: [retirement.rollover, {const: 0}]}
              - {op: test, not: {op: test, eq: [retirement.account, {const: "plan"}]}}
          then: retirement.h_box1_less_rollover
        - guard:
            op: test
            all:
              - {op: test, not: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}}
              - {op: test, not: {op: test, gt: [retirement.rollover, {const: 0}]}}
              - {op: test, eq: [retirement.account, {const: "roth_ira"}]}
              - {op: test, not: {op: test, eq: [retirement.code, {const: "qualified_roth_Q"}]}}
          then: retirement.h_zero
        - guard:
            op: test
            all:
              - {op: test, not: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}}
              - {op: test, not: {op: test, gt: [retirement.rollover, {const: 0}]}}
              - {op: test, eq: [retirement.account, {const: "plan"}]}
              - {op: test, eq: [retirement.annuity, {const: true}]}
          then: retirement.smw9
        - guard:
            op: test
            all:
              - {op: test, not: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}}
              - {op: test, not: {op: test, gt: [retirement.rollover, {const: 0}]}}
              - {op: test, eq: [retirement.account, {const: "plan"}]}
              - {op: test, not: {op: test, eq: [retirement.annuity, {const: true}]}}
          then: retirement.h_box1_less_box5
        - guard:
            op: test
            all:
              - {op: test, not: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}}
              - {op: test, not: {op: test, gt: [retirement.rollover, {const: 0}]}}
              - {op: test, eq: [retirement.account, {const: "traditional_ira"}]}
          then: retirement.h_box1_less_rollover
    refuses:
      - retirement.special
      - retirement.h_roth_requires_8606
    note: "Nonqualified Roth IRA distributions require Form 8606 and are refused. The zero branch for a nonqualified Roth IRA is unreachable when the refusal gate is true."
  - id: retirement.amount_a
    printed: "(helper)"
    label: "Gross distribution amount for line 4a or 5a"
    type: NonNegDollars
    expr: {op: copy, from: retirement.box1}
  - id: retirement.sav_amount
    printed: "(helper)"
    label: "Distribution amount for Form 8880 line 4"
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
              - {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
          then: retirement.h_zero
        - guard:
            op: test
            not:
              op: test
              any:
                - {op: test, eq: [retirement.sav_military, {const: true}]}
                - {op: test, eq: [retirement.sav_404k, {const: true}]}
                - {op: test, eq: [retirement.sav_inherited, {const: true}]}
                - {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
          then: retirement.h_sav_base
    note: "The Form 8880 line 4 exclusion for conversions or rollovers to Roth accounts is not separately identified by the supplied inputs; only the 60-day non-Roth rollover amount and the listed military, 404(k) and inherited-IRA exclusions are applied."
  - id: retirement.l1
    printed: "(helper)"
    label: "Form 5329 line 1 early distribution amount"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_is_early_code, {const: true}]}
          then: retirement.taxable
        - guard: {op: test, eq: [retirement.h_is_early_code, {const: false}]}
          then: retirement.h_zero
    refuses:
      - retirement.early_screen
      - retirement.code_screen
      - retirement.h_other_code
  - id: retirement.l2
    printed: "(helper)"
    label: "Form 5329 line 2 exception amount"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "none"}]}
          then: retirement.h_zero
        - guard: {op: test, ne: [retirement.exception, {const: "none"}]}
          then: retirement.h_l2_capped
    refuses:
      - retirement.early_screen
      - retirement.code_screen
      - retirement.h_other_code
  - id: retirement.l2_e05
    printed: "(helper)"
    label: "Form 5329 line 2 exception 05 amount"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e05"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e05"}]}
          then: retirement.h_zero
    refuses:
      - retirement.early_screen
      - retirement.code_screen
      - retirement.h_other_code
  - id: retirement.l2_e09
    printed: "(helper)"
    label: "Form 5329 line 2 exception 09 amount"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e09"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e09"}]}
          then: retirement.h_zero
    refuses:
      - retirement.early_screen
      - retirement.code_screen
      - retirement.h_other_code
  - id: retirement.l2_e19
    printed: "(helper)"
    label: "Form 5329 line 2 exception 19 amount"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e19"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e19"}]}
          then: retirement.h_zero
    refuses:
      - retirement.early_screen
      - retirement.code_screen
      - retirement.h_other_code
  - id: retirement.l2_e22
    printed: "(helper)"
    label: "Form 5329 line 2 exception 22 amount"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e22"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e22"}]}
          then: retirement.h_zero
    refuses:
      - retirement.early_screen
      - retirement.code_screen
      - retirement.h_other_code
  - id: retirement.is_e23
    printed: "(helper)"
    label: "Whether the exception is 23"
    type: Bool
    expr: {op: test, eq: [retirement.exception, {const: "e23"}]}
  - id: retirement.l2_e23
    printed: "(helper)"
    label: "Form 5329 line 2 exception 23 amount"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.is_e23, {const: true}]}
          then: retirement.l2
        - guard: {op: test, eq: [retirement.is_e23, {const: false}]}
          then: retirement.h_zero
    refuses:
      - retirement.early_screen
      - retirement.code_screen
      - retirement.h_other_code
  - id: retirement.l1_s
    printed: "(helper)"
    label: "Form 5329 line 1 SIMPLE IRA amount"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "simple_S"}]}
          then: retirement.l1
        - guard: {op: test, ne: [retirement.code, {const: "simple_S"}]}
          then: retirement.h_zero
    refuses:
      - retirement.early_screen
      - retirement.code_screen
      - retirement.h_other_code
  - id: retirement.l2_s
    printed: "(helper)"
    label: "Form 5329 line 2 SIMPLE IRA exception amount"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "simple_S"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.code, {const: "simple_S"}]}
          then: retirement.h_zero
    refuses:
      - retirement.early_screen
      - retirement.code_screen
      - retirement.h_other_code
  - id: retirement.h_zero
    printed: "(helper)"
    label: "(helper) zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: retirement.h_box1_less_box5
    printed: "(helper)"
    label: "Gross distribution less box 5"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.box5}
  - id: retirement.h_box1_less_rollover
    printed: "(helper)"
    label: "Gross distribution less rollover"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.rollover}
  - id: retirement.h_plan_rollover
    printed: "(helper)"
    label: "Plan gross distribution less box 5 and rollover"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_box1_less_box5, take: retirement.rollover}
  - id: retirement.h_sav_base
    printed: "(helper)"
    label: "Saver's credit distribution amount before listed exclusions"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.rollover}
  - id: retirement.h_roth_requires_8606
    printed: "(helper)"
    label: "Whether a nonqualified Roth distribution requires Form 8606"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.account, {const: "roth_ira"}]}
        - {op: test, not: {op: test, eq: [retirement.code, {const: "qualified_roth_Q"}]}}
  - id: retirement.h_other_code
    printed: "(helper)"
    label: "Whether the distribution code is other"
    type: Bool
    expr: {op: test, eq: [retirement.code, {const: "other"}]}
  - id: retirement.h_is_early_code
    printed: "(helper)"
    label: "Whether the code is an early distribution subject to the additional tax"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.code, {const: "early_1"}]}
        - {op: test, eq: [retirement.code, {const: "simple_S"}]}
  - id: retirement.h_l2_capped
    printed: "(helper)"
    label: "Exception amount limited to the early distribution amount"
    type: NonNegDollars
    expr: {op: smaller_of, of: [retirement.l1, retirement.exc_amount]}
  - id: retirement.h_smw4_t1_360
    printed: "(helper)"
    label: "Cost divided by Table 1 factor 360"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_360}}
  - id: retirement.h_smw4_t1_310
    printed: "(helper)"
    label: "Cost divided by Table 1 factor 310"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_310}}
  - id: retirement.h_smw4_t1_260
    printed: "(helper)"
    label: "Cost divided by Table 1 factor 260"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_260}}
  - id: retirement.h_smw4_t1_210
    printed: "(helper)"
    label: "Cost divided by Table 1 factor 210"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_210}}
  - id: retirement.h_smw4_t1_160
    printed: "(helper)"
    label: "Cost divided by Table 1 factor 160"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_160}}
  - id: retirement.h_smw4_t2_410
    printed: "(helper)"
    label: "Cost divided by Table 2 factor 410"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_410}}
  - id: retirement.h_smw4_t2_360
    printed: "(helper)"
    label: "Cost divided by Table 2 factor 360"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_360}}
  - id: retirement.h_smw4_t2_310
    printed: "(helper)"
    label: "Cost divided by Table 2 factor 310"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_310}}
  - id: retirement.h_smw4_t2_260
    printed: "(helper)"
    label: "Cost divided by Table 2 factor 260"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_260}}
  - id: retirement.h_smw4_t2_210
    printed: "(helper)"
    label: "Cost divided by Table 2 factor 210"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_210}}
  - id: retirement.h_smw4_table1
    printed: "(helper)"
    label: "Line 4 amount using Table 1"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [retirement.age, {const: 55, type: Count}]}
          then: retirement.h_smw4_t1_360
        - guard:
            op: test
            all:
              - {op: test, gt: [retirement.age, {const: 55, type: Count}]}
              - {op: test, le: [retirement.age, {const: 60, type: Count}]}
          then: retirement.h_smw4_t1_310
        - guard:
            op: test
            all:
              - {op: test, gt: [retirement.age, {const: 60, type: Count}]}
              - {op: test, le: [retirement.age, {const: 65, type: Count}]}
          then: retirement.h_smw4_t1_260
        - guard:
            op: test
            all:
              - {op: test, gt: [retirement.age, {const: 65, type: Count}]}
              - {op: test, le: [retirement.age, {const: 70, type: Count}]}
          then: retirement.h_smw4_t1_210
        - guard: {op: test, ge: [retirement.age, {const: 71, type: Count}]}
          then: retirement.h_smw4_t1_160
  - id: retirement.h_smw4_table2
    printed: "(helper)"
    label: "Line 4 amount using Table 2"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [retirement.combined_age, {const: 110, type: Count}]}
          then: retirement.h_smw4_t2_410
        - guard:
            op: test
            all:
              - {op: test, gt: [retirement.combined_age, {const: 110, type: Count}]}
              - {op: test, le: [retirement.combined_age, {const: 120, type: Count}]}
          then: retirement.h_smw4_t2_360
        - guard:
            op: test
            all:
              - {op: test, gt: [retirement.combined_age, {const: 120, type: Count}]}
              - {op: test, le: [retirement.combined_age, {const: 130, type: Count}]}
          then: retirement.h_smw4_t2_310
        - guard:
            op: test
            all:
              - {op: test, gt: [retirement.combined_age, {const: 130, type: Count}]}
              - {op: test, le: [retirement.combined_age, {const: 140, type: Count}]}
          then: retirement.h_smw4_t2_260
        - guard: {op: test, ge: [retirement.combined_age, {const: 141, type: Count}]}
          then: retirement.h_smw4_t2_210
  - id: retirement.h_smw4_new
    printed: "(helper)"
    label: "Line 4 amount for the current year before the last-year election"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.joint_life, {const: true}]}
          then: retirement.h_smw4_table2
        - guard: {op: test, eq: [retirement.joint_life, {const: false}]}
          then: retirement.h_smw4_table1
```
