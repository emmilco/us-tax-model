# Lane notes: 5a (interest, dividends, foreign tax, accounts outside the United States)

Branch `lane/l5a`. Agent: `claude-fable-5-2`, class judgment, tax year 2025, jurisdiction `us`. No paid call and no
model call was made. Form files: `interest`, `div`, `sb`, `ftc`. Bank entries: those files', and (bank only)
`f1040.line3a`, `f1040.tax_exempt_interest`, `qbi.dividends`; I also set the `order` and `seq` of `sd.distributions`
(lane 5b's file; Part 1 of the map puts it in the dividends block) and nothing else of it.

**A successor reads this file top to bottom, then "Not finished, in rank order".**

## Status (kept current)

| Step | State |
|---|---|
| 0. Every bank entry of the lane has its new `order` and a `seq`; boilerplate help deleted | done |
| 1. `sb.foreign_any` taken apart into five plain parents (map rank 1) | done, see "Step 1" |
| 2. `div.any` as a short ownership question, the rare boxes beneath `div.other_boxes` (map ranks 2 and 4) | done, see "Step 2" |
| 3. `$interest`; `sb.unsupported` as `sb.nominee`, `sb.bonds_any`, `sb.bond_special` (map rank 3) | done, see "Step 3" |
| 4. `ftc.taxes` gated (map rank 2, second half) | done, see "Step 4" |
| 5. `sb.line8`, `sb.form5471`, `sb.fbar_required`, `sb.form8938`, `ftc.*` (map rank 5) | wording only; the role splits are not built |

## Order numbers and `seq` (step 0)

| Order | Questions, in `seq` order |
|---|---|
| 270 Interest | `$interest`, `interest.amount`, `interest.penalty` |
| 271 | `f1040.tax_exempt_interest` (reached only where a credit needs it; kept out of 270 so the block is whole) |
| 272 Dividends | `div.any`, `sb.ordinary_dividends` (box 1a), `f1040.line3a` (1b), `sd.distributions` (2a), `div.box2b` to `2f`, `div.box3`, `qbi.dividends` (box 5), `div.box9`, `box10`, `box12`, `box13`, `div.basis_reconciled`: the printed order of Form 1099-DIV |
| 273 Interest and dividends together | `sb.nominee`, `sb.bonds_any`, `sb.bond_special` (asked once interest or dividends are entered) |
| 280 Foreign tax | `ftc.taxes`, `ftc.all_passive`, `ftc.statements`, `ftc.eligible`, `ftc.elect` |
| 285 Outside the United States | `sb.account_any`, `sb.asset_any`, `sb.trust_any`, `sb.company_any`, `sb.territory_any`, then `sb.fbar_required`, `sb.form8938`, `sb.line8`, `sb.form5471`, `sb.line7a` (never asked) |

**A consequence of moving a block later that every lane will meet.** A refusal fixture withholds (`null`) the
answers to questions that came after its refusal in the old order. Moved to 270 to 285, my refusals are now told
after most other questions, so those withheld answers are asked first and the build fails with "missing or repeated
question". I removed the `null` for each such question in the fixture cases the build named (the question then takes
its default; no expected value or refusal changed). These are inputs of other lanes' ids in fixture cases about my
forms. When the lanes merge and the order changes again, some of these questions will again come after the refusal;
the `null` is then simply absent, which the check accepts (a fixture may answer a question that is never asked).
(Inferred, not tested: that an answer to a question never asked is accepted by every check.)

`ftc.carryover` keeps `order: 10` and has no `seq`: it is a child of `s3.foreign_any` and `s3.prior_other_forms`
(the credits lane's questions, order 279 after lane 7b's reorder). At 280 it was asked after every refusal of the
credits rows, which broke thirteen rows of `coverage/credits.yaml`. See "Requests to other lanes".

## Step 1. `sb.foreign_any` (827 words, read by everyone) as five plain parents

**Model (`forms/2025/sb.yaml`).** Five new Bool inputs, each a question asked of everyone:

| Input | The question as stored | Words as a single filer reads it |
|---|---|---|
| `sb.account_any` | At any time in 2025, did you (or, on a joint return, your spouse) have an account in another country (a bank, investment, pension, payment or crypto account), or the power to sign for one? | 28 |
| `sb.asset_any` | At any time in 2025, did you (...) own anything else of value outside the United States, or were you owed money by someone abroad? | 23 |
| `sb.trust_any` | Do you (...) have anything to do with a trust or family foundation that is outside the United States or has a trustee abroad, as the person who set it up, gave to it, or may receive from it? | 36 |
| `sb.company_any` | In 2025, were you (...) a director, officer or manager of a company set up outside the United States, or an owner, alone or with your family, of 10% or more of one? | 31 |
| `sb.territory_any` | At any time in 2025, did you (...) have an account, an investment, a company or a trust in Puerto Rico, Guam or another U.S. territory? | 24 |

- `sb.foreign_any` is no longer an input. It is a derived line, true when any of the five is true (map 4.1, point 2:
  the technique builds). `sb.fbar_required_if_foreign` and `sb.form8938_if_foreign` still gate on it: a foreign
  account report and Form 8938 can be due for any of the five (an account of a trust or of a company the person
  controls; an interest in a foreign entity is a specified asset), so those two children are asked after any Yes,
  exactly as today.
- `sb.line8_if_foreign` now gates on the new derived line `sb.foreign_trust_any` (`sb.trust_any` or
  `sb.territory_any`), and `sb.form5471_if_foreign` on `sb.foreign_company_any` (`sb.company_any` or
  `sb.territory_any`). A person with only a bank account abroad is no longer asked the trust question (204 words) and
  the Form 5471 question (109 words). The four refusal gates keep their ids and their refusal texts.
