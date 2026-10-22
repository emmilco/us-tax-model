> **Status: draft for the owner (2026-10-22).** Written by a read-only research agent from the archived
> sources in `sources/2025/`, before the stage it maps; its decision batch is a draft and nothing in it is
> decided. Every claim carries a locator and is testimony until checked again at authoring. Spot-checked by the integrating session: the 3.5% share; i1040gi Exception 1 ("You have no capital losses") makes Schedule D required with a carryover; the operand-equivalence entries for Schedule D lines 6 and 14 in engine/src/mutate.ts.

# Stage 20 premise map: the capital loss carryover (roadmap item 6), with a backlog of the smaller situations (roadmap item 9)

Read-only research for the owner, written by a research agent (Claude Code) from the archived snapshots on
2026-10-22. It is testimony for the authoring of the stage, not a verified encoding: each claim carries a
locator, and each line is to be checked again against its cited text when it is encoded. Page N is the N-th
form-feed chunk of `sources/2025/<id>.cols.txt`. For the IRS documents used here that chunk carries the
printed page number, as checked on i1040sd pp. 10 and 14, p550 pp. 101 to 103, i8960 pp. 9 and 10 and
i1040gi p. 31. Documents marked **[2024]** are the tax year 2024 snapshots in `sources/2024/`, which the quote
checker does not search (section 10).

Stage 15 (Forms 8880, 2441, 5695) is treated as landed. Roadmap items 2 to 5 (Schedule 1 income and
adjustments, Schedule E, Form 8962, Form 8863) come before this item in the spec 2.4 order. Where one of them
changes this map, the change is flagged (Schedule E: section 5.4; Form 2441 Part III: backlog B4).

---

## 1. Scope

### 1.1 What the stage retires

| Category (`tools/coverage/categories.json`) | Gate | Share of returns | IRS returns (2023) | Basis |
|---|---|---|---|---|
| `capital_loss_carryover`, "Capital loss carryover from 2024" | `sd.carryover` | 3.5% | 5,622,923 | IRS count only (independence assumed) |

Sources: `reports/2025/filer_coverage.md`, table "Refused situations", and the step table (step 6: coverage
92.1% after, +3.2; +2.1 if covered alone now). The IRS figure is `combine: "max"` over two SOI cells,
`soi-23in14acg` column 59 ("Short-term loss carryover") and column 117 ("Long-term loss carryover")
(`categories.json`). The largest of the two is a lower bound on returns with either. The report has no
microdata overlap for this category, so its independence assumption probably understates the gain, because
filers with a carryover usually also have securities sales, which are already in scope. That last point is my
inference and is not measured. I could not read the two separate SOI counts: pandas fails to import in this
environment (numpy ABI error), so `tools/coverage/estimate.py` could not be run.

`sd.carryover` today is a return-level Bool input, 'Is there a capital loss carried into 2025 from any earlier
year?' (`forms/2025/sd.yaml`). It refuses on `sd.count` and on `sd.line4`, `line5`, `line6`, `line11`,
`line12` and `line14`, each with form "Capital Loss Carryover Worksheet". It is asked in
`interview/questions-2025.yaml` (input `sd.carryover`, order 10), `interview/sales-2025.yaml` and
`interview/stage4-2025.yaml`. Its default is false in `engine/src/compare.ts` and
`tools/engines/generate_cases.py`. Fixtures that set it true: `fixtures/2025/stage3.json` (line 11508) and
`fixtures/2025/classm.json` (lines 1840 and 23342). Those are refusal cases, and they become compute cases or
must be re-pointed.

Open tasks this stage closes: **T-004**, the carryover sign convention for Schedule D lines 6 and 14, 28% Rate
Gain Worksheet line 5 and Unrecaptured Section 1250 Gain Worksheet line 16. It also closes the carryover half
of **T-003**, making `sd.filed` test the raw boxes; the digital-asset half stays open. And it closes the
"capital loss carryover" item of **T-012** (spec 11) and the spec 2.2 bullet "A capital loss carryover from
the prior year" (`TASKS.md`, `spec/spec.md` 2.2).

### 1.2 Recommended scope

**Compute now:**
- The Capital Loss Carryover Worksheet (i1040sd p. 10), from five figures on one 2024 return.
- Schedule D lines 6 and 14 from that worksheet.
- `sd.filed` true when either carryover is above zero.
- The carryovers in the 28% Rate Gain Worksheet line 5 and the Unrecaptured Section 1250 Gain Worksheet line 16.
- A display of the carryovers to 2026, from the same worksheet applied to the 2025 return.
- Everything downstream (Form 1040 lines 7a, 9, 11a; QDCGT; Schedule D Tax Worksheet; Form 4952 lines 4d and 4e;
  Form 8960 line 5a; EIC investment income; QBI). This follows from the existing reads without any edit
  (section 5.2).

**Refuse (new, unmeasured gates):**
- Two 2024 returns that each carry a loss into one 2025 joint return.
- A 2024 joint return with someone who is not the 2025 joint spouse (divorce, separation, death in 2024).
- Canceled debt excluded from income in 2025 (Form 982, Pub. 4681).
- A nonzero prior-year Form 8960 Net Gains and Losses Worksheet line 2(i).
- Inconsistent 2024 inputs.

**Fold in (recommended, small):** the Form 4952 investment interest carryover (`f4952.carryover`). It is the
same kind of 2024 figure (2024 Form 4952 line 7 to 2025 line 2), it sits in the same investment-income cluster,
and its gate is unmeasured (backlog B0).

**Reasoning.** The worksheet has 13 lines and no constants. Every downstream reader already takes Schedule D
lines 7, 15 and 16 or Form 1040 line 7a, so the stage mostly fills two zeros and fixes their sign. The hard
cases are allocation between spouses, attribute reduction under section 108, and the NIIT carryforward
adjustment. Each is rare, and each would need facts the 2024 return does not show, so they fit the owner's
pattern of refusing rare and hard situations (PREMISES.md, Stage 15 decisions 1, 5 and 7).

---

## 2. Sources

Archived and used:
- **f1040sd**: Schedule D 2025, pp. 1 and 2 (lines 6, 14, 16, 21).
- **i1040sd**: pp. 1, 3, 10 (the worksheet), 11 (28% Rate Gain Worksheet), 13 (Unrecaptured Section 1250 Gain
  Worksheet), 14 (line 21). `i1040sd-html` contains the same worksheet text.
- **p550**: pp. 101 to 103 (Capital Losses, Worksheet 4-1, joint and separate returns, decedent).
- **i1040gi** p. 31 (line 7a, Exception 1).
- **f4952** pp. 1 and 3.
- **i8960** pp. 9 and 10.
- **i1041sk1** p. 3 (box 11 codes C and D).
- **[2024] f1040** (lines 11, 14, 15) and **[2024] f1040sd** (lines 6, 7, 14, 15, 16, 21).
- `reports/2025/filer_coverage.md`, `tools/coverage/categories.json`.

f8949 and i8949 are archived but are not needed: carryovers do not pass through Form 8949.

