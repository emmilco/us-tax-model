# Design scout: Schedule E Parts II and III — Schedules K-1 (Forms 1065, 1120-S, 1041) — TY2025

Read-only scout, 2026-11-15. Model claude-opus-5-5, class judgment, year 2025, jurisdiction us.
Tree read: `.claude/worktrees/sweep-tasks` (HEAD 63a20efc). Nothing in the repository was changed.
Locators: `doc p. N` = N-th form-feed chunk of `sources/2025/<doc>.txt` (equal to the printed page for the
instructions read here). Builds on `/tmp/scout-schedule-e.md` (lane x1-sche: Schedule E Part I, Form 8582, called
"the Part I design" below) and on the earlier map `research/premises/stage17-schedule-e.md` §3.4–3.5 with its
verification (`…verification.md`, errors E1–E12, O1–O5), re-checked here against the current tree.

Marks: **[V]** checked in this session against the named file; **[I]** inferred; **[E]** estimate; **[T]** testimony
(a prior write-up not re-checked).

---

## 1. Scope

### 1.1 What this area adds to the Part I design

The Part I design builds `rental`, `royalty`, `rprop`, `rf4562` (collections) and `sche`, `f8582` (forms). This area
adds three collections under `person` and extends four of its lines (§3.6):

| New | Kind, parent | One entry per | Feeds |
|---|---|---|---|
| `k1p` | collection, `person` | Schedule K-1 (Form 1065) | Schedule E line 28 (P), Form 8582 Parts IV/V–VIII, Schedule B, Form 1040 lines 2a/2b/3a/3b/25c, Schedule D lines 5/12, 28% and §1250 worksheets, Schedule SE line 2, Form 8995 line 1, Form 8960 line 4b |
| `k1s` | collection, `person` | Schedule K-1 (Form 1120-S) | same, minus SE; plus the S corporation basis gate (Form 7203, D-K1) |
| `k1e` | collection, `person` | Schedule K-1 (Form 1041) | Schedule E line 33, Form 1040 lines 2a/2b/3a/3b/25c/26, Schedule D, Form 8960 line 7, Form 8995 |

Separate `k1p` / `k1s` collections because the papers number their boxes differently (interest is 1065 box 5 but
1120-S box 4; f1065sk1 p. 1, f1120ssk p. 1 [V]) and N7 asks for "a paper ... entered in the order its boxes are
printed"; SE, general/limited partner and Form 7203 each belong to one entity only. `person` parent because box 14
code A goes to the person's own Schedule SE (i1065sk1 p. 21, "If you and your spouse are both partners, each of you
must complete and file your own Schedule SE") [V].

### 1.2 Computed after this work

| # | Situation | Source |
|---|---|---|
| K1 | Partnership or S corporation K-1, domestic, not a PTP, one activity per box (boxes 22/23, 1120-S 18/19 unchecked): box 1 (trade or business), box 2 (rental real estate), box 3 (other rental), each its own activity | i1065sk1 p. 14 Boxes 1–3; p. 9, "If the partnership had more than one activity, it'll attach a statement" [V] |
| K2 | Box 1 materially participated → nonpassive, column (i)/(k); not materially participated → passive, column (h) or Form 8582 → (g) | i1065sk1 p. 14 Box 1 items 1–2; i1120ssk p. 6 Box 1 [V] |
| K3 | Box 2 passive; Part IV (special allowance) when actively participated as general partner or S shareholder with ≥10% interest; else Part V. Box 2 loss with the Form 8582 exception (conditions a–h) | i1065sk1 p. 14 Box 2 items 1–4; p. 11, "Limited partners can't actively participate", "less than 10% (by value)" [V] |
| K4 | Box 3 passive, Part V | i1065sk1 p. 14, "The amount in box 3 is a passive activity amount for all partners" [V] |
| K5 | Guaranteed payments 4a (services) → column (k) | i1065sk1 p. 15 Box 4a [V] |
| K6 | Portfolio boxes: interest (1065 5 / 1120-S 4 / 1041 1) → Schedule B, 1040 line 2b; ordinary dividends (6a / 5a / 2a) → 3b; qualified (6b / 5b / 2b) → 3a; ST gain (8 / 7 / 3) → Schedule D line 5; LT gain (9a / 8a / 4a) → line 12; collectibles (9b / 8b / 4b) → 28% worksheet line 4; unrecaptured §1250 (9c / 8c, business assets only) → worksheet line 5; (1041 4c) → line 11 | i1065sk1 pp. 15–16; f1041sk1 p. 2 "Report on"; i1041sk1 p. 2 [V] |
| K7 | Self-employment: 1065 box 14 code A → Schedule SE line 2 (general partners; no reductions since UPE, §179, depletion refused); 1120-S has none | i1065sk1 p. 22 Code A; i1040se p. 10, "Your share of the net income of an S corporation is not subject to self-employment tax" [V] |
| K8 | Tax-exempt interest (1065 18A / 1120-S 16A / 1041 14A) → 1040 line 2a; 18B, 18C, 16B, 16C information | i1120ssk p. 15 Box 16 Code A; f1041sk1 p. 2 14A [V]; i1065sk1 18A [T: map, verification "Confirmed"] |
| K9 | Backup withholding (1065 15 O / 1120-S 13 O / 1041 13 B) → 1040 line 25c; 1041 13 A estimated tax credited → line 26 | i1065sk1 p. 34 Code O; i1120ssk p. 13 Code O; f1041sk1 p. 2 [V] |
| K10 | Section 199A statement (1065 20 Z / 1120-S 17 V / 1041 14 I) → Form 8995 line 1, below the threshold only (existing `qbi.via_8995a` refuses above) | i1065sk1 p. 29 Code Z; i8995 pp. 2–3 [V] |
| K11 | Passive losses limited through the Part I design's Form 8582, with per-activity prior-year unallowed losses (2024 Form 8582 Part VII (c)) | i1065sk1 p. 9, "report ... using the Instructions for Form 8582"; f8582 pp. 1–2 [V] |
| K12 | Nonpassive losses (box 1 materially participated) after the filer confirms basis and at-risk cover them (D-K2, D-K3); S corporation only under D-K1 | i1065sk1 p. 3, "the basis limitations, the at-risk limitations, the passive activity limitations, and the excess business loss limitations" [V] |
| K13 | Estate/trust K-1 income: boxes 1–4c, 5 (column (f)), 6–8 income (column (d) passive by default, (f) on material participation), 13 A/B, 14 A, H (Form 8960 line 7), I (QBI) | f1041sk1 p. 2; i1041sk1 p. 2; i1040se p. 11 "ES payment claimed" [V] |
| K14 | NIIT: K-1 Part II/III totals reach line 4a through Schedule 1 line 5 (Part I design D7); nonpassive trade-or-business K-1 income reversed on line 4b; 1041 14 H on line 7 | i8960 p. 8 Lines 4a, 4b, "Nonpassive income not subject to NIIT is entered as a negative amount on line 4b"; "Any income from an estate or trust reported in Part III ... is taken into account on line 7" [V] |
| K15 | Form 8582 MAGI includes nonpassive K-1 income or loss | i1065sk1 p. 10, the nonpassive portion "is included in modified adjusted gross income (MAGI)" (PTP text, same rule); i8582 p. 11 Line 6 [V per Part I design] |
| K16 | Informational boxes with no 1040 effect accepted: 6c, 13 AE, 18 B/C, 20 A/B (unless Form 4952 is used, R-K18), 20 N, 20 AG, 1120-S 16 B/C, 17 AC | i1065sk1 p. 15 Box 6c, "Dividend equivalents aren't reported on Form 1040"; p. 25 Code AE text read [V]; others [I] |

