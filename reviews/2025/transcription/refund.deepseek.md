# Transcription agreement — refund

Second transcription of `State and Local Income Tax Refund Worksheet—Schedule 1, Line 1` by an isolated model (spec 6.5), compared line by line with `forms/2025/refund.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | ec284b7b6e500a6af34dfa28e0c6586edf38a274d00591245eb3d28ca72750c6 |
| prompt policy | source-only-computation-v2 |
| comparison policy | checked-expression-types-v2 |
| input context policy | required-review-interfaces-v2 |
| complete input context | pass |
| required input context sha256 | 69df1010e4e816288a5a5b432d1e05ff1cb4465198994712e0fd778c0d38e0e1 |
| type validation policy | project-expression-types-v3 |
| model type validation | pass |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | fa2340bf10b343c4d737d5266a44774128963c71af1a288bb6c011108890e372 |
| printed lines compared | 11 |
| agree / disagree / missing | 6 / 5 / 0 |
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

Ruling: model error; i1040gi p. 88, Line 1: "If you received a refund, credit, or offset of state or local income taxes in 2025, you may be required to report this amount". refund.has is whether a refund was received (refund.received more than zero, which s1.line1 uses to decide whether to read anything else); the candidate redefines it as line 9 more than zero. executable-triage-v2 (`reviews/2025/transcription/triage/refund.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 445 partial records from 40 bases; 2,327 comparisons; every witness enumerated by an uncapped scratch rerun of tools/transcription/triage.mjs, the record keeps 6 per kind): 1,034 of 2,327 agree; 1,256 candidate-unknown (558 completed), 6 value (4 completed), 4 candidate-refuses, 27 project-unknown (none completed). Completed value, all enumerated: stage16.refund.f1 (no itemizing), f2 (sales-tax election), f4 and f7 (worksheet gives zero): project true, candidate false; Schedule 1 line 1 is $0.00 on both sides. Completed candidate-unknown: 476 no-refund fixtures (for example classm.f2441.1.deepseek) and 80 no-refund partial records on which the candidate needs refund.box8 or another exception gate, since its line 9 declares all four, answers the text does not need without a refund; and stage16.mut.refund_single_unasked and stage16.mut.refund_line3_stop, which need refund.mfs_spouse_itemized through line 8 (see lines 8 and 9). The 2 refused value records (stage16.cleanup.refuse.sa_charity.simultaneous, sa_excluded.simultaneous) are the same mechanism. The 4 candidate-refuses (stage16.refuse.refund.exc_tax, exc_who, box8, not_2024) are refused by the project on refund.taxable or line 1 under the same gates; the project-unknown records withhold refund.received, which the source needs. Project stands.

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

