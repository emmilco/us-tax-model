# Lane x1-sche: Schedule E Part I, Form 8582 and rental depreciation (coverage wave X1)

Model claude-opus-5-5, class judgment, year 2025 (plus 2026 operations), jurisdiction us. Worktree
`.claude/worktrees/x1-sche`, base `refs/scratch/x1-base` (825024d8). Design: `scout-schedule-e.md`; process:
`coverage_expansion_protocol.md`. No paid reviews, no model calls; nothing committed; `check_all.sh` not run;
`mutate` not run (coordinator: it runs at integration).

## 1. What the merge must know

- **Base repair, not mine.** The base `fixtures/2025/defaults.json` was broken mid-merge. As the coordinator directed,
  the tree holds `nx-b1`'s `defaults.json` plus this lane's 65 new defaults, applied by `/tmp/x1sche/defaults_patch.py`
  (reads `/tmp/x1sche/defaults_add.json`). At integration take the integrator's `defaults.json` and rerun that script
  (or merge by input id: every new id is `$rental`, `$royalty`, `$rprop`, `rental.*`, `royalty.*`, `rprop.*`, `sche.*`,
  `scope.rent_personal`).
- **Shared forms changed** (distinct lines):
  - `s1.yaml`: new `s1.line5`, new helper `s1.line10_ex5` (the old `s1.line10` sum: lines 1, 2a, 3, 7, 9), `s1.line10`
    now `sum(s1.line10_ex5, s1.line5)`; `s1.ebl_total` now `sum(s1.ebl_sc, s1.ebl_sche)` with new `s1.ebl_sc` (the old
    expression), `s1.ebl_sche_abs`, `s1.ebl_sche`. The digital lane changes `s1.line9`; `s1.line10_ex5` reads it by id,
    so its change flows through untouched.
  - `scope.yaml`: new `scope.rent_personal` + gate `scope.rent_personal_if_rental`; in `scope.schedule1`'s `any` list
    `scope.rental` is replaced by `scope.rent_personal_if_rental`; `scope.passive` wording drops "or rental".
  - `f8960.yaml`: `f8960.line4a` = `copy s1.line5` (Dollars, new label/cite); `f8960.line4c` retyped Dollars;
    `f8960.unsupported` first item "annuity, rental, royalty, business or pass-through income" → "annuity, business
    or pass-through income" (label and source).
  - `eic.yaml`: `eic.step2_other` gains `sche.any = false` and a refusal on `sche.any` (after the `scope.schedule1` one).
- **Restated fixture inputs (no expected value edited):** `t264.eic.step2_schedule1` (eic.json),
  `stage5.refuse.screens` (returns.json), `stage4.refuse.scope.schedule1` (scope.json) used `scope.rental: true` as a
  Schedule 1 refusal trigger; each gains `scope.rent_personal: true` (renting out equipment), which keeps the same
  refusal at `scope.schedule1`.
- **Coverage rows restated:** `scope.rental` and `scope.royalties` (end refused `scope.schedule1` → completed: the
  approved N9 end change, D12); `scope.equipment_rental` answers gain `scope.rent_personal: true` (same end).
- **Personas:** new `19_rental_house` (14, 17, 18 are taken by other X1 lanes); `11_refused_rental` restated to a
  short-stay rental refused at `rental[beach].stay7_if_short` (its old end, `scope.schedule1`, no longer applies to a
  house rental).
- **Bank (`questions.yaml`):** frames `rental`, `rprop`, `royalty`; groups `rental_rare`, `rental_costs_a/b/c`,
  `royalty_rare`, `rental_return`; questions at 130.4 and 130.11–94 (no slot collision found in the base);
  help changed on `scope.rental` (no longer "A Yes ends the interview here") and on `scope.passive`.
- **Other shared files:** `params/2025.yaml` (4 enums: `rental_kind`, `rprop_kind`, `month`, `realty_year`; values
  `rental.*`, `f8582.*`), `ambiguities/2025.yaml` (10 entries appended), `tools/coverage/tree.json` (19 gate
  placements), `tools/check_all_steps.sh` (step `check_realty_tables`), `tools/README.md` (one row),
  `research/ty2026/changes.md` (3 entries after C-BUS-18), `docs/provisional/DECISIONS.md` (one section).
  `categories.json` untouched (integrator, 9.3): `rental_royalty` should list the new gates and drop `scope.rental`.
