# Proposed bug entries (package "tooling": T-139, T-140, T-142, T-144, T-146, T-147, T-148; T-163 proposal)

Ids are placeholders; the integrator assigns BUG numbers. None of these changes a tax value on a supported
return. They are review-tool, generator and fixture defects, recorded so the changes have entries.

## PENDING-1 — Class M jobs for single documents gave incoming values that only validation helpers read, and were not marked printed-only

- **Caught by:** T-139 (from T-066; owner's decision 2026-10-29), premise check on the current tree, 2026-11-03.
- **Source:** BUG-0143 (the same defect, fixed for collection documents only): an incoming-value catalog should hold what the printed calculation reads, not what implementation validation reads.
- **Symptom:** `buildJob` (engine/src/classm.ts) listed as authoritative givens every foreign line that any line of the document reads, helpers included, and set no `worked_scope`, so the request did not say that only printed lines are wanted and the log did not record the scope. Measured on the full job set (2,000 generated returns plus non-M fixtures, seed 7): see REPORT.md, T-139, for the documents and givens withheld.
- **Fix:** `buildJob` keeps a given only if the printed lines requested read it through the document's own lines (`requestClosure`, the same rule `buildCollectionJob` applies to printed-only collections), and marks the job `worked_scope: "printed-irs-lines"`. `tools/transcription/classm.py` states the printed-only sentence in the single-document request as it already did in the entry request (one shared constant, byte-identical for collections). No old receipt is relabeled: a document migrates when its class M review is next rerun.
- **Fix lines:** none (tool change: `engine/src/classm.ts` `buildJob`, `requestClosure`; `tools/transcription/classm.py` `build_prompt`, `PRINTED_ONLY`).
- **Siblings checked:** `buildCollectionJob` printed-only filter (unchanged; same rule), `buildDefJob` (definitions give only their parameters), `classm.py` `write_outputs` (the "worked target scope" row now appears for single documents).
- **Regression predictions:** `tools/transcription/test_classm_jobs.mjs`: every Form 2441 job is `printed-irs-lines`.
- **Validation:** job generation before and after on the full corpus (REPORT.md); test_classm_jobs.mjs; no model call.
- **Tags:** review-tool; worked-context-feedback; class-m; fixed

## PENDING-2 — Class M requests showed workers answers the route never reads, and the generated cases held answers the interview never asks

- **Caught by:** T-142 (Stage 18 O2, from T-079 (2)) and T-147 (Stage 19, from T-081 (5)); premise checked 2026-11-03.
- **Source:** the interview asks exactly the inputs the evaluation from its targets reads (`engine/src/interview.ts`, `interviewState`: "missing reachable inputs determine the questions").
- **Symptom:** (1) the generator answers both routes of a Form 1095-A so every line computes under `evaluateAll`, and the class M entry request listed all of them: a uniform entry showed `mo_a`, `mo_b`, `c_total` and all 36 monthly amounts, and the job asked for the month-by-month totals `yr_a_monthly`, `yr_b_monthly`, `yr_c_monthly` that only the untaken alternative of lines 33a to 33c reads; a month-by-month entry showed `mo_a`, `mo_b` and `c_total`, which after whole-dollar rounding need not agree with its months (O2), and models copied them. (2) The class M fixtures carry every generated answer, including answers the interview cannot give because nothing on the return's route reads them: `classm.f5695.2` holds `person[taxpayer].sav_claimed` true with `sa.dependent` false (`person.sav_ineligible` tests `sa.dependent` first and stops), `classm.f5695.8` and `classm.s3.3` hold `person[taxpayer].sav_excess` true with no Form W-2 box 12 deferrals (`person.sav_excess_gate` tests `person.sav_w2 > 0` first). Evaluated: none of the three answers is read from the interview's targets or the cases' expectations.
- **Fix:** `routeJob` in `engine/src/classm.ts`, applied to every chosen job: an unprinted collection's helpers are requested only when some route reads them (`liveInCollection`); the answers shown are those the requested lines read (`answersRead` over a lazy evaluation from the requested lines); the fixture inputs keep rosters, the filing status and the answers read from the full interview's targets or by the requested lines. The requested values must be identical on the restricted answers (checked with `evaluateAll`); otherwise the job keeps every answer and the problem is printed. A job's branches are those the restricted answers take. The generator itself is unchanged: both routes stay answered there because evaluateAll-based tools (class M candidate filters, mutation, triage) need every line computed. The three named cases and their DeepSeek twins drop the unread answer (fixtures/2025/classm.json, classm.deepseek.json).
- **Fix lines:** none (tool and fixture change).
- **Siblings checked:** every other class M case on the tree carries generator answers off its route (the same two saver's credit answers alone appear in 11 more Claude and 3 more DeepSeek cases, counted by input values); they are fixed when each document's class M review is regenerated. `buildDefJob` (definition jobs reach their instance through the calling lines, `defCallers`).
- **Regression predictions:** for the six edited cases, no expected value changes (the dropped answers are not read; prediction from the short-circuit order of `person.sav_ineligible` and `person.sav_excess_gate`, f8880 p. 2 "Who Can Take This Credit" and iw2w3 p. 20 box 12). test_classm_jobs.mjs: no Form 1095-A entry shows the other route's answers or requests the other route's totals; no Form 2441 case holds `sav_claimed` without `sa.dependent` Yes.
- **Validation:** test-fixtures; job generation before and after on the full corpus (REPORT.md); test_classm_jobs.mjs.
- **Tags:** review-tool; generator; class-m; unasked-answers; fixed

## PENDING-3 — Mutation report did not say which kills only class M cases made

- **Caught by:** T-144 (Stage 19: person, f2441 and ira kills lost on a class M rerun; from T-081 (6)).
- **Source:** none (tooling).
- **Symptom:** `outcome` in `engine/src/mutate.ts` stopped at the first case that killed a mutant, in file order, so the report could not tell a kill that depends on a class M case (which a class M rerun regenerates) from one a stage fixture also makes. `classm.py` already warns that replaced cases may carry kills, but not which.
- **Fix:** reporting only: non-M cases are tried first; a mutant no other case kills but a class M case does is still killed, counted under "Killed by fixtures", and listed in a new report section "Killed only by class M cases" with the first class M case that kills it; the console line gives the count. No equivalence rule, mutant or score definition changed.
- **Fix lines:** none (`engine/src/mutate.ts` `outcome`, `runMutation` report).
- **Siblings checked:** `mutantShare`/`outcomesOf` (workers pass the outcome strings through unchanged); `classm.py` `write_outputs` replacement warning (unchanged; it now has a report to consult).
- **Regression predictions:** the score and survivor set are unchanged (the kill/survive decision is the same set of cases); only attribution is added.
- **Validation:** a sample of the mutant list through `mutantShare` (REPORT.md); the full count is the parent's check-all mutate step.
- **Tags:** mutation; reporting; class-m; fixed

## PENDING-4 — The review interface did not say that the Schedule D carryover lines hold a negative amount

- **Caught by:** T-140 (Stage 20 adjudication, T-076 (3)).
- **Source:** f1040sd p. 1, lines 6 and 14 printed "( )"; i1040sd p. 11, 28% Rate Gain Worksheet line 5 "( )"; p. 13, Unrecaptured Section 1250 Gain Worksheet line 16 "( )".
- **Symptom:** the transcription prompt publishes only id, printed marker and type (`reference_note` and the requested-line list in tools/transcription/transcribe.py), so a candidate holding `sd.line6`, `sd.line14`, `g28.line5` or `u1250.line16` positive is a sign convention gap, not a reading error, yet triage reports value differences on every line that combines them.
- **Fix:** `NEGATIVE_INTERFACES` and `sign_note` in transcribe.py add "a loss carryover printed in parentheses, held as a negative amount" to those four lines, both where they are requested and where another form's catalog lists them.
- **Fix lines:** none (tool change).
- **Siblings checked:** the other signed Dollars lines whose labels say "negative" (`clcw.prior_11`, `clcw26` line 15 input, the worksheet helpers `sd.line6_ws`, `sd.line14_ws`) are not printed parenthesised interfaces read by another form's transcription; not changed.
- **Regression predictions:** the required-interface check (`input_context.assess`) of the saved g28 and u1250 transcription requests now reports `sd:sd.line14` missing (verified: g28 Claude and DeepSeek went from pass to fail; u1250 was already failing on `scope.schedule1` / `sales.special`). No other saved request lists these four lines as foreign interfaces.
- **Validation:** test_review_tools.py, test_input_context.py; the audit above. The integrator reruns sd, g28 and u1250 transcription.
- **Tags:** review-tool; interface; sign-convention; fixed

## PENDING-5 — Eleven Stage 18 to 21 fixtures carried a stray W-2 box 10 with Form 2441 benefits answered No

- **Caught by:** T-146 (Stage 19, from T-081 (4)); 11 cases found on the current tree (the task lists 11).
- **Source:** the generator's screen rule (engine/src/generate.ts `SCREENS`: box 10 is asked only after `f2441.benefits` Yes); `w2.box10` input text, "zero if the box is blank"; the cases' fact sheets state no dependent care benefits.
- **Symptom:** `stage18.blind.p6`, `p10`, `p20`, `stage18.refuse.year_of_marriage`, `stage18.mut.family_of_20`, `stage18.refuse.family_over_20`, `stage19.blind.e2`, `e4`, `stage20.blind.r7`, `stage21.blind.e7`, `stage21.refuse.e05_joint` held `person[taxpayer].w2[e0].box10` = $1,000 with `f2441.benefits` false.
- **Fix:** the eleven values set to 0 by a line-local text edit (formatting kept).
- **Fix lines:** none (fixtures).
- **Siblings checked:** every fixture file for a nonzero box 10 or box10_wages without `f2441.benefits` Yes: none remain.
- **Regression predictions:** no expected value changes. None of the cases asserts a Form 2441, line 1e or box 10 line; with benefits No, Part III is not reached and line 1e is zero, so the line 1e attribution helpers that read box 10 do not affect any asserted line (i2441 p. 5, Line 12, "Amounts you received as an employee should be shown in box 10 of your Form(s) W-2").
- **Validation:** test-fixtures.
- **Tags:** fixtures; stray-input; fixed

## PENDING-6 — Generated returns left three dependent answers unanswered

- **Caught by:** T-148 (Stage 21, from T-081 (7)); premise re-checked 2026-11-03.
- **Source:** dependent.yaml, `dependent.hoh_lived_half` and `dependent.dc_lived_half` read `dependent.born_died` and `dependent.placed` (then `dependent.part_year_home`) for a person who is not a qualifying child and lived with you half the year or less.
- **Symptom:** on the seeded sample (1,000 returns, seed 7), 4 returns reached `dependent[].born_died`, `placed` and `part_year_home` unanswered (20, 4 and 4 derivations). `f1040.line24` and `f1040.line37` were not unknown on any of the 1,000 (in two the unknown was masked, two refused elsewhere), so the task's "line 24 is unknown" premise no longer holds as stated; the unanswered inputs do.
- **Fix:** `buildInputs` (engine/src/generate.ts) answers `born_died` and `placed` No for every dependent, after every draw, so neither the random stream nor the derived streams move. `part_year_home` is then never reached.
- **Fix lines:** none (generator).
- **Siblings checked:** the same probe over all reached unknown inputs for `f1040.line24` and `f1040.line37` on 1,000 returns: none remain after the change.
- **Regression predictions:** no generated return reaches a dependent answer unanswered; other generated values are unchanged (keys added last).
- **Validation:** the probe (REPORT.md).
- **Tags:** generator; unanswered-input; fixed
