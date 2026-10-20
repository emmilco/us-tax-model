# Class M hand-work — scveh

`Schedule C line 9 and Part IV, and Form 4562 Part V — one vehicle used in a business` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 6 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 6, 7, 8, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 6, 7, 8, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| i4562 | 2025 | 4, 5, 6, 7, 9, 11, 13, 14, 15 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 5, 6, 7, 9, 11, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| n-25-05 | Notice 2025-5 | 1, 2, 3, 4, 5 | whole document | 394f6b5ffb7c30e745322f0f20d9137608b1e2429fc4c76b06dedd690d4fb6e3 | - | 349e2797f87c588214722bcd22b7ec317c86c90a255ec8496941ac0c09909a8d |
| p946 | For use in preparing 2025 returns | 34, 37, 41, 59, 61, 62, 63 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 34, 37, 41, 63 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |

## Lines

### case classm.scveh.1 — prompt sha256 dcbe84e0986070dd9d97508931bce122762a28534c661db41a6ad568574f80ab; branches: scveh.owned:false, scveh.owned:true, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.line9#1, scveh.is_actual_owned:false, scveh.is_actual_owned:true, scveh.is_actual_leased:false, scveh.is_actual_leased:true, scveh.line20a#0, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:false, scveh.passenger:true, scveh.suv:false, scveh.is2025:false, scveh.is2025:true, scveh.is2019:false, scveh.is2019:true, scveh.s179_bad:false, scveh.after_jan19:true, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:false, scveh.claims_bonus:true, scveh.lim_2025#0, scveh.lim_2025#1, scveh.line7#0, scveh.line7#1, scveh.line10#0, scveh.line10#1, scveh.line10_2025#0, scveh.line10_2025#1, scveh.s179_line10:left, scveh.line11:positive, scveh.line14#0, scveh.line14#1, scveh.line15:positive, scveh.bonus_fullcase#0, scveh.bonus_2025#0, scveh.bonus_2025#2, scveh.line16#0, scveh.line16#1, scveh.bonus_allowed:left, scveh.bonus_allowed:right, scveh.line17:floor, scveh.line17:positive, scveh.line18:floor, scveh.line18:positive, scveh.line19#0, scveh.line19#1, scveh.line19_earlier#0, scveh.line19_earlier#1, scveh.line19_2025#0, scveh.line20:left, scveh.line20:right, scveh.b100:positive, scveh.d1:right, scveh.d2:right, scveh.d3:right, scveh.d4:right, scveh.d5:right, scveh.d6:right, scveh.unrecovered:floor, scveh.post_amount:right, scveh.too_old:false, scveh.bonus_v#0, scveh.bonus_v#1, scveh.macrs_pass#0, scveh.macrs_pass#1, scveh.macrs_heavy#0, scveh.macrs_heavy#1, scveh.macrs_v#0, scveh.macrs_v#1, scveh.bonus#0, scveh.bonus#1, scveh.macrs#0, scveh.macrs#1, scveh.s179_2025#0, scveh.s179_2025#1, scveh.mq_q4#0, scveh.mq_q4#1, scveh.mq_total#0, scveh.mq_total#1, scveh.cost179#0, scveh.cost179#1, scveh.q4_basis#1, scveh.q4_basis#2, scveh.mq_q4_o#0, scveh.mq_q4_o#1, scveh.mq_total_o#0, scveh.mq_total_o#1, scveh.cost179_o#0, scveh.cost179_o#1

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $299.91
Model: $29,991.00
Work: 29,991 business miles

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].cm_c — Commuting miles, as cents
Status: **DISAGREE**

Project: $32.37
Model: $3,237.00
Work: 3,237 commuting miles

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $0.07
Model: $7.00
Work: 7 other miles

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $32.44
Model: $3,244.00
Work: 3,237 + 7

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $332.35
Model: $33,235.00
Work: 29,991 + 3,244

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $20,993.70

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $21,993.70

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $7,531.36

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $8,531.36

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $8,531.36

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: yes

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $6,508.95

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $6,508.95

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 1

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **AGREE**

Value: $49,166.83

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: yes

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].lim_first_bonus — First-year limit with the special allowance
Status: **AGREE**

Value: $20,200.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].lim_first_none — First-year limit without the special allowance
Status: **AGREE**

Value: $12,200.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].lim_2025 — Limit for a 2025 vehicle
Status: **AGREE**

Value: $20,200.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $20,200.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $20,200.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $18,228.32

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $18,228.32

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **AGREE**

Value: $49,166.83

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_full — 100% special allowance
Status: **AGREE**

Value: $49,166.83

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $19,666.73

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $49,166.83

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $49,166.83

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $49,166.83

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $18,228.32

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq2

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].rate_hy — MACRS rate, half-year convention
Status: **AGREE**

Value: 20%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].rate_mq — MACRS rate, mid-quarter convention
Status: **DISAGREE**

Project: 25%
Model: 15%
Work: 5-year 200DB MQ, 2nd quarter, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 20%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line19_hy — Line 18 times the half-year rate
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line19_mq — Line 18 times the mid-quarter rate
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $54,485.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 20%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $10,897.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].l1 — Year 1 limit (no special allowance)
Status: **AGREE**

Value: $12,200.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $10,897.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].d1 — Year 1 deduction allowable at 100% business use (the lesser of the limit or the 
Status: **AGREE**

Value: $10,897.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 32%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $17,435.20

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 19.2%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $10,461.12

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 11.52%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $6,276.67

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 11.52%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $6,276.67

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 5.76%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $3,138.34

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $18,228.32

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_v — Column (h)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_o — Special allowance (owned, actual expenses)
Status: **DISAGREE**

Project: $18,228.32
Model: $0.00
Work: Not owned

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_o — Depreciation (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].mq_total_o — mq_total (owned, actual expenses)
Status: **DISAGREE**

Project: $49,166.83
Model: $0.00
Work: Not owned

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].mq_total_a2 — mq_total of a 2025 vehicle
Status: **AGREE**

Value: $49,166.83

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].cost179_o — cost179 (owned, actual expenses)
Status: **DISAGREE**

Project: $49,166.83
Model: $0.00
Work: Not owned

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_1].cost179_a2 — cost179 of a 2025 vehicle
Status: **AGREE**

Value: $49,166.83

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $299.90
Model: $29,990.00
Work: 29,990 business miles

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].cm_c — Commuting miles, as cents
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $39.89
Model: $3,989.00
Work: 3,989 other miles

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $39.89
Model: $3,989.00
Work: 0 + 3,989

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $339.79
Model: $33,979.00
Work: 29,990 + 3,989

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $20,993.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $21,491.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $498.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $498.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: yes

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $2,837.57

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].year — Year of recovery in 2025
Status: **AGREE**

Value: 7

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: yes

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bus_cost — Business/investment cost (cost times business use)
Status: **AGREE**

Value: $4,413.02

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].lim_first_bonus — First-year limit with the special allowance
Status: **DISAGREE**

Project: $5,760.00
Model: $20,200.00
Work: 2025 table, 1st year

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].lim_first_none — First-year limit without the special allowance
Status: **DISAGREE**

Project: $10,100.00
Model: $12,200.00
Work: Footnote 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].lim_2025 — Limit for a 2025 vehicle
Status: **DISAGREE**

Project: $10,100.00
Model: $12,200.00
Work: No special allowance claimed

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $5,760.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $5,760.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $5,083.80

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $5,083.80

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **AGREE**

Value: $4,413.02

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_full — 100% special allowance
Status: **AGREE**

Value: $4,413.02

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $1,765.21

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $4,413.02

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $5,083.80

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line18 — Basis for depreciation (line 15 less line 16)
Status: **AGREE**

Value: $4,413.02

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq3

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $5,000.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 35%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $1,750.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].l1 — Year 1 limit (no special allowance)
Status: **AGREE**

Value: $10,100.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $1,750.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].d1 — Year 1 deduction allowable at 100% business use (the lesser of the limit or the 
Status: **AGREE**

Value: $1,750.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 26%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $1,300.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].l2 — Year 2 limit
Status: **AGREE**

Value: $16,100.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].d2 — Year 2 deduction allowable at 100% business use
Status: **AGREE**

Value: $1,300.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 15.6%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $780.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].l3 — Year 3 limit
Status: **AGREE**

Value: $9,700.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].d3 — Year 3 deduction allowable at 100% business use
Status: **AGREE**

Value: $780.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 11.01%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $550.50

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].l4 — Year 4 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].d4 — Year 4 deduction allowable at 100% business use
Status: **AGREE**

Value: $550.50

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 11.01%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $550.50

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].l5 — Year 5 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].d5 — Year 5 deduction allowable at 100% business use
Status: **AGREE**

Value: $550.50

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 1.38%

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $69.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].l6 — Year 6 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].d6 — Year 6 deduction allowable at 100% business use
Status: **AGREE**

Value: $69.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].d_total — Deductions allowable during the recovery period at 100% business use
Status: **AGREE**

Value: $5,000.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].unrecovered — Unrecovered basis at the end of the recovery period
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].post_amount — The lesser of the limit or the unrecovered basis
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].post — 2025 deduction after the recovery period (times the business use percentage)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_v — Column (h)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_o — Depreciation (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].mq_total_a2 — mq_total of a 2025 vehicle
Status: **DISAGREE**

Project: $4,413.02
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.1 — person[taxpayer].sc[biz_b].scveh[car_2].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $4,413.02
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### case classm.scveh.2 — prompt sha256 068c1de1c94af6e719a0f70b2787ef9e451790fb9c0e360101568b3935b14b4f; branches: scveh.owned:false, scveh.owned:true, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.line9#0, scveh.line9#1, scveh.is_actual_owned:false, scveh.is_actual_owned:true, scveh.is_actual_leased:false, scveh.is_actual_leased:true, scveh.line20a#0, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:true, scveh.suv:false, scveh.is2025:false, scveh.is2025:true, scveh.is2019:false, scveh.is2019:true, scveh.s179_bad:false, scveh.after_jan19:false, scveh.after_jan19:true, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:false, scveh.lim_2025#1, scveh.line7#0, scveh.line7#1, scveh.line10#0, scveh.line10#1, scveh.line10_2025#0, scveh.s179_line10:left, scveh.line11:positive, scveh.line14#0, scveh.line14#1, scveh.line15:positive, scveh.bonus_fullcase#0, scveh.bonus_fullcase#1, scveh.bonus_2025#2, scveh.line16#0, scveh.line16#1, scveh.bonus_allowed:left, scveh.line17:positive, scveh.line18:positive, scveh.line19#0, scveh.line19#1, scveh.line19_earlier#0, scveh.line19_earlier#1, scveh.line19_2025#1, scveh.line20:right, scveh.b100:positive, scveh.d1:left, scveh.d1:right, scveh.d2:left, scveh.d2:right, scveh.d3:left, scveh.d3:right, scveh.d4:left, scveh.d4:right, scveh.d5:left, scveh.d6:right, scveh.unrecovered:positive, scveh.post_amount:left, scveh.too_old:false, scveh.bonus_v#0, scveh.macrs_pass#0, scveh.macrs_pass#1, scveh.macrs_heavy#0, scveh.macrs_heavy#1, scveh.macrs_v#0, scveh.bonus#0, scveh.bonus#1, scveh.macrs#0, scveh.macrs#1, scveh.s179_2025#0, scveh.s179_2025#1, scveh.mq_q4#0, scveh.mq_q4#1, scveh.mq_total#0, scveh.mq_total#1, scveh.cost179#0, scveh.cost179#1, scveh.q4_basis#0, scveh.q4_basis#2, scveh.q4_basis#3, scveh.mq_q4_o#0, scveh.mq_q4_o#1, scveh.mq_total_o#0, scveh.mq_total_o#1, scveh.cost179_o#0, scveh.cost179_o#1

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $242.89
Model: $24,289.00
Work: Business miles 24,289

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].cm_c — Commuting miles, as cents
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $39.62
Model: $3,962.00
Work: Other miles 3,962

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $39.62
Model: $3,962.00
Work: 0 + 3,962

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $282.51
Model: $28,251.00
Work: 24,289 + 3,962

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $17,002.30

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $17,002.30

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].operating_business — The business portion of the operating expenses
Status: **DISAGREE**

Project: $4,585.08
Model: $4,585.09
Work: 5,333 x 24,289/28,251

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **DISAGREE**

Project: $4,585.08
Model: $4,585.09
Work: 4,585.09 + 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **DISAGREE**

Project: $4,585.08
Model: $4,585.09
Work: Actual expenses chosen

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: yes

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 4

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $23,668.25
Model: $23,668.26
Work: 27,529 x 24,289/28,251

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus — First-year limit with the special allowance
Status: **DISAGREE**

Project: $6,460.00
Model: $20,200.00
Work: 2025 first-year limit with special allowance

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $6,460.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $6,460.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $5,554.03

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $5,554.03

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $23,668.25
Model: $23,668.26
Work: 23,668.26 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_full — 100% special allowance
Status: **DISAGREE**

Project: $23,668.25
Model: $23,668.26
Work: Line 15 x 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $9,467.30

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **DISAGREE**

Project: $23,668.25
Model: $23,668.26
Work: Acquired after 1/19/2025, so 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $5,554.03

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $23,668.25
Model: $23,668.26
Work: 23,668.26 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq4

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].rate_hy — MACRS rate, half-year convention
Status: **DISAGREE**

Project: 11.52%
Model: 20%
Work: 5-year 200DB half-year, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].rate_mq — MACRS rate, mid-quarter convention
Status: **DISAGREE**

Project: 13.68%
Model: 5%
Work: 5-year mid-quarter Q4, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 11.52%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line19_hy — Line 18 times the half-year rate
Status: **DISAGREE**

Project: $2,726.58
Model: $4,733.65
Work: 23,668.26 x 20%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line19_mq — Line 18 times the mid-quarter rate
Status: **DISAGREE**

Project: $3,237.82
Model: $1,183.41
Work: 23,668.26 x 5%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **AGREE**

Value: $2,726.58

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $2,726.58

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $2,726.58

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **DISAGREE**

Project: $3,237.82
Model: $1,183.41
Work: Mid-quarter test is yes, so the MQ amount is used

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $2,726.58

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $27,529.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 20%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $5,505.80

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $5,505.80

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 32%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $8,809.28

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].l2 — Year 2 limit
Status: **AGREE**

Value: $18,000.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].d2 — Year 2 deduction allowable at 100% business use
Status: **AGREE**

Value: $8,809.28

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 19.2%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $5,285.57

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].l3 — Year 3 limit
Status: **AGREE**

Value: $10,800.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].d3 — Year 3 deduction allowable at 100% business use
Status: **AGREE**

Value: $5,285.57

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 11.52%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $3,171.34

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].l4 — Year 4 limit
Status: **AGREE**

Value: $6,460.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].d4 — Year 4 deduction allowable at 100% business use
Status: **AGREE**

Value: $3,171.34

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 11.52%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $3,171.34

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 5.76%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $1,585.67

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $2,726.58

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $2,726.58

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_v — Column (h)
Status: **AGREE**

Value: $2,726.58

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $2,726.58

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_o — Depreciation (owned, actual expenses)
Status: **AGREE**

Value: $2,726.58

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **DISAGREE**

Project: $23,668.25
Model: $23,668.26
Work: Q4; business cost less 0 section 179

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **DISAGREE**

Project: $23,668.25
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2 — mq_total of a 2025 vehicle
Status: **DISAGREE**

Project: $23,668.25
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $23,668.25
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $90.83
Model: $9,083.00
Work: Business miles 9,083

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].cm_c — Commuting miles, as cents
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $38.40
Model: $3,840.00
Work: Other miles 3,840

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $38.40
Model: $3,840.00
Work: 0 + 3,840

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $129.23
Model: $12,923.00
Work: 9,083 + 3,840

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $6,358.10

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $6,358.10

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $1,797.90

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $1,797.90

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $6,358.10

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $616.40

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].year — Year of recovery in 2025
Status: **AGREE**

Value: 7

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: yes

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $43,844.09
Model: $43,844.12
Work: 62,380 x 9,083/12,923

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].lim_first_bonus — First-year limit with the special allowance
Status: **DISAGREE**

Project: $5,760.00
Model: $20,200.00
Work: 2025 table, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].lim_first_none — First-year limit without the special allowance
Status: **DISAGREE**

Project: $10,100.00
Model: $12,200.00
Work: 2025 table footnote 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].lim_2025 — Limit for a 2025 vehicle
Status: **DISAGREE**

Project: $10,100.00
Model: $12,200.00
Work: No special allowance claimed

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $5,760.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $5,760.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **DISAGREE**

Project: $4,048.44
Model: $4,048.45
Work: 5,760 x 9,083/12,923

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project: $4,048.44
Model: $4,048.45
Work: 4,048.45 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $43,844.09
Model: $43,844.12
Work: 43,844.12 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_full — 100% special allowance
Status: **DISAGREE**

Project: $43,844.09
Model: $43,844.12
Work: Line 15 x 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_forty — 40% special allowance
Status: **DISAGREE**

Project: $17,537.64
Model: $17,537.65
Work: Line 15 x 40%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **DISAGREE**

Project: $17,537.64
Model: $17,537.65
Work: Not acquired after 1/19/2025, so 40%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_2025 — Special allowance for a 2025 vehicle
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

Project: $4,048.44
Model: $4,048.45
Work: 4,048.45 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $43,844.09
Model: $43,844.12
Work: 43,844.12 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq1

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $62,380.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 20%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $12,476.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].l1 — Year 1 limit (no special allowance)
Status: **AGREE**

Value: $10,100.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $12,476.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].d1 — Year 1 deduction allowable at 100% business use (the lesser of the limit or the 
Status: **AGREE**

Value: $10,100.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 32%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $19,961.60

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].l2 — Year 2 limit
Status: **AGREE**

Value: $16,100.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].d2 — Year 2 deduction allowable at 100% business use
Status: **AGREE**

Value: $16,100.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 19.2%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $11,976.96

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].l3 — Year 3 limit
Status: **AGREE**

Value: $9,700.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].d3 — Year 3 deduction allowable at 100% business use
Status: **AGREE**

Value: $9,700.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 11.52%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $7,186.18

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].l4 — Year 4 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].d4 — Year 4 deduction allowable at 100% business use
Status: **AGREE**

Value: $5,760.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 11.52%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $7,186.18

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].l5 — Year 5 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].d5 — Year 5 deduction allowable at 100% business use
Status: **AGREE**

Value: $5,760.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 5.76%

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $3,593.09

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].l6 — Year 6 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].d6 — Year 6 deduction allowable at 100% business use
Status: **AGREE**

Value: $3,593.09

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].d_total — Deductions allowable during the recovery period at 100% business use
Status: **AGREE**

Value: $51,013.09

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].unrecovered — Unrecovered basis at the end of the recovery period
Status: **AGREE**

Value: $11,366.91

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].post_amount — The lesser of the limit or the unrecovered basis
Status: **AGREE**

Value: $5,760.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].post — 2025 deduction after the recovery period (times the business use percentage)
Status: **DISAGREE**

Project: $4,048.44
Model: $4,048.45
Work: 5,760 x 9,083/12,923

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_pass — Column (h) for a passenger automobile
Status: **DISAGREE**

Project: $4,048.44
Model: $4,048.45
Work: 2019 vehicle: post-recovery amount

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_v — Column (h)
Status: **DISAGREE**

Project: $4,048.44
Model: $4,048.45
Work: Subject to the passenger auto limits

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_o — Depreciation (owned, actual expenses)
Status: **DISAGREE**

Project: $4,048.44
Model: $0.00
Work: Not owned with actual expenses

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total_a2 — mq_total of a 2025 vehicle
Status: **DISAGREE**

