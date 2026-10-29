# Adjudication — dependent

Method: `README.md` in this directory. Round-2 rulings proposed in `.transcription/proposed/round2/` (archived as `proposed-round2__*` under `.transcription/archive/before-round3-2026-10-26/`); round-3 rulings in `.transcription/proposed/round3/` (`transcription.dependent.json`,
`transcription.dependent.deepseek.json`, `render.dependent.json`, `render.dependent.deepseek.json`, `classm.dependent.json`); Stage 18 rulings in `.transcription/proposed/stage18/` (`transcription.dependent.json`,
`transcription.dependent.deepseek.json`, `render.dependent.json`, `render.dependent.deepseek.json`, `classm.dependent.json`,
`classm.dependent.deepseek.json`).

## Round 1 (superseded subject)

No round-1 adjudication: the Claude transcription log had no open rulings then, and the earlier deepseek rulings were made
under the pre-adjudication regime (archived in `.transcription/archive/before-adjudication-fixes-2026-10-26/`).

## Round 2 (superseded subject)

Subject after BUG-0153 (`born_died`, `hoh_part_year`, `hoh_lived_half`; `parent_home_paid` reworded). Triage
`../triage/dependent.json` uses executable-triage-v2: 1,094 fixtures, 500 generated returns (seed 20261026) and 1,819
partial records, for 5,475 comparisons per line. The deepseek reply is invalid (`dc_count`: collection parent binding
mismatch). It is ruled by reading, and triage cannot execute it.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | ctc_child | scope | 2 differ: 1 value (classm.sc.2), 1 project-refuses; both on refused returns | i1040gi p. 18, Step 2 q. 3 | The candidate's joint-return route is right, but every return with sa.dependent yes is refused at line 12e. |
| claude | transcription | odc_person | scope | 145 differ: 142 project-refuses (claimed_no_tin, income_exception), 3 project-unknown | i1040gi p. 19, Step 5; p. 22 | The only differences are cited refusals and the income-exception answers. |
| claude | transcription | ctc_amount | scope | same 2 records as ctc_child | f1040s8812 line 5 | Inherited. |
| claude | transcription | odc_amount | scope | same 145 records as odc_person | f1040s8812 line 7 | Inherited. |
| claude | transcription | actc_amount | scope | same 2 records as ctc_child | f1040s8812 line 16b | Inherited. |
| claude | transcription | hoh_test2 | model error | 241 differ: 28 candidate-unknown, 147 project-refuses, 66 project-unknown; no value | i1040gi p. 14, Test 2 item 1(b); p501 p. 9 | The candidate asks residency and born_died of persons Test 2 excludes. It agrees with BUG-0153 on all head of household regressions. |
| claude | transcription | hoh_test1 | scope | 197 differ: 123 project-refuses, 74 project-unknown (tin) | i1040gi p. 14, Test 1 | The differences are cited refusals and question order. |
| claude | transcription | dc_qp | finding | 848 value (all care no and benefits no: representation), 590 candidate-unknown dc_incapable (model error), 154 candidate-refuses; constructed witness | p503 p. 3, Birth or death | The disabled route defaults the death-year residency rule (F1). The candidate applies it. |
| claude | transcription | 2(d) | representation | 676 differ: 10 value on records with dc_paid supplied for a non-qualifying person; 227 project-unknown | i2441 p. 3, Line 2; amb.2025.dc_line30 | Column (d) is summed only for qualifying persons, and the interview asks dc_paid only for them. |
| claude | transcription | 2(c) | model error | 14 value (care no, e.g. classm.dependent.1, generated 35); 286 candidate-unknown | i2441 p. 3, Column (c) | The candidate checks the box for a person with no care, on a return with no Form 2441. |
| deepseek | transcription | ctc_child | scope | not executable | i1040gi p. 18, Step 2 q. 3 | The only difference is behind the sa.dependent screen. |
| deepseek | transcription | odc_person | model error | not executable | i1040gi p. 17, Before you begin; p. 19, Step 5 q. 1 | Omits the filer SSN-or-ITIN test. |
| deepseek | transcription | ctc_amount | scope | not executable | f1040s8812 line 5 | Inherited. |
| deepseek | transcription | odc_amount | model error | not executable | i1040gi p. 19, Step 5 q. 1 | Inherited. |
| deepseek | transcription | actc_amount | scope | not executable | f1040s8812 line 16b | Inherited. |
| deepseek | transcription | hoh_test2 | model error | not executable | p501 p. 9, Death or birth; i1040gi p. 14 item 1(b) | No part-year rule, and it counts an all-year-only sibling_descendant. |
| deepseek | transcription | hoh_test1 | scope | not executable | i1040gi p. 14, Test 1 | Same test; only the placement of refusals differs. |
| deepseek | transcription | eic_child | model error | not executable | i1040gi p. 44 | Refuses on divorced_rule, which the EIC child test does not need. |
| deepseek | transcription | eic_ssn_child | model error | not executable | i1040gi p. 46 | Inherited from eic_child. |
| deepseek | transcription | dc_qp | scope | not executable | i2441 p. 1, "or could claim as a dependent except" | Nondependent qualifying persons are refused by f2441.nondependent. The care omission does not reach any amount. |
| deepseek | transcription | dc_count | model error | validation failure | i2441 p. 3, Line 2 | Collection parent binding mismatch. |
| deepseek | transcription | 2(c) | representation | not executable | i2441 p. 3, Column (c) | Same age and incapacity test; differences come only through dc_qp. |
| claude | render | 2(d) | ambiguity | - | amb.2025.dc_line30; i2441 p. 4, Column (d) | The model reads the register's rejected reading (column (d) net of benefits). |
| deepseek | render | 2(d) | ambiguity | - | amb.2025.dc_line30 | Same. |
| claude | class M | classm.dependent.1 — dependent[dep_b].dc_line2c | model error (drop) | f2441.care no, f2441.benefits no | i2441 p. 3, Column (c) | Box checked where no care was provided. |

