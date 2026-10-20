# Class M hand-work — se

`Schedule SE (Form 1040) — Self-Employment Tax, one per person` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 3 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1040sse | 2025; created 2025-05-07 | 1, 2 | whole document | d214b41a4e42da1953a1ee216b6f9d263be284a90cf9f7f28dcb87cd0e9913e6 | - | fbeaf5e9b8509f8fe754b52a6b5a643934ae2ff1a6f76e6e69af8be42fcd2cdd |
| i1040sse | 2025 | 1, 2, 3, 4, 5 | whole document | bd4768e77e9087e707701447574c3fd8b1b6ac8deca77fcf2e1bce4c50b7db28 | 1, 2, 3, 4, 5 | 6cb68f929e214450ea7ffa33648d5602e2431f38e91c7a6c83dfbee0ab23f08c |

## Lines

### case classm.se.1 — prompt sha256 55948e5f7510eeb8a751a63e291eee8339e6dc3cfd720b9798337174282fa375; branches: positive:true, line3pos:positive, line4a#0, owes:true, line4c_owes:positive, line4c#0, line9:positive, ss_base:left

### classm.se.1 — line3 — Combine lines 1a, 1b, and 2
Status: **AGREE**

Value: $61,416.00

### classm.se.1 — positive — Line 3 is more than zero
Status: **AGREE**

Value: yes

### classm.se.1 — line4a — If line 3 is more than zero, multiply line 3 by 92.35% (0.9235). Otherwise, ente
Status: **AGREE**

Value: $56,717.68

### classm.se.1 — line4b — If you elect one or both of the optional methods, enter the total of lines 15 an
Status: **AGREE**

Value: $0.00

### classm.se.1 — owes — Line 4c is $400 or more
Status: **AGREE**

Value: yes

### classm.se.1 — line4c — Combine lines 4a and 4b. If less than $400, stop; you don't owe self-employment 
Status: **AGREE**

Value: $56,717.68

### classm.se.1 — line5b — Multiply line 5a by 92.35% (0.9235)
Status: **AGREE**

Value: $0.00

### classm.se.1 — line6 — Add lines 4c and 5b
Status: **AGREE**

Value: $56,717.68

### classm.se.1 — line7 — Maximum amount of combined wages and self-employment earnings subject to social 
Status: **AGREE**

Value: $176,100.00

### classm.se.1 — line8d — Add lines 8a, 8b, and 8c
Status: **AGREE**

Value: $80,138.00

### classm.se.1 — line9 — Subtract line 8d from line 7. If zero or less, enter -0-
Status: **AGREE**

Value: $95,962.00

### classm.se.1 — line10 — Multiply the smaller of line 6 or line 9 by 12.4% (0.124)
Status: **AGREE**

Value: $7,032.99

### classm.se.1 — line11 — Multiply line 6 by 2.9% (0.029)
Status: **AGREE**

Value: $1,644.81

### classm.se.1 — line12 — Self-employment tax. Add lines 10 and 11
Status: **AGREE**

Value: $8,677.80

### classm.se.1 — line13 — Deduction for one-half of self-employment tax. Multiply line 12 by 50% (0.50)
Status: **AGREE**

Value: $4,338.90

### case classm.se.2 — prompt sha256 b6f9ff88bec6ece533e3c16009177c2cf31e30a93dbd12c8e4b70c993ce7056f; branches: positive:false, line4a#1, owes:false, line4c#1, line9:floor, ss_base:left

### classm.se.2 — line3 — Combine lines 1a, 1b, and 2
Status: **AGREE**

Value: $-88,880.80

### classm.se.2 — positive — Line 3 is more than zero
Status: **AGREE**

Value: no

### classm.se.2 — line4a — If line 3 is more than zero, multiply line 3 by 92.35% (0.9235). Otherwise, ente
Status: **AGREE**

Value: $-88,880.80

### classm.se.2 — line4b — If you elect one or both of the optional methods, enter the total of lines 15 an
Status: **AGREE**

Value: $0.00

### classm.se.2 — owes — Line 4c is $400 or more
Status: **AGREE**

Value: no

### classm.se.2 — line4c — Combine lines 4a and 4b. If less than $400, stop; you don't owe self-employment 
Status: **AGREE**

Value: $0.00

### classm.se.2 — line5b — Multiply line 5a by 92.35% (0.9235)
Status: **AGREE**

Value: $0.00

