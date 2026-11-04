# Proposed bug entries (package "review-catalog")

Ids are placeholders; the integrator assigns BUG numbers.

## PENDING-1 — Form 4952 line 4a reads Schedule B lines its source does not reach

- **Caught by:** the review-catalog omission check, 2026-11-03 (source-derived transcription catalog).
- **Source:** f4952 pp. 1, 3–4 (the whole form, cited by `f4952.line4a`) names no Schedule B line; the nearby text names "Form 1040 or 1040-SR, line 3a". f1040sb line 4: "Subtract line 3 from line 2. Enter the result here and on Form 1040 or 1040-SR, line 2b".
- **Symptom:** `f4952.line4a` = `sb.line2` + `sb.line6`. Under the source-chosen catalog, Schedule B is not listed in f4952's prompt, so the required-interface check fails. Separately, Schedule B line 2 is interest before the excludable savings bond interest of line 3 (Form 8815). Whether that interest belongs in line 4a is a source question not settled here.
- **Fix:** proposed. Either cite the page that supports reading Schedule B (so the excerpt reaches it), or read `f1040.line2b`/`f1040.line3b` if the source supports line 4 rather than line 2.
- **Fix lines:** f4952.line4a (not owned by this package).
- **Siblings checked:** f8960 lines 1 and 2 also read `sb.line2`/`sb.line6`, while i8960 names "Form 1040 or 1040-SR, line 2b" and "line 3b". The catalog reaches Schedule B there through the whole i8960 text, but the same line 2 versus line 4 question applies.
- **Regression predictions:** none until a reading is chosen.
- **Validation:** omission.json; `input_context.assess` on the dry-run prompt.
- **Tags:** review-tool; interface; catalog; open

## PENDING-2 — Form 8863 reads the student loan worksheet's dependency question

- **Caught by:** the review-catalog omission check, 2026-11-03.
- **Source:** i8863 p. 3, "Who cannot claim a credit", "1. You're claimed as a dependent on another person's tax return"; the question `sli.claimed` sits on the Student Loan Interest Deduction Worksheet (i1040gi p. 98), which no Form 8863 source names.
- **Symptom:** `f8863.eligible` reads `sli.claimed`. Under the source-chosen catalog, sli is not listed in f8863's prompt, so the required-interface check fails.
- **Fix:** proposed. Ask the "claimed as a dependent" question where both credits' sources reach it (a return-level or person-level question), or cite the shared question's home from f8863.
- **Fix lines:** f8863.eligible (not owned by this package).
- **Siblings checked:** none else found by the omission check.
- **Regression predictions:** no value change if the question is moved with the same wording.
- **Validation:** omission.json.
- **Tags:** review-tool; interface; catalog; open

## PENDING-3 — Transcription catalog listed every form; T-163 visibility wording

- **Caught by:** owner decision 2026-11-03 (catalog of about 450k characters; codex limit 1,048,576) and T-163.
- **Source:** none (tooling).
- **Symptom:** every transcription prompt carried every other form's lines and every collection (363k to 395k characters). The prompt called `shown_when` optional, and all three families omitted it on f8962.
- **Fix:** `catalog_selection` (a source-chosen subset; REPORT.md); screening entries carry the full interface note; `SHOWN_WHEN_NOTE` plus a template row; `PROMPT_POLICY` is now `source-only-computation-v3`.
- **Fix lines:** none (tool change).
- **Siblings checked:** render, class M, completeness and screen prompts are unchanged; the excerpt is byte-identical on all 61 forms.
- **Regression predictions:** the total characters of all prompts fall from 32.5M to 21.8M; person falls from 1,045,076 to 1,022,531; f4952 and f8863 fail complete input context (PENDING-1, PENDING-2).
- **Validation:** test_review_tools.py, test_input_context.py, audit_transcription (identical), check_logs.
- **Tags:** review-tool; catalog; prompt-policy; fixed
