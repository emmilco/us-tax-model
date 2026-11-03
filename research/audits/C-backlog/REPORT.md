# C-backlog report: T-164, T-165, T-166 (f8962, f1095a)

Branch `claude/A-backlog`, based on `main` at `5eec22f`. Proposed bug entries: `PROPOSED_BUGS.md`
(PENDING-1 to PENDING-3). No paid model review was run; no review log, sidecar, `tools/`,
`BUG_INVENTORY.md`, `TASKS.md`, `TASKS-DONE.md` or handoff was edited.

**Branch shared with another session.** When I first pushed, `origin/claude/A-backlog` already held
another session's work (the B-backlog audit: T-169, T-170, later T-172, T-174, in `forms/2025/sa.yaml`,
`asset.yaml`, `sc.yaml`, `scveh.yaml` and `research/audits/B-backlog/`). I did not force-push. I
rebased my commits onto its tip twice, so the branch interleaves the two sessions' commits. Mine touch
only `forms/2025/f8962.yaml`, `forms/2025/f1095a.yaml`, `interview/questions-2025.yaml`,
`rendered/2025/f8962.md`, `rendered/2025/f1095a.md`, the generated `reports/2025/citations.md`, and
this folder. Each can be cherry-picked on its own. The `citations.md` hunk in each of my commits is
a regenerated count; regenerate it rather than merge it.

| Row | Commit |
| --- | --- |
| T-164 | `9538f6c` |
| T-165 | `07985a1` |
| T-166 | `74936c5` |
| report, proposed bugs | the commit that adds this file |

## T-164 — f8962.premium_adjust: Marketplace coverage, 2025 months

**Premise check (inspected).** The row says the question does not limit "coverage" to Marketplace
coverage and does not say the refunded month is a 2025 month. The question on `main` read "coverage
for anyone in your tax family began after the first day of a month ... or were any Marketplace
premiums for a month refunded in 2025?". Both claims hold. The screen review's WIDE and UNCLEAR
findings, and the ruling that accepts them as over-refusal and points to T-164, are in
`reviews/2025/screens/screen_review.json` and `rulings.json` (`unruled:f8962.premium_adjust`). Source
checked in `sources/2025/i8962.cols.txt`: p. 4 says "coverage in a qualified health plan" and
"refunded in 2025"; p. 5 says catastrophic, stand-alone dental and SHOP plans are not qualified
health plans.

**What changed.** The question now asks whether "Marketplace coverage reported on a Form 1095-A (a
qualified health plan) for anyone in your tax family began after the first day of a 2025 month"
(birth, adoption, placement and court-order carve-outs unchanged), or whether "any premiums for a
2025 month of that Marketplace coverage [were] refunded in 2025". It adds that a start date of other
coverage (employer, Medicaid, a catastrophic, stand-alone dental or SHOP plan) does not count. The
interview help says the same. The cite adds the p. 5 sentence; `citations.py --strict` matched the
quote on p. 5. No expression, gate or remedy changed.

**Regression and prediction.** No expression changed, so no fixture can tell the old wording from
the new, and none was added. Protection check (evaluated on the changed tree):
`stage18.refuse.premium_adjust` inputs with the gate yes refuse at `f8962.line24`, `f8962.line25` and
`s3.line9` with gate `f8962.premium_adjust`. The same inputs with the gate no complete: line 24
$3,560, line 25 $3,500, Schedule 3 line 9 $60.

**Over-refusals still accepted.**
- A 2025 refund that the Marketplace already netted out of column A still reads as yes and is
  refused. The screen reviewer raised this; it is an owner question below.
- The refusal remedy still says "Coverage that began after the first day of a month" without
  "Marketplace". It is shown only after a yes answer, and I left it so the existing regression's
  recorded remedy stays valid.

## T-165 — f1095a column B: "zero if blank"

**Premise check (inspected).** The row and BUG-0298 say the `in_b_<month>` and `mo_b` questions end
"; zero if blank" (BUG-0298: "the 13 questions"). **This premise is only partly true.** The twelve
`f1095a.in_b_<month>` questions ended that way. `f1095a.mo_b` does not and never did on `main`; it
ends at "(from the Marketplace's tool, for example HealthCare.gov/Tax-Tool)". It is asked only when
`f1095a.uniform` is true (all twelve months covered), so a blank month does not arise there. Twelve
questions changed, not 13.

**Reproduced (evaluated, unchanged expressions).** One Form 1095-A, not uniform: January to June
column A $500, column B $450, column C $300; July to December zero. Form 8962 line 24 = $1,782.
With March column B entered as 0, as "zero if blank" invites, the return completes with line 24 =
$1,485: the $297 March credit is lost, and no refusal fires. So the question wording is the only
protection.

**What changed.** The twelve questions end "zero only if no one was enrolled in this policy that
month (column A blank)". That departs from the row's text ("no one was enrolled that month") on
purpose. With two policies that follow one another, both counted under `f1095a.b_counted`, reading
"no one" across policies could lead a filer to enter an SLCSP premium on both forms for the same
month and double column B. That last point is inferred from the `b_counted` question and the p. 16
column (b) rule; I did not evaluate it. No expression changed. The shared cite anchor (`&id003`) was
not touched. The column A and C questions keep "zero if blank", which is right for them.

**Regression and prediction.** None added: no expression changed. The reproduction above is the
evidence.

**Over-refusals.** None introduced (no gate touched). The under-statement path remains reachable if
a filer still enters zero; see the owner question.

