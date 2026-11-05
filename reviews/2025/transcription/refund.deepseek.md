# Transcription agreement — refund

Second transcription of `State and Local Income Tax Refund Worksheet—Schedule 1, Line 1` by an isolated model (spec 6.5), compared line by line with `forms/2025/refund.yaml`.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
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
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | e9a5368e306d5d9fbca1b6412dc1183b49c04df4f171cae4524a87e24b6b63bf |
| printed lines compared | 11 |
| agree / disagree / missing | 3 / 8 / 0 |
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
Status: **DISAGREE**

Project:

```json
{"args": [{"const": 0}, {"input": "refund.received"}], "test": "lt"}
```

Second:

```json
{"args": [{"const": 0}, {"line": "9"}], "test": "lt"}
```

Ruling: model error; i1040gi p. 88, Line 1: "If you received a refund, credit, or offset of state or local income taxes in 2025, you may be required to report this amount". refund.has is whether a refund was received (refund.received more than zero), which s1.line1 uses to decide whether to read anything else; the candidate redefines it as line 9 more than zero. Value witnesses: stage16.refund.f1, f2, f4 and f7 (refunds that are not taxable; project true, candidate false) and two refused stage16.cleanup returns; it needs the whole worksheet on every return (completed-return candidate-unknown for refund.box8 on 124 fixtures with no refund, for example), and refuses on the worksheet gates (stage16.refuse.refund.exc_tax, exc_who, box8, not_2024). Triage executable-triage-v2 (`reviews/2025/transcription/triage/refund.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 385 partial records from 40 bases; 2,380 comparisons): 848 agree; differences 4 candidate-refuses, 1499 candidate-unknown, 23 project-unknown, 6 value; on completed returns 254 candidate-unknown; every completed-return witness enumerated by an uncapped scratch rerun of the same evaluator (the record keeps 6 per kind). Project stands.

### refund.taxable — Taxable part of your refund (zero when you did not itemize for 2024 or deducted general sa
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "refund.sales"}], "test": "eq"}, {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "eq"}], "test": "all"}, "then": {"line": "9"}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "refund.sales"}], "test": "ne"}, {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second:

```json
{"line": "9"}
```

Ruling: model error and scope; inherited from lines 6 and 9. i1040gi p. 88, Line 1, TIP: "None of your refund is taxable if, in the year you paid the tax, you either (a) didn’t itemize deductions, or (b) elected to deduct state and local general sales taxes instead of state and local income taxes"; i1040gi p. 90, worksheet line 3: "Is the amount on line 1 more than the amount on line 2? No. STOP None of your refund is taxable.". The candidate copies its line 9 and moves the gates onto the worksheet lines. Its differences on refund returns are stage16.mut.refund_single_unasked (project $1,400.00, candidate unknown for refund.spouse_born) and stage16.mut.refund_line3_stop (project $0.00, candidate unknown for refund.status), inherited from lines 6 and 9; stage16.refuse.refund.line5e_bad (project refuses at the cited screen, candidate $3,000.00) is scope. The completed-return candidate-unknown (refund.exc_tax, exc_who, the status and box answers withheld) are partial records on bases with no refund: Every partial base of the bank is a return with no refund (refund.received $0.00), and s1.line1 reads the worksheet only when refund.has (refund.received more than zero) is true (forms/2025/s1.yaml), so the partial-record differences on those bases are on lines the return never reads. Triage executable-triage-v2 (`reviews/2025/transcription/triage/refund.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 385 partial records from 40 bases; 2,380 comparisons): 2,216 agree; differences 163 candidate-unknown, 1 project-refuses; on completed returns 91 candidate-unknown; every completed-return witness enumerated by an uncapped scratch rerun of the same evaluator (the record keeps 6 per kind). Project stands.

### 1 — Enter the income tax refund from Form(s) 1099-G (or similar statement). But don’t enter mo
Status: **DISAGREE**

Project:

```json
{"of": [{"input": "refund.line5d_2024"}, {"input": "refund.received"}], "op": "smaller_of"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "refund.sales"}], "test": "eq"}, {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"input": "refund.line5d_2024"}, {"input": "refund.received"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "refund.sales"}], "test": "ne"}, {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The instructions’ tip says none of the refund is taxable if you didn’t itemize or elected sales taxes. I set the worksheet lines to zero in that case rather than using line 5d.

Ruling: representation and scope; i1040gi p. 90, worksheet line 1: "Enter the income tax refund from Form(s) 1099-G (or similar statement). But don’t enter more than the amount of your state and local income taxes shown on your 2024 Schedule A, line 5d". Where the worksheet is used (itemized, no sales-tax election) the candidate takes the same smaller of refund.received and line 5d; it enters zero otherwise, where the project's refund.taxable never reads line 1. stage16.refuse.refund.box8 and .not_2024 (candidate refuses on line 1, project $3,000.00 on line 1 and refuses the same returns at refund.taxable) are scope on refused returns. The completed-return differences (refund.itemized, box8 or not_2024 withheld from the candidate; refund.line5d_2024 withheld from the project) are partial records on bases with no refund: Every partial base of the bank is a return with no refund (refund.received $0.00), and s1.line1 reads the worksheet only when refund.has (refund.received more than zero) is true (forms/2025/s1.yaml), so the partial-record differences on those bases are on lines the return never reads. No value differs. Triage executable-triage-v2 (`reviews/2025/transcription/triage/refund.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 385 partial records from 40 bases; 2,380 comparisons): 2,263 agree; differences 2 candidate-refuses, 69 candidate-unknown, 46 project-unknown; on completed returns 39 candidate-unknown, 13 project-unknown; every completed-return witness enumerated by an uncapped scratch rerun of the same evaluator (the record keeps 6 per kind). Project stands.

### 2 — Subtract the amount on your 2024 Schedule A, line 5e, from the amount of state and local i
Status: **DISAGREE**

Project:

```json
{"from": {"input": "refund.line5d_2024"}, "op": "subtract_floor0", "take": {"input": "refund.line5e_2024"}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "refund.sales"}], "test": "eq"}, {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "eq"}], "test": "all"}, "then": {"from": {"input": "refund.line5d_2024"}, "op": "subtract_floor0", "take": {"input": "refund.line5e_2024"}}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "refund.sales"}], "test": "ne"}, {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: When 2024 Schedule A line 5d is not more than line 5e, the worksheet does not enter line 2 and sends line 1 to line 3; I use zero on line 2 so line 3 equals line 1.

Ruling: representation and scope; i1040gi p. 90, worksheet line 2, "Yes. Subtract the amount on your 2024 Schedule A, line 5e" from line 5d. Both take line 5d less line 5e floored at zero where the worksheet is used; the candidate enters zero where it is not. stage16.refuse.refund.line5e_bad (project refuses at the cited impossible-entry screen refund.line5e_bad, candidate $0.00) is scope. The completed-return differences are partial records on bases with no refund: Every partial base of the bank is a return with no refund (refund.received $0.00), and s1.line1 reads the worksheet only when refund.has (refund.received more than zero) is true (forms/2025/s1.yaml), so the partial-record differences on those bases are on lines the return never reads. No value differs. Triage executable-triage-v2 (`reviews/2025/transcription/triage/refund.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 385 partial records from 40 bases; 2,380 comparisons): 2,310 agree; differences 23 candidate-unknown, 1 project-refuses, 46 project-unknown; on completed returns 13 candidate-unknown, 26 project-unknown; every completed-return witness enumerated by an uncapped scratch rerun of the same evaluator (the record keeps 6 per kind). Project stands.

### 3 — Subtract line 2 from line 1
Status: **AGREE**

### 4 — Enter your total itemized deductions from your 2024 Schedule A, line 17
Status: **DISAGREE**

Project:

