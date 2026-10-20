# Class M hand-work — sc

`Schedule C (Form 1040) — Profit or Loss From Business, one per business` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 3 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| i1040sc | 2025 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 | cited pages | dc6f3ee7c7d3e34e515b9af9c411d94e35dcde16f162b9a07f28ac0a90012c4a | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15 | 616b4ac7b587b39aea0d3295151bd50959103a4b1d2de2355886fd2a18d22918 |
| f1040sc | 2025; created 2025-04-03 | 1, 2 | whole document | ff225eb24c4b5c837dad07d20c13abedf26000d03bb1fa6f39978de994d90022 | - | 44d2d9cfa2ff0e47f2ade1dd03e972f7c6cb10c7a4e36d882fa5a6ac2fa55376 |
| p946 | For use in preparing 2025 returns | 17, 18, 19, 34 | cited pages | 18296345e7f2db8e39983267c3e34105e259e807a64a61abe6cdc3790fab64b2 | 17, 18, 19, 34 | da26519fea1cf47d82c185c15ff4f55c7d7749eda83e608cfd4a597cfdb97fc7 |
| f4562 | 2025; created 2025-10-09 | 1, 2, 3 | whole document | 71e2ace527072aaa7293e77897bb4ab8e473fa9c47b6b1ccb977fdc58a93bc2d | - | a1330c49d931e7ecdc867aef2d9e01390fc7b4d7e9321943a21ed0f8e883ed18 |
| i4562 | 2025 | 4, 5, 9, 13, 14, 15 | cited pages | cd46d169c3c1fc12d6f86f25fada33320d63996ab97d142a5202b6ede2c588d2 | 5, 9, 13, 14, 15 | 9466038a0fd7f12850357f7b5b2dd8b3de02e81e83face38fb5bc133ffea15c0 |
| f7206 | 2025; created 2025-10-02 | 1 | whole document | 1f54af11e092a24258ac71f29d2bcfeeda1d6100ca332357d4569eea889e1dbb | - | e3b265efad583dd859c584d4e7e8a17d7b6e927878922ab5f020e2ff79a18d87 |
| i1040gi | 2025; printed date 2026-02-25 | 94, 95, 104, 108 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 95, 104 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| i8995 | 2025; printed date 2026-01-26 | 2, 4, 6 | cited pages | 96284eaad2fe5ec324de9fd4335cea9ea3260e66ff1d8b1725c1cff7fbe1ddc2 | 2, 4, 6 | 6671a64ba0011f89e03eb5985954073dcd984b3f346495182916b0ecaa42ec1a |
| i7206 | 2025 | 1, 2 | whole document | 88aebffe01e22b57dadeb703483459075718cb0b2514fe8f00185975cfbeef3a | 1, 2 | 5bfa308e7e4634d4a0162d76b4af6a4182b8539a390109360875303222231cfe |

## Lines

### case classm.sc.1 — prompt sha256 b43c238eac2a6ab21d3a4fb8d0e9b495ebf58337ef956ae4b19929d2df0ef1c3; branches: sc.statutory:false, sc.passive:true, sc.spouse_owned:false, sc.method_other:false, sc.special:false, sc.screened:false, sc.ho_uses:false, sc.ho_uses:true, sc.ho_other:false, sc.ho_screened:false, sc.ho_over:false, sc.ho_over:true, sc.ho_line4#0, sc.ho_line4#1, sc.ho_unlimited:false, sc.ho_unlimited:true, sc.ho_no179:false, sc.ho_no179:true, sc.ho_limited:left, sc.ho_pre179_floor:floor, sc.ho_pre179_floor:positive, sc.ho_both_limits:false, sc.ho_line5_lim#0, sc.ho_line5_lim#1, sc.ho_line5#0, sc.ho_line5#1, sc.line30#0, sc.line30#1, sc.loss:false, sc.loss:true, sc.at_risk:true, sc.not_at_risk:false, sc.result#0, sc.result#1, sc.inventory_other:false, sc.s179_allowed#0, sc.profit_pos:floor, sc.profit_pos:positive, sc.hi_uses:false, sc.hi_screen:false, sc.hi_screened:false, sc.f7206_has:false, sc.f7206_has:true, sc.f7206_line7#0, sc.f7206_line7#1, sc.f7206_line8:floor, sc.f7206_line8:positive, sc.f7206_line9#0, sc.f7206_line9#1, sc.f7206_line10:floor, sc.f7206_line10:positive, sc.f7206_min:left, sc.f7206_line14#1, sc.qbi_has:false, sc.qbi_has:true, sc.qbi_se#0, sc.qbi_se#1, sc.qbi_plan#0, sc.qbi_plan#1, sc.tips_ot:false

### classm.sc.1 — person[taxpayer].sc[biz_a].screened — Something on this Schedule C is outside this tool
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_a].line3 — Subtract line 2 from line 1
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line4 — Cost of goods sold (from line 42)
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line5 — Gross profit. Subtract line 4 from line 3
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line7 — Gross income. Add lines 5 and 6
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line9 — Car and truck expenses
Status: **AGREE**

Value: $273.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line12 — Depletion
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line13 — Depreciation and section 179 expense deduction (not included in Part III)
Status: **AGREE**

Value: $14,381.65

### classm.sc.1 — person[taxpayer].sc[biz_a].line20a — Rent or lease: vehicles, machinery, and equipment
Status: **AGREE**

Value: $1,503.11

### classm.sc.1 — person[taxpayer].sc[biz_a].meals_50_ded — 50% of the meals subject to the 50% limit
Status: **AGREE**

Value: $7,035.00

### classm.sc.1 — person[taxpayer].sc[biz_a].meals_80_ded — 80% of the meals under the hours of service limits
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line24b — Deductible meals
Status: **AGREE**

Value: $7,035.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line27b — Other expenses (from line 48)
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **AGREE**

Value: $23,192.76

### classm.sc.1 — person[taxpayer].sc[biz_a].line29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **AGREE**

Value: $-23,192.76

### classm.sc.1 — person[taxpayer].sc[biz_a].line28_pre179 — Line 28 without the section 179 expense deduction
Status: **AGREE**

Value: $23,192.76

### classm.sc.1 — person[taxpayer].sc[biz_a].line29_pre179 — Line 29 without the section 179 expense deduction
Status: **AGREE**

Value: $-23,192.76

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_screened — The home office deduction is outside the simplified method this tool covers
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_over — More than 300 square feet
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_line4_actual — Line 2 (the square feet used) times line 3c
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_line4_cap — 300 square feet times line 3c
Status: **AGREE**

Value: $1,500.00

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_line4 — Multiply line 2 by line 3c
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_line1 — Gross income limitation (Schedule C, line 29)
Status: **AGREE**

Value: $-23,192.76

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_room — Line 29 without the section 179 deduction, less the most section 179 deduction t
Status: **AGREE**

Value: $-23,192.76

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_unlimited — Line 4 is not more than the smallest line 29 any section 179 allocation could gi
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_s179_max — The most section 179 deduction this business could take, its 2025 elections plus
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_no179 — No section 179 deduction is possible for this business (no 2025 election and no 
Status: **AGREE**

Value: yes

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_limited — The smaller of line 1 or line 4, with no section 179 election (line 1 is line 29
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_pre179_floor — Line 29 without the section 179 deduction, if zero or less zero
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_both_limits — The gross income limitation could bind together with the section 179 business in
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_both — Line 5 when both income limits could bind
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_line5_lim — Line 5 when line 4 is more than the room left by the section 179 elections
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].ho_line5 — Allowable expenses using the simplified method. Enter the smaller of line 1 or l
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line30 — Expenses for business use of your home
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line31 — Net profit or (loss). Subtract line 30 from line 29
Status: **AGREE**

Value: $-23,192.76

### classm.sc.1 — person[taxpayer].sc[biz_a].line31_pre179 — Line 31 without the section 179 expense deduction
Status: **AGREE**

Value: $-23,192.76

### classm.sc.1 — person[taxpayer].sc[biz_a].loss — Line 31 is a loss
Status: **AGREE**

Value: yes

### classm.sc.1 — person[taxpayer].sc[biz_a].not_at_risk — Some investment is not at risk (box 32b)
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_a].loss_allowed — The loss on line 31 when all investment is at risk
Status: **AGREE**

Value: $-23,192.76

### classm.sc.1 — person[taxpayer].sc[biz_a].result — The amount for Schedule 1, line 3 and Schedule SE, line 2
Status: **AGREE**

Value: $-23,192.76

### classm.sc.1 — person[taxpayer].sc[biz_a].line40 — Add lines 35 through 39
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].line42 — Cost of goods sold. Subtract line 41 from line 40
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f6 — Section 179 elected on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f14 — Special allowance on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f17 — MACRS on earlier property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f19_y3 — MACRS on 2025 property of period y3 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f19_y5 — MACRS on 2025 property of period y5 other than listed property
Status: **AGREE**

Value: $3,151.40

### classm.sc.1 — person[taxpayer].sc[biz_a].f19_y7 — MACRS on 2025 property of period y7 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f19_y10 — MACRS on 2025 property of period y10 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f19_y15 — MACRS on 2025 property of period y15 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f19_y20 — MACRS on 2025 property of period y20 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f19_y15sl — MACRS on 2025 property of period y15sl other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f25_assets — Special allowance on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f25_veh — Special allowance on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f25 — Line 25 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f26_assets — Column (h) of listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f26_veh — Column (h) of vehicles
Status: **AGREE**

Value: $11,230.25

### classm.sc.1 — person[taxpayer].sc[biz_a].f26h — Column (h), line 26, for this business
Status: **AGREE**

Value: $11,230.25

### classm.sc.1 — person[taxpayer].sc[biz_a].f28 — Line 28 for this business
Status: **AGREE**

Value: $11,230.25

### classm.sc.1 — person[taxpayer].sc[biz_a].f29_assets — Section 179 elected on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f29_veh — Section 179 on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f29 — Line 29 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].s179_elected — Section 179 elected for this business's 2025 property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].dep_other — Depreciation other than the section 179 deduction (Form 4562 lines 14, 17, 19 an
Status: **AGREE**

Value: $14,381.65

### classm.sc.1 — person[taxpayer].sc[biz_a].s179_return — The return's section 179 deduction, for its only Schedule C
Status: **DISAGREE**

Project: $10,804.00
Model: $0.00
Work: Return has two Schedules C; not applicable

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the Form 7206 lines for a business without a health plan, the loss lines for a profit, the single-Schedule-C section 179 line on a return with two, the home office line for the limit that does not bind); each is read only in its own case, and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.sc.1 — person[taxpayer].sc[biz_a].s179_allowed — Section 179 expense deduction for this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].mq_q4_a — mq_q4 of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].mq_q4_v — mq_q4 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].mq_q4 — mq_q4 of this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].mq_total_a — mq_total of this business's property
Status: **AGREE**

Value: $15,757.00

### classm.sc.1 — person[taxpayer].sc[biz_a].mq_total_v — mq_total of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].mq_total — mq_total of this business
Status: **AGREE**

Value: $15,757.00

### classm.sc.1 — person[taxpayer].sc[biz_a].cost179_a — cost179 of this business's property
Status: **AGREE**

Value: $15,757.00

### classm.sc.1 — person[taxpayer].sc[biz_a].cost179_v — cost179 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].cost179 — cost179 of this business
Status: **AGREE**

Value: $15,757.00

### classm.sc.1 — person[taxpayer].sc[biz_a].veh_lease — Business part of vehicle lease payments
Status: **AGREE**

Value: $1,503.11

### classm.sc.1 — person[taxpayer].sc[biz_a].profit_pos — Net profit of this business (zero for a loss)
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].hi_screened — This health insurance deduction is outside this tool
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line2 — Qualified long-term care insurance (the smaller of payments or the age limit, fo
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line3 — Add lines 1 and 2
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line4 — Net profit from the trade or business under which the insurance plan is establis
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line5 — Total of all net profits from Schedule C, line 31
Status: **AGREE**

Value: $56,997.40

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_has — Line 4 is more than zero
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line7_pos — Schedule 1, line 15 (this person's), times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line7 — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line8 — Subtract line 7 from line 4
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line9_pos — This person's SEP or SIMPLE deduction times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line9 — Schedule 1, line 16, attributable to the same trade or business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line10 — Subtract line 9 from line 8
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_min — The smaller of line 3 or line 13
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].f7206_line14 — Self-employed health insurance deduction
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].qbi_has — This business has a net profit
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_a].qbi_se_pos — This person's deductible part of self-employment tax attributable to this busine
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].qbi_se — Deductible part of self-employment tax attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].qbi_plan_pos — This person's SEP or SIMPLE deduction attributable to this business (by share of
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].qbi_plan — SEP or SIMPLE deduction attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].qbi_ded — Deductions attributable to this business: self-employment tax, retirement plan a
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_a].qbi — Qualified business income or (loss) of this business
Status: **AGREE**

Value: $-23,192.76

### classm.sc.1 — person[taxpayer].sc[biz_b].screened — Something on this Schedule C is outside this tool
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_b].line3 — Subtract line 2 from line 1
Status: **AGREE**

Value: $146,567.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line4 — Cost of goods sold (from line 42)
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line5 — Gross profit. Subtract line 4 from line 3
Status: **AGREE**

Value: $146,567.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line7 — Gross income. Add lines 5 and 6
Status: **AGREE**

Value: $146,567.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line9 — Car and truck expenses
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line12 — Depletion
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line13 — Depreciation and section 179 expense deduction (not included in Part III)
Status: **AGREE**

Value: $12,659.60

### classm.sc.1 — person[taxpayer].sc[biz_b].line20a — Rent or lease: vehicles, machinery, and equipment
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].meals_50_ded — 50% of the meals subject to the 50% limit
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].meals_80_ded — 80% of the meals under the hours of service limits
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line24b — Deductible meals
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line27b — Other expenses (from line 48)
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **AGREE**

Value: $88,069.60

### classm.sc.1 — person[taxpayer].sc[biz_b].line29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **AGREE**

Value: $58,497.40

### classm.sc.1 — person[taxpayer].sc[biz_b].line28_pre179 — Line 28 without the section 179 expense deduction
Status: **AGREE**

Value: $77,265.60

### classm.sc.1 — person[taxpayer].sc[biz_b].line29_pre179 — Line 29 without the section 179 expense deduction
Status: **AGREE**

Value: $69,301.40

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_screened — The home office deduction is outside the simplified method this tool covers
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_over — More than 300 square feet
Status: **AGREE**

Value: yes

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_line4_actual — Line 2 (the square feet used) times line 3c
Status: **AGREE**

Value: $2,225.00

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_line4_cap — 300 square feet times line 3c
Status: **AGREE**

Value: $1,500.00

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_line4 — Multiply line 2 by line 3c
Status: **AGREE**

Value: $1,500.00

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_line1 — Gross income limitation (Schedule C, line 29)
Status: **AGREE**

Value: $58,497.40

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_room — Line 29 without the section 179 deduction, less the most section 179 deduction t
Status: **AGREE**

