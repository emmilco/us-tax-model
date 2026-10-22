> Adversarial verification of `stage20-capital-loss-carryover.md` by an independent read-only agent after Stage 15 (commit 1c465c2): 8 errors and 8 items out of date. Read it with the map; where they differ, the verification has checked the source.

# Verification: research/premises/stage20-capital-loss-carryover.md

Checker: read-only adversarial pass, 2026-10-22, against the repository at HEAD 1c465c2 (working tree: HANDOFF-STAGE-15.md, TASKS.md and fixtures/2025/stage15.json modified, not by me). Page N = N-th form-feed chunk of `.cols.txt`.

## Errors

1. **The 2024 Schedule D instructions are said to be not archived (section 2, "Not archived ... The 2024 Instructions for Schedule D ... https://www.irs.gov/pub/irs-prior/i1040sd--2024.pdf").**
   They are archived. `sources/2024/manifest.json` has id `i1040sd`, url `https://www.irs.gov/pub/irs-prior/i1040sd--2024.pdf`, fetched 2026-10-21 (commit 94ff90f, before this map). `sources/2024/i1040sd.cols.txt` p. 11 holds the 2023-to-2024 Capital Loss Carryover Worksheet: "Use this worksheet to figure your capital loss carryovers from 2023 to 2024 if your 2023 Schedule D, line 21, is a loss ...". Its 13 lines are the same as the 2025 edition with every year moved back by one.
   Affects **Q5 / D9**. The 2024-to-2025 comparison is archived, independent evidence that the IRS rolls the worksheet forward by changing only the years. That supports the reading that the 2026 display is the 2025 worksheet with each "2024" read as "2025". The map treats this as an unsupported inference.

2. **The mutation equivalence entries that must go (section 5.1, `engine/src/mutate.ts` row) are listed incompletely, and their wording is misdescribed.**
   The map names only `operand.sd.sd.line6.zero`, `operand.sd.sd.line14.zero` and `operand.sd.sd.line7.line6`, and says they claim lines 4, 5 and 6 are "identically zero".
   What the code actually does: mutate.ts (lines 108 to 118) replaces an operand with the nearest earlier line of the same type that the expression does not already reference. I reproduced that rule over `forms/2025/sd.yaml`:
   - In `sd.line7`, every operand (1a.h, 1b.h, 2.h, 3.h, 4, 5, 6) is replaced by **`sd.line14`**.
   - In `sd.line11` (copy `sd.zero`), the operand is replaced by **`sd.line6`**.
   So `operand.sd.sd.line7.line4`, `operand.sd.sd.line7.line5` (mutate.ts lines 239 and 240) and `operand.sd.sd.line11.zero` (line 236) are equivalent today only because lines 6 and 14 are zero. All three stop being equivalent once those lines carry a carryover. `line7.line6` is also a swap with line 14, not with line 6.
   The ".zero" notes say "Both source lines are zero after identical unsupported-source/carryover gates", not "identically zero".
   No draft decision depends on this, but the stage's mutation accounting does (spec 6.2, D12).

3. **"Those are refusal cases" (section 1.1, fixtures that set `sd.carryover` true).**
   Only the `stage3.json` case (`sales.refuse.carryover`) is a refusal case: it expects `f1040.line7a` refused with form "Capital Loss Carryover Worksheet". The `classm.json` cases that set it true (`classm.asset.3`, `classm.person.4`, `classm.s1.3`) expect no refusal and no Schedule D or line 7a value. There, `sd.carryover: true` is incidental, so they do not "become compute cases". They do need the five new inputs, or must be shown unaffected.

4. **"`sd.filed` ... closes the carryover half of T-003" (section 1.1, "making `sd.filed` test the raw boxes"; section 4.4; D10).**
   T-003 (TASKS.md line 14) reads "make `sd.filed` test the raw Form 1099-DIV boxes rather than the netted worksheet results". D10's recommended answer instead adds a line 6 / line 14 test and leaves the raw-box test as the alternative. Section 1.1 says the stage makes `sd.filed` test the raw boxes, which contradicts D10. Under D10 as recommended, T-003's carryover trigger is met but its text is not done.
   Affects **D10**: the owner should choose between closing T-003 by the raw-box test and amending T-003's text.

5. **"The netting worry ... arises only when `g28.line5` or `u1250.line16` is nonzero" (section 4.4).**
   This is too narrow. A short-term carryover alone (Schedule D line 6) makes `sd.line7` negative. That makes `g28.line6` (`smaller_of` sd.line7, sd.zero; g28.yaml line 59) and `u1250.line15` (copy g28.line6) negative, and either can zero `g28.line7` or the u1250 result while box 2d or 2b is above zero. The conclusion survives only because the proposed `sd.filed` also tests line 6 < 0. The reasoning as written does not cover it.

6. **The `categories.json` edit "gates `[]` and label 'supported since Stage 20', following the `schedule_c` pattern" (section 5.1).**
   That edit is not enough. `schedule_c` also has `"refused": false`, and `tools/coverage/estimate.py` line 154 is `refused = [c for c in cats if c.get("refused", True)]`. Without that key the category stays counted as refused.

