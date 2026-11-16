# Scout design: Form 1116, passive category (tax year 2025, federal)

Scout: claude-opus-5-5, judgment class, year 2025, jurisdiction us. Read-only scouting of
`.claude/worktrees/sweep-tasks` at 63a20efc; nothing in the repository was changed. No model calls, agents, paid
reviews or network fetches.

Marks: **[V]** verified by reading the archived source or the tree at the stated place; **[I]** inferred (from
memory of tax law, or a design judgment), to be checked before encoding; **[D]** a decision for the owner.

Sources are cited as `i1116` = `sources/2025/i1116.pdf` (Instructions for Form 1116 (2025), Dec 23, 2025), `f1116` =
`sources/2025/f1116.pdf` (Form 1116 (2025), created 9/16/25). Page numbers of i1116 are the printed page numbers
(the `.cols.txt` form-feed pages match the printed footers, checked on pp. 2, 9, 17, 25).

---

## 1. Scope

### 1.1 What is computed today [V]

`forms/2025/ftc.yaml` computes the Schedule 3 line 1 election without Form 1116 (i1116 pp. 1–2): credit =
smaller of `ftc.taxes_if_asked` and `ftc.regular_tax` (= `f1040.line16` + `s2.line1z`, i1116 p. 25 Line 20).
`s3.line1` copies `ftc.credit`. Two refusal gates send everything else away:

| Gate | Where | Refuses |
|---|---|---|
| `ftc.needs1116` | `ftc.credit` refuses | tax over `ftc.limit` ($300 / $600 MFJ), or `ftc.all_passive_if_tax`, `ftc.statements_if_tax`, `ftc.eligible_if_tax` or `ftc.elect_if_tax` false |
| `ftc.carryover_if_asked` | `ftc.credit` refuses; also `scope.yaml` (scope.credits list) and `s3.other_credit_9` | a foreign tax carryover claimed from another year |

Both are in `docs/COVERAGE.md` (lines 227–235) and `tools/coverage/tree.json` lines 59–60. Neither has an IRS count
in the coverage estimate (`reports/2025/filer_coverage.md` line 20 lists `ftc.needs1116` among the unmeasured gates;
that report is stale per TASKS T-034, regenerate before quoting).

### 1.2 Proposed scope, in two stages

**Stage A (this design, encodable once the three blocking sources of section 2 are archived):** one Form 1116,
category c (passive), for a resident individual, where:

- all foreign income is dividends and interest reported on Forms 1099-DIV / 1099-INT (the "1099 taxes" path of i1116
  p. 19 Tip: amounts in US dollars, no foreign-currency columns), grouped as one "RIC" column for funds (i1116 p. 11,
  RIC pass-through amounts) plus one column per country for directly held foreign shares or bonds [V];
- no foreign capital gains or losses (Worksheets A and B, i1116 pp. 10–16, stay refused);
- line 12 reductions, line 13 high-tax kickout, line 16 adjustments and line 22 (section 960(c)) are all zero, each
  guarded by a refusal (section 1.3);
- the credit is computed whether the tax is over the $300/$600 limit or the filer declines the election;
- Schedule B (Form 1116) is prepared for the current-year carryover the form generates (required by i1116 p. 19,
  Line 10: "Attach Schedule B (Form 1116) ... if you generated a foreign tax carryover in the current year") [V
  the requirement; the schedule itself is not archived, see section 2].

**Stage B (later):** a carryover claimed from earlier years (line 10 from Schedule B (Form 1116) line 3 column
(xiv), i1116 p. 19), which retires `ftc.carryover_if_asked`; foreign tax paid directly (foreign currency, date paid,
conversion, i1116 pp. 3–4 and 18); the Worksheet for Line 18 with foreign qualified dividends in more than one rate
bucket (needs Pub. 514).

### 1.3 Situations that stay refused (Stage A)

