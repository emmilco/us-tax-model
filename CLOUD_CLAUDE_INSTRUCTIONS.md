# Cloud Claude instructions

This file is the task channel for the cloud Claude session working on this repository. The local session writes
tasks here; the cloud session watches it, pulls `origin/f8962-form-pass`, does the work, and records the result
under **Completed** below.

## Protocol

- Poll this file and `origin/f8962-form-pass` about every ten minutes. Pull before starting a task.
- Work only on `f8962-form-pass`. Never push to `main`, never force-push, never rewrite published commits.
- Do not edit `forms/`, `rendered/`, `canonical/`, `fixtures/`, `reviews/`, or `sources/` unless a task explicitly
  asks for it. Do not rule disagreements, do not run triage, and do not run the full suite.
- A task is finished when the **Completed** section names it, the commit or the read-only result, and any
  material problem found. If a task cannot be done, say so there with the exact error; do not substitute a
  different model or hand-write a model response.
- Keep findings short and evidenced: file:line, the source quote or the command output. No summaries of the
  whole repository.

## Task queue

1. **Independent audit of the f8962/f1095a review rulings (read-only).**
   On the pulled branch, read these and check each ruling against the archived source text in `sources/2025/`:
   - `reviews/2025/transcription/f8962.md` and `f8962.deepseek.md`, `f8962.gpt.md` (the interface-gap and scope
     rulings, and the DeepSeek model-error rulings on the invalid `f1095a.c_<month>` declarations and line 24);
   - `reviews/2025/transcription/f1095a.md` and the `.deepseek`/`.gpt` logs (representation/model-error rulings);
   - `reviews/2025/render/f8962.md`, `f1095a.md` and their family logs (the scope rulings on the return-level
     refusals: `sa.dependent`, `s3.mfs`, `scope.schedule1`, `scope.other_line16`, `f8962.two_counted`,
     `f8962.marriage`, `f8962.alloc`, `f8962.other`);
   - `reviews/2025/completeness/rulings.json`, the nine `unruled:f8962#*` and `unruled:f1095a#*` entries.
   Report only material problems: a quote that does not appear on the named page, a ruling that calls a real
   tax-reading difference an interface gap (or the reverse), or a covered ruling whose named line does not
   actually carry the rule. Do not restate rulings you agree with; say "no material problems" if that is the case.

2. **Independent statement-coverage check of `f8962.other` (read-only, second opinion).**
   Read the `f8962.other` question in `forms/2025/f8962.yaml` against i8962 pp. 5–6 and list any *under*-inclusive
   limb (a filer the question would let answer no although the source says the person is eligible for MEC or is
   otherwise excluded), separate from the over-refusals already recorded in the screen ruling. Quote the source
   sentence for each. If there is none, say so.

## Completed

(Cloud session writes here.)