- **`year_shared_refs`/adoption:** `year_diff.py --adopt` re-derives only `recovery_year`; the new
  `tables/<year>/realty_recovery_year.yaml` (keyed by `realty_year`, before1987 → 40) needs the same rule, and
  `macrs_mm` is re-extracted (`tools/extract_realty_tables.py`) from the next Pub. 946. Request below.

- **Extension points for the K-1 lane** (coordinator request): every Form 8582 column total reads a rental-only
  helper through a `sum`, so a K-1 source adds one operand: `f8582.line1a_rental`, `line1b_rental`, `line1c_rental`,
  `line2a_rental`, `line2b_rental`, `line2c_rental` (copied by `f8582.p4a`…`p5c`, a `copy` the K-1 lane turns into a `sum`, which lines 1a–2c, the exception and
  `f8582.deductions`/`required` read), `f8582.p6_total_rental` (copied by `f8582.p6_total`), `f8582.p7_total_rental`
  (copied by `f8582.p7_total`); MAGI: `f8582.magi_income` is a `sum` whose Schedule E operand is `sche.nonpassive_net`;
  `sche.line41` = `copy sche.line26` (to become a sum with line 32); `sche.any` reads `sche.count` = `sum(sche.rental_count, sche.royalty_count)`
  (and is gated on `scope.rental`, which a K-1 lane must widen); `s1.ebl_total` = `sum(s1.ebl_sc, s1.ebl_sche)`.

## 2. What changed

New forms: `rental` (collection, 138 lines), `rprop` (collection under rental, 14), `rf4562` (implicit under rental,
5), `royalty` (collection, 17), `sche` (return, 29), `f8582` (return, 46). New tables `macrs_mm` (Tables A-6, A-7a,
960 rates, by extractor `tools/extract_realty_tables.py` with `--check`) and `realty_recovery_year` (by hand). Forms were
generated by scripts kept outside the tree (`/tmp/x1sche/gen_rental.py`, `gen_rest.py`) whose locators were found by
searching the archived text; the YAML is the deliverable.

**Computed now:** long-term rentals of real estate (types 1–5), several properties, a filer's share; royalties
(type 6) without depletion; lines 3–26 and 41, Schedule 1 line 5; personal use of a unit not used as a home (every
expense divided by fair-rental days over days of use, six-place ratio); a home rented fewer than 15 days left out;
Form 8582 Parts I–VIII with prior-year unallowed losses, Part V for rentals without active participation, the
$25,000 allowance and its $100,000–$150,000 phase-out, the 2026 carryforward shown (`rental.carryforward`); the
filing exception (form shown only when required); depreciation of buildings and improvements by Table A-6
(1987–2025) and Table A-7a (1994–2025), with Form 4562 lines 17, 19i, 19j, 22 for a property with 2025 property;
Form 8960 line 4a.

**Still refused (gate, reason):** self-rental or other type (`rental.self_rental`); average stay ≤ 7 days
(`rental.stay7_if_short`); significant services (`rental.services`); under 10% owned (`rental.under_tenth`); not for
profit (`rental.not_for_profit`); depletion (`rental.depletion`, `royalty.depletion`); car, truck and travel
(`rental.vehicle`, D5); a home rented 15+ days, profit or loss (`rental.ws51`, D2); a prior loss from a year without
active participation (`rental.prior_not_active_if_both`); a loss not at risk (`rental.not_at_risk_if_loss`);
personal property and land improvements (`rprop.personal`, D3); ADS, basis change, disposition, cooperative stock,
bonus/179 (`rprop.screen`); nonresidential before 1994 (`rprop.early_nonres`); royalties of a trade or business or a
working interest (`royalty.business`); real estate professional, grouping, rental QBI business (`sche.re_pro`,
`sche.grouped`, `sche.qbi_business`); EIC with Schedule E (`eic.step2_other` on `sche.any`, D6); renting personal
property (`scope.rent_personal` → `scope.schedule1`); K-1s, farm, MFS, other passive activities, unchanged.

