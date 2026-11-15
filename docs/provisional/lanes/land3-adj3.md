# Lane land3-adj3: transcription adjudication of f5695, retirement and eic (landing round, 2026-11-14)

Model claude-opus-5-5, class judgment, tax year 2025, jurisdiction us. Scope: every `Ruling: open` section of the Claude
transcription logs of f5695 (25), retirement (23) and eic (17). The work changed the three logs and their sidecars
(through `tools/transcription/rule.py --kind transcription`) and the three adjudication summaries
(`reviews/2025/transcription/adjudication/{f5695,retirement,eic}.md`, section "Landing round (2026-11-14)"). Rulings:
`/tmp/land3-adj3/{f5695,retirement,eic}.json`. No form, question, fixture, parameter or tool was edited. No paid review
or model call was made. Nothing was committed.

Evidence: the triage records `.transcription/triage/2025/<form>.json` (executable-triage-v2, as found; not rerun), their
`--explain` witnesses, the line-scoped pass replies (`.transcription/<form>.lines-*.response.txt`), the archived sources
and the form YAML. In one place the interview engine (`interviewState`, profile full) was also used: it showed whether
Form 5695 line 19a is asked after line 17a No.

Triage caveat: `triage.mjs` applies only the project's `shown_when`. It ignores a `shown_when` that the reply declares.
For eic and the retirement worksheet, the "candidate-shows-skipped" counts on lines that the reply's own condition hides
are artifacts, so those `shown_when` were checked by reading.

## Counts

| form | representation | model error | scope | finding | open |
| --- | --- | --- | --- | --- | --- |
| f5695 | 25 | 0 | 0 | 0 | 0 |
| retirement | 11 | 12 | 0 | 0 | 0 |
| eic | 0 | 13 | 4 | 0 | 0 |

## Patterns

- **f5695 (all representation).** The reply reads the raw amount inputs. The redraft asks those amounts only behind
  parent questions: `f5695.any`, the per-kind Yes/No questions, `s3.prior_other_forms`, and the Section A and B home
  questions. So on completed returns where a gate is No, the reply is unknown, and the sampled witnesses show no other
  completed difference. Value differences appear only on refused returns. There the reply zeroes 17e Yes, a missing
  QMID or a Section B new home, which the project refuses (owner decision 7). They also appear on fixtures that carry
  costs with every kind answered No.
- **f5695 line 19c.** Incomplete records with a door cost after line 17a No show project $150 against reply $0. The
  engine shows that the door-cost questions cannot be reached after 17a No (and can after 17a Yes), so that cost is an
  input the filer is never asked. Line 19h is $0 either way. This is not a project defect.
- **retirement.**
  - `has_rollover`, `sav_amount`: representation. Code G: the reply reads `retirement.rollover`, which is never asked
    for a direct rollover (`rolled` = box 1).
  - `l1`, `l2`, `l2_e05/e09/e19/e22/e23`, `l1_s`, `l2_s`: representation. The reply's automatic exception 12 reads
    `retirement.under59`, which is asked only with code 7. For codes 1 and S, exception 12 is claimed through
    `retirement.exception` (i5329 p. 5). Example: the p590b Tom Jones example (age 35) gives project $0, reply $3,000,
    and the reply's figure comes only from the unasked answer.
  - `taxable`, `amount_a`: model error. Besides the code G point, the reply refuses `stage10.smw.recovered_exceeds_cost`,
    a completed return. i1040gi p. 28 makes that payment fully taxable ("you got your entire cost back tax free before
    2025").
  - SMW 1, 2 and 4 to 11: model error, the same reading as the refresh and R2 rounds. The worksheet is shown for a plan
    annuity whose cost was already recovered.
- **eic.**
  - `eic.eligible`: model error. The reply reads it as "can take the credit" and adds the worksheet STOPs, so it is false
    on filers who pass Steps 1 to 5 but get no credit (the same reading as the backlog round).
  - `eic.credit`, `check_27c`, `separated_box`, `(Step 5, 2)`: scope. None has a completed-return difference.
  - Step 5 lines 1, 3 and 5: model error. They have no `shown_when`.
  - `(Step 5, 4)`: model error. The combat pay refusal fires on two completed returns that never reach Step 5.
  - Worksheet lines 4b, 6 (wsb_6), 1, 2, 3, 4, 5 and 6 (line6): model error. Their `shown_when` has no test of Steps 1
    to 4. For example, 4b is shown on Schedule C filers who stop at Step 1 (`stage14.asset.*`), and Worksheet A line 2
    shows $308 on the `stage9.eic.no_child.*` returns that stop at Step 4.
  - `eic.credit` (Form 1040 line 27a) agrees on every completed return.

## Findings

None. No pending bug file was written.

## Lines left open

None. `python3 tools/transcription/check_logs.py | grep -E '^\[claude\] (f5695|retirement|eic)'` reports no open
transcription ruling for these forms. It does report that the class M logs of f5695 and retirement reviewed an earlier
computation; that is outside this lane.

## Notes for the owner

- Several sampled-witness claims rest on the triage record's capped witnesses, not on a full listing. The ruling texts
  say "sampled" where that applies.
- The brief classes gate-ignoring differences as representation. Earlier rounds, under the README, called "a candidate
  that needs an answer the source does not need" a model error. The f5695 and retirement rulings follow the brief.
