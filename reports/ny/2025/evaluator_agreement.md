# Evaluator agreement — TypeScript engine vs Lean reference

Every fixture case and 400 generated whole returns with New York answers (`generate.ts` `nyReturnArbitrary`, fast-check, seed 7: the corpus of the properties check) were evaluated
by both independently written evaluators; every root form line and every line of every confirmed collection entry
was compared (money cents, counts, rates, booleans, enums, full refusals; unknowns compared by kind).

This is the New York run. Its cases are the New York fixture cases and the generated returns of the federal run,
each with the answers of the New York documents added. Both evaluators read the whole build, federal and New York
documents alike, so the lines of the federal documents are compared here too: of the 2457184 values, 212142 are lines of
the New York documents (9380 of them unknown) and 2245042 are lines of the federal documents. The federal run
(`compare`, `reports/2025/evaluator_agreement.md`) compares every line on the federal fixture cases and on the same
generated returns without New York answers.

| Metric | Value |
| --- | --- |
| Cases | 738 |
| Fixture cases | 338 |
| Generated returns | 400 |
| Line values compared | 2457184 |
| Cases with differences | 0 |
| Result | **agreement on every value** |

Line values compared, by the kind of the value. An unknown is a line with no value (an answer it needs was not
given, for example); the two evaluators agree that it is unknown, and its reason is not compared.

The last two columns count, among them, the lines of the New York documents.

| Kind | Fixture cases | Generated returns | New York lines, fixture cases | New York lines, generated returns |
| --- | --- | --- | --- | --- |
| bool | 375975 | 384715 | 29556 | 36830 |
| count | 34021 | 41545 | 2026 | 2210 |
| enum | 3674 | 10288 | 0 | 0 |
| money | 519764 | 660960 | 51363 | 50598 |
| rate | 4273 | 6758 | 0 | 0 |
| refusal | 6480 | 135406 | 4165 | 26014 |
| unknown | 261562 | 11763 | 9198 | 182 |
| all | 1205749 | 1251435 | 96308 | 115834 |

Not compared. Each of these counts as a difference and fails the run.

| Reason | Count |
| --- | --- |
| Cases the Lean evaluator gave no values for | 0 |
| Line values only one evaluator gave | 0 |
| Line values the Lean evaluator ran out of steps on | 0 |
