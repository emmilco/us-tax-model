# Design scout: the tail of the ranking — farm income, pay not on a W-2, other nonrefundable credits (TY2025, federal)

Model claude-opus-5-5, class judgment, year 2025, jurisdiction us. Read-only scout. Base tree read:
`.claude/worktrees/sweep-tasks` at `63a20efc`. No model calls, no agents, no paid reviews, no fetches.
Labels: [V] verified here against the tree or an archived source; [T] testimony (a doc or report, not re-checked);
[I] inferred. Page numbers marked "PDF p." are the form-feed page index of the archived `.txt`; the lane confirms
the printed page before citing.

## 0. Summary and ranking

The stop rule of "about 0.5 points" is not written in the protocol draft (§1 and §8 read; neither defines a threshold);
I applied it as stated in the launch message, to the gain the estimate gives (`reports/2025/filer_coverage.md`, "Gain if
covered alone now") and, where it differs, to the gain a real design can capture.

| Rank | Area | Estimate: share / gain alone / gain in ladder | Gain a design can capture | Cost | Verdict |
|---|---|---|---|---|---|
| 1 | (b) Pay not on a W-2 and other earned income (Form 1040 lines 1b, 1c, 1d, 1g, 1h; Forms 4137, 8919) | 0.8% / +0.6 / +0.8 [V report] | about +0.6 if line 1h's content is what I infer (1.3); 0.3 to 0.6 range [I] | 2 small new forms, ~12 shared forms touched, 2 lanes | **Design (section A).** Best gain over cost. |
| 2 | (a) Farm income, Schedule F | 1.1% / +0.5 / +1.1 [V report] | below +0.5 alone [I]: Form 4797 (livestock and machinery sales), Form 4136, 1099-PATR patrons, crop-share landlords (Form 4835) stay refused and fall on the same filers | 1 large new form + re-parenting depreciation and vehicles, 3 lanes + an architect map | **Design (section B), at the rule's edge.** Recommend running it after Schedule E and the Form 4797 part of "other Schedule 1", where the ladder gives +1.1 and its biggest residual refusal is gone. |
| 3 | (c) Other nonrefundable credits | 0.9% / +0.7 / +0.9 [V report] | ≤ +0.38 [I]: the two largest parts (general business credit 552k, prior-year AMT credit 114k) need Form 3800 and component forms, or Form 6251 | 5 small forms for ~0.4 | **Not designed: does not clear the rule** (section C). |

## 1. Shared findings (all three areas)

1.1 **What the estimate measures.** [V `tools/coverage/categories.json`; SOI cells read with the engines venv]
- `farm`: SOI Table 1.4 col 79 (farm net income, 484,162) + col 81 (net loss, 1,258,869) = 1,743,031; gate
  `scope.schedule1` (a shared catch-all: rental, K-1, farm, NOL and others, `forms/2025/scope.yaml` l.969).
- `wages_not_w2`: max of col 17 "Other earned income" 1,267,621 ($62.9 billion), col 9 household employee wages
  404,554, col 13 taxable dependent care benefits 431,865, col 11 tips not reported 106,786. Col 15 (Form 8919 wages,
  55,403) is not in the catalog. Gate `scope.other_income` (l.1039), also a catch-all (nonresident, chapter 11,
  adoption benefits, care benefits, disaster distributions, passive, reservist repayment, plus `pay_no_w2`,
  `medicaid_waiver`, `excess_deferral`).
- `other_nonrefundable`: Table 3.3 col 18, 1,467,567. Its parts (cols 20–33): general business credit 552,344;
  prior-year minimum tax credit 113,755; adoption 48,062; elderly or disabled 45,136; alternative fuel refueling
  property 104,733; clean vehicle 493,953; mortgage interest credit 86,419.

1.2 **Stale catalog entries** (integrator, protocol 9.3): taxable dependent care benefits (line 1e) are computed
already (`f1040.line1e` from `f2441.line26`) [V], so the `wages_not_w2` label and col 13 cell are stale (the max is
unaffected). `other_nonrefundable` should be split by cols 20–33 so a partial credit round is measurable. The
report is dated before `scope.credits` was removed (protocol 1.1 [T]); refresh before the round.

1.3 **What "other earned income" holds.** [I, the round's main premise to check] For TY2023 the SOI column is most
likely line 1h; Table 1.4 note [1] says adoption benefits (1f) are in total wages "not shown separately", so 1d
(Medicaid waiver) may also sit in col 17 or only in the total. Line 1h is (i1040gi PDF p.24 [V]): strike or lockout
benefits; excess elective deferrals; **disability pensions on Form 1099-R before the employer's minimum retirement
age**; corrective distributions of excess deferrals. At $49,600 average per return the column is dominated by
pension-sized or care-wage-sized amounts, not strike pay or excess deferrals [I]. Therefore the design must cover
the disability-pension route (today refused through `retirement.special` via `retirement.dis_early_if_disability`,
an unmeasured gate [V retirement.yaml l.1144–1190]) and Medicaid waiver payments, or most of the +0.6 is not
captured. No microdata variable was found to split it; state the realized gain as a range.

---

## A. Pay not on a W-2 and other earned income (design)

### A.1 Scope

Becomes computed:
- **Line 1b** household employee wages not on a W-2, per person (amount) [V i1040gi PDF p.24].
- **Line 1c and Form 4137** unreported cash and charge tips, including allocated tips in W-2 box 8 the filer cannot
  show were less; noncash tips go to 1c but not to Form 4137 [V i1040gi p.24 Line 1c; f4137 l.2–13]. Feeds Schedule 2
  line 5, Schedule SE line 8b, Form 8959 line 2, Schedule 1-A line 4b and the tip-employer worksheet column (c).
- **Line 1d and Schedule 1 line 8s** Medicaid waiver payments for care of someone living in the filer's home: in
  W-2 box 1 (then 1a, and subtracted on 8s), or W-2 box 12 code II with box 1 blank, or Form 1099-MISC/NEC with no
  separate care business; the per-person choice to count nontaxable payments as earned income [V i1040gi p.24 Line 1d;
  Schedule 1 line 8s "1a or 1d"]. Feeds EIC Step 5 line 2 and Schedule 8812 Earned Income Worksheet line 4.
- **Line 1g and Form 8919** wages from a firm that treated the person as a contractor, reason codes A, C, G, H
  [V f8919]. Feeds Schedule 2 line 6, Schedule SE line 8c, Form 8959 line 3.
- **Line 1h**: strike or lockout benefits (amount); disability pension before minimum retirement age (the Form
  1099-R taxable amount moves from 5b to 1h). Corrective distributions (code 8) stay refused in this round: the box 7
  enum has no code 8 value, so code 8 falls under "other (any other code, or two codes)" and is refused [V
  retirement.yaml l.27–28]; adding it is a later, optional item.
- Schedule 2 line 7 (= 5 + 6); Form 1040 line 1z sums 1a–1h.

Stays refused (gate, reason):
- Excess elective deferrals (`scope.excess_deferral_if_w2`, narrowed into its own gate): the limit has SIMPLE,
  403(b) 15-year, 457 and catch-up variants, and correction follows next year; low share [I].
- Form 4137 for tips received as a federal, state or local government employee (line 10 instruction) and with
  railroad (RRTA) compensation (`person.rrta`); Form 8919 with RRTA.
- Tips and pay for work in American Samoa, Guam, CNMI, Puerto Rico or USVI (existing territory gates).
- Medicaid waiver payments from a home-care business the filer runs (Schedule C route: allowed only if the existing
  Schedule C screen covers it; else refuse) and payments for care outside the filer's home (they are wages, so 1b
  or 1a, not 1d; help text says so).
- Disability pension from a terrorist attack or military service (`retirement.dis_terror_if_disability`,
  `retirement.dis_military_if_disability`, unchanged); code P corrective distributions (taxable in 2024: amended return).
- Everything else in `scope.other_income` (nonresident, chapter 11, adoption benefits, care benefits not in box 10,
  disaster distributions, passive, reservist repayment).

Gates that go away or narrow:
- `scope.pay_no_w2` dissolves (technique 3.1: keeps its id as a derived line, true only for residual items).
- `scope.medicaid_waiver` dissolves into item lines; the residual refusing items keep gates of their own.
- `scope.other_income` narrows (keeps its id; loses those two members). `eic.step1_resident` and `eic.step5_line2`
  refuse on `scope.other_income` today [V eic.yaml l.580–600, 962–980]; the second is rewired to the new 8s lines.
- `retirement.special` narrows: `retirement.dis_early_if_disability` leaves its any-list.
- `person.se_screen` (a single-input catch-all, order 261) loses "tips reported on Form 4137 or wages on Form 8919";
  its wording changes, so its coverage rows are restated (N9).
- `s1a.line4b_calc` and `tipjob.col_c` refusals (`when: s2.other`, "Form 4137 ... outside this tool") go away.
- `s1.line8_other` loses 8s (`s1.yaml` l.1236 lists 8s among refused lines [V]).
- Schedule 2 `s2.other` screen wording drops "tax on unreported tips (Form 4137)" [V s2.yaml l.305].

Share: the category is 0.79% of returns, +0.6 alone, IRS count only (independence assumed) [V report]. Realized
+0.3 to +0.6 depending on 1.3 [I].

### A.2 Sources

| Doc id | Pages used | 2025 | 2026 edition |
|---|---|---|---|
| i1040gi | PDF p.24 (lines 1b–1i), p.42 (EIC Step 5 line 2), p.92 (Sch 1 line 8s), p.112 (Sch 2 lines 5, 6) | archived [V] | not in `sources/2026` [V]; to archive when posted |
| f1040 | line 1 block | archived | draft archived; lines 1b–1h unchanged [V sources/2026/f1040.txt l.99–110] |
| f4137 | whole form (instructions on page 2) | archived [V] | not archived; to archive |
| f8919 | whole form | archived [V] | not archived; to archive |
| f1040sse / i1040sse | lines 8a–8d; i1040sse "Line 8b", "Line 8c" | archived | draft archived: wage base $184,500 [V] |
| f1040s2 | lines 5, 6, 7 | archived | draft: lines 16a, 16b, 16c [V sources/2026/f1040s2.txt l.117–119] |
| f8959 / i8959 | lines 2, 3 | archived | archived (draft) |
| f1040s1a | line 4b | archived | archived (draft) |
| f1040s1 | line 8s | archived | archived (draft) |
| i1040s8812 | Earned Income Worksheet line 4 | archived | archived |
| iw2w3 | box 8 (allocated tips), box 12 code II | archived | archived |
| Pub 531 (tips), Pub 525 (strike benefits, Medicaid waiver), Notice 2014-7 | rules behind help and the 8s choice | **to archive** | — |
| Pub 575 (disability pensions, minimum retirement age) | 1h route | archived as `p575` [V listing; passage not read] | p575 2026 archived [V listing] |

### A.3 Encoding plan

New forms (collections; each one per person, rows nested, as `asset` nests under `sc`) [I ids; the plan fixes them]:

`forms/2025/f4137.yaml` — collection parent `person` (one per person with unreported tips); child collection
`f4137row` (parent `f4137`), one per employer row A–E:
| id | printed | type | expr sketch | cite |
|---|---|---|---|---|
| f4137row.col_c | 1(c) | NonNegDollars | input | f4137 line 1 (c) |
| f4137row.col_d | 1(d) | NonNegDollars | input | f4137 line 1 (d) |
| f4137row.qualified | (helper) | Bool | input: tips in a listed occupation (feeds 1-A) | f1040s1a line 4b |
| f4137.line2 | 2 | NonNeg | sum_over f4137row.col_c | f4137 l.2 |
| f4137.line3 | 3 | NonNeg | sum_over f4137row.col_d | l.3 |
| f4137.line4 | 4 | NonNeg | subtract_floor0 line2 − line3 | l.4 "Include as income on ... line 1c" |
| f4137.line5 | 5 | NonNeg | input (tips under $20 in a month, not required to report) ≤ line 4 (guard refuses if more) | l.5 |
| f4137.line6 | 6 | NonNeg | line4 − line5 | l.6 |
| f4137.line7 | 7 | NonNeg | param `se.wage_base` (176,100) | l.7 |
| f4137.line8 | 8 | NonNeg | person W-2 boxes 3 + 7 (RRTA refused) | l.8 |
| f4137.line9 | 9 | NonNeg | subtract_floor0 7 − 8 | l.9 |
| f4137.line10 | 10 | NonNeg | smaller_of 6, 9; refuses on government-employee tips | l.10 |
| f4137.line11 | 11 | NonNeg | multiply_rate 10 × 0.062 | l.11 |
| f4137.line12 | 12 | NonNeg | multiply_rate 6 × 0.0145 | l.12 |
| f4137.line13 | 13 | NonNeg | 11 + 12 → Schedule 2 line 5 | l.13 |
Refuses: more than five rows is fine (lines 2–13 are on one form, f4137 p.2 "Line 1"); government employee;
RRTA; territory.

`forms/2025/f8919.yaml` — collection parent `person`; child `f8919firm` (rows 1–5: reason code enum A/C/G/H,
date for A/C, column (f) wages). Lines 6 (sum (f)) → 1g and 8959 line 3; 7 param 176,100; 8 = W-2 boxes 3 + 7 +
`f4137.line10` (form text, f8919 line 8 [V]); 9; 10 smaller of 6 or 9; 11 × 0.062; 12 = line **6** × 0.0145; 13 →
Schedule 2 line 6. Refuses: none of codes A, C, G, H applies (the form says file SS-8 with code G; an "other" choice
refuses), RRTA.

Changed shared forms:
- `se.yaml` (def): new parameters `line1a`, `line1b`, `line8b`, `line8c` (1a/1b for section B; bind zero until then);
  `line8d` = 8a + 8b + 8c; `line3` = 1a + 1b + 2. Callers in `person.yaml` (`person.se_line2/6/12/13/4c`) bind
  `line8b: person.f4137_line10`, `line8c: person.f8919_line10` (person helpers, zero without the form).
- `person.yaml`: inputs `person.household_wages` (1b), `person.strike_benefits` (1h), Medicaid waiver block
  (`person.mw_any`, `person.mw_where` enum {w2_box1, w2_code_ii, form_1099}, `person.mw_amount`,
  `person.mw_earned_choice` Bool), helpers `person.f4137_line10/line6/line4`, `person.f8919_line6/line10`,
  `person.line1h`; `person.se_screen` wording narrowed; per-person earned income (used by Form 2441, IRA
  compensation, saver's credit) gains 1b, 1c, 1d-if-chosen, 1g, 1h [I: lane greps every reader of W-2 box 1 as
  "compensation" or "earned income"].
- `f1040.yaml`: `line1b`, `line1c` (= Σ f4137.line4 + noncash tips), `line1d`, `line1g` (Σ f8919.line6), `line1h`
  (Σ person.line1h incl. disability pension), and `line1z` sums 1a–1h (today 1a + 1e [V]).
- `s1.yaml`: `s1.line8s` (negative: nontaxable Medicaid waiver payments included on 1a or 1d), removed from
  `s1.line8_other`'s refused list; line 9 includes it.
- `s2.yaml`: `s2.line5` (Σ f4137.line13), `s2.line6` (Σ f8919.line13), `s2.line7`; line 21 adds 7.
- `f8959.yaml`: `line2` = Σ f4137.line6, `line3` = Σ f8919.line6 (today copies of zero [V l.63–100]).
- `s1a.yaml` / `tipjob.yaml`: `s1a.line4b_calc` = Σ f4137row.col_c where qualified (row A per the form; more than
  one employer goes through tipjob column (c)); `tipjob.col_c` reads the matching f4137 row (keyed by employer: a
  match rule is a decision, see A.8).
- `eic.yaml`: `eic.step5_line2` = Medicaid waiver payments on 8s not chosen as earned income (today zero + refusal).
- `s8812.yaml`: Earned Income Worksheet line 4, same quantity (today zero + refusal, l.604–613).
- `retirement.yaml`: when `retirement.dis_early_if_disability` the item's taxable amount goes to `person.line1h`,
  not 5b; drop it from `retirement.special`.
- `scope.yaml`: `scope.pay_no_w2`, `scope.medicaid_waiver` become derived lines (3.1); new residual inputs as above.

Parameters: `f4137.ss_rate` 0.062 and `f4137.medicare_rate` 0.0145 (or reuse `se` rates if they are the employee
halves — they are not: se uses 12.4/2.9 [V]); reuse `se.wage_base`.

Ambiguity entries: (1) Medicaid waiver payments in W-2 box 1 *and* box 12 code II (double report): which to trust;
(2) the earned-income choice: ask per person (the form gives the choice) vs. choose the better result — recommend
asking, with help saying it may raise the EIC; (3) allocated tips (box 8) the filer "can prove" were less: take the
filer's figure, no proof modelled; (4) matching f4137 rows to tipjob employers.

### A.4 Interview plan (construction protocol)

Typical filer of the topic: a server with one W-2 who kept some cash tips; filer with nothing: one W-2, no other
pay — answers one tick-box screen ("None of these"), as today.
- Order 146, group `other_pay` (today: `scope.pay_no_w2`, `scope.medicaid_waiver`, `scope.religious_work`, ...).
  Take the `pay_no_w2` tick apart into four ticks (N1), each ≤ 12 words, per person:
  "Pay for work in someone's home, with no W-2" → child amount (1b), help: "$2,800 rule: under it no W-2 is due";
  "Strike or lockout pay from a union" → amount (1h);
  "Pay from a firm that wrongly treated you as a contractor" → `$f8919firm` entries (reason, amount);
  the Medicaid tick stays; its children: where it was shown (W-2 box 1 / only box 12 code II / Form 1099),
  amount, and "Do you want this pay counted as earned income? It can raise some credits." (N10 help ≤ 40 words).
- Unreported tips live with tips (N5): order 150, after `s1a.tips`, per person who has a W-2: "In 2025, did you
  get cash or card tips you did not report in full to your employer?" → `$f4137row` entries in printed order
  (employer, total tips received, tips reported); then line 5 ("tips under $20 in a month at one job"), then noncash
  tips. Who could answer No wrongly: a worker with W-2 box 8 allocated tips — guard with a box-8 check on the W-2
  (if box 8 > 0, the parent is shown with a help line naming box 8).
- Disability pension: no new question; `retirement.dis_early` loses "A Yes ends the interview here."
- Residual refusals told at their topic (N11): excess deferral tick unchanged; government-employee tips as a child of
  the tips parent; RRTA already asked at 140.
- Coverage rows (`interview/2025/coverage/scope.yaml` rows `scope.pay_no_w2`, `scope.medicaid_waiver` change from
  `refused` to `proceeds` — a deliberate change, listed in the lane note, never silent), plus new rows in `jobs.yaml`:
  one per new tick and per residual refusal (~10 rows).
- Personas (next free numbers after the round plan assigns ranges; 14 used): "tipped server with unreported cash
  tips" (typical), "home care provider paid under a Medicaid waiver (code II)", "misclassified worker with Form
  8919", and a refused one "government-employee tips".

### A.5 Fixtures (hand-predicted from the archived forms; cents, half-up products per amb.2025.multiplication_subcent)

All single, under 65, no dependents, standard deduction $15,750 [V params `sa.standard_base`] unless stated.

| # | Inputs | Expected (arithmetic) |
|---|---|---|
| W1 | W-2 box 1 $28,000, box 3 $24,000, box 7 $4,000, box 5 $28,000; one 4137 row: (c) $9,000, (d) $4,000; line 5 $300; no tips deduction | 4137: l2 9,000; l3 4,000; **l4 5,000**; l6 4,700; l8 28,000; l9 148,100; **l10 4,700**; l11 4,700×0.062 = **291.40**; l12 4,700×0.0145 = **68.15**; **l13 359.55**. f1040 1c 5,000; **1z 33,000**; Sch 2 l5 = l7 = 359.55; f8959 l2 4,700 (no tax: l4 32,700 < 200,000) |
| W2 | W1 + the tips are qualified (listed occupation), Schedule 1-A Part II claimed | s1a 4a 4,000 (box 7); **4b 9,000**; 4c larger = 9,000; l7 min(9,000, 25,000) = 9,000; MAGI 33,000 < 150,000 → deduction 9,000; taxable income 33,000 − 15,750 − 9,000 = **8,250** |
| W3 | W-2 box 1, 3, 5 $170,000; one 8919 firm, code H, $10,000 | 8919 l6 **10,000** (→ 1g); l8 170,000; l9 6,100; **l10 6,100**; l11 **378.20**; l12 10,000×0.0145 = **145.00**; **l13 523.20** (Sch 2 l6, l7); 1z 180,000; f8959 l3 10,000, l4 180,000 < 200,000 → 0 |
| W4 | W-2 box 3 $160,000 (box 1 same); 8919 $10,000 code A; Schedule C net $20,000 (no other SE items) | 8919 l8 160,000; l9 16,100; l10 10,000; l11 620.00; l12 145.00; l13 765.00. SE: l2 20,000; l4a 20,000×0.9235 = 18,470.00; l6 18,470; l7 176,100; l8a 160,000; **l8c 10,000**; l8d 170,000; l9 6,100; l10 6,100×0.124 = **756.40**; l11 18,470×0.029 = 535.63; **l12 1,292.03**; l13 646.015 → **646.02** |
| W5 | No W-2; household wages $2,500 (1b) | **1b 2,500**; 1z 2,500; Sch 2 l5/l6 0; `eic.earned_income` **2,500** (>0, positive EIC; the lane reads the table value) |
| W6 | 1099-R box 1 = 2a $18,000, code 3, from an employer plan; `dis_early` Yes; age 45 | **1h 18,000**; 5a/5b from this item **0**; 1z 18,000; `eic.earned_income` **18,000** (vs 0 if routed to 5b); no Form 5329 tax (code 3) |
| W7 | W-2 box 1 $30,000, all qualified Medicaid waiver payments for a parent living with her; choice: not earned income | 1a 30,000; **8s −30,000**; total income 0; `eic.step5_line2` **30,000**; earned income 0 |
| W7b | W7 with the earned-income choice Yes | 8s −30,000; total income 0; `eic.step5_line2` **0**; earned income 30,000 |
| W8 | W-2 $40,000; strike benefits $3,000 | **1h 3,000**; 1z 43,000 |
| W9 | W1 with "tips as a government employee" Yes | refused at `f4137.line10` (gate named in plan) |
| W10 | W3 with person.rrta Yes | refused (RRTA, existing gate) |

Mutation pins to expect: SE `line8d` dropping 8c (W4 line 10 becomes 16,100×0.124 = 1,996.40); 4137 line 12 using
line 4 instead of 6 (W1: 72.50 vs 68.15); 8919 line 12 using line 10 instead of 6 (W3: 88.45 vs 145.00); f8959 line 2
from line 4 instead of 6 (W1 4,700 vs 5,000); 1h vs 5b routing (W6); 8s choice sign (W7/W7b).

External engines: OpenTaxSolver takes 1b, 1c, 1g, 1h and Schedule 2 lines 5, 6 as *inputs* (`taxsolve_US_1040_2025.c`
l.2106–2112, 2690–2691 [V]) — it checks only the flow into 1z, AGI and total tax, not Forms 4137/8919. UsTaxes:
`F4137.ts` computes SS (wage-base capped) and Medicare on unreported tips but has no line 5 (under-$20 tips) and no
RRTA; `F8919.ts` returns line 6 only and `Schedule2.l6` is `undefined` [V]. So W1 (with line 5 = 0) and W3's 1g can be
mapped; 8919 lines 7–13 have no outside check.

### A.6 2026

- Form 1040 2026 draft: lines 1b–1h unchanged [V]. Schedule 2 draft moves lines 5/6/7 to 16a/16b/16c [V] —
  operations in `changes/2026/s2.yaml` (renumber the three new lines; check C-SCHED-10's map, which already restructures
  Schedule 2 [V file head]).
- Wage base $184,500 in the SE draft [V]; Forms 4137 and 8919 2026 not posted/archived → their line 7 takes the same
  parameter, staged, `draft` until the forms post. New files `changes/2026/f4137.yaml`, `f8919.yaml`.
- Schedule 1-A tips deduction continues for 2026 [T OBBBA; lane checks the 2026 draft `f1040s1a` line 4b wording].
- Medicaid waiver and line 8s: check the 2026 Schedule 1 draft line letter (8s) [I unchecked].

### A.7 Lanes (two, one batch)

| Lane | Model / class | Owns (claims) | Work list, ranked |
|---|---|---|---|
| W-tax | Opus / judgment | f4137, f8919 (new), se, person, s2, f8959, s1a, tipjob | 1 Form 4137 + SE 8b + Sch 2 l5; 2 Form 8919 + SE 8c + Sch 2 l6; 3 8959 l2/l3; 4 Schedule 1-A 4b and tipjob (c); 5 person earned income; 6 fixtures W1–W4, W9–W10 |
| W-income | Opus / judgment | f1040, s1, eic, s8812, retirement, scope, interview order 146/150 entries, coverage rows | 1 disability pension → 1h; 2 Medicaid waiver 1d/8s + EIC/8812; 3 1b, strike 1h; 4 scope dissolution + interview + coverage rows; 5 fixtures W5–W8 |
W-income references W-tax's ids (`person.f4137_line4`, `f8919.line6`, `person.household_wages`, ...) fixed in the
plan; person inputs declared by W-tax (it owns person.yaml). Ripple (`defaults.json`) by the integrator.
Reviews (6.1): new f4137, f8919 → transcription, render, class M each (6); changed forms line-scoped: se, person, s2,
f8959, s1a, tipjob, f1040, s1, eic, s8812, retirement, scope → transcription + render (24), class M where a
computation changed (se, s2, f8959, s1a, f1040, s1, eic, s8812, retirement ≈ 9). About 39 review calls; dry-run
estimate before launch.

### A.8 Risks and decisions (owner)

1. The realized gain rests on 1.3 [I]; if col 17 is mostly something else (e.g. 1d not there and 1h dominated by
   excess deferrals), gain could be ~+0.3. Cheap check: none in the archive; accept the range or keep excess
   deferrals in scope too (one more lane item).
2. Medicaid waiver earned-income choice: ask (recommended) or optimise.
3. Allocated tips: trust the filer's figure (no proof modelled).
4. Coverage rows that end in a refusal today will end in `proceeds`: the protocol forbids changing an expected end to
   pass; this is the intended change and must be listed per row in the lane note.
5. `eic.step1_resident` uses `scope.other_income` as a proxy for nonresidence [V]; after narrowing it is still
   correct, but a lane must not repoint it.

---

## B. Farm income, Schedule F (design, conditional)

### B.1 Scope

Computed: Schedule F Parts I and II, **cash method**, one entry per farm per person (i1040sf l.136–137 "you must
file a separate Schedule F" [V text; lane reads the full condition]); Schedule 1 line 6; Schedule SE lines 1a and 1b (CRP payments of a person
receiving Social Security benefits — the tool knows `ssb`); QBI for the farm (Form 8995 path); EIC and Schedule 8812
earned income with farm SE (8812 EIW lines 2c–2e, refused today [V s8812.yaml l.569]); conservation expenses with
the 25%-of-gross-farm-income limit and carryover in [V i1040sf PDF p.6]; crop insurance received and the carried-in
deferred amount (6a–6d), and the election to defer (a yes/no plus amount) [I: cheap; owner may keep it refused];
depreciation (line 14) and car and truck expenses (line 10) through the existing `asset` / `scveh` / Form 4562 model.

Stays refused (gate): accrual method (Part III); not materially participating with a loss (Form 8582); not all at
risk (Form 6198, line 36b); excess business loss (Form 461, existing); CCC loans reported under election (5a);
cooperative distributions (1099-PATR, 3a/3b: the 199A(g) patron reduction is already a QBI refusal [V qbi.yaml
l.122]); prepaid supplies over 50% of other expenses [V p.6]; sales of livestock held for draft, breeding, dairy or
sport, and of machinery (Form 4797, existing refusal); fuel tax credit (Form 4136); farm optional method (Schedule
SE Part II); Schedule J income averaging (`scope.income_averaging_if_business`, unchanged — the return is right
without it, so it may become a non-refusing wish: decision); crop or livestock shares as a landlord (Form 4835,
Schedule E area); farm partnership SE (K-1 box 14 code A).

Gates: `scope.farm` leaves `scope.schedule1`'s any-list and becomes the topic parent (3.1); new residual gates
under `sf.*`; `person.se_screen` loses "farm income (Schedule F) or Conservation Reserve Program payments";
SEP worksheet refusal "self-employment income not on a Schedule C (Schedule F, ...)" [V person.yaml l.1726]
narrows for farm.

Share: 1.1% of returns, +0.5 alone, +1.1 in ladder order, microdata overlap [V report]; realized below +0.5 now [I]
because Form 4797 (1.1% of all returns, IRS-only) and Form 4136 fall heavily on farmers.

### B.2 Sources

| Doc | 2025 | 2026 |
|---|---|---|
| f1040sf (Parts I, II, IV codes) | archived [V] | not archived; to archive |
| i1040sf (PDF p.3 lines B, C, E; p.4 lines 3–6; p.6 lines 12, 14, prepaid; p.9 lines 34, 36) | archived [V] | to archive |
| f1040sse / i1040sse (lines 1a, 1b; PDF p.2–3) | archived | draft archived |
| Pub 225 Farmer's Tax Guide (gross income from farming, conservation, crop insurance deferral, prepaid supplies) | **to archive** | to archive |
| i4562, Pub 946 (farm property 150%/200% DB, Table B-1 class 01.1) | archived [V] | p946 2026 not archived |
| i1040s8812 (EIW lines 2c–2e), i1040gi EIC Worksheet B | archived | archived |
| f8995 / i8995 | archived | archived |

### B.3 Encoding plan

- `forms/2025/sf.yaml`: collection parent `person` (`$sf@person[...]`), printed lines A–G, 1a–1c, 2, 3a/3b (refused
  if > 0), 4a/4b, 5a (refused), 5b/5c, 6a–6d, 7, 8, 9, 10–32f, 33, 34, 36 (a/b; b refuses). About 60 printed lines +
  screens; size like `sc.yaml` minus inventory (≈1,200 lines) [I]. Line 12 = smaller_of(input + carryover in,
  0.25 × gross farm income); line 9 sum per form text; line 34 = 9 − 33.
- **Depreciation and vehicles: the main structural decision.** `asset` and `scveh` have `collection.parent: sc`
  and the schema allows one parent string [V schema `collection.parent` type string]. Options: (i) engine and schema
  allow a list of parents (spec 4.4 change, full tier, Lean too); (ii) a farm is an `sc` entry of kind `farm`
  (no engine change, but every Schedule C line gains a kind guard and printed numbers diverge); (iii) refuse line 10
  actual expenses and line 14 for farms in v1 (kills most of the gain [I]). Recommend (i), decided in the architect
  map (protocol 1.3) before lanes.
- `se.yaml`: `line1a` = Σ sf.line34 for the person; `line1b` = −CRP payments in 4b when the person received SS
  retirement or disability benefits [V f1040sse l.15–18]. `person.yaml` binds them.
- `s1.yaml`: `s1.line6` = Σ over persons and farms of sf.line34.
- `qbi.yaml`, `f8995.yaml`: farm entries as QBI businesses (same as Schedule C: QBI = line 34 less its share of
  the SE deduction).
- `eic.yaml` (Worksheet B), `s8812.yaml` (EIW 2c–2e), `s179.yaml` (business income limit includes farm),
  `carloan.yaml` (Sch 1-A line 22 col (ii) "deducted ... on Schedule F" [V carloan.yaml l.351]).
- Ambiguities: "gross income from farming" for the 25% limit = line 9 with no Form 4797 gains (refused) [I];
  crop insurance deferral eligibility taken from the filer's answer.

### B.4 Interview

Off-ramp: the existing tick `scope.farm` (order 130, group `own_income`) stays the parent; its help drops
"A Yes ends the interview here" and moves crop-share landlords to a child tick that refuses (Form 4835). Topic at
order 253–254 (free [V], between Schedule C lines 252 and vehicles 255): `$sf` entries; principal product (code
from Part IV), method (accrual refuses), material participation (No → asked only with a loss), at-risk (only with a
loss); income in printed order with a tick group "Did this farm get any of these?" (program payments, CCC loans,
crop insurance, cooperative distributions, custom hire, fuel tax refunds); expenses in printed order. Assets and
vehicles at 255/257 reached for farms by option (i). Personas: "grain farmer, cash method" (typical), "hobby-sized
cattle farm with a loss and a W-2", refused "dairy selling culled cows (Form 4797)".

### B.5 Fixtures

| # | Inputs | Expected |
|---|---|---|
| F1 | Single; grain sales (l2) $120,000; ag program payments 4a = 4b $10,000; seeds $15,000, fertilizer $20,000, fuel $8,000, repairs $5,000, insurance $3,000, taxes $2,000, utilities $1,000 | l9 130,000; l33 54,000; **l34 76,000**; SE 4a 76,000×0.9235 = 70,186.00; l10 8,703.06; l11 2,035.39; **l12 10,738.45**; l13 5,369.225 → 5,369.23; **AGI 70,630.77**; QBI 20% × 70,630.77 = 14,126.15; TI-limit 20% × (70,630.77 − 15,750 = 54,880.77) = 10,976.15; QBI deduction **10,976.15**; taxable income **43,904.62** |
| F2 | W-2 $60,000 (box 3 same); cattle sales $20,000; feed $25,000; vet $5,000; materially participates, all at risk | **l34 −10,000**; Sch 1 l6 −10,000; SE l3 negative → SE tax 0; **AGI 50,000**; QBI component 0, loss carryforward −10,000 (Form 8995 l16); TI 34,250 |
| F3 | F1 with conservation spent $40,000 instead of nothing, line 9 $130,000 | limit 32,500; **l12 32,500**; l34 76,000 − 32,500 = 43,500; carryover 7,500 shown |
| F4 | Gross $60,000; conservation $20,000; other expenses $10,000 | limit 15,000; l12 15,000; l33 25,000; **l34 35,000**; SE 4a 32,322.50; l10 4,007.99; l11 937.35; l12 4,945.34; l13 **2,472.67**; AGI 32,527.33 |
| F5 | Retiree with SS benefits; CRP payments 4a = 4b $12,000; expenses $2,000 | l34 10,000; **SE 1b −12,000**; l3 −2,000 → **SE tax 0** (without 1b: 9,235 base, 1,412.96) |
| F6 | Accrual method | refused (Part III) |
| F7 | F2 with "materially participate" No | refused (Form 8582) |
| F8 | F1 + Form 1099-PATR $3,000 | refused (patron) |
Mutation pins: line 12 limit (F3), SE 1b sign (F5), line 34 sign into Schedule 1 (F2).
External engines: UsTaxes `ScheduleSE.l1a` is a TODO returning 0 and there is no Schedule F [V]; OpenTaxSolver
takes Schedule 1 line 6 as an input (`S1_6`) [V]. So only AGI and total tax for a given line 34 can be compared.

### B.6 2026

Schedule F and its instructions for 2026 are not archived; to archive. Known staged changes that touch it: SE wage
base $184,500 [V draft]; bonus depreciation and section 179 already in `changes/2026/asset.yaml` (C-BUS-11, C-BUS-12)
[V README table]. New `changes/2026/sf.yaml` once the draft posts; until then the year_changes check needs an entry
stating "no 2026 document posted".

### B.7 Lanes (after an architect map)

| Lane | Model / class | Owns |
|---|---|---|
| F-map | Opus / judgment, no code | option (i)/(ii) for depreciation parents; topic order; ids |
| F-engine (if (i)) | Opus / judgment | schema, engine collection parents, Lean, `asset`, `scveh` parent lists |
| F-form | Opus / judgment | sf (new), s1, scope, interview 253–254 |
| F-ripple | Opus / judgment | se, person, qbi, f8995, eic, s8812, s179, carloan |
Reviews: sf new (3); changed se, person, s1, qbi, f8995, eic, s8812, s179, carloan, scope, asset, scveh, f4562
(~13 × 2 line-scoped + ~8 class M) ≈ 37.

### B.8 Risks and decisions

1. Run now (+0.5 nominal, less realized) or after Schedule E and Form 4797 (+1.1 in ladder): recommend after.
2. Depreciation parent model (i)/(ii)/(iii).
3. Schedule J: keep refusing, or treat as an optional election the return is right without.
4. Crop insurance deferral election: compute or refuse.

---

## C. Other nonrefundable credits — not designed (does not clear the rule)

Why [V counts §1.1; gains I, at the estimate's independence factor 0.7/0.9 ≈ 0.78]:
- General business credit (552k, ~+0.27) needs Form 3800 and its component forms, mostly from K-1s and businesses
  (Schedule E area refused); Schedule C already refuses it (`sc.business_credit`). Not feasible standalone.
- Prior-year minimum tax credit (114k, ~+0.06) needs Form 8801, whose line 25 needs the current-year tentative
  minimum tax (Form 6251, refused). Belongs with AMT.
- What can be built: clean vehicle (Form 8936 with Schedule A, 494k, ~+0.24), refueling property (Form 8911,
  105k, ~+0.05), mortgage interest credit (Form 8396, 86k, ~+0.04), adoption (Form 8839, 48k, ~+0.02; with line 1f),
  elderly or disabled (Schedule R, 45k, ~+0.02). Together ≈ +0.38, below 0.5, for five forms.
- Form 8936 is effectively one-year: the new and previously-owned vehicle credits end for vehicles acquired after
  September 30, 2025 [T OBBBA; the 2026 Schedule 3 draft still prints 6f and 6m [V], so check i8936 2026 when posted];
  its 2023 count also misses 2025's dealer transfers and the September rush [I], so its true 2025 share is unknown.
- All 2025 documents are archived (f8936, f8936sa, i8936, f8911, i8911, f8396, f8839, i8839, f1040sr = Schedule R,
  i1040sr) [V]; UsTaxes has `F8839.ts` (243 lines), a partial `F8936.ts` and a stub `ScheduleR.ts` [V].
If the owner wants a cheap bundle anyway: one lane, Schedule R + Form 8396 + Form 8936 (≈ +0.3), with the catalog
split of §1.2 first so the gain is measured.

## D. Cross-cutting decisions for the owner

1. Confirm the stop rule's number and whether it applies to the estimate's gain or the realized gain.
2. Order: section A first (one batch, two lanes); section B after Schedule E and Form 4797; section C not now.
3. Approve the catalog edits (§1.2) and an estimate refresh before ranking.
