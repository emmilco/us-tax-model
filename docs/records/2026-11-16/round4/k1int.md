# Lane A5-k1int: K-1 integration plan and draft patches (partnership and S corporation)

Lane A5-k1int. Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Written 2026-11-16, 01:05-01:35.
Read only: nothing in the repository or xint was changed. No build, engine, fixture, walk, check or review was run; no
paid call. Every predicted value is hand arithmetic. Tags: **[C path:line]** checked against that file (paths relative
to xint); **[S]** checked in scratch (YAML parsed, references resolved, patches dry-applied); **[I]** inferred.

## Summary

- **Three form patches and one fixture patch**, in `P/patches/v3/`, stacked in this order (each applies on the one
  before; the stack reproduces the scratch tree exactly [S]):
  1. `k1int-1-f8582.patch` (4 files, 1,369 lines). Gives the K-1 activities their Form 8582 Part VI to VIII rows
     (special allowance, unallowed loss, allowed loss, carryforward, Schedule E column (g)) for k1p and, newly, for
     k1s, and adds the K-1 Part IV/V/VI/VII totals to Form 8582. The contract specified this for k1p
     [C docs/provisional/lanes/x2-k1p_work/k1-wiring-k1p.md:50-60]; nothing was written for k1s.
  2. `k1int-2-ebl-qbi.patch` (7 files, 667 lines). **BUG-0842 and BUG-0885.** The excess business loss screen counts
     K-1 losses. K-1 qualified business income is cut to the allowed share of a passive box 1 loss (i8995 p. 3 ratio),
     a prior-year loss released this year refuses, and the self-employment tax attributable to box 14 A comes off
     (D-K8). Partnership and S corporation QBI reach `person.qbi`, and the suspended-loss question is asked of K-1
     filers.
  3. `k1int-3-return.patch` (10 files, 979 lines). Wires the rest of the contract's money flows: Schedule E Part II
     (lines 29a to 32, 41), `sche.any`, Schedule 1 line 5, Form 8582 MAGI, Schedule B lines 2 and 6, Form 1040
     lines 2a and 25c, Schedule D lines 5 and 12, the 28% and section 1250 worksheets, and Form 8960 line 4b. It adds
     an **interim refusal** for box 14 A self-employment earnings, so they cannot be silently left out of Schedule SE.
  4. `k1int-4-fixtures.patch`: new `fixtures/2025/k1int.json`, 9 cases, all predicted by hand (section 3).
- **What the stack does not do: lift `scope.k1`.** All three form patches change no return while `scope.k1` refuses
  every K-1. No form outside k1p, k1s and person reads the new totals except through K-1 entries, and `scope.k1`
  defaults to false. Lifting it is the interview step (plan step L1). It needs owner decisions D2, D3 and D6.
- **Readiness (section 1): 37 items.** 6 done in xint, 18 patched (v2 or v3, not landed), 13 missing; one of the
  missing items, box 14 A self-employment, has an interim refusal in patch 3. Missing items that block the lift:
  - scope and interview: split `scope.k1`, reword `scope.passive`, gate the roster
  - `f1040.line25c_other` wording: without it, K-1 backup withholding is counted twice (N8)
  - `f1040.line3a` qualified dividends from K-1s
  - `f8960.unsupported` wording: "pass-through income" refuses every K-1 filer
  - a Form 4952 refusal for box 20 A/B
  - tree.json and consumers bookkeeping
  - coverage rows
