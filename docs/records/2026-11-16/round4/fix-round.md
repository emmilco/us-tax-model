# Lane B-chain: the combined fix-round patch (`patches/v3/fix-round.patch`)

claude-opus-5-5, judgment, year 2025, us and ny. Written 2026-11-16, about 01:30-02:00. Read only on xint: its files
were copied, never written. Nothing was built, walked, tested or reviewed. No paid call was made.
Labels: **[C]** checked in this session (by `patch`, a parse, a grep or a script over the scratch trees); **[I]**
inferred or relayed from a lane's .md, not re-checked.

## Summary

- **`P/patches/v3/fix-round.patch`**: 79 files, 17,336 lines, made by `git diff --no-index base work` with the
  prefixes rewritten to repo-relative paths.
  - **`git apply --check` against xint passes [C].**
  - Applying the patch with `patch -p1 -F0` to a fresh copy of `base/` gives a tree byte-identical to `work/` [C].
  - `base/` was still byte-identical to xint for all 80 copied files when the patch was made [C].
- **Chain:** the 23 patches the brief names, then `jr.patch` (v3), `jr-digital.patch` (v3, coordinator) and jr.md's
  ended-marriage reversion (coordinator).
  - Every hunk applied with `-F0` except **five**: one in inc-m12.cod, one in inc-m34, one in k1p, and two pieces of
    k1s (the qbi_passive drop and one rejected hunk).
  - Each of the five was either resolved by hand where both sides' notes made the intent clear, or dropped as briefed.
  - An independent check found every other hunk's new-side text in the tree after its step [C `hunkcheck.py`].
- **Validation [C, `scratch/b-chain/check.py`]:**
  - Every touched YAML file (28 forms, banks, coverage, personas, the ambiguity register) loads under a loader that
    rejects duplicate keys.
  - Every touched JSON file (25) parses, with duplicate object keys rejected.
  - No duplicate input in either bank (federal 1,175 entries, NY 56). No duplicate group id (78 federal, 3 NY), and no
    group over 6 members. Every group is declared and used.
  - No duplicate `(order, seq)`, form line id, ambiguity id, fixture case id or coverage row id in the touched files.
  - Every federal bank input has a form line in xint plus the patched forms.
- **N10:** 98 prompts, tick labels, help texts and headings in changed or new entries are over the limits (section 7).
  No tick label or heading is over (the build caps them at 12 and 25). This list is for the trim pass.

## 1. Files

- Patch: `P/patches/v3/fix-round.patch`.
- Scratch: `P/scratch/b-chain/`:
  - `base/`: pristine xint copies of the 80 files any step touches. `files.txt` and `jr-new.txt` list them.
  - `work/`: the result.
  - `snap-06` … `snap-25`: the tree after each step group.
  - `rej/`: the rejected hunks.
  - `log-0*.txt`: patch output.
  - Scripts: `check.py` (parse and duplicates), `hunkcheck.py` (hunk presence), `n10.py` (overruns). Data:
    `n10.tsv` and `n10_annot.tsv`.
  - `jr.snapshot.patch` and `jr-digital.snapshot.patch`: the jr files as applied. They were byte-compared with
    `patches/v3/` at the end, and are unchanged.
  - `raw.diff`: the unrewritten diff.
- hsa.yaml was copied for jr. After the reversion it ends unchanged, so it is not in the patch.

## 2. Per-step status

Order as briefed. Each step's `.md` order agrees with it (see "Order notes").

