# Design scout: married filing separately (MFS), tax year 2025, federal

Scout: claude-opus-5-5, class judgment, year 2025, jurisdiction us. Read-only; tree read:
`.claude/worktrees/sweep-tasks` (HEAD 63a20efc). Nothing in the repository was changed.

Marks: **[V]** = read in the archived source or in the repository file named; **[I]** = inferred (reasoning, a
grep count, or memory) and to be confirmed by the encoding lane.

---

## 0. Summary

- MFS is refused today by one gate, `s3.mfs` (`forms/2025/s3.yaml` line 1309, `f1040.status == mfs`), at four
  refusal sites: `scope.ready_credits` (scope.yaml l.1197, the return-wide one), `s3.line11` (s3.yaml l.1372),
  `f2441.line11` and `f2441.line26` (f2441.yaml l.988, `&mfs` anchor) [V]. Other MFS-specific refusals:
  `f8889.mfs` (on `f8889.line13_figured`), `s179.mfs`, `sa.mfs_spouse_extra`, `clcw.spouse_screen` [V].
- Most MFS arithmetic is **already encoded, latent**: every status-keyed parameter has an `mfs` value
  (qdcg ceilings, TCW Section C, tax table `mfs` column, SALT $20,000/$250,000/half, $1,500 loss limit, Medicare and
  NIIT $125,000, CTC $200,000, saver's $39,500 and rate table, EIC "other" columns, QBI $197,300, foreign tax $300,
  standard deduction $15,750 and $1,600 boxes, IRA $10,000, PTC Table 5) [V, `params/2025.yaml`, `tables/2025/*`].
  Status branches for MFS exist in ssb, eic, s1a (tips, overtime, senior zero; car loan $100,000), sli (ineligible),
  sa (spouse itemizes, SALT half), s179, refund (2024 MFS), household [V].
- What is **missing or wrong when MFS is reached** (each verified in the form file):
  1. `household.filing_status_conflict` gives `household.no` for mfs, so an MFS filer answering "not married at the end
     of 2025" is accepted (the defaults audit found 47 MFS test cases that answer `household.married_dec31: false`)
     [V household.yaml; docs/2026-11-11_test_data_defaults_audit.md l.85].
  2. No community-property refusal for MFS (`household.hoh_community_property` returns `household.no` for mfs) [V].
  3. `person.ira_line2` gives $10,000 for every MFS filer; the worksheet gives $89,000 if lived apart all year, and a
     non-covered MFS filer whose spouse is covered is "considered covered" unless lived apart all year [V i1040gi
     pp. 96–97]; neither rule is encoded [V person.yaml l.3500–3580].
  4. `f2441.line19` takes line 18 (own earned income) for MFS; the instructions give the spouse's earned income unless
     the filer is "considered unmarried" [V f2441.yaml l.1198; i2441 p. 5]; no line A, no $2,500 cap (`f2441.exclusion_max`
     is $5,000 flat) [V].
  5. Form 8863: no MFS bar except the return-wide refusal (`f8863.eligible` = paid ∧ none claimed) [V f8863.yaml l.65].
  6. Form 8962: no MFS "not an applicable taxpayer" rule and no line A [V f8962.yaml `f8962.applicable`].
  7. Form 1040 line 12b ("Spouse itemizes on a separate return") and Schedule 1 line 20's lived-apart box are not
     lines [V f1040.yaml, s1.yaml; f1040 p. 2; f1040s1 l.20].
  8. The mortgage-limit refusal question names $750,000 / $1,000,000; MFS limits are $375,000 / $500,000 [V
     questions.yaml l.792–797; i1040sca p. 8].
  9. A child who is also the spouse's qualifying child refuses at `dependent.qc_tiebreak` [V dependent.yaml l.1767]:
     most MFS parents who live together would be refused there.
  10. Wording that assumes a joint return: 10 help strings "Enter the amounts of all your and your spouse's Forms
      1099-DIV combined" (questions.yaml l.149–181, 403) [V]; 57 bank lines and 31 input sources mention the spouse
      without "joint/separate/together" [V count; relevance per line I].

---

## 1. Scope

### 1.1 Becomes computed

An MFS return of a resident filer domiciled outside a community property state, with every line in scope today,
including [V source for each rule]:

