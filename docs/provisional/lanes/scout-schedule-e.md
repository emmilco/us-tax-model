# Design scout: Schedule E Part I (rental real estate and royalties), Form 8582, rental depreciation — TY2025

Read-only scout, 2026-11-15. Model claude-opus-5-5, class judgment, year 2025, jurisdiction us.
Tree read: `.claude/worktrees/sweep-tasks` (HEAD 63a20efc). Nothing in the repository was changed.
Locators follow PROJECT_INDEX: `doc p. N` = N-th form-feed chunk of `<doc>.cols.txt`.

**Prior work this supersedes in part.** `research/premises/stage17-schedule-e.md` (draft 2026-10-22) and its
verification `stage17-schedule-e.verification.md` (12 errors) cover all of Schedule E. This design narrows to Part I +
Form 8582 + rental depreciation, re-checks the premises against the current tree (after the interview redraft), and
corrects two of the map's points: (1) Table A-6 is **not** scrambled in the layout text: `sources/2025/p946.txt`
page 73 reads the table cleanly row by row (only `p946.cols.txt` is out of order), so the extractor can read it;
(2) the Form 4562 rows are **19i** (27.5-year) and **19j** (39-year) in 2025 (19h is the new 50-year row, f4562 p. 1;
i4562 p. 1, "New lines 19h and 20e").

Marks: **[V]** checked in this session against the named file; **[I]** inferred; **[E]** estimate.

---

## 1. Scope

### 1.1 Computed after this work

