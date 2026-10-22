# Class M hand-work — retirement

`Form 1099-R distributions (IRAs, pensions and annuities)` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-20 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | 77d496440f63c929553c3a813b35987e945df63bb75851e61c24bd95607f31bb |
| cases | 3 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099r | 2025 (calendar-year form) | - | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | - | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| i1040gi | 2025; printed date 2026-02-25 | 26, 27, 28, 29, 30, 31 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 26, 27, 28, 30, 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.retirement.1 — prompt sha256 9260d80f8ea0fdf818afb67422ed572f16b48ff2677234bbf6d34bd14b97bec6; branches: retirement.special:false, retirement.annuity:false, retirement.annuity:true, retirement.used_last_year:false, retirement.used_last_year:true, retirement.joint_life:false, retirement.joint_life:true, retirement.is_ira:false, retirement.is_ira:true, retirement.roth:false, retirement.direct:false, retirement.direct:true, retirement.bad_code:false, retirement.rolled#0, retirement.rolled#1, retirement.has_rollover:false, retirement.has_rollover:true, retirement.smw4_table1#0, retirement.smw4_table1#4, retirement.smw4_table2#0, retirement.smw4_table2#4, retirement.smw4_new#0, retirement.smw4_new#1, retirement.smw4#0, retirement.smw4#1, retirement.smw8:left, retirement.smw8:right, retirement.smw9:positive, retirement.cost_left:false, retirement.cost_left:true, retirement.annuity_with_cost:false, retirement.annuity_with_cost:true, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.annuity_taxable#1, retirement.ira_taxable#1, retirement.ira_not_rolled:floor, retirement.ira_not_rolled:positive, retirement.plan_simple:floor, retirement.plan_simple:positive, retirement.plan_taxable#0, retirement.plan_taxable#1, retirement.taxable#0, retirement.taxable#1, retirement.show_a:true, retirement.amount_a#0

### classm.retirement.1 — retirement[r1].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r1].roth — Roth IRA distribution
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r1].direct — Direct rollover (code G)
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r1].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r1].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r1].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $40,529.00

### classm.retirement.1 — retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $41,291.00

### classm.retirement.1 — retirement[r1].smw4_t1_360 — Line 2 divided by 360 (Table 1)
Status: **AGREE**

Value: $114.70

### classm.retirement.1 — retirement[r1].smw4_t1_310 — Line 2 divided by 310 (Table 1)
Status: **AGREE**

Value: $133.20

### classm.retirement.1 — retirement[r1].smw4_t1_260 — Line 2 divided by 260 (Table 1)
Status: **AGREE**

Value: $158.81

### classm.retirement.1 — retirement[r1].smw4_t1_210 — Line 2 divided by 210 (Table 1)
Status: **AGREE**

Value: $196.62

### classm.retirement.1 — retirement[r1].smw4_t1_160 — Line 2 divided by 160 (Table 1)
Status: **AGREE**

Value: $258.07

### classm.retirement.1 — retirement[r1].smw4_t2_410 — Line 2 divided by 410 (Table 2)
Status: **AGREE**

Value: $100.71

### classm.retirement.1 — retirement[r1].smw4_t2_360 — Line 2 divided by 360 (Table 2)
Status: **AGREE**

Value: $114.70

### classm.retirement.1 — retirement[r1].smw4_t2_310 — Line 2 divided by 310 (Table 2)
Status: **AGREE**

Value: $133.20

### classm.retirement.1 — retirement[r1].smw4_t2_260 — Line 2 divided by 260 (Table 2)
Status: **AGREE**

Value: $158.81

### classm.retirement.1 — retirement[r1].smw4_t2_210 — Line 2 divided by 210 (Table 2)
Status: **AGREE**

Value: $196.62

### classm.retirement.1 — retirement[r1].smw4_table1 — Line 2 divided by the Table 1 number for the age at the annuity starting date
Status: **AGREE**

Value: $258.07

### classm.retirement.1 — retirement[r1].smw4_table2 — Line 2 divided by the Table 2 number for the combined ages at the annuity starti
Status: **AGREE**

Value: $196.62

### classm.retirement.1 — retirement[r1].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $196.62

### classm.retirement.1 — retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $26,155.00

### classm.retirement.1 — retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $15,136.00

### classm.retirement.1 — retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $40,529.00

### classm.retirement.1 — retirement[r1].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $26,155.00

### classm.retirement.1 — retirement[r1].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $15,136.00

### classm.retirement.1 — retirement[r1].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: yes

### classm.retirement.1 — retirement[r1].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: yes

### classm.retirement.1 — retirement[r1].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r1].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $40,529.00

### classm.retirement.1 — retirement[r1].ira_taxable — Taxable IRA amount: the part not rolled over (zero for a qualified Roth IRA dist
Status: **AGREE**

Value: $40,529.00

### classm.retirement.1 — retirement[r1].ira_not_rolled — Box 1 less the amount rolled over
Status: **AGREE**

Value: $40,529.00

### classm.retirement.1 — retirement[r1].plan_excluded — Taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r1].plan_simple — Box 1 less taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $40,529.00

### classm.retirement.1 — retirement[r1].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $40,529.00

### classm.retirement.1 — retirement[r1].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $40,529.00

### classm.retirement.1 — retirement[r1].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: yes

### classm.retirement.1 — retirement[r1].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $40,529.00

### classm.retirement.1 — retirement[r2].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: yes

### classm.retirement.1 — retirement[r2].roth — Roth IRA distribution
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r2].direct — Direct rollover (code G)
Status: **AGREE**

Value: yes

### classm.retirement.1 — retirement[r2].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r2].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $14,514.00

### classm.retirement.1 — retirement[r2].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: yes

### classm.retirement.1 — retirement[r2].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $14,514.00

### classm.retirement.1 — retirement[r2].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw4_t1_360 — Line 2 divided by 360 (Table 1)
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw4_t1_310 — Line 2 divided by 310 (Table 1)
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw4_t1_260 — Line 2 divided by 260 (Table 1)
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw4_t1_210 — Line 2 divided by 210 (Table 1)
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw4_t1_160 — Line 2 divided by 160 (Table 1)
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw4_t2_410 — Line 2 divided by 410 (Table 2)
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw4_t2_360 — Line 2 divided by 360 (Table 2)
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw4_t2_310 — Line 2 divided by 310 (Table 2)
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw4_t2_260 — Line 2 divided by 260 (Table 2)
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw4_t2_210 — Line 2 divided by 210 (Table 2)
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw4_table1 — Line 2 divided by the Table 1 number for the age at the annuity starting date
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw4_table2 — Line 2 divided by the Table 2 number for the combined ages at the annuity starti
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $15,016.00

