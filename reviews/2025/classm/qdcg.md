# Class M hand-work — qdcg

`Qualified Dividends and Capital Gain Tax Worksheet—Line 16` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-17 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 3 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040gi | 2025; printed date 2026-02-25 | 38 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | - | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.qdcg.1 — prompt sha256 8b52fd00c43b7f086500858d448e1f6356a919c553256daa60d2f37a24e2e5d6; branches: qdcg.schedule_d_filed:true, qdcg.line3#0, qdcg.line5:positive, qdcg.line7:right, qdcg.line8:right, qdcg.line10:right, qdcg.line14:left, qdcg.line16:positive, qdcg.line17:left, qdcg.line25:left

### classm.qdcg.1 — 1 — Enter the amount from Form 1040 or 1040-SR, line 15. However, if you are filing 
Status: **AGREE**

Value: $339,977.00

### classm.qdcg.1 — 2 — Enter the amount from Form 1040 or 1040-SR, line 3a
Status: **AGREE**

Value: $0.00

### classm.qdcg.1 — 3 — Are you filing Schedule D? Yes. Enter the smaller of line 15 or line 16 of Sched
Status: **AGREE**

Value: $5,770.00

### classm.qdcg.1 — 4 — Add lines 2 and 3
Status: **AGREE**

Value: $5,770.00

### classm.qdcg.1 — 5 — Subtract line 4 from line 1. If zero or less, enter -0-
Status: **AGREE**

Value: $334,207.00

### classm.qdcg.1 — 6 — Enter: $48,350 if single or married filing separately, $96,700 if married filing
Status: **AGREE**

Value: $64,750.00

### classm.qdcg.1 — 7 — Enter the smaller of line 1 or line 6
Status: **AGREE**

Value: $64,750.00

### classm.qdcg.1 — 8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $64,750.00

### classm.qdcg.1 — 9 — Subtract line 8 from line 7. This amount is taxed at 0%
Status: **AGREE**

Value: $0.00

### classm.qdcg.1 — 10 — Enter the smaller of line 1 or line 4
Status: **AGREE**

Value: $5,770.00

### classm.qdcg.1 — 11 — Enter the amount from line 9
Status: **AGREE**

Value: $0.00

### classm.qdcg.1 — 12 — Subtract line 11 from line 10
Status: **AGREE**

Value: $5,770.00

### classm.qdcg.1 — 13 — Enter: $533,400 if single, $300,000 if married filing separately, $600,050 if ma
Status: **AGREE**

Value: $566,700.00

### classm.qdcg.1 — 14 — Enter the smaller of line 1 or line 13
Status: **AGREE**

Value: $339,977.00

### classm.qdcg.1 — 15 — Add lines 5 and 9
Status: **AGREE**

Value: $334,207.00

### classm.qdcg.1 — 16 — Subtract line 15 from line 14. If zero or less, enter -0-
Status: **AGREE**

Value: $5,770.00

### classm.qdcg.1 — 17 — Enter the smaller of line 12 or line 16
Status: **AGREE**

Value: $5,770.00

### classm.qdcg.1 — 18 — Multiply line 17 by 15% (0.15)
Status: **AGREE**

Value: $865.50

### classm.qdcg.1 — 19 — Add lines 9 and 17
Status: **AGREE**

Value: $5,770.00

### classm.qdcg.1 — 20 — Subtract line 19 from line 10
Status: **AGREE**

Value: $0.00

### classm.qdcg.1 — 21 — Multiply line 20 by 20% (0.20)
Status: **AGREE**

Value: $0.00

### classm.qdcg.1 — 23 — Add lines 18, 21, and 22
Status: **AGREE**

Value: $85,646.95

### classm.qdcg.1 — 25 — Tax on all taxable income. Enter the smaller of line 23 or line 24. Also include
Status: **AGREE**

Value: $85,646.95

### case classm.qdcg.2 — prompt sha256 6427f95b60b448fa423bce7ef6a1e7239271308ab28d6dc39e5b6285e7844719; branches: qdcg.schedule_d_filed:false, qdcg.line3#1, qdcg.line5:floor, qdcg.line7:left, qdcg.line8:left, qdcg.line10:left, qdcg.line14:left, qdcg.line16:floor, qdcg.line17:left, qdcg.line25:left

### classm.qdcg.2 — 1 — Enter the amount from Form 1040 or 1040-SR, line 15. However, if you are filing 
Status: **AGREE**