### 1.3 Still refused (gate id proposed; all asked under the K-1 they concern, N11)

| # | Situation | Gate | Reason / cite |
|---|---|---|---|
| R-K1 | Publicly traded partnership (item D) | `k1p.ptp` | own netting rules, Form 8582 not used, 751 on sale; i1065sk1 p. 10, p. 11 Item D [V]. D-K4 |
| R-K2 | More than one activity (1065 box 22/23, 1120-S 18/19) | `k1p.multi`, `k1s.multi` | statement-defined activities; i1065sk1 p. 9 [V] |
| R-K3 | Foreign partnership (line 28 col (c)), K-3 with foreign items, foreign taxes (1065 21, 1041 14 B) | `k1p.foreign` | Form 8865, 1116; i1040se p. 9 [V] |
| R-K4 | Sale or other disposition of the interest; final K-1 with a disposition; 20 AB/AC/AD | `k1p.disposed` | frees suspended losses, 751, Form 8949; i1065sk1 p. 2 [V] |
| R-K5 | Loss or deduction above basis (partnership); a prior-year basis or at-risk loss (line 27); unreimbursed partnership expenses | `k1p.basis_short`, `sche.line27` | i1040se p. 8 Basis rules; p. 10 Line 27 [V] |
| R-K6 | Any amount not at risk with a loss (Form 6198) | `k1p.not_at_risk` | i1065sk1 p. 8 [V] |
| R-K7 | S corporation with a loss, distribution (16 D), stock disposition or loan repayment — **unless D-K1 encodes Form 7203** | `k1s.f7203` | f1040se p. 2 Part II note, "you must check the box in column (e) on line 28 and attach the required basis computation" [V]; f7203 not archived |
| R-K8 | Distribution above basis (1065 19) | `k1p.dist_over_basis` | i1065sk1 p. 25 [T, map] |
| R-K9 | Box 10 / 1120-S 9 section 1231 | `k1p.box10` | Form 4797 not encoded; i1065sk1 p. 16 Box 10 [V] |
| R-K10 | Box 11 (all codes) / 1120-S 10 | tick | i1065sk1 p. 33 list [V] |
| R-K11 | Box 12 / 1120-S 11 section 179 | tick | |
| R-K12 | Box 13 / 1120-S 12 codes other than AE (charitable A–G, H investment interest, L, M, R, Z, ZZ …) | tick | Schedule A/4952/7206 paths. D-K6 may compute 13 A |
| R-K13 | Box 15 / 1120-S 13 credits other than O (Form 8582-CR, 3800) | tick | i1065sk1 p. 22 [V] |
| R-K14 | Box 17 / 1120-S 15 / 1041 12 AMT items | tick → existing `s2.amt` remedy | i1040se p. 8 Tax preference items [V] |
| R-K15 | Box 20 codes other than A, B, N, Z, AG (Y, AJ with an EBL effect, AE/AF Form 8990, …) | tick | i1065sk1 pp. 35–36 [V] |
| R-K16 | 1065 4b guaranteed payments for capital — D-K10 | tick | NII treatment not in the archive |
| R-K17 | 14 B, 14 C (farm, optional methods); negative 14 A on a passive or limited activity | tick | i1065sk1 p. 22 [V] |
| R-K18 | Form 4952 in use together with 20 A/B, 17 A/B or 1041 14 E (double count of box 5 interest in line 4a) | `f4952` existing K-1 refusal kept | f4952.yaml lines 19–37 [V] |
| R-K19 | Royalties (1065 7 / 1120-S 6): Schedule E line 4 property column | tick | i1065sk1 p. 15 Box 7 [V]; D-K6 |
| R-K20 | Real estate professional; trader partnership (box 1 from trading; NII) | `sche.re_pro` (Part I), `k1p.trader` | i1065sk1 p. 8 item 2; i8960 p. 8 [V] |
| R-K21 | Material participation by tests 4, 6 or 7 only | tick | i1065sk1 p. 9 [V]; D-K5 |
| R-K22 | QBI when a prior-year suspended K-1 loss is allowed this year (tracking of qualified portions) | existing `qbi.suspended`, made derived | i8995 p. 3, "Losses and deductions retain their status ... you must track each category" [V] |
| R-K23 | Estate/trust: net loss in 6–8, box 9 deductions, 10 (estate tax), 11 (final-year deductions, incl. 11 A → Sch. 1 line 24k, not in `s1`), 13 other credits | ticks | i1041sk1 p. 2 [V]; `s1.line24k` absent [V] |
| R-K24 | Excess business loss (Form 461) | `s1.ebl` extended (Part I design D15) | Form 461 not archived |
| R-K25 | EIC with any Schedule E amount | `eic.step2_other` via `sche.any` (Part I design D6) | i1040gi p. 40 [V per Part I design] |
| R-K26 | MFS | `s3.mfs` (unchanged) | |

### 1.4 Gates that go away or narrow [V: read in the named files]