### classm.retirement.1 — retirement[r2].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $-15,016.00

### classm.retirement.1 — retirement[r2].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $-15,016.00

### classm.retirement.1 — retirement[r2].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $29,530.00

### classm.retirement.1 — retirement[r2].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r2].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r2].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r2].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $14,514.00

### classm.retirement.1 — retirement[r2].ira_taxable — Taxable IRA amount: the part not rolled over (zero for a qualified Roth IRA dist
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].ira_not_rolled — Box 1 less the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].plan_excluded — Taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $14,514.00

### classm.retirement.1 — retirement[r2].plan_simple — Box 1 less taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: yes

### classm.retirement.1 — retirement[r2].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $14,514.00

### case classm.retirement.2 — prompt sha256 fa789980f68b29119fbacbc9e34b1ca57b69853dad83a29083d8de2a151ab655; branches: retirement.special:false, retirement.annuity:false, retirement.used_last_year:true, retirement.joint_life:false, retirement.is_ira:false, retirement.is_ira:true, retirement.roth:false, retirement.roth:true, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw4_table1#1, retirement.smw4_table1#3, retirement.smw4_table2#1, retirement.smw4_new#1, retirement.smw4#0, retirement.smw8:left, retirement.smw8:right, retirement.smw9:floor, retirement.smw9:positive, retirement.cost_left:false, retirement.cost_left:true, retirement.annuity_with_cost:false, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.annuity_taxable#1, retirement.ira_taxable#0, retirement.ira_taxable#1, retirement.ira_not_rolled:floor, retirement.plan_simple:floor, retirement.plan_taxable#1, retirement.taxable#0, retirement.taxable#1, retirement.show_a:false, retirement.show_a:true, retirement.amount_a#0, retirement.amount_a#1

### classm.retirement.2 — retirement[r1].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r1].roth — Roth IRA distribution
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r1].direct — Direct rollover (code G)
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r1].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r1].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $200,000.00

### classm.retirement.2 — retirement[r1].smw4_t1_360 — Line 2 divided by 360 (Table 1)
Status: **AGREE**

Value: $555.56

### classm.retirement.2 — retirement[r1].smw4_t1_310 — Line 2 divided by 310 (Table 1)
Status: **AGREE**

Value: $645.16

### classm.retirement.2 — retirement[r1].smw4_t1_260 — Line 2 divided by 260 (Table 1)
Status: **AGREE**

Value: $769.23

### classm.retirement.2 — retirement[r1].smw4_t1_210 — Line 2 divided by 210 (Table 1)
Status: **AGREE**

Value: $952.38

### classm.retirement.2 — retirement[r1].smw4_t1_160 — Line 2 divided by 160 (Table 1)
Status: **AGREE**

Value: $1,250.00

### classm.retirement.2 — retirement[r1].smw4_t2_410 — Line 2 divided by 410 (Table 2)
Status: **AGREE**

Value: $487.80

### classm.retirement.2 — retirement[r1].smw4_t2_360 — Line 2 divided by 360 (Table 2)
Status: **AGREE**

Value: $555.56

### classm.retirement.2 — retirement[r1].smw4_t2_310 — Line 2 divided by 310 (Table 2)
Status: **AGREE**

Value: $645.16

### classm.retirement.2 — retirement[r1].smw4_t2_260 — Line 2 divided by 260 (Table 2)
Status: **AGREE**

Value: $769.23

### classm.retirement.2 — retirement[r1].smw4_t2_210 — Line 2 divided by 210 (Table 2)
Status: **AGREE**

Value: $952.38

### classm.retirement.2 — retirement[r1].smw4_table1 — Line 2 divided by the Table 1 number for the age at the annuity starting date
Status: **AGREE**

Value: $645.16

### classm.retirement.2 — retirement[r1].smw4_table2 — Line 2 divided by the Table 2 number for the combined ages at the annuity starti
Status: **AGREE**

Value: $555.56

### classm.retirement.2 — retirement[r1].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $645.16

### classm.retirement.2 — retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $200,000.00

### classm.retirement.2 — retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $200,000.00

### classm.retirement.2 — retirement[r1].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: yes

### classm.retirement.2 — retirement[r1].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r1].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r1].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].ira_taxable — Taxable IRA amount: the part not rolled over (zero for a qualified Roth IRA dist
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].ira_not_rolled — Box 1 less the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].plan_excluded — Taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].plan_simple — Box 1 less taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r1].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: yes

### classm.retirement.2 — retirement[r2].roth — Roth IRA distribution
Status: **AGREE**

Value: yes

### classm.retirement.2 — retirement[r2].direct — Direct rollover (code G)
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r2].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r2].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r2].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].smw4_t1_360 — Line 2 divided by 360 (Table 1)
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].smw4_t1_310 — Line 2 divided by 310 (Table 1)
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].smw4_t1_260 — Line 2 divided by 260 (Table 1)
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].smw4_t1_210 — Line 2 divided by 210 (Table 1)
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].smw4_t1_160 — Line 2 divided by 160 (Table 1)
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].smw4_t2_410 — Line 2 divided by 410 (Table 2)
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].smw4_t2_360 — Line 2 divided by 360 (Table 2)
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].smw4_t2_310 — Line 2 divided by 310 (Table 2)
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].smw4_t2_260 — Line 2 divided by 260 (Table 2)
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].smw4_t2_210 — Line 2 divided by 210 (Table 2)
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].smw4_table1 — Line 2 divided by the Table 1 number for the age at the annuity starting date
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].smw4_table2 — Line 2 divided by the Table 2 number for the combined ages at the annuity starti
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $624.00

### classm.retirement.2 — retirement[r2].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $7,488.00

### classm.retirement.2 — retirement[r2].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $35,342.00

### classm.retirement.2 — retirement[r2].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $-35,342.00

### classm.retirement.2 — retirement[r2].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $-35,342.00

### classm.retirement.2 — retirement[r2].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $35,342.00

### classm.retirement.2 — retirement[r2].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r2].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r2].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r2].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].ira_taxable — Taxable IRA amount: the part not rolled over (zero for a qualified Roth IRA dist
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].ira_not_rolled — Box 1 less the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].plan_excluded — Taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].plan_simple — Box 1 less taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: yes

