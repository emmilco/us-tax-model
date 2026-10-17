# Mutation score — implemented worksheets

Single-atom mutations applied to the canonical data; a mutant is killed if the
build-time checker fails on it or if any fixture case's value changes. Fixture
expectations are the recorded values checked in the previous run (the same values
the fixture test compares).

| Metric | Value |
| --- | --- |
| Mutants | 791 |
| Killed by the checker | 45 |
| Killed by fixtures | 614 |
| Surviving | 132 (43 provably equivalent) |
| Mutation score (raw) | 83.3% |
| Mutation score (equivalent mutants excluded) | 88.1% |

## Surviving — classified equivalent

- `operand.f8959.f8959.line3.zero` (replace an operand, f8959.f8959.line3): Copy-chain identity: f8959.zero and f8959.line2 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8959.f8959.line8.zero` (replace an operand, f8959.f8959.line8): Copy-chain identity: f8959.zero and f8959.line3 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8959.f8959.line14.zero` (replace an operand, f8959.f8959.line14): Copy-chain identity: f8959.zero and f8959.line8 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8959.f8959.line23.zero` (replace an operand, f8959.f8959.line23): Copy-chain identity: f8959.zero and f8959.line14 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8959.f8959.line4.line2` (replace an operand, f8959.f8959.line4): Copy-chain identity: f8959.line2 and f8959.line23 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8959.f8959.line4.line3` (replace an operand, f8959.f8959.line4): Copy-chain identity: f8959.line3 and f8959.line23 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8960.f8960.line4a.zero` (replace an operand, f8960.f8960.line4a): Copy-chain identity: f8960.zero and f8960.line3 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8960.f8960.line4b.zero` (replace an operand, f8960.f8960.line4b): Copy-chain identity: f8960.zero and f8960.line4a expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8960.f8960.line5b.zero` (replace an operand, f8960.f8960.line5b): Copy-chain identity: f8960.zero and f8960.line4b expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8960.f8960.line5c.zero` (replace an operand, f8960.f8960.line5c): Copy-chain identity: f8960.zero and f8960.line5b expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8960.f8960.line6.zero` (replace an operand, f8960.f8960.line6): Copy-chain identity: f8960.zero and f8960.line5c expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8960.f8960.line7.zero` (replace an operand, f8960.f8960.line7): Copy-chain identity: f8960.zero and f8960.line6 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8960.f8960.line9c.zero` (replace an operand, f8960.f8960.line9c): Copy-chain identity: f8960.zero and f8960.line7 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8960.f8960.line10.zero` (replace an operand, f8960.f8960.line10): Copy-chain identity: f8960.zero and f8960.line9c expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8960.f8960.line4c.line4a` (replace an operand, f8960.f8960.line4c): Copy-chain identity: f8960.line4a and f8960.line10 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8960.f8960.line4c.line4b` (replace an operand, f8960.f8960.line4c): Copy-chain identity: f8960.line4b and f8960.line10 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8995.f8995.line9.line8` (replace an operand, f8995.f8995.line9): Copy-chain identity: f8995.line8 and f8995.line6 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.f8995a.f8995a.line31.line30` (replace an operand, f8995a.f8995a.line31): Copy-chain identity: f8995a.line30 and f8995a.line28 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.qdcg.qdcg.line8.line7` (replace an operand, qdcg.qdcg.line8): Provably equivalent: line 8 is min(line 5, line 7) and line 7 is min(line 1, line 6) with line 5 ≤ line 1; min(line 5, min(line 1, line 6)) = min(line 5, line 6), so substituting line 6 for line 7 cannot change any value.
- `operand.qdcg.qdcg.line12.line11` (replace an operand, qdcg.qdcg.line12): Copy-chain identity: qdcg.line11 and qdcg.line9 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s2.s2.line3.zero` (replace an operand, s2.s2.line3): Copy-chain identity: s2.zero and s2.line2 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s8812.s8812.line2b.zero` (replace an operand, s8812.s8812.line2b): Copy-chain identity: s8812.zero and s8812.line2a expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s8812.s8812.line2c.zero` (replace an operand, s8812.s8812.line2c): Copy-chain identity: s8812.zero and s8812.line2b expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s8812.s8812.line14.line13` (replace an operand, s8812.s8812.line14): Copy-chain identity: s8812.line13 and s8812.clw_a5 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s8812.s8812.eiw_5.zero` (replace an operand, s8812.s8812.eiw_5): Copy-chain identity: s8812.zero and s8812.eiw_4 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sa.sa.line3.line2` (replace an operand, sa.sa.line3): Copy-chain identity: sa.line2 and sa.agi expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sa.sa.line8b.zero` (replace an operand, sa.sa.line8b): Copy-chain identity: sa.zero and sa.line6 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sa.sa.line8c.zero` (replace an operand, sa.sa.line8c): Copy-chain identity: sa.zero and sa.line8b expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sa.sa.line13.zero` (replace an operand, sa.sa.line13): Copy-chain identity: sa.zero and sa.line8c expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sa.sa.line15.zero` (replace an operand, sa.sa.line15): Copy-chain identity: sa.zero and sa.line13 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sa.sa.line16.zero` (replace an operand, sa.sa.line16): Copy-chain identity: sa.zero and sa.line15 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sa.sa.line7.line6` (replace an operand, sa.sa.line7): Copy-chain identity: sa.line6 and sa.line16 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sd.sd.line5.zero` (replace an operand, sd.sd.line5): Copy-chain identity: sd.zero and sd.line4 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sd.sd.line6.zero` (replace an operand, sd.sd.line6): Copy-chain identity: sd.zero and sd.line5 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sd.sd.line11.zero` (replace an operand, sd.sd.line11): Copy-chain identity: sd.zero and sd.line6 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sd.sd.line12.zero` (replace an operand, sd.sd.line12): Copy-chain identity: sd.zero and sd.line11 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sd.sd.line14.zero` (replace an operand, sd.sd.line14): Copy-chain identity: sd.zero and sd.line12 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sd.sd.line7.line4` (replace an operand, sd.sd.line7): Copy-chain identity: sd.line4 and sd.line14 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sd.sd.line7.line5` (replace an operand, sd.sd.line7): Copy-chain identity: sd.line5 and sd.line14 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.sd.sd.line7.line6` (replace an operand, sd.sd.line7): Copy-chain identity: sd.line6 and sd.line14 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.u1250.u1250.line13.line9` (replace an operand, u1250.u1250.line13): Copy-chain identity: u1250.line9 and u1250.line16 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.u1250.u1250.line13.line10` (replace an operand, u1250.u1250.line13): Copy-chain identity: u1250.line10 and u1250.line16 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.u1250.u1250.line13.line12` (replace an operand, u1250.u1250.line13): Copy-chain identity: u1250.line12 and u1250.line16 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.

## Surviving — not yet explained

| Mutant | Kind | Location | Note |
| --- | --- | --- | --- |
| boundary.dependent.dependent.lived_half | replace strict greater-than with inclusive | dependent.dependent.lived_half |  |
| refusal.dependent.dependent.qualifying_child.0 | remove refusal | dependent.dependent.qualifying_child |  |
| refusal.dependent.dependent.qualifying_child.1 | remove refusal | dependent.dependent.qualifying_child |  |
| refusal.dependent.dependent.qualifying_child.2 | remove refusal | dependent.dependent.qualifying_child |  |
| refusal.dependent.dependent.qualifying_relative.0 | remove refusal | dependent.dependent.qualifying_relative |  |
| refusal.dependent.dependent.qualifying_relative.1 | remove refusal | dependent.dependent.qualifying_relative |  |
| refusal.dependent.dependent.qualifying_relative.2 | remove refusal | dependent.dependent.qualifying_relative |  |
| operand.f1040.f1040.line11b.line11a | replace an operand | f1040.f1040.line11b | f1040.line11a -> f1040.line9 (Dollars) |
| refusal.f1040.f1040.line12e.0 | remove refusal | f1040.f1040.line12e |  |
| operand.f1040.f1040.line14.line13b | replace an operand | f1040.f1040.line14 | f1040.line13b -> f1040.line10 (NonNegDollars) |
| refusal.f1040.f1040.line16.0 | remove refusal | f1040.f1040.line16 |  |
| refusal.f1040.f1040.line29.0 | remove refusal | f1040.f1040.line29 |  |
| refusal.f1040.f1040.line30.0 | remove refusal | f1040.f1040.line30 |  |
| operand.f4952.f4952.line3.line2 | replace an operand | f4952.f4952.line3 | f4952.line2 -> f4952.zero (NonNegDollars) |
| refusal.f4952.f4952.required.1 | remove refusal | f4952.f4952.required |  |
| refusal.f4952.f4952.required.2 | remove refusal | f4952.f4952.required |  |
| operand.f8959.f8959.line11.line9 | replace an operand | f8959.f8959.line11 | f8959.line9 -> f8959.line7 (NonNegDollars) |
| operand.f8959.f8959.line12.line11 | replace an operand | f8959.f8959.line12 | f8959.line11 -> f8959.line10 (NonNegDollars) |
| operand.f8959.f8959.line16.line14 | replace an operand | f8959.f8959.line16 | f8959.line14 -> f8959.line13 (NonNegDollars) |
| operand.f8959.f8959.line16.line15 | replace an operand | f8959.f8959.line16 | f8959.line15 -> f8959.line13 (NonNegDollars) |
| operand.f8959.f8959.line18.line13 | replace an operand | f8959.f8959.line18 | f8959.line13 -> f8959.line16 (NonNegDollars) |
| operand.f8959.f8959.line18.line17 | replace an operand | f8959.f8959.line18 | f8959.line17 -> f8959.line16 (NonNegDollars) |
| operand.f8960.f8960.line8.line5d | replace an operand | f8960.f8960.line8 | f8960.line5d -> f8960.line5a (Dollars) |
| operand.f8960.f8960.line9d.line9c | replace an operand | f8960.f8960.line9d | f8960.line9c -> f8960.line4c (NonNegDollars) |
| operand.f8960.f8960.line12.line11 | replace an operand | f8960.f8960.line12 | f8960.line11 -> f8960.line9d (NonNegDollars) |
| filter.household.household.test1_persons | remove collection filter | household.household.test1_persons |  |
| filter.household.household.test2_persons | remove collection filter | household.household.test2_persons |  |
| boundary.household.household.test1_met | replace strict greater-than with inclusive | household.household.test1_met |  |
| refusal.person.person.medicare5.0 | remove refusal | person.person.medicare5 |  |
| refusal.person.person.medicare6.0 | remove refusal | person.person.medicare6 |  |
| refusal.s3.s3.line8.0 | remove refusal | s3.s3.line8 |  |
| refusal.s8812.s8812.line2a.0 | remove refusal | s8812.s8812.line2a |  |
| refusal.s8812.s8812.line2b.0 | remove refusal | s8812.s8812.line2b |  |
| refusal.s8812.s8812.line2c.0 | remove refusal | s8812.s8812.line2c |  |
| operand.s8812.s8812.line2d.line2a | replace an operand | s8812.s8812.line2d | s8812.line2a -> s8812.zero (NonNegDollars) |
| operand.s8812.s8812.line2d.line2b | replace an operand | s8812.s8812.line2d | s8812.line2b -> s8812.zero (NonNegDollars) |
| operand.s8812.s8812.line2d.line2c | replace an operand | s8812.s8812.line2d | s8812.line2c -> s8812.zero (NonNegDollars) |
| operand.s8812.s8812.line12.line11 | replace an operand | s8812.s8812.line12 | s8812.line11 -> s8812.line10 (NonNegDollars) |
| refusal.s8812.s8812.clw_a2.0 | remove refusal | s8812.s8812.clw_a2 |  |
| refusal.s8812.s8812.clw_a4.0 | remove refusal | s8812.s8812.clw_a4 |  |
| operand.s8812.s8812.clw_a5.clw_a4 | replace an operand | s8812.s8812.clw_a5 | s8812.clw_a4 -> s8812.clw_a2 (Dollars) |
| operand.s8812.s8812.line13.clw_a5 | replace an operand | s8812.s8812.line13 | s8812.clw_a5 -> s8812.clw_a3 (Dollars) |
| refusal.s8812.s8812.eiw_1b.0 | remove refusal | s8812.s8812.eiw_1b |  |
| refusal.s8812.s8812.eiw_3.0 | remove refusal | s8812.s8812.eiw_3 |  |
| refusal.s8812.s8812.eiw_4.0 | remove refusal | s8812.s8812.eiw_4 |  |
| operand.s8812.s8812.eiw_4.zero | replace an operand | s8812.s8812.eiw_4 | s8812.zero -> s8812.eiw_3 (NonNegDollars) |
| refusal.s8812.s8812.eiw_5.0 | remove refusal | s8812.s8812.eiw_5 |  |
| operand.s8812.s8812.eiw_6.eiw_4 | replace an operand | s8812.s8812.eiw_6 | s8812.eiw_4 -> s8812.eiw_3 (NonNegDollars) |
| operand.s8812.s8812.eiw_6.eiw_5 | replace an operand | s8812.s8812.eiw_6 | s8812.eiw_5 -> s8812.eiw_3 (NonNegDollars) |
| operand.s8812.s8812.line18b.eiw_1b | replace an operand | s8812.s8812.line18b | s8812.eiw_1b -> s8812.eiw_6 (NonNegDollars) |
| operand.s8812.s8812.line19.line18a | replace an operand | s8812.s8812.line19 | s8812.line18a -> s8812.line18b (NonNegDollars) |
| operand.s8812.s8812.line20.line19 | replace an operand | s8812.s8812.line20 | s8812.line19 -> s8812.line18b (NonNegDollars) |
| operand.s8812.s8812.amt_ws4.ss_withheld | replace an operand | s8812.s8812.amt_ws4 | s8812.ss_withheld -> s8812.line20 (NonNegDollars) |
| operand.s8812.s8812.line21.amt_ws4 | replace an operand | s8812.s8812.line21 | s8812.amt_ws4 -> s8812.line18a (Dollars) |
| refusal.s8812.s8812.line22.0 | remove refusal | s8812.s8812.line22 |  |
| refusal.s8812.s8812.line22.1 | remove refusal | s8812.s8812.line22 |  |
| operand.s8812.s8812.line23.line21 | replace an operand | s8812.s8812.line23 | s8812.line21 -> s8812.line18a (Dollars) |
| operand.s8812.s8812.line23.line22 | replace an operand | s8812.s8812.line23 | s8812.line22 -> s8812.line18a (Dollars) |
| operand.s8812.s8812.line25.line23 | replace an operand | s8812.s8812.line25 | s8812.line23 -> s8812.line22 (NonNegDollars) |
| operand.s8812.s8812.line25.line24 | replace an operand | s8812.s8812.line25 | s8812.line24 -> s8812.line22 (NonNegDollars) |
| minmax.s8812.s8812.line26 | swap smaller_of/larger_of | s8812.s8812.line26 |  |
| operand.s8812.s8812.line26.line20 | replace an operand | s8812.s8812.line26 | s8812.line20 -> s8812.line24 (NonNegDollars) |
| operand.s8812.s8812.line26.line25 | replace an operand | s8812.s8812.line26 | s8812.line25 -> s8812.line24 (NonNegDollars) |
| operand.s8812.s8812.from_part_iia.line20 | replace an operand | s8812.s8812.from_part_iia | s8812.line20 -> s8812.line26 (NonNegDollars) |
| minmax.s8812.s8812.from_part_iib | swap smaller_of/larger_of | s8812.s8812.from_part_iib |  |
| operand.s8812.s8812.from_part_iib.line17 | replace an operand | s8812.s8812.from_part_iib | s8812.line17 -> s8812.from_part_iia (NonNegDollars) |
| operand.s8812.s8812.from_part_iib.line26 | replace an operand | s8812.s8812.from_part_iib | s8812.line26 -> s8812.from_part_iia (NonNegDollars) |
| refusal.s8812.s8812.line27.0 | remove refusal | s8812.s8812.line27 |  |
| refusal.sa.sa.line17.1 | remove refusal | sa.sa.line17 |  |
| refusal.sa.sa.line17.2 | remove refusal | sa.sa.line17 |  |
| operand.sdtw.sdtw.line12.line9 | replace an operand | sdtw.sdtw.line12 | sdtw.line9 -> sdtw.line10 (NonNegDollars) |
| operand.sdtw.sdtw.line17.line16 | replace an operand | sdtw.sdtw.line17 | sdtw.line16 -> sdtw.line15 (NonNegDollars) |
| operand.sdtw.sdtw.raw27.line26 | replace an operand | sdtw.sdtw.raw27 | sdtw.line26 -> sdtw.raw26 (NonNegDollars) |
| operand.sdtw.sdtw.raw28.line22 | replace an operand | sdtw.sdtw.raw28 | sdtw.line22 -> sdtw.line24 (Dollars) |
| operand.sdtw.sdtw.raw29.line27 | replace an operand | sdtw.sdtw.raw29 | sdtw.line27 -> sdtw.raw27 (NonNegDollars) |
| operand.sdtw.sdtw.raw30.line29 | replace an operand | sdtw.sdtw.raw30 | sdtw.line29 -> sdtw.raw29 (NonNegDollars) |
| operand.sdtw.sdtw.raw31.line30 | replace an operand | sdtw.sdtw.raw31 | sdtw.line30 -> sdtw.raw30 (NonNegDollars) |
| operand.sdtw.sdtw.raw33.line32 | replace an operand | sdtw.sdtw.raw33 | sdtw.line32 -> sdtw.raw32 (Dollars) |
| operand.sdtw.sdtw.raw34.line33 | replace an operand | sdtw.sdtw.raw34 | sdtw.line33 -> sdtw.raw33 (Dollars) |
| operand.sdtw.sdtw.raw38.line37 | replace an operand | sdtw.sdtw.raw38 | sdtw.line37 -> sdtw.raw37 (NonNegDollars) |
| operand.sdtw.sdtw.raw39.line38 | replace an operand | sdtw.sdtw.raw39 | sdtw.line38 -> sdtw.raw38 (NonNegDollars) |
| operand.sdtw.sdtw.raw40.line39 | replace an operand | sdtw.sdtw.raw40 | sdtw.line39 -> sdtw.raw39 (NonNegDollars) |
| operand.sdtw.sdtw.raw42.line41 | replace an operand | sdtw.sdtw.raw42 | sdtw.line41 -> sdtw.raw41 (Dollars) |
| operand.sdtw.sdtw.raw43.line42 | replace an operand | sdtw.sdtw.raw43 | sdtw.line42 -> sdtw.raw42 (Dollars) |
| operand.sdtw.sdtw.line45.line43 | replace an operand | sdtw.sdtw.line45 | sdtw.line43 -> sdtw.raw43 (Dollars) |
| param.actc.earned_floor.$1 | shift a money parameter (+$1) | actc.earned_floor |  |
| param.actc.rate.+1pt | shift a rate parameter (+1 point) | actc.rate |  |
| param.actc.three_children.$1 | shift a money parameter (+$1) | actc.three_children |  |
| param.qr.gross_income_limit.$1 | shift a money parameter (+$1) | qr.gross_income_limit |  |
