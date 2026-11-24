## BUG-NEW-lane-tooling-06 — Closure: BUG-1198 is fixed: check_completeness accepts a branch's pending bug id on a real gap

- **Closes:** BUG-1198
- **Closure:** fixed
- **Caught by:** BUG-1198, listed open by tools/bug_status.py (its 'Tool change (fixed)' field is not a fix field bug_status reads); lane tooling of the 2026-11-24 wave (claude-opus-5-5, judgment).
- **Evidence:** does not reproduce: the fix the entry records is in the tree since 8175c23d (integration of the advfix and advland lanes). check_completeness.validate on a real gap with a pending bug id (BUG-NEW-<name>, the advfix lane's first) returns no error, and with PENDING-1 still refuses ('pending bug id PENDING-1'); its self-test case u:f#6 (a BUG-NEW id) is in tools/transcription/check_completeness.py. Nothing changed here; this entry records the status bug_status could not derive.
- **Tags:** tool, completeness, pending entries, fixed