Value: $0.00

### classm.qdcg.2 — 2 — Enter the amount from Form 1040 or 1040-SR, line 3a
Status: **AGREE**

Value: $24,189.00

### classm.qdcg.2 — 3 — Are you filing Schedule D? Yes. Enter the smaller of line 15 or line 16 of Sched
Status: **AGREE**

Value: $19,947.00

### classm.qdcg.2 — 4 — Add lines 2 and 3
Status: **AGREE**

Value: $44,136.00

### classm.qdcg.2 — 5 — Subtract line 4 from line 1. If zero or less, enter -0-
Status: **AGREE**

Value: $0.00

### classm.qdcg.2 — 6 — Enter: $48,350 if single or married filing separately, $96,700 if married filing
Status: **AGREE**

Value: $48,350.00

### classm.qdcg.2 — 7 — Enter the smaller of line 1 or line 6
Status: **AGREE**

Value: $0.00

### classm.qdcg.2 — 8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $0.00

### classm.qdcg.2 — 9 — Subtract line 8 from line 7. This amount is taxed at 0%
Status: **AGREE**

Value: $0.00

### classm.qdcg.2 — 10 — Enter the smaller of line 1 or line 4
Status: **AGREE**

Value: $0.00

### classm.qdcg.2 — 11 — Enter the amount from line 9
Status: **AGREE**

Value: $0.00

### classm.qdcg.2 — 12 — Subtract line 11 from line 10
Status: **AGREE**

Value: $0.00

### classm.qdcg.2 — 13 — Enter: $533,400 if single, $300,000 if married filing separately, $600,050 if ma
Status: **AGREE**

Value: $533,400.00

### classm.qdcg.2 — 14 — Enter the smaller of line 1 or line 13
Status: **AGREE**

Value: $0.00

### classm.qdcg.2 — 15 — Add lines 5 and 9
Status: **AGREE**

Value: $0.00

### classm.qdcg.2 — 16 — Subtract line 15 from line 14. If zero or less, enter -0-
Status: **AGREE**

Value: $0.00

### classm.qdcg.2 — 17 — Enter the smaller of line 12 or line 16
Status: **AGREE**

Value: $0.00

### classm.qdcg.2 — 18 — Multiply line 17 by 15% (0.15)
Status: **AGREE**

Value: $0.00

### classm.qdcg.2 — 19 — Add lines 9 and 17
Status: **AGREE**

Value: $0.00

### classm.qdcg.2 — 20 — Subtract line 19 from line 10
Status: **AGREE**

Value: $0.00

### classm.qdcg.2 — 21 — Multiply line 20 by 20% (0.20)
Status: **AGREE**

Value: $0.00

### classm.qdcg.2 — 23 — Add lines 18, 21, and 22
Status: **AGREE**

Value: $0.00

### classm.qdcg.2 — 25 — Tax on all taxable income. Enter the smaller of line 23 or line 24. Also include
Status: **AGREE**

Value: $0.00

### case classm.qdcg.3 — prompt sha256 3d586afd67a1f54dad3836aea2ca45de890f825dd4cb9d57dcb8aa51dfa2df26; branches: qdcg.schedule_d_filed:true, qdcg.line3#0, qdcg.line5:positive, qdcg.line7:right, qdcg.line8:left, qdcg.line10:right, qdcg.line14:right, qdcg.line16:positive, qdcg.line17:right, qdcg.line25:left

### classm.qdcg.3 — 1 — Enter the amount from Form 1040 or 1040-SR, line 15. However, if you are filing 
Status: **AGREE**

Value: $376,357.00

### classm.qdcg.3 — 2 — Enter the amount from Form 1040 or 1040-SR, line 3a
Status: **AGREE**

Value: $320,000.00

### classm.qdcg.3 — 3 — Are you filing Schedule D? Yes. Enter the smaller of line 15 or line 16 of Sched
Status: **AGREE**

Value: $19,848.00

### classm.qdcg.3 — 4 — Add lines 2 and 3
Status: **AGREE**

Value: $339,848.00

### classm.qdcg.3 — 5 — Subtract line 4 from line 1. If zero or less, enter -0-
Status: **AGREE**

Value: $36,509.00

### classm.qdcg.3 — 6 — Enter: $48,350 if single or married filing separately, $96,700 if married filing
Status: **AGREE**

Value: $48,350.00

### classm.qdcg.3 — 7 — Enter the smaller of line 1 or line 6
Status: **AGREE**

