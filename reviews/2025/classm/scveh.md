# Class M hand-work — scveh

`Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-11-02 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| prompt policy | worked-values-request-bound-v2 |
| system sha256 | 18ff9cfe094eedd0548bba02012b0ebf2a58d0606e834e3633432585b4192cb7 |
| reasoning effort | provider default |
| output token budget | transport default (65536 for DeepSeek) |
| subject sha256 | c09451e8f5d83628c129ec2426a47f0235b407cc6b518509f6b512b5e3979ce5 |
| cases | 5 |
| worked target scope | printed IRS lines |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 6, 7, 8, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 8, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 4, 5, 6, 7, 9, 10, 11, 13, 14, 15, 16 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 5, 6, 7, 9, 10, 11, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p946 | For use in preparing 2025 returns | 34, 37, 41, 59, 61, 62, 63, 71, 72, 73 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### case classm.scveh.1 — prompt sha256 3637e44b1b7472bddfb252b517c4c6a88b6306b136384c6b96b0c3939f733b8b; branches: scveh.owned:true, scveh.no_miles:false, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.line9#0, scveh.line9#1, scveh.is_actual_owned:false, scveh.is_actual_owned:true, scveh.is_actual_leased:false, scveh.lease_smr_before:false, scveh.lease_smr_bad:false, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:true, scveh.suv:false, scveh.is2025:false, scveh.is2025:true, scveh.is2019:false, scveh.is2019:true, scveh.s179_bad:false, scveh.after_jan19:false, scveh.after_jan19:true, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:false, scveh.claims_bonus:true, scveh.lim_2025#0, scveh.lim_2025#1, scveh.line7#0, scveh.line7#1, scveh.line10#0, scveh.line10#1, scveh.line10_2025#0, scveh.s179_line10:left, scveh.line11:positive, scveh.line14#0, scveh.line14#1, scveh.line15:positive, scveh.bonus_fullcase#0, scveh.bonus_fullcase#1, scveh.bonus_2025#1, scveh.bonus_2025#2, scveh.line16#0, scveh.line16#1, scveh.bonus_allowed:left, scveh.line17:positive, scveh.line18:positive, scveh.line19#0, scveh.line19#1, scveh.line19_earlier#0, scveh.line19_earlier#1, scveh.line19_2025#0, scveh.line20:right, scveh.b100:positive, scveh.d1:left, scveh.d1:right, scveh.d2:left, scveh.d2:right, scveh.d3:left, scveh.d3:right, scveh.d4:left, scveh.d4:right, scveh.d5:left, scveh.d5:right, scveh.d6:right, scveh.unrecovered:positive, scveh.post_amount:right, scveh.too_old:false, scveh.bonus_v#0, scveh.macrs_pass#0, scveh.macrs_pass#1, scveh.macrs_heavy#0, scveh.macrs_heavy#1, scveh.macrs_v#0, scveh.bonus#0, scveh.bonus#1, scveh.macrs#0, scveh.macrs#1, scveh.s179_2025#0, scveh.s179_2025#1, scveh.mq_q4#0, scveh.mq_q4#1, scveh.mq_total#0, scveh.mq_total#1, scveh.cost179#0, scveh.cost179#1, scveh.q4_basis#0, scveh.q4_basis#1, scveh.mq_q4_o#0, scveh.mq_q4_o#1, scveh.mq_total_o#0, scveh.mq_total_o#1, scveh.cost179_o#0, scveh.cost179_o#1

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $980.70

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $43,355.22
Model: $0.00
Work: Standard mileage rate: no depreciation, worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **DISAGREE**

Project: $5,760.00
Model: $0.00
Work: Standard mileage rate: no depreciation, worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **DISAGREE**

Project: $4,849.61
Model: $0.00
Work: Standard mileage rate: no depreciation, worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project: $4,849.61
Model: $0.00
Work: Standard mileage rate: no depreciation, worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $43,355.22
Model: $0.00
Work: Standard mileage rate: no depreciation, worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **DISAGREE**

Project: $4,849.61
Model: $0.00
Work: Standard mileage rate: no depreciation, worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $43,355.22
Model: $0.00
Work: Standard mileage rate: no depreciation, worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_a].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
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
Work: 5,760 × 5,624/8,122

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct); the model multiplied by the exact fraction, a difference of a cent. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project: $3,988.45
Model: $3,988.46
Work: 3,988.46 - 0.00

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct); the model multiplied by the exact fraction, a difference of a cent. [dropped]

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
Work: 3,988.46 - 0.00

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct); the model multiplied by the exact fraction, a difference of a cent. [dropped]

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

### case classm.scveh.2 — prompt sha256 242e2146c41d453cf4b878061a59d1fbe086343aaa2202d351fc44f28516793d; branches: scveh.owned:false, scveh.owned:true, scveh.no_miles:false, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.line9#1, scveh.is_actual_owned:false, scveh.is_actual_owned:true, scveh.is_actual_leased:false, scveh.is_actual_leased:true, scveh.lease_smr_before:false, scveh.lease_smr_bad:false, scveh.line20a#0, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:false, scveh.passenger:true, scveh.suv:false, scveh.is2025:false, scveh.is2025:true, scveh.is2019:false, scveh.s179_bad:false, scveh.after_jan19:false, scveh.after_jan19:true, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:false, scveh.lim_2025#1, scveh.line7#0, scveh.line7#1, scveh.line10#0, scveh.line10#1, scveh.line10_2025#0, scveh.line10_2025#1, scveh.s179_line10:left, scveh.line11:positive, scveh.line14#0, scveh.line14#1, scveh.line15:floor, scveh.line15:positive, scveh.bonus_fullcase#0, scveh.bonus_fullcase#1, scveh.bonus_2025#2, scveh.line16#0, scveh.line16#1, scveh.bonus_allowed:left, scveh.line17:positive, scveh.line18:floor, scveh.line18:positive, scveh.line19#0, scveh.line19#1, scveh.line19_earlier#0, scveh.line19_2025#1, scveh.line20:right, scveh.b100:floor, scveh.b100:positive, scveh.d1:right, scveh.d2:right, scveh.too_old:false, scveh.bonus_v#0, scveh.bonus_v#1, scveh.macrs_pass#0, scveh.macrs_heavy#0, scveh.macrs_v#0, scveh.macrs_v#1, scveh.bonus#0, scveh.bonus#1, scveh.macrs#0, scveh.macrs#1, scveh.s179_2025#0, scveh.s179_2025#1, scveh.mq_q4#0, scveh.mq_q4#1, scveh.mq_total#0, scveh.mq_total#1, scveh.cost179#0, scveh.cost179#1, scveh.q4_basis#2, scveh.q4_basis#3, scveh.mq_q4_o#0, scveh.mq_q4_o#1, scveh.mq_total_o#0, scveh.mq_total_o#1, scveh.cost179_o#0, scveh.cost179_o#1

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
Work: $69,019 x 11,364/12,537 (unrounded percentage; commuting miles 0)

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct); the model multiplied by the exact fraction, a difference of a cent. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **DISAGREE**

Project: $12,200.00
Model: $0.00
Work: Not subject to the passenger automobile limits, so no table limit applies; 0 is entered as not applicable (judgment call)

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **DISAGREE**

Project: $11,058.53
Model: $0.00
Work: Line 7 of $0 x 11,364/12,537; no limit applies

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project: $11,058.53
Model: $0.00
Work: $0 - $0; no limit applies to this vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $62,561.38
Model: $62,561.37
Work: Line 13 of $62,561.37 - line 14 of $0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct); the model multiplied by the exact fraction, a difference of a cent. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **DISAGREE**

Project: $11,058.53
Model: $0.00
Work: Line 11 of $0 - line 16 of $0; no limit applies to this vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $62,561.38
Model: $62,561.37
Work: Line 15 of $62,561.37 - line 16 of $0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct); the model multiplied by the exact fraction, a difference of a cent. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $3,128.07

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $3,128.07

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line9 — Car and truck expenses for this vehicle
Status: **DISAGREE**

Project: $6,698.00
Model: $6,697.99
Work: Actual method: business use 11,498/13,254; $7,646 x use = $6,632.99, plus $65 business parking and tolls

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct); the model multiplied by the exact fraction, a difference of a cent. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $829.34

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bus_cost — Business/investment cost (cost times business use)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **DISAGREE**

Project: $19,800.00
Model: $0.00
Work: Leased vehicle has no depreciation, so the worksheet table limit is not applied (judgment call)

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **DISAGREE**

Project: $17,176.74
Model: $0.00
Work: Leased vehicle; line 7 of $0 x business use

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project: $17,176.74
Model: $0.00
Work: $0 - $0; leased vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **DISAGREE**

Project: $17,176.74
Model: $0.00
Work: Line 11 of $0 - line 16 of $0

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line18 — Basis for depreciation (line 15 less line 16)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $0.00

### case classm.scveh.3 — prompt sha256 ab4fff46351525f379d66771b612c6973f77d186b0e8ba0b5677a5837c5e9390; branches: scveh.owned:true, scveh.no_miles:false, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.line9#0, scveh.line9#1, scveh.is_actual_owned:false, scveh.is_actual_owned:true, scveh.is_actual_leased:false, scveh.lease_smr_before:false, scveh.lease_smr_bad:false, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:true, scveh.suv:false, scveh.is2025:false, scveh.is2025:true, scveh.is2019:false, scveh.is2019:true, scveh.s179_bad:false, scveh.after_jan19:false, scveh.after_jan19:true, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:false, scveh.claims_bonus:true, scveh.lim_2025#0, scveh.lim_2025#1, scveh.line7#0, scveh.line7#1, scveh.line10#0, scveh.line10#1, scveh.line10_2025#0, scveh.s179_line10:left, scveh.s179_line10:right, scveh.line11:floor, scveh.line11:positive, scveh.line14#0, scveh.line14#1, scveh.line15:positive, scveh.bonus_fullcase#0, scveh.bonus_fullcase#1, scveh.bonus_2025#1, scveh.bonus_2025#2, scveh.line16#0, scveh.line16#1, scveh.bonus_allowed:left, scveh.bonus_allowed:right, scveh.line17:floor, scveh.line17:positive, scveh.line18:positive, scveh.line19#0, scveh.line19#1, scveh.line19_earlier#0, scveh.line19_earlier#1, scveh.line19_2025#0, scveh.line20:left, scveh.line20:right, scveh.b100:positive, scveh.d1:right, scveh.d2:right, scveh.d3:right, scveh.d4:right, scveh.d5:right, scveh.d6:right, scveh.unrecovered:floor, scveh.post_amount:right, scveh.too_old:false, scveh.bonus_v#0, scveh.macrs_pass#0, scveh.macrs_pass#1, scveh.macrs_heavy#0, scveh.macrs_heavy#1, scveh.macrs_v#0, scveh.bonus#0, scveh.bonus#1, scveh.macrs#0, scveh.macrs#1, scveh.s179_2025#0, scveh.s179_2025#1, scveh.mq_q4#0, scveh.mq_q4#1, scveh.mq_total#0, scveh.mq_total#1, scveh.cost179#0, scveh.cost179#1, scveh.q4_basis#1, scveh.mq_q4_o#0, scveh.mq_q4_o#1, scveh.mq_total_o#0, scveh.mq_total_o#1, scveh.cost179_o#0, scveh.cost179_o#1

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
Work: 5983.00 x 11777/15401 = 4575.14

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct); the model multiplied by the exact fraction, a difference of a cent. [dropped]

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
Work: 4575.14 - 0.00

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct); the model multiplied by the exact fraction, a difference of a cent. [dropped]

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
Work: 4575.14 - 0.00

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct); the model multiplied by the exact fraction, a difference of a cent. [dropped]

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

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $17,095.98
Model: $0.00
Work: Standard mileage rate: do not deduct depreciation; worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **DISAGREE**

Project: $19,800.00
Model: $0.00
Work: Standard mileage rate: depreciation worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **DISAGREE**

Project: $17,222.10
Model: $0.00
Work: Standard mileage rate: depreciation worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project: $17,222.10
Model: $0.00
Work: Standard mileage rate: depreciation worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $17,095.98
Model: $0.00
Work: Standard mileage rate: depreciation worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **DISAGREE**

Project: $17,222.10
Model: $0.00
Work: Standard mileage rate: depreciation worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $17,095.98
Model: $0.00
Work: Standard mileage rate: depreciation worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **DISAGREE**

Project: $5,812.63
Model: $0.00
Work: Standard mileage rate: depreciation worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **DISAGREE**

Project: $5,812.63
Model: $0.00
Work: Standard mileage rate: do not deduct depreciation

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

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

### case classm.scveh.4 — prompt sha256 07076af292215f6826ffd5ecfe3686f5fa68bc0170552d193a9bfac65d120d53; branches: scveh.owned:true, scveh.no_miles:false, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.line9#0, scveh.line9#1, scveh.is_actual_owned:false, scveh.is_actual_owned:true, scveh.is_actual_leased:false, scveh.lease_smr_before:false, scveh.lease_smr_bad:false, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:false, scveh.suv:false, scveh.is2025:false, scveh.is2019:false, scveh.is2019:true, scveh.s179_bad:false, scveh.after_jan19:true, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:false, scveh.lim_2025#1, scveh.line7#1, scveh.line10#1, scveh.line10_2025#1, scveh.s179_line10:left, scveh.line11:positive, scveh.line14#1, scveh.line15:positive, scveh.bonus_fullcase#0, scveh.bonus_2025#2, scveh.line16#1, scveh.bonus_allowed:left, scveh.line17:positive, scveh.line18:positive, scveh.line19#1, scveh.line19_earlier#0, scveh.line19_earlier#1, scveh.line19_2025#0, scveh.line20:right, scveh.b100:positive, scveh.d1:right, scveh.d2:left, scveh.d2:right, scveh.d3:left, scveh.d4:left, scveh.d5:left, scveh.d6:left, scveh.unrecovered:positive, scveh.post_amount:left, scveh.too_old:false, scveh.bonus_v#1, scveh.macrs_pass#0, scveh.macrs_pass#1, scveh.macrs_heavy#0, scveh.macrs_heavy#1, scveh.macrs_v#1, scveh.bonus#0, scveh.bonus#1, scveh.macrs#0, scveh.macrs#1, scveh.s179_2025#0, scveh.s179_2025#1, scveh.mq_q4#0, scveh.mq_q4#1, scveh.mq_total#0, scveh.mq_total#1, scveh.cost179#0, scveh.cost179#1, scveh.q4_basis#1, scveh.q4_basis#2, scveh.mq_q4_o#1, scveh.mq_total_o#1, scveh.cost179_o#1

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $6,972.70

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $39,085.35
Model: $0.00
Work: Standard mileage rate: do not deduct depreciation, so worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **DISAGREE**

Project: $5,760.00
Model: $0.00
Work: Standard mileage rate: depreciation worksheet not used; also not subject to the limits

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **DISAGREE**

Project: $3,253.86
Model: $0.00
Work: Standard mileage rate: depreciation worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project: $3,253.86
Model: $0.00
Work: Standard mileage rate: depreciation worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $39,085.35
Model: $0.00
Work: Standard mileage rate: depreciation worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **DISAGREE**

Project: $3,253.86
Model: $0.00
Work: Standard mileage rate: depreciation worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $39,085.35
Model: $0.00
Work: Standard mileage rate: depreciation worksheet not used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
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
Work: 24,583.00 x 16,220/18,515 (unrounded); total miles 16,220 + 0 + 2,295 = 18,515

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct); the model multiplied by the exact fraction, a difference of a cent. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **DISAGREE**

Project: $19,800.00
Model: $0.00
Work: Not subject to the passenger automobile limits, so no table maximum applies

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **DISAGREE**

Project: $17,345.71
Model: $0.00
Work: Line 7 of 0.00 x 87.60464%; no limit applies

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project: $17,345.71
Model: $0.00
Work: Line 9 of 0.00 less line 10 of 0.00; no limit applies

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $21,535.84
Model: $21,535.85
Work: Line 13 of 21,535.85 less line 14 of 0.00

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct); the model multiplied by the exact fraction, a difference of a cent. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **DISAGREE**

Project: $17,345.71
Model: $0.00
Work: Line 11 of 0.00 less line 16 of 0.00; no limit applies because vehicle is not subject to the limits

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry; these worksheet lines are read only for an owned passenger automobile on actual expenses (scveh.bonus_v, scveh.macrs_pass), so this amount reaches no return for this vehicle. The model entered zero as not applicable. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $21,535.84
Model: $21,535.85
Work: Line 15 of 21,535.85 less line 16 of 0.00

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (amb.2025.vehicle_business_pct); the model multiplied by the exact fraction, a difference of a cent. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $8,183.62

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $8,183.62

### case classm.scveh.5 — prompt sha256 bd68c7f1de04f84bff42bcbb51fce0bcbc876dbaa3ceb3c0a69b8a860e7f5ba5; branches: scveh.owned:true, scveh.no_miles:false, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.line9#1, scveh.is_actual_owned:true, scveh.is_actual_leased:false, scveh.lease_smr_before:false, scveh.lease_smr_bad:false, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:true, scveh.suv:false, scveh.is2025:true, scveh.is2019:false, scveh.s179_bad:false, scveh.after_jan19:true, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:true, scveh.lim_2025#0, scveh.line7#0, scveh.line10#0, scveh.line10_2025#0, scveh.s179_line10:left, scveh.line11:positive, scveh.line14#0, scveh.line15:positive, scveh.bonus_fullcase#0, scveh.bonus_2025#0, scveh.line16#0, scveh.bonus_allowed:left, scveh.line17:positive, scveh.line18:floor, scveh.line19#0, scveh.line19_earlier#0, scveh.line19_2025#0, scveh.line20:right, scveh.b100:positive, scveh.d1:right, scveh.too_old:false, scveh.bonus_v#0, scveh.macrs_pass#0, scveh.macrs_heavy#0, scveh.macrs_v#0, scveh.bonus#0, scveh.macrs#0, scveh.s179_2025#0, scveh.mq_q4#0, scveh.mq_total#0, scveh.cost179#0, scveh.q4_basis#0, scveh.mq_q4_o#0, scveh.mq_total_o#0, scveh.cost179_o#0

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
    work: "Standard rate allowed: 1,401 × 0.70 = 980.70 + parking/tolls 0.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "0.00"
    work: "Standard mileage rate: do not deduct rent or lease payments; vehicle is owned"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bus_cost"
    value: "0.00"
    work: "Standard mileage rate: no depreciation, worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line7"
    value: "0.00"
    work: "Standard mileage rate: no depreciation, worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9w"
    value: "0.00"
    work: "Standard mileage rate: no depreciation, worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10"
    value: "0.00"
    work: "Standard mileage rate: no depreciation, worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line11"
    value: "0.00"
    work: "Standard mileage rate: no depreciation, worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line14"
    value: "0.00"
    work: "Standard mileage rate: worksheet not used; section 179 given as 0.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line15"
    value: "0.00"
    work: "Standard mileage rate: no depreciation, worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line16"
    value: "0.00"
    work: "Standard mileage rate: no depreciation, worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "Standard mileage rate: no depreciation, worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line17"
    value: "0.00"
    work: "Standard mileage rate: no depreciation, worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line18"
    value: "0.00"
    work: "Standard mileage rate: no depreciation, worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19"
    value: "0.00"
    work: "Standard mileage rate: no depreciation, worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20"
    value: "0.00"
    work: "Standard mileage rate: no depreciation, worksheet not used"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9"
    value: "934.67"
    work: "440 × 5,624/8,122 = 304.67 business portion + 630.00 business parking/tolls"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line20a"
    value: "0.00"
    work: "Vehicle is owned, not leased, so no lease deduction"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bus_cost"
    value: "7534.44"
    work: "10,881 × 5,624/8,122 (69.244% business use)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line7"
    value: "5760.00"
    work: "Pub 946 limit table: placed in service 2020, 4th and later year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9w"
    value: "3988.46"
    work: "5,760 × 5,624/8,122"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line10"
    value: "0.00"
    work: "Enter -0-: 2025 is not the year placed in service"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line11"
    value: "3988.46"
    work: "3,988.46 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line14"
    value: "6516.00"
    work: "Section 179 claimed in the year placed in service, as given"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line15"
    value: "1018.44"
    work: "7,534.44 - 6,516.00"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line16"
    value: "0.00"
    work: "Enter -0-: 2025 is not the year placed in service"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "Smaller of line 16 (0.00) or line 11 (3,988.46)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line17"
    value: "3988.46"
    work: "3,988.46 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line18"
    value: "1018.44"
    work: "1,018.44 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19"
    value: "58.66"
    work: "1,018.44 × 5.76% (Table A-1, 5-year, half-year, year 6)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line20"
    value: "58.66"
    work: "Lesser of line 17 (3,988.46) or line 19 (58.66)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9"
    value: "3162.05"
    work: "4,560 × 8,722/12,578 = 3,162.05 + parking/tolls 0.00"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line20a"
    value: "0.00"
    work: "Vehicle is owned, not leased, so no lease deduction"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bus_cost"
    value: "24797.16"
    work: "35,760 × 8,722/12,578 (69.343% business use)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line7"
    value: "20200.00"
    work: "Placed in service 2025, 1st year, special allowance taken: limit 20,200"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9w"
    value: "14007.35"
    work: "20,200 × 8,722/12,578"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line10"
    value: "0.00"
    work: "Elected section 179 cost is 0.00"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line11"
    value: "14007.35"
    work: "14,007.35 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line14"
    value: "0.00"
    work: "Section 179 claimed in the year placed in service, as given"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line15"
    value: "24797.16"
    work: "24,797.16 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line16"
    value: "9918.86"
    work: "24,797.16 × 40%: acquired before January 20, 2025, placed in service 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_allowed"
    value: "9918.86"
    work: "Smaller of line 16 (9,918.86) or line 11 (14,007.35)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line17"
    value: "4088.49"
    work: "14,007.35 - 9,918.86"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line18"
    value: "14878.30"
    work: "24,797.16 - 9,918.86"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19"
    value: "2975.66"
    work: "14,878.30 × 20% (Table A-1, 5-year, half-year, year 1)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line20"
    value: "2975.66"
    work: "Lesser of line 17 (4,088.49) or line 19 (2,975.66)"
```
```

### classm.scveh.2

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9"
    value: "6517.00"
    work: "Actual method: business use 11,364/12,537; $6,509 x use = $5,900.00 (rounded), plus $617 business parking and tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "0.00"
    work: "Vehicle is owned, so there is no rent or lease deduction; the $226 lease entry is not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bus_cost"
    value: "62561.37"
    work: "$69,019 x 11,364/12,537 (unrounded percentage; commuting miles 0)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line7"
    value: "0.00"
    work: "Not subject to the passenger automobile limits, so no table limit applies; 0 is entered as not applicable (judgment call)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9w"
    value: "0.00"
    work: "Line 7 of $0 x 11,364/12,537; no limit applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10"
    value: "0.00"
    work: "Elected section 179 cost is $0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line11"
    value: "0.00"
    work: "$0 - $0; no limit applies to this vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line14"
    value: "0.00"
    work: "Section 179 claimed in the year placed in service is $0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line15"
    value: "62561.37"
    work: "Line 13 of $62,561.37 - line 14 of $0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line16"
    value: "0.00"
    work: "Special allowance choice for 5-year property is none, so enter -0-"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "Line 16 is $0, so no allowance is allowed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line17"
    value: "0.00"
    work: "Line 11 of $0 - line 16 of $0; no limit applies to this vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line18"
    value: "62561.37"
    work: "Line 15 of $62,561.37 - line 16 of $0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19"
    value: "3128.07"
    work: "$62,561.37 x 5.00% (Table A-5, mid-quarter Q4, 5-year, year 1; given q4 and test used, not the conflicting mq3 entry)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20"
    value: "3128.07"
    work: "Not subject to the limits, so line 17 does not cap the deduction; line 19 of $3,128.07 is used (judgment call)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9"
    value: "6697.99"
    work: "Actual method: business use 11,498/13,254; $7,646 x use = $6,632.99, plus $65 business parking and tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20a"
    value: "829.34"
    work: "Leased, actual method: $956 x 11,498/13,254; no inclusion amount data given"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bus_cost"
    value: "0.00"
    work: "Leased vehicle with cost of $0: $0 x business use"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line7"
    value: "0.00"
    work: "Leased vehicle has no depreciation, so the worksheet table limit is not applied (judgment call)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9w"
    value: "0.00"
    work: "Leased vehicle; line 7 of $0 x business use"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line10"
    value: "0.00"
    work: "Leased vehicle; elected section 179 cost is $0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line11"
    value: "0.00"
    work: "$0 - $0; leased vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line14"
    value: "0.00"
    work: "Section 179 claimed in the year placed in service is $0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line15"
    value: "0.00"
    work: "Line 13 of $0 - line 14 of $0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line16"
    value: "0.00"
    work: "Leased and not the year placed in service, so enter -0-"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_allowed"
    value: "0.00"
    work: "Line 16 is $0, so no allowance is allowed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line17"
    value: "0.00"
    work: "Line 11 of $0 - line 16 of $0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line18"
    value: "0.00"
    work: "Line 15 of $0 - line 16 of $0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19"
    value: "0.00"
    work: "Line 18 of $0 x any table rate = $0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20"
    value: "0.00"
    work: "Lesser of line 17 of $0 or line 19 of $0"
```
```

### classm.scveh.3

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9"
    value: "665.28"
    work: "Actual expenses, business portion: 870.00 x 11777/15401 (76.469%) = 665.28; no parking or tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "0.00"
    work: "Vehicle is owned and lease payments are 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bus_cost"
    value: "4575.14"
    work: "5983.00 x 11777/15401 = 4575.14"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line7"
    value: "5760.00"
    work: "Placed in service 2019; 2025 is a 4th-or-later year; limit is 5760"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9w"
    value: "4404.62"
    work: "5760.00 x 11777/15401 = 4404.62"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10"
    value: "0.00"
    work: "Not the year placed in service; enter -0-"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line11"
    value: "4404.62"
    work: "4404.62 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line14"
    value: "0.00"
    work: "Given section 179 deduction in the year placed in service is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line15"
    value: "4575.14"
    work: "4575.14 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line16"
    value: "0.00"
    work: "Not the year placed in service; enter -0-"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "Smaller of line 16 (0.00) or line 11 (4404.62)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line17"
    value: "4404.62"
    work: "4404.62 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line18"
    value: "4575.14"
    work: "4575.14 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19"
    value: "0.00"
    work: "Year 7 of 5-year property has no Table A-1 rate; basis fully recovered 2019-2024 since limits never applied, so unrecovered basis is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20"
    value: "0.00"
    work: "Lesser of line 17 (4404.62) or line 19 (0.00)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9"
    value: "9811.20"
    work: "Standard mileage: 14016 x 0.70 = 9811.20, plus 0.00 parking and tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20a"
    value: "0.00"
    work: "Standard mileage rate: do not deduct rent or lease payments"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bus_cost"
    value: "0.00"
    work: "Standard mileage rate: do not deduct depreciation; worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line7"
    value: "0.00"
    work: "Standard mileage rate: depreciation worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9w"
    value: "0.00"
    work: "Standard mileage rate: depreciation worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line10"
    value: "0.00"
    work: "Standard mileage rate: depreciation worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line11"
    value: "0.00"
    work: "Standard mileage rate: depreciation worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line14"
    value: "0.00"
    work: "Standard mileage rate: depreciation worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line15"
    value: "0.00"
    work: "Standard mileage rate: depreciation worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line16"
    value: "0.00"
    work: "Standard mileage rate: depreciation worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_allowed"
    value: "0.00"
    work: "Standard mileage rate: depreciation worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line17"
    value: "0.00"
    work: "Standard mileage rate: depreciation worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line18"
    value: "0.00"
    work: "Standard mileage rate: depreciation worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19"
    value: "0.00"
    work: "Standard mileage rate: depreciation worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20"
    value: "0.00"
    work: "Standard mileage rate: do not deduct depreciation"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9"
    value: "911.00"
    work: "Actual expenses, business portion: 986.00 x 13434/14540 (92.393%) = 911.00"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line20a"
    value: "0.00"
    work: "Vehicle is owned, not rented or leased, so the 2745.00 entry is not reported on line 20a"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bus_cost"
    value: "23212.92"
    work: "25124.00 x 13434/14540 = 23212.92"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line7"
    value: "20200.00"
    work: "Placed in service 2025, year 1, special allowance taken; limit is 20200"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9w"
    value: "18663.47"
    work: "20200.00 x 13434/14540 = 18663.47"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line10"
    value: "18663.47"
    work: "Elected 22254.00, limited to line 9 of 18663.47"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line11"
    value: "0.00"
    work: "18663.47 - 18663.47"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line14"
    value: "18663.47"
    work: "Placed in service this year, so the deduction claimed that year is line 10"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line15"
    value: "4549.45"
    work: "23212.92 - 18663.47"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line16"
    value: "1819.78"
    work: "4549.45 x 40% elected rate"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "Line 16 of 1819.78 limited to line 11 of 0.00"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line17"
    value: "0.00"
    work: "Line 11 of 0.00 less line 16; result floored at 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line18"
    value: "2729.67"
    work: "4549.45 - 1819.78"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19"
    value: "545.93"
    work: "2729.67 x 20.00%; mid-quarter test is no, so half-year Table A-1, 5-year, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line20"
    value: "0.00"
    work: "Lesser of line 17 (0.00) or line 19 (545.93)"
```
```

### classm.scveh.4

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9"
    value: "6972.70"
    work: "Standard mileage: 9,961 x 0.70 = 6,972.70, plus 0.00 parking and tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "0.00"
    work: "Standard mileage rate: do not deduct rent or lease payments; vehicle is also owned"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bus_cost"
    value: "0.00"
    work: "Standard mileage rate: do not deduct depreciation, so worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line7"
    value: "0.00"
    work: "Standard mileage rate: depreciation worksheet not used; also not subject to the limits"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9w"
    value: "0.00"
    work: "Standard mileage rate: depreciation worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10"
    value: "0.00"
    work: "Standard mileage rate; not the year placed in service (2019)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line11"
    value: "0.00"
    work: "Standard mileage rate: depreciation worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line14"
    value: "0.00"
    work: "Standard mileage rate: worksheet not used; section 179 claimed was 0.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line15"
    value: "0.00"
    work: "Standard mileage rate: depreciation worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line16"
    value: "0.00"
    work: "Not the year placed in service (2019): enter -0-"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "Line 16 is 0.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line17"
    value: "0.00"
    work: "Standard mileage rate: depreciation worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line18"
    value: "0.00"
    work: "Standard mileage rate: depreciation worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19"
    value: "0.00"
    work: "Standard mileage rate: depreciation worksheet not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20"
    value: "0.00"
    work: "Standard mileage rate: do not deduct depreciation"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9"
    value: "3745.10"
    work: "Actual expenses: 4,275.00 x 16,220/18,515 business use (87.60464%) = 3,745.10, with no parking or tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20a"
    value: "0.00"
    work: "Vehicle is owned, not leased, so the listed lease payments are not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bus_cost"
    value: "21535.85"
    work: "24,583.00 x 16,220/18,515 (unrounded); total miles 16,220 + 0 + 2,295 = 18,515"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line7"
    value: "0.00"
    work: "Not subject to the passenger automobile limits, so no table maximum applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9w"
    value: "0.00"
    work: "Line 7 of 0.00 x 87.60464%; no limit applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line10"
    value: "0.00"
    work: "Not the year placed in service (2024): enter -0-"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line11"
    value: "0.00"
    work: "Line 9 of 0.00 less line 10 of 0.00; no limit applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line14"
    value: "0.00"
    work: "Section 179 claimed in the year placed in service is given as 0.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line15"
    value: "21535.85"
    work: "Line 13 of 21,535.85 less line 14 of 0.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line16"
    value: "0.00"
    work: "Not the year placed in service (2024): enter -0-"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_allowed"
    value: "0.00"
    work: "Line 16 is 0.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line17"
    value: "0.00"
    work: "Line 11 of 0.00 less line 16 of 0.00; no limit applies because vehicle is not subject to the limits"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line18"
    value: "21535.85"
    work: "Line 15 of 21,535.85 less line 16 of 0.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19"
    value: "8183.62"
    work: "21,535.85 x 38.00% (Table A-5, 5-year, year 2; placed in service 2024, MQ fourth quarter)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20"
    value: "8183.62"
    work: "Judgment: line 19 used because the line 17 limit does not apply to a vehicle not subject to the passenger automobile limits"
```
```

### classm.scveh.5

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9"
    value: "929.00"
    work: "Actual method: business portion of operating expenses $0.00 ($0.00 x 99.9746%) + business parking and tolls $929.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "0.00"
    work: "Vehicle is owned, not leased, so the $3,251.00 lease amount is not entered on line 20a"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bus_cost"
    value: "4998.73"
    work: "Use 27,578 / 27,585 total miles = 99.9746%; $5,000.00 x 27,578 / 27,585 = $4,998.73"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line7"
    value: "20200.00"
    work: "Pub 946 passenger automobile table, placed in service 2025, 1st year, special allowance taken = $20,200"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9w"
    value: "20194.87"
    work: "$20,200 x 27,578 / 27,585 = $20,194.87"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10"
    value: "0.00"
    work: "Elected section 179 cost is $0.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line11"
    value: "20194.87"
    work: "Line 9 $20,194.87 - line 10 $0.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line14"
    value: "0.00"
    work: "Section 179 claimed in the year placed in service is $0.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line15"
    value: "4998.73"
    work: "Line 13 $4,998.73 - line 14 $0.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line16"
    value: "4998.73"
    work: "Acquired after Jan 19, 2025, full allowance: line 15 $4,998.73 x 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed"
    value: "4998.73"
    work: "Smaller of line 16 $4,998.73 or line 11 $20,194.87"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line17"
    value: "15196.14"
    work: "Line 11 $20,194.87 - line 16 $4,998.73"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line18"
    value: "0.00"
    work: "Line 15 $4,998.73 - line 16 $4,998.73"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19"
    value: "0.00"
    work: "Line 18 $0.00 x line 6 rate (half-year, 5-year property, year 1, 20%)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20"
    value: "0.00"
    work: "Lesser of line 17 $15,196.14 or line 19 $0.00"
```
```