Not archived, needed for the refusals only, not for the computation:
- Pub. 4681 (canceled debt and attribute reduction): https://www.irs.gov/pub/irs-pdf/p4681.pdf
- Form 982 and its instructions: https://www.irs.gov/pub/irs-pdf/f982.pdf, https://www.irs.gov/pub/irs-pdf/i982.pdf
- The 2024 Instructions for Schedule D, only if the owner wants the 2024 worksheet itself archived for the
  "carryover into 2024" chain. It is not needed because the inputs are 2024 return lines:
  https://www.irs.gov/pub/irs-prior/i1040sd--2024.pdf

---

## 3. Line map

### 3.1 Capital Loss Carryover Worksheet, Lines 6 and 14 (new worksheet; proposed id `clcw`, return-level)

Applicability: i1040sd p. 10, Capital Loss Carryover Worksheet, "Use this worksheet to figure your capital
loss carryovers from 2024 to 2025 if your 2024 Schedule D, line 21, is a loss and (a) that loss is a smaller
loss than the loss on your 2024 Schedule D, line 16; or (b) if the amount on your 2024 Form 1040, 1040-SR or
1040-NR, line 15 would be less than zero if you could enter a negative amount on that line. Otherwise, you
don't have any carryovers."

**Property (checked numerically, not in the text).** When neither (a) nor (b) holds, lines 8 and 13 come out
zero from the arithmetic alone. When the worksheet applies, line 8 plus line 13 equals the 2024 net loss less
the smaller of the allowable deduction and taxable income increased by it, which is Pub. 550's rule (p550
p. 102, "The amount of your capital loss carryover is the amount of your total net loss that is more than the
lesser of"). I checked both by brute force over 200,000 random (taxable income, line 7, line 15) triples with
no violation. The applicability test therefore needs no gate line; it can be a class D property.

| Line | Printed text (i1040sd p. 10) | Computes | Supplied by | New input |
|---|---|---|---|---|
| 1 | "Enter the amount from your 2024 Form 1040, 1040-SR, or 1040-NR, line 15. If the amount would have been a loss if you could enter a negative number on that line, enclose the amount in parentheses" | Signed 2024 taxable income before the zero floor | none | Either two inputs, 2024 Form 1040 line 11 (Dollars) and line 14 (NonNegDollars), with line 1 = `subtract` (line 11 − line 14); or one signed input (D2). [2024] f1040: line 15 "Subtract line 14 from line 11. If zero or less, enter -0-. This is your taxable income"; line 14 "Add lines 12 and 13". |
| 2 | "Enter the loss from your 2024 Schedule D, line 21, as a positive amount" | 2024 deductible loss | none | `clcw.prior_sd21`, NonNegDollars (D3) |
| 3 | "Combine lines 1 and 2. If zero or less, enter -0-" | `sum` helper (Dollars), then `subtract_floor0` (helper − 0), as `g28.combined` and `g28.line7` do | lines 1, 2 | none |
| 4 | "Enter the smaller of line 2 or line 3" | `smaller_of` (the 2024 allowable deduction actually usable) | lines 2, 3 | none |
| skip | "If line 7 of your 2024 Schedule D is a loss, go to line 5; otherwise, enter -0- on line 5 and go to line 9." | no line; line 5 is 0 when line 7 is not a loss, and then line 8 is 0 too | none | none |
| 5 | "Enter the loss from your 2024 Schedule D, line 7, as a positive amount" | `subtract_floor0` (0 − prior line 7) | none | `clcw.prior_sd7`, Dollars, signed. [2024] f1040sd line 7: "Net short-term capital gain or (loss). Combine lines 1a through 6 in column (h)." |
| 6 | "Enter any gain from your 2024 Schedule D, line 15. If a loss, enter -0-" | `subtract_floor0` (prior line 15 − 0) | none | `clcw.prior_sd15`, Dollars, signed. [2024] f1040sd line 15: "Net long-term capital gain or (loss). Combine lines 8a through 14 in column (h)." |
| 7 | "Add lines 4 and 6" | `sum` | lines 4, 6 | none |
| 8 | "Short-term capital loss carryover for 2025. Subtract line 7 from line 5. If zero or less, enter -0-. If more than zero, also enter this amount on Schedule D, line 6" | `subtract_floor0` | lines 5, 7 | none |
| skip | "If line 15 of your 2024 Schedule D is a loss, go to line 9; otherwise, skip lines 9 through 13." | no line; line 9 is 0, so line 13 is 0 | none | none |
| 9 | "Enter the loss from your 2024 Schedule D, line 15, as a positive amount" | `subtract_floor0` (0 − prior line 15) | `clcw.prior_sd15` | none |
| 10 | "Enter any gain from your 2024 Schedule D, line 7. If a loss, enter -0-" | `subtract_floor0` (prior line 7 − 0) | `clcw.prior_sd7` | none |
| 11 | "Subtract line 5 from line 4. If zero or less, enter -0-" | `subtract_floor0` | lines 4, 5 | none |
| 12 | "Add lines 10 and 11" | `sum` | lines 10, 11 | none |
| 13 | "Long-term capital loss carryover for 2025. Subtract line 12 from line 9. If zero or less, enter -0-. If more than zero, also enter this amount on Schedule D, line 14" | `subtract_floor0` | lines 9, 12 | none |

2024 Schedule D line 16 is not an input. The worksheet reads it only in its applicability sentence, which the
property above makes redundant, and [2024] f1040sd line 16 is "Combine lines 7 and 15 and enter the result".

Guarding: when the gate question (`sd.carryover`, reworded per D1) is false, the five inputs are not asked.
Lines 6 and 14 then need a `choose` on the gate (true → worksheet, false → `sd.zero`), so that unknown
2024 inputs never reach Schedule D. Every result is money, so `choose` is allowed (spec 4.2; the Stage 15
correction that `choose` branches must be money).

**Rounding.** The worksheet has no division and no rate. Integer cents in, integer cents out.

