# Evaluator agreement — TypeScript engine vs Lean reference

Every fixture case and 400 generated whole returns (`generate.ts` `sampleReturns`, fast-check, seed 7: the corpus of the properties check) were evaluated
by both independently written evaluators; every root form line and every line of every confirmed collection entry
was compared (money cents, counts, rates, booleans, enums, full refusals; unknowns compared by kind).

This is the federal run. Its cases are the federal fixture cases and federal generated returns; none gives a New York
answer. Both evaluators read the whole build, federal and New York documents alike, so the lines of the New York
documents are compared here too: 939888 of the 11907455 values, of which 554541 are unknown for lack of New York answers
and 385347 have a value (a constant, a figure from federal lines only, or a refusal). The New York run (`compare --ny`,
`reports/ny/2025/evaluator_agreement.md`) compares the New York lines on cases that give New York answers.

| Metric | Value |
| --- | --- |
| Cases | 2928 |
| Fixture cases | 2528 |
| Generated returns | 400 |
| Line values compared | 11907455 |
| Cases with differences | 0 |
| Result | **agreement on every value** |

Line values compared, by the kind of the value. An unknown is a line with no value (an answer it needs was not
given, for example); the two evaluators agree that it is unknown, and its reason is not compared.

The last two columns count, among them, the lines of the New York documents.

| Kind | Fixture cases | Generated returns | New York lines, fixture cases | New York lines, generated returns |
| --- | --- | --- | --- | --- |
| bool | 3204610 | 642729 | 96934 | 13283 |
| count | 287020 | 47811 | 19890 | 3005 |
| enum | 69746 | 22346 | 0 | 0 |
| money | 4783554 | 717055 | 144190 | 20975 |
| rate | 44819 | 8291 | 0 | 0 |
| refusal | 414563 | 195751 | 62419 | 24651 |
| unknown | 1282123 | 187037 | 488055 | 66486 |
| all | 10086435 | 1821020 | 811488 | 128400 |

Not compared. Each of these counts as a difference and fails the run.

| Reason | Count |
| --- | --- |
| Cases the Lean evaluator gave no values for | 0 |
| Line values only one evaluator gave | 0 |
| Line values the Lean evaluator ran out of steps on | 0 |