| Rule | Source (2025, archived) | Where |
|---|---|---|
| Filing status MFS; spouse's name and SSN on the return | i1040gi p. 14, Married Filing Separately | presentation notice only (no name/SSN lines exist) |
| No deduction for tips, overtime, enhanced senior; no SLI; no education credits; EIC and CDCC very limited; no standard deduction if spouse itemizes | i1040gi p. 14; Pub 504 p. 4 items 1–11 | s1a, sli, f8863, eic, f2441, sa |
| Line 12b and zero standard deduction when spouse itemizes | i1040gi p. 33 Line 12b; p. 34 Exception 2 | new f1040.line12b; sa.standard (exists) |
| If one spouse itemizes the other should too | Pub 504 p. 4 "Itemized deductions" | notice |
| Joint expenses on separate returns (Table 1) | Pub 504 pp. 4–5 Table 1 | help text only |
| Joint estimated payments divided as agreed | Pub 504 p. 22 | help text on f1040.line26 |
| SALT $20,000; threshold $250,000; floor $5,000; worksheet line 10 half | i1040sca pp. 1, 3, 7 | sa (exists) |
| Mortgage limits $375,000 / $500,000 | i1040sca p. 8 | refusal question wording |
| Capital loss limit $1,500 | i1040sd p. 3; f1040sd line 21 | sd (exists) |
| SSB: $25,000/$9,000 if lived apart all year; else line 7 × 85% | i1040gi pp. 31–32 | ssb (exists); line 6d |
| IRA: line 2 $89,000 if lived apart all year, $10,000 otherwise; considered covered via spouse unless apart all year; Schedule 1 line 20 box | i1040gi pp. 96–97 | person/ira, s1 |
| Dependent care: line A (considered unmarried: apart last 6 months, home of the qualifying person > half year, paid > half the cost); otherwise no credit, exclusion with spouse's earned income on line 19 and $2,500 on line 21 | f2441 line A, lines 19, 21; i2441 pp. 1, 2, 5; Pub 503 pp. 8–11 | f2441 |
| EIC only with a qualifying child and the separated-spouse rule | i1040gi p. 41 Step 3 q. 3–6, p. 44 | eic (exists) |
| PTC: not an applicable taxpayer unless Exception 2 (abuse/abandonment, line A, 3-year limit); repay APTC up to Table 5 "other" column | i8962 p. 7; p. 18 Table 5 | f8962 |
| Additional Medicare and NIIT thresholds $125,000 | f8959/i8959; i8960 pp. 2–3 | (exist) |
| CTC/ODC threshold $200,000; saver's $39,500; car loan $100,000; QBI $197,300; SEP/SIMPLE none | f1040s8812; f8880; f1040s1a line 26; i8995 | (exist) |
| HSA when the spouse has no HSA and no HDHP of their own | i8889 pp. 4–5, Line 6 | f8889 (narrowed gate) |
| Child who is also the spouse's qualifying child, the spouse not claiming | Pub 501 p. 15, Tiebreaker rules ("both parents claim") | dependent (design D3) |

### 1.2 Stays refused (gate, reason)

| Situation | Gate | Reason |
|---|---|---|
| MFS and lived in a community property state in 2025 | **new** `household.mfs_community_property` | community income split, Form 8958, Pub 555 (not archived); owner precedent amb.2025.hoh_community_property (decision 10, 2026-10-22) [V] |
| Registered domestic partner NV/WA/CA; CP marriage ended | `household.rdp_community_property`, `household.cp_marriage_ended` (exist) | unchanged |
| Section 179 election or carryover on MFS | `s179.mfs` (exists; "owner: refused", s179.yaml l.157) | spouse's property and allocation |
| Spouse's age/blind boxes on MFS | `sa.mfs_spouse_extra` (exists) | rare; owner decision D4 (could be computed with two Bool inputs) |
| HSA when the spouse had their own HSA or own HDHP | `f8889.mfs`, narrowed | family-coverage division (i8889 Line 6, rules 1–6) |
| Capital loss carryover from a joint prior return | `clcw.spouse_screen` (exists) | allocation by net losses (i1040sd p. 10) |
| PTC policy shared with the spouse's tax family | `f8962.alloc` (exists) | Part IV, half the APTC (i8962 p. 7 "repay half") |
| Child claimed by both spouses (tie-breaker by time or AGI) | `dependent.qc_tiebreak` (exists) | design D3 |
| All refusals that already exist for other statuses | unchanged | |

### 1.3 Gates that go away or narrow

- **Removed**: `s3.mfs` as a refusal at `scope.ready_credits`, `s3.line11`, `f2441.line11`, `f2441.line26`. Keep the
  line `s3.mfs` as a plain Bool helper (readers: f2441 refusals, scope) or delete it after its readers move to
  `sa.mfs`/`household.mfs`; it is listed in `tools/coverage/categories.json` l.62 and `tree.json` l.36 [V].
