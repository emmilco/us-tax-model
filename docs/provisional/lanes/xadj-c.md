# Lane xadj-c: round-2 adjudication of s2, s3, se, f8959, f8960 (coverage-expansion merge)

Model claude-opus-5-5, class judgment, tax year 2025, jurisdiction us. Worktree `.claude/worktrees/xint`
(uncommitted). Reviews were run by lane xadj; this lane ruled the open lines with `tools/transcription/rule.py`.
Rulings files `/tmp/xadj/c/<form>.<kind>.json`. Summaries are in `reviews/2025/transcription/adjudication/<form>.md`,
section "Goal-1 coverage-expansion round (2026-11-15)" (`se.md` is new). No forms, fixtures or tools edited; no
pending bugs.

## Findings
None (no high, medium or low).

## Rulings by form and kind

| form | transcription | render | class M |
| --- | --- | --- | --- |
| s2 | line 2: scope (AMT refused at s2.amt; no value difference); 5, 6, 7, 21 agree | 6 match | CLASSM_S2 |
| s3 | s3.other_credit: representation (follow-ups read outside their gates; as in earlier rounds); 11 agrees | 7 match | CLASSM_S3 |
| se | line13: representation (equivalent; 478/480, no value difference) | 2, 3, 4b, 5b: interface gap (refused at the caller through person.se_screen); 13 match | 29 agree; classm.se.2 line 8d: representation (skipped line, drop) |
| f8959 | 2 agree | 3 match | 52 agree, 20 skipped |
| f8960 | 4a: representation (Schedule 1 line 3 netted out by line 4b for an active business; else refused by f8960.unsupported); line 13 ruled mechanically (model error on the declaration); 11 agree | 13 match | 50 agree |

## Notes
- f8960 4a: the triage witnesses checked (stage14.asset.hy_5yr; stage5.return.refund_f8960_refund_unused) file no
  Form 8960; rentals that are a trade or business (real estate professional) are refused in sche, so line 4b at zero
  is consistent.
- se render: the four lines were ruled earlier as "refusal located elsewhere", which compare_families classes as
  unclassified; this round uses interface gap. person.se_screen was checked on the current tree and still names
  every case.
- Observation outside these forms (person.yaml): the refusal text of person.se_line2 still lists "Forms 4137 and
  8919", now figured and no longer on person.se_screen (cosmetic).
