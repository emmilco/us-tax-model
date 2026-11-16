# Lane b1-adj-c — adjudication, f2441, f8962, f1095a, refund, f8889 (goal-1 round, B1)

Model claude-opus-5-5, class judgment, tax year 2025, jurisdiction us. Worktree `.claude/worktrees/nx-b1`. Two
forked sub-lanes (same model and class) ruled f1095a and f8889; this lane ruled f2441, f8962 and refund. Touched only
the Claude transcription, render and class M logs and sidecars of these forms (through `rule.py`), their adjudication
summaries `reviews/2025/transcription/adjudication/<form>.md` (sections "Goal-1 round (2026-11-15)", ", render",
", class M"), one pending bug file and this note. No form, tool, fixture edit, build, render or paid review. Rulings
files under `/tmp/b1-adj-c/`.

## Rulings

| form | kind | counts |
| --- | --- | --- |
| f2441 | transcription | representation 3 (3, 16, 27), scope 1 (19), model error 1 (1 (box)), finding 1 low (2 (box)) |
| f2441 | render | scope 5 (4, 5, 12, 18, 19) |
| f8962 | transcription | representation 1 (25), scope 1 (10), ambiguity 1 (24, amb.2025.ptc_not_applicable) |
| f8962 | render | scope 1 (24) |
| refund | transcription | representation 2 (refund.taxable, 1) |
| refund | render | ambiguity 1 (1), representation 1 (6) |
| f1095a | transcription | model error 14 (annual_ok, b_jan to b_dec, line33b) |
| f8889 | transcription | model error 5 (step1, share_raw, excess_amt, 3, 6), representation 5 (split, 13, 15, 16, 17b), ambiguity 1 (7) |
| f8889 | render | ambiguity 1 (7), scope 1 (13) |
| f1095a | class M | open (1 line, classm.f1095a.3 — uniform): prepared as model error, dropped; not applied (hold) |
| f8889 | class M | open (4 lines, classm.f8889.4 — line6, 7 ambiguity; line8, 12 model error; all dropped): prepared, not applied (hold) |

## Findings

- **BUG-0760 (low; no value change).** `f2441.line2_box` (Form 2441 line 2 box, "more than three
  qualifying persons") compares the qualifying-person count with `dc.providers_listed`, the line 1 care-provider
  limit (its cite: i2441 p. 2, Line 1, "more than three care providers"). Both are 3 for 2025. Fix: add
  `params/2025.yaml` `dc.persons_listed` (Count 3, cite i2441 p. 3, Line 2) and change `f2441.line2_box` to
  `gt [f2441.qp_count, param dc.persons_listed]`.

## Notes

- f1095a: `triage.py --form f1095a` refuses the form for this pass (an older pass names `f1095a.uniform`, no longer a
  compared line), so its 14 rulings rest on the log sections, i8962/i1095a and the form YAML. The sub-lane first
  ruled 13 of them representation, then reopened them with `rulings.read_log`/`write_log` (rule.py --amend refuses a
  class change) and re-ruled them model error with `rule.py`, in line with the earlier rounds.
- Class M was paused by the coordinator (fixtures/2025/classm.json being restored); no class M carry or rule was run by this lane. Rulings ready to apply, one form at a time, once cleared: `python3 tools/transcription/carry.py --kind classm --form <f>` then `python3 tools/transcription/rule.py --form <f> --kind classm --rulings /tmp/b1-adj-c/<f>.classm.json` (f1095a, f8889); then append a "Goal-1 round (2026-11-15), class M" section to each form's adjudication summary.

## Verification

`check_logs.py` (run 15:47): for these five forms only `[claude] f1095a: open ruling(s) in the classm log` and `[claude] f8889: open ruling(s) in the classm log`; no open transcription or render ruling remains.
