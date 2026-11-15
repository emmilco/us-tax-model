# Evaluator agreement — TypeScript engine vs Lean reference

Every fixture case and 400 generated whole returns (`generate.ts` `sampleReturns`, fast-check, seed 7: the corpus of the properties check) were evaluated
by both independently written evaluators; every root form line and every line of every confirmed collection entry
was compared (money cents, counts, rates, booleans, enums, full refusals; unknowns compared by kind).

This is the federal run. Its cases are the federal fixture cases and federal generated returns; none gives a New York
answer. Both evaluators read the whole build, federal and New York documents alike, so the lines of the New York
documents are compared here too: 772326 of the 8157659 values, of which 454033 are unknown for lack of New York answers
and 318293 have a value (a constant, a figure from federal lines only, or a refusal). The New York run (`compare --ny`,
`reports/ny/2025/evaluator_agreement.md`) compares the New York lines on cases that give New York answers.

| Metric | Value |
| --- | --- |
| Cases | 2406 |
| Fixture cases | 2006 |
| Generated returns | 400 |
| Line values compared | 8157659 |
| Cases with differences | 0 |
| Result | **agreement on every value** |

Line values compared, by the kind of the value. An unknown is a line with no value (an answer it needs was not
given, for example); the two evaluators agree that it is unknown, and its reason is not compared.

The last two columns count, among them, the lines of the New York documents.

| Kind | Fixture cases | Generated returns | New York lines, fixture cases | New York lines, generated returns |
| --- | --- | --- | --- | --- |
| bool | 2214091 | 563414 | 75613 | 13431 |
| count | 197507 | 44162 | 15678 | 3005 |
| enum | 47051 | 18817 | 0 | 0 |
| money | 2989087 | 635898 | 113128 | 21143 |
| rate | 27119 | 6048 | 0 | 0 |
| refusal | 254434 | 141247 | 52101 | 24194 |
| unknown | 917289 | 101495 | 387406 | 66627 |
| all | 6646578 | 1511081 | 643926 | 128400 |

Not compared. Each of these counts as a difference and fails the run.

| Reason | Count |
| --- | --- |
| Cases the Lean evaluator gave no values for | 0 |
| Line values only one evaluator gave | 0 |
| Line values the Lean evaluator ran out of steps on | 0 |
