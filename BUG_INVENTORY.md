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
