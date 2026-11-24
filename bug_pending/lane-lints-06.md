## BUG-NEW-lane-lints-06 — ny_it201.ask.noncustodial: the child support question names "you" only, so a spouse who is the noncustodial parent misses the IT-209 refusal

- **Date:** 2026-11-24
- **Caught by:** the spouse-phrase lint (engine/src/spouse-phrase.ts), built and triaged in lane lints (claude-opus-5-5, judgment), 2026-11-24; named as a candidate by the bug-characterization scout of 2026-11-23 (section 4.1)
- **Source:** ny_it201i p. 19, Line 66, "Did you make child support payments payable through a New York State Support Collection Unit?"; ny_it209 line 25, "If your NYS filing status is Married filing joint return, enter the amount from column c" (a joint return claims the credit); interview/README.md, "A joint return combines both spouses' items"
- **Symptom:** ny_it201.ask.noncustodial, asked once per return, said "Did you pay child support in 2025 through New York's child support program ...?". On a joint return where the spouse is the noncustodial parent the filer can answer No, and the refusal for Form IT-209 (the noncustodial parent EIC, which this tool does not compute) is missed.
- **Where:** interview/ny/2025/questions.yaml ny_it201.ask.noncustodial (prompt).
- **Fix:** Prompt: "Did you (or, on a joint return, your spouse) pay child support in 2025 through New York's child support program (a Support Collection Unit)?". No fixture: values unchanged.
- **Fix lines:** ny_it201.ask.noncustodial
- **Siblings checked:** ny_it201.gate.noncustodial
- **Severity:** low
- **Tags:** New York, IT-209, spouse phrase; fixed