Project: $43,844.09
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_a].scveh[car_2].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $43,844.09
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $31.35
Model: $3,135.00
Work: Business miles 3,135

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].cm_c — Commuting miles, as cents
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $4.07
Model: $407.00
Work: Other miles 407

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $4.07
Model: $407.00
Work: 0 + 407

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $35.42
Model: $3,542.00
Work: 3,135 + 407

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $2,194.50

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $2,194.50

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $1,339.15

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $1,339.15

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $2,194.50

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $2,418.96

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 1

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **AGREE**

Value: $12,031.07

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].lim_first_bonus — First-year limit with the special allowance
Status: **AGREE**

Value: $20,200.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].lim_first_none — First-year limit without the special allowance
Status: **AGREE**

Value: $12,200.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].lim_2025 — Limit for a 2025 vehicle
Status: **AGREE**

Value: $12,200.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $20,200.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $12,200.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **DISAGREE**

Project: $10,798.13
Model: $10,798.14
Work: 12,200 x 3,135/3,542

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project: $10,798.13
Model: $10,798.14
Work: 10,798.14 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **AGREE**

Value: $12,031.07

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_full — 100% special allowance
Status: **AGREE**

Value: $12,031.07

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $4,812.43

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $12,031.07

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **DISAGREE**

Project: $10,798.13
Model: $10,798.14
Work: 10,798.14 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **AGREE**

Value: $12,031.07

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq1

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].rate_hy — MACRS rate, half-year convention
Status: **AGREE**

Value: 20%

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].rate_mq — MACRS rate, mid-quarter convention
Status: **AGREE**

Value: 35%

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 5%

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line19_hy — Line 18 times the half-year rate
Status: **AGREE**

Value: $2,406.21

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line19_mq — Line 18 times the mid-quarter rate
Status: **AGREE**

Value: $4,210.87

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **AGREE**

Value: $601.55

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $4,210.87

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $601.55

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **AGREE**

Value: $4,210.87

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $4,210.87

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $13,593.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 5%

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $679.65

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].l1 — Year 1 limit (no special allowance)
Status: **AGREE**

Value: $12,200.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $679.65

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].d1 — Year 1 deduction allowable at 100% business use (the lesser of the limit or the 
Status: **AGREE**

Value: $679.65

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 38%

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $5,165.34

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 22.8%

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $3,099.20

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 13.68%

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $1,859.52

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 10.94%

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $1,487.07

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 9.58%

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $1,302.21

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $4,210.87

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $4,210.87

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_v — Column (h)
Status: **AGREE**

Value: $4,210.87

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_o — Depreciation (owned, actual expenses)
Status: **DISAGREE**

Project: $4,210.87
Model: $0.00
Work: Not owned with actual expenses

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].mq_total_o — mq_total (owned, actual expenses)
Status: **DISAGREE**

Project: $12,031.07
Model: $0.00
Work: Not owned with actual expenses

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].mq_total_a2 — mq_total of a 2025 vehicle
Status: **AGREE**

Value: $12,031.07

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].cost179_o — cost179 (owned, actual expenses)
Status: **DISAGREE**

Project: $12,031.07
Model: $0.00
Work: Not owned with actual expenses

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_1].cost179_a2 — cost179 of a 2025 vehicle
Status: **AGREE**

Value: $12,031.07

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $38.30
Model: $3,830.00
Work: Business miles 3,830

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].cm_c — Commuting miles, as cents
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $0.78
Model: $78.00
Work: Other miles 78

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $0.78
Model: $78.00
Work: 0 + 78

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $39.08
Model: $3,908.00
Work: 3,830 + 78

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $2,681.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $2,681.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: yes

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].year — Year of recovery in 2025
Status: **AGREE**

Value: 1

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].bus_cost — Business/investment cost (cost times business use)
Status: **AGREE**

Value: $76,802.87

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].lim_first_bonus — First-year limit with the special allowance
Status: **AGREE**

Value: $20,200.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].lim_first_none — First-year limit without the special allowance
Status: **AGREE**

Value: $12,200.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].lim_2025 — Limit for a 2025 vehicle
Status: **AGREE**

Value: $12,200.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $20,200.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $12,200.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $11,956.50

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $11,956.50

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **AGREE**

Value: $76,802.87

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_full — 100% special allowance
Status: **AGREE**

Value: $76,802.87

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $30,721.15

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $76,802.87

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $11,956.50

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line18 — Basis for depreciation (line 15 less line 16)
Status: **AGREE**

Value: $76,802.87

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq3

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].rate_hy — MACRS rate, half-year convention
Status: **AGREE**

Value: 20%

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].rate_mq — MACRS rate, mid-quarter convention
Status: **AGREE**

Value: 15%

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 20%

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line19_hy — Line 18 times the half-year rate
Status: **AGREE**

Value: $15,360.57

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line19_mq — Line 18 times the mid-quarter rate
Status: **AGREE**

Value: $11,520.43

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **AGREE**

Value: $15,360.57

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $11,520.43

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $15,360.57

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **AGREE**

Value: $11,520.43

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $11,520.43

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $78,367.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 20%

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $15,673.40

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].l1 — Year 1 limit (no special allowance)
Status: **AGREE**

Value: $12,200.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $15,673.40

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].d1 — Year 1 deduction allowable at 100% business use (the lesser of the limit or the 
Status: **AGREE**

Value: $12,200.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 32%

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $25,077.44

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 19.2%

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $15,046.46

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 11.52%

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $9,027.88

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 11.52%

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $9,027.88

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 5.76%

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $4,513.94

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $11,520.43

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $11,520.43

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_v — Column (h)
Status: **AGREE**

Value: $11,520.43

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_o — Depreciation (owned, actual expenses)
Status: **DISAGREE**

Project: $11,520.43
Model: $0.00
Work: Not owned

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].mq_total_o — mq_total (owned, actual expenses)
Status: **DISAGREE**

Project: $76,802.87
Model: $0.00
Work: Not owned

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].mq_total_a2 — mq_total of a 2025 vehicle
Status: **AGREE**

Value: $76,802.87

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].cost179_o — cost179 (owned, actual expenses)
Status: **DISAGREE**

Project: $76,802.87
Model: $0.00
Work: Not owned

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.2 — person[taxpayer].sc[biz_b].scveh[car_2].cost179_a2 — cost179 of a 2025 vehicle
Status: **AGREE**

Value: $76,802.87

### case classm.scveh.3 — prompt sha256 27b1d718ea57cfaae00271e2788bfacb8aed5373f440000cafec34bf8b9a08bf; branches: scveh.owned:false, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.line9#0, scveh.line9#1, scveh.is_actual_owned:false, scveh.is_actual_leased:false, scveh.is_actual_leased:true, scveh.line20a#0, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:true, scveh.suv:false, scveh.is2025:false, scveh.is2019:false, scveh.s179_bad:false, scveh.after_jan19:true, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:false, scveh.lim_2025#1, scveh.line7#1, scveh.line10#1, scveh.line10_2025#0, scveh.s179_line10:left, scveh.line11:positive, scveh.line14#1, scveh.line15:floor, scveh.line15:positive, scveh.bonus_fullcase#0, scveh.bonus_2025#2, scveh.line16#1, scveh.bonus_allowed:left, scveh.line17:positive, scveh.line18:floor, scveh.line18:positive, scveh.line19#1, scveh.line19_earlier#0, scveh.line19_2025#0, scveh.line20:right, scveh.b100:floor, scveh.b100:positive, scveh.d2:right, scveh.d3:right, scveh.d4:right, scveh.d5:right, scveh.too_old:false, scveh.bonus_v#0, scveh.macrs_pass#0, scveh.macrs_heavy#0, scveh.macrs_v#0, scveh.bonus#1, scveh.macrs#1, scveh.s179_2025#1, scveh.mq_q4#1, scveh.mq_total#1, scveh.cost179#1, scveh.q4_basis#2, scveh.mq_q4_o#1, scveh.mq_total_o#1, scveh.cost179_o#1

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $144.64
Model: $14,464.00
Work: Business miles 14,464

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].cm_c — Commuting miles, as cents
Status: **DISAGREE**

Project: $31.65
Model: $3,165.00
Work: Commuting miles 3,165

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $30.75
Model: $3,075.00
Work: Other miles 3,075

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $62.40
Model: $6,240.00
Work: 3,165 + 3,075

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $207.04
Model: $20,704.00
Work: 14,464 + 6,240

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $10,124.80

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $10,124.80

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $2,325.67

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $2,325.67

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $2,325.67

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: yes

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $3,140.25

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $3,140.25

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 5

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $3,493.05
Model: $3,493.04
Work: 5,000 x 69.86%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus — First-year limit with the special allowance
Status: **DISAGREE**

Project: $5,860.00
Model: $20,200.00
Work: 2025 first-year limit with the special allowance

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $5,860.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $5,860.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $4,093.85

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $4,093.85

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $5,000.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_full — 100% special allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $4,093.85

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq3

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].rate_hy — MACRS rate, half-year convention
Status: **DISAGREE**

Project: 11.52%
Model: 20%
Work: 5-year, 200DB, half-year convention, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].rate_mq — MACRS rate, mid-quarter convention
Status: **DISAGREE**

Project: 11.3%
Model: 15%
Work: 5-year, mid-quarter Q3, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 10.94%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line19_hy — Line 18 times the half-year rate
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line19_mq — Line 18 times the mid-quarter rate
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 5%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $5,000.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 38%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].l2 — Year 2 limit
Status: **AGREE**

Value: $16,400.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].d2 — Year 2 deduction allowable at 100% business use
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 22.8%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].l3 — Year 3 limit
Status: **AGREE**

Value: $9,800.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].d3 — Year 3 deduction allowable at 100% business use
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 13.68%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].l4 — Year 4 limit
Status: **AGREE**

Value: $5,860.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].d4 — Year 4 deduction allowable at 100% business use
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 10.94%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].l5 — Year 5 limit
Status: **AGREE**

Value: $5,860.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].d5 — Year 5 deduction allowable at 100% business use
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 9.58%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_v — Column (h)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_o — Depreciation (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2 — mq_total of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $3,493.05
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $160.03
Model: $16,003.00
Work: Business miles 16,003

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].cm_c — Commuting miles, as cents
Status: **DISAGREE**

Project: $29.10
Model: $2,910.00
Work: Commuting miles 2,910

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $0.04
Model: $4.00
Work: Other miles 4

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $29.14
Model: $2,914.00
Work: 2,910 + 4

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $189.17
Model: $18,917.00
Work: 16,003 + 2,914

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $11,202.10

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $11,202.10

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $3,438.82

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $3,438.82

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $11,202.10

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $6,767.67

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].year — Year of recovery in 2025
Status: **AGREE**

Value: 4

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $34,906.81
Model: $34,906.79
Work: 41,263 x 16,003 / 18,917

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].lim_first_bonus — First-year limit with the special allowance
Status: **DISAGREE**

Project: $6,460.00
Model: $20,200.00
Work: 2025 first-year limit with the special allowance

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $6,460.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $6,460.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **DISAGREE**

Project: $5,464.90
Model: $5,464.89
Work: 6,460 x 16,003 / 18,917

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project: $5,464.90
Model: $5,464.89
Work: 5,464.89 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $2,368.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $32,538.81
Model: $32,538.79
Work: 34,906.79 - 2,368

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_full — 100% special allowance
Status: **DISAGREE**

Project: $32,538.81
Model: $0.00
Work: No allowance claimed, so 0

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_forty — 40% special allowance
Status: **DISAGREE**

Project: $13,015.52
Model: $0.00
Work: No allowance claimed, so 0

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **DISAGREE**

Project: $32,538.81
Model: $0.00
Work: No allowance claimed, so 0

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **DISAGREE**

Project: $5,464.90
Model: $5,464.89
Work: 5,464.89 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $32,538.81
Model: $32,538.79
Work: 32,538.79 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq3

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].rate_hy — MACRS rate, half-year convention
Status: **DISAGREE**

Project: 11.52%
Model: 20%
Work: 5-year, half-year convention, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].rate_mq — MACRS rate, mid-quarter convention
Status: **DISAGREE**

Project: 12.24%
Model: 15%
Work: 5-year, mid-quarter Q3, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 11.52%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line19_hy — Line 18 times the half-year rate
Status: **DISAGREE**

Project: $3,748.47
Model: $6,507.76
Work: 32,538.79 x 20%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line19_mq — Line 18 times the mid-quarter rate
Status: **DISAGREE**

Project: $3,982.75
Model: $4,880.82
Work: 32,538.79 x 15%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **AGREE**

Value: $3,748.47

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $3,748.47

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $3,748.47

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **DISAGREE**

Project: $3,748.47
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $3,748.47

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $38,895.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 20%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $7,779.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $10,147.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 32%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $12,446.40

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].l2 — Year 2 limit
Status: **AGREE**

Value: $18,000.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].d2 — Year 2 deduction allowable at 100% business use
Status: **AGREE**

Value: $12,446.40

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 19.2%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $7,467.84

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].l3 — Year 3 limit
Status: **AGREE**

Value: $10,800.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].d3 — Year 3 deduction allowable at 100% business use
Status: **AGREE**

Value: $7,467.84

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 11.52%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $4,480.70

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].l4 — Year 4 limit
Status: **AGREE**

Value: $6,460.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].d4 — Year 4 deduction allowable at 100% business use
Status: **AGREE**

Value: $4,480.70

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 11.52%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $4,480.70

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 5.76%

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $2,240.35

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $3,748.47

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $3,748.47

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_v — Column (h)
Status: **AGREE**

Value: $3,748.47

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_o — Depreciation (owned, actual expenses)
Status: **DISAGREE**

Project: $3,748.47
Model: $0.00
Work: Not owned on actual expenses

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total_a2 — mq_total of a 2025 vehicle
Status: **DISAGREE**

Project: $32,538.81
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.3 — person[taxpayer].sc[biz_a].scveh[car_2].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $34,906.81
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### case classm.scveh.4 — prompt sha256 7ca3874591428429f226dc82727d57e2d11869302da17ac501fb704d73cb578d; branches: scveh.owned:true, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.line9#1, scveh.is_actual_owned:true, scveh.is_actual_leased:false, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:true, scveh.suv:false, scveh.is2025:false, scveh.is2025:true, scveh.is2019:false, scveh.s179_bad:false, scveh.after_jan19:true, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:false, scveh.lim_2025#1, scveh.line7#0, scveh.line7#1, scveh.line10#0, scveh.line10#1, scveh.line10_2025#0, scveh.s179_line10:left, scveh.s179_line10:right, scveh.line11:floor, scveh.line11:positive, scveh.line14#0, scveh.line14#1, scveh.line15:positive, scveh.bonus_fullcase#0, scveh.bonus_2025#2, scveh.line16#0, scveh.line16#1, scveh.bonus_allowed:left, scveh.line17:floor, scveh.line17:positive, scveh.line18:positive, scveh.line19#0, scveh.line19#1, scveh.line19_earlier#0, scveh.line19_2025#1, scveh.line20:left, scveh.line20:right, scveh.b100:positive, scveh.d1:right, scveh.d2:left, scveh.d3:left, scveh.d4:left, scveh.d5:left, scveh.d6:right, scveh.too_old:false, scveh.bonus_v#0, scveh.macrs_pass#0, scveh.macrs_heavy#0, scveh.macrs_v#0, scveh.bonus#0, scveh.macrs#0, scveh.s179_2025#0, scveh.mq_q4#0, scveh.mq_total#0, scveh.cost179#0, scveh.q4_basis#0, scveh.q4_basis#3, scveh.mq_q4_o#0, scveh.mq_q4_o#1, scveh.mq_total_o#0, scveh.mq_total_o#1, scveh.cost179_o#0, scveh.cost179_o#1

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $271.86
Model: $27,186.00
Work: Business miles 27,186

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].cm_c — Commuting miles, as cents
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $31.77
Model: $3,177.00
Work: Other miles 3,177

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $31.77
Model: $3,177.00
Work: 0 + 3,177

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $303.63
Model: $30,363.00
Work: 27,186 + 3,177

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $19,030.20

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $19,030.20

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $4,402.51

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $4,402.51

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $4,402.51

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: yes

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 1

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **AGREE**

Value: $22,276.71

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus — First-year limit with the special allowance
Status: **AGREE**

Value: $20,200.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].lim_first_none — First-year limit without the special allowance
Status: **AGREE**

Value: $12,200.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].lim_2025 — Limit for a 2025 vehicle
Status: **AGREE**

Value: $12,200.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **DISAGREE**

Project: $20,200.00
Model: $0.00
Work: Not a prior-year vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $12,200.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $10,923.47

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $14,596.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $10,923.47

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $10,923.47

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $10,923.47

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $10,923.47

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **AGREE**

Value: $11,353.24

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_full — 100% special allowance
Status: **AGREE**

Value: $11,353.24

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $4,541.30

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **AGREE**

Value: $11,353.24

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **AGREE**

Value: $11,353.24

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq4

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].rate_hy — MACRS rate, half-year convention
Status: **AGREE**

Value: 20%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].rate_mq — MACRS rate, mid-quarter convention
Status: **AGREE**

Value: 5%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 20%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line19_hy — Line 18 times the half-year rate
Status: **AGREE**

Value: $2,270.65

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line19_mq — Line 18 times the mid-quarter rate
Status: **AGREE**

Value: $567.66

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **AGREE**

Value: $2,270.65

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $567.66

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **DISAGREE**

Project: $2,270.65
Model: $0.00
Work: 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **AGREE**

Value: $567.66

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **DISAGREE**

Project: $24,880.00
Model: $13,956.53
Work: 24,880 - 10,923.47

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 20%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].t1 — Year 1 MACRS amount as if used 100% for business
Status: **DISAGREE**

Project: $4,976.00
Model: $2,791.31
Work: 13,956.53 x 20%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].l1 — Year 1 limit (no special allowance)
Status: **AGREE**

Value: $12,200.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **DISAGREE**

Project: $4,976.00
Model: $13,714.78
Work: 10,923.47 + 2,791.31

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].d1 — Year 1 deduction allowable at 100% business use (the lesser of the limit or the 
Status: **DISAGREE**

Project: $4,976.00
Model: $12,200.00
Work: Lesser of 12,200 or 13,714.78

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 32%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].t2 — Year 2 MACRS amount as if used 100% for business
Status: **DISAGREE**

Project: $7,961.60
Model: $4,466.09
Work: 13,956.53 x 32%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 19.2%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].t3 — Year 3 MACRS amount as if used 100% for business
Status: **DISAGREE**

Project: $4,776.96
Model: $2,679.65
Work: 13,956.53 x 19.2%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 11.52%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].t4 — Year 4 MACRS amount as if used 100% for business
Status: **DISAGREE**

Project: $2,866.18
Model: $1,607.79
Work: 13,956.53 x 11.52%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 11.52%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].t5 — Year 5 MACRS amount as if used 100% for business
Status: **DISAGREE**

Project: $2,866.18
Model: $1,607.79
Work: 13,956.53 x 11.52%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 5.76%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].t6 — Year 6 MACRS amount as if used 100% for business
Status: **DISAGREE**

Project: $1,433.09
Model: $803.90
Work: 13,956.53 x 5.76%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $567.66

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_v — Column (h)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $10,923.47

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $11,353.24

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $11,353.24

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $22,276.71

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_o — Depreciation (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $10,923.47

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **AGREE**

Value: $11,353.24

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $11,353.24

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $11,353.24

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $11,353.24

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2 — mq_total of a 2025 vehicle
Status: **AGREE**

Value: $11,353.24

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $22,276.71

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2 — cost179 of a 2025 vehicle
Status: **AGREE**

Value: $22,276.71

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $297.02
Model: $29,702.00
Work: Business miles 29,702

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].cm_c — Commuting miles, as cents
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $31.85
Model: $3,185.00
Work: Other miles 3,185

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $31.85
Model: $3,185.00
Work: 0 + 3,185

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $328.87
Model: $32,887.00
Work: 29,702 + 3,185

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $20,791.40

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $20,791.40

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $137.28

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $137.28

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $137.28

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: yes

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $3,096.01

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].year — Year of recovery in 2025
Status: **AGREE**

