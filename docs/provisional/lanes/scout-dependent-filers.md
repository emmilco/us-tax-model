# Design scout: filers who can be claimed as a dependent (TY2025, federal)

Model: claude-opus-5-5 · Class: judgment · Year: 2025 · Jurisdiction: us
Read from `.claude/worktrees/sweep-tasks` (HEAD `63a20efc`). Nothing in the repository was changed. No model calls,
agents, paid reviews or network fetches. Evidence labels: **[V]** verified by reading the tree or archived source in
this session; **[T]** testimony (a doc or comment, not grounded); **[I]** inferred. Fixture arithmetic was computed by
this scout, using the archived tax table (`tables/2025/tax_table.yaml`) and the TCW parameters. It is a prediction for the
lane to re-derive independently, not evidence.

---

## 0. Summary

Three pieces, in descending order of yield per unit of work:

| Piece | What becomes computed | Gate(s) | Share | Size |
|---|---|---|---|---|
| **D. Dependent standard deduction** (unlock) | Every return where someone can claim you (or your spouse on a joint return) | `sa.dependent` refusals on `sa.standard` and `sa.deduction`; `eic.step4` refusal | **4.7% of returns; +3.9 points alone, step 3 of the ladder** (`reports/2025/filer_coverage.md`, dated 2026-11-01; protocol 1.1 notes the report is stale for its gate list) [V] | Small: about 8 lines in `sa`, 1 refusal removed in `eic`, 1 gate added in `f8962` |
| **K. Form 8615** (kiddie tax, on the child's return) | Children under 24 with more than $2,700 of unearned income, at the parent's rate | `scope.f8615_if_unearned_2700` → `scope.other_line16` → `f1040.line16` | Unmeasured. T-034 names "the kiddie tax" as an unmeasured gate [V]. Inside the 4.7% for dependents, and also reaches non-dependents | Medium: new form (~30 lines) plus a status-bound QDCG def |
| **P. Form 8814** (parent's election, on the parent's return) | Parent reports a child's interest and dividends | `scope.f8814` → `scope.other_line16`, and `eic.step2_other` | Unmeasured | Medium-large: touches f1040 3a/3b/7a/16, s1 8z, sd 13, sb, f8960, f4952, eic. **Recommend a later batch, or keep refused** |

Almost all of the measured gain comes from D. It is cheap because the downstream consequences of "can be claimed" are
**already encoded** and were only unreachable [V]:
- `dependent.filer_not_dependent` zeroes the filer's own dependents (Pub 501 p. 11, Dependent Taxpayer Test).
- `eic.step4_age` already tests `sa.dependent` (i1040gi p. 42, Step 4 q. 6).
- `f2441.care_other_or_claimable` already reads it.
- `person.sav_ineligible` already reads it, and `person.sav_claimed` ("is claimed") already drives Forms 8863 and 8880
  and the student loan interest (`sli`) bars.
- New York already has item C and the $3,100 dependent standard deduction (`ny_it201.item_c`, `ny.std_deduction.dependent_single`).

---

## 1. Scope

### 1.1 Becomes computed

**D (dependent standard deduction)**
- The Standard Deduction Worksheet for Dependents (i1040gi p. 35) for single, MFJ and HOH filers. MFS is already
  refused by `s3.mfs`.
- Age and blindness boxes: line 4b reuses `sa.extra` × boxes.
- The filer who itemizes while claimable. The `sa.deduction` refusal "whether standard or itemized" goes away.
- The EIC answer "no credit" for a claimable filer without a qualifying child: the value is already computed by
  `eic.step4_age`; only the refusal is removed.
- A claimable filer with a qualifying child keeps the Step 3 path. The archived i1040gi asks the dependency question
  only at Step 4 q. 6; this was checked by grep [V]. Pin it with fixture D9.

**K (Form 8615)**
- Lines 1–18 for a child who does not file jointly, under 24 by the existing age facts, with Form 8615 line 1 over $2,700.
- Child's Unearned Income Worksheet (i8615 p. 3). The Alternate Worksheet for a net self-employment loss reduces to the
  same formula (§3.6, A6).
- Line 5 Worksheets #1 and #3 (i8615 pp. 5–6). #2 applies only to an itemizing child and stays refused.
- Line 7 with other children: line 12a/b uses `prorate` to 3 places.
- Line 9 at the parent's status, by the tax table/TCW or QDCG.
- Lines 15 and 17 at the child's status; line 18 is the larger of 16 and 17.

**P (Form 8814, optional)**
- Lines 1a–15, one entry per child.
- Routing: line 9 to Form 1040 3a/3b (and Sch B 5), line 10 to Sch D 13 or 1040 7a, line 12 to Sch 1 8z, and line 15
  to 1040 line 16 with box 1.

### 1.2 Stays refused (residual gates, each cited; proposed ids)

| Situation | Proposed gate | Reason / cite |
|---|---|---|
| Dependent filer with Marketplace coverage / Form 1095-A | `f8962.dependent_filer` (new) | i8962 p. 3, Who Can Take the PTC, "2. No one can claim you as a dependent for the year"; reconciliation of APTC for someone claimable needs the claimant's return [V text] |
| QSS + claimable | consistency rule, or refusal `sa.dep_qss` | Worksheet line 3 lists no QSS amount (i1040gi p. 35) [V]; Pub 501 p. 11 says a claimable person can't claim a dependent, and QSS needs one → contradiction, not a computation |
| 8615: child, parent or another child needs the Schedule D Tax Worksheet (28% or unrecaptured §1250 gain) | `f8615.sdtw` (child: `f1040.gate.sdtw`; parent and others: tick box) | i8615 p. 7, "if the child, the parent, or any other child has 28% rate gain or unrecaptured section 1250 gain, use the Schedule D Tax Worksheet" |
| 8615: parent used Schedule J, or the Foreign Earned Income Tax Worksheet (Form 2555) | `f8615.parent_special` | i8615 p. 7 (Schedule J), p. 4 line 6 (Form 2555). The child's own 2555 and Schedule J are already refused (`sa.excluded_income`, `scope.income_averaging`) |
| 8615: child itemizes (line 2 "see instructions"; Line 5 Worksheet #2; #3 lines 5 and 11) | `f8615.child_itemizes` | i8615 p. 3, Line 2. Directly connected deductions are mostly suspended miscellaneous deductions, so the case is rare [I]. Roger and Eleanor (class A, p. 3) are left for a later widening |
| 8615: blind dependent child whose condition 2 (required to file) is not settled by the return | `f8615.filing_unsettled` | i8615 p. 1 condition 2; i1040gi p. 10 Chart B blind thresholds. See A3 |
| 8814: line 4 ≥ $13,500; child had withholding or estimated payments; child not eligible (age, other income, joint return) | `f8814.ineligible` | f8814 line 4; i8814 p. 1 conditions |
| 8814 + EIC | keep `eic.step2_other` refusal (8814 only) | i1040gi p. 40 Step 2 q. 4 sends to Pub 596 Worksheet 1, which is not archived [V] |
| Under-16 filer | `household.filer_under16` (unchanged unless the owner decides; §8, decision 2) | Owner decision 2026-10-22, `amb.2025.filer_under_16`. Its stated reason leans on 8615 being refused [V] |

### 1.3 Gates removed or narrowed

- **Removed:** the `sa.dependent` refusal entries on `sa.standard` and `sa.deduction` (sa.yaml lines 1859 and 1920), and
  `eic.step4` `refuses: sa.dependent` (eic.yaml line 900) [V].
- **Narrowed:** `scope.other_line16` drops `scope.f8615_if_unearned_2700`, so it keeps 8814, education credit recapture,
  Schedule J, PFIC, CFC and 8978. If P is built, it also drops `scope.f8814`.
- **Retired inputs:** `scope.unearned_2700` and `scope.f8615` are replaced by facts derived from the return. Section 4
  covers them, and N8 applies.
- **`tools/coverage/categories.json` `dependent_filer`:** its `gates` is `[sa.dependent]` [V]. After D, `sa.dependent`
  is no longer a refusal gate. The integrator sets the category `refused: false`. The new residual gates (`f8962.dependent_filer`,
  `f8615.*`) are not measurable by the estimate, so they join the unmeasured list.
- **`tools/coverage/tree.json`:** the row `sa.dependent` (topic everyone/status) is retired, and the new residual gates
  are placed.
- **Label fix:** `sa.dependent` still says "or are you a dual-status alien" [V]. Dual-status is refused earlier by
  `scope.nonresident` → `scope.other_income` ("nonresident alien for any part of 2025") [V]. The label and source drop
  the dual-status clause; the interview prompt already did. This is a render change on `sa`.

### 1.4 Expected gain

- D: **+3.9 points alone** (4.7% of returns, SOI Table 1.7, independence assumed) [V report]. A dependent filer also
  hit by an unmeasured gate (8615 residuals, PTC) is overcounted [I].
- K and P: unmeasured. Rank them by `interview/2025/gate_frequencies.yaml` if the owner wants a number. SOI publishes
  8615/8814 counts in Pub 1304 tables that are not archived [I]. Archive one before claiming a figure.

---

## 2. Sources

| Doc | Pages used | 2025 | 2026 |
|---|---|---|---|
| i1040gi | p. 10 Chart B; p. 33 line 12a; p. 34 Exception 1, line 16 (8814 box); p. 35 Standard Deduction Worksheet for Dependents; p. 38 QDCG; p. 42 EIC Step 4 q. 6; tax table pp. 68–79; TCW p. 80 | archived [V] | **not archived** (not posted when the TY2026 round ran [T]): to archive |
| p501 | p. 11 Dependent Taxpayer Test; p. 24 dependent standard deduction and **Examples 1–4 (class A)**; p. 26 Table 8 | archived [V] | to archive when posted |
| f8615 / i8615 | form (1 p.); i8615 pp. 1 (who must file, Jan 1 chart), 3 (worksheet, line 2, examples), 4 (lines 6–8, Persimmon example), 5–6 (Line 5 Worksheets), 7 (line 9), 8 (line 10, 12a/b example), 9–10 (lines 14–18) | archived [V] | not archived: to archive (drafts not seen) |
| f8814 / i8814 | form (1 p.); i8814 pp. 1–4 (conditions, Fred example p. 3) | archived [V] | not archived: to archive |
| i8962 | p. 3 Who Can Take the PTC (2) | archived [V] | archived (2026 dir lists i8962) [V] |
| i8863 | p. 7 line 7 (the questions reused for 8615 conditions 3 and 4) | archived [V] | archived [V] |
| f1040 | line 12a, line 16 boxes | archived [V] | draft archived; 12a unchanged, 12d "January 2, 1962", 16 box 1 8814 [V] |
| rp-25-32 (2026 inflation) | p. 13 §.02 kiddie $1,350 / $13,500; p. 14 §.03 QDCG ceilings; p. 19 §.14(2) dependent "greater of $1,350 or $450 + earned income" | — | archived, final [V] |
| **To archive** | Rev. Proc. 2024-40 (2025 §59(j) child AMT exemption, for risk R4); Pub 596 (2025) (8814 + EIC, if P lifts that refusal); an SOI table with 8615/8814 counts | — | — |

Pub 929 is not needed. I believe it is discontinued [I]; check before listing it.

---

## 3. Encoding plan

### 3.1 D — `forms/2025/sa.yaml` (owner: lane D)

| id | printed | type | expr sketch | cite |
|---|---|---|---|---|
| `sa.dep_earned` | (helper) worksheet footnote | Dollars | `f1040.line1z + s1.line3 + s1.line8r − s1.line15` (subtract line 15 from a sum). Sch 1 lines 6/8t/8u are already refused (Schedule F via `scope.schedule1`; 8t/8u via `s1.line8_other`) [V] | i1040gi p. 35 footnote "*Earned income includes…Generally…line 1z, and Schedule 1, lines 3, 6, 8r, 8t, and 8u minus…line 15"; Pub 501 p. 24 Ex. 4 (a business loss reduces it) |
| `sa.dep_over` | (gate) line 2 test | Bool | `test gt [sa.dep_earned, param sa.dep_earned_test]` | p. 35 line 2 "Is your earned income* more than $900?" |
| `sa.dep_line2` | 2 | NonNegDollars | `choose: over → sum(dep_earned, param sa.dep_add); else → param sa.dep_min` | p. 35 line 2 |
| `sa.dep_line3` | 3 | NonNegDollars | `copy sa.standardbase` (status-keyed; QSS → see A1) | p. 35 line 3 |
| `sa.dep_line4a` | 4a | NonNegDollars | `smaller_of [dep_line2, dep_line3]` | p. 35 line 4a |
| `sa.dep_line4b` | 4b | NonNegDollars | `sum [sa.extra_age65, sa.extra_blind]` (= line 1 boxes × $1,600/$2,000) | p. 35 line 4b |
| `sa.dep_line4c` | 4c | NonNegDollars | `sum [4a, 4b]` | p. 35 line 4c |
| `sa.standard_amount` (or re-point `sa.standard`'s false branch) | (helper) | NonNegDollars | `choose: sa.dependent → dep_line4c; else → sa.standardraw` | p. 34 Exception 1 |

- **Parameters** (`params/2025.yaml`, prefix `sa.`, cited on p. 35):
  - `sa.dep_min` 135000;
  - `sa.dep_add` 45000;
  - `sa.dep_earned_test` 90000.
  - All three change with the year (rp-25-32 keeps 1,350/450 for 2026) [V].
- **Refusals:**
  - Remove the `when: sa.dependent` entries at sa.yaml lines 1859 and 1920.
  - Remove the dual-status clause from the `sa.dependent` label and source.
- **`eic.yaml`:** delete the `refuses: when: sa.dependent` at line 900. The value path is `eic.step4_age` → false [V].
- **`f8962.yaml`:**
  - Add a gate line `f8962.dependent_filer = sa.dependent ∧ (a Form 1095-A entered)` and a refusal on the 8962 entry
    line, cite i8962 p. 3.
  - Lane D claims `f8962`.
- **`person.yaml` (optional, ranked last):** gate `person.sav_claimed` on `sa.dependent`
  (`person.sav_claimed_if_claimable`).
  - Someone who is claimed is necessarily claimable, so a No to `sa.dependent` settles it (N8).
  - This removes a question for every non-dependent student and saver. Persona 07 answers it today [V].
  - `person` is a shared file; claim it only in a batch where no other lane holds it.
- **Ambiguity entries:**
  - `amb.2025.sa_dep_qss` (A1);
  - `amb.2025.sa_dep_earned` (A2: the "Generally" footnote is read as the formula; taxable dependent care benefits
    and the 1z items count as written).
- **Twins:** none.

### 3.2 Q — new def `forms/2025/qdcg_amount.yaml` (owner: lane Q, or lane K's first item)

Form 8615 lines 9 and 15 need the QDCG worksheet on an arbitrary amount, at a **bound** status. The existing `qdcg`
cannot do that:
- It is a worksheet bound to `f1040.line15` / `f1040.line3a_if_ordinary` [V].
- Its lines 6 and 13 read status-keyed parameters.
- Status-keyed parameters resolve on `f1040.status` only (`engine/src/eval.ts` lines 342–348; spec 4.7.4) [V].

`tax_on_amount` and `tcw` already take a bound `status` (`table_lookup` with a status operand; TCW sections chosen by
guard) [V].

- **Def:** `qdcg_amount`, parameters `[amount, qd, ncg, status]`, lines 1–25 mirroring `qdcg` (i1040gi p. 38).
  - Lines 22 and 24 instantiate `tax_on_amount` with the bound status.
- **Lines 6 and 13 at the bound status** (decision 3):
  - (a) `keyed_lookup` on a new hand-written keyed table `tables/2025/qdcg_ceiling.yaml` (keys `[status]`, two cells
    or two tables). `keyed_lookup` exists [V]. Add a check that the rows equal `qdcg.zero_rate_ceiling` /
    `qdcg.fifteen_rate_ceiling`.
  - (b) a five-way `choose` on status over unkeyed parameters.
  - (c) an engine change: an explicit status operand on `param`. This is an atom change with a Lean impact.
  - **Recommend (a).**
- **Equivalence pin:** a fixture or property check that `qdcg_amount(f1040.line15, line3a, ncg, f1040.status).line25`
  equals `qdcg.line25` on every existing qdcg case. That catches drift between the two copies.

### 3.3 K — new `forms/2025/f8615.yaml` (owner: lane K)

**Inputs.** All are new, once per return, and asked only when `f8615.applies`.

| id | prompt essence | type |
|---|---|---|
| `f8615.parent_status` | the filing status on the parent's 2025 return (line C) | Enum(filing_status) |
| `f8615.parent_ti` | the parent's taxable income, Form 1040 line 15 (0 if less) | NonNegDollars |
| `f8615.parent_tax` | the parent's line 16 tax, without tax from Form 4972 or 8814 or an education credit recapture | NonNegDollars |
| `f8615.parent_qd` | the parent's qualified dividends (line 3a) | NonNegDollars |
| `f8615.parent_ncg` | the parent's net capital gain (smaller of Sch D 15/16, or line 7a) | NonNegDollars |
| `f8615.parent_sdtw`, `f8615.parent_sj`, `f8615.parent_feitw` | tick group: the parent's return used the Schedule D Tax Worksheet / Schedule J / the Foreign Earned Income Tax Worksheet → refuse | Bool ×3 |
| `f8615.other_children` | the same parent's return figures this tax for another child | Bool |
| `f8615.line7`, `f8615.others_qd`, `f8615.others_ncg`, `f8615.others_sdtw` | gated by `other_children` | NonNegDollars ×3, Bool |

**Derived conditions** (no new questions; each fact asked once, N8):
- **Condition 3 and 4** (age/support/student, parent alive): reuse `person.edu_kid_age` for the taxpayer.
  - It is the same test i8863 p. 7 line 7 copies from 8615: under 18; or 18 with earned income below half of support;
    or a full-time student 19–23 with earned income below half of support; and a parent alive. It already uses the
    January 1 chart (`age.cut_18`, `age.cut_24`) [V].
  - Sum over taxpayer as in `scope.under24_count`.
  - Boundary note: A4.
- **Condition 5:** `f1040.status ≠ mfj` (the existing `scope.under24_if_not_joint`).
- **Condition 1:** `f8615.line1 > param f8615.base`.
- **Condition 2:** A3.
- **`f8615.applies`** = all of the above, minus the residual gates.

**Lines:**

| id | printed | expr sketch | cite |
|---|---|---|---|
| `f8615.uiw` | worksheet line 3 | `f1040.line9 − f1040.line1z − s1.line3 − s1.line18`. This equals the Unearned Income Worksheet (p. 3) and the Alternate Worksheet with an SE loss (A6). 8615 earned income excludes taxable scholarship 8r (p. 1, "Unearned Income… taxable scholarship and fellowship grants not reported on Form W-2") [V] | i8615 p. 3 |
| `f8615.line1` | 1 | `copy uiw` | f8615 line 1; i8615 p. 3 |
| `f8615.line2` | 2 | `param f8615.base` (2,700; the child-itemizes case refuses) | f8615 line 2 |
| `f8615.line3` | 3 | `subtract_floor0 (1, 2)` | line 3 |
| `f8615.line4` | 4 | `copy f1040.line15` | line 4 |
| `f8615.line5` | 5 | `smaller_of [3, 4]` | line 5 |
| `f8615.ws1_*` | Line 5 Worksheet #1, lines 1–9 | 4 and 5 via `prorate`-style ratio to 3 places, capped at 1; 6 and 7 via `prorate(base, qd, line1, 3)`; 8 and 9 via subtract_floor0 then smaller_of | i8615 p. 5 |
| `f8615.ws3_*` | Line 5 Worksheet #3, lines 1–19 (5 = 0 and 11 = the standard deduction, since an itemizing child refuses) | i8615 p. 6 |
| `f8615.qd5`, `f8615.ncg5` | QD and NCG on line 5 | `choose` #1 when `line3 = line5`, else #3 | i8615 p. 4, line 8 |
| `f8615.line6` | 6 | `copy parent_ti` | line 6 |
| `f8615.line7` | 7 | input (0 when no other children) | line 7 |
| `f8615.line8` | 8 | `sum [5, 6, 7]` | line 8 |
| `f8615.line9` | 9 | `choose`: QD or NCG on line 8 > 0 → `qdcg_amount(line8, qd5 + parent_qd + others_qd, ncg5 + parent_ncg + others_ncg, parent_status).line25`; else `tax_on_amount(line8, parent_status)` | i8615 p. 7 |
| `f8615.line10` | 10 | `copy parent_tax` | p. 8 |
| `f8615.line11` | 11 | `subtract (9, 10)` (Dollars; can a negative arise? A7) | p. 8 |
| `f8615.line12a` | 12a | `sum [5, 7]` | p. 8 |
| `f8615.line13` | 13 (12b folded) | `prorate(line11, line5, line12a, 3)`. When line 7 = 0 the ratio is 1.000, so it equals line 11 (equivalent mutant; pin) | f8615 12b "rounded to at least three places"; i8615 p. 8 example .333 |
| `f8615.line14` | 14 | `subtract (4, 5)` | p. 9 |
| `f8615.line15` | 15 | tax on line 14 at the child's status; QDCG when QD/NCG on line 14 (`qd − qd5`, `ncg − ncg5`) > 0 | p. 9 |
| `f8615.line16` | 16 | `sum [13, 15]` | p. 10 |
| `f8615.line17` | 17 | `copy f1040.non_sdtw_tax` (the child's normal tax; SDTW cases refuse) | p. 10 |
| `f8615.line18` | 18 | `choose: line5 > 0 → larger_of [16, 17]; else → line17` (form: "If zero, stop") | f8615 lines 5 and 18 |

- **`f1040.yaml`** (lane K owns it in its batch): `f1040.line16` becomes a choose on `f8615.applies` → `f8615.line18`,
  else the existing choose. Add a refusal when both `f8615.applies` and `f1040.gate.sdtw` hold. Update the line-16
  refusal `form:` text to drop 8615.
- **`scope.yaml`:**
  - `scope.other_line16` drops `scope.f8615_if_unearned_2700`.
  - Retire `scope.unearned_2700`, `scope.f8615`, their gate lines and the profile entries (`interview/2025/sales.yaml`
    lines 137–138, `stage4.yaml` lines 149–150) [V].
  - Keep `scope.under24*`, or move them into f8615.
- **Parameters:** `f8615.base` 270000 (f8615 line 2; i8615 p. 1); the qdcg_ceiling table rows.
- **Ambiguity entries:** A3, A4, A5, A6, A7, plus `amb.2025.f8615_parent_line10` (line 10 names only the 4972, 8814
  and ECR exclusions; the other box-3 amounts are read literally as included).
- **Reviews files:** `reviews/2025/consumers.json` and `operands.json` entries for the new lines (the lane lists them).

### 3.4 P — new `forms/2025/f8814.yaml`, collection `f8814` (one per child; owner: lane P, later batch)

**Lines per entry:**
- 1a, 1b, 2a, 2b and 3 are inputs.
- 4 = sum(1a, 2a, 3), with a refusal when ≥ `f8814.limit` 1,350,000.
- 5 = param 270000.
- 6 = subtract_floor0(4, 5).
- 7 and 8 are folded into 9 = `prorate(6, 2b, 4, 3)` and 10 = `prorate(6, 3, 4, 3)`.
- 11 = 9 + 10.
- 12 = 6 − 11.
- 13 = param 135000.
- 14 = subtract_floor0(4, 13).
- 15 = choose(14 < 135000 → multiply_rate(14, 10%); else → param 13500).

**Totals and readers:**
- `f1040.line3a` and `3b` += Σ9.
- 7a / Sch D 13 += Σ10, via `sd.distributions_if_dividends` or a new term.
- `s1.line8z` = Σ oi8z + Σ12 (s1 is shared).
- `f1040.line16` += Σ15, box 1.
- Sch B line 5 += Σ9 when Sch B is filed.
- f8960 NII includes Σ12 and lines 9 and 10 (i8814 p. 2).
- f4952 investment income includes line 12's interest share (i8814 p. 2).

**Eligibility inputs:** a tick group "Is any of these true of this child?" covering age/student, other income,
withholding/estimated payments, the child filing jointly, and you not being the parent whose return is used. Any Yes
refuses.

**Ambiguity:** A8 (Fred example decimals).

---

## 4. Interview plan (construction protocol, N1–N12)

**Typical filers**
- **D:** a single student 16–23 with one W-2, claimed by parents. The only new fact is `sa.dependent`, already asked
  (order 111 seq 1) [V].
- **K:** a teen with a brokerage account (interest/dividends > $2,700), claimed by parents, parent MFJ.
- **Filer with nothing in the area:** persona 01 (single W-2). It must see no new step. Under-24s also lose
  `scope.unearned_2700` (N8: derived from the return).

**D changes**
- `sa.dependent`:
  - Prompt unchanged.
  - Help: drop "A Yes ends the interview here." Keep "It is whether they can, not whether they do. Answer No if that
    person need not file a return and files none, or files only to get back tax withheld."
- `person.sav_claimed` (optional): move beneath `sa.dependent` as its child.
  - Order 111, seq 2, per person, gated.
  - Prompt "Does that person claim you on their 2025 return?"
  - Help: "Yes only if they actually do, not merely could." (existing help)
- Who could answer `sa.dependent` No wrongly? A student who thinks "my parents claim me" means "do". The help guards it.

**K (new topic "Tax on your investment income at your parent's rate")**
- **Placement:** order 277, between investment interest (276) and NIIT (278); the slot is free [V].
- **Parent:** none needed. The topic is reached only when `f8615.applies` is derived true from entered income, so the
  cost to everyone else is 0.
- **Questions, in order:**
  1. **seq 1:** "Which parent's 2025 return is used for this?" This is a screen with help only (which-parent rules:
     joint return → that return; married filing separately → higher taxable income; unmarried, divorced or separated →
     the parent you lived with most of the year; a remarried parent's joint return). It records nothing.
     - Alternative: fold the rules into seq 2's help. **Recommend folding.** A screen that records nothing is a step
       for no fact (N12).
  2. **seq 2:** `f8615.parent_status`. "What filing status did that parent use on their 2025 return?" (5 choices.)
  3. **seq 3–4:** `parent_ti`, `parent_tax`. "From that return: the taxable income (line 15)" and "the tax (line 16),
     leaving out any tax from Form 4972 or 8814 or an education credit recapture". N6 allows naming a box because the
     filer is holding that paper.
  4. **seq 5–6:** `parent_qd`, `parent_ncg` (lines 3a and 7a / Schedule D 15–16, help on which).
  5. **seq 7:** tick group `parent_return_marks`, heading "Did that return use any of these?" Boxes: "Schedule D Tax
     Worksheet", "Schedule J (farm or fishing income averaging)", "Foreign Earned Income Tax Worksheet". Each refuses.
     This is a once-per-return group; the boxes are rare.
  6. **seq 8:** `f8615.other_children`. "Is that parent's return also used for this tax by another child of theirs?"
     A Yes leads to seq 9–12: the total of the other children's Form 8615 line 5, and their QD, NCG and SDTW parts.
     **[R] Consider refusing in v1** if the lane runs short. That is a ranked item, not a design hole.
- **Conditions 3 and 4:** the questions `person.edu_fulltime`, `person.edu_half_support` and `person.edu_parent`
  (order 243) are reused, not re-asked.
  - Check the walk for "returns to a topic already left". These are reached only after investments (274) make
    `f8615.applies` known. If the walk reports a return, move their `seq`, or accept it with the reason stated.
- **Who could answer No wrongly:**
  - A child unsure which parent: guarded by the help.
  - A parent's tax mis-copied including 8814 tax: the prompt states the exclusion.
- **Refusals that stay** (each told at its own question, N11): `parent_return_marks` boxes, `others_sdtw`, child
  itemizes (told at Schedule A choice), blind dependent with unsettled filing (told at `person.blind`/income).

**P:** keep `scope.f8814` (order 126, `child_extras` tick) as the off-ramp. Add the roster `$f8814` and the per-child
amounts at order 127 (beneath the family topic, N5), with the eligibility tick group per child.

**Coverage rows**
- New files: `interview/2025/coverage/dependent_filers.yaml` (lane D) and `kiddie.yaml` (lane K). One row each:
  - D rows (computed): `dep.w2_student`, `dep.blind`, `dep.mfj_refund_only`, `dep.eic_no_child`.
  - D rows (refused): `dep.ptc_refused`, `dep.qss_conflict`.
  - K rows (computed): `kiddie.interest_parent_mfj`, `kiddie.qd_ws1`, `kiddie.ws3`, `kiddie.other_children`,
    `kiddie.line5_zero`.
  - K rows (refused): `kiddie.parent_sdtw`, `kiddie.parent_sj`, `kiddie.child_itemizes`, `kiddie.blind_dependent`.
  - K rows (not asked): `kiddie.not_asked_over24`, `kiddie.not_asked_joint`.
- **Existing rows whose end changes by design:** `scope.f8615` (refused `scope.other_line16` → completes), and
  `scope.under24_small_income` (`proceeds` on `scope.unearned_2700`, which is retired). See decision 1.

**Personas** (new numbers 14–17; 13 is already duplicated, T-316):
- `14_dependent_student` (typical D);
- `15_kiddie_teen_investor` (typical K);
- `16_refused_kiddie_parent_sdtw`;
- `17_parent_8814` (P).
- Record the walks of 01, 07, 14 and 15 before any change.

---

## 5. Fixtures (hand-predicted by the scout; the lane re-predicts independently)

Unless stated, the filer is single, a resident, claimable (`sa.dependent: true`), born 2007–2009 (16–18, so not under
16) with a parent alive, has no Schedule A, and amounts are in dollars.

**D — dependent standard deduction**

| id | facts | arithmetic (i1040gi p. 35) | expected | class |
|---|---|---|---|---|
| D1 | Pub 501 Ex. 1: age 16, interest 780, wages 150 | earned 150 ≤ 900 → line 2 = 1,350; 4a = min(1,350, 15,750) | `sa.standard` 1,350; AGI 930; line 15 0; tax 0 | **A** (Pub 501 p. 24) |
| D2 | Pub 501 Ex. 3: 18, blind, interest 1,300, wages 2,900 | 2,900+450 = 3,350; 4b = 1 × 2,000 | 5,350; AGI 4,200; line 15 0 | **A** |
| D3 | Pub 501 Ex. 4: 18, wages 7,000, interest 500, Sch C loss 3,000 | earned 7,000−3,000 = 4,000 → 4,450 | 4,450; AGI 4,500; line 15 50; tax 6 (table) | **A** (std) + regression |
| D4 | wages 20,000 | 20,450 vs 15,750 → 15,750 (cap side of smaller_of) | 15,750; line 15 4,250; tax 428 | synthetic |
| D5 | MFJ, both 20–21, both claimable; wages 8,000 + 6,000 | 14,450 vs 31,500 | 14,450; line 15 0 | synthetic |
| D6 | Sch C profit 2,000, no wages | SE 2,000×.9235 = 1,847 → SE tax 282.59, half 141.30 (confirm with the tool's `se`); earned = 2,000 − 141.30 = 1,858.70 → 2,308.70 | `sa.standard` 2,308.70 (kills the mutant dropping `s1.line15`: 2,450) | synthetic |
| D7 | 21, full-time student, wages 2,000, taxable scholarship 8r 3,000, support test met | std earned 5,000 → 5,450; AGI 5,000 → line 15 0; 8615 line 1 = 5,000 − 2,000 = 3,000 (> 2,700), line 3 300, line 4 0, line 5 0 → line 18 = line 17 = 0 | `sa.standard` 5,450; `f8615.line5` 0; `f1040.line16` 0 (pins the two earned-income definitions and the line-5 stop) | synthetic |
| D8 | 30, qualifying relative of a parent; wages 4,000; no child | 4,450; line 15 0; EIC Step 4 q. 6 → no credit | `f1040.line27a` 0, `eic.check_27c` true. Restates `stage9.eic.refuse.dependent_of_another` | synthetic |
| D9 | 20, claimable, with own qualifying child, wages 12,000 | EIC Step 3 path (no dependency question at Step 3) | EIC > 0 from the table. **Lane to compute**; confirm `dependent.filer_not_dependent` does not zero the EIC child | synthetic |

**K — Form 8615**

The child is single and dependent, with std 1,350 unless stated. The parent has no QD/NCG unless stated. All values
were computed with the archived table/TCW.

| id | facts | key arithmetic | expected `f8615.*` / `f1040.line16` |
|---|---|---|---|
| K1 | interest 10,000; parent MFJ, line-15 150,000, tax 22,828 (TCW 150,000×.22−10,172) | L1 10,000; L3 7,300; L4 8,650; L5 7,300; L8 157,300; L9 24,434; L11 1,606; L13 1,606; L14 1,350; L15 136; L16 1,742; L17 868 | **L18 1,742** (larger_of → 16) |
| K2 | as K1, parent single, TI 40,000, tax 4,565 | L8 47,300; L9 5,441; L11 876; L16 1,012; L17 868 | **1,012** (parent status binding) |
| K3 | interest 61,350; parent MFJ, TI 0, tax 0 | L4 60,000; L5 58,650; L9 tax(58,650 MFJ) 6,564; L16 6,700; L17 tax(60,000 single) 8,120 | **8,120** (larger_of → 17) |
| K4 | qualified dividends 6,000 (all qualified); parent MFJ 150,000 | WS #1: .ratio 1.000/0; ws6 2,700; QD5 3,300; L8 153,300 with QD 3,300 → QDCG MFJ: 22,828 + 495 = 23,323; L11 495; L14 1,350 holding QD 2,700 → QDCG line 5 = 0 → L15 0; L17 QDCG 0 | **495** |
| K5 | wages 7,000; traditional IRA deduction 7,000; qualified dividends 12,000; parent MFJ 150,000 | line 9 19,000; AGI 12,000; std 7,450; TI 4,550; L1 = 19,000 − 7,000 = 12,000; L3 9,300; **L5 4,550 < L3 → WS #3**: w4 1.000, w14 = 12,000/12,000 = 1.000, w15 7,450, w16 7,450, w17 0 → QD5 4,550; L8 154,550 → QDCG 22,828 + 682.50 = 23,510.50; L11 682.50; L14 0 → L15 0; L17 0 | **682.50** (smaller_of → 4; WS #3) |
| K6 | Persimmon (i8615 p. 4 and p. 8): Sharon line 5 3,000, line 7 6,000. Facts: interest 5,700; parent MFJ, TI 100,000, tax 11,828 | L8 109,000; L9 13,808; L11 1,980; **L12a 9,000; 12b .333**; L13 659.34; L14 1,350 → 136; L16 795.34; L17 438 | **795.34**; lines 7, 12a, 12b are **class A** (the example); the rest regression |
| K7 | wages 4,000, interest 10,000; parent MFJ 150,000 | std 4,450; TI 9,550; L1 10,000; L5 7,300; L11 1,606; L14 2,250 → 226; L16 1,832; L17 958 | **1,832** (earned income removed from L1) |
| K8 | QD 3,000, cap. gain distributions 4,000 (7a), interest 3,000; parent MFJ, TI 150,000, QD 2,000 (tax 22,688 by QDCG) | WS #1: w4 .300, w5 .400, ws6 810, ws7 1,080 → QD5 2,190, NCG5 2,920; L8 157,300 with QD 4,190, NCG 2,920 → line 5 of QDCG 150,190 → 22,869.80 + 1,066.50 = 23,936.30; L11 1,248.30; L14 1,350 (QD 810, NCG 1,080) → 0; L17 166 | **1,248.30** |
| K9 | refusal: K1 + parent tick "Schedule D Tax Worksheet" | — | `f1040.line16` refusal `f8615.parent_special` |
| K10 | not asked: K1 facts but born 2001 (24) | `person.edu_kid_age` false | `f1040.line16` 868 (normal); no 8615 question asked |

**P — Form 8814 (if built)**

| id | facts | expected |
|---|---|---|
| P1 | **Fred** (i8814 p. 3, class A): QD 2,190 (2a = 2b), CGD 610 | L4 2,800; L6 100; 3-place ratios .782/.218 → L9 78.20, L10 21.80 (the example prints .78/.22 → $78/$22: A8); L12 0; L14 1,450 → **L15 135** |
| P2 | interest 2,000 only | L4 ≤ 2,700 → L6 0; L14 650 → **L15 65**; no income added |
| P3 | interest 5,000, QD 3,000, CGD 1,000; parent MFJ wages 80,000 | L6 6,300; L9 2,097.90 (.333); L10 699.30 (.111); L12 3,502.80; L15 135. Parent AGI 86,300; TI 54,800; QDCG MFJ: tax(52,002.80) 5,766 → **f1040.line16 5,901** |
| P4 | interest 14,000 | refusal (line 4 ≥ 13,500) |

**Branch coverage** (protocol 5.2):
- K1/K3: both sides of `larger_of` 16/17.
- K1/K5: both sides of `smaller_of` 3/4.
- K4/K5: the WS #1 vs #3 `choose`.
- D3/D4: `smaller_of` at 4a.
- D1/D3: the earned > 900 `choose`.
- D7: line 5 = 0.
- K6: line 7 > 0.

**Mutation pins expected** (EQUIVALENT_IF with argument):
- (i) `sa.dep_over` gt→ge at exactly 900: both branches give 1,350.
- (ii) `f8615.line13` with line 7 = 0: the ratio is 1.000, so it equals line 11.
- (iii) 8615 line 15 when L14 = 0: tax(0) = 0.
- (iv) 8814 line 15 lt→le at 1,350: 10% × 1,350 = 135.
- (v) prorate cap at 1.000 in WS #1 lines 4–5: the ratio is ≤ 1 by construction when QD ≤ line 1.

**Restated expected values** (must be pre-authorized; decision 1) [V cases]:
- `sa.json` `stage4.refuse.standard.dependent` and `stage4.refuse.dependent_itemizes`;
- `f1040.json` `stage9.eic.refuse.dependent_of_another`;
- `mutation.json` `m3.scope.l16_f8615_{single,hoh,qss,mfs}`;
- coverage row `scope.f8615`.
- Class M cases that set `sa.dependent: true` and may now evaluate further [I]: `classm.json` `eic.9`, `clcw.3`,
  `tipjob.1`; `classm.deepseek.json` `sa.5`, `f4952.3`, `clcw.3`, `f8889.1`. The lane runs them and lists each change.

**External engines** [V source grep]:

| Engine | Dependent std deduction | Form 8615 | Form 8814 |
|---|---|---|---|
| Tax-Calculator | yes (`StdDed`, DSI flag) | no (only §59(j) kiddie AMT) | — |
| PolicyEngine-US | probably yes (`basic_standard_deduction` reads dependency) [I] | no | — |
| UsTaxes | yes, but uses **wages only** as earned income (would differ on D3, D6, D7, a cited cause) | no (`// TODO: support 8615`) | a stub that returns 0 |
| OpenTaxSolver | no ("Does not handle if someone claims you") | no | no |

So D is class-C checkable on three engines. **8615 and 8814 have no engine**: state this as a gap in the trust statement.

---

## 6. 2026

`changes/2026/` exists and 2026 is not adopted → protocol 7.1 [V].

**D**
- **Line 3:** the amounts follow `sa.standard_base`. Rev. Proc. 2025-32 p. 19 gives $16,100/$32,200/$24,150; the
  existing year changes cover the base.
- **1,350 / 450 / 900:** unchanged (rp-25-32 p. 19 §.14(2)), so `no change` rows for `sa.dep_min`, `sa.dep_add` and
  `sa.dep_earned_test`.
- The i1040gi 2026 worksheet is not posted, so the citation locators await it.
- Write `changes/2026/sa.<round>-dep.yaml` (a split file; `sa` already has `changes/2026/sa.yaml`) only for citation
  edits, once the instructions post.

**K**
- `f8615.base` 2,700 is unchanged (rp-25-32 p. 13: $1,350, doubled on the form).
- QDCG ceilings for the `qdcg_ceiling` table: 49,450/98,900/66,200; 545,500/613,700/306,850/579,600 (rp-25-32 p. 14).
  Add them as table operations in `changes/2026/qdcg_amount.yaml`, or extract them at adoption. Check that the existing
  `qdcg` 2026 operations use the same values.
- The 2026 f8615 and i8615 are not archived: record them as awaited.

**P:** $1,350 / $2,700 / $13,500 are unchanged (rp-25-32 p. 13). The 2026 f8814 and i8814 are awaited.

**Change ids:** `C-<ROUND>-SA-01..`, `C-<ROUND>-F8615-01..`, `C-<ROUND>-QDCGA-01`, appended to
`research/ty2026/changes.md`. Run `year_changes.py --check` and `year_shared_refs.py --year 2026`. No paid review on
the 2026 operations.

---

## 7. Lane split (protocol 8)

| Batch | Lane | Model / class | Owns (claims) | Ranked work |
|---|---|---|---|---|
| 1 | **D** `<r>-dep` | Opus / judgment | `sa`, `eic`, `f8962` (+ `person` if the sav_claimed gate is approved) | 1. dependent worksheet lines and params; 2. remove the refusals; 3. f8962 gate; 4. fixtures D1–D9 and restatements; 5. coverage rows and persona 14; 6. sav_claimed gate (optional) |
| 1 | **Q** `<r>-qdcga` | Opus / judgment (small; could be Sonnet/mechanical given a full spec) | new `qdcg_amount`, the new table | 1. def; 2. table and its check; 3. the equivalence fixture vs `qdcg` |
| 2 | **K** `<r>-k8615` (cut after batch 1 merges; its fixtures need D's unlock) | Opus / judgment | new `f8615`, `scope`, `f1040` | 1. lines 1–18 with #1; 2. f1040 line 16 and scope retirement; 3. interview topic 277 and rows; 4. fixtures K1–K10; 5. WS #3; 6. line 7 / other children; 7. 2026 operations |
| 3 (optional) | **P** `<r>-f8814` | Opus / judgment | new `f8814`, `s1`, `sd`, `sb`, `f8960`, `f4952`, `f1040` (after K merges) | lines and totals; tick eligibility; P1–P4; EIC keeps its refusal |
| after 1 | **E** `<r>-eng` | Sonnet / mechanical | `tools/engines/*`, `engine/src/generate.ts` (full tier) | generate claimable filers; map the std deduction for TC, PE and UsTaxes; record the UsTaxes wages-only cause |
| any | ruling / bookkeeping | Sonnet / mechanical | — | — |

- **Inputs claim:** D, Q and K all add inputs, so commits are serialized by the integrator per protocol 8.1.
- **Collisions:** no two lanes in one batch share a form file. `f1040` belongs to K in batch 2 and to P in batch 3.

**Reviews** (protocol 6.1; the dry-run estimate was **not run**):

| Subject | Kinds | Count |
|---|---|---|
| new `f8615` | transcription, render, class M (whole) | 3 |
| new `qdcg_amount` | transcription, class M (render if defs render) | 2–3 |
| new `f8814` (if P) | T, R, M | 3 |
| `sa` | T (line-scoped), M, R (label) | 3 |
| `f1040` | T, M (and R for the line-16 refusal text) | 2–3 |
| `scope` | T, M | 2 |
| `eic` | T | 1 |
| `f8962` | T, M | 2 |
| `person` (if gated) | T | 1 |
| screen review (kind gate) | `f8962.dependent_filer`, `f8615.*` residuals (~5) | 1 sample per milestone |
| question reviews | ~10 (K) + 1 (sa.dependent help) + ~8 (P) | ~19 |
| completeness / false-no | f8615 (and f8814) | sampled |

That is about 17–21 form-level review runs plus the sampled ones.

**New York (7.4):** dependent returns become computable in NY through `ny_it201.item_c`, which reads `sa.dependent`
[V]. The $3,100 path is encoded but has never been reached [I]. The lane runs `test-fixtures --ny` and `ny_compare`, and
reports. NY has no kiddie tax.

---

## 8. Risks and decisions for the owner

**Decisions**
1. **Pre-authorize the expected values and coverage-row ends that change by design** (§5 list). Protocol 8.4 forbids a
   lane to edit them, but a coverage expansion has to. The plan row should name each one.
2. **Under-16 gate** (`household.filer_under16`, amb.2025.filer_under_16). Its stated reason ("Form 8615 is refused
   only when the filer knows to answer") falls away with K.
   - Keeping it leaves out children under 16, a large part of 8615 filers [I]. It also makes i8615's Amanda example
     (age 13) unusable as a class A case.
   - Options: keep; lift; or lift only for claimable filers.
3. **QDCG at a bound status:** (a) keyed table [recommended], (b) a choose over unkeyed parameters, (c) an engine atom
   change.
4. **8814:** build in batch 3, or keep it refused. It is unmeasured, touches 7 shared forms, and EIC+8814 stays refused
   without Pub 596.
5. **Reuse of the Form 8863 line 7 questions** for 8615 conditions 3 and 4, accepting A4's exact-half boundary
   difference, versus asking 8615's own wording.
6. **8615 other children** (line 7): support in v1, or refuse.
7. **`person.sav_claimed` gated on `sa.dependent`:** it removes a question for non-dependent students (N8), but it is a
   shared-file edit.

**Risks**
- R1: Form 8615 needs another person's return figures. Wrong copying is the main error source, and no review can catch
  it. The help must point to exact lines.
- R2: Line 9 QDCG/table rounding with the parent status. The table midpoints mean line 16 can exceed line 17 by $1
  even when rates are equal. That is expected and not a bug.
- R3: Stale coverage estimate (protocol 1.1 [unverified]). Refresh before claiming +3.9.
- R4: **Child AMT.** The §59(j) exemption cap is not in the archived 2025 i6251 (grep for "child", "9,750", "8615"
  found nothing relevant [V]). It is in rp-25-32 §.11 for 2026 [V].
  - A large 8615 child may owe AMT, and the only screen (`s2.amt_owed`) relies on the filer knowing.
  - Archive Rev. Proc. 2024-40 and decide whether to add a screen for 8615 children.
- R5: HOH with a claimable filer. The qualifying-person interplay is not checked [I]. Add a fixture before release.

**Ambiguities to enter** (ids prefixed by form):
- A1 `amb.2025.sa_dep_qss`: worksheet line 3 omits QSS. Choose: refuse as a contradiction (Pub 501 p. 11).
- A2 `amb.2025.sa_dep_earned`: read the "Generally" formula as written; 8r counts (Pub 501 p. 24).
- A3 `amb.2025.f8615_required_to_file`: condition 2 is not computed.
  - A non-dependent who is not required to file has gross income below the basic standard deduction, so AGI ≤ gross
    income gives TI 0 and line 5 = 0. Moot.
  - A non-blind dependent with line 1 > 2,700 has unearned income > 1,350, so it is required (Chart B, p. 10).
  - A blind dependent → refuse.
- A4 `amb.2025.f8615_support_boundary`: i8863 "less than one-half" vs i8615 "didn't have…more than half" (exactly half).
- A5 `amb.2025.f8615_earned`: 8615 earned income = line 1z + Sch 1 line 3 ("generally", i8615 p. 2). The 30% rule for
  a capital-intensive business is not modeled; it could be refused via a Sch C question if wanted.
- A6 `amb.2025.f8615_alt_worksheet`: with an SE loss, the Alternate Worksheet = line 9 − 1z − line 3 − line 18, the
  same formula (algebra; NOL and 2555 are already refused).
- A7 `amb.2025.f8615_line11_negative`: line 9 < line 10 is possible if the parent's reported tax is not the tax on line
  6 (e.g. it includes other line-16 items). Floor at 0, or keep it signed?
- A8 `amb.2025.f8814_ratio_places`: the form says "at least three places", but the Fred example uses .78/.22 → $78/$22.