Value: $58,497.40

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_unlimited — Line 4 is not more than the smallest line 29 any section 179 allocation could gi
Status: **AGREE**

Value: yes

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_s179_max — The most section 179 deduction this business could take, its 2025 elections plus
Status: **AGREE**

Value: $10,804.00

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_no179 — No section 179 deduction is possible for this business (no 2025 election and no 
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_limited — The smaller of line 1 or line 4, with no section 179 election (line 1 is line 29
Status: **AGREE**

Value: $1,500.00

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_pre179_floor — Line 29 without the section 179 deduction, if zero or less zero
Status: **AGREE**

Value: $69,301.40

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_both_limits — The gross income limitation could bind together with the section 179 business in
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_both — Line 5 when both income limits could bind
Status: **DISAGREE**

Project: $0.00
Model: $1,500.00
Work: Smaller of line 1 or line 4

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the Form 7206 lines for a business without a health plan, the loss lines for a profit, the single-Schedule-C section 179 line on a return with two, the home office line for the limit that does not bind); each is read only in its own case, and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_line5_lim — Line 5 when line 4 is more than the room left by the section 179 elections
Status: **DISAGREE**

Project: $0.00
Model: $1,500.00
Work: Smaller of room 58,497.40 or 1,500

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the Form 7206 lines for a business without a health plan, the loss lines for a profit, the single-Schedule-C section 179 line on a return with two, the home office line for the limit that does not bind); each is read only in its own case, and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.sc.1 — person[taxpayer].sc[biz_b].ho_line5 — Allowable expenses using the simplified method. Enter the smaller of line 1 or l
Status: **AGREE**

Value: $1,500.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line30 — Expenses for business use of your home
Status: **AGREE**

Value: $1,500.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line31 — Net profit or (loss). Subtract line 30 from line 29
Status: **AGREE**

Value: $56,997.40

### classm.sc.1 — person[taxpayer].sc[biz_b].line31_pre179 — Line 31 without the section 179 expense deduction
Status: **AGREE**

Value: $67,801.40

### classm.sc.1 — person[taxpayer].sc[biz_b].loss — Line 31 is a loss
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_b].not_at_risk — Some investment is not at risk (box 32b)
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_b].loss_allowed — The loss on line 31 when all investment is at risk
Status: **DISAGREE**

Project: $56,997.40
Model: $0.00
Work: No loss

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the Form 7206 lines for a business without a health plan, the loss lines for a profit, the single-Schedule-C section 179 line on a return with two, the home office line for the limit that does not bind); each is read only in its own case, and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.sc.1 — person[taxpayer].sc[biz_b].result — The amount for Schedule 1, line 3 and Schedule SE, line 2
Status: **AGREE**

Value: $56,997.40

### classm.sc.1 — person[taxpayer].sc[biz_b].line40 — Add lines 35 through 39
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].line42 — Cost of goods sold. Subtract line 41 from line 40
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f6 — Section 179 elected on property other than listed property
Status: **AGREE**

Value: $10,804.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f14 — Special allowance on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f17 — MACRS on earlier property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f19_y3 — MACRS on 2025 property of period y3 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f19_y5 — MACRS on 2025 property of period y5 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f19_y7 — MACRS on 2025 property of period y7 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f19_y10 — MACRS on 2025 property of period y10 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f19_y15 — MACRS on 2025 property of period y15 other than listed property
Status: **AGREE**

Value: $1,855.60

### classm.sc.1 — person[taxpayer].sc[biz_b].f19_y20 — MACRS on 2025 property of period y20 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f19_y15sl — MACRS on 2025 property of period y15sl other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f25_assets — Special allowance on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f25_veh — Special allowance on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f25 — Line 25 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f26_assets — Column (h) of listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f26_veh — Column (h) of vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f26h — Column (h), line 26, for this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f28 — Line 28 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f29_assets — Section 179 elected on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f29_veh — Section 179 on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f29 — Line 29 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].s179_elected — Section 179 elected for this business's 2025 property
Status: **AGREE**

Value: $10,804.00

### classm.sc.1 — person[taxpayer].sc[biz_b].dep_other — Depreciation other than the section 179 deduction (Form 4562 lines 14, 17, 19 an
Status: **AGREE**

Value: $1,855.60

### classm.sc.1 — person[taxpayer].sc[biz_b].s179_return — The return's section 179 deduction, for its only Schedule C
Status: **DISAGREE**

Project: $10,804.00
Model: $0.00
Work: Return has two Schedules C; not applicable

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the Form 7206 lines for a business without a health plan, the loss lines for a profit, the single-Schedule-C section 179 line on a return with two, the home office line for the limit that does not bind); each is read only in its own case, and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.sc.1 — person[taxpayer].sc[biz_b].s179_allowed — Section 179 expense deduction for this business
Status: **AGREE**

Value: $10,804.00

### classm.sc.1 — person[taxpayer].sc[biz_b].mq_q4_a — mq_q4 of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].mq_q4_v — mq_q4 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].mq_q4 — mq_q4 of this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].mq_total_a — mq_total of this business's property
Status: **AGREE**

Value: $37,112.00

### classm.sc.1 — person[taxpayer].sc[biz_b].mq_total_v — mq_total of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].mq_total — mq_total of this business
Status: **AGREE**

Value: $37,112.00

### classm.sc.1 — person[taxpayer].sc[biz_b].cost179_a — cost179 of this business's property
Status: **AGREE**

Value: $47,916.00

### classm.sc.1 — person[taxpayer].sc[biz_b].cost179_v — cost179 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].cost179 — cost179 of this business
Status: **AGREE**

Value: $47,916.00

### classm.sc.1 — person[taxpayer].sc[biz_b].veh_lease — Business part of vehicle lease payments
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].profit_pos — Net profit of this business (zero for a loss)
Status: **AGREE**

Value: $56,997.40

### classm.sc.1 — person[taxpayer].sc[biz_b].hi_screened — This health insurance deduction is outside this tool
Status: **AGREE**

Value: no

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line2 — Qualified long-term care insurance (the smaller of payments or the age limit, fo
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line3 — Add lines 1 and 2
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line4 — Net profit from the trade or business under which the insurance plan is establis
Status: **DISAGREE**

Project: $56,997.40
Model: $0.00
Work: No plan established under this business

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the Form 7206 lines for a business without a health plan, the loss lines for a profit, the single-Schedule-C section 179 line on a return with two, the home office line for the limit that does not bind); each is read only in its own case, and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line5 — Total of all net profits from Schedule C, line 31
Status: **AGREE**

Value: $56,997.40

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_has — Line 4 is more than zero
Status: **DISAGREE**

Project: yes
Model: no
Work: Line 4 is 0

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the Form 7206 lines for a business without a health plan, the loss lines for a profit, the single-Schedule-C section 179 line on a return with two, the home office line for the limit that does not bind); each is read only in its own case, and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line7_pos — Schedule 1, line 15 (this person's), times line 4 divided by line 5
Status: **DISAGREE**

Project: $2,388.23
Model: $0.00
Work: Line 4 is 0

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the Form 7206 lines for a business without a health plan, the loss lines for a profit, the single-Schedule-C section 179 line on a return with two, the home office line for the limit that does not bind); each is read only in its own case, and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line7 — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax
Status: **DISAGREE**

Project: $2,388.23
Model: $0.00
Work: Line 4 is 0

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the Form 7206 lines for a business without a health plan, the loss lines for a profit, the single-Schedule-C section 179 line on a return with two, the home office line for the limit that does not bind); each is read only in its own case, and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line8 — Subtract line 7 from line 4
Status: **DISAGREE**

Project: $54,609.17
Model: $0.00
Work: 0 - 0

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the Form 7206 lines for a business without a health plan, the loss lines for a profit, the single-Schedule-C section 179 line on a return with two, the home office line for the limit that does not bind); each is read only in its own case, and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line9_pos — This person's SEP or SIMPLE deduction times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line9 — Schedule 1, line 16, attributable to the same trade or business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line10 — Subtract line 9 from line 8
Status: **DISAGREE**

Project: $54,609.17
Model: $0.00
Work: 0 - 0

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the Form 7206 lines for a business without a health plan, the loss lines for a profit, the single-Schedule-C section 179 line on a return with two, the home office line for the limit that does not bind); each is read only in its own case, and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line13 — Subtract line 12 from line 10
Status: **DISAGREE**

Project: $54,609.17
Model: $0.00
Work: 0 - 0

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the Form 7206 lines for a business without a health plan, the loss lines for a profit, the single-Schedule-C section 179 line on a return with two, the home office line for the limit that does not bind); each is read only in its own case, and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_min — The smaller of line 3 or line 13
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].f7206_line14 — Self-employed health insurance deduction
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].qbi_has — This business has a net profit
Status: **AGREE**

Value: yes

### classm.sc.1 — person[taxpayer].sc[biz_b].qbi_se_pos — This person's deductible part of self-employment tax attributable to this busine
Status: **DISAGREE**

Project: $2,388.23
Model: $2,388.22
Work: SE: 33,804.64 x .9235 = 31,218.59 x .153 / 2 = 2,388.22; x 56,997.40/56,997.40

Ruling: model arithmetic; project retained. The model multiplied net earnings by 15.3% at once; Schedule SE figures line 10 (12.4%) and line 11 (2.9%) separately, each rounded to the cent, and line 13 is half their sum (f1040sse lines 10 to 13), which gives the project's amount one cent higher. Not evidence. [dropped]

### classm.sc.1 — person[taxpayer].sc[biz_b].qbi_se — Deductible part of self-employment tax attributable to this business
Status: **DISAGREE**

Project: $2,388.23
Model: $2,388.22
Work: Positive share

Ruling: model arithmetic; project retained. The model multiplied net earnings by 15.3% at once; Schedule SE figures line 10 (12.4%) and line 11 (2.9%) separately, each rounded to the cent, and line 13 is half their sum (f1040sse lines 10 to 13), which gives the project's amount one cent higher. Not evidence. [dropped]

### classm.sc.1 — person[taxpayer].sc[biz_b].qbi_plan_pos — This person's SEP or SIMPLE deduction attributable to this business (by share of
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].qbi_plan — SEP or SIMPLE deduction attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.1 — person[taxpayer].sc[biz_b].qbi_ded — Deductions attributable to this business: self-employment tax, retirement plan a
Status: **DISAGREE**

Project: $2,388.23
Model: $2,388.22
Work: 2,388.22 + 0 + 0

Ruling: model arithmetic; project retained. The model multiplied net earnings by 15.3% at once; Schedule SE figures line 10 (12.4%) and line 11 (2.9%) separately, each rounded to the cent, and line 13 is half their sum (f1040sse lines 10 to 13), which gives the project's amount one cent higher. Not evidence. [dropped]

### classm.sc.1 — person[taxpayer].sc[biz_b].qbi — Qualified business income or (loss) of this business
Status: **DISAGREE**

Project: $54,609.17
Model: $54,609.18
Work: 56,997.40 - 2,388.22

Ruling: model arithmetic; project retained. The model multiplied net earnings by 15.3% at once; Schedule SE figures line 10 (12.4%) and line 11 (2.9%) separately, each rounded to the cent, and line 13 is half their sum (f1040sse lines 10 to 13), which gives the project's amount one cent higher. Not evidence. [dropped]

### case classm.sc.2 — prompt sha256 38b3b4fea292ad88b497be575316dfebec1102b2292c55d1dfcb8edd0486ae65; branches: sc.statutory:false, sc.passive:true, sc.spouse_owned:false, sc.method_other:false, sc.special:false, sc.screened:false, sc.ho_uses:false, sc.ho_uses:true, sc.ho_other:false, sc.ho_screened:false, sc.ho_over:false, sc.ho_line4#0, sc.ho_unlimited:false, sc.ho_unlimited:true, sc.ho_no179:true, sc.ho_limited:left, sc.ho_limited:right, sc.ho_pre179_floor:floor, sc.ho_pre179_floor:positive, sc.ho_both_limits:false, sc.ho_line5_lim#0, sc.ho_line5#0, sc.ho_line5#1, sc.line30#0, sc.line30#1, sc.loss:false, sc.loss:true, sc.at_risk:true, sc.not_at_risk:false, sc.result#0, sc.result#1, sc.inventory_other:false, sc.s179_allowed#0, sc.profit_pos:floor, sc.profit_pos:positive, sc.hi_uses:false, sc.hi_uses:true, sc.hi_screen:false, sc.hi_screened:false, sc.f7206_has:false, sc.f7206_has:true, sc.f7206_line7#0, sc.f7206_line7#1, sc.f7206_line8:floor, sc.f7206_line8:positive, sc.f7206_line9#0, sc.f7206_line9#1, sc.f7206_line10:floor, sc.f7206_line10:positive, sc.f7206_min:left, sc.f7206_line14#0, sc.f7206_line14#1, sc.qbi_has:false, sc.qbi_has:true, sc.qbi_se#0, sc.qbi_se#1, sc.qbi_plan#0, sc.qbi_plan#1, sc.tips_ot:false

### classm.sc.2 — person[taxpayer].sc[biz_a].screened — Something on this Schedule C is outside this tool
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_a].line3 — Subtract line 2 from line 1
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line4 — Cost of goods sold (from line 42)
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line5 — Gross profit. Subtract line 4 from line 3
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line7 — Gross income. Add lines 5 and 6
Status: **AGREE**

Value: $1,387.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line9 — Car and truck expenses
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line12 — Depletion
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line13 — Depreciation and section 179 expense deduction (not included in Part III)
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line20a — Rent or lease: vehicles, machinery, and equipment
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].meals_50_ded — 50% of the meals subject to the 50% limit
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].meals_80_ded — 80% of the meals under the hours of service limits
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line24b — Deductible meals
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line27b — Other expenses (from line 48)
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **AGREE**

Value: $39,721.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **AGREE**

Value: $-38,334.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line28_pre179 — Line 28 without the section 179 expense deduction
Status: **AGREE**

Value: $39,721.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line29_pre179 — Line 29 without the section 179 expense deduction
Status: **AGREE**

Value: $-38,334.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_screened — The home office deduction is outside the simplified method this tool covers
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_over — More than 300 square feet
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_line4_actual — Line 2 (the square feet used) times line 3c
Status: **AGREE**

Value: $685.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_line4_cap — 300 square feet times line 3c
Status: **AGREE**

Value: $1,500.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_line4 — Multiply line 2 by line 3c
Status: **AGREE**

Value: $685.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_line1 — Gross income limitation (Schedule C, line 29)
Status: **AGREE**

Value: $-38,334.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_room — Line 29 without the section 179 deduction, less the most section 179 deduction t
Status: **AGREE**