Findings: three, in `.transcription/proposed/round2/dependent.findings.md`. F1: `dc_disabled_qp` defaults p503's
death-year rule (constructed witness: line 11 $0 against $600). F2: head of household's adoption and foster-placement
part-year rule is defaulted for a non-qualifying-child person (line 12e refused against $23,625). F3: the `hoh_part_year`
question omits juvenile detention. F1 and F2 are pre-existing gaps next to BUG-0153. F3 was introduced by it. BUG-0153's
own logic agrees with p501 p. 9 and i1040gi p. 15, asks its questions only for a claimed non-qualifying-child relative with
months 6 or fewer on a head of household return, and changes no other test.

## Round 3 (superseded subject)

Subject after BUG-0157 (`dc_lived_half`) and BUG-0158 (`placed`, `part_year_home`, `hoh_lived_half`). Both replies are
invalid (`dc_count`: collection parent binding mismatch), so `../triage/dependent.json` and
`../triage/dependent.deepseek.json` executed nothing. Only `dc_count` carries the error, and no other candidate line
depends on it. The other lines are ruled by reading the expressions against the source, after normalizing nesting and
order. Witnesses named "by reading" are fixtures the candidate was not run on.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | ctc_child | scope | not executable; only diff: mfj or sa.dependent no | i1040gi p. 18, Step 2 q. 3; sa.standard refusal (pp. 34–35) | The candidate's joint-return route is right, but every return with sa.dependent yes is refused. |
| claude | transcription | odc_person | scope | not executable; same single diff | i1040gi p. 18, Step 2 q. 3; p. 19, Step 4 q. 4 | Same. |
| claude | transcription | ctc_amount | scope | not executable; inherited guard | f1040s8812 line 5 | Inherited. |
| claude | transcription | odc_amount | scope | not executable; inherited guard | f1040s8812 line 7 | Inherited. |
| claude | transcription | actc_amount | scope | not executable; inherited guard | f1040s8812 line 16b | Inherited. |
| claude | transcription | hoh_test2 | model error | not executable; by reading stage8.hoh.adopted_part_year | i1040gi p. 15; p501 p. 9, Death or birth | No part-year route (born_died, placed, part_year_home were published); the dropped married test is representation. |
| claude | transcription | hoh_test1 | scope | not executable; only the mfj diff | i1040gi p. 14, Test 1 | Same Test 1 conditions. |
| claude | transcription | dc_qp | model error | not executable; by reading stage15.f2441.parent_died_part_year (project yes, $600) | p503 p. 3, Birth or death | The disabled route needs months > 6, dropping BUG-0157's rule; omitting care reaches no amount. |
| claude | transcription | dc_count | model error | validation failure | i2441 p. 3, Line 2 | Collection parent binding mismatch. |
| claude | transcription | 2(d) | model error | not executable; same witness ($4,000 against $0) | p503 p. 3; i2441 p. 3, Line 2 | Inherits dc_qp's error; showing dc_paid for a non-qualifying person is representation (never asked). |
| claude | transcription | 2(c) | model error | not executable; same witness; classm.dependent.1 dep_b | p503 p. 3; i2441 p. 3, Column (c) | Inherits dc_qp's error and checks the box with no care. |
| deepseek | transcription | ctc_child | scope | not executable; omits sa.dependent (listed as a refusal gate) | i1040gi p. 18, Step 2 q. 4 | The project refuses those returns. |
| deepseek | transcription | odc_person | model error | not executable | i1040gi p. 19, Step 5 q. 1; Step 4 relationship list | Omits the filer SSN-or-ITIN test; treats sibling_descendant as a relative. |
| deepseek | transcription | ctc_amount | scope | not executable | f1040s8812 line 5 | Inherited. |
| deepseek | transcription | odc_amount | model error | not executable | i1040gi p. 19, Step 5 q. 1 | Inherited. |
| deepseek | transcription | actc_amount | scope | not executable | f1040s8812 line 16b | Inherited. |
| deepseek | transcription | hoh_test2 | model error | not executable; by reading stage8.hoh.adopted_part_year | i1040gi p. 15; p501 p. 9; p. 19 Step 4 | No part-year rule; counts a sibling_descendant who did not live with you all year. |
| deepseek | transcription | hoh_test1 | scope | not executable | i1040gi p. 14, Test 1 | Same test; sa.dependent moved to a refusal gate. |
| deepseek | transcription | dc_qp | model error | not executable; by reading stage15.f2441.parent_died_part_year | p503 p. 3, Birth or death | No death-year rule (new since round 2); its non-dependent route is behind f2441.nondependent (scope). |
| deepseek | transcription | dc_count | model error | validation failure | i2441 p. 3, Line 2 | Collection parent binding mismatch. |
| deepseek | transcription | 2(c) | model error | not executable; same witness | p503 p. 3; i2441 p. 3, Column (c) | Inherits dc_qp's error and omits care. |
| claude | render | 2(d) | ambiguity | MISMATCH | amb.2025.dc_line30; Form 2441 line 30 | The model reads the rejected reading (column (d) net of benefits). |
| claude | render | 2(c) | model error | MISMATCH | i2441 p. 1, "or could claim as a dependent except" | The excluded non-dependents are refused by f2441.nondependent_gate. Checking that screen found F1. |
| deepseek | render | 2(d) | ambiguity | MISMATCH | amb.2025.dc_line30; Form 2441 line 30 | Rejected reading; line 30 subtracts all of line 28 (lines 24 and 25). |
| deepseek | render | 2(c) | model error | MISMATCH | i2441 p. 3, Column (c); p503 p. 3 | A person over 13 at year end was over 12 for all included care, which is limited to care while disabled. |
| claude | class M | classm.dependent.1 — dependent[dep_b].dc_line2c | model error (drop) | f2441.care no, f2441.benefits no | i2441 p. 3, Column (c) | Box checked where no care was provided. |

