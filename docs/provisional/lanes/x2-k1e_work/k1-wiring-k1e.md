# K-1 wiring contract: lane x2-k1e (Schedule K-1, Form 1041) — final for the lane

Lane x2-k1e, 2026-11-15. Worktree `.claude/worktrees/x2-k1e`; report `docs/provisional/lanes/x2-k1e.md` there.
Naming follows `/tmp/k1-wiring-k1p.md`: per-K-1 lines `k1e.<item>` in `forms/2025/k1e.yaml`; per-person sums
`person.k1e_total_<item>` (Dollars) and `person.k1e_count_<item>` (Count) in `forms/2025/person.yaml`; return-level
readers use `sum_over person field person.k1e_total_<item>`. Item names match k1p's where the meaning is the same
(`interest`, `ord_div`, `qual_div`, `st_gain`, `lt_gain`, `collectibles`, `backup_wh`, `taxexempt_int`, `qbi`).

**No loss is exposed.** Losses in boxes 6–8, box 9 deductions, boxes 10–12, other codes of 13/14, a negative 14 H
and PTP/cooperative items in 14 I are refused per K-1 (`k1e.screen`). Every `k1e.<item>` below is
`sum(<box>, k1e.screen)`, so a refused K-1 refuses every person sum it enters. Schedule E line 33 columns (c) and (e)
and line 34b are therefore zero for estates and trusts; line 36 is zero.

The person totals carry `display:` (the build rejects unread lines). **Remove `display:` from each total the
integration lane wires**; keep it on any total left unread.

| person line | per-K-1 line (box) | type | feeds (integration lane wires) | source |
|---|---|---|---|---|
| `person.k1e_total_interest` | `k1e.interest` (1) | NonNeg | `sb.line2` (Schedule B line 1 lists the estate or trust) → `f1040.line2b` | f1041sk1 p. 2 "Form 1040 or 1040-SR, line 2b"; i1041sk1 p. 2 Box 1 "Schedule B (Form 1040), Part I, line 1, if applicable" |
| `person.k1e_total_ord_div` | `k1e.ord_div` (2a) | NonNeg | `sb.line6` (Part II line 5) → `f1040.line3b` | f1041sk1 p. 2; i1041sk1 p. 2 Box 2a |
| `person.k1e_total_qual_div` | `k1e.qual_div` (2b) | NonNeg | `f1040.line3a` (and through it `qdcg`) | f1041sk1 p. 2 "line 3a" |
| `person.k1e_total_st_gain` | `k1e.st_gain` (3) | NonNeg | `sd.line5` | f1041sk1 p. 2 "Schedule D, line 5" |
| `person.k1e_total_lt_gain` | `k1e.lt_gain` (4a) | NonNeg | `sd.line12` | f1041sk1 p. 2 "Schedule D, line 12" |
| `person.k1e_total_collectibles` | `k1e.collectibles` (4b, 28% rate gain) | NonNeg | `g28.line4` (28% Rate Gain Worksheet line 4; its label already names estates and trusts) | f1041sk1 p. 2 "28% Rate Gain Worksheet, line 4" |
| `person.k1e_total_unrecap_1250` | `k1e.unrecap_1250` (4c) | NonNeg | **`u1250.line11`** (not line 5: the 1041 K-1 sends 4c to line 11; k1p/k1s 9c/8c go to line 5) | f1041sk1 p. 2 "Unrecaptured Section 1250 Gain Worksheet, line 11"; i1041sk1 p. 2 |
| `person.k1e_total_col_d` | `k1e.col_d` (7 + 8 + 6 unless materially participated) | Dollars (≥ 0 after refusal) | `sche.line34a_d` → `sche.line35`; also Form 8582 **Part V line 2a** (passive income of "all other passive activities"; amb `k1e_passive_default`; a beneficiary does not take Part IV — i8582 p. 4 "Only an individual, a qualifying estate, or a qualified revocable trust ... may actively participate") | f1040se p. 2 "(d) Passive income from Schedule K-1" |
| `person.k1e_total_col_f` | `k1e.col_f` (5 + 6 when materially participated) | Dollars (≥ 0) | `sche.line34a_f` → `sche.line35` | f1040se p. 2 "(f) Other income from Schedule K-1" |
| (none: zero) | — | — | `sche.line34b_c`, `sche.line34b_e`, `sche.line36` = 0 for estates/trusts | losses refused |
| (derived) | — | — | `sche.line37 = line35 + line36`; `sche.line41` adds line 37 (→ `s1.line5` → `f8960.line4a`) | f1040se p. 2 lines 35–37, 41 |
| `person.k1e_count_sche` | `k1e.one where k1e.sch_e_any` | Count | `sche.any` (Schedule E attached) and through it the EIC refusal `eic.step2_other` (Part I design D6). A portfolio-only 1041 K-1 puts no row on Schedule E (amb `k1e_portfolio_no_sche`, D-K13) | i1040se p. 10 Part III |
| `person.k1e_total_rre` | `k1e.rre` (7) | Dollars (≥ 0 after refusal) | `f8582.required` (or the x1-sche exception helper): the rental-loss exception fails when > 0 ("You don’t hold any interest in a rental real estate activity as ... a beneficiary of an estate or a trust"). Also col_d > 0 breaks "Rental real estate activities with active participation were your only passive activities" | i8582 p. 1 Who Must File |
| `person.k1e_total_est_tax` | `k1e.est_tax` (13 A) | NonNeg | `f1040.line26` (sum with the entered estimated payments). Not in Schedule E line 37 (col_d/col_f exclude it) | i1040se p. 11 "enter “ES payment claimed” ... Do not include this amount in the total on line 37. Instead, enter the amount on Form 1040 ... line 26" |
| `person.k1e_total_backup_wh` | `k1e.backup_wh` (13 B) | NonNeg | `f1040.line25c` | f1041sk1 p. 2 "line 25c"; i1041sk1 p. 3 |
| `person.k1e_total_taxexempt_int` | `k1e.taxexempt_int` (14 A) | NonNeg | `f1040.line2a` | f1041sk1 p. 2 "line 2a" |
| `person.k1e_total_nii_adj` | `k1e.nii_adj` (14 H, positive only) | Dollars (≥ 0) | `f8960.line7` **and** `f8960.line13` (MAGI) increased by the same amount — the scout named line 7 only | i8960 p. 13 Line 7 "If the amount reported in box 14, code H ... is a positive number, enter it on Form 8960, line 7, and increase your MAGI on Form 8960, line 13" |
| `person.k1e_total_qbi` | `k1e.qbi` (14 I statement QBI) | Dollars (may be negative) | `person.qbi` (→ `f8995.line2`; one Form 8995 line 1 row per estate/trust) | i1041sk1 p. 4 Code I |
| `person.k1e_total_reit` | `k1e.reit` (14 I section 199A dividends) | NonNeg | `qbi.eligible` / `f8995.line6` (with Form 1099-DIV box 5) | i1041sk1 p. 4 "Section 199A dividends" |
| `person.k1e_count_entries` | `k1e.one` | Count | gates (e.g. `qbi.unsupported` wording, `scope` restructuring) | — |