| Situation | Reason | New gate (proposed id) |
|---|---|---|
| Any foreign income not passive (wages or business abroad: general category; branch, 951A, 901(j), treaty re-sourced, lump-sum) | separate Form 1116 per category, Part IV summary, loss allocation across categories (i1116 pp. 5–6, 20–21) | `f1116.other_category` (from `ftc.all_passive` = No) |
| Foreign tax not on a qualified payee statement (paid to a country directly, a foreign brokerage) | foreign-currency Part II columns, conversion rules (i1116 pp. 3–4, 18) | `f1116.not_on_statement` (from `ftc.statements` = No); Stage B |
| Foreign-source capital gain or loss | Worksheets A/B or Pub. 514 (i1116 pp. 10–16) | `f1116.foreign_gain` (new tick box) |
| A carryover from an earlier year | Schedule B (Form 1116) prior-year rows | `ftc.carryover_if_asked` (unchanged); Stage B |
| Carryback of 2025 excess to 2024 | amended 2024 return (i1116 p. 19) | none needed: the tool carries forward only; the help says so [D1] |
| Prior overall foreign loss, separate limitation loss or overall domestic loss account; US net loss this year | line 16 adjustments 2–6 (i1116 pp. 20–22) | `f1116.loss_accounts` (question, asked only of filers whose 2024 return had Form 1116: `s3.prior_forms_if_forms`), `f1116.us_loss` (computed: `f1116.line15` > `f1116.line18`) |
| Line 12 reductions (Form 2555, Puerto Rico, American Samoa, oil and gas, mineral, Forms 5471/8865 failure, boycott, section 909) | i1116 pp. 19–20 | covered by existing refusals (`sa.excluded_income` for 2555/4563/PR; `sb.form5471_if_foreign`) plus one tick box `f1116.reduction` for the rest [I: exact coverage of existing gates to be confirmed by the lane] |
| High-taxed passive income (line 13) | i1116 p. 11, "High-taxed income", p. 20 Line 13; Reg. 1.904-4(c) | `f1116.high_taxed` (computed per column, threshold per [D2]) |
| Interest expense to apportion by the asset method: gross foreign income over $5,000 and any investment interest (Form 4952), student loan interest or car loan interest | i1116 p. 18, Line 4b, "Otherwise, each type of interest expense is apportioned separately using an 'asset method'" | `f1116.asset_method` (computed) |
| Foreign qualified dividends that must be adjusted and fall in more than one rate bucket | i1116 p. 9, "How to make adjustments"; rate assignment not stated in i1116 | `f1116.mixed_rates` (computed); Stage B after Pub. 514 |
| Form 4952 line 4g election together with foreign qualified dividends | i1116 p. 10, "Don't adjust ... qualified dividends that you elected to include on Form 4952, line 4g" | `f1116.f4952_election` (computed: `f4952.line4g` > 0 and foreign dividends > 0) |
| Foreign tax redetermination for an earlier year, contested tax, accrual basis | Schedule C (Form 1116), Form 7204 (i1116 pp. 4–5) | tick box `f1116.redetermination`; accrual: the form's "Paid" box is fixed [I] |
| Tax to a sanctioned country | i1116 p. 3 item 4; Pub. 514 list | inside `ftc.eligible` (creditability), help names the list [I] |
| AMT | Form 6251 is refused through `s2.amt`; a regular FTC lowers Form 6251 line 10 and can create AMT (i6251 p. 10, "Do I need to fill out line 8?") | no new gate; risk R4 |

### 1.4 Gates that go away or narrow

- `ftc.needs1116` stops refusing (technique 3.1 of the interview protocol: the id stays as a derived Bool,
  "the Form 1116 path applies"). Its refusal entry on `ftc.credit` is replaced by the gates of 1.3 on Form 1116 lines.
  `docs/COVERAGE.md` and `tree.json` gain the new gates; the "Foreign" theme's `covered` text widens.
- `ftc.elect` (and `ftc.elect_if_tax`) can be retired [D3]: when the election is available, the election credit
  (smaller of tax and regular tax) is never less than the Form 1116 credit this year, so the tool elects it; the only
  reason to decline is a carryover, which Stage A does not claim. A filer who wants the carryover can be offered it
  only where tax exceeds regular tax (rare).
- `ftc.carryover_if_asked`: unchanged in Stage A; removed (with its `scope.yaml` and `s3.other_credit_9` entries)
  in Stage B.
- The `f4952.alternative_allocation` remedy text ("Form 1116 coordination are outside scope", f4952.yaml lines 309,
  445, 525, 643) stays true for the 4g election (gate above).

### 1.5 Share of filers served

- [V] SOI 2023, Table 3.3 column 4: 11,791,525 returns claimed the foreign tax credit, 7.34% of 160,602,107
  (`interview/2025/gate_frequencies.yaml`, `foreign_tax`).
- [I, estimate, judgment] Returns filing Form 1116 rather than the election: no archived count. Judgment: 1–2.5% of
  all returns (the election covers the many small-fund holders). Stage A (passive, 1099-reported, no prior
  carryover, no exotic adjustments) would serve perhaps 60–80% of those: about **0.6–2% of all returns**.
  The coverage estimate will not move until a count for `ftc.needs1116` is added (T-034 (b)); source to archive:
  SOI "Individual Foreign Tax Credit" statistics (Form 1116 counts by category).

---

## 2. Sources

| Document | 2025 | 2026 | Needed for |
|---|---|---|---|
| Form 1116 (2025) | archived, `sources/2025/f1116.*` [V] | **not archived**; i1116 (2026 draft, Sep 28, 2026) says Part II is moved to page 2 and reformatted [V] | every line |
| Instructions for Form 1116 (2025) | archived, `sources/2025/i1116.*` (26 pp.) [V] | archived draft `sources/2026/i1116.*` [V] | every line |
| Schedule B (Form 1116) and its instructions | **to archive (blocking for Stage A)** | to archive | carryover generated (i1116 p. 19) |
| Pub. 514 (2025), Foreign Tax Credit for Individuals | **to archive (blocking: readings A3, A4, A6)** | to archive when posted | state tax allocation (i1116 p. 17), rate bucket of foreign QD, charitable deductions, SALT-cap split, HTKO, examples for fixtures |
| Treas. Reg. 1.904-4(c) (high-taxed income) | **to archive (blocking: D2)** | same | `f1116.high_taxed` threshold and grouping |
| Treas. Reg. 1.861-8(e)(6), (e)(9) (state taxes; deductions not definitely related) | to archive (supports A3, A6) | same | lines 2, 3a, 3b |
| SOI individual foreign tax credit tables | to archive | n/a | share estimate |
| Schedule C (Form 1116) | not needed (refused) | | |
| i1040gi, f1040s3, i6251, f1099div/i1099div, f1099int, p550, rp-2024-40, tax table | archived [V] | i1040gi etc. per existing 2026 rollover; rp-25-32 archived [V] | line 20, tax, 1099 boxes |

