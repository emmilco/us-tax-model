# Evaluator agreement — TypeScript engine vs Lean reference

Every fixture case and 400 generated whole returns (`generate.ts` `sampleReturns`, fast-check, seed 7: the corpus of the properties check) were evaluated
by both independently written evaluators; every root form line and every line of every confirmed collection entry
was compared (money cents, counts, rates, booleans, enums, full refusals; for an unknown, the missing input it names,
the lower bound of a partial count and whether it awaits a refusal gate's answer).

This is the federal run. Its cases are the federal fixture cases and federal generated returns; none gives a New York
answer. Both evaluators read the whole build, federal and New York documents alike, so the lines of the New York
documents are compared here too: 1167088 of the 13724592 values, of which 646735 are unknown for lack of New York answers
and 520353 have a value (a constant, a figure from federal lines only, or a refusal). The New York run (`compare --ny`,
`reports/ny/2025/evaluator_agreement.md`) compares the New York lines on cases that give New York answers.

| Metric | Value |
| --- | --- |
| Cases | 3224 |
| Fixture cases | 2824 |
| Generated returns | 400 |
| Line values compared | 13724592 |
| Cases with differences | 0 |
| Result | **agreement on every value** |

Line values compared, by the kind of the value. An unknown is a line with no value (an answer it needs was not
given, for example); the two evaluators agree that it is unknown, on the missing input it names, on the lower bound of a
partial count and on whether it awaits a refusal gate's answer, which the interview reads; its reason is not compared.

The last two columns count, among them, the lines of the New York documents.

| Kind | Fixture cases | Generated returns | New York lines, fixture cases | New York lines, generated returns |
| --- | --- | --- | --- | --- |
| bool | 3909133 | 689857 | 155109 | 19028 |
| count | 352557 | 50560 | 25070 | 3269 |
| enum | 76118 | 22450 | 0 | 0 |
| money | 5431646 | 710091 | 181639 | 22598 |
| rate | 49404 | 8285 | 0 | 0 |
| refusal | 505147 | 193763 | 88658 | 24982 |
| unknown | 1485143 | 240438 | 571812 | 74923 |
| all | 11809148 | 1915444 | 1022288 | 144800 |

Not compared. Each of these counts as a difference and fails the run.

| Reason | Count |
| --- | --- |
| Cases the Lean evaluator gave no values for | 0 |
| Line values only one evaluator gave | 0 |
| Line values the Lean evaluator ran out of steps on | 0 |