```json
{"input": "refund.line17_2024"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "refund.sales"}], "test": "eq"}, {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "eq"}], "test": "all"}, "then": {"input": "refund.line17_2024"}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "refund.sales"}], "test": "ne"}, {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i1040gi p. 90, worksheet line 4: "Enter your total itemized deductions from your 2024 Schedule A, line 17." Both enter refund.line17_2024 where the worksheet is used; the candidate enters zero otherwise. Every difference is a partial record on a base with no refund: Every partial base of the bank is a return with no refund (refund.received $0.00), and s1.line1 reads the worksheet only when refund.has (refund.received more than zero) is true (forms/2025/s1.yaml), so the partial-record differences on those bases are on lines the return never reads. No value differs. Triage executable-triage-v2 (`reviews/2025/transcription/triage/refund.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 385 partial records from 40 bases; 2,380 comparisons): 2,334 agree; differences 23 candidate-unknown, 23 project-unknown; on completed returns 13 candidate-unknown, 13 project-unknown; every completed-return witness enumerated by an uncapped scratch rerun of the same evaluator (the record keeps 6 per kind). Project stands.

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
{"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.spouse_blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.spouse_blind"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.spouse_born"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.spouse_born"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.you_blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.you_blind"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.you_born"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.you_born"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}], "op": "choose"}], "op": "sum"}
```

Ruling: model error; i1040gi p. 90, worksheet line 6: "Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)" and its footnote "*If your filing status is married filing separately, you can check the boxes for your spouse only if your spouse had no income, isn’t filing a return, and can’t be claimed as a dependent on another person’s return"; p. 33, Line 12d: "Don’t check any boxes for your spouse if your filing status is head of household". The candidate counts the spouse boxes for every 2024 status and needs them where the source does not: stage16.mut.refund_single_unasked (single; project $0.00, candidate unknown for refund.spouse_born). The other differences are partial records on bases with no refund: Every partial base of the bank is a return with no refund (refund.received $0.00), and s1.line1 reads the worksheet only when refund.has (refund.received more than zero) is true (forms/2025/s1.yaml), so the partial-record differences on those bases are on lines the return never reads. No value differs. Triage executable-triage-v2 (`reviews/2025/transcription/triage/refund.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 385 partial records from 40 bases; 2,380 comparisons): 2,310 agree; differences 47 candidate-unknown, 23 project-unknown; on completed returns 26 candidate-unknown, 13 project-unknown; every completed-return witness enumerated by an uncapped scratch rerun of the same evaluator (the record keeps 6 per kind). Project stands.

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