### classm.se.2 — line6 — Add lines 4c and 5b
Status: **AGREE**

Value: $0.00

### classm.se.2 — line7 — Maximum amount of combined wages and self-employment earnings subject to social 
Status: **AGREE**

Value: $176,100.00

### classm.se.2 — line8d — Add lines 8a, 8b, and 8c
Status: **AGREE**

Value: $176,100.00

### classm.se.2 — line9 — Subtract line 8d from line 7. If zero or less, enter -0-
Status: **AGREE**

Value: $0.00

### classm.se.2 — line10 — Multiply the smaller of line 6 or line 9 by 12.4% (0.124)
Status: **AGREE**

Value: $0.00

### classm.se.2 — line11 — Multiply line 6 by 2.9% (0.029)
Status: **AGREE**

Value: $0.00

### classm.se.2 — line12 — Self-employment tax. Add lines 10 and 11
Status: **AGREE**

Value: $0.00

### classm.se.2 — line13 — Deduction for one-half of self-employment tax. Multiply line 12 by 50% (0.50)
Status: **AGREE**

Value: $0.00

### case classm.se.3 — prompt sha256 66229c63708d6d48482fbe671ba46df88803d38b3ed65dd9e99c621d012c9c15; branches: positive:true, line3pos:positive, line4a#0, owes:true, line4c_owes:positive, line4c#0, line9:positive, ss_base:right

### classm.se.3 — line3 — Combine lines 1a, 1b, and 2
Status: **AGREE**

Value: $148,947.02

### classm.se.3 — positive — Line 3 is more than zero
Status: **AGREE**

Value: yes

### classm.se.3 — line4a — If line 3 is more than zero, multiply line 3 by 92.35% (0.9235). Otherwise, ente
Status: **AGREE**

Value: $137,552.57

### classm.se.3 — line4b — If you elect one or both of the optional methods, enter the total of lines 15 an
Status: **AGREE**

Value: $0.00

### classm.se.3 — owes — Line 4c is $400 or more
Status: **AGREE**

Value: yes

### classm.se.3 — line4c — Combine lines 4a and 4b. If less than $400, stop; you don't owe self-employment 
Status: **AGREE**

Value: $137,552.57

### classm.se.3 — line5b — Multiply line 5a by 92.35% (0.9235)
Status: **AGREE**

Value: $0.00

### classm.se.3 — line6 — Add lines 4c and 5b
Status: **AGREE**

Value: $137,552.57

### classm.se.3 — line7 — Maximum amount of combined wages and self-employment earnings subject to social 
Status: **AGREE**

Value: $176,100.00

### classm.se.3 — line8d — Add lines 8a, 8b, and 8c
Status: **AGREE**

Value: $48,074.00

### classm.se.3 — line9 — Subtract line 8d from line 7. If zero or less, enter -0-
Status: **AGREE**

Value: $128,026.00

### classm.se.3 — line10 — Multiply the smaller of line 6 or line 9 by 12.4% (0.124)
Status: **AGREE**

Value: $15,875.22

### classm.se.3 — line11 — Multiply line 6 by 2.9% (0.029)
Status: **AGREE**

Value: $3,989.02

### classm.se.3 — line12 — Self-employment tax. Add lines 10 and 11
Status: **AGREE**

Value: $19,864.24

### classm.se.3 — line13 — Deduction for one-half of self-employment tax. Multiply line 12 by 50% (0.50)
Status: **AGREE**

Value: $9,932.12

## Raw responses

### classm.se.1

```yaml
lines:
  - printed: "line3"
    value: "61416.00"
    work: "0 + 0 + 61,416.00 (line 2, Sch C line 31)"
  - printed: "positive"
    value: "yes"
    work: "61,416.00 > 0"
  - printed: "line4a"
    value: "56717.68"
    work: "61,416.00 x 0.9235 = 56,717.676"
  - printed: "line4b"
    value: "0.00"
    work: "No optional method elected"
  - printed: "owes"
    value: "yes"
    work: "56,717.68 >= 400"
  - printed: "line4c"
    value: "56717.68"
    work: "56,717.68 + 0"
  - printed: "line5b"
    value: "0.00"
    work: "No church employee income; 0 x 0.9235 = 0"
  - printed: "line6"
    value: "56717.68"
    work: "56,717.68 + 0"
  - printed: "line7"
    value: "176100.00"
    work: "2025 maximum printed on form"
  - printed: "line8d"
    value: "80138.00"
    work: "80,138.00 + 0 + 0; 8a under 176,100 so continue"
  - printed: "line9"
    value: "95962.00"
    work: "176,100.00 - 80,138.00"
  - printed: "line10"
    value: "7032.99"
    work: "smaller(56,717.68, 95,962.00) x 0.124 = 7,032.992"
  - printed: "line11"
    value: "1644.81"
    work: "56,717.68 x 0.029 = 1,644.813"
  - printed: "line12"
    value: "8677.80"
    work: "7,032.99 + 1,644.81"
  - printed: "line13"
    value: "4338.90"
    work: "8,677.80 x 0.50"
```