| # | Step | Result |
|---|---|---|
| 1 | sche-a (v2) | clean, 26 hunks |
| 2 | int-amt (v2) | clean, 837 hunks |
| 3 | int-p18 (v2) | clean |
| 4 | int-personas (v2) | clean |
| 5 | int-n10 (v2) | clean |
| 6 | int-n10-ticks (v2) | clean |
| 7a | int-rprop, non-bank files | clean. Applied from `scratch/round4-lows-sche/rprop_nonbank.patch`, which is byte-identical, file by file, to the 7 non-bank file diffs of `v2/int-rprop.patch` [C] |
| 7b | int-rprop, bank | `scratch/round4-lows-sche/apply_bank_chain.py`: all three asserts held. It adds `rprop_facts`, `rprop.qip` (seq 60), `rprop.basis` → 61 (int-n10's prompt kept), six members at 62-67, `rental.not_at_risk` → 68, and removes the `rprop.screen` entry |
| 8 | inc-m12.base (v2) | clean |
| 9 | inc-m12.cod (v2) | **1 of 2 bank hunks rejected**: resolved R1 |
| 10 | inc-m34 (v2) | **1 of 10 bank hunks rejected**: resolved R2 |
| 11-14 | older-ny, older-credits, older-scha, older-scha-0817a (v2) | clean |
| 15 | sche-a-lows (v3) | clean, all 18 hunks present after the step [C] |
| 16 | int-lows (v3) | clean |
| 17-21 | inc-m12-lows, inc-m34-lows, older-ny-lows, older-credits-lows, older-scha-lows (v3) | clean |
| 22 | k1p (v2) | **1 of 5 bank hunks rejected**: resolved R3 |
| 23 | k1s (v2) minus the qbi_passive hunks | **1 of 2 bank hunks rejected**: resolved R4. The qbi_passive parts are dropped: D1 |
| 24 | jr.patch (v3) | clean, 37 hunks, all present [C] |
| 25 | jr-digital.patch (v3) | clean (coordinator: apply) |
| 26 | jr ended-marriage reversion | by hand: R5 |

**Order notes.**
- int-amt must precede inc-m12 and inc-m34 (sche-int.md). It does.
- int-rprop's bank goes after the v2 chain by script (lows-sche.md, runbook).
- inc-m12-lows needs int-n10-ticks, then m12, then m34 (lows-inc.md).
- jr needs inc-m34-lows (jr.md). It is last.
- older-scha-lows applies after 0817a (lows-older.md).
- The v3 lows go after the whole v2 chain (lows-sche.md).
- No step's .md asked for a different order. The only deviation is the coordinator's addition of steps 25 and 26.

**On jr's report of the wide stack.** In this order, inc-m12(.cod) and inc-m34 each rejected one hunk. The conflicting
lines are int-amt's, not int-n10's: the new `interest_dividends` group declaration, and the `div.*` renumbering. Both
are resolved below (R1, R2).

sche-a-lows ignored nothing here: all 18 hunks applied, and their new-side text is in the tree [C]. jr's
"ignored" hunk was in its own order (sche-a-lows after the k1int stack), which this chain does not use [I].

## 3. Hand resolutions

| Id | File / entry | What each side wanted | Kept |
|---|---|---|---|
| R1 | `questions.yaml` group declarations after `money_b` | inc-m12.cod: declare `cod_why` and `cod_how` after `money_b`. int-amt had already put `interest_dividends` there | All three: `money_b`, `cod_why`, `cod_how`, `interest_dividends`. Declaration order carries no meaning [I]; each group's members carry their own order and seq |
| R2 | `div.other_boxes` help | inc-m34 (BUG-0830, D trim): the new 40-word help, on context `seq: 7`. int-amt renumbered the entry to `seq: 9` and left the help | inc-m34's help on `seq: 9` |
| R3 | `k1p.basis_carry`, `k1p.risk_carry`, `k1p.fuel_2024` (group `k1p_carry`, seq 97-99) | k1p: append the three entries after `k1p.not_at_risk`. int-n10 had added a bank `prompt:` to `k1p.not_at_risk`, which changed the context | The three entries verbatim, after `k1p.not_at_risk` and its int-n10 prompt, before `# --- end k1p ---` |
| R4 | `k1s.trader`, `re_pro`, `dwelling`, `interest_buy` (group `k1s_activity`, seq 179-182); `f7203.election`, `loans`, `line1`, `line2` | k1s: insert the four after `k1s.not_at_risk` and move the f7203 entries from 180-183 to 183-186. int-n10 and int-lows had changed the `k1s.not_at_risk` help and prompt, which were context | The four entries verbatim, after `k1s.not_at_risk` (int-n10 help and int-lows prompt kept), and the f7203 seqs moved to 183-186 |
| R5 | jr ended-marriage reversion (coordinator decision, from jr.md section 1, "To drop it") | jr: the spouse question on the ended-marriage path. Coordinator: too costly (about 14% of returns pay a step); keep it for MFS and married HOH | See below |

**R5 in detail.**
- `household.cp_not_joint`: the `community_property = false` branch is back to `household.no`, and its label is back to
  xint's text.
- `household.cp_spouse_ended` is deleted. Nothing else read it [C grep].
- Coverage, per jr.md's list:
  - Row `household.divorced_2025_spouse_cp_domicile` is deleted.
  - The answer `household.spouse_cp_domicile: false` is removed from `household.single_divorced`,
    `household.hoh_divorced`, `hsa.former_spouse_family` and `hsa.former_spouse_no_family`. These walks no longer
    reach the question.
  - hsa.yaml thereby returns to xint's text.
- Kept: the MFS and married-HOH answers (`opening.separate`, `mfs.*`, `household.hoh_married_not_considered_unmarried`,
  the sets, persona 15) and the rows `household.hoh_married_asks_spouse_state` and `…never_married_not_asked…`.
  `mfs.spouse_died_2025` is kept as well, because MFS reads `cp_any` [I: by jr.md's path list].
- Residual recorded in `amb.2025.mfs_community_property` `reason` (one added passage, mine). It says the spouse
  question is not asked after a marriage that ended in 2025, gives the cost (about 14% of returns pay one step) and
  says it was the coordinator's decision of 2026-11-16, and that such a return is computed without the split.
- **Left as jr wrote it [I, for the trim or review pass]:**
  - The `spouse_cp_domicile` help still says "Count a marriage that ended in 2025 … Answer No if you were not married
    in 2025." It is now shown only to MFS and married HOH filers (an MFS filer whose spouse died in 2025 can still meet
    it), so the sentence is mostly moot, but it is not wrong.
  - The `cp_marriage_ended` remedy in f1040 says "with either of you living in or having a permanent home in". The
    refusal now fires only on the filer's own answer, so the remedy text is broader than its trigger, though not false.

## 4. Omitted hunks

- **D1, k1s.qbi_passive (dropped as briefed; k1int replaces it)** [C: none of it is left in the tree]:
  - `forms/2025/k1s.yaml`: the new line `k1s.qbi_passive` (with cite `&id305`), the `k1s.qbi` label change ("when box 1
    is not a passive loss", which is true only with that refusal), and the `when: k1s.qbi_passive` refusal entry.
  - The k1s form note: the clause "and section 199A information on a K-1 whose box 1 is a passive loss" is removed.
    "and" moves before "interest on money borrowed …" so the list still reads correctly. This is my edit, so that the
    note does not list a refusal that is not there.
  - `fixtures/2025/k1s.json`: cases `k1s.refuse_qbi_passive_loss` (expects the refusal) and `k1s.qbi_material_loss_kept`
    (asserts `qbi_passive` false) are dropped. The other five new k1s cases stay. The second case's other assertions
    (qbi −10,000, col_i 10,000) would still hold [I]. If the owner wants them, restore that case without the
    `qbi_passive` key.
  - **Effect:** the k1s QBI-on-a-passive-loss sibling (k1.md section 7, new entry (b)) is **not** fixed by this round.
    It is latent while `scope.k1` refuses. It is fixed by `k1int-2-ebl-qbi.patch` when that lands.
- **R5's removals** (coordinator): jr's `cp_spouse_ended`, its `cp_not_joint` branch and label, row
  `household.divorced_2025_spouse_cp_domicile`, and the four ended-marriage answers.
- **Not applied, as briefed:** `int-rprop.after-n10.patch` and `int-rprop.after-v2-n10.patch` (the script replaces
  them), `inc-m12.patch` (base and cod were applied instead; they are equal [C per inc.md]), `older-scha-0817b.patch`
  (0817a chosen), the k1int stack, and `jr.xint.patch`.
- No other hunk was left out.

## 5. Closures that land with this patch

Taken from each lane's .md [I: relayed, not re-verified against the inventory]. Record each with
`tools/new_bug.py --pending` on the landing branch.

**sche-a (v2; patches/sche-a.md, v2/sche-int.md)**
- Fixed: BUG-0775, 0789, 0790 (the boat-refusing version), 0836, 0890.
- BUG-0781: close when sche-a lands (lows-sche.md). Residual: a private nonrecourse mortgage the property was taken
  subject to, and the spouse's own nonrecourse note.
- BUG-0911: closure entry recommended (sche-a.md). The field is done in xint (k1int.md item 6).

**sche-a-lows (v3)**
- Fixed: 0772, 0926, 0784, 0783, 0782, 0787, 0788, 0777, 0776, 0922, 0892.
- In part: 0785 (spouse half; the grouped half is deferred), 0925 (residuals listed).

**int-lows (v3)**
- Fixed: 0857 (with int-amt's gate), 0832, 0835 (tick residual), 0509, 0888.

**int-amt, int-p18, int-personas, int-n10, int-n10-ticks, int-rprop**
- These are plan items and name no bug closures.
- int-rprop has a pending new entry: ADS for a building outside the US.

**inc-m12 (v2: base + cod; inc.md, patches/inc-m12.md)**
- 0806, 0808, 0810, 0822, 0896, 0904, 0905, 0906, 0907.
- 0901 as inc-m12.md and inc-m34.md describe it.

**inc-m34 (v2)**
- 0830, 0873, 0897, 0899, 0900, 0901, 0894.
- 0833 is answered by an ambiguity (`amb.2025.f4952_no_2024_form`, owner option (a) open).

**inc-m12-lows (v3)**
- Fixed: 0809, 0811, 0812, 0813, 0814, 0823, 0824, 0825, 0771, 0902, 0903, 0909, 0910, 0868, 0872.
- In part: 0804, 0915, 0866, 0865.

**inc-m34-lows (v3)**
- Fixed: 0898, 0908, 0821, 0826, 0680, 0916, 0917, 0923.
- With no new text: 0893 (superseded) and 0894 (with 0897).

**older-ny (v2)**
- 0850, 0851.
- 0092 and 0629: use the drafts in patches/older-ny.md.

**older-credits (v2)**
- 0793, 0796, 0797, 0861 (residual: married dependents), 0862, 0870.

**older-scha (v2) + 0817a**
- 0803, 0805, 0815 (tick residual: SUI-only workers), 0817.

**older-ny-lows (v3)**
- 0853, 0854, 0855, 0856, 0858, 0859, 0860 (commands drafted in lows-older.md section 4).

**older-scha-lows (v3)**
- 0458 and 0924 (one closure), 0801, 0807, 0816, 0818, 0819, 0820.

**older-credits-lows (v3)**
- Fixed: 0554, 0794 (record that the form source is unchanged), 0798, 0863, 0864, 0869.
- In part: 0555, 0867.

**Bookkeeping closures (lows-older.md, no patch)**
- 0465, 0532, 0729, 0757.
- 0893, already above.
- 0647: owner's call (closing it in part is recommended).

**k1p (v2)**
- 0837, 0838, 0841, 0843.

**k1s (v2, without qbi_passive)**
- 0882 and 0886.
- Sibling (a), `k1s.interest_buy`, is fixed.
- Sibling (b), QBI on a passive loss, is **not** fixed (D1).

**jr (v3) + jr-digital, as reverted**
- New pending entries BUG-NEW-JR-01, 02, 03, 05 and 06 (texts in jr.md), each closed by this patch.
- JR-01's "Proposed fix" text must drop `household.cp_spouse_ended` and the row `household.divorced_2025_spouse_cp_domicile`,
  and state the ended-marriage residual (R5).
- JR-03's fix is the 56-word help (owner question 2 open).
- JR-04 closes with 0896 on the same commit. jr-digital is its follow-on, now applied.

## 6. Reviews expected (one per form per round, after the round's fixes; line-scoped where the tool allows)

**Forms changed (transcription and render, line-scoped)**
- asset, dependent, eic, f1040, f4952 (ambiguity link only; whether a link alone makes it due is unchecked, inc.md),
  f5695, f8582, f8853c, gift (new to the round, older-scha-lows), household (jr), k1p, k1s, person, rental, royalty,
  rprop, s1, s2, sa, scope, tipjob, ny_it201.
- Plus the ambiguity register entries: f4952_no_2024_form, f8853c_line24_public, f8853c_line25_floor,
  mfs_community_property, hoh_community_property, mfs_lived_apart.

**Class M (arithmetic or decision paths changed)**
- f8582 (sche-a), f1040 and s2 (int-amt gate line), rprop (screen derived), s1 (cod), sa (0817a).
- k1p (ask_five, ask_other_gp).
- household (jr: new and rewired lines; after R5 the rewired ones are `cp_any`, `hoh_cp_married`,
  `mfs_community_property`, and the gate line).
- ny_it201 (0850 lines, has_tax_exempt, has_other_income).
- Not k1s: refusals only, and the qbi_passive arithmetic-adjacent line is dropped.

**Screen and false-no samples (subjects that change)**
- The interest_dividends, rental_costs_a/b/c, rental_rare, rental_return, rprop_facts (new), asset_kind, cod_why and
  cod_how, money_a and money_b, sales_rare, k1p_facts, k1p_part_other, k1p_rental and k1p_carry (new), k1s_activity
  (new) and ny_interest screens.
- The gates listed in sche-int.md, int-rprop.md, lows-inc.md section 3, lows-sche.md, lows-older.md section 6 and jr.md
  section 7. In jr's, `gate:household.spouse_cp_domicile` now covers only the MFS and married-HOH paths.

**Question reviews**
- Every changed bank entry. These number roughly 180, as lows-inc 31, lows-sche about 20, lows-older about 45, and the
  v2 lanes' lists.

**Mechanical checks to run in the landing worktree**
- Build, render and `render --check`, citations, test-fixtures (us and `--ny`), interview-coverage (then `--write`),
  tick-groups, interview-rules, interview-order and draft-walk of personas 01, 03, 04, 07, 08, 15, 18, 19, 21 and 22.
- defaults_guard, check_refusal_reach, `tools/coverage/tree.py` (COVERAGE.md), and mutation (for jr's new chooses).

## 7. N10 overruns in changed entries (for the trim pass)

**How it was computed** [C `scratch/b-chain/n10.py`]
- Scope: every federal and NY bank entry whose bank prompt, help or tick changed or is new, or whose form `source`
  changed where no bank prompt overrides it. Also every changed group heading.
- The shown prompt is the bank prompt if there is one, else the form source. The collection frame is put first where
  the text does not already start with it.
- Words are counted by the engine rule (whitespace tokens holding a letter or digit).
- **Child** means the form line has `gated_by`, so the limit is 40. Everything else is a **parent**, limit 25.
- Help is over at more than 40 words; a tick label at more than 12; a heading at more than 25.
- **Before** is the xint count of the same field: the bank prompt if xint had one, else the form source; `—` for a new
  entry.

**Caveats [I]**
- Per-entry questions (marked "per-entry (frame)") are counted as parents unless gated. Several lanes held them to 40
  (for example `rental.days_personal`). The trim pass should settle which limit applies.
- Tick-member prompts (marked "tick member") are shown only behind "What this asks". Whether N10's 25 binds them is
  the owner's open plan item 5.
- Some rows are pre-existing overruns in entries this round touched, and some got shorter (for example
  `dependent.ptc_files` 47 → 40, `rental.days_personal` 62 → 48, `scope.recovery` help 55 → 44).
- No tick label or heading is over.

98 rows: 89 federal, 9 NY.

| Jur | Entry | Field (kind; where the shown text comes from) | Words | Limit | New/changed | Before | Note |
|---|---|---|---|---|---|---|---|
| us | `k1p.upe` | prompt (parent, form source) | 26 | 25 | new | — | tick member (k1p_facts); per-entry (frame) |
| us | `k1p.interest_buy` | prompt (parent, form source) | 29 | 25 | new | — | tick member (k1p_facts); per-entry (frame) |
| us | `k1p.t6` | prompt (child, form source) | 44 | 40 | changed | 29 | tick member (k1p_part_other); per-entry (frame) |
| us | `k1p.basis_carry` | prompt (parent, form source) | 26 | 25 | new | — | tick member (k1p_carry); per-entry (frame) |
| us | `k1p.fuel_2024` | prompt (parent, form source) | 27 | 25 | new | — | tick member (k1p_carry); per-entry (frame) |
| us | `f1040.withheld_other_any` | help | 44 | 40 | changed | 39 | tick member (paid_already) |
| us | `gift.special` | prompt (parent, bank) | 141 | 25 | changed | 92 |  |
| us | `s2.hsa_testing` | help | 42 | 40 | changed | 42 | tick member (rare_accounts) |
| us | `sa.charity_limited` | help | 42 | 40 | changed | 44 |  |
| us | `sa.excluded_income` | prompt (parent, bank) | 26 | 25 | changed | 33 | tick member (about_you) |
| us | `sa.dependent` | help | 56 | 40 | changed | 30 |  |
| us | `sa.spouse_extra` | help | 43 | 40 | changed | 20 |  |
| us | `sa.home_owner` | help | 47 | 40 | changed | 31 | tick member (paid_2025) |
| us | `sa.mortgage_interest` | help | 78 | 40 | changed | 47 |  |
| us | `sa.mortgage_other_use` | help | 41 | 40 | changed | 46 |  |
| us | `sa.line1` | prompt (child, bank) | 325 | 40 | changed | 313 |  |
| us | `sa.personal_property_tax_any` | help | 42 | 40 | changed | 30 | tick member (paid_2025) |
| us | `sa.line5b` | help | 52 | 40 | changed | 29 |  |
| us | `sa.state_tax_other_any` | prompt (parent, bank) | 49 | 25 | changed | 41 | tick member (paid_2025) |
| us | `sa.state_tax_other_any` | help | 43 | 40 | changed | 54 | tick member (paid_2025) |
| us | `sa.medical_any` | help | 51 | 40 | changed | 32 | tick member (paid_2025) |
| us | `sa.line11` | prompt (child, bank) | 48 | 40 | changed | 47 |  |
| us | `sa.line11` | help | 67 | 40 | changed | 54 |  |
| us | `sales.aggregate_eligible` | prompt (parent, bank) | 39 | 25 | changed | 37 |  |
| us | `sb.bonds_any` | help | 42 | 40 | changed | 25 |  |
| us | `scope.armed_forces` | prompt (parent, form source) | 30 | 25 | changed | 26 | tick member (about_you) |
| us | `scope.rental` | prompt (parent, form source) | 36 | 25 | changed | 34 | tick member (own_income) |
| us | `scope.medicaid_waiver` | prompt (parent, form source) | 33 | 25 | changed | 25 | tick member (other_pay) |
| us | `scope.medicaid_waiver` | help | 42 | 40 | changed | 36 | tick member (other_pay) |
| us | `person.household_wages` | prompt (child, form source) | 47 | 40 | changed | 26 | per-entry (frame) |
| us | `scope.religious_work` | prompt (parent, form source) | 53 | 25 | changed | 32 | tick member (other_pay) |
| us | `scope.recovery` | help | 44 | 40 | changed | 55 | tick member (money_b) |
| us | `scope.foreign_shares` | prompt (parent, form source) | 43 | 25 | changed | 34 | tick member (outside_us) |
| us | `scope.nol` | help | 41 | 40 | changed | 28 | tick member (before_2025) |
| us | `sd.sold_other` | help | 42 | 40 | changed | 29 | tick member (sales_rare) |
| us | `f1040.estimated_any` | help | 44 | 40 | changed | 22 | tick member (paid_already) |
| us | `f1040.line26` | help | 43 | 40 | changed | 15 |  |
| us | `dependent.other_only_spouse` | help | 43 | 40 | changed | 35 |  |
| us | `household.married_dec31` | help | 72 | 40 | changed | 64 |  |
| us | `eic.lived_with_relative` | prompt (parent, form source) | 30 | 25 | changed | 38 |  |
| us | `household.community_property` | prompt (parent, bank) | 26 | 25 | changed | 20 |  |
| us | `household.spouse_cp_domicile` | help | 41 | 40 | new | — |  |
| us | `household.credit_disallowed` | prompt (child, bank) | 43 | 40 | changed | 41 |  |
| us | `f8962.mfs_exception` | help | 50 | 40 | changed | 34 |  |
| us | `person.edu_over` | prompt (child, bank) | 57 | 40 | changed | 42 | per-entry (frame) |
| us | `person.edu_over` | help | 46 | 40 | changed | 37 | per-entry (frame) |
| us | `dependent.edu_over` | prompt (child, bank) | 46 | 40 | changed | 31 |  |
| us | `dependent.edu_over` | help | 46 | 40 | changed | 37 |  |
| us | `f8962.alien_below` | prompt (child, bank) | 41 | 40 | changed | 26 |  |
| us | `dependent.ptc_files` | prompt (parent, bank) | 40 | 25 | changed | 47 |  |
| us | `dependent.ptc_files` | help | 44 | 40 | changed | 40 |  |
| us | `s1.alimony_any` | prompt (parent, bank) | 32 | 25 | changed | 30 | tick member (money_b) |
| us | `s1.alimony_any` | help | 41 | 40 | changed | 22 | tick member (money_b) |
| us | `s1.inmate_wages` | prompt (parent, bank) | 29 | 25 | changed | 21 | tick member (money_b) |
| us | `s1.gambling_winnings` | help | 44 | 40 | changed | 40 |  |
| us | `s1.scholarship_any` | prompt (parent, bank) | 27 | 25 | changed | 21 | tick member (money_a) |
| us | `s1.hobby_any` | prompt (parent, bank) | 29 | 25 | changed | 25 | tick member (money_a) |
| us | `f1040.digital_assets` | prompt (parent, bank) | 32 | 25 | changed | 23 |  |
| us | `f1040.digital_assets` | help | 45 | 40 | changed | 35 |  |
| us | `s1.alimony_paid` | help | 41 | 40 | changed | 6 |  |
| us | `s1.cod_bankrupt` | prompt (parent, form source) | 36 | 25 | new | — | tick member (cod_why) |
| us | `s1.cod_interest` | prompt (parent, form source) | 30 | 25 | new | — | tick member (cod_how) |
| us | `f8853c.periodic` | prompt (parent, bank) | 39 | 25 | changed | 26 | per-entry (frame) |
| us | `f8853c.others_paid` | prompt (child, bank) | 49 | 40 | changed | 25 | per-entry (frame) |
| us | `f8853c.line24` | prompt (child, bank) | 42 | 40 | changed | 15 | per-entry (frame) |
| us | `rec.two_returns` | help | 43 | 40 | changed | 25 |  |
| us | `tipjob.listed` | prompt (parent, form source) | 41 | 25 | changed | 34 |  |
| us | `asset.listed` | prompt (parent, bank) | 60 | 25 | changed | 61 | per-entry (frame) |
| us | `f5695.any` | help | 41 | 40 | changed | 34 | tick member (home_school) |
| us | `k1s.mp_other` | prompt (child, form source) | 43 | 40 | changed | 33 | per-entry (frame) |
| us | `k1s.not_at_risk` | prompt (child, bank) | 41 | 40 | changed | 49 | per-entry (frame) |
| us | `k1s.interest_buy` | prompt (parent, form source) | 29 | 25 | new | — | tick member (k1s_activity); per-entry (frame) |
| us | `rental.days_fair` | prompt (parent, bank) | 35 | 25 | changed | 39 | per-entry (frame) |
| us | `rental.personal_any` | help | 45 | 40 | changed | 50 | per-entry (frame) |
| us | `rental.days_personal` | prompt (parent, bank) | 48 | 25 | changed | 62 | per-entry (frame) |
| us | `rental.services` | prompt (parent, form source) | 27 | 25 | changed | 16 | tick member (rental_rare); per-entry (frame) |
| us | `rental.part_home` | prompt (parent, bank) | 28 | 25 | changed | 26 | tick member (rental_rare); per-entry (frame) |
| us | `rental.amt12` | help | 49 | 40 | changed | 17 | per-entry (frame) |
| us | `rental.amt16` | help | 49 | 40 | changed | 13 | per-entry (frame) |
| us | `rental.prior_any` | prompt (parent, form source) | 33 | 25 | changed | 18 | per-entry (frame) |
| us | `rental.prior_not_active` | prompt (child, form source) | 44 | 40 | changed | 22 | per-entry (frame) |
| us | `rprop.basis` | prompt (parent, bank) | 43 | 25 | changed | 40 | per-entry (frame) |
| us | `rprop.disposed` | prompt (parent, form source) | 26 | 25 | new | — | tick member (rprop_facts); per-entry (frame) |
| us | `rprop.fast` | prompt (parent, form source) | 32 | 25 | new | — | tick member (rprop_facts); per-entry (frame) |
| us | `rprop.ads` | prompt (parent, form source) | 26 | 25 | new | — | tick member (rprop_facts); per-entry (frame) |
| us | `rprop.basis_changed` | prompt (parent, form source) | 32 | 25 | new | — | tick member (rprop_facts); per-entry (frame) |
| us | `rprop.credit` | prompt (parent, form source) | 31 | 25 | new | — | tick member (rprop_facts); per-entry (frame) |
| us | `rental.not_at_risk` | prompt (child, form source) | 42 | 40 | changed | 41 | per-entry (frame) |
| us | `royalty.expenses_any` | prompt (parent, form source) | 30 | 25 | changed | 14 | per-entry (frame) |
| ny | `ny_it201.ask.special_accrual` | prompt (child, bank) | 41 | 40 | changed | 32 |  |
| ny | `ny_it201.ask.out_of_state_bond_interest` | help | 44 | 40 | changed | 41 | tick member (ny_interest) |
| ny | `ny_it201.ask.529_nonqualified` | help | 53 | 40 | changed | 37 |  |
| ny | `ny_it201.ask.real_property_credit` | prompt (child, bank) | 46 | 40 | changed | 27 |  |
| ny | `ny_it201.ask.real_property_credit` | help | 59 | 40 | changed | 44 |  |
| ny | `ny_it201.ask.owes_use_tax` | prompt (parent, bank) | 49 | 25 | changed | 40 |  |
| ny | `ny_it201.ask.owes_use_tax` | help | 53 | 40 | changed | 40 |  |
| ny | `ny_it201.ask.est_any` | prompt (parent, form source) | 48 | 25 | changed | 37 |  |
| ny | `ny_it201.ask.est_any` | help | 43 | 40 | changed | 37 |  |