- **Found while drafting:**
  - (a) Taking the *allowed* K-1 losses into the excess business loss screen, as the contract and both bug entries
    propose, would create a cycle: `s1.ebl` → Form 8582 line 9 → MAGI → Schedule 1 line 3, whose refusal is `s1.ebl`.
    The patch therefore counts losses **before** the passive limit. That is the reading the project already applies
    to Schedule E Part I (`amb.2025.s1_ebl_rental` [C ambiguities/2025.yaml:2193-2204]). It can only over-refuse.
  - (b) `prorate` with a zero whole is unknown (spec.md:383). Every new prorate is behind a guard, as the rental
    template's are.
  - (c) Form 461 and i461 are now archived [C sources/2025/f461.txt]. The ambiguity's reason ("Form 461 is not
    archived") is stale.
  - (d) The v2 k1s patch's `k1s.qbi_passive` refusal is superseded by patch 2. Two v2 k1s hunks fail on top of the
    stack [S]; drop them. v2 k1p applies cleanly on top [S].
  - (e) `amb.2025.k1s_qbi_basis` says "no archived text says which part of the QBI loss the allowed loss carries".
    i8995 p. 3 does give the ratio [C sources/2025/i8995.txt:192-201], so `k1s.qbi_cut` could compute instead of
    refuse (D4).
- **Coverage (section 4):** `partnership_scorp` (gate `scope.schedule1`) changes; `estate_trust` stays refused (k1e was
  dropped from xint [C docs/provisional/lanes/xint.md:207]). The headline moves from **85.9% to between 87.8% and
  88.2%** (central measure; read-only bound from the existing report, estimator not rerun). That is an upper bound
  on the real gain, because the interim box 14 A refusal and the other residual K-1 refusals are unmeasured.

## 1. Readiness list (everything that must be true before `scope.k1` stops refusing partnership and S corporation K-1s)

Status: **done** (in xint now), **patched** (draft patch exists, not landed), **missing**.