## T-166 — f8962.other: define "affordable"

**Premise check (inspected).** The employer limb read "employer-sponsored coverage that was offered
and was affordable and provided minimum value (other than during a waiting period before the
benefits begin)" and did not say whose cost is tested. The premise holds. i8962 p. 5 states the
self-only 9.02% test for the employee, the 9.02% test on the cost for the employee and enrolling
family members, and the "affordable for you but not ... other family members" sentence. All three
are on p. 5 in the archive.

**What changed.** The parenthesis now reads: "the offer is affordable for the employee if the
employee's share of the annual cost of self-only coverage is not more than 9.02% of household income
(Form 8962, line 3), whatever family coverage costs, and for another member of the tax family allowed
to enroll if the employee's share of the annual cost of coverage for the employee and the family
members allowed to enroll is not more than 9.02% of household income". The cite adds the three p. 5
sentences. No expression changed.

An error of mine, caught by `citations.py --strict` before the commit: I first tagged two of the
sentences "p. 6", having read a column break in the archive as a page break. They are on p. 5, and
the committed cite says p. 5.

**Regression and prediction.** None added: no expression changed. Protection check (evaluated): the
`stage18.refuse.premium_adjust` inputs with `f8962.premium_adjust` no and `f8962.other` yes refuse at
`f8962.line24`, `f8962.line25` and `s3.line9` with gate `f8962.other`.

**Over-refusals still accepted.** The Marketplace-determination exception (accurate information to
the Marketplace, which found the offer unaffordable) is still not asked. A filer it covers who
answers yes is refused. This was already ruled acceptable in `unruled:f8962.other`.

## Owner questions

1. **T-165: refuse a covered month with zero column B?** A cited gate could refuse when a month has
   column A above zero and column B zero while `f8962.other` is no. The p. 17 "-0-" rule for unpaid
   premiums is already refused through `f8962.other`. I found no other case in i8962 where a covered
   month in a non-refused return has a zero applicable SLCSP premium, but I did not search Pub. 974.
   Whether to add the gate is a scope choice, so I did not.
2. **T-164: a refund already netted in column A.** i8962 p. 4 defines enrollment premiums as net of
   2025 refunds and says column A "reports the enrollment premiums". If the Marketplace's column A
   already reflects a refund, no adjustment is needed, but the question still draws a yes and a
   refusal. Should the question exclude refunds already reflected in column A? The source does not
   say whether Marketplaces net them.
3. **T-166: compute the 9.02% test?** The question asks the filer to compare against household
   income (line 3), which the interview computes only later. Computing the test would need new
   inputs (each employee's self-only and family contributions). That is new computation and a
   scope choice, so I only stated the rule in the question.
4. **Branch naming.** Two sessions were pointed at `claude/A-backlog`. If that was not intended,
   the integrator should take my three commits by cherry-pick.

## Rows not done

None. All three rows changed wording only. Their review reruns are left to the integrator: f8962
screen, transcription, render and completeness (T-164, T-166); f1095a transcription and render, and
f8962 again (T-165).

## Checks run

On my T-164 tree (`main` + T-164 only, before rebasing):
- `node engine/dist/main.js test-fixtures`: 1,437/1,437 passed.
- `tools/check_consumers.py`, `tools/check_instruction_cites.py`, `tools/citations.py --strict` and
  `tools/coverage/tree.py --check`: all exit 0.

On the final combined tree at `74936c5` (includes the other session's commits):
- `test-fixtures`: 1,439/1,439 passed.
- `check_instruction_cites.py` exit 0; `citations.py --strict` exit 0.
- `check_consumers.py` exit 1: 22 new and 2 stale findings, all on `asset.*` and `sc.*` lines (the
  other session's forms), none on f8962 or f1095a.
- `coverage/tree.py --check` exit 1 at `74936c5`: `docs/COVERAGE.md` was out of date on the Form
  4562 asset screen line (the other session's change). The other session's report commit `f50061b`
  regenerated it and the stale `rendered/2025/asset.md`, `sc.md`, `scveh.md` and `index.md`. On
  `f50061b` plus my report commit, `tree.py --check` passes, `npm run render` leaves no diff,
  `citations.py --strict` exits 0, and `check_consumers.py` still exits 1 with the same 22 new
  and 2 stale asset/sc findings, which that session's `research/audits/A-backlog/consumers_proposed.json`
  addresses. `test-fixtures` was not rerun after `f50061b`; that commit changes only generated pages
  and reports.

Not run: `check-all`, `check_logs.py`, mutation, `siblings.py --check`, and all model reviews.
`siblings.py` was run for `f8962.premium_adjust`, `f8962.other` and `f1095a.in_b_jan` (sibling sets
are in `PROPOSED_BUGS.md`). No new inputs were added, so `siblings.py --input` had nothing to
ripple. This is not a green suite.

## Inspected versus inferred

- **Inspected or evaluated:** the question texts on `main`; the i8962 archive text for every quote
  (verified by `citations.py`); the screen-review findings and rulings; the four evaluations above
  (T-164 gate yes and no, T-165 March column B zero, T-166 `f8962.other` yes); the check outputs.
- **Inferred, not evaluated:** that a cross-policy reading of "no one was enrolled" could double
  column B. That no other legitimate zero-column-B covered month exists (i8962 only). That the
  remaining over-refusals cannot understate any amount.

Branch tip after the report commit: see `git log -1 origin/claude/A-backlog`. Rows finished: T-164,
T-165, T-166.
