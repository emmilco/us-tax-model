# Design scout: other Schedule 1 income and adjustments (TY2025, federal)

Model: claude-opus-5-5 · Class: judgment · Year: 2025 · Jurisdiction: us · Read-only scout; tree read:
`.claude/worktrees/sweep-tasks`. Evidence marks: **[V]** read in the tree or an archived source this session;
**[T]** testimony (a doc or another scout's file, not re-checked); **[I]** inferred, unverified.

---

## 0. Ranking and the finding that changes what "+4.2" means

### 0.1 What the estimate actually measures [V]

`reports/2025/filer_coverage.md` gives the group "Other Schedule 1 income and adjustments" +4.2 alone. It is made
of four `tools/coverage/categories.json` categories:

| Category | Share | IRS count | Gate in categories.json | Gate that actually refuses it in the forms |
|---|---|---|---|---|
| `other_income` (SOI 23in14ar cols 91+93, "Other income" net income + net loss) | 4.8% | 7,787,273 | `scope.schedule1` | `s1.line8_other` (8e, 8k, 8m, 8t, 8u, 8v), `oi8z.recovery/additional_tax/figured`, `scope.recovery` |
| `form4797` (cols 41+43) | 1.1% | 1,720,509 | `scope.schedule1` | **`sd.other_forms`** (via `sd.business_property`, `sd.condemned`, `sd.small_business_stock`, `sd.trader_election`) |
| `nol` (col 95) | 0.6% | 1,019,019 | `scope.schedule1` | `scope.nol` (inside `scope.schedule1`) |
| `foreign_earned_income` (col 89) | 0.3% | 432,724 | `sa.excluded_income` | `sa.excluded_income` (29 refusal sites across eic, f2441, f8863, f8880, f8962, s8812, s1a, sa, ira, ssb) |

Three consequences, all [V] from the files above:

1. **The 4.8% cannot be retired by encoding alone.** The category note says the IRS count "does not say which lines
   it holds, so the category stays refused". SOI's "Other income" mixes lines already computed (8g Alaska dividends,
   8h jury pay, 8i prizes, 8j hobby, 8r scholarships, the 8z RTAA and kickbacks kinds) with those still refused. The
   archived SOI tables give no breakdown: I searched every `sources/2025/soi-*.xls` for Schedule 1 line names and
   found none. Table 1.7's footnote lists only categories. **Whatever this area encodes, the estimate will not move
   unless the category is split by Schedule 1 line.** Source to archive: SOI *Individual Income Tax Returns Line Item
   Estimates* (Publication 4801), latest year. It gives return counts for each Schedule 1 line, 8a to 8z [I: from
   memory, not archived]. Also archive the Pub. 1304 "Explanation of terms" section, which defines SOI's "Other
   income" [I].
2. **`form4797` is mapped to the wrong gate.** `scope.schedule1`'s `any:` list (scope.yaml l.969–1035) contains no
   Form 4797 input; Form 4797 is refused by `sd.other_forms` (sd.yaml l.213–259). The estimate's figures come out the
   same today, because the estimate does not use gates to compute. But the protocol's 1.2/3.4 bookkeeping keys on
   them, so the integrator should correct the mapping. `tools/coverage/tree.json` l.44 still words the
   `scope.schedule1` question as covering Form 4797, which is stale.
3. **The `form4797`, `nol` and `foreign_earned_income` shares are "IRS count only (independence assumed)".**
   Filers with Form 4797 or an NOL are mostly Schedule C/E/F and K-1 filers. The estimate treats them as independent,
   so it overstates what covering them *alone* gains. The slices designed below (Schedule C property only; NOL only
   where the 80% limit cannot bind) serve fewer filers than the headline shares [I].

### 0.2 Sub-items ranked (share × cost)

| Rank | Sub-item | Measured share | Realistic slice served | Encoding cost | Verdict |
|---|---|---|---|---|---|
| 0 | Split the estimate's `other_income` category by line (Pub. 4801); fix the `form4797` gate | — | makes the gains below countable | XS (integrator + source lane) | **do first** |
| 1 | Line 8z recoveries of 2024 itemized deductions (Pub. 525 Worksheet 2), plus named fully taxable 8z kinds | part of 4.8% | unmeasured until rank 0 | S–M | **design below** |
| 2 | NOL deduction (8a), only where the 80% limit provably cannot bind | 0.6% | below 0.6% [I] | S | **design below** |
| 3 | Form 8853 Section C, long-term care per diem (8e) | part of 4.8% | unmeasured | M | **design below** |
| 4 | 8u inmate wages, 8k stock option income not on W-2 (amount lines) | part of 4.8% | tiny | XS | fold into the s1 lane |
| 5 | Form 4797 for Schedule C personal property (equipment, then vehicles) | 1.1% | a fraction [I] | L | design below; later batch |
| 6 | 8z taxable Coverdell/529 distributions (Pub. 970 earnings ratio, Form 5329 Part II, Form 8863 coordination) | part of 4.8% | unmeasured | M–L | sketch only; later |
| 7 | 8z insurance dividends (refuse at f8960 line 7 only when Form 8960 applies) | small | small | S | owner reopens amb.2025.line8z_kinds |
| — | 8t NQDC pension (W-2 box 11) | — | — | — | stays refused (ambiguity; §8 D6) |
| — | 8m Olympic, 8n/8o/8p, 8q ABLE, 8s Medicaid waiver | — | — | — | stay refused |
| — | Form 2555 (8d, 24j) | 0.3% | — | L (29 refusal sites, Foreign Earned Income Tax Worksheet, housing, day counts, Form 1116 deferred) | **decline this round** (§8 D1) |

