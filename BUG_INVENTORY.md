# Bug inventory

Append-only record of every defect caught in this repository, kept so that
patterns across defects can be seen. Entries are never edited or removed; a
correction to an entry is a new entry that cites it. `check-all` fails if the
committed prefix of this file has changed.

Each entry records: the sequential id; the date; how it was caught (which
check, test, engine or reading); the symptom; the root cause; where the
defect lived; how it was fixed and in which commit; and pattern tags for
later grouping.

---

## BUG-0001 — Form 1040 line 9 double-counted qualified dividends

- **Date:** 2026-10-16
- **Caught by:** engine differential scout (PolicyEngine-US 2.49.4 and Tax-Calculator 6.8.5 both reported total income 2,000.00 below the project's on fixture `stage5.return.itemized`); confirmed against `sources/2025/f1040.txt` line 80.
- **Symptom:** total income, AGI, taxable income and tax too high by the qualified-dividend amount on every return with qualified dividends.
- **Root cause:** `forms/2025/f1040.yaml`, line `f1040.line9`, summed `f1040.line3a` in addition to `f1040.line3b`. The form text reads "Add lines 1z, 2b, 3b, 4b, 5b, 6b, 7a, and 8"; line 3a is a component of 3b, not an addend. The line's own label was transcribed correctly while its operand list was not.
- **Why it survived:** the Lean reference evaluator agreed because it reads the same data; mutation testing cannot flag an extra operand that every fixture's recorded expectation already contains; the 17 fixtures with qualified dividends had expectations recorded from the engine; the Stage 5 review packet narrated the owed case as "dividends 3,500.00" where the inputs were 2,000.00 ordinary including 1,500.00 qualified, so the narrative absorbed the error.
- **Fix:** removed `f1040.line3a` from the sum. Eleven anchored fixtures (Stage 1, 3 and 4) had their W-2 box 1 raised by the qualified-dividend amount so their designed taxable income is unchanged; the two Stage 5 whole-return fixtures kept their inputs and had their expectations re-recorded; the Stage 5 review packet arithmetic was corrected; one integration check (`engine/src/integration.ts`) carried the wrong amount owed as a literal and was corrected.
- **Tags:** transcription/operand-list; label-correct-expr-wrong; same-data-blind-spot; recorded-expectation-laundering; caught-by-external-engine

---

## BUG-0002 — Tax Computation Worksheet row guards contradicted "not over"

- **Date:** 2026-10-17
- **Caught by:** transcription agreement (spec 6.5): the isolated second transcription of `tcw` read each row as "at least / over X but not over Y" with an inclusive upper bound; the project's guards were strict at the upper bound. Confirmed against `sources/2025/i1040gi.txt`, 2025 Tax Computation Worksheet, Sections A–D.
- **Symptom:** none in values. An amount exactly on a row boundary (for example $103,350 single) was routed to the next row; the worksheet's subtraction amounts make the tax continuous at every boundary, so the computed tax was identical (checked at the four single-status breakpoints before and after the fix). The rendered English of the guards, and the encoding's claim to follow the text, were wrong.
- **Root cause:** `forms/2025/tcw.yaml`, every `*.result` line: the row intervals were encoded as `[lower, upper)` for all four filing-status sections, 16 upper bounds strict and 16 lower bounds inclusive, against text that reads `[100,000, upper]` for row 1 and `(previous upper, upper]` after. The build-time checker (`engine/src/check.ts`) only accepted half-open seams with the upper side exclusive, which made the strict form the path of least resistance.
- **Why it survived:** value-neutral, so no fixture, engine comparison, mutation or evaluator agreement could see it; the checker's seam rule enforced the wrong-way convention; no human had read the rendering against the page.
- **Fix:** the 32 bounds rewritten to match the text; the checker's seam rule changed to require that exactly one side of a seam includes the seam point, so either convention passes and gaps or double inclusion still fail. Fixture, evaluator agreement and breakpoint values unchanged.
- **Tags:** transcription/guard-inclusivity; value-neutral; checker-shaped-the-data; caught-by-second-transcription

---

## BUG-0003 — Helper label on `person.overcount` described a different line

- **Date:** 2026-10-17
- **Caught by:** reading the rendered helper references while building the render comparison (spec 6.5). The renderer was changed to name helper lines by their labels instead of the bare marker "(helper)", and the rendering of `person.over` then read `helper "Total w2.one for this person" > 0`, which is the label of `person.employers`, not a description of the count of employers over the withholding limit.
- **Symptom:** none in values. The authored label of `person.overcount` ("Total w2.one for this person") described `person.employers`; the line's expression counts the W-2 entries whose box 4 exceeds the limit. Every rendering and explanation that named the line misdescribed it.
- **Root cause:** `forms/2025/person.yaml`, line `person.overcount`: the label was carried over from the neighbouring line when the line was authored and never corrected.
- **Why it survived:** value-neutral, so no fixture, engine, mutation or evaluator check could see it; the transcription comparison compares expression trees and ignores labels; the renderer showed helper references as "(helper)" with no label, so the wrong label was never displayed where the line was used.
- **Fix:** label changed to "Number of employers that withheld more than the limit". No expression, fixture or log changed.
- **Tags:** label-wrong-expr-right; value-neutral; authoring/copied-label; caught-by-render-reading

---

## BUG-0004 — Form 8959 screen did not name uncollected Medicare tax in W-2 box 12

- **Date:** 2026-10-17
- **Caught by:** render comparison (spec 6.5): the isolated model judged Form 8959 line 19 a MISMATCH because the instructions say "Also include any uncollected Medicare tax on tips from Form W-2, box 12, code B, and any uncollected Medicare tax on the taxable cost of group-term life insurance over $50,000 (for former employees) from Form W-2, box 12, code N" (i8959 p. 4) and no refusal named those amounts.
- **Symptom:** a filer with a box 12 code B or N amount would have line 19 (Medicare tax withheld) understated with no refusal; the screen question `f8959.unsupported` asked only about self-employment income, RRTA compensation, Form 4137 tips and Form 8919 wages.
- **Root cause:** `forms/2025/f8959.yaml`, line `f8959.unsupported`: the screen question was written from the lines it gates on Form 8959 and did not carry the line 19 instruction's two further sources.
- **Why it survived:** value-neutral for every fixture and generated return (none carries a box 12 amount; the W-2 collection has no box 12 field); the transcription comparison compares expression trees and sees nothing in a question's wording; no human read the line against the page.
- **Fix:** the question now names uncollected Medicare tax in Form W-2 box 12 (codes B or N). No expression changed.
- **Tags:** scope-screen-narrower-than-line; value-neutral; caught-by-render-comparison

---

## BUG-0005 — Schedule A screen did not name the generation-skipping tax deduction

- **Date:** 2026-10-17
- **Caught by:** render comparison (spec 6.5): Schedule A line 6 ("Other taxes") is pinned to zero behind the `sa.unsupported` screen, and the model judged it a MISMATCH because the instructions say "Include on this line income taxes you paid to a foreign country and generation-skipping tax (GST) imposed on certain income distributions" (i1040sca p. 7) while the screen named only the foreign tax deduction.
- **Symptom:** a filer with a deductible GST amount would have line 6 at zero with no refusal.
- **Root cause:** `forms/2025/sa.yaml`, line `sa.unsupported`: the screen question listed the foreign tax deduction and not the second item of the same instruction sentence.
- **Why it survived:** as BUG-0004: value-neutral for every fixture and generated return; invisible to tree comparison; no human reading.
- **Fix:** the question now names the generation-skipping tax deduction. No expression changed.
- **Tags:** scope-screen-narrower-than-line; value-neutral; caught-by-render-comparison

---

## BUG-0006 — Schedule A screen did not name points not reported on Form 1098

- **Date:** 2026-10-17
- **Caught by:** render comparison (spec 6.5): Schedule A line 8c ("Points not reported to you on Form 1098") is pinned to zero behind the `sa.unsupported` screen, and the model judged it a MISMATCH because the screen named "mortgage interest not on Form 1098" and not points.
- **Symptom:** a filer with points paid but not reported on Form 1098 would have line 8c at zero with no refusal, unless they read points as mortgage interest when answering the screen.
- **Root cause:** `forms/2025/sa.yaml`, line `sa.unsupported`: the screen question was written from line 8b's wording and did not name line 8c's item.
- **Why it survived:** as BUG-0004.
- **Fix:** the question now names mortgage interest or points not on Form 1098. No expression changed.
- **Tags:** scope-screen-narrower-than-line; value-neutral; caught-by-render-comparison

---

## BUG-0007 — Taxable income before the QBI deduction omitted Form 1040 line 13b

- **Date:** 2026-10-17
- **Caught by:** render comparison (spec 6.5): the isolated model judged Form 8995 line 11 and Form 8995-A line 33 MISMATCH against the corrected instruction "Form 1040 or 1040-SR, line 11a, minus lines 12e and 13b" (i8995-correction), because the restatement subtracted only line 12e from adjusted gross income.
- **Symptom:** none in values. Line 13b (Schedule 1-A deductions) is zero in this slice and refused through `scope.schedule1a`, so the omission could not change a number; the expression did not say what the instruction says and would have become wrong the moment Schedule 1-A came into scope.
- **Root cause:** `forms/2025/qbi.yaml`, line `qbi.taxable_before`: encoded as AGI less the Schedule A deduction, with the citation's own locator recording that line 13b was left out because the slice refuses it. A refused line was dropped from an expression instead of being carried as the zero it is.
- **Why it survived:** value-neutral; the transcription comparison compares trees after expansion and the second transcriber was given the same scope note; no human reading.
- **Fix:** a helper sums lines 12e and 13b and the subtraction takes that sum, so the refusal on line 13b now propagates and the expression reads as the instruction does. Values unchanged on every fixture.
- **Tags:** refused-line-dropped-from-expression; value-neutral; caught-by-render-comparison

---

## BUG-0008 — Other-income screen did not name the Form 1040 line 1b–1h items

- **Date:** 2026-10-17
- **Caught by:** render comparison (spec 6.5): Form 1040 line 1z is encoded as line 1a alone, and the model judged it a MISMATCH against "Add lines 1a through 1h" because no refusal named lines 1b–1h. The items are refused through `scope.other_income` at line 8, but that screen asked about "other income/return treatment outside wages", which a filer with tips not on a Form W-2 or household employee wages would not recognise.
- **Symptom:** a filer with a line 1b–1h amount could answer the screen No and have line 1z understated with no refusal.
- **Root cause:** `forms/2025/scope.yaml`, line `scope.other_income`: the screen was written for lines 4b–6b and 8 and did not carry the wage-like items of lines 1b–1h that it also stands in for.
- **Why it survived:** as BUG-0004: value-neutral for every fixture and generated return; invisible to tree comparison; no human reading.
- **Fix:** the question now names wages or tips not on a Form W-2, Medicaid waiver payments, dependent care or adoption benefits and other earned income (Form 1040 lines 1b–1h). Line 1z must become the sum of lines 1a–1h when those lines come into scope (already recorded in the transcription rulings). No expression changed.
- **Tags:** scope-screen-narrower-than-line; value-neutral; caught-by-render-comparison

---

## BUG-0009 — Line-16 screen gated only `scope.ready`, not Form 1040 line 16

- **Date:** 2026-10-17
- **Caught by:** render comparison (spec 6.5): the model judged Form 1040 line 16 a MISMATCH because the instructions say "Include in the total on the entry space on line 16 all of the following taxes that apply" (Forms 8814, 4972, section 962, education credit recapture, Forms 8621 and 8978) and no refusal on the line named them. The screen `scope.other_line16` exists, but unlike the other four scope screens, which also gate the lines they stand in for (lines 8, 10, 13b and the credit lines), it gated only `scope.ready`.
- **Symptom:** the whole-return interview reports the return refused (scope.ready is a target), so no prepared return was wrong; the command-line evaluation showed a computed tax on line 16 beside a refused `scope.ready`, and the refusal did not propagate through lines 16–37 as spec 6.3 requires of a fired gate.
- **Root cause:** `forms/2025/f1040.yaml`, line `f1040.line16`: no `refuses` entry for `scope.other_line16`.
- **Why it survived:** the interview-level refusal masked it; the refusal-propagation property only checks lines whose operands are refusals; no human reading.
- **Fix:** line 16 now refuses when `scope.other_line16` is true, with the same citation as the other scope gates. Values unchanged on every fixture.
- **Tags:** scope-screen-not-wired-to-line; refusal-propagation; caught-by-render-comparison

---

## BUG-0010 — Gift screen did not name the clothing or household item Section B case

- **Date:** 2026-10-17
- **Caught by:** render comparison (spec 6.5): the model judged the per-gift `gift.allowed` line a MISMATCH because Form 8283 Section B is also required for "a single article of clothing or household item that is not in good used condition or better and for which you are claiming a deduction of over $500" (i8283 p. 3), a case below the $5,000 threshold that `gift.section_b` tests, and the screen `gift.special` did not name it.
- **Symptom:** a filer deducting more than $500 for such an item could answer the screen No and have the deduction allowed without the Section B refusal.
- **Root cause:** `forms/2025/gift.yaml`, line `gift.special`: the screen listed the appraisal and special-treatment categories and not this one.
- **Why it survived:** as BUG-0004: value-neutral for every fixture and generated return; invisible to tree comparison; no human reading.
- **Fix:** the question now names a clothing or household item not in good used condition claimed at over $500. No expression changed.
- **Tags:** scope-screen-narrower-than-line; value-neutral; caught-by-render-comparison

---

## BUG-0011 — Relationship enum conflated categories the dependent tests separate

- **Date:** 2026-10-17
- **Caught by:** render comparison (spec 6.5) on the new dependent worksheet, before the stage was committed: the model judged `dependent.qr_relationship` and `dependent.hoh_person` MISMATCH because the `sibling` value covered every descendant of a sibling where Step 4 admits only "a son or daughter of any of them" (i1040gi p. 19), and the `parent` value covered ancestors and siblings of a parent where Head of Household Test 1 admits only "your parent" (i1040gi p. 14).
- **Symptom:** a grandniece who lived with the filer less than the whole year would have passed the qualifying-relative relationship test; a grandparent or aunt whose home the filer kept up would have qualified the filer for head of household under Test 1.
- **Root cause:** `params/2025.yaml`, enum `dependent_relationship`: one value each for the sibling and parent families, written from Step 1's broader wording, where Step 4 and Test 1 draw a narrower line.
- **Why it survived:** the encoding was hours old; the generated corpus does not produce the distant relatives; no fixture had one.
- **Fix:** two values added, `sibling_descendant` (a qualifying-child relationship only) and `parent_relative` (a Step 4 relative but not a Test 1 parent); the two tests read the split values.
- **Tags:** enum-value-over-inclusive; household-predicates; caught-by-render-comparison; pre-commit

---

## BUG-0012 — Head of household Test 1 demanded the filer's own home cost

- **Date:** 2026-10-17
- **Caught by:** render comparison (spec 6.5) on the new household form, before the stage was committed: the model judged `household.hoh_eligible` MISMATCH because it required the "paid over half the cost of keeping up your home" answer for every qualifying person, while Test 1 is met by keeping up the parent's home, who "didn't have to live with you" (i1040gi p. 14).
- **Symptom:** a filer who met only Test 1 and answered the own-home question No would have been refused head of household.
- **Root cause:** `forms/2025/household.yaml`: one eligibility test combined both tests' persons behind the Test 2 home-cost condition.
- **Why it survived:** as BUG-0011.
- **Fix:** the per-dependent line splits into Test 1 and Test 2, the household form counts each, and eligibility is unmarried and (Test 1 met, or Test 2 met with the own-home cost).
- **Tags:** condition-attached-to-wrong-branch; household-predicates; caught-by-render-comparison; pre-commit

---

## BUG-0013 — Taxpayer TIN question did not name the applied-for ITIN

- **Date:** 2026-10-17
- **Caught by:** render comparison (spec 6.5) on the new household form, before the stage was committed: Step 5, question 1 says to answer Yes "if you are applying for an ITIN on or before the return due date (including extensions)" (i1040gi p. 19); the question asked only about an issued SSN or ITIN.
- **Symptom:** a filer who had applied for an ITIN would answer No and lose the credit for other dependents.
- **Root cause:** `forms/2025/household.yaml`, line `household.taxpayer_tin`: the question was written from the first clause of the step's question.
- **Why it survived:** as BUG-0011.
- **Fix:** the question now names the applied-for ITIN, as the dependent's own TIN question already did.
- **Tags:** scope-screen-narrower-than-line; household-predicates; caught-by-render-comparison; pre-commit

---

## BUG-0014 — Months-lived question did not carry the born-or-died exception

- **Date:** 2026-10-17
- **Caught by:** render comparison (spec 6.5) on the dependent worksheet, before commit: the model judged `dependent.lived_half` MISMATCH because "more than 6 months" ignores "the person is considered to have lived with you for more than half of 2025 if your home was this person's home for more than half the time the person was alive in 2025" and the same rule for adoption and placement (i1040gi p. 14, Exception to time lived with you).
- **Symptom:** a child born in the second half of 2025 who lived with the filer from birth would have failed the residency test.
- **Root cause:** `forms/2025/dependent.yaml`, line `dependent.months`: the question carried the temporary-absence rule and not the born-or-died rule.
- **Why it survived:** as BUG-0011.
- **Fix:** the question tells the filer to enter 12 for a person born, died, adopted or placed in 2025 whose home was the filer's for more than half the time alive or with them, and 0 otherwise. No expression changed.
- **Tags:** scope-screen-narrower-than-line; household-predicates; caught-by-render-comparison; pre-commit

---

## BUG-0015 — Sibling category still broader than Step 4; all-year relatives not counted (corrects BUG-0011)

- **Date:** 2026-10-17
- **Caught by:** render comparison (spec 6.5) rerun after BUG-0011: the model judged `dependent.qr_relationship` MISMATCH on two counts: Step 4 admits "a son or daughter" of a brother, sister, half brother or half sister but not of a stepbrother or stepsister, which the `sibling` value still included; and a `sibling_descendant` who "lived with you all year as a member of your household" is a Step 4 relative under the last bullet, which the test excluded (i1040gi p. 19).
- **Symptom:** a stepsibling's child would have passed the qualifying-relative relationship test without living with the filer all year; a grandniece who did live with the filer all year would have failed it.
- **Root cause:** BUG-0011's split put step siblings' children on the Step 4 side, and the all-year bullet was tied to one enum value.
- **Why it survived:** the first fix was read against the Step 1 wording, which does admit step siblings' descendants.
- **Fix:** the `sibling` value now ends at the children of a brother, sister, half brother or half sister; any other relationship (`sibling_descendant`, `household_member`, `other`) is a Step 4 relative when the person lived with the filer all year.
- **Tags:** enum-value-over-inclusive; household-predicates; caught-by-render-comparison; pre-commit; corrects-BUG-0011


## BUG-0016 — Rerunning a review tool silently dropped standing rulings

- **Date:** 2026-10-17
- **Caught by:** the mutation tool's baseline check, after the class M rerun on `s8812` (T-020): `mutation baseline mismatch: classm.s8812.1 s8812.line13`. The rerun had reproduced the same 15 disagreements with the same project and model values, yet 9 of the 15 standing rulings came back `Ruling: open`, and the re-admitted model value (a blank read as $0.00 for line 13) was written into `fixtures/2025/classm.json` as a class M expectation.
- **Symptom:** on any rerun of `classm.py`, `transcribe.py` or `render_compare.py`, a ruling on a disagreement whose section follows an agreeing section is lost; for a class M log the model's value then re-enters the fixture file as evidence. Rulings on a disagreement that follows another disagreement survive, which is why 6 of 15 were kept.
- **Root cause:** `existing_rulings` in all three tools matched the section heading with `### (\S+) — .*?\n` under `re.S`, so the lazy remainder could run from an agreeing section's heading across its body to the next `Status: **DISAGREE**`; the ruling was then keyed under the agreeing line's number and never looked up.
- **Why it survived:** the three tools had been rerun rarely and only after data changes, when reopened rulings looked like the expected consequence of changed keys (the Stage 8 handoff says as much); the log checker only requires that no ruling be open at commit time, which a fresh run with lost rulings satisfies once someone rules again.
- **Fix:** the heading remainder is anchored to its line (`[^\n]*`) in all three parsers; the `s8812` log was restored from the previous commit and re-derived offline from the saved responses with all 15 rulings kept. A parse count over every committed log (transcription, render, class M) shows the fixed parsers recover all 235 non-open rulings, where the old parsers keyed 148 of them correctly and would have lost 87 on rerun.
- **Tags:** tooling; regex-spans-sections; ruling-loss; recorded-expectation-laundering; caught-by-mutation-baseline


## BUG-0017 — Months-lived question gave every person the qualifying-child born-or-died rule

- **Date:** 2026-10-17
- **Caught by:** render comparison (spec 6.5), rerun on the reading-order text after T-022: the model judged `dependent.months` MISMATCH because the question told every person born, died, adopted or placed in 2025 to enter 12 when the home was theirs for more than half the time alive, while the instructions give that rule to a qualifying child only and say of anyone else "Any other person is considered to have lived with you for all of 2025 if the person was born or died in 2025 and your home was this person's home for the entire time the person was alive in 2025" (i1040gi p. 21, Exception to time lived with you; p. 15 for head of household).
- **Symptom:** a household-member dependent born mid-year who lived with the filer for most but not all of their life would have passed the all-year test.
- **Root cause:** `forms/2025/dependent.yaml`, line `dependent.months`: the BUG-0014 fix carried the qualifying-child rule into the question without its condition.
- **Why it survived:** the render comparison that produced BUG-0014 read the interleaved layout text; the rerun on reading-order text is the first in which the model quoted the "any other person" sentence.
- **Fix:** the question states both rules, keyed on whether the person meets the other qualifying-child conditions; the citation names p. 21. No expression changed.
- **Tags:** scope-screen-wider-than-line; household-predicates; caught-by-render-comparison; corrects-BUG-0014; reading-order-text

---

## BUG-0018 — TIN question counted a pending SSN application

- **Date:** 2026-10-17
- **Caught by:** render comparison rerun (as BUG-0017): "Answer 'Yes' if you are applying for an ITIN or ATIN for the child" (i1040gi p. 18, Step 3, question 1); the question said "or have you applied for one by then", which includes an SSN application.
- **Symptom:** a child with an SSN applied for but not issued by the due date would have been counted for the credits.
- **Root cause:** `forms/2025/dependent.yaml`, line `dependent.tin`: the question generalised the parenthetical.
- **Why it survived:** as BUG-0017.
- **Fix:** the question names an ITIN or ATIN application. No expression changed.
- **Tags:** scope-screen-wider-than-line; household-predicates; caught-by-render-comparison; reading-order-text

---

## BUG-0019 — "Younger than you" compared whole-year ages

- **Date:** 2026-10-17
- **Caught by:** render comparison rerun (as BUG-0017): the model noted that comparing whole-year ages "misses a child born later in the same age year" (i1040gi p. 17, Step 1, "and younger than you").
- **Symptom:** a sibling of the same whole-year age as the filer, younger by months, failed the qualifying-child age test.
- **Root cause:** `forms/2025/dependent.yaml`, line `dependent.younger`, tested the person's age below the filer's age, both in whole years (`household.taxpayer_age`).
- **Why it survived:** the generated corpus never pairs a filer and a dependent of the same whole-year age; no fixture did.
- **Fix:** `dependent.younger` is a question the filer answers; `household.taxpayer_age` is removed from the household form, the four interview profiles, the generators and the engine differential cases; every fixture dependent carries the answer derived from the ages it had (144 dependents), so no expected value changed.
- **Tags:** derived-where-asked-is-needed; household-predicates; caught-by-render-comparison; reading-order-text

---

## BUG-0020 — Household-member relationship omitted the local-law condition

- **Date:** 2026-10-17
- **Caught by:** render comparison rerun (as BUG-0017): Step 4's last bullet admits "Any other person (other than your spouse) who lived with you all year as a member of your household if your relationship didn't violate local law" (i1040gi p. 19); the relationship question's household-member value said only "any other person who lived with you all year".
- **Symptom:** a person whose relationship violated local law would have been admitted as a qualifying relative.
- **Root cause:** `forms/2025/dependent.yaml`, line `dependent.relationship`: the value's description dropped the condition.
- **Why it survived:** as BUG-0017.
- **Fix:** the value's description carries the condition and the spouse exclusion. No expression changed.
- **Tags:** scope-screen-wider-than-line; household-predicates; caught-by-render-comparison; reading-order-text

---

## BUG-0021 — Head of household Test 2 excluded only one of the three all-year relationship values (corrects BUG-0015)

- **Date:** 2026-10-17
- **Caught by:** render comparison rerun (as BUG-0017): Test 2 excludes "Any person who is your dependent only because the person lived with you for all of 2025" (i1040gi p. 14); after BUG-0015 three relationship values (`household_member`, `sibling_descendant`, `other`) are dependents only through the all-year bullet, and `dependent.hoh_test2` excluded `household_member` alone.
- **Symptom:** a grandniece or an unrelated person claimed through the all-year bullet would have qualified the filer for head of household.
- **Root cause:** BUG-0015 widened the all-year bullet to three values without widening the Test 2 exclusion that mirrors it.
- **Why it survived:** the BUG-0015 render comparison judged `qr_relationship`, not `hoh_test2`; no fixture had a non-household-member all-year dependent on a head of household return.
- **Fix:** the first branch of `dependent.hoh_test2` excludes all three values.
- **Tags:** condition-attached-to-wrong-branch; household-predicates; caught-by-render-comparison; corrects-BUG-0015; reading-order-text

---

## BUG-0022 — Credit refusals still named Schedule 8812 as unsupported

- **Date:** 2026-10-17
- **Caught by:** render comparison rerun (as BUG-0017): the model judged `scope.credits` UNCLEAR because the screen exempts the Schedule 8812 credits while its refusal is titled "Schedule 8812 / other credit forms".
- **Symptom:** a refusal message naming a schedule the tool computes.
- **Root cause:** five refusal entries (`forms/2025/f1040.yaml` lines 29 to 31, `s3.yaml`, `scope.yaml`) written before Stage 8 encoded Schedule 8812 and not revisited.
- **Why it survived:** refusal titles are not compared by any check; the Stage 8 render comparison judged the new lines, not the old refusals that mention them.
- **Fix:** the five entries are titled "Other credit forms (Schedule 3 lines 2 to 4, 5b, 6d, 6f, 6l and 6m; Form 1040 lines 27a and 29 to 31)" and their remedy names the credits the slice does compute.
- **Tags:** stale-text-after-scope-change; caught-by-render-comparison


## BUG-0023 — Citizenship question omitted the adopted-child rule

- **Date:** 2026-10-17
- **Caught by:** render comparison rerun on the reading-order text after BUG-0017 to BUG-0022: an adopted child of a U.S. citizen or national who "lived with you all year as a member of your household ... meets the requirement to be a U.S. citizen in Step 2, question 1; Step 3, question 2; Step 4, question 2; and Step 5, question 3" (i1040gi p. 20, Exception to citizen test); the question asked only about actual citizenship, nationality or residence.
- **Symptom:** such a child would have been denied dependency and both credits.
- **Root cause:** `forms/2025/dependent.yaml`, line `dependent.citizen`: the question was written from the step questions without the "Exception to citizen test" paragraph.
- **Why it survived:** as BUG-0017; the earlier comparison read the spliced columns.
- **Fix:** the question carries the rule in a parenthetical. No expression changed.
- **Tags:** scope-screen-narrower-than-line; household-predicates; caught-by-render-comparison; reading-order-text

---

## BUG-0024 — The "other" relationship value lacked the all-year bullet's conditions (completes BUG-0020)

- **Date:** 2026-10-17
- **Caught by:** render comparison rerun (as BUG-0023): the model judged `dependent.qr_relationship` MISMATCH because the `other` value qualifies through the same bullet as `household_member` when the person lived with the filer all year, and BUG-0020 added the bullet's conditions ("other than your spouse", "if your relationship didn't violate local law", i1040gi p. 19) to the household-member value only.
- **Symptom:** a person entered as `other` whose relationship violated local law would have been admitted as a qualifying relative.
- **Root cause:** BUG-0020's fix attached the conditions to one of the three values that share the bullet (`sibling_descendant`, the third, is a blood relation and is not affected by the local-law condition).
- **Why it survived:** the BUG-0020 render comparison was ruled on the household-member wording.
- **Fix:** the `other` value's description states the conditions. No expression changed.
- **Tags:** scope-screen-wider-than-line; household-predicates; caught-by-render-comparison; corrects-BUG-0020

---

## BUG-0025 — Review tools read the first YAML block of a response, not the finished one

- **Date:** 2026-10-17
- **Caught by:** ruling the class M rerun on the reading-order text: `classm.f1040.1` lines 33, 34 and 37 showed "Model: $0.00, Work: placeholder" and "no answer", while the saved response ended with the agreeing values ($56,000.00, $0.00, $68,722.52).
- **Symptom:** a model response holding an abandoned draft block (ending at line 33 with a placeholder) followed by a complete block was parsed from the draft, turning agreements into disagreements and missing lines.
- **Root cause:** `extract` in `tools/transcription/classm.py`, `render_compare.py` and `transcribe.py` took the first fenced block (`re.search`).
- **Why it survived:** every earlier response had one block; a scan of the 102 saved responses of this rerun found this one with two.
- **Fix:** the three tools take the last fenced block. `classm.py --doc f1040 --from-response` re-derived the log: 105 agreements, no disagreement.
- **Tags:** review-tool-parsing; caught-by-ruling

---

## BUG-0026 — `table_lookup` turned a refused key into an unknown

- **Date:** 2026-10-17
- **Caught by:** the `refusal_propagates` property after Stage 9 added EIC Table lookups keyed by Form 1040 line 11b: with Schedule 1 refusing the adjusted gross income, `eic.line3_table0` evaluated to `unknown` ("lookup key or status missing") instead of the refusal.
- **Symptom:** a lookup whose key or status was refused reported a missing input rather than the refusal and its citation; the Lean reference evaluator (`isUnknown` covers refusals) passed the refusal through, so the two evaluators would have disagreed on such a line.
- **Root cause:** `engine/src/eval.ts`, case `table_lookup`, tested only that the key was money and the status an enum.
- **Why it survived:** the Tax Table's keys (taxable income inside the tax computation) are reached only after the screens that refuse them have already ended the return; no earlier key could be refused at the lookup.
- **Fix:** the case returns an unknown or refused key or status unchanged, as every other atom does.
- **Tags:** evaluator; refusal-propagation; caught-by-property

---

## BUG-0027 — The months-lived question left out adoption and placement for a person who is not a qualifying child

- **Date:** 2026-10-17
- **Caught by:** Stage 9 render comparison of `dependent.months`: the "Exception to time lived with you" (i1040gi p. 21) treats any person other than a qualifying child as living with you all year if born or died in 2025, "or if you adopted the person in 2025, the person was lawfully placed with you for legal adoption by you in 2025, or the person was an eligible foster child placed with you during 2025" and your main home was the person's main home for the entire time since.
- **Symptom:** a household member adopted or placed with the filer during 2025 would have been entered with fewer than 12 months and lost qualifying-relative status through the all-year household bullet.
- **Root cause:** `forms/2025/dependent.yaml`, `dependent.months`: the source text gave the adoption and placement route to qualifying children only; the four interview prompts carried an older wording that did not separate the two groups at all.
- **Why it survived:** the Stage 8 render comparison read the column-spliced p. 21 before T-025 fixed the reading-order text of the flow-chart pages.
- **Fix:** the question and every interview prompt carry the full exception for both groups. No expression changed.
- **Tags:** scope-screen-narrower-than-line; household-predicates; caught-by-render-comparison; reading-order-text

---

## BUG-0028 — The EIC lived-in-the-United-States question left out adoption and placement

- **Date:** 2026-10-17
- **Caught by:** Stage 9 render comparison of the new `dependent.us_half`: the EIC's "Exception to time lived with you" (i1040gi p. 43) counts a child adopted, lawfully placed for adoption or placed as an eligible foster child in 2025 if your main home was the child's main home for more than half the time since.
- **Symptom:** such a child could have been answered "no" and dropped from the EIC count.
- **Root cause:** the question was written from the temporary-absence and birth-or-death sentences only.
- **Why it survived:** caught at the first review of the line.
- **Fix:** the question and its interview prompt carry the adoption and placement sentence.
- **Tags:** scope-screen-narrower-than-line; household-predicates; caught-by-render-comparison

---

## BUG-0029 — The months-lived question counted any detention and lost part-month stays

- **Date:** 2026-10-17
- **Caught by:** Stage 9 render comparison of `dependent.months` and `dependent.lived_half`: the exception counts "detention in a juvenile facility" (i1040gi p. 21), not any detention; and the test "lived with you for more than half of 2025" is encoded as more than 6 whole months, so a person who lived with the filer 6 months and some days would be entered as 6 and fail.
- **Symptom:** an adult detained elsewhere could have been counted as living with the filer; a person living with the filer just over half the year could have failed the residency test.
- **Root cause:** `forms/2025/dependent.yaml`, `dependent.months`: the question shortened the instructions' wording and asked for whole months without saying how to enter a stay of more than half the year but fewer than seven full months.
- **Why it survived:** as BUG-0027; the earlier comparison read the spliced p. 21.
- **Fix:** the question says "detention in a juvenile facility" and "enter 7 if the person lived with you for more than half of 2025 but fewer than 7 full months", so "more than 6" is "more than half of 2025". No expression changed.
- **Tags:** scope-screen-wider-than-line; scope-screen-narrower-than-line; household-predicates; caught-by-render-comparison; reading-order-text

---

## BUG-0030 — The EIC lived-in-the-United-States question left out the military rule

- **Date:** 2026-10-17
- **Caught by:** render comparison of `dependent.us_half` after the owner's Stage 9 rulings: "If you were on extended active duty outside the United States, your main home is considered to be in the United States during that duty period" (i1040gi p. 44, Members of the military, to which p. 45, United States, refers).
- **Symptom:** a child living with a parent on extended active duty abroad could have been answered "no" and dropped from the EIC count.
- **Root cause:** the per-person question was written from the Step 3 box and the exception paragraph; the filer-level question `eic.us_home` carried the military rule, the per-person one did not.
- **Why it survived:** the earlier render comparison of the line was ruled on the adoption sentence (BUG-0028).
- **Fix:** the question and its interview prompt carry the military rule. No expression changed.
- **Tags:** scope-screen-narrower-than-line; household-predicates; caught-by-render-comparison

---

## BUG-0031 — The test harness killed an evaluation whose output passed 1 MiB

- **Date:** 2026-10-17
- **Caught by:** `check-all` after the class M rerun for the owner's Stage 9 rulings: `classm.dependent.1` failed with "eval exited null" although the command-line program, run directly on the same inputs, exits 0.
- **Symptom:** a fixture whose values sheet is larger than 1,048,576 bytes (this one, a return with several dependents, is 1,055,871) fails as if the program had crashed.
- **Root cause:** `spawnSync` in `engine/src/fixtures.ts`, `integration.ts` and `compare.ts` used Node's default output buffer of 1 MiB, past which the child is killed and the status is null.
- **Why it survived:** every earlier fixture's output was under 1 MiB; the new per-person EIC lines pushed this return over.
- **Fix:** every spawn passes `maxBuffer: 256 MiB`.
- **Tags:** test-harness; caught-by-check-all

---

## BUG-0032 — Scope screens narrower than the lines they stand in for (T-008)

- **Date:** 2026-10-17
- **Caught by:** the screen review (`tools/transcription/screen_review.py`, adjudicated in `reviews/2025/screens/screen_review.md`): an isolated model read each screen against the archived pages of every line it gates.
- **Symptom:** a filer could truthfully answer no to a screen and have an unsupported item computed as zero. Examples: never-married parents living apart (`dependent.divorced_rule`); a dependent widowed during 2025 filing jointly (`dependent.married`); church employee income and W-2 box 8 allocated tips (`f8959.unsupported`); a refund of a deduction taken on an earlier Form 8960 that is not taxable (`f8960.refund`); investment expenses other than interest (`f4952.unsupported`); the $5,000 appraisal test across donees and for a single item (`gift.special`); Form CT-2 employee representatives (`person.rrta`); a QBI list readable as excluding what it meant to catch (`qbi.unsupported`); Schedule 2 amounts called repayments, interest or penalties (`s2.other`); combat pay not shown with code Q (`s8812.combat_pay`); filing Form 2555 with no excluded amount (`sa.excluded_income`); sales of entity interests holding collectibles or section 1250 property and the full collectibles list (`sales.special`); market discount and contingent payment debt instruments (`sb.unsupported`); Schedule 3 amounts that are not credits (`scope.credits`); a nonresident alien spouse, W-2 Medicaid waiver payments and passive activity gains (`scope.other_income`); Forms 8621 and 8978 and filing Form 8814 with no tax (`scope.other_line16`); Schedule SE, statutory-employee Schedule C and the line 8s exclusion (`scope.schedule1`); a Schedule 1-A deduction the filer qualifies for but did not plan to claim (`scope.schedule1a`); carryovers from years before 2024 (`sd.carryover`); section 1256 contracts and casualties not yet on a form (`sd.other_forms`). Twenty-five screens were reworded in all; one round-1 rewording (`gift.special`) itself lost the single-item case and was repaired in round 2.
- **Root cause:** each screen was written from the lines it gates, in shorthand, without a check that its wording reaches every situation those lines' instructions cover (the pattern of BUG-0004, 0005, 0006, 0008 and 0010).
- **Why it survived:** the render comparison judges a screen against its own citation, not against the lines it stands in for.
- **Fix:** the 25 screens' questions, labels and interview prompts were reworded; findings covered by a sibling screen gating the same lines, WIDE findings and minor unclear wording were accepted and recorded.
- **Tags:** scope-screen-narrower-than-line; caught-by-screen-review

---

## BUG-0033 — A collection-form line claimed `display` but was never evaluated or shown

- **Date:** 2026-10-18
- **Caught by:** building the Stage 10 fixtures: the hand predictions for Simplified Method Worksheet lines 10 and 11 (`retirement.smw10`, `retirement.smw11`) found no value in `eval --json`, and mutation left every operand change on those lines alive.
- **Symptom:** `retirement.smw11` was marked display ("shown so the filer knows whether next year's payments are fully taxable"), but no Form 1040 line reads it or line 10, so neither was ever computed, and the values sheet prints no collection entry lines at all; the filer was shown nothing.
- **Root cause:** evaluation targets are the lines of non-collection forms; a collection entry's line is evaluated only when a reader reaches it. The unread-line check in `engine/src/build.ts` accepted `display` as the reason an unread line exists without asking whether the line could ever be shown.
- **Why it survived:** before Stage 10 no collection form had a display line (they appear only in `div`, `sa` and `sb`, which are not collections).
- **Fix:** lines 10 and 11 are removed (the owner's ruling; they carry forward to next year and change nothing on the 2025 return); the build rejects `display` on any line of a collection form. Showing collection entry lines on the values sheet is T-030.
- **Tags:** dead-logic; build-check-gap; caught-by-fixture-prediction

---

## BUG-0034 — The EIC age test refused a filer born on January 1, 1961

- **Date:** 2026-10-18
- **Caught by:** the render comparison of Form 1040 lines 27a and 27c in the Stage 10 review pass: "Check 'Yes' if you ... were born after December 31, 1960, and before January 2, 2001" (i1040gi p. 41, Step 4, question 2).
- **Symptom:** a filer with no qualifying child born on January 1, 1961 failed Step 4 and got no earned income credit.
- **Root cause:** Step 4 read the standard-deduction question `sa.age65` ("born before January 2, 1961"), whose boundary is one day later than the EIC's "born after December 31, 1960"; the two tests differ for exactly that birth date.
- **Why it survived:** the Stage 9 fixtures and generated returns never put a filer on that date, and the earlier render comparison of the line did not compare the two boundaries.
- **Fix:** the EIC asks its own question in the instructions' words (`eic.born_after_1960`, the owner's ruling); `stage9.eic.no_child.born_jan1_1961` asserts the credit for that birth date.
- **Tags:** boundary-off-by-one; reused-input-different-rule; caught-by-render-comparison

---

## BUG-0035 — Schedule 1-A gave married filing separately the tips, overtime and senior deductions

- **Date:** 2026-10-18
- **Caught by:** the Stage 12 transcription agreement and render comparison of `s1a` (lines 13, 21 and 36a): "If married, you must file jointly to claim this deduction" (Schedule 1-A Parts II, III and V cautions).
- **Symptom:** a married-filing-separately return would have received the three deductions at the single-filer amounts.
- **Root cause:** the encoding chose amounts by filing status (lines 9, 15, 17, 32) but carried no must-file-jointly condition; the cautions sit above each part, not on a numbered line.
- **Why it survived:** married statuses are refused for whole returns (`s3.married`), so no fixture or generated return reached the lines with that status.
- **Fix:** lines 13, 21 and 36a are zero for married filing separately (`s1a.line13_claim`, `line21_claim`, `line36a_claim`); fixture `stage12.mfs.bar`. Stage 12 commit.
- **Tags:** caution-not-on-a-line; unreachable-status; caught-by-transcription; caught-by-render-comparison

---

## BUG-0036 — The overtime question never asked for overtime outside Form W-2 box 1

- **Date:** 2026-10-18
- **Caught by:** the Stage 12 transcription agreement of `s1a` line 14a: the second transcription noted "No input covers this" for qualified overtime not included in box 1 (i1040gi p. 108, line 14a).
- **Symptom:** the owner had approved accepting deferred overtime, but `otjob.statement` asked only for statement amounts, so a filer would not enter it.
- **Root cause:** the decision was taken into the arithmetic (no cap at box 1) but not into the question wording.
- **Fix:** the question (form source and the three interviews) now says to include overtime not in box 1. Stage 12 commit.
- **Tags:** decision-not-in-question; caught-by-transcription

---

## BUG-0037 — Schedule 1-A refused every Form 2555 filer, claimed or not

- **Date:** 2026-10-18
- **Caught by:** predicting the Stage 12 fixtures by hand: a Form 2555 filer claiming nothing on Schedule 1-A should not need its Part I.
- **Symptom:** `f1040.line13b` refused through `sa.excluded_income` on every such return.
- **Root cause:** line 30 chose between its branches by line 27, which reads modified AGI (line 3, and so the refused lines 2a to 2d), even when no car loan interest was claimed.
- **Fix:** line 30 is zero when no car loan interest is claimed; `stage12.excluded_income_no_claim` and `stage12.refuse.excluded_income`. Stage 12 commit.
- **Tags:** unguarded-read; refusal-too-broad; caught-by-fixture-prediction

---

## BUG-0038 — Batch evaluation failed on a large corpus

- **Date:** 2026-10-18
- **Caught by:** the engine differential run (`tools/engines/run.sh`) after Schedule 1-A entered the generated cases: `RangeError: Invalid string length` in `engine/src/main.ts`.
- **Symptom:** `eval --batch` built the whole `{ cases }` document as one string, longer than V8 allows (the output is about 940 MB).
- **Root cause:** the document grows with lines and derivations per case; Schedule 1-A's lines pushed it past the limit.
- **Fix:** batch mode writes the same document one case at a time. Stage 12 commit.
- **Tags:** tool-scaling; caught-by-engine-differential

---

## BUG-0039 — Engine adapters compared less than they could, and one adapter fed an imputation

- **Date:** 2026-10-18
- **Caught by:** investigating the Schedule 1-A differences in the engine differential.
- **Symptom:** (1) PolicyEngine-US added modeled Medicare Part B premiums ($2,220) to the medical expenses of every filer 65 or older; (2) Tax-Calculator ran in its smoothed mode, so its phase-outs (and the child tax credit's) differed from the printed $1,000 steps and the `ctc_phaseout` exclusion hid comparisons that exact mode passes; (3) Tax-Calculator's forced itemizing pass zeroed the standard deduction but not its addition for age.
- **Root cause:** adapter defaults: `medicare_enrolled` not supplied; `Records(exact_calculations=False)`; `STD_Aged` not zeroed. Before Stage 12 every generated filer was 40, which hid (1) and (3).
- **Fix:** the adapters supply `medicare_enrolled: false`, run Tax-Calculator with `exact_calculations=True` (the `ctc_phaseout` exclusion is removed) and zero `STD_Aged` in the forced pass. Stage 12 commit.
- **Tags:** adapter-default; comparison-weaker-than-possible; fixed-age-blind-spot; caught-by-engine-differential

---

## BUG-0040 — An engine-limitation flag fired on returns it did not concern

- **Date:** 2026-10-18
- **Caught by:** an engine investigation entry (gen-00053, a float32 difference) that stopped being used although its difference remained.
- **Symptom:** `schedule1a_stepped_phaseout` excluded PolicyEngine-US's taxable income and tax on every return above the Schedule 1-A thresholds, including returns that claim nothing on Schedule 1-A.
- **Root cause:** Schedule 1-A's phase-out lines are figured from modified AGI whether or not their part is claimed; the flag tested the reduction alone.
- **Fix:** the flag also requires the part's capped amount (line 7, 15 or 24) to be positive. Stage 12 commit.
- **Tags:** exclusion-too-broad; hidden-comparison; caught-by-stale-investigation

---

## BUG-0041 — Citations by section gave the reviewers no source text

- **Date:** 2026-10-18
- **Caught by:** the dry run of the Stage 12 transcription prompts: `n-25-69 pages []` and `fr-2025-24154 pages []`.
- **Symptom:** the isolated reviewers of `otjob` and `carloan` would have checked those lines without Notice 2025-69 or proposed § 1.163-16 in front of them.
- **Root cause:** the review tools take a document's pages from `p.`/`pp.` in the locator; the Stage 12 locators named sections only.
- **Fix:** every locator citing the two documents names its pages (Notice 2025-69 pp. 22-25; the regulation pp. 20-22). Stage 12 commit.
- **Tags:** citation-without-page; review-input-gap; caught-by-dry-run

---

## BUG-0042 — Schedule 1-A filled out parts that did not apply, and left line 4a at column (d)

- **Date:** 2026-10-18
- **Caught by:** class M of `s1a` (44 lines: "Part IV not filled", "Part V not filled") and the render comparison of line 4a.
- **Symptom:** the values sheet showed modified AGI, thresholds and phase-out amounts in parts the filer must not fill out (the deductions were unaffected); line 4a showed the worksheet's column (d), not column (b), the Form W-2 or Forms 4070 figure the line asks for.
- **Root cause:** the "Fill out Part N only if" conditions were applied only to each part's result line.
- **Fix:** each printed line of Parts II to V is $0 unless its part applies (the owner's choice of the strictly accurate reading); line 4a enters column (b). Stage 12 commit.
- **Tags:** caution-not-on-a-line; presentation-fidelity; caught-by-class-m; caught-by-render-comparison

---

## BUG-0043 — Lines that are zero within scope did not say why

- **Date:** 2026-10-18
- **Caught by:** the Stage 12 render comparison of `s1a` lines 4b, 5, 14b and 36b and `tipjob` column (c): "Always enters $0 and has no refusal".
- **Symptom:** the encoding entered zero on lines whose amounts come from refused forms (Form 4137, a trade or business, a spouse), with the refusal carried only elsewhere.
- **Root cause:** the zero relied on refusals on other lines; the line's own data did not name them. A first fix keyed line 36b to `s3.married` and refused every married return, including isolated worksheet fixtures; it was caught by the fixture run and keyed to `sa.spouse_extra` instead.
- **Fix:** each line carries its refusal (`s2.other`, `scope.schedule1`, `sa.spouse_extra`); `stage12.refuse.*` fixtures. Stage 12 commit.
- **Tags:** implicit-refusal; caught-by-render-comparison

---

## BUG-0044 — A values sheet left out the lines of an entry that no total needed

- **Date:** 2026-10-19
- **Caught by:** the class M fixtures of `f8889` ("line3: not evaluated") after Form 8889 became an entry of each person in Stage 13.
- **Symptom:** `eval` without `--target`, `evaluateAll`, mutation testing and the coverage report evaluated only top-level lines, so a line of a collection entry appeared only when a top-level line demanded it. With no HSA contributions, Form 8889 line 13 takes zero and lines 3 to 12 were never figured or shown; the same held for any unused line of a dependent, a W-2 or a sale.
- **Root cause:** the default target list was built from forms without a `collection` key.
- **Fix:** `allTargets` adds every line of every confirmed entry (whose parent entries are confirmed); `evaluate` accepts an entry line such as `person[taxpayer].f8889[hsa].line3` as a target. Stage 13 part 1 commit.
- **Tags:** incomplete-values-sheet; caught-by-class-m-fixtures

---

## BUG-0045 — A first joint-return SSN rule changed an unmarried filer's Schedule 1-A Part II

- **Date:** 2026-10-19
- **Caught by:** the fixture run (`classm.s1a.1`: lines 8 to 10 became $0).
- **Symptom:** Part II (and Part III) applied only if a person with a valid SSN had a tip (or overtime) employer entered, so an unmarried filer who claimed tips with no employer entered no longer had the modified AGI lines filled in.
- **Root cause:** the joint-return condition ("the spouse who received the qualified tips must have a valid SSN") was applied to every filing status, though the instructions say "You have a valid SSN" first and add the spouse condition only for a joint return.
- **Fix:** `s1a.tip_ssn` and `s1a.ot_ssn` read the taxpayer's SSN unless filing jointly, and a receiving spouse's SSN on a joint return. Stage 13 commit.
- **Tags:** status-scoped-condition; caught-by-fixtures

---

## BUG-0046 — A spouse's decedent refusal made every return ask the decedent question

- **Date:** 2026-10-19
- **Caught by:** the build's interview checks ("missing or repeated question person[taxpayer].died_before_65").
- **Symptom:** placing the refusal for a spouse who died before reaching 65 on Schedule 1-A line 36b, which every return computes, made the decedent question reachable on every return, and it counted both spouses for the taxpayer's line 36a.
- **Root cause:** a refusal's condition is evaluated whenever its line is; line 36a carries its refusal on a helper reached only for a filer born before January 2, 1961.
- **Fix:** each spouse has a decedent gate; the spouse's refusal is on `s1a.line36b_senior`, reached only for a spouse who qualifies. Stage 13 commit.
- **Tags:** refusal-reachability; caught-by-interview-check

---

## BUG-0047 — A dependent's age test asked only whether the person was younger than you

- **Date:** 2026-10-19
- **Caught by:** the Stage 13 render comparison of `dependent` ("a child older than you but younger than your joint-filing spouse would fail").
- **Symptom:** on a joint return a child younger than your spouse but not younger than you failed the qualifying-child age test.
- **Root cause:** the question kept its single-filer wording when married filing jointly came into scope; the earlier ruling rested on married statuses being refused.
- **Fix:** the question asks whether the person was younger than you or, on a joint return, your spouse (i1040gi p. 17; Pub. 501 p. 13). Stage 13 commit.
- **Tags:** stale-scope-ruling; joint-return-wording; caught-by-render-comparison

---

## BUG-0048 — The Form 8889 screen did not name a spouse's Archer MSA

- **Date:** 2026-10-19
- **Caught by:** the Stage 13 render comparison of `f8889` line 4.
- **Symptom:** Form 8889 line 4 also includes amounts contributed to your spouse's Archer MSA when you or your spouse had family coverage, but the screen asked only about contributions by you or your employer, so line 4 could be $0 when it should not.
- **Root cause:** the spouse clause of line 4 had no reader while married filers were refused.
- **Fix:** `f8889.unsupported` names contributions to your spouse's Archer MSA in that case. Stage 13 commit.
- **Tags:** stale-scope-ruling; screen-gap; caught-by-render-comparison

---

## BUG-0049 — The child tax credit's test for the other spouse accepted an ITIN application

- **Date:** 2026-10-19
- **Caught by:** the Stage 13 render comparison of `household` (`id_count`).
- **Symptom:** one question asked for an SSN or ITIN issued by the due date "or applied for an ITIN by then", so a spouse who had only applied for an ITIN satisfied the child tax credit's rule that the other spouse's number "must have been issued on or before the due date".
- **Root cause:** the question was written for the credit for other dependents (Step 5, question 1 allows an application) and reused for the child tax credit.
- **Fix:** `person.tin` asks for an issued number and `person.itin_applied` for an application; the credit for other dependents accepts either, the child tax credit's other-spouse test only the first. Stage 13 commit.
- **Tags:** reused-question; joint-return-rule; caught-by-render-comparison

---

## BUG-0050 — The PDFKit extraction check failed footnote markers joined to amounts

- **Date:** 2026-10-19
- **Caught by:** `check-all` (`tools/check_extraction.py`, PDFKit against poppler) on archiving Pub. 463 and Pub. 946 for Stage 14.
- **Symptom:** `p463` p. 29 and `p946` pp. 60 and 61 failed with 7 or 8 words "only PDFKit" reads, such as `1601` and `0604`; check-all stopped before the fixtures.
- **Root cause:** the tables of maximum depreciation for cars place a footnote marker right after an amount. Poppler reads the marker as its own token (`160`, `1`) and PDFKit joins it to the number (`1601`). On all three pages every PDFKit-only word was exactly a poppler-only number plus a poppler-only digit, so no text was lost; the check counted that as loss.
- **Where:** `tools/check_extraction.py`, `check_pdfkit`, whose same-text rules covered only a line label read as one token or two ("14a", "14 a").
- **Fix:** a second same-text rule: a PDFKit word that is a poppler-only number followed by a poppler-only digit is the same text. The extraction report changed only for `p463`, `p560` (one occurrence under the tolerance) and `p946`.
- **Tags:** checker-false-positive; reader-tokenization; caught-by-check-all

---

## BUG-0051 — Two worksheets left out Schedule 1 lines 15 to 17

- **Date:** 2026-10-19
- **Caught by:** the engine differential with self-employment returns (PolicyEngine-US and Tax-Calculator agreed on taxable social security benefits, Form 1040 line 6b, below the project's on se-00011, se-00075 and se-00163).
- **Symptom:** taxable social security benefits, and with them AGI and taxable income, too high on returns with social security benefits and a Schedule C, since the deductible part of self-employment tax was not subtracted; the student loan interest deduction would have been figured on too high a modified AGI.
- **Root cause:** Stage 14 added Schedule 1 lines 15, 16 and 17 but did not extend the two worksheets that list the Schedule 1 adjustments line by line: the Social Security Benefits Worksheet, line 6, and the Student Loan Interest Deduction Worksheet, line 3, both "Enter the total of the amounts from Schedule 1, lines 11 through 20, and 23 and 25", summed only lines 11 and 13.
- **Where:** `forms/2025/ssb.yaml` (`ssb.line6`) and `forms/2025/sli.yaml` (`sli.line3`).
- **Fix:** both sum lines 11, 13, 15, 16 and 17; the refusal remedy of `ssb.line6` names the lines still outside the tool.
- **Tags:** new-line-missed-by-reader; transcription/operand-list; caught-by-external-engine

---

## BUG-0052 — Mutation operand replacement did not change keyed lookup keys

- **Date:** 2026-10-19
- **Caught by:** review of the Stage 14 mutation survivors (dozens of `operand.*` survivors on `keyed_lookup` lines, each replacing a key with a line of the lookup's result type).
- **Symptom:** every operand mutant of a `keyed_lookup` key survived, inflating the unexplained survivors and leaving the keys of the depreciation tables untested by mutation.
- **Root cause:** `engine/src/mutate.ts` listed the keys as operands (added with the atom) but chose the replacement by the type of the mutated line (a Rate for a rate lookup) rather than of the key, and its `apply` did not rewrite `keys`, so the mutant was the original expression.
- **Where:** `engine/src/mutate.ts`, operand replacement.
- **Fix:** a key is replaced by an earlier same-document line of the key's own type, and `apply` rewrites `keys`; the other atoms are unchanged, so earlier mutant ids and outcomes stand.
- **Tags:** tool-defect; mutation-blind-spot; new-atom-integration; caught-by-review

---

## BUG-0053 — Schedule 8812 line 21 left out one-half of the Additional Medicare Tax on self-employment income

- **Date:** 2026-10-19
- **Caught by:** the Stage 14 transcription agreement for `s8812` (the second transcription added worksheet line 7; the disagreement was ruled against the archived page).
- **Symptom:** on a return with Additional Medicare Tax on self-employment income (Form 8959 line 13 above zero), Schedule 8812 line 21 was low by one-half of that tax; line 25, and with it the additional child tax credit for three or more children, could be too low.
- **Root cause:** the Additional Medicare Tax and RRTA Tax Worksheet (i1040s8812 p. 9) was encoded through line 6 only, when no return in scope had self-employment income. Line 7, "Enter one-half of the Additional Medicare Tax, if any, on self-employment income (one-half of Form 8959, line 13)", and line 16, "Add lines 6, 7, 11, and 15", were not extended when Stage 14 made Form 8959 line 13 reachable.
- **Where:** `forms/2025/s8812.yaml` (`s8812.line21`).
- **Fix:** helpers `s8812.amt_ws6` (line 6) and `s8812.amt_ws7` (line 7, at the 50% parameter), and line 21 is their sum (line 16; lines 11 and 15, Tier 1 RRTA, are refused through the Form 8959 screen); `stage14.f8959.se_above_threshold` now expects line 21.
- **Tags:** new-line-missed-by-reader; transcription/operand-list; caught-by-transcription-agreement

---

## BUG-0054 — The transcription comparison paired lines that share a printed number

- **Date:** 2026-10-19
- **Caught by:** ruling the Stage 14 transcription log for `sc` (Schedule C line 3 was compared with the second transcription's Form 7206 line 3, and so on).
- **Symptom:** on a form that carries more than one IRS worksheet with the same line numbers (Schedule C with the simplified home office worksheet and Form 7206; the vehicle record; the EIC with Worksheet B), most printed lines were reported as disagreements between unrelated lines, and an agreement could have been reported between unrelated lines.
- **Root cause:** `tools/transcription/transcribe.py` keyed both transcriptions by printed number (the second's by a dictionary, so the last of several lines won) and expanded a reference to a printed line as that number, so lines sharing a number were indistinguishable. Every form before Stage 14 had unique printed numbers. The render comparison already qualified a shared marker by the line id.
- **Where:** `tools/transcription/transcribe.py` (`build_prompt`, `Expander.ref`, `compare`).
- **Fix:** `marker_keys` qualifies a printed number that several lines of the form share by the line id, as the render comparison does, in the prompt, in references and in the matching; markers such as `(gate)` and `(screen)` are left as they were, so the prompt of every form without shared numbers is unchanged (checked against the logged prompt hashes). `sc`, `scveh` and `eic` were transcribed again.
- **Tags:** tool-defect; comparison-blind-spot; caught-by-review

---

## BUG-0055 — Schedule 8812 line 18a was negative where the Earned Income Worksheet says to stop

- **Date:** 2026-10-19
- **Caught by:** the Stage 14 transcription agreement for `s8812` (the second transcription encoded the stop at worksheet line 3; ruled against the archived page).
- **Symptom:** on a return not taking the EIC whose Earned Income Worksheet line 3 is zero or less while Schedule 1 line 15 is above zero (a joint return where one spouse's Schedule C profit carries self-employment tax and the other's loss is larger), line 18a showed minus the deductible part of self-employment tax instead of zero. Line 19 floors at zero, so the credit was unchanged.
- **Root cause:** worksheet line 3, "If zero or less, stop. Do not complete the rest of this worksheet. Instead, enter -0- on ... line 18a of Schedule 8812" (i1040s8812 p. 8), was encoded as a floor at zero on line 3 with line 7 still subtracting line 6. Before Stage 14 line 6 was always zero, so the two readings agreed.
- **Where:** `forms/2025/s8812.yaml` (`s8812.eiw_7`).
- **Fix:** `s8812.eiw_7` is zero when line 3 before the stop is zero or less (`s8812.eiw_3_positive`) and line 3 less line 6 otherwise (`s8812.eiw_7_figured`); new hand-predicted case `stage14.s8812.eiw_stop_with_se_tax`.
- **Tags:** stop-instruction-as-floor; latent-until-new-input; caught-by-transcription-agreement

---

## BUG-0056 — The Pub. 560 citations named no page, so the reviews saw none of Pub. 560

- **Date:** 2026-10-19
- **Caught by:** ruling the Stage 14 transcription log for `person` (the second transcription refused SIMPLE plans because "No SIMPLE IRA deduction text is provided"; the log's source table showed Pub. 560 with no pages).
- **Symptom:** the second transcription of the SEP and SIMPLE lines of `person` (Schedule 1 line 16) was made without the Pub. 560 text the lines cite, so its agreements and disagreements on those lines were not evidence about the text. The excess business loss threshold behind the Schedule 1 line 3 refusal (Rev. Proc. 2024-40) was likewise cited without a page in `s1`.
- **Root cause:** the 45 Pub. 560 locators in `forms/2025/person.yaml` named chapters and headings ("chapter 3, Catch-up contributions") and no page, and the excerpt selection takes pages from page numbers or from a heading that starts a line; Pub. 560's two-column layout puts no heading at a line start. `s1.ebl_threshold` cited "section 3.32" alone.
- **Where:** `forms/2025/person.yaml` (every `doc: p560` citation), `forms/2025/s1.yaml` (`s1.ebl_threshold`).
- **Fix:** each locator now begins with its pages, read in the archived text (chapter 2 pp. 8–11, chapter 3 pp. 14–17, chapter 5 pp. 38–40); the threshold cites p. 17. `person` and `s1` were transcribed again with those pages; seven refusal expectations that carry the citation were updated.
- **Tags:** citation-without-locator; review-input-gap; caught-by-review

---

## BUG-0057 — Line 27c was not checked at the Worksheet B line 5 STOP

- **Date:** 2026-10-20
- **Caught by:** the Stage 14 render comparison of `f1040` (line 27c: "It misses the Worksheet B triggers"), checked against i1040gi p. 47.
- **Symptom:** a self-employed filer who passes Steps 1 to 4 but whose Worksheet B line 4b is not less than the earned income limit got no EIC (correct) but no line 27c check, though Worksheet B line 5 says "No. STOP You can't take the credit. Check the box on Form 1040 or 1040-SR, line 27c".
- **Root cause:** `eic.check_27c` was written in Stage 9 from the Worksheet A path, where the matching test (Step 5, question 3, p. 42) has no line 27c instruction. Stage 14 routed self-employed filers through Worksheet B but did not add its line 5 STOP. The line 4b STOP was already covered, since Worksheet B line 6 is then zero and Worksheet A line 2 is zero.
- **Where:** `forms/2025/eic.yaml` (`eic.check_27c`).
- **Fix:** `eic.wsb_line5_stop` (Steps 1 to 4 passed, self-employed, line 4b above zero, earned income not below the limit) is a further term of `eic.check_27c`; hand-predicted cases `stage14.eic.wsb_line5_stop_27c` and `stage14.eic.wsb_stop_27c`.
- **Tags:** stop-instruction-missed; new-path-old-predicate; caught-by-render-comparison

---

## BUG-0058 — Car loan interest on Schedule C could be subtracted twice

- **Date:** 2026-10-20
- **Caught by:** the Stage 14 render comparison of `carloan` (column (iii): "the interest input asks for interest with 'none of it deducted elsewhere on your return,' not the total, so Schedule C interest could be subtracted twice").
- **Symptom:** a filer who answered the interest question as worded (excluding the part deducted on Schedule C) and then entered that part in column (ii) had it subtracted again; Schedule 1-A line 23 and the deduction were too low.
- **Root cause:** before Stage 14 column (ii) was always zero, so the question excluded interest deducted elsewhere instead. Stage 14 added the column (ii) question for a return with a Schedule C but left the interest question's wording, so the two together removed the business part twice. Column (iii) is "the total amount of the QPVLI paid or accrued on the loan during the taxable year minus the amount on line 22, column (ii)" (i1040gi p. 110).
- **Where:** `forms/2025/carloan.yaml` (`carloan.interest`) and the three interview profiles.
- **Fix:** the question asks for the total interest, "including any part you deduct on Schedule C (that part is entered separately)". Schedules E and F remain refused.
- **Tags:** question-wording; new-input-overlaps-old; caught-by-render-comparison

---

## BUG-0059 — Worksheet line 19 was unknown for a vehicle past its recovery period

- **Date:** 2026-10-20
- **Caught by:** the Stage 14 render comparison of `scveh` (line 19: "For a vehicle placed in service in 2019, 2025 is year 7 ... there is no table rate").
- **Symptom:** for a 2019 vehicle, the automobile worksheet's line 19 showed as unknown ("no row of macrs_gds for y5, mq3, 7") on the values sheet; the vehicle's depreciation (`scveh.macrs`, from the unrecovered basis) was right.
- **Root cause:** line 19 multiplied line 18 by the table rate for the 2025 recovery year for every vehicle placed before 2025; the tables have no seventh-year row for 5-year property, and the worksheet is not used after the recovery period (Pub. 946 p. 61, Deductions After the Recovery Period).
- **Where:** `forms/2025/scveh.yaml` (`scveh.line19`).
- **Fix:** `scveh.line19_earlier` is zero for a 2019 vehicle and line 18 times the rate otherwise; `stage14.veh.2019_cheap_mq3` expects line 19 zero.
- **Tags:** not-applicable-line-unknown; table-domain; caught-by-render-comparison

---

## BUG-0060 — The simplified home office deduction could exceed Schedule C line 29 with a section 179 carryover

- **Date:** 2026-10-20
- **Caught by:** the Stage 14 render comparison of `sc` (line 5 of the Simplified Method Worksheet: "a carryover (line 10) can make the deduction larger than the elections, and line 5 could then exceed line 1"), confirmed on a constructed return.
- **Symptom:** with wages, a 2025 section 179 election smaller than the property's cost and a carryover from 2024, Form 4562 line 12 (lines 9 and 10, up to line 11, which includes wages, i4562 p. 5) exceeded the business's own elections; Schedule C line 29 fell to $28.40 while line 30 stayed $1,500, giving a $1,471.60 loss made of the home office deduction, which the worksheet's line 5 ("Enter the smaller of line 1 or line 4") does not allow.
- **Root cause:** the test that the gross income limitation cannot bind (`sc.ho_unlimited`) and the no-section-179 branch (`sc.ho_no179`) used the business's 2025 elections as the most section 179 deduction it could take, leaving out the carryover on Form 4562 line 10.
- **Where:** `forms/2025/sc.yaml` (`sc.ho_room`, `sc.ho_no179`).
- **Fix:** `sc.ho_s179_max` (the elections plus Form 4562 line 10) replaces the elections in both, so a return whose line 4 could exceed line 1 under the deduction it may take goes to the existing refusal for the two interacting limits (Pub. 946 p. 19); case `stage14.ho.refuse_carryover_two_limits`.
- **Tags:** bound-omits-term; interacting-limits; caught-by-render-comparison

---

## BUG-0061 — Class M could not choose a case for the Stage 14 documents

- **Date:** 2026-10-20
- **Caught by:** running `classm-jobs` for `se`, `scveh` and `f4562` (0 cases, every branch "not reachable by a computed case").
- **Symptom:** no class M hand-work was possible for Schedule C, its vehicles, other property, Form 4562 or Schedule SE; the job builder reported nothing wrong beyond zero cases.
- **Root cause:** four gaps, each silent: the return generator (`engine/src/generate.ts`) gave every person an empty Schedule C list, so the corpus had no business; the job builder's `computed()` did not count a Rate value, so an entry with any table rate was never a candidate; every line of every entry is evaluated, and a helper whose printed table has no row for the entry's facts (the 2019-only automobile limits for a later vehicle) is unknown, which also excluded the entry; and a definition was assumed to take exactly an amount and a filing status, so Schedule SE (bound to lines 2 and 8a) had no instances.
- **Where:** `engine/src/generate.ts`, `engine/src/classm.ts`, `tools/transcription/classm.py`.
- **Fix:** the generator draws businesses (receipts, expenses, inventory, home office, health insurance with long-term care, vehicles, other property, SEP or SIMPLE plans) for the taxpayer and, on a joint return, sometimes the spouse, every entry field given a value; `computed()` accepts rates; an unknown helper with a missing table row is left out of the hand-work (a printed line that needed it would be unknown and the case not chosen); a definition's parameters are its input lines; a document with no branch of its own is worked once; `classm.py` reads and compares Rate and Enum lines, with the extra instruction only in prompts that have them. The property tests now cover business returns (all six hold).
- **Tags:** tool-defect; evidence-blind-spot; caught-by-review

---

## BUG-0062 — Section 179 on a separate return used the full dollar limitation

- **Date:** 2026-10-20
- **Caught by:** the Stage 14 transcription agreement for `s179` (the second transcription halved line 5 for married filing separately and added the spouse's property to line 2).
- **Symptom:** a married filer filing separately with a section 179 election got the full $2,500,000 limitation and counted only their own property, where the spouses must allocate the limitation (i4562 p. 5, Line 5, "multiply the total limitation ... by 50% (0.50), unless you both elect a different allocation") and line 2 includes "Any property placed in service by your spouse, even if you are filing a separate return" (p. 4).
- **Root cause:** Part I was encoded for one return's property, with the joint return combining both spouses (owner ruling on the mid-quarter test); the separate-return rules of lines 2 and 5 were not read.
- **Where:** `forms/2025/s179.yaml` (`s179.line5`).
- **Fix (owner):** a section 179 election or carryover on a separate return is refused (`s179.mfs`, on line 5); cases `stage14.s179.refuse_mfs` and `stage14.s179.mfs_no_election`.
- **Tags:** filing-status-rule-missed; caught-by-transcription-agreement

---

## BUG-0063 — The long-term care limit was applied per business, not per person across Forms 7206

- **Date:** 2026-10-20
- **Caught by:** the Stage 14 render comparison of `sc` (Form 7206 line 2: "that limit applies across all Forms 7206"), checked against i7206.
- **Symptom:** a person covered by qualified long-term care insurance under more than one business on the return could have up to the age limit entered on each business's Form 7206, where i7206 (pp. 1–2) says "the total of the amounts entered for each person on line 2 of all Form(s) 7206 can't be more than the appropriate limit shown on line 2 for that person".
- **Root cause:** `ltc` entries are kept per business and capped at the age limit within the entry; nothing related a person's entries under different businesses.
- **Where:** `forms/2025/sc.yaml` (`sc.hi_screen`) and the full interview.
- **Fix (owner):** the health insurance screen also asks whether anyone is covered by qualified long-term care insurance entered for more than one business on the return (yours or your spouse's), and refuses when yes.
- **Tags:** cross-entry-limit; caught-by-render-comparison

---

## BUG-0064 — The material participation question left out the oil and gas exception

- **Date:** 2026-10-20
- **Caught by:** the Stage 14 render comparison of `sc` (line G).
- **Symptom:** a filer reporting a working interest in an oil or gas well, who checks "Yes" on line G under the exception, would have answered the tool's question No and been refused as a passive activity.
- **Root cause:** the question restated the material participation tests and not the exception the line G instruction names: "If your business activity is not a rental activity and you meet any of the material participation tests, explained next, or the exception for oil and gas applies, check the 'Yes' box" (i1040sc p. 4; the exception, p. 5).
- **Where:** `forms/2025/sc.yaml` (`sc.passive`) and the full interview.
- **Fix:** the question includes the exception for a working interest held directly or through an entity that does not limit liability. Depletion, which such a business would usually claim, remains refused through `sc.special`.
- **Tags:** question-wording; exception-missed; caught-by-render-comparison

---

## BUG-0065 — Sixty i4562 citations named the wrong page

- **Date:** 2026-10-20
- **Caught by:** checking the line 11 citation of `s179` while ruling its render log ("p. 4, Line 11", where the archived page 4 has no line 11 instruction), then a check of every i4562 page citation in the Stage 14 forms against the archived text.
- **Symptom:** the excerpts given to the transcription and render reviews of `sc`, `scveh`, `asset` and `f4562` left out pages the lines rest on (i4562 p. 10, column (a) of lines 19a to 19j; p. 15, columns (f) to (h) of line 26; p. 16, column (i)), so those reviews judged some lines without their text; a filer following a citation would turn to the wrong page.
- **Root cause:** the citations were written one page early for the instructions that begin a page later than the topic before them: lines 6, 7 and 10 to 12 (p. 5), lines 26 and 27 (p. 14), columns (f), (g) and (h) of line 26 (p. 15), column (i) (p. 16), column (g) of line 19 (p. 12), and column (a) of lines 19a to 19j (pp. 9–10). The archive's page numbers are the printed ones, so no offset explains it.
- **Where:** 60 locators in `forms/2025/sc.yaml`, `scveh.yaml`, `asset.yaml`, `s179.yaml` and `f4562.yaml`; 11 refusal expectations in `fixtures/2025/stage14.json` that carry the citation. The same check over the other documents' citations in the Stage 14 forms found four more in `sc.yaml`, i1040sc lines 23, 25, 26 and 27a one page early (those reviews had the whole of i1040sc).
- **Fix:** each corrected to the page where its heading is printed; the four reviews whose excerpts changed were run again.
- **Tags:** citation-page-wrong; review-input-gap; caught-by-review

## BUG-0066 — i4562 and i1040sc citations named the wrong page for headings BUG-0065's check missed

- **Date:** 2026-10-20
- **Caught by:** researching `amb.2025.s179_carryover_no_property` for the owner: reading Worksheet 1 page by page in the PDF (`pdftotext -f N -l N`) put it on p. 4, where the register and `s179` cited p. 3. A check of every i4562 and i1040sc page reference in the forms, parameters, register and interviews against the PDF page that prints its heading then found the rest.
- **Symptom:** a reader following the citation turns to a page without the text. The reviews were not affected: the `s179`, `asset`, `scveh` and `f4562` reviews were given the cited pages and their neighbours (for `s179`, pp. 3 to 5), and the `sc` reviews the whole of i1040sc.
- **Root cause:** BUG-0065's check matched only "Line N" headings in the forms, so headings of other shapes kept the one-page-early error, and the interview files kept their own copies of locators BUG-0065 corrected in the forms.
- **Where:**
  - i4562 (12 locators): Worksheet 1 (p. 4, cited p. 3) in `forms/2025/s179.yaml` (3) and `params/2025.yaml` (2); the register's Worksheet 1 and Line 5 (pp. 4 and 5, cited pp. 3 and 4); How to figure the allowance (p. 7, cited p. 6) in `asset.yaml` (2) and `scveh.yaml` (1); Who Must File (p. 2, cited p. 1) in `asset.yaml` and `f4562.yaml`; Listed Property and its Exceptions (p. 3, cited p. 2) in `asset.yaml`.
  - i1040sc, in `sc.yaml`, `scveh.yaml`, `params/2025.yaml` and the three interview files:
    - the Simplified Method Worksheet lines (p. 12, cited p. 11) and its instructions (p. 11, cited p. 10);
    - Reporting your expenses for business use of the home (p. 14, cited p. 13);
    - line 24b's Amount of deduction (p. 10, cited p. 9);
    - in `sc.special`: Medicaid waiver payments and Installment sales (p. 6, cited p. 5), Lines 16a and 16b (p. 8, cited p. 7), Line 23 (p. 9, cited p. 8), Lines 26 and 27a (p. 10, cited p. 9);
    - Information on your vehicle (p. 7, cited p. 6);
    - in the interviews only, Lines 23, 25 and 26 (pp. 9 and 10, cited a page early; the forms were corrected under BUG-0065).
- **Fix:** each corrected to the page where its heading is printed, checked page by page against the PDFs. A check in `check-all` is TASKS.md T-044.
- **Tags:** citation-page-wrong; check-too-narrow; caught-by-research

## BUG-0067 — The gross receipts question asked for every Form 1099-MISC amount

- **Date:** 2026-10-20
- **Caught by:** the render review of `sc`, rerun for T-042: "Line 6 separately takes 'Prizes and awards related to your trade or business' and similar items that can appear on Form 1099-MISC, so 'all amounts reported ... on Forms 1099-MISC' can put line 6 income on line 1."
- **Symptom:** the line 1 question asked for gross receipts "including all amounts reported to you on Forms 1099-NEC, 1099-MISC and 1099-K", while the line 6 question asks for prizes, awards and other business income. A filer could enter a Form 1099-MISC prize on both lines, overstating gross income.
- **Root cause:** the question paraphrased "Be sure to check any Forms 1099 you received for business income that must be reported on this line" (i1040sc p. 5, Line 1) as "all amounts" on those forms.
- **Where:** the `sc.line1` source in `forms/2025/sc.yaml` and the same prompt in the three interview files.
- **Fix:** the question now asks for gross receipts "including amounts properly shown on Forms 1099-NEC and any other gross receipts of this business reported to you on a Form 1099 (such as Form 1099-K); not the other business income asked about separately, such as prizes and awards". The rerun render review matches the new wording.
- **Tags:** render-wording; double-count-risk; caught-by-review

## BUG-0068 — Class M jobs did not give a collection entry the fields of its enclosing entry

- **Date:** 2026-10-20
- **Caught by:** the class M rerun of `sc` for T-042: on returns with Form W-2 wages the model's Form 7206 line 7 and QBI self-employment tax share differed from the project ("Assumes no W-2 wages (Schedule 1 line 15 not given)"). Worked by hand, the project was right: for `classm.sc.3`, $176,100 of W-2 social security wages leave only the 2.9% part, $53,769.20 x 92.35% x 2.9% = $1,440.02, one-half $720.01.
- **Symptom:** the model refigured the person's Schedule SE line 13 without the W-2 wages it never saw, so every line built on it disagreed; on returns without W-2 wages the refigured amount happened to agree, which hid the gap in earlier runs.
- **Root cause:** `buildJob` in `engine/src/classm.ts` skips references into collection documents ("collection fields are given per entry below"), but only the collections a document sums over were given below; a reference to the enclosing entry (`person.se_line13`, `person.s16`, `person.positive_profits` read by `sc`) was given nowhere.
- **Where:** `engine/src/classm.ts`, `buildCollectionJob`.
- **Fix:** each entry is now given the fields of its enclosing entries that the document reads, labelled as given. The `sc` jobs were rebuilt and its class M rerun. `asset`, `scveh` and `ltc` ran under the gap and their logs agree or are ruled; their next class M run will see the givens.
- **Tags:** review-input-gap; classm-tooling; caught-by-review

## BUG-0069 — The 300 square feet of the simplified method applied to each business, not to all of them

- **Date:** 2026-10-20
- **Caught by:** the render review of `sc`, rerun for T-042: "The 300 square foot cap is applied to each Schedule C separately. The text says 'You are limited to a maximum of 300 square feet for all of the businesses you conduct in your home', and no screen or refusal covers more than one business in the same home."
- **Symptom:** a person with two businesses using the home could claim up to 300 square feet for each, overstating the home office deduction.
- **Root cause:** the simplified method worksheet was encoded per Schedule C, as the worksheet is printed, without the paragraph that makes the 300 square feet a limit across a person's businesses (i1040sc p. 10, Simplified method).
- **Where:** `forms/2025/sc.yaml` (`sc.ho_sqft`), `forms/2025/person.yaml`.
- **Fix (owner):** a person with more than one Schedule C claiming the business use of the home is refused (`person.ho_count`, `sc.ho_multi` on `sc.ho_sqft`); fixtures `stage14.ho.refuse_two_businesses` and `stage14.ho.second_business_no_ho`.
- **Tags:** cross-entry-limit; overstatement; caught-by-review

## BUG-0070 — The employee benefit question excluded the filer's own deductible dependent care contributions

- **Date:** 2026-10-20
- **Caught by:** the render review of `sc`, rerun for T-042: "The instructions allow your own dependent care contributions: 'If you made contributions on your behalf as a self-employed person to a dependent care assistance program, complete Form 2441, Parts I and III, to figure your deductible contributions.'"
- **Symptom:** the line 14 question said "not for yourself", so a self-employed filer's own contributions to a dependent care assistance program, deductible on line 14 after Form 2441, were left out with no refusal (an understatement).
- **Root cause:** "not for yourself" was written from the line 14 rules for accident and health plans and group-term life insurance, which do exclude the filer's own contributions, and applied to dependent care, which does not.
- **Where:** `forms/2025/sc.yaml` (`sc.line14`, `sc.special`) and the three interview files.
- **Fix (owner):** Form 2441 is not built, so the Schedule C screen `sc.special` now names these contributions and refuses the return.
- **Tags:** render-wording; understatement; caught-by-review

## BUG-0071 — The renderer printed an Enum parameter's value as money

- **Date:** 2026-10-20
- **Caught by:** the render review of `asset`, rerun for T-030: "the half-year convention helper (asset.hy) is garbled ('Enter 0 $NaN.NaN; 1 $NaN.NaN')".
- **Symptom:** a line that enters an Enum parameter (the MACRS convention `sc.conv_hy`, the recovery period `sc.period_y5`) rendered as "Enter 0 $NaN.NaN; 1 $NaN.NaN", in `rendered/2025/asset.md`, `scveh.md` and `params.md`; the Stage 14 render reviews of `asset` and `scveh` saw that text. Values were unaffected.
- **Root cause:** `paramValueText` in `engine/src/render.ts` handled numbers, booleans and rates, and treated anything else as a per-filing-status table; a string value was taken apart character by character and each character formatted as money.
- **Where:** `engine/src/render.ts`.
- **Fix:** a string value (an Enum parameter) renders as itself ("Enter hy (sc.conv_hy)"); the `asset` and `scveh` render reviews were rerun on the corrected text.
- **Tags:** renderer-bug; review-input-gap; caught-by-review

## BUG-0072 — A vehicle converted from personal use during 2025 got an unprorated business-use percentage

- **Date:** 2026-10-20
- **Caught by:** the render review of `scveh`, rerun for BUG-0071: "It omits the conversion rule: 'If during the tax year you convert property used solely for personal purposes to business/investment use ... Multiply that percentage by the number of months you use the property in your business ... and divide the result by 12.'"
- **Symptom:** the cost question admits a vehicle converted from personal use (giving the basis rule for it), but in the year of conversion the business-use percentage was business miles over the year's total miles, without the months-over-12 proration i4562 requires (p. 14); nothing refused the case, so its depreciation could be over- or understated.
- **Root cause:** the basis rule for converted property was added to the cost question in Stage 14 without the conversion-year percentage rule that goes with it.
- **Where:** `forms/2025/scveh.yaml` (`scveh.screen`) and the three interview files.
- **Fix (owner):** the vehicle screen now names a conversion from personal use during 2025, which is refused; a conversion in an earlier year needs no proration in 2025.
- **Tags:** scope-gap; no-refusal; caught-by-review

## BUG-0073 — Citations named pages, headings and quotes the cited page does not print

- **Date:** 2026-10-20
- **Caught by:** `tools/citations.py`, the citation-page check added to check-all for T-045 part 2 (and T-044 part 1): every quote in a page locator must be printed on the cited pages and the locator's first phrase (its heading) on them or up to two pages before, against both archived text layers.
- **Symptom:** before the corrections the check found 98 distinct problems (344 locators counting the interview files' copies): quotes printed on another page, quotes not printed verbatim anywhere, and headings not printed on the cited page. A reader following such a citation turns to a page without the text, and the transcription and render reviews, which are given the pages a locator names, may have been given the wrong page.
- **Root cause:** citations were written and checked by hand. BUG-0065 and BUG-0066 corrected the pages of "Line N" and other headings in the i4562 and i1040sc citations with one-off scripts that checked headings only. Quotes were never compared with the archived text, so a quote could carry the heading's page when it was printed on the next one, be paraphrased ("doesnt", an added "or", a dropped word), or come from another document (the Form 7206 line 2 text cited to i7206).
- **Where:** 28 files: `forms/2025/` (asset, carloan, dependent, eic, f1040, f4562, f8889, f8960, f8995a, household, ltc, otjob, person, qbi, retirement, s1, s1a, s8812, sa, sc, scveh, sd, ssb, tipjob), `params/2025.yaml`, `tables/2025/auto_limit_first_nobonus.yaml`, and the three interview files. Among them:
  - quotes cited a page early: i4562 Line 14 (the special allowance, pp. 5–6), Line 10 (p. 5), Line 13 of i8889 (p. 8), Column (i) (p. 16), Limits for passenger automobiles (pp. 14–15), Lines 26 and 27 (pp. 13–14), the line 17 caution (p. 9); Pub. 946's Deductions After the Recovery Period example (pp. 61–63); i1040gi Schedule 1-A method 2 (pp. 106–107);
  - quotes not printed as written: p501's "doesn't", the i1040gi QPVLI, qualified tips, head of household and lines 4a–5b quotes, the i8889 worksheet quote, the dependent "time lived with you" exception (quoted from p. 15's wording while citing p. 21), and the EIC flow-chart quotes that ran a question into its answer box;
  - headings not printed: "Who Can Use Form 8995(-A)" (printed "Who Can Take the Deduction"), "methods 1 to 3" (printed as paragraphs 1 through 4), and descriptions in place of a heading (now the printed heading followed by the description).
- **Fix:** each locator corrected to the printed page, heading and wording; quotes that join separated text mark the gap with "...". Eleven anchors and quotes that are correct but cannot be matched as printed text (a section number such as "Section III.B.2", a quote the extraction reads out of order) are ruled in `reviews/2025/citations.json`.
- **Tags:** citation-page-wrong; quote-not-verbatim; review-input-gap; caught-by-check

## BUG-0074 — The interviews asked stale copies of form-line questions and citations

- **Date:** 2026-10-21
- **Caught by:** T-045 part 3, comparing each interview question with the form line it asks for before deriving prompts and citations from the lines.
- **Symptom:** the whole-return interview (`full`) still asked `scope.schedule1` and `s2.other` in their pre-Stage 14 wording, which listed being self-employed or filing Schedule C or SE, and self-employment tax, among the things outside this tool; a self-employed filer answering as asked would have been refused, though Stage 14 prepares Schedule C and SE. Its citations repeated pages since corrected in the forms (BUG-0065, BUG-0066, BUG-0073; for example `scveh.prior_conv` still cited i4562 p. 14, `asset.listed` p. 2) and the Pub. 946 web edition the forms had left. The stage profiles (`sales`, `stage4`, `2025`) asked 111 of the same inputs differently again (help, prompt, order or citation).
- **Root cause:** each interview file carried its own copy of each question's prompt and citation; a change to a form line, or to one profile, reached the others only by hand. The fixtures supply answers directly, so a stale prompt changes no computed value and no fixture noticed.
- **Where:** `interview/2025.yaml`, `sales-2025.yaml`, `stage4-2025.yaml`, `full-2025.yaml`: in `full`, 15 prompts and 65 citations.
- **Fix:** one question bank, `interview/questions-2025.yaml`, from which every profile takes its questions; a prompt is the collection's frame followed by the form line's question text and a citation the line's (a roster question's, its collection's), filled at build, and the build fails if the bank repeats either. Four Stage 4 refusal fixtures answer the three Schedule 1-A questions now asked before their refusal.
- **Tags:** copy-drift; stale-wording; wrong-refusal; caught-by-review

## BUG-0075 — The data schema pinned the interview's tax year to 2025

- **Date:** 2026-10-21
- **Caught by:** the T-045 part 5 test, which adopted the 2025 definitions into a made-up 2026 (in a copy of the tree) and built it: "interview: schema validation failed: data/tax_year must be equal to constant".
- **Symptom:** no year other than 2025 could build, though T-045 part 1 had made the year a setting everywhere else.
- **Root cause:** `schema/data.schema.json` gave the interview's `tax_year` as `"const": 2025`; part 1's search for the year covered the engine, the tools and the Lean evaluator, not the schema, and a build of another year had never been run.
- **Where:** `schema/data.schema.json`.
- **Fix:** the schema requires an integer; the build already requires every document under a year's directories to state that year.
- **Tags:** year-pinned; missed-by-search; caught-by-test

## BUG-0076 — Defects found by rerunning the reviews of changed forms

- **Date:** 2026-10-21
- **Caught by:** T-044 part 2: the transcription, render and class M reviews of the 30 forms whose reviewed content had changed since their reviews (subject hashes) were run again; the disagreements were drafted for ruling by agents, and each defect below was confirmed by evaluating returns.
- **Symptom:**
  - A self-employed person with railroad retirement (tier 1) compensation got Schedule SE without it on line 8a: for $170,000 of railroad pay and a $30,000 Schedule C profit, SE tax $4,238.87 where the form gives $1,559.85, with no refusal.
  - The W-2 roster question said only "List stable keys for Form W-2 — Social Security boxes by employer": a filer listing each Form W-2 of one employer got the excess social security credit (Schedule 3 line 11, $1,481.80 in the example) that i1040gi p. 117 allows only with more than one employer.
  - The student loan interest question asked only whether the filer is claimed as a dependent; i1040gi p. 98 also bars it when the spouse on a joint return is.
  - A vehicle on actual expenses with no miles divided by its total miles: line 9, line 31 and every total after it were unknown, with no question that could settle them and no refusal.
  - Six Form 8995 lines (6, 7, 8, 11, 12, 17) carried placeholder labels ("Amount from qbi.zero") instead of their printed text.
- **Root cause:** Schedule SE's line 8a was bound to the W-2 social security wages and the railroad screen covered only Schedule 3 and Form 8959; the roster's consolidation rule lived only in a note of `w2.yaml`; `sli.claimed` was written from the filer's side only; the business-use proration had no guard for a zero denominator; the Form 8995 labels were never filled in. The earlier reviews had either predated the change or ruled the first two as representation.
- **Where:** `forms/2025/person.yaml`, `sc.yaml`, `se.yaml`, `sli.yaml`, `scveh.yaml`, `f8995.yaml`; `interview/questions-2025.yaml`.
- **Fix:** (owner) railroad compensation with a Schedule C is refused at Schedule SE (`person.se_rrta`, counted through the person's businesses so the question reaches only a person with one); (owner) a vehicle on actual expenses with no miles is refused (`scveh.no_miles`); the W-2 question asks for one key per employer, combining an employer's Forms W-2; the student loan question asks about the spouse on a joint return; the Form 8995 labels are the printed text.
- **Tags:** scope-gap; wording; divide-by-zero; no-refusal; caught-by-review

## BUG-0077 — The class M tool lost answers, built no person cases, and was fed unrealistic returns

- **Date:** 2026-10-21
- **Caught by:** T-044 part 2's class M reruns: the draft rulings for `eic` noted that two lines printed "6" shared one answer; `person` had no cases.
- **Symptom:**
  - `classm.py` keyed the model's answers by printed number, so of EIC Worksheet B line 6 and Worksheet A line 6 one answer stood for both and some comparisons tested the wrong value.
  - `classm-jobs` built no `person` case: a collection document whose lines take a shared definition's result (the person's Schedule SE lines) looked those results up by the bare line id, found nothing, and dropped every case; it also chose among cases it could not build.
  - The generator gave every person SEP and SIMPLE amounts whatever their plan, so a person without a SIMPLE plan tripped the SIMPLE limits on lines nothing reads, and class M (which excludes a person entry with any refusal) found no usable return.
- **Root cause:** the tools were written before a document had two lines with one printed number, before a collection called a shared definition (Stage 14), and before plans were generated (Stage 14).
- **Where:** `tools/transcription/classm.py`, `rule.py`; `engine/src/classm.ts`, `generate.ts`.
- **Fix:** a line to fill is named by a handle, its printed number with its id where two lines share the number, in the prompt, the answers, the log and the rulings; a collection's shared-definition results are given per entry; candidate cases are those a job can be built from; the generator gives a plan's amounts only to a person with that plan. `eic` and `person` were reviewed again.
- **Tags:** tool-bug; review-input-gap; generator; caught-by-review

## BUG-0078 — A SEP or SIMPLE limit was figured on the profit of every business

- **Date:** 2026-10-21
- **Caught by:** the render review of `person`, rerun for T-044 after BUG-0076's fixes; the draft ruling evaluated the case.
- **Symptom:** a self-employed person with a SEP or SIMPLE plan and more than one Schedule C had the plan's limit figured on all businesses' profit: a $100,000 business with a 25% SEP allows $18,587.04, but with a second, $30,000 business the limit became $24,163.16 and a $20,000 contribution was deducted in full on Schedule 1 line 16.
- **Root cause:** the Deduction Worksheet for Self-Employed step 1 (`person.sep_s1`) and the SIMPLE compensation read the person's total Schedule C profit, and the register entry `amb.2025.f7206_plan_attribution` rested on that premise. Pub. 560 p. 7: "If you have more than one business, but only one has a retirement plan, only the earned income from that business is considered for that plan" (also pp. 11 and 40).
- **Where:** `forms/2025/person.yaml` (`person.plan_screened`); `ambiguities/2025.yaml` (`amb.2025.f7206_plan_attribution`, `amb.2025.qbi_attribution` reasons).
- **Fix (owner):** a SEP or SIMPLE plan with more than one Schedule C is refused through the plan screen's gate; the two register reasons are corrected, their readings unchanged.
- **Tags:** wrong-premise; overstatement; caught-by-review

## BUG-0079 — A refusal can wait behind an unknown operand in the binary atoms

- **Date:** 2026-10-22
- **Caught by:** the Stage 15 Form 2441 authoring: the `refusal_propagates` property failed on `f2441.line9a` for generated returns that lacked some Form 2441 inputs, until the generator supplied them.
- **Symptom:** `sum` returns a refusal among its operands before an unknown one, but `multiply_rate` (and, per the authoring agent, `subtract` and `multiply_count`) return the first operand's unknown before looking at the second operand, so a refusal carried by the second operand is not reported while the first is unanswered. The refusal appears once the first operand is known, so no return is produced wrongly; it can arrive later in the interview than the early-refusal rule intends.
- **Root cause:** each atom's evaluator checks its operands in order and returns the first incomplete one, with no common rule that a refusal outranks an unknown; the Lean evaluator agrees case for case (compare finds no difference).
- **Where:** `engine/src/eval.ts` (`multiply_rate` checked; the other binary atoms per the agent's report, not yet checked one by one); `lean/TaxFormalization/Eval.lean`.
- **Fix:** open, for the owner. Proposed: one rule for every atom, a refusal among the operands outranks an unknown (as `sum` does), in both evaluators, with a property test.
- **Tags:** evaluator; refusal-order; caught-by-property

## BUG-0080 — Form 2441's column (c) box was checked for a qualifying person under 13

- **Date:** 2026-10-22
- **Caught by:** the Stage 15 transcription and render reviews of `dependent` (both, independently) and its class M review.
- **Symptom:**
  - Line 2 column (c), "Check here if the qualifying person was over age 12 and was disabled", was checked for every qualifying person unable to care for themselves except a qualifying child under 13 all year, so a disabled qualifying relative under 13 (for example an unrelated household member aged 10) had it checked.
  - The label of `dependent.dc_child` said "under 13 for at least part of 2025", while the line holds only the child who turned 13 during 2025 (the all-year route is `dependent.dc_child_all_year`); the class M model, reading the label, answered yes for children aged 11 and 3.
  - Neither changes an amount: the box is a display line, and `dependent.dc_qp` takes both routes.
- **Root cause:** the box's test stood in "not a qualifying child all year" for "over age 12" (i2441 p. 3, Column (c), "was over age 12 at the time the care was provided and was disabled"); the helper's label described the qualifying-child test as a whole instead of its own route.
- **Where:** `forms/2025/dependent.yaml` (`dependent.dc_line2c`, `dependent.dc_child`).
- **Fix:** the box tests `dependent.age` at or over `dc.child_age`; the label names the turned-13 route.
- **Tags:** display; wrong-premise; caught-by-review

## BUG-0081 — The Schedule 1 refusal text still listed only the Stage 11 adjustments

- **Date:** 2026-10-22
- **Caught by:** the Stage 15 render review of `scope` (rerun because the credits screen changed).
- **Symptom:** the refusal shown when the Schedule 1 screen is answered Yes, under `scope.ready` and on Form 1040
  lines 8 and 10, says "Schedule 1 income and adjustments other than unemployment compensation, educator expenses,
  the HSA deduction and student loan interest are outside this tool", while the screen's own question treats
  Schedule C income, the self-employment tax deduction, self-employed SEP and SIMPLE contributions and the
  self-employed health insurance deduction as supported (since Stage 14). No value changes.
- **Root cause:** Stage 14 narrowed the question and not the three refusal texts that repeat its list.
- **Where:** `forms/2025/scope.yaml` (the `scope.schedule1` refusal), `forms/2025/f1040.yaml` (lines 8 and 10).
- **Fix:** open (TASKS.md T-050): the three texts list the same supported items as the question, with the reviews
  of `scope` and `f1040` rerun after.
- **Tags:** wording; stale-text; caught-by-review

## BUG-0082 — Mutation testing could not see a change in a rate

- **Date:** 2026-10-22
- **Caught by:** the Stage 15 band-edge fixtures: four Form 8880 rate-table mutants survived although a fixture
  asserted exactly the line each one changed; evaluating one by hand showed the line moving from 0.0 to 0.1.
- **Symptom:** `engine/src/mutate.ts` compared values through a normal form that printed every rate as
  "rate:undefined" (a rate has a numerator and denominator, not a `value`), so a mutant whose only effect was on
  a rate line was never killed. This held for `keyed_lookup`'s rates (the MACRS tables) as well as for
  `rate_lookup`. The fixture runner compares by deep equality and was not affected; `compare.ts` had the same
  form and was corrected in 6051ec0.
- **Root cause:** the normal form was written before any line returned a rate.
- **Where:** `engine/src/mutate.ts` (`normal`).
- **Fix:** rates compare as numerator and denominator, exactly. Four survivors are now killed.
- **Tags:** test-tool; rate; caught-by-fixture

## BUG-0083 — A line's refusal gates stop at the first unknown gate (the rest of BUG-0079)

- **Date:** 2026-10-22
- **Caught by:** the fix of BUG-0079 (owner-approved), which made both evaluators take an atom's and a comparison's
  operands by one rule: the first refusal in operand order, else the first unknown, else compute (`smaller_of`,
  `larger_of`, `keyed_lookup` and `rate_lookup` now evaluate past an unknown operand; `sum`, `sum_over`, `all` and
  `any` keep the first unknown; `choose` guards and `all`/`any` keep their order and early stops, since a later
  refusal there is not certain). A new property, `refusal_outranks_unknown` (answers removed from generated
  returns), failed on `f8880.line10` before that fix and holds after it. BUG-0079's atoms are fixed by that change.
- **Symptom:** a line's own list of refusal gates (`refuses`) is still read in order and stops at the first unknown
  gate, so when gate 1 is unknown and gate 2 is true the line is reported unknown though it is certainly refused.
  No return is produced wrongly; the refusal can come later in the interview.
- **Root cause:** the gate list is not an atom and was left out of the operand rule.
- **Where:** `engine/src/eval.ts` and `lean/TaxFormalization/Eval.lean` (the gate loop).
- **Fix:** open, for the owner. Applying the rule there was tried and reverted: the interview then asks a few more
  questions before refusing (658 integration invocations become 661, `stage4.refuse.scope.schedule1` and
  `sales.refuse.digital.G` each asking one or two more).
- **Tags:** evaluator; refusal-order; caught-by-property

## BUG-0084 — The standard deduction counted the age box of a person who died before reaching 65

- **Date:** 2026-10-22
- **Caught by:** the Stage 16 transcription comparison of `sa` (sa.itemizes, sa.deduction): the second
  transcription excluded a person who died in 2025 before reaching 65 from the age boxes.
- **Symptom:** on a joint return whose spouse was born in 1960, died in 2025 before reaching 65 and had no SSN valid
  for employment, Form 1040 line 12e was $33,100 instead of $31,500 and line 15 $76,900 instead of $78,500,
  unrefused (i1040gi p. 33, Line 12d, Death of spouse in 2025, "don't check the box"; p501 p. 23, Death of taxpayer).
- **Root cause:** `sa.boxes_age65` counted `person.age65` alone; the decedent rule was carried only by the Schedule
  1-A Part V refusals (`s1a.senior_decedent`, `s1a.spouse_senior_decedent`), which a spouse without a work SSN does
  not reach. The Stage 13 rulings on `sa.itemizes` and `sa.deduction` did not address the condition.
- **Where:** `forms/2025/sa.yaml` (`sa.boxes_age65`).
- **Fix:** `sa.boxes_age65` counts a person only when `person.age65` is true and `person.died_before_65` is false;
  fixture `stage16.sa.decedent_spouse`; three fixtures with a person aged 65 or older gained the answer
  `died_before_65` false.
- **Tags:** refusal-reachability; stale-scope-ruling; caught-by-transcription-comparison

## BUG-0085 — The HSA medical expense question left out people who would be dependents

- **Date:** 2026-10-22
- **Caught by:** the Stage 16 render review of `f8889` (line 15).
- **Symptom:** the question for Form 8889 line 15 asked for qualified medical expenses "of you, your spouse and your
  dependents", while the line 15 instructions also include anyone who would be a dependent except for filing a joint
  return, having gross income, or the filer being someone else's dependent (i8889 p. 8), and a child of divorced or
  separated parents for both parents (p. 9, TIP). A filer answering as worded could leave such expenses off line 15,
  overstating line 16, Schedule 1 line 8f and the additional 20% tax on line 17b.
- **Root cause:** the question paraphrased the instruction's three-item list as "your dependents".
- **Where:** `forms/2025/f8889.yaml` (`f8889.medical`).
- **Fix:** the question names the would-be dependents and the divorced-parents rule; no expression changed.
- **Tags:** input-wording; question-scope; caught-by-render

## BUG-0086 — The IRA basis question omitted the Form 8606 line 2 adjustments

- **Date:** 2026-10-22
- **Caught by:** the Stage 16 render comparison of Form 8606: line 2 MISMATCH, quoting the Total Basis Chart's 2024
  row and the line 2 adjustments (i8606 p. 9).
- **Symptom:** `person.ira_basis` asked for zero in a first year and otherwise line 14 of the last Form 8606. A filer
  whose basis changed by a return of excess traditional IRA contributions, a transfer incident to divorce, a rollover
  of the nontaxable part of a qualified plan, or line 6 of an earlier Line 15c Worksheet was led to enter the wrong
  basis on Form 8606 lines 2, 3 and 14 (no 2025 tax effect, since a 2025 distribution or conversion is refused; the
  error carries to the next year). The interview help said "zero if you never filed Form 8606".
- **Root cause:** the question was written from the chart's general rule without the "increase or decrease the amount
  from the chart" list beside it or the 2024 row's adjustment.
- **Where:** `forms/2025/person.yaml` (`person.ira_basis`), `interview/questions-2025.yaml` (its help).
- **Fix:** a per-person screen `person.ira_basis_adjusted`, asked of a person who files Form 8606, refuses Form 8606
  line 2 (`person.ira_basis_gate` on `person.ira_8606_line2`); the basis question follows the Total Basis Chart and
  the help says "zero if this is the first year you file Form 8606". Existing fixtures gained the answer false.
- **Tags:** input-wording; screen-missing; caught-by-render

## BUG-0087 — An HSA whose owner died with the estate as beneficiary was not refused

- **Date:** 2026-10-22
- **Caught by:** the Stage 16 rulings on the `f8889` transcription log (an observation beside the line 17b ruling:
  the second transcription noted that the death exception is not covered by line 17a).
- **Symptom:** on a final return where the estate is the HSA's beneficiary, the HSA's value at death is included on
  line 14a and "is not subject to the additional 20% tax" (i8889 p. 3, Death of HSA Account Beneficiary). The line
  17a question names only disability and age 65, and `f8889.unsupported` named only an HSA acquired because of
  someone else's death, so such a return could be charged the 20% tax on an excepted amount. Final returns are in
  scope (`person.died_before_65`).
- **Root cause:** the death rule's two sides (the beneficiary's and the decedent's) were screened on one side only.
- **Where:** `forms/2025/f8889.yaml` (`f8889.unsupported`).
- **Fix:** the screen also names "the HSA of a person who died in 2025 whose estate is the beneficiary"; a Yes refuses
  as before.
- **Tags:** screen-missing; decedent; caught-by-review

## BUG-0088 — The Form 8889 screen was not asked when a person had no 2025 contributions or distributions

- **Date:** 2026-10-22
- **Caught by:** the T-054 regression case. The task asked for the roster question to name the qualified HSA
  funding distribution; driving the interview for a person whose only HSA item is one the tool does not support
  showed that, with the roster answered, the screen is still never asked.
- **Symptom:** `f8889.unsupported` refused only the figured branches of lines 13 and 16, which are reached only when
  line 2 or line 9 (contributions) or line 14a (distributions) is more than zero. A person whose only HSA item was a
  qualified HSA funding distribution from an IRA, a testing-period failure (Part III income and its 10% additional
  tax), an inherited HSA or an Archer MSA answered three amounts with zero and got a computed return without the
  item. The roster question also departed from i8889's Who Must File (p. 1): it named contributions by "you, or your
  employer" (not "or someone else") and left out the HSA acquired on the account beneficiary's death.
- **Root cause:** the screen's refusal entry sat on lines that only some paths reach, not on the printed lines every
  Form 8889 entry reads; the roster question paraphrased Who Must File.
- **Where:** `forms/2025/f8889.yaml` (`f8889.line13`, `f8889.line16` and their figured lines),
  `interview/questions-2025.yaml` (`$f8889`).
- **Fix:** the screen's entry moved from the figured lines to printed lines 13 and 16, so it is asked of every Form
  8889 entry straight after the roster; the roster question follows Who Must File and names the funding
  distribution. Regression `stage16.cleanup.refuse.f8889.screen_no_amounts`; four class M cases whose generated
  returns answered the screen Yes with zero amounts were rebuilt.
- **Tags:** screen-unreached; question-scope; caught-by-fixture

## BUG-0089 — The evidence report counted class M fixtures as R

- **Date:** 2026-10-22
- **Caught by:** human-directed audit (two Claude sessions reviewing the repository at the owner's request, 2026-10-22;
  `docs/2026-10-22_project_evaluation.md`).
- **Symptom:** `reports/2025/evidence.md` has columns for classes A, B, C and R only; the 169 class M cases of
  `fixtures/2025/classm.json` (model hand-work, spec 6.1) were counted in the R column, and the report's own header
  described an M class it never printed. A reader of the report saw the project's largest body of non-recorded
  evidence as synthetic regression.
- **Root cause:** `evidenceReport`'s class mapping has no M branch:
  `ev === "C" ? "C" : ev.startsWith("B") ? "B" : ev.startsWith("A") ? "A" : "R"`, so every label that is not A, B or
  C falls into R.
- **Where:** `engine/src/fixtures.ts` (`evidenceReport`).
- **Why it survived:** the report is generated and read by the same tool chain; no check compares the classes printed
  with the classes present in the fixture files; the header's prose was written for the class list the mapping never
  implemented.
- **Fix:** the evidence report gains an M column, an engine column and a scoreboard (integrity plan item 0.1).
  Integrity plan item 0.1 commit.
- **Tags:** tool-defect; evidence-blind-spot; report-misstates-class; caught-by-audit

## BUG-0090 — Evidence labels misstated two classes

- **Date:** 2026-10-22
- **Caught by:** human-directed audit (two Claude sessions reviewing the repository at the owner's request, 2026-10-22;
  `docs/2026-10-22_project_evaluation.md`).
- **Symptom:** (i) `fixtures/2025/stage1.json`: 57 cases labelled "C" with the note "Recorded from the TypeScript
  evaluator and confirmed by the independently written Lean reference evaluator"; spec 6.1 defines C as agreement with
  an independent engine, and the Lean evaluator reads the same data. (ii) `fixtures/2025/stage1.json` case
  `qdcg.handworked.single` labelled "B" (human hand-work) with the note "Worked by the agent"; spec 6.1 says model work
  is never B. The evidence report therefore overstated both classes.
- **Root cause:** the labels were assigned at Stage 1, before the evidence classes were applied strictly, and never
  revisited.
- **Where:** `fixtures/2025/stage1.json` (the 57 "C" cases; `qdcg.handworked.single`).
- **Why it survived:** the evidence report prints labels without reading their notes; no check compares a label with
  its note, and the notes said in plain words what the labels denied.
- **Fix:** the 58 cases relabelled R with notes saying what the recording is (integrity plan item 0.1); a rerun
  through `classm.py` under the plan will earn M properly. Integrity plan item 0.1 commit.
- **Tags:** evidence-label-wrong; recorded-expectation-laundering; caught-by-audit

## BUG-0091 — Citations that locate nothing passed the citation check

- **Date:** 2026-10-22
- **Caught by:** human-directed audit (two Claude sessions reviewing the repository at the owner's request, 2026-10-22;
  `docs/2026-10-22_project_evaluation.md`).
- **Symptom:** 164 citation segments in the form files (54 on computed lines' own citations) use whole-form span locators ("Schedule A (2025), lines 1–18", "Form 8959
  (2025), lines 1–24", "Form 8960 (2025), Parts I–III, individual lines 1–17", "Form 8995 (2025), lines 1–17", the
  Unrecaptured Section 1250 Gain Worksheet "lines 1–18", the 28% Rate Gain Worksheet "lines 1–7"), and 733 of 2,667
  single-line locator segments name no page. A reader following such a citation is pointed at a whole form, or at a
  line whose page nothing names. Spec 3 item 1 is satisfied in letter (a citation exists) and not in intent.
- **Root cause:** `tools/citations.py` examines only segments that begin "p." or "pp." (its `SEGMENT_RE`); a span
  locator or a form-line locator without a page is never examined, so the check cannot fail on it.
- **Where:** `tools/citations.py` (segment selection); the 187 span locators and 733 page-less segments in
  `forms/2025/`.
- **Why it survived:** the check's scope was written from the locators it could verify (page, anchor, quote) and was
  silent on the rest; BUG-0073's corrections ran inside that scope; the reviews are given the pages a locator names,
  so a locator naming none was never put in front of a reader.
- **Fix:** integrity plan item 0.2: span locators are forbidden on computed lines; form-line locators are verified
  against the form's text; title-only anchors are rejected; the check writes a worklist of locators to rewrite. The
  rewrites follow. Integrity plan item 0.2 commit.
- **Tags:** citation/span-locator; check-scope-gap; caught-by-audit

## BUG-0092 — Form 8889 tests marital status by filing status

- **Date:** 2026-10-22
- **Caught by:** human-directed audit (two Claude sessions reviewing the repository at the owner's request, 2026-10-22;
  `docs/2026-10-22_project_evaluation.md`).
- **Symptom:** `f8889.married_family` and `f8889.age55_unmarried` test `f1040.status = mfj`, so a married person filing
  head of household (considered unmarried for filing status, but married under i8889's "unmarried"/"married" wording
  for the line 3 chart and the age-55 amounts) gets the unmarried treatment on Form 8889 line 3.
- **Root cause:** the instruction's word is marital and the encoding has no marital input here; `eic.yaml` already
  carries one (`eic.married`) for its Step 3 rules. Of 38 lines whose label mentions married and whose expression
  tests `f1040.status`, these two are the only ones where the instruction's word is marital rather than a filing
  status.
- **Where:** `forms/2025/f8889.yaml` (`f8889.married_family`, `f8889.age55_unmarried`).
- **Why it survived:** the render review judges each line's English against the page, and "married filing jointly"
  reads as a faithful rendering of "married" unless the reader holds the head-of-household case in mind; no fixture
  has a married head-of-household filer with family HDHP coverage.
- **Fix:** open; integrity plan item 2.4 (read a marital answer; add a fixture).
- **Tags:** status-vs-marital; scope-screen-wider-than-line; latent-until-new-input; caught-by-audit

## BUG-0093 — The engine differential left 1,443 of 1,700 generated returns unknown from Form 1040 line 10 down

- **Date:** 2026-10-22
- **Caught by:** the evidence-report rewrite of integrity plan item 0.1 (`docs/2026-10-22_integrity_plan.md`), which read
  the engine differential's per-line counts and found `reports/2025/engine_differential.md` at c99e3c5 reporting 1,443
  PolicyEngine-US and 1,231 Tax-Calculator cases "not computed" on `f1040.line10`, every one with the project reason
  `no input supplied for person[taxpayer].f8889[hsa].unsupported`.
- **Symptom:** since the Form 8889 screen's refusal entry moved to printed lines 13 and 16 (BUG-0088, c99e3c5), the screen
  is required on every return that has a Form 8889 entry; `tools/engines/generate_cases.py` gave every return an entry
  but answered the screen only on the returns with HSA contributions. On the other 1,443 returns Schedule 1 line 26,
  Form 1040 line 10 and every line after it were unknown, so the differential compared the two engines against the
  project on about 15% of its cases while reporting 0 unexplained differences.
- **Root cause:** the generator's `f8889.unsupported` answer sat inside the HSA-contribution branch; the comparison
  counts an unknown project value as "not computed" and no rule bounds that count, so a differential that compares
  almost nothing still passes.
- **Where:** `tools/engines/generate_cases.py` (the HSA block); `tools/engines/compare.py` (no floor on "not computed").
- **Why it survived:** check-all's engine_differential step fails only on an unexplained difference; "not computed" is a
  reported column, not a failure; the Stage 16 handoff's "1,700 cases, 0 unexplained" was measured before c99e3c5 and
  the cleanup commit's regenerated report was not read.
- **Fix:** the screen answer moved out of the conditional so every generated return answers it; the differential rerun
  returns every count to its pre-c99e3c5 value (0 unexplained, 4 explained). Open: a floor in `compare.py` that fails
  the run when "not computed" exceeds a stated share of cases on any mapped line, so a blind differential cannot pass
  (integrity plan item 1.4). Integrity plan item 0.1 commit.
- **Tags:** tool-defect; generator; comparison-blind-spot; silent-degradation; caught-by-audit

## BUG-0094 — Schedule A medical floor goes negative with a negative adjusted gross income

- **Date:** 2026-10-22
- **Caught by:** the engine differential after integrity plan item 1.4(a) extended the generated cases (case se-00255:
  Tax-Calculator `sa.line17` $0.00 against the project's $324.85; PolicyEngine-US agreed with Tax-Calculator but its
  comparison was excluded by the `salt_exceeds_agi` feature, which fires spuriously when AGI is negative).
- **Symptom:** on a return with adjusted gross income below zero (a Schedule C loss larger than the other income) and no
  medical expenses, Schedule A line 3 (7.5% of line 2) is negative, line 4 ("Subtract line 3 from line 1. If line 3 is
  more than line 1, enter -0-") is the positive of that amount, and the itemized total carries a medical deduction
  with nothing paid: $324.85 on AGI of −$4,331.38.
- **Root cause:** `forms/2025/sa.yaml` computes line 3 as `multiply_rate` of line 2 (a copy of Form 1040 line 11b, typed
  `Dollars`, signed) and line 4 as `subtract_floor0` of line 1 less line 3; neither floors AGI or line 3 at zero. The
  instruction (i1040sca, line 1) allows "only the part of your medical and dental expenses that exceeds 7.5% of ...
  adjusted gross income"; both engines floor AGI at zero before the percentage.
- **Where:** `forms/2025/sa.yaml` (`sa.line3`, `sa.line4`); the derived feature `salt_exceeds_agi` in
  `tools/engines/run_engines.py` (should require `sa.line5d > 0`).
- **Why it survived:** no fixture has a negative AGI with Schedule A; the generated returns reached negative AGI only
  once self-employment losses were drawn (Stage 14) and the Schedule A line was excluded for most of them by the
  spurious feature; the render review read line 3 as a faithful rendering of "Multiply line 2 by 7.5%", which it is;
  the Lean evaluator computes the same signed product.
- **Fix:** open; the engine difference is recorded as explained with the deciding sentence in
  `fixtures/2025/differential/engine_investigations.json`. Floor line 3 (or its AGI operand) at zero in `sa.yaml`
  with a fixture at negative AGI; make `salt_exceeds_agi` require a positive line 5d. Counts toward the integrity
  plan's Phase 1 stop rule (the third value error).
- **Tags:** signed-operand; floor-missing; latent-until-new-input; caught-by-engine-differential; caught-by-audit

## BUG-0095 — A dependent without a taxpayer identification number is claimed and can qualify the filer for head of household

- **Date:** 2026-10-22
- **Caught by:** the Direct File fact-dictionary comparison of integrity plan item 1.7 (`reviews/2025/direct-file/predicates.md`,
  finding F1): Direct File requires a TIN on every claimed dependent and knocks out a head-of-household qualifying person
  without one; the project's `dependent.claimed`, `dependent.hoh_test1` and `dependent.hoh_test2` never read `dependent.tin`.
- **Symptom:** a person entered with `dependent.tin = false` who passes Steps 1 to 2 or Step 4 is counted as a dependent on
  Form 1040 and can satisfy a head-of-household test; the return is computed where the instructions require an SSN entry
  the filer cannot make.
- **Root cause:** the TIN input is read only by `dependent.ctc_child`, `dependent.odc_person` and the Form 2441 gate
  `dependent.dc_no_tin`; the dependents section's "You must enter each dependent's social security number (SSN)" (i1040gi
  2025 p. 22) was encoded nowhere, and its one exception (a child born and died in 2025, "Died" entered with a birth
  certificate) was named as outside the tool only at `dependent.dc_count`.
- **Where:** `forms/2025/dependent.yaml` (`dependent.claimed`, `dependent.qc_dependent`, `dependent.qr_dependent`, the
  head-of-household tests).
- **Why it survived:** the render and transcription reviews judge each line against the page it cites, and no line cites the
  SSN-entry sentence; no fixture has a dependent without a TIN outside the credit lines; the engines take dependents as
  given.
- **Fix:** open (owner's decision 2026-10-22): a refusal on claiming a dependent with no TIN, naming the born-and-died case
  in the remedy, with a fixture.
- **Tags:** missing-gate; household-predicates; caught-by-direct-file-comparison; caught-by-audit

## BUG-0096 — The filer's SSN test for the earned income credit uses the employment-validity definition

- **Date:** 2026-10-22
- **Caught by:** the Direct File fact-dictionary comparison of integrity plan item 1.7 (finding F3): Direct File tests the
  filer's SSN for the EIC with the EIC definition (`filers/*/ssnValidForEitc`); the project's `eic.step1_ssn` reads
  `household.all_work_ssn`, built from `person.work_ssn` ("valid for employment"), the child tax credit's definition.
- **Symptom:** a filer whose card says "Not Valid for Employment" but was not issued solely to receive a federally funded
  benefit has a valid SSN for the EIC (i1040gi 2025 p. 44: "a valid SSN is a number issued by the Social Security
  Administration unless 'Not Valid for Employment' is printed on the social security card and the number was issued solely
  to allow the recipient of the SSN to apply for or receive a federally funded benefit") and answers `person.work_ssn` No,
  so the project gives no EIC where the text allows it. The project applies the right definition to the child
  (`dependent.eic_ssn`) but not to the filer.
- **Root cause:** one person-level SSN input serves two credits whose definitions differ.
- **Where:** `forms/2025/eic.yaml` (`eic.step1_ssn`), `forms/2025/household.yaml` (`household.all_work_ssn`),
  `forms/2025/person.yaml` (`person.work_ssn`).
- **Why it survived:** the render review of `eic.step1_ssn` read "SSN valid for employment" as a faithful rendering of
  "valid SSN"; no fixture has a filer with that card type; the engines take EIC eligibility from an SSN flag.
- **Fix:** open (owner's decision 2026-10-22): a filer-level EIC SSN input mirroring `dependent.eic_ssn`, read by
  `eic.step1_ssn`; the CTC keeps `person.work_ssn`. Counts toward the integrity plan's Phase 1 stop rule.
- **Tags:** wrong-definition; shared-input-two-rules; household-predicates; caught-by-direct-file-comparison; caught-by-audit

## BUG-0097 — No gate for a prior disallowance of the EIC or the child credits (Form 8862; two- and ten-year bans)

- **Date:** 2026-10-22
- **Caught by:** the Direct File fact-dictionary comparison of integrity plan item 1.7 (finding F4): Direct File asks about
  improper-claim notices for the EIC and the CTC/ACTC/ODC and zeroes the credits under an active ban; `grep` of
  `forms/2025/*.yaml` for 8862, disallowed or reckless finds nothing.
- **Symptom:** a filer barred from the credit (i1040gi 2025 p. 43: "don't file Form 8862 or take the credit for the: 2 years
  after the most recent tax year for which there was a final determination that your EIC claim was due to reckless or
  intentional disregard of the EIC rules, or 10 years after ... fraud"; the same bans for the CTC, ACTC and ODC in the
  Schedule 8812 instructions), or one who must attach Form 8862, has the credit computed with nothing asked.
- **Root cause:** the eligibility steps were encoded from the Step 1 to 6 questions; the disallowance paragraph before them
  carries no step number and was not encoded.
- **Where:** `forms/2025/eic.yaml`, `forms/2025/s8812.yaml`.
- **Why it survived:** no line cites the paragraph, so no review read it; no fixture has a banned filer; the engines have no
  such input.
- **Fix:** open (owner's decision 2026-10-22): one filer-level question (a reduction or disallowance of the EIC, CTC, ACTC or
  ODC for a year after 1996 other than a math or clerical error) feeding a refusal on `eic.credit` and `s8812.line12`
  ("Form 8862 and the disallowance period are outside this tool"), with fixtures. Counts toward the Phase 1 stop rule.
- **Tags:** missing-gate; unnumbered-paragraph; household-predicates; caught-by-direct-file-comparison; caught-by-audit

## BUG-0098 — Tax Computation Worksheet row results keyed to column (d)

- **Date:** 2026-10-22
- **Caught by:** render comparison by the second model family (spec 6.5; deepseek-v4-pro,
  `reviews/2025/render/tcw.deepseek.md`): twenty MISMATCH verdicts, one per `<status>.rowN.tax` line, each reasoning
  "The IRS line (d) is the 'Subtraction amount' of $N, not the result of subtracting it from column (c); 'Subtract (d)
  from (c)' is the separate Tax-column instruction." The Claude render review of the same rendering had returned 46 of
  46 MATCH. The first independence yield of the second family (integrity plan item 1.3).
- **Symptom:** none in values. The 20 row result lines of `forms/2025/tcw.yaml` carried `printed: "(d)"` and
  `label: "Subtract (d) from (c)"`, so the rendering presented each row's tax as column (d); on the page (i1040gi
  p. 80) the heading "(d) Subtraction amount." names the fixed amount ($5,086.00 and so on), while the result belongs
  under the unlettered column headed "Tax. Subtract (d) from (c). Enter the result here and on the entry space on
  line 16." The expression (the product less the subtraction parameter) was correct.
- **Root cause:** the transcription keyed each row's result to the letter in its instruction text rather than to the
  heading of the column the result is entered in; the Tax column has no letter.
- **Where:** `forms/2025/tcw.yaml`, the 20 `<status>.rowN.tax` lines.
- **Why it survived:** value-neutral, so fixtures, the Tax Table conjecture, mutation and class M could not see it;
  the transcription comparison expands `tax` and is marker-blind; the Claude render reviewer accepted "(d) — Subtract
  (d) from (c)" as a match because the instruction fragment is on the page.
- **Fix:** the 20 lines re-keyed to `printed: "Tax"` with the column heading as label; ids, expressions, types and
  citations unchanged; `(b)` and `(d)` stay inline year parameters whose values the rendering prints. Fixtures,
  conjecture and mutation unchanged; all four review logs rerun with no open ruling (DeepSeek render now 46 of 46).
  Integrity plan second-batch commit.
- **Tags:** transcription/marker-keying; value-neutral; caught-by-second-family-render-review; caught-by-audit

## BUG-0099 — Schedule D Tax Worksheet line 4 copies a Form 4952 amount when no Form 4952 is filed

- **Date:** 2026-10-22
- **Caught by:** the OpenTaxSolver differential (integrity plan item 1.4(b); 85 generated cases, feature
  `sdtw_line4_without_4952`): OTS enters zero on worksheet line 4 when no Form 4952 is filed; the project copies
  `f4952.line4e`, which `forms/2025/f4952.yaml` figures whether or not the form is filed.
- **Symptom:** none in values. Line 3 of the worksheet is zero on those returns, so lines 5 and 8 and the tax are
  unmoved; the worksheet's line 4 shows an amount the filer would not have, and the derivation names a form the return
  does not include.
- **Root cause:** `sdtw.line4` copies the Form 4952 line unconditionally; the printed line reads "Enter the amount from
  Form 4952, line 4e*" (i1040sd, Schedule D Tax Worksheet), which presupposes a filed form.
- **Where:** `forms/2025/sdtw.yaml` (`sdtw.line4`), `forms/2025/f4952.yaml` (`f4952.line4e` computed without a filing
  gate).
- **Why it survived:** value-neutral on every fixture and generated return; the render review read "Enter the amount from
  Form 4952 line 4e" as faithful; no engine before OTS computed the worksheet's lines.
- **Fix:** open; a `choose` on whether Form 4952 is filed (zero otherwise), with the register consulted on the asterisk's
  footnote. Explained in `fixtures/2025/differential/engine_investigations.json` meanwhile.
- **Tags:** value-neutral; unconditional-copy; caught-by-engine-differential; caught-by-audit

## BUG-0100 — Form 8995 line 11 floors taxable income before the QBI deduction at zero

- **Date:** 2026-10-22
- **Caught by:** the OpenTaxSolver differential (integrity plan item 1.4(b); 33 generated cases, feature
  `taxable_before_qbi_negative`): OTS prints line 11 as Form 1040 line 11a less lines 12e and 13b, signed; the project's
  `qbi.taxable_before` floors it at zero.
- **Symptom:** sign only. Line 13 (20% of line 11) floors at zero on both sides and the deduction is unmoved; the printed
  line 11 shows $0 where the instruction's arithmetic gives a negative amount.
- **Root cause:** i8995, Line 11: "Enter your taxable income figured before any QBI deduction, computed as follows ...
  line 11a, minus lines 12e and 13b" states a subtraction with no floor; the encoding typed the line NonNegDollars.
- **Where:** `forms/2025/f8995.yaml` / `qbi.yaml` (`qbi.taxable_before`).
- **Why it survived:** the deduction is unchanged, so no fixture, property or engine summary line could see it; the render
  review did not object to the floor.
- **Fix:** open; type the line `Dollars` and drop the floor, keeping the floor at line 13 where the form has it; fixture at
  negative taxable income. Explained in `engine_investigations.json` meanwhile.
- **Tags:** floor-added; sign-only; caught-by-engine-differential; caught-by-audit

## BUG-0101 — Human source readings never enter the evidence report

- **Date:** 2026-10-22
- **Caught by:** continuation audit, tracing the standard-deduction packet through `serve.py`,
  `check_logs.py` and `engine/src/fixtures.ts`.
- **Symptom:** a person can save a reading log, but the evidence report reads only fixtures and engine
  comparisons. The planned human-reading credit cannot appear. The plan also calls these readings class B,
  although spec 6.1 reserves B for human-calculated expected values.
- **Root cause:** the packet/log tools and evidence report were implemented separately, without a complete
  reading-to-report check.
- **Where:** `tools/human_review/`, `tools/transcription/check_logs.py`, `engine/src/fixtures.ts`.
- **Why it survived:** no human log existed and no test supplied one through the whole path.
- **Fix:** add H for human source readings, separate from worked-value class B; the log checker and report
  share a validator. Only current MATCH records with a reason, committed by the named reader with those exact
  contents, count. Expanded helpers are credited explicitly; referenced printed lines are not.
- **Tags:** evidence-accounting; missing-integration; caught-by-audit

## BUG-0102 — A human verdict can silently attest to content the reader did not see

- **Date:** 2026-10-22
- **Caught by:** continuation audit of packet freshness and partial saves.
- **Symptom:** the standard-deduction packet judges Form 1040 line 12e with Schedule A and person helpers,
  but its saved subject hashes only Form 1040's rendering. Changing a folded helper does not stale the log.
  Saving an older browser page also stamps the current subject hash onto an old verdict. Blank entries are
  written as log records; a partial save can erase an earlier verdict.
- **Root cause:** the server recomputes the subject at save time without checking what the browser displayed,
  and uses one form hash for a reading spanning several forms.
- **Where:** `tools/human_review/packet.py`, `serve.py`, `reading.py`, `tools/transcription/check_logs.py`.
- **Why it survived:** freshness checks were copied from form-local model reviews; neither cross-form helper
  changes nor old browser submissions were exercised.
- **Fix:** per-line receipts cover the displayed reading, folded helpers, dependency forms, parameters,
  source snapshots and reading tools. Saves require the browser's receipt to match. Stale saved verdicts and
  drafts are not restored into a new packet. Blank entries stay in the browser; saving requires both a verdict
  and a reason, and preserves other completed entries. Refuse packets built from stale canonical data.
- **Tags:** stale-evidence; review-subject; partial-save; caught-by-audit

## BUG-0103 — Evidence report can use an earlier engine-differential run

- **Date:** 2026-10-22
- **Caught by:** continuation audit of the evidence report's ordering in `tools/check_all_steps.sh`.
- **Symptom:** `evidence` runs in the same wave as `engine_differential`, reading the summary file before
  that run has finished. The green tree can contain a scoreboard based on the previous engine summary.
- **Root cause:** the report was treated as independent of the differential that supplies its E column.
- **Where:** `tools/check_all_steps.sh`.
- **Why it survived:** the summary is deterministic when the inputs are unchanged, hiding the dependency
  until the engine mapping or generated cases change.
- **Fix:** run `evidence` in the following wave, after every engine-differential step has succeeded.
- **Tags:** evidence-accounting; check-order; caught-by-audit

## BUG-0104 — Standard-deduction review asks for the whole calculation in one verdict

- **Date:** 2026-10-22
- **Caught by:** the owner's use of the standard-deduction packet: "i'm being asked to verify a huge
  amount in this one item. it's overwhelming."
- **Symptom:** one Form 1040 line expands ten intermediate computations, their citations, exceptions and
  examples, asking the reader to approve the entire chain at once.
- **Root cause:** the printed line was chosen as the unit of human attention as well as evidence storage.
- **Where:** `tools/human_review/packet.py`, `reading.py`, `logs.py`.
- **Why it survived:** automated checks verified images, saving and evidence integration, but did not
  establish that the amount of material was manageable for a person.
- **Fix:** item 2 becomes fourteen short questions, shown one at a time beside their own source excerpts.
  The English still comes from the canonical expressions, with referenced amounts named instead of expanded.
  Each saved verdict credits only its own computation. The reader can save and stop or skip ahead without
  approving the other questions. Full pages and implementation detail remain available on demand.
- **Tags:** review-usability; oversized-review-unit; owner-found

## BUG-0105 — Save & next appears unresponsive when required fields are missing

- **Date:** 2026-10-23
- **Caught by:** the owner's use of the review packet: "save and next doesn't work"; the live server
  received no POST from the attempts, locating the failure before the save endpoint.
- **Symptom:** validation stops the button when a verdict, reason or reader name is absent, but explains
  that only in the header, which can be out of view. Required fields are not labelled consistently.
- **Root cause:** validation feedback was separated from the button and did not focus the missing field.
- **Where:** `tools/human_review/packet.py`.
- **Why it survived:** the browser test prefilled every field and triggered a programmatic click; it did
  not exercise the missing-field paths a person encounters.
- **Fix:** label required fields, show save feedback beside the navigation, focus the field that needs
  attention, show pending saves, prevent duplicate submissions and keep failed saves on the same question.
  Restoring an older draft preserves the reader's notes while requiring a fresh verdict. Browser tests now
  use pointer clicks and cover missing fields, rejected receipts and draft recovery in a temporary repo.
- **Tags:** silent-validation; review-usability; owner-found

## BUG-0106 — Second-family report still applies the superseded raw-agreement floor

- **Date:** 2026-10-23
- **Caught by:** continuation audit of integrity-plan decision 12 against `compare_families.py`.
- **Symptom:** a correct systematic objection can disqualify a reader, while disagreements later ruled
  model errors are not measured under the agreed ten-percent noise limit.
- **Root cause:** the owner's replacement rule was recorded in the plan but not implemented.
- **Where:** `tools/transcription/compare_families.py`, `check_logs.py`.
- **Why it survived:** the report itself described the older rule and had only one second-family pilot.
- **Fix:** count model-error rulings over the second family's judged lines per form-kind run. Findings,
  representation, scope and ambiguity are separate. Missing/invalid/duplicate verdicts, stale sources,
  unclassified/open rulings and a wrong model keep evidence pending. Required families must qualify;
  optional pending results remain visible. Raw agreement is diagnostic only; current yield is explicitly
  distinguished from historical fixed findings in the bug inventory.
- **Tags:** evidence-accounting; wrong-acceptance-rule; caught-by-audit

## BUG-0107 — Independent transcription receives labels describing the project's computations

- **Date:** 2026-10-23
- **Caught by:** integrity handoff flag, confirmed by reading the prompt builders and a Schedule A dry run.
- **Symptom:** printed targets, exported helpers, collection fields and cross-form references expose
  project-written labels that can name operands or arithmetic, helping the second reader follow the encoding.
- **Root cause:** descriptive interface catalogs reused the same labels as the project's own rendering.
- **Where:** `tools/transcription/transcribe.py`.
- **Why it survived:** isolation checked model file/tool access, not information included in the prompt.
- **Fix:** computed catalogs contain ids, printed markers and types only. Input questions, parameter values
  and collection schemas remain shared interfaces, explicitly acknowledged; computed labels and expressions
  are absent. The new prompt policy is recorded and a pre-policy transcription cannot earn second-family
  eligibility. Offline sentinel tests check that computed labels and operands do not leak.
- **Tags:** independence; prompt-contamination; caught-by-audit

## BUG-0108 — Reusing a saved review response can falsely attach a different prompt

- **Date:** 2026-10-23
- **Caught by:** continuation audit of `--from-response` and `--dry-run` in the review tools.
- **Symptom:** the tool writes a newly built prompt before loading an older response, then records the
  new prompt hash as though that request had produced it. A dry run can also overwrite the saved request.
- **Root cause:** raw response metadata was not bound to its prompt, system instructions, requested model
  and prompt policy.
- **Where:** `tools/transcription/transcribe.py`, `render_compare.py`, `classm.py`, `rerun_all.py`.
- **Why it survived:** response parsing and subject freshness were checked independently of request provenance.
- **Fix:** transcription, render and class M response receipts bind all four fields and preserve the actual request;
  reuse requires exact equality, including the saved prompt bytes. Legacy unbound responses require a fresh
  call. Dry runs write a separate preview. The batch driver resumes only through this validation and writes
  progress as each job completes. Class M also rebuilds current jobs on reuse: a changed supplied
  amount requires fresh work, and dry runs cannot overwrite actual request receipts or fixtures.
- **Tags:** stale-evidence; false-provenance; cached-response; caught-by-audit

## BUG-0109 — Definition transcription reports a qualified interface id as missing

- **Date:** 2026-10-23
- **Caught by:** the first Schedule SE second-family pilot after the prompt-independence repair.
- **Symptom:** the model returns Schedule SE line 13 as `se.line13`; the comparison expects the shared
  definition's bare `line13` and reports it missing without comparing the supplied arithmetic.
- **Root cause:** the prompt mixes form-prefixed id examples with exact bare definition interfaces, and
  the comparator has no definition-namespace normalization.
- **Where:** `tools/transcription/transcribe.py`.
- **Why it survived:** the earlier reader followed the project's id convention; missing outputs were
  treated as a review dispute rather than an interface mismatch.
- **Fix:** request exact ids consistently, describe exported printed result interfaces separately from
  helpers, and strip a definition's own namespace only from exact published ids and their references.
  Unknown helper names are retained; conflicting aliases fail. Arithmetic is unchanged and is still
  compared; normalizing the Schedule SE pilot exposes a real expression difference to rule on, not an
  automatic agreement. The raw response and its actual prompt receipt remain unchanged.
- **Tags:** review-interface; false-missing; caught-by-second-family-pilot

## BUG-0110 — Unexpected review lines can dilute the second-family noise rate

- **Date:** 2026-10-23
- **Caught by:** adversarial audit of the repaired second-family eligibility gate.
- **Symptom:** an expected line ruled model error plus ten extra MATCH lines can appear to pass
  the ten-percent rule, although the only requested line was wrong.
- **Root cause:** the denominator counted every parsed line without restricting it to the expected
  interface, and unexpected line keys did not block qualification.
- **Where:** `tools/transcription/compare_families.py`.
- **Why it survived:** normal review writers emit only requested lines, so valid pilot logs did not
  exercise a malformed or hand-edited log with extra keys.
- **Fix:** count only expected judged lines and keep reviews with unexpected keys pending. An offline
  regression verifies that ten extra agreements cannot dilute one error out of one requested line.
- **Tags:** evidence-accounting; wrong-denominator; caught-by-adversarial-audit

## BUG-0111 — Qualifying-person disability checkbox uses age at year-end

- **Date:** 2026-10-23
- **Caught by:** DeepSeek V4 Pro render comparison of `dependent`, independently confirmed against i2441 p. 3.
- **Symptom:** Form 2441 line 2(c) is checked for a disabled qualifying child who turns 13 during the
  year even when all reported care was provided before the thirteenth birthday. The instructions
  require being over age 12 at the time of care. This changes a displayed checkbox, not the tax amount.
- **Root cause:** `dependent.dc_line2c` tests year-end age >=13 and incapacity; the interface asks about
  care before age 13 for eligibility but does not ask whether the disabled person's care also occurred
  at age 13 or older.
- **Where:** `forms/2025/dependent.yaml`, `dependent.dc_line2c`.
- **Why it survived:** existing disabled-person cases use an older child; the age-13 case is not disabled.
  Earlier source reading accepted the year-end-age proxy.
- **Reproduction:** copy `stage15.f2441.s8` inputs, change `dependent[a].age` from 15 to 13 and set
  `dependent[a].dc_under13=true`; `eval --target 'dependent[a].dc_line2c'` returns true. These inputs also
  describe a disabled child whose care occurred entirely before the birthday, when the checkbox must
  be false. The model cannot distinguish that case from care after the birthday.
- **Source:** archived i2441 (2025), p. 3, qualifying-person Column (c): the test is age at care, not
  year-end age (text hash 361baee739cc7cb7b6a84c7412397cfba901c1a3e5f225a8077cb8716917887e).
- **Fix:** staged in `docs/patches/BUG-0111.patch`: a source-worded care-timing question for a disabled
  qualifying person turning 13, automatic answers outside that boundary, and paired before/after
  fixtures. After rebasing the staged fixture hunk on the BUG-0120 cases, an isolated build and all
  1,066 CLI fixtures pass, plus six targeted age/timing checks. The main tree still has 1,064 cases.
  Not applied to the active tree. Although item 2 does not depend on dependent.yaml, registering the
  new question changes the year-wide question bank included in every human receipt. Keep the patch
  staged while the owner completes the active reading; applying it requires a deliberate receipt refresh.
- **Tags:** source-reading; age-boundary; displayed-checkbox; caught-by-second-family

## BUG-0112 — Raw review parser can hide duplicate judgments before validation

- **Date:** 2026-10-23
- **Caught by:** adversarial audit following BUG-0110.
- **Symptom:** a raw render response can give MISMATCH and then MATCH for one key; the parser silently
  retains only the latter, so the log-level duplicate check never sees the conflict. Duplicate
  transcription ids also collapse in lookup maps. Invalid render statuses are converted to UNCLEAR.
- **Root cause:** response parsers overwrite duplicate dictionary keys before the eligibility gate
  reads the generated log, and coerce invalid verdicts instead of rejecting malformed output.
- **Where:** `tools/transcription/render_compare.py`, `transcribe.py`, `classm.py`.
- **Why it survived:** the new gate tests duplicate log headings, but real writers consume raw responses
  before producing those headings.
- **Fix:** reject duplicate raw verdict/worked-line keys and transcription ids, malformed line lists or ids, invalid
  render statuses and missing reasons before writing a review log. Preserve the raw response for
  investigation. Offline tests exercise the parser-to-log boundary, including a disappearing objection.
- **Tags:** evidence-accounting; parser-validation; lost-disagreement; caught-by-adversarial-audit

## BUG-0113 — A peer reset bypasses the review transport's retry policy

- **Date:** 2026-10-23
- **Caught by:** the full DeepSeek render run (s1a), then the fresh dependent transcription retry.
- **Symptom:** a connection reset while reading the response terminates the job immediately,
  although transient URL/HTTP failures use bounded backoff.
- **Root cause:** urllib can raise ConnectionResetError directly from response-body reads rather
  than wrapping it in URLError, the exception handled by the retry loop.
- **Where:** `tools/transcription/transcribe.py`, `_call_deepseek` (shared transport).
- **Why it survived:** the connection check and early pilot calls did not hit a peer reset.
- **Fix:** catch direct ConnectionError failures and retry the identical fixed request under the
  existing retry limit/backoff. On exhaustion fail without producing review evidence. Offline
  tests verify identical request bytes after a reset and the bounded number of attempts.
- **Tags:** transport; retry-policy; caught-by-full-run

## BUG-0114 — Reasoning can consume the entire fixed output budget

- **Date:** 2026-10-23
- **Caught by:** full DeepSeek transcription of sc/scveh at maximum reasoning effort.
- **Symptom:** sc returns empty content with finish_reason=length: all 65,536 completion tokens were
  reasoning tokens. The tool reports missing YAML instead of identifying output exhaustion.
- **Root cause:** one fixed budget covered both reasoning and the final answer, with no per-run
  override and no rejection based on a length finish reason before parsing/credit.
- **Where:** the shared transport/response receipt in `tools/transcription/transcribe.py` and review CLIs.
- **Why it survived:** smaller pilot documents finished within the fixed budget.
- **Fix:** expose `--max-output-tokens`, bind the effective output budget in response receipts and logs,
  and reject truncated responses on both fresh calls and reuse while preserving the raw receipt.
  Earlier bound requests without the new field retain their actual fixed 65,536 budget; they cannot
  be relabeled as larger-budget calls. Tests cover both directions, unchanged old receipts and
  rejection even when truncated content happens to be valid YAML. Retry large documents with
  131,072 tokens while retaining maximum reasoning effort.
- **Tags:** transport; output-truncation; request-provenance; caught-by-full-run

## BUG-0115 — Model-family checks do not enforce the owner's selected model

- **Date:** 2026-10-23
- **Caught by:** the owner's correction to use deepseek-flash, followed by an eligibility audit.
- **Symptom:** the tools can call Pro and qualify its logs because Pro and Flash both belong to
  the deepseek family, even after the documentation selects Flash.
- **Root cause:** family requirements contain no model pin; call and review eligibility checks
  distinguish families but not the specific model the owner selected.
- **Where:** `tools/transcription/families.json`, `families.py`, `transcribe.py`, `compare_families.py`.
- **Why it survived:** the earlier handoff directed Pro, and the correction was initially recorded
  in prose only. The family-level gate cannot enforce that correction.
- **Fix:** pin deepseek-flash in families.json, reject other DeepSeek models before a network/keychain
  call, and keep a review pending unless its requested/reported model matches the pin. Preserve
  Pro artifacts with hashes separately; never relabel them as Flash output. Offline tests cover
  both accidental Pro calls and Pro results under a Flash request.
- **Tags:** model-selection; evidence-provenance; caught-by-owner

## BUG-0116 — Mutation exemptions retain dead entries and silent prose fallbacks

- **Date:** 2026-10-23
- **Caught by:** integrity-plan item 1.6, the existing equivalence audit, and continuation cleanup.
- **Symptom:** eight entries describe mutants already killed by checks/fixtures. Nine more prose
  entries are hidden behind mechanical copy-chain checks, but could become accepted fallbacks
  if those checks stop proving equivalence after a data change.
- **Root cause:** the exemption tables retain earlier arguments after fixtures or mechanical
  checks supersede them; the prose table remains an unconditional fallback.
- **Where:** `engine/src/mutate.ts`, EQUIVALENT and EQUIVALENT_IF.
- **Why it survived:** an unchanged adjusted score does not reveal dormant exemption entries.
- **Fix:** remove the eight dead entries and nine shadowed prose entries. The nine surviving
  copy-chain cases now rely on the mechanical check. Retain the other 15 prose entries and 57
  conditional entries for the remaining independent review/mechanization work; no new exemption
  is added.
- **Verification:** all eight removed dead entries were re-probed and killed by fixtures. A fresh
  2,278-mutant run retains 235 checker kills, 1,915 fixture kills and 128 equivalent survivors;
  all nine copy-chain cases still have mechanical proofs. Raw score 94.4%, adjusted score 100%.
- **Tags:** stale-equivalence; silent-fallback; caught-by-integrity-audit

## BUG-0117 — Foreign care-provider identification choice omits a required condition

- **Date:** 2026-10-23
- **Caught by:** deepseek-flash render comparison of dcprov line 1(c); confirmed against archived i2441 p. 3.
- **Symptom:** the LAFCP choice requires only living abroad and the foreign provider lacking a U.S.
  identification number. The IRS also requires the provider not to be required to obtain one.
  A provider who should have obtained a number can therefore be assigned the wrong column (c) entry.
- **Root cause:** the input wording compresses two conditions (does not have and is not required
  to get a U.S. taxpayer identification number) into one missing-number condition.
- **Where:** `forms/2025/dcprov.yaml`, dcprov.tin_kind input wording and citation.
- **Why it survived:** Claude and the earlier Pro render review accepted the shortened wording;
  amount-based fixtures do not distinguish the provider's obligation to obtain an identifier.
- **Fix:** add the missing not-required-to-obtain condition and its archived source sentence.
  Applied; both Flash and Claude transcription/render reruns agree on all dcprov lines.
  No amount, enum value or arithmetic changes.
- **Tags:** input-wording; omitted-condition; source-reading; caught-by-flash

## BUG-0118 — Review prompt preparation repeatedly uses the slow YAML parser

- **Date:** 2026-10-23
- **Caught by:** profiling dcprov render prompt preparation during the Flash run.
- **Symptom:** preparing a three-line review takes 13.0 seconds under profiling, with 167 local
  YAML loads consuming 12.9 seconds before the model is called.
- **Root cause:** project catalogs repeatedly use PyYAML's Python safe loader despite the installed
  LibYAML safe loader being available.
- **Where:** `tools/transcription/transcribe.py`, `render_compare.py`, local project YAML reads.
- **Why it survived:** job timings combine local preparation with model latency, hiding this cost.
- **Fix:** use the LibYAML safe loader for local project files when installed, with the Python safe
  loader as fallback. Keep raw model-response parsing on its existing validation path. A regression
  compares both loaders over every form and the year parameters. The same profiled dcprov request
  now prepares in 1.25 seconds and its prompt SHA-256 is identical; all 37 review-tool tests pass.
- **Tags:** performance; prompt-preparation; caught-by-profiling

## BUG-0119 — Dependent-care benefit expenses are limited to a payment year

- **Date:** 2026-10-23
- **Caught by:** deepseek-flash render comparison of f2441 line 16; confirmed against archived i2441 p. 5.
- **Symptom:** the extra-expense question asks only for 2025 care paid or to be paid in 2026. Qualified
  care incurred in 2025 but paid later has no place to be entered, understating line 16 and potentially
  overstating taxable dependent-care benefits on Form 1040 line 1e.
- **Root cause:** the question uses a next-year payment example as a scope limit, although the source
  says the payment date does not matter for the Part III expense total.
- **Where:** `forms/2025/f2441.yaml`, f2441.paid_2026 label and source wording.
- **Why it survived:** fixtures exercise 2025 and next-year payments; the arithmetic correctly sums
  whatever amounts are supplied, so amount tests do not detect the missing question scope.
- **Reproduction:** adapt stage15.f2441.s4 to $4000 benefits and $4000 qualifying care incurred in
  2025, all payable after 2026, with no current-year paid care. Following the old questions leaves
  line 16 at zero and line 26/Form 1040 line 1e at $4000. Including all incurred expenses gives
  line 16 $4000, excluded benefits $4000 and taxable benefits zero. Numeric witness saved in
  `.transcription/f2441-payment-year-witness.json`.
- **Source:** i2441 (2025), p. 5, Line 16: total qualified expenses incurred in 2025; payment timing
  does not matter (text hash 361baee739cc7cb7b6a84c7412397cfba901c1a3e5f225a8077cb8716917887e).
- **Fix:** broaden the existing extra-expense question to all qualifying 2025 incurred expenses not
  already counted per person, regardless of payment date, including still-unpaid expenses. Retain
  the existing input id for fixture compatibility; no arithmetic or new interview-bank entry is needed.
  Applied; both families' affected render reruns now mark line 16 MATCH. The main build,
  all 1055 then-current CLI fixtures and citation checks pass. All 14 active item-2 receipts
  remain unchanged. The older transcription ruling's incorrect payment-year premise was
  explicitly corrected; the archived prior ruling remains available.
- **Tags:** input-wording; omitted-expenses; taxable-benefits; caught-by-flash

## BUG-0120 — Dependent-care forfeiture check includes prior-year benefits

- **Date:** 2026-10-23
- **Caught by:** deepseek-flash render comparison of f2441 line 15, confirmed against archived i2441 p. 5.
- **Symptom:** line 14 can exceed the current-year benefits on line 12 as long as it does not
  exceed lines 12 and 13 together. A prior-year grace-period amount used in 2025 incorrectly
  enlarges the allowed current-year forfeiture/carryforward.
- **Root cause:** the validation gate compares line 14 with the subtotal used in line 15's
  subtraction, rather than the line 12 amount the IRS explicitly says contains line 14.
- **Where:** `forms/2025/f2441.yaml`, f2441.line14_bad and line 15 refusal remedy.
- **Why it survived:** the question already asks for amounts included on line 12, so consistent
  answers produce correct arithmetic; fixtures did not test inconsistent entries between the
  two possible limits. The transcription comparator omits refusal gates from printed-line trees.
- **Reproduction:** line 12 $1000, line 13 $500, line 14 $1200 formerly yields line 15 $300.
  Saved before/after evaluator witnesses are `.transcription/f2441-line14-{before,after}.json`.
- **Source:** i2441 (2025), p. 5, Line 14 limits forfeited/carried-forward amounts to those included
  on line 12. Line 13 is a separate prior-year amount already used in the grace period.
- **Fix:** compare line 14 directly with line 12 and correct the refusal's remedy. Three synthetic
  regressions test one cent below, at and above the $1000 limit with a $500 prior-year carry-in;
  the first two retain the source arithmetic and the third refuses. No new input is introduced.
- **Tags:** validation; incorrect-bound; dependent-care-benefits; caught-by-flash

## BUG-0121 — Review rulings can retain an obsolete input-wording premise

- **Date:** 2026-10-23
- **Caught by:** source adjudication after fixing BUG-0119 and rerunning the affected transcription.
- **Symptom:** the Form 2441 line 16 transcription inherits a prior ruling whose explanation
  incorrectly equated a 2026-only payment question with all 2025 incurred expenses, even though
  the new review's input wording and prompt changed.
- **Root cause:** rulings are keyed by the printed line and canonical project/model expressions.
  Input question text and the review prompt are outside that key, although a ruling can rely on them.
- **Where:** `tools/transcription/rulings.py` and the three review writers' reuse of stored rulings.
- **Why it survived:** repeated identical expression trees normally justify reuse; the tools do
  not distinguish a structural identity from a source or input-meaning argument.
- **Immediate correction:** the current line 16 log and sidecar now explicitly identify the old
  false premise and ground the equivalence in the corrected question. Prior artifacts are archived.
- **Fix:** bind automatically reused rulings to the subject, prompts, source excerpts, system and
  request settings. Class M includes every case prompt. Historical unbound rulings remain readable
  but cannot be automatically reused; migration does not certify them in a new context. Six new
  tests cover wording-only changes with identical trees, all three writers, legacy records and
  dropped-value provenance. All 43 offline review-tool tests pass.
- **Tags:** stale-ruling; input-wording; evidence-provenance; caught-by-source-adjudication

## BUG-0122 — Class M sampling loses active dependent-care returns

- **Date:** 2026-10-24
- **Caught by:** the worked-value rerun after BUG-0120: all four selected cases had both care and
  benefits false, and 16 disputes said Part III was skipped.
- **Symptom:** the refreshed hand-work misses the benefits regime whose validation changed.
  Incidental values from unfiled forms can be counted as agreements while the relevant cases vanish.
- **Root cause:** jobs use a fixed random corpus without known valid regression facts, accept
  unfiled forms, and optimize control-flow coverage without ensuring positive values for own
  money inputs. A tighter validation gate can remove the few random active cases.
- **Where:** `engine/src/classm.ts`, `tools/transcription/classm.py`, `rerun_all.py`.
- **Fix:** review runs add existing non-M fixture inputs to the candidate corpus, with no expected
  values exposed to the reviewer. Restricted runs include only fixtures covering the requested
  documents, keeping memory bounded. An explicit per-form filing Bool must be true. The selector
  also includes a positive example for each own money input when one can be built, so carry-ins
  and forfeitures do not silently stay zero. Generated branch coverage remains a sample, not a
  proof that other logical branches are unreachable.
- **Verification:** a regression with only one random draw still selects six active cases from
  existing facts, including positive benefits and nonzero carry-in/forfeiture. The test runs in
  check-all. Fresh Claude and Flash worked-value reviews completed six active cases and all 1064
  CLI fixtures pass; the discarded four-case
  sample and its raw responses are archived under `.classm/archive/f2441-before-fixture-seeds/`.
- **Tags:** evidence-selection; random-coverage-gap; unfiled-form; caught-by-worked-value-rerun

## BUG-0123 — Blank worked-value replies are credited as numeric zero

- **Date:** 2026-10-24
- **Caught by:** source adjudication of the active Form 2441 worked-value rerun, where the model
  explicitly left lines blank after the line 29 stop.
- **Symptom:** a blank or skipped reply becomes zero (or false/Count0/Rate0). If the project also
  evaluates that line to zero, the fixture records an independent M assertion for unworked arithmetic.
  Invalid Bool strings also become false, and fractional Counts are rounded to integers.
- **Root cause:** parse_value collapses missing presentation values into numeric values before
  comparison, and uses permissive conversions for Boolean/count answers.
- **Where:** `tools/transcription/classm.py`, `compare_families.py`, archived class M logs/fixtures.
- **Fix:** preserve blank as SKIPPED, write no fixture expectation for it and exclude it from
  judged/noise counts. Explicit zero remains an assertion. Reject invalid Boolean/fractional Count
  replies. The archived-response audit reclassifies skipped sections and removes their assertions
  without changing raw answers, inputs or remaining expected values; check-all enforces the audit.
- **Verification:** 52 offline review-tool tests pass, including parser, fixture-writing, noise and
  archive-audit regressions. The first full archive audit found 220 numeric assertions to remove
  across 298 historical log sections; raw responses and original derived files are preserved under
  `.classm/archive/blank-assertions-2026-10-24/` with SHA-256 hashes. Independently of those removals,
  the refreshed Claude f2441 sample has 138 numeric agreements, 64 skipped lines and two retained
  owner-ambiguity disputes, whose proposed values are dropped rather than credited as M.
  Flash has 151 numeric agreements and 53 skipped lines; its M form qualification remains pending
  three skipped required line-29 results. Skips do not enter dispute/independence-yield diagnostics.
- **Tags:** false-evidence; blank-as-zero; permissive-parser; caught-by-worked-value-adjudication

## BUG-0124 — Schedule 3 review omits the governing withholding instructions

- **Date:** 2026-10-24
- **Caught by:** adjudicating the repeated Flash Schedule 3 line 11 error, followed by inspecting
  the actual prompt and its recorded source-page table.
- **Symptom:** both the initial and maximum-reasoning transcription requests supply Schedule 3,
  Form 1040 and i1040gi p. 14, but not p. 117's per-person excess-withholding calculation. The
  model chooses the unrelated g28.line7 interface; the initial ruling treated this solely as model
  error without identifying the missing source context.
- **Root cause:** s3.line11 cites only the printed Schedule 3 line. The excerpt selector follows
  that citation, while computed helper labels/expressions are deliberately hidden for independence.
  The IRS sentence explaining the per-person computation is therefore absent.
- **Where:** `forms/2025/s3.yaml`, s3.line11 citation; derived transcription/render review excerpts.
- **Fix:** cite archived i1040gi p. 117 Line 11, including its instruction to figure the amount
  separately for each spouse. Preserve the prior requests, replies and rulings with hashes and
  rerun both families' transcription/render reviews. No expression, parameter or input changes.
- **Qualification:** the wrong reference remains demonstrably wrong ($0 instead of $1481.80 on
  stage13.excess_ss_you), but the earlier context was incomplete. Do not treat that run as a clean
  source-reading test or relabel its archived rationale as having considered p. 117.
- **Verification:** both refreshed transcriptions agree on line 11. Flash's final maximum-reasoning
  request has no open ruling; other differences are application guards and a redundant zero floor.
  Both refreshed render reviews accept the per-person excess-withholding calculation.
- **Tags:** missing-review-context; citation-selection; repeated-model-error; caught-by-source-adjudication

## BUG-0125 — Render review loses scoped glossary dependencies and their sources

- **Date:** 2026-10-24
- **Caught by:** the refreshed Claude Schedule 3 render review after BUG-0124: line 11 remained
  UNCLEAR because person.eligible and person.excess were not defined, despite their governing
  IRS page now being present. Line 1 also lacked the Form 1116 election instructions.
- **Symptom:** a collection field such as person.credit is included, but its unqualified references
  to printed markers "line eligible" and "line excess" are not followed. Separately, the request
  selects sources only from the main form while exposing foreign helper calculations in the glossary.
- **Root cause:** glossary traversal recognizes quoted helper labels, sum fields and refusal gates,
  but omits local printed references within a foreign entry. Source selection does not use the
  glossary dependency set.
- **Where:** `tools/transcription/render_compare.py`, glossary traversal and source-context selection.
- **Fix:** follow local printed references in the entry's own form scope, deduplicate definitions,
  and include citations/parameter citations for the exposed glossary calculations. Explicit foreign
  printed references remain incoming amounts. Input questions remain supplied records: a question
  about a prior-year line must not expand the current-year calculation. The prompt explains the
  glossary's local scope. Cache immutable lookup tables/patterns during a review process.
- **Verification:** five new regressions cover closure, marker boundaries, foreign scope, prior-year
  inputs, source coverage and absence of raw YAML from the prompt. All 57 offline review-tool tests
  pass. The S3 preview now contains the complete person credit chain and i1040gi p.117/i1116 pp.1-2;
  avoiding false dependencies in input questions keeps it to about 101000 characters rather than
  378000. Five focused Flash and two Claude render reruns completed without transport/parser
  failures; objections are source-adjudicated with explicit scope/input limits. Prior requests are archived.
- **Tags:** incomplete-review-glossary; missing-review-sources; scope-resolution; caught-by-render-review

## BUG-0126 — Foreign-tax-credit citations omit the page defining regular tax

- **Date:** 2026-10-24
- **Caught by:** refreshed Schedule 3 and foreign-tax-credit render reviews after BUG-0125.
- **Symptom:** the supplied election instructions refer the reader to Line 20 for regular tax,
  but the prompt includes only i1116 pp. 1–2. Reviewers cannot verify the use of Form 1040 line 16.
- **Root cause:** ftc citations mention Line 20 while their page range selects only the election.
- **Where:** `forms/2025/ftc.yaml`, i1116 locators; five refusal citation expectations in stage4 fixtures.
- **Fix:** add p. 25, Line 20 to the locators and refresh both families' affected render reviews.
  Prior requests and results are preserved with hashes. No calculation or interview changes.
- **Scope:** p. 25 includes Schedule 2 line 1z and Form 4972/8978 adjustments. Those cases are
  screened by s2.other and scope.other_line16; their absence on supported completed returns is
  necessary for reducing regular tax to Form 1040 line 16. This is not a general identity.
- **Verification:** both families' ftc/s3 render reruns completed and the scope objections are
  adjudicated. The full fixture run passed 1060 cases and identified five citation-only differences;
  after updating just their expected locators, all five pass through the CLI. No input, amount,
  refusal gate or remedy changed. Default citations have zero findings; all fourteen item-2 receipts
  remain unchanged. The review server returns HTTP 200.
- **Tags:** missing-review-context; citation-selection; caught-by-render-review

## BUG-0127 — Optional human review still blocks unrelated validation

- **Date:** 2026-10-24
- **Caught by:** implementing the owner's revised integrity policy: remaining packets and the
  ten-ruling sample are optional; independent source and calculation checks carry the completion gate.
- **Symptom:** a saved MISMATCH, UNCLEAR, incomplete answer or stale receipt aborts the global log
  check and evidence report even though it supplies no human credit and may concern only presentation.
- **Root cause:** evidence eligibility and mandatory build validation share one problems list.
- **Where:** `tools/human_review/logs.py`, `check_logs.py`, evidence-report pending text.
- **Fix:** report ineligible optional readings as pending with no H credit; retain hard failures for
  malformed records, duplicate entries, invalid reader identity and incorrect committed authorship.
  Preserve the original owner verdicts and investigate their findings separately. A missing human
  reading cannot stand in for missing independent calculation evidence or excuse a confirmed defect.
- **Verification:** regression checks cover stale and negative verdicts producing a report without H,
  and structural/authorship errors remaining failures. The former logs, tool versions and fourteen
  current receipts are preserved with hashes before the policy change.
- **Tags:** optional-evidence; inappropriate-global-gate; owner-policy-revision

## BUG-0128 — Standard-deduction packet hides dollar units and chart derivation

- **Date:** 2026-10-24
- **Caught by:** the owner's completed item2 review: three MISMATCH verdicts and one UNCLEAR.
- **Symptom:** the packet shows $2000/$1600 per box beside a chart that prints total deductions,
  without explaining their derivation. The named "addition for one age or blindness box" can be
  read as a count, making separate money-times-count expressions look like count-times-count.
- **Root cause:** short reference labels omit units; the parameter question cites only the chart
  rather than showing both the base deduction and chart, and the final sum omits their connection.
- **Where:** `tools/human_review/steps.py`, the four standard-deduction presentation steps.
- **Fix:** label dollar increments and dollar additions explicitly; provide both base and chart
  excerpts for checking the increment; explain successive-row subtraction and the equivalence of
  separate age/blindness additions to a combined box count. No tax expression or amount changes.
- **Qualification:** the original verdicts remain unchanged. This is an engineering response to
  presentation findings, not a new owner MATCH, H/B assertion or required follow-up assignment.
- **Tags:** unclear-units; derived-value-presentation; source-alignment; caught-by-human-review

## BUG-0129 — Transcription comparison erases literal units

- **Date:** 2026-10-24
- **Caught by:** evaluating the actual refreshed dependent transcription while checking BUG-0111.
- **Symptom:** both reviewers omit `type: Count` from month-count constants. The project evaluator
  treats an untyped numeric literal as money, so a months comparison becomes unknown. Expander.ref
  removes the type annotation and can report AGREE for that invalid comparison.
- **Root cause:** constant normalization preserves only the value, while type checks are run on
  authored project data rather than the returned model IR. An abstract arithmetic match is mistaken
  for a typed transcription match.
- **Where:** `tools/transcription/transcribe.py`, Expander.ref and comparison normalization.
- **Reproduction:** compare Count months > {const:6,type:Count} with months > {const:6}; the current
  tool reports AGREE. `.transcription/constant-unit-erasure-witness.json` preserves the probe.
  The refreshed reviewers' h_lived_half also contains the untyped constant.
- **Status:** open. Preserve literal/parameter units consistently, validate model IR types, add a
  generic schema clarification, and re-audit existing agreements before family promotion. Retain raw
  responses and original comparison receipts; do not silently upgrade old judgments or treat this
  as a project tax-value error. Transcription readings remain outside the numeric scoreboard.
- **Tags:** false-agreement; unit-erasure; invalid-model-ir; caught-by-executable-review-witness

## BUG-0130 — Transcription grammar omits the Count-literal operand syntax

- **Date:** 2026-10-24
- **Caught by:** tracing BUG-0129's repeated untyped month-count constants back to the exact prompt.
- **Symptom:** the operand grammar lists money, Boolean and string constants, but never shows
  `{const: n, type: Count}`. Reviewers return untyped count thresholds; the runtime reads those
  numbers as money. The specification excerpt names Count, but the concise grammar omits its syntax.
- **Root cause:** the model-facing grammar was not extended alongside typed Count operands.
- **Where:** `tools/transcription/transcribe.py`, GRAMMAR.
- **Fix:** state the Count-literal syntax and that untyped numbers mean money cents. Keep this a
  generic schema clarification with no target computation, expected value or authored helper exposed.
  Bind future requests to the actual changed prompt; do not relabel old requests as having seen it.
- **Qualification:** invalid old model IR remains invalid, but the incomplete prompt is a project
  context defect too. Prior noise rulings must not be treated as clean model-only tests without this
  limitation. BUG-0129's qualification hold stays until typing and the prior-agreement audit close.
- **Tags:** incomplete-review-grammar; missing-count-syntax; caught-by-request-audit

## BUG-0131 — Transcription prompts truncate input meanings and scope conditions

- **Date:** 2026-10-25
- **Caught by:** tracing the refreshed dependent reviewers' shared relationship errors to the actual
  saved prompts during the expression-type audit.
- **Symptom:** the input question defines sibling_descendant as more distant relationships such as
  grandnieces, with listed nieces/nephews already included in sibling. Both prompts cut that question
  at 160 characters; neither contains grandniece or the later other/all-year-household explanation.
  Reviewers then misinterpret the enum and produce wrong dependency/ODC predicates.
- **Root cause:** three metadata emitters slice input descriptions at 160 characters and refusal
  questions at 220, treating essential category meanings and late exceptions as expendable prose.
- **Where:** `tools/transcription/transcribe.py`, build_prompt, reference_note and screen_notes.
- **Fix:** retain full supplied-input and refusal wording. It is interface/scope metadata, not an
  authored computation. Regression checks must show late enum meanings and scope conditions while
  still excluding computed labels/expressions. New calls bind the changed prompt; old receipts and
  rulings remain historical and are not relabeled as complete-context tests.
- **Qualification:** old model IR errors are real, but these source-interpretation disagreements
  also had incomplete project context. Do not treat the earlier rulings as clean model-only noise
  evidence. The transcription hold stays while validated fresh/recompared records are adjudicated.
- **Tags:** truncated-review-context; lost-enum-semantics; scope-omission; caught-by-request-audit

## BUG-0132 — Review dependency traversal omits newer operand positions

- **Date:** 2026-10-25
- **Caught by:** checking expression-type diagnostics against the transcription dependency walker.
- **Symptom:** the walker follows arithmetic amounts and comparison operands, but skips
  multiply_count's count, prorate's part/whole, keyed_lookup's keys and sum_over's field;
  round's scalar of reference is mistaken for an array and walked character by character.
  A model helper's type rejection in these positions does not reach the consuming line's
  comparison diagnostic. Refusal closure and shared-definition result discovery use the same walker.
- **Root cause:** new atoms were added without extending the old operand-position list.
- **Where:** `tools/transcription/transcribe.py`, operand_refs and its dependency/closure callers.
- **Fix:** walk the missing reference/operand positions, without treating parameter names, enum
  constants or definition result names as local line references. Regression checks cover every
  omitted position. The whole-form type-failure gate remains a separate protection.
- **Qualification:** this repairs diagnostic propagation, not source correctness. Prior comparisons
  still require verified replay or new requests; BUG-0129's hold remains.
- **Tags:** incomplete-dependency-walk; missed-type-diagnostic; refusal-closure

## BUG-0133 — Transcription prompts omit the available table interfaces

- **Date:** 2026-10-25
- **Caught by:** tracing the expression audit's unresolved pub946/macrs table references to the prompt.
- **Symptom:** the generic grammar offers keyed_lookup and rate_lookup, but the request supplies
  no catalog of table ids, ordered key types or result types. Saved model replies invent table ids
  that the host cannot resolve, including pub946.macrs variants instead of the declared interfaces.
- **Root cause:** line and parameter interfaces were listed, while table interfaces were omitted.
- **Where:** `tools/transcription/transcribe.py`, build_prompt and its interface catalog.
- **Fix:** supply table ids, kinds, public titles, key types and result types, without table cells,
  authored formulas or expected results. Supply the generic expression schema and clarify nested
  Boolean tests and collection binding rules. New requests retain their exact changed prompt hashes;
  old requests are not relabeled or treated as complete-context tests of the new grammar.
- **Qualification:** invalid earlier model IR remains invalid, but a missing table interface is
  also a project context defect. Do not use those records as clean model-only noise evidence.
  BUG-0129's transcription qualification hold remains during replacement and adjudication.
- **Tags:** missing-table-interface; incomplete-review-context; invalid-model-ir

## BUG-0134 — Complete question wording does not declare conditional input availability

- **Date:** 2026-10-25
- **Caught by:** both fresh dependent reviewers requiring dc_under13 for every child, after syntax repair.
- **Symptom:** the request supplies full typed input questions but does not say which answers the
  guided path may omit because age already determines the fact. The returned care predicates read
  dc_under13 for all ages and dc_over12_care for every disabled person. The real interface asks
  those timing questions only at age13; stage15.f2441.s1 has a four-year-old with care expenses
  and no dc_under13 answer. An unconditional reference cannot replace that guided computation.
- **Root cause:** prompt completeness currently checks question text only, not input availability.
  The source-only reviewer sees an input catalog without the guided path's availability contract.
- **Where:** `tools/transcription/transcribe.py`, input metadata/completeness; dependent review contract.
- **Status:** open, T-063. Establish a non-leading availability contract or source-only supplemental
  fact cases, preserve request provenance, and verify younger/age13/older paths before replacing
  the current care predicates. Do not expose authored formulas as hints or fix replies in place.
- **Qualification:** this is a review-context gap, not a newly demonstrated project tax-value bug.
  Current complete-input-context-v1 means complete question wording, not a complete availability
  contract. Do not count these care disagreements as clean model-only noise or clear the global
  transcription hold merely because the reply has valid expression types.
- **Tags:** conditional-input-contract; incomplete-review-context; unknown-value-propagation

## BUG-0135 — Source-only reviewers must guess the meaning of internal adapter helpers

- **Date:** 2026-10-25
- **Caught by:** both fresh dividend replies explicitly noting that the IRS text does not define div.screen.
- **Symptom:** the required NonNegDollars export is an internal zero-after-scope-checks adapter,
  used by other worksheets for excluded source amounts. The blind request gives its id and type,
  but no source-defined meaning. Both reviewers invent a sum of special distributions and say
  the interface is not defined in the IRS pages. Such a sum is not the project's adapter contract.
- **Root cause:** the exported-helper target list treats an internal adapter as if it were an IRS
  quantity whose meaning can be reconstructed independently from the pages.
- **Where:** `tools/transcription/transcribe.py`, exported helper interfaces; div.screen.
- **Status:** open, T-064. Separate source-defined quantities from implementation adapters and
  define/check adapter contracts without counting supplied adapter behavior as blind tax evidence.
  An explicit interface-gap adjudication now blocks qualification and earns no model-noise credit.
- **Qualification:** this is a review-contract defect, not a newly established project tax-value
  error. Do not force the reply into equivalence or count an unprovided contract as clean model-only
  noise. The global transcription qualification hold remains.
- **Tags:** opaque-helper-interface; blind-review-context; unsupported-evidence-claim

## BUG-0136 — Draft partial-input negative cases inherit contradictory qualified expenses

- **Date:** 2026-10-25
- **Caught by:** checking the draft P06/P08 source facts after the first two model runs.
- **Symptom:** the draft bank's common base assigns $1,000 of qualified expenses to all cases,
  including a non-disabled age14 child and an age13 child with no pre-birthday care. The negative
  cases cannot have current-year qualified care expenses under those stated facts.
- **Root cause:** hand-constructed negative records override eligibility facts but inherit the
  positive case's money amount and active-care answer.
- **Where:** `tools/transcription/input_contracts/2025/dependent.json`, P06 and P08.
- **Fix:** give those two no-care records zero qualified expenses and care=false, add a fact-only
  coherence regression, archive the draft bank and actual model requests/replies/logs with hashes,
  and issue fresh requests with the corrected facts. Do not relabel draft results as corrected runs.
- **Qualification:** a benchmark-context defect, not a project tax-value finding. Expected Boolean
  outputs are unchanged; the correction makes the supporting input facts coherent.
- **Tags:** contradictory-test-facts; inherited-positive-input; draft-benchmark-context

## BUG-0137 — Review tests race compilation in a clean-output full check

- **Date:** 2026-10-25
- **Caught by:** tracing the new review tools' imports of engine/dist during the full-check first wave.
- **Symptom:** check-all starts review_tools in parallel with a build function that first compiles
  the evaluator. The review tests require the compiled checker/atom catalog, so a checkout without
  engine/dist can fail before compilation finishes. Existing compiled output masks the dependency.
- **Root cause:** compilation is hidden inside the parallel build/render step rather than declared
  as a prerequisite of all dist-dependent validation tools.
- **Where:** `tools/check_all_steps.sh`, build_and_render and wave scheduling.
- **Fix:** run compilation as a completed first step, then start the source/review/build wave;
  remove redundant compilation from build_and_render. Validate with compiled output initially
  absent, keeping the previous output as a reversible temporary backup.
- **Tags:** build-order-race; clean-output-reproducibility; validation-tool-dependency

### BUG-0135 engineering resolution — 2026-10-25

The identified div.screen adapter now has a host-only engineering contract with 21 cases,
checking zero/refusal/unknown behavior and all 16 direct worksheet copies. It is omitted from
blind targets and explicitly excluded from source agreement/noise denominators. An adapter-only
document produces no new model request or source assertion. Original dividend replies and
interface-gap rulings are preserved; no forced equivalence or evidence credit. See T-064 and
`tools/transcription/adapter_contracts/README.md`. The fresh f4952 reply identifies another target
meaning gap (the full line4g election versus its net-capital-gain share); that remains unresolved.

## BUG-0138 — HSA zero-distribution rollover line demands an inapplicable follow-up

- **Date:** 2026-10-25
- **Caught by:** a source-fact diagnostic of the fresh f8889 transcriptions, also run against the project.
- **Symptom:** with total HSA distributions zero and no rollover answer, f8889.line14b is unknown
  rather than zero. Its expression has a zero branch, but the rollover_bad refusal gate first
  demands the absent rollover answer. Downstream lines15/16/17b independently return zero; this
  witness does not establish an incorrect final tax liability.
- **Source:** i8889 p.8 lines14b/15 and f8889 p.1 Part II describe only amounts included in actual
  distributions; none can be rolled over when total distributions are zero.
- **Witness:** one confirmed person/HSA entry, status=single, f8889.unsupported=false,
  f8889.line14a=0, with rollover/medical/line17a unanswered. The fixed interpreter observes
  unknown(input=rollover) on project line14b, and zero on project lines15/16/17b. Fresh Claude
  demands missing follow-ups on all four; Flash has invalid IR and is not evaluated. Saved
  diagnostic: `.transcription/hsa-zero-distribution-source-witness.json`; current audit report
  records the minimal keyed inputs and result. This case was not in either actual model request.
- **Root cause:** the consistency refusal is evaluated before a branch that makes its question
  unnecessary. Complete question wording does not specify conditional answer availability.
- **Where:** `forms/2025/f8889.yaml`, f8889.rollover_bad and line14b.
- **Status:** open, T-065. Correct the conditional consistency check while retaining rejection of
  contradictory supplied values; add source-based regressions and refresh affected T/R/M receipts.
  No authored HSA rule or numeric fixture is changed in this batch. Keep source qualification held.
- **Tags:** unconditional-consistency-gate; inapplicable-followup; unknown-value-propagation

### BUG-0138 resolution — 2026-10-25

The rollover refusal now explicitly checks supplied figures with when_known=true. A true check
still refuses, a refused gate still propagates, and a missing actual amount stays unknown; only
an unanswered consistency check can be left unperformed when the expression independently knows
the result. TypeScript and Lean share the rule, and a derivation note records it. Its temporary
question dependencies are discarded, so another unanswered question cannot resurrect an irrelevant
rollover prompt. Seventeen source cases include zero/positive distributions, contradictory amounts,
genuine unknowns, mandatory screens and spouse-attributed coverage. Eight source-derived numeric
fixtures and a dedicated mutation protect the regression. This is not a false/zero input default.

## BUG-0139 — Model refusal declarations were outside the type-only validation boundary

- **Date:** 2026-10-25
- **Caught by:** adding the supplied-figure consistency mode to the model IR boundary.
- **Symptom:** ordinary expression validation checked expr but did not validate every refusal
  declaration or prove every declared gate Bool. The earlier finite-case runner checked its own
  gates, but a form without a case bank could report a type pass with malformed or non-Bool gates.
- **Root cause:** refusal lists live outside the expression JSON schema and the public expression
  checker only walks expressions.
- **Where:** tools/transcription/model_candidate.mjs, check_model_types.mjs and check_input_contracts.mjs.
- **Fix:** validate list/object syntax and when_known=true, then check synthetic Bool comparisons
  for every declared gate, including unused helpers, using the same host type checker. No gate is
  executed by the type-only checker. Candidate gate flags are preserved by the bounded interpreter.
- **Qualification:** old type passes are not upgraded or retained blindly; the read-only audit
  rechecks actual saved replies, and the global source-qualification hold remains.
- **Tags:** unchecked-refusal-ir; schema-boundary; incomplete-type-validation

## BUG-0140 — A draft source case prescribes placement of the project scope screen

- **Date:** 2026-10-25
- **Caught by:** the first new Claude reply passing fourteen HSA cases and conservatively requiring
  the unanswered scope screen before intermediate rollover amounts in H12.
- **Symptom:** H12 demanded zero intermediate lines14b/14c despite an unanswered project scope
  screen. The IRS pages do not dictate where a client must apply that screen; this tested the
  project's placement rather than an independently determined source quantity.
- **Root cause:** a benchmark case mixed a real final-output availability requirement with an
  implementation-specific intermediate requirement.
- **Where:** tools/transcription/input_contracts/2025/f8889.json, draft H12.
- **Fix:** require unknown final lines16/17b only. Preserve the draft bank, requests, replies,
  logs and diagnostic (12 files) under .transcription/archive/hsa-before-scope-case-correction-2026-10-25/.
  Issue actual fresh requests. Later spouse cases extend the bank to seventeen; neither earlier
  fifteen-case request is relabeled as having seen the current bank.
- **Tags:** benchmark-overconstraint; scope-placement; source-independence

## BUG-0141 — HSA review metadata and December question omit spouse-attributed coverage

- **Date:** 2026-10-25
- **Caught by:** the new Claude rendering review of Form8889 line3.
- **Symptom:** form input metadata asks only about the person's own family HDHP. The live month-count
  question already clarifies spouse coverage through a bank override, but independent reviewers see
  the narrower form metadata. The derived December question also lacks the spouse-attribution rule.
- **Source:** i8889 p.4 How To Complete Part I and Line3 rule1: when both spouses are eligible and
  either has a family HDHP, both are treated as family-covered and self-only plans are disregarded.
- **Root cause:** a correct interview-only clarification was not propagated to the shared input
  contract, and the December variant had no equivalent clarification.
- **Fix:** align the form metadata and December input, derive the interview wording from them and
  remove the duplicate override. Clarify actual monthly counts versus the separate last-month
  election. Two source cases check common-family coverage with one or two HSAs; refresh T/R/M
  receipts without changing the existing owner-approved last-month/catchup interpretations.
- **Tags:** divergent-input-wording; spouse-attributed-coverage; review-context-gap

## BUG-0142 — Generated spouse HSA coverage counts need not share a possible calendar

- **Date:** 2026-10-25
- **Caught by:** reviewing the regenerated worked-case facts after the spouse-coverage finding.
- **Symptom:** a spouse eligible nine months has nine family months while the spouse eligible all
  twelve months has only three family months. With both eligible during those nine months, both
  must receive family-coverage treatment; the supplied aggregate counts cannot describe that return.
- **Root cause:** each spouse's counts are individually valid but drawn independently without
  constructing the monthly joint coverage facts.
- **Where:** engine/src/generate.ts; generated HSA cases used by properties/Lean/class-M selection.
- **Fix:** construct eligible and family-coverage month calendars, attribute a family-covered month
  to each eligible spouse, then derive the counts and December answers. Tests cover all count pairs
  and the nine-versus-three witness. The sampler uses eligible periods that include December;
  this is a sampling limitation, not a restriction on authored forms or source cases.
- **Provenance:** pre-calendar worked requests/logs/fixtures and job facts (33 files) are hashed in
  .transcription/archive/hsa-before-monthly-calendars-2026-10-25/. New reviews use new calendar-derived
  facts and their actual requests; no inconsistent old result is migrated into a new assertion.
- **Tags:** impossible-generated-facts; coupled-spouse-coverage; benchmark-coherence

## BUG-0143 — Worked-case context includes redundant calculations from the reviewed form

- **Date:** 2026-10-26
- **Caught by:** inspecting the HSA printed-output request after removing ambiguous helper targets.
- **Symptom:** the incoming-value catalog tells the reviewer the household's Step1 sum, share sum
  and split count as authoritative givens. These come from the HSA calculation itself and are
  used by implementation validation, not needed by the printed IRS calculation.
- **Root cause:** the job context scans every computed helper instead of following the requested
  printed calculation through its local expression dependencies.
- **Where:** engine/src/classm.ts, buildCollectionJob and the incoming-value catalog.
- **Fix:** preserve full candidate/branch validation, but filter incoming givens to the dependency
  closure of printed output expressions and their local helpers. Raw marital/roster facts remain;
  validation-only derived totals are withheld. Add a request-content regression. This is not a
  claim that every feedback or pass-through boundary in legacy worked reviews has been audited.
- **Related gap:** the first printed HSA set has only zero distributions. Strengthen four source
  fixtures with complete, ordinary PartI facts so positive PartII calculations can seed worked
  cases. Selection grows from four cases/87 branches to five/97 with no lost branch. Regenerate
  both families' actual requests; prior 90-output replies are historical, not relabeled.
- **Provenance:** 34 prior files are hashed under
  .transcription/archive/hsa-before-positive-printed-cases-2026-10-25/.
- **Tags:** worked-context-feedback; validation-only-givens; zero-only-regime

## BUG-0144 — Expanded refusal validation kept the old type-policy identifier

- **Date:** 2026-10-26
- **Caught by:** tracing the saved-review freshness boundary during T-062 migration.
- **Symptom:** BUG-0139 added refusal syntax and Bool-gate validation, but new and old logs
  both used project-expression-types-v1. The identifier alone could not distinguish a pass
  that included refusal checks from one that did not. Four older passes fail those checks.
- **Root cause:** the host validator changed without versioning its recorded contract.
- **Where:** tools/transcription/check_model_types.mjs and transcribe.py.
- **Fix:** use project-expression-types-v2, preserve original policy identifiers in read-only
  audits, and recheck actual bound requests/replies when assessing new interface-context records.
  Historical headers and raw replies are not rewritten or silently promoted.
- **Impact:** the global BUG-0129 source-qualification hold already prevented these old
  records from earning source qualification. That hold remains until migration closes.
- **Tags:** unversioned-validation-contract; stale-type-pass; review-provenance

## BUG-0145 — Published input stubs import authored computed refusal gates into model validation

- **Date:** 2026-10-26
- **Caught by:** both fresh asset transcriptions rejected for missing asset.screened, and the
  fresh person transcription rejected for missing person.plan_screened, during T-062 replacement.
- **Symptom:** these errors come from original input declarations, not the returned model IR.
  The model was required to reproduce an undisclosed authored helper to pass the new gate checks.
  An authored collection-valued input gate similarly rejected the new Schedule 8812 replies.
- **Root cause:** prepareCandidate reused whole authored input records, including their computed
  refuses metadata, while replacing the authored computed lines with independently supplied ones.
- **Where:** tools/transcription/model_candidate.mjs, also consumed by the bounded case interpreter.
- **Fix:** retain only published input identity/type/question metadata. Input refusal declarations,
  if the model explicitly returns any, come from that reply and are validated with the model's
  own computed gates. Never borrow an authored refusal placement or helper. Version this checker
  contract separately; preserve earlier logs and actual requests as checked at the time.
- **Validation:** source-interface-only candidates must not require an absent authored helper;
  a malformed or non-Bool gate explicitly returned on an input must still fail. Passing types
  remains distinct from source correctness and partial-input behavior; the global hold remains.
- **Tags:** authored-logic-contamination; false-type-rejection; hidden-helper-dependency

## BUG-0146 — Transcription targets omit computed helpers used only as foreign refusal gates

- **Date:** 2026-10-26
- **Caught by:** checking the household candidate's published interface against existing head-of-household fixtures.
- **Symptom:** household.hoh_fails controls the Form1040 deduction refusal but was not a required
  source-transcription target. exported_lines scanned only other lines' expressions, ignoring
  their refusal declarations. The same gap affects twelve helpers across household, ira, s1,
  s179 and s3, including some project scope bridges that need explicit semantic classification.
- **Root cause:** dependency discovery treated arithmetic operands as the entire cross-form interface.
- **Where:** tools/transcription/transcribe.py exported_lines and compare_families.py target coverage.
- **Fix:** include direct foreign refusal and visibility references. Compare both logs against the
  live required-target inventory, not only each other's rows: a changed review target list must
  not qualify old logs merely because their authored-form subjects are unchanged. Preserve old
  requests; newly required targets need actual source requests or explicit verified assessment,
  not fabricated historical coverage. Internal adapters remain separately declared and tested.
- **Impact:** this is an independent source-review coverage gap, not proof the household result
  itself is wrong. The global transcription hold prevents source promotion while it is repaired.
- **Tags:** missing-refusal-dependency; unreviewed-household-predicate; incomplete-source-targets

## BUG-0147 — Schedule 1-A business-tips screen is unreachable without employee tips

- **Date:** 2026-10-26
- **Caught by:** source adjudication of the Claude Schedule 1-A transcription (plan revision item A,
  `reviews/2025/transcription/adjudication/s1a.md`): the candidate refused at `s1.sc_1a` where the
  project completed the return; reproduced on generated return 20261026/369 with
  `sc[biz_a].tips_ot` true under the full interview's targets.
- **Symptom:** a filer whose only qualified tips (or qualified overtime on Form 1099-NEC/MISC) come
  from a Schedule C business was never asked `sc.tips_ot`; Schedule 1-A lines 5, 13, 14b and 21 and
  Form 1040 line 13b were $0 and the return completed, instead of being refused.
- **Root cause:** the `s1.sc_1a` refusal sat only on the helpers `s1a.line5_calc` and
  `s1a.line14b_calc`, evaluated only under `s1a.part2`/`s1a.part3`, which require the employee-only
  questions `s1a.tips`/`s1a.overtime`. i1040gi p. 101 makes Parts II and III apply to anyone who
  received qualified tips or overtime, including in a trade or business (p. 104, line 5; p. 108,
  line 14b). The regression `stage14.refuse.sch1a_tips` asserted the refusal on the helper, which
  fixture checks evaluate but the interview does not.
- **Where:** `forms/2025/s1a.yaml`, lines `s1a.line13` and `s1a.line21`.
- **Fix:** the `s1.sc_1a` refusal is also declared on lines 13 and 21, which every return reaches
  through Form 1040 line 13b, so the screen is asked of every Schedule C. Regression
  `stage14.refuse.sch1a_tips_business_only` asserts the refusal on lines 13 and 21 and Form 1040
  line 37; `stage16.cleanup.mut.clwb_three_figured` now answers the screen it had never been asked.
  New check-all step `refusal_reach` (`tools/check_refusal_reach.mjs`) requires every refusal
  fixture's return to be refused under the full interview, so this class is caught mechanically.
- **Tags:** unreachable-refusal; helper-only-gate; fixture-evaluates-helpers; caught-by-source-adjudication

## BUG-0148 — A section 179 election above the dollar limitation was accepted and lost from basis

- **Date:** 2026-10-26
- **Caught by:** source adjudication of the Form 4562 Part I transcriptions (plan revision item A,
  `reviews/2025/transcription/adjudication/s179.md`), on witnesses built from
  `stage14.s179.dollar_limit` and evaluated under the full interview's targets.
- **Symptom:** an election above line 5 was accepted. Line 9 limited the deduction, but
  `asset.after179` reduced the asset's basis by the whole election, so the excess was neither
  deducted, carried over nor depreciated ($3,000,000 elected against $2,500,000 lost $71,450 of 2025
  MACRS). With line 5 zero, lines 6(c) and 8 printed the election and depreciation was $142,900 short.
- **Root cause:** the project bounded each asset's election by its business cost only. i4562 p. 4,
  Line 3: "The amount of section 179 property for which you can make the election is limited to the
  maximum dollar amount on line 1"; p. 5, Line 5: "If line 5 is zero, you cannot elect to expense any
  section 179 property".
- **Where:** `forms/2025/s179.yaml`.
- **Fix:** new gate `s179.over_limit` (line 8 more than line 5) refuses on line 9, asking the filer
  to elect no more than the limitation; the basis arithmetic is then correct on every computed
  return. Capping and allocating the election instead would need an allocation the text leaves to
  the taxpayer. `stage14.s179.dollar_limit` and `stage14.s179.phase_down` now elect exactly the
  limitation; regressions `stage14.s179.refuse_over_limit` and `stage14.s179.refuse_zero_limit`.
- **Tags:** missing-limit-gate; basis-reduced-by-unallowed-amount; fixture-asserted-limited-line-only; caught-by-source-adjudication

## BUG-0149 — Schedule D lines 18 and 19 kept worksheet results when line 17 is No

- **Date:** 2026-10-26
- **Caught by:** source adjudication of the Claude Schedule D transcription (plan revision item A,
  `reviews/2025/transcription/adjudication/sd.md`); triage witnesses generated 20261026/76 ($4,391.65)
  and `classm.sli.2` ($145).
- **Symptom:** `sd.line18` and `sd.line19` copied the 28% and section 1250 worksheet results whatever
  line 17 said. On the Form 4952 branch of `f1040.gate.sdtw`, which does not test line 17, the
  Schedule D Tax Worksheet read them: line 11 showed $500 where the source gives zero, and lines it
  skips showed amounts. No tax change was found (worksheet line 9 is zero when line 17 is No).
- **Root cause:** f1040sd p. 2, line 17: "No. Skip lines 18 through 21, and go to line 22";
  i1040sd p. 11 completes the worksheets for lines 18 and 19 only "If you checked “Yes” on line 17".
  Both lines were plain copies; their labels still described the worksheets as deferred.
- **Where:** `forms/2025/sd.yaml`.
- **Fix:** both lines choose zero when line 17 is No. Regressions `stage16.sd.line17_no_skips_18`
  and `stage16.sd.line17_no_skips_19`.
- **Tags:** missing-skip-guard; unguarded-copy; stale-label; caught-by-source-adjudication

## BUG-0150 — Schedule D Tax Worksheet lines 41 to 43 were shown when Schedule D line 18 is zero

- **Date:** 2026-10-26
- **Caught by:** source adjudication of the Schedule D Tax Worksheet transcriptions (`adjudication/sdtw.md`);
  309 triage witnesses, 12 on returns that use the worksheet (`sales.select.sdtw.election`, $50,000).
- **Symptom:** with Schedule D lines 18 and 19 both zero, `sdtw.use28` completed line 41 (equal to
  line 1) on the values sheet; lines 42 and 43 were zero and line 47 unchanged.
- **Root cause:** the "go to line 41" after line 34 was read as passing the instruction printed before
  line 41, i1040sd p. 16: "If Schedule D, line 18, is zero or blank, skip lines 41 through 43".
- **Where:** `forms/2025/sdtw.yaml`.
- **Fix:** under the owner's decision of 2026-10-26 (skipped lines are hidden, values unchanged),
  lines 41 to 43 carry `shown_when: sdtw.show41_43` (Schedule D line 18 more than zero). Regression:
  `sales.select.sdtw.election` asserts the condition false.
- **Tags:** skipped-line-shown; flow-instruction-misread; caught-by-source-adjudication

## BUG-0151 — Schedule 8812 lines after a stop, and Part II-B when skipped, were shown

- **Date:** 2026-10-26
- **Caught by:** source adjudication of the Schedule 8812 transcriptions (`adjudication/s8812.md`).
- **Symptom:** every line was shown whatever the stops said: line 13 after the line 12 stop
  (`stage8.single.taxpayer_without_tin`, $17,867); lines 16b to 21 after line 16a was zero
  (`stage8.hoh.child.ctc`: 16b $1,700, 18a $120,000, 19 $117,500, 21 $9,180); Part II-B when the
  instruction after line 20 skips it. Schedule 8812 is attached to the return, so these amounts
  reached a filed form. Lines 14, 17 and 27 were right.
- **Root cause:** f1040s8812 stops ("No. Stop here", line 12; "If zero, stop here", lines 16a and
  16b) and the "Next" routing after line 20 were applied only where line 27 chooses its source.
- **Where:** `forms/2025/s8812.yaml`.
- **Fix:** printed lines 13, 16b, 17 to 20 and 21 to 26 carry `shown_when` on new conditions
  `s8812.show13`, `show16b`, `show_iia` and `show_iib` (owner's decision of 2026-10-26; values
  unchanged). Regressions on `stage8.hoh.child.ctc`, `stage8.single.taxpayer_without_tin` and
  `stage8.hoh.actc.one_child.low_wages`. Credit Limit Worksheets A and B, also evaluated when not to be
  completed (i1040s8812 p. 4), are helper lines, which `shown_when` cannot hide; that part is T-067.
- **Tags:** skipped-line-shown; stop-instruction-ignored; filed-form-presentation; caught-by-source-adjudication

## BUG-0152 — EIC Worksheet A was shown after a STOP, and line 5 when skipped or left blank

- **Date:** 2026-10-26
- **Caught by:** source adjudication of the EIC transcriptions (`adjudication/eic.md`).
- **Symptom:** Worksheet A lines appeared on returns the flowchart had already stopped (generated
  20261026/439: line 6 $3,545 with `eic.credit` $0), and line 5 showed a table lookup when line 4 is
  Yes or line 5 is to be left blank (`classm.f2441.4`, $1,709). Form 1040 line 27a was right.
- **Root cause:** i1040gi p. 43 reaches Worksheet A only after Steps 1 to 5, each "STOP You can't take
  the credit" ending the flowchart; p. 46, line 4: "Yes. Skip line 5"; line 5: "Yes. Leave line 5
  blank". Only `eic.credit` and `eic.line6` respected them.
- **Where:** `forms/2025/eic.yaml`.
- **Fix:** printed lines 1, 2, 3 and 6 are shown when `eic.eligible`; line 5 when the new
  `eic.show5` holds (owner's decisions of 2026-10-26: hidden, values unchanged, and a worksheet after
  a STOP counts as skipped). Regressions: `stage16.cleanup.mut.clwb_three_figured` asserts
  `eic.eligible` false; `stage9.eic.line5_skipped` asserts line 4 Yes and `eic.show5` false.
- **Tags:** skipped-line-shown; stop-instruction-ignored; caught-by-source-adjudication

## BUG-0153 — Head of household refused when a relative qualifying person was born or died in 2025

- **Date:** 2026-10-26
- **Caught by:** source adjudication of the household transcriptions (`adjudication/household.md`),
  reading `dependent.hoh_test1`/`hoh_test2` (never source-reviewed, BUG-0146) against p501; witness
  built from `stage8.hoh.parent.test1`.
- **Symptom:** a filer whose dependent parent or other relative (not a qualifying child) died or was
  born in 2025 and lived with them more than half of the part of the year they were alive was
  refused head of household, because the months question tells them to enter 0 unless the person
  lived with them the whole time; and the Test 1 question asked about the parent's home "for all of
  2025". Line 12e was refused where the source gives $23,625.
- **Root cause:** i1040gi p. 15 sends this case to Pub. 501; p501 p. 9, Death or birth: "Your
  qualifying child or qualifying relative who lived with you for more than half the part of the year
  they were alive" and "Your parent for whom you paid, for the entire part of the year your parent
  was alive, more than half the cost of keeping up the home your parent lived in". The months answer
  encodes the all-year rule a household member needs (i1040gi p. 21), which also feeds the dependent
  care residency test, so it could not carry the part-year rule.
- **Where:** `forms/2025/dependent.yaml`; interview question lists.
- **Fix:** owner's choice (2026-10-26): new questions `dependent.born_died` and
  `dependent.hoh_part_year`, read only by head of household Test 2 through `dependent.hoh_lived_half`
  for a relative who is not a qualifying child (whose months already count the part of the year
  alive); `dependent.parent_home_paid` now asks about the part of 2025 a parent who died was alive.
  Test 2 checks relationship before residency so excluded household members are not asked. Three
  fixtures answer the new question (no birth or death); regressions
  `stage8.hoh.parent.died_lived_part_year` and `stage8.hoh.parent.died_not_half`.
- **Tags:** part-year-rule-missing; question-encodes-wrong-test; unreviewed-household-predicate; caught-by-source-adjudication

## BUG-0154 — The BUG-0147 refusal named business tips for a filer with only Form 1099 overtime

- **Date:** 2026-10-26
- **Caught by:** round 2 source adjudication of Schedule 1-A (`adjudication/s1a.md`), on
  `stage14.sch1a.refuse_overtime_1099`.
- **Symptom:** a filer whose only screened item was qualified overtime on Form 1099-NEC or 1099-MISC was
  refused with the line 13 message about qualified tips received in a trade or business; the return was
  correctly refused.
- **Root cause:** BUG-0147 put the shared gate `s1.sc_1a` on lines 13 and 21 with each line's own text;
  line 13 is evaluated first, so its tips wording reached every refused filer.
- **Where:** `forms/2025/s1a.yaml`, the `s1.sc_1a` refusals on `s1a.line13` and `s1a.line21`.
- **Fix:** both refusals carry one text naming qualified tips received in a trade or business and
  qualified overtime on Form 1099-NEC or 1099-MISC. `stage14.refuse.sch1a_tips_business_only`
  re-recorded with that text.
- **Tags:** refusal-message-wrong; introduced-by-fix; caught-by-source-adjudication

## BUG-0155 — Form 4562 line 10 was shown when line 5 is zero

- **Date:** 2026-10-26
- **Caught by:** round 2 source adjudication of Form 4562 Part I (`adjudication/s179.md`).
- **Symptom:** with line 5 zero, the 2024 carryover appeared on line 10, which the instructions skip;
  lines 12 and 13 were right.
- **Root cause:** i4562 p. 5, Line 5: "If line 5 is zero, you cannot elect to expense any section 179
  property. In this case, skip lines 6 through 11, enter zero on line 12, and enter the carryover ... on
  line 13"; line 10 is the filer's input and had no condition.
- **Where:** `forms/2025/s179.yaml`.
- **Fix:** line 10 carries `shown_when: s179.show10` (line 5 more than zero), values unchanged (owner's
  decision of 2026-10-26). Regression `stage14.s179.zero_limit_carryover`.
- **Tags:** skipped-line-shown; caught-by-source-adjudication

## BUG-0156 — EIC worksheet lines were shown after later STOPs and on unreached worksheets

- **Date:** 2026-10-26
- **Caught by:** round 2 source adjudication of the EIC (`adjudication/eic.md`), gaps left by BUG-0152.
- **Symptom:** Worksheet A lines 3 and 5 appeared after "If line 2 is zero, STOP" (and the Worksheet B
  STOPs that make line 2 zero) (`stage9.eic.no_earned_income`, line 3 $1,000); Worksheet B lines 4b and 6
  appeared for filers who never reach Step 5 or after the Worksheet B line 5 STOP
  (`classm.f2441.2.deepseek`, $85,000; `stage14.eic.wsb_line5_stop_27c`, $19,516.40). The `eic.credit`
  label named only Worksheet A. Form 1040 lines 27a and 27c were right.
- **Root cause:** i1040gi p. 46, line 2: "If line 2 is zero, You can’t take the credit" (a STOP); p. 47:
  "Use this worksheet if you answered “Yes” to Step 5, question 2" and line 5, "No. You can’t take the credit". BUG-0152 tested
  only `eic.eligible`.
- **Where:** `forms/2025/eic.yaml`.
- **Fix:** line 3 is shown on `eic.show3` (eligible and line 2 more than zero), and `eic.show5` also
  requires line 2 more than zero; Worksheet B line 4b on `eic.show_wsb4b` (Step 5 reached, new
  `eic.reached_step5`, and self-employed) and line 6 on `eic.show_wsb6`. `eic.credit` relabelled. The
  Step 5 earned-income lines are helpers, which `shown_when` cannot hide (T-067). Regressions on
  `stage9.eic.no_earned_income`, `stage14.eic.wsb_line5_stop_27c` and `stage9.eic.wsb_not_reached`.
- **Tags:** skipped-line-shown; stop-instruction-ignored; incomplete-fix; caught-by-source-adjudication

## BUG-0157 — Form 2441 refused the death-year rule for a disabled qualifying person

- **Date:** 2026-10-26
- **Caught by:** round 2 source adjudication of the dependents collection (`adjudication/dependent.md`),
  checking BUG-0153's reach.
- **Symptom:** a disabled dependent who died in 2025 and lived with the filer more than half of the part
  of the year they were alive was not a qualifying person, because the months question encodes the
  all-year rule; the credit was $0 where the source gives $600 on the regression's facts.
- **Root cause:** p503 p. 3: "a person who was born or died in 2025 is treated as having lived with you
  for more than half of 2025 if your home was the person's home more than half the time they were alive
  in 2025"; `dependent.dc_disabled_qp` read `dependent.lived_half`.
- **Where:** `forms/2025/dependent.yaml`.
- **Fix:** `dependent.dc_disabled_qp` reads the new `dependent.dc_lived_half` (lived half the year, or a
  person other than a qualifying child born or who died in 2025 whose home was the filer's for more than
  half the part of the year alive), after the inability-to-care test so others are not asked. The
  qualifying-child route already counts part years through months. Regression
  `stage15.f2441.parent_died_part_year`.
- **Tags:** part-year-rule-missing; question-encodes-wrong-test; caught-by-source-adjudication

## BUG-0158 — Head of household refused the adoption and placement part-year rule

- **Date:** 2026-10-26
- **Caught by:** round 2 source adjudication of the dependents collection, checking BUG-0153.
- **Symptom:** a relative other than a qualifying child adopted by, or placed with, the filer in 2025 who
  lived with them more than half of the time since was not a Test 2 person, so head of household was
  refused. BUG-0153's new question also left juvenile detention out of the temporary absences.
- **Root cause:** i1040gi p. 15: "the person is considered to have lived with you for more than half of
  2025 if your main home was this person's main home for more than half the time since the person was
  adopted or placed with you in 2025"; pp. 14–15 list "detention in a juvenile facility" among temporary
  absences. BUG-0153 covered only birth and death.
- **Where:** `forms/2025/dependent.yaml`; interview question lists.
- **Fix:** new question `dependent.placed`; `dependent.hoh_part_year` becomes `dependent.part_year_home`,
  worded for the part of the year alive or since the adoption or placement, with juvenile detention
  among the absences; `dependent.hoh_lived_half` accepts birth, death or placement. Form 2441 uses birth
  or death only (p503 p. 3 states no placement rule). Three fixtures answer `placed`; regression
  `stage8.hoh.adopted_part_year`.
- **Tags:** part-year-rule-missing; incomplete-fix; caught-by-source-adjudication

## BUG-0159 — Form 1040 line 25b sent Form SSA-1099 and RRB-1099 withholding to box 4

- **Date:** 2026-10-26
- **Caught by:** round 2 source adjudication of the Form 1040 render comparison (`adjudication/f1040.md`).
- **Symptom:** the line 25b question and help said to read box 4 on each Form 1099. On Form SSA-1099 box 4
  is benefits repaid; a filer following the question would enter the wrong amount and line 25d, line 33
  and the refund or amount owed would be wrong by the withholding.
- **Root cause:** i1040gi p. 39, Line 25b: "This should be shown in box 4 of Form 1099, box 6, of Form
  SSA-1099, or box 10 of Form RRB-1099."
- **Where:** `forms/2025/f1040.yaml` (`f1040.line25b`), `interview/questions-2025.yaml`.
- **Fix:** the question and help name box 4 of Forms 1099, box 6 of Form SSA-1099 and box 10 of Form
  RRB-1099, citing p. 39. The line is a supplied total, so no computed value changes.
- **Tags:** question-wording-wrong-box; amount-affecting-input; caught-by-render-adjudication

## BUG-0160 — Schedule D Tax Worksheet line 4 copied Form 4952 line 4e with no Form 4952 (closes BUG-0099)

- **Date:** 2026-10-26
- **Caught by:** recorded as BUG-0099 (OpenTaxSolver differential); found again by round 2 source
  adjudication of the worksheet (`adjudication/sdtw.md`, `classm.tcw.1`: $16,981 against $0).
- **Symptom and root cause:** as BUG-0099: `sdtw.line4` copied `f4952.line4e`, figured whether or not
  the form is filed; i1040sd pp. 15–16, line 4, "Enter the amount from Form 4952, line 4e".
- **Where:** `forms/2025/sdtw.yaml`.
- **Fix:** line 4 is the Form 4952 amount when `sd.filing4952`, zero otherwise; lines 5 and 47 are
  unchanged (line 3 is zero on those returns). `stage4.sdtw.special_rates` had recorded the defect and is
  re-recorded to zero.
- **Tags:** unguarded-copy; recorded-expectation-laundering; closes-earlier-entry; caught-by-source-adjudication

## BUG-0161 — Form 2441's non-dependent screen omits the death-year residency rule (open)

- **Date:** 2026-10-26
- **Caught by:** round 3 source adjudication of the dependents collection (`adjudication/dependent.md`),
  checking BUG-0157.
- **Symptom:** the `f2441.nondependent` screen asks whether a disabled person who is not your dependent
  "lived with you for more than half of 2025", without p503 p. 3's rule for a person who died in 2025 (more
  than half the time they were alive). Such a person, who would be a qualifying person, is answered No
  and the credit is understated on that rare return.
- **Root cause:** BUG-0157 applied p503 p. 3 to dependents only; the screen's question text keeps the
  calendar-year wording.
- **Where:** `forms/2025/f2441.yaml`, `f2441.nondependent`.
- **Fix:** open; to be fixed in the next batch (owner's decision of 2026-10-26: round-3 findings are
  recorded and fixed after the commit). Proposed: add the death-year rule to the screen question, citing
  p503 p. 3.
- **Tags:** part-year-rule-missing; incomplete-fix; amount-affecting; open; caught-by-source-adjudication

## BUG-0162 — Form 1040 line 28's box for not claiming the ACTC is neither encoded nor recorded (open)

- **Date:** 2026-10-26
- **Caught by:** round 3 source adjudication of the Form 1040 render comparison (`adjudication/f1040.md`).
- **Symptom:** Form 1040 (2025) line 28 prints "If you do not want to claim the ACTC, check here"; i1040gi
  p. 61: "If you do not want to claim the additional child tax credit, check the box on line 28." The
  project always claims the credit and no line, question, scope screen or task records the limit (line
  27c's equivalent is recorded in T-027). Amounts differ only for a filer who would opt out.
- **Where:** `forms/2025/f1040.yaml`, `f1040.line28`.
- **Fix:** open; next batch. The choice between recording a design limit (a Bool line, always false,
  beside T-027) and asking the choice is the owner's.
- **Tags:** printed-choice-not-encoded; unrecorded-scope-limit; open; caught-by-render-adjudication

## BUG-0163 — Car loan column (ii) subtracts all Schedule C interest from prorated QPVLI (open)

- **Date:** 2026-10-27
- **Caught by:** source adjudication of the carloan render reviews re-run after the rendered-subject
  citation fix (`.transcription/proposed/citefix/`).
- **Symptom:** on a partly qualifying loan (mixed-use, or refinanced above the old balance) column (iii)
  is the prorated QPVLI less the whole interest deducted on Schedule C. Proposed § 1.163-16(g)(1)–(2)
  (fr-2025-24154 p. 23) reduces QPVLI only by deducted interest "that is QPVLI", so the Schedule C amount
  would be prorated by the same ratio. Example: ratio 0.8, interest $1,000, $300 on Schedule C: the
  project gives $500, the pro rata reading $560; Schedule 1-A line 24 and Form 1040 line 13b are
  understated. Moderate confidence; the owner may treat the split as an ambiguity.
- **Where:** `forms/2025/carloan.yaml`, `carloan.col_ii`/`carloan.col_iii`.
- **Fix:** open; next batch (owner's decision whether finding or ambiguity).
- **Tags:** proration-of-subtraction; amount-affecting; open; caught-by-render-adjudication

## BUG-0164 — Form 8995 line 3 input cited a quotation absent from the instructions

- **Date:** 2026-10-27
- **Caught by:** the same render adjudication, checking the qbi locator against the archive.
- **Symptom:** `qbi.carryforward` quoted "enter the amount from line 16 of your 2024 Form 8995", which
  appears in neither i8995 nor f8995; the citation check does not verify quotes on input lines (T-072).
- **Where:** `forms/2025/qbi.yaml`.
- **Fix:** the locator quotes i8995 p. 4, Line 3 and p. 5, Line 16, keeping the owner's note; citation only.
- **Tags:** misquoted-citation; unchecked-input-citation; caught-by-render-adjudication

## BUG-0165 — Form 1040 line 25c omits Additional Medicare Tax withheld from Form 8959 line 24 (open)

- **Date:** 2026-10-27
- **Caught by:** the UsTaxes engine differential (plan revision item C1), generated case gen-00010:
  `f8959.line24` $1,618.39, `f1040.line25c` $0, line 25d $62,472.94 against UsTaxes' $64,091.33.
- **Symptom:** Additional Medicare Tax withheld is computed on Form 8959 line 24 but never reaches Form
  1040 line 25c, so total withholding (line 25d), total payments and the refund are understated for
  every filer with Medicare wages over the threshold.
- **Root cause:** `f1040.line25c` is a supplied total; i1040gi p. 39, Line 25c—Other Forms: "Include the
  amount shown on Form 8959, line 24, in the total on line 25c."
- **Where:** `forms/2025/f1040.yaml`, `f1040.line25c`.
- **Fix:** open; next batch. The UsTaxes adapter excludes the affected cases as
  `additional_medicare_withholding` until then.
- **Tags:** cross-form-amount-not-carried; amount-affecting; open; caught-by-external-engine

## BUG-0166 — Draft cover and watermark text was read as IRS text in the year diff

- **Date:** 2026-10-27
- **Caught by:** the TY2026 adoption rehearsal (`reports/2026/rehearsal_defects.md`, F2).
- **Symptom:** about 500 sentences were reported changed because the draft cover page and "DRAFT"
  watermarks were part of the compared text.
- **Where:** `tools/year_diff.py` (`Archive.read`). **Fix:** draft marks are stripped before comparing,
  with a self-test; other archive readers still do not strip them (rehearsal O5).
- **Tags:** draft-artifact-as-text; year-adoption-tooling; caught-by-rehearsal

## BUG-0167 — Locator relocation rewrote the wrong page list in folded locators

- **Date:** 2026-10-27
- **Caught by:** the TY2026 rehearsal (F3).
- **Symptom:** `--relocate` swapped the page lists of a two-page locator (f8880 "p. 2 / p. 3") and changed
  a number inside an anchor's quoted text; the citation check would not see it.
- **Where:** `tools/citations.py` (`--relocate`). **Fix:** relocation addresses each page list by its
  segment, with a self-test. Open in the same tool: about 15 segments are moved one page too far and
  still pass the check (rehearsal O1), and a second relocation moves f8880 "Caution" again (O2).
- **Tags:** silent-wrong-page; year-adoption-tooling; caught-by-rehearsal

## BUG-0168 — After adoption, changed values and year-named quotes fell off the year worklist

- **Date:** 2026-10-27
- **Caught by:** the TY2026 rehearsal (F4, F5).
- **Symptom:** after `year_diff.py --adopt`, parameters whose dollar values changed (`dc.exclusion_max`,
  `qbi.threshold`, `hsa.*_55`) and quotes naming "2025" no longer appeared on the worklist, so a reviewer
  following it could miss real changes.
- **Where:** `tools/year_diff.py`. **Fix:** the worklist compares adopted values and year-substituted
  quotes against the prior year, with self-tests.
- **Tags:** worklist-misses-change; year-adoption-tooling; caught-by-rehearsal

## BUG-0169 — SEP worksheet Step 1 shows only Schedule C profit when other self-employment income exists (open)

- **Date:** 2026-10-27
- **Caught by:** the mutation-equivalence second reader (plan revision item C5; P3 in
  `reports/2025/equivalence_review.md`): mutant `operand.person.person.sep_s1.sc_total` survives and is
  not equivalent.
- **Symptom:** `person.sep_s1` copies the Schedule C total even when the self-employment screen is Yes or
  unanswered. Pub. 560 (2025), Deduction Worksheet for Self-Employed, Step 1: "Enter your net profit from
  Schedule C (Form 1040), line 31; Schedule F (Form 1040), line 34;* or Schedule K-1 (Form 1065),* box 14,
  code A." With other self-employment income the printed Step 1 is understated, and with the screen
  unanswered it is shown as known. Step 2 refuses on those returns, so no deduction is wrong.
- **Where:** `forms/2025/person.yaml`, `person.sep_s1`.
- **Fix:** open; next batch (gate Step 1 on the screen as Step 2 is). The mutant is listed in
  `OPEN_DEFECT_SURVIVORS` in `engine/src/mutate.ts` until then.
- **Tags:** printed-step-understated; availability-overclaim; open; caught-by-mutation-review

## BUG-0170 — The mutation step could not fail check-all

- **Date:** 2026-10-27
- **Caught by:** the mutation-equivalence second reader (P4).
- **Symptom:** `runMutation` returned 1 when a survivor was unexplained, but `engine/src/main.ts` awaited
  it and discarded the status, so `check-all` passed with unexplained survivors listed in
  `reports/2025/mutation.md`.
- **Where:** `engine/src/main.ts`.
- **Fix:** `process.exit(await runMutation())`. Survivors explained by an open bug entry are listed
  separately (`OPEN_DEFECT_SURVIVORS`); a listed mutant that is killed, or whose entry is not open, fails
  the run.
- **Tags:** discarded-exit-status; silent-check; caught-by-mutation-review

## BUG-0171 — Twelve mutation-equivalence arguments were false

- **Date:** 2026-10-27
- **Caught by:** the independent second reading of every equivalence argument (integrity plan 1.6),
  by differential search over fixtures, generated returns and partial records.
- **Symptom:** 12 survivors were accepted as equivalent with arguments that fail on a counterexample:
  nine were fixture gaps (the project is right per the source; two visible on Form 1040 with complete
  inputs: the self-employed EIC boundary and combat pay), two differ only as unknown against known (P1,
  P2), one is BUG-0169. The shared flaws: ignoring the mutated line's own printed value, and assuming a
  refusal arrives first when an earlier gate can be unanswered.
- **Where:** `engine/src/mutate.ts` (`EQUIVALENT_IF`, `EQUIVALENT`).
- **Fix:** the nine gaps and P1/P2 are killed by new fixtures (stage4, stage8, stage9, stage10,
  stage14); the prose-only table is removed and recurring shapes are checked by structural rules.
- **Tags:** false-equivalence-argument; prose-trusted; caught-by-second-reader

## BUG-0172 — Fix for BUG-0165: Form 1040 line 25c now includes Form 8959 line 24

- **Date:** 2026-10-27
- **Closes:** BUG-0165.
- **Fix:** new input `f1040.line25c_other` (W-2G, Schedules K-1, Forms 1042-S, 8805 and 8288-A, i1040gi p. 39);
  `f1040.line25c` is its sum with `f8959.line24`. 822 fixture inputs renamed; two stage-8 cases
  re-recorded ($137.70 of Additional Medicare Tax withheld now reaches line 25c; line 37 falls by it). The
  OpenTaxSolver adapter now passes OTS's own Form 8959 line 24 into its line 25c, and UsTaxes'
  `additional_medicare_withholding` exclusion is removed; all four engines agree (0 unexplained).
- **Tags:** closes-earlier-entry; cross-form-amount-carried; confirmed-by-external-engines

## BUG-0173 — Fix for BUG-0161: Form 2441's non-dependent screen states the death-year rule

- **Date:** 2026-10-27
- **Closes:** BUG-0161.
- **Fix:** the `f2441.nondependent` question counts, for a person born or who died in 2025, more than half
  of the time they were alive (p503 p. 3); citation added. Question wording only; no computed value changes.
- **Tags:** closes-earlier-entry; question-wording

## BUG-0174 — Disposition of BUG-0162: line 28's ACTC box recorded as a design limit

- **Date:** 2026-10-27
- **Closes:** BUG-0162 (owner's decision, 2026-10-27).
- **Fix:** `f1040.line28_box` (printed "28 (box)") is always unchecked, labelled that the choice not to
  claim the ACTC is not asked, citing i1040gi p. 61, Line 28, as line 27c's choice is handled (T-027).
- **Tags:** closes-earlier-entry; recorded-design-limit

## BUG-0175 — Fix for BUG-0163: car loan column (ii) is the QPVLI part of the Schedule C interest

- **Date:** 2026-10-27
- **Closes:** BUG-0163 (owner's decision, 2026-10-27).
- **Fix:** `carloan.col_ii` (printed 22(ii)) is the Schedule C interest (`carloan.sc_interest`, the former
  column (ii) logic) prorated by the loan's qualifying ratio, as the interest is, and zero for a loan that
  does not qualify; proposed § 1.163-16(g)(1), fr-2025-24154 p. 23: "Independently deductible interest is
  limited to interest that is QPVLI". The raw input `carloan.col_ii_input` is now a helper. Regression
  `stage12.car.mixed_sc_interest_prorated` (column (iii) $254.40, previously $233.20).
- **Tags:** closes-earlier-entry; proration-of-subtraction; amount-affecting

## BUG-0176 — Fix for BUG-0169: SEP worksheet Step 1 refuses with other self-employment income

- **Date:** 2026-10-27
- **Closes:** BUG-0169.
- **Fix:** `person.sep_s1` carries the `person.se_screened` refusal, as Schedule SE line 2 (which Step 2
  reads) does, citing p560 p. 39, Step 1. Regression `stage14.sep.step1_other_se_income`. The mutant is
  removed from `OPEN_DEFECT_SURVIVORS`.
- **Tags:** closes-earlier-entry; availability-overclaim-fixed

## BUG-0177 — Citation relocation placed segments a page late while the check passed them

- **Date:** 2026-10-27
- **Caught by:** the TY2026 adoption rehearsal (`reports/2026/rehearsal_defects.md`, O1–O3; recorded open in
  BUG-0167).
- **Symptom:** `citations.py --relocate` accepted moves that weakened an anchor (its heading printed on the
  old page, only in force on the new), placing 15 TY2026 segments one page late (e.g. `sc.yaml:113` p. 10
  to 12, should be 11) though the citation check passed them; a second run moved f8880 "Caution" again;
  quote-less documents behind a new draft cover learnt no page shift (f4952).
- **Where:** `tools/citations.py`, `tools/year_diff.py` (`--adopt`).
- **Fix:** relocation compares against the source year's page (`--relocate --from`, passed by `--adopt`): a
  move may not weaken the anchor, and a segment that fits two pages is left for review and listed in
  `reports/<year>/relocation_from_<from>.md`; re-runs keep segments the check passes (idempotent); a
  quote-less document behind a draft cover takes the cover's shift. Self-tests added; 15 weakened
  placements to 0. Fourteen segments that pass on their 2025 pages are listed for review.
- **Tags:** silent-wrong-page; non-idempotent-tool; year-adoption-tooling; caught-by-rehearsal

## BUG-0178 — Soft-hyphen line breaks read as two words

- **Date:** 2026-10-27
- **Caught by:** the TY2026 rehearsal (O7): the PDFKit text check failed on the p4681 and i1120ssk drafts.
- **Symptom:** words broken at a line end with a soft hyphen were read as two words by the PDFKit
  comparison and by `citations.norm`; two 2025 final documents also use soft hyphens.
- **Where:** `tools/check_extraction.py`, `tools/citations.py`; archive reading now shared in
  `tools/archive_text.py` (which also strips draft marks for seven readers, rehearsal O5).
- **Fix:** soft hyphens are rejoined before comparing; self-tests in `archive_text.py` and
  `check_extraction.py`.
- **Tags:** text-normalization; caught-by-rehearsal

## BUG-0179 — Year diff reported false value changes and two checkers crashed on a missing source

- **Date:** 2026-10-27
- **Caught by:** the TY2026 rehearsal (O4, O6).
- **Symptom:** amounts under $1,000 matched bare numbers in unrelated text, and a value change was
  reported where the other year's sentence printed the same amount (17 parameters flagged, 13 falsely);
  `check_macrs_tables.py` and `check_auto_limits.py` crashed with a traceback when a source was missing.
- **Where:** `tools/year_diff.py`, `tools/check_macrs_tables.py`, `tools/check_auto_limits.py`.
- **Fix:** small amounts match only with their "$" and a value finding requires the other year's sentence
  not to print the same amount (17 to 4); the checkers fail naming the missing edition and skip a year
  with no table. Self-tests added.
- **Tags:** false-change-report; crash-on-missing-input; year-adoption-tooling; caught-by-rehearsal

## BUG-0180 — SEP worksheet Step 3 floored at zero where Pub. 560 prints no floor (open)

- **Date:** 2026-10-27
- **Caught by:** round 4 source adjudication of the person render review (`adjudication/person.md`).
- **Symptom:** `person.sep_s3` subtracts Step 2 from Step 1 and floors the result at zero; p560 p. 39,
  Deduction Worksheet for Self-Employed, Step 3 prints "Subtract step 2 from step 1" with no floor. On a
  Schedule C loss with a SEP plan the printed Steps 3, 5, 7 and 21 show $0.00 instead of negative amounts.
  No Form 1040 amount changes (the deduction is zero either way). Witness constructed, not executed.
- **Where:** `forms/2025/person.yaml`, `person.sep_s3`.
- **Fix:** open; next batch (proposed: an ambiguity-register entry for the floor and a regression; no
  computed deduction changes).
- **Tags:** printed-step-floored; open; caught-by-render-adjudication

## BUG-0181 — Disposition of BUG-0180: the SEP worksheet Step 3 floor recorded as a registered reading

- **Date:** 2026-10-27
- **Closes:** BUG-0180 (owner's decision of 2026-10-27 to close it before coverage resumes).
- **Witness executed:** Schedule C loss $5,000, SEP plan rate 10%, contribution $0. Step 1 -$5,000.00, Steps 3, 5,
  7 and 21 $0.00, `person.sep_excess` false, Schedule 1 line 16 $0.00, as BUG-0180 predicted.
- **Fix:** `amb.2025.sep_loss_floor` records both readings and chooses the floor, naming `person.sep_s3`.
  The line-level link waits for the next change to `person` (T-074; owner's decision of 2026-10-27), since the
  key is part of the transcription subject and alone would stale the person review logs. The round-4 finding's claim that a zero contribution deducts zero on both readings is not
  right: under the printed arithmetic Step 21 is negative and `person.sep_excess` refuses the return. New
  regression `stage14.sep.loss_floor`. No computed value changes.
- **Tags:** closes-earlier-entry; registered-reading

## BUG-0182 — OpenTaxSolver's IRA limitation left out the student loan interest line it moves

- **Date:** 2026-10-27
- **Caught by:** the engine differential after Stage 20 (case gen-00497, OpenTaxSolver `s1.line21`, project $0,
  engine $82.89, unexplained).
- **Symptom:** the adapter supplies the IRA deduction as the contributions (OpenTaxSolver has no IRA Deduction
  Worksheet). The `ira_phaseout` limitation excluded the lines after AGI, but Schedule 1 line 21's phase-out reads
  modified AGI after the IRA deduction, so on a return in both phase-outs the student loan interest deduction
  differed for the same cause. The Stage 20 carryover moved this return's AGI into the student loan range; before,
  it was above both.
- **Where:** `tools/engines/ots_adapter.py`, `limitations()`, feature `ira_phaseout`.
- **Why the checks did not catch it:** no earlier generated return was in both phase-out ranges at once.
- **Fix:** the limitation also covers `s1.line21`. No project value changes.
- **Tags:** engine-limitation-incomplete; caught-by-engine-differential

## BUG-0183 — The 28% Rate Gain and Unrecaptured Section 1250 Gain Worksheets were shown when Schedule D line 17 is No

- **Date:** 2026-10-27
- **Caught by:** the Stage 20 blind predictions (scenario R8: Form 1099-DIV box 2d $400 and a long-term carryover,
  Schedule D line 16 a loss). Both predictors marked the 28% Rate Gain Worksheet as not used; the values sheet showed
  it with line 4 $400 and line 5 ($3,000).
- **Symptom:** i1040sd p. 11 says to complete both worksheets "If you checked “Yes” on line 17"; Schedule D line 17
  says "No. Skip lines 18 through 21". The worksheets' printed lines had no `shown_when`, so a return that never
  reaches them showed nonzero amounts on them (line 4 from box 2d before this stage; lines 5 and 16 from a carryover
  since). Under the owner's decision of 2026-10-26 a worksheet that is not reached is skipped, and a nonzero amount on
  a skipped line is a defect. No other line changes: Schedule D lines 18 and 19 already read zero when line 17 is No.
- **Where:** `forms/2025/g28.yaml`, `forms/2025/u1250.yaml`.
- **Why the checks did not catch it:** the skipped-line sweep of round 4 covered worksheets after a printed STOP,
  not worksheets entered only from a Schedule D Yes answer.
- **Fix:** `g28.reached` and `u1250.reached` (Schedule D line 17 is Yes); every printed line of both worksheets is
  shown only then. Values unchanged.
- **Tags:** skipped-line-shown; caught-by-blind-prediction

## BUG-0184 — Schedule D lines 4, 5, 11 and 12 are still labelled as screened for carryovers (open)

- **Date:** 2026-10-27
- **Caught by:** the Stage 20 adjudication of the Schedule D reviews (`.transcription/proposed/stage20/sd.findings.md`, F1).
- **Symptom:** the labels of `sd.line4`, `sd.line5`, `sd.line11` and `sd.line12` read "zero only after unsupported
  source/carryover screening"; Stage 20 removed the carryover refusal from those lines, so "/carryover" no longer
  describes them. Wording only: no value, refusal or shown line changes.
- **Where:** `forms/2025/sd.yaml`.
- **Fix:** open; with the next change to `sd.yaml` (drop "/carryover"). Deferred because the labels are part of the
  Schedule D review subject, so a wording change alone would stale the current Schedule D reviews (the pattern of
  T-074).
- **Tags:** stale-label; open; caught-by-source-adjudication

## BUG-0185 — The Capital Loss Carryover Worksheet showed its lines when it does not apply

- **Date:** 2026-10-27
- **Caught by:** the Stage 20 adjudication of the clcw render reviews (`.transcription/proposed/stage20/clcw.findings.md`,
  F1), by reading the form against the source; confirmed on `stage20.mut.line21_below_limit`.
- **Symptom:** i1040sd p. 10: "Use this worksheet ... if your 2024 Schedule D, line 21, is a loss and (a) that loss is a
  smaller loss than the loss on your 2024 Schedule D, line 16; or (b) if the amount on your 2024 Form 1040, 1040-SR or
  1040-NR, line 15 would be less than zero ... Otherwise, you don’t have any carryovers." Where neither holds, lines 1
  to 7 showed amounts (line 8 and 13 are $0 by the arithmetic). A worksheet the filer is told not to use is not reached,
  and a nonzero amount on a line not reached is a defect (owner's decision of 2026-10-26). Display only.
- **Where:** `forms/2025/clcw.yaml`.
- **Why the checks did not catch it:** the decision batch argued the applicability test needs no gate line because the
  carryovers come out zero; that is true of the values, not of the lines shown.
- **Fix:** `clcw.applies` (condition (a) or (b)); lines 1 to 5 are shown on it, lines 6 to 8 on `clcw.show_st` and 9 to 13
  on `clcw.show_lt`, which now require it. Values unchanged.
- **Tags:** skipped-line-shown; caught-by-source-adjudication

## BUG-0186 — A 2024 line 21 loss entered below what any 2024 return shows was accepted

- **Date:** 2026-10-27
- **Caught by:** the same adjudication (F2); witness: a $5,000 2024 loss with line 21 entered as $0 gave a $5,000
  carryover in place of $2,000 and a 2025 deduction $1,000 too large.
- **Symptom:** `clcw.bad` refused line 21 entries above $3,000 or above the line 16 loss, not entries below the smaller of
  the line 16 loss and $1,500, which no correct 2024 return can print for any filing status (i1040sd p. 3, "plus $3,000
  ($1,500 if married filing separately)"). The carryover, the 2025 deduction and the carryover to 2026 changed on a
  wrong entry.
- **Where:** `forms/2025/clcw.yaml`, `clcw.bad`.
- **Why the checks did not catch it:** the generator draws line 21 exactly from the 2024 figures, so no generated return
  carries an understated entry; D2(b) listed only the upper bounds.
- **Fix:** `clcw.prior_floor` (the smaller of the line 16 loss and the new parameter `clcw.prior_limit_mfs`, $1,500); `clcw.bad`
  also refuses an entry below it; the remedy and `amb.2025.clcw_line2_printed` name the bound. Regressions
  `stage20.refuse.line21_zero_with_loss` and `stage20.refuse.line21_below_floor`.
- **Tags:** consistency-screen-incomplete; caught-by-source-adjudication

## BUG-0187 — The carryover to 2026 was shown whenever Schedule D line 16 is a loss

- **Date:** 2026-10-27
- **Caught by:** the same adjudication (`clcw26.findings.md`, F1); witness: a fully deducted $1,000 loss.
- **Symptom:** i1040sd p. 14, Line 21: "You have a capital loss carryover from 2025 to 2026 if you have a loss on line 16
  and either" the loss is more than the loss on line 21 or line 15 would be less than zero. `clcw26.show` tested only the
  loss on line 16, so the worksheet was shown (with $0 carryovers) where the instructions say there is none. Display only.
- **Where:** `forms/2025/clcw26.yaml`, `clcw26.show`.
- **Fix:** `clcw26.show` tests the whole sentence. Values unchanged.
- **Tags:** skipped-line-shown; caught-by-source-adjudication

## BUG-0188 — A lawfully present alien below 100% of the poverty line was computed as not an applicable taxpayer

- **Date:** 2026-10-29
- **Caught by:** the session, checking decision D6 against the encoding before the Stage 18 adjudication; confirmed by the
  render and transcription adjudication (`.transcription/proposed/stage18/f8962.findings.md` and
  `f8962.render-classm.findings.md`, R1). Witness: blind return P8 (line 5 = 79, advance payments $5,000) with an enrolled
  lawfully present alien: line 24 $0 and a $375 repayment where the source allows a $160 net credit.
- **Symptom:** i8962 p. 9, "Alien lawfully present in the United States", makes such a filer an applicable taxpayer below
  100%. D6 decided the branch is refused, but `f8962.other` asks only about someone not lawfully present and no other
  screen asked about it, so the return was completed with a wrong amount instead of refused.
- **Where:** `forms/2025/f8962.yaml`, `f8962.applicable` and the line 24 refusals.
- **Why the checks did not catch it:** the blind predictors and both reviewers worked from the same screens; deepseek's
  render matched every line.
- **Fix:** the gate `f8962.alien_below` (asked only with a Form 1095-A and line 5 below 100) and `f8962.alien_branch`,
  refusing on line 24 with the i8962 p. 9 citation. Regression `stage18.refuse.alien_below_100`.
- **Tags:** missing-screen; caught-by-source-adjudication

## BUG-0189 — Column B was counted per Form 1095-A for the year, not per month

- **Date:** 2026-10-29
- **Caught by:** the Stage 18 transcription adjudication (`.transcription/proposed/stage18/f8962.findings.md`, R2); neither
  reviewer raised it. Witness: one state, a policy for January to June and another for July to December: line 24 $2,100
  and line 26 $600 where the source gives $3,000 and $1,500.
- **Symptom:** i8962 p. 16, Column (b), applies the one-form rule only "If you have more than one Form 1095-A showing
  coverage in a particular month". `f1095a.b_counted` asked for one counted form per state for the whole year, so
  policies that follow one another in one state lost column B for the uncounted form's months, or, with both marked,
  were refused by `f8962.two_counted`.
- **Where:** `forms/2025/f1095a.yaml` `f1095a.b_counted`; `forms/2025/f8962.yaml` `f8962.same_state_counted`,
  `f8962.two_counted` and its remedy.
- **Fix:** the questions ask the per-month rule (count a form unless another counted form from its state covers every
  one of its months; refuse two counted forms from one state that share a month, which also refuses partial overlaps).
  Regression `stage18.mut.sequential_policies_one_state`. The generator draws sequential policies too.
- **Tags:** misread-source; caught-by-source-adjudication

## BUG-0190 — The foreign tax credit limit left out Schedule 2 line 1z

- **Date:** 2026-10-29
- **Caught by:** the Stage 18 adjudication of the Schedule 3 render logs (`.transcription/proposed/stage18/s3.findings.md`,
  F1). Witness: P8 with $200 of foreign tax under the election: credit $0 and refund $167 where the source gives $200 and
  $367.
- **Symptom:** i1116 p. 25, Line 20, "Enter the total of Form 1040 ... line 16, and Schedule 2 (Form 1040), Part I, line
  1z". `ftc.limited` used line 16 alone, which was exact while every Schedule 2 Part I amount was refused; Stage 18 made
  line 1a (the excess advance PTC repayment) computed.
- **Where:** `forms/2025/ftc.yaml`, `ftc.limited`.
- **Fix:** `ftc.regular_tax` = line 16 + Schedule 2 line 1z, cited to i1116 p. 25; Form 4972 stays refused through
  `scope.other_line16`. No other limit reads line 16 alone. Regression `stage18.ftc_limit_with_repayment`.
- **Tags:** stale-assumption; caught-by-source-adjudication

## BUG-0191 — Form 8962 lines were shown on returns with no Form 1095-A

- **Date:** 2026-10-29
- **Caught by:** the Stage 18 class M adjudication (O1): line 10 printed "Yes" on every return without a Form 1095-A.
- **Symptom:** lines 1 to 5, 7, 8a, 8b, 9, 10, 11(a), (b), (f), 24 and 25 were shown on the values sheet of every return,
  though Form 8962 is filed only with a Form 1095-A (i8962 p. 3, Who Must File). Display only.
- **Where:** `forms/2025/f8962.yaml`.
- **Fix:** lines 1 to 5 are shown only when `f8962.any`; lines 7 and 8 use `f8962.show_applicable`. The round-2
  adjudication found the fix incomplete (R3, N1: `show_annual_calc` and `f8962.net` did not test for a form, so 11(c) to
  11(e) and 26 still showed) and that lines after the line 5 STOP showed for a non-applicable taxpayer with no advance
  payments (R4; i8962 p. 10, "if no APTC was paid for any individuals in your tax family, stop; do not complete Form
  8962"). `f8962.filing` (a form, and an applicable taxpayer or advance payments) now gates lines 9, 10, 24, 25, line 11
  (`show_annual`, which `show_annual_calc` reads), every month's `show_<m>`, line 26 (`f8962.net`) and lines 27 to 29 (`f8962.excess`, which the round-3 adjudication found
  printing UNKNOWN on completed returns with no Form 1095-A, R5); its name follows
  the class M convention, so unfiled Forms 8962 are no longer worked by hand. Values unchanged.
- **Tags:** skipped-line-shown; caught-by-source-adjudication

## BUG-0192 — An "other" household member was counted as a qualifying relative without the local-law condition (open)

- **Date:** 2026-10-29
- **Caught by:** the Stage 18 dependent adjudication (`.transcription/proposed/stage18/dependent.findings.md`, F2), from
  the Claude transcription reply's note. Pre-existing.
- **Symptom:** i1040gi p. 19, Step 4, "Any other person ... who lived with you all year as a member of your household if
  your relationship didn't violate local law." `dependent.qr_relationship` is true for `other` with 12 months without
  asking the condition. Low: rare, and it allows a dependent the source might not.
- **Where:** `forms/2025/dependent.yaml`, `dependent.qr_relationship`.
- **Fix:** open; with the next change to `dependent.yaml`: one Bool asked only for `other` with 12 months (the
  alternative, rewording the `other` gloss, changes the owner's `amb.2025.foster_parent_relationship` gloss and needs the
  owner). Deferred because a new input stales the dependent reviews just adjudicated (the pattern of BUG-0184).
- **Tags:** missing-condition; open; caught-by-source-adjudication

## BUG-0193 — Four refusal remedies still say the premium tax credit is "entered from Form 8962" (open)

- **Date:** 2026-10-29
- **Caught by:** the Stage 18 scope adjudication (`.transcription/proposed/stage18/scope.findings.md`, F3) and the Stage 19
  decision draft.
- **Symptom:** the remedies of `scope.credits` in `scope.yaml`, `f1040.yaml` (lines 29 and 30) and `s3.yaml` (line 8)
  list "the net premium tax credit entered from Form 8962"; it is now figured. Wording only.
- **Fix:** open; with Stage 19, which rewrites those remedies to name the education credits (its decision batch, Settled
  item 1). Deferred because `f1040.yaml` is otherwise unchanged by Stage 18.
- **Tags:** stale-label; open; caught-by-source-adjudication

## BUG-0194 — Form 8863 lines skipped by the form's own instructions were shown

- **Date:** 2026-10-29
- **Caught by:** the Stage 19 blind predictions (`reviews/2025/blind/stage19/`): both predictors left blank lines 13 to 16
  when line 10 is zero, and a student's line 24 after line 23 is Yes; the values sheet showed them.
- **Symptom:** f8863 p. 1, line 10, "If zero, skip lines 11 through 17, enter -0- on line 18, and go to line 19"; line 4,
  "If zero or less, stop; you can't take any education credit"; p. 2, lines 23 to 25, "Stop! Go to line 31 for this
  student". The lines after each stop were shown with their computed values. Display only.
- **Where:** `forms/2025/f8863.yaml` (lines 5 to 19), the Part III lines 24 to 26 on `person.yaml` and `dependent.yaml`.
- **Fix:** `f8863.show_after4` (line 4 above zero) gates lines 5 to 19, `f8863.show_llc` (and line 10 above zero) lines 11
  to 16; `edu_show24` to `edu_show26` chain lines 24 to 26 on the answers before them. Values unchanged.
- **Tags:** skipped-line-shown; caught-by-blind-prediction

## BUG-0195 — The EIC main-home test asked only about the filer's home, not the spouse's on a joint return

- **Date:** 2026-10-29
- **Caught by:** the Stage 19 adjudication of the Form 1040 render logs (`.transcription/proposed/stage19/f1040.findings.md`,
  H1). Pre-existing. Witness: `stage9.eic.joint.no_child.12000` with the spouse's main home abroad: the project allows
  $649.00 where the source gives none.
- **Symptom:** i1040gi p. 42, Step 4, question 3, "Was your main home, and your spouse's if filing a joint return, in the
  United States for more than half of 2025?" `eic.us_home` asked "Was your main home in the United States".
- **Where:** `forms/2025/eic.yaml`, `eic.us_home`.
- **Fix:** the question asks about both homes on a joint return, as printed.
- **Tags:** misread-source; caught-by-source-adjudication

## BUG-0196 — Two Form 5695 remedies called the child care and saver's credits outside the tool

- **Date:** 2026-10-29
- **Caught by:** the Stage 19 adjudication of Form 5695 (`.transcription/proposed/stage19/f5695.findings.md`, S1).
- **Symptom:** the `scope.credits` remedies of `f5695.rce_ws2` and `f5695.eehi_ws2` listed only the foreign tax credit,
  the dependent credits, the education credits and the residential energy credits as computed; the tool also computes
  the child and dependent care credit and the saver's credit, which both worksheets include. Wording only.
- **Where:** `forms/2025/f5695.yaml`.
- **Fix:** the remedies name every computed credit, as `s8812.clw_a2`'s does.
- **Tags:** stale-label; caught-by-source-adjudication

## BUG-0197 — The education academic-period screen did not say which expenses to compare

- **Date:** 2026-10-29
- **Caught by:** the Stage 19 adjudication of the person and dependent logs (`.transcription/proposed/stage19/person.findings.md`,
  Q1), in the stage that introduced it.
- **Symptom:** `person.edu_over` and `dependent.edu_over` asked whether a period's assistance exceeded "that period's own
  qualified education expenses". A lifetime learning student whose outside course materials covered the gap would
  answer No, and line 31 would be netted over the year instead of floored for that period (i8863 p. 9, "for each
  student for each academic period"); a constructed witness gives line 31 $3,000 for $2,600.
- **Where:** `forms/2025/person.yaml`, `forms/2025/dependent.yaml` (Stage 19 block).
- **Fix:** the question compares with the expenses that had to be paid to the institution, the lifetime learning
  credit's expenses; for an American opportunity student it can only over-refuse.
- **Tags:** ambiguous-question; caught-by-source-adjudication

## BUG-0198 — A Form 8862 or ban answer refused returns that could take no education credit

- **Date:** 2026-10-29
- **Caught by:** the Stage 19 adjudication of Form 8863 (`.transcription/proposed/stage19/f8863.findings.md`, R2), in the
  stage that introduced it. Witness: Jack and Kay with wages of $200,000 and the ban answered Yes: refused, though line
  4 is zero and no credit can be claimed.
- **Symptom:** `f8863.ban_refused` tested line 1 above zero only; f8863 p. 1, line 4, "If zero or less, stop; you can't
  take any education credit".
- **Where:** `forms/2025/f8863.yaml`.
- **Fix:** the gate also requires line 4 above zero. Accepted residue (round-2 R3): when line 4 is a few dollars, line 6
  rounds to 0.000 and line 7 is $0, so a ban answer still refuses a return that claims nothing; an over-refusal, kept.
- **Tags:** over-refusal; caught-by-source-adjudication

## BUG-0199 — Disposition of BUG-0192 and BUG-0193

- **Date:** 2026-10-29
- **Closes:** BUG-0192 (fixed with the Stage 19 change to `dependent.yaml`, the trigger it was deferred to: the new input
  `dependent.lawful`, asked only for an `other` or `sibling_descendant` person who lived with you all year (the second added in round 2, L1), and `dependent.qr_relationship`
  requiring it, per i1040gi p. 19, Step 4, "if your relationship didn't violate local law"; fixtures with such a person
  answer it Yes, which is how they were already claimed) and BUG-0193 (fixed with Stage 19: the remedies name the
  education credits and the premium tax credit "figured on Form 8962").
- **Tags:** disposition

## BUG-0200 — The joint medical-exception refusal fired on single returns

- **Date:** 2026-10-29
- **Caught by:** the Stage 21 blind-scenario builder (E6, a single filer whose exception 05 exceeds Schedule A line 4), in the
  stage that introduced it, before review.
- **Symptom:** `s2.e05_over` compared the raw exception 05 amounts of everyone on the return with Schedule A line 4, so a
  single filer's medical exception above line 4 was refused instead of limited to it (D4).
- **Where:** `forms/2025/s2.yaml`, `s2.e05_total`.
- **Fix:** the total adds each person's already-limited amount (`person.x_c05`), so only spouses who together exceed line
  4 are refused (D8(d)).
- **Tags:** over-refusal; caught-by-blind-scenario

## BUG-0201 — More than one emergency personal expense distribution a year was excepted

- **Date:** 2026-10-29
- **Caught by:** the Stage 21 blind predictions (E5: both predictors excepted only one of two emergency distributions), in
  the stage that introduced it.
- **Symptom:** p590b p. 28, Distribution limits, "You are limited to taking one emergency personal expense distribution per
  calendar year" (26 U.S.C. 72(t)(2)(I)(ii), "Not more than 1 distribution per calendar year"). The project limited only the
  year's total to $1,000, so two distributions claiming exception 23 were both excepted.
- **Where:** `forms/2025/person.yaml` (Stage 21 block), `forms/2025/f5329.yaml` line 4.
- **Fix:** `person.x_two23` refuses Form 5329 line 4 when exception 23 is claimed on more than one Form 1099-R (the tool
  cannot tell which came first); blind return E5 claims it on the first distribution only.
- **Tags:** missing-limit; caught-by-blind-prediction

## BUG-0202 — A 2025 HSA excess withdrawn by the due date was taxed at 6%

- **Date:** 2026-10-29
- **Caught by:** the Stage 21 adjudication of Form 8889 (`.transcription/proposed/stage21/f8889.findings.md`,
  S21-HSA-WITHDRAWN), in the stage that introduced Part VII.
- **Symptom:** i5329 p. 8, Line 47: excess contributions withdrawn by the due date, with their earnings, "will be treated
  as not having been contributed". `f8889.unsupported` asked only about "a 2025 distribution that withdrew excess
  contributions", so a withdrawal made in 2026 before the due date was not refused and Part VII taxed the excess. D6 had
  said the question would be reworded.
- **Where:** `forms/2025/f8889.yaml`, `f8889.unsupported`.
- **Fix:** the question asks about a withdrawal of excess contributions or their earnings made in 2025 or in 2026 by the
  due date of the 2025 return (refused, as D6 decided).
- **Tags:** missing-screen; caught-by-source-adjudication

## BUG-0203 — The account-value limits of exceptions 22 and 23 were not stated

- **Date:** 2026-10-29
- **Caught by:** the Stage 21 adjudication of retirement, person and the Form 5329 render logs (F1 EXC-LIMITS, VALUE-LIMBS).
- **Symptom:** p590b p. 28 limits exception 22 to the lesser of $10,300 or 50% of the IRA's present value, and exception
  23 to the lesser of $1,000 or the IRA interest less $1,000. D4 put the account-value halves in the question's wording,
  but `retirement.exc_amount` did not mention them (nor D4's help for 07 and 08), and the three-year bar on exception 23
  was not screened.
- **Where:** `forms/2025/retirement.yaml` (Stage 21 block).
- **Fix:** `exc_amount` states both account-value limits and the 07 and 08 amounts; `early_screen` lists an emergency
  distribution within 3 years after an earlier one not repaid. The question also numbers terminal illness 20, as i5329
  p. 5 does (it said 21).
- **Tags:** question-incomplete; caught-by-source-adjudication

## BUG-0204 — The Form 1099-R code question did not offer the new codes

- **Date:** 2026-10-29
- **Caught by:** the Stage 21 adjudication of the person logs (noted), in the stage that added the codes.
- **Symptom:** `retirement.code` listed normal_7, death_4, early_exception_2, direct_rollover_G, qualified_roth_Q and other,
  so a filer with code 1, S or 3 following the wording would answer "other" and be refused.
- **Where:** `forms/2025/retirement.yaml`, `retirement.code`.
- **Fix:** the question names early_1, simple_S and disability_3. `s2.other`'s new clause moves to the end of the question,
  and `s2.line8_box` also cites i1040gi p. 112; the i8889 citations of the HSA excess lines point to p. 8.
- **Tags:** question-incomplete; caught-by-source-adjudication

## BUG-0205 — The exception amount asked how a medical, birth or abuse distribution was spent

- **Date:** 2026-10-29
- **Caught by:** the Stage 21 round-2 adjudication of retirement (`.transcription/proposed/stage21/round2/retirement.findings.md`,
  F4 EXC-USE), in the stage that introduced the question. Witness: classm.retirement.3 with $2,000 of a birth distribution
  spent: line 4 $2,460.75 where the source gives $1,710.75.
- **Symptom:** `retirement.exc_amount` asked for "the amount you used for that purpose" for exceptions 05, 19 and 22, which
  have no use test (i5329 p. 5; p590b pp. 25 and 28); only 09 (first home) and 23 (emergency expenses) turn on the purpose.
- **Where:** `forms/2025/retirement.yaml` (Stage 21 block).
- **Fix:** the question asks, per exception, for the amount that qualifies (05, 19, 22), the amount used for first-home costs
  (09), the emergency amount (23), the premiums (07) and the education expenses (08); 22 and 23 name the IRA or plan account.
  Also from round 2: the HSA withdrawal question says "including extensions" (i5329 p. 8), and the citations of the
  employer-excess lines and the line 8 box quote the paragraphs that state them.
- **Tags:** question-wrong; caught-by-source-adjudication

## BUG-0206 — The Lean evaluator named a refusal gate on an enclosing entry without the entry's key

- **Date:** 2026-10-29
- **Caught by:** the evaluator comparison (`npm run compare`) in the Stage 21 pre-commit check-all: 3 differing cases,
  `stage21.refuse.two23`, `stage21.refuse.limit_binds` and `stage21.refuse.x_other`.
- **Symptom:** a refusal raised in `person[taxpayer].f5329[form]` by a gate on the enclosing person entry
  (`when: person.x_two23`) carried the gate `person.x_two23` in the Lean evaluator and `person[taxpayer].x_two23` in the
  TypeScript one. The form, remedy and citation agreed. `spec.md` section 4 defines a refusal by "the gate line's key";
  keys are qualified by entry, so the TypeScript value is the specified one.
- **Where:** `lean/TaxFormalization/Eval.lean`, the refusal gate loop: it qualified the gate only when the gate line was in
  the current document and otherwise kept the bare id. Stage 21 is the first refusal whose gate is on an enclosing entry.
- **Fix:** the gate's key is built in the enclosing collection entry (`enclosingKey`), as a read of that entry's line is.
  Returned values were never affected.
- **Tags:** tool-defect; value-neutral; latent-until-new-input; caught-by-evaluator-comparison

## BUG-0207 — The Simplified Method Worksheet was shown on IRA entries

- **Date:** 2026-10-29
- **Caught by:** the T-067 adjudication of retirement (`.transcription/proposed/t067/retirement.findings.md`, F5), in the
  change that introduced it. Witness: classm.s2.3.deepseek without the pension answers (a traditional IRA, box 1 $92), all
  ten `(SMW n)` lines printed, `(SMW 1)` $92.
- **Symptom:** the worksheet lines' condition was `retirement.annuity`, which the interview never asks on an IRA entry; the
  values sheet hides a line only on a known false, so the worksheet printed. The worksheet is for lines 5a and 5b (i1040gi
  p. 29); IRA distributions go on lines 4a and 4b (p. 27).
- **Where:** `forms/2025/retirement.yaml`, the `(SMW 1)` to `(SMW 11)` lines.
- **Fix:** `shown_when: retirement.smw_shown` (not an IRA, tested first, and `retirement.annuity_with_cost`). Regression
  `stage21.t067.smw_hidden_ira`.
- **Tags:** skipped-line-shown; value-neutral; caught-by-source-adjudication

## BUG-0208 — The Simplified Method Worksheet was shown on an annuity whose cost was already recovered

- **Date:** 2026-10-29
- **Caught by:** the T-067 adjudication of retirement (F6). Witness: stage10.smw.cost_recovered, `(SMW 9)` $12,000 printed
  beside line 5a $0; generated 395, `(SMW 9)` $22,738.41 against a taxable amount of $0.
- **Symptom:** i1040gi p. 28, Fully Taxable Pensions and Annuities: "Your payments are fully taxable if ... (b) you got your
  entire cost back tax free before 2025"; such payments go on line 5b without the worksheet, which was still shown.
- **Where:** `forms/2025/retirement.yaml`, the `(SMW n)` lines.
- **Fix:** with BUG-0207 (`retirement.smw_shown` requires `retirement.annuity_with_cost`). Regression
  `stage21.t067.smw_hidden_cost_recovered`.
- **Tags:** skipped-line-shown; value-neutral; caught-by-source-adjudication

## BUG-0209 — Form 8880 lines 10 to 12 were shown after the line 9 stop

- **Date:** 2026-10-29
- **Caught by:** the T-067 adjudication of f8880 (`.transcription/proposed/t067/f8880.findings.md`, T067-8880-L9). Witness:
  stage15.f8880.s6, line 9 0.0 with the Credit Limit Worksheet and line 11 showing Form 1040 line 18 ($2,615.00).
- **Symptom:** Form 8880 (2025), line 9: "If line 9 is zero, stop; you can’t take this credit". T-067 hid only what
  follows the line 7 stop.
- **Where:** `forms/2025/f8880.yaml`.
- **Fix:** `f8880.past9` (`f8880.past7` and line 8 not more than `savers.agi_limit`, above which every band of the line 9
  table is 0.0) hides line 10, the worksheet and lines 11 and 12. Regression `stage21.t067.f8880_line9_stop`.
- **Tags:** skipped-line-shown; stop-instruction-ignored; value-neutral; caught-by-source-adjudication

## BUG-0210 — Credit Limit Worksheet B lines 7 to 10 were shown when line 6 says to leave them blank

- **Date:** 2026-10-29
- **Caught by:** the T-067 adjudication of s8812 (`.transcription/proposed/t067/s8812.findings.md`, T067-8812-L6). Witness:
  classm.s8812.4, `(CLW B 7)` $3,442.50 and `(CLW B 10)` $2,587.00 shown; both class M models left them blank.
- **Symptom:** i1040s8812 p. 5, Credit Limit Worksheet B, line 6: "leave lines 7 through 10 blank, enter -0- on line 11,
  and go to line 12" (line 2 under $5,100, or line 5 at least line 1).
- **Where:** `forms/2025/s8812.yaml`, `s8812.clwb_7` to `s8812.clwb_10`.
- **Fix:** `shown_when: s8812.clwb_to7` (Worksheet B completed, line 2 $5,100 or more, line 5 less than line 1).
  Regression `stage21.t067.s8812_clwb_line6_blank`.
- **Tags:** skipped-line-shown; value-neutral; caught-by-source-adjudication

## BUG-0211 — A child placed for adoption had no relationship value

- **Date:** 2026-10-30
- **Caught by:** the section completeness-review experiment (`docs/2026-10-30_completeness_experiment/`, D1; dependents
  claim 5, EIC claim 9), adjudicated. Witness: stage9.eic.one_child.line5 with the child entered as `other`, as the
  question's wording invites for a child placed but not yet adopted: head of household refused and line 27a $0 instead
  of $3,261.
- **Symptom:** `dependent.relationship`'s `child` read "son, daughter, stepchild, foster child or their descendant";
  i1040gi pp. 20 and 43: "An adopted child is always treated as your own child. An adopted child includes a child
  lawfully placed with you for legal adoption."
- **Where:** `forms/2025/dependent.yaml`, `dependent.relationship`.
- **Fix:** the `child` gloss names an adopted child, including one lawfully placed for legal adoption, as your son or
  daughter (with BUG-0214).
- **Tags:** question-incomplete; definition-omitted; caught-by-completeness-review

## BUG-0212 — "Full-time student" was asked without its definition

- **Date:** 2026-10-30
- **Caught by:** the completeness-review experiment (D2; dependents claim 3, EIC claim 7), adjudicated. Witness: the
  stage9 one-child case with the child aged 20: yes gives line 27a $4,324, no gives $0.
- **Symptom:** `dependent.student` asked "Was this person a full-time student in 2025?"; i1040gi p. 21 defines the term
  (5 calendar months; on-farm courses count; on-the-job, correspondence and Internet-only schools do not).
- **Where:** `forms/2025/dependent.yaml`, `dependent.student`.
- **Fix:** the question states the definition, quoting p. 21.
- **Tags:** question-incomplete; definition-omitted; caught-by-completeness-review

## BUG-0213 — No rule for a child presumed kidnapped

- **Date:** 2026-10-30
- **Caught by:** the completeness-review experiment (D3; dependents claim 1, EIC claim 11), adjudicated.
- **Symptom:** i1040gi p. 21, Kidnapped child: such a child may be taken into account for head of household, the child
  tax credit, the credit for other dependents and the EIC (Pub. 501; Pub. 596). The months and residency questions
  listed absences without it, so the child failed the residency tests and the filer lost the credits.
- **Where:** `forms/2025/dependent.yaml`.
- **Fix:** a screen `dependent.kidnapped` refusing `dependent.lived_half` and `dependent.eic_child` (Pub. 501's
  conditions are not encoded); asked of every dependent; the generator answers no. Regression
  `stage21.d3.kidnapped_child_refused`.
- **Tags:** scope-screen-missing; caught-by-completeness-review

## BUG-0214 — "Foster child" was asked without the placement requirement

- **Date:** 2026-10-30
- **Caught by:** the completeness-review experiment (D4; dependents claim 4, EIC claim 8), adjudicated. Witness: a child
  in the filer's care without an agency or court placement entered as `child` gets the qualifying-child path (EIC
  $4,324 and the child tax credit).
- **Symptom:** i1040gi p. 21: "A foster child is any child placed with you by an authorized placement agency or by
  judgment, decree, or other order of any court of competent jurisdiction."
- **Where:** `forms/2025/dependent.yaml`, `dependent.relationship`.
- **Fix:** the gloss names an eligible foster child with that placement and routes a child in your care without it to
  `household_member` or `other` (with BUG-0211).
- **Tags:** question-incomplete; definition-omitted; caught-by-completeness-review

## BUG-0215 — A child's SSN valid only with DHS authorization was not qualified

- **Date:** 2026-10-30
- **Caught by:** the completeness-review experiment (D6; dependents claim 6), adjudicated.
- **Symptom:** i1040gi p. 22: with "Valid for Work Only With DHS Authorization" on the card, "your child has the required
  SSN only as long as the DHS authorization is valid"; `dependent.work_ssn` did not say so (`dependent.eic_ssn` did).
  A yes with lapsed authorization gave line 19 $2,200 where the source gives $500.
- **Where:** `forms/2025/dependent.yaml`, `dependent.work_ssn`.
- **Fix:** the question carries the condition.
- **Tags:** question-incomplete; caught-by-completeness-review

## BUG-0216 — TANF used to support a person was not counted as the filer's support

- **Date:** 2026-10-30
- **Caught by:** the completeness-review experiment (D7; dependents claim 2), adjudicated.
- **Symptom:** i1040gi p. 21 refers to Pub. 501, which (p501 p. 20) treats TANF and similar payments used to support
  another person as support the filer provided; `dependent.supported` gave no guidance, so a filer could answer no and
  lose a qualifying relative (the $500 credit and possibly head of household).
- **Where:** `forms/2025/dependent.yaml`, `dependent.supported`.
- **Fix:** the question says such payments count as support you provided.
- **Tags:** question-incomplete; caught-by-completeness-review

## BUG-0217 — "Permanently and totally disabled" was asked without its definition

- **Date:** 2026-10-30
- **Caught by:** the completeness-review experiment (D9; EIC claim 10), adjudicated.
- **Symptom:** i1040gi p. 21 (and p. 44) defines the term (no substantial gainful activity, and a doctor's
  determination); `dependent.disabled` used the term alone, and a yes removes the age limit for the qualifying child,
  the EIC and head of household.
- **Where:** `forms/2025/dependent.yaml`, `dependent.disabled`.
- **Fix:** the question states the definition, quoting p. 21.
- **Tags:** question-incomplete; definition-omitted; caught-by-completeness-review

## BUG-0218 — Closure: BUG-0095, BUG-0096 and BUG-0097 were fixed in a65e6af

- **Date:** 2026-10-30
- **Caught by:** the adjudication of the completeness-review experiment (note N1): the three entries still read "Fix:
  open (owner's decision 2026-10-22)".
- **Symptom:** the inventory did not record the fixes.
- **Where:** `BUG_INVENTORY.md`.
- **Fix:** recorded here (the inventory is append-only). `a65e6af` ("Integrity plan Phase 1, second batch"): BUG-0095 by
  `dependent.claimed_no_tin`; BUG-0096 by `person.eic_ssn` and `household.all_eic_ssn`; BUG-0097 by
  `household.credit_disallowed`.
- **Tags:** closes-earlier-entry

## BUG-0219 — A qualifying surviving spouse filing status was never tested

- **Date:** 2026-10-30
- **Caught by:** the standing section completeness review of dependent and household, adjudicated (PENDING-1). Witness:
  stage5.return.owed, a single filer switched to qss: tax $18,500 becomes $10,350, with no refusal.
- **Symptom:** `f1040.status` accepted `qss` with no test of the conditions; i1040gi p. 15: "You can check the
  'Qualifying surviving spouse' box ... if all of the following apply. 1. Your spouse died in 2023 or 2024 and you
  didn't remarry before the end of 2025. 2. You have a child or stepchild (not a foster child) whom you can claim as a
  dependent ..." Head of household had `household.hoh_eligible` and `household.hoh_fails`; qss had neither.
- **Where:** `forms/2025/household.yaml`, `forms/2025/f1040.yaml`.
- **Fix:** `household.qss_eligible` asks the five tests; `household.qss_fails` (status qss and the answer no) refuses at
  `f1040.line12e`. Regressions `stage21.pending1.single_claims_qss_refused` and `stage21.pending1.qss_valid_computes`.
- **Tags:** scope-screen-missing; amount-affecting; caught-by-completeness-review

## BUG-0220 — A registered domestic partner's community income was neither asked nor refused

- **Date:** 2026-10-30
- **Caught by:** the standing section completeness review of dependent and household, adjudicated (PENDING-2). Witness:
  audit.household.single_community_property, single, wages $215,300: no refusal.
- **Symptom:** i1040gi p. 23: "A registered domestic partner in Nevada, Washington, or California must generally report
  half the combined community income of the individual and their domestic partner." The only community property gate
  needed a married head of household filer, so the whole $215,300 was reported where the source reports half the
  combined income.
- **Where:** `forms/2025/household.yaml`; `forms/2025/f1040.yaml`.
- **Fix:** `household.rdp` asks about registered domestic partnership; `household.rdp_community_property` (not mfj,
  community property and rdp all yes) refuses at `f1040` with the Form 8958 / Pub. 555 remedy. Regression
  `stage21.pending2.rdp_community_income_refused`.
- **Tags:** scope-screen-missing; amount-affecting; caught-by-completeness-review

## BUG-0221 — A former spouse and relatives by an ended marriage were not covered by the relationship gloss

- **Date:** 2026-10-30
- **Caught by:** the standing section completeness review of dependent and household, adjudicated (PENDING-3 and
  PENDING-5). Witness: stage8.hoh.parent.test1 filed single, `household_member`, 12 months: line 19 $500, the source
  gives $0.
- **Symptom:** p501 p. 19: "If at any time during the year the person was your spouse, that person can't be your
  qualifying relative." and "Any of these relationships that were established by marriage aren't ended by death or
  divorce." The `household_member` gloss said only "other than your spouse", so a spouse divorced in 2025 passed; a
  former in-law was entered as `other`.
- **Where:** `forms/2025/dependent.yaml`, `dependent.relationship`.
- **Fix:** The `household_member` gloss excludes a person who was your spouse at any time during 2025; the `in_law`
  gloss includes a relationship begun by a marriage since ended by death or divorce.
- **Tags:** question-incomplete; definition-omitted; caught-by-completeness-review

## BUG-0222 — A rest home was not said to count as a parent's main home

- **Date:** 2026-10-30
- **Caught by:** the standing section completeness review of dependent and household, adjudicated (PENDING-6). Witness:
  stage8.hoh.parent.test1: `parent_home_paid` yes gives head of household (line 16 $14,378); no, the literal answer of a
  filer paying a care home, gives the refusal `household.hoh_fails`.
- **Symptom:** p501 p. 9: "If you pay more than half the cost of keeping your parent in a rest home or home for the
  elderly, that counts as paying more than half the cost of keeping up your parent's main home."
  `dependent.parent_home_paid` asked about "a home that was their main home" only.
- **Where:** `forms/2025/dependent.yaml`, `dependent.parent_home_paid`.
- **Fix:** The question states that a rest home or home for the elderly counts as the parent's main home if you paid
  over half the cost of keeping your parent there.
- **Tags:** question-incomplete; definition-omitted; caught-by-completeness-review

## BUG-0223 — The support questions omitted Pub. 501's support rules

- **Date:** 2026-10-30
- **Caught by:** the standing section completeness review of dependent and household, adjudicated (PENDING-8, five
  claims). Witness: stage8.hoh.parent.test1 single, `supported` yes $500, no $0.
- **Symptom:** p501 pp. 19-20: "A person's own funds aren't support unless they are actually spent for support."; "For
  lodging, the amount of support is the fair rental value of the lodging."; "Payments you receive for the support of a
  foster child from a child placement agency are considered support provided by the agency." `dependent.supported` had
  only the TANF sentence and `dependent.self_support` none.
- **Where:** `forms/2025/dependent.yaml`, `dependent.supported` and `dependent.self_support`.
- **Fix:** Both questions carry the rules: own funds count only if spent for support, lodging at fair rental value, both
  parts of a military allotment as the filer's, agency payments and support the child paid for with the child's wages
  are not the filer's.
- **Tags:** question-incomplete; definition-omitted; caught-by-completeness-review

## BUG-0224 — The care-expense question omitted the definition of care

- **Date:** 2026-10-30
- **Caught by:** the standing section completeness review of dependent and household, adjudicated (PENDING-9, five
  claims). Witness: stage15.f2441.s2, $2,000 of each $3,500 being kindergarten tuition: line 11 $1,200 as computed, $600
  by the source.
- **Symptom:** i2441 p. 2: "It doesn't include the cost of food, lodging, education, clothing, or entertainment."; "But
  don't include any expenses for sending your child to an overnight camp, a summer school, or a tutoring program."
  `dependent.dc_paid` excluded only prior-year and 2026 care, reimbursements, ineligible providers and medical expenses.
- **Where:** `forms/2025/dependent.yaml`, `dependent.dc_paid`.
- **Fix:** The exclusion list adds food, lodging, education (never kindergarten or above), clothing, entertainment,
  camp, summer school, tutoring, out-of-home care under 8 hours a day, and a non-compliant care center.
- **Tags:** question-incomplete; definition-omitted; amount-affecting; caught-by-completeness-review

## BUG-0225 — An expired, unrenewed ITIN answered the TIN question yes

- **Date:** 2026-10-30
- **Caught by:** the standing section completeness review of dependent and household, adjudicated (PENDING-10). Witness:
  stage8.hoh.parent.test1 single: `tin` yes gives line 19 $500; no, correct for an expired ITIN, gives the refusal
  `dependent.claimed_no_tin`.
- **Symptom:** p503 p. 3: "If your ITIN wasn't included on at least one U.S. federal tax return for the last 3
  consecutive tax years, it expires on December 31 of the third consecutive tax year, and must be renewed before being
  used again on a U.S. federal tax return." An expired ITIN was issued, so the questions answered yes.
- **Where:** `forms/2025/dependent.yaml`, `dependent.tin`; `forms/2025/person.yaml`, `person.tin`.
- **Fix:** Both questions say an expired ITIN counts only if it has been renewed, or renewal applied for, by the due
  date; the locators cite p503 p. 3.
- **Tags:** question-incomplete; caught-by-completeness-review

## BUG-0226 — The Form 1098-T exception omitted the cooperation condition

- **Date:** 2026-10-30
- **Caught by:** the standing section completeness review of dependent and household, adjudicated (PENDING-11). Witness:
  stage19.example.jack_kay: `edu_1098t` yes gives line 30 $2,500, no gives $0.
- **Symptom:** i8863 p. 1: "You must fully cooperate with the educational institution's efforts to gather the
  information needed to furnish the Form 1098-T." The exception required only a request after February 2, 2026 and proof
  of enrollment and payments.
- **Where:** `forms/2025/dependent.yaml`, `dependent.edu_1098t`; `forms/2025/person.yaml`, `person.edu_1098t`.
- **Fix:** Both exceptions add that the filer fully cooperated with the institution's efforts to furnish the form; the
  locators quote i8863 p. 1.
- **Tags:** question-incomplete; caught-by-completeness-review

## BUG-0227 — Sports, hobby and noncredit courses were not excluded from education expenses

- **Date:** 2026-10-30
- **Caught by:** the standing section completeness review of dependent and household, adjudicated (PENDING-12). Witness:
  stage19.example.jack_kay: `edu_inst` $4,300 gives line 30 $2,500; $3,300 without a $1,000 hobby course gives $2,325
  (line 29 falls from $1,000 to $930).
- **Symptom:** i8863 p. 4: "Any course or other education involving sports, games, or hobbies, or any noncredit course,
  unless such course or other education is part of the student's degree program or (for the lifetime learning credit
  only) helps the student acquire or improve job skills." `edu_inst` excluded personal expenses, expenses deducted
  elsewhere and tax-free distributions only.
- **Where:** `forms/2025/dependent.yaml`, `dependent.edu_inst`; `forms/2025/person.yaml`, `person.edu_inst`.
- **Fix:** Both questions exclude such a course unless it is part of the degree program or, where the student cannot get
  the American opportunity credit, helps acquire or improve job skills.
- **Tags:** question-incomplete; definition-omitted; amount-affecting; caught-by-completeness-review

## BUG-0228 — The divorced-parents question could be read as not applying to the custodial parent

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-0-1).
- **Symptom:** i1040gi p. 20: "If conditions (1) through (4) apply, only the noncustodial parent can claim the child for
  purposes of the child tax credit and credit for other dependents." The example was written from the noncustodial side,
  so a custodial parent who signed Form 8332 could answer no and `dependent.qualifying_child` (residency, age,
  relationship tests only) stayed true, claiming the CTC/ODC on both returns.
- **Where:** `forms/2025/dependent.yaml`, `dependent.divorced_rule`.
- **Fix:** The question says to answer yes whether you are the custodial parent who signed the release (or whose decree
  or agreement lets the other parent claim the child) or the noncustodial parent using it.
- **Tags:** question-wording; amount-affecting; caught-by-screen-review

## BUG-0229 — A joint return filed after the person's death could be answered no to both marriage questions

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-0-2).
- **Symptom:** i1040gi p. 21: "If the person is married and files a joint return, you can't claim that person as your
  dependent." A would-be dependent who died in 2025 while married, included in the surviving spouse's joint return, was
  read as "not filing"; `dependent.married` and `dependent.joint_return` both gave no.
- **Where:** `forms/2025/dependent.yaml`, `dependent.married` and `dependent.joint_return`.
- **Fix:** Both ask whether a joint return is being filed for 2025 that includes this person, including one filed by
  this person's surviving spouse after this person died.
- **Tags:** question-wording; caught-by-screen-review

## BUG-0230 — The 2024 state tax refund screen covered only a late estimated payment

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-0-3).
- **Symptom:** p525 p. 24: "If you receive a refund or other recovery that is for amounts you paid in 2 or more separate
  years, you must allocate, on a pro rata basis, the recovered amount between the years in which you paid it."
  `refund.not_2024` asked only about a last estimated payment made in 2025, so an extension or balance-due payment
  answered no and the whole refund ran through the 2024 recovery worksheet.
- **Where:** `forms/2025/refund.yaml`, `refund.not_2024` and its refusal.
- **Fix:** The question asks whether any of the 2024 state or local income tax was paid in 2025 (a last estimated
  payment, a payment with an extension, or a balance due); the refusal text matches.
- **Tags:** scope-screen-narrower-than-line; amount-affecting; caught-by-screen-review

## BUG-0231 — Shares of a metals trust were not reached by the collectibles question

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-0-4).
- **Symptom:** i1040sd p. 11, line 18: "Include on the worksheet any gain (but not loss) from the sale or exchange of an
  interest in a partnership, S corporation, or trust held for more than 1 year and attributable to unrealized
  appreciation of collectibles." A holder of exchange-traded shares of a physically backed gold trust thinks of the sale
  as a stock sale and answers no, so the gain is taxed at 0/15/20% instead of through the 28% Rate Gain Worksheet.
- **Where:** `forms/2025/sales.yaml`, `sales.special`.
- **Fix:** The question names shares of an exchange-traded fund or trust that holds gold, silver, platinum or other
  metals; the locator quotes i1040sd p. 11.
- **Tags:** question-incomplete; definition-omitted; amount-affecting; caught-by-screen-review

## BUG-0232 — Form 8615 was named in the screen by number only

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-0-5).
- **Symptom:** i1040gi p. 36: "You must file Form 8615 if you meet all of the following conditions. 1. You had more than
  $2,700 of unearned income ... 4. At least one of your parents was alive at the end of 2025. 5. You don't file a joint
  return in 2025." A 16-year-old with $10,000 of dividends, not already preparing the form, answered no and was taxed at
  the child's own rates.
- **Where:** `forms/2025/scope.yaml`, `scope.other_line16`.
- **Fix:** The question states the Form 8615 conditions (unearned income over $2,700, required to file, not filing
  jointly, a parent alive at the end of 2025, and the age or student and support tests).
- **Tags:** question-incomplete; definition-omitted; amount-affecting; caught-by-screen-review

## BUG-0233 — "Clergy income" was undefined in the Schedule 1 screen

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-0-6).
- **Symptom:** i1040gi p. 43, Clergy: "The following instructions apply to ministers, members of religious orders who
  have not taken a vow of poverty, and Christian Science practitioners." A member of a religious order paid on Form W-2
  with no Schedule C read "clergy income" as ministers only; `person.se_screen` names all three groups but is reached
  only with a Schedule C.
- **Where:** `forms/2025/scope.yaml`, `scope.schedule1`.
- **Fix:** The question names the three groups, matching `person.se_screen`; the locator quotes i1040gi p. 43.
- **Tags:** question-incomplete; definition-omitted; caught-by-screen-review

## BUG-0234 — The kidnapped-child question said "your child" and was in the present tense

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-1-1).
- **Symptom:** p501 p. 13: "In the year of the child's return, the child lived with you for more than half the part of
  the year following the date of the child's return." A child returned before the interview, or a household member child
  (p501 p. 18: "You can treat a child as your qualifying relative even if the child has been kidnapped"), drew a
  truthful no, so the credits were understated.
- **Where:** `forms/2025/dependent.yaml`, `dependent.kidnapped`.
- **Fix:** The question asks about a child who at any time during 2025 was presumed kidnapped by someone who is not a
  member of your family or the child's family, even if since returned (Pub. 501's phrase). The refusal stays on
  `dependent.lived_half` and `dependent.eic_child` (BUG-0213); `dependent.qr_relationship` was not given a refusal.
- **Tags:** question-wording; caught-by-screen-review

## BUG-0235 — The joint-occupancy question read as a condition on the other occupant filing

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-1-3). Witness (write-up case): filer and
  housemate each pay $2,000 for windows, housemate does not file: line 30 windows credit $600, allocable share $300.
- **Symptom:** i5695 p. 3: "If the aggregate credit that would be allowed to all occupants for any item of property
  exceeds the credit limit below, then you must figure your allocable share ... The denominator is the total amount paid
  by you and all other occupants." The clause "so that each occupant completes their own Form 5695 for the same
  property" read as a condition, so the filer answered no and over-claimed by $300.
- **Where:** `forms/2025/f5695.yaml`, `f5695.joint_occupancy`.
- **Fix:** The question asks about joint occupancy with someone other than a spouse on a joint return, whether or not
  the other occupant files Form 5695 and whether the items paid for are the same or different; the neighbor
  parenthetical is kept.
- **Tags:** question-wording; amount-affecting; caught-by-screen-review

## BUG-0236 — The Archer MSA screen covered only contributions by the filer or the employer

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-1-4).
- **Symptom:** f8889 p. 1, line 4: "If you or your spouse had family coverage under an HDHP at any time during 2025,
  also include any amount contributed to your spouse's Archer MSAs." The screen read as contributions by you or your
  employer, so a spouse's employer contribution answered no, `f8889.line4` stayed zero and the HSA deduction could be
  overstated.
- **Where:** `forms/2025/f8889.yaml`, `f8889.unsupported`.
- **Fix:** The question says any contribution by anyone to the spouse's Archer MSA when you or your spouse had family
  HDHP coverage; the locator quotes f8889 p. 1.
- **Tags:** scope-screen-narrower-than-line; amount-affecting; caught-by-screen-review

## BUG-0237 — A policy whose Form 1095-A went to the other tax family was not reached by the allocation screen

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-1-5).
- **Symptom:** i8962 p. 12: "The other tax family received a Form 1095-A for the policy that includes a member of your
  tax family"; example: "your ex-spouse enrolled a child whom you are claiming as a dependent". A filer holding only
  their own Form 1095-A read the question as the forms held and answered no, leaving the child's premiums, SLCSP and
  APTC out of lines 24 and 25 and understating the excess APTC.
- **Where:** `forms/2025/f8962.yaml`, `f8962.alloc`.
- **Fix:** The question asks about any Marketplace policy, including one whose Form 1095-A went only to someone else,
  and adds a child you claim whom someone else enrolled.
- **Tags:** question-incomplete; amount-affecting; caught-by-screen-review

## BUG-0238 — The premium-payment screen ignored the unextended due date and the appeal 120-day rule

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-1-6).
- **Symptom:** i8962 p. 3: "paid by the due date of your tax return (not including extensions)" and, for retroactive
  enrollment after an appeal, "must be paid on or before the 120th day following the date of the appeals decision." A
  premium paid between the unextended and extended dates, or after the 120th day, answered no and the month computed as
  a coverage month.
- **Where:** `forms/2025/f8962.yaml`, `f8962.other`.
- **Fix:** The question says the due date of your return, not including extensions, and gives the 120th day after the
  appeals decision for coverage enrolled in retroactively.
- **Tags:** question-incomplete; amount-affecting; caught-by-screen-review

## BUG-0239 — "Similar items" of donated property was undefined

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-1-7).
- **Symptom:** i8283 p. 3: "Similar items of property are items of the same general category or type, such as coin
  collections, paintings, books, clothing, jewelry, nonpublicly traded stock, land, or buildings." Two paintings of
  $3,000 each entered as two groups never reached `gift.section_b` (a group over $5,000), so $6,000 passed without
  Section B or a qualified appraisal.
- **Where:** `forms/2025/gift.yaml`, `gift.deduction` and `gift.special`.
- **Fix:** Both carry the definition of similar items quoted from i8283 p. 3.
- **Tags:** question-incomplete; definition-omitted; amount-affecting; caught-by-screen-review

## BUG-0240 — The alimony screen named only child support as a non-alimony part

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-1-8).
- **Symptom:** p504 p. 13: "Alimony doesn't include: Child support, Noncash property settlements, Payments that are your
  spouse's part of community income ..., Payments to keep up the payer's property, or Use of the payer's property." and,
  for a jointly owned home, "see Table 4" (half the mortgage payments are alimony). A payer of the whole mortgage, or of
  a payment reduced at a child's age, answered no and entered the whole payment as alimony.
- **Where:** `forms/2025/s1.yaml`, `s1.alimony_unsupported`, `s1.alimony_received`, `s1.alimony_paid`.
- **Fix:** The screen adds payments for a home either of you owns and amounts reduced on a contingency relating to a
  child; the two amount questions say cash payments only and exclude child support, noncash settlements, community
  income and the payer's property.
- **Tags:** scope-screen-narrower-than-line; amount-affecting; caught-by-screen-review

## BUG-0241 — The EIC age test had no screen for a death in 2025

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-1-9; sa.dependent finding 1).
- **Symptom:** i1040gi p. 42, EIC Step 4 question 2: "If your spouse died in 2025 or if you are preparing a return for
  someone who died in 2025, see Pub. 596 before you answer." `eic.age_range` read the birth-date flags only and no
  screen asked about a death; Pub. 596 is not archived, so the rule itself is unconfirmed here.
- **Where:** `forms/2025/eic.yaml`.
- **Fix:** A new screen `eic.died_2025` refuses `eic.age_range` with the Pub. 596 referral. Regression
  `stage21.pending.eic_death_pub596_refused`. It closes the substance of T-037.
- **Tags:** scope-screen-missing; amount-affecting; caught-by-screen-review

## BUG-0242 — The RMD shortfall question missed a partial or late-corrected distribution

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-2-1).
- **Symptom:** f5329 p. 3, Part IX: "Complete this part if you did not receive the minimum required distribution from
  your qualified retirement plan." i5329 p. 9: "The additional tax is 25% of the excess accumulation, which is the
  difference between the amount that was required to be distributed and the amount that was actually distributed." A
  filer who took $8,000 of a $10,000 RMD answered no to "did not take", and the excise tax was missing from Schedule 2
  line 8.
- **Where:** `forms/2025/person.yaml`, `person.x_other`.
- **Fix:** The last item reads a required minimum distribution "that you did not receive in full by its deadline
  (including a shortfall you made up later)"; the locator quotes f5329 p. 3 and i5329 p. 9.
- **Tags:** scope-screen-narrower-than-line; amount-affecting; caught-by-screen-review

## BUG-0243 — The retirement screen omitted the military disability, beneficiary and property-rollover cases

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-2-2).
- **Symptom:** i1040gi p. 28: "For details on military disability pensions, see Pub. 525." p. 30: "If you are the
  beneficiary of an employee who died, see Pub. 575. If there is more than one beneficiary, see Pub. 575 or Pub. 721 to
  figure each beneficiary's taxable amount." These cases answered no and computed as a plain cash rollover or with the
  whole cost entered.
- **Where:** `forms/2025/retirement.yaml`, `retirement.special`.
- **Fix:** The list adds a military disability pension, an annuity received as beneficiary of an employee who died or
  shared among beneficiaries, and a rollover of property other than cash or of a QDRO distribution.
- **Tags:** scope-screen-narrower-than-line; caught-by-screen-review

## BUG-0244 — The canceled-debt screen reached deductible debt only as box 3 interest

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-2-3).
- **Symptom:** p4681 p. 6, Deductible Debt: "If you use the cash method of accounting, you don't realize income from the
  cancellation of debt if the payment of the debt would have been a deductible expense." An unpaid medical bill canceled
  with no box 3 interest answered no, and `s1.cod_refused` copied the whole amount to Schedule 1 line 8c.
- **Where:** `forms/2025/s1.yaml`, `s1.cod_unsupported`.
- **Fix:** The screen reads "deductible interest or other deductible debt" and the question adds any other amount that
  would have been deductible if paid, for example an unpaid medical bill.
- **Tags:** scope-screen-narrower-than-line; amount-affecting; caught-by-screen-review

## BUG-0245 — The unemployment screen did not say which contributions count

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-2-4).
- **Symptom:** i1040gi p. 89: "If you made contributions to a governmental unemployment compensation program and you
  aren't itemizing deductions, reduce the amount you report on line 7 by those contributions." A filer whose state
  unemployment share was withheld from wages, or paid in an earlier year, answered no and line 7 stayed overstated.
- **Where:** `forms/2025/s1.yaml`, `s1.uc_unsupported`.
- **Fix:** The question asks about contributions in 2025 or any earlier year, including amounts withheld from wages, not
  employer-paid tax or paid family leave or disability insurance contributions; the locator quotes p. 89.
- **Tags:** scope-screen-narrower-than-line; amount-affecting; caught-by-screen-review

## BUG-0246 — The foreign trust question was narrower than the Schedule B line 8 instruction

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-2-5).
- **Symptom:** i1040sb p. 3, Line 8: "For this purpose, a loan of cash or marketable securities is generally considered
  to be a distribution ... If you were the grantor of, or transferor to, a foreign trust that existed during 2025, you
  may have to file Form 3520." A grantor of a trust created earlier, or a borrower from one, answered no, printing No on
  line 8.
- **Where:** `forms/2025/sb.yaml`, `sb.line8`.
- **Fix:** The question counts a loan of cash or marketable securities as a distribution and covers a foreign trust that
  existed at any time during 2025.
- **Tags:** scope-screen-narrower-than-line; caught-by-screen-review

## BUG-0247 — The business-use gloss narrowed "nonbusiness purposes"

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-3-1).
- **Symptom:** i5695 p. 1, Costs: "If less than 80% of the use of an item is for nonbusiness purposes, only that portion
  of the costs that is allocable to the nonbusiness use can be used to determine either credit." The parenthetical "(is
  more than 20% of its use for a business)" read as excluding renting out part of the home, so the full cost stayed in
  line 6a and line 30.
- **Where:** `forms/2025/f5695.yaml`, `f5695.business_use`.
- **Fix:** The parenthetical adds "for renting out or for another income-producing purpose"; the IRS clause is kept.
- **Tags:** question-wording; amount-affecting; caught-by-screen-review

## BUG-0248 — "A disposition adjustment" did not reach NUA gain in the net investment income screen

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-3-2).
- **Symptom:** i8960 p. 9, line 5b: "Any gain attributable to NUA (within the meaning of section 402(e)(4)) that you
  realize on a disposition of employer securities held by a qualified plan is a distribution within the meaning of
  section 1411(c)(5) and isn't included in NII." A filer selling employer stock with NUA did not recognize it as a
  disposition adjustment; `f8960.line5b` is a fixed zero, so the gain stayed in NII (inferred from the expressions, not
  run).
- **Where:** `forms/2025/f8960.yaml`, `f8960.unsupported`.
- **Fix:** The clause is glossed: a disposition adjustment (Form 8960 line 5b or 5c, for example NUA gain on employer
  securities from a qualified plan, or the sale of business property or a partnership or S corporation interest); the
  locator quotes i8960 p. 9.
- **Tags:** scope-screen-narrower-than-line; amount-affecting; caught-by-screen-review

## BUG-0249 — The September 11 fund clause required coverage rather than eligibility

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (PENDING-3-4).
- **Symptom:** i1040gi p. 31, Disability payments: "In the case of the September 11 attacks, injuries eligible for
  coverage by the September 11 Victim Compensation Fund are treated as incurred as a direct result of the attack." A
  filer with an eligible injury who never filed a claim read "covered by" as "compensated by" and answered no, so
  excludable benefits stayed in `ssb.line1`.
- **Where:** `forms/2025/ssb.yaml`, `ssb.terror_disability`.
- **Fix:** The parenthetical reads "for the September 11 attacks, any injury eligible for coverage by the September 11
  Victim Compensation Fund, whether or not you made a claim".
- **Tags:** question-wording; amount-affecting; caught-by-screen-review

## BUG-0250 — The `child` gloss's routing sentence could be read to cover a related child

- **Date:** 2026-10-30
- **Caught by:** the log adjudication of dependent (Q1; `.transcription/proposed/dfix/dependent.findings.md`).
  Introduced by BUG-0214.
- **Symptom:** The BUG-0214 sentence "a child in your care without such a placement is entered as household_member or
  other" read literally covers a grandchild, niece or nephew in the filer's care, who is a `child` or `sibling`
  descendant under i1040gi p. 17, Step 1 ("or a descendant of any of them (for example, your grandchild, niece, or
  nephew)"). Entering `household_member` drops the qualifying-child path: the CTC, EIC and head of household Test 2 are
  lost. No witness; a wording risk.
- **Where:** `forms/2025/dependent.yaml`, `dependent.relationship`.
- **Fix:** The sentence now reads "a child in your care without such a placement who is not otherwise your relative is
  entered as household_member or other".
- **Tags:** question-wording; caught-by-review

## BUG-0251 — The business-income-tax refund screen asked only about Form 1099-G box 8

- **Date:** 2026-10-30
- **Caught by:** the standing screen review (T-088), adjudicated (`reviews/2025/screens/adjudication/group3.md`,
  PENDING-3-3); left out of the first fix round because the group's JSON did not list it.
- **Symptom:** `refund.box8` asked whether box 8 was checked on a Form 1099-G, but `refund.received` includes refunds with
  no Form 1099-G (i1040gi p. 88, "Report any taxable refund you received even if you didn't receive Form 1099-G"); a
  Schedule C filer refunded a business-only income tax without one answered no, and the refund went through the
  itemized-deduction worksheet instead of Schedule C (f1099g p. 5, Box 8, "If taxable, report the amount in box 2 on
  Schedule C or F").
- **Where:** `forms/2025/refund.yaml`, `refund.box8`.
- **Fix:** the question asks whether any refund is of a state or local income tax that applies only to trade or business
  income, box 8 being an example, including one with no Form 1099-G.
- **Tags:** scope-screen-narrower-than-line; caught-by-screen-review

## BUG-0252 — The support questions omitted the scholarship and state-support rules

- **Date:** 2026-10-30
- **Caught by:** the standing completeness review of `dependent`, round 2, adjudicated (`reviews/2025/completeness/r2.findings.md`,
  PENDING-r2-1). Witness: jack_kay with the student earning $8,000: a yes to self-support drops $500, $1,000 and $1,500 of
  credits to $0.
- **Symptom:** p501 p. 15, "A scholarship received by a student isn't taken into account in determining whether the student
  provided more than half of their own support"; p501 p. 20, benefits provided by the state to a needy person are support
  provided by the state. `dependent.self_support` and `dependent.supported` (reworded in BUG-0223) did not say so.
- **Where:** `forms/2025/dependent.yaml`, `dependent.self_support`, `dependent.supported`.
- **Fix:** both questions state the rules, quoting p501 pp. 15, 20 and 21.
- **Tags:** question-incomplete; definition-omitted; caught-by-completeness-review

## BUG-0253 — Gross income for the qualifying-relative test was asked without its definition

- **Date:** 2026-10-30
- **Caught by:** the completeness review of `dependent`, round 2 (PENDING-r2-2). Witness: a parent with gross rents: entering
  net rent of $4,000 passes the $5,200 test and gives head of household and the $500 credit, where the gross amount refuses.
- **Symptom:** p501 p. 19 defines gross income ("all income in the form of money, property, and services that isn't exempt
  from tax"), counting gross rents and a partner's share of gross income; `dependent.gross_income` gave no definition.
- **Where:** `forms/2025/dependent.yaml`, `dependent.gross_income`.
- **Fix:** the question states the definition and its inclusions and exclusions, quoting p501 p. 19.
- **Tags:** question-incomplete; definition-omitted; caught-by-completeness-review

## BUG-0254 — A pre-2019 alimony agreement changed in 2025 lost the payments made before the change

- **Date:** 2026-10-30
- **Caught by:** the fix-round-2 adjudication of `s1` (`.transcription/proposed/fixr2/s1.findings.md`, F1). Witness: line 2a
  $0 instead of $5,000; tax $1,475 instead of $2,075.
- **Symptom:** the `s1.alimony` screen counted alimony only under an agreement "not changed after 2018"; p504 p. 16, Example 2:
  "The alimony payments made in January 2025 through May 2025 are includible in the recipient’s income and deductible from
  the payer’s income."
- **Where:** `forms/2025/s1.yaml`, `s1.alimony`.
- **Fix:** the question counts the payments made before any post-2018 change that excludes alimony from income.
- **Tags:** question-wrong; caught-by-source-adjudication

## BUG-0255 — The alimony-received question said "your spouse's part of community income"

- **Date:** 2026-10-30
- **Caught by:** the fix-round-2 adjudication of `s1` (F2); introduced by BUG-0240's rewording, which copied the payer's wording.
- **Symptom:** for a recipient the excluded amount is the recipient's own part of community income.
- **Where:** `forms/2025/s1.yaml`, `s1.alimony_received`.
- **Fix:** "your own part of community income".
- **Tags:** question-wrong; value-neutral; caught-by-source-adjudication

## BUG-0256 — A pending ITIN renewal satisfied the child tax credit's other-spouse test

- **Date:** 2026-10-30
- **Caught by:** the fix-round-2 adjudication of `person` (`.transcription/proposed/fixr2/person.findings.md`, F1); introduced
  by BUG-0225's mirror of the dependent wording. Witness: stage13.ctc_spouse_ssn, line 19 $2,200 where the chosen reading gives $0.
- **Symptom:** `person.tin` said an expired ITIN counts if "renewed, or renewal applied for"; the child tax credit's
  other-spouse test needs an ITIN issued by the due date, and `amb.2025.ctc_spouse_itin_application` excludes an application.
- **Where:** `forms/2025/person.yaml`, `person.tin`.
- **Fix:** an expired ITIN counts only if renewed by the due date; a renewal only applied for does not (`dependent.tin`, read
  by the credit for other dependents, keeps the application).
- **Tags:** question-wrong; reused-question; caught-by-source-adjudication

## BUG-0257 — An unanswered refusal gate let a count's lower bound decide a test, completing the return

- **Date:** 2026-10-30
- **Caught by:** the fix-round-2 adjudication of `sales` (`.transcription/proposed/fixr2/sales.findings.md`, F1), reproduced
  by the session: classm.f8889.1.deepseek with `sales[s1].special` withheld or null gave `sd.count` unknown but `sd.screen`
  false, and the return completed (line 7a −$3,000, line 16 $18,089.13), as if the collectibles screen had been answered no.
- **Symptom:** `sum_over` attached a lower bound to a partial Count, and comparisons were decided from the bound, even when an
  entry's unknown came from a refusal gate still awaiting its answer, which may yet refuse the whole sum. The same happened
  through `where` tests and nested sums (`household.test2_persons`, `eic.has_qc`, the Form 8863, 2441, 8962 and Schedule 8812
  counts, the rollover counts, `person.x_must`); `household.test2_persons` was decided in three fixture evaluations while
  `dependent.kidnapped` was unanswered.
- **Where:** `engine/src/eval.ts` and `lean/TaxFormalization/Eval.lean` (the lower-bound rule); `spec/spec.md` 4.7.5.
- **Fix:** a pending gate marks its unknown; the mark propagates through operands, sums, tests, `where` and copies; a marked
  partial count has no lower bound and no test is decided from one. Mirrored in Lean (compare 0 differing on 1990 cases);
  spec 4.7.5 states the rule and its two remaining limits (a deciding conjunct of `all`/`any`; unevaluated `choose`
  alternatives, T-093). Regressions in `fixtures/2025/stage21.json` (the four sales witnesses, two `where` witnesses, and two
  cases where the bound still decides). No existing expectation changed.
- **Tags:** evaluator-semantics; amount-affecting; caught-by-source-adjudication

## BUG-0258 — The cost of keeping up a home was asked without its definition

- **Date:** 2026-10-30
- **Caught by:** the standing completeness review of `dependent`, round 3, adjudicated (`reviews/2025/completeness/r3.findings.md`,
  PENDING-r3-1). Witness: stage8.hoh.parent.test1: yes gives head of household (line 24 $13,878); no is refused (`hoh_fails`).
- **Symptom:** i1040gi p. 15, "To find out what is included in the cost of keeping up a home, see Pub. 501"; p501 p. 9 lists
  the costs included and excluded, and treats amounts paid out of a qualifying person's own funds, such as Social Security, as
  paid by that person. `dependent.parent_home_paid` and `household.home_cost` gave no definition.
- **Where:** `forms/2025/dependent.yaml`, `dependent.parent_home_paid`; `forms/2025/household.yaml`, `household.home_cost`.
- **Fix:** both questions state the included and excluded costs, and the parent's own funds rule, quoting p501 p. 9 and
  i1040gi p. 15.
- **Tags:** question-incomplete; definition-omitted; caught-by-completeness-review

## BUG-0259 — A pending renewal of an expired ITIN was not said to count for the credit for other dependents

- **Date:** 2026-10-30
- **Caught by:** the fix-round-3 adjudication of `person` (`.transcription/proposed/fixr3/person.findings.md`); the mirror of
  BUG-0256. Witness: stage13.odc_spouse_no_tin with a renewal applied for: line 19 $0 where the source gives $500.
- **Symptom:** i1040gi p. 19, Step 5, question 1, "Answer 'Yes' if you are applying for an ITIN on or before the return due
  date"; after BUG-0256 `person.tin` excludes an expired ITIN with only a renewal applied for, and `person.itin_applied` did not
  say that the renewal application counts as the application the credit for other dependents accepts.
- **Where:** `forms/2025/person.yaml`, `person.itin_applied`.
- **Fix:** the question asks about an application for an ITIN or for the renewal of an expired one by the due date.
- **Tags:** question-incomplete; caught-by-source-adjudication

## BUG-0260 — The household home-cost questions lacked the own-funds rule and, for QSS, the definition

- **Date:** 2026-10-30
- **Caught by:** the completeness review of `household`, round 4 (`reviews/2025/completeness/r4.findings.md`, PENDING-r4-1), and
  the fix-round-4 adjudication of `household` (`.transcription/proposed/fixr4/household.findings.md`, F1 and F2); a sibling
  BUG-0258 left. Witness: stage8.hoh.child.ctc: a yes that counts the child's Social Security as the filer's payment gives head
  of household (line 24 $12,153) where single gives $15,642.
- **Symptom:** p501 p. 9, Note, "Amounts paid out of funds received in the child’s or qualifying person’s name, such as Social
  Security, are considered paid by the child, not you"; BUG-0258 put the rule only on `dependent.parent_home_paid`, and the
  home-cost test inside `household.qss_eligible` had no definition at all.
- **Where:** `forms/2025/household.yaml`, `household.home_cost`, `household.qss_eligible`.
- **Fix:** both carry the cost definition and the own-funds rule, quoting p501 p. 9.
- **Tags:** question-incomplete; definition-omitted; fix-sibling-missed; caught-by-completeness-review

## BUG-0261 — A section 179 carryover with no business in 2025 was never asked

- **Date:** 2026-10-31
- **Caught by:** the refusal-fixture reachability scan (T-068, `stage14.s179.refuse_orphan`), worked in hardening.
- **Symptom:** Form 4562 was reached only through a Schedule C, so `s179.line10` (the carryover from 2024) was never asked of a
  filer with no business and `s179.orphan` could not fire; an interview with a $3,000 carryover and no Schedule C completed.
  i4562 p. 5, Line 12, puts the deduction on a business's own Form 4562, so with no business there is nowhere to take it.
- **Where:** `interview/full-2025.yaml` (targets).
- **Fix:** `s179.line13` (the carryover to 2026) is an interview target, so `s179.line10` is asked of every filer and the orphan
  carryover is refused; a Schedule C filer has line 13 reported. Regressions `stage21.t068.orphan_with_wages_refused`,
  `stage21.t068.no_business_no_carryover`.
- **Tags:** unreachable-gate; caught-by-audit

## BUG-0262 — Employer-furnished care with nothing paid made all dependent care benefits taxable

- **Date:** 2026-10-31
- **Caught by:** the round-4 adjudication of Form 2441 (`reviews/2025/transcription/adjudication/f2441.md`; T-073).
- **Symptom:** with care furnished by the employer and no expenses paid, `f2441.employer_care_gate` did not fire, line 16 was $0
  and all of W-2 box 10 became taxable (stage16 employer-care case: line 26 and Form 1040 line 1e $2,000). The archived i2441,
  Pub. 503 and the W-2 instructions do not say whether the value of employer-furnished care is a qualified expense incurred on
  line 16 (section 129 is not archived).
- **Where:** `forms/2025/f2441.yaml`.
- **Fix:** `f2441.employer_care_l16` (care furnished by the employer and line 16 less than line 15) refuses line 17 with a
  cited remedy. Regressions `stage21.t073.employer_care_nothing_paid_refused`, `stage21.t073.employer_care_paid_equals_benefits`.
- **Tags:** source-silent; refusal-added; caught-by-source-adjudication

## BUG-0263 — `person.sep_s3` lacked its ambiguity link

- **Date:** 2026-10-31
- **Caught by:** BUG-0181's follow-up (T-074).
- **Symptom:** the register entry `amb.2025.sep_loss_floor` named the line, but the line did not name the entry, so the values
  sheet printed no interpretation note.
- **Where:** `forms/2025/person.yaml`, `person.sep_s3`.
- **Fix:** `ambiguity: amb.2025.sep_loss_floor`. No value change (`stage14.sep.loss_floor` pins the reading).
- **Tags:** traceability; value-neutral

## BUG-0264 — A relative of the spouse on a joint return could not be a qualifying relative

- **Date:** 2026-10-31
- **Caught by:** the standing completeness review of `dependent`, adjudicated
  (`reviews/2025/completeness/dependent_household.findings.md`, PENDING-4; T-091 (1)). Witness: base `stage13.ctc_spouse_ssn`
  (mfj) with a person aged 30, `months` 0, not in the household: `other` gave line 19 $0 where the relationship through the
  spouse gives $500.
- **Symptom:** p501 p. 19, Joint return, "If you file a joint return, the person can be related to either you or your spouse."
  `dependent.relationship` asked only the relationship to you, and a spouse's nephew, niece, aunt or uncle fitted only `other`,
  which needs a full year in the household.
- **Root cause:** `dependent.relationship` feeds both the qualifying-child and the qualifying-relative tests; the review's
  proposed rewording would have let a spouse's relative pass the qualifying-child test, which the joint-return sentence does not
  reach.
- **Where:** `forms/2025/dependent.yaml`, `dependent.relationship`, `dependent.qr_relationship`.
- **Fix:** a new input `dependent.spouse_relative`, read only by `qr_relationship` and only on a joint return; the relationship
  question says to give the relationship to you. Regressions `stage8.t091.spouse_relative.*`.
- **Tags:** input-conflation; amount-affecting; caught-by-completeness-review

## BUG-0265 — A temporary absence counted for head of household without the expected-return condition

- **Date:** 2026-10-31
- **Caught by:** the standing completeness review of `dependent`, adjudicated
  (`reviews/2025/completeness/dependent_household.findings.md`, PENDING-7; T-091 (2)). Witness: base `stage8.hoh.parent.test1`
  with `relationship` `parent_relative` and `household.home_cost` Yes: a grandparent who moved permanently into a nursing home,
  counted at `months` 12, gave head of household (line 16 $14,378) where 0 gives the refusal `household.hoh_fails`.
- **Symptom:** p501 p. 9, Temporary absences, "It must be reasonable to assume the absent person will return to the home after
  the temporary absence. You must continue to keep up the home during the absence." `dependent.months` counted absences for
  medical care with no condition. The QSS question carried the same unconditioned list, and p501 p. 11 points QSS to this rule.
- **Root cause:** `dependent.months` served head of household and the qualifying-relative household test alike, but the
  expected-return sentence sits only under head of household, while p501 p. 19 lets an indefinite nursing-home stay count for a
  qualifying relative.
- **Where:** `forms/2025/dependent.yaml`, `dependent.months`, `dependent.hoh_test2`, `dependent.qr_relationship`;
  `forms/2025/household.yaml`, `household.qss_eligible`.
- **Fix:** a new input `dependent.absence_no_return` and gate `dependent.hoh_absence` refuse `hoh_test2` when the time lived with
  you counted such an absence; the qualifying-relative test reads a new input `dependent.qr_all_year` that counts the indefinite
  nursing-home stay; `months`, `part_year_home` and `us_half` are unchanged; `household.qss_eligible` states the condition.
  Regressions `stage8.t091.absence.*`, `stage8.t091.nursing_home.*`.
- **Tags:** input-conflation; question-incomplete; refusal-added; caught-by-completeness-review

## BUG-0266 — A kidnapped child was not refused on the qualifying-relative test

- **Date:** 2026-10-31
- **Caught by:** BUG-0234's write-up ("`dependent.qr_relationship` was not given a refusal"); T-091 (3). Witness:
  `stage8.t091.kidnapped.qr_refused`, a household-member child presumed kidnapped with `months` 0: the full-year household test
  gave line 19 $0 with no refusal.
- **Symptom:** p501 p. 18, Kidnapped child, "You can treat a child as your qualifying relative even if the child has been
  kidnapped"; the part-year rule there was not applied, and the refusal of BUG-0213 covered only the qualifying-child tests.
- **Where:** `forms/2025/dependent.yaml`, `dependent.qualifying_relative`.
- **Fix:** gate `dependent.qr_kidnapped` (kidnapped, age under 19 at the end of 2025, the safe side of p501 p. 18's "the year
  the child would have reached age 18") refuses `qualifying_relative`; the part-year rule is not encoded. Regressions
  `stage8.t091.kidnapped.*`.
- **Tags:** part-year-rule-missing; refusal-added; fix-sibling-missed; caught-by-audit

## BUG-0267 — The head-of-household absence refusal refused returns another person qualified

- **Date:** 2026-10-31
- **Caught by:** the T-091 round adjudication of `dependent` and `household` (`.transcription/proposed/t091/dependent.findings.md`
  and `household.findings.md`, L1 in each, found independently). Introduced by BUG-0265's fix before it was committed.
  Witness: `stage8.t091r.absence.second_child_clean`, two children of whom one counted an absence head of household does not
  count: lines 12e and 16 were refused at `dependent[child].hoh_absence` where the other child alone gives head of household
  (line 12e $23,625, line 16 $14,378).
- **Symptom:** i1040gi p. 14, Test 2, "in which one of the following also lived for more than half of the year": one Test 2
  person is enough. The gate refused `dependent.hoh_test2` for any entry that lived with you more than half the year and
  answered yes to the absence question, including a person who was not a Test 2 person, and `household.test2_persons` sums
  over every entry, so one entry's refusal refused the return.
- **Root cause:** the refusal sat on the per-person line, below a sum in which a refusal outranks the other entries (spec
  4.7.5, the limit kept at T-093), while whether the absence matters is a fact about the whole return.
- **Where:** `forms/2025/dependent.yaml`, `dependent.hoh_absence`, `dependent.hoh_test2`; `forms/2025/household.yaml`.
- **Fix:** `dependent.hoh_test2_lived` holds the former Test 2 expression; `dependent.hoh_test2` counts a person only without
  such an absence; `dependent.hoh_absence` marks a person who is a Test 2 person only by counting one; the return-level gate
  `household.hoh_absence` (unmarried, Test 1 not met, home cost paid, no Test 2 person, at least one such person) refuses
  `household.hoh_eligible`. Regressions `stage8.t091r.absence.*`; `stage8.t091.absence.hoh_refused` now refuses at the
  household gate.
- **Tags:** over-refusal; fix-introduced; refusal-placement; caught-by-source-adjudication

## BUG-0268 — check-all ran the checks that read the build beside the build

- **Date:** 2026-10-31
- **Caught by:** reading `tools/check_all_steps.sh` while designing the background runner (T-103).
- **Symptom:** the step list's own rule, "none reads what another of its wave writes", was broken: `build` (which writes
  `canonical/` and `rendered/`) ran in the same wave as the source-coverage checks (`check_instruction_cites.py`,
  `check_operands.py`, `check_signs.py`, `check_consumers.py`, `check_limits.py`, `check_screens.py`,
  `check_completeness.py`, all reading `canonical/`) and as `check_logs.py`, `compare_families.py` and
  `audit_skipped.py` (reading `rendered/` and `canonical/` through `subjects.py` and `classm.py`). They read whatever the
  previous build left, or a file the build was writing. A run on edited but unbuilt forms could pass those checks on the
  old data. No wrong green run is known; runs usually followed a build.
- **Where:** `tools/check_all_steps.sh`.
- **Fix:** `build` runs alone, in its own wave after `compile`; every later step sees the build of the tree under test.
  About 50 seconds longer per run (the build no longer overlaps other steps).
- **Tags:** tool-defect; race; caught-by-audit

## BUG-0269 — A merge commit bypassed the commit guard

- **Date:** 2026-10-31
- **Caught by:** the T-091 session: `git pull` made merge commit 286792c, which no check-all run tested; git runs no
  pre-commit hook on a merge and the repository had no other hook.
- **Symptom:** `docs/TRUST.md` section 11 guaranteed that "no commit lands unless the whole suite passed on that exact
  tree", but a merge commit could land, and be pushed, untested. (The tree pushed then was not affected: the next commit,
  274f913, was green and was the tip pushed.)
- **Where:** `tools/hooks/` (no pre-push or pre-merge-commit hook).
- **Fix:** `tools/hooks/pre-push` refuses a push whose commits' trees no green run tested; `tools/green.sh` keeps the last
  50 green trees of the clone (`.git/check-all-green-trees`), which both hooks accept. Owner's choice over a
  pre-merge-commit hook: it covers whatever reaches GitHub (merge, rebase, cherry-pick) and keeps `git pull` one step.
- **Tags:** tool-defect; guard-gap; caught-by-audit

## BUG-0270 — A filer with an SSN was asked whether they had applied for an ITIN

- **Date:** 2026-10-31
- **Caught by:** T-058 (cleanup pass, 2026-10-22), reproduced by a scripted interview: a single filer with wages and a
  claimed parent was asked `person[taxpayer].itin_applied` (question 115) before `person[taxpayer].tin` had been asked.
- **Symptom:** i1040gi p. 19, Step 5, question 1, asks about an ITIN application only of a filer without an SSN or ITIN.
  `household.tin_count` and the education test read `person.tin` or `person.itin_applied`; both questions had order 2, so
  the interview asked them by key, `itin_applied` first. The answer did not change a value.
- **Root cause:** a tie in the question bank's order resolved by name. T-058's trigger ("the next change to the person
  questions") fired in 34b2346 and a428e8b without the change being made.
- **Where:** `interview/questions-2025.yaml`, `person.itin_applied`.
- **Fix:** `person.itin_applied` has order 3, after `person.tin`. Checked by the same scripted interview: with an SSN, `tin` is
  asked and `itin_applied` is not; without one, `itin_applied` is asked after `tin`.
- **Tags:** interview-order; value-neutral; trigger-missed; caught-by-audit

## BUG-0271 — Five entries left with an open or staged fix after the fix was made

- **Date:** 2026-10-31
- **Caught by:** the TASKS.md verification of 2026-10-31 (T-149).
- **Symptom:** these entries still say the fix is open or not applied, though it is done: BUG-0081 ("Fix: open (TASKS.md
  T-050)"; fixed in 6fb728b), BUG-0111 ("staged ... Not applied to the active tree"; integrated in 2fdec33, T-061),
  BUG-0129 ("Status: open"; closed by the owner's decision on per-form qualification, 73b1ebe, T-062), BUG-0134 ("Status:
  open, T-063"; source-based input contracts, 0ef4912) and BUG-0135 ("Status: open, T-064"; adapter contracts, 1b75a3b,
  f4952 adjudicated by 4d24cbc).
- **Root cause:** the inventory is append-only, and no step asked for a closing entry when a fix landed later than the
  entry; the TASKS rows were the only record and were not closed either.
- **Where:** `BUG_INVENTORY.md`.
- **Fix:** this entry records the fixes; the five entries stand as written.
- **Tags:** record-drift; closes-earlier-entry; caught-by-audit

## BUG-0272 — The considered-unmarried question stated none of the rules

- **Date:** 2026-11-01
- **Caught by:** the T-117 check (from the T-091 round 2 adjudication, a question about the spouse's temporary absence).
- **Symptom:** `household.unmarried` asked "Were you unmarried, or considered unmarried under the head of household rules,
  at the end of 2025?" with no rule stated. i1040gi p. 14 gives three ways to be considered unmarried, p. 15 the five
  conditions for married persons who live apart, and p501 p. 8 (test 3) says "Your spouse is considered to live in your
  home even if your spouse is temporarily absent due to special circumstances. See Temporary absences", which brings in
  p. 9's expected-return condition. A filer whose spouse was away on a temporary deployment for the last six months could
  read "lived apart" literally, answer Yes and get head of household where the source makes the filer married (a joint
  return, or a separate one, which the tool refuses). Severity medium: it changes the filing status on a reachable return.
- **Where:** `forms/2025/household.yaml`, `household.unmarried`.
- **Fix:** the question states the three ways, the five conditions and the spouse's temporary-absence rule with its
  expected-return and keeping-up-the-home conditions, citing i1040gi pp. 14 and 15 and p501 pp. 8 and 9. Wording only; no
  value changes for a given answer.
- **Tags:** question-incomplete; definition-omitted; household-predicates; caught-by-source-adjudication

## BUG-0273 — The qualifying surviving spouse question left out the kidnapped-child rule

- **Date:** 2026-11-01
- **Caught by:** fix round 2 adjudication (`.transcription/proposed/fixr2/household.findings.md`, F1; T-114).
- **Symptom:** p501 p. 11, "You may be eligible to file as a qualifying surviving spouse even if the child who qualifies
  you for this filing status has been kidnapped"; test 3 of `household.qss_eligible` listed temporary absences and the
  birth, death and adoption rules but not the kidnapped child, so such a filer answered No and was refused with "the tests
  are not met", which is not true. Every path ended in a refusal; the wrong one fired.
- **Where:** `forms/2025/household.yaml`, `household.qss_eligible`; `forms/2025/f1040.yaml`, the `household.qss_fails`
  refusal at line 12e.
- **Fix:** test 3 tells the filer to answer No for a child presumed kidnapped (the rule of Pub. 501 is outside this tool),
  and the refusal's remedy names that case, citing p501 p. 11. `stage21.pending1.single_claims_qss_refused` carries the
  new remedy.
- **Tags:** question-incomplete; refusal-wording; caught-by-source-adjudication

## BUG-0274 — The household home-cost questions did not say that TANF payments count as paid by you

- **Date:** 2026-11-01
- **Caught by:** fix rounds 4 and 5 and completeness round 5 (`fixr4/household.findings.md` L1, `fixr5/household.findings.md`
  L1, `reviews/2025/completeness/r5.findings.md` L1; T-115).
- **Symptom:** p501 p. 9, Note: TANF or similar payments "used ... to support another person ... are considered support you
  provided"; `household.home_cost` and test 4 of `household.qss_eligible` gave only the own-funds rule, which can lead a
  filer with a child-only TANF grant to count the rent as the child's and answer No. Every path ended in a refusal.
- **Where:** `forms/2025/household.yaml`, `household.home_cost`, `household.qss_eligible`.
- **Fix:** both say "TANF or similar payments you received and used for the home count as paid by you", citing p501 p. 9.
  The same sentence is due on `dependent.parent_home_paid` (T-111), with the dependent pass.
- **Tags:** question-incomplete; definition-omitted; caught-by-source-adjudication

## BUG-0275 — The qualifying surviving spouse home-cost test excluded "anyone's services"

- **Date:** 2026-11-01
- **Caught by:** fix round 5 adjudication (`fixr5/household.findings.md`, L2; T-116).
- **Symptom:** p501 p. 9 excludes "the value of your services or those of a member of your household"; test 4 of
  `household.qss_eligible` said "anyone's services", which can be read to exclude paid labour such as a repair bill.
- **Where:** `forms/2025/household.yaml`, `household.qss_eligible`.
- **Fix:** test 4 excludes "the value of your own or a household member's services", citing p501 p. 9.
- **Tags:** question-wording; caught-by-source-adjudication

## BUG-0276 — Household wording fixes introduced three narrower eligibility readings

- **Date:** 2026-11-01
- **Caught by:** household pass round-one render/completeness adjudication, `.transcription/proposed/hhpass/household.findings.md`, F1–F3.
- **Symptom:** BUG-0272's considered-unmarried text omitted the child's birth/death, adoption/placement and temporary-absence exceptions, and said the other parent "claims" rather than "can claim" the child. BUG-0273's kidnapped-child instruction could refuse a child returned before 2025 who lived at home throughout 2025.
- **Root cause:** paraphrasing the general tests dropped their exceptions and the kidnapping's connection to the tax-year absence.
- **Where:** `forms/2025/household.yaml`, `household.unmarried` and `household.qss_eligible`.
- **Fix:** the working-tree questions include the residence exceptions, "can claim", and a kidnapping that kept the child from living at home throughout 2025. Checked against archived i1040gi pp. 14–15 and p501 pp. 8–11; round-two independent review remains required. These are wording corrections, not changed computations for fixed answers.
- **Siblings checked:** `dependent.kidnapped` timing remains T-104; `dependent.parent_home_paid` TANF wording remains T-111. No claim that those tasks are fixed here.
- **Tags:** fix-introduced; question-incomplete; over-refusal; caught-by-source-adjudication

## BUG-0277 — Single and head-of-household selections had no spouse-death-year check

- **Date:** 2026-11-01
- **Caught by:** household pass round-one adjudication P1 and the Form 1040 sibling check.
- **Symptom:** a filer whose spouse died in 2025 could select single or head of household without answering any death-year question. The household unmarried question did not explain p501 p. 6's whole-year married rule; i1040gi p. 13 permits the widowed Single condition only for a death before January 1, 2025.
- **Root cause:** the qualifying-surviving-spouse question covered an earlier spouse death, but single/HOH had no corresponding death-year boundary.
- **Where:** `forms/2025/household.yaml` and `forms/2025/f1040.yaml`, line 12e.
- **Fix:** owner's 2026-11-01 decision: `household.spouse_died_2025` feeds `household.widowed_2025`, refusing single/HOH at line 12e. The unmarried question states the death-year rule. Source-predicted `stage21.household.widow_*` fixtures cover both statuses with true and false answers; round-two review and full validation remain required.
- **Siblings checked:** qualifying surviving spouse already asks for death in 2023/2024; married-filing-jointly is outside this new gate. Question bank, profiles, both generators and fixture inputs carry the new input.
- **Tags:** missing-condition; filing-status; household-predicates; caught-by-source-adjudication

## BUG-0278 — A marriage ending during the year escaped community-property screening

- **Date:** 2026-11-01
- **Caught by:** household completeness/adjudication P2, `.transcription/proposed/hhpass/household.findings.md`.
- **Symptom:** a non-joint filer divorced or legally separated during 2025 after living married in a community property state could compute from the income entered without a community-income allocation screen. i1040gi p. 23 directs the filer to state law, Form 8958 and Pub. 555.
- **Root cause:** existing gates covered a married head-of-household filer and registered domestic partners, but not a marriage that ended during the year.
- **Where:** `forms/2025/household.yaml` and `forms/2025/f1040.yaml`, line 1a.
- **Fix:** owner's 2026-11-01 decision: ask `household.cp_married` and refuse via `household.cp_marriage_ended` when not joint, community-property residence is yes, married at year end is no, and married during the year in that state is yes. No state-law allocation is inferred. Source-predicted `stage21.household.community_*` fixtures cover the new refusal and negative controls; round-two review and full validation remain required.
- **Siblings checked:** the existing `household.hoh_community_property` refusal is retained and tested separately; registered-domestic-partner screening remains separate. Question bank, profiles, both generators and fixture inputs carry the new input.
- **Tags:** scope-screen-missing; community-property; caught-by-source-adjudication

## BUG-0279 — Foreign return refusals made untouched completeness debt immediately due

- **Caught by:** household round-two completeness check, 2026-11-01.
- **Symptom:** adding the widow and ended-marriage community-property refusals to Form 1040 altered HANDLED ELSEWHERE in foreign review prompts, invalidating 55 untouched forms' deferred baseline subjects. This defeated the approved form-by-form T-094 schedule.
- **Cause:** the exact review-prompt hash also served as the change trigger for never-reviewed baseline debt.
- **Fix:** preserve exact full-prompt matching for every actual review and claim ruling; add verified historical local subjects for never-reviewed debt only. Own canonical form, cited source sections and review policy still invalidate that debt. Original baseline hashes are preserved. Migration reproduced all 56 original fingerprints from an independently built f44bae4 checkout; 55 remain deferred and the changed f1040 remains due.
- **Validation:** completeness self-tests include four debt regression tests, covering own arithmetic/source/policy changes, bad migration records, foreign context changes and the inability to qualify an existing stale receipt. Current completeness check intentionally fails on dependent, f1040, f2441 and household claim1. Full-suite validation and commit remain pending.
- **Tags:** review-debt-invalidation; baseline-scope; tooling

## BUG-0280 — Shared year-end marriage question omitted the federal marriage definitions

- **Caught by:** household completeness round two claim1 (p501 p.6), 2026-11-01.
- **Symptom:** household.married asked whether the filer was married at year end without explaining recognized common-law/foreign/tribal marriages, nonfinal divorce decrees, final divorces/legal separation, annulments or partnerships that are not marriages. A wrong answer can bypass the EIC married-filer tests or alter the HSA age-55 family-coverage limit. Filing-status selection also lacked the cited divorce/remarriage warning.
- **Fix:** the input now states the source definitions and separately labels the divorce/remarriage filing-status warning. It retains the distinction between legal year-end marriage (read by HSA) and the spouse-death filing-status rule, which has a separate screen. The underlying Boolean and all calculation guards are unchanged.
- **Validation:** archived p501 p.6, i1040gi p.13 and i8889 p.4 inspected before editing. Build passed; fresh source/render/completeness reviews and final validation pending. Existing marriage/HOH/HSA fixtures provide calculation controls; the changed rule interpretation is supplied as question text, not a new computed determination of civil status.
- **Tags:** undefined-legal-input; household-wording; source-completeness

## BUG-0281 — Consumer prompt writer skipped changed baseline questions

- **Caught by:** household marriage-definition follow-up, 2026-11-01: the checker reported three new/due pairs but `--prompts` wrote zero prompts.
- **Cause:** write_prompts treated existence of a baseline pair key as acceptance without comparing its recorded subject hash to the current question.
- **Fix:** baseline keys suppress prompt generation only while their subject hash matches. Actual rulings retain the existing acceptance policy.
- **Validation:** reproduce with the three household.married pairs (i8889 pp.5–6 and i1040gi p.23); after correction, all three prompts are generated. A regression is added to the consumer self-test.
- **Tags:** review-prompt-omission; changed-baseline-subject; verification-tooling

## BUG-0282 — Remaining support-definition details in the dependent questions (open)

- **Caught by:** dependent completeness refresh claims1–2; archived earlier rulings already classified these as low and batched them, 2026-11-01.
- **Symptom/source:** dependent.supported and dependent.self_support omit or compress parts of p501 pp.15,20–21: insurance premiums/benefits, excluded taxes and educational assistance, GI Bill amounts, and rarer allocation, property, foster-business and lump-sum support cases.
- **Disposition:** T-107/T-109, expanded with the remaining source sentences, in the dependent form pass. The form is unchanged in the household package. This is deferred definition debt, not an implemented refusal or a certified complete support worksheet.
- **Validation status:** source/implementation inspection and fresh completeness claim; no fix or new independent numeric evidence claimed.
- **Tags:** source-definition-debt; existing-form-pass; explicitly-deferred

## BUG-0283 — Other-claimant screen does not exclude people who are not taxpayers (open)

- **Caught by:** dependent completeness refresh claim3; repeats the original completeness note, 2026-11-01.
- **Symptom/source:** dependent.other_claimant asks about another person without i1040gi p.19 / p501 p.18’s exception for someone not required to file who does not file or files only for a refund. It can refuse an otherwise eligible qualifying relative; it does not produce a wrong completed amount on the identified path.
- **Disposition:** T-153, low over-refusal, with the dependent form pass; preserve existing multi-claimant refusal until that source definition is corrected.
- **Validation status:** source/implementation inspection and fresh completeness claim; no fix or new independent numeric evidence claimed.
- **Tags:** source-definition-debt; existing-form-pass; explicitly-deferred

## BUG-0284 — Care-expense question omits explicit mixed-purpose and daily allocation detail (open)

- **Caught by:** dependent claim9 and f2441 claim1; repeats the previously batched care-definition observation, 2026-11-01.
- **Symptom/source:** dependent.dc_paid asks for care while a qualifying person so the filer can work, and names the major exclusions, but does not explicitly state child-support exclusion, allocation of mixed-purpose costs or the day-by-day work-period method from i2441 p.2 / p503. Unusual entries can overstate qualified expenses if the filer interprets the short definition too broadly.
- **Disposition:** T-154, low clarification debt, in the dependent/f2441 passes. Noncustodial divorced-parent cases are refused separately; the remaining allocation gap is not being treated as a refusal.
- **Validation status:** source/implementation inspection and fresh completeness claim; no fix or new independent numeric evidence claimed.
- **Tags:** source-definition-debt; existing-form-pass; explicitly-deferred

## BUG-0285 — Lifetime learning student eligibility accepts an applied-for TIN (open)

- **Caught by:** dependent completeness refresh claim12; existing owner decision T-113, 2026-11-01.
- **Symptom/source:** dependent.edu_student accepts dependent.tin, whose question includes a timely applied-for ATIN/ITIN. i8863 requires an issued TIN; the p970 p.11 deemed-issuance rule is stated in the American opportunity chapter, not for lifetime learning.
- **Disposition:** Owner decision T-113 schedules the issued-versus-applied-for split for both dependent and person in their form passes. Keep the AOC deeming and refuse the unsupported lifetime-learning case; do not silently change that selected scope during household closure.
- **Validation status:** source/implementation inspection and fresh completeness claim; no fix or new independent numeric evidence claimed.
- **Tags:** source-definition-debt; existing-form-pass; explicitly-deferred

## BUG-0286 — Filing status could contradict the supplied marriage facts

- **Caught by:** household final completeness claim1 and f1040 completeness claim1, 2026-11-01.
- **Source:** i1040gi p.13, Single and Married Filing Jointly; p501 p.6.
- **Symptom:** Single could compute with household.married Yes; joint could compute with year-end marriage No and no spouse death in 2025. The roster check tests counts, not these eligibility contradictions.
- **Fix:** household.filing_status_conflict refuses those two contradictions at f1040.line12e. The joint death-year exception remains supported; HOH/QSS retain their separate tests. The death-year question now also covers joint filers who were not married at year end. This is an entry consistency check, not a new excluded tax situation.
- **Regression predictions:** six stage21.household.status_* cases cover both contradictions, valid single/joint, joint death-year and married HOH. Expected deductions/refusals were written from source before running the evaluator.
- **Fixture context repair:** 17 older Claude ClassM cases supplied joint status and no death-year fact but had household.married False as unused context. Corrected that inferred context fact to True and annotated the host repair; expected numerical values and original model receipts are untouched. Raw saved prompts are not assumed to be the original receipt when hashes differ. These cases do not acquire any new evidence credit.
- **Validation:** build, render, 1,425 CLI fixtures, strict citations, both families' reviews and the offline check set passed before commit; the full check-all is the commit gate for this final gate.
- **Tags:** contradictory-inputs; filing-status-eligibility; source-completeness

## BUG-0287 — Cross-document references were memoized under aliased caller keys

- **Caught by:** technical debt audit 1.1 (memo key pollution), reproduced on the current tree, 2026-11-01.
- **Symptom/source:** `evalLine` computed the memo key from the caller's frame before deciding whether the line belonged to the current document. A reference from inside a collection entry to a top-level line cached the result a second time under a composite key such as `person[spouse].f8606[form].person.ira_files_8606`. On a single return the `values` map carried 64 such aliases; `eval --json`, values-sheet derivations and the TS/Lean comparison exported them. No tax value changed.
- **Fix:** both evaluators memoize a resolved cross-document reference only under the target line's key. TypeScript drops the caller-key insertion; Lean skips insertion when the line is not in the frame's document but resolves elsewhere. `test-integration` asserts no alias keys in the eval values of a return with a collection-entry reference.
- **Validation:** `eval --json` on `stage16.ira.i1` has no alias candidate (was 64); `npm run compare` passes 2,025 cases with 4,471,784 values, 87,101 fewer than before, 0 differing cases; 805 integration checks pass. Fifty-nine stage1 fixtures had recorded the three `qdcg.f1040.*` aliases (and 12 more `f1040.qdcg.line25` or `qdcg.sd.distributions`); those duplicate expectations were removed, leaving the canonical keys, and the CLI fixtures pass 1,425/1,425.
- **Tags:** evidence-integrity; evaluator; fixed

## BUG-0288 — Class C differential reader scanned the investigation log as a calculator record

- **Caught by:** technical debt audit 1.5, confirmed in `engine/src/differential.ts`, 2026-11-01.
- **Symptom/source:** `differential()` filtered directory entries to objects with a `calculator` field, but `differentialClassC()` read every `.json` file in `fixtures/2025/differential/` and immediately accessed `rec.values`. The engine differential's investigation log is a JSON array, so the fixture-coverage path could throw on a directory the comparison path accepts.
- **Fix:** one `calculatorRecords()` helper filters both readers. The class C coverage map now sees only calculator records.
- **Validation:** `node engine/dist/main.js differential` and `coverage` pass on the current tree; the full suite exercises both.
- **Tags:** evidence-integrity; tooling; fixed

## BUG-0289 — Push guard checked only the tip, and the green list had a lost-update race

- **Caught by:** technical debt audit 1.6, confirmed in `tools/hooks/pre-push` and `tools/green.sh`, 2026-11-01.
- **Symptom/source:** the hook's comment promised every commit being pushed, but it checked only the local tip's tree; an untested intermediate commit could ride a green tip. `record_green` read and rewrote `.git/check-all-green-trees` with `tail` plus `mv` and no lock, so two runs finishing together could lose one entry.
- **Fix:** the hook computes the pushed range (`remote..local`, or `local --not --remotes` for a new ref) and requires every commit's tree in the green record. `record_green` takes a directory lock for the read-modify-write.
- **Validation:** `tools/hooks/test_pre_push.sh` covers an untested intermediate, a fully green range, a new ref against a remote-tracking base, and a new ref with an untested commit; `tools/hooks/test_green.sh` records 20 concurrent entries and finds all 20. Both run in check-all. One audit subclaim (dangling snapshot commits in `check_all_bg.sh`) is housekeeping, not a guard defect; git's object pruning handles it.
- **Tags:** commit-guard; process-integrity; fixed

## BUG-0290 — Schedule C at-risk question omits the related-party prong (open)

- **Caught by:** render comparison of `sc` after the 2026-11-01 renderer marker refresh.
- **Source:** i1040sc p. 15, Line 32, Some investment is not at risk: "Amounts borrowed for use in the business from a person who has an interest in the business other than as a creditor or who is related under section 465(b)(3)(C) to a person (other than you) having such an interest."
- **Symptom:** `sc.at_risk` (box 32a) asks about "amounts borrowed from someone with an interest in the business" but omits the related-party prong. A filer with a loan from a person related to an owner could answer Yes and take a loss the at-risk rules would limit.
- **Disposition:** T-157, with the Schedule C form pass; wording only, no new input. Do not change the at-risk refusal path before that pass.
- **Validation:** source and implementation inspection and one render-review objection; no fixture or numerical evidence claimed.
- **Tags:** source-definition-debt; existing-form-pass; explicitly-deferred

## BUG-0291 — Special allowance wording overstates the 40% class and omits 50% reuse property (open)

- **Caught by:** DeepSeek render comparison of `asset` after the 2026-11-01 renderer marker refresh.
- **Source:** i4562 pp. 5–7, Line 14: the 40% allowance is for property acquired after September 27, 2017 and before January 20, 2025; qualified reuse and recycling property placed in service after August 31, 2008 is eligible for a 50% allowance.
- **Symptom:** `asset.bonus_fullcase`'s English says "100% if acquired after January 19, 2025, otherwise 40%," so it applies 40% to property acquired before September 27, 2017, and `asset.bonus_choice` has no 50% reuse/recycling branch. A pre-2017 asset answered "full" gets 40%; a reuse/recycling asset cannot get 50%.
- **Disposition:** T-158, with the asset form pass; add the acquisition-date boundary and the 50% category (input and branch), then rerun the asset and Schedule C reviews.
- **Validation:** source and implementation inspection and one render-review objection; no fixture or numerical evidence claimed.
- **Tags:** source-definition-debt; existing-form-pass; explicitly-deferred

## BUG-0292 — Earlier-year HSA excess is not asked when a 2025 Form 8889 exists (open)

- **Caught by:** the 2026-11-01 screen review of `person.x_other` after the T-118 wording fix.
- **Source:** f5329 p. 2, Part VII, line 46 "Prior year excess contributions" and line 48 "Total excess contributions. Add lines 46 and 47".
- **Symptom:** `person.x_other` asks about an earlier-year HSA excess only when there is no 2025 Form 8889. A filer with a 2025 Form 8889 and an unabsorbed earlier-year excess answers No; `f5329.l48` copies only line 47 and lines 42 to 46 are zero, so the 6% tax on the carried excess is omitted.
- **Disposition:** T-161, with the Form 5329/person pass: add the carried excess as an input or extend the question, then rerun the screen review and the f5329/person reviews.
- **Validation:** one screen-review finding and source/implementation inspection; no fixture or numerical evidence claimed.
- **Tags:** source-definition-debt; existing-form-pass; explicitly-deferred

## BUG-0293 — The f8962 other-coverage screen missed other minimum essential coverage and incarcerated enrollees

- **Caught by:** f8962 completeness review claim 4 (`.transcription/completeness/f8962.response.txt`), 2026-11-01; the same gap as the earlier `f8962.other` screen review finding PENDING-4-4.
- **Source:** i8962 p. 5, Minimum essential coverage (MEC): "Most coverage through government-sponsored programs (including Medicaid coverage, Medicare Part A or C, the Children’s Health Insurance Program (CHIP), certain benefits for veterans and their families, TRICARE, and health coverage for Peace Corps volunteers)", "Most types of employer-sponsored coverage", and "Other health coverage the Department of Health and Human Services designates as MEC"; p. 5, "In addition, if you or your family member enrolls in employer-sponsored coverage for a month, you or your family member is considered eligible for employer-sponsored coverage for that month, even if the coverage does not satisfy the affordability and minimum value standards"; p. 6, COBRA and retiree coverage; p. 6, "Individuals who are incarcerated (other than pending disposition of charges, for example, awaiting trial) are not eligible for coverage in a qualified health plan through a Marketplace"; p. 6, a Marketplace Medicaid or CHIP determination based on intentionally or recklessly incorrect information.
- **Symptom:** `f8962.other` asked only about an unlawfully present enrollee, a QSEHRA or individual coverage HRA, unpaid premiums and advance payments for someone in no tax family. A filer who was eligible for other MEC for a month — including one who enrolled in unaffordable or non-minimum-value employer coverage, or in COBRA or retiree coverage — could truthfully answer no, remain in the coverage family, and take the full credit. The closed program list omitted Peace Corps coverage and other HHS-designated MEC, and the question did not ask about incarceration or a Marketplace Medicaid/CHIP determination later found to rest on intentional or reckless misinformation.
- **Fix:** the `f8962.other` question and label now state every limb of the MEC eligibility rule, the enrollment rule for employer coverage including COBRA and retiree coverage, the Marketplace Medicaid/CHIP misdetermination, and incarceration, and exclude coverage bought in the individual market outside the Marketplace. The refusal and remedy name the situations; the refusal cites i8962 pp. 5–6. The existing stage18.refuse.other_coverage expectation was refreshed and a named enrolled-unaffordable-employer case added.
- **Fix lines:** `f8962.other`
- **Siblings checked:** `f8962.line24`, `f8962.line25`
- **Regression predictions:** stage18.refuse.other_coverage (same screen, refreshed remedy/cite) and stage18.refuse.other_mec_enrolled both refuse at f8962.line24, f8962.line25 and s3.line9 with the new form name, remedy and i8962 pp. 5–6 cite, written from the source before the evaluator was run. The fixture suite is 1,428/1,428 through the command-line program.
- **Tags:** source-completeness; premium-tax-credit; fixed

## BUG-0294 — A VOID or replaced Form 1095-A could feed the Form 8962 columns

- **Caught by:** f8962 completeness review claim 5 (`.transcription/completeness/f8962.response.txt`), 2026-11-01.
- **Source:** i8962 p. 2, "Do not use the information on the Form 1095-A with the “VOID” box checked or the previously received Form 1095-A to complete Form 8962"; "If you receive a Form 1095-A with the “CORRECTED” box checked at the top of the form, use the information on the Form 1095-A with the “CORRECTED” box checked to figure the PTC and reconcile any APTC on Form 8962"; "Do not use the information on the original Form 1095-A you received for the policy shown in Part I of the corrected Form 1095-A."
- **Symptom:** the f1095a collection counted and summed every entered form, with no question, filter or refusal for a VOID form, an original that a later VOID form supersedes (i8962 p. 2: a VOID form means the Marketplace previously sent a form for that policy in error, and neither the VOID form nor the previously received one may be used), or an original that a corrected form replaces. If a filer entered both, the premiums, SLCSP amounts and advance payments were counted twice; if they entered only the VOID or superseded form, its amounts were used. A GPT-6 Astra render review of the first wording found that it named only the corrected-form case; the question and remedy were extended before the pass closed.
- **Fix:** new `f1095a.void` question on each entry (marked VOID, or an original superseded by a later VOID or corrected form); `f8962.void_forms` counts the entries answered yes and `f8962.void_form` refuses the return with a remedy to enter the form the Marketplace says to use and omit the void, replaced or superseded one (i8962 p. 2).
- **Fix lines:** `f1095a.void`, `f8962.void_forms`, `f8962.void_form`
- **Siblings checked:** `f8962.void_forms`, `f8962.void_form`, `f8962.line24`, `f8962.line25`
- **Regression predictions:** stage18.refuse.void_1095a answers `f1095a[m].void` true and refuses at f8962.line24, f8962.line25 and s3.line9 with the `f8962.void_form` form, remedy and i8962 p. 2 cite, written from the source before the evaluator was run. Fixtures 1,428/1,428.
- **Tags:** source-completeness; premium-tax-credit; fixed

## BUG-0295 — Form 8962 took column A as reported when coverage began mid-month or a premium was refunded

- **Caught by:** f8962 completeness review claim 7 (`.transcription/completeness/f8962.response.txt`), 2026-11-01.
- **Source:** i8962 p. 4, "To qualify for a monthly credit amount, at least one individual in your tax family must be enrolled in a qualified health plan on the first day of that month. Generally, if coverage in a qualified health plan began after the first day of the month, you are not allowed a monthly credit amount for the coverage for that month"; the birth, adoption, foster-care placement and court-order exception that treats the individual as enrolled on the first day; "The enrollment premiums are the total amount of the premiums for the month, reduced by any premium amounts for that month that were refunded in 2025".
- **Symptom:** lines 11(a) and 12(a) to 23(a) summed Form 1095-A column A as entered. A month whose coverage began after the first day kept a monthly credit amount, and a premium refunded in 2025 kept inflating the enrollment premium.
- **Fix:** new `f8962.premium_adjust` gate, answered when coverage began after the first day of a month other than on a birth, adoption, placement for adoption or foster care, or a court order (which count from the first day) or when a Marketplace premium was refunded in 2025; the return is refused with the p. 4 rule and remedy. The monthly-adjustment alternative (per-month inputs) was rejected as a fifteen-input change for a narrow case.
- **Fix lines:** `f8962.premium_adjust`
- **Siblings checked:** `f8962.line24`, `f8962.line25`
- **Regression predictions:** stage18.refuse.premium_adjust answers the gate true and refuses at f8962.line24, f8962.line25 and s3.line9 with the `f8962.premium_adjust` form, remedy and p. 4 cite, written from the source before the evaluator was run. Fixtures 1,428/1,428.
- **Tags:** source-completeness; premium-tax-credit; fixed

## BUG-0296 — The below-100% Marketplace-estimate exception ignored intentional or reckless misreporting

- **Caught by:** f8962 completeness review claim 3 (`.transcription/completeness/f8962.response.txt`), 2026-11-01.
- **Source:** i8962 p. 9, "You do not meet the requirements under Estimated household income at least 100% of the federal poverty line, earlier, if: ... You, with intentional or reckless disregard for the facts, provided incorrect information to a Marketplace for the year of coverage."
- **Symptom:** `f8962.estimate_100` asked only whether the Marketplace estimated income at or above 100% of the poverty line. A filer who provided incorrect information with intentional or reckless disregard could answer yes, meet the exception in `f8962.applicable`, and take the PTC below 100% of the poverty line.
- **Fix:** the question now says "Answer no if you, with intentional or reckless disregard for the facts, provided incorrect information to a Marketplace for 2025", and the line cites both p. 9 sentences. No new input: the disqualifier belongs to the same Marketplace-estimate exception.
- **Fix lines:** `f8962.estimate_100`
- **Siblings checked:** `f8962.applicable`
- **Regression predictions:** no new numeric fixture is needed: the input is a Boolean screen, and every existing return answers it. The change is question wording and a citation; the screen review rerun covers the reading.
- **Tags:** source-completeness; premium-tax-credit; fixed

## BUG-0297 — A dependent filer who itemizes bypasses the dependent refusal

- **Caught by:** the cloud Claude session's read-only audit of the f8962 pass rulings, 2026-11-02; reproduced locally.
- **Source:** i8962 p. 6, "Generally, you are an applicable taxpayer if your household income for 2025 ... is at least 100% of the federal poverty line for your family size ... and no one can claim you as a dependent for 2025"; i1040gi pp. 34–35, line 12e.
- **Symptom:** the `sa.dependent` refusal was declared only on `sa.standard`. `sa.itemizes` short-circuits on `sa.elect_itemize`, and `sa.deduction` then takes `sa.line17` without ever evaluating `sa.standard`, so a filer who can be claimed as a dependent and elects to itemize completed the return: witness `stage18.blind.p1` with `sa.dependent=true, sa.elect_itemize=true` gives f1040.line24 $4,565, f8962.line24 $3,560. The 4.7% dependent-filer refusal category was therefore under-enforced, and the completeness and render rulings that rely on a return-wide dependent refusal were true only for standard-deduction filers.
- **Fix:** the same `sa.dependent` refusal (its own form and remedy wording) is declared on `sa.deduction`, the line both branches pass through, so the itemized branch refuses as well. The `sa.standard` refusal stays for the standard branch. New regression `stage4.refuse.dependent_itemizes` asserts the refusal at `sa.deduction`, `f1040.line12e` and f1040.line24.
- **Fix lines:** `sa.deduction`
- **Siblings checked:** `dependent.qc_dependent`, `dependent.qr_dependent`, `eic.step4`, `person.sav_ineligible`, `sa.standard`, `f1040.line12e`
- **Regression predictions:** `stage4.refuse.dependent_itemizes` answers `sa.dependent` true and elects to itemize; the return is refused at sa.deduction, f1040.line12e and f1040.line24 with the new form and remedy, written from the source before the evaluator was run.
- **Validation:** pending the sa and sibling reviews and the full suite.
- **Tags:** source-completeness; eligibility; fixed

## BUG-0298 — The column B questions end with "zero if blank" after asking for the corrected premium

- **Caught by:** the cloud Claude session's audit of the f8962/f1095a completeness rulings, 2026-11-02.
- **Source:** i8962 p. 17, Column (b): "If not allowed a monthly credit amount because your enrollment premiums for the month were unpaid, enter -0- on the appropriate line on Form 8962, column (b). However, if your enrollment premiums for the month were paid by the due date of your return ... enter your applicable SLCSP premium for the month"; p. 16: if no APTC was paid, column B may be blank or wrong and the filer must determine the correct applicable SLCSP premium.
- **Symptom:** the `f1095a.in_b_<month>` and `f1095a.mo_b` questions ask for "the amount in column B, or the correct applicable SLCSP premium if column B is blank, zero or wrong (from the Marketplace's tool…)" and then end with "; zero if blank". For a covered month with a blank column B, the trailing clause tells the filer to enter zero, understating column (b), the SLCSP premium and the PTC. The clause is apt only for a month with no coverage.
- **Disposition:** T-165. Reword the 13 questions to "zero if blank and no one was enrolled that month" at the next f1095a change, then rerun the f1095a and f8962 reviews. The completeness claim `unruled:f8962#3` is ruled a real gap on this entry.
- **Validation:** source and implementation inspection; the first clause already asks for the corrected premium, so no new input or fixture is needed.
- **Tags:** source-definition-debt; premium-tax-credit; explicitly-deferred

## BUG-0299 — The employer-coverage limb of f8962.other leaves "affordable" undefined

- **Caught by:** the cloud Claude session's statement-coverage check of `f8962.other`, 2026-11-02.
- **Source:** i8962 p. 5, "The coverage offered by your employer is generally considered affordable for you if your share of the annual cost for self-only coverage ... is not more than 9.02% of your household income"; "If your employer coverage is affordable for you but not affordable for your other family members, you may be able to take the PTC for your other family members."
- **Symptom:** the question asks whether employer coverage "was offered and was affordable and provided minimum value" without saying whose cost is tested. An employee whose self-only cost is at or below 9.02% but whose family cost is above it may judge affordability by the family premium, answer no, and keep the PTC for the employee's own months. The source makes the employee eligible for MEC in that case. The screen ruling's statement that the undefined measure errs only toward a yes answer holds for family members, not the employee.
- **Disposition:** T-166. Add the 9.02% self-only test for the employee and the family-cost test for a family member to the `f8962.other` question at the f8962/PTC next change (T-132/T-145 or the F3 remainder), then rerun the f8962 reviews and completeness. The question is otherwise complete on i8962 pp. 5–6.
- **Validation:** source and implementation inspection; no fixture change until the wording is fixed.
- **Tags:** source-definition-debt; premium-tax-credit; explicitly-deferred

## BUG-0300 — The dependent questions do not exclude a stillborn child or ask for a live-birth record

- **Caught by:** the dependent completeness review (prompt after BUG-0297), 2026-11-02.
- **Source:** p501 p. 13, "Stillborn child. You can't claim a stillborn child as a dependent"; "State or local law must treat the child as having been born alive."
- **Symptom:** `dependent.born_died` asks only whether the person was born or died in 2025; a stillborn child can be entered as a dependent, and no question asks whether state or local law treats the child as born alive or requires the official record.
- **Disposition:** T-167, with the F1 dependent pass: add the stillborn exclusion and the live-birth requirement to the born/died or claimed question (wording only).
- **Validation:** one completeness claim and source inspection; no fixture or numerical evidence claimed.
- **Tags:** source-definition-debt; dependent; explicitly-deferred

## BUG-0301 — The dependent student question does not define a school or treat co-op students as full-time

- **Caught by:** the dependent completeness review, 2026-11-02.
- **Source:** p501 p. 13, "Students who work on 'co-op' jobs in private industry as a part of a school's regular course of classroom and practical training are considered full-time students"; "A full-time student at a school that has a regular teaching staff and course of study, and a regularly enrolled student body at the school."
- **Symptom:** `dependent.student` asks whether the person was a full-time student without the school definition or the co-op rule; a co-op student can answer no and fail the qualifying-child student test.
- **Disposition:** T-168, with the F1 dependent pass; wording only.
- **Validation:** one completeness claim and source inspection.
- **Tags:** source-definition-debt; dependent; explicitly-deferred

## BUG-0302 — Schedule A definition details in the medical, tax, charity and blindness questions

- **Caught by:** the Schedule A completeness review (prompt after BUG-0297), 2026-11-02.
- **Source:** i1040sca p. 1 (HSA/MSA distributions, pretax insurance premiums, public-safety-officer premiums, long-term care limits, nursing/housework pay, meals with lodging, estate-paid expenses); p. 7 (U.S. territory taxes belong on the state and local line; only taxes paid in 2025 and assessed before 2026); p. 11 (good used condition, the $500 single-item appraisal exception, the $250 contemporaneous acknowledgment for property); i1040gi p. 33 (the certified statement for partial blindness).
- **Symptom:** the `sa.line1`, `sa.line5a`, `sa.line5b`, `sa.line12` and `sa.boxes_blind` questions do not carry these rules, so a filer can omit territory taxes, deduct prepaid 2026 property tax, take a noncash gift without the condition or acknowledgment, miss the blindness certification, or compute the medical deduction without the listed adjustments.
- **Disposition:** T-169, with the Schedule A form pass (F4): extend the questions or add refusals; rerun the sa reviews and this completeness review.
- **Validation:** one completeness review with six claims (five mapped here, the MFS joint-expense claim refused by s3.mfs) and source inspection.
- **Tags:** source-definition-debt; schedule-a; explicitly-deferred

## BUG-0303 — Form 4562 line 2 counted qualified improvement property with no section 179 election

- **Caught by:** Claude transcription of `asset` (asset.cost179, candidate zero against project $30,000 on `stage14.asset.qip`), 2026-11-02, during the T-157/T-158 pass.
- **Source:** i4562 p. 4, Line 2, "Enter the total cost of all section 179 property you placed in service during the tax year (including the total cost of qualified real property that you elect to treat as section 179 property)"; pp. 2-3, Special rules for qualified section 179 real property, "You can elect to treat certain qualified real property placed in service during the tax year as section 179 property".
- **Symptom:** `asset.cost179_2025` took the business cost of every 2025 asset used more than 50% in the business, so qualified improvement property with no election appeared on Form 4562 line 2 ($30,000 instead of $0 on the witness) and counted toward the $4,000,000 threshold that reduces the limit.
- **Fix:** `asset.cost179_2025` now reads `asset.cost179_real`, which takes the business cost only when `asset.is_section179` holds: the class is not qualified improvement property, or an amount is elected on line 6(c). The other qualified section 179 real property (roofs, HVAC, fire protection and security systems) is real property `asset.screen` already refuses.
- **Fix lines:** `asset.cost179_2025`, `asset.cost179_real`, `asset.is_section179`
- **Siblings checked:** `asset.cost179_2025`, `asset.cost179`, `asset.bonus_2025`, `asset.dep_2025`, `asset.mq_q4`, `asset.mq_total`, `asset.s179_2025`, `s179.line2`, `s179.line5`, `s179.mfs`, `sc.cost179`, `sc.cost179_a`, `sc.cost179_v`, `sc.mq_q4`, `sc.mq_q4_a`, `sc.mq_q4_v`, `sc.mq_total`, `sc.mq_total_a`, `sc.mq_total_v`, `scveh.cost179_o`, `scveh.mq_q4_o`, `scveh.mq_total_o`, `asset.after179`, `asset.f26i`, `asset.period`, `asset.s179_bad`
- **Regression predictions:** `stage14.asset.qip` now asserts line 2 $0; `stage14.asset.qip_elected` ($30,000 cost, $10,000 elected) asserts line 2 $30,000 and depreciation of $666 (3.33% of $20,000). Both were written from the source before the evaluator was run.
- **Validation:** fixtures 1,436/1,436 on the fixed tree; asset reviews rerun on it.
- **Tags:** source-transcription; section-179; fixed

## BUG-0304 — The long-term care question tested the covered person's employer eligibility, not the filer's

- **Caught by:** Claude render comparison of `sc` (line 2), 2026-11-02, during the T-157/T-158 pass.
- **Source:** f7206 line 2, "Don't include payments for any month you were eligible to participate in a long-term care insurance plan subsidized by your employer or your spouse's employer, or the employer of either your dependent or your child who was under the age of 27 at the end of 2025."
- **Symptom:** `ltc.payments` excluded months "the person was eligible for a long-term care plan subsidized by an employer". A filer eligible through their own employer who paid premiums for a covered spouse or dependent could answer with the full amount and overstate the deduction.
- **Fix:** the question now states the form's test in its own terms: months you were eligible, through your, your spouse's, your dependent's or your under-27 child's employer.
- **Fix lines:** `ltc.payments`
- **Siblings checked:** `ltc.amount`, `sc.f7206_line1`, `sc.f7206_line2`
- **Regression predictions:** wording only; no new input or fixture amount. The evidence is the ltc reviews rerun on the new wording.
- **Validation:** ltc transcription and render reviews rerun under both families.
- **Tags:** source-definition-debt; wording; fixed

## BUG-0305 — BUG-0290 and BUG-0291 are fixed by the asset/Schedule C pass

- **Caught by:** BUG-0290 and BUG-0291, recorded open; this entry closes them because the inventory is append-only.
- **Source:** i1040sc pp. 14-15, Line 32; i4562 pp. 5-7, Line 14.
- **Symptom:** as recorded in those entries.
- **Fix:** `sc.at_risk` states the related-party prong and that a nonrecourse loan secured only by property used in the business is not at risk. `asset.screen` refuses qualified reuse and recycling property and an acquisition before September 28, 2017, the owner-accepted refusal in place of a computed 50% branch; the `asset.bonus_fullcase` label states the 100% and 40% windows; `asset.after_jan19` points at the screen.
- **Fix lines:** `sc.at_risk`, `asset.screen`, `asset.bonus_fullcase`, `asset.after_jan19`
- **Siblings checked:** `asset.bonus_fullcase`, `sc.not_at_risk`, `asset.screened`, `asset.bonus_choice`, `asset.bonus`
- **Regression predictions:** `stage14.asset.refuse_reuse_recycling` and `stage14.asset.refuse_pre_2017`, predicted from the source before recording.
- **Validation:** asset, sc and scveh reviews rerun; sc completeness rerun.
- **Tags:** source-definition-debt; existing-form-pass; fixed

## BUG-0306 — A vehicle placed in service in 2025 but acquired before September 28, 2017 took the 40% allowance

- **Caught by:** Claude and DeepSeek render comparisons of `scveh` (line 16), 2026-11-02, after BUG-0291's fix reached only `asset`.
- **Source:** i4562 p. 5, Line 14, "Certain qualified property acquired after September 27, 2017, and before January 20, 2025".
- **Symptom:** `scveh.rate40` gives 40% to any claimed 2025 vehicle not acquired after January 19, 2025, including one acquired earlier than the window, which has no allowance at that rate.
- **Fix:** `scveh.screen` refuses a vehicle placed in service in 2025 but acquired before September 28, 2017. It is narrower than the `asset.screen` item so that an older vehicle with no allowance in play is not refused.
- **Fix lines:** `scveh.screen`
- **Siblings checked:** `scveh.screened`, `scveh.rate40`, `scveh.after_jan19`, `asset.screen`
- **Regression predictions:** `stage14.veh.refuse_pre_2017` answers the screen Yes and is refused at the cost line, written from the source before the evaluator was run.
- **Validation:** scveh reviews rerun under both families.
- **Tags:** fix-sibling; source-definition-debt; fixed

## BUG-0307 — Form 4562 property questions omit section 179, allowance, class and listed-use rules

- **Caught by:** the asset completeness review, 2026-11-02, during the T-157/T-158 pass.
- **Source:** i4562 p. 2 (section 179 property and its exclusions); pp. 6-7 (section 168(k)(9) exclusions and used property); pp. 10-11 (statutory classifications outside Appendix B); p946 p. 37 and i4562 p. 12 (short tax year); i4562 p. 14 (qualified business use exclusions and listed property converted to business use); p. 3 (a home as a regular business establishment).
- **Symptom:** the asset questions do not state these rules, so a filer can elect section 179 on ineligible property, claim the allowance on excluded property, take the wrong recovery period, pass the 50% test on general business use, or answer that property is not listed. Each can change an amount or eligibility.
- **Disposition:** T-170, with the F4 asset pass: extend the questions or add refusals; rerun the asset reviews and this completeness review.
- **Validation:** one completeness review with seven claims, each quote matched against the archive; no fixture or numerical evidence claimed.
- **Tags:** source-definition-debt; existing-form-pass; explicitly-deferred

## BUG-0308 — The long-term care entry does not limit who the covered person may be

- **Caught by:** the ltc completeness review, 2026-11-02.
- **Source:** i7206 p. 1, premiums for yourself, your spouse, your dependents, and your child under age 27 at the end of the year.
- **Symptom:** `ltc.payments` accepts premiums for "this person" with no test of the relationship, so premiums for a nondependent parent or an older nondependent child can enter line 2.
- **Disposition:** T-171, with the next ltc or Form 7206 change: state the covered people in the question; rerun the ltc reviews.
- **Validation:** one completeness claim, its quotes matched against the archive.
- **Tags:** source-definition-debt; explicitly-deferred

## BUG-0309 — Schedule C questions omit income, expense, election and QBI rules

- **Caught by:** the sc completeness review, 2026-11-02, during the T-157/T-158 pass.
- **Source:** i1040sc pp. 2-5 (business against hobby; an LLC electing corporate treatment), pp. 5-6 and 9 (sales tax; fuel tax credit), pp. 4 and 15 (tax shelters; long-term contracts), p. 8 (prepaid and shared interest), pp. 9-10 (travel and meal limits; fringe benefits), p. 1 (the $150,000 ceiling), pp. 10 and 13-14 (simplified method conditions), p. 14 (prior-year passive losses); i4562 p. 4 (recapture on non-listed section 179 property); p946 p. 17 (noncorporate lessors; trade-ins); i1040gi p. 94 (personal services as a material income factor); i8995 pp. 2-3 (former employees; Form 1099-PATR).
- **Symptom:** the sc questions do not state these rules or refuse them, so a filer can report an activity that is not a business, misstate income or expenses, keep a double deduction, skip a recapture, or carry an unallowed passive loss. Most can change an amount.
- **Disposition:** T-172, with the F4 Schedule C pass: extend the questions or add refusals; rerun the sc reviews and this completeness review.
- **Validation:** one completeness review with fifteen real-gap claims of seventeen, each quote matched against the archive; no fixture or numerical evidence claimed.
- **Tags:** source-definition-debt; existing-form-pass; explicitly-deferred

## BUG-0310 — A lessee who used the standard mileage rate earlier can switch to actual expenses (open)

- **Caught by:** the scveh completeness review (claim 1), 2026-11-02; reproduced by evaluation. It also shows the earlier render ruling "refusal located elsewhere" on scveh line 9 was wrong.
- **Source:** i1040sc p. 6, "You can't use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle."
- **Symptom:** the `scveh.screen` refusal is declared on `scveh.cost`, which a leased vehicle does not read. `stage14.veh.leased_actual` with the screen answered Yes still completes: line 9 $1,000, line 20a $3,000, and f1040 line 24 unchanged.
- **Disposition:** T-173, in queue 1. Declaring the screen on the leased branch would refuse lessees for its owned-vehicle items, so the fix is a new question for a leased vehicle on actual expenses with its own refusal, which ripples through the question bank and fixtures.
- **Validation:** evaluator run on the fixture with the screen answered both ways; no regression yet.
- **Tags:** eligibility; amount-affecting; explicitly-deferred

## BUG-0311 — Vehicle questions omit qualified use, method, basis, lessor and record rules

- **Caught by:** the scveh completeness review, 2026-11-02.
- **Source:** i4562 p. 14 (qualified business use exclusions); p. 7 and p. 14 (business-to-personal conversion); pp. 7, 11-12 and p946 p. 35 (method and ADS elections, mandatory ADS); p946 pp. 37, 60 (short tax year; basis adjustments); i4562 p. 15 and p946 p. 59 (regular lessors); i1040sc p. 6 (capitalized costs); p946 p. 63 (adequate records).
- **Symptom:** the vehicle questions neither state nor refuse these rules, so a filer can pass the 50% test on excluded use, take the allowance on a vehicle converted to personal use in the same year, keep the table rates after a basis adjustment or an election, or have the limits wrongly applied. Most can change an amount.
- **Disposition:** T-174, with the F4 vehicle pass: extend the questions or add refusals; rerun the scveh reviews and this completeness review.
- **Validation:** one completeness review with eight real-gap claims of twelve, each quote matched against the archive; no fixture or numerical evidence claimed.
- **Tags:** source-definition-debt; existing-form-pass; explicitly-deferred

## BUG-0312 — BUG-0310 is fixed: a lessee who used the standard mileage rate earlier is refused actual expenses

- **Caught by:** BUG-0310, recorded open; this entry closes it because the inventory is append-only.
- **Source:** i1040sc p. 6, "You can't use actual expenses for a leased vehicle if you previously used the standard mileage rate for that vehicle."
- **Symptom:** as recorded in BUG-0310.
- **Fix:** new input `scveh.lease_smr_before` and gate `scveh.lease_smr_bad`; the refusal is declared on `scveh.lease_business`, which only the leased actual-expense path of line 20a reads, so an owned vehicle or a lessee on the standard rate is not asked.
- **Fix lines:** `scveh.lease_smr_before`, `scveh.lease_smr_bad`, `scveh.lease_business`
- **Siblings checked:** `scveh.lease_business`, `scveh.lease_smr_bad`, `scveh.line20a`, `scveh.is_actual_leased`, `scveh.line9`, `scveh.line9_actual`, `scveh.smr_ok`, `scveh.smr_bad`, `scveh.screen`
- **Regression predictions:** `stage14.veh.refuse_lease_smr_before` answers Yes and is refused at line 20a; `stage14.veh.leased_actual` answers No and keeps its amounts. Written from the source before the evaluator was run.
- **Validation:** scveh reviews rerun under both families.
- **Tags:** eligibility; amount-affecting; fixed

## BUG-0313 — BUG-0292 is fixed: an earlier-year HSA excess is refused with or without a 2025 Form 8889

- **Caught by:** BUG-0292, recorded open; this entry closes it because the inventory is append-only.
- **Source:** f5329 p. 2, Part VII, line 42 "Enter the excess contributions from line 48 of your 2024 Form 5329"; i5329, Line 42, "only if the amount on line 49 of your 2024 Form 5329 is more than zero".
- **Symptom:** as recorded in BUG-0292.
- **Fix:** `person.x_other` names the earlier-year HSA excess whether or not a 2025 Form 8889 exists, and the `f5329.l4` remedy follows it. The question asks about the excess itself, including one the filer never reported, so it does not depend on a 2024 Form 5329 having been filed; this over-refuses an excess with no tax on 2024 line 49. No expression changed; lines 42 to 46 stay out of scope, as the form's note says of earlier-year excesses.
- **Fix lines:** `person.x_other`, `f5329.l4`
- **Siblings checked:** `f5329.l4`, `f5329.tax`, `f5329.l47`, `f5329.l48`, `f5329.l49`, `person.x_hsa_value`, `person.x_hsa_excess`, `f8889.line13`
- **Regression predictions:** `stage21.refuse.x_other` already answers the screen Yes with a Form 8889 present and refuses at line 4; its recorded remedy follows the new wording.
- **Validation:** person and f5329 reviews and the screen review rerun.
- **Tags:** source-definition-debt; wording; fixed

## BUG-0314 — Form 5329 Part I omits Roth, recapture, withdrawn-earnings and exception rules

- **Caught by:** the f5329 completeness review, its first run, 2026-11-02.
- **Source:** i5329 p. 1 (Roth distributions with an amount on Form 8606 line 25c; recapture amounts); p. 7 (earnings on a timely withdrawn IRA excess); p. 5 and p590b p. 28 (exception conditions).
- **Symptom:** nothing asks about these amounts or tests the exception conditions beyond the entry's own answer, so an early-distribution amount or an excluded amount on line 2 can be wrong.
- **Disposition:** T-175, with the next f5329/person pass: extend the questions or add refusals; rerun the reviews.
- **Validation:** two completeness claims, their quotes matched against the archive; no fixture or numerical evidence claimed.
- **Tags:** source-definition-debt; existing-form-pass; explicitly-deferred


## BUG-0315 — BUG-0307 is mostly fixed: the asset questions state the section 179, allowance, class, short-year and listed-use rules

- **Caught by:** BUG-0307, recorded open; this entry closes its claims 1 and 3 to 7, and claim 2 except for the used-property conditions, because the inventory is append-only. The used-property part stays open (owner question 1 in REPORT.md).
- **Source:** i4562 pp. 2-3, "Section 179 property is property that you acquire by purchase for use in the active conduct of your trade or business", "Property held for investment (section 212 property)", "for taxpayers other than a corporation, this election does not apply to any section 179 property you purchased and leased to others unless"; p946 p. 17, "Land and land improvements do not qualify as section 179 property", "If you buy qualifying property with cash and a trade-in, its cost for purposes of the section 179 deduction includes only the cash you paid"; i4562 p. 7, "Property described in section 168(k)(9)(A) or 168(k)(9)(B)"; pp. 10-11, the statutory classifications and "Qualified improvement property, as defined in section 168(e)(6), placed in service by you after December 31, 2017"; p946 p. 37, "You cannot use the percentage tables for a short tax year", and p. 46, Property Placed in Service Before a Short Tax Year; i4562 p. 14, the exclusions from qualified business use and the months rule for converted property; p. 3, "a portion of the taxpayer’s home is treated as a regular business establishment only if that portion meets the requirements for deducting expenses attributable to the business use of a home".
- **Symptom:** as recorded in BUG-0307. The premise check also found one amount-affecting case: qualified improvement property placed in service in 2017 and acquired after September 27, 2017 passes the screen (whose acquisition item stops only earlier acquisitions). The 2017 variant of `stage14.asset.qip` completed with Schedule C line 13 $2,001 (15-year straight line, recovery year 9), although the 15-year qualified improvement class applies only from 2018.
- **Fix:** `asset.s179` states what section 179 property is and the p946 p. 17 limits (land and land improvements, investment property, noncorporate leased property unless the two exceptions are met, cash paid only with a trade-in). `asset.screen` adds section 168(k)(9)(A)/(B) property; qualified rent-to-own, section 168(e)(3)(B)(vi) energy property, motorsports complexes, natural gas gathering lines, smart meter and smart grid property, and section 168(e)(3)(E)(v) transmission property; a tax year shorter than 12 months in 2025 or since placed in service; and listed property whose qualified business use is 50% or less after the p. 14 exclusions. `asset.listed` states the home limit on a regular business establishment. `asset.pct` states the months rule for listed property converted to business use in 2025. New gate `asset.qip_early` (class `cqip` and recovery year above 8, that is placed in service before 2018) is folded into `asset.screened`, so `asset.cost` refuses; the refusal's form text names it and the short tax year.
- **Fix lines:** `asset.s179`, `asset.screen`, `asset.listed`, `asset.pct`, `asset.qip_early`, `asset.screened`, `asset.cost`
- **Siblings checked:** `asset.is_section179` (still treats every non-QIP entry as section 179 property for Form 4562 line 2; matters only when line 2 exceeds the $4,000,000 threshold; owner question 3), `asset.s179_bad`, `asset.listed_low`, `asset.over_half`, `asset.bonus_choice`, `asset.class`, `scveh.s179_elect` (trade-ins already screened), `scveh.screen` (see BUG-0317); also generated, covered by the rerun reviews of their forms: `asset.after179`, `asset.basis`, `asset.cost`, `asset.f26i`, `asset.on_17`, `asset.on_19`, `asset.on_26_2025`, `asset.pct_bad`, `asset.pct_c`, `asset.s179_2025`, `asset.screened`, `sc.f14`, `sc.f17`, `sc.f19_y10`, `sc.f19_y15`, `sc.f19_y15sl`, `sc.f19_y20`, `sc.f19_y3`, `sc.f19_y5`, `sc.f19_y7`, `sc.f25_assets`, `sc.f26_assets`, `sc.f29_assets`, `sc.f6`
- **Regression predictions:** `stage14.asset.refuse_qip_2017` (the qip case placed in service in 2017) refuses at `asset.cost` with gate `asset.screened`; `stage14.asset.qip_2018` (placed in service in 2018) gives `asset.macrs2025` and Schedule C line 13 of $1,998 (Pub. 946 Table A-8, p. 76, 15-year column, year 8, 6.66% of $30,000). Both were written from the sources before the evaluator was run; both matched. The three existing refusal fixtures that quote the `asset.cost` refusal form (`stage14.asset.refuse_class`, `refuse_reuse_recycling`, `refuse_pre_2017`) follow the new wording. The other changes are wording only and change no evaluated value.
- **Validation:** fixtures 1,439/1,439 on the asset change alone; evaluator witnesses above. The integrator reruns the asset reviews and the completeness review.
- **Tags:** source-definition-debt; eligibility; amount-affecting (QIP); existing-form-pass; fixed

## BUG-0316 — BUG-0309 is fixed: the Schedule C questions and screens state or refuse the fifteen rules

- **Caught by:** BUG-0309, recorded open; this entry closes it because the inventory is append-only. Its presentation-only remainders (lines B and I, the Form 1099-NEC difference statement, the line 16b Form 1098 statement) are not computed amounts and are left as they were.
- **Source:** i1040sc p. 2, "a sporadic activity, a not-for-profit activity, or a hobby does not qualify as a business" and "unless you have elected to treat the domestic LLC as a corporation"; p. 9, Line 23, the sales tax collected from the buyer (line 1) and retained (line 6); p. 6, "Credit for federal tax paid on fuels claimed on your 2024 Form 1040 or 1040-SR"; i4562 p. 4, section 179 recapture on property not used more than 50%; i1040sc p. 4, long-term contracts, and p. 15, "are not a tax shelter (as defined in section 448(d)(3))"; p946 p. 17 (noncorporate lessors, trade-ins; in `asset.s179`, BUG-0315); i1040sc p. 8, prepaid and shared interest; p. 9, the travel limits and the meal conditions; p. 10, food program reimbursement, taxable fringe benefits and the timely filed, original return for the simplified method; p. 14, "You can’t deduct any excess mortgage interest, excess real estate taxes, or excess casualty losses on Schedule C for this home" and prior year unallowed passive activity losses; p. 1, qualified sound recording productions; i1040gi p. 94, "Your personal services must have been a material income-producing factor in the business"; i8995 pp. 2-3, the former-employee presumption and Form 1099-PATR.
- **Symptom:** as recorded in BUG-0309. Premise check: the specified agricultural or horticultural cooperative part of claim 17 already holds no gap: `qbi.unsupported` refuses any cooperative patron, and a Schedule C return with it answered Yes refuses at f1040 line 13a (evaluated).
- **Fix:** `sc.special` adds non-listed section 179 recapture, section 181 sound recording costs, prior year unallowed passive losses, the former-employee presumption, Form 1099-PATR amounts not reported as qualified items, an activity that is not a business, and a single-member LLC electing corporate treatment. `sc.method_other` adds tax shelters and long-term contracts. `sc.ho_other` adds a return that is not a timely filed original return. Wording states the rule in `sc.line1` (seller's sales tax collected), `sc.line6` (retained sales tax, federal fuel tax credit), `sc.line16a` and `sc.line23` (not the home's mortgage interest or real estate taxes), `sc.line16b` (prepaid part, shared mortgage, not the home), `sc.line24a` (one-year, companion and foreign convention limits), `sc.meals_50` (conditions, no entertainment, food program), `sc.line26` (fringe benefit amounts claimed elsewhere) and `sc.hi_uses` (personal services). No expression, gate or refusal declaration changed; the `sc.line1` refusal keeps its form and remedy text.
- **Fix lines:** `sc.special`, `sc.method_other`, `sc.ho_other`, `sc.line1`, `sc.line6`, `sc.line16a`, `sc.line16b`, `sc.line23`, `sc.line24a`, `sc.meals_50`, `sc.line26`, `sc.hi_uses`
- **Siblings checked:** `sc.screened` (reads `sc.special` and `sc.method_other`; refuses at `sc.line1`, which every Schedule C reads, checked by evaluation), `sc.ho_screened`, `sc.meals_80`, `sc.meals_100`, `sc.line48`, `qbi.unsupported`, `sc.f6`, `asset.s179`; also generated, covered by the rerun reviews of their forms: `sc.f7206_line14`, `sc.line28`, `sc.line28_pre179`, `sc.line3`, `sc.line7`, `sc.meals_50_ded`
- **Regression predictions:** no evaluated value changes and no fixture is added: every new refusal is a new item of an existing screen whose Yes already refuses (`stage14.refuse.special`, `stage14.refuse.method`). The interview text and the rendered sc page change.
- **Validation:** source inspection; evaluation of `sc.special`, `sc.method_other` and `qbi.unsupported` answered Yes on a Schedule C return. The integrator reruns the sc reviews and the completeness review.
- **Tags:** source-definition-debt; wording; existing-form-pass; fixed

## BUG-0317 — BUG-0311 is fixed for owned vehicles on actual expenses: the vehicle screen names the eight rules

- **Caught by:** BUG-0311, recorded open; this entry closes it because the inventory is append-only. Claim 11 (capitalized costs) is closed on the premise check, not by a change to scveh; see Symptom.
- **Source:** i4562 p. 7, "Property converted from business or income-producing use to personal use in the same tax year it is acquired"; p. 9, "the carryover basis of property you acquire in a like-kind exchange or involuntary conversion"; pp. 11-12, the method elections and "The following types of property must be depreciated under ADS"; p. 14, the exclusions from qualified business use and "Treat vehicles used by employees as being used 100% for business/investment purposes"; p. 15, the exception for a business of leasing passenger automobiles; p946 p. 37, the short tax year and casualty basis rules; p. 60, "If you have a short tax year, you must reduce the maximum deduction amount"; p. 63, adequate records.
- **Symptom:** as recorded in BUG-0311. Premise check of claim 11: i1040sc p. 6 exempts a small business taxpayer from capitalizing "certain expenses", and `sc.method_other` already refuses a business that must capitalize under section 263A because its gross receipts exceed $31 million (and now a tax shelter, BUG-0316). What remains is what "certain" leaves out and the creative property exception, which the archive (no Pub. 538) does not settle; owner question 5.
- **Fix:** `scveh.screen` adds conversion to personal use in 2025, an involuntary conversion or like-kind exchange, required or elected ADS and the straight line or 150% elections, a casualty basis reduction, a tax year shorter than 12 months, a business of leasing passenger automobiles, no adequate records, use by employees, and qualified business use of 50% or less after the p. 14 exclusions. Wording only; the refusal stays on `scveh.cost`.
- **Fix lines:** `scveh.screen`
- **Siblings checked:** `scveh.screened`, `scveh.cost`, `scveh.low_use`, `scveh.over_half`, `scveh.passenger`, `scveh.line7`, `scveh.rate_hy`, `scveh.rate_prior`, `scveh.line9`, `scveh.lease_business`, `scveh.smr_ok`.
- **Regression predictions:** no evaluated value changes and no fixture is added. Checked by evaluation on `stage14.veh.refuse_lease_smr_before` variants: an owned vehicle on actual expenses (5,000 business and 1,000 other miles) completes with Schedule C line 13 $16,833.33 with the screen answered No and refuses at f1040 line 24 with gate `scveh.screened` when it is answered Yes. With the screen answered Yes, the standard mileage rate path and the leased actual-expense path still complete: they do not read `scveh.screen`. The new items are depreciation and limit rules, which those paths do not compute, except employee use (owner question 4).
- **Validation:** source inspection and the evaluations above. The integrator reruns the scveh reviews and the completeness review.
- **Tags:** source-definition-debt; wording; existing-form-pass; fixed

## BUG-0318 — BUG-0302 is partly fixed: the Schedule A medical and tax questions carry the definition rules

- **Caught by:** BUG-0302, recorded open; this entry closes its line 1, 5a and 5b parts because the inventory is append-only. The line 12 and blindness parts stay open (BUG-0319, BUG-0320).
- **Source:** i1040sca p. 1, "If you received a distribution from a health savings account or a medical savings account in 2025, see Pub. 969 to figure your deduction", "You can't include insurance premiums paid by making a pretax reduction to your employee compensation", "If you are a retired public safety officer, you can't include any premiums you paid to the extent they were paid for with a tax-free distribution from your retirement plan", "If you paid someone to do both nursing and housework, you can deduct only the cost of the nursing help", "Lodging expenses (but not meals) while away from home to receive medical care", "Certain medical expenses paid out of a deceased taxpayer's estate can be claimed on the deceased taxpayer's final return"; p. 2, the long-term care premium limit chart and "Don't deduct more than $50 a night for each person"; p969 pp. 9 and 13, "You can’t deduct qualified medical expenses as an itemized deduction on Schedule A (Form 1040) that are equal to the tax-free distribution from your HSA" (Archer MSA); i1040sca p. 3, "Include taxes imposed by a U.S. territory with your state and local taxes on lines 5a, 5b, and 5c. However, don't include any U.S. territory taxes you paid that are allocable to excluded income"; p. 6, "Only taxes paid in 2025 and assessed prior to 2026 can be deducted for 2025".
- **Symptom:** as recorded in BUG-0302 for `sa.line1`, `sa.line5a` and `sa.line5b`. The completeness claim named only line 5a for territory taxes; the source sentence on p. 3 names lines 5a, 5b and 5c.
- **Fix:** wording only. `sa.line1` lists the exclusions (amounts equal to tax-free HSA or Archer MSA distributions, pretax premiums, a retired public safety officer's premiums paid with a tax-free plan distribution, the housework part of mixed pay, meals away from home other than hospital care, lodging over $50 a night per person), the long-term care premium limit by age with the chart amounts, and the estate-paid expenses on a final return by reference to Pub. 502. `sa.line5a`, `sa.line5b` and `sa.line5c` include U.S. territory taxes except those allocable to excluded income; `sa.line5a` also excepts territory income taxes taken as a credit; `sa.line5b` states the paid-in-2025-and-assessed-before-2026 rule. Each input now cites i1040sca (and p969 for line 1) instead of the generic Schedule A locator. No expression, gate or refusal changed.
- **Fix lines:** `sa.line1`, `sa.line5a`, `sa.line5b`, `sa.line5c`
- **Siblings checked:** `sa.line4`, `sa.line5d`, `sa.line5e`, `sa.excluded_income` (refuses excluded income, so the excluded-income exception needs no gate), `sa.unsupported` (foreign tax deduction), `ftc.taxes`, `ltc.limit` (Form 7206 uses the same age chart; not reused because Schedule A asks for one amount for all persons).
- **Regression predictions:** no evaluated value changes; every fixture result is unchanged and no fixture is added because no behavior changed. The interview text and the rendered sa page change.
- **Validation:** source inspection; the integrator reruns the sa transcription, render and completeness reviews.
- **Tags:** source-definition-debt; wording; schedule-a; fixed

## BUG-0319 — Line 12 noncash gifts: the good-used-condition rule and the $250 acknowledgment are stated in the gift question

- **Caught by:** the T-169 premise check of BUG-0302, line 12 part.
- **Source:** i1040sca p. 11, "A deduction for these contributions will be allowed only if the items are in good used condition or better. However, this rule doesn't apply to a contribution of any single item for which a deduction of more than $500 is claimed and for which you include a qualified appraisal and Form 8283 with your tax return"; "If the gift of property is $250 or more, you must also have a contemporaneous written acknowledgment from the charity."
- **Symptom:** `sa.line12` has no question of its own; it sums `gift.allowed`, which copies `gift.deduction`. `gift.special` already refuses "a clothing or household item over $500 not in good used condition", so the appraisal exception that BUG-0302 names is refused, not missed. What remains: a clothing or household item of $500 or less not in good used condition is not deductible, and `gift.deduction` does not say so; nothing asks for the contemporaneous written acknowledgment for a gift of property of $250 or more.
- **Fix:** owner decision 2026-11-02: the `gift.deduction` question states the good-used-condition rule and the $250 contemporaneous written acknowledgment, citing i1040sca p. 11; no gate.
- **Fix lines:** `gift.deduction`
- **Siblings checked:** `gift.special`, `gift.allowed`, `sa.line12`; also generated, covered by the rerun reviews of their forms: `gift.section_b`
- **Regression predictions:** wording only; no expression changed.
- **Validation:** gift reviews rerun under Claude and DeepSeek; gift completeness ruled.
- **Tags:** source-definition-debt; schedule-a; charity; fixed

## BUG-0320 — The blindness question does not state the partial-blindness definition or the certified statement (open; the question is in `person`)

- **Caught by:** the T-169 premise check of BUG-0302, blindness part.
- **Source:** i1040gi p. 33, Blindness, "If you weren’t totally blind as of December 31, 2025, you must get a statement certified by your eye doctor (ophthalmologist or optometrist) that: • You can't see better than 20/200 in your better eye with glasses or contact lenses, or • Your field of vision is 20 degrees or less."
- **Symptom:** `sa.boxes_blind` counts `person.blind`, whose question is "Are you blind under the standard-deduction instructions?" in `person.yaml`, with the generic Schedule A locator. A partially blind filer may answer no.
- **Disposition:** needs a change to `person.blind` (form `person`), outside this pass's FORMS. Owner question in REPORT.md.
- **Validation:** source and implementation inspection.
- **Tags:** source-definition-debt; standard-deduction; explicitly-deferred

## BUG-0321 — Line 1 premiums are reduced by the self-employed health insurance deduction and advance credit payments

- **Caught by:** the T-169 rewording of `sa.line1`, reading the Line 1 section.
- **Source:** i1040sca p. 2, Line 1, "If advance payments of the premium tax credit were made or you think you may be eligible to claim a premium tax credit, fill out Form 8962 before filling out Schedule A, line 1"; "if you claimed the self-employed health insurance deduction on Schedule 1 (Form 1040), line 17, reduce the premiums by the amount on line 17"; p. 1, "Reduce the insurance premiums by any self-employed health insurance deduction you claimed on Schedule 1 (Form 1040), line 17."
- **Symptom:** the project computes `s1.line17` and Form 8962, but `sa.line1` asks for one supplied amount and does not tell the filer to subtract the premiums deducted on Schedule 1 line 17 or the premiums covered by the premium tax credit. A self-employed filer who itemizes can count the same premiums twice. Not reproduced by evaluation.
- **Fix:** owner decision 2026-11-02 (wording, not a computed split): `sa.line1` tells the filer to reduce premiums by the Schedule 1 line 17 deduction (i1040sca p. 2, quoted) and to leave out premiums paid by advance payments of the premium tax credit. The second clause is an inference from "after you reduce these expenses by any payments received from insurance or other sources"; how a net premium tax credit claimed on the return interacts is left to T-180 after Pub. 974 is archived.
- **Fix lines:** `sa.line1`
- **Siblings checked:** `s1.line17`, `sc.f7206_line14`, `f8962.line24`; also generated, covered by the rerun reviews of their forms: `sa.line4`
- **Regression predictions:** wording only; no expression changed.
- **Validation:** sa reviews rerun.
- **Tags:** source-definition-debt; schedule-a; cross-form; fixed

## BUG-0322 — T-164 is fixed: f8962.premium_adjust asks only about Marketplace coverage and 2025 months

- **Caught by:** the f8962 screen review's WIDE and UNCLEAR findings on `f8962.premium_adjust`, ruled accepted over-refusal and recorded as T-164; this entry closes T-164.
- **Source:** i8962 p. 4, "Generally, if coverage in a qualified health plan began after the first day of the month, you are not allowed a monthly credit amount for the coverage for that month."; p. 4, "The enrollment premiums are the total amount of the premiums for the month, reduced by any premium amounts for that month that were refunded in 2025"; p. 5, "Catastrophic health plans and stand-alone dental plans purchased through the Marketplace, and all plans purchased through the Small Business Health Options Program (SHOP), are not qualified health plans for purposes of the PTC."
- **Symptom:** the question asked whether "coverage for anyone in your tax family began after the first day of a month" and whether "any Marketplace premiums for a month [were] refunded in 2025". A dependent's employer or Medicaid coverage starting mid-month, or a 2025 refund of a 2024 month's premium, read as yes and refused a return whose column A is right as reported. Over-refusal only; no amount was wrong.
- **Fix:** the question and its interview help ask about Marketplace coverage reported on a Form 1095-A (a qualified health plan) that began after the first day of a 2025 month, and about premiums for a 2025 month of that coverage refunded in 2025; they say a start date of other coverage (employer, Medicaid, a catastrophic, stand-alone dental or SHOP plan) does not count. The cite adds the p. 5 sentence. No expression changed; the refusal remedy is unchanged.
- **Fix lines:** `f8962.premium_adjust`
- **Siblings checked:** `f8962.line24`, `f8962.line25` (the sibling tool on f8962.premium_adjust: no same-anchor siblings)
- **Regression predictions:** `stage18.refuse.premium_adjust` already answers the gate yes and refuses at `f8962.line24`, `f8962.line25` and `s3.line9`; evaluated on the changed tree it still refuses there, and the same inputs with the gate answered no complete (line 24 $3,560, line 25 $3,500). No fixture changed because no expression changed. Fixtures 1,437/1,437.
- **Validation:** source inspection; f8962 screen review to be rerun by the integrator.
- **Tags:** source-definition-debt; wording; premium-tax-credit; fixed

## BUG-0323 — BUG-0298 is fixed: the column B questions no longer say "zero if blank" for a covered month

- **Caught by:** BUG-0298, recorded open (T-165); this entry closes it.
- **Source:** i8962 p. 5, "Form 1095-A, Part III, column B, may be wrong or blank or may report your applicable SLCSP premium as -0-. ... In either case, you must determine your correct applicable SLCSP premium."; p. 17, "If columns (a) and (b) of any of lines 12 through 23 are blank, leave column (c) of the corresponding line blank."
- **Symptom:** as recorded in BUG-0298. Reproduced on the unchanged expressions: one Form 1095-A, January to June covered (column A $500, column B $450, column C $300 a month), not uniform; entering column B as zero for March, as "zero if blank" invites, completes the return with Form 8962 line 24 $1,485 against $1,782 with the correct $450, the $297 credit for March lost. No refusal stops it.
- **Fix:** the twelve monthly column B questions and the uniform one say to use the amount in column B, or the correct applicable SLCSP premium if column B is blank, wrong, or zero for a month whose premiums were paid by the due date of the return; and zero if no one was enrolled in the policy that month or if the premiums were not paid by the due date (i1095a p. 3; i8962 p. 16). The thirteen column A questions take the premiums paid by the due date even when column A shows zero (i8962 p. 16). A partial payment that kept coverage in force is still treated as unpaid; BUG-0327 records it. An earlier draft, "zero only if no one was enrolled", was corrected before commit after the render review found it would replace a correct $0.
- **Fix lines:** `f1095a.in_b_jan` through `f1095a.in_b_dec`, `f1095a.mo_b`, `f1095a.in_a_jan` through `f1095a.in_a_dec`, `f1095a.mo_a`
- **Siblings checked:** `f1095a.b_jan`–`f1095a.b_dec`, `f1095a.yr_b_monthly`, `f1095a.mo_b` (the sibling tool on f1095a.in_b_jan); the column A and C questions keep "zero if blank", which is right for them.; also generated, covered by the f1095a reviews rerun on the final wording: `f1095a.a_apr`, `f1095a.a_aug`, `f1095a.a_dec`, `f1095a.a_feb`, `f1095a.a_jan`, `f1095a.a_jul`, `f1095a.a_jun`, `f1095a.a_mar`, `f1095a.a_may`, `f1095a.a_nov`, `f1095a.a_oct`, `f1095a.a_sep`, `f1095a.b_apr`, `f1095a.b_aug`, `f1095a.b_feb`, `f1095a.b_jul`, `f1095a.b_jun`, `f1095a.b_mar`, `f1095a.b_may`, `f1095a.b_nov`, `f1095a.b_oct`, `f1095a.b_sep`, `f1095a.yr_a_monthly`, `f1095a.yr_a_uniform`, `f1095a.yr_b_uniform`
- **Regression predictions:** no expression changed, so no fixture can tell the wording apart; the reproduction above is recorded in the C-backlog report, not as a fixture. Fixtures pass unchanged.
- **Validation:** source inspection and evaluation of the reproduction; f1095a and f8962 reviews to be rerun by the integrator.
- **Tags:** source-definition-debt; wording; premium-tax-credit; fixed

## BUG-0324 — BUG-0299 is fixed: f8962.other defines "affordable" for the employee and for family members

- **Caught by:** BUG-0299, recorded open (T-166); this entry closes it.
- **Source:** i8962 p. 5, "The coverage offered by your employer is generally considered affordable for you if your share of the annual cost for self-only coverage, which is sometimes referred to as the “employee required contribution,” is not more than 9.02% of your household income."; p. 5, "coverage if your share of the annual cost for coverage for yourself and the other members of your tax family allowed to enroll in the coverage is not more than 9.02% of your household income."; p. 5, "If your employer coverage is affordable for you but not affordable for your other family members, you may be able to take the PTC for your other family members if they enroll in a Marketplace qualified health plan."
- **Symptom:** as recorded in BUG-0299 (an employee whose self-only cost is affordable but whose family cost is not could answer no and keep the PTC for the employee's own months).
- **Fix:** the employer limb of the `f8962.other` question states the test: for the employee, the employee's share of the annual cost of self-only coverage is not more than 9.02% of household income (Form 8962, line 3), whatever family coverage costs; for another member of the tax family allowed to enroll, the employee's share of the annual cost of coverage for the employee and the family members allowed to enroll is not more than 9.02%. The cite adds the three p. 5 sentences. No expression changed; the Marketplace-determination exception stays omitted (accepted over-refusal in the f8962.other screen ruling).
- **Fix lines:** `f8962.other`
- **Siblings checked:** `f8962.line24`, `f8962.line25` (the sibling tool on f8962.other: no same-anchor siblings)
- **Regression predictions:** no expression changed; existing fixtures that answer `f8962.other` yes still refuse (see the report). Fixtures pass unchanged.
- **Validation:** source inspection; f8962 reviews and completeness to be rerun by the integrator.
- **Tags:** source-definition-debt; wording; premium-tax-credit; fixed

## BUG-0325 — An asset past its GDS recovery period is never screened, so ADS and low-use listed property complete with $0 depreciation (open)

- **Caught by:** the cloud ruling audit `claude/ruling-audit-1` (findings C1 and C2), 2026-11-02; C1 reproduced locally on `main` 5eec22f.
- **Source:** i4562 p. 9, Line 17, "For tangible property placed in service in tax years beginning before 2025 and depreciated under MACRS ... enter the deductions for the current year", MACRS including GDS and ADS; p. 13, Column (g), "use the straight line method over the ADS recovery period"; p946 Table B-1 class 00.11 (GDS 7, ADS 10) and Table A-8.
- **Symptom:** `asset.screen` and `asset.listed_low` refuse through `asset.cost` and `asset.basis`, which a prior-year asset reads only inside its GDS period. Past it (`asset.done`), the screen, cost, percentage and listed questions are never asked and the return completes with $0 for the asset. Witness: office furniture placed in service in 2015 under ADS, year 11 of 10: Schedule C line 13 is $0 where the source gives $500, with no refusal.
- **Disposition:** T-176, top of queue 1: declare the refusals on a line every asset reads, or ask about ADS before `asset.done`; check other classes and exchanged basis.
- **Validation:** the audit's witnesses and interview replay; local evaluation of the C1 witnesses and control. C2 not run locally.
- **Tags:** eligibility; amount-affecting; refusal-placement; explicitly-deferred

## BUG-0326 — Completeness gaps found after the A-backlog wording: Schedule C, vehicle, Schedule A and asset rules

- **Caught by:** the sc, scveh, sa and asset completeness reviews rerun on the merged A-backlog tree, 2026-11-02.
- **Source:** i1040sc pp. 5-9 and 13 (vehicle count and first-year standard rate on line 9; installment method; materials and supplies; licenses to amortize; incidental-expense method; home depreciation with the simplified method); p946 pp. 17-18 (excepted section 179 property); i1040gi p. 94 (QSEHRA eligibility); i1040sc p. 6 (capitalized vehicle costs); i1040sca pp. 2-7 (whose medical expenses count; penalties, interest and state disability funds on 5a; levies and service charges on 5b; the value-only test on 5c); i4562 p. 10 (statutory recovery classes).
- **Symptom:** the questions neither state nor refuse these rules, so a filer can misstate an expense or an itemized deduction. Most can change an amount.
- **Disposition:** T-183, with the next sc, scveh, sa and asset passes: extend the questions or add refusals; rerun the reviews.
- **Validation:** completeness claims with their quotes matched against the archive (one asset quote did not match and is recorded as unverified).
- **Tags:** source-definition-debt; explicitly-deferred

## BUG-0327 — Form 8962 does not ask about months whose premiums were unpaid by the due date, or other corrected-SLCSP situations

- **Caught by:** the f8962.premium_adjust screen review (NARROW) and the f8962 completeness review, 2026-11-02.
- **Source:** i8962 p. 14, "You are not allowed a monthly credit amount for any month that the enrollment premiums for the month were not paid by the due date of your return (not including extensions), unless the amount of the premium paid for the month is sufficient to avoid termination of the coverage"; i8962 pp. 14-17, the situations that require a corrected applicable SLCSP premium.
- **Symptom:** the column A and B questions now treat a month whose premiums were not paid by the due date as zero, which is right for an unpaid month but also zeroes a partial payment that kept coverage in force (i8962 p. 16); nothing asks about a covered individual who is not lawfully present; and nothing asks whether the filer's share of a month's premium was unpaid by the due date, or about the other corrected-SLCSP situations, so a month's credit can be allowed where the source disallows it.
- **Disposition:** T-180, with the column B work: ask or refuse, citing i8962 p. 14; check Pub. 974, which is archived.
- **Validation:** one screen-review finding and one completeness claim, quotes matched; not reproduced by evaluation.
- **Tags:** eligibility; premium-tax-credit; amount-affecting; explicitly-deferred

## BUG-0328 — BUG-0325 is fixed: an asset past its GDS period is still screened

- **Caught by:** BUG-0325, recorded open; this entry closes it because the inventory is append-only.
- **Source:** i4562 p. 9, Line 17; p. 13, Column (g), "use the straight line method over the ADS recovery period"; p. 15, Column (f), "used 50% or less ... straight line method over its ADS recovery period"; p946 Table B-1.
- **Symptom:** as recorded in BUG-0325.
- **Fix:** the `asset.screened` and `asset.listed_low` refusals are also declared on `asset.done`, which every asset placed in service before 2025 reads to decide whether its recovery period has ended, so the screen, use percentage and listed questions are asked and a Yes refuses there. Accepted over-refusal: listed property used 50% or less whose ADS period has also ended owes no depreciation but is refused.
- **Fix lines:** `asset.done`
- **Siblings checked:** `asset.macrs_prior`, `asset.dep_prior`, `asset.cost`, `asset.basis`, `asset.screened`, `asset.listed_low`
- **Regression predictions:** `stage14.asset.refuse_ads_past_gds` (office furniture placed in service in 2015 under ADS, screen Yes) and `stage14.asset.refuse_listed_low_past_gds` (listed property at 40% placed in service in 2015) both refuse at `asset.macrs_prior`, where the unfixed tree gave $0 with no refusal. Written from the source before the evaluator was run, from the cloud audit's witnesses.
- **Validation:** fixtures 1,441/1,441; asset reviews rerun.
- **Tags:** eligibility; amount-affecting; refusal-placement; fixed


## BUG-0329 — A returned kidnapped child who lived with you more than half of 2025 was refused

- **Caught by:** T-105 (T-092 split, fixr2 dependent F1); premise reproduced on the current tree by reading the
  refusals (`dependent.lived_half` and `dependent.eic_child` refused on `dependent.kidnapped` alone), 2026-11-03.
- **Source:** p501 p. 13, Kidnapped child, "You can treat your child as meeting the residency test even if the child
  has been kidnapped, but the following statements must be true."; i1040gi p. 17, Step 1, "Who lived with you for
  more than half of 2025"; p. 41, Step 3.
- **Symptom:** a child presumed kidnapped and since returned, who lived with you 11 or 12 months of 2025, was refused
  at the residency tests although the kidnapped-child treatment is not needed to meet them. Over-refusal; no wrong
  amount.
- **Fix:** gates `dependent.kidnap_residency` (kidnapped and fewer than 7 months) on `dependent.lived_half` and
  `dependent.kidnap_eic` (kidnapped, EIC relationship, not in the United States for more than half of 2025) on
  `dependent.eic_child`. `dependent.months` and `dependent.us_half` now say that time a kidnapped child was missing
  does not count, so the refusal still catches every case that needs the treatment. T-104 rewords
  `dependent.kidnapped`: a child missing because of a kidnapping at some time in 2025, whenever law enforcement first
  presumed it (p501 p. 13 ties the year to the kidnapping). The row's suggested wording ("kidnapped in 2025") would
  have dropped a child kidnapped earlier and returned in 2025, whose year of return still applies the rule; the new
  question keeps that case.
- **Fix lines:** `dependent.kidnapped`, `dependent.kidnap_residency`, `dependent.kidnap_eic`, `dependent.lived_half`,
  `dependent.eic_child`, `dependent.months`, `dependent.us_half`
- **Siblings checked:** `dependent.qr_kidnapped` (unchanged: the qualifying-relative branch still refuses any child; also generated, covered by the reviews rerun on the integrated tree: `dependent.eic_child`, `dependent.kidnap_eic`, `dependent.kidnap_residency`, `dependent.lived_half`
  under 19 presumed kidnapped), `household.qss_child` wording (unchanged, its own kidnapped sentence),
  `f1040.line12e` QSS remedy (unchanged), `dependent.hoh_lived_half`, `dependent.dc_lived_half` (both read
  `lived_half`, so they inherit the narrower refusal).
- **Regression predictions:** `f1.kidnapped.returned_11` (11 months, in the United States more than half the year):
  qualifying child, EIC qualifying child, EIC $3,261 (i1040gi p. 53 table rows $25,000 and $30,000, one child).
  `stage21.d3.kidnapped_child_refused` moves to 4 months and not in the United States for more than half the year and
  is refused at line 16 (`kidnap_residency`) and line 27a (`kidnap_eic`). The two `stage21.f1.where_kidnapped_withheld_*`
  evaluator regressions move their withheld child to 4 months (and the EIC case out of the U.S. half-year) so the
  kidnapped answer still decides an unanswered gate; their expectations are unchanged. Predictions written before the
  evaluator was run.
- **Validation:** CLI fixtures; dependent transcription/render reviews rerun (Claude); completeness rerun.
- **Tags:** over-refusal; residency; fixed

## BUG-0330 — BUG-0283 is fixed: a non-taxpayer's qualifying child can be your qualifying relative

- **Caught by:** BUG-0283 (T-153), recorded open; this entry closes it because the inventory is append-only.
- **Source:** i1040gi p. 19, Step 4, "Who wasn’t a qualifying child (see Step 1) of any taxpayer for 2025. For this
  purpose, a person isn’t a taxpayer if the person isn’t required to file a U.S. income tax return and either doesn’t
  file such a return or files only to get a refund of withheld income tax or estimated tax paid."; p501 p. 18, Child of
  person not required to file a return, Examples 1 to 3, and Child in Canada or Mexico; p501 p. 15, Qualifying Child of
  More Than One Person.
- **Symptom:** as recorded in BUG-0283; in addition, the EIC tie-breaker refusal on `dependent.eic_child` fired for any
  listed person answering `other_claimant` Yes, including one who is not your EIC qualifying child.
- **Fix:** new input `dependent.other_nontaxpayer`. Gate `dependent.qc_tiebreak` replaces `other_claimant` on
  `dependent.qualifying_child`: it refuses when the person is the qualifying child of another person and either is
  also your qualifying child (the tie-breaker rules have no non-taxpayer exception, so the refusal stands whatever the
  other person's filing) or the other person is a taxpayer. Gate `dependent.eic_tiebreak` replaces it on
  `dependent.eic_child` and refuses only a child who passes your EIC relationship, age, joint-return and residency
  tests. The row's suggested fix (define the taxpayer in `other_claimant` itself) would also have lifted the
  tie-breaker refusal for your own qualifying child whose other parent does not file, which p501 pp. 15-16 do not
  support; the split avoids that.
- **Fix lines:** `dependent.other_nontaxpayer`, `dependent.qc_tiebreak`, `dependent.eic_tiebreak`,
  `dependent.qualifying_child`, `dependent.eic_child`
- **Siblings checked:** `dependent.qualifying_relative` (unchanged; it reads `dependent.qualifying_child`, whose refusal is now; also generated, covered by the reviews rerun on the integrated tree: `dependent.eic_child`, `dependent.qc_tiebreak`, `dependent.qualifying_child`
  the gate), `eic.qc_of_another` (the filer as another's qualifying child; separate input, unchanged),
  `dependent.other_claimant` question (unchanged; still includes the EIC rules, so a Yes under the EIC rules alone and
  a taxpayer other person still refuses: accepted over-refusal).
- **Regression predictions:** `f1.t153.friend_child_nontaxpayer` (p501 p. 18 Example 1 on a joint return): not your
  qualifying child, your qualifying relative, line 19 $500. `f1.t153.friend_child_taxpayer` (Example 3): refused at
  `qc_tiebreak`. `f1.t153.own_child_nontaxpayer_other`: your own child, other person not a taxpayer, still refused at
  `qc_tiebreak`. `stage8.refuse.dependent.other_claimant` and `stage9.eic.refuse.child_of_another` keep their refusals
  under the new gate ids without answering the new input. Written before the evaluator was run.
- **Validation:** CLI fixtures; eight consumer pairs ruled `same` in `reviews/2025/consumers.json`.
- **Tags:** over-refusal; qualifying-relative; fixed

## BUG-0331 — BUG-0285 is fixed: the lifetime learning credit is refused for a student whose ITIN or ATIN was only applied for

- **Caught by:** BUG-0285 (T-113), recorded open; owner decision T-113 (2026-11-01).
- **Source:** i8863 p. 3, Who cannot claim a credit, "5. The student has not been issued a TIN by the due date of his or
  her 2025 return (including extensions)."; i8863 p. 3, Table 1, lifetime learning column, "Students must have been
  issued a TIN by the due date of their 2025 return (including extensions)"; p970 p. 11 (the deeming sentence, in the
  American opportunity credit chapter only).
- **Symptom:** as recorded in BUG-0285; the person side had the same reading (`person.edu_student` accepts
  `person.itin_applied`).
- **Fix:** gates `dependent.edu_llc_tin_refused` (new input `dependent.edu_tin_issued` No) and
  `person.edu_llc_tin_refused` (`person.tin` No, so only `itin_applied`) refuse line 31 of a lifetime learning credit
  student. `edu_student` and the American opportunity credit are unchanged (p970 p. 11's deeming). Table 1's lifetime
  learning column requires only the student's TIN, so "or filer" in the owner decision is read as the filer who is
  the student; a filer whose ITIN was only applied for and who claims the credit for a dependent student with an
  issued number is not refused.
- **Fix lines:** `dependent.edu_tin_issued`, `dependent.edu_llc_tin_refused`, `dependent.edu_line31`,
  `person.edu_llc_tin_refused`, `person.edu_line31`
- **Siblings checked:** `dependent.edu_aoc`, `person.edu_aoc` (deeming kept through `household.all_tin`),; also generated, covered by the reviews rerun on the integrated tree: `dependent.edu_line27`, `dependent.edu_line28`, `dependent.edu_line29`, `dependent.edu_line30`, `dependent.edu_line31`, `dependent.edu_llc_tin_refused`
  `dependent.edu_llc`, `person.edu_llc`, `f8863.line10`, `household.tin_count`.
- **Regression predictions:** `f1.t113.dep_llc_applied` (stage19.blind.e3, daughter's ATIN applied for) and
  `f1.t113.person_llc_itin_applied` (stage19.example.llc_phaseout, taxpayer's ITIN applied for) refuse at line 31 and
  Part II line 10. `f1.t113.dep_aoc_applied` (stage19.example.jack_kay) and `f1.t113.person_aoc_itin_applied`
  (stage19.example.aoc_phaseout) keep every value. Written before the evaluator was run.
- **Fixture context repair:** `stage19.blind.e3`, `stage19.blind.e9`, `stage19.refuse.period_over_dependent` and
  `stage21.pending1.qss_valid_computes` answer the new input Yes (inferred from their "has a TIN" answer), annotated
  in each evidence note; no expected value changed.
- **Over-refusal accepted:** the return is refused rather than prepared without the lifetime learning credit for that
  student, as the owner decided.
- **Validation:** CLI fixtures; dependent and person transcription/render reviews rerun (Claude).
- **Tags:** eligibility; education; owner-decision; fixed

## BUG-0332 — Form 2441 line 2 columns (c) and (d) were shown for a person who is not a qualifying person

- **Caught by:** T-112 (t091 dependent.classm L1); premise confirmed: neither line had `shown_when`.
- **Source:** i2441 p. 3, Line 2, "Don't list a person on line 2 unless they are listed as an eligible person under
  Qualifying Person(s), earlier".
- **Symptom:** the values sheet showed a line 2 row for every listed dependent; on
  `stage15.regress.f2441.nonqualifying_dependent` four line 2 entries instead of two. No amount changed.
- **Fix:** `shown_when: dependent.dc_qp` on `dependent.dc_line2c` and `dependent.dc_line2d`.
- **Fix lines:** `dependent.dc_line2c`, `dependent.dc_line2d`
- **Siblings checked:** the Form 2441 line 2 column (d) total (sums dependent.dc_line2d over qualifying persons only; unchanged), `dependent.dc_qp`.; also generated, covered by the reviews rerun on the integrated tree: `dependent.dc_age13`, `dependent.dc_child_all_year`, `dependent.dc_disabled_qp`, `dependent.qc_age`, `dependent.qr_kidnapped`, `dependent.under_ctc_age`
- **Regression predictions:** `f1.dc.line2_shown_qualifying_only` asserts the condition (`dc_qp` true and false) and
  line 3 $3,000; the values-sheet count (four to two) was checked by hand with `eval --html`, since fixtures cannot
  assert visibility.
- **Validation:** CLI fixtures; render review rerun.
- **Tags:** display; source-transcription; fixed

## BUG-0333 — BUG-0282 is fixed: support-definition details in the dependent support questions

- **Caught by:** BUG-0282 (T-107, T-108, T-109), recorded open.
- **Source:** p501 p. 15 (foster care payments and expenses), p. 20 (total support, tax-exempt income, year support is
  provided, armed forces allotments and quarters allowances, state support of a needy person, home for the aged),
  p. 21 (own home, rent free, property, capital expenses, medical insurance premiums and benefits, GI Bill, childcare,
  Don't Include in Total Support items 1 to 6).
- **Symptom:** as recorded in BUG-0282; T-108's sentence could be read as the state supporting the filer.
- **Fix:** `dependent.supported` and `dependent.self_support` state the total-support definition and the listed rules;
  "Benefits a state provides to this person as a needy person". Wording only; a filer who answered from the shorter
  text and now counts differently may move between a computed dependent and none. Not a support worksheet.
- **Fix lines:** `dependent.supported`, `dependent.self_support`
- **Siblings checked:** `dependent.qc_tiebreak`, `dependent.qualifying_child`, `dependent.qualifying_relative`; covered by the dependent reviews rerun on the integrated tree
- **Regression predictions:** none (no expression changed).
- **Validation:** dependent render and completeness reviews rerun.
- **Tags:** source-definition-debt; wording; fixed

## BUG-0334 — BUG-0284 is fixed: the care-expense question names child support and the allocation rules

- **Caught by:** BUG-0284 (T-154), recorded open.
- **Source:** i2441 p. 2 ("Child support payments aren't qualified expenses."; "you must figure your expenses for each
  day"); p503 p. 6 (temporary absence, part-time work); p503 p. 8 (expenses partly work related).
- **Fix:** `dependent.dc_paid` adds the child-support exclusion, day-by-day allocation with its two exceptions, and the
  mixed-purpose division; existing exclusions kept. Wording only.
- **Fix lines:** `dependent.dc_paid`
- **Siblings checked:** `dependent.dc_line2d`; covered by the reviews rerun on the integrated tree
- **Tags:** source-definition-debt; wording; fixed

## BUG-0335 — BUG-0300 is fixed: a stillborn child is excluded and a live birth is required

- **Caught by:** BUG-0300 (T-167). **Source:** p501 p. 13, Child born alive and Stillborn child.
- **Fix:** `dependent.born_died` states the live-birth requirement (state or local law, official record) and says not
- **Fix lines:** `dependent.born_died`
- **Siblings checked:** `dependent.dc_lived_half`, `dependent.hoh_lived_half`; covered by the reviews rerun on the integrated tree
  to list a stillborn child. Consumer pairs `born_died@p501:p9` and `born_died@p503:p3` ruled `same`. Wording only.
- **Tags:** source-definition-debt; wording; fixed

## BUG-0336 — BUG-0301 is fixed: the dependent student question defines a school and treats co-op students as full-time

- **Caught by:** BUG-0301 (T-168). **Source:** p501 p. 13, Student defined, Full-time student, School defined,
  Vocational high school students.
- **Fix:** `dependent.student` adds the school definition, the school's own full-time standard, non-consecutive months
- **Fix lines:** `dependent.student`
- **Siblings checked:** `dependent.qc_age`; covered by the reviews rerun on the integrated tree
  and the co-op rule. Wording only.
- **Tags:** source-definition-debt; wording; fixed

## BUG-0337 — Dependent question wording: newborn hospital stay, revoked release, TANF for a parent's home

- **Caught by:** T-106 (completeness r7), T-110 (completeness r3/r4), T-111 (fixr4).
- **Source:** p501 p. 13, Death or birth of child ("except for any required hospital stay following birth"); p501
  p. 22, Revocation of release of claim to an exemption ("written notice of the revocation to the noncustodial parent in
  2024 or earlier"); p501 p. 9, Note (TANF).
- **Fix:** `dependent.months` counts a newborn's required hospital stay; `dependent.divorced_rule` says a release
  revoked without notice in 2024 or earlier still applies for 2025; `dependent.parent_home_paid` counts TANF used for the
  home as paid by you (the household question already carried this sentence, T-115). Wording only.
- **Fix lines:** `dependent.months`, `dependent.divorced_rule`, `dependent.parent_home_paid`
- **Siblings checked:** `dependent.hoh_test1`, `dependent.kidnap_residency`, `dependent.lived_half`, `dependent.qualifying_child`; covered by the reviews rerun on the integrated tree
- **Tags:** source-definition-debt; wording; fixed

## BUG-0338 — The care-expense question omits household services, provider transportation, agency fees and the volunteer-work rule (open)

- **Caught by:** dependent completeness review (Claude), claim dependent#1, on the F1 branch, 2026-11-03.
- **Source:** i2441 p. 2, "These include amounts paid for household services and care of the qualifying person while you
  worked or looked for work." and "However, they don't include the services of a chauffeur, bartender, or gardener.";
  p503 p. 6, "you aren't considered to be working if you do unpaid volunteer work or work for a nominal salary"; p503
  pp. 7-8 (transportation by a care provider, agency fees and deposits, forfeited deposits, a housekeeper's meals and
  lodging).
- **Symptom:** `dependent.dc_paid` asks for expenses "for this person's care" and excludes "food, lodging", so a filer
  can leave out household services or a housekeeper's meals and lodging (understating line 2(d) and the credit) or
  count volunteer work as work. Not reproduced on a return; source and question inspection.
- **Disposition:** wording debt on the same input as BUG-0284; a later dependent/f2441 pass. The completeness ruling
  `unruled:dependent#1` names this placeholder, so `check_completeness.py` fails until the id is filed.
- **Tags:** source-definition-debt; dependent; explicitly-deferred

## BUG-0339 — Residual support-definition details in the support question (open)

- **Caught by:** dependent completeness review (Claude), claim dependent#2, on the F1 branch, 2026-11-03.
- **Source:** p501 p. 20 (one social security check to both spouses; need-based payments not used for support; fair
  rental value includes furniture, appliances, heat and utilities); p501 p. 21 (dividing fair rental value when you
  provide part of the lodging); p501 p. 22 (alimony and separate maintenance are not support of a dependent).
- **Symptom:** after the F1 rewording (BUG-0333) `dependent.supported` still omits these five rules; a filer can
  misallocate support in these cases. Source and question inspection only.
- **Disposition:** residual of BUG-0282; a later dependent pass. Named by completeness ruling `unruled:dependent#2`.
- **Tags:** source-definition-debt; dependent; explicitly-deferred

## BUG-0340 — spec 6.3 claimed every atom is monotone or antitone in each argument, as tabulated; there was no table, and the claim is false

- **Caught by:** T-100 premise check (the README fact check, 2026-10-31, raised the row).
- **Source:** spec/spec.md section 6.3: "Each atom is monotone or antitone in each argument, as tabulated."
  This is a project claim. No IRS text is involved.
- **Symptom:** no table existed. For the evaluator's definitions, four atom arguments are neither monotone
  nor antitone:
  - `percent_floor` in `cap`: part 4005, whole 1000 gives 401 at cap 400 and 400 at cap 401; part 2,
    whole 1 gives 1 at cap 0 and 2 at cap 1.
  - `prorate` in `places`: $10 × 2/3 is $10.00 at 0 places and $7.00 at 1; $10 × 1/3 is $0.00 at 0 places
    and $3.00 at 1.
  - `multiply_rate` with a unit, and `round` half-up, in `unit`: 150 cents gives 200 at unit 100, 150 at
    unit 150 and 200 at unit 200.
  - `table_lookup` in `key` over the earned income credit tables, whose entries rise and then fall.

  Missing lemmas: the whole (`prorate`, `percent_floor`), the rate's denominator (`multiply_rate`) and any
  `table_lookup` property. No computed value is affected: cap, places and unit are data constants, and the
  EIC shape is the law's.
- **Fix:**
  - `Lemmas.lean` proves the antitone lemmas, the `tableBand` lemmas and `decide` counterexamples for each
    "neither".
  - `Atoms.lean` defines `tableBand`, and `Eval.lean`'s `bandTax` now runs through it.
  - Spec 6.3 replaces the sentence with a table of atom, argument, direction, condition and lemma.
- **Fix lines:** none (no form lines); files `lean/TaxFormalization/{Atoms,Eval,Lemmas}.lean`, `spec/spec.md` 6.3.
- **Siblings checked:** every atom in the spec 4 vocabulary (`engine/src/atoms.ts`), including
  `bracket_schedule`, which neither evaluator implements and no line uses. Also README lines 281–282 and
  docs/TRUST.md lines 67–71, which are stale and outside this package; replacement text is in REPORT.md.
- **Regression predictions:** no value changes. The TS/Lean comparison should show 0 differing cases and
  the fixtures should all pass. Both held: 2,042 cases, 0 differing; 1,442/1,442 fixtures.
- **Validation:** `lake build` with no `sorry`, and `#print axioms` showing only `propext`/`Quot.sound`;
  compare; test-fixtures.
- **Tags:** claim-accuracy; spec; lean; fixed

## BUG-0341 — The register entry `amb.2025.dc_born_died_half_year` records a reading the encoding no longer uses

- **Caught by:** T-095 premise check, 2026-11-03. Each unlinked register entry was compared with the lines it names.
- **Source:** p503 p. 3, Birth or death of otherwise qualifying person: "a person who was born or died in 2025 is treated as having lived with you for more than half of 2025 if your home was the person's home more than half the time they were alive in 2025".
- **Symptom:** the entry's `chosen` says "The second, as encoded (no question is added); it can only leave out a qualifying person". That second reading is "The dependent tests' answer stands, so such a person may not be counted". But since BUG-0157, `dependent.dc_disabled_qp` reads `dependent.dc_lived_half`. That line counts a person other than a qualifying child who was born or died in 2025, through `dependent.born_died` and `dependent.part_year_home`. This is the first reading, and the line cites p503 p. 3. The register therefore misstates the reading applied (spec 3, requirement 7). No values sheet shows the entry, because no line links it.
- **Resolution:** not made, because this package may not change a recorded choice or an owner verdict. Proposed: the owner retires the entry as superseded by BUG-0157 (the source rule is now encoded, so no ambiguity remains), or restates `chosen` as the first reading and links it from `dependent.dc_lived_half`.
- **Resolution lines:** `ambiguities/2025.yaml` (`amb.2025.dc_born_died_half_year`); optionally `dependent.dc_lived_half`.
- **Related entries checked:**
  - The 11 other unlinked entries, each against its named lines. This was checked at the level of label, op and `places`, not by evaluating the lines; on that check their `chosen` text matches the encoding: `eic.line1_in_table`, `dependent.eic_ssn`, `scveh.screen`, `scveh.unrecovered`, `mq.q4` and `mq.total`, `scveh.bus_cost` (places 6), `person.sep_s5`, the `sc.f7206_line7`/`_line9` pair with their `_pos` helpers, and `sc.qbi_se`/`qbi_plan`/`qbi_ded`.
  - `dependent.hoh_lived_half` (the head of household twin; BUG-0153), which has no register entry.
- **Regression predictions:** none; no value changes. `stage15.f2441.parent_died_part_year` (BUG-0157's regression) already exercises the first reading.
- **Validation:** source and YAML inspection (`forms/2025/dependent.yaml:388-418`, `:1492-1509`; BUG_INVENTORY BUG-0157).
- **Tags:** register-drift; documentation; owner-decision-needed

## BUG-0342 — Form 2441 lines 18 to 20 left all of line 1e out of earned income, though only line 12 benefits are excluded (T-121)

- **Caught by:** hard1 f2441 L3 (T-092 split, 2026-10-31), T-121; premise checked in the person-dep pass.
- **Source:** i2441 p. 5, Line 18, "however, for purposes of lines 18 and 19, earned income doesn’t include any dependent care benefits shown on line 12"; p. 5, Line 13, "Enter on line 13 the amount you carried forward and used in 2025 during the grace period"; p. 5, Line 15, "Add the amounts on lines 12 and 13 and subtract from that total the amount on line 14"; p. 4, Lines 4 and 5, earned income includes "The amount shown on Form 1040, 1040-SR, or 1040-NR, line 1z".
- **Symptom:** `person.dc_earned_b` (lines 18 and 19) is W-2 box 1 plus self-employment earnings, without any of line 1e. Line 1e (line 26) is the taxable part of line 15, which pools line 12 and the line 13 grace-period carryover; the part that comes from line 13 is not "shown on line 12", so the instructions do not exclude it. The instructions give no rule for splitting line 26 between line 12 and line 13, and line 26 depends on line 18 through lines 20 and 25, so the line 18 the instructions intend is not determined. Witness (evaluated before the fix): head of household, wages $3,000, box 10 $4,000, line 13 $500, expenses $4,500: line 18 $3,000, line 25 $3,000, line 26 and Form 1040 line 1e $1,500, completed. Up to $500 of line 26 can be line 13's, which would raise line 18 and line 25 and lower line 26.
- **Fix:** new gate `f2441.line13_earned` (line 13 above zero, line 20 less than both line 17 and line 21, and line 23 more than line 20, which is line 26 above zero); `f2441.line25` refuses on it, and line 26, line 28 and Form 1040 line 1e follow. Only this case can change an amount: with line 20 equal to line 17, or not less than line 21, more earned income cannot change line 25. The gate reads only lines upstream of line 25, so it adds no cycle. The `person.dc_earned_b` label names the reading and the refusal.
- **Fix lines:** `f2441.line13_earned`, `f2441.line25`, `person.dc_earned_b` (label)
- **Siblings checked:** `f2441.line18`, `f2441.line19`, `f2441.spouse_earned_b`, `f2441.line13`, `person.dc_earned`, `person.dc_1e`, `f2441.attrib_gate` (lines 4 and 5 keep line 1e, as i2441 p. 4 directs). Generated at integration (the packages were integrated together) and covered by this round's reruns and adjudication of their forms' reviews: `f2441.line25`.
- **Regression predictions:** written from i2441 p. 5 before the evaluator was run, all met. `f2.t121.line13_earned_refused` (the witness): lines 15 and 17 $4,500, line 18 and line 20 $3,000, line 21 $5,000, line 23 $4,500, gate true, line 25 and line 26 refused. `f2.t121.line13_earned_not_limiting` (wages $45,000, box 10 $5,000, line 13 $500, expenses $6,000): line 17 $5,500, line 20 $5,500, gate false, line 25 $5,000, line 26 and line 1e $500, line 1z $45,500, line 28 $5,000, line 29 $0. `f2.t121.line13_line21_binds` (wages $5,200): line 18 $5,200 below line 17 $5,500 but line 20 not below line 21 $5,000, gate false, line 25 $5,000, line 26 $500.
- **Validation:** fixtures in `fixtures/2025/stage8.json`; witness evaluated before and after. Accepted over-refusal: when line 19 (the spouse) is the limiting line and the line 13 carryover is the taxpayer's, more earned income for line 18 cannot change line 20, but the case is still refused. A second family reading (GPT-6 Astra) was not run; the prompt is in `receipts/t121_astra.prompt.txt`.
- **Tags:** amount-affecting; source-silent; refusal-added; existing-form-pass; fixed

## BUG-0343 — The line 16 questions did not tell the filer to leave out the value of employer-furnished care (T-123)

- **Caught by:** hard1 f2441 L2 (T-092 split, 2026-10-31), T-123.
- **Source:** i2441 p. 5, Line 16, "Enter the total of all qualified expenses incurred in 2025 for the care of your qualifying person(s)"; p. 3, Columns (a) and (b), "If you were covered by your employer's dependent care plan and your employer furnished the care (either at your workplace or by hiring a care provider), enter your employer's name in column (a)"; BUG-0262 (the archived sources do not say whether that value is a qualified expense incurred).
- **Symptom:** with employer-furnished care, `f2441.employer_care_l16` refuses when line 16 is less than line 15, and otherwise line 16 holds the expenses without the value of the employer's care. With line 16 at least line 15 that reading cannot change an amount (line 17 is line 15 under either reading). But nothing told the filer to leave the value out of `f2441.paid_2026` or `dependent.dc_paid`; a filer who entered it could lift line 16 to line 15, escape the refusal and have benefits excluded under the other reading. `dependent.dc_paid` also said "paid by your employer to the provider", which overlaps care the employer furnishes by hiring a provider.
- **Fix:** `f2441.paid_2026` and `dependent.dc_paid` say not to include the value of care your employer furnished itself (at your workplace or through a care provider it hired); `dependent.dc_paid` now says "paid by your employer to a provider you chose", the wording `f2441.employer_care` uses. Proposed register entry (the integrator owns `ambiguities/2025.yaml`): `amb.2025.dc_employer_care_value`, text at issue i2441 p. 5 Line 16 and p. 3 Columns (a) and (b); readings (1) the value of employer-furnished care is not an expense incurred for line 16, (2) it is; chosen (1) when line 16 is at least line 15 (no amount differs) and refused otherwise (`f2441.employer_care_l16`, BUG-0262); link it from `f2441.line16` and `f2441.paid_2026`.
- **Fix lines:** `f2441.paid_2026`, `dependent.dc_paid`
- **Siblings checked:** `f2441.employer_care`, `f2441.employer_care_gate` (line 30 refusal), `f2441.employer_care_l16`, `f2441.line16`, `f2441.line17`, `dcprov.paid`. Generated at integration (the packages were integrated together) and covered by this round's reruns and adjudication of their forms' reviews: `dependent.dc_line2d`.
- **Regression predictions:** wording only; no value changes. Existing `stage21.t073.employer_care_nothing_paid_refused` and `stage21.t073.employer_care_paid_equals_benefits` still pass (run).
- **Validation:** source and question inspection.
- **Tags:** source-silent; wording; existing-form-pass; fixed (ambiguity entry pending integrator)

## BUG-0344 — `person.ira_excess` omitted "including extensions" from the withdrawal deadline (T-119)

- **Caught by:** fixr4 person L1 (T-092 split), T-119.
- **Source:** p590a p. 35, Tax on Excess Contributions, "In general, if the excess contributions for a year aren’t withdrawn by the date your return for the year is due (including extensions), you are subject to a 6% tax".
- **Symptom:** the screen asked whether the excess "was not withdrawn with its earnings by the due date of your return"; a filer on extension who withdrew in June 2026 could answer Yes and be refused.
- **Fix:** "(including extensions)" added; the p. 35 sentence added to the locator.
- **Fix lines:** `person.ira_excess`
- **Siblings checked:** `person.ira_excess_gate` (already cites the extension rule), `person.x_other`, `ira.special`, `f8889.line14b` (printed form label, not changed).
- **Regression predictions:** wording only; no value changes.
- **Validation:** source inspection; strict citation check passes.
- **Tags:** wording; over-refusal; fixed

## BUG-0345 — `person.itin_applied`'s label lacked the renewal and its help said it counts for the credit for other dependents only (T-120)

- **Caught by:** fixr4 person L2 (T-092 split), T-120.
- **Source:** i1040gi p. 19, Step 5, question 1, "(Answer 'Yes' if you are applying for an ITIN on or before the return due date (including extensions).)"; p970 p. 11, "If an ATIN or ITIN is applied for on or before the due date of a 2025 return (including extensions) and the IRS issues an ATIN or ITIN as a result of the application, the IRS will consider the ATIN or ITIN as issued on or before the due date of the return."
- **Symptom:** the question asks about an application or a renewal, but the label said only "applied for an ITIN"; the interview help said the answer "counts for the credit for other dependents only", though `person.edu_student` reads it for the American opportunity credit (and the T-113 gate refuses the lifetime learning credit on it).
- **Fix:** the label names the renewal; the help says the answer counts for the credit for other dependents (not the child tax credit, `amb.2025.ctc_spouse_itin_application`) and for this person as an American opportunity credit student, and that the lifetime learning credit is refused.
- **Fix lines:** `person.itin_applied` (label), `interview/questions-2025.yaml` (help)
- **Siblings checked:** `household.tin_count`, `household.id_count`, `person.edu_student`, `person.edu_llc_tin_refused`, `person.tin`.
- **Regression predictions:** wording only.
- **Validation:** inspection.
- **Tags:** wording; presentation; fixed

## BUG-0346 — Church employee income glossed without qualified church-controlled organizations (T-127)

- **Caught by:** screens group4 BUG-0345-11 (T-092 split), T-127.
- **Source:** i1040sse p. 1, Employees of Churches and Church Organizations, "Church employee income is wages you received as an employee (other than as a minister, member of a religious order, or Christian Science practitioner) of a church or qualified church-controlled organization that has a certificate in effect electing an exemption from employer social security and Medicare taxes."
- **Symptom:** `scope.schedule1` and `person.se_screen` said "wages from a church that elected exemption"; an employee of an electing church school or hospital could answer No and complete a return that should be refused.
- **Fix:** both say "a church or qualified church-controlled organization"; the i1040sse sentence is added to both locators.
- **Fix lines:** `scope.schedule1` (label and question), `person.se_screen`
- **Siblings checked:** `f8959.unsupported`/its screen (says "any church employee income", no gloss), `eic.clergy`, se (yaml file) lines 4c and 5a (notes only), person (yaml file) Worksheet B note. Generated at integration (the packages were integrated together) and covered by this round's reruns and adjudication of their forms' reviews: `eic.step2_other`, `eic.step5_line1`, `f1040.line10`, `f1040.line8`, `person.se_screened`, `s1a.line14b_calc`, `s1a.line5_calc`, `s8812.eiw_3`, `s8812.eiw_4`, `scope.ready`, `ssb.line6`.
- **Regression predictions:** wording only; no value changes.
- **Validation:** inspection; the `scope.schedule1` screen review is stale and must be rerun (`check_screens.py`).
- **Tags:** wording; under-refusal; fixed

## BUG-0347 — BUG-0320 is fixed: `person.blind` states the partial-blindness test and the certified statement (T-177)

- **Caught by:** BUG-0320, recorded open; this entry closes it because the inventory is append-only. Owner decision 2026-11-02: wording.
- **Source:** i1040gi p. 33, Blindness, "If you weren’t totally blind as of December 31, 2025, you must get a statement certified by your eye doctor (ophthalmologist or optometrist) that:", "You can't see better than 20/200 in your better eye with glasses or contact lenses, or", "Your field of vision is 20 degrees or less.", the not-likely-to-improve alternative and "You must keep the statement for your records."; p. 33, Line 12d, "were blind at the end of 2025".
- **Symptom:** as recorded in BUG-0320.
- **Fix:** the label and question ask whether you were blind at the end of 2025, totally or with the certified statement, and say to keep it; the cite moves from the generic Schedule A locator to i1040gi p. 33.
- **Fix lines:** `person.blind`
- **Siblings checked:** `sa.boxes_blind`, `sa.extra_blind`, `sa.spouse_extra` (refused), `refund.you_blind` (2024 worksheet question, form the refund form, not owned: it asks "Were you blind at the end of 2024?" without the definition; recorded, not changed).
- **Regression predictions:** wording only.
- **Validation:** inspection. `check_consumers.py` now reports `person.blind@i1040gi:p34` and `p35` (read by `sa.boxes_blind`) as changed and `p33` as stale: proposed verdicts in `consumers_proposed.json`.
- **Tags:** source-definition-debt; standard-deduction; wording; fixed
- **Review correction (backlog round, before commit):** the person adjudication found that the reworded question left out p501 p. 23's contact-lens rule (vision correctable beyond the limits only by contact lenses worn briefly because of pain, infection or ulcers qualifies); the question now says to answer yes in that case, citing p501 p. 23.

## BUG-0348 — BUG-0338 is fixed: the care-expense question states household services, housekeeper meals and lodging, provider transportation, agency fees and the volunteer-work rule (T-184)

- **Caught by:** BUG-0338, recorded open; this entry closes it because the inventory is append-only.
- **Source:** i2441 p. 1, "These include amounts paid for household services and care of the qualifying person while you worked or looked for work."; p. 2, Household services, the cook/maid/babysitter/housekeeper/cleaning person sentence and "they don't include the services of a chauffeur, bartender, or gardener"; p503 p. 6, Volunteer work; p503 p. 7, Transportation and Fees and deposits; p503 p. 8, Meals and lodging provided for housekeeper.
- **Symptom:** as recorded in BUG-0338.
- **Fix:** `dependent.dc_paid` states the household-services rule with its examples and exclusions, the housekeeper's meals and extra lodging (excepted from the food-and-lodging exclusion), the care provider's transportation (not other transportation or the provider's travel to your home), agency fees, deposits and application fees (not a forfeited deposit), and that unpaid volunteer work or work for a nominal salary is not work.
- **Fix lines:** `dependent.dc_paid`
- **Siblings checked:** `dependent.dc_line2d`, `f2441.paid_2026`, `f2441.line16`, `dcprov.paid`, `dcprov.household`; the limits baseline entries for `dependent.dc_paid` (`limit:p503:p6:463a57ef`, `limit:p503:p6:ea477d7e`) still hold (check_limits (py file) 0 new).
- **Regression predictions:** wording only; no value changes.
- **Validation:** inspection; strict citation check passes.
- **Tags:** source-definition-debt; dependent; wording; fixed

## BUG-0349 — BUG-0339 is fixed: the support question states the five residual rules (T-185)

- **Caught by:** BUG-0339, recorded open; this entry closes it because the inventory is append-only.
- **Source:** p501 p. 20, Lodging, "Fair rental value includes a reasonable allowance for the use of furniture and appliances, and for heat and other utilities that are provided."; p. 21, "If you don’t provide the total lodging, the total fair rental value must be divided depending on how much of the total lodging you provide."; p. 20, "However, payments based on the needs of the recipient won’t be considered as used entirely for that person’s support if it is shown that part of the payments weren’t used for that purpose."; p. 20, Social security benefits, the one-check sentence; p. 22, Alimony, "Payments to a spouse that are alimony or separate maintenance payments, or similar payments from an estate or trust, aren’t treated as a payment for the support of a dependent."
- **Symptom:** as recorded in BUG-0339.
- **Fix:** `dependent.supported` states all five rules.
- **Fix lines:** `dependent.supported`
- **Siblings checked:** `dependent.self_support` (the qualifying-child test; it already counts the person's own home and state support; the one-check and alimony rules bear on the qualifying-relative support split, so it is unchanged), `dependent.multiple_support`, `dependent.divorced_rule`. Generated at integration (the packages were integrated together) and covered by this round's reruns and adjudication of their forms' reviews: `dependent.qualifying_relative`.
- **Regression predictions:** wording only.
- **Validation:** inspection; strict citation check passes.
- **Tags:** source-definition-debt; dependent; wording; fixed

## BUG-0350 — An earlier credit disallowance refuses the whole return when no credit is claimed (T-101, `household.credit_disallowed`) — fix proposed as a patch, not applied

- **Caught by:** T-101 (coverage tree build, 2026-10-31); premise checked in the person-dep pass.
- **Source:** i1040s8812 p. 2, "you must attach Form 8862 to your tax return to claim the CTC, ACTC, or ODC unless an exception applies"; i1040gi p. 43, "You must file Form 8862 if your EIC for a year after 1996 was reduced or disallowed for any reason other than a math or clerical error".
- **Symptom:** `s8812.line12` and the EIC credit line refuse on `household.credit_disallowed` alone. Witness (evaluated): `stage5.return.owed` (single, no dependents, EIC Steps not passed) with the answer Yes refuses Form 1040 lines 19, 24, 27a and 37; with the gate narrowed it completes with line 24 $18,500, line 27a $0, line 37 $1,500, the values it records with the answer No.
- **Fix (proposed):** gates `household.ctc_disallowed_claim` (the answer Yes and Schedule 8812 line 8 more than line 11, that is line 12 above zero, read without line 12 to avoid a cycle) and `household.eic_disallowed_claim` (the answer Yes and `eic.eligible`), used by the existing refusals in `s8812.yaml` and `eic.yaml`. The refusal sites are in forms this package does not own, so the change is `t101_credit_disallowed.patch` (household, s8812, eic, `tools/coverage/tree.json`, two audit fixtures and one new regression); apply after `coverage_tree_line13.patch`.
- **Fix lines:** `household.ctc_disallowed_claim`, `household.eic_disallowed_claim`, `s8812.line12`, `eic.credit` (proposed)
- **Siblings checked:** `household.credit_disallowed` (input, unchanged), `f8863.ban_refused` (the education-credit ban, a separate input), `s8812.line8`, `s8812.line11`, `eic.eligible`.
- **Regression predictions:** `f2.t101.credit_disallowed_no_credit_claimed` completes with stage5.return.owed's 45 values; `audit.s8812.credit_disallowed` keeps its Schedule 8812 refusals under the new gate id and its line 27a becomes $0 (EIC not eligible there); `audit.eic.credit_disallowed` keeps its refusals under the new ids. Tested in a scratch copy of this worktree with the patch applied: 1,443/1,445 before the two audit fixtures were updated (only those two, gate ids and the line 27a narrowing), all three pass after.
- **Validation:** scratch-copy evaluation; `tree.py --check` accepts the placements (only the generated outputs are then out of date). Not run with the patch: the other per-check scripts.
- **Accepted over-refusal that remains:** the question pools the EIC and the child tax credits, so a filer whose only disallowance was the EIC is still refused on Schedule 8812 when claiming the child tax credit (and the reverse).
- **Tags:** over-refusal; whole-return-screen; T-101; proposed
- **Review correction (backlog round, before commit):** the eic adjudication found `household.eic_disallowed_claim` still refused a return whose Worksheet A line 6 is $0 (witness `classm.ssb.4`: EIC $0, Form 1040 line 34 $920, yet lines 27a to 37 refused). The gate now also requires `eic.line6` above zero; regression `f2.t101.credit_disallowed_eic_zero`, predicted from i1040gi p. 43 before evaluation (same values as the No answer), passes. Residual accepted over-refusal (low): the child tax credit gate refuses when line 12 is positive although lines 14 and 27 come to $0; tightening it on lines 14 or 27 would read lines downstream of the refused line 12.

## BUG-0351 — Alimony screen omits the part of payments that must continue after the recipient's death

- **Caught by:** T-124 (T-092 split; screens group4 BUG-0354-8).
- **Source:** p504 p. 15, Liability for payments after death of recipient spouse, "If any part of payments you make must
  continue to be made for any period after your spouse’s death, that part of your payments isn’t alimony" and "If you
  must make any payments in cash or property after your spouse’s death as a substitute for continuing otherwise
  qualifying payments before the death, the otherwise qualifying payments aren’t alimony".
- **Symptom:** `s1.alimony_unsupported` listed child support and payments for a home as non-alimony parts, but not a
  part that must continue after the recipient's death (or that a post-death payment substitutes for). A filer with such
  a part answered No and entered the whole payment, so Schedule 1 line 2a (or 19a) included an amount that isn't
  alimony. Source and question inspection; not reproduced on a return.
- **Fix:** the screen adds payments of which any part must continue, in cash or property, after the recipient spouse's
  death (even if the instrument does not say so, for example under state law), and payments for which a payment due
  after the death is a substitute. Wording of an existing screen whose Yes already refuses at `s1.alimony_refused` and
  `s1.paid_refused`; the refusal texts are unchanged.
- **Fix lines:** `s1.alimony_unsupported`
- **Siblings checked:** `s1.alimony_refused`, `s1.paid_refused`, `s1.alimony_received`, `s1.alimony_paid`,
  `s1.line2a`, `s1.line19a`, `s1.line19b_notice`.
- **Regression predictions:** no evaluated value changes; no fixture added (the new item is a new item of a screen whose
  Yes already refuses; stage16 alimony refusal fixtures cover the refusal).
- **Validation:** source inspection; fixtures 1,442 of 1,447 (the 5 failures are the T-131 class M cases, BUG-0355).
- **Tags:** source-definition-debt; wording; existing-form-pass; fixed

## BUG-0352 — Unemployment screen's "employer-paid tax" carve-out could exclude a self-employed filer's own payments

- **Caught by:** T-125 (T-092 split; screens group4 BUG-0354-9, introduced by the BUG-0245 rewording).
- **Source:** i1040gi p. 89, Line 7, "If you made contributions to a governmental unemployment compensation program and
  you aren't itemizing deductions, reduce the amount you report on line 7 by those contributions."
- **Symptom:** `s1.uc_unsupported` said "not counting employer-paid tax"; a self-employed filer who paid for elective
  state coverage could read their own payment as employer-paid and answer No, so line 7 was computed unreduced instead
  of refused. Question inspection; not reproduced.
- **Fix:** the question counts "payments you made yourself, such as for coverage you elected as a self-employed person"
  and excludes only "tax an employer paid on your wages". Wording only; the refusal is unchanged.
- **Fix lines:** `s1.uc_unsupported`
- **Siblings checked:** `s1.line7_figured`, `s1.has_uc`, `s1.uc_paid`, `s1.uc_repaid`.
- **Regression predictions:** none (wording only).
- **Validation:** source inspection.
- **Tags:** wording; existing-form-pass; fixed

## BUG-0353 — Alimony questions name only one form of a post-2018 change that applies the new rules

- **Caught by:** T-126 (T-092 split; fixr3 s1 Low).
- **Source:** p504 p. 16, Certain Rules for Instruments Executed or Modified After 2018, "if the modification expressly
  states that the alimony isn’t deductible to the payer or includible in the income of the recipient", and Example 2, "the
  modification expressly provided that the post-2018 alimony rules apply"; i1040gi p. 89, Line 2a.
- **Symptom:** `s1.alimony`, `s1.alimony_received` and `s1.alimony_paid` described a change "that expressly provides that
  alimony received isn't included in income"; a change that only adopts the post-2018 rules, or only denies the payer's
  deduction, could be answered as not changed, and its later payments counted as income or deducted. Question inspection.
- **Fix:** the three questions name a change after 2018 that expressly applies the post-2018 rules: one stating that the
  post-2018 alimony rules apply, or that alimony isn't deductible by the payer or isn't included in the recipient's
  income. Locators add the p504 p. 16 quotations. Wording only.
- **Fix lines:** `s1.alimony`, `s1.alimony_received`, `s1.alimony_paid`
- **Siblings checked:** `s1.alimony_unsupported`, `s1.line2a`, `s1.line19a`, the register entry for the alimony screen (its "chosen". Generated at integration (the packages were integrated together) and covered by this round's reruns and adjudication of their forms' reviews: `s1.alimony_refused`, `s1.paid_refused`.
  text says "a change that expressly excludes them"; proposed wording follow-up for the register's owner, not edited).
- **Regression predictions:** none (wording only).
- **Validation:** source inspection; `citations.py --strict` 0 findings.
- **Tags:** wording; existing-form-pass; fixed

## BUG-0354 — Retirement screen over-refused survivors of retirees and full in-kind rollovers of property

- **Caught by:** T-128 and T-129 (T-092 split; fixr2 retirement F1 and F2).
- **Source:** i1040gi p. 30, Age (or Combined Ages) at Annuity Starting Date, "If you are the survivor of a retiree, use
  the retiree’s age on their annuity starting date" and "If you are the beneficiary of an employee who died, see Pub.
  575"; p. 30, Rollovers, "special rules that apply to ... partial rollovers of property"; p575 p. 34, Survivors of
  retirees, "If the retiree was reporting the annuity under the Simplified Method, the part of each payment that is tax
  free is the same as the tax-free amount figured by the retiree at the annuity starting date", and "If you receive
  guaranteed payments as the decedent’s beneficiary under a life annuity contract"; p575 p. 23, Rollovers of property, "you
  must either roll over the actual property distributed or sell it and roll over the proceeds" and "If you roll over only
  part of the proceeds, you are taxed on the part you keep"; p575 p. 12, Exclusion limited to cost.
- **Symptom:** `retirement.special` refused "an annuity you receive as the beneficiary of an employee who died", which a
  survivor under a retiree's joint and survivor annuity answers Yes, though i1040gi computes it on the worksheet with
  the retiree's age; and "a rollover of property other than cash", which refuses a rollover of all of the same property,
  computed by the ordinary line 5a/5b subtraction. Over-refusals; no wrong amount.
- **Fix:** `retirement.special` now refuses the beneficiary of an employee who died before retiring, guaranteed payments
  as a retiree's beneficiary under a life annuity contract, and an annuity shared among more than one beneficiary, and
  says a survivor annuity under a retiree's joint and survivor annuity is not one of these; and refuses a property
  rollover only when the property was sold and the proceeds rolled over, or only part of the property was rolled over.
  The worksheet questions tell a survivor of a retiree to answer for the retiree's annuity: `retirement.annuity`
  (starting date and the retiree's age), `retirement.cost` (the retiree's cost), `retirement.used_last_year` and
  `retirement.last_line4` (the retiree's worksheet), `retirement.joint_life` and `retirement.combined_age` (the retiree's
  and the survivor's lives and ages), `retirement.recovered` (including the retiree's recovery). No expression changed.
  Pub. 575 (2025) is archived as `sources/2025/p575` for these citations.
- **Fix lines:** `retirement.special`, `retirement.annuity`, `retirement.cost`, `retirement.used_last_year`,
  `retirement.last_line4`, `retirement.joint_life`, `retirement.combined_age`, `retirement.recovered`
- **Siblings checked:** `retirement.rolled`, `retirement.taxable`, `retirement.amount_a`, `retirement.age` (already. Generated at integration (the packages were integrated together) and covered by this round's reruns and adjudication of their forms' reviews: `retirement.annuity_rollover`, `retirement.annuity_with_cost`, `retirement.plan_taxable`, `retirement.show_a`, `retirement.smw2`, `retirement.smw4`.
  stated the survivor's age rule), `retirement.annuity_rollover` (still refuses any rollover of a Simplified Method
  annuity), `retirement.rollover`, `retirement.smw4` to `smw11`, `retirement.plan_taxable`, `retirement.show_a`.
- **Regression predictions:** written from the sources before the evaluator ran; both matched.
  `stage10.smw.survivor_of_retiree`: retiree's annuity from January 1, 2018, joint lives at 65 and 65, cost $31,000, last
  year's line 4 $100, $8,400 recovered by the retiree; survivor receives $600 a month for 12 months (code 4). Lines 4
  $100, 5 $1,200, 10 $9,600, 11 $21,400; Form 1040 line 5a $7,200, line 5b $6,000.
  `stage10.plan.property_rollover_full`: $20,000 of nonemployer stock, code 7, all of it rolled over in kind. Line 5a
  $20,000, line 5b $0, line 5c box 1 checked, line 4c unchecked. An independent GPT-6 Astra reading of both predictions
  agreed (`research/audits/income/receipts/astra_t128_t129.*`).
- **Validation:** fixtures (both new cases pass); `citations.py --strict` 0 findings; consumer and limit verdicts proposed
  (`consumers_proposed.json`).
- **Tags:** over-refusal; wording; existing-form-pass; fixed
- **Review correction (backlog round, before commit):** the retirement adjudication found the narrowed screen no longer refused a survivor whose retiree's annuity started before November 19, 1996 (the item did not say to answer for the retiree's starting date, while the worksheet questions now do); the item now says so (i1040gi p. 30). It also names keeping the property and rolling over cash or other property instead (p575 p. 23).

## BUG-0355 — `sales.wash_loss` accepted a code W amount larger than the loss

- **Caught by:** T-131 (T-092 split; fixr2 sales O1; class M classm.s3.2, where $449 was added to a gain). Owner's
  decision 2026-11-01: refuse as an entry error.
- **Source:** i8949 p. 10, code W, "You have a nondeductible loss from a wash sale" and "enter the amount of the
  nondeductible loss as a positive number in column (g)"; p550 p. 86, Wash Sales, "A wash sale occurs when you sell or
  trade stock or securities at a loss".
- **Symptom:** with code W, column (g) took the entered wash-sale loss whatever the loss on the sale, so an amount larger
  than the loss (or any amount on a gain) raised column (h) above zero, adding a gain. Not re-run on the old tree: by
  the arithmetic of `sales.h`, proceeds $1,000, basis $1,200 and wash $449 give column (h) +$249; the class M case
  classm.s3.2 recorded the gain form of it (a $449 wash amount on a sale at a gain).
- **Fix:** new helper `sales.wash_over` (columns (d) less (e), plus the code B correction, plus the entered wash-sale
  loss) and gate `sales.wash_bad` (code W, wash-sale loss above zero and `sales.wash_over` above zero), refusing at
  `sales.w` as an entry error; `sales.wash_loss` states the limit. The gate is placed in `tools/coverage/tree.json`
  (sales, entry). `engine/src/generate.ts` keeps a valid generated sale's wash-sale loss within the loss (invalid entries
  keep the raw amount, so the gate is exercised); this consumes no extra randomness.
- **Fix lines:** `sales.wash_loss`, `sales.wash_over`, `sales.wash_bad`, `sales.w`
- **Siblings checked:** `sales.has_w`, `sales.b`, `sales.e`, `sales.g`, `sales.h`, `sales.bad_code` (box C/F code B),. Generated at integration (the packages were integrated together) and covered by this round's reruns and adjudication of their forms' reviews: `sales.w`, `sales.wash_bad`, `sales.wash_over`.
  `sales.bad_aggregate` (aggregate route has no codes), `tools/engines/generate_cases.py` (already draws wash within the
  loss), `engine/src/generate.ts`.
- **Regression predictions:** written before the evaluator ran; all three matched. `sales.refuse.wash_over_loss`
  (proceeds $1,000, basis $1,200, wash $449) refuses at `sales[a].w` and Form 1040 line 7a with gate
  `sales[a].wash_bad`; `sales.adjust.A.W.equal_loss` (wash $200 equal to the loss) gives column (g) $200, column (h) $0,
  line 7a $0; `sales.adjust.D.BW.wash_within_corrected_loss` (box D, BW, proceeds $6,000, reported basis $7,000, correct
  basis $8,000, wash $1,500) gives column (g) $500, column (h) -$500, line 7a -$500 (the B correction counts toward the
  loss).
- **Regressions introduced (open until the class M reruns):** five recorded class M cases carry generated wash-sale
  amounts larger than the loss and now refuse: `classm.s3.2`, `classm.s3.2.deepseek`, `classm.qdcg.3`, `classm.tcw.14`,
  `classm.sa.2`. They need class M reruns of s3 (Claude and DeepSeek), qdcg, tcw and sa, which rebuild jobs from the
  corrected generator; sales class M is stale anyway.
- **Validation:** fixtures 1,442/1,447 (the five above); refusal reach 0 exceptions; coverage tree 196 gates placed;
  integration 806 passed.
- **Tags:** amount-affecting; entry-error gate; existing-form-pass; fixed (class M reruns pending)

## BUG-0356 — `sales.special` did not name collectibles held through an entity

- **Caught by:** T-130 (T-092 split; screens group4 BUG-0354-10).
- **Source:** i1040sd p. 11, line 18, "Include on the worksheet any gain (but not loss) from the sale or exchange of an
  interest in a partnership, S corporation, or trust held for more than 1 year and attributable to unrealized appreciation
  of collectibles"; p. 12, line 19, "You reported a long-term capital gain from the sale or exchange of an interest in a
  partnership that owned section 1250 property".
- **Symptom:** "an interest in a partnership, S corporation or trust holding such property" could be read as section
  1250 property only, so stock of an S corporation holding appreciated collectibles was answered No and its 28% gain
  taxed at 15 or 20%. Question inspection.
- **Fix:** the question names "an interest in a partnership, S corporation or trust (including S corporation stock) that
  holds collectibles or section 1250 property, such as stock of an S corporation that owns art or gold worth more than its
  cost"; the locator adds the p. 12 quotation. Wording only.
- **Fix lines:** `sales.special`
- **Siblings checked:** `sales.one` (refuses on Yes), `sales.aggregate_eligible` ("no collectibles"), `g28.line1` and `g28.line4`,
  `sd.other_forms` (K-1 capital gains already refused).
- **Regression predictions:** none (wording; `sales.refuse.special` covers the refusal).
- **Validation:** source inspection. The refusal remedy still says "Direct sales of collectibles, section 1202 stock and
  section 1250 property are unsupported"; left unchanged because stage3 fixtures quote it 35 times (low, for the next sales
  change).
- **Tags:** wording; existing-form-pass; fixed

## BUG-0357 — `sd.filed` cited doc f1040sd for an i1040gi quotation

- **Caught by:** T-141 (TASKS verification, from T-076 (4)).
- **Source:** i1040gi p. 31, Line 7a.
- **Symptom:** the citation named doc f1040sd with an "i1040gi p. 31" locator; the cited document was wrong.
- **Fix:** doc i1040gi, locator "p. 31, Line 7a, ..." with the same three quotations (checked on p. 31).
- **Fix lines:** `sd.filed`
- **Siblings checked:** no further check needed (citation only). Generated at integration (the packages were integrated together) and covered by this round's reruns and adjudication of their forms' reviews: `f1040.gate.qdcg_applies`, `qdcg.schedule_d_filed`.
- **Regression predictions:** none.
- **Validation:** `citations.py --strict` 0 findings.
- **Tags:** citation; fixed

## BUG-0358 — The Part II joint-occupancy question asked about "the home" only

- **Caught by:** the standing screen review, group4 finding 2 (BUG-0361-2, UNCLEAR, low); T-132.
- **Source:** i5695 p. 3, Section B—Residential Energy Property Expenditures, "installed on or in connection with a
  home that you used during 2025"; p. 3, Joint occupancy, "If you occupied your home jointly with someone, each occupant
  must complete their own Form 5695"; p. 6, Lines 21a Through 21c, "Enter the full address of each home where you
  installed qualified energy property".
- **Symptom:** `f5695.joint_occupancy` asked "Did you occupy the home jointly...". A filer who lives alone in the main
  home and has a heat pump at a second home shared with a sibling could read "the home" as the main home and answer No.
  Line 30 then took the full $2,000 heat pump limit where only the allocable share applies (credit overstated).
- **Fix:** the question and its label ask about any home for which Part II costs are entered. They say this includes
  any other home where qualified energy property is installed (a second home or a home you rent) and that sharing any
  one of them is a Yes. The cite adds the two quotes above. The wording follows `f5695.line21a`, which already says the
  home "may be a second home or a home you rent". Wording only.
- **Fix lines:** `f5695.joint_occupancy`
- **Siblings checked:** `f5695.line30`, `f5695.line32a`, `f5695.line21a`, `f5695.qmid_ac`, `f5695.qmid_enabling`,
  `f5695.qmid_furnace`, `f5695.qmid_hp`, `f5695.qmid_wh` (generated by `siblings.py`. The qmid questions share the
  p. 3 and p. 6 anchors and ask nothing about which home.)
- **Regression predictions:** no evaluated value changes. Refusal on Yes is unchanged (`f5695.line30`, gate
  `f5695.joint_occupancy`).
- **Validation:** fixtures 1,446/1,446 (see REPORT.md). The integrator reruns the f5695 screen review
  (`check_screens.py` marks `f5695.joint_occupancy` stale) and the f5695 render review.
- **Tags:** question-wording; amount-affecting; caught-by-screen-review; fixed

## BUG-0359 — Form 5695 lines 32 and 32a read the Part II screens on a return with no Part II

- **Caught by:** T-081 (3), recorded as T-145.
- **Source:** Form 5695 (2025), line 32; i5695 p. 7, Lines 32a and 32b, "Joint occupants of a home who are claiming the
  energy efficient home improvement credit must check the box on line 32a".
- **Symptom:** with `f5695.part2_any` No, the return was right, because `s3.line5b` already guarded its read of line
  32. But printed line 32 read line 30, whose refusals read `f5695.business_use`, `f5695.joint_occupancy` and the other
  Part II screens, and line 32a read `f5695.joint_occupancy` directly. Line 32b already had the guard. **Evaluated** on
  `stage15.f8880.s1` (no Part II, Part II screens unanswered): line 32 was UNKNOWN (no input for
  `f5695.business_use`) and line 32a was UNKNOWN (no input for `f5695.joint_occupancy`). Partial-input triage therefore
  counted unknowns that the form does not need.
- **Fix:** new helper `f5695.eehi_credit` (the smaller of lines 30 and 31). Line 32 becomes a choose on
  `f5695.part2_any`: Yes gives the helper, No gives zero. Line 32a tests `f5695.part2_any` and
  `f5695.joint_occupancy` together, as line 32b does.
- **Fix lines:** `f5695.line32`, `f5695.line32a`, `f5695.eehi_credit`, `f5695.zero` (locator only)
- **Siblings checked:** `f5695.line32b`, `f5695.condo`, `f5695.line30`, `s3.line5b`. Generated at integration (the packages were integrated together) and covered by this round's reruns and adjudication of their forms' reviews: `f5695.line11`, `f5695.line18b`, `f5695.line19h`, `f5695.line20d`, `f5695.line22d`, `f5695.line23d`, `f5695.line24d`, `f5695.line25e`, `f5695.line26c`, `f5695.line29h`, `f5695.line32`, `f5695.line32a`, `f5695.line5b`.
- **Regression predictions:** `stage15.f5695.no_part2` (stage15.f8880.s1 inputs) predicts `f5695.line32` $0,
  `f5695.line32a` false and `s3.line5b` $0 from the form (Part II not completed, no credit claimed, box unchecked).
  It was written before the evaluator was run and matched. No existing fixture changed value.
- **Validation:** fixtures 1,446/1,446. The integrator reruns the f5695 transcription, render and class M reviews
  (line 32's expression changed).
- **Tags:** triage-unknowns; existing-form-pass; fixed

## BUG-0360 — The Net Investment Income Tax screen did not name section 404(k) ESOP dividends

- **Caught by:** the standing screen review, group4 finding 3 (BUG-0361-3, NARROW, low); T-133.
- **Source:** i8960 p. 7, Line 2—Ordinary Dividends, "If line 2 includes dividends from employer securities held in an
  employee stock ownership plan (ESOP) that are deductible under section 404(k) ... include those amounts as negative
  modifications on line 7"; i8960 p. 13, Line 7—Other Modifications to Investment Income, "Section 404(k) dividends
  reported on line 2 (enter as a negative amount)"; i1099div p. 4, Box 1a, "Include reinvested dividends and section
  404(k) dividends paid directly from the corporation".
- **Symptom:** section 404(k) dividends paid directly to a participant are in Form 1099-DIV box 1a and so on Form 8960
  line 2. No screen named them; only the catch-all "another net investment income adjustment" covered them. A filer who
  did not know they were an adjustment answered No, and the tax was overstated by 3.8% of the dividends.
- **Fix:** `f8960.unsupported` names "section 404(k) dividends on employer securities held in an employee stock
  ownership plan (ESOP) and paid directly to you (Form 1099-DIV box 1a)". The cite adds the three quotes. Wording only:
  the existing refusal on Yes is unchanged.
- **Fix lines:** `f8960.unsupported`
- **Siblings checked:** `f8960.line1`, `f8960.line3`, `f8960.line4a`, `f8960.line4b`, `f8960.line5b`, `f8960.line5c`,. Generated at integration (the packages were integrated together) and covered by this round's reruns and adjudication of their forms' reviews: `f8960.line10`, `f8960.line13`, `f8960.line6`, `f8960.line7`, `f8960.line9c`.
  `f8960.line6`, `f8960.line7`, `f8960.line9c`, `f8960.line10`, `f8960.line13`
- **Regression predictions:** no evaluated value changes (a new item in a screen that already refuses on Yes).
- **Validation:** fixtures 1,446/1,446. `check_consumers.py` now reports `consumer:f8960.unsupported@i8960:p13` stale (the
  question cites that page itself); remove it (consumers_proposed.json). The integrator reruns the f8960 screen review.
- **Tags:** scope-screen-narrower-than-line; amount-affecting; caught-by-screen-review; fixed

## BUG-0361 — "Publicly traded securities" was undefined in the noncash gift questions

- **Caught by:** the standing screen review, group4 finding 0 on `gift.special` (BUG-0361-5, NARROW, low); T-136.
- **Source:** i8283 p. 9, Securities, "A security is generally considered to be publicly traded if the security is (a)
  listed on a recognized stock exchange whose quotations are published daily; (b) regularly traded on a national or
  regional over-the-counter market; or (c) quoted daily in a national newspaper of general circulation in the case of
  mutual fund shares", and "Nonpublicly traded securities may include, but are not limited to, privately held stock".
- **Symptom:** take a $12,000 gift of stock that has a ticker symbol but is not regularly traded. The filer could
  answer No to `gift.special` (the publicly traded exception) and Yes to `gift.public_securities`, which had no
  definition. Then `gift.section_b` was false and `gift.allowed` passed $12,000 with no Section B and no qualified
  appraisal.
- **Fix:** `gift.public_securities` states the three-part p. 9 definition. It tells the filer to answer No for
  privately held stock, LLC or partnership interests, and stock that has a ticker but is not regularly traded.
  `gift.special` restates the definition in its exception. Both cites add the p. 9 quote. Wording only.
- **Fix lines:** `gift.public_securities`, `gift.special`
- **Siblings checked:** `gift.section_b`, `gift.allowed`, `gift.deduction`
- **Regression predictions:** no evaluated value changes.
- **Validation:** fixtures 1,446/1,446. Citing i8283 p. 9 brings two items onto the checks' worklists. The first is
  the vehicle sentence there (`limit:i8283:p9:ab5bbab4`, proposed as enforced by `gift.special` in
  limits_proposed.json). The second is the baseline consumer pair `consumer:gift.public_securities@f8283:p1`, proposed
  "same" in consumers_proposed.json. The integrator reruns the gift screen review and the gift render review.
- **Tags:** source-definition-debt; amount-affecting; caught-by-screen-review; fixed
- **Review correction (backlog round, before commit):** the gift adjudication found the new wording narrower than i8283 p. 9 ("counts only if", and "a ticker symbol but is not regularly traded" would send a listed but thinly traded stock to the Section B refusal); it now says "is generally publicly traded if" and limits the No case to stock neither listed nor regularly traded over the counter. Over-refusal only; no value could change.

## BUG-0362 — The 2024 refund screen did not ask about 2024 tax paid before 2024

- **Caught by:** the standing screen review, group4 finding 0 on `refund.not_2024` (BUG-0361-7, NARROW, very low);
  T-137. A residual of BUG-0230.
- **Source:** p525 p. 24, Recovery for 2 or more years, "If you receive a refund or other recovery that is for amounts
  you paid in 2 or more separate years, you must allocate, on a pro rata basis, the recovered amount between the years in
  which you paid it" (already cited by the question).
- **Symptom:** take a 2024 estimated payment made in December 2023, which was deductible on the 2023 return. The filer
  answered No, and the worksheet treated the whole 2024 refund as a recovery of tax paid in 2024.
- **Fix:** the question and label add "or before 2024 (for example a 2024 estimated payment made in December 2023)".
  The `refund.taxable` refusal text adds "or before 2024". The four `stage16` fixtures that record that remedy text
  follow the new wording. No expression changed.
- **Fix lines:** `refund.not_2024`, `refund.taxable` (refusal text)
- **Siblings checked:** `refund.box8`, `refund.exc_tax`, `refund.exc_who`, `refund.received`. Generated at integration (the packages were integrated together) and covered by this round's reruns and adjudication of their forms' reviews: `refund.taxable`.
- **Regression predictions:** no evaluated value changes. The 4 recorded `refund.not_2024` refusals in
  `fixtures/2025/stage16.json` keep their gate, and only the remedy text changes.
- **Validation:** fixtures 1,446/1,446. A GPT-6 Astra second reading (receipts/) agreed for mixed 2023 and 2024
  payments. It noted that a refund wholly of 2023-paid tax is not a multi-year allocation. That case is still not a
  plain 2024 recovery: the TIP turns on "the year you paid the tax". So the refusal stays, as an accepted over-refusal at
  worst. The integrator reruns the refund screen review. `amb.2025.refund_exceptions` names items 1 and 5 only; its
  text could note the pre-2024 case (not edited here).
- **Tags:** scope-screen-narrower-than-line; amount-affecting; caught-by-screen-review; fixed

## BUG-0363 — Form 4952's screens refused whole returns that do not use Form 4952

- **Caught by:** the coverage tree build (`tools/coverage/tree.py`), T-101 (the f4952 part).
- **Source:** f4952 p. 3, Who Must File, "you must file Form 4952 to claim a deduction for your investment interest
  expense" and "Exception. You don’t have to file Form 4952 if all of the following apply"; p. 4, Line 4g, "To make the
  election, enter on line 4g the amount you elect to include in investment income"; p. 4, Note, "you can treat less of
  the amount on line 4e as attributable to line 4g".
- **Symptom:** **Evaluated** on `stage5.return.refund` (standard deduction, Form 4952 line 1 $0, no carryforward, line 4g
  $0). With `f4952.unsupported` Yes, Form 1040 lines 12e and 24 to 37 were REFUSED; `f4952.alternative_allocation` Yes did
  the same. The refusals sat on `f4952.line2`, `f4952.election`, `f4952.line5` and `f4952.required`, and those lines were
  read on every return: through `sa.line9` (Schedule A is figured for the standard-or-itemized comparison),
  `sd.filing4952` and `sd.investment_election`. `f4952.unsupported` asks about any business, royalty or passive
  interest. So a Schedule C filer with business loan interest and no investment interest would truthfully answer Yes
  and be refused.
- **Fix:**
  - New helper `f4952.used`: line 4g above zero (new helper `f4952.has_election`), a 2024 carryforward, or line 1 above
    zero.
  - `f4952.line8` is a choose on `f4952.used` (new helper `f4952.deduction` holds the smaller of lines 3 and 6).
  - `f4952.required` is `f4952.used` and `f4952.required_test`, the former expression with its refusals.
  - `f4952.election` is a choose on `f4952.has_election` (new helper `f4952.election_checked` holds the former copy of
    line 4g with its three refusals).

  No gate id, input or refusal declaration changed, so `tree.py --check` still places every gate. With no investment
  interest, no carryforward and no election, the screens are not reached and lines 8, 4g (as elected) and the filing
  test are zero or false.
- **Fix lines:** `f4952.used`, `f4952.has_election`, `f4952.election`, `f4952.election_checked`, `f4952.line8`,
  `f4952.deduction`, `f4952.required`, `f4952.required_test`
- **Siblings checked:** `f4952.alternative_allocation`, `f4952.bad_dividends`, `f4952.bad_election`,
  `f4952.election_limit`, `f4952.exception`, `f4952.line1`, `f4952.line2`, `f4952.line3`, `f4952.line4a`,
  `f4952.line4b`, `f4952.line4c`, `f4952.line4d`, `f4952.line4e`, `f4952.line4f`, `f4952.line4g`, `f4952.line4h`,
  `f4952.line5`, `f4952.line6`, `f4952.line7`, `f4952.unsupported`, `f4952.zero`, `sa.line9`, `sd.filing4952`,
  `sd.investment_election`
- **Regression predictions:** written from the source before the evaluator was run; all matched.
  - New `stage4.f4952.unused_unsupported` and `stage4.f4952.unused_alternative_allocation` (stage4.base with one screen
    Yes): every stage4.base value unchanged, `f4952.line8` $0, `f4952.election` $0, `f4952.required` false.
  - New `stage5.return.refund_f4952_screens_unused` (both screens Yes): every Form 1040 value of stage5.return.refund
    unchanged, `f4952.line8` $0.
  - Existing fixtures changed: `stage4.refuse.4952.unsupported`, `.alternative_allocation` and `.bad_dividends` had line
    1 $0, so they tested the over-refusal. They now carry $1,000 of investment interest and still refuse with the same
    gates. In those two cases and in `.unsupported_with_carryover` (line 4g $0), `f4952.election` is now $0 instead of
    REFUSED, because the election helper is screened only when an election is entered. The refusal stays on lines 2, 5
    and 8.
  - `bad_dividends` with no Form 4952 is still refused on the return by `div.bad_components`.
- **Validation:** fixtures 1,446/1,446; adapter contracts pass (f4952: 19 cases); refusal reach 323 checked, 0
  exceptions. A GPT-6 Astra second reading agreed (receipts/). The integrator reruns the f4952 transcription, render
  and class M reviews and the f4952 screen reviews (`check_screens.py` lists both screens' rulings as stale).
- **Tags:** over-refusal; scope-screen-wider-than-use; existing-form-pass; fixed

## BUG-0364 — A covered month with zero in column (b) completed with the month's credit lost (owner decision C1)

- **Caught by:** the C-backlog reproduction of BUG-0298 (T-165), carried to T-180 by owner decision C1, 2026-11-02.
- **Source:** p974 p. 6, "To qualify for a monthly credit amount, at least one individual in your tax family must be enrolled in a qualified health plan on the first day of that month.", "The applicable SLCSP premium is the second lowest cost silver plan premium offered through the Marketplace where you reside that applies to your coverage family", "may report your applicable SLCSP premium as -0-", "In either case, you must determine your correct applicable SLCSP premium."; i8962 p. 16, Column (b), "Enter on lines 12 through 23, column (b), the amount of the monthly applicable SLCSP premium reported on Form 1095-A, lines 21 through 32, column B, for the corresponding month"; i8962 p. 17, "credit amount because your enrollment premiums for the month were unpaid, enter -0- on the appropriate line on Form 8962, column (b)".
- **Symptom:** a month with enrollment premiums in column (a) and zero in column (b) completed with no credit for that month. C-backlog witness: one Form 1095-A, January to June, column A $500, B $450, C $300; March column B entered as 0 gave line 24 $1,485 against $1,782. Pub. 974 (archived) was searched for a legitimate covered month with column A above zero and column B zero. The only one in Pub. 974 and i8962 is a month whose premiums were unpaid (i8962 p. 17), and `f8962.other` already refuses it. Every other case where column B is zero is refused by its own gate: other coverage (an empty coverage family), allocation, the year of marriage, QSEHRA, and a person who is not lawfully present. The other zero is the "-0-" that a Marketplace reports when no APTC was paid, and the filer must replace it with the correct premium.
- **Fix:** new helper `f8962.b_zero`: an applicable taxpayer (`f8962.show_applicable`) with any month of lines 12 to 23 where column (a) is above 0 and column (b) is 0. The uniform route is covered because its monthly lines carry `mo_a`/`mo_b`. The helper is folded into the existing computed gate `f8962.two_counted` (any of the old test or `b_zero`), so the coverage tree's gate placement does not change. The gate's label, the line 24/25 refusal remedy and the refusal cite name the zero column (b) case, and the form note lists it.
- **Fix lines:** `f8962.b_zero`, `f8962.two_counted`, `f8962.line24`, `f8962.line25`
- **Siblings checked:** `f8962.same_state_counted`, `f1095a.b_counted`, `f1095a.b_used`, `f1095a.b_jan` to `f1095a.b_dec`, `f1095a.in_b_jan` to `f1095a.in_b_dec`, `f1095a.mo_b`, `f8962.line11a`, `f8962.line11b`, `f8962.line12a` to `f8962.line23b`, `f8962.other`; also generated, covered by the rerun reviews of their forms: `f1095a.a_jan` to `f1095a.a_dec`, `f1095a.in_a_jan` to `f1095a.in_a_dec`, `f1095a.mo_a`, `f1095a.c_total`, `f8962.aptc_total`. Generated at integration (the packages were integrated together) and covered by this round's reruns and adjudication of their forms' reviews: `f8962.line24`, `f8962.line25`, `f8962.line9`, `f8962.two_counted`.
- **Regression predictions:** written before evaluation. `stage18.refuse.b_zero_monthly` (the `stage18.blind.p10` inputs with March column B 0) refuses at `f8962.line24` and `f8962.line25` with gate `f8962.two_counted`. `stage18.refuse.b_zero_uniform` (the `stage18.blind.p1` inputs with `mo_b` 0, line 11 route) refuses the same way. Both matched, and `s3.line9` also refuses. `stage18.refuse.two_counted_same_state` keeps its gate and lines. Only its recorded remedy and cite text were updated to the new wording. No other fixture changed. Fixtures 1,444/1,444.
- **Validation:** source inspection of Pub. 974 and i8962. A GPT-6 Astra second reading (receipts/c1_astra_*.txt) found no legitimate case described. It noted that the text does not prove no such case exists. Any case it missed would be refused, not miscomputed.
- **Tags:** premium-tax-credit; amount-affecting; refusal; fixed

## BUG-0365 — BUG-0321 is settled: Schedule A line 1 takes Marketplace premiums less the credit allowed, not less the advance payments

- **Caught by:** T-180 (BUG-0321's open question on a net premium tax credit), reading Pub. 502.
- **Source:** p502 p. 12, Premium Tax Credit, "You can’t include in medical expenses the amount of health insurance premiums paid by or through the premium tax credit", "You also can’t include in medical expenses any amount of advance payments of the premium tax credit made that you did not have to pay back", "However, any amount of advance payments of the premium tax credit that you did have to pay back can be included in medical expenses", Example 1, "You are treated as paying $5,100 ($8,700 less the allowed premium tax credit of $3,600)"; i8962 p. 2, "You cannot deduct the portion of your health insurance premium on your tax return that is paid for by the PTC or APTC (after you determine how much of any excess APTC you must repay)"; i1040sca p. 2, "fill out Form 8962 before filling out Schedule A, line 1".
- **Symptom:** the BUG-0321 wording told the filer to "leave out premiums paid by advance payments of the premium tax credit". That is right only when the credit allowed equals the advance payments. On Pub. 502's own examples it gave $4,500 where the rule gives $5,100 when excess advance payments are repaid (Example 1), and $4,500 where the rule gives $3,800 when a net credit is claimed (Example 2). Line 1 is a supplied amount, so the error passes into line 4 whenever medical expenses exceed 7.5% of AGI. Not reproduced by evaluation, because the defect is in the wording.
- **Fix:** wording only (owner decision 2026-11-02: not a computed split). For Marketplace coverage, `sa.line1` now takes the total premiums (including the part paid by advance payments), minus the credit allowed on Form 8962 line 24, minus any excess advance payments not repaid because of the repayment limit (line 27 minus line 29). Advance payments that are repaid count as premiums paid. Checked against both Pub. 502 examples (8,700 − 3,600 − 0 = 5,100; 8,700 − 4,900 = 3,800) and against a capped-repayment case. The self-employed health insurance with premium tax credit case stays refused by `sc.hi_screen` (Pub. 974 iterative method).
- **Fix lines:** `sa.line1`
- **Siblings checked:** `sa.line4`, `sa.agi_floor`, `f8962.line24`, `f8962.line27`, `f8962.line29`, `s1.line17`, `sc.hi_screen`
- **Regression predictions:** wording only. No expression changed and no fixture value moves.
- **Validation:** source inspection; arithmetic on the two Pub. 502 examples.
- **Tags:** source-definition-debt; wording; schedule-a; premium-tax-credit; cross-form; fixed

## BUG-0366 — BUG-0327 is closed: three of its four parts were already refused; the corrected-SLCSP situations are stated

- **Caught by:** BUG-0327, recorded open (T-180). This entry closes it because the inventory is append-only.
- **Source:** i8962 p. 14, "If the correct applicable SLCSP premium is not the same for every month of 2025, check “No”"; p. 15, "Examples of changes in circumstances that may affect your applicable SLCSP premium include the following", "You moved during 2025", "If any of the above apply and you did not notify the Marketplace or if you have reason to believe the Marketplace reported the wrong applicable SLCSP premium, determine the correct applicable SLCSP premium for the months affected".
- **Symptom (premise check):** The `f8962.other` question already asks whether "someone enrolled in a Marketplace policy was not lawfully present" and whether "any part of a month's premium was not paid by the due date of your return", and it refuses both. So the not-lawfully-present part, the unpaid-share part and the partial-payment part of BUG-0327 are refused, not missed. A partial payment that kept coverage in force is refused, an over-refusal already accepted in the `f8962.other` ruling. What remained was the list of situations that make column B wrong. The questions said only "blank, wrong, or zero".
- **Fix:** wording only. The `f1095a.uniform` question now says to answer no if the correct column B is not the same every month. It lists the i8962 p. 15 changes in circumstances, and the no-APTC case, that make column B wrong for the months affected. The twelve `f1095a.in_b_<month>` questions and `f1095a.mo_b` add "for example after a move or a change in your tax or coverage family that you did not report to the Marketplace". The shared cites (`f1095a.months`/`f1095a.uniform`; the column B lines) add the p. 14 and p. 15 sentences. BUG-0364 catches a zero that remains.
- **Fix lines:** `f1095a.uniform`, `f1095a.in_b_jan` through `f1095a.in_b_dec`, `f1095a.mo_b`
- **Siblings checked:** `f1095a.months`, `f1095a.b_jan` to `f1095a.b_dec` (share the column B cite), `f1095a.b_counted`, `f8962.line10`, `f8962.nonuniform`, `f8962.show_annual`, `f8962.other`; also generated, covered by the rerun reviews of their forms: `f1095a.line33a`, `f1095a.line33b`, `f1095a.line33c`, `f1095a.yr_b_monthly`, `f1095a.yr_b_uniform`. Generated at integration (the packages were integrated together) and covered by this round's reruns and adjudication of their forms' reviews: `f1095a.a_apr`, `f1095a.a_aug`, `f1095a.a_dec`, `f1095a.a_feb`, `f1095a.a_jan`, `f1095a.a_jul`, `f1095a.a_jun`, `f1095a.a_mar`, `f1095a.a_may`, `f1095a.a_nov`, `f1095a.a_oct`, `f1095a.a_sep`, `f1095a.b_apr`, `f1095a.b_aug`, `f1095a.b_feb`, `f1095a.b_jul`, `f1095a.b_jun`, `f1095a.b_mar`, `f1095a.b_may`, `f1095a.b_nov`, `f1095a.b_oct`, `f1095a.b_sep`.
- **Regression predictions:** wording only. No expression changed and fixtures pass unchanged.
- **Validation:** source and implementation inspection.
- **Tags:** source-definition-debt; wording; premium-tax-credit; fixed

## BUG-0367 — BUG-0326, Schedule A part: whose medical expenses count and the line 5a to 5c rules are stated

- **Caught by:** BUG-0326 (the sa completeness claims sa#1 to sa#4), recorded open (T-183). This entry closes its Schedule A part. The sc, scveh and asset parts stay open.
- **Source:** i1040sca p. 2, "You can include medical and dental bills you paid in 2025 for anyone who was one of the following either when the services were provided or when you paid for them", "Your child whom you don't claim as a dependent because of the rules for children of divorced or separated parents", "Any person you could have claimed as a dependent on your return except that person received $5,200 or more of gross income or filed a joint return", "You can't deduct any premiums attributable to this individual unless", "However, if you had family coverage when you added this individual to your policy and your premiums didn't increase", "If you received a reimbursement in 2025 for prior year medical or dental expenses, don't reduce your 2025 expenses by this amount", "(cafeteria plan) unless the premiums are included in box 1 of your Form(s) W-2"; p. 3, Line 5a (withholding deducted elsewhere, estimated payments, "Don't include penalties or interest.", the mandatory disability, unemployment and family leave fund contributions, refunds not reducing, the state-tax-credit safe harbor); p. 6, Line 5b (business use, uniform general-purpose levies, foreign taxes, service charges, improvement assessments and the maintenance exception, escrow, tax charged to the buyer, refunds and rebates); p. 6, Line 5c ("based on value alone and were imposed on a yearly basis", the car-fee example); p. 7, "Only taxes paid in 2025 and assessed prior to 2026 can be deducted for 2025".
- **Symptom:** as recorded in BUG-0326 for Schedule A.
- **Fix:** wording only.
  - `sa.line1` names whose expenses count and leaves out premiums for a nondependent on the policy (except with family coverage whose premiums did not increase). It also leaves out amounts paid by a cafeteria plan unless included in W-2 box 1, and says a 2025 reimbursement of an earlier year's expenses does not reduce 2025 expenses.
  - `sa.line5a` states the payments that count, excludes penalties and interest, and includes the mandatory fund contributions. It says refunds do not reduce the amount, and it states the state-tax-credit safe harbor.
  - `sa.line5b` states the business-use, uniform-levy and general-purpose tests. It also states the foreign tax, service charge and improvement exclusions (and the maintenance exception), the escrow rule, tax charged to the buyer, and the refund rules.
  - `sa.line5c` states the value-only yearly test, the car-fee example and the paid/assessed rule.
  - The person who can be claimed by someone else (the third i1040sca list item) is not stated, because `sa.dependent` refuses the whole return.
- **Fix lines:** `sa.line1`, `sa.line5a`, `sa.line5b`, `sa.line5c`
- **Siblings checked:** `sa.line4`, `sa.line5d`, `sa.agi_floor`, `sa.dependent`, `sa.unsupported` (sales-tax election and foreign taxes), `sa.line11` (charitable gifts reduced by a state tax credit), `ltc.payments`
- **Regression predictions:** wording only. No expression changed and no fixture value moves.
- **Validation:** source inspection; every added quote is checked by `citations.py --strict`.
- **Tags:** source-definition-debt; wording; schedule-a; fixed

## BUG-0368 — BUG-0308 is fixed: the long-term care question states who may be covered

- **Caught by:** BUG-0308, recorded open (T-171). This entry closes it.
- **Source:** i7206 p. 1, "You may be able to deduct the amount you paid for health insurance, which includes medical, dental, and vision insurance and qualified long-term care insurance for yourself, your spouse, and your dependents.", "The health insurance can cover your child who was under age 27 at the end of 2025, even if the child wasn’t your dependent.", "A child includes your son, daughter, stepchild, adopted child, or foster child."
- **Symptom:** as recorded in BUG-0308.
- **Fix:** wording only. `ltc.payments` says the person must be the filer, the spouse, a dependent, or a child (son, daughter, stepchild, adopted or foster child) under age 27 at the end of 2025, and to enter zero for anyone else. The cite adds the three i7206 p. 1 sentences. The health insurance questions `sc.hi_uses` and `sc.f7206_line1` already name the same people.
- **Fix lines:** `ltc.payments`
- **Siblings checked:** `ltc.amount`, `ltc.limit`, `sc.hi_uses`, `sc.f7206_line1`, `sc.hi_screen` (the retired public safety officer and multiple-business ltc claims are refused there)
- **Regression predictions:** wording only. No expression changed.
- **Validation:** source inspection.
- **Tags:** source-definition-debt; wording; fixed

## BUG-0369 — BUG-0314, premise check: most Form 5329 Part I items are already refused; two remain, in a form this package does not own (open)

- **Caught by:** the T-175 premise check, 2026-11-03.
- **Source:** i5329 p. 1 and p. 3, Line 1; p. 5, Line 2 (the exception conditions); p590b p. 28, "If you received a distribution to buy, build, or rebuild a first home and the purchase or construction was canceled or delayed".
- **Symptom (premise check, inspected in `forms/2025/retirement.yaml`):**
  - Already refused:
    - a Roth IRA distribution other than code Q, so any Form 8606 line 25c or recapture amount (`retirement.bad_code`);
    - a modified series of substantially equal periodic payments (`retirement.early_screen`);
    - a returned 2024 or 2025 IRA contribution, with its earnings (`retirement.special`).
  - Already computed: the rolled-over part is taken out of the taxable amount (`retirement.rolled`, `retirement.l1`).
  - Open:
    - the recontribution within 120 days of a first-home distribution whose purchase was canceled or delayed;
    - the exception conditions. `retirement.exception` names the exceptions but does not state their conditions, for example separation from service in or after the year the person reached 55 (plans only), the disability proof, and the series that must begin after separation from an employer plan.
- **Disposition:** needs `retirement.rollover` and `retirement.exception` (form `retirement`), outside this package's forms. Proposed wording is in REPORT.md (T-175). `f5329` lines only copy `person.x_*`, which sum `retirement.*`.
- **Validation:** implementation inspection.
- **Tags:** source-definition-debt; explicitly-deferred

## BUG-0370 — Form 4562 line 2 counted land improvements and excepted property as section 179 property (T-182)

- **Caught by:** owner question 3 of the A-backlog session (2026-11-02; owner decision A3: an engineering defect) and sc completeness claim 8 (BUG-0326); confirmed by evaluation in this package.
- **Source:** p946 p. 17, "Land and land improvements do not qualify as section 179 property" and "Even if the requirements explained earlier under What Property Qualifies? are met, you cannot elect the section 179 deduction for the following property" (noncorporate lessors, use outside the United States, tax-exempt organizations, governmental units and foreign persons); i4562 p. 2, "Property held for investment (section 212 property)"; p. 3, "for taxpayers other than a corporation, this election does not apply to any section 179 property you purchased and leased to others unless"; p. 4, Line 2, "Enter the total cost of all section 179 property you placed in service during the tax year".
- **Symptom:** `asset.is_section179` was true for every class other than qualified improvement property, so the business cost of any asset placed in service in 2025 and used more than 50% in the business went into Form 4562 line 2. Evaluated on the old tree: furniture of $2,000,000 fully elected, a paved parking area (class 00.3) of $2,400,000 and a $400,000 carryover gave line 2 $4,400,000, line 5 $2,100,000, line 12 $2,100,000, line 13 $300,000 and Schedule C line 13 $2,220,000. The source gives line 2 $2,000,000, line 12 $2,400,000 and Schedule C line 13 $2,520,000. The tax changes only when line 2 exceeds $4,000,000. Then line 11 (the smaller of business income or line 5) can cut a carryover or the deduction, or the election is refused as above line 5. At that income Form 1040 line 24 is refused anyway for Form 8995-A, but Schedule C line 13 and the printed Form 4562 lines 2, 4, 5 and 11 to 13 were wrong. Nothing stopped a section 179 election on such property either. The `asset.s179` question only told the filer to enter zero.
- **Fix:** new input `asset.not179`: a land improvement, investment property, property a noncorporate lessor purchased and leases to others (unless the two exceptions apply), or property used by a tax-exempt organization, a governmental unit or a foreign person or entity (with the source's exceptions). `asset.is_section179` requires it to be No. `asset.s179_bad` adds it, so an election above zero on such property refuses at `asset.after179`; the refusal form and remedy name it. `asset.s179` adds the tax-exempt, governmental and foreign-user items to its zero list. The question is read only for a 2025 asset used more than 50% in the business, or one with an election. It is not asked for qualified improvement property with no election (evaluated).
- **Fix lines:** `asset.not179`, `asset.is_section179`, `asset.s179_bad`, `asset.after179`, `asset.s179`
- **Siblings checked:** `asset.after179`, `asset.f26i`, `asset.is_section179`, `asset.period`, `asset.qip_early`, `asset.s179_2025`, `asset.s179_bad` (generated by `tools/siblings (py file); the package also checked `scveh.cost179_o` and the sc totals, see T-205)
  - `asset.cost179_real`, `asset.cost179_2025`, `asset.cost179`, `sc.cost179_a`, `sc.cost179`, `person.cost179`, `s179.line2`, `s179.line4`, `s179.line5`, `s179.line11`, `s179.line12`, `s179.over_limit`, `asset.f26i`, `asset.on_19`, `sc.f6`, `s179.line6`.
  - `scveh.cost179_o` and `scveh.s179_elect` are not changed. A vehicle used by a governmental unit or leased to others by a noncorporate lessor is still counted on line 2. That is rare for a car-and-truck entry, and a regular business of leasing passenger automobiles is screened. Recorded as a new-row proposal.
  - The trade-in rule (p946 p. 17, "its cost for purposes of the section 179 deduction includes only the cash you paid") is stated in `asset.s179` but not applied to line 2, which uses the whole business cost. Also a new-row proposal.
  - Lodging property, named in the parent's brief, is not in the 2025 list (p946 p. 17). It was not added.
- **Regression predictions:**
  - `stage14.s179.land_improvement` (the witness above, with `not179` Yes on the parking area): line 2 $2,000,000; line 4 $0; line 5 $2,500,000; line 9 $2,000,000; line 11 $2,500,000; line 12 $2,400,000; line 13 $0; Schedule C line 13 $2,520,000 ($2,400,000 plus 5.00% of $2,400,000 from Pub. 946 Table A-1, 15-year, year 1). Matched.
  - `stage14.asset.refuse_s179_not179` (the $3,000 computer of `stage14.asset.hy_5yr`, fully elected, `not179` Yes): refuses at `asset.after179` with gate `asset.s179_bad`. Matched.
  - `stage14.asset.refuse_s179_over` and `stage14.asset.refuse_s179_half` quote the refusal and follow its new wording.
- **Validation:** fixtures 1,446/1,446; evaluator witness before and after; GPT-6 Astra second reading (receipt `research/audits/asset-veh-sc/receipts/gpt-6-astra.168k9_line2.*`) also excludes all three kinds of property from line 2 and the threshold under sections 179(d)(1), 50(b) and 179(d)(5).
- **Tags:** amount-affecting (printed lines; tax above $4,000,000); eligibility; new-input; existing-form-pass; fixed

## BUG-0371 — Owner decisions A1, A2 and A4: used property and section 168(k)(9) property for the special allowance; employee-used vehicles (T-178)

- **Caught by:** A-backlog owner questions 1, 2 and 4 (2026-11-02); owner decisions A1, A2, A4.
- **Source:**
  - i4562 p. 6, "Qualified property can be either new property or certain used property".
  - p946 p. 31, "Original use means the first use to which the property is put, whether or not by you", and "Property containing used parts will not be treated as reconditioned or rebuilt if the cost of the used parts is not more than 20% of the total cost of the property".
  - i4562 p. 7, Exceptions, "Property described in section 168(k)(9)(A) or 168(k)(9)(B)". The plain description restates IRC 168(k)(9) and 163(j)(7)(A)(iv), (j)(9), which are not archived.
  - i4562 p. 14, Column (c), "Treat vehicles used by employees as being used 100% for business/investment purposes if the value of personal use is included in the employees’ gross income, or the employees reimburse the employer for the personal use".
- **Symptom:**
  - A1: nothing asked whether 2025 property claiming the special allowance was used property, for assets or for vehicles (`scveh.bonus_choice` had the same defect).
  - A2: the asset screen named section 168(k)(9)(A)/(B) by number only, and vehicles were not asked about it at all.
  - A4: "your employees use it" sat in `scveh.screen`, which only `scveh.cost` reads. A leased vehicle on actual expenses, or the operating expenses of an owned one, was figured from the filer's miles with employees' personal use (premise from the A-backlog evaluation, rechecked by reading the dependency: `scveh.screen` → `scveh.screened` → `scveh.cost` only).
- **Fix:**
  - `asset.screen` and `scveh.screen` add two items, each conditional on claiming a special depreciation allowance in 2025: original use did not begin with you (with the definition and the reconditioned-property 20% rule); and section 168(k)(9)(A)/(B) property, described in plain words. The asset screen's earlier unconditional 168(k)(9) item is replaced by the conditional one.
  - New input `scveh.employee_use` (do your employees use this vehicle for personal purposes) and gate `scveh.employee_bad`, refused on `scveh.operating_business`, which every actual-expense vehicle reads, owned or leased. The employee item is removed from `scveh.screen`. New gate placed in `tools/coverage/tree.json` (196 gates placed).
- **Fix lines:** `asset.screen`, `scveh.screen`, `scveh.employee_use`, `scveh.employee_bad`, `scveh.operating_business`
- **Siblings checked:** `asset.bonus_choice`, `asset.bonus`, `asset.bonus_fullcase`, `scveh.bonus_choice`, `scveh.claims_bonus`, `scveh.bonus_2025`, `scveh.cost`, `scveh.screened`, `scveh.line9`, `scveh.line9_actual`, `scveh.lease_business`, `scveh.line20a`, `scveh.smr_amount` (the standard rate path does not read the employee question; the owner decision named operating expenses and leases), `scveh.over_half`, `asset.pct` (vehicles use miles; the 100% rule is a vehicle rule).
- **Regression predictions:**
  - `stage14.veh.refuse_employee_use_lease`: the leased vehicle of `stage14.veh.refuse_lease_smr_before`, without the earlier standard rate, with `employee_use` Yes, refuses at line 9 with gate `scveh.employee_bad`. Matched; line 20a still evaluates ($3,000), but Schedule C line 9 and Form 1040 line 24 refuse.
  - `stage14.veh.refuse_employee_use_owned` (the same vehicle, owned): the same refusal. Matched.
  - The screen items are wording on screens whose Yes already refuses; no fixture.
- **Validation:** fixtures 1,446/1,446; GPT-6 Astra second reading of the 168(k)(9) restatement (it found the floor plan vehicle definition and the 163(j)(1)(C) reference missing from the first draft; both added).
- **Tags:** eligibility; owner-decision; new-input; existing-form-pass; fixed

## BUG-0372 — Pub. 538 archived; the small business capitalization exemption settled (T-179; closes the T-174 claim 11 remainder and scveh completeness claim 2 of BUG-0326)

- **Caught by:** BUG-0311 claim 11 and BUG-0326 (scveh, capitalized vehicle costs); owner decision A5.
- **Source:** p538 (Rev. January 2022, the current edition, archived as `sources/2025/p538`) p. 17, Uniform Capitalization Rules, "The uniform capitalization rules do not apply to the following" and "A small business taxpayer that meets the gross receipts test under section 448(c) and that is not a tax shelter"; i1040sc p. 6, "A small business taxpayer (defined later under Part III) is not required to capitalize certain expenses to inventory or other property"; p. 15, the $31 million test.
- **Symptom:** i1040sc's "certain expenses" left open whether a small business taxpayer still had to capitalize some vehicle costs.
- **Fix:** none to an expression. Pub. 538 exempts a small business taxpayer from the uniform capitalization rules altogether, so "certain expenses" leaves nothing for one. `sc.method_other` already refuses a business that is not a small business taxpayer (gross receipts over $31 million, or a tax shelter). Its locator now cites p538 p. 17. The creative-property exception only widens the exemption for freelance artists, authors and photographers; any of them above $31 million is refused (accepted over-refusal).
- **Fix lines:** `sc.method_other` (citation only)
- **Siblings checked:** `sc.screened`, `sc.line1`, `scveh.line9`, `scveh.line20a`, `sc.inventory_other`, `sc.line35` to `sc.line42`.
- **Regression predictions:** none; no evaluated value changes.
- **Validation:** source reading; `fetch_sources.py` verifies 157 documents offline; `check_extraction.py` 122 PDFs, 0 failing.
- **Tags:** source-archive; owner-decision; closed-on-premise

## BUG-0373 — BUG-0326, Schedule C, vehicle and asset parts: the questions state or refuse the rules (T-183, except Schedule A)

- **Caught by:** BUG-0326, recorded open; this entry closes its sc, scveh and asset claims because the inventory is append-only. The Schedule A claims belong to another package.
- **Source:**
  - i1040sc:
    - p. 6: NIL income, "However, report royalties and other NIL income that is not self-employment income on Schedule E instead"; Installment sales.
    - p. 9: Line 22, "You can also deduct the cost of books, professional instruments, equipment, etc., if you normally use them within a year"; Line 23, "But some licenses, such as liquor licenses, may have to be amortized"; Line 24a, the $5-a-day incidental expense method, and "Other rules apply to luxury water travel".
  - p463 p. 12, Luxury Water Travel.
  - i1040gi p. 94, "A qualified small employer health reimbursement arrangement (QSEHRA) is considered to be a subsidized health plan maintained by an employer".
  - i4562:
    - p. 8, "Computer software. Use the straight line method over 36 months"; p. 9, "However, MACRS does not apply to films, videotapes, and sound recordings".
    - p. 10, the utility clearing and grading land improvements; p. 11, the credits and deductions that reduce the basis for depreciation; p. 12, the property that must be depreciated under ADS.
    - p. 14, "allocate the use based on the most appropriate unit of time the property is actually used".
  - p946 p. 17, section 179 excepted property (BUG-0370).
- **Symptom:** as recorded in BUG-0326.
- **Premise checks:**
  - sc claim 0 (line 9) holds no gap. `scveh.smr_ok` asks the first-year, whole-lease and five-vehicle rules, and `scveh.lease_smr_before` the leased-vehicle rule. Depreciation, section 179 and the special allowance are guarded by `scveh.is_actual_owned`, and line 20a is zero on the standard rate (inspected; `stage14.veh.standard` completes with line 31 equal to receipts less line 9). The Part IV statement is presentation.
  - sc claim 6 (home depreciation with the simplified method) holds no gap. A home is real property, which `asset.screen` refuses, and nothing else feeds line 13 from the home.
  - sc claim 7 (section 179 limits): fixed by BUG-0370. The like-kind exchange is screened, the SUV cap is `scveh.s179_bad`, and the trade-in limit is stated (line 2 remainder: new-row proposal).
  - scveh claim 2 is BUG-0372.
- **Fix:**
  - `asset.screen`:
    - replaces "you depreciate it under ADS" with the required-ADS cases (executive-order imports, the 263A(d)(3) election, QIP of an electing real property trade or business, 10-year or longer property of an electing farming business) or an ADS election;
    - adds films, videotapes and sound recordings; computer software unless placed in service in 2025 and fully deducted through section 179 and the special allowance; utility clearing and grading land improvements; and basis reduced by a credit or deduction (the p. 11 list).
  - `asset.pct` states the time-used rule for listed property.
  - `sc.special` replaces "installment sales of timeshares or residential lots" with any income reported under the installment method (including those sales), and adds licenses or other costs you must amortize, and luxury water travel.
  - Wording: `sc.line1` (NIL income that is not self-employment income goes on Schedule E); `sc.line22` (books and instruments used within a year; not longer-lived items); `sc.line23` (not licenses you must amortize); `sc.line24a` (incidental expenses, actual or $5 a day on a day with no meal expenses and no standard meal allowance); `sc.f7206_line1` (QSEHRA eligibility counts as an employer-subsidized plan).
- **Fix lines:** `asset.screen`, `asset.pct`, `sc.special`, `sc.line1`, `sc.line22`, `sc.line23`, `sc.line24a`, `sc.f7206_line1`
- **Siblings checked:** `asset.screened`, `asset.cost`, `asset.done`, `asset.class`, `asset.basis`, `asset.listed`, `asset.listed_low`, `sc.screened`, `sc.line28`, `sc.meals_50`, `sc.line24b`, `sc.hi_screen`, `sc.hi_screened`, `sc.f7206_line3`, `scveh.over_half`.
- **Regression predictions:** no evaluated value changes and no fixture added. Each new refusal is an item of a screen whose Yes already refuses (`stage14.refuse.special`, the asset screen fixtures).
- **Validation:** fixtures 1,446/1,446; `citations.py --strict` 0 findings.
- **Tags:** source-definition-debt; wording; existing-form-pass; fixed

## BUG-0374 — Class M jobs for single documents gave incoming values that only validation helpers read, and were not marked printed-only

- **Caught by:** T-139 (from T-066; owner's decision 2026-10-29), premise check on the current tree, 2026-11-03.
- **Source:** BUG-0143 (the same defect, fixed for collection documents only): an incoming-value catalog should hold what the printed calculation reads, not what implementation validation reads.
- **Symptom:** `buildJob` (engine/src/classm.ts) listed as authoritative givens every foreign line that any line of the document reads, helpers included, and set no `worked_scope`, so the request did not say that only printed lines are wanted and the log did not record the scope. Measured on the full job set (2,000 generated returns plus non-M fixtures, seed 7): see REPORT.md, T-139, for the documents and givens withheld.
- **Tool change:** `buildJob` keeps a given only if the printed lines requested read it through the document's own lines (`requestClosure`, the same rule `buildCollectionJob` applies to printed-only collections), and marks the job `worked_scope: "printed-irs-lines"`. `tools/transcription/classm.py` states the printed-only sentence in the single-document request as it already did in the entry request (one shared constant, byte-identical for collections). No old receipt is relabeled: a document migrates when its class M review is next rerun.
- **Changed form lines:** none (tool change: `engine/src/classm.ts` `buildJob`, `requestClosure`; `tools/transcription/classm.py` `build_prompt`, `PRINTED_ONLY`).
- **Related tools checked:** `buildCollectionJob` printed-only filter (unchanged; same rule), `buildDefJob` (definitions give only their parameters), `classm.py` `write_outputs` (the "worked target scope" row now appears for single documents).
- **Regression predictions:** `tools/transcription/test_classm_jobs.mjs`: every Form 2441 job is `printed-irs-lines`.
- **Validation:** job generation before and after on the full corpus (REPORT.md); test_classm_jobs.mjs; no model call.
- **Tags:** review-tool; worked-context-feedback; class-m; fixed

## BUG-0375 — Class M requests showed workers answers the route never reads, and the generated cases held answers the interview never asks

- **Caught by:** T-142 (Stage 18 O2, from T-079 (2)) and T-147 (Stage 19, from T-081 (5)); premise checked 2026-11-03.
- **Source:** the interview asks exactly the inputs the evaluation from its targets reads (`engine/src/interview.ts`, `interviewState`: "missing reachable inputs determine the questions").
- **Symptom:** (1) the generator answers both routes of a Form 1095-A so every line computes under `evaluateAll`, and the class M entry request listed all of them: a uniform entry showed `mo_a`, `mo_b`, `c_total` and all 36 monthly amounts, and the job asked for the month-by-month totals `yr_a_monthly`, `yr_b_monthly`, `yr_c_monthly` that only the untaken alternative of lines 33a to 33c reads; a month-by-month entry showed `mo_a`, `mo_b` and `c_total`, which after whole-dollar rounding need not agree with its months (O2), and models copied them. (2) The class M fixtures carry every generated answer, including answers the interview cannot give because nothing on the return's route reads them: `classm.f5695.2` holds `person[taxpayer].sav_claimed` true with `sa.dependent` false (`person.sav_ineligible` tests `sa.dependent` first and stops), `classm.f5695.8` and `classm.s3.3` hold `person[taxpayer].sav_excess` true with no Form W-2 box 12 deferrals (`person.sav_excess_gate` tests `person.sav_w2 > 0` first). Evaluated: none of the three answers is read from the interview's targets or the cases' expectations.
- **Tool change:** `routeJob` in `engine/src/classm.ts`, applied to every chosen job: an unprinted collection's helpers are requested only when some route reads them (`liveInCollection`); the answers shown are those the requested lines read (`answersRead` over a lazy evaluation from the requested lines); the fixture inputs keep rosters, the filing status and the answers read from the full interview's targets or by the requested lines. The requested values must be identical on the restricted answers (checked with `evaluateAll`); otherwise the job keeps every answer and the problem is printed. A job's branches are those the restricted answers take. The generator itself is unchanged: both routes stay answered there because evaluateAll-based tools (class M candidate filters, mutation, triage) need every line computed. The three named cases and their DeepSeek twins drop the unread answer (fixtures/2025/classm.json, classm.deepseek.json).
- **Changed form lines:** none (tool and fixture change).
- **Related tools checked:** every other class M case on the tree carries generator answers off its route (the same two saver's credit answers alone appear in 11 more Claude and 3 more DeepSeek cases, counted by input values); they are fixed when each document's class M review is regenerated. `buildDefJob` (definition jobs reach their instance through the calling lines, `defCallers`).
- **Regression predictions:** for the six edited cases, no expected value changes (the dropped answers are not read; prediction from the short-circuit order of `person.sav_ineligible` and `person.sav_excess_gate`, f8880 p. 2 "Who Can Take This Credit" and iw2w3 p. 20 box 12). test_classm_jobs.mjs: no Form 1095-A entry shows the other route's answers or requests the other route's totals; no Form 2441 case holds `sav_claimed` without `sa.dependent` Yes.
- **Validation:** test-fixtures; job generation before and after on the full corpus (REPORT.md); test_classm_jobs.mjs.
- **Tags:** review-tool; generator; class-m; unasked-answers; fixed

## BUG-0376 — Mutation report did not say which kills only class M cases made

- **Caught by:** T-144 (Stage 19: person, f2441 and ira kills lost on a class M rerun; from T-081 (6)).
- **Source:** none (tooling).
- **Symptom:** `outcome` in `engine/src/mutate.ts` stopped at the first case that killed a mutant, in file order, so the report could not tell a kill that depends on a class M case (which a class M rerun regenerates) from one a stage fixture also makes. `classm.py` already warns that replaced cases may carry kills, but not which.
- **Tool change:** reporting only: non-M cases are tried first; a mutant no other case kills but a class M case does is still killed, counted under "Killed by fixtures", and listed in a new report section "Killed only by class M cases" with the first class M case that kills it; the console line gives the count. No equivalence rule, mutant or score definition changed.
- **Changed form lines:** none (`engine/src/mutate.ts` `outcome`, `runMutation` report).
- **Related tools checked:** `mutantShare`/`outcomesOf` (workers pass the outcome strings through unchanged); `classm.py` `write_outputs` replacement warning (unchanged; it now has a report to consult).
- **Regression predictions:** the score and survivor set are unchanged (the kill/survive decision is the same set of cases); only attribution is added.
- **Validation:** a sample of the mutant list through `mutantShare` (REPORT.md); the full count is the parent's check-all mutate step.
- **Tags:** mutation; reporting; class-m; fixed

## BUG-0377 — The review interface did not say that the Schedule D carryover lines hold a negative amount

- **Caught by:** T-140 (Stage 20 adjudication, T-076 (3)).
- **Source:** f1040sd p. 1, lines 6 and 14 printed "( )"; i1040sd p. 11, 28% Rate Gain Worksheet line 5 "( )"; p. 13, Unrecaptured Section 1250 Gain Worksheet line 16 "( )".
- **Symptom:** the transcription prompt publishes only id, printed marker and type (`reference_note` and the requested-line list in tools/transcription/transcribe.py), so a candidate holding `sd.line6`, `sd.line14`, `g28.line5` or `u1250.line16` positive is a sign convention gap, not a reading error, yet triage reports value differences on every line that combines them.
- **Tool change:** `NEGATIVE_INTERFACES` and `sign_note` in transcribe.py add "a loss carryover printed in parentheses, held as a negative amount" to those four lines, both where they are requested and where another form's catalog lists them.
- **Changed form lines:** none (tool change).
- **Related tools checked:** the other signed Dollars lines whose labels say "negative" (`clcw.prior_11`, `clcw26` line 15 input, the worksheet helpers `sd.line6_ws`, `sd.line14_ws`) are not printed parenthesised interfaces read by another form's transcription; not changed.
- **Regression predictions:** the required-interface check (`input_context.assess`) of the saved g28 and u1250 transcription requests now reports `sd:sd.line14` missing (verified: g28 Claude and DeepSeek went from pass to fail; u1250 was already failing on `scope.schedule1` / `sales.special`). No other saved request lists these four lines as foreign interfaces.
- **Validation:** test_review_tools.py, test_input_context.py; the audit above. The integrator reruns sd, g28 and u1250 transcription.
- **Tags:** review-tool; interface; sign-convention; fixed

## BUG-0378 — Eleven Stage 18 to 21 fixtures carried a stray W-2 box 10 with Form 2441 benefits answered No

- **Caught by:** T-146 (Stage 19, from T-081 (4)); 11 cases found on the current tree (the task lists 11).
- **Source:** the generator's screen rule (engine/src/generate.ts `SCREENS`: box 10 is asked only after `f2441.benefits` Yes); `w2.box10` input text, "zero if the box is blank"; the cases' fact sheets state no dependent care benefits.
- **Symptom:** `stage18.blind.p6`, `p10`, `p20`, `stage18.refuse.year_of_marriage`, `stage18.mut.family_of_20`, `stage18.refuse.family_over_20`, `stage19.blind.e2`, `e4`, `stage20.blind.r7`, `stage21.blind.e7`, `stage21.refuse.e05_joint` held `person[taxpayer].w2[e0].box10` = $1,000 with `f2441.benefits` false.
- **Tool change:** the eleven values set to 0 by a line-local text edit (formatting kept).
- **Changed form lines:** none (fixtures).
- **Related tools checked:** every fixture file for a nonzero box 10 or box10_wages without `f2441.benefits` Yes: none remain.
- **Regression predictions:** no expected value changes. None of the cases asserts a Form 2441, line 1e or box 10 line; with benefits No, Part III is not reached and line 1e is zero, so the line 1e attribution helpers that read box 10 do not affect any asserted line (i2441 p. 5, Line 12, "Amounts you received as an employee should be shown in box 10 of your Form(s) W-2").
- **Validation:** test-fixtures.
- **Tags:** fixtures; stray-input; fixed

## BUG-0379 — Generated returns left three dependent answers unanswered

- **Caught by:** T-148 (Stage 21, from T-081 (7)); premise re-checked 2026-11-03.
- **Source:** dependent.yaml, `dependent.hoh_lived_half` and `dependent.dc_lived_half` read `dependent.born_died` and `dependent.placed` (then `dependent.part_year_home`) for a person who is not a qualifying child and lived with you half the year or less.
- **Symptom:** on the seeded sample (1,000 returns, seed 7), 4 returns reached `dependent[].born_died`, `placed` and `part_year_home` unanswered (20, 4 and 4 derivations). `f1040.line24` and `f1040.line37` were not unknown on any of the 1,000 (in two the unknown was masked, two refused elsewhere), so the task's "line 24 is unknown" premise no longer holds as stated; the unanswered inputs do.
- **Tool change:** `buildInputs` (engine/src/generate.ts) answers `born_died` and `placed` No for every dependent, after every draw, so neither the random stream nor the derived streams move. `part_year_home` is then never reached.
- **Changed form lines:** none (generator).
- **Related tools checked:** the same probe over all reached unknown inputs for `f1040.line24` and `f1040.line37` on 1,000 returns: none remain after the change.
- **Regression predictions:** no generated return reaches a dependent answer unanswered; other generated values are unchanged (keys added last).
- **Validation:** the probe (REPORT.md).
- **Tags:** generator; unanswered-input; fixed

## BUG-0380 — Qualified disaster recovery distributions outside codes 1 and S are not screened

- **Caught by:** the `retirement.special` screen review, backlog round, 2026-11-03 (`.transcription/proposed/bklg/screens.findings.md`, PENDING-7-1).
- **Source:** p575 p. 35, "the distribution is included in income ratably over 3 years unless you elect to report the entire amount in the year of distribution"; "Use Form 8915-F to report qualified disaster recovery distributions and repayments."
- **Symptom:** `retirement.early_screen` names the distribution, but `retirement.screen_refused` reads it only for codes 1 and S, and `retirement.special` does not name it; a code 7, 2 or 4 qualified disaster recovery distribution is taxed in full on line 4b/5b (witness from the review: $18,000 against $6,000), and a repayment is unasked.
- **Disposition:** T-210: add the distribution and its repayment to `retirement.special` (wording; the refusal already names Form 8915-F); check whether `scope.other_income` catches the 2025 portion of a 2023 or 2024 distribution.
- **Validation:** screen-review finding with quotes matched; not reproduced by evaluation.
- **Tags:** screen-gap; amount-affecting; pre-existing; explicitly-deferred

## BUG-0381 — `retirement.rollover` excludes rollovers made late under a waiver or extension

- **Caught by:** the `retirement.special` screen review, backlog round, 2026-11-03 (PENDING-7-2).
- **Source:** p575 p. 23, "There are three ways to obtain a waiver of the 60-day requirement"; "The 60-day rollover period is extended by the period for which the amount is a frozen deposit".
- **Symptom:** the input asks for the amount "rolled over within 60 days", so a valid waived or extended rollover is entered as $0 and taxed.
- **Disposition:** T-210: wording in `retirement.rollover`; the computation is unchanged.
- **Validation:** screen-review finding with quotes matched; not reproduced by evaluation.
- **Tags:** source-definition-debt; amount-affecting; pre-existing; explicitly-deferred

## BUG-0382 — Payments while legally separated spouses share a household are counted as alimony

- **Caught by:** the `s1.alimony_unsupported` screen review, backlog round, 2026-11-03 (PENDING-7-3).
- **Source:** p504 p. 14, "Payments to your spouse while you're members of the same household aren't alimony if you're legally separated under a decree of divorce or separate maintenance."
- **Symptom:** neither `s1.alimony_unsupported` nor the amount questions mention the household, so such payments are deducted or included. The same list's "doesn't designate the payment as not alimony" is also unstated.
- **Disposition:** T-210: add the item to `s1.alimony_unsupported` and the designation rule to `s1.alimony_received`/`s1.alimony_paid`.
- **Validation:** screen-review finding with quotes matched; not reproduced by evaluation.
- **Tags:** screen-gap; amount-affecting; pre-existing; explicitly-deferred

## BUG-0383 — Qualified improvement property is offered as a class without its definition

- **Caught by:** the asset completeness review, backlog round, 2026-11-03 (`.transcription/proposed/bklg/completeness.findings.md`, M1).
- **Source:** p946 p. 31, "Generally, this is any improvement to an interior part of a building that is nonresidential real property ... placed in service by you after 2017 and after the date the building was first placed in service by any person"; "The enlargement of the building. • Any elevator or escalator. • The internal structural framework of the building."
- **Symptom:** `asset.class` offers "qualified improvement property" with no definition, so an elevator, an enlargement, structural framework or an improvement to residential rental property can take 15 years, the special allowance and section 179 instead of being refused as real property.
- **Disposition:** T-211: state the definition and exclusions in `asset.class`, cite p946 p. 31.
- **Validation:** completeness claim with quotes matched; not reproduced by evaluation.
- **Tags:** source-definition-debt; amount-affecting; pre-existing; explicitly-deferred

## BUG-0384 — Form 5695 Part II costs are not tied to installation in 2025

- **Caught by:** the f5695 completeness review, backlog round, 2026-11-03 (M2).
- **Source:** i5695 (archived), the Part II requirement that the property be placed in service (installed) in 2025; the credit ends after 2025 (see the findings file for the quotes).
- **Symptom:** an item paid for in 2025 but installed in 2026 can be entered and credited.
- **Disposition:** T-211: state the installation requirement in the Part II cost questions.
- **Validation:** completeness claim with quotes matched; not reproduced by evaluation.
- **Tags:** source-definition-debt; amount-affecting; pre-existing; explicitly-deferred

## BUG-0385 — The short-term or long-term box is taken from records with no holding-period rules

- **Caught by:** the sales completeness review, backlog round, 2026-11-03 (M5).
- **Source:** i8949 and i1040sd holding-period rules (inherited property is long-term; the holding period of gifts and other carryover-basis property); quotes in the findings file.
- **Symptom:** a filer who sold inherited property within a year of the death can enter it as short term, taxing it at ordinary rates.
- **Disposition:** T-211: state the holding-period rules, inherited property first, in the box question.
- **Validation:** completeness claim with quotes matched; not reproduced by evaluation.
- **Tags:** source-definition-debt; amount-affecting; pre-existing; explicitly-deferred

## BUG-0386 — Low completeness and adjudication findings of the backlog round

- **Caught by:** the completeness, screen and transcription adjudications of the backlog round, 2026-11-03 (`.transcription/proposed/bklg/*.findings.md`, Low sections).
- **Symptom:** wording gaps that rarely change an amount: asset#1 (placed in service undefined), f5695#3 to #6 (structural roof parts, dual-function storage, the audit report's contents, one main home only), ltc#1 (qualified contract requirements), retirement#1 (covered by BUG-0381), s1#1 (educator expenses exclusions), sales#2 (correct proceeds above the broker figure), sales#3 (inherited basis limited by Form 8971); `household.taxpayer_work_ssn` cites the child tax credit's "you, or your spouse" sentence though it is the taxpayer's own answer; `dependent.dc_count` is labelled "One qualifying person" but is 1 for every entry; the `sales.special` "holds" reading and `f4952.unsupported` at-risk wording. From the asset, sc and scveh adjudication: `asset.s179` leaves petroleum storage facilities out of its section 179 property list (i4562 p. 2); `sc.line23` leaves out paid family and medical leave fund contributions (i1040sc p. 9); scveh worksheet lines show amounts for standard-mileage vehicles (display only).
- **Disposition:** T-211, batched with each form's next pass.
- **Tags:** source-definition-debt; low; explicitly-deferred

## BUG-0387 — Social Security Benefits Worksheet shows amounts on skipped lines 9, 11 and 15 (married filing separately, lived together)

- **Caught by:** T-159 tier 2 mutation analysis (survivor `operand.ssb.ssb.line16.line16_together.then0` is equivalent only because of this; found while writing `mutation.t2.ssb.mfs_together_skip`).
- **Source:** i1040gi p. 32, Social Security Benefits Worksheet, line 8: "Married filing separately and you lived with your spouse at any time in 2025, skip lines 8 through 15; multiply line 7 by 85% (0.85) and enter the result on line 16."
- **Symptom:** stage10.ss.mfs_together (MFS, lived together, line 7 $20,000): line 8 $0, line 9 $20,000, line 10 $0, line 11 $20,000, line 12 $0, line 13 $0, line 14 $0, line 15 $17,000, line 16 $17,000. Lines 9, 11 and 15 are skipped by the instruction but print amounts. Line 16 and line 18 (and Form 1040 line 6b) are right: line 16 takes `ssb.line16_together`.
- **Proposed fix:** for `ssb.mfs_together`, show lines 8 to 15 as blank: either `shown_when` on lines 8 to 15 (not mfs_together), or a choose to $0 on lines 9, 11 and 15. Owner of `forms/2025/ssb.yaml` to choose.
- **Proposed fix lines:** ssb.line9, ssb.line11, ssb.line15 (and possibly 8, 10, 12 to 14 for display).
- **Siblings to check:** none beyond the worksheet.
- **Regression predictions:** stage10.ss.mfs_together: lines 9, 11 and 15 blank ($0, or hidden); line 16 $17,000; line 18 $17,000; Form 1040 line 6b $17,000 (unchanged). After the fix, `operand.ssb.ssb.line16.line16_together.then0` becomes killable (line 15 is then $0) and the case-split acceptance lapses on its own.
- **Validation:** observed by running the evaluator on the corpus case. The source reading has not had a second review.
- **Tags:** display, ssb, low.

## BUG-0388 — Form 4952 line 4a reads Schedule B lines its source does not reach

- **Caught by:** the review-catalog omission check, 2026-11-03 (source-derived transcription catalog).
- **Source:** f4952 pp. 1, 3–4 (the whole form, cited by `f4952.line4a`) names no Schedule B line; the nearby text names "Form 1040 or 1040-SR, line 3a". f1040sb line 4: "Subtract line 3 from line 2. Enter the result here and on Form 1040 or 1040-SR, line 2b".
- **Symptom:** `f4952.line4a` = `sb.line2` + `sb.line6`. Under the source-chosen catalog, Schedule B is not listed in f4952's prompt, so the required-interface check fails. Separately, Schedule B line 2 is interest before the excludable savings bond interest of line 3 (Form 8815). Whether that interest belongs in line 4a is a source question not settled here.
- **Proposed fix:** proposed. Either cite the page that supports reading Schedule B (so the excerpt reaches it), or read `f1040.line2b`/`f1040.line3b` if the source supports line 4 rather than line 2.
- **Proposed fix lines:** f4952.line4a (not owned by this package).
- **Siblings to check:** f8960 lines 1 and 2 also read `sb.line2`/`sb.line6`, while i8960 names "Form 1040 or 1040-SR, line 2b" and "line 3b". The catalog reaches Schedule B there through the whole i8960 text, but the same line 2 versus line 4 question applies.
- **Regression predictions:** none until a reading is chosen.
- **Validation:** omission.json; `input_context.assess` on the dry-run prompt.
- **Tags:** review-tool; interface; catalog; open

## BUG-0389 — Form 8863 reads the student loan worksheet's dependency question

- **Caught by:** the review-catalog omission check, 2026-11-03.
- **Source:** i8863 p. 3, "Who cannot claim a credit", "1. You're claimed as a dependent on another person's tax return"; the question `sli.claimed` sits on the Student Loan Interest Deduction Worksheet (i1040gi p. 98), which no Form 8863 source names.
- **Symptom:** `f8863.eligible` reads `sli.claimed`. Under the source-chosen catalog, sli is not listed in f8863's prompt, so the required-interface check fails.
- **Proposed fix:** proposed. Ask the "claimed as a dependent" question where both credits' sources reach it (a return-level or person-level question), or cite the shared question's home from f8863.
- **Proposed fix lines:** f8863.eligible (not owned by this package).
- **Siblings to check:** none else found by the omission check.
- **Regression predictions:** no value change if the question is moved with the same wording.
- **Validation:** omission.json.
- **Tags:** review-tool; interface; catalog; open

## BUG-0390 — Transcription catalog listed every form; T-163 visibility wording

- **Caught by:** owner decision 2026-11-03 (catalog of about 450k characters; codex limit 1,048,576) and T-163.
- **Source:** none (tooling).
- **Symptom:** every transcription prompt carried every other form's lines and every collection (363k to 395k characters). The prompt called `shown_when` optional, and all three families omitted it on f8962.
- **Tool change:** `catalog_selection` (a source-chosen subset; REPORT.md); screening entries carry the full interface note; `SHOWN_WHEN_NOTE` plus a template row; `PROMPT_POLICY` is now `source-only-computation-v3`.
- **Changed form lines:** none (tool change).
- **Related tools checked:** render, class M, completeness and screen prompts are unchanged; the excerpt is byte-identical on all 61 forms.
- **Regression predictions:** the total characters of all prompts fall from 32.5M to 21.8M; person falls from 1,045,076 to 1,022,531; f4952 and f8863 fail complete input context (PENDING-1, PENDING-2).
- **Validation:** test_review_tools.py, test_input_context.py, audit_transcription (identical), check_logs.
- **Tags:** review-tool; catalog; prompt-policy; fixed

## BUG-0391 — BUG-0388 is fixed: Form 4952 line 4a and Form 8960 lines 1 and 2 read the Form 1040 lines their sources name

- **Caught by:** the review-catalog omission check (BUG-0388); the f8960 sibling found by the refresh-round package.
- **Source:** f4952 p. 3, Line 4a, "Gross income from property held for investment includes income ... from interest, ordinary dividends"; i8960 p. 7, Line 1, "Form 1040 or 1040-SR, line 2b", and Line 2, "Form 1040 or 1040-SR, line 3b".
- **Symptom:** as recorded in BUG-0388; Form 8960 lines 1 and 2 read Schedule B lines 2 and 6 the same way.
- **Fix:** `f4952.line4a` is `f1040.line2b` plus `f1040.line3b` (taxable interest after excludable savings-bond interest); `f8960.line1` copies `f1040.line2b` and `f8960.line2` copies `f1040.line3b`; `f4952.unsupported` now asks only about interest on line 1 or the carryforward and uses the source's at-risk wording (T-207).
- **Fix lines:** `f4952.line4a`, `f4952.unsupported`, `f8960.line1`, `f8960.line2`
- **Siblings checked:** `f4952.bad_dividends`, `f4952.election_checked`, `f4952.line2`, `f4952.line4c`, `f4952.line5`, `f4952.required_test`, `f8960.line10`, `f8960.line13`, `f8960.line3`, `f8960.line4a`, `f8960.line4b`, `f8960.line5b`, `f8960.line5c`, `f8960.line6`, `f8960.line7`, `f8960.line8`, `f8960.line9c` (generated by the sibling tool; the forms' reviews are rerun in the refresh round)
- **Regression predictions:** new `stage4.f4952.line4a_taxable_interest_and_dividends` (line 4a $3,500, line 8 $3,000), predicted from f4952 before evaluation; no other value changes because Form 8815 is refused, so Schedule B line 2 and line 4 agree.
- **Validation:** fixtures; citations --strict; the catalog selection names Form 1040 for both forms.
- **Tags:** interface; catalog; fixed

## BUG-0392 — BUG-0389 is fixed: Form 8863 reads the per-person dependency answer

- **Caught by:** the review-catalog omission check (BUG-0389).
- **Source:** i8863 p. 3, "1. You’re claimed as a dependent on another person’s tax return".
- **Symptom:** as recorded in BUG-0389.
- **Fix:** new `f8863.claimed_count` counts people with `person.sav_claimed`; `f8863.eligible` requires it to be zero. `person.sav_claimed` is now asked whenever education expenses were paid (its help says so); `sli.claimed` is unchanged.
- **Fix lines:** `f8863.eligible`, `f8863.claimed_count`
- **Siblings checked:** `dependent.edu_student`, `f8863.eligible`, `person.edu_student` (generated by the sibling tool; the forms' reviews are rerun in the refresh round)
- **Regression predictions:** new `stage19.f8863.claimed_person_answer` (eligible false, Form 1040 line 29 $0), predicted before evaluation; `stage19.mut.claimed_filer_llc` and two class M cases gained the answer.
- **Validation:** fixtures; the duplicate question in `sli.claimed` is recorded for retirement (T-215).
- **Tags:** interface; catalog; fixed

## BUG-0393 — BUG-0380, BUG-0381 and BUG-0369 are fixed: disaster distributions, late rollovers and the exception conditions are stated

- **Caught by:** the screen and completeness reviews of the backlog round; T-175.
- **Source:** p575 pp. 23, 34-35; p590b p. 28; i5329 p. 5.
- **Symptom:** as recorded in BUG-0380, BUG-0381 and BUG-0369.
- **Fix:** `retirement.special` names a qualified disaster recovery distribution or its repayment (Form 8915-F); `scope.other_income` names the 2025 part of one received in 2023 or 2024; `retirement.rollover` counts waived or frozen-deposit late rollovers and a first-home distribution recontributed within 120 days; `retirement.exception` states the conditions of exceptions 01 to 04.
- **Fix lines:** `retirement.special`, `retirement.rollover`, `retirement.exception`, `scope.other_income`
- **Siblings checked:** `eic.step1_resident`, `eic.step5_line2`, `f1040.line8`, `retirement.amount_a`, `retirement.has_exception`, `retirement.is_e05`, `retirement.is_e09`, `retirement.is_e19`, `retirement.is_e22`, `retirement.is_e23`, `retirement.rolled`, `retirement.taxable`, `retirement.wrong_kind`, `scope.ready` (generated by the sibling tool; the forms' reviews are rerun in the refresh round)
- **Regression predictions:** wording; no value changes; fixtures unchanged and passing.
- **Validation:** fixtures; citations --strict; screen reviews rerun.
- **Tags:** screen-gap; wording; fixed

## BUG-0394 — BUG-0382 is fixed, with the educator-expense exclusions: alimony and educator expense questions state their rules

- **Caught by:** the screen and completeness reviews of the backlog round.
- **Source:** p504 pp. 14-15; i1040gi p. 93.
- **Symptom:** as recorded in BUG-0382; `person.educator_expenses` did not exclude home schooling or nonathletic supplies.
- **Fix:** `s1.alimony_received` and `s1.alimony_paid` exclude payments the instrument designates as not alimony and same-household payments under a decree (with the one-month exception), stated as exclusions in the amounts rather than refusals; `person.educator_expenses` states the exclusions.
- **Fix lines:** `s1.alimony_received`, `s1.alimony_paid`, `person.educator_expenses`
- **Siblings checked:** `person.educator_limited`, `person.has_educator_expenses`, `s1.alimony_refused`, `s1.paid_refused` (generated by the sibling tool; the forms' reviews are rerun in the refresh round)
- **Regression predictions:** wording; no value changes.
- **Validation:** fixtures; citations --strict.
- **Tags:** source-definition-debt; wording; fixed

## BUG-0395 — BUG-0385 is fixed, with the sales lows: holding periods, correct proceeds and inherited basis are stated

- **Caught by:** the sales completeness review of the backlog round; T-207.
- **Source:** i8949 pp. 2, 6; p550 p. 82.
- **Symptom:** as recorded in BUG-0385 and BUG-0386 (sales#2, sales#3, the `sales.special` reading).
- **Fix:** `sales.box` states the holding-period rules (inherited property first, the day count, a gift's tacked period, a block bought on different dates); `sales.proceeds` takes the correct proceeds when more than reported; `sales.correct_basis` is limited by Form 8971; `sales.special` says "directly or through another entity"; the `sales.one` remedy names entity interests (35 stage3 quotations follow).
- **Fix lines:** `sales.box`, `sales.proceeds`, `sales.correct_basis`, `sales.special`, `sales.one`
- **Siblings checked:** `sales.b_difference`, `sales.bad_code`, `sales.before_adjustment`, `sales.covered`, `sales.digital`, `sales.e`, `sales.one`, `sd.line10.d`, `sd.line10.e`, `sd.line10.g`, `sd.line10.h`, `sd.line1a.d`, `sd.line1a.e`, `sd.line1a.g`, `sd.line1a.h`, `sd.line1b.d`, `sd.line1b.e`, `sd.line1b.g`, `sd.line1b.h`, `sd.line2.d`, `sd.line2.e`, `sd.line2.g`, `sd.line2.h`, `sd.line3.d`, `sd.line3.e`, `sd.line3.g`, `sd.line3.h`, `sd.line8a.d`, `sd.line8a.e`, `sd.line8a.g`, `sd.line8a.h`, `sd.line8b.d`, `sd.line8b.e`, `sd.line8b.g`, `sd.line8b.h`, `sd.line9.d`, `sd.line9.e`, `sd.line9.g`, `sd.line9.h` (generated by the sibling tool; the forms' reviews are rerun in the refresh round)
- **Regression predictions:** wording; recorded remedy text follows in stage3; no value changes.
- **Validation:** fixtures; citations --strict.
- **Tags:** source-definition-debt; wording; fixed

## BUG-0396 — BUG-0383 is fixed: qualified improvement property is defined in the class question

- **Caught by:** BUG-0383.
- **Source:** p946 p. 31.
- **Symptom:** as recorded in BUG-0383.
- **Fix:** `asset.class` states the definition and the exclusions (enlargement, elevator or escalator, internal structural framework, residential rental property), which are real property the screen refuses.
- **Fix lines:** `asset.class`
- **Siblings checked:** `asset.is_section179`, `asset.period`, `asset.qip_early` (generated by the sibling tool; the forms' reviews are rerun in the refresh round)
- **Regression predictions:** wording; no value changes.
- **Validation:** fixtures; citations --strict.
- **Tags:** source-definition-debt; wording; fixed

## BUG-0397 — BUG-0384 is fixed: Form 5695 Part II costs count when the installation is completed

- **Caught by:** BUG-0384.
- **Source:** i5695 p. 1, Costs and Termination of credits.
- **Symptom:** as recorded in BUG-0384.
- **Fix:** `f5695.part2_any` and the help of 24 Part II cost questions say a cost counts in 2025 when its original installation is completed, whenever paid, and that an item installed after 2025 does not qualify.
- **Fix lines:** `f5695.part2_any`
- **Siblings checked:** `f5695.line32`, `f5695.line32a`, `f5695.line32b`, `s3.line5b` (generated by the sibling tool; the forms' reviews are rerun in the refresh round)
- **Regression predictions:** wording; no value changes.
- **Validation:** fixtures; citations --strict.
- **Tags:** source-definition-debt; wording; fixed

## BUG-0398 — The BUG-0386 lows are fixed for asset, Form 5695, long-term care, household, dependent, Schedule C and vehicles

- **Caught by:** BUG-0386.
- **Source:** p946 p. 32; i4562 p. 2; i5695 pp. 1-3, 5; i7206 p. 2; i1040gi pp. 101, 104, 108, 110; i1040sc p. 9.
- **Symptom:** as recorded in BUG-0386.
- **Fix:** `asset.placed` defines placed in service; `asset.s179` names petroleum storage facilities; Form 5695 lines 1 to 4 and the battery cost state the roof and storage-medium limits, line 17a the one main home, line 26a the audit report contents; `ltc.payments` the qualified contract; `household.taxpayer_work_ssn` cites the Schedule 1-A SSN sentences; `dependent.dc_count` is relabelled; `sc.line23` names state fund contributions; vehicle worksheet lines are shown only for the vehicles that use them (new helper `scveh.on_auto_limits`).
- **Fix lines:** `asset.placed`, `asset.s179`, `f5695.line1`, `f5695.line2`, `f5695.line17a`, `f5695.line26a`, `ltc.payments`, `household.taxpayer_work_ssn`, `dependent.dc_count`, `sc.line23`, `scveh.on_auto_limits`
- **Siblings checked:** `asset.after179`, `asset.f26i`, `asset.is2025`, `asset.is_section179`, `asset.s179_2025`, `asset.s179_bad`, `asset.year`, `f2441.qp_count`, `f5695.line26c`, `f5695.line6a`, `f5695.sec_a_claimed`, `ltc.amount`, `s1a.line36a_senior`, `s1a.ot_ssn`, `s1a.tip_ssn`, `sc.line28`, `sc.line28_pre179`, `scveh.bonus_v`, `scveh.line10_2025`, `scveh.macrs_v`, `scveh.s179_bad` (generated by the sibling tool; the forms' reviews are rerun in the refresh round)
- **Regression predictions:** wording, cites and display; no value changes (stage14.veh.standard hides the worksheet lines).
- **Validation:** fixtures; citations --strict.
- **Tags:** low; wording; display; fixed

## BUG-0399 — BUG-0387 is fixed: Social Security Benefits Worksheet lines 8 to 15 are hidden when married filing separately and living together

- **Caught by:** BUG-0387.
- **Source:** i1040gi p. 32, line 8, "skip lines 8 through 15".
- **Symptom:** as recorded in BUG-0387.
- **Fix:** new helper `ssb.lines8_to_15`; lines 8 to 15 carry it as `shown_when`. Values are still computed, so the mutation survivor `operand.ssb.ssb.line16.line16_together.then0` stays equivalent.
- **Fix lines:** `ssb.lines8_to_15`
- **Siblings checked:** none generated (generated by the sibling tool; the forms' reviews are rerun in the refresh round)
- **Regression predictions:** stage10.ss.mfs_together hides lines 8 to 15; line 16 and line 18 $17,000 (matched).
- **Validation:** fixtures.
- **Tags:** display; low; fixed

## BUG-0400 — T-205: an asset bought with a trade-in and excepted vehicle use are refused

- **Caught by:** T-205 (BUG-0370 remainder).
- **Source:** p946 p. 17, cash-only section 179 cost and the excepted property; i4562 pp. 3-4, 14.
- **Symptom:** Form 4562 line 2 used the whole cost of property bought with a trade-in, and vehicles were not asked about excepted section 179 use.
- **Fix:** `asset.screen` refuses property acquired with a trade-in (as `scveh.screen` already did); `scveh.screen` refuses a vehicle a noncorporate lessor leases to others or used by a tax-exempt organization, a governmental unit or a foreign person; the unreachable trade-in sentence left `asset.s179`. Accepted over-refusals: a trade-in where only line 2 would differ; excepted-use vehicles, though only section 179 is barred for them.
- **Fix lines:** `asset.screen`, `asset.s179`, `scveh.screen`
- **Siblings checked:** `asset.after179`, `asset.f26i`, `asset.is_section179`, `asset.s179_2025`, `asset.s179_bad`, `asset.screened`, `scveh.screened` (generated by the sibling tool; the forms' reviews are rerun in the refresh round)
- **Regression predictions:** no fixture changes (all answer the screens No).
- **Validation:** fixtures; citations --strict; screen reviews.
- **Tags:** eligibility; accepted-over-refusal; fixed

## BUG-0401 — T-101 remainder: the Form 8960 screens depend on the form being filed, and the combat pay question on Part II-A

- **Caught by:** T-101.
- **Source:** i8960 p. 1, "Attach Form 8960 ... if your MAGI is greater than the applicable threshold amount"; i1040s8812, Part II-A.
- **Symptom:** `f8960.unsupported`, `f8960.refund` and `s8812.combat_pay` refused whole returns that do not file Form 8960 or complete Part II-A.
- **Fix:** new `f8960.used` (AGI above line 14; the MAGI items are refused elsewhere) gates `f8960.line16` through `f8960.line16_figured`; `s8812.from_part_iia` and `s8812.part_iib_result` choose on `s8812.show_iia` through new figured helpers. `f8959.unsupported` stays a whole-return screen: every item it names is refused elsewhere and several enter the threshold test. Residual, unverified: a CFC or PFIC interest with no 2025 inclusion whose MAGI adjustment alone would cross the threshold.
- **Fix lines:** `f8960.used`, `f8960.line16`, `f8960.line16_figured`, `s8812.from_part_iia`, `s8812.part_iib_result`
- **Siblings checked:** `f8960.line16`, `f8960.line17`, `s8812.line27` (generated by the sibling tool; the forms' reviews are rerun in the refresh round)
- **Regression predictions:** new stage5 cases (Form 8960 unused with each screen Yes; combat pay with no children) keep every Form 1040 value; four stage4 refusal cases raised to $250,000 of wages stay refusals; `stage8.single.filer_is_dependent` line 28 is $0 with line 24 still refused; one refusal-reach exception recorded.
- **Validation:** fixtures; refusal reach; mutation.
- **Tags:** over-refusal; refusal-gate; fixed

## BUG-0402 — Low completeness and screen findings of the refresh round

- **Caught by:** the completeness reviews of 49 forms (33 reviewed for the first time, the T-094 burn-down) and the reruns of seven screens, refresh round, 2026-11-03.
- **Source:** the quotes listed per claim in `research/audits/refresh/BUG-0402_lows.md` (each matched against the archive).
- **Symptom:** 20 completeness gaps and 6 screen points that rarely change an amount, among them the conditions of retirement exceptions 09, 19 and the reservist exception (retirement#4, nearest to medium; the dollar caps are applied) and a territorial Form W-2 whose box 2 holds territorial tax but would be credited as federal withholding (w2#2, rare).
- **Disposition:** T-222, with each form's next pass.
- **Validation:** completeness and screen rulings carry `BUG-0402`; not reproduced by evaluation.
- **Tags:** source-definition-debt; low; explicitly-deferred

## BUG-0403 — Pub. 946 three-column pages were read across the columns

- **Caught by:** T-040.
- **Source:** tools/extract_text.py gutters(): the column gutters on Pub. 946 pp. 98, 109 and 110 are about 4 points wide, under the 8-point minimum.
- **Symptom:** those pages (and p550 pp. 110-111, p970 p. 72, i1099r p. 18) read across the columns, so the prose ran together.
- **Tool change:** a page with no normal-width gutter is checked for narrow ones (at least 3 points, crossed by at most 2% of body lines), kept only when every gutter is narrow and the page then reads as prose; extractor version 0.11. The archived text is not regenerated: re-extracting p946, p550 and p970 would stale 83 review logs pinned to their text, so the improved extraction lands when those documents are next fetched, and the three p946 exceptions stay.
- **Validation:** re-extraction of all 2024 to 2026 archives changes only the named pages; the HTML check on p946 goes from 17 to 14 failing pages; a synthetic self-test case fails with the fix disabled.
- **Tags:** extraction; tool change

## BUG-0404 — The Premium Tax Credit table extractor read the archive directly, unseen by the archive self-test

- **Caught by:** T-152 audit (T-189).
- **Source:** tools/extract_ptc_tables.py read sources/2025 through its own path constant; tools/archive_text.py's self-test only caught literal paths.
- **Symptom:** a reader that bypassed the draft and revision handling of archive_text; latent, because i8962 is not a draft.
- **Tool change:** the extractor reads through archive_text.read; the self-test also flags any name assigned to a path built through "sources".
- **Validation:** the planted case and the old file are flagged; the rewritten tables are byte-identical.
- **Tags:** tooling; archive; tool change

## BUG-0405 — check-all with a year ran four steps on 2025 regardless

- **Caught by:** T-152 audit (T-188).
- **Source:** tools/check_all_steps.sh did not forward "$@" to check_ptc_tables, siblings_check, refusal_reach and classm_job_seeds; test_classm_jobs.mjs passed no year.
- **Symptom:** a run for another year would have checked those four steps against 2025.
- **Tool change:** "$@" forwarded and YEAR_ARGS passed; the year-specific extractors, PARTS and page tables now stop on a year other than 2025, and the engine adapters read their 2025 amounts from canonical params.
- **Validation:** the steps run with --year 2025; the extractors exit 1 with --year 2026; the engine differential inputs and outputs are byte-identical before and after.
- **Tags:** year-adoption; tool change

## BUG-0406 — The limits-check sentence split stopped at abbreviations such as "U.S."

- **Caught by:** T-152 audit (T-198).
- **Source:** tools/check_limits.py and tools/year_diff.py split sentences on every period.
- **Symptom:** the i1116 p. 25 Line 24 limit sentence was stored cut off at "allocated amount of U.S.".
- **Tool change:** new citations.split_sentences does not end a sentence after Pub, Rev, Proc, Rul, Reg(s), Treas, Ch, U.S, e.g, i.e or vs, and after No, Nos, p, pp, Fig or Sec only before a number; both checks use it. The one moved key is remapped in reviews/2025/limits.json.
- **Validation:** self-tests; check_limits 0 new, 0 stale.
- **Tags:** source-coverage; tool change

## BUG-0407 — Review excerpts dropped pages after "and" and misattributed hyphenated document ids

- **Caught by:** T-195, the locator-equivalence sweep of the line-scoped review package, 2026-11-04.
- **Source:** `tools/transcription/transcribe.py` `locator_pages` and `secondary_pages` used their own locator grammar instead of `tools/citations.py`'s.
- **Symptom:** pages named after "and" ("pp. 17 and 19") were never sent to reviewers, and pages of documents with hyphenated ids (fs-2025-01, fr-2025-24154) were attributed to the citing document: Form 5695's reviews lacked fs-2025-01 pp. 5, 11, 12 and 16, retirement's lacked f1099r p. 9, and carloan's were sent i1040gi p. 23. Four transcription and nine render prompts change.
- **Tool change:** both use `citations.PAGES_RE` and `citations.page_list`. The affected forms get the corrected pages at their next content change (prompt changes apply prospectively); `--from-response` replay of their saved receipts now refuses.
- **Validation:** all-forms excerpt and prompt-hash diff; `LocatorPages` tests.
- **Tags:** review-tools; excerpt; tool change

## BUG-0408 — The refresh-round lows (BUG-0402) fixed in round 2

- **Caught by:** BUG-0402 (refresh round completeness and screen reviews, 2026-11-03); T-222.
- **Source:** the quotes listed per claim in `research/audits/refresh/BUG-0402_lows.md`, read again on the pages each fix cites: p590b pp. 6, 28; p575 pp. 21, 35; i8606 p. 9; i1040gi pp. 36, 93, 98-99, 102, 106, 117; i8889 pp. 3-4; p550 pp. 82, 86; i8949 pp. 2, 5, 7; i1040sd p. 11; f4952 p. 3; i8960 pp. 9, 13; iw2w3 p. 17; p504 p. 14; i1040sc pp. 9, 15; p463 pp. 25-26; i4562 pp. 9, 16; p946 pp. 33-34.
- **Symptom:** as listed in BUG-0402: questions and screens that left out a source condition (retirement exceptions 09, 19 and the reservist exception; territorial Form W-2 box 2; holding-period and basis rules on Form 8949; conversions of leased vehicles; and others), and display conditions missing on the SEP and social security worksheets.
- **Fix:** each question or screen states the source rule (no new input); a repayment of a qualified reservist distribution and Schedule J averaging are refused through `scope.other_income` and `scope.other_line16`; a leased vehicle converted to or from personal use on actual expenses is refused through the lease screen; Form 4562 Part V column (i) prints the capped section 179 amount; new display helpers `person.sep_shown` and `ssb.past7`, `ssb.past9`, `ssb.show8_9`, `ssb.show10_15`, `ssb.show16_18`. s179#5 is not a defect: i4562 p. 5 line 10 has no condition, and p. 3 reports a carryover attributable to qualified section 179 real property on line 13.
- **Fix lines:** `retirement.exception`, `retirement.rollover`, `retirement.special`, `scope.other_income`, `scope.other_line16`, `f8889.line2`, `f8889.rollover`, `sales.box`, `sales.correct_basis`, `sales.special`, `f4952.line1`, `f8960.unsupported`, `scveh.miles_commuting`, `scveh.lease_smr_before`, `scveh.lease_smr_bad`, `scveh.lease_business`, `scveh.s179_elect`, `scveh.s179_2025`, `sc.line24a`, `asset.class`, `asset.placed`, `asset.screen`, `w2.box2`, `otjob.statement`, `tipjob.qualified`, `s3.line10`, `s1.alimony_received`, `s1.alimony_paid`, `sli.interest`, `person.educator_expenses`, `person.sep_shown`, `ssb.past7`, `ssb.past9`, `ssb.show8_9`, `ssb.show10_15`, `ssb.show16_18`
- **Siblings checked:** `asset.is2025`, `asset.is_section179`, `asset.period`, `asset.qip_early`, `asset.screened`, `asset.year`, `eic.step1_resident`, `eic.step2_other`, `eic.step5_line2`, `f1040.line16`, `f1040.line8`, `f4952.exception`, `f4952.line3`, `f4952.used`, `f8889.any`, `f8889.excess_own`, `f8889.line13_figured`, `f8889.line14b`, `f8889.rollover_bad`, `f8960.line1`, `f8960.line10`, `f8960.line13`, `f8960.line3`, `f8960.line4a`, `f8960.line4b`, `f8960.line5b`, `f8960.line5c`, `f8960.line6`, `f8960.line7`, `f8960.line9c`, `otjob.by_half`, `otjob.by_quarter`, `otjob.by_third`, `otjob.figured`, `person.box2`, `person.educator_limited`, `person.has_educator_expenses`, `person.ira_se_plan`, `person.plan_deduction`, `person.plan_screened`, `person.sav_simple_plan`, `retirement.amount_a`, `retirement.has_exception`, `retirement.is_e05`, `retirement.is_e09`, `retirement.is_e19`, `retirement.is_e22`, `retirement.is_e23`, `retirement.rolled`, `retirement.taxable`, `retirement.wrong_kind`, `s1.alimony_refused`, `s1.paid_refused`, `s3.line15`, `sales.b_difference`, `sales.bad_code`, `sales.covered`, `sales.digital`, `sales.e`, `sales.one`, `sc.f29_veh`, `sc.line28`, `sc.line28_pre179`, `scope.ready`, `scveh.cm_c`, `scveh.lease_business`, `scveh.lease_smr_bad`, `scveh.no_miles`, `scveh.s179_2025_ok`, `scveh.s179_bad`, `sd.line10.d`, `sd.line10.e`, `sd.line10.g`, `sd.line10.h`, `sd.line1a.d`, `sd.line1a.e`, `sd.line1a.g`, `sd.line1a.h`, `sd.line1b.d`, `sd.line1b.e`, `sd.line1b.g`, `sd.line1b.h`, `sd.line2.d`, `sd.line2.e`, `sd.line2.g`, `sd.line2.h`, `sd.line3.d`, `sd.line3.e`, `sd.line3.g`, `sd.line3.h`, `sd.line8a.d`, `sd.line8a.e`, `sd.line8a.g`, `sd.line8a.h`, `sd.line8b.d`, `sd.line8b.e`, `sd.line8b.g`, `sd.line8b.h`, `sd.line9.d`, `sd.line9.e`, `sd.line9.g`, `sd.line9.h`, `sli.has`, `sli.line1`, `ssb.show10_15`, `ssb.show16_18`, `ssb.show8_9`, `tipjob.mixed` (generated by the sibling tool; no change was needed in any; their forms' reviews were rerun in round 2, f1040 and f8863 on these lines alone)
- **Regression predictions:** new fixtures `stage14.veh.2025_179_over_line9`, `stage10.ss.stop_line9`, `stage10.ss.stop_line7`, `stage10.ss.shown_all`, `stage10.ss.mfs_together_shown`, `stage14.sep.worksheet_shown`, `stage14.sep.worksheet_hidden`, each written from the source before evaluating; `stage14.veh.refuse_lease_smr_before` carries the new refusal text; no other expected value changes.
- **Validation:** fixtures; citations --strict; screen, completeness, transcription and render reviews of the changed forms (round 2).
- **Tags:** source-definition-debt; low; fixed


## BUG-0409 — A CFC or PFIC interest with nothing to include for 2025 could raise MAGI over the Form 8960 threshold unseen

- **Caught by:** T-216 (BUG-0401 residual).
- **Source:** i8960 p. 22, Line 13: "Increase AGI by the amount of any distributions described in section 959(d) or 1293(c) included in your NII as a dividend", and section 1291 excess distributions "included in MAGI but not included in gross income for regular income tax purposes".
- **Symptom:** `f8960.used` tests AGI; a holder of CFC or PFIC stock whose modified AGI exceeds the threshold through those adjustments while AGI does not got no net investment income tax (inferred from the text; no fixture demonstrates it).
- **Fix:** `scope.other_line16` refuses any stock in a CFC or PFIC, owned directly or indirectly, even with nothing to include in income for 2025; the `f8960.used` citation names the case.
- **Fix lines:** `scope.other_line16`, `f8960.used`
- **Siblings checked:** `eic.step2_other`, `f1040.line16`, `f8960.line16`, `scope.ready` (generated by the sibling tool; no change was needed in any; their forms' reviews were rerun in round 2, f1040 and f8863 on these lines alone)
- **Regression predictions:** no expected value changes (the screen's Yes path is already exercised).
- **Validation:** fixtures; citations --strict; the scope screen review.
- **Tags:** over-refusal accepted; refusal-gate; fixed


## BUG-0410 — The student loan interest worksheet asked its own copy of the dependency question

- **Caught by:** T-215.
- **Source:** i1040gi p. 98, Line 21: the deduction is not allowed if "you, or your spouse if filing jointly, can be claimed as a dependent".
- **Symptom:** `sli.claimed` and `person.sav_claimed` asked the same fact separately and could be answered inconsistently (22 of 276 fixtures disagreed), so the student loan worksheet and Forms 8863 and 8880 read different answers.
- **Fix:** `sli.claimed` is retired; `sli.claimed_count` counts the persons whose `person.sav_claimed` is Yes, and `sli.eligible` requires it to be 0. Fixtures, interview profiles and `tools/engines/generate_cases.py` follow.
- **Fix lines:** `sli.claimed_count`, `sli.eligible`, `person.sav_claimed`
- **Siblings checked:** `f8863.claimed_count`, `person.sav_ineligible`, `sli.allowed`, `sli.claimed_count`, `sli.eligible` (generated by the sibling tool; no change was needed in any; their forms' reviews were rerun in round 2, f1040 and f8863 on these lines alone)
- **Regression predictions:** `stage11.sli.spouse_claimed` (count 1, deduction $0) and `stage11.sli.none_claimed_joint` (count 0, deduction $2,497.50); migrated fixtures keep their values.
- **Validation:** fixtures; properties 9/9.
- **Tags:** input-ripple; low; fixed


## BUG-0411 — Merged review logs' line-scoped passes were not verified for second-family credit

- **Caught by:** T-226 premise check.
- **Source:** `tools/transcription/README.md` (line-scoped reviews) against `compare_families.compare` and `audit_transcription.audit`.
- **Symptom:** both read only a merged log's header; a pass made while the header subject was current would have shared the header's credit unverified. Latent: no log had passes.
- **Tool change:** `compare_families.pass_blockers` holds each pass to the header's conditions; `audit_transcription.audit_pass` checks each pass's receipt, prompt hash, reply and metadata and compares it again on the pass's scope.
- **Validation:** review-tool tests; `reports/2025/second_family.md` unchanged.
- **Tags:** review-tools; tool change


## BUG-0412 — Inputs with two taxpayer entries were accepted

- **Caught by:** mutation tier 2 (T-213): the mutant `operand.s1a.s1a.line36a_senior.line35.then1` survives only on such a return.
- **Source:** the roster has one entry for the filer and, on a joint return, one for the spouse (interview `$person`).
- **Symptom:** a return with two `person` entries of role taxpayer was refused on Form 1040 lines 1a and 15 (`household.roster_bad`) but evaluated elsewhere: `s1a.line36a` was $0, and $6,000 under the mutant.
- **Tool change:** `validateInputs` (`engine/src/eval.ts`) rejects more than one `$person` entry with role taxpayer.
- **Validation:** integration test (a second taxpayer entry is rejected; the same entry as spouse evaluates).
- **Tags:** input-validation; tool change


## BUG-0413 — Net unrealized appreciation in employer securities was taxed in the year of the distribution

- **Caught by:** round 2 completeness review of retirement (claim retirement#2), 2026-11-04.
- **Source:** p575 p. 21: "The NUA in employer securities (box 6 of Form 1099-R) received as part of a lump-sum distribution is generally tax free until you sell or exchange the securities"; i1099r p. 7, Box 6: the NUA "is taxed only when you sell the securities unless you choose to include it in your gross income this year".
- **Symptom:** `retirement.plan_simple` is box 1 less box 5 less the rollover; box 1 includes the NUA, so it was taxed on Form 1040 line 5b, and nothing asked about box 6. Read from the expression; no fixture shows it.
- **Fix:** `retirement.special` names a distribution of employer securities with net unrealized appreciation (an amount in box 6), so such a distribution is refused; the screen's citation adds p575 p. 16. Computing the deferral (box 1 less box 6 unless the filer elects to include it) would need two new inputs and is not done.
- **Fix lines:** `retirement.special`
- **Siblings checked:** `retirement.amount_a`, `retirement.rolled`, `retirement.taxable` (generated by the sibling tool; no change was needed in any; their forms' reviews were rerun in round 2, f1040 and f8863 on these lines alone)
- **Regression predictions:** no expected value changes; the screen's Yes path is exercised by `stage16.cleanup.refuse.retirement.special_first`.
- **Validation:** fixtures; the retirement.special screen review.
- **Tags:** wrong-amount; refusal-gate; medium; fixed


## BUG-0414 — Low completeness findings of round 2

- **Caught by:** the round 2 completeness reviews of 15 changed forms, 2026-11-04.
- **Source:** the quotes listed per claim in `research/audits/round2/BUG-0414_lows.md`.
- **Symptom:** 12 completeness gaps that rarely change an amount, among them the wash-sale definition (sales#4, nearest to medium) and investment-use miles of a vehicle (scveh#3).
- **Disposition:** T-229, with each form's next pass.
- **Validation:** completeness rulings carry `BUG-0414`; not reproduced by evaluation.
- **Tags:** source-definition-debt; low; explicitly-deferred

## BUG-0415 — The round-2 lows (BUG-0414) fixed in round 3

- **Caught by:** BUG-0414 (round 2 completeness reviews and the T-094 reviews, 2026-11-04); T-229.
- **Source:** the quotes listed per claim in `research/audits/round2/BUG-0414_lows.md`, read again on the pages each fix cites: p550 pp. 60-61, 81-82, 86-87; i8949 pp. 6-7, 10; i1040sd pp. 5-6, 10; f4952 p. 4; p575 pp. 16-17, 21, 24; p560 pp. 17-18; i5329 p. 2; i8889 pp. 2-4; p504 pp. 13-14; p4681 p. 5; p463 pp. 25-26; i4562 p. 14.
- **Symptom:** as listed in BUG-0414: questions that left out a source rule (holding period, basis and wash-sale rules on Form 8949; the exercised written call premium; the Form 4952 election on a timely filed return; non-eligible rollover distributions; a nonperiodic annuity payment; HSA premiums and transfers; the SIMPLE contribution deadline; third-party alimony payments; student loan repayment assistance; vehicle cost items), and a vehicle with investment use or a substantial improvement not refused.
- **Fix:** each question states the source rule (no new input); refused because the tool cannot compute them: the three partial-exclusion nonperiodic payments and the recontribution of a wrongfully levied amount (`retirement.special`), and a vehicle with 2025 investment use or a substantial improvement (`scveh.screen`).
- **Fix lines:** `sales.box`, `sales.code`, `sales.proceeds`, `sales.correct_basis`, `sales.wash_loss`, `f4952.line4g`, `retirement.annuity`, `retirement.special`, `retirement.rollover`, `f8889.medical`, `f8889.line2`, `f8889.line14a`, `person.simple_employer`, `s1.alimony_received`, `s1.alimony_paid`, `sli.interest`, `scveh.cost`, `scveh.screen`
- **Siblings checked:** `f4952.bad_election`, `f4952.election_checked`, `f4952.has_election`, `f8889.any`, `f8889.excess_own`, `f8889.has_dist`, `f8889.line13_figured`, `f8889.line14c`, `f8889.line15`, `f8889.rollover_bad`, `person.simple_deduction`, `person.simple_excess`, `retirement.amount_a`, `retirement.annuity_rollover`, `retirement.annuity_with_cost`, `retirement.plan_taxable`, `retirement.rolled`, `retirement.show_a`, `retirement.taxable`, `s1.alimony_refused`, `s1.paid_refused`, `sales.b_difference`, `sales.bad_aggregate`, `sales.bad_code`, `sales.before_adjustment`, `sales.covered`, `sales.digital`, `sales.e`, `sales.has_b`, `sales.has_w`, `sales.w`, `sales.wash_bad`, `sales.wash_over`, `scveh.b100`, `scveh.bus_cost`, `scveh.screened`, `scveh.unrecovered`, `sd.line10.d`, `sd.line10.e`, `sd.line10.g`, `sd.line10.h`, `sd.line1a.d`, `sd.line1a.e`, `sd.line1a.g`, `sd.line1a.h`, `sd.line1b.d`, `sd.line1b.e`, `sd.line1b.g`, `sd.line1b.h`, `sd.line2.d`, `sd.line2.e`, `sd.line2.g`, `sd.line2.h`, `sd.line3.d`, `sd.line3.e`, `sd.line3.g`, `sd.line3.h`, `sd.line8a.d`, `sd.line8a.e`, `sd.line8a.g`, `sd.line8a.h`, `sd.line8b.d`, `sd.line8b.e`, `sd.line8b.g`, `sd.line8b.h`, `sd.line9.d`, `sd.line9.e`, `sd.line9.g`, `sd.line9.h`, `sli.has`, `sli.line1` (generated by the sibling tool; no change was needed in any but `f8889.line14a`, changed with `f8889.line2`; their forms' reviews were rerun in round 3)
- **Regression predictions:** no expected value changes (question text and screen items only).
- **Validation:** fixtures; citations --strict; transcription, render, completeness and screen reviews of the changed forms (round 3).
- **Tags:** source-definition-debt; low; fixed

## BUG-0416 — Round 3's own low findings fixed: short sales, inherited basis, the late Form 4952 election

- **Caught by:** the round 3 completeness review of sales (sales#3, #4, #5) and DeepSeek render review of f4952, 2026-11-04.
- **Source:** i1040sd p. 6, "your gain when closing a short sale is short term if you (a) held substantially identical property for 1 year or less on the date of the short sale, or (b) acquired property substantially identical to the property sold short after the short sale but on or before the date you close the short sale"; p550 p. 87, "The wash sale rules apply to a loss realized on a short sale if you sell, or enter into another short sale of, substantially identical stock or securities within a period beginning 30 days before the date the short sale is complete and ending 30 days after that date"; p550 pp. 59-61, 86 (inherited, traded, spousal, compensatory and short-sale in-lieu basis); f4952 p. 4, "if you timely filed your return without making the election, you can make the election on an amended return filed within 6 months of the due date of your return (excluding extensions)".
- **Symptom:** the round-3 wording of these questions left out the short-sale gain rule and the year a short sale is reported, the wash-sale rule for short sales, several basis rules, and the late election on an amended return.
- **Fix:** each question states the rule (no new input, no expression change).
- **Fix lines:** `sales.box`, `sales.wash_loss`, `sales.correct_basis`, `f4952.line4g`
- **Siblings checked:** `f4952.bad_election`, `f4952.election_checked`, `f4952.has_election`, `sales.b_difference`, `sales.bad_code`, `sales.covered`, `sales.digital`, `sales.e`, `sales.w`, `sales.wash_bad`, `sales.wash_over`, `sd.line10.d`, `sd.line10.e`, `sd.line10.g`, `sd.line10.h`, `sd.line1a.d`, `sd.line1a.e`, `sd.line1a.g`, `sd.line1a.h`, `sd.line1b.d`, `sd.line1b.e`, `sd.line1b.g`, `sd.line1b.h`, `sd.line2.d`, `sd.line2.e`, `sd.line2.g`, `sd.line2.h`, `sd.line3.d`, `sd.line3.e`, `sd.line3.g`, `sd.line3.h`, `sd.line8a.d`, `sd.line8a.e`, `sd.line8a.g`, `sd.line8a.h`, `sd.line8b.d`, `sd.line8b.e`, `sd.line8b.g`, `sd.line8b.h`, `sd.line9.d`, `sd.line9.e`, `sd.line9.g`, `sd.line9.h` (generated by the sibling tool; no change was needed in any; their forms' reviews were rerun after the fix)
- **Regression predictions:** no expected value changes (question text only).
- **Validation:** fixtures; citations --strict; the line-scoped transcription and render reviews and the completeness reviews of sales and f4952 after the fix.
- **Tags:** source-definition-debt; low; fixed

## BUG-0417 — Low completeness findings of round 3

- **Caught by:** the completeness review of sales after BUG-0416, 2026-11-04.
- **Source:** p550 p. 88; i1040sd p. 6 (listed per claim in `research/audits/round3/BUG-0417_lows.md`).
- **Symptom:** two rare holding-period and wash-sale details of Pub. 550 that `sales.box` and `sales.wash_loss` do not state: written and expired options, securities futures and demutualized stock (sales#2), and the 6-month window for REMIC residual interests (sales#4).
- **Disposition:** T-233, with the next sales pass.
- **Validation:** completeness rulings carry `BUG-0417`; not reproduced by evaluation.
- **Tags:** source-definition-debt; low; explicitly-deferred

## BUG-0418 — The round-3 sales lows (BUG-0417) and the last sales review findings fixed

- **Caught by:** BUG-0417 (T-233) and the sales completeness and `sales.special` screen reviews that followed each fix, 2026-11-04.
- **Source:** p550 p. 88, "If you are not in the business of writing options and an option you write on stocks, securities, commodities, or commodity futures is not exercised (or repurchased), the amount you receive is a short-term capital gain.", "you are considered to have sold or traded the option on the date it expired", "Any capital gain or loss on a sale, exchange, or termination of a contract to sell property will be considered short term, regardless of how long you hold the contract." and the REMIC residual interest 6-month window; p550 p. 87, securities futures contracts to sell; i1040sd p. 6, demutualization; p550 p. 86, payments in lieu of dividends (extraordinary dividends, the holding-period exclusion and the collateral-income offset); i1040sd p. 12, "the depreciation allowed or allowable"; i1040sd p. 10, Disposal of QOF Investment.
- **Symptom:** `sales.box` lacked the written and expired option, contract-to-sell and demutualization holding periods; `sales.wash_loss` the REMIC window; `sales.correct_basis` the limits on adding in-lieu payments to basis; `sales.special` called section 1250 property only property "that you depreciated" (missing allowable but unclaimed depreciation) and did not refuse a qualified opportunity fund disposition or deferral on the detail route, whose deferred gain would be left out.
- **Fix:** each question states the rule; `sales.special` refuses a QOF disposition or deferral.
- **Fix lines:** `sales.box`, `sales.wash_loss`, `sales.special`, `sales.correct_basis`
- **Siblings checked:** `sales.b_difference`, `sales.bad_code`, `sales.covered`, `sales.digital`, `sales.e`, `sales.one`, `sales.w`, `sales.wash_bad`, `sales.wash_over`, `sd.line10.d`, `sd.line10.e`, `sd.line10.g`, `sd.line10.h`, `sd.line1a.d`, `sd.line1a.e`, `sd.line1a.g`, `sd.line1a.h`, `sd.line1b.d`, `sd.line1b.e`, `sd.line1b.g`, `sd.line1b.h`, `sd.line2.d`, `sd.line2.e`, `sd.line2.g`, `sd.line2.h`, `sd.line3.d`, `sd.line3.e`, `sd.line3.g`, `sd.line3.h`, `sd.line8a.d`, `sd.line8a.e`, `sd.line8a.g`, `sd.line8a.h`, `sd.line8b.d`, `sd.line8b.e`, `sd.line8b.g`, `sd.line8b.h`, `sd.line9.d`, `sd.line9.e`, `sd.line9.g`, `sd.line9.h` (generated by the sibling tool; no change was needed in any; their forms' reviews were rerun after the fix)
- **Regression predictions:** no expected value changes (question text and a screen item; the screen's Yes path is already exercised).
- **Validation:** fixtures; citations --strict; the line-scoped sales transcription and render reviews, the sales completeness review (converged: every claim refused elsewhere) and the `sales.special` screen review (WIDE only).
- **Tags:** source-definition-debt; refusal-gate; low; fixed

## BUG-0419 — A federal render wrote the New York documents into the federal folder

- **Caught by:** the owner's machine, New York integration, 2026-11-04.
- **Source:** none (a tool defect).
- **Symptom:** on the New York branch, `render` (federal) added `ny_*.md` to `rendered/2025/` and changed `params.md`, `ambiguities.md` and `index.md`, because the loader merges the New York canonical files.
- **Tool change:** `engine/src/render.ts` renders only its own jurisdiction's documents, tables, parameters and register; `render --ny` writes to `rendered/ny/2025/`.
- **Validation:** a federal render leaves `rendered/2025/` byte-identical to the committed tree.
- **Tags:** review-tools; jurisdiction; tool change

## BUG-0420 — check_logs crashed on the New York canonical files

- **Caught by:** the owner's machine, New York integration, 2026-11-04.
- **Source:** none (a tool defect).
- **Symptom:** `tools/transcription/check_logs.py` raised `FileNotFoundError: forms/2025/ny_city_rs.yaml` in `tools/human_review/reading.py` `Canon`, which read `forms/2025/<id>.yaml` for every canonical file.
- **Tool change:** `Canon` skips New York documents.
- **Validation:** federal `check_logs` output identical to main's.
- **Tags:** review-tools; jurisdiction; tool change

## BUG-0421 — Class M jobs for one New York document built no case

- **Caught by:** New York review tooling package, 2026-11-04.
- **Source:** none (a tool defect).
- **Symptom:** `classm-jobs --ny --docs <one document>` built 0 jobs: the corpus was seeded from the federal fixtures only.
- **Tool change:** with `--ny`, every New York fixture seeds the corpus (`engine/src/classm.ts`).
- **Validation:** `--docs ny_it2` builds 1 job; `test_classm_jobs.mjs` passes.
- **Tags:** class-m; jurisdiction; tool change

## BUG-0422 — A mutant could change a different document's line of the same id

- **Caught by:** New York mutation package, 2026-11-04 (the federal run crashed on `floor.se.line9`).
- **Source:** none (a tool defect).
- **Symptom:** each mutant's `apply` looked its line up by id across all forms and definitions; definition-local ids repeat (`line9` in `ny_tcw` and the federal `se`, `single.b1.excess` in `ny_rs` and `ny_city_rs`), so a mutant could change the wrong line. On main ids were unique, so no federal result was affected.
- **Tool change:** `mutations()` looks the line up in its own document; the federal run takes only federal mutants and `mutate --ny` only New York mutants (a separate check-all step).
- **Validation:** the federal mutation run is unchanged (5,124 mutants, 287 surviving, all explained); the New York run 718 mutants, all survivors explained.
- **Tags:** mutation; tool change

## BUG-0423 — IT-201 line 54b showed $0 when the MCTMT is refused

- **Caught by:** New York mutation package (the last unexplained survivor, `operand.ny_it201.ny_it201.line54d.line54b`), 2026-11-04.
- **Source:** ny_it201i p. 15, Lines 54a through 54e, "Zone 2- Enter the amount of net earnings from self-employment allocated to Zone 2 for the tax year on line 54b."
- **Symptom:** with the MCTMT screen Yes, line 54a refused but line 54b (and so line 54d) showed $0; totals were unaffected because line 54e and line 58 carry the refusal.
- **Fix:** `ny_it201.line54b` is refused with line 54a under `ny_it201.gate.mctmt`; `ny.refuse.mctmt` asserts the refusal on lines 54b and 54d.
- **Fix lines:** `ny_it201.line54b`
- **Siblings checked:** `ny_it201.line54a` (generated by the sibling tool; no change was needed in any)
- **Regression predictions:** `ny.refuse.mctmt` gains refusals on lines 54b and 54d; no amount changes.
- **Validation:** `test-fixtures --ny`; the New York mutation run.
- **Tags:** refusal-gate; new-york; low; fixed

## BUG-0424 — Low findings of the first New York reviews

- **Caught by:** the first completeness, transcription, render and class M reviews of the New York documents, 2026-11-04.
- **Source:** the quotes listed per claim in `research/audits/ny/BUG-0424_lows.md`.
- **Symptom:** rare gaps outside the pilot profile (a spouse who cannot sign a joint return, a Form W-2c, foreign income without a Form W-2), a citation on the City table note, and three review-tool gaps (render and class M prompts lack the whole-dollar rule their lines link; class M chooses a worksheet independently of the filing status).
- **Disposition:** T-244, with the New York forms' and review tools' next change.
- **Validation:** rulings carry `BUG-0424`; not reproduced by evaluation.
- **Tags:** new-york; source-definition-debt; review-tools; low; explicitly-deferred

## BUG-0425 — The New York build walked class M and mutation fixtures through the interview

- **Caught by:** the owner's machine, New York class M round, 2026-11-04 (every class M run failed at its rebuild).
- **Source:** none (a tool defect).
- **Symptom:** the build walked every New York fixture file through the interview, including class M cases, which keep only the answers their route reads (so `classm.ny_it2.1` failed on `person[spouse].work_ssn`), and the mutation cases, whose 64-dependent returns took the build past ten minutes; a fixed 600-step cap also stopped those paths.
- **Tool change:** as federally, the New York walk covers the hand-authored stage fixtures only (`engine/src/build.ts`), and a path's step bound is the fixture's input count plus one, exact because each step answers a distinct input (`engine/src/interview-check.ts`).
- **Validation:** build OK in about 2.5 minutes; `test-fixtures --ny` passes.
- **Tags:** interview; jurisdiction; tool change

## BUG-0426 — Background check-all runs compared HEAD-relative checks with the snapshot itself

- **Caught by:** T-238 implementation agent, reading `tools/check_all_bg.sh`; confirmed by a probe, 2026-11-05.
- **Source:** `tools/check_bug_inventory.py` ("The committed content (git HEAD) must be a byte-for-byte prefix of the working file") against `tools/check_all_bg.sh` `prepare()`.
- **Symptom:** the background runner checked the snapshot out with HEAD at the snapshot commit, so `git show HEAD:BUG_INVENTORY.md` equalled the working file and the append-only check could not fail; `siblings.py` and `human_review/logs.py`, which also read HEAD, saw no uncommitted change. A probe snapshot that edited BUG-0001's heading passed (425 entries, append-only). Latent: all 71 committed changes to BUG_INVENTORY.md are pure appends.
- **Why the checks missed it:** the foreground run (`tools/check_all.sh`) has HEAD at the real commit; the background runner was tested for tree identity, not for what HEAD-relative steps see.
- **Tool change:** `prepare` takes the base and resets HEAD to it softly after the checkout, so the snapshot's changes are uncommitted against the commit it was taken on.
- **Validation:** the same probe fails with the fix ("committed content was modified"); the full background run of this change.
- **Tags:** commit-guard; tool change

## BUG-0427 — A choose stopped at an unknown guard hid a refusal on every way

- **Caught by:** New York integration check-all (properties with the New York documents in scope), 2026-11-05; T-245.
- **Source:** spec 4.7.3 (choose) and the property refusal_outranks_unknown ("an unknown operand does not hide a refused one").
- **Symptom:** with the filing status unanswered and New York taxable income refused, ny_it201.tax_schedule, city_tax_schedule, tcw.w1/w7/w12 and ny_tcw line 3 were unknown though every status's schedule is that refusal; federally eic.limit and eic.line5_threshold behaved the same. No wrong number; the refusal surfaced later in the interview.
- **Root cause:** choose (eval.ts and Eval.lean) returned the first unknown or refused guard without evaluating the other alternatives, so refusal versus unknown depended on guard order.
- **Why it survived:** properties ran on federal-only data, and federal tax_on_amount tests the amount before the status; no New York return generator existed; Lean shares the semantics, so compare agreed; at the choose itself no refused operand was recorded, only one level up at a copy(instance) binding.
- **Tool change:** past the first unknown guard, every alternative still possible is evaluated; the line is a refusal when every way refuses (the first way's refusal), else the guard's unknown with the memo undone. Both evaluators; spec 4.7.3 rewritten; properties --ny added (check-all step ny_properties).
- **Regression predictions:** fixtures ny.reg.choose.status_unanswered_refused_income and stage21.choose.eic_limit_status_unanswered fail on the old engine; unasserted values in 231 federal fixture cases move from unknown to refusal; no recorded expectation changes; Lean compare agrees.
- **Validation:** test-fixtures 1638/1638 and --ny 332/332; properties and properties --ny clean; compare 0 differing (2,238 and 932 cases); mutation kills unchanged.
- **Tags:** engine; lean; refusal; new-york; tool change

## BUG-0428 — Mutation path dominance trusted refusalsSame past guard reads

- **Caught by:** independent review of the T-245 mutation rules, 2026-11-05 (synthetic counterexample).
- **Source:** engine/src/mutate.ts dominatedBy against spec 4.7.3.
- **Symptom:** a step's fact counted when hidden or refusalsSame, but refusalsSame held only for the start line; a downstream guard reading a helper could turn a value difference into a refusal difference. Synthetic form t: mutant operand.t.t.H.gated was accepted as Guarded figure while base t.Rd is unknown and the mutant's a refusal with t.f unanswered. Latent: no current equivalent relied on it.
- **Tool change:** refusalsSame applies only along refusal-transparent steps (ungated copy, round, sum, subtract, subtract_floor0, smaller_of, larger_of, multiply_rate, multiply_count, prorate, or a choose taking the line as an alternative); a def-instance binding fails closed; guardedFigureSelfTest rejects the counterexample, with a control.
- **Validation:** mutate and mutate --ny: kills and classifications unchanged; self-tests clean.
- **Tags:** mutation; tool change

## BUG-0429 — Seven pinned equivalence arguments were counted as proven on every input

- **Caught by:** independent review of the T-245 mutation rules, 2026-11-05 (fuzz over all 287 equivalents, 171,817 partial returns).
- **Source:** the arguments' own text, which scopes them to answered inputs, against reports/2025/mutation.md ("provably equivalent").
- **Symptom:** f2441.attrib_gate (operand ... line31.all.3.gt.0) is killed with f2441.benefits and f1040.status unanswered (base refusal f2441.student_disabled, mutant unknown); sc.qbi_se, sdtw.line4, dependent.dc_line2c, roster_ok, eic.step5_income and s8812.line18a carry the same caveat. The report counted all seven as equivalent.
- **Tool change:** the report lists them as equivalent on answered inputs only and gives the score both ways (99.9% on every input, 100.0% with them); killing or re-arguing them is T-250.
- **Tags:** mutation; report; tool change

## BUG-0430 — all and any refuse eagerly on incomplete returns

- **Caught by:** T-245 completion-soundness probe, 2026-11-05.
- **Source:** spec 4.7.2 (a conjunct that is a refusal ends the test, after an earlier unknown conjunct).
- **Symptom:** a partial return shows a refusal that answering the unknown conjunct could clear: over 400 federal partial returns, 741 line values are a refusal on the partial return and a value on the full one. Mid-interview only; complete returns are unaffected.
- **Disposition:** open: T-248 (fix under the T-245 rule, or label refusals on incomplete returns as provisional in the T-236 UI).
- **Tags:** engine; refusal; open

## BUG-0431 — check-all in an agent worktree regenerates reports from partial review data

- **Caught by:** T-254 item 1 and the T-236 design agents, 2026-11-06.
- **Symptom:** A linked worktree has only part of the git-ignored review data (.transcription/: 15 entries against 1430 in the main checkout), so tools/check_all.sh run there regenerates reports/2025/second_family.md from partial data and still reports green; one agent committed the wrong report (35d04c3, not merged).
- **Disposition:** open: check-all should refuse when the review data is incomplete, or the worktree setup should clone it in.
- **Tags:** tooling; worktree; open

## BUG-0432 — the social-security interview profile fails to start

- **Caught by:** T-254 item 1 agent, 2026-11-06.
- **Symptom:** interview start --profile social-security fails on a fresh build with: no question for reachable input f8962.alloc (also on the code before T-254).
- **Disposition:** open.
- **Tags:** interview; open

## BUG-0433 — scope.other_line16 omits the IRS examples of unearned income in its Form 8615 condition

- **Caught by:** R0 screen review of scope.other_line16 (finding 2, UNCLEAR), 2026-11-06.
- **Symptom:** The Form 8615 condition says only "more than $2,700 of unearned income"; i1040gi p. 36 says "(such as taxable interest, ordinary dividends, or capital gains (including capital gain distributions))". A child whose unearned income is mostly capital gains or capital gain distributions may read unearned income as interest and dividends only, answer no, and get no Form 8615 tax on line 16. The wording predates R0 (R0 kept it word for word).
- **Disposition:** open; low. Fix by adding the IRS examples to the condition, a content change outside R0's no-new-clauses rule, with the screen review rerun.
- **Tags:** screen wording; open

## BUG-0434 — The Part I cost questions do not say the home must be one you lived in during 2025

- **Caught by:** R1 completeness review of f5695 (claim 1), 2026-11-07.
- **Symptom:** i5695 p. 1, Home: "A home is where you lived in 2025 and can include a house, houseboat, mobile home, cooperative apartment, condominium, and a manufactured home that conforms to Federal Manufactured Home Construction and Safety Standards." f5695.part1_any and the Part I cost questions (f5695.line1 to line4, f5695.battery_cost) ask about property "for a home in the United States (it need not be your main home)" and never say the filer must have lived there in 2025, or that a manufactured home must conform to the federal standards. A home that is rented out is refused by f5695.business_use (more than 20% of an item's use for renting out); a home neither lived in nor rented in 2025 (for example a second home first used after 2025, other than a home under construction, which f5695.construction_later handles) can be entered and credited. The wording predates R1 (R1 kept it word for word).
- **Disposition:** open; low. Fix by adding the lived-in-2025 condition (and the manufactured-home standard) to f5695.part1_any, a content change outside R1's no-new-clauses rule, with the completeness and render reviews rerun.
- **Tags:** source-definition-debt; low; pre-existing; open

## BUG-0435 — retirement.rollover does not exclude a rollover into a SIMPLE IRA in its first 2 years

- **Caught by:** R2 completeness review of retirement (claim 2), 2026-11-07.
- **Symptom:** p575 p. 21, Rollovers to SIMPLE retirement accounts: "During the first 2 years of participation in a SIMPLE retirement account, you may roll over amounts from one SIMPLE retirement account into another SIMPLE retirement account." The rollover question counts any amount rolled over to "an IRA other than a Roth IRA" and limits only code S distributions out of a SIMPLE IRA, so a plan or non-SIMPLE IRA distribution rolled into a SIMPLE IRA in its first 2 years would be excluded though it stays taxable. The wording predates R2 (R2 kept it word for word).
- **Disposition:** open; low. Fix at the form's next substantive change by excluding that case from the question (or refusing it), a content change outside R2's no-new-clauses rule, with the completeness and render reviews rerun.
- **Tags:** retirement; question wording; open

## BUG-0436 — sales.code does not name the nominee or personal-use loss adjustments

- **Caught by:** the sales completeness review rerun after the R3 restructuring, 2026-11-07 (sales#1).
- **Source:** i8949 p. 3 ("Loss on the sale of personal property is not deductible ... you should report the loss with an offsetting entry ... on Form 8949, by entering an adjustment"); i8949 p. 9 (a Form 1099-B, 1099-DA or 1099-S received as a nominee for the actual owner: report the transaction and enter the resulting gain or loss as an offsetting adjustment in column (g)).
- **Symptom:** the adjustment-code question (Adjustment codes: none, B, W, BW; choose other for any additional code, such as code E ...) names only code E as an example, so a filer who received a broker or payment report as a nominee, or who sold personal-use property at a loss, can answer none; the tool then reports a gain or loss the source offsets to zero. A filer who answers other is refused (sales.bad_code). Pre-existing; not caused by the R3 restructuring, which did not touch sales.code.
- **Disposition:** open, low: name the nominee and personal-use-loss situations in sales.code (or ask them and refuse); rerun the sales reviews.
- **Tags:** completeness; sales; open

## BUG-0437 — Transcription request listed structured questions on one line with the structure flattened

- **Caught by:** the R2 restructuring agents, 2026-11-07.
- **Source:** tools/transcription/transcribe.py reference_note and tools/transcription/classm.py (one-line listings of other documents' input questions and labels).
- **Symptom:** The one-line interface listing in the transcription request (and the classm given/fill lists) joined each line of a structured question with a space, so bullets ran on as ' - ' and nesting and full stops were lost (f8962.other, retirement.rollover). No reply misread a question; more forms were being restructured. The other review tools (render_compare, completeness_review, screen_review, gates, false_no_review) print structured text through indent_rest and were not affected.
- **Tool change:** structured_text.inline replaces flat: the question, then each further block after ' — ', a list as 'Heading: (1) item; (2) item [nested: sub; sub]'. reference_note and classm use it; plain text is returned unchanged.
- **Validation:** All 441 review prompts dry-run before and after (61 transcription requests and 62 render requests; 62 completeness, 58 screen and 198 classm prompts; no false-no gates exist): 380 byte-identical, and the 61 that differ are exactly the transcription requests (the screen-question list every request carries now holds structured questions), and each of those returns to the old bytes when every structured text's new rendering is replaced by its old flattening. Transcription, render and classm logs are judged by line subjects and foreign-interface hashes (not the prompt text), and the screen, completeness and false-no hashes are unchanged, so no check goes stale; no review was rerun.
- **Tags:** transcription; structured text; tool change
