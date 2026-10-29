# Transcription agreement — retirement

Second transcription of `Form 1099-R distributions (IRAs, pensions and annuities)` by an isolated model (spec 6.5), compared line by line with `forms/2025/retirement.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-29 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
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
| output token budget | 65536 |
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

Ruling: representation; i1040gi p. 26, Lines 4a and 4b, IRA Distributions (the IRA lines take traditional and Roth IRA distributions; the account Enum is traditional_ira, roth_ira or plan). The candidate tests account = traditional_ira or roth_ira; the project tests account ≠ plan, the same set over the three-valued Enum. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 2,463 of 2,463 agree. Same reply text as round 2. Project stands.

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

Ruling: scope; i1040gi p. 27, Exception 1: "Enter the total distribution on line 4a if you rolled over part or all of the distribution ... If the total distribution wasn’t rolled over, enter the part not rolled over on line 4b"; i1040gi p. 30, Rollovers. The candidate's test (code G, or a rollover amount above zero) is the project's. Every difference is the project's: it reads retirement.rolled, which carries the cited refusals retirement.special and retirement.bad_code. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 2,157 of 2,463 agree; 186 project-refuses (none completed), 120 project-unknown (none completed). The project-unknown are partial records that withhold retirement.account, retirement.code or retirement.special, which the interview asks of every entry. No value differs. Same reply text as round 2. Project stands.

### retirement.taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second transcription's note: Within the supported scope, taxable is zero for direct rollovers and qualified Roth distributions; for a plan with a Simplified Method annuity it is SMW9; otherwise it is gross minus rollover (and box 5 for a plan). A nonqualified Roth distribution needs Form 8606 and is refused.

Ruling: model error; i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost ... or (b) you got your entire cost back tax free before 2025 ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a."; i1040gi p. 29, Simplified Method Worksheet, line 4: "Divide line 2 by the number on line 3. If you completed this worksheet last year, enter the amount from line 4 of last year’s worksheet". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 2,249 of 2,463 agree; 14 value (7 completed), 4 candidate-refuses (none completed), 114 project-refuses (none completed), 4 candidate-unknown (none completed), 78 project-unknown (none completed). Code G and code Q entries are zero, and the IRA and plan branches are the project's, except: (1) its Simplified Method line 7 is signed, so when the answers put the amount recovered above the cost its line 8 is negative and line 9 exceeds box 1, where the source makes the payments fully taxable: classm.tcw.15 (completed; cost $0, recovered $9,979, box 1 $39,110) project $39,110.00, candidate $49,089.00; also classm.tcw.14 (refused) $25,703.00 against $51,602.00 and stage10.smw.recovered_exceeds_cost (incomplete) $12,000.00 against $21,000.00. (2) Its (SMW 4) ignores last year's line 4 (see (SMW 4)): classm.f8962.2 (completed) project $35,839.00, candidate $41,992.24. The candidate-refuses are its h_code_other and h_roth_nonq where the project refuses on retirement.bad_code; the project-refuses are the cited retirement.bad_code, retirement.annuity_rollover, retirement.special and retirement.screen_refused: scope. The unknowns are partial records withholding answers asked of every entry or of a worksheet annuity. Project stands.

### retirement.amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}, {"const": 0}], "test": "le"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"args": [{"args": [{"input": "retirement.box5"}, {"const": 0}], "test": "le"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "ne"}], "test": "any"}], "test": "all"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "retirement.box5"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}], "test": "all"}], "test": "any"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": 0}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "test": "lt"}], "test": "any"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "any"}, "then": {"input": "retirement.box1"}}], "op": "choose"}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"input": "retirement.box1"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}, {"input": "retirement.box1"}], "test": "lt"}, "then": {"input": "retirement.box1"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second transcription's note: Entered on line 4a or 5a only when the distribution is not fully taxable; fully taxable distributions go only on 4b or 5b.

Ruling: scope; i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if (a) you didn’t contribute to the cost ... or (b) you got your entire cost back tax free before 2025 ... If your pension or annuity is fully taxable, enter the total pension or annuity payments (from Form(s) 1099-R, box 1) on line 5b; don’t make an entry on line 5a.". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 2,207 of 2,463 agree; 4 candidate-refuses (none completed), 114 project-refuses (none completed), 72 candidate-unknown (none completed), 66 project-unknown (none completed); no completed return differs. The candidate enters box 1 on line 4a/5a only when the taxable amount is below box 1, which on every record triage ran matches the project, including code G entries and the cost-recovered annuity (its taxable amount above box 1 gives no entry); the round-2 error (box 1 on every entry) is gone. The project-refuses are its cited retirement.bad_code, retirement.annuity_rollover, retirement.special and retirement.screen_refused; the candidate-refuses are its h_code_other and h_roth_nonq on refused or incomplete returns; the unknowns are partial records withholding answers asked of every entry (box 1, code, account, annuity, the screens). Project stands.

### retirement.sav_amount — This distribution's amount on Form 8880 line 4
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "ne"}], "test": "any"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "ne"}], "test": "any"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}, {"guard": {"args": [{"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "eq"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "eq"}, {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "ne"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"from": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "retirement.sav_404k"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_inherited"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.sav_military"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second transcription's note: Form 8880 line 4 excludes rollovers and the military, 404(k) and inherited IRA distributions; other exclusions are in retirement.special and are refused.

Ruling: model error; f8880 p. 2, Line 4: "Don’t include any of the following. • Distributions not taxable as the result of a rollover or a trustee-to-trustee transfer ... • Distributions from a military retirement plan (other than the federal TSP). • Distributions from an inherited IRA by a nonspousal beneficiary". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 2,243 of 2,463 agree; 8 candidate-refuses (none completed), 68 project-refuses (none completed), 87 candidate-unknown (23 completed), 57 project-unknown (none completed). The amount (box 1 less the rollover, the whole box 1 on a code G entry) is now the project's; round 2's whole-distribution exclusion is gone. It still applies the military-plan and section 404(k) exclusions to IRA entries and the inherited-IRA exclusion to plan entries, so it needs answers the source does not ask of that kind of account: partial of classm.s2.3.deepseek withholding retirement.sav_military (completed) project $92.00, candidate unknown (the inherited reading is amb.2025.savers_inherited_plans). The project-refuses are its cited retirement.bad_code (scope); the candidate-refuses are its h_code_other on refused returns. Project stands.

### retirement.l1 — Form 5329 line 1 share: the taxable amount of an early distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "normal_7"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second transcription's note: The early amount is the taxable amount for early, SIMPLE, code 2, disability and death codes; normal, rollover and qualified Roth distributions are not early. The screening gates refuse partial code 2, recapture and other unsupported cases.

Ruling: ambiguity and model error; i5329 p. 3, Line 1: "Enter the amount of early distributions includible in income (other than qualified disaster recovery distributions) that you received from:". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 1,292 of 2,463 agree; 194 value (20 completed), 122 candidate-refuses (none completed), 1 project-refuses (none completed), 854 candidate-unknown (42 completed). (1) It puts codes 2, 3 and 4 on line 1: generated 22 (completed; code 4, traditional IRA, box 1 $18,218.60) project $0.00, candidate $18,218.60; ambiguity amb.2025.f5329_line1_codes (owner D8(a): line 1 holds only code 1 and S entries; i5329 p. 3 "includible in income" would on its face take a code 2 distribution too, offset on line 2, so line 3 and the tax are unchanged). The register names code 2; codes 3 and 4 are the same choice, since the code shows the exception and the candidate puts the same amount on line 2 (D2: "exception 03 shown by the code, no tax"). (2) generated 278 (completed; code 1 plan annuity that used the worksheet last year, line 4 then $1,320.33): through the candidate's (SMW 4), which ignores last year's line 4, its taxable amount and line 1 are positive where the project's are $0.00, and its exception 19 share is $2,648.29. (3) It declares retirement.special, retirement.early_screen and retirement.code_screen as refusals of every entry, so it needs screen answers on entries the screens do not concern (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7 (decision D3(a), the cited screens of retirement.screen_refused)): classm.dependent.5.deepseek (completed; code 7) project $0.00, candidate unknown. (4) Its h_code_other and h_roth_nonq refuse where the project refuses on retirement.bad_code; 1 project-refuses on the cited retirement.bad_code (stage21.refuse.bad_code_screen_unasked): scope. Project stands.

### retirement.l2 — Form 5329 line 2 share before the per-person limits
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "normal_7"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "normal_7"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second transcription's note: For codes 2, 3 and 4 the exception is treated as covering the whole early amount; otherwise the exception amount is the smaller of the early amount and exc_amount. Per-person dollar caps are applied later.

Ruling: ambiguity and model error; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 1,232 of 2,463 agree; 194 value (20 completed), 132 candidate-refuses (none completed), 1 project-refuses (none completed), 904 candidate-unknown (48 completed). Round 2's redefinition (zero for the capped exceptions) is gone: the excepted amount is the exception amount capped by line 1, as the project's. (1) For codes 2, 3 and 4 it enters line 1 again (generated 22, completed: $0.00 against $18,218.60), the offset of ambiguity amb.2025.f5329_line1_codes (owner D8(a): line 1 holds only code 1 and S entries; i5329 p. 3 "includible in income" would on its face take a code 2 distribution too, offset on line 2, so line 3 and the tax are unchanged). The register names code 2; codes 3 and 4 are the same choice, since the code shows the exception and the candidate puts the same amount on line 2 (D2: "exception 03 shown by the code, no tax"). (2) Inherited from (SMW 4): generated 278 (completed; code 1 plan annuity that used the worksheet last year, line 4 then $1,320.33): through the candidate's (SMW 4), which ignores last year's line 4, its taxable amount and line 1 are positive where the project's are $0.00, and its exception 19 share is $2,648.29. (3) It tests the exception and declares the screens on every entry, needing answers the source does not ask (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7 (decision D3(a), the cited screens of retirement.screen_refused); classm.dependent.5.deepseek, completed, code 7). (4) It has no account rule; on stage21.refuse.wrong_kind the project refuses on the cited retirement.wrong_kind (i5329 p. 5, "Qualified retirement plan distributions (doesn’t apply to IRAs)"): scope. Project stands.

### retirement.l2_e05 — Line 2 share under exception 05
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "normal_7"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "normal_7"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"const": "e05"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Ruling: model error; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." The exception number is asked only for an early distribution, a code 1 or S entry on line 1 (retirement.has_exception). The candidate tests retirement.exception = e05 on every entry and declares retirement.special, retirement.early_screen and retirement.code_screen as refusals of every entry, so it needs answers the source does not ask: classm.dependent.5.deepseek (completed, code 7) project $0.00, candidate unknown. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 1,406 of 2,463 agree; 132 candidate-refuses (none completed), 925 candidate-unknown (49 completed). The candidate-refuses are on returns the project refuses elsewhere. Its share (its line 2 when the exception matches) is the project's. Project stands.

### retirement.l2_e09 — Line 2 share under exception 09
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "normal_7"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "normal_7"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"const": "e09"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Ruling: model error; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." The exception number is asked only for an early distribution, a code 1 or S entry on line 1 (retirement.has_exception). The candidate tests retirement.exception = e09 on every entry and declares retirement.special, retirement.early_screen and retirement.code_screen as refusals of every entry, so it needs answers the source does not ask: classm.dependent.5.deepseek (completed, code 7) project $0.00, candidate unknown. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 1,406 of 2,463 agree; 132 candidate-refuses (none completed), 925 candidate-unknown (49 completed). The candidate-refuses are on returns the project refuses elsewhere. Its share (its line 2 when the exception matches) is the project's. Project stands.

### retirement.l2_e19 — Line 2 share under exception 19
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "normal_7"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "normal_7"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"const": "e19"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Ruling: model error; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." The exception number is asked only for an early distribution, a code 1 or S entry on line 1 (retirement.has_exception). The candidate tests retirement.exception = e19 on every entry and declares retirement.special, retirement.early_screen and retirement.code_screen as refusals of every entry, so it needs answers the source does not ask: classm.dependent.5.deepseek (completed, code 7) project $0.00, candidate unknown. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 1,409 of 2,463 agree; 1 value (1 completed), 132 candidate-refuses (none completed), 921 candidate-unknown (49 completed). The candidate-refuses are on returns the project refuses elsewhere. Its share (its line 2 when the exception matches) is the project's. One completed value difference is inherited from (SMW 4): generated 278 (completed; code 1 plan annuity that used the worksheet last year, line 4 then $1,320.33): through the candidate's (SMW 4), which ignores last year's line 4, its taxable amount and line 1 are positive where the project's are $0.00, and its exception 19 share is $2,648.29 (project $0.00). Project stands.

### retirement.l2_e22 — Line 2 share under exception 22
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "normal_7"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "normal_7"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"const": "e22"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Ruling: model error; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." The exception number is asked only for an early distribution, a code 1 or S entry on line 1 (retirement.has_exception). The candidate tests retirement.exception = e22 on every entry and declares retirement.special, retirement.early_screen and retirement.code_screen as refusals of every entry, so it needs answers the source does not ask: classm.dependent.5.deepseek (completed, code 7) project $0.00, candidate unknown. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 1,398 of 2,463 agree; 132 candidate-refuses (none completed), 933 candidate-unknown (49 completed). The candidate-refuses are on returns the project refuses elsewhere. Its share (its line 2 when the exception matches) is the project's. Project stands.

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

Ruling: model error; p590b p. 28, Emergency personal expense distributions, Distribution limits: "You are limited to taking one emergency personal expense distribution per calendar year"; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." The candidate tests retirement.exception = e23 on every entry, so it needs the exception answer on entries it is not asked of: classm.dependent.5.deepseek (completed, code 7) project false, candidate unknown. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 1,599 of 2,463 agree; 862 candidate-unknown (35 completed), 2 project-unknown (none completed); the project-unknown are partial records withholding retirement.code, asked of every entry. No value differs. Same reply text as round 2. Project stands.

### retirement.l2_e23 — Line 2 share under exception 23
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "normal_7"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "normal_7"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"const": "e23"}, {"input": "retirement.exception"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Ruling: model error; i5329 p. 5, Line 2: "Enter on line 2 the amount that you can exclude. In the space provided, enter the applicable exception number (01–23). If more than one exception applies, enter 99." The exception number is asked only for an early distribution, a code 1 or S entry on line 1 (retirement.has_exception). The candidate tests retirement.exception = e23 on every entry and declares retirement.special, retirement.early_screen and retirement.code_screen as refusals of every entry, so it needs answers the source does not ask: classm.dependent.5.deepseek (completed, code 7) project $0.00, candidate unknown. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 1,406 of 2,463 agree; 132 candidate-refuses (none completed), 925 candidate-unknown (49 completed). The candidate-refuses are on returns the project refuses elsewhere. Its share (its line 2 when the exception matches) is the project's. Project stands.

### retirement.l1_s — Line 1 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "normal_7"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Ruling: model error and scope; i5329 p. 5, Line 4: "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%. These distributions are included in boxes 1 and 2a of Form 1099-R and are designated with code S in box 7." The code S share is the project's, but the candidate declares retirement.special, retirement.early_screen and retirement.code_screen as refusals of every entry, so it needs screen answers on entries they do not concern (retirement.early_screen is asked only for code 1 and S entries and retirement.code_screen only for codes 2, 4 and 7 (decision D3(a), the cited screens of retirement.screen_refused); classm.dependent.5.deepseek, code 7, completed). executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 1,457 of 2,463 agree; 132 candidate-refuses (none completed), 1 project-refuses (none completed), 873 candidate-unknown (42 completed). The candidate-refuses are on returns the project refuses elsewhere; 1 project-refuses on the cited retirement.bad_code (stage21.refuse.bad_code_screen_unasked): scope. No value differs. Project stands.

### retirement.l2_s — Line 2 share from a code S distribution
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"alternatives": [{"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"of": [{"input": "retirement.box5"}, {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}], "op": "sum"}}}, {"guard": {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"line": "(SMW 7)"}, {"const": 0}], "test": "le"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": 0}, {"line": "(SMW 7)"}], "test": "lt"}, "then": {"line": "(SMW 9)"}}], "op": "choose"}}], "op": "choose"}}, {"guard": {"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"alternatives": [{"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "ne"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"alternatives": [{"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"input": "retirement.box1"}}, {"guard": {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"input": "retirement.rollover"}}], "op": "choose"}}}], "op": "choose"}}], "op": "choose"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"from": {"alternatives": [{"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "eq"}, {"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "none"}, {"input": "retirement.exception"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "retirement.exc_amount"}, {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "normal_7"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "death_4"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "disability_3"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_1"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "early_exception_2"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": false}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"from": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.box5"}}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}, {"guard": {"args": [{"args": [{"const": "plan"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": true}, {"input": "retirement.annuity"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, "then": {"line": "(SMW 9)"}}, {"guard": {"args": [{"args": [{"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}], "test": "all"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"args": [{"const": "roth_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}, {"args": [{"args": [{"const": "traditional_ira"}, {"input": "retirement.account"}], "test": "eq"}, {"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "ne"}], "test": "all"}], "test": "any"}, "then": {"from": {"input": "retirement.box1"}, "op": "subtract_floor0", "take": {"input": "retirement.rollover"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"args": [{"const": "direct_rollover_G"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "normal_7"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "other"}, {"input": "retirement.code"}], "test": "eq"}, {"args": [{"const": "qualified_roth_Q"}, {"input": "retirement.code"}], "test": "eq"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}}, {"guard": {"args": [{"const": "simple_S"}, {"input": "retirement.code"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Ruling: model error; i5329 p. 5, Line 4: "If any amount on line 3 was a distribution from a SIMPLE IRA received within 2 years from the date you first participated in the SIMPLE IRA plan, you must multiply that amount by 25% instead of 10%. These distributions are included in boxes 1 and 2a of Form 1099-R and are designated with code S in box 7." The code S share of line 2 is the project's on every computed entry, but the candidate needs the screen answers on every entry, as on retirement.l1_s. executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 1,457 of 2,463 agree; 132 candidate-refuses (none completed), 874 candidate-unknown (42 completed). No value differs. Project stands.

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
{"from": {"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": 70, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_160"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 110, "type": "Count"}], "test": "le"}], "test": "all"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table2_410"}}}, {"guard": {"args": [{"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.age"}, {"const": 55, "type": "Count"}], "test": "le"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 120, "type": "Count"}], "test": "le"}, {"args": [{"const": 110, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}], "test": "any"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_360"}}}, {"guard": {"args": [{"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.age"}, {"const": 60, "type": "Count"}], "test": "le"}, {"args": [{"const": 55, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 130, "type": "Count"}], "test": "le"}, {"args": [{"const": 120, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}], "test": "any"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_310"}}}, {"guard": {"args": [{"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.age"}, {"const": 65, "type": "Count"}], "test": "le"}, {"args": [{"const": 60, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.combined_age"}, {"const": 140, "type": "Count"}], "test": "le"}, {"args": [{"const": 130, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}], "test": "any"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_260"}}}, {"guard": {"args": [{"args": [{"args": [{"const": false}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"input": "retirement.age"}, {"const": 70, "type": "Count"}], "test": "le"}, {"args": [{"const": 65, "type": "Count"}, {"input": "retirement.age"}], "test": "lt"}], "test": "all"}, {"args": [{"args": [{"const": true}, {"input": "retirement.joint_life"}], "test": "eq"}, {"args": [{"const": 140, "type": "Count"}, {"input": "retirement.combined_age"}], "test": "lt"}], "test": "all"}], "test": "any"}, "then": {"amount": {"line": "(SMW 2)"}, "op": "multiply_rate", "rate": {"param": "smw.table1_210"}}}], "op": "choose"}, "op": "subtract_floor0", "take": {"const": 0}}
```