Lines to avoid (per launch message): `s1.line8v` and the `s1.line9` sum (lane x1-digital), and `s1.line5`/`s1.line10`
(lane x1-sche; its scout `/tmp/scout-schedule-e.md` turns `s1.line10` into `sum(s1.line10_ex5, s1.line5)` [T]). This
area's NOL and 8e/8u/8k need `s1.line9`, and Form 4797 needs `s1.line10` (line 4). **So rank 2–4 merge after
x1-digital, and rank 5 after x1-sche** (§7).

---

## 1. Scope

### 1.1 Becomes computed

| Situation | Gate removed or narrowed | Residual refusal kept (new gate, where the refusal sits) |
|---|---|---|
| Recovery of 2024 itemized deductions: property or real estate tax refund, mortgage interest refund (Form 1098 box 4), medical reimbursement, other Schedule A item refunded, with or without a 2024 state income tax refund | `scope.recovery` leaves `scope.schedule1`'s `any:`; `oi8z.recovery` no longer refuses the kind `recovery` | `rec.not_2024` (paid in a year before 2024, Pub. 525 p. 27, "complete a separate worksheet for each year"); `rec.nonitemized` (bad debt or other non-itemized deduction, or a credit, Pub. 525 p. 24 "Tax benefit rule"); `rec.limited` (2024 itemized deductions limited, AMT, unused credits, 0% capital-gain-rate year: Pub. 525 p. 24–25 statements 3, 6, 7 and "Capital gains"). The existing `refund.exc_tax`/`refund.exc_who` screens cover these; they become asked when `refund.has OR rec.any` |
| 8z kinds that are fully taxable as reported, with no other form or additional tax: `fiduciary_fees` (fees as a nonprofessional executor or personal representative), `misc_box3` (Form 1099-MISC box 3 amounts that are not a prize or award and not from a business, such as research-study or focus-group pay), `taxable_damages` (punitive damages, or damages not for a physical injury or sickness), `found_property` | the kind `other` narrows | `other` stays refused (`oi8z.figured`); `taxable_damages` refuses at its own child if any part is for a physical injury or sickness (Pub. 525, Court awards and damages; page to locate, near txt l.3027) |
| NOL carryover deducted on 8a, all from tax years after 2017, none from a section 461(l) excess business loss, where 4·(AGI − deductions) ≥ carryover | `scope.nol` leaves `scope.schedule1`'s `any:` and becomes a parent | `s1.nol_pre2018`, `s1.nol_ebl`, `s1.nol_limit` (the 80% limit may bind), refused at **f1040.line15** (not at s1.line8a: the test reads lines downstream of 8a, so a refusal there would be a cycle [I], and the build's cycle check confirms it) |
| LTC per diem payments and periodic accelerated death benefits (Form 8853 Section C, per insured) | `s1.ltc_payout` leaves `s1.line8_other` | `f8853c.other_payees` (line 15 Yes, "Multiple Payees"); `f8853c.pre1996` (reimbursements from pre-August-1996 contracts); `f8853c.nonqualified` (line 17 caution: a non-qualified contract); Archer/Medicare Advantage MSA stays refused by `scope.archer_msa` |
| Inmate wages (8u), option income not on W-2 (8k) | `s1.inmate_wages`, `s1.stock_options_if_options` leave `s1.line8_other` | — |
| (Later batch) Sale or trade-in of Schedule C personal property (section 1245) | `sd.business_property` narrows | real property / section 1250, rental, farm and K-1 property, partial dispositions, Part IV recapture (business use 50% or less), installment, like-kind, condemnation, casualty (all existing gates), and new `f4797p.mixed_use` (D3 vehicles only) and `eic.f4797_investment` (investment income over $11,950 with Form 4797 needs Pub. 596 Worksheet 1) |

`s1.line8_other` stays as the gate for 8m, 8t, (8v until x1-digital lands) and any line not listed.

### 1.2 Share served

From the estimate: up to 4.8% (`other_income`, unsplittable today), 0.6% (`nol`) and 1.1% (`form4797`), with
independence assumed. The slices above are smaller by unmeasured amounts. **Mark every gain as an estimate until the
source of rank 0 is archived and the category is split.**

---

## 2. Sources