Value: $-38,334.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_unlimited — Line 4 is not more than the smallest line 29 any section 179 allocation could gi
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_s179_max — The most section 179 deduction this business could take, its 2025 elections plus
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_no179 — No section 179 deduction is possible for this business (no 2025 election and no 
Status: **AGREE**

Value: yes

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_limited — The smaller of line 1 or line 4, with no section 179 election (line 1 is line 29
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_pre179_floor — Line 29 without the section 179 deduction, if zero or less zero
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_both_limits — The gross income limitation could bind together with the section 179 business in
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_both — Line 5 when both income limits could bind
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_line5_lim — Line 5 when line 4 is more than the room left by the section 179 elections
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].ho_line5 — Allowable expenses using the simplified method. Enter the smaller of line 1 or l
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line30 — Expenses for business use of your home
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line31 — Net profit or (loss). Subtract line 30 from line 29
Status: **AGREE**

Value: $-38,334.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line31_pre179 — Line 31 without the section 179 expense deduction
Status: **AGREE**

Value: $-38,334.00

### classm.sc.2 — person[taxpayer].sc[biz_a].loss — Line 31 is a loss
Status: **AGREE**

Value: yes

### classm.sc.2 — person[taxpayer].sc[biz_a].not_at_risk — Some investment is not at risk (box 32b)
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_a].loss_allowed — The loss on line 31 when all investment is at risk
Status: **AGREE**

Value: $-38,334.00

### classm.sc.2 — person[taxpayer].sc[biz_a].result — The amount for Schedule 1, line 3 and Schedule SE, line 2
Status: **AGREE**

Value: $-38,334.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line40 — Add lines 35 through 39
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].line42 — Cost of goods sold. Subtract line 41 from line 40
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f6 — Section 179 elected on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f14 — Special allowance on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f17 — MACRS on earlier property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f19_y3 — MACRS on 2025 property of period y3 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f19_y5 — MACRS on 2025 property of period y5 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f19_y7 — MACRS on 2025 property of period y7 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f19_y10 — MACRS on 2025 property of period y10 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f19_y15 — MACRS on 2025 property of period y15 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f19_y20 — MACRS on 2025 property of period y20 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f19_y15sl — MACRS on 2025 property of period y15sl other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f25_assets — Special allowance on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f25_veh — Special allowance on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f25 — Line 25 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f26_assets — Column (h) of listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f26_veh — Column (h) of vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f26h — Column (h), line 26, for this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f28 — Line 28 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f29_assets — Section 179 elected on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f29_veh — Section 179 on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f29 — Line 29 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].s179_elected — Section 179 elected for this business's 2025 property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].dep_other — Depreciation other than the section 179 deduction (Form 4562 lines 14, 17, 19 an
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].s179_return — The return's section 179 deduction, for its only Schedule C
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].s179_allowed — Section 179 expense deduction for this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].mq_q4_a — mq_q4 of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].mq_q4_v — mq_q4 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].mq_q4 — mq_q4 of this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].mq_total_a — mq_total of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].mq_total_v — mq_total of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].mq_total — mq_total of this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].cost179_a — cost179 of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].cost179_v — cost179 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].cost179 — cost179 of this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].veh_lease — Business part of vehicle lease payments
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].profit_pos — Net profit of this business (zero for a loss)
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].hi_screened — This health insurance deduction is outside this tool
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line2 — Qualified long-term care insurance (the smaller of payments or the age limit, fo
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line3 — Add lines 1 and 2
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line4 — Net profit from the trade or business under which the insurance plan is establis
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line5 — Total of all net profits from Schedule C, line 31
Status: **AGREE**

Value: $24,376.22

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_has — Line 4 is more than zero
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line7_pos — Schedule 1, line 15 (this person's), times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line7 — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line8 — Subtract line 7 from line 4
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line9_pos — This person's SEP or SIMPLE deduction times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line9 — Schedule 1, line 16, attributable to the same trade or business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line10 — Subtract line 9 from line 8
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_min — The smaller of line 3 or line 13
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].f7206_line14 — Self-employed health insurance deduction
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].qbi_has — This business has a net profit
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_a].qbi_se_pos — This person's deductible part of self-employment tax attributable to this busine
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].qbi_se — Deductible part of self-employment tax attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].qbi_plan_pos — This person's SEP or SIMPLE deduction attributable to this business (by share of
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].qbi_plan — SEP or SIMPLE deduction attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].qbi_ded — Deductions attributable to this business: self-employment tax, retirement plan a
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_a].qbi — Qualified business income or (loss) of this business
Status: **AGREE**

Value: $-38,334.00

### classm.sc.2 — person[taxpayer].sc[biz_b].screened — Something on this Schedule C is outside this tool
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_b].line3 — Subtract line 2 from line 1
Status: **AGREE**

Value: $119,082.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line4 — Cost of goods sold (from line 42)
Status: **AGREE**

Value: $22,066.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line5 — Gross profit. Subtract line 4 from line 3
Status: **AGREE**

Value: $97,016.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line7 — Gross income. Add lines 5 and 6
Status: **AGREE**

Value: $97,016.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line9 — Car and truck expenses
Status: **AGREE**

Value: $15,768.40

### classm.sc.2 — person[taxpayer].sc[biz_b].line12 — Depletion
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line13 — Depreciation and section 179 expense deduction (not included in Part III)
Status: **AGREE**

Value: $476.38

### classm.sc.2 — person[taxpayer].sc[biz_b].line20a — Rent or lease: vehicles, machinery, and equipment
Status: **AGREE**

Value: $13,213.00

### classm.sc.2 — person[taxpayer].sc[biz_b].meals_50_ded — 50% of the meals subject to the 50% limit
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].meals_80_ded — 80% of the meals under the hours of service limits
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line24b — Deductible meals
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line27b — Other expenses (from line 48)
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **AGREE**

Value: $72,639.78

### classm.sc.2 — person[taxpayer].sc[biz_b].line29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **AGREE**

Value: $24,376.22

### classm.sc.2 — person[taxpayer].sc[biz_b].line28_pre179 — Line 28 without the section 179 expense deduction
Status: **AGREE**

Value: $72,639.78

### classm.sc.2 — person[taxpayer].sc[biz_b].line29_pre179 — Line 29 without the section 179 expense deduction
Status: **AGREE**

Value: $24,376.22

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_screened — The home office deduction is outside the simplified method this tool covers
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_over — More than 300 square feet
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_line4_actual — Line 2 (the square feet used) times line 3c
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_line4_cap — 300 square feet times line 3c
Status: **AGREE**

Value: $1,500.00

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_line4 — Multiply line 2 by line 3c
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_line1 — Gross income limitation (Schedule C, line 29)
Status: **AGREE**

Value: $24,376.22

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_room — Line 29 without the section 179 deduction, less the most section 179 deduction t
Status: **AGREE**

Value: $24,376.22

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_unlimited — Line 4 is not more than the smallest line 29 any section 179 allocation could gi
Status: **AGREE**

Value: yes

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_s179_max — The most section 179 deduction this business could take, its 2025 elections plus
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_no179 — No section 179 deduction is possible for this business (no 2025 election and no 
Status: **AGREE**

Value: yes

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_limited — The smaller of line 1 or line 4, with no section 179 election (line 1 is line 29
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_pre179_floor — Line 29 without the section 179 deduction, if zero or less zero
Status: **AGREE**

Value: $24,376.22

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_both_limits — The gross income limitation could bind together with the section 179 business in
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_both — Line 5 when both income limits could bind
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_line5_lim — Line 5 when line 4 is more than the room left by the section 179 elections
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].ho_line5 — Allowable expenses using the simplified method. Enter the smaller of line 1 or l
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line30 — Expenses for business use of your home
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line31 — Net profit or (loss). Subtract line 30 from line 29
Status: **AGREE**

Value: $24,376.22

### classm.sc.2 — person[taxpayer].sc[biz_b].line31_pre179 — Line 31 without the section 179 expense deduction
Status: **AGREE**

Value: $24,376.22

### classm.sc.2 — person[taxpayer].sc[biz_b].loss — Line 31 is a loss
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_b].not_at_risk — Some investment is not at risk (box 32b)
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_b].loss_allowed — The loss on line 31 when all investment is at risk
Status: **DISAGREE**

Project: $24,376.22
Model: $0.00
Work: No loss

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the Form 7206 lines for a business without a health plan, the loss lines for a profit, the single-Schedule-C section 179 line on a return with two, the home office line for the limit that does not bind); each is read only in its own case, and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.sc.2 — person[taxpayer].sc[biz_b].result — The amount for Schedule 1, line 3 and Schedule SE, line 2
Status: **AGREE**

Value: $24,376.22

### classm.sc.2 — person[taxpayer].sc[biz_b].line40 — Add lines 35 through 39
Status: **AGREE**

Value: $24,744.00

### classm.sc.2 — person[taxpayer].sc[biz_b].line42 — Cost of goods sold. Subtract line 41 from line 40
Status: **AGREE**

Value: $22,066.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f6 — Section 179 elected on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f14 — Special allowance on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f17 — MACRS on earlier property other than listed property
Status: **AGREE**

Value: $476.38

### classm.sc.2 — person[taxpayer].sc[biz_b].f19_y3 — MACRS on 2025 property of period y3 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f19_y5 — MACRS on 2025 property of period y5 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f19_y7 — MACRS on 2025 property of period y7 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f19_y10 — MACRS on 2025 property of period y10 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f19_y15 — MACRS on 2025 property of period y15 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f19_y20 — MACRS on 2025 property of period y20 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f19_y15sl — MACRS on 2025 property of period y15sl other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f25_assets — Special allowance on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f25_veh — Special allowance on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f25 — Line 25 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f26_assets — Column (h) of listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f26_veh — Column (h) of vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f26h — Column (h), line 26, for this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f28 — Line 28 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f29_assets — Section 179 elected on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f29_veh — Section 179 on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f29 — Line 29 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].s179_elected — Section 179 elected for this business's 2025 property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].dep_other — Depreciation other than the section 179 deduction (Form 4562 lines 14, 17, 19 an
Status: **AGREE**

Value: $476.38

### classm.sc.2 — person[taxpayer].sc[biz_b].s179_return — The return's section 179 deduction, for its only Schedule C
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].s179_allowed — Section 179 expense deduction for this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].mq_q4_a — mq_q4 of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].mq_q4_v — mq_q4 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].mq_q4 — mq_q4 of this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].mq_total_a — mq_total of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].mq_total_v — mq_total of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].mq_total — mq_total of this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].cost179_a — cost179 of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].cost179_v — cost179 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].cost179 — cost179 of this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].veh_lease — Business part of vehicle lease payments
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].profit_pos — Net profit of this business (zero for a loss)
Status: **AGREE**

Value: $24,376.22

### classm.sc.2 — person[taxpayer].sc[biz_b].hi_screened — This health insurance deduction is outside this tool
Status: **AGREE**

Value: no

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line2 — Qualified long-term care insurance (the smaller of payments or the age limit, fo
Status: **AGREE**

Value: $480.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line3 — Add lines 1 and 2
Status: **AGREE**

Value: $1,837.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line4 — Net profit from the trade or business under which the insurance plan is establis
Status: **AGREE**

Value: $24,376.22

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line5 — Total of all net profits from Schedule C, line 31
Status: **AGREE**

Value: $24,376.22

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_has — Line 4 is more than zero
Status: **AGREE**

Value: yes

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line7_pos — Schedule 1, line 15 (this person's), times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line7 — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line8 — Subtract line 7 from line 4
Status: **AGREE**

Value: $24,376.22

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line9_pos — This person's SEP or SIMPLE deduction times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line9 — Schedule 1, line 16, attributable to the same trade or business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line10 — Subtract line 9 from line 8
Status: **AGREE**

Value: $24,376.22

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $24,376.22

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_min — The smaller of line 3 or line 13
Status: **AGREE**

Value: $1,837.00

### classm.sc.2 — person[taxpayer].sc[biz_b].f7206_line14 — Self-employed health insurance deduction
Status: **AGREE**

Value: $1,837.00

### classm.sc.2 — person[taxpayer].sc[biz_b].qbi_has — This business has a net profit
Status: **AGREE**

Value: yes

### classm.sc.2 — person[taxpayer].sc[biz_b].qbi_se_pos — This person's deductible part of self-employment tax attributable to this busine
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].qbi_se — Deductible part of self-employment tax attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].qbi_plan_pos — This person's SEP or SIMPLE deduction attributable to this business (by share of
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].qbi_plan — SEP or SIMPLE deduction attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.2 — person[taxpayer].sc[biz_b].qbi_ded — Deductions attributable to this business: self-employment tax, retirement plan a
Status: **AGREE**

Value: $1,837.00

### classm.sc.2 — person[taxpayer].sc[biz_b].qbi — Qualified business income or (loss) of this business
Status: **AGREE**

Value: $22,539.22

### case classm.sc.3 — prompt sha256 b3c1db87ceda7f654d50d4e14a5ce7dcc21c8dff5ccdadfb37243b08dbcdfbc3; branches: sc.statutory:false, sc.passive:true, sc.spouse_owned:false, sc.method_other:false, sc.special:false, sc.screened:false, sc.ho_uses:false, sc.ho_other:false, sc.ho_screened:false, sc.ho_over:false, sc.ho_line4#0, sc.ho_unlimited:false, sc.ho_unlimited:true, sc.ho_no179:true, sc.ho_limited:left, sc.ho_pre179_floor:floor, sc.ho_pre179_floor:positive, sc.ho_both_limits:false, sc.ho_line5_lim#0, sc.ho_line5#0, sc.ho_line5#1, sc.line30#1, sc.loss:false, sc.loss:true, sc.at_risk:true, sc.not_at_risk:false, sc.result#0, sc.result#1, sc.inventory_other:false, sc.s179_allowed#0, sc.profit_pos:floor, sc.profit_pos:positive, sc.hi_uses:false, sc.hi_uses:true, sc.hi_screen:false, sc.hi_screened:false, sc.f7206_has:false, sc.f7206_has:true, sc.f7206_line7#0, sc.f7206_line7#1, sc.f7206_line8:floor, sc.f7206_line8:positive, sc.f7206_line9#0, sc.f7206_line9#1, sc.f7206_line10:floor, sc.f7206_line10:positive, sc.f7206_min:left, sc.f7206_min:right, sc.f7206_line14#0, sc.f7206_line14#1, sc.qbi_has:false, sc.qbi_has:true, sc.qbi_se#0, sc.qbi_se#1, sc.qbi_plan#0, sc.qbi_plan#1, sc.tips_ot:false

### classm.sc.3 — person[taxpayer].sc[biz_a].screened — Something on this Schedule C is outside this tool
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_a].line3 — Subtract line 2 from line 1
Status: **AGREE**

Value: $88,883.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line4 — Cost of goods sold (from line 42)
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line5 — Gross profit. Subtract line 4 from line 3
Status: **AGREE**

Value: $88,883.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line7 — Gross income. Add lines 5 and 6
Status: **AGREE**

Value: $88,883.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line9 — Car and truck expenses
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line12 — Depletion
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line13 — Depreciation and section 179 expense deduction (not included in Part III)
Status: **AGREE**

Value: $815.78

### classm.sc.3 — person[taxpayer].sc[biz_a].line20a — Rent or lease: vehicles, machinery, and equipment
Status: **AGREE**

Value: $30,000.00

### classm.sc.3 — person[taxpayer].sc[biz_a].meals_50_ded — 50% of the meals subject to the 50% limit
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].meals_80_ded — 80% of the meals under the hours of service limits
Status: **AGREE**

