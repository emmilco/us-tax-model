# se: adjudication summary

## Goal-1 coverage-expansion round (2026-11-15)

Lane xadj-c (claude-opus-5-5, judgment, tax year 2025, jurisdiction us), round 2 of the coverage-expansion merge in the xint worktree (uncommitted). Reviews run by lane xadj (rerun_all, line-scoped where the tool allowed). Rulings files `/tmp/xadj/c/<form>.<kind>.json`, applied with rule.py; full text in the logs and sidecars.

The Schedule SE definition gained lines 8b (Form 4137 line 10) and 8c (Form 8919 line 10), summed into 8d; both reviews ran whole.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | line13 | representation | 478/480 agree; 2 project-unknown on refused returns (Form 8919 roster unconfirmed); no value differs | Schedule SE (2025) lines 4a, 8a-8d, 10-13 | Same inputs (8b, 8c included) and parameters; the reply omits a floor at zero that never binds in its branch. |
| claude | render | 2 | interface gap | UNCLEAR | i1040sse pp. 1-5; person.se_screen | Partnership (K-1 box 14 code A), other non-Schedule C income, church and minister cases are refused at the caller person.se_line2 through person.se_screen. |
| claude | render | 3 | interface gap | MISMATCH | i1040sse pp. 1-5; person.se_screen | Farm income, CRP payments, chapter 11 and community income are refused by the same screen; line 3 is line 2. |
| claude | render | 4b | interface gap | MISMATCH | i1040sse Part II; person.se_screen | The optional methods are refused by the same screen; line 4b is zero. |
| claude | render | 5b | interface gap | MISMATCH | i1040sse p. 1, Employees of Churches; person.se_screen | Church employee income is refused by the same screen; line 5b is zero. |

Render: 13 match, 4 ruled. The same four render lines were ruled earlier ("refusal located elsewhere", an unclassified wording); interface gap is the class here.

Counts: transcription representation 1; render interface gap 4. Findings: none. Observation (person.yaml, not this form): the refusal text of person.se_line2 still lists "Forms 4137 and 8919", which are now figured and no longer on person.se_screen (cosmetic).

### Class M (whole, this round)

29 agree, 1 disagree:

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | class M | classm.se.2 — line8d | representation (skipped line, drop) | owes false; line 8a at the wage base; every reached line agrees | Schedule SE (2025) lines 4c and 8a | The model wrote $0 on a line the form says to skip; the engine carries 8a + 8b + 8c = $176,100. Dropped from the fixture, as for f8880. |