Value: 6

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $55,566.49
Model: $55,566.50
Work: 61,525 x 29,702/32,887

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].lim_first_bonus — First-year limit with the special allowance
Status: **DISAGREE**

Project: $5,760.00
Model: $18,100.00
Work: Pub 946 table, 2020 1st year

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $5,760.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $5,760.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $5,202.16

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $5,202.16

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $55,566.49
Model: $55,566.50
Work: 55,566.50 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_full — 100% special allowance
Status: **DISAGREE**

Project: $55,566.49
Model: $55,566.50
Work: 55,566.50 x 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $22,226.60

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **DISAGREE**

Project: $55,566.49
Model: $55,566.50
Work: Acquired after Jan 19, 2025 = yes

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $5,202.16

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $55,566.49
Model: $55,566.50
Work: 55,566.50 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq1

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].rate_hy — MACRS rate, half-year convention
Status: **DISAGREE**

Project: 5.76%
Model: 20%
Work: 5-year HY, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].rate_mq — MACRS rate, mid-quarter convention
Status: **DISAGREE**

Project: 1.38%
Model: 35%
Work: 5-year MQ Q1, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 4.26%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line19_hy — Line 18 times the half-year rate
Status: **DISAGREE**

Project: $3,200.63
Model: $11,113.30
Work: 55,566.50 x 20%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line19_mq — Line 18 times the mid-quarter rate
Status: **DISAGREE**

Project: $766.82
Model: $19,448.28
Work: 55,566.50 x 35%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **AGREE**

Value: $2,367.13

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $2,367.13

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $2,367.13

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **DISAGREE**

Project: $766.82
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $2,367.13

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $61,525.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 25%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $15,381.25

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $15,381.25

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 30%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $18,457.50

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].l2 — Year 2 limit
Status: **AGREE**

Value: $16,100.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].d2 — Year 2 deduction allowable at 100% business use
Status: **AGREE**

Value: $16,100.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 18%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $11,074.50

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].l3 — Year 3 limit
Status: **AGREE**

Value: $9,700.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].d3 — Year 3 deduction allowable at 100% business use
Status: **AGREE**

Value: $9,700.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 11.37%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $6,995.39

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].l4 — Year 4 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].d4 — Year 4 deduction allowable at 100% business use
Status: **AGREE**

Value: $5,760.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 11.37%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $6,995.39

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].l5 — Year 5 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].d5 — Year 5 deduction allowable at 100% business use
Status: **AGREE**

Value: $5,760.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 4.26%

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $2,620.97

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].l6 — Year 6 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].d6 — Year 6 deduction allowable at 100% business use
Status: **AGREE**

Value: $2,620.97

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $2,367.13

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $2,367.13

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_v — Column (h)
Status: **AGREE**

Value: $2,367.13

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $2,367.13

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_o — Depreciation (owned, actual expenses)
Status: **AGREE**

Value: $2,367.13

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total_a2 — mq_total of a 2025 vehicle
Status: **DISAGREE**

Project: $55,566.49
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.4 — person[taxpayer].sc[biz_a].scveh[car_2].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $55,566.49
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### case classm.scveh.5 — prompt sha256 f7ef2bf873b95ee30f121a5ff6106bf8eb0e769e18c275d60e0b7e188347d8d9; branches: scveh.owned:false, scveh.owned:true, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.line9#0, scveh.line9#1, scveh.is_actual_owned:false, scveh.is_actual_owned:true, scveh.is_actual_leased:false, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:true, scveh.suv:false, scveh.is2025:false, scveh.is2025:true, scveh.is2019:false, scveh.s179_bad:false, scveh.after_jan19:true, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:false, scveh.claims_bonus:true, scveh.lim_2025#0, scveh.lim_2025#1, scveh.line7#0, scveh.line7#1, scveh.line10#0, scveh.line10#1, scveh.line10_2025#0, scveh.s179_line10:left, scveh.line11:positive, scveh.line14#0, scveh.line14#1, scveh.line15:positive, scveh.bonus_fullcase#0, scveh.bonus_2025#1, scveh.bonus_2025#2, scveh.line16#0, scveh.line16#1, scveh.bonus_allowed:left, scveh.bonus_allowed:right, scveh.line17:floor, scveh.line17:positive, scveh.line18:positive, scveh.line19#0, scveh.line19#1, scveh.line19_earlier#0, scveh.line19_2025#0, scveh.line20:left, scveh.line20:right, scveh.b100:positive, scveh.d1:right, scveh.d2:right, scveh.d3:right, scveh.d4:right, scveh.d5:right, scveh.d6:right, scveh.too_old:false, scveh.bonus_v#0, scveh.macrs_pass#0, scveh.macrs_heavy#0, scveh.macrs_v#0, scveh.bonus#0, scveh.bonus#1, scveh.macrs#0, scveh.macrs#1, scveh.s179_2025#0, scveh.s179_2025#1, scveh.mq_q4#0, scveh.mq_q4#1, scveh.mq_total#0, scveh.mq_total#1, scveh.cost179#0, scveh.cost179#1, scveh.q4_basis#0, scveh.q4_basis#2, scveh.mq_q4_o#0, scveh.mq_q4_o#1, scveh.mq_total_o#0, scveh.mq_total_o#1, scveh.cost179_o#0, scveh.cost179_o#1

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $216.32
Model: $21,632.00
Work: Business miles 21,632

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].cm_c — Commuting miles, as cents
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $18.03
Model: $1,803.00
Work: Other miles 1,803

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $18.03
Model: $1,803.00
Work: 0 + 1,803

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $234.35
Model: $23,435.00
Work: 21,632 + 1,803

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $15,142.40

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $15,142.40

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $1,853.51

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $1,853.51

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $1,853.51

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: yes

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $6,701.44

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 1

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: yes

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $58,785.33
Model: $58,785.32
Work: 63,685 x 21,632/23,435

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: yes

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].lim_first_bonus — First-year limit with the special allowance
Status: **AGREE**

Value: $20,200.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].lim_first_none — First-year limit without the special allowance
Status: **AGREE**

Value: $12,200.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].lim_2025 — Limit for a 2025 vehicle
Status: **AGREE**

Value: $20,200.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **DISAGREE**

Project: $20,200.00
Model: $0.00
Work: Not a prior-year vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $20,200.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $18,645.89

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $18,645.89

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $58,785.33
Model: $58,785.32
Work: 58,785.32 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_full — 100% special allowance
Status: **DISAGREE**

Project: $58,785.33
Model: $58,785.32
Work: 100% x 58,785.32

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $23,514.13

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **DISAGREE**

Project: $58,785.33
Model: $58,785.32
Work: Acquired after January 19, 2025, so 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $23,514.13

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $23,514.13

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $18,645.89

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $35,271.20
Model: $35,271.19
Work: 58,785.32 - 23,514.13

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq3

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].rate_hy — MACRS rate, half-year convention
Status: **AGREE**

Value: 20%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].rate_mq — MACRS rate, mid-quarter convention
Status: **AGREE**

Value: 15%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **DISAGREE**

Project: 15%
Model: 20%
Work: Year 1, HY applies (mid-quarter test is no)

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line19_hy — Line 18 times the half-year rate
Status: **AGREE**

Value: $7,054.24

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line19_mq — Line 18 times the mid-quarter rate
Status: **AGREE**

Value: $5,290.68

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **DISAGREE**

Project: $5,290.68
Model: $7,054.24
Work: 35,271.19 x 20%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $7,054.24

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **DISAGREE**

Project: $5,290.68
Model: $7,054.24
Work: line19_prior; not a 2019 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **AGREE**

Value: $7,054.24

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $63,685.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].r1 — MACRS rate for year 1
Status: **DISAGREE**

Project: 15%
Model: 20%
Work: 5-yr HY, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].t1 — Year 1 MACRS amount as if used 100% for business
Status: **DISAGREE**

Project: $9,552.75
Model: $12,737.00
Work: 63,685 x 20%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].l1 — Year 1 limit (no special allowance)
Status: **AGREE**

Value: $12,200.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **DISAGREE**

Project: $9,552.75
Model: $12,737.00
Work: 0 + 12,737

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].d1 — Year 1 deduction allowable at 100% business use (the lesser of the limit or the 
Status: **DISAGREE**

Project: $9,552.75
Model: $12,200.00
Work: Lesser of 12,200 or 12,737

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].r2 — MACRS rate for year 2
Status: **DISAGREE**

Project: 34%
Model: 32%
Work: 5-yr HY, year 2

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].t2 — Year 2 MACRS amount as if used 100% for business
Status: **DISAGREE**

Project: $21,652.90
Model: $20,379.20
Work: 63,685 x 32%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].r3 — MACRS rate for year 3
Status: **DISAGREE**

Project: 20.4%
Model: 19.2%
Work: 5-yr HY, year 3

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].t3 — Year 3 MACRS amount as if used 100% for business
Status: **DISAGREE**

Project: $12,991.74
Model: $12,227.52
Work: 63,685 x 19.2%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].r4 — MACRS rate for year 4
Status: **DISAGREE**

Project: 12.24%
Model: 11.52%
Work: 5-yr HY, year 4

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].t4 — Year 4 MACRS amount as if used 100% for business
Status: **DISAGREE**

Project: $7,795.04
Model: $7,336.51
Work: 63,685 x 11.52%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].r5 — MACRS rate for year 5
Status: **DISAGREE**

Project: 11.3%
Model: 11.52%
Work: 5-yr HY, year 5

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].t5 — Year 5 MACRS amount as if used 100% for business
Status: **DISAGREE**

Project: $7,196.41
Model: $7,336.51
Work: 63,685 x 11.52%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].r6 — MACRS rate for year 6
Status: **DISAGREE**

Project: 7.06%
Model: 5.76%
Work: 5-yr HY, year 6

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].t6 — Year 6 MACRS amount as if used 100% for business
Status: **DISAGREE**

Project: $4,496.16
Model: $3,668.26
Work: 63,685 x 5.76%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $18,645.89

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $7,054.24

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_v — Column (h)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $18,645.89

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **DISAGREE**

Project: $58,785.33
Model: $58,785.32
Work: Business basis less section 179 of 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **DISAGREE**

Project: $58,785.33
Model: $58,785.32
Work: Business-use cost

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $18,645.89

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].macrs_o — Depreciation (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **DISAGREE**

Project: $0.00
Model: $58,785.32
Work: 58,785.32 - 0

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].mq_total_o — mq_total (owned, actual expenses)
Status: **DISAGREE**

Project: $58,785.33
Model: $58,785.32
Work: Owned, actual expenses

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].mq_total_a2 — mq_total of a 2025 vehicle
Status: **DISAGREE**

Project: $58,785.33
Model: $58,785.32
Work: 2025 vehicle

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].cost179_o — cost179 (owned, actual expenses)
Status: **DISAGREE**

Project: $58,785.33
Model: $58,785.32
Work: Owned, actual expenses

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_1].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $58,785.33
Model: $58,785.32
Work: 2025 vehicle

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $159.02
Model: $15,902.00
Work: Business miles 15,902

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].cm_c — Commuting miles, as cents
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $0.12
Model: $12.00
Work: Other miles 12

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $0.12
Model: $12.00
Work: 0 + 12

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $159.14
Model: $15,914.00
Work: 15,902 + 12

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $11,131.40

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $11,131.40

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $1,017.23

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $1,017.23

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $11,131.40

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $3,068.68

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].year — Year of recovery in 2025
Status: **AGREE**

Value: 6

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $32,395.56
Model: $32,395.55
Work: 32,420 x 15,902/15,914

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].lim_first_bonus — First-year limit with the special allowance
Status: **DISAGREE**

Project: $5,760.00
Model: $20,200.00
Work: 2025 table, first year

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $5,760.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $5,760.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $5,755.66

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $5,755.66

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $32,395.56
Model: $32,395.55
Work: 32,395.55 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_full — 100% special allowance
Status: **DISAGREE**

Project: $32,395.56
Model: $32,395.55
Work: 100% x 32,395.55

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $12,958.22

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **DISAGREE**

Project: $32,395.56
Model: $32,395.55
Work: Acquired after January 19, 2025, so 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $5,755.66

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $32,395.56
Model: $32,395.55
Work: 32,395.55 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq1

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].rate_hy — MACRS rate, half-year convention
Status: **DISAGREE**

Project: 5.76%
Model: 20%
Work: 5-yr HY, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].rate_mq — MACRS rate, mid-quarter convention
Status: **DISAGREE**

Project: 1.38%
Model: 35%
Work: 5-yr MQ Q1, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 4.26%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line19_hy — Line 18 times the half-year rate
Status: **DISAGREE**

Project: $1,865.98
Model: $6,479.11
Work: 32,395.55 x 20%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line19_mq — Line 18 times the mid-quarter rate
Status: **DISAGREE**

Project: $447.06
Model: $11,338.44
Work: 32,395.55 x 35%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **AGREE**

Value: $1,380.05

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $1,380.05

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $1,380.05

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **DISAGREE**

Project: $1,865.98
Model: $6,479.11
Work: Half-year convention, because the mid-quarter test is no

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $1,380.05

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $32,420.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 25%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $8,105.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $8,105.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 30%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $9,726.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].l2 — Year 2 limit
Status: **AGREE**

Value: $16,100.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].d2 — Year 2 deduction allowable at 100% business use
Status: **AGREE**

Value: $9,726.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 18%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $5,835.60

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].l3 — Year 3 limit
Status: **AGREE**

Value: $9,700.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].d3 — Year 3 deduction allowable at 100% business use
Status: **AGREE**

Value: $5,835.60

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 11.37%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $3,686.15

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].l4 — Year 4 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].d4 — Year 4 deduction allowable at 100% business use
Status: **AGREE**

Value: $3,686.15

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 11.37%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $3,686.15

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].l5 — Year 5 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].d5 — Year 5 deduction allowable at 100% business use
Status: **AGREE**

Value: $3,686.15

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 4.26%

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $1,381.09

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].l6 — Year 6 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].d6 — Year 6 deduction allowable at 100% business use
Status: **AGREE**

Value: $1,381.09

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $1,380.05

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $1,380.05

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_v — Column (h)
Status: **AGREE**

Value: $1,380.05

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].macrs_o — Depreciation (owned, actual expenses)
Status: **DISAGREE**

Project: $1,380.05
Model: $0.00
Work: Not owned with actual expenses

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **DISAGREE**

Project: $0.00
Model: $32,395.55
Work: 32,395.55 - 0

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].mq_total_a2 — mq_total of a 2025 vehicle
Status: **DISAGREE**

Project: $32,395.56
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.5 — person[taxpayer].sc[biz_b].scveh[car_2].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $32,395.56
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### case classm.scveh.6 — prompt sha256 7b51ac38b87881fd1d64090868e2cc3a528f54ce25eb19eb2dfe027545a4b59a; branches: scveh.owned:false, scveh.owned:true, scveh.over_half:true, scveh.smr_ok:true, scveh.smr_bad:false, scveh.line9#0, scveh.is_actual_owned:false, scveh.is_actual_leased:false, scveh.line20a#1, scveh.low_use:false, scveh.screen:false, scveh.screened:false, scveh.passenger:true, scveh.suv:false, scveh.is2025:false, scveh.is2019:false, scveh.is2019:true, scveh.s179_bad:false, scveh.after_jan19:false, scveh.after_jan19:true, scveh.bonus_same:true, scveh.bonus_mixed:false, scveh.claims_bonus:false, scveh.lim_2025#1, scveh.line7#1, scveh.line10#1, scveh.line10_2025#0, scveh.s179_line10:left, scveh.line11:positive, scveh.line14#1, scveh.line15:positive, scveh.bonus_fullcase#0, scveh.bonus_fullcase#1, scveh.bonus_2025#2, scveh.line16#1, scveh.bonus_allowed:left, scveh.line17:positive, scveh.line18:positive, scveh.line19#1, scveh.line19_earlier#0, scveh.line19_earlier#1, scveh.line19_2025#1, scveh.line20:right, scveh.b100:positive, scveh.d1:right, scveh.d2:left, scveh.d2:right, scveh.d3:left, scveh.d4:left, scveh.d5:left, scveh.d6:left, scveh.unrecovered:positive, scveh.post_amount:left, scveh.too_old:false, scveh.bonus_v#0, scveh.macrs_pass#0, scveh.macrs_pass#1, scveh.macrs_heavy#0, scveh.macrs_heavy#1, scveh.macrs_v#0, scveh.bonus#1, scveh.macrs#1, scveh.s179_2025#1, scveh.mq_q4#1, scveh.mq_total#1, scveh.cost179#1, scveh.q4_basis#1, scveh.q4_basis#2, scveh.mq_q4_o#1, scveh.mq_total_o#1, scveh.cost179_o#1

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $197.88
Model: $19,788.00
Work: Business miles given: 19,788

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].cm_c — Commuting miles, as cents
Status: **DISAGREE**

Project: $18.42
Model: $1,842.00
Work: Commuting miles given: 1,842

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $22.48
Model: $2,248.00
Work: Other miles given: 2,248

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $40.90
Model: $4,090.00
Work: 1,842 + 2,248

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $238.78
Model: $23,878.00
Work: 19,788 + 4,090

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $13,851.60

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $13,884.60

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $2,902.98

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $2,935.98

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $13,884.60

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $1,775.93

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].year — Year of recovery in 2025
Status: **AGREE**

Value: 2

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $28,954.40
Model: $28,954.39
Work: 34,939 x 19,788 / 23,878

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus — First-year limit with the special allowance
Status: **DISAGREE**

Project: $19,800.00
Model: $20,200.00
Work: Pub 946 table, 2025, 1st year: $20,200

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $19,800.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $19,800.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **DISAGREE**

Project: $16,408.52
Model: $16,408.51
Work: 19,800 x 19,788 / 23,878

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line11 — Subtract line 10 from line 9
Status: **DISAGREE**

Project: $16,408.52
Model: $16,408.51
Work: 16,408.51 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $28,954.40
Model: $28,954.39
Work: 28,954.39 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_full — 100% special allowance
Status: **DISAGREE**

Project: $28,954.40
Model: $28,954.39
Work: 28,954.39 x 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty — 40% special allowance
Status: **AGREE**

Value: $11,581.76

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **DISAGREE**

Project: $28,954.40
Model: $28,954.39
Work: Acquired after January 19, 2025, so 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **DISAGREE**

Project: $16,408.52
Model: $16,408.51
Work: 16,408.51 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $28,954.40
Model: $28,954.39
Work: 28,954.39 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq3

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].rate_hy — MACRS rate, half-year convention
Status: **DISAGREE**

Project: 32%
Model: 20%
Work: 5-year 200DB half-year convention, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].rate_mq — MACRS rate, mid-quarter convention
Status: **DISAGREE**

Project: 34%
Model: 15%
Work: 5-year 200DB mid-quarter, 3rd quarter, year 1

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].rate_prior — MACRS rate for the 2025 year of recovery
Status: **AGREE**

Value: 26%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line19_hy — Line 18 times the half-year rate
Status: **DISAGREE**

Project: $9,265.41
Model: $5,790.88
Work: 28,954.39 x 20%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line19_mq — Line 18 times the mid-quarter rate
Status: **DISAGREE**

Project: $9,844.50
Model: $4,343.16
Work: 28,954.39 x 15%

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line19_prior — Line 18 times the rate for the 2025 year of recovery
Status: **AGREE**

Value: $7,528.14

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $7,528.14

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $7,528.14

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line19_2025 — Line 19 for a 2025 vehicle, half-year or mid-quarter
Status: **DISAGREE**

Project: $9,844.50
Model: $4,343.16
Work: Mid-quarter convention applies (given test is yes)

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $7,528.14

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $34,939.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 35%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $12,228.65

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $12,228.65

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 26%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $9,084.14

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].l2 — Year 2 limit
Status: **AGREE**

Value: $19,800.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].d2 — Year 2 deduction allowable at 100% business use
Status: **AGREE**

