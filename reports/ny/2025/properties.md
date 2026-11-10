# Data-level properties

The refusal properties of spec 6.3 checked over 400 generated returns with New York answers (fast-check, seed 7, every filing status): a generated federal return and the answers of the New York documents (`generate.ts` `nyReturnArbitrary`), every federal and New York line evaluated. "Applicable" counts the cases where the property's premise held. A failure is reported with the smallest counterexample fast-check found. The branch coverage below is of the New York documents.

| Property | Statement | Cases | Applicable | Result |
| --- | --- | --- | --- | --- |
| refusal_propagates | No line computes a value from an operand that is a refusal; every line evaluated from a refused operand is a refusal. | 400 | 385 | holds |
| refusal_outranks_unknown | On generated returns with up to eight answers removed, every line evaluated from a refused operand is a refusal, whatever its other operands are; in particular an unknown operand does not hide a refused one. A choose whose guard is unknown is a refusal exactly when every way it can still resolve is a refusal, whatever the order of its guards. | 400 | 373 | holds |

## refusal_outranks_unknown

- Cases with a refused operand somewhere: 373; cases with a line that has both a refused and an unknown operand (the order this property guards): 253; cases with a choose stopped at an unknown guard: 392, of which 18 have one refused on every way it can still resolve.

## Branch coverage of the generated corpus

311 of 333 branches (choose guards, Bool lines both ways, floor and positive sides of subtract_floor0, left and right of smaller_of and larger_of) reached by the 400 generated returns. Unreached:

- ny_it201.no:true
- ny_it201.gate.line26:true
- ny_it201.gate.line29:true
- ny_it201.tcw.mfj#3
- ny_it201.tcw.mfj#4
- ny_it201.tcw.single#2
- ny_it201.tcw.single#3
- ny_it201.tcw.hoh#2
- ny_it201.tcw.hoh#3
- ny_it201.agi_top:true
- ny_it201.tax_high#0
- ny_it201.hh_state_t2#4
- ny_it201.hh_state_t2#5
- ny_it201.hh_state_t2#6
- ny_it201.hh_city_t5#4
- ny_it201.hh_city_t5#5
- ny_it201.hh_city_t5#6
- ny_it201.gate.hh_state_over7:true
- ny_it201.gate.hh_city_over7:true
- ny_it201.gate.use_tax_abode:true
- ny_it201.gate.use_tax_st141:true
- ny_it201.gate.line79_over:true