- `sb.territory_any` exists because the old question counted a bank, a company and a trust in a U.S. territory as
  foreign for Form 8938, line 8 and Form 5471, and "another country" does not say Puerto Rico to anyone. A Yes opens
  all four children.
- `sb.line7a` is untouched. It is an input that no target reaches (the umbrella design said so; the walks confirm it
  is never asked). The map placed `sb.account_any` "above `sb.line7a`"; there is nothing to place it above.

**Who could answer each parent No wrongly, and the guard** (my analysis from the old question's bullets; no review
was run; this is review debt):

| Wrong No | Guard |
|---|---|
| Signature authority only (an employer's or a relative's account) | In the parent's words: "or the power to sign for one"; help names the employer and the relative |
| An account closed early in 2025, or with little in it | Parent: "at any time in 2025"; help |
| A balance with a payment service, crypto exchange or betting site abroad; a foreign pension | Named in the parent's parenthesis ("pension, payment or crypto account"). A betting or precious-metals account is caught only if the filer reads `sb.asset_any` ("anything else of value") as covering it: **weak; a candidate for one more question** |
| A cash-value policy of a foreign insurer; shares of a foreign company held outside a U.S. account; a loan to a relative abroad; an heir of an estate abroad | `sb.asset_any` is the second question; these four are its help's examples. **Help carrying the guard is against Part 4.5**; the remedy by the norms is one question each (see "Not finished") |
| A U.S.-law trust with a trustee abroad; a foundation, a waqf | "or has a trustee abroad" is in the parent; foundation in the parent; Stiftung, Anstalt, waqf in help |
| A trust the filer only benefits from | "or may receive from it" in the parent |
| 10% counting family shares | "alone or with your family" in the parent; the exact attribution in the child `sb.form5471` |
| A manager (not a director) of an employer's foreign subsidiary | "director, officer or manager" in the parent; the subsidiary in help |
| Anything in Puerto Rico, Guam or another territory | `sb.territory_any` |
| What is held through an LLC, a living trust or a company the filer controls ("directly or indirectly" in the old opening) | **Not guarded.** No parent says "count what a company or trust you control holds". A filer who thinks of the LLC's account as the LLC's answers No. Candidate child: after all five Nos nothing is asked, so it needs a sixth question ("Does a company, partnership or trust that you control have any of these?"); not built |
| Accounts of a child whose income is on the parent's return (Form 8814) | Handed to lane 9 (`scope.f8814` refuses; map 2.7). Until that lands on this branch the bullet is asked by no question here; `scope.other_line16` still refuses Form 8814 |

**Cost and share (NORMS section 3; costs are my estimates, shares from `gate_frequencies.yaml` where marked gf).**

| Question | Share answering Yes | Cost of No | Cost of Yes | Children's cost C | Pays (g < q·C)? |
|---|---|---|---|---|---|
| `sb.foreign_any` today | 2.5% gf (`foreign_accounts`) | 20 (827 words) | 20 | 60 (four screens) | It did, at a cost of 20 to everyone |
| `sb.account_any` | 2.5% gf | 1 | 1 | 40 (FBAR, Form 8938) | Yes: 1 < 0.975 × 40 |
| `sb.asset_any` | 1% (judgment) | 2 | 5 | 40 | Yes |
| `sb.trust_any` | 0.1% (judgment; `foreign_trust` gf 0.05% is the refusing share) | 2 | 5 | 20 + 40 | Yes |
| `sb.company_any` | 0.2% (judgment) | 2 | 3 | 15 + 40 | Yes |
| `sb.territory_any` | 1% (judgment) | 1 | 1 | 75 | Yes |

Five questions at a total cost of about 8 replace one at 20. They are five flat questions asked of everyone, which
is the pattern the owner rejected at fourteen; they are listed under "Candidates for one tick-list".

**Order inside 285.** The five parents first (`seq` 1 to 5), then the children: `sb.fbar_required` (6),
`sb.form8938` (7), `sb.line8` (8), `sb.form5471` (9). A child therefore follows its parent after up to four one-line siblings,
not at once. I chose this so the five can be one tick-list screen; with children interleaved the screen would break.

**Fixtures.** `sb.foreign_any` renamed to `sb.account_any` in every fixture input (708 cases); in the 30 cases where
it was true, `sb.trust_any: true` added where the case answers `sb.line8` true and `sb.company_any: true` where it
answers `sb.form5471` true, so that every gate line has the value it had. `defaults.json`: five defaults (false) in
place of one. `engine/src/generate.ts` and `tools/engines/generate_cases.py` set the five (the generator answers
`sb.account_any` yes exactly where it answered `sb.foreign_any` yes, the trust and company parents with their
screens). Profiles `sales.yaml` and `stage4.yaml` list the five. `engine/src/umbrella-what-if.ts` still names
`sb.foreign_any` as a proposed umbrella; it would now throw "already exists" if run (not in the bar; not fixed).

## Step 2. Dividends

**`div.any` (217 words) is now:** "In 2025, did you (or, on a joint return, your spouse) own shares of a company or a
fund outside a retirement account, or get a Form 1099-DIV?" (22 words for a single filer). The line's `label` and
`source` in `div.yaml` are this text. The answer is wider than before (an owner whose shares paid nothing answers
Yes and enters zeros), so no value changes: the amounts decide.

