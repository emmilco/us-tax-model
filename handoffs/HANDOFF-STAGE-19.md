# Handoff: Stage 19 (the education credits), built and reviewed

The third stage of the route to the first coverage goal (`docs/2026-10-26_plan_revision.md` section E). The owner's
decisions are in `research/premises/stage19-education-credits.decisions.md` (all recommended, 2026-10-29);
`sources/2025/PREMISES.md` records them; TASKS.md T-080.

## Scope

- **Computed:** Form 8863 Parts I to III (`forms/2025/f8863.yaml`) for you, your spouse on a joint return and each
  dependent you claim: the American opportunity credit with its MAGI phase-out and the 40% refundable part (Form 1040
  line 29), the line 7 test for filers under 24, the lifetime learning credit with the $10,000 cap per return, and the
  Credit Limit Worksheet (to Schedule 3 line 3). Part III and the Adjusted Qualified Education Expenses Worksheet are on
  each student's person or dependent entry (`person.edu_*`, `dependent.edu_*`), with the arithmetic in one shared
  definition (`forms/2025/aqee.yaml`, D2). Without a Form 1098-T (or an exception) or a TIN the student gets no credit;
  without the filers' TINs or the institution's EIN an American opportunity student goes to line 31 (D4).
- **Refused:** a Form 8862 claim or a ban (`f8863.ban`), an academic period whose tax-free assistance and refunds exceed
  that period's own expenses (D3, `edu_over`), excluded foreign or possession income on lines 3 and 14. Married filing
  separately, nonresident aliens and recapture stay refused as before.
- **Downstream:** Schedule 3 line 3 and line 8; Form 1040 line 29; the four Credit Limit Worksheets that list Schedule 3
  line 3 (`s8812.clw_a2`, `f8880.clw2`, `f5695.rce_ws2`, `f5695.eehi_ws2`); `scope.credits` names the education credits.
- **Coverage:** `education` retired; the estimate is 79.6% (from 75.6%). The 80% goal needs Stage 21 (Form 5329).

## How it was built

- Forms written by `/tmp/s19/gen.py` (scratch; the YAML is authoritative), which checks every quoted citation against
  the archived page before writing. Sources `usc-26-25a` and `f1098t` archived (D9).
- **One addition the owner did not separately rule:** a return-level screen `f8863.paid` ("Did anyone pay qualified
  education expenses in 2025 for you, your spouse or a dependent you claim?") is asked before D2's per-person question,
  so a return without education expenses is asked one question, not one per person; every fixture answers it No.
- **Official examples** (`fixtures/2025/stage19.json`, 14 cases): Pub. 970 Jack and Kay, Bruce and Toni, both phase-out
  examples, the Pell examples, Bill 1 to 3, and Jane example 5 with its three scholarship variants (the Credit Limit
  Worksheet at a $51 tax, Schedule 8812 and the EIC together) all agree with the evaluator.
- **Blind predictions** (`reviews/2025/blind/stage19/`): ten returns, two Opus predictors from the archived text; after
  BUG-0194 they agree with each other and the evaluator on all 427 compared values (348 asserted).
- **Engines:** the generator draws students on about one return in seven (`putEdu`, a derived stream;
  `add_education`). PolicyEngine, Tax-Calculator and UsTaxes compare Form 8863; limitations `edu_no_refund`,
  `edu_phaseout_inexact`, `ustaxes_edu_cents`, `edu_credit_limited`, `ustaxes_edu_no_schedule3`, `education` (OTS).
  Engine differential: 0 unexplained in 562,844 comparisons.
- **Reviews:** fresh Claude and deepseek-flash transcription, render and class M reviews of every changed form,
  adjudicated by Opus agents under `.transcription/proposed/stage19/BRIEF.md` in three rounds (the changed forms were
  re-reviewed after each round's fixes; eic joined in round 2). Archives: `.transcription/archive/before-stage19-2026-10-29/`,
  `stage19-before-round2-2026-10-29/`, `stage19-before-round3-2026-10-29/`.

## Findings (all in BUG_INVENTORY.md)

- BUG-0194 (display): lines after the form's own stops were shown; caught by the blind predictions.
- BUG-0195 (value, pre-existing): the EIC main-home test asked about the filer only, not the spouse on a joint return.
- BUG-0196 (wording): two Form 5695 remedies listed too few computed credits.
- BUG-0197 (question wording): the academic-period screen now compares with the expenses paid to the institution.
- BUG-0198 (over-refusal): the ban refused returns that could take no credit.
- BUG-0199: closes BUG-0192 (the local-law condition, `dependent.lawful`, for `other` and, after round 2's L1,
  `sibling_descendant`) and BUG-0193. The generator answers `lawful` yes without a draw.
- T-081: review-tool and fixture-hygiene points (the class M "CLW n" parse, helpers that cannot be hidden, stray
  W-2 box 10 inputs).

## Facts a fresh session needs

- Every computed line is a target of the interview, so a computed line that reads entry inputs must short-circuit
  before reaching them (`edu_adj` chooses on `edu_student`; `person.edu_kid` is gated by `f8863.kid_needed`, which
  tests line 1 first). A `test all` evaluates every operand when one is unknown, collecting their inputs as pending.
- Orders: `f8863.paid` at 10 (before `sli.claimed`), the per-student questions at 21, the line 7, ban and
  academic-period questions at 31 (after every income question).
- Schedule 3 line 3 and Form 1040 line 29 copy Form 8863 only when `f8863.eligible`, so a return without the form does
  not read its tax lines.
- Next on the route: Stage 21, Form 5329, from its premise map and verification (a decision batch first).
