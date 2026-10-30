# Transcription agreement — retirement

Second transcription of `Form 1099-R distributions (IRAs, pensions and annuities)` by an isolated model (spec 6.5), compared line by line with `forms/2025/retirement.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
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
| output token budget | transport default (65536 for DeepSeek) |
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

Ruling: representation; i1040gi p. 26, Lines 4a and 4b, IRA Distributions. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,894 of 1,894 agree. Same set over the three-valued account Enum. Project stands.

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

Ruling: model error and scope; i1040gi p. 30, Rollovers: "Use lines 5a and 5b to report a rollover, including a direct rollover, from one qualified employer’s plan to another or to an IRA. ... Also check box 1 on line 5c."; i1040gi p. 27, Exception 1: "Enter the total distribution on line 4a if you rolled over part or all of the distribution ... Also check box 1 on line 4c.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,544 of 1,894 agree; 228 project-refuses (none completed), 89 project-unknown (none completed), 28 value (3 completed), 5 candidate-unknown (none completed). (1) A code G direct rollover with $0 in box 1 is not a rollover to the candidate; the source makes it one: classm.tcw.5, classm.f1040.3 and classm.f1040.3.deepseek (completed; code G, box 1 $0) project true, candidate false; the other value differences are on refused or incomplete returns. (2) The project-refuses are its cited retirement.special and retirement.bad_code read through retirement.rolled, and the unknowns partial records: scope. Same reading as rounds 4 and T-067 round 1. Project stands.

### retirement.taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}
```

Second transcription's note: A Roth IRA reaches this line only with code Q, for which Exception 2(b) says enter -0- on line 4b.

Ruling: model error and scope; i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost ... of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,824 of 1,894 agree; 35 project-unknown (none completed), 18 candidate-refuses (12 completed), 12 candidate-unknown (none completed), 5 project-refuses (none completed). The candidate refuses (h_recovered_bad, recovered above cost) the annuity whose cost was recovered before 2025, which the source makes fully taxable rather than out of scope: the 12 completed candidate-refuses are classm.tcw.15 (project $39,110.00) and 10 of its partial records, and generated 395 r2 (project $0.00, box 1 $0). The project-refuses are its cited retirement.special and retirement.bad_code; the unknowns are partial records: scope. Same as round 4's Claude reply. Project stands.

### retirement.amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"input": "retirement.box5"}, {"const": 0}], "test": "le"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.box5"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"input": "retirement.box1"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}], "test": "eq"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, {"args": [{"input": "retirement.box1"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}], "test": "ne"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Second transcription's note: For a fully taxable distribution the instructions say to make no entry on line 4a or 5a. A rollover, a Roth IRA distribution, a partly taxable pension and any Simplified Method annuity (SMW line 1) enter box 1.

Ruling: model error and scope; i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost ... of your pension or annuity, or (b) you got your entire cost back tax free before 2025. ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a."; i1040gi p. 27, Lines 4a and 4b: "If the distribution from your IRA is fully taxable, enter the total distribution on line 4b; don’t make an entry on line 4a.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,716 of 1,894 agree; 82 project-unknown (none completed), 44 candidate-unknown (none completed), 29 value (1 completed), 18 candidate-refuses (12 completed), 5 project-refuses (none completed). (1) The 12 completed candidate-refuses are the same h_recovered_bad refusals as on retirement.taxable (classm.tcw.15 and partials, generated 395). (2) generated 314 (completed; r2, plan, code 4, annuity true, cost $0, box 1 $46,209.90) project $0.00, candidate $46,209.90: a pension with no cost is fully taxable, "don’t make an entry on line 5a", but the candidate treats every Simplified Method annuity as partly taxable. The other value differences are on incomplete or refused returns; the project-refuses are its cited gates: scope. Project stands.

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

Second transcription's note: Other Form 8880 exclusions (conversions, excess or returned contributions, loans, Roth rollovers) are screened out by retirement.special.

Ruling: model error and scope; f8880 p. 2, Line 4: "Don’t include any of the following. • Distributions not taxable as the result of a rollover or a trustee-to-trustee transfer ... • Distributions from a military retirement plan (other than the federal TSP). • Distributions from an inherited IRA by a nonspousal beneficiary". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,640 of 1,894 agree; 137 project-refuses (none completed), 65 candidate-unknown (18 completed), 48 project-unknown (none completed), 4 candidate-refuses (none completed). No value differs. The 18 completed candidate-unknown are partial records withholding retirement.sav_military (8) or retirement.sav_404k (8) on IRA entries, or retirement.sav_inherited (2) on plan entries (partial of classm.tcw.7, plan): it applies the exclusions to account kinds the interview does not ask them of (inherited reading: amb.2025.savers_inherited_plans). The project-refuses are its cited retirement.bad_code and the candidate-refuses retirement.special on refused returns: scope. Project stands.

