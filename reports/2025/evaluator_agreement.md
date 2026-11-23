# Evaluator agreement — TypeScript engine vs Lean reference

Every fixture case and 400 generated whole returns (`generate.ts` `sampleReturns`, fast-check, seed 7: the corpus of the properties check) were evaluated
by both independently written evaluators; every root form line and every line of every confirmed collection entry
was compared (money cents, counts, rates, booleans, enums, full refusals; for an unknown, the missing input it names,
the lower bound of a partial count and whether it awaits a refusal gate's answer).

This is the federal run. Its cases are the federal fixture cases and federal generated returns; none gives a New York
answer. Both evaluators read the whole build, federal and New York documents alike, so the lines of the New York
documents are compared here too: 992445 of the 12411056 values, of which 588682 are unknown for lack of New York answers
and 403763 have a value (a constant, a figure from federal lines only, or a refusal). The New York run (`compare --ny`,
`reports/ny/2025/evaluator_agreement.md`) compares the New York lines on cases that give New York answers.

| Metric | Value |
| --- | --- |
| Cases | 3035 |
| Fixture cases | 2635 |
| Generated returns | 400 |
| Line values compared | 12411056 |
| Cases with differences | 0 |
| Result | **agreement on every value** |

Line values compared, by the kind of the value. An unknown is a line with no value (an answer it needs was not
given, for example); the two evaluators agree that it is unknown, on the missing input it names, on the lower bound of a
partial count and on whether it awaits a refusal gate's answer, which the interview reads; its reason is not compared.

The last two columns count, among them, the lines of the New York documents.

| Kind | Fixture cases | Generated returns | New York lines, fixture cases | New York lines, generated returns |
| --- | --- | --- | --- | --- |
| bool | 3362285 | 648150 | 103711 | 13362 |
| count | 298187 | 47921 | 20756 | 2948 |
| enum | 71492 | 22532 | 0 | 0 |
| money | 4961555 | 690044 | 152945 | 20847 |
| rate | 46375 | 8290 | 0 | 0 |
| refusal | 431646 | 194162 | 64451 | 24743 |
| unknown | 1402312 | 226105 | 519782 | 68900 |
| all | 10573852 | 1837204 | 861645 | 130800 |

Not compared. Each of these counts as a difference and fails the run.

| Reason | Count |
| --- | --- |
| Cases the Lean evaluator gave no values for | 0 |
| Line values only one evaluator gave | 0 |
| Line values the Lean evaluator ran out of steps on | 0 |
