# Class M hand-work — ny_city_rs

`New York City tax rate schedule` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/ny/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-11-05 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 14a5e4eb8d846a6706a317abd7af9a45f1e53937087ad30bf4e35fe555725b8e |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | ae4a6be40d11cad23745675e8a3d0cf567df9da900776d4e2302afefaaf31aca |
| cases | 14 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| ny_it201i-html | Web edition of Form IT-201-I (2025) ('2025 Form IT-201-I, Instructions for Form IT-201'); page 'Updated: July 27, 2026'. Every number of the PDF edition occurs in it and every word of every PDF page bar the six excepted pages (check_extraction.py --jurisdiction ny) | 1 | cited sections: New York City tax rate schedule | 63863fe461c33d052e26a67c87d000ed70b896c72437350880a9e1c680104982 | - | - |
| ny_it201i | Form IT-201-I (2025), Instructions for Form IT-201 (including instructions for Forms IT-195 and IT-201-ATT), 41 pages; final 2025 edition; PDF modified 2025-11-20 | 4 | cited pages | 05f677379d60faca0da08ac2dc171a937cf56878f73956511975c1dcc48aeff9 | 4 | 460f67bd9e14ac9d7ed2e001426510569307546a5c2cf0a97784808e2678eeaf |

## Lines

### case classm.ny_city_rs.1 — prompt sha256 ee59b5fd0a3db2f01ba56ae5f6e4424fa9180d558d30f7c9a86de20c2718bd93; branches: mfj.b2.excess:positive, mfj.result#1, tax#1

### classm.ny_city_rs.1 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $1,292.00
Model: $1,292.31
Work: MFJ over 21,600 not over 45,000: 665 + 3.762% x (38,275 - 21,600 = 16,675) = 665 + 627.31 = 1,292.31

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse", the bracket for line 47 of $38,275: $665 plus 3.762% of the excess over $21,600: exactly $1,292.3135, which the project rounds half-up to $1,292.00; the model's $1,292.31 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_city_rs.2 — prompt sha256 39920c47595d3e1d6c05195218fd2e9b12e7961b69054f56843133a727d3e9e0; branches: single.b3.excess:positive, single.result#2, tax#0

### classm.ny_city_rs.2 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $1,125.00
Model: $1,125.33
Work: Single, over 25,000 not over 50,000: 858 + 3.819% x (32,000 - 25,000) = 858 + 267.33 = 1,125.33

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York City tax rate schedule, "Single and married filing separately", the bracket for line 47 of $32,000: $858 plus 3.819% of the excess over $25,000: exactly $1,125.33, which the project rounds half-up to $1,125.00; the model's $1,125.33 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_city_rs.3 — prompt sha256 af7454cce6e89b92b226a006cd69f7ef7e1dafc653dff7ba09c48205229025ed; branches: hoh.b1.excess:floor, hoh.result#0, tax#4

### classm.ny_city_rs.3 — tax — The tax from the schedule for the filing status
Status: **AGREE**

Value: $0.00

### case classm.ny_city_rs.4 — prompt sha256 ffe51b0dd1cfd20b684f8a1c6a950d4b9203df4d80860608942f8052d0054824; branches: mfj.b3.excess:positive, mfj.result#2, tax#2

### classm.ny_city_rs.4 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $2,500.00
Model: $2,499.75
Work: Status 5, over $45,000 not over $90,000: $1,545 + 3.819% x ($70,000 - $45,000) = $1,545 + $954.75

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse", the bracket for line 47 of $70,000: $1,545 plus 3.819% of the excess over $45,000: exactly $2,499.75, which the project rounds half-up to $2,500.00; the model's $2,499.75 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_city_rs.5 — prompt sha256 99c98d3127b05c8fc8685c0fadc524806291f5d2b9a70913894a9008347ed2ae; branches: single.b4.excess:positive, single.result#3, tax#3

### classm.ny_city_rs.5 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $2,588.00
Model: $2,588.20
Work: MFS schedule, over $50,000: $1,813 + 3.876% x ($70,000 - $50,000 = $20,000) = $1,813 + $775.20 = $2,588.20

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York City tax rate schedule, "Single and married filing separately", the bracket for line 47 of $70,000: $1,813 plus 3.876% of the excess over $50,000: exactly $2,588.20, which the project rounds half-up to $2,588.00; the model's $2,588.20 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_city_rs.6 — prompt sha256 6e6ad3a3b0a2eb44a47664d7b69a71268c93cbbb76993b84ad3f1af0362b1c9f; branches: mfj.b1.excess:floor, mfj.result#0, tax#1

### classm.ny_city_rs.6 — tax — The tax from the schedule for the filing status
Status: **AGREE**

Value: $0.00

### case classm.ny_city_rs.7 — prompt sha256 a8a5bafd24f8955093bf854cade357966027809132229bb98a630bfb98ed32df; branches: hoh.b2.excess:positive, hoh.result#1, tax#4

