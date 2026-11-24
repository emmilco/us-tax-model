## BUG-NEW-lane-lints-17 — person.ira_line2_apart: its label prints the 2025 amount of ira.line2_apart, which changes in 2026, and no 2026 operation relabels it

- **Date:** 2026-11-24
- **Caught by:** the year-label lint (tools/check_label_year.py), built in lane lints (claude-opus-5-5, judgment), 2026-11-24; named as a candidate by the bug-characterization scout of 2026-11-23 (section 4.2)
- **Source:** p590a (2026) p. 15, "$91,000 or more"; research/ty2026/params-2026.proposed.yaml ira.line2_apart (source: draft)
- **Symptom:** The label of person.ira_line2_apart prints "$89,000 (married filing separately and lived apart from your spouse for all of 2025)". The line reads ira.line2_apart, whose staged 2026 value differs, and no operation of changes/2026/ set the label, so the adopted 2026 line would print the 2025 amount beside the 2026 value (the BUG-1032 shape). Values unchanged.
- **Where:** forms/2025/person.yaml person.ira_line2_apart (label), as adopted for 2026.
- **Fix:** changes/2026/person.labels.yaml, entry BUG-NEW-lane-lints-17: a set of the label to "$91,000 (married filing separately and lived apart from your spouse for all of 2026)" (verified: draft). No 2025 text or value changes.
- **Fix lines:** person.ira_line2_apart
- **Siblings checked:** person.ira_line2_status
- **Severity:** low
- **Tags:** TY2026, year changes, labels; fixed
