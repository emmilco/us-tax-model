# Adjudication — qdcg

Method: `README.md` in this directory. Triage record: `../triage/qdcg.deepseek.json`
(executable-triage-v1; 1,083 fixtures, 500 generated returns, seed 20261026, 0 partial records: the
worksheet has no own inputs). DeepSeek family only. Full ruling text is in the log and its sidecar.

## Round 1 (superseded subject)

| family | line | class | triage | deciding source | reason |
| --- | --- | --- | --- | --- | --- |
| deepseek | 3 | representation | 1,583/1,583 agree | i1040gi p. 38, worksheet line 3 | The two-guard Schedule D branch equals the floored smaller of lines 15 and 16; without Schedule D, line 7a equals sd.distributions. |
| deepseek | 6 | representation | 1,583/1,583 agree | i1040gi p. 38, worksheet line 6 | Same parameter; the floor at zero is a type wrapper over positive values. |
| deepseek | 13 | representation | 1,583/1,583 agree | i1040gi p. 38, worksheet line 13 | Same parameter; the floor at zero is a type wrapper over positive values. |

Findings: none. Project lines unchanged.

## Stage 20

Render only, Claude only (the deepseek render log has no open line). The worksheet was re-rendered because the English
names of the Schedule D lines it reads changed in Stage 20. Full ruling text:
`.transcription/proposed/stage20/render.qdcg.json`.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | render | 1 | scope | MISMATCH, Form 2555 alternative not refused | i1040gi p. 36, Line 16; s1.line8_other (line 8d) | A Form 2555 exclusion is refused on Schedule 1 before the worksheet; the note records the alternative as not encoded. |

Findings: none for qdcg in Stage 20.