| # | Item | Status | Where / evidence |
|---|---|---|---|
| 1 | k1p form (boxes, material participation, Part IV/V columns, refusals on `k1p.screened`) | done | forms/2025/k1p.yaml [C]; 27 fixtures [C fixtures/2025/k1p.json] |
| 2 | k1s form and Form 7203 (basis limit before passive) | done | forms/2025/k1s.yaml, f7203.yaml [C]; 17 fixtures |
| 3 | k1e (estates, trusts) | missing (dropped from xint) | xint.md:207 [C]. Not needed for partnership/S corp if `scope.k1` is split (D6) |
| 4 | BUG-0837, 0838, 0841, 0843 (k1p participation tests, spouse wording, own Schedule E items, real estate professional/dwelling) | patched | `P/patches/v2/k1p.patch`; applies cleanly on the v3 stack [S] |
| 5 | BUG-0882, 0886 + siblings (k1s trader, re_pro, dwelling, interest_buy) | patched | `P/patches/v2/k1s.patch`; its two `k1s.qbi_passive` hunks are superseded by v3 patch 2 (drop them) [S] |
| 6 | BUG-0911 (box 9b signed) | done | k1p.yaml:613-621 (per med-k1sche.md; inventory field rename only) |
| 7 | Form 8582 Part VI-VIII per K-1 activity (k1p) | patched (v3-1) | contract lines 50-60 |
| 8 | Same for k1s (per-activity overall loss, Part VI, VII, VIII, column (g)) | patched (v3-1) | not in any contract; k1s exposed only per-K-1 Part V sums [C k1s.yaml:2272-2386] |
| 9 | Form 8582 lines 1a-2c, Part VI/VII totals include K-1 rows | patched (v3-1) | f8582.yaml p4a..p5c, p6_total, p7_total [C :44-186, 536-567] |
| 10 | Form 8582 MAGI keeps K-1 nonpassive income | patched (v3-3) | `sche.nonpassive_net` + `sche.k1_nonpassive` |
| 11 | Form 8582 exception: K-1 Part V passive *income* (another passive activity) should defeat it; i1065sk1 p. 14 box 2 conditions | missing (display only) | `f8582.exception` tests p5b/p5c only [C f8582.yaml:579-610]; amounts are unaffected (line 9 = loss when the exception holds) [I] |
| 12 | BUG-0836 (MFS lived together gets the Part II allowance) | missing (lane A, live) | K-1 Part IV rows read the same line 9: land before the lift |
| 13 | Form 7203 inside k1s (allowed1-3 feed b{n}_net) | done | k1s.yaml:1631-1666 [C]; residual refusals stay (loans, election, distribution above basis, basis carryover) |
| 14 | Excess business loss (Form 461) with K-1 losses (BUG-0842, 0885) | patched (v3-2) | pre-limit reading, cycle note in Summary; D1 |
| 15 | k1p QBI after the passive limit (D-K7), prior-year release refused | patched (v3-2) | new `amb.2025.k1p_qbi_passive` |
| 16 | k1p QBI less SE tax attribution (D-K8); `sc.qbi_se_pos` whole includes positive 14 A | patched (v3-2) | `person.se_pos_whole` |
| 17 | k1s QBI after the passive limit | patched (v3-2) | replaces v2 `k1s.qbi_passive` |
| 18 | K-1 QBI into `person.qbi`, Form 8995; suspended-loss question asked of K-1 filers | patched (v3-2) | `qbi.has_business` |
| 19 | QBI above the Form 8995 threshold | done | `qbi.business_any` refuses on any `f8995.line2` ≠ 0 [C qbi.yaml:207-240] |
| 20 | `qbi.unsupported` label still says K-1 QBI is refused by scope | missing (label) | qbi.yaml:123 [C] |
| 21 | Schedule E Part II lines 29a, 29b, 30, 31, 32; line 41; `sche.any`; Schedule 1 line 5 gate | patched (v3-3) | line 29b (j) zero (section 179 refused by D-K6) |
| 22 | Schedule E line 27 Yes/No and line 28 row rendering (names, columns per K-1) | missing (render) | how collection rows render on Schedule E not checked [I] |
| 23 | Schedule B lines 2, 6 (K-1 interest, dividends) | patched (v3-3) | Part I payer listing for the K-1 not rendered [I] |
| 24 | Form 1040 line 2a, line 25c | patched (v3-3) | |
| 25 | `f1040.line25c_other` input says "Schedules K-1"; with v3-3 a K-1's backup withholding would be entered twice | **missing (blocks)** | f1040.yaml:926-959 [C]; reword the source to exclude K-1 (question review) |
| 26 | Form 1040 line 3a qualified dividends from K-1s | **missing (blocks)** | line 3a is an input [C f1040.yaml:265-276]; 599 fixture facts in 16 files set it [C grep]; D3 |
| 27 | Schedule D lines 5, 12 | patched (v3-3) | |
| 28 | 28% worksheet line 4 (signed K-1 collectibles), section 1250 worksheet line 5 | patched (v3-3) | new `amb.2025.k1_collectibles_loss`; D5 |
| 29 | Self-employment tax for box 14 A (Schedule SE line 2, `person.se_screen` clause, `eic_se`, `dc_earned`, `s8812` earned income, SEP/SIMPLE base, Form 7206, NY MCTMT note) | missing; **interim refusal patched** (v3-3 `person.k1_se_any`) | `person.se_line2` copies `sc_total` [C person.yaml:2323-2340]; se_screen names 14 A [C :2298]; D2 |
| 30 | NIIT: Form 8960 line 4b (nonpassive trade or business, incl. 4a) | patched (v3-3) | line 4a already takes Schedule 1 line 5 [C f8960.yaml:188-196] |
| 31 | `f8960.unsupported` lists "annuity, business or pass-through income": every K-1 filer answers Yes | **missing (blocks)** | f8960.yaml:16 [C]; question change |
| 32 | Form 4952: box 20 A/B (k1p) investment interest | **missing** | `person.k1p_count_inv` unread (display) [C person.yaml:7813]; contract R-K18 |
| 33 | EIC: any Schedule E row refuses (via `sche.any`) | patched (v3-3) | eic.yaml:640-680 reads `sche.any` [C] |
| 34 | `scope.k1` out of `scope.schedule1`; split question (partnership/S corp vs estate/trust); `$k1p`/`$k1s` roster behind it; `scope.passive` reworded to exclude K-1 businesses; coverage rows; personas; walks | **missing (blocks)** | scope.yaml:433-442, 1186-1189, 1101-1111 [C]; k1p rows parked [C x2-k1p_work/coverage_k1p.yaml]; no k1s rows written [C x2-k1s.md:91-97] |
| 35 | tree.json placement of the new gates (`k1p.qbi_release`, `k1s.qbi_release`, `person.k1_se_any`); consumers.json rulings for new reads | missing | mechanical |
| 36 | Class M fixtures and mutation for k1p, k1s, f8582 with the new lines | missing | mutate runs at integration [C x2-k1p.md:126] |
| 37 | NY: IT-225 screen already names pass-through modifications; NY line 11 follows federal line 5 [I]; MCTMT note relies on federal SE refusal [C ny_it201.yaml:1810] | done [I] | recheck when D2 wires SE |