7. **The R9 bound: "A 2024 MFS return reaching this test ... is only possible when R2 does not apply (2025 MFJ, one 2024 MFS return with the loss)" (section 7).**
   This is too narrow. A 2024 MFS return followed by a 2025 single or HOH return (divorce) is also computed: D6 refuses only a 2024 *joint* return. In that case the 2024 limit was $1,500. The recommendation (use the $3,000 bound or ask the 2024 status) still holds.
   Affects **D3** / R9 slightly.

8. **The downstream readers list (section 5.2) "checked by grep for `sd.` and `f1040.line7a` readers" omits `ssb.line3`.**
   `forms/2025/ssb.yaml` line 134 sums `f1040.line7a` directly ("Combine the amounts from Form 1040 or 1040-SR, lines 1z, 2b, 3b, 4b, 5b, 7a, and 8"). It is not only reached through AGI. The value-change conclusion is unaffected.

## Out of date after Stage 15

1. **Coverage step (section 1.1): "step 6: coverage 92.1% after, +3.2; +2.1 if covered alone now".**
   The current `reports/2025/filer_coverage.md` (64.7%) reads "| 5 | Capital loss carryover | 91.3% (+3.2) | +2.3 |". The 92.1 / +2.1 figures are the 6051ec0 report. The 3.5% share and the 5,622,923 count are unchanged.

2. **Roadmap numbering.** The map calls this "roadmap item 6", Form 5329 item 7, MFS "roadmap item 8" (section 5.4), the backlog "roadmap item 9", and says "Roadmap items 2 to 5 ... come before this item". It also refers to "roadmap items 1 and 2" for the Schedule 1 and credit residuals (Backlog, section 10). Spec 2.4 now reads:
   - "5. The capital loss carryover (91%)."
   - "6. ... Form 5329 (94%)."
   - "7. Married filing separately (97%, the target)."
   - "8. Form 1116 and the remaining deferrals of 2.2, and the smaller situations".
   - Schedule 1 is item 1; other credits is no longer listed.

3. **Backlog table, "Group gain if alone" column.** "in group 1" for `other_nonrefundable`, and "in group 2" for `form4797`, `nol`, `early_withdrawal`, `hsa_distribution`, `foreign_earned_income`, `cancellation_of_debt`, alimony. These are the old step numbers. The report now has Schedule 1 (`schedule1_misc`) as step 1 (+7.7) and Other credits as step 9 (+0.6 alone).

4. **Fixture line numbers (section 1.1): "stage3.json (line 11508) and classm.json (lines 1840 and 23342)".**
   Now `stage3.json` line 11736, and `classm.json` lines 1881, 31076 and 38340. There are three classm cases now, not two. The 6051ec0 values match the map.

5. **`params/2025.yaml` line 994 (section 7).** `sd.loss_limit:` is now at line 1049 (it was 994 at 6051ec0). The values are unchanged.

6. **"The project has no general 'died in 2025' fact" (section 4.3; Q4; D9).**
   Stage 15 added `f2441.spouse_died`, "Did your spouse die in 2025?" (forms/2025/f2441.yaml line 80, cited p503 p. 11), and `f2441.spouse_died_gate` (MFJ and spouse died). Q4's `shown_when` option could reuse or generalise that fact rather than add a new one. It is asked within Form 2441, so whether it is asked for every filer is to be checked.

7. **Backlog B4: "Line 1e may come almost free from Stage 15's Form 2441 Part III ... to be checked once Stage 15 lands."**
   It has landed. `f1040.line1e` is computed (`choose` on `f2441.benefits`, then `f2441.line26`), and `f1040.line1z` is now `sum` of `line1a` and `line1e` (f1040.yaml lines 38 to 69). T-002's text ("now line 1a alone") is itself stale. B4's remaining work is lines 1b, 1d and 1h.

8. **Backlog B6: "cheap once Stage 15 models W-2 box 12".**
   Stage 15 modelled box 12 only for codes D, E, F, G, H, S, AA, BB and EE (`w2.box12_any`, `w2.box12_d` and the rest; w2.yaml lines 208 to 272). Codes A, B, M and N are not modelled, but the per-code input pattern now exists.

## Unverifiable

- **The two separate SOI counts** (`soi-23in14acg` columns 59 and 117). The file is `.xls`, and neither xlrd nor openpyxl (nor a working pandas) is available. Only the `max` (5,622,923) is confirmed, through the report.
- **The coverage gain understated by the independence assumption.** This is the map's own unmeasured inference, with no microdata variable for it.
- **Section 108(b)(2)(F), Form 982 and Pub. 4681.** Confirmed not archived (absent from `sources/2025/manifest.json`), so the text cannot be checked.
- **The 2024 Form 1040-NR line 15 (R12).** Not archived in `sources/2024`.
- **Whether `f8960.unsupported`'s existing wording ("a disposition adjustment ... or another net investment income adjustment?") already captures a prior-year line 2(i) carryforward.** That is a reading question, so D8's need for a new question is open, not wrong.