| Document | 2025 | Pages used | 2026 |
|---|---|---|---|
| i1040gi | archived [V] | p. 91 Lines 8a, 8d, 8e, 8k, 8m (PDF p. 91); p. 92 Lines 8p–8z; p. 93 nontaxable income; p. 100 Line 24j | not archived |
| f1040s1 | archived | lines 4, 8a–8z, 9, 10 | draft archived [V] (lines unchanged; full sub-line numbering; scout-digital [T]) |
| p525 | archived [V] | p. 24 Recoveries, Tax benefit rule, Itemized Deduction Recoveries statements 1–6; p. 25 statements 7–9, Total recovery included in income, Examples 30–32, Allocating the included part (Ex. 31); p. 26 Negative taxable income (Ex. 33), Recovery limited to deduction (Ex. 34), Worksheet 2a; p. 27 Worksheet 2; Miscellaneous Income (fees, damages, found property; pages to locate) | not archived |
| f8853 / i8853 | archived | f8853 p. 2 Section C lines 14–26 ($420 printed on line 21 [V]); i8853 Filing Requirements for Section C, Multiple Payees, LTC period, line 22 | not archived; **rp-25-32 [V]: 2026 per diem $430** (l.1514–1520) |
| rp-2024-40 | archived | per diem $420 (l.1084–1092 [V]); FEIE $130,000 (l.749–751 [V]) | rp-25-32: FEIE $132,900 [V] |
| **Form 172, i172 (2025)** | **to archive** | i1040gi p. 91 Line 8a: "See the Instructions for Form 172 for details" [V]; the 80% limit, the pre-2018 rule and carryover ordering live there [I] | to archive when posted |
| **26 U.S.C. 172** | **to archive** | §172(a)(2) 80% limitation [I] | same text |
| i6251 | archived | p. 1 Who Must File, statement 4 (lines 2c–3 negative), Line 2f ATNOLD [V] | — |
| i8995 | archived | QBI includes a section 1231 gain or loss "only ... if it isn't capital gain or loss" [V, txt l.171]; previously disallowed losses | — |
| f4797 / i4797 | archived [V] | f4797 lines 1a–18b, 19–32; i4797 p. 6 Part I and Line 8; p. 8 Line 10; p. 9 Lines 20, 22; p. 10 Line 25 (PDF pages) | not archived |
| p946 | archived | PDF p. 39/41, disposal-year depreciation (half-year: half; mid-quarter: 12.5/37.5/62.5/87.5%) [V] | not archived |
| p463 | archived | Disposition of a Car; depreciation per mile, 2025 0.33, 2024 0.30 and earlier rows [V] | **n-26-10 [V]: 35¢ for 2026**, and confirms 26/28/30/33¢ for 2022–2025 |
| **p596** | **to archive** | Worksheet 1, EIC investment income with Form 4797 (eic.yaml l.630–638 [V] refers to it) | — |
| **p544** | to archive (optional) | §1231 and §1245 background i4797 cites | — |
| f2555 / i2555 | archived | only if D1 is reversed | — |
| SOI Pub. 4801 line item estimates; Pub. 1304 Explanation of Terms | **to archive** | rank 0 | — |

---

## 3. Encoding plan

### 3.1 New form `rec`: Pub. 525 Worksheets 2a and 2, singleton, for 2024 recoveries [V text, p. 26–27]