Value: $48,350.00

### classm.qdcg.3 — 8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $36,509.00

### classm.qdcg.3 — 9 — Subtract line 8 from line 7. This amount is taxed at 0%
Status: **AGREE**

Value: $11,841.00

### classm.qdcg.3 — 10 — Enter the smaller of line 1 or line 4
Status: **AGREE**

Value: $339,848.00

### classm.qdcg.3 — 11 — Enter the amount from line 9
Status: **AGREE**

Value: $11,841.00

### classm.qdcg.3 — 12 — Subtract line 11 from line 10
Status: **AGREE**

Value: $328,007.00

### classm.qdcg.3 — 13 — Enter: $533,400 if single, $300,000 if married filing separately, $600,050 if ma
Status: **AGREE**

Value: $300,000.00

### classm.qdcg.3 — 14 — Enter the smaller of line 1 or line 13
Status: **AGREE**

Value: $300,000.00

### classm.qdcg.3 — 15 — Add lines 5 and 9
Status: **AGREE**

Value: $48,350.00

### classm.qdcg.3 — 16 — Subtract line 15 from line 14. If zero or less, enter -0-
Status: **AGREE**

Value: $251,650.00

### classm.qdcg.3 — 17 — Enter the smaller of line 12 or line 16
Status: **AGREE**

Value: $251,650.00

### classm.qdcg.3 — 18 — Multiply line 17 by 15% (0.15)
Status: **AGREE**

Value: $37,747.50

### classm.qdcg.3 — 19 — Add lines 9 and 17
Status: **AGREE**

Value: $263,491.00

### classm.qdcg.3 — 20 — Subtract line 19 from line 10
Status: **AGREE**

Value: $76,357.00

### classm.qdcg.3 — 21 — Multiply line 20 by 20% (0.20)
Status: **AGREE**

Value: $15,271.40

### classm.qdcg.3 — 23 — Add lines 18, 21, and 22
Status: **AGREE**

Value: $57,163.90

### classm.qdcg.3 — 25 — Tax on all taxable income. Enter the smaller of line 23 or line 24. Also include
Status: **AGREE**

Value: $57,163.90

## Raw responses

### classm.qdcg.1

```yaml
```yaml
lines:
  - printed: "1"
    value: "339977.00"
    work: "Form 1040 line 15 = 339,977.00 (no Form 2555)"
  - printed: "2"
    value: "0.00"
    work: "Form 1040 line 3a = 0.00"
  - printed: "3"
    value: "5770.00"
    work: "Filing Schedule D: yes; smaller of Sch D line 15 or 16 = 5,770.00"
  - printed: "4"
    value: "5770.00"
    work: "0.00 + 5,770.00"
  - printed: "5"
    value: "334207.00"
    work: "339,977.00 - 5,770.00"
  - printed: "6"
    value: "64750.00"
    work: "Head of household threshold"
  - printed: "7"
    value: "64750.00"
    work: "smaller of 339,977.00 or 64,750.00"
  - printed: "8"
    value: "64750.00"
    work: "smaller of 334,207.00 or 64,750.00"
  - printed: "9"
    value: "0.00"
    work: "64,750.00 - 64,750.00"
  - printed: "10"
    value: "5770.00"
    work: "smaller of 339,977.00 or 5,770.00"
  - printed: "11"
    value: "0.00"
    work: "line 9"
  - printed: "12"
    value: "5770.00"
    work: "5,770.00 - 0.00"
  - printed: "13"
    value: "566700.00"
    work: "Head of household threshold"
  - printed: "14"
    value: "339977.00"
    work: "smaller of 339,977.00 or 566,700.00"
  - printed: "15"
    value: "334207.00"
    work: "334,207.00 + 0.00"
  - printed: "16"
    value: "5770.00"
    work: "339,977.00 - 334,207.00"
  - printed: "17"
    value: "5770.00"
    work: "smaller of 5,770.00 or 5,770.00"
  - printed: "18"
    value: "865.50"
    work: "5,770.00 x 0.15"
  - printed: "19"
    value: "5770.00"
    work: "0.00 + 5,770.00"
  - printed: "20"
    value: "0.00"
    work: "5,770.00 - 5,770.00"
  - printed: "21"
    value: "0.00"
    work: "0.00 x 0.20"
  - printed: "23"
    value: "85646.95"
    work: "865.50 + 0.00 + 84,781.45"
  - printed: "25"
    value: "85646.95"
    work: "smaller of 85,646.95 or 86,800.95"