Ruling: model error and scope; inherited from lines 8 and 9. i1040gi p. 88, Line 1, TIP: "None of your refund is taxable if, in the year you paid the tax, you either (a) didn’t itemize deductions, or (b) elected to deduct state and local general sales taxes"; i1040gi p. 90, worksheet line 3: "Is the amount on line 1 more than the amount on line 2? No. STOP None of your refund is taxable.". executable-triage-v2 (`reviews/2025/transcription/triage/refund.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 445 partial records from 40 bases; 2,327 comparisons; every witness enumerated by an uncapped scratch rerun of tools/transcription/triage.mjs, the record keeps 6 per kind): 2,270 of 2,327 agree; 56 candidate-unknown (34 completed), 1 project-refuses. The candidate copies its line 9, which now declares all four exception gates itself, so box 8 and refund.not_2024 are asked of every refund (the earlier omission is gone); by reading it also asks exc_tax and exc_who of a filer who did not itemize, where the project asks them only on the worksheet path (line 1), answers the text does not need (no sampled refund return reaches it: the bank's partial bases have no refund). Completed candidate-unknown, all enumerated: 32 no-refund partial records withholding refund.exc_tax or refund.exc_who (project $0.00; s1.line1 reads refund.taxable only when refund.has (refund.received more than zero) is true (forms/2025/s1.yaml), and every partial base of the bank has no refund (refund.has false)); stage16.mut.refund_single_unasked (single 2024 filer, project $1,400.00) and stage16.mut.refund_line3_stop (project $0.00 at the line 3 STOP), on which the candidate needs refund.mfs_spouse_itemized: model error (lines 8 and 9). The project-refuses record (stage16.refuse.refund.line5e_bad, candidate $3,000.00) is the cited impossible-entry screen refund.line5e_bad (i1040sca p. 7, Line 5e, "enter the smaller of line 5d or $40,000"): scope. Project stands.

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
{"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.spouse_blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.spouse_blind"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.spouse_born"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.spouse_born"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.you_blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.you_blind"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.you_born"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.you_born"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}], "op": "choose"}], "op": "sum"}
```

Ruling: model error and scope; i1040gi p. 90, worksheet line 6: "Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)" and footnote "*If your filing status is married filing separately, you can check the boxes for your spouse only if your spouse had no income, isn’t filing a return, and can’t be claimed as a dependent on another person’s return"; p. 33, Line 12d: "Don’t check any boxes for your spouse if your filing status is head of household". executable-triage-v2 (`reviews/2025/transcription/triage/refund.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 445 partial records from 40 bases; 2,327 comparisons; every witness enumerated by an uncapped scratch rerun of tools/transcription/triage.mjs, the record keeps 6 per kind): 2,133 of 2,327 agree; 163 candidate-unknown (97 completed), 27 project-unknown (16 completed), 4 candidate-refuses. The candidate counts the spouse boxes for every 2024 filing status (a single or head of household filer answering yes would add $1,950 per spouse box), where the project asks them only for a joint or separate return (amb.2025.refund_boxes_2024); same reading as the archived ruling. Completed candidate-unknown, all enumerated: stage16.mut.refund_single_unasked (single filer, project $0.00, candidate needs refund.spouse_born) and 96 no-refund partial records withholding a spouse box question the project does not ask on that base or one of the four exception gates the candidate declares on line 6. The 16 completed project-unknown withhold refund.status where no box is checked; line 5 needs the status whenever line 6 is used, so not reachable. The candidate-refuses (stage16.refuse.refund.exc_tax, exc_who, box8, not_2024) are refused by the project on refund.taxable or line 1: scope. Box amounts otherwise agree. Project stands.

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
{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.mfs_spouse_itemized"}], "test": "eq"}, "then": {"from": {"line": "4"}, "op": "subtract_floor0", "take": {"line": "7"}}}, {"guard": {"args": [{"const": true}, {"input": "refund.mfs_spouse_itemized"}], "test": "eq"}, "then": {"line": "4"}}], "op": "choose"}
```

Second transcription's note: If the 2024 filing status was married filing separately and the spouse itemized, the worksheet says to skip lines 5 through 7 and enter line 4 on line 8; the true branch does that.

Ruling: model error and scope; i1040gi p. 90, Note: "If the filing status on your 2024 Form 1040 or 1040-SR was married filing separately and your spouse itemized deductions in 2024, skip lines 5 through 7, enter the amount from line 4 on line 8". executable-triage-v2 (`reviews/2025/transcription/triage/refund.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 445 partial records from 40 bases; 2,327 comparisons; every witness enumerated by an uncapped scratch rerun of tools/transcription/triage.mjs, the record keeps 6 per kind): 2,133 of 2,327 agree; 190 candidate-unknown (113 completed), 4 candidate-refuses. The candidate copies line 4 whenever refund.mfs_spouse_itemized is true without testing the 2024 status, so it asks every filer whether a spouse itemized (and a non-separate filer answering yes would skip lines 5 to 7); the Note applies only to a separate return. Completed candidate-unknown, all enumerated: stage16.mut.refund_single_unasked (single filer, project $1,400.00, candidate needs refund.mfs_spouse_itemized) and 112 no-refund partial records withholding refund.mfs_spouse_itemized, a spouse box question or an exception gate the candidate declares on line 8. The candidate-refuses (stage16.refuse.refund.exc_tax, exc_who, box8, not_2024; project $15,400.00) are refused by the project on refund.taxable or line 1: scope. Project stands.

### 9 — Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on Schedule 1,
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "2"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "2"}, {"line": "1"}], "test": "lt"}, "then": {"of": [{"line": "3"}, {"line": "8"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": false}, {"input": "refund.sales"}], "test": "eq"}, {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "eq"}], "test": "all"}, "then": {"of": [{"line": "3"}, {"line": "8"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": false}, {"input": "refund.sales"}], "test": "ne"}, {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The opening instruction says none of the refund is taxable if you did not itemize deductions or elected state and local general sales taxes instead of income taxes; line 9 is zero in those cases, otherwise it is the smaller of lines 3 and 8.

Ruling: model error and scope; i1040gi p. 90, worksheet line 3: "Is the amount on line 1 more than the amount on line 2? No. STOP None of your refund is taxable."; line 9: "Enter the smaller of line 3 or line 8". executable-triage-v2 (`reviews/2025/transcription/triage/refund.deepseek.json`; 1,382 fixtures, 500 generated returns seed 20261026, 445 partial records from 40 bases; 2,327 comparisons; every witness enumerated by an uncapped scratch rerun of tools/transcription/triage.mjs, the record keeps 6 per kind): 2,160 of 2,327 agree; 83 candidate-unknown (50 completed), 81 project-unknown (32 completed), 2 candidate-refuses, 1 project-refuses. The candidate takes the smaller of lines 3 and 8 whenever the worksheet applies, so after a line 3 STOP it still needs line 8 and the questions behind it, and it inherits line 8's spouse-itemized question. Completed candidate-unknown, all enumerated: stage16.mut.refund_line3_stop (project $0.00 at the STOP) and stage16.mut.refund_single_unasked (project $1,400.00), both needing refund.mfs_spouse_itemized; 48 no-refund partial records withholding refund.box8, refund.not_2024 or refund.itemized. The 32 completed project-unknown are no-refund partial records withholding refund.line5d_2024 or refund.line5e_2024 where the candidate gives $0.00 (worksheet not used), on which refund.taxable does not read line 9. The candidate-refuses (stage16.refuse.refund.box8, not_2024; project $0.00) are refused by the project on refund.taxable: scope. The project-refuses record (stage16.refuse.refund.line5e_bad, candidate $3,000.00) is the cited impossible-entry screen refund.line5e_bad (i1040sca p. 7, Line 5e, "enter the smaller of line 5d or $40,000"): scope. Project stands.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| refund.has | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 |
| refund.taxable | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | - |
| 1 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.not_2024 |
| 2 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 |
| 3 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.not_2024 |
| 4 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 |
| 5 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 |
| 6 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 |
| 7 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 |
| 8 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 |
| 9 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.not_2024 |

## Raw second transcription

```yaml
lines:
  - id: refund.line1
    printed: "1"
    label: "Enter the income tax refund from Form(s) 1099-G (or similar statement). But don’t enter more than the amount of your state and local income taxes shown on your 2024 Schedule A, line 5d."
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [refund.received, refund.line5d_2024]
    refuses: [refund.box8, refund.not_2024, refund.exc_tax, refund.exc_who]
  - id: refund.line2
    printed: "2"
    label: "Is the amount of state and local income taxes (or general sales taxes), real estate taxes, and personal property taxes paid in 2024 (generally, this is the amount reported on your 2024 Schedule A, line 5d) more than the amount on your 2024 Schedule A, line 5e? No. Enter the amount from line 1 on line 3 and go to line 4. Yes. Subtract the amount on your 2024 Schedule A, line 5e, from the amount of state and local income taxes (or general sales taxes), real estate taxes, and personal property taxes paid in 2024 (generally, this is the amount reported on your 2024 Schedule A, line 5d)."
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: refund.line5d_2024
      take: refund.line5e_2024
    refuses: [refund.box8, refund.not_2024, refund.exc_tax, refund.exc_who]
    note: "If 2024 Schedule A line 5d is not more than line 5e, the worksheet directs line 1 to line 3; line 2 is set to zero so that line 3 equals line 1."
  - id: refund.line3
    printed: "3"
    label: "Is the amount on line 1 more than the amount on line 2? No. STOP. None of your refund is taxable. Yes. Subtract line 2 from line 1."
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: refund.line1
      take: refund.line2
    refuses: [refund.box8, refund.not_2024, refund.exc_tax, refund.exc_who]
  - id: refund.line4
    printed: "4"
    label: "Enter your total itemized deductions from your 2024 Schedule A, line 17."
    type: NonNegDollars
    expr:
      op: copy
      from: refund.line17_2024
    refuses: [refund.box8, refund.not_2024, refund.exc_tax, refund.exc_who]
  - id: refund.line5
    printed: "5"
    label: "Enter the amount shown below for the filing status claimed on your 2024 Form 1040 or 1040-SR. • Single or married filing separately—$14,600 • Married filing jointly or qualifying surviving spouse—$29,200 • Head of household—$21,900."
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
    refuses: [refund.box8, refund.not_2024, refund.exc_tax, refund.exc_who]
  - id: refund.line6
    printed: "6"
    label: "Check any boxes that apply. No boxes checked. Enter -0-. Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)."
    type: NonNegDollars
    expr:
      op: sum
      of: [refund.h_box_you_born, refund.h_box_you_blind, refund.h_box_spouse_born, refund.h_box_spouse_blind]
    refuses: [refund.box8, refund.not_2024, refund.exc_tax, refund.exc_who]
  - id: refund.line7
    printed: "7"
    label: "Add lines 5 and 6."
    type: NonNegDollars
    expr:
      op: sum
      of: [refund.line5, refund.line6]
    refuses: [refund.box8, refund.not_2024, refund.exc_tax, refund.exc_who]
  - id: refund.line8
    printed: "8"
    label: "Is the amount on line 7 less than the amount on line 4? No. STOP. None of your refund is taxable. Yes. Subtract line 7 from line 4."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.mfs_spouse_itemized, {const: true}]}
          then: refund.line4
        - guard: {op: test, eq: [refund.mfs_spouse_itemized, {const: false}]}
          then: refund.h_line8_diff
    refuses: [refund.box8, refund.not_2024, refund.exc_tax, refund.exc_who]
    note: "If the 2024 filing status was married filing separately and the spouse itemized, the worksheet says to skip lines 5 through 7 and enter line 4 on line 8; the true branch does that."
  - id: refund.line9
    printed: "9"
    label: "Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on Schedule 1, line 1."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.h_applies, {const: true}]}
          then: refund.h_min_line3_line8
        - guard: {op: test, eq: [refund.h_applies, {const: false}]}
          then: refund.h_zero
    refuses: [refund.box8, refund.not_2024, refund.exc_tax, refund.exc_who]
    note: "The opening instruction says none of the refund is taxable if you did not itemize deductions or elected state and local general sales taxes instead of income taxes; line 9 is zero in those cases, otherwise it is the smaller of lines 3 and 8."
  - id: refund.h_zero
    printed: "(helper)"
    label: "Zero amount helper."
    type: NonNegDollars
    expr:
      op: param
      ref: sales.zero
  - id: refund.h_std_single
    printed: "(helper)"
    label: "2024 standard amount for single or married filing separately."
    type: NonNegDollars
    expr:
      op: param
      ref: refund.std_single
  - id: refund.h_std_joint
    printed: "(helper)"
    label: "2024 standard amount for married filing jointly or qualifying surviving spouse."
    type: NonNegDollars
    expr:
      op: param
      ref: refund.std_joint
  - id: refund.h_std_hoh
    printed: "(helper)"
    label: "2024 standard amount for head of household."
    type: NonNegDollars
    expr:
      op: param
      ref: refund.std_hoh
  - id: refund.h_box_1550
    printed: "(helper)"
    label: "Amount per checked box, $1,550."
    type: NonNegDollars
    expr:
      op: param
      ref: refund.box_married
  - id: refund.h_box_1950
    printed: "(helper)"
    label: "Amount per checked box, $1,950."
    type: NonNegDollars
    expr:
      op: param
      ref: refund.box_unmarried
  - id: refund.h_box_amount
    printed: "(helper)"
    label: "Amount per checked box for the 2024 filing status."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.status, {const: "single"}]}
          then: refund.h_box_1950
        - guard: {op: test, eq: [refund.status, {const: "hoh"}]}
          then: refund.h_box_1950
        - guard: {op: test, eq: [refund.status, {const: "mfs"}]}
          then: refund.h_box_1550
        - guard: {op: test, eq: [refund.status, {const: "mfj"}]}
          then: refund.h_box_1550
        - guard: {op: test, eq: [refund.status, {const: "qss"}]}
          then: refund.h_box_1550
  - id: refund.h_box_you_born
    printed: "(helper)"
    label: "Amount for the box that you were born before January 2, 1960."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.you_born, {const: true}]}
          then: refund.h_box_amount
        - guard: {op: test, eq: [refund.you_born, {const: false}]}
          then: refund.h_zero
  - id: refund.h_box_you_blind
    printed: "(helper)"
    label: "Amount for the box that you were blind at the end of 2024."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.you_blind, {const: true}]}
          then: refund.h_box_amount
        - guard: {op: test, eq: [refund.you_blind, {const: false}]}
          then: refund.h_zero
  - id: refund.h_box_spouse_born
    printed: "(helper)"
    label: "Amount for the box that your spouse was born before January 2, 1960."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.spouse_born, {const: true}]}
          then: refund.h_box_amount
        - guard: {op: test, eq: [refund.spouse_born, {const: false}]}
          then: refund.h_zero
  - id: refund.h_box_spouse_blind
    printed: "(helper)"
    label: "Amount for the box that your spouse was blind at the end of 2024."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.spouse_blind, {const: true}]}
          then: refund.h_box_amount
        - guard: {op: test, eq: [refund.spouse_blind, {const: false}]}
          then: refund.h_zero
  - id: refund.h_line8_diff
    printed: "(helper)"
    label: "Line 8 amount before the married-filing-separately spouse-itemized branch."
    type: NonNegDollars
    expr:
      op: subtract_floor0
      from: refund.line4
      take: refund.line7
  - id: refund.h_applies
    printed: "(helper)"
    label: "Whether the refund worksheet can produce a taxable amount: deductions were itemized for 2024 and state and local general sales taxes were not elected."
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [refund.itemized, {const: true}]}
        - {op: test, eq: [refund.sales, {const: false}]}
  - id: refund.h_min_line3_line8
    printed: "(helper)"
    label: "Smaller of lines 3 and 8."
    type: NonNegDollars
    expr:
      op: smaller_of
      of: [refund.line3, refund.line8]
  - id: refund.has
    printed: "(helper)"
    label: "Whether any part of the refund is taxable."
    type: Bool
    expr:
      op: test
      gt: [refund.line9, {const: 0}]
  - id: refund.taxable
    printed: "(helper)"
    label: "Taxable part of the refund."
    type: NonNegDollars
    expr:
      op: copy
      from: refund.line9
```