**Questions added** (prompt = frame + the form line's source unless a bank prompt is given):
- 130.4 `scope.rent_personal`: "Was any of what you rented out something other than a building, a room or land, such
  as a car, a trailer or equipment?"
- (Orders below are the design's 268/269; as built every rental question is 130.(seq+10) and every royalty and
  return-level question 130.(seq+70), see §3.)
- 268.1 `$rental`: "List each house, apartment, room, building or piece of land you … rented out or offered for rent
  in 2025, one entry each."; 268.2 `rental.kind` (7 choices); 268.3 `rental.days_fair` "How many days in 2025 was it
  rented at a fair price? …"; 268.4 `rental.personal_any` "On any day in 2025, did you, your family or another owner
  use it, or did anyone stay free or below a fair rent?"; 268.5 `days_personal`; 268.6 `days_overlap` "Of those days,
  how many were also days it was rented at a fair price …?"; 268.7 `short_stays` "Did renters stay 30 days or less, on
  average? …"; 268.8 `stay7` "Was the average stay 7 days or less?"; 268.9–12 tick group "Is any of these true of this
  rental?" (services; under a tenth; not for profit; depletion); 268.13 `active` "Did you or your spouse help make
  decisions for it, such as approving tenants, setting the rent or approving repairs, even if a manager did the daily
  work?"; 268.14 `rents`; 268.15–28 three cost tick groups (mortgage interest on a Form 1098; other interest; property
  tax; insurance; management fees; commissions | repairs; cleaning and maintenance; utilities; supplies; advertising;
  legal or professional fees | other costs; car, truck or travel costs (refuses)); 268.29–41 the amounts in printed
  order; 268.42 `prior_any` "Was a loss from this rental held back (not deducted) on your 2024 return or an earlier
  one?"; 268.43 `prior_amt`; 268.44 `prior_not_active`; 268.45 `$rprop` "List the building and each improvement to it
  you depreciate …"; 268.46–50 kind, month, year, basis, screen; 268.51 `not_at_risk` (only with a loss).
- 269.1 `$royalty`; 269.2 amount; 269.3–4 tick group (own business or working interest; depletion); 269.5
  `expenses_any`; 269.6–8 amounts; 269.22–24 tick group "Is any of these true of
  your … rentals?" (real estate professional; grouped; QBI business).

**Who could answer No wrongly** (guard): `rental.personal_any` — a relative paying below-market rent (prompt says
"below a fair rent"); `short_stays` — an owner who thinks of a lease length (help gives the average formula);
`prior_any` — a filer whose software held a loss back silently (help: look for Form 8582); `active` — guarded in
reverse (help: most owners answer Yes); `scope.rent_personal` — a landlord of a furnished house (help: furniture
counts as part of the home). Cost/share figures: the scout's §4 table [E], not re-estimated.

## 3. Decisions

All scout decisions D1–D13, D15 settled as recommended; recorded in `docs/provisional/DECISIONS.md` (lane x1-sche).
Lane-level choices:
- Royalty from the filer's own trade or business, or a working interest, refused (`royalty.business`); not in the
  scout (i1040se p. 6, Line 4, "report your royalty income and expenses on Schedule C"). Alternative: route to
  Schedule C silently.
- The at-risk question is asked whenever line 21 is a loss, not only for property placed after 1986 (the scout's
  narrower trigger): over-asks a rare filer, never under-asks.
- EBL (D15) counts losses before the passive limit (`sche.loss_prelimit`): counting the after-limit Schedule 1 line 5
  made a dependency cycle through Form 8582's MAGI (`s1.line3` refuses on `s1.ebl`).
- Form 8960 line 4a copies Schedule 1 line 5 only; i8960 p. 8 says lines 3, 5 and 6, but a Schedule C filer still
  answers Yes to `f8960.unsupported` ("business … income") and line 6 is refused, so the two agree on every return
  that reaches the line.