## Confirmed

About 70 premises were checked. The decision-critical ones:

**Source text and arithmetic**
- Worksheet lines 1 to 13, both skip sentences, and the applicability, joint-return and canceled-debt sentences: verbatim in i1040sd p. 10. p550 p. 102 Worksheet 4-1 is the same, with the noted wording differences.
- The section 3.1 property. I re-ran it independently: 300,000 random cases, 0 violations of "neither (a) nor (b) gives lines 8 = 13 = 0" or of "line 8 + line 13 = net loss − max(0, min(allowable, TI + allowable))". It holds with the worksheet's zero floor on line 3. Pub. 550's prose "lesser of" needs that floor when negative taxable income exceeds the deduction.
- p550 pp. 101 to 103: every quote is on its stated page (limit, carryover rule, negative taxable income, short-term first, character, "whether or not you filed", joint/separate, decedent, the $4,000 example).
- f1040sd lines 6, 7, 14, 15 (p. 1) and 16, 21 with "($3,000), or if married filing separately, ($1,500)" (p. 2). The [2024] f1040sd and f1040 lines 11, 14 and 15 match (2024 line 14 "Add lines 12 and 13"; 2024 line 11 is AGI).
- i1040sd p. 3 (limit), p. 11 (g28 line 5 and line 7), p. 13 (u1250 lines 16 and 17 and the Form 2555 footnote), p. 14 (line 21, carryover to 2026), p. 1 (digital-asset codes).
- i1040gi p. 31, Exception 1 item 1 "You have no capital losses ...". The chunk carries printed page 31. `reviews/2025/transcription/sd.md` line 85 cites it as p. 33, which is that file's discrepancy.
- i8960 p. 9 (carryforward adjustment) and p. 10 (lines 2(h), 2(i), (i)(1), (i)(2)). (i)(1) is the sum of 2(a) to 2(h) and 3(d), so inside the slice it is 2(h), as the map says.
- f4952 p. 1 (line 2, line 7) and p. 3 (lines 4d and 4e, and the no-carryover filing exception).
- i1041sk1 p. 3: codes C and D go to Schedule D lines 5 and 12, g28 line 5 and u1250 line 16.

**Project code and records**
- `sd.carryover` is a Bool input with the stated wording. It refuses `sd.count` and lines 4, 5, 6, 11, 12 and 14 with form "Capital Loss Carryover Worksheet".
- `sd.line6` and `sd.line14` are Dollars copies of `sd.zero`. `sd.line7`, `sd.line15` and `sd.line16` are sums. `sd.line21` is a `choose` on `sd.has_loss`, through `sd.limited_loss` = `larger_of`(line16, loss_limit).
- `sd.filed` = count > 0 or line18 > 0 or line19 > 0.
- `g28.line5` and `u1250.line16` are NonNegDollars copies of `div.screen`. `g28.line7` and `u1250.line17` are as stated. `g28.line6` and `sd.line21` are held negative.
- `qdcg.line3` (via `qdcg.schedule_d_filed` / `schedule_d_net_gain`, copies of `sd.filed` / `sd.net_gain`). `f1040.gate.qdcg_applies` has the "not filed and distributions" disjunct.
- `f4952.line4d` (sd.line16) and `line4e` (sd.net_gain). `f8960.line5a` = copy `f1040.line7a`, with the stated form note. `eic.gain_7a`. `f1040.line15` = `subtract_floor0`(line11b, line14).
- `sd.loss_limit` values (−300000, mfs −150000).
- `s3.mfs` refused in `scope.ready`. `person.died_before_65` is at person.yaml line 129.
- Defaults are false in `compare.ts` line 50 and `generate_cases.py` line 57. Interview occurrences: questions (order 10), sales and stage4.
- Second-transcription sign choices: g28.md line 48, u1250.md line 234 and render/g28.md line 58 are quoted correctly.
- `run_engines.py` lines 170, 173 and 245.
- T-003, T-004 and T-012 texts. Spec 2.2 bullet "A capital loss carryover from the prior year."; spec 11 "Capital loss carryover in and out" (supports D9). Spec 4.2: `choose` returns money.
- PREMISES.md Stage 15 decisions 1, 5 and 7 are refusals as described.
- Archive status: Pub. 4681, Form 982 and i982, f1040sf, f4797, f6251, p536, f1040sh and f1116 are not archived; i1116, i8889, i1040sse, p526, f8949 and i8949 are.

**Engines (bears on D12, which the map left unchecked)**
- The installed PolicyEngine-US (2.49.4, `.engines/venv`) has a native `long_term_capital_loss_carryover` input. It is a memo item feeding the 28%-rate and unrecaptured-1250 computations; long-term gains are still expected to include it.
- It has no short-term counterpart, and no worksheet.
- Tax-Calculator has only the `p22250` / `p23250` nets and no carryover variable.
