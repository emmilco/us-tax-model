## BUG-NEW-lane-lints-33 — ftc.statements: "a similar statement" lets in a foreign bank or broker certificate, which is not a qualified payee statement

- **Date:** 2026-11-24
- **Caught by:** the question review of 2026-11-24 (claude-opus-5-5), sample #1 on the reworded question, ruled in lane lints (claude-opus-5-5, judgment)
- **Source:** i1116 p. 1, the election without Form 1116: all foreign source gross income and foreign taxes must be reported on a qualified payee statement (Form 1099-DIV, 1099-INT, Schedule K-1 (Form 1041), Schedule K-3, or a similar substitute statement)
- **Symptom:** A filer whose foreign dividends and withheld tax appear only on a foreign institution's certificate can answer Yes, and the election is taken where Form 1116 is required.
- **Where:** interview/2025/questions.yaml ftc.statements (prompt or help).
- **Proposed fix:** Say "a substitute for one of these forms" and add to the help that a statement from a foreign bank or broker does not count.
- **Proposed fix lines:** ftc.statements
- **Severity:** low
- **Tags:** foreign tax credit, wording, question review; open