## 2. The patches

Scratch: `P/scratch/round4-k1int/` (`a/` = xint copies; `b1`, `b2`, `b3`, `b4` = after each patch; `gen.py` and
`fixtures.py` regenerate them; `check.py` parses every form, resolves every reference and checks the display rule).
Checks run [S]:
- All edited YAML and JSON parse.
- Line ids are unique, and every reference in the edited forms resolves. The only unresolved names are year
  parameters, as in xint.
- No `display:` remains on a line that is now read, and no new unread line lacks one.
- The four patches apply in order to fresh copies and reproduce `b3`/`b4`.
- New YAML anchors are `&id210`/`&id211` (k1p) and `&id310`-`&id312` (k1s), clear of v2's `&id201`-`&id206` and
  `&id301`-`&id305`.

Not run: build, render, test-fixtures, citations, tree, consumers.

### k1int-1-f8582.patch (prerequisite of BUG-0842 and BUG-0885)

| File | Hunk |
|---|---|
| k1p.yaml | For activities 1 to 3, mirroring `rental.p6c`…`rental.carryforward` [C rental.yaml:1806-1948]: `b2_p6_on`, `b2_p6c_share`, `b2_p6c`, `b{n}_p7a`, `b{n}_p7_on`, `b{n}_p7c_share`, `b{n}_p7c`, `b{n}_allowed`, `b{n}_carryforward` (display), `p7a`, `col_g`. `display` is dropped from `b1_overall_loss` and `b3_overall_loss`, which are now read |
| k1s.yaml | Same chain, plus the per-activity losses k1s lacked: `b{n}_loss_sum` (passive loss after basis plus prior-year loss), `b{n}_overall_loss`, `p6_loss_raw`/`p6_loss`. Totals are guarded by `k1s.ok` like the other k1s outputs |
| person.yaml | `person.k1p_total_p7a`, `k1p_total_col_g` (display until patch 3), `k1s_total_p6_loss`, `k1s_total_p7a`, `k1s_total_col_g`; a new block `person.k1_p4_income` … `k1_p7a` (partnership plus S corporation); `display` dropped from the 13 Part IV/V/VI totals now read |
| f8582.yaml | `f8582.line1a_k1` … `p7_total_k1` (sum over person). `p4a`…`p5c`, `p6_total` and `p7_total` become `sum(rental, k1)`. The form note is updated |

### k1int-2-ebl-qbi.patch (BUG-0842, BUG-0885)