### classm.retirement.2 — retirement[r2].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $0.00

### case classm.retirement.3 — prompt sha256 88b93a79c0dbd6197a2e43aaa5e5a361a4571f34e13cdcba76bfb36b5e8bfe1a; branches: retirement.special:false, retirement.annuity:false, retirement.used_last_year:false, retirement.used_last_year:true, retirement.joint_life:false, retirement.joint_life:true, retirement.is_ira:true, retirement.roth:false, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw4_table1#2, retirement.smw4_table2#2, retirement.smw4_table2#3, retirement.smw4_new#0, retirement.smw4_new#1, retirement.smw4#0, retirement.smw4#1, retirement.smw8:left, retirement.smw8:right, retirement.smw9:floor, retirement.smw9:positive, retirement.cost_left:true, retirement.annuity_with_cost:false, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.ira_taxable#1, retirement.ira_not_rolled:floor, retirement.ira_not_rolled:positive, retirement.plan_simple:floor, retirement.plan_simple:positive, retirement.plan_taxable#1, retirement.taxable#0, retirement.show_a:false, retirement.amount_a#1

### classm.retirement.3 — retirement[r1].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: yes

### classm.retirement.3 — retirement[r1].roth — Roth IRA distribution
Status: **AGREE**

Value: no

### classm.retirement.3 — retirement[r1].direct — Direct rollover (code G)
Status: **AGREE**

Value: no

### classm.retirement.3 — retirement[r1].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.3 — retirement[r1].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r1].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: no

### classm.retirement.3 — retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $4,653.00

### classm.retirement.3 — retirement[r1].smw4_t1_360 — Line 2 divided by 360 (Table 1)
Status: **AGREE**

Value: $12.93

### classm.retirement.3 — retirement[r1].smw4_t1_310 — Line 2 divided by 310 (Table 1)
Status: **AGREE**

Value: $15.01

### classm.retirement.3 — retirement[r1].smw4_t1_260 — Line 2 divided by 260 (Table 1)
Status: **AGREE**

Value: $17.90

### classm.retirement.3 — retirement[r1].smw4_t1_210 — Line 2 divided by 210 (Table 1)
Status: **AGREE**

Value: $22.16

### classm.retirement.3 — retirement[r1].smw4_t1_160 — Line 2 divided by 160 (Table 1)
Status: **AGREE**

Value: $29.08

### classm.retirement.3 — retirement[r1].smw4_t2_410 — Line 2 divided by 410 (Table 2)
Status: **AGREE**

Value: $11.35

### classm.retirement.3 — retirement[r1].smw4_t2_360 — Line 2 divided by 360 (Table 2)
Status: **AGREE**

Value: $12.93

### classm.retirement.3 — retirement[r1].smw4_t2_310 — Line 2 divided by 310 (Table 2)
Status: **AGREE**

Value: $15.01

### classm.retirement.3 — retirement[r1].smw4_t2_260 — Line 2 divided by 260 (Table 2)
Status: **AGREE**

Value: $17.90

### classm.retirement.3 — retirement[r1].smw4_t2_210 — Line 2 divided by 210 (Table 2)
Status: **AGREE**

Value: $22.16

### classm.retirement.3 — retirement[r1].smw4_table1 — Line 2 divided by the Table 1 number for the age at the annuity starting date
Status: **AGREE**

Value: $17.90

### classm.retirement.3 — retirement[r1].smw4_table2 — Line 2 divided by the Table 2 number for the combined ages at the annuity starti
Status: **AGREE**

Value: $15.01

### classm.retirement.3 — retirement[r1].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $17.90

### classm.retirement.3 — retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $1,925.00

### classm.retirement.3 — retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $5,775.00

### classm.retirement.3 — retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $4,653.00

### classm.retirement.3 — retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $4,653.00

### classm.retirement.3 — retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r1].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $4,653.00

### classm.retirement.3 — retirement[r1].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r1].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: yes

### classm.retirement.3 — retirement[r1].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: no

### classm.retirement.3 — retirement[r1].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.3 — retirement[r1].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r1].ira_taxable — Taxable IRA amount: the part not rolled over (zero for a qualified Roth IRA dist
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r1].ira_not_rolled — Box 1 less the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r1].plan_excluded — Taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r1].plan_simple — Box 1 less taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r1].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r1].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r1].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: no

### classm.retirement.3 — retirement[r1].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r2].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: yes

### classm.retirement.3 — retirement[r2].roth — Roth IRA distribution
Status: **AGREE**

Value: no

### classm.retirement.3 — retirement[r2].direct — Direct rollover (code G)
Status: **AGREE**

Value: no

### classm.retirement.3 — retirement[r2].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.3 — retirement[r2].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r2].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: no

### classm.retirement.3 — retirement[r2].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $27,508.00

### classm.retirement.3 — retirement[r2].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $51,447.00

### classm.retirement.3 — retirement[r2].smw4_t1_360 — Line 2 divided by 360 (Table 1)
Status: **AGREE**

Value: $142.91

### classm.retirement.3 — retirement[r2].smw4_t1_310 — Line 2 divided by 310 (Table 1)
Status: **AGREE**

Value: $165.96

### classm.retirement.3 — retirement[r2].smw4_t1_260 — Line 2 divided by 260 (Table 1)
Status: **AGREE**

Value: $197.87

### classm.retirement.3 — retirement[r2].smw4_t1_210 — Line 2 divided by 210 (Table 1)
Status: **AGREE**

Value: $244.99

### classm.retirement.3 — retirement[r2].smw4_t1_160 — Line 2 divided by 160 (Table 1)
Status: **AGREE**

Value: $321.54

### classm.retirement.3 — retirement[r2].smw4_t2_410 — Line 2 divided by 410 (Table 2)
Status: **AGREE**

Value: $125.48

### classm.retirement.3 — retirement[r2].smw4_t2_360 — Line 2 divided by 360 (Table 2)
Status: **AGREE**

Value: $142.91

### classm.retirement.3 — retirement[r2].smw4_t2_310 — Line 2 divided by 310 (Table 2)
Status: **AGREE**

Value: $165.96

### classm.retirement.3 — retirement[r2].smw4_t2_260 — Line 2 divided by 260 (Table 2)
Status: **AGREE**

Value: $197.87

### classm.retirement.3 — retirement[r2].smw4_t2_210 — Line 2 divided by 210 (Table 2)
Status: **AGREE**

