# Evaluator agreement — TypeScript engine vs Lean reference

Every fixture case and 400 generated whole returns (`generate.ts` `sampleReturns`, fast-check, seed 7: the corpus of the properties check) were evaluated
by both independently written evaluators; every root form line and every line of every confirmed collection entry
was compared (money cents, counts, rates, booleans, enums, full refusals; for an unknown, the missing input it names,
the lower bound of a partial count and whether it awaits a refusal gate's answer).

This is the federal run. Its cases are the federal fixture cases and federal generated returns; none gives a New York
answer. Both evaluators read the whole build, federal and New York documents alike, so the lines of the New York
documents are compared here too: 1097605 of the 13183119 values, of which 620936 are unknown for lack of New York answers
and 476669 have a value (a constant, a figure from federal lines only, or a refusal). The New York run (`compare --ny`,
`reports/ny/2025/evaluator_agreement.md`) compares the New York lines on cases that give New York answers.

| Metric | Value |
| --- | --- |
| Cases | 3145 |
| Fixture cases | 2745 |
| Generated returns | 400 |
| Line values compared | 13183119 |
| Cases with differences | 0 |
| Result | **agreement on every value** |

Line values compared, by the kind of the value. An unknown is a line with no value (an answer it needs was not
given, for example); the two evaluators agree that it is unknown, on the missing input it names, on the lower bound of a
partial count and on whether it awaits a refusal gate's answer, which the interview reads; its reason is not compared.

The last two columns count, among them, the lines of the New York documents.

| Kind | Fixture cases | Generated returns | New York lines, fixture cases | New York lines, generated returns |
| --- | --- | --- | --- | --- |
| bool | 3681353 | 672382 | 127220 | 15920 |
| count | 322874 | 47963 | 21640 | 2961 |
| enum | 74187 | 22158 | 0 | 0 |
| money | 5231526 | 705850 | 176483 | 22616 |
| rate | 48178 | 7998 | 0 | 0 |
| refusal | 477754 | 189119 | 84679 | 25150 |
| unknown | 1468755 | 233022 | 547983 | 72953 |
| all | 11304627 | 1878492 | 958005 | 139600 |

Not compared. Each of these counts as a difference and fails the run.

| Reason | Count |
| --- | --- |
| Cases the Lean evaluator gave no values for | 0 |
| Line values only one evaluator gave | 0 |
| Line values the Lean evaluator ran out of steps on | 0 |