**Pub. 550 counterpart.** p550 p. 102, Worksheet 4-1, matches i1040sd line for line. The wording differs at
line 1 ("If the amount would have been a loss and if you could enter a negative number on that line"), at
line 8 ("carryover to 2025" against i1040sd's "carryover for 2025"), and by adding "(Form 1040)" after each
"Schedule D".

### 3.2 Schedule D (f1040sd)

| Line | Printed text | Now (`forms/2025/sd.yaml`) | Proposed |
|---|---|---|---|
| 6 | f1040sd p. 1, "Short-term capital loss carryover. Enter the amount, if any, from line 8 of your Capital Loss Carryover Worksheet in the instructions". The entry is printed in parentheses. | `sd.line6`: copy `sd.zero`; refuses on `sd.other_forms` and `sd.carryover` | `choose` on the gate: `subtract` (`sd.zero` − `clcw.line8`), held negative (D4); no refusal (line 6 carries no K-1 amount) |
| 14 | f1040sd p. 1, "Long-term capital loss carryover. Enter the amount, if any, from line 13 of your Capital Loss Carryover Worksheet in the instructions". The entry is printed in parentheses. | `sd.line14`: copy `sd.zero`; same refusals | the same, from `clcw.line13` |
| 7 | f1040sd p. 1, "Net short-term capital gain or (loss). Combine lines 1a through 6 in column (h)." | `sum` including `sd.line6` | unchanged if line 6 is held negative; under the other D4 reading, `subtract` |
| 15 | f1040sd p. 1, "Net long-term capital gain or (loss). Combine lines 8a through 14 in column (h)." | `sum` including `sd.line14` | the same |
| 16 | f1040sd p. 2, "Combine lines 7 and 15 and enter the result" | `sum` | unchanged |
| 21 | f1040sd p. 2, "If line 16 is a loss, enter here and on Form 1040, 1040-SR, or 1040-NR, line 7a, the smaller of", followed by "The loss on line 16; or", followed by "($3,000), or if married filing separately, ($1,500)" | `sd.line21`: `choose` on `sd.has_loss`, `larger_of` (line 16, `sd.loss_limit`) | unchanged; the limit is already in params (section 7) |
| (helper) | — | `sd.carryover`, the refusal input | becomes the gate (D1); refusals removed from `sd.count`, lines 4, 5, 11, 12 (kept for `sd.other_forms`) and lines 6, 14 |
| (helper) | — | `sd.filed`: any of count > 0, `sd.line18` > 0, `sd.line19` > 0 | add `sd.line6` < 0 or `sd.line14` < 0 (section 4.4) |

### 3.3 Carryover to 2026 (display; proposed id `clcw26`)

Text: i1040sd p. 14, Line 21, "You have a capital loss carryover from 2025 to 2026 if you have a loss on line 16
and either", followed by "That loss is more than the loss on line 21; or" and "The amount on Form 1040,
1040-SR, or 1040-NR, line 15, would be less than zero if you could enter a negative amount on that line." Then
"To figure any capital loss carryover to 2026, you will use the Capital Loss Carryover Worksheet in the 2026
Instructions for Schedule D. If you want to figure your carryover to 2026 now, see Pub. 550."

Pub. 550 gives the rule but prints no 2025-to-2026 worksheet. Its Worksheet 4-1 is "from 2024 to 2025"
(p550 p. 102). The rule, p550 p. 102: "The amount of your capital loss carryover is the amount of your total
net loss that is more than the lesser of", then "1. Your allowable capital loss deduction for the year, or" and
"2. Your taxable income increased by your allowable capital loss deduction for the year." Negative taxable
income: "If your deductions are more than your gross income for the tax year, use your negative taxable income
in figuring the amount in (2) above." Ordering: "When you figure your capital loss carryover, use your
short-term capital losses first, even if you incurred them after a long-term capital loss." Character: "When
you carry over a loss, it remains long-term or short-term."

Proposed encoding: a second instance of the 13 lines, with "2024 return" read as this 2025 return (an inference
recorded in the ambiguity register; open question Q5).
- line 1 = new helper `subtract` (`f1040.line11b` − `f1040.line14`), signed. `f1040.line15` is
  `subtract_floor0` of the same two lines (`forms/2025/f1040.yaml`).
- line 2 = 0 − `sd.line21`.
- line 5 = max(0, −`sd.line7`).
- line 6 = max(0, `sd.line15`).
- line 9 = max(0, −`sd.line15`).
- line 10 = max(0, `sd.line7`).

Lines 8 and 13 are `display` lines ("Short-term/Long-term capital loss carryover to 2026"), read by no other
line (spec 4.3 `display`). Class A evidence is available for the total: p550 p. 102, Example, "The unused part
of the loss, $4,000 ($7,000 − $3,000), can be carried over to 2026." The checker cannot match that quote
because of the minus sign, so it is cited here without quotation.

For a later year, the 2025 display is exactly the 2026 input. Under spec 6.7 (fixtures across years) a 2026
return could take it from the 2025 values sheet rather than from the filer. That is a note for the 2026 diff,
not this stage.

### 3.4 28% Rate Gain Worksheet (`forms/2025/g28.yaml`) and Unrecaptured Section 1250 Gain Worksheet (`forms/2025/u1250.yaml`)

| Line | Printed text | Now | Proposed |
|---|---|---|---|
| g28 5 | i1040sd p. 11, 28% Rate Gain Worksheet, "Enter your long-term capital loss carryovers from Schedule D, line 14; and Schedule K-1 (Form 1041), box 11, code D". The entry is printed in parentheses. | `g28.line5`: NonNegDollars, copy `div.screen` | Dollars, copy `sd.line14` (negative under D4). The K-1 part stays refused by `sd.other_forms` until Schedule E. |
| g28 7 | i1040sd p. 11, "Combine lines 1 through 6. If zero or less, enter -0-. If more than zero, also enter this amount on Schedule D, line 18" | `subtract_floor0` (`g28.combined` − `sd.zero`) | unchanged; the carryover can now zero it while 1099-DIV box 2d is above zero (section 4.4) |
| u1250 16 | i1040sd p. 13, "Enter your long-term capital loss carryovers from Schedule D, line 14; and Schedule K-1 (Form 1041), box 11, code D*". The entry is printed in parentheses. | `u1250.line16`: NonNegDollars, copy `div.screen` | Dollars, copy `sd.line14`. The footnote: "If you are filing Form 2555 (relating to foreign earned income), see the footnote in the Foreign Earned Income Tax Worksheet in the Instructions for Form 1040 before completing this line." Form 2555 stays refused (`sa.excluded_income`, `scope.other_income`). |
| u1250 17 | i1040sd p. 13, "Combine lines 14 through 16. If the result is a (loss), enter it as a positive amount. If the result is zero or a gain, enter -0-" | `subtract_floor0` (`sd.zero` − `u1250.combined`) | unchanged; it already handles a negative line 16 |

Recorded earlier: the second transcriptions of both worksheets chose "copy sd.line14 as a signed loss (zero or
negative)" (`reviews/2025/transcription/g28.md` line 48; `u1250.md` line 234: "it is held as a signed amount
(a loss is negative), the same sign convention as Schedule D, line 14"). The render ruling on g28 line 5 said:
"A carryover must be entered here as a loss when carryovers co[me into scope]"
(`reviews/2025/render/g28.md` line 58).

---

## 4. Rules

### 4.1 The limit and character
- i1040sd p. 3, Capital Losses: "You can deduct capital losses up to the amount of your capital gains plus
  $3,000 ($1,500 if married filing separately)."
- p550 p. 101, Limit on deduction: "Your allowable capital loss deduction, figured on Schedule D (Form 1040),
  is the lesser of".
- p550 p. 102: "When you figure the amount of any capital loss carryover to the next year, you must take the
  current year's allowable deduction into account, whether or not you claimed it and whether or not you filed a
  return for the current year." This bears on D3.
- p550 p. 102: "A long-term capital loss you carry over to the next tax year will reduce that year's long-term
  capital gains before it reduces that year's short-term capital gains." Schedule D already does this by placing
  line 14 in Part II.

