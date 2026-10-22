# Class M hand-work — retirement

`Form 1099-R distributions (IRAs, pensions and annuities)` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-22 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| subject sha256 | a9821cd3a8b5e42c6c022ae1d5f62644213adb8025c23079b46d7d659a092e39 |
| cases | 4 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099r | 2025 (calendar-year form) | - | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | - | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| i1040gi | 2025; printed date 2026-02-25 | 26, 27, 28, 29, 30, 31 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 26, 27, 28, 30, 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |
| f8880 | 2025; created 2025-11-04 | 1, 2 | whole document | e8b37e5065850674d94eecd145d787e1789924b0c2b09bf3693992c45ba9dc94 | 2 | e082ccb481b2d0e872449d7728c290669213b8d16d4c94f281c1bb70aeaed575 |

## Lines

### case classm.retirement.1 — prompt sha256 1f613d2eff198f1142d5796f2f936b394260fab79efec01030a1891b47bb1709; branches: retirement.special:false, retirement.annuity:false, retirement.used_last_year:false, retirement.used_last_year:true, retirement.joint_life:false, retirement.joint_life:true, retirement.is_ira:false, retirement.is_ira:true, retirement.roth:false, retirement.roth:true, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw4_table1#3, retirement.smw4_table1#4, retirement.smw4_table2#0, retirement.smw4_table2#4, retirement.smw4_new#0, retirement.smw4_new#1, retirement.smw4#0, retirement.smw4#1, retirement.smw8:left, retirement.smw8:right, retirement.smw9:floor, retirement.smw9:positive, retirement.cost_left:false, retirement.cost_left:true, retirement.annuity_with_cost:false, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.annuity_taxable#1, retirement.ira_taxable#0, retirement.ira_taxable#1, retirement.ira_not_rolled:floor, retirement.ira_not_rolled:positive, retirement.plan_simple:floor, retirement.plan_simple:positive, retirement.plan_taxable#1, retirement.taxable#0, retirement.taxable#1, retirement.show_a:true, retirement.amount_a#0, retirement.sav_military:false, retirement.sav_404k:false, retirement.sav_inherited:false, retirement.sav_inherited:true, retirement.sav_excluded:false, retirement.sav_excluded:true, retirement.sav_gross:floor, retirement.sav_gross:positive, retirement.sav_amount#0, retirement.sav_amount#1

### classm.retirement.1 — retirement[r1].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: yes

### classm.retirement.1 — retirement[r1].roth — Roth IRA distribution
Status: **AGREE**

Value: yes

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

Value: $25,958.00

### classm.retirement.1 — retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $27,998.00

### classm.retirement.1 — retirement[r1].smw4_t1_360 — Line 2 divided by 360 (Table 1)
Status: **AGREE**

Value: $77.77

### classm.retirement.1 — retirement[r1].smw4_t1_310 — Line 2 divided by 310 (Table 1)
Status: **AGREE**

Value: $90.32

### classm.retirement.1 — retirement[r1].smw4_t1_260 — Line 2 divided by 260 (Table 1)
Status: **AGREE**

Value: $107.68

### classm.retirement.1 — retirement[r1].smw4_t1_210 — Line 2 divided by 210 (Table 1)
Status: **AGREE**

Value: $133.32

### classm.retirement.1 — retirement[r1].smw4_t1_160 — Line 2 divided by 160 (Table 1)
Status: **AGREE**

Value: $174.99

### classm.retirement.1 — retirement[r1].smw4_t2_410 — Line 2 divided by 410 (Table 2)
Status: **AGREE**

Value: $68.29

### classm.retirement.1 — retirement[r1].smw4_t2_360 — Line 2 divided by 360 (Table 2)
Status: **AGREE**

Value: $77.77

### classm.retirement.1 — retirement[r1].smw4_t2_310 — Line 2 divided by 310 (Table 2)
Status: **AGREE**

Value: $90.32

### classm.retirement.1 — retirement[r1].smw4_t2_260 — Line 2 divided by 260 (Table 2)
Status: **AGREE**

Value: $107.68

### classm.retirement.1 — retirement[r1].smw4_t2_210 — Line 2 divided by 210 (Table 2)
Status: **AGREE**

Value: $133.32

### classm.retirement.1 — retirement[r1].smw4_table1 — Line 2 divided by the Table 1 number for the age at the annuity starting date
Status: **AGREE**

Value: $133.32

### classm.retirement.1 — retirement[r1].smw4_table2 — Line 2 divided by the Table 2 number for the combined ages at the annuity starti
Status: **AGREE**

Value: $68.29

### classm.retirement.1 — retirement[r1].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $133.32

### classm.retirement.1 — retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $133.32

### classm.retirement.1 — retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $799.92

### classm.retirement.1 — retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $47,319.00

### classm.retirement.1 — retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $-19,321.00

### classm.retirement.1 — retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $-19,321.00

### classm.retirement.1 — retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $45,279.00

### classm.retirement.1 — retirement[r1].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $27,998.00

### classm.retirement.1 — retirement[r1].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r1].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r1].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r1].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r1].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $25,958.00

### classm.retirement.1 — retirement[r1].ira_taxable — Taxable IRA amount: the part not rolled over (zero for a qualified Roth IRA dist
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r1].ira_not_rolled — Box 1 less the amount rolled over
Status: **AGREE**

Value: $25,958.00

### classm.retirement.1 — retirement[r1].plan_excluded — Taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r1].plan_simple — Box 1 less taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $25,958.00

### classm.retirement.1 — retirement[r1].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $25,958.00

### classm.retirement.1 — retirement[r1].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r1].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: yes

### classm.retirement.1 — retirement[r1].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $25,958.00

### classm.retirement.1 — retirement[r1].sav_excluded — A distribution Form 8880 line 4 does not count (from a military retirement plan 
Status: **AGREE**

Value: yes

### classm.retirement.1 — retirement[r1].sav_gross — The distribution less the part rolled over (the whole distribution for a direct 
Status: **AGREE**

Value: $25,958.00

### classm.retirement.1 — retirement[r1].sav_amount — This distribution's amount on Form 8880 line 4
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r2].roth — Roth IRA distribution
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r2].direct — Direct rollover (code G)
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r2].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r2].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r2].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $30,498.00

### classm.retirement.1 — retirement[r2].smw4_t1_360 — Line 2 divided by 360 (Table 1)
Status: **AGREE**

Value: $84.72

### classm.retirement.1 — retirement[r2].smw4_t1_310 — Line 2 divided by 310 (Table 1)
Status: **AGREE**

Value: $98.38

### classm.retirement.1 — retirement[r2].smw4_t1_260 — Line 2 divided by 260 (Table 1)
Status: **AGREE**

Value: $117.30

### classm.retirement.1 — retirement[r2].smw4_t1_210 — Line 2 divided by 210 (Table 1)
Status: **AGREE**

Value: $145.23

### classm.retirement.1 — retirement[r2].smw4_t1_160 — Line 2 divided by 160 (Table 1)
Status: **AGREE**

Value: $190.61

### classm.retirement.1 — retirement[r2].smw4_t2_410 — Line 2 divided by 410 (Table 2)
Status: **AGREE**

Value: $74.39

### classm.retirement.1 — retirement[r2].smw4_t2_360 — Line 2 divided by 360 (Table 2)
Status: **AGREE**

Value: $84.72

### classm.retirement.1 — retirement[r2].smw4_t2_310 — Line 2 divided by 310 (Table 2)
Status: **AGREE**

Value: $98.38

### classm.retirement.1 — retirement[r2].smw4_t2_260 — Line 2 divided by 260 (Table 2)
Status: **AGREE**

Value: $117.30

### classm.retirement.1 — retirement[r2].smw4_t2_210 — Line 2 divided by 210 (Table 2)
Status: **AGREE**

Value: $145.23

### classm.retirement.1 — retirement[r2].smw4_table1 — Line 2 divided by the Table 1 number for the age at the annuity starting date
Status: **AGREE**

Value: $190.61

### classm.retirement.1 — retirement[r2].smw4_table2 — Line 2 divided by the Table 2 number for the combined ages at the annuity starti
Status: **AGREE**

Value: $145.23

### classm.retirement.1 — retirement[r2].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $145.23

### classm.retirement.1 — retirement[r2].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $14,678.00

### classm.retirement.1 — retirement[r2].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $15,820.00

### classm.retirement.1 — retirement[r2].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $14,678.00

### classm.retirement.1 — retirement[r2].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $15,820.00

### classm.retirement.1 — retirement[r2].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: yes

### classm.retirement.1 — retirement[r2].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r2].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r2].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].ira_taxable — Taxable IRA amount: the part not rolled over (zero for a qualified Roth IRA dist
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].ira_not_rolled — Box 1 less the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].plan_excluded — Taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $545.00

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
Status: **DISAGREE**

Project: yes
Model: no
Work: Taxable amount equals box 1 (both 0), so no line 5a entry is needed

Ruling: representation; project retained; model value dropped from the fixture. As in the earlier ruling on classm.retirement.9: box 1 is $0, so line 5a is $0 whether or not the entry is shown (amount_a agrees); the project shows it because box 5 ($545.00) is nonzero on a plan distribution outside the Simplified Method, i1040gi p. 28, Partially Taxable Pensions and Annuities. [dropped]

### classm.retirement.1 — retirement[r2].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].sav_excluded — A distribution Form 8880 line 4 does not count (from a military retirement plan 
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r2].sav_gross — The distribution less the part rolled over (the whole distribution for a direct 
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r2].sav_amount — This distribution's amount on Form 8880 line 4
Status: **AGREE**

Value: $0.00