Page index for 2025 citations [V]: election and purpose pp. 1–2; creditable / not creditable p. 3; categories
pp. 5–6; RIC column and HTKO p. 11; foreign QD and capital gains, adjustment exception pp. 9–11; Part I lines 1a–3f
pp. 11, 17–18; lines 4a/4b and the Worksheet for Home Mortgage Interest p. 18; Part II and the 1099 Tip pp. 18–19;
line 10 and carryover rules p. 19; line 12 pp. 19–20; lines 13, 15, 16 pp. 20–22; Worksheet for Line 18 and line 18
pp. 23–25; lines 19–24 and Part IV p. 25.

---

## 3. Encoding plan

### 3.1 New collection `f1116col` (one entry per Part I column / Part II line) [I design]

Keyed entries: `ric` for all funds together (i1116 p. 11 "Enter 'RIC' on line i"), one key per country otherwise.

| Line id | Printed | Type | Expression sketch | Cite |
|---|---|---|---|---|
| `f1116col.kind` | (helper) | Enum {dividends, interest, both} | input | f1116 Part II cols (q), (s) |
| `f1116col.div_income` | 1a part | NonNegDollars | input (gated: kind ≠ interest) | i1116 p. 11, Lines 1a and 1b |
| `f1116col.int_income` | 1a part | NonNegDollars | input (gated: kind ≠ dividends) | same |
| `f1116col.div_qualified` | (helper) | NonNegDollars | input, asked only when `f1116.must_adjust` and not `f1116.exception_by_total` | i1116 p. 9 |
| `f1116col.line3d` | 3d | NonNegDollars | sum(div_income, int_income) (unadjusted) | i1116 p. 17, Line 3d ("without regard to any adjustments") |
| `f1116col.line1a` | 1a | NonNegDollars | choose: unadjusted = line3d; adjusted = int_income + (div_income − div_qualified) + multiply_rate(div_qualified, bucket factor) | f1116 line 1a; i1116 p. 9 |
| `f1116col.line3f` | 3f | Rate (shown) | prorate ratio of line3d / `f1116.line3e`, places 4, cap 1 | i1116 p. 18, Line 3f ("at least four decimal places", precedent `amb.2025` student-loan entry: exactly the stated places) |
| `f1116col.line3g` | 3g | NonNegDollars | prorate(`f1116.line3c`, line3d, `f1116.line3e`, places 4) | f1116 line 3g |
| `f1116col.line4a` | 4a | NonNegDollars | choose: `f1116.line3d_total` ≤ $5,000 → 0; else prorate(`sa.line8e`, line3d, `f1116.line3e_hmi`, 4) | i1116 p. 18, Line 4a and worksheet |
| `f1116col.line2` | 2 | NonNegDollars | per reading A3 (state income tax), else 0 | i1116 p. 17, Line 2 |
| `f1116col.line6` | 6 | NonNegDollars | sum(line2, line3g, line4a) (4b and 5 are 0 in Stage A) | f1116 line 6 |
| `f1116col.line7` | 7 | Dollars | subtract(line1a, line6) | f1116 line 7 |
| `f1116col.tax_div`, `f1116col.tax_int` | 8 (q), (s) | NonNegDollars | input | f1116 Part II; i1116 p. 19 Tip ("1099 taxes") |
| `f1116col.line8u` | (u) | NonNegDollars | sum(tax_div, tax_int) | f1116 Part II col (u) |
| `f1116col.high_taxed` | (gate) | Bool | test line8u > rate × larger_of(line7, 0) per [D2] | i1116 p. 11; p. 20 Line 13 |

### 3.2 New form `f1116` (return-level lines) [I design; line text V]

