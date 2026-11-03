# Class M hand-work — asset

`Form 4562 — one item of depreciable property (other than a vehicle) of a business` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | 147c649ced5c8fc37c98b9192bd0bd1183b85534f98028807438b786cc52bc33 |
| cases | 4 |
| worked target scope | printed IRS lines |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i4562 | 2025 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| p946 | For use in preparing 2025 returns | 17, 34, 37, 39, 41, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 34, 37, 39, 41 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### case classm.asset.1 — prompt sha256 6f89b7c042e64cff0641cc7b53f51756899d22c2ebfa7666fd3777840df3d901; branches: asset.outside:false, asset.qip_early:false, asset.screen:false, asset.screened:false, asset.pct_bad:false, asset.listed:false, asset.listed:true, asset.over_half:false, asset.over_half:true, asset.listed_low:false, asset.is2025:false, asset.is2025:true, asset.on_19:false, asset.on_19:true, asset.on_17:false, asset.on_17:true, asset.on_26_2025:false, asset.on_26_2025:true, asset.done:false, asset.s179_bad:false, asset.after179:positive, asset.after_jan19:false, asset.after_jan19:true, asset.bonus_same:true, asset.bonus_mixed:false, asset.bonus_fullcase#0, asset.bonus_fullcase#1, asset.bonus#0, asset.bonus#1, asset.ub:positive, asset.macrs2025#1, asset.mq_q4_2025#0, asset.mq_q4_2025#1, asset.mq_q4_2025#3, asset.ub_prior_a:positive, asset.ub_prior:positive, asset.macrs_prior#0, asset.dep_2025#0, asset.dep_2025#1, asset.bonus_2025#0, asset.bonus_2025#1, asset.s179_2025#0, asset.s179_2025#1, asset.mq_q4#0, asset.mq_q4#1, asset.mq_total#0, asset.mq_total#1, asset.cost179#0, asset.cost179#1, asset.cost179_2025#0, asset.cost179_2025#1, asset.is_section179:true, asset.cost179_real#0, asset.dep_prior#0, asset.dep_prior#1

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].period — Recovery period under GDS for the asset class
Status: **AGREE**

Value: y5

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $13,339.52

### classm.asset.1 — person[taxpayer].sc[biz_a].asset[item_1].macrs_prior — MACRS deduction for 2025 on property placed in service before 2025
Status: **AGREE**

Value: $2,561.19

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].period — Recovery period under GDS for the asset class
Status: **AGREE**

Value: y7

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $17,923.00

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].bonus — Special depreciation allowance for this property
Status: **AGREE**

Value: $5,528.40

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].col19c — Basis for depreciation (business/investment use only), column (c), after the sec
Status: **AGREE**

Value: $8,292.60

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_1].macrs2025 — MACRS depreciation for 2025 property
Status: **AGREE**

Value: $2,073.15

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_2].period — Recovery period under GDS for the asset class
Status: **AGREE**

Value: y7

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_2].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $46,295.40

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_2].f25 — Special depreciation allowance for this listed property (line 25)
Status: **AGREE**

Value: $18,518.16

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_2].f26i — Elected section 179 cost of this listed property (column (i))
Status: **AGREE**

Value: $0.00

### classm.asset.1 — person[taxpayer].sc[biz_b].asset[item_2].dep_listed — Depreciation of this listed property (column (h))
Status: **AGREE**

Value: $991.65

### case classm.asset.2 — prompt sha256 d59397da84bbd6628b08ac5f34cb980c3d2cc4d72da4e8c3b5221d697ea5e2be; branches: asset.outside:false, asset.qip_early:false, asset.screen:false, asset.screened:false, asset.pct_bad:false, asset.listed:false, asset.over_half:true, asset.listed_low:false, asset.is2025:true, asset.on_19:true, asset.on_17:false, asset.on_26_2025:false, asset.done:false, asset.s179_bad:false, asset.after179:positive, asset.after_jan19:true, asset.bonus_same:true, asset.bonus_mixed:false, asset.bonus_fullcase#0, asset.bonus#2, asset.ub:positive, asset.macrs2025#0, asset.mq_q4_2025#2, asset.mq_q4_2025#3, asset.ub_prior_a:positive, asset.ub_prior:positive, asset.macrs_prior#0, asset.dep_2025#0, asset.bonus_2025#0, asset.s179_2025#0, asset.mq_q4#0, asset.mq_total#0, asset.cost179#0, asset.cost179_2025#0, asset.is_section179:false, asset.is_section179:true, asset.cost179_real#0, asset.cost179_real#1, asset.dep_prior#1

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].period — Recovery period under GDS for the asset class
Status: **DISAGREE**

