# Adjudication — scope

Method: `README.md` in this directory. Earlier rulings were made in the logs' sidecars before Stage 18 (archived in
`.transcription/archive/before-stage18-2026-10-28/`); no summary was kept for them.

## Stage 18 (superseded subject)

Subject after Stage 18 (`scope.credits` wording: "the net premium tax credit this tool figures on Form 8962 from your
Forms 1095-A (Schedule 3 line 9)"). Only the deepseek render log has open sections. The model was given Form 1040
pp. 1-2 and i1040gi p. 14. Rulings in `.transcription/proposed/stage18/render.scope.deepseek.json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| deepseek | render | schedule1 | interface gap | UNCLEAR | f1040 lines 8, 10; f1040s1 (earlier rulings) | Schedule 1 not given; question unchanged and checked before. |
| deepseek | render | credits | interface gap | UNCLEAR | f1040s3 p. 1, lines 3, 6a-6z, 9 | Schedule 3 not given; the new wording matches `s3.line9`. |
| deepseek | render | other_income | interface gap | UNCLEAR | f1040 lines 1b-1h | Defining text not given; unchanged. |
| deepseek | render | other_line16 | interface gap | UNCLEAR | f1040 line 16 | Listed forms not given; unchanged. |
| deepseek | render | ready | finding (F3) | UNCLEAR | i1040gi p. 14; i1040gi p. 117, Line 9 | MFS refusal right; the scope.credits refusal remedy still says "entered from Form 8962". |

Findings: one, F3 in `.transcription/proposed/stage18/scope.findings.md` (cosmetic, a refusal message): the
`scope.credits` remedy (scope.yaml, f1040.yaml twice, s3.yaml) still calls the premium tax credit "entered from Form
8962". The question's own Stage 18 wording is right.

## Stage 19 (superseded subject)

Subject after Stage 19. `scope.credits` now lists "the education credits this tool figures on Form 8863 (the
American opportunity and lifetime learning credits)" as supported. Its refusal now reads "Other credit forms
(Schedule 3 lines 6a to 6z; Form 1040 lines 30 and 31)", and the remedy names "the net premium tax credit figured on
Form 8962 and the education credits (Form 8863)" (BUG-0193; Stage 18 F3 fixed). The transcription logs have no open
sections. In the render reviews both models were given Form 1040 pp. 1-2 and i1040gi p. 14 only. Full ruling text is
in `.transcription/proposed/stage19/render.scope[.deepseek].json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| both | render | schedule1 | interface gap | UNCLEAR | f1040 lines 8, 10; f1040s1 (earlier rulings) | Schedule 1 not given; unchanged. |
| both | render | credits | interface gap | UNCLEAR | f1040s3 p. 1, lines 3, 6a-6z, 9; f1040 line 29 | Schedule 3 not given. The new wording matches s3.line3 and f1040.line29, and the refusal and remedy are current. The refused education situations have their own screens. |
| deepseek | render | other_income | interface gap | UNCLEAR | f1040 lines 1b-1h; i1040gi p. 115 | Unchanged. Its nonresident alien clause refuses more widely than p. 115's bar, which is scope. |
| deepseek | render | other_line16 | interface gap | UNCLEAR | f1040 line 16 | Unchanged. It keeps education credit recapture refused (D1). |
| deepseek | render | ready | interface gap | UNCLEAR | i1040gi p. 14 | The married filing separately refusal is right; F3's stale remedy is fixed. |

Findings: none for scope in Stage 19.

## Fix round 2 (superseded subject)

Subject after BUG-0232 (`scope.other_line16` states the Form 8615 conditions) and BUG-0233 (`scope.schedule1` names
ministers, members of religious orders without a vow of poverty and Christian Science practitioners). Both transcription
logs and the deepseek render log have no open section. The Claude render model was given Form 1040 pp. 1-2 and i1040gi
pp. 14, 36 and 43, and judged both changed questions MATCH against pp. 36 and 43. Full ruling text:
`.transcription/proposed/fixr2/render.scope.json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | schedule1 | interface gap | UNCLEAR | f1040 lines 8, 10; i1040gi p. 43, Clergy | Schedule 1 not given; the clergy wording quotes p. 43. |
| claude | render | credits | interface gap | UNCLEAR | f1040s3 p. 1 | Schedule 3 not given; question unchanged. |

Fix check: the Form 8615 gloss matches i1040gi p. 36 conditions 1 to 5 ("didn't have earned income that was more than half
of your support" as "earned income of not more than half your support"; "at least age 19 but under age 24" as "19 to 23");
the clergy wording is p. 43 verbatim. Both widen refusing screens. No error introduced. Findings: none.

## Backlog round (superseded subject)
Subject after person-dep PENDING-5: `scope.schedule1` says "a church or qualified church-controlled organization" and cites i1040sse p. 1. The three transcription logs (claude, deepseek, gpt) and the Claude render log have no open section; the deepseek render model was given Form 1040, i1040gi pp. 14, 36, 43 and i1040sse.

Triage: `../triage/<stem>.json`, executable-triage-v2, rerun today with `tools/transcription/triage.py` (1,495 fixtures, 500 generated returns seed 20261026, partial records per form); every completed-return difference was enumerated with the witness cap lifted in a scratch run (`/tmp/adj-bklg-person-scope-household/`), and the printed amounts a helper could reach were checked where the ruling says so. `fixtures/2025/classm*.json` were rewritten by a concurrent class M run at 15:14 while this round was adjudicated; witnesses on `classm.*` cases may not rebuild identically from the current files. Full ruling text: `.transcription/proposed/bklg/<kind>.<stem>.json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| deepseek | render | schedule1 | scope | render MISMATCH | i1040sse p. 1, Employees of Churches and Church Organizations; i1040gi p. 43, Clergy | The objection is that statutory-employee, clergy and church-employee income go to Schedule SE rather than Schedule 1 |
| deepseek | render | credits | interface gap | render UNCLEAR | f1040s3 p. 1 (Part I lines 1 to 8, line 9) | The pages given (Form 1040, i1040gi pp. 14, 36, 43, i1040sse) omit Schedule 3 and the credit instructions; question unchanged and checked in earlier rounds against ... |
| deepseek | render | other_income | interface gap | render UNCLEAR | f1040 lines 1b-1h; i1040gi p. 115 | The defining instructions were not given; question unchanged. |
| deepseek | render | other_line16 | interface gap | render UNCLEAR | f1040 line 16; i1040gi p. 36 | The reviewer confirms the Form 8615 conditions on p. 36; the other listed forms' text was not given; question unchanged. |
| deepseek | render | ready | interface gap | render UNCLEAR | i1040gi p. 14. scope.ready is the whole-return readiness gate (the constant true carrying the scope refusals,  |  |

Counts: deepseek render scope 1, interface gap 4. Fix check: the church wording matches i1040sse p. 1. Errors introduced: none. Findings: none.

## Refresh round

Subject after the refresh-round fixes BUG-0391 to BUG-0401 (for these forms: BUG-0392 `person.sav_claimed` asked whenever education expenses are paid; BUG-0394 `person.educator_expenses` exclusions; BUG-0398 `household.taxpayer_work_ssn` cites and the `dependent.dc_count` label; BUG-0393 `scope.other_income` disaster distributions), transcription prompt `source-only-computation-v3`. Fresh replies of claude-opus-5-5 and deepseek-flash. Rulings in `.transcription/proposed/rf/` (`transcription.<stem>.json`, `render.<stem>.json`); prior rulings reused where the line, the disagreement and the evidence are the same, re-checked against `.transcription/archive/before-catalog-refresh-2026-11-03/`.

Triage: `../triage/<stem>.json`, executable-triage-v2, rerun today with `tools/transcription/triage.py` (1,565 fixtures, 500 generated returns seed 20261026, partial records per form); every completed-return difference was enumerated with the witness cap lifted in a scratch run (`/tmp/adj-rf-pers/full/`), and witnesses were traced with `--explain` where a ruling names one.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| deepseek | render | schedule1 | interface gap | render MISMATCH | The reviewer says the pages given cite only Form 1040 lines 8 and 10 from Schedule 1, so it cannot verify the listed items; the deciding tex | The prior scope ruling on the listed clergy, church and statutory-employee items stands (i1040sse p. 1; the question names them, so the filer answers Yes and is refused). Project stands. |
| deepseek | render | credits | interface gap | render MISMATCH | f1040s3 p. 1 (Part I lines 1 to 8, line 3 from Form 8863; Part II line 9, Form 8962). | The pages given lack Schedule 3 and the listed credits' instructions: a coverage gap of the review. As the prior ruling. Project stands. |
| deepseek | render | other_income | interface gap | render MISMATCH | f1040 (2025) lines 1b to 1h; p575 p. 35, "you can include $6,000 in your income in 2023, 2024, and 2025". | The pages given cover Form 1040 and the p575 disaster-distribution excerpt only; the other listed items are not decided there: a coverage gap. Checked the refresh change (BUG-0393): the clause names the 2025 part of a qu |
| deepseek | render | other_line16 | interface gap | render MISMATCH | f1040 (2025) line 16. | The reviewer confirms the Form 8615 conditions; the pages given lack the other listed items (Form 8814, Form 4972, section 962, Form 8621, Form 8978, education credit recapture): a coverage gap. As the prior ruling. Proj |
| deepseek | render | ready | interface gap | render MISMATCH | The MFS refusal matches i1040gi p. 14, Married Filing Separately; the other screens are filer-answered declarations whose items are cited on | As the prior ruling. Project stands. |

Counts: deepseek render interface gap 5 (5). Errors introduced: none (BUG-0393's `scope.other_income` clause, a qualified disaster recovery distribution received in 2023 or 2024 or a 2025 repayment, leaves a 2025 distribution to `retirement.special`). Reclassified: deepseek `schedule1` (scope to interface gap: the reviewer now objects only that the pages lack Schedule 1). The transcription logs have no open section. Findings: none.

## Landing round (2026-11-14)

Pass 1ad4bbd67c02 (lines scope.has_w2, scope.reservist_repaid_if_armed_forces, scope.excess_deferral_if_w2, scope.schedule1, scope.other_income, scope.other_line16). Evidence: triage record `.transcription/triage/2025/scope.json` (executable-triage-v2; 4,036 comparisons per line), read with the source, `forms/2025/scope.yaml` and the readers of the three screens (`f1040`, `carloan`, `f2441`, `eic`). Rulings text in `/tmp/land3-adj5/scope.json` (lane land3-adj5).

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | scope.reservist_repaid_if_armed_forces | representation | 3,997/4,036; 39 project-unknown; no value | i1040gi p. 95, Line 20 | Equivalent conjunction of gate and question. |
| claude | transcription | scope.schedule1 | model error | 3,592/4,036; 77 value (refused returns, project true / reply false); 37 candidate-unknown (5 completed) | i1040se p. 1; i1040sf p. 2; i1040gi p. 25 (statutory employee), Line 8z | Leaves rental, K-1, farm, clergy/church, statutory-employee and recovery items out of the Schedule 1 screen that carloan, f2441 and f1040 rely on. |
| claude | transcription | scope.other_income | model error | 3,503/4,036; 63 value (refused returns); 279 candidate-unknown (37 completed) | i1040gi p. 8 (nonresident aliens), p. 23 (chapter 11), p. 95 (Line 20); i2441 p. 5 | Leaves out nonresident status (named in the label), chapter 11, reservist repayments and other dependent care benefits. |
| claude | transcription | scope.other_line16 | model error | 3,861/4,036; 16 value (refused; mutation.m3.scope.l16_cfc and ungated generated answers); 75 candidate-unknown (14 completed) | i1040gi, Line 16, "Tax with respect to a section 962 election" | Leaves out the CFC screen, the only input reaching a section 962 election; reads income averaging and Form 8978 without their gates. |

4 lines: 1 representation, 3 model error. No findings.

## Landing round (2026-11-14), after the scope-hole fixes

Subject after lane land3-holes (BUG-0642: `scope.nol` ungated, read directly by `scope.schedule1`, and asked in the new tick group `before_2025`). Claude transcription pass b8c2e2325e96 (line `scope.schedule1`), triage record `.transcription/triage/2025/scope.json` (executable-triage-v2, 4,039 comparisons, newer than the log; carry ruled nothing). Claude render pass 1b4bf43be4e1 (whole form; the reviewer was given Form 1040 pp. 1-2, i1040gi pp. 14, 36, 43, i1040sse and p575 p. 35 only). Rulings text in `/tmp/land3-adj10/scope.transcription.json` and `/tmp/land3-adj10/scope.render.json` (lane land3-adj10).

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | scope.schedule1 | model error | 3,651/4,039; 74 value (refused returns, project true / reply false, e.g. scope.rental, scope.clergy_if_religious_work); 6 candidate-unknown (none completed) | i1040se p. 1; i1040sf p. 2; i1040gi p. 25, Lines 8z, 24f | As the earlier landing ruling: leaves rental, K-1, farm, clergy/church, W-2 marks, recovery and other self-employed plans out of the Schedule 1 screen; scope.nol agrees. |
| claude | render | armed_forces | interface gap | UNCLEAR | p590a p. 9, "2 years after your active duty period ends" | A 2025 repayment needs active duty ending after 2022 began; the window is no narrower than the source. |
| claude | render | pay_no_w2 | interface gap | MISMATCH | i1040gi p. 24, Line 1c (box 8) | Box 8 allocated tips are refused by s2.w2_marks in the same W-2 tick group; the help names box 8 too. |
| claude | render | w2_marks | interface gap | UNCLEAR | fw2 box 12 code H; i1040gi Line 24f; p525 p. 10 | Code H deferrals are deducted on Schedule 1 line 24f. |
| claude | render | artist_official_if_w2 | interface gap | UNCLEAR | p463 pp. 20, 23 | The line 12 deduction is for employees (Form 2106); an official paid only in fees misses only a refusal whose remedy is to go on without the deduction. |
| claude | render | recovery | finding (medium) | UNCLEAR | p525 p. 24, Recoveries and Tax benefit rule; f1040s1 line 1 | Names a deduction but not a credit; excepts a state but not a local income tax refund (BUG-0640). |
| claude | render | disaster_distribution | interface gap | MISMATCH | i8915f p. 2, Who Must File; p. 8, Carrybacks | 2025 distributions are screened per Form 1099-R by retirement.disaster; a late-2025 repayment of a 2022 distribution is carried back. |
| claude | render | reforestation | interface gap | UNCLEAR | i4562 p. 18, section 194, "84-month period" | Amortization reaching 2025 starts no earlier than 2018. |
| claude | render | passive_if_business_before | interface gap | MISMATCH | i1040sc p. 4, Line G (sc.passive); scope.rental, scope.k1, scope.farm | Activities begun in 2025 are refused by those screens. |
| claude | render | other_line16 | interface gap | MISMATCH | i1040gi p. 36, Line 16; retirement lump-sum screen; scope.k1 | Form 4972 is refused per Form 1099-R; a section 965(i) triggering event comes with a 2025 K-1. |

10 lines: transcription 1 model error; render 8 interface gap, 1 finding (medium). Findings: BUG-0640 (`scope.recovery` wording).

## Landing round (2026-11-14), after the scope.recovery fix

Subject after BUG-0640 (`scope.recovery`: deduction or credit, state or local refund, p525 p. 24). Last
review of this round for scope. Claude transcription pass 2eb39b30c079 (line `scope.schedule1`), triage
`.transcription/triage/2025/scope.json` (executable-triage-v2, 4,053 comparisons; carry ruled nothing). Rulings in
`/tmp/land3-adj14/scope.transcription.json` (lane land3-adj14).

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | scope.schedule1 | model error | 3,689/4,053; 59 value (refused returns, project true / reply false: scope.rental, scope.clergy_if_religious_work); 53 candidate-unknown (3 completed) | i1040se p. 1; i1040sf p. 2; i1040gi Line 24f | Third time: leaves rental, K-1, farm, clergy/church, W-2 marks out of the screen; its extra CFC term is refused by scope.other_line16 anyway. |

1 line: 1 model error. Findings: none.

## Goal-1 round (2026-11-15), render

Claude render log, whole (forced: a review of scope logged after the fixes of BUG-0651, BUG-0675 and BUG-0733):
match 71, mismatch 1, unclear 1. Both ruled; no finding.

| family | kind | line | class | evidence | deciding source | reason |
|---|---|---|---|---|---|---|
| claude | render | disaster_distribution | refusal located elsewhere | MISMATCH: a 2025 qualified disaster distribution is not covered by the question | forms/2025/retirement.yaml retirement.disaster (operand of retirement.special); i8915f | A 2025 distribution has a 2025 Form 1099-R, whose record asks retirement.disaster and refuses; the scope question covers only 2023 and 2024 distributions spread into or repaid in 2025 |
| claude | render | reforestation | scope | UNCLEAR: the seven-year window is not in Schedule 1's text | i4562 (2025) p. 18, Qualified forestation and reforestation costs (section 194), "over an 84-month period" | The window follows the 84-month amortization; the question screens out Schedule 1 line 24d |

Counts: 2 ruled (refusal located elsewhere 1, scope 1); 0 findings.

## Goal-1 coverage-expansion round (2026-11-15)

Lane xadj-f (claude-opus-5-5, judgment, tax year 2025, jurisdiction us), in the coverage-expansion merge worktree (xint). Claude transcription log, line-scoped pass 4be1d7385eb3 (scope.household_pay_if_pay, contractor_pay_if_pay, tips_unreported_if_pay, strike_pay_if_pay, schedule1, other_income); triage `.transcription/triage/2025/scope.json` (executable-triage-v2, 4,499 comparisons per line). Rulings file `/tmp/xadj/f/scope.transcription.json`. What changed (lane notes x2-paynow2, x1-sche, x2-s1o): the four pay gates are new; scope.schedule1 takes scope.rent_personal_if_rental in place of scope.rental and drops scope.recovery and scope.nol (now computed); scope.other_income takes scope.wages_no_form_if_pay in place of scope.pay_no_w2 and scope.medicaid_waiver (now computed).

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | scope.household_pay_if_pay, contractor_pay_if_pay, tips_unreported_if_pay, strike_pay_if_pay | representation | 4,483/4,499 agree each; 16 project-unknown on incomplete/refused partial records (gate unanswered); no value difference | i1040gi p. 24, Lines 1b, 1c, 1h; f8919 p. 1 | A conjunction with scope.pay_no_w2 is the gated choose. |
| claude | transcription | scope.schedule1 | model error | 4,134/4,499; 48 value, all refused returns (project true, reply false: the reply's operands are a subset of the project's); 279 project-unknown; 38 candidate-unknown (27 completed) | i1040se p. 1; i1040sf p. 2; i1040sse p. 1; i1040gi p. 25 | Fourth time: leaves personal-property rental, K-1, farm, clergy/church, W-2 marks and other plans out of the screen. Agrees with the project in leaving NOL and recoveries out. |
| claude | transcription | scope.other_income | model error | 4,207/4,499; 34 value, all refused returns; 212 project-unknown; 46 candidate-unknown (34 completed: scope.excess_deferral read without its W-2 gate) | i1040gi p. 8, p. 23, p. 95 Line 20; i2441 p. 5; i8915f p. 2; i8582 p. 1 | Leaves out nonresident status, chapter 11, reservist repayments, benefits, disaster distributions, passive losses. Agrees in leaving the newly computed pay out. |

Counts: claude transcription: representation 4, model error 2. Findings: BUG-0771 (low; found while checking scope.other_income, not a review disagreement): the cite of scope.other_income still quotes i1040gi p. 24 Lines 1b, 1c, 1d and 1h for pay the tool now computes. No line left open.

## Goal-1 coverage-expansion round (2026-11-15), render

Claude render log, line-scoped (the changed pay, rental and Schedule 1 lines): match 19, mismatch 1. Rulings file `/tmp/xadj/f/scope.render.json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | passive_if_business_before | scope | MISMATCH: a business first owned in 2025 without material participation is not screened | i1040sc p. 4, Line G (sc.screened on sc.passive false); scope.schedule1 (scope.farm, scope.k1); f8582 | Each activity begun in 2025 is screened where entered, and rentals are now computed with Form 8582; the gated question covers prior-year passive activities. |

Counts: render scope 1; no finding.