| Line id | Printed | Type | Expression sketch | Cite |
|---|---|---|---|---|
| `f1116.applies` | (gate) | Bool | copy `ftc.needs1116` (renamed meaning) | i1116 p. 2, Who should file |
| `f1116.line3a` | 3a | NonNegDollars | choose: not itemizing → `f1040.line12e`; itemizing → `sa.line4` + allocated part of `sa.line5e` for 5b+5c per A4 | i1116 p. 17, Line 3a |
| `f1116.line3b` | 3b | NonNegDollars | `s1.line26` − `s1.line21` (student loan interest goes to 4b) per A6; Schedule 1-A line 37 excluded | i1116 p. 17, Line 3b |
| `f1116.line3c` | 3c | NonNegDollars | sum(3a, 3b) | f1116 |
| `f1116.line3d_total` | (helper) | NonNegDollars | sum_over f1116col.line3d | f1116 |
| `f1116.line3e` | 3e | NonNegDollars | gross income from all sources per A1 | i1116 p. 17, Lines 3d and 3e |
| `f1116.line3e_hmi` | (helper) | NonNegDollars | same as 3e (no Form 2555 in scope) | i1116 p. 18 worksheet line 2 |
| `f1116.line1a_total`, `line6_total`, `line7_total` | 1a, 6, 7 Total | Dollars | sum_over | f1116 |
| `f1116.line8` | 8 | NonNegDollars | sum_over f1116col.line8u | f1116 |
| `f1116.line9` | 9 | copy line8 | | f1116 |
| `f1116.line10` | 10 | const 0 in Stage A (`ftc.carryover_if_asked` refuses) | | i1116 p. 19 |
| `f1116.line11` | 11 | sum(9, 10) | | |
| `f1116.line12`, `line13` | 12, 13 | 0, guarded | | i1116 pp. 19–20 |
| `f1116.line14` | 14 | sum(11, −12, 13) = line11 in Stage A | | |
| `f1116.line15` | 15 | copy line7_total | | |
| `f1116.line16` | 16 | 0, guarded by `f1116.us_loss`, `f1116.loss_accounts` | | i1116 p. 20 |
| `f1116.line17` | 17 | sum(15, 16) | | |
| `f1116.ti_base` | (helper) | Dollars | `f1040.line11b` − `f1040.line14` + `s1a.line37` | f1116 line 18; i1116 p. 23 |
| `f1116.must_adjust` | (gate) | Bool | (QDCG path: `qdcg.line5` > 0 and `qdcg.line23` < `qdcg.line24`) or (SDTW path: `sdtw.line18` > 0 and `sdtw.line45` < `sdtw.line46`) | i1116 pp. 9–10, 23–24 |
| `f1116.exception` | (gate) | Bool | (qdcg.line5 or sdtw.line18) ≤ param `f1116.exception_ceiling`[fs] and foreign QD + foreign NCG < param $20,000 (foreign NCG = 0 in scope) | i1116 p. 9 (QDCGTW), p. 10 (Schedule D filers), p. 24 |
| `f1116.exception_by_total` | (helper) | Bool | sum_over div_income < $20,000 (sufficient for the second condition, so the qualified split need not be asked) | design |
| `f1116.adjusted` | (gate) | Bool | must_adjust and not exception [D4: or the better of both] | |
| `f1116.ws18_line1..12` | WS18 1–12 | Dollars | line1 = ti_base; 2 = sdtw.line42, 4 = sdtw.line39 (SDTW path only); 6 = qdcg.line20 / sdtw.line33; 8 = qdcg.line17 / sdtw.line30; 10 = qdcg.line9 / sdtw.line22; 3,5,7,9 = multiply_rate by 0.2432, 0.3243, 0.4595, 0.5946; 11 = sum; 12 = subtract_floor0(1, 11) | i1116 pp. 23–25 |
| `f1116.line18` | 18 | NonNegDollars | choose: adjusted → ws18_line12; else floor0(ti_base) | f1116 line 18 |
| `f1116.line19` | 19 | Rate (shown) | choose: line17 ≤ 0 or line18 = 0 → 0; line17 > line18 → 1; else ratio places per A2 | i1116 p. 25, Line 19 |
| `f1116.line20` | 20 | copy `ftc.regular_tax` | | i1116 p. 25, Line 20 |
| `f1116.line21` | 21 | multiply_rate(line20, line19) — or prorate(line20, line17, line18, places) | | f1116 |
| `f1116.line22` | 22 | 0 (`s3.section960c_if_foreign` already refuses) | | i1116 p. 25 |
| `f1116.line23` | 23 | sum(21, 22) | | |
| `f1116.line24` | 24 | smaller_of(14, 23) | | f1116; i1116 p. 25 |
| `f1116.line27` | 27 | copy line24 | | f1116 Part IV ("must now be completed even when filing only one Form 1116", i1116 p. 1 What's New) |
| `f1116.line32` | 32 | copy line27 | | |
| `f1116.line33` | 33 | smaller_of(20, 32) | | |
| `f1116.line34` | 34 | 0 (boycott refused) | | |
| `f1116.line35` | 35 | subtract(33, 34) | | f1116 line 35 |
| `f1116.excess` | (helper) | NonNegDollars | subtract_floor0(line14, line24): the current-year carryover to Schedule B (Form 1116) | i1116 p. 19 |

Bucket factor for `f1116col.line1a` (adjusted path): 0.4054 if all qualified dividends are at 15% (`qdcg.line9` = 0
and `qdcg.line20` = 0, `qdcg.line17` > 0), 0.5405 if all at 20%, 0 if all at 0%; otherwise `f1116.mixed_rates`
refuses [V factors, i1116 p. 9; I the single-bucket test].

### 3.3 `f1116sb` (Schedule B (Form 1116)) [I: not archived]

Minimal Part I for passive category: the current-year excess (`f1116.excess`) as the 2025 row, carryover to 2026
column (xiv). Line ids and printed numbers to be taken from the archived schedule. Stage B adds the prior-year rows
and line 10 of Form 1116.

### 3.4 Parameters (`params/2025.yaml`, Lane 1 only) [V values from i1116]

`f1116.exception_ceiling` {mfj 39460000, qss 39460000, mfs 19730000, single 19730000, hoh 19730000} (i1116 p. 9);
`f1116.exception_qd_limit` 2000000 (p. 9, "less than $20,000"); `f1116.interest_threshold` 500000 (p. 18, "doesn't
exceed $5,000"); rates `f1116.adj_15` 0.4054, `f1116.adj_20` 0.5405 (p. 9); `f1116.ws18_28` 0.2432, `ws18_25`
0.3243, `ws18_20` 0.4595, `ws18_15` 0.5946 (p. 23); `f1116.high_tax_rate` per D2; `f1116.ratio_places` 4.

### 3.5 Changes to existing forms

- `ftc.yaml`: `ftc.needs1116` keeps its id as "Form 1116 path"; `ftc.credit` = choose(election path →
  `ftc.limited`; Form 1116 path → `f1116.line35`; no tax → 0). Its refusal list loses `ftc.needs1116` and keeps
  `ftc.carryover_if_asked` (Stage A). `ftc.elect` retired or kept per D3. `ftc.taxes` stays the parent amount; a
  conflict check (`interview/2025/conflict_checks.yaml`) requires sum_over `f1116col.line8u` = `ftc.taxes` on the
  Form 1116 path.
- `s3.line1` unchanged (copies `ftc.credit`) [V]; the credit limit worksheets that read Schedule 3 line 1 need no edit.
- `sales.yaml`: none if `sum_over` with a `where` test on `sales.h` > 0 is accepted (precedent: `eic.yaml` line 70
  `where` on collection fields) [I that `where` admits a money comparison].
- `scope.yaml`, `s3.yaml`: none in Stage A.

### 3.6 Readings needed (ambiguity register entries, `ambiguities/2025.yaml`)

- **A1 `amb.2025.f1116_gross_income`** (line 3e). "gross income means the total of your gross receipts (reduced by
  cost of goods sold), total capital and ordinary gains (before subtracting any losses), and all other income (before
  subtracting any deductions)" (i1116 p. 17). Proposed: wages `f1040.line1z` + `f1040.line2b` + `f1040.line3b` +
  `f1040.line4b` + `f1040.line5b` + `f1040.line6b` + gains (sum of positive `sales.h` rows, the positive aggregate
  rows `sd.line1a`/`sd.line8a`, and `sd.distributions`) + Schedule C line 7 per business + Schedule 1 income lines
  (1, 2a, 7, 8b–8z). Open: the aggregate (no Form 8949) route gives only netted totals per box; readings: (a) net per
  box, (b) ask gross gains. Fixture F11 shows the reading moves the credit by $3.82.
- **A2 `amb.2025.f1116_line19_places`**: line 19 states no rounding. Readings: 4 places half-up (as line 3f and the
  lump-sum worksheet line 4, i1116 p. 7), full precision, 6 places. Proposed: 4.
- **A3 `amb.2025.f1116_state_tax`**: state income tax of itemizers (i1116 p. 17, Line 2 "Also include on line 2 state
  and local income taxes related to foreign source income"; "you may be required to make a special allocation ...
  See Pub. 514"). Blocked on Pub. 514 and Reg. 1.861-8(e)(6). Until read: refuse itemizers with state income tax on
  line 5a and foreign gross income above a de minimis, or apportion by 3d/3e [D5].
- **A4 `amb.2025.f1116_salt_cap`**: "Don't include more state and local taxes on Form 1116, lines 2 and 3a, than the
  amount reported on Schedule A (Form 1040), line 5e" (p. 17). How the cap is split among income, real estate and
  personal property tax: pro rata proposed.
- **A5 `amb.2025.f1116_interest_threshold`**: "you can allocate all of your interest expense to U.S. source income"
  (p. 18) is permissive; the tool takes it (always favourable).
- **A6 `amb.2025.f1116_3b_items`**: which deductions are on 3b. Literal reading: every Schedule 1 Part II adjustment
  except student loan interest (4b); not the Schedule 1-A tips, overtime or QBI deductions (definitely related to US
  income) and not the senior deduction (p. 17 says so). Charitable gifts and gambling losses are not in the 3a list;
  their treatment needs Pub. 514 [I].
- **A7 `amb.2025.f1116_exception_choice`**: under the adjustment exception, adjusting is still allowed; the tool
  elects not to adjust [D4].

---

## 4. Interview plan (per `docs/2026-11-13_interview_construction_protocol.md`)

Typical filer: a person with an international index fund in a US brokerage, one Form 1099-DIV with box 7 above
$300, box 8 blank, and a year-end tax supplement listing "foreign source income". Filer with nothing: no foreign
tax (`ftc.taxes` = 0): asked nothing new. Topic: order 280 (investments, foreign), after `ftc.taxes` (seq 1) and the
existing seq 2–4.

Questions (seq after 4; words are drafts for the lane to apply section 2 of the protocol to):

1. `ftc.all_passive` (exists, seq 2): keep; a No now refuses at `f1116.other_category`. Fix BUG-0540 help.
2. `ftc.statements` (exists, seq 3): keep; No refuses at `f1116.not_on_statement` (Stage A).
3. `ftc.eligible` (exists, seq 4): keep.
4. `ftc.elect`: retire [D3] (saves one step for every foreign-tax filer under the limit).
5. `$f1116col` (seq 6, only on the Form 1116 path): "Where did this foreign tax come from? Add your mutual funds and
   ETFs together as one entry, and each country of shares you own directly as its own entry." Help (≤40 words): box 8
   of the 1099-DIV is blank for a fund and names the country for a foreign company.
6. Per entry, `f1116col.kind` (one choice, typical answer "Dividends" cheap): "Was it from dividends, interest or
   both?"
7. Per entry, `f1116col.div_income`: "How much of the dividends came from sources outside the United States?" Help:
   "A fund's year-end tax information lists its foreign source income; for shares of a foreign company it is the
   whole dividend (box 1a)." N2 check: who could answer wrongly? A fund holder who enters all dividends; the help and
   a conflict check (foreign income ≤ `sb.ordinary_dividends`) guard it.
8. Per entry, `f1116col.tax_div` (and `_int`): "How much foreign tax was taken from them? (box 7)".
9. Per entry, `f1116col.div_qualified`: asked only when `f1116.must_adjust` and not `f1116.exception_by_total`
   (N4: the typical filer never sees it).
10. Tick group `f1116_screens` (one step, "None of these" typical): "Do any of these apply to your foreign income
    or tax?" Boxes (≤12 words each): a foreign-source capital gain or loss (`f1116.foreign_gain`); a refund or change
    of foreign tax for an earlier year (`f1116.redetermination`); a reduction listed for Form 1116 line 12
    (`f1116.reduction`, help lists them). Commonest refusal (capital gain) first.
11. `f1116.loss_accounts` beneath `s3.prior_forms_if_forms` (a 2024 Form 1116): "Does your 2024 Form 1116 show a
    foreign or domestic loss account still to recapture?" (N5: lives with the 2024 return question).

Computed refusals (no question): `f1116.asset_method`, `f1116.us_loss`, `f1116.high_taxed`, `f1116.mixed_rates`,
`f1116.f4952_election`, `ftc.carryover_if_asked` (unchanged).

Coverage rows (`interview/2025/coverage/investments_foreign.yaml`): `ftc.election_small` (proceeds, not_asked the
1116 questions); `ftc1116.fund_over_limit` (F1, proceeds, `f1116.line35`); `ftc1116.declines_election` (if D3 keeps
the question); `ftc1116.general_category` (refused `f1116.other_category`); `ftc1116.paid_directly` (refused
`f1116.not_on_statement`); `ftc1116.foreign_gain`; `ftc1116.redetermination`; `ftc1116.loss_account`;
`ftc1116.asset_method` (foreign income $6,000 and student loan interest); `ftc1116.carryover_in` (refused
`ftc.carryover_if_asked`).

Persona: `interview/2025/personas/14_investor_international_fund.yaml`: single, 45, one W-2 ($80,000), one
international fund: $6,000 ordinary dividends ($4,000 qualified), $2,500 foreign source, $400 foreign tax (fixture
F1). Record its walk before and after (protocol section 7, item 8); expected new steps for it: about 4 (entry list,
kind, income, tax) plus the tick screen.

---

## 5. Fixtures (hand-predicted from i1116/f1116; tax from the archived 2025 Tax Table / rate schedule and the QDCG
worksheet; cents half-up; ratios 4 places half-up per A2)

Arithmetic was run in exact decimal from `tables/2025/tax_table.yaml` and `rate_schedule.yaml` [V the tables; the
fixture values are this scout's computation, evidence class "synthetic, source-predicted", not independent hand
work]. All have one RIC column unless stated, no interest, standard deduction unless stated.

| ID | Facts | Key arithmetic | Expected |
|---|---|---|---|
| F1 | Single; wages 80,000; div 6,000 (QD 4,000); foreign 2,500; tax 400 | AGI 86,000, TI 70,250; 3e 86,000; 3f 2,500/86,000 = 0.0291; 3g 15,750×0.0291 = 458.33; 7 = 2,041.67; QDCGTW 22 tax(66,250) 9,495 + 600 = 10,095 = line 20; exception (L5 66,250); 19 = 2,041.67/70,250 = 0.0291; 21 = 293.76 | 24 = 35 = **293.76**; excess 106.24 (Schedule B) |
| F2 | MFJ, 66 and 67; IRA 50,000; div 30,000 (QD 25,000); foreign 12,000; tax 1,100 | std 34,700; senior 12,000; TI 33,300; line 20 = tax(8,300) = 833; 18 = 80,000 − 46,700 + 12,000 = 45,300; 3f 0.1500; 3g 5,205; 7 = 6,795; 19 = 0.1500 | **124.95**; excess 975.05. Pins the Schedule 1-A line 37 add-back |
| F3 | Single, itemizes (no state income tax): wages 150,000; div 20,000 (QD 15,000); foreign 6,000; tax 450; mortgage (8e) 18,000; real estate tax 8,000 | TI 144,000; 3a 8,000; 3f 6,000/170,000 = 0.0353; 3g 282.40; 4a 18,000×0.0353 = 635.40; 7 = 5,082.20; line 20 = 23,807 + 2,250 = 26,057; 19 = 0.0353; 21 = 919.81 | **450** (not limited); excess 0 |
| F4 | F3 with foreign 5,000, tax 800 | 4a = 0 (≤ $5,000); 3g 235.20; 7 = 4,764.80; 19 = 0.0331; 21 = 862.49 | **800**; pins the $5,000 boundary |
| F4b | F3 with foreign 5,001, tax 800 | 4a = 529.20; 7 = 4,236.60; 19 = 0.0294; 21 = 766.08 | **766.08**; excess 33.92 |
| F5 | Single; wages 260,000; div 30,000 all QD, all at 15%; foreign 10,000 (all QD); tax 900 | TI 274,250; L5 244,250 > 197,300: adjust. 1a = 10,000×0.4054 = 4,054; 3f (unadjusted 3d) 0.0345; 3g 543.38; 7 = 3,510.62; WS18: 8 = 30,000, 9 = 17,838, 12 = 256,412; 19 = 0.0137; line 20 = 55,223 + 4,500 = 59,723; 21 = 818.21 | **818.21**; excess 81.79 (unadjusted would give 900) |
| F6 | Single; wages 213,050; div 8,000 all QD; foreign 3,000; tax 320 | TI 205,300; L5 = 197,300 exactly: exception available; 3f 0.0136; 3g 214.20; 7 = 2,785.80; 19 = 0.0136; line 20 = 41,399; 21 = 563.03 | **320** |
| F6b | F6 with wages 213,051 | L5 197,301: must adjust; 1a 1,216.20; 7 = 1,002.00; 18 = 205,301 − 4,756.80 = 200,544.20; 19 = 0.0050; 21 = 207.00 | **207.00**; excess 113.00. Pins `≤` at the ceiling |
| F7 | Single; wages 100,000; div 25,000 all QD; foreign 20,000 all QD; tax 1,800 | TI 109,250; L5 84,250; exception fails (20,000 not < 20,000); 1a 8,108; 3f 0.1600; 3g 2,520; 7 = 5,588; WS18 12 = 109,250 − 14,865 = 94,385; 19 = 0.0592; line 20 17,205; 21 = 1,018.54 | **1,018.54**; excess 781.46 (with `≤` the mutant gives 1,800). Pins `<` |
| F8 | Single, 70; only div 20,000 (QD 18,000); foreign 8,000; tax 700 | std 17,750; senior 6,000; TI 0, line 20 = 0; 18 = 20,000 − 23,750 + 6,000 = 2,250; 3f 0.4000; 7 = 900; 19 = 0.4000; 21 = 0 | **0**; excess 700. Under D2 at 37%, 700 > 0.37×900 refuses (`f1116.high_taxed`): decide D2 before fixing the expectation |
| F9 | Single; only nonqualified foreign dividends 40,000 (column Canada); tax 1,500 | TI 24,250; 3f 1.0000; 7 = 24,250 = line 18; 19 = 1.0000; line 20 = tax(24,250) 2,675 | **1,500** |
| F10 | MFJ; wages 120,000; RIC div 8,000 incl. foreign 3,000 (tax 210); Canada 2,000 (tax 300); Japan 1,000 (tax 153.15); QD 9,000 | TI 99,500; per column 3f 0.0229, 0.0153, 0.0076; 3g 721.35, 481.95, 239.40; 7 = 2,278.65 + 1,518.05 + 760.60 = 4,557.30; 19 = 0.0458; line 20 10,806; 21 = 494.91 | **494.91**; excess 168.24. Pins per-column rounding (total-ratio rounding gives a different 3g) |
| F11 | Single; wages 60,000; long-term sales +10,000 and −4,000; CGD 1,000; div 5,000 (QD 4,000); foreign 3,000; tax 330 | TI 56,250; A1 gross reading 3e 76,000: 3f 0.0395, 3g 622.13, 7 = 2,377.87, 19 0.0423, line 20 6,380, 21 = 269.87 | **269.87** (net reading 72,000 gives 266.05) |

Refusal fixtures (expect the gate): general-category wages abroad; tax paid directly; foreign capital gain;
carryover in; foreign gross 6,000 with $500 student loan interest (`f1116.asset_method`); prior loss account.

Mutation pins to expect (`reports/2025/mutation.md` kinds: operand replacement, boundary): the $5,000 boundary
(F4/F4b), the exception ceiling `≤` (F6/F6b), the $20,000 `<` (F7), the 3f places (F1, F10), `smaller_of` on line 24
(F3 unlimited vs F1 limited), the add-back of `s1a.line37` (F2), the adjusted/unadjusted choice (F5). Expected
survivors: the line 19 cap and the `line17 ≤ 0` branch (equality F9 cannot tell `>` from `≥`; line 17 ≤ 0 with
line 20 > 0 is not reachable in Stage A without line 2 amounts) — list them as equivalent on answered inputs.

External engines [V by reading the local copies under `.engines/`]: neither computes Form 1116. OpenTaxSolver 2025
(`taxsolve_US_1040_2025.c` line 2750) takes Schedule 3 line 1 as an entered amount; UsTaxes 2025
(`irsForms/Schedule3.ts` lines 58–59) takes `otherIncome.foreignTaxCredit` directly, with no limit. The adapters can
compare the rest of the return by feeding the tool's `f1116.line35` as the entered credit (the existing pattern,
`ots_adapter.py` line 371 and `ustaxes_adapter.py` line 141), which checks nothing about Form 1116 itself.
PolicyEngine's credit is a supplied amount (tools/engines/README.md line 379). Independent evidence for Form 1116
therefore rests on the Lean evaluator, class M and the reviews.