| File | Hunk |
|---|---|
| k1p.yaml | `ebl_loss` = box 1, 2, 3 losses before the passive limit. QBI: `qbi_loss_abs`, `qbi_limited` (code Z loss and a passive box 1 net loss), `qbi_loss_allowed` = prorate(code Z loss, `b1_allowed`, `b1_net_loss`), `qbi_neg_allowed`, `qbi_after_pal`, `qbi_release` (gate: a prior-year box 1 loss allowed this year with code Z), `has_se_pos`, `qbi_se` (guarded) / `qbi_se_share` = prorate(`person.se_line13`, `se_pos`, `person.se_pos_whole`), `qbi` (refuses on `qbi_release`) |
| k1s.yaml | `ebl_loss_raw` (np_loss + p1/p2/p3 losses after basis) and `ebl_loss` (guarded); the same QBI chain on code V. `k1s.qbi` takes `qbi_after_pal`, its label says "after", and it refuses on `qbi_release` after `qbi_cut` |
| person.yaml | `k1p_total_ebl_loss`, `k1p_total_qbi`, `k1s_total_ebl_loss`, `k1_ebl_loss`, `k1_qbi`, `se_pos_whole`. `person.qbi` = `sc_qbi` (the old sum) + `k1_qbi`. `display` dropped from `k1p_total_se_pos` and `k1s_total_qbi` |
| sc.yaml | `sc.qbi_se_pos` whole becomes `person.se_pos_whole` (D-K8). There is no change while 14 A is refused, because then the whole equals `positive_profits` [I] |
| s1.yaml | `s1.ebl_k1_abs`, `s1.ebl_k1`; `s1.ebl_total` adds `s1.ebl_k1`. The `s1.ebl` label is widened. **Remedy text kept** ("A Schedule C loss …"), because fixtures pin it [C fixtures/2025/s1.json:350]. Rewording it to "A business loss …" is optional (D1) |
| qbi.yaml | `qbi.k1_total`, `qbi.has_business`; `qbi.suspended_if_business` is now guarded by `has_business` (Schedule C or K-1 QBI) instead of `s1.has_sc` |
| ambiguities | `amb.2025.k1p_qbi_passive` (scale by allowed share; refuse a release) |

**Why before the passive limit.** If the screen took the allowed loss, the chain would be `s1.ebl` → `k1p.b1_allowed`
→ `f8582.p7_C` → `f8582.line9` → `line6` (MAGI) → `s1.line10_ex5` → `s1.line3`, which refuses when `s1.ebl`: a cycle
[C s1.yaml:198-301, 350-367; f8582.yaml:386-406]. Part I avoided it the same way. Form 461 (now archived) takes
Schedule 1 line 5, which is after the passive limit [C sources/2025/f461.txt lines 2-5], so the pre-limit count
over-refuses a filer whose passive loss is largely held back. Encoding Form 461 itself is plan step L8.

### k1int-3-return.patch

| File | Hunk |
|---|---|
| person.yaml | `person.k1_col_h/col_g/col_i/col_k/nonpassive/interest/ord_div/st_gain/lt_gain/collectibles/unrecap_1250/backup_wh/taxexempt_int`, `k1_count_sche`. `display` dropped from the 27 k1p/k1s totals now read. New gate `person.k1_se_any` (14 A ≠ 0) refuses at `person.se_line2`, ahead of `se_screened`. Cite f1040sse line 2 |
| sche.yaml | `line29a_h`, `29a_k`, `29b_g`, `29b_i`, `sche.zero`, `line30`, `line31_abs`, `line31`, `line32`. `line41` = 26 + 32. `nonpassive_net` = royalties + `sche.k1_nonpassive`; new `sche.roy_net`, `sche.k1_rows`. `sche.any` = rental rows or K-1 rows (old expression kept as `sche.any_rental`). New `sche.filed` (scope.rental ∨ K-1 rows). Note updated |
| s1.yaml | `s1.line5` guarded by `sche.filed` instead of `scope.rental` |
| sb.yaml | `sb.interest_forms` (the old sum), `sb.k1_interest`, `sb.k1_ord_div`; lines 2 and 6 add them (refusals unchanged) |
| f1040.yaml | `f1040.k1_taxexempt` → line 2a; `f1040.k1_backup_wh` → line 25c |
| sd.yaml | lines 5 and 12 = sum over person of K-1 short/long-term gain (refusal on `sd.other_forms` kept); labels |
| g28.yaml / u1250.yaml | `g28.line4` Dollars, + `g28.k1` (amb); `u1250.line5` + `u1250.k1` |
| f8960.yaml | `f8960.k1_nonpassive`; line 4b Dollars = −(K-1 nonpassive net) (column (k) includes 4a guaranteed payments, which are not NII) |
| ambiguities | `amb.2025.k1_collectibles_loss` |

Not in patch 3 (they are question changes, which the interview protocol governs; plan L1):
- `scope.k1` and its split
- `scope.passive`
- the `f1040.line25c_other` source
- `f8960.unsupported`
- `person.se_screen`
- `qbi.unsupported` label
- line 3a

