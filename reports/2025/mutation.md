# Mutation score — implemented worksheets

Single-atom mutations applied to the canonical data; a mutant is killed if the
build-time checker fails on it or if any fixture case's value changes. Fixture
expectations are the recorded values checked in the previous run (the same values
the fixture test compares).

| Metric | Value |
| --- | --- |
| Mutants | 927 |
| Killed by the checker | 55 |
| Killed by fixtures | 769 |
| Surviving | 103 (67 provably equivalent) |
| Mutation score (raw) | 88.9% |
| Mutation score (equivalent mutants excluded) | 95.8% |

## Surviving — classified equivalent

- `refusal.dependent.dependent.qualifying_relative.2` (remove refusal, dependent.dependent.qualifying_relative): The married gate on the qualifying-relative test duplicates, word for word, the married gate on the qualifying-child test. The qualifying-relative test is read only by qr_dependent, which is read only by claimed, whose any-test evaluates qc_dependent, and so qualifying_child, before qr_dependent; for a married person qualifying_child refuses first with the same refusal, so this gate never fires. (structural conditions re-checked this run.)
- `refusal.eic.eic.step1_resident.0` (remove refusal, eic.eic.step1_resident): The gate scope.other_income also refuses a line that Form 1040 line 11b reads, and eic.eligible tests eic.below_top (which reads line 11b) first, so the return's EIC refuses through line 11b whenever scope.other_income is true; the copy of the gate on eic.step1_resident adds nothing to any Form 1040 line. (structural conditions re-checked this run.)
- `refusal.eic.eic.step2_other.0` (remove refusal, eic.eic.step2_other): The gate scope.schedule1 also refuses a line that Form 1040 line 11b reads, and eic.eligible tests eic.below_top (which reads line 11b) first, so the return's EIC refuses through line 11b whenever scope.schedule1 is true; the copy of the gate on eic.step2_other adds nothing to any Form 1040 line. (structural conditions re-checked this run.)
- `refusal.eic.eic.step5_line1.0` (remove refusal, eic.eic.step5_line1): The gate scope.schedule1 also refuses a line that Form 1040 line 11b reads, and eic.eligible tests eic.below_top (which reads line 11b) first, so the return's EIC refuses through line 11b whenever scope.schedule1 is true; the copy of the gate on eic.step5_line1 adds nothing to any Form 1040 line. (structural conditions re-checked this run.)
- `refusal.eic.eic.step5_line2.0` (remove refusal, eic.eic.step5_line2): The gate scope.other_income also refuses a line that Form 1040 line 11b reads, and eic.eligible tests eic.below_top (which reads line 11b) first, so the return's EIC refuses through line 11b whenever scope.other_income is true; the copy of the gate on eic.step5_line2 adds nothing to any Form 1040 line. (structural conditions re-checked this run.)
- `operand.eic.eic.step5_line4.zero` (replace an operand, eic.eic.step5_line4): Step 5 line 4 keeps its own combat-pay refusal whatever it reads; the substituted line 2 is the same zero (a copy of eic.zero) carrying only the gate scope.other_income, and earned income adds line 3 (line 1 less line 2) before line 4, so when that gate is true line 3 has already refused with the same refusal. No value can change. (structural conditions re-checked this run.)
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
- `refusal.retirement.retirement.amount_a.0` (remove refusal, retirement.retirement.amount_a): retirement.amount_a reads retirement.show_a -> retirement.has_rollover -> retirement.rolled first, and retirement.rolled carries the identical refusal entry, so without the entry on retirement.amount_a the same refusal arrives through the chain. (structural conditions re-checked this run.)
- `refusal.retirement.retirement.amount_a.1` (remove refusal, retirement.retirement.amount_a): retirement.amount_a reads retirement.show_a -> retirement.has_rollover -> retirement.rolled first, and retirement.rolled carries the identical refusal entry, so without the entry on retirement.amount_a the same refusal arrives through the chain. (structural conditions re-checked this run.)
- `operand.s2.s2.line3.zero` (replace an operand, s2.s2.line3): Copy-chain identity: s2.zero and s2.line2 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s8812.s8812.line2b.zero` (replace an operand, s8812.s8812.line2b): Copy-chain identity: s8812.zero and s8812.line2a expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s8812.s8812.line2c.zero` (replace an operand, s8812.s8812.line2c): Copy-chain identity: s8812.zero and s8812.line2b expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.s8812.s8812.line2d.line2a` (replace an operand, s8812.s8812.line2d): Shared-gate identity: s8812.line2a and s8812.line2b, s8812.line2c are the same value behind the same refusal gates (sa.excluded_income) with identical refusal text, and s8812.zero is that value ungated; whichever operand refuses, the sum carries the same refusal, and when none does the operands are equal.
- `operand.s8812.s8812.line2d.line2b` (replace an operand, s8812.s8812.line2d): Shared-gate identity: s8812.line2b and s8812.line2a, s8812.line2c are the same value behind the same refusal gates (sa.excluded_income) with identical refusal text, and s8812.zero is that value ungated; whichever operand refuses, the sum carries the same refusal, and when none does the operands are equal.
- `operand.s8812.s8812.line2d.line2c` (replace an operand, s8812.s8812.line2d): Shared-gate identity: s8812.line2c and s8812.line2a, s8812.line2b are the same value behind the same refusal gates (sa.excluded_income) with identical refusal text, and s8812.zero is that value ungated; whichever operand refuses, the sum carries the same refusal, and when none does the operands are equal.
- `operand.s8812.s8812.line13.clw_a5` (replace an operand, s8812.s8812.line13): Credit Limit Worksheet A line 5 is line 3 less line 4, and line 4 is zero behind the same gate that line 2, an operand of line 3, carries. When the gate fires, line 3 already refuses and the subtraction returns its first operand's refusal; when it does not, line 4 is zero. Line 13 therefore reads the same value from line 5 as from line 3 on every input. (structural conditions re-checked this run.)
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
- `refusal.ssb.ssb.line6.0` (remove refusal, ssb.ssb.line6): ssb.line6 is read only by ssb.line7, which reads ssb.line5 -> ssb.line3 -> f1040.line8 first; f1040.line8 refuses on the same gate, so whenever it is true ssb.line7 returns a refusal from that chain (or an earlier one) and the entry on ssb.line6 never decides a value. (structural conditions re-checked this run.)
- `operand.u1250.u1250.line13.line9` (replace an operand, u1250.u1250.line13): Copy-chain identity: u1250.line9 and u1250.line16 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.u1250.u1250.line13.line10` (replace an operand, u1250.u1250.line13): Copy-chain identity: u1250.line10 and u1250.line16 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `operand.u1250.u1250.line13.line12` (replace an operand, u1250.u1250.line13): Copy-chain identity: u1250.line12 and u1250.line16 expand to the same value, including remaining refusal gates. Identical gates already checked by the containing line are redundant within its expression.
- `param.eic.earned_amount0.$1` (shift a money parameter (+$1), eic.earned_amount0): Unread parameter: no line of any form or definition reads eic.earned_amount0; it serves a cross-check outside the computation, so shifting it cannot change any value.
- `param.eic.earned_amount1.$1` (shift a money parameter (+$1), eic.earned_amount1): Unread parameter: no line of any form or definition reads eic.earned_amount1; it serves a cross-check outside the computation, so shifting it cannot change any value.
- `param.eic.earned_amount2.$1` (shift a money parameter (+$1), eic.earned_amount2): Unread parameter: no line of any form or definition reads eic.earned_amount2; it serves a cross-check outside the computation, so shifting it cannot change any value.
- `param.eic.earned_amount3.$1` (shift a money parameter (+$1), eic.earned_amount3): Unread parameter: no line of any form or definition reads eic.earned_amount3; it serves a cross-check outside the computation, so shifting it cannot change any value.
- `param.eic.maximum0.$1` (shift a money parameter (+$1), eic.maximum0): Unread parameter: no line of any form or definition reads eic.maximum0; it serves a cross-check outside the computation, so shifting it cannot change any value.
- `param.eic.maximum1.$1` (shift a money parameter (+$1), eic.maximum1): Unread parameter: no line of any form or definition reads eic.maximum1; it serves a cross-check outside the computation, so shifting it cannot change any value.
- `param.eic.maximum2.$1` (shift a money parameter (+$1), eic.maximum2): Unread parameter: no line of any form or definition reads eic.maximum2; it serves a cross-check outside the computation, so shifting it cannot change any value.
- `param.eic.maximum3.$1` (shift a money parameter (+$1), eic.maximum3): Unread parameter: no line of any form or definition reads eic.maximum3; it serves a cross-check outside the computation, so shifting it cannot change any value.
- `param.eic.ws_threshold0.joint.$1` (shift a money parameter (+$1), eic.ws_threshold0.joint): Line 5 amount eic.ws_threshold0.joint: in eic_0 the bands covering [eic.ws_threshold0.joint, eic.ws_threshold0.joint + $1) print each table's maximum in the column used, so shifting the amount by $1 can only turn a lookup equal to the maximum into a blank line 5; line 6 is line 2 either way. (structural conditions re-checked this run.)
- `param.eic.ws_threshold0.other.$1` (shift a money parameter (+$1), eic.ws_threshold0.other): Line 5 amount eic.ws_threshold0.other: in eic_0 the bands covering [eic.ws_threshold0.other, eic.ws_threshold0.other + $1) print each table's maximum in the column used, so shifting the amount by $1 can only turn a lookup equal to the maximum into a blank line 5; line 6 is line 2 either way. (structural conditions re-checked this run.)
- `param.eic.ws_threshold1.joint.$1` (shift a money parameter (+$1), eic.ws_threshold1.joint): Line 5 amount eic.ws_threshold1.joint: in eic_1, eic_2, eic_3 the bands covering [eic.ws_threshold1.joint, eic.ws_threshold1.joint + $1) print each table's maximum in the column used, so shifting the amount by $1 can only turn a lookup equal to the maximum into a blank line 5; line 6 is line 2 either way. (structural conditions re-checked this run.)

## Surviving — not yet explained

| Mutant | Kind | Location | Note |
| --- | --- | --- | --- |
| operand.f1040.f1040.line11b.line11a | replace an operand | f1040.f1040.line11b | f1040.line11a -> f1040.line9 (Dollars) |
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
| refusal.person.person.medicare5.0 | remove refusal | person.person.medicare5 |  |
| refusal.person.person.medicare6.0 | remove refusal | person.person.medicare6 |  |
| refusal.s3.s3.line8.0 | remove refusal | s3.s3.line8 |  |
| refusal.sa.sa.line17.1 | remove refusal | sa.sa.line17 |  |
| refusal.sa.sa.line17.2 | remove refusal | sa.sa.line17 |  |
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
