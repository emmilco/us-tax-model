# Class M hand-work — retirement

`Form 1099-R distributions (IRAs, pensions and annuities)` worked by hand by an isolated model from its archived pages and the amounts flowing into it, for generated returns that together take every reachable branch (spec 6.1, class M; spec 6.5). Agreements are class M fixtures in `fixtures/2025/classm.json`; each disagreement carries a ruling.

| field | value |
| --- | --- |
| date | 2026-10-18 |
| model requested | claude-opus-5-5 |
| model reported | claude-opus-5-5 |
| cases | 11 |

## Source pages given to the model

| document | revision | pages | selection | text sha256 | reading-order pages | cols sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| f1099r | 2025 (calendar-year form) | - | cited pages | 97b0b54ae7c95303418077d54e349c0106cbbd5c4b5695ef684c23c39a5fda3f | - | af300d066f4492afc97aa90824bfc681581f64482976e6d6a705e7e94b0e4e67 |
| i1040gi | 2025; printed date 2026-02-25 | 26, 27, 28, 29, 30, 31 | cited pages | 6024dc94dd1f545ed6e2068a42ea11859be546e8fe18ec3082021259f9b45ff1 | 26, 27, 28, 30, 31 | af24119d58f0b99fbe0f83494c36b62e6d043170ab7fe810469f9c5230cf8420 |

## Lines

### case classm.retirement.1 — prompt sha256 07e795e23f4dcc01b85c8f1a9d854acf1a34175c0dfb004a1e0337e14a261cea; branches: retirement.special:false, retirement.annuity:true, retirement.used_last_year:false, retirement.joint_life:true, retirement.is_ira:false, retirement.is_ira:true, retirement.roth:false, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw4_table2#2, retirement.smw4_new#0, retirement.smw4#1, retirement.smw8:left, retirement.smw9:positive, retirement.cost_left:true, retirement.annuity_with_cost:true, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.ira_taxable#1, retirement.ira_not_rolled:floor, retirement.plan_taxable#0, retirement.taxable#0, retirement.taxable#1, retirement.show_a:false, retirement.show_a:true, retirement.amount_a#0, retirement.amount_a#1

### classm.retirement.1 — retirement[r1].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: yes

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

### classm.retirement.1 — retirement[r1].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r1].ira_taxable — Taxable IRA amount: the part not rolled over (zero for a qualified Roth IRA dist
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r1].ira_not_rolled — Box 1 less the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r1].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $0.00

### classm.retirement.1 — retirement[r1].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r1].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
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

Value: $46,647.00

### classm.retirement.1 — retirement[r2].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $122,313.00

### classm.retirement.1 — retirement[r2].smw4_t2_310 — Line 2 divided by 310 (Table 2)
Status: **AGREE**

Value: $394.56

### classm.retirement.1 — retirement[r2].smw4_table2 — Line 2 divided by the Table 2 number for the combined ages at the annuity starti
Status: **AGREE**

Value: $394.56

### classm.retirement.1 — retirement[r2].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $394.56

### classm.retirement.1 — retirement[r2].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $394.56

### classm.retirement.1 — retirement[r2].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $4,734.72

### classm.retirement.1 — retirement[r2].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $47,260.00

### classm.retirement.1 — retirement[r2].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $75,053.00

### classm.retirement.1 — retirement[r2].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $4,734.72

### classm.retirement.1 — retirement[r2].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $41,912.28

### classm.retirement.1 — retirement[r2].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: yes

### classm.retirement.1 — retirement[r2].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: yes

### classm.retirement.1 — retirement[r2].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.1 — retirement[r2].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $41,912.28

### classm.retirement.1 — retirement[r2].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $41,912.28

### classm.retirement.1 — retirement[r2].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $41,912.28

### classm.retirement.1 — retirement[r2].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: yes

### classm.retirement.1 — retirement[r2].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $46,647.00

### case classm.retirement.2 — prompt sha256 418f8473a881171e42058c76ebbbae8930044e62766e9f95a0fde052e8abfb82; branches: retirement.special:false, retirement.annuity:false, retirement.annuity:true, retirement.used_last_year:true, retirement.is_ira:false, retirement.roth:false, retirement.direct:false, retirement.direct:true, retirement.bad_code:false, retirement.rolled#0, retirement.rolled#1, retirement.has_rollover:false, retirement.has_rollover:true, retirement.smw4#0, retirement.smw8:left, retirement.smw9:floor, retirement.cost_left:true, retirement.annuity_with_cost:true, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.plan_simple:floor, retirement.plan_taxable#0, retirement.plan_taxable#1, retirement.taxable#1, retirement.show_a:true, retirement.amount_a#0

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

Value: $98,901.00

### classm.retirement.2 — retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $1,165.00

### classm.retirement.2 — retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $13,980.00

### classm.retirement.2 — retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $25,500.00

### classm.retirement.2 — retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $73,401.00

### classm.retirement.2 — retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $13,980.00

### classm.retirement.2 — retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $0.00

### classm.retirement.2 — retirement[r1].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: yes

### classm.retirement.2 — retirement[r1].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: yes

### classm.retirement.2 — retirement[r1].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r1].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
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

### classm.retirement.2 — retirement[r2].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r2].direct — Direct rollover (code G)
Status: **AGREE**

Value: yes

### classm.retirement.2 — retirement[r2].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r2].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $11,322.00

### classm.retirement.2 — retirement[r2].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: yes

### classm.retirement.2 — retirement[r2].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.2 — retirement[r2].plan_excluded — Taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $11,322.00

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

Value: $11,322.00

### case classm.retirement.3 — prompt sha256 ffd3c64c77cd7d59114ec3c5944d8ed3f52d624c0563fbef412a5f881c6c2f58; branches: retirement.special:false, retirement.annuity:true, retirement.used_last_year:false, retirement.joint_life:false, retirement.is_ira:false, retirement.is_ira:true, retirement.roth:false, retirement.roth:true, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw4_table1#3, retirement.smw4_new#1, retirement.smw4#1, retirement.smw8:left, retirement.smw9:positive, retirement.cost_left:true, retirement.annuity_with_cost:true, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.ira_taxable#0, retirement.plan_taxable#0, retirement.taxable#0, retirement.taxable#1, retirement.show_a:true, retirement.amount_a#0

### classm.retirement.3 — retirement[r1].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: no

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

Value: $18,476.00

### classm.retirement.3 — retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $143,786.00

### classm.retirement.3 — retirement[r1].smw4_t1_210 — Line 2 divided by 210 (Table 1)
Status: **AGREE**

Value: $684.70

### classm.retirement.3 — retirement[r1].smw4_table1 — Line 2 divided by the Table 1 number for the age at the annuity starting date
Status: **AGREE**

Value: $684.70

### classm.retirement.3 — retirement[r1].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $684.70

### classm.retirement.3 — retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $684.70

### classm.retirement.3 — retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $3,423.50

### classm.retirement.3 — retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $45,880.00

### classm.retirement.3 — retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $97,906.00

### classm.retirement.3 — retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $3,423.50

### classm.retirement.3 — retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $15,052.50

### classm.retirement.3 — retirement[r1].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: yes

### classm.retirement.3 — retirement[r1].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: yes

### classm.retirement.3 — retirement[r1].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.3 — retirement[r1].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $15,052.50

### classm.retirement.3 — retirement[r1].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $15,052.50

### classm.retirement.3 — retirement[r1].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $15,052.50

### classm.retirement.3 — retirement[r1].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: yes

### classm.retirement.3 — retirement[r1].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $18,476.00

### classm.retirement.3 — retirement[r2].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: yes

### classm.retirement.3 — retirement[r2].roth — Roth IRA distribution
Status: **AGREE**

Value: yes

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

### classm.retirement.3 — retirement[r2].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.3 — retirement[r2].ira_taxable — Taxable IRA amount: the part not rolled over (zero for a qualified Roth IRA dist
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r2].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $0.00

### classm.retirement.3 — retirement[r2].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: yes

### classm.retirement.3 — retirement[r2].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $26,836.00

### case classm.retirement.4 — prompt sha256 99f93b5beb65b0171c656f6839eaf641ce33dc6643a15ea1480f2277decefa1a; branches: retirement.special:false, retirement.annuity:true, retirement.is_ira:false, retirement.is_ira:true, retirement.roth:false, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.cost_left:false, retirement.annuity_with_cost:false, retirement.annuity_rollover:false, retirement.annuity_taxable#1, retirement.ira_taxable#1, retirement.ira_not_rolled:positive, retirement.plan_taxable#0, retirement.taxable#0, retirement.taxable#1, retirement.show_a:false, retirement.amount_a#1

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

### classm.retirement.4 — retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $4,478.00

### classm.retirement.4 — retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $44,438.00

### classm.retirement.4 — retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $-39,960.00

### classm.retirement.4 — retirement[r1].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r1].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r1].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r1].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $38,494.00

### classm.retirement.4 — retirement[r1].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $38,494.00

### classm.retirement.4 — retirement[r1].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $38,494.00

### classm.retirement.4 — retirement[r1].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r1].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $0.00

### classm.retirement.4 — retirement[r2].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: yes

### classm.retirement.4 — retirement[r2].roth — Roth IRA distribution
Status: **AGREE**

Value: no

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

### classm.retirement.4 — retirement[r2].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r2].ira_taxable — Taxable IRA amount: the part not rolled over (zero for a qualified Roth IRA dist
Status: **AGREE**

Value: $37,072.00

### classm.retirement.4 — retirement[r2].ira_not_rolled — Box 1 less the amount rolled over
Status: **AGREE**

Value: $37,072.00

### classm.retirement.4 — retirement[r2].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $37,072.00

### classm.retirement.4 — retirement[r2].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: no

### classm.retirement.4 — retirement[r2].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $0.00