- **Narrowed**: `f8889.mfs` (all MFS with Form 8889 → MFS with a spouse's own HSA/HDHP).
- **New**: `household.mfs_community_property`.
- **Reworded**: `household.widowed_this_year` remedy ("or a separate return, which this tool does not support",
  f1040.yaml l.412) and `refusal_notes.yaml` `s3.mfs` note (becomes the note for the new CP gate).

### 1.4 Share of filers

- MFS: **2.6% of returns** (4,139,858 of 160,602,107, SOI 2023 Table 1.2, `soi-23in12ms`); gain if covered alone now
  **+2.1 points**; step 4 of the roadmap (+2.5 after steps 1–3) [V `reports/2025/filer_coverage.md` l.31, l.45].
- Community property states: about 31% of US population (CA, TX, AZ, WA, NV, NM, ID, LA, WI) — **estimate from memory
  of 2024 census figures [I]**; no archived source splits MFS returns by state. Residual sub-refusals (s179, HSA with
  spouse's HSA, shared PTC policy, spouse boxes, joint-carryover, both-claim) are small [I].
- **Expected gain ≈ +1.3 to +1.5 points [I]** (2.1 × ~0.69, less residuals). The CP gate is unmeasured
  (no IRS count); `categories.json` should map the `mfs` category to the new set of gates and the report will show the
  CP share as unmeasured unless the owner accepts a population-share estimate.

---

## 2. Sources

### 2.1 2025 (all archived unless marked)

| Doc | Pages used | Status |
|---|---|---|
| i1040gi | p. 13–15 filing status, MFS, HOH, live apart; p. 23 community property; p. 31 line 6d; p. 32 SSB worksheet; p. 33 line 12b; p. 34 Exception 2; p. 41, 44 EIC Step 3 and separated spouses; pp. 96–98 IRA worksheet and SLI; p. 80 TCW Section C | archived [V] |
| f1040 | p. 1 filing status, separated-spouses box; p. 2 lines 6d, 12a–12e | archived [V] |
| f1040s1 | line 20 box | archived [V] |
| f1040s1a | Parts II, III, V "If married, you must file jointly"; line 26 $100,000 | archived [V] |
| i1040sca / f1040sa | pp. 1, 3, 7 SALT; p. 8 mortgage limits; p. 4–5 sales tax election coordination (refused) | archived [V] |
| Pub 504 | p. 4 MFS special rules 1–11, itemized deductions; pp. 4–5 Table 1; p. 22 joint estimated payments, community income; pp. 23–24 spouses living apart all year (§66) | archived [V] |
| Pub 501 | pp. 6–9 considered unmarried, temporary absences; p. 15 tiebreaker rules | archived [V] |
| f2441 / i2441 / Pub 503 | line A; lines 5, 19, 21; i2441 pp. 1, 2, 5; Pub 503 pp. 8–11 | archived [V] |
| i8863 | p. 3, "Who cannot claim a credit", item 2 | archived [V] |
| i8962 / f8962 | p. 7 Married taxpayers, Exceptions 1–2, MFS; p. 18 Table 5 | archived [V] |
| i8889 | pp. 4–5 Line 3 rules, Line 6, Line 7 | archived [V] |
| p590a | MFS IRA tables (pp. 13–20) for cross-check | archived [V presence; pages not read] |
| i4562 p. 5 | line 5 MFS (kept refused) | archived [V] |
| **Pub 555 (2025)** | community property | **to archive** if D1 chooses computing CP |
| **Pub 915 (2025)** | "lived apart at all times" for SSB and temporary absence | **to archive** (ambiguity amb.2025.mfs_lived_apart) |
| Pub 936 | mortgage limits detail | not needed (i1040sca p. 8 suffices) |

### 2.2 2026 editions [V `sources/2026/manifest.json` listing]

- Archived drafts: f1040 (line 12b and 6d unchanged; separated box; 12d birth 1962; new 12f non-itemizer charity),
  f1040s1 (line 20 box), f1040s1a, f1040sa ($20,200 / $252,500 MFS), f2441 (line A; line 21 $7,500 / $3,750),
  f8962 (line A; lines 28–29 reserved), f8889, f8863, i2441, i8889, i8863, i8962, p590a, p503 [V grep].
- Not posted / not archived: **i1040gi 2026** (the MFS disallowance list of p. 14), i1040sca 2026, Pub 504 and Pub 501
  2026. The 2026 MFS rules for tips, overtime and senior rest on `plaw-119-21` (archived) [I: sections not read].

---

## 3. Encoding plan

Conventions followed: gate lines `<child>_if_<cond>`; `choose` with exhaustive guards over the five statuses
(household.yaml pattern); every line `cite`; Bool `(gate)`/`(helper)` printed tags [V household.yaml, sa.yaml].

### 3.1 household.yaml / params (lane L1)

| id | printed | type | expr sketch | cite |
|---|---|---|---|---|
| `household.mfs` | (helper) | Bool | `f1040.status == mfs` | i1040gi p. 14 MFS |
| `household.mfs_living` | (helper) | Enum(mfs_living) | input; values `together_late` (lived together at some time Jul–Dec), `apart_last6` (together only before July), `apart_all_year`; gated_by `household.mfs_living_if_mfs` | i1040gi p. 15 Married persons who live apart; p. 32 line 8; p. 97 line 2; Pub 501 p. 9 temporary absences |
| `household.mfs_living_if_mfs` | (gate) | Bool | choose on `household.mfs` | same |
| `household.mfs_apart_all_year` | (helper) | Bool | mfs ∧ mfs_living == apart_all_year | i1040gi p. 31 line 6d, p. 97 |
| `household.mfs_apart_last6` | (helper) | Bool | mfs ∧ mfs_living ∈ {apart_last6, apart_all_year} | i2441 p. 2; i1040gi p. 41 q. 4 |
| `household.mfs_community_property` | (gate) | Bool | choose status: mfs → `household.community_property`; others → `household.no` | i1040gi p. 23; Pub 504 p. 22 |
| `household.filing_status_conflict` | (gate, changed) | Bool | mfs alternative: `household.no` → `household.joint_unmarried` (as mfj) | i1040gi p. 14 "if you are married at the end of 2025"; p501 p. 6 spouse died |
| `household.hoh_community_property` | unchanged | | mfs alternative stays `household.no` (the new gate covers it) | |

Refusal: `household.mfs_community_property` on `f1040.status`'s `refuses:` beside `cp_marriage_ended` (f1040.yaml
l.39), form "Community income on a married filing separately return (Form 8958; Pub. 555)", cite i1040gi p. 23 and
Pub 504 p. 22 "If you and your spouse file separate returns, you must report half of any income described ...".
Order the entry first on that line so the refusal arrives right after the status (protocol 3.5, N11).

Params: enum `mfs_living` (cite i1040gi p. 15); `ira.line2_apart` = 8,900,000 (i1040gi p. 97, "married filing
separately and you lived apart ... enter $89,000"); `dc.exclusion_max_mfs` = 250,000 (i2441 p. 5 Line 21). (L1 owns
`params/2025.yaml`; L2/L3 request their params.)

### 3.2 scope.yaml, s3.yaml, f1040.yaml, ssb.yaml, eic.yaml (lane L1)

- `scope.ready_credits`: delete the `s3.mfs` refusal entry. `s3.line11`: delete its `refuses:` (s3.line11 is a sum over
  persons; on MFS only the taxpayer) [V].
- `f1040.line12b` (new, printed "12b", Bool): copy `sa.mfs_spouse_itemizes`; cite f1040 p. 2 line 12b, i1040gi p. 33.
  Readers: none (display); `sa.standard` already zeroes.
- `f1040.line6d`: read `household.mfs_apart_all_year` (now reads `ssb.lived_apart`). Ambiguity: print whenever MFS
  apart all year, or only with benefits (amb.2025.mfs_lived_apart_boxes).
- `ssb.lived_apart`: input → derived line = `household.mfs_apart_all_year` (protocol 3.1/3.3: id kept, no reader
  changes; `ssb.lines8_to_15`, `ssb.mfs_together`, `ssb.line8`, `ssb.line10`, `ssb.line16` unchanged).
- `eic.same_home`: for MFS derived (`together_late` ⇔ same principal residence for the last 6 months); keep the input
  for married HOH. Implement as `eic.same_home` = choose(mfs → `household.mfs_living == together_late`, else
  `eic.same_home_input`) — rename the input `eic.same_home_input` (bank entry follows). `eic.legally_separated` unchanged.
- `household.widowed_this_year` remedy text (f1040.yaml l.412): point to the MFS line.

### 3.3 sa.yaml, s1.yaml, sli.yaml, ira.yaml, person.yaml (lane L2)

- `sa.spouse_itemizes` (exists): reword source to the fact ("Is your husband or wife itemizing deductions on their own
  2025 return instead of taking the standard deduction?"); cite i1040gi p. 33 Line 12b, Pub 504 p. 4.
- `sa.mortgage_over_limit`: add `sa.mortgage_over_limit_mfs` (Bool input, "... more than $375,000 ($500,000 if all
  borrowed on or before December 15, 2017) ...", cite i1040sca p. 8) and make `sa.mortgage_over_limit_if_interest`
  choose by `sa.mfs`. Same refusal, same gate line (3.1 technique keeps the refusal id).
- `sa.spouse_extra`: keep refused (D4) or compute with `sa.spouse_age65`, `sa.spouse_blind` (Bool inputs) feeding
  `sa.standardraw`'s box count; cite i1040gi p. 33 Line 12d, p. 35 chart.
- `s1.line20_box` (new, printed "20 (box)", Bool): `household.mfs_apart_all_year`; cite f1040s1 line 20, i1040gi
  p. 96 "check the box on line 20".
- `sli.any`: gate it `sli.any_if_eligible_status` (status ≠ mfs ∧ not dependent) so the question is not asked on MFS
  (N8); `sli.eligible` unchanged [I that sli.any is reached on MFS today: `sli.deduction` chooses on `sli.has` first,
  l.602].
- IRA (person.yaml l.3500–3580, ira.yaml):
  - `ira.mfs_spouse_covered` (new input, Bool, gated_by `ira.mfs_spouse_covered_if_asked` = mfs ∧ ¬apart_all_year ∧ any
    taxpayer with `person.ira_cov` false and a traditional contribution): "Was your husband or wife covered by a
    retirement plan at work in 2025?"; cite i1040gi p. 96 "Married persons filing separately".
  - `person.ira_cov_effective` (helper): `person.ira_cov` ∨ `ira.mfs_spouse_covered_if_asked`; every reader of
    `person.ira_cov` on the worksheet's line 1a path switches to it (lane lists readers first).
  - `person.ira_line2_status`: choose(`household.mfs_apart_all_year` → param `ira.line2_apart`; else `ira.line2`).

### 3.4 f2441.yaml, f8863.yaml, f8962.yaml, f8889.yaml (lane L3)

Form 2441:
- `f2441.line_a` (new, printed "A", Bool): mfs ∧ `household.mfs_apart_last6` ∧ `household.home_cost` ∧ (some
  qualifying person whose main home was the filer's for more than half of 2025: the dependent's existing lived-half
  line, e.g. `dependent.lived_half` [I id]); cite f2441 line A; i2441 p. 2.
- `f2441.mfs_married` (helper): mfs ∧ ¬line_a.
- `f2441.line19`: choose(joint → spouse_earned_b; `f2441.mfs_married` → `f2441.mfs_spouse_earned`; else line 18).
  `f2441.mfs_spouse_earned` (new NonNegDollars input, gated on `f2441.mfs_married` ∧ benefits > 0); cite i2441 p. 5
  Line 19 "No. Enter your spouse's earned income".
- `f2441.line5` unchanged (MFS with line A = "all others").
- `f2441.exclusion_cap` (helper): choose(`f2441.mfs_married` → `dc.exclusion_max_mfs`; else `dc.exclusion_max`);
  `f2441.line21` takes the smaller of it and `f2441.plan_max`.
- Credit: `f2441.credit_allowed` = ¬`f2441.mfs_married`; `s3.line2` (or `f2441.line11`) zero when false; ambiguity
  amb.2025.f2441_mfs_no_credit (line 11 zero vs. Part II not completed). Delete the two `s3.mfs` refusals.
Form 8863:
- `f8863.eligible`: add status: choose(mfs → `f8863.no`; else current). Gate `f8863.paid` by a new
  `f8863.paid_if_not_mfs` and switch its readers (f8863.yaml l.76–82; dependent.yaml l.2339–2345; f1040.yaml l.918) so
  the question is not asked on MFS; cite i8863 p. 3 item 2.
Form 8962:
- `f8962.line_a` (new, printed "A", Bool) = mfs ∧ `f8962.mfs_exception` ∧ ¬`f8962.mfs_three_years`; both new inputs gated
  on mfs ∧ `f8962.any`; cite i8962 p. 7 Exception 2 and "3-year limit".
- `f8962.applicable`: and-in (status ≠ mfs ∨ line_a). The not-applicable path already exists (owner decision D7(a),
  amb.2025.ptc_not_applicable: line 24 zero, column (f) only) [V]; i8962 p. 7 states the MFS rule explicitly ("complete
  lines 1 through 5 ... Skip lines 7 through 8b ... complete only column (f)").
- `f8962.marriage` unchanged. Table 5 "other" column for MFS [V params].
Form 8889:
- `f8889.mfs_spouse_hdhp` (new Bool input, gated on mfs and the Form 8889 entry): "Did your husband or wife have their
  own HSA, or their own high-deductible health plan, at any time in 2025?"; `f8889.mfs` becomes mfs ∧ that answer;
  cite i8889 p. 4 How To Complete Part I, Line 3 rule 1, p. 5 Line 6. With No, line 6 = line 5 (no spouse HSA).

### 3.5 dependent.yaml (lane L4)

- `dependent.other_only_spouse` (Bool input, gated on mfs ∧ `dependent.other_claimant`): "Is your husband or wife the
  only other person this child could be the qualifying child of?"
- `dependent.spouse_claims` (Bool input, gated on that Yes): "Will your husband or wife claim this child on their
  2025 return?"
- `dependent.tiebreak_other` / `dependent.qc_tiebreak_claimant` and `dependent.eic_tiebreak`: when the only other person
  is the spouse and the spouse does not claim, no tie-breaker arises (Pub 501 p. 15, "both parents claim"); when the
  spouse does claim, refuse at the existing gate (or exclude the child: D3). Ambiguity amb.2025.mfs_spouse_qc.

### 3.6 Interactions (who reads or feeds)

`f1040.status` → household.*, sa.mfs, s179.separate, s1a, sli, eic, ssb, f2441, f8863, f8962, f8889, params by status.
`household.mfs_living` → ssb.lived_apart → f1040.line6b/6d; person.ira_line2 → s1.line20 → f1040.line10;
eic.same_home → f1040.line27a, f1040.separated_spouses; f2441.line_a → s3.line2, f1040.line1e.
`sa.mfs_spouse_itemizes` → sa.standard, sa.itemizes → f1040.line12e, f1040.line12b. `f8962.applicable` → s3.line9,
s2.line1a. Nothing feeds MFS from other forms.

### 3.7 Ambiguity entries (ambiguities/2025.yaml)

| id | text at issue | proposed reading |
|---|---|---|
| amb.2025.mfs_community_property | i1040gi p. 23; Pub 504 p. 22 (domicile "during any part of your tax year") | refuse MFS who lived in a CP state at any time in 2025 (precedent decision 10) |
| amb.2025.mfs_lived_apart | "lived apart from your spouse for all of 2025" (pp. 31, 32, 97) vs. temporary absence (Pub 501 p. 9, for the 6-month rule only); Pub 915 not archived | temporary absences count as living together for both tests |
| amb.2025.mfs_lived_apart_boxes | lines 6d and Sch 1 line 20 boxes | print when MFS apart all year and the line is used |
| amb.2025.f2441_mfs_no_credit | i2441 p. 2 "can't generally take the credit" | line 11 (and Sch 3 line 2) zero |
| amb.2025.mfs_spouse_qc | Pub 501 p. 15 tiebreaker "both parents claim" | spouse not claiming → filer claims, no tie-break |
| amb.2025.mfs_spouse_itemizes | i1040gi p. 33 (the spouse's election, possibly unknown at filing) | ask the fact; notice that both must choose alike |

---

## 4. Interview plan (protocol 2026-11-13)

Typical MFS filer [I]: married, living together, separate finances or liability concerns, one or two W-2s, renter or
co-owner, no Marketplace plan, usually no children claimed or one claimed by agreement. Filer with nothing extra:
one W-2. Refused filer: MFS in Texas or California.

| Q | id | parent / gate | order, seq | prompt (draft) | help (≤40 words) |
|---|---|---|---|---|---|
| 1 | `f1040.status` (exists) | O2 line "Married, and filing apart ..." | 100/2 | unchanged | unchanged |
| 2 | `household.community_property` (exists) | reached first on MFS via the new gate | 100/3 | unchanged ("Did you live in a community property state (Arizona, ...) at any time in 2025?") | "A Yes ends the interview here." (N11: the commonest MFS refusal, alone and first) |
| 3 | `household.married_dec31` (exists) | as for MFJ | 101 | unchanged | unchanged |
| 4 | `household.mfs_living` (new, choice) | mfs, reached when a reader needs it | 102/1 | "Did you live with your husband or wife in 2025?" — "Yes, at some time from July to December" / "Only before July" / "No, not at any time in 2025" | "Time away for work, school, medical care or military service, when you expected to return, counts as living together." |
| 5 | `sa.spouse_itemizes` (exists, reworded) | mfs | 200, first (before group `paid_2025`) | "Is your husband or wife itemizing deductions on their own 2025 return, instead of taking the standard deduction?" | "If they itemize, your standard deduction is zero and you list yours too. If you itemize, they must too. Ask them if you do not know." |
| 6 | `sa.mortgage_over_limit_mfs` (new) | replaces the MFJ wording on MFS | 200/22 | "Did the loans on your home add up to more than $375,000 at any time in 2025, or to more than the home is worth?" | as now, with $500,000 for loans on or before Dec 15, 2017 |
| 7 | `ira.mfs_spouse_covered` (new) | beneath `person.ira_cov` No, mfs, not apart all year | saving topic, after ira_cov | "Was your husband or wife covered by a retirement plan at work in 2025?" | "A 401(k), 403(b), pension or SEP or SIMPLE counts, even if they put nothing in." |
| 8 | `household.home_cost` (exists) | reached for MFS with care expenses (line A) | as now | unchanged | unchanged |
| 9 | `f2441.mfs_spouse_earned` (new) | mfs ∧ ¬line A ∧ W-2 box 10 > 0 | care topic, after box 10 | "How much did your husband or wife earn from work in 2025?" | "Wages (W-2 box 1) plus net earnings from self-employment." |
| 10 | `f8962.mfs_exception` / `f8962.mfs_three_years` (new) | mfs ∧ a 1095-A | Marketplace topic, after the 1095-A | "Are you living apart from your husband or wife now, and unable to file with them because of domestic abuse or because they abandoned you?" / "Did you claim the credit this way on separate returns for 2022, 2023 and 2024?" | i8962 p. 7 definitions, one line |
| 11 | `f8889.mfs_spouse_hdhp` (new, refusing) | mfs ∧ Form 8889 | HSA topic, after coverage | "Did your husband or wife have their own HSA, or their own high-deductible health plan, in 2025?" | "A Yes ends the interview here." |
| 12 | `dependent.other_only_spouse`, `dependent.spouse_claims` (new) | beneath `dependent.other_claimant` on MFS | dependents topic | see 3.5 | "Only one of you can claim a child; agree which." |

Gated off on MFS, never asked (N8): `f8863.paid`, `sli.any`, the tips and overtime parents if reached (lane checks the
walk: `s1a.line13` chooses on `s1a.tips` before the status [V]; gate the parent), `eic.same_home` (derived),
`ssb.lived_apart` (derived).
Wording audit (bank and input sources): replace "all your and your spouse's" with "(on a joint return, yours and your
spouse's)"; add the Pub 504 Table 1 and p. 22 rules to the help of interest, dividends, 1098, property tax and
estimated payments ("On a separate return, enter only your share").
Notices (presentation, cite i1040gi p. 14 and Pub 504 p. 4): enter the spouse's name and SSN on page 1; if you itemize,
your spouse must too.

Refusals remaining in the walk: `household.mfs_community_property`, `household.filing_status_conflict` (MFS not
married), `f8889.mfs`, `s179.mfs`, `sa.mfs_spouse_extra`, `clcw.spouse_screen`, `f8962.alloc`, `dependent.qc_tiebreak`.

Coverage rows (new `interview/2025/coverage/mfs.yaml`, profile full; and `opening.yaml`):
- `opening.separate`: expect **changes** from `refused: s3.mfs` to `proceeds: {f1040.status: mfs}` (owner approval, D2).
- `mfs.community_property` → refused `household.mfs_community_property`; `mfs.not_married` → refused
  `household.filing_status_conflict`; `mfs.spouse_died_2025` → proceeds; `mfs.spouse_itemizes` → asks the Schedule A
  screens, records `f1040.line12b: true`; `mfs.no_education` → not_asked `f8863.paid`, `sli.any`;
  `mfs.ssb_apart` → asks `household.mfs_living`; `mfs.hsa_spouse` → refused `f8889.mfs`; `mfs.s179` → refused
  `s179.mfs`; `mfs.ptc_exception` → asks `f8962.mfs_three_years`; `mfs.dc_benefits` → asks
  `f2441.mfs_spouse_earned`; `mfs.child_spouse_claims` → refused `dependent.qc_tiebreak`; `mfs.spouse_extra` →
  refused `sa.mfs_spouse_extra`.
Personas: `14_mfs_separate_finances` (complete: Ohio, 44, lives with spouse, W-2 $85,000, 1098 share $9,000, property
tax $3,500, spouse itemizes); `15_mfs_separated_parent` (complete: fixture M7); `16_refused_mfs_texas` (refused at the
CP gate). Record walks before and after (protocol 7.1, 7.8).

---

## 5. Fixtures (hand-predicted, 2025)

Common inputs: resident, contiguous US, not in a CP state, born 1985 unless stated, no other income; W-2 box 1 = 3 = 5,
box 4 = 6.2%, box 6 = 1.45% unless stated. Tax from `tables/2025/tax_table.yaml` `mfs` column or TCW Section C [V the
lookups; one hand check: 44,275 midpoint → 1,192.50 + 12% × 32,350 = 5,074.50 → $5,075, matches].

| # | Inputs | Expected (arithmetic) |
|---|---|---|
| M1 basic | W-2 $60,000, box 2 $6,000 | L12e 15,750; L15 44,250; L16 **5,075**; L33 6,000; refund **925** |
| M2 spouse itemizes | M1 + state income tax $3,000; `sa.spouse_itemizes` Yes | 5d 3,000; 5e min(3,000, 20,000) = 3,000; `sa.standard` 0; **L12b true**; L12e **3,000**; L15 57,000; L16 **7,460**; owe 1,460 |
| M3 Medicare + NIIT | W-2 $300,000 (box 6 = 4,350 + 900 = 5,250), interest $20,000 | AGI 320,000; L15 304,250; TCW C: 304,250 × 35% − 30,452.75 = **76,034.75**; 8959: L6 300,000 − 125,000 = 175,000, L7 **1,575**; L19 5,250 − L20 4,350 = L21 **900** → L25c; 8960: NII 20,000, MAGI − 125,000 = 195,000, ×3.8% of 20,000 = **760** |
| M4 SALT phase-down | W-2 $320,000, state tax $25,000, 1098 $12,000 | SALT wks: L1 40,000; L4 320,000; L5 250,000; L6 70,000; L7 21,000; L8 19,000; L9 19,000; L10 half = **9,500**; itemized 21,500; L15 298,500; tax 298,500 × 35% − 30,452.75 = **74,022.25** |
| M5 SSB together | SSA box 5 $20,000; W-2 $30,000; born 1962; together_late | L1 20,000; L2 10,000; L3 30,000; L5/L7 40,000; L16 = 40,000 × 85% = 34,000; L17 17,000; **L6b 17,000**; 6d false; AGI 47,000; L15 31,250; tax **3,515** |
| M6 SSB apart | M5 with apart_all_year | L8 25,000; L9 15,000; L10 9,000; L11 6,000; L12 9,000; L13 4,500; L14 4,500; L15 5,100; L16 9,600; **L6b 9,600**; **6d true**; AGI 39,600; L15 23,850; tax **2,627** |
| M7 separated parent | W-2 $20,000, box 2 0; child born 2019 lived with filer all year; apart_last6 (together Jan–Apr); home_cost No (not HOH); spouse not the child's QC (lived with child under half the year) | L15 4,250; tax **428**; Sch 8812: CTC 2,200, L19 = **428**; ACTC min(2,200 − 428 = 1,772, $1,700, 15% × 17,500 = 2,625) = **1,700**; EIC table eic_1 `other` at 20,000 = **4,328**; separated box **true**; refund **6,028** |
| M8 MFS no child | W-2 $15,000, box 2 $500; student loan interest paid $1,000 | EIC **0** (Step 4); s1.line21 **0** and `sli.any` not asked; L15 0; refund 500 |
| M9 IRA considered covered + loss | W-2 $50,000; not covered, spouse covered, together_late; traditional IRA $7,000; 1099-B box A short-term loss $5,000 | Sch D L21 **−1,500**; IRA L2 10,000, L5 48,500 ≥ 10,000 → **L20 0** (Form 8606 line 1 7,000); AGI 48,500; L15 32,750; tax **3,695**; carryover 3,500 |
| M10 IRA apart | M9 with apart_all_year | not considered covered → L1a No → **L20 7,000**; **Sch 1 line 20 box true**; AGI 41,500; L15 25,750; tax **2,855** |
| M11 DC benefits, no credit | W-2 box 1 $60,000, box 10 $5,000; plan max $5,000; child 4 lived with both all year; care $6,000; spouse earned $50,000; together_late; spouse will not claim the child | 2441: L12 5,000; L15 5,000; L16 6,000; L17 5,000; L18 60,000; **L19 50,000**; L20 5,000; **L21 2,500**; L23 5,000; L25 2,500; **L26 2,500** → L1e; credit **0**; AGI 62,500; L15 46,750; tax 5,375; CTC **2,200**; L22 3,175 |
| M12 PTC no exception | W-2 $40,000; 1095-A 12 months: premium 500, SLCSP 450, APTC 250 | L1 1; L3 40,000; L4 15,060; L5 **265**; not applicable; L24 0; L25 3,000; L27 3,000; L28 (200–299, other) **1,950**; **L29 1,950** → Sch 2 L1a; L15 24,250; tax 2,675 |
| M12b exception | M12 with line A | applicable figure at 265 = 0.0460 [V table]; L8a 1,840; annual: 6,000 / 5,400 / 1,840 / 3,560 → max PTC 3,560; APTC 3,000; **net PTC 560** → Sch 3 L9 |

Evidence class: hand-predicted from source (spec 6.1). M7 and M11 depend on D3; M12 on the existing D7(a) path.
Existing fixtures whose expectation **changes** (owner approval, D2): `stage4.refuse.married` (scope.json),
`ss.mfs` (s3.json), `stage15.refuse.f2441.mfs`, `stage15.refuse.f2441.mfs_benefits` (f2441.json),
`stage11.refuse.hsa_married` (f1040.json; stays refused only if its inputs say the spouse has an HSA). Line-level MFS
fixtures (115 cases across sd, qdcg, sa, ssb, f8959, f8960, s1a, eic, mutation, classm) keep their values [V count].
Defaults: the 47 MFS cases that answer `household.married_dec31: false` would refuse at the tightened conflict gate;
their **input** is restated to true (the audit already named it untruthful) [V audit].

Mutation pins to expect [I]: operand mutants on the new choose alternatives (`person.ira_line2_status` apart branch —
killed by M10; `f2441.line19` MFS branch — M11; `f2441.exclusion_cap` — M11; `f8962.applicable` mfs term — M12/M12b;
`household.filing_status_conflict` mfs alternative — mfs.not_married row and a fixture; `f1040.line12b` — M2). The
24 equivalence arguments in `reports/2025/mutation.md` that reason about the mfs alternatives (s1a.line13_claim,
line21_claim, f8889.bad_months) should be re-checked; any that relied on the return being refused go stale.

External engines [V grep of `.engines/`]: both adapters map `mfs` (`ustaxes_adapter.py` l.82, `ots_adapter.py` l.225);
`generate_cases.py` never emits mfs (l.217, 637) — add an MFS branch. UsTaxes 2025 handles MFS brackets, SALT halves,
$1,500 loss, SSB with a LIVE_APART question, SLI bar, 2441 $2,500, saver's; its EIC refuses all MFS
(`ScheduleEIC.ts` l.78, no separated-spouse rule) → expected differences on M7; no spouse-itemizes handling found [I].
OpenTaxSolver 2025 handles MFS QDCG/SDTW ceilings, −1,500, SALT MFS, and skips Schedule 1-A Parts II–V for MFS
(`taxsolve_US_1040_2025.c` l.175, 1401, 1824, 2463–2493) [V lines; behaviour I].

---

## 6. 2026

- Mend in the same commit as the 2025 change (check-all applies the ops every run, and their `from:` values quote the
  `s3.mfs` refusals): `changes/2026/scope.credits.yaml` (the `refuses` from/to lists, l.17 and l.177),
  `changes/2026/f2441.yaml` (line11 refuses, l.163), the notes quoted in `changes/2026/f8962.yaml` (l.298, 304) and
  `changes/2026/s1a.yaml` (l.31, 36) [V].
- Figures already in the change map with MFS amounts: SALT $20,200 / $252,500 (C-PRI-14..), QBI $201,775 (C-SCHED-30,
  confirmed by rp-25-32 p. 22), f2441 line 21 $3,750 (C-CRED-11: also set `dc.exclusion_max_mfs` 375,000), saver's,
  IRA ($10,000 MFS unchanged; `ira.line2_apart` → 9,100,000 per C-PEOP-08 note) [V changes.md l.1755–1759].
- New in 2026 with MFS effect: Form 8962 lines 28–29 reserved (C-PEOP-12: full repayment, so M12's line 29 = 3,000 in
  2026); line 12f non-itemizer charity (C-PRI-01: rule text unarchived; MFS amount $1,000 and the spouse-itemizes
  interaction unverified [I]); 12d birth date 1962.
- The 2026 i1040gi is not posted: the MFS disallowance list is unverified for 2026; the new lines' 2026 cites wait.

---

## 7. Lane split

| Lane | Files owned | Model / class | Order |
|---|---|---|---|
| L1 opening & household | household.yaml, f1040.yaml, scope.yaml, s3.yaml, ssb.yaml, eic.yaml, params/2025.yaml, refusal_notes.yaml, coverage/opening.yaml, coverage/mfs.yaml (its rows), changes/2026 mends, tools/coverage/categories.json + tree.json | Opus, judgment | first (declares `household.mfs_living`, `household.mfs_apart_*` ids; others may start on the declared ids) |
| L2 deductions & adjustments | sa.yaml, s1.yaml, sli.yaml, ira.yaml, person.yaml | Opus, judgment | parallel |
| L3 credits | f2441.yaml, f8863.yaml, f8962.yaml, f8889.yaml | Opus, judgment | parallel |
| L4 dependents | dependent.yaml | Opus, judgment | parallel (D3 first) |
| L5 fixtures, engines, wording | fixtures/2025/* (M1–M12b in returns.json; restated defaults), tools/engines/generate_cases.py, bank wording audit | Sonnet, mechanical | after L1–L4 merge |

`interview/2025/questions.yaml` is shared, bank-only, merged by entry (protocol phase 5). Params requests from L2/L3
go to L1's notes. Claims via `tools/claims.py`.

Reviews (one per form per round, line-scoped, after the form's fixes land): transcription + render + class M for
household, f1040, scope, s3, ssb, eic, sa, s1, sli, ira, person, f2441, f8863, f8962, f8889, dependent — **16 forms ×
3 ≈ 48 runs**; question review for ~10 new or reworded questions; screen and false-no review for the three new
refusing questions (CP, HSA spouse, spouse claims) under the per-release sample. Note: 96 review files cite the MFS
refusal in their rulings (transcription 46, render 38, class M 4, other 8) [V grep]; rerunning will surface MFS
value differences that earlier rulings dismissed as "on refused returns", so adjudication load is higher than usual.

---

## 8. Risks and decisions for the owner

Decisions:
- **D1** Community property: refuse every MFS filer who lived in a CP state (precedent; ~31% of MFS [I]) — or compute
  with Pub 504 pp. 22–24 and the §66 lived-apart-all-year rule (needs Pub 555 archived; a large lane).
- **D2** Approve the changed expectations: `opening.separate` and five refusal fixtures move from `s3.mfs` to computed
  (a scope change, not a bar bend); the 47 default inputs restated.
- **D3** A child who is also the spouse's qualifying child: ask whether the spouse claims (computes most MFS parents)
  — or keep the tie-breaker refusal (keeps them refused).
- **D4** Spouse's age/blind boxes on MFS: keep refused (rare) or compute with two questions.
- **D5** HSA: narrow refusal to a spouse with their own HSA/HDHP (proposed) — or compute the line 6 division.
- **D6** PTC Exception 2: asking about domestic abuse and abandonment in the interview (wording, sensitivity).
- **D7** Notices only (spouse name/SSN; itemize together); no advice that a joint or HOH return may cost less?
- **D8** New York: once federal MFS computes, NY MFS returns become reachable (`tools/ny_fixtures.py` l.435
  assumes the federal refusal; NY has `gate.hh_state_mfs`) — a NY lane must check before release.

Risks:
- Latent MFS branches were never exercised on a whole return; items 1–10 of section 0 were found by reading, and
  more may surface (e.g. any `f1040.status == mfj` test that treats MFS like single where the source differs:
  f8880.yaml l.30, ira.yaml l.31/46, dependent.yaml l.1034, clcw_next_year l.287 — read and judged correct for MFS
  by this scout only for f8880 and ira [I for the others]).
- Lazy evaluation may ask `household.mfs_living` of every MFS return through lines 6d / line 20 box unless those are
  gated (amb.2025.mfs_lived_apart_boxes).
- 2026 operations break the moment the 2025 refusals are removed unless mended in the same commit.
- Estimate: CP share and residual refusals are unmeasured; the +1.3 to +1.5 point gain is an inference.
