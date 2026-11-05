# Transcription agreement — refund

Second transcription of `State and Local Income Tax Refund Worksheet—Schedule 1, Line 1` by an isolated model (spec 6.5), compared line by line with `forms/2025/refund.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt sha256 | 735433445969b66293c212c466b4bc7a9e2c1883ef614e1c579a8834e8001d1f |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | c3e68d2892e11f98022a0c84d9040f28175f4e7d0b28d24d24ed65e0e03c7392 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | e9a5368e306d5d9fbca1b6412dc1183b49c04df4f171cae4524a87e24b6b63bf |
| printed lines compared | 11 |
| agree / disagree / missing | 7 / 4 / 0 |
| extra printed lines in second | none |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 33, 88, 89, 90 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 88, 89 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1099g | Rev. March 2024 (continuous-use form for calendar year 2025; the December 2026 revision is first used for 2026) | 1, 2, 3, 4, 5, 6 | whole document | c3505294585e00ec5e957f73aa97dee32ad4b6916cd3eb48fef7f3c79f123270 | 5 | 49cc781de5cf6d881cc347361880de4b4b20fca0f13397bc94c94e84a20cff6d |
| i1040sca | 2025; printed date 2025-12-08 | 7 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | - | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| p525 | 2025 | 24 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 24 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

## Lines

### refund.has — Any state or local income tax refund received in 2025
Status: **AGREE**

### refund.taxable — Taxable part of your refund (zero when you did not itemize for 2024 or deducted general sa
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "refund.sales"}], "test": "eq"}, {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "eq"}], "test": "all"}, "then": {"line": "9"}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "refund.sales"}], "test": "ne"}, {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "refund.sales"}], "test": "eq"}, {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "eq"}, {"args": [{"const": 0}, {"input": "refund.received"}], "test": "lt"}], "test": "all"}, "then": {"line": "9"}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "refund.itemized"}], "test": "eq"}, {"args": [{"const": true}, {"input": "refund.sales"}], "test": "eq"}, {"args": [{"input": "refund.received"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: Read as the Schedule 1 line 1 amount. The TIP says none of the refund is taxable if, in the year you paid the tax, you didn't itemize or you elected to deduct general sales taxes. Otherwise the amount is line 9 of the worksheet. A refund of a tax on trade or business income only (box 8) is reported on Schedule C, not here, so it is refused.

Ruling: model error and scope; inherited from the candidate's lines 6 and 9. i1040gi p. 88, Line 1, TIP: "None of your refund is taxable if, in the year you paid the tax, you either (a) didn’t itemize deductions, or (b) elected to deduct state and local general sales taxes instead of state and local income taxes". The candidate's own choice (zero without a refund, zero when the 2024 tax was not deducted on Schedule A, line 9 otherwise) is the project's choice on refund.worksheet, with the box 8 and other-year gates (refund.not_2024, whose PENDING-5 wording adds tax paid "before 2024") met on every refund on both sides. On refund returns the differences are: stage16.mut.refund_single_unasked (single 2024 status; project $1,400.00, candidate unknown for refund.spouse_born) and stage16.mut.refund_line3_stop (line 3 STOP; project $0.00, candidate unknown for refund.status), inherited from lines 6 and 9 (model error there); and stage16.refuse.refund.line5e_bad (project refuses at the cited impossible-entry screen refund.line5e_bad, candidate $3,000.00): scope. The completed-return project-unknown (partials withholding refund.not_2024 or refund.itemized) are on bases with no refund: Every partial base of the bank is a return with no refund (refund.received $0.00), and s1.line1 reads the worksheet only when refund.has (refund.received more than zero) is true (forms/2025/s1.yaml), so the partial-record differences on those bases are on lines the return never reads. Triage executable-triage-v2 (`reviews/2025/transcription/triage/refund.json`; 1,495 fixtures, 500 generated returns seed 20261026, 640 partial records from 40 bases; 2,635 comparisons): 2,552 agree; differences 2 candidate-unknown, 1 project-refuses, 80 project-unknown; on completed returns 44 project-unknown; every completed-return witness enumerated by an uncapped scratch rerun of the same evaluator (the record keeps 6 per kind). Project stands.

### 1 — Enter the income tax refund from Form(s) 1099-G (or similar statement). But don’t enter mo
Status: **AGREE**

### 2 — Subtract the amount on your 2024 Schedule A, line 5e, from the amount of state and local i
Status: **AGREE**

### 3 — Subtract line 2 from line 1
Status: **AGREE**

### 4 — Enter your total itemized deductions from your 2024 Schedule A, line 17
Status: **AGREE**

### 5 — Enter the amount shown below for the filing status claimed on your 2024 Form 1040 or 1040-
Status: **AGREE**

### 6 — Check any boxes that apply. Multiply the number of boxes checked by $1,550 ($1,950 if your
Status: **DISAGREE**

Project:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.spouse_blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.spouse_blind"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "ne"}], "test": "all"}, "then": {"const": 0}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.spouse_born"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.spouse_born"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.you_blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.you_blind"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.you_born"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.you_born"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}], "op": "choose"}], "op": "sum"}
```

