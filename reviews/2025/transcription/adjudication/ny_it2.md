# Adjudication — ny_it2 (New York, 2025)

New York logs live under `.transcription/logs/ny/2025/`; this directory has no New York counterpart, so the
New York form's rounds are summarized here.

## Goal-1 round (2026-11-15)

Lane b1-adj-ny (claude-opus-5-5, judgment, tax year 2025, jurisdiction ny), in the B1 integration worktree. Open
lines of the Claude transcription log `.transcription/logs/ny/2025/transcription/ny_it2.md` (line-scoped pass
898b729f5b1b, rerun because the W-2c wording of the input questions changed). `carry.py --jurisdiction ny` carried
nothing. Triage did not reach these lines (no whole-form section); the value expressions are identical by
inspection, and only `shown_when` differs. The deepseek family is dormant and not ruled.

| family | kind | line | class | evidence | deciding source | reason |
| --- | --- | --- | --- | --- | --- | --- |
| claude | transcription | 17a (whole dollars) | finding (low) | log; form YAML | IT-2 p. 2, Boxes 15a through 17a, "If you have no New York State wages or withholding, leave boxes 16a and 17a blank." | The project shows the box on every record ($0 without withholding); the reply shows it only when more than zero. The 2026-11-04 model-error ruling rested on the record being required for every W-2, which does not make the box required. |
| claude | transcription | 19 (whole dollars) | finding (low) | log; form YAML | IT-2 p. 2, Boxes 18 through 20, "Complete the locality boxes 18 through 20 only for NYC or Yonkers (or both) wages and withholding, if reported on federal Form W-2." | As 17a, for the NYC locality box. |

Counts: claude transcription: finding 2.

Findings: BUG-0763 (low; presentation only, totals to IT-201 lines 72 and 73 unchanged). No line left open.