### classm.se.2

```yaml
```yaml
lines:
  - printed: "line3"
    value: "-88880.80"
    work: "Lines 1a (0) + 1b (0) + 2 (-88,880.80) = -88,880.80"
  - printed: "positive"
    value: "no"
    work: "Line 3 (-88,880.80) is not more than zero"
  - printed: "line4a"
    value: "-88880.80"
    work: "Line 3 is not more than zero, so line 4a = line 3"
  - printed: "line4b"
    value: "0.00"
    work: "No optional method elected; lines 15 and 17 are blank"
  - printed: "owes"
    value: "no"
    work: "Line 4c is less than $400"
  - printed: "line4c"
    value: "0.00"
    work: "-88,880.80 + 0 = -88,880.80, under $400: stop, no SE tax; floored at 0"
  - printed: "line5b"
    value: "0.00"
    work: "No church employee income on line 5a; stopped at line 4c anyway"
  - printed: "line6"
    value: "0.00"
    work: "Line 4c (0) + line 5b (0) = 0"
  - printed: "line7"
    value: "176100.00"
    work: "Amount preprinted on the form for 2025"
  - printed: "line8d"
    value: "176100.00"
    work: "Line 8a 176,100 + 8b 0 + 8c 0 = 176,100"
  - printed: "line9"
    value: "0.00"
    work: "176,100 - 176,100 = 0, so enter -0-"
  - printed: "line10"
    value: "0.00"
    work: "Smaller of line 6 (0) or line 9 (0) x 0.124 = 0"
  - printed: "line11"
    value: "0.00"
    work: "Line 6 (0) x 0.029 = 0"
  - printed: "line12"
    value: "0.00"
    work: "Line 10 (0) + line 11 (0) = 0"
  - printed: "line13"
    value: "0.00"
    work: "Line 12 (0) x 0.50 = 0"
```
```

### classm.se.3

```yaml
lines:
  - printed: "line3"
    value: "148947.02"
    work: "Line 1a 0 + line 1b 0 + line 2 148,947.02 = 148,947.02"
  - printed: "positive"
    value: "yes"
    work: "148,947.02 > 0"
  - printed: "line4a"
    value: "137552.57"
    work: "148,947.02 x 0.9235 = 137,552.573, rounded to 137,552.57"
  - printed: "line4b"
    value: "0.00"
    work: "No optional method elected"
  - printed: "owes"
    value: "yes"
    work: "Line 4c 137,552.57 >= 400"
  - printed: "line4c"
    value: "137552.57"
    work: "137,552.57 + 0 = 137,552.57"
  - printed: "line5b"
    value: "0.00"
    work: "No church employee income; 0 x 0.9235 = 0"
  - printed: "line6"
    value: "137552.57"
    work: "137,552.57 + 0 = 137,552.57"
  - printed: "line7"
    value: "176100.00"
    work: "2025 maximum printed on form"
  - printed: "line8d"
    value: "48074.00"
    work: "48,074.00 + 0 + 0 = 48,074.00 (under 176,100, so continue)"
  - printed: "line9"
    value: "128026.00"
    work: "176,100 - 48,074 = 128,026"
  - printed: "line10"
    value: "15875.22"
    work: "smaller of 137,552.57 or 128,026 is 128,026; x 0.124 = 15,875.224, rounded to 15,875.22"
  - printed: "line11"
    value: "3989.02"
    work: "137,552.57 x 0.029 = 3,989.025, rounded to 3,989.02"
  - printed: "line12"
    value: "19864.24"
    work: "15,875.22 + 3,989.02 = 19,864.24"
  - printed: "line13"
    value: "9932.12"
    work: "19,864.24 x 0.50 = 9,932.12"
```