### case classm.retirement.2 — prompt sha256 1a1a51bedfba6f6c0ecd6fd8d0a2a64b2637807b240f87f4be011c1e9c823740; branches: retirement.special:false, retirement.annuity:false, retirement.annuity:true, retirement.used_last_year:false, retirement.joint_life:false, retirement.is_ira:false, retirement.is_ira:true, retirement.roth:false, retirement.direct:false, retirement.direct:true, retirement.bad_code:false, retirement.rolled#0, retirement.rolled#1, retirement.has_rollover:false, retirement.has_rollover:true, retirement.smw4_table1#2, retirement.smw4_table1#3, retirement.smw4_table2#1, retirement.smw4_table2#2, retirement.smw4_new#1, retirement.smw4#1, retirement.smw8:right, retirement.smw9:positive, retirement.cost_left:false, retirement.annuity_with_cost:false, retirement.annuity_rollover:false, retirement.annuity_taxable#1, retirement.ira_taxable#1, retirement.ira_not_rolled:floor, retirement.ira_not_rolled:positive, retirement.plan_simple:floor, retirement.plan_simple:positive, retirement.plan_taxable#0, retirement.plan_taxable#1, retirement.taxable#0, retirement.taxable#1, retirement.show_a:false, retirement.show_a:true, retirement.amount_a#0, retirement.amount_a#1, retirement.sav_military:false, retirement.sav_404k:false, retirement.sav_inherited:false, retirement.sav_excluded:false, retirement.sav_gross:floor, retirement.sav_gross:positive, retirement.sav_amount#1

### classm.retirement.2 — retirement[r1].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: yes

### classm.retirement.2 — retirement[r1].roth — Roth IRA distribution
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r1].direct — Direct rollover (code G)
Status: **AGREE**

Value: yes

### classm.retirement.2 — retirement[r1].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r1].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: yes

### classm.retirement.2 — retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $3,060.00

### classm.retirement.2 — retirement[r1].smw4_t1_360 — Line 2 divided by 360 (Table 1)
Status: **AGREE**

Value: $8.50

### classm.retirement.2 — retirement[r1].smw4_t1_310 — Line 2 divided by 310 (Table 1)
Status: **AGREE**

Value: $9.87

### classm.retirement.2 — retirement[r1].smw4_t1_260 — Line 2 divided by 260 (Table 1)
Status: **AGREE**

Value: $11.77

### classm.retirement.2 — retirement[r1].smw4_t1_210 — Line 2 divided by 210 (Table 1)
Status: **AGREE**

Value: $14.57

### classm.retirement.2 — retirement[r1].smw4_t1_160 — Line 2 divided by 160 (Table 1)
Status: **AGREE**

Value: $19.13

### classm.retirement.2 — retirement[r1].smw4_t2_410 — Line 2 divided by 410 (Table 2)
Status: **AGREE**

Value: $7.46

### classm.retirement.2 — retirement[r1].smw4_t2_360 — Line 2 divided by 360 (Table 2)
Status: **AGREE**

Value: $8.50

### classm.retirement.2 — retirement[r1].smw4_t2_310 — Line 2 divided by 310 (Table 2)
Status: **AGREE**

Value: $9.87

### classm.retirement.2 — retirement[r1].smw4_t2_260 — Line 2 divided by 260 (Table 2)
Status: **AGREE**

Value: $11.77

### classm.retirement.2 — retirement[r1].smw4_t2_210 — Line 2 divided by 210 (Table 2)
Status: **AGREE**

Value: $14.57

### classm.retirement.2 — retirement[r1].smw4_table1 — Line 2 divided by the Table 1 number for the age at the annuity starting date
Status: **AGREE**

Value: $11.77

### classm.retirement.2 — retirement[r1].smw4_table2 — Line 2 divided by the Table 2 number for the combined ages at the annuity starti
Status: **AGREE**

Value: $9.87

### classm.retirement.2 — retirement[r1].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $11.77

### classm.retirement.2 — retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $11.77

### classm.retirement.2 — retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $141.24

### classm.retirement.2 — retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $12,495.00

### classm.retirement.2 — retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $-9,435.00

### classm.retirement.2 — retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $-9,435.00

### classm.retirement.2 — retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $9,435.00

### classm.retirement.2 — retirement[r1].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $3,060.00

### classm.retirement.2 — retirement[r1].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: no

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

Value: yes

### classm.retirement.2 — retirement[r1].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].sav_excluded — A distribution Form 8880 line 4 does not count (from a military retirement plan 
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r1].sav_gross — The distribution less the part rolled over (the whole distribution for a direct 
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].sav_amount — This distribution's amount on Form 8880 line 4
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r2].roth — Roth IRA distribution
Status: **AGREE**

Value: no

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

Value: $26,827.00

### classm.retirement.2 — retirement[r2].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $15,431.00

### classm.retirement.2 — retirement[r2].smw4_t1_360 — Line 2 divided by 360 (Table 1)
Status: **AGREE**

Value: $42.86

### classm.retirement.2 — retirement[r2].smw4_t1_310 — Line 2 divided by 310 (Table 1)
Status: **AGREE**

Value: $49.78

### classm.retirement.2 — retirement[r2].smw4_t1_260 — Line 2 divided by 260 (Table 1)
Status: **AGREE**

Value: $59.35

### classm.retirement.2 — retirement[r2].smw4_t1_210 — Line 2 divided by 210 (Table 1)
Status: **AGREE**

Value: $73.48

### classm.retirement.2 — retirement[r2].smw4_t1_160 — Line 2 divided by 160 (Table 1)
Status: **AGREE**

Value: $96.44

### classm.retirement.2 — retirement[r2].smw4_t2_410 — Line 2 divided by 410 (Table 2)
Status: **AGREE**

Value: $37.64

### classm.retirement.2 — retirement[r2].smw4_t2_360 — Line 2 divided by 360 (Table 2)
Status: **AGREE**

Value: $42.86

### classm.retirement.2 — retirement[r2].smw4_t2_310 — Line 2 divided by 310 (Table 2)
Status: **AGREE**

Value: $49.78

### classm.retirement.2 — retirement[r2].smw4_t2_260 — Line 2 divided by 260 (Table 2)
Status: **AGREE**

Value: $59.35

### classm.retirement.2 — retirement[r2].smw4_t2_210 — Line 2 divided by 210 (Table 2)
Status: **AGREE**

Value: $73.48

### classm.retirement.2 — retirement[r2].smw4_table1 — Line 2 divided by the Table 1 number for the age at the annuity starting date
Status: **AGREE**

Value: $73.48

### classm.retirement.2 — retirement[r2].smw4_table2 — Line 2 divided by the Table 2 number for the combined ages at the annuity starti
Status: **AGREE**

Value: $42.86

### classm.retirement.2 — retirement[r2].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $73.48

### classm.retirement.2 — retirement[r2].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $73.48

### classm.retirement.2 — retirement[r2].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $514.36

### classm.retirement.2 — retirement[r2].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $41,795.00

### classm.retirement.2 — retirement[r2].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $-26,364.00

### classm.retirement.2 — retirement[r2].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $-26,364.00

### classm.retirement.2 — retirement[r2].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $53,191.00

### classm.retirement.2 — retirement[r2].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $15,431.00

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

Value: $26,827.00

### classm.retirement.2 — retirement[r2].ira_taxable — Taxable IRA amount: the part not rolled over (zero for a qualified Roth IRA dist
Status: **AGREE**

Value: $26,827.00

### classm.retirement.2 — retirement[r2].ira_not_rolled — Box 1 less the amount rolled over
Status: **AGREE**

Value: $26,827.00

### classm.retirement.2 — retirement[r2].plan_excluded — Taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].plan_simple — Box 1 less taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $26,827.00

### classm.retirement.2 — retirement[r2].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $26,827.00

### classm.retirement.2 — retirement[r2].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $26,827.00