## 3. Fixtures (`fixtures/2025/k1int.json`, hand-predicted)

Single filer, defaults for everything not stated. `scope.k1` defaults to false, and these lines are not behind it, as
with the existing x2k1p cases [C v2/k1.md:74-76].

| Case | Inputs | Expected (derivation) |
|---|---|---|
| `k1int.p5_suspended` | limited partner, box 2 −12,000 | line 2b −12,000, line 3 −12,000, line 9 0, line C 12,000; b2_p7a 12,000, p7c 12,000 (ratio 1), allowed 0, carryforward 12,000, col_g 0; required true |
| `k1int.p4_allowance` | general, active (decisions, tenth), box 2 −12,000 | Assumes MAGI 0 from defaults [I]: line 8 25,000, line 4 12,000, line 9 12,000, p6_total 12,000, b2_p6c 12,000, p7a 0, C 0, allowed 12,000, col_g 12,000; exception holds (required false) |
| `k1int.passive_qbi_prorate` | LP box 1 −10,000 (no work), code Z −10,000; second K-1 box 3 +4,000 | line 2a 4,000, 2b −10,000, line 3 −6,000, C 6,000; b1_p7c 6,000, allowed 4,000, col_g 4,000; QBI 10,000 × 4,000/10,000 → −4,000; person.qbi −4,000 |
| `k1int.prior_release_refuses` | box 1 +5,000, prior box 1 8,000, code Z 5,000 | overall loss 3,000, C 3,000, p7c 3,000, allowed 5,000, carryforward 3,000; `k1p_total_qbi` refused at `qbi_release` |
| `k1int.ebl_k1p_refuses` | box 1 −400,000, test 1 | col_i 400,000, ebl_loss 400,000, s1.ebl_total −400,000, s1.ebl true, s1.line3 refused (Form 461; existing remedy/cite) |
| `k1int.ebl_k1s_under` | S corp box 1 −300,000, test 1, basis 500,000 | col_i 300,000, ebl_loss 300,000, s1.ebl_total −300,000, s1.ebl false |
| `k1int.k1s_qbi_passive` | S corp box 1 −10,000 passive, V −10,000, basis 20,000 | overall 10,000, p7c 10,000, allowed 0, carryforward 10,000, col_g 0; qbi 0 (was −10,000) |
| `k1int.sche_part2` | LLC box 1 +20,000 (test 1), box 5 300; LP box 2 −12,000 | 29a (k) 20,000, (h) 0, 29b 0/0, line 30 20,000, 31 0, 32 20,000, 41 20,000, sche.any true, s1.line5 20,000, sb.line2 300, f8960.line4b −20,000, C 12,000 |
| `k1int.se_14a_refuses` | general, box 1 20,000, 14 A 20,000 | `person.se_line2` refused at `person.k1_se_any` |

Refusal cites carry the snapshots existing fixtures use for i1040sc, i8995 and f1040sse [C]. **Unverified:**
- the MAGI-0 assumption in `p4_allowance`;
- that a non-class-M file named `k1int.json` takes defaults (the x2k1p cases do [T v2/k1.md]);
- that `refusal` expectations on `person.se_line2` and `k1p_total_qbi` name the gate path as written;
- every value, since nothing was run.

Siblings with existing cases: `x2k1p.prior_box1_partly_used` and `fk3*` assert per-K-1 lines that patch 1 does not
change. The only existing fixture that asserts a K-1 `qbi` line is `k1s.refuse_qbi_basis_cut` [C fixtures/2025/k1s.json:858].
It refuses at `qbi_cut`, which still comes first, so it is unchanged [I].

## 4. Coverage estimate effect

| categories.json entry | Now [C tools/coverage/categories.json] | After the lift |
|---|---|---|
| `partnership_scorp` (gates `scope.schedule1`; IRS max of partnership/S corp counts, 5,554,014 returns, 3.5%) | refused | Its gate no longer refuses it. Either `refused: false` (the schedule_c convention: residual refusals unmeasured) or a gate list of the residual K-1 gates (D7) |
| `estate_trust` (gates `scope.schedule1`) | refused | unchanged, if `scope.k1e` stays in `scope.schedule1` |
| `rental_royalty` | refused: false | unchanged |

