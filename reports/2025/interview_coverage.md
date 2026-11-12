# Situations the interview is known to handle (2025)

Written by `node engine/dist/main.js interview-coverage --write` from the rows in `interview/2025/coverage/`; check-all fails when it is not current.
No model is called. Each row names a situation as the answers a filer in it gives. The check walks the built interview with those answers, in the interview's own order, and the row passes only when the walk ends where the row says.

How to read a path: the numbered answers are the row's own (or a named set's, marked), with the question's number in the walk. Every other question on the way was answered by the background return (the last section): the answer a filer with nothing to report gives to the same question. The background answers only the kinds of question it is itself asked; a question opened by the row's answers must be answered by the row. A refusal met on a background answer, or an expected value the background supplied, fails the row.

16 rows: 16 pass, 0 fail. 3 of them are written against the interview as it stands before a redesigned part lands, and are marked for replacement.

## Credits the tool does not figure

Rows: `interview/2025/coverage/credits.yaml`.

| Row | Design row | Situation | How the interview ends |
|---|---|---|---|
| `credits.form_1116` | C.2 row 1 (foreign tax credit needing Form 1116) | A filer paid more foreign tax than can be credited without Form 1116. | Refused at `ftc.needs1116`: Form 1116. The small-tax election is unavailable or not chosen. Form 1116 is deferred, not dropped; prepare it separately. |
| `credits.mortgage_certificate` † | C.2 row 8 (mortgage interest credit, current year) | A homeowner holds a mortgage credit certificate and wants the mortgage interest credit. | Refused at `scope.credits`: Credit Limit Worksheet A, line 2 (Schedule 3 lines 6d, 6f, 6l, 6m). Credits other than the foreign tax credit, the dependent credits, the child and dependent care credit, the education credits, the saver's credit and the residential energy credits are outside this tool. |
| `credits.form_2439` | C.2 row 17 (Form 2439) | A fund sent the filer a Form 2439 for gains it kept and paid tax on. | Refused at `sd.other_forms`: Schedule D additional source forms. Prepare the required source forms; their gains/losses are outside the supported securities slice. |
| `credits.fuel_typed_in` † | C.2 row 16 (credit for federal tax on fuels) | A filer with a fuel tax credit answers the credits screen No and types the Form 4136 amount in. | The return is completed, with `s3.line12` = $250.00. |

† Written against the interview as it stands; to be replaced: the credits screen is taken apart.

Paths:

- `credits.form_1116`: (24 background answers) → 25. `ftc.taxes` = $5,000.00
- `credits.mortgage_certificate`: (2 background answers) → 3. `scope.credits` = Yes
- `credits.form_2439`: (60 background answers) → 61. `sd.other_forms` = Yes
- `credits.fuel_typed_in`: (2 background answers) → 3. `scope.credits` = No → (42 background answers) → 46. `s3.line12` = $250.00 → (30 background answers)

## Health savings accounts

Rows: `interview/2025/coverage/hsa.yaml`.

| Row | Design row | Situation | How the interview ends |
|---|---|---|---|
| `hsa.archer_msa` † | C.3 row 2 (Archer MSA contributions, own or spouse's) | A person with a health savings account also had money put into an Archer MSA for 2025. | Refused at `person[taxpayer].f8889[hsa].unsupported`: Form 8889 Part III, Form 8853, a Form 8889 for a person who died in 2025 (prepare it with the decedent's final return), or other HSA situations. Qualified HSA funding distributions, Archer MSAs, prior-year excess contributions, testing-period failures, inherited HSAs, deemed distributions, withdrawals of excess contributions and repaid mistaken distributions are outside this tool. |
| `hsa.earlier_year_excess` | C.3 row 3 (excess contributions of an earlier year still in the account) | Too much was put into a person's health savings account in an earlier year and is still in it. | Refused at `person[taxpayer].x_other`: Form 5329 Parts II, III, IV, V, VI, VIII or IX, or an earlier-year excess in Part VII. Taxable Coverdell, qualified tuition program or ABLE distributions, excess contributions to IRAs from an earlier year, excess Coverdell, Archer MSA or ABLE contributions, earlier-year HSA excess, and missed required minimum distributions need Form 5329 parts this tool does not prepare. |

† Written against the interview as it stands; to be replaced: the redesigned health savings account questions land.

Paths:

- `hsa.archer_msa`: (15 background answers) → 16. `$f8889@person[taxpayer]` = the entries `hsa` → (11 background answers) → 28. `person[taxpayer].f8889[hsa].unsupported` = Yes
- `hsa.earlier_year_excess`: (43 background answers) → 44. `person[taxpayer].x_other` = Yes

## The opening (who the return is for, and the filing status)

Rows: `interview/2025/coverage/opening.yaml`.