### case classm.retirement.5 — prompt sha256 d1915360b7fe38d3a206a71afad99e2b575b98aae62ee7a024925cd92f115de7; branches: retirement.special:false, retirement.annuity:false, retirement.annuity:true, retirement.used_last_year:false, retirement.joint_life:true, retirement.is_ira:false, retirement.roth:false, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw4_table2#4, retirement.smw4_new#0, retirement.smw4#1, retirement.smw8:left, retirement.smw9:positive, retirement.cost_left:true, retirement.annuity_with_cost:false, retirement.annuity_with_cost:true, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.plan_simple:positive, retirement.plan_taxable#0, retirement.plan_taxable#1, retirement.taxable#1, retirement.show_a:false, retirement.show_a:true, retirement.amount_a#0, retirement.amount_a#1

### classm.retirement.5 — retirement[r1].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: no

### classm.retirement.5 — retirement[r1].roth — Roth IRA distribution
Status: **AGREE**

Value: no

### classm.retirement.5 — retirement[r1].direct — Direct rollover (code G)
Status: **AGREE**

Value: no

### classm.retirement.5 — retirement[r1].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.5 — retirement[r1].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.5 — retirement[r1].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: no

### classm.retirement.5 — retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $49,404.00

### classm.retirement.5 — retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $47,655.00

### classm.retirement.5 — retirement[r1].smw4_t2_210 — Line 2 divided by 210 (Table 2)
Status: **AGREE**

Value: $226.93

### classm.retirement.5 — retirement[r1].smw4_table2 — Line 2 divided by the Table 2 number for the combined ages at the annuity starti
Status: **AGREE**

Value: $226.93

### classm.retirement.5 — retirement[r1].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $226.93

### classm.retirement.5 — retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $226.93

### classm.retirement.5 — retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $2,723.16

### classm.retirement.5 — retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $6,742.00

### classm.retirement.5 — retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $40,913.00

### classm.retirement.5 — retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $2,723.16

### classm.retirement.5 — retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $46,680.84

### classm.retirement.5 — retirement[r1].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: yes

### classm.retirement.5 — retirement[r1].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: yes

### classm.retirement.5 — retirement[r1].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.5 — retirement[r1].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $46,680.84

### classm.retirement.5 — retirement[r1].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $46,680.84

### classm.retirement.5 — retirement[r1].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $46,680.84

### classm.retirement.5 — retirement[r1].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: yes

### classm.retirement.5 — retirement[r1].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $49,404.00

### classm.retirement.5 — retirement[r2].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: no

### classm.retirement.5 — retirement[r2].roth — Roth IRA distribution
Status: **AGREE**

Value: no

### classm.retirement.5 — retirement[r2].direct — Direct rollover (code G)
Status: **AGREE**

Value: no

### classm.retirement.5 — retirement[r2].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.5 — retirement[r2].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.5 — retirement[r2].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: no

### classm.retirement.5 — retirement[r2].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: no

### classm.retirement.5 — retirement[r2].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.5 — retirement[r2].plan_excluded — Taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.5 — retirement[r2].plan_simple — Box 1 less taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $37,436.00

### classm.retirement.5 — retirement[r2].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $37,436.00

### classm.retirement.5 — retirement[r2].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $37,436.00

### classm.retirement.5 — retirement[r2].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: no

### classm.retirement.5 — retirement[r2].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $0.00

### case classm.retirement.6 — prompt sha256 217f765da38318c12fccb2de4401da5193d59c018a49e1a02b625f6b879094e7; branches: retirement.special:false, retirement.annuity:true, retirement.used_last_year:false, retirement.joint_life:false, retirement.is_ira:false, retirement.roth:false, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw4_table1#2, retirement.smw4_table1#4, retirement.smw4_new#1, retirement.smw4#1, retirement.smw8:left, retirement.smw9:positive, retirement.cost_left:true, retirement.annuity_with_cost:true, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.plan_taxable#0, retirement.taxable#1, retirement.show_a:true, retirement.amount_a#0

### classm.retirement.6 — retirement[r1].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: no

### classm.retirement.6 — retirement[r1].roth — Roth IRA distribution
Status: **AGREE**

Value: no

### classm.retirement.6 — retirement[r1].direct — Direct rollover (code G)
Status: **AGREE**

Value: no

### classm.retirement.6 — retirement[r1].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.6 — retirement[r1].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.6 — retirement[r1].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: no

### classm.retirement.6 — retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $13,170.00

### classm.retirement.6 — retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $176,842.00

### classm.retirement.6 — retirement[r1].smw4_t1_260 — Line 2 divided by 260 (Table 1)
Status: **AGREE**

Value: $680.16

### classm.retirement.6 — retirement[r1].smw4_table1 — Line 2 divided by the Table 1 number for the age at the annuity starting date
Status: **AGREE**

Value: $680.16

### classm.retirement.6 — retirement[r1].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $680.16

### classm.retirement.6 — retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $680.16

### classm.retirement.6 — retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $8,161.92

### classm.retirement.6 — retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $0.00

### classm.retirement.6 — retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $176,842.00

### classm.retirement.6 — retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $8,161.92

### classm.retirement.6 — retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $5,008.08

### classm.retirement.6 — retirement[r1].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: yes

### classm.retirement.6 — retirement[r1].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: yes

### classm.retirement.6 — retirement[r1].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.6 — retirement[r1].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $5,008.08

### classm.retirement.6 — retirement[r1].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $5,008.08

### classm.retirement.6 — retirement[r1].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $5,008.08

### classm.retirement.6 — retirement[r1].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: yes

### classm.retirement.6 — retirement[r1].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $13,170.00

### classm.retirement.6 — retirement[r2].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: no

### classm.retirement.6 — retirement[r2].roth — Roth IRA distribution
Status: **AGREE**

Value: no

### classm.retirement.6 — retirement[r2].direct — Direct rollover (code G)
Status: **AGREE**

Value: no

### classm.retirement.6 — retirement[r2].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.6 — retirement[r2].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.6 — retirement[r2].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: no

### classm.retirement.6 — retirement[r2].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $49,743.00

### classm.retirement.6 — retirement[r2].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $79,404.00

### classm.retirement.6 — retirement[r2].smw4_t1_160 — Line 2 divided by 160 (Table 1)
Status: **AGREE**

Value: $496.28

### classm.retirement.6 — retirement[r2].smw4_table1 — Line 2 divided by the Table 1 number for the age at the annuity starting date
Status: **AGREE**

Value: $496.28

### classm.retirement.6 — retirement[r2].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $496.28

### classm.retirement.6 — retirement[r2].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $496.28

### classm.retirement.6 — retirement[r2].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $3,970.24

### classm.retirement.6 — retirement[r2].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $41,333.00

### classm.retirement.6 — retirement[r2].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $38,071.00

### classm.retirement.6 — retirement[r2].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $3,970.24

### classm.retirement.6 — retirement[r2].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $45,772.76

### classm.retirement.6 — retirement[r2].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: yes

### classm.retirement.6 — retirement[r2].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: yes

### classm.retirement.6 — retirement[r2].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.6 — retirement[r2].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $45,772.76

### classm.retirement.6 — retirement[r2].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $45,772.76

### classm.retirement.6 — retirement[r2].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $45,772.76

### classm.retirement.6 — retirement[r2].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: yes

### classm.retirement.6 — retirement[r2].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $49,743.00

### case classm.retirement.7 — prompt sha256 e51badd2a23cc9296b69e6789d1148825576d8b65ae7aedea60f4b619675aab5; branches: retirement.special:false, retirement.annuity:true, retirement.used_last_year:false, retirement.joint_life:true, retirement.is_ira:false, retirement.roth:false, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw4_table2#0, retirement.smw4_new#0, retirement.smw4#1, retirement.smw8:left, retirement.smw9:positive, retirement.cost_left:true, retirement.annuity_with_cost:true, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.plan_taxable#0, retirement.taxable#1, retirement.show_a:true, retirement.amount_a#0

### classm.retirement.7 — retirement[r1].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: no

### classm.retirement.7 — retirement[r1].roth — Roth IRA distribution
Status: **AGREE**

Value: no

### classm.retirement.7 — retirement[r1].direct — Direct rollover (code G)
Status: **AGREE**

Value: no

### classm.retirement.7 — retirement[r1].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.7 — retirement[r1].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.7 — retirement[r1].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: no

### classm.retirement.7 — retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $48,674.00

### classm.retirement.7 — retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $35,297.00

### classm.retirement.7 — retirement[r1].smw4_t2_410 — Line 2 divided by 410 (Table 2)
Status: **AGREE**

Value: $86.09

### classm.retirement.7 — retirement[r1].smw4_table2 — Line 2 divided by the Table 2 number for the combined ages at the annuity starti
Status: **AGREE**

Value: $86.09

### classm.retirement.7 — retirement[r1].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $86.09

### classm.retirement.7 — retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $86.09

### classm.retirement.7 — retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $258.27

### classm.retirement.7 — retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $0.00

### classm.retirement.7 — retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $35,297.00

### classm.retirement.7 — retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $258.27

### classm.retirement.7 — retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $48,415.73

### classm.retirement.7 — retirement[r1].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: yes

### classm.retirement.7 — retirement[r1].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: yes

### classm.retirement.7 — retirement[r1].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.7 — retirement[r1].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $48,415.73

### classm.retirement.7 — retirement[r1].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $48,415.73

### classm.retirement.7 — retirement[r1].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $48,415.73

### classm.retirement.7 — retirement[r1].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: yes

### classm.retirement.7 — retirement[r1].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $48,674.00

### case classm.retirement.8 — prompt sha256 1daffb5ceab4ba198030807e625d584a9d5af8b9e088736ad821a863b39e0ecd; branches: retirement.special:false, retirement.annuity:true, retirement.used_last_year:false, retirement.joint_life:true, retirement.is_ira:false, retirement.roth:false, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw4_table2#3, retirement.smw4_new#0, retirement.smw4#1, retirement.smw8:left, retirement.smw9:positive, retirement.cost_left:true, retirement.annuity_with_cost:true, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.plan_taxable#0, retirement.taxable#1, retirement.show_a:true, retirement.amount_a#0

### classm.retirement.8 — retirement[r1].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: no

### classm.retirement.8 — retirement[r1].roth — Roth IRA distribution
Status: **AGREE**

Value: no

### classm.retirement.8 — retirement[r1].direct — Direct rollover (code G)
Status: **AGREE**

