# Evaluator agreement — TypeScript engine vs Lean reference

Every fixture case and 400 generated whole returns (`generate.ts` `sampleReturns`, fast-check, seed 7: the corpus of the properties check) were evaluated
by both independently written evaluators; every root form line and every line of every confirmed collection entry
was compared (money cents, counts, rates, booleans, enums, full refusals; unknowns compared by kind).

This is the federal run. Its cases are the federal fixture cases and federal generated returns; none gives a New York
answer. Both evaluators read the whole build, federal and New York documents alike, so the lines of the New York
documents are compared here too: 786129 of the 8640148 values, of which 462192 are unknown for lack of New York answers
and 323937 have a value (a constant, a figure from federal lines only, or a refusal). The New York run (`compare --ny`,
`reports/ny/2025/evaluator_agreement.md`) compares the New York lines on cases that give New York answers.

| Metric | Value |
| --- | --- |
| Cases | 2449 |
| Fixture cases | 2049 |
| Generated returns | 400 |
| Line values compared | 8640148 |
| Cases with differences | 0 |
| Result | **agreement on every value** |

Line values compared, by the kind of the value. An unknown is a line with no value (an answer it needs was not
given, for example); the two evaluators agree that it is unknown, and its reason is not compared.

The last two columns count, among them, the lines of the New York documents.

| Kind | Fixture cases | Generated returns | New York lines, fixture cases | New York lines, generated returns |
| --- | --- | --- | --- | --- |
| bool | 2337433 | 584987 | 77769 | 13362 |
| count | 214772 | 47134 | 16025 | 3007 |
| enum | 49163 | 20553 | 0 | 0 |
| money | 3203443 | 648782 | 115972 | 20996 |
| rate | 27901 | 6561 | 0 | 0 |
| refusal | 290392 | 171900 | 52146 | 24660 |
| unknown | 934004 | 103123 | 395817 | 66375 |
| all | 7057108 | 1583040 | 657729 | 128400 |

Not compared. Each of these counts as a difference and fails the run.

| Reason | Count |
| --- | --- |
| Cases the Lean evaluator gave no values for | 0 |
| Line values only one evaluator gave | 0 |
| Line values the Lean evaluator ran out of steps on | 0 |