Value: $9,084.14

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 15.6%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $5,450.48

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 11.01%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $3,846.78

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 11.01%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $3,846.78

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 1.38%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $482.16

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $7,528.14

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $7,528.14

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_v — Column (h)
Status: **AGREE**

Value: $7,528.14

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].macrs_o — Depreciation (owned, actual expenses)
Status: **DISAGREE**

Project: $7,528.14
Model: $0.00
Work: Not owned on actual expenses

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2 — mq_total of a 2025 vehicle
Status: **DISAGREE**

Project: $28,954.40
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $28,954.40
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bm_c — Business miles, as cents
Status: **DISAGREE**

Project: $234.84
Model: $23,484.00
Work: Business miles given: 23,484

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].cm_c — Commuting miles, as cents
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].om_c — Other miles, as cents
Status: **DISAGREE**

Project: $18.94
Model: $1,894.00
Work: Other miles given: 1,894

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].nonbusiness_c — Commuting and other miles, as cents
Status: **DISAGREE**

Project: $18.94
Model: $1,894.00
Work: 0 + 1,894

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].total_c — Total miles, as cents
Status: **DISAGREE**

Project: $253.78
Model: $25,378.00
Work: 23,484 + 1,894

Ruling: representation; project retained. A mile count is carried as one cent per mile (multiply_count by one cent) so that miles can be added and divided like amounts in the business-use ratio; the model read the cents as dollars. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].over_half — Business use is more than 50%
Status: **AGREE**

Value: yes

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].smr_bad — The standard mileage rate is not available for this vehicle
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].smr_amount — Business miles times the standard mileage rate
Status: **AGREE**

Value: $16,438.80

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line9_standard — Standard mileage amount plus parking fees and tolls
Status: **AGREE**

Value: $17,307.80

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].operating_business — The business portion of the operating expenses
Status: **AGREE**

Value: $8,938.13

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line9_actual — Business portion of the operating expenses plus parking fees and tolls
Status: **AGREE**

Value: $9,807.13

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line9 — Car and truck expenses for this vehicle
Status: **AGREE**

Value: $17,307.80

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].is_actual_owned — Owned and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].is_actual_leased — Leased and on actual expenses
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].lease_business — The business portion of the lease payments
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line20a — Rent or lease of this vehicle (business portion)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].low_use — Business use is 50% or less
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].screened — This vehicle's depreciation is outside this tool
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].year — Year of recovery in 2025
Status: **AGREE**

Value: 7

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].is2025 — Placed in service in 2025
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].is2019 — Placed in service in 2019 (2025 is after the recovery period)
Status: **AGREE**

Value: yes

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bus_cost — Business/investment cost (cost times business use)
Status: **DISAGREE**

Project: $70,413.10
Model: $70,413.13
Work: 76,092 x 23,484 / 25,378

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].s179_bad — The section 179 election is more than the business cost, or than the SUV limit
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_mixed — The special allowance choice differs within the 5-year class
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].claims_bonus — A special allowance is claimed
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].lim_first_bonus — First-year limit with the special allowance
Status: **DISAGREE**

Project: $5,760.00
Model: $18,100.00
Work: Pub 946 table, 2019, 1st year: $18,100

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].lim_first_none — First-year limit without the special allowance
Status: **AGREE**

Value: $10,100.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].lim_2025 — Limit for a 2025 vehicle
Status: **DISAGREE**

Project: $10,100.00
Model: $12,200.00
Work: 2025 with no special allowance: $12,200

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].lim_prior — Limit for the vehicle's 2025 year of recovery
Status: **AGREE**

Value: $5,760.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line7 — Maximum depreciation deduction for this year from the appropriate table
Status: **AGREE**

Value: $5,760.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line9w — Adjusted maximum depreciation deduction (line 7 times the business/investment-us
Status: **AGREE**

Value: $5,330.12

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_ok — Section 179 elected for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line10 — Section 179 deduction claimed this year (not more than line 9 for a passenger au
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line10_2025 — Section 179 for a 2025 vehicle: not more than line 9 for a passenger automobile
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].s179_line10 — The section 179 election, not more than line 9
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line11 — Subtract line 10 from line 9
Status: **AGREE**

Value: $5,330.12

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line14 — Section 179 deduction claimed in the year you placed the car in service
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line15 — Tentative basis for depreciation (line 13 less line 14)
Status: **DISAGREE**

Project: $70,413.10
Model: $70,413.13
Work: 70,413.13 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_full — 100% special allowance
Status: **DISAGREE**

Project: $70,413.10
Model: $70,413.13
Work: 70,413.13 x 100%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_forty — 40% special allowance
Status: **DISAGREE**

Project: $28,165.24
Model: $28,165.25
Work: 70,413.13 x 40%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_fullcase — The allowance when it is claimed: 100% if acquired after January 19, 2025, other
Status: **DISAGREE**

Project: $28,165.24
Model: $28,165.25
Work: Not acquired after January 19, 2025, so 40%

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_2025 — Special allowance for a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line16 — Special depreciation allowance
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_allowed — Special depreciation allowance allowed (not more than line 11)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line17 — Limit on the MACRS depreciation (line 11 less line 16)
Status: **AGREE**

Value: $5,330.12

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line18 — Basis for depreciation (line 15 less line 16)
Status: **DISAGREE**

Project: $70,413.10
Model: $70,413.13
Work: 70,413.13 - 0

Ruling: owner's ruling; project retained. The business-use percentage is business miles over total miles rounded half-up to six places (owner ruling 3c, amb.2025 register); the model multiplied by the exact fraction, a difference of a few cents. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].qconv — Mid-quarter convention for that quarter
Status: **AGREE**

Value: mq2

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line19 — Tentative MACRS depreciation deduction (line 18 times line 6)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line19_earlier — Line 19 for a vehicle placed in service before 2025 (zero after the recovery per
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].line20 — MACRS depreciation deduction (the lesser of line 17 or line 19)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].b100 — Cost less the section 179 deduction (as if used 100% for business)
Status: **AGREE**

Value: $76,092.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].r1 — MACRS rate for year 1
Status: **AGREE**

Value: 5%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].t1 — Year 1 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $3,804.60

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].l1 — Year 1 limit (no special allowance)
Status: **AGREE**

Value: $10,100.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].t1s — Year 1 section 179 deduction plus MACRS amount
Status: **AGREE**

Value: $3,804.60

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].d1 — Year 1 deduction allowable at 100% business use (the lesser of the limit or the 
Status: **AGREE**

Value: $3,804.60

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].r2 — MACRS rate for year 2
Status: **AGREE**

Value: 38%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].t2 — Year 2 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $28,914.96

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].l2 — Year 2 limit
Status: **AGREE**

Value: $16,100.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].d2 — Year 2 deduction allowable at 100% business use
Status: **AGREE**

Value: $16,100.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].r3 — MACRS rate for year 3
Status: **AGREE**

Value: 22.8%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].t3 — Year 3 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $17,348.98

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].l3 — Year 3 limit
Status: **AGREE**

Value: $9,700.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].d3 — Year 3 deduction allowable at 100% business use
Status: **AGREE**

Value: $9,700.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].r4 — MACRS rate for year 4
Status: **AGREE**

Value: 13.68%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].t4 — Year 4 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $10,409.39

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].l4 — Year 4 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].d4 — Year 4 deduction allowable at 100% business use
Status: **AGREE**

Value: $5,760.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].r5 — MACRS rate for year 5
Status: **AGREE**

Value: 10.94%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].t5 — Year 5 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $8,324.46

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].l5 — Year 5 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].d5 — Year 5 deduction allowable at 100% business use
Status: **AGREE**

Value: $5,760.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].r6 — MACRS rate for year 6
Status: **AGREE**

Value: 9.58%

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].t6 — Year 6 MACRS amount as if used 100% for business
Status: **AGREE**

Value: $7,289.61

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].l6 — Year 6 limit
Status: **AGREE**

Value: $5,760.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].d6 — Year 6 deduction allowable at 100% business use
Status: **AGREE**

Value: $5,760.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].d_total — Deductions allowable during the recovery period at 100% business use
Status: **AGREE**

Value: $46,884.60

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].unrecovered — Unrecovered basis at the end of the recovery period
Status: **AGREE**

Value: $29,207.40

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].post_amount — The lesser of the limit or the unrecovered basis
Status: **AGREE**

Value: $5,760.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].post — 2025 deduction after the recovery period (times the business use percentage)
Status: **AGREE**

Value: $5,330.12

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].too_old — Placed in service before 2019
Status: **AGREE**

Value: no

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_v — Special allowance for this vehicle (line 25)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_pass — Column (h) for a passenger automobile
Status: **AGREE**

Value: $5,330.12

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_heavy — Column (h) for a vehicle not subject to the limits
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_v — Column (h)
Status: **AGREE**

Value: $5,330.12

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bonus — Line 25: special allowance of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].macrs — Column (h): depreciation of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025 — Column (i): elected section 179 cost of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4 — Mid-quarter test basis, fourth quarter of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total — Mid-quarter test basis, 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].cost179 — Cost of section 179 property placed in service in 2025 of this vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].bonus_o — Special allowance (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].macrs_o — Depreciation (owned, actual expenses)
Status: **DISAGREE**

Project: $5,330.12
Model: $0.00
Work: Not owned on actual expenses

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_o — Section 179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].q4_basis — Basis for the mid-quarter test when placed in service October to December
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_o — mq_q4 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_a2 — mq_q4 of a 2025 vehicle
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total_o — mq_total (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].mq_total_a2 — mq_total of a 2025 vehicle
Status: **DISAGREE**

Project: $70,413.10
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].cost179_o — cost179 (owned, actual expenses)
Status: **AGREE**

Value: $0.00

### classm.scveh.6 — person[taxpayer].sc[biz_a].scveh[car_2].cost179_a2 — cost179 of a 2025 vehicle
Status: **DISAGREE**

Project: $70,413.10
Model: $0.00
Work: Not a 2025 vehicle

Ruling: helper of a branch this vehicle does not take; project retained. The project figures every line of every entry (the 2025 lines for an earlier vehicle, the 2019 recovery chain for a later one, the owned-vehicle lines for a leased one, the fourth-quarter basis for another quarter); no printed result reads it in this case, and the printed lines of the entry agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

## Raw responses

### classm.scveh.1

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bm_c"
    value: "29991.00"
    work: "29,991 business miles"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cm_c"
    value: "3237.00"
    work: "3,237 commuting miles"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].om_c"
    value: "7.00"
    work: "7 other miles"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].nonbusiness_c"
    value: "3244.00"
    work: "3,237 + 7"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].total_c"
    value: "33235.00"
    work: "29,991 + 3,244"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].over_half"
    value: "yes"
    work: "29,991 / 33,235 = 90.24%, more than 50%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].smr_bad"
    value: "no"
    work: "Filer answered that the standard mileage rate may be used"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].smr_amount"
    value: "20993.70"
    work: "29,991 x 0.70"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9_standard"
    value: "21993.70"
    work: "20,993.70 + 1,000.00"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].operating_business"
    value: "7531.36"
    work: "8,346 x 29,991 / 33,235"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9_actual"
    value: "8531.36"
    work: "7,531.36 + 1,000.00"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9"
    value: "8531.36"
    work: "Actual expenses method chosen"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is_actual_owned"
    value: "no"
    work: "Vehicle is leased"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is_actual_leased"
    value: "yes"
    work: "Leased vehicle on actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lease_business"
    value: "6508.95"
    work: "7,213 x 29,991 / 33,235"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line20a"
    value: "6508.95"
    work: "Leased on actual expenses: business portion of lease payments"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].low_use"
    value: "no"
    work: "Business use 90.24% is more than 50%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].screened"
    value: "no"
    work: "None of the screening conditions apply"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].year"
    value: "1"
    work: "Placed in service 2025, so 2025 is year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is2025"
    value: "yes"
    work: "Year placed in service is y2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is2019"
    value: "no"
    work: "Year placed in service is y2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bus_cost"
    value: "49166.83"
    work: "54,485 x 29,991 / 33,235"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_bad"
    value: "no"
    work: "Section 179 elected is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_mixed"
    value: "no"
    work: "Choice is the same for all 5-year property"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].claims_bonus"
    value: "yes"
    work: "Special allowance choice is full"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lim_first_bonus"
    value: "20200.00"
    work: "Pub 946 table, 2025, 1st year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lim_first_none"
    value: "12200.00"
    work: "Pub 946 footnote 1 (no special allowance)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lim_2025"
    value: "20200.00"
    work: "Special allowance claimed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lim_prior"
    value: "20200.00"
    work: "2025 row, year 1, with special allowance"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line7"
    value: "20200.00"
    work: "2025 vehicle limit"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9w"
    value: "18228.32"
    work: "20,200 x 29,991 / 33,235"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_ok"
    value: "0.00"
    work: "Elected section 179 is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line10"
    value: "0.00"
    work: "No section 179"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line10_2025"
    value: "0.00"
    work: "smaller of 0 or line 9"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_line10"
    value: "0.00"
    work: "smaller of 0 or 18,228.32"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line11"
    value: "18228.32"
    work: "18,228.32 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line14"
    value: "0.00"
    work: "Section 179 claimed in year placed in service is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line15"
    value: "49166.83"
    work: "49,166.83 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_full"
    value: "49166.83"
    work: "49,166.83 x 100%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_forty"
    value: "19666.73"
    work: "49,166.83 x 40%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_fullcase"
    value: "49166.83"
    work: "Acquired after Jan 19, 2025, so 100%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_2025"
    value: "49166.83"
    work: "Allowance claimed, full"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line16"
    value: "49166.83"
    work: "2025 vehicle with special allowance"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_allowed"
    value: "18228.32"
    work: "smaller of 49,166.83 or line 11 of 18,228.32"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line17"
    value: "0.00"
    work: "18,228.32 - 49,166.83 is less than zero, so 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line18"
    value: "0.00"
    work: "49,166.83 - 49,166.83"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].qconv"
    value: "mq2"
    work: "Placed in service in q2"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].rate_hy"
    value: "20.00%"
    work: "5-year 200DB HY, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].rate_mq"
    value: "15.00%"
    work: "5-year 200DB MQ, 2nd quarter, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].rate_prior"
    value: "20.00%"
    work: "HY convention, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_hy"
    value: "0.00"
    work: "0 x 20%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_mq"
    value: "0.00"
    work: "0 x 15%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_prior"
    value: "0.00"
    work: "0 x 20%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19"
    value: "0.00"
    work: "Line 18 is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_earlier"
    value: "0.00"
    work: "Not placed in service before 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_2025"
    value: "0.00"
    work: "HY convention: 0 x 20%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line20"
    value: "0.00"
    work: "lesser of 0 or 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].b100"
    value: "54485.00"
    work: "54,485 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r1"
    value: "20.00%"
    work: "5-year HY, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t1"
    value: "10897.00"
    work: "54,485 x 20%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].l1"
    value: "12200.00"
    work: "2025 limit, no special allowance"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t1s"
    value: "10897.00"
    work: "0 + 10,897.00"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].d1"
    value: "10897.00"
    work: "lesser of 12,200 or 10,897"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r2"
    value: "32.00%"
    work: "5-year HY, year 2"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t2"
    value: "17435.20"
    work: "54,485 x 32%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r3"
    value: "19.20%"
    work: "5-year HY, year 3"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t3"
    value: "10461.12"
    work: "54,485 x 19.20%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r4"
    value: "11.52%"
    work: "5-year HY, year 4"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t4"
    value: "6276.67"
    work: "54,485 x 11.52%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r5"
    value: "11.52%"
    work: "5-year HY, year 5"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t5"
    value: "6276.67"
    work: "54,485 x 11.52%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r6"
    value: "5.76%"
    work: "5-year HY, year 6"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t6"
    value: "3138.34"
    work: "54,485 x 5.76%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].too_old"
    value: "no"
    work: "Placed in service 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_v"
    value: "18228.32"
    work: "Special allowance allowed, 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_pass"
    value: "0.00"
    work: "Line 20"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_heavy"
    value: "0.00"
    work: "Basis is fully absorbed by the 100% allowance"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_v"
    value: "0.00"
    work: "Passenger automobile: macrs_pass"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus"
    value: "0.00"
    work: "Leased vehicle: no depreciation"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs"
    value: "0.00"
    work: "Leased vehicle: no depreciation"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_2025"
    value: "0.00"
    work: "Leased vehicle; no election"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_q4"
    value: "0.00"
    work: "Leased vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_total"
    value: "0.00"
    work: "Leased vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cost179"
    value: "0.00"
    work: "Leased vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].q4_basis"
    value: "0.00"
    work: "Placed in service in q2, not October to December"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_a2"
    value: "0.00"
    work: "q4_basis is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_total_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_total_a2"
    value: "49166.83"
    work: "Business cost less section 179 of 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cost179_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cost179_a2"
    value: "49166.83"
    work: "Business cost of a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bm_c"
    value: "29990.00"
    work: "29,990 business miles"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cm_c"
    value: "0.00"
    work: "0 commuting miles"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].om_c"
    value: "3989.00"
    work: "3,989 other miles"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].nonbusiness_c"
    value: "3989.00"
    work: "0 + 3,989"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].total_c"
    value: "33979.00"
    work: "29,990 + 3,989"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].over_half"
    value: "yes"
    work: "29,990 / 33,979 = 88.26%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].smr_bad"
    value: "no"
    work: "Filer answered that the standard mileage rate may be used"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].smr_amount"
    value: "20993.00"
    work: "29,990 x 0.70"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9_standard"
    value: "21491.00"
    work: "20,993.00 + 498.00"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].operating_business"
    value: "0.00"
    work: "0 x 88.26%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9_actual"
    value: "498.00"
    work: "0 + 498.00"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9"
    value: "498.00"
    work: "Actual expenses method chosen"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is_actual_owned"
    value: "yes"
    work: "Owned vehicle on actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is_actual_leased"
    value: "no"
    work: "Vehicle is owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].lease_business"
    value: "2837.57"
    work: "3,215 x 29,990 / 33,979"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line20a"
    value: "0.00"
    work: "Not leased"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].low_use"
    value: "no"
    work: "Business use 88.26% is more than 50%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].screened"
    value: "no"
    work: "None of the screening conditions apply"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].year"
    value: "7"
    work: "2019 is year 1, so 2025 is year 7"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is2025"
    value: "no"
    work: "Placed in service 2019"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is2019"
    value: "yes"
    work: "Year placed in service is y2019"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bus_cost"
    value: "4413.02"
    work: "5,000 x 29,990 / 33,979"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_bad"
    value: "no"
    work: "Section 179 elected is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_mixed"
    value: "no"
    work: "Choice is the same within the class"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].claims_bonus"
    value: "no"
    work: "Special allowance choice is none"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].lim_first_bonus"
    value: "20200.00"
    work: "2025 table, 1st year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].lim_first_none"
    value: "12200.00"
    work: "Footnote 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].lim_2025"
    value: "12200.00"
    work: "No special allowance claimed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].lim_prior"
    value: "5760.00"
    work: "2019 row, 4th and later years"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line7"
    value: "5760.00"
    work: "Limit for a prior-year vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9w"
    value: "5083.80"
    work: "5,760 x 29,990 / 33,979"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_ok"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line10"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line10_2025"
    value: "0.00"
    work: "Section 179 is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_line10"
    value: "0.00"
    work: "Section 179 is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line11"
    value: "5083.80"
    work: "5,083.80 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line14"
    value: "0.00"
    work: "Section 179 claimed in year placed in service is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line15"
    value: "4413.02"
    work: "4,413.02 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_full"
    value: "4413.02"
    work: "4,413.02 x 100%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_forty"
    value: "1765.21"
    work: "4,413.02 x 40%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_fullcase"
    value: "4413.02"
    work: "Acquired after Jan 19, 2025, so 100%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_2025"
    value: "0.00"
    work: "No allowance claimed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line16"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_allowed"
    value: "0.00"
    work: "smaller of 0 or line 11"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line17"
    value: "5083.80"
    work: "5,083.80 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line18"
    value: "4413.02"
    work: "4,413.02 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].qconv"
    value: "mq3"
    work: "Quarter given is q3"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19"
    value: "0.00"
    work: "Year 7 is past the 5-year table"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_earlier"
    value: "0.00"
    work: "After the recovery period"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line20"
    value: "0.00"
    work: "lesser of 5,083.80 or 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].b100"
    value: "5000.00"
    work: "5,000 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r1"
    value: "35.00%"
    work: "5-year MQ, 1st quarter, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t1"
    value: "1750.00"
    work: "5,000 x 35%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].l1"
    value: "10100.00"
    work: "2019 limit, no special allowance (footnote 6)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t1s"
    value: "1750.00"
    work: "0 + 1,750"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].d1"
    value: "1750.00"
    work: "lesser of 10,100 or 1,750"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r2"
    value: "26.00%"
    work: "5-year MQ Q1, year 2"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t2"
    value: "1300.00"
    work: "5,000 x 26%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].l2"
    value: "16100.00"
    work: "2019 row, 2nd year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].d2"
    value: "1300.00"
    work: "lesser of 16,100 or 1,300"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r3"
    value: "15.60%"
    work: "5-year MQ Q1, year 3"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t3"
    value: "780.00"
    work: "5,000 x 15.60%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].l3"
    value: "9700.00"
    work: "2019 row, 3rd year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].d3"
    value: "780.00"
    work: "lesser of 9,700 or 780"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r4"
    value: "11.01%"
    work: "5-year MQ Q1, year 4"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t4"
    value: "550.50"
    work: "5,000 x 11.01%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].l4"
    value: "5760.00"
    work: "2019 row, 4th and later years"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].d4"
    value: "550.50"
    work: "lesser of 5,760 or 550.50"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r5"
    value: "11.01%"
    work: "5-year MQ Q1, year 5"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t5"
    value: "550.50"
    work: "5,000 x 11.01%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].l5"
    value: "5760.00"
    work: "2019 row, 4th and later years"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].d5"
    value: "550.50"
    work: "lesser of 5,760 or 550.50"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r6"
    value: "1.38%"
    work: "5-year MQ Q1, year 6"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t6"
    value: "69.00"
    work: "5,000 x 1.38%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].l6"
    value: "5760.00"
    work: "2019 row, 4th and later years"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].d6"
    value: "69.00"
    work: "lesser of 5,760 or 69"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].d_total"
    value: "5000.00"
    work: "1,750 + 1,300 + 780 + 550.50 + 550.50 + 69"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].unrecovered"
    value: "0.00"
    work: "5,000 - 5,000"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].post_amount"
    value: "0.00"
    work: "lesser of 5,760 or 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].post"
    value: "0.00"
    work: "0 x 88.26%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].too_old"
    value: "no"
    work: "Placed in service 2019"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_v"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_pass"
    value: "0.00"
    work: "Post-recovery amount is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_heavy"
    value: "0.00"
    work: "No depreciation after the recovery period for non-passenger listed property"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_v"
    value: "0.00"
    work: "Not subject to the limits: macrs_heavy"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus"
    value: "0.00"
    work: "bonus_v"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs"
    value: "0.00"
    work: "macrs_v"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_2025"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_q4"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_total"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cost179"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_o"
    value: "0.00"
    work: "Owned actual: bonus_v of 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_o"
    value: "0.00"
    work: "Owned actual: macrs_v of 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_o"
    value: "0.00"
    work: "No section 179"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].q4_basis"
    value: "0.00"
    work: "q3, not October to December"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_o"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_total_o"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_total_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cost179_o"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cost179_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
