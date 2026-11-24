## BUG-NEW-lane-lints-07 — ny_it201.ask.other_withholding: New York tax withheld from a payment "to you" leaves out the spouse's Forms 1099-R, 1099-G and W-2G

- **Date:** 2026-11-24
- **Caught by:** the spouse-phrase lint (engine/src/spouse-phrase.ts), built and triaged in lane lints (claude-opus-5-5, judgment), 2026-11-24; named as a candidate by the bug-characterization scout of 2026-11-23 (section 4.1)
- **Source:** ny_it201i p. 21, Lines 72, 73, and 74, "Enter on the appropriate line your total New York State, New York City, and Yonkers tax withheld from any of the following:"; interview/README.md, "A joint return combines both spouses' items"
- **Symptom:** ny_it201.ask.other_withholding, asked once per return, said "Was New York income tax taken out of any retirement, unemployment or other payment to you (not pay on a Form W-2)?". A joint filer whose spouse's Form 1099-R shows New York withholding can answer No: the refusal is missed and the withholding is left off lines 72 to 74 (the New York balance due overstated).
- **Where:** interview/ny/2025/questions.yaml ny_it201.ask.other_withholding (prompt and help).
- **Fix:** Prompt: "Was New York income tax taken out of any retirement, unemployment or other payment (not pay on a Form W-2) to you (or, on a joint return, your spouse)?"; help: "Look at the state and local boxes of your (or, on a joint return, your spouse's) Forms 1099-R, 1099-G and W-2G. ..." No fixture: values unchanged. The question's gating (BUG-1153) is not changed here.
- **Fix lines:** ny_it201.ask.other_withholding
- **Siblings checked:** ny_it201.gate.other_withholding
- **Severity:** low
- **Tags:** New York, withholding, spouse phrase; fixed
