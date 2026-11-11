# Umbrella gates: questions saved (what-if)

Written by `node engine/dist/main.js interview-length --what-if --write` (engine/src/interview-length.ts and
engine/src/umbrella-what-if.ts; deterministic, no model calls). Each proposed umbrella of the
umbrella gates design (2026-11-10) is put into a copy of the built data in memory (a new Bool input; a gate line
`<input>_if_<umbrella>` in place of each gated input in every reader; a roster's readers under the same `choose`), and
every return of `interview_length.md` is walked in today's order as built and with the umbrella. The umbrella is
answered yes exactly when the walk as built answered one of its inputs with something other than false, 0 or none,
which is the truthful answer for these returns; both walks reach the same status and values on every return (checked;
a difference fails the run). The forms in the repository are unchanged.

*Saved* is questions asked as built minus questions asked with the umbrella (the umbrella question counted), as a mean
per return of the view. The returns are synthetic and answer nearly every rare question no, so the saving here is close
to the most an umbrella can save; the design weighs it by the share answering yes.

Returns not walkable as built (skipped): 0.

| Scenario | Umbrella asked (returns) | Answered yes | Full profile, complete (Stage 5 and generated): saved (mean) | Minimal: every gate closed: saved (mean) | All complete returns: saved (mean) | All returns, refused included: saved (mean) | Full profile: before → after |
|---|---|---|---|---|---|---|---|
| `s1.line8_any` | 229 of 253 | 0 | 8.0 | 8.0 | 7.2 | 6.9 | 111.2 → 103.2 |
| `s1.part1_other_any` | 229 of 253 | 0 | 9.0 | 9.0 | 8.1 | 7.8 | 111.2 → 102.2 |
| `sb.foreign_any` | 223 of 253 | 4 | 3.0 | 3.0 | 2.7 | 2.6 | 111.2 → 108.2 |
| `sb.foreign_wide_any` | 232 of 253 | 5 | 4.0 | 4.0 | 3.6 | 3.4 | 111.2 → 107.2 |
| `f1040.other_payments_any` | 50 of 253 | 7 | 2.0 | 5.0 | 0.5 | 0.4 | 111.2 → 109.2 |
| `f1040.withholding_other_any` | 29 of 253 | 0 | 1.0 | 1.0 | 0.1 | 0.1 | 111.2 → 110.2 |
| `sd.carryovers_any` | 218 of 253 | 1 | 2.0 | 2.0 | 1.0 | 0.7 | 111.2 → 109.2 |
| `f5695.any` | 29 of 253 | 1 | 1.0 | 1.0 | 0.1 | 0.1 | 111.2 → 110.2 |
| `f2441.any` | 225 of 253 | 1 | 1.0 | 1.0 | 0.1 | 0.1 | 111.2 → 110.2 |
| `s2.other_taxes_any` | 232 of 253 | 6 | 4.0 | 4.0 | 2.2 | 2.3 | 111.2 → 107.2 |
| `s1.adjustments_any` | 229 of 253 | 3 | 0.8 | 1.0 | 0.9 | 0.9 | 111.2 → 110.3 |
| `s1a.any` | 198 of 253 | 1 | 2.0 | 2.0 | 1.8 | 1.3 | 111.2 → 109.2 |
| **recommended together** | 253 of 253 | 13 | 16.0 | 19.0 | 11.5 | 10.8 | 111.2 → 95.2 |

## Per return, full profile

Questions asked as built, then the saving under each scenario.

| Return | Status | As built | `s1.line8_any` | `s1.part1_other_any` | `sb.foreign_any` | `sb.foreign_wide_any` | `f1040.other_payments_any` | `f1040.withholding_other_any` | `sd.carryovers_any` | `f5695.any` | `f2441.any` | `s2.other_taxes_any` | `s1.adjustments_any` | `s1a.any` | **recommended together** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| stage5.return.owed | complete | 105 | 8 | 9 | 3 | 4 | 5 | 1 | 2 | 1 | 1 | 4 | 1 | 2 | 19 |
| stage5.return.refund | complete | 84 | 8 | 9 | 3 | 4 | -1 | 1 | 2 | 1 | 1 | 4 | 1 | 2 | 13 |
| stage5.return.itemized | complete | 119 | 8 | 9 | 3 | 4 | 5 | 1 | 2 | 1 | 1 | 4 | 1 | 2 | 19 |
| stage5.refuse.screens | refused | 43 | 0 | 0 | 3 | 4 | 2 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 6 |
| stage5.refuse.other_income | refused | 48 | 0 | 0 | 3 | 4 | 2 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 6 |
| stage5.return.refund_f4952_screens_unused | complete | 84 | 8 | 9 | 3 | 4 | -1 | 1 | 2 | 1 | 1 | 4 | 1 | 2 | 13 |
| stage5.return.refund_f8960_unsupported_unused | complete | 84 | 8 | 9 | 3 | 4 | -1 | 1 | 2 | 1 | 1 | 4 | 1 | 2 | 13 |
| stage5.return.f8960_unsupported_agi_at_threshold | complete | 84 | 8 | 9 | 3 | 4 | -1 | 1 | 2 | 1 | 1 | 4 | 1 | 2 | 13 |
| stage5.return.refund_f8960_refund_unused | complete | 84 | 8 | 9 | 3 | 4 | -1 | 1 | 2 | 1 | 1 | 4 | 1 | 2 | 13 |
| stage5.return.refund_combat_pay_no_children | complete | 84 | 8 | 9 | 3 | 4 | -1 | 1 | 2 | 1 | 1 | 4 | 1 | 2 | 13 |
| stage5.return.itemized_f8960_allocation_unused | complete | 119 | 8 | 9 | 3 | 4 | 5 | 1 | 2 | 1 | 1 | 4 | 1 | 2 | 19 |
| generated.0 | complete | 115 | 8 | 9 | 3 | 4 | 5 | 1 | 2 | 1 | 1 | 4 | 1 | 2 | 19 |
| generated.1 | refused | 107 | 8 | 9 | 3 | 4 | 2 | 1 | 1 | 1 | 1 | 1 | -1 | 0 | 15 |
| generated.2 | refused | 133 | 8 | 9 | 3 | 4 | 2 | 1 | 1 | -1 | 1 | 4 | -1 | 0 | 13 |
| generated.3 | refused | 142 | 8 | 9 | 3 | 4 | 3 | 1 | 1 | 0 | 1 | 4 | 1 | 0 | 15 |
| generated.4 | complete | 264 | 8 | 9 | 3 | 4 | 5 | 1 | 2 | 1 | 1 | 4 | -1 | 2 | 19 |
| generated.5 | refused | 79 | 0 | 0 | 3 | 3 | 2 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 6 |
| generated.6 | complete | 108 | 8 | 9 | 3 | 4 | 5 | 1 | 2 | 1 | 1 | 4 | 1 | 2 | 19 |
| generated.7 | refused | 80 | 0 | 0 | 3 | 3 | 2 | 1 | 1 | 0 | 1 | 1 | 2 | -1 | 6 |
| generated.8 | refused | 152 | 8 | 9 | 3 | 4 | 3 | 1 | 2 | 1 | 1 | 4 | 1 | 2 | 17 |
| generated.9 | refused | 100 | 8 | 9 | -1 | -1 | 2 | 1 | 1 | 0 | -1 | -1 | 1 | 0 | 10 |
| generated.10 | refused | 259 | 8 | 9 | 3 | 4 | 5 | 1 | 1 | 0 | 1 | 4 | 1 | 0 | 17 |
| generated.11 | refused | 126 | 8 | 9 | 3 | 4 | 5 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 18 |
| every gate closed | complete | 80 | 8 | 9 | 3 | 4 | 5 | 1 | 2 | 1 | 1 | 4 | 1 | 2 | 19 |
| div.any = true alone | complete | 86 | 8 | 9 | 3 | 4 | 5 | 1 | 2 | 1 | 1 | 4 | 1 | 2 | 19 |
| f4952.has_interest = true alone | complete | 82 | 8 | 9 | 3 | 4 | 5 | 1 | 2 | 1 | 1 | 4 | 1 | 2 | 19 |
| f8889.coverage_year = "family" alone | complete | 80 | 8 | 9 | 3 | 4 | 5 | 1 | 2 | 1 | 1 | 4 | 1 | 2 | 19 |
| f8889.coverage_year = "changed" alone | complete | 80 | 8 | 9 | 3 | 4 | 5 | 1 | 2 | 1 | 1 | 4 | 1 | 2 | 19 |
| sa.gifts = true alone | complete | 83 | 8 | 9 | 3 | 4 | 5 | 1 | 2 | 1 | 1 | 4 | 1 | 2 | 19 |

<!-- Hand-written findings below this line are kept when the tool rewrites the report. -->