Project: y15sl
Model: y15
Work: Qualified improvement property placed in service after 2017 is 15-year property (i4562 line 19 col (a)).

Ruling: model error; p946 Table 4-1, GDS using SL: "Qualified improvement property (as defined in section 168(e)(6) of the Internal Revenue Code) placed in service after 2017". The class is 15-year straight line, as the project has it. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $46,490.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].bonus — Special depreciation allowance for this property
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].col19c — Basis for depreciation (business/investment use only), column (c), after the sec
Status: **AGREE**

Value: $46,490.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_1].macrs2025 — MACRS depreciation for 2025 property
Status: **DISAGREE**

Project: $1,548.12
Model: $2,324.50
Work: Mid-quarter test is no, so HY applies; Table A-1 15-year year 1 rate 5.00% x $46,490.00 = $2,324.50.

Ruling: model error; p946 Table 4-1, GDS using SL: "Qualified improvement property (as defined in section 168(e)(6) of the Internal Revenue Code) placed in service after 2017". The class is 15-year straight line, as the project has it. The model applied Table A-1's 150% declining balance rate of 5.00%; the straight-line half-year rate of 3.33% gives the project's $1,548.12. [dropped]

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].period — Recovery period under GDS for the asset class
Status: **AGREE**

Value: y7

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $35,528.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].bonus — Special depreciation allowance for this property
Status: **AGREE**

Value: $0.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].col19c — Basis for depreciation (business/investment use only), column (c), after the sec
Status: **AGREE**

Value: $22,312.00

### classm.asset.2 — person[taxpayer].sc[biz_a].asset[item_2].macrs2025 — MACRS depreciation for 2025 property
Status: **AGREE**

Value: $3,188.38

### case classm.asset.3 — prompt sha256 37fc87f068d0fc2ba2595f03c15dd837166d6d383e092713b8c3096abcf2bfcd; branches: asset.outside:false, asset.qip_early:false, asset.screen:false, asset.screened:false, asset.pct_bad:false, asset.listed:false, asset.over_half:true, asset.listed_low:false, asset.is2025:true, asset.on_19:true, asset.on_17:false, asset.on_26_2025:false, asset.done:false, asset.s179_bad:false, asset.after179:floor, asset.after_jan19:false, asset.bonus_same:true, asset.bonus_mixed:false, asset.bonus_fullcase#1, asset.bonus#1, asset.ub:floor, asset.macrs2025#0, asset.mq_q4_2025#3, asset.ub_prior_a:positive, asset.ub_prior:positive, asset.macrs_prior#0, asset.dep_2025#0, asset.bonus_2025#0, asset.s179_2025#0, asset.mq_q4#0, asset.mq_total#0, asset.cost179#0, asset.cost179_2025#0, asset.is_section179:true, asset.cost179_real#0, asset.dep_prior#1

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].period — Recovery period under GDS for the asset class
Status: **AGREE**

Value: y3

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $100.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].bonus — Special depreciation allowance for this property
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].col19c — Basis for depreciation (business/investment use only), column (c), after the sec
Status: **AGREE**

Value: $0.00

### classm.asset.3 — person[taxpayer].sc[biz_a].asset[item_1].macrs2025 — MACRS depreciation for 2025 property
Status: **AGREE**

Value: $0.00

