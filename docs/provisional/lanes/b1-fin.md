# Lane b1-fin: finishing the review round of the goal-1 merge (B1)

claude-opus-5-5, judgment; tax year 2025, us. Worktree `.claude/worktrees/nx-b1`. Not committed; no check_all.

## Step 0

`/tmp/b1-r2-cm.log` ended `exit=0` (s3 agree 182; sb agree 11; sc 11 disagreements; scveh 14; sd agree 106).
Every class M carry and rule after that ran one at a time.

## Step 1: class M rulings

`carry.py --kind classm` ruled nothing on any form. Rulings were applied with `rule.py --kind classm`. Every model
value ruled here is dropped from the fixture. Summaries are under "Goal-1 round (2026-11-15), class M" in
`reviews/2025/transcription/adjudication/<form>.md`.

| form | open | ruled | classes | source of rulings |
| --- | --- | --- | --- | --- |
| person | 4 | 4 | model error 4 (box 1 summed for person.wages; w2.wages is boxes 3+7) | 4 of the 18 staged rulings in `/tmp/b1-adj-b/person.classm.json`. The other 14 named sections that are no longer open. Keys and values were checked against the rerun log. |
| f1095a | 1 | 1 | model error 1 (uniform; corrected column B) | staged `/tmp/b1-adj-c/f1095a.classm.json`. Key and values match. |
| f8889 | 4 | 4 | ambiguity 2 (line6, line7: amb.2025.hsa_line7_months), model error 2 (line8, line12: a 1-cent rounding slip) | staged `/tmp/b1-adj-c/f8889.classm.json`. Keys and values match. |
| sc | 11 | 11 | representation 5 (biz_a Form 7206 lines 4-13: no plan, so these are helpers; the model zeroed them), ambiguity 6 (biz_a qbi and biz_b lines 7/8/10/13/qbi: amb.2025.f7206_ratio_places, 6-place ratio against the exact one, 1 cent) | new, `/tmp/b1-fin/sc.classm.json` |
| scveh | 14 | 14 | ambiguity 14 (amb.2025.vehicle_business_pct, 6-place business-use percentage, 1 cent; checked against cases 3 and 4) | new, `/tmp/b1-fin/scveh.classm.json` |
| s2, s3, sb, sd, f8962, refund | 0 | none | none | none |

## Step 2: form changes and reviews

- (a) BUG-0758 (medium) fixed. In `forms/2025/s1.yaml`, s1.scholarship_taxable's source now excludes NHSC,
  Armed Forces HPSP and work-college work-learning-service pay. Its cite adds the p525 p. 35 Exceptions, with the quote
  and page checked in sources/2025/p525.txt. `interview/2025/questions.yaml` adds the help sentence. The pending
  entry has Fix, Fix lines, Siblings checked, Regression predictions, Validation and Status: fixed.
- (b) The f1040.yaml hunk of `/tmp/b1-asm-phase1.patch` was applied: line 12e now tests widowed_this_year before
  hoh_fails.
- Checks: compile and build OK; render (68 files) and render --ny (12) ran; test-fixtures 2031/2031 and --ny 357/357;
  citations --strict, year_changes --check and check_questions all exited 0.
- Paid reviews (`rerun_all.py`, line-scoped, estimated $2.17):
  - s1 transcription 8r: AGREE.
  - s1 render 8r: MATCH.
  - f1040 render 12e, 14, 27b: MATCH.
  - f1040 transcription: 12e AGREE. f1040.gate.qdcg_applies and f1040.gate.sdtw were ruled representation from
    triage.
    - qdcg: the 65 value differences all have the SDTW gate true, so line 16 is unaffected. s2.amt_l7 needs the
      inclusive gate.
    - sdtw: no value difference.
- No new findings.

## Step 3: checks

- check_logs (federal) exits 1. Its non-OK lines are:
  - `[claude] f8960`: the transcription log is stale for 5b, because another document's input changed.
  - `[claude] clcw`: the render log reviewed an earlier rendered English. This comes from sd.carryover's helper
    label, which another lane changed.
  - `[claude] f8960`: the render log is stale for 5b.
  - "human reading pending (no H credit)" lines: f1040.line12e; person.age65; and 14 sa lines (sa.extra,
    sa.extra_age65 and sa.extra_blind MISMATCH; sa.standardraw UNCLEAR). Optional under the validation policy.
  - classm [claude] OK (55 forms). rulings: 1671 in logs, all in sidecars.
- check_logs --jurisdiction ny: OK for all kinds (exit 0).
- siblings.py --check exits 1 with 12 problems, none in b1-adj-a-01:
  - Fix lines missing: BUG-0649, b1-adj-a-02, b1-adj-c-01, b1-adj-d-01, b1-adj-ny-01, b1-adj-ny-02.
  - Siblings checked missing: BUG-0653, BUG-0655.
  - No review log changed since the fix, for sibling forms: BUG-0651 (scope), BUG-0675 (scope), BUG-0706 (clcw,
    f8960), BUG-0733 (scope).
- check_bug_inventory exits 1 with 102 lines. Every one is "(a g1 placeholder) is cited
  (docs/provisional/lanes/b1-integration.md) but no pending file exists" (g1-close 16, g1-f6 11, g1-f8 9 and others).
