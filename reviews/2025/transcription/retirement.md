# Transcription agreement — retirement

Second transcription of `Form 1099-R distributions (IRAs, pensions and annuities)` by an isolated model (spec 6.5), compared line by line with `forms/2025/retirement.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | a41b38e4f59afdcf40afbbe211734b330954f9dfa51d847fdcd4d371bd578b48 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 9beda0d63a6d970b36d7ec3db41ee0731cda5e9e070a7b3cfe910ebf8c9c1b00 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 4d76fe9c3a2591d4836a843bbecd1d9e3fa1771d6e6711001c1d9b9e1ceea70b |
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

Ruling: representation; i1040gi p. 26, Lines 4a and 4b, IRA Distributions (the IRA lines take traditional and Roth IRA distributions; the account Enum is traditional_ira, roth_ira or plan). The candidate tests account = traditional_ira or roth_ira; the project tests account ≠ plan, the same set over the three-valued Enum. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 2,463 of 2,463 agree. Same reply text as round 2. Project stands.

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

Ruling: scope; i1040gi p. 27, Exception 1: "Enter the total distribution on line 4a if you rolled over part or all of the distribution ... If the total distribution wasn’t rolled over, enter the part not rolled over on line 4b"; i1040gi p. 30, Rollovers. The candidate's test (code G, or a rollover amount above zero) is the project's. Every difference is the project's: it reads retirement.rolled, which carries the cited refusals retirement.special and retirement.bad_code. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 2,157 of 2,463 agree; 186 project-refuses (none completed), 120 project-unknown (none completed). The project-refuses are on refused returns (for example classm.w2.1.deepseek on bad_code, classm.f8606.1 on special) but one incomplete; the project-unknown are partial records that withhold retirement.account, retirement.code or retirement.special, which the interview asks of every entry. No value differs. Same reply text as round 2. Project stands.

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

Ruling: model error; i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost ... or (b) you got your entire cost back tax free before 2025 ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a."; i1040gi p. 30, Rollovers: "Use lines 5a and 5b to report a rollover, including a direct rollover, from one qualified employer’s plan to another or to an IRA. Enter on line 5a the distribution from Form 1099-R, box 1. From this amount, subtract any contributions (usually shown in box 5) that were taxable to you when made. From that result, subtract the amount of the rollover". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 2,173 of 2,463 agree; 46 value (5 completed), 123 project-refuses (none completed), 6 candidate-unknown (none completed), 115 project-unknown (none completed). Its branches are the project's otherwise, and the round-2 gate h_recovered_bad is gone. Two errors: (1) its Simplified Method line 7 is signed, so when the answers put the amount recovered above the cost its line 8 is negative and line 9 exceeds box 1, where the source makes the payments fully taxable: classm.tcw.15 (completed; cost $0, recovered $9,979, box 1 $39,110) project $39,110.00, candidate $49,089.00 (the completed differences include it); (2) a code G direct rollover is taxed unless the rollover amount is also answered. The project takes the whole box 1 as rolled over on a code G entry (retirement.rolled; the rollover question says "for a direct rollover, code G, the whole distribution is treated as rolled over") and does not read the amount there. Fixtures that answer it $0 show the difference: classm.aqee.1.deepseek, classm.eic.4.deepseek, classm.clcw.3.deepseek and classm.retirement.4.deepseek (plan or IRA, code G, refused returns). On the partial records that withhold retirement.rollover on such an entry, as the interview does, the candidate is unknown (classm.aqee.1[.deepseek]): project $0.00, candidate the whole box 1 ($45,285.00 on classm.aqee.1.deepseek). The project-refuses are its cited retirement.bad_code, retirement.annuity_rollover and retirement.screen_refused (witnesses 0, 7-11: scope); the project-unknown are partial records withholding the cited screens or answers asked of every entry (code, account). Project stands.

### retirement.amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"input": "retirement.box5"}, {"const": 0}], "test": "le"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.box5"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"input": "retirement.box1"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"input": "retirement.box1"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}], "test": "ne"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Second transcription's note: 'Fully taxable' is read as the taxable amount equalling box 1. In that case the instructions say to enter the total on line 4b or 5b and make no entry on line 4a or 5a. Otherwise (a rollover, a Roth exception, after-tax cost) the total goes on line 4a or 5a.

Ruling: model error; i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost ... or (b) you got your entire cost back tax free before 2025 ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a."; i1040gi p. 29, Simplified Method Worksheet, line 1: "Enter the total pension or annuity payments from Form 1099-R, box 1. Also, enter this amount on Form 1040 or 1040-SR, line 5a". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 2,099 of 2,463 agree; 42 value (5 completed), 123 project-refuses (none completed), 84 candidate-unknown (none completed), 115 project-unknown (none completed). The candidate leaves line 4a/5a blank when its taxable amount equals box 1, so it inherits both errors of retirement.taxable: classm.tcw.15 (completed) project $0.00 (fully taxable, no line 5a entry), candidate $39,110.00, because its taxable amount $49,089.00 is not box 1; and a code G entry answered with a $0 rollover is fully taxable to it, so line 5a is blank (classm.aqee.1.deepseek, refused: project $45,285.00, candidate $0.00). By reading, as in round 2, it also leaves line 5a blank for a Simplified Method annuity whose worksheet line 8 is zero, against worksheet line 1. The project-refuses are cited gates (scope); the unknowns are partial records withholding answers asked of every entry. Project stands.

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

Second transcription's note: The other Form 8880 exclusions (conversions, in-plan Roth rollovers, excess contributions, returned contributions) are screened out by retirement.special. Loans treated as distributions are not separately identifiable from the interface.

Ruling: model error; f8880 p. 2, Line 4: "Don’t include any of the following. • Distributions not taxable as the result of a rollover or a trustee-to-trustee transfer ... • Distributions from a military retirement plan (other than the federal TSP). • Distributions from an inherited IRA by a nonspousal beneficiary". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 1,987 of 2,463 agree; 47 value (3 completed), 178 project-refuses (none completed), 82 candidate-unknown (23 completed), 169 project-unknown (none completed). (1) As in round 2 it applies the military-plan and section 404(k) exclusions to IRA entries and the inherited-IRA exclusion to plan entries, so it needs answers the source does not ask of that kind of account: partial of classm.s2.3.deepseek withholding retirement.sav_military (completed) project $92.00, candidate unknown (the inherited reading is amb.2025.savers_inherited_plans). (2) A code G direct rollover answered with a $0 rollover counts in full, though it is not taxable as the result of a rollover: classm.retirement.4 (refused) project $0.00, candidate $10,905.00 (see retirement.taxable). The project-refuses are its cited retirement.bad_code and retirement.special (scope). Project stands.

### retirement.l1 — Form 5329 line 1 share: the taxable amount of an early distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}
```

