# Evaluator agreement — TypeScript engine vs Lean reference

Every fixture case and 400 generated whole returns with New York answers (`generate.ts` `nyReturnArbitrary`, fast-check, seed 7: the corpus of the properties check) were evaluated
by both independently written evaluators; every root form line and every line of every confirmed collection entry
was compared (money cents, counts, rates, booleans, enums, full refusals; for an unknown, the missing input it names,
the lower bound of a partial count and whether it awaits a refusal gate's answer).

This is the New York run. Its cases are the New York fixture cases and the generated returns of the federal run,
each with the answers of the New York documents added. Both evaluators read the whole build, federal and New York
documents alike, so the lines of the federal documents are compared here too: of the 3995884 values, 297956 are lines of
the New York documents (28428 of them unknown) and 3697928 are lines of the federal documents. The federal run
(`compare`, `reports/2025/evaluator_agreement.md`) compares every line on the federal fixture cases and on the same
generated returns without New York answers.

| Metric | Value |
| --- | --- |
| Cases | 802 |
| Fixture cases | 402 |
| Generated returns | 400 |
| Line values compared | 3995884 |
| Cases with differences | 0 |
| Result | **agreement on every value** |

Line values compared, by the kind of the value. An unknown is a line with no value (an answer it needs was not
given, for example); the two evaluators agree that it is unknown, on the missing input it names, on the lower bound of a
partial count and on whether it awaits a refusal gate's answer, which the interview reads; its reason is not compared.

The last two columns count, among them, the lines of the New York documents.

| Kind | Fixture cases | Generated returns | New York lines, fixture cases | New York lines, generated returns |
| --- | --- | --- | --- | --- |
| bool | 782368 | 731667 | 59410 | 60838 |
| count | 52598 | 50560 | 3616 | 3269 |
| enum | 14325 | 22450 | 0 | 0 |
| money | 802485 | 732355 | 60743 | 44862 |
| rate | 7076 | 8285 | 0 | 0 |
| refusal | 11594 | 197257 | 8314 | 28476 |
| unknown | 404882 | 177982 | 15961 | 12467 |
| all | 2075328 | 1920556 | 148044 | 149912 |

Not compared. Each of these counts as a difference and fails the run.

| Reason | Count |
| --- | --- |
| Cases the Lean evaluator gave no values for | 0 |
| Line values only one evaluator gave | 0 |
| Line values the Lean evaluator ran out of steps on | 0 |