Value: $244.99

### classm.retirement.3 — retirement[r2].smw4_table1 — Line 2 divided by the Table 1 number for the age at the annuity starting date
Status: **AGREE**

Value: $197.87

### classm.retirement.3 — retirement[r2].smw4_table2 — Line 2 divided by the Table 2 number for the combined ages at the annuity starti
Status: **AGREE**

Value: $197.87

### classm.retirement.3 — retirement[r2].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $197.87

### classm.retirement.3 — retirement[r2].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $197.87

### classm.retirement.3 — retirement[r2].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $2,374.44

### classm.retirement.3 — retirement[r2].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $7,061.00

### classm.retirement.3 — retirement[r2].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $44,386.00

### classm.retirement.3 — retirement[r2].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $2,374.44

### classm.retirement.3 — retirement[r2].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $25,133.56

### classm.retirement.3 — retirement[r2].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $9,435.44

### classm.retirement.3 — retirement[r2].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $42,011.56

### classm.retirement.3 — retirement[r2].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: yes

### classm.retirement.3 — retirement[r2].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: no

### classm.retirement.3 — retirement[r2].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.3 — retirement[r2].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **DISAGREE**

Project: $25,133.56
Model: $27,508.00
Work: Simplified Method not used; whole box 1

Ruling: helper of a branch this entry does not take; project retained. The entry is a traditional IRA distribution (retirement.annuity is false), whose taxable amount is the IRA route's figure, $27,508.00 (retirement.taxable, which agrees); the Simplified Method helper is figured for every entry but read only for an annuity with cost. Dropped from the fixture as not evidence. [dropped]

### classm.retirement.3 — retirement[r2].ira_taxable — Taxable IRA amount: the part not rolled over (zero for a qualified Roth IRA dist
Status: **AGREE**

Value: $27,508.00

### classm.retirement.3 — retirement[r2].ira_not_rolled — Box 1 less the amount rolled over
Status: **AGREE**

Value: $27,508.00

### classm.retirement.3 — retirement[r2].plan_excluded — Taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r2].plan_simple — Box 1 less taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $27,508.00

### classm.retirement.3 — retirement[r2].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $27,508.00

### classm.retirement.3 — retirement[r2].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $27,508.00

### classm.retirement.3 — retirement[r2].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: no

### classm.retirement.3 — retirement[r2].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.retirement.1

