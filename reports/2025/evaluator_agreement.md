# Evaluator agreement — TypeScript engine vs Lean reference

Every fixture case and 400 generated whole returns (`generate.ts` `sampleReturns`, fast-check, seed 7: the corpus of the properties check) were evaluated
by both independently written evaluators; every root form line and every line of every confirmed collection entry
was compared (money cents, counts, rates, booleans, enums, full refusals; unknowns compared by kind).

This is the federal run. Its cases are the federal fixture cases and federal generated returns; none gives a New York
answer. Both evaluators read the whole build, federal and New York documents alike, so the lines of the New York
documents are compared here too: 607040 of the 6114183 values, of which 389308 are unknown for lack of New York answers
and 217732 have a value (a constant, a figure from federal lines only, or a refusal). The New York run (`compare --ny`,
`reports/ny/2025/evaluator_agreement.md`) compares the New York lines on cases that give New York answers.

| Metric | Value |
| --- | --- |
| Cases | 2168 |
| Fixture cases | 1768 |
| Generated returns | 400 |
| Line values compared | 6114183 |
| Cases with differences | 0 |
| Result | **agreement on every value** |

Line values compared, by the kind of the value. An unknown is a line with no value (an answer it needs was not
given, for example); the two evaluators agree that it is unknown, and its reason is not compared.

The last two columns count, among them, the lines of the New York documents.

| Kind | Fixture cases | Generated returns | New York lines, fixture cases | New York lines, generated returns |
| --- | --- | --- | --- | --- |
| bool | 1216390 | 354029 | 29716 | 6144 |
| count | 161405 | 41545 | 10400 | 2210 |
| enum | 19679 | 10288 | 0 | 0 |
| money | 2553317 | 629458 | 88607 | 19096 |
| rate | 24531 | 6758 | 0 | 0 |
| refusal | 207326 | 131319 | 39632 | 21927 |
| unknown | 683934 | 74204 | 326685 | 62623 |
| all | 4866582 | 1247601 | 495040 | 112000 |

Not compared. Each of these counts as a difference and fails the run.

| Reason | Count |
| --- | --- |
| Cases the Lean evaluator gave no values for | 0 |
| Line values only one evaluator gave | 0 |
| Line values the Lean evaluator ran out of steps on | 0 |