Value: $16,508.80

### classm.sc.3 — person[taxpayer].sc[biz_a].line24b — Deductible meals
Status: **AGREE**

Value: $16,508.80

### classm.sc.3 — person[taxpayer].sc[biz_a].line27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line27b — Other expenses (from line 48)
Status: **AGREE**

Value: $9,283.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **AGREE**

Value: $88,651.58

### classm.sc.3 — person[taxpayer].sc[biz_a].line29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **AGREE**

Value: $231.42

### classm.sc.3 — person[taxpayer].sc[biz_a].line28_pre179 — Line 28 without the section 179 expense deduction
Status: **AGREE**

Value: $88,651.58

### classm.sc.3 — person[taxpayer].sc[biz_a].line29_pre179 — Line 29 without the section 179 expense deduction
Status: **AGREE**

Value: $231.42

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_screened — The home office deduction is outside the simplified method this tool covers
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_over — More than 300 square feet
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_line4_actual — Line 2 (the square feet used) times line 3c
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_line4_cap — 300 square feet times line 3c
Status: **AGREE**

Value: $1,500.00

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_line4 — Multiply line 2 by line 3c
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_line1 — Gross income limitation (Schedule C, line 29)
Status: **AGREE**

Value: $231.42

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_room — Line 29 without the section 179 deduction, less the most section 179 deduction t
Status: **AGREE**

Value: $231.42

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_unlimited — Line 4 is not more than the smallest line 29 any section 179 allocation could gi
Status: **AGREE**

Value: yes

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_s179_max — The most section 179 deduction this business could take, its 2025 elections plus
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_no179 — No section 179 deduction is possible for this business (no 2025 election and no 
Status: **AGREE**

Value: yes

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_limited — The smaller of line 1 or line 4, with no section 179 election (line 1 is line 29
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_pre179_floor — Line 29 without the section 179 deduction, if zero or less zero
Status: **AGREE**

Value: $231.42

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_both_limits — The gross income limitation could bind together with the section 179 business in
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_both — Line 5 when both income limits could bind
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_line5_lim — Line 5 when line 4 is more than the room left by the section 179 elections
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].ho_line5 — Allowable expenses using the simplified method. Enter the smaller of line 1 or l
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line30 — Expenses for business use of your home
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line31 — Net profit or (loss). Subtract line 30 from line 29
Status: **AGREE**

Value: $231.42

### classm.sc.3 — person[taxpayer].sc[biz_a].line31_pre179 — Line 31 without the section 179 expense deduction
Status: **AGREE**

Value: $231.42

### classm.sc.3 — person[taxpayer].sc[biz_a].loss — Line 31 is a loss
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_a].not_at_risk — Some investment is not at risk (box 32b)
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_a].loss_allowed — The loss on line 31 when all investment is at risk
Status: **DISAGREE**

Project: $231.42
Model: $0.00
Work: No loss

Ruling: helper of a branch this entry does not take; project retained. The project figures every line of every entry (the Form 7206 lines for a business without a health plan, the loss lines for a profit, the single-Schedule-C section 179 line on a return with two, the home office line for the limit that does not bind); each is read only in its own case, and the printed lines of the entry that the case uses agree. The model entered zero or worked it as if it applied. Not evidence. [dropped]

### classm.sc.3 — person[taxpayer].sc[biz_a].result — The amount for Schedule 1, line 3 and Schedule SE, line 2
Status: **AGREE**

Value: $231.42

### classm.sc.3 — person[taxpayer].sc[biz_a].line40 — Add lines 35 through 39
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].line42 — Cost of goods sold. Subtract line 41 from line 40
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f6 — Section 179 elected on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f14 — Special allowance on property other than listed property
Status: **AGREE**

Value: $671.78

### classm.sc.3 — person[taxpayer].sc[biz_a].f17 — MACRS on earlier property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f19_y3 — MACRS on 2025 property of period y3 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f19_y5 — MACRS on 2025 property of period y5 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f19_y7 — MACRS on 2025 property of period y7 other than listed property
Status: **AGREE**

Value: $144.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f19_y10 — MACRS on 2025 property of period y10 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f19_y15 — MACRS on 2025 property of period y15 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f19_y20 — MACRS on 2025 property of period y20 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f19_y15sl — MACRS on 2025 property of period y15sl other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f25_assets — Special allowance on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f25_veh — Special allowance on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f25 — Line 25 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f26_assets — Column (h) of listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f26_veh — Column (h) of vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f26h — Column (h), line 26, for this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f28 — Line 28 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f29_assets — Section 179 elected on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f29_veh — Section 179 on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f29 — Line 29 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].s179_elected — Section 179 elected for this business's 2025 property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].dep_other — Depreciation other than the section 179 deduction (Form 4562 lines 14, 17, 19 an
Status: **AGREE**

Value: $815.78

### classm.sc.3 — person[taxpayer].sc[biz_a].s179_return — The return's section 179 deduction, for its only Schedule C
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].s179_allowed — Section 179 expense deduction for this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].mq_q4_a — mq_q4 of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].mq_q4_v — mq_q4 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].mq_q4 — mq_q4 of this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].mq_total_a — mq_total of this business's property
Status: **AGREE**

Value: $1,679.46

### classm.sc.3 — person[taxpayer].sc[biz_a].mq_total_v — mq_total of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].mq_total — mq_total of this business
Status: **AGREE**

Value: $1,679.46

### classm.sc.3 — person[taxpayer].sc[biz_a].cost179_a — cost179 of this business's property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].cost179_v — cost179 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].cost179 — cost179 of this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].veh_lease — Business part of vehicle lease payments
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].profit_pos — Net profit of this business (zero for a loss)
Status: **AGREE**

Value: $231.42

### classm.sc.3 — person[taxpayer].sc[biz_a].hi_screened — This health insurance deduction is outside this tool
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line2 — Qualified long-term care insurance (the smaller of payments or the age limit, fo
Status: **AGREE**

Value: $3,996.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line3 — Add lines 1 and 2
Status: **AGREE**

Value: $3,996.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line4 — Net profit from the trade or business under which the insurance plan is establis
Status: **AGREE**

Value: $231.42

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line5 — Total of all net profits from Schedule C, line 31
Status: **AGREE**

Value: $231.42

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_has — Line 4 is more than zero
Status: **AGREE**

Value: yes

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line7_pos — Schedule 1, line 15 (this person's), times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line7 — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line8 — Subtract line 7 from line 4
Status: **AGREE**

Value: $231.42

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line9_pos — This person's SEP or SIMPLE deduction times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line9 — Schedule 1, line 16, attributable to the same trade or business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line10 — Subtract line 9 from line 8
Status: **AGREE**

Value: $231.42

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $231.42

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_min — The smaller of line 3 or line 13
Status: **AGREE**

Value: $231.42

### classm.sc.3 — person[taxpayer].sc[biz_a].f7206_line14 — Self-employed health insurance deduction
Status: **AGREE**

Value: $231.42

### classm.sc.3 — person[taxpayer].sc[biz_a].qbi_has — This business has a net profit
Status: **AGREE**

Value: yes

### classm.sc.3 — person[taxpayer].sc[biz_a].qbi_se_pos — This person's deductible part of self-employment tax attributable to this busine
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].qbi_se — Deductible part of self-employment tax attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].qbi_plan_pos — This person's SEP or SIMPLE deduction attributable to this business (by share of
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].qbi_plan — SEP or SIMPLE deduction attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_a].qbi_ded — Deductions attributable to this business: self-employment tax, retirement plan a
Status: **AGREE**

Value: $231.42

### classm.sc.3 — person[taxpayer].sc[biz_a].qbi — Qualified business income or (loss) of this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].screened — Something on this Schedule C is outside this tool
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_b].line3 — Subtract line 2 from line 1
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].line4 — Cost of goods sold (from line 42)
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].line5 — Gross profit. Subtract line 4 from line 3
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].line7 — Gross income. Add lines 5 and 6
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].line9 — Car and truck expenses
Status: **AGREE**

Value: $13,157.00

### classm.sc.3 — person[taxpayer].sc[biz_b].line12 — Depletion
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].line13 — Depreciation and section 179 expense deduction (not included in Part III)
Status: **AGREE**

Value: $14.29

### classm.sc.3 — person[taxpayer].sc[biz_b].line20a — Rent or lease: vehicles, machinery, and equipment
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].meals_50_ded — 50% of the meals subject to the 50% limit
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].meals_80_ded — 80% of the meals under the hours of service limits
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].line24b — Deductible meals
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].line27a — Energy efficient commercial buildings deduction (attach Form 7205)
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].line27b — Other expenses (from line 48)
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].line28 — Total expenses before expenses for business use of home. Add lines 8 through 27b
Status: **AGREE**

Value: $29,876.29

### classm.sc.3 — person[taxpayer].sc[biz_b].line29 — Tentative profit or (loss). Subtract line 28 from line 7
Status: **AGREE**

Value: $-29,876.29

### classm.sc.3 — person[taxpayer].sc[biz_b].line28_pre179 — Line 28 without the section 179 expense deduction
Status: **AGREE**

Value: $29,876.29

### classm.sc.3 — person[taxpayer].sc[biz_b].line29_pre179 — Line 29 without the section 179 expense deduction
Status: **AGREE**

Value: $-29,876.29

### classm.sc.3 — person[taxpayer].sc[biz_b].ho_screened — The home office deduction is outside the simplified method this tool covers
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_b].ho_over — More than 300 square feet
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_b].ho_line4_actual — Line 2 (the square feet used) times line 3c
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].ho_line4_cap — 300 square feet times line 3c
Status: **AGREE**

Value: $1,500.00

### classm.sc.3 — person[taxpayer].sc[biz_b].ho_line4 — Multiply line 2 by line 3c
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].ho_line1 — Gross income limitation (Schedule C, line 29)
Status: **AGREE**

Value: $-29,876.29

### classm.sc.3 — person[taxpayer].sc[biz_b].ho_room — Line 29 without the section 179 deduction, less the most section 179 deduction t
Status: **AGREE**

Value: $-29,876.29

### classm.sc.3 — person[taxpayer].sc[biz_b].ho_unlimited — Line 4 is not more than the smallest line 29 any section 179 allocation could gi
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_b].ho_s179_max — The most section 179 deduction this business could take, its 2025 elections plus
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].ho_no179 — No section 179 deduction is possible for this business (no 2025 election and no 
Status: **AGREE**

Value: yes

### classm.sc.3 — person[taxpayer].sc[biz_b].ho_limited — The smaller of line 1 or line 4, with no section 179 election (line 1 is line 29
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].ho_pre179_floor — Line 29 without the section 179 deduction, if zero or less zero
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].ho_both_limits — The gross income limitation could bind together with the section 179 business in
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_b].ho_both — Line 5 when both income limits could bind
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].ho_line5_lim — Line 5 when line 4 is more than the room left by the section 179 elections
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].ho_line5 — Allowable expenses using the simplified method. Enter the smaller of line 1 or l
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].line30 — Expenses for business use of your home
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].line31 — Net profit or (loss). Subtract line 30 from line 29
Status: **AGREE**

Value: $-29,876.29

### classm.sc.3 — person[taxpayer].sc[biz_b].line31_pre179 — Line 31 without the section 179 expense deduction
Status: **AGREE**

Value: $-29,876.29

### classm.sc.3 — person[taxpayer].sc[biz_b].loss — Line 31 is a loss
Status: **AGREE**

Value: yes

### classm.sc.3 — person[taxpayer].sc[biz_b].not_at_risk — Some investment is not at risk (box 32b)
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_b].loss_allowed — The loss on line 31 when all investment is at risk
Status: **AGREE**

Value: $-29,876.29

### classm.sc.3 — person[taxpayer].sc[biz_b].result — The amount for Schedule 1, line 3 and Schedule SE, line 2
Status: **AGREE**

Value: $-29,876.29

### classm.sc.3 — person[taxpayer].sc[biz_b].line40 — Add lines 35 through 39
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].line42 — Cost of goods sold. Subtract line 41 from line 40
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f6 — Section 179 elected on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f14 — Special allowance on property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f17 — MACRS on earlier property other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f19_y3 — MACRS on 2025 property of period y3 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f19_y5 — MACRS on 2025 property of period y5 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f19_y7 — MACRS on 2025 property of period y7 other than listed property
Status: **AGREE**

Value: $14.29

### classm.sc.3 — person[taxpayer].sc[biz_b].f19_y10 — MACRS on 2025 property of period y10 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f19_y15 — MACRS on 2025 property of period y15 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f19_y20 — MACRS on 2025 property of period y20 other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f19_y15sl — MACRS on 2025 property of period y15sl other than listed property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f25_assets — Special allowance on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f25_veh — Special allowance on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f25 — Line 25 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f26_assets — Column (h) of listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f26_veh — Column (h) of vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f26h — Column (h), line 26, for this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f28 — Line 28 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f29_assets — Section 179 elected on listed property other than vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f29_veh — Section 179 on vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f29 — Line 29 for this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].s179_elected — Section 179 elected for this business's 2025 property
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].dep_other — Depreciation other than the section 179 deduction (Form 4562 lines 14, 17, 19 an
Status: **AGREE**

Value: $14.29

### classm.sc.3 — person[taxpayer].sc[biz_b].s179_return — The return's section 179 deduction, for its only Schedule C
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].s179_allowed — Section 179 expense deduction for this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].mq_q4_a — mq_q4 of this business's property
Status: **AGREE**

Value: $100.00

### classm.sc.3 — person[taxpayer].sc[biz_b].mq_q4_v — mq_q4 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].mq_q4 — mq_q4 of this business
Status: **AGREE**

Value: $100.00

### classm.sc.3 — person[taxpayer].sc[biz_b].mq_total_a — mq_total of this business's property
Status: **AGREE**

Value: $100.00

### classm.sc.3 — person[taxpayer].sc[biz_b].mq_total_v — mq_total of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].mq_total — mq_total of this business
Status: **AGREE**

Value: $100.00

### classm.sc.3 — person[taxpayer].sc[biz_b].cost179_a — cost179 of this business's property
Status: **AGREE**

Value: $100.00

### classm.sc.3 — person[taxpayer].sc[biz_b].cost179_v — cost179 of this business's vehicles
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].cost179 — cost179 of this business
Status: **AGREE**

Value: $100.00

