# Evaluator agreement — TypeScript engine vs Lean reference

Every fixture case and 400 generated whole returns with New York answers (`generate.ts` `nyReturnArbitrary`, fast-check, seed 7) were evaluated
by both independently written evaluators; every root form line and every line of every confirmed collection entry
was compared (money cents, counts, rates, booleans, enums, full refusals; unknowns compared by kind).

| Metric | Value |
| --- | --- |
| Cases | 738 |
| Fixture cases | 338 |
| Generated returns | 400 |
| Line values compared | 2457184 |
| Cases with differences | 0 |
| Result | **agreement on every value** |

Line values compared, by the kind of the value. An unknown is a line with no value (an answer it needs was not
given, for example); the two evaluators agree that it is unknown, and its reason is not compared.

| Kind | Fixture cases | Generated returns |
| --- | --- | --- |
| bool | 376244 | 384715 |
| count | 34021 | 41545 |
| enum | 3674 | 10288 |
| money | 519764 | 660960 |
| rate | 4273 | 6758 |
| refusal | 6480 | 135406 |
| unknown | 261293 | 11763 |
| all | 1205749 | 1251435 |

Not compared. Each of these counts as a difference and fails the run.

| Reason | Count |
| --- | --- |
| Cases the Lean evaluator gave no values for | 0 |
| Line values only one evaluator gave | 0 |
| Line values the Lean evaluator ran out of steps on | 0 |