Second:

```json
{"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.spouse_blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.spouse_blind"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "ne"}], "test": "all"}, "then": {"param": "refund.box_married"}}, {"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.spouse_born"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.spouse_born"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "ne"}], "test": "all"}, "then": {"param": "refund.box_married"}}, {"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.you_blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.you_blind"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "ne"}], "test": "all"}, "then": {"param": "refund.box_married"}}, {"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.you_born"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.you_born"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "ne"}], "test": "all"}, "then": {"param": "refund.box_married"}}, {"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}], "op": "choose"}}], "op": "choose"}], "op": "sum"}
```

Second transcription's note: The count of boxes times the per-box amount is written as the sum of the per-box amount for each checked box, which is the same value.

Ruling: model error; i1040gi p. 90, worksheet line 6: "Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)" and its footnote "*If your filing status is married filing separately, you can check the boxes for your spouse only if your spouse had no income, isn’t filing a return, and can’t be claimed as a dependent on another person’s return"; p. 33, Line 12d: "Don’t check any boxes for your spouse if your filing status is head of household". The candidate takes the spouse boxes for every 2024 filing status; the project counts them only for married filing jointly or separately, and zeroes them for single, head of household and qualifying surviving spouse (amb.2025.refund_boxes_2024). The candidate therefore needs the spouse answers where the source does not: stage16.mut.refund_single_unasked (single, a refund, the spouse questions unasked) gives the project $0.00 and the candidate unknown for refund.spouse_born. No value differs on any record. The completed-return candidate-unknown (spouse boxes withheld) and project-unknown (refund.status withheld where the candidate's answers are No) are partial records on bases with no refund: Every partial base of the bank is a return with no refund (refund.received $0.00), and s1.line1 reads the worksheet only when refund.has (refund.received more than zero) is true (forms/2025/s1.yaml), so the partial-record differences on those bases are on lines the return never reads. Triage executable-triage-v2 (`reviews/2025/transcription/triage/refund.json`; 1,495 fixtures, 500 generated returns seed 20261026, 640 partial records from 40 bases; 2,635 comparisons): 2,514 agree; differences 81 candidate-unknown, 40 project-unknown; on completed returns 44 candidate-unknown, 22 project-unknown; every completed-return witness enumerated by an uncapped scratch rerun of the same evaluator (the record keeps 6 per kind). Project stands.

### 7 — Add lines 5 and 6
Status: **AGREE**

### 8 — Subtract line 7 from line 4 (if your 2024 filing status was married filing separately and
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"from": {"line": "4"}, "op": "subtract_floor0", "take": {"line": "7"}}}, {"guard": {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.mfs_spouse_itemized"}], "test": "eq"}, "then": {"from": {"line": "4"}, "op": "subtract_floor0", "take": {"line": "7"}}}, {"guard": {"args": [{"const": true}, {"input": "refund.mfs_spouse_itemized"}], "test": "eq"}, "then": {"line": "4"}}], "op": "choose"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": true}, {"input": "refund.mfs_spouse_itemized"}], "test": "eq"}], "test": "all"}, "then": {"line": "4"}}, {"guard": {"args": [{"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": true}, {"input": "refund.mfs_spouse_itemized"}], "test": "ne"}], "test": "any"}, "then": {"from": {"line": "4"}, "op": "subtract_floor0", "take": {"line": "7"}}}], "op": "choose"}
```

Second transcription's note: In the STOP case this line is zero, so line 9 is zero and none of the refund is taxable.

Ruling: model error; inherited from line 6. i1040gi p. 90, Note: "If the filing status on your 2024 Form 1040 or 1040-SR was married filing separately and your spouse itemized deductions in 2024, skip lines 5 through 7, enter the amount from line 4 on line 8", and line 8: "Is the amount on line 7 less than the amount on line 4? No. STOP None of your refund is taxable. Yes. Subtract line 7 from line 4". The candidate's own line 8 (copy line 4 for a separate return with an itemizing spouse, otherwise line 4 less line 7 floored) is the project's. Its only differences come through line 7 from its line 6: stage16.mut.refund_single_unasked (project $1,400.00, candidate unknown for refund.spouse_born) and partial records withholding the spouse boxes on bases with no refund (Every partial base of the bank is a return with no refund (refund.received $0.00), and s1.line1 reads the worksheet only when refund.has (refund.received more than zero) is true (forms/2025/s1.yaml), so the partial-record differences on those bases are on lines the return never reads). Triage executable-triage-v2 (`reviews/2025/transcription/triage/refund.json`; 1,495 fixtures, 500 generated returns seed 20261026, 640 partial records from 40 bases; 2,635 comparisons): 2,554 agree; differences 81 candidate-unknown; on completed returns 44 candidate-unknown; every completed-return witness enumerated by an uncapped scratch rerun of the same evaluator (the record keeps 6 per kind). Project stands.

### 9 — Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on Schedule 1,
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "2"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "2"}, {"line": "1"}], "test": "lt"}, "then": {"of": [{"line": "3"}, {"line": "8"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"of": [{"line": "3"}, {"line": "8"}], "op": "smaller_of"}
```