### 4.2 Joint and separate returns
- i1040sd p. 10: "If you and your spouse once filed a joint return and are filing separate returns for 2025, any
  capital loss carryover from the joint return can be deducted only on the return of the spouse who actually had
  the loss."
- p550 p. 103, Joint and separate returns: "If you and your spouse once filed separate returns and are now
  filing a joint return, combine your separate capital loss carryovers."

MFS is refused project-wide (`s3.mfs` in `scope.ready`), so the first sentence matters here only when the 2025
status is single, head of household or qualifying surviving spouse after a 2024 joint return. That happens on
divorce, on separation with HOH, or on the death of the spouse in 2024. The second sentence matters when both
spouses filed 2024 returns that were not joint.

### 4.3 Decedent
p550 p. 103, Decedent's capital loss: "A capital loss sustained by a decedent during the decedent's last tax year
(or carried over to that year from an earlier year) can be deducted only on the final income tax return filed
for the decedent." and "The decedent's estate cannot deduct any of the loss or carry it over to following
years."
- Spouse died in 2024, 2025 return QSS or single: the decedent's share of the 2024 joint carryover is gone, so an
  allocation is needed (refuse; D6).
- Spouse died in 2025, 2025 joint return: the joint return is the decedent's final return, so the 2025
  computation is unaffected. Only the carryover to 2026 display overstates what survives (Q4). The project has
  no general "died in 2025" fact. `person.died_before_65` is a narrow Schedule 1-A question
  (`forms/2025/person.yaml` line 129).

### 4.4 When Schedule D is required
i1040gi p. 31, Line 7a, Exception 1: "You have no capital losses, and your only capital gains are capital gain
distributions from Form(s) 1099-DIV, box 2a (or substitute statements); and". A carryover is a capital loss, so a
filer whose only capital items are a carryover and box 2a distributions must file Schedule D. `sd.filed` has to
become true on a nonzero line 6 or 14. That changes `qdcg.line3` (Yes branch, `sd.net_gain`, in place of
`sd.distributions`) and `f1040.gate.qdcg_applies` (its "not filing Schedule D and distributions" disjunct
gives way to `sd.line17`).

The same change settles the carryover half of T-003. The netting worry recorded in
`reviews/2025/transcription/sd.md` (line 85: "If carryovers come into scope the netting could ze[ro]") arises
only when `g28.line5` or `u1250.line16` is nonzero, which now implies `sd.line14` < 0 and so `sd.filed`. Inside
the slice this is my inference from the encoding; the raw-box test is still the cleaner form.

### 4.5 Form 4952 and Form 8960
- f4952 p. 3, Line 4d: "When figuring this amount, include capital gain distributions from mutual funds and
  capital loss carryovers." `f4952.line4d` is `subtract_floor0` (`sd.line16` − 0), which includes them once lines
  6 and 14 are filled. Line 4e, f4952 p. 3: "Net capital gain from the disposition of property held for
  investment is the excess, if any, of your net long-term capital gain over your net short-term capital loss".
  `f4952.line4e` reads `sd.net_gain`, which includes them.
- Form 8960 line 5a reads `f1040.line7a`, the limited loss (`forms/2025/f8960.yaml`). Its form note reads: "NIIT
  uses the limited capital loss on Form 1040 line 7a, not the unlimited Schedule D loss." That includes the
  carryover; no change.
- i8960 p. 9, Adjustments to your capital loss carryforwards: "Starting in 2014, capital loss carryforwards must
  be adjusted if any sum of all capital gain or loss amounts excluded from NII on lines 5b and 5c was a net
  loss". The Net Gains and Losses Worksheet (i8960 p. 10) carries the adjustment through two lines:
  - line 2(h): "Enter the amount reported on line 2(i) of this worksheet from your prior tax year return
    calculations. Enter as a positive number".
  - line 2(i): "If you don't have a capital loss carryover to next year, then skip this line and go to line
    2(j). Otherwise, enter the lesser of (i)(1) or (i)(2) as a negative amount". Its (i)(2) is "The amount of
    capital loss carried over to next year (Schedule D (Form 1040), line 16, less the amount allowed as a current
    deduction on Schedule D (Form 1040), line 21) entered as a positive number".

  Inside the slice, lines 2(a) to 2(g) and 3 are zero, because `f8960.unsupported` refuses "a disposition
  adjustment" and pass-through income. So (i)(1) is just 2(h), and line 5b is nonzero only when the 2024 return
  had a 2(i) amount. That requires a 2024 excluded net capital loss (for example a non-section 1411 business
  asset), which is rare. Recommendation D8: refuse a nonzero 2024 line 2(i).

### 4.6 Estate and trust carryovers (K-1)
i1041sk1 p. 3, Box 11, Codes C and D: "A short-term capital loss carryover, reported as code C, is reported on
Schedule D (Form 1040), line 5." and "A long-term capital loss carryover, reported as code D, is reported, as
appropriate, on Schedule D (Form 1040), line 12; line 5 of the 28% Rate Gain Worksheet-Line 18 in the Schedule D
(Form 1040) instructions; and line 16 of the Unrecaptured Section 1250 Gain Worksheet-Line 19 in the Schedule D
(Form 1040) instructions." These go on lines 5 and 12, not 6 and 14. They stay refused by `sd.other_forms`
('capital gains or losses on a Schedule K-1') until the Schedule E stage, which must add them to `g28.line5` and
`u1250.line16` (section 5.4).

### 4.7 Canceled debt
i1040sd p. 10: "If you excluded canceled debt from income in 2025, see Pub. 4681." (the same in p550 p. 102). From
general knowledge, not archived: section 108(b)(2)(F) reduces capital loss carryovers by excluded canceled debt,
figured on Form 982. Refuse (D7).

---

## 5. Ordering and every existing line that changes

### 5.1 Lines edited
| Id | Change |
|---|---|
| `sd.carryover` | Reworded gate (D1); no longer a refusal on its own |
| `sd.count` | Drop the `sd.carryover` refusal (keep `sd.other_forms`) |
| `sd.line4`, `sd.line5`, `sd.line11`, `sd.line12` | Drop the `sd.carryover` refusal |
| `sd.line6`, `sd.line14` | Copy `sd.zero` becomes a guarded negative of `clcw.line8` and `clcw.line13`; labels become the printed text; refusals dropped. A Dollars type is already declared. |
| `sd.line7`, `sd.line15` | None if negative (D4), otherwise `subtract` |
| `sd.filed` | Add the line 6 or line 14 nonzero test (section 4.4) |
| `g28.line5`, `u1250.line16` | NonNegDollars copy `div.screen` becomes Dollars copy `sd.line14` |
| form notes of `sd`, `g28`, `u1250` | Drop "prior-year carryovers are refused" |
| `f4952.carryover`, `f4952.line2` (if B0 folded in) | Refusal becomes a 2024 Form 4952 line 7 input. Not read in detail here: check `forms/2025/f4952.yaml` lines 1 to 60 for the current line 2 encoding. |
| `f8960.unsupported` (or a new gate) | Add the prior-year line 2(i) amount (D8) |
| new `f1040` helper | Signed line 11b − line 14, for `clcw26` line 1 |
| `engine/src/mutate.ts` lines 234 to 241 | The equivalence notes "operand.sd.sd.line6.zero", "operand.sd.sd.line14.zero" and "operand.sd.sd.line7.line6" say lines 4, 5 and 6 are "identically zero with identical refusal gates". That stops being true for lines 6 and 14, so those entries must go or mutants on lines 6 and 14 go unexamined. |
| `engine/src/compare.ts`, `tools/engines/generate_cases.py` | Defaults for the new inputs. The engine facts `short_term_gain` and `long_term_gain` must include the carryover (section 5.3). |
| `tools/coverage/categories.json` | `capital_loss_carryover`: gates `[]` and label "supported since Stage 20", following the `schedule_c` pattern |
| `spec/spec.md` 2.2 and 2.4, `TASKS.md` T-003, T-004, T-012 | Scope text |

