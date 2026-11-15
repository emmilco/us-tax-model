# Adjudication — sli

Method: `README.md` in this directory. Full ruling text is in each log and its sidecar.

## Landing round (2026-11-14)

Interview redraft (landing worktree), Claude line-scoped pass 30019246ca23. Triage `.transcription/triage/2025/sli.json` (executable-triage-v2, regenerated 2026-11-14 on the fresh build; not rerun). Rulings applied with `rule.py`; full text in the log and sidecar.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | sli.deduction | model error | 2,063/2,726; 6 value (3 completed), 155 candidate-unknown, 492 candidate-refuses, 10 project-unknown | i1040gi p. 98, line 21 | Drops "aren't claimed as a dependent" though person.sav_claimed was in the request (stage11.sli.claimed $0 / $1,200). |
| claude | transcription | 1 | representation | 2,643/2,726; 83 candidate-unknown (20 completed); no value | i1040gi p. 99, worksheet line 1 | Same arithmetic; reads the loan answers without sli.any. |

Counts: model error 1, representation 1 (2). Findings: none. Project lines unchanged.


## Landing round (2026-11-14), class M

Lane land3-adj13 (claude-opus-5-5, judgment; tax year 2025, us). Claude class M log of 2026-11-14; `carry.py --kind classm` ruled nothing. Evidence: the log section and raw reply, the case prompt (`.classm/<case>.prompt.txt`) and job (`.classm/jobs.json`), the archived sources and the form YAML. Rulings file `/tmp/land3-adj13/sli.json`, applied with `rule.py --kind classm`; every model value ruled here is dropped from the fixture. Full ruling text: the log and `reviews/2025/classm/sli.rulings.json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | classm | classm.sli.3 — 1 | representation | project $1,500.00, model $0.00; dropped from the fixture | i1040gi p. 98, Line 21 (not claimed as a dependent); p. 99 worksheet | Model wrote the dependent bar into line 1; the project applies it in sli.eligible, deduction $0.00 both (engine eval: s1.line21 $0.00). |
| claude | classm | classm.sli.3 — 8 | representation | project $273.00, model $0.00; dropped from the fixture | i1040gi p. 98, Line 21 (not claimed as a dependent); p. 99 worksheet | Model wrote the dependent bar into line 1; the project applies it in sli.eligible, deduction $0.00 both (engine eval: s1.line21 $0.00). |
| claude | classm | classm.sli.3 — 9 | representation | project $1,227.00, model $0.00; dropped from the fixture | i1040gi p. 98, Line 21 (not claimed as a dependent); p. 99 worksheet | Model wrote the dependent bar into line 1; the project applies it in sli.eligible, deduction $0.00 both (engine eval: s1.line21 $0.00). |

Counts: claude classm representation 3. Findings: none. Left open: none.
