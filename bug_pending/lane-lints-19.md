## BUG-NEW-lane-lints-19 — person.ira_line2_table: its label prints the 2025 amount of ira.line2, which changes in 2026, and no 2026 operation relabels it

- **Date:** 2026-11-24
- **Caught by:** the year-label lint (tools/check_label_year.py), built in lane lints (claude-opus-5-5, judgment), 2026-11-24
- **Source:** n-25-67 (2026) p. 4, "between $81,000 and $91,000"; n-25-67 (2026) p. 4, "between $129,000 and $149,000"; n-25-67 (2026) p. 4, "remains $0 to $10,000"; research/ty2026/params-2026.proposed.yaml ira.line2 (source: final)
- **Symptom:** The label of person.ira_line2_table prints "The line 2 amount for the filing status ($89,000; $146,000 if married filing jointly or qualifying surviving spouse; $10,000 if married filing separately)". The line reads ira.line2, whose staged 2026 value differs, and no operation of changes/2026/ set the label, so the adopted 2026 line would print the 2025 amount beside the 2026 value (the BUG-1032 shape). Values unchanged.
- **Where:** forms/2025/person.yaml person.ira_line2_table (label), as adopted for 2026.
- **Fix:** changes/2026/person.labels.yaml, entry BUG-NEW-lane-lints-19: a set of the label to "The line 2 amount for the filing status ($91,000; $149,000 if married filing jointly or qualifying surviving spouse; $10,000 if married filing separately)" (verified: final). No 2025 text or value changes.
- **Fix lines:** person.ira_line2_table
- **Siblings checked:** person.ira_line2_status
- **Severity:** low
- **Tags:** TY2026, year changes, labels; fixed
