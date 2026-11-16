# Lane x2-paynow2: pay not on a W-2 (coverage expansion, scout-tail part A)

Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Worktree `.claude/worktrees/x2-paynow2` (x1-base).
Design: `docs/provisional/lanes/scout-tail.md` part A. No paid reviews, no model calls, no commits.

Base caution applied: `fixtures/2025/defaults.json` copied from `nx-b1`; this lane's 22 defaults are added by
`/tmp/mfs-x2-paynow2/defaults_patch.py` (idempotent; run it on the merged file). `npm run compile` reports the known
`sampledShare` error from `mutate-worker.ts`; tsc still emits and the build runs. Mutate skipped (brief).

## What is figured now (all five ranked items built)

| Item | Lines | Inputs (ask) |
|---|---|---|
| 1. Form 8919 + line 1g | new `f8919` (implicit, one per person: lines 6–13, `files`), `f8919firm` (rows: `reason` enum a/c/g/h, `wages` col (f)); `person.f8919_firms/_wages/_line10/_tax`; `f1040.line1g`; `s2.line6`, `s2.line7`; `f8959.line3`; SE `line8c` | `scope.contractor_pay`, `$f8919firm`, `f8919firm.reason`, `f8919firm.wages` |
| 2. Form 4137 + line 1c | new `f4137` (implicit: lines 2–13, `files`, `line5_over`), `f4137row` (col (c), col (d)); `person.f4137_rows_c/_rows_d/_col_c/_col_d/_line4/_line6/_line10/_tax/_filed`, `person.line1c`; `f1040.line1c`; `s2.line5`; `f8959.line2`; SE `line8b`; Form 8919 line 8 adds 4137 line 10 | `scope.tips_unreported`, `$f4137row`, `col_c`, `col_d`, `person.f4137_under20`, `person.tips_gov`, `person.tips_noncash` |
| 3. Medicaid waiver (1d, 8s, choice) | `person.mw_*` (box 1, not box 1, Form 1099 part, business, total, paid, earned choice, other, other_1d, not_earned), `person.line1d`, `person.line8s`; `f1040.line1d`; `s1.line8s`, `s1.line8s_neg`; `s1.line9` (now Dollars, adds 8s as a negative); `eic.step5_line2` and `s8812.eiw_4` = Σ `person.mw_not_earned` | `person.mw_box1`, `mw_not_box1`, `mw_1099`, `mw_business`, `mw_earned` (asked; owner decision) |
| 4. Disability pension → 1h | `retirement.dis_all_early(+_if_early)`, `retirement.dis_wages`, `retirement.dis_split` (replaces `dis_early_if_disability` in `retirement.special`); `person.plan_amount_a`/`plan_taxable` exclude `dis_wages` items; `person.dis_wages`; `retirement.bad_code` no longer refuses code 3 from a plan when `dis_wages` | `retirement.dis_all_early` |
| 5. Lines 1b, 1h (strike) | `person.household_wages(+_if_pay)`, `person.strike(+_if_pay)`, `person.line1h`; `f1040.line1b`, `f1040.line1h`; `f1040.line1z` = 1a+1b+1c+1d+1e+1g+1h | `scope.household_pay`, `scope.strike_pay`, `person.household_wages`, `person.strike` |

Also: `person.earned_not_w2` (1b+1c+1d+1g+1h per person) added to `person.dc_earned` and `dc_earned_b` (Form 2441
earned income, i2441 "line 1z"; p503 p. 4 "Earned income also includes strike benefits"). SE def gains parameters
`line8b`, `line8c`; `line8d` = 8a+8b+8c; the four `person.se_*` callers bind them.

Interview (questions.yaml): `scope.pay_no_w2` and `scope.medicaid_waiver` stay as the same ticks (order 146, group
`other_pay`), no longer refusing; help reworded. A Yes to pay_no_w2 opens tick group `pay_kinds` (order 146 seq 20–24:
household, contractor, tips, strike, "other wages with no W-2" [refuses]). Per-person children: order 147 (household
amount, `$f8919firm` + reason + wages, strike), 148 (`$f4137row` + columns, under-$20, government, noncash), 149
(Medicaid). `retirement.dis_early` help changed; `retirement.dis_all_early` order 170 seq 52. The filer with nothing
answers the same single `other_pay` screen as before (not walked: see below).

## Still refused (gate, reason)
- `scope.wages_no_form_if_pay` (in `scope.other_income`): wages from an employer that sent no W-2.
- `person.tips_gov_if_rows` at f4137 line 10: tips as a government employee paid only the 1.45% Medicare tax.
- `f4137.line5_over` (line 5 > line 4), `person.mw_1099_over` (inconsistent entries).
- `person.mw_business_if_1099`: Medicaid pay in a home-care business (Schedule C route).
- `retirement.dis_split` (in `retirement.special`): disability pension in the year minimum retirement age is reached,
  or before that age with after-tax cost.
