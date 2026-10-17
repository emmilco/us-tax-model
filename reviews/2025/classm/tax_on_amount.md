# Class M hand-work — tax_on_amount

`Tax on an amount — Tax Table or Tax Computation Worksheet` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 2 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 68, 80 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.tax_on_amount.1 — prompt sha256 52d5b22061f379ab1726ad80f3cd928d248ef426b8c92eaf46dd6ece271b493b; branches: below_boundary:false, tax#1

### classm.tax_on_amount.1 — below_boundary — Is the amount less than $100,000?
Status: **AGREE**

Value: no

### classm.tax_on_amount.1 — tax — Tax on the amount
Status: **AGREE**

Value: $84,781.45

### case classm.tax_on_amount.2 — prompt sha256 604571736c7c7a70a9ea2f8e315d3c6e2f0c2f66fad8fe62d71e2f55dd65e68e; branches: below_boundary:true, tax#0

### classm.tax_on_amount.2 — below_boundary — Is the amount less than $100,000?
Status: **AGREE**

Value: yes

### classm.tax_on_amount.2 — tax — Tax on the amount
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.tax_on_amount.1

```yaml
```yaml
lines:
  - printed: "below_boundary"
    value: "no"
    work: "334,207.00 is not less than 100,000, so the Tax Computation Worksheet applies, not the Tax Table"
  - printed: "tax"
    value: "84781.45"
    work: "Section D, row over 250,500 but not over 626,350: 334,207.00 x 0.35 = 116,972.45; 116,972.45 - 32,191.00 = 84,781.45"
```
```

### classm.tax_on_amount.2

```yaml
lines:
  - printed: "below_boundary"
    value: "yes"
    work: "$0.00 < $100,000, so use Tax Table, not Tax Computation Worksheet"
  - printed: "tax"
    value: "0.00"
    work: "Tax Table row at least 0 but less than 5, MFS column: 0"
```
