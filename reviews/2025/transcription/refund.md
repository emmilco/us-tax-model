# Transcription agreement — refund

Second transcription of `State and Local Income Tax Refund Worksheet—Schedule 1, Line 1` by an isolated model (spec 6.5), compared line by line with `forms/2025/refund.yaml`.

| field | value |
| --- | --- |
| date | 2026-10-30 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
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
| output token budget | transport default (65536 for DeepSeek) |
| interface normalization | a definition's own namespace prefix may be removed from exact published ids; raw response unchanged |
| subject sha256 | fa2340bf10b343c4d737d5266a44774128963c71af1a288bb6c011108890e372 |
| printed lines compared | 11 |
| agree / disagree / missing | 8 / 3 / 0 |
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
{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": false}, {"input": "refund.sales"}], "test": "eq"}, {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "eq"}], "test": "all"}, {"args": [{"const": 0}, {"input": "refund.received"}], "test": "lt"}], "test": "all"}, "then": {"line": "9"}}, {"guard": {"args": [{"args": [{"args": [{"args": [{"const": false}, {"input": "refund.sales"}], "test": "ne"}, {"args": [{"const": true}, {"input": "refund.itemized"}], "test": "ne"}], "test": "any"}, {"args": [{"const": 0}, {"input": "refund.received"}], "test": "lt"}], "test": "all"}, {"args": [{"input": "refund.received"}, {"const": 0}], "test": "le"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}
```

Second transcription's note: The pages do not define this interface name. Chosen reading: the amount for Schedule 1, line 1, which is zero with no refund, zero when the tax was not deducted on the 2024 Schedule A, and otherwise worksheet line 9.

Ruling: representation and scope; i1040gi p. 88, Line 1, TIP: "None of your refund is taxable if, in the year you paid the tax, you either (a) didn’t itemize deductions, or (b) elected to deduct state and local general sales taxes instead of state and local income taxes"; f1099g p. 5, Box 8: "If taxable, report the amount in box 2 on Schedule C or F (Form 1040), as appropriate". executable-triage-v2 (`reviews/2025/transcription/triage/refund.json`; 1,382 fixtures, 500 generated returns seed 20261026, 640 partial records from 40 bases; 2,522 comparisons; every witness enumerated by an uncapped scratch rerun of tools/transcription/triage.mjs, the record keeps 6 per kind): 1,242 of 2,522 agree; 1,239 project-unknown (524 completed), 40 candidate-unknown (none completed), 1 project-refuses. The candidate gives zero without a refund, zero when the 2024 tax was not deducted on Schedule A (itemized and no sales-tax election), and line 9 otherwise, the project's choice on refund.worksheet; it places the box 8 and other-year gates on its not-deducted branch and all four exception gates on line 1, so every refund meets box 8 and refund.not_2024 on both sides and exc_tax/exc_who only where the worksheet is used, as the project does. All 1,239 project-unknown records are returns with no refund (candidate refund.has false, $0.00): 1,119 fixtures (476 completed, for example classm.f2441.1.deepseek) and 120 partial records withholding refund.box8, refund.not_2024 or refund.itemized (48 completed); the project's line reads the box 8 gate there, but s1.line1 reads refund.taxable only when refund.has (refund.received more than zero) is true (forms/2025/s1.yaml), and every partial base of the bank has no refund (refund.has false), so the line is never read on them. The 40 candidate-unknown records withhold refund.received, which s1.line1 needs through refund.has on both sides. The project-refuses record (stage16.refuse.refund.line5e_bad, candidate $3,000.00) is the cited impossible-entry screen refund.line5e_bad (i1040sca p. 7, Line 5e, "enter the smaller of line 5d or $40,000"): scope. The reworded gates (BUG-0230 refund.not_2024, BUG-0251 refund.box8) change no expression; no completed return differs. Project stands.

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
{"of": [{"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "refund.spouse_blind"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "ne"}], "test": "all"}, "then": {"param": "refund.box_married"}}, {"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "refund.spouse_blind"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, {"args": [{"const": true}, {"input": "refund.spouse_born"}], "test": "eq"}], "test": "all"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "ne"}], "test": "all"}, "then": {"param": "refund.box_married"}}, {"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}], "op": "choose"}}, {"guard": {"args": [{"args": [{"args": [{"const": "mfj"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": "mfs"}, {"input": "refund.status"}], "test": "ne"}], "test": "all"}, {"args": [{"const": true}, {"input": "refund.spouse_born"}], "test": "ne"}], "test": "any"}, "then": {"const": 0}}], "op": "choose"}, {"of": [{"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.you_blind"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.you_blind"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "ne"}], "test": "all"}, "then": {"param": "refund.box_married"}}, {"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}], "op": "choose"}}], "op": "choose"}, {"alternatives": [{"guard": {"args": [{"const": false}, {"input": "refund.you_born"}], "test": "eq"}, "then": {"const": 0}}, {"guard": {"args": [{"const": true}, {"input": "refund.you_born"}], "test": "eq"}, "then": {"alternatives": [{"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "ne"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "ne"}], "test": "all"}, "then": {"param": "refund.box_married"}}, {"guard": {"args": [{"args": [{"const": "hoh"}, {"input": "refund.status"}], "test": "eq"}, {"args": [{"const": "single"}, {"input": "refund.status"}], "test": "eq"}], "test": "any"}, "then": {"param": "refund.box_unmarried"}}], "op": "choose"}}], "op": "choose"}], "op": "sum"}], "op": "sum"}
```

Second transcription's note: The grammar has no way to count Bool answers, so the product is written as one per-box amount for each checked box, which gives the same result.

Ruling: representation; i1040gi p. 90, worksheet line 6: "Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)" and footnote "*If your filing status is married filing separately, you can check the boxes for your spouse only if your spouse had no income, isn’t filing a return, and can’t be claimed as a dependent on another person’s return"; p. 33, Line 12d: "Don’t check any boxes for your spouse if your filing status is head of household". executable-triage-v2 (`reviews/2025/transcription/triage/refund.json`; 1,382 fixtures, 500 generated returns seed 20261026, 640 partial records from 40 bases; 2,522 comparisons; every witness enumerated by an uncapped scratch rerun of tools/transcription/triage.mjs, the record keeps 6 per kind): 2,482 of 2,522 agree; 40 project-unknown (16 completed), all partial records withholding refund.status on no-refund bases. The candidate counts the spouse boxes only for a 2024 joint or separate return, as the project does (amb.2025.refund_boxes_2024), at $1,550 per box or $1,950 for single or head of household, and the sum of per-box amounts equals the count times the amount; the earlier qualifying-surviving-spouse difference is gone. The project reads the status before the boxes, the candidate only when a box is checked; line 6 is read only through line 7, and line 5 needs the 2024 status whenever line 7 is, so the difference is not reachable. Project stands.

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

Ruling: representation; i1040gi p. 90, Note: "If the filing status on your 2024 Form 1040 or 1040-SR was married filing separately and your spouse itemized deductions in 2024, skip lines 5 through 7, enter the amount from line 4 on line 8", and line 8: "Yes. Subtract line 7 from line 4" (the No branch, "STOP None of your refund is taxable", is the zero floor). executable-triage-v2 (`reviews/2025/transcription/triage/refund.json`; 1,382 fixtures, 500 generated returns seed 20261026, 640 partial records from 40 bases; 2,522 comparisons; every witness enumerated by an uncapped scratch rerun of tools/transcription/triage.mjs, the record keeps 6 per kind): 2,522 of 2,522 agree. Both give line 4 for a 2024 separate return with an itemizing spouse and line 4 less line 7, not below zero, otherwise; the project splits by filing status first. Same reading as the archived ruling. Project stands.

### 9 — Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on Schedule 1,
Status: **AGREE**

## Refusal gates listed by the second transcription

Reported, not judged: the project often refuses before a worksheet is used, on the line that chooses it, which a per-line comparison cannot see.

| line | gates listed | not read by the project's line |
| --- | --- | --- |
| refund.taxable | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | - |
| 1 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.not_2024 |
| 3 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.not_2024 |
| 9 | refund.box8, refund.exc_tax, refund.exc_who, refund.not_2024 | refund.box8, refund.not_2024 |

## Raw second transcription

```yaml
```yaml
lines:
  - id: refund.has
    printed: "(helper)"
    label: "You received a refund, credit, or offset of state or local income taxes in 2025"
    type: Bool
    expr: {op: test, gt: [refund.received, {const: 0}]}
    note: "The pages do not define this interface name. Chosen reading: true when the amount of refunds, credits or offsets received is more than zero."
  - id: refund.h_zero
    printed: "(helper)"
    label: "Zero"
    type: NonNegDollars
    expr: {op: param, ref: ss.zero}
  - id: refund.h_deducted
    printed: "(helper)"
    label: "In the year you paid the tax you itemized deductions and did not elect to deduct state and local general sales taxes instead of state and local income taxes"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [refund.itemized, {const: true}]}
        - {op: test, eq: [refund.sales, {const: false}]}
  - id: refund.line1
    printed: "1"
    label: "Enter the income tax refund from Form(s) 1099-G (or similar statement). But don't enter more than the amount of your state and local income taxes shown on your 2024 Schedule A, line 5d"
    type: NonNegDollars
    expr: {op: smaller_of, of: [refund.received, refund.line5d_2024]}
    refuses: [refund.box8, refund.not_2024, refund.exc_tax, refund.exc_who]
    note: "Line 5d adds income or sales taxes, real estate taxes and personal property taxes, so 'state and local income taxes shown on line 5d' is open. The closed interface supplies only the line 5d total, so the cap uses that total."
  - id: refund.line2
    printed: "2"
    label: "Is the amount of state and local income taxes (or general sales taxes), real estate taxes, and personal property taxes paid in 2024 (generally, your 2024 Schedule A, line 5d) more than the amount on your 2024 Schedule A, line 5e? No: enter the amount from line 1 on line 3 and go to line 4. Yes: subtract line 5e from that amount"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: refund.line5d_2024, take: refund.line5e_2024}
    note: "The No branch leaves line 2 without an entry. It is represented as zero, so line 3 equals line 1 as the worksheet directs."
  - id: refund.line3
    printed: "3"
    label: "Is the amount on line 1 more than the amount on line 2? No: STOP, none of your refund is taxable. Yes: subtract line 2 from line 1"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: refund.line1, take: refund.line2}
  - id: refund.line4
    printed: "4"
    label: "Enter your total itemized deductions from your 2024 Schedule A, line 17"
    type: NonNegDollars
    expr: {op: copy, from: refund.line17_2024}
  - id: refund.h_mfs_skip
    printed: "(helper)"
    label: "The filing status on your 2024 Form 1040 or 1040-SR was married filing separately and your spouse itemized deductions in 2024"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [refund.status, {const: "mfs"}]}
        - {op: test, eq: [refund.mfs_spouse_itemized, {const: true}]}
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
    label: "Amount for each box checked: $1,550 ($1,950 if your 2024 filing status was single or head of household)"
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
  - id: refund.h_has_spouse
    printed: "(helper)"
    label: "The 2024 filing status allows boxes for a spouse (married filing jointly or married filing separately)"
    type: Bool
    expr:
      op: test
      any:
        - {op: test, eq: [refund.status, {const: "mfj"}]}
        - {op: test, eq: [refund.status, {const: "mfs"}]}
    note: "The worksheet does not say which statuses may check spouse boxes. Chosen reading, following the Form 1040 line 12d instructions: spouse boxes count only for joint and married-filing-separately filers."
  - id: refund.h_you_born
    printed: "(helper)"
    label: "Amount for the box: You were born before January 2, 1960"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.you_born, {const: true}]}
          then: refund.h_box_amount
        - guard: {op: test, eq: [refund.you_born, {const: false}]}
          then: refund.h_zero
  - id: refund.h_you_blind
    printed: "(helper)"
    label: "Amount for the box: You are blind"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.you_blind, {const: true}]}
          then: refund.h_box_amount
        - guard: {op: test, eq: [refund.you_blind, {const: false}]}
          then: refund.h_zero
  - id: refund.h_spouse_born_box
    printed: "(helper)"
    label: "The box is checked: Spouse was born before January 2, 1960"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [refund.h_has_spouse, {const: true}]}
        - {op: test, eq: [refund.spouse_born, {const: true}]}
  - id: refund.h_spouse_born
    printed: "(helper)"
    label: "Amount for the box: Spouse was born before January 2, 1960"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.h_spouse_born_box, {const: true}]}
          then: refund.h_box_amount
        - guard: {op: test, eq: [refund.h_spouse_born_box, {const: false}]}
          then: refund.h_zero
  - id: refund.h_spouse_blind_box
    printed: "(helper)"
    label: "The box is checked: Spouse is blind"
    type: Bool
    expr:
      op: test
      all:
        - {op: test, eq: [refund.h_has_spouse, {const: true}]}
        - {op: test, eq: [refund.spouse_blind, {const: true}]}
  - id: refund.h_spouse_blind
    printed: "(helper)"
    label: "Amount for the box: Spouse is blind"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.h_spouse_blind_box, {const: true}]}
          then: refund.h_box_amount
        - guard: {op: test, eq: [refund.h_spouse_blind_box, {const: false}]}
          then: refund.h_zero
  - id: refund.h_boxes_first
    printed: "(helper)"
    label: "Amounts for the boxes about you"
    type: NonNegDollars
    expr: {op: sum, of: [refund.h_you_born, refund.h_you_blind]}
  - id: refund.line6
    printed: "6"
    label: "Check any boxes that apply. No boxes checked: enter -0-. Multiply the number of boxes checked by $1,550 ($1,950 if your 2024 filing status was single or head of household)"
    type: NonNegDollars
    expr: {op: sum, of: [refund.h_boxes_first, refund.h_spouse_born, refund.h_spouse_blind]}
    note: "The grammar has no way to count Bool answers, so the product is written as one per-box amount for each checked box, which gives the same result."
  - id: refund.line7
    printed: "7"
    label: "Add lines 5 and 6"
    type: NonNegDollars
    expr: {op: sum, of: [refund.line5, refund.line6]}
  - id: refund.h_line4_less_7
    printed: "(helper)"
    label: "Is the amount on line 7 less than the amount on line 4? No: STOP, none of your refund is taxable. Yes: subtract line 7 from line 4"
    type: NonNegDollars
    expr: {op: subtract_floor0, from: refund.line4, take: refund.line7}
  - id: refund.line8
    printed: "8"
    label: "Is the amount on line 7 less than the amount on line 4? No: STOP, none of your refund is taxable. Yes: subtract line 7 from line 4. (If married filing separately and your spouse itemized deductions in 2024, skip lines 5 through 7 and enter the amount from line 4 on line 8.)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.h_mfs_skip, {const: true}]}
          then: refund.line4
        - guard: {op: test, eq: [refund.h_mfs_skip, {const: false}]}
          then: refund.h_line4_less_7
  - id: refund.h_smaller
    printed: "(helper)"
    label: "The smaller of line 3 or line 8"
    type: NonNegDollars
    expr: {op: smaller_of, of: [refund.line3, refund.line8]}
  - id: refund.line9
    printed: "9"
    label: "Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on Schedule 1, line 1"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, gt: [refund.line1, refund.line2]}
          then: refund.h_smaller
        - guard:
            op: test
            not: {op: test, gt: [refund.line1, refund.line2]}
          then: refund.h_zero
    note: "The line 3 STOP gives zero here without reading lines 4 to 8. The line 8 STOP makes line 8 zero, so the smaller amount is zero."
  - id: refund.h_not_deducted
    printed: "(helper)"
    label: "None of your refund is taxable if, in the year you paid the tax, you either (a) didn't itemize deductions, or (b) elected to deduct state and local general sales taxes instead of state and local income taxes"
    type: NonNegDollars
    expr: {op: copy, from: refund.h_zero}
    refuses: [refund.box8, refund.not_2024]
    note: "The answers about 2024 do not settle a refund for another tax year or a refund of a tax on trade or business income, so those two screens also apply here. The refund.exc_tax and refund.exc_who screens apply only where the worksheet is used, so they are listed on line 1."
  - id: refund.taxable
    printed: "(helper)"
    label: "Taxable refunds, credits, or offsets of state and local income taxes (Schedule 1, line 1)"
    type: NonNegDollars
    expr:
      op: choose
      alternatives:
        - guard: {op: test, eq: [refund.has, {const: false}]}
          then: refund.h_zero
        - guard:
            op: test
            all:
              - {op: test, eq: [refund.has, {const: true}]}
              - {op: test, eq: [refund.h_deducted, {const: false}]}
          then: refund.h_not_deducted
        - guard:
            op: test
            all:
              - {op: test, eq: [refund.has, {const: true}]}
              - {op: test, eq: [refund.h_deducted, {const: true}]}
          then: refund.line9
    note: "The pages do not define this interface name. Chosen reading: the amount for Schedule 1, line 1, which is zero with no refund, zero when the tax was not deducted on the 2024 Schedule A, and otherwise worksheet line 9."
```
```