### 5.2 Downstream readers that change value with no edit (checked by grep for `sd.` and `f1040.line7a` readers in `forms/2025/`)
- `f1040.line7a` (copy `sd.to1040`), which feeds `f1040.line9`, `line11a` and `line11b`. Through those it reaches
  every AGI reader: Schedule 1-A phase-outs, student loan interest, the 8812 worksheets, the EIC, Form 8880 line
  8 and Form 2441 line 7 (Stage 15), and the Form 8959 and 8960 MAGI.
- `eic.gain_7a` (Step 2 investment income, line 7a floored at zero).
- `f8960.line5a`.
- `f4952.line4d` (`sd.line16`) and `f4952.line4e` (`sd.net_gain`).
- `qdcg.line3` (via `sd.filed` and `sd.net_gain`), `qbi` line 134 (`sd.net_gain`).
- `sdtw.line7` (`sd.line15`, `sd.line16`), `sdtw.line11` and `sdtw.use28`/`use1250` (`sd.line18`, `sd.line19`).
- `f1040.gate.qdcg_applies` and `f1040.gate.sdtw` (`sd.filed`, `sd.line17`, `sd.line18`, `sd.line19`).
- `g28.line6`, `u1250.line15` (`sd.line7`).

There is no credit ordering in this stage. The carryover changes income, and so it changes every
income-dependent credit through AGI and the tax.

### 5.3 Engine differential
The generator gives the engines "net short- and long-term gain" from the raw amounts
(`tools/engines/README.md`; Tax-Calculator `p22250`/`p23250`, PolicyEngine `short_term_capital_gains`/
`long_term_capital_gains`, in `tools/engines/run_engines.py` lines 170 to 173 and 245). Feeding the
carryover-adjusted nets lets the engines check line 21, the limit and everything downstream, but not the
worksheet itself. I have not checked whether either engine has a native carryover input. The worksheet
arithmetic needs class M fixtures (spec 6.2) on both sides of each `subtract_floor0` and `smaller_of`: line 3 at
zero, line 4 both ways, lines 8, 11 and 13 at zero.

### 5.4 Dependencies on other stages
- Schedule E (roadmap item 3): K-1 (Form 1041) box 11 code D must be added to `g28.line5` and `u1250.line16`,
  and code C/D amounts to lines 5 and 12 (section 4.6).
- Form 1040 line 1z (T-002) is unaffected.
- MFS (roadmap item 8) reuses the existing `sd.loss_limit` mfs value (-150000) and must take up the "spouse who
  actually had the loss" rule (section 4.2).

---

## 6. Refuse-or-compute candidates

| # | Situation | Why it is hard | Recommendation |
|---|---|---|---|
| R1 | Simple carryover: one 2024 return (the same filer, or the same spouse jointly), any 2025 status in scope | none: 5 inputs, 13 lines | **Compute** |
| R2 | 2025 MFJ; both spouses filed non-joint 2024 returns, each with a loss carryover | Two worksheets summed (p550 p. 103, "combine your separate capital loss carryovers"); needs a 2-entry collection or per-person inputs | **Refuse** (D5). If only one spouse's 2024 return carries a loss, compute from that return. |
| R3 | 2024 joint return with someone who is not the 2025 joint spouse (divorce, separation, spouse died in 2024) | Allocation to "the spouse who actually had the loss" needs records the 2024 return does not show | **Refuse** (D6) |
| R4 | Spouse died in 2025, 2025 MFJ | 2025 is fine; the 2026 carryover is overstated by the decedent's share | **Compute**, with a caveat on the 2026 display (Q4) |
| R5 | Canceled debt excluded in 2025 (Form 982) | Section 108(b) attribute reduction; Pub. 4681 and Form 982 not archived | **Refuse** (D7) |
| R6 | Prior-year Form 8960 line 2(i) amount | NIIT carryforward adjustment (i8960 p. 9) | **Refuse** (D8) |
| R7 | K-1 (Form 1041) box 11 codes C/D | Belongs to Schedule E | Stays refused by `sd.other_forms` |
| R8 | AMT capital loss carryover differs from the regular one | Form 6251 | Stays refused by `s2.amt` |
| R9 | Inconsistent 2024 inputs: line 21 above $3,000, or above the loss on line 7 + line 15, or above zero when line 7 + line 15 ≥ 0 | Data error | **Refuse** with a "check your 2024 Schedule D" remedy (as `f4952.bad_election` does) |
| R10 | No 2024 return filed, or a 2024 Schedule D never prepared although a loss carried into 2024 | p550 p. 102: "whether or not you filed a return for the current year" | Compute; interview help tells the filer to figure the 2024 lines as they should have been (Q3) |
| R11 | 2024 return amended or adjusted by the IRS | none | Compute from the corrected figures (interview help) |
| R12 | 2024 Form 1040-NR (2025 resident) | The worksheet names 1040-NR line 15 | Compute; same line numbers. I did not check the 2024 1040-NR (not archived). |

---

## 7. Parameters (`params/2025.yaml`)

No new rate or threshold is required. The existing entry is `sd.loss_limit`: single -300000, mfj -300000, mfs
-150000, hoh -300000, qss -300000, type Dollars, cited `f1040sd` "Schedule D (2025), Parts I–III"
(`params/2025.yaml` line 994). Its value matches f1040sd p. 2, line 21, "($3,000), or if married filing
separately, ($1,500)". The locator could be tightened to "p. 2, line 21".

Optional, for the R9 check: `clcw.prior_limit` = 300000 (NonNegDollars), cited [2024] f1040sd p. 2, line 21,
"($3,000), or if married filing separately, ($1,500)". The 2024 figure is the same, checked against
`sources/2024/f1040sd.cols.txt` p. 2. A 2024 MFS return reaching this test would need 150000. That is only
possible when R2 does not apply (2025 MFJ, one 2024 MFS return with the loss), so the check should use the
$3,000 bound or an input for the 2024 status.

---

## 8. Open questions