---

## 6. Tax year 2026 (from `sources/2026/i1116.*`, draft of Sep 28, 2026) [V unless marked]

- Senior deduction moves to Schedule 1-A line 43; car loan interest to line 36 (2026 i1116 p. 2 Reminders, p. 20
  Line 3b, p. 26 Line 18). The ids `s1a.line37` / `s1a.line30` keep their ids in 2026 (`changes/2026/s1a.yaml`
  lines 518–526, 673–684 set `printed` only), so the 2026 operations on `f1116` are citation and label `set`s.
- Adjustment exception ceilings: $403,550 MFJ/QSS, $201,775 single and MFS, $201,750 HOH (2026 i1116 p. 11);
  consistent with rp-25-32's 32% bracket starts (`sources/2026/rp-25-32.txt` lines 452–473). `set` on the parameter.
- The 0.4054/0.5405 and Worksheet for Line 18 factors are unchanged (2026 i1116 pp. 11, 27).
- Itemized deduction limit: each itemized deduction used on lines 2, 3a, 3b, 4a, 4b is reduced by the reduction
  percentage (2026 i1116 p. 20). The 2026 Schedule A refuses the limit (`f1040.gate.itemized_limit`,
  `changes/2026/sa.yaml` lines 493–497), so no operation is needed while that refusal stands; note it there.