### classm.retirement.2 — retirement[r2].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r2].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r2].sav_excluded — A distribution Form 8880 line 4 does not count (from a military retirement plan 
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r2].sav_gross — The distribution less the part rolled over (the whole distribution for a direct 
Status: **AGREE**

Value: $26,827.00

### classm.retirement.2 — retirement[r2].sav_amount — This distribution's amount on Form 8880 line 4
Status: **AGREE**

Value: $26,827.00

### case classm.retirement.3 — prompt sha256 b32e12bfcf6900692d1c494cd0362d9ed95394ed05f94fe1af7442adad370e71; branches: retirement.special:false, retirement.annuity:false, retirement.used_last_year:true, retirement.joint_life:false, retirement.joint_life:true, retirement.is_ira:false, retirement.is_ira:true, retirement.roth:false, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw4_table1#0, retirement.smw4_table1#3, retirement.smw4_table2#3, retirement.smw4_table2#4, retirement.smw4_new#0, retirement.smw4_new#1, retirement.smw4#0, retirement.smw8:left, retirement.smw9:floor, retirement.smw9:positive, retirement.cost_left:true, retirement.annuity_with_cost:false, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.ira_taxable#1, retirement.ira_not_rolled:floor, retirement.ira_not_rolled:positive, retirement.plan_simple:floor, retirement.plan_simple:positive, retirement.plan_taxable#1, retirement.taxable#0, retirement.taxable#1, retirement.show_a:false, retirement.show_a:true, retirement.amount_a#0, retirement.amount_a#1, retirement.sav_military:false, retirement.sav_military:true, retirement.sav_404k:false, retirement.sav_inherited:false, retirement.sav_excluded:false, retirement.sav_excluded:true, retirement.sav_gross:floor, retirement.sav_gross:positive, retirement.sav_amount#0, retirement.sav_amount#1

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

Value: $42,431.00

### classm.retirement.3 — retirement[r1].smw4_t1_360 — Line 2 divided by 360 (Table 1)
Status: **AGREE**

Value: $117.86

### classm.retirement.3 — retirement[r1].smw4_t1_310 — Line 2 divided by 310 (Table 1)
Status: **AGREE**

Value: $136.87

### classm.retirement.3 — retirement[r1].smw4_t1_260 — Line 2 divided by 260 (Table 1)
Status: **AGREE**

Value: $163.20

### classm.retirement.3 — retirement[r1].smw4_t1_210 — Line 2 divided by 210 (Table 1)
Status: **AGREE**

Value: $202.05

### classm.retirement.3 — retirement[r1].smw4_t1_160 — Line 2 divided by 160 (Table 1)
Status: **AGREE**

Value: $265.19

### classm.retirement.3 — retirement[r1].smw4_t2_410 — Line 2 divided by 410 (Table 2)
Status: **AGREE**

Value: $103.49

### classm.retirement.3 — retirement[r1].smw4_t2_360 — Line 2 divided by 360 (Table 2)
Status: **AGREE**

Value: $117.86

### classm.retirement.3 — retirement[r1].smw4_t2_310 — Line 2 divided by 310 (Table 2)
Status: **AGREE**

Value: $136.87

### classm.retirement.3 — retirement[r1].smw4_t2_260 — Line 2 divided by 260 (Table 2)
Status: **AGREE**

Value: $163.20

### classm.retirement.3 — retirement[r1].smw4_t2_210 — Line 2 divided by 210 (Table 2)
Status: **AGREE**

Value: $202.05

### classm.retirement.3 — retirement[r1].smw4_table1 — Line 2 divided by the Table 1 number for the age at the annuity starting date
Status: **AGREE**

Value: $202.05

### classm.retirement.3 — retirement[r1].smw4_table2 — Line 2 divided by the Table 2 number for the combined ages at the annuity starti
Status: **AGREE**

Value: $202.05

### classm.retirement.3 — retirement[r1].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $202.05

### classm.retirement.3 — retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $1,801.00

### classm.retirement.3 — retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $21,612.00

### classm.retirement.3 — retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $42,431.00

### classm.retirement.3 — retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $21,612.00

### classm.retirement.3 — retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r1].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $21,612.00

### classm.retirement.3 — retirement[r1].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $20,819.00

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

### classm.retirement.3 — retirement[r1].sav_excluded — A distribution Form 8880 line 4 does not count (from a military retirement plan 
Status: **AGREE**

Value: no

### classm.retirement.3 — retirement[r1].sav_gross — The distribution less the part rolled over (the whole distribution for a direct 
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r1].sav_amount — This distribution's amount on Form 8880 line 4
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r2].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: no

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

Value: $41,168.00

### classm.retirement.3 — retirement[r2].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $29,819.00

### classm.retirement.3 — retirement[r2].smw4_t1_360 — Line 2 divided by 360 (Table 1)
Status: **AGREE**

Value: $82.83

### classm.retirement.3 — retirement[r2].smw4_t1_310 — Line 2 divided by 310 (Table 1)
Status: **AGREE**

Value: $96.19

### classm.retirement.3 — retirement[r2].smw4_t1_260 — Line 2 divided by 260 (Table 1)
Status: **AGREE**

Value: $114.69

### classm.retirement.3 — retirement[r2].smw4_t1_210 — Line 2 divided by 210 (Table 1)
Status: **AGREE**

Value: $142.00

### classm.retirement.3 — retirement[r2].smw4_t1_160 — Line 2 divided by 160 (Table 1)
Status: **AGREE**

Value: $186.37

### classm.retirement.3 — retirement[r2].smw4_t2_410 — Line 2 divided by 410 (Table 2)
Status: **AGREE**

Value: $72.73

### classm.retirement.3 — retirement[r2].smw4_t2_360 — Line 2 divided by 360 (Table 2)
Status: **AGREE**

Value: $82.83

### classm.retirement.3 — retirement[r2].smw4_t2_310 — Line 2 divided by 310 (Table 2)
Status: **AGREE**

Value: $96.19

### classm.retirement.3 — retirement[r2].smw4_t2_260 — Line 2 divided by 260 (Table 2)
Status: **AGREE**

Value: $114.69

### classm.retirement.3 — retirement[r2].smw4_t2_210 — Line 2 divided by 210 (Table 2)
Status: **AGREE**

Value: $142.00

### classm.retirement.3 — retirement[r2].smw4_table1 — Line 2 divided by the Table 1 number for the age at the annuity starting date
Status: **AGREE**

Value: $82.83

### classm.retirement.3 — retirement[r2].smw4_table2 — Line 2 divided by the Table 2 number for the combined ages at the annuity starti
Status: **AGREE**

Value: $114.69

### classm.retirement.3 — retirement[r2].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $114.69

### classm.retirement.3 — retirement[r2].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $816.00

### classm.retirement.3 — retirement[r2].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $9,792.00

### classm.retirement.3 — retirement[r2].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r2].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $29,819.00

### classm.retirement.3 — retirement[r2].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $9,792.00

### classm.retirement.3 — retirement[r2].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $31,376.00

### classm.retirement.3 — retirement[r2].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $9,792.00

### classm.retirement.3 — retirement[r2].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $20,027.00

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

Project: $31,376.00
Model: $41,168.00
Work: Simplified Method not applied, so use the whole of box 1 = 41,168

Ruling: helper of a branch this entry does not take; project retained. The entry is a plan distribution outside the Simplified Method (retirement.annuity is false), whose taxable amount is box 1 less box 5, $38,511.00 (retirement.plan_taxable and retirement.taxable, which agree); the Simplified Method helper (worksheet line 9, $31,376.00, while cost is left) is figured for every entry but read only for an annuity (retirement.plan_taxable). Dropped from the fixture as not evidence. [dropped]

### classm.retirement.3 — retirement[r2].ira_taxable — Taxable IRA amount: the part not rolled over (zero for a qualified Roth IRA dist
Status: **DISAGREE**

Project: $41,168.00
Model: $0.00
Work: Not an IRA distribution

Ruling: helper of a branch this entry does not take; project retained. The entry is not an IRA distribution (retirement.is_ira is no, agreed); the IRA helper, box 1 less the amount rolled over ($41,168.00), is figured for every entry but read only for an IRA (retirement.taxable), and the taxable amount, $38,511.00, agrees. Dropped from the fixture as not evidence. [dropped]

### classm.retirement.3 — retirement[r2].ira_not_rolled — Box 1 less the amount rolled over
Status: **AGREE**

Value: $41,168.00

### classm.retirement.3 — retirement[r2].plan_excluded — Taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $2,657.00

### classm.retirement.3 — retirement[r2].plan_simple — Box 1 less taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $38,511.00

### classm.retirement.3 — retirement[r2].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $38,511.00

### classm.retirement.3 — retirement[r2].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $38,511.00

### classm.retirement.3 — retirement[r2].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: yes

### classm.retirement.3 — retirement[r2].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $41,168.00

### classm.retirement.3 — retirement[r2].sav_excluded — A distribution Form 8880 line 4 does not count (from a military retirement plan 
Status: **AGREE**

Value: yes

### classm.retirement.3 — retirement[r2].sav_gross — The distribution less the part rolled over (the whole distribution for a direct 
Status: **AGREE**

Value: $41,168.00

### classm.retirement.3 — retirement[r2].sav_amount — This distribution's amount on Form 8880 line 4
Status: **AGREE**

Value: $0.00

### case classm.retirement.4 — prompt sha256 86e6aa251857a79c69352aa12de71b7ca27a524e7a1bbb8f3bc818c2f7aff9c3; branches: retirement.special:false, retirement.annuity:false, retirement.annuity:true, retirement.used_last_year:false, retirement.joint_life:false, retirement.is_ira:false, retirement.is_ira:true, retirement.roth:false, retirement.roth:true, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw4_table1#1, retirement.smw4_table1#4, retirement.smw4_table2#1, retirement.smw4_table2#4, retirement.smw4_new#1, retirement.smw4#1, retirement.smw8:left, retirement.smw8:right, retirement.smw9:positive, retirement.cost_left:false, retirement.cost_left:true, retirement.annuity_with_cost:false, retirement.annuity_with_cost:true, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.annuity_taxable#1, retirement.ira_taxable#0, retirement.ira_taxable#1, retirement.ira_not_rolled:floor, retirement.ira_not_rolled:positive, retirement.plan_simple:floor, retirement.plan_simple:positive, retirement.plan_taxable#0, retirement.plan_taxable#1, retirement.taxable#0, retirement.taxable#1, retirement.show_a:true, retirement.amount_a#0, retirement.sav_military:false, retirement.sav_404k:false, retirement.sav_inherited:false, retirement.sav_excluded:false, retirement.sav_gross:floor, retirement.sav_gross:positive, retirement.sav_amount#1

### classm.retirement.4 — retirement[r1].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r1].roth — Roth IRA distribution
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r1].direct — Direct rollover (code G)
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r1].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r1].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — retirement[r1].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $34,952.00

### classm.retirement.4 — retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $82,373.00

### classm.retirement.4 — retirement[r1].smw4_t1_360 — Line 2 divided by 360 (Table 1)
Status: **AGREE**

Value: $228.81

### classm.retirement.4 — retirement[r1].smw4_t1_310 — Line 2 divided by 310 (Table 1)
Status: **AGREE**

Value: $265.72

### classm.retirement.4 — retirement[r1].smw4_t1_260 — Line 2 divided by 260 (Table 1)
Status: **AGREE**

Value: $316.82

### classm.retirement.4 — retirement[r1].smw4_t1_210 — Line 2 divided by 210 (Table 1)
Status: **AGREE**

Value: $392.25

### classm.retirement.4 — retirement[r1].smw4_t1_160 — Line 2 divided by 160 (Table 1)
Status: **AGREE**

Value: $514.83

### classm.retirement.4 — retirement[r1].smw4_t2_410 — Line 2 divided by 410 (Table 2)
Status: **AGREE**

Value: $200.91

### classm.retirement.4 — retirement[r1].smw4_t2_360 — Line 2 divided by 360 (Table 2)
Status: **AGREE**

Value: $228.81