Value: no

### classm.retirement.8 — retirement[r1].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.8 — retirement[r1].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.8 — retirement[r1].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: no

### classm.retirement.8 — retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $58,261.00

### classm.retirement.8 — retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $61,912.00

### classm.retirement.8 — retirement[r1].smw4_t2_260 — Line 2 divided by 260 (Table 2)
Status: **AGREE**

Value: $238.12

### classm.retirement.8 — retirement[r1].smw4_table2 — Line 2 divided by the Table 2 number for the combined ages at the annuity starti
Status: **AGREE**

Value: $238.12

### classm.retirement.8 — retirement[r1].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $238.12

### classm.retirement.8 — retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $238.12

### classm.retirement.8 — retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $2,857.44

### classm.retirement.8 — retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $35,118.00

### classm.retirement.8 — retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $26,794.00

### classm.retirement.8 — retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $2,857.44

### classm.retirement.8 — retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $55,403.56

### classm.retirement.8 — retirement[r1].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: yes

### classm.retirement.8 — retirement[r1].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: yes

### classm.retirement.8 — retirement[r1].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.8 — retirement[r1].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $55,403.56

### classm.retirement.8 — retirement[r1].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $55,403.56

### classm.retirement.8 — retirement[r1].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $55,403.56

### classm.retirement.8 — retirement[r1].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: yes

### classm.retirement.8 — retirement[r1].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $58,261.00

### case classm.retirement.9 — prompt sha256 3612ff7eb3888dccb1eec50477102ae398b8ea252aef08f0b297f1321e7c8566; branches: retirement.special:false, retirement.annuity:false, retirement.annuity:true, retirement.used_last_year:false, retirement.joint_life:false, retirement.is_ira:false, retirement.roth:false, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw4_table1#1, retirement.smw4_new#1, retirement.smw4#1, retirement.smw8:left, retirement.smw9:floor, retirement.cost_left:true, retirement.annuity_with_cost:false, retirement.annuity_with_cost:true, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.plan_simple:floor, retirement.plan_taxable#0, retirement.plan_taxable#1, retirement.taxable#1, retirement.show_a:true, retirement.amount_a#0

### classm.retirement.9 — retirement[r1].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: no

### classm.retirement.9 — retirement[r1].roth — Roth IRA distribution
Status: **AGREE**

Value: no

### classm.retirement.9 — retirement[r1].direct — Direct rollover (code G)
Status: **AGREE**

Value: no

### classm.retirement.9 — retirement[r1].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.9 — retirement[r1].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.9 — retirement[r1].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: no

### classm.retirement.9 — retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $1,536.00

### classm.retirement.9 — retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $74,075.00

### classm.retirement.9 — retirement[r1].smw4_t1_310 — Line 2 divided by 310 (Table 1)
Status: **AGREE**

Value: $238.95

### classm.retirement.9 — retirement[r1].smw4_table1 — Line 2 divided by the Table 1 number for the age at the annuity starting date
Status: **AGREE**

Value: $238.95

### classm.retirement.9 — retirement[r1].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $238.95

### classm.retirement.9 — retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $238.95

### classm.retirement.9 — retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $2,867.40

### classm.retirement.9 — retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $0.00

### classm.retirement.9 — retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $74,075.00

### classm.retirement.9 — retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $2,867.40

### classm.retirement.9 — retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $0.00

### classm.retirement.9 — retirement[r1].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: yes

### classm.retirement.9 — retirement[r1].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: yes

### classm.retirement.9 — retirement[r1].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.9 — retirement[r1].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $0.00

### classm.retirement.9 — retirement[r1].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $0.00

### classm.retirement.9 — retirement[r1].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $0.00

### classm.retirement.9 — retirement[r1].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: yes

### classm.retirement.9 — retirement[r1].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $1,536.00

### classm.retirement.9 — retirement[r2].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: no

### classm.retirement.9 — retirement[r2].roth — Roth IRA distribution
Status: **AGREE**

Value: no

### classm.retirement.9 — retirement[r2].direct — Direct rollover (code G)
Status: **AGREE**

Value: no

### classm.retirement.9 — retirement[r2].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.9 — retirement[r2].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.9 — retirement[r2].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: no

### classm.retirement.9 — retirement[r2].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: no

### classm.retirement.9 — retirement[r2].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.9 — retirement[r2].plan_excluded — Taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $1,652.00

### classm.retirement.9 — retirement[r2].plan_simple — Box 1 less taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.9 — retirement[r2].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $0.00

### classm.retirement.9 — retirement[r2].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $0.00

### classm.retirement.9 — retirement[r2].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **DISAGREE**

Project: yes
Model: no
Work: Taxable (0) equals box 1 (0), so it is treated as fully taxable and nothing goes on line 5a

Ruling: representation; project retained; model value dropped from the fixture. Box 1 is $0, so line 5a is $0 whether or not the entry is shown; the project shows it because box 5 is nonzero on a plan distribution outside the Simplified Method. [dropped]

### classm.retirement.9 — retirement[r2].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $0.00

### case classm.retirement.10 — prompt sha256 cdee278ea546a9bb5b41169be6c846aeb4273bc92f3e67cc2f25ba2a01adb035; branches: retirement.special:false, retirement.annuity:false, retirement.annuity:true, retirement.used_last_year:true, retirement.is_ira:false, retirement.roth:false, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw4#0, retirement.smw8:right, retirement.smw9:positive, retirement.cost_left:true, retirement.annuity_with_cost:false, retirement.annuity_with_cost:true, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.plan_simple:positive, retirement.plan_taxable#0, retirement.plan_taxable#1, retirement.taxable#1, retirement.show_a:false, retirement.show_a:true, retirement.amount_a#0, retirement.amount_a#1

### classm.retirement.10 — retirement[r1].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: no

### classm.retirement.10 — retirement[r1].roth — Roth IRA distribution
Status: **AGREE**

Value: no

### classm.retirement.10 — retirement[r1].direct — Direct rollover (code G)
Status: **AGREE**

Value: no

### classm.retirement.10 — retirement[r1].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.10 — retirement[r1].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.10 — retirement[r1].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: no

### classm.retirement.10 — retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $40,461.00

### classm.retirement.10 — retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $20,797.00

### classm.retirement.10 — retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $1,676.00

### classm.retirement.10 — retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $20,112.00

### classm.retirement.10 — retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $18,271.00

### classm.retirement.10 — retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $2,526.00

### classm.retirement.10 — retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $2,526.00

### classm.retirement.10 — retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $37,935.00

### classm.retirement.10 — retirement[r1].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: yes

### classm.retirement.10 — retirement[r1].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: yes

### classm.retirement.10 — retirement[r1].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.10 — retirement[r1].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $37,935.00

### classm.retirement.10 — retirement[r1].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $37,935.00

### classm.retirement.10 — retirement[r1].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $37,935.00

### classm.retirement.10 — retirement[r1].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: yes

### classm.retirement.10 — retirement[r1].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $40,461.00

### classm.retirement.10 — retirement[r2].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: no

### classm.retirement.10 — retirement[r2].roth — Roth IRA distribution
Status: **AGREE**

Value: no

### classm.retirement.10 — retirement[r2].direct — Direct rollover (code G)
Status: **AGREE**

Value: no

### classm.retirement.10 — retirement[r2].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.10 — retirement[r2].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.10 — retirement[r2].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: no

### classm.retirement.10 — retirement[r2].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: no

### classm.retirement.10 — retirement[r2].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.10 — retirement[r2].plan_excluded — Taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $0.00

### classm.retirement.10 — retirement[r2].plan_simple — Box 1 less taxable contributions (box 5) and the amount rolled over
Status: **AGREE**

Value: $34,097.00

### classm.retirement.10 — retirement[r2].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $34,097.00

### classm.retirement.10 — retirement[r2].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $34,097.00

### classm.retirement.10 — retirement[r2].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: no

### classm.retirement.10 — retirement[r2].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $0.00

### case classm.retirement.11 — prompt sha256 52074782755964c701c6dde029348b57f5d5ef67f11998af78dc93bf9a622928; branches: retirement.special:false, retirement.annuity:true, retirement.used_last_year:false, retirement.joint_life:false, retirement.is_ira:false, retirement.roth:false, retirement.direct:false, retirement.bad_code:false, retirement.rolled#1, retirement.has_rollover:false, retirement.smw4_table1#0, retirement.smw4_new#1, retirement.smw4#1, retirement.smw8:left, retirement.smw9:floor, retirement.cost_left:true, retirement.annuity_with_cost:true, retirement.annuity_rollover:false, retirement.annuity_taxable#0, retirement.plan_taxable#0, retirement.taxable#1, retirement.show_a:true, retirement.amount_a#0

### classm.retirement.11 — retirement[r1].is_ira — IRA distribution (lines 4a and 4b)
Status: **AGREE**

Value: no

### classm.retirement.11 — retirement[r1].roth — Roth IRA distribution
Status: **AGREE**

Value: no

### classm.retirement.11 — retirement[r1].direct — Direct rollover (code G)
Status: **AGREE**

Value: no

### classm.retirement.11 — retirement[r1].bad_code — Distribution code the tool does not compute
Status: **AGREE**

Value: no

### classm.retirement.11 — retirement[r1].rolled — Amount rolled over (the whole distribution for a direct rollover)
Status: **AGREE**

Value: $0.00

### classm.retirement.11 — retirement[r1].has_rollover — Part or all of the distribution was rolled over (an amount rolled over, or a dir
Status: **AGREE**

Value: no

### classm.retirement.11 — retirement[r1].smw1 — Enter the total pension or annuity payments from Form 1099-R, box 1
Status: **AGREE**

Value: $0.00

### classm.retirement.11 — retirement[r1].smw2 — Enter your cost in the plan at the annuity starting date
Status: **AGREE**

Value: $49,049.00

### classm.retirement.11 — retirement[r1].smw4_t1_360 — Line 2 divided by 360 (Table 1)
Status: **AGREE**

Value: $136.25

