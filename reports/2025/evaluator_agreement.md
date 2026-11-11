# Evaluator agreement — TypeScript engine vs Lean reference

Every fixture case and 400 generated whole returns (`generate.ts` `sampleReturns`, fast-check, seed 7: the corpus of the properties check) were evaluated
by both independently written evaluators; every root form line and every line of every confirmed collection entry
was compared (money cents, counts, rates, booleans, enums, full refusals; unknowns compared by kind).

This is the federal run. Its cases are the federal fixture cases and federal generated returns; none gives a New York
answer. Both evaluators read the whole build, federal and New York documents alike, so the lines of the New York
documents are compared here too: 605920 of the 6115883 values, of which 388668 are unknown for lack of New York answers
and 217252 have a value (a constant, a figure from federal lines only, or a refusal). The New York run (`compare --ny`,
`reports/ny/2025/evaluator_agreement.md`) compares the New York lines on cases that give New York answers.

| Metric | Value |
| --- | --- |
| Cases | 2164 |
| Fixture cases | 1764 |
| Generated returns | 400 |
| Line values compared | 6115883 |
| Cases with differences | 0 |
| Result | **agreement on every value** |

Line values compared, by the kind of the value. An unknown is a line with no value (an answer it needs was not
given, for example); the two evaluators agree that it is unknown, and its reason is not compared.

The last two columns count, among them, the lines of the New York documents.

| Kind | Fixture cases | Generated returns | New York lines, fixture cases | New York lines, generated returns |
| --- | --- | --- | --- | --- |
| bool | 1221121 | 357697 | 29674 | 6144 |
| count | 161060 | 41545 | 10376 | 2210 |
| enum | 19649 | 10288 | 0 | 0 |
| money | 2549777 | 629458 | 88461 | 19096 |
| rate | 24468 | 6758 | 0 | 0 |
| refusal | 206268 | 131886 | 39364 | 21927 |
| unknown | 681704 | 74204 | 326045 | 62623 |
| all | 4864047 | 1251836 | 493920 | 112000 |

Not compared. Each of these counts as a difference and fails the run.

| Reason | Count |
| --- | --- |
| Cases the Lean evaluator gave no values for | 0 |
| Line values only one evaluator gave | 0 |
| Line values the Lean evaluator ran out of steps on | 0 |
