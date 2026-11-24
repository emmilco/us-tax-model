## BUG-NEW-lane-lints-29 — s2.amt_l6_high: its label prints the 2025 amount of amt.bracket, which changes in 2026, and no 2026 operation relabels it

- **Date:** 2026-11-24
- **Caught by:** the year-label lint (tools/check_label_year.py), built in lane lints (claude-opus-5-5, judgment), 2026-11-24
- **Source:** rp-25-32 (2026) p. 16, "Married Individuals Filing Separate Returns $122,250"; rp-25-32 (2026) p. 16, "All Other Taxpayers $244,500"; research/ty2026/params-2026.proposed.yaml amt.bracket (source: final)
- **Symptom:** The label of s2.amt_l6_high prints "Line 6 is more than $239,100 ($119,550 if married filing separately)". The line reads amt.bracket, whose staged 2026 value differs, and no operation of changes/2026/ set the label, so the adopted 2026 line would print the 2025 amount beside the 2026 value (the BUG-1032 shape). Values unchanged.
- **Where:** forms/2025/s2.yaml s2.amt_l6_high (label), as adopted for 2026.
- **Fix:** changes/2026/s2.labels.yaml, entry BUG-NEW-lane-lints-29: a set of the label to "Line 6 is more than $244,500 ($122,250 if married filing separately)" (verified: final). No 2025 text or value changes.
- **Fix lines:** s2.amt_l6_high
- **Siblings checked:** s2.amt_l39
- **Severity:** low
- **Tags:** TY2026, year changes, labels; fixed
