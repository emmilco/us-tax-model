# Evaluator agreement — TypeScript engine vs Lean reference

Every fixture case and 400 generated whole returns with New York answers (`generate.ts` `nyReturnArbitrary`, fast-check, seed 7: the corpus of the properties check) were evaluated
by both independently written evaluators; every root form line and every line of every confirmed collection entry
was compared (money cents, counts, rates, booleans, enums, full refusals; for an unknown, the missing input it names,
the lower bound of a partial count and whether it awaits a refusal gate's answer).

This is the New York run. Its cases are the New York fixture cases and the generated returns of the federal run,
each with the answers of the New York documents added. Both evaluators read the whole build, federal and New York
documents alike, so the lines of the federal documents are compared here too: of the 3836280 values, 280470 are lines of
the New York documents (24835 of them unknown) and 3555810 are lines of the federal documents. The federal run
(`compare`, `reports/2025/evaluator_agreement.md`) compares every line on the federal fixture cases and on the same
generated returns without New York answers.

| Metric | Value |
| --- | --- |
| Cases | 782 |
| Fixture cases | 382 |
| Generated returns | 400 |
| Line values compared | 3836280 |
| Cases with differences | 0 |
| Result | **agreement on every value** |

Line values compared, by the kind of the value. An unknown is a line with no value (an answer it needs was not
given, for example); the two evaluators agree that it is unknown, on the missing input it names, on the lower bound of a
partial count and on whether it awaits a refusal gate's answer, which the interview reads; its reason is not compared.

The last two columns count, among them, the lines of the New York documents.

| Kind | Fixture cases | Generated returns | New York lines, fixture cases | New York lines, generated returns |
| --- | --- | --- | --- | --- |
| bool | 723332 | 712756 | 52760 | 56294 |
| count | 47217 | 47963 | 3054 | 2961 |
| enum | 13736 | 22158 | 0 | 0 |
| money | 752614 | 728253 | 60853 | 45019 |
| rate | 6699 | 7998 | 0 | 0 |
| refusal | 9834 | 191776 | 6887 | 27807 |
| unknown | 399244 | 172700 | 12204 | 12631 |
| all | 1952676 | 1883604 | 135758 | 144712 |

Not compared. Each of these counts as a difference and fails the run.

| Reason | Count |
| --- | --- |
| Cases the Lean evaluator gave no values for | 0 |
| Line values only one evaluator gave | 0 |
| Line values the Lean evaluator ran out of steps on | 0 |
