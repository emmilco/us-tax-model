# The persona walks: summary

Written by `node engine/dist/main.js draft-walk` (engine/src/draft-walk.ts; deterministic, no model calls) from the personas in `interview/2025/personas/`, on the built interview (profile `full`, 2025). A topic is the form a question's input belongs to; a switch is a question whose topic differs from the one before it, and a return is a switch to a topic already left. “No, zero, none” counts the questions answered no, zero or with an empty list. A refused persona's figures end at its refusal.

| Persona | Questions | Prompt words | Help words | No, zero, none | Topics | Switches | Returns | End | Problems |
|---|---|---|---|---|---|---|---|---|---|
| `01_single_w2` | 86 | 6777 | 2376 | 78 | 32 | 43 | 12 | complete |  |
| `02_couple_children_mortgage` | 133 | 10168 | 3286 | 95 | 34 | 50 | 17 | complete |  |
| `03_single_parent_child_care` | 121 | 10100 | 2969 | 93 | 35 | 58 | 24 | complete |  |
| `04_retired_couple` | 122 | 9030 | 2970 | 105 | 32 | 50 | 19 | complete |  |
| `05_self_employed` | 133 | 9905 | 2360 | 108 | 34 | 49 | 16 | complete |  |
| `06_investor_loss_carryover` | 114 | 9298 | 2787 | 86 | 33 | 49 | 17 | complete |  |
| `07_college_student` | 110 | 7747 | 2681 | 88 | 33 | 49 | 17 | complete |  |
| `08_hsa_marketplace` | 150 | 10384 | 4105 | 121 | 33 | 48 | 16 | complete |  |
| `09_tips_overtime` | 95 | 7363 | 2466 | 77 | 34 | 49 | 16 | complete |  |
| `10_homeowner_solar_heat_pump` | 117 | 8425 | 6281 | 102 | 32 | 43 | 12 | complete |  |
| `11_refused_rental` | 4 | 490 | 231 | 1 | 3 | 2 | 0 | refused at `scope.schedule1` |  |
| `12_refused_nonresident` | 5 | 678 | 281 | 2 | 3 | 2 | 0 | refused at `scope.other_income` |  |

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
