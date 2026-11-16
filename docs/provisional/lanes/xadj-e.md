# Lane xadj-e: round-2 adjudication of retirement, ira, person, ssb, refund (2025, us)

Model: claude-opus-5-5. Class: judgment. Year: 2025. Jurisdiction: us.
Worktree `.claude/worktrees/xint` (coverage-expansion merge, uncommitted). Fork of lane xadj. No forms, questions, params or
tools edited; no build, render, check_all or paid review run by this lane. Rulings files in `/tmp/xadj/e/`; summaries in
`reviews/2025/transcription/adjudication/<form>.md`, sections "Goal-1 coverage-expansion round (2026-11-15)" (and
", class M").

## Results

| form | kind | open | ruled | classes |
| --- | --- | --- | --- | --- |
| refund | transcription | 2 | 2 | representation 1, model error 1 |
| refund | render | 2 | 2 | ambiguity 1 (line 1, amb.2025.refund_cap_5d), representation 1 (line 6) |
| ira | transcription | 9 | 9 | representation 7, model error 2 |
| ira | render | 0 | - | review clean |
| ira | class M | 3 | 3 | model error 3 (dropped) |
| retirement | transcription | 14 | 14 | representation 12, model error 2 |
| retirement | render | - | - | log current, not rerun |
| retirement | class M | 0 | - | 80 agree, 0 disagree |
| ssb | transcription | 9 | 9 | representation 9 |
| ssb | render | 0 | - | review clean |
| person | transcription | 36 | 36 | representation 32, model error 4 |
| person | render | 0 | - | review clean (3 match) |
| person | class M | 16 | 12 carried, 4 ruled | model error 4 (dropped) |
| refund | class M | 0 | - | 51 agree, 0 disagree |
| ssb | class M | - | - | not run by 22:03 |

Findings: none (no medium, high or low). Every value difference traced to the reply: reading answers the interview does
not ask (parent gates, code G rollover amount, `retirement.under59` outside code 7, `person.sav_claimed` without
`sa.dependent`, `person.plan` without a Schedule C), display lines of a worksheet not used without a traditional IRA
contribution, or a misreading of the source (refund recovery path, ira.cov_gate without benefits, ira.excl_gate read as
the traditional-and-Roth exclusion, retirement box 5 / Simplified Method / code G entries, person.dc_earned without line
1e, the age-50 IRA limit from `person.age50_at_year_end`).

## Open matters for the coordinator

- **person transcription stale after ruling.** `forms/2025/s1.yaml`, `f2441.yaml` and `s2.yaml` were changed at 21:06:57
  (not by this lane), after the 20:54 person review. check_logs reports 8 person lines stale for changed foreign
  interfaces: person.se_line6, se_line12, se_line13, eic_se, dc_earned, dc_earned_b, ira_se, Step 2. They are ruled
  against the reply that exists; a line-scoped rerun (`transcribe.py --form person --lines auto`) is due once those
  edits settle. carry.py declined to run on person for the same reason.
- Class M person: finished at about 22:00 (after the 21:50 deadline). carry carried 12 rulings; the 4 left open
  (classm.person.5, 12, 13, 14, `person[taxpayer].wages`: the model summed W-2 box 1, the line is boxes 3 + 7) were
  ruled model error and dropped, the same ruling as in the Goal-1 class M round.
- Class M ssb: had not started at 22:03 (`/tmp/xadj/classm-ssb.txt` absent). Not reviewed by this lane; check_logs
  reports its log as reviewing an earlier computation.
- refund class M: 51 agree, 0 disagree ($0.73). ira class M: 3 disagreements on classm.ira.2 (no traditional
  contribution; the model filled worksheet lines 1b, 2a, 2b), model error, dropped from the fixture.
- check_logs at 21:31 (federal): no open ruling in any of the five forms; the remaining lines are the person staleness
  above and the two pending class M runs.
