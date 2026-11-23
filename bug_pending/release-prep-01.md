## BUG-NEW-release-prep-01 — QSS child conflict screen counts foster children and descendants as the qualifying surviving spouse's child

- **Date:** 2026-11-23
- **Caught by:** release preparation of next (7466debd), tools/check_consumers.py: new pair dependent.relationship@i1040gi:p15, read by household.qss_children_listed.
- **Symptom:** household.qss_children_listed and household.qss_children_all_year count dependents whose relationship is child, which the question defines as a son, daughter, stepchild, eligible foster child or a descendant of any of them. The qualifying surviving spouse test (i1040gi p. 15, test 2) needs "a child or stepchild (not a foster child)". The conflict screen household.qss_child_conflict (refused through household.qss_fails) therefore misses the case where a listed stepchild did not live with the filer all year while a listed foster child or grandchild did, and refuses where only a foster child or grandchild is listed and did not live there all year. The screen is a backstop to the filer's Yes to the QSS tests; no amount changes.
- **Where:** forms/2025/household.yaml household.qss_children_listed, household.qss_children_all_year; dependent.relationship (forms/2025/dependent.yaml).
- **Proposed fix:** count only sons, daughters and stepchildren: split the child answer (or add a follow-up asked of a child entry: foster child or descendant) and filter the two counts on it.
- **Severity:** low
- **Tags:** household, QSS, consumers; open
