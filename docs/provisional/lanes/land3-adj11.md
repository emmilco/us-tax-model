# Lane land3-adj11: transcription, render and class M adjudication of ny_it201

Agent: `claude-opus-5-5`, class judgment, tax year 2025, jurisdiction `ny`. No paid call, no model call from code, no
build, render or check-all. Forms, questions, params and tools untouched; the class M fixture changed only through
`rule.py` drops.

`carry.py --jurisdiction ny` was run for all three kinds and ruled nothing; triage was rerun for the transcription
log. All open Claude sections ruled with `rule.py --jurisdiction ny`; rulings in
`/tmp/land3-adj11/ny_it201.{transcription,render,classm}.json`. Summary: three "Landing round (2026-11-14)" sections
in `reviews/2025/transcription/adjudication/ny_it201.md` (new; there is no New York adjudication directory).
`check_logs.py --jurisdiction ny` shows no open ruling for ny_it201 in any of the three logs.

| kind | lines | counts |
| --- | --- | --- |
| transcription | C, 1, 79 | 2 representation (C: a federal Yes refuses the federal return, so item C is always the New York question on a completed return; 79: no overpayment, nothing to apply), 1 ambiguity (1: `amb.ny.2025.whole_dollars`, the reply keeps cents) |
| render | C, 53 | 2 scope (C: the spouse and dual-status cases come only through sa.dependent Yes, which is refused; 53: UBT and accumulation distribution credits come through Schedule C or a Schedule K-1, which scope.k1 refuses, and the part-year child care credit through part-year City residence, which is refused) |
| class M | 97 of 98 (one already ruled) | 75 interface gap, 22 ambiguity; all dropped from `fixtures/ny/2025/classm.json` |

Class M patterns:

- **75 lines, interface gap (cases 1, 2, 3, 4, 6).** The prompt's given amounts include fourteen "this document,
  line (39)" and one "(47a)", noted as the shared tax computation, which are the rate-schedule instances on the exact
  amount (ny_rs, ny_tcw, ny_city_rs). Lines 39 and 47a read the Tax Tables (`table_lookup`), which `classm.ts` does
  not count as the shared computation and the pages do not include, so the reply copied the given amount and was $1
  off on 39 and 47a and every line below. The engine matches the published table row in each case (checked in
  `sources/ny/2025/ny_it201_tax_tables.txt`).
- **22 lines, ambiguity (cases 1 to 5).** The NYC school tax credit rate-reduction products and the sales and use tax
  chart's top-row product: the engine rounds them where computed (C4); the reply keeps cents on the helper. The
  printed lines (69a, 59) agree in every case.

Finding:

- **BUG-0641, low (tool, not the engine).** `engine/src/classm.ts` buildJob gives only definition
  lines as the shared tax computation, so a New York form's Tax Table lookups are left to the model without the
  tables; `tools/transcription/classm.py` given_name names this document's lines by printed number alone, so the
  fifteen (39)/(47a) amounts are indistinguishable. Fix: give a `table_lookup` line over a tax table as a
  shared-computation result and drop it from the lines to fill; name this document's given lines by handle and
  label. Rerun ny_it201 class M at its next real change. No completed return is affected.

No line left open.
