# Class M hand-work — oi8z

`Schedule 1, line 8z — other income, one entry per item listed` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | a162587c5fa281914595d4a07ce8ba565f22d1b3ef1ea027d615434839d2f909 |
| cases | 1 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 92, 93 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 92, 93 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| p525 | 2025 | 34 | pages named by another document's citation | 7df495537860edb313c70301e591c2a0775567fab771e3d5f9bbb0cbccb69182 | 34 | 27f9e8c0836aae6360658725d1b0db69ecaf91bfa77998e1637b51f92b18df65 |

## Lines

### case classm.oi8z.1 — prompt sha256 56e77980b9205480a926362d1d5eada11f73e5e52b8618cf1cd64168b7de58fc; branches: oi8z.recovery:false, oi8z.additional_tax:false, oi8z.figured:false

### classm.oi8z.1 — oi8z[item_a].recovery — The item is a recovery of an amount deducted in an earlier year
Status: **AGREE**

Value: no

### classm.oi8z.1 — oi8z[item_a].additional_tax — The item carries an additional tax or interest (a charitable deduction recapture
Status: **AGREE**

Value: no

### classm.oi8z.1 — oi8z[item_a].figured — The item's taxable amount is figured under rules this tool does not encode (a co
Status: **AGREE**

Value: no

### classm.oi8z.1 — oi8z[item_a].taxable — The amount of this item included on line 8z
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.oi8z.1

```yaml
lines:
  - printed: "oi8z[item_a].recovery"
    value: "no"
    work: "Kickbacks are payments received (Pub. 525), not reimbursements of items deducted in an earlier year"
  - printed: "oi8z[item_a].additional_tax"
    value: "no"
    work: "Kickbacks are not a charitable deduction recapture or a Coverdell ESA/QTP distribution, so no additional tax or interest applies"
  - printed: "oi8z[item_a].figured"
    value: "no"
    work: "Pub. 525: kickbacks must be included in income on line 8z; no special taxable-part rule applies"
  - printed: "oi8z[item_a].taxable"
    value: "0.00"
    work: "Full amount is included: $0.00"
```