Ruling: model error; i1040gi p. 90, worksheet line 3: "Is the amount on line 1 more than the amount on line 2? No. STOP None of your refund is taxable." and line 9: "Enter the smaller of line 3 or line 8". The project stops at line 3 (zero when line 1 is not more than line 2, without lines 4 to 8); the candidate always takes the smaller of lines 3 and 8, so after a line 3 STOP it still needs line 8, the 2024 filing status and the box answers: stage16.mut.refund_line3_stop gives the project $0.00 and the candidate unknown for refund.status. It also inherits line 6 (stage16.mut.refund_single_unasked: project $1,400.00, candidate unknown for refund.spouse_born). stage16.refuse.refund.box8 and .not_2024 (candidate refuses on its line-1 gates; the project refuses the same returns at refund.taxable) and stage16.refuse.refund.line5e_bad (project refuses at the cited screen, candidate $3,000.00) are scope on refused returns. The completed-return candidate-unknown are partial records on bases with no refund: Every partial base of the bank is a return with no refund (refund.received $0.00), and s1.line1 reads the worksheet only when refund.has (refund.received more than zero) is true (forms/2025/s1.yaml), so the partial-record differences on those bases are on lines the return never reads. No value differs. Triage executable-triage-v2 (`reviews/2025/transcription/triage/refund.json`; 1,495 fixtures, 500 generated returns seed 20261026, 640 partial records from 40 bases; 2,635 comparisons): 2,310 agree; differences 2 candidate-refuses, 322 candidate-unknown, 1 project-refuses; on completed returns 176 candidate-unknown; every completed-return witness enumerated by an uncapped scratch rerun of the same evaluator (the record keeps 6 per kind). Corrects the earlier "equivalent" class of this unchanged pair, whose triage did not show the STOP witness. Project stands.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| refund.taxable | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | - |
| 1 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.not_2024 |
| 3 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.not_2024 |
| 9 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.not_2024 |