```yaml
```yaml
lines:
  - printed: "retirement[r1].is_ira"
    value: "no"
    work: "Account kind is plan, so it goes on lines 5a/5b"
  - printed: "retirement[r1].roth"
    value: "no"
    work: "Not a Roth account"
  - printed: "retirement[r1].direct"
    value: "no"
    work: "Box 7 code is 7, not G"
  - printed: "retirement[r1].bad_code"
    value: "no"
    work: "Code 7 (normal) is handled; filer answered no to all listed special situations"
  - printed: "retirement[r1].rolled"
    value: "0.00"
    work: "No amount rolled over and not a direct rollover"
  - printed: "retirement[r1].has_rollover"
    value: "no"
    work: "Rolled over 0 and not code G"
  - printed: "retirement[r1].smw1"
    value: "40529.00"
    work: "Box 1"
  - printed: "retirement[r1].smw2"
    value: "41291.00"
    work: "Cost in plan at annuity starting date"
  - printed: "retirement[r1].smw4_t1_360"
    value: "114.70"
    work: "41291 / 360"
  - printed: "retirement[r1].smw4_t1_310"
    value: "133.20"
    work: "41291 / 310"
  - printed: "retirement[r1].smw4_t1_260"
    value: "158.81"
    work: "41291 / 260"
  - printed: "retirement[r1].smw4_t1_210"
    value: "196.62"
    work: "41291 / 210"
  - printed: "retirement[r1].smw4_t1_160"
    value: "258.07"
    work: "41291 / 160"
  - printed: "retirement[r1].smw4_t2_410"
    value: "100.71"
    work: "41291 / 410"
  - printed: "retirement[r1].smw4_t2_360"
    value: "114.70"
    work: "41291 / 360"
  - printed: "retirement[r1].smw4_t2_310"
    value: "133.20"
    work: "41291 / 310"
  - printed: "retirement[r1].smw4_t2_260"
    value: "158.81"
    work: "41291 / 260"
  - printed: "retirement[r1].smw4_t2_210"
    value: "196.62"
    work: "41291 / 210"
  - printed: "retirement[r1].smw4_table1"
    value: "258.07"
    work: "Age 73 (71 or older, after 11/18/1996) gives 160; 41291 / 160"
  - printed: "retirement[r1].smw4_table2"
    value: "196.62"
    work: "Combined ages 149 (141 or older) gives 210; 41291 / 210"
  - printed: "retirement[r1].smw4_new"
    value: "196.62"
    work: "Joint and survivor annuity starting after 1997, so Table 2"
  - printed: "retirement[r1].smw4"
    value: "0.00"
    work: "Worksheet completed last year, so skip line 3 and use last year's line 4 = 0.00"
  - printed: "retirement[r1].smw5"
    value: "0.00"
    work: "0.00 x 12"
  - printed: "retirement[r1].smw6"
    value: "26155.00"
    work: "Line 10 of last year's worksheet"
  - printed: "retirement[r1].smw7"
    value: "15136.00"
    work: "41291 - 26155"
  - printed: "retirement[r1].smw8"
    value: "0.00"
    work: "Smaller of 0.00 or 15136.00"
  - printed: "retirement[r1].smw9"
    value: "40529.00"
    work: "40529 - 0"
  - printed: "retirement[r1].smw10"
    value: "26155.00"
    work: "26155 + 0"
  - printed: "retirement[r1].smw11"
    value: "15136.00"
    work: "41291 - 26155"
  - printed: "retirement[r1].cost_left"
    value: "yes"
    work: "Line 7 = 15136 > 0"
  - printed: "retirement[r1].annuity_with_cost"
    value: "yes"
    work: "Simplified Method applies and line 7 > 0"
  - printed: "retirement[r1].annuity_rollover"
    value: "no"
    work: "Nothing rolled over"
  - printed: "retirement[r1].annuity_taxable"
    value: "40529.00"
    work: "Simplified Method line 9"
  - printed: "retirement[r1].ira_taxable"
    value: "40529.00"
    work: "Part not rolled over (40529 - 0); not a Roth"
  - printed: "retirement[r1].ira_not_rolled"
    value: "40529.00"
    work: "40529 - 0"
  - printed: "retirement[r1].plan_excluded"
    value: "0.00"
    work: "Box 5 (0) + rolled over (0)"
  - printed: "retirement[r1].plan_simple"
    value: "40529.00"
    work: "40529 - 0 - 0"
  - printed: "retirement[r1].plan_taxable"
    value: "40529.00"
    work: "Annuity with cost, so Simplified Method line 9"
  - printed: "retirement[r1].taxable"
    value: "40529.00"
    work: "Pension: plan_taxable goes on line 5b"
  - printed: "retirement[r1].show_a"
    value: "yes"
    work: "Partially taxable annuity: worksheet line 1 is entered on line 5a"
  - printed: "retirement[r1].amount_a"
    value: "40529.00"
    work: "Box 1 total on line 5a"
  - printed: "retirement[r2].is_ira"
    value: "yes"
    work: "Traditional IRA, so lines 4a/4b"
  - printed: "retirement[r2].roth"
    value: "no"
    work: "Traditional IRA, not Roth"
  - printed: "retirement[r2].direct"
    value: "yes"
    work: "Box 7 code G"
  - printed: "retirement[r2].bad_code"
    value: "no"
    work: "Code G is handled; no special situations"
  - printed: "retirement[r2].rolled"
    value: "14514.00"
    work: "Direct rollover, so the whole distribution"
  - printed: "retirement[r2].has_rollover"
    value: "yes"
    work: "Code G and amount rolled over 14514"
  - printed: "retirement[r2].smw1"
    value: "14514.00"
    work: "Box 1"
  - printed: "retirement[r2].smw2"
    value: "0.00"
    work: "Cost given as 0"
  - printed: "retirement[r2].smw4_t1_360"
    value: "0.00"
    work: "0 / 360"
  - printed: "retirement[r2].smw4_t1_310"
    value: "0.00"
    work: "0 / 310"
  - printed: "retirement[r2].smw4_t1_260"
    value: "0.00"
    work: "0 / 260"
  - printed: "retirement[r2].smw4_t1_210"
    value: "0.00"
    work: "0 / 210"
  - printed: "retirement[r2].smw4_t1_160"
    value: "0.00"
    work: "0 / 160"
  - printed: "retirement[r2].smw4_t2_410"
    value: "0.00"
    work: "0 / 410"
  - printed: "retirement[r2].smw4_t2_360"
    value: "0.00"
    work: "0 / 360"
  - printed: "retirement[r2].smw4_t2_310"
    value: "0.00"
    work: "0 / 310"
  - printed: "retirement[r2].smw4_t2_260"
    value: "0.00"
    work: "0 / 260"
  - printed: "retirement[r2].smw4_t2_210"
    value: "0.00"
    work: "0 / 210"
  - printed: "retirement[r2].smw4_table1"
    value: "0.00"
    work: "Age 55 (55 or under, after 11/18/1996) gives 360; 0 / 360"
  - printed: "retirement[r2].smw4_table2"
    value: "0.00"
    work: "Combined ages 104 (110 or under) gives 410; 0 / 410"
  - printed: "retirement[r2].smw4_new"
    value: "0.00"
    work: "Not a joint and survivor annuity, so Table 1"
  - printed: "retirement[r2].smw4"
    value: "0.00"
    work: "Not completed last year, so line 2 / line 3 = 0"
  - printed: "retirement[r2].smw5"
    value: "0.00"
    work: "0 x 12"
  - printed: "retirement[r2].smw6"
    value: "15016.00"
    work: "Amount recovered tax free after 1986, as given"
  - printed: "retirement[r2].smw7"
    value: "-15016.00"
    work: "0 - 15016"
  - printed: "retirement[r2].smw8"
    value: "-15016.00"
    work: "Smaller of 0.00 or -15016.00"
  - printed: "retirement[r2].smw9"
    value: "29530.00"
    work: "14514 - (-15016) = 29530, not less than zero"
  - printed: "retirement[r2].smw10"
    value: "0.00"
    work: "15016 + (-15016)"
  - printed: "retirement[r2].smw11"
    value: "0.00"
    work: "0 - 0"
  - printed: "retirement[r2].cost_left"
    value: "no"
    work: "Line 7 = -15016, not more than zero"
  - printed: "retirement[r2].annuity_with_cost"
    value: "no"
    work: "Simplified Method does not apply; no cost left"
  - printed: "retirement[r2].annuity_rollover"
    value: "no"
    work: "Not a Simplified Method annuity"
  - printed: "retirement[r2].annuity_taxable"
    value: "14514.00"
    work: "No cost left to recover, so the whole of box 1"
  - printed: "retirement[r2].ira_taxable"
    value: "0.00"
    work: "Exception 1: total rolled over, so line 4b is -0-"
  - printed: "retirement[r2].ira_not_rolled"
    value: "0.00"
    work: "14514 - 14514"
  - printed: "retirement[r2].plan_excluded"
    value: "14514.00"
    work: "Box 5 (0) + rolled over (14514)"
  - printed: "retirement[r2].plan_simple"
    value: "0.00"
    work: "14514 - 0 - 14514"
  - printed: "retirement[r2].plan_taxable"
    value: "0.00"
    work: "No annuity with cost, so plan_simple"
  - printed: "retirement[r2].taxable"
    value: "0.00"
    work: "IRA: ira_taxable goes on line 4b"
  - printed: "retirement[r2].show_a"
    value: "yes"
    work: "Exception 1 (rollover): total distribution goes on line 4a"
  - printed: "retirement[r2].amount_a"
    value: "14514.00"
    work: "Box 1 total on line 4a"
```
```

### classm.retirement.2