```
```

### classm.scveh.2

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bm_c"
    value: "24289.00"
    work: "Business miles 24,289"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cm_c"
    value: "0.00"
    work: "Commuting miles 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].om_c"
    value: "3962.00"
    work: "Other miles 3,962"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c"
    value: "3962.00"
    work: "0 + 3,962"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].total_c"
    value: "28251.00"
    work: "24,289 + 3,962"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].over_half"
    value: "yes"
    work: "24,289/28,251 = 85.98% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_bad"
    value: "no"
    work: "Filer answered that the standard mileage rate may be used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_amount"
    value: "17002.30"
    work: "24,289 x 0.70"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_standard"
    value: "17002.30"
    work: "17,002.30 + 0 parking/tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].operating_business"
    value: "4585.09"
    work: "5,333 x 24,289/28,251"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_actual"
    value: "4585.09"
    work: "4,585.09 + 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9"
    value: "4585.09"
    work: "Actual expenses chosen"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned"
    value: "yes"
    work: "Owned and actual"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased"
    value: "no"
    work: "Not leased"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lease_business"
    value: "0.00"
    work: "Lease payments 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "0.00"
    work: "Not leased"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].low_use"
    value: "no"
    work: "85.98% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].screened"
    value: "no"
    work: "None of the screening conditions apply; use > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].year"
    value: "4"
    work: "Placed in service 2022; 2025 is year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2025"
    value: "no"
    work: "Placed in service 2022"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2019"
    value: "no"
    work: "Placed in service 2022"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bus_cost"
    value: "23668.26"
    work: "27,529 x 24,289/28,251"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_bad"
    value: "no"
    work: "Section 179 election 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed"
    value: "no"
    work: "Choice is the same for all 5-year property"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus"
    value: "no"
    work: "Special allowance = none"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus"
    value: "20200.00"
    work: "2025 first-year limit with special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_prior"
    value: "6460.00"
    work: "2022 vehicle, 4th & later year"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line7"
    value: "6460.00"
    work: "Table limit for year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9w"
    value: "5554.03"
    work: "6,460 x 24,289/28,251"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok"
    value: "0.00"
    work: "Not a 2025 vehicle; election 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10_2025"
    value: "0.00"
    work: "Election 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_line10"
    value: "0.00"
    work: "min(0, line 9)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line11"
    value: "5554.03"
    work: "5,554.03 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line14"
    value: "0.00"
    work: "Section 179 in the year placed in service = 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line15"
    value: "23668.26"
    work: "23,668.26 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_full"
    value: "23668.26"
    work: "Line 15 x 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty"
    value: "9467.30"
    work: "Line 15 x 40%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase"
    value: "23668.26"
    work: "Acquired after 1/19/2025, so 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025"
    value: "0.00"
    work: "Not claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line16"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "min(0, line 11)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line17"
    value: "5554.03"
    work: "5,554.03 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line18"
    value: "23668.26"
    work: "23,668.26 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].qconv"
    value: "mq4"
    work: "Quarter q4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_hy"
    value: "20.00%"
    work: "5-year 200DB half-year, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_mq"
    value: "5.00%"
    work: "5-year mid-quarter Q4, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_prior"
    value: "11.52%"
    work: "Half-year convention, year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_hy"
    value: "4733.65"
    work: "23,668.26 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_mq"
    value: "1183.41"
    work: "23,668.26 x 5%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_prior"
    value: "2726.58"
    work: "23,668.26 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19"
    value: "2726.58"
    work: "Prior-year vehicle rate applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier"
    value: "2726.58"
    work: "Within the recovery period"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_2025"
    value: "1183.41"
    work: "Mid-quarter test is yes, so the MQ amount is used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20"
    value: "2726.58"
    work: "min(5,554.03, 2,726.58)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].b100"
    value: "27529.00"
    work: "27,529 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r1"
    value: "20.00%"
    work: "HY year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1"
    value: "5505.80"
    work: "27,529 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1s"
    value: "5505.80"
    work: "0 + 5,505.80"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r2"
    value: "32.00%"
    work: "HY year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t2"
    value: "8809.28"
    work: "27,529 x 32%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l2"
    value: "18000.00"
    work: "2022 vehicle, 2nd year"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d2"
    value: "8809.28"
    work: "min(18,000, 8,809.28)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r3"
    value: "19.20%"
    work: "HY year 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t3"
    value: "5285.57"
    work: "27,529 x 19.2%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l3"
    value: "10800.00"
    work: "2022 vehicle, 3rd year"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d3"
    value: "5285.57"
    work: "min(10,800, 5,285.57)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r4"
    value: "11.52%"
    work: "HY year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t4"
    value: "3171.34"
    work: "27,529 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l4"
    value: "6460.00"
    work: "2022 vehicle, 4th year"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d4"
    value: "3171.34"
    work: "min(6,460, 3,171.34)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r5"
    value: "11.52%"
    work: "HY year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t5"
    value: "3171.34"
    work: "27,529 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r6"
    value: "5.76%"
    work: "HY year 6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t6"
    value: "1585.67"
    work: "27,529 x 5.76%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].too_old"
    value: "no"
    work: "Placed in service 2022"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_v"
    value: "0.00"
    work: "No special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass"
    value: "2726.58"
    work: "Line 20"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy"
    value: "2726.58"
    work: "Line 19 without the limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_v"
    value: "2726.58"
    work: "Subject to the passenger auto limits"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus"
    value: "0.00"
    work: "bonus_o"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs"
    value: "2726.58"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_o"
    value: "0.00"
    work: "No special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_o"
    value: "2726.58"
    work: "macrs_v; owned, actual"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].q4_basis"
    value: "23668.26"
    work: "Q4; business cost less 0 section 179"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_o"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bm_c"
    value: "9083.00"
    work: "Business miles 9,083"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cm_c"
    value: "0.00"
    work: "Commuting miles 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].om_c"
    value: "3840.00"
    work: "Other miles 3,840"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].nonbusiness_c"
    value: "3840.00"
    work: "0 + 3,840"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].total_c"
    value: "12923.00"
    work: "9,083 + 3,840"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].over_half"
    value: "yes"
    work: "9,083/12,923 = 70.29%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].smr_bad"
    value: "no"
    work: "Filer answered that the standard mileage rate may be used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].smr_amount"
    value: "6358.10"
    work: "9,083 x 0.70"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9_standard"
    value: "6358.10"
    work: "6,358.10 + 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].operating_business"
    value: "1797.90"
    work: "2,558 x 9,083/12,923"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9_actual"
    value: "1797.90"
    work: "1,797.90 + 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9"
    value: "6358.10"
    work: "Standard mileage rate chosen"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is_actual_owned"
    value: "no"
    work: "Standard mileage rate"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is_actual_leased"
    value: "no"
    work: "Owned; standard mileage rate"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lease_business"
    value: "616.40"
    work: "877 x 9,083/12,923"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20a"
    value: "0.00"
    work: "Standard rate: no lease deduction"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].low_use"
    value: "no"
    work: "70.29% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].screened"
    value: "no"
    work: "No screening condition applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].year"
    value: "7"
    work: "Placed in service 2019; 2025 is year 7"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is2025"
    value: "no"
    work: "Placed in service 2019"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is2019"
    value: "yes"
    work: "Placed in service 2019"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bus_cost"
    value: "43844.12"
    work: "62,380 x 9,083/12,923"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_bad"
    value: "no"
    work: "Election 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_mixed"
    value: "no"
    work: "Same choice for all 5-year property"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].claims_bonus"
    value: "no"
    work: "Special allowance = none"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_first_bonus"
    value: "20200.00"
    work: "2025 table, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_first_none"
    value: "12200.00"
    work: "2025 table footnote 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_2025"
    value: "12200.00"
    work: "No special allowance claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_prior"
    value: "5760.00"
    work: "2019 vehicle, 4th & later year"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line7"
    value: "5760.00"
    work: "Year 7 uses the 4th & later limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9w"
    value: "4048.45"
    work: "5,760 x 9,083/12,923"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_ok"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line10"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line10_2025"
    value: "0.00"
    work: "Election 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_line10"
    value: "0.00"
    work: "min(0, line 9)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line11"
    value: "4048.45"
    work: "4,048.45 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line14"
    value: "0.00"
    work: "Section 179 in the year placed in service = 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line15"
    value: "43844.12"
    work: "43,844.12 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_full"
    value: "43844.12"
    work: "Line 15 x 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_forty"
    value: "17537.65"
    work: "Line 15 x 40%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_fullcase"
    value: "17537.65"
    work: "Not acquired after 1/19/2025, so 40%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_2025"
    value: "0.00"
    work: "Not claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line16"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_allowed"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line17"
    value: "4048.45"
    work: "4,048.45 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line18"
    value: "43844.12"
    work: "43,844.12 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].qconv"
    value: "mq1"
    work: "Quarter q1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19"
    value: "0.00"
    work: "After the 6-year recovery period; no table rate"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_earlier"
    value: "0.00"
    work: "Zero after the recovery period"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20"
    value: "0.00"
    work: "min(4,048.45, 0)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].b100"
    value: "62380.00"
    work: "62,380 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r1"
    value: "20.00%"
    work: "HY year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t1"
    value: "12476.00"
    work: "62,380 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l1"
    value: "10100.00"
    work: "2019 limit without special allowance (footnote 6)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t1s"
    value: "12476.00"
    work: "0 + 12,476"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d1"
    value: "10100.00"
    work: "min(10,100, 12,476)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r2"
    value: "32.00%"
    work: "HY year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t2"
    value: "19961.60"
    work: "62,380 x 32%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l2"
    value: "16100.00"
    work: "2019 vehicle, 2nd year"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d2"
    value: "16100.00"
    work: "min(16,100, 19,961.60)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r3"
    value: "19.20%"
    work: "HY year 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t3"
    value: "11976.96"
    work: "62,380 x 19.2%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l3"
    value: "9700.00"
    work: "2019 vehicle, 3rd year"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d3"
    value: "9700.00"
    work: "min(9,700, 11,976.96)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r4"
    value: "11.52%"
    work: "HY year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t4"
    value: "7186.18"
    work: "62,380 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l4"
    value: "5760.00"
    work: "2019 vehicle, 4th & later year"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d4"
    value: "5760.00"
    work: "min(5,760, 7,186.18)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r5"
    value: "11.52%"
    work: "HY year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t5"
    value: "7186.18"
    work: "62,380 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l5"
    value: "5760.00"
    work: "4th & later limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d5"
    value: "5760.00"
    work: "min(5,760, 7,186.18)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r6"
    value: "5.76%"
    work: "HY year 6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t6"
    value: "3593.09"
    work: "62,380 x 5.76%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l6"
    value: "5760.00"
    work: "4th & later limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d6"
    value: "3593.09"
    work: "min(5,760, 3,593.09)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d_total"
    value: "51013.09"
    work: "10,100 + 16,100 + 9,700 + 5,760 + 5,760 + 3,593.09"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].unrecovered"
    value: "11366.91"
    work: "62,380 - 51,013.09"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].post_amount"
    value: "5760.00"
    work: "min(5,760, 11,366.91)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].post"
    value: "4048.45"
    work: "5,760 x 9,083/12,923"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].too_old"
    value: "no"
    work: "Placed in service 2019"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_v"
    value: "0.00"
    work: "No special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_pass"
    value: "4048.45"
    work: "2019 vehicle: post-recovery amount"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_heavy"
    value: "0.00"
    work: "No deduction after the recovery period for property not subject to the limits"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_v"
    value: "4048.45"
    work: "Subject to the passenger auto limits"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus"
    value: "0.00"
    work: "Standard rate: no depreciation"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs"
    value: "0.00"
    work: "Standard rate: no depreciation"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_o"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_o"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_o"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].q4_basis"
    value: "0.00"
    work: "Quarter q1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_o"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total_o"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179_o"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bm_c"
    value: "3135.00"
    work: "Business miles 3,135"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cm_c"
    value: "0.00"
    work: "Commuting miles 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].om_c"
    value: "407.00"
    work: "Other miles 407"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].nonbusiness_c"
    value: "407.00"
    work: "0 + 407"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].total_c"
    value: "3542.00"
    work: "3,135 + 407"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].over_half"
    value: "yes"
    work: "3,135/3,542 = 88.51%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].smr_bad"
    value: "no"
    work: "Filer answered that the standard mileage rate may be used"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].smr_amount"
    value: "2194.50"
    work: "3,135 x 0.70"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9_standard"
    value: "2194.50"
    work: "2,194.50 + 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].operating_business"
    value: "1339.15"
    work: "1,513 x 3,135/3,542"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9_actual"
    value: "1339.15"
    work: "1,339.15 + 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9"
    value: "2194.50"
    work: "Standard mileage rate chosen"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is_actual_owned"
    value: "no"
    work: "Leased; standard rate"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is_actual_leased"
    value: "no"
    work: "Standard rate"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lease_business"
    value: "2418.96"
    work: "2,733 x 3,135/3,542"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line20a"
    value: "0.00"
    work: "Standard rate: no lease payments deducted"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].low_use"
    value: "no"
    work: "88.51% > 50%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].screened"
    value: "no"
    work: "No screening condition applies"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].year"
    value: "1"
    work: "Placed in service 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is2025"
    value: "yes"
    work: "Placed in service 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is2019"
    value: "no"
    work: "Placed in service 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bus_cost"
    value: "12031.07"
    work: "13,593 x 3,135/3,542"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_bad"
    value: "no"
    work: "Election 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_mixed"
    value: "no"
    work: "Same choice for all 5-year property"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].claims_bonus"
    value: "no"
    work: "Special allowance = none"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lim_first_bonus"
    value: "20200.00"
    work: "2025 table, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lim_first_none"
    value: "12200.00"
    work: "2025 table footnote 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lim_2025"
    value: "12200.00"
    work: "No special allowance claimed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lim_prior"
    value: "20200.00"
    work: "2025 table, 1st year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line7"
    value: "12200.00"
    work: "2025 vehicle with no special allowance"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9w"
    value: "10798.14"
    work: "12,200 x 3,135/3,542"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_ok"
    value: "0.00"
    work: "Election 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line10"
    value: "0.00"
    work: "Election 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line10_2025"
    value: "0.00"
    work: "min(0, 10,798.14)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_line10"
    value: "0.00"
    work: "min(0, line 9)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line11"
    value: "10798.14"
    work: "10,798.14 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line14"
    value: "0.00"
    work: "Section 179 = 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line15"
    value: "12031.07"
    work: "12,031.07 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_full"
    value: "12031.07"
    work: "Line 15 x 100%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_forty"
    value: "4812.43"
    work: "Line 15 x 40%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_fullcase"
    value: "12031.07"
    work: "Acquired after 1/19/2025, so 100%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_2025"
    value: "0.00"
    work: "Not claimed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line16"
    value: "0.00"
    work: "Elected none"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line17"
    value: "10798.14"
    work: "10,798.14 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line18"
    value: "12031.07"
    work: "12,031.07 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].qconv"
    value: "mq1"
    work: "Quarter q1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].rate_hy"
    value: "20.00%"
    work: "HY year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].rate_mq"
    value: "35.00%"
    work: "MQ Q1 year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].rate_prior"
    value: "5.00%"
    work: "Convention mq4, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_hy"
    value: "2406.21"
    work: "12,031.07 x 20%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_mq"
    value: "4210.87"
    work: "12,031.07 x 35%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_prior"
    value: "601.55"
    work: "12,031.07 x 5%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19"
    value: "4210.87"
    work: "2025 vehicle; mid-quarter test is yes"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_earlier"
    value: "601.55"
    work: "line19_prior"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_2025"
    value: "4210.87"
    work: "Mid-quarter Q1 amount"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line20"
    value: "4210.87"
    work: "min(10,798.14, 4,210.87)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].b100"
    value: "13593.00"
    work: "13,593 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r1"
    value: "5.00%"
    work: "Convention mq4, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t1"
    value: "679.65"
    work: "13,593 x 5%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].l1"
    value: "12200.00"
    work: "2025 limit without special allowance"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t1s"
    value: "679.65"
    work: "0 + 679.65"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].d1"
    value: "679.65"
    work: "min(12,200, 679.65)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r2"
    value: "38.00%"
    work: "MQ Q4 year 2"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t2"
    value: "5165.34"
    work: "13,593 x 38%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r3"
    value: "22.80%"
    work: "MQ Q4 year 3"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t3"
    value: "3099.20"
    work: "13,593 x 22.8%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r4"
    value: "13.68%"
    work: "MQ Q4 year 4"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t4"
    value: "1859.52"
    work: "13,593 x 13.68%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r5"
    value: "10.94%"
    work: "MQ Q4 year 5"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t5"
    value: "1487.07"
    work: "13,593 x 10.94%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r6"
    value: "9.58%"
    work: "MQ Q4 year 6"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t6"
    value: "1302.21"
    work: "13,593 x 9.58%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].too_old"
    value: "no"
    work: "Placed in service 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_v"
    value: "0.00"
    work: "No special allowance"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_pass"
    value: "4210.87"
    work: "Line 20"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_heavy"
    value: "4210.87"
    work: "Line 19"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_v"
    value: "4210.87"
    work: "Subject to the passenger auto limits"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus"
    value: "0.00"
    work: "Leased, standard rate"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs"
    value: "0.00"
    work: "Leased, standard rate"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_2025"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_q4"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_total"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cost179"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_o"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_o"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_o"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].q4_basis"
    value: "0.00"
    work: "Quarter q1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_o"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_a2"
    value: "0.00"
    work: "q4_basis = 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_total_o"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_total_a2"
    value: "12031.07"
    work: "Business cost less 0 section 179"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cost179_o"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cost179_a2"
    value: "12031.07"
    work: "Business cost"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bm_c"
    value: "3830.00"
    work: "Business miles 3,830"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cm_c"
    value: "0.00"
    work: "Commuting miles 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].om_c"
    value: "78.00"
    work: "Other miles 78"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].nonbusiness_c"
    value: "78.00"
    work: "0 + 78"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].total_c"
    value: "3908.00"
    work: "3,830 + 78"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].over_half"
    value: "yes"
    work: "3,830/3,908 = 98.00%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].smr_bad"
    value: "no"
    work: "Filer answered that the standard mileage rate may be used"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].smr_amount"
    value: "2681.00"
    work: "3,830 x 0.70"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9_standard"
    value: "2681.00"
    work: "2,681 + 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].operating_business"
    value: "0.00"
    work: "Operating expenses 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9_actual"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9"
    value: "0.00"
    work: "Actual expenses chosen"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is_actual_owned"
    value: "no"
    work: "Leased"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is_actual_leased"
    value: "yes"
    work: "Leased, actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].lease_business"
    value: "0.00"
    work: "Lease payments 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line20a"
    value: "0.00"
    work: "Lease business portion 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].low_use"
    value: "no"
    work: "98.00% > 50%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].screened"
    value: "no"
    work: "No screening condition applies"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].year"
    value: "1"
    work: "Placed in service 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is2025"
    value: "yes"
    work: "Placed in service 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is2019"
    value: "no"
    work: "Placed in service 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bus_cost"
    value: "76802.87"
    work: "78,367 x 3,830/3,908"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_bad"
    value: "no"
    work: "Election 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_mixed"
    value: "no"
    work: "Same choice for all 5-year property"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].claims_bonus"
    value: "no"
    work: "Special allowance = none"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].lim_first_bonus"
    value: "20200.00"
    work: "2025 table, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].lim_first_none"
    value: "12200.00"
    work: "2025 table footnote 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].lim_2025"
    value: "12200.00"
    work: "No special allowance claimed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].lim_prior"
    value: "20200.00"
    work: "2025 table, 1st year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line7"
    value: "12200.00"
    work: "2025 vehicle with no special allowance"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9w"
    value: "11956.50"
    work: "12,200 x 3,830/3,908"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_ok"
    value: "0.00"
    work: "Election 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line10"
    value: "0.00"
    work: "Election 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line10_2025"
    value: "0.00"
    work: "min(0, 11,956.50)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_line10"
    value: "0.00"
    work: "min(0, line 9)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line11"
    value: "11956.50"
    work: "11,956.50 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line14"
    value: "0.00"
    work: "Section 179 = 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line15"
    value: "76802.87"
    work: "76,802.87 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_full"
    value: "76802.87"
    work: "Line 15 x 100%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_forty"
    value: "30721.15"
    work: "Line 15 x 40%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_fullcase"
    value: "76802.87"
    work: "Acquired after 1/19/2025, so 100%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_2025"
    value: "0.00"
    work: "Not claimed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line16"
    value: "0.00"
    work: "Elected none"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_allowed"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line17"
    value: "11956.50"
    work: "11,956.50 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line18"
    value: "76802.87"
    work: "76,802.87 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].qconv"
    value: "mq3"
    work: "Quarter q3"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].rate_hy"
    value: "20.00%"
    work: "HY year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].rate_mq"
    value: "15.00%"
    work: "MQ Q3 year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].rate_prior"
    value: "20.00%"
    work: "Convention hy, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_hy"
    value: "15360.57"
    work: "76,802.87 x 20%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_mq"
    value: "11520.43"
    work: "76,802.87 x 15%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_prior"
    value: "15360.57"
    work: "76,802.87 x 20%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19"
    value: "11520.43"
    work: "2025 vehicle; mid-quarter test is yes"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_earlier"
    value: "15360.57"
    work: "line19_prior"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_2025"
    value: "11520.43"
    work: "Mid-quarter Q3 amount"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line20"
    value: "11520.43"
    work: "min(11,956.50, 11,520.43)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].b100"
    value: "78367.00"
    work: "78,367 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r1"
    value: "20.00%"
    work: "HY year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t1"
    value: "15673.40"
    work: "78,367 x 20%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].l1"
    value: "12200.00"
    work: "2025 limit without special allowance"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t1s"
    value: "15673.40"
    work: "0 + 15,673.40"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].d1"
    value: "12200.00"
    work: "min(12,200, 15,673.40)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r2"
    value: "32.00%"
    work: "HY year 2"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t2"
    value: "25077.44"
    work: "78,367 x 32%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r3"
    value: "19.20%"
    work: "HY year 3"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t3"
    value: "15046.46"
    work: "78,367 x 19.2%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r4"
    value: "11.52%"
    work: "HY year 4"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t4"
    value: "9027.88"
    work: "78,367 x 11.52%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r5"
    value: "11.52%"
    work: "HY year 5"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t5"
    value: "9027.88"
    work: "78,367 x 11.52%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r6"
    value: "5.76%"
    work: "HY year 6"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t6"
    value: "4513.94"
    work: "78,367 x 5.76%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].too_old"
    value: "no"
    work: "Placed in service 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_v"
    value: "0.00"
    work: "No special allowance"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_pass"
    value: "11520.43"
    work: "Line 20"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_heavy"
    value: "11520.43"
    work: "Line 19"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_v"
    value: "11520.43"
    work: "Subject to the passenger auto limits"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus"
    value: "0.00"
    work: "Leased: no depreciation"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs"
    value: "0.00"
    work: "Leased: no depreciation"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_2025"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_q4"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_total"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cost179"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].q4_basis"
    value: "0.00"
    work: "Quarter q3"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_a2"
    value: "0.00"
    work: "q4_basis = 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_total_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_total_a2"
    value: "76802.87"
    work: "Business cost less 0 section 179"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cost179_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cost179_a2"
    value: "76802.87"
    work: "Business cost"
