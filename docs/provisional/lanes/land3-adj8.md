# Lane land3-adj8: transcription adjudication of f1095a after the column-B fix (2026-11-14)

Model claude-opus-5-5, class judgment, tax year 2025, jurisdiction us. Rulings applied with
`tools/transcription/rule.py --kind transcription` (rulings file `/tmp/land3-adj8/f1095a.json`); summary appended to
`reviews/2025/transcription/adjudication/f1095a.md` ("Landing round (2026-11-14), after the column-B fix"). No form,
question, fixture, param or tool was edited; no build, render, check-all or paid review was run; nothing committed.

## f1095a (28 open, line-scoped pass ea49629f14d1): 1 finding (low), 14 representation, 13 model error

- Finding, low (1): `f1095a.uniform`, BUG-0635. The reply's column B test differs both ways:
  - The reply is wrong on no APTC. It tests only `b_blank`, `b_changed` and `b_doubt`, reading situation 1 as a blank
    column B. i8962 p. 14 makes no APTC a trigger of its own ("If either of these two situations applies to you ... you
    must determine the correct applicable SLCSP premium for every month"; p. 16, "or if no APTC was paid"). Completed
    value witness: stage18.reg.no_aptc_slcsp_by_month (project No, reply Yes).
  - The project is wrong where Part III differs by month: `f1095a.b_wrong_asked` reads only `b_wrong` there, so
    `b_doubt` and no advance payments never reach `b_fixed_same`, while `b_blank` does. A form with column A the same all
    year and a corrected column B the same every month gets Form 8962 line 10 No and lines 12 to 23, where line 10 is a
    test on the corrected premium (i8962 p. 14 bullets, "But see Missing or incorrect SLCSP premium";
    amb.2025.ptc_annual_route). Effect: the line 10 box and a few dollars through line 8b rounding. Not reached by any
    sample input; found by reading.
- Representation (14): `a_jan`–`a_dec`, `line33a`, `line33c`. The project's expressions, differing only through the
  reply's `uniform`; where the routes part column A is the same every month and line 33C equals the monthly sum. The one
  completed value (stage18.reg.no_aptc_slcsp_by_month) is a fixture that states the monthly inputs and not `mo_a`.
- Model error (13): `b_jan`–`b_dec`, `line33b`. The deviation ruled in R2, Stage 18 and the first landing round (an
  uncounted form's own column B zeroed through `b_counted`, needed even with one form; i8962 p. 16, Column (b)), plus the
  dropped no-APTC limb.

## Findings

- BUG-0635 (low), `bug_pending/land3-adj8-01.md`. Where: `f1095a.b_wrong_asked` (No branch),
  `f1095a.uniform`, read by `f8962.nonuniform`/`f8962.line10`. Proposed fix, no new question: add
  `f1095a.months_uniform` (every `in_a_*` equals `in_a_jan` and is above zero; every `in_b_*` equals `in_b_jan`) and
  `f1095a.annual_ok` = any(`f1095a.uniform`, `f1095a.months_uniform`); `f8962.nonuniform` counts forms with
  `annual_ok` false instead of `uniform` false. `uniform` stays the entry route (mo_a/mo_b against in_*). Alternative:
  on the No branch read any(`b_wrong`, `b_doubt`, `yr_c_monthly` = 0) before `b_fixed_same`, which costs steps and
  reorders the bank.

Lines left open: none.
