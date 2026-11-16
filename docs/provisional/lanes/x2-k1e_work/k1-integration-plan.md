# Return-integration plan for the three K-1 lanes (k1p, k1s, k1e) on top of x1-sche — DRAFT

Written by lane x2-k1e, 2026-11-15, model claude-opus-5-5 (judgment). Inputs read: `/tmp/scout-schedule-e.md` (x1-sche
design, §3.5, 3.6, 3.8), `docs/provisional/lanes/scout-k1.md` §3.5–3.7, `/tmp/k1-wiring-k1p.md` (early declaration),
`/tmp/k1-wiring-k1e.md` (final for k1e). **`/tmp/k1-wiring-k1s.md` did not exist when this was written**: k1s names below
are the scout's §3.3 sketch, mapped onto the k1p convention [I]; confirm them against that file before wiring.
Line ids of x1-sche are its design's contract (scout-schedule-e §3.1 "Line id contract", §3.5, §3.6) [T]; confirm
against the merged `sche.yaml` / `f8582.yaml`. Nothing here was run.

Convention: return-level forms read per-person sums with `sum_over person field person.<coll>_total_<item>`; below,
`Σ k1p.X` abbreviates that for `person.k1p_total_X` (likewise k1s, k1e).

## 1. Schedule E (`sche.yaml`, owned by x1-sche; the integration lane adds Parts II and III)

| Line | Today (x1-sche design) | Change |
|---|---|---|
| `sche.line29a_h` (new) | — | `sum(Σ k1p.passive_income, Σ k1s.passive_income)` — column (h) |
| `sche.line29a_k` (new) | — | `sum(Σ k1p.nonpassive_income, Σ k1s.nonpassive_income)` — column (k) |
| `sche.line29b_g` (new) | — | allowed passive loss magnitude per K-1 from the Form 8582 Part VI–VIII rows (k1p/k1s final contracts); NonNeg, read negated |
| `sche.line29b_i` (new) | — | `sum(Σ k1p.nonpassive_loss, Σ k1s.nonpassive_loss)` magnitude |
| `sche.line29b_j` (new) | — | 0 (section 179 refused) |
| `sche.line30` (new) | — | `sum(line29a_h, line29a_k)` |
| `sche.line31` (new) | — | `−sum(line29b_g, line29b_i, line29b_j)` (held negative, T-004 precedent) |
| `sche.line32` (new) | — | `sum(line30, line31)` |
| `sche.line34a_d` (new) | — | `Σ k1e.col_d` |
| `sche.line34a_f` (new) | — | `Σ k1e.col_f` |
| `sche.line34b_c`, `sche.line34b_e` (new) | — | 0 (k1e refuses every loss; `copy sche.zero` or omit and make line 36 zero) |
| `sche.line35` (new) | — | `sum(line34a_d, line34a_f)` |
| `sche.line36` (new) | — | 0 |
| `sche.line37` (new) | — | `sum(line35, line36)`; 13 A estimated tax is **not** in it (i1040se p. 11) |
| `sche.line27` (new) | — | Bool input, refusing Yes (prior basis/at-risk loss, UPE); asked when any k1p/k1s row |
| `sche.line41` | `copy sche.line26` | `sum(line26, line32, line37)` (Part IV and line 40 stay refused) |
| `sche.any` | rental ∨ royalty | `∨ Σ k1p.count_sche > 0 ∨ Σ k1s.count_sche > 0 ∨ Σ k1e.count_sche > 0` (a portfolio-only K-1 adds no row: amb `k1e_portfolio_no_sche`) |
| `sche.nonpassive_net` | royalty net | `+ Σ k1p.nonpassive + Σ k1s.nonpassive + Σ k1e.col_f` (Form 8582 MAGI keeps nonpassive income; k1e column (f) is nonpassive: box 5 and materially-participated box 6) |

## 2. Form 8582 (`f8582.yaml`, owned by x1-sche)