```
```

### classm.scveh.3

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bm_c"
    value: "14464.00"
    work: "Business miles 14,464"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cm_c"
    value: "3165.00"
    work: "Commuting miles 3,165"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].om_c"
    value: "3075.00"
    work: "Other miles 3,075"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c"
    value: "6240.00"
    work: "3,165 + 3,075"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].total_c"
    value: "20704.00"
    work: "14,464 + 6,240"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].over_half"
    value: "yes"
    work: "14,464 / 20,704 = 69.86% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_bad"
    value: "no"
    work: "Filer says the standard mileage rate may be used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_amount"
    value: "10124.80"
    work: "14,464 x 0.70"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_standard"
    value: "10124.80"
    work: "10,124.80 + 0 parking and tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].operating_business"
    value: "2325.67"
    work: "3,329 x 14,464 / 20,704"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_actual"
    value: "2325.67"
    work: "2,325.67 + 0 parking and tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9"
    value: "2325.67"
    work: "Actual expenses chosen"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned"
    value: "no"
    work: "Vehicle is leased"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased"
    value: "yes"
    work: "Leased and on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lease_business"
    value: "3140.25"
    work: "4,495 x 14,464 / 20,704"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "3140.25"
    work: "Leased and on actual expenses, so the business lease portion goes on line 20a"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].low_use"
    value: "no"
    work: "Business use is 69.86%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].screened"
    value: "no"
    work: "None of the screening conditions applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].year"
    value: "5"
    work: "Placed in service 2021, so 2025 is year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2025"
    value: "no"
    work: "Placed in service 2021"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2019"
    value: "no"
    work: "Placed in service 2021"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bus_cost"
    value: "3493.04"
    work: "5,000 x 69.86%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_bad"
    value: "no"
    work: "Elected 0 is not more than the business cost"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed"
    value: "no"
    work: "Same choice for all 5-year property"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus"
    value: "no"
    work: "Special allowance = none"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus"
    value: "20200.00"
    work: "2025 first-year limit with the special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_prior"
    value: "5860.00"
    work: "2021 vehicle, 4th and later year limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line7"
    value: "5860.00"
    work: "Limit for year 5 of a 2021 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9w"
    value: "4093.85"
    work: "5,860 x 14,464 / 20,704"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10"
    value: "0.00"
    work: "Not the year placed in service, so -0-"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10_2025"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_line10"
    value: "0.00"
    work: "Smaller of election 0 or line 9"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line11"
    value: "4093.85"
    work: "4,093.85 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line14"
    value: "5000.00"
    work: "Section 179 claimed in the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line15"
    value: "0.00"
    work: "3,493.04 - 5,000 is less than zero, so 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_full"
    value: "0.00"
    work: "0 x 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty"
    value: "0.00"
    work: "0 x 40%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase"
    value: "0.00"
    work: "Acquired after January 19, 2025, so 100% of 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025"
    value: "0.00"
    work: "Not claimed and not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line16"
    value: "0.00"
    work: "Not the year placed in service, so -0-"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "Smaller of 0 or line 11"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line17"
    value: "4093.85"
    work: "4,093.85 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line18"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].qconv"
    value: "mq3"
    work: "Placed in service in Q3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_hy"
    value: "20.00%"
    work: "5-year, 200DB, half-year convention, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_mq"
    value: "15.00%"
    work: "5-year, mid-quarter Q3, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_prior"
    value: "10.94%"
    work: "5-year, mid-quarter Q4, year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_hy"
    value: "0.00"
    work: "0 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_mq"
    value: "0.00"
    work: "0 x 15%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_prior"
    value: "0.00"
    work: "0 x 10.94%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19"
    value: "0.00"
    work: "Prior-year rate applied"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier"
    value: "0.00"
    work: "Line 19 for a pre-2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_2025"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20"
    value: "0.00"
    work: "Lesser of 4,093.85 or 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].b100"
    value: "0.00"
    work: "5,000 - 5,000"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r1"
    value: "5.00%"
    work: "Mid-quarter Q4, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1"
    value: "0.00"
    work: "0 x 5%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1s"
    value: "5000.00"
    work: "5,000 + 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r2"
    value: "38.00%"
    work: "Mid-quarter Q4, year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t2"
    value: "0.00"
    work: "0 x 38%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l2"
    value: "16400.00"
    work: "2021 vehicle, 2nd year limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d2"
    value: "0.00"
    work: "Lesser of 0 or 16,400"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r3"
    value: "22.80%"
    work: "Mid-quarter Q4, year 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t3"
    value: "0.00"
    work: "0 x 22.8%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l3"
    value: "9800.00"
    work: "2021 vehicle, 3rd year limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d3"
    value: "0.00"
    work: "Lesser of 0 or 9,800"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r4"
    value: "13.68%"
    work: "Mid-quarter Q4, year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t4"
    value: "0.00"
    work: "0 x 13.68%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l4"
    value: "5860.00"
    work: "2021 vehicle, 4th year limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d4"
    value: "0.00"
    work: "Lesser of 0 or 5,860"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r5"
    value: "10.94%"
    work: "Mid-quarter Q4, year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t5"
    value: "0.00"
    work: "0 x 10.94%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l5"
    value: "5860.00"
    work: "2021 vehicle, later-year limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d5"
    value: "0.00"
    work: "Lesser of 0 or 5,860"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r6"
    value: "9.58%"
    work: "Mid-quarter Q4, year 6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t6"
    value: "0.00"
    work: "0 x 9.58%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].too_old"
    value: "no"
    work: "Placed in service 2021"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_v"
    value: "0.00"
    work: "Line 16 = 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass"
    value: "0.00"
    work: "Line 20"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy"
    value: "0.00"
    work: "Line 19"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_v"
    value: "0.00"
    work: "Passenger automobile, so macrs_pass"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus"
    value: "0.00"
    work: "Leased vehicle, no depreciation"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs"
    value: "0.00"
    work: "Leased vehicle, no depreciation"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025"
    value: "0.00"
    work: "Leased vehicle, not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4"
    value: "0.00"
    work: "Not a 2025 owned vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total"
    value: "0.00"
    work: "Not a 2025 owned vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179"
    value: "0.00"
    work: "Not a 2025 owned vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].q4_basis"
    value: "0.00"
    work: "Placed in service in Q3, not October to December"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_o"
    value: "0.00"
    work: "Not owned"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bm_c"
    value: "16003.00"
    work: "Business miles 16,003"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cm_c"
    value: "2910.00"
    work: "Commuting miles 2,910"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].om_c"
    value: "4.00"
    work: "Other miles 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].nonbusiness_c"
    value: "2914.00"
    work: "2,910 + 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].total_c"
    value: "18917.00"
    work: "16,003 + 2,914"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].over_half"
    value: "yes"
    work: "16,003 / 18,917 = 84.60% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].smr_bad"
    value: "no"
    work: "Filer says the standard mileage rate may be used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].smr_amount"
    value: "11202.10"
    work: "16,003 x 0.70"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9_standard"
    value: "11202.10"
    work: "11,202.10 + 0 parking and tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].operating_business"
    value: "3438.82"
    work: "4,065 x 16,003 / 18,917"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9_actual"
    value: "3438.82"
    work: "3,438.82 + 0 parking and tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9"
    value: "11202.10"
    work: "Standard mileage rate chosen"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is_actual_owned"
    value: "no"
    work: "Standard rate, leased"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is_actual_leased"
    value: "no"
    work: "Standard rate"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lease_business"
    value: "6767.67"
    work: "8,000 x 16,003 / 18,917"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20a"
    value: "0.00"
    work: "Standard rate, so no lease payments are deducted"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].low_use"
    value: "no"
    work: "Business use is 84.60%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].screened"
    value: "no"
    work: "None of the screening conditions applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].year"
    value: "4"
    work: "Placed in service 2022, so 2025 is year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is2025"
    value: "no"
    work: "Placed in service 2022"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is2019"
    value: "no"
    work: "Placed in service 2022"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bus_cost"
    value: "34906.79"
    work: "41,263 x 16,003 / 18,917"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_bad"
    value: "no"
    work: "Elected 0 is not more than the business cost"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_mixed"
    value: "no"
    work: "Same choice for all 5-year property"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].claims_bonus"
    value: "no"
    work: "Special allowance = none"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_first_bonus"
    value: "20200.00"
    work: "2025 first-year limit with the special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_prior"
    value: "6460.00"
    work: "2022 vehicle, 4th year limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line7"
    value: "6460.00"
    work: "Limit for year 4 of a 2022 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9w"
    value: "5464.89"
    work: "6,460 x 16,003 / 18,917"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_ok"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line10"
    value: "0.00"
    work: "Not the year placed in service, so -0-"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line10_2025"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_line10"
    value: "0.00"
    work: "Smaller of election 0 or line 9"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line11"
    value: "5464.89"
    work: "5,464.89 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line14"
    value: "2368.00"
    work: "Section 179 claimed in the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line15"
    value: "32538.79"
    work: "34,906.79 - 2,368"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_full"
    value: "0.00"
    work: "No allowance claimed, so 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_forty"
    value: "0.00"
    work: "No allowance claimed, so 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_fullcase"
    value: "0.00"
    work: "No allowance claimed, so 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_2025"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line16"
    value: "0.00"
    work: "Not the year placed in service, so -0-"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_allowed"
    value: "0.00"
    work: "Smaller of 0 or line 11"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line17"
    value: "5464.89"
    work: "5,464.89 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line18"
    value: "32538.79"
    work: "32,538.79 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].qconv"
    value: "mq3"
    work: "Placed in service in Q3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].rate_hy"
    value: "20.00%"
    work: "5-year, half-year convention, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].rate_mq"
    value: "15.00%"
    work: "5-year, mid-quarter Q3, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].rate_prior"
    value: "11.52%"
    work: "5-year, half-year convention, year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_hy"
    value: "6507.76"
    work: "32,538.79 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_mq"
    value: "4880.82"
    work: "32,538.79 x 15%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_prior"
    value: "3748.47"
    work: "32,538.79 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19"
    value: "3748.47"
    work: "Prior-year vehicle, so year-4 rate"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_earlier"
    value: "3748.47"
    work: "Line 19 for a pre-2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_2025"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20"
    value: "3748.47"
    work: "Lesser of 5,464.89 or 3,748.47"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].b100"
    value: "38895.00"
    work: "41,263 - 2,368"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r1"
    value: "20.00%"
    work: "Half-year convention, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t1"
    value: "7779.00"
    work: "38,895 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t1s"
    value: "10147.00"
    work: "2,368 + 7,779"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r2"
    value: "32.00%"
    work: "Half-year convention, year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t2"
    value: "12446.40"
    work: "38,895 x 32%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l2"
    value: "18000.00"
    work: "2022 vehicle, 2nd year limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d2"
    value: "12446.40"
    work: "Lesser of 12,446.40 or 18,000"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r3"
    value: "19.20%"
    work: "Half-year convention, year 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t3"
    value: "7467.84"
    work: "38,895 x 19.2%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l3"
    value: "10800.00"
    work: "2022 vehicle, 3rd year limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d3"
    value: "7467.84"
    work: "Lesser of 7,467.84 or 10,800"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r4"
    value: "11.52%"
    work: "Half-year convention, year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t4"
    value: "4480.70"
    work: "38,895 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l4"
    value: "6460.00"
    work: "2022 vehicle, 4th year limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d4"
    value: "4480.70"
    work: "Lesser of 4,480.70 or 6,460"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r5"
    value: "11.52%"
    work: "Half-year convention, year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t5"
    value: "4480.70"
    work: "38,895 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r6"
    value: "5.76%"
    work: "Half-year convention, year 6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t6"
    value: "2240.35"
    work: "38,895 x 5.76%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].too_old"
    value: "no"
    work: "Placed in service 2022"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_v"
    value: "0.00"
    work: "Line 16 = 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_pass"
    value: "3748.47"
    work: "Line 20"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_heavy"
    value: "3748.47"
    work: "Line 19"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_v"
    value: "3748.47"
    work: "Passenger automobile, so macrs_pass"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus"
    value: "0.00"
    work: "Standard rate and leased, no depreciation"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs"
    value: "0.00"
    work: "Standard rate and leased, no depreciation"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025"
    value: "0.00"
    work: "Not owned on actual expenses, not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4"
    value: "0.00"
    work: "Not a 2025 owned vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total"
    value: "0.00"
    work: "Not a 2025 owned vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179"
    value: "0.00"
    work: "Not a 2025 owned vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].q4_basis"
    value: "0.00"
    work: "Placed in service in Q3, not October to December"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
```
```