### classm.retirement.11 — retirement[r1].smw4_table1 — Line 2 divided by the Table 1 number for the age at the annuity starting date
Status: **AGREE**

Value: $136.25

### classm.retirement.11 — retirement[r1].smw4_new — Line 2 divided by the number on line 3 (Table 2 for a joint and survivor annuity
Status: **AGREE**

Value: $136.25

### classm.retirement.11 — retirement[r1].smw4 — Divide line 2 by the number on line 3 (or, if you completed this worksheet last 
Status: **AGREE**

Value: $136.25

### classm.retirement.11 — retirement[r1].smw5 — Multiply line 4 by the number of months for which this year's payments were made
Status: **AGREE**

Value: $1,635.00

### classm.retirement.11 — retirement[r1].smw6 — Enter the amount, if any, recovered tax free in years after 1986
Status: **AGREE**

Value: $5,243.00

### classm.retirement.11 — retirement[r1].smw7 — Subtract line 6 from line 2
Status: **AGREE**

Value: $43,806.00

### classm.retirement.11 — retirement[r1].smw8 — Enter the smaller of line 5 or line 7
Status: **AGREE**

Value: $1,635.00

### classm.retirement.11 — retirement[r1].smw9 — Taxable amount. Subtract line 8 from line 1. Enter the result, but not less than
Status: **AGREE**

Value: $0.00

### classm.retirement.11 — retirement[r1].cost_left — Some cost is left to recover (line 7 of the Simplified Method Worksheet is more 
Status: **AGREE**

Value: yes

### classm.retirement.11 — retirement[r1].annuity_with_cost — The Simplified Method applies and some cost is left to recover
Status: **AGREE**

Value: yes

### classm.retirement.11 — retirement[r1].annuity_rollover — A pension or annuity figured by the Simplified Method of which some amount was r
Status: **AGREE**

Value: no

### classm.retirement.11 — retirement[r1].annuity_taxable — Taxable annuity amount: Simplified Method line 9, or the whole of box 1 once the
Status: **AGREE**

Value: $0.00

### classm.retirement.11 — retirement[r1].plan_taxable — Taxable pension or annuity amount (the Simplified Method for an annuity with aft
Status: **AGREE**

Value: $0.00

### classm.retirement.11 — retirement[r1].taxable — Taxable amount of this distribution (line 4b or 5b)
Status: **AGREE**

Value: $0.00

### classm.retirement.11 — retirement[r1].show_a — An exception applies, so the total distribution goes on line 4a or 5a
Status: **AGREE**

Value: yes

### classm.retirement.11 — retirement[r1].amount_a — Total distribution entered on line 4a or 5a (none when fully taxable)
Status: **AGREE**

Value: $0.00

## Raw responses

### classm.retirement.1

```yaml
```yaml
lines:
  - printed: "retirement[r1].is_ira"
    value: "yes"
    work: "Account is a traditional IRA, so it is reported on lines 4a/4b"
  - printed: "retirement[r1].roth"
    value: "no"
    work: "Traditional IRA, not a Roth IRA"
  - printed: "retirement[r1].direct"
    value: "no"
    work: "Box 7 code is 7, not G"
  - printed: "retirement[r1].bad_code"
    value: "no"
    work: "Code 7 (normal distribution) is handled"
  - printed: "retirement[r1].rolled"
    value: "0.00"
    work: "No amount rolled over and not a direct rollover"
  - printed: "retirement[r1].has_rollover"
    value: "no"
    work: "Rolled over $0 and code is not G"
  - printed: "retirement[r1].annuity_rollover"
    value: "no"
    work: "IRA, not a Simplified Method annuity"
  - printed: "retirement[r1].ira_taxable"
    value: "0.00"
    work: "Box 1 $0.00 - rollover $0.00 = $0.00"
  - printed: "retirement[r1].ira_not_rolled"
    value: "0.00"
    work: "$0.00 - $0.00 = $0.00"
  - printed: "retirement[r1].taxable"
    value: "0.00"
    work: "Fully taxable amount of $0.00 goes on line 4b"
  - printed: "retirement[r1].show_a"
    value: "no"
    work: "No exception applies, so line 4a is left blank"
  - printed: "retirement[r1].amount_a"
    value: "0.00"
    work: "Fully taxable, so no line 4a entry"
  - printed: "retirement[r2].is_ira"
    value: "no"
    work: "Distribution is from a plan, so it goes on lines 5a/5b"
  - printed: "retirement[r2].roth"
    value: "no"
    work: "Not a Roth IRA"
  - printed: "retirement[r2].direct"
    value: "no"
    work: "Box 7 code is 7, not G"
  - printed: "retirement[r2].bad_code"
    value: "no"
    work: "Code 7 is handled"
  - printed: "retirement[r2].rolled"
    value: "0.00"
    work: "No amount rolled over"
  - printed: "retirement[r2].has_rollover"
    value: "no"
    work: "Rolled over $0 and code is not G"
  - printed: "retirement[r2].smw1"
    value: "46647.00"
    work: "Form 1099-R box 1"
  - printed: "retirement[r2].smw2"
    value: "122313.00"
    work: "Cost in the plan at the annuity starting date"
  - printed: "retirement[r2].smw4_t2_310"
    value: "394.56"
    work: "$122,313 / 310 = $394.56"
  - printed: "retirement[r2].smw4_table2"
    value: "394.56"
    work: "Combined ages 125 fall in 121-130, so Table 2 gives 310; $122,313 / 310"
  - printed: "retirement[r2].smw4_new"
    value: "394.56"
    work: "Joint/survivor annuity starting after 1997, so Table 2 applies"
  - printed: "retirement[r2].smw4"
    value: "394.56"
    work: "Worksheet not completed last year, so line 4 = line 2 / line 3"
  - printed: "retirement[r2].smw5"
    value: "4734.72"
    work: "$394.56 x 12 months"
  - printed: "retirement[r2].smw6"
    value: "47260.00"
    work: "Amount recovered tax free after 1986"
  - printed: "retirement[r2].smw7"
    value: "75053.00"
    work: "$122,313 - $47,260"
  - printed: "retirement[r2].smw8"
    value: "4734.72"
    work: "Smaller of $4,734.72 and $75,053.00"
  - printed: "retirement[r2].smw9"
    value: "41912.28"
    work: "$46,647.00 - $4,734.72"
  - printed: "retirement[r2].cost_left"
    value: "yes"
    work: "Line 7 is $75,053, which is more than 0"
  - printed: "retirement[r2].annuity_with_cost"
    value: "yes"
    work: "Simplified Method applies and cost remains"
  - printed: "retirement[r2].annuity_rollover"
    value: "no"
    work: "No amount rolled over"
  - printed: "retirement[r2].annuity_taxable"
    value: "41912.28"
    work: "Simplified Method Worksheet line 9"
  - printed: "retirement[r2].plan_taxable"
    value: "41912.28"
    work: "Simplified Method result"
  - printed: "retirement[r2].taxable"
    value: "41912.28"
    work: "Line 5b"
  - printed: "retirement[r2].show_a"
    value: "yes"
    work: "Partially taxable annuity, so the total goes on line 5a"
  - printed: "retirement[r2].amount_a"
    value: "46647.00"
    work: "Box 1 total goes on line 5a"
```
```

### classm.retirement.2

```yaml
```yaml
lines:
  - printed: "retirement[r1].is_ira"
    value: "no"
    work: "The account kind is a plan, not an IRA, so it goes on lines 5a/5b."
  - printed: "retirement[r1].roth"
    value: "no"
    work: "The account kind is a plan, not a Roth IRA."
  - printed: "retirement[r1].direct"
    value: "no"
    work: "Box 7 code is 2, not G."
  - printed: "retirement[r1].bad_code"
    value: "no"
    work: "Code 2 (early distribution, exception applies) is computed normally."
  - printed: "retirement[r1].rolled"
    value: "0.00"
    work: "Amount rolled over is $0.00 and this is not a direct rollover."
  - printed: "retirement[r1].has_rollover"
    value: "no"
    work: "Nothing was rolled over and the code is not G."
  - printed: "retirement[r1].smw1"
    value: "0.00"
    work: "SMW line 1 = box 1 = 0.00."
  - printed: "retirement[r1].smw2"
    value: "98901.00"
    work: "SMW line 2 = cost in the plan at the annuity starting date."
  - printed: "retirement[r1].smw4"
    value: "1165.00"
    work: "Worksheet completed last year, so skip line 3 and use last year's line 4 = 1,165.00."
  - printed: "retirement[r1].smw5"
    value: "13980.00"
    work: "1,165.00 x 12 months = 13,980.00."
  - printed: "retirement[r1].smw6"
    value: "25500.00"
    work: "Line 10 of last year's worksheet = 25,500.00."
  - printed: "retirement[r1].smw7"
    value: "73401.00"
    work: "98,901.00 - 25,500.00 = 73,401.00."
  - printed: "retirement[r1].smw8"
    value: "13980.00"
    work: "Smaller of 13,980.00 and 73,401.00."
  - printed: "retirement[r1].smw9"
    value: "0.00"
    work: "0.00 - 13,980.00 is less than zero, so enter 0."
  - printed: "retirement[r1].cost_left"
    value: "yes"
    work: "Line 7 = 73,401.00, which is more than 0."
  - printed: "retirement[r1].annuity_with_cost"
    value: "yes"
    work: "The Simplified Method applies and line 7 is more than 0."
  - printed: "retirement[r1].annuity_rollover"
    value: "no"
    work: "No amount was rolled over."
  - printed: "retirement[r1].annuity_taxable"
    value: "0.00"
    work: "Cost remains, so use SMW line 9 = 0.00."
  - printed: "retirement[r1].plan_taxable"
    value: "0.00"
    work: "Simplified Method taxable amount = 0.00."
  - printed: "retirement[r1].taxable"
    value: "0.00"
    work: "Line 5b = 0.00."
  - printed: "retirement[r1].show_a"
    value: "yes"
    work: "Partially taxable annuity: the total payments go on line 5a (SMW line 1)."
  - printed: "retirement[r1].amount_a"
    value: "0.00"
    work: "Line 5a = box 1 = 0.00."
  - printed: "retirement[r2].is_ira"
    value: "no"
    work: "The account kind is a plan, so it goes on lines 5a/5b."
  - printed: "retirement[r2].direct"
    value: "yes"
    work: "Box 7 code is G."
  - printed: "retirement[r2].bad_code"
    value: "no"
    work: "Code G is handled under Rollovers."
  - printed: "retirement[r2].rolled"
    value: "11322.00"
    work: "Direct rollover, so the whole distribution of 11,322.00 counts as rolled over."
  - printed: "retirement[r2].has_rollover"
    value: "yes"
    work: "Direct rollover, code G."
  - printed: "retirement[r2].annuity_rollover"
    value: "no"
    work: "The Simplified Method does not apply."
  - printed: "retirement[r2].plan_excluded"
    value: "11322.00"
    work: "Box 5 0.00 + rollover 11,322.00 = 11,322.00."
  - printed: "retirement[r2].plan_simple"
    value: "0.00"
    work: "11,322.00 - 0.00 - 11,322.00 = 0.00."
  - printed: "retirement[r2].plan_taxable"
    value: "0.00"
    work: "Per Rollovers, the remaining amount is 0, so enter -0- on line 5b."
  - printed: "retirement[r2].taxable"
    value: "0.00"
    work: "Line 5b = 0.00."
  - printed: "retirement[r2].show_a"
    value: "yes"
    work: "Rollover: box 1 goes on line 5a."
  - printed: "retirement[r2].amount_a"
    value: "11322.00"
    work: "Line 5a = box 1 = 11,322.00."
