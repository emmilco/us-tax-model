## BUG-NEW-lane-lints-18 — person.ira_line2_nc: its label prints the 2025 amount of ira.line2_not_covered, which changes in 2026, and no 2026 operation relabels it

- **Date:** 2026-11-24
- **Caught by:** the year-label lint (tools/check_label_year.py), built in lane lints (claude-opus-5-5, judgment), 2026-11-24; named as a candidate by the bug-characterization scout of 2026-11-23 (section 4.2)
- **Source:** n-25-67 (2026) p. 4, "between $242,000 and $252,000"; research/ty2026/params-2026.proposed.yaml ira.line2_not_covered (source: final)
- **Symptom:** The label of person.ira_line2_nc prints "$246,000". The line reads ira.line2_not_covered, whose staged 2026 value differs, and no operation of changes/2026/ set the label, so the adopted 2026 line would print the 2025 amount beside the 2026 value (the BUG-1032 shape). Values unchanged.
- **Where:** forms/2025/person.yaml person.ira_line2_nc (label), as adopted for 2026.
- **Fix:** changes/2026/person.labels.yaml, entry BUG-NEW-lane-lints-18: a set of the label to "$252,000" (verified: final). No 2025 text or value changes.
- **Fix lines:** person.ira_line2_nc
- **Siblings checked:** person.ira_line2
- **Severity:** low
- **Tags:** TY2026, year changes, labels; fixed