### classm.sc.3 — person[taxpayer].sc[biz_b].veh_lease — Business part of vehicle lease payments
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].profit_pos — Net profit of this business (zero for a loss)
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].hi_screened — This health insurance deduction is outside this tool
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_b].f7206_line2 — Qualified long-term care insurance (the smaller of payments or the age limit, fo
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f7206_line3 — Add lines 1 and 2
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f7206_line4 — Net profit from the trade or business under which the insurance plan is establis
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f7206_line5 — Total of all net profits from Schedule C, line 31
Status: **AGREE**

Value: $231.42

### classm.sc.3 — person[taxpayer].sc[biz_b].f7206_has — Line 4 is more than zero
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_b].f7206_line7_pos — Schedule 1, line 15 (this person's), times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f7206_line7 — Multiply Schedule 1 (Form 1040), line 15, deductible part of self-employment tax
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f7206_line8 — Subtract line 7 from line 4
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f7206_line9_pos — This person's SEP or SIMPLE deduction times line 4 divided by line 5
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f7206_line9 — Schedule 1, line 16, attributable to the same trade or business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f7206_line10 — Subtract line 9 from line 8
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f7206_line13 — Subtract line 12 from line 10
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f7206_min — The smaller of line 3 or line 13
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].f7206_line14 — Self-employed health insurance deduction
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].qbi_has — This business has a net profit
Status: **AGREE**

Value: no

### classm.sc.3 — person[taxpayer].sc[biz_b].qbi_se_pos — This person's deductible part of self-employment tax attributable to this busine
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].qbi_se — Deductible part of self-employment tax attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].qbi_plan_pos — This person's SEP or SIMPLE deduction attributable to this business (by share of
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].qbi_plan — SEP or SIMPLE deduction attributable to this business
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].qbi_ded — Deductions attributable to this business: self-employment tax, retirement plan a
Status: **AGREE**

Value: $0.00

### classm.sc.3 — person[taxpayer].sc[biz_b].qbi — Qualified business income or (loss) of this business
Status: **AGREE**

Value: $-29,876.29

## Raw responses

### classm.sc.1

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].screened"
    value: "no"
    work: "All screening answers are no"
  - printed: "person[taxpayer].sc[biz_a].line3"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line4"
    value: "0.00"
    work: "From line 42"
  - printed: "person[taxpayer].sc[biz_a].line5"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line7"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].line9"
    value: "273.00"
    work: "car_1 273.00 + car_2 0.00"
  - printed: "person[taxpayer].sc[biz_a].line12"
    value: "0.00"
    work: "No depletion"
  - printed: "person[taxpayer].sc[biz_a].line13"
    value: "14381.65"
    work: "s179 0.00 + other depreciation 14,381.65"
  - printed: "person[taxpayer].sc[biz_a].line20a"
    value: "1503.11"
    work: "Vehicle lease 1,503.11 + equipment 0.00"
  - printed: "person[taxpayer].sc[biz_a].meals_50_ded"
    value: "7035.00"
    work: "14,070.00 x 50%"
  - printed: "person[taxpayer].sc[biz_a].meals_80_ded"
    value: "0.00"
    work: "0.00 x 80%"
  - printed: "person[taxpayer].sc[biz_a].line24b"
    value: "7035.00"
    work: "7,035.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].line27a"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].line27b"
    value: "0.00"
    work: "Line 48 is 0.00"
  - printed: "person[taxpayer].sc[biz_a].line28"
    value: "23192.76"
    work: "273 + 14,381.65 + 1,503.11 + 7,035"
  - printed: "person[taxpayer].sc[biz_a].line29"
    value: "-23192.76"
    work: "0.00 - 23,192.76"
  - printed: "person[taxpayer].sc[biz_a].line28_pre179"
    value: "23192.76"
    work: "23,192.76 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line29_pre179"
    value: "-23192.76"
    work: "0.00 - 23,192.76"
  - printed: "person[taxpayer].sc[biz_a].ho_screened"
    value: "no"
    work: "No home office claimed"
  - printed: "person[taxpayer].sc[biz_a].ho_over"
    value: "no"
    work: "0 sq ft is not more than 300"
  - printed: "person[taxpayer].sc[biz_a].ho_line4_actual"
    value: "0.00"
    work: "0 x 5.00"
  - printed: "person[taxpayer].sc[biz_a].ho_line4_cap"
    value: "1500.00"
    work: "300 x 5.00"
  - printed: "person[taxpayer].sc[biz_a].ho_line4"
    value: "0.00"
    work: "No home office deduction claimed"
  - printed: "person[taxpayer].sc[biz_a].ho_line1"
    value: "-23192.76"
    work: "Schedule C line 29"
  - printed: "person[taxpayer].sc[biz_a].ho_room"
    value: "-23192.76"
    work: "-23,192.76 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].ho_unlimited"
    value: "no"
    work: "0.00 is more than -23,192.76"
  - printed: "person[taxpayer].sc[biz_a].ho_s179_max"
    value: "0.00"
    work: "Elected 0.00 + carryover 0.00"
  - printed: "person[taxpayer].sc[biz_a].ho_no179"
    value: "yes"
    work: "No election and no carryover"
  - printed: "person[taxpayer].sc[biz_a].ho_limited"
    value: "0.00"
    work: "Smaller of -23,192.76 or 0; zero or less, so 0"
  - printed: "person[taxpayer].sc[biz_a].ho_pre179_floor"
    value: "0.00"
    work: "-23,192.76 is less than zero, so 0"
  - printed: "person[taxpayer].sc[biz_a].ho_both_limits"
    value: "no"
    work: "No section 179 is possible"
  - printed: "person[taxpayer].sc[biz_a].ho_both"
    value: "0.00"
    work: "Not applicable"
  - printed: "person[taxpayer].sc[biz_a].ho_line5_lim"
    value: "0.00"
    work: "Not applicable"
  - printed: "person[taxpayer].sc[biz_a].ho_line5"
    value: "0.00"
    work: "Smaller of line 1 or line 4; zero or less, so 0"
  - printed: "person[taxpayer].sc[biz_a].line30"
    value: "0.00"
    work: "No home office"
  - printed: "person[taxpayer].sc[biz_a].line31"
    value: "-23192.76"
    work: "-23,192.76 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line31_pre179"
    value: "-23192.76"
    work: "-23,192.76 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].loss"
    value: "yes"
    work: "Line 31 is negative"
  - printed: "person[taxpayer].sc[biz_a].not_at_risk"
    value: "no"
    work: "All investment is at risk (32a)"
  - printed: "person[taxpayer].sc[biz_a].loss_allowed"
    value: "-23192.76"
    work: "32a checked and G yes; loss is not limited"
  - printed: "person[taxpayer].sc[biz_a].result"
    value: "-23192.76"
    work: "Line 31"
  - printed: "person[taxpayer].sc[biz_a].line40"
    value: "0.00"
    work: "Lines 35-39 are all 0"
  - printed: "person[taxpayer].sc[biz_a].line42"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].f6"
    value: "0.00"
    work: "Elected 0.00"
  - printed: "person[taxpayer].sc[biz_a].f14"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f17"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y3"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y5"
    value: "3151.40"
    work: "item_1, y5, not listed"
  - printed: "person[taxpayer].sc[biz_a].f19_y7"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y10"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y15"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y20"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y15sl"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f25_assets"
    value: "0.00"
    work: "No listed assets"
  - printed: "person[taxpayer].sc[biz_a].f25_veh"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].f25"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].f26_assets"
    value: "0.00"
    work: "Asset is not listed property"
  - printed: "person[taxpayer].sc[biz_a].f26_veh"
    value: "11230.25"
    work: "0.00 + 11,230.25"
  - printed: "person[taxpayer].sc[biz_a].f26h"
    value: "11230.25"
    work: "0 + 11,230.25"
  - printed: "person[taxpayer].sc[biz_a].f28"
    value: "11230.25"
    work: "Line 25 0 + line 26 11,230.25"
  - printed: "person[taxpayer].sc[biz_a].f29_assets"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f29_veh"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f29"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].s179_elected"
    value: "0.00"
    work: "f6 0 + f29 0"
  - printed: "person[taxpayer].sc[biz_a].dep_other"
    value: "14381.65"
    work: "0 + 0 + 3,151.40 + 11,230.25"
  - printed: "person[taxpayer].sc[biz_a].s179_return"
    value: "0.00"
    work: "Return has two Schedules C; not applicable"
  - printed: "person[taxpayer].sc[biz_a].s179_allowed"
    value: "0.00"
    work: "Deduction equals elections; this business elected 0"
  - printed: "person[taxpayer].sc[biz_a].mq_q4_a"
    value: "0.00"
    work: "item_1 is 0"
  - printed: "person[taxpayer].sc[biz_a].mq_q4_v"
    value: "0.00"
    work: "Vehicles are 0"
  - printed: "person[taxpayer].sc[biz_a].mq_q4"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].mq_total_a"
    value: "15757.00"
    work: "item_1"
  - printed: "person[taxpayer].sc[biz_a].mq_total_v"
    value: "0.00"
    work: "Vehicles are 0"
  - printed: "person[taxpayer].sc[biz_a].mq_total"
    value: "15757.00"
    work: "15,757 + 0"
  - printed: "person[taxpayer].sc[biz_a].cost179_a"
    value: "15757.00"
    work: "item_1"
  - printed: "person[taxpayer].sc[biz_a].cost179_v"
    value: "0.00"
    work: "Vehicles are 0"
  - printed: "person[taxpayer].sc[biz_a].cost179"
    value: "15757.00"
    work: "15,757 + 0"
  - printed: "person[taxpayer].sc[biz_a].veh_lease"
    value: "1503.11"
    work: "car_1 1,503.11 + car_2 0"
  - printed: "person[taxpayer].sc[biz_a].profit_pos"
    value: "0.00"
    work: "Loss"
  - printed: "person[taxpayer].sc[biz_a].hi_screened"
    value: "no"
    work: "Answered no"
  - printed: "person[taxpayer].sc[biz_a].f7206_line2"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f7206_line3"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line4"
    value: "0.00"
    work: "No plan; loss"
  - printed: "person[taxpayer].sc[biz_a].f7206_line5"
    value: "56997.40"
    work: "biz_b net profit only"
  - printed: "person[taxpayer].sc[biz_a].f7206_has"
    value: "no"
    work: "Line 4 is 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line7_pos"
    value: "0.00"
    work: "Line 4 is 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line7"
    value: "0.00"
    work: "Line 4 is 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line8"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line9_pos"
    value: "0.00"
    work: "No SEP"
  - printed: "person[taxpayer].sc[biz_a].f7206_line9"
    value: "0.00"
    work: "No SEP"
  - printed: "person[taxpayer].sc[biz_a].f7206_line10"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line13"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_min"
    value: "0.00"
    work: "Smaller of 0 or 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line14"
    value: "0.00"
    work: "No health insurance"
  - printed: "person[taxpayer].sc[biz_a].qbi_has"
    value: "no"
    work: "Loss"
  - printed: "person[taxpayer].sc[biz_a].qbi_se_pos"
    value: "0.00"
    work: "No net profit"
  - printed: "person[taxpayer].sc[biz_a].qbi_se"
    value: "0.00"
    work: "No net profit"
  - printed: "person[taxpayer].sc[biz_a].qbi_plan_pos"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].qbi_plan"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].qbi_ded"
    value: "0.00"
    work: "0 + 0 + 0"
  - printed: "person[taxpayer].sc[biz_a].qbi"
    value: "-23192.76"
    work: "-23,192.76 - 0"
  - printed: "person[taxpayer].sc[biz_b].screened"
    value: "no"
    work: "All screening answers are no"
  - printed: "person[taxpayer].sc[biz_b].line3"
    value: "146567.00"
    work: "146,567 - 0"
  - printed: "person[taxpayer].sc[biz_b].line4"
    value: "0.00"
    work: "From line 42"
  - printed: "person[taxpayer].sc[biz_b].line5"
    value: "146567.00"
    work: "146,567 - 0"
  - printed: "person[taxpayer].sc[biz_b].line7"
    value: "146567.00"
    work: "146,567 + 0"
  - printed: "person[taxpayer].sc[biz_b].line9"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_b].line12"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].line13"
    value: "12659.60"
    work: "10,804 + 1,855.60"
  - printed: "person[taxpayer].sc[biz_b].line20a"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].meals_50_ded"
    value: "0.00"
    work: "0 x 50%"
  - printed: "person[taxpayer].sc[biz_b].meals_80_ded"
    value: "0.00"
    work: "0 x 80%"
  - printed: "person[taxpayer].sc[biz_b].line24b"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].line27a"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].line27b"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].line28"
    value: "88069.60"
    work: "13,020 + 2,428 + 20,366 + 12,645 + 26,951 + 12,659.60"
  - printed: "person[taxpayer].sc[biz_b].line29"
    value: "58497.40"
    work: "146,567 - 88,069.60"
  - printed: "person[taxpayer].sc[biz_b].line28_pre179"
    value: "77265.60"
    work: "88,069.60 - 10,804"
  - printed: "person[taxpayer].sc[biz_b].line29_pre179"
    value: "69301.40"
    work: "146,567 - 77,265.60"
  - printed: "person[taxpayer].sc[biz_b].ho_screened"
    value: "no"
    work: "Simplified method; no exceptions"
  - printed: "person[taxpayer].sc[biz_b].ho_over"
    value: "yes"
    work: "445 > 300"
  - printed: "person[taxpayer].sc[biz_b].ho_line4_actual"
    value: "2225.00"
    work: "445 x 5.00"
  - printed: "person[taxpayer].sc[biz_b].ho_line4_cap"
    value: "1500.00"
    work: "300 x 5.00"
  - printed: "person[taxpayer].sc[biz_b].ho_line4"
    value: "1500.00"
    work: "Line 2 capped at 300 sq ft"
  - printed: "person[taxpayer].sc[biz_b].ho_line1"
    value: "58497.40"
    work: "Schedule C line 29"
  - printed: "person[taxpayer].sc[biz_b].ho_room"
    value: "58497.40"
    work: "69,301.40 - 10,804"
  - printed: "person[taxpayer].sc[biz_b].ho_unlimited"
    value: "yes"
    work: "1,500 <= 58,497.40"
  - printed: "person[taxpayer].sc[biz_b].ho_s179_max"
    value: "10804.00"
    work: "10,804 + 0"
  - printed: "person[taxpayer].sc[biz_b].ho_no179"
    value: "no"
    work: "Election of 10,804"
  - printed: "person[taxpayer].sc[biz_b].ho_limited"
    value: "1500.00"
    work: "Smaller of 69,301.40 or 1,500"
  - printed: "person[taxpayer].sc[biz_b].ho_pre179_floor"
    value: "69301.40"
    work: "Positive"
  - printed: "person[taxpayer].sc[biz_b].ho_both_limits"
    value: "no"
    work: "Line 4 is within the room"
  - printed: "person[taxpayer].sc[biz_b].ho_both"
    value: "1500.00"
    work: "Smaller of line 1 or line 4"
  - printed: "person[taxpayer].sc[biz_b].ho_line5_lim"
    value: "1500.00"
    work: "Smaller of room 58,497.40 or 1,500"
  - printed: "person[taxpayer].sc[biz_b].ho_line5"
    value: "1500.00"
    work: "Smaller of 58,497.40 or 1,500"
  - printed: "person[taxpayer].sc[biz_b].line30"
    value: "1500.00"
    work: "Worksheet line 5"
  - printed: "person[taxpayer].sc[biz_b].line31"
    value: "56997.40"
    work: "58,497.40 - 1,500"
  - printed: "person[taxpayer].sc[biz_b].line31_pre179"
    value: "67801.40"
    work: "69,301.40 - 1,500"
  - printed: "person[taxpayer].sc[biz_b].loss"
    value: "no"
    work: "Profit"
  - printed: "person[taxpayer].sc[biz_b].not_at_risk"
    value: "no"
    work: "32a"
  - printed: "person[taxpayer].sc[biz_b].loss_allowed"
    value: "0.00"
    work: "No loss"
  - printed: "person[taxpayer].sc[biz_b].result"
    value: "56997.40"
    work: "Line 31"
  - printed: "person[taxpayer].sc[biz_b].line40"
    value: "0.00"
    work: "Lines 35-39 are 0"
  - printed: "person[taxpayer].sc[biz_b].line42"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_b].f6"
    value: "10804.00"
    work: "item_1 10,804 + item_2 0"
  - printed: "person[taxpayer].sc[biz_b].f14"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f17"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y3"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y5"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y7"
    value: "0.00"
    work: "item_2 is 0"
  - printed: "person[taxpayer].sc[biz_b].f19_y10"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y15"
    value: "1855.60"
    work: "item_1"
  - printed: "person[taxpayer].sc[biz_b].f19_y20"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y15sl"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f25_assets"
    value: "0.00"
    work: "Not listed"
  - printed: "person[taxpayer].sc[biz_b].f25_veh"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_b].f25"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].f26_assets"
    value: "0.00"
    work: "Not listed"
  - printed: "person[taxpayer].sc[biz_b].f26_veh"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_b].f26h"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].f28"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].f29_assets"
    value: "0.00"
    work: "Not listed"
  - printed: "person[taxpayer].sc[biz_b].f29_veh"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_b].f29"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].s179_elected"
    value: "10804.00"
    work: "f6 10,804 + f29 0"
  - printed: "person[taxpayer].sc[biz_b].dep_other"
    value: "1855.60"
    work: "0 + 0 + 1,855.60 + 0"
  - printed: "person[taxpayer].sc[biz_b].s179_return"
    value: "0.00"
    work: "Return has two Schedules C; not applicable"
  - printed: "person[taxpayer].sc[biz_b].s179_allowed"
    value: "10804.00"
    work: "Deduction equals elections; allocate as elected"
  - printed: "person[taxpayer].sc[biz_b].mq_q4_a"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].mq_q4_v"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_b].mq_q4"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].mq_total_a"
    value: "37112.00"
    work: "37,112 + 0"
  - printed: "person[taxpayer].sc[biz_b].mq_total_v"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_b].mq_total"
    value: "37112.00"
    work: "37,112 + 0"
  - printed: "person[taxpayer].sc[biz_b].cost179_a"
    value: "47916.00"
    work: "47,916 + 0"
  - printed: "person[taxpayer].sc[biz_b].cost179_v"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_b].cost179"
    value: "47916.00"
    work: "47,916 + 0"
  - printed: "person[taxpayer].sc[biz_b].veh_lease"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_b].profit_pos"
    value: "56997.40"
    work: "Line 31 profit"
  - printed: "person[taxpayer].sc[biz_b].hi_screened"
    value: "no"
    work: "Answered no"
  - printed: "person[taxpayer].sc[biz_b].f7206_line2"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f7206_line3"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line4"
    value: "0.00"
    work: "No plan established under this business"
  - printed: "person[taxpayer].sc[biz_b].f7206_line5"
    value: "56997.40"
    work: "Net profits only"
  - printed: "person[taxpayer].sc[biz_b].f7206_has"
    value: "no"
    work: "Line 4 is 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line7_pos"
    value: "0.00"
    work: "Line 4 is 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line7"
    value: "0.00"
    work: "Line 4 is 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line8"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line9_pos"
    value: "0.00"
    work: "No SEP"
  - printed: "person[taxpayer].sc[biz_b].f7206_line9"
    value: "0.00"
    work: "No SEP"
  - printed: "person[taxpayer].sc[biz_b].f7206_line10"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line13"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_min"
    value: "0.00"
    work: "Smaller of 0 or 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line14"
    value: "0.00"
    work: "No health insurance"
  - printed: "person[taxpayer].sc[biz_b].qbi_has"
    value: "yes"
    work: "Net profit 56,997.40"
  - printed: "person[taxpayer].sc[biz_b].qbi_se_pos"
    value: "2388.22"
    work: "SE: 33,804.64 x .9235 = 31,218.59 x .153 / 2 = 2,388.22; x 56,997.40/56,997.40"
  - printed: "person[taxpayer].sc[biz_b].qbi_se"
    value: "2388.22"
    work: "Positive share"
  - printed: "person[taxpayer].sc[biz_b].qbi_plan_pos"
    value: "0.00"
    work: "No SEP or SIMPLE"
  - printed: "person[taxpayer].sc[biz_b].qbi_plan"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].qbi_ded"
    value: "2388.22"
    work: "2,388.22 + 0 + 0"
  - printed: "person[taxpayer].sc[biz_b].qbi"
    value: "54609.18"
    work: "56,997.40 - 2,388.22"