| Line | Today | Change |
|---|---|---|
| `f8582.line1a/1b/1c` | rental Part IV | `+ Σ k1p.p4_income / p4_loss / p4_prior` and the k1s equivalents (box 2 with active participation). **k1e adds nothing to Part IV** (a beneficiary does not actively participate: i8582 p. 4, "Only an individual, a qualifying estate, or a qualified revocable trust ... may actively participate"; amb `k1e_passive_default`) |
| `f8582.line2a` | rental Part V income | `+ Σ k1p.p5_income + Σ k1s.p5_income + Σ k1e.col_d` |
| `f8582.line2b/2c` | rental Part V | `+ Σ k1p.p5_loss/p5_prior + k1s` (k1e none) |
| `f8582.p6_total`, `p7_total` | rental | `+` the k1p/k1s Part VI/VII contributions (k1e none: income only) |
| `f8582.required` | rental conditions | `∨` any k1p/k1s Part V activity with a loss or prior loss; `∨` a Part IV K-1 outside i1065sk1 p. 14 conditions a–h; and **the rental exception fails** when `Σ k1e.rre > 0` (i8582 p. 1, "You don’t hold any interest in a rental real estate activity as a limited partner or as a beneficiary of an estate or a trust") or when any other passive activity exists (`Σ k1e.col_d > 0`, k1p/k1s passive rows: "Rental real estate activities with active participation were your only passive activities") |
| `f8582.magi_income` | no s1.line5 | via `sche.nonpassive_net` above (no direct change) |

## 3. Schedule 1, Schedule B, Form 1040, Schedule D and worksheets

| Line | Today [V for current tree, scout-k1 §3.7] | Change |
|---|---|---|
| `s1.line5` | x1-sche: `copy sche.line41` | none (Parts II/III arrive through line 41) |
| `s1.ebl_total` | x1-sche D15 | `+ Σ k1p.ebl_part + Σ k1s.ebl_part` (k1e none) |
| `sb.line2` | `sum_over interest field interest.amount` | `sum(…, Σ k1p.interest, Σ k1s.interest, Σ k1e.interest)` |
| `sb.line6` | ordinary dividends | `+ Σ k1p.ord_div + Σ k1s.ord_div + Σ k1e.ord_div` |
| `f1040.line2a` | `sum(tax_exempt_interest, div.box12)` | `+ Σ k1p.taxexempt_int + Σ k1s.taxexempt_int + Σ k1e.taxexempt_int` |
| `f1040.line3a` | input | `sum(f1040.line3a_entered, Σ k1p.qual_div, Σ k1s.qual_div, Σ k1e.qual_div)`; the entered input's help says "not from a Schedule K-1" (N8). This renames an input: restate fixtures that set `f1040.line3a` (list them) |
| `f1040.line25c` | `sum(line25c_other…, f8959.line24)` | `+ Σ k1p.backup_wh + Σ k1s.backup_wh + Σ k1e.backup_wh`; `line25c_other` help excludes K-1 |
| `f1040.line26` | input | `sum(f1040.line26_entered, Σ k1e.est_tax)` (same rename caution) |
| `sd.line5` | `copy sd.zero` | `sum(Σ k1p.st_gain, Σ k1s.st_gain, Σ k1e.st_gain)` (k1p may be negative: Dollars) |
| `sd.line12` | `copy sd.zero` | `sum(Σ k1p.lt_gain, Σ k1s.lt_gain, Σ k1e.lt_gain)` |
| `sd.other_forms` | refuses "capital gains or losses on a Schedule K-1" | drop that clause (remaining clauses stay) |
| `g28.line4` | 1099-DIV 2d, Form 2439 | `+ Σ k1p.collectibles + Σ k1s.collectibles + Σ k1e.collectibles` |
| `u1250.line5` | K-1 partnership/S corp | `+ Σ k1p.unrecap_1250 + Σ k1s.unrecap_1250` |
| `u1250.line11` | 1099-DIV 2b, Form 2439 | `+ Σ k1e.unrecap_1250` (the 1041 K-1 routes 4c to line 11, not line 5) |

## 4. Self-employment, QBI, NIIT, EIC, child tax credit