- **Q1. Line 2: printed or allowable?** Worksheet line 2 says to enter the loss "from your 2024 Schedule D, line
  21". p550 p. 102 says the current year's "allowable deduction" counts "whether or not you claimed it". If the
  filer's 2024 line 21 was understated (for example left blank), the printed figure and the allowable figure
  differ. Reading A: take the figure as printed. Reading B: recompute line 2 as the smaller of the 2024 net loss
  and the 2024 limit, which needs the 2024 filing status.
- **Q2. Line 1 when 2024 line 15 was floored.** The worksheet asks for the would-be negative amount. Should the
  interview ask for 2024 lines 11 and 14 (two printed numbers, no hand computation), or for one signed figure
  with help text?
- **Q3. No usable 2024 return.** For a filer who did not file in 2024, or whose 2024 Schedule D omitted a
  carryover from 2023, the inputs are figures the filer must reconstruct. Should the tool accept them with a
  notice, or refuse?
- **Q4. The 2026 display after a 2025 death.** With a 2025 MFJ return where a spouse died in 2025, the 2026
  carryover shown includes the decedent's share, which does not carry (p550 p. 103). Should the display carry a
  standing caveat, or be hidden (`shown_when`) behind a new 'did a spouse die in 2025' fact?
- **Q5. Applying the 2025 worksheet to the 2025 return for the 2026 display.** i1040sd p. 14 points to the 2026
  instructions or Pub. 550. Pub. 550 gives the rule in prose and a worksheet dated "from 2024 to 2025". Reading
  the same 13 lines with every "2024" as "2025" is an inference (consistent with the rule, as checked
  numerically in section 3.1) and belongs in the ambiguity register.
