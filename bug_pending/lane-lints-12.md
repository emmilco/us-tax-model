## BUG-NEW-lane-lints-12 — f8880.agi_limit: its label prints the 2025 amount of savers.agi_limit, which changes in 2026, and no 2026 operation relabels it

- **Date:** 2026-11-24
- **Caught by:** the year-label lint (tools/check_label_year.py), built in lane lints (claude-opus-5-5, judgment), 2026-11-24
- **Source:** f8880 (2026) p. 2, "is more than $40,250 ($60,375 if head of household; $80,500 if married filing jointly)."; research/ty2026/params-2026.proposed.yaml savers.agi_limit (source: final)
- **Symptom:** The label of f8880.agi_limit prints "Year parameter savers.agi_limit ($39,500; $59,250 if head of household; $79,000 if married filing jointly)". The line reads savers.agi_limit, whose staged 2026 value differs, and no operation of changes/2026/ set the label, so the adopted 2026 line would print the 2025 amount beside the 2026 value (the BUG-1032 shape). Values unchanged.
- **Where:** forms/2025/f8880.yaml f8880.agi_limit (label), as adopted for 2026.
- **Fix:** changes/2026/f8880.labels.yaml, entry BUG-NEW-lane-lints-12: a set of the label to "Year parameter savers.agi_limit ($40,250; $60,375 if head of household; $80,500 if married filing jointly)" (verified: final). No 2025 text or value changes.
- **Fix lines:** f8880.agi_limit
- **Siblings checked:** f8880.past9, f8880.within_limit
- **Severity:** low
- **Tags:** TY2026, year changes, labels; fixed
