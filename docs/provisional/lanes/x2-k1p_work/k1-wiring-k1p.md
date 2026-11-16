# K-1 wiring contract: lane x2-k1p (Schedule K-1, Form 1065)

Worktree `.claude/worktrees/x2-k1p`; lane note `docs/provisional/lanes/x2-k1p.md` there. Every line below exists in
that tree (`forms/2025/k1p.yaml`, and the `person.k1p_*` block in `forms/2025/person.yaml`, between the comments
`# --- k1p sums (lane x2-k1p) ---` and `# --- end k1p sums ---`). Nothing outside k1p/person reads them yet; the
person totals carry `display:` only so the build accepts unread lines — drop `display` from each one you wire.

## Naming convention (shared with x2-k1s, x2-k1e)

- Per-K-1 lines: `<coll>.<item>` in `forms/2025/<coll>.yaml`.
- Per-person sums: `person.<coll>_total_<item>` (money) and `person.<coll>_count_<item>` (Count), in `person.yaml`.
  Return-level readers use `sum_over person field person.<coll>_total_<item>` (spec 4.4).
- Loss columns are non-negative magnitudes (`NonNegDollars`); the reader negates (Schedule E line 31, Form 8582 lines
  1b/1c/2b/2c are printed as losses).
- **Every person sum filters `where k1p.screened = true`.** `k1p.screened` carries all of a K-1's refusals (PTP, the
  refusing boxes, sale, distributions, trading, tests 4/6/7, basis, at-risk, former passive, prior not active). A
  reader that reaches any `person.k1p_*` line therefore meets the K-1's refusal. Wire at least one total that every
  return with a K-1 reads (e.g. Schedule E line 32 and Schedule B line 2) so no refusal is skipped.

## Lines and where they go

