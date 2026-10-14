# Mutation score — Stage 1 worksheets

Single-atom mutations applied to the canonical data; a mutant is killed if the
build-time checker fails on it or if any fixture case's value changes. Fixture
expectations are the recorded values checked in the previous run (the same values
the fixture test compares).

| Metric | Value |
| --- | --- |
| Mutants | 100 |
| Killed by the checker | 9 |
| Killed by fixtures | 89 |
| Surviving | 2 (2 provably equivalent) |
| Mutation score (raw) | 98.0% |
| Mutation score (equivalent mutants excluded) | 100.0% |

## Surviving — classified equivalent

- `operand.qdcg.qdcg.line8.line7` (replace an operand, qdcg.qdcg.line8): Provably equivalent: line 8 is min(line 5, line 7) and line 7 is min(line 1, line 6) with line 5 ≤ line 1; min(line 5, min(line 1, line 6)) = min(line 5, line 6), so substituting line 6 for line 7 cannot change any value.
- `operand.qdcg.qdcg.line12.line11` (replace an operand, qdcg.qdcg.line12): Provably equivalent: line 11 is 'Enter the amount from line 9' (a copy), so the substituted operand is the same value at every input.
