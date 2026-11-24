## BUG-NEW-lane-lints-03 — scope.military_move: storage fees "while you were posted" outside the United States leaves out a spouse posted abroad

- **Date:** 2026-11-24
- **Caught by:** the spouse-phrase lint (engine/src/spouse-phrase.ts), built and triaged in lane lints (claude-opus-5-5, judgment), 2026-11-24; named as a candidate by the bug-characterization scout of 2026-11-23 (section 4.1) (weaker)
- **Source:** i1040gi p. 93, Line 14, "If you are claiming only storage fees during your absence from the United States, check the box on line 14"; i1040gi p. 13, "report their combined income and deduct their combined allowable expenses" (a joint return); interview/README.md, "A joint return combines both spouses' items"
- **Symptom:** scope.military_move, asked once per return after scope.armed_forces (which names the spouse), said "... or storage fees while you were posted outside the United States?". On a joint return where the spouse is the member posted abroad, the filer can answer No and the refusal of the Form 3903 deduction is not told; the return is then figured without a deduction the couple may take.
- **Where:** forms/2025/scope.yaml scope.military_move (label and source).
- **Fix:** Label and prompt: "... or storage fees while you (or, on a joint return, your spouse) were posted outside the United States?". No fixture: values unchanged.
- **Fix lines:** scope.military_move
- **Siblings checked:** scope.military_move_if_armed_forces
- **Severity:** low
- **Tags:** scope, Form 3903, spouse phrase; fixed