Second transcription's note: Distributions with codes 2 and 3 show an exception that covers the whole distribution (partial coverage is screened out by code_screen), so they are not entered here. Codes 4, 7, G and Q are not early. A taxable distribution coded 'other' refuses, because the text does not let the tool decide whether it is early.

Ruling: model error and scope; i5329 p. 3, Line 1: "Enter the amount of early distributions includible in income (other than qualified disaster recovery distributions) that you received from:". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 1,556 of 2,463 agree; 9 candidate-refuses (none completed), 1 project-refuses (none completed), 897 candidate-unknown (42 completed). (1) The candidate declares retirement.early_screen and retirement.code_screen as refusals of every entry, so it needs screen answers on entries neither screen concerns (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7 (decision D3(a), the cited screens of retirement.screen_refused)): classm.dependent.5.deepseek (completed; code 7) project $0.00, candidate unknown. (2) Its candidate-refuses are its h_other_code and h_roth_nonq on refused returns (code other or a Roth entry without code Q, generated 184, 201, 292, 332, 471, 475), entries the project refuses on retirement.bad_code, and the project-refuses is the cited retirement.bad_code (stage21.refuse.bad_code_screen_unasked): scope. No value differs: line 1 now holds only code 1 and S entries, the chosen reading of amb.2025.f5329_line1_codes (round 2 put codes 2 and 3 there). Project stands.

