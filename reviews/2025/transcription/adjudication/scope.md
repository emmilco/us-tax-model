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

## Stage 19

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
