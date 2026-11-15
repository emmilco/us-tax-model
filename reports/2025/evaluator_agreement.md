# Evaluator agreement — TypeScript engine vs Lean reference

Every fixture case and 400 generated whole returns (`generate.ts` `sampleReturns`, fast-check, seed 7: the corpus of the properties check) were evaluated
by both independently written evaluators; every root form line and every line of every confirmed collection entry
was compared (money cents, counts, rates, booleans, enums, full refusals; unknowns compared by kind).

This is the federal run. Its cases are the federal fixture cases and federal generated returns; none gives a New York
answer. Both evaluators read the whole build, federal and New York documents alike, so the lines of the New York
documents are compared here too: 771363 of the 8147388 values, of which 453379 are unknown for lack of New York answers
and 317984 have a value (a constant, a figure from federal lines only, or a refusal). The New York run (`compare --ny`,
`reports/ny/2025/evaluator_agreement.md`) compares the New York lines on cases that give New York answers.

| Metric | Value |
| --- | --- |
| Cases | 2403 |
| Fixture cases | 2003 |
| Generated returns | 400 |
| Line values compared | 8147388 |
| Cases with differences | 0 |
| Result | **agreement on every value** |

Line values compared, by the kind of the value. An unknown is a line with no value (an answer it needs was not
given, for example); the two evaluators agree that it is unknown, and its reason is not compared.

The last two columns count, among them, the lines of the New York documents.

| Kind | Fixture cases | Generated returns | New York lines, fixture cases | New York lines, generated returns |
| --- | --- | --- | --- | --- |
| bool | 2210860 | 563414 | 75514 | 13431 |
| count | 197214 | 44162 | 15655 | 3005 |
| enum | 46954 | 18817 | 0 | 0 |
| money | 2984699 | 635898 | 112965 | 21143 |
| rate | 27074 | 6048 | 0 | 0 |
| refusal | 254353 | 141247 | 52077 | 24194 |
| unknown | 915153 | 101495 | 386752 | 66627 |
| all | 6636307 | 1511081 | 642963 | 128400 |

Not compared. Each of these counts as a difference and fails the run.

| Reason | Count |
| --- | --- |
| Cases the Lean evaluator gave no values for | 0 |
| Line values only one evaluator gave | 0 |
| Line values the Lean evaluator ran out of steps on | 0 |
