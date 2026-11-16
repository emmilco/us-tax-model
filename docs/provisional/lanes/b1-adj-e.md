# Lane b1-adj-e: adjudication, goal-1 round 2 (sc, scveh, carloan, otjob, ftc)

Model claude-opus-5-5, class judgment; tax year 2025, jurisdiction us. Brief: /tmp/b1-adj-brief.md (transcription,
with the render and class M overrides). Rulings files: /tmp/b1-adj-e/<form>.json (transcription) and
/tmp/b1-adj-e/<form>.render.json (render), applied with `tools/transcription/rule.py`. Summaries: a "Goal-1 round
(2026-11-15)" section in `reviews/2025/transcription/adjudication/{sc,scveh,carloan,ftc}.md`. Nothing else edited; no
paid review, build, render or check-all run; no commit.

## Rulings

| form | kind | line | class |
| --- | --- | --- | --- |
| sc | transcription | 4 (sc.ho_line4) | representation |
| sc | transcription | 5 (sc.ho_line5) | model error |
| sc | render | 5 (sc.ho_line5) | scope |
| scveh | transcription | 13, 15, 16, 18 | ambiguity (amb.2025.vehicle_business_pct rounding) |
| scveh | transcription | 10, 14, 19 | model error |
| carloan | transcription | 22(ii), 22(iii) | model error |
| carloan | render | 22(ii) | scope |
| ftc | transcription | ftc.has_tax | representation |
| ftc | transcription | ftc.credit | model error |
| ftc | render | limited | scope |
| otjob | transcription, render | - | no open line |

Counts: sc transcription 1 model error, 1 representation; sc render 1 scope. scveh transcription 4 ambiguity, 3 model
error. carloan transcription 2 model error; carloan render 1 scope. ftc transcription 1 model error, 1 representation;
ftc render 1 scope. otjob none.

Points worth a reader's attention:
- scveh 19 (model error): the reply multiplies by the table rate for `scveh.prior_conv` in every year, including the year
  placed in service, where the convention comes from the mid-quarter test (p946 p. 41). Witness:
  stage14.veh.2025_mq_nobonus, project $1,500 (Table A-5, 5.00%), reply $6,000 (half-year 20%). The landing round ruled
  this line ambiguity; this pass's reply differs in substance.
- scveh 10, 14: no value differs. Line 10's reply caps every vehicle at line 9 (passenger automobiles only); line 14's
  reply shows the line past the line 10 stop note that the project now follows (BUG-0633 fix).
- sc 4: on 19 completed returns the project leaves line 4 unknown where sc.ho_uses is false and ho_sqft is not asked
  (classm.f1040.4, classm.s2.4); line 30 is $0 on both sides there. Ruled representation, as earlier rounds; not
  checked how the rendered return displays an unknown worksheet line that is not used.

## Findings

None. No pending bug filed (prefix b1-adj-e unused).

## Class M

Not done. At 15:25 the sc and scveh class M logs had no open line, and the coordinator then told this lane not to run
`rule.py --kind classm` or `carry.py --kind classm` until messaged (fixtures/2025/classm.json being restored by serial
reruns). Their reruns had not reported when this lane finished.

## Verification

`python3 tools/transcription/check_logs.py` (run after the rulings; exit 1 from other forms): no "open ruling(s)" line for
sc, scveh, carloan, otjob or ftc in either the transcription or the render log. The only lines for these forms are
`[claude] sc` and `[claude] scveh`: "the classm log reviewed an earlier computation; rerun the review" (the pending
class M reruns).
