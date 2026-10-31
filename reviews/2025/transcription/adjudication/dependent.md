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

## Stage 18 (superseded subject)

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

## Stage 19 (superseded subject)

Subject after Stage 19 (the `dependent.edu_*` block and lines 23 to 31 through `aqee`). Fresh replies of 2026-10-29.
Full ruling text: `.transcription/proposed/stage19/transcription.dependent.json`, `transcription.dependent.deepseek.json`,
`render.dependent.json`, `render.dependent.deepseek.json`, `classm.dependent.json`, `classm.dependent.deepseek.json`.
Claude triage: `../triage/dependent.json`, executable-triage-v2 (1,306 fixtures, 500 generated returns seed 20261026,
2,299 partial records; 6,922 comparisons per line). The deepseek-flash reply fails validation (`dependent.dc_count`,
collection parent binding mismatch), so its lines are ruled by reading. The old lines repeat Stage 18's points; each is
re-checked against the rewritten replies (the Claude reply dropped its part-year HOH route and the `other` relationship;
the deepseek reply dropped its filer SSN tests). Every edu line other than 27 to 31 agreed in both families.

Counts — claude transcription: finding 1 (carried), model error 15, representation 2; deepseek transcription: model error
17, representation 1; render (each family): ambiguity 1; class M (each family): representation 1 (dropped).

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | dependent.claimed | finding | 6,289/6,922 agree; 8 candidate-refuses, 48 candidate-unknown, 124 project-refuses, 96 project-unknown, 357 value | i1040gi p. 19, Step 4 | BUG-0192 (other without the local-law test) still open; the reply drops other altogether and refuses multiple support for a child. |
| claude | transcription | dependent.ctc_child | model error | 6,625/6,922 agree; 150 candidate-refuses, 33 candidate-unknown, 84 project-unknown, 30 value | i1040gi p. 18, Step 3 | Filer SSN test now present; differences inherit its claimed (multiple support) and the sa.dependent route (refused). |
| claude | transcription | dependent.ctc_amount | model error | 6,625/6,922 agree; 150 candidate-refuses, 33 candidate-unknown, 84 project-unknown, 30 value | i1040gi p. 21, Multiple support agreements | Filer SSN test now present; differences inherit its claimed (multiple support) and the sa.dependent route (refused). |
| claude | transcription | dependent.actc_amount | model error | 6,625/6,922 agree; 150 candidate-refuses, 33 candidate-unknown, 84 project-unknown, 30 value | i1040gi p. 21, Multiple support agreements | Filer SSN test now present; differences inherit its claimed (multiple support) and the sa.dependent route (refused). |
| claude | transcription | dependent.odc_person | model error | 6,395/6,922 agree; 8 candidate-refuses, 41 candidate-unknown, 124 project-refuses, 35 project-unknown, 319 value | i1040gi p. 19, Step 5 | Values are the other relationship the reply drops (classm.u1250.2.deepseek). |
| claude | transcription | dependent.odc_amount | model error | 6,395/6,922 agree; 8 candidate-refuses, 41 candidate-unknown, 124 project-refuses, 35 project-unknown, 319 value | i1040gi p. 19, Step 5 | Values are the other relationship the reply drops (classm.u1250.2.deepseek). |
| claude | transcription | dependent.hoh_test2 | model error | 6,482/6,922 agree; 8 candidate-refuses, 65 candidate-unknown, 124 project-refuses, 240 project-unknown, 3 value | i1040gi p. 14, Test 2 | Drops last round's part-year route (stage8.hoh.parent.died_lived_part_year). |
| claude | transcription | dependent.hoh_test1 | model error | 6,561/6,922 agree; 158 candidate-refuses, 1 candidate-unknown, 117 project-refuses, 85 project-unknown | i1040gi p. 14, Test 1 | Same Test 1; refusals inherit its claimed (multiple support). |
| claude | transcription | dependent.dc_qp | model error | 4,745/6,922 agree; 71 candidate-refuses, 777 candidate-unknown, 5 project-refuses, 6 project-unknown, 1,318 value | i2441 p. 1, Purpose of Form | Care omission reaches no amount; no death-year rule (BUG-0157 case). |
| claude | transcription | dependent.dc_count | model error | 1,575/6,922 agree; 71 candidate-refuses, 837 candidate-unknown, 4,439 value | i2441 p. 3, Line 2 | Values representation (counted only where dc_qp); the rest inherit dc_qp. |
| claude | transcription | dependent.ptc_magi_counted | representation | 5,823/6,922 agree; 310 candidate-refuses, 788 project-unknown, 1 value | i8962 p. 8, Line 2b | Line 2b sums only claimed dependents; refusals inherit claimed. |
| claude | transcription | 2(d) | representation | 6,122/6,922 agree; 71 candidate-refuses, 270 candidate-unknown, 444 project-unknown, 15 value | i2441 p. 3, Line 2 | Values are entries never counted or asked; line 3 unchanged. |
| claude | transcription | 2(c) | model error | 6,258/6,922 agree; 71 candidate-refuses, 575 candidate-unknown, 5 project-refuses, 13 value | i2441 p. 3, Column | Inherits dc_qp: unchecked for the BUG-0157 parent; care omitted. |
| claude | transcription | 27 | model error | 2,594/6,922 agree; 152 candidate-refuses, 1 candidate-shows-skipped, 4,094 candidate-unknown, 6 project-refuses, 17 project-unknown, 58 value | i8863 p. 3, Who cannot claim a credit | Omits filer TIN and f8863.paid (generated 47 shows $4,000.00 on a skipped line); inherits its claimed. |
| claude | transcription | 28 | model error | 2,594/6,922 agree; 152 candidate-refuses, 1 candidate-shows-skipped, 4,094 candidate-unknown, 6 project-refuses, 17 project-unknown, 58 value | i8863 p. 3, Who cannot claim a credit | Omits filer TIN and f8863.paid (generated 47 shows $4,000.00 on a skipped line); inherits its claimed. |
| claude | transcription | 29 | model error | 2,594/6,922 agree; 152 candidate-refuses, 1 candidate-shows-skipped, 4,094 candidate-unknown, 6 project-refuses, 17 project-unknown, 58 value | i8863 p. 3, Who cannot claim a credit | Omits filer TIN and f8863.paid (generated 47 shows $4,000.00 on a skipped line); inherits its claimed. |
| claude | transcription | 30 | model error | 2,594/6,922 agree; 152 candidate-refuses, 1 candidate-shows-skipped, 4,094 candidate-unknown, 6 project-refuses, 17 project-unknown, 58 value | i8863 p. 3, Who cannot claim a credit | Omits filer TIN and f8863.paid (generated 47 shows $4,000.00 on a skipped line); inherits its claimed. |
| claude | transcription | 31 | model error | 2,656/6,922 agree; 151 candidate-refuses, 4,094 candidate-unknown, 6 project-refuses, 12 project-unknown, 3 value | i8863 p. 3, Who cannot claim a credit | Inherits its claimed (generated 398: $0.00 against $10,383.28); omits the filer TIN routing and f8863.paid. |
| claude | render | 2(d) | ambiguity | render MISMATCH | i2441 p. 3, Column | Rejected reading (column (d) net of benefits), as every round. |
| claude | class M | classm.dependent.8 — dependent[dep_b].dc_line2d | representation (drop) | class M DISAGREE | i2441 p. 3, Line 2 | Model's $0.00 is the source reading; $250.00 displays an answer never asked and never summed. |
| deepseek | transcription | dependent.claimed | model error | not executable (reply invalid) | i1040gi p. 19, Step 4 | Counts sibling_descendant as a listed relative without the all-year test; drops the TIN screen. |
| deepseek | transcription | dependent.ctc_child | model error | not executable (reply invalid) | i1040gi p. 18, Step 3 | Drops the filer valid-SSN test. |
| deepseek | transcription | dependent.ctc_amount | model error | not executable (reply invalid) | i1040gi p. 18, Step 3 | Drops the filer valid-SSN test. |
| deepseek | transcription | dependent.actc_amount | model error | not executable (reply invalid) | i1040gi p. 18, Step 3 | Drops the filer valid-SSN test. |
| deepseek | transcription | dependent.odc_person | model error | not executable (reply invalid) | i1040gi p. 19, Step 5 | Drops the filer SSN/ITIN test; inherits claimed. |
| deepseek | transcription | dependent.odc_amount | model error | not executable (reply invalid) | i1040gi p. 19, Step 5 | Drops the filer SSN/ITIN test; inherits claimed. |
| deepseek | transcription | dependent.hoh_test2 | model error | not executable (reply invalid) | i1040gi p. 14, Test 2 | No part-year rule, as round 3. |
| deepseek | transcription | dependent.hoh_test1 | representation | not executable (reply invalid) | i1040gi p. 14, Test 1 | Same Test 1 for a parent; dropped TIN and answered-no refusals are refused cases. |
| deepseek | transcription | dependent.eic_child | model error | not executable (reply invalid) | i1040gi p. 41, Step 3 | Reads divorced_rule, married, other_claimant as conditions the EIC test does not have. |
| deepseek | transcription | dependent.eic_ssn_child | model error | not executable (reply invalid) | i1040gi p. 46, Worksheet A | Inherited from eic_child. |
| deepseek | transcription | dependent.dc_qp | model error | not executable (reply invalid) | i2441 p. 1, Purpose of Form | No birth-or-death rule; care omission is representation. |
| deepseek | transcription | dependent.dc_count | model error | not executable (reply invalid) | i2441 p. 3, Line 2 | Declaration invalid (sum over the parent collection from an entry). |
| deepseek | transcription | 2(c) | model error | not executable (reply invalid) | i2441 p. 3, Column | Copies dc_over12_care with no qualifying-person test. |
| deepseek | transcription | 27 | model error | not executable (reply invalid) | i8863 p. 3, Who cannot claim a credit | No routing at all: shows AOC amounts on lines the form skips; no TIN tests. |
| deepseek | transcription | 28 | model error | not executable (reply invalid) | i8863 p. 3, Who cannot claim a credit | No routing at all: shows AOC amounts on lines the form skips; no TIN tests. |
| deepseek | transcription | 29 | model error | not executable (reply invalid) | i8863 p. 3, Who cannot claim a credit | No routing at all: shows AOC amounts on lines the form skips; no TIN tests. |
| deepseek | transcription | 30 | model error | not executable (reply invalid) | i8863 p. 3, Who cannot claim a credit | No routing at all: shows AOC amounts on lines the form skips; no TIN tests. |
| deepseek | transcription | 31 | model error | not executable (reply invalid) | i8863 p. 3, Who cannot claim a credit | No routing: shows a lifetime learning amount for every student, AOC students included. |
| deepseek | render | 2(d) | ambiguity | render MISMATCH | i2441 p. 3, Column | Rejected reading (column (d) net of benefits), as every round. |
| deepseek | class M | classm.dependent.8 — dependent[dep_b].dc_line2d | representation (drop) | class M DISAGREE | i2441 p. 3, Line 2 | Model's $0.00 is the source reading; $250.00 displays an answer never asked and never summed. |