- Part II moved to page 2, foreign-currency columns first, US-dollar columns (r)–(w) (2026 i1116 p. 2, p. 22 Tip):
  `printed` sets on the Part II lines once the 2026 Form 1116 draft is archived (it is not).
- New section 904(b)(6) code on line i (inventory): out of scope; no operation.
- Page locators shift (the draft has a cover page): every cite needs a 2026 locator.
- File: `changes/2026/f1116.yaml` (plus `ftc.yaml` entries if the ftc labels change), `verified: draft`.

---

## 7. Lane split

Interface agreed before lanes start: ids of section 3 (`f1116.*`, `f1116col.*`, `f1116sb.*`, the gate ids of 1.3),
and that `ftc.credit` reads `f1116.line35`.

| Lane | Files (no overlap) | Model / class | Work |
|---|---|---|---|
| 0 Sources | `sources/2025/`, `sources/2026/` new files only | Sonnet, mechanical | archive Schedule B (Form 1116) and instructions, Pub. 514, Reg. 1.904-4 and 1.861-8, 2026 Form 1116 draft, SOI FTC tables. Precedes 1 and 2 |
| 1 Form 1116 | `forms/2025/f1116.yaml`, `forms/2025/f1116col.yaml`, `params/2025.yaml` (new keys only), `ambiguities/2025.yaml` (A1–A7) | Opus, judgment | sections 3.1, 3.2, 3.4, 3.6; fixtures F1–F11 in `fixtures/2025/f1116.json` |
| 2 Schedule B (Form 1116) | `forms/2025/f1116sb.yaml` | Opus, judgment | section 3.3; its fixtures (the excess of F1, F2, F5, F7, F10) |
| 3 Wiring and interview | `forms/2025/ftc.yaml`, `interview/2025/questions.yaml`, `interview/2025/coverage/investments_foreign.yaml`, `interview/2025/conflict_checks.yaml`, persona 14, `tools/coverage/tree.json` | Opus (interview judgment); bank formatting Sonnet | section 3.5, section 4 |
| 4 Year 2026 | `changes/2026/f1116.yaml`, `changes/2026/ftc.yaml` | Sonnet for the sets, Opus to adjudicate | section 6, after 1–3 land |