| id | printed | type | expression sketch | cite |
|---|---|---|---|---|
| `rec.any` | (gate) | Bool | input; becomes the parent (the old `scope.recovery` id is kept as a derived copy, construction protocol 3.1) | p525 p. 24 Recoveries |
| `rec.property_tax` | (helper) | NonNegDollars | input, gated: 2024 real estate and personal property taxes refunded in 2025 | p525 p. 26 Worksheet 2a line 2 |
| `rec.mortgage` | (helper) | NonNegDollars | input, gated: mortgage interest refunded (Form 1098 box 4) | p525 p. 24 Mortgage interest refund |
| `rec.medical`, `rec.medical_deducted` | (helper) | NonNegDollars | inputs; the second is the 2024 Schedule A line 4 | p525 p. 26 Ex. 34 ("only ... $200, the amount actually deducted") |
| `rec.other_item`, `rec.other_deducted` | (helper) | NonNegDollars | inputs | p525 p. 27 footnote 2 |
| `rec.w2a_line1` … `rec.w2a_line8` | 2a:1–8 | NonNegDollars | line 1 = `refund.received_if_worksheet` capped as today; line 2 = `rec.property_tax`; line 3 = `smaller_of(1+2, refund.line5d_prior_year)`; line 4 = `choose(5d > 5e → 5d − 5e; else line 3)`; line 5 = `subtract_floor0(3, 4)` when 3 > 4; line 6 = 1 + 2; line 7 = `choose(line5 blank → line1; else line1 ÷ line6 × line5)`; line 8 likewise for line 2 | p525 p. 26 Worksheet 2a |
| `rec.line1a` | 1a | NonNegDollars | `rec.w2a_line7` (footnote 1 cap by `refund.sales` existing) | p. 27 |
| `rec.line1b` | 1b | NonNegDollars | `rec.w2a_line8` | p. 27 |
| `rec.line2` | 2 | NonNegDollars | sum(`smaller_of(mortgage, …)`, `smaller_of(medical, medical_deducted)`, `smaller_of(other_item, other_deducted)`) | p. 27 line 2 and fn 2 |
| `rec.line3` | 3 | NonNegDollars | 1a + 1b + 2 | p. 27 |
| `rec.line4` | 4 | NonNegDollars | copy `refund.line17_prior_year` (asked once; its gate widens to `refund.has OR rec.any`) | p. 27 |
| `rec.line5` | 5 | NonNegDollars | input, default 0 ("previously refunded") | p. 27 |
| `rec.line6` | 6 | NonNegDollars | `subtract_floor0(4, 5)` | p. 27 |
| `rec.line7` | 7 | NonNegDollars | copy `refund.line7` (2024 standard deduction with boxes, already encoded) | p. 27, fn 3 |
| `rec.line8` | 8 | NonNegDollars | `subtract_floor0(6, 7)` ("If ... zero or less, stop here") | p. 27 |
| `rec.line9` | 9 | NonNegDollars | `smaller_of(3, 8)` | p. 27 |
| `rec.line10` | 10 | Dollars | `subtract(rec.agi_prior, rec.deductions_prior)`: 2024 Form 1040 line 11 minus line 14, signed (fn 4 and p. 26 "the sum of lines 12 and 13 ... more than line 11") | p. 26–27 |
| `rec.line11` | 11 | NonNegDollars | `choose(line10 ≥ 0 → line9; else floor0(line9 + line10))` | p. 27 line 11 |
| `rec.to_line1` | B | NonNegDollars | `choose(line11 = line3 → 1a; 1b+2 = 0 → line11; 1a = 0 → 0; else line11 × 1a ÷ line3)` | p. 27 lines A–B |
| `rec.to_line8z` | C | NonNegDollars | `line11 − rec.to_line1` | p. 27 line C |
| `rec.used` | (gate) | Bool | `rec.any` and line 3 > 0 | p. 24 statement 2 ("a refund other than an income tax refund") |

Changes in existing forms:
- `refund.taxable` becomes `choose(rec.used → rec.to_line1; else today's worksheet)`. `s1.line1` is unchanged
  (it reads `refund.taxable` [V] s1.yaml l.20–40).
- `s1.line8z` becomes `sum(sum_over oi8z taxable, rec.to_line8z)` (s1 owner lane). The `oi8z` kind `recovery` is
  removed from the enum: one fact, one asker (N8). A filer who picks it is routed to the `rec` questions.
- `f8960`: the existing `f8960.refund` gate (the Deduction Recoveries Worksheet) must also fire on `rec.used` when
  Form 8960 is filed. The lane reads its predicate.
- Parameters: none new (2024 standard deductions are already `refund.std_*` [V] params l.1710).
- Ambiguities: `amb.2025.rec_ratio_rounding` (line A's percentage precision is not stated; reading: exact rational,
  then round B to cents); `amb.2025.rec_prior_taxable` (line 10 as line 11 − line 14 of 2024).

### 3.2 `oi8z` kinds (enum `other_income_kind`)

Add `fiduciary_fees`, `misc_box3`, `taxable_damages`, `found_property` (computed, `taxable = amount`). Remove
`recovery` (now `rec`). Keep the refused kinds. Add one child gate `oi8z.injury` (taxable_damages only; any part for a
physical injury or sickness → refuse). Update `amb.2025.line8z_kinds` (`set_ambiguity`): this is owner decision D4's
list, so it goes to the owner (§8 D2). NII: none of the new kinds is NII [I, p. i8960 line 7 to check]. If the owner
wants a guard, a refusal at `f8960.line7` when Form 8960 applies and such a kind is present avoids the cycle that
amb.2025.line8z_kinds describes.

### 3.3 NOL: lines in `s1` (s1 owner lane)

| id | printed | type | sketch | cite |
|---|---|---|---|---|
| `scope.nol` | (gate) | Bool | stays the input (tick in `before_2025`); removed from `scope.schedule1`'s `any:` | i1040gi p. 91 Line 8a |
| `s1.nol_amount` | (helper) | NonNegDollars | input `gated_by: s1.nol_amount_if_nol` | i1040gi p. 91 Line 8a; i172 (to archive) |
| `s1.nol_pre2018`, `s1.nol_ebl` | (gate) | Bool | inputs under the parent; refuse at `f1040.line15` | i172 [to archive]; i8995 (previously disallowed losses) |
| `s1.line8a` | 8a | Dollars (≤ 0) | `negate(s1.nol_amount_if_nol)` | i1040gi p. 91 "Enter the amount in the preprinted parentheses (as a negative number)" |
| `s1.line9` | 9 | **Dollars** (was NonNegDollars) | add `s1.line8a`, `s1.line8e`, `s1.line8k`, `s1.line8u` to `sum.of` **on top of x1-digital's 8v** | f1040s1 line 9 |
| `s1.ti_signed` | (helper) | Dollars | `subtract(f1040.line11b, f1040.line14)` | f1040 line 15 |
| `s1.nol_limit` | (gate) | Bool | `test: 4 × s1.ti_signed < s1.nol_amount_if_nol`, with 4× written as the sum of four copies if no scale atom exists; refuses at `f1040.line15` | §172(a)(2) [to archive], i172 |