- `scope.k1` (scope.yaml line 400) stays the off-ramp but **leaves the `any` list of `scope.schedule1`** (line 990).
  Every refusal on `scope.schedule1` was listed by the Part I design; for this area `s8812.eiw_3` ("Earned Income
  Worksheet, lines 2a–2e (statutory employee, farm or partnership income)", s8812.yaml line 596) and
  `s1a.line5_calc` (tips in a Schedule E business) are lifted with it (verification E1): `s8812.eiw_3` must take K-1
  14 A into line 2b (O4 of the verification) or gain its own gate; `s1a.line5_calc` needs a new gate on any
  nonpassive K-1 box 1 (tips in a pass-through business refused) [I].
- `scope.passive` ("income or a loss from ... a business or rental that you owned but did not help run", line 907) would
  refuse every passive K-1 investor: narrowed to activities not entered as a K-1 or a rental (same change the Part
  I design makes for rentals; one edit).
- `person.se_screen` (person.yaml line 1388): the clause "net earnings from self-employment from a partnership
  (Schedule K-1, box 14, code A)" is removed. The SEP clause (line 1726) stays (partner SEP refused).
- `sd.other_forms` (sd.yaml line 215): drop "or capital gains or losses on a Schedule K-1" (the remaining clauses
  stay; 11 C section 1256 is refused under R-K10).
- `qbi.unsupported` label (qbi.yaml line 122) and `f8995` note: K-1 QBI no longer refused by scope; `qbi.suspended`
  derived from K-1 prior-loss allowance (R-K22) rather than only asked.
- `f8960.unsupported`: drop "pass-through" from "annuity, rental, royalty, business or pass-through income" (the
  Part I design drops rental, royalty).
- `f2441` notes (lines 1007, 1382) name "partnership (Schedule K-1, scope.schedule1)": dependent care benefits from a
  partnership become a new refusing tick under `k1p` (1065 13 O is in R-K12) [I].
- `tools/coverage/categories.json`: `partnership_scorp` and `estate_trust` → `refused: false`, `gates: []`, label
  "supported; remaining refusals unmeasured" (verification E4: the estimator keys on the flag) [V].

### 1.5 Share served [E]

`reports/2025/filer_coverage.md` (generated 2026-11-01, stale, T-294) [V]: partnership or S corporation income or
loss **3.5%** (5,554,014 returns, a lower bound: max of the partnership and S corporation counts); estate or trust
**0.4%** (685,175). SOI detail [T, verified by the verification]: partnership net income 3.27 M / net loss 2.10 M;
S corporation 4.14 M / 1.42 M; estate/trust 0.65 M / 0.04 M.

No archived count exists for PTP holders, S corporation distributions, multi-activity K-1s, box 10/11/13/15
amounts or K-3s. Inferences [I/E]: S corporation shareholders who take distributions are likely the majority
(owner-operators), so **without Form 7203 (D-K1) the S corporation half is mostly still refused**; partnership
investors in funds often carry K-3s, box 13 and 20 statements and multiple activities (refused). Estimate of the
gain: **+1.0 to +2.0 points with D-K1 = encode Form 7203; +0.5 to +1.0 without**, plus **+0.2 to +0.3** for
estates and trusts (final-year K-1s with box 11 are the main residual). Unmeasured until `categories.json` is
updated and the estimator rerun.

---

## 2. Sources

### 2.1 Needed for 2025, archived [V: `ls sources/2025`]

| Doc | Pages used |
|---|---|
| f1065sk1 (created 2/26/25) | p. 1 (items D, G, J, K1, L; boxes 1–23) |
| i1065sk1 (2025) | p. 2 (sale), p. 3 (limitation order; basis worksheet start), pp. 3–7 (Worksheet for Adjusting the Basis), p. 8 (at-risk; nonpassive list), p. 9 (material participation tests 1–7; limited partners), pp. 10–11 (PTP; special allowance; 10%; MAGI), p. 12 (items J, K1, L), pp. 14–16 (boxes 1–11), p. 21–22 (box 14, 15), pp. 29–30 (20 Z), pp. 33–36 (list of codes) |
| f1120ssk / i1120ssk (2025) | f p. 1; i p. 2–3 (basis, Form 7203 mention), p. 6 (box 1), p. 7, p. 13 (13 O), p. 15 (16 A–D, 17 A), p. 17 (17 V) |
| f1041sk1 / i1041sk1 (2025) | f p. 2 ("Report on" list); i p. 2 (boxes 1–11 A) |
| f1040se / i1040se (2025) | f p. 2 (lines 27–43); i pp. 8–11 (Parts II, III, line 27, 28) |
| f8582 / i8582, p925 | as the Part I design |
| f6198 / i6198 (Rev. Nov 2025) | cited by R-K6 only |
| f8995 / i8995 | i8995 p. 2 ("deductible part of self-employment tax"), p. 3 (K-1 items, suspended losses), p. 4 Line 1 |
| f8960 / i8960 | i8960 p. 8 (lines 4a, 4b), p. 13 (line 7) |
| f4797, f8990, f1116, f8949 | refusals only |

### 2.2 Not archived (do not fetch; to archive)

| Doc | Needed for | Priority |
|---|---|---|
| **Form 7203 and instructions (2025)** | D-K1 (S corporation stock basis; required with any distribution or loss) | high, gates most S corporation coverage |
| Pub. 541 (Partnerships) | basis help text, D-K2 option (b) | low |
| Form 461 + instructions (2025) | R-K24 reading (shared with Part I D15) | medium |
| Form 8582-CR + instructions | only if passive credits are ever computed | none now |
| i1065sk1 **2026** | 2026 edition (not posted when the 2026 set was fetched; absent from `sources/2026`) | for §6 |

### 2.3 2026 editions [V: `sources/2026/manifest.json`, normalized diffs]

| Doc | 2026 status | Change found |
|---|---|---|
| f1065sk1 | DRAFT 2026-05-21 | none of substance ("current year" wording) |
| f1120ssk | DRAFT 2026-04-29 | none |
| f1041sk1 | DRAFT 2026-06-01 | a line reference beside 28% rate gain changed ("16"→"17e", page-2 list) [V diff; meaning not read] |
| i1120ssk | DRAFT 2026-09-18 | 17 V threshold $201,750 ($201,775 MFS; $403,500 MFJ) [V] |
| i1041sk1 | DRAFT 2026-08-25 | not diffed in detail |
| i1065sk1 | **not archived** | — |
| f1040se / i1040se | DRAFTs | Parts II/III unchanged; Part I line 13a/13b only [V diff] |
| f8995 / i8995 | DRAFTs | thresholds; minimum deduction for active QBI (already in `changes/2026/f8995.yaml`) [V] |
| i8582, p925 | DRAFTs | MAGI less deductible SE tax (Part I design) |

---

## 3. Encoding plan

### 3.1 Activity rows: one shape, seven users

Each K-1 carries up to three activities (box 1, 2, 3); with `rental` the Form 8582 per-activity chain (net income,
net loss, prior, overall loss, VI (c), VII (a), VII (c), VIII (a), VIII (c)) recurs 7 times. Two encodings:

- **(a) Suffix lines** in each collection: `k1p.b1_net_loss`, `k1p.b2_…`, `k1p.b3_…` (27 lines per collection,
  copied from the Part I design's `rental.*` rows). No new mechanism; mechanical; 3× the review surface.
- **(b) A def `pal_row`** (parameters: `net` Dollars, `prior` NonNegDollars, `part4` Bool) instantiated per activity,
  as `tax_on_amount` is (`forms/2025/tax_on_amount.yaml`, `qdcg.line22` binds it [V]). Whether a def may be
  instantiated with bindings that are lines of a collection entry was **not verified** (spec 4.7.1/4.7.6 describe the
  memo key as frame key + def + bindings, which suggests yes [I]). D-K16.

Recommendation: (a) for v1 (no dependency on an engine question), (b) as a later refactor of rental + K-1 together.

### 3.2 `k1p` lines (per Schedule K-1, Form 1065). Printed column/box in brackets.

| id | printed | type | sketch | cite |
|---|---|---|---|---|
| `k1p.name`, `k1p.ein` | 28 (a), (d) | display inputs | | f1040se p. 2 |
| `k1p.ptp` | item D | Bool, refusing | | i1065sk1 p. 11 Item D |
| `k1p.general` | item G | Bool | "general partner or LLC member-manager" | f1065sk1 p. 1 item G |
| `k1p.box1`, `box2`, `box3` | 1, 2, 3 | Dollars | inputs, asked behind a tick of nonzero boxes | i1065sk1 p. 14 |
| `k1p.box4a` | 4a | NonNegDollars | input | p. 15 |
| `k1p.box5`, `box6a`, `box6b` | 5, 6a, 6b | NonNegDollars | inputs | p. 15 |
| `k1p.box8`, `box9a` | 8, 9a | Dollars | inputs | p. 15 |
| `k1p.box9b`, `box9c` | 9b, 9c | NonNegDollars (9b loss refused) | inputs | p. 16 |
| `k1p.box14a` | 14 A | Dollars | input; negative refused unless `nonpassive_b1` | p. 22 |
| `k1p.box15o` | 15 O | NonNegDollars | input | p. 34 |
| `k1p.box18a` | 18 A | NonNegDollars | input | [T] |
| `k1p.box19` | 19 | NonNegDollars | input (display; gates `dist_over_basis`) | [T] |
| `k1p.box20a`, `box20b` | 20 A, B | NonNegDollars | information inputs (only to gate R-K18) | p. 27 |
| `k1p.qbi_stmt` | 20 Z | Dollars | "QBI or loss" from the statement (0 when no Z) | p. 29 |
| `k1p.material` | (gate) | Bool | from the layered participation questions (§4); false when `general` false unless tests 1/5 | p. 9 |
| `k1p.active` | (gate) | Bool | `general` ∧ input "helped make management decisions" ∧ input "owned at least a tenth" | p. 11 |
| `k1p.b{1,2,3}_passive` | (gate) | Bool | b1: ¬material; b2, b3: true | p. 14 |
| `k1p.b2_part4` | (gate) | Bool | `b2_passive` ∧ `active` | i8582 p. 10 Part IV |
| `k1p.b{n}_prior` | Part IV/V (c) | NonNegDollars | gated input (parent `k1p.prior_any`) "2024 Form 8582, Part VII, column (c)" | i8582 p. 10 |
| `k1p.b{n}_net_income`, `_net_loss`, `_overall_loss`, `_p6c` (b2 only), `_p7a`, `_p7c`, `_p8a`, `_allowed` | Parts IV–VIII | as `rental.*` in the Part I design §3.2 | same expressions with `box{n}` for `line21` | i8582 pp. 10–13 |
| `k1p.col_g` | 28 (g) | Dollars ≤ 0 | −Σ over passive activities of `_allowed` | i1040se p. 9 |
| `k1p.col_h` | 28 (h) | NonNegDollars | Σ passive `_net_income` | same |
| `k1p.col_i` | 28 (i) | Dollars ≤ 0 | `min(0, box1)` when ¬`b1_passive` | i1065sk1 p. 14 item 1 |
| `k1p.col_j` | 28 (j) | 0 | §179 refused | |
| `k1p.col_k` | 28 (k) | NonNegDollars | `max(0, box1)` when nonpassive + `box4a` | p. 14–15 |
| `k1p.sch_e_any` | (gate) | Bool | any of g–k ≠ 0 (Schedule E row shown) | i1040se p. 10 Line 28 |
| `k1p.nonpassive` | (helper) | Dollars | `col_i + col_k` (MAGI, NIIT 4b) | i8960 p. 8 |
| `k1p.ebl_part` | (helper) | Dollars | nonpassive box 1 + allowed passive box-1 loss (trade or business) | i1065sk1 p. 11 Excess Business Loss |
| `k1p.qbi` | 1 (c) | Dollars | `qbi_stmt` when ≥ 0 or the box-1 loss is fully allowed; else `−prorate(−qbi_stmt, b1_allowed, b1_net_loss, 6)`; less `qbi_se` (D-K8) | i8995 p. 3, "only the portion of the allowed loss ... attributable to QBI" |
| `k1p.qbi_se` | (helper) | NonNegDollars | `prorate(person.se_line13, max(0,box14a), person.se_pos_whole, 6)` | i8995 p. 2; amb `qbi_attribution` |
| screens | (gates) | Bool | ptp, multi, foreign, disposed, basis_short (asked on any loss: box 1–3 < 0, 8/9a < 0), not_at_risk (same), dist_over_basis (box19 > 0), trader, rare_boxes tick group, participation_other | §1.3 |

### 3.3 `k1s` lines (Form 1120-S)

Same as `k1p` with the 1120-S box numbers (f1120ssk p. 1 [V]): 1, 2, 3, 4 (interest), 5a, 5b, 7, 8a, 8b, 8c, 13 O,
16 A, 16 D, 17 A/B, 17 V (`qbi_stmt`), 18/19 (multi). Differences: no `general` (a shareholder may actively
participate; i1040se p. 9, "if you are a general partner or an S corporation shareholder ... and you meet all of the
conditions") [V]; no SE lines; `k1s.qbi` without `qbi_se`; the Form 7203 gate `k1s.f7203` = loss ∨ `box16d > 0` ∨
disposition ∨ loan repayment (refusing under D-K1 = refuse; computed under D-K1 = encode, then
`k1s.basis_short` reads Form 7203 Part III). Distributions are not dividends (i1120ssk p. 1) [T].

### 3.4 `k1e` lines (Form 1041)

`k1e.box1`, `box2a`, `box2b`, `box3`, `box4a`, `box4b`, `box4c`, `box5`, `box6`, `box7`, `box8` (≥ 0: a negative
amount refuses), `box13a`, `box13b`, `box14a`, `box14h` (Dollars), `qbi_stmt` (14 I); `k1e.material` (tick, default
false); `k1e.col_c` = 0 (losses refused); `col_d` = Σ boxes 6–8 when ¬material; `col_e` = 0; `col_f` = box5 +
(boxes 6–8 when material); `k1e.passive_income` (feeds Form 8582 Part V line 2a as an activity with net income
only: it can free other passive losses); screens for 9, 10, 11, 12, 13 C–ZZ, 14 B, other codes.
Cites: f1041sk1 p. 2 "Report on" rows; i1041sk1 p. 2, "Box 5 ... isn't subject to the passive activity rules"; Boxes 6
Through 8, "The rules for applying these limitations to beneficiaries haven't yet been issued" (amb) [V].

### 3.5 Person-level helpers (person.yaml)

Return-level forms read entries only through `sum_over person field person.X` (spec 4.4: an entry reads only its
enclosing entries [V]); each new reader needs a person sum over `k1p`, `k1s`, `k1e`:
`person.k1_int`, `k1_ord_div`, `k1_qual_div`, `k1_st`, `k1_lt`, `k1_28`, `k1_1250_5`, `k1_1250_11`, `k1_taxexempt`,
`k1_backup`, `k1_est`, `k1_se` (14 A), `k1_g`, `k1_h`, `k1_i`, `k1_k`, `k1e_c`…`k1e_f`, `k1_nonpassive`,
`k1_ebl`, `k1_qbi`, `k1_8582_{1a,1b,1c,2a,2b,2c,p6,p7}`, `k1_prior_allowed` (for R-K22), `k1_any` (Schedule E).

### 3.6 Lines of the Part I design that this area extends (request to lane x1-sche: split now)

| Part I line | Today (Part I design) | Change | Ask of x1-sche |
|---|---|---|---|
| `f8582.line1a/1b/1c` | sum over `rental where part4` | + `sum_over person field person.k1_8582_1a…` | write each as `sum(f8582.rent_1a)` over a rental helper so the K-1 lane adds one operand |
| `f8582.line2a/2b/2c` | sum over rental Part V | + K-1 Part V (+ `k1e` income in 2a) | same |
| `f8582.p6_total`, `p7_total` | sum over rental | + K-1 | same |
| `f8582.required` | rental conditions | any K-1 Part V activity with a loss or prior loss; any Part IV K-1 not meeting i1065sk1 p. 14 a–h | expose a helper |
| `f8582.magi_income` / `sche.nonpassive_net` | royalty net | + `person.k1_nonpassive`, + `k1e` col (f) | keep `sche.nonpassive_net` a sum |
| `sche.line41` | `copy line26` | `sum(line26, line32, line37)` | — |
| `sche.any` | rental/royalty | ∨ any `k1p/k1s.sch_e_any` ∨ any `k1e` col ≠ 0 (a portfolio-only K-1 does not put Schedule E on the return) | — |
| `s1.ebl_total` | + Schedule E line 26 when negative (D15) | + `person.k1_ebl` | — |

New `sche` lines (this area): `sche.line27` (Bool, refusing Yes), `sche.line29a_{h,k}`, `sche.line29b_{g,i,j}`,
`sche.line30` (h + k), `sche.line31` (g + i + j, held negative, T-004 precedent [T]), `sche.line32`,
`sche.line34a_{d,f}`, `sche.line34b_{c,e}`, `sche.line35`, `sche.line36`, `sche.line37`, `sche.line42` (0; 14 B
refused). f1040se p. 2 [V].

### 3.7 Other existing lines that change [V: ids and current expressions read]

| Line | Today | Change |
|---|---|---|
| `sb.line2` | `sum_over interest field interest.amount` | + `sum_over person field person.k1_int` (Schedule B line 1 lists the entity) |
| `sb.line6` (→ `f1040.line3b`) | copy of ordinary dividends | + `person.k1_ord_div` |
| `f1040.line3a` | input total | `sum(f1040.line3a_entered, k1 qualified)`; help "not from a K-1" (N8) |
| `f1040.line2a` | `sum(tax_exempt_interest, div.box12)` | + `person.k1_taxexempt` |
| `f1040.line25c` | `sum(line25c_other…, f8959.line24)` | + `person.k1_backup` (help on `line25c_other` excludes K-1) |
| `f1040.line26` | input | `sum(entered, k1e 13 A)`; i1040se p. 11 "ES payment claimed" |
| `sd.line5`, `sd.line12` | `copy sd.zero` | `sum_over person k1_st / k1_lt` |
| `g28.line4`, `u1250.line5`, `u1250.line11` | K-1 parts | + K-1 sums (labels already name K-1 [V]) |
| `person.se_line2` | `copy person.sc_total` | `sum(person.sc_total, person.k1_se)` (also `person.eic_se`, `person.dc_earned` per O3) |
| `person.qbi` | `sum_over sc field sc.qbi` | + `person.k1_qbi` |
| `sc.qbi_se_pos` | whole `person.positive_profits` | whole `person.se_pos_whole` = positive profits + positive 14 A (D-K8) |
| `qbi.suspended` | input | `any(input, person.k1_prior_allowed > 0)` (R-K22) |
| `f8960.line4b` | NonNegDollars, copy zero | Dollars: `−Σ person.k1_nonpassive` (trade-or-business nonpassive; trader refused) |
| `f8960.line7` | NonNegDollars, copy zero | Dollars: `Σ k1e.box14h` |
| `s8812.eiw_2b` / `eiw_3` | copy `s1.line3`; refuses partnership | + K-1 14 A (verification O4) |
| `f2441` notes | name scope.schedule1 | name the K-1 tick |

### 3.8 Parameters, enums

No new money parameters: the Part I design's `pal.*` serve; QBI thresholds exist (`qbi.threshold` [V]). Enums:
none needed if entity is a collection; `k1e` has no enum. Constants for the 10% interest test are a Bool question.

### 3.9 Ambiguity entries (`ambiguities/2025.yaml`)

1. `amb.2025.k1_activity_per_box` — each of boxes 1, 2, 3 of one K-1 is one activity; multi-activity statements refused.
2. `amb.2025.k1_basis_by_filer` — the basis and at-risk sufficiency is the filer's statement (D-K2/D-K3), not computed.
3. `amb.2025.k1_qbi_suspended_share` — QBI of a partly suspended current-year loss is `qbi_stmt × allowed / net loss`, six places.
4. `amb.2025.k1_qbi_se_attribution` — partner's deductible SE tax attributed to the K-1 by its share of positive SE earnings (extends `amb.2025.qbi_attribution`).
5. `amb.2025.k1e_passive_default` — estate/trust boxes 6–8 passive unless the beneficiary says it materially participated (i1041sk1 p. 2: rules not issued).
6. `amb.2025.k1_nii_4b` — line 4b reverses nonpassive box 1 and 4a; 4b (capital) refused.
7. `amb.2025.k1_portfolio_no_sche` — a K-1 with only portfolio items puts no row on Schedule E.
8. `amb.2025.k1_box9c_type` — only the business-asset type of unrecaptured §1250 gain (box 9c amount); statement types refused.

---

## 4. Interview plan (construction protocol; Part I design's conventions)

**Typical filers [I]:** (a) an S corporation owner-operator: W-2 from the corporation, box 1 income, 17 V,
distributions (needs D-K1); (b) a partner in a small operating LLC (general, 14 A); (c) a limited partner in a real
estate fund (box 2 loss, suspended). **Filer with nothing:** answers the existing `scope.k1` box (no new step).
**Refused filer:** a PTP unit holder.

**Placement [V: orders 262, 264, 266 are free; 268–269 taken by the Part I design].** `scope.k1` stays at 130.2 in
tick group `own_income`. Topic `$k1p` and `$k1s` at **264**, `$k1e` at **266** (business ownership after the own
businesses 250–261, before rentals 268 and interest 270). D-K11.

| order.seq | input | prompt sketch | notes |
|---|---|---|---|
| 264.1 | `$k1p` | "List each Schedule K-1 (Form 1065) from a partnership or LLC; one entry each." | label = entity name |
| 264.2 | `k1p.ptp` | "Is the box in item D checked (a partnership traded on a stock exchange)?" | commonest refusal, alone first (3.6); [an MLP unit holder who has never read item D — help: "Item D is near the top left."] |
| 264.3 | `k1p.general` | choice "General partner or LLC member-manager" / "Limited partner or other LLC member" (item G) | |
| 264.4 | tick group `k1p_boxes` "Which boxes show an amount?" (1, 2, 3, 4a, 5, 6a, 6b, 8, 9a, 9b, 9c, 14, 18 A, 19, 20) | each tick opens its amount in printed order (N7) | |
| 264.5 | tick group `k1p_rare` (refusing): boxes 4b, 7, 10, 11, 12, 13 (other than AE), 15 (other than O), 17, 21, 20 codes other than A/B/N/Z/AG; box 22 or 23 checked; foreign partnership; K-3 with foreign tax | each refuses at its tick | |
| 264.6 | `k1p.disposed` | "Did you sell or give up any of your share in 2025?" | refuses |
| 264.7 | `k1p.work` → `k1p.hours500` → (general only) `k1p.most_hours` → `k1p.five_of_ten` | "Did you or your spouse work in this business in 2025?" No → passive (typical investor); Yes → "More than 500 hours?"; No → "Over 100 hours, and no one worked more?" / "Did you take part materially in 5 of the 10 years before?" + refusing tick for tests 4, 6, 7 | asked only when box 1 ≠ 0; [an owner with 400 hours who runs it alone answers the 500-hour child No — the next child catches it] |
| 264.8 | `k1p.active` → `k1p.tenth` | "Did you help make decisions for its rental property, such as approving tenants or rents?" → "Did you and your spouse own at least a tenth of it all year?" | asked only when box 2 ≠ 0 and general |
| 264.9 | `k1p.trader` | "Is its business trading stocks, commodities or other investments?" | asked when box 1 ≠ 0; refuses |
| 264.10 | `k1p.basis_short` | "Was your loss more than what you have in the partnership (what you put in, plus your share of income and debts, less losses and money taken out)?" | asked on any loss; help points to the basis worksheet in the K-1 instructions; refuses |
| 264.11 | `k1p.not_at_risk` | "Was any of what you have in it protected from loss, such as a loan no partner is liable for (other than a bank loan on real estate)?" | asked on any loss; refuses |
| 264.12 | `k1p.dist_over_basis` | asked when box 19 > 0 | refuses |
| 264.13 | `k1p.prior_any` → `k1p.b{n}_prior` | "Was a loss from this partnership held back on your 2024 return (Form 8582)?" | as the Part I design 268.13 |
| 264.20–33 | `$k1s` and its entries | same shape; item D absent; 1120-S box list; `k1s.f7203` asked as "Did you get money or property from the corporation in 2025 (box 16, code D), or have a loss?" refusing unless D-K1 | |
| 266.x | `$k1e` → boxes tick (1, 2a, 2b, 3, 4a–4c, 5, 6–8, 13 A/B, 14 A/H/I), `k1e_rare` tick (9, 10, 11, 12, 13 others, 14 B/F/others, a loss in 6–8), `k1e.material` (tick, rare) | | |
| 268.21 (Part I) | `sche.line27` joins the Part I design's return tick `rental_return` | "a loss held back in an earlier year by basis or at-risk rules, or partnership expenses you paid yourself" | refuses |

Existing bank help that changes (N8, one asker): interest (270) and dividends (272) — "not from a Schedule K-1";
`f1040.line3a` help; `f1040.line25c_other`, `f1040.line26` help; `scope.passive` wording narrowed.

**Cost and share [E, judgment]:** `scope.k1` Yes ≈ 4%; `k1p.ptp` Yes ≈ 25–40% of partnership K-1 holders;
`k1p.work` Yes ≈ 40%; loss ≈ 30%; `prior_any` ≈ 20% of losing entries. Typical S-corp walk ≈ 12–15 steps per K-1;
fund LP ≈ 14 (not walked).

**Coverage rows** (`interview/2025/coverage/scope.yaml` and new `k1.yaml`):
- Restated, end changes (owner approval, N9): `scope.k1` (refused → computed); rows ending at `person.se_screen`
  for partnership SE, `sd.other_forms` for K-1 capital gains, `s8812.eiw_3` for partnership income, `qbi`/`f8960`
  rows naming pass-through income (list to be generated by grep of `refused:` ends at those gates).
- New refusal rows, one per §1.3 item, each told at its own question.
- New computed rows: S corp nonpassive income; passive LP loss suspended; Part IV K-1 rental; portfolio-only K-1;
  estate final-year portfolio K-1; trust passive income.

**Personas:** `15_k1_scorp_owner` (typical, needs D-K1 or no distributions), `16_k1_fund_lp` (box 2 loss
suspended), `17_refused_ptp`; existing personas' walks must not gain a step.

---

## 5. Fixtures (hand-predicted; single unless stated; standard deduction $15,750 (`sa.standard_base` [V]); cents half-up)

| # | Inputs | Expected key values (arithmetic) | Evidence |
|---|---|---|---|
| FK1 | W-2 60,000. K-1 1120-S: box 1 40,000, materially participated, 17 V QBI 40,000, no distribution | line 28 (k) 40,000; 30 = 32 = 41 = s1.line5 **40,000**; AGI 100,000; 8995: line 2 40,000, 5 8,000, 11 = 100,000 − 15,750 = 84,250, 14 16,850, 15 **8,000**; TI 76,250 | i1120ssk p. 6; f8995 |
| FK2 | No wages. K-1 1065 general partner: box 1 50,000 materially participated, 14 A 50,000, 20 Z QBI 50,000 | SE 4a 50,000 × 0.9235 = 46,175.00; 10: × 12.4% = 5,725.70; 11: × 2.9% = 1,339.075 → 1,339.08; 12 **7,064.78**; 13 3,532.39; AGI 46,467.61; QBI 50,000 − 3,532.39 = 46,467.61; line 5 9,293.52; 11 30,717.61; 14 6,143.52; 15 **6,143.52**; TI 24,574.09 | i1065sk1 p. 22; i8995 p. 2 |
| FK3 | W-2 90,000. K-1 1065 limited partner, box 2 −12,000 | 8582 2b −12,000; 2d −12,000; 3 −12,000; Part II skipped; 9 0; 11 0; VII (c) 12,000; VIII (c) 0; 28 (g) 0; s1.line5 0; AGI **90,000**; carryforward 12,000; Form 8582 required | i8582 p. 10 Part V; i1065sk1 p. 11 |
| FK3b | As FK3 but general partner, active, ≥ 10% | Part IV: 1b −12,000; 4 12,000; 6 90,000 ≤ 100,000 → 8 25,000; 9 12,000; 28 (g) **−12,000**; AGI 78,000; Form 8582 not required (i1065sk1 p. 14 conditions a–h) | i1065sk1 p. 14 item 1 |
| FK4 | FK3 + K-1 1120-S box 1 5,000 not materially participated, 17 V 5,000; the fund's 20 Z QBI −12,000 | 2a 5,000; 2b −12,000; 2d = 3 −7,000; 10 5,000; 11 5,000; VII C = 7,000 − 0 → fund (c) 7,000; VIII (c) 5,000; S corp (h) 5,000; fund (g) −5,000; 32 0; AGI 90,000; carryforward 7,000. QBI: fund −prorate(12,000, 5,000, 12,000) = −(0.416667 × 12,000 = 5,000.004) = −5,000.00; 8995 line 2 **0**; deduction 0 | i8995 p. 3 |
| FK5 | W-2 120,000. K-1 1065 general, active, ≥ 10%, box 2 −20,000 | 1b −20,000; 4 20,000; 6 120,000; 7 30,000; 8 **15,000**; 9 15,000; VI (c) 15,000; VII (c) 5,000; VIII (c) 15,000; 28 (g) −15,000; AGI **105,000**; carryforward 5,000 | p925 p. 6 shape |
| FK6 | W-2 80,000. K-1 1120-S box 1 −10,000 materially participated, basis confirmed (D-K1), 17 V −10,000 | 28 (i) −10,000; 31 −10,000; s1.line5 −10,000; AGI **70,000**; 8995 line 2 −10,000, line 4 0, line 16 **−10,000** | i1120ssk p. 6 item 1 |
| FK7 | W-2 50,000. K-1 1065 limited partner: 5 300, 6a 1,000, 6b 800, 9a 2,500, 20 A 3,800 | no Schedule E row; `sche.any` false; 2b 300; 3b 1,000; 3a 800; Sch. D line 12 2,500 → 7a 2,500; AGI **53,800**; TI 38,050 | i1065sk1 p. 15 |
| FK8 | W-2 40,000. K-1 1041 (estate): 1 400, 2a 600, 2b 500, 3 1,000, 4a 5,000, 14 A 200 | 2a 200; 2b 400; 3b 600; 3a 500; Sch. D 5 1,000, 12 5,000; 7a 6,000; AGI **47,000** | f1041sk1 p. 2 |
| FK9 | W-2 210,000. K-1 1041 (trust): 5 3,000; 6 2,000 (no participation) | 33 (f) 3,000, (d) 2,000; 37 = 41 = s1.line5 5,000; AGI 215,000; 8960 4a 5,000; 8 5,000; 13 215,000; 15 15,000; 16 5,000; 17 **190.00** | i8960 p. 8 |
| FK10 | W-2 108,000; 1099-INT 2,000; K-1 1120-S box 1 100,000 materially participated, 17 V 100,000 | AGI 210,000; 8960 line 1 2,000; 4a 100,000; 4b **−100,000**; 8 2,000; 15 10,000; 17 **76.00** (without 4b: 380.00); 8995: 11 194,250 ≤ 197,300; 15 **20,000** | i8960 p. 8 Line 4b |
| FK11 | MFJ, W-2 240,000; K-1 1065 limited partner box 1 30,000, 20 Z 30,000 | 28 (h) 30,000; AGI 270,000; 8960 4b 0; 8 30,000; 15 20,000; 17 **760.00**; 8995: 11 = 270,000 − 31,500 = 238,500; 15 **6,000**; Form 8582 not filed | i8582 p. 1 |
| FK12 | Refusals, one each: PTP; box 23 checked; S corp distribution (if D-K1 refuse); loss above basis; not at risk; box 10 gain; 1041 11 A; sale of the interest; line 27 Yes | refused at `k1p.ptp`, `k1p.multi`, `k1s.f7203`, `k1p.basis_short`, `k1p.not_at_risk`, `k1p.box10`, `k1e.rare`, `k1p.disposed`, `sche.line27` | §1.3 |

**Mutation pins to expect [I]** (`engine/src/mutate.ts` kinds, per the Part I design): column routing `choose`
guards at box 1 = 0 (add a zero-box-1 K-1 with box 4a only); `b2_part4` filter removal survives unless FK3/FK3b are
both present (they are); `active ∧ tenth` operand drops survive without a general partner with `tenth` = false
(add one); `prorate` part/whole swaps in `k1p.qbi` (FK4 has part ≠ whole; add a case with two loss activities);
`qbi_se` whole replaced by part survives with one SE source (add Schedule C + K-1 14 A); `f8960.line4b` sign
(FK10); `sd.line5` (no fixture has a K-1 ST amount except FK8: add a 1065 box 8 loss with Schedule D line 21 cap).

**External engines [V: read `.engines/ustaxes-src/src`].** UsTaxes Y2025 has `ScheduleK1Form1065` (core/data
index.ts l. 512): box 1, 4a, 4b, 5, 14 A/B/C, 19 A, 199A QBI, an `isPassive` flag; `ScheduleE.ts` places box 1 in
(g)/(h)/(i)/(k) **with no Form 8582 limit on K-1 losses** (l. 166–245); `ScheduleSE.ts` adds 14 A; `ScheduleB.ts`
lists K-1 interest; `F8995.ts` lists K-1s with positive QBI only. **The adapter passes `scheduleK1Form1065s: []`
(`tools/engines/ustaxes_adapter.py` l. 150)**: a mapping is needed. Usable differentially for FK1-like (as a 1065),
FK2, FK11 and income-only passive cases; it will disagree by design on FK3–FK6 and anything 1120-S-specific or
1041. OpenTaxSolver takes Schedule 1 line 5 as an input: integration check only.

---

## 6. 2026

| Change | Evidence | Operation in `changes/2026/` |
|---|---|---|
| Form 8995 threshold $201,750 / $201,775 MFS / $403,500 MFJ | f8995 2026 draft; i1120ssk 2026 17 V [V] | already in `changes/2026/f8995.yaml`; K-1 help texts quoting $197,300 need `relabel` |
| **Minimum deduction for active QBI**: active = trades or businesses in which the filer materially participated | `changes/2026/f8995.yaml` `f8995.min_qualifies` (line 2: "every Schedule C business") [V] | `replace_expr f8995.min_qualifies` to add K-1 QBI where `k1p/k1s.material` (passive K-1 QBI excluded) — new person helper `person.k1_qbi_active` added by an `add_line` in `person` ops |
| Form 8582 MAGI less deductible SE tax | i8582 2026 draft (Part I design) | the Part I design's op; partners' 14 A flows into `s1.line15`, so nothing K-1-specific |
| 1041 K-1 page 2 line reference beside 28% rate gain | f1041sk1 2026 diff [V, meaning not read] | `recite` on `k1e.box4b` once the 2026 Schedule D instructions are read |
| i1065sk1 2026 | not archived | archive; then diff codes (box 20 list) and 199A threshold text |
| Suspended QBI tracking (FK4's −7,000) | i8995 p. 3 | none: R-K22 refuses its release in 2026 |

---

## 7. Lane split (worktrees; claims via `tools/claims.py`; protocol §8)

Precondition: x1-sche's batch merged, or at least its f8582/sche line-id contract and the §3.6 helper split agreed.
The K-1 lanes then run as the **second batch of the same round**, so `sche` and `f8582` get one review each.

| Lane | Model / class | Owns | Depends on |
|---|---|---|---|
| S0 Sources | Sonnet / mechanical | archive f7203, i7203 (D-K1), f461/i461, p541; i1065sk1 2026 when posted | — |
| K1 Partnership | Opus / judgment | `forms/2025/k1p.yaml` | §3.6 contract |
| K2 S corporation | Opus / judgment | `forms/2025/k1s.yaml` (+ `f7203.yaml` if D-K1 = encode, or a separate lane K2b) | S0 for f7203 |
| K3 Estates and trusts | Opus / judgment (small; Sonnet could do the portfolio boxes) | `forms/2025/k1e.yaml` | — |
| K4 Return integration | Opus / judgment | `sche.yaml` (Part II/III lines, 41), `f8582.yaml` (sum operands), `person.yaml` helpers, `s1.yaml` (EBL), `eic.yaml`, `f8960.yaml`, `qbi.yaml`, `f8995.yaml`, `sc.yaml` (`qbi_se_pos` whole), `s8812.yaml` | K1–K3 line ids |
| K5 Investment flows | Sonnet / mechanical | `sb.yaml`, `f1040.yaml` (2a, 3a, 25c, 26), `sd.yaml`, `g28.yaml`, `u1250.yaml` | K1–K3 line ids |
| K6 Interview | Opus (wording) + Sonnet (fixtures, bookkeeping) | `scope.yaml` (k1 leaves schedule1; `scope.passive`; `person.se_screen` stays in K4), bank 264/266, coverage rows, personas, fixtures `k1*.json` | K1–K5 |

K4 is large (11 shared files); split it if context is short: K4a (`sche`, `f8582`, `s1`, `eic`) and K4b (`person`,
`sc`, `qbi`, `f8995`, `f8960`, `s8812`). `person.yaml` and `f1040.yaml` are shared forms (protocol 8.1): one lane each
per batch. The `inputs` claim serializes K1/K2/K3/K6 commits (protocol 8.1 [R]).

**Reviews (one per form per round) [E]:** new k1p, k1s, k1e (+ f7203) → transcription + render + class M = 9 (12);
changed sche, f8582 (counted once with x1-sche if same round), person, sb, f1040, sd, g28, u1250, f8960, qbi, f8995,
sc, s8812, s1, eic, scope → line-scoped transcription + render ≈ 30; class M for f8960, f8995, person, sche ≈ 4.
**≈ 43–46 calls** (≈ 34 if `sche`/`f8582` reviews are shared with x1-sche's round). Several need `--approve-cost`.

---

## 8. Decisions for the owner (recommended first) and risks

- **D-K1 S corporation basis (Form 7203).** Archive f7203/i7203 and encode Parts I (stock basis) and III (loss
  limitation), refusing Part II (debt basis: loans from the shareholder). Alternative: refuse any S corporation K-1
  with a loss or distribution (cheap; keeps most S corporation filers refused [I]).
- **D-K2 Partnership basis.** Ask the filer whether the loss exceeds basis (refuse Yes). Alternatives: encode the
  Partner's Basis Worksheet (i1065sk1 pp. 3–7, needs prior-year basis); refuse all partnership losses.
- **D-K3 At-risk.** Ask on any loss; refuse Form 6198 cases (Form 6198 is archived; encoding is a later lane).
- **D-K4 PTPs.** Refuse in v1. Alternative: income-only PTP with no prior losses (net gain nonpassive, column (k),
  Form 8995 line 6) — common among retail investors, but the sale case (751, Form 8949 basis) usually follows.
- **D-K5 Material participation.** Layered questions for tests 1, 2/3 and 5; refusing tick for tests 4, 6, 7.
  Alternative: one question with all seven tests in help (fails N10).
- **D-K6 Box allow-list** as §1.2/§1.3. Candidates to add later: 13 A (cash charity → Schedule A), royalties (7/6),
  21 foreign taxes into `ftc` (K-1 counts as a payee statement [I, not checked]).
- **D-K7 QBI with a partly suspended loss.** Compute by `prorate` (amb 3); refuse when a prior-year loss is released.
- **D-K8 Partner SE attribution for QBI.** Extend `sc.qbi_se_pos`'s whole to include positive 14 A (amb 4).
- **D-K9 Estates and trusts.** Income only; boxes 6–8 passive by default; refuse 9, 10, 11 (incl. 11 A) and losses.
  Alternative: add `s1.line24k` for 11 A (final-year estates are the commonest 1041 K-1 [I]).
- **D-K10 Guaranteed payments for capital (4b).** Refuse (NII treatment unarchived). Alternative: column (k) and NII.
- **D-K11 Placement.** `$k1p`/`$k1s` at 264, `$k1e` at 266.
- **D-K12 Coverage end changes** for the rows of §4 (N9).
- **D-K13 Schedule E presence.** A portfolio-only K-1 does not file Schedule E (amb 7), so it does not trip the EIC
  refusal; any Part II/III amount does.
- **D-K14 Foreign items.** Refuse foreign partnerships, K-3 foreign tax and box 21.
- **D-K15 Timing.** Second batch of x1-sche's round (one review of `sche` and `f8582`).
- **D-K16 Activity rows.** Suffix lines now; def refactor later (§3.1).

**Risks.**
- Basis is asked, not computed (D-K2): a filer who answers "No" wrongly gets an unlimited loss; the guard is help only.
- S corporation coverage depends almost wholly on D-K1; without it the share estimate halves.
- Many fund K-1s carry statements (multiple activities, 20 Z by activity, K-3): they refuse, and no count exists.
- The material-participation answer decides passive vs nonpassive, NIIT line 4b, and (2026) the active-QBI minimum.
- `person.yaml`, `f1040.yaml`, `sche.yaml`, `f8582.yaml` are touched by both this area and x1-sche: the helper split
  of §3.6 must be agreed before either lane commits, or K4 restates x1-sche's lines.
- UsTaxes gives no Form 8582 differential for K-1 losses; FK3–FK6 rest on hand prediction and the i8582 arithmetic.
- `i1040se` p. 8 says "Part III, column (e)" for the S corporation basis box; the form puts it in Part II line 28 (e)
  (erratum, [T] verification "Confirmed").

**Verified vs inferred.** Verified this session: every page cited [V] above was read in `sources/2025` or
`sources/2026`; line ids and current expressions in §3.7 were read in `forms/2025`; free orders 262/264/266; UsTaxes
files and adapter line. Inferred: the share estimates, the def-in-collection question, the frequency guesses, the
2026 1041 line-reference meaning, the NII treatment of 4b, the K-1-as-payee-statement for the foreign tax election,
and that no `scope.schedule1` refusal other than `s8812.eiw_3` and `s1a.line5_calc` concerns K-1s specifically.
