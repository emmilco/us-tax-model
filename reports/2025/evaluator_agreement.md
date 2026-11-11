# Evaluator agreement — TypeScript engine vs Lean reference

Every fixture case and 400 generated whole returns (`generate.ts` `sampleReturns`, fast-check, seed 7) were evaluated
by both independently written evaluators; every root form line and every line of every confirmed collection entry
was compared (money cents, counts, rates, booleans, enums, full refusals; unknowns compared by kind).

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

| Kind | Fixture cases | Generated returns |
| --- | --- | --- |
| bool | 1216390 | 354029 |
| count | 161405 | 41545 |
| enum | 19679 | 10288 |
| money | 2553317 | 629458 |
| rate | 24531 | 6758 |
| refusal | 207326 | 131319 |
| unknown | 683934 | 74204 |
| all | 4866582 | 1247601 |

Not compared. Each of these counts as a difference and fails the run.

| Reason | Count |
| --- | --- |
| Cases the Lean evaluator gave no values for | 0 |
| Line values only one evaluator gave | 0 |
| Line values the Lean evaluator ran out of steps on | 0 |