### retirement.l1 — Form 5329 line 1 share: the taxable amount of an early distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}
```

Second transcription's note: Codes 1, 2 and S are treated as early distributions. Codes 3, 4 and 7 are not, with a wrong code 4 or 7 screened by code_screen. The amount is the taxable amount, since a rolled-over part is not subject to the additional tax.

Ruling: ambiguity and model error (+ scope); i5329 p. 3, Line 1: "Enter the amount of early distributions includible in income (other than qualified disaster recovery distributions) that you received from:". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,234 of 1,894 agree; 643 candidate-unknown (61 completed), 13 value (2 completed), 3 candidate-refuses (none completed), 1 project-refuses (none completed). (1) Value: the candidate puts code 2 entries on line 1 (and the same amount on line 2), the other reading of amb.2025.f5329_line1_codes (chosen: line 1 holds only code 1 and S; the other reading puts code 2 on line 1 and offsets it on line 2; owner's decision D8(a)); the tax is the same: generated 175 (completed; plan, code 2, box 1 $52,095.29) project $0.00, candidate $52,095.29, and generated 348 (IRA, code 2) $0.00 against $4,784.11; the 11 refused-return values are the same reading. (2) It declares the screens on every entry (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused): of the 61 completed candidate-unknown, 54 need early_screen on other codes and 7 need code_screen on code 1 or S entries (partial of classm.s2.3.deepseek). Candidate-refuses on refused returns; project-refuses the cited retirement.bad_code: scope. Project stands.

### retirement.l2 — Form 5329 line 2 share before the per-person limits
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}], "op": "choose"}
```

Second transcription's note: For code 2, the whole distribution is treated as excepted (a partial exception is screened by code_screen) and is not assigned to the per-person capped exception amounts below. This reading is a choice, since the text does not say whether the payer's code 2 replaces the per-person limits.

