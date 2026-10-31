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