**Why the test is sound (a premise for the ambiguity entry and a proof obligation):** let N be the carryover and
T = TI after deducting N. The limit is 0.8·T₀, where T₀ is taxable income computed without the NOL deduction (and
without the §199A deduction). If every AGI-dependent deduction in scope does not rise as AGI rises, then T₀ ≥ T + N.
In that case N ≤ 4T implies N ≤ 0.8(T + N) ≤ 0.8·T₀, and the limit cannot bind. With only wages and the standard
deduction the test is exact (T₀ = T + N). The AGI-dependent deductions in scope that need the check are the medical
floor, the student loan and IRA phase-outs, the Schedule 1-A phase-outs, the taxable Social Security benefits, and the
QBI deduction (excluded from T₀, which only helps). The one in the wrong direction, the charitable AGI limit, is
refused when it binds (`sa.charity_limited` [V], in the unmeasured gate list). **[I]: the lane checks this against
each form and records it in `amb.2025.s1_nol_limit_test`.** A Lean lemma is optional.

Other interactions: the 2026 carryover is 0 whenever the deduction is computed (shown as a notice). AMT stays on
attestation (`s2.amt_owed`), but i6251 Who Must File statement 4 can require Form 6251 with an NOL (§8 D4). A §1411
NOL is already asked by `f8960.unsupported` [V tree.json l.84]. New York reads federal AGI; the lane runs the NY steps
and reports any NY NOL modification (it changes no NY form).

### 3.4 New collection `f8853c`: Form 8853 Section C, one per insured [V f8853 text]

`f8853c.per_diem` (17, box 1 with "Per diem" checked), `f8853c.qualified` (gate for 18 = 17), `f8853c.adb_periodic`
(19), `f8853c.terminal` (16; when it is the only payment, line 26 = 0), `f8853c.line20` = 18 + 19,
`f8853c.days` (LTC period days), `f8853c.line21` = `param f8853c.per_diem_limit` (42000 cents/day, `moves_with_year`)
× days, `f8853c.line22` costs, `f8853c.line23` = `larger_of(21, 22)`, `f8853c.line24` reimbursements, `f8853c.line25` =
`subtract_floor0(23, 24)`, `f8853c.line26` = `subtract_floor0(20, 25)`. `s1.line8e` = `sum_over f8853c line26`
(Sections A/B are zero while `scope.archer_msa` refuses them). Refusals as in §1.1. Ambiguity `amb.2025.f8853c_days`
(the LTC period when certification starts mid-year). The day count × rate multiply needs the closed atom set's
product-by-count; if it has none, a declared exception.

### 3.5 Line 8u, 8k (s1 owner lane)

`s1.inmate_amount` → `s1.line8u`; `s1.options_amount` → `s1.line8k`, both `choose(parent → amount; else zero)`, in
the jury pay pattern (s1.yaml l.656–702 [T, scout-digital]). EIC: 8u is not on line 1z, so EIC earned income is
unaffected [I]. The lane confirms eic.yaml reads no line 8 item.

### 3.6 Form 4797 for Schedule C personal property (later batch)

New collection `f4797p` (one per property sold), and new singleton `f4797`:
- Each item has: link to its business (`sc` entry), source route: **D1** fully deducted before 2025 (allowable = cost:
  the common case of 100% bonus or §179 in 2018–2022 [I]); **D2** an `asset` roster entry (allowable = prior years
  from the tables + 2025 disposal-year depreciation, Pub. 946 p. 39/41 rules; `asset.ended_this_year` [V] stops
  refusing); **D3** an `scveh` vehicle (standard-mileage depreciation basis reduction, p463 table, 0.33 for 2025).
  Then date acquired/sold (held > 1 year), gross price, expense of sale.
- Lines: line 20–25b per item (§1245 only); gain → line 30/31/32; loss or held ≤ 1 year → line 2 or line 10.
  `f4797.line7` = sum of line 2 losses/gains + line 6; line 8 input (nonrecaptured §1231 losses 2020–2024, i4797 p. 6
  [V]); line 9 = `subtract_floor0(7, 8)`; line 11/12/13/17/18b; `sd.line11` = gain to Schedule D (today it copies
  zero [V] sd.yaml l.1491); new `s1.line4` = 18b; **`s1.line10` adds line 4** (collides with x1-sche).
- Interactions [V where noted]: `f8960.line5a` copies only `f1040.line7a` today [V]. It must add `s1.line4`, and
  `f8960.line5b` (typed NonNegDollars and zero today [V]) must carry the nonpassive-trade exclusion, so it becomes
  Dollars. `qbi`: the ordinary part (lines 13, 11 and 12) enters the business's QBI, and the capital part does not (i8995 [V]).
  `eic`: new residual `eic.f4797_investment`. `sc`/`f4562`: disposal-year depreciation on line 17. `u1250`: unchanged
  (real property stays refused).

