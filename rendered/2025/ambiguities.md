# Ambiguity register, tax year 2025

## amb.2025.multiplication_subcent

- Text at issue: QDCGT lines 18 and 21 multiply an amount by 15% and 20%. With the return-wide rounding setting off (dollars and cents), the instructions do not state how a fractional cent in the product is treated.

- Candidate readings: Round the product half-up to the nearest cent at the multiplication. | Truncate the product toward zero to whole cents. | Carry the exact fraction forward until some later rounding step.
- **Chosen:** Round the product half-up to the nearest cent at the multiplication.
- Reason: Matches the half-up convention of the printed whole-dollar rounding rules. The whole-dollar default is unaffected: whole-dollar amounts multiplied by these rates produce exact cents, so the reading only matters when cents are turned on.

- Status: Chosen for Stage 1; shown to the user whenever it can affect the return.
- Cite: [i1040gi] QDCGT worksheet, lines 18 and 21; Rounding Off to Whole Dollars, p. 23 (2025; printed date 2026-02-25; sha256 482e9c48)
