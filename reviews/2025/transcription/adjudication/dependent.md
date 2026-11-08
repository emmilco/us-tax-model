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

## Fix round 4 (superseded subject)

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

## T-091 round (superseded subject)

Subject after BUG-0264 to BUG-0266 (`dependent.spouse_relative`, `dependent.qr_all_year`, `dependent.absence_no_return`;
gates `dependent.hoh_absence` on `hoh_test2` and `dependent.qr_kidnapped` on `qualifying_relative`). Fresh replies of
2026-10-31. Transcription rulings: `.transcription/proposed/t091/transcription.dependent.json` and
`transcription.dependent.deepseek.json`; findings in `.transcription/proposed/t091/dependent.findings.md`. Render and class M
rows of this round are adjudicated separately (`dependent.classm.findings.md`, `render.dependent*.json`, `classm.dependent*.json`
in the same directory) and are merged here by the orchestrator. Triage `../triage/dependent.json`, executable-triage-v2 (1,408
fixtures, 500 generated returns seed 20261026, 2,809 partial records; 8,269 comparisons per line), reproduced exactly by an
uncapped rerun (scratch `adj-t091-dep-transcription/`); every completed-return difference of the Claude reply was assigned
to a named cause, none unexplained. The deepseek reply is invalid only on `dependent.dc_count` (collection parent binding
mismatch); its other lines validate and are ruled by reading.

T-091 introduces no error of medium severity. The Claude reply encodes the three new inputs as the project does; the only
triage differences they produce are partial records, the two `hoh_absence` regressions (the reply makes the absence a
condition of Test 2 instead of a refusal) and one mfj value of `hoh_test2` that no head-of-household return reads. One low
(L1, for T-092): `hoh_absence` refuses the return for any entry with an absence answer, even one that is not needed to
qualify you. Compared with fix round 4, the Claude reply's Step 3 lines and `hoh_test2` no longer inherit the multiple-support
refusal (now scope); it still declares multiple_support on `claimed` (2 completed returns, classm.s3.4 dep_a), has no
f2441.care test, and no filer-TIN or f8863.paid test for the education lines. The deepseek reply's `ctc_child` now tests
any dependent instead of a qualifying child, and its `hoh_test2` has no absence rule.