Reviews (one per form per round, after its fixes, per project CLAUDE.md): transcription, render and class M for
`f1116`, `f1116col`, `f1116sb` and the changed lines of `ftc` = 12 calls, line-scoped for `ftc`. Screen and false-no
reviews of the new question gates (about 8) and a completeness review are sampled per release. Rough total: 12 to
16 paid calls.

---

## 8. Risks and decisions for the owner

Decisions:

- **D1** Carryback: the tool never carries 2025 excess back to 2024 (that needs an amended 2024 return); it
  carries forward on Schedule B. Help says so.
- **D2** High-taxed income threshold and grouping (Reg. 1.904-4(c), not archived): 37% of each column's net income
  (i1116 p. 11: "exceed the highest U.S. tax that can be imposed on the income"), or a lower rate for qualified
  dividends. At 20% the Japan column of F10 (153.15 on 760.60, 20.1%) would be high-taxed; at 37% it is not. Low-
  income filers like F8 are high-taxed under either reading (the standard deduction apportioned to the column
  leaves little net income), so the gate refuses them. Their credit is $0 in any case; only the carryover is lost.
- **D3** Retire `ftc.elect` and elect automatically when the election is available.
- **D4** Under the adjustment exception, take the unadjusted path (simple), or compute both and take the larger
  credit (the adjusted path can win when foreign income is nonqualified and US gains are large; the instructions
  allow either).
