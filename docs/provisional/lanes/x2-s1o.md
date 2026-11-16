# Lane x2-s1o: other Schedule 1 income (ranks 1 to 4 of scout-s1-other)

Model: claude-opus-5-5 · Class: judgment · Year: 2025 · Jurisdiction: us · Worktree:
`.claude/worktrees/x2-s1o` (base `825024d8`, x1-base, plus lane x1-digital's in-progress `s1.line8v`). No paid
reviews, no model calls, no commit. check-all not run (brief). Status of each check: section 8.

Evidence marks: **[run]** run and seen in this worktree; **[read]** read in a source or file; **[inferred]** not checked.

## 1. What the merge must know

- **Build base.** `fixtures/2025/defaults.json` is `nx-b1`'s copy (the brief's base caution) plus
  `/tmp/mfs-x2-s1o/defaults_patch.py`: 36 defaults of this lane (`LANE`) and, build-only, x1-digital's two
  (`f1040.digital_assets`, `s1.digital_amount`; `--with-digital`). Re-apply the lane's 36 with
  `python3 /tmp/mfs-x2-s1o/defaults_patch.py fixtures/2025/defaults.json` on the integrated file.
- **Source overlay (not this lane's).** This worktree's `sources/2025`, `sources/2026`, `tools/sources/2025.json` and
  `tools/sources/2026.json` carry the source lane's archive (copied from `x2-k1e`, same base, which carries `nx-src`'s
  additions: i172, f172, usc-26-172, p536, p596, p4801, among others). Citations to `i172` need it. Take those files
  from the source lane at integration, not from this tree.