| person line (sum over k1p) | per-K-1 line | meaning | feeds |
|---|---|---|---|
| person.k1p_total_passive_income | k1p.col_h | Sch. E 28 (h): passive net income of boxes 1 (not materially participated), 2, 3 | sche line 29a (h) -> 30 |
| person.k1p_total_nonpassive_income | k1p.col_k | Sch. E 28 (k): box 1 income materially participated + box 4a | sche line 29a (k) -> 30 |
| person.k1p_total_nonpassive_loss | k1p.col_i | Sch. E 28 (i), magnitude: box 1 loss materially participated | sche line 29b (i) -> 31 |
| person.k1p_total_nonpassive | k1p.nonpassive_net | col_k - col_i (Dollars) | f8582.magi_income (via sche.nonpassive_net); f8960.line4b (negated; trade or business nonpassive incl. 4a, amb scout-k1 #6) |
| person.k1p_total_p4_income / _p4_loss / _p4_prior | k1p.p4_income / p4_loss / p4_prior | Form 8582 Part IV (a)/(b)/(c): box 2 with active participation | f8582.line1a / line1b / line1c (x1-sche split helpers `line1a_rental` etc.: add one operand) |
| person.k1p_total_p5_income / _p5_loss / _p5_prior | k1p.p5_income / p5_loss / p5_prior | Form 8582 Part V (a)/(b)/(c): box 1 passive, box 2 not active, box 3 | f8582.line2a / 2b / 2c |
| person.k1p_total_p6_loss | k1p.p6_loss | Part VI column (a) (box 2 overall loss, Part IV) | f8582.p6_total |
| person.k1p_total_prior | k1p.prior_total | all prior-year unallowed losses of the K-1s | qbi.suspended (R-K22: release of a suspended K-1 loss), f8582.exception (condition c) |
| person.k1p_count_passive_loss | k1p.passive_loss | K-1s with a passive net loss or prior loss | f8582.required |
| person.k1p_count_general | k1p.general | K-1s held as general partner | f8582.exception condition (h) (a Part IV K-1 is always general: `k1p.active` requires it) |
| person.k1p_count_sche | k1p.sche_row | K-1s putting a row on Sch. E line 28 | sche.any (EIC refusal via sche.any) |
| person.k1p_count | k1p.one | number of partnership K-1s | — |
| person.k1p_total_interest | k1p.box5_if_any | box 5 | sb.line2 (Schedule B line 1 lists the partnership) |
| person.k1p_total_ord_div | k1p.box6a_if_any | box 6a | sb.line6 -> f1040.line3b |
| person.k1p_total_qual_div | k1p.box6b_if_any | box 6b | f1040.line3a |
| person.k1p_total_st_gain | k1p.box8_if_any | box 8 (Dollars) | sd.line5 |
| person.k1p_total_lt_gain | k1p.box9a_if_any | box 9a (Dollars) | sd.line12 |
| person.k1p_total_collectibles | k1p.box9b_if_any | box 9b (Dollars: a loss is negative, i1065sk1 p. 16 "gain or loss on line 4"; g28.line4 must take a signed amount, as for k1s box 8b) | g28.line4 |
| person.k1p_total_unrecap_1250 | k1p.box9c_if_any | box 9c (business-asset type only) | u1250.line5 |
| person.k1p_total_se_earnings | k1p.box14a_if_any | box 14 code A (Dollars; a loss refuses unless box 1 materially participated) | person.se_line2 (+ person.eic_se, person.dc_earned per scout O3); s8812.eiw (O4) |
| person.k1p_total_se_pos | k1p.se_pos | positive 14 A | D-K8: the whole of the SE-tax attribution (sc.qbi_se_pos whole = positive Sch. C profits + this) |
| person.k1p_total_backup_wh | k1p.box15o_if_any | 15 O | f1040.line25c |
| person.k1p_total_taxexempt_int | k1p.box18a_if_any | 18 A | f1040.line2a |
| person.k1p_total_qbi_stmt | k1p.box20z_if_any | 20 Z QBI as stated (before the suspended-loss share and SE attribution) | see k1p.qbi below |
| person.k1p_count_inv | k1p.has_b20ab | K-1s with 20 A/B | f4952 K-1 refusal (R-K18) |

## Lines the integration lane writes in k1p.yaml (they read f8582, absent from this tree)

Mirror `rental.p6_loss` ... `rental.allowed` of x1-sche's `forms/2025/rental.yaml` (same cites, `amb.2025.f8582_ratio_places`):

- `k1p.b2_p6c` = choose(`k1p.p6_loss` > 0 and `f8582.line9` > 0 -> prorate(`f8582.line9`, part `k1p.p6_loss`, whole `f8582.p6_total`, 6); else zero). Boxes 1 and 3 have no Part VI.
- `k1p.b{1,3}_p7a` = copy `k1p.b{n}_overall_loss` (displays then dropped); `k1p.b2_p7a` = subtract_floor0(`b2_overall_loss`, `b2_p6c`).
- `k1p.b{n}_p7c` = choose(`b{n}_p7a` > 0 and `f8582.p7_C` > 0 -> prorate(`f8582.p7_C`, `b{n}_p7a`, `f8582.p7_total`, 6); else zero).
- `k1p.b{n}_allowed` = subtract_floor0(`b{n}_loss_sum`, `b{n}_p7c`); `k1p.b{n}_carryforward` = copy `b{n}_p7c`.
- `k1p.col_g` = sum(`b1_allowed`, `b2_allowed`, `b3_allowed`) (magnitude) -> `person.k1p_total_col_g` -> sche line 29b (g).
  When the box 2 exception of i1065sk1 p. 14 (conditions a-h) holds, `f8582.line9` route gives the same column (g).
- `person.k1p_total_p7a` (sum of `b{n}_p7a`) -> add to `f8582.p7_total`.
- `k1p.qbi` (D-K7, scout amb 3): `box20z_if_any` when >= 0, or when box 1 is nonpassive; otherwise
  -prorate(-box20z, `b1_allowed` less the allowed share of `prior_b1_if`, `b1_net_loss`, 6) (the current-year loss's
  allowed share; a prior-year release refuses through `qbi.suspended`). Then less the SE attribution (D-K8):
  prorate(`person.se_line13` half, `k1p.se_pos`, whole, 6). `person.k1p_total_qbi` -> `person.qbi`.
- EBL (`s1.ebl_total`): box 1 trade or business losses = `col_i` + `b1_allowed`.

## Not in this lane (for the integrator)

- `scope.k1` must leave `scope.schedule1`'s `any` list (scope.yaml line ~990) only when Schedule E Part II and the
  Form 1040 lines above are wired; until then every K-1 filer still refuses at `scope.k1` and no k1p question is asked.
- Coverage rows for k1p: `docs/provisional/lanes/x2-k1p_work/coverage_k1p.yaml` (move to
  `interview/2025/coverage/k1p.yaml` once reachable; unverified here).
- The full profile needs no target if Schedule E line 41 and the Form 1040 lines read the totals.