## Notes for the integration lane

- **NIIT:** no `f8960.line4b` entry for estates/trusts: i8960 p. 8 "Any income from an estate or trust reported in Part
  III of Schedule E ... that excluded NII is taken into account on line 7. Don't report those adjustments on line 4b."
- **Form 8582 MAGI** (line 6/7): needs nothing K-1-specific from k1e (Schedule E line 37 is already in AGI).
- **EIC investment income** [I, not read]: if `eic`'s investment-income test reads Schedule E or passive income
  separately from lines 2a/2b/3b/Schedule D, k1e columns (d)/(f) need adding there; check before wiring.
- **Scope:** `scope.k1` still refuses estate/trust holders through `scope.schedule1`; the k1e bank entries (order 266)
  are unreachable until scope.k1 is restructured (k1e reached only after scope.k1 Yes, or a split question for
  estates/trusts). Coverage row `scope.estate_excess_deductions` (scope.yaml) then ends at `k1e.box11_any`
  (N9 end change); row `scope.k1` likewise.
- **Box 2b ≤ 2a, 4b + 4c ≤ 4a** are not checked (no archived sentence states them for the 1041 K-1); `div.bad_components`
  reads 1099-DIV lines only.

## Checked with a scratch wiring (applied, built, reverted in the k1e worktree)

With `scope.k1` out of `scope.schedule1` and a return line summing all 16 totals behind `scope.k1`, the 11 rows of
`docs/provisional/lanes/x2-k1e_work/coverage_k1e.yaml` pass (0 problems) and persona 18 completes. Two facts for the
wiring: a total that keeps `display:` once read fails the build; the k1e roster must sit behind `scope.k1` Yes (a
scratch target outside it made the one-W-2 filer answer an empty `$k1e`). Every `k1e.<item>` adds `k1e.screen`, so any
wired total tells the K-1's refusal; wire at least one total every K-1 return reads (e.g. `sb.line2`), as k1p asks.