- Day counts are carried as cents (the engine allows no Count `choose` and `prorate` takes money).
- **Placement (D11 changed by a check):** the property topic was built at 268/269 as the scout recommends, but
  `tick-groups` fails it: a question a tick-box Yes opens (`$rental`, `$royalty`, opened by `scope.rental` in
  `own_income`) must take the group's order number, or it waits behind questions of earlier orders. So the topic sits
  at order 130, directly after the tick group — the scout's alternative for D11.
- **Schedule E lines A and B dropped from the interview and the forms:** as display-only inputs no target reads them,
  so the interview never asked them; making them a target would ask every filer. Left open (§11).
- **Return-level refusals hang on `sche.line26`**, which the return reads; on `sche.line23a` (read by nothing) they were
  never asked.
- `scope.passive` stays gated by `scope.business_before` and loses "or rental"; held-back losses of rentals no longer
  owned are named in its help.

## 4. Gates replaced and residual refusals

`scope.rental` is no longer a `scope.schedule1` trigger; `scope.rent_personal_if_rental` replaces it. `f8960.unsupported`
narrowed (rental, royalty). Residual refusals: §2, all placed in `tree.json` (topic `other_income`, part `rental`;
`sche.any` under `eic`) and walked by rows in `interview/2025/coverage/rental.yaml` (24 rows).

## 5. Next year

`changes/2026/rental.yaml` (C-X1SCHE-RENTAL-01: line 13 → 13b "Other"; 13a vehicle loan not encoded, vehicles refused),
`changes/2026/f8582.yaml`
(C-X1SCHE-F8582-01: MAGI reduced by the deductible part of SE tax, `s1.line15` added to `f8582.magi_adj`); all
`verified: draft`; entries added to `research/ty2026/changes.md`. No change found: f8582 amounts ($150,000, $25,000),
p925. Awaited / to archive: p946 2026 (Tables A-6, A-7a), i4562 2026, Notice 2026-11. New parameters for
`propose_params.py`: `rental.day_cents`, `rental.tenth_cents`, `rental.home_days`, `rental.min_rental_days`,
`rental.one`, `f8582.phaseout_end`, `f8582.special_max`, `f8582.rate`, `f8582.exception_magi`,
`f8582.exception_loss`. New tables at adoption: `macrs_mm` (extract), `realty_recovery_year` (by rule).

## 6. Defects