```
```

### classm.retirement.3

```yaml
```yaml
lines:
  - printed: "retirement[r1].is_ira"
    value: "no"
    work: "Account kind is plan, not IRA; report on lines 5a/5b"
  - printed: "retirement[r1].roth"
    value: "no"
    work: "Account kind is plan, not Roth IRA"
  - printed: "retirement[r1].direct"
    value: "no"
    work: "Box 7 code is 4 (death), not G"
  - printed: "retirement[r1].bad_code"
    value: "no"
    work: "Code 4 (death) is handled as an ordinary pension/annuity distribution"
  - printed: "retirement[r1].rolled"
    value: "0.00"
    work: "Amount rolled over within 60 days = $0; not a direct rollover"
  - printed: "retirement[r1].has_rollover"
    value: "no"
    work: "Rolled amount is 0 and the code is not G"
  - printed: "retirement[r1].smw1"
    value: "18476.00"
    work: "Form 1099-R, box 1"
  - printed: "retirement[r1].smw2"
    value: "143786.00"
    work: "Cost in plan at annuity starting date"
  - printed: "retirement[r1].smw4_t1_210"
    value: "684.70"
    work: "143,786 / 210 = 684.695 -> 684.70"
  - printed: "retirement[r1].smw4_table1"
    value: "684.70"
    work: "Age 68 is in 66-70; start date after 11/18/1996, so Table 1 = 210; 143,786 / 210"
  - printed: "retirement[r1].smw4_new"
    value: "684.70"
    work: "Not a joint and survivor annuity, so Table 1 (210) applies; 143,786 / 210"
  - printed: "retirement[r1].smw4"
    value: "684.70"
    work: "Worksheet not completed last year, so line 2 / line 3 = 143,786 / 210"
  - printed: "retirement[r1].smw5"
    value: "3423.50"
    work: "684.70 x 5 months"
  - printed: "retirement[r1].smw6"
    value: "45880.00"
    work: "Amount recovered tax free after 1986"
  - printed: "retirement[r1].smw7"
    value: "97906.00"
    work: "143,786 - 45,880"
  - printed: "retirement[r1].smw8"
    value: "3423.50"
    work: "Smaller of 3,423.50 or 97,906"
  - printed: "retirement[r1].smw9"
    value: "15052.50"
    work: "18,476 - 3,423.50; not less than zero"
  - printed: "retirement[r1].cost_left"
    value: "yes"
    work: "Line 7 of 97,906 is more than zero"
  - printed: "retirement[r1].annuity_with_cost"
    value: "yes"
    work: "Simplified Method applies and cost remains to recover"
  - printed: "retirement[r1].annuity_rollover"
    value: "no"
    work: "No amount was rolled over"
  - printed: "retirement[r1].annuity_taxable"
    value: "15052.50"
    work: "Simplified Method Worksheet line 9"
  - printed: "retirement[r1].plan_taxable"
    value: "15052.50"
    work: "Simplified Method taxable amount"
  - printed: "retirement[r1].taxable"
    value: "15052.50"
    work: "Line 5b"
  - printed: "retirement[r1].show_a"
    value: "yes"
    work: "Partially taxable annuity: box 1 total goes on line 5a (worksheet line 1)"
  - printed: "retirement[r1].amount_a"
    value: "18476.00"
    work: "Box 1 total on line 5a"
  - printed: "retirement[r2].is_ira"
    value: "yes"
    work: "A Roth IRA is an IRA; report on lines 4a/4b"
  - printed: "retirement[r2].roth"
    value: "yes"
    work: "Account kind is roth_ira"
  - printed: "retirement[r2].direct"
    value: "no"
    work: "Box 7 code is Q, not G"
  - printed: "retirement[r2].bad_code"
    value: "no"
    work: "Code Q (qualified Roth distribution) is handled under Exception 2(b)"
  - printed: "retirement[r2].rolled"
    value: "0.00"
    work: "Amount rolled over = $0"
  - printed: "retirement[r2].has_rollover"
    value: "no"
    work: "Rolled amount is 0 and the code is not G"
  - printed: "retirement[r2].annuity_rollover"
    value: "no"
    work: "Not a Simplified Method annuity"
  - printed: "retirement[r2].ira_taxable"
    value: "0.00"
    work: "Exception 2(b): code Q, so enter -0- on line 4b"
  - printed: "retirement[r2].taxable"
    value: "0.00"
    work: "Line 4b = -0- for code Q"
  - printed: "retirement[r2].show_a"
    value: "yes"
    work: "Exception 2 (Roth IRA distribution): total distribution goes on line 4a"
  - printed: "retirement[r2].amount_a"
    value: "26836.00"
    work: "Box 1 total on line 4a"
```
```

### classm.retirement.4

```yaml
```yaml
lines:
  - printed: "retirement[r1].is_ira"
    value: "no"
    work: "Account kind is plan, not an IRA, so it goes on lines 5a/5b"
  - printed: "retirement[r1].roth"
    value: "no"
    work: "Not a Roth IRA"
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
  - printed: "retirement[r1].smw2"
    value: "4478.00"
    work: "SMW line 2: cost in the plan at the annuity starting date"
  - printed: "retirement[r1].smw6"
    value: "44438.00"
    work: "SMW line 6: line 10 of last year's worksheet"
  - printed: "retirement[r1].smw7"
    value: "-39960.00"
    work: "SMW line 7: 4,478.00 - 44,438.00"
  - printed: "retirement[r1].cost_left"
    value: "no"
    work: "Line 7 is not more than zero"
  - printed: "retirement[r1].annuity_with_cost"
    value: "no"
    work: "The Simplified Method applies, but no cost is left to recover"
  - printed: "retirement[r1].annuity_rollover"
    value: "no"
    work: "No cost is left and nothing was rolled over"
  - printed: "retirement[r1].annuity_taxable"
    value: "38494.00"
    work: "Cost is fully recovered, so the whole of box 1 is taxable"
  - printed: "retirement[r1].plan_taxable"
    value: "38494.00"
    work: "Equals the taxable annuity amount"
  - printed: "retirement[r1].taxable"
    value: "38494.00"
    work: "Line 5b: fully taxable; entire cost was recovered before 2025"
  - printed: "retirement[r1].show_a"
    value: "no"
    work: "Fully taxable, so no entry on line 5a"
  - printed: "retirement[r1].amount_a"
    value: "0.00"
    work: "Fully taxable, so no line 5a amount"
  - printed: "retirement[r2].is_ira"
    value: "yes"
    work: "Traditional IRA, so it goes on lines 4a/4b"
  - printed: "retirement[r2].roth"
    value: "no"
    work: "Traditional, not a Roth IRA"
  - printed: "retirement[r2].direct"
    value: "no"
    work: "Box 7 code is 7, not G"
  - printed: "retirement[r2].bad_code"
    value: "no"
    work: "Code 7 is handled"
  - printed: "retirement[r2].rolled"
    value: "0.00"
    work: "Amount rolled over is $0"
  - printed: "retirement[r2].has_rollover"
    value: "no"
    work: "Nothing was rolled over"
  - printed: "retirement[r2].annuity_rollover"
    value: "no"
    work: "IRA distribution, not a Simplified Method annuity"
  - printed: "retirement[r2].ira_taxable"
    value: "37072.00"
    work: "The part not rolled over: 37,072.00"
  - printed: "retirement[r2].ira_not_rolled"
    value: "37072.00"
    work: "37,072.00 - 0.00"
  - printed: "retirement[r2].taxable"
    value: "37072.00"
    work: "Line 4b: fully taxable IRA distribution"
  - printed: "retirement[r2].show_a"
    value: "no"
    work: "No exception applies; fully taxable, so no entry on line 4a"
  - printed: "retirement[r2].amount_a"
    value: "0.00"
    work: "Fully taxable, so no line 4a amount"
```
```

### classm.retirement.5