```yaml
```yaml
lines:
  - printed: "retirement[r1].is_ira"
    value: "no"
    work: "Account kind is plan, not an IRA, so it goes on lines 5a/5b"
  - printed: "retirement[r1].roth"
    value: "no"
    work: "Account kind is plan, not a Roth IRA"
  - printed: "retirement[r1].direct"
    value: "no"
    work: "Box 7 code is 7, not G"
  - printed: "retirement[r1].bad_code"
    value: "no"
    work: "Code 7 (normal distribution) is handled"
  - printed: "retirement[r1].rolled"
    value: "0.00"
    work: "Amount rolled over is $0; not a direct rollover"
  - printed: "retirement[r1].has_rollover"
    value: "no"
    work: "Nothing was rolled over and the code is not G"
  - printed: "retirement[r1].smw1"
    value: "0.00"
    work: "Box 1 = 0.00"
  - printed: "retirement[r1].smw2"
    value: "200000.00"
    work: "Cost at the annuity starting date = 200,000.00"
  - printed: "retirement[r1].smw4_t1_360"
    value: "555.56"
    work: "200,000 / 360"
  - printed: "retirement[r1].smw4_t1_310"
    value: "645.16"
    work: "200,000 / 310"
  - printed: "retirement[r1].smw4_t1_260"
    value: "769.23"
    work: "200,000 / 260"
  - printed: "retirement[r1].smw4_t1_210"
    value: "952.38"
    work: "200,000 / 210"
  - printed: "retirement[r1].smw4_t1_160"
    value: "1250.00"
    work: "200,000 / 160"
  - printed: "retirement[r1].smw4_t2_410"
    value: "487.80"
    work: "200,000 / 410"
  - printed: "retirement[r1].smw4_t2_360"
    value: "555.56"
    work: "200,000 / 360"
  - printed: "retirement[r1].smw4_t2_310"
    value: "645.16"
    work: "200,000 / 310"
  - printed: "retirement[r1].smw4_t2_260"
    value: "769.23"
    work: "200,000 / 260"
  - printed: "retirement[r1].smw4_t2_210"
    value: "952.38"
    work: "200,000 / 210"
  - printed: "retirement[r1].smw4_table1"
    value: "645.16"
    work: "Age 59 falls in 56-60; Table 1 number after 11/18/1996 is 310; 200,000 / 310"
  - printed: "retirement[r1].smw4_table2"
    value: "555.56"
    work: "Combined ages 119 fall in 111-120; Table 2 number is 360; 200,000 / 360"
  - printed: "retirement[r1].smw4_new"
    value: "645.16"
    work: "Not a joint and survivor annuity after 1997, so Table 1 applies"
  - printed: "retirement[r1].smw4"
    value: "0.00"
    work: "Worksheet was completed last year; use last year's line 4 = 0.00"
  - printed: "retirement[r1].smw5"
    value: "0.00"
    work: "0.00 x 12 months"
  - printed: "retirement[r1].smw6"
    value: "0.00"
    work: "Last year's line 10 = 0.00"
  - printed: "retirement[r1].smw7"
    value: "200000.00"
    work: "200,000 - 0"
  - printed: "retirement[r1].smw8"
    value: "0.00"
    work: "Smaller of 0.00 or 200,000"
  - printed: "retirement[r1].smw9"
    value: "0.00"
    work: "0 - 0, not less than zero"
  - printed: "retirement[r1].smw10"
    value: "0.00"
    work: "0 + 0"
  - printed: "retirement[r1].smw11"
    value: "200000.00"
    work: "200,000 - 0"
  - printed: "retirement[r1].cost_left"
    value: "yes"
    work: "Line 7 is 200,000, which is more than zero"
  - printed: "retirement[r1].annuity_with_cost"
    value: "no"
    work: "Filer answered no: the Simplified Method does not apply"
  - printed: "retirement[r1].annuity_rollover"
    value: "no"
    work: "Not a Simplified Method annuity and nothing rolled over"
  - printed: "retirement[r1].annuity_taxable"
    value: "0.00"
    work: "Not a Simplified Method annuity; box 1 = 0"
  - printed: "retirement[r1].ira_taxable"
    value: "0.00"
    work: "Not an IRA distribution"
  - printed: "retirement[r1].ira_not_rolled"
    value: "0.00"
    work: "0 - 0"
  - printed: "retirement[r1].plan_excluded"
    value: "0.00"
    work: "Box 5 (0) + rolled over (0)"
  - printed: "retirement[r1].plan_simple"
    value: "0.00"
    work: "0 - 0 - 0"
  - printed: "retirement[r1].plan_taxable"
    value: "0.00"
    work: "No Simplified Method annuity, so use plan_simple = 0"
  - printed: "retirement[r1].taxable"
    value: "0.00"
    work: "Line 5b = plan taxable amount, 0"
  - printed: "retirement[r1].show_a"
    value: "no"
    work: "No rollover or other exception; fully taxable, so line 5a is left blank"
  - printed: "retirement[r1].amount_a"
    value: "0.00"
    work: "No entry on line 5a"
  - printed: "retirement[r2].is_ira"
    value: "yes"
    work: "Roth IRA distribution goes on lines 4a/4b"
  - printed: "retirement[r2].roth"
    value: "yes"
    work: "Account kind is roth_ira"
  - printed: "retirement[r2].direct"
    value: "no"
    work: "Box 7 code is Q, not G"
  - printed: "retirement[r2].bad_code"
    value: "no"
    work: "Code Q is handled under Exception 2(b)"
  - printed: "retirement[r2].rolled"
    value: "0.00"
    work: "Amount rolled over is $0"
  - printed: "retirement[r2].has_rollover"
    value: "no"
    work: "Nothing was rolled over and the code is not G"
  - printed: "retirement[r2].smw1"
    value: "0.00"
    work: "Box 1 = 0.00"
  - printed: "retirement[r2].smw2"
    value: "0.00"
    work: "Cost = 0.00"
  - printed: "retirement[r2].smw4_t1_360"
    value: "0.00"
    work: "0 / 360"
  - printed: "retirement[r2].smw4_t1_310"
    value: "0.00"
    work: "0 / 310"
  - printed: "retirement[r2].smw4_t1_260"
    value: "0.00"
    work: "0 / 260"
  - printed: "retirement[r2].smw4_t1_210"
    value: "0.00"
    work: "0 / 210"
  - printed: "retirement[r2].smw4_t1_160"
    value: "0.00"
    work: "0 / 160"
  - printed: "retirement[r2].smw4_t2_410"
    value: "0.00"
    work: "0 / 410"
  - printed: "retirement[r2].smw4_t2_360"
    value: "0.00"
    work: "0 / 360"
  - printed: "retirement[r2].smw4_t2_310"
    value: "0.00"
    work: "0 / 310"
  - printed: "retirement[r2].smw4_t2_260"
    value: "0.00"
    work: "0 / 260"
  - printed: "retirement[r2].smw4_t2_210"
    value: "0.00"
    work: "0 / 210"
  - printed: "retirement[r2].smw4_table1"
    value: "0.00"
    work: "Age 69 falls in 66-70; Table 1 number is 210; 0 / 210"
  - printed: "retirement[r2].smw4_table2"
    value: "0.00"
    work: "Combined ages 117 fall in 111-120; Table 2 number is 360; 0 / 360"
  - printed: "retirement[r2].smw4_new"
    value: "0.00"
    work: "Not a joint and survivor annuity, so Table 1 applies; 0"
  - printed: "retirement[r2].smw4"
    value: "624.00"
    work: "Worksheet was completed last year; use last year's line 4 = 624.00"
  - printed: "retirement[r2].smw5"
    value: "7488.00"
    work: "624.00 x 12 months"
  - printed: "retirement[r2].smw6"
    value: "35342.00"
    work: "Last year's line 10 = 35,342.00"
  - printed: "retirement[r2].smw7"
    value: "-35342.00"
    work: "0 - 35,342"
  - printed: "retirement[r2].smw8"
    value: "-35342.00"
    work: "Smaller of 7,488 or -35,342"
  - printed: "retirement[r2].smw9"
    value: "35342.00"
    work: "0 - (-35,342) = 35,342; result is not less than zero"
  - printed: "retirement[r2].smw10"
    value: "0.00"
    work: "35,342 + (-35,342)"
  - printed: "retirement[r2].smw11"
    value: "0.00"
    work: "0 - 0"
  - printed: "retirement[r2].cost_left"
    value: "no"
    work: "Line 7 is -35,342, which is not more than zero"
  - printed: "retirement[r2].annuity_with_cost"
    value: "no"
    work: "Simplified Method does not apply and no cost is left"
  - printed: "retirement[r2].annuity_rollover"
    value: "no"
    work: "Not a Simplified Method annuity and nothing rolled over"
  - printed: "retirement[r2].annuity_taxable"
    value: "0.00"
    work: "Not a Simplified Method annuity; use box 1 = 0"
  - printed: "retirement[r2].ira_taxable"
    value: "0.00"
    work: "Code Q qualified Roth distribution; Exception 2(b) says enter -0- on line 4b"
  - printed: "retirement[r2].ira_not_rolled"
    value: "0.00"
    work: "0 - 0"
  - printed: "retirement[r2].plan_excluded"
    value: "0.00"
    work: "Box 5 (0) + rolled over (0)"
  - printed: "retirement[r2].plan_simple"
    value: "0.00"
    work: "0 - 0 - 0"
  - printed: "retirement[r2].plan_taxable"
    value: "0.00"
    work: "No Simplified Method annuity; plan_simple = 0"
  - printed: "retirement[r2].taxable"
    value: "0.00"
    work: "IRA distribution, so line 4b = ira_taxable = 0"
  - printed: "retirement[r2].show_a"
    value: "yes"
    work: "Exception 2 (distribution from a Roth IRA) puts the total distribution on line 4a"
  - printed: "retirement[r2].amount_a"
    value: "0.00"
    work: "Line 4a = box 1 = 0.00"
