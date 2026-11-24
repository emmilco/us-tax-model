## BUG-NEW-lane-lints-01 — f4952.line1: the investment interest amount is asked of "you" only on a joint return

- **Date:** 2026-11-24
- **Caught by:** the spouse-phrase lint (engine/src/spouse-phrase.ts), built and triaged in lane lints (claude-opus-5-5, judgment), 2026-11-24; named as a candidate by the bug-characterization scout of 2026-11-23 (section 4.1)
- **Source:** f4952 p. 3, Line 1, "Investment interest expense is interest paid or accrued on a loan or part of a loan that is allocable to property held for investment"; i1040gi p. 13, "report their combined income and deduct their combined allowable expenses" (a joint return); interview/README.md, "A joint return combines both spouses' items"
- **Symptom:** f4952.line1, asked once per return, said "How much interest did you pay in 2025 on money borrowed to buy investments?" while its parent f4952.has_interest asks of "you (or, on a joint return, your spouse)". A joint filer whose spouse paid margin interest can leave it out: Form 4952 line 1, and the deduction it allows, are understated.
- **Where:** interview/2025/questions.yaml f4952.line1 (prompt).
- **Fix:** Prompt: "How much interest did you (or, on a joint return, your spouse) pay in 2025 on money borrowed to buy investments? ..." (the rest unchanged). No fixture: the value read is unchanged; only the wording that leads to it.
- **Fix lines:** f4952.line1
- **Siblings checked:** f4952.line1_if_interest
- **Severity:** low
- **Tags:** Form 4952, spouse phrase; fixed