Findings: one, in `.transcription/proposed/round3/dependent.findings.md`. F1 (form f2441, found by checking BUG-0157's
reach): the `f2441.nondependent` screen asks "lived with you for more than half of 2025" and omits p503 p. 3's
death-year rule. A non-dependent disabled person who died after living with the filer for more than half of the time
alive is then not refused, and the credit is understated (amount, rare). BUG-0157 and BUG-0158 themselves agree with
p503 p. 3, i1040gi pp. 15 and 21 and p501 p. 9. No finding was introduced by them.

## Stage 18

Subject after Stage 18 (`ptc_files`, `ptc_magi`, `ptc_magi_counted`; D7(b)). Both replies validate and execute for the
first time: `../triage/dependent.json` and `../triage/dependent.deepseek.json` (executable-triage-v2; 1,222 fixtures, 500
generated returns seed 20261026, 2,111 partial records; 6,774 comparisons per line). Most differences are old lines the
fresh replies rewrote; each is ruled on every kind it shows. Witnesses were rebuilt with `triage.py --explain`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | claimed | finding (F2) | 395 value (154 completed), 133 project-refuses, 105 project-unknown, 75 candidate-refuses, 52 candidate-unknown; classm.u1250.2.deepseek, classm.dependent.4.deepseek, classm.s3.4 | i1040gi p. 19, Step 4 last bullet; p. 21, Multiple support agreements | The candidate drops `other` and counts `household_member` with 10 months, and refuses multiple support on a qualifying child (model errors); its note exposes that `other` with 12 months is counted without the local-law condition. |
| claude | transcription | ctc_child | model error | 101 candidate-refuses, 26 candidate-unknown, 111 project-unknown, 1 value (classm.sc.2, refused) | i1040gi p. 18, Step 3 | Same Step 3 test; differences inherit its `claimed` (multiple support) and the sa.dependent route (scope). |
| claude | transcription | ctc_amount, actc_amount | model error | same 239 records | f1040s8812 lines 5, 16b | Inherited. |
| claude | transcription | odc_person | model error | 322 value (`other`, 12 months), 133 project-refuses, 77 candidate-refuses | i1040gi p. 19, Step 5; Step 4 | Inherits `claimed`; the `other` values bear on F2. |
| claude | transcription | odc_amount | model error | same 600 records | f1040s8812 line 7 | Inherited. |
| claude | transcription | hoh_test2 | model error | no value; 133 project-refuses, 75 candidate-refuses, 52 candidate-unknown | i1040gi p. 14, Test 2; p501 p. 9 | Part-year route now present; only the multiple-support refusal and claimed_no_tin (scope) differ. |
| claude | transcription | hoh_test1 | scope | no value; 61 project-refuses, 81 project-unknown | i1040gi p. 14, Test 1 | Same test; differences are the cited claimed_no_tin refusal and tin partials. |
| claude | transcription | dc_qp | model error | 1,332 value (care no), 779 candidate-unknown, 295 candidate-refuses | i2441 p. 1, Qualifying Person(s); p503 p. 3 | Care omission reaches no amount (representation); asks dc_incapable with no care and applies the placement rule to Form 2441. |
| claude | transcription | dc_count | model error | 4,135 value, 819 candidate-unknown, 299 candidate-refuses | i2441 p. 3, Line 2 | Values are representation (counted only where dc_qp); the rest inherit dc_qp. |
| claude | transcription | ptc_magi_counted | representation | 818 project-unknown, 299 candidate-refuses, 1 value (stage18.mut.unclaimed_relative) | i8962 p. 8, Line 2b; p. 3 | Line 2b sums only claimed dependents; the refusals inherit `claimed`. |
| claude | transcription | 2(d) | model error | 55 value (dc_paid on a non-qualifying entry), 217 project-unknown, 284 candidate-unknown, 299 candidate-refuses | i2441 p. 3, Line 2 | Values are representation (never asked, never summed); the rest inherit dc_qp. |
| claude | transcription | 2(c) | model error | 15 value (care no: classm.dependent.1 dep_b, generated 10, 23), 352 candidate-unknown | i2441 p. 3, Column (c); p. 1 | Checks the box with no care. |
| deepseek | transcription | claimed | model error | 293 value, 134 project-refuses, 125 project-unknown, 76 candidate-refuses, 110 candidate-unknown; classm.dependent.4.deepseek, classm.f8995a.2, classm.dependent.3.deepseek | i1040gi p. 19, Step 4; p. 18, Step 2 q. 1 | No all-year test for household_member or sibling_descendant, no citizenship test on the child route, multiple support on a qualifying child; married-no/joint-return-yes records are representation. |
| deepseek | transcription | ctc_child | model error | 1,908 value (975 completed), 405 candidate-unknown, 102 candidate-refuses | i1040gi p. 18, Step 3 | Gives the child tax credit to qualifying relatives under 17 (classm.f4952.1.deepseek). |
| deepseek | transcription | ctc_amount, actc_amount | model error | same 2,418 records | f1040s8812 lines 5, 16b | Inherited. |
| deepseek | transcription | odc_person, odc_amount | model error | 2,126 value, 183 candidate-unknown, 134 project-refuses | i1040gi p. 19, Step 5 | Mirror of ctc_child; inherits `claimed`. |
| deepseek | transcription | hoh_test2 | model error | 13 value (stage8.hoh.parent.died_lived_part_year), 210 project-unknown | i1040gi p. 14; p501 p. 9 | No part-year rule, as round 3. |
| deepseek | transcription | hoh_test1 | scope | no value; 270 candidate-refuses, 88 candidate-unknown, 51 project-refuses | i1040gi p. 14, Test 1 | Same test; refusals reached through `claimed` on returns the project refuses (multiple support on a child: model error). |
| deepseek | transcription | eic_child, eic_ssn_child | model error | no value; 74 candidate-refuses (73 refused returns), 85 candidate-unknown | i1040gi p. 41, Step 3; p. 44 | Refuses and asks divorced_rule, which the EIC test does not need, as round 2. |
| deepseek | transcription | dc_qp | model error | 1,451 value (care no), 854 candidate-unknown, 295 candidate-refuses | i2441 p. 1; p503 p. 3 | No birth-or-death rule; dc_under13 asked of everyone and read without age; care omission is representation. |
| deepseek | transcription | dc_count | model error | 3,941 value, 890 candidate-unknown, 299 candidate-refuses | i2441 p. 3, Line 2 | Values representation; rest inherit dc_qp. |
| deepseek | transcription | 2(c) | model error | no value; 1,155 candidate-unknown | i2441 p. 3, Column (c) | Asks dc_over12_care of every incapable entry, without dc_qp or care. |
| claude | render | 2(d) | ambiguity | MISMATCH | amb.2025.dc_line30 | Rejected reading (column (d) net of benefits). |
| deepseek | render | 2(d) | ambiguity | MISMATCH | amb.2025.dc_line30; amb.2025.dc_ineligible_providers | Both points are recorded readings (Pub. 503's provider list is chosen). |
| claude | class M | classm.dependent.1 — dependent[dep_b].dc_line2c | model error (drop) | f2441.care no; dc_qp no | i2441 p. 3, Column (c) | Box checked with no care, as rounds 2 and 3. |
| claude | class M | classm.dependent.5 — dependent[dep_b].dc_line2d | representation (drop) | dc_qp no; dc_paid $250.00 supplied; line 3 $1,480.00 either way | i2441 p. 3, Line 2 | The model's $0.00 is the source reading; the project's $250.00 is a display of an answer the interview never asks and line 3 never sums. |
| deepseek | class M | classm.dependent.1 — dependent[dep_b].dc_line2c | model error (drop) | same inputs | i2441 p. 3, Column (c) | Same; also reads permanent disability for inability to care for oneself. |
| deepseek | class M | classm.dependent.5 — dependent[dep_b].dc_line2d | representation (drop) | same inputs | i2441 p. 3, Line 2 | Same. |

Findings: one, F2 in `.transcription/proposed/stage18/dependent.findings.md` (low): `dependent.qr_relationship` counts
`other` with 12 months without the local-law condition of i1040gi p. 19. Pre-existing, raised by the Claude reply's note.
The Stage 18 lines themselves (`ptc_files`, `ptc_magi`, `ptc_magi_counted`) agree with i8962 p. 8 under
amb.2025.ptc_dependent_filing; no finding against them.