### classm.scveh.4

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bm_c"
    value: "27186.00"
    work: "Business miles 27,186"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cm_c"
    value: "0.00"
    work: "Commuting miles 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].om_c"
    value: "3177.00"
    work: "Other miles 3,177"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c"
    value: "3177.00"
    work: "0 + 3,177"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].total_c"
    value: "30363.00"
    work: "27,186 + 3,177"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].over_half"
    value: "yes"
    work: "27,186/30,363 = 89.54% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_bad"
    value: "no"
    work: "Filer may use the standard mileage rate"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_amount"
    value: "19030.20"
    work: "27,186 x 0.70"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_standard"
    value: "19030.20"
    work: "19,030.20 + 0 parking/tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].operating_business"
    value: "4402.51"
    work: "4,917 x 27,186/30,363"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_actual"
    value: "4402.51"
    work: "4,402.51 + 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9"
    value: "4402.51"
    work: "Actual expenses chosen"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned"
    value: "yes"
    work: "Owned; actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased"
    value: "no"
    work: "Not leased"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lease_business"
    value: "0.00"
    work: "0 lease payments x business %"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "0.00"
    work: "Owned vehicle; no lease"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].low_use"
    value: "no"
    work: "89.54% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].screened"
    value: "no"
    work: "No special case applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].year"
    value: "1"
    work: "Placed in service 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2025"
    value: "yes"
    work: "y2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2019"
    value: "no"
    work: "y2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bus_cost"
    value: "22276.71"
    work: "24,880 x 27,186/30,363"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_bad"
    value: "no"
    work: "14,596 <= 22,276.71; not an SUV"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed"
    value: "no"
    work: "Same choice for all 5-year property"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus"
    value: "no"
    work: "Special allowance = none"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus"
    value: "20200.00"
    work: "Pub 946 table, 2025 1st year"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_first_none"
    value: "12200.00"
    work: "Footnote 1: no special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_2025"
    value: "12200.00"
    work: "No special allowance claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_prior"
    value: "0.00"
    work: "Not a prior-year vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line7"
    value: "12200.00"
    work: "2025 vehicle limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9w"
    value: "10923.47"
    work: "12,200 x 27,186/30,363"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok"
    value: "14596.00"
    work: "Elected section 179 cost"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10"
    value: "10923.47"
    work: "Smaller of 14,596 or line 9 10,923.47"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10_2025"
    value: "10923.47"
    work: "Smaller of 14,596 or 10,923.47"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_line10"
    value: "10923.47"
    work: "Smaller of 14,596 or 10,923.47"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line11"
    value: "0.00"
    work: "10,923.47 - 10,923.47"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line14"
    value: "10923.47"
    work: "Section 179 claimed in 2025 (line 10)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line15"
    value: "11353.24"
    work: "22,276.71 - 10,923.47"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_full"
    value: "11353.24"
    work: "11,353.24 x 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty"
    value: "4541.30"
    work: "11,353.24 x 40%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase"
    value: "11353.24"
    work: "Acquired after Jan 19, 2025, so 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025"
    value: "0.00"
    work: "No special allowance claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line16"
    value: "0.00"
    work: "Not claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "Smaller of 0 or line 11 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line17"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line18"
    value: "11353.24"
    work: "11,353.24 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].qconv"
    value: "mq4"
    work: "Placed in service in Q4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_hy"
    value: "20.00%"
    work: "5-year 200DB HY, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_mq"
    value: "5.00%"
    work: "5-year 200DB MQ Q4, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_prior"
    value: "20.00%"
    work: "HY convention given, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_hy"
    value: "2270.65"
    work: "11,353.24 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_mq"
    value: "567.66"
    work: "11,353.24 x 5%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_prior"
    value: "2270.65"
    work: "11,353.24 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19"
    value: "567.66"
    work: "Mid-quarter convention applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier"
    value: "0.00"
    work: "2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_2025"
    value: "567.66"
    work: "MQ test is yes, so use the MQ rate"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20"
    value: "0.00"
    work: "Lesser of line 17 0 or 567.66"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].b100"
    value: "13956.53"
    work: "24,880 - 10,923.47"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r1"
    value: "20.00%"
    work: "5-year HY, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1"
    value: "2791.31"
    work: "13,956.53 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l1"
    value: "12200.00"
    work: "2025 limit without special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1s"
    value: "13714.78"
    work: "10,923.47 + 2,791.31"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d1"
    value: "12200.00"
    work: "Lesser of 12,200 or 13,714.78"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r2"
    value: "32.00%"
    work: "5-year HY, year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t2"
    value: "4466.09"
    work: "13,956.53 x 32%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r3"
    value: "19.20%"
    work: "5-year HY, year 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t3"
    value: "2679.65"
    work: "13,956.53 x 19.2%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r4"
    value: "11.52%"
    work: "5-year HY, year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t4"
    value: "1607.79"
    work: "13,956.53 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r5"
    value: "11.52%"
    work: "5-year HY, year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t5"
    value: "1607.79"
    work: "13,956.53 x 11.52%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r6"
    value: "5.76%"
    work: "5-year HY, year 6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t6"
    value: "803.90"
    work: "13,956.53 x 5.76%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].too_old"
    value: "no"
    work: "Placed in service 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_v"
    value: "0.00"
    work: "No special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass"
    value: "0.00"
    work: "Worksheet line 20"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy"
    value: "567.66"
    work: "Line 18 x MQ rate, no limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_v"
    value: "0.00"
    work: "Subject to the passenger automobile limits"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus"
    value: "0.00"
    work: "bonus_v"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs"
    value: "0.00"
    work: "macrs_v"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025"
    value: "10923.47"
    work: "Line 10"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4"
    value: "11353.24"
    work: "22,276.71 - 10,923.47, Q4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total"
    value: "11353.24"
    work: "Business basis less section 179"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179"
    value: "22276.71"
    work: "Business cost of listed section 179 property"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_o"
    value: "0.00"
    work: "Owned, actual"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_o"
    value: "0.00"
    work: "Owned, actual"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o"
    value: "10923.47"
    work: "Owned, actual"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].q4_basis"
    value: "11353.24"
    work: "Placed in service in Q4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o"
    value: "11353.24"
    work: "Owned, actual"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2"
    value: "11353.24"
    work: "2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o"
    value: "11353.24"
    work: "Owned, actual"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2"
    value: "11353.24"
    work: "2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_o"
    value: "22276.71"
    work: "Owned, actual"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2"
    value: "22276.71"
    work: "2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bm_c"
    value: "29702.00"
    work: "Business miles 29,702"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cm_c"
    value: "0.00"
    work: "Commuting miles 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].om_c"
    value: "3185.00"
    work: "Other miles 3,185"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].nonbusiness_c"
    value: "3185.00"
    work: "0 + 3,185"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].total_c"
    value: "32887.00"
    work: "29,702 + 3,185"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].over_half"
    value: "yes"
    work: "29,702/32,887 = 90.32% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].smr_bad"
    value: "no"
    work: "Filer may use the standard mileage rate"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].smr_amount"
    value: "20791.40"
    work: "29,702 x 0.70"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9_standard"
    value: "20791.40"
    work: "20,791.40 + 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].operating_business"
    value: "137.28"
    work: "152 x 29,702/32,887"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9_actual"
    value: "137.28"
    work: "137.28 + 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9"
    value: "137.28"
    work: "Actual expenses chosen"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is_actual_owned"
    value: "yes"
    work: "Owned; actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is_actual_leased"
    value: "no"
    work: "Not leased"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lease_business"
    value: "3096.01"
    work: "3,428 x 29,702/32,887"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20a"
    value: "0.00"
    work: "Owned vehicle, so no line 20a amount"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].low_use"
    value: "no"
    work: "90.32% > 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].screened"
    value: "no"
    work: "No special case applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].year"
    value: "6"
    work: "2025 - 2020 + 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is2025"
    value: "no"
    work: "y2020"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is2019"
    value: "no"
    work: "y2020"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bus_cost"
    value: "55566.50"
    work: "61,525 x 29,702/32,887"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_bad"
    value: "no"
    work: "Election 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_mixed"
    value: "no"
    work: "Same choice for all 5-year property"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].claims_bonus"
    value: "no"
    work: "Special allowance = none"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_first_bonus"
    value: "18100.00"
    work: "Pub 946 table, 2020 1st year"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_prior"
    value: "5760.00"
    work: "2020 vehicle, 4th and later year"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line7"
    value: "5760.00"
    work: "Year 6 limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9w"
    value: "5202.16"
    work: "5,760 x 29,702/32,887"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_ok"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line10"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line10_2025"
    value: "0.00"
    work: "Election 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_line10"
    value: "0.00"
    work: "Election 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line11"
    value: "5202.16"
    work: "5,202.16 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line14"
    value: "0.00"
    work: "Section 179 claimed in 2020 = 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line15"
    value: "55566.50"
    work: "55,566.50 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_full"
    value: "55566.50"
    work: "55,566.50 x 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_forty"
    value: "22226.60"
    work: "55,566.50 x 40%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_fullcase"
    value: "55566.50"
    work: "Acquired after Jan 19, 2025 = yes"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_2025"
    value: "0.00"
    work: "Not a 2025 vehicle; not claimed"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line16"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_allowed"
    value: "0.00"
    work: "Smaller of 0 or 5,202.16"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line17"
    value: "5202.16"
    work: "5,202.16 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line18"
    value: "55566.50"
    work: "55,566.50 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].qconv"
    value: "mq1"
    work: "Quarter q1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].rate_hy"
    value: "20.00%"
    work: "5-year HY, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].rate_mq"
    value: "35.00%"
    work: "5-year MQ Q1, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].rate_prior"
    value: "4.26%"
    work: "5-year MQ Q2 (mq2), year 6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_hy"
    value: "11113.30"
    work: "55,566.50 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_mq"
    value: "19448.28"
    work: "55,566.50 x 35%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_prior"
    value: "2367.13"
    work: "55,566.50 x 4.26%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19"
    value: "2367.13"
    work: "Prior-year vehicle rate"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_earlier"
    value: "2367.13"
    work: "Year 6 is within the recovery period"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_2025"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20"
    value: "2367.13"
    work: "Lesser of 5,202.16 or 2,367.13"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].b100"
    value: "61525.00"
    work: "61,525 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r1"
    value: "25.00%"
    work: "5-year MQ Q2, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t1"
    value: "15381.25"
    work: "61,525 x 25%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t1s"
    value: "15381.25"
    work: "0 + 15,381.25"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r2"
    value: "30.00%"
    work: "5-year MQ Q2, year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t2"
    value: "18457.50"
    work: "61,525 x 30%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l2"
    value: "16100.00"
    work: "2020 vehicle, 2nd year"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d2"
    value: "16100.00"
    work: "Lesser of 16,100 or 18,457.50"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r3"
    value: "18.00%"
    work: "5-year MQ Q2, year 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t3"
    value: "11074.50"
    work: "61,525 x 18%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l3"
    value: "9700.00"
    work: "2020 vehicle, 3rd year"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d3"
    value: "9700.00"
    work: "Lesser of 9,700 or 11,074.50"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r4"
    value: "11.37%"
    work: "5-year MQ Q2, year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t4"
    value: "6995.39"
    work: "61,525 x 11.37%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l4"
    value: "5760.00"
    work: "2020 vehicle, 4th and later year"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d4"
    value: "5760.00"
    work: "Lesser of 5,760 or 6,995.39"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r5"
    value: "11.37%"
    work: "5-year MQ Q2, year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t5"
    value: "6995.39"
    work: "61,525 x 11.37%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l5"
    value: "5760.00"
    work: "2020 vehicle, 4th and later year"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d5"
    value: "5760.00"
    work: "Lesser of 5,760 or 6,995.39"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r6"
    value: "4.26%"
    work: "5-year MQ Q2, year 6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t6"
    value: "2620.97"
    work: "61,525 x 4.26%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l6"
    value: "5760.00"
    work: "2020 vehicle, 4th and later year"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d6"
    value: "2620.97"
    work: "Lesser of 5,760 or 2,620.97"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].too_old"
    value: "no"
    work: "Placed in service 2020"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_v"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_pass"
    value: "2367.13"
    work: "Worksheet line 20"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_heavy"
    value: "2367.13"
    work: "Line 18 x year-6 rate, no limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_v"
    value: "2367.13"
    work: "Passenger automobile"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus"
    value: "0.00"
    work: "bonus_v"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs"
    value: "2367.13"
    work: "macrs_v"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4"
    value: "0.00"
    work: "Not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total"
    value: "0.00"
    work: "Not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179"
    value: "0.00"
    work: "Not placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_o"
    value: "0.00"
    work: "Owned, actual"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_o"
    value: "2367.13"
    work: "Owned, actual"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_o"
    value: "0.00"
    work: "Owned, actual"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].q4_basis"
    value: "0.00"
    work: "Quarter q1, not Q4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_o"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total_o"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179_o"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
```
```

### classm.scveh.5

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bm_c"
    value: "21632.00"
    work: "Business miles 21,632"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cm_c"
    value: "0.00"
    work: "Commuting miles 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].om_c"
    value: "1803.00"
    work: "Other miles 1,803"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].nonbusiness_c"
    value: "1803.00"
    work: "0 + 1,803"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].total_c"
    value: "23435.00"
    work: "21,632 + 1,803"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].over_half"
    value: "yes"
    work: "21,632/23,435 = 92.31% > 50%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].smr_bad"
    value: "no"
    work: "Filer says the standard mileage rate may be used"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].smr_amount"
    value: "15142.40"
    work: "21,632 x 0.70"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9_standard"
    value: "15142.40"
    work: "15,142.40 + 0 parking and tolls"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].operating_business"
    value: "1853.51"
    work: "2,008 x 21,632/23,435"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9_actual"
    value: "1853.51"
    work: "1,853.51 + 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9"
    value: "1853.51"
    work: "Actual expenses method"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is_actual_owned"
    value: "yes"
    work: "Owned and actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is_actual_leased"
    value: "no"
    work: "Not leased"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lease_business"
    value: "6701.44"
    work: "7,260 x 21,632/23,435"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line20a"
    value: "0.00"
    work: "Not a leased vehicle on actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].low_use"
    value: "no"
    work: "92.31% business use"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].screened"
    value: "no"
    work: "None of the screening conditions apply"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].year"
    value: "1"
    work: "Placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is2025"
    value: "yes"
    work: "y2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].is2019"
    value: "no"
    work: "y2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bus_cost"
    value: "58785.32"
    work: "63,685 x 21,632/23,435"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_bad"
    value: "no"
    work: "Section 179 election is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_mixed"
    value: "no"
    work: "Same choice for all 5-year property"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].claims_bonus"
    value: "yes"
    work: "Filer chose the 40% allowance"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lim_first_bonus"
    value: "20200.00"
    work: "2025 table, first year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lim_first_none"
    value: "12200.00"
    work: "2025 table, footnote 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lim_2025"
    value: "20200.00"
    work: "Special allowance claimed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].lim_prior"
    value: "0.00"
    work: "Not a prior-year vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line7"
    value: "20200.00"
    work: "lim_2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line9w"
    value: "18645.89"
    work: "20,200 x 21,632/23,435"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_ok"
    value: "0.00"
    work: "No section 179 elected"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line10"
    value: "0.00"
    work: "No section 179"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line10_2025"
    value: "0.00"
    work: "min(0, line 9)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_line10"
    value: "0.00"
    work: "min(0, line 9)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line11"
    value: "18645.89"
    work: "18,645.89 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line14"
    value: "0.00"
    work: "No section 179"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line15"
    value: "58785.32"
    work: "58,785.32 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_full"
    value: "58785.32"
    work: "100% x 58,785.32"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_forty"
    value: "23514.13"
    work: "40% x 58,785.32"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_fullcase"
    value: "58785.32"
    work: "Acquired after January 19, 2025, so 100%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_2025"
    value: "23514.13"
    work: "Filer elected 40%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line16"
    value: "23514.13"
    work: "bonus_2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_allowed"
    value: "18645.89"
    work: "min(23,514.13, line 11 18,645.89)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line17"
    value: "0.00"
    work: "18,645.89 - 23,514.13 < 0, so 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line18"
    value: "35271.19"
    work: "58,785.32 - 23,514.13"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].qconv"
    value: "mq3"
    work: "Placed in service in q3"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].rate_hy"
    value: "20.00%"
    work: "5-yr 200DB HY, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].rate_mq"
    value: "15.00%"
    work: "5-yr 200DB MQ Q3, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].rate_prior"
    value: "20.00%"
    work: "Year 1, HY applies (mid-quarter test is no)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_hy"
    value: "7054.24"
    work: "35,271.19 x 20%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_mq"
    value: "5290.68"
    work: "35,271.19 x 15%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_prior"
    value: "7054.24"
    work: "35,271.19 x 20%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19"
    value: "7054.24"
    work: "Half-year convention applies"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_earlier"
    value: "7054.24"
    work: "line19_prior; not a 2019 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line19_2025"
    value: "7054.24"
    work: "Half-year convention, because the mid-quarter test is no"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].line20"
    value: "0.00"
    work: "Lesser of 0 or 7,054.24"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].b100"
    value: "63685.00"
    work: "63,685 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r1"
    value: "20.00%"
    work: "5-yr HY, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t1"
    value: "12737.00"
    work: "63,685 x 20%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].l1"
    value: "12200.00"
    work: "2025 first-year limit, no special allowance"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t1s"
    value: "12737.00"
    work: "0 + 12,737"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].d1"
    value: "12200.00"
    work: "Lesser of 12,200 or 12,737"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r2"
    value: "32.00%"
    work: "5-yr HY, year 2"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t2"
    value: "20379.20"
    work: "63,685 x 32%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r3"
    value: "19.20%"
    work: "5-yr HY, year 3"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t3"
    value: "12227.52"
    work: "63,685 x 19.2%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r4"
    value: "11.52%"
    work: "5-yr HY, year 4"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t4"
    value: "7336.51"
    work: "63,685 x 11.52%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r5"
    value: "11.52%"
    work: "5-yr HY, year 5"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t5"
    value: "7336.51"
    work: "63,685 x 11.52%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].r6"
    value: "5.76%"
    work: "5-yr HY, year 6"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].t6"
    value: "3668.26"
    work: "63,685 x 5.76%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].too_old"
    value: "no"
    work: "Placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_v"
    value: "18645.89"
    work: "bonus_allowed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_pass"
    value: "0.00"
    work: "line 20"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_heavy"
    value: "7054.24"
    work: "line 19, no limit"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_v"
    value: "0.00"
    work: "Subject to the passenger automobile limits"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus"
    value: "18645.89"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs"
    value: "0.00"
    work: "macrs_v"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_2025"
    value: "0.00"
    work: "No section 179"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_q4"
    value: "0.00"
    work: "Placed in service in Q3"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_total"
    value: "58785.32"
    work: "Business basis less section 179 of 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cost179"
    value: "58785.32"
    work: "Business-use cost"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].bonus_o"
    value: "18645.89"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].macrs_o"
    value: "0.00"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].s179_2025_o"
    value: "0.00"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].q4_basis"
    value: "58785.32"
    work: "58,785.32 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_o"
    value: "0.00"
    work: "Not placed in service in Q4"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_q4_a2"
    value: "0.00"
    work: "Not placed in service in Q4"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_total_o"
    value: "58785.32"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].mq_total_a2"
    value: "58785.32"
    work: "2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cost179_o"
    value: "58785.32"
    work: "Owned, actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_1].cost179_a2"
    value: "58785.32"
    work: "2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bm_c"
    value: "15902.00"
    work: "Business miles 15,902"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cm_c"
    value: "0.00"
    work: "Commuting miles 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].om_c"
    value: "12.00"
    work: "Other miles 12"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].nonbusiness_c"
    value: "12.00"
    work: "0 + 12"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].total_c"
    value: "15914.00"
    work: "15,902 + 12"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].over_half"
    value: "yes"
    work: "15,902/15,914 = 99.92%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].smr_bad"
    value: "no"
    work: "Filer says the standard mileage rate may be used"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].smr_amount"
    value: "11131.40"
    work: "15,902 x 0.70"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9_standard"
    value: "11131.40"
    work: "11,131.40 + 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].operating_business"
    value: "1017.23"
    work: "1,018 x 15,902/15,914"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9_actual"
    value: "1017.23"
    work: "1,017.23 + 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9"
    value: "11131.40"
    work: "Standard mileage method"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is_actual_owned"
    value: "no"
    work: "Standard mileage, leased"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is_actual_leased"
    value: "no"
    work: "Standard mileage method"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].lease_business"
    value: "3068.68"
    work: "3,071 x 15,902/15,914"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line20a"
    value: "0.00"
    work: "No lease deduction under the standard mileage rate"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].low_use"
    value: "no"
    work: "99.92% business use"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].screened"
    value: "no"
    work: "None of the screening conditions apply"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].year"
    value: "6"
    work: "Placed in service 2020, so 2025 is year 6"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is2025"
    value: "no"
    work: "y2020"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].is2019"
    value: "no"
    work: "y2020"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bus_cost"
    value: "32395.55"
    work: "32,420 x 15,902/15,914"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_bad"
    value: "no"
    work: "Section 179 election is 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_mixed"
    value: "no"
    work: "Same choice for all 5-year property"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].claims_bonus"
    value: "no"
    work: "Special allowance is none"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].lim_first_bonus"
    value: "20200.00"
    work: "2025 table, first year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].lim_prior"
    value: "5760.00"
    work: "2020 row, 4th and later year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line7"
    value: "5760.00"
    work: "lim_prior"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line9w"
    value: "5755.66"
    work: "5,760 x 15,902/15,914"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_ok"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line10"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line10_2025"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_line10"
    value: "0.00"
    work: "min(0, line 9)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line11"
    value: "5755.66"
    work: "5,755.66 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line14"
    value: "0.00"
    work: "No section 179 claimed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line15"
    value: "32395.55"
    work: "32,395.55 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_full"
    value: "32395.55"
    work: "100% x 32,395.55"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_forty"
    value: "12958.22"
    work: "40% x 32,395.55"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_fullcase"
    value: "32395.55"
    work: "Acquired after January 19, 2025, so 100%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_2025"
    value: "0.00"
    work: "No allowance claimed"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line16"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_allowed"
    value: "0.00"
    work: "min(0, line 11)"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line17"
    value: "5755.66"
    work: "5,755.66 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line18"
    value: "32395.55"
    work: "32,395.55 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].qconv"
    value: "mq1"
    work: "Placed in service in q1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].rate_hy"
    value: "20.00%"
    work: "5-yr HY, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].rate_mq"
    value: "35.00%"
    work: "5-yr MQ Q1, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].rate_prior"
    value: "4.26%"
    work: "5-yr MQ Q2 (mq2), year 6"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_hy"
    value: "6479.11"
    work: "32,395.55 x 20%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_mq"
    value: "11338.44"
    work: "32,395.55 x 35%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_prior"
    value: "1380.05"
    work: "32,395.55 x 4.26%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19"
    value: "1380.05"
    work: "Prior-year vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_earlier"
    value: "1380.05"
    work: "Not a 2019 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line19_2025"
    value: "6479.11"
    work: "Half-year convention, because the mid-quarter test is no"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].line20"
    value: "1380.05"
    work: "Lesser of 5,755.66 or 1,380.05"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].b100"
    value: "32420.00"
    work: "32,420 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r1"
    value: "25.00%"
    work: "5-yr MQ Q2, year 1"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t1"
    value: "8105.00"
    work: "32,420 x 25%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t1s"
    value: "8105.00"
    work: "0 + 8,105"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r2"
    value: "30.00%"
    work: "5-yr MQ Q2, year 2"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t2"
    value: "9726.00"
    work: "32,420 x 30%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].l2"
    value: "16100.00"
    work: "2020 row, 2nd year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].d2"
    value: "9726.00"
    work: "Lesser of 16,100 or 9,726"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r3"
    value: "18.00%"
    work: "5-yr MQ Q2, year 3"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t3"
    value: "5835.60"
    work: "32,420 x 18%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].l3"
    value: "9700.00"
    work: "2020 row, 3rd year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].d3"
    value: "5835.60"
    work: "Lesser of 9,700 or 5,835.60"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r4"
    value: "11.37%"
    work: "5-yr MQ Q2, year 4"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t4"
    value: "3686.15"
    work: "32,420 x 11.37%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].l4"
    value: "5760.00"
    work: "2020 row, 4th and later year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].d4"
    value: "3686.15"
    work: "Lesser of 5,760 or 3,686.15"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r5"
    value: "11.37%"
    work: "5-yr MQ Q2, year 5"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t5"
    value: "3686.15"
    work: "32,420 x 11.37%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].l5"
    value: "5760.00"
    work: "2020 row, 4th and later year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].d5"
    value: "3686.15"
    work: "Lesser of 5,760 or 3,686.15"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].r6"
    value: "4.26%"
    work: "5-yr MQ Q2, year 6"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].t6"
    value: "1381.09"
    work: "32,420 x 4.26%"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].l6"
    value: "5760.00"
    work: "2020 row, 4th and later year"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].d6"
    value: "1381.09"
    work: "Lesser of 5,760 or 1,381.09"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].too_old"
    value: "no"
    work: "Placed in service in 2020"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_v"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_pass"
    value: "1380.05"
    work: "line 20"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_heavy"
    value: "1380.05"
    work: "line 19"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_v"
    value: "1380.05"
    work: "Passenger automobile"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus"
    value: "0.00"
    work: "Standard mileage, leased: no depreciation"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs"
    value: "0.00"
    work: "Standard mileage, leased: no depreciation"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_2025"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_q4"
    value: "0.00"
    work: "Not a 2025 owned vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_total"
    value: "0.00"
    work: "Not a 2025 owned vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cost179"
    value: "0.00"
    work: "Not a 2025 owned vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].bonus_o"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].macrs_o"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].s179_2025_o"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].q4_basis"
    value: "32395.55"
    work: "32,395.55 - 0"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_o"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_q4_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_total_o"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].mq_total_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cost179_o"
    value: "0.00"
    work: "Not owned with actual expenses"
  - printed: "person[taxpayer].sc[biz_b].scveh[car_2].cost179_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
