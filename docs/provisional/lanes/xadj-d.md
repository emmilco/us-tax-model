# Lane xadj-d: round-2 adjudication of the credit forms (f2441, f8863, f8889, f8962, ftc, f1116)

Model: claude-opus-5-5. Class: judgment. Year: 2025. Jurisdiction: us. Fork of lane xadj, worktree `xint`.
No forms, fixtures, params or tools edited; no build, render, check-all or paid review; no commit. Rulings files in
`/tmp/xadj/xadj-d/`; summaries appended to `reviews/2025/transcription/adjudication/<form>.md` under
"Goal-1 coverage-expansion round (2026-11-15)" (plus ", render" / ", class M").

## Findings (pending bugs)

| id | severity | form line | proposed fix |
| --- | --- | --- | --- |
| BUG-0769 | medium | ftc.needs1116 | Add `sa.excluded_income = true` to the `any` list of failed election conditions (i1040gi Schedule 3, line 1, condition 4: "You aren't filing Form 4563 or excluding income from sources within Puerto Rico"). The return then takes the Form 1116 path, where f1116.reduction refuses. Today a Form 4563 filer or Puerto Rico excluder with foreign tax of $300 or less ($600 joint) gets the election credit; sa.excluded_income refuses only on Schedule A, Schedule 1-A, sli and other credits. |
| BUG-0770 | low | f8962.line11a, line11b, line12a/12b to line23a/23b (26 lines) | Hide columns (a) and (b) when f8962.mfs_barred is true (i8962: a separate filer without Exception 2 must "skip columns (a) through (e), and complete only column (f)"). Columns (c) to (e) are already hidden; no amount changes. Keep (a) and (b) shown for a filer below 100% of the poverty line. |

## Counts by form and kind

| form | transcription | render | class M |
| --- | --- | --- | --- |
| ftc | model error 6, representation 1 | 22 match; finding 1 (medium), ambiguity 1, scope 1 | not run this round |
| f8863 | model error 20, representation 6 | 25 match, none open | 66 agree, none open |
| f1116 | interface gap 1 (3e) | 1 match | ambiguity 11, model error 2 (dropped) |
| f2441 | representation 5, scope 1 | 32 match; scope 5 | 243 agree, none open |
| f8889 | model error 7, representation 3 | 17 match; ambiguity 1, scope 1 | 252 agree; ambiguity 3 (dropped) |
| f8962 | representation 90 | 68 match; finding 26 (low), scope 2 | 365 agree, none open |

## Notes for the coordinator

- Tool gap (not a form defect): the line-scoped transcription request for f1116
  (`.transcription/f1116.lines-a0e3f14dd0cd.prompt.txt`) records complete input context: fail. It carried none of
  the Form 1040 / Schedule 1 income lines that line 3e reads, so the reply could not transcribe 3e (ruled interface gap).
- Owner question (ruled ambiguity, not a finding): ftc.elect makes the election whenever available
  (amb.2025.f1116_carryover_election, D3). When the foreign tax exceeds the regular tax, the election forfeits the
  carryforward a Form 1116 would keep; on this tool's Form 1116 path that excess refuses (f1116.carryover_out). A
  refusal in that case instead of the election would keep the filer's carryforward.
- The main model errors are the reply's, not the project's: ftc gates the foreign tax on s3.foreign_any alone, whose
  help tells box 7 fund-tax holders to answer No; f8863 drops "claimed as a dependent"; f8889 claims the HSA entry
  cannot read the person's age (the request carried person.birth_year), dropping the $1,000 age-55 amount.
- check_logs could not be run to completion at 21:07: the build is stale (forms/2025/s2.yaml edited 21:06:57 by
  another lane); this lane does not build.