| # | Situation | Notes |
|---|---|---|
| C1 | Long-term rental of real estate (Schedule E types 1 single family, 2 multi-family, 4 commercial, 5 land), one or more properties, owned alone, jointly with a spouse, or as a part interest (filer enters own share) | i1040se p. 4, "report only your part of the income and expenses" [V] |
| C2 | Royalties (type 6) from copyrights, patents, NIL rights, oil/gas/mineral (non-operating), **without depletion** | i1040se p. 6, Line 4 [V] |
| C3 | Lines 3–21 per property; lines 23a–26 for the return; Schedule 1 line 5 | f1040se p. 1 [V] |
| C4 | Personal use of a dwelling unit **not** used as a home: expenses divided by days (rental days ÷ total use days) | i1040se p. 5 Line 2, "10% (7 ÷ 70)"; p527 p. 26 "85/99 (86%)" [V] |
| C5 | Used as a home and rented under 15 days: nothing reported (exclusion) | i1040se p. 5, "do not report the rental income and do not deduct any rental expenses" [V] |
| C6 | Passive loss limit: Form 8582 Parts I–IV, V (rentals without active participation), VI, VII, VIII; the $25,000 special allowance with the $100,000–$150,000 phase-out; prior-year unallowed losses per property; the 2026 carryforward shown | f8582 pp. 1–2; i8582 pp. 9–14 [V] |
| C7 | The Form 8582 filing exception: computed by the same arithmetic, form shown only when required | i8582 p. 1, Exception; equality of results is [I] from the arithmetic (line 9 = line 4 under the exception's conditions) |
| C8 | Depreciation of the building and of improvements to it: 27.5-year residential (Table A-6) placed in service 1987–2025, 39-year nonresidential (Table A-7a) placed in service 1994–2025, mid-month, straight line | p946 pp. 73–74 [V]; i4562 p. 11 Column (e), p. 12 Column (f) [V] |
| C9 | Form 4562 per property when property was placed in service in 2025 (lines 17, 19i, 19j, 22) | i1040se p. 7, Line 18, "You must complete and attach Form 4562 only if…" [V] |
| C10 | Property converted from personal use in 2025: filer enters rental-period amounts; depreciation from the conversion month; basis the lesser of FMV and adjusted basis (filer input) | p527 pp. 24–25 example [V] |
| C11 | Form 8960 line 4a = Schedule 1 line 5 (passive rental and royalty net income or loss is NII) — **owner decision D7** | i8960 p. 8, Line 4a [V] |

### 1.2 Still refused (gate, reason)

| # | Situation | Gate (proposed id) | Cite |
|---|---|---|---|
| R1 | Rental of personal property (equipment, vehicles) | new `scope.rent_personal` (child of `scope.rental`), feeds `scope.schedule1` | i1040se p. 5, Personal property [V] |
| R2 | Average stay 7 days or less, or 30 days or less with significant personal services (not a "rental activity"); significant services (Schedule C) | `rental.not_rental_activity`, `rental.services` | i8582 p. 3, Exceptions item 1; i1040se p. 5, Line 3 [V] |
| R3 | Dwelling used as a home and rented 15+ days **with a net loss** (Worksheet 5-1) | `rental.ws51` | p527 p. 28, "Used as a home and rented 15 days or more" [V] |
| R4 | Self-rental (type 7) and other recharacterized income | `rental.self_rental` | i1040se p. 5, Self-rental; i8582 p. 8 Recharacterization [V] |
| R5 | Real estate professional (line 43) | `sche.re_pro` | i1040se p. 3–4 [V] |
| R6 | Loss with amounts not at risk (Form 6198) | `rental.not_at_risk` (asked only when line 21 < 0 and placed after 1986) | i1040se p. 3; i1040se p. 7 Line 21 [V] |
| R7 | Not rented for profit | `rental.not_for_profit` | p527 p. 24 [V per map; not re-read] |
| R8 | Depletion | `royalty.depletion`, `rental.depletion` | i1040se p. 7, Line 18 [V] |
| R9 | Rental treated as a trade or business for QBI (250-hour safe harbor or section 162), and any rental trade or business (Form 8990) | `sche.qbi_business` | i8995 pp. 1–2; i1040se p. 7 Limitation on business interest [V] |
| R10 | ADS (elected or required), 31.5-year nonresidential (before 1994), qualified improvement property, cooperative stock, basis adjustments, dispositions | `rprop.screen` | i4562 p. 12; p946 p. 74 Table A-7 [V] |
| R11 | Depreciable personal property and land improvements in a rental (appliances, carpet, furniture, fences) — **v1 only, owner decision D3** | `rprop.kind = personal` | p527 p. 13 [V per map] |
| R12 | Vehicles in a rental (line 6 auto) — **owner decision D5** | `rental.vehicle` | i1040se p. 6, Line 6 [V] |
| R13 | Prior-year unallowed losses of a passive activity **not** listed this year; prior unallowed CRD; grouping of rentals as one activity | narrowed `scope.passive`; `sche.grouped` | i8582 pp. 5–6, 10 [V] |
| R14 | Sale or disposition of a rental (Form 4797; frees suspended losses) | existing `sd.sold_other` / Form 4797 refusal | i8582 p. 9 Dispositions [V] |
| R15 | Prior-year loss in Part IV column (c) from a year without active participation (goes to Part V) — **or computed, D2** | `rental.prior_not_active` | i8582 p. 10, Part IV [V] |
| R16 | EIC with any Schedule E (Pub. 596 Worksheet 1 not archived) — **owner decision D6** | `eic.step2_other` refuses on new `sche.any` | i1040gi p. 40, Step 2 q. 4, "You are filing Schedule E." [V] |
| R17 | Excess business loss over the threshold, counting Schedule E losses (Form 461) | extended `s1.ebl` | i1040se p. 1, Reminders [V] |
| R18 | Married filing separately | unchanged (`s3.mfs` at `scope.ready`) | — |
| R19 | K-1 rentals (Parts II, III), farm rental (Form 4835) | unchanged `scope.k1`, `scope.farm` | — |

### 1.3 Gates that go away or narrow [V: read in `forms/2025/scope.yaml`, `f8960.yaml`, `eic.yaml`]

- `scope.rental` stays an input (it is the off-ramp), but **leaves the `any` list of `scope.schedule1`**
  (scope.yaml line 986). Its equipment branch moves to the new child `scope.rent_personal`, which joins that list
  (technique 3.1: `scope.schedule1` keeps its id, its refusals keep their wording).
- Every refusal on `scope.schedule1` was read: `f1040.line8`, `f1040.line10`, `scope.ready_schedule1`, `ssb.line6`,
  `s8812.eiw_3`, `s8812.eiw_4`, `s1a.line5_calc`, `s1a.line14b_calc`, `eic.step5_line1`, `eic.clergy`,
  `eic.step2_other`. Only `eic.step2_other` concerns Schedule E (its remedy names it); it needs the new gate `sche.any`.
  The others concern earned income, SE, tips/overtime, which Part I rentals do not touch [I, from their remedies].
- `scope.passive` (gated by `scope.business_before`, scope.yaml line 905; bank help "Count a loss … held back in an
  earlier year") narrows to activities other than the rentals listed, and their held-back losses.
- `f8960.unsupported` drops "rental, royalty" from its first item (keeps annuity, business, pass-through) — D7.
- `tools/coverage/categories.json` `rental_royalty`: `gates` → the new rental gates, `refused: false` with a label
  "supported; remaining refusals unmeasured" (the estimator keys on the flag, verification E4) [V].

### 1.4 Share served [E]

`reports/2025/filer_coverage.md` (stale, generated 2026-11-01; T-294): rental and royalty income or loss is
**5.9%** of returns (9,542,639 of 160.6 M, soi-23in14ar cols 63 + 65) [V]. The report gives the gain only for the whole
Schedule E group (+5.7 points, with partnerships and estates). The rental category alone was not measured (the
estimator writes into `reports/`, so it was not run). **Estimate: +3 to +4.5 points of measured coverage**, less the
unmeasured residual refusals above (short-term rentals and personal property in rentals are the largest; no IRS count
exists for them). SOI detail [V, via map, verified]: rent net income 4.89 M, rent net loss 4.34 M, royalty net income
1.80 M, royalty loss 0.08 M returns.

---

## 2. Sources

### 2.1 Needed for 2025, archived [V: `sources/2025/manifest.json`]

| Doc | Revision | Pages used |
|---|---|---|
| f1040se | 2025 (created 5/6/25) | p. 1 (Part I lines A–26), p. 2 (line 41, 43) |
| i1040se | 2025 (Nov 12, 2025) | pp. 3–4 (passive rules, exception, active participation), pp. 4–8 (Part I line instructions) |
| f8582 | 2025 (created 5/8/25) | pp. 1–2 (Parts I–VIII) |
| i8582 | 2025 (Nov 26, 2025) | p. 1 (Who must file, Exception), pp. 2–5 (definitions, rental activity, special allowance), p. 9–14 (specific instructions), p. 11 (line 6 MAGI) |
| p925 | 2025 | pp. 5–7 (special allowance, phase-out example $120,000/$31,000) |
| p527 | 2025 | pp. 17, 21 (examples), pp. 24–25 (conversion example), pp. 25–30 (personal use, Worksheet 5-1) |
| p946 | 2025 | p. 39 (recovery year), p. 73 Table A-6, p. 74 Table A-7a (layout text `p946.txt`) |
| f4562 / i4562 | 2025 | f4562 p. 1 lines 17, 19i, 19j, 22; i4562 pp. 10–12 |
| f8960 / i8960 | 2025 | i8960 p. 8 lines 4a/4b |
| i1040gi | 2025 | p. 40 EIC Step 2 q. 4 |
| f4797 / i4797 | 2025 | archived since the map (it said absent); cited only by refusals |

### 2.2 Not archived (do not fetch; listed to archive)

| Doc | Needed for | Status |
|---|---|---|
| Pub. 596 (2025), Worksheet 1 | D6 only (computing EIC with Schedule E) | absent |
| Rev. Proc. 2019-38 | D8 only (rental QBI safe harbor) | absent |
| Form 461 + instructions (2025) | D15 (EBL reading) | absent |
| Form 8990 + instructions | R9 citation could use it; i1040se p. 7 suffices | absent |
| Pub. 534 | pre-1987 ACRS (not needed: such buildings are fully depreciated by 2025 [I]) | absent |

### 2.3 2026 editions [V: `sources/2026/manifest.json`]

| Doc | 2026 status |
|---|---|
| f1040se | DRAFT 2026-05-19, archived |
| i1040se | DRAFT 2026-09-24, archived |
| f8582 | DRAFT 2026-09-18, archived |
| i8582 | DRAFT 2026-11-05, archived |
| p925 | DRAFT 2026-11-06, archived |
| f4562 | DRAFT 2026-06-01, archived; **i4562 2026 not archived** |
| p527 2026, p946 2026 | **not archived** (Table A-6/A-7a are statutory schedules, unchanged in substance [I]) |
| Notice 2026-11 (bonus, named in i1040se 2026 What's New) | not archived |

---

## 3. Encoding plan

### 3.1 New collections and forms

| Form id | Kind | Parent | One entry per |
|---|---|---|---|
| `rental` | collection | none (return) | Part I real-estate property (types 1–5, 7, 8 asked; 3 = vacation/short-term) |
| `royalty` | collection | none (return) | royalty source (Part I type 6) |
| `rprop` | collection | `rental` | building, or improvement to it (separate property, p946 p. 33) |
| `rf4562` | collection, implicit | `rental` | one Form 4562 per property (as `f4562` is to `sc`, i4562 p. 2 "File a separate Form 4562 for each business or activity") |
| `sche` | form | — | Schedule E return lines A, B, 23a–26, 43 screen |
| `f8582` | form | — | Form 8582 Parts I–III and the return-level sums for Parts IV–VII |

`sc`, `asset`, `f4562` are under `person`/`sc` and cannot be reused under `rental` (spec 4.4: an entry reads only its
enclosing entries; `asset.collection.parent: sc`) [V]. Separate `royalty` keeps royalty rows free of the day, activity
and passive questions (i1040se p. 4, "For royalty property, enter code “6” on line 1b and leave lines 1a and 2 blank") [V].

**Line id contract between lanes** (agree before lanes start): `rental.line21`, `rental.passive`, `rental.part4`,
`rental.net_income`, `rental.net_loss`, `rental.prior_loss`, `rental.overall_loss`, `rental.line22`,
`rental.excluded`, `rental.share`, `rental.line18`; `rprop.dep`, `rprop.placed_2025`; `royalty.line21`;
`f8582.line3`, `f8582.line9`, `f8582.p6_total`, `f8582.p7_C`, `f8582.p7_total`; `sche.line26`, `sche.any`.

### 3.2 `rental` lines (per property)

| id | printed | type | expression sketch | cite |
|---|---|---|---|---|
| `rental.kind` | 1b | Enum(rental_kind: sfr, multi, vacation, commercial, land, self_rental, other) | input | f1040se p. 1 Type of Property |
| `rental.days_fair` | 2 (fair rental) | Count | input | i1040se p. 5 Line 2 |
| `rental.personal_any` | (helper) | Bool | input (parent) | i1040se p. 5, "A day of personal use is…" |
| `rental.days_personal` | 2 (personal use) | Count | gated input; 0 when `personal_any` false | same |
| `rental.days_overlap` | (helper) | Count | gated child: personal days that were also fair-rental days (p527 p. 26) | p527 p. 26 |
| `rental.home` | (gate) | Bool | `test gt( multiply_count(10¢, home_days_personal), larger_of(multiply_count(10¢·14…)…))`: personal > max(14, 10% × rental) exactly, via `multiply_count` (10 cents × personal vs 1 cent × fair-rental-for-test; and personal > 14) — use `any`/`all` of two `gt` tests | i1040se p. 5; verification E9 (exact test agrees with Pub. 527's rounding down) |
| `rental.excluded` | (gate) | Bool | `home` and `days_fair < 15` (param `home.min_rental_days` 15) | i1040se p. 5 |
| `rental.share` | (helper) | — | not a line: each expense line is `prorate(amount, part = days_fair_div, whole = days_total, places 6)`; `days_fair_div`, `days_total` Count lines; when `days_personal = 0` a `choose` copies the amount (avoids the ratio) | p527 p. 26; amb `rental_use_ratio_places` |
| `rental.line3` | 3 | NonNegDollars | input × (0 when excluded) via `choose` | i1040se p. 5 Line 3 |
| `rental.line5`…`rental.line17`, `rental.line19` | 5–17, 19 | NonNegDollars | per line: `*_entered` input (gated by expense tick boxes) → `prorate` by days → `choose` zero when excluded | i1040se pp. 6–7 |
| `rental.line12` | 12 | NonNegDollars | mortgage interest to banks (Form 1098 box 1, own share) | i1040se p. 7 Lines 12 and 13 |
| `rental.line13` | 13 | NonNegDollars | other interest (no Form 1098, or co-borrower's 1098) | same |
| `rental.line18` | 18 | NonNegDollars | `copy rf4562.line22` when any 2025 property, else `sum_over rprop field rprop.dep` (both × day share) | i1040se p. 7 Line 18 |
| `rental.line20` | 20 | NonNegDollars | `sum` lines 5–19 | f1040se line 20 |
| `rental.line21` | 21 | Dollars | `subtract(line3, line20)` | f1040se line 21 |
| `rental.passive` | (gate) | Bool | not excluded, not home-used (home-used with profit is nonpassive, i8582 p. 3 item 4) | i8582 p. 3 |
| `rental.active` | (helper) | Bool | input "helped make management decisions" | i1040se p. 4 Active participation |
| `rental.part4` | (gate) | Bool | `passive` and `active` and not `prior_not_active` | i8582 p. 10 Part IV |
| `rental.net_income`, `rental.net_loss` | Part IV/V (a),(b) | NonNegDollars | `subtract_floor0(line21, 0)`, `subtract_floor0(0, line21)` | i8582 p. 10 |
| `rental.prior_loss` | Part IV/V (c) | NonNegDollars | gated input (parent `rental.prior_any`), from 2024 Form 8582 | i8582 p. 10, "You find these amounts in Part VII, column (c), of your 2024 Form 8582" |
| `rental.overall_loss` | (e) | NonNegDollars | `subtract_floor0(sum(net_loss, prior_loss), net_income)` | i8582 p. 10 Columns (d) and (e) |
| `rental.p6c` | Part VI (c) | NonNegDollars | `choose`: part4 ∧ overall_loss > 0 ∧ f8582.p6_total > 0 → `prorate(f8582.line9, overall_loss, f8582.p6_total, 6)`; else 0 | i8582 p. 12 |
| `rental.p7a` | Part VII (a) | NonNegDollars | `subtract_floor0(overall_loss, p6c)` (Part V: overall_loss) | i8582 p. 12 |
| `rental.p7c` | Part VII (c) = Part VIII (b) | NonNegDollars | `choose`: f8582.line3 < 0 ∧ f8582.p7_total > 0 → `prorate(f8582.p7_C, p7a, f8582.p7_total, 6)`; else 0 | i8582 p. 13 |
| `rental.p8a` | Part VIII (a) | NonNegDollars | `sum(net_loss, prior_loss)` | i8582 p. 13 |
| `rental.allowed` | Part VIII (c) | NonNegDollars | `subtract_floor0(p8a, p7c)` | i8582 p. 13 |
| `rental.line22` | 22 | Dollars (≤ 0) | `subtract(0, allowed)` for passive; `copy line21` when loss and not passive (home-used cannot reach: refused R3); shown_when loss or prior | i1040se p. 8 Line 22; i8582 p. 14 How To Report |
| `rental.carryforward` | (display) | NonNegDollars | `copy p7c` | i8582 p. 13, "Keep a record of these amounts" |
| screens | (gates) | Bool | `not_rental_activity`, `services`, `self_rental` (kind), `not_for_profit`, `ws51` (home ∧ ¬excluded ∧ line21 < 0), `not_at_risk`, `depletion`, `vehicle`, `prior_not_active` (D2) | §1.2 |

### 3.3 `royalty` lines

`royalty.line4` (input, Form 1099-MISC box 2), `royalty.expenses_any` (parent) → `royalty.line10`, `royalty.line16`,
`royalty.line19` (inputs), `royalty.line20` (sum), `royalty.line21` (subtract), `royalty.depletion` (refusing).
Not passive, never on Form 8582 (i1040se p. 4, "Royalty income not derived in the ordinary course of a trade or
business … is not considered income from a passive activity"; i1040se p. 8, "Do not complete line 22 if the amount on
line 21 is from royalty properties") [V].

### 3.4 `rprop` lines (per building or improvement)

| id | printed (Form 4562) | type | sketch |
|---|---|---|---|
| `rprop.kind` | (a) | Enum(rprop_kind: residential, nonresidential, personal) | input; `personal` refuses in v1 (D3) |
| `rprop.month` | (b) | Enum(month: m1…m12) | input |
| `rprop.year` | (b) | Enum(realty_year: y1987…y2025, before1987) | input (`extends_with_year`) |
| `rprop.basis` | (c) | NonNegDollars | input: cost of the building (not land), or the improvement; converted property: lesser of FMV and adjusted basis (p527 p. 22) |
| `rprop.recovery_year` | (helper) | Count | `keyed_lookup realty_recovery_year[year]` (before1987 → a year past the table) |
| `rprop.rate` | (helper) | Rate | `keyed_lookup macrs_mm[period, month, recovery_year]` (period = y27_5 / y39 from kind); rows with 0 for years past the end |
| `rprop.dep` | (g) | NonNegDollars | `multiply_rate(basis, rate)` |
| `rprop.placed_2025` | (gate) | Bool | `year = y2025` (Form 4562 needed) |
| `rprop.screen` | (gate) | Bool | ADS, QIP, nonresidential before 1994, basis changed, disposed, cooperative stock → refuse |

`rf4562` (implicit under `rental`): `rf4562.line17` = `sum_over rprop where ¬placed_2025 field dep`;
`rf4562.line19i` = `sum_over rprop where placed_2025 ∧ residential`; `rf4562.line19j` same nonresidential;
`rf4562.line22` = sum; `shown_when` any 2025 property (f4562 p. 1 line 17, "MACRS deductions for assets placed in
service in tax years beginning before 2025") [V].

### 3.5 `sche` lines (return)

| id | printed | sketch |
|---|---|---|
| `sche.lineA`, `sche.lineB` | A, B | inputs (display), asked once when `sche.any` |
| `sche.line23a` | 23a | `sum_over rental field line3` |
| `sche.line23b` | 23b | `sum_over royalty field line4` |
| `sche.line23c` | 23c | `sum_over rental line12` + `sum_over royalty` (royalty has no line 12: 0) |
| `sche.line23d` | 23d | `sum_over rental line18` |
| `sche.line23e` | 23e | `sum` of `sum_over rental line20`, `sum_over royalty line20` |
| `sche.line24` | 24 | `sum` of `sum_over rental net_income`, `sum_over royalty` positive part |
| `sche.line25` | 25 | `sum` of `sum_over rental line22`, `sum_over royalty` negative part (held negative, T-004 precedent) |
| `sche.line26` | 26 | `sum(line24, line25)` |
| `sche.line41` | 41 | `copy line26` (Parts II–IV refused) |
| `sche.any` | (gate) | any rental not excluded, or any royalty |
| `sche.re_pro` | (gate, 43) | input, refusing |
| `sche.qbi_business`, `sche.grouped` | (gates) | inputs, refusing |
| `sche.nonpassive_net` | (helper) | `sum_over royalty field line21` (+ home-used profit rentals if D2 computes them) — read by the MAGI build |

### 3.6 `f8582` lines (return)

| id | printed | sketch | cite |
|---|---|---|---|
| `f8582.line1a` | 1a | `sum_over rental where part4 field net_income` | f8582 p. 1 |
| `f8582.line1b` | 1b | negative of `sum_over rental where part4 field net_loss` | same |
| `f8582.line1c` | 1c | negative of `sum_over rental where part4 field prior_loss` | same |
| `f8582.line1d` | 1d | `sum` | same |
| `f8582.line2a`–`2d` | 2a–2d | same over `where passive ∧ ¬part4` (Part V) | same |
| `f8582.line3` | 3 | `sum(line1d, line2d)` (CRD refused) | same |
| `f8582.line4` | 4 | `choose`: line3 < 0 ∧ line1d < 0 → `smaller_of(−1d, −3)`; else 0 | i8582 p. 11 Line 4 |
| `f8582.line5` | 5 | `param pal.phaseout_end` (150,000; MFS 75,000) | f8582 line 5 |
| `f8582.magi_income` | (helper) | `sum(f1040.line1z, 2b, 3b, 4b, 5b, 7a, s1.line10_ex5, sche.nonpassive_net)` — **no line 6b, no s1.line5** | i8582 p. 11 Line 6 |
| `f8582.magi_adj` | (helper) | `sum(s1.line11, 13, 16, 17, 18, 19a, 25)` — s1.line26 less lines 15 (SE tax), 20 (IRA), 21 (student loan) | same |
| `f8582.line6` | 6 | `subtract_floor0(magi_income, magi_adj)` | same; amb `pal_magi_build` |
| `f8582.line7` | 7 | `subtract_floor0(line5, line6)` | f8582 note under line 6 |
| `f8582.line8` | 8 | `smaller_of(multiply_rate(line7, pal.rate ½), param pal.special_max)` | f8582 line 8 |
| `f8582.line9` | 9 | `smaller_of(line4, line8)` (0 when line 4 is 0) | f8582 line 9 |
| `f8582.line10` | 10 | `sum(line1a, line2a)` | f8582 line 10 |
| `f8582.line11` | 11 | `sum(line9, line10)` | f8582 line 11 |
| `f8582.p6_total` | VI total (a) | `sum_over rental where part4 field overall_loss` | i8582 p. 12 |
| `f8582.p7_total` | VII total (a) | `sum_over rental field p7a` | i8582 p. 12 |
| `f8582.p7_C` | VII worksheet C | `subtract_floor0(−line3, line9)` | i8582 p. 13, "A… B… C. Subtract line B from line A" |
| `f8582.required` | (display gate) | any passive rental with loss or prior loss, unless the exception holds (only Part IV, no prior, loss ≤ $25,000, MAGI ≤ $100,000) | i8582 p. 1; amb `f8582_shown` |

New dependency check [I]: `f8582.line6` reads no line that reads `s1.line5` (taxable SS, IRA and student-loan
deductions are excluded, and they are the only AGI-dependent adjustments), so the graph has no cycle; the checker
rejects cycles (verification, Confirmed).

### 3.7 Parameters, enums, tables

- `params/2025.yaml`: `pal.special_max` (2,500,000; MFS 1,250,000), `pal.phaseout_end` (15,000,000; MFS 7,500,000),
  `pal.rate` (½), `pal.exception_magi` (10,000,000; MFS 5,000,000), `pal.exception_loss` (2,500,000; MFS 1,250,000),
  `home.days` (14), `home.tenth` (10¢ / 1¢ pair for the exact test), `home.min_rental_days` (15). Locators: map §7 [V].
- Enums: `rental_kind`, `rprop_kind`, `month`, `realty_year` (y1987–y2025, before1987; extends_with_year),
  `macrs_mm_period` (y27_5, y39).
- Tables: `tables/2025/macrs_mm.yaml` — Table A-6 (12 months × 29 years) and Table A-7a (12 × 40), extracted from the
  **layout** text `sources/2025/p946.txt` page 73–74 (verified readable this session), with a second transcription and a
  table check: every month row sums to 100.000% (A-6) / 100.000% (A-7a) to the printed precision.
  `tables/2025/realty_recovery_year.yaml` (2025 − year + 1).
  Values read this session [V]: A-6 year 1 Jan 3.485 … Dec 0.152; years 2–9 3.636; months 1–6 even years 10–26 3.637,
  odd 11–27 3.636; months 7–12 the opposite; year 28 months 1–6 1.97/2.273/2.576/2.879/3.182/3.485, months 7–12 3.636;
  year 29 months 7–12 0.152…1.667. A-7a year 1 Jan 2.461 … Dec 0.107; years 2–39 2.564; year 40 0.107 … 2.461.

### 3.8 Existing lines that change

| Line | Change |
|---|---|
| `s1.line5` (new) | printed 5, `copy sche.line41` |
| `s1.line10` | today `sum(line1, 2a, 3, 7, 9)` [V]; becomes `sum(s1.line10_ex5, s1.line5)` with new helper `s1.line10_ex5` (the MAGI build needs the sum without line 5) |
| `scope.schedule1` | `any` list: remove `scope.rental`, add `scope.rent_personal_if_rental` |
| `scope.rent_personal`, `scope.rent_personal_if_rental` | new child of `scope.rental` |
| `scope.passive` | label/source narrowed to activities and held-back losses other than the rentals listed |
| `eic.step2_other` | `all(...)` gains `sche.any = false`; new refusal `when: sche.any` (same form/remedy as today) |
| `f8960.unsupported` | drop "rental, royalty" (D7) |
| `f8960.line4a` | `copy s1.line5`, retyped Dollars; `f8960.line4c` retyped Dollars (line 4b stays 0: nonpassive rentals refused) [V: today NonNegDollars copy of zero] |
| `s1.ebl_total` | add `sche.line26` when negative (D15) |
| `sa.yaml` 1098 and line 5b | help only: a rental's Form 1098 and taxes go with the rental (N8; D2 for mixed use) |
| `tools/coverage/categories.json` | §1.3 |

### 3.9 Ambiguity entries needed (`ambiguities/2025.yaml`)

1. `amb.2025.rental_activity_per_property` — each property one activity; grouping refused (i8582 p. 6).
2. `amb.2025.pal_magi_build` — MAGI built without any Part IV/V amount (i8582 p. 11 vs p925 p. 6 wording; same result whenever line 9 is reached [I]).
3. `amb.2025.pal_ratio_places` — Parts VI/VII ratios to six places; cents residue against line 9/11 accepted (i8582 p. 12 "must be the same").
4. `amb.2025.rental_use_ratio_places` — personal-use division to six places (p527 p. 26 shows "86%").
5. `amb.2025.rental_overlap_days` — line 2 printed in the home-test view (map Q1 reading A).
6. `amb.2025.rental_direct_expenses` — whether rental-only expenses (advertising, commissions, management) are divided by days in the not-a-home case (p527 Worksheet 5-1 line 2d treats them as undivided; ch. 5 text says "divide your expenses"). D2.
7. `amb.2025.rental_not_qbi` — a rental is not a qualified trade or business unless the filer says it meets the safe harbor or section 162 (refused then).
8. `amb.2025.rental_prior_depreciation_tables` — prior-year property figured from the tables, not the filer's schedule (p527 p. 15 "substantially the same").
9. `amb.2025.f8582_shown` — form shown only when required (i8582 p. 1).
10. `amb.2025.rental_ebl` — Schedule E losses counted toward the EBL screen conservatively (Form 461 not archived).

---

## 4. Interview plan (per the construction protocol)

**Typical filer [I]:** one W-2, one long-term single-family rental owned for years, a tenant all year, a bank mortgage
with a Form 1098, property tax, insurance, a few repairs, the building's depreciation from the prior return's schedule,
MAGI under $150,000, a small loss or profit, standard deduction. **Filer with nothing:** answers the existing
`scope.rental` box (no new step). **Refused filer:** a whole-house short-term rental (average stay 3 days).

**Placement.** `scope.rental` stays at order 130 in tick group `own_income` (the off-ramp; already a box, so the
filer with nothing pays nothing new). The refusing child `scope.rent_personal` follows at 130 (asked only on Yes, told
at its topic, N11). The property topic takes free orders **268** (`$rental` and its entries) and **269**
(`$royalty`), after the business block (250–267) and before interest (270) [V: orders read from the bank]. Owner may
prefer the topic directly after 130 (D11).

**Questions** (one subject each; plain words; who could answer No wrongly in brackets):

| order.seq | input | prompt sketch | notes |
|---|---|---|---|
| 130.4 | `scope.rent_personal` | "Was any of it something other than a building, a room or land, such as a car, a trailer or equipment?" | refuses; [a landlord renting a furnished house — help: "Furniture rented with a home counts as part of the home."] |
| 268.1 | `$rental` | "List each building, home, room or piece of land you rented out in 2025; one entry each." | roster; label = a short address |
| 268.2 | `rental.kind` | choice: "A house or condo (one home)", "A building with two or more homes", "A vacation or short-stay rental", "Shops or offices", "Land only", "Rented to a business you or your spouse run", "Something else" | self-rental and other refuse |
| 268.3 | `rental.days_fair` | "How many days in 2025 was it rented at a fair price?" | Count 0–366 |
| 268.4 | `rental.personal_any` | "On any day in 2025, did you, your family or a co-owner use it, or did anyone stay free or below a fair rent?" | [renting to a son at a fair rent as his home — help says that is not personal use, p527 p. 27 Ex. 3] |
| 268.5–6 | `rental.days_personal`, `rental.days_overlap` | days; overlap child only when > 0 | home test, exclusion and division derived (N8) |
| 268.7 | `rental.short_stays` | "Did renters stay 30 days or less on average?" → child "7 days or less?" → child "Did you provide services such as cleaning during stays or meals?" | refuses R2 [STR owner who thinks of the 30-day lease — help gives the average formula] |
| 268.8 | tick group `rental_rare` (per entry): owned with others under a tenth; not rented to make a profit; anyone not personally liable on a loan used for it (seller or private nonrecourse); a deduction for depletion | each refuses; the commonest refusal (short stays) is not in it (asked alone first, 3.6) |
| 268.9 | `rental.active` | "Did you or your spouse help make decisions for it, such as approving tenants, setting the rent or approving repairs, even if a manager did the daily work?" | typical Yes; No → Part V |
| 268.10 | `rental.line3` | "Rent received for 2025 (your share), including fees and expenses the tenant paid for you" | 1099-MISC box 1 in help |
| 268.11–12 | tick groups `rental_costs_a` (mortgage interest on a Form 1098; other interest; property tax; insurance; management fees; commissions) and `rental_costs_b` (repairs; cleaning and maintenance; utilities; supplies; advertising; legal and tax-preparation fees) + `rental.other_any` | each tick opens its amount; printed order kept for the amounts (N7) |
| 268.13 | `rental.prior_any` → `rental.prior_loss` | "Was a loss from this rental held back (not deducted) on your 2024 return?" → amount "from 2024 Form 8582, Part VII, column (c)" | [a filer whose 2024 software held it back silently — help: "Look for Form 8582 in your 2024 return."] |
| 268.14 | `$rprop` | "List the building and each improvement you depreciate for it (a new roof, a furnace)." | per entry: kind, month, year, basis (help: land is not depreciated; prior depreciation schedule shows the basis) |
| 268.15 | `rental.not_at_risk` | asked only when line 21 is a loss and property placed after 1986 | sc.at_risk wording precedent |
| 268.20 | `sche.lineA` → `sche.lineB` | "Did you pay any one person or company (not an employee) $600 or more for work on your rentals?" | display |
| 268.21 | tick group `rental_return` (once): more than 750 hours in real estate businesses and over half your work time; rentals treated as one activity; rentals run as a business for the QBI deduction (250 hours, separate books) | each refuses |
| 269.1 | `$royalty` → `royalty.line4`, `royalty.expenses_any`, `royalty.depletion` | "List each source of royalties (a book, a patent, an oil or gas lease)." | |

**Cost and share notes [E, agent judgment, owner may overrule]:** `scope.rental` Yes ≈ 6% (SOI share);
`rental.personal_any` Yes ≈ 10–15% of properties; `rental.short_stays` Yes ≈ 10–20%; `rental.prior_any` Yes ≈ 15–25%
of losing properties. Typical single-property walk ≈ 23–26 steps and ≈ 600 prompt words (not walked; inferred).

**Coverage rows** (`interview/2025/coverage/scope.yaml` and a new `rental.yaml`):
- Restated, **end changes** (owner approval, N9): `scope.rental` (house → computed), `scope.royalties` (→ computed).
- Restated, same end: `scope.equipment_rental` (`scope.rent_personal: true` → refused `scope.schedule1`);
  `scope.passive` rows (narrowed wording).
- New refusal rows, each told at its own question: short stays ≤7; ≤30 with services; Worksheet 5-1 (home, ≥15 days,
  loss); self-rental; real estate professional; not at risk; not for profit; depletion (rental and royalty); QBI
  business; grouping; personal property in a rental (D3); nonresidential before 1994; ADS; vehicle (D5); prior loss not
  active both years (D2); EIC with Schedule E (D6); EBL.
- New computed rows: excluded (<15 days); personal use not a home; prior loss absorbed; Part V.

**Personas:** new `14_rental_house` (typical); `11_refused_rental` restated to the short-stay refusal
(`end: { refused: rental.not_rental_activity }`); the existing personas' walks must not gain a step (the filer with
nothing).

---

## 5. Fixtures (hand-predicted; cents, half-up; single, wages only unless stated; standard deduction)

| # | Inputs | Expected key values (arithmetic) | Evidence |
|---|---|---|---|
| F1 | Wages 60,000. SFR, 365 fair days, rents 18,000; mortgage int. 6,000, tax 2,400, insurance 1,200, repairs 800; building 160,000, Feb 2020 | dep 160,000 × 3.636% = **5,817.60**; line 20 = 16,217.60; line 21 = **1,782.40** = line 24 = 26 = s1.line5; Form 8582 not shown; AGI 61,782.40 | Table A-6 year 6 |
| F2 | Pub. 527 p. 21 house: rents 13,500; expenses 9,350 (8,000 + 250 + 400 + 500 + 200); building 120,000, Feb 2020; wages 50,000 | dep **4,363.20**; line 21 = **−213.20** = line 22 (exception); AGI 49,786.80 (Pub. prints 4,363 and (213): whole dollars) | published example |
| F3 | Pub. 925 p. 6: wages 120,000; one active rental with line 21 = −31,000 (rents 12,000; mortgage 28,000; tax 4,500; ins 1,500; repairs 3,000.60; dep 165,000 × 3.636% = 5,999.40, placed 2018) | 8582: 1b −31,000; 3 −31,000; 4 31,000; 6 120,000; 7 30,000; 8 **15,000**; 9 15,000; 11 15,000; VI (d) 16,000; VII (c) 16,000; VIII (c) **15,000**; line 22 −15,000; s1.line5 −15,000; AGI 105,000; carryforward **16,000** | published example |
| F4 | Two properties, wages 130,000: A line 21 +4,000; B line 21 −20,000 | 1a 4,000; 1b −20,000; 3 −16,000; 4 16,000; 7 20,000; 8 10,000; 9 10,000; 10 4,000; 11 14,000; B: VI (c) 10,000, (d) 10,000; VII C = 16,000 − 10,000 = 6,000 → B (c) 6,000; VIII (c) 14,000; line 22 B −14,000; line 24 4,000; line 25 −14,000; line 26 −10,000; AGI 120,000 | i8582 arithmetic |
| F5 | Prior loss absorbed: wages 160,000; one rental line 21 +3,000, prior 5,000 | overall loss 2,000; 1a 3,000, 1c −5,000, 3 −2,000; 6 ≥ 5 → 9 = 0; 11 3,000; VII (c) 2,000; VIII (a) 5,000, (c) **3,000**; line 22 −3,000; line 26 0; carryforward 2,000 | i8582 p. 15 (profit on 21, allowed loss on 22, per map) |
| F6 | MAGI excludes taxable SS: pension 98,000 (taxable), SS 30,000, rental −24,000 | 8582 line 6 = **98,000** (not 123,500) → full 24,000 allowed (exception applies; form not shown); taxable SS: provisional 98,000 − 24,000 + 15,000 = 89,000 → 0.85 × 55,000 + 4,500 = 51,250 → capped **25,500**; AGI 99,500. Wrong MAGI would allow only 13,250 | i8582 p. 11 Line 6 |
| F7 | Royalty in MAGI: wages 98,600, royalty 2,400 (no expenses), rental −10,000 | MAGI 101,000 → line 8 = 25,000 − 500 = 24,500 ≥ 10,000 → allowed 10,000; Form 8582 **required** (MAGI > 100,000); line 26 = 2,400 − 10,000 = −7,600; AGI 91,000 | i8582 p. 1 Exception |
| F8 | Not a home: 200 fair days, 10 personal; rents 24,000; mortgage 12,000, tax 3,000, ins 1,500, utilities 2,100; building 220,000, 2019 | home? 10 ≤ max(14, 20) → no; ratio 200/210 = 0.952381; lines: 11,428.57, 2,857.14, 1,428.57, 2,000.00; dep 7,999.20 × r = 7,618.29; line 20 25,332.57; line 21 **−1,332.57** | i1040se p. 5; amb ratio places |
| F9 | Excluded: personal 200 days, rented 10 days for 5,000 | `rental.excluded` true; every line 0; s1.line5 0 | i1040se p. 5 |
| F10 | Part V: rental not actively participated, line 21 −4,000; wages 80,000 | 2b −4,000; 1d 0 → Part II skipped; 9 0; 11 0; VII (c) 4,000; line 22 **0**; carryforward 4,000; AGI 80,000 | i8582 p. 10 Part V |
| F11 | Conversion (Pub. 527 pp. 24–25): rental from Feb; rents 8,250; rental-period expenses 1,650 + 92 + 297 + 1,100 = 3,139; house basis 39,000 Feb 2025; furnace 4,000 May 2025; dishwasher 425 (needs D3 = compute, with bonus elected out) | dep 1,240.98 + 90.92 + 85.00 = **1,416.90**; line 21 **3,694.10**; rf4562 19i = 1,331.90; shown | published example (Pub. rounds to dollars: 1,417 / 3,694) |
| F12 | 39-year: commercial, basis 390,000, Mar 2010 (year 16) | 2.564% → **9,999.60** | Table A-7a |
| F13 | Refusals (one case each): average stay 3 days; home 30 personal / 200 rented with a loss (Worksheet 5-1); real estate professional; seller-financed nonrecourse with a loss; trailer rental | refused at `rental.not_rental_activity`, `rental.ws51`, `sche.re_pro`, `rental.not_at_risk`, `scope.schedule1` | §1.2 |

**Mutation pins to expect [I]** (mutation kinds read in `engine/src/mutate.ts`): boundary `gt→ge` survivors unless
fixtures sit on the edges — personal days exactly 14; personal = exactly 10% (300 fair / 30 personal); rented exactly
15 days; MAGI exactly 150,000 and exactly 100,000 (exception edge); loss exactly 25,000. `smaller_of/larger_of` swaps on
lines 4, 8, 9 survive when the operands are equal — add one fixture where line 1d < line 3 (a Part V gain, i8582 p. 11
example: 1d −3,000, 2d +100 → line 4 2,900). Operand replacements on Part VI/VII `part`/`whole` survive with a single
loss activity — F4 has one loss activity; add a two-loss-activity case. `remove collection filter` on
`where part4` survives without a Part V activity next to a Part IV one — add F4 + F10 combined. Param shifts:
`pal.special_max` (+$1) needs a loss > 25,000 with MAGI ≤ 100,000; `pal.rate` (+1 point) needs a phase-out case (F3).
The `choose` guards that avoid `prorate` with a zero whole will need pinned equivalence arguments if they are
unobservable (`pinned(` in mutate.ts).

**External engines [V: read `.engines/` sources]:** UsTaxes Y2025 computes Schedule E Part I (`ScheduleE.ts`) with
depreciation as an **entered amount**, no day division (it zeroes expenses of a home-used unit), and a simplified
Form 8582 (`F8582.ts`: "simplified active-participation path"; MAGI = `l11b()`, i.e. AGI; losses scaled
proportionally; property income not netted against losses; no prior-year losses). Usable as a differential only for
F1, F2-like cases with no personal use and MAGI ≤ $100,000; it will disagree by design on F3–F7, F10. OpenTaxSolver
2025 takes Schedule 1 line 5 as an input (`S1_5`) and has a royalty-only Schedule E program: a downstream integration
check only. Neither computes Table A-6.

---

## 6. 2026

From the archived drafts [V by normalized diff 2025 vs 2026]:

| Change | Evidence | Operation in `changes/2026/` |
|---|---|---|
| Schedule E line 13 split: **13a Vehicle loan**, **13b Other** | f1040se 2026 draft p. 1; i1040se 2026 draft "New line 13a—Vehicle loan" | `rental.yaml`: `rename_line`/relabel 13 → 13b; `add_line` 13a input (gated on a rental vehicle; refused while D5 refuses vehicles, so possibly a screen only); `sche` 23c unchanged |
| Standard mileage 72.5¢ (Jan–Jun), 76¢ (Jul–Dec) | i1040se 2026 What's New | only if D5 computes mileage: reuse `sc.mileage_rate_h1/_h2` from `changes/2026/scveh.yaml` (C-BUS-01) |
| Form 8582 line 6: MAGI **is reduced** by the deductible part of SE tax (figured without the special allowance) | i8582 2026 draft p. (Line 6), "For 2026 and future years, MAGI is generally reduced by the deductible part of self-employment tax" | `f8582.yaml`: `replace_expr f8582.magi_adj` to add `s1.line15`; new cite |
| SE tax deduction attributable to a passive activity may be treated as a passive deduction | i8582, p925 2026 drafts What's New | none (passive SE activities refused) |
| Bonus 100% permanent after Jan 19, 2025 | i1040se 2026 What's New | only for `rasset` if D3 computes (mirror C-BUS-11 in `changes/2026/asset.yaml`) |
| Form 8582: wording only ("Prior-years'", "commercial revitalization deduction (CRD)" spelled out); $150,000 and $25,000 unchanged | f8582 2026 draft lines 5, 8 | label/cite updates |
| Table A-6/A-7a, `realty_year` | Pub. 946 2026 not archived | `extends_with_year` adds y2026; `realty_recovery_year` table shifted; **archive p946 2026 and i4562 2026** before verifying |

---

## 7. Lane split (worktrees; claims via `tools/claims.py`)

| Lane | Model / class | Owns (no other lane edits these) | Depends on |
|---|---|---|---|
| L0 Tables | claude-sonnet (mechanical) | `tools/extract_macrs_tables.py` (A-6, A-7a from `p946.txt`), `tables/2025/macrs_mm.yaml`, `tables/2025/realty_recovery_year.yaml`, table check | — |
| L1 Property | claude-opus-5-5 (judgment) | `forms/2025/rental.yaml`, `royalty.yaml`; their params/enums block | id contract §3.1 |
| L2 Depreciation | claude-opus-5-5 (judgment) | `forms/2025/rprop.yaml`, `rf4562.yaml`; enums `rprop_kind`, `month`, `realty_year` | L0 |
| L3 Limits and totals | claude-opus-5-5 (judgment) | `forms/2025/f8582.yaml`, `sche.yaml`, `s1.yaml` (line 5, line 10, EBL), `f8960.yaml` (4a/4c), `eic.yaml` (gate); `pal.*` params | id contract |
| L4 Interview | claude-opus-5-5 (judgment) for wording; Sonnet for fixture JSON and bookkeeping | `forms/2025/scope.yaml`, `interview/2025/questions.yaml`, coverage rows, personas, `categories.json`, fixtures | L1–L3 merged |
| L5 (optional, D3) | claude-opus-5-5 | `forms/2025/rasset.yaml`, `mq.yaml` | L1 |

`params/2025.yaml` and `ambiguities/2025.yaml` are shared: each lane appends its own contiguous block; the integrator
merges structurally. Bank entries are L4's alone; other lanes file requests in their notes.

**Reviews (one per form per round, after its fixes)** [E]: new forms rental, royalty, rprop, rf4562, sche, f8582 →
transcription + render + class M = 18; changed s1, scope, f8960, eic → line-scoped transcription + render, class M for
s1 and f8960 ≈ 10; table second transcription 1; sampled completeness/screen/false-no per release 3. **≈ 30 review
calls**; several may exceed $3.00 and need `--approve-cost`.

---

## 8. Owner decisions and risks

**Decisions** (recommended first):

- **D1 Scope of Form 8582.** Full Parts I–VIII with prior losses and Part V. Alternative: exception only (refuse any
  return needing the form) as a first commit.
- **D2 Mixed use.** Compute the not-a-home division (all lines prorated, amb 6) and refuse home-used with a loss; refuse
  home-used with a profit too in v1 (it is nonpassive and touches Schedule A). Prior loss from a year without active
  participation: refuse (R15) rather than ask.
- **D3 Personal property in rentals** (appliances, carpet, furniture, land improvements). Refuse in v1; then a
  `rasset` lane copying the subset of `asset` (no section 179, p946 p. 16; bonus; mid-quarter joined in `mq`).
  Many landlords have an appliance in recovery, so the v1 refusal costs coverage [I].
- **D4 Royalties.** Compute without depletion; refuse depletion.
- **D5 Vehicles.** Refuse in v1; standard mileage later.
- **D6 EIC.** Keep refusing with Schedule E; archive Pub. 596 later.
- **D7 NIIT.** Compute line 4a = Schedule 1 line 5 and narrow `f8960.unsupported`. Alternative: keep refusing rentals
  above the NIIT threshold.
- **D8 QBI.** Rentals not QBI; refuse a filer who says the safe harbor or section 162 applies.
- **D9 Commercial.** Compute 39-year placed 1994+; refuse earlier.
- **D10 Prior-year depreciation.** From the tables (Stage 14 precedent) rather than the filer's figure.
- **D11 Placement.** `scope.rental` at 130; property topic at 268–269.
- **D12 Coverage row end changes** for the house and royalty rows (N9).
- **D13 QJV.** Not asked; spouses co-owning enter one property; an elected QJV enters each spouse's share as a separate
  property (no tax effect, i1040se p. 2).
- **D15 EBL.** Count Schedule E losses toward the existing screen.

**Risks:**

- Basis is the hardest input (land split, conversion basis, improvements); a wrong basis is silent. Mitigation: help
  pointing at the prior depreciation schedule; first-year help on assessed-value split (i1040se p. 7).
- A preparer's earlier schedule may differ from the tables by cents or method; recomputing from tables can disagree
  with the filer's records (amb 8).
- Carryforward inputs depend on the filer finding the 2024 Form 8582; a filer whose software held a loss back may
  answer No wrongly (the guard is the help text only).
- Double entry of the rental mortgage on Schedule A (one fact, one asker): needs help changes in `sa`.
- Rounding residue in Parts VI–VIII (cents) against lines 9 and 11 (amb 3).
- The short-stay test is the commonest refusal and is easy to answer wrongly (lease length versus average stay).
- The coverage gain is unmeasured until `categories.json` is updated and the estimator rerun (T-294).
- The interview redraft protocol counts steps: about 25 steps per property for the typical filer [I], to be compared
  by walks before and after.