Ruling: model error; inherited from line 6. i1040gi p. 90, line 8: "Is the amount on line 7 less than the amount on line 4? No. STOP None of your refund is taxable. Yes. Subtract line 7 from line 4". The candidate's own line 8 logic is the project's; its differences are stage16.mut.refund_single_unasked (project $1,400.00, candidate unknown for refund.spouse_born, through line 7) and partial records on bases with no refund (Every partial base of the bank is a return with no refund (refund.received $0.00), and s1.line1 reads the worksheet only when refund.has (refund.received more than zero) is true (forms/2025/s1.yaml), so the partial-record differences on those bases are on lines the return never reads). Triage executable-triage-v2 (`reviews/2025/transcription/triage/refund.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 385 partial records from 40 bases; 2,380 comparisons): 2,287 agree; differences 70 candidate-unknown, 23 project-unknown; on completed returns 39 candidate-unknown, 13 project-unknown; every completed-return witness enumerated by an uncapped scratch rerun of the same evaluator (the record keeps 6 per kind). Project stands.

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

Ruling: model error; i1040gi p. 90, worksheet line 3: "Is the amount on line 1 more than the amount on line 2? No. STOP None of your refund is taxable.". The candidate always takes the smaller of lines 3 and 8, so after a line 3 STOP it still needs line 8 and the 2024 filing status: stage16.mut.refund_line3_stop (project $0.00, candidate unknown for refund.status); it inherits line 6 (stage16.mut.refund_single_unasked). stage16.refuse.refund.box8, .not_2024 and .line5e_bad are scope on refused returns. The completed-return differences are partial records on bases with no refund: Every partial base of the bank is a return with no refund (refund.received $0.00), and s1.line1 reads the worksheet only when refund.has (refund.received more than zero) is true (forms/2025/s1.yaml), so the partial-record differences on those bases are on lines the return never reads. No value differs. Triage executable-triage-v2 (`reviews/2025/transcription/triage/refund.deepseek.json`; 1,495 fixtures, 500 generated returns seed 20261026, 385 partial records from 40 bases; 2,380 comparisons): 2,122 agree; differences 2 candidate-refuses, 186 candidate-unknown, 1 project-refuses, 69 project-unknown; on completed returns 104 candidate-unknown, 26 project-unknown; every completed-return witness enumerated by an uncapped scratch rerun of the same evaluator (the record keeps 6 per kind). Project stands.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| refund.has | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 |
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
lines:
  - id: refund.line1
    printed: "1"
    label: "Enter the income tax refund from Form(s) 1099-G (or similar statement). But don’t enter more than the amount of your state and local income taxes shown on your 2024 Schedule A, line 5d"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.h_applies, {const: true}]}
          then: refund.h_line1_limited
        - guard: {op: test, eq: [refund.h_applies, {const: false}]}
          then: refund.h_zero
    refuses: [refund.box8, refund.not_2024, refund.exc_tax, refund.exc_who]
    note: "The instructions’ tip says none of the refund is taxable if you didn’t itemize or elected sales taxes. I set the worksheet lines to zero in that case rather than using line 5d."
  - id: refund.line2
    printed: "2"
    label: "Is the amount of state and local income taxes (or general sales taxes), real estate taxes, and personal property taxes paid in 2024 (generally, this is the amount reported on your 2024 Schedule A, line 5d) more than the amount on your 2024 Schedule A, line 5e?"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.h_applies, {const: true}]}
          then: refund.h_line2_sub
        - guard: {op: test, eq: [refund.h_applies, {const: false}]}
          then: refund.h_zero
    note: "When 2024 Schedule A line 5d is not more than line 5e, the worksheet does not enter line 2 and sends line 1 to line 3; I use zero on line 2 so line 3 equals line 1."
  - id: refund.line3
    printed: "3"
    label: "Is the amount on line 1 more than the amount on line 2?"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: refund.line1
      take: refund.line2
  - id: refund.line4
    printed: "4"
    label: "Enter your total itemized deductions from your 2024 Schedule A, line 17."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.h_applies, {const: true}]}
          then: refund.line17_2024
        - guard: {op: test, eq: [refund.h_applies, {const: false}]}
          then: refund.h_zero
  - id: refund.line5
    printed: "5"
    label: "Enter the amount shown below for the filing status claimed on your 2024 Form 1040 or 1040-SR. • Single or married filing separately—$14,600 • Married filing jointly or qualifying surviving spouse—$29,200 • Head of household—$21,900"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.status, {const: "single"}]}
          then: refund.h_std_single
        - guard: {op: test, eq: [refund.status, {const: "mfs"}]}
          then: refund.h_std_single
        - guard: {op: test, eq: [refund.status, {const: "mfj"}]}
          then: refund.h_std_joint
        - guard: {op: test, eq: [refund.status, {const: "qss"}]}
          then: refund.h_std_joint
        - guard: {op: test, eq: [refund.status, {const: "hoh"}]}
          then: refund.h_std_hoh
  - id: refund.line6
    printed: "6"
    label: "Check any boxes that apply.* You were born before January 2, 1960. You are blind. Spouse was born before January 2, 1960. Spouse is blind. No boxes checked. Enter -0-. Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)."
    type: NonNegDollars
    expr:
      op: sum
      of: [refund.h_box_you_born, refund.h_box_you_blind, refund.h_box_spouse_born, refund.h_box_spouse_blind]
  - id: refund.line7
    printed: "7"
    label: "Add lines 5 and 6"
    type: NonNegDollars
    expr:
      op: sum
      of: [refund.line5, refund.line6]
  - id: refund.line8
    printed: "8"
    label: "Is the amount on line 7 less than the amount on line 4?"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.h_mfs_skip, {const: true}]}
          then: refund.line4
        - guard: {op: test, eq: [refund.h_mfs_skip, {const: false}]}
          then: refund.h_line8_base
  - id: refund.line9
    printed: "9"
    label: "Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on Schedule 1, line 1"
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [refund.line3, refund.line8]
  - id: refund.has
    printed: "(helper)"
    label: "Whether any part of the refund is taxable"
    type: Bool
    expr:
      op: test
      gt: [refund.taxable, {const: 0}]
  - id: refund.taxable
    printed: "(helper)"
    label: "Taxable part of the refund"
    type: NonNegDollars
    expr:
      op: copy
      from: refund.line9
  - id: refund.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: refund.h_applies
    printed: "(helper)"
    label: "Whether the worksheet applies (itemized and did not elect sales taxes)"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [refund.itemized, {const: true}]}
        - {op: test, eq: [refund.sales, {const: false}]}
  - id: refund.h_line1_limited
    printed: "(helper)"
    label: "Refund limited to 2024 Schedule A line 5d"
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [refund.received, refund.line5d_2024]
  - id: refund.h_line2_sub
    printed: "(helper)"
    label: "2024 Schedule A line 5d less line 5e"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: refund.line5d_2024
      take: refund.line5e_2024
  - id: refund.h_std_single
    printed: "(helper)"
    label: "Standard amount for single or married filing separately"
    type: NonNegDollars
    expr: {op: param, ref: refund.std_single}
  - id: refund.h_std_joint
    printed: "(helper)"
    label: "Standard amount for married filing jointly or qualifying surviving spouse"
    type: NonNegDollars
    expr: {op: param, ref: refund.std_joint}
  - id: refund.h_std_hoh
    printed: "(helper)"
    label: "Standard amount for head of household"
    type: NonNegDollars
    expr: {op: param, ref: refund.std_hoh}
  - id: refund.h_box_married
    printed: "(helper)"
    label: "Amount per box for a married 2024 filing status"
    type: NonNegDollars
    expr: {op: param, ref: refund.box_married}
  - id: refund.h_box_unmarried
    printed: "(helper)"
    label: "Amount per box for a single or head of household 2024 filing status"
    type: NonNegDollars
    expr: {op: param, ref: refund.box_unmarried}
  - id: refund.h_box_rate
    printed: "(helper)"
    label: "Amount per box checked"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.status, {const: "single"}]}
          then: refund.h_box_unmarried
        - guard: {op: test, eq: [refund.status, {const: "mfs"}]}
          then: refund.h_box_married
        - guard: {op: test, eq: [refund.status, {const: "mfj"}]}
          then: refund.h_box_married
        - guard: {op: test, eq: [refund.status, {const: "qss"}]}
          then: refund.h_box_married
        - guard: {op: test, eq: [refund.status, {const: "hoh"}]}
          then: refund.h_box_unmarried
  - id: refund.h_box_you_born
    printed: "(helper)"
    label: "Amount for the taxpayer born before January 2, 1960"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.you_born, {const: true}]}
          then: refund.h_box_rate
        - guard: {op: test, eq: [refund.you_born, {const: false}]}
          then: refund.h_zero
  - id: refund.h_box_you_blind
    printed: "(helper)"
    label: "Amount for the taxpayer blind at the end of 2024"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.you_blind, {const: true}]}
          then: refund.h_box_rate
        - guard: {op: test, eq: [refund.you_blind, {const: false}]}
          then: refund.h_zero
  - id: refund.h_box_spouse_born
    printed: "(helper)"
    label: "Amount for the spouse born before January 2, 1960"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.spouse_born, {const: true}]}
          then: refund.h_box_rate
        - guard: {op: test, eq: [refund.spouse_born, {const: false}]}
          then: refund.h_zero
  - id: refund.h_box_spouse_blind
    printed: "(helper)"
    label: "Amount for the spouse blind at the end of 2024"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.spouse_blind, {const: true}]}
          then: refund.h_box_rate
        - guard: {op: test, eq: [refund.spouse_blind, {const: false}]}
          then: refund.h_zero
  - id: refund.h_line8_base
    printed: "(helper)"
    label: "Line 4 less line 7, not below zero"
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: refund.line4
      take: refund.line7
  - id: refund.h_mfs_skip
    printed: "(helper)"
    label: "Whether married filing separately with a spouse who itemized in 2024"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [refund.status, {const: "mfs"}]}
        - {op: test, eq: [refund.mfs_spouse_itemized, {const: true}]}
```