Who could answer No wrongly: a person who sold every share before 2025 and was paid a late dividend, an ESOP
participant paid a dividend in cash, a person with only a brokerage sweep fund. Each receives a Form 1099-DIV, which
is the second half of the question. A dividend with no form, on shares the filer does not think of as owned (held
in a parent's name): the child `sb.ordinary_dividends` asks for "your share of dividends paid in someone else's
name", but only after a Yes: **unguarded for a person who owns no other shares.** Dividends on a Schedule K-1: lane
9's `scope.k1`.

The seven bullets: (1) a Form 1099-DIV: in the parent; (2) stock, fund, ETF, money market fund, REIT: the parent's
"a company or a fund" and help; (3) capital gain, exempt-interest, nondividend and liquidation distributions: boxes
2a, 12, 3, 9, 10, asked beneath; (4) ESOP: the Form 1099-DIV cue; (5) nominee and paid in someone else's name: help
of `sb.ordinary_dividends`, and `sb.nominee` (step 3); (6) a corporation paid personal expenses: the filer owns its
shares, so Yes; then nothing asks for the amount except "ordinary dividends received without a form" in the help of
box 1a: **weak**; (7) foreign company, K-1, no form: owner of shares; `scope.k1`; help.

**New parent `div.other_boxes`** (model change in `div.yaml`): "Look at your (...) Forms 1099-DIV for 2025. Does any
of them show an amount in box 2b, 2c, 2d, 2e, 2f, 3, 9, 10 or 13?" Asked after a Yes to `div.any`. The nine amounts
were each asked before (2b, 2c, 2d, 2f with capital gain distributions; 2e with ordinary dividends; 3, 9, 10, 13 of
every Yes); now only after a Yes here. Gate lines: `div.other_boxes_if_dividends` (a `choose` on `div.any`),
`div.capital_gain_boxes` and `div.ordinary_boxes` (nested `choose`: box 2a or 1a above zero, then the answer). The
nine existing gate lines keep their ids and read these. Box 12 (exempt-interest dividends) is not in the list: it is
common for holders of municipal bond funds and is asked where a credit needs it.

| Question | Share Yes | Cost No | Cost Yes | C | Pays? |
|---|---|---|---|---|---|
| `div.any` today | 21% gf | 5 (217 words) | 5 | | |
| `div.any` now | about 25% (21% gf plus owners with no dividend; judgment) | 1 | 1 | | |
| `div.other_boxes` | 5% of those with a form (judgment) | 3 (a look at the paper) | 3 | 9 amounts at 1 to 2 each, about 12; today 5 to 9 are asked | Yes: 3 < 0.95 × 8 |

Fixtures: `div.other_boxes: true` added to the 82 cases that give one of the nine boxes an amount (or withhold it);
default false; the generator sets it from the boxes.

**Wording (bank only).** `sb.ordinary_dividends`, `f1040.line3a` and `qbi.dividends` are asked by box ("Add up box
1a (total ordinary dividends) of all your Forms 1099-DIV for 2025"), in the printed order of the form. Figures in
their help are from the archive: 61 days (i1040gi, line 3a exception), more than 45 days (i8995, qualified REIT
dividends). `sd.distributions` (box 2a) is lane 5b's entry: its wording is unchanged; it should read "Add up box 2a
(total capital gain distributions) of the same forms" (request to 5b).

## Step 4. Foreign tax: `ftc.taxes` asked only where there can be an amount

`ftc.taxes` asks: "How much foreign tax did you (...) pay in 2025? Add up box 7 of your Forms 1099-DIV, box 6 of
your Forms 1099-INT, and any income tax you paid to another country yourself. Zero if none."

**The map's plan (beneath `s3.foreign_any` alone) is wrong and I did not follow it:** the help of `s3.foreign_any`
tells a fund holder *not* to count foreign tax a fund paid (Form 1099-DIV box 7) unless they once filed Form 1116,
so a No there is the usual answer of exactly the filers who have an amount for `ftc.taxes`.

**Model (`ftc.yaml`).** `ftc.taxes` is gated (`gated_by: ftc.taxes_if_asked`). The new derived line `ftc.asked` is
true when any of three things is: `div.any` is yes (the filer owns shares or has a Form 1099-DIV: box 7),
`sb.interest_total` is above zero (a Form 1099-INT: box 6), or `s3.foreign_any` is yes (the filer paid income tax to
another country). Otherwise the amount is zero and the question is not asked. The three readers of `ftc.taxes`
(`ftc.has_tax`, `ftc.needs1116`, `ftc.limited`) read the gate line. No refusal changed.

Who is no longer asked and could have had an amount: a filer with no shares, no Form 1099-DIV, no interest, who
answers No to "Have you ever paid income tax to another country ...". Foreign tax withheld on a foreign pension or
on rent from property abroad is "income tax paid to another country", so that filer answers `s3.foreign_any` Yes. A
filer whose only foreign tax is on a Schedule K-1 is refused at lane 9's `scope.k1`. I found no one else.

| Question | Share asked | Cost | Notes |
|---|---|---|---|
| `ftc.taxes` today | 100% | 3 (form words; 17 words) | 7% gf enter an amount |
| `ftc.taxes` now | about 45% (34% gf interest, 21% gf dividends, overlapping; judgment) | 2 for a filer holding the forms | not asked of the other 55% |

**Fixtures.** 42 cases enter foreign tax with no dividends, no interest and `s3.foreign_any` false; each gets
`s3.foreign_any: true` ("paid income tax to another country", which is what such a filer did). **This is an input of
the credits lane's id, edited in other forms' fixture files** (`household.json` 16, `ftc.json` 9, `dependent.json`
4, `f1040.json` 3, `s8812.json` 1, class M 4, mutation 5): it is the only truthful opener for a case with no
investments. No expected value or refusal changed. The row `credits.form1116` of `coverage/credits.yaml` now
answers `s3.foreign_any: true` before its foreign tax, and `credits.foreign_none` answers `ftc.taxes: 0`. The
generator sets `s3.foreign_any` on a return with foreign tax and no dividends.

`ftc.all_passive`, `ftc.statements`, `ftc.eligible`, `ftc.elect` |
| 285 Outside the United States | `sb.account_any`, `sb.asset_any`, `sb.trust_any`, `sb.company_any`, `sb.territory_any`, then `sb.fbar_required`, `sb.form8938`, `sb.line8`, `sb.form5471`, `sb.line7a` (never asked) |

**A consequence of moving a block later that every lane will meet.** A refusal fixture withholds (`null`) the
answers to questions that came after its refusal in the old order. Moved to 270 to 285, my refusals are now told
after most other questions, so those withheld answers are asked first and the build fails with "missing or repeated
question". I removed the `null` for each such question in the fixture cases the build named (the question then takes
its default; no expected value or refusal changed). These are inputs of other lanes' ids in fixture cases about my
forms. When the lanes merge and the order changes again, some of these questions will again come after the refusal;
the `null` is then simply absent, which the check accepts (a fixture may answer a question that is never asked).
(Inferred, not tested: that an answer to a question never asked is accepted by every check.)

`ftc.carryover` keeps `order: 10` and has no `seq`: it is a child of `s3.foreign_any` and `s3.prior_other_forms`
(the credits lane's questions, order 279 after lane 7b's reorder). At 280 it was asked after every refusal of the
credits rows, which broke thirteen rows of `coverage/credits.yaml`. See "Requests to other lanes".

## Step 1. `sb.foreign_any` (827 words, read by everyone) as five plain parents

**Model (`forms/2025/sb.yaml`).** Five new Bool inputs, each a question asked of everyone:

| Input | The question as stored | Words as a single filer reads it |
|---|---|---|
| `sb.account_any` | At any time in 2025, did you (or, on a joint return, your spouse) have an account in another country (a bank, investment, pension, payment or crypto account), or the power to sign for one? | 28 |
| `sb.asset_any` | At any time in 2025, did you (...) own anything else of value outside the United States, or were you owed money by someone abroad? | 23 |
| `sb.trust_any` | Do you (...) have anything to do with a trust or family foundation that is outside the United States or has a trustee abroad, as the person who set it up, gave to it, or may receive from it? | 36 |
| `sb.company_any` | In 2025, were you (...) a director, officer or manager of a company set up outside the United States, or an owner, alone or with your family, of 10% or more of one? | 31 |
| `sb.territory_any` | At any time in 2025, did you (...) have an account, an investment, a company or a trust in Puerto Rico, Guam or another U.S. territory? | 24 |

- `sb.foreign_any` is no longer an input. It is a derived line, true when any of the five is true (map 4.1, point 2:
  the technique builds). `sb.fbar_required_if_foreign` and `sb.form8938_if_foreign` still gate on it: a foreign
  account report and Form 8938 can be due for any of the five (an account of a trust or of a company the person
  controls; an interest in a foreign entity is a specified asset), so those two children are asked after any Yes,
  exactly as today.
- `sb.line8_if_foreign` now gates on the new derived line `sb.foreign_trust_any` (`sb.trust_any` or
  `sb.territory_any`), and `sb.form5471_if_foreign` on `sb.foreign_company_any` (`sb.company_any` or
  `sb.territory_any`). A person with only a bank account abroad is no longer asked the trust question (204 words) and
  the Form 5471 question (109 words). The four refusal gates keep their ids and their refusal texts.
- `sb.territory_any` exists because the old question counted a bank, a company and a trust in a U.S. territory as
  foreign for Form 8938, line 8 and Form 5471, and "another country" does not say Puerto Rico to anyone. A Yes opens
  all four children.
- `sb.line7a` is untouched. It is an input that no target reaches (the umbrella design said so; the walks confirm it
  is never asked). The map placed `sb.account_any` "above `sb.line7a`"; there is nothing to place it above.

**Who could answer each parent No wrongly, and the guard** (my analysis from the old question's bullets; no review
was run; this is review debt):

| Wrong No | Guard |
|---|---|
| Signature authority only (an employer's or a relative's account) | In the parent's words: "or the power to sign for one"; help names the employer and the relative |
| An account closed early in 2025, or with little in it | Parent: "at any time in 2025"; help |
| A balance with a payment service, crypto exchange or betting site abroad; a foreign pension | Named in the parent's parenthesis ("pension, payment or crypto account"). A betting or precious-metals account is caught only if the filer reads `sb.asset_any` ("anything else of value") as covering it: **weak; a candidate for one more question** |
| A cash-value policy of a foreign insurer; shares of a foreign company held outside a U.S. account; a loan to a relative abroad; an heir of an estate abroad | `sb.asset_any` is the second question; these four are its help's examples. **Help carrying the guard is against Part 4.5**; the remedy by the norms is one question each (see "Not finished") |
| A U.S.-law trust with a trustee abroad; a foundation, a waqf | "or has a trustee abroad" is in the parent; foundation in the parent; Stiftung, Anstalt, waqf in help |
| A trust the filer only benefits from | "or may receive from it" in the parent |
| 10% counting family shares | "alone or with your family" in the parent; the exact attribution in the child `sb.form5471` |
| A manager (not a director) of an employer's foreign subsidiary | "director, officer or manager" in the parent; the subsidiary in help |
| Anything in Puerto Rico, Guam or another territory | `sb.territory_any` |
| What is held through an LLC, a living trust or a company the filer controls ("directly or indirectly" in the old opening) | **Not guarded.** No parent says "count what a company or trust you control holds". A filer who thinks of the LLC's account as the LLC's answers No. Candidate child: after all five Nos nothing is asked, so it needs a sixth question ("Does a company, partnership or trust that you control have any of these?"); not built |
| Accounts of a child whose income is on the parent's return (Form 8814) | Handed to lane 9 (`scope.f8814` refuses; map 2.7). Until that lands on this branch the bullet is asked by no question here; `scope.other_line16` still refuses Form 8814 |

**Cost and share (NORMS section 3; costs are my estimates, shares from `gate_frequencies.yaml` where marked gf).**

| Question | Share answering Yes | Cost of No | Cost of Yes | Children's cost C | Pays (g < q·C)? |
|---|---|---|---|---|---|
| `sb.foreign_any` today | 2.5% gf (`foreign_accounts`) | 20 (827 words) | 20 | 60 (four screens) | It did, at a cost of 20 to everyone |
| `sb.account_any` | 2.5% gf | 1 | 1 | 40 (FBAR, Form 8938) | Yes: 1 < 0.975 × 40 |
| `sb.asset_any` | 1% (judgment) | 2 | 5 | 40 | Yes |
| `sb.trust_any` | 0.1% (judgment; `foreign_trust` gf 0.05% is the refusing share) | 2 | 5 | 20 + 40 | Yes |
| `sb.company_any` | 0.2% (judgment) | 2 | 3 | 15 + 40 | Yes |
| `sb.territory_any` | 1% (judgment) | 1 | 1 | 75 | Yes |

Five questions at a total cost of about 8 replace one at 20. They are five flat questions asked of everyone, which
is the pattern the owner rejected at fourteen; they are listed under "Candidates for one tick-list".

**Order inside 285.** The five parents first (`seq` 1 to 5), then the children: `sb.fbar_required` (6),
`sb.form8938` (7), `sb.line8` (8), `sb.form5471` (9). A child therefore follows its parent after up to four one-line siblings,
not at once. I chose this so the five can be one tick-list screen; with children interleaved the screen would break.

**Fixtures.** `sb.foreign_any` renamed to `sb.account_any` in every fixture input (708 cases); in the 30 cases where
it was true, `sb.trust_any: true` added where the case answers `sb.line8` true and `sb.company_any: true` where it
answers `sb.form5471` true, so that every gate line has the value it had. `defaults.json`: five defaults (false) in
place of one. `engine/src/generate.ts` and `tools/engines/generate_cases.py` set the five (the generator answers
`sb.account_any` yes exactly where it answered `sb.foreign_any` yes, the trust and company parents with their
screens). Profiles `sales.yaml` and `stage4.yaml` list the five. `engine/src/umbrella-what-if.ts` still names
`sb.foreign_any` as a proposed umbrella; it would now throw "already exists" if run (not in the bar; not fixed).

## Step 2. Dividends

**`div.any` (217 words) is now:** "In 2025, did you (or, on a joint return, your spouse) own shares of a company or a
fund outside a retirement account, or get a Form 1099-DIV?" (22 words for a single filer). The line's `label` and
`source` in `div.yaml` are this text. The answer is wider than before (an owner whose shares paid nothing answers
Yes and enters zeros), so no value changes: the amounts decide.

Who could answer No wrongly: a person who sold every share before 2025 and was paid a late dividend, an ESOP
participant paid a dividend in cash, a person with only a brokerage sweep fund. Each receives a Form 1099-DIV, which
is the second half of the question. A dividend with no form, on shares the filer does not think of as owned (held
in a parent's name): the child `sb.ordinary_dividends` asks for "your share of dividends paid in someone else's
name", but only after a Yes: **unguarded for a person who owns no other shares.** Dividends on a Schedule K-1: lane
9's `scope.k1`.

The seven bullets: (1) a Form 1099-DIV: in the parent; (2) stock, fund, ETF, money market fund, REIT: the parent's
"a company or a fund" and help; (3) capital gain, exempt-interest, nondividend and liquidation distributions: boxes
2a, 12, 3, 9, 10, asked beneath; (4) ESOP: the Form 1099-DIV cue; (5) nominee and paid in someone else's name: help
of `sb.ordinary_dividends`, and `sb.nominee` (step 3); (6) a corporation paid personal expenses: the filer owns its
shares, so Yes; then nothing asks for the amount except "ordinary dividends received without a form" in the help of
box 1a: **weak**; (7) foreign company, K-1, no form: owner of shares; `scope.k1`; help.

**New parent `div.other_boxes`** (model change in `div.yaml`): "Look at your (...) Forms 1099-DIV for 2025. Does any
of them show an amount in box 2b, 2c, 2d, 2e, 2f, 3, 9, 10 or 13?" Asked after a Yes to `div.any`. The nine amounts
were each asked before (2b, 2c, 2d, 2f with capital gain distributions; 2e with ordinary dividends; 3, 9, 10, 13 of
every Yes); now only after a Yes here. Gate lines: `div.other_boxes_if_dividends` (a `choose` on `div.any`),
`div.capital_gain_boxes` and `div.ordinary_boxes` (nested `choose`: box 2a or 1a above zero, then the answer). The
nine existing gate lines keep their ids and read these. Box 12 (exempt-interest dividends) is not in the list: it is
common for holders of municipal bond funds and is asked where a credit needs it.

| Question | Share Yes | Cost No | Cost Yes | C | Pays? |
|---|---|---|---|---|---|
| `div.any` today | 21% gf | 5 (217 words) | 5 | | |
| `div.any` now | about 25% (21% gf plus owners with no dividend; judgment) | 1 | 1 | | |
| `div.other_boxes` | 5% of those with a form (judgment) | 3 (a look at the paper) | 3 | 9 amounts at 1 to 2 each, about 12; today 5 to 9 are asked | Yes: 3 < 0.95 × 8 |

Fixtures: `div.other_boxes: true` added to the 82 cases that give one of the nine boxes an amount (or withhold it);
default false; the generator sets it from the boxes.

**Wording (bank only).** `sb.ordinary_dividends`, `f1040.line3a` and `qbi.dividends` are asked by box ("Add up box
1a (total ordinary dividends) of all your Forms 1099-DIV for 2025"), in the printed order of the form. Figures in
their help are from the archive: 61 days (i1040gi, line 3a exception), more than 45 days (i8995, qualified REIT
dividends). `sd.distributions` (box 2a) is lane 5b's entry: its wording is unchanged; it should read "Add up box 2a
(total capital gain distributions) of the same forms" (request to 5b).

## Foreign tax (bank wording only; the gate was not built)

`ftc.taxes` asks: "How much foreign tax did you (...) pay in 2025? Add up box 7 of your Forms 1099-DIV, box 6 of
your Forms 1099-INT, and any income tax you paid to another country yourself. Zero if none." It is still asked of
everyone. **The map's plan (beneath `s3.foreign_any`) is wrong and I did not follow it:** the help of
`s3.foreign_any` tells a fund holder *not* to count foreign tax a fund paid (Form 1099-DIV box 7) unless they once
filed Form 1116, so a No there is the usual answer of exactly the filers who have an amount for `ftc.taxes`.
The gate I would build (not built; see "Not finished"): ask `ftc.taxes` only when `div.any` is yes, or interest is
listed, or `s3.foreign_any` is yes. Its readers are all in `ftc.yaml`.

`ftc.all_passive`, `ftc.statements`, `ftc.eligible`, `ftc.elect`: reworded from the election's conditions as the
Form 1116 instructions state them (i1116, "Election To Claim the Foreign Tax Credit Without Filing Form 1116").
`ftc.eligible` still asks the filer to vouch for three rules by name (cost 20 for the 7% who reach it).

## The foreign children (bank wording only)

`sb.fbar_required` and `sb.form8938` now state the test in the prompt ($10,000 at any time: fincen114, quoted in the
gate line's cite; $50,000 at year end or $75,000 at any time, $100,000 and $150,000 jointly: i8938, lines 257 to 278
of the archived text, read for filers living in the United States). They still ask "do you have to file", not the
amounts: the tool does not apply the exceptions. `sb.line8` and `sb.form5471` have short prompts over the unchanged
source-faithful lines; each still joins roles with "or" (received from, set up, gave to; officer, director, 10%
owner), which map 2.9 wanted as one child per role.

## Step 3. Interest, and `sb.unsupported` (45 words, nine items in one sentence, cost 20, asked of everyone with interest or dividends)

**Model (`sb.yaml`).** `sb.unsupported` is no longer an input. It is a derived line, true when either of two gate
lines is true, and `sb.unsupported_if_income` (the line every refusal names) is a copy of it, so the refusal's gate
id and text are unchanged. Three new inputs, all asked only when interest, ordinary dividends or capital gain
distributions are above zero (as the old question was):

| Input | Question | Gate |
|---|---|---|
| `sb.nominee` | Does any of the interest or dividends you (...) received in 2025 belong to someone else, for example to the other owner of a joint account who is not your spouse? | `sb.nominee_if_income`; a Yes refuses |
| `sb.bonds_any` (parent) | In 2025, did you (...) own bonds or notes directly (not through a fund), cash in U.S. savings bonds, or receive interest on money you lent or on a property you sold? | `sb.bonds_any_if_income`; refuses nothing |
| `sb.bond_special` | "Does any of these apply to that interest?" and seven bullets (accrued interest paid on a purchase; bond premium or boxes 10 to 13 of Form 1099-INT; original issue discount other than as on Form 1099-OID, or market discount; a contingent payment debt instrument; a seller-financed mortgage; the savings bond exclusion, Form 8815; any other adjustment) | `sb.bond_special_if_bonds` (a `choose` on `sb.bonds_any_if_income`); a Yes refuses |

| Question | Share Yes | Cost No | Cost Yes | C | Pays? |
|---|---|---|---|---|---|
| `sb.unsupported` today | 2% (judgment; gf `schedule_b_special` has the figure) | 20 | 20 | | |
| `sb.nominee` | 1% (judgment) | 2 | 2 | | no parent |
| `sb.bonds_any` | 8% of those with interest or dividends (judgment) | 1 | 2 | 10 (`sb.bond_special`, a list) | Yes: 1 < 0.92 × 10 |

A filer with bank interest reads 28 + 33 words and answers two plain Nos, where they read one sentence of nine tax
terms. **`sb.bond_special` is still a list of seven unrelated items** (86 words); it is reached only after a Yes to
the bonds parent. Map 2.9 wanted each item by its paper; see "Not finished".

Who could answer `sb.bonds_any` No wrongly: the holder of a multi-year certificate of deposit with a Form 1099-OID
who must report a different amount (a bank product, so "bonds or notes" does not say it to them: rare, unguarded);
a holder of bonds inside a brokerage account who thinks of them as "investments" (the word "bonds" is plain).
"Any other adjustment" can concern dividends, which the parent's wording about interest does not reach: unguarded
residual, as the map said ("lane 5a closes it from the Schedule B instructions": not done).

**Fixtures.** `sb.unsupported` renamed `sb.bond_special`; where it was true, `sb.bonds_any: true` added; where it
was withheld (`null`), all three new inputs are withheld. Defaults: three (false). Generator: `sb.nominee` and
`sb.bonds_any` are not drawn; `sb.bonds_any` follows `sb.bond_special`. **The generator's random stream changes**
(the drawn Boolean is now named `sb.bond_special`), so generated returns differ from those of earlier runs; no
check of the bar reads them.

**Wording (bank only).** `$interest`: "Which banks, credit unions or others paid you (...) interest in 2025? List
each one. Leave the list empty if none did." Its help (104 words on what counts as interest: original issue
discount, market discount, contingent payment instruments, seller financing, nominees) is now 38 words; those items
are what `sb.bonds_any` and `sb.nominee` ask. `interest.amount` reads the boxes of Form 1099-INT (1, 3; not 8),
checked against the archived form.

**The order of the refusal entries on `sb.line2`, `sb.line3` and `sb.line6` was changed** (special treatment, FBAR,
Form 8938, line 8, Form 5471; it was special treatment, Form 5471, FBAR, Form 8938, line 8). The interview opens a
block's questions as it reaches each refusal entry, so with the Form 5471 entry second the five parents were asked
company, territory, account, asset, trust. With the FBAR entry second they are asked in `seq` order. No fixture has
two of the four true together with Form 5471 (checked for `mutation.json`; the fixtures check confirms).

## Before and after, from the persona walks

From `docs/provisional/walks/before/` and `after/` (this branch only: every other topic is still in its old order
and wording, so the totals of a persona show only this lane's change). Counted: the questions of this lane's topic
(`$interest`, `interest.*`, `div.*`, `sb.*`, `ftc.*`, `f1040.line3a`, `f1040.tax_exempt_interest`, `qbi.dividends`,
`sd.distributions`) and their prompt words as shown.

| Persona | Before: questions, words | After: questions, words |
|---|---|---|
| `01_single_w2` (nothing in the topic) | 4, 1,080 | 7, 189 |
| `06_investor_loss_carryover` (dividends, no interest) | 14, 1,212 | 15, 364 |
| `04_retired_couple` (bank interest, a fund's dividends) | 22, 1,353 | 19, 537 |
| The whole walk of `01_single_w2` | 86, 6,777 | 89, 5,886 |

The filer with nothing answers three more questions (five foreign questions for one, and no foreign tax question)
and reads 891 fewer words. Each of the seven is one line answered No from what the person knows.

**Where the topic is asked.** In all twelve walks the topic is now asked in one sitting, in this order: interest
payers, each payer's amount and penalty, (tax-exempt interest where a credit needs it), dividends by box, the two
questions on interest and dividends together, foreign tax, the five foreign questions. On this branch it is the last
thing asked, because every other bank entry still has an order number below 100.

**Questions that still arrive away from their place** (seen in the walks):

- `qbi.dividends` (box 5, `seq` 5) is asked after `div.other_boxes` (`seq` 7), not after box 2a: it becomes
  reachable only when the qualified business income deduction is reached. Waiting on the order agent, or on a direct
  target in `full.yaml` (`qbi.dividends_if_ordinary` or the line that reads it).
- `div.box12` (exempt-interest dividends) is asked only where a credit or the social security worksheet needs
  modified income; for the retired couple it arrives in place (after box 2a). (Inferred from the walks: a filer for whom no
  line needs it is not asked.)
- `f1040.tax_exempt_interest` (271) likewise: in place for the retired couple; asked only where needed.
- `ftc.carryover` is asked with the credits lane's foreign questions (order 10 here), not in 280: see requests.

## Ids added, removed, renamed

| Id | What happened |
|---|---|
| `sb.account_any`, `sb.asset_any`, `sb.trust_any`, `sb.company_any`, `sb.territory_any` | new inputs (questions asked of everyone) |
| `sb.foreign_any` | no longer an input or a question; a derived line (any of the five) |
| `sb.foreign_trust_any`, `sb.foreign_company_any` | new derived lines (the gates of `sb.line8` and `sb.form5471`) |
| `sb.nominee`, `sb.bonds_any`, `sb.bond_special` | new inputs (asked with interest or dividends) |
| `sb.nominee_if_income`, `sb.bonds_any_if_income`, `sb.bond_special_if_bonds` | new gate lines |
| `sb.unsupported` | no longer an input or a question; a derived line. `sb.unsupported_if_income` is now a copy of it and still the refusal's gate |
| `div.other_boxes` | new input (asked after a Yes to `div.any`) |
| `div.other_boxes_if_dividends`, `div.capital_gain_boxes`, `div.ordinary_boxes` | new gate lines; the nine box gate lines keep their ids |
| `div.any` | same id, new wording (label and source) |
| `ftc.asked`, `ftc.taxes_if_asked` | new derived line and gate line; `ftc.taxes` is now gated |

**Ids changed from the map:** the map named four parents (`sb.account_any`, `sb.asset_any`, `sb.trust_any`,
`sb.company_any`); I added `sb.territory_any`. The map's parent for `sb.unsupported` ("Do you own bonds, or did you
lend money to a person?") is `sb.bonds_any`; nominee income is `sb.nominee`. `div.other_boxes` and the `ftc` gate
are not in the map.

## Candidates for one tick-list

Heading: **"Money, property and ties outside the United States"**. Five short yes or no facts asked of everyone, with
adjacent `seq` (order 285, `seq` 1 to 5), each recorded as its own answer:

1. `sb.account_any`: an account in another country, or the power to sign for one
2. `sb.asset_any`: anything else of value outside the United States, or money owed by someone abroad
3. `sb.trust_any`: a trust or family foundation outside the United States
4. `sb.company_any`: a director, officer, manager or 10% owner of a company set up outside the United States
5. `sb.territory_any`: an account, investment, company or trust in Puerto Rico, Guam or another U.S. territory

The credits lane's `s3.foreign_any` (279) and lane 9's `scope.foreign_shares` (287) are the same theme and would make
seven; six is the limit the brief gives, so one screen would hold these five and `scope.foreign_shares`, with
`s3.foreign_any` staying with foreign tax.

## Requests to other lanes

- **Lane 7b (order of the credits questions).** Give `ftc.carryover` (my bank entry, left at `order: 10`) the order
  number and a `seq` of the block you give `s3.foreign_any` and its children (279), directly after
  `s3.foreign_any`. I did not move it because its parents are still at order 10 on this branch.
- **Lane 7b or the coordinator.** `s3.foreign_any` now also opens `ftc.taxes` (at 280). Its help says to count a
  fund's foreign tax only if Form 1116 was once filed; that sentence should stay (it is why `ftc.taxes` is also
  opened by `div.any` and by interest).
- **Lane 5b.** `sd.distributions` (your entry): I set `order: 272`, `seq: 4` and nothing else. Wanted wording: "Add
  up box 2a (total capital gain distributions) of the same forms. Zero if none.", with its present help.
- **Lane 9.** The bullet of the old foreign question on a child's accounts (Form 8814) is asked by nothing on this
  branch; map 2.7 gives it to `scope.f8814`. `scope.foreign_shares` at 287 follows my five parents; if a tick-list
  screen is built it belongs on it.
- **Order agent.** `qbi.dividends` needs a direct target to be asked with the other boxes (above). Within a block,
  the order in which a line's `refuses` entries are written decides which questions open first; I reordered mine in
  `sb.yaml` to get the parents in `seq` order, which a rule in the engine would make unnecessary.
- **Every lane, at the merge.** Refusal fixtures about my forms lost five withheld answers each (`s1a.tips`,
  `s1a.overtime`, `s1a.carloan` in the five `stage4.refuse.ftc.*` cases) because those questions are now asked before
  my refusals. After the merge the set of questions asked before a refusal changes again.

## Review debt this lane creates

- Every new question and every reworded one has had no transcription, render, class M, screen, false-no or question
  review. The wrong-No tables above are my own analysis.
- New gates with no adversarial review: `sb.account_any` and the four other foreign parents; `sb.bonds_any`;
  `div.other_boxes`; `ftc.asked`; `div.any` in its wider meaning.
- `gate_frequencies.yaml` has no entry for the new gates (the build did not ask for one).
- Citations: the new `sb` inputs reuse the cite of the question they came from; `div.other_boxes` cites "Instructions
  for Recipient, boxes 1–16" as the box inputs do. None has been checked by the cite check.
- `rendered/`, `canonical/` and `reports/` were rewritten by the build and the checks.
- The generator's random stream changed (step 3). `engine/src/umbrella-what-if.ts` names `sb.foreign_any` as a
  proposed input and would now refuse to run.

## Not finished, in rank order

1. **`sb.bond_special` is still a seven-item list** (reached by the 8% or so who answer the bonds parent Yes). Map
   2.9: one child per item, by the paper where there is one (boxes 10 to 13 of Form 1099-INT; Form 1099-OID; "Did you
   sell a home and lend the buyer the money?"; the Form 8815 wish with "to go on without it, answer No"), and the
   residual closed from the Schedule B instructions. Each child becomes an input in `sb.yaml` and `sb.bond_special` a
   derived line, exactly as `sb.unsupported` was done.
2. **`sb.line8` and `sb.form5471` one child per role** (received from, set up, gave to a foreign trust; officer or
   director, 10% owner). Their prompts are short now; each still joins roles with "or".
3. **The wrong Nos marked weak or unguarded above:** what is held through a company or trust the filer controls; a
   betting or precious-metals account abroad; the four examples that live in the help of `sb.asset_any`; a dividend
   with no form on shares held in another's name; a constructive dividend's amount.
4. **`ftc.eligible`** still asks the filer to vouch for three rules by name. The Form 1116 instructions' lists
   ("Foreign Taxes Not Eligible for a Credit", "Reduction of Foreign Taxes") would give its children; I did not read
   them.
5. **`div.basis_reconciled`** (84 words) and the nine box amounts keep their old wording ("Section 897 ordinary
   dividends, box 2e"): short, named by box, asked with the paper in hand; not reworded.
6. **`f1040.tax_exempt_interest`** (52 words) keeps its wording.
7. **`sb.fbar_required` and `sb.form8938`** ask "do you have to file" with the main threshold stated. Asking the
   amounts and deciding would be a scope change (the tool does not apply the exceptions).

## For the owner

- The foreign topic is five questions where it was one. I judged five one-line Nos cheaper than one 827-word No;
  the count is what you objected to in the credits lane. The tick-list page is what makes it one screen.
- `div.any` now asks what the person owns, so an owner of shares that paid nothing answers Yes and types zeros
  (about four more questions for that filer, who was asked none before).
- A Yes to `sb.territory_any` (an account in Puerto Rico) leads to four hard questions (FBAR, Form 8938, the trust
  and the company question). The old question did the same; it is more visible now.
- I changed the order of refusal entries in `sb.yaml` and set `s3.foreign_any: true` in 42 fixture cases of other
  forms; both are described above and neither changed an expected value.

## What I ran and saw, and what I infer

**Ran and saw** (on the tree of the commit before the last one, 2026-11-13, machine under heavy load):
`tools/draft_check.sh` in full: build OK; test-fixtures 1854/1854; interview-rules 0 problems; interview-coverage 0
problems (106 rows, 27 of them in `investments_foreign.yaml`); person wording report current; spouse-wording,
check and draft-walk self-tests passed; test-integration 718 invocations passed; properties and test-serve passed;
twins 0 problems; **render --check failed** (eight files of `rendered/2025/` stale). I then ran `render` and
`render --check` (passes) and committed the rendered files with `reports/`; the full script was not run a second
time on the final tree, which differs from the checked one only by those generated files and this section.
`draft-walk` over the twelve personas: 0 problems; the before and after figures above are from its transcripts.

**Inferred, not checked:** every wrong-No analysis; every share marked judgment and every cost; that the five
foreign parents and the bonds parent would be answered correctly by real filers; that `qbi.dividends` and
`div.box12` arrive late because of reachability (I read the walks, not `askOrder`); that an answer left in a
fixture for a question that is no longer asked is harmless after the merge; the effect of the generator change on
the differential engines (not run).