### classm.ny_city_rs.7 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $842.00
Model: $841.73
Work: HOH bracket $14,400-$30,000: $443 + 3.762% x ($24,999 - $14,400 = $10,599) = $443 + $398.73 = $841.73

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York City tax rate schedule, "Head of household", the bracket for line 47 of $24,999: $443 plus 3.762% of the excess over $14,400: exactly $841.73438, which the project rounds half-up to $842.00; the model's $841.73 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_city_rs.8 — prompt sha256 3fbe466cf2e2ce30fdde9b5cce961616380c51934ada37bf32ffdd66638a18ac; branches: hoh.b3.excess:positive, hoh.result#2, tax#4

### classm.ny_city_rs.8 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $1,346.00
Model: $1,346.02
Work: HOH ④, over 30,000 not over 60,000: 1,030 + 3.819% × (38,275 − 30,000 = 8,275) = 1,030 + 316.02 = 1,346.02

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York City tax rate schedule, "Head of household", the bracket for line 47 of $38,275: $1,030 plus 3.819% of the excess over $30,000: exactly $1,346.02225, which the project rounds half-up to $1,346.00; the model's $1,346.02 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_city_rs.9 — prompt sha256 54134bd2c8c3338df38103f7a6d2cfa8c49ae360b3d9a4a4eda836400c0416ea; branches: hoh.b4.excess:positive, hoh.result#3, tax#4

### classm.ny_city_rs.9 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $2,370.00
Model: $2,369.76
Work: HOH: over 60,000, so 2,176 + 3.876% x (64,999 - 60,000 = 4,999) = 2,176 + 193.76 = 2,369.76

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York City tax rate schedule, "Head of household", the bracket for line 47 of $64,999: $2,176 plus 3.876% of the excess over $60,000: exactly $2,369.76124, which the project rounds half-up to $2,370.00; the model's $2,369.76 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_city_rs.10 — prompt sha256 7d632fabebc13af5a34317d6dc5bbaf77af665ae13f4336191b0256a7a4b0faa; branches: mfj.b4.excess:positive, mfj.result#3, tax#1

### classm.ny_city_rs.10 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $3,458.00
Model: $3,457.80
Work: MFJ over 90,000: 3,264 + 3.876% x (95,000 - 90,000) = 3,264 + 193.80 = 3,457.80

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse", the bracket for line 47 of $95,000: $3,264 plus 3.876% of the excess over $90,000: exactly $3,457.80, which the project rounds half-up to $3,458.00; the model's $3,457.80 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_city_rs.11 — prompt sha256 be0b5cd5aced5546b140c9726f14e2c0e35227b1d42a06a866957f5e59a799f9; branches: single.b2.excess:positive, single.result#1, tax#3

### classm.ny_city_rs.11 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $482.00
Model: $481.86
Work: MFS (status 3) bracket $12,000-$25,000: $369 + 3.762% x ($15,000 - $12,000) = $369 + $112.86 = $481.86

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York City tax rate schedule, "Single and married filing separately", the bracket for line 47 of $15,000: $369 plus 3.762% of the excess over $12,000: exactly $481.86, which the project rounds half-up to $482.00; the model's $481.86 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_city_rs.12 — prompt sha256 afd7a625d82c4aa017a60cf92f04688b8ab1e56126c8bb09c674b2b135ee4716; branches: single.b1.excess:positive, single.result#0, tax#3

### classm.ny_city_rs.12 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $237.00
Model: $236.64
Work: Single/MFS schedule, line 47 $7,688 not over $12,000: 3.078% x 7,688 = 236.64

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York City tax rate schedule, "Single and married filing separately", the bracket for line 47 of $7,688: 3.078% of the amount: exactly $236.63664, which the project rounds half-up to $237.00; the model's $236.64 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_city_rs.13 — prompt sha256 e2b3844206f18ba323fc4ab343721e5115fbe385d6ae59af41d2b34961994f9c; branches: mfj.b1.excess:positive, mfj.result#0, tax#1

### classm.ny_city_rs.13 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $0.00
Model: $0.37
Work: MFJ schedule, line 47 of $12 is not over $21,600: 3.078% x $12.00 = $0.36936, rounded to $0.37

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York City tax rate schedule, "Married filing jointly and qualifying surviving spouse", the bracket for line 47 of $12: 3.078% of the amount: exactly $0.36936, which the project rounds half-up to $0.00; the model's $0.37 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

### case classm.ny_city_rs.14 — prompt sha256 923aed1c94d2ebbd02bc225a911624f841c10f946a127a592c94b5997c380531; branches: hoh.b1.excess:positive, hoh.result#0, tax#4

### classm.ny_city_rs.14 — tax — The tax from the schedule for the filing status
Status: **DISAGREE**

Project: $0.00
Model: $0.37
Work: HOH, line 47 $12 not over $14,400: 3.078% x 12.00 = 0.36936, rounded to 0.37

