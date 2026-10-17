# Class M hand-work — gift

`Form 8283 — groups of similar noncash property` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 1 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i8283 | December 2025; printed date 2026-01-30 | 1, 2, 3 | cited pages | cd582a9f231564c755d552a21d937b33e24df8b9fe65f4f823b7c9eca9dfe1ad | 1, 2, 3 | 53a4b54ff613d5c600c1af7ba5bf9024418fe89441ae8d629a955bd59aa6e3c7 |

## Lines

### case classm.gift.1 — prompt sha256 078fb5ed76d23ec9268090e3c9b63f9eeeaa24f9301478b059df2ca3d622e5c2; branches: gift.public_securities:false, gift.public_securities:true, gift.special:false, gift.section_b:false

### classm.gift.1 — gift[item_a].section_b — Appraisal threshold: non-publicly-traded group over $5,000
Status: **AGREE**

Value: no

### classm.gift.1 — gift[item_a].allowed — Amount from gift.deduction
Status: **AGREE**

Value: $4,087.00

### classm.gift.1 — gift[item_b].section_b — Appraisal threshold: non-publicly-traded group over $5,000
Status: **AGREE**

Value: no

### classm.gift.1 — gift[item_b].allowed — Amount from gift.deduction
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.gift.1

```yaml
lines:
  - printed: "gift[item_a].section_b"
    value: "no"
    work: "Not publicly traded, no special treatment; deduction $4,087.00 is not more than $5,000, so Section A (i8283 Which Sections To Complete)"
  - printed: "gift[item_a].allowed"
    value: "4087.00"
    work: "Deduction before income limits as given = $4,087.00"
  - printed: "gift[item_b].section_b"
    value: "no"
    work: "Publicly traded securities go in Section A regardless of amount; deduction $0.00 is also not over $5,000"
  - printed: "gift[item_b].allowed"
    value: "0.00"
    work: "Deduction before income limits as given = $0.00"
```
