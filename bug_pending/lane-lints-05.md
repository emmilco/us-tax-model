## BUG-NEW-lane-lints-05 — ftc.statements: foreign income "reported to you" on a payee statement leaves out the spouse's statements

- **Date:** 2026-11-24
- **Caught by:** the spouse-phrase lint (engine/src/spouse-phrase.ts), built and triaged in lane lints (claude-opus-5-5, judgment), 2026-11-24
- **Source:** i1116 pp. 1-2, the election to claim the credit without Form 1116, available only if all foreign income and taxes are reported on qualified payee statements; i1040gi p. 13, "report their combined income and deduct their combined allowable expenses" (a joint return); interview/README.md, "A joint return combines both spouses' items"
- **Symptom:** ftc.statements, asked once per return, said "Was all of that income, and the foreign tax on it, reported to you on a Form 1099-DIV, ...". A joint filer whose spouse's Form 1099-DIV reports the foreign tax can answer No, and the return is then sent to Form 1116 (refused) although the election applies.
- **Where:** interview/2025/questions.yaml ftc.statements (prompt).
- **Fix:** Prompt: "... reported to you (or, on a joint return, your spouse) on a Form 1099-DIV, ...". No fixture: values unchanged.
- **Fix lines:** ftc.statements
- **Siblings checked:** ftc.statements_if_tax
- **Severity:** low
- **Tags:** foreign tax credit, spouse phrase; fixed