| Line | Change |
|---|---|
| `person.se_line2` | `sum(person.sc_total, person.k1p_total_se_earnings)` (k1s/k1e none); also `person.eic_se`, `person.dc_earned` (scout-k1 O3) |
| `person.se_screen` | drop the K-1 box 14 A clause |
| `person.qbi` | `sum(sum_over sc field sc.qbi, person.k1p_total_qbi, person.k1s_total_qbi, person.k1e_total_qbi)`; `k1p.qbi` less its SE attribution (D-K8) |
| `sc.qbi_se_pos` | whole becomes `person.se_pos_whole` (positive Schedule C profits + positive 14 A) (D-K8) |
| `qbi.eligible` / `f8995.line6` | `+ Σ k1e.reit` (and k1p/k1s REIT items if exposed) |
| `qbi.suspended` | `any(input, Σ k1p/k1s prior_allowed > 0)` (R-K22) |
| `qbi.unsupported` label | K-1 QBI no longer refused by scope |
| `f8960.line4a` | x1-sche: `copy s1.line5` — K-1 Parts II/III arrive through it |
| `f8960.line4b` | Dollars: `−(Σ k1p.nonpassive + Σ k1s.nonpassive)` (trade-or-business nonpassive only; **no k1e term**: i8960 p. 8 note, estate/trust adjustments go on line 7) |
| `f8960.line7` | Dollars: `Σ k1e.nii_adj` (positive only; negative refused) |
| `f8960.line13` (MAGI) | `+ Σ k1e.nii_adj` (i8960 p. 13: "increase your MAGI on Form 8960, line 13 ... by the same amount") — the scout named line 7 only |
| `f8960.unsupported` | drop "pass-through" |
| `eic.step2_other` | via `sche.any` (Part I design D6) — any Part II/III row refuses EIC; check whether the EIC investment-income test needs the K-1 amounts beyond lines 2a/2b/3b/Schedule D [I, not read] |
| `s8812.eiw_2b` / `eiw_3` | `+ person.k1p_total_se_earnings` or keep refusing partnership SE (scout-k1 verification O4) |
| `s1a.line5_calc` | new gate on any nonpassive K-1 box 1 (tips in a pass-through business refused) |

## 5. Scope and interview

- `scope.k1` leaves the `any` list of `scope.schedule1` and becomes the parent (off-ramp) of `$k1p`, `$k1s` (264) and
  `$k1e` (266). The k1e bank (order 266, seq 1–36, groups `k1e_refused`, `k1e_boxes`, `k1e_codes`) is in the k1e lane's
  diff; it becomes reachable only after this change. Consider splitting `scope.k1` into "partnership or S corporation"
  and "estate or trust" so a beneficiary is not asked the 1065/1120-S roster questions (N8: one question each).
- `scope.passive` narrowed (Part I design does the rental half); `f2441` notes; `tools/coverage/categories.json`
  (`partnership_scorp`, `estate_trust` → `refused: false`).
- Coverage rows: `scope.k1` and `scope.estate_excess_deductions` (scope.yaml) change their ends (N9, approved by D-K12):
  the latter to `k1e.box11_any`. Move `docs/provisional/lanes/x2-k1e_work/coverage_k1e.yaml` to
  `interview/2025/coverage/k1e.yaml` and the two personas to `interview/2025/personas/` (numbers 18, 19); run
  `interview-coverage --write`.
- Remove `display:` from every `person.k1e_total_*` / `person.k1e_count_*` the wiring reads.

## 6. Order of work and checks

1. Merge x1-sche, then k1p, k1s, k1e (the K-1 lanes touch distinct files except `person.yaml`, `questions.yaml`,
   `defaults.json`, `ambiguities/2025.yaml`, `tree.json`: merge by id).
2. Wire §1–§4 in one lane (scout-k1 K4/K5), §5 in the interview lane (K6).
3. Fixtures FK1–FK12 of scout-k1 §5 become return-level cases; the k1e lane's entry-level cases (`fixtures/2025/k1e.json`)
   stay as they are.
4. Reviews (one per form per round): new k1p, k1s, k1e → transcription, render, class M; changed sche, f8582, person,
   sb, f1040, sd, g28, u1250, f8960, qbi, f8995, sc, s8812, s1, eic, scope → line-scoped transcription (+ render where
   wording changed); class M for f8960, f8995, person, sche.