- `s1a.f4137` (line 4b) and `person.f4137_filed` (tipjob col (c)): the tips deduction with Form 4137 tips (row match rule
  deferred; replaces the old `s2.other` refusal on those two lines).
- Allocated tips (W-2 box 8): still `s2.w2_marks` (Schedule 2 screen, other lane's form). Excess deferrals, code 8/P
  corrective distributions, terror/military disability: unchanged. RRTA: refused (`person.rrta`, also on 4137/8919 line 8).

## Premises checked against archived sources
f8919 p. 1–2 (reason codes; G is the fallback, so no "other" refusal; lines 6–13; line 8 includes 4137 line 10; line
12 uses line 6); f4137 p. 1–2 (lines 2–13; line 12 uses line 6; line 10 government-tips instruction; RRTA); f1040sse
lines 8b/8c/8d; f1040s2 lines 5–7; i8959 p. 3 lines 2/3; i1040gi p. 24–25 lines 1b–1h, p. 42 EIC Step 5 line 2, p. 92
line 8s; i1040s8812 EIW line 4; p525 p. 33 (Medicaid waiver = difficulty-of-care, count limits); p503 p. 4 (strike
benefits are earned income); p575 p. 6 (disability pension wages until minimum retirement age; p575 has no inspected
revision in the manifest, so it is not cited). Scout correction: code 3 from a plan was refused by `retirement.bad_code`
(the scout did not mention it), so the 1h route needed that gate narrowed.

## Fixtures (hand-predicted before evaluation; arithmetic in each case's evidence_note)
`fixtures/2025/f4137.json` (7: W1, W1+noncash, noncash only, over SS base, W9 government, line5_over, tips deduction
refused), `f8919.json` (4: W3, W4 with Schedule SE, with Form 4137, W10 RRTA), `pay_not_w2.json` (11: W5, W8, W6,
split year, W7, W7b, code II earned/not earned, Form 1099, business). Every computed case also asserts AGI (line 11a).
Result (lane runner `/tmp/mfs-x2-paynow2/runmine.py`, fixture-inputs + eval): **24 of 24 pass**. No predicted value was
changed; for refusals the prediction was the gate, and the refusal's text (form, remedy, cite) was filled from the
evaluation once the gate matched (8 values). First run found two model errors the predictions caught: Medicaid was
still in `scope.other_income` (W7 AGI), and code 3 plan pensions refused via `bad_code` (W6); both fixed.

Restated existing cases (approved end changes, scout A.8 item 4), listed:
- `eic.json` `stage9.eic.refuse.other_income`: Medicaid was a refusal; now `person.mw_box1` $4,000 stated;
  step5_line2 $4,000, step5_line4 $0, line 27a $0 (all predicted, pass).
- `s1a.json` `stage12.refuse.form4137_one_employer` / `_two_employers`: Form 4137 was modeled by `s2.other_tax`; now a
  real 4137 row; still refused, gates `s1a.f4137` / `person.f4137_filed`.
Tool-managed inputs (inputs only, no expectation changed): `scope.pay_no_w2: false`, `scope.medicaid_waiver: false`
added to 18 cases of `classm.json`, 2 of `classm.deepseek.json`, 1 of `mutation.json`; `mutation.m3.scope.oi_pay_no_w2`
gains `scope.wages_no_form: true` (keeps its refusal at `scope.other_income`). Not verified by a full run (coordinator).

## Verification run
- build OK (final, after all edits); `citations.py --strict` 0 findings; `year_changes.py --check` 0 failures (131 entries).
- Lane fixture cases 24/24. Coverage rows: `interview-coverage --rows coverage/pay_not_w2.yaml`: 11 rows, 0 problems. The
  restated rows `scope.pay_no_w2`, `scope.medicaid_waiver`, `scope.strike_benefits` passed in the run of
  `coverage/scope.yaml` (that file's other failures, e.g. `scope.statutory_employee` asking W-2 box 3, are in rows this
  lane did not touch; no base run was made to compare). `retirement.dis_reached_age` passes. `retirement.dis_early` (restated to proceeds) is
  **not yet passing**: with the pension now earned income the walk goes on to the saver's credit questions
  (`person.sav_student` answered, then `person.sav_voluntary` …), which the background return never answers; the row
  needs the rest of that chain answered (open, deadline). The file's 7 other problems are in rows this lane did not
  touch (not compared with a base run).
- Not run (coordinator's deadline / broken base): full test-fixtures (an earlier full run on the base: 598 cases crash on
  `s2.amt_owed`, an input the cases state that the base does not declare; not this lane's), `--ny`, interview-rules,
  tick-groups, check_consumers/questions/screens/false_no, siblings, check_bug_inventory, mutate, draft-walk personas.

## 2026
`changes/2026/s2.x2-paynow2.yaml` (C-X2-S2-01: 5/6/7 → 16a/16b/16c; 16c added to line 20); `changes/2026/s2.yaml`
C-SCHED-10: two `from` values updated for line 21 (now includes `s2.line7`) — shared file, merge caution. Change map
entry appended to `research/ty2026/changes.md`. Forms 4137 and 8919 for 2026: not posted, awaited (archive both).
2026 f1040 line 1d caption changed ("...not reported on Form(s) W-2"): left for the f1040 2026 owner. No new parameter
needs proposing beyond `f4137.rate_062/_0145`, `f8919.rate_062/_0145` (unchanged rates) and the enum
`contractor_reason`.

## Shared lines changed (merge cautions)
- `s1.line9`: type NonNegDollars → Dollars and operand `s1.line8s_neg` added (lane x2-s1o adds operands to the same list;
  x1-digital adds 8v). New `s1.line8s`, `s1.line8s_neg`; cite text of line 9 edited.
- `s2.line21`: operand `s2.line7` added and label; new `s2.line5/6/7`; `s2.other` label lost "tax on unreported tips"
  (F7b changed s2 1z/2/3/21 refusals).
- `f1040.line1z` operands; new 1b/1c/1d/1g/1h. `f8959.line2/3`. `se.yaml` def; `person.se_*` binds.
- `scope.other_income` any-list: `scope.pay_no_w2` → `scope.wages_no_form_if_pay`, `scope.medicaid_waiver` removed.
- `eic.step5_line2` (refusal on `scope.other_income` removed), `s8812.eiw_4` expr, `retirement.special`,
  `retirement.bad_code`, `tipjob.col_c` and `s1a.line4b_calc` refusal gates, `person.dc_earned(_b)` operands.
- `fixtures/2025/defaults.json`: from nx-b1 + `/tmp/mfs-x2-paynow2/defaults_patch.py` (22 entries).
- `tools/coverage/tree.json`: 6 residual gates added. `categories.json` for the integrator: drop `scope.pay_no_w2`,
  `scope.medicaid_waiver` from `wages_not_w2`; the tree.json `scope.other_income` question still names "wages not on a
  Form W-2, Medicaid waiver payments" (stale text, integrator).
- Pending wording: the `person.se_screened` refusal text still lists "Forms 4137 and 8919" (kept so no expectation
  changes; they no longer trigger it) — restate with the fixtures that quote it.

## Findings from the coverage walks (open)
- `f8919firm.reason` (column (c)) is never asked: no line reads it, and the interview asks only what a target reads. The
  printed form's column (c) is not collected. Fix: a display target or a reader (e.g. a `files` note); left open.
- The government-tips refusal (`person.tips_gov_if_rows`, at Form 4137 line 10) is told only when the walk reaches the
  Schedule 2 screens (`s2.other_tax`, question 115), not at its own question (N11). Row `pay.tips_government` answers
  `s2.other_tax: false` to pass; the asking order (a `seq` or a refusal entry order, technique 3.5) is left open.

## Left for later
- Schedule 1-A line 4b / worksheet col (c) with Form 4137 (row-match decision); allocated tips in W-2 box 8.
- IRA compensation (`ira.wages`, box 1 only) does not add 1b/1c/1g; `s179.income_wages` reads line 1a only (i4562 text).
- Personas and before/after walks (checklist §7 items 1, 8) not recorded; question reviews of the new questions.
- Full-tier checks listed above; NY (`test-fixtures --ny`): NY reads `f1040.line1z` and `s1.line9`, so NY lines 1/16 move
  for returns with these items (expected, not run).

## Round 2 reviews
New forms whole: f4137, f4137row, f8919, f8919firm — transcription, render, class M (12). Changed, line-scoped
transcription + render: person, se, s2, f8959, f1040, s1, s1a, tipjob, eic, s8812, retirement, scope; class M where
arithmetic changed: se, s2, f8959, f1040, s1, eic, s8812, retirement, person. Screen review: the residual gates above.
Question review: the 21 new or changed questions. Dry-run price first.

## Coverage gain (estimate)
Category `wages_not_w2` 0.8% of returns, +0.6 alone (report); realized +0.3 to +0.6 (scout 1.3: depends on what SOI col
17 holds; allocated tips and the tips deduction with 4137 remain refused, which lowers the tips part). Inferred, not run.

