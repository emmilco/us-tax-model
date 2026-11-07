# Applicability survey: formal gates for the interview

Author: claude-opus-5-5, judgment class (source reading and design survey). Main checkout at a68b8df (uncommitted
working tree as in `git status`; no repository file other than this one was written).

Purpose: the material the formal-gates design (`docs/2026-11-06_formal_gates_design.md`) is to be written from. It
answers six questions: how the evaluator decides reachability (1); the applicability conditions each form document's
archived instructions state, and how far the model already encodes them (2); the existence facts needed where no
instruction states a condition (3); how the 34 high and medium findings of the ladder review
(`research/audits/2026-11-06_t251_ladder_review.md`) fare under a design restricted to such gates (4); the
instructions' own item lists behind the complement screens (5); and a rough sizing (6).

## How this was done, and what is read vs inferred

- **Evaluator (part 1): read and run.** `engine/src/eval.ts` and `engine/src/interview.ts` were read in full. Every
  claim in part 1 was then run against the built evaluator (`engine/dist`, already built; `canonical/2025`, already
  built; both git-ignored, not rebuilt). The runs used a synthetic document `t` added in memory to the loaded
  canonical data, called through `evaluate()`, from a script in `/tmp/appsurvey/` (nothing written to the repo). An
  input counts as **asked** when some derivation's value is `unknown` with that `input` key, which is exactly how
  `interviewState` builds its question set (interview.ts line 31).
- **What the interview asks today: run.** `/tmp/appsurvey/walk.mjs` walks the `ny` profile (`interviewState`,
  first pending question each step) answering from the fixture `ny.table.single.0` (`fixtures/ny/2025/it201.json`; a
  single NYC filer with two W-2s, one interest payer with $0, nothing else). It asks **165 questions** and completes.
  This matches the "165 before T-251" in `/tmp/ladder_proposal.md`. The list of these 165 is the concrete target of the
  design: every input in it is reachable for a filer with almost nothing; every input not in it is already gated by
  something (a roster, an amount, or a Bool). Appendix A groups them.
- **Instructions (parts 2, 3, 5): read.** Quotes are from the archived reading-order text (`sources/2025/<id>.cols.txt`,
  `sources/ny/2025/<id>.cols.txt`). Page numbers are the page of the archived file. For i1040gi this equals the printed
  page (checked: pp. 91–93 end with "91", "92", "93"); for the others it matches the project's own locators where I
  compared (i1040sc p. 3 Line A, i2441 p. 2 Line 1).
- **Model (parts 2–6): read** from `forms/2025/*.yaml`, `forms/ny/2025/*.yaml` by script (labels, expressions,
  refusal gates, readers of each input).
- **Not read:** the T-251 topic file and `ladder.ts` (they live on the branch at 204cc77, not on main); `rendered/`;
  review logs. **Not archived** (so any condition resting on them is marked so): i6251, i4684, i6252, i8814, i4136,
  i8938, Pub. 519, Pub. 555, IT-214, IT-225 instructions, IT-2105.9.
- Sizing (part 6) is **arithmetic on the walk, not a run of a modified model**; it is labelled as an estimate.

---

## 1. Evaluator behaviour

### 1.1 Mechanism (eval.ts)

- **What is asked.** `interviewState` evaluates the profile targets once (interview.ts l. 27) and collects every
  derivation in the memo whose value is `unknown` and carries an `input` key (l. 31). An `unknown` keeps the `input` of
  the input it came from as it propagates, so "asked" means: some input line was evaluated, had no answer, and its
  derivation is still in the memo when evaluation ends. Questions are then sorted by bank order (l. 32–36); all
  currently reachable inputs are pending at once, the interview presents the first.
- **Memo persists across targets** (eval.ts l. 69–103): an input reachable from any target path is asked. A gate on
  one reader does not hide an input that another reader evaluates unconditionally.
- **`choose`** (l. 613–644). Guards are evaluated in order. The first true guard's `then` is evaluated and nothing after
  it (l. 636–640). A false guard's `then` is never evaluated (l. 641). If no guard is true the line is
  `unknown "no guard matched"` with **no** `input` (l. 643): nothing is asked, and the line can never become known.
  If a guard is a refusal, the line is that refusal (l. 633).
- **`choose` with an unknown guard** (`chooseUnresolved`, l. 667–697). The later guards and the `then` of every still
  possible alternative are evaluated, then every memo entry made after the first unknown guard is deleted (mark at
  l. 673, deletion at l. 693). Result: only the inputs of the guards up to the first unknown one are asked; the
  alternatives' inputs are not. Exception: if every possible way is a refusal, the line is that refusal and the memo
  is not rolled back (l. 688–692).
