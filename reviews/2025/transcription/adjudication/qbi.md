# Adjudication — qbi

Method: `README.md` in this directory. Full ruling text is in each log and its sidecar.

## Landing round (2026-11-14)

Interview redraft (landing worktree), Claude line-scoped pass 8fa59c59015e. Triage `.transcription/triage/2025/qbi.json` (executable-triage-v2, regenerated 2026-11-14 on the fresh build; not rerun). Rulings applied with `rule.py`; full text in the log and sidecar.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | qbi.eligible | representation | 2,372/2,672; 151 candidate-unknown (13 completed), 125 project-unknown, 24 project-refuses; no value | f1099div p. 5, Box 5 | Drops the box 1a parent and the qbi.unsupported refusal. |
| claude | transcription | qbi.carryforward_if_prior_form | representation (equivalent) | 2,672/2,672 | i8995 p. 3, Line 3 | Guards in the other order. |
| claude | transcription | qbi.deduction | representation | 1,992/2,672; 476 candidate-unknown (34 completed), 204 project-refuses; no value | f8995 p. 1; i8995 p. 1 | Same form choice; the reply reads the refusal answers without their parents and routes a patron to 8995-A (project refuses, amb.2025.qbi_cooperative_patron). |

Counts: representation 3 (3). Findings: none. Project lines unchanged.

## Goal-1 round (2026-11-15)

Lane b1-adj-b (claude-opus-5-5, judgment; tax year 2025, us), B1 merge worktree nx-b1. Open lines of the Claude transcription log ((the 2026-11-15 review)), ruled against `.transcription/triage/2025/qbi.json` (executable-triage-v2, log sha matches), the archived sources and `forms/2025/qbi.yaml`. Rulings `/tmp/b1-adj-b/qbi.json`, applied with `rule.py --kind transcription`; full text in the log and sidecar.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | qbi.eligible | representation | 2,193/2,716 agree; 501 candidate-unknown, 11 project-unknown, 5 candidate-refuses, 5 project-refuses, 1 value; completed: 36 candidate-unknown | f1099div p. 5, Box 5 ("Box 5 ... included in box 1a"); i8995 pp. 3-4 | Caps at box 1a, which the project enforces by refusing box 5 above box 1a; reads qbi.suspended unasked. |

Counts: claude transcription representation 1. Findings: none. Left open: none.
