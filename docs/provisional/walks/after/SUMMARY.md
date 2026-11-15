# The persona walks: summary

Written by `node engine/dist/main.js draft-walk` (engine/src/draft-walk.ts; deterministic, no model calls) from the personas in `interview/2025/personas/`, on the built interview (profile `full`, 2025). A step is one screen: a tick-box group shown together is one step, and its prompt words are its heading and labels, counted once. A topic is the form a question's input belongs to; a switch is a question whose topic differs from the one before it, and a return is a switch to a topic already left. “No, zero, none” counts the questions answered no, zero or with an empty list. A refused persona's figures end at its refusal.

| Persona | Questions | Steps | Prompt words | Help words | No, zero, none | Topics | Switches | Returns | End | Problems |
|---|---|---|---|---|---|---|---|---|---|---|
| `01_single_w2` | 123 | 56 | 1717 | 3090 | 114 | 30 | 58 | 29 | complete |  |
| `02_couple_children_mortgage` | 172 | 97 | 2882 | 4294 | 134 | 32 | 68 | 37 | complete |  |
| `03_single_parent_child_care` | 154 | 81 | 2838 | 3932 | 128 | 33 | 72 | 40 | complete |  |
| `04_retired_couple` | 156 | 82 | 2593 | 3839 | 138 | 31 | 66 | 36 | complete |  |
| `05_self_employed` | 164 | 94 | 3137 | 4037 | 136 | 32 | 61 | 30 | complete |  |
| `06_investor_loss_carryover` | 149 | 82 | 2421 | 3784 | 122 | 32 | 69 | 38 | complete |  |
| `07_college_student` | 143 | 76 | 2146 | 3647 | 124 | 31 | 64 | 34 | complete |  |
| `08_hsa_marketplace` | 198 | 124 | 3195 | 5137 | 168 | 31 | 64 | 34 | complete |  |
| `09_tips_overtime` | 135 | 66 | 1952 | 3495 | 116 | 32 | 61 | 30 | complete |  |
| `10_homeowner_solar_heat_pump` | 151 | 70 | 2075 | 3509 | 134 | 30 | 59 | 30 | complete |  |
| `11_refused_rental` | 18 | 12 | 242 | 504 | 14 | 7 | 12 | 6 | refused at `scope.schedule1` |  |
| `12_refused_nonresident` | 12 | 9 | 159 | 378 | 7 | 5 | 8 | 4 | refused at `scope.other_income` |  |
| `13_ira_saver` | 135 | 66 | 1991 | 3458 | 122 | 32 | 62 | 31 | complete |  |
| `13_self_employed_actual_vehicle_computer` | 212 | 127 | 4116 | 4610 | 165 | 32 | 61 | 30 | complete |  |
| `ny01_single_nyc_w2` | 154 | 83 | 2307 | 3915 | 138 | 32 | 62 | 31 | complete |  |
| `ny02_couple_nyc_children` | 31 | 22 | 501 | 769 | 16 | 6 | 9 | 4 | refused at `ny_it201.gate.child_credit` |  |
| `ny03_retiree_gov_pension` | 169 | 92 | 2817 | 4227 | 146 | 32 | 67 | 36 | refused at `ny_it201.gate.line26` |  |
| `ny04_refused_part_year` | 129 | 62 | 1818 | 3300 | 118 | 31 | 60 | 30 | refused at `ny_it201.gate.part_year_state` |  |
| `ny05_investor_nyc` | 183 | 111 | 3050 | 4693 | 149 | 34 | 73 | 40 | complete |  |

The New York stretch of the personas of profile `ny`: the questions whose input is a line of a New York form (wherever asked; a tick-box screen of them is one step).

| Persona | New York questions | Steps | Prompt words | Help words | No, zero, none | First New York question at | End |
|---|---|---|---|---|---|---|---|
| `ny01_single_nyc_w2` | 27 | 23 | 519 | 713 | 22 | question 128 of 154 | complete |
| `ny02_couple_nyc_children` | 0 | 0 | 0 | 0 | 0 | none | refused at `ny_it201.gate.child_credit` |
| `ny03_retiree_gov_pension` | 10 | 7 | 164 | 314 | 7 | question 160 of 169 | refused at `ny_it201.gate.line26` |
| `ny04_refused_part_year` | 2 | 2 | 30 | 98 | 2 | question 128 of 129 | refused at `ny_it201.gate.part_year_state` |
| `ny05_investor_nyc` | 29 | 24 | 542 | 785 | 24 | question 155 of 183 | complete |

Who each persona is:

- `01_single_w2`: A single person, 31, with one job (one Form W-2, $52,000 of wages) and nothing else to report.
- `02_couple_children_mortgage`: A married couple filing together, each with one job (two Forms W-2, $95,000 and $68,000), two children aged 3 and 6, and a mortgaged home; they itemize.
- `03_single_parent_child_care`: An unmarried parent, 29, with one child aged 4 who lives with her all year, $26,000 of wages from one job, and day care she pays for so she can work; head of household.
- `04_retired_couple`: A retired married couple, 71 and 69, filing together, with social security benefits, one pension (a Form 1099-R), bank interest and some dividends from a mutual fund.
- `05_self_employed`: A single self-employed graphic designer, 38, with one business, a car used partly for the business, and an office in her home.
- `06_investor_loss_carryover`: A single person, 45, with wages from one job and a brokerage account, who sold stock in 2025, received dividends, and carries a capital loss over from 2024.
- `07_college_student`: A single college student, 24, who supports himself with a part-time job ($19,000 of wages) and paid his own tuition for his third year of college.
- `08_hsa_marketplace`: A single person, 34, who bought Marketplace health insurance for January to April (a Form 1095-A), then started a job with a high-deductible health plan and a health savings account.
- `09_tips_overtime`: A single restaurant server, 27, with one job that paid wages, tips and overtime.
- `10_homeowner_solar_heat_pump`: A single homeowner, 52, with wages from one job, who had solar panels and a heat pump installed at her home in 2025.
- `11_refused_rental`: A single person with wages from one job who also rents out a house she owns; the tool does not prepare rental income.
- `12_refused_nonresident`: A single person with wages from one job who was a nonresident alien for part of 2025; the tool does not prepare that return.
- `13_ira_saver`: A single person, 40, with one job that has a 401(k) (one Form W-2, $52,000 of wages), who put $4,000 into a traditional IRA for 2025.
- `13_self_employed_actual_vehicle_computer`: A single self-employed graphic designer, 38, with one business, an office in her home, a van she bought new in 2025 and deducts by its actual costs, and a computer bought new in 2025.
- `ny01_single_nyc_w2`: A single person, 31, who lived in Brooklyn all of 2025 with one job (one Form W-2, $52,000 of wages, New York State and City tax withheld) and nothing else to report.
- `ny02_couple_nyc_children`: A married couple in Queens all of 2025, filing together, each with one job, with two children aged 3 and 6; New York's child credit for a child under 17 is not computed by this tool.
- `ny03_retiree_gov_pension`: A retired married couple in Manhattan all of 2025, 71 and 69, filing together, with social security, a New York City pension (a Form 1099-R), bank interest and some fund dividends.
- `ny04_refused_part_year`: A single person with one job who moved from New Jersey to the Bronx in June 2025; the tool does not prepare a part-year resident's New York return.
- `ny05_investor_nyc`: The investor of persona 06 (one job, interest, dividends and stock sales, a capital loss carried over), living in Manhattan all of 2025.
