# Mutation score — implemented worksheets

Single-atom mutations applied to the canonical data; a mutant is killed if the
build-time checker fails on it or if any fixture case's value changes. Fixture
expectations are the recorded values checked in the previous run (the same values
the fixture test compares).

| Metric | Value |
| --- | --- |
| Mutants | 235 |
| Killed by the checker | 5 |
| Killed by fixtures | 220 |
| Surviving | 10 (10 provably equivalent) |
| Mutation score (raw) | 95.7% |
| Mutation score (equivalent mutants excluded) | 100.0% |

## Surviving — classified equivalent

- `operand.qdcg.qdcg.line8.line7` (replace an operand, qdcg.qdcg.line8): Provably equivalent: line 8 is min(line 5, line 7) and line 7 is min(line 1, line 6) with line 5 ≤ line 1; min(line 5, min(line 1, line 6)) = min(line 5, line 6), so substituting line 6 for line 7 cannot change any value.
- `operand.qdcg.qdcg.line12.line11` (replace an operand, qdcg.qdcg.line12): Provably equivalent: line 11 is 'Enter the amount from line 9' (a copy), so the substituted operand is the same value at every input.
- `operand.sd.sd.line5.zero` (replace an operand, sd.sd.line5): Both source lines are zero after identical unsupported-source/carryover gates. The destination checks the same gates before either source is evaluated.
- `operand.sd.sd.line6.zero` (replace an operand, sd.sd.line6): Both source lines are zero after identical unsupported-source/carryover gates. The destination checks the same gates before either source is evaluated.
- `operand.sd.sd.line11.zero` (replace an operand, sd.sd.line11): Both source lines are zero after identical unsupported-source/carryover gates. The destination checks the same gates before either source is evaluated.
- `operand.sd.sd.line12.zero` (replace an operand, sd.sd.line12): Both source lines are zero after identical unsupported-source/carryover gates. The destination checks the same gates before either source is evaluated.
- `operand.sd.sd.line14.zero` (replace an operand, sd.sd.line14): Both source lines are zero after identical unsupported-source/carryover gates. The destination checks the same gates before either source is evaluated.
- `operand.sd.sd.line7.line4` (replace an operand, sd.sd.line7): Both source lines are identically zero with identical refusal gates; substitution preserves known, unknown and refused values.
- `operand.sd.sd.line7.line5` (replace an operand, sd.sd.line7): Both source lines are identically zero with identical refusal gates; substitution preserves known, unknown and refused values.
- `operand.sd.sd.line7.line6` (replace an operand, sd.sd.line7): Both source lines are identically zero with identical refusal gates; substitution preserves known, unknown and refused values.