### case classm.asset.4 — prompt sha256 c1bd49bd84dcdbf3c5860eb9d66f97a2bb210eb399e0e62387995e185fa8def4; branches: asset.outside:false, asset.qip_early:false, asset.screen:false, asset.screened:false, asset.pct_bad:false, asset.listed:false, asset.listed:true, asset.over_half:true, asset.listed_low:false, asset.is2025:false, asset.is2025:true, asset.on_19:false, asset.on_17:false, asset.on_17:true, asset.on_26_2025:false, asset.on_26_2025:true, asset.done:false, asset.s179_bad:false, asset.after179:positive, asset.after_jan19:true, asset.bonus_same:true, asset.bonus_mixed:false, asset.bonus_fullcase#0, asset.bonus#1, asset.bonus#2, asset.ub:positive, asset.macrs2025#1, asset.mq_q4_2025#3, asset.ub_prior_a:floor, asset.ub_prior_a:positive, asset.ub_prior:floor, asset.ub_prior:positive, asset.macrs_prior#0, asset.dep_2025#0, asset.dep_2025#1, asset.bonus_2025#0, asset.bonus_2025#1, asset.s179_2025#0, asset.s179_2025#1, asset.mq_q4#0, asset.mq_q4#1, asset.mq_total#0, asset.mq_total#1, asset.cost179#0, asset.cost179#1, asset.cost179_2025#0, asset.is_section179:true, asset.cost179_real#0, asset.dep_prior#0, asset.dep_prior#1

### classm.asset.4 — person[taxpayer].sc[biz_b].asset[item_1].period — Recovery period under GDS for the asset class
Status: **AGREE**

Value: y5

### classm.asset.4 — person[taxpayer].sc[biz_b].asset[item_1].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $729.75

### classm.asset.4 — person[taxpayer].sc[biz_b].asset[item_1].macrs_prior — MACRS deduction for 2025 on property placed in service before 2025
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_b].asset[item_2].period — Recovery period under GDS for the asset class
Status: **AGREE**

Value: y7

### classm.asset.4 — person[taxpayer].sc[biz_b].asset[item_2].basis — Basis for depreciation (business/investment use only), before section 179 and th
Status: **AGREE**

Value: $42,124.00

### classm.asset.4 — person[taxpayer].sc[biz_b].asset[item_2].f25 — Special depreciation allowance for this listed property (line 25)
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_b].asset[item_2].f26i — Elected section 179 cost of this listed property (column (i))
Status: **AGREE**

Value: $0.00

### classm.asset.4 — person[taxpayer].sc[biz_b].asset[item_2].dep_listed — Depreciation of this listed property (column (h))
Status: **AGREE**

Value: $1,503.83

## Raw responses

### classm.asset.1

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].period"
    value: "y5"
    work: "Pub. 946 Table B-2 class 22.4 (Manufacture of Textile Yarns): GDS recovery period 5 years"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].basis"
    value: "13339.52"
    work: "41,686.00 x 32% business/investment use = 13,339.52; section 179 and special allowance are both 0"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs_prior"
    value: "2561.19"
    work: "Placed in service 2023 under half-year convention, so 2025 is year 3; Table A-1 5-yr year 3 = 19.20%; 13,339.52 x 19.20% = 2,561.19 (line 17)"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].period"
    value: "y7"
    work: "Pub. 946 Table B-2 class 37.42 (Manufacture of Railroad Cars): GDS recovery period 7 years"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].basis"
    value: "17923.00"
    work: "17,923.00 x 100% business/investment use = 17,923.00"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].bonus"
    value: "5528.40"
    work: "Acquired before Jan 20, 2025, so the allowance is limited to 40%; depreciable basis 17,923 - 4,102 section 179 = 13,821; 13,821 x 40% = 5,528.40"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].col19c"
    value: "8292.60"
    work: "17,923.00 - 4,102.00 section 179 - 5,528.40 special allowance = 8,292.60"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].macrs2025"
    value: "2073.15"
    work: "Mid-quarter convention applies, placed in service in Q1: Table A-2 7-yr year 1 = 25.00%; 8,292.60 x 25% = 2,073.15"
  - printed: "person[taxpayer].sc[biz_b].asset[item_2].period"
    value: "y7"
    work: "Pub. 946 Table B-2 class 20.4 (Manufacture of Other Food and Kindred Products): GDS recovery period 7 years"
  - printed: "person[taxpayer].sc[biz_b].asset[item_2].basis"
    value: "46295.40"
    work: "49,780.00 x 93% business/investment use = 46,295.40"
  - printed: "person[taxpayer].sc[biz_b].asset[item_2].f25"
    value: "18518.16"
    work: "Listed property used more than 50%; acquired after Jan 19, 2025 with 40% elected: 46,295.40 x 40% = 18,518.16"
  - printed: "person[taxpayer].sc[biz_b].asset[item_2].f26i"
    value: "0.00"
    work: "No section 179 elected for this listed property"
  - printed: "person[taxpayer].sc[biz_b].asset[item_2].dep_listed"
    value: "991.65"
    work: "Column (e) = 46,295.40 - 18,518.16 = 27,777.24; mid-quarter convention applies, Q4: Table A-5 7-yr year 1 = 3.57%; 27,777.24 x 3.57% = 991.65"