### retirement.l2 — Form 5329 line 2 share before the per-person limits
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: This line covers every exception kind for this distribution, before the per-person dollar limits (05, 09, 19, 22, 23). Those limits are applied at person level from the l2_eNN lines, as the exc_amount question says. The text does not say whether l2 should exclude the capped kinds; including them is the reading chosen.

Ruling: model error and scope; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 1,548 of 2,463 agree; 13 candidate-refuses (none completed), 902 candidate-unknown (42 completed). The excepted amount (the exception amount capped by line 1; zero with no exception) and the account rule (its h_exc_bad is the project's retirement.wrong_kind) are the project's; like the project's retirement.l2 it includes the capped exceptions, which person.x_l2_all sums. (1) As on retirement.l1, it refuses every entry on the two screens and needs their answers on entries they do not concern (classm.dependent.5.deepseek, completed, code 7: project $0.00, candidate unknown). (2) The candidate-refuses are its early_screen on returns the project refuses on retirement.screen_refused (stage21.refuse.early_screen and its partials): scope. No value differs. Project stands.

### retirement.l2_e05 — Line 2 share under exception 05
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." The exception number is asked only for an early distribution, a code 1 or S entry on line 1 (retirement.has_exception). The candidate tests retirement.exception = e05 on every entry, without that guard, so it needs the exception answer for code 2, 3, 4, 7, G and Q entries, which the source does not ask: classm.dependent.5.deepseek (completed, code 7) project $0.00, candidate unknown. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 1,599 of 2,463 agree; 864 candidate-unknown (35 completed); all of this kind. Its share (retirement.l2 when the exception matches) is the project's. Same as round 2. Project stands.

### retirement.l2_e09 — Line 2 share under exception 09
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." The exception number is asked only for an early distribution, a code 1 or S entry on line 1 (retirement.has_exception). The candidate tests retirement.exception = e09 on every entry, without that guard, so it needs the exception answer for code 2, 3, 4, 7, G and Q entries, which the source does not ask: classm.dependent.5.deepseek (completed, code 7) project $0.00, candidate unknown. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 1,599 of 2,463 agree; 864 candidate-unknown (37 completed); all of this kind. Its share (retirement.l2 when the exception matches) is the project's. Same as round 2. Project stands.

### retirement.l2_e19 — Line 2 share under exception 19
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." The exception number is asked only for an early distribution, a code 1 or S entry on line 1 (retirement.has_exception). The candidate tests retirement.exception = e19 on every entry, without that guard, so it needs the exception answer for code 2, 3, 4, 7, G and Q entries, which the source does not ask: classm.dependent.5.deepseek (completed, code 7) project $0.00, candidate unknown. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 1,598 of 2,463 agree; 865 candidate-unknown (37 completed); all of this kind. Its share (retirement.l2 when the exception matches) is the project's. Same as round 2. Project stands.

### retirement.l2_e22 — Line 2 share under exception 22
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." The exception number is asked only for an early distribution, a code 1 or S entry on line 1 (retirement.has_exception). The candidate tests retirement.exception = e22 on every entry, without that guard, so it needs the exception answer for code 2, 3, 4, 7, G and Q entries, which the source does not ask: classm.dependent.5.deepseek (completed, code 7) project $0.00, candidate unknown. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 1,601 of 2,463 agree; 862 candidate-unknown (35 completed); all of this kind. Its share (retirement.l2 when the exception matches) is the project's. Same as round 2. Project stands.

### retirement.is_e23 — Exception 23
Status: **DISAGREE**

Project:

```json
{"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}
```

Second:

```json
{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}
```

Ruling: representation; p590b p. 28, Emergency personal expense distributions, Distribution limits: "You are limited to taking one emergency personal expense distribution per calendar year"; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 2,463 of 2,463 agree. The candidate now tests a code 1 or S entry (h_early) with exception 23, as retirement.has_exception does, so it no longer needs the exception answer on code 2 and 3 entries (the round-2 difference). Project stands.

### retirement.l2_e23 — Line 2 share under exception 23
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." The exception number is asked only for an early distribution, a code 1 or S entry on line 1 (retirement.has_exception). The candidate tests retirement.exception = e23 on every entry, without that guard, so it needs the exception answer for code 2, 3, 4, 7, G and Q entries, which the source does not ask: classm.dependent.5.deepseek (completed, code 7) project $0.00, candidate unknown. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 1,599 of 2,463 agree; 864 candidate-unknown (35 completed); all of this kind. Its share (retirement.l2 when the exception matches) is the project's. Same as round 2. Project stands.

### retirement.l1_s — Line 1 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error and scope; i5329 p. 5, Line 4: "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%. These distributions are included in boxes 1 and 2a of Form 1099-R and are designated with code S in box 7." The code S share is the project's (line 1 of a code S entry). executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 2,461 of 2,463 agree; 1 project-refuses (none completed), 1 candidate-unknown (none completed). On the partial of classm.retirement.3 that withholds retirement.code_screen the candidate needs that answer on a code S entry (project $11,843.00, candidate unknown), because it refuses line 1 on code_screen, a screen for codes 2, 4 and 7 only; on stage21.refuse.bad_code_screen_unasked the project refuses on the cited retirement.bad_code (scope). Same as rounds 1 and 2. Project stands.

### retirement.l2_s — Line 2 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: model error; i5329 p. 5, Line 4: "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%. These distributions are included in boxes 1 and 2a of Form 1099-R and are designated with code S in box 7." The code S share of line 2 is the project's. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 2,461 of 2,463 agree; 2 candidate-unknown (none completed). Both differences are candidate-unknown on refused returns: it needs retirement.code_screen on a code S entry (partial of classm.retirement.3: project $4,915.00, candidate unknown) and retirement.early_screen on an entry the project refuses on retirement.bad_code (stage21.refuse.bad_code_screen_unasked). Same as rounds 1 and 2. Project stands.

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
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "retirement.age"}, {"const": 60, "type": "Count"}], "test": "le"}, {"args": [{"const": 55, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_310"}}}, {"guard": {"args": [{"args": [{"input": "retirement.age"}, {"const": 65, "type": "Count"}], "test": "le"}, {"args": [{"const": 60, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_260"}}}, {"guard": {"args": [{"args": [{"input": "retirement.age"}, {"const": 70, "type": "Count"}], "test": "le"}, {"args": [{"const": 65, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_210"}}}, {"guard": {"args": [{"input": "retirement.age"}, {"const": 55, "type": "Count"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_360"}}}, {"guard": {"args": [{"const": 70, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_160"}}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"input": "retirement.combined_age"}, {"const": 120, "type": "Count"}], "test": "le"}, {"args": [{"const": 110, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_360"}}}, {"guard": {"args": [{"args": [{"input": "retirement.combined_age"}, {"const": 130, "type": "Count"}], "test": "le"}, {"args": [{"const": 120, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_310"}}}, {"guard": {"args": [{"args": [{"input": "retirement.combined_age"}, {"const": 140, "type": "Count"}], "test": "le"}, {"args": [{"const": 130, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_260"}}}, {"guard": {"args": [{"input": "retirement.combined_age"}, {"const": 110, "type": "Count"}], "test": "le"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_410"}}}, {"guard": {"args": [{"const": 140, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_210"}}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "retirement.used_last_year"}], "test": "eq"}, "then": {"input": "retirement.last_line4"}}], "op": "choose"}
```

Ruling: representation; i1040gi p. 29, Simplified Method Worksheet, line 4: "Divide line 2 by the number on line 3. If you completed this worksheet last year, enter the amount from line 4 of last year’s worksheet", and Tables 1 and 2 ("after November 18, 1996" column: 360, 310, 260, 210, 160; Table 2: 410, 360, 310, 260, 210). Ages are whole numbers, so the candidate's bands equal the project's; the pre-November-19-1996 column is screened by retirement.special and retirement.annuity, as the earlier rulings record. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 2,463 of 2,463 agree. Project stands.

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
| retirement.taxable | retirement.h_rollover_bad, retirement.h_roth_nonq, retirement.special | retirement.h_rollover_bad, retirement.h_roth_nonq |
| retirement.amount_a | retirement.h_rollover_bad, retirement.h_roth_nonq, retirement.special | retirement.h_rollover_bad, retirement.h_roth_nonq |
| retirement.l1 | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_rollover_bad, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_rollover_bad, retirement.h_roth_nonq |
| retirement.l2 | retirement.code_screen, retirement.early_screen, retirement.h_exc_bad, retirement.h_other_code, retirement.h_rollover_bad, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_exc_bad, retirement.h_other_code, retirement.h_rollover_bad, retirement.h_roth_nonq |
| retirement.l2_e05 | retirement.code_screen, retirement.early_screen, retirement.h_exc_bad, retirement.h_other_code, retirement.h_rollover_bad, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_exc_bad, retirement.h_other_code, retirement.h_rollover_bad, retirement.h_roth_nonq |
| retirement.l2_e09 | retirement.code_screen, retirement.early_screen, retirement.h_exc_bad, retirement.h_other_code, retirement.h_rollover_bad, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_exc_bad, retirement.h_other_code, retirement.h_rollover_bad, retirement.h_roth_nonq |
| retirement.l2_e19 | retirement.code_screen, retirement.early_screen, retirement.h_exc_bad, retirement.h_other_code, retirement.h_rollover_bad, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_exc_bad, retirement.h_other_code, retirement.h_rollover_bad, retirement.h_roth_nonq |
| retirement.l2_e22 | retirement.code_screen, retirement.early_screen, retirement.h_exc_bad, retirement.h_other_code, retirement.h_rollover_bad, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_exc_bad, retirement.h_other_code, retirement.h_rollover_bad, retirement.h_roth_nonq |
| retirement.l2_e23 | retirement.code_screen, retirement.early_screen, retirement.h_exc_bad, retirement.h_other_code, retirement.h_rollover_bad, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_exc_bad, retirement.h_other_code, retirement.h_rollover_bad, retirement.h_roth_nonq |
| retirement.l1_s | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_rollover_bad, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_other_code, retirement.h_rollover_bad, retirement.h_roth_nonq |
| retirement.l2_s | retirement.code_screen, retirement.early_screen, retirement.h_exc_bad, retirement.h_other_code, retirement.h_rollover_bad, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_exc_bad, retirement.h_other_code, retirement.h_rollover_bad, retirement.h_roth_nonq |

## Raw second transcription

```yaml
```yaml
lines:
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
    note: "The death benefit exclusion that the worksheet's 'Before you begin' adds to line 2 is screened out by retirement.special. It is not added here."

  - id: retirement.h_t1_360
    printed: "(helper)"
    label: "Line 2 divided by 360 (Table 1, age 55 or under, annuity starting date after November 18, 1996)"
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_360}}
    note: "The worksheet says 'Divide line 2 by the number on line 3' and gives no rounding rule. This line rounds the quotient half-up to the cent."

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
    label: "Line 2 divided by the appropriate number from Table 1 (annuity starting date after November 18, 1996)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [retirement.age, {const: 55, type: Count}]}
          then: retirement.h_t1_360
        - guard: {op: test, all: [{op: test, gt: [retirement.age, {const: 55, type: Count}]}, {op: test, le: [retirement.age, {const: 60, type: Count}]}]}
          then: retirement.h_t1_310
        - guard: {op: test, all: [{op: test, gt: [retirement.age, {const: 60, type: Count}]}, {op: test, le: [retirement.age, {const: 65, type: Count}]}]}
          then: retirement.h_t1_260
        - guard: {op: test, all: [{op: test, gt: [retirement.age, {const: 65, type: Count}]}, {op: test, le: [retirement.age, {const: 70, type: Count}]}]}
          then: retirement.h_t1_210
        - guard: {op: test, gt: [retirement.age, {const: 70, type: Count}]}
          then: retirement.h_t1_160
    note: "Only the 'after November 18, 1996' column of Table 1 is used. The Simplified Method question (retirement.annuity) requires a starting date after November 18, 1996, and earlier dates are screened out by retirement.special."

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
    label: "Line 2 divided by the appropriate number from Table 2"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, le: [retirement.combined_age, {const: 110, type: Count}]}
          then: retirement.h_t2_410
        - guard: {op: test, all: [{op: test, gt: [retirement.combined_age, {const: 110, type: Count}]}, {op: test, le: [retirement.combined_age, {const: 120, type: Count}]}]}
          then: retirement.h_t2_360
        - guard: {op: test, all: [{op: test, gt: [retirement.combined_age, {const: 120, type: Count}]}, {op: test, le: [retirement.combined_age, {const: 130, type: Count}]}]}
          then: retirement.h_t2_310
        - guard: {op: test, all: [{op: test, gt: [retirement.combined_age, {const: 130, type: Count}]}, {op: test, le: [retirement.combined_age, {const: 140, type: Count}]}]}
          then: retirement.h_t2_260
        - guard: {op: test, gt: [retirement.combined_age, {const: 140, type: Count}]}
          then: retirement.h_t2_210

  - id: retirement.h_new4
    printed: "(helper)"
    label: "Line 3 and line 4: the number from Table 1, or Table 2 if the annuity starting date was after 1997 and the payments are for your life and that of your beneficiary; line 2 divided by that number"
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
    label: "Divide line 2 by the number on line 3 (if you completed this worksheet last year, enter the amount from line 4 of last year's worksheet)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.used_last_year, {const: true}]}
          then: retirement.last_line4
        - guard: {op: test, eq: [retirement.used_last_year, {const: false}]}
          then: retirement.h_new4

  - id: retirement.smw5
    printed: "(SMW 5)"
    label: "Multiply line 4 by the number of months for which this year's payments were made"
    type: NonNegDollars
    expr: {op: multiply_count, amount: retirement.smw4, count: retirement.months}
    note: "The branch for an annuity starting date before 1987 (skip lines 6 and 7) is not encoded. The Simplified Method question requires a starting date after November 18, 1996."

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

  - id: retirement.smw8
    printed: "(SMW 8)"
    label: "Enter the smaller of line 5 or line 7"
    type: Dollars
    expr: {op: smaller_of, of: [retirement.smw5, retirement.smw7]}

  - id: retirement.smw9
    printed: "(SMW 9)"
    label: "Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than zero"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.smw1, take: retirement.smw8}

  - id: retirement.smw10
    printed: "(SMW 10)"
    label: "Add lines 6 and 8. This is the amount you have recovered tax free through 2025"
    type: Dollars
    expr: {op: sum, of: [retirement.smw6, retirement.smw8]}
    note: "Line 10 asks whether the annuity starting date was before 1987 (if yes, STOP). That answer is always No in this scope, so the No branch is encoded."

  - id: retirement.smw11
    printed: "(SMW 11)"
    label: "Balance of cost to be recovered. Subtract line 10 from line 2"
    type: Dollars
    expr: {op: subtract, from: retirement.smw2, take: retirement.smw10}

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
    label: "Distribution from an IRA (traditional, SEP, SIMPLE or Roth), reported on lines 4a and 4b"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.account, {const: "traditional_ira"}]}
        - {op: test, eq: [retirement.account, {const: "roth_ira"}]}

  - id: retirement.has_rollover
    printed: "(helper)"
    label: "Part or all of the distribution was rolled over (check box 1 on line 4c or 5c)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, gt: [retirement.rollover, {const: 0}]}
        - {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}

  - id: retirement.h_rollover_bad
    printed: "(gate)"
    label: "The amount rolled over is more than the gross distribution in box 1"
    type: Bool
    expr: {op: test, gt: [retirement.rollover, retirement.box1]}

  - id: retirement.h_ira_taxable
    printed: "(helper)"
    label: "Traditional IRA: the part of the distribution not rolled over (Exception 1), or the total distribution if fully taxable"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.rollover}

  - id: retirement.h_roth_nonq
    printed: "(gate)"
    label: "Roth IRA distribution without code Q: see Form 8606 and its instructions to figure the amount on line 4b"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.account, {const: "roth_ira"}]}
        - {op: test, ne: [retirement.code, {const: "qualified_roth_Q"}]}

  - id: retirement.h_roth_taxable
    printed: "(helper)"
    label: "Roth IRA distribution with code Q: enter -0- on line 4b"
    type: NonNegDollars
    expr: {op: copy, from: retirement.h_zero}
    refuses: [retirement.h_roth_nonq]
    note: "Exception 2(2)(a) (code T with a Roth contribution for 2020 or earlier) cannot be determined from the closed interface. Every Roth distribution without code Q refuses, because it needs Form 8606."

  - id: retirement.h_plan_net
    printed: "(helper)"
    label: "Distribution from Form 1099-R box 1 minus contributions taxable when made (box 5)"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.box5}

  - id: retirement.h_plan_taxable
    printed: "(helper)"
    label: "From that result, subtract the amount of the rollover; enter the remaining amount on line 5b"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_plan_net, take: retirement.rollover}
    note: "The box 5 and rollover subtraction comes from the Rollovers instructions. It is also used for non-annuity plan distributions without a rollover (fully taxable when box 5 is zero). General Rule cases are screened out by retirement.special."

  - id: retirement.taxable
    printed: "(helper)"
    label: "Taxable amount of this distribution (line 4b or line 5b)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.account, {const: "traditional_ira"}]}
          then: retirement.h_ira_taxable
        - guard: {op: test, eq: [retirement.account, {const: "roth_ira"}]}
          then: retirement.h_roth_taxable
        - guard: {op: test, all: [{op: test, eq: [retirement.account, {const: "plan"}]}, {op: test, eq: [retirement.annuity, {const: true}]}]}
          then: retirement.smw9
        - guard: {op: test, all: [{op: test, eq: [retirement.account, {const: "plan"}]}, {op: test, eq: [retirement.annuity, {const: false}]}]}
          then: retirement.h_plan_taxable
    refuses: [retirement.special, {when: retirement.h_rollover_bad, when_known: true}]

  - id: retirement.amount_a
    printed: "(helper)"
    label: "Total distribution entered on line 4a or line 5a (no entry if the distribution is fully taxable)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.taxable, retirement.box1]}
          then: retirement.h_zero
        - guard: {op: test, ne: [retirement.taxable, retirement.box1]}
          then: retirement.box1
    note: "'Fully taxable' is read as the taxable amount equalling box 1. In that case the instructions say to enter the total on line 4b or 5b and make no entry on line 4a or 5a. Otherwise (a rollover, a Roth exception, after-tax cost) the total goes on line 4a or 5a."

  - id: retirement.h_sav_excluded
    printed: "(helper)"
    label: "Distribution excluded from Form 8880 line 4 (military retirement plan, section 404(k) dividends, or inherited IRA as a nonspousal beneficiary)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.sav_military, {const: true}]}
        - {op: test, eq: [retirement.sav_404k, {const: true}]}
        - {op: test, eq: [retirement.sav_inherited, {const: true}]}

  - id: retirement.h_sav_net
    printed: "(helper)"
    label: "Distribution minus the part not taxable as the result of a rollover"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.rollover}

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
    note: "The other Form 8880 exclusions (conversions, in-plan Roth rollovers, excess contributions, returned contributions) are screened out by retirement.special. Loans treated as distributions are not separately identifiable from the interface."

  - id: retirement.h_early
    printed: "(helper)"
    label: "Box 7 code 1 (early distribution, no known exception) or code S (SIMPLE IRA in first 2 years)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.code, {const: "early_1"}]}
        - {op: test, eq: [retirement.code, {const: "simple_S"}]}

  - id: retirement.h_other_code
    printed: "(gate)"
    label: "Taxable distribution with another code or two codes in box 7, whose status as an early distribution cannot be determined"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.code, {const: "other"}]}
        - {op: test, gt: [retirement.taxable, {const: 0}]}

  - id: retirement.l1
    printed: "(helper)"
    label: "Form 5329 line 1: early distributions includible in income"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_early, {const: true}]}
          then: retirement.taxable
        - guard: {op: test, eq: [retirement.h_early, {const: false}]}
          then: retirement.h_zero
    refuses: [retirement.early_screen, retirement.code_screen, retirement.h_other_code]
    note: "Distributions with codes 2 and 3 show an exception that covers the whole distribution (partial coverage is screened out by code_screen), so they are not entered here. Codes 4, 7, G and Q are not early. A taxable distribution coded 'other' refuses, because the text does not let the tool decide whether it is early."

  - id: retirement.h_exc_bad
    printed: "(gate)"
    label: "The exception chosen does not apply to this kind of account (01 and 06 don't apply to IRAs; 07, 08 and 09 are IRA distributions only)"
    type: Bool
    expr:
      op: test
      any:
        - op: test
          all:
            - {op: test, eq: [retirement.is_ira, {const: true}]}
            - {op: test, any: [{op: test, eq: [retirement.exception, {const: "e01"}]}, {op: test, eq: [retirement.exception, {const: "e06"}]}]}
        - op: test
          all:
            - {op: test, eq: [retirement.account, {const: "plan"}]}
            - {op: test, any: [{op: test, eq: [retirement.exception, {const: "e07"}]}, {op: test, eq: [retirement.exception, {const: "e08"}]}, {op: test, eq: [retirement.exception, {const: "e09"}]}]}

  - id: retirement.h_has_exc
    printed: "(helper)"
    label: "An exception to the additional tax applies to this early distribution"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.h_early, {const: true}]}
        - {op: test, ne: [retirement.exception, {const: "none"}]}

  - id: retirement.h_exc_limited
    printed: "(helper)"
    label: "Exception amount, not more than the early distribution included on line 1"
    type: NonNegDollars
    expr: {op: smaller_of, of: [retirement.exc_amount, retirement.l1]}

  - id: retirement.l2
    printed: "(helper)"
    label: "Form 5329 line 2: early distributions not subject to additional tax (amount you can exclude)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.h_has_exc, {const: true}]}
          then: retirement.h_exc_limited
        - guard: {op: test, eq: [retirement.h_has_exc, {const: false}]}
          then: retirement.h_zero
    refuses: [retirement.early_screen, retirement.code_screen, {when: retirement.h_exc_bad, when_known: true}]
    note: "This line covers every exception kind for this distribution, before the per-person dollar limits (05, 09, 19, 22, 23). Those limits are applied at person level from the l2_eNN lines, as the exc_amount question says. The text does not say whether l2 should exclude the capped kinds; including them is the reading chosen."

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
    label: "This early distribution is an eligible emergency expense distribution (exception 23)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.h_early, {const: true}]}
        - {op: test, eq: [retirement.exception, {const: "e23"}]}

  - id: retirement.l2_e23
    printed: "(helper)"
    label: "Line 2 amount under exception 23 (eligible emergency expense distributions)"
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
    label: "Line 1 amount from a SIMPLE IRA received within 2 years of first participating (code S)"
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
    label: "Line 2 amount for a code S SIMPLE IRA distribution"
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