## Line subjects

What each compared line's verdict depends on within the document (tools/transcription/subjects.py); a line-scoped review reruns the lines whose hash changed.

| line | subject sha256 |
| --- | --- |
| refund.has | 6bd0ea50399f2920d7ff293034a6853e1de7c6cfc1f1b0dc94229cbd400ab049 |
| refund.taxable | 44e2ccc3c429357f1e1bf8789bbf3172ac3da031a3bdd8cd3d2169683d15b7d9 |
| 1 | c7db273fdb74a02c74e40bf81a97232f756a677bb3dd7be39a63f54709999fda |
| 2 | 91eb1ef47a73d5a7374918887568614cf502d38e4d54dd584ff71e4c439c2fc6 |
| 3 | dee0b86519f8bb9ddf2c825b78358413221b68d930a03e98e7344a8d18bf6ede |
| 4 | 3c5a9ffb234d55e9d92f41c2448191732b0c6e38e87d64a593f5b1a5603fc4e3 |
| 5 | c02e5042fa5062503cbaf42cafe2f64610447e57d9faf525a0e1904747cfda6f |
| 6 | bd0f71484f4b227904202cecbc11ee69fc6b5c8cda8b7ca7fa271046dbc23630 |
| 7 | 5d74c147b1a5ab8fec6ef3b481bfde13d4561526952288baa8079115adfad20c |
| 8 | 3f62e583d65006a11a37557b8c3af5e2fea48bf36f8e191f1cced570c6f3cb8c |
| 9 | 17798256689f7d38756c72948184990c053352ca7de96936fb93cb52982ee74e |
| (rest of the document) | 9a12945506dcc91b7709e71f5f54423e182739ad982dde223b33e1168f0e0716 |

## Raw second transcription

