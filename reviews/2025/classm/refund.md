# Class M hand-work — refund

`State and Local Income Tax Refund Worksheet—Schedule 1, Line 1` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | 87e6772baead59e830f3aa998aa288dcdd3ce5050bb6bc21d308a76d6f27320a |
| cases | 1 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 33, 88, 89, 90 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 33, 88, 89 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f1099g | Rev. March 2024 (continuous-use form for calendar year 2025; the December 2026 revision is first used for 2026) | 1, 2, 3, 4, 5, 6 | whole document | c3505294585e00ec5e957f73aa97dee32ad4b6916cd3eb48fef7f3c79f123270 | 5 | 49cc781de5cf6d881cc347361880de4b4b20fca0f13397bc94c94e84a20cff6d |
| i1040sca | 2025; printed date 2025-12-08 | 7 | cited pages | 18001c3e295230bbac198d1982e4c52265139aa983ef9cb9fb69d2a41a06119b | - | 5e2e018247f585c4ecb192b2c1a75e444bbf96b9653026722bc9720d70cc114c |
| p525 | 2025 | 24 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 24 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

## Lines

### case classm.refund.1 — prompt sha256 1e966a46ec241b5438a780c4258facd244a806ace73418a5849e623bb216f55d; branches: refund.has:false, refund.box8:false, refund.not_2024:false, refund.itemized:false, refund.sales:false, refund.worksheet:false, refund.exc_tax:false, refund.exc_who:false, refund.line5e_bad:false, refund.line1:left, refund.line2_more:false, refund.line2:floor, refund.line3_more:false, refund.line3:floor, refund.mfs_spouse_itemized:false, refund.line5#0, refund.per_box#0, refund.you_born:false, refund.you_blind:false, refund.spouse_born:false, refund.spouse_blind:false, refund.spouse_boxes:false, refund.amt_you_born#1, refund.amt_you_blind#1, refund.amt_spouse_born#0, refund.amt_spouse_born_checked#1, refund.amt_spouse_blind#0, refund.amt_spouse_blind_checked#1, refund.line8_figured:floor, refund.line8#0, refund.line8_mfs#1, refund.line9_figured:left, refund.line9#0, refund.taxable#0

### classm.refund.1 — 1 — Enter the income tax refund from Form(s) 1099-G (or similar statement). But don’
Status: **AGREE**

Value: $0.00

### classm.refund.1 — 2 — Subtract the amount on your 2024 Schedule A, line 5e, from the amount of state a
Status: **AGREE**

Value: $0.00

### classm.refund.1 — 3 — Subtract line 2 from line 1
Status: **AGREE**

Value: $0.00

### classm.refund.1 — 4 — Enter your total itemized deductions from your 2024 Schedule A, line 17
Status: **AGREE**

Value: $0.00

### classm.refund.1 — 5 — Enter the amount shown below for the filing status claimed on your 2024 Form 104
Status: **AGREE**

Value: $14,600.00

### classm.refund.1 — 6 — Check any boxes that apply. Multiply the number of boxes checked by $1,550 ($1,9
Status: **AGREE**

Value: $0.00

### classm.refund.1 — 7 — Add lines 5 and 6
Status: **AGREE**

Value: $14,600.00

### classm.refund.1 — 8 — Subtract line 7 from line 4 (if your 2024 filing status was married filing separ
Status: **AGREE**

Value: $0.00

### classm.refund.1 — 9 — Taxable part of your refund. Enter the smaller of line 3 or line 8 here and on S
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.refund.1

```yaml
```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "1099-G box 2 refunds $0.00, which is under the 2024 Sch A line 5d limit of $0.00"
  - printed: "2"
    value: ""
    work: "Is 2024 line 5d ($0.00) more than line 5e ($0.00)? No, so skip line 2, enter line 1 on line 3, and go to line 4"
  - printed: "3"
    value: "0.00"
    work: "Line 2 answer was No, so the amount from line 1 is entered: $0.00"
  - printed: "4"
    value: "0.00"
    work: "2024 Sch A line 17 total itemized deductions = $0.00"
  - printed: "5"
    value: "14600.00"
    work: "2024 filing status Single, so $14,600"
  - printed: "6"
    value: "0.00"
    work: "No boxes checked (not born before 1/2/1960 and not blind; no spouse boxes), so -0-"
  - printed: "7"
    value: "14600.00"
    work: "14,600.00 + 0.00 = 14,600.00"
  - printed: "8"
    value: ""
    work: "Is line 7 ($14,600) less than line 4 ($0)? No, so STOP: none of the refund is taxable"
  - printed: "9"
    value: ""
    work: "Not reached because the worksheet stopped at line 8; the taxable refund is zero"
```
```
