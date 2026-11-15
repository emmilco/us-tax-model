# Lane land3-adj1: adjudication of f8962 (landing round, 2026-11-14)

Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. The lane made no model calls and no paid reviews.

## What was ruled

There were 89 open disagreements in `.transcription/logs/2025/transcription/f8962.md`: lines 7 to 29, the line-scoped
pass 0adff78003b5. All 89 were ruled with `tools/transcription/rule.py` (rulings: `/tmp/land3-adj1/f8962.json`). The round
is summarised in `reviews/2025/transcription/adjudication/f8962.md`, "Landing round (2026-11-14)".

Counts: model error (+ scope) 89. Findings: none. Left open: none.

## Evidence

- The executable triage record of the pass (`.transcription/triage/2025/f8962.json`).
- A scratch rerun of the same evaluator with the witness cap lifted (`/tmp/land3-adj1/triage/f8962.json`; identical counts).
- On every line, every completed-return difference is on a record where the project hides the line. Where the project
  shows a line on a completed return, no value differs.
- Triage applies the project's display condition only, so the reply's own display conditions were ruled by reading its
  expressions.

## The limbs of the reply

- **M1, every line from 9 on.** The reply reads `f8962.married_this_year` on every filing status, through line 9 and then
  line 10. The interview asks it only on joint returns, and i8962 p. 13, Table 4, question 3 limits the alternative
  calculation to joint filers. So the reply needs an answer that is never asked, on single, head of household and
  qualifying surviving spouse returns.
- **V1, lines 7, 8a, 8b and 11(c).** The reply never tests `f8962.any`, although the request tells it to. So these lines
  show on returns with no Form 1095-A.
- **V2, the (a), (b), (d) and (e) columns of line 11 and lines 12 to 23.** Below 100% of the poverty line with no APTC,
  i8962 p. 10 says "stop; do not complete Form 8962". The reply still shows nonzero amounts there.
- **V3, the (d) and (e) columns.** For a filer who is not an applicable taxpayer but had APTC, the reply shows a PTC
  allowed beside its own line 24 of zero. The project's reading is recorded in amb.2025.ptc_not_applicable (D7(a)).
- **Scope.** The project refuses at its cited gates:
  - a Form 1095-A marked VOID (`f8962.void_form`);
  - married filing separately (`s3.mfs`);
  - the alien route below 100% (`f8962.alien_branch`);
  - `f8962.two_counted`;
  - `f8962.a_zero_paid`.

  The 19 value differences are all on refused returns: line 10 has 1, and lines 24 and 26 have 9 each.

## Change of class from earlier rounds

Earlier rounds ruled the reply's display conditions an interface gap (T-163). That task is done: the
source-only-computation-v3 request requires `shown_when`, and the line-scoped request names `f8962.any` as the condition
to test. So the display limbs are now ruled model errors. The coordinator may want to know this before comparing these
rulings with the 2026-11-11 round.