Ruling: ambiguity; amb.ny.2025.whole_dollars (owner decision C4; chosen reading: each computed tax, credit or worksheet line rounded half-up to the dollar where it is computed): IT-201-I p. 2, Entering whole dollar amounts, "When you enter amounts on your return, enter whole dollar amounts only." ... "Increase amounts that are 50 cents or more to the next dollar." IT-201-I (web edition), New York City tax rate schedule, "Head of household", the bracket for line 47 of $12: 3.078% of the amount: exactly $0.36936, which the project rounds half-up to $0.00; the model's $0.37 is the same amount in cents. The model kept cents (the register's third reading, round only the final lines); the class M prompt carries neither the whole-dollar page nor the register entry (the tooling low in research/audits/ny/BUG-0424_lows.md). Recomputed from the source, not from the engine. Model value dropped from the fixture as not evidence. [dropped]

## Raw responses

### classm.ny_city_rs.1

```yaml
38,275 - 21,600 = 16,675. × 0.03762 = 627.3135. Plus 665 = 1,292.3135 → 1,292.31.

```yaml
lines:
  - printed: "tax"
    value: "1292.31"
    work: "MFJ over 21,600 not over 45,000: 665 + 3.762% x (38,275 - 21,600 = 16,675) = 665 + 627.31 = 1,292.31"
```
```

### classm.ny_city_rs.2

```yaml
lines:
  - printed: "tax"
    value: "1123.86"
    work: "Single, over 25,000 not over 50,000: 858 + 3.819% x (32,000 - 25,000) = 858 + 267.33 = 1,125.33"

Wait—recompute: 7,000 × 0.03819 = 267.33; 858 + 267.33 = 1,125.33.

lines:
  - printed: "tax"
    value: "1125.33"
    work: "Single, over 25,000 not over 50,000: 858 + 3.819% x (32,000 - 25,000) = 858 + 267.33 = 1,125.33"
```

### classm.ny_city_rs.3

```yaml
lines:
  - printed: "tax"
    value: "0.00"
    work: "HOH schedule: line 47 $0 is not over $14,400, so tax = 3.078% x $0 = $0.00"
```

### classm.ny_city_rs.4

```yaml
Status 5: 45,000–90,000 bracket. 1,545 + 3.819% × 25,000 = 1,545 + 954.75 = 2,499.75.

lines:
  - printed: "tax"
    value: "2499.75"
    work: "Status 5, over $45,000 not over $90,000: $1,545 + 3.819% x ($70,000 - $45,000) = $1,545 + $954.75"
```

### classm.ny_city_rs.5

```yaml
lines:
  - printed: "tax"
    value: "2588.20"
    work: "MFS schedule, over $50,000: $1,813 + 3.876% x ($70,000 - $50,000 = $20,000) = $1,813 + $775.20 = $2,588.20"
```

### classm.ny_city_rs.6

```yaml
lines:
  - printed: "tax"
    value: "0.00"
    work: "MFJ schedule, line 47 $0 (not over $21,600): 3.078% x $0.00 = $0.00"
```

### classm.ny_city_rs.7

```yaml
lines:
  - printed: "tax"
    value: "841.73"
    work: "HOH bracket $14,400-$30,000: $443 + 3.762% x ($24,999 - $14,400 = $10,599) = $443 + $398.73 = $841.73"
```

### classm.ny_city_rs.8

```yaml
lines:
  - printed: "tax"
    value: "1346.02"
    work: "HOH ④, over 30,000 not over 60,000: 1,030 + 3.819% × (38,275 − 30,000 = 8,275) = 1,030 + 316.02 = 1,346.02"
```

### classm.ny_city_rs.9

```yaml
lines:
  - printed: "tax"
    value: "2369.76"
    work: "HOH: over 60,000, so 2,176 + 3.876% x (64,999 - 60,000 = 4,999) = 2,176 + 193.76 = 2,369.76"
```

### classm.ny_city_rs.10

```yaml
lines:
  - printed: "tax"
    value: "3457.80"
    work: "MFJ over 90,000: 3,264 + 3.876% x (95,000 - 90,000) = 3,264 + 193.80 = 3,457.80"
```

### classm.ny_city_rs.11

```yaml
lines:
  - printed: "tax"
    value: "481.86"
    work: "MFS (status 3) bracket $12,000-$25,000: $369 + 3.762% x ($15,000 - $12,000) = $369 + $112.86 = $481.86"
```

### classm.ny_city_rs.12

```yaml
lines:
  - printed: "tax"
    value: "236.64"
    work: "Single/MFS schedule, line 47 $7,688 not over $12,000: 3.078% x 7,688 = 236.64"
```

### classm.ny_city_rs.13

```yaml
lines:
  - printed: "tax"
    value: "0.37"
    work: "MFJ schedule, line 47 of $12 is not over $21,600: 3.078% x $12.00 = $0.36936, rounded to $0.37"
```

### classm.ny_city_rs.14

```yaml
lines:
  - printed: "tax"
    value: "0.37"
    work: "HOH, line 47 $12 not over $14,400: 3.078% x 12.00 = 0.36936, rounded to 0.37"
```
