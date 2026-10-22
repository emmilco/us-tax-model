# Class M hand-work — ltc

`Form 7206, line 2 — qualified long-term care insurance, one per person covered` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | 7caf324abc51fb605d8006837146c5a18c8103e6a0993368765c0660852d97f0 |
| cases | 2 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |

## Lines

### case classm.ltc.1 — prompt sha256 5e90a485bacbe1215316664400d365742eba13d0a5da7fda45c0a29366c8fa26; branches: ltc.amount:right

### classm.ltc.1 — person[taxpayer].sc[biz_a].ltc[self].limit — The amount for that person's age
Status: **AGREE**

Value: $900.00

### classm.ltc.1 — person[taxpayer].sc[biz_a].ltc[self].amount — The smaller of (a) or (b)
Status: **AGREE**

Value: $900.00

### case classm.ltc.2 — prompt sha256 123fb8bfcfdb11241d38a2077a22dddad4d2fef3d7d3aace48305fa071a40633; branches: ltc.amount:left

### classm.ltc.2 — person[taxpayer].sc[biz_a].ltc[self].limit — The amount for that person's age
Status: **AGREE**

Value: $900.00

### classm.ltc.2 — person[taxpayer].sc[biz_a].ltc[self].amount — The smaller of (a) or (b)
Status: **AGREE**

Value: $90.00

## Raw responses

### classm.ltc.1

```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].ltc[self].limit"
    value: "900.00"
    work: "Line 2(b): age bracket 41 to 50 -> $900"
  - printed: "person[taxpayer].sc[biz_a].ltc[self].amount"
    value: "900.00"
    work: "Line 2: smaller of (a) $5,787.00 or (b) $900.00 = $900.00"
```

### classm.ltc.2

```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].ltc[self].limit"
    value: "900.00"
    work: "Age band 'to50' = age 41 to 50; line 2(b) limit $900"
  - printed: "person[taxpayer].sc[biz_a].ltc[self].amount"
    value: "90.00"
    work: "Smaller of (a) $90.00 paid or (b) $900.00 = $90.00"
```
