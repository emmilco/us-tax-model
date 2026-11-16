# Evaluator agreement — TypeScript engine vs Lean reference

Every fixture case and 400 generated whole returns with New York answers (`generate.ts` `nyReturnArbitrary`, fast-check, seed 7: the corpus of the properties check) were evaluated
by both independently written evaluators; every root form line and every line of every confirmed collection entry
was compared (money cents, counts, rates, booleans, enums, full refusals; unknowns compared by kind).

This is the New York run. Its cases are the New York fixture cases and the generated returns of the federal run,
each with the answers of the New York documents added. Both evaluators read the whole build, federal and New York
documents alike, so the lines of the federal documents are compared here too: of the 3629355 values, 248934 are lines of
the New York documents (17442 of them unknown) and 3380421 are lines of the federal documents. The federal run
(`compare`, `reports/2025/evaluator_agreement.md`) compares every line on the federal fixture cases and on the same
generated returns without New York answers.

| Metric | Value |
| --- | --- |
| Cases | 758 |
| Fixture cases | 358 |
| Generated returns | 400 |
| Line values compared | 3629355 |
| Cases with differences | 0 |
| Result | **agreement on every value** |

Line values compared, by the kind of the value. An unknown is a line with no value (an answer it needs was not
given, for example); the two evaluators agree that it is unknown, and its reason is not compared.

The last two columns count, among them, the lines of the New York documents.

| Kind | Fixture cases | Generated returns | New York lines, fixture cases | New York lines, generated returns |
| --- | --- | --- | --- | --- |
| bool | 657220 | 677933 | 43356 | 48487 |
| count | 43261 | 47811 | 2862 | 3005 |
| enum | 13164 | 22346 | 0 | 0 |
| money | 689655 | 741805 | 54507 | 45725 |
| rate | 6272 | 8291 | 0 | 0 |
| refusal | 8010 | 198863 | 5787 | 27763 |
| unknown | 386919 | 127805 | 10188 | 7254 |
| all | 1804501 | 1824854 | 116700 | 132234 |

Not compared. Each of these counts as a difference and fails the run.

| Reason | Count |
| --- | --- |
| Cases the Lean evaluator gave no values for | 0 |
| Line values only one evaluator gave | 0 |
| Line values the Lean evaluator ran out of steps on | 0 |
