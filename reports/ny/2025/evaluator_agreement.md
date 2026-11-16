# Evaluator agreement — TypeScript engine vs Lean reference

Every fixture case and 400 generated whole returns with New York answers (`generate.ts` `nyReturnArbitrary`, fast-check, seed 7: the corpus of the properties check) were evaluated
by both independently written evaluators; every root form line and every line of every confirmed collection entry
was compared (money cents, counts, rates, booleans, enums, full refusals; unknowns compared by kind).

This is the New York run. Its cases are the New York fixture cases and the generated returns of the federal run,
each with the answers of the New York documents added. Both evaluators read the whole build, federal and New York
documents alike, so the lines of the federal documents are compared here too: of the 3145896 values, 248613 are lines of
the New York documents (16622 of them unknown) and 2897283 are lines of the federal documents. The federal run
(`compare`, `reports/2025/evaluator_agreement.md`) compares every line on the federal fixture cases and on the same
generated returns without New York answers.

| Metric | Value |
| --- | --- |
| Cases | 757 |
| Fixture cases | 357 |
| Generated returns | 400 |
| Line values compared | 3145896 |
| Cases with differences | 0 |
| Result | **agreement on every value** |

Line values compared, by the kind of the value. An unknown is a line with no value (an answer it needs was not
given, for example); the two evaluators agree that it is unknown, and its reason is not compared.

The last two columns count, among them, the lines of the New York documents.

| Kind | Fixture cases | Generated returns | New York lines, fixture cases | New York lines, generated returns |
| --- | --- | --- | --- | --- |
| bool | 601361 | 620072 | 43233 | 48447 |
| count | 41002 | 47134 | 2854 | 3007 |
| enum | 11619 | 20553 | 0 | 0 |
| money | 597936 | 673005 | 54422 | 45219 |
| rate | 4500 | 6561 | 0 | 0 |
| refusal | 8149 | 176366 | 5683 | 29126 |
| unknown | 294455 | 43183 | 10187 | 6435 |
| all | 1559022 | 1586874 | 116379 | 132234 |

Not compared. Each of these counts as a difference and fails the run.

| Reason | Count |
| --- | --- |
| Cases the Lean evaluator gave no values for | 0 |
| Line values only one evaluator gave | 0 |
| Line values the Lean evaluator ran out of steps on | 0 |