```
```

### classm.scveh.6

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bm_c"
    value: "19788.00"
    work: "Business miles given: 19,788"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cm_c"
    value: "1842.00"
    work: "Commuting miles given: 1,842"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].om_c"
    value: "2248.00"
    work: "Other miles given: 2,248"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].nonbusiness_c"
    value: "4090.00"
    work: "1,842 + 2,248"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].total_c"
    value: "23878.00"
    work: "19,788 + 4,090"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].over_half"
    value: "yes"
    work: "19,788 / 23,878 = 82.87%, which is more than 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_bad"
    value: "no"
    work: "Filer says the standard mileage rate may be used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].smr_amount"
    value: "13851.60"
    work: "19,788 x 0.70"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_standard"
    value: "13884.60"
    work: "13,851.60 + 33.00 parking and tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].operating_business"
    value: "2902.98"
    work: "3,503 x 19,788 / 23,878"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9_actual"
    value: "2935.98"
    work: "2,902.98 + 33.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9"
    value: "13884.60"
    work: "Standard mileage method chosen"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_owned"
    value: "no"
    work: "Standard mileage method, not actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is_actual_leased"
    value: "no"
    work: "Standard mileage method"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lease_business"
    value: "1775.93"
    work: "2,143 x 19,788 / 23,878"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20a"
    value: "0.00"
    work: "Standard mileage rate: no deduction for lease payments"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].low_use"
    value: "no"
    work: "Business use is 82.87%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].screened"
    value: "no"
    work: "Filer says none of the exceptions applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].year"
    value: "2"
    work: "Placed in service in 2024, so 2025 is recovery year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2025"
    value: "no"
    work: "Placed in service in 2024"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].is2019"
    value: "no"
    work: "Placed in service in 2024"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bus_cost"
    value: "28954.39"
    work: "34,939 x 19,788 / 23,878"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_bad"
    value: "no"
    work: "Section 179 election is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_mixed"
    value: "no"
    work: "Filer says the choice is the same for all 5-year property"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].claims_bonus"
    value: "no"
    work: "Special allowance = none"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_first_bonus"
    value: "20200.00"
    work: "Pub 946 table, 2025, 1st year: $20,200"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].lim_prior"
    value: "19800.00"
    work: "Pub 946 table, 2024, 2nd year: $19,800"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line7"
    value: "19800.00"
    work: "Year-2 limit for a 2024 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line9w"
    value: "16408.51"
    work: "19,800 x 19,788 / 23,878"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_ok"
    value: "0.00"
    work: "Not a 2025 vehicle; election is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line10_2025"
    value: "0.00"
    work: "Election is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_line10"
    value: "0.00"
    work: "Smaller of 0 or line 9"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line11"
    value: "16408.51"
    work: "16,408.51 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line14"
    value: "0.00"
    work: "Section 179 claimed in the year placed in service: 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line15"
    value: "28954.39"
    work: "28,954.39 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_full"
    value: "28954.39"
    work: "28,954.39 x 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_forty"
    value: "11581.76"
    work: "28,954.39 x 40%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_fullcase"
    value: "28954.39"
    work: "Acquired after January 19, 2025, so 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_2025"
    value: "0.00"
    work: "No special allowance claimed; not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line16"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_allowed"
    value: "0.00"
    work: "Line 16 is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line17"
    value: "16408.51"
    work: "16,408.51 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line18"
    value: "28954.39"
    work: "28,954.39 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].qconv"
    value: "mq3"
    work: "Quarter given is q3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_hy"
    value: "20.00%"
    work: "5-year 200DB half-year convention, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_mq"
    value: "15.00%"
    work: "5-year 200DB mid-quarter, 3rd quarter, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].rate_prior"
    value: "26.00%"
    work: "5-year 200DB mid-quarter, 1st quarter (mq1), year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_hy"
    value: "5790.88"
    work: "28,954.39 x 20%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_mq"
    value: "4343.16"
    work: "28,954.39 x 15%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_prior"
    value: "7528.14"
    work: "28,954.39 x 26%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19"
    value: "7528.14"
    work: "Placed in service before 2025, so the year-2 rate applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_earlier"
    value: "7528.14"
    work: "Within the recovery period"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line19_2025"
    value: "4343.16"
    work: "Mid-quarter convention applies (given test is yes)"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].line20"
    value: "7528.14"
    work: "Lesser of 16,408.51 or 7,528.14"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].b100"
    value: "34939.00"
    work: "34,939 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r1"
    value: "35.00%"
    work: "Mid-quarter, 1st quarter, year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1"
    value: "12228.65"
    work: "34,939 x 35%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t1s"
    value: "12228.65"
    work: "0 + 12,228.65"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r2"
    value: "26.00%"
    work: "Mid-quarter, 1st quarter, year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t2"
    value: "9084.14"
    work: "34,939 x 26%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].l2"
    value: "19800.00"
    work: "2024 vehicle, 2nd year limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].d2"
    value: "9084.14"
    work: "Lesser of 19,800 or 9,084.14"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r3"
    value: "15.60%"
    work: "Mid-quarter, 1st quarter, year 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t3"
    value: "5450.48"
    work: "34,939 x 15.6%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r4"
    value: "11.01%"
    work: "Mid-quarter, 1st quarter, year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t4"
    value: "3846.78"
    work: "34,939 x 11.01%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r5"
    value: "11.01%"
    work: "Mid-quarter, 1st quarter, year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t5"
    value: "3846.78"
    work: "34,939 x 11.01%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].r6"
    value: "1.38%"
    work: "Mid-quarter, 1st quarter, year 6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].t6"
    value: "482.16"
    work: "34,939 x 1.38%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].too_old"
    value: "no"
    work: "Placed in service in 2024"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_v"
    value: "0.00"
    work: "No special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_pass"
    value: "7528.14"
    work: "Worksheet line 20"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_heavy"
    value: "7528.14"
    work: "Line 19 without the limits"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_v"
    value: "7528.14"
    work: "Subject to the passenger automobile limits"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus"
    value: "0.00"
    work: "Standard mileage rate: no depreciation is deducted"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs"
    value: "0.00"
    work: "Standard mileage rate: no depreciation is deducted"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025"
    value: "0.00"
    work: "Standard mileage rate"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4"
    value: "0.00"
    work: "Not an owned vehicle on actual expenses placed in service in 2025"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].bonus_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].macrs_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].s179_2025_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].q4_basis"
    value: "0.00"
    work: "Quarter given is q3, not q4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_q4_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].mq_total_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_1].cost179_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bm_c"
    value: "23484.00"
    work: "Business miles given: 23,484"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cm_c"
    value: "0.00"
    work: "Commuting miles given: 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].om_c"
    value: "1894.00"
    work: "Other miles given: 1,894"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].nonbusiness_c"
    value: "1894.00"
    work: "0 + 1,894"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].total_c"
    value: "25378.00"
    work: "23,484 + 1,894"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].over_half"
    value: "yes"
    work: "23,484 / 25,378 = 92.54%, which is more than 50%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].smr_bad"
    value: "no"
    work: "Filer says the standard mileage rate may be used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].smr_amount"
    value: "16438.80"
    work: "23,484 x 0.70"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9_standard"
    value: "17307.80"
    work: "16,438.80 + 869.00 parking and tolls"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].operating_business"
    value: "8938.13"
    work: "9,659 x 23,484 / 25,378"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9_actual"
    value: "9807.13"
    work: "8,938.13 + 869.00"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9"
    value: "17307.80"
    work: "Standard mileage method chosen"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is_actual_owned"
    value: "no"
    work: "Leased vehicle on the standard mileage rate"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is_actual_leased"
    value: "no"
    work: "Standard mileage method"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lease_business"
    value: "0.00"
    work: "Lease payments are 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20a"
    value: "0.00"
    work: "Standard mileage rate: no deduction for lease payments"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].low_use"
    value: "no"
    work: "Business use is 92.54%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].screened"
    value: "no"
    work: "Filer says none of the exceptions applies"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].year"
    value: "7"
    work: "Placed in service in 2019, so 2025 is year 7"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is2025"
    value: "no"
    work: "Placed in service in 2019"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].is2019"
    value: "yes"
    work: "Placed in service in 2019"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bus_cost"
    value: "70413.13"
    work: "76,092 x 23,484 / 25,378"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_bad"
    value: "no"
    work: "Section 179 election is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_mixed"
    value: "no"
    work: "Filer says the choice is the same for all 5-year property"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].claims_bonus"
    value: "no"
    work: "Special allowance = none"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_first_bonus"
    value: "18100.00"
    work: "Pub 946 table, 2019, 1st year: $18,100"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_first_none"
    value: "10100.00"
    work: "2019 footnote 6: $10,100"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_2025"
    value: "12200.00"
    work: "2025 with no special allowance: $12,200"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].lim_prior"
    value: "5760.00"
    work: "2019, 4th and later years: $5,760"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line7"
    value: "5760.00"
    work: "Year-7 limit for a 2019 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line9w"
    value: "5330.12"
    work: "5,760 x 23,484 / 25,378"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_ok"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line10"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line10_2025"
    value: "0.00"
    work: "Election is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_line10"
    value: "0.00"
    work: "Smaller of 0 or line 9"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line11"
    value: "5330.12"
    work: "5,330.12 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line14"
    value: "0.00"
    work: "Section 179 claimed in the year placed in service: 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line15"
    value: "70413.13"
    work: "70,413.13 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_full"
    value: "70413.13"
    work: "70,413.13 x 100%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_forty"
    value: "28165.25"
    work: "70,413.13 x 40%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_fullcase"
    value: "28165.25"
    work: "Not acquired after January 19, 2025, so 40%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_2025"
    value: "0.00"
    work: "No special allowance claimed; not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line16"
    value: "0.00"
    work: "Not the year placed in service"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_allowed"
    value: "0.00"
    work: "Line 16 is 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line17"
    value: "5330.12"
    work: "5,330.12 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line18"
    value: "70413.13"
    work: "70,413.13 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].qconv"
    value: "mq2"
    work: "Quarter given is q2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19"
    value: "0.00"
    work: "After the recovery period: there is no table rate for year 7"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line19_earlier"
    value: "0.00"
    work: "After the recovery period, the worksheet is not used"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].line20"
    value: "0.00"
    work: "Lesser of 5,330.12 or 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].b100"
    value: "76092.00"
    work: "76,092 - 0"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r1"
    value: "5.00%"
    work: "Mid-quarter, 4th quarter (mq4), year 1"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t1"
    value: "3804.60"
    work: "76,092 x 5%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l1"
    value: "10100.00"
    work: "2019, 1st year, no special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t1s"
    value: "3804.60"
    work: "0 + 3,804.60"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d1"
    value: "3804.60"
    work: "Lesser of 10,100 or 3,804.60"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r2"
    value: "38.00%"
    work: "Mid-quarter, 4th quarter, year 2"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t2"
    value: "28914.96"
    work: "76,092 x 38%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l2"
    value: "16100.00"
    work: "2019, 2nd year limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d2"
    value: "16100.00"
    work: "Lesser of 16,100 or 28,914.96"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r3"
    value: "22.80%"
    work: "Mid-quarter, 4th quarter, year 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t3"
    value: "17348.98"
    work: "76,092 x 22.8%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l3"
    value: "9700.00"
    work: "2019, 3rd year limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d3"
    value: "9700.00"
    work: "Lesser of 9,700 or 17,348.98"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r4"
    value: "13.68%"
    work: "Mid-quarter, 4th quarter, year 4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t4"
    value: "10409.39"
    work: "76,092 x 13.68%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l4"
    value: "5760.00"
    work: "2019, 4th and later years limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d4"
    value: "5760.00"
    work: "Lesser of 5,760 or 10,409.39"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r5"
    value: "10.94%"
    work: "Mid-quarter, 4th quarter, year 5"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t5"
    value: "8324.46"
    work: "76,092 x 10.94%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l5"
    value: "5760.00"
    work: "2019, 4th and later years limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d5"
    value: "5760.00"
    work: "Lesser of 5,760 or 8,324.46"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].r6"
    value: "9.58%"
    work: "Mid-quarter, 4th quarter, year 6"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].t6"
    value: "7289.61"
    work: "76,092 x 9.58%"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].l6"
    value: "5760.00"
    work: "2019, 4th and later years limit"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d6"
    value: "5760.00"
    work: "Lesser of 5,760 or 7,289.61"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].d_total"
    value: "46884.60"
    work: "3,804.60 + 16,100 + 9,700 + 5,760 x 3"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].unrecovered"
    value: "29207.40"
    work: "76,092 - 46,884.60"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].post_amount"
    value: "5760.00"
    work: "Lesser of 5,760 or 29,207.40"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].post"
    value: "5330.12"
    work: "5,760 x 23,484 / 25,378"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].too_old"
    value: "no"
    work: "Placed in service in 2019"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_v"
    value: "0.00"
    work: "No special allowance"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_pass"
    value: "5330.12"
    work: "Deduction after the recovery period"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_heavy"
    value: "0.00"
    work: "No deduction after the recovery period for a vehicle not subject to the limits"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_v"
    value: "5330.12"
    work: "Subject to the passenger automobile limits"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus"
    value: "0.00"
    work: "Standard mileage rate; leased vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs"
    value: "0.00"
    work: "Standard mileage rate; not owned"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025"
    value: "0.00"
    work: "Standard mileage rate"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].bonus_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].macrs_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].s179_2025_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].q4_basis"
    value: "0.00"
    work: "Quarter given is q2, not q4"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_q4_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].mq_total_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179_o"
    value: "0.00"
    work: "Not owned on actual expenses"
  - printed: "person[taxpayer].sc[biz_a].scveh[car_2].cost179_a2"
    value: "0.00"
    work: "Not a 2025 vehicle"
```
```
