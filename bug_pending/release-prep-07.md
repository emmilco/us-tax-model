## BUG-NEW-release-prep-07 — audit_skipped.py raises on a class M log case removed from its fixture

- **Date:** 2026-11-23
- **Caught by:** release preparation of next: full tier step classm_skipped (ValueError: classm.f1040.4: no matching fixture case).
- **Symptom:** Integration 5 (8175c23d) removed the DeepSeek fixture case classm.f1040.4.deepseek (its gifts refused under BUG-1204) while the DeepSeek class M log of f1040 keeps the case with blank model rows; tools/transcription/audit_skipped.py raised on the first blank row of a case with no fixture, so the step failed on next.
- **Where:** tools/transcription/audit_skipped.py reclassify.
- **Tool change:** a blank row of a case that is not in the fixture is passed over (it holds no assertion to drop); the log section is left as written.
- **Evidence:** audit_skipped.py: 0 numeric assertions to exclude; 0 log sections reclassified; exit 0.
- **Severity:** low
- **Tags:** tool, class M, fixtures, fixed
