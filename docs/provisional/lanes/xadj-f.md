# Lane xadj-f: round-2 adjudication of sales, sd, tipjob, f8919, scope (coverage-expansion merge)

Model claude-opus-5-5, class judgment, tax year 2025, jurisdiction us. Worktree `.claude/worktrees/xint`. A fork of
lane xadj. Reviews were run by xadj (rerun_all for transcription and render, classm_one.sh for class M); this lane
ruled them with `tools/transcription/rule.py`. Rulings files in `/tmp/xadj/f/`. Summaries: "Goal-1 coverage-expansion
round (2026-11-15)" sections in `reviews/2025/transcription/adjudication/{scope,sales,sd,f8919}.md`.

## Counts
| form | kind | review | ruled |
|---|---|---|---|
| scope | transcription (pass 4be1d7385eb3) | 0 agree, 6 disagree | representation 4 (the four pay gates), model error 2 (schedule1, other_income) |
| scope | render | 19 match, 1 mismatch | scope 1 (passive_if_business_before) |
| sales | transcription (pass 60bd5eac256b) | 2 agree, 3 disagree | representation 1 ((e)), model error 2 ((g), (h)) |
| sales | render | 2 match, 1 mismatch | scope 1 ((g)) |
| sd | transcription (pass da3c033dcfd8) | 6 agree, 27 disagree | model error 1 (sd.filed), representation 26 |
| sd | render | 34 match | none to rule |
| tipjob | transcription, render | 1 agree; 2 match | none to rule |
| f8919 | render (lines 8, 9) | 1 match, 1 unclear | representation 1 (8) |
| sales | class M | 18 agree, 0 disagree | none to rule |
| sd | class M | 126 agree, 0 disagree, 12 skipped | none to rule |

## Findings
- BUG-0771 (low): `scope.other_income`'s cite still quotes i1040gi p. 24 Lines 1b, 1c, 1d and 1h (household
  wages, unreported tips, Medicaid waiver, strike benefits), which this merge made computed; its operands no longer
  refuse them (`scope.wages_no_form_if_pay` replaced `scope.pay_no_w2` and `scope.medicaid_waiver`). Fix: drop those
  four quotes from `scope.other_income`'s `cite.locator` and cite i1040gi p. 25, Missing or Incorrect Form W-2?, "Even
  if you don't get a Form W-2, you must still report your earnings" (the cite of `scope.wages_no_form`). Value
  unaffected. Not a review disagreement: seen while checking the line.
- No medium or high finding.

## Notes
- sd: triage did not evaluate the new reply (its sd.filed and lines 4, 5, 11, 12 reference `sd.other_forms`, which
  does not resolve), so carry ruled nothing; all 27 rulings rest on the expressions and the source (subset and
  linearity arguments are in each ruling).
- tipjob has no adjudication summary file (`reviews/2025/transcription/adjudication/tipjob.md` does not exist); with
  nothing to rule, none was created.