```yaml
```yaml
lines:
  - printed: "retirement[r1].is_ira"
    value: "no"
    work: "Kind of account = plan, so lines 5a/5b, not IRA"
  - printed: "retirement[r1].roth"
    value: "no"
    work: "Not a Roth IRA; account is a plan"
  - printed: "retirement[r1].direct"
    value: "no"
    work: "Box 7 code is 2, not G"
  - printed: "retirement[r1].bad_code"
    value: "no"
    work: "Code 2 (early distribution, exception applies) is handled; no special-case answer was yes"
  - printed: "retirement[r1].rolled"
    value: "0.00"
    work: "Amount rolled over = $0; not a direct rollover"
  - printed: "retirement[r1].has_rollover"
    value: "no"
    work: "Rolled = 0 and the code is not G"
  - printed: "retirement[r1].smw1"
    value: "49404.00"
    work: "SMW line 1 = box 1 amount"
  - printed: "retirement[r1].smw2"
    value: "47655.00"
    work: "SMW line 2 = cost at the annuity starting date"
  - printed: "retirement[r1].smw4_t2_210"
    value: "226.93"
    work: "47,655 / 210 = 226.93"
  - printed: "retirement[r1].smw4_table2"
    value: "226.93"
    work: "Combined ages 145 fall in the 141-or-older row of Table 2, so the divisor is 210; 47,655 / 210 = 226.93"
  - printed: "retirement[r1].smw4_new"
    value: "226.93"
    work: "Start date after 1997 and joint lives, so Table 2 applies: 226.93"
  - printed: "retirement[r1].smw4"
    value: "226.93"
    work: "Worksheet not completed last year, so line 4 = line 2 / line 3 = 226.93"
  - printed: "retirement[r1].smw5"
    value: "2723.16"
    work: "226.93 x 12 = 2,723.16"
  - printed: "retirement[r1].smw6"
    value: "6742.00"
    work: "Amount recovered tax free after 1986 = 6,742"
  - printed: "retirement[r1].smw7"
    value: "40913.00"
    work: "47,655 - 6,742 = 40,913"
  - printed: "retirement[r1].smw8"
    value: "2723.16"
    work: "Smaller of 2,723.16 or 40,913"
  - printed: "retirement[r1].smw9"
    value: "46680.84"
    work: "49,404 - 2,723.16 = 46,680.84"
  - printed: "retirement[r1].cost_left"
    value: "yes"
    work: "Line 7 = 40,913 > 0"
  - printed: "retirement[r1].annuity_with_cost"
    value: "yes"
    work: "Simplified Method applies and line 7 > 0"
  - printed: "retirement[r1].annuity_rollover"
    value: "no"
    work: "No amount rolled over"
  - printed: "retirement[r1].annuity_taxable"
    value: "46680.84"
    work: "SMW line 9"
  - printed: "retirement[r1].plan_taxable"
    value: "46680.84"
    work: "Simplified Method taxable amount"
  - printed: "retirement[r1].taxable"
    value: "46680.84"
    work: "Line 5b amount"
  - printed: "retirement[r1].show_a"
    value: "yes"
    work: "Partially taxable annuity; SMW line 1 says enter box 1 on line 5a"
  - printed: "retirement[r1].amount_a"
    value: "49404.00"
    work: "Total distribution on line 5a"
  - printed: "retirement[r2].is_ira"
    value: "no"
    work: "Kind of account = plan"
  - printed: "retirement[r2].roth"
    value: "no"
    work: "Not a Roth IRA"
  - printed: "retirement[r2].direct"
    value: "no"
    work: "Code 7, not G"
  - printed: "retirement[r2].bad_code"
    value: "no"
    work: "Code 7 (normal distribution) is handled; no special-case answer was yes"
  - printed: "retirement[r2].rolled"
    value: "0.00"
    work: "Amount rolled over = $0"
  - printed: "retirement[r2].has_rollover"
    value: "no"
    work: "No rollover and the code is not G"
  - printed: "retirement[r2].annuity_with_cost"
    value: "no"
    work: "Simplified Method does not apply"
  - printed: "retirement[r2].annuity_rollover"
    value: "no"
    work: "No Simplified Method and no rollover"
  - printed: "retirement[r2].plan_excluded"
    value: "0.00"
    work: "Box 5 of 0 + rollover of 0 = 0"
  - printed: "retirement[r2].plan_simple"
    value: "37436.00"
    work: "37,436 - 0 = 37,436"
  - printed: "retirement[r2].plan_taxable"
    value: "37436.00"
    work: "No after-tax cost, so fully taxable"
  - printed: "retirement[r2].taxable"
    value: "37436.00"
    work: "Line 5b amount"
  - printed: "retirement[r2].show_a"
    value: "no"
    work: "Fully taxable; enter on 5b only, no entry on 5a"
  - printed: "retirement[r2].amount_a"
    value: "0.00"
    work: "No line 5a entry when fully taxable"
```
```

### classm.retirement.6

```yaml
```yaml
lines:
  - printed: "retirement[r1].is_ira"
    value: "no"
    work: "Kind of account = plan, so lines 5a/5b, not an IRA"
  - printed: "retirement[r1].roth"
    value: "no"
    work: "Account is a plan, not a Roth IRA"
  - printed: "retirement[r1].direct"
    value: "no"
    work: "Box 7 code is 2, not G"
  - printed: "retirement[r1].bad_code"
    value: "no"
    work: "Code 2 (early, exception applies) is handled; filer answered no to the special situations"
  - printed: "retirement[r1].rolled"
    value: "0.00"
    work: "Amount rolled over within 60 days = $0; no direct rollover"
  - printed: "retirement[r1].has_rollover"
    value: "no"
    work: "Rolled = 0 and not code G"
  - printed: "retirement[r1].smw1"
    value: "13170.00"
    work: "SMW line 1 = Form 1099-R box 1"
  - printed: "retirement[r1].smw2"
    value: "176842.00"
    work: "SMW line 2 = cost in the plan at the annuity starting date"
  - printed: "retirement[r1].smw4_t1_260"
    value: "680.16"
    work: "176,842 / 260 = 680.16 (Table 1, age 61-65, start after 11/18/1996)"
  - printed: "retirement[r1].smw4_table1"
    value: "680.16"
    work: "Age 63 gives Table 1 number 260; 176,842 / 260 = 680.16"
  - printed: "retirement[r1].smw4_new"
    value: "680.16"
    work: "Not a joint and survivor annuity, so Table 1 is used: 680.16"
  - printed: "retirement[r1].smw4"
    value: "680.16"
    work: "No worksheet last year, so line 4 = 176,842 / 260 = 680.16"
  - printed: "retirement[r1].smw5"
    value: "8161.92"
    work: "680.16 x 12 months = 8,161.92"
  - printed: "retirement[r1].smw6"
    value: "0.00"
    work: "Amount recovered tax free after 1986 = $0"
  - printed: "retirement[r1].smw7"
    value: "176842.00"
    work: "176,842 - 0 = 176,842.00"
  - printed: "retirement[r1].smw8"
    value: "8161.92"
    work: "Smaller of 8,161.92 or 176,842.00"
  - printed: "retirement[r1].smw9"
    value: "5008.08"
    work: "13,170.00 - 8,161.92 = 5,008.08"
  - printed: "retirement[r1].cost_left"
    value: "yes"
    work: "Line 7 = 176,842 > 0"
  - printed: "retirement[r1].annuity_with_cost"
    value: "yes"
    work: "Simplified Method applies and line 7 > 0"
  - printed: "retirement[r1].annuity_rollover"
    value: "no"
    work: "No amount was rolled over"
  - printed: "retirement[r1].annuity_taxable"
    value: "5008.08"
    work: "Simplified Method line 9"
  - printed: "retirement[r1].plan_taxable"
    value: "5008.08"
    work: "Simplified Method taxable amount"
  - printed: "retirement[r1].taxable"
    value: "5008.08"
    work: "Line 5b amount = 5,008.08"
  - printed: "retirement[r1].show_a"
    value: "yes"
    work: "Partially taxable annuity, so the box 1 total goes on line 5a"
  - printed: "retirement[r1].amount_a"
    value: "13170.00"
    work: "Line 5a = box 1, 13,170.00"
  - printed: "retirement[r2].is_ira"
    value: "no"
    work: "Kind of account = plan, so lines 5a/5b, not an IRA"
  - printed: "retirement[r2].roth"
    value: "no"
    work: "Account is a plan, not a Roth IRA"
  - printed: "retirement[r2].direct"
    value: "no"
    work: "Box 7 code is 7, not G"
  - printed: "retirement[r2].bad_code"
    value: "no"
    work: "Code 7 (normal distribution) is handled; filer answered no to the special situations"
  - printed: "retirement[r2].rolled"
    value: "0.00"
    work: "Amount rolled over = $0; no direct rollover"
  - printed: "retirement[r2].has_rollover"
    value: "no"
    work: "Rolled = 0 and not code G"
  - printed: "retirement[r2].smw1"
    value: "49743.00"
    work: "SMW line 1 = Form 1099-R box 1"
  - printed: "retirement[r2].smw2"
    value: "79404.00"
    work: "SMW line 2 = cost in the plan at the annuity starting date"
  - printed: "retirement[r2].smw4_t1_160"
    value: "496.28"
    work: "79,404 / 160 = 496.275, rounded to 496.28 (Table 1, age 71 or older, start after 11/18/1996)"
  - printed: "retirement[r2].smw4_table1"
    value: "496.28"
    work: "Age 80 gives Table 1 number 160; 79,404 / 160 = 496.28"
  - printed: "retirement[r2].smw4_new"
    value: "496.28"
    work: "Not a joint and survivor annuity, so Table 1 is used: 496.28"
  - printed: "retirement[r2].smw4"
    value: "496.28"
    work: "No worksheet last year, so line 4 = 79,404 / 160 = 496.28"
  - printed: "retirement[r2].smw5"
    value: "3970.24"
    work: "496.28 x 8 months = 3,970.24"
  - printed: "retirement[r2].smw6"
    value: "41333.00"
    work: "Amount recovered tax free after 1986 = 41,333.00"
  - printed: "retirement[r2].smw7"
    value: "38071.00"
    work: "79,404 - 41,333 = 38,071.00"
  - printed: "retirement[r2].smw8"
    value: "3970.24"
    work: "Smaller of 3,970.24 or 38,071.00"
  - printed: "retirement[r2].smw9"
    value: "45772.76"
    work: "49,743.00 - 3,970.24 = 45,772.76"
  - printed: "retirement[r2].cost_left"
    value: "yes"
    work: "Line 7 = 38,071 > 0"
  - printed: "retirement[r2].annuity_with_cost"
    value: "yes"
    work: "Simplified Method applies and line 7 > 0"
  - printed: "retirement[r2].annuity_rollover"
    value: "no"
    work: "No amount was rolled over"
  - printed: "retirement[r2].annuity_taxable"
    value: "45772.76"
    work: "Simplified Method line 9"
  - printed: "retirement[r2].plan_taxable"
    value: "45772.76"
    work: "Simplified Method taxable amount"
  - printed: "retirement[r2].taxable"
    value: "45772.76"
    work: "Line 5b amount = 45,772.76"
  - printed: "retirement[r2].show_a"
    value: "yes"
    work: "Partially taxable annuity, so the box 1 total goes on line 5a"
  - printed: "retirement[r2].amount_a"
    value: "49743.00"
    work: "Line 5a = box 1, 49,743.00"