Findings: Q1 (low, new), `dependent.edu_over`, the same D3-screen wording concern as person Q1
(`.transcription/proposed/stage19/dependent.findings.md`); BUG-0192 (low, open, carried from Stage 18 F2) now also reaches
Form 8863 through `dependent.edu_student`, which reads `dependent.claimed`. The dependent routing (claimed dependent, student
TIN, Form 1098-T, the filer-TIN fallback to line 31) agrees with i8863 pp. 2 to 4.

## Stage 19 round 2 (superseded subject)

Subject after the round-1 fixes (for this entry BUG-0197, the reworded `dependent.edu_over`, and BUG-0199, the new input
`dependent.lawful` in `dependent.qr_relationship`). Fresh replies of 2026-10-29. Full ruling text:
`.transcription/proposed/stage19/round2/transcription.dependent.json`, `transcription.dependent.deepseek.json`,
`render.dependent.json`, `render.dependent.deepseek.json`, `classm.dependent.json`, `classm.dependent.deepseek.json`.
Claude triage: `../triage/dependent.json`, executable-triage-v2 (1,325 fixtures, 500 generated returns seed 20261026,
2,284 partial records; 6,903 comparisons per line). The triage ran before the generator began answering
`dependent.lawful` (engine/src/generate.ts), so generated witnesses with `lawful` unknown are artifacts. The deepseek-flash
reply fails validation (`dependent.dc_count`, collection parent binding mismatch), so its lines are ruled by reading. Both
replies now carry the local-law test for `other`; the Claude reply also applies it to `sibling_descendant`, which exposed
L1.

Counts — claude transcription: finding 1, model error 16, representation 1; deepseek transcription: model error 15, representation 1, scope 3; render: claude ambiguity 1, deepseek ambiguity 1, model error 1; class M (each family): representation 1 (dropped).

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | dependent.claimed | finding | 6,715/6,903 agree; 8 candidate-refuses, 41 candidate-unknown, 53 project-refuses, 72 project-unknown, 14 value | i1040gi p. 19, Step 4; p501 p. 19 | L1: sibling_descendant has no local-law test (exposed by the reply); reply's own household_member and multiple-support errors. |
| claude | transcription | dependent.ctc_child | model error | 6,755/6,903 agree; 30 candidate-refuses, 20 candidate-unknown, 3 project-refuses, 94 project-unknown, 1 value | i1040gi p. 18, Step 3; p. 21 | Differences inherit its claimed (multiple support on a child). |
| claude | transcription | dependent.ctc_amount | model error | 6,755/6,903 agree; 30 candidate-refuses, 20 candidate-unknown, 3 project-refuses, 94 project-unknown, 1 value | f1040s8812 line 5; i1040gi p. 21 | Differences inherit its claimed (multiple support on a child). |
| claude | transcription | dependent.actc_amount | model error | 6,755/6,903 agree; 30 candidate-refuses, 20 candidate-unknown, 3 project-refuses, 94 project-unknown, 1 value | f1040s8812 line 16b; i1040gi p. 21 | Differences inherit its claimed (multiple support on a child). |
| claude | transcription | dependent.odc_person | model error | 6,802/6,903 agree; 8 candidate-refuses, 23 candidate-unknown, 53 project-refuses, 4 project-unknown, 13 value | i1040gi p. 19, Steps 4-5 | household_member without the all-year test (classm.tcw.5). |
| claude | transcription | dependent.odc_amount | model error | 6,802/6,903 agree; 8 candidate-refuses, 23 candidate-unknown, 53 project-refuses, 4 project-unknown, 13 value | i1040gi p. 19, Steps 4-5 | household_member without the all-year test (classm.tcw.5). |
| claude | transcription | dependent.hoh_test2 | model error | 6,528/6,903 agree; 8 candidate-refuses, 67 candidate-unknown, 53 project-refuses, 244 project-unknown, 3 value | i1040gi p. 14, Test 2; p501 p. 9 | No part-year route. |
| claude | transcription | dependent.hoh_test1 | model error | 6,134/6,903 agree; 338 candidate-refuses, 306 candidate-unknown, 47 project-refuses, 78 project-unknown | i1040gi p. 14, Test 1 | Same Test 1; refusals are its claimed's placements. |
| claude | transcription | dependent.dc_qp | model error | 4,308/6,903 agree; 413 candidate-refuses, 722 candidate-unknown, 1 project-refuses, 4 project-unknown, 1,455 value | i2441 p. 1; p503 p. 3 | No death-year rule; care omission reaches no amount. |
| claude | transcription | dependent.dc_count | model error | 1,643/6,903 agree; 417 candidate-refuses, 763 candidate-unknown, 4,080 value | i2441 p. 3, Line 2 | Values representation; rest inherit dc_qp. |
| claude | transcription | dependent.ptc_magi_counted | representation | 6,277/6,903 agree; 417 candidate-refuses, 208 project-unknown, 1 value | i8962 p. 8, Line 2b | Line 2b sums only claimed dependents. |
| claude | transcription | 2(d) | model error | 5,837/6,903 agree; 417 candidate-refuses, 443 candidate-unknown, 196 project-unknown, 10 value | i2441 p. 3, Line 2; p503 p. 3 | Inherits dc_qp: $0.00 for the BUG-0157 parent ($4,000.00). |
| claude | transcription | 2(c) | model error | 6,207/6,903 agree; 413 candidate-refuses, 269 candidate-unknown, 1 project-refuses, 13 value | i2441 p. 3, Column (c); p503 p. 3 | Inherits dc_qp: unchecked for the BUG-0157 parent. |
| claude | transcription | 27 | model error | 3,186/6,903 agree; 153 candidate-refuses, 1 candidate-shows-skipped, 3,558 candidate-unknown, 5 project-refuses | i8863 p. 3, item 5 | No filer-TIN or f8863.paid test (generated 47 shows a skipped $4,000.00). |
| claude | transcription | 28 | model error | 3,186/6,903 agree; 153 candidate-refuses, 1 candidate-shows-skipped, 3,558 candidate-unknown, 5 project-refuses | i8863 p. 3, item 5 | As line 27. |
| claude | transcription | 29 | model error | 3,186/6,903 agree; 153 candidate-refuses, 1 candidate-shows-skipped, 3,558 candidate-unknown, 5 project-refuses | i8863 p. 3, item 5 | As line 27. |
| claude | transcription | 30 | model error | 3,186/6,903 agree; 153 candidate-refuses, 1 candidate-shows-skipped, 3,558 candidate-unknown, 5 project-refuses | i8863 p. 3, item 5 | As line 27. |
| claude | transcription | 31 | model error | 3,186/6,903 agree; 152 candidate-refuses, 3,559 candidate-unknown, 5 project-refuses, 1 value | i8863 p. 3, item 5 | Filer-TIN routing missing (generated 47: $0.00 against $14,396.61). |
| deepseek | transcription | dependent.claimed | model error | not executable (reply invalid) | i1040gi p. 19, Step 4 | sibling_descendant as a listed relative, no all-year test. |
| deepseek | transcription | dependent.ctc_child | model error | not executable (reply invalid) | i1040gi pp. 17-18, Step 3 | No filer SSN test. |
| deepseek | transcription | dependent.ctc_amount | model error | not executable (reply invalid) | i1040gi pp. 17-18, Step 3 | No filer SSN test. |
| deepseek | transcription | dependent.actc_amount | model error | not executable (reply invalid) | i1040gi pp. 17-18, Step 3 | No filer SSN test. |
| deepseek | transcription | dependent.odc_person | model error | not executable (reply invalid) | i1040gi p. 17; p. 19, Step 5 | No filer SSN/ITIN test; inherits claimed. |
| deepseek | transcription | dependent.odc_amount | model error | not executable (reply invalid) | i1040gi p. 17; p. 19, Step 5 | No filer SSN/ITIN test; inherits claimed. |
| deepseek | transcription | dependent.hoh_test2 | model error | not executable (reply invalid) | i1040gi p. 14, Test 2 | No part-year rule. |
| deepseek | transcription | dependent.hoh_test1 | scope | not executable (reply invalid) | i1040gi p. 14, Test 1; p501 p. 10 | Multiple-support exclusion is a refusal in the project. |
| deepseek | transcription | dependent.eic_child | scope | not executable (reply invalid) | i1040gi p. 41, Step 3; p. 44 | Married and tie-breaker cases are project refusals. |
| deepseek | transcription | dependent.eic_ssn_child | scope | not executable (reply invalid) | i1040gi p. 46, Worksheet A | As eic_child. |
| deepseek | transcription | dependent.dc_qp | model error | not executable (reply invalid) | i2441 p. 1; p503 p. 3 | No death-year rule. |
| deepseek | transcription | dependent.dc_count | model error | not executable (reply invalid) | i2441 p. 3, Line 2 | Declaration invalid (sum over the parent collection). |
| deepseek | transcription | 2(d) | model error | not executable (reply invalid) | i2441 p. 3, Line 2; p503 p. 3 | Inherits dc_qp for the BUG-0157 parent. |
| deepseek | transcription | 2(c) | representation | not executable (reply invalid) | i2441 p. 3, Column (c) | dc_paid is asked only of a qualifying person; same box. |
| deepseek | transcription | 27 | model error | not executable (reply invalid) | i8863 p. 3; f8863 p. 2, lines 23-26 | No routing. |
| deepseek | transcription | 28 | model error | not executable (reply invalid) | i8863 p. 3; f8863 p. 2 | No routing. |
| deepseek | transcription | 29 | model error | not executable (reply invalid) | i8863 p. 3; f8863 p. 2 | No routing. |
| deepseek | transcription | 30 | model error | not executable (reply invalid) | i8863 p. 3; f8863 p. 2 | No routing. |
| deepseek | transcription | 31 | model error | not executable (reply invalid) | f8863 p. 2, Caution | LLC amount for every unrouted entry. |
| claude | render | 2(d) | ambiguity | render MISMATCH | i2441 p. 3, Column (d) | Rejected reading (column (d) net of benefits), amb.2025.dc_line30. |
| deepseek | render | 2(d) | ambiguity | render MISMATCH | i2441 p. 3, Column (d) | Rejected reading (column (d) net of benefits), amb.2025.dc_line30. |
| deepseek | render | 2(c) | model error | render MISMATCH | i2441 p. 3, Column (c); dependent.dc_paid | Included care is care while a qualifying person; over 13 at year end means over 12 throughout. |
| claude | class M | classm.dependent.8 — dependent[dep_b].dc_line2d | representation (drop) | class M DISAGREE | i2441 p. 3, Line 2 | dc_paid supplied for a non-qualifying entry; line 3 unchanged. |
| deepseek | class M | classm.dependent.8 — dependent[dep_b].dc_line2d | representation (drop) | class M DISAGREE | i2441 p. 3, Line 2 | dc_paid supplied for a non-qualifying entry; line 3 unchanged. |