| Row | Design row | Situation | How the interview ends |
|---|---|---|---|
| `opening.couple` | C.1 row 1 (married, filing together) | A married couple puts both incomes on one return and is not asked for a filing status or whose entry is whose. | Recorded without being asked: `f1040.status` = `mfj` (Married, and filing together with my husband or wife on one return (married filing jointly)), `person[taxpayer].role` = `taxpayer`, `person[spouse].role` = `spouse`. Not asked on the way: `f1040.status`. |
| `opening.couple_spouse_died` | C.1 row 2 (filing together, spouse died in 2025) | A person whose husband or wife died during 2025 files one return for the two of them. | The return is completed, with `f1040.status` = `mfj` (Married, and filing together with my husband or wife on one return (married filing jointly)), `household.spouse_died_2025` = Yes. |
| `opening.pair_not_married` | C.1 row 3 (filing together, not married, no death) | Two people who are not married to each other choose one return together. | Stopped as conflicting answers at `household.filing_status_conflict`: Filing status inconsistent with your marriage facts. Correct the filing status or marriage facts. A person married at the end of 2025 cannot file as single; filing jointly requires marriage at year end or the death of a spouse during 2025. The head of household and qualifying surviving spouse tests are checked separately. |
| `opening.separate` | C.1 row 4 (married, filing a separate return) | A married person files a return apart from their husband or wife. | Refused at `s3.mfs`: Married filing separately. The rules for a married filing separately return (among them a spouse who itemizes, the Social Security base for spouses who lived together and the credits a separate return cannot take) are outside this tool. Married filing jointly is supported. |
| `opening.living_apart_parent` | C.1 row 5 (married, living apart, child at home; may be head of household) | A married parent who lives apart from their husband or wife picks the line about paying for a home and is asked whether they count as unmarried. | Asked next: `household.unmarried`, “Were you unmarried at the end of 2025, or considered unmarried for head of household?”. |
| `opening.unmarried_with_child` | C.1 row 6 (unmarried with a child or supported relative) | An unmarried person who pays for the home of their child picks the line about a home, says they were unmarried, and is asked about the cost of the home. | Asked next: `household.home_cost`, “Did you pay over half the cost of keeping up your home for 2025? Cost of keeping up a home includes expenses such as rent, mortgage interest, real estate taxes, insurance on the home, repairs, utilities, and food eaten in the home. It does not include the cost of clothing, education, medical treatment, vacations, life insurance, or transportation, or the value of your services or those of a member of your household. Amounts paid out of funds received in the name of a person who lives in the home, such as their Social Security, count as paid by that person, not you. TANF or similar payments you received and used for the home count as paid by you.”. |
| `opening.widowed_with_child` | C.1 row 7 (widowed in 2023 or 2024 with a child) | A person widowed in 2023 or 2024 whose child lives with them picks that line and is asked its five tests. | Asked next: `household.qss_eligible`, “Do all five of these tests apply to you?”. |
| `opening.single` | C.1 row 8 (unmarried, none of these) | An unmarried person with no child or supported relative takes the last line and files as single. | The return is completed, with `f1040.status` = `single` (None of these: I was not married (single)), `person[taxpayer].role` = `taxpayer`. |
| `opening.married_picks_single` | C.1 row 9 (married, picks "None of these") | A married person takes the line that says they were not married, then says they were married at the end of 2025. | Stopped as conflicting answers at `household.filing_status_conflict`: Filing status inconsistent with your marriage facts. Correct the filing status or marriage facts. A person married at the end of 2025 cannot file as single; filing jointly requires marriage at year end or the death of a spouse during 2025. The head of household and qualifying surviving spouse tests are checked separately. |
| `opening.widowed_this_year_alone` | C.1 row 10 (spouse died in 2025, filing alone) | A person whose husband or wife died during 2025 files for themselves alone as single. | Refused at `household.widowed_2025`: Filing status after a spouse's death in 2025. Your spouse died in 2025, so you are considered married for the whole year for filing status; file a joint return with your deceased spouse (married filing jointly), or a separate return, which this tool does not support. |

Paths:

- `opening.couple`: 1. `$person` = the entries `taxpayer`, `spouse`
- `opening.couple_spouse_died`: 1. `$person` = the entries `taxpayer`, `spouse` → (8 background answers) → 10. `household.married` = No → 11. `household.spouse_died_2025` = Yes → (75 background answers)
- `opening.pair_not_married`: 1. `$person` = the entries `taxpayer`, `spouse` → (8 background answers) → 10. `household.married` = No → 11. `household.spouse_died_2025` = No
- `opening.separate`: 1. `$person` = the entries `taxpayer` → 2. `f1040.status` = `mfs` (Married, and filing apart from my husband or wife (married filing separately))
- `opening.living_apart_parent`: 1. `$person` = the entries `taxpayer` → 2. `f1040.status` = `hoh` (I paid over half the cost of the home of my child, or of a relative I support (head of household)) → (7 background answers)
- `opening.unmarried_with_child`: 1. `$person` = the entries `taxpayer` → 2. `f1040.status` = `hoh` (I paid over half the cost of the home of my child, or of a relative I support (head of household)) → (7 background answers) → 10. `household.unmarried` = Yes
- `opening.widowed_with_child`: 1. `$person` = the entries `taxpayer` → 2. `f1040.status` = `qss` (Widowed in 2023 or 2024, not remarried, and my child lived with me all of 2025 (qualifying surviving spouse)) → (7 background answers)
- `opening.single`: 1. `$person` = the entries `taxpayer` → 2. `f1040.status` = `single` (None of these: I was not married (single)) → (7 background answers) → 10. `household.married` = No → 11. `household.spouse_died_2025` = No → (65 background answers)
- `opening.married_picks_single`: 1. `$person` = the entries `taxpayer` → 2. `f1040.status` = `single` (None of these: I was not married (single)) → (7 background answers) → 10. `household.married` = Yes
- `opening.widowed_this_year_alone`: 1. `$person` = the entries `taxpayer` → 2. `f1040.status` = `single` (None of these: I was not married (single)) → (7 background answers) → 10. `household.married` = No → 11. `household.spouse_died_2025` = Yes