```
```

### classm.sc.2

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].screened"
    value: "no"
    work: "Not a statutory employee; no joint ownership; no special method; no excluded items"
  - printed: "person[taxpayer].sc[biz_a].line3"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line4"
    value: "0.00"
    work: "From line 42"
  - printed: "person[taxpayer].sc[biz_a].line5"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line7"
    value: "1387.00"
    work: "0.00 + 1,387.00"
  - printed: "person[taxpayer].sc[biz_a].line9"
    value: "0.00"
    work: "No vehicles for this business"
  - printed: "person[taxpayer].sc[biz_a].line12"
    value: "0.00"
    work: "No depletion"
  - printed: "person[taxpayer].sc[biz_a].line13"
    value: "0.00"
    work: "Depreciation 0 + section 179 0"
  - printed: "person[taxpayer].sc[biz_a].line20a"
    value: "0.00"
    work: "Equipment rent 0 + vehicle lease 0"
  - printed: "person[taxpayer].sc[biz_a].meals_50_ded"
    value: "0.00"
    work: "50% of 0"
  - printed: "person[taxpayer].sc[biz_a].meals_80_ded"
    value: "0.00"
    work: "80% of 0"
  - printed: "person[taxpayer].sc[biz_a].line24b"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].line27a"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].line27b"
    value: "0.00"
    work: "Line 48 = 0"
  - printed: "person[taxpayer].sc[biz_a].line28"
    value: "39721.00"
    work: "13,593 + 10,329 + 15,799"
  - printed: "person[taxpayer].sc[biz_a].line29"
    value: "-38334.00"
    work: "1,387 - 39,721"
  - printed: "person[taxpayer].sc[biz_a].line28_pre179"
    value: "39721.00"
    work: "Line 28 with no section 179"
  - printed: "person[taxpayer].sc[biz_a].line29_pre179"
    value: "-38334.00"
    work: "1,387 - 39,721"
  - printed: "person[taxpayer].sc[biz_a].ho_screened"
    value: "no"
    work: "No disqualifying condition; simplified method used"
  - printed: "person[taxpayer].sc[biz_a].ho_over"
    value: "no"
    work: "137 is not more than 300"
  - printed: "person[taxpayer].sc[biz_a].ho_line4_actual"
    value: "685.00"
    work: "137 x 5.00"
  - printed: "person[taxpayer].sc[biz_a].ho_line4_cap"
    value: "1500.00"
    work: "300 x 5.00"
  - printed: "person[taxpayer].sc[biz_a].ho_line4"
    value: "685.00"
    work: "137 sq ft x $5"
  - printed: "person[taxpayer].sc[biz_a].ho_line1"
    value: "-38334.00"
    work: "Schedule C line 29"
  - printed: "person[taxpayer].sc[biz_a].ho_room"
    value: "-38334.00"
    work: "-38,334 - 0"
  - printed: "person[taxpayer].sc[biz_a].ho_unlimited"
    value: "no"
    work: "685 > -38,334"
  - printed: "person[taxpayer].sc[biz_a].ho_s179_max"
    value: "0.00"
    work: "Elections 0 + carryover 0"
  - printed: "person[taxpayer].sc[biz_a].ho_no179"
    value: "yes"
    work: "No election and no carryover"
  - printed: "person[taxpayer].sc[biz_a].ho_limited"
    value: "0.00"
    work: "Smaller of -38,334 or 685; zero or less, so 0"
  - printed: "person[taxpayer].sc[biz_a].ho_pre179_floor"
    value: "0.00"
    work: "-38,334 floored at 0"
  - printed: "person[taxpayer].sc[biz_a].ho_both_limits"
    value: "no"
    work: "No section 179 possible"
  - printed: "person[taxpayer].sc[biz_a].ho_both"
    value: "0.00"
    work: "Not applicable"
  - printed: "person[taxpayer].sc[biz_a].ho_line5_lim"
    value: "0.00"
    work: "Room is negative, so 0"
  - printed: "person[taxpayer].sc[biz_a].ho_line5"
    value: "0.00"
    work: "Smaller of -38,334 or 685; zero or less, so 0"
  - printed: "person[taxpayer].sc[biz_a].line30"
    value: "0.00"
    work: "Worksheet line 5"
  - printed: "person[taxpayer].sc[biz_a].line31"
    value: "-38334.00"
    work: "-38,334 - 0"
  - printed: "person[taxpayer].sc[biz_a].line31_pre179"
    value: "-38334.00"
    work: "-38,334 - 0"
  - printed: "person[taxpayer].sc[biz_a].loss"
    value: "yes"
    work: "Line 31 is negative"
  - printed: "person[taxpayer].sc[biz_a].not_at_risk"
    value: "no"
    work: "All investment at risk (box 32a)"
  - printed: "person[taxpayer].sc[biz_a].loss_allowed"
    value: "-38334.00"
    work: "32a checked and line G is Yes; loss not reduced"
  - printed: "person[taxpayer].sc[biz_a].result"
    value: "-38334.00"
    work: "Line 31"
  - printed: "person[taxpayer].sc[biz_a].line40"
    value: "0.00"
    work: "All of lines 35-39 are 0"
  - printed: "person[taxpayer].sc[biz_a].line42"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].f6"
    value: "0.00"
    work: "Item_2 = 0"
  - printed: "person[taxpayer].sc[biz_a].f14"
    value: "0.00"
    work: "Item_2 = 0"
  - printed: "person[taxpayer].sc[biz_a].f17"
    value: "0.00"
    work: "Item_2 = 0"
  - printed: "person[taxpayer].sc[biz_a].f19_y3"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y5"
    value: "0.00"
    work: "Item_1 is listed; excluded"
  - printed: "person[taxpayer].sc[biz_a].f19_y7"
    value: "0.00"
    work: "Item_2 = 0"
  - printed: "person[taxpayer].sc[biz_a].f19_y10"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y15"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y20"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y15sl"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f25_assets"
    value: "0.00"
    work: "Item_1 = 0"
  - printed: "person[taxpayer].sc[biz_a].f25_veh"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].f25"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].f26_assets"
    value: "0.00"
    work: "Item_1 = 0"
  - printed: "person[taxpayer].sc[biz_a].f26_veh"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].f26h"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].f28"
    value: "0.00"
    work: "Line 25 + line 26"
  - printed: "person[taxpayer].sc[biz_a].f29_assets"
    value: "0.00"
    work: "Item_1 = 0"
  - printed: "person[taxpayer].sc[biz_a].f29_veh"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].f29"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].s179_elected"
    value: "0.00"
    work: "f6 + f29"
  - printed: "person[taxpayer].sc[biz_a].dep_other"
    value: "0.00"
    work: "Lines 14 + 17 + 19 + 21 = 0"
  - printed: "person[taxpayer].sc[biz_a].s179_return"
    value: "0.00"
    work: "Form 4562 line 12 = 0"
  - printed: "person[taxpayer].sc[biz_a].s179_allowed"
    value: "0.00"
    work: "Line 12 = 0"
  - printed: "person[taxpayer].sc[biz_a].mq_q4_a"
    value: "0.00"
    work: "Assets = 0"
  - printed: "person[taxpayer].sc[biz_a].mq_q4_v"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].mq_q4"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].mq_total_a"
    value: "0.00"
    work: "Assets = 0"
  - printed: "person[taxpayer].sc[biz_a].mq_total_v"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].mq_total"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].cost179_a"
    value: "0.00"
    work: "Assets = 0"
  - printed: "person[taxpayer].sc[biz_a].cost179_v"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].cost179"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].veh_lease"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].profit_pos"
    value: "0.00"
    work: "Loss, so 0"
  - printed: "person[taxpayer].sc[biz_a].hi_screened"
    value: "no"
    work: "No health insurance under this business"
  - printed: "person[taxpayer].sc[biz_a].f7206_line2"
    value: "0.00"
    work: "No long-term care under this business"
  - printed: "person[taxpayer].sc[biz_a].f7206_line3"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line4"
    value: "0.00"
    work: "Net loss, so 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line5"
    value: "24376.22"
    work: "Only net profit is biz_b line 31"
  - printed: "person[taxpayer].sc[biz_a].f7206_has"
    value: "no"
    work: "Line 4 is 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line7_pos"
    value: "0.00"
    work: "Line 4 is 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line7"
    value: "0.00"
    work: "Line 4 is 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line8"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line9_pos"
    value: "0.00"
    work: "No SEP or SIMPLE"
  - printed: "person[taxpayer].sc[biz_a].f7206_line9"
    value: "0.00"
    work: "No SEP or SIMPLE"
  - printed: "person[taxpayer].sc[biz_a].f7206_line10"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line13"
    value: "0.00"
    work: "0 - 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_min"
    value: "0.00"
    work: "Smaller of 0 or 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line14"
    value: "0.00"
    work: "No plan"
  - printed: "person[taxpayer].sc[biz_a].qbi_has"
    value: "no"
    work: "Loss"
  - printed: "person[taxpayer].sc[biz_a].qbi_se_pos"
    value: "0.00"
    work: "No profit"
  - printed: "person[taxpayer].sc[biz_a].qbi_se"
    value: "0.00"
    work: "No profit"
  - printed: "person[taxpayer].sc[biz_a].qbi_plan_pos"
    value: "0.00"
    work: "No profit"
  - printed: "person[taxpayer].sc[biz_a].qbi_plan"
    value: "0.00"
    work: "No profit"
  - printed: "person[taxpayer].sc[biz_a].qbi_ded"
    value: "0.00"
    work: "0 + 0 + 0"
  - printed: "person[taxpayer].sc[biz_a].qbi"
    value: "-38334.00"
    work: "-38,334 - 0"
  - printed: "person[taxpayer].sc[biz_b].screened"
    value: "no"
    work: "All screening answers are no"
  - printed: "person[taxpayer].sc[biz_b].line3"
    value: "119082.00"
    work: "119,082 - 0"
  - printed: "person[taxpayer].sc[biz_b].line4"
    value: "22066.00"
    work: "From line 42"
  - printed: "person[taxpayer].sc[biz_b].line5"
    value: "97016.00"
    work: "119,082 - 22,066"
  - printed: "person[taxpayer].sc[biz_b].line7"
    value: "97016.00"
    work: "97,016 + 0"
  - printed: "person[taxpayer].sc[biz_b].line9"
    value: "15768.40"
    work: "11,799.90 + 3,968.50"
  - printed: "person[taxpayer].sc[biz_b].line12"
    value: "0.00"
    work: "No depletion"
  - printed: "person[taxpayer].sc[biz_b].line13"
    value: "476.38"
    work: "Line 17 MACRS 476.38 + section 179 0"
  - printed: "person[taxpayer].sc[biz_b].line20a"
    value: "13213.00"
    work: "13,213 + vehicle lease 0"
  - printed: "person[taxpayer].sc[biz_b].meals_50_ded"
    value: "0.00"
    work: "50% of 0"
  - printed: "person[taxpayer].sc[biz_b].meals_80_ded"
    value: "0.00"
    work: "80% of 0"
  - printed: "person[taxpayer].sc[biz_b].line24b"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].line27a"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].line27b"
    value: "0.00"
    work: "Line 48 = 0"
  - printed: "person[taxpayer].sc[biz_b].line28"
    value: "72639.78"
    work: "21,489 + 15,768.40 + 476.38 + 4,731 + 16,962 + 13,213"
  - printed: "person[taxpayer].sc[biz_b].line29"
    value: "24376.22"
    work: "97,016 - 72,639.78"
  - printed: "person[taxpayer].sc[biz_b].line28_pre179"
    value: "72639.78"
    work: "Line 28 with no section 179"
  - printed: "person[taxpayer].sc[biz_b].line29_pre179"
    value: "24376.22"
    work: "97,016 - 72,639.78"
  - printed: "person[taxpayer].sc[biz_b].ho_screened"
    value: "no"
    work: "No home office claimed"
  - printed: "person[taxpayer].sc[biz_b].ho_over"
    value: "no"
    work: "0 sq ft"
  - printed: "person[taxpayer].sc[biz_b].ho_line4_actual"
    value: "0.00"
    work: "0 x 5.00"
  - printed: "person[taxpayer].sc[biz_b].ho_line4_cap"
    value: "1500.00"
    work: "300 x 5.00"
  - printed: "person[taxpayer].sc[biz_b].ho_line4"
    value: "0.00"
    work: "No home office"
  - printed: "person[taxpayer].sc[biz_b].ho_line1"
    value: "24376.22"
    work: "Line 29"
  - printed: "person[taxpayer].sc[biz_b].ho_room"
    value: "24376.22"
    work: "24,376.22 - 0"
  - printed: "person[taxpayer].sc[biz_b].ho_unlimited"
    value: "yes"
    work: "0 <= 24,376.22"
  - printed: "person[taxpayer].sc[biz_b].ho_s179_max"
    value: "0.00"
    work: "Elections 0 + carryover 0"
  - printed: "person[taxpayer].sc[biz_b].ho_no179"
    value: "yes"
    work: "No election and no carryover"
  - printed: "person[taxpayer].sc[biz_b].ho_limited"
    value: "0.00"
    work: "Smaller of 24,376.22 or 0"
  - printed: "person[taxpayer].sc[biz_b].ho_pre179_floor"
    value: "24376.22"
    work: "Positive"
  - printed: "person[taxpayer].sc[biz_b].ho_both_limits"
    value: "no"
    work: "No section 179"
  - printed: "person[taxpayer].sc[biz_b].ho_both"
    value: "0.00"
    work: "Not applicable"
  - printed: "person[taxpayer].sc[biz_b].ho_line5_lim"
    value: "0.00"
    work: "Not applicable"
  - printed: "person[taxpayer].sc[biz_b].ho_line5"
    value: "0.00"
    work: "Smaller of 24,376.22 or 0"
  - printed: "person[taxpayer].sc[biz_b].line30"
    value: "0.00"
    work: "No home office"
  - printed: "person[taxpayer].sc[biz_b].line31"
    value: "24376.22"
    work: "24,376.22 - 0"
  - printed: "person[taxpayer].sc[biz_b].line31_pre179"
    value: "24376.22"
    work: "24,376.22 - 0"
  - printed: "person[taxpayer].sc[biz_b].loss"
    value: "no"
    work: "Profit"
  - printed: "person[taxpayer].sc[biz_b].not_at_risk"
    value: "no"
    work: "All investment at risk"
  - printed: "person[taxpayer].sc[biz_b].loss_allowed"
    value: "0.00"
    work: "No loss"
  - printed: "person[taxpayer].sc[biz_b].result"
    value: "24376.22"
    work: "Line 31"
  - printed: "person[taxpayer].sc[biz_b].line40"
    value: "24744.00"
    work: "0 + 24,744 + 0 + 0 + 0"
  - printed: "person[taxpayer].sc[biz_b].line42"
    value: "22066.00"
    work: "24,744 - 2,678"
  - printed: "person[taxpayer].sc[biz_b].f6"
    value: "0.00"
    work: "Item_1 = 0"
  - printed: "person[taxpayer].sc[biz_b].f14"
    value: "0.00"
    work: "Item_1 = 0"
  - printed: "person[taxpayer].sc[biz_b].f17"
    value: "476.38"
    work: "Item_1, not listed"
  - printed: "person[taxpayer].sc[biz_b].f19_y3"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y5"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y7"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y10"
    value: "0.00"
    work: "Item_1 2025 MACRS = 0"
  - printed: "person[taxpayer].sc[biz_b].f19_y15"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y20"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y15sl"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f25_assets"
    value: "0.00"
    work: "No listed assets"
  - printed: "person[taxpayer].sc[biz_b].f25_veh"
    value: "0.00"
    work: "Car_1 0 + car_2 0"
  - printed: "person[taxpayer].sc[biz_b].f25"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].f26_assets"
    value: "0.00"
    work: "Item_1 is not listed"
  - printed: "person[taxpayer].sc[biz_b].f26_veh"
    value: "0.00"
    work: "Car_1 0 + car_2 0"
  - printed: "person[taxpayer].sc[biz_b].f26h"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].f28"
    value: "0.00"
    work: "Line 25 + line 26"
  - printed: "person[taxpayer].sc[biz_b].f29_assets"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f29_veh"
    value: "0.00"
    work: "Vehicles 0"
  - printed: "person[taxpayer].sc[biz_b].f29"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].s179_elected"
    value: "0.00"
    work: "f6 + f29"
  - printed: "person[taxpayer].sc[biz_b].dep_other"
    value: "476.38"
    work: "Line 17 = 476.38"
  - printed: "person[taxpayer].sc[biz_b].s179_return"
    value: "0.00"
    work: "Form 4562 line 12 = 0"
  - printed: "person[taxpayer].sc[biz_b].s179_allowed"
    value: "0.00"
    work: "Line 12 = 0"
  - printed: "person[taxpayer].sc[biz_b].mq_q4_a"
    value: "0.00"
    work: "Item_1 = 0"
  - printed: "person[taxpayer].sc[biz_b].mq_q4_v"
    value: "0.00"
    work: "Vehicles 0"
  - printed: "person[taxpayer].sc[biz_b].mq_q4"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].mq_total_a"
    value: "0.00"
    work: "Item_1 = 0"
  - printed: "person[taxpayer].sc[biz_b].mq_total_v"
    value: "0.00"
    work: "Vehicles 0"
  - printed: "person[taxpayer].sc[biz_b].mq_total"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].cost179_a"
    value: "0.00"
    work: "Item_1 = 0"
  - printed: "person[taxpayer].sc[biz_b].cost179_v"
    value: "0.00"
    work: "Vehicles 0"
  - printed: "person[taxpayer].sc[biz_b].cost179"
    value: "0.00"
    work: "0 + 0"
  - printed: "person[taxpayer].sc[biz_b].veh_lease"
    value: "0.00"
    work: "Car_1 0 + car_2 0"
  - printed: "person[taxpayer].sc[biz_b].profit_pos"
    value: "24376.22"
    work: "Line 31 positive"
  - printed: "person[taxpayer].sc[biz_b].hi_screened"
    value: "no"
    work: "No special condition applies"
  - printed: "person[taxpayer].sc[biz_b].f7206_line2"
    value: "480.00"
    work: "Smaller of (a) or (b) = 480"
  - printed: "person[taxpayer].sc[biz_b].f7206_line3"
    value: "1837.00"
    work: "1,357 + 480"
  - printed: "person[taxpayer].sc[biz_b].f7206_line4"
    value: "24376.22"
    work: "Biz_b net profit"
  - printed: "person[taxpayer].sc[biz_b].f7206_line5"
    value: "24376.22"
    work: "Only profitable Schedule C"
  - printed: "person[taxpayer].sc[biz_b].f7206_has"
    value: "yes"
    work: "24,376.22 > 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line7_pos"
    value: "0.00"
    work: "Schedule 1 line 15 is 0: combined SE line 2 = 24,376.22 - 38,334 < 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line7"
    value: "0.00"
    work: "0 x 100%"
  - printed: "person[taxpayer].sc[biz_b].f7206_line8"
    value: "24376.22"
    work: "24,376.22 - 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line9_pos"
    value: "0.00"
    work: "No Schedule 1 line 16 amount"
  - printed: "person[taxpayer].sc[biz_b].f7206_line9"
    value: "0.00"
    work: "No SEP or SIMPLE for self"
  - printed: "person[taxpayer].sc[biz_b].f7206_line10"
    value: "24376.22"
    work: "24,376.22 - 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line13"
    value: "24376.22"
    work: "24,376.22 - 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_min"
    value: "1837.00"
    work: "Smaller of 1,837 or 24,376.22"
  - printed: "person[taxpayer].sc[biz_b].f7206_line14"
    value: "1837.00"
    work: "Line 14 = smaller of line 3 or line 13"
  - printed: "person[taxpayer].sc[biz_b].qbi_has"
    value: "yes"
    work: "Net profit"
  - printed: "person[taxpayer].sc[biz_b].qbi_se_pos"
    value: "0.00"
    work: "Schedule 1 line 15 = 0"
  - printed: "person[taxpayer].sc[biz_b].qbi_se"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_b].qbi_plan_pos"
    value: "0.00"
    work: "No SEP or SIMPLE"
  - printed: "person[taxpayer].sc[biz_b].qbi_plan"
    value: "0.00"
    work: "0"
  - printed: "person[taxpayer].sc[biz_b].qbi_ded"
    value: "1837.00"
    work: "0 + 0 + 1,837"
  - printed: "person[taxpayer].sc[biz_b].qbi"
    value: "22539.22"
    work: "24,376.22 - 1,837"