### classm.retirement.4 — retirement[r1].smw4_t2_310 — Line 2 divided by 310 (Table 2)
Status: **AGREE**

Value: $265.72

### classm.retirement.4 — retirement[r1].smw4_t2_260 — Line 2 divided by 260 (Table 2)
Status: **AGREE**

Value: $316.82

### classm.retirement.4 — retirement[r1].smw4_t2_210 — Line 2 divided by 210 (Table 2)
Status: **AGREE**

Value: $392.25

### classm.retirement.4 — retirement[r1].smw4_table1 — Line 2 divided by the Table 1 number for the age at the annuity starting date
Status: **AGREE**

Value: $514.83

### classm.retirement.4 — retirement[r1].smw4_table2 — Line 2 divided by the Table 2 number for the combined ages at the annuity starti
Status: **AGREE**

Value: $392.25

### classm.retirement.4 — retirement[r1].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $514.83

### classm.retirement.4 — retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $514.83

### classm.retirement.4 — retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $6,177.96

### classm.retirement.4 — retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $82,373.00

### classm.retirement.4 — retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $6,177.96

### classm.retirement.4 — retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $28,774.04

### classm.retirement.4 — retirement[r1].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $6,177.96

### classm.retirement.4 — retirement[r1].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $76,195.04

### classm.retirement.4 — retirement[r1].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: yes

### classm.retirement.4 — retirement[r1].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: yes

### classm.retirement.4 — retirement[r1].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r1].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $28,774.04

### classm.retirement.4 — retirement[r1].ira_taxable — Taxable IRA amount: the part not rolled over (zero for a qualified Roth IRA dist
Status: **DISAGREE**

Project: $34,952.00
Model: $0.00
Work: Not an IRA

Ruling: helper of a branch this entry does not take; project retained. The entry is a Simplified Method annuity from a plan (retirement.is_ira is no, agreed); the IRA helper, box 1 less the amount rolled over ($34,952.00), is figured for every entry but read only for an IRA (retirement.taxable), and the taxable amount, $28,774.04, agrees. Dropped from the fixture as not evidence. [dropped]

### classm.retirement.4 — retirement[r1].ira_not_rolled — Box 1 less the amount rolled over
Status: **AGREE**

Value: $34,952.00

### classm.retirement.4 — retirement[r1].plan_excluded — Taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — retirement[r1].plan_simple — Box 1 less taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $34,952.00

### classm.retirement.4 — retirement[r1].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $28,774.04

### classm.retirement.4 — retirement[r1].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $28,774.04

### classm.retirement.4 — retirement[r1].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: yes

### classm.retirement.4 — retirement[r1].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $34,952.00

### classm.retirement.4 — retirement[r1].sav_excluded — A distribution Form 8880 line 4 does not count (from a military retirement plan 
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r1].sav_gross — The distribution less the part rolled over (the whole distribution for a direct 
Status: **AGREE**

Value: $34,952.00

### classm.retirement.4 — retirement[r1].sav_amount — This distribution's amount on Form 8880 line 4
Status: **AGREE**

Value: $34,952.00

### classm.retirement.4 — retirement[r2].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: yes

### classm.retirement.4 — retirement[r2].roth — Roth IRA distribution
Status: **AGREE**

Value: yes

### classm.retirement.4 — retirement[r2].direct — Direct rollover (code G)
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r2].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r2].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — retirement[r2].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r2].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — retirement[r2].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $6,690.00

### classm.retirement.4 — retirement[r2].smw4_t1_360 — Line 2 divided by 360 (Table 1)
Status: **AGREE**

Value: $18.58

### classm.retirement.4 — retirement[r2].smw4_t1_310 — Line 2 divided by 310 (Table 1)
Status: **AGREE**

Value: $21.58

### classm.retirement.4 — retirement[r2].smw4_t1_260 — Line 2 divided by 260 (Table 1)
Status: **AGREE**

Value: $25.73

### classm.retirement.4 — retirement[r2].smw4_t1_210 — Line 2 divided by 210 (Table 1)
Status: **AGREE**

Value: $31.86

### classm.retirement.4 — retirement[r2].smw4_t1_160 — Line 2 divided by 160 (Table 1)
Status: **AGREE**

Value: $41.81

### classm.retirement.4 — retirement[r2].smw4_t2_410 — Line 2 divided by 410 (Table 2)
Status: **AGREE**

Value: $16.32

### classm.retirement.4 — retirement[r2].smw4_t2_360 — Line 2 divided by 360 (Table 2)
Status: **AGREE**

Value: $18.58

### classm.retirement.4 — retirement[r2].smw4_t2_310 — Line 2 divided by 310 (Table 2)
Status: **AGREE**

Value: $21.58

### classm.retirement.4 — retirement[r2].smw4_t2_260 — Line 2 divided by 260 (Table 2)
Status: **AGREE**

Value: $25.73

### classm.retirement.4 — retirement[r2].smw4_t2_210 — Line 2 divided by 210 (Table 2)
Status: **AGREE**

Value: $31.86

### classm.retirement.4 — retirement[r2].smw4_table1 — Line 2 divided by the Table 1 number for the age at the annuity starting date
Status: **AGREE**

Value: $21.58

### classm.retirement.4 — retirement[r2].smw4_table2 — Line 2 divided by the Table 2 number for the combined ages at the annuity starti
Status: **AGREE**

Value: $18.58

### classm.retirement.4 — retirement[r2].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $21.58

### classm.retirement.4 — retirement[r2].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $21.58

### classm.retirement.4 — retirement[r2].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $258.96

### classm.retirement.4 — retirement[r2].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $46,308.00

### classm.retirement.4 — retirement[r2].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $-39,618.00

### classm.retirement.4 — retirement[r2].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $-39,618.00

### classm.retirement.4 — retirement[r2].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $39,618.00

### classm.retirement.4 — retirement[r2].smw10 — Add lines 6 and 8. This is the amount you have recovered tax free through 2025
Status: **AGREE**

Value: $6,690.00

