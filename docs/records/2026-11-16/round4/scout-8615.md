# Scout and design: Form 8615, tax for certain children who have unearned income (TY2025, federal)

Lane A7-8615 · Model: claude-opus-5-5 · Class: judgment · Year: 2025 · Jurisdiction: us
Read from `.claude/worktrees/xint` (HEAD `acde74b5` plus the uncommitted expansion candidate), with
`.claude/worktrees/x2-dep` and the commit object `e812db31` read for the deferred `qdcg_amount` def. Nothing in the
repository was changed. No builds, test runs, model calls or network fetches. One read-only Python script read the SOI
spreadsheets (with the `.engines` venv's `xlrd`, `-I`).

Evidence labels: **[V]** checked this session against a file (path:line where useful); **[T]** testimony (a prior note,
not re-grounded); **[I]** inferred. Fixture arithmetic is this scout's own, a prediction for the build lane to re-derive
independently (protocol 5.1), not evidence.

This scout supersedes section K of `docs/provisional/lanes/scout-dependent-filers.md` (written against `sweep-tasks`,
HEAD `63a20efc`). It re-checks that design against the xint tree and the archived source, keeps what holds, and
corrects what does not (section 0.2).

---

## 0. Summary

### 0.1 Headline

| Item | Finding |
|---|---|
| Share of returns | **0.143%** (228,992 dependent returns with "kiddie tax" of 160,602,107; SOI TY2023 Table 1.7 col. 35, `sources/2025/soi-23in17dp.xls`; total from Table 1.2) [V]. Dependent returns only; non-dependent Form 8615 filers are not in it. Already the basis of `interview/2025/gate_frequencies.yaml:142-152` [V] |
| Stop rule | **Below** the protocol 1.1 stop rule (about 0.5 points). The area is taken by recorded judgment (it unblocks `qdcg_amount` and finishes the dependent filer), not by measured gain. Owner decision O1 |
| Estimate effect | **None on `estimate.py`'s figure.** `scope.other_line16` is in the report's unmeasured list (`reports/2025/filer_coverage.md:19-20`) [V]. The gate-frequency share drops (section 8) |
| Sources | f8615, i8615 2025 **archived** [V]; 2026 drafts **archived** (`tools/sources/2026.json:644-656`, `draft: true`) [V]; Rev. Proc. 2024-40 **archived** (2025 child AMT cap $9,550) [V]. Nothing is to fetch for the build. Optional: Pub 1304 Table 3.1A (all 8615 returns, by AGI) |
| Size | One new form (~32 lines), the revived `qdcg_amount` def (exists, unchanged base), one line-16 change in `f1040`, a §59(j) cap in `s2`, the retirement of two `scope` inputs, one interview topic (6 to 10 questions). Two build lanes plus one mechanical lane (section 7) |
| Engines | None computes Form 8615's regular tax: UsTaxes `// TODO: support 8615` (`.engines/ustaxes-src/src/forms/Y2025/irsForms/F1040.ts:509`) [V]; Tax-Calculator and PolicyEngine-US compute only the §59(j) child AMT (`taxcalc/calcfunctions.py:2495`; `policyengine_us/.../alternative_minimum_tax/kiddie_tax/`) [V]; OpenTaxSolver nothing [V grep]. Class C gap for the trust statement |

### 0.2 What changed against the earlier scout (K)

1. **The deferred def survives, but only loosely.** `qdcg_amount` was dropped from xint (`docs/provisional/lanes/xint.md:373-382`) [V].
   Its full version (def, two keyed tables, `tools/check_qdcg_ceiling.py`, its `check_all_steps.sh` step at line 202 and
   `self_tests.py` entry at line 52) is in commit `e812db31` ("xint snapshot for classm-jobs repro"), which **no ref
   contains** (`git for-each-ref --contains e812db31` is empty) [V]. A copy is staged, uncommitted, in the `x2-dep`
   worktree [V]. `qdcg.yaml`, `tax_on_amount.yaml` and `tcw.yaml` are byte-identical between x2-dep and xint (`diff -q`)
   [V], so the def can be revived as is. **Pin it now** (owner action O9): it is otherwise lost to `git gc` or a worktree
   removal.
2. **Child AMT is a silent wrong answer, not a side risk.** Rev. Proc. 2024-40 §3.12 is archived and caps a kiddie-tax
   child's AMT exemption at earned income + $9,550 (`sources/2025/rp-2024-40.txt`, ~line 410) [V]. The archived i6251
   and f6251 say nothing of it (grep "8615", "child", "9,550", "unearned": no hits) [V]. The tool computes Form 6251
   (`s2.amt_*`; exemption at `s2.amt_l5`, `forms/2025/s2.yaml:328`) [V], so once 8615 children are let through, a
   child with large interest and a low-bracket parent gets AMT 0 where it is thousands (fixture K11: $4,705). The cap
   must be built or refused in the same round (O3). The earlier scout listed rp-2024-40 as "to archive": stale.
3. **Condition 2 ("required to file") needs no refusal.** The earlier scout proposed `f8615.filing_unsettled` for a
   blind dependent. Chart B (i1040gi p. 10, `sources/2025/i1040gi.txt:467-497`) [V]: the gross-income test for a
   dependent is "more than the larger of $1,350 or earned income (up to $15,300) plus $450" (blind: $3,350 or earned +
   $2,450), which is exactly the dependent standard deduction (plus the blind addition). So a child not required to file
   has gross income at most their standard deduction, AGI ≤ gross income, taxable income 0, Form 8615 line 4 = 0, line
   5 = 0, and line 18 = line 17 [I, from the text]. The same holds for a non-dependent (gross income below the basic
   standard deduction). Record it as an ambiguity entry, no gate.
4. **Line 1 has two branches.** i8615 p. 2, Line 1: "If the child had no earned income ..., enter the child's adjusted
   gross income from Form 1040 ..., line 11b" (`sources/2025/i8615.txt:127-129`) [V]; otherwise the worksheet, line 9
   minus earned income minus the early-withdrawal penalty (p. 3). AGI subtracts every adjustment; the worksheet only the
   penalty. The earlier design had only the worksheet. Encode both (A9). The difference changes line 5 only for a child
   with no earned income and an adjustment other than the penalty, which a dependent can hardly have (student loan
   interest and HSA are barred to dependents; an IRA needs compensation), and for a non-dependent line 4 binds [I]. It
   changes the printed lines 1 and 3 and Worksheet #1's ratios, so fidelity needs it.
5. **The Form 8615 earned-income definition sets Schedule 1 line 3 losses to zero** (worksheet line D: "if Schedule 1
   ..., line 3 or 6 is a loss, use zero", `i8615.txt:174-179`) [V], but a net SE loss sends the child to the Alternate
   Worksheet (p. 2). The earlier algebra (A6: both reduce to line 9 − 1z − s1.line3 − s1.line18) still holds [V
   re-derived: with Schedule C loss L, A + B − D = line9 + L − 1z − 0 − line18].
6. **Persona and order numbers moved.** Personas now run to `22_refused_old_loss` [V], so new ones start at 23. Order
   277 is still free (orders 276 and 278 are used, `interview/2025/questions.yaml:634-698`) [V].
7. **The retired inputs reach ~900 fixture lines.** `scope.unearned_2700` / `scope.f8615` occur in 13 fixture files:
   `mutation.json` 493 lines, `classm.deepseek.json` 224, `classm.json` 128, `returns.json` 22, `classm.gpt.json` 12,
   `f1040.json` 10, `s3.json` 9, `scope.json` 7, `eic.json` 3, `defaults.json`, `s1a.json` 2 each, `s8812.json`,
   `ssb.json` 1 each (grep -c) [V]. The engine rejects undeclared inputs (x2-dep's note: "12 rejected by the base's
   undeclared inputs", `docs/provisional/lanes/x2-dep.md:12`) [T]. Retiring the inputs is a mechanical lane of its own
   (O4).
8. **Pub 929 is archived, but as the 2021 edition** (`tools/sources/2025.json:2410-2413`, URL `p929--2021.pdf`) [V].
   Not needed as a source.

---

## 1. Who it affects, and the share

**Who** (i8615 p. 1, Who Must File, `i8615.txt:44-68`) [V]: a child with more than $2,700 of unearned income, required
to file, under 18 (or 18, or a full-time student 19 to 23, with earned income not more than half of support), with a
parent alive, not filing jointly. "These rules apply whether or not the child is a dependent."

**Typical filer** [I]: a 16- or 17-year-old, claimed by parents filing jointly, with a brokerage or custodial (UTMA)
account paying $3,000 to $20,000 of interest and dividends, and perhaps a summer W-2. The parent fills in the return,
holding the parents' own Form 1040.

**Share** [V, computed from the archived tables]:

| Measure | Value | Source |
|---|---|---|
| Dependent returns with "kiddie tax" (TY2023) | 228,992 | Table 1.7 (`soi-23in17dp.xls`) col. 35, row "All returns" |
| All returns (TY2023) | 160,602,107 | Table 1.2 (`soi-23in12ms.xls`) row 8 col. 1 |
| Share | 0.143% | ratio |
| Of those, AGI under $20,000 | 163,622 (71%) | Table 1.7 col. 35, rows $2,000 to $20,000 |
| Of those, AGI $50,000 or more | 14,216 (6%) | rows $50,000+ |
| Tentative tax of those returns | $854.0 million | col. 36 |

Limits:
- Table 1.7 counts dependent returns only. Non-dependent 8615 filers (students 19 to 23 whose parents do not claim them)
  are missing [V header]. Pub 1304 Table 3.1A ("Returns with Form 8615 Tax Computation", listed at
  `sources/2025/soi-agi-size.txt:293`) would count them; it is not archived [V].
- No archived table splits these returns by age. The share under 16, which `household.filer_under16` refuses regardless,
  is unknown [V absence]. Primary filers under 18 are 1,803,861 returns (Table 1.6, cited in
  `gate_frequencies.yaml` `filer_under16`) [T]. A custodial account is often opened young, so a large part of the
  kiddie returns may be under 16 [I]. With the under-16 gate kept, the served share is materially below 0.143% (O2).

---

## 2. The form and instructions

| Document | 2025 | 2026 | Pages used |
|---|---|---|---|
| f8615 | archived (`sources/2025/f8615.*`, "Created 9/9/25") [V] | draft archived (`sources/2026/f8615.*`, "Created 5/7/26", `draft: true`) [V] | the form (1 p.) |
| i8615 | archived (Oct 22, 2025, 10 pp.) [V] | draft archived (`draft_posted` 2026-08-04) [V] | p. 1 Who Must File, Jan 1 chart, which parent; p. 2 line 1, earned income, Alternate Worksheet; p. 3 Unearned Income Worksheet, line 2, Amanda/Roger/Eleanor; p. 4 lines 7, 8, Persimmon; p. 5 Worksheets #1, #2; p. 6 Worksheet #3; p. 7 line 9; p. 8 Sch J for line 9, line 10, line 11, 12a/12b (Persimmon .333); p. 9 lines 13 to 15; p. 10 line 15 SDTW, line 17, line 18 [V by page footers in `i8615.txt`] |
| i1040gi | archived [V] | not archived [T] | p. 10 Chart B; p. 34 line 16 (8615 conditions); p. 38 QDCG worksheet |
| rp-2024-40 | archived (`document_tax_year: 2025`) [V] | rp-25-32 archived; §3.11 child AMT cap $9,750 (`sources/2026/rp-25-32.txt:737-746`) [V] | §3.12 child AMT exemption cap $9,550 |
| rp-25-32 §3.02 | — | $1,350 / $2,700 / $13,500 unchanged (`rp-25-32.txt:516-532`) [V] | |
| i6251 | archived; silent on §59(j) [V] | archived [T] | p. 9 Exemption Worksheet |

**Nothing needs fetching for the build.** Optional for the estimate: Pub 1304 Table 3.1A, TY2023 XLS (the URL is on
the `soi-agi-size` page; not fetched).

**2026 draft against 2025** (amounts and vocabulary diff of the two `i8615.txt`, plus the form's line list) [V]: no
dollar amount changes; only the year and the January 1 chart years (2008/2007/2002 to 2009/2008/2003, which
`age.cut_*` already moves with the year [T]); wording edits (the Pub 970 tip renamed; "widow or widower" reworded).
Form lines 1 to 18 are unchanged. The 2026 work is citation operations only (section 9).

---

## 3. Lines, worksheets and parent-return inputs

### 3.1 The bound QDCG def (revive; owner: lane K-form)

Revive from `e812db31` (or `x2-dep`, identical for these files [I: x2-dep has the def unwired; e812db31 has the
wiring]): `forms/2025/qdcg_amount.yaml` (207 lines; parameters `[amount, qd, ncg, status]`), the keyed tables
`tables/2025/qdcg_zero_ceiling.yaml` and `qdcg_fifteen_ceiling.yaml` (rows checked equal to `qdcg.zero_rate_ceiling` /
`fifteen_rate_ceiling`, `params/2025.yaml:473,486`), `tools/check_qdcg_ceiling.py` with its check-all step and self-test
entry. x2-dep's equivalence run (bound to the return's own lines: equal to `qdcg.line25` on 1,047 money cases) is
testimony [T]; repeat it as a fixture pin once a real line reads the def.

### 3.2 New `forms/2025/f8615.yaml`

**Inputs** (new, once per return, asked only when `f8615.applies`):

| id | prompt essence | type | cite |
|---|---|---|---|
| `f8615.parent_status` | that parent's filing status on their 2025 return | Enum(filing_status) | f8615 line C; i8615 p. 4 Lines A–C |
| `f8615.parent_ti` | the parent's taxable income, Form 1040 line 15 (0 if less) | NonNegDollars | f8615 line 6 |
| `f8615.parent_tax` | the parent's line 16, without tax from Form 4972 or 8814 or an education credit recapture | NonNegDollars | f8615 line 10; i8615 p. 8 (O5: ask or compute) |
| `f8615.parent_qd` | the parent's qualified dividends, line 3a | NonNegDollars | i8615 p. 4, line 8 "Qualified dividends" |
| `f8615.parent_ncg` | the parent's net capital gain: smaller of Schedule D lines 15 and 16, or line 7a | NonNegDollars | i8615 p. 4, line 8 "Net capital gain" |
| tick group `f8615.parent_marks`: `parent_sdtw`, `parent_sj`, `parent_feitw` | the parent's return used the Schedule D Tax Worksheet / Schedule J / the Foreign Earned Income Tax Worksheet; each refuses | Bool ×3 | i8615 p. 7 line 9; p. 4 line 6 and p. 8 line 10 (Form 2555) |
| `f8615.other_children` | that parent's return is used for another child's Form 8615 | Bool | f8615 line 7; i8615 p. 4 |
| `f8615.line7`, `f8615.others_qd`, `f8615.others_ncg`, `f8615.others_sdtw` | gated by `other_children` (O6) | NonNegDollars ×3, Bool | i8615 p. 4 line 8 "on line 7" |

**Derived conditions** (no new question; N8):
- Condition 1: `f8615.line1 > param f8615.base` (270000).
- Condition 2: moot (0.2 item 3); ambiguity entry, no line.
- Conditions 3 and 4: `person.edu_kid_age` for the taxpayer (`forms/2025/person.yaml:6392`) [V], summed as
  `scope.under24_count` does (`scope.yaml:204-219`) [V]. It is i8863 line 7's copy of the same test, with the
  January 1 chart. Boundary: i8863 "less than one-half" vs i8615 "didn't have earned income that was more than half"
  (A4; O7).
- Condition 5: the existing `scope.under24_if_not_joint` (`scope.yaml:240-280`) [V] or a copy in f8615.
- `f8615.applies` = all of these and no residual gate.

**Lines** (expression sketches; `f8615.` prefix omitted):

| id | printed | expr sketch | cite |
|---|---|---|---|
| `earned` | (helper) | `f1040.line1z + floor0(s1.line3)` (s1 line 6 does not exist: farm refused via `scope.schedule1` [V grep]) | i8615 p. 2 "Earned income"; worksheet line D (p. 3) |
| `uiw` | worksheet line 3 | `f1040.line9 − f1040.line1z − s1.line3 − s1.line18` (equals the Alternate Worksheet when Schedule C is a loss, A6) | i8615 p. 3; p. 2 Alternate Worksheet |
| `line1` | 1 | `choose: earned = 0 → f1040.line11b; else → uiw` (A9) | i8615 p. 2 Line 1 |
| `line2` | 2 | `param f8615.base` (an itemizing child refuses) | f8615 line 2 |
| `line3` | 3 | `subtract_floor0(line1, line2)` | f8615 line 3 |
| `line4` | 4 | `copy f1040.line15` (Form 2555 already refused, `sa.excluded_income` [T]) | f8615 line 4 |
| `line5` | 5 | `smaller_of [line3, line4]` | f8615 line 5 |
| `ws1_*` | Worksheet #1, 1–9 | 4, 5: `prorate`-style ratio to 3 places, cap 1.000; 6, 7: 2,700 × ratio; 8: `clamp(qd − ws6, 0, line5)`; 9: `clamp(ncg − ws7, 0, line5 − ws8)` | i8615 p. 5 |
| `ws3_*` | Worksheet #3, 1–19 | 5 = 0, 11 = `sa.standard` (itemizer refuses); 14 = `line3_ws / f1040.line11b` cap 1.000; 18, 19 clamps as #1 | i8615 p. 6 |
| `qd5`, `ncg5` | (helper) | `choose: line3 = line5 → ws1_8 / ws1_9; else → ws3_18 / ws3_19` | i8615 p. 4 "on line 5" |
| `line6` | 6 | `copy parent_ti` | f8615 line 6 |
| `line7` | 7 | input when `other_children`, else 0 | f8615 line 7 |
| `line8` | 8 | `sum [line5, line6, line7]` | f8615 line 8 |
| `qd8`, `ncg8` | (helper) | `qd5 + parent_qd + others_qd`; `ncg5 + parent_ncg + others_ncg` | i8615 p. 4 |
| `line9` | 9 | `choose: qd8 + ncg8 > 0 → qdcg_amount(line8, qd8, ncg8, parent_status).line25; else → tax_on_amount(line8, parent_status)` | i8615 p. 7 |
| `line10` | 10 | `copy parent_tax` (or computed, O5) | i8615 p. 8 |
| `line11` | 11 | `subtract(line9, line10)`, signed as printed (A7) | f8615 line 11 |
| `line12a` | 12a | `sum [line5, line7]` | i8615 p. 8 |
| `line12b` | 12b | ratio line5 / line12a to 3 places | f8615 12b; i8615 p. 8 (.333) |
| `line13` | 13 | `choose: line7 = 0 → line11; else → prorate(line11, line5, line12a, 3)` (the form: "If line 7 is blank, also enter this amount on line 13") | f8615 line 11, 13 |
| `line14` | 14 | `subtract(line4, line5)` | p. 9 |
| `qd14`, `ncg14` | (helper) | worksheet line 1 − its next-to-last line; line 2 − its last line | i8615 p. 9 "on line 14" |
| `line15` | 15 | `choose: line14 = 0 → 0; qd14 + ncg14 > 0 → qdcg_amount(line14, qd14, ncg14, f1040.status).line25; else → tax_on_amount(line14, f1040.status)` | p. 9; Part III heading |
| `line16` | 16 | `sum [line13, line15]` | p. 10 |
| `line17` | 17 | `copy f1040.non_sdtw_tax` (`f1040.yaml:718`) [V]; child SDTW refuses | p. 10 |
| `line18` | 18 | `choose: line5 > 0 → larger_of [line16, line17]; else → line17` | f8615 lines 3, 5, 18 |

### 3.3 Changes to shared forms

- **`f1040.yaml`** (`f1040.line16`, `f1040.yaml:748-776`) [V]: a first alternative `f8615.applies → f8615.line18`; a
  refusal when `f8615.applies` and `f1040.gate.sdtw` hold; the refusal `form:` text drops "8615".
- **`scope.yaml`**: `scope.other_line16` (`scope.yaml:~1284`) drops `scope.f8615_if_unearned_2700`; retire
  `scope.unearned_2700`, `scope.f8615` and their gates (`scope.yaml:281-347`) [V]; keep `scope.under24*` or move them.
- **`s2.yaml`** (O3): `s2.amt_l5_kiddie = choose: f8615.applies → smaller_of [s2.amt_l5, sum(f8615.earned_59j, param
  s2.amt_kiddie_add)]; else → s2.amt_l5`, and read it in `s2.amt_l6`. There is a parallel `s2.amt_h*` chain
  (`s2.amt_h5`, line 810) [V] that needs the same cap [I: purpose of the h chain not read]. Parameter
  `s2.amt_kiddie_add` 955000, cited to rp-2024-40 §3.12. §59(j) "earned income" is §911(d)(2) earned income [I];
  ambiguity entry A10.
- **Readers of `f1040.line16`**: `s2.amt_l10` (`s2.yaml:706`) and `ftc` [V grep]. Both now see the 8615 tax, as Form
  6251 line 10 and Form 1116 expect [I]. No New York form reads it [V grep].

### 3.4 Parameters and ambiguities

- Parameters: `f8615.base` 270000 (f8615 line 2); `s2.amt_kiddie_add` 955000; the qdcg ceiling tables (revived).
  2,700 and 1,350 move with the year (unchanged for 2026) [V].
- Ambiguity entries (prefix by form): A3 condition 2 moot (0.2 item 3, replaces the earlier refusal); A4 exact-half
  support; A5 earned income "generally" and the 30% rule not modeled; A6 Alternate Worksheet algebra; A7 line 11 signed;
  A9 line 1 branch on "no earned income" using the 8615 earned definition; A10 §59(j) earned income; plus
  `amb.2025.f8615_parent_line10` (Form 8615 line 10 says "minus any alternative minimum tax"; the instructions do not;
  Form 1040 line 16 holds no AMT, so it is moot for a 1040 parent [I]).

---

## 4. Refusals to keep

| Situation | Gate (proposed id) | Cite | Asked at |
|---|---|---|---|
| Child itemizes (line 2 rule, Worksheet #2, #3 lines 5 and 11) | `f8615.child_itemizes` = `f8615.applies ∧ sa.itemizes` | i8615 p. 3 Line 2; p. 5 #2 | the Schedule A choice (N11) |
| Child, parent or other child needs the Schedule D Tax Worksheet (28% or unrecaptured §1250 gain; a Form 4952 election) | `f8615.sdtw` (child: `f1040.gate.sdtw`; parent: tick; others: `others_sdtw`) | i8615 p. 7 line 9 | the parent tick group |
| Parent used Schedule J or the Foreign Earned Income Tax Worksheet | `f8615.parent_special` | i8615 p. 7 (Sch J); p. 4 line 6, p. 8 line 10 (Form 2555) | the parent tick group |
| Child files Form 2555 or Schedule J | existing `sa.excluded_income`, `scope.income_averaging` [T] | i8615 p. 4, p. 10 | unchanged |
| Child under 16 | existing `household.filer_under16` (O2) | `amb.2025.filer_under_16` (`ambiguities/2025.yaml:1423`) [V] | unchanged |
| Other children with SDTW items (if O6 supports line 7) | via `others_sdtw` | i8615 p. 7 | the other-children group |
| (Dropped) blind dependent with unsettled filing | none: A3 | Chart B | — |
| §59(j) child AMT, if O3 chooses refusal over the cap | `f8615.amt_possible` | rp-2024-40 §3.12 | after investments |

`scope.other_line16` remains for 8814, 4972, 8621, 8978, the §962 election and education credit recapture. Each new gate
is placed in `tools/coverage/tree.json` (topic `investments` or a new `kiddie` topic, part `taxes`).

---

## 5. Interview questions (construction protocol N1–N12)

**Typical filer:** the 16- or 17-year-old with a custodial account, parents MFJ (section 1). **Filer with nothing in
the area:** persona 01 (single W-2) and every filer 24 or over or filing jointly: they must see no new step. Today every
non-joint filer under 24 is asked `scope.unearned_2700` (order 113 seq 11, `questions.yaml:1809`) [V]; after the change
nobody is (N8: line 1 is derived from the income entered). That is a saving of one step for the filer with nothing.

**Placement:** a new topic at order 277, "Tax on your investment income at your parent's rate", between investment
interest (276) and the NIIT (278) [V free]. No parent question is needed: the topic is reached only when `f8615.applies`
is derived true (N2/N3: its cost to everyone else is 0).

| seq | input | prompt (draft) | norms |
|---|---|---|---|
| 1 | `f8615.parent_status` | "Your investment income is taxed partly at a parent's rate. Which filing status is on that parent's 2025 return?" Help: which parent (joint return → that return; married filing separately → higher taxable income; unmarried or divorced → the parent you lived with most of the year; a remarried custodial parent's joint return), from i8615 p. 1 | N1, N10 (help optional); the which-parent screen is folded into help (N12: no step for no fact) |
| 2 | `f8615.parent_ti` | "From that return: the taxable income on line 15." | N6 (the filer holds that paper) |
| 3 | `f8615.parent_tax` | "The tax on line 16, leaving out any tax from Form 4972 or Form 8814 or an education credit recapture." (dropped if O5 computes it) | N6 |
| 4–5 | `f8615.parent_qd`, `f8615.parent_ncg` | "Qualified dividends on line 3a"; "Net capital gain: the smaller of Schedule D lines 15 and 16, or line 7a if no Schedule D" | N6; a typical parent has 0 (N4: the cheap answer is 0) |
| 6 | tick group `parent_marks` | "Did that return use any of these?" Schedule D Tax Worksheet / Schedule J / Foreign Earned Income Tax Worksheet; each box refuses, told here | N11; N4 (typical: none ticked) |
| 7 | `f8615.other_children` | "Is that parent's return also used for this tax by another child of theirs?" | N2 (a No spares 8 to 10) |
| 8–10 | `line7`, `others_qd`, `others_ncg` (+ `others_sdtw` box) | "Their Form 8615 line 5 amounts, added together", and the qualified dividends and net capital gain within them | gated (O6) |

Conditions 3 and 4 reuse `person.edu_half_support`, `edu_fulltime`, `edu_parent` (order 243 seq 3–5,
`questions.yaml:3375-3392`) [V]; they are asked only when the age makes them matter (`person.edu_kid_age` structure,
`person.yaml:6392-6440`) [V]. The walk must show whether reaching them from topic 277 "returns to a topic already
left"; if it does, the lane moves their seq or records the reason (N7).

**Who could answer No wrongly** (judgment record):
- `other_children`: a parent filling in one child's return forgets the sibling. Guard: help "If you are preparing a
  return with this form for a brother or sister too, answer Yes." Cost: line 7 and 12b wrong in the child's favor.
- Tick group: a parent who used tax software does not know which worksheet it used. Guard: help naming where it shows
  (the SDTW is used only with Schedule D lines 18 or 19, or a Form 4952 line 4g election).

**Coverage rows** (new file `interview/2025/coverage/kiddie.yaml`): computed `kiddie.interest_parent_mfj`,
`kiddie.qd_ws1`, `kiddie.ws3`, `kiddie.other_children`, `kiddie.line5_zero`, `kiddie.amt` (if O3 builds the cap);
refused `kiddie.parent_sdtw`, `kiddie.parent_sj`, `kiddie.child_itemizes`; not asked `kiddie.not_asked_over24`,
`kiddie.not_asked_joint`, `kiddie.not_asked_small` (line 1 ≤ 2,700).

**Existing rows whose end changes by design** (pre-authorize, O8): `interview/2025/coverage/scope.yaml:502`
`scope.f8615` (refused → completes); `scope.yaml:511` `scope.under24_small_income` (`proceeds` on a retired input);
`dependent_filers.yaml:32` (answers `scope.unearned_2700`) [V].

**Personas:** `23_kiddie_teen_investor` (typical), `24_refused_kiddie_parent_sdtw`, and the walks of 01 and
`20_dependent_student` (nothing in the area) recorded before any change.

---

## 6. Fixtures (hand-predicted; the lane re-predicts)

The child is single, claimable, born 2008 (17 at the end of 2025, a parent alive), standard deduction $1,350 unless
stated; the parent has no QD/NCG unless stated. Tax by the 2025 table/TCW. K1–K10 are from the earlier scout [T];
**K1, K3, K4 and K5 re-derived here** [I, arithmetic shown]; K11–K14 are new.

| id | facts | key arithmetic | expected `f8615.line18` = `f1040.line16` |
|---|---|---|---|
| K1 | interest 10,000; parent MFJ TI 150,000, tax 22,828 | L1 = AGI 10,000 (no earned); L3 7,300; L4 8,650; L5 7,300; L8 157,300 → TCW .22×157,300 − 10,172 = 24,434; L11 1,606; L14 1,350 → 136; L16 1,742; L17 tax(8,650) 868 | **1,742** (larger_of → 16) |
| K2 | K1, parent single TI 40,000, tax 4,565 | earlier scout | 1,012 [T] |
| K3 | interest 61,350; parent MFJ TI 0, tax 0 | L4 60,000; L5 58,650; L9 tax MFJ(58,650) 6,564; L16 6,700; L17 tax single(60,000) 8,120 | **8,120** (larger_of → 17) |
| K4 | QD 6,000; parent MFJ 150,000 | WS #1: w4 1.000, w6 2,700, w8 3,300; L8 153,300 QDCG 22,828 + 495; L14 1,350 holding QD 2,700 > 1,350 → QDCG 0; L17 0 | **495** (also: QD above the amount in `qdcg_amount`) |
| K5 | wages 7,000, IRA deduction 7,000, QD 12,000; parent MFJ 150,000 | AGI 12,000; dep. std 7,450; TI 4,550; L1 19,000 − 7,000 = 12,000; L3 9,300 > L5 4,550 → WS #3: w14 1.000, w15 7,450, w18 4,550; L9 22,828 + 682.50; L11 682.50; L14 0 | **682.50** (WS #3; smaller_of → 4) |
| K6 | Persimmon (i8615 pp. 4, 8): Sharon line 5 3,000, line 7 6,000 | 12a 9,000; 12b .333 (class A); rest per earlier scout | 795.34 [T]; lines 7, 12a, 12b class A |
| K7 | wages 4,000, interest 10,000 | earlier scout | 1,832 [T] |
| K8 | QD 3,000, CGD 4,000, interest 3,000; parent QD 2,000 | earlier scout | 1,248.30 [T] |
| K9 | K1 + parent tick SDTW | — | refusal `f8615.parent_special` / `sdtw` |
| K10 | K1, born 2001 | not asked | 868 |
| **K11** | interest 50,000, no earned; parent MFJ TI 40,000, tax 4,326 | L4 48,650; L5 47,300; L8 87,300 → 10,002; L11 5,676; L15 136; L16 5,812; L17 5,623. **AMT:** AMTI 48,650 + 1,350 = 50,000; exemption min(88,100, 0 + 9,550) = 9,550; 40,450 × 26% = 10,517; less 5,812 | line 18 **5,812**; Schedule 2 line 1 **4,705** (0 without the cap) |
| **K12** | non-dependent, 22, full-time student, support test met, interest 30,000 | std 15,750; TI 14,250; L1 30,000; L3 27,300; L5 = L4 14,250 (WS #3 path, no QD); L8 = 14,250 + parent TI | pins line 4 binding for non-dependents |
| **K13** | a child with no earned income and an early-withdrawal penalty 100, interest 10,000 | L1 = AGI 9,900 (both branches agree) | pins the A9 choose on both sides with K7 |
| **K14** | Amanda (i8615 p. 3, age 13) line 1 = 2,800 | class A for line 1 **only if O2 lifts the under-16 gate**; otherwise the case expects the `household.filer_under16` refusal | — |

Branch coverage (5.2): K1/K3 larger_of; K1/K5 smaller_of; K4/K5 WS #1 vs #3; K6 line 7 > 0; K10 not applies; K13/K7
line 1 branch; K11 AMT cap. Mutation pins expected: line 13 with line 7 = 0 (ratio 1.000; avoided if line 13 is a
choose); line 15 with line 14 = 0; the WS ratio cap at 1.000 when QD ≤ line 1.

Restated by design (pre-authorize, O8): the four `mutation.json` `m3.scope.l16_f8615_*` cases [V count 4];
`f1040.json` (10 lines) and `scope.json` (7 lines) cases that set the retired inputs; coverage rows in section 5.

---

## 7. Lanes and sizes

| Batch | Lane | Model / class | Owns (claims) | Ranked work | Size |
|---|---|---|---|---|---|
| 1 | **K-form** `<r>-k8615` | Opus / judgment | new `f8615`, revived `qdcg_amount` + tables + check, `f1040`, `s2` | 1. revive the def (from `e812db31`); 2. lines 1–18 with WS #1; 3. f1040 line 16; 4. fixtures K1–K5, K9, K10; 5. WS #3, K5; 6. §59(j) cap (O3), K11; 7. line 7 (O6), K6; 8. 2026 operations | ~32 lines, 2 params, 6 to 8 ambiguity entries, ~14 fixtures. About the size of one earlier x1 lane [I] |
| 1 | **K-int** `<r>-k8615i` | Opus / judgment | `scope`, `questions.yaml` order 277 and the retired order-113 entries, `coverage/kiddie.yaml`, personas 23–24, `tree.json` placements | 1. retire `scope.unearned_2700`, `scope.f8615`; 2. topic 277; 3. coverage rows; 4. walks before/after | 6–10 questions; input ids fixed by the plan so it can run beside K-form |
| 1→2 | **K-strip** `<r>-strip` | Sonnet / mechanical | the ~900 fixture lines of the retired inputs (classm*, mutation, returns and 8 form fixture files) | a script that drops the two keys by case id, listing counts per file (protocol 5.4) | mechanical; one commit per file family |
| after | **E** `<r>-eng` | Sonnet / mechanical | `tools/engines/*` (full tier) | map nothing (no engine computes 8615); generate kiddie returns so the differential records the gap; PE and TC's §59(j) AMT can check K11 | small |

Collisions: K-form and K-int share no form file; both add inputs, so the integrator serializes commits (protocol 8.1).
`f1040` and `s2` are shared forms: no other lane in the batch may hold them.

**Reviews** (protocol 6.1; dry-run not run):

| Subject | Kinds | Count |
|---|---|---|
| `f8615` (new) | transcription, render, class M, whole | 3 |
| `qdcg_amount` (new def) | transcription, class M (render if defs render) | 2–3 |
| `f1040` | transcription, class M (line 16), render (refusal text) | 3, line-scoped |
| `s2` | transcription, class M (the cap) | 2, line-scoped |
| `scope` | transcription, render | 2 |
| screens (kind gate) | `f8615.child_itemizes`, `f8615.sdtw`, `f8615.parent_special` | sampled |
| questions | ~7 to 10 new, plus the retired ones' removal | per subject |
| completeness, false-no | `f8615` | sampled |

About 12 to 13 form-level runs plus sampled reviews.

---

## 8. Coverage estimate effect

- **`estimate.py`:** no change. `scope.other_line16` is unmeasured (`reports/2025/filer_coverage.md:19-20`) [V], and no
  category in `tools/coverage/categories.json` names it (scan) [V]. `dependent_filer` is already `refused: false`
  with `gates: []` [V].
- **Option (O1):** add a measured category `kiddie_tax` from Table 1.7 col. 35. The estimate would first drop by about
  0.14 points (a refusal newly counted), and recover it when the area is covered, less the under-16 share. That makes
  the gain visible; it is a measurement change, not a coverage change.
- **`gate_frequencies.yaml` `scope_other_line16`:** share 0.002 (range 0.0014–0.005), with the reasoning "the kiddie
  tax alone is 0.14%" [V]. After the area its residual is 8814, 4972 and the rest: set to about 0.0006 [I], by
  judgment, and add entries for the new residual gates (each well under 0.1% [I]).
- **Served share:** at most 0.143% plus the uncounted non-dependent filers, minus the children under 16 while that
  gate stands, minus the residual refusals [I].

---

## 9. Next year (protocol 7.1)

`changes/2026/` exists and 2026 is not adopted [T, protocol text]. No `changes/2026/` file names 8615 or qdcg today
[V grep]. Operations:
- `changes/2026/f8615.yaml`: citation and quote edits only (2026 draft form and instructions, `verified: draft`);
  `f8615.base` 2,700 unchanged → a "no change" row (rp-25-32 §3.02) [V].
- `changes/2026/qdcg_amount.yaml`: table rows for 2026 ceilings (rp-25-32 §3.03), checked equal to the `qdcg` 2026
  parameter operations [I: those operations not read here].
- `changes/2026/s2.<round>-k8615.yaml`: `s2.amt_kiddie_add` 9,550 → 9,750 (rp-25-32 §3.11) [V].
- Change ids `C-<ROUND>-F8615-NN`, `C-<ROUND>-QDCGA-NN`, appended to `research/ty2026/changes.md`. No paid review.

---

## 10. Owner decisions

1. **O1. Open the area below the stop rule.** Measured share 0.143% (dependent returns) is below about 0.5 points.
   Taken by judgment: it lands the deferred def and finishes the dependent-filer work. Also: add a measured `kiddie_tax`
   category, or not.
2. **O2. The under-16 gate** (`household.filer_under16`, owner decision 2026-10-22). Its recorded reason leans on Form
   8615 being refused (`ambiguities/2025.yaml:1432-1434`) [V]. Options: keep (the area serves 16–23 only; Amanda,
   Roger and Eleanor stay unusable as class A); lift; lift only where nothing else in the return depends on it. The
   area's real value depends on this.
3. **O3. Child AMT (§59(j)).** Build the cap in `s2` (recommended; source archived) or refuse 8615 returns where the
   AMT could bind. Doing neither gives a wrong answer silently (K11: $4,705 owed, $0 shown).
4. **O4. Retired inputs.** Strip `scope.unearned_2700` / `scope.f8615` from ~900 fixture lines (mechanical lane), or
   keep them declared and unread for one round.
5. **O5. Line 10:** ask the parent's tax (fidelity to the form, a second check on the copied figures; recommended), or
   compute it from the parent's taxable income, status, QD and NCG (one question fewer; relies on the parent's return
   having no other line-16 tax).
6. **O6. Other children (line 7):** support (Persimmon is class A for it; siblings with custodial accounts are common
   [I]) or refuse in v1.
7. **O7. Reuse of the Form 8863 line 7 questions** for conditions 3 and 4, accepting the exact-half boundary (A4).
8. **O8. Pre-authorize** the restated expected values and coverage-row ends (sections 5 and 6).
9. **O9. Pin `e812db31`** (for example `git update-ref refs/scratch/qdcg-amount e812db31`) before the x2-dep worktree
   is removed or `git gc` runs. Not done here (read-only).

## 11. Risks

- R1. The parent's figures are copied from another return; no review can catch a copying error. Prompts name exact lines.
- R2. Line 9 and line 10 by the tax table round at midpoints; line 16 can exceed line 17 by $1 with equal rates. Expected.
- R3. `s2.amt_h*` is a second AMT chain whose purpose was not read; the cap may be needed there too.
- R4. The 6251 instructions might carry other 8615-specific rules in Part III that the archived text lacks; grep found
  none [V absence], which is weak evidence of absence.
- R5. Non-dependent 8615 filers (students 19–23) are uncounted and have no persona; K12 is their only fixture.