---

## 4. Interview plan (construction protocol §§1–3, 7)

| Input | Order/seq | Parent / group | Prompt (draft) | Help (≤40 words) |
|---|---|---|---|---|
| `rec.any` (keeps `scope.recovery` as a derived copy) | 161/6, `money_b` | tick | "Money back in 2025 for something on your 2024 itemized deductions" | "Such as a property tax refund, mortgage interest refunded (Form 1098 box 4), or a medical bill insurance paid back. A state income tax refund is asked separately. If you took the standard deduction for 2024, answer No." |
| `refund.itemized` (existing, gate widened) | 161/30 | child of `rec.any` | as today | as today |
| `rec.property_tax`, `rec.mortgage`, `rec.medical`(+`_deducted`), `rec.other_item`(+`_deducted`) | 161/31–36 | children | "How much of your 2024 property tax was refunded in 2025?" … | where on the paper; "Give 0 if none" |
| `rec.not_2024`, `rec.nonitemized` | 161/37–38 | tick group `rec_rare` (new, ≤2 boxes) | "Any of it for something paid before 2024" / "Any of it for a deduction you took without itemizing, or a credit" | "A Yes ends the interview here." |
| `rec.agi_prior`, `rec.deductions_prior` | 161/39–40 | children, asked only when `rec.line8 > 0` | "On your 2024 Form 1040, what is line 11?" / "… line 14?" | — (a box of a paper the filer is holding is allowed, N6) |
| `oi8z.kind` labels | 294/2 | existing | add 4 labels; drop `recovery` | update "Only the first two kinds" help |
| `oi8z.injury` | 294/4 | child of kind `taxable_damages` | "Was any of it paid for a physical injury or physical sickness?" | "A Yes ends the interview here." |
| `scope.nol` (tick unchanged; help loses "A Yes ends the interview") | 258/2 `before_2025` | — | — | "A loss bigger than that year's income, carried forward on an earlier return." |
| `s1.nol_amount` | 258/10 | child | "How much of that loss is still unused and carried into 2025?" | "Your records from the year of the loss, or Form 172, show it." |
| `s1.nol_pre2018`, `s1.nol_ebl` | 258/11–12 | children | "Did any of it come from a year before 2018?" / "Did any of it come from a business loss over the yearly limit (Form 461)?" | "A Yes ends the interview here." |
| `s1.ltc_payout` (tick stays) | 161/3 | parent | — | drop "A Yes ends…" |
| `$f8853c` roster and items | 161/50–58 | frame "For this person whose care was paid for —" | box 3 kind, box 1, box 4 qualified, box 5 terminally ill, days, costs, other payees | 1099-LTC box names |
| `s1.inmate_amount`, `s1.options_amount` | 161/41, 146/14 | children of existing questions | "How much were you paid for it?" | — |
| (later) `f4797p` per item | 274/26 children of `sd.business_property`; per `asset`/`scveh` "Did you sell or trade this in 2025?" | — | — | — |

Notes required by the protocol: the cost/share table [judgment until the owner rates it]. `rec.any` is answered No by
about 99% [I], and its children cost about 6 short questions, so the parent pays (g < q·C). Who could answer No
wrongly at `rec.any`? Someone whose 2024 medical bill was reimbursed by insurance, so the tick names it.

Coverage rows: `interview/2025/coverage/other.yaml` (or a new `recoveries.yaml` owned by lane A). One row per
situation: Ex. 30 proceeds, the earlier-year refusal, the non-itemized refusal, NOL computed, NOL pre-2018 refused,
NOL limit refused, the 8853 per-diem computed, 8853 with other payees refused, damages for an injury refused. The
existing rows that expect `refused: scope.schedule1` with `scope.nol: true`, or `s1.line8_other` with `ltc_payout`,
change their end. **That is an expected-end change the lane may not make itself (protocol 8.4). It is listed for the
owner as part of the scope change.**