```
```

### classm.retirement.7

```yaml
```yaml
lines:
  - printed: "retirement[r1].is_ira"
    value: "no"
    work: "Kind of account = plan, so this goes on lines 5a/5b, not 4a/4b"
  - printed: "retirement[r1].roth"
    value: "no"
    work: "Plan distribution, not from a Roth IRA"
  - printed: "retirement[r1].direct"
    value: "no"
    work: "Box 7 code is 4 (death), not G"
  - printed: "retirement[r1].bad_code"
    value: "no"
    work: "Code 4 (death) is computed normally; filer answered no to every special situation"
  - printed: "retirement[r1].rolled"
    value: "0.00"
    work: "Amount rolled over is $0.00 and this is not a direct rollover"
  - printed: "retirement[r1].has_rollover"
    value: "no"
    work: "No amount rolled over and no code G"
  - printed: "retirement[r1].smw1"
    value: "48674.00"
    work: "Form 1099-R box 1"
  - printed: "retirement[r1].smw2"
    value: "35297.00"
    work: "Cost in the plan at the annuity starting date, as given"
  - printed: "retirement[r1].smw4_t2_410"
    value: "86.09"
    work: "35,297.00 / 410 = 86.09"
  - printed: "retirement[r1].smw4_table2"
    value: "86.09"
    work: "Combined ages 102 are 110 or under, so Table 2 gives 410; 35,297.00 / 410 = 86.09"
  - printed: "retirement[r1].smw4_new"
    value: "86.09"
    work: "Starting date after 1997, joint life, so Table 2 applies; 35,297.00 / 410 = 86.09"
  - printed: "retirement[r1].smw4"
    value: "86.09"
    work: "Worksheet not completed last year, so use line 2 / line 3 = 86.09"
  - printed: "retirement[r1].smw5"
    value: "258.27"
    work: "86.09 x 3 months = 258.27"
  - printed: "retirement[r1].smw6"
    value: "0.00"
    work: "Amount recovered tax free after 1986 is $0.00"
  - printed: "retirement[r1].smw7"
    value: "35297.00"
    work: "35,297.00 - 0.00 = 35,297.00"
  - printed: "retirement[r1].smw8"
    value: "258.27"
    work: "Smaller of 258.27 or 35,297.00 = 258.27"
  - printed: "retirement[r1].smw9"
    value: "48415.73"
    work: "48,674.00 - 258.27 = 48,415.73, which is not less than zero"
  - printed: "retirement[r1].cost_left"
    value: "yes"
    work: "Line 7 is 35,297.00, which is more than 0"
  - printed: "retirement[r1].annuity_with_cost"
    value: "yes"
    work: "The Simplified Method applies and line 7 is more than 0"
  - printed: "retirement[r1].annuity_rollover"
    value: "no"
    work: "No part of the distribution was rolled over"
  - printed: "retirement[r1].annuity_taxable"
    value: "48415.73"
    work: "Cost not yet recovered, so use Simplified Method line 9"
  - printed: "retirement[r1].plan_taxable"
    value: "48415.73"
    work: "Simplified Method result for an annuity with after-tax cost"
  - printed: "retirement[r1].taxable"
    value: "48415.73"
    work: "Line 5b amount"
  - printed: "retirement[r1].show_a"
    value: "yes"
    work: "Partially taxable annuity, so the total goes on line 5a"
  - printed: "retirement[r1].amount_a"
    value: "48674.00"
    work: "Box 1 total entered on line 5a (Simplified Method Worksheet line 1)"
```
```

### classm.retirement.8

```yaml
```yaml
lines:
  - printed: "retirement[r1].is_ira"
    value: "no"
    work: "Account kind is plan, not IRA; reported on lines 5a/5b"
  - printed: "retirement[r1].roth"
    value: "no"
    work: "Account kind is plan, not a Roth IRA"
  - printed: "retirement[r1].direct"
    value: "no"
    work: "Box 7 code is 4 (death), not G"
  - printed: "retirement[r1].bad_code"
    value: "no"
    work: "Code 4 (death) is not code 1, J or S and needs no special handling"
  - printed: "retirement[r1].rolled"
    value: "0.00"
    work: "Amount rolled over within 60 days = $0.00; not a direct rollover"
  - printed: "retirement[r1].has_rollover"
    value: "no"
    work: "No amount rolled over and no code G"
  - printed: "retirement[r1].smw1"
    value: "58261.00"
    work: "SMW line 1 = Form 1099-R box 1"
  - printed: "retirement[r1].smw2"
    value: "61912.00"
    work: "SMW line 2 = cost in plan at annuity starting date"
  - printed: "retirement[r1].smw4_t2_260"
    value: "238.12"
    work: "61,912 / 260 = 238.12"
  - printed: "retirement[r1].smw4_table2"
    value: "238.12"
    work: "Table 2, combined ages 137 (131-140) = 260; 61,912 / 260 = 238.12"
  - printed: "retirement[r1].smw4_new"
    value: "238.12"
    work: "Joint and survivor annuity starting after 1997 uses Table 2 (260); 61,912 / 260"
  - printed: "retirement[r1].smw4"
    value: "238.12"
    work: "Worksheet not completed last year, so line 4 = line 2 / line 3 = 238.12"
  - printed: "retirement[r1].smw5"
    value: "2857.44"
    work: "238.12 x 12 months = 2,857.44"
  - printed: "retirement[r1].smw6"
    value: "35118.00"
    work: "Amount recovered tax free after 1986, as supplied"
  - printed: "retirement[r1].smw7"
    value: "26794.00"
    work: "61,912 - 35,118 = 26,794"
  - printed: "retirement[r1].smw8"
    value: "2857.44"
    work: "Smaller of line 5 (2,857.44) or line 7 (26,794)"
  - printed: "retirement[r1].smw9"
    value: "55403.56"
    work: "58,261.00 - 2,857.44 = 55,403.56 (not less than zero)"
  - printed: "retirement[r1].cost_left"
    value: "yes"
    work: "Line 7 = 26,794 > 0"
  - printed: "retirement[r1].annuity_with_cost"
    value: "yes"
    work: "Simplified Method applies and line 7 > 0"
  - printed: "retirement[r1].annuity_rollover"
    value: "no"
    work: "No rollover"
  - printed: "retirement[r1].annuity_taxable"
    value: "55403.56"
    work: "Cost not yet recovered, so taxable amount = SMW line 9"
  - printed: "retirement[r1].plan_taxable"
    value: "55403.56"
    work: "Plan annuity with after-tax cost, figured by the Simplified Method"
  - printed: "retirement[r1].taxable"
    value: "55403.56"
    work: "Line 5b = SMW line 9"
  - printed: "retirement[r1].show_a"
    value: "yes"
    work: "Partially taxable annuity: total payments go on line 5a (SMW line 1)"
  - printed: "retirement[r1].amount_a"
    value: "58261.00"
    work: "Line 5a = box 1 total, 58,261.00"
```
```

### classm.retirement.9

```yaml
lines:
  - printed: "retirement[r1].is_ira"
    value: "no"
    work: "The account kind is a plan, not an IRA, so it goes on lines 5a/5b"
  - printed: "retirement[r1].roth"
    value: "no"
    work: "The account kind is a plan, not a Roth IRA"
  - printed: "retirement[r1].direct"
    value: "no"
    work: "Box 7 code is 7, not G"
  - printed: "retirement[r1].bad_code"
    value: "no"
    work: "Code 7 (normal distribution) can be computed; no exception was flagged"
  - printed: "retirement[r1].rolled"
    value: "0.00"
    work: "Amount rolled over is $0.00 and this is not a direct rollover"
  - printed: "retirement[r1].has_rollover"
    value: "no"
    work: "Nothing was rolled over and the code is not G"
  - printed: "retirement[r1].smw1"
    value: "1536.00"
    work: "SMW line 1 = box 1 = 1,536.00"
  - printed: "retirement[r1].smw2"
    value: "74075.00"
    work: "SMW line 2 = cost in the plan at the annuity starting date"
  - printed: "retirement[r1].smw4_t1_310"
    value: "238.95"
    work: "74,075 / 310 = 238.95"
  - printed: "retirement[r1].smw4_table1"
    value: "238.95"
    work: "Table 1: age 56-60 with a start after Nov 18, 1996 gives 310; 74,075 / 310 = 238.95"
  - printed: "retirement[r1].smw4_new"
    value: "238.95"
    work: "Not a joint and survivor annuity, so Table 1 (310) applies; 238.95"
  - printed: "retirement[r1].smw4"
    value: "238.95"
    work: "Worksheet not completed last year, so line 4 = line 2 / line 3 = 238.95"
  - printed: "retirement[r1].smw5"
    value: "2867.40"
    work: "238.95 x 12 months = 2,867.40"
  - printed: "retirement[r1].smw6"
    value: "0.00"
    work: "Amount recovered tax free after 1986 = 0"
  - printed: "retirement[r1].smw7"
    value: "74075.00"
    work: "74,075.00 - 0 = 74,075.00"
  - printed: "retirement[r1].smw8"
    value: "2867.40"
    work: "Smaller of 2,867.40 and 74,075.00"
  - printed: "retirement[r1].smw9"
    value: "0.00"
    work: "1,536.00 - 2,867.40 is below zero, so enter 0"
  - printed: "retirement[r1].cost_left"
    value: "yes"
    work: "Line 7 (74,075.00) is more than 0"
  - printed: "retirement[r1].annuity_with_cost"
    value: "yes"
    work: "The Simplified Method applies and cost is left to recover"
  - printed: "retirement[r1].annuity_rollover"
    value: "no"
    work: "There is no rollover"
  - printed: "retirement[r1].annuity_taxable"
    value: "0.00"
    work: "Equals SMW line 9 = 0.00"
  - printed: "retirement[r1].plan_taxable"
    value: "0.00"
    work: "Simplified Method taxable amount = 0.00"
  - printed: "retirement[r1].taxable"
    value: "0.00"
    work: "Line 5b = 0.00"
  - printed: "retirement[r1].show_a"
    value: "yes"
    work: "Partly taxable annuity, so the total goes on line 5a (SMW line 1)"
  - printed: "retirement[r1].amount_a"
    value: "1536.00"
    work: "Line 5a = box 1 = 1,536.00"
  - printed: "retirement[r2].is_ira"
    value: "no"
    work: "The account kind is a plan"
  - printed: "retirement[r2].roth"
    value: "no"
    work: "The account kind is a plan"
  - printed: "retirement[r2].direct"
    value: "no"
    work: "Code is 7, not G"
  - printed: "retirement[r2].bad_code"
    value: "no"
    work: "Code 7 can be computed; no exception was flagged"
  - printed: "retirement[r2].rolled"
    value: "0.00"
    work: "Amount rolled over is $0.00"
  - printed: "retirement[r2].has_rollover"
    value: "no"
    work: "Nothing was rolled over and the code is not G"
  - printed: "retirement[r2].annuity_with_cost"
    value: "no"
    work: "The Simplified Method does not apply"
  - printed: "retirement[r2].annuity_rollover"
    value: "no"
    work: "No Simplified Method and no rollover"
  - printed: "retirement[r2].plan_excluded"
    value: "1652.00"
    work: "Box 5 1,652.00 + rolled 0 = 1,652.00"
  - printed: "retirement[r2].plan_simple"
    value: "0.00"
    work: "0.00 - 1,652.00 is below zero, so 0"
  - printed: "retirement[r2].plan_taxable"
    value: "0.00"
    work: "Taxable amount = plan_simple = 0.00"
  - printed: "retirement[r2].taxable"
    value: "0.00"
    work: "Line 5b = 0.00"
  - printed: "retirement[r2].show_a"
    value: "no"
    work: "Taxable (0) equals box 1 (0), so it is treated as fully taxable and nothing goes on line 5a"
  - printed: "retirement[r2].amount_a"
    value: "0.00"
    work: "No line 5a entry"
```