**Headline (read-only, from `reports/2025/filer_coverage.json`, estimator not rerun):** central 85.9% now.
- Covering the whole schedule_e group would gain +2.33 points (`gain_if_covered_alone.schedule_e` = 0.023305),
  giving 88.2%.
- Partnership/S corp alone gains at least that, less the estate/trust share (0.43%), so between +1.90 and +2.33.
- **New central headline: 87.8%–88.2%.**

This bounds the measured situations only. While box 14 A refuses (D2), every general partner or LLC member with
self-employment earnings is still refused. The microdata does not separate them, so the flip overstates until the SE
wiring lands. Running `estimate.py` after the 02:15 check would give the exact figure. Inputs: `.engines/venv`, the
microdata cache. I did not run it (CPU rule).

## 5. Sized plan for the rest (after v2 k1p/k1s and v3 1-4 land)

| Step | Work | Class / model | Size |
|---|---|---|---|
| L0 | Land v2 k1p, v2 k1s (without its two `qbi_passive` hunks), then v3 1-4; run build, render, citations, test-fixtures, tree.py, check_consumers, tick-groups in a lane worktree; fix what the build finds | mechanical, Sonnet (judgment on build failures) | 2-3 h incl. check time |
| L1 | Interview, for the lift (protocol normative): split `scope.k1` (D6) and leave `scope.k1e` in `scope.schedule1`; gate `$k1p`/`$k1s` on it; reword `scope.passive` (exclude a K-1 business); reword `f1040.line25c_other` (exclude K-1); `f8960.unsupported` (drop "pass-through", keep "business" for others); `qbi.unsupported` label; take `scope.k1` out of `scope.schedule1`; move the 10 k1p coverage rows, write ~8 k1s rows, personas 15/17, walks; update `scope.k1` row ends (N9) | judgment, Opus | 4-5 h incl. question reviews |
| L2 | Line 3a (D3): rename the input to `f1040.line3a_entered` and sum K-1 qualified dividends (599 facts / 16 fixture files restated by script), or add a helper the readers take | mechanical, Sonnet | 1-2 h |
| L3 | SE for 14 A (D2): Schedule SE line 2, drop the 14 A clause from `person.se_screen`, `dc_earned`, `s8812` earned income, SEP/SIMPLE base and Form 7206 for partners (or refuse those), NY MCTMT note; remove the interim refusal | judgment, Opus | 3-4 h |
| L4 | Form 4952: refuse K-1 box 20 A/B (`person.k1p_count_inv`), or wire it | mechanical | 0.5 h |
| L5 | Class M cases and mutation for k1p, k1s, f8582, s1, sche; defaults none new | mechanical | 1-2 h |
| L6 | Reviews, one per form per round. Transcription line-scoped: k1p, k1s, person, f8582, s1, qbi, sc, sche, sb, f1040, sd, g28, u1250, f8960. Class M: f8582, k1p, k1s, s1, sche, f8960, qbi, person. Render for new/changed lines. Question/screen reviews for the L1 wording. Estimate first with `rerun_all.py --dry-run`; the $3.00 gate applies | paid | estimate not run |
| L7 | `categories.json` (D7) and an `estimate.py` rerun; COVERAGE.md | mechanical | 0.5 h |
| L8 (optional) | Encode Form 461 (now archived) in place of the pre-limit screen | judgment | 2-3 h |
| L9 | Rendering: Schedule E line 28 rows and line 27, Schedule B Part I K-1 payers, Form 8582 worksheet rows for K-1 activities | judgment | 2 h [I: render mechanism not read] |
| — | Lane A's BUG-0836 must land before the lift (K-1 Part IV rows read line 9) | — | in lane A |

