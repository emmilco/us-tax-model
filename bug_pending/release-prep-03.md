## BUG-NEW-release-prep-03 — samples.confirmed_bugs counts a bug id named in a ruling's class even when the class rules no defect

- **Date:** 2026-11-23
- **Caught by:** queue item 6 of .claude/wave-2026-11-22/after-int-queue.md (integration of 2026-11-23); filed in release preparation.
- **Symptom:** confirmed_bugs() adds every BUG id found in a ruling's class text (BUG_ID.findall on ruling['class']), so a class such as 'no defect (as BUG-NNNN, already fixed)' or 'covered by BUG-NNNN' confirms that bug, and samples.open_defects fails the release on an open medium or high bug the ruling only mentions. Its docstring says an id named only as context is not a confirmation.
- **Where:** tools/transcription/samples.py confirmed_bugs (the class branch).
- **Proposed fix:** take ids from the class only when the class itself classes a defect or a real gap (the same test the findings branch applies), with a self-test of a 'no defect' class naming an id.
- **Severity:** low
- **Tags:** tool, sampled reviews, release gate; open
