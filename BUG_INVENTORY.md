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