Second transcription's note: The worksheet's line 3 has a pre-November 19, 1996 column; the retirement.annuity input limits this slice to annuities with an annuity starting date after November 18, 1996, so only that column is used.

Ruling: model error; i1040gi p. 29, Simplified Method Worksheet, line 4: "Divide line 2 by the number on line 3. If you completed this worksheet last year, enter the amount from line 4 of last year’s worksheet". executable-triage-v2 (`reviews/2025/transcription/triage/retirement.deepseek.json`; 1,373 fixtures, 500 generated returns seed 20261026, 1,118 partial records from 40 bases; 2,463 comparisons): 2,283 of 2,463 agree; 58 value (6 completed), 58 candidate-unknown (15 completed), 64 project-unknown (14 completed). The candidate always divides line 2 by the table number and has no branch for last year's line 4 (its note covers only the pre-November-19-1996 column): classm.f8962.2 (completed; retirement.used_last_year true, last year's line 4 $690.00) project $690.00, candidate $177.23; classm.retirement.1 (refused) $892.00 against $15.31. Its project-unknown are partial records withholding retirement.used_last_year or retirement.last_line4, which the source asks; its candidate-unknown are partial records withholding cost, joint_life or age where the project takes last year's line 4 and the source does not need them. The table bands are the project's. Project stands.

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
| retirement.taxable | retirement.h_code_other, retirement.h_roth_nonq, retirement.special | retirement.h_code_other, retirement.h_roth_nonq |
| retirement.amount_a | retirement.h_code_other, retirement.h_roth_nonq, retirement.special | retirement.h_code_other, retirement.h_roth_nonq |
| retirement.sav_amount | retirement.h_code_other, retirement.special | retirement.h_code_other |
| retirement.l1 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_nonq |
| retirement.l2 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_nonq |
| retirement.l2_e05 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_nonq |
| retirement.l2_e09 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_nonq |
| retirement.l2_e19 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_nonq |
| retirement.l2_e22 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_nonq |
| retirement.l2_e23 | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_nonq |
| retirement.l1_s | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_nonq |
| retirement.l2_s | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_nonq, retirement.special | retirement.code_screen, retirement.early_screen, retirement.h_code_other, retirement.h_roth_nonq |

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
    expr: {op: subtract_floor0, from: retirement.h_smw4_raw, take: {const: 0}}
    note: "The worksheet's line 3 has a pre-November 19, 1996 column; the retirement.annuity input limits this slice to annuities with an annuity starting date after November 18, 1996, so only that column is used."

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
    note: "The worksheet says STOP if the annuity starting date was before 1987; the retirement.annuity input limits this slice to after November 18, 1996, so line 10 is computed."

  - id: retirement.smw11
    printed: "(SMW 11)"
    label: "Balance of cost to be recovered. Subtract line 10 from line 2. If zero, you won't have to complete this worksheet next year. The payments you receive next year will generally be fully taxable."
    type: Dollars
    expr: {op: subtract, from: retirement.smw2, take: retirement.smw10}

  - id: retirement.one
    printed: "(helper)"
    label: "One distribution."
    type: Count
    expr: {op: param, ref: person.one}

  - id: retirement.is_ira
    printed: "(helper)"
    label: "Distribution is from an IRA (traditional or Roth)."
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.account, {const: "traditional_ira"}]}
        - {op: test, eq: [retirement.account, {const: "roth_ira"}]}

  - id: retirement.has_rollover
    printed: "(helper)"
    label: "Distribution was rolled over (code G direct rollover or a rollover amount)."
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
        - {op: test, gt: [retirement.rollover, {const: 0}]}

  - id: retirement.taxable
    printed: "(helper)"
    label: "Taxable amount of this distribution."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_taxable_raw, take: {const: 0}}
    refuses: [retirement.h_code_other, retirement.h_roth_nonq, retirement.special]
    note: "Within the supported scope, taxable is zero for direct rollovers and qualified Roth distributions; for a plan with a Simplified Method annuity it is SMW9; otherwise it is gross minus rollover (and box 5 for a plan). A nonqualified Roth distribution needs Form 8606 and is refused."

  - id: retirement.amount_a
    printed: "(helper)"
    label: "Amount to report on Form 1040 line 4a or 5a for this distribution."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_amount_a_raw, take: {const: 0}}
    refuses: [retirement.h_code_other, retirement.h_roth_nonq, retirement.special]
    note: "Entered on line 4a or 5a only when the distribution is not fully taxable; fully taxable distributions go only on 4b or 5b."

  - id: retirement.sav_amount
    printed: "(helper)"
    label: "Distribution amount to include on Form 8880, line 4."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_sav_amount_raw, take: {const: 0}}
    refuses: [retirement.h_code_other, retirement.special]
    note: "Form 8880 line 4 excludes rollovers and the military, 404(k) and inherited IRA distributions; other exclusions are in retirement.special and are refused."

  - id: retirement.l1
    printed: "(helper)"
    label: "Early distribution includible in income for Form 5329, line 1."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_l1_raw, take: {const: 0}}
    refuses: [retirement.h_code_other, retirement.h_roth_nonq, retirement.early_screen, retirement.code_screen, retirement.special]
    note: "The early amount is the taxable amount for early, SIMPLE, code 2, disability and death codes; normal, rollover and qualified Roth distributions are not early. The screening gates refuse partial code 2, recapture and other unsupported cases."

  - id: retirement.l2
    printed: "(helper)"
    label: "Early distribution not subject to additional tax for Form 5329, line 2."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_l2_raw, take: {const: 0}}
    refuses: [retirement.h_code_other, retirement.h_roth_nonq, retirement.early_screen, retirement.code_screen, retirement.special]
    note: "For codes 2, 3 and 4 the exception is treated as covering the whole early amount; otherwise the exception amount is the smaller of the early amount and exc_amount. Per-person dollar caps are applied later."

  - id: retirement.l2_e05
    printed: "(helper)"
    label: "Exception 05 (medical expenses) amount included in Form 5329 line 2."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_l2_e05_raw, take: {const: 0}}
    refuses: [retirement.h_code_other, retirement.h_roth_nonq, retirement.early_screen, retirement.code_screen, retirement.special]

  - id: retirement.l2_e09
    printed: "(helper)"
    label: "Exception 09 (first home) amount included in Form 5329 line 2."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_l2_e09_raw, take: {const: 0}}
    refuses: [retirement.h_code_other, retirement.h_roth_nonq, retirement.early_screen, retirement.code_screen, retirement.special]

  - id: retirement.l2_e19
    printed: "(helper)"
    label: "Exception 19 (birth or adoption) amount included in Form 5329 line 2."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_l2_e19_raw, take: {const: 0}}
    refuses: [retirement.h_code_other, retirement.h_roth_nonq, retirement.early_screen, retirement.code_screen, retirement.special]

  - id: retirement.l2_e22
    printed: "(helper)"
    label: "Exception 22 (domestic abuse) amount included in Form 5329 line 2."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_l2_e22_raw, take: {const: 0}}
    refuses: [retirement.h_code_other, retirement.h_roth_nonq, retirement.early_screen, retirement.code_screen, retirement.special]

  - id: retirement.is_e23
    printed: "(helper)"
    label: "Exception 23 (emergency personal expense) applies."
    type: Bool
    expr: {op: test, eq: [retirement.exception, {const: "e23"}]}

  - id: retirement.l2_e23
    printed: "(helper)"
    label: "Exception 23 (emergency personal expense) amount included in Form 5329 line 2."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_l2_e23_raw, take: {const: 0}}
    refuses: [retirement.h_code_other, retirement.h_roth_nonq, retirement.early_screen, retirement.code_screen, retirement.special]

  - id: retirement.l1_s
    printed: "(helper)"
    label: "SIMPLE IRA early distribution included in Form 5329 line 1."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_l1_s_raw, take: {const: 0}}
    refuses: [retirement.h_code_other, retirement.h_roth_nonq, retirement.early_screen, retirement.code_screen, retirement.special]

  - id: retirement.l2_s
    printed: "(helper)"
    label: "SIMPLE IRA exception amount included in Form 5329 line 2."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_l2_s_raw, take: {const: 0}}
    refuses: [retirement.h_code_other, retirement.h_roth_nonq, retirement.early_screen, retirement.code_screen, retirement.special]

  - id: retirement.h_zero
    printed: "(helper)"
    label: "Zero."
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}

  - id: retirement.h_code_other
    printed: "(helper)"
    label: "Distribution code is other."
    type: Bool
    expr: {op: test, eq: [retirement.code, {const: "other"}]}

  - id: retirement.h_roth_nonq
    printed: "(helper)"
    label: "Nonqualified Roth IRA distribution."
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [retirement.account, {const: "roth_ira"}]}
        - {op: test, ne: [retirement.code, {const: "qualified_roth_Q"}]}
        - {op: test, ne: [retirement.code, {const: "direct_rollover_G"}]}

  - id: retirement.h_smw4_410
    printed: "(helper)"
    label: "Line 2 times 1/410."
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table2_410}}

  - id: retirement.h_smw4_360
    printed: "(helper)"
    label: "Line 2 times 1/360."
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_360}}

  - id: retirement.h_smw4_310
    printed: "(helper)"
    label: "Line 2 times 1/310."
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_310}}

  - id: retirement.h_smw4_260
    printed: "(helper)"
    label: "Line 2 times 1/260."
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_260}}

  - id: retirement.h_smw4_210
    printed: "(helper)"
    label: "Line 2 times 1/210."
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_210}}

  - id: retirement.h_smw4_160
    printed: "(helper)"
    label: "Line 2 times 1/160."
    type: NonNegDollars
    expr: {op: multiply_rate, amount: retirement.smw2, rate: {param: smw.table1_160}}

  - id: retirement.h_smw4_raw
    printed: "(helper)"
    label: "Line 4 before the zero floor."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, all: [{op: test, eq: [retirement.joint_life, {const: true}]}, {op: test, le: [retirement.combined_age, {const: 110, type: Count}]}]}
          then: retirement.h_smw4_410
        - guard: {op: test, all: [{op: test, eq: [retirement.joint_life, {const: true}]}, {op: test, gt: [retirement.combined_age, {const: 110, type: Count}]}, {op: test, le: [retirement.combined_age, {const: 120, type: Count}]}]}
          then: retirement.h_smw4_360
        - guard: {op: test, all: [{op: test, eq: [retirement.joint_life, {const: true}]}, {op: test, gt: [retirement.combined_age, {const: 120, type: Count}]}, {op: test, le: [retirement.combined_age, {const: 130, type: Count}]}]}
          then: retirement.h_smw4_310
        - guard: {op: test, all: [{op: test, eq: [retirement.joint_life, {const: true}]}, {op: test, gt: [retirement.combined_age, {const: 130, type: Count}]}, {op: test, le: [retirement.combined_age, {const: 140, type: Count}]}]}
          then: retirement.h_smw4_260
        - guard: {op: test, all: [{op: test, eq: [retirement.joint_life, {const: true}]}, {op: test, gt: [retirement.combined_age, {const: 140, type: Count}]}]}
          then: retirement.h_smw4_210
        - guard: {op: test, all: [{op: test, eq: [retirement.joint_life, {const: false}]}, {op: test, le: [retirement.age, {const: 55, type: Count}]}]}
          then: retirement.h_smw4_360
        - guard: {op: test, all: [{op: test, eq: [retirement.joint_life, {const: false}]}, {op: test, gt: [retirement.age, {const: 55, type: Count}]}, {op: test, le: [retirement.age, {const: 60, type: Count}]}]}
          then: retirement.h_smw4_310
        - guard: {op: test, all: [{op: test, eq: [retirement.joint_life, {const: false}]}, {op: test, gt: [retirement.age, {const: 60, type: Count}]}, {op: test, le: [retirement.age, {const: 65, type: Count}]}]}
          then: retirement.h_smw4_260
        - guard: {op: test, all: [{op: test, eq: [retirement.joint_life, {const: false}]}, {op: test, gt: [retirement.age, {const: 65, type: Count}]}, {op: test, le: [retirement.age, {const: 70, type: Count}]}]}
          then: retirement.h_smw4_210
        - guard: {op: test, all: [{op: test, eq: [retirement.joint_life, {const: false}]}, {op: test, gt: [retirement.age, {const: 70, type: Count}]}]}
          then: retirement.h_smw4_160

  - id: retirement.h_plan_net5
    printed: "(helper)"
    label: "Plan gross distribution less box 5."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.box5}

  - id: retirement.h_plan_taxable
    printed: "(helper)"
    label: "Plan taxable amount after box 5 and rollover."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_plan_net5, take: retirement.rollover}

  - id: retirement.h_ira_taxable
    printed: "(helper)"
    label: "IRA taxable amount after rollover."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.rollover}

  - id: retirement.h_taxable_raw
    printed: "(helper)"
    label: "Taxable amount before the zero floor."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
          then: retirement.h_zero
        - guard: {op: test, all: [{op: test, eq: [retirement.account, {const: "roth_ira"}]}, {op: test, eq: [retirement.code, {const: "qualified_roth_Q"}]}]}
          then: retirement.h_zero
        - guard: {op: test, all: [{op: test, eq: [retirement.account, {const: "plan"}]}, {op: test, eq: [retirement.annuity, {const: true}]}, {op: test, ne: [retirement.code, {const: "direct_rollover_G"}]}]}
          then: retirement.smw9
        - guard: {op: test, all: [{op: test, eq: [retirement.account, {const: "plan"}]}, {op: test, eq: [retirement.annuity, {const: false}]}, {op: test, ne: [retirement.code, {const: "direct_rollover_G"}]}]}
          then: retirement.h_plan_taxable
        - guard: {op: test, all: [{op: test, eq: [retirement.account, {const: "roth_ira"}]}, {op: test, ne: [retirement.code, {const: "qualified_roth_Q"}]}, {op: test, ne: [retirement.code, {const: "direct_rollover_G"}]}]}
          then: retirement.h_ira_taxable
        - guard: {op: test, all: [{op: test, eq: [retirement.account, {const: "traditional_ira"}]}, {op: test, ne: [retirement.code, {const: "direct_rollover_G"}]}]}
          then: retirement.h_ira_taxable

  - id: retirement.h_amount_a_raw
    printed: "(helper)"
    label: "Line 4a/5a amount before the zero floor."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, lt: [retirement.taxable, retirement.box1]}
          then: retirement.box1
        - guard: {op: test, ge: [retirement.taxable, retirement.box1]}
          then: retirement.h_zero

  - id: retirement.h_rollover_effective_raw
    printed: "(helper)"
    label: "Rollover amount, treating code G as the whole distribution."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
          then: retirement.box1
        - guard: {op: test, ne: [retirement.code, {const: "direct_rollover_G"}]}
          then: retirement.rollover

  - id: retirement.h_rollover_effective
    printed: "(helper)"
    label: "Rollover amount with a zero floor."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.h_rollover_effective_raw, take: {const: 0}}

  - id: retirement.h_sav_gross
    printed: "(helper)"
    label: "Distribution remaining after rollover for Form 8880 line 4."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: retirement.box1, take: retirement.h_rollover_effective}

  - id: retirement.h_sav_amount_raw
    printed: "(helper)"
    label: "Form 8880 line 4 amount before the zero floor."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, any: [{op: test, eq: [retirement.sav_military, {const: true}]}, {op: test, eq: [retirement.sav_404k, {const: true}]}, {op: test, eq: [retirement.sav_inherited, {const: true}]}]}
          then: retirement.h_zero
        - guard: {op: test, not: {op: test, any: [{op: test, eq: [retirement.sav_military, {const: true}]}, {op: test, eq: [retirement.sav_404k, {const: true}]}, {op: test, eq: [retirement.sav_inherited, {const: true}]}]}}
          then: retirement.h_sav_gross

  - id: retirement.h_l1_raw
    printed: "(helper)"
    label: "Form 5329 line 1 amount before the zero floor."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "normal_7"}]}
          then: retirement.h_zero
        - guard: {op: test, eq: [retirement.code, {const: "direct_rollover_G"}]}
          then: retirement.h_zero
        - guard: {op: test, eq: [retirement.code, {const: "qualified_roth_Q"}]}
          then: retirement.h_zero
        - guard: {op: test, eq: [retirement.code, {const: "other"}]}
          then: retirement.h_zero
        - guard: {op: test, eq: [retirement.code, {const: "early_1"}]}
          then: retirement.taxable
        - guard: {op: test, eq: [retirement.code, {const: "simple_S"}]}
          then: retirement.taxable
        - guard: {op: test, eq: [retirement.code, {const: "early_exception_2"}]}
          then: retirement.taxable
        - guard: {op: test, eq: [retirement.code, {const: "disability_3"}]}
          then: retirement.taxable
        - guard: {op: test, eq: [retirement.code, {const: "death_4"}]}
          then: retirement.taxable

  - id: retirement.h_l2_exc
    printed: "(helper)"
    label: "Exception amount capped at the early amount."
    type: NonNegDollars
    expr: {op: smaller_of, of: [retirement.l1, retirement.exc_amount]}

  - id: retirement.h_l2_raw
    printed: "(helper)"
    label: "Form 5329 line 2 amount before the zero floor."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "death_4"}]}
          then: retirement.l1
        - guard: {op: test, eq: [retirement.code, {const: "disability_3"}]}
          then: retirement.l1
        - guard: {op: test, eq: [retirement.code, {const: "early_exception_2"}]}
          then: retirement.l1
        - guard: {op: test, all: [{op: test, ne: [retirement.exception, {const: "none"}]}, {op: test, ne: [retirement.code, {const: "death_4"}]}, {op: test, ne: [retirement.code, {const: "disability_3"}]}, {op: test, ne: [retirement.code, {const: "early_exception_2"}]}]}
          then: retirement.h_l2_exc
        - guard: {op: test, all: [{op: test, eq: [retirement.exception, {const: "none"}]}, {op: test, ne: [retirement.code, {const: "death_4"}]}, {op: test, ne: [retirement.code, {const: "disability_3"}]}, {op: test, ne: [retirement.code, {const: "early_exception_2"}]}]}
          then: retirement.h_zero

  - id: retirement.h_l2_e05_raw
    printed: "(helper)"
    label: "Exception 05 amount before the zero floor."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e05"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e05"}]}
          then: retirement.h_zero

  - id: retirement.h_l2_e09_raw
    printed: "(helper)"
    label: "Exception 09 amount before the zero floor."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e09"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e09"}]}
          then: retirement.h_zero

  - id: retirement.h_l2_e19_raw
    printed: "(helper)"
    label: "Exception 19 amount before the zero floor."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e19"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e19"}]}
          then: retirement.h_zero

  - id: retirement.h_l2_e22_raw
    printed: "(helper)"
    label: "Exception 22 amount before the zero floor."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e22"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e22"}]}
          then: retirement.h_zero

  - id: retirement.h_l2_e23_raw
    printed: "(helper)"
    label: "Exception 23 amount before the zero floor."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.exception, {const: "e23"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.exception, {const: "e23"}]}
          then: retirement.h_zero

  - id: retirement.h_l1_s_raw
    printed: "(helper)"
    label: "SIMPLE IRA early amount before the zero floor."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "simple_S"}]}
          then: retirement.l1
        - guard: {op: test, ne: [retirement.code, {const: "simple_S"}]}
          then: retirement.h_zero

  - id: retirement.h_l2_s_raw
    printed: "(helper)"
    label: "SIMPLE IRA exception amount before the zero floor."
    type: Dollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [retirement.code, {const: "simple_S"}]}
          then: retirement.l2
        - guard: {op: test, ne: [retirement.code, {const: "simple_S"}]}
          then: retirement.h_zero
```