None filed. Base defects seen (not this lane's): `mutate-worker.ts` imports `sampledShare` absent from `mutate.ts`
(compile error); `defaults.json` mid-merge (coordinator aware); `stage4.sb.foreign_no_filing` fails on the base
(`sb.partIII` false), unrelated to these forms.

## 7. Requests

1. `year_diff.py --adopt`: re-derive `realty_recovery_year` as it does `recovery_year` (before1987 stays 40).
2. Integrator: `categories.json` `rental_royalty` gates → this lane's gates, `refused: false` with the
   "supported; remaining refusals unmeasured" label (scout §1.3); rerun the estimate.
3. Archive Pub. 596 (2025), Rev. Proc. 2019-38, Form 461 and instructions, p946 2026, i4562 2026.
4. Mutation pins: run at integration; the scout §5 lists the expected survivors (boundary tests on the home test,
   15 days, MAGI and loss edges). Fixtures f16, f17, f20 sit on the 14-day, 10% and 15-day edges; f15 on line 4's
   `smaller_of`; f13 on the `where part4` filter; f14 on two Part VI ratios.

## 8. Verification

What was run and seen (on this worktree, base defaults repaired as in §1):

| Command | Result |
|---|---|
| `npm run compile` | engine type error from the base (`mutate-worker.ts` `sampledShare`); dist emitted, unrelated |
| `node engine/dist/main.js build`, `render`, `render --ny` | build OK; renders OK (final tree) |
| own fixtures (`fixtures/2025/rental.json`, 27 cases, 138 expected values) via `fixture-inputs` + `eval --batch` on the final tree | 138/138 match. Earlier full `test-fixtures` run (before lines A/B were dropped): all 27 `x1sche.*` cases ok; the 15 value cases matched their hand predictions on the first run; the 12 refusal cases matched on gate, and their form/remedy/cite were then copied from the forms |
| full `test-fixtures` (earlier tree) | 1420/2038; the 618 failures are the base's (598 `s2.amt_owed`, 18 `sd.qof`, 1 tipjob, 1 `stage4.sb.foreign_no_filing`); the 3 restated cases pass |
| `test-fixtures --ny` (earlier tree) | 142/357; all 215 failures name `s2.amt_owed` or `sd.qof` (base) |
| `interview-coverage --rows rental.yaml --rows scope.yaml` (final tree) | 0 problems; 77 rows of 2 files walked |
| `tick-groups` | 0 problems (full, ny) after moving the topic to order 130 |
| `citations.py --strict` (final tree) | exit 0: 0 findings, 0 locators to rewrite, 0 new input-quote findings |
| `check_consumers.py` | my 20 new pairs ruled `same` in `reviews/2025/consumers.json`, 8 stale `scope.rental` rulings removed; remaining findings are the base's |
| `year_changes.py --check` (final tree) | exit 0, all 132 entries apply |
| `extract_realty_tables.py --check` | ok, 960 rates, every column totals 100% |
| `coverage/tree.py --check` | only the base's six unplaced gates remain (after removing a `part` field from my placements) |
| `draft-walk` 19_rental_house, 11_refused_rental, 01_single_w2 | 0 problems each |
| `siblings.py --check`, `check_bug_inventory.py` | fail on base pending entries only (g1-*, ty26-*); this lane filed none |
| `check_questions.py`, `check_screens.py`, `check_false_no.py` | not present in this tree |
| `interview-rules` | not completed on the final tree (stopped at the coordinator's deadline); an earlier run on an earlier bank showed only base problems (`s2.amt_owed` walks, NY, `person.tin`) |
| `mutate`, `check_all.sh` | not run (coordinator) |

## 9. Review debt (round 2; none run here)

- New forms, whole: `rental`, `rprop`, `rf4562`, `royalty`, `sche`, `f8582` — transcription, render, class M (18).
- Changed arithmetic, line-scoped: `s1` (line5, line10, line10_ex5, EBL lines), `f8960` (line4a, line4c), `eic`
  (`eic.step2_other`) — transcription + class M; `scope` (`scope.schedule1`, `scope.rent_personal*`) — transcription.
- Changed wording: `scope.passive`, `f8960.unsupported` — render.
- Screens/gates (screen review, kind gate): the 19 refusal gates of §2; false-no: `rental.personal_any`,
  `rental.short_stays`, `rental.prior_any`, `scope.rent_personal`, `rental.active`; completeness: `f8582`, `sche`.
- Question review: the 66 new bank entries. Table second transcription: `macrs_mm` (the extractor's 100% column
  check is the only one run).
- Dry-run cost estimate not run (no paid tooling run in the lane).

## 10. Walks (after; no before-walk was recorded)

| Persona | Questions | Screens | Prompt words | Help words | End |
|---|---|---|---|---|---|
| 01_single_w2 (filer with nothing) | 126 | 57 | 1,767 | 3,411 | completed |
| 19_rental_house (typical) | 167 | 82 | 2,530 | 3,755 | completed |
| 11_refused_rental (refused) | 25 | 19 | 406 | 682 | refused at `rental[beach].stay7_if_short` |

The filer with nothing gains no step (scope.rental is a tick box they leave; only its help changed) [inferred: no
before-walk was run to compare]. The typical rental filer answers 41 more questions on 25 more screens than persona 01
(one property, one building); the scout estimated 23–26 steps.

## 11. Left open, in rank order

1. Mutation (integration). 2. Engine differential (UsTaxes computes Schedule E with entered depreciation and a
simplified Form 8582; usable for F1/F2-like cases only): not mapped. 3. Personal property in rentals (D3), the
largest residual refusal. 4. i8582 p. 3 exceptions 3–6 (incidental rentals and the like) are not screened. 5. A prior
unallowed loss of a property left out (rented under 15 days as a home) is not carried. 6. Line 6 of Schedule E for
travel without a vehicle is refused with vehicles. 7. Schedule E lines A and B (Forms 1099 paid) are not asked or
shown; the 2026 threshold change ($600 → $2,000, i1040se 2026 p. 2) applies when they are.
