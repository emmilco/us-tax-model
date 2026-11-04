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