```
```

### classm.sc.3

```yaml
```yaml
lines:
  - printed: "person[taxpayer].sc[biz_a].screened"
    value: "no"
    work: "All screening questions answered no"
  - printed: "person[taxpayer].sc[biz_a].line3"
    value: "88883.00"
    work: "88,883.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line4"
    value: "0.00"
    work: "From line 42"
  - printed: "person[taxpayer].sc[biz_a].line5"
    value: "88883.00"
    work: "88,883.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line7"
    value: "88883.00"
    work: "88,883.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].line9"
    value: "0.00"
    work: "No vehicles for this business"
  - printed: "person[taxpayer].sc[biz_a].line12"
    value: "0.00"
    work: "No depletion"
  - printed: "person[taxpayer].sc[biz_a].line13"
    value: "815.78"
    work: "Section 179 0.00 + other depreciation 815.78"
  - printed: "person[taxpayer].sc[biz_a].line20a"
    value: "30000.00"
    work: "30,000.00 machinery/equipment + 0.00 vehicle lease"
  - printed: "person[taxpayer].sc[biz_a].meals_50_ded"
    value: "0.00"
    work: "50% x 0.00"
  - printed: "person[taxpayer].sc[biz_a].meals_80_ded"
    value: "16508.80"
    work: "80% x 20,636.00"
  - printed: "person[taxpayer].sc[biz_a].line24b"
    value: "16508.80"
    work: "0.00 + 16,508.80"
  - printed: "person[taxpayer].sc[biz_a].line27a"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].line27b"
    value: "9283.00"
    work: "From line 48"
  - printed: "person[taxpayer].sc[biz_a].line28"
    value: "88651.58"
    work: "8,277 + 23,767 + 815.78 + 30,000 + 16,508.80 + 9,283"
  - printed: "person[taxpayer].sc[biz_a].line29"
    value: "231.42"
    work: "88,883.00 - 88,651.58"
  - printed: "person[taxpayer].sc[biz_a].line28_pre179"
    value: "88651.58"
    work: "Section 179 is 0.00"
  - printed: "person[taxpayer].sc[biz_a].line29_pre179"
    value: "231.42"
    work: "88,883.00 - 88,651.58"
  - printed: "person[taxpayer].sc[biz_a].ho_screened"
    value: "no"
    work: "No home office claimed"
  - printed: "person[taxpayer].sc[biz_a].ho_over"
    value: "no"
    work: "0 sq ft"
  - printed: "person[taxpayer].sc[biz_a].ho_line4_actual"
    value: "0.00"
    work: "0 x 5.00"
  - printed: "person[taxpayer].sc[biz_a].ho_line4_cap"
    value: "1500.00"
    work: "300 x 5.00"
  - printed: "person[taxpayer].sc[biz_a].ho_line4"
    value: "0.00"
    work: "0 sq ft x 5.00"
  - printed: "person[taxpayer].sc[biz_a].ho_line1"
    value: "231.42"
    work: "Schedule C line 29"
  - printed: "person[taxpayer].sc[biz_a].ho_room"
    value: "231.42"
    work: "231.42 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].ho_unlimited"
    value: "yes"
    work: "0.00 <= 231.42"
  - printed: "person[taxpayer].sc[biz_a].ho_s179_max"
    value: "0.00"
    work: "Elected 0.00 + carryover 0.00"
  - printed: "person[taxpayer].sc[biz_a].ho_no179"
    value: "yes"
    work: "No election and no carryover"
  - printed: "person[taxpayer].sc[biz_a].ho_limited"
    value: "0.00"
    work: "Smaller of 231.42 or 0.00"
  - printed: "person[taxpayer].sc[biz_a].ho_pre179_floor"
    value: "231.42"
    work: "231.42 is positive"
  - printed: "person[taxpayer].sc[biz_a].ho_both_limits"
    value: "no"
    work: "No section 179 possible"
  - printed: "person[taxpayer].sc[biz_a].ho_both"
    value: "0.00"
    work: "Not applicable"
  - printed: "person[taxpayer].sc[biz_a].ho_line5_lim"
    value: "0.00"
    work: "Not applicable"
  - printed: "person[taxpayer].sc[biz_a].ho_line5"
    value: "0.00"
    work: "Smaller of 231.42 or 0.00"
  - printed: "person[taxpayer].sc[biz_a].line30"
    value: "0.00"
    work: "No home office deduction"
  - printed: "person[taxpayer].sc[biz_a].line31"
    value: "231.42"
    work: "231.42 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].line31_pre179"
    value: "231.42"
    work: "231.42 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].loss"
    value: "no"
    work: "Line 31 is a profit"
  - printed: "person[taxpayer].sc[biz_a].not_at_risk"
    value: "no"
    work: "All investment at risk"
  - printed: "person[taxpayer].sc[biz_a].loss_allowed"
    value: "0.00"
    work: "No loss"
  - printed: "person[taxpayer].sc[biz_a].result"
    value: "231.42"
    work: "Line 31"
  - printed: "person[taxpayer].sc[biz_a].line40"
    value: "0.00"
    work: "All lines 35-39 are 0"
  - printed: "person[taxpayer].sc[biz_a].line42"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].f6"
    value: "0.00"
    work: "Elected 0.00"
  - printed: "person[taxpayer].sc[biz_a].f14"
    value: "671.78"
    work: "Special allowance, not listed property"
  - printed: "person[taxpayer].sc[biz_a].f17"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y3"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y5"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y7"
    value: "144.00"
    work: "Item_1, 7-year property"
  - printed: "person[taxpayer].sc[biz_a].f19_y10"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y15"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y20"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f19_y15sl"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f25_assets"
    value: "0.00"
    work: "No listed property"
  - printed: "person[taxpayer].sc[biz_a].f25_veh"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].f25"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].f26_assets"
    value: "0.00"
    work: "Asset is not listed property"
  - printed: "person[taxpayer].sc[biz_a].f26_veh"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].f26h"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].f28"
    value: "0.00"
    work: "Line 25 + line 26 = 0.00"
  - printed: "person[taxpayer].sc[biz_a].f29_assets"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f29_veh"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f29"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].s179_elected"
    value: "0.00"
    work: "f6 0.00 + f29 0.00"
  - printed: "person[taxpayer].sc[biz_a].dep_other"
    value: "815.78"
    work: "671.78 + 0 + 144.00 + 0"
  - printed: "person[taxpayer].sc[biz_a].s179_return"
    value: "0.00"
    work: "Form 4562 line 12 = 0.00"
  - printed: "person[taxpayer].sc[biz_a].s179_allowed"
    value: "0.00"
    work: "Return total is 0.00"
  - printed: "person[taxpayer].sc[biz_a].mq_q4_a"
    value: "0.00"
    work: "Item_1"
  - printed: "person[taxpayer].sc[biz_a].mq_q4_v"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].mq_q4"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].mq_total_a"
    value: "1679.46"
    work: "Item_1"
  - printed: "person[taxpayer].sc[biz_a].mq_total_v"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].mq_total"
    value: "1679.46"
    work: "1,679.46 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].cost179_a"
    value: "0.00"
    work: "Item_1"
  - printed: "person[taxpayer].sc[biz_a].cost179_v"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].cost179"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_a].veh_lease"
    value: "0.00"
    work: "No vehicles"
  - printed: "person[taxpayer].sc[biz_a].profit_pos"
    value: "231.42"
    work: "Line 31 is positive"
  - printed: "person[taxpayer].sc[biz_a].hi_screened"
    value: "no"
    work: "Answered no"
  - printed: "person[taxpayer].sc[biz_a].f7206_line2"
    value: "3996.00"
    work: "Given smaller of (a) or (b)"
  - printed: "person[taxpayer].sc[biz_a].f7206_line3"
    value: "3996.00"
    work: "0.00 + 3,996.00"
  - printed: "person[taxpayer].sc[biz_a].f7206_line4"
    value: "231.42"
    work: "Net profit of biz_a"
  - printed: "person[taxpayer].sc[biz_a].f7206_line5"
    value: "231.42"
    work: "Only net profit; biz_b loss excluded"
  - printed: "person[taxpayer].sc[biz_a].f7206_has"
    value: "yes"
    work: "231.42 > 0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line7_pos"
    value: "0.00"
    work: "Sch 1 line 15 is 0 (combined SE earnings negative) x 1.0"
  - printed: "person[taxpayer].sc[biz_a].f7206_line7"
    value: "0.00"
    work: "0.00 x 100%"
  - printed: "person[taxpayer].sc[biz_a].f7206_line8"
    value: "231.42"
    work: "231.42 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].f7206_line9_pos"
    value: "0.00"
    work: "No SEP/SIMPLE deduction"
  - printed: "person[taxpayer].sc[biz_a].f7206_line9"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_a].f7206_line10"
    value: "231.42"
    work: "231.42 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].f7206_line13"
    value: "231.42"
    work: "231.42 - 0.00"
  - printed: "person[taxpayer].sc[biz_a].f7206_min"
    value: "231.42"
    work: "Smaller of 3,996.00 or 231.42"
  - printed: "person[taxpayer].sc[biz_a].f7206_line14"
    value: "231.42"
    work: "Smaller of line 3 or line 13"
  - printed: "person[taxpayer].sc[biz_a].qbi_has"
    value: "yes"
    work: "Line 31 = 231.42 > 0"
  - printed: "person[taxpayer].sc[biz_a].qbi_se_pos"
    value: "0.00"
    work: "Sch 1 line 15 is 0.00"
  - printed: "person[taxpayer].sc[biz_a].qbi_se"
    value: "0.00"
    work: "0.00"
  - printed: "person[taxpayer].sc[biz_a].qbi_plan_pos"
    value: "0.00"
    work: "No plan deduction"
  - printed: "person[taxpayer].sc[biz_a].qbi_plan"
    value: "0.00"
    work: "0.00"
  - printed: "person[taxpayer].sc[biz_a].qbi_ded"
    value: "231.42"
    work: "0.00 + 0.00 + 231.42"
  - printed: "person[taxpayer].sc[biz_a].qbi"
    value: "0.00"
    work: "231.42 - 231.42"
  - printed: "person[taxpayer].sc[biz_b].screened"
    value: "no"
    work: "All screening questions answered no"
  - printed: "person[taxpayer].sc[biz_b].line3"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].line4"
    value: "0.00"
    work: "From line 42"
  - printed: "person[taxpayer].sc[biz_b].line5"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].line7"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].line9"
    value: "13157.00"
    work: "6,178.00 + 6,979.00"
  - printed: "person[taxpayer].sc[biz_b].line12"
    value: "0.00"
    work: "No depletion"
  - printed: "person[taxpayer].sc[biz_b].line13"
    value: "14.29"
    work: "Section 179 0.00 + other depreciation 14.29"
  - printed: "person[taxpayer].sc[biz_b].line20a"
    value: "0.00"
    work: "0.00 + 0.00 vehicle lease"
  - printed: "person[taxpayer].sc[biz_b].meals_50_ded"
    value: "0.00"
    work: "50% x 0.00"
  - printed: "person[taxpayer].sc[biz_b].meals_80_ded"
    value: "0.00"
    work: "80% x 0.00"
  - printed: "person[taxpayer].sc[biz_b].line24b"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].line27a"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].line27b"
    value: "0.00"
    work: "From line 48"
  - printed: "person[taxpayer].sc[biz_b].line28"
    value: "29876.29"
    work: "13,157.00 + 14.29 + 16,705.00"
  - printed: "person[taxpayer].sc[biz_b].line29"
    value: "-29876.29"
    work: "0.00 - 29,876.29"
  - printed: "person[taxpayer].sc[biz_b].line28_pre179"
    value: "29876.29"
    work: "Section 179 is 0.00"
  - printed: "person[taxpayer].sc[biz_b].line29_pre179"
    value: "-29876.29"
    work: "0.00 - 29,876.29"
  - printed: "person[taxpayer].sc[biz_b].ho_screened"
    value: "no"
    work: "No home office claimed"
  - printed: "person[taxpayer].sc[biz_b].ho_over"
    value: "no"
    work: "0 sq ft"
  - printed: "person[taxpayer].sc[biz_b].ho_line4_actual"
    value: "0.00"
    work: "0 x 5.00"
  - printed: "person[taxpayer].sc[biz_b].ho_line4_cap"
    value: "1500.00"
    work: "300 x 5.00"
  - printed: "person[taxpayer].sc[biz_b].ho_line4"
    value: "0.00"
    work: "0 sq ft x 5.00"
  - printed: "person[taxpayer].sc[biz_b].ho_line1"
    value: "-29876.29"
    work: "Schedule C line 29"
  - printed: "person[taxpayer].sc[biz_b].ho_room"
    value: "-29876.29"
    work: "-29,876.29 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].ho_unlimited"
    value: "no"
    work: "0.00 > -29,876.29"
  - printed: "person[taxpayer].sc[biz_b].ho_s179_max"
    value: "0.00"
    work: "Elected 0.00 + carryover 0.00"
  - printed: "person[taxpayer].sc[biz_b].ho_no179"
    value: "yes"
    work: "No election and no carryover"
  - printed: "person[taxpayer].sc[biz_b].ho_limited"
    value: "0.00"
    work: "Smaller of -29,876.29 or 0.00; if zero or less enter -0-"
  - printed: "person[taxpayer].sc[biz_b].ho_pre179_floor"
    value: "0.00"
    work: "-29,876.29 floored at 0"
  - printed: "person[taxpayer].sc[biz_b].ho_both_limits"
    value: "no"
    work: "No section 179 possible"
  - printed: "person[taxpayer].sc[biz_b].ho_both"
    value: "0.00"
    work: "Not applicable"
  - printed: "person[taxpayer].sc[biz_b].ho_line5_lim"
    value: "0.00"
    work: "Not applicable"
  - printed: "person[taxpayer].sc[biz_b].ho_line5"
    value: "0.00"
    work: "Smaller of line 1 or 0.00; floor 0"
  - printed: "person[taxpayer].sc[biz_b].line30"
    value: "0.00"
    work: "No home office deduction"
  - printed: "person[taxpayer].sc[biz_b].line31"
    value: "-29876.29"
    work: "-29,876.29 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].line31_pre179"
    value: "-29876.29"
    work: "-29,876.29 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].loss"
    value: "yes"
    work: "Line 31 < 0"
  - printed: "person[taxpayer].sc[biz_b].not_at_risk"
    value: "no"
    work: "Box 32a, all investment at risk"
  - printed: "person[taxpayer].sc[biz_b].loss_allowed"
    value: "-29876.29"
    work: "All at risk, material participation yes"
  - printed: "person[taxpayer].sc[biz_b].result"
    value: "-29876.29"
    work: "Line 31"
  - printed: "person[taxpayer].sc[biz_b].line40"
    value: "0.00"
    work: "All lines 35-39 are 0"
  - printed: "person[taxpayer].sc[biz_b].line42"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].f6"
    value: "0.00"
    work: "Elected 0.00"
  - printed: "person[taxpayer].sc[biz_b].f14"
    value: "0.00"
    work: "Special allowance 0.00"
  - printed: "person[taxpayer].sc[biz_b].f17"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y3"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y5"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y7"
    value: "14.29"
    work: "Item_1, 7-year property"
  - printed: "person[taxpayer].sc[biz_b].f19_y10"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y15"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y20"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f19_y15sl"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f25_assets"
    value: "0.00"
    work: "No listed property"
  - printed: "person[taxpayer].sc[biz_b].f25_veh"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].f25"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].f26_assets"
    value: "0.00"
    work: "Asset is not listed property"
  - printed: "person[taxpayer].sc[biz_b].f26_veh"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].f26h"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].f28"
    value: "0.00"
    work: "Line 25 + line 26 = 0.00"
  - printed: "person[taxpayer].sc[biz_b].f29_assets"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f29_veh"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].f29"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].s179_elected"
    value: "0.00"
    work: "f6 0.00 + f29 0.00"
  - printed: "person[taxpayer].sc[biz_b].dep_other"
    value: "14.29"
    work: "0 + 0 + 14.29 + 0"
  - printed: "person[taxpayer].sc[biz_b].s179_return"
    value: "0.00"
    work: "Form 4562 line 12 = 0.00"
  - printed: "person[taxpayer].sc[biz_b].s179_allowed"
    value: "0.00"
    work: "Return total is 0.00"
  - printed: "person[taxpayer].sc[biz_b].mq_q4_a"
    value: "100.00"
    work: "Item_1"
  - printed: "person[taxpayer].sc[biz_b].mq_q4_v"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].mq_q4"
    value: "100.00"
    work: "100.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].mq_total_a"
    value: "100.00"
    work: "Item_1"
  - printed: "person[taxpayer].sc[biz_b].mq_total_v"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].mq_total"
    value: "100.00"
    work: "100.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].cost179_a"
    value: "100.00"
    work: "Item_1"
  - printed: "person[taxpayer].sc[biz_b].cost179_v"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].cost179"
    value: "100.00"
    work: "100.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].veh_lease"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].profit_pos"
    value: "0.00"
    work: "Line 31 is a loss"
  - printed: "person[taxpayer].sc[biz_b].hi_screened"
    value: "no"
    work: "Answered no"
  - printed: "person[taxpayer].sc[biz_b].f7206_line2"
    value: "0.00"
    work: "No plan under this business"
  - printed: "person[taxpayer].sc[biz_b].f7206_line3"
    value: "0.00"
    work: "0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].f7206_line4"
    value: "0.00"
    work: "Net loss, not more than zero"
  - printed: "person[taxpayer].sc[biz_b].f7206_line5"
    value: "231.42"
    work: "Total net profits (biz_a only)"
  - printed: "person[taxpayer].sc[biz_b].f7206_has"
    value: "no"
    work: "Line 4 is 0"
  - printed: "person[taxpayer].sc[biz_b].f7206_line7_pos"
    value: "0.00"
    work: "0.00 x 0/231.42"
  - printed: "person[taxpayer].sc[biz_b].f7206_line7"
    value: "0.00"
    work: "Line 4 is zero"
  - printed: "person[taxpayer].sc[biz_b].f7206_line8"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].f7206_line9_pos"
    value: "0.00"
    work: "No plan deduction"
  - printed: "person[taxpayer].sc[biz_b].f7206_line9"
    value: "0.00"
    work: "None"
  - printed: "person[taxpayer].sc[biz_b].f7206_line10"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].f7206_line13"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "person[taxpayer].sc[biz_b].f7206_min"
    value: "0.00"
    work: "Smaller of 0.00 or 0.00"
  - printed: "person[taxpayer].sc[biz_b].f7206_line14"
    value: "0.00"
    work: "No health plan under this business"
  - printed: "person[taxpayer].sc[biz_b].qbi_has"
    value: "no"
    work: "Line 31 is a loss"
  - printed: "person[taxpayer].sc[biz_b].qbi_se_pos"
    value: "0.00"
    work: "No net profit"
  - printed: "person[taxpayer].sc[biz_b].qbi_se"
    value: "0.00"
    work: "No net profit"
  - printed: "person[taxpayer].sc[biz_b].qbi_plan_pos"
    value: "0.00"
    work: "No net profit"
  - printed: "person[taxpayer].sc[biz_b].qbi_plan"
    value: "0.00"
    work: "No net profit"
  - printed: "person[taxpayer].sc[biz_b].qbi_ded"
    value: "0.00"
    work: "0.00 + 0.00 + 0.00"
  - printed: "person[taxpayer].sc[biz_b].qbi"
    value: "-29876.29"
    work: "-29,876.29 - 0.00"
```
```