## The background return

The 76 questions a filer with nothing to report is asked, in order, and the answer given to each: no, zero, none or the first option (the other option where that one refuses). It is the minimal return `interview-rules` checks to completion.

| # | Question | Answer |
|---|---|---|
| 1 | `$person` | the entries `taxpayer` |
| 2 | `f1040.status` | `single` (None of these: I was not married (single)) |
| 3 | `scope.credits` | No |
| 4 | `scope.other_line16` | No |
| 5 | `scope.schedule1` | No |
| 6 | `scope.other_income` | No |
| 7 | `$f1095a` | none |
| 8 | `$retirement@person[taxpayer]` | none |
| 9 | `$dependent` | none |
| 10 | `household.married` | No |
| 11 | `household.spouse_died_2025` | No |
| 12 | `person[taxpayer].under16` | No |
| 13 | `household.community_property` | No |
| 14 | `$w2@person[taxpayer]` | none |
| 15 | `$interest` | none |
| 16 | `$f8889@person[taxpayer]` | none |
| 17 | `div.any` | No |
| 18 | `f1040.line25b` | $0.00 |
| 19 | `f1040.line25c_other` | $0.00 |
| 20 | `f1040.line26` | $0.00 |
| 21 | `f4952.has_interest` | No |
| 22 | `f4952.line4g` | $0.00 |
| 23 | `f8863.paid` | No |
| 24 | `f8959.unsupported` | No |
| 25 | `ftc.taxes` | $0.00 |
| 26 | `person[taxpayer].age65` | No |
| 27 | `person[taxpayer].educator_expenses` | $0.00 |
| 28 | `person[taxpayer].rrta` | No |
| 29 | `refund.received` | $0.00 |
| 30 | `s1.alimony` | No |
| 31 | `s1.line8_other` | No |
| 32 | `$oi8z` | none |
| 33 | `s1.cod_any` | No |
| 34 | `s1.gambling_winnings` | $0.00 |
| 35 | `s1.line8g` | $0.00 |
| 36 | `s1.line8h` | $0.00 |
| 37 | `s1.line8i` | $0.00 |
| 38 | `s1.line8j` | $0.00 |
| 39 | `s1.line8r` | $0.00 |
| 40 | `s1.uc_paid` | $0.00 |
| 41 | `s1a.carloan` | No |
| 42 | `s2.amt` | No |
| 43 | `s2.other` | No |
| 44 | `person[taxpayer].x_other` | No |
| 45 | `s3.line10` | $0.00 |
| 46 | `s3.line12` | $0.00 |
| 47 | `s3.line14` | $0.00 |
| 48 | `sa.dependent` | No |
| 49 | `person[taxpayer].blind` | No |
| 50 | `sa.elect_itemize` | No |
| 51 | `sa.excluded_income` | No |
| 52 | `sa.unsupported` | No |
| 53 | `sa.gifts` | No |
| 54 | `sa.line1` | $0.00 |
| 55 | `sa.line5a` | $0.00 |
| 56 | `sa.line5b` | $0.00 |
| 57 | `sa.line5c` | $0.00 |
| 58 | `sa.line8a` | $0.00 |
| 59 | `sb.foreign_any` | No |
| 60 | `sd.carryover` | No |
| 61 | `sd.other_forms` | No |
| 62 | `$sales` | none |
| 63 | `sli.interest` | $0.00 |
| 64 | `ssb.benefits` | $0.00 |
| 65 | `$sc@person[taxpayer]` | none |
| 66 | `s1a.overtime` | No |
| 67 | `s1a.tips` | No |
| 68 | `s179.line10` | $0.00 |
| 69 | `f2441.benefits` | No |
| 70 | `f2441.care` | No |
| 71 | `person[taxpayer].sav_trad` | No |
| 72 | `qbi.unsupported` | No |
| 73 | `qbi.carryforward` | $0.00 |
| 74 | `f5695.part1_any` | No |
| 75 | `f5695.part2_any` | No |
| 76 | `person[taxpayer].eic_ssn` | No |
