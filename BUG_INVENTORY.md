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