Counts:
- Claude transcription: model error 13, scope 5.
- Deepseek transcription: model error 15, scope 3.
- Render (both families): ambiguity 1 each (2(d), amb.2025.dc_line30).
- Class M (both families, same 8 cases): model error 1 (classm.dependent.2 dc_line2c), representation 1 (classm.dependent.8 dc_line2d), both dropped; the project is right on both, and the dc_* lines are unchanged by T-091.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | dependent.claimed | model error | 7,820/8,269 agree; completed returns: 31 candidate-unknown, 2 candidate-refuses, 1 project-unknown | i1040gi p. 21, Multiple support agreements; p. 17, Step 1 | Multiple-support refusal on a qualifying child (classm.s3.4 dep_a); lawful asked of a household_member; rest partial records. |
| claude | transcription | dependent.ctc_child | scope | 8,240/8,269 agree; completed returns: none | i1040gi p. 18, Steps 2 and 3; p501 p. 18 | Project's Step 3 test; kidnapped refusals on T-091 regressions and the sa.dependent joint-return route, on refused or incomplete returns. |
| claude | transcription | dependent.odc_person | model error | 7,933/8,269 agree; completed returns: 9 candidate-unknown, 2 candidate-refuses | i1040gi p. 19, Step 5; p. 21 | Inherits its claimed. |
| claude | transcription | dependent.ctc_amount | scope | 8,240/8,269 agree; completed returns: none | f1040s8812 line 5 | Inherited from ctc_child. |
| claude | transcription | dependent.actc_amount | scope | 8,240/8,269 agree; completed returns: none | f1040s8812 line 16b | Inherited from ctc_child. |
| claude | transcription | dependent.odc_amount | model error | 7,933/8,269 agree; completed returns: 9 candidate-unknown, 2 candidate-refuses | f1040s8812 line 7 | Inherited from odc_person. |
| claude | transcription | dependent.hoh_test2 | scope | 7,980/8,269 agree; completed returns: 8 project-unknown, 6 candidate-unknown | i1040gi p. 14, Test 2; p501 pp. 9, 19 | Absence as a condition, not a refusal (meets the project on completed returns); all completed differences partial records; mfj value unread. |
| claude | transcription | dependent.hoh_test1 | scope | 7,955/8,269 agree; completed returns: 1 project-unknown | i1040gi p. 14, Test 1; p. 22 | Project's test; differences are the project's cited refusals and 1 partial record. |
| claude | transcription | dependent.dc_qp | model error | 4,771/8,269 agree; completed returns: 825 value, 30 candidate-unknown | i2441 pp. 1, 3; p503 p. 3 | No f2441.care test: 825 values reach no amount; asks care questions without care. |
| claude | transcription | dependent.dc_count | model error | 2,313/8,269 agree; completed returns: 1,845 value, 30 candidate-unknown | i2441 p. 3, Line 2 | Values on entries f2441.qp_count never counts; inherits dc_qp. |
| claude | transcription | dependent.ptc_magi_counted | model error | 7,826/8,269 agree; completed returns: 30 project-unknown, 2 candidate-refuses | i8962 p. 8, Line 2b | Own formula representation; inherits claimed. |
| claude | transcription | 2(d) | model error | 7,452/8,269 agree; completed returns: 44 project-unknown, 28 candidate-unknown | i2441 p. 3, Column (d), Line 2 | No completed value; refused-return values are non-qualifying persons (dc_paid's own wording makes them $0.00). |
| claude | transcription | 2(c) | model error | 7,598/8,269 agree; completed returns: 19 candidate-unknown, 4 value | i2441 p. 3, Column (c) | 4 care-omission boxes reach no amount; classm.dependent.2 dep_b: project right (no care). |
| claude | transcription | 27 | model error | 4,681/8,269 agree; completed returns: 765 candidate-unknown, 2 candidate-refuses | i8863 p. 2; p. 3, item 5 | No filer-TIN test (jack_kay rerun: line 30 $2,500.00 against line 31 $4,300.00) and no f8863.paid test (755 asks). |
| claude | transcription | 28 | model error | 4,681/8,269 agree; completed returns: 765 candidate-unknown, 2 candidate-refuses | i8863 p. 2; p. 3, item 5 | As line 27. |
| claude | transcription | 29 | model error | 4,681/8,269 agree; completed returns: 765 candidate-unknown, 2 candidate-refuses | i8863 p. 2; p. 3, item 5 | As line 27. |
| claude | transcription | 30 | model error | 4,681/8,269 agree; completed returns: 765 candidate-unknown, 2 candidate-refuses | i8863 p. 2; p. 3, item 5 | As line 27. |
| claude | transcription | 31 | model error | 4,682/8,269 agree; completed returns: 765 candidate-unknown, 2 candidate-refuses | i8863 p. 2; p. 3, item 5; p. 9 | As line 27 (line 31 $0.00 against $4,300.00). |
| deepseek | transcription | dependent.claimed | model error | not executable (reply invalid on dc_count) | i1040gi p. 21; p. 17, Step 1 | T-091 inputs as the project; multiple-support refusal on the line reaches a qualifying child. |
| deepseek | transcription | dependent.ctc_child | model error | not executable (reply invalid on dc_count) | i1040gi p. 18, Step 3 | Reads claimed, not a qualifying child (a qualifying relative under 17 gets the CTC); no household.ctc_ssn. |
| deepseek | transcription | dependent.odc_person | model error | not executable (reply invalid on dc_count) | i1040gi p. 19, Step 5 | No filers' TIN test; inherits claimed and ctc_child. |
| deepseek | transcription | dependent.ctc_amount | model error | not executable (reply invalid on dc_count) | f1040s8812 line 5 | Inherited from ctc_child. |
| deepseek | transcription | dependent.actc_amount | model error | not executable (reply invalid on dc_count) | f1040s8812 line 16b | Inherited from ctc_child. |
| deepseek | transcription | dependent.odc_amount | model error | not executable (reply invalid on dc_count) | f1040s8812 line 7 | Inherited from odc_person. |
| deepseek | transcription | dependent.hoh_test2 | model error | not executable (reply invalid on dc_count) | p501 p. 9, Temporary absences, Death or birth; i1040gi p. 14 | No absence rule (t091.absence.hoh_refused met), no part-year route, relative counted without sa.dependent. |
| deepseek | transcription | dependent.hoh_test1 | scope | not executable (reply invalid on dc_count) | i1040gi p. 14, Test 1 | Project's test; differences are the project's refusals. |
| deepseek | transcription | dependent.eic_child | scope | not executable (reply invalid on dc_count) | i1040gi pp. 20, 41 | divorced_rule refusal reaches only refused returns. |
| deepseek | transcription | dependent.eic_ssn_child | scope | not executable (reply invalid on dc_count) | i1040gi pp. 41, 46 | Inherits eic_child. |
| deepseek | transcription | dependent.dc_qp | model error | not executable (reply invalid on dc_count) | i2441 p. 1; p503 p. 3 | Under-13 route takes any dependent; no death-year route. |
| deepseek | transcription | dependent.dc_count | model error | not executable (reply invalid on dc_count) | README (validation); i2441 p. 3 | Collection parent binding mismatch. |
| deepseek | transcription | 2(c) | model error | not executable (reply invalid on dc_count) | i2441 p. 3, Column (c), Line 2 | No qualifying-person condition. |
| deepseek | transcription | 27 | model error | not executable (reply invalid on dc_count) | f8863 p. 2, line 26; i8863 p. 3, item 5 | No filers' TIN or f8863.paid test; raw edu_over refusal. |
| deepseek | transcription | 28 | model error | not executable (reply invalid on dc_count) | f8863 p. 2, line 26; i8863 p. 3, item 5 | As line 27. |
| deepseek | transcription | 29 | model error | not executable (reply invalid on dc_count) | f8863 p. 2, line 26; i8863 p. 3, item 5 | As line 27. |
| deepseek | transcription | 30 | model error | not executable (reply invalid on dc_count) | f8863 p. 2, line 26; i8863 p. 3, item 5 | As line 27. |
| deepseek | transcription | 31 | model error | not executable (reply invalid on dc_count) | f8863 p. 2; i8863 p. 9 | Inherits line 27's missing filers' TIN test. |
| claude | render | 2(d) | ambiguity | render MISMATCH | amb.2025.dc_line30; i2441 p. 3, Column (d) | Rejected reading (column (d) net of benefits); line unchanged by T-091. |
| deepseek | render | 2(d) | ambiguity | render MISMATCH | amb.2025.dc_line30 | Rejected reading; unchanged. |
| claude | class M | classm.dependent.2 — dependent[dep_b].dc_line2c | model error (drop) | f2441.care no, benefits no; dc_disabled_qp yes, dc_qp no; qp_count 0 | i2441 p. 1, Purpose of Form; p. 3, Column (c) | Box checked with no care paid: no line 2 entry, no "time the care was provided". |
| deepseek | class M | classm.dependent.2 — dependent[dep_b].dc_line2c | model error (drop) | same inputs | i2441 p. 1; p. 3, Column (c) | Same; also reads permanent disability for inability to care for oneself. |
| claude | class M | classm.dependent.8 — dependent[dep_b].dc_line2d | representation (drop) | dc_qp no; dc_paid $250.00 supplied; line 3 $1,480.00 either way; targeted eval never demands dep_b's dc_paid | i2441 p. 3, Line 2 | Model's $0.00 is the source reading; $250.00 displays an answer never asked and never summed. |
| deepseek | class M | classm.dependent.8 — dependent[dep_b].dc_line2d | representation (drop) | same inputs | i2441 p. 3, Line 2 | Same. |

Findings (transcription): none of medium or higher severity. Low L1 (for T-092) in
`.transcription/proposed/t091/dependent.findings.md`.

## T-091 round 2 (superseded subject)

Subject after BUG-0267 (the correction of T-091 before commit): `dependent.hoh_test2_lived` (the former Test 2 expression),
`dependent.hoh_test2` = `hoh_test2_lived` and not `absence_no_return`, `dependent.hoh_absence` = `hoh_test2_lived` and
`absence_no_return`, and the return-level gate `household.hoh_absence` (unmarried, Test 1 not met, home cost yes, no Test 2
person, at least one absence person) refusing `household.hoh_eligible`. Fresh replies of 2026-10-31. Transcription rulings:
`.transcription/proposed/t091r2/transcription.dependent.json` and `transcription.dependent.deepseek.json`; findings in
`.transcription/proposed/t091r2/dependent.findings.md`. Render and class M rows of this round are adjudicated separately and
merged here by the orchestrator. Triage `../triage/dependent.json`, executable-triage-v2 (1,411 fixtures, 500 generated returns
seed 20261026, 2,809 partial records; 8,275 comparisons per line), reproduced exactly by an uncapped rerun (scratch
`adj-t091r2-dep-transcription/`); every completed-return difference of the Claude reply was assigned to a named cause, none
unexplained. The deepseek reply is invalid in triage (`dc_count` collection parent binding; `dc_over12_care` redeclared over
the published input; `edu_line31` reads a line `aqee` lacks); its other lines are ruled by reading.

No finding: neither T-091 nor its correction introduces an error of any severity. The gate fires exactly when head of
household turns on the recount (192-scenario matrix; the household adjudicator's 19 scenarios agree), the former Test 2
expression is unchanged as `hoh_test2_lived`, and nothing else in the subject changed. The Claude reply's 55 completed
claimed/odc values are contradictory married-no/joint-return-yes records; its `hoh_test2` counts an absence head of household
does not count and has no part-year route; its claimed no longer refuses multiple support on a qualifying child (Step 3 and
ptc lines now scope). The deepseek reply excludes the absence person from Test 2 as the project does, but marks every entry's
absence answer on `hoh_absence`, omits `spouse_relative`, treats sibling_descendant as a relative who need not live with you,
and has no ctc_ssn or all_tin test.

Counts:
- Claude transcription: model error 13, scope 8.
- Deepseek transcription: model error 16, scope 3.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | dependent.claimed | model error | 7,623/8,275 agree; completed returns: 55 value, 30 candidate-unknown, 1 project-unknown | i1040gi p. 19, Step 4; p. 21, Married person | lawful asked of a household_member (classm.clcw26.2 dep_b); 55 values contradictory married/joint_return records; rest partial records. |
| claude | transcription | dependent.ctc_child | scope | 8,178/8,275 agree; completed returns: none | i1040gi p. 18, Step 3; p501 p. 18 | Project's Step 3 test; kidnapped refusals and the joint-return route on refused or incomplete returns. |
| claude | transcription | dependent.odc_person | model error | 7,705/8,275 agree; completed returns: 55 value, 28 candidate-unknown | i1040gi p. 19, Step 5 | Inherits its claimed. |
| claude | transcription | dependent.ctc_amount | scope | 8,178/8,275 agree; completed returns: none | f1040s8812 line 5 | Inherited from ctc_child. |
| claude | transcription | dependent.odc_amount | model error | 7,705/8,275 agree; completed returns: 55 value, 28 candidate-unknown | f1040s8812 line 7 | Inherited from odc_person. |
| claude | transcription | dependent.actc_amount | scope | 8,178/8,275 agree; completed returns: none | f1040s8812 line 16b | Inherited from ctc_child. |
| claude | transcription | dependent.hoh_absence | scope | 8,038/8,275 agree; completed returns: 1 project-unknown | p501 p. 9, Temporary absences | The project's definition; differences are the project's cited screens and 1 partial record. |
| claude | transcription | dependent.hoh_test2 | model error | 7,469/8,275 agree; completed returns: 82 project-unknown, 23 candidate-unknown, 7 value | i1040gi p. 14, Test 2; p501 p. 9 | Counts an absence head of household does not count (t091.absence.hoh_refused child) and has no part-year route (stage8.hoh.parent.died_lived_part_year); completed: 7 contradictory records, unknowns unread or partial. |
| claude | transcription | dependent.hoh_test1 | scope | 7,958/8,275 agree; completed returns: 1 project-unknown | i1040gi p. 14, Test 1 | Project's test; project's cited refusals and 1 partial record. |
| claude | transcription | dependent.eic_child | scope | 8,072/8,275 agree; completed returns: 3 candidate-unknown, 2 project-unknown | i1040gi pp. 20, 41, 44 | divorced_rule refusals on refused returns; married refused by the project; partial records. |
| claude | transcription | dependent.eic_ssn_child | scope | completed returns: 3 candidate-unknown, 2 project-unknown | i1040gi p. 46 | Inherits eic_child. |
| claude | transcription | dependent.dc_qp | model error | 4,957/8,275 agree; completed returns: 840 value, 27 candidate-unknown | i2441 p. 1; p503 p. 3 | No f2441.care test (840 values reach no amount); no death-year route (stage15.f2441.parent_died_part_year). |
| claude | transcription | dependent.dc_count | model error | 2,346/8,275 agree; completed returns: 1,878 value, 27 candidate-unknown | i2441 p. 3, Line 2 | Values on care-no entries f2441.qp_count never counts; inherits dc_qp. |
| claude | transcription | dependent.ptc_magi_counted | scope | 7,798/8,275 agree; completed returns: 31 project-unknown | i8962 p. 8, Line 2b | Own formula a representation; unknowns on entries line 2b does not sum; candidate refusals on refused returns. |
| claude | transcription | 2(d) | model error | 7,395/8,275 agree; completed returns: 45 project-unknown, 26 candidate-unknown | i2441 p. 3, Column (d); p503 p. 3 | Inherits dc_qp's death-year omission ($4,000.00 against $0.00); no completed value. |
| claude | transcription | 2(c) | model error | 7,658/8,275 agree; completed returns: 17 candidate-unknown, 4 value | i2441 p. 3, Column (c) | Care omission reaches no amount; inherits dc_qp's death-year omission. |
| claude | transcription | 27 | model error | 4,819/8,275 agree; completed returns: 758 candidate-unknown | i8863 p. 2; p. 3, item 5 | No filer-TIN test (jack_kay rerun: line 30 $2,500.00 against line 31 $4,300.00) and no f8863.paid test (741 asks). |
| claude | transcription | 28 | model error | 4,819/8,275 agree; completed returns: 758 candidate-unknown | i8863 p. 2; p. 3, item 5 | As line 27. |
| claude | transcription | 29 | model error | 4,819/8,275 agree; completed returns: 758 candidate-unknown | i8863 p. 2; p. 3, item 5 | As line 27. |
| claude | transcription | 30 | model error | 4,819/8,275 agree; completed returns: 758 candidate-unknown | i8863 p. 2; p. 3, item 5 | As line 27. |
| claude | transcription | 31 | model error | 4,820/8,275 agree; completed returns: 758 candidate-unknown | i8863 p. 2; p. 3, item 5; p. 9 | As line 27 (line 31 $0.00 against $4,300.00). |
| deepseek | transcription | dependent.claimed | model error | not executable (reply invalid) | p501 p. 19, Relatives who don't have to live with you, Joint return; i1040gi p. 21 | sibling_descendant needs no all-year test; no spouse_relative; multiple-support refusal reaches a qualifying child. |
| deepseek | transcription | dependent.ctc_child | model error | not executable (reply invalid) | i1040gi p. 18, Step 3, question 4 | No household.ctc_ssn. |
| deepseek | transcription | dependent.odc_person | model error | not executable (reply invalid) | i1040gi p. 19, Step 5, question 1 | No filers' TIN test; inherits claimed and ctc_child. |
| deepseek | transcription | dependent.ctc_amount | model error | not executable (reply invalid) | f1040s8812 line 5 | Inherited from ctc_child. |
| deepseek | transcription | dependent.odc_amount | model error | not executable (reply invalid) | f1040s8812 line 7 | Inherited from odc_person. |
| deepseek | transcription | dependent.actc_amount | model error | not executable (reply invalid) | f1040s8812 line 16b | Inherited from ctc_child. |
| deepseek | transcription | dependent.hoh_absence | model error | not executable (reply invalid) | p501 p. 9, Temporary absences | Copies absence_no_return for every entry (yes for a non-Test-2 roommate; answer asked of every entry). |
| deepseek | transcription | dependent.hoh_test2 | model error | not executable (reply invalid) | p501 p. 9, Death or birth; i1040gi p. 14 | No part-year route; sibling_descendant counted; home_cost read on the line. |
| deepseek | transcription | dependent.hoh_test1 | scope | not executable (reply invalid) | i1040gi p. 14, Test 1 | Project's test; differences are refusals. |
| deepseek | transcription | dependent.eic_child | scope | not executable (reply invalid) | i1040gi pp. 41, 44 | Married child refused through its claimed; refusals only. |
| deepseek | transcription | dependent.eic_ssn_child | scope | not executable (reply invalid) | i1040gi p. 46 | Inherits eic_child. |
| deepseek | transcription | dependent.dc_qp | model error | not executable (reply invalid) | i2441 p. 1; p503 p. 3 | No death-year route; inherits claimed. |
| deepseek | transcription | dependent.dc_count | model error | not executable (reply invalid) | README (validation); i2441 p. 3 | Collection parent binding mismatch. |
| deepseek | transcription | 2(c) | model error | not executable (reply invalid) | README (validation); i2441 p. 3, Column (c) | Reads dc_over12_care redeclared over the published input. |
| deepseek | transcription | 27 | model error | not executable (reply invalid) | f8863 p. 2, line 26; i8863 p. 3, item 5 | Copies aqee line 27 for every entry, no eligibility test. |
| deepseek | transcription | 28 | model error | not executable (reply invalid) | f8863 p. 2, line 26 | As line 27. |
| deepseek | transcription | 29 | model error | not executable (reply invalid) | f8863 p. 2, line 26 | As line 27. |
| deepseek | transcription | 30 | model error | not executable (reply invalid) | f8863 p. 2, line 26 | As line 27. |
| deepseek | transcription | 31 | model error | not executable (reply invalid) | README (validation); i8863 p. 9 | aqee has no line 31. |
| claude | render | 2(d) | ambiguity | render MISMATCH | amb.2025.dc_line30; i2441 p. 3, Column (d) | Rejected reading (column (d) net of benefits); line unchanged. |
| claude | render | 2(c) | interface gap | render MISMATCH (MATCH in round 1 on identical text) | i2441 p. 1, Qualifying Person(s), item 3 | Non-dependent disabled person (items a-c) is refused by f2441.nondependent_gate on qp_count and paid_total, a form the reviewer did not see; column (c) test matches. |
| deepseek | render | 2(d) | ambiguity | render MISMATCH | amb.2025.dc_line30 | Rejected reading; unchanged. |
| claude | class M | classm.dependent.8 — dependent[dep_b].dc_line2d | representation (drop) | dc_qp no; dc_paid $250.00 supplied; line 3 $1,480.00 either way; targeted eval demands only dep_a's dc_paid | i2441 p. 3, Line 2 | Model's $0.00 is the source reading; $250.00 displays an answer never asked and never summed. |
| deepseek | class M | classm.dependent.2 — dependent[dep_b].dc_line2c | model error (drop) | f2441.care no, benefits no; dc_disabled_qp yes, dc_qp no; qp_count 0 | i2441 p. 1, Purpose of Form; p. 3, Column (c) | Box checked with no care paid; also reads permanent disability for inability to care for oneself. (Claude now agrees.) |
| deepseek | class M | classm.dependent.8 — dependent[dep_b].dc_line2d | representation (drop) | same inputs as Claude | i2441 p. 3, Line 2 | Same as Claude. |

Findings (transcription): none. `.transcription/proposed/t091r2/dependent.findings.md`.

## Backlog round (superseded subject)
Subject after the person-dep and p4-docs packages (2026-11-03, uncommitted on main 3affaa5): `dependent.dc_paid` states the
care-expense rules of T-184 and leaves out the value of employer-furnished care (T-123); `dependent.supported` states the
five residual support rules (T-185); `dependent.eic_ssn` links `amb.2025.eic_valid_ssn`. No expression changed. Fresh replies
of 2026-11-03 from claude-opus-5-5, deepseek-flash and gpt-6-astra (first gpt review of this form). Rulings:
`.transcription/proposed/bklg/{transcription,render}.dependent[.deepseek|.gpt].json`; findings
`.transcription/proposed/bklg/dependent.findings.md`. All three replies are valid and were triaged with the witness cap lifted
(triage.py's triage() called directly; scratch `/tmp/adj-bklg-dep-f2441/triage/`; executable-triage-v2, 1,495 fixtures, 500
generated returns seed 20261026, 2,946 partial records from 40 bases, 9,011 comparisons per line). The committed records in
`../triage/` predate these replies and were not rewritten. Every completed-return value difference was traced to a cause:
the Claude reply's household_member test without qr_all_year (claimed, odc), the missing f2441.care test (dc_qp, dc_count),
and, for deepseek and gpt, married-no/joint-return-yes records the interview cannot produce, plus deepseek's exclusion of a
non-citizen qualifying child from Test 2 (6 consistent records).

No finding; no error introduced by either package (wording and links only; each new sentence checked against its quote).
Low L1 (predates this round): the `dependent.dc_count` label "One qualifying person" for a per-entry constant, which two
f2441 replies summed unfiltered.

Counts:
- Claude transcription: model error 13, scope 6.
- Deepseek transcription: model error 15, scope 5, representation 1.
- GPT transcription: model error 12, scope 8.
- Render (Claude, deepseek, gpt): ambiguity 1 each.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | dependent.claimed | model error | 8,616/9,011 agree; completed returns: 21 candidate-unknown, 7 value, 2 candidate-refuses | i1040gi p. 19, Step 4; p501 p. 21 | household_member passes without qr_all_year (all 7 completed values); multiple-support refusal reaches qualifying children. |
| claude | transcription | dependent.ctc_child | scope | 8,803/9,011 agree; completed returns: 14 candidate-unknown, 2 candidate-refuses | i1040gi p. 18, Step 3 | Project's Step 3 test; differences are refusals; 1 value on a refused return (classm.sc.2). |
| claude | transcription | dependent.odc_person | model error | 8,700/9,011 agree; completed returns: 18 candidate-unknown, 7 value, 2 candidate-refuses | i1040gi p. 19, Step 5 | Inherits claimed (7 completed values). |
| claude | transcription | dependent.ctc_amount | scope | 8,803/9,011 agree; completed returns: 14 candidate-unknown, 2 candidate-refuses | f1040s8812 line 5 | Inherits ctc_child. |
| claude | transcription | dependent.odc_amount | model error | 8,700/9,011 agree; completed returns: 18 candidate-unknown, 7 value, 2 candidate-refuses | f1040s8812 line 7 | Inherits odc_person ($0.00 against $500.00, 7 completed). |
| claude | transcription | dependent.actc_amount | scope | 8,803/9,011 agree; completed returns: 14 candidate-unknown, 2 candidate-refuses | f1040s8812 line 16b | Inherits ctc_child. |
| claude | transcription | dependent.hoh_absence | scope | 8,855/9,011 agree; completed returns: 2 candidate-refuses, 1 candidate-unknown | i1040gi p. 14, Test 2; p501 p. 9 | Project's design; cited refusals and 1 partial record. |
| claude | transcription | dependent.hoh_test2 | model error | 8,436/9,011 agree; completed returns: 42 project-unknown, 17 candidate-unknown, 2 candidate-refuses | i1040gi p. 14, Test 2; p501 p. 9, Death or birth | No part-year route; counts a non-returning absence (t091 regressions); no completed value. |
| claude | transcription | dependent.hoh_test1 | scope | 8,807/9,011 agree; completed returns: none | i1040gi p. 14, Test 1 | Project's test; project refusals only. |
| claude | transcription | dependent.dc_qp | model error | 5,679/9,011 agree; completed returns: 1,080 value, 56 candidate-unknown, 2 candidate-refuses | i2441 p. 1, Qualifying Person(s); p503 p. 3 | No f2441.care test (1,080 completed values); no death-year route. |
| claude | transcription | dependent.dc_count | model error | 2,379/9,011 agree; completed returns: 2,447 value, 56 candidate-unknown, 2 candidate-refuses | i2441 p. 3, Line 2 | 1 or 0 by its dc_qp; inherits dc_qp. |
| claude | transcription | dependent.ptc_magi_counted | scope | 8,357/9,011 agree; completed returns: 34 project-unknown, 2 candidate-refuses | i8962 p. 8, Line 2b | Representation of the project's line; partial records and its refusals. |
| claude | transcription | 2(d) | model error | 7,343/9,011 agree; completed returns: 74 candidate-unknown, 2 candidate-refuses | i2441 p. 3, Column (d) | Inherits dc_qp (death-year value $4,000.00 against $0.00, incomplete). |
| claude | transcription | 2(c) | model error | 7,865/9,011 agree; completed returns: 30 candidate-unknown, 4 candidate-shows-skipped, 2 candidate-refuses | i2441 p. 3, Column (c) | Inherits dc_qp: 4 completed boxes checked without care. |
| claude | transcription | 27 | model error | 4,657/9,011 agree; completed returns: 1,294 candidate-unknown, 2 candidate-refuses | i8863 p. 3, item 5; p970 p. 11 | Requires an issued TIN for the AOC (f1.t113.dep_aoc_applied $4,000.00 against $0.00); edu_over asked of every entry. |
| claude | transcription | 28 | model error | 4,657/9,011 agree; completed returns: 1,294 candidate-unknown, 2 candidate-refuses | i8863 p. 3, item 5; p970 p. 11 | As line 27. |
| claude | transcription | 29 | model error | 4,657/9,011 agree; completed returns: 1,294 candidate-unknown, 2 candidate-refuses | i8863 p. 3, item 5; p970 p. 11 | As line 27. |
| claude | transcription | 30 | model error | 4,657/9,011 agree; completed returns: 1,294 candidate-unknown, 2 candidate-refuses | i8863 p. 3, item 5; p970 p. 11 | As line 27. |
| claude | transcription | 31 | model error | 4,652/9,011 agree; completed returns: 1,294 candidate-unknown, 2 candidate-refuses | i8863 p. 3, item 5; p970 p. 11; i8863 p. 9 | As line 27; 2 values on refused returns. |
| deepseek | transcription | dependent.claimed | model error | 8,560/9,011 agree; completed returns: 61 candidate-unknown, 11 value, 2 candidate-refuses | i1040gi p. 19, Step 4; p501 p. 21 | sibling_descendant needs no household test; joint_return asked of unmarried persons; 11 completed values all married-no/joint-yes records. |
| deepseek | transcription | dependent.ctc_child | scope | 8,826/9,011 agree; completed returns: 14 candidate-unknown, 2 candidate-refuses | i1040gi p. 18, Step 3 | Refusals only; 1 value on a refused return. |
| deepseek | transcription | dependent.odc_person | model error | 8,574/9,011 agree; completed returns: 58 candidate-unknown, 11 value, 2 candidate-refuses | i1040gi p. 19, Step 5 | Inherits claimed. |
| deepseek | transcription | dependent.ctc_amount | scope | 8,826/9,011 agree; completed returns: 14 candidate-unknown, 2 candidate-refuses | f1040s8812 line 5 | Inherits ctc_child. |
| deepseek | transcription | dependent.odc_amount | model error | 8,574/9,011 agree; completed returns: 58 candidate-unknown, 11 value, 2 candidate-refuses | f1040s8812 line 7 | Inherits odc_person. |
| deepseek | transcription | dependent.actc_amount | scope | 8,826/9,011 agree; completed returns: 14 candidate-unknown, 2 candidate-refuses | f1040s8812 line 16b | Inherits ctc_child. |
| deepseek | transcription | dependent.hoh_absence | model error | 8,615/9,011 agree; completed returns: 10 candidate-unknown | i1040gi p. 14, Test 2; p501 p. 9 | absence_no_return copied for every entry (10 completed unknowns). |
| deepseek | transcription | dependent.hoh_test2 | model error | 8,381/9,011 agree; completed returns: 41 candidate-unknown, 13 value, 3 project-unknown, 2 candidate-refuses | i1040gi p. 14, Test 2; p501 p. 9 | Drops a non-citizen unmarried qualifying child (6 completed values on consistent records); no part-year route. |
| deepseek | transcription | dependent.hoh_test1 | model error | 8,671/9,011 agree; completed returns: 20 candidate-unknown, 2 candidate-refuses | i1040gi p. 14, Test 1 | Inherits claimed (joint_return asked). |
| deepseek | transcription | dependent.eic_child | scope | 8,691/9,011 agree; completed returns: 4 project-unknown, 1 candidate-unknown | i1040gi pp. 20, 41 | divorced_rule refusals; partial records withholding kidnapped. |
| deepseek | transcription | dependent.eic_ssn_child | scope | 8,693/9,011 agree; completed returns: 4 project-unknown, 1 candidate-unknown | i1040gi p. 46 | Inherits eic_child. |
| deepseek | transcription | dependent.dc_qp | model error | 3,958/9,011 agree; completed returns: 1,938 value, 84 candidate-unknown, 2 candidate-refuses | i2441 p. 1, Qualifying Person(s) | No f2441.care test (1,938 completed values). |
| deepseek | transcription | dependent.dc_count | model error | 3,922/9,011 agree; completed returns: 1,561 value, 84 candidate-unknown, 2 candidate-refuses | i2441 p. 3, Line 2 | Inherits dc_qp. |
| deepseek | transcription | dependent.ptc_magi_counted | representation | 9,011/9,011 agree; completed returns: none | i8962 p. 8, Line 2b | No difference. |
| deepseek | transcription | 2(d) | model error | 7,027/9,011 agree; completed returns: 114 candidate-unknown, 2 candidate-refuses | i2441 p. 3, Column (d) | Inherits dc_qp; 133 shows-skipped on refused returns. |
| deepseek | transcription | 2(c) | model error | 7,869/9,011 agree; completed returns: 37 candidate-unknown | i2441 p. 3, Column (c) | No qualifying-person test; dc_incapable asked of every entry 13 or older. |
| deepseek | transcription | 27 | model error | 4,878/9,011 agree; completed returns: 1,274 candidate-unknown, 1 candidate-shows-skipped | i8863 p. 3, item 5; p970 p. 11 | No claimed test (edu asked of every entry); issued TIN required; 1 completed shows-skipped. |
| deepseek | transcription | 28 | model error | 4,878/9,011 agree; completed returns: 1,274 candidate-unknown, 1 candidate-shows-skipped | i8863 p. 3, item 5; p970 p. 11 | As line 27. |
| deepseek | transcription | 29 | model error | 4,878/9,011 agree; completed returns: 1,274 candidate-unknown, 1 candidate-shows-skipped | i8863 p. 3, item 5; p970 p. 11 | As line 27. |
| deepseek | transcription | 30 | model error | 4,878/9,011 agree; completed returns: 1,274 candidate-unknown, 1 candidate-shows-skipped | i8863 p. 3, item 5; p970 p. 11 | As line 27. |
| deepseek | transcription | 31 | model error | 4,874/9,011 agree; completed returns: 1,274 candidate-unknown | i8863 p. 3, item 5; p970 p. 11 | As line 27. |
| gpt | transcription | dependent.claimed | model error | 8,522/9,011 agree; completed returns: 83 candidate-unknown, 11 value, 2 candidate-refuses | i1040gi p. 19, Step 4; p501 pp. 18, 21 | joint_return required of everyone; kidnapped children refused; 11 completed values all married-no/joint-yes records. |
| gpt | transcription | dependent.ctc_child | scope | 8,781/9,011 agree; completed returns: 28 candidate-unknown, 2 candidate-refuses | i1040gi p. 18, Step 3 | Refusals; 11 values on refused returns (no dependent TIN test, refused by the project). |
| gpt | transcription | dependent.odc_person | model error | 8,583/9,011 agree; completed returns: 78 candidate-unknown, 11 value, 2 candidate-refuses | i1040gi p. 19, Step 5 | Inherits claimed. |
| gpt | transcription | dependent.ctc_amount | scope | 8,781/9,011 agree; completed returns: 28 candidate-unknown, 2 candidate-refuses | f1040s8812 line 5 | Inherits ctc_child (refused returns only). |
| gpt | transcription | dependent.odc_amount | model error | 8,583/9,011 agree; completed returns: 78 candidate-unknown, 11 value, 2 candidate-refuses | f1040s8812 line 7 | Inherits odc_person. |
| gpt | transcription | dependent.actc_amount | scope | 8,781/9,011 agree; completed returns: 28 candidate-unknown, 2 candidate-refuses | f1040s8812 line 16b | Inherits ctc_child. |
| gpt | transcription | dependent.hoh_absence | scope | 8,873/9,011 agree; completed returns: 2 candidate-refuses, 1 candidate-unknown | i1040gi p. 14, Test 2; p501 p. 9 | Project's design; refusals only. |
| gpt | transcription | dependent.hoh_test2 | model error | 8,608/9,011 agree; completed returns: 67 candidate-unknown, 7 value, 2 candidate-refuses, 1 project-unknown | i1040gi p. 14, Test 2; p501 p. 9 | Inherits claimed (7 contradictory completed values); per-person absence refusal. |
| gpt | transcription | dependent.hoh_test1 | model error | 8,674/9,011 agree; completed returns: 21 candidate-unknown, 2 candidate-refuses | i1040gi p. 14, Test 1 | Inherits claimed. |
| gpt | transcription | dependent.eic_child | scope | 8,512/9,011 agree; completed returns: 6 candidate-unknown | i1040gi pp. 41, 43-45 | Refusals (divorced_rule, h_competing, kidnapping) only. |
| gpt | transcription | dependent.eic_ssn_child | scope | 8,513/9,011 agree; completed returns: 6 candidate-unknown | i1040gi p. 46 | Inherits eic_child. |
| gpt | transcription | dependent.dc_qp | model error | 5,626/9,011 agree; completed returns: 1,066 value, 69 candidate-unknown, 2 candidate-refuses | i2441 p. 1, Qualifying Person(s) | No f2441.care test (1,066 completed values). |
| gpt | transcription | dependent.ptc_magi_counted | scope | 8,284/9,011 agree; completed returns: 36 project-unknown, 2 candidate-refuses | i8962 p. 8, Line 2b | Representation; refusals and partial records. |
| gpt | transcription | 2(d) | model error | 7,096/9,011 agree; completed returns: 87 candidate-unknown, 2 candidate-refuses | i2441 p. 3, Column (d) | Inherits dc_qp. |
| gpt | transcription | 2(c) | scope | 7,858/9,011 agree; completed returns: 12 candidate-unknown, 2 candidate-refuses | i2441 p. 3, Column (c) | No value; refusals from its claimed. |
| gpt | transcription | 27 | model error | 8,744/9,011 agree; completed returns: 4 candidate-unknown, 2 candidate-refuses, 1 value | i8863 p. 3, item 5; p970 p. 11 | Issued TIN required for the AOC (classm.f8863.2, classm.aqee.1); completed value is a contradictory record. |
| gpt | transcription | 28 | model error | 8,745/9,011 agree; completed returns: 4 candidate-unknown, 2 candidate-refuses | i8863 p. 3, item 5; p970 p. 11 | As line 27. |
| gpt | transcription | 29 | model error | 8,745/9,011 agree; completed returns: 4 candidate-unknown, 2 candidate-refuses | i8863 p. 3, item 5; p970 p. 11 | As line 27. |
| gpt | transcription | 30 | model error | 8,744/9,011 agree; completed returns: 4 candidate-unknown, 2 candidate-refuses, 1 value | i8863 p. 3, item 5; p970 p. 11 | As line 27. |
| gpt | transcription | 31 | model error | 8,738/9,011 agree; completed returns: 4 candidate-unknown, 2 candidate-refuses | i8863 p. 3, item 5; p970 p. 11 | As line 27. |
| claude | render | 2(d) | ambiguity | render MISMATCH | amb.2025.dc_line30; i2441 p. 3, Column (d) | Rejected reading (column (d) net of benefits); dc_paid wording changes do not touch it. |
| deepseek | render | 2(d) | ambiguity | render MISMATCH | amb.2025.dc_line30; i2441 p. 3, Column (d) | Rejected reading (column (d) net of benefits); dc_paid wording changes do not touch it. |
| gpt | render | 2(d) | ambiguity | render MISMATCH | amb.2025.dc_line30; i2441 p. 3, Column (d) | Rejected reading (column (d) net of benefits); dc_paid wording changes do not touch it. |

Findings: none of medium or higher severity. `.transcription/proposed/bklg/dependent.findings.md`.

## Refresh round

Subject after the refresh-round fixes BUG-0391 to BUG-0401 (for these forms: BUG-0392 `person.sav_claimed` asked whenever education expenses are paid; BUG-0394 `person.educator_expenses` exclusions; BUG-0398 `household.taxpayer_work_ssn` cites and the `dependent.dc_count` label; BUG-0393 `scope.other_income` disaster distributions), transcription prompt `source-only-computation-v3`. Fresh replies of claude-opus-5-5 and deepseek-flash. Rulings in `.transcription/proposed/rf/` (`transcription.<stem>.json`, `render.<stem>.json`); prior rulings reused where the line, the disagreement and the evidence are the same, re-checked against `.transcription/archive/before-catalog-refresh-2026-11-03/`.

Triage: `../triage/<stem>.json`, executable-triage-v2, rerun today with `tools/transcription/triage.py` (1,565 fixtures, 500 generated returns seed 20261026, partial records per form); every completed-return difference was enumerated with the witness cap lifted in a scratch run (`/tmp/adj-rf-pers/full/`), and witnesses were traced with `--explain` where a ruling names one.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | dependent.claimed | model error | 8,110/8,578 agree; 233 candidate-unknown, 117 project-unknown, 114 project-refuses, 4 candidate-refuses; completed: 38 candidate-unknown | i1040gi p. 19, Step 4, "Any other person (other than your spouse) who lived with you all year as a member of your household if your relation | The reply asks dependent.kidnapped of every entry (the project asks it only through dependent.kidnap_residency, months under 7; p501 p. 13: a child who lived with you more than half the year meets the residency test with |
| claude | transcription | dependent.ctc_child | scope | 8,415/8,578 agree; 118 project-unknown, 24 project-refuses, 21 candidate-refuses | i1040gi p. 18, Step 3, questions 1 to 4. | The Step 3 test is the project's; every difference is a refusal or a refusal-driven unknown on a refused or incomplete record (the project's cited qc_tiebreak, kidnap_residency and claimed_no_tin screens; the reply's own |
| claude | transcription | dependent.odc_person | model error | 8,195/8,578 agree; 219 candidate-unknown, 114 project-refuses, 46 project-unknown, 4 candidate-refuses; completed: 32 candidate-unknown | i1040gi p. 19, Step 5; Step 4. | The Step 5 tests are the project's; the line inherits the reply's dependent.claimed: 32 completed candidate-unknowns on dependent.kidnapped and dependent.lawful (project yes, $500 on odc_amount). No completed-return amou |
| claude | transcription | dependent.ctc_amount | scope | 8,415/8,578 agree; 118 project-unknown, 24 project-refuses, 21 candidate-refuses | f1040s8812 line 5, "Multiply line 4 by $2,200". | Inherits dependent.ctc_child; no completed-return difference. |
| claude | transcription | dependent.odc_amount | model error | 8,195/8,578 agree; 219 candidate-unknown, 114 project-refuses, 46 project-unknown, 4 candidate-refuses; completed: 32 candidate-unknown | f1040s8812 line 7. | Inherits dependent.odc_person (32 completed candidate-unknowns, project $500 or $0). No completed-return amount differs. |
| claude | transcription | dependent.actc_amount | scope | 8,415/8,578 agree; 118 project-unknown, 24 project-refuses, 21 candidate-refuses | f1040s8812 line 16b. | Inherits dependent.ctc_child; no completed-return difference. |
| claude | transcription | dependent.hoh_absence | model error | 8,374/8,578 agree; 114 project-refuses, 83 candidate-unknown, 4 project-unknown, 3 candidate-refuses; completed: 10 candidate-unknown | i1040gi p. 14, Test 2; p501 p. 9, Temporary absences. | The gate is the project's design, but the reply now asks dependent.kidnapped of every entry (the project asks it only through dependent.kidnap_residency, months under 7; p501 p. 13: a child who lived with you more than h |
| claude | transcription | dependent.hoh_test2 | model error | 7,980/8,578 agree; 378 project-unknown, 114 project-refuses, 96 candidate-unknown, 7 value, 3 candidate-refuses; completed: 72 project-unknown, 12 candidate-unknown | i1040gi p. 14, Test 2; p501 p. 9, Temporary absences and Death or birth. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`) (no part-year route); it also asks dependent.kidnapped of every entry (the project asks it only through dependent.kidnap_residency, months |
| claude | transcription | dependent.hoh_test1 | scope | 8,442/8,578 agree; 80 project-unknown, 52 project-refuses, 3 candidate-refuses, 1 candidate-unknown | i1040gi p. 14, Test 1. | The reply's test (parent, claimed, parent_home_paid) is the project's; every difference is a project refusal (claimed_no_tin and other cited screens) or an unknown on a partial or refused record; none completed. As the p |
| claude | transcription | dependent.dc_qp | model error | 5,243/8,578 agree; 2,123 value, 996 candidate-unknown, 206 candidate-refuses, 8 project-unknown, 2 project-refuses; completed: 1,087 value, 138 candidate-unknown | i2441 p. 1, Qualifying Person(s); p503 p. 3. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): no f2441.care condition: 1,087 completed values, project no and candidate yes on entries with no care paid (for example classm.f4952.1.de |
| claude | transcription | dependent.dc_count | model error | 2,436/8,578 agree; 4,885 value, 1,050 candidate-unknown, 207 candidate-refuses; completed: 2,340 value, 138 candidate-unknown | i2441 p. 3, Line 2. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`) (BUG-0398 changed only the label): the project counts one per entry and f2441.qp_count filters by dependent.dc_qp; the reply's count is 1  |
| claude | transcription | dependent.ptc_magi_counted | scope | 8,069/8,578 agree; 301 project-unknown, 207 candidate-refuses, 1 value; completed: 16 project-unknown | i8962 p. 8, Line 2b, dependents "who are required to file". | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply's formula represents the project's choose on ptc_files; the 16 completed project-unknowns (for example classm.f8960.2.deepseek  |
| claude | transcription | 2(d) | model error | 6,844/8,578 agree; 1,517 candidate-unknown, 206 candidate-refuses, 8 project-unknown, 2 project-refuses, 1 value; completed: 203 candidate-unknown | i2441 p. 3, Column (d); p. 1, Qualifying Person(s). | Column (d) inherits the reply's dc_qp: 203 completed candidate-unknowns (dc_incapable, dc_paid, kidnapped, lawful asked where no care was paid and the project hides the column). No completed-return amount differs. |
| claude | transcription | 2(c) | model error | 7,725/8,578 agree; 574 candidate-unknown, 206 candidate-refuses, 57 project-unknown, 13 candidate-shows-skipped, 2 project-refuses, 1 value; completed: 91 candidate-unknown, 4 candidate-shows-skipped | i2441 p. 3, Column (c). | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the box inherits the reply's dc_qp: 4 completed candidate-shows-skipped (generated 35, 355 and others: the box checked with f2441.care no |
| claude | transcription | 27 | model error | 4,470/8,578 agree; 3,897 candidate-unknown, 200 candidate-refuses, 8 project-refuses, 2 candidate-shows-skipped, 1 value; completed: 1,524 candidate-unknown | f8863 p. 2, line 27; i8863 p. 3, Who cannot claim a credit; p970 p. 11. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply asks dependent.edu of every entry (1,485 completed unknowns where the project hides the line, for example classm.f4952.1.deepse |
| claude | transcription | 28 | model error | 4,470/8,578 agree; 3,897 candidate-unknown, 200 candidate-refuses, 8 project-refuses, 2 candidate-shows-skipped, 1 value; completed: 1,524 candidate-unknown | f8863 p. 2, line 28; i8863 p. 3, Who cannot claim a credit; p970 p. 11. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply asks dependent.edu of every entry (1,485 completed unknowns where the project hides the line, for example classm.f4952.1.deepse |
| claude | transcription | 29 | model error | 4,470/8,578 agree; 3,897 candidate-unknown, 200 candidate-refuses, 8 project-refuses, 2 candidate-shows-skipped, 1 value; completed: 1,524 candidate-unknown | f8863 p. 2, line 29; i8863 p. 3, Who cannot claim a credit; p970 p. 11. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply asks dependent.edu of every entry (1,485 completed unknowns where the project hides the line, for example classm.f4952.1.deepse |
| claude | transcription | 30 | model error | 4,470/8,578 agree; 3,897 candidate-unknown, 200 candidate-refuses, 8 project-refuses, 2 candidate-shows-skipped, 1 value; completed: 1,524 candidate-unknown | f8863 p. 2, line 30; i8863 p. 3, Who cannot claim a credit; p970 p. 11. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply asks dependent.edu of every entry (1,485 completed unknowns where the project hides the line, for example classm.f4952.1.deepse |
| claude | transcription | 31 | model error | 4,465/8,578 agree; 3,903 candidate-unknown, 199 candidate-refuses, 9 project-refuses, 2 value; completed: 1,524 candidate-unknown | f8863 p. 2, line 31; i8863 p. 3, Who cannot claim a credit; p970 p. 11. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the reply asks dependent.edu of every entry (1,485 completed unknowns where the project hides the line, for example classm.f4952.1.deepse |
| deepseek | transcription | dependent.claimed | model error | 7,513/8,578 agree; 747 candidate-unknown, 120 project-refuses, 101 project-unknown, 90 value, 7 candidate-refuses; completed: 208 candidate-unknown, 11 value | i1040gi p. 19, Step 4; p501 p. 21, Multiple Support Agreement. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): its tests read dependent.joint_return (asked by the project only of a married person; 119 completed unknowns), dependent.multiple_support |
| deepseek | transcription | dependent.ctc_child | model error | 8,382/8,578 agree; 65 candidate-unknown, 59 value, 40 project-unknown, 29 project-refuses, 3 candidate-refuses; completed: 4 candidate-unknown, 2 value | i1040gi p. 7, "to be eligible to claim the CTC or ACTC, you must have a valid SSN, which means it must be valid for employment"; p. 18, Step | The reply drops household.ctc_ssn: completed generated 360 and 439 (dep_a, a 9-year-old sibling with an SSN; the filer has no SSN valid for employment): project false, candidate true. The other differences are refusals a |
| deepseek | transcription | dependent.odc_person | model error | 7,530/8,578 agree; 743 candidate-unknown, 132 value, 120 project-refuses, 46 project-unknown, 7 candidate-refuses; completed: 208 candidate-unknown, 14 value | i1040gi p. 19, Steps 4 and 5. | Inherits the reply's dependent.claimed: 13 completed values on the contradictory married/joint_return records (for example classm.f8889.1.deepseek dep_b) and 208 completed unknowns (joint_return, multiple_support, lawful |
| deepseek | transcription | dependent.ctc_amount | model error | 8,382/8,578 agree; 65 candidate-unknown, 59 value, 40 project-unknown, 29 project-refuses, 3 candidate-refuses; completed: 4 candidate-unknown, 2 value | f1040s8812 line 5; i1040gi p. 7 (the filer's valid SSN). | Inherits dependent.ctc_child: completed generated 360 and 439, project $0, candidate $2,200. |
| deepseek | transcription | dependent.odc_amount | model error | 7,530/8,578 agree; 743 candidate-unknown, 132 value, 120 project-refuses, 46 project-unknown, 7 candidate-refuses; completed: 208 candidate-unknown, 14 value | f1040s8812 line 7. | Inherits dependent.odc_person: 13 completed values ($500 against $0) on the contradictory records, 208 completed unknowns. |
| deepseek | transcription | dependent.actc_amount | model error | 8,382/8,578 agree; 65 candidate-unknown, 59 value, 40 project-unknown, 29 project-refuses, 3 candidate-refuses; completed: 4 candidate-unknown, 2 value | f1040s8812 line 16b. | Inherits dependent.ctc_child: completed generated 360 and 439, project $0, candidate $1,700. |
| deepseek | transcription | dependent.hoh_absence | model error | 318/8,578 agree; 7,827 value, 318 project-refuses, 115 candidate-unknown; completed: 3,454 value, 25 candidate-unknown | i1040gi p. 14, Test 2; p501 p. 9, Temporary absences. | The reply is the negation of dependent.absence_no_return for every entry, so it is true for entries that are not Test 2 persons through an absence (3,454 completed values, for example classm.f8889.1.deepseek dep_a, a hou |
| deepseek | transcription | dependent.hoh_test2 | model error | 6,316/8,578 agree; 1,321 value, 459 candidate-unknown, 352 project-unknown, 124 project-refuses, 6 candidate-refuses; completed: 402 value, 133 candidate-unknown, 48 project-unknown | i1040gi p. 14, Test 2 (items 2 to 4, qualifying children who are not your dependent); p501 p. 9. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): its Test 2 person must pass its dependency tests, so unclaimed qualifying children are left out (402 completed values, for example classm |
| deepseek | transcription | dependent.hoh_test1 | model error | 7,987/8,578 agree; 454 candidate-unknown, 68 project-unknown, 55 project-refuses, 14 candidate-refuses; completed: 73 candidate-unknown | i1040gi p. 14, Test 1. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): its own test is the project's but it inherits the reply's multiple-support refusal and joint_return question (73 completed unknowns). |
| deepseek | transcription | dependent.eic_child | scope | 8,242/8,578 agree; 165 candidate-refuses, 84 project-unknown, 81 candidate-unknown, 6 project-refuses; completed: 11 project-unknown, 2 candidate-unknown | i1040gi p. 41, Step 3. | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): the differences are refusals (the reply's dependent.divorced_rule refusal on refused returns; the project's cited eic_tiebreak and kidnap |
| deepseek | transcription | dependent.eic_ssn_child | scope | 8,245/8,578 agree; 165 candidate-refuses, 84 project-unknown, 78 candidate-unknown, 6 project-refuses; completed: 11 project-unknown, 1 candidate-unknown | i1040gi p. 46, Worksheet A, line 2. | Inherits dependent.eic_child (11 completed project-unknowns on returns with no EIC). No completed-return amount differs. |
| deepseek | transcription | dependent.dc_qp | model error | 1,162/8,578 agree; 5,379 value, 1,829 candidate-unknown, 203 candidate-refuses, 3 project-unknown, 2 project-refuses; completed: 3,001 value, 229 candidate-unknown | i2441 p. 1, Qualifying Person(s). | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): no f2441.care condition: 3,001 completed values, project no and candidate yes on entries without care (for example classm.f8960.1.deepsee |
| deepseek | transcription | 2(d) | model error | 6,624/8,578 agree; 1,604 candidate-unknown, 285 candidate-shows-skipped, 62 project-unknown, 3 project-refuses; completed: 211 candidate-unknown, 1 candidate-shows-skipped | i2441 p. 3, Column (d). | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): it asks dc_paid of every entry (211 completed unknowns where the project hides the column) and shows an amount on a hidden column (genera |
| deepseek | transcription | 2(c) | model error | 7,833/8,578 agree; 680 candidate-unknown, 57 project-unknown, 5 candidate-refuses, 3 project-refuses; completed: 76 candidate-unknown | i2441 p. 3, Column (c). | As the prior ruling (`.transcription/archive/before-catalog-refresh-2026-11-03/`): no qualifying-person test; it reads dc_incapable and dc_over12_care for every entry aged 13 or more (76 completed unknowns on entries wit |
| deepseek | transcription | 27 | model error | 4,079/8,578 agree; 4,360 candidate-unknown, 102 candidate-shows-skipped, 20 project-unknown, 16 project-refuses, 1 candidate-refuses; completed: 1,644 candidate-unknown, 78 candidate-shows-skipped | f8863 p. 2, line 27; i8863 pp. 2-3. | The reply has no gate on an education credit being claimed: it asks dependent.edu_over of every entry (1,549 completed unknowns) and shows amounts where the project hides the line (completed candidate-shows-skipped, for  |
| deepseek | transcription | 28 | model error | 4,079/8,578 agree; 4,360 candidate-unknown, 102 candidate-shows-skipped, 20 project-unknown, 16 project-refuses, 1 candidate-refuses; completed: 1,644 candidate-unknown, 78 candidate-shows-skipped | f8863 p. 2, line 28; i8863 pp. 2-3. | The reply has no gate on an education credit being claimed: it asks dependent.edu_over of every entry (1,549 completed unknowns) and shows amounts where the project hides the line (completed candidate-shows-skipped, for  |
| deepseek | transcription | 29 | model error | 4,079/8,578 agree; 4,360 candidate-unknown, 102 candidate-shows-skipped, 20 project-unknown, 16 project-refuses, 1 candidate-refuses; completed: 1,644 candidate-unknown, 78 candidate-shows-skipped | f8863 p. 2, line 29; i8863 pp. 2-3. | The reply has no gate on an education credit being claimed: it asks dependent.edu_over of every entry (1,549 completed unknowns) and shows amounts where the project hides the line (completed candidate-shows-skipped, for  |
| deepseek | transcription | 30 | model error | 4,079/8,578 agree; 4,360 candidate-unknown, 102 candidate-shows-skipped, 20 project-unknown, 16 project-refuses, 1 candidate-refuses; completed: 1,644 candidate-unknown, 78 candidate-shows-skipped | f8863 p. 2, line 30; i8863 pp. 2-3. | The reply has no gate on an education credit being claimed: it asks dependent.edu_over of every entry (1,549 completed unknowns) and shows amounts where the project hides the line (completed candidate-shows-skipped, for  |
| deepseek | transcription | 31 | model error | 4,086/8,578 agree; 4,336 candidate-unknown, 115 candidate-shows-skipped, 24 project-unknown, 17 project-refuses; completed: 1,625 candidate-unknown, 87 candidate-shows-skipped | f8863 p. 2, line 31; i8863 pp. 2-3. | The reply has no gate on an education credit being claimed: it asks dependent.edu_over of every entry (1,549 completed unknowns) and shows amounts where the project hides the line (completed candidate-shows-skipped, for  |
| claude | render | 2(d) | ambiguity | render MISMATCH | amb.2025.dc_line30 (owner's decision, Stage 15 decision 6): column (d) shows each person's expenses including those paid with dependent care | The reviewer reads the rejected reading. As the prior ruling. Project stands. |
| deepseek | render | 2(d) | ambiguity | render MISMATCH | amb.2025.dc_line30 (owner ruling, Stage 15 decision 6, T-048); i2441 p. 3, Column (d). | As the prior ruling. Project stands. |

Counts: claude transcription model error 14, scope 5 (19); deepseek transcription model error 17, scope 2 (19); claude render ambiguity 1 (1); deepseek render ambiguity 1 (1). Errors introduced: none (BUG-0398 relabelled `dependent.dc_count`; its expression is unchanged). Reclassified: Claude `dependent.hoh_absence` (scope to model error: it now asks `dependent.kidnapped` of every entry); deepseek `dependent.ctc_child`, `dependent.ctc_amount` and `dependent.actc_amount` (scope to model error: the reply drops the filer's SSN valid for employment, household.ctc_ssn; completed generated 360 and 439 give $2,200 and $1,700 where the project gives $0, i1040gi p. 7). Findings: none.

## R2 round (2026-11-07, long questions restructured)

Subject after the long input questions of eleven dependent inputs (dependent.relationship, student, months, us_half, self_support, spouse_relative, qr_all_year, supported, parent_home_paid, dc_paid, edu_inst) were set as a one-line question with paragraphs and lists, meaning and words unchanged; no expression changed. Fresh whole-form replies of 2026-11-07 from claude-opus-5-5 (21 disagreements; dependent.eic_child and dependent.eic_ssn_child newly disagree) and deepseek-flash (20; dependent.dc_count newly disagrees, dependent.ptc_magi_counted now agrees). Rulings written with `tools/transcription/rule.py` from `/tmp/r2/adj/dependent.claude.rulings.json` and `/tmp/r2/adj/dependent.deepseek.rulings.json`; earlier rulings reused only where the reply makes the same deviation, and said so.

Triage: `../triage/dependent[.deepseek].json`, executable-triage-v2, rerun today (1,638 fixtures, 500 generated returns seed 20261026, 2,358 partial records from 40 bases, 7,537 comparisons per line); every completed-return difference was enumerated with the witness cap lifted (scratch `/tmp/r2/adj/dep/full/`) and traced with `--explain`. The deepseek reply's dependent.dc_count fails validation; its other lines were executed.

Wording: no difference was traced to the restructured questions. Every completed-return value difference traces to an input whose question did not change (dependent.citizen and canada_mexico, joint_return and married, f2441.care) or to the count design. Changes in the replies that touch a reworded input are noted, not attributed: the Claude reply no longer asks dependent.kidnapped (its note: the kidnapped-child exception's conditions are answered by no input) and treats residency as the months answer, which the project also does apart from its cited kidnap_residency refusal; the deepseek reply adds a born/died/placed residency route although the months question already applies that rule (one completed born_died question), and stops reading dependent.spouse_relative (no witness).

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | dependent.claimed | model error | 6,144/7,537 agree; 890 candidate-unknown, 316 project-refuses, 110 project-unknown, 72 value, 5 candidate-refuses; completed: 315 candidate-unknown, 9 value, 1 candidate-refuses | i1040gi p. 19, Step 4, question 3; p501 p. 21, Multiple Support Agreement | As the earlier rulings: joint_return asked of every entry (173 completed), multiple_support refused for every entry (120 completed; generated 126 refused), lawful for household_member (14); 9 values on married No/joint_return Yes records the interview cannot produce. Kidnapped question gone. |
| claude | transcription | dependent.ctc_child | model error | 7,025/7,537 agree; 344 candidate-unknown, 121 project-unknown, 27 project-refuses, 20 candidate-refuses; completed: 114 candidate-unknown, 1 candidate-refuses | p501 p. 21, Multiple Support Agreement; i1040gi p. 18, Step 3 | Class changes from scope: inherits the multiple-support refusal, 114 completed unknowns on qualifying children (project $2,200). No completed value. |
| claude | transcription | dependent.odc_person | model error | 6,209/7,537 agree; 865 candidate-unknown, 316 project-refuses, 72 value, 70 project-unknown, 5 candidate-refuses; completed: 305 candidate-unknown, 9 value, 1 candidate-refuses | i1040gi p. 19, Steps 4 and 5 | Inherits dependent.claimed (joint_return 171, multiple_support 120, lawful 14 completed unknowns; 9 values on the contradictory records). |
| claude | transcription | dependent.ctc_amount | model error | 7,025/7,537 agree; 344 candidate-unknown, 121 project-unknown, 27 project-refuses, 20 candidate-refuses; completed: 114 candidate-unknown, 1 candidate-refuses | f1040s8812 line 5; p501 p. 21 | Inherits dependent.ctc_child (114 completed unknowns, project $2,200). |
| claude | transcription | dependent.odc_amount | model error | 6,209/7,537 agree; 865 candidate-unknown, 316 project-refuses, 72 value, 70 project-unknown, 5 candidate-refuses; completed: 305 candidate-unknown, 9 value, 1 candidate-refuses | f1040s8812 line 7 | Inherits dependent.odc_person (9 values $500 against $0 on the contradictory records). |
| claude | transcription | dependent.actc_amount | model error | 7,025/7,537 agree; 344 candidate-unknown, 121 project-unknown, 27 project-refuses, 20 candidate-refuses; completed: 114 candidate-unknown, 1 candidate-refuses | f1040s8812 line 16b | Inherits dependent.ctc_child (114 completed unknowns, project $1,700). |
| claude | transcription | dependent.hoh_absence | model error | 7,180/7,537 agree; 328 project-refuses, 23 project-unknown, 5 candidate-refuses, 1 candidate-unknown; completed: 1 candidate-refuses, 1 candidate-unknown, 1 project-unknown | i1040gi p. 14, Test 2; p501 p. 9; p501 p. 21 | Kidnapped question gone; generated 126 dep_b (a qualifying child) refused by the multiple-support refusal. |
| claude | transcription | dependent.hoh_test2 | model error | 6,335/7,537 agree; 518 project-unknown, 329 candidate-unknown, 328 project-refuses, 22 value, 5 candidate-refuses; completed: 127 candidate-unknown, 82 project-unknown, 5 value, 1 candidate-refuses | i1040gi p. 14, Test 2; p501 p. 9 | As the earlier ruling (no part-year route; 78 absence_no_return project-unknowns on non-HOH returns); now joint_return (123 completed), multiple-support refusal, 5 values on the contradictory records. |
| claude | transcription | dependent.hoh_test1 | scope | 7,112/7,537 agree; 304 project-refuses, 117 project-unknown, 4 candidate-unknown; completed: 2 candidate-unknown, 1 project-unknown | i1040gi p. 14, Test 1 | As the earlier ruling: project refusals and partial-record unknowns only. |
| claude | transcription | dependent.eic_child | scope | 7,268/7,537 agree; 135 project-unknown, 82 candidate-unknown, 33 candidate-refuses, 19 project-refuses; completed: 10 project-unknown, 3 candidate-unknown | i1040gi p. 41, Step 3; p. 44 | Fresh (agreed at the last review; the reply dropped its kidnap and tiebreaker gates): refusals (project kidnap_eic, eic_tiebreak, married; reply divorced_rule) and 8 completed kidnapped project-unknowns on returns with no EIC. |
| claude | transcription | dependent.eic_ssn_child | scope | 7,280/7,537 agree; 129 project-unknown, 76 candidate-unknown, 33 candidate-refuses, 19 project-refuses; completed: 9 project-unknown, 2 candidate-unknown | i1040gi p. 46, Worksheet A, line 2 | Inherits dependent.eic_child. |
| claude | transcription | dependent.dc_qp | model error | 4,640/7,537 agree; 1,562 candidate-unknown, 1,256 value, 72 candidate-refuses, 5 project-unknown, 2 project-refuses; completed: 619 value, 308 candidate-unknown, 1 candidate-refuses | i2441 p. 1, Qualifying Person(s); p503 p. 3 | As the earlier ruling: no f2441.care condition (619 completed values, all care no); inherits claimed (joint_return, multiple_support, lawful). |
| claude | transcription | dependent.dc_count | model error | 1,496/7,537 agree; 4,349 value, 1,619 candidate-unknown, 73 candidate-refuses; completed: 2,046 value, 308 candidate-unknown, 1 candidate-refuses | i2441 p. 3, Line 2 | As the earlier ruling: 1-or-0 count by its own dc_qp (2,046 completed values, project 1, candidate 0). |
| claude | transcription | dependent.ptc_magi_counted | model error | 7,014/7,537 agree; 449 project-unknown, 73 candidate-refuses, 1 value; completed: 28 project-unknown, 1 candidate-refuses | i8962 p. 8, Line 2b; p501 p. 21 | Class changes from scope: 28 ptc_files project-unknowns on returns with no Form 8962 as before, but generated 126 dep_b (a qualifying child, project $0) is refused by the multiple-support refusal on a completed return. |
| claude | transcription | 2(d) | model error | 5,673/7,537 agree; 1,784 candidate-unknown, 72 candidate-refuses, 5 project-unknown, 2 project-refuses, 1 value; completed: 319 candidate-unknown, 1 candidate-refuses | i2441 p. 3, Column (d); p. 1 | As the earlier ruling: inherits dc_qp, 319 completed unknowns where the column is hidden. No amount differs. |
| claude | transcription | 2(c) | model error | 6,680/7,537 agree; 712 candidate-unknown, 72 candidate-refuses, 57 project-unknown, 13 candidate-shows-skipped, 2 project-refuses, 1 value; completed: 116 candidate-unknown, 4 candidate-shows-skipped, 1 candidate-refuses | i2441 p. 3, Column (c) | As the earlier ruling: 4 completed candidate-shows-skipped (generated 35, 355, 401, care no), 116 completed unknowns. |
| claude | transcription | 27 | model error | 4,591/7,537 agree; 2,858 candidate-unknown, 67 project-refuses, 12 project-unknown, 8 candidate-refuses, 1 value; completed: 866 candidate-unknown | f8863 p. 2, line 27; i8863 p. 3; p970 p. 11 | As the earlier ruling: edu asked of every entry (856 completed), edu_tin_issued required (10). |
| claude | transcription | 28 | model error | 4,591/7,537 agree; 2,858 candidate-unknown, 67 project-refuses, 12 project-unknown, 8 candidate-refuses, 1 value; completed: 866 candidate-unknown | f8863 p. 2, line 28; i8863 p. 3; p970 p. 11 | As the earlier ruling: edu asked of every entry (856 completed), edu_tin_issued required (10). |
| claude | transcription | 29 | model error | 4,591/7,537 agree; 2,858 candidate-unknown, 67 project-refuses, 12 project-unknown, 8 candidate-refuses, 1 value; completed: 866 candidate-unknown | f8863 p. 2, line 29; i8863 p. 3; p970 p. 11 | As the earlier ruling: edu asked of every entry (856 completed), edu_tin_issued required (10). |
| claude | transcription | 30 | model error | 4,591/7,537 agree; 2,858 candidate-unknown, 67 project-refuses, 12 project-unknown, 8 candidate-refuses, 1 value; completed: 866 candidate-unknown | f8863 p. 2, line 30; i8863 p. 3; p970 p. 11 | As the earlier ruling: edu asked of every entry (856 completed), edu_tin_issued required (10). |
| claude | transcription | 31 | model error | 4,586/7,537 agree; 2,864 candidate-unknown, 68 project-refuses, 12 project-unknown, 7 candidate-refuses; completed: 868 candidate-unknown | f8863 p. 2, line 31; i8863 p. 3; p970 p. 11 | As the earlier ruling: edu asked of every entry (856 completed), edu_tin_issued required (10); joint_return (2, project $9,553). |
| deepseek | transcription | dependent.claimed | model error | 6,234/7,537 agree; 483 candidate-unknown, 338 value, 316 project-refuses, 161 project-unknown, 5 candidate-refuses; completed: 200 value, 155 candidate-unknown, 3 project-unknown, 1 candidate-refuses | i1040gi p. 18, Step 2, q. 1; p. 19, Step 4, q. 2; p501 p. 21 | New: drops the citizenship test (200 completed values, project no, candidate yes; classm.s2.3.deepseek dep_c), the could-be-claimed test (sa.dependent) and the spouse_relative route. As the earlier ruling: multiple-support refusal on every entry (120 completed), lawful (14). |
| deepseek | transcription | dependent.ctc_child | model error | 7,361/7,537 agree; 97 candidate-unknown, 38 project-unknown, 28 project-refuses, 12 value, 1 candidate-refuses; completed: 6 candidate-unknown | i1040gi p. 7; p. 18, Step 3, q. 4; Step 2, q. 4 | As the earlier ruling (no household.ctc_ssn): now household.taxpayer_work_ssn (stage13.ctc_spouse_ssn, ctc_spouse_no_id) and no sa.dependent test (stage8.single.filer_is_dependent); 12 values, none completed. |
| deepseek | transcription | dependent.odc_person | model error | 6,658/7,537 agree; 487 candidate-unknown, 316 project-refuses, 55 project-unknown, 16 value, 5 candidate-refuses; completed: 143 candidate-unknown, 1 candidate-refuses | i1040gi p. 19, Steps 4 and 5 | As the earlier ruling: inherits claimed (multiple_support 123, lawful 14 completed unknowns; generated 126 refused). |
| deepseek | transcription | dependent.ctc_amount | model error | 7,361/7,537 agree; 97 candidate-unknown, 38 project-unknown, 28 project-refuses, 12 value, 1 candidate-refuses; completed: 6 candidate-unknown | f1040s8812 line 5; i1040gi p. 7 | Inherits dependent.ctc_child; values on incomplete records only. |
| deepseek | transcription | dependent.odc_amount | model error | 6,658/7,537 agree; 487 candidate-unknown, 316 project-refuses, 55 project-unknown, 16 value, 5 candidate-refuses; completed: 143 candidate-unknown, 1 candidate-refuses | f1040s8812 line 7 | Inherits dependent.odc_person (143 completed unknowns). |
| deepseek | transcription | dependent.actc_amount | model error | 7,361/7,537 agree; 97 candidate-unknown, 38 project-unknown, 28 project-refuses, 12 value, 1 candidate-refuses; completed: 6 candidate-unknown | f1040s8812 line 16b | Inherits dependent.ctc_child. |
| deepseek | transcription | dependent.hoh_absence | model error | 6,897/7,537 agree; 385 project-refuses, 251 candidate-unknown, 3 value, 1 project-unknown; completed: 38 candidate-unknown | i1040gi p. 14, Test 2; p501 p. 9 | As the earlier ruling (no Test 2 condition); now a copy of absence_no_return (was its negation): 38 completed unknowns. |
| deepseek | transcription | dependent.hoh_test2 | model error | 6,470/7,537 agree; 412 candidate-unknown, 317 project-refuses, 228 value, 105 project-unknown, 5 candidate-refuses; completed: 177 value, 100 candidate-unknown, 1 candidate-refuses, 1 project-unknown | i1040gi p. 14, Test 2; i1040gi pp. 18-19 (citizenship) | New: the unclaimed-qualifying-child defect is gone; inherits the dropped citizenship test (177 completed values, project false, candidate true), multiple-support refusal (66 completed). |
| deepseek | transcription | dependent.hoh_test1 | model error | 6,520/7,537 agree; 607 candidate-unknown, 296 project-refuses, 97 project-unknown, 14 candidate-refuses, 3 value; completed: 137 candidate-unknown, 2 value, 1 candidate-refuses, 1 project-unknown | i1040gi p. 14, Test 1 | As the earlier ruling: multiple-support refusal on every entry (123 completed unknowns); new: 2 completed values from the dropped citizenship test (generated 35, 179). |
| deepseek | transcription | dependent.eic_child | scope | 7,364/7,537 agree; 82 candidate-unknown, 52 project-unknown, 33 candidate-refuses, 6 project-refuses; completed: 8 project-unknown, 3 candidate-unknown | i1040gi p. 41, Step 3; p. 44 | As the earlier ruling: refusals and 8 completed kidnapped project-unknowns on returns with no EIC. |
| deepseek | transcription | dependent.eic_ssn_child | scope | 7,358/7,537 agree; 88 candidate-unknown, 52 project-unknown, 33 candidate-refuses, 6 project-refuses; completed: 8 project-unknown, 4 candidate-unknown | i1040gi p. 46, Worksheet A, line 2 | As the earlier ruling: inherits dependent.eic_child. |
| deepseek | transcription | dependent.dc_qp | model error | 7,099/7,537 agree; 246 candidate-unknown, 135 value, 52 candidate-refuses, 3 project-unknown, 2 project-refuses; completed: 5 candidate-unknown | i2441 p. 1, Qualifying Person(s), item 1 | The earlier no-f2441.care defect is gone; new: under-13 route without the qualifying-child test (135 values on refused returns, classm.dependent.3.deepseek dep_a). No completed value. |
| deepseek | transcription | dependent.dc_count | model error | not executed; 7,537 candidate-invalid | i2441 p. 3, Line 2 | Fresh (agreed at the last review): the declaration fails validation (sum_over in a per-entry line, "collection parent binding mismatch"); not executed. |
| deepseek | transcription | 2(d) | model error | 5,195/7,537 agree; 1,964 candidate-unknown, 313 candidate-shows-skipped, 62 project-unknown, 3 project-refuses; completed: 333 candidate-unknown, 1 candidate-shows-skipped | i2441 p. 3, Column (d) | As the earlier ruling: dc_paid of every entry (333 completed unknowns), generated 360 dep_b $5,920 on a hidden column. |
| deepseek | transcription | 2(c) | model error | 6,657/7,537 agree; 820 candidate-unknown, 57 project-unknown, 3 project-refuses; completed: 110 candidate-unknown | i2441 p. 3, Column (c) | As the earlier ruling: no qualifying-person test (109 completed dc_incapable unknowns). |
| deepseek | transcription | 27 | model error | 4,321/7,537 agree; 3,100 candidate-unknown, 71 project-refuses, 37 project-unknown, 6 candidate-shows-skipped, 2 value; completed: 967 candidate-unknown, 2 candidate-shows-skipped | f8863 p. 2, line 27; i8863 p. 2; p970 p. 11 | As the earlier ruling: no claimed-dependent gate (880 completed edu unknowns; generated 135 and 311 shown where hidden); edu_tin_issued required (85); edu_over refusal gone. |
| deepseek | transcription | 28 | model error | 4,321/7,537 agree; 3,100 candidate-unknown, 71 project-refuses, 37 project-unknown, 6 candidate-shows-skipped, 2 value; completed: 967 candidate-unknown, 2 candidate-shows-skipped | f8863 p. 2, line 28; i8863 p. 2; p970 p. 11 | As the earlier ruling: no claimed-dependent gate (880 completed edu unknowns; generated 135 and 311 shown where hidden); edu_tin_issued required (85); edu_over refusal gone. |
| deepseek | transcription | 29 | model error | 4,321/7,537 agree; 3,100 candidate-unknown, 71 project-refuses, 37 project-unknown, 6 candidate-shows-skipped, 2 value; completed: 967 candidate-unknown, 2 candidate-shows-skipped | f8863 p. 2, line 29; i8863 p. 2; p970 p. 11 | As the earlier ruling: no claimed-dependent gate (880 completed edu unknowns; generated 135 and 311 shown where hidden); edu_tin_issued required (85); edu_over refusal gone. |
| deepseek | transcription | 30 | model error | 4,321/7,537 agree; 3,100 candidate-unknown, 71 project-refuses, 37 project-unknown, 6 candidate-shows-skipped, 2 value; completed: 967 candidate-unknown, 2 candidate-shows-skipped | f8863 p. 2, line 30; i8863 p. 2; p970 p. 11 | As the earlier ruling: no claimed-dependent gate (880 completed edu unknowns; generated 135 and 311 shown where hidden); edu_tin_issued required (85); edu_over refusal gone. |
| deepseek | transcription | 31 | model error | 4,322/7,537 agree; 3,105 candidate-unknown, 73 project-refuses, 37 project-unknown; completed: 967 candidate-unknown | f8863 p. 2, line 31; i8863 p. 2; p970 p. 11 | As the earlier ruling: no claimed-dependent gate (880 completed edu unknowns); edu_tin_issued required (86); edu_over refusal gone. |

Counts: claude transcription model error 18, scope 3 (21); deepseek transcription model error 18, scope 2 (20). Reclassified: Claude dependent.ctc_child, ctc_amount, actc_amount (scope to model error: the reply's multiple-support refusal now reaches qualifying children on completed returns), dependent.ptc_magi_counted (scope to model error: generated 126 refused). Newly ruled: Claude dependent.eic_child and eic_ssn_child (scope); deepseek dependent.dc_count (model error, validation). Errors introduced: none. Findings: none.


## Formal-gates round (2026-11-07, American opportunity credit test in the form's order)

Subject after `dependent.edu_aoc` was rewritten from one all-test into a nested choice in the form's order (lines 23 to 26, then
`household.all_tin`, then the EIN answer; BUG-0460), so that no question is reached past an unanswered one; no value changes on a
complete return. dependent has partial-input cases, so the review was rerun whole: a fresh reply of 2026-11-07 from claude-opus-5-5
(19 disagreements; dependent.eic_child and dependent.eic_ssn_child now agree). Rulings written with `tools/transcription/rule.py`;
triage counts from a scratch run of `tools/transcription/triage.mjs` with the witness cap lifted (1,640 fixtures, 500 generated returns
seed 20261026, 2,167 partial records). Every ruling is model error on the reply's multiple-support refusal placed on every entry
(completed generated 126 dep_b, a qualifying child), with the line's other differences as stated.

| family | kind | line | class | triage | source | note |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | dependent.claimed | model error | 5,817/7,218 agree; 1,047 candidate-unknown, 179 project-refuses, 145 project-unknown, 24 value, 6 candidate-refuses; completed: 316 candidate-unknown, 9 value, 1 candidate-refuses | i1040gi p. 21, Multiple support agreements; Married person | multiple_support and joint_return read of every entry; 9 completed values are unmarried persons answered as on a joint return. |
| claude | transcription | dependent.ctc_child | model error | 6,722/7,218 agree; 326 candidate-unknown, 119 project-unknown, 30 project-refuses, 21 candidate-refuses; completed: 97 candidate-unknown, 1 candidate-refuses | i1040gi p. 21 | multiple_support of every entry; no value differs. |
| claude | transcription | dependent.odc_person | model error | 5,969/7,218 agree; 987 candidate-unknown, 179 project-refuses, 53 project-unknown, 24 value, 6 candidate-refuses; completed: 306 candidate-unknown, 9 value, 1 candidate-refuses | i1040gi p. 21 | As dependent.claimed. |
| claude | transcription | dependent.ctc_amount | model error | 6,722/7,218 agree; 326 candidate-unknown, 119 project-unknown, 30 project-refuses, 21 candidate-refuses; completed: 97 candidate-unknown, 1 candidate-refuses | i1040gi p. 21 | As dependent.ctc_child. |
| claude | transcription | dependent.odc_amount | model error | 5,969/7,218 agree; 987 candidate-unknown, 179 project-refuses, 53 project-unknown, 24 value, 6 candidate-refuses; completed: 306 candidate-unknown, 9 value, 1 candidate-refuses | i1040gi p. 21 | As dependent.claimed. |
| claude | transcription | dependent.actc_amount | model error | 6,722/7,218 agree; 326 candidate-unknown, 119 project-unknown, 30 project-refuses, 21 candidate-refuses; completed: 97 candidate-unknown, 1 candidate-refuses | i1040gi p. 21 | As dependent.ctc_child. |
| claude | transcription | dependent.hoh_absence | model error | 7,005/7,218 agree; 180 project-refuses, 16 project-unknown, 11 candidate-unknown, 6 candidate-refuses; completed: 4 candidate-unknown, 3 project-unknown, 1 candidate-refuses | i1040gi p. 21 | multiple_support refusal; other differences are partials or answers the interview completes without. |
| claude | transcription | dependent.hoh_test2 | model error | 6,377/7,218 agree; 466 candidate-unknown, 180 project-refuses, 173 project-unknown, 16 value, 6 candidate-refuses; completed: 163 candidate-unknown, 28 project-unknown, 3 value, 1 candidate-refuses | i1040gi p. 21; p. 14, Test 2 | As dependent.claimed (3 completed values, unmarried joint-return answers). |
| claude | transcription | dependent.hoh_test1 | model error | 6,450/7,218 agree; 522 candidate-unknown, 157 project-refuses, 75 project-unknown, 14 candidate-refuses; completed: 105 candidate-unknown, 1 candidate-refuses, 1 project-unknown | i1040gi p. 21; p. 14, Test 1 | multiple_support of every entry; Test 1 reading as the prior ruling. |
| claude | transcription | dependent.dc_qp | model error | 3,585/7,218 agree; 2,009 candidate-unknown, 1,448 value, 174 candidate-refuses, 2 project-refuses; completed: 568 value, 332 candidate-unknown, 1 candidate-refuses | i1040gi p. 21; i2441 p. 1, Qualifying Person(s) | New: drops f2441.care (568 completed values, no care expenses); dc_incapable of every entry. |
| claude | transcription | dependent.dc_count | model error | 1,557/7,218 agree; 3,416 value, 2,070 candidate-unknown, 175 candidate-refuses; completed: 1,687 value, 332 candidate-unknown, 1 candidate-refuses | i1040gi p. 21; i2441 p. 3, Line 2 | As the prior ruling (test applied where summed); plus dc_qp's defects. |
| claude | transcription | dependent.ptc_magi_counted | model error | 6,556/7,218 agree; 458 project-unknown, 203 candidate-refuses, 1 value; completed: 50 project-unknown, 1 candidate-refuses | i1040gi p. 21; i8962 p. 8, Line 2b | As the prior ruling (ptc_files not asked without Form 8962); plus the refusal. |
| claude | transcription | 2(d) | model error | 4,693/7,218 agree; 2,349 candidate-unknown, 174 candidate-refuses, 2 project-refuses; completed: 343 candidate-unknown, 1 candidate-refuses | i1040gi p. 21; i2441 p. 3, Line 2 | As the prior ruling; plus dc_qp's defects. |
| claude | transcription | 2(c) | model error | 5,976/7,218 agree; 998 candidate-unknown, 174 candidate-refuses, 54 project-unknown, 14 candidate-shows-skipped, 2 project-refuses; completed: 145 candidate-unknown, 4 candidate-shows-skipped, 1 candidate-refuses | i1040gi p. 21; i2441 p. 3, Column (c) | Box only; plus dc_qp's defects. |
| claude | transcription | 27 | model error | 3,247/7,218 agree; 3,739 candidate-unknown, 189 candidate-refuses, 42 project-refuses, 1 value; completed: 1,080 candidate-unknown, 1 candidate-refuses | f8863 p. 2, line 27; p970 p. 11 | edu_over of every entry; ITIN applied for (T-113). |
| claude | transcription | 28 | model error | 3,247/7,218 agree; 3,739 candidate-unknown, 189 candidate-refuses, 42 project-refuses, 1 value; completed: 1,080 candidate-unknown, 1 candidate-refuses | f8863 p. 2, line 28; p970 p. 11 | As 27. |
| claude | transcription | 29 | model error | 3,247/7,218 agree; 3,739 candidate-unknown, 189 candidate-refuses, 42 project-refuses, 1 value; completed: 1,080 candidate-unknown, 1 candidate-refuses | f8863 p. 2, line 29; p970 p. 11 | As 27. |
| claude | transcription | 30 | model error | 3,247/7,218 agree; 3,739 candidate-unknown, 189 candidate-refuses, 42 project-refuses, 1 value; completed: 1,080 candidate-unknown, 1 candidate-refuses | f8863 p. 2, line 30; p970 p. 11 | As 27. |
| claude | transcription | 31 | model error | 3,241/7,218 agree; 3,746 candidate-unknown, 188 candidate-refuses, 43 project-refuses; completed: 1,082 candidate-unknown, 1 candidate-refuses | f8863 p. 2, line 31; i8863 p. 3 | As 27; amount is aqee ws4_llc. |

Counts: claude transcription model error 19 (19). Errors introduced: none. Findings: none.


## Round 3 (2026-11-07, whole-form rerun after the education tests were put in the form's order)

Whole-form rerun of dependent (claude-opus-5-5) after `edu_student` and `edu_aoc` became nested choices (BUG-0460) and line 31 stopped binding `edu_mat` (BUG-0462). Triage: `../triage/dependent.json`, executable-triage-v2, 1,643 fixtures, 500 generated returns seed 20261026, 2,157 partial records. Rulings marked carried were taken from an earlier revision of the log with an identical disagreement (both trees) on a line whose own reading path is unchanged; the others restate the earlier reasoning against this round's triage or rule new objections.

| family | kind | line | class | triage | source | note |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | dependent.claimed | model error | 6,679/7,119 agree; 179 candidate-unknown, 161 project-unknown, 99 project-refuses, 1 candidate-refuses; completed: 75 candidate-unknown | i1040gi p. 19, Step 4 | repeat, re-ruled |
| claude | transcription | dependent.odc_person | model error | 6,765/7,119 agree; 167 candidate-unknown, 99 project-refuses, 87 project-unknown, 1 candidate-refuses; completed: 69 candidate-unknown | i1040gi p. 19, Steps 4 and 5 | repeat, re-ruled |
| claude | transcription | dependent.odc_amount | model error | 6,765/7,119 agree; 167 candidate-unknown, 99 project-refuses, 87 project-unknown, 1 candidate-refuses; completed: 69 candidate-unknown | f1040s8812 line 7 | repeat, re-ruled |
| claude | transcription | dependent.ctc_child | scope | 6,931/7,119 agree; 124 project-unknown, 62 project-refuses, 2 candidate-refuses; completed: none | i1040gi p. 18, Step 3, questions 1 to 4 | repeat, re-ruled |
| claude | transcription | dependent.ctc_amount | scope | 6,931/7,119 agree; 124 project-unknown, 62 project-refuses, 2 candidate-refuses; completed: none | f1040s8812 line 5, "Multiply line 4 by $2,200" | repeat, re-ruled |
| claude | transcription | dependent.actc_amount | scope | 6,931/7,119 agree; 124 project-unknown, 62 project-refuses, 2 candidate-refuses; completed: none | f1040s8812 line 16b | repeat, re-ruled |
| claude | transcription | dependent.hoh_absence | scope | 6,977/7,119 agree; 111 project-refuses, 30 project-unknown, 1 candidate-refuses; completed: none | i1040gi p. 14, Test 2; p501 p. 9, Temporary absences | repeat, re-ruled |
| claude | transcription | dependent.hoh_test2 | model error | 6,545/7,119 agree; 454 project-unknown, 111 project-refuses, 7 value, 1 candidate-refuses, 1 candidate-unknown; completed: 63 project-unknown | i1040gi p. 14, Test 2; p501 p. 9, Temporary absences and Death or birth | repeat, re-ruled |
| claude | transcription | dependent.hoh_test1 | scope | 6,953/7,119 agree; 88 project-unknown, 78 project-refuses; completed: none | i1040gi p. 14, Test 1, "your parent whom you can claim as a dependent, except under a multiple support agreement" | repeat, re-ruled |
| claude | transcription | dependent.eic_child | scope | 6,826/7,119 agree; 269 project-unknown, 19 project-refuses, 5 candidate-refuses; completed: 21 project-unknown | i1040gi p. 41, Step 3; p. 44, Qualifying child of more than one person and Married child | repeat, re-ruled |
| claude | transcription | dependent.eic_ssn_child | scope | 6,829/7,119 agree; 266 project-unknown, 19 project-refuses, 5 candidate-refuses; completed: 20 project-unknown | i1040gi p. 46, Worksheet A, line 2 | repeat, re-ruled |
| claude | transcription | dependent.dc_qp | model error | 3,322/7,119 agree; 2,026 candidate-unknown, 1,605 value, 150 candidate-refuses, 13 project-unknown, 3 project-refuses; completed: 602 value, 348 candidate-unknown | i2441 p. 1, Qualifying Person(s), "A qualifying child under age 13 whom you can claim as a dependent"; p503 p. 3 | repeat, re-ruled |
| claude | transcription | dependent.ptc_magi_counted | scope | 6,302/7,119 agree; 617 project-unknown, 199 candidate-refuses, 1 value; completed: 126 project-unknown | i8962 p. 8, Line 2b, dependents "who are required to file" | repeat, re-ruled |
| claude | transcription | 2(d) | model error | 4,201/7,119 agree; 2,751 candidate-unknown, 150 candidate-refuses, 13 project-unknown, 3 project-refuses, 1 value; completed: 461 candidate-unknown | i2441 p. 3, Column (d); p. 1, Qualifying Person(s) | repeat, re-ruled |
| claude | transcription | 2(c) | model error | 5,539/7,119 agree; 1,352 candidate-unknown, 150 candidate-refuses, 59 project-unknown, 15 candidate-shows-skipped, 3 project-refuses, 1 value; completed: 215 candidate-unknown, 4 candidate-shows-skipped | i2441 p. 3, Column (c) | repeat, re-ruled |
| claude | transcription | 27 | model error | 3,198/7,119 agree; 3,643 candidate-unknown, 192 candidate-refuses, 83 project-unknown, 2 project-refuses, 1 value; completed: 922 candidate-unknown | f8863 p. 2, line 27; i8863 p. 3; p970 p. 11 | repeat, re-ruled |
| claude | transcription | 28 | model error | 3,198/7,119 agree; 3,643 candidate-unknown, 192 candidate-refuses, 83 project-unknown, 2 project-refuses, 1 value; completed: 922 candidate-unknown | f8863 p. 2, line 28; i8863 p. 3; p970 p. 11 | repeat, re-ruled |
| claude | transcription | 29 | model error | 3,198/7,119 agree; 3,643 candidate-unknown, 192 candidate-refuses, 83 project-unknown, 2 project-refuses, 1 value; completed: 922 candidate-unknown | f8863 p. 2, line 29; i8863 p. 3; p970 p. 11 | repeat, re-ruled |
| claude | transcription | 30 | model error | 3,198/7,119 agree; 3,643 candidate-unknown, 192 candidate-refuses, 83 project-unknown, 2 project-refuses, 1 value; completed: 922 candidate-unknown | f8863 p. 2, line 30; i8863 p. 3; p970 p. 11 | repeat, re-ruled |
| claude | transcription | 31 | model error | 3,193/7,119 agree; 3,649 candidate-unknown, 191 candidate-refuses, 83 project-unknown, 3 project-refuses; completed: 922 candidate-unknown | f8863 p. 2, line 31; i8863 p. 3, Who cannot claim a credit | repeat, re-ruled |
| claude | render | 23 | ambiguity | render MISMATCH | amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29). i8863 p. 1: "After January 31, 2026, but before you file the return, you or the student must requ... | |
| claude | render | 24 | ambiguity | render MISMATCH | amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29). i8863 p. 1: "After January 31, 2026, but before you file the return, you or the student must requ... | |
| claude | render | 25 | ambiguity | render MISMATCH | amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29). i8863 p. 1: "After January 31, 2026, but before you file the return, you or the student must requ... | |
| claude | render | 26 | ambiguity | render MISMATCH | amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29). i8863 p. 1: "After January 31, 2026, but before you file the return, you or the student must requ... | |
| claude | render | 27 | ambiguity | render MISMATCH | amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29). i8863 p. 1: "After January 31, 2026, but before you file the return, you or the student must requ... | |
| claude | render | 28 | ambiguity | render MISMATCH | amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29). i8863 p. 1: "After January 31, 2026, but before you file the return, you or the student must requ... | |
| claude | render | 29 | ambiguity | render MISMATCH | amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29). i8863 p. 1: "After January 31, 2026, but before you file the return, you or the student must requ... | |
| claude | render | 30 | ambiguity | render MISMATCH | amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29). i8863 p. 1: "After January 31, 2026, but before you file the return, you or the student must requ... | |
| claude | render | 31 | ambiguity | render MISMATCH | amb.2025.edu_1098t_date (owner decision D7(d), 2026-10-29). i8863 p. 1: "After January 31, 2026, but before you file the return, you or the student must requ... | |
| claude | render | 2(d) | ambiguity | render MISMATCH | amb.2025.dc_line30 (owner's decision, Stage 15 decision 6) | |
| claude | render | 2(c) | model error | render MISMATCH | i2441 p. 1, Qualifying Person(s), "or could claim as a dependent except" | |
| deepseek | render | 2(d) | ambiguity | render MISMATCH | amb.2025.dc_line30 (owner's decision, Stage 15 decision 6) | |

Counts: claude render ambiguity 10, model error 1; claude transcription model error 12, scope 8; deepseek render ambiguity 1. Errors introduced: none. Findings: none.