Personas (numbers from the plan's range): "retiree who itemized 2024 and got a property-tax refund" (typical),
"wage earner with nothing in this area" (nothing), "small-business owner with an old loss carried in" (NOL computed),
"caregiver's parent with a per-diem LTC policy" (8853), "refused: loss from 2016".

---

## 5. Fixtures (hand-predicted; the arithmetic is from the sources)

2025 standard deduction single $15,750 (params l.1616 [V]). Class A where the source prints the result.

| # | Inputs (non-default) | Expected | Arithmetic / class |
|---|---|---|---|
| F1 | MFJ; 2024 itemized 30,700, std 29,200, TI 60,000; state refund 400 (5d = 5e, so no SALT cap); medical reimb. 200 (deducted ≥200); mortgage refund 325 | `rec.line3` 925, `line8` 1,500, `line11` 925; **s1.line1 400, s1.line8z 525** | 30,700 − 29,200 = 1,500; min(925, 1,500) = 925 = line 3. **Class A, Pub. 525 Ex. 30** |
| F2 | MFJ; 2024 itemized 29,450, std 29,200, TI 45,000; other recoveries 2,100 | `line8` 250, **s1.line8z 250**, s1.line1 0 | min(2,100, 250). **Class A, Ex. 32** |
| F3 | F2 with 2024 line 11 − line 14 = −200 | **s1.line8z 50** | 250 + (−200). **Class A, Ex. 33** |
| F4 | 2024 itemized 30,700, std 29,200, TI 50,000; state refund 500; other recoveries 2,000 | line3 2,500, line11 1,500; **s1.line1 300, s1.line8z 1,200** | A = 500/2,500 = 20%; B = 300; C = 1,200. Results are those of **Ex. 31** (class A); the inputs are constructed (B) |
| F5 | Single; 2024 itemized 14,000 < std 14,600; property tax refund 300 | line8 0; **s1.line8z 0** | 14,000 − 14,600 < 0 → stop (Ex. 29 rule). B |
| F6 | Single; wages 80,000; NOL 20,000 (post-2017) | **s1.line8a −20,000**, AGI 60,000, line 15 44,250 | 60,000 − 15,750; test 4×44,250 = 177,000 ≥ 20,000. Check: T₀ = 64,250, 80% = 51,400 ≥ 20,000. B |
| F7 | Single; wages 40,000; NOL 30,000 | **refused `s1.nol_limit` at f1040.line15** | T = −5,750; true T₀ = 24,250 → limit 19,400 < 30,000 (the limit binds; the refusal is correct). B |
| F8 | Single; wages 65,750; NOL 40,000 (boundary) | computed; line 15 **10,000** | 4×10,000 = 40,000 = N (≤ holds); T₀ = 50,000 × 0.8 = 40,000. **Pins `<` vs `≤`**. B |
| F9 | 8853c: per diem 160,600, qualified, 365 days, costs 120,000, reimb. 0 | line21 153,300; line23 153,300; line25 153,300; **line26 = s1.line8e 7,300** | 420×365; larger_of; 160,600 − 153,300. B |
| F10 | 8853c: per diem 100,000, 365 days, costs 0 | **line26 0** (form shown) | floor at 0. B |
| F11 (later) | Sch C 5-yr equipment, cost 10,000, 2022, bonus elected out, half-year; sold Sept 2025 for 6,000 | dep 2,000+3,200+1,920+576 = 7,696; basis 2,304; gain 3,696 = recapture → **s1.line4 3,696**, sd.line11 0, f4562 line 17 +576 | Pub. 946 Table A-1 (20/32/19.2/11.52%) and half-year disposal rule. B |
| F12 (later) | F11 sold for 12,000; nonrecaptured §1231 losses 500 | gain 9,696; line31 7,696; line32 2,000 = line7; line9 **1,500 → sd.line11**; line12 500; **s1.line4 8,196** | i4797 lines 7–12 [V]. B |

Mutation pins to expect: `rec.line8` floor; `rec.line9` smaller_of (F1 takes line 3, F2 takes line 8);
`rec.line11` negative branch (F3); allocation (F4) vs whole (F1); `s1.nol_limit` comparator (F8);
`f8853c.line23` larger_of (F9 takes 21; add a case with costs > 21); `line26` floor (F10); 4797 `smaller_of` 24/25a
(F11 takes the gain, F12 takes the depreciation); line 9 floor; line 7 sign.

External engines [I, adapter greps only]: OpenTaxSolver takes Schedule 1 lines as entered amounts. The UsTaxes
adapter maps only `otherIncome` IRA and foreign tax inputs. PolicyEngine-US takes `miscellaneous_income` as an input.
Tax-Calculator has a Form 4797 net gain input (`e01200` [I]). **None computes Worksheet 2, Form 8853 Section C, the
NOL limit or Form 4797 recapture.** They can confirm only pass-through of the totals. The lane says so in its note,
and that is the trust gap.

---

## 6. 2026

`changes/2026/` exists, so protocol 7.1 applies. Drafts archived: f1040s1 only (no line change for 4, 8a, 8e, 8z;
[T] scout-digital). Operations:
- `changes/2026/f8853c.yaml`: set param `f8853c.per_diem_limit` 42000 → 43000 (rp-25-32 [V]); line 21 printed
  amount; verified: draft until i8853/f8853 2026 are posted.
- `changes/2026/rec.yaml`: prior year becomes 2025. The cites move to 2025 Schedule A, and the prior-year standard
  deductions become the 2025 amounts (15,750 / 31,500 / 23,625, with the 2025 boxes). **[I]: no `refund.*` operations
  exist in `changes/2026/` yet** (`ls` shows no refund file), so the rec and refund worksheets move together in one
  operation set.
- NOL: no known change (the 80% rule is not in the archived 2026 sources; the i172 2026 edition is awaited).
- Form 4797: awaited (no 2026 f4797/i4797). The mileage depreciation rate for 2026 is 35¢ (n-26-10 [V]), a new table
  row.
- FEIE (only if D1 is reversed): 132,900 (rp-25-32 [V]).

---

## 7. Lane split (no two lanes own one form file)

**Batch 1** (starts after x1-digital merges, because of `s1.line9`):

| Lane | Model / class | Owns | Work (ranked) |
|---|---|---|---|
| A `rec` | Opus / judgment | `rec` (new), `oi8z`, `refund`, interview order 161/30–40 and 294, coverage file `recoveries.yaml` | Worksheet 2a/2; refund switch; new 8z kinds; F1–F5. **Requests** to lane B: `s1.line8z` wiring, `scope.recovery` removal |
| B `s1` | Opus / judgment | `s1`, `scope`, `f1040` (refusal at line 15) | NOL lines and test; 8u/8k; `s1.line9` (+8a, 8e, 8k, 8u, retyped Dollars); `s1.line8z` += `rec.to_line8z`; `s1.line8e` = sum f8853c; `scope.schedule1` narrows; F6–F8 |
| C `f8853c` | Sonnet / mechanical (form transcription from a printed form) | `f8853c` (new), param `f8853c.per_diem_limit`, roster frame | Section C; F9–F10. Wiring through lane B |
| S sources | Sonnet / mechanical | `tools/sources/2025.json`, `sources/` | archive i172, f172, usc-26-172, p596, p544, SOI Pub. 4801 and the Pub. 1304 terms; 2026 editions as posted |

**Batch 2** (after x1-sche merges, because of `s1.line10` and `f8960` 4a/4c): lane D `f4797` (Opus / judgment): `f4797`, `f4797p`,
`sd` (line 11), `asset`, `scveh`, `f4562`, `qbi`, `f8960` (5a/5b), `eic`, plus `s1.line4`/`line10` by request to whoever
owns s1 in that batch. Ranked list: D1 fully deducted items, D2 roster assets, D3 vehicles. Probably two lanes (D-a
f4797/f4797p/sd/s1-request; D-b asset/scveh/f4562/qbi/f8960/eic) with an id contract.

Integrator: `categories.json` (fix the `form4797` gate; split `other_income` once the source exists), `tree.json`
table, retired gates.

Reviews (protocol 6.1), rough count: new forms `rec`, `f8853c` (and later `f4797`, `f4797p`) need transcription,
render and class M: **6 now, +6 later**. Changed arithmetic, line-scoped transcription and class M: `s1`, `refund`,
`oi8z`, `f1040`, `scope` (+ later `sd`, `f8960`, `qbi`, `asset`, `scveh`, `f4562`, `eic`): **about 10 now, +12
later**. Screen reviews for the new gates (about 9) and question reviews for about 20 new questions, one sample each
per milestone. Price with `rerun_all.py --dry-run`; anything above $3.00 needs `--approve-cost`.

---

## 8. Risks and decisions for the owner

- **D1 Form 2555: decline this round** (0.3%; 29 refusal sites, the Foreign Earned Income Tax Worksheet, the housing
  base and caps, physical-presence day counts, and Form 1116, which is deferred by decision). Alternative: wages-only
  exclusion with no housing. It still touches every MAGI add-back.
- **D2** The new 8z kinds amend owner decision D4 (`amb.2025.line8z_kinds`). Approve the list
  (fiduciary_fees, misc_box3, taxable_damages, found_property), and decide whether insurance dividends come in with a
  refusal at `f8960.line7`.
- **D3** The NOL sufficiency test: computing only when 4·T ≥ N is conservative and needs the monotonicity premise
  (§3.3). Accept it, or require Form 172-style T₀ (a shadow chain, cost L).
- **D4** The NOL and AMT: i6251 statement 4 can require Form 6251 when lines 2c–3 (including ATNOLD) are negative. Keep the
  `s2.amt_owed` attestation with a help sentence, or refuse an NOL above some size.
- **D5** Coverage accounting: approve archiving SOI Pub. 4801 and splitting `other_income`. Without it, ranks 1, 3
  and 4 show **0.0** gain in the report however much is built.
- **D6** 8t (W-2 box 11): i1040gi p. 92 says 8t "may be shown in box 11 of Form W-2", while the IRA worksheet note
  (i1040gi, l.8764 of the text) treats box 11 income as included in box 1. Encoding 8t risks double counting, so it
  stays refused pending a reading.
- **D7** Expected-end changes to existing coverage rows (rows that today end in `scope.schedule1` or
  `s1.line8_other` for NOL/LTC/inmate/options). Protocol 8.4 forbids lanes to edit them; the owner authorizes it as
  part of the scope change.
- Risk: Form 4797's "allowed or allowable" computed from tables may differ from what the filer actually claimed
  (`amb.2025.f4797_allowable`). Risk: SALT-cap interaction in Worksheet 2a when the 2024 cap bound. It is handled by
  5d/5e as printed [V], but needs a fixture.
