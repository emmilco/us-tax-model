# Lane plan-interview: fix proposals for the interview problems of the 2026-11-15 walks

claude-opus-5-5, judgment, year 2025, jurisdiction us. Read only; no build, walk, check or model call was run.
Tree read: `.claude/worktrees/xint` (working tree, about 23:30), its built `canonical/2025/interview-full.json`,
the walk transcripts in `/private/tmp/wout-after/` and `/private/tmp/wout-before/`, and `main` / `66a808c8` by
`git show` / `git grep`. Labels: **[C path:line]** checked against that file; **[I]** inferred, not checked.
Word counts in the proposals are counted by hand the way the walk counts (frame included); a fix lane should
confirm them with `draft-walk`.

## Summary

1. **`f1040.tax_exempt_interest` for every filer.** Cause: Form 6251 bound `s2.amt_could` and the private-activity
   bond gate read `f1040.tax_exempt_interest` directly, and `s2.amt` (read by every return) reads them; before
   g1-f7b nothing read it for a filer like 01 (only EIC, SSB, 8962 and NY did). The AMT screen does need a
   tax-exempt-interest fact from everyone, because the amount is unbounded, but it does not need a dollar amount:
   a yes/no box is enough (protocol 3.2, "an amount asked of everyone becomes a yes or no parent with the amount
   beneath it"). **Proposal:** new input `f1040.tax_exempt_any` and gate `f1040.tax_exempt_interest_if_any`. The
   box goes on a new two-box screen with `div.any` at order 272. That gives 01 one screen where it now has two, so
   it is back to 57 steps (zero extra), 07 also saves a step, and the AMT arithmetic stays the same. Exact diff in
   section 1.
2. **N10 rewrites.** I give verbatim wording within the limits for every listed child over 40 in the seven areas
   (`rprop.screen`, `rprop.kind`, `rental.days_personal`, `rprop.basis`, `rental.not_at_risk`,
   `rental.days_fair`, `person.f4137_under20`, `person.mw_not_box1`, `person.mw_box1`), for the four outside ones
   that can be fixed by wording alone (`s2.amt_business`, `k1s.not_at_risk`, `k1s.past_years`,
   `k1p.not_at_risk`, `k1p.basis_short`), and for the twelve tick-member prompts in the seven areas plus `sd.qof`,
   in case the owner applies the 25-word limit to them (item 5). `rprop.screen` cannot be fixed by wording: it is a
   seven-item refusing catch-all. The proposal is technique 3.1: one six-box per-building screen, with the
   qualified-improvement item moved beneath `rprop.kind = nonresidential`. Same step count.
   **Side finding:** `rental.not_at_risk` asks only about nonrecourse loans. It omits two at-risk cases the source
   lists: guarantees or stop-loss agreements, and loans from a person with an interest in the activity. That is a
   possible false No (section 2.2).
3. **Personas 21 and 22.** Proposed answers: all `false`, each consistent with the story. 21 also needs one
   sentence added to `who:` so that `refund.exc_tax: false` follows from the story. **Side finding:**
   `refund.you_born` ("born before January 2, 1960?") is asked after the birth year 1967 was given. That is an N8
   violation from before tonight's work.
4. **Persona 18.** Yes, this is an N11 conflict: the Yes at `sales[nft].special` (Q101) is shown only at Q110,
   after the sale's proceeds, basis and code and the whole `sales_rare` screen. The likely cause [I] is that
   `sd.count` is the line that reads `sales.one` (where the special refusal sits), and it refuses first on
   `sd.other_forms`, which reads `sd.qof` and the other `sales_rare` boxes [C forms/2025/sd.yaml:373-386,
   :226-268]. **Fix:** ask the `sales_rare` screen (and the `sd.sold_other` follow-ups) before `$sales`, by
   reordering `seq` within order 274. This edits only the bank: no gate ids or expected values change, and a QOF
   owner also hears their refusal earlier.
5. **25 words: label or full prompt?** Recommendation: apply N10's parent limit to the **full prompt** of a tick
   member and keep the 12-word cap on the label. The full prompt is shown as *the question itself* in four
   real paths: the CLI, the last open member of a group, "Answer this one on its own", and a reopened answer
   (interview/README.md:129-141, 557-560). N10 is a rule about questions, not screens.

---

## 1. `f1040.tax_exempt_interest` as an unconditional screen

### 1.1 Why it became one

- On `66a808c8` (BEFORE) the readers of `f1040.tax_exempt_interest` were only `f1040.line2a`, and the readers of
  line 2a were EIC, SSB, Form 8962 and NY IT-201 [C `git grep 66a808c8` output: eic.yaml:620, f8962.yaml:648,
  ssb.yaml:243, ny_it201.yaml:635]. None of these is read for persona 01, so 01 was never asked it. (The walk
  file's wording "opened only behind the `s2.amt_owed` tick box" is loose: `s2.amt_owed` was a refusing box,
  questions.yaml@66a808c8:494-500. Removing it cut a box, not a screen, and the new reader added the screen.)
- g1-f7b added three readers in `s2` that every return reaches [C forms/2025/s2.yaml:209, :239, :736]:
  - `s2.amt_pab_ask` (TE > 0 and `s2.amt_could`);
  - `s2.amt_pab_over`;
  - `s2.amt_h_extra` = TE + mortgage interest. It feeds `s2.amt_h4` → … → `s2.amt_could` [C s2.yaml:733-872].
  `s2.amt` reads `s2.amt_tmt_over` [C s2.yaml:958-979], and `s2.amt` gates Schedule 2 lines 2 and 3, which every
  return reads. So 01 now must answer the amount.
- The lane note's "the filer with no Schedule C is asked nothing about the alternative minimum tax" is true of the
  three questions it added (`s2.amt_pab`, `s2.amt_boat`, `s2.amt_business`). It overlooked that the bound reads
  an existing input that had not been asked of everyone [C docs/provisional/lanes/g1-f7b.md:76-78]. The persona
  walks were not re-run there [C same, line 77].

### 1.2 Is it needed?

A **fact** about tax-exempt interest is needed from everyone; a **dollar amount** is not. TE interest is
unbounded, so no arithmetic on the return can clear `s2.amt_could` without knowing whether there is any: the
bound counts all of it as private-activity-bond interest [C s2.yaml:733-737, :872-878; design note
docs/2026-11-15_amt_computed_screen.md:98-106]. If the No path enters 0 exactly as the amount question's "Zero if
none" does today, a Yes/No parent does not change the arithmetic. A wrong result then needs a wrong No to the
box, and the same filer could equally have typed 0 today.

Alternatives considered and rejected:
- **Gate the amount on `$interest` being non-empty.** 01's list is empty [C wout-after/01_single_w2.md:560-570],
  so 01 would save the step. But a filer whose only interest is tax-exempt may leave the list empty, because
  `interest.amount` says "Leave out tax-exempt interest (box 8)". That opens a new false-zero path into the AMT,
  EIC and SSB. It would also not save 02's step, if 02 lists a bank.
- **Box on `invest_other` (order 276).** This also gives zero steps, but the amount would be asked at 276, after
  the sales, splitting line 2a from lines 2b and 3a (N7). It is an acceptable fallback if the owner does not want
  `div.any` on a tick screen.

### 1.3 Proposal (exact change)

Share check: tax-exempt interest is on 6,893,860 of 160,602,107 returns, about 4.3%, and dividends are on 21%
[C interview/2025/gate_frequencies.yaml:20, :184-207]. So both boxes are typically No (3.6), and both are plain
parents.

**forms/2025/f1040.yaml**: after `f1040.tax_exempt_interest` (line 220), add the parent and the gate, and gate the
input. Follow the pattern of `f1040.estimated_any` / `f1040.line26_if_estimated` [C f1040.yaml:986-1003,
1144-1162]:

```yaml
    - id: f1040.tax_exempt_any
      printed: (gate)
      label: Was tax-exempt interest received in 2025?
      type: Bool
      expr:
        op: input
        source: In 2025, did you (or, on a joint return, your spouse) get tax-exempt interest, for example from a city or state bond?
      cite:
        doc: i1040gi
        locator: Instructions for Form 1040, p. 25, line 2a, "Enter the total on line 2a"   # same locator as the amount
    - id: f1040.tax_exempt_interest
      ...                                  # unchanged, plus:
      gated_by: f1040.tax_exempt_interest_if_any
    - id: f1040.tax_exempt_interest_if_any
      printed: (helper)
      label: Tax-exempt interest when any was received; zero otherwise
      type: NonNegDollars
      expr:
        op: choose
        alternatives:
          - guard: { op: test, eq: [f1040.tax_exempt_any, { const: true }] }
            then: f1040.tax_exempt_interest
          - guard: { op: test, eq: [f1040.tax_exempt_any, { const: false }] }
            then: div.zero
      cite: (as the amount)
```

**Readers** change from `f1040.tax_exempt_interest` to `f1040.tax_exempt_interest_if_any`, because a gated input
is read only by its gate [C engine/src/gates.ts:67-68]:
- `f1040.line2a` [C f1040.yaml:238];
- `s2.amt_pab_ask` [C s2.yaml:209];
- `s2.amt_pab_over` [C s2.yaml:239];
- `s2.amt_h_extra` [C s2.yaml:736].

No other form reads it [C grep forms/2025, forms/ny].

**interview/2025/questions.yaml**:
- new group: `- id: interest_dividends` / `heading: "In 2025, did you (or, on a joint return, your spouse) get either of these?"`
- `f1040.tax_exempt_any`: `order: 272`, `seq: 1`, `group: interest_dividends`,
  `tick: "Tax-exempt interest, such as from a city or state bond"` (9 words). Help: "Box 8 of Form 1099-INT, or
  tax-exempt amounts on Form 1099-OID. Exempt-interest dividends from a fund (Form 1099-DIV box 12) are asked
  with dividends."
- `div.any`: add `group: interest_dividends`, `seq: 2` (now `seq: 1`; renumber the order-272 block so that no other
  question's `seq` lies between the members: `f1040.tax_exempt_interest` seq 3, `sb.ordinary_dividends` 4,
  `f1040.line3a` 5, and so on, keeping the present relative order [C canonical order-272 listing]), and
  `tick: "Shares or a fund outside a retirement account, or a Form 1099-DIV"` (12 words). The prompt and help stay
  as they are (the help's "If you are not sure, answer Yes" survives behind "What this asks").
- `f1040.tax_exempt_interest`: `order: 271` → `272`, `seq: 3`. Prompt: "How much tax-exempt interest did you (or, on
  a joint return, your spouse) get in 2025? Zero if none." Help unchanged.
- The members are of two once-per-return forms (`f1040`, `div`), and neither is a list's form, so the build
  rule allows them in one group [C interview/README.md:591-600].

**Fixtures and coverage** (input restatement only; no expected value):
- `defaults.json`: add `f1040.tax_exempt_any: false` with the "Closed" reason. Keep
  `f1040.tax_exempt_interest: 0` only if the runner tolerates an input behind a false gate; the lane must check
  that first.
- Every case with a non-zero amount gains `f1040.tax_exempt_any: true`. By a grep of the values, there are about 11
  such cases: ssb 1, f1040 1, f8962 1, s2 6, classm 1, NY it201 1. Coverage rows ny.yaml:199 and other.yaml:95 too.
  The roughly 800 zero cases need `false`, or nothing if the default applies [I: counts by grep, not by case].
- Personas 03, 04, 07 and 08 state `f1040.tax_exempt_interest: 0` [C personas:33-46]. Change it to
  `f1040.tax_exempt_any: false`.

**Expected walk effect [I]:** 01 goes from 58 to 57 steps (TE screen and `div.any` screen become one screen). 07
also loses one step. A filer with TE interest gets one more short screen (the amount). The AMT, EIC, SSB and 8962
values are unchanged for the same facts.

**Risk.** Who could wrongly pass over the box: a muni-bond holder whose brokerage's combined 1099 lists
"Tax-exempt interest" under its 1099-INT part. The label uses that exact term. A muni-fund holder may tick it
wrongly; the amount help sends box 12 elsewhere, so such a wrong Yes costs a step, not a wrong value.

**Reviews:** class M and transcription on f1040 (new lines), line-scoped; s2 render line-scoped on the 3 lines
whose reads changed; false-no sample on `f1040.tax_exempt_any`.

---

## 2. N10: proposed wording

Limits: under 25 words in a parent and under 40 in a child; help about 40 at most. A rule moved out of a prompt goes
into a child question, not into help [C protocol:92-95]. Frames counted: "For this rental property — " 4,
"For this building or improvement — " 5, "For this person (you, or your spouse on a joint return) — " 10,
"For this S corporation — " 4, "On this Schedule K-1 (Form 1065) — " 6.

### 2.1 Schedule E

**`rprop.screen` (144) — needs a model change, not a rewording.** It is a seven-item catch-all that refuses
[C forms/2025/rprop.yaml:71-95; refusal :172-178]. Under N10 the items cannot go into help, and the prompt cannot
hold them. Proposal under technique 3.1:
- `rprop.screen` stays as a derived Bool, the `any` of the items below. The refusal entry `when: rprop.screen`
  and its wording stay as they are, so no expected refusal changes.
- New per-entry tick group `rprop_facts`, heading "Is any of these true of it?" (6 words + frame). Six boxes, all
  Bool inputs of `rprop`:

| new input | tick (words) | source item (prompt bullet) |
|---|---|---|
| `rprop.ads` | Depreciated by the longer alternative system (ADS), required or chosen (10) | bullet 1 |
| `rprop.fast` | Some of its cost deducted in one year, or another method used (12) | bullet 5 (special allowance, section 179, other method) |
| `rprop.credit` | A credit or deduction taken for part of its cost (10) | bullet 7 |
| `rprop.basis_changed` | Its basis changed after you began depreciating it (for example, a casualty) (12) | bullet 2 |
| `rprop.disposed` | Sold, given away or no longer rented in 2025 (8) | bullet 3 |
| `rprop.coop` | Stock in a cooperative housing corporation (6) | bullet 4 |

- Bullet 6 (qualified improvement property) becomes a child asked only when `rprop.kind = nonresidential` (§2
  item 5: gate on what is already said). Gate `rprop.qip_if_nonres`. Prompt: "For this building or improvement —
  Is it an improvement to the inside of the building, placed in service in 2018 or later, after the building
  itself (not an enlargement, elevator, escalator or structural framework)?" (34 words). It covers the same
  exceptions as today's bullet. Source: the qualified-improvement definition at i4562.cols.txt:195 and :45 [C].
  The exceptions (enlargement, elevator/escalator, internal structural framework) are those of section
  168(e)(6). They are kept as worded today; I did not re-read them in an archived source [I].
- Step cost: one screen per building, the same as today. A residential building, the typical case, never sees
  the qualified-improvement question.
- Coverage rows: one per item (protocol 3.7). The fixtures that state `rprop.screen` need the six inputs instead,
  because the evaluator refuses input on a derived line [C g1-f7b.md:16-17].

**`rprop.kind` (60).** Use a bank `prompt:` override; the choices are already in `value_labels`
[C questions.yaml:7112-7119]:
- prompt: "For this building or improvement — What is it?" (8)
- `residential`: "A building whose rent comes mostly (80% or more) from homes, or an improvement to one" (the 80%
  rule moves from the prompt to the choice it defines)
- `nonresidential` and `personal`: unchanged.

Source: "Residential rental property is a building in which 80% or more of the total rent is from dwelling units"
[C sources/2025/i4562.cols.txt:195]. Who could answer wrongly: the owner of a mixed shop-and-flat building; the
80% is on the option they read.

**`rental.days_personal` (66).** Its parent `rental.personal_any` comes immediately before it (seq 14 then 15)
[C canonical listing] and already names the users, so the child need not repeat them (N8):
"For this rental property — How many days was it used that way? Leave out days spent mostly on repairs, and
days it was your main home before or after renting it (or trying to) for 12 months in a row." (40)

Checked against p527 [C p527.cols.txt:870-875]: who counts as a personal user; "Any day that you spend working
substantially full time repairing and maintaining"; "rented or tried to rent the property for 12 or more
consecutive months". "12 months in a row" is met by any longer run. The year comes from the parent's "in 2025".
Help unchanged (14). The sale-ending period of under 12 months (p527's second bullet) is not covered, as
today [I: a sold rental is refused elsewhere].

**`rprop.basis` (45).** "For this building or improvement — Your share of what it cost, not counting the land.
If you used it yourself before renting it, use the smaller of its value then and your adjusted basis." (35)

Source: "If you used the property for personal purposes before changing it to rental use, its basis for depreciation
is the lesser of its adjusted basis or its FMV when you change it to rental use" [C p527.cols.txt:291]. This is
broader and more exact than today's "a home you lived in". Help unchanged.

**`rental.not_at_risk` (45).** "For this rental property — Did you pay for it, or for work on it, with a loan you are
not personally liable for, from someone other than a bank, a government or another regular lender (for example,
the seller)?" (38)

Source: qualified nonrecourse financing (government, or a qualified person who "actively and regularly engages in
the business of lending money", not the seller) [C i1040se.cols.txt:49].

**Correctness gap, not N10 [C i1040se.cols.txt:48]:** the source also counts as not at risk amounts "protected
against loss by a guarantee, stop-loss agreement" and amounts "borrowed ... from a person who has an interest in
the activity". Neither today's prompt nor this rewrite asks about them. Proposal for the owner: a child or a
second box, "Is any money you put into it protected by a guarantee or stop-loss agreement, or borrowed from
another owner or someone related to one?" (with frame, 26). It should also go into the false-no review sample.

**`rental.days_fair` (43).** "For this rental property — How many days in 2025 was it rented at a fair price,
including any of those days you also used it? Leave out days it was empty but offered for rent." (35)

Source: "Any day that the unit is rented at a fair rental price is a day of rental use even if you used the unit for
personal purposes that day" and "available for rent but not actually rented isn't a day of rental use"
[C p527.cols.txt:845-847]. Help unchanged.

**`rental.personal_any` (help 50).** Shorter help (37 words): "Family: a spouse, parent, grandparent, child,
grandchild, brother or sister. Not personal use: family paying a fair rent to live there as their main home, or
days it was your main home before or after renting it out." The repair-days rule goes, because the child
(`rental.days_personal`) now carries it, and a repair day only changes the count, not this Yes/No [I].

### 2.2 Pay not on a W-2

**`person.f4137_under20` (47).** "For this person (you, or your spouse on a joint return) — Of the cash and card tips
you did not report, how much was from a month in which your tips at that job were under $20? Zero if none." (38)

Source: f4137 Line 5, "Enter only the tips you weren't required to report to your employer because the total
received was less than $20 in a calendar month", and "the $20 rule applies separately to the tips you received
while working for each employer" [C as quoted in the canonical cite; the archived f4137.cols.txt did not match my
grep, so this is not re-read in the PDF].

Help (41 to 29): "Tips under $20 in a month at one job did not have to be reported to the employer. They are still
income but carry no social security or Medicare tax."

**`person.mw_not_box1` (46).** "For this person (you, or your spouse on a joint return) — How much of that Medicaid
pay is not in box 1 of a W-2? Zero if none." (26)

Help (new; today it has none): "It may show only in box 12 with code II, on a Form 1099-MISC or 1099-NEC, or on no
form." This is where on a paper the thing is found, which help is for (N10).

Source: "payments that were not reported on Form(s) W-2, or not reported in box 1 of Form(s) W-2"
[C i1040gi.cols.txt:475]; code II per the cited p. 92 quote.

**`person.mw_box1` (42).** "For this person (you, or your spouse on a joint return) — How much 2025 Medicaid pay
for caring for someone who lived in your home with you is in box 1 of your W-2s? Zero if none." (36)

Same source, p. 92 ("If nontaxable payments were reported to you in box 1"). Help unchanged.

### 2.3 Outside the seven areas (children)

**`s2.amt_business` (42).** "Do you (or, on a joint return, your spouse) deduct in a business costs of gaining or
keeping readers for a newspaper, magazine or newsletter, exploring for or developing a mine, or drilling an oil,
gas or geothermal well?" (39)

Source: circulation costs "to establish, maintain, or increase the circulation of a newspaper, magazine, or other
periodical"; mining exploration and development; IDCs [C cite of s2.yaml:933-935]. The design note's guard word
"newsletter" is kept [C amt design note:116].

**`k1s.not_at_risk` (53).** "For this S corporation — Did you pay for your shares, or lend to it, with money
borrowed on terms that protect you from loss, or borrowed from another owner or someone related to one?" (34)

Help: "Such as a loan you are not personally liable for, or one someone guarantees for you. A bank loan you must
repay yourself does not count. A Yes ends the interview here." (31)

Source: i1040se.cols.txt:48 (the same three classes) [C].

**`k1s.past_years` (49; help 68).** "For this S corporation — Did you (or, on a joint return, your spouse) materially
participate in this business in at least 5 of the years 2015 to 2024 (any 3 earlier years if it provides personal
services)?" (37)

Help (about 40): "Personal services: health, law, engineering, architecture, accounting, actuarial science, performing
arts, consulting, or other work where capital is not a major source of income. A year counts if its income was in
column (i) or (k) of your Schedule E."

Source: i1120ssk p. 4, both tests, as cited [C cite text].

**`k1p.not_at_risk` (48).** "On this Schedule K-1 (Form 1065) — Was any of what you put in borrowed without
personal liability (other than qualified real estate loans), protected by a guarantee or stop-loss agreement, or
lent by another partner or someone related to one?" (40)

Source: i1040se.cols.txt:48-49 [C].

**`k1p.basis_short` (44).** "On this Schedule K-1 (Form 1065) — Were your 2025 losses from it more than your basis
at the end of its year (what you put in, plus your share of its income and debts, less losses and money taken
out)?" (40). The wording is unchanged; only the sentence break moves.

### 2.4 Tick-member full prompts (only if item 5's recommendation is adopted)

| id | now | proposed full prompt (words incl. frame) | note |
|---|---|---|---|
| `rental.part_home` | 30 | For this rental property — Is it part of a building you live in, such as a room or a unit? (20) | i1040se p. 6 "Renting out part of your home" |
| `sche.qbi_business` | 28 | Do you treat a rental as a business for the qualified business income deduction? (14) | example (250 hours, separate books) to help |
| `royalty.business` | 26 | For this royalty — Did it come from your work as a self-employed writer, artist, musician or inventor, or an oil or gas working interest? (24) | |
| `f1116sb.changed` | 36 | Since you filed your 2024 return, has anything changed the foreign tax carried from it? (15) | the examples are already in its help |
| `f1116sb.split` | 29 | Is any foreign tax carried into 2025 from an earlier joint return with someone you are not filing jointly with now? (21) | p514 p. 39 |
| `f1116.reduction` | 27 | Does any of the foreign tax relate to income you exclude, foreign oil, gas or minerals, an international boycott, or another reduction? (22) | help already lists the others |
| `rec.has_other` | 41 | Was any of it a refund or reimbursement of something else you itemized on your 2024 Schedule A, such as a casualty loss? (23) | the excluded kinds are the sibling boxes of `rec_kinds` and asked before it |
| `s1.nol_not_married` | 26 | Were you and your spouse not married to each other in a year the loss arose, or in any year since? (21) | i172 p. 3 |
| `scope.tips_unreported` | 42 | In 2025, did you (or, on a joint return, your spouse) get tips at work not fully reported to the employer, or noncash tips? (24) | i1040gi p. 24 line 1c; "tickets" stays in help |
| `scope.household_pay` | 34 | In 2025, were you (or, on a joint return, your spouse) paid by a household for work in its home, with no W-2? (22) | examples stay in help |
| `scope.contractor_pay` | 33 | In 2025, did a firm pay you (or, on a joint return, your spouse) as a contractor when you believe you were its employee? (24) | the no-withholding condition stays in help, as on the label; **owner judgment** |
| `scope.wages_no_form` | 30 | In 2025, did an employer pay you (or, on a joint return, your spouse) other wages for which you have no W-2? (22) | "other" relies on the sibling boxes |
| `sd.qof` | 35 | Did you (or, on a joint return, your spouse) hold an opportunity zone fund (QOF) in 2025, or put a 2025 gain into one? (24) | i1040sd p. 1, Form 8997 |

Not drafted, for lack of time: `k1p.t6`, `k1p.t4`, `k1s.disposed`, `k1s.box16ef`, `k1p.r_b14bc` and
`k1s.basis_carry`. Each is 1 to 10 words over, and the frame ("On this Schedule K-1 (Form 1065) — ", 6 words)
accounts for much of it. Help over 40 in the MFS, HSA and AMT rows is not drafted either.

---

## 3. Personas 21 and 22: answers to add

**21_money_back_itemizer.** The story: one W-2, a 2024 itemizer who got back 2024 state income tax and property tax,
an NOL from a small business closed in 2023 [C interview/2025/personas/21_money_back_itemizer.yaml:2].

| question | answer | reason from the story |
|---|---|---|
| `refund.box8` | false | A wage earner's state income tax refund, not a tax on business income only |
| `refund.other_year` | false | "2024 state income tax" |
| `refund.paid_other_time` | false | Tax was taken from 2024 pay; the help says that counts as paid in 2024 [C wout-after/21:422] |
| `refund.exc_tax` | false | On $90,000 of wages: no AMT, no unused credits, line 16 not zero. Fourth bullet: see the note below |
| `refund.exc_who` | false | 58, files her own 1040, single in 2024 (`refund.status: single`) |
| `refund.you_born` | false | Born 1967 |
| `refund.you_blind` | false | Nothing in the story |
| `scope.passive` | false | The loss is from a business they ran and closed (an NOL), not a passive activity |
| `scope.f8978` | false | No partnership |
| `s179.prior_form` | false | The story names only the NOL as carried |

Add to `who:` so that the fourth `exc_tax` bullet follows from the story: "Their 2024 Schedule A deducted $5,000 of
state income tax and $4,000 of property tax." This matches line 5d of $9,000 [C persona: `refund.line5d_prior_year:
900000`], and the $400 refund is less than the income tax deducted less any sales-tax alternative. The fix lane
must confirm that the values the persona states do not need a 5a answer [I].

**22_refused_old_loss.** `scope.passive: false`, `scope.f8978: false`, `s179.prior_form: false`, for the same
reasons (a W-2 earner with an old NOL from their own business). Discrepancy to check: the persona's `end` says
`s1.nol_before_limit_date_if_nol` [C 22_refused_old_loss.yaml:3], but the walk ended at `s1.nol_pre2018_if_nol`
"as the persona expects" [C wout-after/22:626; walks file:120]. Either the walk maps the name or the file is
stale [I].

**Side finding (N8, from before tonight's work):** `refund.you_born` ("Were you born before January 2, 1960?") is
asked after `person.birth_year`. The form line exists on 66a808c8 [C git grep 66a808c8 refund.yaml:550]. Proposal:
technique 3.3. Derive it from the birth year: true at 1959 or earlier, false at 1961 or later. Ask a narrow
question ("Were you born on January 1, 1960?") only for birth year 1960. The 2024 return's taxpayer is the same
person (`refund.status`); for a 2024 joint return, the spouse's box needs the same treatment if it is asked.

---

## 4. Persona 18: refusal at `sales[nft].special` told at Q110

**Observed** [C wout-after/18_refused_nft_art.md:101-110, 717-723]:
- Q101: the persona answers Yes to `sales[nft].special`.
- Q102-104: proceeds, basis and code are asked; the persona has no answers for them.
- Q105-110: the `sales_rare` screen.
- The refusal is shown only after `sd.qof`.

**N11: yes, a conflict.** "A refusal is told at its topic, plainly, as early as that topic comes, at the question
that names the filer's situation" [C protocol:97-98]. The situation (an NFT of a painting, a collectible) is
named at Q101, and the filer answers four more questions and a whole screen of unrelated boxes after it.
Protocol 3.5 asks for a check "that the refusal arrives on the row's own answer" [C protocol:166-167].

**Mechanism [I, from the form text; confirm with `interview-order`]:**
- The refusal on `sales.special` is the first entry of `sales.one` [C forms/2025/sales.yaml:686-699].
- On the Schedule D path, `sales.one` is read through `sd.count` (sum over sales) [C sd.yaml:373-381].
- `sd.count` refuses first on `sd.other_forms` [C sd.yaml:385-386], which is an `any` over the `sales_rare`
  boxes, the `sd.sold_other` follow-ups, `sd.casualty`, `sd.f2439` and `sd.qof` [C sd.yaml:226-268].
- A line's expression (here, the sum that carries `sales.one`'s refusal) is reached only after the line's own
  gates are settled. That is the behaviour g1-f7b recorded for Schedule 2 line 21 [C g1-f7b.md:154-155] and
  protocol 3.1(a)/(b).
- So the special refusal waits for every `sales_rare` box. `sd.casualty` (order 200) and `sd.f2439` (272) are
  already answered by then [C canonical listing].

**Fix (bank only, no gate or expected-value change):**
- Ask the `sales_rare` screen and its `sd.sold_other` follow-ups before `$sales`, by renumbering `seq` within
  order 274:
  - `sd.sold_other` 1, `sd.sec1256` 2, `sd.condemned` 3, `sd.small_business_stock` 4, `sd.trader_election` 5,
    `sd.qof` 6;
  - `sd.business_property` 7, `sd.installment` 8, `sd.like_kind` 9;
  - `$sales` 10, `sd.route_each` 11, `sales.box` 12, `sales.special` 13, `sales.proceeds` 14,
    `sales.reported_basis` 15, `sales.correct_basis` 16, `sales.code` 17, `sales.wash_loss` 18, `sales.route` 19,
    `sales.aggregate_eligible` 20.
- Then `sd.other_forms` is settled before any sale is entered, and the special refusal should arrive on its own
  answer [I].
- This also follows N7 ("off-ramps first") and 3.6 ("keep the commonest refusals in small early groups"): a QOF
  owner or trader is now refused before typing in sales.
- Step count is the same for every filer. The heading "In 2025, did you have any of these less common sales or
  trades?" reads well before the list of ordinary sales.
- **Check after the change:**
  - persona 18 ends at Q101 with no unanswered sale questions; the `proceeds`/`correct_basis`/`code` problems
    should go away, since they were asked only because the refusal had not yet arrived [I];
  - `tick-groups` passes;
  - the sales coverage rows keep their ends. Rows whose answers list the sale before the boxes may need their
    answers restated (3.7), never their ends.

**Not chosen:** dropping `when: sd.other_forms` from `sd.count`. `sd.count` is the line that refuses on it for a
filer with other forms and no Schedule D sale (the other carriers, lines 4, 5, 6, 11, 12 and 14
[C sd.yaml:1631-1775], may not be read then), so dropping it could lose a refusal. Also not chosen: a new
refusal gate ahead of `sd.other_forms`, which would change the refusal gate id the persona and fixtures expect.

---

## 5. Does 25 words apply to the full prompt behind a tick box, or only to the label?

**Recommendation: apply N10's parent limit to the member's full prompt. The label keeps its own 12-word cap (a
build rule).** Reasons, from the texts:

1. **The full prompt is the question on several real paths, not hidden help.**
   - The CLI asks the members one at a time [C interview/README.md:557-560].
   - "When one member is left it is asked as an ordinary question" [C README:140-141].
   - "Answer this one on its own" shows it as an ordinary question [C README:134-136].
   - After answering, "choosing one reopens that question alone" [C README:138-139].
   On each of these paths the filer reads the full prompt as the parent question, and N10's limit is for
   questions [C protocol:92].
2. **A tick group is presentation only.** "Each member stays its own input with its own prompt, help and
   citation" [C README:557-559]; "Each box is still its own input, recorded and corrected on its own"
   [C protocol:171-172]. Nothing in N10 or 3.6 exempts a member's prompt.
3. **N2 and N10 say where the length should go.** If a member's prompt needs more than 25 words to be right, the
   precision belongs in a child or in its help (an example), "never a longer parent" [C protocol:64, :94-95].
   Section 2.4 shows that every listed member can be brought under 25 without loss once examples move to help.
4. **The label limit is about a different act.** 3.6 asks that a box be passed over "at a glance and be right",
   with the label worded for the person who might wrongly pass over it [C protocol:173-177]. That is a
   12-word glance standard, enforced by the build [C README:593]. It does not replace the question standard.

**Counter-argument, stated fairly:** on the web page the typical filer never reads the full prompt, so its length
costs that filer nothing, and N12 measures steps and the words shown. If the owner gives weight to that, a middle
reading is to treat the full prompt as a child (under 40). Under that reading only `rec.has_other` (41) and
`scope.tips_unreported` (42) are over, as long as the frame is counted. I still recommend 25. The CLI and the
correction path are real; the rewrites cost little; and a prompt held to 25 words also keeps the label honest,
because the label is a summary of the prompt.

**One counting point for the owner:** the walk counts the entry frame. "On this Schedule K-1 (Form 1065) — " is 6
words and "For this person (you, or your spouse on a joint return) — " is 10, so per-entry members start well into
the limit. The protocol does not say whether the frame counts. My proposals count it.

---

## What was not done

- No walk, build or check was run. Every "expected effect" is inferred and needs `draft-walk`, `tick-groups`,
  `interview-coverage` and `test-fixtures` in a fix lane.
- f4137 and two i1040gi quotes were checked against the canonical cite text, not re-read in the archived PDF
  text.
- Tick-member rewrites for six K-1 members and help rewrites for the MFS, HSA and AMT rows are not drafted.