```
```

### classm.qdcg.2

```yaml
lines:
  - printed: "1"
    value: "0.00"
    work: "Form 1040 line 15 = 0.00"
  - printed: "2"
    value: "24189.00"
    work: "Form 1040 line 3a = 24,189.00"
  - printed: "3"
    value: "19947.00"
    work: "No Schedule D; Form 1040 line 7a gets the capital gain distributions = 19,947.00"
  - printed: "4"
    value: "44136.00"
    work: "24,189.00 + 19,947.00 = 44,136.00"
  - printed: "5"
    value: "0.00"
    work: "0.00 - 44,136.00 is less than zero, so enter -0-"
  - printed: "6"
    value: "48350.00"
    work: "Single = 48,350.00"
  - printed: "7"
    value: "0.00"
    work: "smaller of 0.00 and 48,350.00"
  - printed: "8"
    value: "0.00"
    work: "smaller of 0.00 and 0.00"
  - printed: "9"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "10"
    value: "0.00"
    work: "smaller of 0.00 and 44,136.00"
  - printed: "11"
    value: "0.00"
    work: "line 9 = 0.00"
  - printed: "12"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "13"
    value: "533400.00"
    work: "Single = 533,400.00"
  - printed: "14"
    value: "0.00"
    work: "smaller of 0.00 and 533,400.00"
  - printed: "15"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "16"
    value: "0.00"
    work: "0.00 - 0.00 = 0, so enter -0-"
  - printed: "17"
    value: "0.00"
    work: "smaller of 0.00 and 0.00"
  - printed: "18"
    value: "0.00"
    work: "0.00 x 0.15"
  - printed: "19"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "20"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "21"
    value: "0.00"
    work: "0.00 x 0.20"
  - printed: "23"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00 (line 22 given)"
  - printed: "25"
    value: "0.00"
    work: "smaller of 0.00 and 0.00 (line 24 given)"
```

### classm.qdcg.3

```yaml
```yaml
lines:
  - printed: "1"
    value: "376357.00"
    work: "Form 1040 line 15 = 376,357.00 (no Form 2555)"
  - printed: "2"
    value: "320000.00"
    work: "Form 1040 line 3a = 320,000.00"
  - printed: "3"
    value: "19848.00"
    work: "Filing Schedule D: yes; smaller of Sch D line 15 or 16 = 19,848.00"
  - printed: "4"
    value: "339848.00"
    work: "320,000.00 + 19,848.00"
  - printed: "5"
    value: "36509.00"
    work: "376,357.00 - 339,848.00"
  - printed: "6"
    value: "48350.00"
    work: "Married filing separately: 48,350"
  - printed: "7"
    value: "48350.00"
    work: "smaller of 376,357.00 or 48,350.00"
  - printed: "8"
    value: "36509.00"
    work: "smaller of 36,509.00 or 48,350.00"
  - printed: "9"
    value: "11841.00"
    work: "48,350.00 - 36,509.00"
  - printed: "10"
    value: "339848.00"
    work: "smaller of 376,357.00 or 339,848.00"
  - printed: "11"
    value: "11841.00"
    work: "line 9"
  - printed: "12"
    value: "328007.00"
    work: "339,848.00 - 11,841.00"
  - printed: "13"
    value: "300000.00"
    work: "Married filing separately: 300,000"
  - printed: "14"
    value: "300000.00"
    work: "smaller of 376,357.00 or 300,000.00"
  - printed: "15"
    value: "48350.00"
    work: "36,509.00 + 11,841.00"
  - printed: "16"
    value: "251650.00"
    work: "300,000.00 - 48,350.00"
  - printed: "17"
    value: "251650.00"
    work: "smaller of 328,007.00 or 251,650.00"
  - printed: "18"
    value: "37747.50"
    work: "251,650.00 x 0.15"
  - printed: "19"
    value: "263491.00"
    work: "11,841.00 + 251,650.00"
  - printed: "20"
    value: "76357.00"
    work: "339,848.00 - 263,491.00"
  - printed: "21"
    value: "15271.40"
    work: "76,357.00 x 0.20"
  - printed: "23"
    value: "57163.90"
    work: "37,747.50 + 15,271.40 + 4,145.00"
  - printed: "25"
    value: "57163.90"
    work: "smaller of 57,163.90 or 101,283.34"
```
```