Findings: L1 (low, new), `dependent.qr_relationship` asks `dependent.lawful` only for `other`, so a `sibling_descendant`
(a grandniece or a stepsibling's child, none of the listed relatives) who lived with you all year is claimed without the
local-law condition of i1040gi p. 19, Step 4; executed witness: claimed yes and line 19 $1,000.00 where the source gives
$500.00 (`.transcription/proposed/stage19/round2/dependent.findings.md`). BUG-0199 is correct for `other`; BUG-0197 on
`dependent.edu_over` checked, no new error (stale label only).

## Stage 19 round 3 (superseded subject)

Subject after the round-2 finding L1 was fixed (`dependent.qr_relationship` requires `dependent.lawful` for both `other` and
`sibling_descendant`), with the reworded `dependent.lawful` question and the `edu_over` label "exceed its expenses paid to the
institution". Fresh replies of 2026-10-29. Full ruling text: `.transcription/proposed/stage19/round3/transcription.dependent.json`,
`transcription.dependent.deepseek.json`, `render.dependent.json`, `render.dependent.deepseek.json`, `classm.dependent.json`,
`classm.dependent.deepseek.json`. Claude triage: `../triage/dependent.json`, executable-triage-v2 (1,323 fixtures, 500 generated
returns seed 20261026, 2,268 partial records; 6,899 comparisons per line), regenerated after the generator answers
`dependent.lawful` for every entry (generated indices moved: the filer-without-TIN return of round 2, generated 47, is now 99).
The deepseek-flash reply again fails validation (`dependent.dc_count`), so its lines are ruled by reading. L1 checked fixed by
execution (the round-2 witness with `lawful` no: claimed no, line 19 $500.00; with yes: claimed yes, $1,000.00).

Render: the dependent MISMATCH count rose from 1 to 7 per family, but the render prompt changed only in `qr_relationship`, the
`lawful` question and the `edu_over` label, and no new MISMATCH concerns them. The Claude reviewer now objects to the Form 1098-T
request date in `dependent.edu_1098t` (the gate of lines 23 to 31; amb.2025.edu_1098t_date, owner decision D7(d); p970 was not
among its pages); the deepseek reviewer to the ITIN/ATIN "applied for" wording of `dependent.tin` and `household.all_tin` (allowed by
p970 p. 11, which it was not given). Both texts are unchanged since round 2, where they were judged MATCH: reviewer variance, no defect.

Counts — claude transcription: model error 15, representation 1, scope 1; deepseek transcription: model error 15, scope 4; render: claude ambiguity 7, deepseek ambiguity 1, interface gap 6; class M: claude representation 1 (dropped), deepseek model error 1 and representation 1 (both dropped).

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | dependent.claimed | model error | 6,442/6,899 agree; 127 candidate-refuses, 157 candidate-unknown, 103 project-refuses, 69 project-unknown, 1 value | i1040gi p. 19, Step 4; p. 21 | Multiple support refused for a qualifying child; household_member lawful asked again (no amount); sibling_descendant now matches the L1-fixed project. |
| claude | transcription | dependent.ctc_child | model error | 6,622/6,899 agree; 157 candidate-refuses, 20 candidate-unknown, 99 project-unknown, 1 value | i1040gi p. 18, Step 3; p. 21 | Differences inherit its claimed (multiple support on a child). |
| claude | transcription | dependent.ctc_amount | model error | 6,622/6,899 agree; 157 candidate-refuses, 20 candidate-unknown, 99 project-unknown, 1 value | f1040s8812 line 5; i1040gi p. 21 | Differences inherit its claimed (multiple support on a child). |
| claude | transcription | dependent.actc_amount | model error | 6,622/6,899 agree; 157 candidate-refuses, 20 candidate-unknown, 99 project-unknown, 1 value | f1040s8812 line 16b; i1040gi p. 21 | Differences inherit its claimed (multiple support on a child). |
| claude | transcription | dependent.odc_person | model error | 6,514/6,899 agree; 127 candidate-refuses, 153 candidate-unknown, 103 project-refuses, 2 project-unknown | i1040gi p. 19, Steps 4-5; p. 21 | No value differs now; refusals are its claimed multiple-support placement. |
| claude | transcription | dependent.odc_amount | model error | 6,514/6,899 agree; 127 candidate-refuses, 153 candidate-unknown, 103 project-refuses, 2 project-unknown | i1040gi p. 19, Steps 4-5; p. 21 | No value differs now; refusals are its claimed multiple-support placement. |
| claude | transcription | dependent.hoh_test2 | model error | 6,626/6,899 agree; 7 candidate-unknown, 111 project-refuses, 152 project-unknown, 3 value | i1040gi p. 14, Test 2; p501 p. 9 | No part-year route (3 completed fixtures). |
| claude | transcription | dependent.hoh_test1 | scope | 6,718/6,899 agree; 101 project-refuses, 80 project-unknown | i1040gi p. 14, Test 1; p501 p. 10, note 4 | Only project refusals (claimed_no_tin, multiple support) and tin-withheld partials differ. |
| claude | transcription | dependent.dc_qp | model error | 4,260/6,899 agree; 381 candidate-refuses, 902 candidate-unknown, 1 project-refuses, 4 project-unknown, 1,351 value | i2441 p. 1; p503 p. 3 | No death-year rule; care omission reaches no amount. |
| claude | transcription | dependent.ptc_magi_counted | representation | 6,166/6,899 agree; 385 candidate-refuses, 347 project-unknown, 1 value | i8962 p. 8, Line 2b | Line 2b sums only claimed dependents. |
| claude | transcription | 2(d) | model error | 5,932/6,899 agree; 385 candidate-refuses, 255 candidate-unknown, 274 project-unknown, 53 value | i2441 p. 3, Line 2; p503 p. 3 | Inherits dc_qp: $0.00 for the BUG-0157 parent ($4,000.00). |
| claude | transcription | 2(c) | model error | 6,083/6,899 agree; 381 candidate-refuses, 418 candidate-unknown, 1 project-refuses, 16 value | i2441 p. 3, Column (c); p503 p. 3 | Inherits dc_qp: unchecked for the BUG-0157 parent. |
| claude | transcription | 27 | model error | 3,166/6,899 agree; 2 candidate-refuses, 2 candidate-shows-skipped, 3,719 candidate-unknown, 10 project-refuses | i8863 p. 3, item 5 | No filer-TIN or f8863.paid test (generated 99 shows a skipped $4,000.00). |
| claude | transcription | 28 | model error | 3,166/6,899 agree; 2 candidate-refuses, 2 candidate-shows-skipped, 3,719 candidate-unknown, 10 project-refuses | i8863 p. 3, item 5 | As line 27. |
| claude | transcription | 29 | model error | 3,166/6,899 agree; 2 candidate-refuses, 2 candidate-shows-skipped, 3,719 candidate-unknown, 10 project-refuses | i8863 p. 3, item 5 | As line 27. |
| claude | transcription | 30 | model error | 3,166/6,899 agree; 2 candidate-refuses, 2 candidate-shows-skipped, 3,719 candidate-unknown, 10 project-refuses | i8863 p. 3, item 5 | As line 27. |
| claude | transcription | 31 | model error | 3,167/6,899 agree; 1 candidate-refuses, 3,719 candidate-unknown, 10 project-refuses, 2 value | i8863 p. 3, item 5 | Filer-TIN routing missing (generated 99: $0.00 against $12,706.94 and $5,509.61). |
| deepseek | transcription | dependent.claimed | scope | not executable (reply invalid) | i1040gi p. 19, Step 4; p. 22 | sibling_descendant fixed; only refusals (TIN, sa.dependent, multiple support) and an extra lawful question differ. |
| deepseek | transcription | dependent.ctc_child | model error | not executable (reply invalid) | i1040gi pp. 17-18, Step 3 | No filer SSN test. |
| deepseek | transcription | dependent.ctc_amount | model error | not executable (reply invalid) | i1040gi pp. 17-18, Step 3 | No filer SSN test. |
| deepseek | transcription | dependent.actc_amount | model error | not executable (reply invalid) | i1040gi pp. 17-18, Step 3 | No filer SSN test. |
| deepseek | transcription | dependent.odc_person | model error | not executable (reply invalid) | i1040gi p. 17; p. 19, Step 5 | No filer SSN/ITIN test. |
| deepseek | transcription | dependent.odc_amount | model error | not executable (reply invalid) | i1040gi p. 17; p. 19, Step 5 | No filer SSN/ITIN test. |
| deepseek | transcription | dependent.hoh_test2 | model error | not executable (reply invalid) | i1040gi p. 14, Test 2; p501 p. 9 | No part-year rule. |
| deepseek | transcription | dependent.hoh_test1 | scope | not executable (reply invalid) | i1040gi p. 14, Test 1; p501 p. 10 | Multiple-support exclusion is a refusal in the project. |
| deepseek | transcription | dependent.eic_child | scope | not executable (reply invalid) | i1040gi p. 41, Step 3; p. 44 | Equivalent test; extra divorced_rule refusal. |
| deepseek | transcription | dependent.eic_ssn_child | scope | not executable (reply invalid) | i1040gi p. 46, Worksheet A | As eic_child. |
| deepseek | transcription | dependent.dc_qp | model error | not executable (reply invalid) | i2441 p. 1; p503 p. 3 | Under-13 route has no qualifying-child test (new); no death-year rule. |
| deepseek | transcription | dependent.dc_count | model error | not executable (reply invalid) | i2441 p. 3, Line 2 | Declaration invalid (sum over the parent collection). |
| deepseek | transcription | 2(d) | model error | not executable (reply invalid) | i2441 p. 3, Line 2; p503 p. 3 | Inherits dc_qp for the BUG-0157 parent. |
| deepseek | transcription | 2(c) | model error | not executable (reply invalid) | i2441 p. 3, Column (c) | Box test now the project's; inherits dc_qp for the BUG-0157 parent. |
| deepseek | transcription | 27 | model error | not executable (reply invalid) | i8863 p. 3, item 5; p. 2 | Routed by lines 23-26 now, but no claimed, student TIN, filer TIN or f8863.paid test. |
| deepseek | transcription | 28 | model error | not executable (reply invalid) | i8863 p. 3; f8863 p. 2 | As line 27. |
| deepseek | transcription | 29 | model error | not executable (reply invalid) | i8863 p. 3; f8863 p. 2 | As line 27. |
| deepseek | transcription | 30 | model error | not executable (reply invalid) | i8863 p. 3; f8863 p. 2 | As line 27. |
| deepseek | transcription | 31 | model error | not executable (reply invalid) | f8863 p. 2; i8863 p. 3 | LLC amount without claimed/TIN tests; filer-without-TIN student gets $0.00. |
| claude | render | 2(d) | ambiguity | render MISMATCH | i2441 p. 3, Column (d) | Rejected reading (column (d) net of benefits), amb.2025.dc_line30. |
| claude | render | 23 | ambiguity | render MISMATCH | i8863 p. 1; p970 p. 2 | Form 1098-T request date, amb.2025.edu_1098t_date (Pub. 970 chosen); English says what the project asks. |
| claude | render | 27 | ambiguity | render MISMATCH | i8863 p. 1; p970 p. 2 | Form 1098-T request date, amb.2025.edu_1098t_date (Pub. 970 chosen); English says what the project asks. |
| claude | render | 28 | ambiguity | render MISMATCH | i8863 p. 1; p970 p. 2 | Form 1098-T request date, amb.2025.edu_1098t_date (Pub. 970 chosen); English says what the project asks. |
| claude | render | 29 | ambiguity | render MISMATCH | i8863 p. 1; p970 p. 2 | Form 1098-T request date, amb.2025.edu_1098t_date (Pub. 970 chosen); English says what the project asks. |
| claude | render | 30 | ambiguity | render MISMATCH | i8863 p. 1; p970 p. 2 | Form 1098-T request date, amb.2025.edu_1098t_date (Pub. 970 chosen); English says what the project asks. |
| claude | render | 31 | ambiguity | render MISMATCH | i8863 p. 1; p970 p. 2 | Form 1098-T request date, amb.2025.edu_1098t_date (Pub. 970 chosen); English says what the project asks. |
| deepseek | render | 2(d) | ambiguity | render MISMATCH | i2441 p. 3, Column (d) | Rejected reading (column (d) net of benefits), amb.2025.dc_line30. |
| deepseek | render | 23 | interface gap | render MISMATCH | p970 p. 11; i8863 p. 3 | ITIN/ATIN applied for by the due date and issued counts as issued; p970 not given. |
| deepseek | render | 27 | interface gap | render MISMATCH | p970 p. 11; i8863 p. 3 | ITIN/ATIN applied for by the due date and issued counts as issued; p970 not given. |
| deepseek | render | 28 | interface gap | render MISMATCH | p970 p. 11; i8863 p. 3 | ITIN/ATIN applied for by the due date and issued counts as issued; p970 not given. |
| deepseek | render | 29 | interface gap | render MISMATCH | p970 p. 11; i8863 p. 3 | ITIN/ATIN applied for by the due date and issued counts as issued; p970 not given. |
| deepseek | render | 30 | interface gap | render MISMATCH | p970 p. 11; i8863 p. 3 | ITIN/ATIN applied for by the due date and issued counts as issued; p970 not given. |
| deepseek | render | 31 | interface gap | render MISMATCH | p970 p. 11; i8863 p. 3 | ITIN/ATIN applied for by the due date and issued counts as issued; p970 not given. |
| claude | class M | classm.dependent.6 — dependent[dep_b].dc_line2d | representation (drop) | class M DISAGREE | i2441 p. 3, Line 2 | dc_paid supplied for a non-qualifying entry (the round-2 classm.dependent.8, renumbered). |
| deepseek | class M | classm.dependent.1 — dependent[dep_a].dc_line2c | model error (drop) | class M DISAGREE | i2441 p. 3, Column (c); p. 1 | f2441.care no: no care, no box. |
| deepseek | class M | classm.dependent.6 — dependent[dep_b].dc_line2d | representation (drop) | class M DISAGREE | i2441 p. 3, Line 2 | dc_paid supplied for a non-qualifying entry. |

Findings: none new. L1 (round 2) is fixed and verified by execution; both replies now read `sibling_descendant` as the project does.
No `round3/dependent.findings.md`.

## Completeness fixes (superseded subject)

Subject after BUG-0211 to BUG-0217, the fixes for the completeness-review experiment: the `child` gloss (adoption, an eligible
foster child's placement), the definitions in `student`, `disabled`, `work_ssn` and `supported`, the new screen
`dependent.kidnapped` refusing `lived_half` and `eic_child`, and the i8863 pages in the line 23 to 31 citations. No
arithmetic changed. Fresh replies of 2026-10-30; previous logs archived in `.transcription/archive/before-d-fixes-2026-10-30/`.
Full ruling text: `.transcription/proposed/dfix/transcription.dependent.json`, `transcription.dependent.deepseek.json`,
`render.dependent.json`, `render.dependent.deepseek.json`, `classm.dependent.json`, `classm.dependent.deepseek.json`.
Triage: `../triage/dependent.json` and `../triage/dependent.deepseek.json`, executable-triage-v2 (1,378 fixtures, 500
generated returns seed 20261026, 2,485 partial records; 7,441 comparisons per line). Both replies validate and execute this
round. Every completed-return difference was enumerated with the witness cap lifted (triage.mjs run directly, scratch only)
and assigned to a named cause; none is unexplained.

Two causes recur. First, both replies refuse `dependent.multiple_support` on every entry. That accounts for 83 completed-return
refusals per line, all on classm.s3.4 dep_a, a qualifying child. Second, some generated and class M records answer married no
with joint_return yes. Those answers contradict `dependent.married`, which asks "... or is this person filing a joint return".
Both replies test joint_return for a qualifying relative, where the project relies on the married screen, so the two sides
differ only on contradictory records. That kind is ruled representation.

The new wording introduces no difference in either reply. The deepseek reply reproduces the kidnapped refusal at
`dependent.claimed`. The Claude reply narrows it to a child who fails residency or support. The project's screen refuses
`stage21.d3.kidnapped_child_refused` (12 months), which the Claude reply computes: a broader cited screen (scope). The
render MISMATCH count rose from 7 to 11 (Claude). Lines 24 to 26 are new because their citations now include i8863 p. 8.
Line 2(c) is reviewer variance.

Counts. Claude transcription: model error 17, scope 1. Deepseek transcription: model error 15, scope 1, representation 1.
Render: Claude ambiguity 10 and interface gap 1; deepseek ambiguity 1. Class M: representation 1 per family (both dropped).

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | dependent.claimed | model error | 6,533/7,441 agree; completed returns: 83 candidate-refuses, 41 candidate-unknown, 11 value, 1 project-unknown | i1040gi p. 21, Multiple support agreements; p. 17, Step 1 | Refuses multiple_support on a qualifying child (83 completed, classm.s3.4 dep_a); 11 values are contradictory married/joint_return answers. |
| claude | transcription | dependent.ctc_child | model error | 7,054/7,441 agree; completed returns: 83 candidate-refuses, 18 candidate-unknown | i1040gi p. 18, Step 3; p. 21 | Step 3 tests are the project's; differences inherit its claimed. |
| claude | transcription | dependent.odc_person | model error | 6,614/7,441 agree; completed returns: 83 candidate-refuses, 39 candidate-unknown, 11 value | i1040gi p. 19, Step 5; p. 21 | Inherits its claimed; 11 contradictory records. |
| claude | transcription | dependent.ctc_amount | model error | 7,054/7,441 agree; completed returns: 83 candidate-refuses, 18 candidate-unknown | f1040s8812 line 5 | Inherited from ctc_child. |
| claude | transcription | dependent.odc_amount | model error | 6,614/7,441 agree; completed returns: 83 candidate-refuses, 39 candidate-unknown, 11 value | f1040s8812 line 7 | Inherited from odc_person. |
| claude | transcription | dependent.actc_amount | model error | 7,054/7,441 agree; completed returns: 83 candidate-refuses, 18 candidate-unknown | f1040s8812 line 16b | Inherited from ctc_child. |
| claude | transcription | dependent.hoh_test2 | model error | 6,699/7,441 agree; completed returns: 83 candidate-refuses, 35 candidate-unknown, 21 project-unknown, 9 value | p501 p. 9; i1040gi p. 14, Test 2 | No part-year route (3 completed fixtures). |
| claude | transcription | dependent.hoh_test1 | scope | 7,045/7,441 agree; completed returns: 20 project-unknown, 1 candidate-unknown | i1040gi p. 14, Test 1 | Only cited project refusals and question-order partials differ. |
| claude | transcription | dependent.dc_qp | model error | 4,589/7,441 agree; completed returns: 703 value, 83 candidate-refuses, 81 candidate-unknown | i2441 p. 1; p503 p. 3 | No death-year rule (stage15.f2441.parent_died_part_year); 702 care-omission values reach no amount. |
| claude | transcription | dependent.dc_count | model error | 1,914/7,441 agree; completed returns: 1,328 value, 83 candidate-refuses, 81 candidate-unknown | i2441 p. 3, Line 2; p503 p. 3 | Inherits dc_qp; 1,327 values are entries f2441.qp_count never sums. |
| claude | transcription | dependent.ptc_magi_counted | model error | 6,470/7,441 agree; completed returns: 83 candidate-refuses, 16 project-unknown, 1 value | i8962 p. 8, Line 2b | Inherits claimed's refusal; its own formula is representation (line 2b sums dependents only). |
| claude | transcription | 2(d) | model error | 6,283/7,441 agree; completed returns: 83 candidate-refuses, 42 candidate-unknown, 29 project-unknown, 1 value | i2441 p. 3, Line 2; p503 p. 3 | Inherits dc_qp ($4,000.00 against $0.00). |
| claude | transcription | 2(c) | model error | 6,544/7,441 agree; completed returns: 83 candidate-refuses, 36 candidate-unknown, 1 value | i2441 p. 3, Column (c); p503 p. 3 | Inherits dc_qp (box unchecked for the parent). |
| claude | transcription | 27 | model error | 3,937/7,441 agree; completed returns: 1,097 candidate-unknown, 83 candidate-refuses, 1 value | i8863 p. 2; p. 3, item 5 | No f8863.paid test: asks dependent.edu on 1,068 completed records; filer TIN now applied. |
| claude | transcription | 28 | model error | 3,937/7,441 agree; completed returns: 1,097 candidate-unknown, 83 candidate-refuses, 1 value | i8863 p. 2; p. 3, item 5 | As line 27. |
| claude | transcription | 29 | model error | 3,937/7,441 agree; completed returns: 1,097 candidate-unknown, 83 candidate-refuses, 1 value | i8863 p. 2; p. 3, item 5 | As line 27. |
| claude | transcription | 30 | model error | 3,937/7,441 agree; completed returns: 1,097 candidate-unknown, 83 candidate-refuses, 1 value | i8863 p. 2; p. 3, item 5 | As line 27. |
| claude | transcription | 31 | model error | 3,936/7,441 agree; completed returns: 1,097 candidate-unknown, 83 candidate-refuses | i8863 p. 2; p. 9, Line 31 | As line 27 (no value differs). |
| deepseek | transcription | dependent.claimed | model error | 6,480/7,441 agree; completed returns: 83 candidate-refuses, 48 candidate-unknown, 14 value, 7 project-unknown | i1040gi p. 21; p. 17, Step 1 | Refuses multiple_support on a qualifying child (83 completed, classm.s3.4 dep_a); household_member months < 12 records are contradictory. |
| deepseek | transcription | dependent.ctc_child | model error | 4,959/7,441 agree; completed returns: 889 value, 83 candidate-refuses, 72 candidate-unknown | i1040gi p. 18, Step 3 | No qualifying-child test: 889 qualifying relatives or failed children get the credit (new). |
| deepseek | transcription | dependent.odc_person | model error | 4,754/7,441 agree; completed returns: 901 value, 83 candidate-refuses, 77 candidate-unknown | i1040gi p. 18, Step 3 q. 3; p. 19, Step 5 | Inherits its ctc_child (890 values). |
| deepseek | transcription | dependent.ctc_amount | model error | 4,959/7,441 agree; completed returns: 889 value, 83 candidate-refuses, 72 candidate-unknown | f1040s8812 line 5 | Inherited ($2,200.00 against $0.00). |
| deepseek | transcription | dependent.odc_amount | model error | 4,754/7,441 agree; completed returns: 901 value, 83 candidate-refuses, 77 candidate-unknown | f1040s8812 line 7 | Inherited. |
| deepseek | transcription | dependent.actc_amount | model error | 4,959/7,441 agree; completed returns: 889 value, 83 candidate-refuses, 72 candidate-unknown | f1040s8812 line 16b | Inherited. |
| deepseek | transcription | dependent.hoh_test2 | model error | 5,284/7,441 agree; completed returns: 128 value, 83 candidate-refuses, 37 candidate-unknown, 18 project-unknown | p501 p. 9; i1040gi p. 14, Test 2 | No part-year rule; its home_cost conjunct is representation. |
| deepseek | transcription | dependent.hoh_test1 | scope | 7,034/7,441 agree; completed returns: 20 project-unknown, 1 candidate-unknown | i1040gi p. 14, Test 1 | Only cited project refusals and partials differ. |
| deepseek | transcription | dependent.dc_qp | model error | 4,426/7,441 agree; completed returns: 722 value, 83 candidate-refuses, 82 candidate-unknown | i2441 p. 1; p503 p. 3 | No death-year rule; care omission reaches no amount. |
| deepseek | transcription | dependent.ptc_magi_counted | representation | 7,441/7,441 agree | i8962 p. 8, Line 2b | Same choice on ptc_files. |
| deepseek | transcription | 2(d) | model error | 6,279/7,441 agree; completed returns: 83 candidate-refuses, 43 candidate-unknown, 29 project-unknown, 1 value | i2441 p. 3, Line 2; p503 p. 3 | Inherits dc_qp. |
| deepseek | transcription | 2(c) | model error | 6,534/7,441 agree; completed returns: 83 candidate-refuses, 50 candidate-unknown, 1 value | i2441 p. 3, Column (c); p503 p. 3 | Inherits dc_qp. |
| deepseek | transcription | 27 | model error | 3,569/7,441 agree; completed returns: 1,142 candidate-unknown, 3 candidate-shows-skipped | i8863 p. 2; p. 3, item 5 | Shows skipped amounts for non-dependents (3 completed); needs edu_over everywhere. |
| deepseek | transcription | 28 | model error | 3,569/7,441 agree; completed returns: 1,142 candidate-unknown, 3 candidate-shows-skipped | i8863 p. 2; p. 3, item 5 | As line 27. |
| deepseek | transcription | 29 | model error | 3,569/7,441 agree; completed returns: 1,142 candidate-unknown, 3 candidate-shows-skipped | i8863 p. 2; p. 3, item 5 | As line 27. |
| deepseek | transcription | 30 | model error | 3,569/7,441 agree; completed returns: 1,142 candidate-unknown, 3 candidate-shows-skipped | i8863 p. 2; p. 3, item 5 | As line 27. |
| deepseek | transcription | 31 | model error | 3,548/7,441 agree; completed returns: 1,142 candidate-unknown | i8863 p. 2; p. 9 | Needs edu_over everywhere; no dependent test by reading. |
| claude | render | 2(d) | ambiguity | render MISMATCH | amb.2025.dc_line30; i2441 p. 3, Column (d) | Rejected reading (column (d) net of benefits). |
| claude | render | 2(c) | interface gap | render MISMATCH | i2441 p. 1, item 3 | Nondependent qualifying persons are refused by f2441.nondependent_gate, outside the dependent render. |
| claude | render | 23 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | 1098-T date is amb.2025.edu_1098t_date; TIN applied-for wording allowed by p970 p. 11 (interface gap). |
| claude | render | 24 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | 1098-T date is amb.2025.edu_1098t_date; TIN applied-for wording allowed by p970 p. 11 (interface gap). |
| claude | render | 25 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | 1098-T date is amb.2025.edu_1098t_date; TIN applied-for wording allowed by p970 p. 11 (interface gap). |
| claude | render | 26 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | 1098-T date is amb.2025.edu_1098t_date; TIN applied-for wording allowed by p970 p. 11 (interface gap). |
| claude | render | 27 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | 1098-T date is amb.2025.edu_1098t_date; TIN applied-for wording allowed by p970 p. 11 (interface gap). |
| claude | render | 28 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | 1098-T date is amb.2025.edu_1098t_date; TIN applied-for wording allowed by p970 p. 11 (interface gap). |
| claude | render | 29 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | 1098-T date is amb.2025.edu_1098t_date; TIN applied-for wording allowed by p970 p. 11 (interface gap). |
| claude | render | 30 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | 1098-T date is amb.2025.edu_1098t_date; TIN applied-for wording allowed by p970 p. 11 (interface gap). |
| claude | render | 31 | ambiguity | render MISMATCH | i8863 p. 1; p970 pp. 2, 11 | 1098-T date is amb.2025.edu_1098t_date; TIN applied-for wording allowed by p970 p. 11 (interface gap). |
| deepseek | render | 2(d) | ambiguity | render MISMATCH | amb.2025.dc_line30 | Rejected reading. |
| claude | class M | classm.dependent.5 — dependent[dep_b].dc_line2d | representation (drop) | class M DISAGREE | i2441 p. 3, Line 2 | dc_paid shown for a non-qualifying entry; not summed (Stage 19 round 3 classm.dependent.6, renumbered). |
| deepseek | class M | classm.dependent.5 — dependent[dep_b].dc_line2d | representation (drop) | class M DISAGREE | i2441 p. 3, Line 2 | Same. |

Findings: Q1 (low, new), in `.transcription/proposed/dfix/dependent.findings.md`. The `child` gloss's sentence "a child in
your care without such a placement is entered as household_member or other" can be read to send a related child (a grandchild,
niece or nephew) without an agency placement off the qualifying-child path. Suggested wording: "a child who is not otherwise
your relative". The same file lists what was checked: the other glosses, the kidnapped screen's breadth and the i8863 page
cites.

## Fix round 2 (superseded subject)

Subject after the fix-round-2 wording (BUG-0221 to BUG-0229, BUG-0234 `kidnapped` reworded to "at any time during 2025 ...
even if since returned", BUG-0250 `child` gloss). No expression changed. Fresh replies of 2026-10-30; previous logs archived in
`.transcription/archive/before-fix-round2-2026-10-30/`. Full ruling text: `.transcription/proposed/fixr2/transcription.dependent.json`,
`transcription.dependent.deepseek.json`, `render.dependent.json`, `render.dependent.deepseek.json`; findings in
`.transcription/proposed/fixr2/dependent.findings.md`. Triage `../triage/dependent.json`, executable-triage-v2 (1,382 fixtures,
500 generated returns seed 20261026, 2,487 partial records; 7,447 comparisons per line). The Claude reply validates. Every
completed-return difference was enumerated with the witness cap lifted (triage.mjs run directly, scratch only) and assigned
to a named cause; none is unexplained. The deepseek reply is invalid: bare line references sit inside test lists in claimed,
hoh_test2, eic_child, dc_qp and five helpers. `../triage/dependent.deepseek.json` executed nothing, so its lines are ruled on
validation, or on the merits by reading. Class M dependent has no open section.

The Claude reply now carries the part-year rule for head of household Test 2 and the death-year rule for Form 2441. The
previous round's part-year and death-year model errors no longer differ. Its multiple-support refusal on a qualifying child
(classm.s3.4 dep_a, 83 completed returns per line) remains. That refusal is now also declared on hoh_test1, so that line
moves from scope to model error. eic_child and eic_ssn_child are new to the open list (scope). Their only differences are
refusals and partials. The wording fixes produce no completed-return difference.

The project's `dependent.kidnapped` screen refuses `lived_half` and `eic_child` whenever the answer is yes. After BUG-0234,
that includes a child who was returned and lived with you for most of the year, and a household-member child. Those returns
are refused, while the source computes them without the kidnapped rule. That is finding F1 (low).

Counts:
- Claude transcription: model error 18, scope 2.
- Deepseek transcription: model error 18.
- Claude render: ambiguity 10, interface gap 1.
- Deepseek render: ambiguity 1.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | dependent.claimed | model error | 6,677/7,447 agree; completed returns: 83 candidate-refuses, 23 candidate-unknown, 1 project-unknown | i1040gi p. 21, Multiple support agreements; p. 17, Step 1 | Refuses multiple_support on a qualifying child (83 completed, classm.s3.4 dep_a); 3 lawful fixtures, 21 partials. |
| claude | transcription | dependent.ctc_child | model error | 7,060/7,447 agree; completed returns: 83 candidate-refuses, 18 candidate-unknown | i1040gi p. 18, Step 3; p. 21 | Step 3 tests are the project's; inherits its claimed. |
| claude | transcription | dependent.odc_person | model error | 6,754/7,447 agree; completed returns: 83 candidate-refuses, 21 candidate-unknown | i1040gi p. 19, Step 5; p. 21 | Inherits its claimed. |
| claude | transcription | dependent.ctc_amount | model error | 7,060/7,447 agree; completed returns: 83 candidate-refuses, 18 candidate-unknown | f1040s8812 line 5 | Inherited from ctc_child. |
| claude | transcription | dependent.odc_amount | model error | 6,754/7,447 agree; completed returns: 83 candidate-refuses, 21 candidate-unknown | f1040s8812 line 7 | Inherited from odc_person. |
| claude | transcription | dependent.actc_amount | model error | 7,060/7,447 agree; completed returns: 83 candidate-refuses, 18 candidate-unknown | f1040s8812 line 16b | Inherited from ctc_child. |
| claude | transcription | dependent.hoh_test2 | model error | 6,874/7,447 agree; completed returns: 83 candidate-refuses, 20 candidate-unknown, 9 project-unknown | i1040gi p. 21; p. 14, Test 2; p501 p. 9 | Part-year route now present (no value differs); multiple-support refusal remains. |
| claude | transcription | dependent.hoh_test1 | model error | 6,899/7,447 agree; completed returns: 83 candidate-refuses, 19 candidate-unknown, 19 project-unknown | i1040gi p. 14, Test 1 | Declares the multiple-support refusal on Test 1 itself, firing for a child (83 completed); scope last round. |
| claude | transcription | dependent.eic_child | scope | 7,138/7,447 agree; completed returns: 12 project-unknown, 3 candidate-unknown | i1040gi p. 41, Step 3; p501 p. 13 | Only refusals and partials differ; reply narrows the kidnapped gate (stage21.d3 refused by the project, F1) and adds a divorced_rule refusal on refused returns. |
| claude | transcription | dependent.eic_ssn_child | scope | 7,142/7,447 agree; completed returns: 10 project-unknown, 2 candidate-unknown | i1040gi p. 46, line 2 | Inherits eic_child. |
| claude | transcription | dependent.dc_qp | model error | 4,483/7,447 agree; completed returns: 702 value, 84 candidate-unknown, 83 candidate-refuses | i2441 p. 1; p503 p. 3 | Death-year rule now present; 702 care-omission values reach no amount; no-care asks (29). |
| claude | transcription | dependent.dc_count | model error | 1,919/7,447 agree; completed returns: 1,325 value, 84 candidate-unknown, 83 candidate-refuses | i2441 p. 3, Line 2 | 1,325 values are entries f2441.qp_count never sums; inherits dc_qp. |
| claude | transcription | dependent.ptc_magi_counted | model error | 6,625/7,447 agree; completed returns: 83 candidate-refuses, 15 project-unknown, 1 value | i8962 p. 8, Line 2b | Inherits claimed's refusal; own formula representation. |
| claude | transcription | 2(d) | model error | 6,079/7,447 agree; completed returns: 236 project-unknown, 6 candidate-unknown | i2441 p. 3, Line 2 | 236 project-unknown dc_paid with care no (representation); 6 multiple-support partials. |
| claude | transcription | 2(c) | model error | 6,420/7,447 agree; completed returns: 83 candidate-refuses, 48 candidate-unknown, 4 value | i2441 p. 3, Column (c) | Multiple support; 4 care-omission boxes reach no amount. |
| claude | transcription | 27 | model error | 3,639/7,447 agree; completed returns: 1,124 candidate-unknown, 1 candidate-refuses | i8863 p. 2; p. 3, item 5 | No f8863.paid test: asks dependent.edu on 1,124 completed records. |
| claude | transcription | 28 | model error | 3,639/7,447 agree; completed returns: 1,124 candidate-unknown, 1 candidate-refuses | i8863 p. 2; p. 3, item 5 | As line 27. |
| claude | transcription | 29 | model error | 3,639/7,447 agree; completed returns: 1,124 candidate-unknown, 1 candidate-refuses | i8863 p. 2; p. 3, item 5 | As line 27. |
| claude | transcription | 30 | model error | 3,639/7,447 agree; completed returns: 1,124 candidate-unknown, 1 candidate-refuses | i8863 p. 2; p. 3, item 5 | As line 27. |
| claude | transcription | 31 | model error | 3,637/7,447 agree; completed returns: 1,124 candidate-unknown, 1 candidate-refuses | i8863 p. 2; p. 9, Line 31 | As line 27. |
| deepseek | transcription | dependent.claimed | model error | not executable (reply invalid) | README (validation); i1040gi p. 21 | Malformed expression; by reading multiple support refused at every entry. |
| deepseek | transcription | dependent.ctc_child | model error | not executable (reply invalid) | i1040gi p. 18, Step 3 | Invalid dependency; no qualifying-child test (qualifying relatives get the CTC). |
| deepseek | transcription | dependent.odc_person | model error | not executable (reply invalid) | i1040gi p. 19, Step 5 q. 1 | Invalid dependency; omits household.all_tin. |
| deepseek | transcription | dependent.ctc_amount | model error | not executable (reply invalid) | f1040s8812 line 5 | Inherited. |
| deepseek | transcription | dependent.odc_amount | model error | not executable (reply invalid) | f1040s8812 line 7 | Inherited. |
| deepseek | transcription | dependent.actc_amount | model error | not executable (reply invalid) | f1040s8812 line 16b | Inherited. |
| deepseek | transcription | dependent.hoh_test2 | model error | not executable (reply invalid) | p501 p. 9; i1040gi p. 14, Test 2 | Malformed; no part-year route; claimed niece fails Test 2. |
| deepseek | transcription | dependent.hoh_test1 | model error | not executable (reply invalid) | README (validation); i1040gi p. 14 | Invalid dependency; Test 1 itself is the project's. |
| deepseek | transcription | dependent.eic_child | model error | not executable (reply invalid) | README (validation); i1040gi pp. 41, 44 | Malformed; by reading the project's test, married-child branch is a scope difference. |
| deepseek | transcription | dependent.eic_ssn_child | model error | not executable (reply invalid) | README (validation) | Invalid dependency. |
| deepseek | transcription | dependent.dc_qp | model error | not executable (reply invalid) | i2441 p. 1; p503 p. 3 | Malformed; under-13 route by answer alone for any dependent; no death-year rule. |
| deepseek | transcription | 2(d) | model error | not executable (reply invalid) | README (validation); i2441 p. 3 | Invalid dependency on dc_qp. |
| deepseek | transcription | 2(c) | model error | not executable (reply invalid) | i2441 p. 3, Column (c) | No qualifying-person test: box for any disabled entry. |
| deepseek | transcription | 27 | model error | not executable (reply invalid) | i8863 p. 2; p. 3, item 5 | No dependent, filer-TIN or f8863.paid test (by reading). |
| deepseek | transcription | 28 | model error | not executable (reply invalid) | i8863 p. 2; p. 3, item 5 | As line 27. |
| deepseek | transcription | 29 | model error | not executable (reply invalid) | i8863 p. 2; p. 3, item 5 | As line 27. |
| deepseek | transcription | 30 | model error | not executable (reply invalid) | i8863 p. 2; p. 3, item 5 | As line 27. |
| deepseek | transcription | 31 | model error | not executable (reply invalid) | i8863 p. 2; p. 9 | As line 27. |
| claude | render | 2(d) | ambiguity | render MISMATCH | amb.2025.dc_line30; i2441 p. 3, Column (d) | Rejected reading (column (d) net of benefits); BUG-0224 exclusions unobjected. |
| claude | render | 2(c) | interface gap | render MISMATCH | i2441 p. 1, item 3 | Nondependent qualifying persons are refused by f2441.nondependent_gate, outside the dependent render. |
| claude | render | 23 | ambiguity | render MISMATCH | i8863 p. 1; p970 p. 2 | 1098-T request date (amb.2025.edu_1098t_date); line text matches; no TIN objection this round. |
| claude | render | 24 | ambiguity | render MISMATCH | i8863 p. 1; p970 p. 2 | 1098-T request date (amb.2025.edu_1098t_date); line text matches; no TIN objection this round. |
| claude | render | 25 | ambiguity | render MISMATCH | i8863 p. 1; p970 p. 2 | 1098-T request date (amb.2025.edu_1098t_date); line text matches; no TIN objection this round. |
| claude | render | 26 | ambiguity | render MISMATCH | i8863 p. 1; p970 p. 2 | 1098-T request date (amb.2025.edu_1098t_date); line text matches; no TIN objection this round. |
| claude | render | 27 | ambiguity | render MISMATCH | i8863 p. 1; p970 p. 2 | 1098-T request date (amb.2025.edu_1098t_date); line text matches; no TIN objection this round. |
| claude | render | 28 | ambiguity | render MISMATCH | i8863 p. 1; p970 p. 2 | 1098-T request date (amb.2025.edu_1098t_date); line text matches; no TIN objection this round. |
| claude | render | 29 | ambiguity | render MISMATCH | i8863 p. 1; p970 p. 2 | 1098-T request date (amb.2025.edu_1098t_date); line text matches; no TIN objection this round. |
| claude | render | 30 | ambiguity | render MISMATCH | i8863 p. 1; p970 p. 2 | 1098-T request date (amb.2025.edu_1098t_date); line text matches; no TIN objection this round. |
| claude | render | 31 | ambiguity | render MISMATCH | i8863 p. 1; p970 p. 2 | 1098-T request date (amb.2025.edu_1098t_date); line text matches; no TIN objection this round. |
| deepseek | render | 2(d) | ambiguity | render MISMATCH | amb.2025.dc_line30 | Rejected reading. |

Findings: F1 (low), in `.transcription/proposed/fixr2/dependent.findings.md`. The kidnapped screen's refusals on `lived_half`
and `eic_child` are unconditional. Witness: stage9.eic.one_child.line5 with 11 months; kidnapped no gives line 27a $3,261.00,
and kidnapped yes refuses it. The proposed fix gates the refusals on months under 7, or on a qualifying-child relationship with
us_half no. The same file lists what was checked: `eic.died_2025`, BUG-0221 to BUG-0229, and the uncertain "renewal applied
for" in BUG-0225.

## Fix round 3 (superseded subject)

Subject after BUG-0252 (`self_support` and `supported` gain the scholarship, state-support and related p501 support rules)
and BUG-0253 (`gross_income` gains the p501 p. 19 definition). No expression changed. Fresh replies of 2026-10-30; previous
logs archived in `.transcription/archive/before-fix-round3-2026-10-30/`. Full ruling text: `.transcription/proposed/fixr3/`
(`transcription.dependent.json`, `transcription.dependent.deepseek.json`, `render.dependent.json`,
`render.dependent.deepseek.json`); findings and low observations in `.transcription/proposed/fixr3/dependent.findings.md`.
Triage `../triage/dependent.json`, executable-triage-v2 (1,390 fixtures, 500 generated returns seed 20261026, 2,487 partial records;
7,463 comparisons per line), built after the concurrent engine change (spec 4.7.5) and reproduced exactly by an uncapped rerun.
The Claude reply validates. Every completed-return difference was enumerated with the witness cap lifted (triage.mjs run
directly, scratch only) and assigned to a named cause; none is unexplained. The deepseek reply is invalid
(`dependent.h_edu_aqee31` references an aqee line31; `dependent.dc_count` has a collection parent binding mismatch), so
`../triage/dependent.deepseek.json` executed nothing and its lines are ruled on validation, or on the merits by reading.
Class M dependent has no open section. eic_child and eic_ssn_child now agree in both families; deepseek 2(d) agrees.

The rewording produces no completed-return difference, and checked against p501 pp. 15, 19 to 21 it introduces no error
of medium severity. One low reading risk is recorded for T-092: the `supported` sentence on state benefits to "a needy
person". The Claude reply now refuses kidnapped as the project does, so fix-round-2 F1 has no witness here. Compared with
its round-2 reply, the Claude reply regressed in two places:
- it dropped the Form 2441 death-year route (p503 p. 3). On `stage15.f2441.parent_died_part_year`, its line 11 is $0.00
  against the project's $600.00.
- it dropped the filer-TIN test of the American opportunity credit (i8863 p. 3, item 5). No sampled record has that
  combination. A constructed witness, `stage19.example.jack_kay` with the spouse's TIN set to no, gives line 30 $2,500.00
  where the project gives line 31 $4,300.00.

Both are model errors. Its multiple-support refusal on a qualifying child (83 completed returns per line) remains. The
deepseek reply fixed its round-2 ctc_child, odc_person and 2(c) gaps but reads the taxpayer's work SSN alone for the child
tax credit. It still treats sibling_descendant as a relative who need not live with you.

Counts:
- Claude transcription: model error 18.
- Deepseek transcription: model error 16, representation 1.
- Claude render: ambiguity 10, interface gap 1.
- Deepseek render: ambiguity 1, model error 1.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | dependent.claimed | model error | 6,693/7,463 agree; completed returns: 83 candidate-refuses, 24 candidate-unknown | i1040gi p. 21, Multiple support agreements; p. 17, Step 1 | Refuses multiple_support on a qualifying child (83 completed, classm.s3.4 dep_a); 3 lawful fixtures, 21 partials. |
| claude | transcription | dependent.ctc_child | model error | 7,075/7,463 agree; completed returns: 83 candidate-refuses, 18 candidate-unknown | i1040gi p. 18, Step 3; p. 21 | Step 3 tests are the project's; inherits its claimed. |
| claude | transcription | dependent.odc_person | model error | 6,772/7,463 agree; completed returns: 83 candidate-refuses, 22 candidate-unknown | i1040gi p. 19, Step 5; p. 21 | Inherits its claimed. |
| claude | transcription | dependent.ctc_amount | model error | 7,075/7,463 agree; completed returns: 83 candidate-refuses, 18 candidate-unknown | f1040s8812 line 5 | Inherited from ctc_child. |
| claude | transcription | dependent.odc_amount | model error | 6,772/7,463 agree; completed returns: 83 candidate-refuses, 22 candidate-unknown | f1040s8812 line 7 | Inherited from odc_person. |
| claude | transcription | dependent.actc_amount | model error | 7,075/7,463 agree; completed returns: 83 candidate-refuses, 18 candidate-unknown | f1040s8812 line 16b | Inherited from ctc_child. |
| claude | transcription | dependent.hoh_test2 | model error | 6,880/7,463 agree; completed returns: 83 candidate-refuses, 21 candidate-unknown | i1040gi p. 21; p. 14, Test 2; p501 p. 9 | Part-year route kept (no value differs); multiple-support refusal remains. |
| claude | transcription | dependent.hoh_test1 | model error | 6,903/7,463 agree; completed returns: 83 candidate-refuses, 20 candidate-unknown, 9 project-unknown | i1040gi p. 14, Test 1 | Multiple-support refusal declared on Test 1 itself, firing for a child (83 completed). |
| claude | transcription | dependent.dc_qp | model error | 4,595/7,463 agree; completed returns: 684 value, 83 candidate-refuses, 73 candidate-unknown | i2441 p. 1; p503 p. 3 | Death-year route dropped again: stage15.f2441.parent_died_part_year line 11 $0.00 against $600.00; 683 care-omission values reach no amount. |
| claude | transcription | dependent.dc_count | model error | 1,924/7,463 agree; completed returns: 1,315 value, 83 candidate-refuses, 73 candidate-unknown | i2441 p. 3, Line 2; p503 p. 3 | 1,314 values are entries f2441.qp_count never sums; 1 is the death-year error. |
| claude | transcription | dependent.ptc_magi_counted | model error | 6,644/7,463 agree; completed returns: 83 candidate-refuses, 15 project-unknown, 1 value | i8962 p. 8, Line 2b | Inherits claimed's refusal; own formula representation. |
| claude | transcription | 2(d) | model error | 6,306/7,463 agree; completed returns: 83 candidate-refuses, 33 candidate-unknown, 29 project-unknown, 1 value | i2441 p. 3, Line 2; p503 p. 3 | Death-year witness $4,000.00 against $0.00; 29 project-unknown dc_paid with care no (representation). |
| claude | transcription | 2(c) | model error | 6,528/7,463 agree; completed returns: 83 candidate-refuses, 47 candidate-unknown, 5 value | i2441 p. 3, Column (c); p503 p. 3 | Death-year witness box; 4 care-omission boxes reach no amount. |
| claude | transcription | 27 | model error | 3,871/7,463 agree; completed returns: 1,076 candidate-unknown, 83 candidate-refuses | i8863 p. 2; p. 3, item 5 | No filer-TIN test (constructed jack_kay witness: line 30 $2,500.00 where the project goes to line 31) and no f8863.paid test (1,059 asks). |
| claude | transcription | 28 | model error | 3,871/7,463 agree; completed returns: 1,076 candidate-unknown, 83 candidate-refuses | i8863 p. 2; p. 3, item 5 | As line 27. |
| claude | transcription | 29 | model error | 3,871/7,463 agree; completed returns: 1,076 candidate-unknown, 83 candidate-refuses | i8863 p. 2; p. 3, item 5 | As line 27. |
| claude | transcription | 30 | model error | 3,871/7,463 agree; completed returns: 1,076 candidate-unknown, 83 candidate-refuses | i8863 p. 2; p. 3, item 5 | As line 27. |
| claude | transcription | 31 | model error | 3,869/7,463 agree; completed returns: 1,076 candidate-unknown, 83 candidate-refuses | i8863 p. 2; p. 3, item 5; p. 9 | As line 27 (line 31 $0.00 where the project gives $4,300.00). |
| deepseek | transcription | dependent.claimed | model error | not executable (reply invalid) | i1040gi p. 19, Step 4 | Counts sibling_descendant as a relative who need not live with you. |
| deepseek | transcription | dependent.ctc_child | model error | not executable (reply invalid) | i1040gi p. 18, Step 3 q. 4 | Reads household.taxpayer_work_ssn: no CTC where only the spouse has a work SSN. |
| deepseek | transcription | dependent.odc_person | model error | not executable (reply invalid) | i1040gi p. 19, Steps 4-5 | Filer-TIN test now present; inherits claimed and ctc_child. |
| deepseek | transcription | dependent.ctc_amount | model error | not executable (reply invalid) | f1040s8812 line 5 | Inherited. |
| deepseek | transcription | dependent.odc_amount | model error | not executable (reply invalid) | f1040s8812 line 7 | Inherited. |
| deepseek | transcription | dependent.actc_amount | model error | not executable (reply invalid) | f1040s8812 line 16b | Inherited. |
| deepseek | transcription | dependent.hoh_test2 | model error | not executable (reply invalid) | i1040gi p. 14, Test 2; p501 p. 9 | part_year_home in place of months; multiple-support refusal on the line; inherits claimed. |
| deepseek | transcription | dependent.hoh_test1 | model error | not executable (reply invalid) | i1040gi p. 14, Test 1 | Multiple-support refusal declared on the line, firing for any entry. |
| deepseek | transcription | dependent.dc_qp | model error | not executable (reply invalid) | i2441 p. 1; p503 p. 3 | No death-year route; asks dc_under13 at 14 or over. |
| deepseek | transcription | dependent.dc_count | model error | not executable (reply invalid) | README (validation); i2441 p. 3 | Collection parent binding mismatch. |
| deepseek | transcription | dependent.ptc_magi_counted | representation | not executable (reply invalid) | i8962 p. 8, Line 2b | Same choose on ptc_files; zero spelled as $0.00 minus $0.00. |
| deepseek | transcription | 2(c) | model error | not executable (reply invalid) | i2441 p. 3, Column (c); p503 p. 3 | Box test is the project's; inherits dc_qp's death-year error. |
| deepseek | transcription | 27 | model error | not executable (reply invalid) | i8863 p. 2; p. 3, item 5 | No dependent, filer-TIN or f8863.paid test. |
| deepseek | transcription | 28 | model error | not executable (reply invalid) | i8863 p. 2; p. 3, item 5 | As line 27. |
| deepseek | transcription | 29 | model error | not executable (reply invalid) | i8863 p. 2; p. 3, item 5 | As line 27. |
| deepseek | transcription | 30 | model error | not executable (reply invalid) | i8863 p. 2; p. 3, item 5 | As line 27. |
| deepseek | transcription | 31 | model error | not executable (reply invalid) | README (validation); i8863 p. 9 | Invalid reference (aqee line31); no dependent or f8863.paid test. |
| claude | render | 2(d) | ambiguity | render MISMATCH | amb.2025.dc_line30; i2441 p. 3, Column (d) | Rejected reading (column (d) net of benefits). |
| claude | render | 2(c) | interface gap | render MISMATCH | i2441 p. 1, item 3 | Nondependent qualifying persons are refused by f2441.nondependent_gate, outside the dependent render. |
| claude | render | 23 | ambiguity | render MISMATCH | i8863 p. 1; p970 p. 2 | 1098-T request date (amb.2025.edu_1098t_date); line text matches. |
| claude | render | 24 | ambiguity | render MISMATCH | i8863 p. 1; p970 p. 2 | 1098-T request date (amb.2025.edu_1098t_date); line text matches. |
| claude | render | 25 | ambiguity | render MISMATCH | i8863 p. 1; p970 p. 2 | 1098-T request date (amb.2025.edu_1098t_date); line text matches. |
| claude | render | 26 | ambiguity | render MISMATCH | i8863 p. 1; p970 p. 2 | 1098-T request date (amb.2025.edu_1098t_date); line text matches. |
| claude | render | 27 | ambiguity | render MISMATCH | i8863 p. 1, p. 3; p970 pp. 2, 11 | 1098-T request date (amb.2025.edu_1098t_date); the TIN-applied-for objection is p970 p. 11, not given (interface gap). |
| claude | render | 28 | ambiguity | render MISMATCH | i8863 p. 1, p. 3; p970 pp. 2, 11 | 1098-T request date (amb.2025.edu_1098t_date); the TIN-applied-for objection is p970 p. 11, not given (interface gap). |
| claude | render | 29 | ambiguity | render MISMATCH | i8863 p. 1, p. 3; p970 pp. 2, 11 | 1098-T request date (amb.2025.edu_1098t_date); the TIN-applied-for objection is p970 p. 11, not given (interface gap). |
| claude | render | 30 | ambiguity | render MISMATCH | i8863 p. 1, p. 3; p970 pp. 2, 11 | 1098-T request date (amb.2025.edu_1098t_date); the TIN-applied-for objection is p970 p. 11, not given (interface gap). |
| claude | render | 31 | ambiguity | render MISMATCH | i8863 p. 1, p. 3; p970 pp. 2, 11 | 1098-T request date (amb.2025.edu_1098t_date); the TIN-applied-for objection is p970 p. 11, not given (interface gap). |
| deepseek | render | 2(d) | ambiguity | render MISMATCH | amb.2025.dc_line30 | Rejected reading. |
| deepseek | render | 2(c) | model error | render MISMATCH | i2441 p. 3, Column (c); dependent.dc_paid | Included care is care while a qualifying person; over 13 at year end means over 12 throughout. |

Findings: none of medium or higher severity. Low L1 (for T-092) in `.transcription/proposed/fixr3/dependent.findings.md`:
`dependent.supported` should say that state benefits are the state's support when the state provides them to this person
as a needy person. As now worded, a filer may apply the sentence to their own benefits, against p501 p. 20's TANF rule.

## Fix round 4

Subject after BUG-0258 (`parent_home_paid` gains the p501 p. 9 definition of the cost of keeping up a home and the
parent's own-funds rule), with the BUG-0257 engine change in place. No expression changed. Fresh replies of 2026-10-30.
Full ruling text: `.transcription/proposed/fixr4/` (`transcription.dependent.json`, `transcription.dependent.deepseek.json`,
`render.dependent.json`, `render.dependent.deepseek.json`); findings and low observations in
`.transcription/proposed/fixr4/dependent.findings.md`. Triage `../triage/dependent.json`, executable-triage-v2 (1,390
fixtures, 500 generated returns seed 20261026, 2,487 partial records; 7,463 comparisons per line), built after the engine
rebuild and reproduced exactly by an uncapped rerun (scratch `/tmp/adj-fixr2-dependent-household/`). The Claude reply
validates; every completed-return difference was assigned to a named cause, none unexplained. The deepseek reply is invalid
(`dependent.h_qr_dep` and `dependent.h_dc_would_be` reference an unresolved `dependent.h_qr_rel`; `dependent.dc_count` has
a collection parent binding mismatch), so its lines are ruled on validation, or on the merits by reading. Class M
dependent has no open section.

The rewording produces no completed-return difference, and checked against p501 p. 9 it introduces no error of medium
severity in `dependent.parent_home_paid` (one low: the TANF note, L1 for T-092). The same definition is incomplete in
`household.home_cost` and missing from `household.qss_eligible` (household findings F1 and F2). Compared with round 3, the
Claude reply restored the Form 2441 death-year route (stage15.f2441.parent_died_part_year agrees) and dropped the
multiple-support refusal from hoh_test1 (now scope); it still refuses multiple_support on a qualifying child, still lacks
the filer-TIN test of the American opportunity credit, and now asks born_died where months decides. eic_child and
eic_ssn_child are open again (scope, as in fix round 2). The deepseek reply fixed its sibling_descendant and dc_under13
errors but is invalid on a misnamed helper, and its lines 27 to 31 copy the worksheet with no eligibility condition.

Counts:
- Claude transcription: model error 17, scope 3.
- Deepseek transcription: model error 16, scope 2, representation 1.
- Claude render: ambiguity 2, interface gap 1.
- Deepseek render: ambiguity 1.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | dependent.claimed | model error | 6,650/7,463 agree; completed returns: 83 candidate-refuses, 29 candidate-unknown | i1040gi p. 21, Multiple support agreements; p. 17, Step 1 | Multiple-support refusal on a qualifying child (83 completed, classm.s3.4 dep_a); 6 born_died asks months already decides. |
| claude | transcription | dependent.ctc_child | model error | 7,061/7,463 agree; completed returns: 83 candidate-refuses, 23 candidate-unknown | i1040gi p. 18, Step 3; p. 21 | Step 3 tests are the project's; inherits its claimed. |
| claude | transcription | dependent.odc_person | model error | 6,732/7,463 agree; completed returns: 83 candidate-refuses, 26 candidate-unknown | i1040gi p. 19, Step 5; p. 21 | Inherits its claimed. |
| claude | transcription | dependent.ctc_amount | model error | 7,061/7,463 agree; completed returns: 83 candidate-refuses, 23 candidate-unknown | f1040s8812 line 5 | Inherited from ctc_child. |
| claude | transcription | dependent.actc_amount | model error | 7,061/7,463 agree; completed returns: 83 candidate-refuses, 23 candidate-unknown | f1040s8812 line 16b | Inherited from ctc_child. |
| claude | transcription | dependent.odc_amount | model error | 6,732/7,463 agree; completed returns: 83 candidate-refuses, 26 candidate-unknown | f1040s8812 line 7 | Inherited from odc_person. |
| claude | transcription | dependent.hoh_test2 | model error | 6,861/7,463 agree; completed returns: 83 candidate-refuses, 23 candidate-unknown, 3 project-unknown | i1040gi p. 14, Test 2; p. 21; p501 p. 9 | Per-person test is the project's; inherits claimed. |
| claude | transcription | dependent.hoh_test1 | scope | 7,072/7,463 agree; completed returns: 10 project-unknown | i1040gi p. 14, Test 1; p. 22 | Project's test; differences are the project's cited refusals and 10 partial records. |
| claude | transcription | dependent.eic_child | scope | 7,156/7,463 agree; completed returns: 3 project-unknown, 2 candidate-unknown | i1040gi pp. 20, 41; p501 p. 13 | Divorced_rule refusal reaches only refused returns; kidnapped asked later. |
| claude | transcription | dependent.eic_ssn_child | scope | 7,160/7,463 agree; completed returns: 2 candidate-unknown, 2 project-unknown | i1040gi pp. 41, 46 | Inherits eic_child. |
| claude | transcription | dependent.dc_qp | model error | 4,473/7,463 agree; completed returns: 683 value, 83 candidate-refuses, 79 candidate-unknown | i2441 p. 1; p503 p. 3 | Death-year route restored; 683 care-omission values reach no amount; inherits claimed. |
| claude | transcription | dependent.dc_count | model error | 1,925/7,463 agree; completed returns: 1,308 value, 83 candidate-refuses, 79 candidate-unknown | i2441 p. 3, Line 2 | 1,308 values are entries f2441.qp_count never counts; inherits dc_qp. |
| claude | transcription | dependent.ptc_magi_counted | model error | 6,647/7,463 agree; completed returns: 83 candidate-refuses, 12 project-unknown, 1 value | i8962 p. 8, Line 2b | Own formula representation; inherits claimed. |
| claude | transcription | 2(d) | model error | 6,398/7,463 agree; completed returns: 83 candidate-refuses, 36 candidate-unknown, 26 project-unknown | i2441 p. 3, Column (d) | No completed value difference; inherits dc_qp. |
| claude | transcription | 2(c) | model error | 6,431/7,463 agree; completed returns: 83 candidate-refuses, 49 candidate-unknown, 4 value | i2441 p. 3, Column (c) | 4 care-omission boxes reach no amount; inherits dc_qp. |
| claude | transcription | 27 | model error | 3,326/7,463 agree; completed returns: 1,100 candidate-unknown, 83 candidate-refuses | i8863 p. 2; p. 3, item 5 | No filer-TIN test (jack_kay rerun: line 30 $2,500.00 where the project gives line 31 $4,300.00) and no f8863.paid test (1,100 asks). |
| claude | transcription | 28 | model error | 3,326/7,463 agree; completed returns: 1,100 candidate-unknown, 83 candidate-refuses | i8863 p. 2; p. 3, item 5 | As line 27. |
| claude | transcription | 29 | model error | 3,326/7,463 agree; completed returns: 1,100 candidate-unknown, 83 candidate-refuses | i8863 p. 2; p. 3, item 5 | As line 27. |
| claude | transcription | 30 | model error | 3,326/7,463 agree; completed returns: 1,100 candidate-unknown, 83 candidate-refuses | i8863 p. 2; p. 3, item 5 | As line 27. |
| claude | transcription | 31 | model error | 3,326/7,463 agree; completed returns: 1,100 candidate-unknown, 83 candidate-refuses | i8863 p. 2; p. 3, item 5; p. 9 | As line 27 (line 31 $0.00 against $4,300.00). |
| deepseek | transcription | dependent.claimed | model error | not executable (reply invalid) | README (validation); i1040gi pp. 17, 19 | Reads h_qr_dep, whose h_qr_rel does not resolve; tests otherwise the project's. |
| deepseek | transcription | dependent.ctc_child | model error | not executable (reply invalid) | i1040gi p. 18, Step 3 q. 4 | Reads household.taxpayer_work_ssn: no CTC where only the spouse has a work SSN. |
| deepseek | transcription | dependent.odc_person | model error | not executable (reply invalid) | README (validation); i1040gi p. 19, Step 5 | Invalid via claimed; no filers' TIN test; inherits ctc_child. |
| deepseek | transcription | dependent.ctc_amount | model error | not executable (reply invalid) | f1040s8812 line 5 | Inherited from ctc_child. |
| deepseek | transcription | dependent.actc_amount | model error | not executable (reply invalid) | f1040s8812 line 16b | Inherited from ctc_child. |
| deepseek | transcription | dependent.odc_amount | model error | not executable (reply invalid) | README (validation); f1040s8812 line 7 | Inherited from odc_person. |
| deepseek | transcription | dependent.hoh_test2 | model error | not executable (reply invalid) | README (validation); i1040gi p. 14, Test 2; p501 p. 9 | Invalid via claimed; no part-year route; sibling_descendant counted; multiple-support refusal on the line. |
| deepseek | transcription | dependent.hoh_test1 | model error | not executable (reply invalid) | README (validation); i1040gi p. 14, Test 1 | Invalid via claimed; multiple-support refusal on the line. |
| deepseek | transcription | dependent.eic_child | scope | not executable (reply invalid) | i1040gi pp. 20, 41, 44 | Refusals only (divorced_rule reaches refused returns; married child computed where the project refuses). |
| deepseek | transcription | dependent.eic_ssn_child | scope | not executable (reply invalid) | i1040gi pp. 41, 46 | Inherits eic_child. |
| deepseek | transcription | dependent.dc_qp | model error | not executable (reply invalid) | README (validation); i2441 p. 1; p503 p. 3 | Invalid via claimed and h_dc_would_be; no death-year route. |
| deepseek | transcription | dependent.dc_count | model error | not executable (reply invalid) | README (validation); i2441 p. 3 | Collection parent binding mismatch. |
| deepseek | transcription | dependent.ptc_magi_counted | representation | not executable (reply invalid) | i8962 p. 8, Line 2b | Unchanged; zero spelled as $0.00 minus $0.00. |
| deepseek | transcription | 2(c) | model error | not executable (reply invalid) | README (validation); i2441 p. 3, Column (c) | Invalid via dc_qp; adds a dc_paid condition at 14 or over; death-year error. |
| deepseek | transcription | 27 | model error | not executable (reply invalid) | f8863 p. 2, lines 23 to 26; i8863 p. 2 | Copies aqee line27 with no eligibility condition. |
| deepseek | transcription | 28 | model error | not executable (reply invalid) | f8863 p. 2, lines 23 to 26; i8863 p. 2 | As line 27. |
| deepseek | transcription | 29 | model error | not executable (reply invalid) | f8863 p. 2, lines 23 to 26; i8863 p. 2 | As line 27. |
| deepseek | transcription | 30 | model error | not executable (reply invalid) | f8863 p. 2, lines 23 to 26; i8863 p. 2 | As line 27. |
| deepseek | transcription | 31 | model error | not executable (reply invalid) | f8863 p. 2, line 26 caution; i8863 p. 9 | Copies ws4_llc for every entry, including AOC students. |
| claude | render | 2(d) | ambiguity | render MISMATCH | amb.2025.dc_line30; i2441 p. 3, Column (d) | Rejected reading (column (d) net of benefits). |
| claude | render | 2(c) | interface gap | render MISMATCH | i2441 p. 1, item 3 | Nondependent qualifying persons are refused by f2441.nondependent_gate, outside the dependent render. |
| claude | render | 23 | ambiguity | render MISMATCH | amb.2025.edu_1098t_date; i8863 p. 1; p970 p. 2 | 1098-T request date; line text matches. |
| deepseek | render | 2(d) | ambiguity | render MISMATCH | amb.2025.dc_line30 | Rejected reading. |

Findings: none of medium or higher severity for dependent. Low L1 (for T-092) in
`.transcription/proposed/fixr4/dependent.findings.md`.
