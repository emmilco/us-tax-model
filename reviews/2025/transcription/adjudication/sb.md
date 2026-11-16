# Adjudication — sb

Method: `README.md` in this directory. Earlier rulings were made in the logs' sidecars (archived in
`.transcription/archive/before-fix-round2-2026-10-30/`); no summary was kept for them, so there is no earlier table to mark
superseded.

## Fix round 2

Subject after BUG-0246 (`sb.line8` counts a loan of cash or marketable securities as a distribution and covers a foreign
trust that existed at any time during 2025). Transcription logs (both families) and class M log: no open section. Both
render models were given i1040sb pp. 1-3 only and judged line 8 MATCH. Full ruling text:
`.transcription/proposed/fixr2/render.sb[.deepseek].json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| both | render | 4 | interface gap | UNCLEAR | f1040sb p. 1, line 4 | Form face not given; the restatement is the form's line. |
| deepseek | render | 7a | representation | MISMATCH | i1040sb p. 3, Line 7a—Question 2 | Question 2 is the helper sb.fbar_required. |

Fix check: the new `sb.line8` wording matches i1040sb p. 3, Line 8 ("a loan of cash or marketable securities is generally
considered to be a distribution"; "a foreign trust that existed during 2025"); "counts" drops "generally", which can only
add Yes answers, and a Yes refuses (Form 3520 / Form 3520-A), so the change widens a refusing screen. No error introduced.
Findings: none.

## Goal-1 round (2026-11-15)

Lane b1-adj-a (claude-opus-5-5, judgment, tax year 2025, jurisdiction us), in the B1 integration worktree. Open lines of the Claude transcription log (line-scoped pass 602d75169f27; triage `.transcription/triage/2025/sb.json`) and render log (pass 4f81ca75d3f6). Full ruling text is in the logs and sidecars; rulings files `/tmp/b1-adj-a/<form>.json` (transcription) and `/tmp/b1-adj-a/render/<form>.json` (render), applied with rule.py. The deepseek family is dormant and not ruled.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | 6 | representation | 2,548/3,063 agree; no value; 225 candidate-unknown (sb.ordinary_dividends read where div.any is No), 2 candidate-refuses, 68 project-refuses, 220 project-unknown | f1040sb line 6; i1040sb, Line 5 | The project asks the amount only under div.any. |
| claude | render | 8 | finding (low) | UNCLEAR; indirect receipt, free use of trust property, foundation/waqf | i1040sb p. 3, Line 8 | The clauses follow Form 3520 rules that are not archived or cited; each only widens a refusing Yes. BUG-0759. |

Counts: claude transcription: representation 1; claude render: finding 1. Findings: BUG-0759 (low; citation; no value change). No line left open. Class M (sb) not ruled in this section: its rerun was held by the coordinator.