```
```

### classm.asset.2

```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].period"
    value: "y15"
    work: "Qualified improvement property placed in service after 2017 is 15-year property (i4562 line 19 col (a))."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].basis"
    value: "46490.00"
    work: "$46,490.00 cost x 100% business use = $46,490.00."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus"
    value: "0.00"
    work: "Special allowance for this class is none (elected out for the class), so the allowance is $0."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].col19c"
    value: "46490.00"
    work: "$46,490.00 - $0 section 179 - $0 special allowance = $46,490.00."
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs2025"
    value: "2324.50"
    work: "Mid-quarter test is no, so HY applies; Table A-1 15-year year 1 rate 5.00% x $46,490.00 = $2,324.50."
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].period"
    value: "y7"
    work: "Asset class 37.31 (Ship and Boat Building Machinery and Equipment) has a 7-year GDS period."
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].basis"
    value: "35528.00"
    work: "$35,528.00 cost x 100% business use = $35,528.00."
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].bonus"
    value: "0.00"
    work: "Special allowance for this class is none (elected out for the class), so the allowance is $0."
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].col19c"
    value: "22312.00"
    work: "$35,528.00 - $13,216.00 section 179 - $0 special allowance = $22,312.00."
  - printed: "person[taxpayer].sc[biz_a].asset[item_2].macrs2025"
    value: "3188.38"
    work: "HY applies; Table A-1 7-year year 1 rate 14.29% x $22,312.00 = $3,188.38."
```

### classm.asset.3

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].period"
    value: "y3"
    work: "Pub 946 Table B-1 asset class 00.26 (tractor units, over-the-road) has a GDS recovery period of 3 years"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].basis"
    value: "100.00"
    work: "Cost $100.00 x 100% business use = $100.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].bonus"
    value: "0.00"
    work: "Acquired before 1/20/2025, so the 40% rate applies; 40% x ($100.00 - $100.00 sec. 179) = $0.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].col19c"
    value: "0.00"
    work: "$100.00 - $100.00 sec. 179 - $0.00 special allowance = $0.00"
  - printed: "person[taxpayer].sc[biz_a].asset[item_1].macrs2025"
    value: "0.00"
    work: "Mid-quarter test is no, so half-year convention (Table A-1, 3-yr, year 1, 33.33%); $0.00 x 33.33% = $0.00"
```
```

### classm.asset.4

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].period"
    value: "y5"
    work: "Pub. 946 Table B-2 asset class 33.21: GDS recovery period 5 years"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].basis"
    value: "729.75"
    work: "$973.00 x 75% business use = $729.75"
  - printed: "person[taxpayer].sc[biz_b].asset[item_1].macrs_prior"
    value: "0.00"
    work: "Unadjusted basis = $729.75 - $730 sec 179 - $0 special allowance = $0 (cannot be below zero); 2025 is year 6, Table A-4 5-yr rate 7.06% x $0 = $0"
  - printed: "person[taxpayer].sc[biz_b].asset[item_2].period"
    value: "y7"
    work: "Pub. 946 Table B-2 asset class 31.0: GDS recovery period 7 years"
  - printed: "person[taxpayer].sc[biz_b].asset[item_2].basis"
    value: "42124.00"
    work: "$42,124.00 x 100% business use = $42,124.00"
  - printed: "person[taxpayer].sc[biz_b].asset[item_2].f25"
    value: "0.00"
    work: "Special allowance for this class is none (elected out), so line 25 is $0"
  - printed: "person[taxpayer].sc[biz_b].asset[item_2].f26i"
    value: "0.00"
    work: "Elected section 179 cost is $0"
  - printed: "person[taxpayer].sc[biz_b].asset[item_2].dep_listed"
    value: "1503.83"
    work: "Use >50%, so line 26; mid-quarter convention, placed in service Q4: Table A-5 7-yr year 1 rate 3.57% x $42,124 = $1,503.83"
```
```