```
```

### classm.retirement.3

```yaml
```yaml
lines:
  - printed: "retirement[r1].is_ira"
    value: "yes"
    work: "Account kind is traditional_ira, so lines 4a/4b"
  - printed: "retirement[r1].roth"
    value: "no"
    work: "Traditional IRA, not Roth"
  - printed: "retirement[r1].direct"
    value: "no"
    work: "Box 7 code is 7, not G"
  - printed: "retirement[r1].bad_code"
    value: "no"
    work: "Code 7 normal distribution; no special situation"
  - printed: "retirement[r1].rolled"
    value: "0.00"
    work: "No amount rolled over; not a direct rollover"
  - printed: "retirement[r1].has_rollover"
    value: "no"
    work: "Rolled 0 and not code G"
  - printed: "retirement[r1].smw1"
    value: "0.00"
    work: "Box 1 = 0.00"
  - printed: "retirement[r1].smw2"
    value: "4653.00"
    work: "Cost given 4,653.00"
  - printed: "retirement[r1].smw4_t1_360"
    value: "12.93"
    work: "4653/360 = 12.925"
  - printed: "retirement[r1].smw4_t1_310"
    value: "15.01"
    work: "4653/310 = 15.0097"
  - printed: "retirement[r1].smw4_t1_260"
    value: "17.90"
    work: "4653/260 = 17.896"
  - printed: "retirement[r1].smw4_t1_210"
    value: "22.16"
    work: "4653/210 = 22.157"
  - printed: "retirement[r1].smw4_t1_160"
    value: "29.08"
    work: "4653/160 = 29.081"
  - printed: "retirement[r1].smw4_t2_410"
    value: "11.35"
    work: "4653/410 = 11.349"
  - printed: "retirement[r1].smw4_t2_360"
    value: "12.93"
    work: "4653/360 = 12.925"
  - printed: "retirement[r1].smw4_t2_310"
    value: "15.01"
    work: "4653/310 = 15.0097"
  - printed: "retirement[r1].smw4_t2_260"
    value: "17.90"
    work: "4653/260 = 17.896"
  - printed: "retirement[r1].smw4_t2_210"
    value: "22.16"
    work: "4653/210 = 22.157"
  - printed: "retirement[r1].smw4_table1"
    value: "17.90"
    work: "Age 64 is in the 61-65 row; after 11/18/1996 that row gives 260"
  - printed: "retirement[r1].smw4_table2"
    value: "15.01"
    work: "Combined ages 124 is in the 121-130 row, which gives 310"
  - printed: "retirement[r1].smw4_new"
    value: "17.90"
    work: "Not a joint and survivor annuity after 1997, so Table 1"
  - printed: "retirement[r1].smw4"
    value: "1925.00"
    work: "Worksheet completed last year; use last year's line 4"
  - printed: "retirement[r1].smw5"
    value: "5775.00"
    work: "1925.00 x 3 months"
  - printed: "retirement[r1].smw6"
    value: "0.00"
    work: "Last year's line 10 = 0.00"
  - printed: "retirement[r1].smw7"
    value: "4653.00"
    work: "4653.00 - 0.00"
  - printed: "retirement[r1].smw8"
    value: "4653.00"
    work: "Smaller of 5775.00 or 4653.00"
  - printed: "retirement[r1].smw9"
    value: "0.00"
    work: "0.00 - 4653.00 is less than zero, so 0"
  - printed: "retirement[r1].smw10"
    value: "4653.00"
    work: "0.00 + 4653.00"
  - printed: "retirement[r1].smw11"
    value: "0.00"
    work: "4653.00 - 4653.00"
  - printed: "retirement[r1].cost_left"
    value: "yes"
    work: "Line 7 is 4653.00, which is more than 0"
  - printed: "retirement[r1].annuity_with_cost"
    value: "no"
    work: "Simplified Method does not apply (answer no)"
  - printed: "retirement[r1].annuity_rollover"
    value: "no"
    work: "Simplified Method does not apply and nothing was rolled over"
  - printed: "retirement[r1].annuity_taxable"
    value: "0.00"
    work: "Simplified Method not used; box 1 = 0.00"
  - printed: "retirement[r1].ira_taxable"
    value: "0.00"
    work: "Part not rolled over = 0.00 - 0.00"
  - printed: "retirement[r1].ira_not_rolled"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "retirement[r1].plan_excluded"
    value: "0.00"
    work: "Box 5 0.00 + rolled 0.00"
  - printed: "retirement[r1].plan_simple"
    value: "0.00"
    work: "0.00 - 0.00"
  - printed: "retirement[r1].plan_taxable"
    value: "0.00"
    work: "No Simplified Method; plan_simple = 0.00"
  - printed: "retirement[r1].taxable"
    value: "0.00"
    work: "IRA is fully taxable: 0.00 on line 4b"
  - printed: "retirement[r1].show_a"
    value: "no"
    work: "No exception applies; fully taxable"
  - printed: "retirement[r1].amount_a"
    value: "0.00"
    work: "Fully taxable, so no line 4a entry"
  - printed: "retirement[r2].is_ira"
    value: "yes"
    work: "Account kind is traditional_ira"
  - printed: "retirement[r2].roth"
    value: "no"
    work: "Traditional IRA, not Roth"
  - printed: "retirement[r2].direct"
    value: "no"
    work: "Code 7, not G"
  - printed: "retirement[r2].bad_code"
    value: "no"
    work: "Code 7 normal distribution; no special situation"
  - printed: "retirement[r2].rolled"
    value: "0.00"
    work: "No amount rolled over"
  - printed: "retirement[r2].has_rollover"
    value: "no"
    work: "Rolled 0 and not code G"
  - printed: "retirement[r2].smw1"
    value: "27508.00"
    work: "Box 1 = 27,508.00"
  - printed: "retirement[r2].smw2"
    value: "51447.00"
    work: "Cost given 51,447.00"
  - printed: "retirement[r2].smw4_t1_360"
    value: "142.91"
    work: "51447/360 = 142.908"
  - printed: "retirement[r2].smw4_t1_310"
    value: "165.96"
    work: "51447/310 = 165.958"
  - printed: "retirement[r2].smw4_t1_260"
    value: "197.87"
    work: "51447/260 = 197.873"
  - printed: "retirement[r2].smw4_t1_210"
    value: "244.99"
    work: "51447/210 = 244.986"
  - printed: "retirement[r2].smw4_t1_160"
    value: "321.54"
    work: "51447/160 = 321.544"
  - printed: "retirement[r2].smw4_t2_410"
    value: "125.48"
    work: "51447/410 = 125.480"
  - printed: "retirement[r2].smw4_t2_360"
    value: "142.91"
    work: "51447/360 = 142.908"
  - printed: "retirement[r2].smw4_t2_310"
    value: "165.96"
    work: "51447/310 = 165.958"
  - printed: "retirement[r2].smw4_t2_260"
    value: "197.87"
    work: "51447/260 = 197.873"
  - printed: "retirement[r2].smw4_t2_210"
    value: "244.99"
    work: "51447/210 = 244.986"
  - printed: "retirement[r2].smw4_table1"
    value: "197.87"
    work: "Age 64 is in the 61-65 row; after 11/18/1996 that row gives 260"
  - printed: "retirement[r2].smw4_table2"
    value: "197.87"
    work: "Combined ages 132 is in the 131-140 row, which gives 260"
  - printed: "retirement[r2].smw4_new"
    value: "197.87"
    work: "Joint and survivor annuity after 1997, so Table 2"
  - printed: "retirement[r2].smw4"
    value: "197.87"
    work: "Worksheet not completed last year; use 51447/260"
  - printed: "retirement[r2].smw5"
    value: "2374.44"
    work: "197.87 x 12 months"
  - printed: "retirement[r2].smw6"
    value: "7061.00"
    work: "Amount recovered after 1986 = 7,061.00"
  - printed: "retirement[r2].smw7"
    value: "44386.00"
    work: "51447.00 - 7061.00"
  - printed: "retirement[r2].smw8"
    value: "2374.44"
    work: "Smaller of 2374.44 or 44386.00"
  - printed: "retirement[r2].smw9"
    value: "25133.56"
    work: "27508.00 - 2374.44"
  - printed: "retirement[r2].smw10"
    value: "9435.44"
    work: "7061.00 + 2374.44"
  - printed: "retirement[r2].smw11"
    value: "42011.56"
    work: "51447.00 - 9435.44"
  - printed: "retirement[r2].cost_left"
    value: "yes"
    work: "Line 7 is 44386.00, which is more than 0"
  - printed: "retirement[r2].annuity_with_cost"
    value: "no"
    work: "Simplified Method does not apply (answer no)"
  - printed: "retirement[r2].annuity_rollover"
    value: "no"
    work: "Simplified Method does not apply and nothing was rolled over"
  - printed: "retirement[r2].annuity_taxable"
    value: "27508.00"
    work: "Simplified Method not used; whole box 1"
  - printed: "retirement[r2].ira_taxable"
    value: "27508.00"
    work: "Part not rolled over = 27508.00 - 0.00"
  - printed: "retirement[r2].ira_not_rolled"
    value: "27508.00"
    work: "27508.00 - 0.00"
  - printed: "retirement[r2].plan_excluded"
    value: "0.00"
    work: "Box 5 0.00 + rolled 0.00"
  - printed: "retirement[r2].plan_simple"
    value: "27508.00"
    work: "27508.00 - 0.00 - 0.00"
  - printed: "retirement[r2].plan_taxable"
    value: "27508.00"
    work: "No Simplified Method; plan_simple"
  - printed: "retirement[r2].taxable"
    value: "27508.00"
    work: "IRA fully taxable: total distribution goes on line 4b"
  - printed: "retirement[r2].show_a"
    value: "no"
    work: "No exception applies; fully taxable"
  - printed: "retirement[r2].amount_a"
    value: "0.00"
    work: "Fully taxable, so no line 4a entry"
```
```