- **Q6. Gate wording.** Should the gate ask about the 2024 Schedule D ('Did line 21 of your 2024 Schedule D
  show a loss?'), or keep 'a capital loss carried into 2025 from any earlier year'? The first is checkable
  against a document. The second is the familiar phrase but can be answered yes with a worksheet result of zero,
  which is harmless.
- **Q7. Lines 6 and 14 shown when zero.** When the gate is true but the worksheet gives zero, should Schedule D
  show line 6 or 14 as blank (zero) with Schedule D still required? Section 4.4 proposes testing the line values,
  not the gate, so that a zero carryover does not force Schedule D.

---

## 9. Draft owner decision batch

Each item has a recommended answer and the alternative.

1. **D1. Inputs.** Recommended: compute the worksheet from five 2024 figures (2024 Form 1040 lines 11 and 14;
   2024 Schedule D lines 7, 15 and 21), behind a reworded gate. Alternative: accept the two carryover amounts
   (worksheet lines 8 and 13) as inputs, which is less evidence and no check.
2. **D2. Line 1.** Recommended: two printed inputs, 2024 lines 11 and 14, with line 1 as their signed
   difference. Alternative: one signed input with help text.
3. **D3. Line 2.** Recommended: as printed on 2024 Schedule D line 21, with the R9 consistency refusal, and
   reading A recorded in the ambiguity register. Alternative: recompute the allowable amount, which needs the
   2024 status.
4. **D4. Sign convention (T-004).** Recommended: hold Schedule D lines 6 and 14, `g28.line5` and `u1250.line16`
   negative (Dollars), so that lines 7 and 15 and the worksheets' sums stay sums, as the second transcriptions
   chose and as `sd.line21` and `g28.line6` already do. Alternative: positive amounts with lines 7, 15 and the
   worksheet combinations rewritten as subtractions.
5. **D5. Spouses with two 2024 returns.** Recommended: refuse when both spouses' non-joint 2024 returns carry a
   loss into a 2025 joint return; compute from the one return otherwise. Alternative: a two-entry collection of
   2024 returns, summed.
6. **D6. A 2024 joint return with someone else.** Recommended: refuse when the 2024 return was joint and the
   2025 return is not joint with the same spouse (divorce, separation, death in 2024). Alternative: ask for the
   filer's own share and skip the worksheet.
7. **D7. Excluded canceled debt.** Recommended: refuse a carryover return that excluded canceled debt in 2025
   (Form 982, Pub. 4681). Alternative: archive Pub. 4681 and Form 982 and compute the reduction (a stage of its
   own).
8. **D8. NIIT carryforward.** Recommended: refuse a nonzero 2024 Form 8960 Net Gains and Losses Worksheet line
   2(i) (one question, asked only when Form 8960 is required and a carryover exists). Alternative: compute lines
   2(h) and 2(i) into line 5b.
9. **D9. Carryover to 2026.** Recommended: compute and display both carryovers to 2026 by the same worksheet on
   the 2025 return, with the reading in the ambiguity register and a standing caveat for a spouse who died in
   2025. Alternative: omit the display and tell the filer to use the 2026 instructions.
10. **D10. Schedule D required.** Recommended: `sd.filed` true on a nonzero line 6 or 14, which closes the
    carryover half of T-003. Alternative: also switch `sd.filed` to the raw 1099-DIV boxes now (the rest of
    T-003).
11. **D11. Form 4952 carryover.** Recommended: fold the investment interest carryover (2024 Form 4952 line 7 to
    2025 line 2) into this stage. Alternative: leave it for the backlog.
12. **D12. Engines.** Recommended: feed the engines carryover-adjusted short- and long-term nets, and cover the
    worksheet with class M fixtures. Alternative: look for native carryover inputs in PolicyEngine-US and
    Tax-Calculator first.
13. **D13. Backlog order.** Recommended: take the backlog below in the order of measured share, with the cheap
    add-ons (B0, B4, B6) folded into adjacent stages. Alternative: strict share order.

---

## 10. Verified and inferred

**Checked against the archived text:**
- Every quotation from 2025 documents in this file was run through `/tmp/premises/check_quotes.py`. The misses
  and their explanations are listed below.
- The worksheet lines 1 to 13, the applicability sentences and the joint-return sentence, against
  `i1040sd.txt` and `i1040sd.cols.txt` p. 10 and against p550 p. 102.
- Schedule D lines 6, 7, 14, 15, 16 and 21 (2025 and [2024]).
- [2024] Form 1040 lines 11, 14 and 15 (`sources/2024/f1040.cols.txt`).
- i1040sd p. 14 (line 21); p550 pp. 101 to 103; i8960 pp. 9 and 10; f4952 pp. 1 and 3; i1041sk1 p. 3; i1040gi
  p. 31.
- The project lines named in section 5, by reading `forms/2025/sd.yaml`, `g28.yaml`, `u1250.yaml`, `qdcg.yaml`,
  `sdtw.yaml` (parts), `f4952.yaml` (lines 160 to 240), `f8960.yaml` (parts), `f1040.yaml` (lines 290 to 520),
  `params/2025.yaml` (`sd.loss_limit`), and by grepping every `forms/2025/*.yaml` for `sd.` and `f1040.line7a`
  readers.
- The coverage share and IRS count, from `reports/2025/filer_coverage.md` and `categories.json`.

**Inferred, not checked:**
- That lines 8 and 13 come out zero whenever the applicability test fails, and that their sum equals the
  Pub. 550 rule. Checked numerically by brute force on my own transcription of the worksheet; not a proof and
  not a project test.
- That the coverage gain is understated by the independence assumption.
- Section 108(b)(2)(F) and Form 982 (not archived).
- The 2024 Form 1040-NR line numbers.
- Whether either engine has a carryover input.
- The current encoding of `f4952.line2` (not read).
- That 2023 homebuyer-credit repayments do not recur in 2025 (backlog B5).
- That roadmap items 1 and 2 leave the residual Schedule 1 and credit situations in the backlog unscoped.

**Quote-checker misses, with reasons.** The checker reported 33 misses in the body of the map. It reports 41 in all, because it also counts the
quotations repeated in this list. None is a misquoted IRS passage:
- **[2024] quotes** (section 3.1 table, line 1 row: "Subtract line 14 from line 11 ...", "Add lines 12 and 13";
  section 7): the checker searches only `sources/2025`. They were checked by hand against
  `sources/2024/f1040.cols.txt` and `sources/2024/f1040sd.cols.txt`.
- **Worksheet rows 1, 5 and 6 of the section 3.1 table**: the quotes are i1040sd p. 10 text (the checker found
  them in `i1040sd` and `i1040sd-html`). The row mentions only f1040 or f1040sd, so the checker looked there
  first.
- **Section 3.1, "carryover to 2025"**: the p550 wording, found in `p550`. The line also names i1040sd.
- **Pairing artifacts** on lines with several quotations, where the checker paired a closing quote with the next
  opening quote (sections 4.5, 7 and 8, B0, B6). Every passage there was rechecked singly with the checker's own
  normalisation and found: f4952 (3 passages), iw2w3 (2), f1040s2 (3), i8960 (2), p550 (4), f1040sd (1),
  f1040s1 (1).
- **Not IRS text**:
  - Report and category headings ("Refused situations", the SOI column headers in `categories.json`).
  - Project YAML, identifiers and review files (`mutate.ts` keys, "Schedule D (2025), Parts I–III" from
    `params/2025.yaml`, the bracketed "co[me into scope]" and "ze[ro]" from `reviews/2025/`).
  - The spec ("Deferred, not dropped").
  - The engines README ("net short- and long-term gain").
  - Proposed labels ("supported since Stage 20", "Short-term/Long-term capital loss carryover to 2026", "check
    your 2024 Schedule D").
  - My own phrases ("carryover into 2024", "not filing Schedule D and distributions", "prior-year carryovers are
    refused").

---

## Backlog: the smaller situations after Form 5329 (roadmap item 9), by measured share

Shares and counts are from `reports/2025/filer_coverage.md`. Married filing separately (2.6%) comes next in the
report, but it is roadmap item 8 and not a small situation, so it is not sketched. The Schedule 1 and credit
residuals are listed because roadmap items 1 and 2 name only some of their group (spec 2.4: "among them a
taxable state refund, other income, gambling winnings and the IRA deduction"). The owner may have scoped them
there already.

| Rank | Situation (category) | Share | IRS returns | Gate | Group gain if alone |
|---|---|---|---|---|---|
| 1 | Farm income or loss (`farm`) | 1.1% | 1,743,031 | `scope.schedule1` | +0.3 |
| 2 | Sales of business property, Form 4797 (`form4797`) | 1.1% | 1,720,509 | `scope.schedule1` | in group 2 |
| 3 | Other nonrefundable credits (`other_nonrefundable`) | 0.9% | 1,467,567 | `scope.credits` | in group 1 |
| 4 | Wages or tips not on Form W-2, dependent care benefits, other earned income (`wages_not_w2`) | 0.8% | 1,267,621 | `scope.other_income` | +0.5 |
| 5 | Net operating loss deduction (`nol`) | 0.6% | 1,019,019 | `scope.schedule1` | in group 2 |
| 6 | Penalty on early withdrawal of savings (`early_withdrawal`) | 0.6% | 904,938 | `scope.schedule1` | in group 2 |
| 7 | Household employment, uncollected tip taxes, homebuyer repayment (`schedule2_other`) | 0.4% | 574,187 | `s2.other` | +0.3 (with AMT) |
| 8 | Taxable HSA distributions (`hsa_distribution`) | 0.3% | 464,689 | `f8889.unsupported` | in group 2 |
| 9 | Foreign earned income exclusion, Form 2555 (`foreign_earned_income`) | 0.3% | 432,724 | `sa.excluded_income` | in group 2 |
| 10 | Cancellation of debt (`cancellation_of_debt`) | 0.2% | 386,021 | `scope.schedule1` | in group 2 |
| 11 | Alimony paid / received (`alimony_paid`, `alimony_received`) | 0.2% / 0.1% | 278,541 / 183,582 | `scope.schedule1` | in group 2 |
| 12 | Alternative minimum tax (`amt`) | 0.1% | 150,167 | `s2.amt` | with 7 |

Unmeasured deferrals of spec 2.2 that roadmap item 9 also names follow the table as B0 and B13 to B16.

**B0. Investment interest carryover (`f4952.carryover`, unmeasured).** f4952 p. 1 line 2, "Disallowed investment
interest expense from 2024 Form 4952, line 7". Line 7 is already computed for 2025 as the carryforward, "to be
carried forward to 2026". One input replaces a refusal. The filing exception changes too: f4952 p. 3, "You don't
have any carryover of disallowed investment interest expense from 2024.", so a carryover forces the form. Sources
are archived. Recommended to fold into Stage 20 (D11).

**B1. Farm income, Schedule F (1.1%).** Schedule F with its cash and accrual parts. It flows to Schedule 1 line 6
and Schedule SE, with the farm optional method (i1040sse is archived). It interacts with Form 4562 (built in
Stage 14), the QBI deduction, the EIC earned income, and possibly Form 4835, Schedule J income averaging,
Commodity Credit Corporation loans and crop insurance deferral. None of the farm documents is archived
(Schedule F and instructions: https://www.irs.gov/pub/irs-pdf/f1040sf.pdf, https://www.irs.gov/pub/irs-pdf/i1040sf.pdf;
Pub. 225: https://www.irs.gov/pub/irs-pdf/p225.pdf). Its microdata share before raking is 0.1% against an IRS 1.1%.
Its structure resembles Schedule C, so a first cut could mirror `sc.yaml` and refuse income averaging, accrual
inventories, CCC loans and the optional method. It is the largest single situation left, but a sizeable stage.

**B2. Form 4797 (1.1%).** Business property sales: Part I section 1231 netting with the five-year lookback, Part
II ordinary gain, Part III depreciation recapture (sections 1245 and 1250). It feeds Schedule D line 11 and the
Unrecaptured Section 1250 Gain Worksheet lines 1 to 9, now `div.screen` zeros (`u1250.yaml`). It is the natural
next stage after Schedule C (sold business assets) and rental (Schedule E). Form 4797 and its instructions are
not archived (https://www.irs.gov/pub/irs-pdf/f4797.pdf, https://www.irs.gov/pub/irs-pdf/i4797.pdf). It is hard:
it needs prior-year section 1231 losses, an input like this stage's, and per-asset recapture. Recommend after
Schedule E, with installment sales (Form 6252) and like-kind exchanges (Form 8824) refused.

**B3. Other nonrefundable credits (0.9%).** One IRS total over many credits: general business (Form 3800),
adoption (8839), clean vehicles (8936), the credit for the elderly or disabled (Schedule R), mortgage interest
(8396), prior-year minimum tax (8801) and others. The SOI table may split them; that needs pandas, which did not
load here. The shares within it are unmeasured, so a first step is to split the category in
`categories.json` from `soi-23in33ar` columns. None of these forms is archived. Candidates by simplicity:
Schedule R (age or disability, income limits, a fixed table), Form 8936 (now with OBBBA date cutoffs) and Form
8801 (needs a prior-year Form 6251).

**B4. Wages not on Form W-2 and other earned income (0.8%).** Form 1040 lines 1b to 1h (f1040: "Household employee
wages not reported on Form(s) W-2", "Tip income not reported on line 1a (see instructions)", "Medicaid waiver
payments not reported on Form(s) W-2 (see instructions)", "Taxable dependent care benefits from Form 2441, line
26", "Employer-provided adoption benefits from Form 8839, line 31", "Wages from Form 8919, line 6", "Other earned
income (see instructions)").
- Line 1e may come almost free from Stage 15's Form 2441 Part III (decision 6 assigns line 1e per spouse), to be
  checked once Stage 15 lands.
- Lines 1b and 1h are inputs with EIC and earned-income consequences.
- Lines 1c and 1g bring Forms 4137 and 8919 with Schedule 2 lines 5 and 6 (not archived).
- Closes T-002 (line 1z becomes the sum).

Recommended as a small stage after Stage 15: lines 1b, 1d, 1e and 1h, with 1c, 1f and 1g refused.

**B5. Penalty on early withdrawal of savings (0.6%).** Form 1099-INT box 2 ("Early withdrawal penalty", f1099int)
to Schedule 1 line 18 ("Penalty on early withdrawal of savings", f1040s1). It is one per-entry input on the
interest collection (`forms/2025/interest.yaml`) and one `sum_over`. It is the cheapest item on this list and
could ride with roadmap item 2.

**B6. Schedule 2 other taxes (0.4%).**
- Uncollected social security and Medicare tax on tips or group-term life insurance, Schedule 2 line 13 (f1040s2,
  "Uncollected social security and Medicare or RRTA tax on tips or group-term life insurance from Form W-2, box
  12"), from W-2 box 12 codes A, B, M and N (iw2w3: "Code A-Uncollected social security or RRTA tax on tips",
  "Code B-Uncollected Medicare tax on tips"). It is cheap once Stage 15 models W-2 box 12.
- Household employment tax, Schedule 2 line 9 ("Household employment taxes. Attach Schedule H"), needs Schedule
  H (not archived: https://www.irs.gov/pub/irs-pdf/f1040sh.pdf).
- The first-time homebuyer credit repayment: the 2025 Schedule 2 prints line 10 as "Reserved for future use"
  (f1040s2). The 2023 count's repayment part probably does not recur, which is an inference.

Recommend line 13 now and Schedule H as a small stage. The category should then be split.

**B7. Net operating loss deduction (0.6%).** Schedule 1 line 8a ("Net operating loss", f1040s1, printed in
parentheses). The carryover amount comes from a prior-year computation (Pub. 536, not archived:
https://www.irs.gov/pub/irs-pdf/p536.pdf), with the 80% taxable-income limit for post-2017 losses. A first cut
could take the deduction as an input with a refusal for the 80% limit. It is the same shape as this stage's
problem (prior-year figures), but the figuring is harder.

**B8. Taxable HSA distributions (0.3%).** Form 8889 Part II lines 14 to 17b and the 20% additional tax to
Schedule 2 line 17c. The project already has `f8889.yaml` (1,263 lines) with Part I. Part II and the additional
tax are refused by `f8889.unsupported`, and i8889 is archived. The additional tax overlaps Form 5329's territory
(item 7). Recommend it with or right after item 7.

**B9. Foreign earned income exclusion (0.3%).** Form 2555, which carries the Foreign Earned Income Tax Worksheet
into the QDCGT, the Schedule D Tax Worksheet line 1, the u1250 line 16 footnote and the Schedule 8812 lines 2a to
2c. It touches many lines for a small share. Form 2555 and its instructions are not archived. Recommend late.

**B10. Cancellation of debt (0.2%).** Schedule 1 line 8c ("Cancellation of debt"), from Form 1099-C. The taxable
case is one input. The excluded case is Form 982, which is this stage's R5 refusal. Recommend the taxable input
with the exclusions refused (Pub. 4681 not archived).

**B11. Alimony (0.2% paid, 0.1% received).** Schedule 1 lines 2a and 19a, with the pre-2019 instrument date
("Date of original divorce or separation agreement", f1040s1) and the recipient's SSN. Simple inputs and a date
gate; no worksheet. Cheap; it could ride with item 2.

**B12. Alternative minimum tax (0.1%).** Form 6251 (not archived: https://www.irs.gov/pub/irs-pdf/f6251.pdf,
https://www.irs.gov/pub/irs-pdf/i6251.pdf). It is a full parallel computation: exemption phase-out, a 26%/28% band
and the Part III capital gain rates that mirror the Schedule D Tax Worksheet. The measured share is small, but
`s2.amt` today also refuses filers who must merely check whether AMT applies. Most filers could be released by
the i1040gi line 2 screening worksheet, which is not checked here. Recommend computing the full form only after
the screening worksheet shows how many it still refuses.

**B13. Digital assets, Form 8949 boxes G to L (`sales.digital`, unmeasured).** i1040sd p. 1, What's New: "Codes
G, H, I, J, K, and L were added to lines 1b, 2, 3, 8b, 9, and 10 to represent the reporting of digital asset
transactions." The arithmetic is the same as boxes A to F. This is T-003's first half, widening the box tests.
Cheap; f8949 and i8949 are archived.

**B14. Other Form 8949 adjustment codes, collectibles, section 1202 and directly sold section 1250 property
(`sales.bad_code`, `sales.special`, `div.section1202`).** These fill `g28.line1` to `line3` (now `div.screen`)
and need the section 1202 exclusion fractions printed on 28% Rate Gain Worksheet line 2. Moderate; sources are
archived (f8949, i8949, i1040sd).

**B15. Form 1116 (`ftc.needs1116`, unmeasured).** Named in spec 2.2 as "Deferred, not dropped". i1116 is archived
but the form is not (https://www.irs.gov/pub/irs-pdf/f1116.pdf). The passive category alone, with the qualified
dividend and capital gain adjustments, would be the first cut. It is a sizeable stage.

**B16. Schedule A and Schedule B deferrals (unmeasured).** Investment interest carryover (B0); charitable
contributions limited by income or carried over (`sa.charity_limited`), which is again a prior-year carryover,
with Pub. 526 archived; Form 8283 Section B; and Schedule B nominee interest, OID, bond premium and the Form 8815
savings bond exclusion. Each is small. Their shares are not measured.