- **Shared form files, lines touched** (all other lines untouched):
  - `s1.yaml`: new lines `s1.options_amount`, `s1.line8k`, `s1.inmate_amount`, `s1.line8u`, `s1.f8853c_total`,
    `s1.line8e`, `s1.oi8z_total`, the NOL block (`s1.nol_amount`, `_if_nol`, `s1.nol_pre2018`(+`_if_nol`),
    `s1.nol_ebl`(+`_if_nol`), `s1.nol_joint`, `s1.nol_separate`, `s1.nol_not_married`(+`_if_joint`),
    `s1.nol_was_joint`(+`_if_separate`), `s1.nol_marital`, `s1.line8a`, `s1.nol_ti`, `s1.nol_ti4`,
    `s1.nol_limit_test`, `s1.nol_limit`); changed `s1.line8z` (now `sum` of `s1.oi8z_total` and `rec.to_line8z`),
    `s1.line8_other` (three disjuncts removed: `s1.stock_options_if_options`, `s1.ltc_payout`, `s1.inmate_wages`;
    cite trimmed to 8m and 8t) and **`s1.line9`**: type `NonNegDollars` → `Dollars`; **operands added: `s1.line8a`,
    `s1.line8e`, `s1.line8k`, `s1.line8u`** (x1-digital's `s1.line8v` kept as it was); its line cite now lists only what
    stays refused. Its refusal entry (remedy wording) is unchanged. MFS lane L2 also owns `s1.yaml` (line 20 box).
  - `f1040.yaml`: one `refuses:` block added to `f1040.line15` (`s1.nol_limit`). MFS lane L1 owns the file.
  - `scope.yaml`: `scope.recovery` and `scope.nol` removed from `scope.schedule1`'s `any:`, and their two quotes from
    its cite. The inputs themselves are unchanged. MFS lane L1 owns the file.
  - `s2.yaml`: `s2.amt_l4_sum` adds `s1.nol_amount_if_nol` (label and cite updated). Fix lane F7b works in `s2.yaml`;
    its copy of this line was identical to the base when checked.
  - `refund.yaml`: `refund.taxable` is now a switch (`rec.path` → `rec.to_line1`, else new `refund.taxable_1040`, the
    old expression with its ambiguity); its three refusal entries are unchanged; the form note reworded.
  - `oi8z.yaml`: three enum kinds; `oi8z.no`, `oi8z.damages`, `oi8z.injury`, `oi8z.injury_if_damages`; one refusal entry
    added to `oi8z.taxable` (before `oi8z.figured`); note and kind-list source updated.
- **New forms:** `forms/2025/rec.yaml` (Pub. 525 Worksheets 2a and 2), `forms/2025/f8853c.yaml` (Form 8853 Section C,
  collection). **Params:** `f8853c.per_diem_limit` ($420); enum `other_income_kind` + `fiduciary_fees`,
  `found_property`, `taxable_damages` (before `other`).
- **Ambiguities:** new `amb.2025.rec_two_returns`, `rec_mortgage_cap`, `rec_ratio_places`, `rec_line5`,
  `rec_prior_taxable`, `s1_nol_limit_test`, `f8853c_period`; `amb.2025.line8z_kinds` chosen/status amended (D2).
- **Bank (`questions.yaml`):** frame `f8853c`; groups `nol_facts`, `rec_rare`, `rec_kinds`; new entries at 146/14,
  161/16–31, 165/21–33, 258/10–14, 294/4; helps changed on `scope.recovery`, `scope.nol`, `s1.ltc_payout`,
  `s1.inmate_wages` (tick help removed), `s1.stock_options`, `refund.itemized`, `$oi8z`, `oi8z.kind` (three labels).
- **Coverage rows, ends restated** (owner decision D7): `scope.recovery`, `scope.nol`, `scope.nol_casualty_no_business`
  (`coverage/scope.yaml`), `other.options_income_not_on_w2`, `other.ltc_payout`, `other.inmate_wages`
  (`coverage/other.yaml`). New file `coverage/s1_other.yaml` (this lane's).
- **`changes/2026/f1040.yaml`:** C-PRI-18 op 5 restated (section 8).
- **Personas:** `21_money_back_itemizer`, `22_refused_old_loss` (not walked).
- **Fixtures:** see section 8 (new files `rec.json`, `f8853c.json`; cases appended to `s1.json`, `oi8z.json`) and the
  restatements listed there.

## 2. What changed

(See section 1 for ids.) Computed now:

| Situation | Where |
|---|---|
| Money paid back in 2025 for 2024 itemized deductions (property tax, mortgage interest, medical, other), alone or with a state income tax refund: Worksheet 2a (the 2024 SALT limit) and Worksheet 2 (standard deduction limit, negative 2024 taxable income, the split between line 1 and line 8z) | `rec`, `refund.taxable`, `s1.line8z` |
| Line 8z: fees as a nonprofessional executor, found property, taxable damages not for a physical injury | `oi8z` |
| NOL carryover on line 8a when the carryover is at most four times taxable income after it | `s1.line8a`, `s1.line9` |
| Form 8853 Section C, one insured, one LTC period: per diem and periodic accelerated death benefits against $420 × days or the costs, less reimbursements | `f8853c`, `s1.line8e` |
| Line 8u (inmate pay), line 8k (stock option income not on a W-2) | `s1.line8u`, `s1.line8k` |

## 3. Decisions (each with the alternative rejected)

- The parent of the recoveries stays the existing input `scope.recovery` (removed from `scope.schedule1`), not a new
  `rec.any` with `scope.recovery` derived. Rejected: renaming, which would touch every case and row that names it for
  no change in meaning; the wording already asks the fact.
- The 2024 Schedule A facts are the refund worksheet's own inputs (`refund.itemized`, `line5d/5e_prior_year`,
  `line17_prior_year`, `status`, the age and blindness boxes): one fact, one asker. `refund.exc_tax` and
  `refund.exc_who` refuse in the rec path too (at `rec.line11`, with rec remedies). Rejected: new rec screens.
- The children of `scope.recovery`: the three refusing facts in tick group `rec_rare` right after the money group
  (161/28–30), told before any amount; the kinds in tick group `rec_kinds` (165/21–24) after the refund block, since
  they hang on `refund.itemized` (165/7). Rejected: four amount questions "give 0 if none" (four steps instead of one).
- Line 10 of Worksheet 2: a Yes/No on 2024 line 15 first; lines 11 and 14 asked only on No (`amb.2025.rec_prior_taxable`).
- Line 5 of Worksheet 2 is zero (`amb.2025.rec_line5`). Ratios to six places (`amb.2025.rec_ratio_places`).
- Mortgage refund capped in the question, medical refund capped by a second question (`amb.2025.rec_mortgage_cap`).
- The kind `recovery` of line 8z keeps its refusal unchanged (fixture remedies compare whole); `$oi8z` help now sends
  recoveries to their own questions. Rejected: dropping the enum value (restates fixture inputs). Residual N8 overlap:
  for the owner.
- `misc_box3` (scout D2 list) not added: no recipient-side citation in the archive.
- NOL: the refusals that are facts (`s1.nol_pre2018`, `s1.nol_ebl`, `s1.nol_marital`) sit on line 8a, told at their
  topic; only the arithmetic test sits on line 15 (a refusal on 8a reading lines 11b and 14 would be a cycle). The
  marital refusal is the scout's gap: i172 p. 3 (Change in Marital Status) was not in the scout's list.
- AMT (D4): line 2e added to the screen's upper bound; rejected: refusing an NOL above a size.
- Form 8853: lines 14a, 14b and 16 are not shown (no amount depends on them); one LTC period (equal payment rate method),
  a rate change refused (`amb.2025.f8853c_period`).
- 8k is not earned income for EIC (EIC reads line 1z; i1040gi line 8k says "not otherwise reported on ... line 1h",
  other earned income) [read]. 8u is not EIC earned income (p596, "Earnings while an inmate") [read].

## 4. Gates replaced and residual refusals

Removed from `scope.schedule1`: `scope.recovery`, `scope.nol`. Removed from `s1.line8_other`: 8e, 8k, 8u. New residual
refusals (each cited, a coverage row each; `tools/coverage/tree.json` placement **not done**, see 7):
`rec.not_2024_if_any`, `rec.nonitemized_if_any`, `rec.sales_tax_if_any`, `rec.two_returns_if_joint` (at
`rec.to_line8z`), `refund.exc_tax`/`refund.exc_who`/`rec.nol_negative` (at `rec.line11`), `s1.nol_pre2018_if_nol`,
`s1.nol_ebl_if_nol`, `s1.nol_marital` (at `s1.line8a`), `s1.nol_limit` (at `f1040.line15`),
`f8853c.others_paid_if_periodic`, `f8853c.rate_changed_if_periodic` (line 21), `f8853c.pre1996_if_reimbursed`
(line 25), `f8853c.nonqualified_if_periodic` (line 26), `oi8z.injury_if_damages`.
Unchanged: `s1.line8_other` (8m, 8t), `oi8z.recovery`, `oi8z.figured`, `scope.archer_msa` (Form 8853 A/B).

## 5. Next year

Edited: `changes/2026/f1040.yaml` (C-PRI-18, op 5) as section 8 says. The 2026 copy of the `s1.nol_limit` remedy still
says "carried into 2025"; it needs a wording operation with the rest of the NOL lines.


`changes/2026/` exists (7.1). Not written this lane, for the reason and with the facts below:
- `f8853c`: the 2026 Form 8853 and its instructions are not archived. The parameter moves 42000 → 43000
  (rp-25-32 p. 34, "For calendar year 2026, the stated dollar amount of the per diem limitation ... is $430") [read]:
  for the next `propose_params.py --from 2025 --to 2026`. The labels quoting $420 move with the form, awaited.
- `rec`: every year in its wording moves (2024 → 2025, 2025 → 2026), and with it the prior-year standard deductions read
  through `refund.*`. `refund` has no 2026 operations yet (no `changes/2026/refund*.yaml`) [run: ls], so the two move
  together; Pub. 525 2026 draft and i172 2026 draft are archived (`sources/2026/manifest.json`) [read]. Left for a
  next-year lane with `year_changes.py --record`.
- `s1`, `oi8z`, `f1040`, `scope`, `s2` lines added here: no 2026 operation written; the 2026 f1040s1 draft keeps 8a,
  8e, 8k, 8u, 8z (scout [T]).
`year_changes.py --check`: see section 8.

## 6. Defects

None filed.

## 7. For other lanes and requests

- Integrator: `tools/coverage/categories.json` — `nol` (gate `scope.schedule1`) and `other_income` no longer match the
  forms: the NOL now refuses only at `s1.nol_*` gates; split `other_income` by line once SOI Pub. 4801 (archived by the
  source lane as `p4801`) is read; correct `form4797`'s gate to `sd.other_forms`. `tree.json` l.44 still names the NOL
  in `scope.schedule1`'s question; place the new gates of section 4.
- Integrator: `interview/2025/gate_frequencies.yaml` entries for the new gates.
- Owner: residual N8 overlap of the line 8z kind `recovery` with `scope.recovery` (drop the kind with a fixture
  restatement).
- Owner: the remedies of `s1.line9` (line8_other), `f1040.line8`/`line10` (scope.schedule1) and `oi8z.figured` list
  what the tool computes and are now incomplete; left unchanged because fixtures compare the remedy whole.
- Engine differential: none of OpenTaxSolver, UsTaxes, PolicyEngine-US or Tax-Calculator computes Worksheet 2,
  Form 8853 Section C or the NOL limit (scout [T]); that is the trust gap.

## 8. Verification

All in this worktree. Per the coordinator's deadline message (14:35), verification is limited to the lane's own
fixtures and coverage rows, `citations.py --strict` and `year_changes.py --check`; no full test-fixtures verdict on the
broken base, no mutate.

| Command | Result |
|---|---|
| `node engine/dist/main.js build` (after the last model change) | [run] `build OK` (canonical written) after the last model change (f8853c refusals moved to line 26) |
| Own fixture cases, evaluated against hand predictions written first (`/tmp/mfs-x2-s1o/fx/*`, compared by `/tmp/mfs-x2-s1o/bin/check_cases.py`) | [run] all 60 predicted values of the 46 new cases equal the evaluator's (no prediction or value edited); refusal objects are the evaluator's |
| `test-fixtures` (federal), before the last f8853c refusal move | [run] every lane case and both restated cases `ok`; 619 failures, all base: 598 `s2.amt_owed` not declared (stale input in class M/mutation cases), 74 values `sd.qof`/`s2.mortgage_subsidy` missing (base defaults), and `classm.s1.1`–`13` missing `scope.nol` (this lane's; fixed, see 1) |
| `test-fixtures --ny` | [run] failures all base (`s2.amt_owed` ×214, `sd.qof` ×5); none from this lane. Scan of NY `classm`, `classm.deepseek`, `mutation` with `s2.amt_owed` stripped: no lane input unknown [run] |
| `tick-groups` | [run] rc 0, 48 groups, 0 problems (new groups lie behind answers the background does not give) |
| `interview-coverage --rows coverage/s1_other.yaml` | [run] 20 rows, 0 problems. Seen in the walk: `s1.nol_limit` is told only at the end of the return (on the last answer, `qbi.coop_patron`), since line 15 needs every line before it; the factual NOL refusals are told at 258, the recovery refusals at 161, and `refund.exc_tax` refuses a rec filer at 165/10, before the kinds are asked |
| `interview-coverage` on the six restated rows (copy in `/tmp/mfs-x2-s1o/restated_rows.yaml`) | [run] `scope.recovery`, `other.options_income_not_on_w2`, `other.ltc_payout`, `other.inmate_wages`: 0 problems; `scope.nol`, `scope.nol_casualty_no_business` after their answers were completed (W-2 screens, `scope.passive`, `scope.f8978`, `s179.prior_form`): 0 problems (`/tmp/mfs-x2-s1o/restated2.yaml`). The full `scope.yaml` and `other.yaml` files were not walked whole (deadline) |
| `interview-rules` | not run to the end (deadline) |
| `citations.py --strict` | [run] rc 0, 0 findings (after fixing six quotes this lane wrote: pages and page-spanning quotes) |
| `year_changes.py --check` | [run] all 1256 operations apply, after resolving one collision: `changes/2026/f1040.yaml` C-PRI-18 op 5 set `f1040.line15 refuses` from `null`; its `from`/`to` now carry this lane's `s1.nol_limit` entry first (the later lane resolves, protocol 8.4) |
| `check_consumers.py` | [run] 18 new pairs on this lane's lines, need rulings (round 2); stale entries for the retired pairs |
| `check_questions.py`, `check_screens.py`, `check_false_no.py` | [run] refused to run: stale rendered text (render not rerun) |
| `siblings.py --check`, `check_bug_inventory.py` | [run] failures all base (pending bug files of other lanes) |
| `mutate`, Lean comparison, engine differential, check-all | not run |

Consumer pairs to rule: `f8853c.nonqualified@i8853:p8`, `f8853c.others_paid@i8853:p9`, `scope.recovery@p525:p27`,
`scope.recovery@p525:p28`, `rec.nonitemized@p525:p28`, `rec.sales_tax@p525:p24`, `rec.has_medical@p525:p25`,
`refund.mfs_spouse_itemized@p525:p25`, `refund.status@p525:p25`, `scope.nol@p525:p27`, `refund.exc_who@p525:p27`,
`refund.exc_tax@p525:p27`, `refund.box8@p525:p24`, `refund.box8@p525:p25`, `s1.nol_pre2018@i172:p2`,
`scope.nol@i172:p2`, `scope.nol@i8995:p3`, `scope.nol@i172:p3`. The lane's reading of each is "same" (the question asks
what the page's rule needs); a write of those verdicts was refused to this lane, as it should be.

Restated existing fixtures (approved end changes, N9): `s1.json` `stage16.refuse.s1.line8_other` (lines 9, 10 and Form
1040 line 8: refusal → $5,000, since line 8e with no Section C entry is $0; its refusal is kept by the new case
`x2s1o.refuse.s1.line8_other`, through line 8m); `scope.json` `scope.reg.nol_casualty_no_business` (`scope.ready`:
refusal `scope.schedule1` → true). For the integrator or L5, not edited: `mutation.json`
`mutation.m3.scope.s1_recovery` and `mutation.m3.scope.s1_nol` pin the two disjuncts this lane removed from
`scope.schedule1`; drop both. Class M: `classm.json` `classm.s1.1` to `classm.s1.13` now state `"scope.nol": false`
(13 lines added, nothing else).

## 9. Review debt (round 2)

No dry-run price was taken (no review tool run in this lane). What round 2 must run, by protocol 6.1:

| Subject | Reviews | Scope |
|---|---|---|
| `rec` (new form) | transcription, render, class M | whole |
| `f8853c` (new form) | transcription, render, class M | whole |
| `s1` (8a, 8e, 8k, 8u, 8z, 9, the NOL block, `line8_other`) | transcription, class M; render (new lines) | `--lines auto` |
| `refund` (`refund.taxable`, `refund.taxable_1040`, note) | transcription, class M, render | `--lines auto` |
| `oi8z` (kinds, `injury`, `damages`) | transcription, class M, render | `--lines auto` |
| `f1040` (line 15 refusal), `scope` (`schedule1`), `s2` (`amt_l4_sum`) | transcription, class M | `--lines auto` |
| New gates: `rec.not_2024_if_any`, `rec.nonitemized_if_any`, `rec.sales_tax_if_any`, `rec.two_returns_if_joint`, `rec.nol_negative`, `s1.nol_pre2018_if_nol`, `s1.nol_ebl_if_nol`, `s1.nol_marital`, `s1.nol_limit`, `f8853c.others_paid_if_periodic`, `f8853c.rate_changed_if_periodic`, `f8853c.nonqualified_if_periodic`, `f8853c.pre1996_if_reimbursed`, `oi8z.injury_if_damages` | screen review (kind `gate`) | one sample each |
| `rec`, `f8853c` | completeness; false-no for `scope.recovery`, `s1.ltc_payout`, `f8853c.periodic`, `rec_kinds` | one sample each |
| The 36 new questions and the 8 with changed help (section 1) | question review | per question |
| Consumers: 18 new (input, page) pairs from `check_consumers.py` (listed in section 8) | adjudication (rulings in `reviews/2025/consumers.json`) | — |

## 10. Walks before and after

Not recorded: the "before" walk was not taken before the model changes, and the after walks were not run (deadline).
Personas added for the integrator to walk: `21_money_back_itemizer` (typical: a state refund and a property tax refund
after itemizing for 2024, and a $5,000 NOL carried in) and `22_refused_old_loss` (refused at `s1.nol_pre2018_if_nol`).
The filer with nothing in the area (`01_single_w2`) meets no new question [inferred: every new question sits beneath a
Yes to `scope.recovery`, `scope.nol`, `s1.ltc_payout`, `s1.inmate_wages`, `s1.stock_options` or a line 8z kind].
Coverage gain: unmeasured. `other_income` (4.8%) cannot move until split by line; `nol` (0.6%) is served in part
(post-2017 carryovers within the four-times test).

## 11. Left open, in rank order

1. Ranks 5 to 7 of the scout (Form 4797 for Schedule C property; Coverdell/529; insurance dividends) and D1 (Form 2555):
   not this lane.
2. The 2026 operations for `rec`, `f8853c` and the new `s1` lines (section 5).
3. `tools/coverage/tree.json` placement of the new gates, `categories.json`, `gate_frequencies.yaml` (integrator).
4. The 18 consumer pairs to rule, and the stale consumer entries of the retired pairs (`scope.recovery` ×9, `scope.nol`
   ×8, `s1.ltc_payout`, `s1.inmate_wages`): this lane was not permitted to write rulings itself.
5. Mutation (`mutate`) not run: the brief's base caution (it runs at integration). Mutants to expect on this lane's
   lines are killed by the cases of section 2 (both sides of `rec.w2a_line5_more`, `rec.w2a_cap`, `rec.line11_is_line3`,
   `rec.ti_positive`, the NOL comparator at the boundary, `f8853c.line23`'s two sides, line 26's floor), not run.
