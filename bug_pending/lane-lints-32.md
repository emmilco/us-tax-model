## BUG-NEW-lane-lints-32 — f4952.line1: interest on money borrowed for a rental or a passive activity is not left out, so a filer may count it as investment interest

- **Date:** 2026-11-24
- **Caught by:** the question review of 2026-11-24 (claude-opus-5-5), sample #1 on the reworded question, ruled in lane lints (claude-opus-5-5, judgment)
- **Source:** f4952 p. 3, Property held for investment, "However, it doesn’t include an interest in a passive activity." (a rental property is a passive activity; its interest goes on Schedule E)
- **Symptom:** The prompt leaves out interest on a home, tax-exempt bonds and a business, but not a rental property or a passive partnership, which filers often call investments. A filer with a rental mortgage can report its interest on Form 4952 line 1 (and on Schedule E), overstating the deduction.
- **Where:** interview/2025/questions.yaml f4952.line1 (prompt or help).
- **Proposed fix:** Add a rental property or other passive activity to what is left out ("..., a rental property or a business").
- **Proposed fix lines:** f4952.line1
- **Severity:** low
- **Tags:** Form 4952, wording, question review; open
