# Transcription agreement — refund

Second transcription of `State and Local Income Tax Refund Worksheet—Schedule 1, Line 1` by an isolated model (spec 6.5), compared line by line with `forms/2025/refund.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-23 |
| model requested | deepseek-flash |
| model reported | deepseek-flash |
| prompt sha256 | 2c06ed661628b2815c3f5430bbfff5658f6e3e91312848849cb0cf0b5a9d786b |
| prompt policy | source-only-computation-v2 |
| system sha256 | f8e157616efb47ec346ddc26271ad22feb92b5bf2176e505eff5f7058425cef9 |
| reasoning effort | provider default |
| output token budget | 65536 |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | 19b64f2343c301d334f12697341c4e987cb0338554757fa20f2d9aea79795acc |
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

Second transcription's note: The IRS worksheet does not print a separate yes/no result; I encode has as true exactly when the taxable part on line 9 is greater than zero.

Ruling: model error; i1040gi p. 88, Line 1: "If you received a refund, credit, or offset of state or local income taxes in 2025, you may be required to report this amount." refund.has is whether a refund was received (the project tests refund.received > 0, which s1.line1 uses to decide whether to ask anything else); the candidate redefines it as line 9 > 0 and so reads the itemizing questions on every return. Triage executable-triage-v1 (triage/refund.deepseek.json; 1,083 fixtures, 500 generated returns, 295 partial records over 17 bases): 870 of 1,878 comparisons agree. The 981 candidate-unknown records are returns with no refund (classm.f2441.1.deepseek: refund.received $0, project false) on which the candidate requires refund.itemized, which the text does not need. The 6 value differences (stage16.refund.f1, f2, f4, f7, stage16.cleanup.refuse.sa_charity.simultaneous, sa_excluded.simultaneous: a $1,000 refund with refund.itemized false, project true, candidate false) leave Schedule 1 line 1 at zero on both sides, but the candidate then never asks the box 8 and other-year questions the project asks of every refund (amb.2025.refund_exceptions). The 17 project-unknown records withhold refund.received, which the source needs. The 4 candidate-refuses records (stage16.refuse.refund.exc_tax, exc_who, box8, not_2024) are refused by the project on refund.taxable or line 1 under the same gates. Project stands.

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

Ruling: model error; f1099g p. 5, Instructions for Recipient: "Box 8. If this box is checked, the amount in box 2 is attributable to an income tax that applies exclusively to income from a trade or business" and "If taxable, report the amount in box 2 on Schedule C or F (Form 1040), as appropriate"; i1040gi p. 88, TIP: "None of your refund is taxable if, in the year you paid the tax, you either (a) didn't itemize deductions". Neither the box 8 rule nor a refund for a year other than 2024 depends on 2024 itemizing, and the project asks both of every refund (amb.2025.refund_exceptions, chosen reading); the candidate copies its line 9, which puts all four exception gates on line 1 behind the 2024 itemizing test, so it gives zero without asking them. Triage executable-triage-v1 (triage/refund.deepseek.json; 1,083 fixtures, 500 generated returns, 295 partial records over 17 bases): 1,841 of 1,878 agree. The 34 project-unknown records (17 bases each withholding refund.box8 or refund.not_2024, e.g. classm.f8889.2.deepseek with refund.itemized false: project unknown, candidate $0.00) are that omission. The 2 candidate-unknown records are inherited from lines 6 and 9: stage16.mut.refund_single_unasked (single filer, project $1,400.00, candidate needs refund.spouse_born) and stage16.mut.refund_line3_stop (project $0.00 at the line 3 STOP, candidate needs refund.status). The 1 project-refuses record (stage16.refuse.refund.line5e_bad, candidate $3,000.00) is the cited impossible-entry screen refund.line5e_bad (i1040sca p. 7, Line 5e, "enter the smaller of line 5d or $40,000"), scope. Project stands.

### 1 — Enter the income tax refund from Form(s) 1099-G (or similar statement). But don’t enter mo
Status: **DISAGREE**

Project:

```json
{"of": [{"input": "refund.line5d_2024"}, {"input": "refund.received"}], "op": "smaller_of"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "refund.itemized"}], "test": "eq"}, {"args": [{"const": true}, {"input": "refund.sales"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"input": "refund.line5d_2024"}, {"input": "refund.received"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "refund.sales"}], "test": "eq"}, {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The IRS says none of the refund is taxable if you did not itemize or elected general sales taxes; I set line 1 to zero in those cases so that line 9 is zero.

Ruling: representation; i1040gi p. 90, worksheet line 1: "Enter the income tax refund from Form(s) 1099-G (or similar statement). But don't enter more than the amount of your state and local income taxes shown on your 2024 Schedule A, line 5d"; p. 88: the worksheet is used "If the refund was for a tax you paid in 2024 and you deducted state and local income taxes on your 2024 Schedule A". Where the worksheet is used (itemized, no sales-tax election) the candidate takes the same smaller of refund.received and line 5d; it enters zero otherwise, where the project's refund.taxable never reads line 1. Triage executable-triage-v1 (triage/refund.deepseek.json; 1,083 fixtures, 500 generated returns, 295 partial records over 17 bases): 1,791 of 1,878 agree. The 34 project-unknown records (17 bases withholding refund.received or refund.line5d_2024) and the 51 candidate-unknown records (withholding refund.itemized, refund.box8 or refund.not_2024) are partial records on which the candidate yields $0.00, so its eligibility test is false there and the worksheet is not reached; in the interview refund.itemized, box 8 and not_2024 are answered on refund.taxable before line 1 is read. The 2 candidate-refuses records (stage16.refuse.refund.box8, not_2024; project line 1 $3,000.00) are returns the project refuses on refund.taxable under the same gates, scope. No printed amount differs.

### 2 — Subtract the amount on your 2024 Schedule A, line 5e, from the amount of state and local i
Status: **DISAGREE**

Project:

```json
{"from": {"input": "refund.line5d_2024"}, "op": "subtract_floor0", "take": {"input": "refund.line5e_2024"}}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "refund.itemized"}], "test": "eq"}, {"args": [{"const": true}, {"input": "refund.sales"}], "test": "ne"}], "test": "all"}, "then": {"from": {"input": "refund.line5d_2024"}, "op": "subtract_floor0", "take": {"input": "refund.line5e_2024"}}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "refund.sales"}], "test": "eq"}, {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Ruling: representation; i1040gi p. 90, worksheet line 2: "Is the amount ... paid in 2024 (generally, this is the amount reported on your 2024 Schedule A, line 5d) more than the amount on your 2024 Schedule A, line 5e? No. Enter the amount from line 1 on line 3 and go to line 4. Yes. Subtract the amount on your 2024 Schedule A, line 5e". Both take line 5d less line 5e floored at zero where the worksheet is used; the candidate enters zero where it is not. Triage executable-triage-v1 (triage/refund.deepseek.json; 1,083 fixtures, 500 generated returns, 295 partial records over 17 bases): 1,826 of 1,878 agree. The 34 project-unknown (withholding refund.line5d_2024 or refund.line5e_2024) and 17 candidate-unknown (withholding refund.itemized) records are partial records off the worksheet path (candidate $0.00 from its false eligibility test). The 1 project-refuses record (stage16.refuse.refund.line5e_bad, candidate $0.00) is the cited impossible-entry screen (i1040sca p. 7, Line 5e, "enter the smaller of line 5d or $40,000"), scope. Project stands.

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
{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "eq"}, "then": {"input": "refund.line17_2024"}}, {"guard": {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: If there were no 2024 itemized deductions, line 4 is set to zero because the worksheet is not used.

Ruling: representation; i1040gi p. 90, worksheet line 4: "Enter your total itemized deductions from your 2024 Schedule A, line 17." Both enter refund.line17_2024 when 2024 deductions were itemized; the candidate enters zero otherwise, where the worksheet is not used and the project's line 4 is not reached. Triage executable-triage-v1 (triage/refund.deepseek.json; 1,083 fixtures, 500 generated returns, 295 partial records over 17 bases): 1,844 of 1,878 agree; the 17 candidate-unknown records withhold refund.itemized and the 17 project-unknown records withhold refund.line17_2024 on bases where the candidate gives $0.00 (not itemized), all partial records off the worksheet path. Project stands.

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
{"of": [{"alternatives": [{"guard": {"args": [{"const": true}, {"input": "refund.spouse_blind"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "refund.spouse_blind"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "refund.spouse_born"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "refund.spouse_born"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "refund.you_blind"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "refund.you_blind"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": true}, {"input": "refund.you_born"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}, {"guard": {"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "qss"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_married"}}], "op": "choose"}}, {"guard": {"args": [{"const": true}, {"input": "refund.you_born"}], "test": "ne"}, "then": {"const": 0}}], "op": "choose"}], "op": "sum"}
```

Ruling: model error; i1040gi p. 90, worksheet line 6: "Spouse was born before January 2, 1960. Spouse is blind." with "*If your filing status is married filing separately, you can check the boxes for your spouse only if your spouse had no income", and i1040gi p. 33, Line 12d (given to the reviewer): "Don't check any boxes for your spouse if your filing status is head of household". The project asks the spouse boxes only for a 2024 joint or separate return (amb.2025.refund_boxes_2024); the candidate asks refund.spouse_born and refund.spouse_blind of every filer, including single and head of household, answers the text does not need. Triage executable-triage-v1 (triage/refund.deepseek.json; 1,083 fixtures, 500 generated returns, 295 partial records over 17 bases): 1,826 of 1,878 agree. Of the 35 candidate-unknown records, stage16.mut.refund_single_unasked is a single filer (project $0.00, candidate needs refund.spouse_born) and the other 34 withhold a spouse question the project does not ask on that base. The 17 project-unknown records withhold refund.status where no box is checked; the project reads status for line 6 even then, but line 5 needs status whenever line 6 is used (lines 5 to 7 are skipped only for a 2024 separate return, itself a status answer), so this is not a reachable difference. Box amounts and status mapping otherwise agree. Project stands.

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

Second transcription's note: The worksheet's note for married filing separately when the spouse itemized deductions is implemented by copying line 4 to line 8 and bypassing lines 5 through 7.

Ruling: model error; i1040gi p. 90, Note: "If the filing status on your 2024 Form 1040 or 1040-SR was married filing separately and your spouse itemized deductions in 2024, skip lines 5 through 7, enter the amount from line 4 on line 8", and line 8: "Is the amount on line 7 less than the amount on line 4? No. STOP ... Yes. Subtract line 7 from line 4". The candidate's own line 8 logic (copy line 4 for a separate return with an itemizing spouse, else line 4 less line 7 floored) is equivalent to the project's; the differences are inherited. Triage executable-triage-v1 (triage/refund.deepseek.json; 1,083 fixtures, 500 generated returns, 295 partial records over 17 bases): 1,809 of 1,878 agree. Of the 52 candidate-unknown records, stage16.mut.refund_single_unasked (single filer, project $1,400.00) and 34 partial records need the spouse questions of line 6, the model error ruled there; 17 withhold refund.itemized (line 4 guard, off the worksheet path). The 17 project-unknown records withhold refund.line17_2024 on bases not using the worksheet (candidate $0.00). Project stands.

### 9 — Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on Schedule 1,
Status: **DISAGREE**

Project:

```json
{"alternatives": [{"guard": {"args": [{"line": "1"}, {"line": "2"}], "test": "le"}, "then": {"const": 0}}, {"guard": {"args": [{"line": "2"}, {"line": "1"}], "test": "lt"}, "then": {"of": [{"line": "3"}, {"line": "8"}], "op": "smaller_of"}}], "op": "choose"}
```

Second:

```json
{"alternatives": [{"guard": {"args": [{"args": [{"const": true}, {"input": "refund.itemized"}], "test": "eq"}, {"args": [{"const": true}, {"input": "refund.sales"}], "test": "ne"}], "test": "all"}, "then": {"of": [{"line": "3"}, {"line": "8"}], "op": "smaller_of"}}, {"guard": {"args": [{"args": [{"const": true}, {"input": "refund.sales"}], "test": "eq"}, {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The STOP conditions on lines 3 and 8 are carried into zero through subtract_floor0 and the smaller of line 3 or line 8.

Ruling: model error; i1040gi p. 90, worksheet line 3: "Is the amount on line 1 more than the amount on line 2? No. STOP None of your refund is taxable." The project stops at line 3 (refund.line3_more false gives zero without lines 4 to 8); the candidate always takes the smaller of line 3 and line 8, so after a line 3 STOP it still needs line 8 and the 2024 filing status, which the text does not need, and it inherits the line 6 spouse questions. Triage executable-triage-v1 (triage/refund.deepseek.json; 1,083 fixtures, 500 generated returns, 295 partial records over 17 bases): 1,771 of 1,878 agree. Candidate-unknown 19: stage16.mut.refund_line3_stop (project $0.00, candidate needs refund.status), stage16.mut.refund_single_unasked (project $1,400.00, needs refund.spouse_born), and 17 partial records withholding refund.itemized, which the project answers on refund.taxable before line 9. Project-unknown 85: 17 bases each withholding refund.received, refund.exc_tax, refund.exc_who, refund.line5d_2024 or refund.line5e_2024 where the candidate gives $0.00 (not itemized), so the project's refund.taxable takes zero without line 9. Candidate-refuses 2 (stage16.refuse.refund.box8, not_2024; project line 9 $0.00) are refused by the project on refund.taxable, scope; project-refuses 1 (stage16.refuse.refund.line5e_bad, candidate $3,000.00) is the cited impossible-entry screen (i1040sca p. 7, Line 5e), scope. Project stands.

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| refund.has | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 |
| refund.taxable | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | - |
| 1 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.not_2024 |
| 3 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.not_2024 |
| 9 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.not_2024 |

## Raw second transcription

```yaml
lines:
  - id: refund.line1
    printed: "1"
    label: "Enter the income tax refund from Form(s) 1099-G (or similar statement). But don’t enter more than the amount of your state and local income taxes shown on your 2024 Schedule A, line 5d."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.h_eligible_initial, {const: true}]}
          then: refund.h_line1_amount
        - guard: {op: test, not: {op: test, eq: [refund.h_eligible_initial, {const: true}]}}
          then: refund.h_zero
    refuses: [refund.box8, refund.not_2024, refund.exc_tax, refund.exc_who]
    note: "The IRS says none of the refund is taxable if you did not itemize or elected general sales taxes; I set line 1 to zero in those cases so that line 9 is zero."
  - id: refund.line2
    printed: "2"
    label: "Is the amount of state and local income taxes (or general sales taxes), real estate taxes, and personal property taxes paid in 2024 (generally, this is the amount reported on your 2024 Schedule A, line 5d) more than the amount on your 2024 Schedule A, line 5e?"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.h_eligible_initial, {const: true}]}
          then: refund.h_line2_amount
        - guard: {op: test, not: {op: test, eq: [refund.h_eligible_initial, {const: true}]}}
          then: refund.h_zero
  - id: refund.line3
    printed: "3"
    label: "Is the amount on line 1 more than the amount on line 2? No. STOP None of your refund is taxable. Yes. Subtract line 2 from line 1."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: refund.line1, take: refund.line2}
    note: "The STOP case on line 3 is carried to zero by subtract_floor0."
  - id: refund.line4
    printed: "4"
    label: "Enter your total itemized deductions from your 2024 Schedule A, line 17."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.itemized, {const: true}]}
          then: refund.h_line4_amount
        - guard: {op: test, not: {op: test, eq: [refund.itemized, {const: true}]}}
          then: refund.h_zero
    note: "If there were no 2024 itemized deductions, line 4 is set to zero because the worksheet is not used."
  - id: refund.line5
    printed: "5"
    label: "Enter the amount shown below for the filing status claimed on your 2024 Form 1040 or 1040-SR. Single or married filing separately—$14,600; Married filing jointly or qualifying surviving spouse—$29,200; Head of household—$21,900."
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
  - id: refund.line6
    printed: "6"
    label: "Check any boxes that apply. No boxes checked. Enter -0-. Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)."
    type: NonNegDollars
    expr: {op: sum, of: [refund.h_box_you_born, refund.h_box_you_blind, refund.h_box_spouse_born, refund.h_box_spouse_blind]}
  - id: refund.line7
    printed: "7"
    label: "Add lines 5 and 6."
    type: NonNegDollars
    expr: {op: sum, of: [refund.line5, refund.line6]}
  - id: refund.line8
    printed: "8"
    label: "Is the amount on line 7 less than the amount on line 4? No. STOP None of your refund is taxable. Yes. Subtract line 7 from line 4."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.h_skip, {const: true}]}
          then: refund.line4
        - guard: {op: test, not: {op: test, eq: [refund.h_skip, {const: true}]}}
          then: refund.h_line8_normal
    note: "The worksheet's note for married filing separately when the spouse itemized deductions is implemented by copying line 4 to line 8 and bypassing lines 5 through 7."
  - id: refund.line9
    printed: "9"
    label: "Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on Schedule 1, line 1."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.h_eligible_initial, {const: true}]}
          then: refund.h_line9_amount
        - guard: {op: test, not: {op: test, eq: [refund.h_eligible_initial, {const: true}]}}
          then: refund.h_zero
    note: "The STOP conditions on lines 3 and 8 are carried into zero through subtract_floor0 and the smaller of line 3 or line 8."
  - id: refund.h_zero
    printed: "(helper)"
    label: "Zero amount."
    type: NonNegDollars
    expr: {op: param, ref: sales.zero}
  - id: refund.h_std_single
    printed: "(helper)"
    label: "Standard deduction amount for single or married filing separately on the 2024 return."
    type: NonNegDollars
    expr: {op: param, ref: refund.std_single}
  - id: refund.h_std_joint
    printed: "(helper)"
    label: "Standard deduction amount for married filing jointly or qualifying surviving spouse on the 2024 return."
    type: NonNegDollars
    expr: {op: param, ref: refund.std_joint}
  - id: refund.h_std_hoh
    printed: "(helper)"
    label: "Standard deduction amount for head of household on the 2024 return."
    type: NonNegDollars
    expr: {op: param, ref: refund.std_hoh}
  - id: refund.h_box_married
    printed: "(helper)"
    label: "Amount per checked box if the 2024 filing status was neither single nor head of household."
    type: NonNegDollars
    expr: {op: param, ref: refund.box_married}
  - id: refund.h_box_unmarried
    printed: "(helper)"
    label: "Amount per checked box if the 2024 filing status was single or head of household."
    type: NonNegDollars
    expr: {op: param, ref: refund.box_unmarried}
  - id: refund.h_eligible_initial
    printed: "(helper)"
    label: "Whether the refund worksheet can reach a taxable amount: 2024 deductions were itemized and general sales taxes were not elected."
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [refund.itemized, {const: true}]}
        - {op: test, not: {op: test, eq: [refund.sales, {const: true}]}}
  - id: refund.h_line1_amount
    printed: "(helper)"
    label: "Line 1 before applying the no-itemize or sales-tax election stop."
    type: NonNegDollars
    expr: {op: smaller_of, of: [refund.received, refund.line5d_2024]}
  - id: refund.h_line2_amount
    printed: "(helper)"
    label: "Line 2 subtraction when 2024 Schedule A line 5d is more than line 5e."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: refund.line5d_2024, take: refund.line5e_2024}
  - id: refund.h_line4_amount
    printed: "(helper)"
    label: "2024 total itemized deductions before applying the no-itemize stop."
    type: NonNegDollars
    expr: {op: copy, from: refund.line17_2024}
  - id: refund.h_box_amount
    printed: "(helper)"
    label: "Amount per checked box for the 2024 filing status."
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
            any:
              - {op: test, eq: [refund.status, {const: "mfs"}]}
              - {op: test, eq: [refund.status, {const: "mfj"}]}
              - {op: test, eq: [refund.status, {const: "qss"}]}
          then: refund.h_box_married
  - id: refund.h_box_you_born
    printed: "(helper)"
    label: "Amount for the box that the taxpayer was born before January 2, 1960."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.you_born, {const: true}]}
          then: refund.h_box_amount
        - guard: {op: test, not: {op: test, eq: [refund.you_born, {const: true}]}}
          then: refund.h_zero
  - id: refund.h_box_you_blind
    printed: "(helper)"
    label: "Amount for the box that the taxpayer was blind."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.you_blind, {const: true}]}
          then: refund.h_box_amount
        - guard: {op: test, not: {op: test, eq: [refund.you_blind, {const: true}]}}
          then: refund.h_zero
  - id: refund.h_box_spouse_born
    printed: "(helper)"
    label: "Amount for the box that the spouse was born before January 2, 1960."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.spouse_born, {const: true}]}
          then: refund.h_box_amount
        - guard: {op: test, not: {op: test, eq: [refund.spouse_born, {const: true}]}}
          then: refund.h_zero
  - id: refund.h_box_spouse_blind
    printed: "(helper)"
    label: "Amount for the box that the spouse was blind."
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.spouse_blind, {const: true}]}
          then: refund.h_box_amount
        - guard: {op: test, not: {op: test, eq: [refund.spouse_blind, {const: true}]}}
          then: refund.h_zero
  - id: refund.h_line8_normal
    printed: "(helper)"
    label: "Line 8 subtraction when the married-filing-separately spouse-itemized skip does not apply."
    type: NonNegDollars
    expr: {op: subtract_floor0, from: refund.line4, take: refund.line7}
  - id: refund.h_skip
    printed: "(helper)"
    label: "Whether the 2024 filing status was married filing separately and the spouse itemized deductions."
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [refund.status, {const: "mfs"}]}
        - {op: test, eq: [refund.mfs_spouse_itemized, {const: true}]}
  - id: refund.h_line9_amount
    printed: "(helper)"
    label: "Smaller of line 3 or line 8 before applying the no-itemize or sales-tax election stop."
    type: NonNegDollars
    expr: {op: smaller_of, of: [refund.line3, refund.line8]}
  - id: refund.taxable
    printed: "(helper)"
    label: "Taxable part of the refund from line 9, for Schedule 1, line 1."
    type: NonNegDollars
    expr: {op: copy, from: refund.line9}
  - id: refund.has
    printed: "(helper)"
    label: "Whether any part of the refund is taxable (line 9 greater than zero)."
    type: Bool
    expr: {op: test, gt: [refund.taxable, refund.h_zero]}
    note: "The IRS worksheet does not print a separate yes/no result; I encode has as true exactly when the taxable part on line 9 is greater than zero."
```
