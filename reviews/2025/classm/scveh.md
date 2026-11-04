# Class M hand-work — scveh

`Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-11-03 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | da9e2090264689345e69f76544337bd540a603b16c17b3f243e3e597108fe8bf |
| cases | 5 |
| worked target scope | printed IRS lines |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 6, 7, 8, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 8, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p946 | For use in preparing 2025 returns | 17, 31, 34, 37, 41, 59, 60, 61, 62, 63, 71, 72, 73 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 31, 34, 37, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### case classm.scveh.1 — prompt sha256 742ec17075880c13e773e5f2552673f75f667e0c89079b0a6ed49b64b24f5b76; branches: scveh.owned:true, scveh.no_miles:false, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.employee_use:false, scveh.employee_bad:false, scveh.line9#0, scveh.line9#1, scveh.is_actual_owned:false, scveh.is_actual_owned:true, scveh.on_auto_limits:false, scveh.on_auto_limits:true, scveh.is_actual_leased:false, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:true, scveh.is2025:false, scveh.is2025:true, scveh.is2019:false, scveh.s179_bad:false, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:true, scveh.lim_2025#0, scveh.line7#0, scveh.line7#1, scveh.line10#0, scveh.line10#1, scveh.line10_2025#0, scveh.s179_line10:left, scveh.line11:positive, scveh.line14#0, scveh.line14#1, scveh.line15:positive, scveh.bonus_2025#1, scveh.line16#0, scveh.line16#1, scveh.bonus_allowed:left, scveh.line17:positive, scveh.line18:positive, scveh.line19#0, scveh.line19#1, scveh.line19_earlier#0, scveh.line19_2025#0, scveh.line20:right, scveh.b100:positive, scveh.d2:right, scveh.d3:right, scveh.d4:right, scveh.d5:right, scveh.d6:right, scveh.too_old:false, scveh.bonus_v#0, scveh.macrs_pass#0, scveh.macrs_heavy#0, scveh.macrs_v#0, scveh.bonus#0, scveh.bonus#1, scveh.macrs#0, scveh.macrs#1, scveh.s179_2025#0, scveh.s179_2025#1, scveh.mq_q4#0, scveh.mq_q4#1, scveh.mq_total#0, scveh.mq_total#1, scveh.cost179#0, scveh.cost179#1, scveh.q4_basis#0, scveh.mq_q4_o#0, scveh.mq_q4_o#1, scveh.mq_total_o#0, scveh.mq_total_o#1, scveh.cost179_o#0, scveh.cost179_o#1

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $980.70

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $934.67

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **AGREE**

Value: $7,534.44

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $5,760.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **DISAGREE**

Project: $3,988.45
Model: $3,988.46
Work: 5,760 x 69.244% = 3,988.46

Ruling: model error; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct, owner's ruling); the model multiplied by the exact fraction, a difference of a cent. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project: $3,988.45
Model: $3,988.46
Work: 3,988.46 - 0 = 3,988.46

Ruling: model error; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct, owner's ruling); the model multiplied by the exact fraction, a difference of a cent. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $6,516.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **AGREE**

Value: $1,018.44

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **DISAGREE**

Project: $3,988.45
Model: $3,988.46
Work: 3,988.46 - 0 = 3,988.46

Ruling: model error; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct, owner's ruling); the model multiplied by the exact fraction, a difference of a cent. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **AGREE**

Value: $1,018.44

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $58.66

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $58.66

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $3,162.05

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bus_cost — Business/investment cost (cost times business use)
Status: **AGREE**

Value: $24,797.16

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $20,200.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $14,007.35

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $14,007.35

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **AGREE**

Value: $24,797.16

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line16 — Special depreciation allowance
Status: **AGREE**

Value: $9,918.86

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $9,918.86

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $4,088.49

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line18 — Basis for depreciation (line 15 less line 16)
Status: **AGREE**

Value: $14,878.30

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $2,975.66

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $2,975.66

### case classm.scveh.2 — prompt sha256 8a0e0760334bba66840f22f50e8ad33b4367956fd0cef745587d2a540e174656; branches: scveh.owned:false, scveh.owned:true, scveh.no_miles:false, scveh.over_half:true, scveh.employee_use:false, scveh.employee_bad:false, scveh.line9#1, scveh.is_actual_owned:false, scveh.is_actual_owned:true, scveh.on_auto_limits:false, scveh.is_actual_leased:false, scveh.is_actual_leased:true, scveh.lease_smr_before:false, scveh.lease_smr_bad:false, scveh.line20a#0, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:false, scveh.suv:false, scveh.is2025:true, scveh.is2019:false, scveh.s179_bad:false, scveh.claims_bonus:false, scveh.lim_2025#1, scveh.line7#0, scveh.line10#0, scveh.line10_2025#1, scveh.s179_line10:left, scveh.line11:positive, scveh.line14#0, scveh.line15:positive, scveh.bonus_2025#2, scveh.line16#0, scveh.bonus_allowed:left, scveh.line17:positive, scveh.line18:positive, scveh.line19#0, scveh.line19_earlier#0, scveh.line19_2025#1, scveh.line20:right, scveh.too_old:false, scveh.bonus_v#1, scveh.macrs_pass#0, scveh.macrs_heavy#0, scveh.macrs_v#1, scveh.bonus#0, scveh.bonus#1, scveh.macrs#0, scveh.macrs#1, scveh.s179_2025#0, scveh.s179_2025#1, scveh.mq_q4#0, scveh.mq_q4#1, scveh.mq_total#0, scveh.mq_total#1, scveh.cost179#0, scveh.cost179#1, scveh.q4_basis#3, scveh.mq_q4_o#0, scveh.mq_total_o#0, scveh.cost179_o#0

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $6,517.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $62,561.38
Model: $62,561.37
Work: $69,019 x 11364/12537 = $62,561.37

Ruling: model error; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct, owner's ruling); the model multiplied by the exact fraction, a difference of a cent. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $62,561.38
Model: $62,561.37
Work: Line 13 $62,561.37 - line 14 $0 = $62,561.37

Ruling: model error; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct, owner's ruling); the model multiplied by the exact fraction, a difference of a cent. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $62,561.38
Model: $62,561.37
Work: Line 15 $62,561.37 - line 16 $0 = $62,561.37

Ruling: model error; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct, owner's ruling); the model multiplied by the exact fraction, a difference of a cent. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $3,128.07

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line9 — Car and truck expenses for this vehicle
Status: **DISAGREE**

Project: $6,698.00
Model: $6,697.99
Work: Business use 11498/13254; $7,646 x 11498/13254 = $6,632.99; plus parking and tolls $65 = $6,697.99

Ruling: model error; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct, owner's ruling); the model multiplied by the exact fraction, a difference of a cent. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $829.34

### case classm.scveh.3 — prompt sha256 a68bff946da2d58f2b8502eeb419f59cd02fcd000c589160310bbf2d415ed5e8; branches: scveh.owned:true, scveh.no_miles:false, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.employee_use:false, scveh.employee_bad:false, scveh.line9#0, scveh.line9#1, scveh.is_actual_owned:false, scveh.is_actual_owned:true, scveh.on_auto_limits:false, scveh.on_auto_limits:true, scveh.is_actual_leased:false, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:true, scveh.is2025:false, scveh.is2025:true, scveh.is2019:false, scveh.is2019:true, scveh.s179_bad:false, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:true, scveh.lim_2025#0, scveh.line7#0, scveh.line7#1, scveh.line10#0, scveh.line10#1, scveh.line10_2025#0, scveh.s179_line10:right, scveh.line11:floor, scveh.line11:positive, scveh.line14#0, scveh.line14#1, scveh.line15:positive, scveh.bonus_2025#1, scveh.line16#0, scveh.line16#1, scveh.bonus_allowed:left, scveh.bonus_allowed:right, scveh.line17:floor, scveh.line17:positive, scveh.line18:positive, scveh.line19#0, scveh.line19#1, scveh.line19_earlier#0, scveh.line19_earlier#1, scveh.line19_2025#0, scveh.line20:left, scveh.line20:right, scveh.b100:positive, scveh.d1:right, scveh.d2:right, scveh.d3:right, scveh.d4:right, scveh.d5:right, scveh.d6:right, scveh.unrecovered:floor, scveh.post_amount:right, scveh.too_old:false, scveh.bonus_v#0, scveh.macrs_pass#0, scveh.macrs_pass#1, scveh.macrs_heavy#0, scveh.macrs_heavy#1, scveh.macrs_v#0, scveh.bonus#0, scveh.bonus#1, scveh.macrs#0, scveh.macrs#1, scveh.s179_2025#0, scveh.s179_2025#1, scveh.mq_q4#0, scveh.mq_q4#1, scveh.mq_total#0, scveh.mq_total#1, scveh.cost179#0, scveh.cost179#1, scveh.q4_basis#1, scveh.mq_q4_o#0, scveh.mq_q4_o#1, scveh.mq_total_o#0, scveh.mq_total_o#1, scveh.cost179_o#0, scveh.cost179_o#1

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $665.28

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $4,575.15
Model: $4,575.14
Work: $5,983 × 11,777 ÷ 15,401 = $4,575.14.

Ruling: model error; project retained. A one-cent difference from the business-use percentage: the model multiplies by the exact mileage fraction, while the project rounds the percentage to six places, the reading recorded as amb.2025.vehicle_business_pct (p946 pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 13). Same class as the backlog-round rulings of this log. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $5,760.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $4,404.62

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $4,404.62

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $4,575.15
Model: $4,575.14
Work: Line 13 $4,575.14 − line 14 $0 = $4,575.14.

Ruling: model error; project retained. A one-cent difference from the business-use percentage: the model multiplies by the exact mileage fraction, while the project rounds the percentage to six places, the reading recorded as amb.2025.vehicle_business_pct (p946 pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 13). Same class as the backlog-round rulings of this log. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $4,404.62

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $4,575.15
Model: $4,575.14
Work: Line 15 $4,575.14 − line 16 $0 = $4,575.14.

Ruling: model error; project retained. A one-cent difference from the business-use percentage: the model multiplies by the exact mileage fraction, while the project rounds the percentage to six places, the reading recorded as amb.2025.vehicle_business_pct (p946 pp. 61-62, Depreciation Worksheet for Passenger Automobiles, line 13). Same class as the backlog-round rulings of this log. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $9,811.20

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_b].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $911.00

### classm.scveh.3 — person[taxpayer].sc[biz_b].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_b].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **AGREE**

Value: $23,212.92

### classm.scveh.3 — person[taxpayer].sc[biz_b].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $20,200.00

### classm.scveh.3 — person[taxpayer].sc[biz_b].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $18,663.47

### classm.scveh.3 — person[taxpayer].sc[biz_b].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $18,663.47

### classm.scveh.3 — person[taxpayer].sc[biz_b].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_b].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $18,663.47

### classm.scveh.3 — person[taxpayer].sc[biz_b].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **AGREE**

Value: $4,549.45

### classm.scveh.3 — person[taxpayer].sc[biz_b].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $1,819.78

### classm.scveh.3 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_b].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_b].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **AGREE**

Value: $2,729.67

### classm.scveh.3 — person[taxpayer].sc[biz_b].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $545.93

### classm.scveh.3 — person[taxpayer].sc[biz_b].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $0.00

### case classm.scveh.4 — prompt sha256 5bcc5d5fd05728178e76cd56b6342ccef5bff523ccc4a783328a11f38ccd351f; branches: scveh.owned:true, scveh.no_miles:false, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.employee_use:false, scveh.employee_bad:false, scveh.line9#0, scveh.line9#1, scveh.is_actual_owned:false, scveh.is_actual_owned:true, scveh.on_auto_limits:false, scveh.is_actual_leased:false, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:false, scveh.is2025:false, scveh.is2019:false, scveh.line7#1, scveh.line10#1, scveh.line10_2025#1, scveh.line11:positive, scveh.line14#1, scveh.line15:positive, scveh.line16#1, scveh.bonus_allowed:left, scveh.line17:positive, scveh.line18:positive, scveh.line19#1, scveh.line19_earlier#0, scveh.line19_2025#0, scveh.line20:right, scveh.b100:positive, scveh.d2:right, scveh.too_old:false, scveh.bonus_v#1, scveh.macrs_pass#0, scveh.macrs_heavy#0, scveh.macrs_v#1, scveh.bonus#0, scveh.bonus#1, scveh.macrs#0, scveh.macrs#1, scveh.s179_2025#0, scveh.s179_2025#1, scveh.mq_q4#0, scveh.mq_q4#1, scveh.mq_total#0, scveh.mq_total#1, scveh.cost179#0, scveh.cost179#1, scveh.mq_q4_o#1, scveh.mq_total_o#1, scveh.cost179_o#1

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $6,972.70

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $3,745.10

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $21,535.84
Model: $21,535.85
Work: Worksheet line 13: 24,583 x 16,220/18,515 = 21,535.85

Ruling: model error; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct, owner's ruling); the model multiplied by the exact fraction, a difference of a cent. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $21,535.84
Model: $21,535.85
Work: 21,535.85 - 0 = 21,535.85

Ruling: model error; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct, owner's ruling); the model multiplied by the exact fraction, a difference of a cent. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $21,535.84
Model: $21,535.85
Work: 21,535.85 - 0 = 21,535.85

Ruling: model error; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct, owner's ruling); the model multiplied by the exact fraction, a difference of a cent. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $8,183.62

### case classm.scveh.5 — prompt sha256 1b4d9325c36c2c3b7d35be1e2c2908491dbf8af480a9ae7f885947539b3681eb; branches: scveh.owned:true, scveh.no_miles:false, scveh.over_half:true, scveh.employee_use:false, scveh.employee_bad:false, scveh.line9#1, scveh.is_actual_owned:true, scveh.on_auto_limits:true, scveh.is_actual_leased:false, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:true, scveh.is2025:true, scveh.is2019:false, scveh.s179_bad:false, scveh.after_jan19:true, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:true, scveh.lim_2025#0, scveh.line7#0, scveh.line10#0, scveh.line10_2025#0, scveh.s179_line10:left, scveh.line11:positive, scveh.line14#0, scveh.line15:positive, scveh.bonus_fullcase#0, scveh.bonus_2025#0, scveh.line16#0, scveh.bonus_allowed:left, scveh.line17:positive, scveh.line18:floor, scveh.line19#0, scveh.line19_earlier#0, scveh.line19_2025#0, scveh.line20:right, scveh.too_old:false, scveh.bonus_v#0, scveh.macrs_pass#0, scveh.macrs_heavy#0, scveh.macrs_v#0, scveh.bonus#0, scveh.macrs#0, scveh.s179_2025#0, scveh.mq_q4#0, scveh.mq_total#0, scveh.cost179#0, scveh.q4_basis#0, scveh.mq_q4_o#0, scveh.mq_total_o#0, scveh.cost179_o#0

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $929.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **AGREE**

Value: $4,998.73

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $20,200.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $20,194.87

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $20,194.87

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **AGREE**

Value: $4,998.73

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $4,998.73

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $4,998.73

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $15,196.14

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_a].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.scveh.1

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9"
    value: "980.70"
    work: "Standard mileage rate: 1,401 mi x 0.70 = 980.70; plus parking/tolls 0.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "0.00"
    work: "Standard mileage rate: no rent or lease payments are deducted"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9"
    value: "934.67"
    work: "Business use 5,624/8,122 = 69.244%; 440 x 69.244% = 304.67; plus parking/tolls 630 = 934.67"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line20a"
    value: "0.00"
    work: "Vehicle is owned, so there is no rent or lease"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bus_cost"
    value: "7534.44"
    work: "Worksheet line 13: 10,881 x 69.244% = 7,534.44"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line7"
    value: "5760.00"
    work: "Placed in service 2020; 2025 is year 6 (4th & later year) = $5,760"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9w"
    value: "3988.46"
    work: "5,760 x 69.244% = 3,988.46"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line10"
    value: "0.00"
    work: "Not the year placed in service, so enter -0-"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line11"
    value: "3988.46"
    work: "3,988.46 - 0 = 3,988.46"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line14"
    value: "6516.00"
    work: "Section 179 deduction claimed in 2020, as given"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line15"
    value: "1018.44"
    work: "7,534.44 - 6,516.00 = 1,018.44"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line16"
    value: "0.00"
    work: "Not the year placed in service, so enter -0-"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "Smaller of 0 and line 11 = 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line17"
    value: "3988.46"
    work: "3,988.46 - 0 = 3,988.46"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line18"
    value: "1018.44"
    work: "1,018.44 - 0 = 1,018.44"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19"
    value: "58.66"
    work: "Table A-1, 5-year property, HY, year 6 rate 5.76%; 1,018.44 x 0.0576 = 58.66"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line20"
    value: "58.66"
    work: "Lesser of 3,988.46 or 58.66"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9"
    value: "3162.05"
    work: "Business use 8,722/12,578 = 69.343%; 4,560 x 69.343% = 3,162.05; plus parking/tolls 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line20a"
    value: "0.00"
    work: "Vehicle is owned, so there is no rent or lease"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bus_cost"
    value: "24797.16"
    work: "35,760 x 69.343% = 24,797.16"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line7"
    value: "20200.00"
    work: "Placed in service 2025, year 1, special allowance taken = $20,200"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9w"
    value: "14007.35"
    work: "20,200 x 69.343% = 14,007.35"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line10"
    value: "0.00"
    work: "Elected section 179 cost is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line11"
    value: "14007.35"
    work: "14,007.35 - 0 = 14,007.35"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line14"
    value: "0.00"
    work: "No section 179 deduction claimed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line15"
    value: "24797.16"
    work: "24,797.16 - 0 = 24,797.16"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line16"
    value: "9918.86"
    work: "Elected 40% special allowance: 24,797.16 x 0.40 = 9,918.86"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_allowed"
    value: "9918.86"
    work: "Smaller of 9,918.86 and line 11 of 14,007.35"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line17"
    value: "4088.49"
    work: "14,007.35 - 9,918.86 = 4,088.49"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line18"
    value: "14878.30"
    work: "24,797.16 - 9,918.86 = 14,878.30"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19"
    value: "2975.66"
    work: "Mid-quarter test is no, so HY applies; Table A-1, 5-year property, year 1 rate 20%; 14,878.30 x 0.20 = 2,975.66"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line20"
    value: "2975.66"
    work: "Lesser of 4,088.49 or 2,975.66"
```
```

### classm.scveh.2

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9"
    value: "6517.00"
    work: "Business use 11364/12537 = 90.6437%; $6,509 x 11364/12537 = $5,900.00; plus parking and tolls $617 = $6,517.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "0.00"
    work: "Vehicle is owned, not leased, so there is no rent or lease cost"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bus_cost"
    value: "62561.37"
    work: "$69,019 x 11364/12537 = $62,561.37"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10"
    value: "0.00"
    work: "Elected section 179 cost is $0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line14"
    value: "0.00"
    work: "No section 179 was claimed in the year placed in service (2025)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line15"
    value: "62561.37"
    work: "Line 13 $62,561.37 - line 14 $0 = $62,561.37"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line16"
    value: "0.00"
    work: "Special depreciation allowance is none, so enter -0-"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line18"
    value: "62561.37"
    work: "Line 15 $62,561.37 - line 16 $0 = $62,561.37"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19"
    value: "3128.07"
    work: "5-yr 200DB, mid-quarter convention, Q4, year 1 rate 5.00% (Table A-5); $62,561.37 x 0.05 = $3,128.07; no passenger auto limit applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9"
    value: "6697.99"
    work: "Business use 11498/13254; $7,646 x 11498/13254 = $6,632.99; plus parking and tolls $65 = $6,697.99"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20a"
    value: "829.34"
    work: "Business portion of lease payments: $956 x 11498/13254 = $829.34"
```
```

### classm.scveh.3

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9"
    value: "665.28"
    work: "Actual costs $870 × business use (11,777 ÷ 15,401 = 76.47%) = $665.28. Depreciation goes on line 13, not here."
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "0.00"
    work: "The vehicle is owned, not leased, so there is no rent or lease amount."
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bus_cost"
    value: "4575.14"
    work: "$5,983 × 11,777 ÷ 15,401 = $4,575.14."
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line7"
    value: "5760.00"
    work: "Placed in service in 2019; 2025 is its 7th tax year (4th or later year). Table limit is $5,760."
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9w"
    value: "4404.62"
    work: "$5,760 × 11,777 ÷ 15,401 = $4,404.62."
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10"
    value: "0.00"
    work: "2025 is not the year the car was placed in service, so enter -0-."
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line11"
    value: "4404.62"
    work: "Line 9 $4,404.62 − line 10 $0 = $4,404.62."
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line14"
    value: "0.00"
    work: "Section 179 claimed in 2019 was $0."
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line15"
    value: "4575.14"
    work: "Line 13 $4,575.14 − line 14 $0 = $4,575.14."
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line16"
    value: "0.00"
    work: "Not the year placed in service, so enter -0-."
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "Smaller of line 16 ($0) or line 11, which is $0."
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line17"
    value: "4404.62"
    work: "Line 11 $4,404.62 − line 16 $0 = $4,404.62."
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line18"
    value: "4575.14"
    work: "Line 15 $4,575.14 − line 16 $0 = $4,575.14."
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19"
    value: "0.00"
    work: "The 5-year HY recovery period (2019–2024) has ended, so there is no 2025 table rate. Unrecovered basis is $0 because the limits never bound on a $5,983 cost."
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20"
    value: "0.00"
    work: "Lesser of line 17 ($4,404.62) or line 19 ($0) = $0."
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9"
    value: "9811.20"
    work: "Standard mileage rate: 14,016 miles × $0.70 + $0 parking and tolls = $9,811.20."
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20a"
    value: "0.00"
    work: "Under the standard mileage rate, no rent or lease payments are deducted."
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9"
    value: "911.00"
    work: "Actual costs $986 × business use (13,434 ÷ 14,540 = 92.39%) = $911.00."
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line20a"
    value: "0.00"
    work: "The vehicle is owned, not leased, so there is no rent or lease amount."
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bus_cost"
    value: "23212.92"
    work: "$25,124 × 13,434 ÷ 14,540 = $23,212.92."
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line7"
    value: "20200.00"
    work: "Placed in service in 2025, 1st year, with the 40% special allowance elected. Table limit is $20,200."
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9w"
    value: "18663.47"
    work: "$20,200 × 13,434 ÷ 14,540 = $18,663.47."
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line10"
    value: "18663.47"
    work: "Elected section 179 of $22,254 is capped at line 9, so $18,663.47."
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line11"
    value: "0.00"
    work: "Line 9 $18,663.47 − line 10 $18,663.47 = $0."
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line14"
    value: "18663.47"
    work: "Section 179 claimed in 2025, the year placed in service = $18,663.47."
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line15"
    value: "4549.45"
    work: "Line 13 $23,212.92 − line 14 $18,663.47 = $4,549.45."
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line16"
    value: "1819.78"
    work: "$4,549.45 × 40% = $1,819.78."
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "Smaller of line 16 ($1,819.78) or line 11 ($0) = $0."
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line17"
    value: "0.00"
    work: "Line 11 $0 − line 16 is less than zero, so $0."
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line18"
    value: "2729.67"
    work: "Line 15 $4,549.45 − line 16 $1,819.78 = $2,729.67."
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19"
    value: "545.93"
    work: "Mid-quarter test is no, so half-year convention applies. Table A-1, 5-year, year 1 rate 20%: $2,729.67 × 20% = $545.93."
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line20"
    value: "0.00"
    work: "Lesser of line 17 ($0) or line 19 ($545.93) = $0."
```
```

### classm.scveh.4

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9"
    value: "6972.70"
    work: "Standard mileage rate: 9,961 x 0.70 = 6,972.70; plus parking and tolls of 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "0.00"
    work: "Standard mileage rate: no rent or lease payments may be deducted"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9"
    value: "3745.10"
    work: "Business use 16,220/18,515 = 87.60%; 4,275 x 16,220/18,515 = 3,745.10"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20a"
    value: "0.00"
    work: "Vehicle is owned, not leased"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bus_cost"
    value: "21535.85"
    work: "Worksheet line 13: 24,583 x 16,220/18,515 = 21,535.85"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line10"
    value: "0.00"
    work: "Not the year placed in service (2024), so enter -0-"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line14"
    value: "0.00"
    work: "Section 179 claimed in the year placed in service = 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line15"
    value: "21535.85"
    work: "21,535.85 - 0 = 21,535.85"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line16"
    value: "0.00"
    work: "Not the year placed in service, so enter -0-"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line18"
    value: "21535.85"
    work: "21,535.85 - 0 = 21,535.85"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19"
    value: "8183.62"
    work: "Table A-5 (mid-quarter, 4th quarter), 5-year property, year 2 rate 38.00%; 21,535.85 x 0.38 = 8,183.62"
```
```

### classm.scveh.5

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9"
    value: "929.00"
    work: "Actual expenses: business portion of operating expenses $0.00 + parking and tolls $929.00 = $929.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "0.00"
    work: "Vehicle is owned, not leased, so there is no rent or lease cost"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bus_cost"
    value: "4998.73"
    work: "Business use 27,578/(27,578+0+7)=27,578/27,585; $5,000.00 x 27,578/27,585 = $4,998.73"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line7"
    value: "20200.00"
    work: "Placed in service 2025, 1st year, special allowance taken on qualified property: $20,200 (Pub 946 table, note 1)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9w"
    value: "20194.87"
    work: "$20,200 x 27,578/27,585 = $20,194.87"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10"
    value: "0.00"
    work: "No section 179 elected"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line11"
    value: "20194.87"
    work: "$20,194.87 - $0.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line14"
    value: "0.00"
    work: "No section 179 claimed in the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line15"
    value: "4998.73"
    work: "Line 13 $4,998.73 - line 14 $0.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line16"
    value: "4998.73"
    work: "Acquired after 1/19/2025, used more than 50% for business, full allowance: 100% x $4,998.73"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed"
    value: "4998.73"
    work: "Smaller of line 16 $4,998.73 or line 11 $20,194.87"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line17"
    value: "15196.14"
    work: "$20,194.87 - $4,998.73"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line18"
    value: "0.00"
    work: "$4,998.73 - $4,998.73"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19"
    value: "0.00"
    work: "$0.00 x 20% (5-year property, half-year convention, year 1)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20"
    value: "0.00"
    work: "Lesser of line 17 $15,196.14 or line 19 $0.00"
```
```