Bug-entry text for xint's inventory (uncommitted). Format: `- **Fix:** amount, lane A5-k1int (claude-opus-5-5,
judgment).`
- **BUG-0842.**
  - Excess business loss: `s1.ebl_total` adds the K-1 losses in boxes 1-3 before the passive limit
    (`k1p.ebl_loss`, `s1.ebl_k1`). This is amb.2025.s1_ebl_rental's reading; the allowed loss would be circular.
  - QBI: `k1p.qbi` scales a code Z loss by the allowed share of a passive box 1 loss (i8995 p. 3), refuses a
    prior-year release, and takes off the attributable SE tax.
  - Fixtures: `k1int.ebl_k1p_refuses`, `k1int.passive_qbi_prorate`, `k1int.prior_release_refuses`.
- **BUG-0885.** Same, on `k1s.ebl_loss` (after basis). Fixture `k1int.ebl_k1s_under`. Sibling `k1s.qbi`, passive
  prorate: `k1int.k1s_qbi_passive`.

## Owner decisions needed

- **D1. Excess business loss reading.** Patch 2 counts K-1 losses in boxes 1-3 before the passive limit, as Part I
  already does (over-refuses only). The alternatives are box 1 only (the bug entries' "trade or business" losses), or
  encoding Form 461, which is now archived and works from amounts after the passive limit. And should the `s1.line3`
  refusal remedy change from "A Schedule C loss …" to "A business loss …"? That restates the fixtures that pin it.
- **D2. Partnership self-employment earnings (box 14 A).** Option 1: keep refusing them. Patch 3 makes that
  mechanical, but it leaves most working partners refused. Option 2: wire them into Schedule SE, the child care and
  child tax credit earned income, and the retirement-plan base (L3, 3-4 h). This sets how much of the coverage gain
  is real.
- **D3. Form 1040 line 3a.** Option 1: turn the input into "entered" plus K-1 qualified dividends (599 fixture facts
  restated by script). Option 2: keep the input and have readers take a new total (the printed line would then omit
  K-1 dividends).
- **D4. QBI.** Accept `amb.2025.k1p_qbi_passive`: scale by the allowed share and refuse a prior-year release. Also,
  should `k1s.qbi_cut` (a loss limited by basis) use the same i8995 p. 3 ratio instead of refusing? Its ambiguity's
  premise, that no archived text gives the method, looks wrong.
- **D5. Collectibles loss on 28% worksheet line 4.** Option 1: enter it signed (the K-1 instructions say gain or
  loss). Option 2: refuse it.
- **D6. Split `scope.k1`.** Make "partnership or S corporation" one question and "estate or trust" another
  (`scope.k1e`, still refused), or keep one question with a follow-up tick?
- **D7. `partnership_scorp` in categories.json.** Option 1: `refused: false` now, which overstates while 14 A
  refuses. Option 2: keep it refused until D2 is wired. Option 3: re-gate it on the residual K-1 gates.
- **Pending from decisions.md:** memo item 5 (ask the held-back-loss question of every partnership K-1) and the D-K2
  watch. The v2 notes leave both open.

## Provenance

Inspected:
- In xint: the K-1 contracts and integration plan, the x2-k1p/x2-k1s/xint lane notes, `P/med-k1sche.md`,
  `P/patches/v2/k1.md`, `P/decisions.md` items 4-5.
- The forms read at the lines cited: k1p, k1s, f8582, rental (template), sche, s1, person, qbi, sc, f8960, sb,
  f1040, sd, g28, u1250, scope, eic.
- Sources: f461, i8995 p. 3, i8995a FIFO, i1040sd line 4.
- The spec on `prorate`; categories.json and the existing coverage report.
- Patches: generated from copies, parsed, reference-checked and dry-applied, and v2 composition tested [S].

Inferred (unverified):
- that the build accepts the new lines, guards and types;
- every fixture value;
- the absence of cycles beyond the one traced;
- that `sum_over person` lines may be read by return-level forms as written (the existing `f8995.line2` does the
  same [C]);
- rendering behaviour;
- NY effects;
- the coverage bound's tightness.

Gap I could not close: the interview roster gating mechanism for `$k1p`/`$k1s` (questions.yaml not read), which L1
must settle.