### classm.retirement.10

```yaml
lines:
  - printed: "retirement[r1].is_ira"
    value: "no"
    work: "Account kind is plan, not IRA; reported on lines 5a/5b"
  - printed: "retirement[r1].roth"
    value: "no"
    work: "Plan distribution, not a Roth IRA"
  - printed: "retirement[r1].direct"
    value: "no"
    work: "Box 7 code is 2, not G"
  - printed: "retirement[r1].bad_code"
    value: "no"
    work: "Code 2 (early, exception applies) is handled; no listed special situations"
  - printed: "retirement[r1].rolled"
    value: "0.00"
    work: "Amount rolled over given as $0.00; not a direct rollover"
  - printed: "retirement[r1].has_rollover"
    value: "no"
    work: "Rolled over $0 and no code G"
  - printed: "retirement[r1].smw1"
    value: "40461.00"
    work: "Box 1 gross distribution"
  - printed: "retirement[r1].smw2"
    value: "20797.00"
    work: "Cost in plan at annuity starting date"
  - printed: "retirement[r1].smw4"
    value: "1676.00"
    work: "Completed worksheet last year; use last year's line 4"
  - printed: "retirement[r1].smw5"
    value: "20112.00"
    work: "1,676 x 12 months = 20,112"
  - printed: "retirement[r1].smw6"
    value: "18271.00"
    work: "Line 10 of last year's worksheet"
  - printed: "retirement[r1].smw7"
    value: "2526.00"
    work: "20,797 - 18,271 = 2,526"
  - printed: "retirement[r1].smw8"
    value: "2526.00"
    work: "Smaller of 20,112 or 2,526"
  - printed: "retirement[r1].smw9"
    value: "37935.00"
    work: "40,461 - 2,526 = 37,935"
  - printed: "retirement[r1].cost_left"
    value: "yes"
    work: "Line 7 is 2,526, more than zero"
  - printed: "retirement[r1].annuity_with_cost"
    value: "yes"
    work: "Simplified Method applies and line 7 is more than 0"
  - printed: "retirement[r1].annuity_rollover"
    value: "no"
    work: "No amount rolled over"
  - printed: "retirement[r1].annuity_taxable"
    value: "37935.00"
    work: "Simplified Method line 9"
  - printed: "retirement[r1].plan_taxable"
    value: "37935.00"
    work: "Simplified Method taxable amount"
  - printed: "retirement[r1].taxable"
    value: "37935.00"
    work: "Line 5b amount for this distribution"
  - printed: "retirement[r1].show_a"
    value: "yes"
    work: "Partially taxable annuity; enter total on line 5a (worksheet line 1)"
  - printed: "retirement[r1].amount_a"
    value: "40461.00"
    work: "Box 1 total on line 5a"
  - printed: "retirement[r2].is_ira"
    value: "no"
    work: "Account kind is plan, not IRA"
  - printed: "retirement[r2].roth"
    value: "no"
    work: "Plan distribution, not a Roth IRA"
  - printed: "retirement[r2].direct"
    value: "no"
    work: "Box 7 code is 7, not G"
  - printed: "retirement[r2].bad_code"
    value: "no"
    work: "Code 7 (normal distribution) is handled; no listed special situations"
  - printed: "retirement[r2].rolled"
    value: "0.00"
    work: "Amount rolled over given as $0.00"
  - printed: "retirement[r2].has_rollover"
    value: "no"
    work: "Rolled over $0 and no code G"
  - printed: "retirement[r2].annuity_with_cost"
    value: "no"
    work: "Simplified Method does not apply"
  - printed: "retirement[r2].annuity_rollover"
    value: "no"
    work: "Not a Simplified Method annuity; nothing rolled over"
  - printed: "retirement[r2].plan_excluded"
    value: "0.00"
    work: "Box 5 of 0 + rollover of 0 = 0"
  - printed: "retirement[r2].plan_simple"
    value: "34097.00"
    work: "34,097 - 0 = 34,097"
  - printed: "retirement[r2].plan_taxable"
    value: "34097.00"
    work: "No cost and no rollover, so fully taxable"
  - printed: "retirement[r2].taxable"
    value: "34097.00"
    work: "Line 5b amount for this distribution"
  - printed: "retirement[r2].show_a"
    value: "no"
    work: "Fully taxable; no entry on line 5a"
  - printed: "retirement[r2].amount_a"
    value: "0.00"
    work: "None when fully taxable"
```

### classm.retirement.11

```yaml
```yaml
lines:
  - printed: "retirement[r1].is_ira"
    value: "no"
    work: "Kind of account = plan, not an IRA, so it is reported on lines 5a/5b"
  - printed: "retirement[r1].roth"
    value: "no"
    work: "Account is a plan, not a Roth IRA"
  - printed: "retirement[r1].direct"
    value: "no"
    work: "Box 7 code is 7, not G"
  - printed: "retirement[r1].bad_code"
    value: "no"
    work: "Code 7 (normal distribution) is handled; filer answered no to all special situations"
  - printed: "retirement[r1].rolled"
    value: "0.00"
    work: "Amount rolled over within 60 days = $0.00; not a direct rollover"
  - printed: "retirement[r1].has_rollover"
    value: "no"
    work: "Rolled amount is 0 and the code is not G"
  - printed: "retirement[r1].smw1"
    value: "0.00"
    work: "Form 1099-R box 1 = $0.00"
  - printed: "retirement[r1].smw2"
    value: "49049.00"
    work: "Cost in plan at annuity starting date = $49,049.00"
  - printed: "retirement[r1].smw4_t1_360"
    value: "136.25"
    work: "49,049.00 / 360 = 136.25"
  - printed: "retirement[r1].smw4_table1"
    value: "136.25"
    work: "Age 52 (55 or under), start after Nov 18, 1996 -> Table 1 = 360; 49,049 / 360 = 136.25"
  - printed: "retirement[r1].smw4_new"
    value: "136.25"
    work: "Not a joint-and-survivor annuity starting after 1997, so Table 1 (360) applies; 136.25"
  - printed: "retirement[r1].smw4"
    value: "136.25"
    work: "Worksheet not completed last year, so line 4 = line 2 / line 3 = 136.25"
  - printed: "retirement[r1].smw5"
    value: "1635.00"
    work: "136.25 x 12 months = 1,635.00"
  - printed: "retirement[r1].smw6"
    value: "5243.00"
    work: "Amount recovered tax free after 1986 = $5,243.00"
  - printed: "retirement[r1].smw7"
    value: "43806.00"
    work: "49,049.00 - 5,243.00 = 43,806.00"
  - printed: "retirement[r1].smw8"
    value: "1635.00"
    work: "Smaller of 1,635.00 or 43,806.00"
  - printed: "retirement[r1].smw9"
    value: "0.00"
    work: "0.00 - 1,635.00 < 0, so enter 0"
  - printed: "retirement[r1].cost_left"
    value: "yes"
    work: "Line 7 = 43,806.00 > 0"
  - printed: "retirement[r1].annuity_with_cost"
    value: "yes"
    work: "Simplified Method applies and line 7 > 0"
  - printed: "retirement[r1].annuity_rollover"
    value: "no"
    work: "No amount was rolled over"
  - printed: "retirement[r1].annuity_taxable"
    value: "0.00"
    work: "Simplified Method line 9 = 0.00"
  - printed: "retirement[r1].plan_taxable"
    value: "0.00"
    work: "Simplified Method taxable amount = 0.00"
  - printed: "retirement[r1].taxable"
    value: "0.00"
    work: "Line 5b = 0.00"
  - printed: "retirement[r1].show_a"
    value: "yes"
    work: "Partially taxable annuity: box 1 total goes on line 5a (SMW line 1)"
  - printed: "retirement[r1].amount_a"
    value: "0.00"
    work: "Line 5a = box 1 = 0.00"
```
```