### classm.retirement.4 — retirement[r2].smw11 — Balance of cost to be recovered. Subtract line 10 from line 2
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — retirement[r2].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r2].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r2].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r2].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — retirement[r2].ira_taxable — Taxable IRA amount: the part not rolled over (zero for a qualified Roth IRA dist
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — retirement[r2].ira_not_rolled — Box 1 less the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — retirement[r2].plan_excluded — Taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — retirement[r2].plan_simple — Box 1 less taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — retirement[r2].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — retirement[r2].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — retirement[r2].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: yes

### classm.retirement.4 — retirement[r2].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — retirement[r2].sav_excluded — A distribution Form 8880 line 4 does not count (from a military retirement plan 
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r2].sav_gross — The distribution less the part rolled over (the whole distribution for a direct 
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — retirement[r2].sav_amount — This distribution's amount on Form 8880 line 4
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.retirement.1

```yaml
```yaml
lines:
  - printed: "retirement[r1].is_ira"
    value: "yes"
    work: "Account kind roth_ira, so it is an IRA distribution (lines 4a/4b)"
  - printed: "retirement[r1].roth"
    value: "yes"
    work: "Account kind is roth_ira"
  - printed: "retirement[r1].direct"
    value: "no"
    work: "Box 7 code is Q, not G"
  - printed: "retirement[r1].bad_code"
    value: "no"
    work: "Code Q is handled by Exception 2(b); the special-situations question was answered no"
  - printed: "retirement[r1].rolled"
    value: "0.00"
    work: "Amount rolled over is $0; not a direct rollover"
  - printed: "retirement[r1].has_rollover"
    value: "no"
    work: "Nothing rolled over and no code G"
  - printed: "retirement[r1].smw1"
    value: "25958.00"
    work: "Box 1"
  - printed: "retirement[r1].smw2"
    value: "27998.00"
    work: "Cost at the annuity starting date, as given"
  - printed: "retirement[r1].smw4_t1_360"
    value: "77.77"
    work: "27,998 / 360"
  - printed: "retirement[r1].smw4_t1_310"
    value: "90.32"
    work: "27,998 / 310"
  - printed: "retirement[r1].smw4_t1_260"
    value: "107.68"
    work: "27,998 / 260"
  - printed: "retirement[r1].smw4_t1_210"
    value: "133.32"
    work: "27,998 / 210"
  - printed: "retirement[r1].smw4_t1_160"
    value: "174.99"
    work: "27,998 / 160"
  - printed: "retirement[r1].smw4_t2_410"
    value: "68.29"
    work: "27,998 / 410"
  - printed: "retirement[r1].smw4_t2_360"
    value: "77.77"
    work: "27,998 / 360"
  - printed: "retirement[r1].smw4_t2_310"
    value: "90.32"
    work: "27,998 / 310"
  - printed: "retirement[r1].smw4_t2_260"
    value: "107.68"
    work: "27,998 / 260"
  - printed: "retirement[r1].smw4_t2_210"
    value: "133.32"
    work: "27,998 / 210"
  - printed: "retirement[r1].smw4_table1"
    value: "133.32"
    work: "Age 68 is in the 66-70 band, after-11/18/1996 column, so divide by 210"
  - printed: "retirement[r1].smw4_table2"
    value: "68.29"
    work: "Combined ages 104 is 110 or under, so divide by 410"
  - printed: "retirement[r1].smw4_new"
    value: "133.32"
    work: "Not a joint-and-survivor annuity starting after 1997, so use Table 1"
  - printed: "retirement[r1].smw4"
    value: "133.32"
    work: "Worksheet not completed last year, so use line 2 / line 3"
  - printed: "retirement[r1].smw5"
    value: "799.92"
    work: "133.32 x 6 months"
  - printed: "retirement[r1].smw6"
    value: "47319.00"
    work: "Amount recovered tax free after 1986, as given"
  - printed: "retirement[r1].smw7"
    value: "-19321.00"
    work: "27,998 - 47,319"
  - printed: "retirement[r1].smw8"
    value: "-19321.00"
    work: "Smaller of 799.92 or -19,321"
  - printed: "retirement[r1].smw9"
    value: "45279.00"
    work: "25,958 - (-19,321); not less than zero"
  - printed: "retirement[r1].smw10"
    value: "27998.00"
    work: "47,319 + (-19,321)"
  - printed: "retirement[r1].smw11"
    value: "0.00"
    work: "27,998 - 27,998"
  - printed: "retirement[r1].cost_left"
    value: "no"
    work: "Line 7 is -19,321, which is not more than zero"
  - printed: "retirement[r1].annuity_with_cost"
    value: "no"
    work: "The Simplified Method does not apply (answered no)"
  - printed: "retirement[r1].annuity_rollover"
    value: "no"
    work: "Simplified Method not used and nothing rolled over"
  - printed: "retirement[r1].annuity_taxable"
    value: "25958.00"
    work: "No Simplified Method with cost left, so the whole of box 1"
  - printed: "retirement[r1].ira_taxable"
    value: "0.00"
    work: "Exception 2(b): code Q, so enter -0- on line 4b"
  - printed: "retirement[r1].ira_not_rolled"
    value: "25958.00"
    work: "25,958 - 0"
  - printed: "retirement[r1].plan_excluded"
    value: "0.00"
    work: "Box 5 of 0 + rolled over 0"
  - printed: "retirement[r1].plan_simple"
    value: "25958.00"
    work: "25,958 - 0"
  - printed: "retirement[r1].plan_taxable"
    value: "25958.00"
    work: "Simplified Method not applied, so the simple amount"
  - printed: "retirement[r1].taxable"
    value: "0.00"
    work: "IRA distribution, so the IRA taxable amount goes on line 4b"
  - printed: "retirement[r1].show_a"
    value: "yes"
    work: "Exception 2 applies (Roth IRA distribution, code Q)"
  - printed: "retirement[r1].amount_a"
    value: "25958.00"
    work: "Total distribution entered on line 4a"
  - printed: "retirement[r1].sav_excluded"
    value: "yes"
    work: "Inherited IRA received as a nonspouse beneficiary"
  - printed: "retirement[r1].sav_gross"
    value: "25958.00"
    work: "25,958 - 0 rolled over"
  - printed: "retirement[r1].sav_amount"
    value: "0.00"
    work: "Excluded from Form 8880 line 4"
  - printed: "retirement[r2].is_ira"
    value: "no"
    work: "Account kind is plan"
  - printed: "retirement[r2].roth"
    value: "no"
    work: "Not a Roth IRA"
  - printed: "retirement[r2].direct"
    value: "no"
    work: "Box 7 code is 7, not G"
  - printed: "retirement[r2].bad_code"
    value: "no"
    work: "Code 7 is a normal distribution; the special-situations question was answered no"
  - printed: "retirement[r2].rolled"
    value: "0.00"
    work: "Amount rolled over is $0; not a direct rollover"
  - printed: "retirement[r2].has_rollover"
    value: "no"
    work: "Nothing rolled over and no code G"
  - printed: "retirement[r2].smw1"
    value: "0.00"
    work: "Box 1"
  - printed: "retirement[r2].smw2"
    value: "30498.00"
    work: "Cost at the annuity starting date, as given"
  - printed: "retirement[r2].smw4_t1_360"
    value: "84.72"
    work: "30,498 / 360"
  - printed: "retirement[r2].smw4_t1_310"
    value: "98.38"
    work: "30,498 / 310"
  - printed: "retirement[r2].smw4_t1_260"
    value: "117.30"
    work: "30,498 / 260"
  - printed: "retirement[r2].smw4_t1_210"
    value: "145.23"
    work: "30,498 / 210"
  - printed: "retirement[r2].smw4_t1_160"
    value: "190.61"
    work: "30,498 / 160"
  - printed: "retirement[r2].smw4_t2_410"
    value: "74.39"
    work: "30,498 / 410"
  - printed: "retirement[r2].smw4_t2_360"
    value: "84.72"
    work: "30,498 / 360"
  - printed: "retirement[r2].smw4_t2_310"
    value: "98.38"
    work: "30,498 / 310"
  - printed: "retirement[r2].smw4_t2_260"
    value: "117.30"
    work: "30,498 / 260"
  - printed: "retirement[r2].smw4_t2_210"
    value: "145.23"
    work: "30,498 / 210"
  - printed: "retirement[r2].smw4_table1"
    value: "190.61"
    work: "Age 77 is 71 or older, after-11/18/1996 column, so divide by 160"
  - printed: "retirement[r2].smw4_table2"
    value: "145.23"
    work: "Combined ages 158 is 141 or older, so divide by 210"
  - printed: "retirement[r2].smw4_new"
    value: "145.23"
    work: "Joint-and-survivor annuity starting after 1997, so use Table 2"
  - printed: "retirement[r2].smw4"
    value: "0.00"
    work: "Worksheet completed last year, so use last year's line 4 of $0"
  - printed: "retirement[r2].smw5"
    value: "0.00"
    work: "0 x 12 months"
  - printed: "retirement[r2].smw6"
    value: "14678.00"
    work: "Last year's line 10"
  - printed: "retirement[r2].smw7"
    value: "15820.00"
    work: "30,498 - 14,678"
  - printed: "retirement[r2].smw8"
    value: "0.00"
    work: "Smaller of 0 or 15,820"
  - printed: "retirement[r2].smw9"
    value: "0.00"
    work: "0 - 0; not less than zero"
  - printed: "retirement[r2].smw10"
    value: "14678.00"
    work: "14,678 + 0"
  - printed: "retirement[r2].smw11"
    value: "15820.00"
    work: "30,498 - 14,678"
  - printed: "retirement[r2].cost_left"
    value: "yes"
    work: "Line 7 is 15,820, which is more than zero"
  - printed: "retirement[r2].annuity_with_cost"
    value: "no"
    work: "The Simplified Method does not apply (answered no)"
  - printed: "retirement[r2].annuity_rollover"
    value: "no"
    work: "Simplified Method not used and nothing rolled over"
  - printed: "retirement[r2].annuity_taxable"
    value: "0.00"
    work: "Not a Simplified Method annuity with cost left, so the whole of box 1, which is 0"
  - printed: "retirement[r2].ira_taxable"
    value: "0.00"
    work: "Box 1 of 0 less 0 rolled over"
  - printed: "retirement[r2].ira_not_rolled"
    value: "0.00"
    work: "0 - 0"
  - printed: "retirement[r2].plan_excluded"
    value: "545.00"
    work: "Box 5 of 545 + rolled over 0"
  - printed: "retirement[r2].plan_simple"
    value: "0.00"
    work: "0 - 545, floored at zero"
  - printed: "retirement[r2].plan_taxable"
    value: "0.00"
    work: "Simplified Method not applied, so the simple amount"
  - printed: "retirement[r2].taxable"
    value: "0.00"
    work: "Plan distribution, so the plan taxable amount goes on line 5b"
  - printed: "retirement[r2].show_a"
    value: "no"
    work: "Taxable amount equals box 1 (both 0), so no line 5a entry is needed"
  - printed: "retirement[r2].amount_a"
    value: "0.00"
    work: "No line 5a entry"
  - printed: "retirement[r2].sav_excluded"
    value: "no"
    work: "Not military retirement pay and not section 404(k) dividends"
  - printed: "retirement[r2].sav_gross"
    value: "0.00"
    work: "0 - 0 rolled over"
  - printed: "retirement[r2].sav_amount"
    value: "0.00"
    work: "Gross amount of 0 is counted"
```
```

### classm.retirement.2

```yaml
```yaml
lines:
  - printed: "retirement[r1].is_ira"
    value: "yes"
    work: "Account kind is traditional_ira, so it goes on lines 4a/4b"
  - printed: "retirement[r1].roth"
    value: "no"
    work: "Traditional IRA, not a Roth IRA"
  - printed: "retirement[r1].direct"
    value: "yes"
    work: "Box 7 code G is a direct rollover"
  - printed: "retirement[r1].bad_code"
    value: "no"
    work: "Code G is handled and no listed special situation applies"
  - printed: "retirement[r1].rolled"
    value: "0.00"
    work: "Direct rollover, so the whole box 1 amount of 0.00 is rolled over"
  - printed: "retirement[r1].has_rollover"
    value: "yes"
    work: "Direct rollover, code G"
  - printed: "retirement[r1].smw1"
    value: "0.00"
    work: "Box 1"
  - printed: "retirement[r1].smw2"
    value: "3060.00"
    work: "Cost in the plan as given"
  - printed: "retirement[r1].smw4_t1_360"
    value: "8.50"
    work: "3060/360"
  - printed: "retirement[r1].smw4_t1_310"
    value: "9.87"
    work: "3060/310"
  - printed: "retirement[r1].smw4_t1_260"
    value: "11.77"
    work: "3060/260"
  - printed: "retirement[r1].smw4_t1_210"
    value: "14.57"
    work: "3060/210"
  - printed: "retirement[r1].smw4_t1_160"
    value: "19.13"
    work: "3060/160 = 19.125, rounded"
  - printed: "retirement[r1].smw4_t2_410"
    value: "7.46"
    work: "3060/410"
  - printed: "retirement[r1].smw4_t2_360"
    value: "8.50"
    work: "3060/360"
  - printed: "retirement[r1].smw4_t2_310"
    value: "9.87"
    work: "3060/310"
  - printed: "retirement[r1].smw4_t2_260"
    value: "11.77"
    work: "3060/260"
  - printed: "retirement[r1].smw4_t2_210"
    value: "14.57"
    work: "3060/210"
  - printed: "retirement[r1].smw4_table1"
    value: "11.77"
    work: "Age 65 falls in 61-65; after 11/18/1996 column gives 260"
  - printed: "retirement[r1].smw4_table2"
    value: "9.87"
    work: "Combined ages 128 fall in 121-130, which gives 310"
  - printed: "retirement[r1].smw4_new"
    value: "11.77"
    work: "Not a joint-life annuity after 1997, so Table 1 applies"
  - printed: "retirement[r1].smw4"
    value: "11.77"
    work: "Worksheet not completed last year, so use line 2 / line 3"
  - printed: "retirement[r1].smw5"
    value: "141.24"
    work: "11.77 x 12"
  - printed: "retirement[r1].smw6"
    value: "12495.00"
    work: "Amount recovered tax free after 1986, as given"
  - printed: "retirement[r1].smw7"
    value: "-9435.00"
    work: "3060 - 12495"
  - printed: "retirement[r1].smw8"
    value: "-9435.00"
    work: "Smaller of 141.24 or -9435"
  - printed: "retirement[r1].smw9"
    value: "9435.00"
    work: "0 - (-9435), not less than zero"
  - printed: "retirement[r1].smw10"
    value: "3060.00"
    work: "12495 + (-9435)"
  - printed: "retirement[r1].smw11"
    value: "0.00"
    work: "3060 - 3060"
  - printed: "retirement[r1].cost_left"
    value: "no"
    work: "Line 7 is not more than zero"
  - printed: "retirement[r1].annuity_with_cost"
    value: "no"
    work: "The Simplified Method does not apply and no cost is left"
  - printed: "retirement[r1].annuity_rollover"
    value: "no"
    work: "The Simplified Method does not apply"
  - printed: "retirement[r1].annuity_taxable"
    value: "0.00"
    work: "No cost is left, so the whole of box 1 (0.00)"
  - printed: "retirement[r1].ira_taxable"
    value: "0.00"
    work: "Exception 1: the part not rolled over is 0"
  - printed: "retirement[r1].ira_not_rolled"
    value: "0.00"
    work: "0 - 0"
  - printed: "retirement[r1].plan_excluded"
    value: "0.00"
    work: "Box 5 of 0 plus rolled amount of 0"
  - printed: "retirement[r1].plan_simple"
    value: "0.00"
    work: "0 - 0"
  - printed: "retirement[r1].plan_taxable"
    value: "0.00"
    work: "The Simplified Method does not apply, so use plan_simple"
  - printed: "retirement[r1].taxable"
    value: "0.00"
    work: "IRA, so the line 4b amount is ira_taxable"
  - printed: "retirement[r1].show_a"
    value: "yes"
    work: "Exception 1 (rollover) applies"
  - printed: "retirement[r1].amount_a"
    value: "0.00"
    work: "Total distribution from box 1 goes on line 4a"
  - printed: "retirement[r1].sav_excluded"
    value: "no"
    work: "Not an inherited IRA received by a nonspouse beneficiary"
  - printed: "retirement[r1].sav_gross"
    value: "0.00"
    work: "Box 1 is 0"
  - printed: "retirement[r1].sav_amount"
    value: "0.00"
    work: "Nothing to count on Form 8880 line 4"
  - printed: "retirement[r2].is_ira"
    value: "no"
    work: "Account kind is plan, so it goes on lines 5a/5b"
  - printed: "retirement[r2].roth"
    value: "no"
    work: "Not a Roth IRA"
  - printed: "retirement[r2].direct"
    value: "no"
    work: "Box 7 code is 4, not G"
  - printed: "retirement[r2].bad_code"
    value: "no"
    work: "Code 4 (death) is handled and no listed special situation applies"
  - printed: "retirement[r2].rolled"
    value: "0.00"
    work: "No amount was rolled over"
  - printed: "retirement[r2].has_rollover"
    value: "no"
    work: "No rollover and not code G"
  - printed: "retirement[r2].smw1"
    value: "26827.00"
    work: "Box 1"
  - printed: "retirement[r2].smw2"
    value: "15431.00"
    work: "Cost in the plan as given"
  - printed: "retirement[r2].smw4_t1_360"
    value: "42.86"
    work: "15431/360"
  - printed: "retirement[r2].smw4_t1_310"
    value: "49.78"
    work: "15431/310"
  - printed: "retirement[r2].smw4_t1_260"
    value: "59.35"
    work: "15431/260"
  - printed: "retirement[r2].smw4_t1_210"
    value: "73.48"
    work: "15431/210"
  - printed: "retirement[r2].smw4_t1_160"
    value: "96.44"
    work: "15431/160"
  - printed: "retirement[r2].smw4_t2_410"
    value: "37.64"
    work: "15431/410"
  - printed: "retirement[r2].smw4_t2_360"
    value: "42.86"
    work: "15431/360"
  - printed: "retirement[r2].smw4_t2_310"
    value: "49.78"
    work: "15431/310"
  - printed: "retirement[r2].smw4_t2_260"
    value: "59.35"
    work: "15431/260"
  - printed: "retirement[r2].smw4_t2_210"
    value: "73.48"
    work: "15431/210"
  - printed: "retirement[r2].smw4_table1"
    value: "73.48"
    work: "Age 68 falls in 66-70; after 11/18/1996 column gives 210"
  - printed: "retirement[r2].smw4_table2"
    value: "42.86"
    work: "Combined ages 117 fall in 111-120, which gives 360"
  - printed: "retirement[r2].smw4_new"
    value: "73.48"
    work: "Not a joint-life annuity after 1997, so Table 1 applies"
  - printed: "retirement[r2].smw4"
    value: "73.48"
    work: "Worksheet not completed last year, so use line 2 / line 3"
  - printed: "retirement[r2].smw5"
    value: "514.36"
    work: "73.48 x 7"
  - printed: "retirement[r2].smw6"
    value: "41795.00"
    work: "Amount recovered tax free after 1986, as given"
  - printed: "retirement[r2].smw7"
    value: "-26364.00"
    work: "15431 - 41795"
  - printed: "retirement[r2].smw8"
    value: "-26364.00"
    work: "Smaller of 514.36 or -26364"
  - printed: "retirement[r2].smw9"
    value: "53191.00"
    work: "26827 - (-26364), not less than zero"
  - printed: "retirement[r2].smw10"
    value: "15431.00"
    work: "41795 + (-26364)"
  - printed: "retirement[r2].smw11"
    value: "0.00"
    work: "15431 - 15431"
  - printed: "retirement[r2].cost_left"
    value: "no"
    work: "Line 7 is not more than zero"
  - printed: "retirement[r2].annuity_with_cost"
    value: "no"
    work: "The Simplified Method applies but no cost is left"
  - printed: "retirement[r2].annuity_rollover"
    value: "no"
    work: "Nothing was rolled over"
  - printed: "retirement[r2].annuity_taxable"
    value: "26827.00"
    work: "Cost is fully recovered, so the whole of box 1 is taxable"
  - printed: "retirement[r2].ira_taxable"
    value: "26827.00"
    work: "Part not rolled over is 26827 - 0"
  - printed: "retirement[r2].ira_not_rolled"
    value: "26827.00"
    work: "26827 - 0"
  - printed: "retirement[r2].plan_excluded"
    value: "0.00"
    work: "Box 5 of 0 plus rolled amount of 0"
  - printed: "retirement[r2].plan_simple"
    value: "26827.00"
    work: "26827 - 0"
  - printed: "retirement[r2].plan_taxable"
    value: "26827.00"
    work: "Simplified Method with cost recovered: whole of box 1"
  - printed: "retirement[r2].taxable"
    value: "26827.00"
    work: "Plan, so the line 5b amount is plan_taxable"
  - printed: "retirement[r2].show_a"
    value: "no"
    work: "Fully taxable, so no entry on line 5a"
  - printed: "retirement[r2].amount_a"
    value: "0.00"
    work: "None when fully taxable"
  - printed: "retirement[r2].sav_excluded"
    value: "no"
    work: "Not a military plan and not section 404(k) dividends"
  - printed: "retirement[r2].sav_gross"
    value: "26827.00"
    work: "26827 - 0 rolled over"
  - printed: "retirement[r2].sav_amount"
    value: "26827.00"
    work: "Counted on Form 8880 line 4"
```
```

### classm.retirement.3

```yaml
```yaml
lines:
  - printed: "retirement[r1].is_ira"
    value: "yes"
    work: "Kind of account = traditional_ira, so the distribution goes on lines 4a/4b"
  - printed: "retirement[r1].roth"
    value: "no"
    work: "The account is a traditional IRA, not a Roth IRA"
  - printed: "retirement[r1].direct"
    value: "no"
    work: "Box 7 code is normal_7, not G"
  - printed: "retirement[r1].bad_code"
    value: "no"
    work: "Code 7 (normal distribution) is handled"
  - printed: "retirement[r1].rolled"
    value: "0.00"
    work: "Amount rolled over is $0; not a direct rollover"
  - printed: "retirement[r1].has_rollover"
    value: "no"
    work: "Amount rolled over is 0 and the code is not G"
  - printed: "retirement[r1].smw1"
    value: "0.00"
    work: "Line 1 = box 1 = 0.00"
  - printed: "retirement[r1].smw2"
    value: "42431.00"
    work: "Line 2 = cost in the plan = 42,431"
  - printed: "retirement[r1].smw4_t1_360"
    value: "117.86"
    work: "42,431 / 360 = 117.86"
  - printed: "retirement[r1].smw4_t1_310"
    value: "136.87"
    work: "42,431 / 310 = 136.87"
  - printed: "retirement[r1].smw4_t1_260"
    value: "163.20"
    work: "42,431 / 260 = 163.20"
  - printed: "retirement[r1].smw4_t1_210"
    value: "202.05"
    work: "42,431 / 210 = 202.05"
  - printed: "retirement[r1].smw4_t1_160"
    value: "265.19"
    work: "42,431 / 160 = 265.19"
  - printed: "retirement[r1].smw4_t2_410"
    value: "103.49"
    work: "42,431 / 410 = 103.49"
  - printed: "retirement[r1].smw4_t2_360"
    value: "117.86"
    work: "42,431 / 360 = 117.86"
  - printed: "retirement[r1].smw4_t2_310"
    value: "136.87"
    work: "42,431 / 310 = 136.87"
  - printed: "retirement[r1].smw4_t2_260"
    value: "163.20"
    work: "42,431 / 260 = 163.20"
  - printed: "retirement[r1].smw4_t2_210"
    value: "202.05"
    work: "42,431 / 210 = 202.05"
  - printed: "retirement[r1].smw4_table1"
    value: "202.05"
    work: "Age 67 falls in 66-70; Table 1 (after Nov 18, 1996) gives 210; 42,431 / 210"
  - printed: "retirement[r1].smw4_table2"
    value: "202.05"
    work: "Combined ages 148 is 141 or older; Table 2 gives 210; 42,431 / 210"
  - printed: "retirement[r1].smw4_new"
    value: "202.05"
    work: "Not a joint-and-survivor annuity starting after 1997, so Table 1 applies"
  - printed: "retirement[r1].smw4"
    value: "1801.00"
    work: "Worksheet completed last year, so use last year's line 4 = 1,801"
  - printed: "retirement[r1].smw5"
    value: "21612.00"
    work: "1,801 x 12 months = 21,612"
  - printed: "retirement[r1].smw6"
    value: "0.00"
    work: "Last year's line 10 = 0"
  - printed: "retirement[r1].smw7"
    value: "42431.00"
    work: "42,431 - 0 = 42,431"
  - printed: "retirement[r1].smw8"
    value: "21612.00"
    work: "Smaller of 21,612 or 42,431"
  - printed: "retirement[r1].smw9"
    value: "0.00"
    work: "0 - 21,612 is less than zero, so enter 0"
  - printed: "retirement[r1].smw10"
    value: "21612.00"
    work: "0 + 21,612 = 21,612"
  - printed: "retirement[r1].smw11"
    value: "20819.00"
    work: "42,431 - 21,612 = 20,819"
  - printed: "retirement[r1].cost_left"
    value: "yes"
    work: "Line 7 = 42,431, which is more than 0"
  - printed: "retirement[r1].annuity_with_cost"
    value: "no"
    work: "Filer answered no: the Simplified Method does not apply"
  - printed: "retirement[r1].annuity_rollover"
    value: "no"
    work: "Not a Simplified Method annuity and nothing was rolled over"
  - printed: "retirement[r1].annuity_taxable"
    value: "0.00"
    work: "Simplified Method not applied, so use the whole of box 1 = 0"
  - printed: "retirement[r1].ira_taxable"
    value: "0.00"
    work: "Part not rolled over = 0 - 0 = 0"
  - printed: "retirement[r1].ira_not_rolled"
    value: "0.00"
    work: "Box 1 0 - rolled 0 = 0"
  - printed: "retirement[r1].plan_excluded"
    value: "0.00"
    work: "Box 5 0 + rolled 0 = 0"
  - printed: "retirement[r1].plan_simple"
    value: "0.00"
    work: "0 - 0 = 0"
  - printed: "retirement[r1].plan_taxable"
    value: "0.00"
    work: "Not a plan distribution; amount is 0"
  - printed: "retirement[r1].taxable"
    value: "0.00"
    work: "IRA taxable amount for line 4b = 0"
  - printed: "retirement[r1].show_a"
    value: "no"
    work: "No exception applies; the distribution is fully taxable, so only line 4b is used"
  - printed: "retirement[r1].amount_a"
    value: "0.00"
    work: "Nothing is entered on line 4a when fully taxable"
  - printed: "retirement[r1].sav_excluded"
    value: "no"
    work: "Not an inherited IRA from a nonspouse"
  - printed: "retirement[r1].sav_gross"
    value: "0.00"
    work: "Box 1 0 - rolled 0 = 0"
  - printed: "retirement[r1].sav_amount"
    value: "0.00"
    work: "Form 8880 line 4 counts the distribution of 0"
  - printed: "retirement[r2].is_ira"
    value: "no"
    work: "Kind of account = plan, so the distribution goes on lines 5a/5b"
  - printed: "retirement[r2].roth"
    value: "no"
    work: "Not a Roth account"
  - printed: "retirement[r2].direct"
    value: "no"
    work: "Box 7 code is normal_7, not G"
  - printed: "retirement[r2].bad_code"
    value: "no"
    work: "Code 7 (normal distribution) is handled"
  - printed: "retirement[r2].rolled"
    value: "0.00"
    work: "Amount rolled over is $0"
  - printed: "retirement[r2].has_rollover"
    value: "no"
    work: "Amount rolled over is 0 and the code is not G"
  - printed: "retirement[r2].smw1"
    value: "41168.00"
    work: "Line 1 = box 1 = 41,168"
  - printed: "retirement[r2].smw2"
    value: "29819.00"
    work: "Line 2 = cost in the plan = 29,819"
  - printed: "retirement[r2].smw4_t1_360"
    value: "82.83"
    work: "29,819 / 360 = 82.83"
  - printed: "retirement[r2].smw4_t1_310"
    value: "96.19"
    work: "29,819 / 310 = 96.19"
  - printed: "retirement[r2].smw4_t1_260"
    value: "114.69"
    work: "29,819 / 260 = 114.69"
  - printed: "retirement[r2].smw4_t1_210"
    value: "142.00"
    work: "29,819 / 210 = 142.00"
  - printed: "retirement[r2].smw4_t1_160"
    value: "186.37"
    work: "29,819 / 160 = 186.37"
  - printed: "retirement[r2].smw4_t2_410"
    value: "72.73"
    work: "29,819 / 410 = 72.73"
  - printed: "retirement[r2].smw4_t2_360"
    value: "82.83"
    work: "29,819 / 360 = 82.83"
  - printed: "retirement[r2].smw4_t2_310"
    value: "96.19"
    work: "29,819 / 310 = 96.19"
  - printed: "retirement[r2].smw4_t2_260"
    value: "114.69"
    work: "29,819 / 260 = 114.69"
  - printed: "retirement[r2].smw4_t2_210"
    value: "142.00"
    work: "29,819 / 210 = 142.00"
  - printed: "retirement[r2].smw4_table1"
    value: "82.83"
    work: "Age 51 is 55 or under; Table 1 gives 360; 29,819 / 360"
  - printed: "retirement[r2].smw4_table2"
    value: "114.69"
    work: "Combined ages 136 falls in 131-140; Table 2 gives 260; 29,819 / 260"
  - printed: "retirement[r2].smw4_new"
    value: "114.69"
    work: "Joint-and-survivor annuity starting after 1997, so Table 2 applies"
  - printed: "retirement[r2].smw4"
    value: "816.00"
    work: "Worksheet completed last year, so use last year's line 4 = 816"
  - printed: "retirement[r2].smw5"
    value: "9792.00"
    work: "816 x 12 months = 9,792"
  - printed: "retirement[r2].smw6"
    value: "0.00"
    work: "Last year's line 10 = 0"
  - printed: "retirement[r2].smw7"
    value: "29819.00"
    work: "29,819 - 0 = 29,819"
  - printed: "retirement[r2].smw8"
    value: "9792.00"
    work: "Smaller of 9,792 or 29,819"
  - printed: "retirement[r2].smw9"
    value: "31376.00"
    work: "41,168 - 9,792 = 31,376"
  - printed: "retirement[r2].smw10"
    value: "9792.00"
    work: "0 + 9,792 = 9,792"
  - printed: "retirement[r2].smw11"
    value: "20027.00"
    work: "29,819 - 9,792 = 20,027"
  - printed: "retirement[r2].cost_left"
    value: "yes"
    work: "Line 7 = 29,819, which is more than 0"
  - printed: "retirement[r2].annuity_with_cost"
    value: "no"
    work: "Filer answered no: the Simplified Method does not apply"
  - printed: "retirement[r2].annuity_rollover"
    value: "no"
    work: "Not a Simplified Method annuity and nothing was rolled over"
  - printed: "retirement[r2].annuity_taxable"
    value: "41168.00"
    work: "Simplified Method not applied, so use the whole of box 1 = 41,168"
  - printed: "retirement[r2].ira_taxable"
    value: "0.00"
    work: "Not an IRA distribution"
  - printed: "retirement[r2].ira_not_rolled"
    value: "41168.00"
    work: "41,168 - 0 = 41,168"
  - printed: "retirement[r2].plan_excluded"
    value: "2657.00"
    work: "Box 5 2,657 + rolled 0 = 2,657"
  - printed: "retirement[r2].plan_simple"
    value: "38511.00"
    work: "41,168 - 2,657 - 0 = 38,511"
  - printed: "retirement[r2].plan_taxable"
    value: "38511.00"
    work: "Simplified Method not applied, so box 1 less box 5 and rollover = 38,511"
  - printed: "retirement[r2].taxable"
    value: "38511.00"
    work: "Line 5b = plan taxable amount 38,511"
  - printed: "retirement[r2].show_a"
    value: "yes"
    work: "Partially taxable (38,511 < 41,168), so the total distribution goes on line 5a"
  - printed: "retirement[r2].amount_a"
    value: "41168.00"
    work: "Line 5a = box 1 = 41,168"
  - printed: "retirement[r2].sav_excluded"
    value: "yes"
    work: "Distribution from a military retirement plan is excluded from Form 8880 line 4"
  - printed: "retirement[r2].sav_gross"
    value: "41168.00"
    work: "41,168 - 0 rolled = 41,168"
  - printed: "retirement[r2].sav_amount"
    value: "0.00"
    work: "Excluded military distribution, so 0 on Form 8880 line 4"
```
```

### classm.retirement.4

```yaml
lines:
  - printed: "retirement[r1].is_ira"
    value: "no"
    work: "Account kind is plan, so this goes on lines 5a/5b"
  - printed: "retirement[r1].roth"
    value: "no"
    work: "Not a Roth IRA"
  - printed: "retirement[r1].direct"
    value: "no"
    work: "Box 7 code is 7, not G"
  - printed: "retirement[r1].bad_code"
    value: "no"
    work: "Code 7 is a normal distribution and no special situation applies"
  - printed: "retirement[r1].rolled"
    value: "0.00"
    work: "Amount rolled over is $0 and there is no direct rollover"
  - printed: "retirement[r1].has_rollover"
    value: "no"
    work: "Nothing rolled over and not code G"
  - printed: "retirement[r1].smw1"
    value: "34952.00"
    work: "Box 1"
  - printed: "retirement[r1].smw2"
    value: "82373.00"
    work: "Cost in the plan at the annuity starting date"
  - printed: "retirement[r1].smw4_t1_360"
    value: "228.81"
    work: "82373/360"
  - printed: "retirement[r1].smw4_t1_310"
    value: "265.72"
    work: "82373/310"
  - printed: "retirement[r1].smw4_t1_260"
    value: "316.82"
    work: "82373/260"
  - printed: "retirement[r1].smw4_t1_210"
    value: "392.25"
    work: "82373/210"
  - printed: "retirement[r1].smw4_t1_160"
    value: "514.83"
    work: "82373/160"
  - printed: "retirement[r1].smw4_t2_410"
    value: "200.91"
    work: "82373/410"
  - printed: "retirement[r1].smw4_t2_360"
    value: "228.81"
    work: "82373/360"
  - printed: "retirement[r1].smw4_t2_310"
    value: "265.72"
    work: "82373/310"
  - printed: "retirement[r1].smw4_t2_260"
    value: "316.82"
    work: "82373/260"
  - printed: "retirement[r1].smw4_t2_210"
    value: "392.25"
    work: "82373/210"
  - printed: "retirement[r1].smw4_table1"
    value: "514.83"
    work: "Age 76 is 71 or older and the start date is after 11/18/1996, so Table 1 gives 160"
  - printed: "retirement[r1].smw4_table2"
    value: "392.25"
    work: "Combined ages 157 is 141 or older, so Table 2 gives 210"
  - printed: "retirement[r1].smw4_new"
    value: "514.83"
    work: "Not a joint and survivor annuity, so use Table 1"
  - printed: "retirement[r1].smw4"
    value: "514.83"
    work: "Worksheet not completed last year, so use line 2 divided by line 3"
  - printed: "retirement[r1].smw5"
    value: "6177.96"
    work: "514.83 x 12"
  - printed: "retirement[r1].smw6"
    value: "0.00"
    work: "Nothing recovered tax free after 1986"
  - printed: "retirement[r1].smw7"
    value: "82373.00"
    work: "82373 - 0"
  - printed: "retirement[r1].smw8"
    value: "6177.96"
    work: "Smaller of 6177.96 and 82373"
  - printed: "retirement[r1].smw9"
    value: "28774.04"
    work: "34952 - 6177.96"
  - printed: "retirement[r1].smw10"
    value: "6177.96"
    work: "0 + 6177.96"
  - printed: "retirement[r1].smw11"
    value: "76195.04"
    work: "82373 - 6177.96"
  - printed: "retirement[r1].cost_left"
    value: "yes"
    work: "Line 7 is 82373, more than zero"
  - printed: "retirement[r1].annuity_with_cost"
    value: "yes"
    work: "Simplified Method applies and cost is left"
  - printed: "retirement[r1].annuity_rollover"
    value: "no"
    work: "Nothing rolled over"
  - printed: "retirement[r1].annuity_taxable"
    value: "28774.04"
    work: "Simplified Method line 9"
  - printed: "retirement[r1].ira_taxable"
    value: "0.00"
    work: "Not an IRA"
  - printed: "retirement[r1].ira_not_rolled"
    value: "34952.00"
    work: "34952 - 0"
  - printed: "retirement[r1].plan_excluded"
    value: "0.00"
    work: "Box 5 is 0 and rolled over is 0"
  - printed: "retirement[r1].plan_simple"
    value: "34952.00"
    work: "34952 - 0"
  - printed: "retirement[r1].plan_taxable"
    value: "28774.04"
    work: "Annuity with after-tax cost, so use the Simplified Method"
  - printed: "retirement[r1].taxable"
    value: "28774.04"
    work: "Line 5b"
  - printed: "retirement[r1].show_a"
    value: "yes"
    work: "Partially taxable annuity, so the total goes on line 5a"
  - printed: "retirement[r1].amount_a"
    value: "34952.00"
    work: "Simplified Method Worksheet line 1, entered on line 5a"
  - printed: "retirement[r1].sav_excluded"
    value: "no"
    work: "Not a military plan and not 404(k) dividends"
  - printed: "retirement[r1].sav_gross"
    value: "34952.00"
    work: "34952 - 0 rolled over"
  - printed: "retirement[r1].sav_amount"
    value: "34952.00"
    work: "Counts on Form 8880 line 4"
  - printed: "retirement[r2].is_ira"
    value: "yes"
    work: "Account kind is roth_ira"
  - printed: "retirement[r2].roth"
    value: "yes"
    work: "Roth IRA"
  - printed: "retirement[r2].direct"
    value: "no"
    work: "Code Q, not G"
  - printed: "retirement[r2].bad_code"
    value: "no"
    work: "Code Q is handled by Exception 2(b)"
  - printed: "retirement[r2].rolled"
    value: "0.00"
    work: "Nothing rolled over"
  - printed: "retirement[r2].has_rollover"
    value: "no"
    work: "Nothing rolled over and not code G"
  - printed: "retirement[r2].smw1"
    value: "0.00"
    work: "Box 1"
  - printed: "retirement[r2].smw2"
    value: "6690.00"
    work: "Cost given"
  - printed: "retirement[r2].smw4_t1_360"
    value: "18.58"
    work: "6690/360"
  - printed: "retirement[r2].smw4_t1_310"
    value: "21.58"
    work: "6690/310"
  - printed: "retirement[r2].smw4_t1_260"
    value: "25.73"
    work: "6690/260"
  - printed: "retirement[r2].smw4_t1_210"
    value: "31.86"
    work: "6690/210"
  - printed: "retirement[r2].smw4_t1_160"
    value: "41.81"
    work: "6690/160"
  - printed: "retirement[r2].smw4_t2_410"
    value: "16.32"
    work: "6690/410"
  - printed: "retirement[r2].smw4_t2_360"
    value: "18.58"
    work: "6690/360"
  - printed: "retirement[r2].smw4_t2_310"
    value: "21.58"
    work: "6690/310"
  - printed: "retirement[r2].smw4_t2_260"
    value: "25.73"
    work: "6690/260"
  - printed: "retirement[r2].smw4_t2_210"
    value: "31.86"
    work: "6690/210"
  - printed: "retirement[r2].smw4_table1"
    value: "21.58"
    work: "Age 59 is in 56-60 and after 11/18/1996, so 310"
  - printed: "retirement[r2].smw4_table2"
    value: "18.58"
    work: "Combined ages 115 is in 111-120, so 360"
  - printed: "retirement[r2].smw4_new"
    value: "21.58"
    work: "Not a joint and survivor annuity, so use Table 1"
  - printed: "retirement[r2].smw4"
    value: "21.58"
    work: "Worksheet not completed last year"
  - printed: "retirement[r2].smw5"
    value: "258.96"
    work: "21.58 x 12"
  - printed: "retirement[r2].smw6"
    value: "46308.00"
    work: "Amount recovered after 1986"
  - printed: "retirement[r2].smw7"
    value: "-39618.00"
    work: "6690 - 46308"
  - printed: "retirement[r2].smw8"
    value: "-39618.00"
    work: "Smaller of 258.96 and -39618"
  - printed: "retirement[r2].smw9"
    value: "39618.00"
    work: "0 - (-39618), not less than zero; worksheet not used for this entry"
  - printed: "retirement[r2].smw10"
    value: "6690.00"
    work: "46308 + (-39618)"
  - printed: "retirement[r2].smw11"
    value: "0.00"
    work: "6690 - 6690"
  - printed: "retirement[r2].cost_left"
    value: "no"
    work: "Line 7 is not more than zero"
  - printed: "retirement[r2].annuity_with_cost"
    value: "no"
    work: "Simplified Method does not apply"
  - printed: "retirement[r2].annuity_rollover"
    value: "no"
    work: "Not a Simplified Method annuity and nothing rolled over"
  - printed: "retirement[r2].annuity_taxable"
    value: "0.00"
    work: "Not an annuity, and box 1 is 0"
  - printed: "retirement[r2].ira_taxable"
    value: "0.00"
    work: "Code Q, so enter -0- on line 4b under Exception 2(b)"
  - printed: "retirement[r2].ira_not_rolled"
    value: "0.00"
    work: "0 - 0"
  - printed: "retirement[r2].plan_excluded"
    value: "0.00"
    work: "Box 5 is 0 and rolled over is 0"
  - printed: "retirement[r2].plan_simple"
    value: "0.00"
    work: "0 - 0"
  - printed: "retirement[r2].plan_taxable"
    value: "0.00"
    work: "Not a plan distribution"
  - printed: "retirement[r2].taxable"
    value: "0.00"
    work: "Line 4b is -0- for code Q"
  - printed: "retirement[r2].show_a"
    value: "yes"
    work: "Exception 2: distribution from a Roth IRA"
  - printed: "retirement[r2].amount_a"
    value: "0.00"
    work: "Box 1 total is 0"
  - printed: "retirement[r2].sav_excluded"
    value: "no"
    work: "Not an inherited IRA received as a nonspouse beneficiary"
  - printed: "retirement[r2].sav_gross"
    value: "0.00"
    work: "0 - 0"
  - printed: "retirement[r2].sav_amount"
    value: "0.00"
    work: "Distribution is 0"
```