Ruling: ambiguity and model error; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,236 of 1,894 agree; 643 candidate-unknown (56 completed), 13 value (2 completed), 2 candidate-refuses (none completed). (1) Value: generated 175 ($0.00 against $52,095.29) and generated 348 ($0.00 against $4,784.11), completed, are the code 2 offset of amb.2025.f5329_line1_codes (chosen: line 1 holds only code 1 and S; the other reading puts code 2 on line 1 and offsets it on line 2; owner's decision D8(a)), equal to the candidate's line 1. (2) The 56 completed candidate-unknown need retirement.exception (53), early_screen (1) or code_screen (2) on entries the source does not ask them of (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7, decision D3(a), the cited screens of retirement.screen_refused). Candidate-refuses on refused returns only. Project stands.

### retirement.l2_e05 — Line 2 share under exception 05
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,358 of 1,894 agree; 536 candidate-unknown (54 completed). The exception number is asked only for a code 1 or S entry (retirement.has_exception); the candidate tests retirement.exception = e05 on every entry, so its completed candidate-unknown need that answer (or code_screen) on entries it is not asked of (classm.dependent.5.deepseek, code 7, project $0.00). No value differs. Project stands.

### retirement.l2_e09 — Line 2 share under exception 09
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,359 of 1,894 agree; 535 candidate-unknown (53 completed). The exception number is asked only for a code 1 or S entry (retirement.has_exception); the candidate tests retirement.exception = e09 on every entry, so its completed candidate-unknown need that answer (or code_screen) on entries it is not asked of (classm.dependent.5.deepseek, code 7, project $0.00). No value differs. Project stands.

### retirement.l2_e19 — Line 2 share under exception 19
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,358 of 1,894 agree; 536 candidate-unknown (54 completed). The exception number is asked only for a code 1 or S entry (retirement.has_exception); the candidate tests retirement.exception = e19 on every entry, so its completed candidate-unknown need that answer (or code_screen) on entries it is not asked of (classm.dependent.5.deepseek, code 7, project $0.00). No value differs. Project stands.

### retirement.l2_e22 — Line 2 share under exception 22
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,359 of 1,894 agree; 535 candidate-unknown (53 completed). The exception number is asked only for a code 1 or S entry (retirement.has_exception); the candidate tests retirement.exception = e22 on every entry, so its completed candidate-unknown need that answer (or code_screen) on entries it is not asked of (classm.dependent.5.deepseek, code 7, project $0.00). No value differs. Project stands.

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

Second transcription's note: Counts every distribution entered under exception 23, whatever its code.

Ruling: model error; p590b p. 28, Emergency personal expense distributions, Distribution limits: "You are limited to taking one emergency personal expense distribution per calendar year"; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,282 of 1,894 agree; 612 candidate-unknown (54 completed). The reply now tests retirement.exception = e23 without the code 1 or S guard, so the 54 completed candidate-unknown need the exception answer on entries it is not asked of (classm.dependent.5.deepseek, code 7, project false). No value differs. Round 1's reply was guarded (representation). Project stands.

### retirement.l2_e23 — Line 2 share under exception 23
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "The additional tax on early distributions doesn’t apply to the distributions described next. Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99."; p590b p. 28, Emergency personal expense distributions, Distribution limits: "You are limited to taking one emergency personal expense distribution per calendar year". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,359 of 1,894 agree; 535 candidate-unknown (53 completed). The exception number is asked only for a code 1 or S entry (retirement.has_exception); the candidate tests retirement.exception = e23 on every entry, so its completed candidate-unknown need that answer (or code_screen) on entries it is not asked of (classm.dependent.5.deepseek, code 7, project $0.00). No value differs. Project stands.

### retirement.l1_s — Line 1 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 4: "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%. These distributions are included in boxes 1 and 2a of Form 1099-R and are designated with code S in box 7.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,891 of 1,894 agree; 2 candidate-unknown (2 completed), 1 project-refuses (none completed). The code S share is the project's; the 2 completed candidate-unknown are partial records withholding retirement.code_screen on a code S entry, a screen for codes 2, 4 and 7 only; the project-refuses is its cited retirement.bad_code: scope. Project stands.

### retirement.l2_s — Line 2 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i5329 p. 5, Line 4: "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%. These distributions are included in boxes 1 and 2a of Form 1099-R and are designated with code S in box 7.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,894 of 1,894 agree. The code S share of line 2 is the project's. Project stands.

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
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"input": "retirement.age"}, {"const": 55, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_360"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"input": "retirement.age"}, {"const": 60, "type": "Count"}], "test": "le"}, {"args": [{"const": 55, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_310"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"input": "retirement.age"}, {"const": 65, "type": "Count"}], "test": "le"}, {"args": [{"const": 60, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_260"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"input": "retirement.age"}, {"const": 70, "type": "Count"}], "test": "le"}, {"args": [{"const": 65, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_210"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": 70, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_160"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 110, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_410"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 120, "type": "Count"}], "test": "le"}, {"args": [{"const": 110, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_360"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 130, "type": "Count"}], "test": "le"}, {"args": [{"const": 120, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_310"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 140, "type": "Count"}], "test": "le"}, {"args": [{"const": 130, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_260"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": 140, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_210"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"input": "retirement.last_line4"}}], "op": "choose"}
```

Second transcription's note: Line 3 (the table number) is folded into the divisor rates. Only the 'after November 18, 1996' column of Table 1 is used, since earlier starting dates are screened out by retirement.special. The worksheet does not say how to round the quotient; it is rounded half-up to the cent.

Ruling: model error; i1040gi p. 29, Simplified Method Worksheet, line 4 and the note under line 2; i1040gi p. 30, Simplified Method: "If you must use the Simplified Method, complete the Simplified Method Worksheet in these instructions to figure the taxable part of your pension or annuity."; i1040gi p. 28, Fully Taxable Pensions and Annuities: "(a) you didn’t contribute to the cost ... or (b) you got your entire cost back tax free before 2025"; i1040gi p. 29, line 11: "If zero, you won’t have to complete this worksheet next year." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,376 fixtures, 500 generated returns seed 20261026, 1,000 partial records from 40 bases; 1,894 comparisons; uncapped re-run of triage.mjs in scratch, same counts): 1,496 of 1,894 agree; 313 candidate-unknown (87 completed), 85 candidate-shows-skipped (1 completed). All 398 differences are on entries where the project hides the line (retirement.smw_shown false). The reply gives the worksheet lines no hiding condition, so it shows line 4 on entries the source never takes through the worksheet: the 85 candidate-shows-skipped are cost-recovered annuities (generated 395 r2, completed, $1,550.08 from last year's line 4; stage10.smw.cost_recovered[_box5], stage10.smw.recovered_exceeds_cost, stage21.t067.smw_hidden_cost_recovered and partials, $119.23; generated 184, 214 and 229, refused) and the IRA entry of classm.dcprov.1 ($624.31, refused); the 313 candidate-unknown (87 completed) need worksheet answers on IRA and non-annuity plan entries. Its value is the project's wherever the project shows the line. The worksheet lines now carry shown_when retirement.smw_shown (is_ira false, tested first, and annuity_with_cost true; BUG-0207, BUG-0208). Checked by evaluating: classm.s2.3.deepseek without the worksheet answers and stage21.t067.smw_hidden_ira (IRA, annuity unasked; interview complete) show no (SMW n) line; stage10.smw.cost_recovered, stage10.smw.recovered_exceeds_cost, stage21.t067.smw_hidden_cost_recovered, classm.tcw.15 and generated 395 (cost recovered or $0) show none, with 5a $0 and 5b box 1; a code 7 plan pension with annuity false shows none (5b $20,000); stage10.smw.first_year and a variant with $500 of cost left show all ten lines, (SMW 9) equal to 5b. A sweep of all 1,376 fixtures and 500 generated returns found smw_shown equal to (plan, annuity true, cost above recovered) on every entry where those are answered, false on every IRA entry (answered or not); the only unknown is a plan entry on a return refused on retirement.special before annuity is asked (stage16.cleanup.refuse.retirement.special_first). The project's hiding condition is right; no finding. Project stands.

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
| retirement.has_rollover | retirement.h_rollover_bad | retirement.h_rollover_bad |
| retirement.taxable | retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate, retirement.special | retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate |
| retirement.amount_a | retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate, retirement.special | retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate |
| retirement.sav_amount | retirement.h_rollover_bad, retirement.special | retirement.h_rollover_bad |
| retirement.l1 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_exc_mismatch, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_exc_mismatch, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate |
| retirement.l2 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_exc_mismatch, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_exc_mismatch, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate |
| retirement.l2_e05 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_exc_mismatch, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_exc_mismatch, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate |
| retirement.l2_e09 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_exc_mismatch, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_exc_mismatch, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate |
| retirement.l2_e19 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_exc_mismatch, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_exc_mismatch, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate |
| retirement.l2_e22 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_exc_mismatch, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_exc_mismatch, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate |
| retirement.l2_e23 | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_exc_mismatch, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_exc_mismatch, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate |
| retirement.l1_s | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_exc_mismatch, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_exc_mismatch, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate |
| retirement.l2_s | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_exc_mismatch, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_annuity_rollover, retirement.h_code_other, retirement.h_exc_mismatch, retirement.h_recovered_bad, retirement.h_rollover_bad, retirement.h_roth_gate |
| (SMW 7) | retirement.h_recovered_bad | retirement.h_recovered_bad |
| (SMW 8) | retirement.h_recovered_bad | retirement.h_recovered_bad |
| (SMW 9) | retirement.h_recovered_bad | retirement.h_recovered_bad |
| (SMW 10) | retirement.h_recovered_bad | retirement.h_recovered_bad |
| (SMW 11) | retirement.h_recovered_bad | retirement.h_recovered_bad |

## Raw second transcription

```yaml
```yaml
lines:
  - id: retirement.one
    printed: "(helper)"
    label: "One (this Form 1099-R distribution, for counting)"
    type: Count
    expr: {op: param, ref: person.one}

  - id: retirement.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: retirement.is_ira
    printed: "(helper)"
    label: "Distribution from an IRA (traditional, SEP, SIMPLE or Roth), reported on lines 4a and 4b rather than 5a and 5b"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: ["retirement.account", {const: "traditional_ira"}]}
        - {op: test, eq: ["retirement.account", {const: "roth_ira"}]}

  - id: retirement.h_rollover_bad
    printed: "(helper)"
    label: "Consistency check: amount rolled over is more than the gross distribution in box 1"
    type: Bool
    expr: {op: test, gt: ["retirement.rollover", "retirement.box1"]}

  - id: retirement.h_rolled
    printed: "(helper)"
    label: "Amount of the distribution rolled over (the whole distribution for a direct rollover, code G)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: ["retirement.code", {const: "direct_rollover_G"}]}
          then: retirement.box1
        - guard: {op: test, ne: ["retirement.code", {const: "direct_rollover_G"}]}
          then: retirement.rollover
    refuses:
      - {when: retirement.h_rollover_bad, when_known: true}

  - id: retirement.has_rollover
    printed: "(helper)"
    label: "You rolled over part or all of the distribution (check box 1 on line 4c or 5c)"
    type: Bool
    expr: {op: test, gt: ["retirement.h_rolled", {const: 0}]}

  - id: retirement.h_roth_gate
    printed: "(helper)"
    label: "Roth IRA distribution other than code Q, or code Q on a distribution that is not from a Roth IRA (Form 8606 or Pub. 575 needed)"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          all:
            - {op: test, eq: ["retirement.account", {const: "roth_ira"}]}
            - {op: test, ne: ["retirement.code", {const: "qualified_roth_Q"}]}
        - op: test
          all:
            - {op: test, ne: ["retirement.account", {const: "roth_ira"}]}
            - {op: test, eq: ["retirement.code", {const: "qualified_roth_Q"}]}
    note: "Exception 2 sends a Roth IRA distribution to Form 8606 unless code Q (or code T with an early Roth contribution) applies; only code Q is computed. The supplied text does not say how a code Q distribution from a designated Roth account in a plan is taxed, so that case is also refused."

  - id: retirement.h_code_other
    printed: "(helper)"
    label: "Distribution code is another code or two codes"
    type: Bool
    expr: {op: test, eq: ["retirement.code", {const: "other"}]}
    note: "The supplied text does not determine the taxable or early-distribution treatment of the remaining codes (for example B, L, 5 or combined codes); chosen to refuse rather than guess."

  - id: retirement.h_annuity_rollover
    printed: "(helper)"
    label: "Rollover of a pension or annuity figured with the Simplified Method"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: ["retirement.account", {const: "plan"}]}
        - {op: test, eq: ["retirement.annuity", {const: true}]}
        - {op: test, gt: ["retirement.h_rolled", {const: 0}]}
    note: "The Simplified Method Worksheet has no step for a rollover; this combination is refused."

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
    note: "A death benefit exclusion added to line 2 is screened out by retirement.special."

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

  - id: retirement.smw4
    printed: "(SMW 4)"
    label: "Divide line 2 by the number on line 3 (if you completed this worksheet last year, enter the amount from line 4 of last year's worksheet)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: ["retirement.used_last_year", {const: true}]}
          then: retirement.last_line4
        - guard:
            op: test
            all:
              - {op: test, eq: ["retirement.used_last_year", {const: false}]}
              - {op: test, eq: ["retirement.joint_life", {const: false}]}
              - {op: test, le: ["retirement.age", {const: 55, type: Count}]}
          then: retirement.h_t1_360
        - guard:
            op: test
            all:
              - {op: test, eq: ["retirement.used_last_year", {const: false}]}
              - {op: test, eq: ["retirement.joint_life", {const: false}]}
              - {op: test, gt: ["retirement.age", {const: 55, type: Count}]}
              - {op: test, le: ["retirement.age", {const: 60, type: Count}]}
          then: retirement.h_t1_310
        - guard:
            op: test
            all:
              - {op: test, eq: ["retirement.used_last_year", {const: false}]}
              - {op: test, eq: ["retirement.joint_life", {const: false}]}
              - {op: test, gt: ["retirement.age", {const: 60, type: Count}]}
              - {op: test, le: ["retirement.age", {const: 65, type: Count}]}
          then: retirement.h_t1_260
        - guard:
            op: test
            all:
              - {op: test, eq: ["retirement.used_last_year", {const: false}]}
              - {op: test, eq: ["retirement.joint_life", {const: false}]}
              - {op: test, gt: ["retirement.age", {const: 65, type: Count}]}
              - {op: test, le: ["retirement.age", {const: 70, type: Count}]}
          then: retirement.h_t1_210
        - guard:
            op: test
            all:
              - {op: test, eq: ["retirement.used_last_year", {const: false}]}
              - {op: test, eq: ["retirement.joint_life", {const: false}]}
              - {op: test, gt: ["retirement.age", {const: 70, type: Count}]}
          then: retirement.h_t1_160
        - guard:
            op: test
            all:
              - {op: test, eq: ["retirement.used_last_year", {const: false}]}
              - {op: test, eq: ["retirement.joint_life", {const: true}]}
              - {op: test, le: ["retirement.combined_age", {const: 110, type: Count}]}
          then: retirement.h_t2_410
        - guard:
            op: test
            all:
              - {op: test, eq: ["retirement.used_last_year", {const: false}]}
              - {op: test, eq: ["retirement.joint_life", {const: true}]}
              - {op: test, gt: ["retirement.combined_age", {const: 110, type: Count}]}
              - {op: test, le: ["retirement.combined_age", {const: 120, type: Count}]}
          then: retirement.h_t2_360
        - guard:
            op: test
            all:
              - {op: test, eq: ["retirement.used_last_year", {const: false}]}
              - {op: test, eq: ["retirement.joint_life", {const: true}]}
              - {op: test, gt: ["retirement.combined_age", {const: 120, type: Count}]}
              - {op: test, le: ["retirement.combined_age", {const: 130, type: Count}]}
          then: retirement.h_t2_310
        - guard:
            op: test
            all:
              - {op: test, eq: ["retirement.used_last_year", {const: false}]}
              - {op: test, eq: ["retirement.joint_life", {const: true}]}
              - {op: test, gt: ["retirement.combined_age", {const: 130, type: Count}]}
              - {op: test, le: ["retirement.combined_age", {const: 140, type: Count}]}
          then: retirement.h_t2_260
        - guard:
            op: test
            all:
              - {op: test, eq: ["retirement.used_last_year", {const: false}]}
              - {op: test, eq: ["retirement.joint_life", {const: true}]}
              - {op: test, gt: ["retirement.combined_age", {const: 140, type: Count}]}
          then: retirement.h_t2_210
    note: "Line 3 (the table number) is folded into the divisor rates. Only the 'after November 18, 1996' column of Table 1 is used, since earlier starting dates are screened out by retirement.special. The worksheet does not say how to round the quotient; it is rounded half-up to the cent."

  - id: retirement.smw5
    printed: "(SMW 5)"
    label: "Multiply line 4 by the number of months for which this year's payments were made"
    type: NonNegDollars
    expr: {op: multiply_count, amount: retirement.smw4, count: retirement.months}
    note: "The pre-1987 skip to line 8 never applies in scope, because annuity starting dates before November 19, 1996 are screened out by retirement.special."

  - id: retirement.smw6
    printed: "(SMW 6)"
    label: "Enter the amount, if any, recovered tax free in years after 1986. If you completed this worksheet last year, enter the amount from line 10 of last year's worksheet"
    type: NonNegDollars
    expr: {op: copy, from: retirement.recovered}

  - id: retirement.h_recovered_bad
    printed: "(helper)"
    label: "Consistency check: amount recovered tax free is more than your cost"
    type: Bool
    expr: {op: test, gt: ["retirement.recovered", "retirement.cost"]}

  - id: retirement.smw7
    printed: "(SMW 7)"
    label: "Subtract line 6 from line 2"
    type: Dollars
    expr: {op: subtract, from: retirement.smw2, take: retirement.smw6}
    refuses:
      - {when: retirement.h_recovered_bad, when_known: true}

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
    label: "Add lines 6 and 8. This is the amount you have recovered tax free through 2025"
    type: Dollars
    expr: {op: sum, of: [retirement.smw6, retirement.smw8]}
    note: "The 'Yes, starting date before 1987, STOP' branch never applies in scope (see line 5)."

  - id: retirement.smw11
    printed: "(SMW 11)"
    label: "Balance of cost to be recovered. Subtract line 10 from line 2"
    type: Dollars
    expr: {op: subtract, from: retirement.smw2, take: retirement.smw10}

  - id: retirement.h_ira_taxable
    printed: "(helper)"
    label: "Traditional IRA: part of the distribution not rolled over (line 4b)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.h_rolled}

  - id: retirement.h_plan_net
    printed: "(helper)"
    label: "Box 1 minus contributions taxable when made (box 5)"
    type: Dollars
    expr: {op: subtract, from: retirement.box1, take: retirement.box5}

  - id: retirement.h_plan_taxable
    printed: "(helper)"
    label: "Pension or plan distribution (not Simplified Method): box 1 minus box 5 minus the rollover"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_plan_net, take: retirement.h_rolled}
    note: "The Rollovers instruction gives box 1 less box 5 less the rollover. Applied also when there is no rollover, reading box 5 as the after-tax investment recovered tax free this year; this case is otherwise fully taxable when box 5 is zero."

  - id: retirement.taxable
    printed: "(helper)"
    label: "Taxable amount of this distribution (included in Form 1040 line 4b or 5b)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: ["retirement.account", {const: "traditional_ira"}]}
          then: retirement.h_ira_taxable
        - guard: {op: test, eq: ["retirement.account", {const: "roth_ira"}]}
          then: retirement.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: ["retirement.account", {const: "plan"}]}
              - {op: test, eq: ["retirement.annuity", {const: true}]}
          then: retirement.smw9
        - guard:
            op: test
            all:
              - {op: test, eq: ["retirement.account", {const: "plan"}]}
              - {op: test, eq: ["retirement.annuity", {const: false}]}
          then: retirement.h_plan_taxable
    refuses: [retirement.special, retirement.h_roth_gate, retirement.h_annuity_rollover, retirement.h_code_other]
    note: "A Roth IRA reaches this line only with code Q, for which Exception 2(b) says enter -0- on line 4b."

  - id: retirement.h_fully
    printed: "(helper)"
    label: "Distribution is fully taxable and not figured on the Simplified Method Worksheet (no entry on line 4a or 5a)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: ["retirement.taxable", "retirement.box1"]}
        - op: test
          not:
            op: test
            all:
              - {op: test, eq: ["retirement.account", {const: "plan"}]}
              - {op: test, eq: ["retirement.annuity", {const: true}]}

  - id: retirement.amount_a
    printed: "(helper)"
    label: "Amount of this distribution entered on Form 1040 line 4a or 5a"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: ["retirement.h_fully", {const: true}]}
          then: retirement.h_zero
        - guard: {op: test, eq: ["retirement.h_fully", {const: false}]}
          then: retirement.box1
    note: "For a fully taxable distribution the instructions say to make no entry on line 4a or 5a. A rollover, a Roth IRA distribution, a partly taxable pension and any Simplified Method annuity (SMW line 1) enter box 1."

  - id: retirement.h_sav_net
    printed: "(helper)"
    label: "Distribution not counting the part not taxable because of a rollover"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.h_rolled}

  - id: retirement.h_sav_excluded
    printed: "(helper)"
    label: "Distribution excluded from Form 8880 line 4 (military retirement plan, section 404(k) dividends, inherited IRA of a nonspouse beneficiary)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: ["retirement.sav_military", {const: true}]}
        - {op: test, eq: ["retirement.sav_404k", {const: true}]}
        - {op: test, eq: ["retirement.sav_inherited", {const: true}]}

  - id: retirement.sav_amount
    printed: "(helper)"
    label: "Amount of this 2025 distribution counted on Form 8880, line 4"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: ["retirement.h_sav_excluded", {const: true}]}
          then: retirement.h_zero
        - guard: {op: test, eq: ["retirement.h_sav_excluded", {const: false}]}
          then: retirement.h_sav_net
    refuses: [retirement.special]
    note: "Other Form 8880 exclusions (conversions, excess or returned contributions, loans, Roth rollovers) are screened out by retirement.special."

  - id: retirement.h_exc_mismatch
    printed: "(helper)"
    label: "Consistency check: the exception chosen does not apply to this kind of account (01 and 06 do not apply to IRAs; 07, 08 and 09 are IRA distributions only)"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          all:
            - {op: test, eq: ["retirement.is_ira", {const: true}]}
            - op: test
              any:
                - {op: test, eq: ["retirement.exception", {const: "e01"}]}
                - {op: test, eq: ["retirement.exception", {const: "e06"}]}
        - op: test
          all:
            - {op: test, eq: ["retirement.account", {const: "plan"}]}
            - op: test
              any:
                - {op: test, eq: ["retirement.exception", {const: "e07"}]}
                - {op: test, eq: ["retirement.exception", {const: "e08"}]}
                - {op: test, eq: ["retirement.exception", {const: "e09"}]}

  - id: retirement.l1
    printed: "(helper)"
    label: "Early distributions includible in income from this distribution (Form 5329, line 1)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            any:
              - {op: test, eq: ["retirement.code", {const: "early_1"}]}
              - {op: test, eq: ["retirement.code", {const: "simple_S"}]}
              - {op: test, eq: ["retirement.code", {const: "early_exception_2"}]}
          then: retirement.taxable
        - guard:
            op: test
            not:
              op: test
              any:
                - {op: test, eq: ["retirement.code", {const: "early_1"}]}
                - {op: test, eq: ["retirement.code", {const: "simple_S"}]}
                - {op: test, eq: ["retirement.code", {const: "early_exception_2"}]}
          then: retirement.h_zero
    refuses:
      - retirement.early_screen
      - retirement.code_screen
      - {when: retirement.h_exc_mismatch, when_known: true}
    note: "Codes 1, 2 and S are treated as early distributions. Codes 3, 4 and 7 are not, with a wrong code 4 or 7 screened by code_screen. The amount is the taxable amount, since a rolled-over part is not subject to the additional tax."

  - id: retirement.h_has_exc
    printed: "(helper)"
    label: "An exception number is entered for this distribution"
    type: Bool
    expr: {op: test, ne: ["retirement.exception", {const: "none"}]}

  - id: retirement.h_exc_min
    printed: "(helper)"
    label: "Exception amount, not more than the early distribution"
    type: NonNegDollars
    expr: {op: smaller_of, of: [retirement.exc_amount, retirement.l1]}

  - id: retirement.h_l2_coded
    printed: "(helper)"
    label: "Amount excluded by the exception entered (codes 1 and S)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: ["retirement.h_has_exc", {const: true}]}
          then: retirement.h_exc_min
        - guard: {op: test, eq: ["retirement.h_has_exc", {const: false}]}
          then: retirement.h_zero

  - id: retirement.l2
    printed: "(helper)"
    label: "Amount of this distribution excluded by an exception to the additional tax (Form 5329, line 2), before the per-person dollar limits"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: ["retirement.code", {const: "early_exception_2"}]}
          then: retirement.l1
        - guard: {op: test, ne: ["retirement.code", {const: "early_exception_2"}]}
          then: retirement.h_l2_coded
    note: "For code 2, the whole distribution is treated as excepted (a partial exception is screened by code_screen) and is not assigned to the per-person capped exception amounts below. This reading is a choice, since the text does not say whether the payer's code 2 replaces the per-person limits."

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
              - {op: test, ne: ["retirement.code", {const: "early_exception_2"}]}
              - {op: test, eq: ["retirement.exception", {const: "e05"}]}
          then: retirement.l2
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, ne: ["retirement.code", {const: "early_exception_2"}]}
                - {op: test, eq: ["retirement.exception", {const: "e05"}]}
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
              - {op: test, ne: ["retirement.code", {const: "early_exception_2"}]}
              - {op: test, eq: ["retirement.exception", {const: "e09"}]}
          then: retirement.l2
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, ne: ["retirement.code", {const: "early_exception_2"}]}
                - {op: test, eq: ["retirement.exception", {const: "e09"}]}
          then: retirement.h_zero

  - id: retirement.l2_e19
    printed: "(helper)"
    label: "Part of line 2 under exception 19 (birth or adoption, up to $5,000)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, ne: ["retirement.code", {const: "early_exception_2"}]}
              - {op: test, eq: ["retirement.exception", {const: "e19"}]}
          then: retirement.l2
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, ne: ["retirement.code", {const: "early_exception_2"}]}
                - {op: test, eq: ["retirement.exception", {const: "e19"}]}
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
              - {op: test, ne: ["retirement.code", {const: "early_exception_2"}]}
              - {op: test, eq: ["retirement.exception", {const: "e22"}]}
          then: retirement.l2
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, ne: ["retirement.code", {const: "early_exception_2"}]}
                - {op: test, eq: ["retirement.exception", {const: "e22"}]}
          then: retirement.h_zero

  - id: retirement.is_e23
    printed: "(helper)"
    label: "This is an emergency personal expense distribution (exception 23)"
    type: Bool
    expr: {op: test, eq: ["retirement.exception", {const: "e23"}]}
    note: "Counts every distribution entered under exception 23, whatever its code."

  - id: retirement.l2_e23
    printed: "(helper)"
    label: "Part of line 2 under exception 23 (emergency personal expenses)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            all:
              - {op: test, ne: ["retirement.code", {const: "early_exception_2"}]}
              - {op: test, eq: ["retirement.is_e23", {const: true}]}
          then: retirement.l2
        - guard:
            op: test
            not:
              op: test
              all:
                - {op: test, ne: ["retirement.code", {const: "early_exception_2"}]}
                - {op: test, eq: ["retirement.is_e23", {const: true}]}
          then: retirement.h_zero

  - id: retirement.l1_s
    printed: "(helper)"
    label: "Part of line 1 from a SIMPLE IRA in the first 2 years of participation (code S, 25% rate on line 4)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: ["retirement.code", {const: "simple_S"}]}
          then: retirement.l1
        - guard: {op: test, ne: ["retirement.code", {const: "simple_S"}]}
          then: retirement.h_zero

  - id: retirement.l2_s
    printed: "(helper)"
    label: "Part of line 2 from a code S SIMPLE IRA distribution"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: ["retirement.code", {const: "simple_S"}]}
          then: retirement.l2
        - guard: {op: test, ne: ["retirement.code", {const: "simple_S"}]}
          then: retirement.h_zero
```
```