- **`refuses`** (l. 224–240) are evaluated **before** the line's expression, for every line that is reached.
  - Without `when_known`: gate true → the line is a refusal and its expression is not evaluated (l. 235–237); gate
    unknown → the line is the gate's unknown (marked gate-pending) and its expression is not evaluated (l. 239), so
    the line's own inputs wait until the gate is answered; gate false → the next gate, then the expression (l. 243–254).
  - With `when_known` (only 1 of the model's 451 refusal gates): the memo is snapshotted (l. 225) and, if the gate is
    unknown, restored (l. 227–231). The gate's inputs are not asked and the expression is evaluated as if no gate.
- **`shown_when`** is not read by the evaluator. It is read only by the values sheet (`output.ts` l. 47–49) and class M
  (`classm.ts` l. 90–93, 186, 292–294) to omit a printed line. It has no effect on reachability.
- **`sum_over`** (l. 394–424): roster not given → `unknown` with the roster key as `input`, so the roster question is
  asked and no entry field (l. 399). A confirmed empty roster sums to 0 and nothing else is asked. For each entry the
  `where` test is evaluated first; an entry whose test is false is skipped and its field not evaluated (l. 408–413).
  An unknown entry does not stop the loop: all entries' fields are evaluated (l. 417). For a Count field the known
  entries give a lower bound (l. 422), which a later comparison can use (l. 768–771).
- **Arithmetic** (`sum`, `subtract`, `smaller_of`, `larger_of`, `multiply_rate`, `multiply_count`, `prorate`,
  `percent_floor`, lookups): every operand is evaluated; none short-circuits on a zero. `smaller_of`/`larger_of` and
  `keyed_lookup` stop only at a refusal (l. 464, 546).
- **`test` with `all`/`any`** (l. 746–758): operands are evaluated in order; the first decisive operand (false for
  `all`, true for `any`) returns at once and later operands are not evaluated (l. 755). An **unknown operand does not
  stop the loop** (l. 754): the next operands are evaluated too. So every operand before the decisive one is evaluated
  (and asked if unknown), and when no operand is decisive, all are asked together. Nothing is rolled back.
- **`not`** passes an unknown through (l. 759–763).
- **`copy` of a definition instance** evaluates every `bind` operand in the caller frame "for the record" (l. 383–386,
  and l. 623–626 for a `choose` alternative that is an instance). Every bound operand is reachable whenever the copy
  is, whether or not the definition's line uses it. (Code reading; not run.)
- **Answers to unreachable inputs** are accepted and kept (validateInputs l. 796–821 checks all supplied inputs,
  including "values on currently unselected branches"); they do not affect any value while unreachable.

### 1.2 Runs (synthetic document, built evaluator)

`g`, `h` are Bool inputs, `a`, `b` money inputs, `z` the zero parameter. "asked" is the reachable-unknown set.

| # | Pattern | Answers | Value | Asked |
|---|---|---|---|---|
| P1 | `choose [g=true → a, g=false → z]` | none | unknown | `g` |
| | | g=false | 0 | — |
| | | g=true | unknown | `a` |
| P1b | `choose [b>0 → a, b≤0 → z]` (an amount as the gate) | none | unknown | `b` |
| | | b=0 | 0 | — |
| P2 | `sum [z, a]` | none | unknown | `a` |
| P3 | `smaller_of [z, a]` | none | unknown | `a` |
| P4 | input line with `refuses: when g` | none | unknown | `g` |
| | | g=false | unknown | the line itself |
| | | g=true | refusal | — |
| P5 | input line with `refuses: when h, when_known` | none | unknown | the line itself (not `h`) |
| P6 | `test all [g=true, h=true]` | g=false | false | — |
| | | h=false, g unanswered | false | **`g`** (evaluated before the decisive `h`) |
| | | none | unknown | `g`, `h` together |
| P6' | `test any [g=true, h=true]` | h=true, g unanswered | true | **`g`** |
| P7 | `choose [all(g,h) → a, not all(g,h) → z]` | g=false | 0 | — |
| | | none | unknown | `g`, `h` together |
| | | g=true | unknown | `h` |
| P8 | input line with `shown_when: g` | g=false | unknown | the line itself |
| P9 | line copying `a` with `refuses: when gh`, `gh = all(g,h)` | none | unknown | `g`, `h` together |
| | | g=false | unknown | `a` |
| P10 | `choose [g=true → a]` (no else) | g=false | unknown (no input) | — (never completes) |
| P11 | `sb.line2 = sum_over interest` (real) | `$interest` unanswered | unknown | `$interest` |
| | | `$interest=[]` | 0 | — |
| | | `$interest=[a]` | unknown | `interest[a].amount` |
| P12 | `sb.line2` with `$interest=[]`, screens unanswered | | unknown | `sb.unsupported` (refusal screens precede the sum) |
| P13 | refusal gate `gh2 = choose [g=true → h, g=false → const false]` on a copy of `a` | none | unknown | `g` only |
| | | g=false | unknown | `a` |
| | | g=true | unknown | `h` |
| | | g=true, h=false | unknown | `a` |
| P14 | `choose [g=true → sum(a,b), g=false → z]` | g=false | 0 | — |
| | | none | unknown | `g` only |

### 1.3 Which patterns make a gated input unreachable when the gate is false

An input `x` is unreachable on a return exactly when no reachable line evaluates it. For a gate `G`:

**Patterns that work**

1. **`choose` on `G` with an explicit else.** `x` is read only inside the alternative guarded by `G` (directly or via
   any lines below it), and every other reader of `x` is likewise only under `G`. `G` false: `x` never evaluated
   (P1, P14). `G` unknown: only `G` is asked; the alternatives' inputs are rolled back (P1, P14; l. 693). The else
   alternative is required: without it the line is unknown forever and the return never completes (P10). With a Bool
   gate, `eq true`/`eq false` alternatives are recognised as exhaustive (`guardsCover`, l. 703–729).
2. **An amount as its own gate**: `choose [x_amount > 0 → …, else → zero]` (P1b). The amount is asked; what depends on
   it being positive is not. Already used: `person.has_educator_expenses` defers `person.eligible_educator`;
   `ftc.has_tax`; `f8960.used` defers the whole Form 8960 slice (its screens `f8960.unsupported`/`refund` were not
   asked in the walk because AGI was under the threshold).
3. **Empty roster** (`sum_over` over `[]`, P11): nothing in the collection is asked. A `where` test false on an entry
   skips that entry's field.
4. **A screen behind a gate, used as a refusal gate**: the refusal `when` must be a line that is itself a `choose`
   on `G` (P13), not an `all(G, screen)` (P9).

**Patterns that do not**

- **`refuses: when G` with G false** evaluates the expression (P4): a refusal gate defers a line's inputs only while
  the gate is unknown, the opposite of an applicability gate. And refusal screens are evaluated before the line's
  amount, so a screen on a line whose amount is zero is still asked (P12: `sb.unsupported` with no interest).
- **Arithmetic with a zero operand** (P2, P3; also `multiply_rate` by a zero rate): all operands are evaluated.
- **`shown_when`** (P8): display only.
- **`all`/`any` conjunctions** are not sequencing. `G` false as the *first* operand of `all` does skip the later ones
  (P6), but: if `G` is unknown, every operand after it is asked at the same time (P6, P7, P9); and an unknown operand
  placed *before* a false `G` is asked even though the result is false (P6). Whether the screen is asked therefore
  depends on question order, not on the facts. To defer a screen behind a gate, nest a `choose` (P13).
- **Definition-instance binds** (l. 383–386): bound operands are evaluated even if the instance's line ignores them.
- **Another reader**: if any reachable line reads `x` outside the gate, `x` is asked (memo is global).

**Gate unknown**: a `choose` gate asks only itself (sequencing); a refusal gate asks only itself (it defers the line);
an `all`/`any` asks every operand it reaches.

### 1.4 What this means for the model as it stands (read)

- 154 `all`/`any` tests in the model (nested tests counted separately; within the 540 `test` lines and the guards of
  the 409 `choose` lines) mix a Bool input with a computed operand (script over `forms/`). Where the computed operand is unknown when the interview reaches it, the Bool is asked in parallel. Seen
  in the walk:
  - `ftc.needs1116 = all[has_tax, any[taxes>limit, all_passive=false, statements=false, eligible=false,
    elect=false]]`: with `ftc.taxes` unanswered, all four election conditions are asked; the walk asked them before
    `ftc.taxes` (bank order) and the fixture's foreign tax is $0.
  - `div.unsupported` contains `all[box3>0, basis_reconciled=false]`: `div.basis_reconciled` is asked while box 3
    is unknown.
  - `household.ctc_disallowed_claim = all[credit_disallowed, s8812.line8 > s8812.line11]` and
    `household.eic_disallowed_claim`: the Form 8862 question is first, so it is asked of every filer.
  - `f8880.can_take = all[contributions>0, AGI ≤ limit, …]`: contributions first, so the saver's credit inputs
    (`person.sav_roth`, `sav_able`, `sav_voluntary`, `sav_excess`, each W-2's `box12_any`) were asked of a filer whose
    AGI ($40,000) is over the $39,500 limit.
  - `ny_it201.gate.estimated_penalty`: an `any` of two `all`s; the prior-year questions are asked while the tax due
    is still unknown.
- Refusal screens attached to many lines are asked whenever any of those lines is reached:
  `sa.charity_limited` gates `sa.line6`, `8b`, `8c`, `12`, `13`, `15`, `16`, `17` (taxes, interest, gifts…), so it is
  asked of a filer with no gifts.

---

## 2. Applicability conditions by form

Legend. **Kind**: **F** = a filing obligation (a threshold for having to file the form; it does not mean amounts
below it are not taxable); **E** = an existence condition (the form has nothing to report unless something exists);
**C** = a condition on computed amounts (stated by the instructions, decidable from lines the model already has).
**Encoded**: how the model represents it today. **Unneeded if false**: inputs a false condition would make
unnecessary that are *currently asked* (from the walk; inputs not in the walk are already gated). "—" = nothing to gain.

### 2.1 Forms whose inputs are asked of nearly everyone (the walk's 165)

| Form | Instruction condition (quote, page) | Kind | Encoded today | Unneeded if false (currently asked) |
|---|---|---|---|---|
| `sb` Schedule B | i1040sb p. 1: "Use Schedule B (Form 1040) if any of the following applies. • You had over $1,500 of taxable interest or ordinary dividends. • You received interest from a seller-financed mortgage … • You have accrued interest from a bond. • … OID of less than the amount shown on Form 1099-OID. • … less than the amount shown on a Form 1099 due to amortizable bond premium. • … exclusion of interest from series EE or I U.S. savings bonds … • You received interest or ordinary dividends as a nominee. • You had a financial interest in, or signature authority over, a financial account in a foreign country or you received a distribution from, or were a grantor of, or transferor to, a foreign trust." f1040sb line 7a: "If 'Yes,' are you required to file FinCEN Form 114". i1040sb p. 2 TIP: Form 8938 "Regardless of whether you are required to file FinCEN Form 114". | $1,500: F. Bullets 2–7: E (each needs interest or dividends). Bullet 8: E (foreign account/trust). FBAR question: E, conditional on 7a yes (form text). | No gate. `sb.unsupported` (one complement of bullets 2–7 plus market discount, contingent debt, "foreign corporation reporting", "other special treatment") is a refusal screen on `sb.line2/3/6`; `sb.fbar_required`, `sb.form8938`, `sb.line8` likewise. `sb.line7a` exists but is read only by `sb.partIII` and was **not asked** in the walk; FBAR is asked without it. `sb.partIII` encodes the $1,500 F condition (`line4`/`line6` > 150000 cents, or 7a, or 8). | No interest and no dividends: `sb.unsupported` (P12), except its 5471 clause (L-34). 7a no: `sb.fbar_required`. `sb.form8938`, `sb.line8` stay (independent facts). |
| `interest` (payer roster) | i1040sb p. 1 (as above); i1040gi p. 95 line 18 (penalty). | E | Roster `$interest`; per payer `amount`, `penalty`. | — (roster is the existence fact). |
| `div` 1099-DIV boxes (+ `sb.ordinary_dividends`, `f1040.line3a`, `sd.distributions`, `qbi.dividends`) | No applicability condition. i1040gi p. 26 (lines 3a/3b) only says each payer should send a Form 1099-DIV. Box structure, f1099div p. 5: "Box 2b. Shows the portion of the amount in box 2a that is unrecaptured section 1250 gain"; 2c, 2d likewise "portion of the amount in box 2a"; "Box 2e … portion of the amount in box 1a"; "Box 2f … portion of the amount in box 2a"; box 13 "This amount is included in box 12" (cited in `div.box12`). | Subset relations: C (form-defined). Existence of any dividend: none stated → (B) fact. | Ten box inputs, `div.basis_reconciled`, and the four amounts above are all asked directly; no gate. `div.section1202`, `div.amt`, `div.unsupported`, `div.bad_special` are tests over them. | Subset gating with no new input: 1b (`f1040.line3a`), 2e and 5 (`qbi.dividends`) under 1a>0; 2b, 2c, 2d, 2f under 2a>0; `basis_reconciled` under box 3>0. With a (B) fact (part 3, B-1): also 1a, 2a, 3, 9, 10, 12, 13. Walk: 14 asked, all $0. |
| `ftc` foreign tax credit election | i1116 p. 1, Election To Claim the Foreign Tax Credit Without Filing Form 1116: "This election is available only if you meet all of the following conditions. • All of your foreign source gross income was 'passive category income' … • All the income and any foreign taxes paid on it were reported to you on a qualified payee statement …" (and the $300/$600 limit, the holding-period and election items further down the same list). | C (conditions of an election; moot with no foreign tax). | Formal already: `ftc.has_tax = taxes > 0` and `ftc.needs1116`. Leaks through `all` (§1.4). | `ftc.taxes` = 0: `all_passive`, `statements`, `eligible`, `elect` (4). Fix is a `choose` on `ftc.has_tax`; no new input. |
| `f4952` investment interest | f4952 p. 3, Who Must File: "you must file Form 4952 to claim a deduction for your investment interest expense. Exception. You don't have to file Form 4952 if all of the following apply …" | E (A-kind: investment interest paid, or a carryforward). | `f4952.carryover` (Bool) and `f4952.line1` (amount) asked directly; `f4952.used = any[has_election, carryover, line1>0]`. | No interest and no carryforward: `f4952.line4g` (election amount) under no new input; with an (A) Bool "investment interest paid in 2025 or carried forward from 2024" also `line1`, `carryover` (3 → 1). |
| `f8959` Additional Medicare Tax | i8959 p. 1, Who Must File: "• Your Medicare wages and tips on any single Form W-2 (box 5) are greater than $200,000. • Your RRTA compensation on any single Form W-2 (box 14) is greater than $200,000. • Your total Medicare wages and tips plus your self-employment income … are greater than the threshold amount … • Your total RRTA compensation …" | F, C | `f8959.unsupported` is a screen on 7 lines, asked always. | Not gateable without its own items: the screen's items (Form 4137 tips, 8919 wages, RRTA, church income, territory wages) are themselves part of the threshold sums. Keep direct. |
| `f8960` NIIT | i8960 p. 1: "Attach Form 8960 to your return if your modified adjusted gross income (MAGI) is greater than the applicable threshold amount." | F, C | **Already gated** (`f8960.used` = AGI > threshold, `choose` at `f8960.line16`); screens not asked in the walk. | — (precedent for a C gate). Caveat: MAGI adds back section 911 exclusions; the gate uses AGI with `f8960.unsupported` covering 911 (read, not re-verified). |
| `f8863` education credits | i8863 p. 2, Who Can Claim: "You may be able to claim an education credit if you, your spouse, or a dependent you claim on your tax return was a student enrolled at or attending an eligible educational institution." | E | `f8863.paid` (Bool, "Qualified education expenses paid in 2025 for you, your spouse or a dependent you claim"); gates the rest. | — (exists; its wording is an expense fact, the instruction's is an enrolment fact). |
| `f2441` care credit | i2441 p. 2: "You can take the credit or the exclusion if all five of the following apply. … 2. The care was provided so you (or your spouse if filing jointly) could work or look for work …" | E | `f2441.care`, `f2441.benefits` (Bools). | — (exist). NY line 64 can be gated by `f2441.care` (below). |
| `f5695` energy credits | i5695 p. 1: "You may be able to take the credits if you made energy saving improvements to your home located in the United States in 2025." Purpose: "Also use Form 5695 to take any residential clean energy credit carryforward from 2024". | E | `f5695.part1_any` ("…or a carryforward from 2024"), `f5695.part2_any`. | — (exist). |
| `f8880` saver's credit (`person.sav_*`, `w2.box12_any`) | f8880 p. 2: "You may be able to take this credit if you, or your spouse if filing jointly, made (a) contributions … However, you can't take the credit if either of the following applies. • The amount on Form 1040 … line 11 is more than $39,500 …" (and born after January 1, 2008 / full-time student / claimed as a dependent). | E and C | Formal (`f8880.can_take`, `person.sav_ineligible`) but the contribution inputs come first (§1.4). | AGI over the limit: `sav_roth`, `sav_able`, `sav_voluntary`, `sav_excess`, each `box12_any` (6 in the walk). `sav_trad` stays (it also feeds the IRA deduction and so AGI). No new input. |
| `s1` Schedule 1 | i1040gi p. 3 table: "Have additional income, such as business or farm income or loss, unemployment compensation, or prize or award money. → Schedule 1, Part I"; "Have any adjustments to income, such as student loan interest, self-employment tax, or educator expenses. → Part II". The table calls itself "a general guide". Line-level: p. 88 line 1 "If you received a refund, credit, or offset of state or local income taxes in 2025 …"; p. 99 line 24a "Enter your jury duty pay if you gave the pay to your employer …"; pp. 91–92 lines 8a–8z. | E, but stated as open "such as" lists, so as gates they are (B)-like (defined by lines 1–8z / 11–24z). | `s1.alimony`, `s1.cod_any` Bools; amounts `refund.received`, `s1.uc_paid`, `s1.gambling_winnings`, `s1.line8g/8h/8i/8j/8r`, `s1.jury_to_employer`; complement `s1.line8_other`; roster `$oi8z`. | 24a is a part of 8h: `s1.jury_to_employer` under `s1.line8h > 0` (no new input). A Part I gate (part 3, B-2) would cover 8b–8z items, `cod_any`, `$oi8z`, `line8_other` (9–12 inputs). |
| `s1a` Schedule 1-A | i1040gi p. 109: "Fill out Schedule 1-A, Part IV, only if you paid or accrued QPVLI in 2025"; p. 110 Part V "Fill out Schedule 1-A, Part V, only if: • You (and/or your spouse …) were born before January 2, 1961. • You have a valid social security number"; Part II/III (pp. 101, 106) state tips / overtime received. | E (and C for Part V from age and SSN) | `s1a.tips`, `s1a.overtime`, `s1a.carloan` Bools; Part V from `person.age65`, `person.tin`. | — |
| `s2` Schedule 2 | i1040gi p. 112: "See the Instructions for Form 6251 to see if you must file the form" (i6251 **not archived**). p. 3 table (general guide). | F/C (AMT, unarchived), complement | `s2.amt`, `s2.other` screens. | Not gateable from archived text; keep. Complement list in part 5. |
| `s3` Schedule 3 | i1040gi p. 3 table: "Have other payments, such as an amount paid with a request for an extension to file …"; lines 10, 12 (Form 4136, i4136 **not archived**), 13a–13z. | E | `s3.line10`, `s3.line12`, `s3.line14` amounts. | — (one amount each; a gate would not save a question). |
| `sa` Schedule A | i1040sca p. 1: "In most cases, your federal income tax will be less if you take the larger of your itemized deductions or your standard deduction." No applicability condition. Line 18 (election to itemize when smaller). | none (E per line) | Amounts `sa.line1`, `5a`, `5b`, `5c`, `8a`, `11`; roster `$gift`; screens `sa.unsupported`, `sa.charity_limited`, `sa.excluded_income`; `sa.dependent`, `person.blind`, `sa.elect_itemize`. | `sa.charity_limited` under (line 11 > 0 or `$gift` non-empty), no new input; `sa.elect_itemize` under (0 < itemized total ≤ standard), no new input. With a (B) gift fact: `line11`, `$gift` too. |
| `sd` Schedule D | i1040sd p. 1: "Use Schedule D: • To figure the overall gain or loss from transactions reported on Form 8949; • To report certain transactions you don't have to report on Form 8949; • To report a gain from Form 2439 or 6252 or Part I of Form 4797; • To report a gain or loss from Form 4684, 6781, or 8824; • To report a gain or loss from a partnership, S corporation, estate, or trust; • To report capital gain distributions not reported directly on Form 1040 … line 7a …; and • To report a capital loss carryover from 2024 to 2025." | E (a closed list) | Each bullet is already its own question: `$sales`, `sd.other_forms` (2439/6252/4797/4684/6781/8824/K-1), `sd.distributions`, `sd.carryover`. | — beyond `sd.distributions` under the dividend fact. The list *is* the gate; a single Schedule D gate would replace four questions with five for a filer with any item. |
| `sales` (8949 roster) | i8949 p. 1: "Individuals use Form 8949 to report the following. • The sale or exchange of a capital asset reported on a Form 1099-K, Form 1099-B, or Form 1099-DA. … • Gains from involuntary conversions (other than from casualty or theft) … • Nonbusiness bad debts. • Worthlessness of a security. • The election to defer capital gain invested in a qualified opportunity fund … • To elect out of the installment method." | E | Roster `$sales`; per entry `sales.special`. | — (roster). Its question wording must carry this list (L-3). |
| `qbi`, `f8995`, `f8995a` | i8995 p. 1: "Individuals … use Form 8995 to figure the QBI deduction if: • You have QBI, qualified REIT dividends, or qualified PTP income or loss …; and • Your 2025 taxable income before your QBI deduction is less than or equal to $394,600 … $197,300 …; and • You aren't a patron in a specified agricultural or horticultural cooperative." i8995a p. 1 the converse. | E (QBI/REIT/PTP) and C (taxable income; 8995 vs 8995-A) | `qbi.unsupported` (complement), `qbi.carryforward` (amount), `qbi.dividends` (box 5); `qbi.business_any`. | `qbi.dividends` under the dividend fact / box 1a. An (A) Bool from the first bullet would gate `qbi.unsupported` + `qbi.carryforward` (2 → 1); marginal. |
| `s179` | i4562 p. 2, Who Must File: "• A section 179 expense deduction (which may include a carryover from a previous year)." Line 10 is the 2024 Form 4562 line 13 carryover. | E (prior-year document) | `s179.line10` amount asked always (also needed for target `s179.line13`, the carryover to 2026). | — (one amount). A prior-year-document fact would not save a question. |
| `ssb` | i1040gi p. 31: "You should receive a Form SSA-1099 …" | E | `ssb.benefits` amount; the four `ssb.*` Bools are under benefits > 0 (not asked). | — (precedent: amount as gate). |
| `sli` | i1040gi p. 98: "You can take this deduction only if all of the following apply. • You paid interest in 2025 on a qualified student loan … • Your filing status is any status except married filing separately. • Your modified adjusted gross income … is less than $100,000 …" | E and C | `sli.interest` amount; MAGI is computed. | — |
| `refund` worksheet | i1040gi p. 88, line 1: "If you received a refund, credit, or offset of state or local income taxes in 2025, you may be required to report this amount." TIP: "None of your refund is taxable if, in the year you paid the tax, you either (a) didn't itemize deductions, or (b) elected to deduct state and local general sales taxes". | E (then C from the TIP) | `refund.received` amount; the worksheet's 11 Bools are under received > 0 (not asked). | — (precedent). |
| `person` (per person) | i1040gi p. 93, line 11: "If you were an eligible educator in 2025, you can deduct …"; p. 3 table; i8959 p. 3 line 14 (RRTA, CT-2). | E | `person.educator_expenses` amount gates `person.eligible_educator`; `person.rrta` asked of every person; `person.x_other` (Form 5329 complement); `person.age65`, `blind`, `under16`, `tin`… are filing facts. | — `person.rrta` must not be put behind W-2 existence (L-11: a CT-2 representative has no W-2). |
| `f5329` / `person.x_other` | i5329 p. 1, Who Must File: "You must file Form 5329 if any of the following apply. • You received a distribution from a Roth IRA and … • You received a distribution subject to the tax on early distributions … • … you meet an exception … but box 7 … doesn't indicate an exception … • You received taxable distributions from Coverdell ESAs, QTPs, or ABLE accounts. • The contributions for 2025 to your traditional IRAs, Roth IRAs, Coverdell ESAs, Archer MSAs, HSAs, or ABLE accounts exceed your maximum contribution limit, or you had a tax due from an excess contribution on line 17, 25, 33, 41, or 49 of your 2024 Form 5329. • You didn't receive the minimum required distribution from your qualified retirement plan." | E (closed list) | `person.x_other` ("Form 5329 parts this tool does not prepare") screen; Parts I and VII from the `retirement` roster. | — (it is the list). Bullets 1–3 are partly decidable from 1099-R entries; the others are facts. |
| `household` | i1040gi p. 39 and p. 43: "Form 8862, who must file. You must file Form 8862 to claim the child tax credit or credit for other dependents if your child tax credit … was reduced or disallowed …"; same for the EIC. | C (only if one of those credits is claimed) | `household.credit_disallowed` asked first inside an `all` (§1.4). Filing-status Bools (`married`, `spouse_died_2025`, `community_property`) asked of all. | Credit_disallowed under "claims EIC/CTC/ODC/ACTC" (no new input). `community_property`: relevant to MFS, RDP and head of household rules (Pub. 555 **not archived**; inferred). |
| `s8812` | i1040s8812 p. 1: "Use Schedule 8812 (Form 1040) to figure your child tax credit (CTC), credit for other dependents (ODC), and additional child tax credit (ACTC)." Combat pay: i1040gi (Form W-2 box 12 code Q). | C (needs a qualifying child or other dependent) | `s8812.puerto_rico` (read by line 27 and the earned-income worksheet) and `s8812.combat_pay` (read by EIC, 2441, 8812, IRA) asked with an empty `$dependent`. | `s8812.puerto_rico` under "any qualifying child" (no new input). `s8812.combat_pay` is a W-2 box 12 code Q amount: gateable under some W-2's `box12_any` (no new input), but see the interaction with the 8880 change (§6). |
| `f1040` | i1040gi p. 39, lines 25b ("Include on line 25b any federal income tax withheld on your Form(s) 1099-R …"), 26 ("Enter any estimated federal income tax payments you made for 2025"). | E | Amounts `f1040.line25b`, `25c_other`, `26`, `3a`. | `line3a` under box 1a (above). A (B) "withholding other than on W-2" would replace 25b+25c (saves 1). |
| `scope` | (complements; part 5) | — | four screens asked of all. | — |
| `ny_it201` | Most NY lines are phrased by the instructions themselves as yes/no applicability questions with "If No, go to line …" (ny_it201i pp. 7–23; quoted below). | E, C | 36 `ny_it201.ask.*` Bools asked of the fixture. | See 2.3. |
| `ny_it2` | ny_it201i p. 21: "You must complete a W-2 record for each …" (collection cite). | E | Roster `$ny_it2`, separate from `$w2`. | — (the roster duplicates the federal `$w2` roster rather than deriving from it; owner question). |

### 2.2 Forms already gated by a roster, an amount or a Bool (not in the walk)

Each condition below is already encoded; nothing in these forms is asked of a filer for whom the condition is false.
They need only a check that the roster or Bool question is worded as the instruction's list (L-3, L-4 style).

| Form | Instruction condition (page) | Kind | Encoded by |
|---|---|---|---|
| `sc`, `scveh`, `asset`, `f4562`, `ltc`, `mq`, `se` | i1040sc p. 2: "Use Schedule C (Form 1040) to report income or (loss) from a business you operated or a profession you practiced as a sole proprietor … Also, use Schedule C to report (a) wages and expenses you had as a statutory employee; (b) income and deductions of certain qualified joint ventures …". i4562 p. 2 Who Must File (depreciation, 179, listed property, amortization). i1040sse p. 1: "You must file Schedule SE if: • The amount on line 4c of Schedule SE is $400 or more, or • You had church employee income of $108.28 or more." f7206/i7206 p. 1 (self-employed health insurance). | E (sc), F (SE $400), E (4562) | `$sc@person` roster; per business `$scveh`, `$asset`, `$ltc`; `f4562` implicit; SE by computation. Church employee income is outside (in `scope.schedule1` / `f8959.unsupported`). |
| `w2`, `otjob`, `tipjob`, `carloan` | i1040gi p. 104/108/110 (Schedule 1-A lines 4c, 14a, 22). | E | `$w2@person`; `$otjob`/`$tipjob` under `s1a.overtime`/`tips`; `$carloan` under `s1a.carloan` (`choose` at `s1a.line23`). |
| `retirement`, `f8606`, `f5329` (Parts I, VII), `ira` | i1040gi pp. 26–28 lines 4a–5b: "You should receive a Form 1099-R …"; i8606 p. 2 Who Must File ("File 2025 Form 8606 if any of the following apply. • You made nondeductible contributions to a traditional IRA for 2025. • You received distributions from a traditional IRA in 2025; your basis … is more than zero; …"); i1040gi p. 95 line 20 (IRA deduction). | E | `$retirement@person` roster (one entry per Form 1099-R); `f8606`/`f5329` implicit per person; `person.sav_trad` gates the IRA worksheet. |
| `f8889` | i8889 p. 1: "You must file Form 8889 if any of the following applies. • You, your employer, or someone else made contributions to your HSA. • Your HSA made a distribution. • You failed to be an 'eligible individual' during a 'testing period' and must recognize income. • You acquired an interest in an HSA because of the death of the account beneficiary." | E (closed list) | `$f8889@person` roster. The roster question should carry the four bullets. |
| `f1095a`, `f8962` | i8962 p. 3: "You must file Form 8962 … if any of the following apply to you. • You are taking the PTC. • APTC was paid for you or another individual in your tax family. • APTC was paid for an individual you told the Marketplace would be in your tax family and neither you nor anyone else included that individual …" i8962 p. 2: "you should complete Form 8962 only for health insurance coverage in a qualified health plan purchased through a Marketplace". | E | `$f1095a` roster (one per Form 1095-A). The third bullet (APTC for an individual in no one's tax family) is a case the roster wording must name. |
| `dependent`, `dcprov`, `eic` | i1040gi dependents and EIC sections; i2441 p. 2 line 1. | E | `$dependent` roster; `$dcprov` under `f2441.filing`; EIC by computation with its own screens. |
| `gift` | i8283 p. 1: "You must file one or more Forms 8283 if the amount of your deduction for each noncash contribution is more than $500. You must also file Form 8283 if you have a group of similar items for which a total deduction of over $500 is claimed." | F ($500) / E (any noncash gift) | `$gift` roster — **asked of every filer** (in the walk), since `sa.line12` is reached whenever Schedule A is. The $500 is F: it decides filing Form 8283, not whether the gift is deductible, so it must not gate the amounts. |
| `oi8z` | i1040gi p. 92 line 8z: "Examples of income to report on line 8z include the following." (an open list) | E | `$oi8z` roster (asked of all). |
| `clcw`, `clcw26` | i1040sd p. 10: "Use this worksheet to figure your capital loss carryovers from 2024 to 2025 if your 2024 Schedule D, line 21, is a loss and …" | E | `sd.carryover` ("Did line 21 of your 2024 Schedule D show a loss?") gates the worksheet. |
| `aqee`, `g28`, `u1250`, `qdcg`, `sdtw`, `tcw`, `tax_on_amount`, `f8995`, `f8995a`, `ny_rs`, `ny_city_rs`, `ny_tcw`, `ny_tcw_first` | Worksheets and rate schedules; their use conditions (e.g. i1040gi line 16 tax method; i1040sd pp. 11–12 lines 18–19) are computed. | C | `choose` on computed lines, or definition instances. No applicability inputs. |

### 2.3 New York lines (ny_it201i; all asked of the fixture)

The NY instructions put most applicability conditions as the line's own question. The model's `ny_it201.ask.*` inputs
are those questions. What a formal gate can add is a *federal* fact the NY question itself refers to.

| Input | NY instruction (page) | Formal gate available from existing lines (no new input) | Read/inferred |
|---|---|---|---|
| `ask.out_of_state_bond_interest` (line 20) | p. 7: "Do you have interest income from state and local bonds and obligations from states other than New York State …? • If No, go to line 21. • If Yes, enter any such interest income … that was not included in your federal adjusted gross income. This includes … interest and dividend income from tax-exempt bond mutual funds" | Federal tax-exempt interest (Form 1040 line 2a, `f1040.line2a`) or exempt-interest dividends (`div.box12`) > 0. `f1040.line2a` is not asked today; gating would add it. No net saving unless line 2a is asked anyway. | read; saving inferred |
| `ask.414h` (line 21) | p. 8: "Are you a public employee of New York State or its local governments? … enter the amount of 414(h) retirement contributions, if shown on any federal Form W-2" | `$w2` non-empty | read |
| `ask.529_nonqualified` (line 22), `ask.529_owner` (line 30), `ask.refund_529` | p. 8 line 22: "Did you make a nonqualified withdrawal during 2025 from an account established under New York's 529 college savings program?"; p. 10 line 30: "During 2025, did you, as an account owner, make contributions to or a withdrawal from one or more tuition savings accounts …?" | Line 22 behind line 30's yes, if a nonqualified withdrawal is necessarily an account owner's withdrawal; `refund_529` behind an overpayment (`line78` > 0). | read; the owner/withdrawal relation is **inferred** |
| `ask.inflation_check` (line 25) | p. 8: "If you received an inflation refund check from the Tax Department and included the check amount in the calculation of federal adjusted gross income …" | Possibly Schedule 1 line 1 or 8z > 0; where the check lands federally is not stated in the archived text. | inferred; not recommended without a source |
| `ask.gov_pension` (line 26), `ask.pension_exclusion` (line 29) | p. 9 line 29: "Did you enter an amount of pension income or annuity income, or both (generally reported on line 9 or 10) that was not from a New York State or local government pension plan or federal government pension plan?"; line 26 heading (pensions of NYS, local and federal government). | IT-201 lines 9 or 10 (federal 4b/5b) > 0, i.e. some `$retirement` entry with a taxable amount. Line 29 also needs age 59½ before 2025 ("If Yes, and you were 59½ before January 1, 2025") — a further gate from a birth-date fact. | read |
| `ask.us_obligation_interest` (line 28) | p. 9: "Did you include interest income from U.S. government bonds or other U.S. government obligations on lines 2, 6, or 11? … Dividends you received from a regulated investment company (mutual fund) that invests in obligations of the U.S. government … qualify" | IT-201 lines 2, 3, 6 or 11 ≠ 0. **The question names lines 2, 6, 11; the next paragraph adds fund dividends (line 3).** A gate on the question's own lines alone would reproduce L-21. | read |
| `ask.dependent_care` (line 64) | p. 19: "Would you qualify to claim the federal child and dependent care credit for 2025 (whether or not you actually claimed it)? • If No, you do not qualify for this credit." | `f2441.care` = false ⇒ no. | read; the implication rests on i2441 p. 2 condition 2 |
| `ask.noncustodial` (line 66), `ask.contributions` (line 60), `ask.owes_use_tax` (line 59), `ask.resident_credit` (line 41), `ask.late_penalty`, `ask.yonkers`, `ask.decedent`, `ask.special_accrual`, `ask.item_c`, `ask.state_resident`, `ask.city_resident` | Own questions (pp. 3–19) | none | read |
| `ask.college_tuition` (line 68) | p. 19: "Did you or your spouse or any dependents pay college tuition expenses during 2025? • If No, you do not qualify for this credit." | Candidate: `f8863.paid` = false ⇒ no. NY "college tuition" and federal "qualified education expenses" are defined differently (IT-272 **not archived**). | inferred; not recommended without IT-272 |
| `ask.real_property_credit` (line 67) | p. 19: "Review the instructions for Form IT-214 … to see if you qualify" | A federal-AGI bound on household gross income would need IT-214 (**not archived**). | not formalizable from archive |
| `ask.mctmt` | p. 15 (per L-41): net earnings from self-employment allocated to the MCTD "exceed $50,000", "calculated on an individual basis" | Schedule SE earnings per person ≤ $50,000 ⇒ no; with `$sc` empty, 0. L-41's open point (per-source base) applies. | read (via L-41) |
| `ask.city_credits` | UBT credit, accumulation distribution credit, part-year school tax credit (label) | Partly: UBT needs a business (`$sc`); accumulation credit a trust distribution (no federal input). | inferred |
| `ask.itemize` (line 34) | p. 10–11: compare NY standard and itemized deductions (IT-196) | Not safely: IT-196 has NY-only items. | read; gate not recommended |
| `ask.prior_agi_high`, `ask.prior_year_tax`, `ask.prior_full_year`, `ask.est_late` (line 81) | p. 23: "You may owe an estimated tax penalty if you did not have enough tax withheld …" | Already formal (`gate.estimated_penalty`), leaks through `all`/`any` (§1.4): a `choose` on `tax_due > 0` first. | read |
| `line79` | p. 23: "Enter the amount of overpayment from line 77 that you want applied to … estimated tax for 2026." | `line77` > 0 | read |
| `ask.special_code`, `ask.it225`, `ask.other_credits`, `ask.other_taxes`, `ask.other_withholding` | complements; part 5 | — | — |

---

## 3. Existence facts (B) needed where no instruction states a condition

Each is defined, as the owner's rule requires, as exactly the set of lines it gates: the fact is "yes" when any of
those lines could be non-zero. A fact gates an input only through a `choose` (§1.3 pattern 1); the gated input keeps
its own question for a "yes".

| Id (proposed) | Gates exactly | Definition | Why no (A) condition exists | Questions on a "no" (walk) |
|---|---|---|---|---|
| **B-1 dividends** | `sb.ordinary_dividends` (1a), `f1040.line3a` (1b), `sd.distributions` (2a), `div.box2b`–`2f`, `div.box3`, `div.box9`, `div.box10`, `div.box12`, `div.box13`, `div.basis_reconciled`, `qbi.dividends` (5). Not box 4 (withholding, in `f1040.line25b`) or box 7 (foreign tax, in `ftc.taxes`): those lines have other sources. | "Did you receive any dividends or other distributions from a corporation, mutual fund, ETF or REIT (anything in boxes 1a, 2a, 3, 9, 10 or 12 of a Form 1099-DIV), whether or not you received the form?" | i1040gi p. 26 (lines 3a/3b) states no condition; f1099div defines boxes only. | 14 → 1 (or 6 → 1 after subset gating, which needs no new input). |
| **B-2 Schedule 1 line 8 income** | `s1.gambling_winnings` (8b), `s1.cod_any` (8c), `s1.line8g`, `8h` (and through it `s1.jury_to_employer`), `8i`, `8j`, `8r`, `s1.line8_other` (8a, 8d–8f, 8k–8q, 8s–8v), `$oi8z` (8z). Optionally also lines 1 (`refund.received`) and 7 (`s1.uc_paid`), i.e. all of Part I that is not business, Schedule E or alimony. | "Any income for Schedule 1 line 8 (lines 8a–8z)", stated with the line list of i1040gi pp. 91–92. | The i1040gi p. 3 table is a "general guide" with "such as" examples; line 8z's list is open ("Examples … include"). | 10 → 1 (12 → 1 with lines 1 and 7). Largest saving and largest blast radius (a wrong "no" drops nine lines). |
| **B-3 charitable gifts** | `sa.line11`, `$gift`, and the `sa.charity_limited` refusal gate (8 lines) | "Any gift to a charity in 2025 (cash, check, card or property), or a charitable contribution carryover from an earlier year" | i1040sca gives no condition. The $500 of i8283 is F (filing Form 8283), not existence. | 3 → 1 (charity_limited alone needs no new input). |
| **B-4 withholding other than W-2** | `f1040.line25b`, `f1040.line25c_other` | "Federal income tax withheld on any Form 1099, W-2G, Schedule K-1, 1042-S, 8805 or 8288-A" | i1040gi p. 39 lines 25b/25c give no condition. | 2 → 1. Low value. |
| **B-5 prior-year business carryovers** (optional) | `s179.line10`, `qbi.carryforward` | "Did your 2024 return include Form 4562 with a carryover on line 13, or Form 8995/8995-A with a loss carryforward on line 16?" (document facts, per L-20) | i4562 p. 2 and i8995 line 3 state the carryover, not a condition on the filer. | 2 → 1; addresses L-20's memory problem better than a saving. |
| **B-6 NY 529 account** (optional) | `ask.529_owner`, `ask.529_nonqualified`, `ask.refund_529` | "Are you an owner or beneficiary of a New York 529 college savings account?" | The NY lines ask about contributions/withdrawals, not about having an account. | 3 → 1 (partly overlaps the no-new-input gates in 2.3). |

Applicability conditions that are (A) but not yet inputs, for comparison: **A-1** investment interest (f4952 p. 3,
gates `f4952.line1`, `carryover`, `line4g`); **A-2** Schedule B Part III question 1 (`sb.line7a`, f1040sb, gates
`sb.fbar_required`; the input exists but is unreached).

---

## 4. The review's findings under a design restricted to (A) and (B) gates

The 34 high and medium findings all have the same cause: a narrower life fact was put *above* a screen or input, and
a truthful "no" to the narrower fact implied the screen false. Under the new rules no gate may sit above a screen
unless it is (A) the instruction's own condition or (B) defined by exactly the lines it gates. So a finding is
**designed out** when (i) the screen it concerned stays a direct question, or (ii) the only gate above it is the
instruction's own list, which by construction includes the case. It **needs a specific fact or test** when a gate is
proposed above it and the instruction's condition does not cover the case, or when the defect is in the model's
existing wording.

| Finding | Screen/input concerned | Under the new design | Instruction condition that covers it (page) |
|---|---|---|---|
| L-1 installment sale | `sd.other_forms` (6252), `s2.other` (lines 14, 15) | Designed out: both stay direct; no gate proposed above them. If Schedule D were ever gated, its own list names "a gain from Form 2439 or 6252", which includes payments on earlier sales. | i1040sd p. 1 |
| L-2 Form 2439 from a REIT | `sd.other_forms`, `s3.line14` (13a) | Designed out: the screens name the form, not the issuer. B-1 (dividends) must not gate them. | i1040sd p. 1, p. 6 |
| L-3 worthless securities, bad debts, condemnation | `$sales` | Designed out if the roster question carries i8949's own list. Needs that wording. | i8949 p. 1 |
| L-4 Form 1099-R not a payment | `$retirement` | Designed out: the roster is "one entry per Form 1099-R"; no gate above it. | i1040gi pp. 26–28 |
| L-5 partnership audit (8978) | `scope.credits`, `scope.other_line16` | Designed out: complements stay direct. | i1040gi pp. 34–36, 116 |
| L-6 fractional-gift recapture | `s2.other` (17g), `$oi8z` (8z) | Designed out for `s2.other` (direct). **B-2 gates `$oi8z`**: B-2's definition must include 8z recaptures; it does if stated as "lines 8a–8z". | i1040gi p. 92 |
| L-7 FBAR signature authority | `sb.line7a` | Designed out: A-2 uses line 7a's own words ("financial interest in or signature authority"). | i1040sb pp. 1–2 |
| L-8 foreign-trust grantor | `sb.line8` | Designed out: direct; its label already has "grantor of, or a transferor to, a foreign trust that existed". | i1040sb p. 3 |
| L-9 missed RMD (employer plan) | `person.x_other` | Designed out: direct; i5329's list says "your qualified retirement plan". | i5329 p. 1 |
| L-10 NOL | `scope.schedule1` (8a) | Designed out: `scope.schedule1` stays direct. **If B-2 is extended to "Part I", 8a (NOL) is inside it**, so the definition covers it. | i1040gi p. 91 |
| L-11 railroad CT-2 | `person.rrta` | Designed out only if `person.rrta` is **not** gated by W-2 existence. Its label already names CT-2. | i8959 p. 3 |
| L-12 409A/457A income not paid | `s2.other` (17h, 17i) | Designed out (direct). | i1040gi p. 114 |
| L-13 PFIC sold during 2025 | `scope.other_line16` | **Needs wording**: the existing screen says "stock you own, directly or indirectly, in a CFC or PFIC" (present tense; label read). Not a gate problem. | i1040gi pp. 34, 114 |
| L-14 strike benefits (1h) | `scope.other_income` | Designed out (direct; its label names lines 1b–1d and 1f–1h). | i1040gi p. 24 |
| L-15 FTC passive condition | `ftc.all_passive` | Designed out: the (C) gate is `ftc.taxes > 0`, and the election's own conditions are then each asked. | i1116 p. 1 |
| L-16 section 1244 loss | `sd.other_forms` (4797), `scope.schedule1` (line 4) | Designed out (direct). | i1040sd p. 6 |
| L-17 spouse omitted | all child prompts | Not a gate question. Rule 4: "you or your spouse" is form text; needs a wording convention in labels of per-return gates (B-1…B-6 are per return and must say "you or your spouse"). | — |
| L-18 casualty timing | `sd.other_forms` (4684), `sa.unsupported` | Designed out (direct). i4684 not archived. | — |
| L-19 recoveries | `scope.schedule1` (named clause), `$oi8z` | Designed out for `scope.schedule1`. B-2 must name recoveries in its definition (i1040gi p. 92 first 8z example). | i1040gi p. 92 |
| L-20 QBI carryforward memory | `qbi.carryforward`, `s179.line10` | Not a gate problem today (direct amounts). B-5, if adopted, is a document fact and addresses it. | i8995 line 3; i4562 p. 2 |
| L-21 Treasury money-market funds (NY) | `ask.us_obligation_interest` | Designed out if the gate is "IT-201 lines 2, 3, 6 or 11 ≠ 0" (fund dividends are line 3). **Not** if the gate copies the question's own "lines 2, 6, or 11". | ny_it201i p. 9 |
| L-22 federal agency bonds (NY) | same | Designed out: the input stays the NY question, worded "or other U.S. government obligations". | ny_it201i p. 9 |
| L-23 co-op owners | `sa.line5b`, `sa.line8a` | Designed out (direct amounts; help text). | i1040sca p. 7 |
| L-24 trust beneficiaries | `scope.schedule1`, `qbi.unsupported` | Designed out (direct). | i1040gi p. 100 |
| L-25 forks, mining | `s1.line8_other` (8v) | Designed out if B-2's definition lists 8v as written ("income from forks, staking, or mining"). | i1040gi p. 92 |
| L-26 yard workers | `s2.other` (line 9) | Designed out (direct). | i1040gi p. 113 |
| L-27 1099-K personal items at a loss | none in the model | **Model gap**, not a gate problem: no input reaches the Schedule 1 entry space. Owner decision. | i1040gi p. 88 |
| L-28 13z items | `s3.line14` | Designed out (direct amount). | i1040gi p. 117 |
| L-29 section 965 | `scope.other_line16`, `s2.other` (20), `s3.line14` (13d) | Designed out: "Any additional Form 1040 line 16 tax" is a complement and includes 965INC; if ever enumerated, 965(i) must be added (its label's list omits it). | i1040gi p. 36 |
| L-30 1y refueling recapture | `s2.other` | Designed out (direct). | i1040gi p. 111 |
| L-31 tax credit bonds | `scope.credits` | Designed out (direct). | i1040gi p. 116 |
| L-32 Form 8814 parent | `scope.other_line16` | Designed out (direct; names Form 8814). | i1040gi p. 34 |
| L-33 SEP help text | `person.sav_trad` / IRA inputs | Wording (rule 4), not a gate. | i1040gi pp. 93–95 |
| L-34 Form 5471 officer | `sb.unsupported` ("foreign corporation reporting") | **Needs a decision** if `sb.unsupported` is gated by interest/dividend existence: the 5471 clause has nothing to do with interest. Move it to its own direct screen, or leave `sb.unsupported` ungated. | i1040sb p. 2 |

Summary: 22 are designed out outright (the screen stays direct, or the only gate is the instruction's own list); 5 are
designed out only if a proposed gate's definition includes the case (L-6, L-10, L-19, L-25 → B-2; L-21 → the NY
line-28 gate); 2 constrain where gates may *not* go (L-11, L-34); 3 are wording (L-13, L-17, L-33); 1 is a model gap
(L-27); 1 is helped by B-5 (L-20). Total 34.

---

## 5. Complements and the instructions' own lists

| Screen | Its form lines | The instructions' list (page) | Closed? |
|---|---|---|---|
| `scope.schedule1` | Schedule 1 lines 1–8z, 11–24z | i1040gi pp. 88–100, one heading per line. Line 8z: p. 92 "Examples of income to report on line 8z include the following" (open; the model's `$oi8z` roster takes 8z). Line 24z: p. 100 "Leave line 24z blank." | Closed except 8z (roster). |
| `s1.line8_other` | Schedule 1 lines 8a–8v not computed | i1040gi pp. 91–92, lines 8a–8v, each its own heading. | Closed. |
| `scope.credits` | Schedule 3 lines 1–6z; Form 1040 credit lines | i1040gi pp. 115–116, lines 1–6l; line 6z: p. 116 "Leave line 6z blank." | Closed. |
| `scope.other_income` | Form 1040 lines 1a–1z, passive activity, 8915-F, 8606 line 1, nonresident status | i1040gi p. 24, line 1h: "The following types of income must be included in the total on line 1h. • Strike or lockout benefits … • Excess elective deferrals …" (list continues); lines 1b–1g on pp. 23–24. Nonresident alien status: Pub. 519, **not archived**. "Other return treatment" in the label has no list. | Lines closed; "other return treatment" open. |
| `scope.other_line16` | Form 1040 line 16 boxes | i1040gi pp. 34–36: "Include in the total on the entry space on line 16 all of the following taxes that apply. • Tax on your taxable income … • Tax from Form(s) 8814 … • Tax from Form 4972 … • Tax from Form 8621 … • Tax from Form 8978 … • … 'ECR' … • Triggering event under section 965(i) …" (and 962, Schedule J). | Closed. The screen's label omits 965(i) (L-29). |
| `s2.other` | Schedule 2 lines 1b–1z, 4–21 except those computed | i1040gi pp. 111–114. Line 1y, p. 111: "Enter the following additions to tax. 1. Recapture of the alternative fuel vehicle refueling property credit … 'ARPCR.' 2. … 'EPE8933.' 3. … 'NEPE8933.' 4. … 'EPGEPE.' 5. Any section 6418(g)(2) …" (closed list). Line 17z, p. 114: "Use line 17z to report any taxes not reported elsewhere … Other taxes to be listed include the following. • The prevailing wage and apprenticeship penalties (PWA) from Form 4255 … • Form 8978 adjustment …" | 1y closed; **17z open** ("not reported elsewhere", "include"). |
| `s3.line14` (amount) | Schedule 3 lines 13a–13z | i1040gi p. 117, line 13z: "Use line 13z to report the credit under section 960(c) …" (plus Forms 8689 and 1062 per the review, L-28). | Closed as written. |
| `sa.unsupported` | Schedule A lines 6, 8 limits, 15, 16, sales-tax election | i1040sca p. 11, line 16: "Only the expenses listed next can be deducted on line 16. … • Gambling losses … • Casualty and theft losses of income-producing property …" (list continues). | Line 16 closed. |
| `sb.unsupported` | Schedule B Parts I–II special treatments | i1040sb p. 1 bullets (quoted in 2.1); p. 2 Part II TIP, Form 5471 ("if, in 2025, you were an officer or director of a foreign corporation"; "owned 10% or more"). "Other special treatment" in the label has no list. | Bullets closed; label's "other" open. |
| `sd.other_forms` | Schedule D lines 4, 5, 11, 12 | i1040sd p. 1, "Use Schedule D" bullets (quoted in 2.1). | Closed. |
| `qbi.unsupported` | Form 8995 lines 1–17 | i8995 p. 1, Who Can Take the Deduction (quoted in 2.1). | Closed. |
| `person.x_other` | Form 5329 Parts II–IX | i5329 p. 1, Who Must File (quoted in 2.1). | Closed. |
| `f8959.unsupported`, `f8960.unsupported` | Forms 8959, 8960 lines | i8959 pp. 1–3 (line 14 RRTA, Form 4137, 8919); i8960 line instructions (not enumerated here). | Not checked in full. |
| `ny_it201.ask.special_code` | Item G | ny_it201i p. 5–6: "If you qualify for one or more of the special conditions below, enter the specified two-character code." followed by the codes. | Closed (code list). |
| `ny_it201.ask.it225` | Lines 23, 31 | ny_it201i p. 8 line 23, p. 10 line 31: "Use this line to report other additions [subtractions] that are not specifically listed on Form IT-201. Enter … the amount from Form IT-225". The code list is in the IT-225 instructions, **not archived**. | Open here. |
| `ny_it201.ask.other_credits`, `ask.other_taxes` | Lines 42, 45, 71 | IT-201-ATT (archived `ny_it201att`), Part 1 Sections A–D (p. 1–2) and Part 2 "Other New York State taxes" (p. 2): each credit and tax is a printed line. | Closed (form lines). |
| `ny_it201.ask.city_credits` | NYC credits | Names three credits (label); IT-201-I line references not checked. | Closed as labelled. |

---

## 6. Rough sizing (estimates, arithmetic on the walk of `ny.table.single.0`, 165 questions)

### 6.1 Changes needing no new input (C gates and sequencing; each cites the instruction or form text it rests on)

| Change | Lines changed (approx.) | Forms | Walk saving |
|---|---|---|---|
| `ftc.needs1116`: `choose` on `ftc.has_tax` | 1 | ftc | −4 |
| 1099-DIV subset gating (1b, 2e, 5 under 1a; 2b–2d, 2f under 2a; `basis_reconciled` under box 3) | 8 wrappers (or ~20 reader edits) | div, f1040, qbi | −8 |
| `s1.jury_to_employer` under 8h > 0 | 1–2 | s1 | −1 |
| Form 8862 question under "claims EIC/CTC/ODC/ACTC" | 2 | household | −1 |
| `s8812.puerto_rico` under a qualifying child; `combat_pay` under a W-2 box 12 | 2–3 | s8812, w2 | −1 to −2 |
| Form 8880: AGI and eligibility before contributions | 3–5 | f8880, person, w2 | −6 |
| `sa.charity_limited` behind a gift gate line | 1 new test line + 8 `refuses` edits | sa | −1 |
| `sa.elect_itemize` under 0 < itemized ≤ standard | 1 | sa | −1 |
| `f4952.line4g` under interest paid or carryforward | 1–2 | f4952 | −1 |
| NY: lines 26/29 under federal pensions; 28 under lines 2/3/6/11; 64 under `f2441.care`; MCTMT under SE earnings; 79 and IT-195 under an overpayment; 22 under 30 (inferred) | ~8 gate lines | ny_it201 | −8 to −9 |
| **Subtotal** | **~30–35 lines** | 13 forms | **≈ −32 to −34** |

### 6.2 New Bool inputs

| Gate | New Bools | Lines changed | Walk saving (net of the new question) |
|---|---|---|---|
| B-1 dividends (after subset gating) | 1 | ~6 wrappers | −5 (1a, 2a, 3, 9, 10, 13 → 1; box 12 is not asked today) |
| B-2 Schedule 1 line 8 income | 1 | ~9 wrappers | −8 (−10 with lines 1 and 7) |
| B-3 charitable gifts | 1 | 2–3 | −1 |
| A-1 investment interest | 1 | 2–3 | −1 |
| A-2 `sb.line7a` gating FBAR | 0 (exists) | 1–3 | 0 |
| `sb.unsupported` under interest or dividends > 0 (needs L-34 decision) | 0 | 1 + 3 `refuses` edits | −1 |
| B-4 withholding; B-5 carryovers; B-6 NY 529 | 0–3 (optional) | 2–4 each | −1 each |
| **Subtotal** | **4 (core) to 7** | **~25–35** | **≈ −16 to −21** |

**Total estimate**: about 165 → 110–117 for this return; roughly 55–70 expression lines changed and 4–7 new Bool
inputs, across about 15 form documents (ftc, div, f1040, qbi, sd, sb, s1, household, s8812, w2, f8880, person, sa,
f4952, ny_it201). For comparison, the T-251 ladder estimated 110–114 for the same return.

Caveats:
- Inputs are read by several lines (e.g. `f1040.line3a` by 8, `sa.charity_limited` by 8 as a refusal gate). Gating at
  each reader multiplies edits; wrapping each gated input once (input renamed, old id becomes the `choose`) keeps the
  edits to one line per input but renames input keys, which touches the question bank, fixtures and answer logs.
  Owner question 1.
- The 8880 change makes `w2.box12_any` unreachable for high-AGI filers; gating `s8812.combat_pay` on `box12_any` would
  then add it back. Gate combat pay on its other readers' applicability instead, or accept no saving there.
- Savings for filers with entries are smaller (their gates are "yes"); the change never adds more than the new Bools.

### 6.3 Reviews that would rerun

Per CLAUDE.md (review what changed; one review per form per round after its fixes land) and `tools/transcription/subjects.py`:

- **Transcription and render** (`transcribe.py`, `render_compare.py`): every form whose definition / rendered English
  changes: the ~15 above. DeepSeek transcription only where `compare_families.py` makes it eligible; DeepSeek render
  as before.
- **Class M** (`classm.py`): every document whose expressions change (the same ~15; `ny_it201` once). DeepSeek class M
  as before.
- **Completeness** (`completeness_review.py`): the same forms, since their content changes.
- **Screen review** (`screen_review.py`): its subject today is "a yes/no input that one or more lines name as a refusal
  gate" (docstring). **Choose-guard gates (all of B-1…B-6, A-1, A-2) are not screens under that definition and would
  not be reviewed.** Rule 7 of the design draft requires them to be; the tool needs extending (a gate is a Bool input
  a `choose` guard tests to select a zero alternative), then a review of each new gate. Existing screens whose gated
  lines change become stale by prompt hash and rerun: `sa.charity_limited`, `sb.unsupported`, `sb.fbar_required`,
  `household.credit_disallowed`, the NY `ask.*` screens whose gate lines change (~8).
- Mechanical checks (check-all): Lean comparison, mutation, interview-check, `check_refusal_reach.mjs`; the `all`/`any`
  rewrites are evaluator-visible only through `choose` and so need no evaluator change.

---

## Open questions for the owner

1. **How to gate an input with several readers.** (a) Rename the input and make its old id a `choose` on the gate
   (one line per input; changes input keys, the question bank, fixtures and any answer logs), or (b) put the `choose`
   at every reader (keys unchanged; several edits per input, and a missed reader silently re-exposes the input).
2. **A third kind of gate.** Many savings come from conditions the instructions state on *computed* amounts (Form 8880's
   AGI limit, the election conditions behind `ftc.taxes > 0`, 1099-DIV boxes that are "the portion of the amount in
   box 2a", Form 8960's MAGI threshold, already used). They need no new input. Are these (A) conditions, or a separate
   kind the standing rules should name?
3. **`all`/`any` do not sequence.** Rewrite the affected tests as nested `choose` where a Bool should wait (154 mixed
   tests exist; only those on the asked path matter), or change the evaluator so `all`/`any` stop at the first unknown
   operand? The second changes the reachable set model-wide and must be matched in the Lean evaluator.
4. **B-2 (Schedule 1 line 8 income).** The largest saving and the largest blast radius: a wrong "no" drops nine lines.
   The 1040 instructions' own table ("Have additional income, such as …") calls itself a general guide. Accept B-2,
   extend it to all of Part I (lines 1 and 7 too), or leave the line 8 inputs direct?
5. **Filing thresholds are not gates.** Confirm that F conditions (Schedule B's $1,500, Form 8283's $500, Schedule SE's
   $400) gate only the printing of a form or part, never the amount inputs below them.
6. **`sb.unsupported`'s Form 5471 clause (L-34).** Split it into its own direct screen so the rest can be gated by
   interest/dividend existence, or leave `sb.unsupported` ungated?
7. **Screen review for `choose` gates.** Extend `screen_review.py` (and `check_screens.py` currency) to Bool inputs used
   as `choose` guards, before any new gate lands?
8. **NY conditions that rest on unarchived sources** (IT-214 real property credit, IT-272 college tuition, IT-225 codes,
   the inflation-check line): archive them first, or keep those questions direct?
9. **`f1040.line2a` (tax-exempt interest)** is not asked unless a reader needs it; NY line 20 could be gated by it plus
   exempt-interest dividends only if line 2a is asked of everyone. Ask it (it is a printed Form 1040 line), or keep NY
   line 20 direct?
10. **`$ny_it2` duplicates `$w2`.** Derive the NY W-2 records from the federal roster (one per W-2 entry), or keep the
    separate roster?
11. **Spouse wording (L-17).** Per-return gates (B-1…B-6, A-1) need "you or your spouse" in the form label; adopt that as
    the convention for every per-return Bool?

## Appendix A. The 165 questions of the walk, grouped

Asked of the `ny.table.single.0` return (single, two W-2s, one interest payer with $0), in order. `*` marks an input a
change in part 6 would make unreachable on this return.

- Return and people (9): `$person`, `f1040.status`, `person.role`, `household.married`, `household.spouse_died_2025`,
  `person.under16`, `household.community_property`, `person.age65`, `person.blind`.
- Complements (4): `scope.credits`, `scope.other_income`, `scope.other_line16`, `scope.schedule1`.
- Rosters (10): `$f1095a`, `$retirement`, `$dependent`, `$w2`, `$interest`, `$f8889`, `$oi8z`*(B-2), `$gift`*(B-3),
  `$sales`, `$sc`.
- W-2 entries (16): boxes 1–7 ×2, `box12_any` ×2* (8880).
- Interest (2): `interest.amount`, `interest.penalty`.
- Dividends (14)*: `sb.ordinary_dividends`, `f1040.line3a`, `sd.distributions`, `div.box2b`, `2c`, `2d`, `2e`, `2f`,
  `3`, `9`, `10`, `13`, `div.basis_reconciled`, `qbi.dividends`.
- Schedule B (4): `sb.unsupported`*, `sb.fbar_required`, `sb.form8938`, `sb.line8`.
- Schedule D (2): `sd.carryover`, `sd.other_forms`.
- Payments (5): `f1040.line25b`, `f1040.line25c_other`, `f1040.line26`, `s3.line10`, `s3.line14`.
- Schedule 1 (12): `refund.received`, `s1.alimony`, `s1.jury_to_employer`*, `s1.line8_other`*, `s1.cod_any`*,
  `s1.gambling_winnings`*, `s1.line8g`*, `8h`*, `8i`*, `8j`*, `8r`*, `s1.uc_paid`; plus `person.educator_expenses`,
  `sli.interest`, `ssb.benefits`.
- Schedule 1-A (3): `s1a.carloan`, `s1a.tips`, `s1a.overtime`.
- Schedule 2/3 screens (4): `s2.amt`, `s2.other`, `person.x_other`, `s3.line12`.
- Schedule A (11): `sa.dependent`, `sa.elect_itemize`*, `sa.excluded_income`, `sa.unsupported`, `sa.charity_limited`*,
  `sa.line1`, `sa.line11`*(B-3), `sa.line5a`, `sa.line5b`, `sa.line5c`, `sa.line8a`.
- Credits and other (21): `f4952.carryover`*, `f4952.line1`*, `f4952.line4g`* (A-1), `f8863.paid`, `f8959.unsupported`,
  `ftc.all_passive`*, `ftc.elect`*, `ftc.eligible`*, `ftc.statements`*, `ftc.taxes`, `person.rrta`, `s179.line10`,
  `qbi.unsupported`, `qbi.carryforward`, `f2441.benefits`, `f2441.care`, `household.credit_disallowed`*,
  `s8812.combat_pay`, `s8812.puerto_rico`*, `f5695.part1_any`, `f5695.part2_any`.
- Saver's credit (5): `person.sav_trad`, `sav_excess`*, `sav_roth`*, `sav_able`*, `sav_voluntary`*.
- New York (40): 34 `ny_it201.ask.*` (`gov_pension`*, `pension_exclusion`*, `us_obligation_interest`*,
  `dependent_care`*, `mctmt`*, `529_nonqualified`*, `refund_529`* and `prior_year_tax` among them), `$ny_it2` and its
  three fields, `ny_it201.line75`, `ny_it201.line79`*.

Total 165 (per-form counts from the walk log, `/tmp/appsurvey/walk_base.txt`).