```yaml
```yaml
lines:
  - id: refund.h_zero
    printed: "(helper)"
    label: "Zero (used where the worksheet says none of the refund is taxable or no box is checked)"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}

  - id: refund.has
    printed: "(helper)"
    label: "You received a refund, credit, or offset of state or local income taxes in 2025"
    type: Bool
    expr: {op: test, gt: [refund.received, {const: 0}]}
    note: "Open: the interface name only. Read as 'some state or local income tax refund, credit or offset was received in 2025' (refund.received is more than zero), the condition under which the line 1 instructions apply."

  - id: refund.line1
    printed: "1"
    label: "Enter the income tax refund from Form(s) 1099-G (or similar statement). But don't enter more than the amount of your state and local income taxes shown on your 2024 Schedule A, line 5d"
    type: NonNegDollars
    expr: {op: smaller_of, of: [refund.received, refund.line5d_2024]}
    refuses: [refund.box8, refund.not_2024, refund.exc_tax, refund.exc_who]
    note: "Open: the cap is 'the amount of your state and local income taxes shown on your 2024 Schedule A, line 5d', but the closed interface supplies only the full line 5d amount (income or sales taxes, real estate taxes and personal property taxes together). Chose line 5d as the cap. The Exception list (refunds for other years, 0% capital gain rate, refund more than the income-minus-sales-tax difference, 2024 tax paid in 2025, AMT, unused credits, dependent, joint state return) is refused here through the screening gates. A refund attributable to a tax on trade or business income only (Form 1099-G box 8) is also refused."

  - id: refund.line2
    printed: "2"
    label: "Is the amount of state and local income taxes (or general sales taxes), real estate taxes, and personal property taxes paid in 2024 (generally, your 2024 Schedule A, line 5d) more than the amount on your 2024 Schedule A, line 5e? No: enter the amount from line 1 on line 3 and go to line 4. Yes: subtract line 5e from that amount"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: refund.line5d_2024, take: refund.line5e_2024}
    note: "In the 'No' case line 2 is left blank. It is held as zero, so line 3 (line 1 minus line 2) equals line 1, as the 'No' instruction requires."

  - id: refund.line3
    printed: "3"
    label: "Is the amount on line 1 more than the amount on line 2? No: STOP. None of your refund is taxable. Yes: Subtract line 2 from line 1"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: refund.line1, take: refund.line2}
    note: "In the STOP case this line is zero. Line 9, the smaller of lines 3 and 8, is then zero, so none of the refund is taxable."

  - id: refund.line4
    printed: "4"
    label: "Enter your total itemized deductions from your 2024 Schedule A, line 17"
    type: NonNegDollars
    expr: {op: copy, from: refund.line17_2024}

  - id: refund.h_std_single
    printed: "(helper)"
    label: "Single or married filing separately—$14,600"
    type: NonNegDollars
    expr: {op: param, ref: refund.std_single}

  - id: refund.h_std_joint
    printed: "(helper)"
    label: "Married filing jointly or qualifying surviving spouse—$29,200"
    type: NonNegDollars
    expr: {op: param, ref: refund.std_joint}

  - id: refund.h_std_hoh
    printed: "(helper)"
    label: "Head of household—$21,900"
    type: NonNegDollars
    expr: {op: param, ref: refund.std_hoh}

  - id: refund.line5
    printed: "5"
    label: "Enter the amount shown below for the filing status claimed on your 2024 Form 1040 or 1040-SR"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            any:
              - {op: test, eq: [refund.status, {const: "single"}]}
              - {op: test, eq: [refund.status, {const: "mfs"}]}
          then: refund.h_std_single
        - guard:
            op: test
            any:
              - {op: test, eq: [refund.status, {const: "mfj"}]}
              - {op: test, eq: [refund.status, {const: "qss"}]}
          then: refund.h_std_joint
        - guard: {op: test, eq: [refund.status, {const: "hoh"}]}
          then: refund.h_std_hoh

  - id: refund.h_box_married
    printed: "(helper)"
    label: "$1,550 per box checked"
    type: NonNegDollars
    expr: {op: param, ref: refund.box_married}

  - id: refund.h_box_unmarried
    printed: "(helper)"
    label: "$1,950 per box checked if your 2024 filing status was single or head of household"
    type: NonNegDollars
    expr: {op: param, ref: refund.box_unmarried}

  - id: refund.h_box_amount
    printed: "(helper)"
    label: "Amount per box checked: $1,550 ($1,950 if your 2024 filing status was single or head of household)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            any:
              - {op: test, eq: [refund.status, {const: "single"}]}
              - {op: test, eq: [refund.status, {const: "hoh"}]}
          then: refund.h_box_unmarried
        - guard:
            op: test
            not:
              op: test
              any:
                - {op: test, eq: [refund.status, {const: "single"}]}
                - {op: test, eq: [refund.status, {const: "hoh"}]}
          then: refund.h_box_married

  - id: refund.h_you_born_amt
    printed: "(helper)"
    label: "You were born before January 2, 1960 (box amount if checked)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.you_born, {const: true}]}
          then: refund.h_box_amount
        - guard: {op: test, eq: [refund.you_born, {const: false}]}
          then: refund.h_zero

  - id: refund.h_you_blind_amt
    printed: "(helper)"
    label: "You are blind (box amount if checked)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.you_blind, {const: true}]}
          then: refund.h_box_amount
        - guard: {op: test, eq: [refund.you_blind, {const: false}]}
          then: refund.h_zero

  - id: refund.h_spouse_born_amt
    printed: "(helper)"
    label: "Spouse was born before January 2, 1960 (box amount if checked)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.spouse_born, {const: true}]}
          then: refund.h_box_amount
        - guard: {op: test, eq: [refund.spouse_born, {const: false}]}
          then: refund.h_zero
    note: "The married-filing-separately restriction (spouse had no income, isn't filing a return and can't be claimed as a dependent) is carried by the wording of the spouse_born input. The worksheet does not otherwise restrict the spouse boxes by status, so the input is used as answered."

  - id: refund.h_spouse_blind_amt
    printed: "(helper)"
    label: "Spouse is blind (box amount if checked)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.spouse_blind, {const: true}]}
          then: refund.h_box_amount
        - guard: {op: test, eq: [refund.spouse_blind, {const: false}]}
          then: refund.h_zero
    note: "The married-filing-separately restriction is carried by the wording of the spouse_blind input."

  - id: refund.line6
    printed: "6"
    label: "Check any boxes that apply. No boxes checked: enter -0-. Otherwise multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)"
    type: NonNegDollars
    expr: {op: sum, of: [refund.h_you_born_amt, refund.h_you_blind_amt, refund.h_spouse_born_amt, refund.h_spouse_blind_amt]}
    note: "The count of boxes times the per-box amount is written as the sum of the per-box amount for each checked box, which is the same value."

  - id: refund.line7
    printed: "7"
    label: "Add lines 5 and 6"
    type: NonNegDollars
    expr: {op: sum, of: [refund.line5, refund.line6]}

  - id: refund.h_line8_figured
    printed: "(helper)"
    label: "Is the amount on line 7 less than the amount on line 4? No: STOP. None of your refund is taxable. Yes: Subtract line 7 from line 4"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: refund.line4, take: refund.line7}

  - id: refund.h_mfs_skip
    printed: "(helper)"
    label: "Filing status on your 2024 Form 1040 or 1040-SR was married filing separately and your spouse itemized deductions in 2024"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [refund.status, {const: "mfs"}]}
        - {op: test, eq: [refund.mfs_spouse_itemized, {const: true}]}

  - id: refund.line8
    printed: "8"
    label: "Is the amount on line 7 less than the amount on line 4? No: STOP. None of your refund is taxable. Yes: Subtract line 7 from line 4. (If 2024 status was married filing separately and your spouse itemized, enter the amount from line 4.)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.h_mfs_skip, {const: true}]}
          then: refund.line4
        - guard: {op: test, eq: [refund.h_mfs_skip, {const: false}]}
          then: refund.h_line8_figured
    note: "In the STOP case this line is zero, so line 9 is zero and none of the refund is taxable."

  - id: refund.line9
    printed: "9"
    label: "Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on Schedule 1, line 1"
    type: NonNegDollars
    expr: {op: smaller_of, of: [refund.line3, refund.line8]}

  - id: refund.taxable
    printed: "(helper)"
    label: "Taxable refunds, credits, or offsets of state and local income taxes (Schedule 1, line 1)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard:
            op: test
            any:
              - {op: test, eq: [refund.has, {const: false}]}
              - {op: test, eq: [refund.itemized, {const: false}]}
              - {op: test, eq: [refund.sales, {const: true}]}
          then: refund.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [refund.has, {const: true}]}
              - {op: test, eq: [refund.itemized, {const: true}]}
              - {op: test, eq: [refund.sales, {const: false}]}
          then: refund.line9
    refuses: [refund.box8]
    note: "Read as the Schedule 1 line 1 amount. The TIP says none of the refund is taxable if, in the year you paid the tax, you didn't itemize or you elected to deduct general sales taxes. Otherwise the amount is line 9 of the worksheet. A refund of a tax on trade or business income only (box 8) is reported on Schedule C, not here, so it is refused."
```
```