- **D5** State income tax of itemizers (A3): refuse until Pub. 514 is read, or apportion by 3d/3e on line 2. Most
  itemizers in income-tax states hit this, so refusing narrows Stage A a lot.
- **D6** Line 19 rounding (A2) and gross income composition (A1, the aggregate-route gap).

Risks:

- **R1** Three blocking sources are not archived (Schedule B (Form 1116), Pub. 514, Reg. 1.904-4). Section 3.3 and
  readings A3, A4, A6 and D2 are inferred until they are.
- **R2** Foreign-source income is not on the 1099-DIV. The filer must find it on the fund's supplement, which is
  the heaviest new question; a wrong entry (all dividends) overstates the credit. Guard: conflict check against
  `sb.ordinary_dividends` and help.
- **R3** Line 3e reads many forms (wages, Schedule C line 7, Schedule 1 lines, sales rows). A form added later that
  adds income must also feed 3e. Name it in `docs/` as a reader list.
- **R4** AMT: a larger regular FTC lowers Form 6251 line 10 and can make AMT due. `s2.amt_owed` is a self-assessment
  question, so the tool depends on the filer's answer. Unused AMT foreign tax credits are not tracked (i6251 p. 10).
- **R5** The coverage estimate will not show the gain until a count for the Form 1116 gates exists (T-034 (b)).
- **R6** Interview cost: the typical election filer (tax ≤ $300) must see no new step. Check it in the walk of
  personas 04 and 06 (both have `ftc.taxes: 0` today) and of the new persona.
