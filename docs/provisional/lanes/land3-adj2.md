# Lane land3-adj2: transcription adjudication of sd and f1095a (2026-11-14)

Model claude-opus-5-5, class judgment, tax year 2025, jurisdiction us. Rulings applied with
`tools/transcription/rule.py --kind transcription`; summaries appended to
`reviews/2025/transcription/adjudication/{sd,f1095a}.md` ("Landing round (2026-11-14)"). No form, question,
fixture, param or tool was edited; no build, render, check-all or paid review was run; nothing committed.

## sd (35 open, pass da3c033dcfd8): 32 scope, 3 model error

- Scope (32): lines 1a–10, columns (d)(e)(g)(h). The reply adds digital boxes G–L, which `sales.one` refuses (T-003),
  and drops the detail-route test on lines 2, 3, 9 and 10, which `sales.bad_aggregate` makes immaterial. No value
  differs; the differences are project refusals (`sd.other_forms`, `sales.digital`) or partial records that withhold
  an asked screen answer (`div.any`, `sd.sold_other`).
- Model error (3): `sd.distributions_if_dividends` gates box 2a on `div.has_capital_gain`, which is defined as
  `sd.distributions_if_dividends > 0`. The line reads itself ("cycle at sd.distributions_if_dividends" on every
  completed return). Line 13 copies that helper. `sd.filed` files whenever `sd.carryover` is Yes even when lines 6 and
  14 are $0 (completed witnesses stage20.line21_at_both_bounds and stage20.mut.line21_below_limit; i1040sd p. 10,
  "Otherwise, you don’t have any carryovers"). It also reads the raw boxes through the circular helper.

## f1095a (28 open, pass 76f2f43e33d3): 1 representation, 14 scope, 13 model error

- Representation (1): `f1095a.uniform`. (same_months ∧ ¬b_wrong) ∨ (b_wrong ∧ b_fixed_same) is the same function as
  the project's choose on `b_wrong_asked` (i8962 p. 14, Line 10). The only differences are 21 partials that withhold
  `b_blank` or `b_changed`.
- Scope (14): `a_jan`–`a_dec`, `line33a`, `line33c`. The reply zeroes a void form. The project refuses that return
  (`f8962.void_form`, i8962 p. 2). No value differs.
- Model error (13): `b_jan`–`b_dec` and `line33b`. This is the deviation already ruled in Stage 18 and R2: the reply
  zeroes an uncounted form's own column B and needs `b_counted` with a single form (i8962 p. 16, Column (b)).
  Completed value witnesses: stage18.blind.p11 and stage18.mut.two_forms_one_state_*; no Form 8962 amount differs.

## Findings

None, and no pending bug was filed. Lines left open: none. `check_logs.py` shows no open transcription ruling for sd
or f1095a. The render and class M items it still lists for these forms belong to other lanes and runs.

## Observation (tooling)

The line-scoped catalog lists `div.has_capital_gain` as a derived Bool gate without a label or definition, although it
is computed from `sd.distributions_if_dividends`, a line under review. The reply picked it as that line's gate and became
circular. A catalog that marked interfaces depending on reviewed lines, or left them out, would prevent this. It is not
filed as a bug.
