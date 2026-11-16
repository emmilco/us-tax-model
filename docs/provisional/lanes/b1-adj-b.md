# Lane b1-adj-b: adjudication, goal-1 round 2 (B1 merge)

Model claude-opus-5-5, class judgment; tax year 2025, jurisdiction us. Worktree nx-b1 (uncommitted B1 merge).
Forms: person, ira, retirement, dependent, f8863, qbi. Brief: /tmp/b1-adj-brief.md (transcription; overrides for
render and class M).

Evidence per line: the open log section, the executable triage record `.transcription/triage/2025/<form>.json`
(log sha matched the log for every form), witness operands, the fixtures' hand-predicted evidence notes, the archived
sources and the form YAML. Rulings files are in `/tmp/b1-adj-b/` (`<form>.json`, `dependent.render.json`,
`person.classm.json`), applied with `tools/transcription/rule.py`. Each form's adjudication summary has a new
`## Goal-1 round (2026-11-15)` section in `reviews/2025/transcription/adjudication/<form>.md`. The dependent render
rulings are a `, render` section there, as earlier rounds did.

## Rulings per class

| form | kind | lines | model error | representation | interface gap | ambiguity |
| --- | --- | --- | --- | --- | --- | --- |
| person | transcription | 23 | 11 | 12 | - | - |
| ira | transcription | 1 | 1 | - | - | - |
| retirement | transcription | 13 | 2 | 11 | - | - |
| dependent | transcription | 20 | 19 | 1 | - | - |
| f8863 | transcription | 26 | 8 | - | 18 | - |
| qbi | transcription | 1 | - | 1 | - | - |
| dependent | render | 5 | - | - | - | 5 |
| person | class M | 18 | see below | | | |

Findings: none. Pending bugs: none.

## Notable points

- person: the line-scoped reply takes the IRA $8,000 limit from `person.age50_at_year_end`, which is asked only for a
  birth in the cut-off year, instead of from `person.birth_year`. A filer born in 1970 who contributed $8,000
  (stage16.ira.i5, i7; the two age-50 audit cases) is screened as having an excess, and ira_deduction,
  ira_nondeductible and ira_files_8606 refuse. Model error; the project is right. `person.amt_dep`: the reply keeps
  only Form 4562 line 17. i6251 p. 5 exempts only qualified property, and the project line is an upper bound for the
  AMT screen. Model error.
- retirement: the reply ignores Form 1099-R box 5 employee contributions (stage10.plan.box5 $12,000 against $10,800,
  i1099r box 5 "recover tax free this year"). It also gives $21,000 on a $12,000 payment whose cost was recovered
  before 2025. Model error on taxable and amount_a. The rest follows the gate pattern of earlier rounds (code G
  rollover; raw `retirement.under59` asked only with code 7).
- f8863: pass 573118875700 records "complete input context: fail". The reply was not given `person.sav_claimed` or
  `s3.line2`, so the claimed-filer bar (i8863 p. 3 item 1) and CLW line 5's line 2 are interface gaps. The
  unconditional `f8863.ban` refusal on line 1 (it refuses after the line 4 stop, stage19.mut.aoc_line4_zero_ban) and
  the worksheet without a line 4 stop are model errors. FOR THE COORDINATOR: the incomplete input context of that
  line-scoped pass is a review-tool matter, not a project defect. A rerun with the full context could replace the 18
  interface-gap rulings if wanted (paid; not run).
- dependent: the whole-form reply's dependent test still exempts a joint return from the dependent-taxpayer test and
  has a months-only qualifying-child residency test, as ruled in the Landing round. hoh_test2_lived drops the
  "Test 2 person" half of its label. Lines 27-30 hide the credit for a student whose TIN was only applied for (T-113).
  Lines 28-30 were ruled representation in the Landing round; they are model error here because each line's own
  shown_when carries the test.
- dependent render 27-31: amb.2025.edu_1098t_date (owner D7(d)), as the Landing round.

## Class M (person)

NOT APPLIED: held at the coordinator's instruction while fixtures/2025/classm.json is being restored. All 18 open
lines are the Landing-round pattern: `person[...].wages` is the total of w2.wages, which each prompt gives as
"Add social security wages and social security tips = $0.00" (checked in all 16 case prompts), and the model summed
W-2 box 1. Each is a model error, dropped from the fixture. Rulings are staged in `/tmp/b1-adj-b/person.classm.json`.
To apply: `python3 tools/transcription/carry.py --kind classm --form person`, then
`python3 tools/transcription/rule.py --form person --kind classm --rulings /tmp/b1-adj-b/person.classm.json`, and add a
"Goal-1 round (2026-11-15), class M" section to reviews/2025/transcription/adjudication/person.md.

check_logs (16:05): for these forms only "[claude] person: open ruling(s) in the classm log" remains; transcription and
render are clear.
